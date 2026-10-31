---
name: wi-income-tax
description: Use this skill whenever asked about Wisconsin individual income tax, Wisconsin Form 1, Wisconsin graduated tax rates, Wisconsin self-employment income tax at the state level, Wisconsin sliding-scale standard deduction, or any Wisconsin personal income tax question for sole proprietors. Trigger on phrases like "Wisconsin income tax", "WI income tax", "Wisconsin Form 1", "Wisconsin tax brackets", "Wisconsin 7.65%", "Wis. Stat. 71", or any request involving Wisconsin state individual income tax computation or filing.
version: "0.1"
jurisdiction: US-WI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# WI Income Tax

## Wisconsin Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers the Wisconsin individual income tax return (Form 1) for full-year Wisconsin residents who are sole proprietors or single-member LLC owners. It addresses the graduated rate computation, Wisconsin income starting from federal AGI, the sliding-scale standard deduction, and Wisconsin-specific credits.

> **Quality tier.** Q3 — AI-drafted, not independently verified. All rates and rules are sourced from the Wisconsin Department of Revenue publications and third-party research current as of May 2026. A licensed CPA or EA should verify before relying on this skill for filing.

## Section 1: Metadata

- **Jurisdiction** — Wisconsin, United States
- **Jurisdiction code** — US-WI
- **Tax type** — Individual income tax
- **Rate structure** — Graduated (4 brackets)
- **Rate range** — 3.50% – 7.65%
- **Primary form** — Form 1 (Wisconsin Income Tax Return)
- **Governing statute** — Wisconsin Statutes Chapter 71
- **Tax authority** — Wisconsin Department of Revenue (DOR)
- **Filing portal** — https://www.revenue.wi.gov
- **Tax year covered** — 2025 (filed 2026) and 2026 (filed 2027)
- **Last updated** — May 22, 2026

### Sources

**Sources table**

| # | Source | URL |
| --- | --- | --- |
| 1 | Wisconsin DOR — Income Tax | https://www.revenue.wi.gov/pages/individ/home.aspx |
| 2 | 2025 Form 1 Instructions (I-111) | https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf |
| 3 | 2025 Wisconsin Act 15 (Budget Bill) — Tax rate changes | https://docs.legis.wisconsin.gov/2025/related/acts/15 |
| 4 | Tax Foundation — Wisconsin profile | https://taxfoundation.org/location/wisconsin/ |

## Section 2: Quick reference — rates and thresholds

### Tax brackets — Single / Head of Household (2025 and 2026, per Act 15)

**Tax brackets — Single / Head of Household**

| Taxable income bracket | Marginal rate |
| --- | --- |
| $0 – $14,680 | 3.50% |
| $14,681 – $50,480 | 4.40% |
| $50,481 – $323,290 | 5.30% |
| $323,291 and above | 7.65% |

### Tax brackets — Married filing jointly (2025 and 2026)

**Tax brackets — Married filing jointly**

| Taxable income bracket | Marginal rate |
| --- | --- |
| $0 – $19,580 | 3.50% |
| $19,581 – $67,300 | 4.40% |
| $67,301 – $431,060 | 5.30% |
| $431,061 and above | 7.65% |

### Tax brackets — Married filing separately (2025 and 2026)

**Tax brackets — Married filing separately**

| Taxable income bracket | Marginal rate |
| --- | --- |
| $0 – $9,790 | 3.50% |
| $9,791 – $33,650 | 4.40% |
| $33,651 – $215,530 | 5.30% |
| $215,531 and above | 7.65% |

### Standard deduction (sliding scale — 2025)

**Standard deduction (sliding scale)**

| Filing status | Maximum amount | Phase-out begins at WI AGI |
| --- | --- | --- |
| Single | $14,260 | Phases out as income rises |
| Married filing jointly | $26,510 | Phases out as income rises |
| Married filing separately | $12,630 | Phases out as income rises |
| Head of household | $18,220 | Phases out as income rises |

The Wisconsin standard deduction is reduced as income increases. At high income levels, the standard deduction can be reduced to $0. The exact phase-out formula is published annually in the Form 1 instructions.

### Personal exemptions (2025)

**Personal exemptions table**

| Item | Amount |
| --- | --- |
| Personal exemption — taxpayer | $700 |
| Personal exemption — spouse (MFJ) | $700 |
| Each dependent | $700 |
| Additional — age 65+ | $250 per person |

### Other key thresholds

**Other key thresholds table**

| Item | Amount | Source |
| --- | --- | --- |
| Filing deadline | April 15 | Wis. Stat. §71.03(8) |
| Extension | October 15 (automatic with federal) | Wis. Stat. §71.03(8)(b) |
| Estimated tax threshold | $500 expected liability | Wis. Stat. §71.09 |
| State sales tax rate | 5% | Wis. Stat. §77.52 |
| County sales tax | 0.5% (most counties) | Wis. Stat. §77.70 |

## Section 3: How this skill works with the federal return

Wisconsin starts from **federal adjusted gross income (AGI)** — Form 1040, Line 11. This is BEFORE the federal standard deduction and QBI deduction.

**Flow:**
1. Federal Form 1040 is completed (including Schedule C, SE).
2. Federal AGI (Line 11) flows to Wisconsin Form 1, Line 1.
3. Wisconsin additions are applied (Schedule AD) — e.g., state/local tax refunds, depreciation differences.
4. Wisconsin subtractions are applied (Schedule SB) — e.g., US government interest, retirement income.
5. Wisconsin AGI is computed.
6. Wisconsin standard deduction (sliding scale) is subtracted.
7. Personal exemptions are subtracted.
8. Wisconsin taxable income is computed; tax is looked up in the tax table or computed from rate schedule.
9. Credits are applied.

**Key structural point:** Because Wisconsin starts from federal AGI, the federal standard deduction and QBI deduction are NOT included. Wisconsin applies its own (sliding-scale) standard deduction. The QBI deduction does not exist for Wisconsin purposes.

### Self-employment tax deduction

- **Self-employment tax deduction flow-through** — The federal deduction for 50% of self-employment tax reduces federal AGI → flows through to Wisconsin automatically.

### Retirement contributions

- **Retirement contributions flow-through** — SEP-IRA, SIMPLE IRA, solo 401(k) contributions reduce federal AGI → flow through automatically.

### Health insurance deduction

- **Health insurance deduction flow-through** — Self-employed health insurance deduction reduces federal AGI → flows through automatically.

### QBI deduction (§199A)

- **QBI deduction not conformed** — Wisconsin does NOT conform to the QBI deduction. Since Wisconsin starts from AGI (before QBI), the §199A deduction is not part of Wisconsin's computation. Wisconsin taxable income will be higher by the QBI amount.

### Home office deduction

- **Home office deduction flow-through** — Reduces Schedule C net profit → reduces federal AGI → flows through.

### Wisconsin retirement income subtraction

- **Retirement income subtraction** — For 2025+, taxpayers age 67+ may subtract up to $24,000 of qualifying retirement income (Act 15). Not typically relevant for active self-employed, but may apply to semi-retired sole proprietors.  _(Act 15)_

### Estimated tax payments

- **Estimated tax payments requirement** — Required if expected Wisconsin tax after withholding and credits exceeds $500. Due dates: April 15, June 15, September 15, January 15. Form 1-ES (voucher).

## Section 5: Tier 1 rules — deterministic

- **[T1-WI-1] Tax computation** — Apply the graduated rate schedule to Wisconsin taxable income based on filing status. Use Wisconsin tax tables (for taxable income under $100,000) or rate schedules (for $100,000+).  _(T1-WI-1)_
- **[T1-WI-2] Starting point** — Begin with federal adjusted gross income from Form 1040, Line 11. Enter on Wisconsin Form 1, Line 1.  _(T1-WI-2)_
- **[T1-WI-3] Wisconsin additions (Schedule AD)** — Common additions for self-employed: - State/local income tax refund (if deducted federally in prior year) - Wisconsin does not conform to federal bonus depreciation §168(k) — add back the difference between federal and Wisconsin depreciation (Section 179 is generally allowed) - Certain capital gain exclusions claimed federally but not recognized by WI  _(T1-WI-3)_
- **[T1-WI-4] Wisconsin subtractions (Schedule SB)** — Common subtractions: - Interest from US government obligations (Treasury bonds) - Retirement income subtraction (age 67+, up to $24,000 per Act 15) - Net operating loss differences (Wisconsin has its own NOL rules) - College savings account (EdVest/Tomorrow's Scholar) contributions — up to $5,130 per beneficiary  _(T1-WI-4)_
- **[T1-WI-5] Standard deduction computation** — Wisconsin uses a sliding-scale standard deduction that decreases as income rises. The deduction amount is calculated using tables in the Form 1 instructions. High-income self-employed individuals may receive $0 standard deduction.  _(T1-WI-5)_
- **[T1-WI-6] Filing due date** — April 15 following the tax year (April 15, 2026 for TY 2025). Extension: October 15 (automatic if federal extension is obtained; file Form 1 by October 15 but pay by April 15).  _(T1-WI-6)_
- **[T1-WI-7] Estimated tax payments** — Required if expected liability exceeds $500. Due dates: April 15, June 15, September 15, January 15. Use Form 1-ES. Underpayment penalty applies if <90% of current year or <100% of prior year liability paid timely.  _(T1-WI-7)_
- **[T1-WI-8] Wisconsin Earned Income Credit** — Varies by number of children: - 1 qualifying child: 4% of federal EIC - 2 qualifying children: 11% of federal EIC - 3+ qualifying children: 34% of federal EIC - No children: not eligible for WI EIC Partially refundable.  _(T1-WI-8)_

## Section 6: Tier 2 rules — requires judgment

- **[T2-WI-1] Residency determination** — Wisconsin defines a resident as a person domiciled in Wisconsin. Domicile is determined by intent and ties (voter registration, driver's license, home ownership, family location). A non-domiciliary maintaining an abode in WI and present 183+ days may also be treated as a resident.  _(T2-WI-1)_
- **[T2-WI-2] Depreciation differences** — Wisconsin requires its own depreciation schedule for assets placed in service after 2000 where federal bonus depreciation was claimed. This creates a tracking requirement — Wisconsin depreciation may differ from federal depreciation in each year. Reviewer must maintain a Wisconsin-specific depreciation schedule.  _(T2-WI-2)_
- **[T2-WI-3] Multi-state credit** — Wisconsin allows a credit for net income taxes paid to other states on income also taxable by Wisconsin. The credit cannot exceed Wisconsin tax attributable to the other-state income. Computed on Schedule OS.  _(T2-WI-3)_
- **[T2-WI-4] Sliding-scale standard deduction phase-out** — The exact amount depends on the taxpayer's Wisconsin AGI and filing status. For higher-income self-employed individuals, the standard deduction may be $0, making this determination critical. The phase-out formula changes annually.  _(T2-WI-4)_
- **[T2-WI-5] Manufacturer's and agriculture credit** — Certain qualifying manufacturing or agricultural activities may be eligible for a credit that can reduce the effective tax rate. Requires detailed analysis of qualifying income.  _(T2-WI-5)_

## Section 7: Supplier pattern library

**Supplier pattern library table**

| Income/deduction type | Wisconsin treatment | Notes |
| --- | --- | --- |
| Schedule C net profit | Included via federal AGI | No adjustment |
| Self-employment tax deduction | Included via federal AGI reduction | No adjustment |
| SEP/SIMPLE/solo 401(k) | Included via federal AGI reduction | No adjustment |
| QBI deduction (§199A) | NOT included — WI starts from AGI | WI taxable income higher |
| Self-employed health insurance | Included via federal AGI reduction | No adjustment |
| Home office deduction | Included via Schedule C → AGI reduction | No adjustment |
| Federal bonus depreciation (§168(k)) | Add back; use WI depreciation | Tracking required |
| US government bond interest | Subtract | Exempt from WI tax |
| State/local tax refund | Add if deducted in prior year | Follows federal treatment |
| Social Security benefits | Exempt (not included in WI income) | Subtract if included in AGI |

## Section 8: Form mapping

**Form mapping table**

| Form 1 Line | Description | Source |
| --- | --- | --- |
| Line 1 | Federal adjusted gross income | Form 1040, Line 11 |
| Line 2 | Wisconsin additions (Schedule AD) | Computed |
| Line 3 | Total (Line 1 + Line 2) | Computed |
| Line 4 | Wisconsin subtractions (Schedule SB) | Computed |
| Line 5 | Wisconsin income (Line 3 − Line 4) | Computed |
| Line 7 | Standard deduction (sliding scale) | From instructions table |
| Line 9 | Exemptions ($700 × number) | Computed |
| Line 11 | Wisconsin taxable income | Line 5 − 7 − 9 |
| Line 12 | Tax (from tax table or rate schedule) | Per brackets |
| Line 19 | Credits | Various |
| Line 26+ | Payments (withholding, estimated) | W-2s, Form 1-ES |

## Section 9: Refusal catalogue

**Refusal catalogue table**

| ID | Refusal | Reason |
| --- | --- | --- |
| R-WI-1 | Part-year resident return | Requires income allocation |
| R-WI-2 | Nonresident return (Form 1NPR) | Different form and sourcing rules |
| R-WI-3 | Wisconsin corporate income/franchise tax | Different tax type (Form 4) |
| R-WI-4 | Wisconsin estate/inheritance tax | No longer in effect (repealed) |
| R-WI-5 | Manufacturer's/agriculture credit computation | Specialized credit with complex qualification |
| R-WI-6 | Amended returns (Form 1X) | Requires additional procedures |
| R-WI-7 | Wisconsin alternative minimum tax (Schedule MT) | Requires separate parallel computation |
| R-WI-8 | Farmland preservation credit | Specialized credit requiring assessments |

- **R-WI-1** — Part-year resident return  _(Requires income allocation)_
- **R-WI-2** — Nonresident return (Form 1NPR)  _(Different form and sourcing rules)_
- **R-WI-3** — Wisconsin corporate income/franchise tax  _(Different tax type (Form 4))_
- **R-WI-4** — Wisconsin estate/inheritance tax  _(No longer in effect (repealed))_
- **R-WI-5** — Manufacturer's/agriculture credit computation  _(Specialized credit with complex qualification)_
- **R-WI-6** — Amended returns (Form 1X)  _(Requires additional procedures)_
- **R-WI-7** — Wisconsin alternative minimum tax (Schedule MT)  _(Requires separate parallel computation)_
- **R-WI-8** — Farmland preservation credit  _(Specialized credit requiring assessments)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only. They do not constitute tax advice, legal advice, or a substitute for the professional judgment of a qualified CPA, Enrolled Agent, or tax attorney. Tax law changes frequently; always verify rates, thresholds, and rules against current official sources before filing. The contributors and maintainers of OpenAccountants accept no liability for errors, omissions, or actions taken based on this content.

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
