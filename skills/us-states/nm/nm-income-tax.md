---
name: nm-income-tax
description: Use this skill whenever asked about New Mexico individual income tax for self-employed / sole proprietors. Trigger on phrases like "New Mexico income tax", "NM income tax", "Form PIT-1", "NM Taxation and Revenue", "NM self-employment tax".
version: "0.1"
jurisdiction: US-NM
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NM Income Tax

## New Mexico Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers New Mexico Form PIT-1 (Personal Income Tax Return) for full-year NM residents who are sole proprietors or single-member LLC owners. Tax year 2025 (returns filed in 2026). New Mexico uses a six-bracket graduated rate structure ranging from 1.5% to 5.9%, restructured under HB 252 effective 2025.
>
> **Quality tier.** Q3 — AI-drafted, not independently verified. All outputs must be reviewed by a qualified tax professional before filing.

## Section 1: Metadata

**Metadata table**

| Field | Value |
| --- | --- |
| Tax type | Individual income tax (Personal Income Tax) |
| Jurisdiction | New Mexico (US-NM) |
| Tax year | 2025 (filed 2026) |
| Primary form | Form PIT-1 |
| Supporting schedules | Schedule PIT-B (Nonresident/Part-year), Schedule PIT-CR (Credits), Schedule PIT-ADJ (Adjustments) |
| Tax structure | Graduated (6 brackets) |
| Rate range | 1.5% – 5.9% |
| Filing deadline | April 15, 2026 |
| Extension deadline | October 15, 2026 (automatic with federal extension) |
| Tax authority | New Mexico Taxation and Revenue Department |
| Website | https://www.tax.newmexico.gov |
| Statute | N.M. Stat. Ann. §7-2-7 (Income Tax Act) |

**Sources:**
- NM Taxation and Revenue Department, Personal Income Tax: https://www.tax.newmexico.gov/individuals/personal-income-tax-information-overview/
- HB 252 (2024 omnibus tax bill — restructured brackets effective 2025)
- EY Tax News: "New Mexico governor signs omnibus tax bill" (2024-0722)
- N.M. Stat. Ann. §7-2-7 (rate schedule)

## Section 2: Quick reference — rates and thresholds

### Tax brackets — Single / Estates and trusts (TY 2025)

**Tax brackets — Single / Estates and trusts (TY 2025)**

| Taxable income over | But not over | Rate | Tax on lower amount |
| --- | --- | --- | --- |
| $0 | $5,500 | 1.5% | $0 |
| $5,500 | $16,500 | 3.2% | $82.50 |
| $16,500 | $33,500 | 4.3% | $434.50 |
| $33,500 | $66,500 | 4.7% | $1,165.50 |
| $66,500 | $210,000 | 4.9% | $2,716.50 |
| $210,000 | — | 5.9% | $9,748 |

### Tax brackets — Married filing jointly / Head of household / Qualifying surviving spouse (TY 2025)

**Tax brackets — MFJ / HOH / QSS (TY 2025)**

| Taxable income over | But not over | Rate | Tax on lower amount |
| --- | --- | --- | --- |
| $0 | $8,000 | 1.5% | $0 |
| $8,000 | $25,000 | 3.2% | $120 |
| $25,000 | $50,000 | 4.3% | $664 |
| $50,000 | $100,000 | 4.7% | $1,739 |
| $100,000 | $315,000 | 4.9% | $4,089 |
| $315,000 | — | 5.9% | $14,624 |

### Tax brackets — Married filing separately (TY 2025)

**Tax brackets — Married filing separately (TY 2025)**

| Taxable income over | But not over | Rate | Tax on lower amount |
| --- | --- | --- | --- |
| $0 | $4,000 | 1.5% | $0 |
| $4,000 | $12,500 | 3.2% | $60 |
| $12,500 | $25,000 | 4.3% | $332 |
| $25,000 | $50,000 | 4.7% | $869.50 |
| $50,000 | $157,500 | 4.9% | $2,044.50 |
| $157,500 | — | 5.9% | $7,312 |

### Standard deduction

New Mexico follows the **federal standard deduction** amounts (NM conforms to federal for this purpose).

**Standard deduction (TY 2025)**

| Filing status | Standard deduction (TY 2025) |
| --- | --- |
| Single | $15,000 (federal amount — verify) |
| Married filing jointly | $30,000 (federal amount — verify) |
| Head of household | $22,500 (federal amount — verify) |

### Low-and-middle-income exemption

- **Low-and-middle-income exemption** — New Mexico offers a low-and-middle-income exemption of up to $2,500 per qualified exemption, based on adjusted gross income. All taxpayers (residents, part-year residents, nonresidents) may claim this exemption.

### Local income tax

- **Local income tax** — New Mexico does not permit local income taxes.

## Section 3: How this skill works with the federal return

New Mexico taxable income starts with **federal adjusted gross income (FAGI)** from federal Form 1040, Line 11.

1. **Start with federal AGI** → PIT-1
2. **Add NM additions** — items NM adds back
3. **Subtract NM subtractions** — items NM excludes
4. **Subtract NM exemptions** (low-and-middle-income exemption, blind/aged exemptions)
5. **Subtract standard or itemized deductions** (NM follows federal amounts)
6. **Result = NM taxable income**
7. **Apply the graduated rate schedule** → NM tax
8. **Apply credits and rebates** (Schedule PIT-CR) → final tax due or refund

### Key addition modifications

**Key addition modifications**

| Addition | Description |
| --- | --- |
| Lump-sum distributions | Certain lump-sum distributions not included in federal AGI |
| NM income not in federal AGI | Income taxable by NM but excluded from federal return |

### Key subtraction modifications

**Key subtraction modifications**

| Subtraction | Description |
| --- | --- |
| US government bond interest | Interest from US Treasury obligations |
| Social Security | NM does not tax Social Security benefits |
| Military retirement pay | Exempt for certain qualifying individuals |
| Age 65+ income exemption | Up to $8,000 for 65+ with AGI under $51,000 (single) or $36,667 (MFJ per spouse) |

## Section 4: Self-employed specific rules

### Self-employment income flow

- **Self-employment income flow** — Schedule C net profit flows into federal AGI, which is the starting point for NM. NM follows the federal self-employment tax deduction (deductible half of SE tax) through federal AGI.

### Estimated tax

- **Estimated tax threshold** — NM requires estimated tax payments if you expect to owe $1,000 or more after subtracting withholding and credits.

**Estimated tax installment due dates**

| Installment | Due date |
| --- | --- |
| 1st quarter | April 15 |
| 2nd quarter | June 15 |
| 3rd quarter | September 15 |
| 4th quarter | January 15 (following year) |

Form PIT-ES is used for estimated tax payments.

### Gross Receipts Tax (GRT) interaction

- **GRT interaction** — Self-employed taxpayers in NM are also subject to the Gross Receipts Tax (GRT), which is NM's equivalent of a sales/use tax but is imposed on the seller's gross receipts. Unlike a traditional sales tax, the GRT is imposed on the business (not the buyer), though it is commonly passed through to customers. - GRT applies to most services as well as goods (unlike most state sales taxes). - Rates vary by location (combined state + local: approximately 5.0% to 9.4375%). - Self-employed service providers must register for and collect/remit GRT. - GRT paid is deductible as a business expense on the federal Schedule C.

### Working Families Tax Credit (NM EIC)

- **NM Working Families Tax Credit** — NM offers a refundable earned income credit equal to 25% of the federal Earned Income Credit (EIC) for TY 2025. This is particularly valuable for lower-income self-employed taxpayers.

## Section 5: Tier 1 rules — deterministic

- **NM-T1-01** — NM taxable income = federal AGI ± NM modifications − exemptions − deductions  _(N.M. Stat. Ann. §7-2-2)_
- **NM-T1-02** — Tax computed using 6-bracket schedule: 1.5%–5.9% (TY 2025)  _(N.M. Stat. Ann. §7-2-7; HB 252)_
- **NM-T1-03** — Starting point is federal AGI (Form 1040, Line 11)  _(N.M. Stat. Ann. §7-2-2)_
- **NM-T1-04** — Social Security benefits fully exempt  _(N.M. Stat. Ann. §7-2-2(S))_
- **NM-T1-05** — Low-and-middle-income exemption: up to $2,500 per qualified exemption  _(N.M. Stat. Ann. §7-2-5.6)_
- **NM-T1-06** — NM Working Families Tax Credit = 25% of federal EIC (refundable)  _(N.M. Stat. Ann. §7-2-18.16)_
- **NM-T1-07** — Estimated tax required if expected liability ≥ $1,000  _(N.M. Stat. Ann. §7-2-12.2)_
- **NM-T1-08** — NM follows federal standard deduction amounts  _(N.M. Stat. Ann. §7-2-2)_

## Section 6: Tier 2 rules — requires judgment

- **NM-T2-01** — Multi-state income: Taxpayer has income from another state  _(NM taxes worldwide income of residents. Credit for taxes paid to other states available on Schedule PIT-CR.)_
- **NM-T2-02** — GRT vs. income tax interaction  _(GRT is a separate tax on gross receipts, not a credit against income tax. GRT paid is deductible as a business expense on federal Schedule C, which flows through to NM.)_
- **NM-T2-03** — Technology jobs tax credit  _(NM offers credits for qualifying technology businesses. Requires certification.)_
- **NM-T2-04** — Angel investment credit  _(NM allows credits for qualified investments in NM small businesses. Requires approval from NM Economic Development Department.)_
- **NM-T2-05** — Federal IRC conformity  _(NM's conformity with the IRC should be verified for recent federal changes. NM generally has rolling conformity but may decouple from specific provisions.)_
- **NM-T2-06** — Community property  _(New Mexico IS a community property state. MFS returns require community property income allocation.)_

## Section 7: Supplier pattern library

**Supplier pattern library**

| Input needed | Where to find it |
| --- | --- |
| Federal AGI | Federal Form 1040, Line 11 |
| NM additions | PIT-1 / Schedule PIT-ADJ |
| NM subtractions | PIT-1 / Schedule PIT-ADJ |
| Standard/itemized deduction | Federal amounts (NM conforms) |
| Low-and-middle-income exemption | Based on AGI and number of exemptions |
| Tax credits and rebates | Schedule PIT-CR |
| Estimated tax payments | PIT-ES records |
| NM withholding | W-2 Box 17 / 1099 NM withholding amounts |
| Federal EIC amount | Federal Schedule EIC / Form 1040 (for NM WFTC calculation) |

## Section 8: Form mapping

**Form PIT-1 line mapping**

| Form PIT-1 Line | Description | Source |
| --- | --- | --- |
| Line 7 | Federal adjusted gross income | Federal 1040, Line 11 |
| Line 8 | NM additions | Schedule PIT-ADJ |
| Line 10 | NM subtractions | Schedule PIT-ADJ |
| Line 13 | NM exemptions (low-and-middle-income, blind, aged) | Computed |
| Line 15 | Standard or itemized deduction | Federal amount |
| Line 17 | NM taxable income | Computed |
| Line 18 | NM income tax | From rate schedule |
| Line 21 | Credits and rebates | Schedule PIT-CR |
| Line 25 | NM withholding | W-2s / 1099s |
| Line 26 | Estimated tax payments | PIT-ES payments |
| Line 31 | Amount owed or refund | Computed |

## Section 9: Refusal catalogue

- **R-NM-01** — Part-year or nonresident  _("NM part-year and nonresident returns require Schedule PIT-B. This is outside the scope of this skill.")_
- **R-NM-02** — Corporate return  _("This skill covers personal income tax only (Form PIT-1). Corporate income tax (CIT) is not covered.")_
- **R-NM-03** — Fiduciary return  _("NM fiduciary returns (Form FID-1) are not covered by this skill.")_
- **R-NM-04** — Amended return  _("NM amended returns (amended PIT-1) are not covered.")_
- **R-NM-05** — GRT computation  _("NM Gross Receipts Tax is a separate tax. See nm-sales-tax.md for GRT details.")_
- **R-NM-06** — Oil and gas taxation  _("NM oil, gas, and mineral taxation (severance taxes, conservation taxes) requires specialist review.")_

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
