"""Guard the Australian figures corrected in PR 168 and their effective years.

ATO sources checked on 25 September 2026:
https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/super-guarantee
https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/work-related-deductions/cars-transport-and-travel/motor-vehicle-and-car-expenses/expenses-for-a-car-you-own-or-lease/cents-per-kilometre-method

Check source guides only: generated packages may legitimately await publication.
These cases protect specified historical years, not a moving 'current' rate.
"""

from decimal import Decimal
from pathlib import Path
import re
import unittest


GUIDES = Path(__file__).resolve().parents[1] / "skills/international/australia"


class AustralianGuideRegressionTests(unittest.TestCase):
    def line_for(self, name: str, marker: str) -> str:
        text = (GUIDES / name).read_text(encoding="utf-8")
        lines = [line for line in text.splitlines() if marker in line]
        self.assertEqual(len(lines), 1, f"{name}: expected one {marker!r} line")
        return lines[0]

    def test_nfp_super_rates_follow_the_table_years(self) -> None:
        name = "au-not-for-profit.md"
        header = self.line_for(name, "| Item |")
        row = self.line_for(name, "| Super guarantee rate (see au-super-guarantee) |")
        years = [
            cell.strip().replace("\u2013", "-")
            for cell in header.strip("|").split("|")[1:]
        ]
        values = [
            Decimal(cell.strip().removesuffix("%"))
            for cell in row.strip("|").split("|")[1:]
        ]

        self.assertEqual(len(years), len(values), "Every rate needs its own year column")
        self.assertEqual(len(set(years)), len(years), "Year columns must be distinct")
        rates = dict(zip(years, values))
        for year in ("2025-26", "2026-27"):
            with self.subTest(year=year):
                self.assertEqual(rates.get(year), Decimal("12"))

    def test_formation_super_rate_starts_in_2025_26(self) -> None:
        line = self.line_for("australia-formation.md", "**R-AU-F4")
        match = re.search(r"at least\s+([\d.]+)%\s+\((20\d\d)[-\u2013/]+(\d{2})\b", line)
        self.assertIsNotNone(match, "The employer rule must bind its rate to a financial year")
        self.assertEqual(
            (Decimal(match[1]), int(match[2]), int(match[3])),
            (Decimal("12"), 2025, 26),
        )

    def test_nfp_workpaper_dates_the_rate_from_july_2025(self) -> None:
        line = self.line_for("au-not-for-profit.md", "  Super guarantee ")
        match = re.search(r"Super guarantee\s+([\d.]+)%\s+\(from (\d+) Jul(?:y)? (20\d\d)\)", line)
        self.assertIsNotNone(match, "The workpaper must state the rate and its effective date")
        self.assertEqual(
            (Decimal(match[1]), int(match[2]), int(match[3])),
            (Decimal("12"), 1, 2025),
        )

    def test_kilometre_rates_are_bound_to_their_financial_years(self) -> None:
        line = self.line_for("australia-tax-optimization.md", "**Business-use substantiation**")
        matches = re.findall(r"([\d.]+)c/km\s+(?:for|from)\s+(20\d\d)[-\u2013/]+(\d{2})\b", line)
        rates = [(Decimal(rate), int(start), int(end)) for rate, start, end in matches]
        self.assertEqual(rates, [(Decimal("88"), 2025, 26), (Decimal("91"), 2026, 27)])

    def test_kilometre_cap_matches_the_stated_rate_and_distance(self) -> None:
        line = self.line_for("australia-tax-optimization.md", "**Business-use substantiation**")
        rate = re.search(r"([\d.]+)c/km\s+for\s+2025[-\u2013/]+26\b", line)
        cap = re.search(
            r"max\s+([\d,]+)\s+business km\s*=\s*\$([\d,]+(?:\.\d{1,2})?)(?![\d.])",
            line,
        )
        self.assertIsNotNone(rate, "The worked maximum must identify its financial year rate")
        self.assertIsNotNone(cap, "The worked maximum must identify distance and deduction")
        distance = Decimal(cap[1].replace(",", ""))
        deduction = Decimal(cap[2].replace(",", ""))
        self.assertEqual(distance, Decimal("5000"))
        self.assertEqual(deduction, distance * Decimal(rate[1]) / 100)


if __name__ == "__main__":
    unittest.main()
