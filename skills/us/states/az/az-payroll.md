---
name: az-payroll
description: Arizona employer payroll for 2026, state income tax withholding and state unemployment insurance. Withholding is a percentage of each employee's gross taxable wages (federal W-2 box 1 wages) chosen on Form A-4 (0.5%, 1.0%, 1.5%, 2.0%, 2.5%, 3.0% or 3.5%, or zero), with 2.0% withheld when no A-4 is given within five days of hire; nonresidents are withheld after 60 days in Arizona. Payments follow the federal deposit schedule once quarterly withholding averaged over $1,500, otherwise quarterly with Form A1-QRT (due 30 April, 31 July, 31 October, 31 January); the annual Form A1-R and W-2s are due 31 January. Unemployment insurance (Arizona DES) for 2026 is on the first $8,000 of each employee's wages, at 2.00% for new employers and 0.03% to 8.36% for rated employers. Also covers earned paid sick time accrual and final pay timing. Trigger on "Arizona payroll", "Arizona withholding", "Form A-4", "A1-QRT", "A1-R", "Arizona unemployment tax", "Arizona SUTA", "AZ DES UI rate". Federal payroll lives in us-form-941-940-payroll.
version: "1.1"
jurisdiction: US-AZ
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Arizona payroll: withholding and unemployment insurance, 2026

> **Source-cited draft.** Built from A.R.S. 43-401, 43-412, 23-353, 23-372, 23-622 and 23-730 on azleg.gov, the ADOR 2026 Form A-4 and withholding pages, and the Arizona Department of Economic Security (DES) 2026 Unemployment Insurance Tax Rate Chart and employer page, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Arizona withholding is not computed from a wage table. Each employee picks a percentage on **Form A-4**: 0.5%, 1.0%, 1.5%, 2.0%, 2.5%, 3.0% or 3.5% of **gross taxable wages** (generally W-2 box 1 wages), plus any extra amount, or zero if they expect no Arizona tax. With no A-4 within five days of hire, the employer withholds **2.0%**. Unemployment insurance for 2026 is paid on the first **$8,000** of each employee's wages: **2.00%** for a new employer, **0.03% to 8.36%** for rated employers.

## Scope and who this is for

In scope: any employer paying wages for services performed in Arizona in 2026, in-state or out-of-state; Arizona income tax withholding (A-4, A1-QRT, A1-R, A1-APR); Arizona unemployment insurance with DES (rates, wage base, quarterly report); earned paid sick time accrual and final pay timing, as payroll facts.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Federal income tax withholding, FICA, FUTA, Forms 941, 940, W-2 | `us-form-941-940-payroll` |
| Payroll rules across states | `us-state-payroll-matrix` |
| The employee's Arizona income tax return | `az-income-tax` |
| Transaction privilege tax | `az-sales-tax` |
| Workers' compensation, public employer retirement systems, city minimum wage ordinances, equity compensation withholding | Not covered |

## Ask the client first

1. Where does each employee physically work, and where do they live? Nonresidents in Arizona under 60 days, and Arizona residents working outside Arizona, are treated differently.
2. Has each employee given a current Form A-4 (and, for zero withholding, a new one this year)?
3. Each employee's gross taxable wages: gross pay less pre-tax deductions that reduce W-2 box 1 (cafeteria plan, traditional 401(k)).
4. Arizona withholding in each of the last four quarters (it sets the deposit schedule) and the federal deposit schedule.
5. Is the employer new to Arizona unemployment insurance, or does it have a DES rate notice for 2026?
6. Number of employees (it sets the paid sick time cap).

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure | Source |
| --- | --- | --- |
| A-4 withholding percentages | 0.5%, 1.0%, 1.5%, 2.0%, 2.5%, 3.0%, 3.5% of gross taxable wages, plus any extra amount; or zero | [Form A-4 (2026)](https://azdor.gov/sites/default/files/document/FORMS_WITHHOLDING_2026_A-4_f.pdf) |
| Default when no A-4 is given | 2.0% of gross taxable wages | [Form A-4 (2026)](https://azdor.gov/sites/default/files/document/FORMS_WITHHOLDING_2026_A-4_f.pdf) |
| A-4 deadline for new employees | Within the first five days of employment | [Form A-4 (2026)](https://azdor.gov/sites/default/files/document/FORMS_WITHHOLDING_2026_A-4_f.pdf) |
| Gross taxable wages | The federal definition of wages in 26 U.S.C. 3401; generally W-2 box 1 | [ADOR Arizona Withholding Tax](https://azdor.gov/business/withholding-tax) |
| Nonresident working in Arizona | Withholding required once the employee has worked in Arizona for 60 days (earlier if both agree) | [ADOR Arizona Withholding Tax](https://azdor.gov/business/withholding-tax) |
| Quarterly payment | Average withholding not over one thousand five hundred dollars in each of the preceding four quarters: pay with the quarterly return by 30 April, 31 July, 31 October, 31 January | [A.R.S. 43-401(C)](https://www.azleg.gov/ars/43/00401.htm) |
| Federal-schedule payment | Over one thousand five hundred dollars in each of the preceding four quarters: pay Arizona withholding when federal deposits are due under IRC 6302 | [A.R.S. 43-401(C)](https://www.azleg.gov/ars/43/00401.htm) |
| Quarterly reconciliation | 30 April, 31 July, 31 October, 31 January; 10 May, 10 August, 10 November, 10 February if all tax was paid on time | [A.R.S. 43-401(C)](https://www.azleg.gov/ars/43/00401.htm) |
| Annual return (A1-R) | 31 January of the following year | [A.R.S. 43-412(B)](https://www.azleg.gov/ars/43/00412.htm) |
| UI taxable wage base | $8,000 per employee per calendar year (2023 on) | [A.R.S. 23-622](https://www.azleg.gov/ars/23/00622.htm); [DES 2026 rate chart](https://des.az.gov/sites/default/files/dl/UIT-0603A_FY26.pdf) |
| UI new employer rate | 2.00% | [DES 2026 rate chart](https://des.az.gov/sites/default/files/dl/UIT-0603A_FY26.pdf) |
| UI rated employer range | 0.03% (positive ratio 13% or over) to 8.36% (negative ratio 13% or more); zero ratio 4.18% | [DES 2026 rate chart](https://des.az.gov/sites/default/files/dl/UIT-0603A_FY26.pdf) |
| Earned paid sick time | 1 hour per 30 hours worked; use or accrual capped at 40 hours a year (15 or more employees) or 24 hours (fewer than 15) | [A.R.S. 23-372](https://www.azleg.gov/ars/23/00372.htm) |
| Final pay | Discharged: within seven working days or the end of the next pay period, whichever is sooner; quit: by the regular payday | [A.R.S. 23-353](https://www.azleg.gov/ars/23/00353.htm) |

### Step 1: register

One Joint Tax Application (JT-1) on AZTaxes.gov opens the ADOR withholding account and the DES unemployment insurance account ([ADOR Arizona Withholding Tax](https://azdor.gov/business/withholding-tax)).

### Step 2: collect the A-4

New employees complete Form A-4 within five days. The form is kept by the employer, not sent to ADOR. A zero election must be renewed each calendar year; if not renewed the employer may withhold again. Employees can also ask for reduced withholding for charitable and school tax credit contributions (Form A-4C) and nonresidents or Arizona residents working elsewhere can elect voluntary withholding (Form A-4V).

### Step 3: compute withholding each payday

Gross taxable wages for the pay period (gross pay less pre-tax deductions that reduce W-2 box 1) x the elected percentage, plus any extra amount. Supplemental pay (bonuses, commissions) uses the same percentage. Do not apply the percentage to gross pay before pre-tax deductions.

### Step 4: pay and file

Set the payment schedule from the four-quarter $1,500 test in A.R.S. 43-401(C). File the quarterly withholding return (A1-QRT) for each quarter, even with no tax, and the annual A1-R with W-2s by 31 January. Employers that qualify for annual payment under ADOR rules file A1-APR instead of quarterly payments. Pay and file through AZTaxes.gov. An employer may elect not to withhold in December by notifying ADOR and its employees (A.R.S. 43-401(B)).

### Step 5: unemployment insurance

For each employee, UI taxable wages = the smaller of wages paid in 2026 and $8,000 (the wage base restarts each calendar year and with each new employer, subject to successor rules). Contributions = taxable wages x the employer's DES rate. File the quarterly Unemployment Tax and Wage Report (UC-018) and pay through the DES Tax and Wage System. DES sends rate notices each year; 2027 notices are to be mailed on 31 December 2026, and from 1 January 2027 new reporting rules apply (the Unemployment Insurance Operating Fund) ([DES employer page](https://des.az.gov/services/employment/unemployment-employer)).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Employee gave no A-4 | Withhold 2.0% of gross taxable wages |
| Zero election from 2025 not renewed for 2026 | Employer may resume withholding until a new A-4 arrives |
| Arizona resident working entirely in another state for an out-of-state employer | No Arizona withholding required; the employee may ask for voluntary withholding on Form A-4V |
| Nonresident in Arizona under 60 days for an employer with Arizona property, payroll and sales | Excluded from withholding (athletes and entertainers are not excluded) |
| Nonresident from California, Indiana, Oregon or Virginia who gets credit for home-state tax | May claim exemption on Form WEC |
| Enrolled tribal member living and working on that tribe's reservation; qualifying military spouse | Exempt from withholding (Form WEC) |
| Domestic service in a private home, casual labor, most seasonal farm labor | Excluded from withholding |
| Withholding averaged $1,400 in three quarters and $1,700 in one | Not over $1,500 in each of the four: quarterly payment |
| Employee earned $30,000 by March | UI stops after the first $8,000 |
| Independent contractor or employee? | ADOR follows the IRS determination (WTR 16-4); misclassification exposes back withholding and UI |

### Defaults when a fact is missing

| Missing fact | Default |
| --- | --- |
| A-4 | 2.0% |
| UI rate for a business new to Arizona | 2.00% |
| Payment history for the four-quarter test | Ask; a new employer starts quarterly |

### Red flags to raise with the client

| Flag | Why |
| --- | --- |
| Percentage applied to gross pay before pre-tax deductions | Over-withholding; the base is W-2 box 1 wages |
| An old A-4 with percentages above 3.5% | The current options top out at 3.5% |
| UI computed on all wages | Only the first $8,000 per employee |
| UI rate of 2.7% or another state's new employer rate | Arizona's new employer rate is 2.00% |
| No A1-QRT for a quarter with no payroll | A quarterly return is still due |

## Worked cases

**Case 1, withholding for one pay period.** An employee earns $4,000 every two weeks with $750 of pre-tax deductions (cafeteria plan and traditional 401(k)). Gross taxable wages: $3,250. With no A-4 the employer withholds 2.0% = $65.00. If the employee elects 2.5%, the withholding is $81.25.

```oa-check
name: AZ 2026 withholding on gross taxable wages, default against 2.5% election
inputs:
  gross_pay: 4000
  pretax_deductions: 750
  default_rate: 0.02
  elected_rate: 0.025
steps:
  - taxable_wages: gross_pay - pretax_deductions
  - default_withholding: taxable_wages * default_rate
  - elected_withholding: taxable_wages * elected_rate
expected:
  taxable_wages: 3250.00
  default_withholding: 65.00
  elected_withholding: 81.25
```

**Case 2, a decision: which deposit schedule, and how much UI is due?** A new Arizona employer has three employees paid $30,000, $12,000 and $6,000 in 2026. Arizona withholding has averaged under $1,500 in each quarter so far, so it pays Arizona withholding quarterly with the return rather than on the federal schedule. UI taxable wages: $8,000 + $8,000 + $6,000 = $22,000. At the 2.00% new employer rate, 2026 UI contributions are $440.00.

```oa-check
name: AZ 2026 UI contributions for a new employer with three employees
inputs:
  wages_a: 30000
  wages_b: 12000
  wages_c: 6000
  wage_base: 8000
  rate: 0.02
steps:
  - taxable: min(wages_a, wage_base) + min(wages_b, wage_base) + min(wages_c, wage_base)
  - contributions: taxable * rate
expected:
  taxable: 22000.00
  contributions: 440.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-AZ-PR-1 | Multistate employee with days split across states and no records | Refer; allocation needs a workday record |
| R-AZ-PR-2 | Successor employer, transfer of experience or a UI rate protest | Refer to DES rules |
| R-AZ-PR-3 | Worker classification dispute or audit | Refer |
| R-AZ-PR-4 | Equity compensation (ISO, NSO, RSU, ESPP) withholding | Refer |
| R-AZ-PR-5 | Paid sick time claims, penalties or retaliation questions | Refer to an employment lawyer |
| R-AZ-PR-6 | Tribal-land employment or federal contract wage rules | Refer |

## Filing and payment

1. **Register** on the JT-1 through AZTaxes.gov (withholding and UI).
2. **Each payday:** withhold the A-4 percentage; deposit on the federal schedule if the four-quarter $1,500 test is met.
3. **Each quarter:** A1-QRT to ADOR by the last day of the month after the quarter (or the 10th of the next month if all tax was paid on time); UC-018 to DES through the Tax and Wage System.
4. **Each year:** A1-R and W-2s to ADOR by 31 January 2027 for 2026; give employees W-2s with Arizona wages and tax.
5. **Records:** keep each A-4.

## Completion checklist

- A-4 on file for every employee, zero elections renewed for 2026.
- Withholding base is W-2 box 1 wages.
- Deposit schedule set from the last four quarters.
- UI capped at $8,000 per employee; correct 2026 DES rate used.
- A1-QRT filed for every quarter; A1-R and W-2s by 31 January.
- Sick time accrual (1 per 30 hours) and cap (24 or 40 hours) set up.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| ADOR Form A-4 (2026). Read for the seven percentages, the zero election, five days, and the 2.0% default. | https://azdor.gov/sites/default/files/document/FORMS_WITHHOLDING_2026_A-4_f.pdf | 2026-11-13 |
| ADOR, Arizona Withholding Tax (employers). Read for gross taxable wages under 26 U.S.C. 3401, excluded employment, the 60-day nonresident rule, the JT-1 and the annual zero renewal. | https://azdor.gov/business/withholding-tax | 2026-11-13 |
| ADOR, Withholding Tax: Individual. Read for Form WEC (California, Indiana, Oregon, Virginia; tribal members; military spouses) and Form A-4C. | https://azdor.gov/individuals/withholding-tax-individual | 2026-11-13 |
| A.R.S. 43-401. Read for (B) the December election and (C) the $1,500 four-quarter test, the federal schedule and the reconciliation dates. | https://www.azleg.gov/ars/43/00401.htm | 2026-11-13 |
| A.R.S. 43-412. Read for the annual return due 31 January. | https://www.azleg.gov/ars/43/00412.htm | 2026-11-13 |
| DES, Unemployment Insurance Tax Rate Chart, calendar year 2026. Read for the rate table (0.03% to 8.36%, zero ratio 4.18%), "New Employer Rate 2.00%" and "2026 Taxable Wage Limit $8,000". | https://des.az.gov/sites/default/files/dl/UIT-0603A_FY26.pdf | 2026-11-13 |
| DES, Unemployment: Employer. Read for the $8,000 base since 2023, the Tax and Wage System, UC-018 and the 2027 changes. | https://des.az.gov/services/employment/unemployment-employer | 2026-11-13 |
| A.R.S. 23-622. Read for $8,000 from calendar year 2023. | https://www.azleg.gov/ars/23/00622.htm | 2026-11-13 |
| A.R.S. 23-730. Read for the adjusted rate computation. | https://www.azleg.gov/ars/23/00730.htm | 2026-11-13 |
| A.R.S. 23-372. Read for 1 hour per 30, 40 and 24 hour caps. | https://www.azleg.gov/ars/23/00372.htm | 2026-11-13 |
| A.R.S. 23-353. Read for final pay timing. | https://www.azleg.gov/ars/23/00353.htm | 2026-11-13 |

Not yet confirmed: the A1-APR annual payment eligibility rule (set by ADOR rule, not opened); the job training tax (A.R.S. 23-769 page did not load, so no rate is given); the deadline for registering with DES after the first payroll; how long a new employer keeps the 2.00% rate before experience rating (A.R.S. 23-729 not fully read).
