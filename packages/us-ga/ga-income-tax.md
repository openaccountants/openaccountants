---
name: ga-income-tax
description: "Georgia Individual Income Tax Return (Form 500) for sole proprietors and single-member LLCs.   Covers the flat 5.19% rate (tax year 2025), Georgia taxable income computation from federal AGI,   standard deduction, dependent exemption, and estimated tax. Trigger: taxpayer is a Georgia   resident or has Georgia-source income."
version: "0.1"
jurisdiction: US-GA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# GA Income Tax

## Georgia Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers Georgia individual income tax for self-employed individuals and sole proprietors filing Form 500. Georgia has a flat income tax rate of 5.19% for tax year 2025.
> **Quality tier.** Q3 — AI-drafted with citations. Must be reviewed by a qualified professional before use.

## Section 1: Metadata

**Section 1 Metadata table**

| Field | Value |
| --- | --- |
| Jurisdiction | US-GA (Georgia) |
| Tax authority | Georgia Department of Revenue (GA DOR) |
| Filing portal | [Georgia Tax Center (GTC)](https://gtc.dor.ga.gov/) |
| Legislation citation | O.C.G.A. Title 48, Chapter 7 (Income Taxes) |
| Primary form | Form 500 (Individual Income Tax Return) |
| Filing deadline | April 15, 2026 (for tax year 2025) |
| Extension | Automatic with federal extension (attach Form 4868 or IRS confirmation); or use GA Form IT-303 |
| Version | 0.1 |
| Generated date | May 22, 2026 |
| Validation status | AI-drafted — Q3 |

### Sources consulted

- Georgia DOR — 2025 IT-511 Individual Income Tax Booklet: https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download
- Georgia DOR — Important Tax Updates: https://dor.georgia.gov/taxes/important-tax-updates
- O.C.G.A. § 48-7-20 (tax rate): as amended by HB 111 (signed April 2025)
- NerdWallet — Georgia State Income Tax: https://www.nerdwallet.com/taxes/learn/georgia-state-tax
- BlueWave HR — Georgia Flat Income Tax 2026: https://bluewavehr.com/blog/georgia-flat-income-tax-2026.html

## Section 2: Quick reference — rates and thresholds

### Tax year 2025 rate

**Tax year 2025 rate table**  _(O.C.G.A. § 48-7-20, as amended by HB 111 (2025). Rate reduced from 5.39% (2024) to 5.19% (2025).)_

| Rate | Applies to |
| --- | --- |
| 5.19% (flat) | All Georgia taxable income |

- **2026 rate change** — Under HB 111, the rate automatically drops by 0.10% per year until reaching 4.99%, subject to revenue targets. Expected 2026 rate is 5.09% (pending Georgia Department of Audits certification).  _(O.C.G.A. § 48-7-20, as amended by HB 111 (2025))_

### Standard deduction (tax year 2025)

**Standard deduction table**

| Filing status | Standard deduction |
| --- | --- |
| Single | $12,000 |
| Married filing jointly | $24,000 |
| Married filing separately | $12,000 |
| Head of household | $12,000 |

### Dependent exemption

**Dependent exemption table**

| Item | Amount |
| --- | --- |
| Dependent exemption (per dependent) | $4,000 |
| Personal exemption | None (eliminated after 12/31/2023) |

### Filing thresholds

- **Filing requirement** — You must file Georgia Form 500 if: You are required to file a federal income tax return, OR You have income subject to Georgia tax but not federal tax, OR Your gross income exceeds $24,000 (MFJ) or $12,000 (all other filers)

## Section 3: How this skill works with the federal return

**Starting point:** Georgia begins with federal adjusted gross income (AGI) from federal Form 1040, Line 11.

### Key additions to Georgia income (Schedule 3)

- **Additions list** — Interest on obligations of other states (not Georgia or federal); Bonus depreciation add-back (Georgia does NOT conform to federal §168(k) bonus depreciation); Other state-specific additions

### Key subtractions from Georgia income (Schedule 3)

- **Social Security exemption** — Social Security benefits (Georgia fully exempts Social Security from state income tax)
- **Retirement income exclusion** — up to $35,000 per taxpayer age 62–64; up to $65,000 per taxpayer age 65+ (includes retirement plan distributions, interest, dividends, capital gains, rental income). Within the exclusion, earned income (wages, self-employment income) is capped at $4,000. USD  _(O.C.G.A. §48-7-27(a)(5))_
- **Georgia lottery winnings exemption** — first $5,000 exempt USD
- **Military retirement income exclusion** — up to $35,000 for taxpayers under 62 USD

### Net result

- **Georgia income tax computation** — Federal AGI ± Georgia modifications = Georgia adjusted gross income → minus standard deduction → minus dependent exemptions = Georgia taxable income → × 5.19% = Georgia income tax.

## Section 4: Self-employed specific rules

### QBI conformity

- **QBI treatment** — Georgia starts from federal AGI. The federal QBI deduction (§199A) is below AGI and does NOT flow into Georgia's computation. Georgia taxable income is computed independently.

### SE health insurance deduction

- **SE health insurance** — Already reflected in federal AGI. Flows through to Georgia automatically.

### Retirement contributions (SEP, SIMPLE, solo 401(k))

- **Retirement contributions** — Already reflected in federal AGI. No Georgia add-back required.

### Home office deduction

- **Home office deduction** — Already reflected in Schedule C → federal AGI. Flows through automatically.

### Estimated tax (Form 500-ES)

- **Estimated payment requirement** — Self-employed individuals must make quarterly estimated payments if they expect to owe $1,000 or more after withholding and credits.
- **Voucher due dates** — April 15, June 15, September 15, January 15.
- **Safe harbor** — No penalty if payments equal at least 100% of prior year tax OR 90% of current year tax.

### Bonus depreciation add-back

- **Bonus depreciation treatment** — Georgia has NOT adopted federal bonus depreciation under §168(k). Taxpayers who claimed bonus depreciation on the federal return must add back the excess over Georgia's allowed depreciation (typically straight-line MACRS) and then claim the Georgia depreciation as a subtraction in subsequent years.

## Section 5: Tier 1 rules — deterministic

**Tier 1 rules table**

| Rule ID | Rule |
| --- | --- |
| GA-IT-1.01 | Georgia tax = Georgia taxable income × 5.19% |
| GA-IT-1.02 | Georgia taxable income = GA AGI − standard deduction − (dependent exemptions × $4,000) |
| GA-IT-1.03 | Social Security benefits are fully excluded |
| GA-IT-1.04 | No local/city income taxes anywhere in Georgia |
| GA-IT-1.05 | Form 500EZ discontinued — all filers use Form 500 (beginning tax year 2025) |
| GA-IT-1.06 | Georgia allows credit for taxes paid to other states (to prevent double taxation) |
| GA-IT-1.07 | Georgia does not have a state-level EITC |
| GA-IT-1.08 | Filing deadline same as federal: April 15 |

## Section 6: Tier 2 rules — requires judgment

**Tier 2 rules table**

| Rule ID | Rule | Judgment needed |
| --- | --- | --- |
| GA-IT-2.01 | Bonus depreciation add-back/recovery | Multi-year tracking required; Georgia allows recovery over asset life |
| GA-IT-2.02 | Part-year resident allocation | Prorate income for period of Georgia residency |
| GA-IT-2.03 | Retirement income exclusion eligibility | Verify age, income type, and per-taxpayer limits |
| GA-IT-2.04 | Credit for taxes paid to other states | Verify other state tax was actually paid on same income |
| GA-IT-2.05 | 2026 rate change | Monitor whether revenue targets are met for automatic rate reduction to 5.09% |

## Section 7: Supplier pattern library

**Supplier pattern library table**

| Pattern on bank statement | Likely meaning |
| --- | --- |
| GA DEPT OF REVENUE | Georgia income tax payment |
| STATE OF GA TAX PMT | Georgia estimated tax payment |
| GEORGIA TAX REFUND | Georgia income tax refund |
| GA DOR GTC | Georgia Tax Center payment |

## Section 8: Form mapping

**Form mapping table**

| Georgia Form | Federal equivalent / Input |
| --- | --- |
| Form 500, Line 8 | Federal Form 1040, Line 11 (AGI) |
| Form 500, Schedule 3 | Georgia additions and subtractions |
| Form 500, Line 14 | Georgia adjusted gross income |
| Form 500, Line 15 | Standard deduction |
| Form 500, Line 16 | Dependent exemptions |
| Form 500, Line 17 | Georgia taxable income |
| Form 500, Line 18 | Georgia income tax (taxable income × 5.19%) |
| Form 500-ES | Quarterly estimated payments |

## Section 9: Refusal catalogue

**Refusal catalogue table**

| Refusal ID | Topic | Reason |
| --- | --- | --- |
| R-GA-01 | Corporate income tax | Not individual income tax |
| R-GA-02 | Net worth tax | Separate corporate obligation |
| R-GA-03 | Part-year / nonresident allocation | Complex allocation rules |
| R-GA-04 | Multi-state business apportionment | Requires detailed analysis |
| R-GA-05 | Partnership/S-corp pass-through | Different forms and rules |
| R-GA-06 | Withholding tax obligations | Employer-level |
| R-GA-07 | Hurricane Helene disaster relief | Special provisions; verify applicability |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
