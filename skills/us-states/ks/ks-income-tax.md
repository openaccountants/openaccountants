---
name: ks-income-tax
description: Use this skill whenever asked about Kansas individual income tax. Trigger on phrases like "Kansas income tax", "KS income tax", "K-40", "KDOR income tax", "K.S.A. 79-32,110". Kansas has a two-bracket progressive system (5.20%–5.58%) effective 2024+; Social Security is fully exempt for tax years 2024+ regardless of AGI (K.S.A. 79-32,117(a)(xviii)(B)). ALWAYS load us-tax-workflow-base first.
version: "0.3"
jurisdiction: US-KS
tax_year: 2026
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kansas individual income tax, tax year 2026

> **Source-cited draft.** Built from K.S.A. 79-32,101, 79-32,103, 79-32,107, 79-32,110, 79-32,117 and 79-32,121 and the KDOR 2025 Individual Income Tax booklet, read on 2026-10-28. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Kansas Individual Income Tax Skill — Self-Employed / Sole Proprietor.** This skill covers Kansas Form K-40 (Individual Income Tax Return) for sole proprietors and single-member LLCs. It addresses the two-bracket progressive income tax, Kansas modifications to federal AGI, and Schedule S adjustments. It does NOT cover corporate returns (K-120), partnership/S-corp pass-throughs (K-120S), or detailed multi-state allocation.

| Field | Value |
| --- | --- |
| Jurisdiction | Kansas (US-KS) |
| Tax authority | [Kansas Department of Revenue (KDOR)](https://www.ksrevenue.gov/) |
| Filing portal | [Kansas WebFile](https://www.kansas.gov/webfile/) |
| Legislation | K.S.A. 79-32,110 et seq. |
| Primary form | Form K-40 (Kansas Individual Income Tax Return) + Schedule S |
| Filing deadline | April 15, 2027 (for tax year 2026) |

See also: `ks-payroll`, `ks-cross-border`, `ks-corporate-income-tax`.

## Who this applies to

Kansas individual taxpayers filing Form K-40, with this skill focused on sole proprietors and single-member LLCs (Schedule C income flowing through federal AGI). Kansas has NO local/county income taxes; only the state tax applies (rule R-8 below). Nonresidents and part-year residents use Schedule S Part B (see `ks-cross-border`).

### Refusal catalogue

| Code | Situation | Action |
| --- | --- | --- |
| REF-KS-01 | Taxpayer is a nonresident with complex Kansas source income allocation | Refuse; requires Schedule S Part B detailed analysis. |
| REF-KS-02 | Taxpayer has partnership or S-corp pass-through with Kansas K-1 modifications | Flag for reviewer. |
| REF-KS-03 | Taxpayer claims Kansas Historic Preservation Credit or other complex credits | Flag for reviewer — separate forms required. |
| REF-KS-04 | Taxpayer has farm income with Kansas-specific depreciation differences | Flag for reviewer. |
| REF-KS-05 | Taxpayer is amending a pre-2024 return with Social Security income near the $75,000 AGI cap | Flag for reviewer — historical cap applies to those years only. |

## Rates, bands and thresholds

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

| Filing status | Amount | Source |
| --- | --- | --- |
| Single | $3,605 | [KDOR 2025 booklet](https://www.ksrevenue.gov/incomebook25.html) |
| Married Filing Jointly | $8,240 | KDOR 2025 booklet |
| Head of Household | $6,180 | KDOR 2025 booklet |
| Married Filing Separately | $4,120 | KDOR 2025 booklet |

### Personal exemptions (2025 tax year)

| Category | Amount | Source |
| --- | --- | --- |
| Single / HoH / MFS | $9,160 | [K.S.A. 79-32,121](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0121.html); KDOR 2025 booklet |
| Married Filing Jointly | $18,320 | K.S.A. 79-32,121; KDOR 2025 booklet |
| Each dependent | $2,320 | K.S.A. 79-32,121; KDOR 2025 booklet |

### Estimated tax threshold

| Item | Amount | Source |
| --- | --- | --- |
| Estimated payments required | Expected tax of **$500 or more** after withholding and credits, and withholding and credits below 90% of current-year tax or 100% of prior-year tax | [K.S.A. 79-32,101(a)(1)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0101.html) |

## The taxable base

### Starting point

- **Starting point** — Kansas starts from federal adjusted gross income (AGI) — Form 1040, Line 11. This is entered on Form K-40, Line 1.

### Additions (Schedule S, Part A)

**Additions table**  _(K.S.A. 79-32,117)_

| Item | Description | Source |
| --- | --- | --- |
| State/local income tax refunds | If not already in federal AGI | K.S.A. 79-32,117 |
| Out-of-state municipal bond interest | Interest from bonds of states other than Kansas | K.S.A. 79-32,117(b) |

### Subtractions (Schedule S, Part A)

**Subtractions table**  _(K.S.A. 79-32,117)_

| Item | Description | Source |
| --- | --- | --- |
| Kansas state income tax refund | If included in federal AGI (state tax refund recovery) | K.S.A. 79-32,117(a) |
| Social Security benefits | Fully exempt for all tax years beginning after Dec 31, 2023 (no AGI limit). The $75,000 AGI cap applied only to tax years ending before Jan 1, 2024 | K.S.A. 79-32,117(a)(xviii)(B) |
| U.S. government interest | Interest on U.S. obligations | K.S.A. 79-32,117(a)(i) |
| KPERS contributions | Kansas Public Employees Retirement System contributions | K.S.A. 79-32,117(a)(ii) |
| Military pay | Active-duty military compensation | K.S.A. 79-32,117 |
| Retirement income exclusion | Social Security fully exempt (2024+); KPERS and other retirement provisions vary — see Schedule S line A11 | K.S.A. 79-32,117 |

### Resulting computation

- **Kansas taxable income formula** — Federal AGI ± Schedule S modifications = Kansas AGI → minus standard or itemized deduction → minus personal exemptions = Kansas taxable income → apply bracket rates.

### Self-employed specific rules

- **Self-employment health insurance** — Kansas follows federal treatment — the deduction reduces federal AGI and flows through.
- **Retirement contributions (SEP, SIMPLE, Solo 401(k))** — Kansas follows federal treatment — these deductions reduce federal AGI and flow through.
- **Home office deduction** — Kansas follows the federal home office deduction as part of Schedule C, included in federal AGI.
- **QBI deduction (Section 199A)** — Kansas does not allow the federal QBI deduction because Kansas starts from federal AGI (before the QBI deduction is taken). The QBI deduction does not affect Kansas taxable income.
- **Standard vs. itemized deductions** — Kansas allows taxpayers to choose between the Kansas standard deduction and Kansas itemized deductions. If itemizing, Kansas generally follows the federal itemized deductions with modifications on Schedule S.

### Tier 1 rules — deterministic

| Rule | Description |
| --- | --- |
| R-1 | Apply the two-bracket rate schedule based on filing status. Single/HoH/MFS: 5.20% up to $23,000, 5.58% above. MFJ: 5.20% up to $46,000, 5.58% above. |
| R-2 | Start from federal AGI and apply Schedule S modifications. |
| R-3 | Subtract the standard deduction or itemized deductions (taxpayer's choice). |
| R-4 | Subtract personal exemptions ($9,160 single; $18,320 MFJ; $2,320 per dependent — 2025 amounts). |
| R-5 | Social Security benefits are fully exempt for tax years 2024 and later (K.S.A. 79-32,117(a)(xviii)(B)). |
| R-6 | Add back interest from out-of-state municipal bonds. |
| R-7 | Subtract U.S. government bond interest. |
| R-8 | Kansas has NO local/county income taxes. Only the state tax applies. |

### Tier 2 rules — requires judgment

| Rule | Description |
| --- | --- |
| J-1 | For pre-2024 amended returns, apply the historical $75,000 AGI cap on Social Security exemption. |
| J-2 | Evaluate whether Kansas itemized deductions exceed the Kansas standard deduction, especially when federal SALT deductions differ. |
| J-3 | Assess Kansas NOL carryforward interaction with federal NOL when there are differing modification histories. |
| J-4 | Determine Kansas source income allocation for taxpayers with multi-state activity. |

### Supplier pattern library

| Pattern | Kansas treatment |
| --- | --- |
| Freelance income (Schedule C) | Flows through federal AGI → Kansas AGI. Subject to state tax at bracket rates. |
| Rental income (Schedule E) | Flows through federal AGI → Kansas AGI. Subject to state tax. |
| Capital gains | Fully taxable at bracket rates. |
| Interest / dividends | Taxable except U.S. government obligations (exempt). |
| Social Security | Fully exempt (tax years 2024+). Pre-2024 years: exempt only if federal AGI ≤ $75,000. |
| Retirement distributions | Generally taxable; KPERS contributions are exempt. |

## Deadlines and filing

| Obligation | When | Source |
| --- | --- | --- |
| Form K-40, calendar-year filers | April 15 of the following year (April 15, 2026 for 2025; April 15, 2027 for 2026); fiscal-year returns the 15th day of the 4th month after year end | [KDOR 2025 booklet](https://www.ksrevenue.gov/incomebook25.html) |
| Estimated tax, Form K-40ES: 1st quarter | April 15 | [K.S.A. 79-32,103](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0103.html); KDOR 2025 booklet |
| 2nd quarter | June 15 | K.S.A. 79-32,103 |
| 3rd quarter | September 15 | K.S.A. 79-32,103 |
| 4th quarter | January 15 (following year) | K.S.A. 79-32,103 |
| Electronic filing | Kansas WebFile (free; residents and nonresidents who filed a Kansas return in the past 3 years) or IRS e-File | [Kansas WebFile](https://www.kansas.gov/webfile/); KDOR 2025 booklet |

### Form K-40 mapping

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

## Penalties and interest

- **Underpaid estimated tax:** a penalty at the delinquent-tax interest rate of K.S.A. 79-2968(b) runs on the underpayment from the installment due date until paid or until the 15th day of the 4th month after year end, whichever is earlier; it is not added if it does not exceed $1 ([K.S.A. 79-32,107(a)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0107.html)).
- Late-filing and late-payment penalty percentages for individuals (K.S.A. 79-3228) are listed under Not yet confirmed.

## Cross-border points

- Nonresidents with Kansas-source income and part-year residents allocate on Schedule S Part B; complex allocations are refused (REF-KS-01) and multi-state sourcing is a judgment rule (J-4). See `ks-cross-border`.
- Resident wages earned out of state stay subject to Kansas withholding (see `ks-payroll`).

## Worked examples

### Example 1: single filer, Kansas taxable income $60,000

The first $23,000 is taxed at 5.20% = $1,196. The remaining $37,000 is taxed at 5.58% = $2,064.60. Kansas tax $3,260.60.

```oa-check
name: KS 2025 single, taxable income 60,000
inputs:
  ti: 60000
steps:
  - b1: min(ti, 23000) * 0.052
  - b2: max(ti - 23000, 0) * 0.0558
  - tax: b1 + b2
expected:
  tax: 3260.60
```

### Example 2: married filing jointly, Kansas taxable income $90,000

The joint bracket doubles: the first $46,000 is taxed at 5.20% = $2,392. The remaining $44,000 is taxed at 5.58% = $2,455.20. Kansas tax $4,847.20. Using the single bracket break by mistake would overstate the tax.

```oa-check
name: KS 2025 married filing jointly, taxable income 90,000
inputs:
  ti: 90000
steps:
  - b1: min(ti, 46000) * 0.052
  - b2: max(ti - 46000, 0) * 0.0558
  - tax: b1 + b2
expected:
  tax: 4847.20
```

## Ask the client first

1. **Filing status and dependents?** They set the bracket break, the standard deduction and the exemptions.
2. **Kansas resident for the whole year?** Nonresidents and part-year residents go to Schedule S Part B.
3. **Social Security, KPERS, military or other retirement income?** Schedule S subtractions.
4. **Out-of-state municipal bond interest or U.S. government interest?** Schedule S additions and subtractions.
5. **Itemizing federally, and how large are state and local taxes?** Kansas standard vs itemized choice.
6. **Estimated payments and withholding so far?** The $500 estimated-tax test and the underpayment penalty.

## Sources

| Source | URL | Read on |
|---|---|---|
| K.S.A. 79-32,110 (individual rates and brackets) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110.html | 2026-10-28 |
| K.S.A. 79-32,117 (Kansas modifications; Social Security (xviii)(A)/(B)) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0117.html | 2026-10-28 |
| K.S.A. 79-32,121 (personal exemptions) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0121.html | 2026-10-28 |
| K.S.A. 79-32,120 (Kansas itemized deductions of an individual; election in lieu of the standard deduction) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0120.html | 2026-10-28 |
| K.S.A. 79-32,101 (estimated tax, $500 threshold) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0101.html | 2026-10-28 |
| K.S.A. 79-32,103 (installment dates) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0103.html | 2026-10-28 |
| K.S.A. 79-32,107 (underpayment of estimated tax) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0107.html | 2026-10-28 |
| KDOR 2025 Individual Income Tax booklet (HTML: due dates, standard deduction, exemptions, K-40ES, WebFile) | https://www.ksrevenue.gov/incomebook25.html | 2026-10-28 |
| KDOR 2025 Individual Income Tax booklet (PDF, Schedule S) | https://www.ksrevenue.gov/pdf/ip25.pdf | 2026-10-28 |
| Kansas WebFile | https://www.kansas.gov/webfile/ | 2026-10-28 |
| Kansas Department of Revenue | https://www.ksrevenue.gov/ | 2026-10-28 |

Not yet confirmed: whether Kansas decouples from IRC §179 / bonus depreciation (v0.2 said Kansas "may decouple from certain federal accelerated depreciation provisions", cited generally to K.S.A. 79-32,117); the standard deduction and personal exemption amounts for tax year 2026 (the tables show 2025 amounts); individual late-filing and late-payment penalty percentages under K.S.A. 79-3228 and the current interest-rate value under K.S.A. 79-2968(b). Two secondary sources listed in v0.2 are no longer cited (rule 1).

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
