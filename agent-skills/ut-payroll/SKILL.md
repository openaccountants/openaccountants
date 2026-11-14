---
name: ut-payroll
description: "Utah 2026 employer withholding effective June 1 percentage schedules, quarterly returns/monthly deposits, and DWS unemployment 50700 wage base, assigned rates and reporting."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ut-payroll"
  jurisdiction: "US-UT"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Utah payroll withholding and unemployment insurance, tax year 2026

> **General reference only.** Written by Codex. Not reviewed by an accountant. Obtain qualified professional review before filing, paying or taking a tax position.

> **Circular 230 section 10.37:** Apply relevant law to the taxpayer's facts, evaluate reasonable assumptions and relevant circumstances, and obtain professional review of federal tax implications. Federal figures belong to linked federal owner skills.

**Answer first.** Handle two separate state obligations: Tax Commission wage withholding and Department of Workforce Services unemployment insurance. Current withholding schedules apply to pay periods **beginning 1 June 2026**; the 2026 SUI taxable wage base is **USD 50,700 per employee**. SUI is employer funded and uses the actual assigned 2026 total rate. Do not apply June tables to earlier pay periods or deduct SUI from employees. Sources: [Pub 14 effective date and schedules](https://files.tax.utah.gov/tax/forms/pubs/pub-14.pdf); [2026 wage base](https://jobs.utah.gov/ui/Employer/public/Questions/ExcessWages.aspx); [employer contributions](https://jobs.utah.gov/ui/Employer/Public/Handbook/EmployerHandbookFAQs.aspx).

## Scope

Ordinary contributing employer with Utah-covered employee wages. This skill owns **both state income-tax withholding and SUI**. Federal payroll/FICA/FUTA belongs to `us-form-941-940-payroll`; final employee income tax belongs to `ut-income-tax`. Interstate, temporary nonresident, agricultural, domestic, family, nonprofit, reimbursing and successor employers require separate coverage decisions.

## Ask the client first

1. Employer FEIN, Tax Commission withholding account, DWS account and actual 2026 rate notice.
2. Employee residence/work locations, classification, start/end dates and federal W-4 status.
3. Pay-period start/date/frequency, Utah-taxable wages, deductions and additional withholding.
4. Prior year-to-date UI covered wages by employee, predecessor wages and current pay.
5. Monthly withholding liability, assigned payment/return frequency and annual-filing eligibility.
6. Quarter/year-end wages, W-2/1099 withholding, prior confirmations, zero activity and closure notices.

## The method, step by step

### Rates, bands and thresholds

| Item | Rate or amount and conditions | Official source |
|---|---|---|
| Withholding from pay periods beginning 1 June 2026 | 4.45% of Utah-taxable wages less frequency/status allowance credit, not below zero | [effective date and Schedules 1-8](https://files.tax.utah.gov/tax/forms/pubs/pub-14.pdf) |
| Weekly single allowance credit | USD 9 less 1.3% of wages over USD 180, not below zero | [Schedule 1](https://files.tax.utah.gov/tax/forms/pubs/pub-14.pdf) |
| Weekly married allowance credit | USD 19 less 1.3% of wages over USD 360, not below zero | [Schedule 1](https://files.tax.utah.gov/tax/forms/pubs/pub-14.pdf) |
| 2026 SUI wage base | USD 50,700 per employee per year; gross-wage reporting continues above cap | [2026 table](https://jobs.utah.gov/ui/Employer/public/Questions/ExcessWages.aspx); [reportable wages](https://jobs.utah.gov/UI/Employer/Public/Questions/QuarterlyReporting.aspx) |
| SUI rate | Actual DWS assigned total rate; new employers use industry-based assignment | [rate calculation and annual notice](https://jobs.utah.gov/ui/Employer/Public/Handbook/EmployerHandbookFAQs.aspx) |
| Withholding payment threshold | Under USD 1,000 each month: quarterly payment; USD 1,000 or more each month: monthly payment with quarterly returns | [filing/payment chart](https://files.tax.utah.gov/tax/forms/pubs/pub-14.pdf) |
| Records | DWS: four calendar years; withholding: at least four years from due date of income-tax return reporting wages | [records](https://jobs.utah.gov/UI/Employer/Public/Questions/QuarterlyReporting.aspx); [filing record](https://files.tax.utah.gov/tax/forms/pubs/pub-14.pdf) |

1. Register withholding at https://tap.tax.utah.gov using the tax-account application. Register DWS separately at https://jobs.utah.gov/ui/Employer/EmployerRegistration/. New or acquired businesses submit a status report so DWS can determine liability and rate. Federal W-4 supplies withholding status; Utah-taxable wages follow wages subject to federal withholding, without deducting federal W-4 allowances. Determine work/residence coverage before computing. Sources: [registration, taxable wages and W-4](https://files.tax.utah.gov/tax/forms/pubs/pub-14.pdf); [Form 1 and registration](https://jobs.utah.gov/ui/Employer/Public/Handbook/EmployerHandbookFAQs.aspx).
2. For pay periods beginning 1 June 2026 or later, select the published schedule for frequency/status. Weekly percentage method: gross tax = wages x 0.0445; single credit = max(9 - 0.013 x max(wages - 180,0),0); married credit = max(19 - 0.013 x max(wages - 360,0),0). Withholding = max(gross tax - credit,0), plus authorized additional withholding. Do not substitute the final annual taxpayer credit or federal withholding. **January-May 2026 tables are Not yet confirmed** here. Source: [Schedule 1 and instructions](https://files.tax.utah.gov/tax/forms/pubs/pub-14.pdf).
3. Other frequencies have separate allowances and phase-out bases. Pub 14 lists weekly 52, biweekly 26, semimonthly 24, monthly 12, quarterly 4, semiannual 2, annual 1 and daily/miscellaneous schedules. Monthly single uses allowance 40 and phase-out base 779; married uses 81 and 1,558. Use the appropriate published schedule and additional-pay instructions. Supplemental wages and special nonresident/interstate cases require full facts. Source: [Schedules 1-8](https://files.tax.utah.gov/tax/forms/pubs/pub-14.pdf).
4. Establish DWS covered wages, including applicable bonuses, tips, in-kind payments and 401(k) amounts. Current taxable wages per employee = min(current covered wages, max(50,700 - prior year-to-date covered wages,0)). Report all gross wages after the cap; tax only remaining covered base. Multiply taxable wages by the actual 2026 total contribution rate. Do not add reserve/social components twice. Sources: [2026 excess-wage example](https://jobs.utah.gov/ui/Employer/public/Questions/ExcessWages.aspx); [reportable wages](https://jobs.utah.gov/UI/Employer/Public/Questions/QuarterlyReporting.aspx); [rate factors](https://jobs.utah.gov/ui/Employer/Public/Handbook/EmployerHandbookFAQs.aspx).
5. New employers receive industry-based rates; experienced employers receive earned rates. DWS describes a basic benefit ratio, reserve factor, social tax and delinquency surcharge, followed by an annual written rate notice. Obtain the actual total rate and year. The official TaxRates.aspx page did not return readable content during research: **2026 published minimum/maximum rates, reserve/social parameters and industry table remain Not yet confirmed**. Do not turn indexed search figures into usable rate guidance. The accessible handbook and actual 2026 wage-base page support computation with a genuine notice-rate input. Source: [rate calculation and written notice](https://jobs.utah.gov/ui/Employer/Public/Handbook/EmployerHandbookFAQs.aspx).
6. Employer pays the entire UI contribution; deducting it from employee earnings is prohibited. Worker status follows independence/control facts, not a contract or 1099 label. Interstate UI coverage applies localization, base-of-operations, direction/control and residence tests in order. Successorship can transfer experience and unpaid liability; do not assume the new-employer rate after acquisition. Source: [coverage, classification, contributions and successors](https://jobs.utah.gov/ui/Employer/Public/Handbook/EmployerHandbookFAQs.aspx).
7. Reconcile withholding to Tax Commission deposits, returns and W-2/1099 totals. Reconcile UI gross, excess and taxable wages and contributions separately to DWS reports. Save accepted returns, payment confirmations, rate notices and adjustments. Zero activity does not automatically close either account. Sources: [returns and annual reconciliation](https://files.tax.utah.gov/tax/forms/pubs/pub-14.pdf); [zero-quarter reporting](https://jobs.utah.gov/UI/Employer/Public/Questions/QuarterlyReporting.aspx).

### Boundary decisions

| Situation | Decision |
|---|---|
| Pay period begins before 1 June 2026 | Obtain historical 2026 tables; do not apply June formula |
| Weekly USD 500 single | Allowance partly phases out; compute credit before withholding |
| Employee already earned USD 50,700 | No further SUI taxable wages, but report gross wages |
| Rate lacks year/components | Obtain actual 2026 total DWS rate notice |
| Monthly withholding payments | Quarterly returns still required |
| Household annual election | Withholding and DWS annual eligibility differ |
| Family/agriculture, nonprofit/reimbursing, PEO or acquisition | Obtain specific coverage/rate determination |

## Worked cases

**Case 1, ordinary weekly withholding after June change.** Invented single employee has USD 500 Utah-taxable weekly wages, no additional withholding, and a pay period beginning after 1 June 2026. Gross calculation USD 22.25 less USD 4.84 allowance credit gives USD 17.41 withholding. This is payroll withholding, not final annual tax.

```oa-check
name: UtahJune2026weeklysinglewithholding
inputs:
  weekly_wages: 500
  additional_wh: 0
steps:
  - gross_tax: weekly_wages * 0.0445
  - allowance_credit: max(9 - max(weekly_wages - 180, 0) * 0.013, 0)
  - withholding: max(gross_tax - allowance_credit, 0) + additional_wh
expected:
  gross_tax: 22.25
  allowance_credit: 4.84
  withholding: 17.41
```

**Case 2, SUI cap and rate decision.** Invented employer's actual 2026 notice is assumed to assign a 1.2% total rate, solely an example input. An employee has USD 50,000 prior covered wages and USD 2,000 current wages. Only USD 700 remains taxable, USD 1,300 is excess and employer SUI is USD 8.40. Full-year contribution at this assumed rate is USD 608.40; no employee deduction.

```oa-check
name: Utah2026SUIremainingbasewithnoticeinput
inputs:
  prior_covered: 50000
  current_covered: 2000
  assigned_total_rate: 0.012
steps:
  - taxable_current: min(current_covered, max(50700 - prior_covered, 0))
  - excess_current: current_covered - taxable_current
  - employer_sui: taxable_current * assigned_total_rate
  - annual_max: 50700 * assigned_total_rate
expected:
  taxable_current: 700
  excess_current: 1300
  employer_sui: 8.4
  annual_max: 608.4
```

## When to refuse or refer

Refer pre-June payroll without actual tables, unsupported rate notices, supplemental/nonresident pay, interstate localization, classification disputes, special coverage, reimbursing employers, PEOs and acquisitions. Do not deduct employer SUI from staff or use a future year's rate.

## Filing and payment

**Withholding:** file returns electronically through TAP. Pub 14 permits online payment or mailed payment with TC-941PC; payment alone is not a return. Under USD 1,000 withheld each month generally means quarterly returns/payments. USD 1,000 or more each month means quarterly returns with monthly payments due last day of the following month. Utah does not follow federal semiweekly/next-day deposit rules. Quarterly due dates are 30 April, 31 July, 31 October and 31 January. Eligible federal Form 944/Schedule H employers may file/pay annually by 31 January. Tax Commission weekend/legal-holiday deadlines move to the next business day. Source: [filing/payment methods and due-date chart](https://files.tax.utah.gov/tax/forms/pubs/pub-14.pdf).

Annual reconciliation is combined with the fourth-quarter or annual return and is required even with no withholding for the year. Electronically file the reconciliation and required W-2/1099 statements by 31 January. Match withholding totals to statements; amend the original period online using corrected totals rather than only the difference. Retain confirmation for return and payment separately. Final 2026 transmission layouts and all annual/supplemental exceptions remain Not yet confirmed. Source: [zero returns, amendments, reconciliation and W-2/1099 requirements](https://files.tax.utah.gov/tax/forms/pubs/pub-14.pdf).

**SUI:** DWS online Employer's Quarterly Wage List/Contribution Report and contribution payment are separate from TAP. DWS lists 30 April, 31 July, 31 October and 31 January deadlines. Report gross wages for each worker with name/SSN and reconcile taxable/excess wages, assigned rate and contribution; pay using DWS online/EFT and retain both confirmations. Continue zero quarters until DWS closes the account or determines exemption; seasonal closure does not end reporting. Domestic employers may elect annual reporting by 31 January with quarterly breakdown. Retain records for four calendar years. **DWS weekend/holiday electronic cutoff rules are Not yet confirmed** here; obtain the account calendar before relying on an extension. Sources: [reporting, wages, records and schedule](https://jobs.utah.gov/UI/Employer/Public/Questions/QuarterlyReporting.aspx); [reports, EFT and closure](https://jobs.utah.gov/ui/Employer/Public/Handbook/EmployerHandbookFAQs.aspx).

## Penalties and interest

DWS handbook describes late-report penalty of 5% within the first 15 days, another 5% for each further 15 days or fraction, capped at 25% but at least USD 25; a separate 5% late-contribution penalty and 1% monthly interest. It also describes wage-information penalties and delinquency rate surcharge. Compute an assessment only with actual dates, balance and current applicable rules. Tax Commission withholding penalties are separate: Pub 14 lists graduated greater-of-USD-20-or-2%/5%/10% charges by days late and an additional charge when unpaid after 90 days. Current dated interest/assessment calculations under Pub 58 remain Not yet confirmed. Sources: [delinquency and extension sections](https://jobs.utah.gov/ui/Employer/Public/Handbook/EmployerHandbookFAQs.aspx); [penalties and interest](https://files.tax.utah.gov/tax/forms/pubs/pub-14.pdf).

## Completion checklist

- Utah withholding and DWS accounts, coverage, W-4 and actual 2026 rate recorded.
- Pay-period effective date/frequency, allowance credit and UI wage cap checked.
- Employee withholding and employer SUI separated; wage reports reconcile.
- Payment/return/annual obligations, zero returns and record retention documented.

## Sources

| Official source and scope actually read | URL | Read on |
|---|---|---|
| Read for Pub 14 revision 04/26, effective pay periods beginning June 1,2026: registration, coverage, taxable wages/W4, records, quarterly returns/monthly payments, annual reconciliation, electronic W-2/1099, percentage schedules and examples, penalties and adjacent clauses | https://files.tax.utah.gov/tax/forms/pubs/pub-14.pdf | 2026-11-13 |
| Read for actual 2026 excess-wage table: 50,700 base, per-employee cap and quarterly gross/excess/taxable wage examples | https://jobs.utah.gov/ui/Employer/public/Questions/ExcessWages.aspx | 2026-11-13 |
| Read for quarterly reporting: gross wages including 401(k), online report/payment, zero quarters, domestic annual option, records and four due dates | https://jobs.utah.gov/UI/Employer/Public/Questions/QuarterlyReporting.aspx | 2026-11-13 |
| Read for employer handbook: Form 1/registration, industry and earned rates/annual notice, contributions, interstate coverage, classification, successors, reports/EFT/closure, records, penalties and extensions | https://jobs.utah.gov/ui/Employer/Public/Handbook/EmployerHandbookFAQs.aspx | 2026-11-13 |

Not yet confirmed: January-May 2026 withholding tables; full supplemental/nonresident exceptions; final 2026 W-2/1099 transmission layouts; published 2026 SUI minimum/maximum rates, reserve/social parameters and industry table because TaxRates.aspx was unreadable; DWS weekend/holiday electronic cutoffs; full special coverage, reimbursement and successor rules; dated Pub 58 assessments. Ordinary withholding from June and SUI with an actual 2026 notice-rate input are supported.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ut-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ut-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
