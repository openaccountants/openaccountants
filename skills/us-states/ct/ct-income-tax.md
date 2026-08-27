---
name: ct-income-tax
description: Use this skill whenever asked about Connecticut individual income tax for self-employed individuals or sole proprietors — filing Form CT-1040, CT estimated tax (Form CT-1040ES), Connecticut tax brackets, Connecticut personal exemption, or any query involving Connecticut state income tax compliance. Trigger on phrases like "Connecticut income tax", "CT income tax", "Form CT-1040", "Connecticut estimated tax", "Connecticut self-employed tax", "DRS income tax", "CT AGI", or "Conn. Gen. Stat. §12-700".
version: "0.1"
jurisdiction: US-CT
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# CT Income Tax

## Connecticut Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers Connecticut individual income tax for self-employed individuals and sole proprietors filing Form CT-1040. It addresses tax computation, personal exemptions, estimated payments, and form mapping.
> **Quality tier.** Q3 — AI-drafted with citations; not independently verified by a licensed professional.

## Section 1: Metadata

**Metadata table**

| Field | Value |
| --- | --- |
| Jurisdiction | Connecticut, United States |
| Jurisdiction code | US-CT |
| Tax authority | Connecticut Department of Revenue Services (DRS) |
| Filing portal | https://portal.ct.gov/DRS-myconneCT |
| Legislation citation | Conn. Gen. Stat. §12-700 et seq. |
| Primary form | Form CT-1040 — Connecticut Resident Income Tax Return |
| Filing deadline | April 15 (follows federal deadline) |
| Version | 0.1 |
| Generated | 2026-05-22 |
| Validation status | AI-drafted — Q3 |

### Sources consulted

1. Connecticut DRS — Form CT-1040 Instructions (TY 2025): https://portal.ct.gov/-/media/drs/forms/2025/income/2025-ct-1040-instructions_1225.pdf
2. Connecticut DRS — Form CT-1040ES (2025): https://portal.ct.gov/-/media/drs/forms/2025/es-forms/ct1040es-flat0125.pdf
3. Connecticut DRS — Tax Information: https://portal.ct.gov/drs/individuals/resident-income-tax/tax-information
4. TurboTax — CT State Income Tax Guide: https://blog.turbotax.intuit.com/income-tax-by-state/connecticut-106627/

## Section 2: Quick reference — rates and thresholds

### Tax rates (TY 2025)

Connecticut uses a complex progressive system with 7 brackets, plus a personal exemption phase-out (Table C) and tax recapture (Table D) for higher incomes.

**Single and Married Filing Separately (Table B — Initial Tax Calculation)**

| CT taxable income | Tax |
| --- | --- |
| $0 – $10,000 | 2.00% of amount |
| $10,001 – $50,000 | $200 + 4.50% of excess over $10,000 |
| $50,001 – $100,000 | $2,000 + 5.50% of excess over $50,000 |
| $100,001 – $200,000 | $4,750 + 6.00% of excess over $100,000 |
| $200,001 – $250,000 | $10,750 + 6.50% of excess over $200,000 |
| $250,001 – $500,000 | $14,000 + 6.90% of excess over $250,000 |
| Over $500,000 | $31,250 + 6.99% of excess over $500,000 |

**Married Filing Jointly / Qualifying Surviving Spouse**

| CT taxable income | Tax |
| --- | --- |
| $0 – $20,000 | 2.00% of amount |
| $20,001 – $100,000 | $400 + 4.50% of excess over $20,000 |
| $100,001 – $200,000 | $4,000 + 5.50% of excess over $100,000 |
| $200,001 – $400,000 | $9,500 + 6.00% of excess over $200,000 |
| $400,001 – $500,000 | $21,500 + 6.50% of excess over $400,000 |
| $500,001 – $1,000,000 | $28,000 + 6.90% of excess over $500,000 |
| Over $1,000,000 | $62,500 + 6.99% of excess over $1,000,000 |

**Head of Household**

| CT taxable income | Tax |
| --- | --- |
| $0 – $16,000 | 2.00% of amount |
| $16,001 – $80,000 | $320 + 4.50% of excess over $16,000 |
| $80,001 – $160,000 | $3,200 + 5.50% of excess over $80,000 |
| $160,001 – $320,000 | $7,600 + 6.00% of excess over $160,000 |
| $320,001 – $400,000 | $17,200 + 6.50% of excess over $320,000 |
| $400,001 – $800,000 | $22,400 + 6.90% of excess over $400,000 |
| Over $800,000 | $50,000 + 6.99% of excess over $800,000 |

### Personal exemption (not a standard deduction)

Connecticut does **not** have a standard deduction. Instead, it uses a personal exemption that phases out at higher income levels:

**Personal exemption by filing status**

| Filing status | Maximum personal exemption | Phase-out begins (CT AGI) |
| --- | --- | --- |
| Single | $15,000 | $30,000 |
| Married Filing Jointly | $24,000 | $48,000 |
| Head of Household | $19,000 | $38,000 |
| Married Filing Separately | $12,000 | $24,000 |

- **Exemption reduction mechanics** — The exemption is reduced by $1,000 for each $1,000 (or fraction) of CT AGI above the phase-out threshold, until fully phased out.

### Additional tax adjustments

- **Table C:** 2% phase-out add-back applied at higher income levels.
- **Table D:** Tax recapture for highest earners (effectively increases marginal rate).

## Section 3: How this skill works with the federal return

- **Starting point** — Connecticut begins with federal adjusted gross income (federal Form 1040, Line 11).
- **Connecticut additions (Schedule 1)** — Add back amounts deducted federally but not recognized by CT (e.g., interest on non-Connecticut state/local obligations, certain lump-sum distributions).
- **Connecticut subtractions (Schedule 1)** — Subtract CT-exempt income (e.g., social security benefits, military retirement pay, interest on U.S. obligations, exempt pension income).
- **Connecticut AGI** — Federal AGI ± additions – subtractions = CT AGI (Line 5).
- **Income tax calculation** — Apply Table B rates to CT AGI (no deductions subtracted first — CT does not have a standard deduction).
- **Personal exemption application** — Applied as a tax credit reduction (Table A), not a subtraction from income.
- **Phase-out and recapture** — Apply Table C (2% add-back) and Table D (recapture) if applicable.
- **Result** — CT income tax after adjustments.

## Section 4: Self-employed specific rules

### Federal conformity

- **Federal conformity rules** — - Connecticut generally conforms to the IRC for computing federal AGI. - Schedule C business deductions flow through federal AGI into Connecticut's computation.

### QBI deduction (§199A)

- **QBI deduction treatment** — The federal QBI deduction is taken below the line on the federal return and does not affect federal AGI. Therefore, it does not reduce Connecticut's starting point (CT begins from federal AGI). Connecticut does not have its own QBI equivalent.

### SE health insurance deduction

- **SE health insurance deduction treatment** — Flows through federal AGI (above-the-line deduction) and is automatically reflected in CT's starting point.

### Retirement contributions

- **Retirement contributions treatment** — SEP-IRA and Solo 401(k) contributions reduce federal AGI and therefore reduce CT starting income.

### Home office deduction

- **Home office deduction treatment** — Federal home office deduction flows through Schedule C → federal AGI → CT.

### Estimated tax payments (Form CT-1040ES)

- **Estimated tax threshold** — Must pay estimated tax if you expect CT income tax (after withholding and PE Tax Credit) ≥ $1,000 AND withholding < required annual payment.
- **Required annual payment** — Lesser of 90% of current year tax or 100% of prior year tax.
- **Due dates** — April 15, June 15, September 15, January 15.
- **Payment methods** — myconneCT portal (portal.ct.gov/DRS-myconneCT), credit card, or mail Form CT-1040ES to DRS.
- **Underpayment penalty** — Interest charged on underpayment (Form CT-2210).

## Section 5: Tier 1 rules — deterministic

**Tier 1 rules table**

| # | Rule | Logic |
| --- | --- | --- |
| T1-01 | Apply Table B rates to CT AGI | Graduated rates by filing status (7 brackets: 2%–6.99%) |
| T1-02 | Personal exemption (Table A) | Based on filing status and CT AGI; phases out |
| T1-03 | No standard deduction | CT does not allow a standard deduction — only personal exemption |
| T1-04 | Social Security benefits subtracted | If included in federal AGI, full subtraction allowed |
| T1-05 | Estimated tax threshold | CT tax after withholding/credits ≥ $1,000 |
| T1-06 | Filing threshold | Single: CT AGI > $15,000; MFJ: > $24,000; HOH: > $19,000; MFS: > $12,000 |
| T1-07 | Use tax reporting | Schedule 4 on CT-1040 for online purchases without sales tax |

## Section 6: Tier 2 rules — requires judgment

**Tier 2 rules table**

| # | Rule | Why judgment needed |
| --- | --- | --- |
| T2-01 | Table C 2% phase-out add-back | Complex calculation based on CT AGI relative to thresholds |
| T2-02 | Table D tax recapture | Additional tax for highest earners; requires careful computation |
| T2-03 | Pass-Through Entity Tax Credit | If business operates as PTE making CT PE tax payments, taxpayer claims credit |
| T2-04 | Part-year/nonresident allocation | Requires Form CT-1040NR/PY and income sourcing |
| T2-05 | Credit for taxes paid to other states | Schedule 2 on CT-1040; requires documentation |
| T2-06 | Pension/annuity income exemption | Complex eligibility based on age, income type, and CT AGI thresholds |
| T2-07 | CT earned income tax credit (CT EITC) | 40% of federal EITC; phased out at higher income |

## Section 7: Supplier pattern library

**Supplier pattern library table**

| Pattern on bank/CC statement | Likely meaning |
| --- | --- |
| `CT DRS` / `CONN DEPT REV` | Connecticut income tax payment |
| `MYCONNECT CT` / `MYCONNECT TAX` | Payment via myconneCT portal |
| `STATE OF CT TAX` | State tax payment |
| `CT REVENUE SERVICES` | DRS payment |
| `CT-1040ES` | Estimated tax payment |

## Section 8: Form mapping

**Form mapping table**

| Computed value | Form CT-1040 line |
| --- | --- |
| Federal AGI | Line 1 |
| Connecticut additions | Line 2 (from Schedule 1, Line 38) |
| Connecticut subtractions | Line 4 (from Schedule 1, Line 50) |
| Connecticut AGI | Line 5 |
| Income tax (from Table B or tax tables) | Line 6 |
| Credit for income taxes paid to other jurisdictions | Line 7 (Schedule 2) |
| CT alternative minimum tax | Line 9 |
| Adjusted net CT income tax | Line 12 |
| CT income tax (after credits) | Line 14 |
| Use tax | Line 15 (Schedule 4) |
| Estimated tax payments | Line 19 |
| Balance due / refund | Lines 22–24 |

## Section 9: Refusal catalogue

This skill must refuse and recommend professional review when:

**Refusal catalogue table**

| # | Condition |
| --- | --- |
| R-01 | Taxpayer has multistate business activity requiring allocation |
| R-02 | Taxpayer is a part-year/nonresident with complex CT-source income |
| R-03 | Complex PE Tax Credit calculations for pass-through entity owners |
| R-04 | CT alternative minimum tax applicability |
| R-05 | Questions about Connecticut estate/gift tax planning |
| R-06 | Issues involving CT Angel Investor Tax Credit or Film Tax Credit |
| R-07 | Determination of domicile vs. statutory residency (183-day rule) |
| R-08 | Audit representation or controversy matters |
| R-09 | Any question about tax fraud, evasion, or aggressive positions |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
