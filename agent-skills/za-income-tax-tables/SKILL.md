---
name: za-income-tax-tables
description: "Year-keyed South African income tax rate tables for individuals and special trusts, for the years of assessment 2023 to 2027, with the current year being the 2027 year of assessment (1 March 2026 to 28 February 2027, written 2026/27). Holds the progressive brackets with base amounts, the primary, secondary and tertiary rebates, the tax thresholds by age, the medical scheme fees tax credits, the section 11F retirement contribution limits, the section 18A donations limit, the interest exemption, the foreign dividend maximum effective rate and the section 10(1)(o)(ii) foreign employment cap, each row linked to the SARS page it was read on. Use for any South African bracket, rebate, threshold or credit lookup, current or prior year, including amended assessments and late returns."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/za-income-tax-tables"
  jurisdiction: "ZA"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# South Africa: income tax rate tables for individuals, years of assessment 2023 to 2027

Year-keyed rate tables for **natural persons and special trusts**. This file is data only: it states the figures and where they come from. It does not compute tax and does not set out the order of deductions; that belongs to the computation skills that use it (`za-income-tax`). An accountant-approved file with the same tables exists: `income-tax-rate-tables-by-year-of-assessment-2023-to-2027`. Where the two ever differ, the SARS page linked on the row decides.

**Current year:** the 2027 year of assessment, 1 March 2026 to 28 February 2027 (commonly written 2026/27).

## How South African years of assessment are labelled

SARS numbers a year of assessment by the calendar year in which it **ends**. The tax year runs 1 March to the last day of February. So the year ending 28 February 2027 is **YoA 2027**, commonly written "2026/27". Getting this wrong by one year is the single most common error in South African rate lookups. Every table below is keyed by year of assessment.

| Year of assessment | Commonly written | Period |
| --- | --- | --- |
| 2023 | 2022/23 | 1 March 2022 to 28 February 2023 |
| 2024 | 2023/24 | 1 March 2023 to 29 February 2024 |
| 2025 | 2024/25 | 1 March 2024 to 28 February 2025 |
| 2026 | 2025/26 | 1 March 2025 to 28 February 2026 |
| 2027 | 2026/27 | 1 March 2026 to 28 February 2027 |

## Scope

For each year of assessment 2023 to 2027: progressive brackets for individuals and special trusts (Income Tax Act 58 of 1962 s 5, read with the annual Rates and Monetary Amounts Act); rebates (s 6); tax thresholds by age; medical scheme fees tax credits (s 6A); the retirement fund contribution deduction limits (s 11F); the donations limit (s 18A); the interest exemption (s 10(1)(i)); the foreign dividend maximum effective rate (s 10B); the foreign employment remuneration exemption cap (s 10(1)(o)(ii)).

Not covered: company, ordinary trust and turnover tax rates; capital gains tax (see `za-capital-gains-tables`); travel allowance and logbook tables (see `za-travel-allowance-tables`); any computation rule.

## Rates, bands and thresholds

### Progressive brackets

Each band gives the **base amount** payable at the bottom of the band plus the **marginal rate** on the excess above the band floor. Amounts in rand.

**YoA 2027 (2026/27), 1 March 2026 to 28 February 2027**

| Taxable income (R) | Base amount (R) | Rate on excess | Source |
| --- | --- | --- | --- |
| 1 to 245,100 | 0 | 18% | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ |
| 245,101 to 383,100 | 44,118 | 26% above 245,100 | same |
| 383,101 to 530,200 | 79,998 | 31% above 383,100 | same |
| 530,201 to 695,800 | 125,599 | 36% above 530,200 | same |
| 695,801 to 887,000 | 185,215 | 39% above 695,800 | same |
| 887,001 to 1,878,600 | 259,783 | 41% above 887,000 | same |
| 1,878,601 and above | 666,339 | 45% above 1,878,600 | same |

**YoA 2024, 2025 and 2026 (2023/24, 2024/25, 2025/26): one table, unchanged across the three years**

SARS states "No changes" for 2026 and "No changes from last year" for 2025 against the 2024 table.

| Taxable income (R) | Base amount (R) | Rate on excess | Source |
| --- | --- | --- | --- |
| 1 to 237,100 | 0 | 18% | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ |
| 237,101 to 370,500 | 42,678 | 26% above 237,100 | same |
| 370,501 to 512,800 | 77,362 | 31% above 370,500 | same |
| 512,801 to 673,000 | 121,475 | 36% above 512,800 | same |
| 673,001 to 857,900 | 179,147 | 39% above 673,000 | same |
| 857,901 to 1,817,000 | 251,258 | 41% above 857,900 | same |
| 1,817,001 and above | 644,489 | 45% above 1,817,000 | same |

**YoA 2023 (2022/23)**

| Taxable income (R) | Base amount (R) | Rate on excess | Source |
| --- | --- | --- | --- |
| 1 to 226,000 | 0 | 18% | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ |
| 226,001 to 353,100 | 40,680 | 26% above 226,000 | same |
| 353,101 to 488,700 | 73,726 | 31% above 353,100 | same |
| 488,701 to 641,400 | 115,762 | 36% above 488,700 | same |
| 641,401 to 817,600 | 170,734 | 39% above 641,400 | same |
| 817,601 to 1,731,600 | 239,452 | 41% above 817,600 | same |
| 1,731,601 and above | 614,192 | 45% above 1,731,600 | same |

### Rebates (s 6)

Rebates are credits against tax, not deductions from income. The secondary and tertiary rebates are **added** to the primary rebate, not substituted for it.

| YoA | Primary | Secondary (65 and older, added) | Tertiary (75 and older, added) | Source |
| --- | --- | --- | --- | --- |
| 2027 (2026/27) | R17,820 | R9,765 | R3,249 | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ |
| 2026 (2025/26) | R17,235 | R9,444 | R3,145 | same |
| 2025 (2024/25) | R17,235 | R9,444 | R3,145 | same |
| 2024 (2023/24) | R17,235 | R9,444 | R3,145 | same |
| 2023 (2022/23) | R16,425 | R9,000 | R2,997 | same |

### Tax thresholds

The income below which no tax is payable, as SARS publishes it. Each equals the cumulative rebate for the age band divided by 18%.

| YoA | Under 65 | 65 and older | 75 and older | Source |
| --- | --- | --- | --- | --- |
| 2027 (2026/27) | R99,000 | R153,250 | R171,300 | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ |
| 2026 (2025/26) | R95,750 | R148,217 | R165,689 | same |
| 2025 (2024/25) | R95,750 | R148,217 | R165,689 | same |
| 2024 (2023/24) | R95,750 | R148,217 | R165,689 | same |
| 2023 (2022/23) | R91,250 | R141,250 | R157,900 | same |

### Medical scheme fees tax credits (s 6A), per month

SARS words the first two columns as: the taxpayer (or one dependant who is a scheme member where the taxpayer is not); the taxpayer and one dependant (or two dependants). The second column is the combined amount for two persons, so each of the first two persons carries the one-person amount.

| YoA | One person | Taxpayer and one dependant (combined) | Each additional dependant | Source |
| --- | --- | --- | --- | --- |
| 2027 (2026/27) | R376 | R752 | R254 | https://www.sars.gov.za/tax-rates/medical-tax-credit-rates/ |
| 2026 (2025/26) | R364 | R728 | R246 | same |
| 2025 (2024/25) | R364 | R728 | R246 | same |
| 2024 (2023/24) | R364 | R728 | R246 | same |
| 2023 (2022/23) | R347 | R694 | R234 | same |

### Retirement fund contributions (s 11F)

Deduction limited to 27.5% of the greater of remuneration (for employees' tax) and taxable income, both before retirement fund lump sums and severance benefits, and further limited to the lower of the rand cap and 27.5% of taxable income before the inclusion of a taxable capital gain. Excess carries forward to the next year.

| YoA | Percentage | Annual rand cap | Source |
| --- | --- | --- | --- |
| 2027 (2026/27) | 27.5% | R430,000 | https://www.sars.gov.za/budget-tax-guide-2026-online-version-for-printing/ |
| 2026 (2025/26) | 27.5% | R350,000 | https://www.sars.gov.za/budget-tax-guide-21-may-2025/ |
| 2025 (2024/25) | 27.5% | R350,000 | https://www.sars.gov.za/wp-content/uploads/Budget-tax-guide-2024-_.pdf |
| 2024 (2023/24) | 27.5% | R350,000 | https://www.sars.gov.za/budget-2023-tax-guide/ |
| 2023 (2022/23) | 27.5% | R350,000 | https://www.sars.gov.za/budget-tax-guide-2022/ |

### Donations, interest exemption and foreign dividends

| YoA | s 18A donations limit | Interest exemption, under 65 | Interest exemption, 65 and older | Foreign dividends, maximum effective rate | Source |
| --- | --- | --- | --- | --- | --- |
| 2027 (2026/27) | 10% of taxable income | R23,800 | R34,500 | 20% | https://www.sars.gov.za/budget-tax-guide-2026-online-version-for-printing/ |
| 2026 (2025/26) | 10% of taxable income | R23,800 | R34,500 | 20% | https://www.sars.gov.za/budget-tax-guide-21-may-2025/ |
| 2025 (2024/25) | 10% of taxable income | R23,800 | R34,500 | 20% | https://www.sars.gov.za/wp-content/uploads/Budget-tax-guide-2024-_.pdf |
| 2024 (2023/24) | 10% of taxable income | R23,800 | R34,500 | 20% | https://www.sars.gov.za/budget-2023-tax-guide/ |
| 2023 (2022/23) | 10% of taxable income | R23,800 | R34,500 | 20% | https://www.sars.gov.za/budget-tax-guide-2022/ |

Donations above the 10% limit carry forward to the next year as donations to qualifying public benefit organisations. The 20% foreign dividend rate applies to individuals holding less than 10% of the foreign company, and no deductions are allowed against foreign dividends. The 20% rate is what an exempt fraction of 25/45 produces against the 45% top rate (45% x 20/45 = 20%); SARS publishes the rate, not the fraction.

### Foreign employment remuneration exemption cap (s 10(1)(o)(ii))

| YoA | Cap | Applies from | Source |
| --- | --- | --- | --- |
| 2021 onwards, including 2023 to 2027 | R1.25 million per year of assessment | Years of assessment commencing on or after 1 March 2020 | https://www.sars.gov.za/individuals/tax-during-all-life-stages-and-events/foreign-employment-income-exemption/ |

How the cap interacts with the work-day ratio is in `za-foreign-employment-exemption`.

### Edge cases and traps

- **No bracket adjustment for three years.** YoA 2024, 2025 and 2026 share identical brackets, rebates, thresholds and medical credits. This is not a transcription error. Do not "correct" one year to differ.
- **Base amounts must reconcile.** Each band's base amount equals the previous band's base plus the previous band's width times its rate. A table that fails this is wrong.
- **The age test for the rebates.** The earlier version of this file said age at any time during the year of assessment; the usual reading of s 6(2) is the age on the last day of the year of assessment (or the age the person would have reached, if they died during the year). Neither reading was confirmed in the Act text today: ask the client's date of birth and read s 6(2) before relying on the secondary or tertiary rebate near a birthday.
- **Secondary and tertiary rebates add.** A 76-year-old receives all three.
- **Prior-year lookups matter.** Amended assessments, late returns and objections use the rates for the year of assessment concerned, never the current year.
- **The s 11F cap rose for YoA 2027** from R350,000 to R430,000. A skill still quoting R350,000 for 2026/27 is wrong.

### Self-checks

1. **Base-amount reconciliation.** For every band after the first, base(n) = base(n-1) + (floor(n) - floor(n-1)) x rate(n-1). Every year in this file satisfies this.
2. **Threshold reconciliation.** threshold = cumulative rebate / 18%. YoA 2027: 17,820 / 0.18 = 99,000.
3. **Year check.** Confirm the year of assessment, not the calendar year. A return for the year ended 28 February 2027 uses YoA 2027.

### Worked example: under-65 employee, YoA 2027

Taxable income R500,000, under 65, a medical scheme member with one dependant for all 12 months.

- Bracket R383,101 to R530,200, so tax before rebates is R79,998 + 31% x (500,000 - 383,100) = R79,998 + R36,239 = R116,237.
- Less the primary rebate R17,820: R98,417.
- Less the medical scheme fees tax credit for two persons, R752 x 12 = R9,024: **R89,393** normal tax.

```oa-check
name: YoA 2027, taxable income R500,000, under 65, medical credit for two persons
inputs:
  taxable_income: 500000
  band_floor: 383100
  band_base: 79998
  band_rate: 0.31
  primary_rebate: 17820
  mtc_two_persons_month: 752
  months: 12
steps:
  - tax_before_rebates: band_base + (taxable_income - band_floor) * band_rate
  - after_rebate: tax_before_rebates - primary_rebate
  - mtc: mtc_two_persons_month * months
  - normal_tax: after_rebate - mtc
expected:
  tax_before_rebates: 116237.00
  after_rebate: 98417.00
  mtc: 9024.00
  normal_tax: 89393.00
```

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| SARS, Rates of Tax for Individuals: read for the brackets for YoA 2023 to 2027, the rebates and the tax thresholds by age for 2023 to 2027 (page last updated 28 October 2026) | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ | 2026-11-14 |
| SARS, Medical Tax Credit Rates: read for the monthly credits for 2022 to 2027 | https://www.sars.gov.za/tax-rates/medical-tax-credit-rates/ | 2026-11-14 |
| SARS, Budget Tax Guide 2026 (tax pocket guide for 2026/27): read for the s 11F limits (R430,000, 27.5%), s 18A 10%, the interest exemptions, the 20% foreign dividend rate | https://www.sars.gov.za/budget-tax-guide-2026-online-version-for-printing/ | 2026-11-14 |
| SARS, Budget Tax Guide 21 May 2025 (tax rates from 1 March 2025 to 28 February 2026): read for the same items for YoA 2026 | https://www.sars.gov.za/budget-tax-guide-21-may-2025/ | 2026-11-14 |
| SARS, Budget Tax Guide 2024 (tax rates from 1 March 2024 to 28 February 2025): read for the same items for YoA 2025 | https://www.sars.gov.za/wp-content/uploads/Budget-tax-guide-2024-_.pdf | 2026-11-14 |
| SARS, Budget 2023 Tax Guide (tax rates from 1 March 2023 to 29 February 2024): read for the same items for YoA 2024 | https://www.sars.gov.za/budget-2023-tax-guide/ | 2026-11-14 |
| SARS, Budget Tax Guide 2022 (tax rates from 1 March 2022 to 28 February 2023): read for the same items for YoA 2023 | https://www.sars.gov.za/budget-tax-guide-2022/ | 2026-11-14 |
| SARS, Foreign Employment Income Exemption page: read for the R1.25 million cap from years of assessment commencing on or after 1 March 2020 | https://www.sars.gov.za/individuals/tax-during-all-life-stages-and-events/foreign-employment-income-exemption/ | 2026-11-14 |
| Rates and Monetary Amounts and Amendment of Revenue Laws Act 3 of 2026 (GG 54446, 1 April 2026): read for its long title and the sections it amends | https://www.sars.gov.za/legal-lprim-aa-2026-01-rates-and-monetary-amounts-and-amendment-of-revenue-laws-act-3-of-2026-gg-54446-1-april-2026/ | 2026-11-14 |

Not yet confirmed: the s 6(2) age test for the secondary and tertiary rebates (the Income Tax Act text is published through an external legislation service that did not open by script today). The 25/45 foreign dividend fraction is derived from the 20% rate SARS publishes, not read in s 10B.

## Disclaimer

> **General reference only.** This file is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status or local procedures. Do not rely on it to file, pay, amend or take a tax position without review by a qualified professional in South Africa.

> Contributed by Brandon Iverach.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `za-income-tax-tables` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/za-income-tax-tables. If neither is available, confirm every figure against the official source pages cited above before relying on it.
