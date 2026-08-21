---
name: nj-income-tax
description: Use this skill whenever asked about New Jersey individual income tax for self-employed / sole proprietors. Trigger on phrases like "New Jersey income tax", "NJ income tax", "Form NJ-1040", "NJ Division of Taxation", "NJ self-employment tax".
version: "0.1"
jurisdiction: US-NJ
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NJ Income Tax

## New Jersey Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers New Jersey Form NJ-1040 (Resident Income Tax Return) for full-year NJ residents who are sole proprietors or single-member LLC owners. Tax year 2025 (returns filed in 2026). New Jersey uses a graduated rate structure with rates from 1.4% to 10.75%.
>
> **Quality tier.** Q3 — AI-drafted, not independently verified. All outputs must be reviewed by a qualified tax professional before filing.

## Section 1: Metadata

**Metadata table**

| Field | Value |
| --- | --- |
| Tax type | Individual income tax |
| Jurisdiction | New Jersey (US-NJ) |
| Tax year | 2025 (filed 2026) |
| Primary form | Form NJ-1040 (residents) |
| Nonresident form | Form NJ-1040NR |
| Tax structure | Graduated (7 brackets single, 8 brackets MFJ) |
| Rate range | 1.4% – 10.75% |
| Filing deadline | April 15, 2026 |
| Extension deadline | October 15, 2026 (with NJ-630 or federal extension) |
| Tax authority | New Jersey Division of Taxation |
| Website | https://www.nj.gov/treasury/taxation |
| Statute | N.J.S.A. 54A:1-1 et seq. (NJ Gross Income Tax Act) |

**Sources:**
- NJ Division of Taxation, NJ Income Tax Rates: https://www.nj.gov/treasury/taxation/taxtables.shtml
- NJ-1040 Instructions (2025): https://www.nj.gov/treasury/taxation/prntgit.shtml
- N.J.S.A. 54A:2-1 (imposition of tax and rates)

## Section 2: Quick reference — rates and thresholds

### Tax brackets — Single / Married filing separately (TY 2025)

**Tax brackets — Single / Married filing separately (TY 2025)**

| Taxable income over | But not over | Rate | Tax on lower amount |
| --- | --- | --- | --- |
| $0 | $20,000 | 1.4% | $0 |
| $20,000 | $35,000 | 1.75% | $280 |
| $35,000 | $40,000 | 3.5% | $542.50 |
| $40,000 | $75,000 | 5.525% | $717.50 |
| $75,000 | $500,000 | 6.37% | $2,651.25 |
| $500,000 | $1,000,000 | 8.97% | $29,726.25 |
| $1,000,000 | — | 10.75% | $74,576.25 |

### Tax brackets — Married filing jointly / Head of household / Qualifying surviving spouse (TY 2025)

**Tax brackets — Married filing jointly / Head of household / Qualifying surviving spouse (TY 2025)**

| Taxable income over | But not over | Rate | Tax on lower amount |
| --- | --- | --- | --- |
| $0 | $20,000 | 1.4% | $0 |
| $20,000 | $50,000 | 1.75% | $280 |
| $50,000 | $70,000 | 2.45% | $805 |
| $70,000 | $80,000 | 3.5% | $1,295 |
| $80,000 | $150,000 | 5.525% | $1,645 |
| $150,000 | $500,000 | 6.37% | $5,512.50 |
| $500,000 | $1,000,000 | 8.97% | $27,807.50 |
| $1,000,000 | — | 10.75% | $72,657.50 |

### $100,000 rule

- **$100,000 rule** — If NJ taxable income is $100,000 or more, you must use the NJ Tax Rate Schedules (above) instead of the tax tables.  _(NJ-1040 Instructions)_

### Personal exemptions (TY 2025)

**Personal exemptions (TY 2025)**

| Exemption | Amount |
| --- | --- |
| Taxpayer | $1,000 |
| Spouse (MFJ) | $1,000 |
| Each dependent | $1,500 |
| Age 65+ (additional) | $1,000 |
| Blind/disabled (additional) | $1,000 |
| Veteran | $6,000 |

New Jersey does **not** have a standard deduction. It uses a personal exemption system instead.

### Local income tax

- **Local income tax** — New Jersey does not permit local income taxes.  _(unsure)_

## Section 3: How this skill works with the federal return

**Critical difference:** New Jersey does **NOT** start from federal AGI or federal taxable income. NJ has its own gross income definition (NJ Gross Income) with its own categories of income.

NJ Gross Income includes income from 18 categories defined in N.J.S.A. 54A:5-1, including:
- Net profits from business (similar to Schedule C)
- Wages, salaries, tips
- Net gains or income from disposition of property
- Interest, dividends, and other investment income
- Rental income
- Pension/retirement income

### Computation flow

1. **Compute NJ Gross Income** from each NJ category (NOT from federal AGI)
2. **Subtract NJ exemptions** (personal exemptions, not a standard deduction)
3. **Apply NJ deductions** (limited list — medical expenses over 2% of NJ gross income, Archer MSA contributions, health enterprise zone deductions, qualified conservation contributions)
4. **Result = NJ taxable income**
5. **Apply the graduated rate schedule** → NJ tax
6. **Apply credits** → final tax due or refund

### Key NJ vs. federal differences

**Key NJ vs. federal differences**

| Item | Federal treatment | NJ treatment |
| --- | --- | --- |
| Starting point | AGI | NJ Gross Income (own categories) |
| Standard deduction | Yes ($15,000 single 2025) | No — NJ has no standard deduction |
| 401(k)/403(b) contributions | Pre-tax (excluded from wages) | **Taxable** — NJ does not exclude employee retirement contributions |
| IRA deductions | Deductible (traditional IRA) | **Not deductible** for NJ purposes |
| Self-employed health insurance | Deductible from AGI | **Not deductible** for NJ purposes |
| Capital gains | Preferential rates (0/15/20%) | Taxed as ordinary income at NJ rates |
| Social Security | Up to 85% taxable | **Fully exempt** |
| Property taxes | SALT cap ($10,000 federal) | Property tax deduction up to $15,000 (or credit for income under $150,000) |
| Alimony (pre-2019 agreements) | Deductible/includible | Deductible/includible (NJ conforms) |
| Net operating losses | Deductible | NJ does not allow NOL deductions for individuals |

## Section 4: Self-employed specific rules

### Self-employment income

- **Self-employment income treatment** — NJ taxes net profits from business as a separate category of NJ Gross Income. The computation is similar to federal Schedule C but with NJ-specific rules. Key differences: - **Depreciation:** NJ generally conforms to federal depreciation, but verify conformity with recent federal changes (OBBBA provisions). - **Self-employed health insurance:** NOT deductible for NJ purposes (it is deductible federally). - **Self-employed retirement contributions:** NOT deductible for NJ purposes (already excluded at the contribution level for Keogh/SEP plans — verify). - **Home office deduction:** NJ generally conforms to federal rules.  _(unsure)_

### Estimated tax

- **Estimated tax payment requirement** — $400 or more USD (expected NJ income tax liability after subtracting withholding)  _(unsure)_

**Estimated tax installment due dates**

| Installment | Due date |
| --- | --- |
| 1st quarter | April 15 |
| 2nd quarter | June 15 |
| 3rd quarter | September 15 |
| 4th quarter | January 15 (following year) |

Form NJ-1040-ES is used for estimated tax payments.

### NJ self-employment tax interaction

- **NJ self-employment tax interaction** — NJ does not impose its own self-employment tax (Social Security/Medicare). Those are federal only. However, NJ does not allow a deduction for the federal self-employment tax deduction (the deductible half of SE tax). Since NJ starts from its own gross income definition rather than federal AGI, this difference is structural.  _(unsure)_

### Property tax deduction / credit

- **Property tax deduction / credit** — Self-employed NJ residents who own their home can deduct property taxes up to $15,000 on their NJ return. This is separate from the federal SALT cap. Alternatively, taxpayers with NJ gross income of $150,000 or less may claim a property tax credit.  _(unsure)_

## Section 5: Tier 1 rules — deterministic

**Tier 1 rules — deterministic**

| Rule ID | Rule | Source |
| --- | --- | --- |
| NJ-T1-01 | NJ taxable income = NJ Gross Income − exemptions − NJ deductions | N.J.S.A. 54A:2-1 |
| NJ-T1-02 | Tax computed using graduated schedule: 1.4% – 10.75% (TY 2025) | N.J.S.A. 54A:2-1 |
| NJ-T1-03 | NJ starts from own gross income categories, NOT federal AGI | N.J.S.A. 54A:5-1 |
| NJ-T1-04 | No standard deduction; personal exemptions only ($1,000 taxpayer, $1,500 dependent) | N.J.S.A. 54A:3-1 |
| NJ-T1-05 | 401(k)/403(b) contributions are taxable for NJ purposes | N.J.S.A. 54A:6-21 |
| NJ-T1-06 | Social Security benefits are fully exempt | N.J.S.A. 54A:6-2 |
| NJ-T1-07 | Capital gains taxed at ordinary income rates (no preferential rate) | N.J.S.A. 54A:5-1(c) |
| NJ-T1-08 | Estimated tax required if expected liability ≥ $400 | N.J.S.A. 54A:9-6 |
| NJ-T1-09 | If taxable income ≥ $100,000, must use Tax Rate Schedules | NJ-1040 Instructions |
| NJ-T1-10 | Property tax deduction capped at $15,000 | N.J.S.A. 54A:3A-1 |

## Section 6: Tier 2 rules — requires judgment

**Tier 2 rules — requires judgment**

| Rule ID | Situation | Guidance |
| --- | --- | --- |
| NJ-T2-01 | **Multi-state income:** Taxpayer earns income in another state | NJ taxes worldwide income of residents. Credit for taxes paid to other states available. Complex for NY/NJ commuters — verify convenience-of-the-employer issues. |
| NJ-T2-02 | **NY/NJ commuter tax interaction** | NJ residents working in NY pay NY tax on NY-source income and get a credit on their NJ return. However, NJ may challenge the credit if the NY tax was based on the convenience-of-the-employer rule. |
| NJ-T2-03 | **Business income categorization** | NJ's 18 income categories can create allocation issues for self-employed taxpayers with mixed income types. Review whether income should be "net profits from business" or another category. |
| NJ-T2-04 | **PTET/BAIT election** | NJ's Pass-Through Business Alternative Income Tax allows certain pass-throughs to pay entity-level tax. Not applicable to sole proprietors but relevant for multi-member LLCs. |
| NJ-T2-05 | **Federal conformity for depreciation** | Verify NJ's current position on federal bonus depreciation and OBBBA changes. NJ's non-conformity with certain federal provisions may require separate depreciation schedules. |

## Section 7: Supplier pattern library

**Supplier pattern library**

| Input needed | Where to find it |
| --- | --- |
| NJ Gross Income | Computed from each NJ income category (NOT from federal return directly) |
| Net profits from business | Similar to federal Schedule C, with NJ modifications |
| Personal exemptions | Based on filing status, dependents, age, veteran status |
| NJ deductions | Medical (over 2% of NJ GI), property taxes (up to $15,000) |
| Tax credits | Property tax credit, NJ EIC, excess UI/SDI contributions |
| Estimated tax payments | NJ-1040-ES records |
| NJ withholding | W-2 Box 17 / 1099 NJ withholding amounts |

## Section 8: Form mapping

**Form mapping**

| Form NJ-1040 Line | Description | Source |
| --- | --- | --- |
| Lines 16-26 | NJ Gross Income by category | NJ income category computations |
| Line 27 | Total NJ Gross Income | Sum of Lines 16-26 |
| Line 29 | Total exemptions | Personal + dependent + additional |
| Line 36 | NJ deductions (medical, property tax, etc.) | Computed |
| Line 38 | NJ taxable income | Line 27 − Line 29 − Line 36 |
| Line 39 | NJ tax | From tax table or Rate Schedule |
| Line 44 | Total credits | Computed |
| Line 49 | NJ income tax withheld | W-2s / 1099s |
| Line 50 | Estimated tax payments | NJ-1040-ES payments |
| Line 55 | Amount owed or refund | Computed |

## Section 9: Refusal catalogue

**Refusal catalogue**

| Refusal ID | Trigger | Response |
| --- | --- | --- |
| R-NJ-01 | Part-year or nonresident | "NJ nonresident returns require Form NJ-1040NR. This is outside the scope of this skill." |
| R-NJ-02 | Corporate or CBT return | "This skill covers individual gross income tax only (Form NJ-1040). Corporation Business Tax is not covered." |
| R-NJ-03 | Estate or trust return | "NJ fiduciary returns (Form NJ-1041) are not covered by this skill." |
| R-NJ-04 | Amended return | "NJ amended returns (Form NJ-1040X) are not covered." |
| R-NJ-05 | PTET/BAIT computation | "The Pass-Through Business Alternative Income Tax (BAIT) election and computation are not covered by this skill." |
| R-NJ-06 | Inheritance tax | "NJ inheritance tax (N.J.S.A. 54:34-1) is not covered by this income tax skill." |

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
