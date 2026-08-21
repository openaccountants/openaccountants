---
name: canada-payroll
description: Use this skill whenever asked about Canadian payroll, source deductions, CPP contributions, EI premiums, or employer obligations in Canada. Trigger on phrases like "source deductions", "CPP", "Canada Pension Plan", "CPP2", "EI", "employment insurance", "T4", "TD1", "payroll deductions", "CRA payroll", "remittance", "ROE", "record of employment", "statutory holiday pay", "vacation pay Canada", "minimum wage Canada", "provincial tax", "payroll Canada", "PD7A", "remitter type", or any question about running payroll in Canada. This skill covers federal rules; Quebec (QPP/QPIP) differences are noted but not fully detailed. ALWAYS read this skill before processing any Canadian payroll work.
version: 1.0
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Edgar Lautsyus
review_status: current
depends_on: - payroll-workflow-base
category: payroll
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Canada Payroll

## Canada -- Payroll Skill v1.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Nathan Wiebe** on 2026-06-21.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Payroll

- **$0–$58,523** — 14%  _(Bill C-4; CRA — 2026 payroll deductions tables (T4032) — verify on canada.ca)_
- **$58,523–$117,045** — 20.5%  _(CRA T4032 2026)_
- **$117,045–$181,440** — 26%  _(CRA T4032 2026)_
- **$181,440–$258,482** — 29%  _(CRA T4032 2026)_
- **$258,482+** — 33%  _(CRA T4032 2026)_
- **BPA (2026)** — $16,452 (up to $181,440); $14,829 (above $258,482)  _(CRA — Basic personal amount 2026 — canada.ca (verify))_
- **CPP employee rate** — 5.95%  _(CRA — CPP rates — canada.ca)_
- **CPP employer rate** — 5.95% (matches employee)  _(Canada Pension Plan Act s.9)_
- **YMPE (2026)** — $74,600  _(CRA — CPP contribution rates — canada.ca (verify 2026 announcement))_
- **CPP2 employee rate** — 4.00%  _(CRA — CPP rates — canada.ca)_
- **YAMPE (2026)** — $85,000  _(CRA — CPP contribution rates — canada.ca (verify 2026 announcement))_
- **Basic exemption** — $3,500  _(Canada Pension Plan Act s.20)_
- **Max CPP contribution (EE, 2026)** — $4,230.45  _(CRA — CPP contribution rates — canada.ca (verify 2026 YMPE))_
- **Max CPP2 contribution (EE, 2026)** — $416.00  _(CRA — CPP contribution rates — canada.ca (verify 2026 YAMPE))_
- **EI employee rate (non-QC)** — 1.63%  _(ESDC — EI premium rates — canada.ca (verify 2026))_
- **EI employer rate** — 2.282% (1.4× employee)  _(Employment Insurance Act s.68)_
- **Max insurable earnings** — $68,900  _(ESDC — EI premium rates — canada.ca (verify 2026))_
- **Max EE premium** — $1,123.07  _(ESDC — EI premium rates — canada.ca)_
- **Max ER premium** — $1,572.30  _(ESDC — EI premium rates — canada.ca)_
- **EI QC employee rate** — Quebec EI rate 1.30% for 2026  _(ESDC — EI premium rates — canada.ca (verify 2026 Quebec rate))_
- **Ontario EHT threshold** — $1,000,000  _(Employer Health Tax Act (Ontario))_
- **Ontario EHT rate** — 0.98%–1.95%  _(Employer Health Tax Act (Ontario) s.2)_
- **BC EHT threshold** — $1,000,000  _(Employer Health Tax Act (BC))_
- **BC EHT rate** — BC EHT rate is 1.95% if remuneration exceeds $1,500,000. If remuneration is between $1 million and $1.5 million, the rate is 5.85% of remuneration exceeding $1,000,000.  _(Employer Health Tax Act (BC))_
- **Federal** — Federal minimum wage $18.15/hr as of April 2026. Indexed to CPI and updated each April.  _(Canada Labour Code s.178; ESDC — Minimum wage — canada.ca)_
- **Ontario** — Ontario minimum wage $17.60/hr As of October 1, 2025  _(Employment Standards Act, 2000 (ON); Ontario Ministry of Labour)_
- **British Columbia** — BC minimum wage $18.25/hr as of June 1, 2026  _(Employment Standards Act (BC); BC government)_
- **Alberta** — $15.00/hr  _(Employment Standards Code (AB); Alberta government)_
- **Federal — after 1 year** — 4% (2 weeks)  _(Canada Labour Code s.184)_
- **Federal — after 5 years** — 6% (3 weeks)  _(Canada Labour Code s.184)_
- **T4 slips to employees** — T4 slips: last day of February following the calendar year. Next business day if falls on weekend.  _(ITA s.153(1); CRA — T4 guide)_
- **ROE** — Within 5 calendar days of earnings interruption  _(Employment Insurance Act s.19; Service Canada)_
- **Late T4 penalty** — Late T4 penalty: minimum $100, maximum $7,500. The daily penalty amount depends on the number of slips that are filed late. See table below.  _(ITA s.162(7.01))_

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Canada |
| Currency | CAD ($) only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Income Tax Act (federal); Canada Pension Plan Act; Employment Insurance Act; Canada Labour Code (federal employees) |
| Tax authority | Canada Revenue Agency (CRA) |
| Reporting system | T4/T4A information returns; PD7A remittance voucher |
| Pay frequency | Biweekly (most common), semi-monthly, monthly, weekly |
| Employer registration | Business Number (BN) + payroll program account (RP) via CRA |
| Provincial variation | Each province/territory has its own income tax brackets, ESA, and minimum wage |
| Validated by | Verified by Nathan Wiebe on 2026-06-21 |
| Skill version | 1.0 |

## Section 2 -- Income Tax Withholding (Source Deductions)

Employers withhold both federal and provincial/territorial income tax from each pay. CRA publishes payroll deduction tables (T4032) and formulas (T4127) annually.

### Federal Tax Brackets (2026)

**Federal Tax Brackets (2026)**

| Taxable Income (CAD) | Rate |
| --- | --- |
| 0 -- 58,523 | 14% |
| 58,523 -- 117,045 | 20.5% |
| 117,045 -- 181,440 | 26% |
| 181,440 -- 258,482 | 29% |
| 258,482+ | 33% |

- **Lowest bracket rate change** — The lowest bracket rate was reduced from 15% to 14% effective for the 2026 tax year (enacted via 2025 tax reform).

### Federal Basic Personal Amount (BPA) -- 2026

**Federal Basic Personal Amount (BPA) -- 2026**

| Income Level | BPA (CAD) |
| --- | --- |
| Up to $181,440 | $16,452 |
| $181,440 -- $258,482 | Claws back to $14,829 |
| Above $258,482 | $14,829 |

### Provincial/Territorial Tax

Each province has its own tax brackets applied on top of federal tax. The employer determines the applicable province based on the employee's **province of employment** (where they physically report to work). Employees complete a federal TD1 and a provincial TD1 form.

### Key Provincial Top Marginal Rates (Combined Federal + Provincial, 2026)

**Key Provincial Top Marginal Rates (Combined Federal + Provincial, 2026)**

| Province | Top Combined Rate (approx.) |
| --- | --- |
| Ontario | ~53.5% |
| British Columbia | ~53.5% |
| Alberta | ~48.0% |
| Quebec | ~53.3% |
| Manitoba | ~50.4% |
| Saskatchewan | ~47.5% |

## Section 3 -- Social Security: Employee Deductions

### Canada Pension Plan (CPP) -- 2026

**Canada Pension Plan (CPP) -- 2026**

| Component | Rate (Employee) | Ceiling | Maximum Contribution |
| --- | --- | --- | --- |
| CPP base + first additional | 5.95% | YMPE $74,600 (less $3,500 basic exemption) | $4,230.45 |
| CPP2 (second additional) | 4.00% | Earnings between YMPE $74,600 and YAMPE $85,000 | $416.00 |

- **Basic exemption** — $3,500/year (pro-rated per pay period)
- **CPP age eligibility** — CPP applies to employees aged 18--69 (mandatory 18--65; elective 65--70)
- **CPP2** — CPP2 is a second tier introduced in 2024 on earnings between the first and second ceilings

### Employment Insurance (EI) -- 2026

**Employment Insurance (EI) -- 2026**

| Item | Rate | Maximum Insurable Earnings | Maximum Annual Premium |
| --- | --- | --- | --- |
| Employee (Canada except Quebec) | 1.63% | $68,900 | $1,123.07 |
| Employee (Quebec -- reduced for QPIP) | 1.30% | $68,900 | $902.59 |

### Quebec Differences

Quebec employees pay QPP instead of CPP (rate 6.40% for 2026) and QPIP (Quebec Parental Insurance Plan) at 0.494%. These are deducted separately.

## Section 4 -- Social Security: Employer Contributions

### CPP Employer Contributions -- 2026

**CPP Employer Contributions -- 2026**

| Component | Rate | Maximum |
| --- | --- | --- |
| CPP base + first additional | 5.95% (matches employee) | $4,230.45 |
| CPP2 | 4.00% (matches employee) | $416.00 |

- **Employer CPP matching** — Employer CPP contributions mirror the employee amount exactly (1:1 match).

### EI Employer Contributions -- 2026

**EI Employer Contributions -- 2026**

| Item | Rate | Maximum |
| --- | --- | --- |
| Employer (Canada except Quebec) | 2.282% (1.4× employee rate) | $1,572.30 |
| Employer (Quebec) | 1.834% (1.4× employee rate) | $1,264.03 |

- **Employer EI multiplier** — The employer pays 1.4 times the employee EI premium. Employers may apply for an EI premium reduction if they have a qualifying short-term disability plan.

### Workers' Compensation

Provincial/territorial requirement. Premiums vary by industry classification and province. Typically $0.50--$3.00 per $100 of insurable earnings for office workers; higher for construction/manufacturing.

### Employer Health Tax (Select Provinces)

**Employer Health Tax (Select Provinces)**

| Province | Threshold | Rate |
| --- | --- | --- |
| Ontario (EHT) | $1,000,000 | 0.98%--1.95% |
| British Columbia (EHT) | $1,000,000 | 1.95% (above $1,500,000); 5.85% of remuneration exceeding $1,000,000 (between $1M–$1.5M) |
| Manitoba (HE levy) | $2,250,000 | 2.15%--4.3% |
| Quebec (HSF) | All payroll | 1.65%--4.26% |

## Section 5 -- Minimum Wage and Overtime

### Federal Minimum Wage

- **Federal minimum wage** — $18.15/hour (as of April 2026, indexed annually to CPI). Applies to federally regulated industries only (banking, telecom, interprovincial transport).

### Select Provincial Minimum Wages (2026)

**Select Provincial Minimum Wages (2026)**

| Province | Rate (CAD/hour) |
| --- | --- |
| Ontario | $17.60 |
| British Columbia | $18.25 |
| Alberta | $15.00 |
| Quebec | $16.10 |
| Manitoba | $15.80 |
| Saskatchewan | $15.00 |

Rates are approximate and subject to annual adjustments.

### Overtime

**Overtime**

| Jurisdiction | Threshold | Rate |
| --- | --- | --- |
| Federal | 8 hrs/day or 40 hrs/week | 1.5× regular rate |
| Ontario | 44 hrs/week | 1.5× regular rate |
| British Columbia | > 8 hrs/day or > 40 hrs/week | 1.5×; > 12 hrs/day = 2× |
| Alberta | > 8 hrs/day or > 44 hrs/week | 1.5× regular rate |
| Quebec | > 40 hrs/week | 1.5× regular rate |

## Section 6 -- Mandatory Benefits

### Vacation Pay

**Vacation Pay**

| Jurisdiction | After 1 Year | After 5+ Years |
| --- | --- | --- |
| Federal | 4% (2 weeks) | 6% (3 weeks) |
| Ontario | 4% (2 weeks) | 6% (3 weeks after 5 years) |
| British Columbia | 4% (2 weeks) | 6% (3 weeks after 5 years) |
| Alberta | 4% (2 weeks) | 6% (3 weeks after 5 years) |
| Quebec | 4% (2 weeks) initially; 6% after 3 years | 6% (3 weeks) |
| Saskatchewan | 5.77% (3 weeks) | 7.69% (4 weeks after 10 years) |

### Statutory / Public Holidays

9 federal statutory holidays. Provincial holidays vary (6--10 per province). Employees are entitled to the statutory holiday with pay or premium pay (typically 1.5× or time off in lieu) if they work on the holiday.

### Sick Leave

**Sick Leave**

| Jurisdiction | Paid Days | Unpaid Days |
| --- | --- | --- |
| Federal | 10 paid (after 30 days of service) | -- |
| Ontario | 3 paid | -- |
| British Columbia | 5 paid | 3 unpaid |
| Quebec | 2 paid (after 3 months) | 24 unpaid |
| Alberta | 0 paid | 16 unpaid |

### Maternity / Parental Leave (EI Benefits)

**Maternity / Parental Leave (EI Benefits)**

| Benefit | Duration | EI Rate |
| --- | --- | --- |
| Maternity (birth parent only) | 15 weeks | 55% of insurable earnings (max ~$695/week for 2026) |
| Standard parental | 35 weeks | 55% of insurable earnings |
| Extended parental | 61 weeks | 33% of insurable earnings |

- **Top-up / waiting period** — Employers are not required to top up EI benefits, though many do contractually. The one-week EI waiting period is currently waived (suspended).

### Group Benefits

Not legally mandated, but most Canadian employers provide extended health, dental, life insurance, and short/long-term disability as part of competitive compensation.

## Section 7 -- Payslip Requirements

The Canada Labour Code (federal) and provincial Employment Standards Acts require employers to provide a pay statement each pay period.

### Mandatory Payslip Contents

- Pay period dates
- Gross earnings
- All deductions itemised (CPP, EI, federal tax, provincial tax, other)
- Net pay
- Hours worked (if hourly)
- Rate of pay
- Overtime hours and pay (if applicable)
- Vacation pay (if applicable)

### Additional Requirements by Province

Ontario requires the employer's name and address, the employee's name, and the pay period. Quebec requires similar plus contribution details. Most provinces align with the above minimum.

## Section 8 -- Filing Obligations

### Remittance of Source Deductions

**Remittance of Source Deductions**

| Remitter Type | Threshold (Avg Monthly Withholding) | Due Date |
| --- | --- | --- |
| Quarterly | < $1,000 (new, perfect compliance) | 15th of month after quarter end |
| Regular | < $25,000 | 15th of following month |
| Threshold 1 accelerated | $25,000 -- $99,999.99 | Twice monthly (15th and month-end) |
| Threshold 2 accelerated | ≥ $100,000 | Up to 4 times per month (within 3 business days of pay date) |

### Year-End Filing (T4)

**Year-End Filing (T4)**

| Task | Deadline |
| --- | --- |
| T4 slips to employees | Last day of February (next business day if falls on weekend) |
| T4 Summary to CRA | Last day of February |
| T4A slips (contract/other income) | Last day of February |
| Quebec: RL-1 slips to employees and Revenu Québec | Last day of February |

### Record of Employment (ROE)

- **ROE issuance** — Must be issued within 5 calendar days of an interruption in earnings (layoff, leave, termination, etc.). Filed electronically via ROE Web.

### Penalties

**Penalties**

| Violation | Penalty |
| --- | --- |
| Late remittance | 3% (1--3 days late) to 10% (7+ days late) + arrears interest |
| Failure to deduct | Employer liable for undeducted amounts + 10% penalty |
| Late T4 filing | Min $100, max $7,500; daily penalty depends on number of slips filed late |
| Failure to issue ROE | Up to $2,000 fine and/or 6 months imprisonment |

## Section 9 -- Common Payroll Patterns

### Pattern 1 -- Biweekly Employee (Ontario)

Annual salary $75,000. Paid biweekly (26 pay periods).

1. Gross per period: $75,000 ÷ 26 = $2,884.62
2. CPP: ($2,884.62 - $134.62 exemption) × 5.95% = $163.60
3. CPP2: if annualised earnings exceed $74,600, additional 4% applies on the excess (calculated cumulatively)
4. EI: $2,884.62 × 1.63% = $47.02
5. Federal tax: per T4032 table for biweekly pay
6. Ontario provincial tax: per T4032-ON table
7. Employer CPP: $163.60 (matches employee)
8. Employer EI: $47.02 × 1.4 = $65.83

### Pattern 2 -- Employee Reaching CPP Maximum

Employee paid $80,000 semi-monthly ($3,333.33/period). By period 11, cumulative pensionable earnings exceed YMPE $74,600. CPP deductions stop at $4,230.45. CPP2 continues until YAMPE $85,000 is reached (max $416.00). Payroll software tracks cumulative contributions and stops deducting when maximums are reached.

### Pattern 3 -- Vacation Pay Payout

Employee earning $52,000/year with 4% vacation pay. Vacation pay accrues: $52,000 × 4% = $2,080/year. Can be paid on each cheque (added to gross, subject to all deductions) or accrued and paid when vacation is taken.

### Pattern 4 -- Termination with ROE

Employee terminated without cause. Final pay includes:
- Outstanding regular wages through last day
- Accrued vacation pay (mandatory payout)
- Termination pay (if applicable under ESA -- typically 1 week per year of service)
- Severance (Ontario: 1 week per year if 5+ years and employer payroll ≥ $2.5M)

Issue ROE within 5 days via ROE Web. Code M (dismissal) or other applicable code.

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Skill | Interaction |
| --- | --- |
| payroll-workflow-base | Provides generic payroll processing steps; this skill adds Canadian-specific rules |
| canada-bookkeeping | Payroll journals: salaries + ER CPP/EI + ER EHT/WCB to P&L; net pay + source deductions payable to BS |
| canada-corporate-tax | Employer CPP/EI and provincial health taxes are deductible business expenses |
| canada-gst-hst | No GST/HST on wages; but taxable benefits may trigger GST/HST |

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
