"""Pin the ACT and NT payroll tax figures that changed in 2025 and 2026."""

import unittest
from pathlib import Path

AU = Path(__file__).resolve().parents[1] / "skills" / "australia"


def read(name: str) -> str:
    return (AU / name).read_text(encoding="utf-8")


class PayrollTaxTableTest(unittest.TestCase):
    def test_payroll_guide_rows(self) -> None:
        text = read("australia-payroll.md")
        self.assertIn("| ACT | $1,750,000 | 6.75%", text)
        self.assertIn("| NT | $2,500,000 | 5.50%", text)
        self.assertNotIn("| ACT | $2,000,000 |", text)
        self.assertNotIn("| NT | $1,500,000 |", text)

    def test_rates_card_row(self) -> None:
        text = read("au-rates-2026-27.md")
        # Each jurisdiction now has its own sourced row; pin the figures rather
        # than the retired compact summary's punctuation.
        act, = (line for line in text.splitlines() if line.startswith("| Payroll tax ACT |"))
        nt, = (line for line in text.splitlines() if line.startswith("| Payroll tax NT |"))
        self.assertIn("$1.75m annual threshold", act)
        for band in ("above $1.75m to $20m, 6.75%", "above $20m to $50m, 6.85%",
                     "above $50m to $100m, 7.35%", "above $100m to $150m, 7.85%",
                     "above $150m, 8.75%"):
            with self.subTest(band=band):
                self.assertIn(band, act)
        self.assertIn("5.5% below $100m", nt)
        self.assertIn("6.5% at $100m or more", nt)
        self.assertIn("Maximum annual deduction $2.5m", nt)
        self.assertIn("reduced by $1 per $2 above $2.5m and nil at $7.5m", nt)


if __name__ == "__main__":
    unittest.main()
