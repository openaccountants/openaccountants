---
name: za-income-tax-tables
description: >
  Year-keyed South African income tax rate tables for individuals and special trusts, for the years of assessment 2023 to 2027, with the current year being the 2027 year of assessment (1 March 2026 to 28 February 2027, written 2026/27). Holds the progressive brackets with base amounts, the primary, secondary and tertiary rebates, the tax thresholds by age, the medical scheme fees tax credits, the section 11F retirement contribution limits, the section 18A donations limit, the interest exemption, the foreign dividend maximum effective rate and the section 10(1)(o)(ii) foreign employment cap, each row linked to the SARS page it was read on. Use for any South African bracket, rebate, threshold or credit lookup, current or prior year, including amended assessments and late returns.
version: 1.1
jurisdiction: ZA
tax_year: 2026
tax_year_notes: "2026-27, the 2027 year of assessment (1 March 2026 to 28 February 2027); prior years 2023 to 2026 kept for amended and late returns"
last_updated: 2026-11-14
depends_on:
  - workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: rates-card
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

For each year of assessment 2023 to 2027: progressive brackets for individuals and special trusts (Income Tax Act 58 of 1962 s 5, read with the annual Rates and Monetary Amounts Act); rebates (s 6); tax thresholds by age; medical scheme fees tax credits (s 6A); the retirement fund contribution deduction limits (s 11F); the donations limit (s 18A); the interest exemption (s 10(1)(i)); the foreign dividend maximum effective rate (s 10B); the foreign employment remuneration exemption cap (s 10(1)(o)(ii)). For YoA 2027 only: how SARS works out the two provisional tax (IRP6) payments and their due dates.

Not covered: company, ordinary trust and turnover tax rates; capital gains tax (see `za-capital-gains-tables`); travel allowance and logbook tables (see `za-travel-allowance-tables`); any other computation rule (the provisional tax payment layout above is SARS's own).

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

The credit for a month is allowed only for a month in which the taxpayer paid the contributions (contributions an employer paid count where the taxpayer was taxed on them as a fringe benefit). For three or more persons the monthly credit is the two-person amount plus the additional amount for each further person: YoA 2026, a member and two dependants is R728 + R246 = R974 a month (SARS IT07 Example 9).

**The credit cannot create a refund.** The medical scheme fees tax credit is a rebate, not a deduction: it is not refundable and cannot exceed the normal tax payable, because it is limited to the tax payable before employees' tax and provisional tax are set off. Any excess is lost; it is not carried forward to a later year (SARS, Guide on the Determination of Medical Tax Credits, Issue 18, para 2.3: https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-IT07-Guide-on-the-Determination-of-Medical-Tax-Credits.pdf).

### Retirement fund contributions (s 11F)

The deduction under s 11F(2) is limited to the least of three amounts:

1. the annual rand cap in the table below (s 11F(2)(a));
2. 27.5% of the higher of remuneration (as defined in paragraph 1 of the Fourth Schedule) and taxable income, each excluding retirement fund lump sum benefits, retirement fund lump sum withdrawal benefits and severance benefits, with taxable income determined before the s 11F and s 18A deductions; a taxable capital gain is included in this taxable income (s 11F(2)(b));
3. taxable income determined before the s 11F deduction and before the inclusion of any taxable capital gain (s 11F(2)(c)). This third limit is the taxable income itself, not 27.5% of it.

Contributions above the limit carry forward to the next year of assessment and are deemed to be contributed in that year. Source for the three limits: SARS, FAQ: What will the effect of CGT be when calculating the deduction for donations, medical and retirement fund contributions? (https://www.sars.gov.za/faq/faq-what-will-the-effect-of-cgt-be-when-calculating-the-deduction-for-donations-medical-and-retirement-fund-contributions/). The SARS Budget Tax Guide summary words the further limit as "the lower of R350 000 or 27.5% of taxable income, before the inclusion of a taxable capital gain"; follow the three limits above, which set out s 11F(2) itself.

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

The interest exemption applies to interest from a South African source (other than from a tax-free investment) earned by a natural person: R23,800 for a person below the age of 65 and R34,500 for a person 65 years or older (SARS, Guide on Income Tax and the Individual 2025/26, para 4.2: https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-IT01-Guide-on-Income-Tax-and-the-Individual.pdf). Interest from a foreign source is not exempt.

Donations above the 10% limit carry forward to the next year as donations to qualifying public benefit organisations. The 20% foreign dividend rate applies to individuals holding less than 10% of the foreign company, and no deductions are allowed against foreign dividends. The 20% rate is what an exempt fraction of 25/45 produces against the 45% top rate (45% x 20/45 = 20%); SARS publishes the rate, not the fraction.

### Foreign employment remuneration exemption cap (s 10(1)(o)(ii))

| YoA | Cap | Applies from | Source |
| --- | --- | --- | --- |
| 2021 onwards, including 2023 to 2027 | R1.25 million per year of assessment | Years of assessment commencing on or after 1 March 2020 | https://www.sars.gov.za/individuals/tax-during-all-life-stages-and-events/foreign-employment-income-exemption/ |

How the cap interacts with the work-day ratio is in `za-foreign-employment-exemption`.

### Provisional tax (IRP6) payments and due dates, YoA 2027

How SARS works out the two compulsory payments on the estimated taxable income for the year (SARS, How to work out amounts due for Provisional Tax, example: https://www.sars.gov.za/types-of-tax/provisional-tax/how-to-work-out-amounts-due-for-provisional-tax-example/):

- **Total tax payable (A):** normal tax on the estimated taxable income, less the s 6 primary, secondary and tertiary rebates, less the s 6A medical scheme fees tax credit, less the s 6B additional medical expenses tax credit.
- **First payment:** half of A (A/2), less the employees' tax deducted from the taxpayer's remuneration during the first period, less foreign tax credits (s 6quat and s 6quin) for the first 6 months. Employees' tax is deducted after halving, not before.
- **Second payment:** A, less the employees' tax deducted from the taxpayer's remuneration during the year, less the first provisional tax payment (if actually paid), less foreign tax credits for the year.
- **Due dates for YoA 2027:** first payment by 31 August 2026 (a Monday); second payment by 26 February 2027, the last business day of February 2027 (28 February 2027 is a Sunday). SARS: the first payment is due within six months of the start of the year of assessment, 31 August if it is a business day, or the last business day before; the second no later than the last business day of February (https://www.sars.gov.za/types-of-tax/provisional-tax/).

The underestimation penalty, the basic amount and who is a provisional taxpayer are in `za-provisional-tax`.

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

### Worked example: SARS Annexure B, YoA 2026

SARS's own example (Guide on Income Tax and the Individual 2025/26, Annexure B): a resident employee under 65, 1 March 2025 to 28 February 2026. Salary R230,000, overtime R17,000 and bonus R25,000 (remuneration R272,000); interest from South African banks R24,000; gross rental income R27,000 with R10,000 of expenses; pension fund contributions R17,250; employees' tax R30,068; provisional tax paid R1,500.

- Exempt interest R23,800, so taxable interest R200.
- Taxable income = R272,000 + R200 + R17,000 - R17,250 = **R271,950** (the pension contribution is within all three s 11F limits).
- Normal tax = R42,678 + 26% x (271,950 - 237,100) = R42,678 + R9,061 = R51,739.
- Less the primary rebate R17,235: R34,504.
- Less employees' tax R30,068 and provisional tax R1,500: **R2,936 due** on assessment.

```oa-check
name: YoA 2026, SARS Annexure B, under 65, taxable income R271,950
inputs:
  remuneration: 272000
  sa_interest: 24000
  interest_exemption: 23800
  rental_income: 27000
  rental_expenses: 10000
  pension_contributions: 17250
  band_floor: 237100
  band_base: 42678
  band_rate: 0.26
  primary_rebate: 17235
  employees_tax: 30068
  provisional_tax: 1500
steps:
  - taxable_income: remuneration + (sa_interest - interest_exemption) + (rental_income - rental_expenses) - pension_contributions
  - normal_tax: band_base + (taxable_income - band_floor) * band_rate
  - net_normal_tax: normal_tax - primary_rebate
  - due: net_normal_tax - employees_tax - provisional_tax
expected:
  taxable_income: 271950.00
  normal_tax: 51739.00
  net_normal_tax: 34504.00
  due: 2936.00
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
| SARS, FAQ: What will the effect of CGT be when calculating the deduction for donations, medical and retirement fund contributions? (last updated 8 March 2021): read for the three s 11F(2) limits and how a taxable capital gain enters each | https://www.sars.gov.za/faq/faq-what-will-the-effect-of-cgt-be-when-calculating-the-deduction-for-donations-medical-and-retirement-fund-contributions/ | 2026-11-14 |
| SARS, Guide on the Determination of Medical Tax Credits (Issue 18): read for para 2.3 (the credit is not refundable and cannot exceed normal tax), para 2.4 (the monthly amounts for YoA 2026) and Examples 7 to 9 | https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-IT07-Guide-on-the-Determination-of-Medical-Tax-Credits.pdf | 2026-11-14 |
| SARS, Guide on Income Tax and the Individual (2025/26): read for the interest exemption (local interest, not from a tax-free investment) and the Annexure B worked example | https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-IT01-Guide-on-Income-Tax-and-the-Individual.pdf | 2026-11-14 |
| SARS, How to work out amounts due for Provisional Tax, example (last updated 19 February 2025): read for the first, second and third period calculations | https://www.sars.gov.za/types-of-tax/provisional-tax/how-to-work-out-amounts-due-for-provisional-tax-example/ | 2026-11-14 |
| SARS, Provisional Tax page: read for the due dates (31 August or the last business day before; the last business day of February) | https://www.sars.gov.za/types-of-tax/provisional-tax/ | 2026-11-14 |
| SARS, Foreign Employment Income Exemption page: read for the R1.25 million cap from years of assessment commencing on or after 1 March 2020 | https://www.sars.gov.za/individuals/tax-during-all-life-stages-and-events/foreign-employment-income-exemption/ | 2026-11-14 |
| Rates and Monetary Amounts and Amendment of Revenue Laws Act 3 of 2026 (GG 54446, 1 April 2026): read for its long title and the sections it amends | https://www.sars.gov.za/legal-lprim-aa-2026-01-rates-and-monetary-amounts-and-amendment-of-revenue-laws-act-3-of-2026-gg-54446-1-april-2026/ | 2026-11-14 |

Not yet confirmed: the s 6(2) age test for the secondary and tertiary rebates (the Income Tax Act text is published through an external legislation service that did not open by script today). The 25/45 foreign dividend fraction is derived from the 20% rate SARS publishes, not read in s 10B.

## Disclaimer

> **General reference only.** This file is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status or local procedures. Do not rely on it to file, pay, amend or take a tax position without review by a qualified professional in South Africa.

> Contributed by Brandon Iverach.
