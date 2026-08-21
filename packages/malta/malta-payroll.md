---
name: malta-payroll
description: Use this skill whenever asked about Malta payroll processing for employed persons. Trigger on phrases like "Malta payroll", "FSS deduction", "employee SSC", "Class 1 contributions", "FS5", "FS3", "FS7", "payslip Malta", "net salary Malta", "PAYE Malta", "tax withholding Malta", "employer SSC Malta", "Maternity Trust Fund", "COLA Malta", "minimum wage Malta", "overtime Malta", "gross to net Malta", "salary calculation Malta", or any question about computing employee pay, withholding tax, or social security contributions for Malta-based employees. This skill covers FSS income tax withholding, Class 1 SSC (employee and employer), statutory bonuses, minimum wage, mandatory benefits, payslip requirements, and filing obligations. ALWAYS read this skill before processing any Malta payroll.
version: 1.0
jurisdiction: MT
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Malta Payroll

## Malta Payroll Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Malta (Republic of Malta) |
| Currency | EUR only |
| Standard pay frequency | Monthly (most common); weekly permitted |
| Tax year | Calendar year (1 January -- 31 December) |
| Tax withholding system | Final Settlement System (FSS) -- cumulative monthly PAYE |
| Tax authority | Commissioner for Revenue (CFR) / MTCA |
| Social security authority | Department of Social Security (DSS) |
| Key legislation | Income Tax Act (Cap. 123); Income Tax Management Act (Cap. 372); Social Security Act (Cap. 318); Employment and Industrial Relations Act (Cap. 452) |
| Filing portal | MTCA e-Services |
| Validated by | Pending -- requires sign-off by a Maltese warranted accountant |
| Skill version | 1.0 |

## Section 2 -- Income Tax Withholding (FSS)

The employer withholds income tax monthly under the Final Settlement System (FSS) based on the employee's FS4 status declaration. Tax is computed cumulatively across the year.

### FS4 Status Categories (2026)

**FS4 Status Categories (2026)**

| Status Code | Description |
| --- | --- |
| S | Single |
| M0 | Married (no qualifying children) |
| M1 | Married (1 qualifying child) |
| M2 | Married (2+ qualifying children) |
| P | Parent (single parent, no qualifying child category) |
| P1 | Parent (1 qualifying child) |
| P2 | Parent (2+ qualifying children) |

### Tax Rate Tables (2026)

**Single (S)**

| Chargeable Income (EUR) | Rate | Subtract (EUR) |
| --- | --- | --- |
| 0 -- 12,000 | 0% | 0 |
| 12,001 -- 16,000 | 15% | 1,800 |
| 16,001 -- 60,000 | 25% | 3,400 |
| 60,001+ | 35% | 9,400 |

**Married -- No Children (M0)**

| Chargeable Income (EUR) | Rate | Subtract (EUR) |
| --- | --- | --- |
| 0 -- 15,500 | 0% | 0 |
| 15,001 -- 23,000 | 15% | 2,250 |
| 23,001 -- 60,000 | 25% | 4,550 |
| 60,001+ | 35% | 10,550 |

**Married -- 1 Child (M1)**

| Chargeable Income (EUR) | Rate | Subtract (EUR) |
| --- | --- | --- |
| 0 -- 17,500 | 0% | 0 |
| 17,501 -- 26,500 | 15% | 2,625 |
| 26,501 -- 60,000 | 25% | 5,275 |
| 60,001+ | 35% | 11,275 |

**Married -- 2+ Children (M2)**

| Chargeable Income (EUR) | Rate | Subtract (EUR) |
| --- | --- | --- |
| 0 -- 22,500 | 0% | 0 |
| 22,501 -- 32,000 | 15% | 3,375 |
| 32,001 -- 60,000 | 25% | 6,575 |
| 60,001+ | 35% | 12,575 |

**Parent (P)**

| Chargeable Income (EUR) | Rate | Subtract (EUR) |
| --- | --- | --- |
| 0 -- 13,000 | 0% | 0 |
| 13,001 -- 17,500 | 15% | 1,950 |
| 17,501 -- 60,000 | 25% | 3,700 |
| 60,001+ | 35% | 9,700 |

**Parent -- 1 Child (P1)**

| Chargeable Income (EUR) | Rate | Subtract (EUR) |
| --- | --- | --- |
| 0 -- 14,500 | 0% | 0 |
| 14,501 -- 21,000 | 15% | 2,175 |
| 21,001 -- 60,000 | 25% | 4,275 |
| 60,001+ | 35% | 10,275 |

**Parent -- 2+ Children (P2)**

| Chargeable Income (EUR) | Rate | Subtract (EUR) |
| --- | --- | --- |
| 0 -- 18,500 | 0% | 0 |
| 18,501 -- 25,500 | 15% | 2,775 |
| 25,501 -- 60,000 | 25% | 5,325 |
| 60,001+ | 35% | 11,325 |

### FSS Computation Method

- **FSS Computation Method** — Monthly tax = (Cumulative gross emoluments x Rate - Subtract) / 12, adjusted cumulatively. The employer applies the rate table to projected annual income, divides by 12, then adjusts month-by-month to ensure smooth withholding. No separate Grundfreibetrag exists -- the 0% band IS the tax-free allowance.

## Section 3 -- Social Security -- Employee Deductions

Employee SSC is Class 1, computed weekly on the basic weekly wage at 10%, subject to caps.

### Class 1 Employee SSC Rates (2026)

**Class 1 Employee SSC Rates (2026)**

| Category | Who | Weekly Rate | Max Weekly | Annual Max |
| --- | --- | --- | --- | --- |
| A | Under 18, wage ≤ EUR 229.44 | EUR 6.62 flat | EUR 6.62 | EUR 344.24 |
| B | Age 18+, wage ≤ EUR 229.44 | EUR 22.94 flat (or 10%) | EUR 22.94 | EUR 1,192.88 |
| C1 (born ≤ 1961) | Wage EUR 229.45 -- 490.38 | 10% of basic weekly wage | -- | -- |
| D1 (born ≤ 1961) | Wage ≥ EUR 490.39 | EUR 49.04 | EUR 49.04 | EUR 2,550.08 |
| C2 (born ≥ 1962) | Wage EUR 229.45 -- 559.30 | 10% of basic weekly wage | -- | -- |
| D2 (born ≥ 1962) | Wage ≥ EUR 559.31 | EUR 55.93 | EUR 55.93 | EUR 2,908.36 |

- **Monthly to weekly conversion** — For monthly-paid employees, convert to weekly equivalent: monthly salary x 12 / 52.

## Section 4 -- Social Security -- Employer Contributions

Employer SSC mirrors employee SSC exactly -- 10% of basic weekly wage with identical caps. The employer also pays the Maternity Trust Fund levy.

### Employer Contributions (2026)

**Employer Contributions (2026)**

| Contribution | Rate | Ceiling | Notes |
| --- | --- | --- | --- |
| Class 1 SSC (employer) | 10% of basic weekly wage | Same caps as employee (D2: EUR 55.93/week) | Matches employee pound-for-pound |
| Maternity Trust Fund | 0.30% of basic weekly wage | Follows SSC wage bands | Max EUR 1.68/week (D2 category) |

**Total employer cost per high-earning employee (born ≥ 1962):** EUR 55.93 SSC + EUR 1.68 Maternity = EUR 57.61 per week (EUR 2,995.72/year).

## Section 5 -- Minimum Wage and Overtime

### National Minimum Wage (2026)

**National Minimum Wage (2026)**

| Category | Weekly Amount |
| --- | --- |
| Age 18+ | EUR 229.44 |
| Age 17 | EUR 222.66 |
| Under 17 | EUR 219.82 |

- **Part-time** — Part-time: pro rata at weekly NMW / 40 hours = EUR 5.74/hour (age 18+).

### Statutory Bonuses (Mandatory)

**Statutory Bonuses (Mandatory)**

| Bonus | Amount | Payment Schedule | Taxable? |
| --- | --- | --- | --- |
| Government Bonus | EUR 135.10 per half-year | June and December | Yes |
| Weekly Allowance | EUR 121.16 per half-year | June and December | Yes |
| COLA (Cost of Living Adjustment) | EUR 512.52 per year (2026) | Quarterly (EUR 128.13 per quarter) | No -- tax-exempt |

### Overtime

**Overtime**

| Rule | Detail |
| --- | --- |
| Standard weekly hours | 40 hours (per EIRA and most WROs) |
| Overtime rate (no WRO) | 1.5x normal hourly rate for hours above 40/week (averaged over 4 weeks) |
| Maximum average | 48 hours/week (averaged over 17 weeks); opt-out requires written consent |
| Weekend/public holiday premium | 1.5x applies equally -- no separate Sunday or holiday multiplier in general law |

Wage Regulation Orders (WROs) for specific sectors may specify different overtime rates and thresholds.

## Section 6 -- Mandatory Benefits

### Annual Leave

**Annual Leave**

| Entitlement | Detail |
| --- | --- |
| Full-time (40 hrs/week) | 192 hours (24 days) per calendar year |
| Public holidays falling on non-work days | Additional compensatory day per occurrence |
| Minimum non-substitutable | 4 weeks (160 hours) -- cannot be bought out except on termination |
| Accrual | 2 days per month from employment start |
| Part-time | Pro rata |

Malta has 14 public holidays per year. In practice, total paid time off can reach 28--30 days.

### Sick Leave

**Sick Leave**

| Entitlement | Detail |
| --- | --- |
| Full-time (no WRO) | 2 working weeks per calendar year on full pay |
| WRO-covered sectors | 15--30 days depending on WRO |
| Deduction | Employer pay is reduced by the SSA sickness benefit amount |
| Medical certificate | Required; within 1 week for absences > 7 days |

### Maternity Leave

**Maternity Leave**

| Entitlement | Detail |
| --- | --- |
| Duration | 18 weeks uninterrupted |
| Employer-paid | First 14 weeks at basic salary rate |
| Government-paid | Final 4 weeks at EUR 213.54/week (Maternity Leave Benefit) |
| Notice | 4 weeks written notice to employer before start |
| Mandatory post-birth | Minimum 6 weeks immediately after delivery |

### Other Statutory Leave (2026)

**Other Statutory Leave (2026)**

| Leave Type | Duration |
| --- | --- |
| Birth Leave (father/partner) | 10 working days on full pay |
| Parental Leave (unpaid) | 4 months per parent (per child, until age 8) |
| Bereavement Leave | 2 days |
| Parental Bereavement Leave (child < 18 death) | 7 working days (new from 2026) |
| Miscarriage Leave | 7 working days for both parents (new from 2026) |
| Urgent Family Leave | 1 day per event (force majeure) |
| Marriage Leave | 2 days |

## Section 7 -- Payslip Requirements

Malta's Itemised Payslip Regulations (LN 274 of 2018 under EIRA Cap. 452) mandate the following.

### Mandatory Payslip Fields

**Mandatory Payslip Fields**

| Field | Required |
| --- | --- |
| Employer name and address | Yes |
| Employee name and designation | Yes |
| Breakdown of total wages paid | Yes |
| Normal hours worked | Yes |
| Overtime hours worked | Yes |
| Annual leave hours used and remaining balance | Yes |
| Sick leave hours used | Yes |
| Breakdown of bonuses | Yes |
| Breakdown of allowances or commissions | Yes |
| Deductions (FSS tax, SSC, other) | Yes |

### Delivery

- Must be provided before or on the day wages are due
- Paper or electronic format permitted
- Non-compliance fine: EUR 500 -- EUR 1,165

## Section 8 -- Filing Obligations

### Monthly

**Monthly**

| Form | Purpose | Deadline |
| --- | --- | --- |
| FS5 (Payer's Monthly Payment Advice) | Company-level summary of gross emoluments, FSS tax withheld, and SSC | 15 days after month-end |
| Payment of FSS tax + SSC to CFR | Remittance of withheld amounts | Same as FS5 deadline |

### Annual

**Annual**

| Form | Purpose | Deadline |
| --- | --- | --- |
| FS3 (Payee Statement of Earnings) | Individual employee annual earnings, tax, and SSC statement | By mid-March of following year |
| FS7 (Payer's Annual Reconciliation) | Reconciliation of all monthly FS5 payments against total FS3s | 31 March of following year (electronic) |

### Employee-Level

**Employee-Level**

| Item | Detail |
| --- | --- |
| FS4 (Payee Status Declaration) | Employee submits to employer (and MTCA) to declare tax computation status. Updated when marital/child status changes. |

## Section 9 -- Common Payroll Patterns

### Typical Bank Statement Descriptions (Salary Credits)

**Typical Bank Statement Descriptions (Salary Credits)**

| Pattern | Classification |
| --- | --- |
| PAGA, SALARY, STIPENDJU | Net salary payment |
| EMPLOYER [name] TRANSFER, WAGES | Net salary payment |
| BONUS GVERN, GOVT BONUS | Statutory bonus (June/December) |
| COLA, COST OF LIVING | COLA payment (quarterly, tax-exempt) |
| SSC REFUND | SSC adjustment -- not income |

### Typical Employer Debit Patterns

**Typical Employer Debit Patterns**

| Pattern | Classification |
| --- | --- |
| CFR FSS, MTCA FSS, TAX REMITTANCE | FSS tax + SSC payment to CFR |
| SSC EMPLOYER, CLASS 1 | Employer SSC contribution |
| MATERNITY FUND, MTF | Maternity Trust Fund levy |
| NET WAGES, SALARY RUN, PAYROLL | Salary disbursement to employees |

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Scenario | Skill to Use |
| --- | --- |
| Employee payroll (FSS + SSC) | **This skill (malta-payroll.md)** |
| Self-employed income tax (TA24/TA22) | malta-income-tax.md |
| Self-employed SSC (Class 2) | malta-ssc.md |
| Malta VAT returns | malta-vat-return.md |
| Malta bookkeeping | malta-bookkeeping.md |
| Employer corporate tax | malta-corporate-tax.md |

### Key Handoff Points

- **Payroll → Bookkeeping:** Gross wages, employer SSC, and Maternity Fund are expenses; FSS tax and employee SSC are liabilities until remitted.
- **Payroll → Income Tax:** The FS3 annual statement feeds into the employee's personal TA24 return. Employment income goes to Box 4 if the employee is also self-employed.
- **Payroll → SSC:** Class 1 contributions paid through payroll count toward the employee's pension entitlement. Separate from Class 2 (self-employed).

## PROHIBITIONS

- NEVER process payroll without a valid FS4 status declaration from the employee
- NEVER apply single rates to a married employee or vice versa without confirming FS4 status
- NEVER compute SSC on total remuneration -- use basic weekly wage only (exclude overtime premiums, bonuses above basic)
- NEVER forget the Maternity Trust Fund levy on top of employer SSC
- NEVER pay COLA as taxable income -- it is tax-exempt
- NEVER omit statutory bonuses (Government Bonus + Weekly Allowance) from payroll
- NEVER issue a payslip missing any of the mandatory fields under LN 274/2018
- NEVER miss the FS5 deadline (15 days after month-end) -- penalties apply
- NEVER present payroll computations as definitive -- always label as estimated and direct to a warranted accountant

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a warranted accountant in Malta) before implementation.

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
