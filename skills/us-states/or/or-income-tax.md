---
name: or-income-tax
description: Triggers when the taxpayer is an Oregon resident sole proprietor or single-member LLC needing to file Oregon Form OR-40. Covers Oregon's four-bracket graduated income tax (4.75%–9.9% for tax year 2025), standard and itemized deductions, personal exemption credit, federal tax subtraction, and Oregon's unique no-sales-tax environment. Must be loaded alongside us-tax-workflow-base and us-federal-return-assembly.
version: "0.1"
jurisdiction: US-OR
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# OR Income Tax

## Oregon Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** Oregon Form OR-40 (Full-Year Resident) for tax year 2025 for full-year Oregon resident sole proprietors and disregarded single-member LLCs. Covers Oregon's four-bracket graduated income tax, standard and itemized deductions, Oregon-specific modifications to federal income, and credits.
> **Quality tier.** Q3 — AI-drafted, not independently verified. All rates and thresholds have been researched from primary sources but must be confirmed by a qualified professional before use in return preparation.

## Section 1: Metadata

- **Tax year covered** — 2025 (returns due April 15, 2026)
- **Primary form** — Oregon Form OR-40 (Full-Year Resident)
- **Tax authority** — [Oregon Department of Revenue](https://www.oregon.gov/dor)
- **Tax type** — Graduated income tax
- **Currency date** — May 2026

**Section 1 metadata table**

| Field | Value |
| --- | --- |
| Tax year covered | 2025 (returns due April 15, 2026) |
| Primary form | Oregon Form OR-40 (Full-Year Resident) |
| Tax authority | [Oregon Department of Revenue](https://www.oregon.gov/dor) |
| Tax type | Graduated income tax |
| Currency date | May 2026 |

**Primary sources**

| Source | URL |
| --- | --- |
| Oregon Revised Statutes Chapter 316 (personal income tax) | https://www.oregonlegislature.gov/bills_laws/ors/ors316.html |
| 2025 Form OR-40 Instructions (Publication OR-40-FY) | https://www.oregon.gov/dor/programs/individuals/Pages/PIT.aspx |
| Oregon Tax Rate Charts (2025) | https://www.oregon.gov/dor/programs/individuals/Pages/PIT.aspx |

## Section 2: Quick reference — rates and thresholds

### Tax brackets — Single and Married Filing Separately (tax year 2025)

**Tax brackets — Single and Married Filing Separately (tax year 2025)**

| Oregon taxable income | Tax |
| --- | --- |
| $0 – $4,400 | 4.75% of taxable income |
| $4,401 – $11,100 | $209 + 6.75% of excess over $4,400 |
| $11,101 – $125,000 | $661 + 8.75% of excess over $11,100 |
| Over $125,000 | $10,627 + 9.9% of excess over $125,000 |

### Tax brackets — MFJ, HOH, and Qualifying Surviving Spouse (tax year 2025)

**Tax brackets — MFJ, HOH, and Qualifying Surviving Spouse (tax year 2025)**

| Oregon taxable income | Tax |
| --- | --- |
| $0 – $8,800 | 4.75% of taxable income |
| $8,801 – $22,200 | $418 + 6.75% of excess over $8,800 |
| $22,201 – $250,000 | $1,323 + 8.75% of excess over $22,200 |
| Over $250,000 | $21,256 + 9.9% of excess over $250,000 |

### Standard deduction (tax year 2025)

**Standard deduction (tax year 2025)**

| Filing status | Standard deduction |
| --- | --- |
| Single | $2,835 |
| MFJ | $5,670 |
| HOH | $4,560 |
| MFS | $2,835 |

### Personal exemption credit (tax year 2025)

**Personal exemption credit (tax year 2025)**

| Item | Value |
| --- | --- |
| Credit per exemption | $256 |
| Income phase-out begins | $100,000 (single) / $200,000 (MFJ) |

### Other key figures

**Other key figures**

| Item | Value |
| --- | --- |
| Oregon EITC | 12% of federal EITC (refundable) for those with qualifying children under 3; 9% otherwise |
| Oregon kicker credit | Varies by year — taxpayers receive a credit when state revenues exceed projections by >2%. Check for 2025. |
| No sales tax | Oregon has no state or local sales tax |
| Estimated tax interest rate | 9% for 2025, 8% for 2026 |

## Section 3: How this skill works with the federal return

Oregon starts from **federal taxable income** (federal Form 1040, Line 15), NOT federal AGI. This is a critical difference from most states. Oregon then applies Oregon-specific additions and subtractions on Schedule OR-ASC to arrive at Oregon taxable income.

**Key flow:**

1. Federal taxable income → Oregon additions → Oregon subtractions → Oregon taxable income
2. Apply graduated tax rates → Oregon tax before credits
3. Apply credits (personal exemption credits, EITC, kicker, etc.) → Oregon income tax liability

### Critical: Oregon starts from federal taxable income

- **Oregon starts from federal taxable income; standard deduction stacks on top** — Because Oregon starts from federal taxable income (which already includes the federal standard or itemized deduction), Oregon allows its own standard deduction on top. The Oregon standard deduction is relatively small ($2,835 single) because the federal deduction has already been taken. **However,** Oregon requires modifications for items where Oregon does not conform to the IRC: - Oregon additions (income Oregon taxes but federal does not, or deductions federal allows but Oregon does not) - Oregon subtractions (income federal taxes but Oregon does not, or deductions Oregon allows but federal does not)

## Section 4: Self-employed specific rules

### No sales tax advantage

- **No sales tax advantage** — Oregon's lack of a sales tax means sole proprietors selling goods to Oregon customers do not need to collect Oregon sales tax. However, they may still need to collect sales tax for sales to customers in other states with economic nexus.

### Oregon EITC

- **Oregon EITC** — Oregon provides a refundable earned income tax credit: - 12% of federal EITC for taxpayers with a qualifying child under age 3 - 9% of federal EITC for all other qualifying taxpayers - ITIN filers are eligible for the Oregon EITC - Self-employment income qualifies

### Oregon-specific local taxes (warning)

- **Local taxes warning** — Self-employed individuals in certain parts of Oregon face additional local taxes that are NOT part of the state income tax but may be filed alongside it: - **TriMet self-employment tax** (Portland metro area): rate varies, approximately 0.8237% (verify 2025) - **Lane Transit District (LTD) tax** (Eugene/Springfield area): approximately 0.80% (verify 2025) - **Metro Supportive Housing Services (SHS) tax**: 1% on taxable income above $125,000 (single) / $200,000 (MFJ) for residents of Clackamas, Multnomah, and Washington counties - **Multnomah County Preschool for All (PFA) tax**: 1.5% on taxable income above $125,000 (single) / $200,000 (MFJ); additional 1.5% above $250,000 (single) / $400,000 (MFJ) - **Statewide Transit Tax (STT)**: 0.1% of wages (self-employed individuals are subject via Form OR-STT) These are separate filings and are NOT covered by this skill.

### Oregon additions (common for self-employed)

- **Oregon additions list** — - Federal income taxes (if deducted on federal Schedule A — not applicable if taxpayer took the federal standard deduction) - Interest/dividends from other states' bonds (Oregon taxes these; federal may not) - Bonus depreciation add-back (if Oregon does not conform to federal §168(k) — verify conformity) - OBBBA-specific deductions not conformed to by Oregon (verify)

### Oregon subtractions (common for self-employed)

- **Oregon subtractions list** — - Oregon income tax refund (if included in federal income) - Federal tax paid on a fiscal-year basis (if applicable) - Interest on U.S. government obligations (Oregon cannot tax federal bond interest) - Social Security benefits (Oregon fully exempts Social Security — subtract if included in federal taxable income) - Oregon 529 plan contributions (subtraction up to $300 per student for single, $600 for MFJ)

## Section 5: Tier 1 rules — deterministic

- **R-OR-1. Federal taxable income is the starting point.** — Form OR-40 Line 7 = federal Form 1040, Line 15 (federal taxable income). This includes the federal standard or itemized deduction already.
- **R-OR-2. Oregon standard deduction is in addition to federal.** — The Oregon standard deduction ($2,835 single / $5,670 MFJ) is subtracted from Oregon adjusted income to arrive at Oregon taxable income.
- **R-OR-3. Social Security is fully exempt.** — Subtract any Social Security benefits that were included in federal taxable income.
- **R-OR-4. Oregon income tax refund subtraction.** — If the taxpayer received an Oregon income tax refund in 2025 and included it in federal income (Schedule 1 Line 1), subtract it on the Oregon return — Oregon does not tax its own refund.
- **R-OR-5. U.S. government bond interest is exempt.** — Subtract interest from U.S. Treasury obligations, I-bonds, and other federal securities included in federal income.
- **R-OR-6. Personal exemption credit is $256 per exemption.** — Apply after computing tax, subject to income phase-out.
- **R-OR-7. Oregon EITC is refundable.** — Compute at 9% (or 12% with qualifying child under 3) of federal EITC.

## Section 6: Tier 2 rules — requires judgment

- **J-OR-1. Oregon conformity with OBBBA.** — Oregon's IRC conformity date must be verified. If Oregon does not conform to specific OBBBA provisions (§168(k) bonus depreciation, §179, §174A R&E), additions on Schedule OR-ASC may be required.
- **J-OR-2. Standard vs. itemized deduction choice.** — Oregon allows a separate standard deduction even though federal taxable income already reflects the federal deduction. The small Oregon standard deduction ($2,835 single) means most taxpayers should take it unless specific Oregon itemized deductions are advantageous.
- **J-OR-3. TriMet / LTD / Metro SHS / PFA applicability.** — Self-employed individuals in the Portland metro or Eugene/Springfield areas must determine whether they are subject to local transit and housing services taxes. Geographic location of the taxpayer's residence determines applicability.
- **J-OR-4. Oregon kicker credit availability.** — The kicker is a unique Oregon mechanism that returns excess state revenue to taxpayers. Whether a kicker is available for tax year 2025 depends on state revenue performance. Verify availability and amount.

## Section 7: Supplier pattern library

**Supplier pattern library**

| Pattern | Description |
| --- | --- |
| Portland-area freelancer | Subject to TriMet SE tax + Metro SHS tax + potentially Multnomah PFA tax in addition to state income tax. Combined marginal rate can exceed 14%. Flag all local obligations. |
| Federal taxable income reconciliation | Oregon starts from federal taxable income, not AGI. Ensure correct line reference (1040 Line 15, not Line 11). |
| Social Security recipient | Full subtraction of Social Security from Oregon taxable income. |
| No sales tax seller | No Oregon sales tax collection needed, but may have nexus in other states. |
| High-income earner (>$125K single) | Top bracket at 9.9% plus potential Metro SHS (1%) and PFA (1.5%+) taxes if in Portland metro. |

## Section 8: Form mapping

**Form OR-40 line mapping**

| Form OR-40 line | Description | Source |
| --- | --- | --- |
| Line 7 | Federal taxable income | Federal Form 1040, Line 15 |
| Lines 8–13 | Oregon additions | Schedule OR-ASC (Section A) |
| Lines 14–18 | Oregon subtractions | Schedule OR-ASC (Section B) |
| Line 19 | Oregon taxable income | After additions, subtractions, and Oregon standard deduction |
| Line 20 | Oregon tax | Tax tables (if <$50,000) or rate chart (if ≥$50,000) |
| Line 22 | Oregon tax after standard/special credits | After exemption credits and other nonrefundable credits |
| Line 32 | Oregon EITC | 9% or 12% of federal EITC |
| Line 34 | Kicker credit | If applicable for the tax year |
| Line 44 | Total tax after all credits | Final Oregon tax liability |

## Section 9: Refusal catalogue

- **REFUSE-OR-1** — REFUSE to prepare an Oregon return for a part-year resident or nonresident without Form OR-40-P or OR-40-N. This skill covers full-year residents only.
- **REFUSE-OR-2** — REFUSE to compute TriMet, LTD, Metro SHS, or Multnomah PFA taxes. These are separate local taxes with their own rules, forms, and filing requirements.
- **REFUSE-OR-3** — REFUSE to compute Oregon Corporate Activity Tax (CAT). The CAT is a business-level tax ($250 + 0.57% on taxable commercial activity over $1M) that applies to larger businesses and is outside the scope of this individual income tax skill.
- **REFUSE-OR-4** — REFUSE to determine the Oregon kicker credit amount without verifying the kicker status for the specific tax year. The kicker is not available every year.
- **REFUSE-OR-5** — REFUSE to apply Oregon tax rates to a return without verifying Oregon's current IRC conformity date and any OBBBA decoupling provisions.

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
