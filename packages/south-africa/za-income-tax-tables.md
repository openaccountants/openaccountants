---
name: za-income-tax-tables
description: >
  Year-keyed South African income tax rate tables for individuals and special trusts, covering five years of assessment (2023 to 2027). Contains the progressive tax brackets with base amounts, the primary, secondary and tertiary rebates, tax thresholds by age, medical scheme fees tax credits, the section 11F retirement contribution cap and percentage, the section 18A donations limit, the interest exemption, the foreign dividend fraction and the section 10(1)(o)(ii) foreign employment cap. Use for any South African bracket, rebate, threshold or credit lookup, current year or prior year, including amended assessments and late returns.
version: 0.1
jurisdiction: ZA
last_updated: 2026-09-03
review_status: pending_review
depends_on:
  - foundation
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# South Africa — Income Tax Rate Tables (individuals)

## South Africa — Income Tax Rate Tables (individuals)

Year-keyed rate tables for **natural persons and special trusts**, years of
assessment 2023 to 2027. This file is data only: it states what the figures are
and where they come from. It does not compute tax and does not set out the
ordering of deductions — those belong to the computation guides that consume it.

> **Verification status — checked 2 September 2026.**
>
> Confirmed against SARS, figure by figure:
>
> - **Progressive tax brackets and base amounts, all five years** — every band, every
>   base amount, matches SARS exactly
> - **Primary, secondary and tertiary rebates, all five years**
> - **Tax thresholds, all three age bands** — and they reconcile against the rebates
> - SARS confirms **no change to brackets or rebates across YoA 2024, 2025 and 2026**
>
> **Still to confirm** — carried from the same reconciled source, but not
> independently re-checked:
>
> - Medical scheme fees tax credits (s 6A)
> - The s 11F retirement cap and percentage, and the s 18A donations limit
> - Interest exemption, foreign dividend fraction, s 10(1)(o)(ii) cap

## How South African years of assessment are labelled

SARS numbers a year of assessment by the calendar year in which it **ends**. The tax
year runs 1 March to the last day of February. So the year of assessment ending
28 February 2027 is **YoA 2027**, and it is the year commonly written "2026/27".

**Year of assessment labelling**  _(SARS numbers a year of assessment by the calendar year in which it ends)_

| Year of assessment | Commonly written | Period |
| --- | --- | --- |
| 2023 | 2022/23 | 1 March 2022 – 28 February 2023 |
| 2024 | 2023/24 | 1 March 2023 – 29 February 2024 |
| 2025 | 2024/25 | 1 March 2024 – 28 February 2025 |
| 2026 | 2025/26 | 1 March 2025 – 28 February 2026 |
| 2027 | 2026/27 | 1 March 2026 – 28 February 2027 |

## How South African years of assessment are labelled

Getting this wrong by one year is the single most common error in South African rate
lookups. Every table below is keyed by **year of assessment**.

## Section 1 — Scope

This file covers, for each year of assessment 2023-2027:

- Progressive tax brackets for individuals and special trusts (s 5, read with the
  annual Rates and Monetary Amounts and Amendment of Revenue Laws Act)
- Rebates: primary, secondary (65+), tertiary (75+) (s 6)
- Tax thresholds by age band (derived from the rebates)
- Medical scheme fees tax credits (s 6A)
- Retirement fund contribution deduction: percentage and annual cap (s 11F)
- Donations to public benefit organisations: annual limit (s 18A)
- Interest exemption by age (s 10(1)(i))
- Foreign dividend exempt fraction (s 10B(3))
- Foreign employment remuneration exemption cap (s 10(1)(o)(ii))

Not covered here: company, trust (other than special trusts) and turnover tax
rates; capital gains tax (see `za-capital-gains-tables`); travel allowance and
logbook tables (see `za-travel-allowance-tables`); any computation rule.

## Section 2 — Progressive tax brackets

Each band states the **base amount** payable at the bottom of the band plus the
**marginal rate** on the excess above the band floor. Amounts are rand.

### Year of assessment 2023 (2022/23)

**Progressive tax brackets — Year of assessment 2023 (2022/23)**  _([SARS, Rates of Tax for Individuals — 2023 tax year. https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ Confirmed 2026-09-02.](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_

| Taxable income | Base amount | Rate on excess |
| --- | --- | --- |
| 1 – 226,000 | — | 18% |
| 226,001 – 353,100 | R40,680 | 26% above R226,000 |
| 353,101 – 488,700 | R73,726 | 31% above R353,100 |
| 488,701 – 641,400 | R115,762 | 36% above R488,700 |
| 641,401 – 817,600 | R170,734 | 39% above R641,400 |
| 817,601 – 1,731,600 | R239,452 | 41% above R817,600 |
| 1,731,601 and above | R614,192 | 45% above R1,731,600 |

### Year of assessment 2024 (2023/24)

**Progressive tax brackets — Year of assessment 2024 (2023/24)**  _([SARS, Rates of Tax for Individuals — 2024 tax year. https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ Confirmed 2026-09-02.](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_

| Taxable income | Base amount | Rate on excess |
| --- | --- | --- |
| 1 – 237,100 | — | 18% |
| 237,101 – 370,500 | R42,678 | 26% above R237,100 |
| 370,501 – 512,800 | R77,362 | 31% above R370,500 |
| 512,801 – 673,000 | R121,475 | 36% above R512,800 |
| 673,001 – 857,900 | R179,147 | 39% above R673,000 |
| 857,901 – 1,817,000 | R251,258 | 41% above R857,900 |
| 1,817,001 and above | R644,489 | 45% above R1,817,000 |

### Year of assessment 2025 (2024/25)

**Progressive tax brackets — Year of assessment 2025 (2024/25)**  _([SARS, Rates of Tax for Individuals — 2025 tax year. https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ Confirmed 2026-09-02.](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_

| Taxable income | Base amount | Rate on excess |
| --- | --- | --- |
| 1 – 237,100 | — | 18% |
| 237,101 – 370,500 | R42,678 | 26% above R237,100 |
| 370,501 – 512,800 | R77,362 | 31% above R370,500 |
| 512,801 – 673,000 | R121,475 | 36% above R512,800 |
| 673,001 – 857,900 | R179,147 | 39% above R673,000 |
| 857,901 – 1,817,000 | R251,258 | 41% above R857,900 |
| 1,817,001 and above | R644,489 | 45% above R1,817,000 |

### Year of assessment 2026 (2025/26)

**Progressive tax brackets — Year of assessment 2026 (2025/26)**  _([SARS, Rates of Tax for Individuals — 2026 tax year. https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ Confirmed 2026-09-02.](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_

| Taxable income | Base amount | Rate on excess |
| --- | --- | --- |
| 1 – 237,100 | — | 18% |
| 237,101 – 370,500 | R42,678 | 26% above R237,100 |
| 370,501 – 512,800 | R77,362 | 31% above R370,500 |
| 512,801 – 673,000 | R121,475 | 36% above R512,800 |
| 673,001 – 857,900 | R179,147 | 39% above R673,000 |
| 857,901 – 1,817,000 | R251,258 | 41% above R857,900 |
| 1,817,001 and above | R644,489 | 45% above R1,817,000 |

### Year of assessment 2027 (2026/27)

**Progressive tax brackets — Year of assessment 2027 (2026/27)**  _([SARS, Rates of Tax for Individuals — 2027 tax year. https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ Confirmed 2026-09-02.](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_

| Taxable income | Base amount | Rate on excess |
| --- | --- | --- |
| 1 – 245,100 | — | 18% |
| 245,101 – 383,100 | R44,118 | 26% above R245,100 |
| 383,101 – 530,200 | R79,998 | 31% above R383,100 |
| 530,201 – 695,800 | R125,599 | 36% above R530,200 |
| 695,801 – 887,000 | R185,215 | 39% above R695,800 |
| 887,001 – 1,878,600 | R259,783 | 41% above R887,000 |
| 1,878,601 and above | R666,339 | 45% above R1,878,600 |

## Section 3 — Rebates and tax thresholds

Rebates are credits against tax, not deductions from income. The secondary and
tertiary rebates are **additional** to the primary rebate, not replacements for it.

**Rebates: primary, secondary, tertiary**  _(Income Tax Act 58 of 1962 s 6; SARS Rates of Tax for Individuals.)_

| YoA | Primary | Secondary (65+, additional) | Tertiary (75+, additional) |
| --- | --- | --- | --- |
| 2023 (2022/23) | R16,425 | R9,000 | R2,997 |
| 2024 (2023/24) | R17,235 | R9,444 | R3,145 |
| 2025 (2024/25) | R17,235 | R9,444 | R3,145 |
| 2026 (2025/26) | R17,235 | R9,444 | R3,145 |
| 2027 (2026/27) | R17,820 | R9,765 | R3,249 |

**Cumulative rebate by age band**  _(Income Tax Act 58 of 1962 s 6; SARS Rates of Tax for Individuals.)_

| YoA | Under 65 | 65 to 74 | 75 and over |
| --- | --- | --- | --- |
| 2023 (2022/23) | R16,425 | R25,425 | R28,422 |
| 2024 (2023/24) | R17,235 | R26,679 | R29,824 |
| 2025 (2024/25) | R17,235 | R26,679 | R29,824 |
| 2026 (2025/26) | R17,235 | R26,679 | R29,824 |
| 2027 (2026/27) | R17,820 | R27,585 | R30,834 |

**Tax thresholds — income below which no tax is payable**  _(Income Tax Act 58 of 1962 s 6; SARS Rates of Tax for Individuals.)_

| YoA | Under 65 | 65 to 74 | 75 and over |
| --- | --- | --- | --- |
| 2023 (2022/23) | R91,250 | R141,250 | R157,900 |
| 2024 (2023/24) | R95,750 | R148,217 | R165,689 |
| 2025 (2024/25) | R95,750 | R148,217 | R165,689 |
| 2026 (2025/26) | R95,750 | R148,217 | R165,689 |
| 2027 (2026/27) | R99,000 | R153,250 | R171,300 |

## Section 4 — Medical scheme fees tax credits

**Medical scheme fees tax credits (s 6A)**  _(Income Tax Act 58 of 1962 s 6A; SARS Medical Tax Credit Rates.)_

| YoA | Principal member | First dependant | Each additional dependant |
| --- | --- | --- | --- |
| 2023 (2022/23) | R347 pm | R347 pm | R234 pm |
| 2024 (2023/24) | R364 pm | R364 pm | R246 pm |
| 2025 (2024/25) | R364 pm | R364 pm | R246 pm |
| 2026 (2025/26) | R364 pm | R364 pm | R246 pm |
| 2027 (2026/27) | R376 pm | R376 pm | R254 pm |

## Section 5 — Other annual limits and thresholds

**s 11F retirement cap, s 11F percentage, s 18A donations limit**  _(Income Tax Act 58 of 1962 s 11F, s 18A, s 10(1)(i), s 10B(3), s 10(1)(o)(ii).)_

| YoA | s 11F retirement cap | s 11F percentage | s 18A donations limit |
| --- | --- | --- | --- |
| 2023 (2022/23) | R350,000 | 27.5% of the greater of remuneration or taxable income | 10% of taxable income |
| 2024 (2023/24) | R350,000 | 27.5% of the greater of remuneration or taxable income | 10% of taxable income |
| 2025 (2024/25) | R350,000 | 27.5% of the greater of remuneration or taxable income | 10% of taxable income |
| 2026 (2025/26) | R350,000 | 27.5% of the greater of remuneration or taxable income | 10% of taxable income |
| 2027 (2026/27) | R430,000 | 27.5% of the greater of remuneration or taxable income | 10% of taxable income |

**Interest exemption, foreign dividend fraction, s 10(1)(o)(ii) cap**  _(Income Tax Act 58 of 1962 s 11F, s 18A, s 10(1)(i), s 10B(3), s 10(1)(o)(ii).)_

| YoA | Interest exemption (under 65) | Interest exemption (65+) | Foreign dividend exempt fraction | s 10(1)(o)(ii) cap |
| --- | --- | --- | --- | --- |
| 2023 (2022/23) | R23,800 | R34,500 | 25/45 | R1,250,000 |
| 2024 (2023/24) | R23,800 | R34,500 | 25/45 | R1,250,000 |
| 2025 (2024/25) | R23,800 | R34,500 | 25/45 | R1,250,000 |
| 2026 (2025/26) | R23,800 | R34,500 | 25/45 | R1,250,000 |
| 2027 (2026/27) | R23,800 | R34,500 | 25/45 | R1,250,000 |

## Section 6 — Edge cases and traps

- **No bracket adjustment for three consecutive years.** Years of assessment 2024,
  2025 and 2026 share identical brackets, rebates and medical credits. This is not a
  transcription error in this file — no inflation adjustment was made across those
  years. Do not "correct" one year to differ from the others.
- **Base amounts must reconcile.** Each band's base amount equals the previous
  band's base plus the previous band's width times its rate. If a table fails this
  check, the table is wrong. See the self-check below.
- **Rebates are age-based on the taxpayer's age at any time during the year of
  assessment**, not at year end.
- **Secondary and tertiary rebates are additive.** A 76-year-old receives all three.
- **Prior-year lookups matter.** Amended assessments, late returns and objections are
  computed on the rates for the year of assessment concerned, never the current year.

## Section 7 — Self-checks

Run these before relying on any bracket table, including this one:

1. **Base-amount reconciliation.** For every band after the first,
   `base(n) = base(n-1) + (floor(n) - floor(n-1)) x rate(n-1)`. Every year in this
   file satisfies this exactly.
2. **Threshold reconciliation.** `threshold = cumulative rebate / lowest marginal
   rate`. For YoA 2027: 17,820 / 0.18 = 99,000.
3. **Year check.** Confirm the year of assessment, not the calendar year. A return
   for the year ended 28 February 2027 uses YoA 2027.

## Disclaimer

> **General reference only.** This file is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status or local procedures. Do not rely on it to file, pay, amend or take a tax position without review by a qualified professional in South Africa.

> Contributed by Brandon Iverach.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
