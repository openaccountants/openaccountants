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


def guide(slug, code="XX"):
    return {"slug": slug, "path": f"skills/international/xx/{slug}.md", "jurisdiction": code, "category": ""}


def check(guides, added=(), deleted=(), covered_by=None):
    return vg.cell_conflicts(cr, guides, {g["path"] for g in added}, set(deleted), lambda g: covered_by or {})


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


class NewSkillCellTest(unittest.TestCase):
    def setUp(self):
        self.old = guide("xx-vat")
        self.new = guide("xx-vat-return")

    def test_occupied_cell_fails(self):
        errors, _ = check([self.old, self.new], added=[self.new])
        self.assertEqual(len(errors), 1)
        self.assertIn("XX VAT already holds xx-vat", errors[0])

    def test_empty_cell_passes(self):
        self.assertEqual(check([self.old, guide("xx-payroll")], added=[guide("xx-payroll")]), ([], []))

    def test_pr_deletes_the_holder(self):
        self.assertEqual(check([self.new], added=[self.new], deleted=[self.old["path"]]), ([], []))

    def test_covered_by_names_the_new_slug(self):
        errors, _ = check([self.old, self.new], added=[self.new], covered_by={"VAT": "xx-vat-return"})
        self.assertEqual(errors, [])

    def test_edit_of_existing_skill_is_not_checked(self):
        self.assertEqual(check([self.old, self.new]), ([], []))

    def test_other_country_is_a_different_cell(self):
        other = guide("yy-vat", "YY")
        self.assertEqual(check([self.old, other], added=[other]), ([], []))

    def test_pseudo_code_is_skipped(self):
        new = guide("eu-vat", "EU")
        self.assertEqual(check([guide("eu-vat-base", "EU"), new], added=[new]), ([], []))

    def test_unclassified_topic_only_warns(self):
        new = guide("xx-tax-calendar")
        errors, warnings = check([self.old, new], added=[new])
        self.assertEqual(errors, [])
        self.assertEqual(len(warnings), 1)


if __name__ == "__main__":
    unittest.main()
