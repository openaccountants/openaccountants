"""The seven shapes: a declared ``type:`` changes what the body must hold; no type changes nothing."""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import skill_checks  # noqa: E402

EXAMPLE = "```oa-check\nincome = 100\ntax = income * 0.1\nassert tax == 10\n```\n"


def headings(*names):
    return "".join(f"## {n}\n\ntext\n\n" for n in names)


class SkillTypes(unittest.TestCase):
    def test_no_type_keeps_the_old_rules(self):
        self.assertEqual(skill_checks.check_two_oa_checks("x.md", EXAMPLE, {}), ["1 oa-check block(s), need 2"])
        self.assertEqual(skill_checks.check_rates_rows_sourced("x.md", "no table", {}), ["no rates table"])

    def test_unknown_type_keeps_the_old_rules(self):
        fm = {"type": "essay"}
        self.assertEqual(skill_checks.skill_type(fm), None)
        self.assertEqual(skill_checks.check_two_oa_checks("x.md", "", fm), ["0 oa-check block(s), need 2"])

    def test_rates_card_needs_no_examples_but_a_table(self):
        fm = {"type": "rates-card"}
        self.assertEqual(skill_checks.check_two_oa_checks("x.md", "", fm), [])
        self.assertEqual(skill_checks.check_rates_rows_sourced("x.md", "no table", fm), ["no rates table"])

    def test_router_needs_no_table_and_no_examples(self):
        fm = {"type": "router"}
        self.assertEqual(skill_checks.check_two_oa_checks("x.md", "", fm), [])
        self.assertEqual(skill_checks.check_rates_rows_sourced("x.md", "no table", fm), [])

    def test_filing_howto_needs_one_example(self):
        fm = {"type": "filing-howto"}
        self.assertEqual(skill_checks.check_two_oa_checks("x.md", EXAMPLE, fm), [])
        self.assertEqual(skill_checks.check_two_oa_checks("x.md", "", fm), ["0 oa-check block(s), need 1"])

    def test_computation_still_needs_two(self):
        fm = {"type": "computation"}
        self.assertEqual(skill_checks.check_two_oa_checks("x.md", EXAMPLE, fm), ["1 oa-check block(s), need 2"])

    def test_shape_headings(self):
        fm = {"type": "router"}
        ok = headings("The method, step by step", "When to refuse or refer", "Sources")
        self.assertEqual(skill_checks.check_canonical_headings("x.md", ok, fm), [])
        bad = headings("Sources", "The method, step by step")
        problems = skill_checks.check_canonical_headings("x.md", bad, fm)
        self.assertTrue(problems and problems[0].startswith("router set: "))

    def test_situation_rules_accepts_either_canonical_set(self):
        fm = {"type": "situation-rules"}
        text = headings(*skill_checks.CANONICAL_HEADINGS)
        self.assertEqual(skill_checks.check_canonical_headings("x.md", text, fm), [])

    def test_type_declared(self):
        self.assertEqual(skill_checks.check_type_declared("x.md", "", {"type": "decision"}), [])
        self.assertTrue(skill_checks.check_type_declared("x.md", "", {}))
        self.assertTrue(skill_checks.check_type_declared("x.md", "", {"type": "single_select"}))


if __name__ == "__main__":
    unittest.main()
