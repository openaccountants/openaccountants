---
name: za-income-tax-tables
description: >
  South African individual income tax brackets, rebates, age thresholds and
  medical scheme fees tax credits for years of assessment 2023 to 2027.
  Includes personal interest exemptions, provisional-payment calculations and
  two worked examples. Refers retirement deductions, donations, foreign
  dividends and foreign employment exemption questions to a partner accountant.
version: 1.3
jurisdiction: ZA
tax_year: 2026
tax_year_notes: "2026-27, the 2027 year of assessment (1 March 2026 to 28 February 2027); prior years 2023 to 2026 kept for amended and late returns"
last_updated: 2026-11-26
depends_on:
  - workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: rates-card
---

# South Africa: individual income tax tables, years of assessment 2023 to 2027

## Scope

Use the **year of assessment**, not the calendar year of filing. An ordinary individual year runs from 1 March to the last day of February; YoA 2027 is 1 March 2026 to 28 February 2027. Prior-year returns use their own year's column. Source: [SARS individual guide, section 2](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-IT01-Guide-on-Income-Tax-and-the-Individual.pdf).

The progressive brackets cover ordinary taxable income of individuals and special trusts; retirement fund lump sum benefits, withdrawal benefits and severance benefits have separate tables. Special trusts do not receive the personal rebates or medical credits below; the age thresholds and interest exemptions here are for individuals. See [SARS trusts FAQ](https://www.sars.gov.za/businesses-and-employers/trusts/trust-frequently-asked-questions-faqs/).

**Current-year basis, read 26 November 2026:** the 2027 brackets, rebates and medical credits below are SARS's published Budget amounts. Budget-announced changes have temporary effect for 12 months from their announced dates, subject to Parliament passing the implementing legislation within that period: Income Tax Act ss 5(2)(b), 6(6)(b) and 6A(5)(b), as enacted by [Act 23 of 2018, ss 3–5](https://www.sars.gov.za/wp-content/uploads/Legal/AmendActs/LAPD-LPrim-AA-2018-03-Taxation-Laws-Amend-Act-23-of-2018-GG-42172.pdf). [SARS still lists B34–2026 as a Bill](https://www.sars.gov.za/legal-counsel/preparation-of-legislation/bills/); this Guide does not describe it as an enacted Act. For use after that temporary period, check the implementing Act with one of our partner accountants.

## Ask the client first

Confirm the year, individual or special-trust status, date of birth, ordinary or shortened year, ordinary income versus lump sums, qualifying medical contributions and covered persons by month, shared contributions, and tax already paid. This card does not determine taxable income or eligibility for a deduction. Use `za-income-tax` for computation, `za-capital-gains-tables` for gains and `za-travel-allowance-tables` for travel; company, ordinary-trust and turnover-tax rates are outside this card.

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

### Rebates (s 6): subtract from tax, not income

Amounts in rand. The primary rebate applies first; add the secondary at age 65 and the tertiary at age 75. Use age on the last day of the year, including the age the taxpayer would have reached had they lived: [Act 19 of 2023, s 3](https://www.sars.gov.za/wp-content/uploads/Legal/AmendActs/Legal-LPrim-AA-2023-01-Rates-and-Monetary-Amounts-and-Amendment-of-Revenue-Laws-Act-19-of-2023-GG-49948-Notice-4228-22-December-2023.pdf). Thus a 76-year-old qualifies for all three. Short-year rebate apportionment: Check this point with one of our partner accountants.

| Rebate | YoA 2023 | YoA 2024–2026 | YoA 2027 | Official source |
| --- | --- | --- | --- | --- |
| Primary | 16,425 | 17,235 | 17,820 | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ |
| Secondary, additional at 65+ | 9,000 | 9,444 | 9,765 | same |
| Tertiary, additional at 75+ | 2,997 | 3,145 | 3,249 | same |

### Tax thresholds: ordinary full-year individual

These are SARS's published maximum taxable-income amounts giving no normal tax after the age rebates, rather than separate deductions or return-filing exemptions. Rounding cumulative rebate divided by 18% to the nearest rand reproduces the table, including R148,216.67 rounded to R148,217 and R165,688.89 rounded to R165,689 for YoA 2024–2026.

| Age band | YoA 2023 | YoA 2024–2026 | YoA 2027 | Official source |
| --- | --- | --- | --- | --- |
| Under 65 | 91,250 | 95,750 | 99,000 | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ |
| 65–74 | 141,250 | 148,217 | 153,250 | same |
| 75+ | 157,900 | 165,689 | 171,300 | same |

### Medical scheme fees tax credit (s 6A): monthly rand amounts

| Persons covered | YoA 2023 | YoA 2024–2026 | YoA 2027 | Official source |
| --- | --- | --- | --- | --- |
| Taxpayer, or one qualifying dependant where taxpayer is not a member | 347 | 364 | 376 | https://www.sars.gov.za/tax-rates/medical-tax-credit-rates/ |
| Taxpayer plus one dependant, or two qualifying dependants where taxpayer is not a member: combined | 694 | 728 | 752 | same |
| Each further qualifying dependant | 234 | 246 | 254 | same |

Claim only for months for which qualifying contributions are paid to a registered medical scheme or a qualifying equivalent foreign fund. Employer contributions count to the extent included as a taxable benefit. If contributors share the fees, apportion the credit in the ratio each pays. The credit reduces normal tax before PAYE and provisional payments are set off; it cannot exceed that tax, and unused credit neither refunds nor carries forward. Source: [SARS medical guide, sections 2.2–2.5](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-IT07-Guide-on-the-Determination-of-Medical-Tax-Credits.pdf).

For a member and two dependants in YoA 2026, the maximum monthly credit is R728 + R246 = **R974**, limited by normal tax payable. Additional medical expenses credit under s 6B: Check this point with one of our partner accountants.

### Personal interest exemption (s 10(1)(i))

For South African-source interest of an individual, excluding tax-free investment interest dealt with separately. These amounts do not exempt foreign-source interest under this provision.

| Age | Annual exemption, YoA 2023–2027 | Official source |
| --- | --- | --- |
| Under 65 | R23,800 | https://www.sars.gov.za/tax-rates/income-tax/interest-and-dividends/ |
| 65+ | R34,500 | same |

### Retirement fund contribution deductions (s 11F)

Annual caps, remuneration/taxable-income bases, capital-gain and lump-sum exclusions, short-year limits and unused-contribution carryforward: Check this point with one of our partner accountants. The pension deduction in the historical worked case below is an explicit fact of SARS's example, not a general deduction limit.

### Donations deduction (s 18A)

Qualifying receipts, the taxable-income limit and calculation order, lump-sum exclusions and excess-donation carryforward: Check this point with one of our partner accountants.

### Foreign dividends (ss 10B and 23(q))

Full versus partial exemption, the equity-share/voting-rights participation test, the exempt fraction and effective marginal tax rate, and expenditure disallowance: Check this point with one of our partner accountants.

### Foreign employment income exemption (s 10(1)(o)(ii))

Eligibility, qualifying employment/remuneration, full-day tests, annual cap and work-day apportionment: Check this point with one of our partner accountants. See `za-foreign-employment-exemption` for the topic.

### Provisional tax (IRP6), ordinary full-year individual, YoA 2027

Use the current estimate of the year's taxable income. Let A be normal tax on that estimate less applicable s 6 rebates, s 6A credit and s 6B additional medical credit. These are payment calculations; determine the estimate/basic-amount requirements separately.

- First payment: A / 2, less PAYE for the first period, then qualifying s 6quat foreign tax credits proved payable by the end of that period. Halve A before subtracting PAYE.
- Second payment: A less PAYE for the year, the first provisional payment actually paid, and qualifying s 6quat foreign tax credits for the year. Section 6quin is no longer available; the older SARS short example webpage still includes it and must not be followed on that point.
- First payment deadline: **31 August 2026**. Second payment deadline: **26 February 2027**, because 28 February is a Sunday. The ordinary deadlines are within six months of the start and by the last day of the year; a weekend/public-holiday deadline moves to the preceding working day. Short years and an approved alternative IRP6 cycle: Check this point with one of our partner accountants.

Source: [SARS provisional guide, revision 28, sections 9.1 and 10](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/GEN-PT-01-G01-Guide-for-Provisional-Tax-External-Guide.pdf). Provisional-taxpayer status, the basic amount, underestimation penalties and the precise foreign-credit limitation: Check this point with one of our partner accountants. See `za-provisional-tax`.

### Worked example: under-65 employee, YoA 2027

Basis: SARS individual rates and medical credit rates linked above; the ordinary full-year case below uses the published 2027 amounts.

Taxable income R500,000, under 65, qualifying medical scheme contributions paid solely by the employee for the member and one dependant in all 12 months; no additional medical expenses credit is claimed.

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
- Taxable income = R272,000 + R200 + R17,000 - R17,250 = **R271,950** (SARS states that this case's pension contribution qualifies in full).
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

| Official source and passages actually read | URL | Read on |
| --- | --- | --- |
| SARS individual rates: all 2023–2027 brackets, rebate rows and threshold rows | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ | 2026-11-26 |
| SARS medical credit rates: all 2023–2027 monthly person-category rows | https://www.sars.gov.za/tax-rates/medical-tax-credit-rates/ | 2026-11-26 |
| SARS interest and dividends: South African-source interest and both age exemptions, 2023–2027 | https://www.sars.gov.za/tax-rates/income-tax/interest-and-dividends/ | 2026-11-26 |
| SARS trusts FAQ: special-trust brackets and personal relief exclusions | https://www.sars.gov.za/businesses-and-employers/trusts/trust-frequently-asked-questions-faqs/ | 2026-11-26 |
| SARS medical guide, Issue 18, sections 2.2–2.5: payment, qualifying scheme/fund, taxable employer contribution, monthly credit, apportionment and non-refundable cap; these unchanged conditions apply with the current rates above | https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-IT07-Guide-on-the-Determination-of-Medical-Tax-Credits.pdf | 2026-11-26 |
| SARS individual guide 2025/26: section 2 year definition, local-interest exclusion for tax-free investments, Annexure B's complete original facts and calculation | https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-IT01-Guide-on-Income-Tax-and-the-Individual.pdf | 2026-11-26 |
| SARS provisional guide, revision 28: sections 9.1 and 10 including 6quin deletion, payment order and prior-working-day rule | https://www.sars.gov.za/wp-content/uploads/Ops/Guides/GEN-PT-01-G01-Guide-for-Provisional-Tax-External-Guide.pdf | 2026-11-26 |
| Act 19 of 2023, s 3: enacted age test and cumulative rebates, unchanged conditions distinguished from updated amounts | https://www.sars.gov.za/wp-content/uploads/Legal/AmendActs/Legal-LPrim-AA-2023-01-Rates-and-Monetary-Amounts-and-Amendment-of-Revenue-Laws-Act-19-of-2023-GG-49948-Notice-4228-22-December-2023.pdf | 2026-11-26 |
| Act 23 of 2018, ss 3–5: enacted temporary effect of Budget-announced brackets and rebates/medical credit changes | https://www.sars.gov.za/wp-content/uploads/Legal/AmendActs/LAPD-LPrim-AA-2018-03-Taxation-Laws-Amend-Act-23-of-2018-GG-42172.pdf | 2026-11-26 |
| SARS Bills list: B34–2026 remains listed as a Bill; no claim of final enactment | https://www.sars.gov.za/legal-counsel/preparation-of-legislation/bills/ | 2026-11-26 |

Not yet confirmed: no unresolved tax assertion is supplied as usable guidance. Referred topics above require the stated partner-accountant check; they are not clearance to apply the former figures.

## Disclaimer

> **General reference only.** This file is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status or local procedures. Do not rely on it to file, pay, amend or take a tax position without review by a qualified professional in South Africa.

> Contributed by Brandon Iverach.
