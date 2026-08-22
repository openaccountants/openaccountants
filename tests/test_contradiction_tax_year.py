"""Tests for contradiction-scanner tax-year selection and binding."""

from __future__ import annotations

import importlib.util
import json
import re
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "detect-contradictions.py"
SPEC = importlib.util.spec_from_file_location("detect_contradictions", SCRIPT)
scanner = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(scanner)

US_FEDERAL = REPO_ROOT / "packages" / "us-federal"


def populated(year: int) -> dict:
    """A canonical rates payload with every required section filled in."""
    return {
        "tax_year": year,
        "valid_as_of": f"{year}-11-15",
        "legislative_basis": "Rev. Proc. 0000-00",
        "rates_individual": {
            "standard_deduction": {"single": 15_750, "mfj": 31_500},
            "ordinary_income_brackets": {"single": [[0, 0.10]], "mfj": [[0, 0.10]]},
        },
    }


def skeleton(year: int) -> dict:
    """The December placeholder ANNUAL-UPDATE-RUNBOOK.md mandates creating."""
    payload = populated(year)
    payload["valid_as_of"] = None
    payload["_TODO_valid_as_of"] = "await Rev. Proc."
    payload["rates_individual"]["ordinary_income_brackets"] = {
        "single": None, "mfj": None, "_TODO": "await Rev. Proc."
    }
    return payload


class ContradictionTaxYearTests(unittest.TestCase):
    def test_selects_newest_valid_rate_year(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "rates.2025.json").write_text(
                json.dumps(populated(2025)), encoding="utf-8"
            )
            (root / "rates.2026.json").write_text(
                json.dumps(populated(2026)), encoding="utf-8"
            )
            (root / "rates.latest.json").write_text("not json", encoding="utf-8")

            self.assertEqual(scanner.resolve_tax_year(rates_dir=directory), 2026)
            self.assertEqual(scanner.available_rate_years(directory), [2025, 2026])

    def test_explicit_year_must_have_a_populated_rates_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "rates.2024.json").write_text(
                json.dumps(populated(2024)), encoding="utf-8"
            )
            (root / "rates.2025.json").write_text(
                json.dumps(populated(2025)), encoding="utf-8"
            )

            self.assertEqual(scanner.resolve_tax_year(2024, directory), 2024)
            with self.assertRaisesRegex(ValueError, "positive four-digit"):
                scanner.resolve_tax_year(999, directory)
            # Unvalidated, this bound every undated claim to a year no sentence
            # or frontmatter year could ever join.
            with self.assertRaisesRegex(
                ValueError, r"2042 has no populated canonical rates file"
            ):
                scanner.resolve_tax_year(2042, directory)

    def test_missing_rate_directory_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "no valid rates"):
                scanner.resolve_tax_year(rates_dir=directory)

    def test_malformed_or_mismatched_canonical_rate_file_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "rates.2025.json").write_text(
                json.dumps(populated(2025)), encoding="utf-8"
            )
            (root / "rates.2026.json").write_text("not json", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, r"invalid JSON.*rates\.2026\.json"):
                scanner.resolve_tax_year(rates_dir=directory)

            (root / "rates.2026.json").write_text(
                json.dumps(populated(2025)), encoding="utf-8"
            )
            with self.assertRaisesRegex(ValueError, r"rates\.2026\.json.*tax_year 2026"):
                scanner.resolve_tax_year(rates_dir=directory)

    def test_zero_canonical_rate_year_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            (Path(directory) / "rates.0000.json").write_text(
                json.dumps({"tax_year": 0}), encoding="utf-8"
            )
            with self.assertRaisesRegex(ValueError, "positive four-digit"):
                scanner.resolve_tax_year(rates_dir=directory)

    def test_frontmatter_year_wins_and_missing_year_uses_default(self) -> None:
        compiled = scanner.compile_concepts()
        stats = {
            "claims": 0,
            "multivalue_lines_skipped": 0,
            "ambiguous_year_dropped": 0,
            "historical_dropped": 0,
        }

        def claim(frontmatter_year: str) -> dict:
            text = (
                "---\nname: test\njurisdiction: DE\ncategory: international\n"
                f"{frontmatter_year}---\n\n# Rules\nThe Grundfreibetrag is EUR 12,000.\n"
            )
            return scanner.extract_claims(
                "synthetic.md", text, "DE", compiled, stats, 2026
            )[0]

        self.assertEqual(claim("")["year"], 2026)
        self.assertEqual(claim("tax_year: 2025\n")["year"], 2025)


class CanonicalRatesPopulationTests(unittest.TestCase):
    """A rates file only binds a year once it actually carries figures."""

    def test_unpopulated_skeleton_is_skipped_not_selected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "rates.2025.json").write_text(
                json.dumps(populated(2025)), encoding="utf-8"
            )
            (root / "rates.2026.json").write_text(
                json.dumps(skeleton(2026)), encoding="utf-8"
            )

            self.assertEqual(scanner.available_rate_years(directory), [2025])
            self.assertEqual(scanner.resolve_tax_year(rates_dir=directory), 2025)

    def test_todo_marker_anywhere_disqualifies_a_rates_file(self) -> None:
        payload = populated(2026)
        payload["rates_individual"]["_TODO_amt"] = "await Rev. Proc."

        self.assertFalse(scanner.is_populated_rates(payload))

    def test_null_required_leaf_disqualifies_a_rates_file(self) -> None:
        payload = populated(2026)
        payload["legislative_basis"] = None

        self.assertFalse(scanner.is_populated_rates(payload))

    def test_all_null_required_branch_disqualifies_a_rates_file(self) -> None:
        payload = populated(2026)
        payload["rates_individual"]["ordinary_income_brackets"] = {
            "single": None, "mfj": None, "mfs": None, "hoh": None,
        }

        self.assertFalse(scanner.is_populated_rates(payload))


class BindingYearWindowTests(unittest.TestCase):
    """The binding window must move with the anchor, not expire on a literal."""

    def test_window_follows_the_resolved_year(self) -> None:
        for anchor in (2025, 2028, 2031):
            with self.subTest(anchor=anchor):
                window = scanner.binding_years(anchor)
                self.assertIn(anchor - 1, window)
                self.assertIn(anchor, window)
                self.assertIn(anchor + 1, window)

    def test_prose_binds_at_an_anchor_the_old_literal_range_excluded(self) -> None:
        """A fixed range(2023, 2028) made sentence_years() return nothing here,
        so no prose could bind and claims fell away with no signal."""
        window = scanner.binding_years(2028)

        self.assertEqual(
            scanner.sentence_years("The 2028 threshold is USD 1,000.", window), {2028}
        )


class RealPackagesTreeTests(unittest.TestCase):
    """Behaviour on the corpus the scanner actually reads.

    Every other test here builds its own temporary tree, which is why the
    migration of 157 of 196 packages/us-federal claims from 2025 to 2026 got
    through CI: nothing looked at the real guides.
    """

    #: The coverage year each guide states in its own frontmatter description
    #: ("Covers tax year 2025 under OBBBA ..."). An independent signal from the
    #: one content_tax_year derives, so this is a check and not a restatement.
    STATED_YEAR_RE = re.compile(r"tax year\s+(20\d\d)", re.IGNORECASE)

    def _guides(self) -> list[Path]:
        guides = sorted(US_FEDERAL.glob("*.md"))
        self.assertTrue(guides, "packages/us-federal has no guides to check")
        return guides

    def _stated_year(self, text: str) -> int | None:
        """The single coverage year a guide declares, or None if it declares none."""
        frontmatter = text.split("---", 2)[1] if text.startswith("---") else ""
        stated = set(self.STATED_YEAR_RE.findall(frontmatter))
        return int(stated.pop()) if len(stated) == 1 else None

    @staticmethod
    def _fresh_stats() -> dict:
        return dict.fromkeys(
            ("claims", "multivalue_lines_skipped",
             "ambiguous_year_dropped", "historical_dropped"), 0
        )

    def test_us_federal_guides_carry_no_frontmatter_tax_year(self) -> None:
        """The premise the rest of this class rests on; assert it, don't assume."""
        tagged = [
            g.name for g in self._guides()
            if re.search(r"^tax_year:", g.read_text(encoding="utf-8"), re.MULTILINE)
        ]

        self.assertEqual(tagged, [])

    def test_untagged_guides_bind_to_the_year_they_say_they_cover(self) -> None:
        default = scanner.resolve_tax_year()
        binding = scanner.binding_years(default)
        checked = 0
        for guide in self._guides():
            text = guide.read_text(encoding="utf-8")
            stated = self._stated_year(text)
            if stated is None:
                continue  # this guide declares no single coverage year
            checked += 1
            with self.subTest(guide=guide.name):
                self.assertEqual(
                    scanner.content_tax_year(text, default, binding), stated,
                    f"{guide.name} binds to a year other than the one it covers",
                )
        self.assertGreater(checked, 20, "expected most guides to state their year")

    def test_a_future_default_never_drags_undated_claims_forward(self) -> None:
        """The structural regression, exercised through extract_claims.

        Once next year's rates file is populated the default year advances, but
        a guide whose prose is still this year's must not advance with it, or a
        real drift against its twin in skills/federal silently stops being
        reported.
        """
        compiled = scanner.compile_concepts()
        ahead = scanner.resolve_tax_year() + 1
        checked = 0
        for guide in self._guides():
            text = guide.read_text(encoding="utf-8")
            stated = self._stated_year(text)
            if stated is None:
                continue
            claims = scanner.extract_claims(
                str(guide), text, "US", compiled, self._fresh_stats(), ahead
            ) or []
            inferred = {c["year"] for c in claims if not c["year_explicit"]}
            if not inferred:
                continue
            checked += 1
            with self.subTest(guide=guide.name):
                self.assertEqual(
                    inferred, {stated},
                    f"{guide.name} binds undated claims away from tax year {stated}",
                )
        self.assertGreater(checked, 10, "expected real undated claims to check")

    def test_a_skeleton_rates_file_never_becomes_the_default_year(self) -> None:
        """ANNUAL-UPDATE-RUNBOOK.md has next year's skeleton created in December,
        before the markdown is refreshed, so max(rates year) structurally leads
        the content every year unless skeletons are excluded."""
        rates = sorted(US_FEDERAL.glob("rates.*.json"))
        self.assertTrue(rates, "packages/us-federal has no canonical rates files")
        canonical = scanner.available_rate_years()
        for path in rates:
            year = int(path.name.split(".")[1])
            payload = json.loads(path.read_text(encoding="utf-8"))
            with self.subTest(rates=path.name):
                self.assertEqual(
                    scanner.is_populated_rates(payload), year in canonical
                )


if __name__ == "__main__":
    unittest.main()
