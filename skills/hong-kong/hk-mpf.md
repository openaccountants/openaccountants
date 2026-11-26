---
name: hk-mpf
description: Use this skill whenever asked about Hong Kong Mandatory Provident Fund (MPF) contributions in 2026 (year of assessment 2026/27). Trigger on phrases like "MPF", "Mandatory Provident Fund", "強積金", "employer contribution Hong Kong", "employee contribution HK", "MPF self-employed", "TVC", "voluntary contributions", "MPF cap", "relevant income MPF", "MPFA", "eMPF", or any question about MPF contribution rates, caps, voluntary contributions, tax deductions, the end of the offsetting arrangement and self-employed obligations. It gives the 5% rates, the HKD 7,100 and HKD 30,000 relevant income levels, the 10th-day contribution day and the 60-day enrolment rule. Built from the law, not reviewed by an accountant.
version: "2.1"
jurisdiction: HK
tax_year: 2026
tax_year_notes: "Calendar 2026 and year of assessment 2026/27. Relevant income levels checked on 26 November 2026. The offsetting transition was on 1 May 2025. The first phase of MPF Full Portability starts on 21 December 2026."
last_updated: 2026-11-26
depends_on:
  - hk-salaries-tax
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Hong Kong Mandatory Provident Fund (強制性公積金), 2026

> **General reference only.** Built from the law, not reviewed by an accountant. Do not file, pay or take a position on it without review by a qualified professional or MPF intermediary in Hong Kong.

## Who this applies to

Except for exempt persons, employees and self-employed persons aged 18 to 64 must join an MPF scheme under the Mandatory Provident Fund Schemes Ordinance (MPFSO), Cap. 485. Regulator: Mandatory Provident Fund Schemes Authority (MPFA, 積金局). Contributions, enrolment and records now run through the eMPF Platform. Currency: HKD.

| Category | MPF required | Notes |
| --- | --- | --- |
| Regular employees aged 18 to 64, employed 60 days or more | Yes | Full-time and part-time alike |
| Casual employees in construction or catering, hired day-to-day or for a fixed period under 60 days | Yes | The employer may use an Industry Scheme or a Master Trust Scheme. Enrol within the first 10 days unless the employee already has an account in the same Industry Scheme |
| Self-employed persons aged 18 to 64 | Yes | Open an SEP account within 60 days |
| Under 18 or aged 65 or older | No mandatory contributions | Voluntary contributions depend on the scheme |
| Exempt persons, including domestic employees, members of exempted ORSO schemes and civil servants on pension terms | No | The immigration exemption applies to certain holders of permission to work for up to 13 months or members of an overseas retirement scheme. See Cross-border points |

Salaries tax deduction for contributions: `hk-salaries-tax`.

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| Employer mandatory contribution | 5% of relevant income | Capped at the maximum relevant income | https://www.mpfa.org.hk/en/mpf-system/mandatory-contributions/employees |
| Employee mandatory contribution | 5% of relevant income | None if monthly relevant income is below the minimum | same |
| Minimum relevant income, monthly paid | HKD 7,100 a month | Below it: employer pays 5%, employee pays nothing | same |
| Maximum relevant income, monthly paid | HKD 30,000 a month | Contributions above it: HKD 1,500 each | same |
| Maximum mandatory contribution, each party | HKD 1,500 a month | Relevant income above HKD 30,000 | same |
| Daily levels (non-monthly wage periods) | Minimum HKD 280 a day and maximum HKD 1,000 a day | For ordinary percentage-based contributions, multiply by days in the wage period (weekly: HKD 1,960 and HKD 7,000). Industry Schemes for casual construction and catering employees have a separate scale | same |
| Enrolment deadline, regular employees | Within the first 60 days of employment | Count calendar days. If the last day is a Saturday, public holiday, gale or black rainstorm warning day or a relevant eMPF suspension day, move to the next non-excluded day | https://www.mpfa.org.hk/en/mpf-system/enrolment-and-termination |
| Contribution day, regular employees paid monthly | 10th day of the following month | First payment is due by the 10th after the month in which day 60 falls. The same excluded-day rule applies. Distinguish the employee contribution holiday from the employer’s contribution below | https://www.mpfa.org.hk/en/mpf-system/mandatory-contributions/employees |
| Failure to enrol | Fine up to HKD 350,000 and 3 years’ imprisonment | Employer offence | https://www.mpfa.org.hk/en/enforcement/enforcement-against-employers/enforcement-measures-and-penalties |
| Pay records to employees | Within 7 working days after contributing | Employer duty. Casual employees in Industry Schemes have separate rules | https://www.mpfa.org.hk/en/mpf-system/mandatory-contributions/employees |
| TVC and QDAP salaries tax deduction | Up to HKD 60,000 a year combined | Tax-deductible voluntary contributions | https://www.mpfa.org.hk/en/mpf-system/voluntary-contributions-or-tax-deductible-voluntary-contributions |
| Mandatory contributions deduction | Up to HKD 18,000 a year | Employee under salaries tax (s. 26G) or self-employed person under profits tax (s. 16AA) | https://www.ird.gov.hk/eng/pdf/dipn57.pdf#page=24 |
| Offsetting arrangement abolished | From 1 May 2025 (transition date) | Employees ceasing employment on or after that date; no retrospective effect | https://www.mpfa.org.hk/en/mpf-system/long-service-and-severance-payments |
| Withdrawal age | 65 | Earlier only on statutory grounds | https://www.mpfa.org.hk/en/mpf-system/withdrawal-of-mpf |

## The base

### Relevant income (MPFSO s. 2)

- **Included**. Wages, salary, overtime, commissions, bonuses, leave pay, fees, end-of-year payments and gratuities. Include tips and service charges collected through the employer and distributed to employees.
- **Excluded**. Statutory severance and long service payments, non-cash benefits such as a home or car and reimbursement of necessary employment expenses. Direct tips kept or shared without employer intervention are excluded. Include monetary housing or car allowances where paid or payable to the employee.

### Computation for a regular employee paid monthly

1. Confirm relevant income for the wage period and whether the employee contribution holiday applies. For regular employees, employee contributions are waived for the first 30 days and any immediately following incomplete wage period. The employer generally contributes from day 1 when the employee meets the 60-day rule.
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
| Cap | HKD 1,500 monthly on relevant income of HKD 30,000 or more in total, or HKD 18,000 yearly on HKD 360,000 or more |
| Below the minimum | No mandatory contribution below HKD 7,100 per month or HKD 85,200 per year, using the applicable contribution period |

The SEP uses the contribution day set by the monthly or annual rule. If the day is a Saturday, public holiday, gale or black rainstorm warning day or a relevant eMPF suspension day, move to the next non-excluded day.

### Voluntary contributions

| Feature | TVC (tax-deductible voluntary contribution) | Other voluntary contributions |
| --- | --- | --- |
| Account | Separate TVC account | Employer-scheme voluntary contribution account or a separate special voluntary contribution account, depending on the arrangement |
| Tax deduction | Up to HKD 60,000 combined with QDAP premiums, with TVC deducted first, under salaries tax or personal assessment | No deduction for the employee or SEP |
| Withdrawal | At 65, or early on statutory grounds | Per scheme rules |
| Vesting | Immediate | Employer voluntary contributions may vest by scale |

Calculate salaries tax with and without the deduction and take the difference. In each calculation use the lower of progressive tax on net chargeable income (2% to 17%) and standard tax on net income before allowances (15% on the first HKD 5 million and 16% on the remainder). A deduction can span bands or change which method gives the lower tax.

### Vesting

Employee and employer mandatory contributions vest immediately; employer voluntary contributions may follow a vesting scale under scheme rules.

### Edge cases

- **Multiple employments.** Apply the rate, thresholds and contribution holiday separately for each covered employment. Each employer remits its own contributions. The HKD 18,000 annual mandatory-contribution deduction cap applies across employments.
- **Employee becomes self-employed.** Arrange retention or transfer of accrued employee-account benefits on leaving, and open a separate SEP account within 60 days. Withdrawal remains subject to the statutory grounds. From 21 December 2026, phase one of Full Portability also permits a transfer of the employer mandatory balance from a current job that began on or after 1 May 2025, generally once per calendar year.
- **Multiple part-time jobs.** For regular employees, test 60 continuous days and the monthly HKD 7,100 level separately for each job. On monthly relevant income of HKD 5,000 and HKD 4,000, employers A and B pay HKD 250 and HKD 200 respectively. The employee pays nothing for either job.


**End of offsetting (from 1 May 2025).** Employers can no longer use the MPF from employer mandatory contributions to offset severance or long service payments for service from 1 May 2025. For employees who started before and leave on or after that date, the employer may still use employer mandatory contributions (including accrued returns) to offset the part of the payment for service before 1 May 2025, and employer voluntary contributions for any part. The Labour Department's Subsidy Scheme for Abolition of MPF Offsetting Arrangement shares some of the employer cost. Correction: the old file said offsetting was still permitted in the "current position (2024/25)".

### Conservative defaults

| Ambiguity | Default |
| --- | --- |
| Unknown relevant income | Confirm the actual amount before determining any employee deduction |
| Unknown start date | Confirm the first day of employment before counting the 60 days |
| Self-employed or employee | Confirm the working arrangement before choosing the applicable rules |
| TVC or employer voluntary | Check which type of contribution the employee or SEP made before claiming a deduction |

## Deadlines and filing

| Obligation | Deadline |
| --- | --- |
| Enrol new employee | Within the first 60 days of employment |
| Pay contributions (monthly paid) | On or before the 10th day of the following month |
| Pay records | Within 7 working days after contributing, subject to the Industry Scheme exception |
| Notify specified changes of employer or SEP particulars to the eMPF Platform | In writing within 30 days |
| SEP account | Within 60 days of becoming self-employed |
| SEP annual benefit statement (issued by eMPF) | Within 3 months after the scheme’s financial period |
| Remittance statement information | Keep for at least 7 years from the statement date. The MPFA gives separate 6-month periods for basic employee details and wage breakdowns |

## Penalties and interest

The MPFA can add a 5% surcharge to overdue employer mandatory contributions. On prosecution, the maximum for failure to enrol an employee is HKD 350,000 and 3 years’ imprisonment. For employer non-payment, the maximum is HKD 350,000 and 3 years if no employee deduction was made, or HKD 450,000 and 4 years if the employer deducted the employee contribution. For an SEP who fails to enrol or pay, the maximum is HKD 50,000 and 6 months for the first conviction, and HKD 100,000 and 1 year for each subsequent conviction.

## Cross-border points

- A worker entering Hong Kong for employment under s. 11 of the Immigration Ordinance can qualify for exemption if the permitted stay is 13 months or less or the worker belongs to an overseas retirement scheme. If an initial stay of 13 months or less is extended beyond 13 months and no other exemption applies, enrol within 60 days after the exemption ends. A permit exceeding 13 months from the start does not give the worker a 13-month exemption.
- Permanent departure is an early withdrawal ground subject to a statutory declaration and evidence. Other grounds include retirement from age 60 after ceasing all work, total incapacity, terminal illness, death and a balance of no more than HKD 5,000 in only one scheme with at least 12 months since the last contribution and the required declaration.

## Two worked examples that recompute

**Example 1: three regular employees outside their contribution holidays.** Monthly relevant income of HKD 25,000 gives HKD 1,250 each for employer and employee. At HKD 80,000 both are capped at HKD 1,500. At HKD 6,000 the employer pays HKD 300 and the employee pays nothing. The employer pays HKD 3,050 a month in total and withholds HKD 2,750 from employees.

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

**Example 2: contribute HKD 60,000 to TVC.** Assume the whole contribution is deductible. If the same tax method stays lower before and after the deduction and all HKD 60,000 falls in one marginal band, savings are HKD 10,200 at 17% progressive, HKD 9,000 at 15% standard or HKD 9,600 at 16% standard. TVC generally stays preserved until age 65 unless a statutory early withdrawal ground applies. A self-employed person with HKD 500,000 of annual relevant income pays HKD 18,000 in mandatory contributions. This is deductible under profits tax. If the person elects for personal assessment and has sufficient assessable income, the separate HKD 60,000 TVC deduction can bring the total deduction to HKD 78,000.

```oa-check
name: HK 2026/27 TVC saving within each applicable marginal band
inputs:
  tvc: 60000
steps:
  - saving_progressive: tvc * 0.17
  - saving_standard_first_tier: tvc * 0.15
  - saving_standard_second_tier: tvc * 0.16
  - sep_mandatory: 30000 * 0.05 * 12
  - sep_total_deductible: sep_mandatory + tvc
expected:
  saving_progressive: 10200
  saving_standard_first_tier: 9000
  saving_standard_second_tier: 9600
  sep_mandatory: 18000
  sep_total_deductible: 78000
```

## Ask the client first

1. Employee or self-employed; age; start date.
2. Monthly relevant income, and wage period if not monthly.
3. Any exemption, including domestic employment, ORSO membership, initial permitted stay and overseas retirement scheme membership.
4. For a leaver: start date and whether severance or long service payment is due (offsetting rules).
5. Voluntary contributions wanted, and the marginal salaries tax rate.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| MPFA, mandatory contributions for employees. Read for the 5% rates, the 7,100 and 30,000 levels, HKD 1,500 cap and daily levels | https://www.mpfa.org.hk/en/mpf-system/mandatory-contributions/employees | 2026-11-14 |
| MPFA, enrolment and termination. Read for the 60-day rule, Industry Scheme 10 days and the HKD 350,000 fine | https://www.mpfa.org.hk/en/mpf-system/enrolment-and-termination | 2026-11-14 |
| MPFA, MPF coverage. Read for ages 18 to 64, casual employees and exemptions | https://www.mpfa.org.hk/en/mpf-system/mpf-coverage | 2026-11-14 |
| MPFA, tax-deductible voluntary contributions and the combined HKD 60,000 cap | https://www.mpfa.org.hk/en/mpf-system/voluntary-contributions-or-tax-deductible-voluntary-contributions/tax-deductible-voluntary-contributions | 2026-11-26 |
| MPFA, self-employed persons. Read for monthly and yearly contribution days | https://www.mpfa.org.hk/en/mpf-system/mandatory-contributions/self-employed-persons | 2026-11-14 |
| MPFA, long service and severance payments. Read for the 1 May 2025 abolition of offsetting | https://www.mpfa.org.hk/en/mpf-system/long-service-and-severance-payments | 2026-11-14 |
| MPFA, withdrawal of MPF. Read for age 65 and statutory grounds | https://www.mpfa.org.hk/en/mpf-system/withdrawal-of-mpf | 2026-11-14 |
| MPFA, enforcement against employers. Read for contribution day, pay records and 30-day notices | https://www.mpfa.org.hk/en/enforcement/enforcement-against-employers | 2026-11-14 |
| IRD, A brief guide to taxes 2025/26 (PDF). Read for the HKD 18,000 deduction cap | https://www.ird.gov.hk/eng/pdf/2026/BriefGuide20252026.pdf | 2026-11-14 |
| IRD, rates and deductions for YA 2026/27 | https://www.ird.gov.hk/eng/pdf/pam61e.pdf | 2026-11-26 |
| IRD, practice note 57, statutory deductions for mandatory and voluntary contributions | https://www.ird.gov.hk/eng/pdf/dipn57.pdf#page=24 | 2026-11-26 |
| MPFA, permitted Industry Scheme and Master Trust arrangements for casual employees | https://www.mpfa.org.hk/en/mpf-system/types-of-mpf-schemes/industry-schemes | 2026-11-26 |
| MPFA, employer surcharge and non-payment penalty tiers | https://www.mpfa.org.hk/en/enforcement/enforcement-against-employers/enforcement-measures-and-penalties | 2026-11-26 |
| MPFA, SEP enforcement and conviction tiers | https://www.mpfa.org.hk/en/enforcement/self-employed/enforcement-measures-and-penalties | 2026-11-26 |
| MPFA, early withdrawal conditions | https://www.mpfa.org.hk/en/mpf-system/withdrawal-of-mpf/early-withdrawal | 2026-11-26 |
| MPFA, end of employment and record retention | https://www.mpfa.org.hk/en/mpf-system/enrolment-and-termination/terminating-mpf-accounts | 2026-11-26 |
| Financial Services and the Treasury Bureau, commencement notice and eligibility for phase one portability | https://www.fstb.gov.hk/fsb/en/legco/docs/mpf2148c_20261014-e.pdf | 2026-11-26 |

Not yet confirmed: the older MPFSO reference table’s section-by-section mapping beyond the provisions cited in this guide. Check the scheme-specific terms for voluntary contribution vesting or withdrawal.

MPFA publishes the current [register of approved trustees](https://www.mpfa.org.hk/en/info-centre/public-registers/mpf-approved-trustees) and [registered schemes](https://www.mpfa.org.hk/en/info-centre/public-registers/registered-mpf-schemes).
