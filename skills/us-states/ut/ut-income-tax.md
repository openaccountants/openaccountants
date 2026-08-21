---
name: ut-income-tax
description: Use this skill whenever asked about Utah individual income tax, Utah Form TC-40, Utah flat tax rate, Utah taxpayer tax credit, Utah self-employment tax at the state level, or any Utah personal income tax question for sole proprietors. Trigger on phrases like "Utah income tax", "UT income tax", "Form TC-40", "Utah flat tax", "Utah taxpayer tax credit", "Utah 4.45%", or any request involving Utah state individual income tax computation or filing.
version: "0.1"
jurisdiction: US-UT
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UT Income Tax

## Utah Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers the Utah individual income tax return (Form TC-40) for full-year Utah residents who are sole proprietors or single-member LLC owners. It addresses the flat rate computation, the taxpayer tax credit, and Utah-specific adjustments starting from federal taxable income.

> **Quality tier.** Q3 — AI-drafted, not independently verified. All rates and rules are sourced from official Utah State Tax Commission publications and third-party research current as of May 2026. A licensed CPA or EA should verify before relying on this skill for filing.

## Section 1: Metadata

**Metadata table**

| Field | Value |
| --- | --- |
| Jurisdiction | Utah, United States |
| Jurisdiction code | US-UT |
| Tax type | Individual income tax |
| Rate structure | Flat rate |
| Current rate (2026) | 4.45% |
| Primary form | TC-40 (Individual Income Tax Return) |
| Governing statute | Utah Code §59-10 |
| Tax authority | Utah State Tax Commission (USTC) |
| Filing portal | https://incometax.utah.gov |
| Tax year covered | 2025 (filed 2026) and 2026 (filed 2027) |
| Last updated | May 22, 2026 |

### Sources

**Sources table**

| # | Source | URL |
| --- | --- | --- |
| 1 | Utah State Tax Commission — Tax Rates | https://incometax.utah.gov/paying/tax-rates |
| 2 | Utah Code Title 59, Chapter 10 — Individual Income Tax | https://le.utah.gov/xcode/Title59/Chapter10/59-10.html |
| 3 | Tax Foundation — 2026 Utah Tax Profile | https://taxfoundation.org/location/utah/ |
| 4 | TC-40 Instructions (2025 tax year) | https://incometax.utah.gov/forms |

## Section 2: Quick reference — rates and thresholds

### Tax rate history

**Tax rate history**

| Tax year | Rate |
| --- | --- |
| 2026 | 4.45% |
| 2025 | 4.50% |
| 2024 | 4.55% |
| 2023 | 4.65% |
| 2022 | 4.85% |

### Key amounts (2025 tax year, filed 2026)

**Key amounts (2025 tax year, filed 2026)**

| Item | Amount | Source |
| --- | --- | --- |
| Flat income tax rate | 4.50% | Utah Code §59-10-104 |
| Taxpayer tax credit — single/HoH | $966 per taxpayer | TC-40 instructions |
| Taxpayer tax credit — MFJ | $1,932 ($966 × 2) | TC-40 instructions |
| Dependent exemption (per dependent) | $2,111 | TC-40 instructions |
| Credit phase-out — begins at MAGI | $16,464 (single), $32,928 (MFJ) | TC-40 instructions |
| Credit phase-out rate | 1.3% of MAGI exceeding threshold | TC-40 instructions |
| State sales tax rate (for reference) | 6.10% (includes mandatory 1.25% local) | Utah Code §59-12 |

### Key amounts (2026 tax year, filed 2027)

**Key amounts (2026 tax year, filed 2027)**

| Item | Amount | Source |
| --- | --- | --- |
| Flat income tax rate | 4.45% | Senate Bill 60 (2026 session) |
| Taxpayer tax credit | TBD — indexed annually | Pending USTC publication |

## Section 3: How this skill works with the federal return

- **Utah starting point** — Utah starts from federal taxable income (Form 1040, Line 15) — NOT federal AGI. The federal standard deduction or itemized deductions are already subtracted. The QBI deduction (§199A) is already subtracted. Self-employment income from Schedule C is included via AGI.  _(Section 3)_
- **Flow** — 1. Federal Form 1040 is completed (including Schedule C, SE, and all federal deductions). 2. Federal taxable income flows to Utah TC-40, Line 1. 3. Utah additions and subtractions are applied (Lines 2–8). 4. Utah income is multiplied by the flat rate (Line 9 × rate = Line 10). 5. Credits (taxpayer tax credit, others) are applied to reduce tax.  _(Section 3)_

## Section 4: Self-employed specific rules

### Self-employment tax deduction

- **Self-employment tax deduction** — The federal deduction for 50% of self-employment tax (Form 1040, Schedule 1, Line 15) reduces federal AGI, which flows through to federal taxable income. Utah benefits from this automatically since it starts from federal taxable income.  _(Section 4)_

### Retirement contributions

- **Retirement contributions** — Contributions to SEP-IRA, SIMPLE IRA, or solo 401(k) that reduce federal AGI flow through automatically. Utah does not add back these deductions.  _(Section 4)_

### Health insurance deduction

- **Health insurance deduction** — The self-employed health insurance deduction (Form 1040, Schedule 1, Line 17) reduces federal AGI and flows through to Utah automatically.  _(Section 4)_

### Home office deduction

- **Home office deduction** — The home office deduction reduces Schedule C net profit, which reduces federal AGI. No separate Utah adjustment needed.  _(Section 4)_

### Utah-specific: no SE tax at state level

- **No SE tax at state level** — Utah does not impose a separate self-employment tax. The only state-level obligation is income tax at the flat rate on Utah taxable income.  _(Section 4)_

## Section 5: Tier 1 rules — deterministic

- **[T1-UT-1] Tax computation** — Multiply Utah state taxable income (TC-40, Line 9) by the applicable flat rate. For TY 2025: Line 9 × 0.045 = Line 10.  _([T1-UT-1])_
- **[T1-UT-2] Starting point** — Begin with federal taxable income from Form 1040, Line 15. Enter on TC-40, Line 1.  _([T1-UT-2])_
- **[T1-UT-3] Additions to income (TC-40, Line 2)** — Common additions: State/municipal bond interest from non-Utah states (Utah-exempt bonds excluded); Lump-sum distributions taxed at federal level under 10-year averaging (rare); Certain adoption expenses previously deducted.  _([T1-UT-3])_
- **[T1-UT-4] Subtractions from income (TC-40, Lines 3–7)** — Common subtractions: Utah state tax refund included in federal income (if itemized prior year); Railroad retirement benefits (Tier 1 and Tier 2); Social Security benefits (Utah exempts all Social Security — full subtraction of amount included in federal taxable income); Military pay exclusions; Retirement income credit (age 65+ with retirement income, up to $450 credit).  _([T1-UT-4])_
- **[T1-UT-5] Taxpayer tax credit** — This is Utah's equivalent of a personal exemption. The base credit amount is $966 per taxpayer (2025). For MFJ: $966 × 2 = $1,932. Additional $2,111 per qualifying dependent. The total credit phases out at 1.3% of MAGI exceeding the threshold.  _([T1-UT-5])_
- **[T1-UT-6] Filing due date** — April 15 following the tax year (April 15, 2026 for TY 2025). Extension: October 15 (automatic with federal extension, but payment still due April 15).  _([T1-UT-6])_
- **[T1-UT-7] Estimated tax payments** — Required if Utah tax liability after credits will exceed $1,000. Due dates: April 15, June 15, September 15, January 15 (same as federal). Underpayment penalty applies if <90% of current year liability or <100% of prior year liability is paid by deadline.  _([T1-UT-7])_

## Section 6: Tier 2 rules — requires judgment

- **[T2-UT-1] Residency determination** — A domiciliary of Utah is a resident regardless of time spent outside the state. A non-domiciliary who spends 183+ days in Utah may be treated as a resident. Part-year residents apportion income to the Utah period. Freelancers who travel extensively should document days carefully.  _([T2-UT-1])_
- **[T2-UT-2] Multi-state income apportionment** — If the taxpayer has income sourced to multiple states, Utah provides a credit for taxes paid to other states (TC-40A). The credit is limited to the lesser of: (a) tax actually paid to the other state, or (b) Utah tax on the income sourced to the other state.  _([T2-UT-2])_
- **[T2-UT-3] Taxpayer tax credit phase-out computation** — For high-income filers, the taxpayer tax credit phases out entirely. The effective result is that Utah tax approaches a true flat tax on all taxable income for higher earners, while lower earners pay less due to the credit. Reviewer should verify phase-out math for edge cases.  _([T2-UT-3])_
- **[T2-UT-4] Business vs. hobby determination** — Same federal §183 analysis applies. If the IRS recharacterizes Schedule C activity as a hobby, Utah follows that treatment.  _([T2-UT-4])_

## Section 7: Supplier pattern library

**Supplier pattern library**

| Income/deduction type | Utah treatment | Notes |
| --- | --- | --- |
| Schedule C net profit | Included via federal taxable income | No adjustment |
| Self-employment tax deduction | Included via federal AGI reduction | No adjustment |
| SEP/SIMPLE/solo 401(k) | Included via federal AGI reduction | No adjustment |
| QBI deduction (§199A) | Included via federal taxable income | No adjustment |
| Self-employed health insurance | Included via federal AGI reduction | No adjustment |
| Home office deduction | Included via Schedule C reduction | No adjustment |
| Social Security benefits | Subtract from Utah income | Full exemption |
| State income tax refund | Subtract if included federally | Prevents double-tax |
| Out-of-state municipal bond interest | Add to Utah income | Not exempt for UT |
| Utah municipal bond interest | Exempt | No addition needed |

## Section 8: Form mapping

**Form mapping**

| TC-40 Line | Description | Source |
| --- | --- | --- |
| Line 1 | Federal taxable income | Form 1040, Line 15 |
| Line 2 | Additions | TC-40, Additions schedule |
| Line 3–7 | Subtractions (Social Security, retirement, etc.) | TC-40, Subtractions schedule |
| Line 8 | Other subtractions | Various |
| Line 9 | Utah state taxable income (Line 1 + 2 − subtractions) | Computed |
| Line 10 | Tax (Line 9 × rate) | 4.50% for TY 2025 |
| Line 11 | Taxpayer tax credit | Computed per credit schedule |
| Line 12 | Income tax after credits | Line 10 − Line 11 (min $0) |
| Line 20+ | Payments and refundable credits | W-2 withholding, estimated payments |

## Section 9: Refusal catalogue

**Refusal catalogue**

| ID | Refusal | Reason |
| --- | --- | --- |
| R-UT-1 | Part-year resident apportionment | Requires pro-rata computation outside skill scope |
| R-UT-2 | Nonresident return (TC-40B) | Different form and sourcing rules |
| R-UT-3 | Utah corporate income tax | Different tax type (Form TC-20) |
| R-UT-4 | Utah estate/trust return | Different form (TC-41) |
| R-UT-5 | Historic preservation / renewable energy credits | Specialized credit computation beyond scope |
| R-UT-6 | Amended returns (TC-40A for credits paid to other states) | Complexity in multi-state allocation |
| R-UT-7 | Mining/extraction tax credits | Industry-specific, requires specialist |

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
