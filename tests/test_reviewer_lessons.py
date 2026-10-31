from __future__ import annotations

import importlib.util
import os
import sys
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import skill_checks as sc  # noqa: E402

spec = importlib.util.spec_from_file_location("validate_lessons", REPO_ROOT / "scripts" / "validate-guides.py")
validate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validate)


def table(rows, header="| Source | URL | Read on |"):
    return "## Sources\n\n" + header + "\n|---|---|---|\n" + "\n".join(rows) + "\n"


class ReadDates(unittest.TestCase):
    def test_bulk_stamp_warns_but_scoped_rows_pass(self):
        bare = [f"| Page {i} | https://a.gov/{i} | 2026-10-30 |" for i in range(6)]
        scoped = [f"| Act, art. {i} | https://a.gov/{i} | 2026-10-30 |" for i in range(6)]
        self.assertTrue(sc.check_read_date_evidence("x.md", table(bare), {}))
        self.assertEqual(sc.check_read_date_evidence("x.md", table(scoped), {}), [])

    def test_future_and_status_only(self):
        self.assertIn("future", sc.check_read_date_evidence("x.md", table(["| A | https://a.gov | 2999-01-01 |"]), {})[0])
        self.assertTrue(sc.check_read_date_evidence("x.md", table(["| A | https://a.gov | 2026-10-30, HTTP 200 |"]), {}))

    def test_honest_failure_and_law_dates_pass(self):
        text = table([
            "| A | https://a.gov | 2026-10-30 (refused with HTTP 403; not read) |",
            "| Law in force 2027-01-01 | https://a.gov/b | 2026-10-30 |",
        ])
        self.assertEqual(sc.check_read_date_evidence("x.md", text, {}), [])


class Columns(unittest.TestCase):
    def test_misfilled(self):
        self.assertTrue(sc.check_sources_columns("x.md", table(["| A | 2026-10-30 | https://a.gov |"]), {}))

    def test_good_rows_and_reference_links(self):
        text = table(["| A | https://a.gov | 2026-10-30 |", "| B | [Act][law] | 2026-10-30 |"])
        self.assertEqual(sc.check_sources_columns("x.md", text, {}), [])


class Hosts(unittest.TestCase):
    def test_secondary_authority_and_foreign(self):
        fm = {"jurisdiction": "FR"}
        self.assertTrue(sc.check_source_hosts("fr-x.md", table(["| Rates | https://taxsummaries.pwc.com/a | 2026-10-30 |"]), fm))
        self.assertTrue(sc.check_source_hosts("fr-x.md", table(["| HMRC manual | https://example.com/a | 2026-10-30 |"]), fm))
        self.assertTrue(sc.check_source_hosts("fr-x.md", table(["| Law | https://www.boe.es/a | 2026-10-30 |"]), fm))

    def test_neighbour_and_treaty_pass(self):
        self.assertEqual(sc.check_source_hosts("mc-x.md", table(["| Law | https://legifrance.gouv.fr/a | 2026-10-30 |"]), {"jurisdiction": "MC"}), [])
        self.assertEqual(sc.check_source_hosts("fr-x.md", table(["| Treaty | https://www.boe.es/a | 2026-10-30 |"]), {"jurisdiction": "FR"}), [])


class Jurisdiction(unittest.TestCase):
    def path(self, tail):
        return str(REPO_ROOT / "skills" / tail)

    def test_indiana_with_rupees(self):
        body = "---\nname: x\n---\n# x\n" + "₹1,00,000 is one lakh. " * 5
        problems = sc.check_jurisdiction_body(self.path("us/states/in/in-income-tax.md"), body, {"jurisdiction": "IN"})
        self.assertEqual(len(problems), 2)

    def test_home_currency_and_portuguese_irs_pass(self):
        body = "# x\n" + "₹1,00,000 " * 9
        self.assertEqual(sc.check_jurisdiction_body(self.path("india/in-x.md"), body, {"jurisdiction": "IN"}), [])
        self.assertEqual(sc.check_jurisdiction_body(self.path("portugal/pt-x.md"), "IRS " * 9, {"jurisdiction": "PT"}), [])


class Years(unittest.TestCase):
    def test_earlier_year_in_url(self):
        text = table(["| Rates 2026 | https://a.gov/tax-rates-2024 | 2026-10-30 |"])
        self.assertTrue(sc.check_year_matches_link("x.md", text, {"tax_year": 2026}))

    def test_publication_year_and_span_pass(self):
        text = table([
            "| Rates 2026 | https://a.gov/rev-proc-2025-32 | 2026-10-30 |",
            "| Rates 2026 | https://a.gov/tax-rates-2025-26 | 2026-10-30 |",
        ])
        self.assertEqual(sc.check_year_matches_link("x.md", text, {"tax_year": 2026}), [])


class MergeRecord(unittest.TestCase):
    LOSER = "---\nname: l\n---\n## Rates\n\n## Penalties\n"
    BODY = "Folds loser-x.\n\n## Moved\n\n| Item | From |\n|---|---|\n| Rates | body |\n\n## Not moved\n\n| Item | Why |\n|---|---|\n| Penalties | duplicate |\n"

    def test_full_record_passes(self):
        self.assertEqual(sc.merge_record_problems("loser-x", self.LOSER, self.BODY), ([], []))

    def test_missing_sections_error(self):
        errors, _ = sc.merge_record_problems("loser-x", self.LOSER, "Merged loser-x, no content lost.")
        self.assertEqual(len(errors), 2)

    def test_unlisted_heading_warns(self):
        body = self.BODY.replace("| Penalties | duplicate |", "| Trigger words | duplicate |")
        errors, warnings = sc.merge_record_problems("loser-x", self.LOSER, body)
        self.assertEqual(errors, [])
        self.assertIn("Penalties", warnings[0])

    def test_validator_wiring(self):
        errors, warnings = [], []
        validate.check_merge_records(errors, warnings, pr_body="nothing", deleted={"skills/x/loser-x.md"}, old_text=lambda _: self.LOSER)
        self.assertEqual(len(errors), 3)
        errors, warnings = [], []
        # On a pull_request run Actions sets GITHUB_EVENT_PATH, so pr_body=None
        # would pick up the real PR body. Clear it to test the no-PR path.
        with mock.patch.dict(os.environ):
            os.environ.pop("GITHUB_EVENT_PATH", None)
            validate.check_merge_records(errors, warnings, pr_body=None, deleted={"skills/x/loser-x.md"})
        self.assertEqual(len(warnings), 1)


if __name__ == "__main__":
    unittest.main()
