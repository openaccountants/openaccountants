---
name: nd-income-tax
description: Use this skill whenever asked about North Dakota individual income tax for self-employed / sole proprietors. Trigger on phrases like "North Dakota income tax", "ND income tax", "Form ND-1", "ND Tax Commissioner", "ND self-employment tax".
version: "0.1"
jurisdiction: US-ND
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ND Income Tax

## North Dakota Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers North Dakota Form ND-1 (Individual Income Tax Return) for full-year ND residents who are sole proprietors or single-member LLC owners. Tax year 2025 (returns filed in 2026). North Dakota uses a three-bracket graduated rate structure with a 0% first bracket, making it one of the lowest-tax states.
>
> **Quality tier.** Q3 — AI-drafted, not independently verified. All outputs must be reviewed by a qualified tax professional before filing.

## Section 1: Metadata

**Metadata table**

| Field | Value |
| --- | --- |
| Tax type | Individual income tax |
| Jurisdiction | North Dakota (US-ND) |
| Tax year | 2025 (filed 2026) |
| Primary form | Form ND-1 |
| Supporting schedules | Schedule ND-1SA (Modifications), Schedule ND-1TC (Credits), Schedule ND-1NR (Nonresidents/Part-year) |
| Tax structure | Graduated (3 brackets) |
| Rate range | 0% – 2.50% |
| Filing deadline | April 15, 2026 |
| Extension deadline | October 15, 2026 |
| Tax authority | North Dakota Office of State Tax Commissioner |
| Website | https://www.tax.nd.gov |
| Statute | N.D.C.C. Chapter 57-38 |

**Sources:**
- ND Office of State Tax Commissioner, Individual Income Tax: https://www.tax.nd.gov/tax-types/individual-income-tax
- ND Office of State Tax Commissioner, 2025 Individual Income Tax Booklet: https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf
- N.D.C.C. §57-38-30.3 (tax rates)

## Section 2: Quick reference — rates and thresholds

### Tax brackets — Single (TY 2025)

**Tax brackets — Single (TY 2025)**

| Taxable income over | But not over | Rate | Tax on lower amount |
| --- | --- | --- | --- |
| $0 | $48,475 | 0.00% | $0 |
| $48,475 | $244,825 | 1.95% | $0 |
| $244,825 | — | 2.50% | $3,828.83 |

### Tax brackets — Married filing jointly / Qualifying surviving spouse (TY 2025)

**Tax brackets — Married filing jointly / Qualifying surviving spouse (TY 2025)**

| Taxable income over | But not over | Rate | Tax on lower amount |
| --- | --- | --- | --- |
| $0 | $80,975 | 0.00% | $0 |
| $80,975 | $298,075 | 1.95% | $0 |
| $298,075 | — | 2.50% | $4,233.45 |

### Tax brackets — Married filing separately (TY 2025)

**Tax brackets — Married filing separately (TY 2025)**

| Taxable income over | But not over | Rate | Tax on lower amount |
| --- | --- | --- | --- |
| $0 | $40,475 | 0.00% | $0 |
| $40,475 | $149,025 | 1.95% | $0 |
| $149,025 | — | 2.50% | $2,116.73 |

### Tax brackets — Head of household (TY 2025)

**Tax brackets — Head of household (TY 2025)**

| Taxable income over | But not over | Rate | Tax on lower amount |
| --- | --- | --- | --- |
| $0 | $64,950 | 0.00% | $0 |
| $64,950 | $271,450 | 1.95% | $0 |
| $271,450 | — | 2.50% | $4,026.75 |

### Standard deduction

- **ND standard deduction** — North Dakota does not have its own standard deduction. It uses the federal standard deduction as the starting point is federal taxable income (not federal AGI).

### Local income tax

- **Local income tax permitted** — North Dakota does not permit local income taxes.

## Section 3: How this skill works with the federal return

North Dakota taxable income starts with **federal taxable income** from federal Form 1040, Line 15 (not federal AGI — this is different from many other states).

1. **Start with federal taxable income** → ND-1, Line 1
2. **Add ND additions** (Schedule ND-1SA) — items ND adds back
3. **Subtract ND subtractions** (Schedule ND-1SA) — items ND excludes
4. **Result = ND taxable income**
5. **Apply the graduated rate schedule** → ND tax
6. **Subtract credits** (Schedule ND-1TC) → final tax due or refund

### Key addition modifications (Schedule ND-1SA)

**Key addition modifications (Schedule ND-1SA)**

| Addition | Description |
| --- | --- |
| State/local bond interest | Interest from bonds of states other than ND |
| State income tax refund adjustment | If federal treatment differs from ND |

### Key subtraction modifications (Schedule ND-1SA)

**Key subtraction modifications (Schedule ND-1SA)**

| Subtraction | Description |
| --- | --- |
| US government bond interest | Interest from US Treasury obligations |
| Native American reservation income | Income earned by enrolled members on their reservation |
| ND Renaissance Zone income | Income from activity in a designated Renaissance Zone |

## Section 4: Self-employed specific rules

### Self-employment income flow

- **Schedule C flow to ND** — Schedule C net profit flows into federal taxable income, which is the starting point for ND. Because ND starts from federal taxable income (after the standard/itemized deduction and QBI deduction), the federal deductions are already incorporated.

### Estimated tax

- **Estimated tax requirement threshold** — $1,000 USD (ND net tax liability expected)

**Estimated tax installment due dates**

| Installment | Due date |
| --- | --- |
| 1st quarter | April 15 |
| 2nd quarter | June 15 |
| 3rd quarter | September 15 |
| 4th quarter | January 15 (following year) |

Form ND-1ES is used for estimated tax payments. Payments can be made via the North Dakota Taxpayer Access Point (ND TAP).

### Depreciation

- **ND conformity to federal depreciation** — ND generally conforms to federal depreciation rules, including IRC §168(k) bonus depreciation. No state-level add-back is required for bonus depreciation.

### 0% bracket benefit

- **Zero bracket threshold benefit** — The 0% first bracket means that a single filer with ND taxable income of $48,475 or less (or MFJ of $80,975 or less) owes zero ND income tax. This is particularly beneficial for self-employed taxpayers with moderate income.

## Section 5: Tier 1 rules — deterministic

**Tier 1 rules table**

| Rule ID | Rule | Source |
| --- | --- | --- |
| ND-T1-01 | ND taxable income = federal taxable income ± ND modifications | N.D.C.C. §57-38-01 |
| ND-T1-02 | Tax computed using 3-bracket schedule: 0%, 1.95%, 2.50% (TY 2025) | N.D.C.C. §57-38-30.3 |
| ND-T1-03 | Starting point is federal taxable income (Form 1040, Line 15), not federal AGI | N.D.C.C. §57-38-01(7) |
| ND-T1-04 | ND generally conforms to federal depreciation including §168(k) | N.D.C.C. §57-38 |
| ND-T1-05 | Estimated tax required if expected liability ≥ $1,000 | N.D.C.C. §57-38-62 |
| ND-T1-06 | Extension: automatic 6-month extension with valid federal extension | ND Tax Commissioner guidelines |

## Section 6: Tier 2 rules — requires judgment

**Tier 2 rules table**

| Rule ID | Situation | Guidance |
| --- | --- | --- |
| ND-T2-01 | **Multi-state income:** Taxpayer has income from another state | ND allows a credit for taxes paid to other states. Schedule ND-1CR. Requires allocation review. |
| ND-T2-02 | **Renaissance Zone exemption** | Income from qualified ND Renaissance Zones may be exempt. Requires verification of zone designation and compliance with program requirements. |
| ND-T2-03 | **Tribal reservation income** | Income earned by enrolled tribal members on their reservation may be subtracted. Requires verification of enrollment and income sourcing. |
| ND-T2-04 | **Oil and gas income** | ND has specific rules for oil, gas, and mineral income. Production taxes are separate from income tax. Review sourcing. |
| ND-T2-05 | **Federal conformity changes** | ND's IRC conformity is generally rolling. Monitor for any legislative decoupling from recent federal changes. |

## Section 7: Supplier pattern library

**Supplier pattern library table**

| Input needed | Where to find it |
| --- | --- |
| Federal taxable income | Federal Form 1040, Line 15 |
| ND additions | Schedule ND-1SA (computed from federal return) |
| ND subtractions | Schedule ND-1SA (computed from federal return) |
| Tax credits | Schedule ND-1TC |
| Estimated tax payments | ND-1ES records / ND TAP |
| ND withholding | W-2 Box 17 / 1099 ND withholding amounts |

## Section 8: Form mapping

**Form ND-1 line mapping table**

| Form ND-1 Line | Description | Source |
| --- | --- | --- |
| Line 1 | Federal taxable income | Federal 1040, Line 15 |
| Line 2 | ND additions | Schedule ND-1SA |
| Line 3 | ND subtractions | Schedule ND-1SA |
| Line 4 | ND taxable income | Line 1 + Line 2 − Line 3 |
| Line 6 | ND income tax | Computed from rate schedule |
| Line 14 | Total credits | Schedule ND-1TC |
| Line 17 | ND income tax withheld | W-2s / 1099s |
| Line 18 | Estimated tax payments | ND-1ES payments |
| Line 22 | Amount owed or refund | Computed |

## Section 9: Refusal catalogue

**Refusal catalogue table**

| Refusal ID | Trigger | Response |
| --- | --- | --- |
| R-ND-01 | Part-year or nonresident | "ND part-year and nonresident returns require Schedule ND-1NR. This is outside the scope of this skill." |
| R-ND-02 | Corporate return | "This skill covers individual income tax only (Form ND-1). Corporate returns (Form 40) are not covered." |
| R-ND-03 | Estate or trust return | "ND fiduciary returns (Form 38) are not covered by this skill." |
| R-ND-04 | Amended return | "ND amended returns are not covered. File an amended ND-1 with the amended box checked." |
| R-ND-05 | Farm income special rules | "Detailed ND farm income rules (including farm income averaging) require specialist review." |

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
