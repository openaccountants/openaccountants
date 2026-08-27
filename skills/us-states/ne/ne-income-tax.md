---
name: ne-income-tax
description: Use this skill whenever asked about Nebraska individual income tax for self-employed / sole proprietors. Trigger on phrases like "Nebraska income tax", "NE income tax", "Form 1040N", "Nebraska Department of Revenue", "NE self-employment tax".
version: "0.1"
jurisdiction: US-NE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NE Income Tax

## Nebraska Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers Nebraska Form 1040N (Nebraska Individual Income Tax Return) for full-year NE residents who are sole proprietors or single-member LLC owners. Tax year 2025 (returns filed in 2026). Nebraska uses a four-bracket graduated rate structure ranging from 2.46% to 5.20%.
>
> **Quality tier.** Q3 — AI-drafted, not independently verified. All outputs must be reviewed by a qualified tax professional before filing.

## Section 1: Metadata

**Metadata table**

**Metadata table**

| Field | Value |
| --- | --- |
| Tax type | Individual income tax |
| Jurisdiction | Nebraska (US-NE) |
| Tax year | 2025 (filed 2026) |
| Primary form | Form 1040N |
| Supporting schedules | Schedule I (Nebraska Adjustments to Income), Schedule II (Credits), Schedule III (Computation of Nebraska Tax) |
| Tax structure | Graduated (4 brackets) |
| Rate range | 2.46% – 5.20% (TY 2025) |
| Filing deadline | April 15, 2026 |
| Extension deadline | October 15, 2026 |
| Tax authority | Nebraska Department of Revenue |
| Website | https://revenue.nebraska.gov |
| Statute | Neb. Rev. Stat. §77-2715.03 |

**Sources:**
- Nebraska Department of Revenue, Individual Income Tax: https://revenue.nebraska.gov/individuals/individual-income-tax
- Neb. Rev. Stat. §77-2715.03 (rate schedule and future rate reductions)
- Nebraska 2025 Individual Income Tax Booklet

## Section 2: Quick reference — rates and thresholds

### Tax brackets — Single / Married filing separately (TY 2025)

**Tax brackets — Single / Married filing separately (TY 2025)**

| Taxable income over | But not over | Rate | Tax on lower amount |
| --- | --- | --- | --- |
| $0 | $4,030 | 2.46% | $0 |
| $4,030 | $24,120 | 3.51% | $99.14 |
| $24,120 | $38,870 | 5.01% | $804.30 |
| $38,870 | — | 5.20% | $1,543.28 |

### Tax brackets — Married filing jointly / Qualifying surviving spouse (TY 2025)

**Tax brackets — Married filing jointly / Qualifying surviving spouse (TY 2025)**

| Taxable income over | But not over | Rate | Tax on lower amount |
| --- | --- | --- | --- |
| $0 | $8,040 | 2.46% | $0 |
| $8,040 | $48,250 | 3.51% | $197.78 |
| $48,250 | $77,730 | 5.01% | $1,609.15 |
| $77,730 | — | 5.20% | $3,086.10 |

### Tax brackets — Head of household (TY 2025)

**Tax brackets — Head of household (TY 2025)**

| Taxable income over | But not over | Rate | Tax on lower amount |
| --- | --- | --- | --- |
| $0 | $7,510 | 2.46% | $0 |
| $7,510 | $38,590 | 3.51% | $184.75 |
| $38,590 | $57,630 | 5.01% | $1,275.66 |
| $57,630 | — | 5.20% | $2,229.56 |

### Upcoming rate reductions

**Upcoming rate reductions**  _(Neb. Rev. Stat. §77-2715.03)_

| Tax year | Bracket 3 rate | Bracket 4 (top) rate | Source |
| --- | --- | --- | --- |
| 2025 | 5.01% | 5.20% | Neb. Rev. Stat. §77-2715.03 |
| 2026 | 4.55% | 4.55% | Neb. Rev. Stat. §77-2715.03 |
| 2027+ | 3.99% | 3.99% | Neb. Rev. Stat. §77-2715.03 |

### Standard deduction

Nebraska does **not** have its own standard deduction. The starting point is federal AGI, and Nebraska applies its own adjustments to arrive at Nebraska taxable income.

### Personal exemption credit (TY 2025)

**Personal exemption credit (TY 2025)**

| Filing status | Credit amount |
| --- | --- |
| Single | $157 |
| Married filing jointly | $314 |
| Each dependent | $157 |

### Local income tax

Nebraska does **not** permit local income taxes.

## Section 3: How this skill works with the federal return

Nebraska taxable income starts with **federal adjusted gross income (AGI)** from federal Form 1040, Line 11.

1. **Start with federal AGI** → Form 1040N, Line 3
2. **Add NE additions** (Schedule I) — items NE adds back
3. **Subtract NE subtractions** (Schedule I) — items NE excludes
4. **Subtract Nebraska standard deduction or itemized deductions** (Nebraska follows federal amounts with modifications)
5. **Result = Nebraska taxable income**
6. **Apply the graduated rate schedule** → Nebraska tax
7. **Subtract personal exemption credit and other credits** (Schedule II)
8. **Result = final tax due or refund**

### Key addition modifications (Schedule I)

**Key addition modifications (Schedule I)**

| Addition | Description |
| --- | --- |
| State/local bond interest | Interest from bonds of states other than NE |
| Bonus depreciation add-back | NE partially decouples from IRC §168(k) — verify current conformity status |

### Key subtraction modifications (Schedule I)

**Key subtraction modifications (Schedule I)**

| Subtraction | Description |
| --- | --- |
| US government bond interest | Interest from US Treasury obligations |
| State income tax refund | If included in federal AGI |
| Social Security (partial) | Nebraska is phasing out Social Security taxation — for TY 2025, Social Security benefits are fully exempt |

## Section 4: Self-employed specific rules

### Self-employment income flow

Schedule C net profit flows into federal AGI, which is the starting point for Nebraska. Nebraska conforms to the federal self-employment tax deduction (the deductible half of SE tax is already reflected in federal AGI).

### Estimated tax

- **Estimated tax threshold** — Nebraska requires estimated tax payments if you expect to owe $500 or more in Nebraska income tax after subtracting withholding and credits.

**Estimated tax installment due dates**

| Installment | Due date |
| --- | --- |
| 1st quarter | April 15 |
| 2nd quarter | June 15 |
| 3rd quarter | September 15 |
| 4th quarter | January 15 (following year) |

Form 1040N-ES is used for estimated tax payments.

### Depreciation

Nebraska's conformity with federal bonus depreciation under IRC §168(k) should be verified for the current tax year. Nebraska has historically required partial add-backs for bonus depreciation in certain years. Check the 2025 Form 1040N instructions.

### Nebraska inheritance tax

Nebraska is one of six states with an inheritance tax (separate from estate tax). This is administered at the county level and is **not** covered by this income tax skill. Self-employed taxpayers should be aware of this for estate planning purposes.

## Section 5: Tier 1 rules — deterministic

**Tier 1 rules table**

| Rule ID | Rule | Source |
| --- | --- | --- |
| NE-T1-01 | NE taxable income = federal AGI ± NE modifications − NE standard/itemized deduction | Neb. Rev. Stat. §77-2716 |
| NE-T1-02 | Tax computed using 4-bracket schedule: 2.46%, 3.51%, 5.01%, 5.20% (TY 2025) | Neb. Rev. Stat. §77-2715.03 |
| NE-T1-03 | Starting point is federal AGI (Form 1040, Line 11) | Neb. Rev. Stat. §77-2716 |
| NE-T1-04 | Personal exemption credit: $157 per exemption (TY 2025) | Neb. Rev. Stat. §77-2716.01 |
| NE-T1-05 | Estimated tax required if expected liability ≥ $500 | Neb. Rev. Stat. §77-2770 |
| NE-T1-06 | Social Security benefits fully exempt for TY 2025 | Neb. Rev. Stat. §77-2716 (LB 873, 2024) |
| NE-T1-07 | Top rate drops to 4.55% for TY 2026 and 3.99% for TY 2027 | Neb. Rev. Stat. §77-2715.03 |

## Section 6: Tier 2 rules — requires judgment

**Tier 2 rules table**

| Rule ID | Situation | Guidance |
| --- | --- | --- |
| NE-T2-01 | **Multi-state income:** Taxpayer has income from another state | NE allows a credit for taxes paid to other states. Requires allocation review and Schedule II. |
| NE-T2-02 | **Business vs. hobby determination** | NE follows federal hobby loss rules. If IRS disallows Schedule C, NE deductions are also disallowed. |
| NE-T2-03 | **Bonus depreciation conformity** | Verify NE's current IRC §168(k) conformity status for TY 2025. Add-backs may be required. |
| NE-T2-04 | **Nebraska Advantage Act credits** | Business incentive credits under the Nebraska Advantage Act may be available. Requires verification of certification and compliance. |
| NE-T2-05 | **Community property** | Nebraska is NOT a community property state. Standard federal rules apply for MFS. |

## Section 7: Supplier pattern library

**Supplier pattern library table**

| Input needed | Where to find it |
| --- | --- |
| Federal AGI | Federal Form 1040, Line 11 |
| NE additions | Schedule I (computed from federal return) |
| NE subtractions | Schedule I (computed from federal return) |
| Standard/itemized deduction | Federal amounts with NE modifications |
| Personal exemption credit | Based on filing status and dependents |
| Tax credits | Schedule II |
| Estimated tax payments | 1040N-ES records |
| NE withholding | W-2 Box 17 / 1099 NE withholding amounts |

## Section 8: Form mapping

**Form mapping table**

| Form 1040N Line | Description | Source |
| --- | --- | --- |
| Line 3 | Federal adjusted gross income | Federal 1040, Line 11 |
| Line 4 | Nebraska additions | Schedule I |
| Line 5 | Nebraska subtractions | Schedule I |
| Line 7 | Nebraska standard or itemized deduction | Computed |
| Line 10 | Nebraska taxable income | Computed |
| Line 11 | Nebraska income tax | From tax table or Schedule III |
| Line 14 | Personal exemption credit | $157 × number of exemptions |
| Line 20 | Other credits | Schedule II |
| Line 26 | Nebraska income tax withheld | W-2s / 1099s |
| Line 27 | Estimated tax payments | 1040N-ES payments |
| Line 33 | Amount owed or refund | Computed |

## Section 9: Refusal catalogue

**Refusal catalogue table**

| Refusal ID | Trigger | Response |
| --- | --- | --- |
| R-NE-01 | Part-year or nonresident | "NE part-year and nonresident returns require Schedule III allocation. This is outside the scope of this skill." |
| R-NE-02 | Corporate return | "This skill covers individual income tax only (Form 1040N). Corporate returns (Form 1120N) are not covered." |
| R-NE-03 | Fiduciary return | "NE fiduciary returns (Form 1041N) are not covered by this skill." |
| R-NE-04 | Amended return | "NE amended returns (Form 1040XN) are not covered." |
| R-NE-05 | Inheritance tax | "Nebraska inheritance tax is administered at the county level and is not covered by this skill." |

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
