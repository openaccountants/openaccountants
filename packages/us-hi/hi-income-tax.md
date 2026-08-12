---
name: hi-income-tax
description: "Hawaii Individual Income Tax Return (Form N-11) for sole proprietors and single-member LLCs. Covers the twelve-bracket graduated system (1.4%–11%), Hawaii standard deduction, personal exemptions, modifications to federal AGI, and estimated tax (Form N-1). Trigger: taxpayer is a Hawaii resident or has Hawaii-source income."
version: "0.1"
jurisdiction: US-HI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# HI Income Tax

## Hawaii Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers Hawaii individual income tax for self-employed individuals and sole proprietors filing Form N-11. Hawaii has one of the most progressive rate structures in the U.S. with 12 brackets ranging from 1.4% to 11%.
> **Quality tier.** Q3 — AI-drafted with citations. Must be reviewed by a qualified professional before use.

## Section 1: Metadata

- **Jurisdiction** — US-HI (Hawaii)
- **Tax authority** — Hawaii Department of Taxation (DOTAX)
- **Filing portal** — [Hawaii Tax Online](https://hitax.hawaii.gov/)
- **Legislation citation** — Hawaii Revised Statutes (HRS) Chapter 235 (Income Tax Law)
- **Primary form** — Form N-11 (Individual Income Tax Return — Resident)
- **Filing deadline** — April 20, 2026 (for tax year 2025)
- **Extension** — Automatic 6-month extension to October 20 if estimated tax is paid by April 20
- **Version** — 0.1
- **Generated date** — May 22, 2026
- **Validation status** — AI-drafted — Q3

### Sources consulted

- Hawaii Department of Taxation — Tax Rate Schedules (2025): https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/
- Hawaii Department of Taxation — Tax Year 2025 Information: https://tax.hawaii.gov/tax-year-information/
- HRS § 235-51 (tax rates): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0051.htm
- Everlance — Guide to Hawaii Self-Employed Taxes: https://www.everlance.com/blog/hawaii-self-employed-taxes
- TurboTax — Hawaii State Income Tax Guide: https://blog.turbotax.intuit.com/income-tax-by-state/hawaii-108220/

## Section 2: Quick reference — rates and thresholds

### Tax year 2025 brackets — Single / Married filing separately

**Tax year 2025 brackets — Single / Married filing separately**  _(HRS § 235-51; Hawaii DOTAX Tax Year 2025 schedules.)_

| Taxable income | Rate | Cumulative tax at top of bracket |
| --- | --- | --- |
| $0 – $9,600 | 1.40% | $134 |
| $9,601 – $14,400 | 3.20% | $288 |
| $14,401 – $19,200 | 5.50% | $552 |
| $19,201 – $24,000 | 6.40% | $859 |
| $24,001 – $36,000 | 6.80% | $1,675 |
| $36,001 – $48,000 | 7.20% | $2,539 |
| $48,001 – $125,000 | 7.60% | $8,391 |
| $125,001 – $175,000 | 7.90% | $12,341 |
| $175,001 – $225,000 | 8.25% | $16,466 |
| $225,001 – $275,000 | 9.00% | $20,966 |
| $275,001 – $325,000 | 10.00% | $25,966 |
| Over $325,000 | 11.00% | — |

### Tax year 2025 brackets — Married filing jointly / Qualifying surviving spouse

**Tax year 2025 brackets — Married filing jointly / Qualifying surviving spouse**  _(HRS § 235-51; Hawaii DOTAX Tax Year 2025 schedules.)_

| Taxable income | Rate | Cumulative tax at top of bracket |
| --- | --- | --- |
| $0 – $19,200 | 1.40% | $269 |
| $19,201 – $28,800 | 3.20% | $576 |
| $28,801 – $38,400 | 5.50% | $1,104 |
| $38,401 – $48,000 | 6.40% | $1,718 |
| $48,001 – $72,000 | 6.80% | $3,350 |
| $72,001 – $96,000 | 7.20% | $5,078 |
| $96,001 – $250,000 | 7.60% | $16,782 |
| $250,001 – $350,000 | 7.90% | $24,682 |
| $350,001 – $450,000 | 8.25% | $32,932 |
| $450,001 – $550,000 | 9.00% | $41,932 |
| $550,001 – $650,000 | 10.00% | $51,932 |
| Over $650,000 | 11.00% | — |

### Standard deduction (tax year 2025)

**Standard deduction (tax year 2025)**

| Filing status | Standard deduction |
| --- | --- |
| Single | $4,400 |
| Married filing jointly | $8,800 |
| Married filing separately | $4,400 |
| Head of household | $6,424 |

### Personal exemptions (tax year 2025)

**Personal exemptions (tax year 2025)**

| Item | Amount |
| --- | --- |
| Personal exemption (each taxpayer/spouse) | $1,144 |
| Dependent exemption (each) | $1,144 |

### Filing thresholds (tax year 2025)

**Filing thresholds (tax year 2025)**

| Filing status | Threshold (gross income) |
| --- | --- |
| Single (under 65) | $5,544 |
| Single (65+) | $6,688 |
| Married filing jointly (both under 65) | $11,088 |
| Married filing jointly (one 65+) | $12,232 |
| Head of household (under 65) | $7,568 |

- **Doing business filing requirement** — Additionally, anyone "doing business" in Hawaii must file regardless of income level.

## Section 3: How this skill works with the federal return

- **Starting point** — Hawaii begins with federal adjusted gross income (AGI) from federal Form 1040, Line 11.

### Key additions to Hawaii income

- Interest on state/local obligations of other states
- Amounts deducted federally but not allowed by Hawaii

### Key subtractions from Hawaii income

- Social Security benefits (Hawaii does not tax Social Security)
- Interest on U.S. government obligations (Treasury bonds, savings bonds)
- Military reserve/National Guard pay (limited exclusion)
- Certain pension income adjustments

### Net result

- **Hawaii taxable income calculation** — Federal AGI ± Hawaii modifications = Hawaii AGI → minus standard or itemized deductions → minus personal exemptions = Hawaii taxable income → apply rate schedule.

### QBI conformity

- **QBI conformity** — Hawaii starts from federal AGI. The federal QBI deduction (§199A) is below AGI and does NOT flow into Hawaii's computation.

### SE health insurance deduction

- **SE health insurance deduction** — Already reflected in federal AGI. Flows through to Hawaii automatically.

### Retirement contributions (SEP, SIMPLE, solo 401(k))

- **Retirement contributions** — Already reflected in federal AGI. No Hawaii add-back required.

### Home office deduction

- **Home office deduction** — Already reflected in Schedule C → federal AGI. Flows through automatically.

### Estimated tax (Form N-1)

- **Quarterly estimated payment requirement** — Self-employed individuals must make quarterly estimated payments if they expect to owe $500 or more.
- **Voucher due dates** — April 20, June 20, September 20, January 20

**Note:** Hawaii's due dates are the 20th (not the 15th like most states).

### General Excise Tax (GET) interaction

- **GET interaction with income tax** — Hawaii self-employed individuals are also subject to GET on gross business income (4% general rate, 4.5% in Honolulu County with the county surcharge). GET is NOT the same as income tax. GET paid is a deductible business expense on federal Schedule C, reducing federal AGI and therefore Hawaii taxable income. See `hi-sales-tax.md` for GET details.

### Hawaii conformity notes

- **IRC conformity and depreciation differences** — Hawaii generally conforms to the Internal Revenue Code as of a specific date. However, Hawaii has its own depreciation rules and may not conform to all federal provisions. Key differences: - Hawaii does NOT conform to federal bonus depreciation (§168(k)) - Taxpayers must use Hawaii's depreciation schedule (generally straight-line MACRS equivalent)

## Section 5: Tier 1 rules — deterministic

**Tier 1 rules — deterministic**

| Rule ID | Rule |
| --- | --- |
| HI-IT-1.01 | Hawaii taxable income = Hawaii AGI − deduction − personal exemptions |
| HI-IT-1.02 | If taxable income < $100,000, use tax table; if ≥ $100,000, use rate schedule |
| HI-IT-1.03 | Personal exemption: $1,144 per taxpayer, spouse (if joint), and each dependent |
| HI-IT-1.04 | Social Security benefits are fully excluded from Hawaii income |
| HI-IT-1.05 | Filing deadline is April 20 (not April 15) |
| HI-IT-1.06 | Automatic 6-month extension to October 20 if estimated tax paid timely |
| HI-IT-1.07 | Hawaii does not conform to federal §168(k) bonus depreciation |
| HI-IT-1.08 | Hawaii allows credit for taxes paid to other states |

## Section 6: Tier 2 rules — requires judgment

**Tier 2 rules — requires judgment**

| Rule ID | Rule | Judgment needed |
| --- | --- | --- |
| HI-IT-2.01 | Standard vs. itemized deduction election | Hawaii allows itemization independently of federal choice |
| HI-IT-2.02 | Depreciation conformity analysis | Determine add-back for federal bonus depreciation vs. Hawaii depreciation |
| HI-IT-2.03 | Part-year resident allocation | Prorate income for period of Hawaii residency |
| HI-IT-2.04 | GET vs. income tax interaction | Ensure GET is properly deducted on Schedule C, not double-counted |
| HI-IT-2.05 | Food/excise tax credit | Available to lower-income residents; verify eligibility |
| HI-IT-2.06 | Refundable food/excise tax credit | $110 per exemption if federal AGI ≤ $50,000 (single) |

## Section 7: Supplier pattern library

**Supplier pattern library**

| Pattern on bank statement | Likely meaning |
| --- | --- |
| STATE OF HI TAX | Hawaii income tax payment |
| HAWAII DOTAX | Hawaii Department of Taxation payment |
| HI TAX REFUND | Hawaii income tax refund |
| HITAX PMT | Hawaii estimated tax payment |

## Section 8: Form mapping

**Form mapping**

| Hawaii Form | Federal equivalent / Input |
| --- | --- |
| Form N-11, Line 10 | Federal Form 1040, Line 11 (AGI) |
| Form N-11, Lines 11–17 | Hawaii modifications (additions/subtractions) |
| Form N-11, Line 22 | Hawaii AGI |
| Form N-11, Line 24 | Standard or itemized deductions |
| Form N-11, Line 25 | Personal exemptions |
| Form N-11, Line 26 | Hawaii taxable income |
| Form N-11, Line 27 | Tax from table or schedule |
| Form N-1 | Quarterly estimated payments |
| Form N-210 | Underpayment of estimated tax penalty |

## Section 9: Refusal catalogue

**Refusal catalogue**

| Refusal ID | Topic | Reason |
| --- | --- | --- |
| R-HI-01 | Corporate income tax (Form N-30) | Not individual income tax |
| R-HI-02 | Transient accommodations tax (TAT) | Separate regime for lodging |
| R-HI-03 | Part-year / nonresident returns (Form N-15) | Different form and allocation rules |
| R-HI-04 | GET computation details | See hi-sales-tax.md |
| R-HI-05 | County surcharge details | Varies by county; requires local analysis |
| R-HI-06 | Conveyance tax | Real property transaction tax |
| R-HI-07 | Estate tax | Separate regime |

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
