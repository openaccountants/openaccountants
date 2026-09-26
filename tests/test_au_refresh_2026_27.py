"""Pin the 2026-27 figures in the crypto, rental property and PAYG instalment guides."""

import unittest
from pathlib import Path

AU = Path(__file__).resolve().parents[1] / "skills" / "international" / "australia"


def read(name: str) -> str:
    return (AU / name).read_text(encoding="utf-8")


class Refresh202627Test(unittest.TestCase):
    def test_crypto_rate_scale(self) -> None:
        text = read("au-crypto-tax.md")
        self.assertIn("Individual Marginal Tax Rates (2026-27)", text)
        self.assertIn("| 18,201 -- 45,000 | 15% |", text)
        self.assertNotIn("(2024-25)", text)

    def test_rental_thresholds(self) -> None:
        text = read("au-rental-property.md")
        self.assertIn("| 18,201 -- 45,000 | 15% | $4,020 |", text)
        self.assertIn("| 190,001+ | 45% | -- |", text)
        self.assertIn("$105,000 single or $210,000 family in 2026-27", text)
        self.assertNotIn("above $93,000", text)
        self.assertNotIn("Key Thresholds (2024-25)", text)

    def test_payg_instalment_factors(self) -> None:
        text = read("au-payg-instalments.md")
        self.assertIn("5% for 2026-27", text)
        self.assertIn("$364 a unit from 1 July 2026", text)
        self.assertIn("T7 = $3,150/quarter", text)
        self.assertNotIn("$313 per 28-day period", text)
        self.assertNotIn("GDP uplift factor | 6%", text)


if __name__ == "__main__":
    unittest.main()
