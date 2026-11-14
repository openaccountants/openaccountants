---
name: sc-payroll
description: "South Carolina 2026 employer payroll: published annualized withholding formula kept distinct from reformed final income tax, SCW4 and WH1605/1606, UI14000 wage base,1.06 percent new total including DACA, SUITS filing."
version: "0.1"
jurisdiction: US-SC
category: state-tax
tax_year: 2026
last_updated: 2026-11-13
tier: 2
domain: payroll
type: computation
---

# South Carolina employer withholding and unemployment, tax year 2026

> **General reference only.** Written by Codex. Not reviewed by an accountant. Obtain qualified professional review before filing, paying or taking a tax position.

> **Circular 230 section 10.37:** Apply relevant law to the taxpayer's facts, evaluate reasonable assumptions and relevant circumstances, and obtain professional review of federal tax implications. Federal figures and computations belong to the linked federal owner skills.

**Answer first.** Compute SC wage withholding using the **published 2026 WH-1603F**, and employer UI separately using the 2026 rate notice plus remaining USD 14,000 annual wage base. The 2026 UI table gives new employers 1% base plus 0.06% DACA, **1.06% total**. Do not replace the published withholding formula with the new final-return 1.99%/5.21% rates on your own. Sources: [2026 formula](https://dor.sc.gov/sites/dor/files/forms/WH1603F_2026.pdf); [actual 2026 table](https://www.dew.sc.gov/employers/tax-rate-information/previous-years-tax-contribution-tables); [withholding transition](https://dor.sc.gov/sites/dor/files/policies/IL26-20.pdf).

## Scope

Ordinary covered SC employees/private employers. SC withholding applies to SC work regardless of employee residence, and specified resident wages earned in a state without income tax. Multistate, family, agricultural, domestic, reimbursing and successor cases require additional coverage determination. Federal FICA/FUTA/withholding figures belong to `us-form-941-940-payroll`; final individual liability to `sc-income-tax`. This skill owns state WH and SUI in one workflow.

## Ask the client first

1. Employer principal business location, FEIN, SCDOR withholding number and DEW SUITS account.
2. Employee work/residence states, SCW4 allowances/additional withholding and exemption records.
3. Pay dates/frequency, taxable wages, benefits and supplemental pay.
4. Each employee's year-to-date covered UI wages, assigned 2026 rate/class and any acquired business.
5. Federal deposit schedule and whether employer is resident/nonresident for SC payment timing.
6. Quarterly payroll/wage detail, deposits, WH1605/1606, W-2/1099 and prior-report adjustments.

## The method, step by step

### Rates, bands and thresholds

|2026 item|Rate, amount and conditions|Official source|
|---|---|---|
|UI annual wage base|First USD 14,000 per employee per employer|[2026 introductory paragraphs](https://www.dew.sc.gov/employers/tax-rate-information/previous-years-tax-contribution-tables)|
|Experienced UI total range|0.06% to 5.46%, including 0.06% DACA; assigned rate controls|[2026 table classes 1 to 20](https://www.dew.sc.gov/employers/tax-rate-information/previous-years-tax-contribution-tables)|
|New employer class 30|1.000% base +0.000% solvency +0.060% DACA =1.060%; maximum USD 148.40 per employee|[2026 class 30 row](https://www.dew.sc.gov/employers/tax-rate-information/previous-years-tax-contribution-tables)|
|2026 solvency surcharge|0% in actual 2026 table|[table and period heading](https://www.dew.sc.gov/employers/tax-rate-information/previous-years-tax-contribution-tables)|
|Withholding personal allowance|USD 5,000 each annualized; zero if zero allowances|[section II](https://dor.sc.gov/sites/dor/files/forms/WH1603F_2026.pdf)|
|Withholding standard deduction|Zero if zero allowances; otherwise 10% annual wages capped USD 7,500|[section II](https://dor.sc.gov/sites/dor/files/forms/WH1603F_2026.pdf)|
|Annualized withholding taxable below USD 3,640|0%|[subtraction method](https://dor.sc.gov/sites/dor/files/forms/WH1603F_2026.pdf)|
|USD 3,640 to below USD 18,230|3% x annualized taxable wages less USD 109.20|[subtraction method](https://dor.sc.gov/sites/dor/files/forms/WH1603F_2026.pdf)|
|USD 18,230 or more|6% x annualized taxable wages less USD 656.10|[subtraction method](https://dor.sc.gov/sites/dor/files/forms/WH1603F_2026.pdf)|

The published formula was revised 4 November 2025 for 2026; current withholding page still links it on read date 13 November 2026. IL26-20 says SCDOR will adjust tables to reflect reform in consultation with fiscal authorities. No later replacement was fetched. This is a **published withholding method**, not a claim that final 2026 personal tax remains 0%/3%/6%. Source: [2026 tables links](https://dor.sc.gov/withholding); [Withholding Tables section](https://dor.sc.gov/sites/dor/files/policies/IL26-20.pdf).

1. Register withholding through MyDORWAY or SCDOR-111 and obtain the nine-digit state file number; retain FEIN/account confirmation. Separately register with DEW through the **SUITS Registration Wizard** for liability determination, giving legal entity, ownership/acquisition, first wages and workforce. Ordinary UI liability can arise with USD 1,500 wages in a quarter or one employee in 20 weeks; different nonprofit/domestic/agriculture rules apply. Sources: [registration](https://dor.sc.gov/sites/dor/files/forms/WH105.pdf); [October 2026 handbook registration/liability sections](https://dew.sc.gov/sites/dew/files/Documents/Employer%20Handbook_As%20of%2010.2026.pdf).
2. Obtain signed SC W-4. The verified WH105 instructions require zero allowances for post 2019 hires without SC W-4 and submission of forms claiming 10 or more allowances or believed incorrect to SCDOR within 30 days. Federal W-4 is not a substitute for current SC allowance instructions. Determine SC-source wages and applicable resident/nonresident exception, rather than withholding solely by payroll office location. Sources: [employee sourcing](https://dor.sc.gov/withholding); [SCW4 requirements](https://dor.sc.gov/sites/dor/files/forms/WH105.pdf).
3. For weekly regular pay, annualize by 52, subtract USD 5,000 per claimed allowance and, only if at least one allowance, subtract 10% wages capped USD 7,500. Apply the published annualized band table and divide annual withholding by 52. Use the correct period constants/tables for other pay frequencies and any additional employee election. Source: [steps I-IV and constants](https://dor.sc.gov/sites/dor/files/forms/WH1603F_2026.pdf).
4. Compute UI covered/excess wages separately. For each employee, current taxable =min(current covered pay, max(14,000-prior YTD covered pay,0)). Apply the actual 2026 **total** effective rate from DEW notice/table; do not add DACA again to an already combined total. Employer UI is employer expense, not an employee deduction. The actual 2026 table, now on the previous-years page because the live page shows 2027, controls 2026 wages. Source: [2026 table and new-employer rule](https://www.dew.sc.gov/employers/tax-rate-information/previous-years-tax-contribution-tables).
5. Reconcile payroll withholding deductions with SCDOR deposits and quarter/annual returns. Reconcile UI covered/excess wages and contribution with separate DEW wage reports. Employee-versus-contractor status follows actual law/DEW determination, not a contract label alone. Successor employers may inherit experience; do not assume new 1.06% when buying an existing business. Source: [covered employment, successorship and wage reporting sections](https://dew.sc.gov/sites/dew/files/Documents/Employer%20Handbook_As%20of%2010.2026.pdf).

## Boundary and exception table

|Situation|Action|
|---|---|
|Zero SCW4 allowances|No payroll standard deduction/personal allowance under published formula|
|One or more allowances|Apply 10% wages capped 7,500 as well as 5,000 per allowance|
|2026 reform versus published payroll bands|Use published WH instructions; final liability has separate AGI/SCIAD model|
|New employer quote 1%|Table adds 0.06% DACA; 2026 total 1.06%; actual notice controls|
|UI wage cap reached|Continue total-wage reporting; tax only remaining covered base|
|Employer outside SC|Withholding payment schedule differs from resident withholding agent|
|Family/nonprofit/agricultural/domestic or successor|Obtain DEW liability/rate determination; ordinary method may not apply|

## Worked cases

**Case 1, ordinary weekly payroll.** WH-1603F's example uses USD 750 weekly and three allowances. Annual wages USD 39,000 less USD 15,000 allowances and USD 3,900 payroll standard deduction gives USD 20,100 taxable; annual WH USD 549.90 and weekly USD 10.575, rounded USD 10.58. This is withholding under the published 2026 formula, not final annual personal tax.

```oa-check
name: South Carolina published2026 weekly withholding
inputs:
  weekly_wages: 750
  allowances: 3
steps:
  - annual_wages: weekly_wages * 52
  - payroll_deduction: min(annual_wages * 0.1, 7500)
  - taxable: annual_wages - allowances * 5000 - payroll_deduction
  - annual_wh: taxable * 0.06 - 656.10
  - weekly_wh: annual_wh / 52
expected:
  annual_wages: 39000
  payroll_deduction: 3900
  taxable: 20100
  annual_wh: 549.9
  weekly_wh: 10.575
```

**Case 2, UI base and rate decision.** Invented new employer has one employee with prior covered wages USD 13,500 and current USD 2,000. Only USD 500 remains taxable. Base contribution USD 5 plus DACA USD 0.30 totals USD 5.30. The full-year maximum at USD 14,000 is USD 148.40, not USD 140; no UI deduction is taken from the employee.

```oa-check
name: South Carolina new employer UI cap including DACA
inputs:
  prior_wages: 13500
  current_wages: 2000
steps:
  - ui_taxable: min(current_wages, max(14000 - prior_wages, 0))
  - base_contribution: ui_taxable * 0.01
  - daca: ui_taxable * 0.0006
  - employer_ui: base_contribution + daca
  - annual_maximum: 14000 * 0.0106
expected:
  ui_taxable: 500
  base_contribution: 5
  daca: 0.3
  employer_ui: 5.3
  annual_maximum: 148.4
```

## When to refuse or refer

Refer new replacement withholding tables, interstate wages, misclassification, acquisitions/experience transfers, reimbursing employers, special coverage and undocumented rate changes. Do not make the employee fund employer UI or use 2027 rates for 2026 payroll.

## Filing and payment

**Withholding:** use https://mydorway.dor.sc.gov. Resident agents (principal business in SC) pay on the same schedule as federal deposits; no federal dollar thresholds are repeated here. Nonresident agents pay quarterly when quarterly liability below USD 500, due last day next month; once USD 500 or more, monthly by 15th following month. Return frequency is separate: **WH1605** for Q1-Q3, **WH1606** for Q4 and annual reconciliation, ordinarily 30 April/31 July/31 October/31 January, next business day for weekend/holiday under WH-105. An open account files even without wages/withholding; payment alone is not a return. Electronic filing/payment mandated for USD 15,000 or more per quarter or 24 or more payments/year. Annual W-2/1099 withholding statements generally due 31 January, with electronic obligations; obtain final current transmission specifications. Sources: [filing/deposit schedules and mandate](https://dor.sc.gov/withholding); [returns, zero activity, annual statements and weekend rule](https://dor.sc.gov/sites/dor/files/forms/WH105.pdf).

**UI:** use https://uitax.dew.sc.gov (**SUITS**), select quarter, report employee names/SSNs, total/covered/excess wages and required weeks/hours fields, verify assigned 2026 rate/assessment and contribution, submit wage report and pay, retaining both confirmations. Quarterly reports/payments ordinarily due 30 April,31 July,31 October,31 January. October 2026 handbook permits mailed reports/payments postmarked next business day for weekend/holiday. Confirm electronic cutoff/account calendar separately. Keep reports and amendments by original quarter; zero-activity/closing requirements follow DEW account instructions. Sources: [wage reporting, SUITS and due-date calendar](https://dew.sc.gov/sites/dew/files/Documents/Employer%20Handbook_As%20of%2010.2026.pdf); [payment methods and quarterly dates](https://www.dew.sc.gov/unemployment-tax-information/paying-your-tax).

## Completion checklist

- SCDOR and DEW accounts, SCW4, worker status and work/residence documented.
- Correct published 2026 WH method/frequency used; later official replacement checked.
- UI remaining 14,000 base and actual total rate including DACA recomputed; employer liability separated.
- WH1605/1606 and DEW reports reconcile to payroll/deposits; accepted returns and payments retained.

## Sources

| Official source and scope actually read | URL | Read on |
|---|---|---|
| Read for Official forms-folder 2026 WH1603F:allonepage, annualization, zero/positive allowance distinction, three bands, both methods and 750/three-allowance example. | https://dor.sc.gov/sites/dor/files/forms/WH1603F_2026.pdf | 2026-11-13 |
| Read for Current withholding page:coverage,2026 formula link, quarterly returns, agent residence-based deposit schedule,15,000/24 electronic mandate. | https://dor.sc.gov/withholding | 2026-11-13 |
| Read for WH105 revision 2/13/23:SCW4, registration, resident/nonresident payment, WH1605/1606, zero activity, January statements and weekend rule; current page corroboration. | https://dor.sc.gov/sites/dor/files/forms/WH105.pdf | 2026-11-13 |
| Read for IL26-20 withholding transition and 2026 final-tax changes; not substituted for payroll formula. | https://dor.sc.gov/sites/dor/files/policies/IL26-20.pdf | 2026-11-13 |
| Read for Previous-years contribution page:actual 2026 heading/period, allclasses,14,000 base, zero solvency,0.06 DACA, newclass 30 total 1.06; 2027 live-page values excluded. | https://www.dew.sc.gov/employers/tax-rate-information/previous-years-tax-contribution-tables | 2026-11-13 |
| Read for October 2026 DEW employer handbook:funding/DACA, coverage, successor, newrate rule, registration/liability, wage reports, SUITS, payment/calendar and weekend clauses. | https://dew.sc.gov/sites/dew/files/Documents/Employer%20Handbook_As%20of%2010.2026.pdf | 2026-11-13 |
| Read for Paying Your Tax:quarterly dates, SUITS/payment, wage base, new/experienced-rate process and paper route. | https://www.dew.sc.gov/unemployment-tax-information/paying-your-tax | 2026-11-13 |

Not yet confirmed: any post-reform replacement of the currently linked 2026 withholding formula, final annual 2026 transmission specifications/supplemental-pay exceptions, employer-specific electronic UI cutoffs, full special-coverage/reimbursing/successor rules, and specific penalty/interest assessments. Ordinary published WH and actual 2026 UI/DACA computations are supported; special cases remain partial.
