---
name: mt-income-tax
description: Use this skill whenever asked about Montana individual income tax for self-employed persons, sole proprietors, or single-member LLCs. Trigger on phrases like "Montana income tax", "MT income tax", "Form 2", "Montana DOR", "MCA 15-30-2103".
version: "0.1"
jurisdiction: US-MT
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MT Income Tax

## Montana Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers Montana Form 2 for full-year Montana residents
> who are sole proprietors or single-member LLC owners. Montana uses a
> two-bracket graduated income tax: 4.7% on lower income and 5.65% on
> higher income (TY 2026, per HB 337). Montana has NO general sales tax.
> Montana also applies separate, lower rates to net long-term capital gains.
>
> **Quality tier.** Q3 — AI-drafted, not independently verified. All rates and
> thresholds were researched on 2026-05-22 from official Montana Department
> of Revenue publications. A qualified professional must review before filing.

## Section 1: Metadata

**Section 1 metadata table**

| Field | Value |
| --- | --- |
| Jurisdiction | Montana (US-MT) |
| Tax type | Individual income tax |
| Primary form | Form 2 (Montana Individual Income Tax Return) |
| Tax year | 2025 (filed in 2026) / 2026 |
| Authority | Montana Department of Revenue |
| Statute | MCA 15-30-2103 et seq. |
| Version | 0.1 |
| Last updated | 2026-05-22 |
| Validation | AI-drafted — Q3 |

### Sources consulted

**Sources consulted**

| # | Source | URL |
| --- | --- | --- |
| 1 | Montana DOR — HB337: 2026–2027 Income Tax Changes | https://revenue.mt.gov/news/recent-news/HB-337 |
| 2 | Montana Income Tax Rates (TY 2025) | https://remotelaws.com/state-income-tax/us-states/montana/ |
| 3 | PolicyEngine — Montana Reduces Top Rate (HB337 analysis) | https://www.policyengine.org/us/research/montana-tax-cuts-2026 |
| 4 | MCA 15-30-2103 (rate statute) | https://leg.mt.gov/bills/mca/title_0150/chapter_0300/part_0210/section_0030/0150-0300-0210-0030.html |

## Section 2: Quick reference — rates and thresholds

### Ordinary income tax rates — TY 2025 (filed in 2026)

**Ordinary income tax rates — TY 2025 (filed in 2026)**

| Filing status | Lower bracket (4.7%) | Upper bracket (5.9%) |
| --- | --- | --- |
| Single / MFS | $0 – $21,100 | Over $21,100 |
| Head of Household | $0 – $31,700 | Over $31,700 |
| MFJ / Surviving Spouse | $0 – $42,200 | Over $42,200 |

### Ordinary income tax rates — TY 2026 (per HB 337)

**Ordinary income tax rates — TY 2026 (per HB 337)**

| Filing status | Lower bracket (4.7%) | Upper bracket (5.65%) |
| --- | --- | --- |
| Single / MFS | $0 – $47,500 | Over $47,500 |
| Head of Household | $0 – $71,250 | Over $71,250 |
| MFJ / Surviving Spouse | $0 – $95,000 | Over $95,000 |

### Net long-term capital gains rates

**Net long-term capital gains rates**

| Capital gains income | Rate |
| --- | --- |
| Within the lower bracket (after subtracting ordinary income) | 3.0% |
| Above the lower bracket threshold | 4.1% |

### Standard deduction

Montana uses the **federal standard deduction** amount. For TY 2025:

**Standard deduction table**

| Filing status | Amount |
| --- | --- |
| Single | $15,000 |
| MFJ / Surviving Spouse | $30,000 |
| Head of Household | $22,500 |
| MFS | $15,000 |

- **Personal exemption elimination** — Montana eliminated the personal exemption effective TY 2024.

### Other deductions / subtractions

**Other deductions / subtractions table**

| Item | Amount | Source |
| --- | --- | --- |
| Age 65+ subtraction | $5,660 from federal taxable income (TY 2025) | MCA 15-30-2110 |
| Medical savings account deduction | Up to $4,600 | MCA 15-61-202 |

### Key thresholds

**Key thresholds table**

| Item | Value | Source |
| --- | --- | --- |
| Filing deadline | April 15, 2026 (for TY 2025) | MCA 15-30-2604 |
| Extension | Automatic 6-month with federal extension | MCA 15-30-2604 |
| Estimated tax threshold | $500 expected liability after withholding and credits | MCA 15-30-2512 |
| No sales tax | Montana does not impose a general sales tax | — |

### Earned Income Tax Credit — TY 2026+

- **Montana EITC** — 20% of federal Earned Income Credit (refundable) (Doubled from 10% by HB 337, effective TY 2026.)  _(HB 337)_

## Section 3: How this skill works with the federal return

Montana taxable income begins with **federal taxable income** from federal Form 1040, Line 15 (after the federal standard or itemized deduction).

1. **Additions** — Add back items Montana does not exclude (limited; Montana closely conforms to federal definitions).
2. **Subtractions** — Subtract items Montana excludes:
   - Interest on U.S. government obligations
   - Montana state income tax refund included in federal taxable income
   - Age 65+ subtraction ($5,660 for TY 2025)
   - Qualified medical savings account contributions
3. **Montana taxable income** — Federal taxable income + additions − subtractions.
4. **Separate capital gains** — Net long-term capital gains are taxed at preferential Montana rates (3.0% / 4.1%) rather than the ordinary rates.
5. **Tax** — Apply the two-bracket rates to ordinary income, and the capital gains rates to qualifying gains.
6. **Credits** — Apply applicable credits (EITC, elderly homeowner/renter credit, etc.).

## Section 4: Self-employed specific rules

1. **Self-employment income** flows through federal Schedule C → federal AGI → federal taxable income → Montana taxable income. No separate Montana schedule for self-employment income.
2. **Federal SE tax deduction** — Already reflected in federal AGI/taxable income. No separate Montana adjustment.
3. **Estimated taxes** — Self-employed taxpayers must make quarterly estimated payments (Form ESA) if expected liability exceeds $500 after withholding and credits. Due dates: April 15, June 15, September 15, January 15.
4. **Business equipment depreciation** — Montana generally conforms to federal depreciation, including IRC § 179. Montana conforms to bonus depreciation (IRC § 168(k)).
5. **Capital gains from business asset sales** — Net long-term capital gains (including from business asset dispositions) qualify for the preferential 3.0%/4.1% Montana rates. Short-term gains are taxed as ordinary income.
6. **Health insurance deduction** — Self-employed health insurance deduction is in federal AGI/taxable income. No Montana add-back.
7. **No sales tax** — Montana has no general sales tax, which means sole proprietors do not need to collect or remit sales tax on goods sold in Montana (some resort areas impose a local resort tax on specific goods/services).
8. **Montana EITC** — 20% of federal EITC (TY 2026+), refundable. Available to qualifying self-employed filers.

## Section 5: Tier 1 rules — deterministic

**Tier 1 rules — deterministic table**

| Rule ID | Rule | Source |
| --- | --- | --- |
| MT-T1-01 | Start with federal taxable income (Form 1040, Line 15) | MCA 15-30-2101 |
| MT-T1-02 | Subtract interest on U.S. government obligations | MCA 15-30-2110 |
| MT-T1-03 | Subtract state income tax refund included in federal income | MCA 15-30-2110 |
| MT-T1-04 | Age 65+ subtraction: $5,660 from federal taxable income (TY 2025) | MCA 15-30-2110 |
| MT-T1-05 | Apply ordinary rates: 4.7% / 5.9% (TY 2025) or 4.7% / 5.65% (TY 2026) | MCA 15-30-2103, HB 337 |
| MT-T1-06 | Net long-term capital gains: 3.0% on gains within the lower bracket; 4.1% on gains above | MCA 15-30-2103 |
| MT-T1-07 | Montana EITC: 20% of federal EIC (refundable, TY 2026+) | HB 337 |
| MT-T1-08 | Personal exemption: eliminated effective TY 2024 | MCA 15-30-2114 |
| MT-T1-09 | Standard deduction: uses federal standard deduction amount | MCA 15-30-2101 |
| MT-T1-10 | No general sales tax in Montana | — |

## Section 6: Tier 2 rules — requires judgment

**Tier 2 rules — requires judgment table**

| Rule ID | Rule | Guidance |
| --- | --- | --- |
| MT-T2-01 | **Residency determination** — Montana uses a domicile test. A person domiciled in Montana or spending 180+ days in the state is presumed a resident. | If taxpayer has homes in multiple states, flag for professional review. |
| MT-T2-02 | **Capital gains classification** — Determine which gains are long-term (held > 1 year) vs. short-term. Only net long-term gains qualify for the 3.0%/4.1% preferential rates. | Review holding periods for all disposed assets. |
| MT-T2-03 | **Capital gains bracket interaction** — The 3.0% rate applies to capital gains that fall within the lower ordinary-income bracket (after subtracting Montana ordinary income from the threshold). | If ordinary income exceeds the lower bracket, all capital gains are taxed at 4.1%. |
| MT-T2-04 | **Elderly homeowner/renter credit** — Available to Montana residents age 62+ with household income below thresholds. | Income-based calculation; flag for review if taxpayer qualifies. |
| MT-T2-05 | **Credit for taxes paid to other states** — Non-refundable credit to prevent double taxation. | Requires the other state's return. |
| MT-T2-06 | **Resort tax** — Some Montana resort areas impose a local resort tax (up to 3%) on certain goods and services. Not an income tax, but self-employed persons in resort areas may need to collect it. | Flag if taxpayer operates in a resort community. |

## Section 7: Supplier pattern library

**Supplier pattern library table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| W-2 wages from Montana employer | MT withholding applies; include on Form 2 | Most common |
| Schedule C net profit (sole prop) | Flows through federal taxable income → Montana taxable income | No separate MT schedule |
| Rental income (Schedule E) | Included in federal taxable income → Montana taxable income | MT-source if property in MT |
| Interest on U.S. government bonds | Subtract from Montana taxable income | MCA 15-30-2110 |
| Social Security benefits | Only the amount included in federal taxable income flows through; Montana does not add back | — |
| Long-term capital gains | Preferential MT rates: 3.0% / 4.1% | Separate from ordinary income |
| Short-term capital gains | Taxed as ordinary income (4.7% / 5.65%) | No preferential rate |
| 1099-NEC freelance income | Flows through Schedule C → federal taxable income | Estimated payments likely needed |

## Section 8: Form mapping

**Form mapping table**

| Montana form / schedule | What it covers | Federal counterpart |
| --- | --- | --- |
| Form 2 | Montana Individual Income Tax Return | Form 1040 |
| Schedule I (Form 2) | Additions and Subtractions to Federal Taxable Income | Schedule 1 (Form 1040) |
| Schedule II (Form 2) | Tax Computation (ordinary + capital gains) | N/A |
| Schedule III (Form 2) | Credits | N/A |
| Schedule IV (Form 2) | Non-resident / Part-year Allocation | N/A |
| Form ESA | Estimated Tax Payment Voucher | Form 1040-ES |
| Form EITC | Montana Earned Income Tax Credit | Schedule EIC |

## Section 9: Refusal catalogue

**Refusal catalogue table**

| ID | Situation | Action |
| --- | --- | --- |
| MT-R-01 | Part-year or non-resident return (Schedule IV) | Refuse — out of scope |
| MT-R-02 | Corporate income tax (Form CIT) | Refuse — out of scope |
| MT-R-03 | Partnership / S-corp pass-through returns | Refuse — out of scope |
| MT-R-04 | Multi-state income apportionment | Refuse — flag for professional review |
| MT-R-05 | Amended returns | Refuse — out of scope |
| MT-R-06 | Tax year other than 2025 or 2026 | Refuse — rates and thresholds may differ |
| MT-R-07 | Resort tax / local accommodation tax | Refuse — separate local tax; out of scope |

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
