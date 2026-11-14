---
name: ny-payroll
description: New York employer payroll for 2026. State, New York City and Yonkers withholding (2026 NYS-50-T tables, supplemental rates 11.70% state, 4.25% city, 1.95975% Yonkers resident, 0.50% Yonkers nonresident), NYS-1 deposits under the $700 rule and the 3-day or 5-day rule, the quarterly NYS-45, unemployment insurance (2026 wage base $17,600, new employer total rate 4.1%, rated range 1.7% to 9.5%, 0.075% re-employment service fund), Paid Family Leave (0.432% to an annual cap of $411.91), disability benefits (one-half of one percent up to 60 cents a week), the general minimum wage ($17.00 New York City, Long Island and Westchester; $16.00 elsewhere) and Wage Theft Prevention Act notices. MCTMT figures live in ny-mctmt. Trigger on "New York payroll", "NYS-45", "NYS-1", "IT-2104", "NY unemployment insurance", "NY PFL", "NY disability", "Wage Theft Prevention Act". New York only.
version: "3.1"
jurisdiction: US-NY
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: situation-rules
---

# New York employer payroll, 2026: withholding, NYS-45, unemployment insurance, PFL, disability benefits and wage notices

> **Source-cited draft.** Built from Publication NYS-50 and the 2026 NYS-50-T withholding tables, the 2026 instructions for Forms NYS-45 and NYS-1, the Department of Labor's unemployment insurance rate and minimum wage pages, the Workers' Compensation Board's 2026 Paid Family Leave and disability benefits pages and the Department of Labor's Wage Theft Prevention Act pages, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A New York employer registers for withholding and unemployment insurance (UI) through NY Business Express, withholds state tax (and New York City or Yonkers tax for residents of those cities) from the 2026 NYS-50-T tables, deposits withholding on Form NYS-1 once accumulated withholding reaches **USD 700**, and files Form **NYS-45** every quarter by the last day of the following month. For 2026 the UI wage base is **USD 17,600** per employee; a new employer pays **4.1%** in total (4.025% UI plus 0.075% re-employment service fund). Employees pay Paid Family Leave at **0.432%** of gross wages up to **USD 411.91** for the year, and the employer may take up to **60 cents a week** for disability benefits. The general minimum wage is **USD 17.00** an hour in New York City, Nassau, Suffolk and Westchester and **USD 16.00** in the rest of the state, unchanged on 1 January 2027. The employer MCTMT is a separate quarterly return: see `ny-mctmt`.

## Scope and who this is for

- **Covers:** private employers with employees in New York State: withholding of New York State tax, New York City resident tax, the Yonkers resident surcharge and the Yonkers nonresident earnings tax; Form NYS-1 deposits and the quarterly Form NYS-45; UI contributions and the re-employment service fund; Paid Family Leave (PFL) and disability benefits (DBL) employee contributions; the general minimum wage; and the Wage Theft Prevention Act (WTPA) pay notice and pay statement.
- **Does not cover:** federal payroll taxes (Forms 941, 940 and W-2: see the federal payroll skills); the employee's own return (Form IT-201 or IT-203); worker classification; final pay timing, pay frequency and wage deductions under Labor Law sections 191 to 193; overtime rules and industry minimum wages (fast food, home care, tipped, farm); public employers.
- **MCTMT.** The employer metropolitan commuter transportation mobility tax (Form MTA-305) has its own skill, `ny-mctmt`, which holds its threshold and rates. In short: test each quarter whether MCTD payroll expense across both zones is greater than USD 312,500.
- **Remote and cross-border workers.** Where a nonresident works partly outside New York, the employer allocates wages by days worked. The convenience-of-the-employer rule can treat days worked at home outside New York as New York days. That rule and residency tests are in `us-multi-state-residency-and-allocation`.

## Ask the client first

1. **Where does each employee live (New York State, New York City, Yonkers, or out of state), and where do they work, on how many days in each place?** Use the Tax Department's Jurisdiction/Rate Lookup by address for addresses near city lines ([NYS-50](https://www.tax.ny.gov/forms/publications/wt/nys50.htm)).
2. **Registration and UI rate.** Is the business registered for withholding and UI? What 2026 rate is on the Department of Labor rate notice? Is it a new employer?
3. **Deposit status.** How much New York State, New York City and Yonkers tax did it withhold in the calendar year before last (this sets the 3-day or 5-day rule), and has the Tax Department told it that it is a PrompTax filer?
4. **Disability and PFL insurer.** Who is the insurer, has the policy been in force with no lapse, and does the employer take the employee contributions?
5. **Work county for every employee** (for the minimum wage), and whether any employee is in a special industry.
6. **WTPA notices.** Are signed pay notices on file for every employee, in the employee's primary language? Were any bonuses or other supplemental wages paid separately from regular pay?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Supplemental withholding rate, New York State (only if tax is withheld from regular wages) | 11.70% | [NYS-50-T-NYS (1/26)](https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_nys.pdf) |
| Supplemental withholding rate, New York City | 4.25% | [NYS-50-T-NYC (1/26)](https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_nyc.pdf) |
| Supplemental withholding rate, Yonkers resident | 1.95975% | [NYS-50-T-Y (1/26)](https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_y.pdf) |
| Supplemental withholding rate, Yonkers nonresident | 0.50% | [NYS-50-T-Y (1/26)](https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_y.pdf) |
| Yonkers resident surcharge, share of the New York State withholding | 16.75% | [NYS-50](https://www.tax.ny.gov/forms/publications/wt/nys50.htm) |
| Yonkers nonresident earnings tax: no withholding if Yonkers wages are reasonably expected not to exceed | USD 3,000 a year | [NYS-50](https://www.tax.ny.gov/forms/publications/wt/nys50.htm) |
| NYS-1 needed after the payroll that brings accumulated withholding to | USD 700 or more | [Tax Department, withholding due dates](https://www.tax.ny.gov/bus/wt/duedates.htm) |
| 3-business-day filer if withholding in the calendar year before the previous year was | USD 15,000 or more (less: 5 business days) | [Tax Department, withholding due dates](https://www.tax.ny.gov/bus/wt/duedates.htm) |
| UI taxable wage base per employee | USD 17,600 | [NYS-45-I (1/26)](https://www.tax.ny.gov/pdf/current_forms/wt/nys45i.pdf) |
| UI new employer total rate (normal rate capped at 3.4% per NYS-50, plus subsidiary 0.625% (derived: 4.1% less 3.4% less 0.075%), plus 0.075% re-employment service fund) | 4.1% | [DOL, UI rate information](https://dol.ny.gov/unemployment-insurance-rate-information); [NYS-50](https://www.tax.ny.gov/forms/publications/wt/nys50.htm) |
| UI total rate range for rated employers | 1.7% to 9.5% | [DOL, UI rate information](https://dol.ny.gov/unemployment-insurance-rate-information) |
| New employer normal rate cap | 3.4% | [NYS-50](https://www.tax.ny.gov/forms/publications/wt/nys50.htm) |
| Re-employment service fund, on taxable wages | 0.075% | [NYS-45-I (1/26)](https://www.tax.ny.gov/pdf/current_forms/wt/nys45i.pdf) |
| UI liability starts (most employers): remuneration in a calendar quarter of | USD 300 or more | [NYS-50](https://www.tax.ny.gov/forms/publications/wt/nys50.htm) |
| UI liability starts (household employers): cash wages in a calendar quarter of | USD 500 or more | [NYS-50](https://www.tax.ny.gov/forms/publications/wt/nys50.htm) |
| Interest on late UI contributions (cannot be waived) | 12% a year | [NYS-50](https://www.tax.ny.gov/forms/publications/wt/nys50.htm) |
| PFL employee contribution, share of gross wages each pay period | 0.432% | [WCB, Paid Family Leave 2026](https://www.wcb.ny.gov/content/main/PressRe/paid-family-leave-2026.jsp) |
| PFL annual maximum employee contribution | USD 411.91 | [WCB, Paid Family Leave 2026](https://www.wcb.ny.gov/content/main/PressRe/paid-family-leave-2026.jsp) |
| PFL maximum weekly benefit (67% of the USD 1,833.63 state average weekly wage) | USD 1,228.53 | [WCB, Paid Family Leave 2026](https://www.wcb.ny.gov/content/main/PressRe/paid-family-leave-2026.jsp) |
| DBL employee contribution (optional for the employer) | one-half of one percent of wages, at most 60 cents a week | [WCB, disability benefits for employees](https://www.wcb.ny.gov/content/main/DisabilityBenefits/employee-disability-benefits.jsp) |
| Minimum wage, New York City, Nassau, Suffolk and Westchester, from 1 January 2026 (unchanged 1 January 2027) | USD 17.00 an hour | [DOL, minimum wage](https://dol.ny.gov/minimum-wage-0) |
| Minimum wage, rest of the state, from 1 January 2026 (unchanged 1 January 2027) | USD 16.00 an hour | [DOL, minimum wage](https://dol.ny.gov/minimum-wage-0) |
| WTPA: damages for no pay notice | up to USD 50 a day per worker | [DOL, WTPA fact sheet](https://dol.ny.gov/p715-wage-theft-prevention-act) |
| WTPA: damages for no or a deficient pay statement | up to USD 250 a day per worker | [DOL, WTPA fact sheet](https://dol.ny.gov/p715-wage-theft-prevention-act) |

### Steps

1. **Register.** Register for UI, withholding and wage reporting through NY Business Express. Report each new or rehired employee who will work in New York within 20 calendar days of the hire date ([NYS-50](https://www.tax.ny.gov/forms/publications/wt/nys50.htm)).
2. **Collect Form IT-2104** from each employee. If an employee gave a federal Form W-4 for 2020 or later and no IT-2104, the employer may use zero allowances; if the W-4 is from before 2020, it may use the allowances on that W-4. Ask every employee for an IT-2104 anyway; the 2026 tables reflect the rate cuts in Chapter 59 of the Laws of 2025, Part A, and employees who used the pre-2026 worksheet should complete a 2026 IT-2104 ([NYS-50-T-NYS (1/26)](https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_nys.pdf)). Send the Tax Department a copy of any IT-2104 claiming more than 14 allowances, and any IT-2104-E from an employee who usually earns more than USD 200 a week ([NYS-50](https://www.tax.ny.gov/forms/publications/wt/nys50.htm)). Nonresidents who work partly outside New York, or partly outside Yonkers, give Form IT-2104.1.
3. **Work out which taxes to withhold.** An employer must withhold only if it keeps an office or transacts business in New York State. An out-of-state employer not incorporated or licensed under New York law, with no office or business in New York, need not withhold for New York residents; if it agrees to, the full rules apply ([NYS-50](https://www.tax.ny.gov/forms/publications/wt/nys50.htm)).
   - **New York State residents:** state tax on all wages, even wages earned outside the state.
   - **Nonresidents:** state tax on wages for services in New York, allocated by New York days over total days worked; leave out weekends, holidays, sick days, vacation and leave.
   - **New York City residents:** city tax on all wages wherever the work is done. New York City has no withholding for nonresidents.
   - **Yonkers residents:** the resident surcharge, 16.75% of the state tax.
   - **Yonkers nonresidents working in Yonkers:** the nonresident earnings tax on Yonkers wages, unless those wages are reasonably expected not to exceed USD 3,000 for the year.
4. **Compute withholding** from the 2026 tables or the exact calculation method in NYS-50-T-NYS, NYS-50-T-NYC and NYS-50-T-Y (effective 1 January to 31 December 2026). Never compute it from the return rate schedules.
5. **Supplemental wages** (bonuses, commissions and similar) paid separately, or with regular pay but shown separately: if the employer withholds from the employee's regular wages, it may withhold at the flat supplemental rates in the table; otherwise add the supplemental wages to the latest regular pay, compute tax on the total and subtract what was already withheld. If paid with regular pay and not shown separately, treat the total as one regular payment ([NYS-50-T-NYS (1/26)](https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_nys.pdf)).
6. **Deduct the employee contributions:** PFL at 0.432% each pay period until USD 411.91 has been taken (an employee earning under the state average weekly wage pays less than the cap); DBL if the employer collects it, at the lower of one-half of one percent of wages or 60 cents a week. Some part-time or seasonal employees may waive PFL; check the Board's rules before stopping deductions ([coverage requirements](https://www.wcb.ny.gov/content/main/coverage-required-db.jsp)). The PFL contribution is taxable: NYS-50's chart of income items answers "Yes, for premiums paid. No, for benefits.", so take it after tax ([NYS-50](https://www.tax.ny.gov/forms/publications/wt/nys50.htm)). **Never deduct any part of UI contributions from pay**: the law forbids it and doing so is a misdemeanor ([NYS-50](https://www.tax.ny.gov/forms/publications/wt/nys50.htm)).
7. **Deposit withholding on Form NYS-1** under the USD 700 rule and the 3-day or 5-day rule (boundary table; [withholding due dates](https://www.tax.ny.gov/bus/wt/duedates.htm)).
8. **File Form NYS-45 each quarter** with Parts A (UI), B (withholding reconciliation) and C (employee wages, with New York State, New York City and Yonkers tax withheld shown separately for each employee) ([March 2025 changes](https://www.tax.ny.gov/bus/wt/changes-2025/default.htm)).
9. **Pay UI and re-employment service fund contributions** on NYS-45 Part A on wages up to USD 17,600 per employee for 2026. From 2026 the wage base resets each 1 January to 18% of the state average annual wage, rounded up to the next USD 100, and cannot fall below the previous year's figure ([NYS-45-I (1/26)](https://www.tax.ny.gov/pdf/current_forms/wt/nys45i.pdf)). A newly liable employer pays the new employer rate until it has five completed calendar quarters of liability at a 31 December computation date ([IA 318.12](https://forms.labor.ny.gov/UI/IA318.12.pdf)). The re-employment service fund is not a credit against federal FUTA ([re-employment service fund](https://dol.ny.gov/re-employment-service-fund-rsf)).
10. **Test MCTMT each quarter** with `ny-mctmt`.
11. **Disability and PFL cover.** An employer with one or more employees on each of at least 30 days in a calendar year (not necessarily consecutive) becomes a covered employer four weeks after the 30th day; post Forms DB-120 and PFL-120 ([coverage requirements](https://www.wcb.ny.gov/content/main/coverage-required-db.jsp)). PFL is usually a rider on the DBL policy and contributions go to the insurer, not to the Tax Department. DBL pays 50% of the average weekly wage up to USD 170 a week for up to 26 weeks in 52; DBL and PFL cannot be paid at the same time and together cannot exceed 26 weeks in 52 ([WCB, disability benefits for employees](https://www.wcb.ny.gov/content/main/DisabilityBenefits/employee-disability-benefits.jsp)).
12. **Wage-and-hour items.** Pay at least the regional minimum wage, give the WTPA pay notice at hire and a compliant pay statement every payday, and keep payroll records for six years ([WTPA fact sheet](https://dol.ny.gov/p715-wage-theft-prevention-act)).
    - **The pay notice at hire states** the rate or rates of pay (with the overtime rate if it applies), how the employee is paid (hour, shift, day, week, commission and so on), the regular payday, the employer's official name and any other names it uses, the address and phone number of the main office or principal location, and any allowances taken as part of the minimum wage (tips, meals, lodging). It is given in English and in the employee's primary language where the Department of Labor offers a translation; the employee signs and dates it ([notice of pay rate](https://dol.ny.gov/notice-pay-rate)).
    - **The pay statement every payday** shows hours worked (regular and overtime), rates of pay, how the employee is paid, piece rates and pieces where used, gross and net wages, itemized deductions, itemized allowances and credits claimed, the employee's name, the employer's name, address and phone number, and the dates covered. Give any employee who asks a written explanation of how wages were computed ([WTPA fact sheet](https://dol.ny.gov/p715-wage-theft-prevention-act)).

## Boundary and exception table

| Rule | Condition that decides it | Source |
| --- | --- | --- |
| NYS-1 needed at all | Only after a payroll that brings accumulated withholding to USD 700 or more. Under USD 700 in a calendar quarter: pay with the NYS-45 | [withholding due dates](https://www.tax.ny.gov/bus/wt/duedates.htm) |
| 3-day or 5-day filer | USD 15,000 or more withheld in the calendar year before the previous calendar year: 3 business days. Less: 5 business days. New employers are 5-day filers until told otherwise. Educational organizations (Tax Law 9(a)(2)) and health care providers (Tax Law 9(a)(4)) use 5 business days whatever they withheld | [withholding due dates](https://www.tax.ny.gov/bus/wt/duedates.htm); [NYS-1-I (1/26)](https://www.tax.ny.gov/pdf/current_forms/wt/nys1i.pdf) |
| Several payrolls in one week | File NYS-1 after the last payroll of the week (Sunday to Saturday). If a quarter ends between payrolls in a week, remit any accumulated USD 700 or more after the quarter's last payroll | [NYS-1-I (1/26)](https://www.tax.ny.gov/pdf/current_forms/wt/nys1i.pdf) |
| Supplemental flat rate | Allowed only if tax is withheld from the employee's regular wages | [NYS-50-T-NYS (1/26)](https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_nys.pdf) |
| City tax for residents working elsewhere | Keep withholding New York City or Yonkers resident tax however long the employee works outside the city. Form IT-2104.1 may be accepted as proof of nonresidence unless the employer knows or has reason to know it is wrong | [NYS-50](https://www.tax.ny.gov/forms/publications/wt/nys50.htm) |
| Household employees | Income tax withholding is voluntary by agreement; UI liability starts at USD 500 cash in a quarter; no MCTMT on household wages | [NYS-50](https://www.tax.ny.gov/forms/publications/wt/nys50.htm) |
| DBL contribution | The lower of one-half of one percent of wages or 60 cents a week. More only under an accepted plan, by agreement | [WCB, disability benefits for employees](https://www.wcb.ny.gov/content/main/DisabilityBenefits/employee-disability-benefits.jsp) |
| Employee with two jobs, combined wages over USD 120 a week | May ask each employer to share the DBL deduction in proportion to earnings; combined at most 60 cents a week | [WCB, disability benefits for employees](https://www.wcb.ny.gov/content/main/DisabilityBenefits/employee-disability-benefits.jsp) |
| Late UI contributions | Received more than 60 days after the quarterly due date: not credited for experience rating, so the rate can rise | [NYS-45-I (1/26)](https://www.tax.ny.gov/pdf/current_forms/wt/nys45i.pdf) |
| WTPA notice update | Within 7 days of a change, unless the next pay statement shows it. Hospitality employers give a new notice for every rate change | [WTPA FAQ](https://dol.ny.gov/wage-theft-prevention-act-frequently-asked-questions); [WTPA fact sheet](https://dol.ny.gov/p715-wage-theft-prevention-act) |
| Minimum wage location | Follows the place of work, not the employer's headquarters | [DOL, minimum wage](https://dol.ny.gov/minimum-wage-0) |
| Remote nonresident employee | Days at home outside New York may still be New York days under the convenience rule: use `us-multi-state-residency-and-allocation` | [NYS-50](https://www.tax.ny.gov/forms/publications/wt/nys50.htm) |
| Interest assessment surcharge | Levied each year since 2022 on the federal UI loan. Check any 2026 bill against the Department of Labor's notice; do not assume there is none | [NYS-50](https://www.tax.ny.gov/forms/publications/wt/nys50.htm); [DOL, UI rate information](https://dol.ny.gov/unemployment-insurance-rate-information) |

### Payrolls for 2025 (corrections and late filings)

| Item | 2025 rule | Source |
| --- | --- | --- |
| Withholding tables | The 2025 tables; the 2026 tables apply only to payrolls on or after 1 January 2026 | [NYS-50-T-NYS (1/26)](https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_nys.pdf) |
| UI wage base | USD 12,800 | [NYS-45-I (1/26)](https://www.tax.ny.gov/pdf/current_forms/wt/nys45i.pdf) |
| UI rate | Use the rate on the employer's 2025 rate notice | [DOL, UI rate information](https://dol.ny.gov/unemployment-insurance-rate-information) |
| PFL | 0.388%, capped at USD 354.53 | [WCB, Paid Family Leave 2025](https://www.wcb.ny.gov/content/main/PressRe/paid-family-leave-2025.jsp) |
| Minimum wage | USD 16.50 (New York City, Nassau, Suffolk, Westchester); USD 15.50 elsewhere | [DOL, history of the minimum wage](https://dol.ny.gov/history-minimum-wage-new-york-state) |
| MCTMT | Q1 and Q2 2025 use the old tables; Q3 and Q4 the new ones: see `ny-mctmt` | [MCTMT for employers](https://www.tax.ny.gov/bus/mctmt/emp.htm) |
| Amending | From March 2025 Forms NYS-45-X and NYS-45-ATT are discontinued: amend by filing a complete new NYS-45. A credit cannot be carried across tax years; a Q4 overpayment is refunded | [March 2025 changes](https://www.tax.ny.gov/bus/wt/changes-2025/default.htm) |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| UI rate for a new employer | 4.1% total for 2026, until the Department of Labor's notice arrives |
| 3-day or 5-day status | 5 business days for a new employer; otherwise ask for the withholding total two years back |
| Employee's IT-2104 | Zero allowances (2020 or later W-4) or the W-4 allowances (pre-2020 W-4); ask for a 2026 IT-2104 |
| Whether the employer takes the DBL contribution | Assume it does not; ask |
| Employee's work county | Do not guess the minimum wage region; ask |

## Worked cases

**Case 1, UI and PFL for a new employer in 2026.** A new employer pays one employee USD 60,000 in 2026 (USD 1,153.85 a week, under the state average weekly wage of USD 1,833.63). Its UI rate is 4.025% plus 0.075% for the re-employment service fund. Only the first USD 17,600 is subject: UI USD 17,600 x 4.025% = USD 708.40; fund USD 17,600 x 0.075% = USD 13.20; total USD 721.60 (the same as 4.1% of USD 17,600). Under the 2025 base of USD 12,800 the same 4.1% would have cost USD 524.80. If USD 15,000 is paid in Q1, Q1 taxable wages are USD 15,000 and Q2 taxable wages are the remaining USD 2,600; later wages are excess wages on line 2 of Part A. The employee's PFL is 0.432% of USD 60,000 = USD 259.20, under the USD 411.91 cap. A colleague paid USD 120,000 would reach the cap: 0.432% x USD 120,000 = USD 518.40, so deductions stop once USD 411.91 has been taken.

```oa-check
name: New York UI for a new employer and PFL, 2026
inputs:
  wages: 60000
  high_wages: 120000
  wage_base: 17600
  ui_rate: 0.04025
  rsf_rate: 0.00075
  pfl_rate: 0.00432
  pfl_cap: 411.91
steps:
  - taxable: min(wages, wage_base)
  - ui: taxable * ui_rate
  - rsf: taxable * rsf_rate
  - total_ui: ui + rsf
  - ui_2025_base: min(wages, 12800) * 0.041
  - pfl: min(wages * pfl_rate, pfl_cap)
  - pfl_high: min(high_wages * pfl_rate, pfl_cap)
expected:
  taxable: 17600
  ui: 708.40
  rsf: 13.20
  total_ui: 721.60
  ui_2025_base: 524.80
  pfl: 259.20
  pfl_high: 411.91
```

**Case 2, a decision: when must this week's withholding be deposited?** An employer withheld USD 14,500 of New York State and New York City tax in 2024 (the calendar year before the previous year, for 2026). That is under USD 15,000, so it is a 5-business-day filer for 2026. Its weekly payroll withholds USD 450. After week 1 the accumulated tax is USD 450: under USD 700, so no NYS-1 yet. After week 2 it is USD 900: USD 700 or more, so file NYS-1 and pay within 5 business days of that payroll, then start the count again. Had 2024 withholding been USD 15,000 or more, the deadline would be 3 business days. Decision: deposit USD 900 after the week-2 payroll, within 5 business days. A USD 10,000 bonus paid in its own check to a Yonkers resident whose regular pay is taxed can use the flat rates: state USD 10,000 x 11.70% = USD 1,170; Yonkers resident USD 10,000 x 1.95975% = USD 195.98.

```oa-check
name: NYS-1 deposit decision and flat supplemental withholding, 2026
inputs:
  withheld_two_years_back: 14500
  weekly_withholding: 450
  bonus: 10000
steps:
  - is_3_day_filer: min(1, floor(withheld_two_years_back / 15000))
  - deposit_days: 5 - 2 * is_3_day_filer
  - after_week_1: weekly_withholding
  - after_week_2: weekly_withholding * 2
  - nys1_due_after_week_2: min(1, floor(after_week_2 / 700))
  - state_supplemental: bonus * 0.117
  - yonkers_supplemental: round(bonus * 0.0195975, 2)
expected:
  is_3_day_filer: 0
  deposit_days: 5
  after_week_1: 450
  after_week_2: 900
  nys1_due_after_week_2: 1
  state_supplemental: 1170.00
  yonkers_supplemental: 195.98
```

Further illustrations kept from the earlier version: an employee paid USD 1,000 a week has PFL of USD 4.32 a week and a DBL deduction of USD 0.60 (one-half of one percent would be USD 5.00, over the limit); a part-time employee paid USD 100 a week has a DBL deduction of USD 0.50. A general worker in Nassau County is owed at least USD 17.00 an hour in 2026 (USD 16.50 in 2025); the same job in Albany USD 16.00 (USD 15.50 in 2025).

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-NYP-REMOTE | An employee lives or works outside New York, works remotely, or moved during the year | Refer to `us-multi-state-residency-and-allocation`; never guess an allocation percentage |
| R-NYP-MULTIUI | Which state's UI covers a worker in more than one state | Refer: localization tests need the facts |
| R-NYP-TABLES | Asked to compute withholding from the return rate schedules | Refuse: use the NYS-50-T tables or exact calculation method for the right year |
| R-NYP-LABOR | Worker classification, overtime exemptions, industry minimum wages, WTPA litigation | Refer to an employment lawyer |
| R-NYP-DOL | PrompTax enrolment, successor employer UI transfers, voluntary UI contributions, UI rate disputes | Refer to the Department of Labor or the Tax Department |
| R-NYP-OPEN | A figure not yet confirmed (the 2025 new employer UI rate; the 2027 UI wage base) | Say so; do not guess |

## Filing and payment

- **Form NYS-45:** due the last day of the month after each quarter (30 April, 31 July, 31 October, 31 January), the next business day if that falls on a weekend or legal holiday. No extensions of time to file or pay. File every quarter, including zero quarters, unless the employer has seasonal status ([withholding due dates](https://www.tax.ny.gov/bus/wt/duedates.htm); [NYS-45-I (1/26)](https://www.tax.ny.gov/pdf/current_forms/wt/nys45i.pdf)).
- **Form NYS-1:** due 3 or 5 business days after the payroll that brings accumulated withholding to USD 700 or more. PrompTax filers follow the PrompTax schedule; the largest filers must use PrompTax and are told so ([NYS-50](https://www.tax.ny.gov/forms/publications/wt/nys50.htm)).
- **Form MTA-305:** see `ny-mctmt`.
- **E-filing:** returns must be filed and paid electronically; paper filing when required to e-file costs USD 50 for each document not e-filed, plus USD 50 for not paying electronically ([NYS-50](https://www.tax.ny.gov/forms/publications/wt/nys50.htm)).
- **Penalties and interest:** late UI contributions carry interest at 12% a year, which cannot be waived. A person responsible for withholding who fails to pay it over is personally liable for a penalty equal to the unpaid tax (Tax Law 685(g)). An employee whose statement lowers withholding without a reasonable basis faces USD 500 per statement (Tax Law 685(s)), waived if their liability is no more than their credits. For other amounts use the Tax Department's penalty and interest calculator ([NYS-50](https://www.tax.ny.gov/forms/publications/wt/nys50.htm); [penalties](https://www.tax.ny.gov/bus/wt/penalties.htm)).
- **No DBL or PFL cover:** the Board may impose a penalty of up to one-half of one percent of payroll for the period without cover plus up to USD 500 for each period, and the employer is liable for the greater of the claims paid or one percent of payroll. Failing to insure is a misdemeanor (a fine of USD 100 to USD 500, up to one year in prison, or both, with higher fines for repeat violations within five years). Sole proprietors, partners and corporate officers can be personally liable ([penalties for no coverage](https://www.wcb.ny.gov/content/main/DisabilityBenefits/penalties-no-coverage.jsp)).
- **WTPA:** missing notice, damages of up to USD 50 a day per worker; missing or deficient pay statement, up to USD 250 a day per worker; each stops at USD 5,000 per worker in a worker's own lawsuit, and the fact sheet says they do not apply if the employer paid all wages required by law. Liquidated damages can reach 100% of unpaid wages ([WTPA fact sheet](https://dol.ny.gov/p715-wage-theft-prevention-act)).
- **Records:** keep withholding records for four years after the due date of the tax, or the date it was paid if later ([NYS-50](https://www.tax.ny.gov/forms/publications/wt/nys50.htm)); keep WTPA payroll records and notices for six years ([WTPA fact sheet](https://dol.ny.gov/p715-wage-theft-prevention-act)).

## Completion checklist

- Every employee has IT-2104 on file (and IT-2104.1 where needed); certificates over 14 allowances and IT-2104-E over USD 200 a week sent to the Tax Department.
- New hires reported within 20 calendar days.
- 2026 tables used for 2026 payrolls; city and Yonkers taxes applied to the right employees; the Yonkers USD 3,000 nonresident exception checked.
- NYS-1 deposits met the USD 700 rule and the 3-day or 5-day rule.
- NYS-45 Part B ties to the NYS-1 payments; Part C shows state, city and Yonkers withholding for each employee.
- UI paid on wages up to USD 17,600 (2026) or USD 12,800 (2025), at the notice rate, plus 0.075%.
- PFL at 0.432% up to USD 411.91 (2026); DBL within the one-half-percent or 60-cent limit; a DBL and PFL policy in force all year; DB-120 and PFL-120 posted.
- MCTMT tested each quarter with `ny-mctmt`.
- Pay rates at or above the 2026 regional minimum wage.
- WTPA notices signed and kept; pay statements show every required item.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Publication NYS-50, Employer's Guide to Unemployment Insurance, Wage Reporting, and Withholding Tax. Read for registration, IT-2104 rules, who withholds, Yonkers (16.75%, USD 3,000), UI liability (USD 300, USD 500), the 3.4% new employer cap, 12% interest, the UI deduction ban, records and penalties. | https://www.tax.ny.gov/forms/publications/wt/nys50.htm | 2026-11-13 |
| NYS-50-T-NYS (1/26), effective 1 January to 31 December 2026. Read for the 2026 state tables and the 11.70% supplemental rate. | https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_nys.pdf | 2026-11-13 |
| NYS-50-T-NYC (1/26). Read for the 4.25% New York City supplemental rate. | https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_nyc.pdf | 2026-11-13 |
| NYS-50-T-Y (1/26). Read for the Yonkers supplemental rates (1.95975% resident, 0.50% nonresident). | https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_y.pdf | 2026-11-13 |
| Tax Department, withholding due dates. Read for the USD 700 rule, the USD 15,000 3-day and 5-day test, NYS-45 due dates and no extensions. | https://www.tax.ny.gov/bus/wt/duedates.htm | 2026-11-13 |
| Instructions for Form NYS-1 (1/26). Read for the weekly payroll rule and the 5-day rule for educational organizations and health care providers. | https://www.tax.ny.gov/pdf/current_forms/wt/nys1i.pdf | 2026-11-13 |
| Instructions for Form NYS-45 (1/26). Read for the USD 17,600 wage base (2026), USD 12,800 (2025), the 18% formula, the 4.025% example rate, 0.075% and the 60-day rule. | https://www.tax.ny.gov/pdf/current_forms/wt/nys45i.pdf | 2026-11-13 |
| Department of Labor, unemployment insurance rate information. Read for the 2026 range (1.7% lowest, 4.1% new employer, 9.5% highest) and the subsidiary table. | https://dol.ny.gov/unemployment-insurance-rate-information | 2026-11-13 |
| Department of Labor, re-employment service fund. Read for the fund not being a FUTA credit. | https://dol.ny.gov/re-employment-service-fund-rsf | 2026-11-13 |
| Tax Department, March 2025 withholding changes. Read for the NYS-45-X and NYS-45-ATT discontinuance and the no carry-across rule. | https://www.tax.ny.gov/bus/wt/changes-2025/default.htm | 2026-11-13 |
| Workers' Compensation Board, Paid Family Leave 2026. Read for 0.432%, USD 411.91, USD 1,833.63 and USD 1,228.53. | https://www.wcb.ny.gov/content/main/PressRe/paid-family-leave-2026.jsp | 2026-11-13 |
| Workers' Compensation Board, disability benefits for employees. Read for one-half of one percent, 60 cents a week (WCL 209), the two-job rule, the 50% benefit up to USD 170 a week (WCL 204) and 26 weeks (WCL 205). | https://www.wcb.ny.gov/content/main/DisabilityBenefits/employee-disability-benefits.jsp | 2026-11-13 |
| Workers' Compensation Board, coverage requirements. Read for the 30-day covered employer test and the four-week rule. | https://www.wcb.ny.gov/content/main/coverage-required-db.jsp | 2026-11-13 |
| Workers' Compensation Board, penalties for no coverage. Read for the penalty and misdemeanor amounts. | https://www.wcb.ny.gov/content/main/DisabilityBenefits/penalties-no-coverage.jsp | 2026-11-13 |
| Workers' Compensation Board, Paid Family Leave 2025. Read for 0.388% and USD 354.53 (2025). | https://www.wcb.ny.gov/content/main/PressRe/paid-family-leave-2025.jsp | 2026-11-13 |
| Department of Labor, history of the minimum wage. Read for USD 16.50 (2025) and USD 17.00 (2026) in New York City, Long Island and Westchester. | https://dol.ny.gov/history-minimum-wage-new-york-state | 2026-11-13 |
| Department of Labor, IA 318.12. Read for the five completed calendar quarters rule for newly liable employers. | https://forms.labor.ny.gov/UI/IA318.12.pdf | 2026-11-13 |
| Department of Labor, minimum wage. Read for USD 17.00 and USD 16.00 from 1 January 2026 and no increase on 1 January 2027. | https://dol.ny.gov/minimum-wage-0 | 2026-11-13 |
| Department of Labor, WTPA fact sheet (read through Firecrawl; the page needs JavaScript). Read for USD 50 and USD 250 a day, the USD 5,000 caps, 100% liquidated damages and six-year records. | https://dol.ny.gov/p715-wage-theft-prevention-act | 2026-11-13 |
| Department of Labor, WTPA frequently asked questions (read through Firecrawl). Read for the 7-day update rule and primary language notices. | https://dol.ny.gov/wage-theft-prevention-act-frequently-asked-questions | 2026-11-13 |
| Department of Labor, notice of pay rate (read through Firecrawl). Read for the contents of the pay notice and the languages offered. | https://dol.ny.gov/notice-pay-rate | 2026-11-13 |

Not yet confirmed: the 2025 new employer UI rate (use the 2025 rate notice), the amount of any 2026 interest assessment surcharge, and the 2027 UI wage base (not yet published).
