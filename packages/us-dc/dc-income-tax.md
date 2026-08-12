---
name: dc-income-tax
description: "District of Columbia Individual Income Tax Return (Form D-40) for sole proprietors and single-member LLCs. Covers the seven-bracket graduated system (4%–10.75%), DC standard deduction computation, Schedule S additions and subtractions, estimated tax (D-40ES), and the Earned Income Tax Credit. Trigger: taxpayer is domiciled in DC or maintains an abode for 183+ days during the tax year."
version: "0.1"
jurisdiction: US-DC
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# DC Income Tax

## District of Columbia Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers DC individual income tax for self-employed individuals and sole proprietors filing Form D-40. It handles the graduated rate structure, DC-specific standard deduction, and modifications to federal AGI.
> **Quality tier.** Q3 — AI-drafted with citations. Must be reviewed by a qualified professional before use.

## Section 1: Metadata

- **Jurisdiction** — US-DC (District of Columbia)
- **Tax authority** — DC Office of Tax and Revenue (OTR)
- **Filing portal** — [MyTax.DC.gov](https://mytax.dc.gov/)
- **Legislation citation** — DC Code Title 47, Chapter 18
- **Primary form** — D-40 (Individual Income Tax Return)
- **Filing deadline** — April 15, 2026 (for tax year 2025)
- **Extension** — Automatic 6-month extension if federal extension filed; tax must still be paid by April 15
- **Version** — 0.1
- **Generated date** — May 22, 2026
- **Validation status** — AI-drafted — Q3

### Sources consulted

- DC Office of Tax and Revenue — Individual and Fiduciary Income Tax Rates: https://otr.cfo.dc.gov/page/dc-individual-and-fiduciary-income-tax-rates
- 2025 D-40 Booklet (Instructions): https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_Final_wLinks_030526_v1.0.pdf
- D-40ES Estimated Payment Voucher (2026): https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2026_D40ES_Book_wLinks04012026.pdf
- DC Code § 47-1806.03 (tax rates): https://code.dccouncil.gov/us/dc/council/code/sections/47-1806.03
- Thomson Reuters — DC Temporary Legislation (Act 26-214): https://tax.thomsonreuters.com/news/d-c-enacts-temporary-legislation-amending-conformity-with-various-irc-provisions-other-tax-changes/

## Section 2: Quick reference — rates and thresholds

### Tax year 2025 brackets (all filing statuses)

**Tax year 2025 brackets (all filing statuses)**  _(DC Code § 47-1806.03; OTR official rate table (effective for tax years beginning after 12/31/2021).)_

| Taxable income | Rate | Cumulative tax at top of bracket |
| --- | --- | --- |
| $0 – $10,000 | 4% | $400 |
| $10,001 – $40,000 | 6% | $2,200 |
| $40,001 – $60,000 | 6.5% | $3,500 |
| $60,001 – $250,000 | 8.5% | $19,650 |
| $250,001 – $500,000 | 9.25% | $42,775 |
| $500,001 – $1,000,000 | 9.75% | $91,525 |
| Over $1,000,000 | 10.75% | — |

### DC standard deduction (tax year 2025)

**DC standard deduction (tax year 2025)**

| Filing status | Standard deduction |
| --- | --- |
| Single / Married filing separately | $15,000 |
| Head of household | $22,500 |
| Married filing jointly / Qualifying surviving spouse | $30,000 |

- **Additional standard deduction** — Additional standard deduction: $1,600 ($2,000 if single/HoH) for taxpayers born before January 2, 1961, or who are blind.

**Note:** Beginning with tax year 2025, DC has decoupled from the federal standard deduction and has repealed personal exemptions entirely (DC Act 26-214).

### Filing thresholds (tax year 2025)

**Filing thresholds (tax year 2025)**

| Filing status | Gross income threshold |
| --- | --- |
| Single / Married filing separately | $15,000 |
| Married filing jointly | $30,000 |
| Head of household | $22,500 |

## Section 3: How this skill works with the federal return

**Starting point:** DC begins with federal adjusted gross income (AGI) from federal Form 1040, Line 11.

### Key additions to DC income (Schedule S)

- **Key additions to DC income (Schedule S)** — - Franchise tax deducted on federal return - State/local income tax refunds not already in federal AGI (if applicable) - Any DC-decoupled items (e.g., §174A R&E immediate expensing — DC decoupled effective 2025)

### Key subtractions from DC income (Schedule S)

- **Key subtractions from DC income (Schedule S)** — - DC government pension/annuity exclusion (up to $3,000 for qualifying recipients) - Social Security benefits (DC does not tax Social Security) - Income earned by DC National Guard members on active duty

### Net result

- **DC taxable income computation** — Federal AGI ± DC modifications = DC adjusted gross income → minus standard or itemized deduction = DC taxable income → apply rate table.

## Section 4: Self-employed specific rules

### QBI conformity

- **QBI conformity** — DC starts from federal AGI. The federal QBI deduction (§199A) is taken below AGI on the federal return (line 13 of Form 1040) and does NOT flow into DC's computation. DC taxable income is computed independently from federal taxable income.

### SE health insurance deduction

- **SE health insurance deduction** — Already reflected in federal AGI (Form 1040, Schedule 1, Line 17). Flows through to DC automatically.

### Retirement contributions (SEP, SIMPLE, solo 401(k))

- **Retirement contributions (SEP, SIMPLE, solo 401(k))** — Already reflected in federal AGI. No DC add-back required.

### Home office deduction

- **Home office deduction** — Already reflected in Schedule C → federal AGI. Flows through to DC automatically.

### Estimated tax (Form D-40ES)

- **Estimated tax requirement** — Self-employed individuals must make quarterly estimated payments if they expect to owe $100 or more after credits and withholding. Voucher due dates: April 15, June 15, September 15, January 15.
- **Safe harbor** — Safe harbor: No penalty if payments equal at least 110% of prior year DC tax liability OR at least 90% of current year tax.

### DC Unincorporated Business Franchise Tax (Form D-30)

- **D-30 franchise tax obligation** — Self-employed individuals and sole proprietors with DC gross receipts exceeding $12,000 may also owe the DC unincorporated business franchise tax (currently 9.75% on net income over $12,000). **This skill does NOT compute the D-30.** That is a separate obligation. However, any D-30 franchise tax paid is deductible as a business expense on the federal Schedule C and flows through to reduce federal AGI.

## Section 5: Tier 1 rules — deterministic

**Tier 1 rules — deterministic**

| Rule ID | Rule |
| --- | --- |
| DC-IT-1.01 | DC taxable income = DC AGI minus DC standard deduction (or itemized deductions if elected) |
| DC-IT-1.02 | Apply the seven-bracket rate schedule to DC taxable income to compute DC tax |
| DC-IT-1.03 | If DC taxable income ≤ $100,000, use tax tables; if > $100,000, use tax computation worksheet |
| DC-IT-1.04 | Standard deduction election must match itemized/standard choice concept but DC sets its own amounts independently of federal |
| DC-IT-1.05 | Social Security benefits are fully excluded from DC taxable income |
| DC-IT-1.06 | DC EITC = 70% of federal EITC (refundable) — applies for tax year 2025 |
| DC-IT-1.07 | Property tax credit (Schedule H) available if household gross income < $50,000 and DC homeowner/renter |
| DC-IT-1.08 | Estimated tax penalty applies if total payments < 90% of current year tax AND < 110% of prior year tax |

## Section 6: Tier 2 rules — requires judgment

**Tier 2 rules — requires judgment**

| Rule ID | Rule | Judgment needed |
| --- | --- | --- |
| DC-IT-2.01 | Standard vs. itemized deduction election | Compare DC standard deduction to DC allowable itemized deductions; note DC decouples from certain federal itemization rules |
| DC-IT-2.02 | DC Schedule N (apportionment) for multi-state income | If taxpayer has income from sources outside DC, apportionment may apply |
| DC-IT-2.03 | D-30 filing obligation | Determine if gross receipts exceed $12,000 threshold; if so, refer to separate D-30 skill |
| DC-IT-2.04 | DC conformity with federal depreciation | DC decoupled from §168(k) bonus depreciation and §174A R&E — reviewer must verify add-back |

## Section 7: Supplier pattern library

**Supplier pattern library**

| Pattern on bank statement | Likely meaning |
| --- | --- |
| DC TREASURER TAX PMT | DC estimated income tax payment |
| OTR DC GOV | DC Office of Tax and Revenue payment |
| DC GOV TAX REFUND | DC income tax refund |
| DIST OF COLUMBIA TAX | DC tax payment (various) |

## Section 8: Form mapping

**Form mapping**

| DC Form | Federal equivalent / Input |
| --- | --- |
| D-40, Line 1 | Federal Form 1040, Line 11 (AGI) |
| D-40, Line 4 (Additions) | Schedule S Part I |
| D-40, Line 7 (Subtractions) | Schedule S Part II |
| D-40, Line 16 (DC AGI) | After additions/subtractions |
| D-40, Line 18 (Deduction) | DC standard deduction or itemized |
| D-40, Line 19 (Taxable income) | Line 16 minus Line 18 |
| D-40, Line 20 (Tax) | From rate table or computation worksheet |
| D-40ES | Quarterly estimated payments |
| Schedule H | Homeowner/renter property tax credit |

## Section 9: Refusal catalogue

**Refusal catalogue**

| Refusal ID | Topic | Reason |
| --- | --- | --- |
| R-DC-01 | D-30 unincorporated business franchise tax | Separate complex computation; out of scope |
| R-DC-02 | Part-year / nonresident returns (D-40B) | Different form and allocation rules |
| R-DC-03 | Corporate franchise tax (D-20) | Not individual income tax |
| R-DC-04 | Ballpark fee | Employer-level tax |
| R-DC-05 | DC itemized deduction limitations | Complex phase-out rules require separate analysis |
| R-DC-06 | Multi-state apportionment (Schedule N) | Requires detailed allocation analysis |
| R-DC-07 | Real property tax computation | Not income tax |
| R-DC-08 | Estate tax | Separate regime |

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
