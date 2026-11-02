---
name: wv-income-tax
description: Use this skill whenever asked about West Virginia individual income tax, West Virginia Form IT-140, West Virginia graduated tax rates, West Virginia self-employment income tax at the state level, West Virginia 2026 rate cut, or any West Virginia personal income tax question for sole proprietors. Trigger on phrases like "West Virginia income tax", "WV income tax", "Form IT-140", "West Virginia tax brackets", "WV 4.58%", "W.Va. Code §11-21", or any request involving West Virginia state individual income tax computation or filing.
version: "0.1"
jurisdiction: US-WV
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# WV Income Tax

## Scope

Scope. This skill covers the West Virginia individual income tax return (Form IT-140) for full-year West Virginia residents who are sole proprietors or single-member LLC owners. It addresses the graduated rate computation (updated for the 2026 rate cut under SB 392), West Virginia adjustments to federal AGI, and West Virginia-specific credits.

## Quality tier

Quality tier. Q3 — AI-drafted, not independently verified. All rates and rules are sourced from the West Virginia State Tax Division publications and third-party research current as of May 2026. A licensed CPA or EA should verify before relying on this skill for filing.

## Section 1: Metadata

**Metadata table**

| Field | Value |
| --- | --- |
| Jurisdiction | West Virginia, United States |
| Jurisdiction code | US-WV |
| Tax type | Individual income tax |
| Rate structure | Graduated (5 brackets) |
| Rate range | 2.11% – 4.58% (2026) |
| Primary form | Form IT-140 (Personal Income Tax Return) |
| Governing statute | W.Va. Code §11-21 |
| Tax authority | West Virginia State Tax Division |
| Filing portal | https://tax.wv.gov |
| Tax year covered | 2025 (filed 2026) and 2026 (filed 2027) |
| Last updated | May 22, 2026 |

### Sources

**Sources table**

| # | Source | URL |
| --- | --- | --- |
| 1 | WV State Tax Division — 2026 Income Tax Rate Cut | https://tax.wv.gov/Individuals/Pages/PersonalIncomeTaxReductionBill.aspx |
| 2 | 2025 Form IT-140 Instructions | https://tax.wv.gov/Individuals/Pages/PersonalIncomeTax.aspx |
| 3 | W.Va. Code §11-21 — Personal Income Tax | http://www.wvlegislature.gov/wvcode/code.cfm?chap=11&art=21 |
| 4 | Tax Foundation — West Virginia profile | https://taxfoundation.org/location/west-virginia/ |
| 5 | SB 392 (2026 session) — 5% across-the-board rate reduction | https://www.wvlegislature.gov/Bill_Status/Bills_history.cfm?input=392&year=2026&sessiontype=RS&btype=bill |

## Section 2: Quick reference — rates and thresholds

### Tax brackets — 2026 (SB 392 — 5% rate cut, retroactive to January 1, 2026)

**All filing statuses except Married Filing Separately**

| WV taxable income | Rate | Tax on bracket base |
| --- | --- | --- |
| $0 – $10,000 | 2.11% | — |
| $10,001 – $25,000 | 2.81% | $211.00 + 2.81% of excess over $10,000 |
| $25,001 – $40,000 | 3.16% | $632.50 + 3.16% of excess over $25,000 |
| $40,001 – $60,000 | 4.22% | $1,106.50 + 4.22% of excess over $40,000 |
| $60,001 and above | 4.58% | $1,950.50 + 4.58% of excess over $60,000 |

**Married Filing Separately (brackets halved)**

| WV taxable income | Rate | Tax on bracket base |
| --- | --- | --- |
| $0 – $5,000 | 2.11% | — |
| $5,001 – $12,500 | 2.81% | $105.50 + 2.81% of excess over $5,000 |
| $12,501 – $20,000 | 3.16% | $316.25 + 3.16% of excess over $12,500 |
| $20,001 – $30,000 | 4.22% | $553.25 + 4.22% of excess over $20,000 |
| $30,001 and above | 4.58% | $975.25 + 4.58% of excess over $30,000 |

### Tax brackets — 2025 (pre-SB 392)

**2025 brackets**

| WV taxable income | Rate |
| --- | --- |
| $0 – $10,000 | 2.22% |
| $10,001 – $25,000 | 2.96% |
| $25,001 – $40,000 | 3.33% |
| $40,001 – $60,000 | 4.44% |
| $60,001 and above | 4.82% |

### Rate reduction history

**Rate reduction history table**

| Tax year | Top rate | Legislation |
| --- | --- | --- |
| 2026 | 4.58% | SB 392 (2026 session) — 5% across-the-board cut |
| 2025 | 4.82% | HB 2526 (2024) |
| 2024 | 5.12% | HB 2526 (2023) — 21.25% reduction from 6.5% |
| 2023 | 6.50% | Prior law |

Note: West Virginia enacted legislation in 2023 (HB 2526) with revenue triggers that could eventually eliminate the personal income tax. The 2026 SB 392 is an additional legislated cut on top of the trigger-based reductions.

### Key thresholds

**Key thresholds table**

| Item | Amount | Source |
| --- | --- | --- |
| Filing deadline | April 15 | W.Va. Code §11-21-15 |
| Extension | October 15 (automatic with federal) | W.Va. Code §11-21-15 |
| Estimated tax threshold | If tax owed will exceed withholding by $600+ | W.Va. Code §11-21-21 |
| Family tax credit | $40 per exemption (low-income only) | Form IT-140 instructions |
| State sales tax rate | 6% | W.Va. Code §11-15 |

## Section 3: How this skill works with the federal return

West Virginia starts from federal adjusted gross income (AGI) — Form 1040, Line 11.

Flow:
1. Federal Form 1040 is completed (including Schedule C, SE).
2. Federal AGI (Line 11) flows to West Virginia Form IT-140, Line 1.
3. West Virginia additions are applied (Schedule M, Additions).
4. West Virginia subtractions are applied (Schedule M, Subtractions).
5. West Virginia taxable income is computed.
6. Tax is computed from the rate schedule (or tax table if taxable income ≤$100,000).
7. For part-year/nonresidents: apportion using Schedule A (WV income ÷ total income × tentative tax).
8. Credits are applied.

Key structural point: Because WV starts from federal AGI, the federal standard deduction and QBI deduction are NOT included. West Virginia does NOT have its own standard deduction or personal exemption deduction below the line. The entire federal AGI (after WV modifications) is subject to tax. The only below-the-line relief is via credits (family tax credit, low-income earned income exclusion).

## Section 4: Self-employed specific rules

### Self-employment tax deduction

- **Self-employment tax deduction** — The federal deduction for 50% of self-employment tax reduces federal AGI → flows through to West Virginia automatically.

### Retirement contributions

- **Retirement contributions** — SEP-IRA, SIMPLE IRA, solo 401(k) contributions reduce federal AGI → flow through automatically.

### Health insurance deduction

- **Health insurance deduction** — Self-employed health insurance deduction reduces federal AGI → flows through automatically.

### QBI deduction (§199A)

- **QBI deduction (§199A)** — West Virginia does NOT conform to the QBI deduction. Since WV starts from AGI (before QBI), the §199A deduction does not reduce WV taxable income. WV taxable income will be higher than federal taxable income by the standard deduction + QBI amounts.

### Home office deduction

- **Home office deduction** — Reduces Schedule C net profit → reduces federal AGI → flows through.

### No standard deduction

- **No standard deduction** — West Virginia does not offer a state-level standard deduction. The tax is computed on the entire West Virginia taxable income (federal AGI ± modifications). Low-income relief is provided through the family tax credit and low-income exclusion.

### Estimated tax payments

- **Estimated tax payments** — Required if expected WV tax liability after withholding will exceed $600. Due dates: April 15, June 15, September 15, January 15. Form IT-140ES (voucher).

## Section 5: Tier 1 rules — deterministic

## Section 5: Tier 1 rules — deterministic

- **[T1-WV-1] Tax computation** — Apply the graduated rate schedule to West Virginia taxable income. For TY 2026, use the SB 392 rates (2.11% – 4.58%). For taxable income ≤$100,000, use the tax table. For >$100,000, use Rate Schedule I (or Rate Schedule II for MFS).

## Section 5: Tier 1 rules — deterministic

- **[T1-WV-2] Starting point** — Begin with federal adjusted gross income from Form 1040, Line 11. Enter on Form IT-140, Line 1.

## Section 5: Tier 1 rules — deterministic

- **[T1-WV-3] West Virginia additions (Schedule M)** — Common additions for self-employed: - Interest/dividend income from other states' obligations (exempt federally but taxable for WV) - Lump sum distributions not included in federal AGI - Any income exempt from federal tax but taxable under WV law

## Section 5: Tier 1 rules — deterministic

- **[T1-WV-4] West Virginia subtractions (Schedule M)** — Common subtractions: - Interest from US government obligations (Treasury bonds, savings bonds) - Social Security benefits included in federal AGI (WV exempts) - Railroad retirement income - West Virginia state/local tax refund (if included in federal AGI) - Military pay (active duty) - WV public employee retirement benefits (partial exclusion — up to $2,000)

## Section 5: Tier 1 rules — deterministic

- **[T1-WV-5] Social Security exemption** — West Virginia fully exempts Social Security benefits from state income tax. If Social Security was included in federal AGI, subtract the entire amount on Schedule M.

## Section 5: Tier 1 rules — deterministic

- **[T1-WV-6] Filing due date** — April 15 following the tax year (April 15, 2026 for TY 2025). Extension: October 15 (automatic if federal extension obtained; attach copy of federal extension with WV return).

## Section 5: Tier 1 rules — deterministic

- **[T1-WV-7] Estimated tax payments** — Required if expected tax after withholding exceeds $600. Quarterly due dates: April 15, June 15, September 15, January 15. Form IT-140ES. Safe harbor: pay 100% of prior year liability or 90% of current year.

## Section 5: Tier 1 rules — deterministic

- **[T1-WV-8] Family tax credit** — A nonrefundable credit of $40 per exemption is available for low-income taxpayers. The credit phases out at higher income levels. Available only if WV taxable income is below the threshold in the form instructions.

## Section 5: Tier 1 rules — deterministic

- **[T1-WV-9] Senior citizen tax credit** — Taxpayers 65+ with income below $50,000 (single) or $100,000 (MFJ) may claim a credit. Amount per the published schedule.

## Section 6: Tier 2 rules — requires judgment

## Section 6: Tier 2 rules — requires judgment

- **[T2-WV-1] Residency determination** — West Virginia defines a resident as a person domiciled in WV or maintaining a permanent place of abode in WV for more than 30 days AND being present in WV for 183+ days. Freelancers working remotely who split time between states must carefully track days.

## Section 6: Tier 2 rules — requires judgment

- **[T2-WV-2] Revenue trigger elimination** — West Virginia has enacted legislation (2023 HB 2526) establishing revenue triggers that could progressively reduce and ultimately eliminate the state income tax. The 2026 rates reflect an additional legislative cut (SB 392) on top of the trigger framework. Reviewer should confirm the applicable rates for the filing year against the Tax Division's published tables.

## Section 6: Tier 2 rules — requires judgment

- **[T2-WV-3] Multi-state credit** — West Virginia allows a credit for income taxes paid to other states on income also taxed by WV. Cannot exceed WV tax on the income sourced to the other state. Requires Schedule E (Credit for Tax Paid to Other States).

## Section 6: Tier 2 rules — requires judgment

- **[T2-WV-4] Business vs. hobby** — West Virginia follows the federal §183 determination. If Schedule C activity is reclassified as hobby, WV follows.

## Section 6: Tier 2 rules — requires judgment

- **[T2-WV-5] No standard deduction — impact on effective rate** — Because WV taxes the full AGI (after modifications) without a standard deduction, the effective tax rate on low-income self-employed can be relatively high compared to states with generous standard deductions. Reviewer should assess whether estimated payments are adequate.

## Section 7: Supplier pattern library

**Supplier pattern library table**

| Income/deduction type | West Virginia treatment | Notes |
| --- | --- | --- |
| Schedule C net profit | Included via federal AGI | No adjustment |
| Self-employment tax deduction | Included via federal AGI reduction | No adjustment |
| SEP/SIMPLE/solo 401(k) | Included via federal AGI reduction | No adjustment |
| QBI deduction (§199A) | NOT included — WV starts from AGI | WV taxable income higher |
| Self-employed health insurance | Included via federal AGI reduction | No adjustment |
| Home office deduction | Included via Schedule C → AGI reduction | No adjustment |
| Social Security benefits | Subtract from WV income | Full exemption |
| US government bond interest | Subtract | Exempt from WV tax |
| Out-of-state bond interest | Add to WV income | Not exempt for WV |
| State income tax refund | Subtract if included in federal AGI | Prevents double counting |

## Section 8: Form mapping

**Form mapping table**

| IT-140 Line | Description | Source |
| --- | --- | --- |
| Line 1 | Federal adjusted gross income | Form 1040, Line 11 |
| Line 2 | WV additions (Schedule M) | Computed |
| Line 3 | Subtotal (Line 1 + Line 2) | Computed |
| Line 4 | WV subtractions (Schedule M) | Computed |
| Line 5 | WV adjusted gross income (Line 3 − Line 4) | Computed |
| Line 6 | WV personal exemptions (for low-income credit only) | Per instructions |
| Line 7 | WV taxable income (Line 5 − Line 6) | Computed |
| Line 8 | Tax (from tax table or rate schedule) | Per 2026 rates |
| Line 10 | Total income tax due (after nonresident apportionment) | Computed |
| Line 11+ | Credits | Family tax credit, senior credit |
| Line 16+ | Payments (withholding, estimated) | W-2s, IT-140ES |

## Section 9: Refusal catalogue

**Refusal catalogue table**

| ID | Refusal | Reason |
| --- | --- | --- |
| R-WV-1 | Part-year resident return | Requires pro-rata allocation (Schedule A) |
| R-WV-2 | Nonresident return | Different sourcing and apportionment rules |
| R-WV-3 | West Virginia corporate net income tax | Different tax type (Form CNF-120) |
| R-WV-4 | West Virginia B&O (Business & Occupation) tax | Separate tax administered locally |
| R-WV-5 | Severance tax (coal, natural gas, timber) | Industry-specific, separate form |
| R-WV-6 | Amended returns (Form IT-140 amended) | Requires additional procedures |
| R-WV-7 | West Virginia fiduciary income tax | Different form (IT-141) |
| R-WV-8 | Historic rehabilitation / neighborhood investment credits | Specialized credit programs |

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
