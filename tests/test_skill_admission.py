"""Real admission functions against fictional files, never legal guidance."""
import contextlib
import importlib.util
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import skill_checks as sc


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validator = load("admission_validator", "validate-guides.py")
examples = load("admission_examples", "check-examples.py")
index = sc._build_index
SOURCE = "## Sources\n\n| Source | URL | Read on |\n|---|---|---|\n| Fictional parser fixture | https://www.revenue.ie/fictional | 2026-11-12 |\n\nNot yet confirmed: None.\n"
EXAMPLE = "```oa-check\nname: Fictional addition\ninputs:\n  a: 2\nsteps:\n  total: a + 3\nexpected:\n  total: 5\n```\n"
ROUTER = "## The method, step by step\n\nLoad the appropriate skill.\n\n## When to refuse or refer\n\nRefer unsupported work.\n\n" + SOURCE


def document(body, fields=""):
    return ("---\nname: fictional-test\ndescription: Fictional parser fixture only, not accounting guidance.\n"
            "jurisdiction: GLOBAL\ncategory: foundation\ntax_year: 2026\ntier: 2\n"
            "last_updated: 2026-11-12\nversion: 0.1\n" + fields + "---\n\n" + body)


class Admission(unittest.TestCase):
    def check(self, text, old="", untouched=False, rel="skills/global/methods/fictional-vat-router.md"):
        class Files:
            extract_frontmatter = staticmethod(index.extract_frontmatter)
            parse_known_keys = staticmethod(index.parse_known_keys)
            guide_files = staticmethod(lambda: [rel])
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            path = root / rel
            path.parent.mkdir(parents=True)
            path.write_text(text)
            errors, warnings = [], []
            def old_source(*args, **kwargs):
                if not old:
                    raise subprocess.CalledProcessError(128, "git show")
                return SimpleNamespace(stdout=old)
            with patch.object(validator, "REPO_ROOT", temp), patch.object(sc, "REPO_ROOT", temp), \
                 patch.object(validator, "body_unchanged_vs_main", return_value=untouched), \
                 patch.object(validator, "check_approval_resets"), \
                 patch.object(validator.subprocess, "run", side_effect=old_source), \
                 contextlib.redirect_stdout(io.StringIO()):
                validator.check_guides(Files, errors, warnings, only_files={rel})
            return errors, warnings

    def test_router_passes_both_admission_and_arithmetic_policy(self):
        text = document(ROUTER, "type: router\n")
        self.assertEqual(self.check(text)[0], [])
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "fictional-vat-router.md"
            path.write_text(text)
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(examples.main(["--require", str(path)]), 0)

    def test_router_with_rates_heading_needs_an_example(self):
        text = document(ROUTER.replace("## When", "## Deadlines and filing\n\nFictional deadline.\n\n## When"), "type: router\n")
        self.assertTrue(any("two_oa_checks" in e for e in self.check(text)[0]))

    def test_non_tax_missing_sources_and_examples_is_rejected(self):
        text = document("Fictional standard with no evidence.\n", "domain: financial-reporting\ntype: situation-rules\nstandard: Fictional standard\neffective_date: 2026-01-01\n")
        errors, _ = self.check(text, rel="skills/global/financial-reporting/fictional-standard.md")
        self.assertTrue(any("sources_read_dates" in e for e in errors))
        self.assertTrue(any("two_oa_checks" in e for e in errors))

    def test_new_shape_gap_blocks_but_unchanged_legacy_gap_warns(self):
        text = document(SOURCE, "type: router\n")
        self.assertTrue(any("canonical_headings" in e for e in self.check(text)[0]))
        errors, warnings = self.check(text + "\nAdded ordinary prose.\n", old=text)
        self.assertEqual(errors, [])
        self.assertTrue(any("canonical_headings" in w for w in warnings))

    def test_removing_previously_present_shape_heading_blocks(self):
        old = document(ROUTER, "type: router\n")
        self.assertTrue(any("canonical_headings" in e for e in self.check(old.replace("## When to refuse or refer", "## Another heading"), old=old)[0]))

    def test_metadata_only_approval_does_not_inherit_old_body_defects(self):
        self.assertEqual(self.check(document("Legacy incomplete body.\n"), untouched=True)[0], [])

    def test_date_domain_and_shape_changes_cannot_claim_the_approval_only_exemption(self):
        old = document(ROUTER, "type: router\ndomain: tax\n")
        self.assertTrue(sc.admission_content_unchanged(old, old.replace("tier: 2", "tier: 1\nreviewed_by: Test Person")))
        for before, after in (("tax_year: 2026", "tax_year: 2015\ntax_year_notes: old material"),
                              ("type: router", "type: computation"), ("domain: tax", "domain: advisory")):
            self.assertFalse(sc.admission_content_unchanged(old, old.replace(before, after)))

    def test_source_metadata_changes_reset_approval_without_inheriting_old_body_defects(self):
        old = document(ROUTER, "type: router\ndepends_on: [workflow-base]\n")
        for before, after in (("name: fictional-test", "name: corrected-test"),
                              ("category: foundation", "category: international"),
                              ("depends_on: [workflow-base]", "depends_on: [another-base]"),
                              ("description: Fictional", "description: Revised fictional")):
            new = old.replace(before, after)
            self.assertTrue(sc.admission_content_unchanged(old, new))
            self.assertFalse(sc.approved_source_unchanged(old, new))

    def test_metadata_only_approval_needs_real_nonfuture_date(self):
        old = document("Legacy incomplete body.\n")
        approved = old.replace("tier: 2", "tier: 1\nreviewed_by: Test Person")
        for date in ("", '\nreviewed_on: "2026-99-01"', "\nreviewed_on: 2999-01-01"):
            errors, _ = self.check(approved.replace("reviewed_by: Test Person", "reviewed_by: Test Person" + date), old=old, untouched=True)
            self.assertTrue(any("reviewed_on" in e for e in errors), date)
        errors, _ = self.check(approved.replace("reviewed_by: Test Person", "reviewed_by: Test Person\nreviewed_on: 2026-01-01"), old=old, untouched=True)
        self.assertEqual(errors, [])

    def test_impossible_bare_yaml_date_is_a_validation_error_not_a_crash(self):
        text = document(ROUTER, "type: router\nreviewed_on: 2026-99-01\n")
        self.assertTrue(any("invalid YAML frontmatter" in e for e in self.check(text)[0]))

    def test_active_non_tax_domain_rejects_new_unofficial_sources(self):
        path = "skills/global/financial-reporting/fictional-standard.md"
        unofficial = SOURCE.replace("www.revenue.ie", "example.com")
        text = document(ROUTER.replace(SOURCE, unofficial), "domain: financial-reporting\ntype: router\nstandard: Fictional standard\neffective_date: 2026-01-01\n")
        self.assertTrue(any("not an official source" in e for e in self.check(text, rel=path)[0]))
        self.assertEqual(sc.source_evidence_regressions(unofficial, unofficial + "\nOther prose.", path, {"domain": "financial-reporting"}), [])

    def test_relabelling_domain_cannot_grandfather_a_newly_unofficial_host(self):
        path = "skills/global/financial-reporting/fictional-standard.md"
        body = ROUTER.replace("www.revenue.ie", "example.com")
        old = document(body, "domain: tax\ntype: router\n")
        new = old.replace("domain: tax", "domain: financial-reporting\nstandard: Fictional standard\neffective_date: 2026-01-01")
        self.assertTrue(sc.source_evidence_regressions(old, new, path, sc.read_frontmatter(new)))

    def test_unverified_figures_are_not_an_escape_from_source_gating(self):
        row = "## Rates, bands and thresholds\n\n| Item | Rate | Source |\n|---|---|---|\n| Fictional rate | 1 | Unverified: unavailable |\n"
        self.assertTrue(sc.source_evidence_regressions("", row))
        self.assertEqual(sc.source_evidence_regressions(row, row + "\nOther prose."), [])
        self.assertEqual(sc.source_evidence_regressions("", SOURCE + "\nNot yet confirmed: fictional rate unavailable.\n"), [])

    def test_method_does_not_require_a_platform_cta(self):
        text = "\n".join("## " + h + "\n\nFictional instructions.\n" for h in sc.METHOD_HEADINGS[:-1]) + EXAMPLE + SOURCE
        self.assertEqual(sc.check_canonical_headings("x.md", text, {"type": "filing-howto"}), [])


class PeriodLabels(unittest.TestCase):
    def test_only_the_named_current_period_exempts_an_old_start_year(self):
        for note in ("old material", "Edited 2026-11-12", "2026 figures apply", "2015-2026", "Retained for 2024-25"):
            self.assertTrue(sc.check_tax_year_current("x.md", "", {"tax_year": 2015, "tax_year_notes": note}), note)
        for note in ("2025-26", "FY 2025/2026", "Retained for 2025–26 returns"):
            self.assertEqual(sc.check_tax_year_current("x.md", "", {"tax_year": 2025, "tax_year_notes": note}), [], note)
        self.assertTrue(sc.check_tax_year_current("x.md", "", {"tax_year": 2025, "tax_year_notes": "Use 2026-27 figures only where labelled"}))


if __name__ == "__main__":
    unittest.main()
