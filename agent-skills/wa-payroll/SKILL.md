---
name: wa-payroll
description: "Washington State employer payroll taxes for 2026. Washington has no state income tax withholding. Covers unemployment insurance from the Employment Security Department (ESD) with the $78,200 taxable wage base, 40 rate classes from 0.27% to 6.03% including the employment administration fund, and the new-employer rate; Paid Family and Medical Leave at 1.13% of wages up to $184,500 with the 71.43% employee and 28.57% employer split and the 50-employee rule; the WA Cares Fund long-term care premium of 0.58% with no wage cap and its exemptions; quarterly reports and due dates; and a pointer to Labor and Industries workers' compensation. Trigger on \"Washington payroll\", \"WA payroll tax\", \"Washington unemployment tax\", \"ESD tax rate\", \"Washington SUI\", \"Paid Family and Medical Leave premium\", \"PFML Washington\", \"WA Cares\", \"long-term care tax Washington\", \"Washington new employer\". Federal payroll taxes are in us-form-941-940-payroll."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/wa-payroll"
  jurisdiction: "US-WA"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Washington employer payroll taxes, 2026

> **Source-cited draft.** Built from the Washington Employment Security Department (ESD) 2026 tax rate table and employer pages, the Paid Leave and WA Cares Fund employer pages, the Department of Revenue income tax page and the Department of Labor and Industries (L&I) insurance pages, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026 a Washington employer withholds **no state income tax** (Washington has none for 2026). It pays **unemployment insurance** to ESD on the first **$78,200** of each employee's wages, at its assigned total rate (0.27% to 6.03% for experienced employers). It collects or pays **Paid Family and Medical Leave** premiums of **1.13%** of wages up to **$184,500**: the employee share is up to 71.43%, and an employer with 50 or more employees also pays the 28.57% employer share. It withholds the **WA Cares Fund** premium of **0.58%** of all wages, with no cap, from employees who are not exempt. Workers' compensation is a separate, hour-based premium to L&I.

## Scope and who this is for

In scope: an employer with employees working in Washington in 2026: no state income tax withholding, state unemployment insurance (UI), Paid Family and Medical Leave (PFML) premiums, WA Cares Fund premiums, the quarterly reports for each, and where workers' compensation sits.

Out of scope, and where it goes:

| Topic | Skill or place |
| --- | --- |
| Federal income tax withholding, Social Security, Medicare, FUTA, Forms 941 and 940 | `us-form-941-940-payroll` |
| Workers' compensation premiums (rates by risk class, per hour worked) | L&I, [lni.wa.gov/insurance](https://lni.wa.gov/insurance/) (pointer only, no rates stated here) |
| B&O tax on the employer's own receipts | `wa-bo-tax` |
| Washington's 9.9% income tax on adjusted gross income over $1 million from 1 January 2028 (SB 6346) | not yet a skill; see the pack README |
| Seattle and other local labour standards (minimum wage, paid sick time) | not covered |
| Self-employed owners electing PFML or WA Cares coverage | refer |

## Ask the client first

1. **Where do the employees work?** Washington taxes apply to work localized in Washington; workers split across states need the localization test (refer if unclear).
2. **ESD account and 2026 rate notice:** is the business a new employer (under about 2 1/2 to 3 years), and what total UI rate does its 2026 notice show?
3. **Number of employees in Washington** as counted by Paid Leave each September (50 or more means the employer PFML share is mandatory for 2026).
4. **Wages per employee for 2026**, and whether any employee has passed $78,200 (UI) or $184,500 (PFML).
5. **WA Cares exemptions:** has any employee given you an ESD approval letter exempting them?
6. **Does the employer choose to pay the employee PFML share** on employees' behalf instead of withholding it?

## The method, step by step

1. **State income tax:** none. Do not withhold Washington income tax; there is none for 2026 ([DOR income tax](https://dor.wa.gov/taxes-rates/income-tax)). The 9.9% tax from 2028 is not a payroll withholding item for 2026.
2. **UI taxable wages:** for each employee, wages up to $78,200 in calendar 2026. Wages above that are reported but not taxed for UI.
3. **UI tax:** taxable wages x the employer's total rate (experience rate + social cost rate + employment administration fund (EAF)) from the ESD rate notice. UI is an employer cost.
4. **PFML premium:** gross wages (not tips) up to $184,500 x 1.13%. The employer may withhold up to 71.43% of it from the employee. If the employer had 50 or more employees, it must also pay the remaining 28.57%; under 50, it need not, unless it received a small business assistance grant.
5. **WA Cares premium:** gross wages x 0.58%, no cap, withheld from each employee who is not exempt. Do not deduct it from an employee with an approval letter on file.
6. **File and pay quarterly:** UI and wage report to ESD; PFML report and premiums to Paid Leave; WA Cares premiums with the Paid Leave report; workers' compensation report to L&I. All are due the last day of the month after the quarter.

### Rates, bands and thresholds

| Item | 2026 figure | Source |
| --- | --- | --- |
| State income tax withholding | None ("Washington does not currently have an individual income tax") | [DOR income tax](https://dor.wa.gov/taxes-rates/income-tax) |
| UI taxable wage base, per employee | $78,200 (2025: $72,800; 2027: $82,000) | [ESD news release, average annual wage](https://esd.wa.gov/about-us/news-release/2026/new-average-annual-wage-estimates-adjust-unemployment-insurance-and-paid-leave-benefits) |
| UI total rate, qualified employers, rate class 1 | 0.27% (experience 0.00 + social cost 0.24 = 0.24, plus EAF) | [ESD 2026 tax rates for employers](https://esd.wa.gov/media/pdf/4819/2026-unemployment-tax-rates-employerspdf/download?inline) |
| UI total rate, qualified employers, highest classes | 6.03% (class 39); class 40 shows 6.02% | same |
| UI experience rate cap | 5.4% | [ESD how we determine tax rates](https://esd.wa.gov/employer-requirements/unemployment-taxes/how-we-determine-tax-rates) |
| UI social cost rate cap | 1.22% | same |
| Employment administration fund (EAF) | 0.02% to 0.03%, by rate class | same |
| Experience plus social cost, maximum | 6% | same |
| New employer UI rate | 115% of the average rate for the employer's industry; federal minimum 1%; new-employer status ends after 2 1/2 to 3 years | same |
| Delinquent employers | Extra 0.5%, 1.0%, 1.5% or 2.0% tables (for example class 1 at 0.5% delinquency: 1.25% total) | [ESD 2026 tax rates for employers](https://esd.wa.gov/media/pdf/4819/2026-unemployment-tax-rates-employerspdf/download?inline) |
| PFML premium rate | 1.13% of gross wages, not including tips (2027: 1.2%) | [Paid Leave employer responsibilities](https://paidleave.wa.gov/employer-roles-responsibilities/) |
| PFML wage cap | $184,500 (the 2026 Social Security cap) | same |
| PFML employee share | Up to 71.43% of the premium | same |
| PFML employer share | About 28.57%, mandatory for 50 or more employees (counted each September for the next calendar year) | same |
| WA Cares Fund premium | 0.58% of gross wages, not capped | [WA Cares employers](https://wacaresfund.wa.gov/employers/) |

The full 40-class table, and the delinquent and deferred-payment tables, are in the ESD PDF. Use the employer's own rate notice: the class depends on its benefit ratio over the past 4 fiscal years.

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Employee earns over $78,200 | UI stops at $78,200 of 2026 wages; PFML continues to $184,500; WA Cares on all wages | ESD news release; Paid Leave; WA Cares |
| Employer has 49 employees at the September count | No employer PFML share for 2026; still remits the employee share (withheld or paid on their behalf) | [Paid Leave employer responsibilities](https://paidleave.wa.gov/employer-roles-responsibilities/) |
| Employer under 50 that received a small business assistance grant | Pays the employer share | same |
| Employer pays the employee PFML share as a benefit | Allowed for all employers | same |
| Employee with an ESD WA Cares exemption letter | Keep a copy; do not deduct WA Cares; exemptions may be permanent or conditional | [WA Cares employers](https://wacaresfund.wa.gov/employers/) |
| Exempt employee loses the exemption without telling the employer | The employee owes back premiums and penalties | same |
| Tips | Not included in PFML wages | [Paid Leave employer responsibilities](https://paidleave.wa.gov/employer-roles-responsibilities/) |
| New business | ESD assigns an industry-based rate (115% of industry average, minimum 1%); the tax rate calculator cannot be used | [ESD how we determine tax rates](https://esd.wa.gov/employer-requirements/unemployment-taxes/how-we-determine-tax-rates) |
| Workers misclassified as independent contractors | A common error ESD flags; refer the classification question | [ESD quarterly reports](https://esd.wa.gov/employer-requirements/quarterly-reports) |
| Late PFML reports or premiums | From 1 August 2026 Paid Leave applies penalties to past-due reports and interest to overdue premiums | [Paid Leave reporting](https://paidleave.wa.gov/reporting/) |
| Due date on a weekend or state holiday | ESD accepts the UI report the next business day | [ESD how to file quarterly reports](https://esd.wa.gov/employer-requirements/quarterly-reports/how-file-your-quarterly-tax-and-wage-reports) |

## Worked cases

Employers and employees are invented; rates and caps are 2026 figures from the rates table.

**Case A: one employee earning $200,000, employer with 60 employees.** The employer's 2026 notice puts it in rate class 8, total 1.20% ([ESD 2026 tax rates](https://esd.wa.gov/media/pdf/4819/2026-unemployment-tax-rates-employerspdf/download?inline)).
- UI: $78,200 x 1.20% = $938.40 (employer cost).
- PFML: $184,500 x 1.13% = $2,084.85. Employee share 71.43% = $1,489.21 withheld; employer share (60 employees, so mandatory) $595.64.
- WA Cares: $200,000 x 0.58% = $1,160.00 withheld (no cap).
- No Washington income tax withheld.

```oa-check
name: Washington employer taxes on $200,000 of wages, 60 employees, class 8 (2026)
inputs:
  wages: 200000
  ui_base: 78200
  ui_rate: 0.012
  pfml_cap: 184500
  pfml_rate: 0.0113
  employee_share: 0.7143
  wa_cares_rate: 0.0058
steps:
  - ui_tax: min(wages, ui_base) * ui_rate
  - pfml_total: min(wages, pfml_cap) * pfml_rate
  - pfml_employee: round(pfml_total * employee_share, 2)
  - pfml_employer: pfml_total - pfml_employee
  - wa_cares: wages * wa_cares_rate
expected:
  ui_tax: 938.40
  pfml_total: 2084.85
  pfml_employee: 1489.21
  pfml_employer: 595.64
  wa_cares: 1160.00
```

**Case B, a decision: a 40-employee employer deciding whether to withhold the employee PFML share or pay it.** An employee earns $60,000. PFML is $60,000 x 1.13% = $678.00. The employee share is $484.30. With 40 employees the employer share ($193.70) is not required. If the employer withholds, its PFML cost is $0 and the employee pays $484.30. If it pays the employee share as a benefit, its cost is $484.30 for this employee. Had the business had 50 or more employees at the September count, it would owe $193.70 more either way. WA Cares ($60,000 x 0.58% = $348.00) is withheld from the employee in all cases unless they are exempt.

```oa-check
name: PFML withhold or pay, 40 employees, $60,000 wages (2026)
inputs:
  wages: 60000
  pfml_rate: 0.0113
  employee_share: 0.7143
  employees: 40
steps:
  - pfml_total: wages * pfml_rate
  - pfml_employee: round(pfml_total * employee_share, 2)
  - employer_share_required: clamp(employees - 49, 0, 1)
  - employer_cost_if_withheld: employer_share_required * (pfml_total - pfml_employee)
  - employer_cost_if_paid: pfml_employee + employer_share_required * (pfml_total - pfml_employee)
  - wa_cares: wages * 0.0058
expected:
  pfml_total: 678.00
  pfml_employee: 484.30
  employer_share_required: 0
  employer_cost_if_withheld: 0
  employer_cost_if_paid: 484.30
  wa_cares: 348.00
```

## When to refuse or refer

- Employees working in more than one state: the UI localization test and which state's PFML applies. Refer.
- Self-employed owners, corporate officers or tribal businesses electing coverage, and any question on who counts as an employee. Refer.
- Workers' compensation rates, risk classes and hour reporting: send to L&I; this skill states no rates.
- Voluntary plans that replace state PFML, UI rate appeals, deferred-payment contracts and delinquency. Refer.
- Washington's 2028 income tax: not a 2026 payroll item; do not withhold for it.

## Filing and payment

| Report | Where | Due |
| --- | --- | --- |
| UI quarterly tax and wage report and payment | ESD Employer Account Management Services (EAMS), secureaccess.wa.gov, or by mail | Last day of the month after the quarter: 30 April, 31 July, 31 October, 31 January ([ESD how to file quarterly reports](https://esd.wa.gov/employer-requirements/quarterly-reports/how-file-your-quarterly-tax-and-wage-reports)) |
| PFML quarterly report (wages and hours) and premiums | Paid Leave employer account | 30 April (Q1), 31 July (Q2), 31 October (Q3), 31 January (Q4) ([Paid Leave reporting](https://paidleave.wa.gov/reporting/)) |
| WA Cares premiums | Reported and paid with the Paid Leave report | same dates ([WA Cares employers](https://wacaresfund.wa.gov/employers/)) |
| Workers' compensation quarterly report and premiums | My L&I | Quarterly; see L&I's due-date page ([L&I insurance](https://lni.wa.gov/insurance/)) |

ESD mails each employer's rate notice for the next year in December. A due date on a weekend or state holiday moves to the next business day for the ESD report.

## Completion checklist

- [ ] No Washington income tax withheld
- [ ] UI rate taken from the employer's 2026 ESD notice (or the new-employer industry rate)
- [ ] UI applied to the first $78,200 per employee only
- [ ] PFML at 1.13% to $184,500; employee share withheld or paid; employer share if 50 or more employees
- [ ] WA Cares at 0.58% on all wages, except employees with an exemption letter on file
- [ ] Quarterly reports to ESD, Paid Leave and L&I by the last day of the month after the quarter
- [ ] Federal payroll handled in `us-form-941-940-payroll`

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| DOR income tax page. Read for "Washington does not currently have an individual income tax" and the 9.9% tax from 1 January 2028 (SB 6346). | https://dor.wa.gov/taxes-rates/income-tax | 2026-11-13 |
| ESD 2026 tax rates for employers (PDF, 6 pages). Read for rate classes 1 to 40 (class 1 total 0.27, class 8 total 1.20, class 39 total 6.03, class 40 total 6.02) and the delinquent tables. | https://esd.wa.gov/media/pdf/4819/2026-unemployment-tax-rates-employerspdf/download?inline | 2026-11-13 |
| ESD news release, new average annual wage estimates. Read for "employers will pay unemployment payroll taxes on the first $82,000 paid to each employee, up from $78,200 in 2026". | https://esd.wa.gov/about-us/news-release/2026/new-average-annual-wage-estimates-adjust-unemployment-insurance-and-paid-leave-benefits | 2026-11-13 |
| ESD how we determine tax rates. Read for the 5.4% and 1.22% caps, EAF 0.02% to 0.03%, the 6% total, and "For 2026, you will pay 115% of the average rate for all businesses in your industry. Federal law sets the minimum rate at 1%." | https://esd.wa.gov/employer-requirements/unemployment-taxes/how-we-determine-tax-rates | 2026-11-13 |
| ESD how to file quarterly tax and wage reports. Read for "due on the last day of the month after the last day of each quarter". | https://esd.wa.gov/employer-requirements/quarterly-reports/how-file-your-quarterly-tax-and-wage-reports | 2026-11-13 |
| ESD quarterly reports. Read for EAMS and the misclassification warning. | https://esd.wa.gov/employer-requirements/quarterly-reports | 2026-11-13 |
| Paid Leave employer roles and responsibilities. Read for "In 2026, the premium rate is 1.13% ... up to the 2026 Social Security cap ($184,500)", 71.43%, 28.57% and the 50-employee rule. | https://paidleave.wa.gov/employer-roles-responsibilities/ | 2026-11-13 |
| Paid Leave reporting. Read for the quarterly due dates and penalties from 1 August 2026. | https://paidleave.wa.gov/reporting/ | 2026-11-13 |
| WA Cares Fund employers. Read for "The premium is 0.58% of an employee's gross wages", no cap, and exemption handling. | https://wacaresfund.wa.gov/employers/ | 2026-11-13 |
| L&I insurance. Read for workers' compensation as a separate quarterly premium (pointer only). | https://lni.wa.gov/insurance/ | 2026-11-13 |

Not yet confirmed: workers' compensation rates (L&I publishes them by risk class; not stated here); the PFML premium due-date rule when the 31st falls on a weekend (not stated on the Paid Leave page read); the exact September headcount method for the 50-employee test (the page says it is "determined each September").

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `wa-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/wa-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
