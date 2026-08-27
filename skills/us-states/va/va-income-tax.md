---
name: va-income-tax
description: Use this skill whenever asked about Virginia individual income tax, Virginia Form 760, Virginia graduated tax rates, Virginia self-employment income tax at the state level, Virginia standard deduction, or any Virginia personal income tax question for sole proprietors. Trigger on phrases like "Virginia income tax", "VA income tax", "Form 760", "Virginia tax brackets", "Virginia 5.75%", "Virginia standard deduction", or any request involving Virginia state individual income tax computation or filing.
version: "0.1"
jurisdiction: US-VA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# VA Income Tax

## Virginia Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers the Virginia individual income tax return (Form 760) for full-year Virginia residents who are sole proprietors or single-member LLC owners. It addresses the graduated rate computation, Virginia adjustments to federal AGI, the standard deduction, and Virginia-specific credits.

> **Quality tier.** Q3 — AI-drafted, not independently verified. All rates and rules are sourced from the Virginia Department of Taxation publications and third-party research current as of May 2026. A licensed CPA or EA should verify before relying on this skill for filing.

## Section 1: Metadata

- **Jurisdiction** — Virginia, United States
- **Jurisdiction code** — US-VA
- **Tax type** — Individual income tax
- **Rate structure** — Graduated (4 brackets)
- **Rate range** — 2% – 5.75%
- **Primary form** — Form 760 (Resident Individual Income Tax Return)
- **Governing statute** — Virginia Code §58.1-320 et seq.
- **Tax authority** — Virginia Department of Taxation
- **Filing portal** — https://www.tax.virginia.gov
- **Tax year covered** — 2025 (filed 2026) and 2026 (filed 2027)
- **Last updated** — May 22, 2026

### Sources

**Sources**

| # | Source | URL |
| --- | --- | --- |
| 1 | Virginia Department of Taxation — Income Tax | https://www.tax.virginia.gov/individual-income-tax |
| 2 | 2025 Form 760 Instructions | https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-760-instructions.pdf |
| 3 | Virginia Code §58.1-320 — Tax rates | https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-320/ |
| 4 | Tax Foundation — Virginia profile | https://taxfoundation.org/location/virginia/ |

## Section 2: Quick reference — rates and thresholds

### Tax brackets (2025 and 2026 — same rates, all filing statuses)

**Tax brackets (2025 and 2026 — same rates, all filing statuses)**

| Taxable income bracket | Marginal rate | Tax on prior brackets |
| --- | --- | --- |
| $0 – $3,000 | 2% | $0 |
| $3,001 – $5,000 | 3% | $60 |
| $5,001 – $17,000 | 5% | $120 |
| $17,001 and above | 5.75% | $720 |

- **Formula for taxable income over $17,000** — Tax = $720 + 5.75% × (taxable income − $17,000)

### Standard deduction (2025 tax year, filed 2026)

**Standard deduction (2025 tax year, filed 2026)**

| Filing status | Standard deduction |
| --- | --- |
| Single | $8,500 |
| Married filing jointly | $17,000 |
| Married filing separately | $8,500 |

### Standard deduction (2026 tax year, filed 2027)

**Standard deduction (2026 tax year, filed 2027)**

| Filing status | Standard deduction |
| --- | --- |
| Single / HoH | $8,750 |
| Married filing jointly | $17,500 |
| Married filing separately | $8,750 |

**Note:** The increased standard deduction is scheduled to sunset after TY 2026, reverting to $3,000 (single) / $6,000 (MFJ) unless extended by the General Assembly.

### Personal exemptions (2025 and 2026)

**Personal exemptions (2025 and 2026)**

| Item | Amount |
| --- | --- |
| Personal exemption — each taxpayer | $930 |
| Personal exemption — each dependent | $930 |
| Age 65+ additional exemption | $800 per person |
| Blind additional exemption | $800 per person |

### Other key thresholds

**Other key thresholds**

| Item | Amount | Source |
| --- | --- | --- |
| Filing threshold (single, under 65) | $11,950 (based on federal filing requirement) | Form 760-I |
| Extension deadline | November 1 (automatic 6-month from May 1) | Va. Code §58.1-344 |
| Filing due date | May 1 (Virginia's unique deadline) | Va. Code §58.1-341 |
| State sales tax rate (general) | 5.3% (4.3% state + 1% local) | Va. Code §58.1-603 |
| Sales tax — Hampton Roads / Northern VA | 6.0% (additional 0.7% regional) | Va. Code §58.1-603.1 |

## Section 3: How this skill works with the federal return

Virginia starts from **federal adjusted gross income (FAGI)** — Form 1040, Line 11. This is BEFORE the federal standard deduction and QBI deduction.

**Flow:**
1. Federal Form 1040 is completed (including Schedule C, SE).
2. Federal AGI (Line 11) flows to Virginia Form 760, Line 1.
3. Virginia additions are applied (Line 2 — e.g., state tax deduction add-back if itemizing for VA while claiming state taxes federally).
4. Virginia subtractions are applied (Line 6 — e.g., Social Security if applicable).
5. Virginia AGI is computed (Line 7 = FAGI + additions − subtractions).
6. Standard deduction OR itemized deductions (must match federal choice) are subtracted.
7. Personal exemptions are subtracted.
8. Virginia taxable income results; tax is computed from the rate table.

**Key structural point:** Because Virginia starts from federal AGI, the federal standard deduction is NOT already baked in. Virginia applies its own (typically larger) standard deduction. The QBI deduction (§199A) is also NOT included in the starting point — it does not exist for Virginia purposes.

## Section 4: Self-employed specific rules

### Self-employment tax deduction

- **Self-employment tax deduction flow-through** — The federal deduction for 50% of self-employment tax (Form 1040, Schedule 1, Line 15) reduces federal AGI. Since Virginia starts from federal AGI, this flows through automatically.  _(Form 1040, Schedule 1, Line 15)_

### Retirement contributions

- **Retirement contributions flow-through** — SEP-IRA, SIMPLE IRA, and solo 401(k) contributions that reduce federal AGI flow through to Virginia automatically.

### Health insurance deduction

- **Self-employed health insurance deduction flow-through** — The self-employed health insurance deduction (Schedule 1, Line 17) reduces federal AGI and flows through automatically.  _(Schedule 1, Line 17)_

### QBI deduction (§199A)

- **Virginia non-conformity to QBI deduction** — Virginia does NOT conform to the federal QBI deduction. The §199A deduction reduces federal taxable income (after AGI) but since Virginia starts from AGI, it is not part of the Virginia computation. Virginia taxable income will be higher than federal taxable income by the QBI amount (all else equal).  _(§199A)_

### Home office deduction

- **Home office deduction flow-through** — Reduces Schedule C net profit → reduces federal AGI → flows through to Virginia.

### Estimated tax payments

- **Estimated tax payment requirement** — Virginia requires estimated payments if the expected tax liability (after withholding and credits) will be $150 or more. Due dates: May 1, June 15, September 15, January 15. Note the first payment aligns with the May 1 filing deadline (not April 15).

## Section 5: Tier 1 rules — deterministic

- **[T1-VA-1] Tax computation** — Apply the graduated rate table to Virginia taxable income: - First $3,000 × 2% = $60 - Next $2,000 × 3% = $60 - Next $12,000 × 5% = $600 - Remainder × 5.75%  _(T1-VA-1)_
- **[T1-VA-2] Starting point** — Begin with federal adjusted gross income from Form 1040, Line 11. Enter on Form 760, Line 1.  _(T1-VA-2)_
- **[T1-VA-3] Virginia additions (Form 760, Line 2)** — Common additions for self-employed: - Interest income from other states' obligations (tax-exempt federally but not for VA) - Certain fixed-date conformity additions (Virginia does not automatically conform to all post-2021 IRC changes)  _(T1-VA-3)_
- **[T1-VA-4] Virginia subtractions (Form 760, Line 6)** — Common subtractions: - First $20,000 of military pay (if applicable) - Virginia lottery winnings up to $600 (already reported federally) - Age deduction: up to $12,000 per taxpayer age 65+ (subject to income limits — phases out above $50,000 single / $75,000 MFJ AFAGI)  _(T1-VA-4)_
- **[T1-VA-5] Deduction choice** — Virginia requires the same deduction method as federal: if you claimed federal standard deduction, you must claim Virginia standard deduction. If you itemized federally, you must itemize for Virginia (using Virginia Schedule A, which largely mirrors federal but excludes state/local income tax deduction).  _(T1-VA-5)_
- **[T1-VA-6] Filing due date** — May 1 following the tax year (NOT April 15). For TY 2025, the deadline is May 1, 2026. Extension is automatic for 6 months to November 1.  _(T1-VA-6)_
- **[T1-VA-7] Estimated tax payments** — Required if expected liability exceeds $150 after withholding and credits. Quarterly dates: May 1, June 15, September 15, January 15.  _(T1-VA-7)_
- **[T1-VA-8] Virginia Earned Income Credit** — 20% of the federal EIC amount, refundable, for TY 2025 and 2026 (Va. Code § 58.1-339.8; the earlier choice of a 20% nonrefundable or 15% refundable credit no longer applies for these years). Claimed on Schedule ADJ, Line 16b. BARRED if you or anyone on the return claims the age deduction (Va. Code § 58.1-322.02) or the additional exemption for age 65 or over or for blindness — claiming either one disqualifies the taxpayer from BOTH this credit and the Credit for Low-Income Individuals (2025 Form 760 instructions; https://www.tax.virginia.gov/low-income-individuals-credit). This credit and the Credit for Low-Income Individuals are also mutually exclusive: claim one, not both. Nonresidents and part-year residents may not claim the refundable version.  _(T1-VA-8)_

## Section 6: Tier 2 rules — requires judgment

- **[T2-VA-1] Residency determination** — Virginia defines a resident as a person domiciled in Virginia or who maintains a place of abode in Virginia and is present for 183+ days. "Domicile" requires intent to remain permanently or indefinitely. Freelancers who split time between states should document domicile carefully.  _(T2-VA-1)_
- **[T2-VA-2] Fixed-date conformity** — Virginia conforms to the Internal Revenue Code as of a specific date set by the General Assembly (currently December 31, 2022 for most provisions). Federal tax law changes after that date may require Virginia additions or subtractions. Reviewer should check current conformity date for the filing year.  _(T2-VA-2)_
- **[T2-VA-3] Multi-state credit** — Virginia provides a credit for income taxes paid to other states on income also taxed by Virginia (Schedule OSC). The credit cannot exceed Virginia tax on the income sourced to the other state.  _(T2-VA-3)_
- **[T2-VA-4] Standard deduction sunset** — The enhanced standard deduction ($8,750 single / $17,500 MFJ for 2026) is scheduled to revert to $3,000 / $6,000 after TY 2026 unless the General Assembly acts. Reviewer should monitor this for future-year planning.  _(T2-VA-4)_
- **[T2-VA-5] Business vs. hobby** — Virginia follows the federal §183 determination. If Schedule C activity is reclassified as hobby by IRS, Virginia follows.  _(T2-VA-5)_

## Section 7: Supplier pattern library

**Supplier pattern library**

| Income/deduction type | Virginia treatment | Notes |
| --- | --- | --- |
| Schedule C net profit | Included via federal AGI | No adjustment |
| Self-employment tax deduction | Included via federal AGI reduction | No adjustment |
| SEP/SIMPLE/solo 401(k) | Included via federal AGI reduction | No adjustment |
| QBI deduction (§199A) | NOT included — Virginia starts from AGI | VA taxable income is higher |
| Self-employed health insurance | Included via federal AGI reduction | No adjustment |
| Home office deduction | Included via Schedule C reduction | No adjustment |
| Social Security benefits | Partially/fully included (follows federal inclusion) | No VA subtraction for <65 |
| Out-of-state bond interest | Add to Virginia income | Not exempt for VA |
| Virginia bond interest | Subtract from Virginia income | Exempt |
| Federal tax refund | Not applicable (VA doesn't deduct federal tax) | N/A |

## Section 8: Form mapping

**Form 760 line mapping**

| Form 760 Line | Description | Source |
| --- | --- | --- |
| Line 1 | Federal adjusted gross income (FAGI) | Form 1040, Line 11 |
| Line 2 | Additions (Schedule ADJ, Section A) | Computed |
| Line 3 | Adjusted FAGI (Line 1 + Line 2) | Computed |
| Line 6 | Subtractions (Schedule ADJ, Section B) | Computed |
| Line 7 | Virginia AGI (Line 3 − Line 6) | Computed |
| Line 9 | Deductions (standard or itemized) | Per filing method |
| Line 10 | Exemptions ($930 × number) | Computed |
| Line 11 | Virginia taxable income (Line 7 − 9 − 10) | Computed |
| Line 12 | Tax (from rate table) | Computed per brackets |
| Line 17 | Tax after credits | Computed |
| Line 22+ | Payments (withholding, estimated) | W-2s, vouchers |

## Section 9: Refusal catalogue

**Refusal catalogue**

| ID | Refusal | Reason |
| --- | --- | --- |
| R-VA-1 | Part-year resident return (Form 760PY) | Different form and allocation rules |
| R-VA-2 | Nonresident return (Form 763) | Different form and sourcing rules |
| R-VA-3 | Virginia corporate income tax | Different tax type (Form 500) |
| R-VA-4 | BPOL (local business license tax) | Local tax, not state-administered |
| R-VA-5 | Virginia estate/trust return | Different form (Form 770) |
| R-VA-6 | Land preservation / historic rehabilitation credits | Specialized credit computation |
| R-VA-7 | Amended returns (Form 760C / 760F) | Requires additional procedures |
| R-VA-8 | Pass-through entity tax (PTET) election | For multi-owner entities only |

- **R-VA-1** — Part-year resident return (Form 760PY)  _(Different form and allocation rules)_
- **R-VA-2** — Nonresident return (Form 763)  _(Different form and sourcing rules)_
- **R-VA-3** — Virginia corporate income tax  _(Different tax type (Form 500))_
- **R-VA-4** — BPOL (local business license tax)  _(Local tax, not state-administered)_
- **R-VA-5** — Virginia estate/trust return  _(Different form (Form 770))_
- **R-VA-6** — Land preservation / historic rehabilitation credits  _(Specialized credit computation)_
- **R-VA-7** — Amended returns (Form 760C / 760F)  _(Requires additional procedures)_
- **R-VA-8** — Pass-through entity tax (PTET) election  _(For multi-owner entities only)_

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
