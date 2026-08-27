---
name: ri-income-tax
description: Triggers when the taxpayer is a Rhode Island resident sole proprietor or single-member LLC needing to file Rhode Island Form RI-1040. Covers Rhode Island's three-bracket graduated income tax (3.75%–5.99% for tax year 2025), standard deduction, personal exemptions, RI modifications to federal AGI, and the new RI Schedule HR1 for OBBBA add-backs. Must be loaded alongside us-tax-workflow-base and us-federal-return-assembly.
version: "0.1"
jurisdiction: US-RI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# RI Income Tax

## Rhode Island Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** Rhode Island Form RI-1040 for tax year 2025 for full-year Rhode Island resident sole proprietors and disregarded single-member LLCs. Covers the three-bracket tax computation, RI modifications, standard and itemized deductions, and the new Schedule HR1 for OBBBA-related add-backs.
> **Quality tier.** Q3 — AI-drafted, not independently verified. All rates and thresholds have been researched from primary sources but must be confirmed by a qualified professional before use in return preparation.

## Section 1: Metadata

- **Tax year covered** — 2025 (returns due April 15, 2026)
- **Primary form** — RI-1040 (Rhode Island Resident Individual Income Tax Return)
- **Tax authority** — [Rhode Island Division of Taxation](https://tax.ri.gov)
- **Tax type** — Graduated income tax
- **Currency date** — May 2026

**Section 1 metadata table**

| Field | Value |
| --- | --- |
| Tax year covered | 2025 (returns due April 15, 2026) |
| Primary form | RI-1040 (Rhode Island Resident Individual Income Tax Return) |
| Tax authority | [Rhode Island Division of Taxation](https://tax.ri.gov) |
| Tax type | Graduated income tax |
| Currency date | May 2026 |

**Primary sources**

| Source | URL |
| --- | --- |
| R.I. Gen. Laws § 44-30 (personal income tax) | http://webserver.rilin.state.ri.us/Statutes/TITLE44/44-30/INDEX.HTM |
| RI-1040 Instructions (2025) | https://tax.ri.gov/tax-sections/personal-income-tax |
| RI Division of Taxation Advisory 2025-22 (2026 inflation adjustments) | https://tax.ri.gov/sites/g/files/xkgbur541/files/2025-11/ADV_2025_22_Inflation_Adjustments.pdf |
| RI 2025 Tax Tables (SC1040TT) | https://tax.ri.gov/sites/g/files/xkgbur541/files/2025-10/2025%20RI%20Tax%20Tables_Full_d.pdf |

## Section 2: Quick reference — rates and thresholds

### Tax brackets — all filing statuses (tax year 2025)

Rhode Island uses a uniform rate schedule that applies to all filing statuses.

**Tax brackets — all filing statuses (tax year 2025)**

| RI taxable income | Base tax | Rate | On excess over |
| --- | --- | --- | --- |
| $0 – $79,900 | $0 | 3.75% | $0 |
| $79,901 – $181,650 | $2,996.25 | 4.75% | $79,900 |
| Over $181,650 | $7,829.38 | 5.99% | $181,650 |

### Tax brackets — all filing statuses (tax year 2026, for reference)

**Tax brackets — all filing statuses (tax year 2026, for reference)**

| RI taxable income | Base tax | Rate | On excess over |
| --- | --- | --- | --- |
| $0 – $82,050 | $0 | 3.75% | $0 |
| $82,051 – $186,450 | $3,076.88 | 4.75% | $82,050 |
| Over $186,450 | $8,035.88 | 5.99% | $186,450 |

### Standard deduction (tax year 2025)

**Standard deduction (tax year 2025)**

| Filing status | Standard deduction |
| --- | --- |
| Single | $10,900 |
| MFJ / QSS | $21,800 |
| MFS | $10,900 |
| HOH | $16,350 |

### Personal exemption (tax year 2025)

**Personal exemption (tax year 2025)**

| Item | Value |
| --- | --- |
| Exemption amount per person | $5,100 |

### Other key figures

**Other key figures**

| Item | Value |
| --- | --- |
| RI EITC | 16% of federal EITC (partially refundable — 15% of the credit is refundable) |
| RI child tax credit | $500 per qualifying child under 6 (income limits apply, verify 2025) |
| Property tax circuit breaker credit | Available for low-income homeowners and renters |

## Section 3: How this skill works with the federal return

- **Starting point and flow** — Rhode Island starts from federal adjusted gross income (AGI) on federal Form 1040, Line 11. Rhode Island then applies modifications (additions and subtractions) to arrive at RI modified AGI, then subtracts the RI standard deduction (or itemized, if applicable) and personal exemptions to arrive at RI taxable income.
- **Key flow** — 1. Federal AGI → RI modifications (Schedule M) → RI modified AGI 2. RI modified AGI − standard or itemized deduction − exemptions = RI taxable income 3. Apply tax rates → RI tax before credits 4. Apply credits → RI income tax liability

### Important: RI Schedule HR1 (new for 2025)

- **Schedule HR1 required add-backs** — For tax year 2025, Rhode Island introduced Schedule HR1 to handle OBBBA-related add-backs. This schedule requires taxpayers to add back certain deductions claimed on the federal return under P.L. 119-21 (OBBBA), including: - Business interest expense deduction under §163(j) (if changed by OBBBA) - §174A amortization adjustment for R&E expenditures - §179(b) expensing limit increase - Qualified sound recording production deduction under §181

## Section 4: Self-employed specific rules

### RI modifications for self-employed

- **Common additions and subtractions** — **Common additions (RI taxes, federal does not):** - State/local income tax refund (if not already in federal AGI) - OBBBA-related add-backs via Schedule HR1 **Common subtractions (RI exempts, federal taxes):** - Social Security benefits (RI provides a subtraction for Social Security for taxpayers below certain income thresholds — verify 2025 rules, as RI recently expanded this) - Certain military pension income

### Rhode Island EITC

- **RI EITC** — 16% of the federal EITC for tax year 2025; partially refundable — 15% of the credit is refundable. Self-employment income qualifies.

### RI itemized deduction rules

- **Itemized deduction treatment** — If the taxpayer itemizes, Rhode Island uses the federal itemized deduction amount as a starting point. Rhode Island does NOT impose its own SALT cap. Taxpayers who itemize on the RI return generally use their federal Schedule A total (with RI-specific modifications if any).

## Section 5: Tier 1 rules — deterministic

- **R-RI-1** — Federal AGI is the starting point. RI-1040 starts from federal Form 1040, Line 11.  _(R-RI-1)_
- **R-RI-2** — Uniform rate schedule applies to all filing statuses. Unlike most states, RI uses the same tax brackets regardless of filing status. Only the standard deduction and exemption amounts vary by status.  _(R-RI-2)_
- **R-RI-3** — Standard deduction is based on filing status. $10,900 (single/MFS), $21,800 (MFJ/QSS), $16,350 (HOH) for 2025.  _(R-RI-3)_
- **R-RI-4** — Personal exemption is $5,100 per person. Subject to income-based phase-out for high earners.  _(R-RI-4)_
- **R-RI-5** — RI EITC = 16% of federal EITC. Partially refundable (15% of the credit is the refundable portion). Self-employment income qualifies.  _(R-RI-5)_
- **R-RI-6** — Schedule HR1 is mandatory for OBBBA add-backs. If the taxpayer claimed any OBBBA-specific deductions on the federal return (§163(j), §174A, §179(b) increase, §181), complete Schedule HR1 to add these back.  _(R-RI-6)_
- **R-RI-7** — Tax tables for income under $100,000. Use the RI tax tables for taxable income under $100,000; use the tax computation worksheet for $100,000 and above.  _(R-RI-7)_

## Section 6: Tier 2 rules — requires judgment

- **J-RI-1** — Social Security exemption eligibility. Rhode Island has been expanding its Social Security exemption. Verify the 2025 income thresholds for the Social Security subtraction — it may now be available to a wider range of taxpayers than in prior years.  _(J-RI-1)_
- **J-RI-2** — OBBBA conformity determination. Rhode Island introduced Schedule HR1 to decouple from specific OBBBA provisions. Judgment is needed to determine exactly which federal deductions were claimed under OBBBA and must be added back.  _(J-RI-2)_
- **J-RI-3** — Residency determination. RI considers a person domiciled in RI or maintaining a permanent place of abode in RI while spending 183+ days there as a resident. For taxpayers who moved, nonresident/part-year rules apply.  _(J-RI-3)_
- **J-RI-4** — Property tax credit eligibility. The RI property tax circuit breaker credit has specific income and property tax thresholds. Verify eligibility.  _(J-RI-4)_

## Section 7: Supplier pattern library

**Supplier pattern library**

| Pattern | Description |
| --- | --- |
| OBBBA filer | Must complete Schedule HR1 to add back OBBBA-specific deductions (§163(j), §174A, §179(b), §181). |
| Low-income freelancer with children | Check eligibility for RI EITC (16% of federal) and RI child tax credit ($500/child under 6). |
| Social Security recipient | Verify eligibility for RI Social Security subtraction based on income thresholds. |
| High earner (>$181,650) | Top bracket at 5.99%. Plus personal exemption phase-out may apply. |
| Standard vs. itemized | RI standard deduction is relatively generous ($10,900 single). Compare against itemized before choosing. |

## Section 8: Form mapping

**Form mapping**

| RI-1040 line | Description | Source |
| --- | --- | --- |
| Line 1 | Federal AGI | Federal Form 1040, Line 11 |
| Line 2 | Modifications (additions/subtractions) | Schedule M |
| Line 2a | OBBBA add-backs | Schedule HR1 |
| Line 3 | RI modified AGI | Line 1 ± modifications |
| Line 4 | Deduction (standard or itemized) | Standard deduction or RI Schedule A |
| Line 5 | Exemptions | $5,100 per person |
| Line 7 | RI taxable income | Line 3 − deduction − exemptions |
| Line 8 | RI income tax | Tax tables or tax computation worksheet |
| Line 14 | RI EITC | 16% of federal EITC |
| Line 18 | RI tax after credits | After all credits applied |

## Section 9: Refusal catalogue

- **REFUSE-RI-1** — REFUSE to prepare a RI return for a part-year resident or nonresident without Form RI-1040NR. This skill covers full-year residents only.  _(REFUSE-RI-1)_
- **REFUSE-RI-2** — REFUSE to skip Schedule HR1 if the taxpayer claimed any OBBBA-specific deductions on the federal return. The schedule is mandatory for 2025.  _(REFUSE-RI-2)_
- **REFUSE-RI-3** — REFUSE to claim the Social Security subtraction without verifying income eligibility thresholds for 2025.  _(REFUSE-RI-3)_
- **REFUSE-RI-4** — REFUSE to apply 2026 inflation-adjusted brackets ($82,050 / $186,450) to a 2025 return. Use the 2025 brackets ($79,900 / $181,650).  _(REFUSE-RI-4)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
