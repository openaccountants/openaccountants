"""Pin the ACT and NT payroll tax figures that changed in 2025 and 2026."""

import unittest
from pathlib import Path

AU = Path(__file__).resolve().parents[1] / "skills" / "international" / "australia"


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
        self.assertIn("ACT 6.75% to 8.75% tiered/$1.75m", text)
        self.assertIn("NT 5.5% (6.5% at $100m+)/$2.5m", text)
        self.assertNotIn("ACT 6.85%/$2m", text)
        self.assertNotIn("NT 5.5%/$1.5m", text)


if __name__ == "__main__":
    unittest.main()
