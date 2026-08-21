---
name: pa-income-tax
description: Triggers when the taxpayer is a Pennsylvania resident sole proprietor or single-member LLC needing to file Pennsylvania Form PA-40. Covers Pennsylvania's flat 3.07% income tax on eight classes of income, the unique PA rules that disallow many federal deductions, net profits computation for self-employed, and interaction with local earned income taxes. Must be loaded alongside us-tax-workflow-base and us-federal-return-assembly.
version: "0.1"
jurisdiction: US-PA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# PA Income Tax

## Pennsylvania Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** Pennsylvania Form PA-40 for tax year 2025 for full-year Pennsylvania resident sole proprietors and disregarded single-member LLCs. Pennsylvania is an unusual state with a flat tax rate, no standard deduction, no personal exemptions, and a unique class-of-income system that differs significantly from most states.
> **Quality tier.** Q3 — AI-drafted, not independently verified. All rates and thresholds have been researched from primary sources but must be confirmed by a qualified professional before use in return preparation.

## Section 1: Metadata

**Metadata table**

| Field | Value |
| --- | --- |
| Tax year covered | 2025 (returns due April 15, 2026) |
| Primary form | PA-40 (Pennsylvania Personal Income Tax Return) |
| Tax authority | [Pennsylvania Department of Revenue](https://www.pa.gov/agencies/revenue/) |
| Tax type | Flat rate income tax (3.07%) |
| Currency date | May 2026 |

**Primary sources**

| Source | URL |
| --- | --- |
| 72 P.S. § 7302 (tax rate) | https://www.legis.state.pa.us/cfdocs/legis/li/uconsCheck.cfm?yr=1971&sessInd=0&act=2 |
| PA-40 Instructions (2025) | https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/personal-income-tax/ |
| PA Department of Revenue — Personal Income Tax | https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/personal-income-tax/ |

## Section 2: Quick reference — rates and thresholds

### Tax rate

**Pennsylvania personal income tax rate table**

| Item | Value |
| --- | --- |
| Pennsylvania personal income tax rate | **3.07% flat** (all income, all filing statuses) |

- **No graduated brackets** — Pennsylvania does NOT have graduated brackets. All taxable income is taxed at the same 3.07% rate.

### Key differences from most states

**Key differences from most states table**

| Feature | Pennsylvania rule |
| --- | --- |
| Standard deduction | **None** |
| Personal exemption | **None** |
| Itemized deductions | **Not allowed** (PA does not use federal Schedule A) |
| Starting point | **NOT federal AGI or federal taxable income** — PA computes each class of income independently |
| Net operating loss | **Not allowed** (losses in one class cannot offset income in another class) |
| Retirement income | **Fully exempt** (pensions, 401(k), IRA distributions, Social Security) |

### Eight classes of income

Pennsylvania taxes eight separate classes of income. Each class is computed independently, and losses in one class generally cannot offset income in another.

**Eight classes of income table**

| Class | Description | Relevant to sole proprietors? |
| --- | --- | --- |
| 1. Compensation | Wages, salaries, tips, fees | Yes (if also W-2 employed) |
| 2. Net profits | Business income (Schedule C equivalent) | **Yes — primary class** |
| 3. Interest | Interest income | Yes |
| 4. Dividends | Dividend income | Yes |
| 5. Rental/royalty | Net income from rents and royalties | Yes (if applicable) |
| 6. Estate/trust | Income from estates and trusts | Rare |
| 7. Gambling/lottery | Gambling and lottery winnings | If applicable |
| 8. Sale of property | Gains from sale of property | Yes (if applicable) |

### Tax forgiveness (low-income provision)

PA provides a "tax forgiveness" credit for low-income taxpayers based on eligibility income and family size.

**Tax forgiveness table**

| Eligibility income | Single (no dependents) | With 1 dependent | With 2+ dependents |
| --- | --- | --- | --- |
| 100% forgiveness | $6,500 or less | $6,500 plus $9,500 per dep | Varies |

- **Threshold increase per dependent** — The threshold increases are $9,500 per dependent for 2025. The program phases out gradually. See Schedule SP.  _(Schedule SP)_

### Income threshold for filing

**Income threshold for filing table**

| Tax year | Filing threshold |
| --- | --- |
| 2025 | $11,000 |
| 2026 | $14,000 |

## Section 3: How this skill works with the federal return

**Pennsylvania does NOT start from federal AGI or federal taxable income.** Instead, Pennsylvania computes each class of income independently using Pennsylvania-specific rules.

For a sole proprietor, the most important class is **Class 2: Net Profits**, which corresponds (roughly) to federal Schedule C but with significant differences:

**Key flow for self-employed:**

1. Compute PA net profits (PA Schedule C equivalent with PA-specific rules)
2. Compute each other class of income separately
3. Sum all eight classes → Total PA taxable income
4. Multiply by 3.07% → PA income tax before credits
5. Apply tax forgiveness (if eligible) and other credits → PA income tax liability

### Critical differences in computing net profits

**Federal deduction vs PA treatment table**

| Federal deduction | PA treatment |
| --- | --- |
| 50% of self-employment tax | **Not deductible** on PA return |
| Self-employed health insurance | **Not deductible** on PA return (but may be deductible as a business expense if structured correctly) |
| SEP/SIMPLE/solo 401(k) contributions | **Not deductible** on PA return (PA exempts the retirement income when distributed, but does not allow the contribution deduction) |
| Home office deduction | **Allowed** (if calculated per PA rules — generally follows federal) |
| Business expenses (Schedule C) | **Generally allowed** (ordinary and necessary business expenses are deductible) |
| Depreciation | **PA uses its own depreciation rules** — no bonus depreciation; PA follows federal MACRS but without §168(k) bonus |
| §179 expensing | **PA conforms to $25,000 limit** (not the federal $1,220,000+ limit). Excess must be depreciated under MACRS. |
| Net operating loss | **Not allowed** for individuals. Business losses cannot offset income from other classes, and PA does not allow NOL carryforward for individuals. |

## Section 4: Self-employed specific rules

### Net profits computation (Class 2)

- **Net profits computation basis** — The PA net profits computation is on PA Schedule C (different from federal Schedule C). The starting point is gross receipts minus cost of goods sold, minus allowable business expenses under PA rules.
- **§179 limited to $25,000** — If the taxpayer claimed more than $25,000 in §179 on the federal return, the excess must be depreciated over the asset's life on the PA return.
- **No bonus depreciation** — PA does not conform to §168(k). Any bonus depreciation claimed federally must be added back, and regular MACRS depreciation substituted.  _(§168(k))_
- **No NOL** — If net profits are negative, the loss stays within Class 2. It cannot reduce compensation (Class 1) or other income classes. PA does not allow individual NOL carryforward.

### Loss limitation (critical)

- **No offset between classes** — **Pennsylvania does not allow losses in one class of income to offset income in another class.** If a sole proprietor has a $20,000 loss in net profits (Class 2) and $80,000 in compensation (Class 1), the taxpayer pays 3.07% on $80,000. The $20,000 loss is wasted — it cannot be carried forward.

This is one of the most taxpayer-unfriendly provisions in the state tax landscape and catches many preparers off guard.

### Local earned income tax (warning)

- **Local EIT filing requirement** — Pennsylvania's over 2,500 municipalities and school districts impose local earned income taxes (EIT), typically 1%–3.9% combined. Self-employed individuals must file local EIT returns in their resident jurisdiction. The largest local taxes are: - **Philadelphia:** 3.75% wage tax (residents) / 3.44% net profits tax (verify 2025) - **Chester City:** 3.75% - **Reading:** 3.6% Local EIT is NOT covered by this skill but represents a significant additional tax burden.

### Reciprocal agreements

- **Reciprocal agreement states** — Pennsylvania has reciprocal agreements with IN, MD, NJ, OH, VA, and WV. If the taxpayer works in one of these states, only Pennsylvania taxes the compensation.

## Section 5: Tier 1 rules — deterministic

- **R-PA-1. Flat rate of 3.07%** — All taxable income from all eight classes is taxed at 3.07%. No brackets, no graduated rates.  _(R-PA-1)_
- **R-PA-2. No standard deduction and no personal exemptions** — PA does not provide any standard deduction or personal exemption. All income is taxed from dollar one (subject to tax forgiveness for low-income filers).  _(R-PA-2)_
- **R-PA-3. §179 limited to $25,000** — If federal §179 exceeds $25,000, add back the excess on the PA return and depreciate over the asset's useful life.  _(R-PA-3)_
- **R-PA-4. No bonus depreciation** — Add back all §168(k) bonus depreciation claimed on the federal return. Substitute regular MACRS depreciation on the PA return.  _(R-PA-4)_
- **R-PA-5. No loss offsets between classes** — Business losses (Class 2) cannot offset compensation (Class 1) or any other class.  _(R-PA-5)_
- **R-PA-6. Retirement income is fully exempt** — Pensions, 401(k) distributions, IRA distributions, and Social Security are all exempt from PA income tax when received. However, the contributions are NOT deductible when made (no above-the-line deduction for SEP/SIMPLE/solo 401(k) on PA return).  _(R-PA-6)_
- **R-PA-7. Tax forgiveness for low-income filers** — Apply Schedule SP to determine if the taxpayer qualifies for partial or full forgiveness of PA income tax.  _(R-PA-7)_

## Section 6: Tier 2 rules — requires judgment

- **J-PA-1. Business expense classification** — Because PA computes net profits using its own rules, judgment is needed to determine which federal Schedule C expenses are allowable under PA law. Most ordinary and necessary business expenses are allowed, but some items differ.  _(J-PA-1)_
- **J-PA-2. Self-employed health insurance deductibility** — The federal above-the-line deduction for self-employed health insurance is NOT allowed on the PA return. However, if health insurance premiums are a legitimate business expense of the sole proprietorship (e.g., paid by the business), they may be deductible on PA Schedule C. The distinction requires judgment.  _(J-PA-2)_
- **J-PA-3. Depreciation reconciliation** — When federal and PA depreciation differ (due to §179 and §168(k) differences), a depreciation schedule tracking PA basis vs. federal basis is required for all depreciable assets.  _(J-PA-3)_
- **J-PA-4. Residency determination** — PA considers a person domiciled in PA as a resident. The statutory residency test (183+ days in PA) also applies. For taxpayers who moved, part-year resident rules apply.  _(J-PA-4)_

## Section 7: Supplier pattern library

**Supplier pattern library table**

| Pattern | Description |
| --- | --- |
| Heavy equipment purchaser | Large §179 claim federally. PA limits §179 to $25,000 — must add back excess and compute PA MACRS. Creates ongoing PA/federal depreciation tracking requirement. |
| Schedule C loss with W-2 income | PA does not allow Class 2 loss to offset Class 1 compensation. Taxpayer pays 3.07% on full W-2 income despite business loss. |
| SEP contributor | SEP contribution is not deductible on PA return. PA tax on the contribution amount now, but exempt when distributed in retirement. |
| Low-income freelancer | Check Schedule SP for tax forgiveness. Full forgiveness available if eligibility income is below threshold. |
| Philadelphia resident | Additional 3.75% city wage tax on all earned income (compensation + net profits). Massive additional burden. |

## Section 8: Form mapping

**PA-40 form mapping table**

| PA-40 line | Description | Source |
| --- | --- | --- |
| Line 1a | Gross compensation | W-2 wages (if any) |
| Line 4 | Net income or loss from business (net profits) | PA Schedule C |
| Line 5 | Net gain or loss from rents/royalties | PA Schedule E equivalent |
| Line 6 | Interest income | 1099-INT |
| Line 7 | Dividend income | 1099-DIV |
| Line 8 | Income from estates/trusts | Schedule K-1 |
| Line 9 | Gambling/lottery winnings | W-2G |
| Line 10 | Gain on sale of property | PA Schedule D |
| Line 11 | Total PA taxable income | Sum of all eight classes |
| Line 12 | PA income tax (3.07%) | Line 11 × 0.0307 |
| Line 13 | Tax forgiveness credit | Schedule SP |
| Line 14 | PA income tax after forgiveness | Line 12 − Line 13 |

## Section 9: Refusal catalogue

- **REFUSE-PA-1** — REFUSE to prepare a PA return for a part-year resident or nonresident without determining the apportionment of each class of income to PA-source income.  _(REFUSE-PA-1)_
- **REFUSE-PA-2** — REFUSE to allow losses in one class of income to offset income in another class. This is a hard rule — no exceptions.  _(REFUSE-PA-2)_
- **REFUSE-PA-3** — REFUSE to apply federal §179 amounts above $25,000 on the PA return. The excess must be depreciated.  _(REFUSE-PA-3)_
- **REFUSE-PA-4** — REFUSE to apply federal bonus depreciation on the PA return. PA does not conform to §168(k).  _(REFUSE-PA-4)_
- **REFUSE-PA-5** — REFUSE to compute local earned income tax (EIT), Philadelphia wage/net profits tax, or school district taxes. These are separate filings with separate rules.  _(REFUSE-PA-5)_
- **REFUSE-PA-6** — REFUSE to deduct SEP, SIMPLE, or solo 401(k) contributions on the PA return. PA does not allow these deductions (but exempts the distributions in retirement).  _(REFUSE-PA-6)_

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
