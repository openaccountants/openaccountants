---
name: me-income-tax
description: Use this skill whenever asked about Maine individual income tax for self-employed persons, sole proprietors, or single-member LLCs. Trigger on phrases like "Maine income tax", "ME income tax", "Form 1040ME", "Maine Revenue Services", "36 M.R.S. § 5111".
version: "0.1"
jurisdiction: US-ME
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ME Income Tax

## Maine Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers Maine Form 1040ME for full-year Maine residents who are sole proprietors or single-member LLC owners. It addresses the graduated rate structure (5.8%–7.15%, plus a 2% surcharge on high earners), the Maine standard deduction, personal exemption, and key credits.
>
> **Quality tier.** Q3 — AI-drafted, not independently verified. All rates and thresholds were researched on 2026-05-22 from official Maine Revenue Services publications. A qualified professional must review before filing.

## Section 1: Metadata

**Metadata**

| Field | Value |
| --- | --- |
| Jurisdiction | Maine (US-ME) |
| Tax type | Individual income tax |
| Primary form | Form 1040ME |
| Tax year | 2026 (filed in 2027) |
| Authority | Maine Revenue Services (MRS) |
| Statute | 36 M.R.S. § 5111 et seq. |
| Version | 0.1 |
| Last updated | 2026-05-22 |
| Validation | AI-drafted — Q3 |

### Sources consulted

**Sources consulted**

| # | Source | URL |
| --- | --- | --- |
| 1 | Maine Revenue Services — Individual Income Tax (1040ME) | https://www.maine.gov/revenue/taxes/income-estate-tax/individual-income-tax-1040me |
| 2 | 2026 Individual Income Tax Rate Schedules (PDF) | https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/ind_tax_rate_sched_2026.pdf |
| 3 | Thomson Reuters — Maine 2026 Rate Announcement | https://tax.thomsonreuters.com/news/maine-announces-individual-income-tax-rate-schedules-personal-exemption-standard-deduction-for-2026/ |
| 4 | 36 M.R.S. § 5111 (rate statute) | https://legislature.maine.gov/statutes/36/title36sec5111.html |

## Section 2: Quick reference — rates and thresholds

### Tax rates — 2026 tax year (Single / MFS)

**Tax rates — 2026 tax year (Single / MFS)**

| Taxable income | Rate |
| --- | --- |
| $0 – $27,400 | 5.80% |
| $27,400 – $64,850 | 6.75% |
| $64,850 – $1,000,000 | 7.15% |
| Over $1,000,000 | 9.15% (7.15% + 2% surcharge) |

### Tax rates — 2026 tax year (MFJ / Qualifying Surviving Spouse)

**Tax rates — 2026 tax year (MFJ / Qualifying Surviving Spouse)**

| Taxable income | Rate |
| --- | --- |
| $0 – $54,850 | 5.80% |
| $54,850 – $129,750 | 6.75% |
| $129,750 – $1,500,000 | 7.15% |
| Over $1,500,000 | 9.15% (7.15% + 2% surcharge) |

### Tax rates — 2026 tax year (Head of Household)

**Tax rates — 2026 tax year (Head of Household)**

| Taxable income | Rate |
| --- | --- |
| $0 – $41,100 | 5.80% |
| $41,100 – $97,300 | 6.75% |
| $97,300 – $1,500,000 | 7.15% |
| Over $1,500,000 | 9.15% (7.15% + 2% surcharge) |

### Standard deduction — 2026

**Standard deduction — 2026**

| Filing status | Amount |
| --- | --- |
| Single / MFS | $15,300 |
| MFJ / Surviving Spouse | $30,600 |
| Head of Household | $22,950 |

- **Standard deduction phase-out** — The standard deduction phases out for single filers with Maine income over $102,250 and MFJ filers with income over $204,550.

### Personal exemption — 2026

- **Personal exemption per taxpayer/spouse** — $5,300 USD

### Key thresholds

**Key thresholds**

| Item | Value | Source |
| --- | --- | --- |
| Filing deadline | April 15, 2027 (for TY 2026) | 36 M.R.S. § 5227 |
| Extension | Automatic 6-month with federal extension | 36 M.R.S. § 5227 |
| Estimated tax threshold | $1,000 expected liability after credits and withholding | 36 M.R.S. § 5228 |

## Section 3: How this skill works with the federal return

- **Maine taxable income starting point** — Maine taxable income begins with **federal adjusted gross income (AGI)** from federal Form 1040, Line 11. 1. **Additions** — Add back items Maine does not exclude (e.g., interest on non-Maine state/municipal bonds). 2. **Subtractions** — Subtract items Maine excludes (e.g., Social Security benefits included in federal AGI, U.S. government pension income, Maine public pension income). 3. **Maine adjusted gross income** — Federal AGI + additions − subtractions. 4. **Standard or itemized deduction** — Maine conforms to the federal standard deduction amounts (with phase-out at higher incomes) or allows Maine itemized deductions. 5. **Personal exemption** — $5,300 per qualifying person (2026). 6. **Maine taxable income** — Maine AGI − deduction − exemptions. 7. **Tax** — Apply graduated rates to Maine taxable income. 8. **Credits** — Apply applicable credits (child care, earned income, property tax fairness, etc.).

## Section 4: Self-employed specific rules

- **Self-employed specific rules** — 1. **Self-employment income** flows through federal Schedule C → federal AGI → Maine AGI. No separate Maine schedule for self-employment income is required. 2. **Federal SE tax deduction** — The 50% self-employment tax deduction is already reflected in federal AGI. Maine begins from federal AGI, so this deduction carries through automatically. 3. **Estimated taxes** — Self-employed taxpayers must make quarterly estimated payments (Form 1040ES-ME) if they expect to owe $1,000 or more after withholding and credits. Due dates: April 15, June 15, September 15, January 15. 4. **Business equipment depreciation** — Maine generally conforms to federal depreciation rules, including IRC § 179 expensing. Maine does NOT conform to 100% federal bonus depreciation under IRC § 168(k); check the current conformity date for partial adjustments. 5. **Home office deduction** — Flows through federal Schedule C; no separate Maine adjustment needed. 6. **Health insurance deduction** — The self-employed health insurance deduction is included in federal AGI. No Maine add-back required.

## Section 5: Tier 1 rules — deterministic

**Tier 1 rules — deterministic**

| Rule ID | Rule | Source |
| --- | --- | --- |
| ME-T1-01 | Start with federal AGI (Form 1040, Line 11) | 36 M.R.S. § 5121 |
| ME-T1-02 | Add back interest on out-of-state municipal bonds | 36 M.R.S. § 5122 |
| ME-T1-03 | Subtract Social Security benefits included in federal AGI | 36 M.R.S. § 5122(2)(M) |
| ME-T1-04 | Subtract pension income from Maine public retirement system (up to $25,000, reduced by Social Security) | 36 M.R.S. § 5122(2)(N) |
| ME-T1-05 | Apply standard deduction: $15,300 (single), $30,600 (MFJ), $22,950 (HoH) for 2026 | 36 M.R.S. § 5124-C |
| ME-T1-06 | Phase out standard deduction for AGI over $102,250 (single) / $204,550 (MFJ) | 36 M.R.S. § 5124-C |
| ME-T1-07 | Personal exemption: $5,300 per person (2026) | 36 M.R.S. § 5126-A |
| ME-T1-08 | Apply graduated rates: 5.80%, 6.75%, 7.15% | 36 M.R.S. § 5111 |
| ME-T1-09 | Apply 2% surcharge on taxable income over $1M (single) / $1.5M (MFJ/HoH) / $750K (MFS) | 36 M.R.S. § 5111 (2026+) |
| ME-T1-10 | Property Tax Fairness Credit: refundable credit for property taxes or rent constituting an excessive share of income (max $1,500 or $2,000 if 65+) | 36 M.R.S. § 5219-KK |
| ME-T1-11 | Maine Earned Income Credit: 12% of federal EIC (refundable) | 36 M.R.S. § 5219-S |

## Section 6: Tier 2 rules — requires judgment

**Tier 2 rules — requires judgment**

| Rule ID | Rule | Guidance |
| --- | --- | --- |
| ME-T2-01 | **Residency determination** — Maine uses a domicile + permanent place of abode test. A taxpayer who maintains a permanent home in Maine and spends more than 183 days there is a statutory resident. | If the taxpayer has homes in multiple states, flag for professional review. |
| ME-T2-02 | **Bonus depreciation conformity** — Maine selectively conforms to IRC § 168(k). Check the current conformity date; partial add-backs may be required. | Compare Maine conformity date to federal asset placed-in-service date. |
| ME-T2-03 | **Standard deduction phase-out** — Computation requires interpolation when AGI is in the phase-out range. | If AGI is near the threshold, compute the reduced deduction carefully. |
| ME-T2-04 | **Credit for taxes paid to other states** — Non-refundable credit to prevent double taxation on income earned in another state. | Requires the other state's return to compute; flag if multi-state. |
| ME-T2-05 | **Maine itemized deductions** — If the taxpayer itemizes, Maine generally conforms to federal itemized deductions with some modifications (e.g., Maine caps the medical expense threshold). | Compare federal Schedule A to Maine allowable amounts. |

## Section 7: Supplier pattern library

**Supplier pattern library**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| W-2 wages from Maine employer | Maine withholding applies; include on 1040ME | Most common |
| Schedule C net profit (sole prop) | Flows through federal AGI → Maine AGI | No separate ME schedule |
| Rental income (Schedule E) | Included in federal AGI → Maine AGI | Maine-source if property in ME |
| Interest on U.S. government bonds | Subtract from Maine AGI | 36 M.R.S. § 5122 |
| Interest on non-Maine muni bonds | Add back to Maine AGI | Taxable for ME purposes |
| Social Security benefits | Subtract from Maine AGI (fully exempt) | 36 M.R.S. § 5122(2)(M) |
| Capital gains from asset sale | Included in federal AGI → Maine AGI | No special ME rate |
| 1099-NEC freelance income | Flows through Schedule C → federal AGI | Estimated payments likely needed |

## Section 8: Form mapping

**Form mapping**

| Maine form / schedule | What it covers | Federal counterpart |
| --- | --- | --- |
| Form 1040ME | Maine Individual Income Tax Return | Form 1040 |
| Schedule 1 (1040ME) | Maine Adjustments to Income | Schedule 1 (Form 1040) |
| Schedule 2 (1040ME) | Maine Tax Computation / Credits | N/A |
| Schedule A (1040ME) | Maine Itemized Deductions | Schedule A (Form 1040) |
| Form 1040ES-ME | Estimated Tax Payment Voucher | Form 1040-ES |
| Schedule NR | Non-resident / Part-year Resident | N/A |
| Schedule CP | Charitable Contributions, Property Tax Fairness Credit | N/A |

## Section 9: Refusal catalogue

**Refusal catalogue**

| ID | Situation | Action |
| --- | --- | --- |
| ME-R-01 | Part-year or non-resident return (Schedule NR) | Refuse — out of scope |
| ME-R-02 | Corporate income tax (Form 1120ME) | Refuse — out of scope |
| ME-R-03 | Estate or trust income tax | Refuse — out of scope |
| ME-R-04 | Multi-state income apportionment | Refuse — flag for professional review |
| ME-R-05 | Amended returns | Refuse — out of scope |
| ME-R-06 | Tax year other than current | Refuse — rates and thresholds may differ |
| ME-R-07 | Insurance premiums tax | Refuse — different tax type |

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
