---
name: ks-income-tax
description: Use this skill whenever asked about Kansas individual income tax. Trigger on phrases like "Kansas income tax", "KS income tax", "K-40", "KDOR income tax", "K.S.A. 79-32,110". Kansas has a two-bracket progressive system (5.20%–5.58%) effective 2024+. ALWAYS load us-tax-workflow-base first.
version: "0.1"
jurisdiction: US-KS
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# KS Income Tax

## Kansas Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers Kansas Form K-40 (Individual Income Tax Return) for sole proprietors and single-member LLCs. It addresses the two-bracket progressive income tax, Kansas modifications to federal AGI, and Schedule S adjustments. It does NOT cover corporate returns (K-120), partnership/S-corp pass-throughs (K-120S), or detailed multi-state allocation.

> **Quality tier.** Q3 — AI-drafted, not independently verified. All outputs must be reviewed by a qualified tax professional before filing.

## Section 1: Metadata

**Section 1 Metadata table**

| Field | Value |
| --- | --- |
| Jurisdiction | Kansas (US-KS) |
| Tax authority | [Kansas Department of Revenue (KDOR)](https://www.ksrevenue.gov/) |
| Filing portal | [Kansas WebFile](https://www.kansas.gov/webfile/) |
| Legislation | K.S.A. 79-32,110 et seq. |
| Primary form | Form K-40 (Kansas Individual Income Tax Return) + Schedule S |
| Filing deadline | April 15, 2027 (for tax year 2026) |
| Version | 0.1 |
| Date | May 22, 2026 |
| Validation status | AI-drafted — Q3 |

### Sources consulted

1. Kansas Legislature — K.S.A. 79-32,110: <https://www.kslegislature.gov/b2025_26/laws/079_000_0000_chapter/079_032_0000_article/079_032_0110_section/079_032_0110_k/>
2. KDOR — 2025 Individual Income Tax Booklet: <https://www.ksrevenue.gov/pdf/ip25.pdf>
3. Tax Foundation — Kansas Tax Rates: <https://taxfoundation.org/location/kansas/>
4. RemoteLaws — Kansas Income Tax Rates 2025–2026: <https://remotelaws.com/state-income-tax/us-states/kansas/>

## Section 2: Quick reference — rates and thresholds

### Tax brackets (tax year 2024 and thereafter, per K.S.A. 79-32,110(B))

**Single, Head of Household, Married Filing Separately bracket table**  _(K.S.A. 79-32,110(B))_

| Taxable income | Rate | Tax calculation |
| --- | --- | --- |
| $0 – $23,000 | 5.20% | 5.20% of Kansas taxable income |
| Over $23,000 | 5.58% | $1,196 + 5.58% of excess over $23,000 |

**Married Filing Jointly bracket table**  _(K.S.A. 79-32,110(B))_

| Taxable income | Rate | Tax calculation |
| --- | --- | --- |
| $0 – $46,000 | 5.20% | 5.20% of Kansas taxable income |
| Over $46,000 | 5.58% | $2,392 + 5.58% of excess over $46,000 |

**Note:** These two-bracket rates replaced the prior three-bracket system (3.1% / 5.25% / 5.7%) effective for tax year 2024 under Senate Bill 1 (2024).

### Standard deduction (2025 tax year)

**Standard deduction table**

| Filing status | Amount |
| --- | --- |
| Single | $3,605 |
| Married Filing Jointly | $8,240 |
| Head of Household | $6,180 |
| Married Filing Separately | $4,120 |

### Personal exemptions (2025 tax year)

**Personal exemptions table**

| Category | Amount |
| --- | --- |
| Single / HoH / MFS | $9,160 |
| Married Filing Jointly | $18,320 |
| Each dependent | $2,320 |

## Section 3: How this skill works with the federal return

### Starting point

- **Starting point** — Kansas starts from federal adjusted gross income (AGI) — Form 1040, Line 11. This is entered on Form K-40, Line 1.

### Additions (Schedule S, Part A)

**Additions table**  _(K.S.A. 79-32,117)_

| Item | Description | Source |
| --- | --- | --- |
| State/local income tax refunds | If not already in federal AGI | K.S.A. 79-32,117 |
| Out-of-state municipal bond interest | Interest from bonds of states other than Kansas | K.S.A. 79-32,117(b) |
| IRC §179 / bonus depreciation differences | Kansas may decouple from certain federal accelerated depreciation provisions | K.S.A. 79-32,117 |

### Subtractions (Schedule S, Part A)

**Subtractions table**  _(K.S.A. 79-32,117)_

| Item | Description | Source |
| --- | --- | --- |
| Kansas state income tax refund | If included in federal AGI (state tax refund recovery) | K.S.A. 79-32,117(a) |
| Social Security benefits | Kansas fully exempts Social Security if federal AGI is $75,000 or less | K.S.A. 79-32,117(c)(viii) |
| U.S. government interest | Interest on U.S. obligations | K.S.A. 79-32,117(a)(i) |
| KPERS contributions | Kansas Public Employees Retirement System contributions | K.S.A. 79-32,117(a)(ii) |
| Military pay | Active-duty military compensation | K.S.A. 79-32,117 |
| Retirement income exclusion | Social Security exempt for AGI ≤ $75,000; other retirement income provisions vary | K.S.A. 79-32,117 |

### Resulting computation

- **Kansas taxable income formula** — Federal AGI ± Schedule S modifications = Kansas AGI → minus standard or itemized deduction → minus personal exemptions = Kansas taxable income → apply bracket rates.

## Section 4: Self-employed specific rules

### Estimated tax payments

- **Estimated tax payments requirement** — Self-employed individuals must make quarterly estimated tax payments if they expect to owe $500 or more for the year.

**Estimated tax payment vouchers table**

| Voucher | Due date |
| --- | --- |
| 1st quarter | April 15 |
| 2nd quarter | June 15 |
| 3rd quarter | September 15 |
| 4th quarter | January 15 (following year) |

- **Estimated payment form** — Use Form K-40ES for estimated payments.

### Self-employment health insurance

- **SE health insurance treatment** — Kansas follows federal treatment — the deduction reduces federal AGI and flows through.

### Retirement contributions (SEP, SIMPLE, Solo 401(k))

- **Retirement contributions treatment** — Kansas follows federal treatment — these deductions reduce federal AGI and flow through.

### Home office deduction

- **Home office deduction treatment** — Kansas follows the federal home office deduction as part of Schedule C, included in federal AGI.

### QBI deduction (Section 199A)

- **QBI deduction treatment** — Kansas does not allow the federal QBI deduction because Kansas starts from federal AGI (before the QBI deduction is taken). The QBI deduction does not affect Kansas taxable income.

### Standard vs. itemized deductions

- **Standard vs itemized choice** — Kansas allows taxpayers to choose between the Kansas standard deduction and Kansas itemized deductions. If itemizing, Kansas generally follows the federal itemized deductions with modifications on Schedule S.

## Section 5: Tier 1 rules — deterministic

**Tier 1 rules table**

| Rule | Description |
| --- | --- |
| R-1 | Apply the two-bracket rate schedule based on filing status. Single/HoH/MFS: 5.20% up to $23,000, 5.58% above. MFJ: 5.20% up to $46,000, 5.58% above. |
| R-2 | Start from federal AGI and apply Schedule S modifications. |
| R-3 | Subtract the standard deduction or itemized deductions (taxpayer's choice). |
| R-4 | Subtract personal exemptions ($9,160 single; $18,320 MFJ; $2,320 per dependent — 2025 amounts). |
| R-5 | Social Security benefits are fully exempt if federal AGI ≤ $75,000. |
| R-6 | Add back interest from out-of-state municipal bonds. |
| R-7 | Subtract U.S. government bond interest. |
| R-8 | Kansas has NO local/county income taxes. Only the state tax applies. |

## Section 6: Tier 2 rules — requires judgment

**Tier 2 rules table**

| Rule | Description |
| --- | --- |
| J-1 | Determine Social Security exemption eligibility when federal AGI is near the $75,000 threshold. |
| J-2 | Evaluate whether Kansas itemized deductions exceed the Kansas standard deduction, especially when federal SALT deductions differ. |
| J-3 | Assess Kansas NOL carryforward interaction with federal NOL when there are differing modification histories. |
| J-4 | Determine Kansas source income allocation for taxpayers with multi-state activity. |

## Section 7: Supplier pattern library

**Supplier pattern library table**

| Pattern | Kansas treatment |
| --- | --- |
| Freelance income (Schedule C) | Flows through federal AGI → Kansas AGI. Subject to state tax at bracket rates. |
| Rental income (Schedule E) | Flows through federal AGI → Kansas AGI. Subject to state tax. |
| Capital gains | Fully taxable at bracket rates. |
| Interest / dividends | Taxable except U.S. government obligations (exempt). |
| Social Security | Fully exempt if federal AGI ≤ $75,000. Taxable above $75,000. |
| Retirement distributions | Generally taxable; KPERS contributions are exempt. |

## Section 8: Form mapping

**Form K-40 mapping table**

| Form K-40 line | Description | Source |
| --- | --- | --- |
| Line 1 | Federal AGI (Form 1040, Line 11) | Federal return |
| Line 2 | Modifications from Schedule S | K.S.A. 79-32,117 |
| Line 3 | Kansas AGI (Line 1 ± Line 2) | Computed |
| Line 4 | Standard or itemized deduction | K.S.A. 79-32,120 |
| Line 5 | Personal exemptions | K.S.A. 79-32,121 |
| Line 7 | Kansas taxable income | Line 3 − Line 4 − Line 5 |
| Line 8 | Kansas tax (from rate schedule or tax table) | K.S.A. 79-32,110 |
| Lines 9–13 | Credits | Various |
| Lines 14–20 | Payments and withholding | Various |
| Line 23 | Balance due or refund | Computed |

## Section 9: Refusal catalogue

**Refusal catalogue table**

| Code | Situation | Action |
| --- | --- | --- |
| REF-KS-01 | Taxpayer is a nonresident with complex Kansas source income allocation | Refuse; requires Schedule S Part B detailed analysis. |
| REF-KS-02 | Taxpayer has partnership or S-corp pass-through with Kansas K-1 modifications | Flag for reviewer. |
| REF-KS-03 | Taxpayer claims Kansas Historic Preservation Credit or other complex credits | Flag for reviewer — separate forms required. |
| REF-KS-04 | Taxpayer has farm income with Kansas-specific depreciation differences | Flag for reviewer. |
| REF-KS-05 | Taxpayer has Social Security income and federal AGI is near the $75,000 exemption threshold | Flag for reviewer — cliff-effect determination needed. |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
