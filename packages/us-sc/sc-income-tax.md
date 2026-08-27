---
name: sc-income-tax
description: Triggers when the taxpayer is a South Carolina resident sole proprietor or single-member LLC needing to file South Carolina Form SC1040. Covers SC's three-bracket graduated income tax (0%/3%/6% for tax year 2025, top rate recently reduced from 7%), the 3% reduced rate for active trade or business income, SC modifications to federal taxable income, and IRC conformity. Must be loaded alongside us-tax-workflow-base and us-federal-return-assembly.
version: "0.1"
jurisdiction: US-SC
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# SC Income Tax

## South Carolina Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** South Carolina Form SC1040 for tax year 2025 for full-year South Carolina resident sole proprietors and disregarded single-member LLCs. Covers SC's graduated income tax computation, the reduced 3% rate for active trade or business income (I-335), SC-specific additions and subtractions from federal taxable income, and the dependent exemption.
> **Quality tier.** Q3 — AI-drafted, not independently verified. All rates and thresholds have been researched from primary sources but must be confirmed by a qualified professional before use in return preparation.

## Section 1: Metadata

- **Tax year covered** — 2025 (returns originally due April 15, 2026; extended to October 15, 2026 by SCDOR)
- **Primary form** — SC1040 (South Carolina Individual Income Tax Return)
- **Tax authority** — [South Carolina Department of Revenue (SCDOR)](https://dor.sc.gov)
- **Tax type** — Graduated income tax
- **Currency date** — May 2026

**Section 1: Metadata field table**

| Field | Value |
| --- | --- |
| Tax year covered | 2025 (returns originally due April 15, 2026; extended to October 15, 2026 by SCDOR) |
| Primary form | SC1040 (South Carolina Individual Income Tax Return) |
| Tax authority | [South Carolina Department of Revenue (SCDOR)](https://dor.sc.gov) |
| Tax type | Graduated income tax |
| Currency date | May 2026 |

**Primary sources**

| Source | URL |
| --- | --- |
| S.C. Code Ann. § 12-6-510 (individual income tax rates) | https://www.scstatehouse.gov/code/t12c006.php |
| S.C. Code Ann. § 12-6-545 (reduced rate on active trade or business income) | https://www.scstatehouse.gov/code/t12c006.php |
| SC1040 Instructions (2025) | https://dor.sc.gov/forms |
| SC1040TT — 2025 Tax Tables | https://www.dor.sc.gov/sites/dor/files/forms/SC1040TT_2025.pdf |
| SCDOR — Individual Income Tax Page | https://dor.sc.gov/tax/individual-income |
| H. 4216 (2026 tax reform) | https://dor.sc.gov/news/information-about-h-4216 |

## Section 2: Quick reference — rates and thresholds

### Tax year 2025 — effective bracket structure

**SC taxable income (approximate) — effective rate**

| SC taxable income (approximate) | Effective rate |
| --- | --- |
| $0 – $3,560 (verify 2025) | 0% |
| $3,561 – $17,840 (verify 2025) | 3% |
| Over $17,840 (verify 2025) | 6% |

- **Simplified computation for income ≥ $100,000** — 6% × taxable income − $642

**Note:** The bracket thresholds are inflation-indexed annually. The exact 2025 thresholds should be verified against the SC1040TT. The top rate has been reduced from 7% (2021 and prior) to 6% for 2025 through a series of annual legislative reductions.

### Top rate history

**Top rate history table**

| Tax year | Top marginal rate |
| --- | --- |
| 2021 and prior | 7.0% |
| 2022 | 6.5% |
| 2023 | 6.4% |
| 2024 | 6.2% |
| 2025 | 6.0% |
| 2026 (H. 4216) | 5.21% (new two-bracket system) |

### Active trade or business income — reduced rate

**Active trade or business income reduced rate table**

| Item | Value |
| --- | --- |
| Reduced rate on active trade or business income | **3% flat** |
| Eligible entities | Sole proprietors, partnerships, S corps, LLCs taxed as partnerships or sole proprietorships |
| Form | I-335 (Active Trade or Business Income Reduced Rate Computation) |
| Election | Taxpayer elects on Form I-335; reported on SC1040 Line 8 |

This is a significant benefit for sole proprietors. Active trade or business income from a pass-through entity can be taxed at a flat 3% instead of the graduated rates (up to 6%).

### Standard / itemized deduction

- **SC standard/itemized deduction** — South Carolina does NOT have its own standard or itemized deduction for tax year 2025. The SC1040 starts from federal taxable income (which already includes the federal standard or itemized deduction).

### Dependent exemption (tax year 2025)

**SC dependent exemption table**

| Item | Value |
| --- | --- |
| SC dependent exemption | $4,930 per qualifying dependent |

### Other key figures

**Other key figures table**

| Item | Value |
| --- | --- |
| SC conforms to IRC as of | December 31, 2024 |
| Filing status | Follows federal |
| SC EITC | None (South Carolina does not have a state EITC) |

### 2026 reform alert (H. 4216)

Signed March 30, 2026, effective retroactive to January 1, 2026:
- **New two-bracket system:** 1.99% on income under $30,000; 5.21% on income $30,000 and above
- **New SC Income Adjusted Deduction (SCIAD):** replaces federal standard/itemized deduction coupling. $15,000 (single/MFS), $22,500 (HOH), $30,000 (MFJ/QSS)
- **Federal AGI becomes the starting point** (instead of federal taxable income)
- Automatic trigger mechanism for further rate reductions based on revenue growth
- **Does NOT affect 2025 returns** — 2025 returns use the pre-reform rules described in this skill

## Section 3: How this skill works with the federal return

- **Starting point and flow** — For tax year 2025, South Carolina starts from federal taxable income (federal Form 1040, Line 15). SC then applies additions and subtractions to arrive at SC income subject to tax. **Key flow:** 1. Federal taxable income → SC additions → SC subtractions = SC income subject to tax 2. Apply tax rates (from SC1040TT or simplified formula) → SC tax before active trade or business income election 3. If electing 3% rate: separate active trade or business income → compute on I-335 at 3% 4. Remaining income taxed at graduated rates 5. Apply credits → SC income tax liability

### Starting point: federal taxable income

- **No additional SC standard deduction** — Because SC starts from federal taxable income, the federal standard or itemized deduction is already included. SC does not provide an additional standard deduction for 2025.

## Section 4: Self-employed specific rules

### 3% reduced rate election (I-335) — critical for sole proprietors

- **I-335 election details** — South Carolina provides a reduced 3% flat rate on "active trade or business income" from pass-through businesses (S.C. Code Ann. § 12-6-545). For a sole proprietor, this means: - Schedule C net profit may qualify as active trade or business income - The taxpayer elects the reduced rate by completing Form I-335 - The qualified income is separated from the regular SC1040 computation and taxed at 3% flat - The remaining income is taxed at the regular graduated rates  _(S.C. Code Ann. § 12-6-545)_

**This is a substantial benefit.** A sole proprietor with $100,000 in Schedule C net profit would pay 3% ($3,000) on the business income instead of up to 6% ($5,358 via the standard computation).

### Definition of "active trade or business income"

- **Active trade or business income definition** — Per S.C. Code Ann. § 12-6-545 and SC Revenue Ruling #08-2: - Income must be from an active trade or business (not passive investment income) - The taxpayer must materially participate in the business - The income must flow through a pass-through entity (sole proprietorship qualifies) - Rental income generally does NOT qualify unless the taxpayer is a real estate professional  _(S.C. Code Ann. § 12-6-545 and SC Revenue Ruling #08-2)_

### SC modifications for self-employed

- **Common additions and subtractions** — **Common additions (SC1040 Line 2):** - State tax add-back: if the taxpayer itemized on the federal return and deducted state income taxes, add back the SC income tax portion - Other additions for items SC does not conform to **Common subtractions (SC1040 Line 4):** - State tax refund: if included in federal income - Military retirement income exclusion (up to $30,600 for those under 65, verify 2025) - Dependent exemption: $4,930 per qualifying dependent - SC retirement income deduction ($3,000 per qualifying individual, or $10,000 if 65+, verify 2025)

### IRC conformity

- **IRC conformity date and OBBBA note** — South Carolina conforms to the IRC as of December 31, 2024. For 2025, OBBBA provisions enacted after December 31, 2024 may or may not be conformed to — verify whether SC has enacted additional conformity legislation. If SC conforms to extended (but not amended) IRC sections, OBBBA provisions that simply extended existing law may flow through, but new OBBBA provisions may not.

## Section 5: Tier 1 rules — deterministic

- **R-SC-1** — Federal taxable income is the starting point. SC1040 Line 1 = federal Form 1040, Line 15.
- **R-SC-2** — State tax add-back if itemizing. If the taxpayer itemized federally and deducted SC state income taxes, add back on SC1040 Line 2a.
- **R-SC-3** — Dependent exemption is $4,930 per dependent. Claim on SC1040 Line w (subtraction section).
- **R-SC-4** — Use SC1040TT for tax computation. If taxable income < $100,000, use the tax tables. If ≥ $100,000, use the formula: 6% × taxable income − $642.
- **R-SC-5** — Active trade or business income may be taxed at 3%. Complete Form I-335 to elect the reduced rate. This is generally advantageous for any sole proprietor with net business income.
- **R-SC-6** — No state EITC. South Carolina does not offer a state earned income tax credit.

## Section 6: Tier 2 rules — requires judgment

- **J-SC-1** — Material participation for I-335 election. The taxpayer must materially participate in the trade or business to qualify for the 3% reduced rate. Apply the same material participation tests used for federal passive activity rules.
- **J-SC-2** — IRC conformity with OBBBA. Verify whether SC has enacted conformity to OBBBA provisions enacted after December 31, 2024. If not, adjustments may be needed for bonus depreciation, §179, and other OBBBA items.
- **J-SC-3** — Retirement income deduction eligibility. If the taxpayer is 65+ or receives qualifying retirement income, verify eligibility for the SC retirement income deduction. The deduction amount and rules vary based on age and income source.
- **J-SC-4** — Residency determination. SC considers a person domiciled in SC as a resident. For taxpayers who moved, part-year resident rules (Schedule NR) apply.

## Section 7: Supplier pattern library

**Supplier pattern library table**

| Pattern | Description |
| --- | --- |
| Sole proprietor with I-335 election | Always evaluate the 3% reduced rate on active trade or business income. For most sole proprietors, this produces significant savings vs. the 6% top rate. |
| Federal itemizer with state tax deduction | Must add back SC income taxes deducted on federal Schedule A. |
| Semi-retired freelancer | Check eligibility for SC retirement income deduction ($3,000 or $10,000 if 65+). |
| High-income sole proprietor | For income well above $100,000, use simplified formula (6% × income − $642) for non-business income, and 3% flat for business income via I-335. |
| Taxpayer approaching 2026 | 2026 brings major reform (H. 4216). Consider timing strategies — deferring income to 2026 may save tax due to lower 5.21% top rate and new SCIAD deduction. |

## Section 8: Form mapping

**Form mapping table**

| SC1040 line | Description | Source |
| --- | --- | --- |
| Line 1 | Federal taxable income | Federal Form 1040, Line 15 |
| Line 2 | Total additions | State tax add-back, other additions |
| Line 3 | Subtotal (Line 1 + Line 2) |  |
| Line 4 | Total subtractions | State refund, dependent exemption, retirement income, military pay |
| Line 5 | SC income subject to tax | Line 3 − Line 4 |
| Line 6 | Tax on SC income subject to tax | From SC1040TT or formula |
| Line 8 | Tax on active trade or business income | From Form I-335 (3% flat) |
| Line 10 | Total SC tax | Sum of Line 6 through Line 9 |
| Line 16 | SC income tax after credits | After withholding, estimated payments, credits |

## Section 9: Refusal catalogue

- **REFUSE-SC-1** — REFUSE to prepare a SC return for a nonresident or part-year resident without Schedule NR. This skill covers full-year residents only.
- **REFUSE-SC-2** — REFUSE to claim the I-335 reduced rate without confirming the taxpayer materially participates in the trade or business.
- **REFUSE-SC-3** — REFUSE to apply 2026 tax reform rules (H. 4216) to a 2025 return. The new two-bracket system (1.99%/5.21%) and SCIAD are effective January 1, 2026 only.
- **REFUSE-SC-4** — REFUSE to assume IRC conformity with post-December-31-2024 OBBBA provisions without verifying SC's enacted conformity position.

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
