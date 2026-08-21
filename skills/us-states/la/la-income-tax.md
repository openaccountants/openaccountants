---
name: la-income-tax
description: Use this skill whenever asked about Louisiana individual income tax. Trigger on phrases like "Louisiana income tax", "LA income tax", "IT-540", "LDR", "R.S. 47:21", "Louisiana flat tax". Louisiana reformed to a flat 3% rate effective 2025 (Act 11 of 2024 3rd Extraordinary Session). ALWAYS load us-tax-workflow-base first.
version: "0.1"
jurisdiction: US-LA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# LA Income Tax

## Louisiana Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers Louisiana Form IT-540 (Resident Individual Income Tax Return) for sole proprietors and single-member LLCs. It addresses the flat 3% income tax rate (effective 2025), the significantly increased standard deduction, and Louisiana-specific modifications to federal AGI. It does NOT cover nonresident returns (Form IT-540B), corporate returns (CIFT-620), or partnership/S-corp pass-throughs.

> **Quality tier.** Q3 — AI-drafted, not independently verified. All outputs must be reviewed by a qualified tax professional before filing.

## Section 1: Metadata

**Metadata table**

| Field | Value |
| --- | --- |
| Jurisdiction | Louisiana (US-LA) |
| Tax authority | [Louisiana Department of Revenue (LDR)](https://revenue.louisiana.gov/) |
| Filing portal | [Louisiana File Online](https://revenue.louisiana.gov/EServices) |
| Legislation | La. R.S. 47:21 et seq.; Act 11 of the 2024 Third Extraordinary Session |
| Primary form | Form IT-540 (Louisiana Resident Individual Income Tax Return) |
| Filing deadline | May 15, 2027 (for tax year 2026) — Louisiana uses May 15, not April 15 |
| Version | 0.1 |
| Date | May 22, 2026 |
| Validation status | AI-drafted — Q3 |

### Sources consulted

1. Louisiana Department of Revenue — Revenue Information Bulletin 25-012 (Income Tax Reform): <https://dam.ldr.la.gov/lawspolicies/RIB-25-012-Louisiana-Individual-Income-Tax-Reform-1.pdf>
2. LDR — 2025 IT-540 Instructions: <https://revenue.louisiana.gov/tax-forms/individuals/>
3. EY Tax News — Louisiana flat income tax rate: <https://taxnews.ey.com/news/2024-2322-louisiana-law-implements-a-flat-personal-income-tax-rate-starting-in-2025>
4. La. R.S. 47:32 — Tax rate
5. Act 11 (H.B. 10) of the 2024 Third Extraordinary Session

## Section 2: Quick reference — rates and thresholds

### State income tax rate

**State income tax rate table**

| Tax year | Rate | Source |
| --- | --- | --- |
| 2024 and prior | Graduated: 1.85% / 3.50% / 4.25% | La. R.S. 47:32 (prior law) |
| 2025 and after | **Flat 3.00%** | Act 11 (H.B. 10, 2024 3rd Extraordinary Session) |

- **Flat rate effective date** — Effective January 1, 2025, Louisiana replaced its three-bracket graduated system with a flat 3% rate on all taxable income, for all filing statuses.  _(Act 11 (H.B. 10, 2024 3rd Extraordinary Session))_

### Standard deduction (2025 tax year)

**Standard deduction table**

| Filing status | Amount |
| --- | --- |
| Single | $12,500 |
| Married Filing Separately | $12,500 |
| Married Filing Jointly | $25,000 |
| Head of Household | $25,000 |
| Qualifying Surviving Spouse | $25,000 |

- **Standard deduction note** — These amounts were significantly increased by Act 11 (previously $4,500 / $9,000). Beginning January 1, 2026, the standard deduction is adjusted annually for CPI inflation.  _(Act 11)_

### Personal exemptions

- **Personal exemptions repealed** — Act 11 repealed the prior personal exemptions ($1,000 for age 65+, blind, and dependents). These are no longer available for TY2025+.  _(Act 11)_

### Retirement income exemption

- **Retirement income exemption** — $12,000 USD (annual retirement income exempt for taxpayers age 65+; adjusted annually for CPI beginning in 2026)

## Section 3: How this skill works with the federal return

### Starting point

- **Starting point** — Louisiana starts from federal adjusted gross income (AGI) — Form 1040, Line 11.

### Additions to income

**Additions to income table**

| Item | Description | Source |
| --- | --- | --- |
| Out-of-state bond interest | Interest on bonds of other states must be added | La. R.S. 47:293(4) |
| Federal income tax deducted | Louisiana historically allowed a deduction for federal taxes; under the reformed law, verify if this continues to apply | La. R.S. 47:293 |
| IRC decoupling items | Any areas where Louisiana decouples from federal tax code changes | La. R.S. 47 |

### Subtractions from income

**Subtractions from income table**

| Item | Description | Source |
| --- | --- | --- |
| U.S. government interest | Interest on U.S. obligations | La. R.S. 47:293(6) |
| Social Security benefits | Louisiana exempts Social Security | La. R.S. 47:44.2 |
| Federal income taxes paid | Louisiana allows a deduction for federal income taxes paid (may be limited under new law — verify) | La. R.S. 47:293(3) |
| Retirement income | Up to $12,000 for taxpayers age 65+ | La. R.S. 47:44.1 |
| Military pay | Active-duty military compensation exclusion | La. R.S. 47:293 |

### Resulting computation

- **Louisiana taxable income and tax formula** — Federal AGI + additions − subtractions − standard deduction = Louisiana taxable income → times 3% = Louisiana income tax.

**Important:** Louisiana has historically allowed a deduction for federal income taxes paid, which is unusual among states. Under the 2025 reform, confirm the current treatment of this deduction.

## Section 4: Self-employed specific rules

### Estimated tax payments

- **Estimated payment requirement** — Self-employed individuals must make quarterly estimated tax payments if they expect to owe $1,000 or more.

**Estimated tax payment due dates**

| Voucher | Due date |
| --- | --- |
| 1st quarter | April 15 |
| 2nd quarter | June 15 |
| 3rd quarter | September 15 |
| 4th quarter | January 15 (following year) |

- **Estimated payment form** — Use Form IT-540ES for estimated payments.

### Self-employment health insurance

- **Self-employment health insurance treatment** — Louisiana follows federal treatment — the deduction reduces federal AGI and flows through.

### Retirement contributions (SEP, SIMPLE, Solo 401(k))

- **Retirement contributions treatment** — Louisiana follows federal treatment — these deductions reduce federal AGI and flow through.

### Home office deduction

- **Home office deduction treatment** — Louisiana follows the federal home office deduction as part of Schedule C, included in federal AGI.

### QBI deduction (Section 199A)

- **QBI deduction treatment** — Louisiana does not allow the federal QBI deduction because Louisiana starts from federal AGI (before the QBI deduction). The QBI deduction does not affect Louisiana taxable income.

### Filing deadline

- **Filing deadline** — Louisiana's individual income tax return deadline is May 15 (not April 15). This is one month later than most states.

## Section 5: Tier 1 rules — deterministic

**Tier 1 rules table**

| Rule | Description |
| --- | --- |
| R-1 | Apply the flat 3% rate to Louisiana taxable income. No brackets for TY2025+. |
| R-2 | Start from federal AGI and apply Louisiana modifications. |
| R-3 | Subtract the standard deduction ($12,500 single/MFS; $25,000 MFJ/HoH/QSS for TY2025). |
| R-4 | Social Security benefits are fully exempt. |
| R-5 | U.S. government bond interest is exempt. |
| R-6 | Retirement income exemption: up to $12,000 for age 65+. |
| R-7 | The filing deadline is May 15, NOT April 15. |
| R-8 | Prior personal exemptions ($1,000 for age 65+, blind, dependents) were repealed by Act 11 for TY2025+. |
| R-9 | Standard deduction is adjusted annually for CPI beginning in TY2026. |

## Section 6: Tier 2 rules — requires judgment

**Tier 2 rules table**

| Rule | Description |
| --- | --- |
| J-1 | Determine the current-year treatment of the federal income tax deduction under the reformed law. |
| J-2 | Evaluate whether itemized deductions exceed the increased standard deduction (less likely under the new $12,500/$25,000 amounts). |
| J-3 | Assess IRC conformity for any areas where Louisiana decouples from recent federal changes. |
| J-4 | Determine the CPI-adjusted standard deduction and retirement exemption amounts for TY2026+. |
| J-5 | Evaluate credit for taxes paid to other states for multi-state taxpayers. |

## Section 7: Supplier pattern library

**Supplier pattern library table**

| Pattern | Louisiana treatment |
| --- | --- |
| Freelance income (Schedule C) | Flows through federal AGI → LA taxable income. Subject to flat 3% state tax. |
| Rental income (Schedule E) | Flows through federal AGI → LA taxable income. Subject to flat 3%. |
| Capital gains | Fully taxable at the flat 3% rate. |
| Interest / dividends | Taxable except U.S. government obligations (exempt). |
| Social Security | Fully exempt. |
| Retirement distributions | Up to $12,000 exempt for age 65+; remainder taxable at 3%. |

## Section 8: Form mapping

**Form mapping table**

| Form IT-540 line | Description | Source |
| --- | --- | --- |
| Line 7 | Federal AGI (Form 1040, Line 11) | Federal return |
| Line 8 | Louisiana standard deduction ($12,500 or $25,000) | La. R.S. 47:293; Act 11 |
| Line 9 | Adjustments and modifications | La. R.S. 47:293 |
| Line 10 | Louisiana taxable income | Computed |
| Line 11 | Louisiana income tax (Line 10 × 3%) | La. R.S. 47:32 (as amended) |
| Lines 12–19 | Credits (nonrefundable and refundable) | Various |
| Lines 20–25 | Payments, withholding, estimated payments | Various |
| Line 30 | Balance due or refund | Computed |

## Section 9: Refusal catalogue

**Refusal catalogue table**

| Code | Situation | Action |
| --- | --- | --- |
| REF-LA-01 | Taxpayer is a nonresident or part-year resident | Refuse; requires Form IT-540B. |
| REF-LA-02 | Taxpayer has complex federal income tax deduction computations | Flag for reviewer — interaction between federal and state deductions requires specialist analysis. |
| REF-LA-03 | Taxpayer has partnership or S-corp K-1 with Louisiana-specific adjustments | Flag for reviewer. |
| REF-LA-04 | Taxpayer claims complex credits (e.g., LA Historic Rehabilitation, Motion Picture, Enterprise Zone) | Flag for reviewer — separate forms required. |
| REF-LA-05 | Taxpayer needs CPI-adjusted amounts for TY2026+ | Flag for reviewer — confirm published inflation-adjusted figures. |

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
