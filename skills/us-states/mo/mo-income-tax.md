---
name: mo-income-tax
description: Use this skill whenever asked about Missouri individual income tax for self-employed persons, sole proprietors, or single-member LLCs. Trigger on phrases like "Missouri income tax", "MO income tax", "Form MO-1040", "Missouri DOR", "RSMo § 143".
version: "0.1"
jurisdiction: US-MO
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MO Income Tax

## Missouri Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers Missouri Form MO-1040 for full-year Missouri residents who are sole proprietors or single-member LLC owners. Missouri uses an eight-bracket graduated income tax with rates from 0% to 4.7% (TY 2025–2026). Same brackets apply to all filing statuses.
>
> **Quality tier.** Q3 — AI-drafted, not independently verified. All rates and thresholds were researched on 2026-05-22 from official Missouri Department of Revenue publications. A qualified professional must review before filing.

## Section 1: Metadata

**Section 1 Metadata**

| Field | Value |
| --- | --- |
| Jurisdiction | Missouri (US-MO) |
| Tax type | Individual income tax |
| Primary form | Form MO-1040 |
| Tax year | 2025 (filed April 2026) and 2026 |
| Authority | Missouri Department of Revenue |
| Statute | RSMo § 143.011 et seq. |
| Version | 0.1 |
| Last updated | 2026-05-22 |
| Validation | AI-drafted — Q3 |

### Sources consulted

**Sources consulted**

| # | Source | URL |
| --- | --- | --- |
| 1 | Missouri DOR — Individual Income Tax Year Changes | https://dor.mo.gov/taxation/individual/tax-types/income/year-changes/ |
| 2 | RSMo § 143.011 (tax rate) | https://revisor.mo.gov/main/OneSection.aspx?section=143.011 |
| 3 | Missouri Form MO-1040 Instructions | https://dor.mo.gov/taxation/individual/tax-types/income/forms/ |
| 4 | RSMo § 143.121 (Missouri adjusted gross income) | https://revisor.mo.gov/main/OneSection.aspx?section=143.121 |

## Section 2: Quick reference — rates and thresholds

### Tax rates — TY 2025 / 2026 (all filing statuses)

**Tax rates — TY 2025 / 2026 (all filing statuses)**

| Missouri taxable income | Tax |
| --- | --- |
| $0 – $1,313 | $0 (0%) |
| Over $1,313 – $2,626 | 2.0% of excess over $1,313 |
| Over $2,626 – $3,939 | $26 + 2.5% of excess over $2,626 |
| Over $3,939 – $5,252 | $59 + 3.0% of excess over $3,939 |
| Over $5,252 – $6,565 | $98 + 3.5% of excess over $5,252 |
| Over $6,565 – $7,878 | $144 + 4.0% of excess over $6,565 |
| Over $7,878 – $9,191 | $197 + 4.5% of excess over $7,878 |
| Over $9,191 | $256 + 4.7% of excess over $9,191 |

Missouri uses the **same brackets for all filing statuses**. The standard deduction varies by filing status, which determines how much income is subject to tax.

### Standard deduction — TY 2025

**Standard deduction — TY 2025**

| Filing status | Amount |
| --- | --- |
| Single | $15,750 |
| MFJ / Qualifying Surviving Spouse | $31,500 |
| MFS | $15,750 |
| Head of Household | $23,625 |

Missouri does NOT have a separate personal exemption. The standard deduction is the primary below-the-line deduction.

### Key thresholds

**Key thresholds**

| Item | Value | Source |
| --- | --- | --- |
| Filing deadline | April 15, 2026 (for TY 2025) | RSMo § 143.511 |
| Extension | Automatic 6-month with federal extension | RSMo § 143.511 |
| Estimated tax threshold | $100 expected liability | RSMo § 143.521 |
| Capital gains subtraction | 100% of net capital gains (effective TY 2025) | RSMo § 143.022 |

### City earnings taxes

**City earnings taxes**

| City | Rate | Notes |
| --- | --- | --- |
| Kansas City | 1.0% | On earned income; separate return |
| St. Louis | 1.0% | On earned income; separate return |

## Section 3: How this skill works with the federal return

- **Missouri AGI starting point** — Missouri adjusted gross income begins with federal adjusted gross income (AGI) from federal Form 1040, Line 11, then applies Missouri-specific modifications.
- **Additions (Form MO-A)** — Add back items Missouri does not exclude (e.g., interest on non-Missouri state/municipal bonds).
- **Subtractions (Form MO-A)** — Subtract items Missouri excludes: 100% of net capital gains (effective TY 2025); Social Security benefits included in federal AGI; Federal income tax deduction (Missouri is one of few states that allows a deduction for federal income tax paid, capped at $5,000 single / $10,000 MFJ); U.S. government bond interest.
- **Missouri AGI** — Federal AGI + additions − subtractions.
- **Standard or itemized deduction** — Missouri conforms to federal amounts (with some modifications).
- **Missouri taxable income** — Missouri AGI − deductions.
- **Tax** — Apply the eight graduated brackets.
- **Credits** — Apply applicable credits.

## Section 4: Self-employed specific rules

- **Self-employment income flow** — Self-employment income flows through federal Schedule C → federal AGI → Missouri AGI. No separate Missouri schedule for self-employment income.
- **Federal SE tax deduction** — Reflected in federal AGI; carries through to Missouri automatically.
- **Federal income tax deduction** — Missouri allows a deduction for federal income tax paid (including SE tax), capped at $5,000 (single/HoH/MFS) or $10,000 (MFJ). This is a significant benefit.
- **Capital gains subtraction** — 100% of net capital gains reported on the federal return may be subtracted from Missouri AGI (effective TY 2025). If a sole proprietor sells business assets, the gain may qualify.
- **Estimated taxes** — Self-employed taxpayers must make quarterly estimated payments (Form MO-1040ES) if expected liability exceeds $100. Due dates: April 15, June 15, September 15, January 15.
- **Health insurance deduction** — Self-employed health insurance deduction is in federal AGI. No Missouri add-back.
- **City earnings tax** — If located in Kansas City or St. Louis, self-employment earnings are subject to the 1% city earnings tax (separate filing required).

## Section 5: Tier 1 rules — deterministic

**Tier 1 rules — deterministic**

| Rule ID | Rule | Source |
| --- | --- | --- |
| MO-T1-01 | Start with federal AGI (Form 1040, Line 11) | RSMo § 143.121 |
| MO-T1-02 | Add back interest on non-Missouri state/municipal bonds | RSMo § 143.121 |
| MO-T1-03 | Subtract federal income tax paid (up to $5,000 single / $10,000 MFJ) | RSMo § 143.171 |
| MO-T1-04 | Subtract Social Security benefits included in federal AGI (fully exempt) | RSMo § 143.124 |
| MO-T1-05 | Subtract U.S. government bond interest | RSMo § 143.121 |
| MO-T1-06 | Subtract 100% of net capital gains (TY 2025+) | RSMo § 143.022 |
| MO-T1-07 | Apply standard deduction: $15,750 (single), $31,500 (MFJ), $23,625 (HoH) | RSMo § 143.131 |
| MO-T1-08 | Apply graduated rates: 0% to 4.7% across 8 brackets | RSMo § 143.011 |
| MO-T1-09 | Missouri Property Tax Credit: refundable credit for seniors/disabled (Form MO-PTC) | RSMo § 135.010 |
| MO-T1-10 | Missouri Earned Income Credit: percentage of federal EIC (non-refundable) | RSMo § 143.174 |

## Section 6: Tier 2 rules — requires judgment

**Tier 2 rules — requires judgment**

| Rule ID | Rule | Guidance |
| --- | --- | --- |
| MO-T2-01 | **Residency determination** — Missouri uses a domicile test. A person domiciled in Missouri is a full-year resident. | If taxpayer has homes in multiple states, flag for professional review. |
| MO-T2-02 | **Federal tax deduction** — The deduction is for federal tax actually paid (not accrued). Compute using taxes paid during the calendar year, including estimated payments and withholding. | This interacts with federal refunds/balances due in a circular manner. Use prior-year federal tax paid as a proxy. |
| MO-T2-03 | **Capital gains subtraction** — Applies to net long-term capital gains. Determine which gains qualify (e.g., business asset sales, stock sales). | Ensure net capital gains are correctly computed before applying 100% subtraction. |
| MO-T2-04 | **Credit for taxes paid to other states (Form MO-CR)** — Non-refundable credit to prevent double taxation. | Requires the other state's return. |
| MO-T2-05 | **Kansas City / St. Louis earnings tax** — Self-employed persons with business activity in these cities must file separately. | Flag if taxpayer operates in KC or STL. |
| MO-T2-06 | **Standard vs. itemized deduction** — Missouri allows either; if itemizing, Missouri generally conforms to federal Schedule A with modifications. | Compare both methods; Missouri itemized deductions may differ from federal. |

## Section 7: Supplier pattern library

**Supplier pattern library**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| W-2 wages from Missouri employer | MO withholding applies; include on MO-1040 | Most common |
| Schedule C net profit (sole prop) | Flows through federal AGI → Missouri AGI | Federal tax deduction available |
| Rental income (Schedule E) | Included in federal AGI → Missouri AGI | MO-source if property in MO |
| Interest on U.S. government bonds | Subtract from Missouri AGI | RSMo § 143.121 |
| Interest on non-MO muni bonds | Add back to Missouri AGI | Taxable for MO purposes |
| Social Security benefits | Subtract from Missouri AGI (fully exempt) | RSMo § 143.124 |
| Long-term capital gains | Subtract 100% from Missouri AGI (TY 2025+) | RSMo § 143.022 |
| 1099-NEC freelance income | Flows through Schedule C → federal AGI | Estimated payments likely needed |
| Federal income tax paid | Deductible up to $5,000 (single) / $10,000 (MFJ) | RSMo § 143.171 |

## Section 8: Form mapping

**Form mapping**

| Missouri form / schedule | What it covers | Federal counterpart |
| --- | --- | --- |
| Form MO-1040 | Missouri Individual Income Tax Return | Form 1040 |
| Form MO-A | Missouri Adjustments (additions/subtractions) | Schedule 1 (Form 1040) |
| Form MO-CR | Credit for Taxes Paid to Other States | N/A |
| Form MO-1040ES | Estimated Tax Payment Voucher | Form 1040-ES |
| Form MO-PTC | Property Tax Credit | N/A |
| Form MO-1040P | Part-year Resident Return | N/A |
| Form MO-NRI | Non-Resident Return | N/A |
| Schedule MO-SI | Self-Employed Tax Credit Schedule | N/A |

## Section 9: Refusal catalogue

**Refusal catalogue**

| ID | Situation | Action |
| --- | --- | --- |
| MO-R-01 | Part-year or non-resident return (MO-1040P / MO-NRI) | Refuse — out of scope |
| MO-R-02 | Corporate income tax (Form MO-1120) | Refuse — out of scope |
| MO-R-03 | Kansas City or St. Louis earnings tax return | Refuse — separate filing; out of scope |
| MO-R-04 | Multi-state income apportionment | Refuse — flag for professional review |
| MO-R-05 | Amended returns (Form MO-1040X) | Refuse — out of scope |
| MO-R-06 | Tax year other than current | Refuse — rates and thresholds may differ |
| MO-R-07 | Partnership / S-corp returns (MO-1065 / MO-1120S) | Refuse — out of scope |

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
