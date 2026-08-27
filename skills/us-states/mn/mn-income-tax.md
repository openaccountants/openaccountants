---
name: mn-income-tax
description: Use this skill whenever asked about Minnesota individual income tax for self-employed persons, sole proprietors, or single-member LLCs. Trigger on phrases like "Minnesota income tax", "MN income tax", "Form M1", "Minnesota DOR", "Minn. Stat. § 290.06".
version: "0.1"
jurisdiction: US-MN
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MN Income Tax

## Minnesota Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers Minnesota Form M1 for full-year Minnesota residents who are sole proprietors or single-member LLC owners. Minnesota imposes a four-bracket graduated income tax with rates of 5.35%, 6.80%, 7.85%, and 9.85%.
>
> **Quality tier.** Q3 — AI-drafted, not independently verified. All rates and thresholds were researched on 2026-05-22 from official Minnesota Department of Revenue publications. A qualified professional must review before filing.

## Section 1: Metadata

**Section 1: Metadata**

| Field | Value |
| --- | --- |
| Jurisdiction | Minnesota (US-MN) |
| Tax type | Individual income tax |
| Primary form | Form M1 |
| Tax year | 2026 (filed in 2027) |
| Authority | Minnesota Department of Revenue |
| Statute | Minn. Stat. § 290.06 |
| Version | 0.1 |
| Last updated | 2026-05-22 |
| Validation | AI-drafted — Q3 |

### Sources consulted

**Sources consulted**

| # | Source | URL |
| --- | --- | --- |
| 1 | Minnesota DOR — Income Tax Rates and Brackets (2026) | https://www.revenue.state.mn.us/minnesota-income-tax-rates-and-brackets |
| 2 | Minnesota DOR — 2026 Bracket Announcement | https://www.revenue.state.mn.us/press-release/2025-12-16/minnesota-income-tax-brackets-standard-deduction-and-dependent-exemption |
| 3 | Minn. Stat. § 290.06 | https://www.revisor.mn.gov/statutes/cite/290.06 |
| 4 | Minnesota Form M1 Instructions | https://www.revenue.state.mn.us/form-m1-individual-income-tax |

## Section 2: Quick reference — rates and thresholds

### Tax rates — 2026 tax year (Single)

**Tax rates — 2026 tax year (Single)**

| Taxable income | Rate |
| --- | --- |
| $0 – $33,310 | 5.35% |
| $33,311 – $109,430 | 6.80% |
| $109,431 – $203,150 | 7.85% |
| $203,151+ | 9.85% |

### Tax rates — 2026 tax year (MFJ / Qualifying Surviving Spouse)

**Tax rates — 2026 tax year (MFJ / Qualifying Surviving Spouse)**

| Taxable income | Rate |
| --- | --- |
| $0 – $48,700 | 5.35% |
| $48,701 – $193,480 | 6.80% |
| $193,481 – $337,930 | 7.85% |
| $337,931+ | 9.85% |

### Tax rates — 2026 tax year (MFS)

**Tax rates — 2026 tax year (MFS)**

| Taxable income | Rate |
| --- | --- |
| $0 – $24,350 | 5.35% |
| $24,351 – $96,740 | 6.80% |
| $96,741 – $168,965 | 7.85% |
| $168,966+ | 9.85% |

### Tax rates — 2026 tax year (Head of Household)

**Tax rates — 2026 tax year (Head of Household)**

| Taxable income | Rate |
| --- | --- |
| $0 – $41,010 | 5.35% |
| $41,011 – $164,800 | 6.80% |
| $164,801 – $270,060 | 7.85% |
| $270,061+ | 9.85% |

### Standard deduction — 2026

**Standard deduction — 2026**

| Filing status | Amount |
| --- | --- |
| Single / MFS | $15,300 |
| MFJ / Surviving Spouse | $30,600 |
| Head of Household | $23,000 |

### Dependent exemption — 2026

- **Personal exemption per taxpayer/spouse** — $5,300 USD

### Key thresholds

**Key thresholds**

| Item | Value | Source |
| --- | --- | --- |
| Filing deadline | April 15, 2027 (for TY 2026) | Minn. Stat. § 289A.18 |
| Extension | Automatic 6-month with federal extension | Minn. Stat. § 289A.19 |
| Estimated tax threshold | Liability of $500 or more after withholding and credits | Minn. Stat. § 289A.25 |

## Section 3: How this skill works with the federal return

Minnesota taxable income begins with **federal taxable income** (Form 1040, Line 15 — after the federal standard or itemized deduction).

1. **Additions (Schedule M1M)** — Add back items Minnesota does not allow (e.g., state income tax deducted federally on Schedule A, certain bonus depreciation, IRC § 199A QBI deduction).
2. **Subtractions (Schedule M1M)** — Subtract items Minnesota excludes (e.g., state income tax refund included in federal income, U.S. government bond interest, Social Security subtraction for qualifying taxpayers, K-12 education credit subtraction).
3. **Minnesota taxable income** — Federal taxable income + additions − subtractions.
4. **Tax** — Apply the four graduated rates to Minnesota taxable income.
5. **Credits** — Apply applicable credits.

**Key difference from many states:** Minnesota starts from federal **taxable income** (after the standard/itemized deduction), not from federal AGI. This means the federal standard deduction and itemized deductions are already factored in. Minnesota then applies its own standard deduction or uses the federal amounts depending on the schedule.

## Section 4: Self-employed specific rules

1. **Self-employment income** flows through federal Schedule C → federal AGI → federal taxable income → Minnesota taxable income (with additions/subtractions).
2. **Federal SE tax deduction** — Already reflected in federal AGI and thus in federal taxable income. No separate Minnesota adjustment.
3. **QBI deduction add-back** — Minnesota requires an addition for the federal qualified business income deduction (IRC § 199A) if it was claimed on the federal return.
4. **Estimated taxes** — Self-employed taxpayers must make quarterly estimated payments (Form M1, Schedule M14) if expected liability exceeds $500 after withholding and credits. Due dates: April 15, June 15, September 15, January 15.
5. **Business equipment depreciation** — Minnesota requires addition of federal bonus depreciation (IRC § 168(k)) and substitution of straight-line MACRS depreciation (§ 168(a)). This creates a timing difference tracked on Schedule M1AR.
6. **Health insurance deduction** — Self-employed health insurance deduction is in federal AGI. No Minnesota add-back.
7. **No local income tax** — Minnesota does not have any local or city income taxes.

## Section 5: Tier 1 rules — deterministic

**Section 5: Tier 1 rules — deterministic**

| Rule ID | Rule | Source |
| --- | --- | --- |
| MN-T1-01 | Start with federal taxable income (Form 1040, Line 15) | Minn. Stat. § 290.01 |
| MN-T1-02 | Add back state/local tax deduction claimed on federal Schedule A | Minn. Stat. § 290.0131 |
| MN-T1-03 | Add back IRC § 199A QBI deduction | Minn. Stat. § 290.0131 |
| MN-T1-04 | Add back federal bonus depreciation (IRC § 168(k)) and replace with straight-line MACRS | Minn. Stat. § 290.0131 |
| MN-T1-05 | Subtract U.S. government bond interest | Minn. Stat. § 290.0132 |
| MN-T1-06 | Subtract state income tax refund included in federal taxable income | Minn. Stat. § 290.0132 |
| MN-T1-07 | Apply graduated rates: 5.35%, 6.80%, 7.85%, 9.85% to the 2026 brackets | Minn. Stat. § 290.06 |
| MN-T1-08 | Dependent exemption: $5,300 per qualifying dependent (2026) — reduces tax, not income | Minn. Stat. § 290.0674 |
| MN-T1-09 | Minnesota Working Family Credit (state EITC): percentage of federal EIC (refundable) | Minn. Stat. § 290.0671 |
| MN-T1-10 | K-12 Education Credit: credit for qualifying education expenses (income-limited) | Minn. Stat. § 290.0674 |
| MN-T1-11 | Child and Dependent Care Credit: percentage of federal credit | Minn. Stat. § 290.067 |

## Section 6: Tier 2 rules — requires judgment

**Section 6: Tier 2 rules — requires judgment**

| Rule ID | Rule | Guidance |
| --- | --- | --- |
| MN-T2-01 | **Residency determination** — Minnesota uses a domicile test. A person domiciled in Minnesota is a resident. Spending 183+ days in MN creates a presumption of residency. | If taxpayer has homes in multiple states, flag for professional review. |
| MN-T2-02 | **Bonus depreciation add-back** — Track multi-year timing differences between federal and Minnesota depreciation on Schedule M1AR. | Maintain a depreciation schedule parallel to federal. |
| MN-T2-03 | **Social Security subtraction** — Minnesota taxes Social Security for higher-income taxpayers but provides a partial subtraction. Phase-out applies based on provisional income. | Compute the subtraction using the worksheet in M1 instructions. |
| MN-T2-04 | **Credit for taxes paid to other states (Schedule M1CR)** — Non-refundable credit to prevent double taxation. | Requires the other state's return to compute. |
| MN-T2-05 | **Marriage credit** — Reduces the marriage penalty for two-earner MFJ couples. Income-based calculation. | Compute using Schedule M1MA. |
| MN-T2-06 | **Alternative minimum tax** — Minnesota imposes a state AMT (Schedule M1MT). Self-employed with large § 179 or depreciation differences should check. | Compute AMT if federal AMT preferences are significant. |

## Section 7: Supplier pattern library

**Section 7: Supplier pattern library**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| W-2 wages from Minnesota employer | MN withholding applies; include on M1 | Most common |
| Schedule C net profit (sole prop) | Flows through federal taxable income → MN taxable income | QBI deduction add-back required |
| Rental income (Schedule E) | Included in federal taxable income → MN taxable income | MN-source if property in MN |
| Interest on U.S. government bonds | Subtract from MN taxable income | Minn. Stat. § 290.0132 |
| Interest on non-MN muni bonds | No addition needed (already in federal taxable income if taxed federally) | Check if exempt at federal level |
| Social Security benefits | Partial subtraction available (income-limited) | Use worksheet in M1 instructions |
| Capital gains from asset sale | Included in federal taxable income → MN taxable income | No special MN rate |
| 1099-NEC freelance income | Flows through Schedule C → federal taxable income | Estimated payments likely needed |

## Section 8: Form mapping

**Section 8: Form mapping**

| Minnesota form / schedule | What it covers | Federal counterpart |
| --- | --- | --- |
| Form M1 | Minnesota Individual Income Tax Return | Form 1040 |
| Schedule M1M | Income Additions and Subtractions | Schedule 1 (Form 1040) |
| Schedule M1W | Minnesota Withholding | W-2/1099 withholding summary |
| Schedule M1CR | Credit for Taxes Paid to Other States | N/A |
| Schedule M1MA | Marriage Credit | N/A |
| Schedule M1MT | Alternative Minimum Tax | Form 6251 |
| Schedule M1AR | Accelerated Depreciation Adjustment | N/A |
| Schedule M1WFC | Working Family Credit (state EITC) | Schedule EIC |
| Schedule M1ED | K-12 Education Credit | N/A |
| Form M14 | Estimated Tax Instructions | Form 1040-ES |

## Section 9: Refusal catalogue

**Section 9: Refusal catalogue**

| ID | Situation | Action |
| --- | --- | --- |
| MN-R-01 | Part-year or non-resident return (Schedule M1NR) | Refuse — out of scope |
| MN-R-02 | Corporate franchise tax (Form M4) | Refuse — out of scope |
| MN-R-03 | Estate tax (Form M706) | Refuse — out of scope |
| MN-R-04 | Partnership / S-corp pass-through returns | Refuse — out of scope |
| MN-R-05 | Multi-state income apportionment | Refuse — flag for professional review |
| MN-R-06 | Amended returns (Form M1X) | Refuse — out of scope |
| MN-R-07 | Tax year other than current | Refuse — rates and thresholds may differ |
| MN-R-08 | MinnesotaCare provider tax | Refuse — different tax type |

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
