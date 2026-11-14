---
name: hk-mpf
description: "Use this skill whenever asked about Hong Kong Mandatory Provident Fund (MPF) contributions in 2026 (year of assessment 2026/27). Trigger on phrases like \"MPF\", \"Mandatory Provident Fund\", \"強積金\", \"employer contribution Hong Kong\", \"employee contribution HK\", \"MPF self-employed\", \"TVC\", \"voluntary contributions\", \"MPF cap\", \"relevant income MPF\", \"MPFA\", \"eMPF\", or any question about MPF contribution rates, caps, voluntary contributions, tax deductions, the end of the offsetting arrangement and self-employed obligations. It gives the 5% rates, the HKD 7,100 and HKD 30,000 relevant income levels, the 10th-day contribution day and the 60-day enrolment rule. Built from the law, not reviewed by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/hk-mpf"
  jurisdiction: "HK"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Hong Kong Mandatory Provident Fund (強制性公積金), 2026

> **General reference only.** Built from the law, not reviewed by an accountant. Do not file, pay or take a position on it without review by a qualified professional or MPF intermediary in Hong Kong.

## Who this applies to

Except for exempt persons, employees and self-employed persons aged 18 to 64 must join an MPF scheme under the Mandatory Provident Fund Schemes Ordinance (MPFSO), Cap. 485. Regulator: Mandatory Provident Fund Schemes Authority (MPFA, 積金局). Contributions, enrolment and records now run through the eMPF Platform. Currency: HKD.

| Category | MPF required | Notes |
| --- | --- | --- |
| Regular employees aged 18 to 64, employed 60 days or more | Yes | Full-time and part-time alike |
| Casual employees in construction or catering (day-to-day or under 60 days) | Yes, Industry Scheme | Enrol within the first 10 days if no account in the same Industry Scheme |
| Self-employed persons aged 18 to 64 | Yes | Open an SEP account within 60 days |
| Under 18 or over 65 | No | May contribute voluntarily |
| Exempt persons (for example domestic employees, members of exempted ORSO schemes, certain expatriates for the first 13 months, civil servants on pension terms) | No | Exemption categories per MPFA coverage page |

Salaries tax deduction for contributions: `hk-salaries-tax`.

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| Employer mandatory contribution | 5% of relevant income | Capped at the maximum relevant income | https://www.mpfa.org.hk/en/mpf-system/mandatory-contributions/employees |
| Employee mandatory contribution | 5% of relevant income | None if monthly relevant income is below the minimum | same |
| Minimum relevant income, monthly paid | HKD 7,100 a month | Below it: employer pays 5%, employee pays nothing | same |
| Maximum relevant income, monthly paid | HKD 30,000 a month | Contributions above it: HKD 1,500 each | same |
| Maximum mandatory contribution, each party | HKD 1,500 a month | Relevant income above HKD 30,000 | same |
| Daily levels (non-monthly wage periods) | Minimum HKD 280 a day; maximum HKD 1,000 a day | Times the days in the wage period (weekly: 1,960 and 7,000) | same |
| Enrolment deadline | Within the first 60 days of employment | Calendar days; next working day if the 60th falls on a Saturday or holiday | https://www.mpfa.org.hk/en/mpf-system/enrolment-and-termination |
| Contribution day, monthly paid employees | 10th day of the following month | First contribution: the 10th after the month in which the 60th day falls | https://www.mpfa.org.hk/en/mpf-system/voluntary-contributions-or-tax-deductible-voluntary-contributions |
| Failure to enrol | Fine up to HKD 350,000 and 3 years' imprisonment | Employer offence | https://www.mpfa.org.hk/en/mpf-system/enrolment-and-termination |
| Pay records to employees | Within 7 working days after contributing | Employer duty | https://www.mpfa.org.hk/en/enforcement/enforcement-against-employers |
| TVC and QDAP salaries tax deduction | Up to HKD 60,000 a year combined | Tax-deductible voluntary contributions | https://www.mpfa.org.hk/en/mpf-system/voluntary-contributions-or-tax-deductible-voluntary-contributions |
| Mandatory contributions salaries tax deduction | Up to HKD 18,000 a year | Employee or SEP | https://www.ird.gov.hk/eng/pdf/2026/BriefGuide20252026.pdf |
| Offsetting arrangement abolished | From 1 May 2025 (transition date) | Employees ceasing employment on or after that date; no retrospective effect | https://www.mpfa.org.hk/en/mpf-system/long-service-and-severance-payments |
| Withdrawal age | 65 | Earlier only on statutory grounds | https://www.mpfa.org.hk/en/mpf-system/withdrawal-of-mpf |

## The base

### Relevant income (MPFSO s. 2)

- **Included:** wages, salary, overtime pay; commission, bonus; leave pay (annual, sick, maternity, paternity); fees, tips; end-of-year payments, gratuities.
- **Excluded:** severance and long service payments under the Employment Ordinance; non-cash housing benefit; reimbursement of expenses. Non-cash benefits (housing, company car) are not relevant income unless commutable to cash at the employee's option.

### Computation, employee

1. Relevant income for the wage period.
2. Below HKD 7,100 a month: employer 5%, employee 0.
3. HKD 7,100 to 30,000: each pays 5%.
4. Above HKD 30,000: each pays HKD 1,500.
5. Pay by the contribution day through the eMPF Platform.

### Self-employed persons (SEP)

| Rule | Detail |
| --- | --- |
| Mandatory contribution | 5% of relevant income (net self-employment income) |
| Frequency | Monthly or yearly, chosen on enrolment |
| Monthly | Contribution day as specified by the SEP (for example the last day of each month) |
| Yearly | Contribution day is the last day of the scheme's financial year |
| Cap | 5% of the maximum relevant income: HKD 1,500 a month, HKD 18,000 a year |
| Below the minimum | No mandatory contribution |

Correction: the old file said SEP contributions were due "within 30 days after the end of the contribution period or financial year"; the MPFA page sets the contribution day as above.

### Voluntary contributions

| Feature | TVC (tax-deductible voluntary contribution) | Other voluntary contributions |
| --- | --- | --- |
| Account | Special TVC account | Regular account (employer or employee voluntary) |
| Tax deduction | Up to HKD 60,000 a year with QDAP premiums | None |
| Withdrawal | At 65, or early on statutory grounds | Per scheme rules |
| Vesting | Immediate | Employer voluntary contributions may vest by scale |

Tax benefit of TVC = contribution times the marginal salaries tax rate (2% to 17%, or 15% under the standard rate).

### Vesting

Employee and employer mandatory contributions vest immediately; employer voluntary contributions may follow a vesting scale under scheme rules.

### Edge cases

- **Multiple Employments**: Each employer must contribute separately; Employee contributes 5% to each scheme; Combined employee contributions may exceed $18,000/year tax deduction cap; Tax deduction still capped at $18,000 for mandatory across all employments
- **Employee Becomes Self-Employed**: Employee account becomes "preserved" on leaving employment; Self-employed opens new self-employed account; May consolidate accounts into one personal account; Previous employer contributions preserved until qualifying event
- **Part-Time / Multiple Part-Time Jobs**: Each employer with ≥60 days employment must enrol; Income threshold ($7,100) applies per employment separately; Part-time worker earning $5,000 from employer A and $4,000 from employer B: Employer A: contributes 5% × $5,000 = $250; employee contributes $0 (below threshold); Employer B: contributes 5% × $4,000 = $200; employee contributes $0 (below threshold)
- **Non-Monetary Benefits**: Non-cash benefits (housing, company car) are NOT relevant income for MPF; Only monetary payments count towards MPF calculation; Exception: if benefit is commutable to cash at employee's option, it may be relevant income


**End of offsetting (from 1 May 2025).** Employers can no longer use the MPF from employer mandatory contributions to offset severance or long service payments for service from 1 May 2025. For employees who started before and leave on or after that date, the employer may still use employer mandatory contributions (including accrued returns) to offset the part of the payment for service before 1 May 2025, and employer voluntary contributions for any part. The Labour Department's Subsidy Scheme for Abolition of MPF Offsetting Arrangement shares some of the employer cost. Correction: the old file said offsetting was still permitted in the "current position (2024/25)".

### Conservative defaults

| Ambiguity | Default |
| --- | --- |
| Unknown relevant income | Treat as above the HKD 7,100 minimum until confirmed |
| Unknown start date | Count 60 calendar days from the first day of employment |
| Self-employed or employee | Check the control test; if ambiguous, treat as employee |
| TVC or employer voluntary | Only TVC is tax-deductible |

## Deadlines and filing

| Obligation | Deadline |
| --- | --- |
| Enrol new employee | Within the first 60 days of employment |
| Pay contributions (monthly paid) | On or before the 10th day of the following month |
| Pay records | Within 7 working days after contributing |
| Notify changes of particulars to the eMPF Platform | Within 30 days |
| SEP account | Within 60 days of becoming self-employed |
| SEP annual benefit statement (issued by eMPF) | Within three months after the scheme's financial period |

## Penalties and interest

Failure to enrol an employee: fine up to HKD 350,000 and imprisonment for three years. Failure to pay contributions on or before the contribution day is an offence and the MPFA adds a contribution surcharge (the 5% rate and the other fines in the old file, HKD 350,000 for non-payment and deductions from wages, HKD 50,000 and 6 months for an SEP who fails to join, are not confirmed on an official page in this pass).

## Cross-border points

- Expatriates entering Hong Kong for employment may be exempt for the first 13 months; after that the employer must enrol them within 60 days.
- Permanent departure from Hong Kong is a statutory ground for early withdrawal (statutory declaration and evidence).
- Members of overseas retirement schemes may be exempt persons; check the MPFA list.

## Two worked examples that recompute

**Example 1: three employees, monthly contributions for 2026.** A earns HKD 25,000: employer 1,250, employee 1,250. B earns 80,000: each capped at 1,500. C earns 6,000: employer 300, employee nothing. Total employer cost: 3,050 a month; employee deductions: 2,750.

```oa-check
name: HK 2026 MPF mandatory contributions, three pay levels
inputs:
  a: 25000
  b: 80000
  c: 6000
steps:
  - er_a: min(a, 30000) * 0.05
  - er_b: min(b, 30000) * 0.05
  - er_c: min(c, 30000) * 0.05
  - ee_a: min(a, 30000) * 0.05
  - ee_b: min(b, 30000) * 0.05
  - ee_c: 0
  - employer_total: er_a + er_b + er_c
  - employee_total: ee_a + ee_b + ee_c
expected:
  employer_total: 3050
  employee_total: 2750
```

**Example 2: decision, put HKD 60,000 into TVC.** A taxpayer on the progressive rates with net chargeable income well above HKD 200,000 (marginal 17%) saves HKD 10,200 of salaries tax by contributing the full HKD 60,000 as TVC. A taxpayer on the 15% standard rate saves HKD 9,000. The money is locked until 65 (or a statutory ground); the deciding figures are the marginal rate and whether the money is needed before 65. A self-employed person with HKD 500,000 profit pays mandatory 18,000 (5% of 30,000 times 12) and can add up to 60,000 TVC: 78,000 deductible in total.

```oa-check
name: HK 2026/27 TVC tax saving at 17% and 15%
inputs:
  tvc: 60000
steps:
  - saving_progressive: tvc * 0.17
  - saving_standard: tvc * 0.15
  - sep_mandatory: 30000 * 0.05 * 12
  - sep_total_deductible: sep_mandatory + tvc
expected:
  saving_progressive: 10200
  saving_standard: 9000
  sep_mandatory: 18000
  sep_total_deductible: 78000
```

## Ask the client first

1. Employee or self-employed; age; start date.
2. Monthly relevant income, and wage period if not monthly.
3. Any exemption (domestic employee, ORSO scheme, expatriate within 13 months).
4. For a leaver: start date and whether severance or long service payment is due (offsetting rules).
5. Voluntary contributions wanted, and the marginal salaries tax rate.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| MPFA, mandatory contributions for employees. Read for the 5% rates, the 7,100 and 30,000 levels, HKD 1,500 cap and daily levels | https://www.mpfa.org.hk/en/mpf-system/mandatory-contributions/employees | 2026-11-14 |
| MPFA, enrolment and termination. Read for the 60-day rule, Industry Scheme 10 days and the HKD 350,000 fine | https://www.mpfa.org.hk/en/mpf-system/enrolment-and-termination | 2026-11-14 |
| MPFA, MPF coverage. Read for ages 18 to 64, casual employees and exemptions | https://www.mpfa.org.hk/en/mpf-system/mpf-coverage | 2026-11-14 |
| MPFA, voluntary contributions and TVC. Read for the HKD 60,000 cap and the 10th-day contribution day | https://www.mpfa.org.hk/en/mpf-system/voluntary-contributions-or-tax-deductible-voluntary-contributions | 2026-11-14 |
| MPFA, self-employed persons. Read for monthly and yearly contribution days | https://www.mpfa.org.hk/en/mpf-system/mandatory-contributions/self-employed-persons | 2026-11-14 |
| MPFA, long service and severance payments. Read for the 1 May 2025 abolition of offsetting | https://www.mpfa.org.hk/en/mpf-system/long-service-and-severance-payments | 2026-11-14 |
| MPFA, withdrawal of MPF. Read for age 65 and statutory grounds | https://www.mpfa.org.hk/en/mpf-system/withdrawal-of-mpf | 2026-11-14 |
| MPFA, enforcement against employers. Read for contribution day, pay records and 30-day notices | https://www.mpfa.org.hk/en/enforcement/enforcement-against-employers | 2026-11-14 |
| IRD, A brief guide to taxes 2025/26 (PDF). Read for the HKD 18,000 deduction cap | https://www.ird.gov.hk/eng/pdf/2026/BriefGuide20252026.pdf | 2026-11-14 |

Not yet confirmed: the contribution surcharge rate (old file: 5%) and the fines for non-payment (HKD 350,000) and SEP failure to join (HKD 50,000 and 6 months); record-keeping period (old file: 7 years); the early withdrawal grounds in detail (early retirement at 60, permanent departure, incapacity, terminal illness, small balance under HKD 5,000, death) as listed in the old file; MPFSO and IRO section references in the old reference table.

**Reference (from the old file, section numbers not re-checked):** MPFSO Cap. 485 ss. 2, 6C, 7, 7A, 7C, 7D, 12A, 43A, 43B, 43E, Schedules 1, 2 and 12; IRO s. 12(1)(e) and the TVC provisions. Major approved trustees named in the old file (HSBC Provident Fund Trustee, Manulife, AIA, Sun Life, Bank Consortium Trust, BOCI-Prudential) and scheme types (master trust, employer-sponsored, industry) remain as listed on the MPFA site.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `hk-mpf` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/hk-mpf. If neither is available, confirm every figure against the official source pages cited above before relying on it.
