---
name: my-pcb
description: Use this skill whenever asked about Malaysia PCB (monthly tax deduction) or CP500 instalment payments. Trigger on phrases like "PCB", "Potongan Cukai Bulanan", "monthly tax deduction Malaysia", "CP500", "instalment tax Malaysia", "self-employed tax payment Malaysia", "e-PCB", "LHDN instalments", "advance tax Malaysia", or any question about paying income tax during the year in Malaysia. Covers PCB for employees, CP500 for self-employed, payment schedules, penalties, and revision procedures. ALWAYS read this skill before advising on Malaysian tax prepayments.
version: 1.0
jurisdiction: MY
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: MUHAMMAD HANIS MAT HUSSIN
review_status: current
depends_on: - my-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MY Pcb

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Malaysia |
| System | PCB (Potongan Cukai Bulanan) for employees; CP500 for self-employed |
| Currency | MYR (Malaysian Ringgit / RM) |
| Tax year | Calendar year (YA = Year of Assessment) |
| Primary legislation | Income Tax Act 1967, Sections 107-107B; Income Tax (Deduction from Remuneration) Rules 1994 |
| Tax authority | LHDN (Lembaga Hasil Dalam Negeri) |
| Portal | MyTax (https://mytax.hasil.gov.my) |
| Validated by | Pending |
| Validation date | Pending |
| Skill version | 1.0 |

### System Overview

**System Overview**

| System | Applies To | Frequency | Responsible Party |
| --- | --- | --- | --- |
| PCB (Potongan Cukai Bulanan) | Employees | Monthly | Employer deducts and remits |
| CP500 | Self-employed, sole proprietors, partnerships, rental/investment income | Bimonthly (6 instalments/year) | Taxpayer pays directly |

## Section 2 -- PCB (Monthly Tax Deduction for Employees)

### 2.1 What Is PCB

- **PCB** — PCB is the Malaysian PAYE (Pay As You Earn) system. Employers withhold income tax from employees' monthly remuneration and remit it to LHDN.

### 2.2 Employer Obligations

**Employer Obligations**

| Obligation | Detail |
| --- | --- |
| Registration | Employer must register with LHDN as an employer |
| Calculation | Use LHDN's PCB Schedule or e-PCB Calculator |
| Deduction | Deduct PCB from employee's monthly salary |
| Remittance | Remit to LHDN by 15th of following month |
| Reporting | Submit Form CP39 with each remittance |
| Annual | Issue Form EA (statement of remuneration) to employees by end of February |

### 2.3 PCB Calculation Factors

**PCB Calculation Factors**

| Factor | Detail |
| --- | --- |
| Monthly remuneration | Salary, allowances, bonuses, commissions |
| Tax reliefs | Employee declares reliefs via Form TP1 |
| EPF deduction | Reduces chargeable income |
| Number of children | Affects relief calculation |
| Marital status | Single / married / spouse with income |

### 2.4 e-PCB

**e-PCB**

| Item | Detail |
| --- | --- |
| Portal | https://e.hasil.gov.my/epay (or via MyTax) |
| Submission | Monthly CP39 electronic submission |
| Payment | Online banking, FPX, or manual payment at LHDN counter |
| Deadline | 15th of the month following salary payment |

## Section 3 -- CP500 (Self-Employed Instalments)

### 3.1 What Is CP500

- **CP500** — CP500 is the instalment tax payment system for individuals with business or non-employment income. LHDN issues a CP500 notice specifying the amounts and due dates.

### 3.2 Who Receives CP500

**Who Receives CP500**

| Category | Obligation |
| --- | --- |
| Sole proprietors (business income) | Mandatory |
| Partners in partnerships | Mandatory (based on share of partnership income) |
| Individuals with rental income | May receive CP500 |
| Individuals with investment income | May receive CP500 if significant |
| First-year businesses | May not receive CP500 until first Form B is filed |

### 3.3 Basis of CP500

LHDN calculates CP500 based on:

**Basis of CP500**

| Basis | Detail |
| --- | --- |
| Prior year tax liability | LHDN uses the latest assessed or estimated tax from the prior Form B |
| Standard uplift | LHDN may increase by 5-10% to account for expected income growth |
| New businesses | Based on estimated income declared in Form B or registration |

### 3.4 Payment Schedule

CP500 is payable in **6 bimonthly instalments**:

**Payment Schedule**

| Instalment | Month | Due Date |
| --- | --- | --- |
| 1st | March | 15 March |
| 2nd | May | 15 May |
| 3rd | July | 15 July |
| 4th | September | 15 September |
| 5th | November | 15 November |
| 6th | January (following year) | 15 January |

- **Due date rule** — The due date is the 15th of the instalment month. If the 15th falls on a weekend or public holiday, the next business day applies.

### 3.5 Payment Methods

**Payment Methods**

| Method | Detail |
| --- | --- |
| Online banking (FPX) | Via MyTax portal or ByrHASiL |
| Bank counter | Using CP500 payment slip with reference number |
| ATM / CDM | Selected banks |
| Direct debit | Can be arranged with LHDN |

## Section 4 -- Revising CP500

### 4.1 When to Revise

- Business income significantly higher or lower than LHDN's estimate
- Business started or ceased mid-year
- Major change in expenses or deductions
- Change in personal reliefs

### 4.2 How to Revise

**How to Revise**

| Method | Detail |
| --- | --- |
| Form CP502 | Application to revise CP500 instalments |
| Submission deadline | By 30 June of the YA (i.e., before the 4th instalment) |
| Portal | Submit via MyTax or LHDN branch |
| Effect | LHDN revises remaining instalments; amounts already paid are credited |

### 4.3 Revision Rules

**Revision Rules**  _(Section 107B(3))_

| Rule | Detail |
| --- | --- |
| Underestimation penalty | If revised estimate is >30% below actual tax, a 10% penalty applies on the difference (Section 107B(3)) |
| Cannot revise after 30 June | Remaining instalments must be paid as per last revision |
| Increase voluntarily | Taxpayer can always pay more than the CP500 amount |

## Section 5 -- Penalties

### 5.1 Late Payment

**Late Payment**  _(Section 107B(2))_

| Situation | Penalty |
| --- | --- |
| CP500 instalment not paid by due date | 10% increase on the unpaid amount (Section 107B(2)) |
| Persistent non-payment | LHDN may take enforcement action (garnishee, travel restriction) |

### 5.2 Underestimation

**Underestimation**  _(Section 107B(3))_

| Situation | Penalty |
| --- | --- |
| Revised CP500 estimate is >30% below actual tax liability | 10% penalty on the difference between actual and estimated tax (Section 107B(3)) |
| No revision filed but significant underpayment | Penalty at assessment stage |

### 5.3 Employer PCB Penalties

**Employer PCB Penalties**

| Situation | Penalty |
| --- | --- |
| Failure to deduct PCB | Employer is personally liable for the amount |
| Late remittance | 10% increase on late amount |
| Failure to furnish Form EA | Fine up to RM20,000 or imprisonment up to 6 months |

## Section 6 -- Worked Examples

### Example 1 -- Sole Proprietor CP500

**Situation:** Graphic designer, YA 2024 tax liability was RM8,400. LHDN issues CP500 for YA 2025 based on this amount.

**CP500 schedule:** 6 × RM1,400 = RM8,400 total
- 15 Mar: RM1,400
- 15 May: RM1,400
- 15 Jul: RM1,400
- 15 Sep: RM1,400
- 15 Nov: RM1,400
- 15 Jan 2026: RM1,400

**Actual YA 2025 tax liability:** RM10,200. Balance of RM1,800 due upon filing Form B (30 June 2026).

### Example 2 -- CP500 Revision

**Situation:** Consultant expects income to drop significantly. Revised estimate: RM4,500 tax for the year.

**Action:** Submits Form CP502 by 30 June 2025. Remaining 3 instalments reduced. Already paid RM4,200 (3 × RM1,400). New instalments: RM100 each for Jul, Sep, Nov.

**Risk:** If actual tax turns out to be RM7,000, difference from revised estimate (RM7,000 - RM4,500 = RM2,500) is >30% of actual (30% × RM7,000 = RM2,100). Since RM2,500 > RM2,100, a 10% penalty on RM2,500 = RM250 may apply.

## Section 7 -- Interaction with Other Systems

**Interaction with Other Systems**

| System | Interaction |
| --- | --- |
| Form B filing | CP500 paid is credited against final tax liability on Form B |
| EPF/SOCSO/EIS | See **my-epf-socso** skill; these are separate from income tax instalments |
| Section 108 (withholding) | Tax withheld by payer on certain payments is also credited against final tax |

## Section 8 -- Reference Material

### Key Sections of ITA 1967

**Key Sections of ITA 1967**

| Topic | Reference |
| --- | --- |
| Employer PCB | Section 107; Income Tax (Deduction from Remuneration) Rules 1994 |
| CP500 instalments | Section 107B |
| Revision of estimate | Section 107B(3); Form CP502 |
| Penalties | Sections 107B(2), 107B(3), 112 |

### LHDN Resources

**LHDN Resources**

| Resource | URL |
| --- | --- |
| MyTax portal | https://mytax.hasil.gov.my |
| PCB calculator | https://e.hasil.gov.my |
| CP500 payment | ByrHASiL via MyTax |
| Contact | 03-8911 1000 |

## Prohibitions

- NEVER treat CP500 payments as deductible expenses -- they are credits against final tax
- NEVER advise skipping CP500 payments -- 10% penalty applies immediately
- NEVER revise CP500 below 70% of expected actual tax without warning about underestimation penalty
- NEVER submit Form CP502 after 30 June of the assessment year
- NEVER assume first-year businesses will automatically receive CP500 -- they may need to register
- NEVER present calculations as definitive -- always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
