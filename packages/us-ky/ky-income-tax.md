---
name: ky-income-tax
description: Use this skill whenever asked about Kentucky individual income tax. Trigger on phrases like "Kentucky income tax", "KY income tax", "Form 740", "KRS 141", "Kentucky flat tax". Kentucky has a flat 3.5% rate for TY2026 (was 4% for TY2025). ALWAYS load us-tax-workflow-base first.
version: "0.1"
jurisdiction: US-KY
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# KY Income Tax

## Kentucky Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers Kentucky Form 740 (Full-Year Resident Individual Income Tax Return) for sole proprietors and single-member LLCs. It addresses the flat state income tax and Kentucky-specific modifications to federal AGI. It does NOT cover part-year or nonresident returns (Form 740-NP), corporate returns (Form 720), or LLET.

> **Quality tier.** Q3 — AI-drafted, not independently verified. All outputs must be reviewed by a qualified tax professional before filing.

## Section 1: Metadata

- **Jurisdiction** — Kentucky (US-KY)
- **Tax authority** — [Kentucky Department of Revenue](https://revenue.ky.gov/)
- **Filing portal** — [Kentucky E-File](https://revenue.ky.gov/Individual/Pages/File-Your-Return.aspx)
- **Legislation** — KRS Chapter 141 — Income Taxes
- **Primary form** — Form 740 (Kentucky Individual Income Tax Return — Full-Year Resident)
- **Filing deadline** — April 15, 2027 (for tax year 2026)
- **Version** — 0.1
- **Date** — May 22, 2026
- **Validation status** — AI-drafted — Q3

**Section 1 metadata table**

| Field | Value |
| --- | --- |
| Jurisdiction | Kentucky (US-KY) |
| Tax authority | [Kentucky Department of Revenue](https://revenue.ky.gov/) |
| Filing portal | [Kentucky E-File](https://revenue.ky.gov/Individual/Pages/File-Your-Return.aspx) |
| Legislation | KRS Chapter 141 — Income Taxes |
| Primary form | Form 740 (Kentucky Individual Income Tax Return — Full-Year Resident) |
| Filing deadline | April 15, 2027 (for tax year 2026) |
| Version | 0.1 |
| Date | May 22, 2026 |
| Validation status | AI-drafted — Q3 |

### Sources consulted

1. Kentucky Department of Revenue — Individual Income Tax: <https://revenue.ky.gov/Individual/Individual-Income-Tax/Pages/default.aspx>
2. AARP — Kentucky State Taxes 2026: <https://www.aarp.org/states/kentucky/state-tax-guide.html>
3. University of Kentucky Income Tax Seminar 2025 (DOR presentation): <https://ukincometax.mgcafe.uky.edu/>
4. KRS 141.020 — Tax rate
5. H.B. 1 (2025) — Rate reduction to 3.5% for tax year 2026

## Section 2: Quick reference — rates and thresholds

### State income tax rate

**State income tax rate table**  _(KRS 141.020)_

| Tax year | Rate | Source |
| --- | --- | --- |
| 2025 | 4.00% | KRS 141.020 |
| 2026 | 3.50% | H.B. 1 (2025); KRS 141.020 as amended |

- **2025** — 4.00%  _(KRS 141.020)_
- **2026** — 3.50%  _(H.B. 1 (2025); KRS 141.020 as amended)_

Kentucky imposes a **flat** income tax rate. There are no graduated brackets. The same rate applies to all filing statuses.

### Standard deduction

**Standard deduction table**  _(KRS 141.081)_

| Tax year | Amount | Source |
| --- | --- | --- |
| 2025 | $3,270 | KRS 141.081 |
| 2026 | $3,360 | H.B. 1 (2025); DOR announcement |

- **2025** — $3,270  _(KRS 141.081)_
- **2026** — $3,360  _(H.B. 1 (2025); DOR announcement)_

Kentucky allows either the standard deduction or itemized deductions (not both).

### Personal exemptions

Kentucky provides a personal tax credit rather than a traditional exemption. For TY2025, the credit is $40 per taxpayer. Dependent credits may also apply.

## Section 3: How this skill works with the federal return

### Starting point

- **Starting point** — Kentucky starts from **federal adjusted gross income (AGI)** — Form 1040, Line 11. This is entered on Form 740, Line 5.

### Additions to income

**Additions to income table**

| Item | Description | Source |
| --- | --- | --- |
| State/local income tax refunds | If deducted federally and included as income in federal AGI | KRS 141.010 |
| Interest from other states' bonds | Interest on obligations of other states must be added back | KRS 141.010(10) |
| Lump-sum distribution exclusion | If federal exclusion was taken | KRS 141.010 |
| IRC differences | Kentucky decouples from certain post-2017 TCJA provisions — review annually | KRS 141.0101 |

- **State/local income tax refunds** — If deducted federally and included as income in federal AGI  _(KRS 141.010)_
- **Interest from other states' bonds** — Interest on obligations of other states must be added back  _(KRS 141.010(10))_
- **Lump-sum distribution exclusion** — If federal exclusion was taken  _(KRS 141.010)_
- **IRC differences** — Kentucky decouples from certain post-2017 TCJA provisions — review annually  _(KRS 141.0101)_

### Subtractions from income

**Subtractions from income table**

| Item | Description | Source |
| --- | --- | --- |
| U.S. government interest | Interest on U.S. obligations | KRS 141.010(10)(d) |
| Social Security benefits | Kentucky fully exempts Social Security benefits | KRS 141.019(1)(a) |
| Railroad retirement benefits | Fully exempt | KRS 141.019 |
| Kentucky pension exclusion | Up to $31,110 (2025) for qualifying retirement income | KRS 141.019(1)(l) |
| Military pay | Various exclusions for active-duty service | KRS 141.019 |

- **U.S. government interest** — Interest on U.S. obligations  _(KRS 141.010(10)(d))_
- **Social Security benefits** — Kentucky fully exempts Social Security benefits  _(KRS 141.019(1)(a))_
- **Railroad retirement benefits** — Fully exempt  _(KRS 141.019)_
- **Kentucky pension exclusion** — Up to $31,110 (2025) for qualifying retirement income  _(KRS 141.019(1)(l))_
- **Military pay** — Various exclusions for active-duty service  _(KRS 141.019)_

### Resulting computation

- **KY tax computation** — Federal AGI + additions − subtractions = Kentucky AGI → minus standard or itemized deduction = Kentucky taxable income → times 3.5% (TY2026) = Kentucky tax → minus credits.

## Section 4: Self-employed specific rules

### Estimated tax payments

- **Estimated payment requirement** — Self-employed individuals must make quarterly estimated payments if they expect to owe $500 or more.

**Estimated tax payments table**

| Voucher | Due date |
| --- | --- |
| 1st quarter | April 15 |
| 2nd quarter | June 15 |
| 3rd quarter | September 15 |
| 4th quarter | January 15 (following year) |

- **1st quarter** — April 15
- **2nd quarter** — June 15
- **3rd quarter** — September 15
- **4th quarter** — January 15 (following year)

Use Form 740-ES for estimated payments.

### Self-employment health insurance

- **SE health insurance treatment** — Kentucky follows federal treatment — the deduction reduces federal AGI and flows through.

### Retirement contributions (SEP, SIMPLE, Solo 401(k))

- **Retirement contribution treatment** — Kentucky follows federal treatment — these deductions reduce federal AGI and flow through.

### Home office deduction

- **Home office treatment** — Kentucky follows the federal home office deduction as part of Schedule C, included in federal AGI.

### QBI deduction (Section 199A)

- **QBI treatment** — Kentucky does **not** allow the federal QBI deduction because Kentucky starts from federal AGI (before the QBI deduction). The QBI deduction does not affect Kentucky taxable income.

### Local occupational taxes

- **Local occupational taxes** — Many Kentucky cities and counties levy local occupational license taxes (e.g., Louisville Metro at ~2.2%, Lexington-Fayette at ~2.25%). These are separate from state income tax and are filed on separate local forms. Self-employed individuals are subject to these taxes on net self-employment income earned within the locality.

## Section 5: Tier 1 rules — deterministic

**Tier 1 rules table**

| Rule | Description |
| --- | --- |
| R-1 | Apply the flat 3.5% rate (TY2026) to Kentucky taxable income. No brackets. |
| R-2 | Start from federal AGI and apply Kentucky modifications. |
| R-3 | Subtract either the standard deduction ($3,360 for TY2026) or itemized deductions. |
| R-4 | Social Security benefits are fully exempt. |
| R-5 | U.S. government bond interest is exempt. |
| R-6 | Add back interest from out-of-state municipal bonds. |
| R-7 | The pension exclusion is up to $31,110 (2025 amount) for qualifying retirement income. |
| R-8 | Kentucky does NOT have local/county income taxes at the state level, but local occupational taxes are separate obligations. |

- **R-1** — Apply the flat 3.5% rate (TY2026) to Kentucky taxable income. No brackets.
- **R-2** — Start from federal AGI and apply Kentucky modifications.
- **R-3** — Subtract either the standard deduction ($3,360 for TY2026) or itemized deductions.
- **R-4** — Social Security benefits are fully exempt.
- **R-5** — U.S. government bond interest is exempt.
- **R-6** — Add back interest from out-of-state municipal bonds.
- **R-7** — The pension exclusion is up to $31,110 (2025 amount) for qualifying retirement income.
- **R-8** — Kentucky does NOT have local/county income taxes at the state level, but local occupational taxes are separate obligations.

## Section 6: Tier 2 rules — requires judgment

**Tier 2 rules table**

| Rule | Description |
| --- | --- |
| J-1 | Determine whether retirement income qualifies for the pension exclusion when income comes from multiple sources. |
| J-2 | Evaluate whether Kentucky itemized deductions exceed the standard deduction. |
| J-3 | Assess IRC conformity issues when Kentucky decouples from recent federal changes (review annually). |
| J-4 | Determine local occupational tax obligations based on where self-employment activity is performed. |
| J-5 | Evaluate credit for taxes paid to other states when the taxpayer has multi-state income. |

- **J-1** — Determine whether retirement income qualifies for the pension exclusion when income comes from multiple sources.
- **J-2** — Evaluate whether Kentucky itemized deductions exceed the standard deduction.
- **J-3** — Assess IRC conformity issues when Kentucky decouples from recent federal changes (review annually).
- **J-4** — Determine local occupational tax obligations based on where self-employment activity is performed.
- **J-5** — Evaluate credit for taxes paid to other states when the taxpayer has multi-state income.

## Section 7: Supplier pattern library

**Supplier pattern library table**

| Pattern | Kentucky treatment |
| --- | --- |
| Freelance income (Schedule C) | Flows through federal AGI → KY AGI. Subject to flat 3.5% state tax (TY2026). Also potentially subject to local occupational taxes. |
| Rental income (Schedule E) | Flows through federal AGI → KY AGI. Subject to flat rate. |
| Capital gains | Fully taxable at the flat rate. |
| Interest / dividends | Taxable except U.S. government obligations (exempt). |
| Social Security | Fully exempt from Kentucky income tax. |
| Pension / retirement | Up to $31,110 exempt under the pension exclusion (qualifying plans only). |

- **Freelance income (Schedule C)** — Flows through federal AGI → KY AGI. Subject to flat 3.5% state tax (TY2026). Also potentially subject to local occupational taxes.
- **Rental income (Schedule E)** — Flows through federal AGI → KY AGI. Subject to flat rate.
- **Capital gains** — Fully taxable at the flat rate.
- **Interest / dividends** — Taxable except U.S. government obligations (exempt).
- **Social Security** — Fully exempt from Kentucky income tax.
- **Pension / retirement** — Up to $31,110 exempt under the pension exclusion (qualifying plans only).

## Section 8: Form mapping

**Form mapping table**

| Form 740 line | Description | Source |
| --- | --- | --- |
| Line 5 | Federal AGI (Form 1040, Line 11) | Federal return |
| Line 6 | Additions to income | KRS 141.010 |
| Line 7 | Subtotal (Line 5 + Line 6) | Computed |
| Line 8 | Subtractions from income (Schedule M) | KRS 141.019 |
| Line 9 | Kentucky AGI (Line 7 − Line 8) | Computed |
| Line 11 | Standard or itemized deduction | KRS 141.081 |
| Line 13 | Kentucky taxable income | Line 9 − Line 11 |
| Line 14 | Kentucky tax (Line 13 × 3.5% for TY2026) | KRS 141.020 |
| Lines 22–27 | Credits | Various |
| Lines 28–35 | Payments, withholding, estimated payments | Various |
| Line 36 | Balance due or refund | Computed |

- **Federal AGI (Form 1040, Line 11)** — Line 5  _(Federal return)_
- **Additions to income** — Line 6  _(KRS 141.010)_
- **Subtotal (Line 5 + Line 6)** — Line 7  _(Computed)_
- **Subtractions from income (Schedule M)** — Line 8  _(KRS 141.019)_
- **Kentucky AGI (Line 7 − Line 8)** — Line 9  _(Computed)_
- **Standard or itemized deduction** — Line 11  _(KRS 141.081)_
- **Kentucky taxable income** — Line 13  _(Line 9 − Line 11)_
- **Kentucky tax (Line 13 × 3.5% for TY2026)** — Line 14  _(KRS 141.020)_
- **Credits** — Lines 22–27  _(Various)_
- **Payments, withholding, estimated payments** — Lines 28–35  _(Various)_
- **Balance due or refund** — Line 36  _(Computed)_

## Section 9: Refusal catalogue

**Refusal catalogue table**

| Code | Situation | Action |
| --- | --- | --- |
| REF-KY-01 | Taxpayer is a part-year or nonresident | Refuse; requires Form 740-NP. |
| REF-KY-02 | Taxpayer has LLET obligations | Refuse; requires Form 725 and specialist review. |
| REF-KY-03 | Taxpayer has partnership or S-corp K-1 with Kentucky-specific adjustments | Flag for reviewer. |
| REF-KY-04 | Taxpayer claims complex credits (e.g., KY Historic Preservation, Angel Investor, Film Industry) | Flag for reviewer. |
| REF-KY-05 | Taxpayer has local occupational tax filings in multiple jurisdictions | Flag for reviewer — requires separate local filings. |

- **REF-KY-01** — Taxpayer is a part-year or nonresident  _(Refuse; requires Form 740-NP.)_
- **REF-KY-02** — Taxpayer has LLET obligations  _(Refuse; requires Form 725 and specialist review.)_
- **REF-KY-03** — Taxpayer has partnership or S-corp K-1 with Kentucky-specific adjustments  _(Flag for reviewer.)_
- **REF-KY-04** — Taxpayer claims complex credits (e.g., KY Historic Preservation, Angel Investor, Film Industry)  _(Flag for reviewer.)_
- **REF-KY-05** — Taxpayer has local occupational tax filings in multiple jurisdictions  _(Flag for reviewer — requires separate local filings.)_

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
