"""Row-by-row figure check (scripts/check-row-sources.py): offline, with fake pages."""
import importlib.util
import os
import unittest

spec = importlib.util.spec_from_file_location(
    "row_sources", os.path.join(os.path.dirname(__file__), "..", "scripts", "check-row-sources.py"))
rs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rs)

A = "https://tax.example.gov/a"
B = "https://tax.example.gov/b"


def skill(*rows, worked=""):
    table = "\n".join(rows)
    return f"## Rates, bands and thresholds\n\n| Item | Value | Source |\n|---|---|---|\n{table}\n\n## Worked cases\n\n{worked}\n"


def pages(**by_url):
    return lambda u: by_url.get(u)


class RowSources(unittest.TestCase):
    def test_figure_on_linked_page_passes(self):
        t = skill(f"| Rate | 5.20% up to $23,000 | [law]({A}) |")
        n, misses, unreadable = rs.check_text(t, pages(**{A: "rate 5.2% of income not over $23000 " * 20}))
        self.assertEqual((n, misses, unreadable), (1, [], []))

    def test_decimal_comma_pages_pass(self):
        t = skill(f"| Rate | 2.25% on EUR 4,050 | [law]({A}) |", f"| Cap | EUR 1,234.56 | [b]({B}) |")
        n, misses, _ = rs.check_text(t, pages(**{A: "taxa 2,25 % peste 4.050 lei " * 30,
                                                  B: "plafond 1\u202f234,56 euros " * 30}))
        self.assertEqual((n, misses), (2, []))

    def test_wrong_figure_still_misses_on_decimal_comma_page(self):
        t = skill(f"| Rate | 2.5% | [law]({A}) |")
        _, misses, _ = rs.check_text(t, pages(**{A: "taxa 2,25 % in 2026 100 lei " * 30}))
        self.assertEqual([m[0] for m in misses], ["2.5%"])

    def test_figure_missing_from_its_own_page_is_a_miss(self):
        t = skill(f"| Rate | 6.5% | [law]({A}) |", f"| Base | $184,500 | [ssa]({B}) |")
        n, misses, _ = rs.check_text(t, pages(**{A: "the rate is 6.5 percent " * 30, B: "base 176,100 " * 40}))
        self.assertEqual(n, 2)
        self.assertEqual([m[0] for m in misses], ["$184,500"])

    def test_figure_on_another_rows_page_does_not_count(self):
        t = skill(f"| Rate | 7% | [a]({A}) |", f"| Other | 3% | [b]({B}) |")
        _, misses, _ = rs.check_text(t, pages(**{A: "seven 3% " * 50, B: "three 3% " * 50}))
        self.assertEqual([m[0] for m in misses], ["7%"])

    def test_same_inherits_the_link_above(self):
        t = skill(f"| Rate | 4% | [a]({A}) |", "| Reduced | 1.5% | same |")
        n, misses, _ = rs.check_text(t, pages(**{A: "4% and 1.5% apply " * 30}))
        self.assertEqual((n, misses), (2, []))

    def test_unreadable_page_is_not_a_miss(self):
        t = skill(f"| Rate | 9% | [a]({A}) |")
        n, misses, unreadable = rs.check_text(t, pages())
        self.assertEqual((n, misses, len(unreadable)), (1, [], 1))

    def test_rate_sheet_decimal_counts_for_percent(self):
        t = skill(f"| Homer | 4.85% | [sheet]({A}) |")
        _, misses, _ = rs.check_text(t, pages(**{A: "Homer City 4.8500000000000001E-2 0.0485 " * 20}))
        self.assertEqual(misses, [])

    def test_statute_and_form_numbers_are_not_figures(self):
        self.assertEqual(rs.figures(f"| Rate | section 79-32,110 Form 1,040 | [a]({A}) |"), [])

    def test_derived_rows_and_zero_are_not_misses(self):
        t = skill(f"| MFS | $125,000 (derived: half of $250,000) | [a]({A}) |", f"| Band | $0 to $10,000 | [a]({A}) |")
        _, misses, _ = rs.check_text(t, pages(**{A: "10,000 joint 250,000 " * 30}))
        self.assertEqual(misses, [])

    def test_worked_cases_are_skipped(self):
        t = skill(f"| Rate | 2% | [a]({A}) |", worked=f"| Tax | $9,999 | [a]({A}) |")
        _, misses, _ = rs.check_text(t, pages(**{A: "2% " * 200}))
        self.assertEqual(misses, [])


if __name__ == "__main__":
    unittest.main()
