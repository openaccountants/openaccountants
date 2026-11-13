---
name: ak-payroll
description: "Compute Alaska 2026 unemployment insurance with employee withholding, the 54,200 dollar wage base, assigned employer rates, coverage exceptions and TQ01 quarterly reporting. Trigger on Alaska payroll, Alaska withholding, Alaska SUI, Employment Security Tax, UI employee deductions and myAlaska."
version: "0.1"
jurisdiction: US-AK
category: state-tax
tax_year: 2026
last_updated: 2026-11-13
tier: 2
domain: payroll
type: computation
---

# Alaska payroll and unemployment insurance, tax year 2026

> **Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant. General reference for AI-assisted working papers. A qualified professional must review the established facts and filing result. Circular 230 section 10.37: consider relevant facts and circumstances; do not assume missing facts or rely on audit risk.

**Answer first.** Alaska has no individual income tax and no state income-tax wage withholding, but covered employment generally requires **both employer UI contributions and employee UI deductions**. No income-tax withholding is not the same as no state payroll tax. [DOR](https://tax.alaska.gov/programs/programs/index.aspx?10001); [2026 first-time filers](https://dol.alaska.gov/estax/forms/2026_First_Time_Filers.pdf).

## Scope

Ordinary contributory Alaska employers for calendar 2026: state income-tax withholding status, UI coverage, employee deductions, employer contribution and quarterly filing. Federal income withholding, FICA and FUTA belong to `us-payroll`. Reimbursable public/nonprofit/tribal arrangements, disputed employment localization and workers' compensation are separate matters.

## Ask the client first

1. Entity as registered with the state, ownership, officers/members, UI account and coverage elections.
2. Employees, locations of work, services, payroll dates and covered wage components.
3. Each employee's same-employer year-to-date covered wages, transfers and successor/predecessor records.
4. Exact 2026 contribution-rate notice, new/experienced/ineligible status and industry classification.
5. Quarterly gross wages, UI deductions, prior reports/payments, online access and bank authorization.

## The method, step by step

### Rates, bands and thresholds

| Item and condition | 2026 amount | Official source |
| --- | --- | --- |
| Individual income-tax wage withholding | None required | [DOR personal income tax](https://tax.alaska.gov/programs/programs/index.aspx?10001) |
| UI annual covered wage base per employee | USD 54, 200 for both contribution shares; report excess wages without taxing excess | [2026 first-time filers](https://dol.alaska.gov/estax/forms/2026_First_Time_Filers.pdf) |
| Employee UI contribution | 0.50%; maximum USD 271 for this employer absent special wage-base credits | [Wages FAQ](https://www.labor.alaska.gov/estax/faq/WagesDeductions.htm) |
| Published 2026 new industry employer rates | 1.00% employer +0.50% employee =1.50% total in every listed industry, including construction; use assigned notice | [2026 industry table](https://labor.alaska.gov/estax/2026-industry-rates.html) |
| New employer filing before rate assignment | Use 1.50% total maximum in first-time filer instructions; credit if assigned rate is lower | [2026 first-time filers](https://dol.alaska.gov/estax/forms/2026_First_Time_Filers.pdf) |
| Experienced employer classes 1-20 | 1.00% employer +0.50% employee; obtain actual class/rate notice | [2026 experience table](https://labor.alaska.gov/estax/2026-experience-rates.html) |
| Experienced employer class 21 | 5.40% employer +0.50% employee =5.90% total | [2026 experience table](https://labor.alaska.gov/estax/2026-experience-rates.html) |
| Ineligible employer | Rate on reverse of employer's Notice of Contribution Rates; do not assume the new-employer rate | [2026 experience table](https://labor.alaska.gov/estax/2026-experience-rates.html) |

The industry page has a stale last-update footer despite its 2026 title. Its USD 54, 200 base and new-employer shares are independently corroborated by the dated 2026 first-time filer PDF and current wages FAQ. The rate notice remains necessary; 1% is not a universal rate for all employers.

1. Register with Employment Security Tax when employing covered workers. The handbook's general employer definition begins with one individual performing services for the business; establish actual exclusions rather than importing another state's payroll threshold.
2. Determine coverage using state entity status and services. Officers of AS 10.06 corporations are excluded unless voluntary coverage is approved; nonprofit/financial-institution officers not incorporated under AS 10.06 are covered under the FAQ. Sole proprietors and partners are excluded and cannot elect coverage. LLC members are excluded and cannot elect UI coverage, even if the LLC elects S corporation federal tax treatment; a nonmember manager is an employee. Do not extend these exceptions to all staff.
3. Identify covered wages rather than simply using federal W-2 wages. The FAQ treats bonuses as wages; eligible qualified-plan exclusions and documented expense reimbursements require their stated conditions. Unsupported allowances are reportable. Resolve contractor status under the handbook before excluding a worker.
4. Compute each employee's remaining wage base: max(54, 200 minus prior same-employer covered wages, 0). Current taxable wages are the lesser of current covered wages and remaining base. Calculate employer tax using the notice, employee deduction at 0.50%, and remit both shares. Keep gross reportable and limited taxable totals separate.
5. A different unrelated employer generally starts its own base. Same-employer interstate transfers and qualifying business successions have specific wage-credit rules in the handbook; obtain supporting records before giving a credit. Do not reuse the employee's personal multi-employer maximum as this employer's base.
6. Reconcile employee deductions, taxable wages and employer contributions to the quarter report and bank payment. Correct coverage or wage errors through the account rather than silently carrying differences to an unrelated quarter.

## Boundary and exception table

| Facts | Decision |
| --- | --- |
| Ordinary covered employee earning above the annual base | Stop both UI shares at this employer's wage base, but continue reporting gross wages |
| Employee says they cannot qualify for benefits | That alone does not exempt wages or the employee contribution |
| LLC owner elects federal S corporation tax | State UI member exclusion remains; federal income-tax classification does not control UI coverage |
| Nonmember LLC manager | Covered employee under the FAQ |
| No wages in an open account | File a zero report; do not assume the account has closed |
| Reimbursable employer, maritime or multi-state worker | Use the special coverage/payment rules and refer unresolved localization |

## Worked cases

**Case 1.** An invented covered employee has USD 50, 000 earlier 2026 wages with this employer and earns USD 8, 000 this quarter. Employer notice is 1%. Remaining taxable wages are USD 4, 200; employer contribution USD 42, employee deduction USD 21, remittance USD 63. Report all USD 8, 000 gross wages, not only USD 4, 200.

```oa-check
name: Alaska UI crossing the 2026 annual wage base
inputs:
  prior_wages: 50000
  current_wages: 8000
  wage_base: 54200
steps:
  - taxable: min(current_wages, max(wage_base - prior_wages, 0))
  - employer_ui: taxable * 0.01
  - employee_ui: taxable * 0.005
  - remit: employer_ui + employee_ui
expected:
  taxable: 4200
  employer_ui: 42
  employee_ui: 21
  remit: 63
```

**Case 2, rate decision.** An invented experienced employer's notice assigns class 21, 5.40%, not the new-employer 1%. On USD 10, 000 covered wages below the base, employer UI is USD 540 and employee UI USD 50; total USD 590. Using the new-employer rate would understate the employer share by USD 440.

```oa-check
name: Alaska experienced notice versus new-employer assumption
inputs:
  taxable_wages: 10000
  assigned_employer_rate: 0.054
  new_employer_rate: 0.01
steps:
  - employer_ui: taxable_wages * assigned_employer_rate
  - employee_ui: taxable_wages * 0.005
  - total_ui: employer_ui + employee_ui
  - employer_shortfall: employer_ui - taxable_wages * new_employer_rate
expected:
  employer_ui: 540
  employee_ui: 50
  total_ui: 590
  employer_shortfall: 440
```

## When to refuse or refer

Refer disputed employee/contractor status, maritime work, multi-state coverage, successor liability, member/officer elections, reimbursable plans and missing or contested rate notices. Do not classify a worker using the income-tax return alone or deduct the employer's share from employee pay.

## Filing and payment

Use labor.alaska.gov/estax, Online Employer Services, myAlaska sign-in, then Employment Security Tax. Register/activate the employer account, select the quarter, enter employee wage schedules and reportable wages, enter aggregate taxable wages in TQ 01 block 4, reconcile both tax shares, certify and submit. Arrange EFT separately, including first-time bank pre-note, retain confirmation and check the account ledger for completion. An online submission alone does not prove payment.

Reports, wage schedules and payment are due the last day of the month following the quarter: April 30, July 31, October 31, January 31, with applicable weekend/holiday rules. A closing business files within 10 days of cessation. File zeros for every quarter while the account stays open. Internet filing is mandatory once a quarterly wage schedule lists at least 50 employees, taxable wages reach USD 1 million in the current or preceding year, or a payroll agent reports for the employer. The handbook requires payroll records for at least five years.

For contributory employers, the handbook's late-report penalty is 5% of contributions per 30-day period or part, maximum 25%, minimum USD 10 even where no tax is due. Nonpayment can add the greater of USD 10 or 10% of contributions. Unpaid contributions accrue 12% annual interest from the due date. Misappropriating withheld employee contributions can add five times the employee share, minimum USD 25. Reimbursable employer rules differ; do not apply the contributory table to them.

## Completion checklist

- State income-tax withholding marked not applicable; federal payroll handled separately.
- Coverage and elected exceptions supported for each employee/officer/member.
- Actual rate notice and 2026 employee rate entered separately.
- Wage base and eligible prior-wage credits checked employee by employee.
- Gross/taxable wage reconciliation, zero-quarter duty, acceptance and payment confirmed.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| DOR personal income tax program. Read for no individual income tax and no state income-tax employee withholding. | https://tax.alaska.gov/programs/programs/index.aspx?10001 | 2026-11-13 |
| 2026 First Time Filers TQ 01. Read for USD 54, 200 base, employee/employer shares, pre-assignment rate, block 4 and online/EFT process. | https://dol.alaska.gov/estax/forms/2026_First_Time_Filers.pdf | 2026-11-13 |
| 2026 industry-rate table. Read for every listed new-employer industry including construction and notice-dependent treatment. | https://labor.alaska.gov/estax/2026-industry-rates.html | 2026-11-13 |
| 2026 experience-rate table. Read for classes 1-21, employee share and ineligible employer notice warning. | https://labor.alaska.gov/estax/2026-experience-rates.html | 2026-11-13 |
| Wages and deductions FAQ. Read for 2026 base, employee maximum, officers, LLC members, bonuses and reimbursements. | https://www.labor.alaska.gov/estax/faq/WagesDeductions.htm | 2026-11-13 |
| Employment Security Tax Handbook. Read for registration, coverage, wage credits, quarterly deadlines, mandatory online filing, zero reports, record retention and penalties/interest. | https://labor.alaska.gov/estax/documents/taxbook.pdf | 2026-11-13 |

Not yet confirmed: each employer's actual contribution notice, special coverage/localization determinations, approved officer elections, eligible successor wage credits and account-specific appeal/payment arrangements. The ordinary contributory workflow does not compute reimbursable employer billings, maritime exceptions or workers' compensation.
