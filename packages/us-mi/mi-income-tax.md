---
name: mi-income-tax
description: Use this skill whenever asked about Michigan individual income tax for self-employed persons, sole proprietors, or single-member LLCs. Trigger on phrases like "Michigan income tax", "MI income tax", "Form MI-1040", "Michigan Treasury", "MCL 206.51".
version: "0.1"
jurisdiction: US-MI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MI Income Tax

## Michigan Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers Michigan Form MI-1040 for full-year Michigan residents who are sole proprietors or single-member LLC owners. Michigan imposes a flat 4.25% income tax. This skill also flags city-level income taxes that may apply in 24 Michigan cities.
>
> **Quality tier.** Q3 — AI-drafted, not independently verified. All rates and thresholds were researched on 2026-05-22 from official Michigan Department of Treasury publications. A qualified professional must review before filing.

## Section 1: Metadata

**Metadata table**

| Field | Value |
| --- | --- |
| Jurisdiction | Michigan (US-MI) |
| Tax type | Individual income tax |
| Primary form | Form MI-1040 |
| Tax year | 2026 (filed in 2027) |
| Authority | Michigan Department of Treasury |
| Statute | MCL 206.1 et seq. (Income Tax Act of 1967) |
| Version | 0.1 |
| Last updated | 2026-05-22 |
| Validation | AI-drafted — Q3 |

### Sources consulted

**Sources consulted table**

| # | Source | URL |
| --- | --- | --- |
| 1 | Michigan Treasury — 4.25% Rate Notice for 2026 | https://www.michigan.gov/treasury/reference/taxpayer-notices/2026/04/15/425-income-tax-rate-for-individuals-and-fiduciaries-in-2026-tax-year |
| 2 | MI-1040 Book (TY 2025 instructions) | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040-Book.pdf |
| 3 | MCL 206.51 — Tax rate | https://legislature.mi.gov/Laws/MCL?objectName=mcl-206-51 |
| 4 | Michigan city income tax list | https://www.michigan.gov/taxes/iit/city |

## Section 2: Quick reference — rates and thresholds

### Tax rate — 2026 tax year

**Michigan flat income tax rate table**  _(MCL 206.51)_

| Item | Value | Source |
| --- | --- | --- |
| Michigan flat income tax rate | 4.25% | MCL 206.51 |

- **Flat rate applicability** — Michigan uses a flat rate — the same 4.25% applies to all taxable income regardless of filing status or income level.  _(MCL 206.51)_

### Exemptions — 2026

**Exemptions table**  _(MCL 206.30)_

| Item | Amount | Source |
| --- | --- | --- |
| Personal exemption | $5,800 per person | MCL 206.30 |
| Stillbirth exemption | $5,800 | MCL 206.30 |
| Special exemption (disabled/deaf/blind) | $3,400 | MCL 206.30 |
| Disabled veteran exemption | $500 | MCL 206.30 |

- **No state standard deduction** — Michigan does NOT have a state-level standard deduction for most filers. Taxpayers under age 67 deduct only personal exemptions from AGI.  _(MCL 206.30)_

### Retirement / senior deductions (age 67+)

**Senior deduction table**

| Filing status | Deduction |
| --- | --- |
| Single (age 67+) | $20,000 against all income |
| MFJ (both 67+) | $40,000 against all income |

### Key thresholds

**Key thresholds table**

| Item | Value |
| --- | --- |
| Filing deadline | April 15, 2027 (for TY 2026) |
| Extension | Automatic 6-month with federal extension |
| Estimated tax threshold | $500 expected liability after credits and withholding |
| Estimated payment due dates | April 15, June 15, September 15, January 15 |

### City income taxes (overview)

24 Michigan cities impose a separate city income tax. The most notable:

**City income tax rates table**

| City | Resident rate | Non-resident / worker rate |
| --- | --- | --- |
| Detroit | 2.4% | 1.2% |
| Grand Rapids | 1.5% | 0.75% |
| All other cities | 1.0% | 0.5% |

- **City tax filing separate from MI-1040** — City income tax is filed on a separate return directly with the city. It is NOT computed on Form MI-1040.

## Section 3: How this skill works with the federal return

- **Starting point** — Michigan taxable income begins with federal adjusted gross income (AGI) from federal Form 1040, Line 11.
- **Step 1 - Additions** — Additions — Add back items Michigan does not exclude (e.g., deductions for income taxed by a Michigan city, interest on non-Michigan state/municipal bonds).
- **Step 2 - Subtractions** — Subtractions — Subtract items Michigan excludes (e.g., U.S. government bond interest, Social Security benefits, Michigan state/local income tax refunds included in federal AGI, retirement/pension income for qualifying seniors).
- **Step 3 - Michigan AGI** — Michigan AGI = Federal AGI + additions − subtractions.
- **Step 4 - Personal exemptions** — Personal exemptions — $5,800 per qualifying exemption (2026).
- **Step 5 - Michigan taxable income** — Michigan taxable income = Michigan AGI − exemptions.
- **Step 6 - Tax** — Tax = Michigan taxable income × 4.25%.
- **Step 7 - Credits** — Credits — Apply applicable credits.
- **No standard/itemized deduction under 67** — Michigan does NOT have a state standard deduction or itemized deductions for taxpayers under age 67.

## Section 4: Self-employed specific rules

- **1. Self-employment income flow-through** — Self-employment income flows through federal Schedule C → federal AGI → Michigan AGI. No separate Michigan schedule for self-employment income.
- **2. Federal SE tax deduction** — The 50% self-employment tax deduction is reflected in federal AGI. Michigan starts from federal AGI, so this carries through.
- **3. Estimated taxes** — Self-employed taxpayers must make quarterly estimated payments (Form MI-1040ES) if expected liability exceeds $500. Penalty applies for underpayment.
- **4. Business equipment depreciation** — Michigan generally conforms to federal depreciation, including IRC § 179. Michigan also conforms to bonus depreciation under IRC § 168(k).
- **5. Home office deduction** — Flows through federal Schedule C; no separate Michigan adjustment.
- **6. Health insurance deduction** — The self-employed health insurance deduction is included in federal AGI. No Michigan add-back required.
- **7. City income tax** — If the taxpayer operates a business in a city with a city income tax (e.g., Detroit), a separate city income tax return may be required.

## Section 5: Tier 1 rules — deterministic

**Tier 1 rules table**

| Rule ID | Rule | Source |
| --- | --- | --- |
| MI-T1-01 | Start with federal AGI (Form 1040, Line 11) | MCL 206.30 |
| MI-T1-02 | Add back interest on out-of-state municipal bonds | MCL 206.30(1)(d) |
| MI-T1-03 | Add back city income tax deduction claimed on federal Schedule A | MCL 206.30 |
| MI-T1-04 | Subtract U.S. government bond interest | MCL 206.30(1)(f) |
| MI-T1-05 | Subtract Social Security, military pay, railroad retirement (fully exempt) | MCL 206.30(1)(f) |
| MI-T1-06 | Personal exemption: $5,800 per person (2026) | MCL 206.30 |
| MI-T1-07 | Flat rate: taxable income × 4.25% | MCL 206.51 |
| MI-T1-08 | Michigan EITC: 30% of federal Earned Income Credit (refundable) | MCL 206.272 |
| MI-T1-09 | Homestead Property Tax Credit: available to homeowners/renters with household income ≤ certain thresholds (filed on MI-1040CR) | MCL 206.520 |
| MI-T1-10 | Credit for taxes paid to other states: non-refundable, limited to Michigan tax on income also taxed by other state | MCL 206.255 |

## Section 6: Tier 2 rules — requires judgment

**Tier 2 rules table**

| Rule ID | Rule | Guidance |
| --- | --- | --- |
| MI-T2-01 | **Residency determination** — Michigan uses a domicile test. A person domiciled in Michigan is a resident for the full year, even if temporarily absent. | If taxpayer has homes in multiple states, flag for professional review. |
| MI-T2-02 | **Reciprocal agreements** — Michigan has reciprocity with IL, IN, KY, MN, OH, WI. Wages earned in those states by a MI resident are taxed only by MI. | Verify the employer withheld for MI (not the work state) and file exemption certificate. |
| MI-T2-03 | **City income tax nexus** — If a self-employed person has customers or performs work in a city with city income tax, apportionment rules may apply. | Flag for professional review if the taxpayer works in Detroit, Grand Rapids, or other taxing cities. |
| MI-T2-04 | **Retirement/pension income subtraction** — Complex rules for taxpayers born before 1946, between 1946–1952, and after 1952. | Apply the correct tier based on birth year. |
| MI-T2-05 | **Home heating credit** — Income-based credit available to low-income households. | Requires separate computation on MI-1040CR-7. |

## Section 7: Supplier pattern library

**Supplier pattern library table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| W-2 wages from Michigan employer | Michigan withholding applies; include on MI-1040 | Most common |
| W-2 wages from reciprocal state (IL, IN, KY, MN, OH, WI) | Should have MI withholding; if not, claim credit | File exemption with employer |
| Schedule C net profit (sole prop) | Flows through federal AGI → Michigan AGI | No separate MI schedule |
| Rental income (Schedule E) | Included in federal AGI → Michigan AGI | Michigan-source if property in MI |
| Interest on U.S. government bonds | Subtract from Michigan AGI | MCL 206.30 |
| Interest on non-Michigan muni bonds | Add back to Michigan AGI | Taxable for MI purposes |
| Social Security benefits | Subtract from Michigan AGI (fully exempt) | MCL 206.30 |
| Capital gains from asset sale | Included in federal AGI → Michigan AGI | No special MI rate |
| 1099-NEC freelance income | Flows through Schedule C → federal AGI | Estimated payments likely needed |

## Section 8: Form mapping

**Form mapping table**

| Michigan form / schedule | What it covers | Federal counterpart |
| --- | --- | --- |
| Form MI-1040 | Michigan Individual Income Tax Return | Form 1040 |
| Schedule 1 (MI-1040) | Additions and Subtractions | Schedule 1 (Form 1040) |
| Schedule NR | Non-resident / Part-year Resident | N/A |
| Schedule W | Michigan Withholding | W-2/1099 withholding summary |
| MI-1040CR | Homestead Property Tax Credit | N/A |
| MI-1040CR-7 | Home Heating Credit | N/A |
| MI-1040ES | Estimated Tax Payment Voucher | Form 1040-ES |
| City returns (various) | City income tax | N/A |

## Section 9: Refusal catalogue

**Refusal catalogue table**

| ID | Situation | Action |
| --- | --- | --- |
| MI-R-01 | Part-year or non-resident return (Schedule NR) | Refuse — out of scope |
| MI-R-02 | Corporate income tax (CIT) | Refuse — out of scope |
| MI-R-03 | City income tax return (Detroit, Grand Rapids, etc.) | Refuse — separate filing; out of scope |
| MI-R-04 | Multi-state income apportionment | Refuse — flag for professional review |
| MI-R-05 | Amended returns | Refuse — out of scope |
| MI-R-06 | Tax year other than current | Refuse — rate may differ |
| MI-R-07 | Michigan Business Tax (MBT) or Corporate Income Tax | Refuse — different tax type |

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
