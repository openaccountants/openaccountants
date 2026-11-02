---
name: vt-income-tax
description: Use this skill whenever asked about Vermont individual income tax, Vermont Form IN-111, Vermont graduated tax rates, Vermont self-employment income tax at the state level, Vermont earned income tax credit, or any Vermont personal income tax question for sole proprietors. Trigger on phrases like "Vermont income tax", "VT income tax", "Form IN-111", "Vermont tax brackets", "Vermont 8.75%", "32 V.S.A. Chapter 151", or any request involving Vermont state individual income tax computation or filing.
version: "0.1"
jurisdiction: US-VT
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# VT Income Tax

## Vermont Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers the Vermont individual income tax return (Form IN-111) for full-year Vermont residents who are sole proprietors or single-member LLC owners. It addresses the graduated rate computation, Vermont taxable income derived from federal taxable income, and Vermont-specific credits.

> **Quality tier.** Q3 — AI-drafted, not independently verified. All rates and rules are sourced from the Vermont Department of Taxes publications and third-party research current as of May 2026. A licensed CPA or EA should verify before relying on this skill for filing.

## Section 1: Metadata

**Metadata table**

| Field | Value |
| --- | --- |
| Jurisdiction | Vermont, United States |
| Jurisdiction code | US-VT |
| Tax type | Individual income tax |
| Rate structure | Graduated (4 brackets) |
| Rate range | 3.35% – 8.75% |
| Primary form | Form IN-111 (Vermont Income Tax Return) |
| Governing statute | 32 V.S.A. Chapter 151 (§5822 et seq.) |
| Tax authority | Vermont Department of Taxes |
| Filing portal | https://tax.vermont.gov |
| Tax year covered | 2025 (filed 2026) and 2026 (filed 2027) |
| Last updated | May 22, 2026 |

### Sources

**Sources table**

| # | Source | URL |
| --- | --- | --- |
| 1 | Vermont Department of Taxes — Rate Schedules | https://tax.vermont.gov/individuals/personal-income-tax/rates |
| 2 | 32 V.S.A. §5822 — Tax rates | https://legislature.vermont.gov/statutes/section/32/151/05822 |
| 3 | 2025 Form IN-111 Instructions | https://tax.vermont.gov/all-forms |
| 4 | Tax Foundation — Vermont profile | https://taxfoundation.org/location/vermont/ |

## Section 2: Quick reference — rates and thresholds

### Tax brackets — Single filers (2025 and 2026)

**Single filer brackets**

| Taxable income bracket | Marginal rate |
| --- | --- |
| $0 – $47,900 | 3.35% |
| $47,901 – $116,000 | 6.60% |
| $116,001 – $242,000 | 7.60% |
| $242,001 and above | 8.75% |

### Tax brackets — Married filing jointly (2025 and 2026)

**MFJ brackets**

| Taxable income bracket | Marginal rate |
| --- | --- |
| $0 – $79,950 | 3.35% |
| $79,951 – $193,300 | 6.60% |
| $193,301 – $294,600 | 7.60% |
| $294,601 and above | 8.75% |

### Tax brackets — Married filing separately (2025 and 2026)

**MFS brackets**

| Taxable income bracket | Marginal rate |
| --- | --- |
| $0 – $39,975 | 3.35% |
| $39,976 – $96,650 | 6.60% |
| $96,651 – $147,300 | 7.60% |
| $147,301 and above | 8.75% |

### Tax brackets — Head of household (2025 and 2026)

**HOH brackets**

| Taxable income bracket | Marginal rate |
| --- | --- |
| $0 – $64,200 | 3.35% |
| $64,201 – $165,700 | 6.60% |
| $165,701 – $268,300 | 7.60% |
| $268,301 and above | 8.75% |

### Key thresholds

**Key thresholds table**

| Item | Amount | Source |
| --- | --- | --- |
| Standard deduction | Uses federal amounts | 32 V.S.A. §5811(21) |
| Personal exemption | Uses federal amounts (pre-TCJA equivalent via VT credit) | 32 V.S.A. §5822 |
| Filing deadline | April 15 | 32 V.S.A. §5848 |
| Extension | October 15 (automatic with federal) | 32 V.S.A. §5848 |
| Estimated tax threshold | $500 expected liability | 32 V.S.A. §5851 |
| VT Earned Income Credit | 38% of federal EIC (refundable) | 32 V.S.A. §5828b |
| VT Child and Dependent Care Credit | 72% of federal credit (for AGI ≤$30,000) | 32 V.S.A. §5828c |
| State sales tax rate | 6% | 32 V.S.A. §9771 |

## Section 3: How this skill works with the federal return

Vermont starts from **federal taxable income** (Form 1040, Line 15). This is AFTER the federal standard deduction (or itemized deductions) and the QBI deduction.

**Flow:**
1. Federal Form 1040 is completed (including Schedule C, SE, and all deductions).
2. Federal taxable income (Line 15) flows to Vermont Form IN-111, Line 1.
3. Vermont additions are applied (Form IN-112) — rare for most sole proprietors.
4. Vermont subtractions are applied (Form IN-113) — e.g., interest from US obligations.
5. Vermont taxable income is computed.
6. Vermont tax is computed using the rate schedule for the filing status.
7. Credits (earned income credit, renter credit, etc.) are applied.

**Key structural point:** Because Vermont starts from federal taxable income, both the federal standard deduction AND the QBI deduction are already subtracted. Vermont does not apply its own standard deduction — it piggybacks on the federal amount.

## Section 4: Self-employed specific rules

### Self-employment tax deduction

- **Self-employment tax deduction** — The federal deduction for 50% of self-employment tax reduces federal AGI → reduces federal taxable income → flows through to Vermont automatically.

### Retirement contributions

- **Retirement contributions** — SEP-IRA, SIMPLE IRA, solo 401(k) contributions reduce federal AGI → flow through automatically.

### Health insurance deduction

- **Health insurance deduction** — The self-employed health insurance deduction reduces federal AGI → flows through automatically.

### QBI deduction (§199A)

- **QBI deduction (§199A)** — Vermont conforms — the QBI deduction is included in federal taxable income (it reduces FTI), so it benefits the Vermont computation. No add-back.

### Home office deduction

- **Home office deduction** — Reduces Schedule C net profit → reduces federal AGI → reduces federal taxable income → flows through.

### Estimated tax payments

- **Estimated tax payments** — Vermont requires estimated payments if expected tax liability (after credits and withholding) exceeds $500. Due dates follow federal: April 15, June 15, September 15, January 15.

## Section 5: Tier 1 rules — deterministic

- **[T1-VT-1] Tax computation** — Apply the graduated rate schedule to Vermont taxable income based on filing status. Use the Vermont rate schedules or tax tables published annually by the Department of Taxes.
- **[T1-VT-2] Starting point** — Begin with federal taxable income from Form 1040, Line 15. Enter on Form IN-111, Line 1.
- **[T1-VT-3] Vermont additions (Form IN-112)** — Common additions: - State and local bond interest from non-Vermont issuers (if excluded federally — rare since most muni interest is excluded from federal AGI, not TI) - Capital gains exclusion recapture (Vermont does not conform to certain federal exclusions) - IRC §168(k) bonus depreciation add-back (Vermont decoupled — requires add-back and substitution of VT depreciation)
- **[T1-VT-4] Vermont subtractions (Form IN-113)** — Common subtractions: - Interest from US government obligations (Treasury bonds, savings bonds) - Vermont depreciation allowance (replacement for disallowed federal bonus depreciation) - 40% capital gains exclusion on qualifying Vermont assets held 3+ years (32 V.S.A. §5811(21))  _(32 V.S.A. §5811(21))_
- **[T1-VT-5] Vermont Earned Income Credit** — 38% of the federal Earned Income Credit (fully refundable). Claimed on IN-111. If the taxpayer qualifies for federal EIC, they automatically qualify for VT EIC.
- **[T1-VT-6] Filing due date** — April 15 following the tax year (April 15, 2026 for TY 2025). Extension: October 15 (automatic with federal, no separate VT form needed). Payment is still due by April 15.
- **[T1-VT-7] Estimated tax payments** — Required if expected VT tax liability after withholding and credits exceeds $500. Quarterly due dates: April 15, June 15, September 15, January 15. Form IN-114 (voucher).
- **[T1-VT-8] Use tax reporting** — Form IN-111 includes a line for reporting use tax on out-of-state purchases. Self-employed individuals who purchase equipment/supplies online without VT sales tax should report use tax here.

## Section 6: Tier 2 rules — requires judgment

- **[T2-VT-1] Residency determination** — Vermont defines a resident as a person domiciled in Vermont or maintaining a permanent home in Vermont and spending 183+ days there. Domicile requires intent analysis. Freelancers splitting time between VT and another state need careful documentation.
- **[T2-VT-2] Bonus depreciation add-back** — Vermont requires add-back of federal §168(k) bonus depreciation and substitutes its own depreciation schedule. This creates timing differences. Reviewer must track the Vermont depreciation schedule separately and ensure proper subtraction in subsequent years.
- **[T2-VT-3] Capital gains exclusion** — Vermont allows a 40% exclusion on net long-term capital gains from the sale of qualifying Vermont-connected assets held for 3+ years. The asset must be a business, farm, or rental property located in Vermont, or an interest in certain Vermont businesses. Reviewer must verify the asset qualifies.
- **[T2-VT-4] Multi-state credit** — Vermont allows a credit for income taxes paid to other states/jurisdictions. The credit is the lesser of: (a) tax paid to the other state, or (b) Vermont tax attributable to the income taxed by the other state. Requires careful allocation for multi-state freelancers.
- **[T2-VT-5] Renter credit / property tax credit** — Vermont offers a property tax credit (via HS-122) and renter credit for eligible residents. Income limits and homestead value limits apply. These interact with overall VT tax liability.

## Section 7: Supplier pattern library

**Supplier pattern library table**

| Income/deduction type | Vermont treatment | Notes |
| --- | --- | --- |
| Schedule C net profit | Included via federal taxable income | No adjustment |
| Self-employment tax deduction | Included via federal AGI → FTI reduction | No adjustment |
| SEP/SIMPLE/solo 401(k) | Included via federal AGI → FTI reduction | No adjustment |
| QBI deduction (§199A) | Included via federal taxable income | Vermont conforms |
| Self-employed health insurance | Included via federal AGI → FTI reduction | No adjustment |
| Home office deduction | Included via Schedule C → FTI reduction | No adjustment |
| Federal bonus depreciation (§168(k)) | Add back, substitute VT depreciation | Timing difference |
| US government bond interest | Subtract | Exempt from state tax |
| Out-of-state municipal bond interest | Generally no adjustment (already excluded from federal AGI) | Confirm per situation |
| VT capital gains (qualifying assets, 3+ yr) | 40% exclusion available | Must verify qualification |

## Section 8: Form mapping

**Form mapping table**

| IN-111 Line | Description | Source |
| --- | --- | --- |
| Line 1 | Federal taxable income | Form 1040, Line 15 |
| Line 2 | Vermont additions (from IN-112) | Computed |
| Line 3 | Vermont subtractions (from IN-113) | Computed |
| Line 4 | Vermont taxable income (Line 1 + 2 − 3) | Computed |
| Line 5 | Vermont income tax (from rate schedule/table) | Per brackets |
| Line 7 | Vermont earned income credit (38% of federal EIC) | Computed |
| Line 8 | Other credits | Various |
| Line 9 | Net Vermont tax | Computed |
| Line 14+ | Payments (withholding, estimated, extension) | W-2s, IN-114 |
| Line 18 | Use tax | Self-reported |

## Section 9: Refusal catalogue

**Refusal catalogue table**

| ID | Refusal | Reason |
| --- | --- | --- |
| R-VT-1 | Part-year resident return | Requires allocation computation |
| R-VT-2 | Nonresident return (Form IN-111, Schedule IN-119) | Different sourcing rules |
| R-VT-3 | Vermont corporate income tax (Form CO-411) | Different tax type |
| R-VT-4 | Vermont estate tax | Different form and threshold analysis |
| R-VT-5 | Vermont meals and rooms tax | Separate tax system (9%) |
| R-VT-6 | Homestead declaration / property tax credit | Requires property valuation analysis |
| R-VT-7 | Amended returns | Requires additional procedures |
| R-VT-8 | Farm income averaging | Specialized computation |

- **R-VT-1** — Part-year resident return  _(Requires allocation computation)_
- **R-VT-2** — Nonresident return (Form IN-111, Schedule IN-119)  _(Different sourcing rules)_
- **R-VT-3** — Vermont corporate income tax (Form CO-411)  _(Different tax type)_
- **R-VT-4** — Vermont estate tax  _(Different form and threshold analysis)_
- **R-VT-5** — Vermont meals and rooms tax  _(Separate tax system (9%))_
- **R-VT-6** — Homestead declaration / property tax credit  _(Requires property valuation analysis)_
- **R-VT-7** — Amended returns  _(Requires additional procedures)_
- **R-VT-8** — Farm income averaging  _(Specialized computation)_

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
