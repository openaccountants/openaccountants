"""Check (c): every rates row is linked or marked unverified, and the counts say which."""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import skill_checks  # noqa: E402


def doc(*rows):
    table = "\n".join(f"| {a} | {b} |" for a, b in rows)
    return f"## Rates, bands and thresholds\n\n| Item | Source |\n|---|---|\n{table}\n"


URL = "https://example.gov/x"


class RatesRows(unittest.TestCase):
    def check(self, text):
        return skill_checks.check_rates_rows_sourced("x.md", text, {}), skill_checks.rates_row_counts(text)

    def test_all_linked_passes(self):
        problems, c = self.check(doc(("VAT", URL), ("Reduced", "same")))
        self.assertEqual(problems, [])
        self.assertEqual((c["total"], c["linked"], c["linked_pct"]), (2, 2, 100.0))

    def test_marked_row_passes_but_is_not_linked(self):
        problems, c = self.check(doc(("VAT", URL), ("Reduced", "**Unverified**: page blocked")))
        self.assertEqual(problems, [])
        self.assertEqual((c["linked"], c["unverified"], c["linked_pct"], c["unverified_pct"]), (1, 1, 50.0, 50.0))

    def test_mark_beats_a_url(self):
        _, c = self.check(doc(("VAT", f"unverified {URL}"),))
        self.assertEqual((c["linked"], c["unverified"]), (0, 1))

    def test_unmarked_row_fails(self):
        problems, c = self.check(doc(("VAT", URL), ("Reduced", "the VAT Act")))
        self.assertEqual(c["missing"], 1)
        self.assertIn("1 of 2", problems[0])
        self.assertIn("50% linked, 0% unverified", problems[0])

    def test_word_inside_a_rule_is_not_a_mark(self):
        problems, c = self.check(doc(("Rate", "47% for unverified payees"),))
        self.assertEqual(c["unverified"], 0)
        self.assertTrue(problems)

    def test_same_inherits_status_never_upgrades(self):
        self.assertEqual(self.check(doc(("A", "the Act"), ("B", "same")))[1]["missing"], 2)
        self.assertEqual(self.check(doc(("A", "unverified"), ("B", "same")))[1]["unverified"], 2)
        self.assertEqual(self.check(doc(("A", "same"),))[1]["missing"], 1)

    def test_same_does_not_cross_tables(self):
        text = doc(("A", URL)) + "\n| Item | Source |\n|---|---|\n| B | same |\n"
        self.assertEqual(self.check(text)[1]["missing"], 1)

    def test_no_table_fails(self):
        problems, c = self.check("## Scope\n\ntext\n")
        self.assertEqual(problems, ["no rates table"])
        self.assertIsNone(c["linked_pct"])


if __name__ == "__main__":
    unittest.main()
