---
name: oh-income-tax
description: Triggers when the taxpayer is an Ohio resident sole proprietor or single-member LLC needing to file Ohio Form IT 1040. Covers Ohio's graduated income tax on nonbusiness income (0%, 2.75%, 3.125% for tax year 2025), the business income deduction ($250,000 exclusion taxed at flat 3%), Ohio Schedule of Adjustments, and interaction with federal AGI. Must be loaded alongside us-tax-workflow-base and us-federal-return-assembly.
version: "0.1"
jurisdiction: US-OH
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# OH Income Tax

## Ohio Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** Ohio Form IT 1040 for tax year 2025 for full-year Ohio resident sole proprietors and disregarded single-member LLCs. Covers nonbusiness income tax computation, business income deduction (BID), Ohio Schedule of Adjustments, and personal credits and exemptions.
> **Quality tier.** Q3 — AI-drafted, not independently verified. All rates and thresholds have been researched from primary sources but must be confirmed by a qualified professional before use in return preparation.

## Section 1: Metadata

**Metadata fields**

| Field | Value |
| --- | --- |
| Tax year covered | 2025 (returns due April 15, 2026) |
| Primary form | Ohio IT 1040 |
| Tax authority | [Ohio Department of Taxation](https://tax.ohio.gov) |
| Tax type | Graduated income tax (nonbusiness); flat rate (business) |
| Filing threshold | Ohio AGI > $0 (Ohio requires filing for all residents with income; see exemption below) |
| Currency date | May 2026 |

**Primary sources**

| Source | URL |
| --- | --- |
| Ohio Revised Code § 5747.02 (income tax rates) | https://codes.ohio.gov/ohio-revised-code/section-5747.02 |
| Ohio IT 1040 Instructions (2025) | https://tax.ohio.gov/individual/file-now/it-1040-instructions |
| Ohio Annual Tax Rates | https://tax.ohio.gov/individual/file-now/annual-tax-rates |
| Ohio HB 96 (2025 — flat tax transition for 2026) | https://www.legislature.ohio.gov/legislation/135/hb96 |

### Nonbusiness income tax brackets (tax year 2025)

**Nonbusiness income tax brackets (tax year 2025)**

| Ohio taxable nonbusiness income | Tax |
| --- | --- |
| $0 – $26,050 | 0% (no tax) |
| $26,051 – $100,000 | $342.00 + 2.75% of excess over $26,050 |
| Over $100,000 | $2,394.32 + 3.125% of excess over $100,000 |

All filing statuses use the same bracket structure. Ohio does not differentiate brackets by filing status.

### Business income

**Business income figures**

| Item | Value |
| --- | --- |
| Business Income Deduction (BID) | First $250,000 excluded ($125,000 if MFS) |
| Tax rate on business income above BID | 3% flat |

### Personal exemptions (based on Ohio AGI)

**Personal exemptions**

| Ohio AGI | Exemption per person |
| --- | --- |
| $40,000 or less | $2,400 |
| $40,001 – $80,000 | $2,150 |
| $80,001 and above | $1,900 |

### Other key figures

**Other key figures**

| Item | Value |
| --- | --- |
| Standard deduction | None (Ohio does not have a state standard deduction) |
| Filing status options | Single, MFJ, MFS, HOH, QSS (follows federal) |
| Personal credits | Joint filer credit, child/dependent care credit, earned income credit (10% of federal EITC, nonrefundable), retirement income credit, lump-sum credit |
| Ohio EITC | 10% of federal EITC (nonrefundable for 2025) |

### 2026 change alert

- **2026 flat tax transition** — Starting tax year 2026 (HB 96, signed June 30, 2025), Ohio moves to a true flat tax: 0% on the first $26,050 and 2.75% flat on all nonbusiness income above $26,050. The 3.125% bracket is eliminated.  _(Ohio HB 96 (2025 — flat tax transition for 2026))_

## Section 3: How this skill works with the federal return

Ohio starts from **federal adjusted gross income (AGI)** on federal Form 1040, Line 11. Ohio then applies its own adjustments on the Ohio Schedule of Adjustments to arrive at Ohio AGI, then separates income into business and nonbusiness categories.

**Key flow:**

1. Federal AGI → Ohio Schedule of Adjustments → Ohio AGI
2. Ohio AGI → separate into business income and nonbusiness income
3. Business income: first $250,000 excluded via BID; excess taxed at 3% flat
4. Nonbusiness income: taxed at graduated rates (0% / 2.75% / 3.125%)
5. Apply exemptions and credits → Ohio income tax liability

**Ohio does NOT start from federal taxable income.** The starting point is federal AGI. Ohio does not use the federal standard or itemized deductions. Ohio has no standard deduction of its own.

### Business Income Deduction (BID)

- **Business Income Deduction (BID)** — The first $250,000 of business income ($125,000 if MFS) is fully deductible — effectively taxed at 0%. Business income exceeding the BID threshold is taxed at a flat 3% rate, separate from the graduated nonbusiness brackets. "Business income" for a sole proprietor generally means Schedule C net profit, plus other income from business activity (Schedule E rental income from active businesses, farm income from Schedule F, etc.). The BID election is made on Ohio Schedule IT BUS.  _(ORC § 5747.01(B))_

### Self-employment tax interaction

- **Self-employment tax interaction** — Ohio does not impose a separate self-employment tax. The federal self-employment tax (Social Security and Medicare) is computed on the federal return only. However, the deductible portion of SE tax (50% deduction on federal Schedule 1) reduces federal AGI, which flows through to reduce Ohio AGI.

### Ohio Municipal Income Tax (warning)

Most Ohio cities and many school districts levy their own local income taxes (typically 1%–3%). These are separate from state income tax and are NOT covered by this skill. Self-employed individuals must file and pay municipal income tax in their city of residence and potentially in cities where they perform work.

## Section 5: Tier 1 rules — deterministic

- **R-OH-1. Federal AGI is the starting point.** — Ohio IT 1040 Line 1 = federal Form 1040 Line 11 (federal AGI).  _(R-OH-1)_
- **R-OH-2. Ohio Schedule of Adjustments.** — Common adjustments for self-employed filers: - **Additions:** state/local government bond interest from other states; federal tax-exempt income items that Ohio taxes - **Subtractions:** Ohio state/local government bond interest; Social Security benefits (Ohio fully exempts Social Security); federal interest/dividend income already taxed by Ohio; military pay (if applicable); Ohio 529 contributions (up to $4,000 per beneficiary per year)  _(R-OH-2)_
- **R-OH-3. Business vs. nonbusiness income classification.** — Schedule C net profit is business income. Wage income (W-2) is nonbusiness income. Capital gains may be business or nonbusiness depending on the nature of the asset. Interest and dividends are generally nonbusiness unless generated from business activity.  _(R-OH-3)_
- **R-OH-4. BID is automatic if business income is identified.** — The first $250,000 of business income is excluded. No election is required — but the taxpayer must complete Ohio Schedule IT BUS to claim the deduction.  _(R-OH-4)_
- **R-OH-5. Personal exemption is based on Ohio AGI, not federal AGI.** — Use Ohio AGI to determine the per-person exemption amount ($2,400 / $2,150 / $1,900).  _(R-OH-5)_
- **R-OH-6. Ohio does not conform to OBBBA for §179 purposes.** — Ohio generally conforms to the IRC as of a specific date. Verify Ohio's conformity date and determine whether OBBBA §179 and §168(k) changes flow through or require adjustment on the Ohio Schedule of Adjustments.  _(R-OH-6)_
- **R-OH-7. Social Security is fully exempt.** — If federal AGI includes Social Security benefits, subtract the full amount included in federal AGI on the Ohio Schedule of Adjustments.  _(R-OH-7)_

## Section 6: Tier 2 rules — requires judgment

- **J-OH-1. Business vs. nonbusiness income classification for mixed-use assets.** — When a sole proprietor sells a vehicle or equipment used partly for business and partly for personal use, judgment is needed to allocate the gain between business income (eligible for BID) and nonbusiness income.  _(J-OH-1)_
- **J-OH-2. Municipal credit on state return.** — Ohio allows a credit (limited) for municipal income taxes paid. The Joint Filing Credit (for MFJ) is a separate credit on the state return. Interaction between these credits requires careful calculation.  _(J-OH-2)_
- **J-OH-3. Residency determination.** — Ohio defines "resident" as an individual domiciled in Ohio. Part-year residents and nonresidents use different schedules. Flag any taxpayer who moved to or from Ohio during the year.  _(J-OH-3)_
- **J-OH-4. Ohio IRC conformity date.** — Ohio's conformity to the Internal Revenue Code must be verified against the most recent budget bill. If OBBBA provisions are not conformed to, any OBBBA-specific federal deductions or exclusions may need adjustment.  _(J-OH-4)_

## Section 7: Supplier pattern library

**Supplier pattern library**

| Pattern | Description |
| --- | --- |
| High BID utilization | Sole proprietor with >$250K Schedule C profit. Business income above BID taxed at 3% flat — often lower than nonbusiness graduated rates. |
| W-2 + Schedule C combo | Taxpayer with both W-2 wages (nonbusiness) and Schedule C profit (business). Allocate correctly between the two income categories. |
| Social Security recipient | Subtract Social Security from Ohio AGI — Ohio fully exempts. |
| Out-of-state municipal bonds | Add back interest from non-Ohio state/local government bonds on the Schedule of Adjustments. |
| Reciprocal state worker | Ohio has reciprocity agreements with IN, KY, MI, PA, WV. If taxpayer works in one of these states, only Ohio taxes the income. |

## Section 8: Form mapping

**Ohio IT 1040 form mapping**

| Ohio IT 1040 line | Description | Source |
| --- | --- | --- |
| Line 1 | Federal AGI | Federal Form 1040, Line 11 |
| Schedule of Adjustments | Additions / subtractions | Various (see R-OH-2) |
| Line 3 | Ohio AGI | Line 1 + additions − subtractions |
| Schedule IT BUS | Business income / BID | Schedule C net profit, BID computation |
| Line 5 | Ohio taxable nonbusiness income | Ohio AGI − business income − exemptions |
| Line 8a | Nonbusiness income tax | Tax table or rate schedule |
| Line 8b | Business income tax (3% flat on excess over BID) | Schedule IT BUS |
| Line 8c | Total Ohio income tax before credits | Line 8a + Line 8b |
| Line 14 | Ohio income tax after credits | After applying all credits |
| Line 23 | Amount owed / refund | After payments and withholding |

## Section 9: Refusal catalogue

- **REFUSE-OH-1** — REFUSE to prepare an Ohio return for a part-year resident or nonresident without the appropriate nonresident credit schedule. This skill covers full-year residents only.  _(REFUSE-OH-1)_
- **REFUSE-OH-2** — REFUSE to compute Ohio municipal income taxes. These are separate filings administered by individual cities and are outside the scope of this skill.  _(REFUSE-OH-2)_
- **REFUSE-OH-3** — REFUSE to compute school district income tax. Ohio has over 200 school districts with their own income taxes (traditional or earned income based). These require a separate SD 100 filing.  _(REFUSE-OH-3)_
- **REFUSE-OH-4** — REFUSE to classify ambiguous income as business or nonbusiness without reviewer guidance. Misclassification can result in significant tax differences.  _(REFUSE-OH-4)_
- **REFUSE-OH-5** — REFUSE to apply 2026 flat tax rates to a 2025 return. Tax year 2025 uses the three-bracket graduated system.  _(REFUSE-OH-5)_

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
