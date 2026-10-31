"""Pack states (coverage-report.py) and the one-skill-per-cell PR check (validate-guides.py)."""
import importlib.util
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cr = _load("coverage_report_states", "coverage-report.py")
vg = _load("validate_guides_states", "validate-guides.py")
ji = _load("job_identity_states", "job_identity.py")
WORDS = ji.load_jurisdiction_words()


def guide(slug, code="NL", **extra):
    return {"slug": slug, "path": f"skills/international/x/{slug}.md", "jurisdiction": code, "category": "", **extra}


def check(guides, added=(), deleted=(), covered_by=None):
    return vg.job_conflicts(cr, guides, {g["path"] for g in added}, set(deleted), lambda g: covered_by or {}, WORDS)


class PackStateTest(unittest.TestCase):
    def test_order_of_states(self):
        self.assertEqual(cr.pack_state(["VAT"], ["a"], ["a"]), "needs_writing")
        self.assertEqual(cr.pack_state([], ["a"], ["a"]), "needs_updating")
        self.assertEqual(cr.pack_state([], [], ["a"]), "needs_signature")
        self.assertEqual(cr.pack_state([], [], []), "complete")

    def test_covered_by_keeps_only_the_named_skill_in_scope(self):
        old, named = guide("xx-vat-old"), guide("xx-vat-return")
        scope = cr.required_guides([old, named], {"VAT"}, {"VAT": "xx-vat-return"})
        self.assertEqual(scope, [named])

    def test_report_is_consistent(self):
        rows = cr.build_report()["rows"]
        for r in rows:
            self.assertEqual(r["state"], cr.pack_state(r["missing"], r["outdated"], r["unsigned"]))
            self.assertEqual(r["complete"], not r["missing"] and not r["outdated"])


class JobIdentityTest(unittest.TestCase):
    def test_slug_strips_place_year_and_number(self):
        self.assertEqual(ji.strip_place("nl-vat-return", "NL", WORDS), "vat-return")
        self.assertEqual(ji.strip_place("netherlands-vat-return-2026", "NL", WORDS), "vat-return")
        self.assertEqual(ji.strip_place("ke-income-tax-2", "KE", WORDS), "income-tax")
        self.assertEqual(ji.strip_place("new-york-sales-tax", "US-NY", WORDS), "sales-tax")
        self.assertEqual(ji.strip_place("us-ny-sales-tax", "US-NY", WORDS), "sales-tax")
        self.assertEqual(ji.strip_place("uk-vat-return", "GB", WORDS), "vat-return")

    def test_form_numbers_survive(self):
        self.assertEqual(ji.strip_place("us-form-1040", "US", WORDS), "form-1040")
        self.assertEqual(ji.strip_place("nl-30-percent-ruling", "NL", WORDS), "30-percent-ruling")

    def test_families(self):
        for job in ("vat", "gst", "vat-return", "vat-gst"):
            self.assertEqual(ji.family(job), "vat-gst")
        self.assertEqual(ji.family("corporation-tax"), ji.family("cit"))
        self.assertEqual(ji.family("personal-income-tax"), ji.family("income-tax"))
        self.assertEqual(ji.family("paye"), ji.family("payroll"))


class NewSkillJobTest(unittest.TestCase):
    def assert_fails(self, old, new, code):
        a, b = guide(old, code), guide(new, code)
        errors, _ = check([a, b], added=[b])
        self.assertEqual(len(errors), 1, (old, new))
        self.assertIn(old, errors[0])

    def test_same_job_fails(self):
        self.assert_fails("nl-vat-return", "netherlands-vat-return", "NL")
        self.assert_fails("ke-income-tax", "ke-income-tax-2", "KE")
        self.assert_fails("ke-vat-return", "kenya-vat", "KE")
        self.assert_fails("de-payroll", "germany-payroll", "DE")
        self.assert_fails("mt-cit", "malta-corporate-tax", "MT")

    def test_niche_skill_only_warns(self):
        new = guide("nl-30-percent-ruling")
        errors, warnings = check([guide("nl-income-tax"), new], added=[new])
        self.assertEqual(errors, [])
        niche = guide("nl-vat-margin-scheme")
        errors, warnings = check([guide("nl-vat-return"), niche], added=[niche])
        self.assertEqual(errors, [])
        self.assertEqual(len(warnings), 1)
        self.assertIn("different job", warnings[0])

    def test_declared_job_counts(self):
        old = guide("nl-expat-regime", job="30-percent-ruling")
        new = guide("nl-30-percent-ruling")
        self.assertEqual(len(check([old, new], added=[new])[0]), 1)

    def test_declared_job_cannot_hide_a_matching_name(self):
        old = guide("nl-vat-return")
        new = guide("netherlands-vat-return", job="something-else")
        self.assertEqual(len(check([old, new], added=[new])[0]), 1)

    def test_pr_deletes_the_other_skill(self):
        old, new = guide("nl-vat"), guide("nl-vat-return")
        self.assertEqual(check([new], added=[new], deleted=[old["path"]])[0], [])
        self.assertEqual(check([old, new], added=[new], deleted=[old["path"]])[0], [])

    def test_two_new_skills_in_one_pr_fail_once(self):
        a, b = guide("nl-vat"), guide("nl-vat-return")
        self.assertEqual(len(check([a, b], added=[a, b])[0]), 1)

    def test_edit_of_existing_skill_is_not_checked(self):
        self.assertEqual(check([guide("nl-vat"), guide("nl-vat-return")]), ([], []))

    def test_other_country_passes(self):
        new = guide("de-vat", "DE")
        self.assertEqual(check([guide("nl-vat"), new], added=[new]), ([], []))

    def test_pseudo_code_is_skipped(self):
        new = guide("eu-vat", "EU")
        self.assertEqual(check([guide("eu-vat-2", "EU"), new], added=[new]), ([], []))

    def test_unclassified_topic_only_warns(self):
        new = guide("nl-tax-calendar")
        errors, warnings = check([guide("nl-vat"), new], added=[new])
        self.assertEqual(errors, [])
        self.assertEqual(len(warnings), 1)


class SameJobReportTest(unittest.TestCase):
    def test_a_package_copy_is_not_a_group(self):
        copy = {**guide("nl-vat"), "path": "packages/nl/nl-vat.md"}
        self.assertEqual(ji.same_job_groups([guide("nl-vat"), copy], WORDS), {})

    def test_group_and_report(self):
        groups = ji.same_job_groups([guide("nl-vat"), guide("netherlands-vat-return"), guide("nl-wage")], WORDS)
        self.assertEqual(list(groups), [("NL", "vat-gst")])
        self.assertIn("| NL | vat-gst |", ji.render_report(groups))


if __name__ == "__main__":
    unittest.main()
