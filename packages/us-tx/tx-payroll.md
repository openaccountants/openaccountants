---
name: tx-payroll
description: Texas employer payroll obligations for tax year 2026. Texas has no state income tax, so there is no state withholding, no state W-4 and no state annual withholding reconciliation. The state payroll tax is Texas Workforce Commission (TWC) unemployment insurance tax, paid by the employer only, on the first $9,000 of each employee's wages a year. 2026 rates run from 0.32% to 6.32%; a new employer starts at 2.70%. Covers who is a liable employer ($1,500 of wages in a calendar quarter, or one employee in 20 weeks), registering within 10 days, the five parts of the experience rate, quarterly wage reports and payments due the last day of the month after each quarter, electronic filing, late report penalties and interest. Trigger on "Texas payroll", "Texas withholding", "TWC", "Texas unemployment tax", "Texas SUTA", "Texas wage base", "Texas new employer rate", "C-3 report".
version: "1.1"
jurisdiction: US-TX
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - us-form-941-940-payroll
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Texas payroll: unemployment tax, and no state withholding, tax year 2026

> **Source-cited draft.** Built from the Texas Workforce Commission (TWC) pages Unemployment Insurance Tax Rates, Your 2026 Tax Rates, Unemployment Tax Basics, Tax Report and Payment Due Dates, Employer's Quarterly Wage Report Filing Options and Unemployment Tax Registration, Texas Labor Code Chapters 201 and 213 and Article 8 of the Texas Constitution, read on 2026-11-13. No accountant has reviewed it. Do not run a payroll from it without review by a qualified professional.

**Answer first.** Texas does not tax wages, so a Texas employer withholds only federal taxes. The one state payroll tax is **unemployment insurance (UI) tax**, paid to the TWC by the employer and never deducted from the employee. In 2026 it is charged on the first **$9,000** each employee is paid in the year, at the employer's own rate, between **0.32% and 6.32%**. A newly liable employer pays **2.70%**. Reports and payments are due quarterly, by the last day of the month after the quarter ends, and must be filed electronically.

## Scope

In scope: Texas state payroll for a private employer with employees working in Texas in 2026: whether there is any state withholding, when the employer becomes liable for Texas UI tax, registration with the TWC, the 2026 wage base and rates, how the experience rate is built, the quarterly wage report and payment, and late-filing penalties and interest.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Federal income tax withholding, Social Security and Medicare, Forms 941 and 940, FUTA | `us-form-941-940-payroll` |
| New hire reporting to the state | `us-state-new-hire-reporting-matrix` |
| Other states' withholding and unemployment rules | `us-state-payroll-matrix` |
| Whether a worker is an employee or an independent contractor | Refer (R-TX-PR-CLASS) |
| Government, nonprofit reimbursing and agricultural employers | Refer (R-TX-PR-SPECIAL) |
| Texas franchise tax, which counts wages as a deduction | `tx-franchise-tax` |

## Ask the client first

1. **Wages paid by calendar quarter in 2025 and 2026.** Has the business paid $1,500 or more in any quarter, or had at least one employee on 20 or more different weeks, in either year? That makes it a liable employer.
2. **Is the business new to Texas UI tax, or did it take over another employer's business?** A new account starts at 2.70%; an acquisition can carry over the seller's experience rate.
3. **The 2026 TWC tax rate notice**, if the employer has an account. The rate on the notice is the rate to use; do not rebuild it.
4. **Wages paid to each employee in 2026 so far**, to know when each one passes $9,000.
5. **Who is paid**: employees only, or also owners and contractors? Domestic workers in a private home have their own rules and an annual reporting option.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| State income tax withholding | None: Texas has no individual income tax | [Texas Constitution, Article 8, Section 24-a](https://statutes.capitol.texas.gov/Docs/CN/htm/CN.8.htm) |
| UI taxable wage base, per employee per calendar year | USD 9,000 | [TWC, Unemployment Insurance Tax Rates](https://www.twc.texas.gov/programs/unemployment-tax/tax-rates); [Labor Code 201.082(1)](https://tcss.legis.texas.gov/resources/LA/htm/LA.201.htm) |
| Minimum UI tax rate | 0.32% | [TWC, Your 2026 Tax Rates](https://www.twc.texas.gov/programs/unemployment-tax/your-tax-rates) |
| Maximum UI tax rate | 6.32% | [TWC, Your 2026 Tax Rates](https://www.twc.texas.gov/programs/unemployment-tax/your-tax-rates) |
| Entry-level rate for a newly liable employer (all industry groups) | 2.70% | [TWC, Unemployment Insurance Tax Rates](https://www.twc.texas.gov/programs/unemployment-tax/tax-rates) |
| Average tax rate; average experience tax rate | 1.20%; 0.99% | [TWC, Unemployment Insurance Tax Rates](https://www.twc.texas.gov/programs/unemployment-tax/tax-rates) |
| Replenishment ratio (used in the General Tax Rate) | 1.20 | [TWC, Your 2026 Tax Rates](https://www.twc.texas.gov/programs/unemployment-tax/your-tax-rates) |
| Replenishment Tax Rate (flat, all employers) | 0.21% | [TWC, Your 2026 Tax Rates](https://www.twc.texas.gov/programs/unemployment-tax/your-tax-rates) |
| Obligation Assessment: Bond Obligation Assessment Rate | None for 2026 (ratio 0.00%) | [TWC, Your 2026 Tax Rates](https://www.twc.texas.gov/programs/unemployment-tax/your-tax-rates) |
| Obligation Assessment: Interest Tax Rate | 0.01% | [TWC, Your 2026 Tax Rates](https://www.twc.texas.gov/programs/unemployment-tax/your-tax-rates) |
| Deficit Tax Rate | None for 2026 (ratio 0.00%) | [TWC, Your 2026 Tax Rates](https://www.twc.texas.gov/programs/unemployment-tax/your-tax-rates) |
| Employment and Training Investment Assessment (ETIA) | 0.10% | [TWC, Your 2026 Tax Rates](https://www.twc.texas.gov/programs/unemployment-tax/your-tax-rates) |
| Liable employer: wages paid in a calendar quarter of the current or preceding year | USD 1,500 or more | [Labor Code 201.021(a)(1)](https://tcss.legis.texas.gov/resources/LA/htm/LA.201.htm) |
| Liable employer: weeks with at least one employee in the current or preceding year | 20 or more different calendar weeks | [Labor Code 201.021(a)(2)](https://statutes.capitol.texas.gov/Docs/LA/htm/LA.201.htm) |
| Register with the TWC after becoming liable | Within 10 days | [TWC, Unemployment Tax Registration](https://www.twc.texas.gov/businesses/unemployment-tax-registration) |
| Interest on late tax | 1.5% of the tax for each month or part month, capped at 37.5% of the tax due (in words on the page) | [Labor Code 213.021(a)](https://tcss.legis.texas.gov/resources/LA/htm/LA.213.htm) |
| Late report penalty, filed within 15 days of the due date | USD 15 | [Labor Code 213.022(1)](https://statutes.capitol.texas.gov/Docs/LA/htm/LA.213.htm) |

The wage base is set by statute and has been USD 9,000 every year since at least 2017 (TWC rates table). The 2026 minimum rate equals the three flat parts that every experience-rated employer pays: 0.21% + 0.01% + 0.10% = 0.32%.

### Step 1: is there any Texas withholding?

No. Texas may not tax the net incomes of individuals (Texas Constitution, Article 8, Section 24-a), so there is no state income tax to withhold, no state withholding certificate for employees, and no state annual reconciliation. Withhold and report federal income tax, Social Security and Medicare under `us-form-941-940-payroll`. Texas UI tax is not taken from the employee's pay (TWC, Unemployment Tax Basics).

### Step 2: is the business a liable employer?

A private employer is liable for Texas UI tax if, in the current or preceding calendar year, it paid wages of USD 1,500 or more in any calendar quarter, or employed at least one person for part of a day in 20 or more different calendar weeks (Labor Code 201.021(a)). Domestic and agricultural employment have their own tests (Labor Code 201.023 and 201.028; TWC, Definition and Types of Employment). "Wages" for the tax are the first USD 9,000 per employee per year; payments under a general plan for retirement, sickness or accident disability and the other items in Labor Code 201.082 are not wages.

### Step 3: register

Register on Unemployment Tax Registration (UTR), free and online, within 10 days of becoming liable. UTR says at the end whether the business is liable; if it is, it gives a TWC tax account number at once and the TWC mails an Employer Liability Notice in about two weeks (TWC, Unemployment Tax Registration). Then use Unemployment Tax Services (UTS), with the same login, to file and pay.

### Step 4: find the rate

- **New employer:** 2.70% for 2026 for every industry group. A new account keeps this predetermined rate until it has four chargeable quarters; it usually becomes chargeable in its third quarter of paying wages, and needs six quarters of wages for an experience rating. An employer that acquired a business with experience may instead get a computed rate (TWC, Unemployment Insurance Tax Rates).
- **Interim rate:** after the first four chargeable quarters, an interim rate for the rest of the calendar year, based on taxable wages, timely payment and any benefits charged.
- **Experience-rated employer:** the rate on the TWC rate notice, computed as of 1 October for the next calendar year and normally mailed in December, also shown in UTS. It is the sum of five parts (TWC, Your 2026 Tax Rates):
  1. General Tax Rate (GTR) = benefit ratio x replenishment ratio (1.20 for 2026). Benefit ratio = the last three years of benefits charged to the employer (chargebacks) divided by the last three years of taxable wages; for 2026 the period was the fourth quarter of 2022 to the third quarter of 2025. No chargebacks gives a GTR of 0.00%.
  2. Replenishment Tax Rate: 0.21%.
  3. Obligation Assessment: no bond part for 2026; interest part 0.01%.
  4. Deficit Tax Rate: none for 2026.
  5. ETIA: 0.10%. By law the replenishment rate is reduced by the same 0.10%, so the ETIA does not raise the total.

  Use the rate printed on the notice; rebuild it only to check it.

### Step 5: compute the tax for each quarter

For each employee, taxable wages for the quarter = wages paid in the quarter, but only until that employee's wages for the year reach USD 9,000. Tax = total taxable wages x the employer's rate. The base restarts on 1 January. Wages paid to the same employee by a predecessor employer may count toward the base in some successions; check the TWC rules before assuming it.

### Step 6: report and pay

File the Employer's Quarterly Wage Report and pay the tax by the last day of the month after the quarter (Step "Filing and payment" below). TWC Rules 815.107 and 815.109 require electronic filing and payment, through UTS (up to 1,000 employees; upload, copy last report, manual entry, or a No Wages report), QuickFile (any size; ICESA, MMREF-1, delimited or fixed formats) or approved software; an employer that files on paper may be penalized under Labor Code 213.023 and 213.024 (TWC, Employer's Quarterly Wage Report Filing Options). A liable employer that paid no wages in a quarter still files, as a No Wages report.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Employer with no employees in Texas | No Texas UI account; check the states where employees work (`us-state-payroll-matrix`) |
| Paid under USD 1,500 in every quarter and fewer than 20 weeks of employment, this year and last | Not a liable employer under 201.021 |
| Employee earns more than USD 9,000 in the year | Tax stops once that employee's wages reach USD 9,000; report the full wages, tax only the first USD 9,000 |
| New employer, 2026 | 2.70% until four chargeable quarters, then an interim rate |
| Business bought from another employer | Experience may transfer to the successor; a partial transfer needs a TWC application within one year (two years for common ownership) signed by both parties |
| Moving employees to a new entity to get a lower rate | Unlawful (SUTA dumping) |
| Domestic employer in a private home | May have elected annual reporting: report and pay by 31 January for the prior year (2 February 2026 for 2025, because 31 January 2026 was a Saturday) |
| Reimbursing employer (certain nonprofits and governments) | Quarterly wage reports, reimbursements by the last day of the following month; refer (R-TX-PR-SPECIAL) |
| Benefits charged to the account raise the rate | Voluntary contribution: an employer above the minimum may pay some of the charges to lower its GTR; not available on a predetermined rate |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| The employer's 2026 rate | 2.70% if the account is new; otherwise ask for the rate notice before filing |
| Whether the liability tests are met | Treat as liable once USD 1,500 is paid in any quarter; register within 10 days |
| Year-to-date wages per employee | Rebuild from payroll records before applying the USD 9,000 cut-off |
| Worker status | Employee, until a review says otherwise |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Wages paid but no TWC account | Unregistered liability, back tax, penalties and interest |
| Payroll software set up with a "Texas income tax" deduction | There is none; refund the employee |
| Quarterly report filed late more than 15 days | Penalty grows with each month and with unreported wages (213.022) |
| A rate well above 2.70% after a change of owner | Experience may have transferred; check the rate notice |
| Contractors paid like staff | TWC audits at least 1% of employers each year and reclassifies workers |

## Worked cases

**Case 1, a new employer: liable, then the 2026 tax.** A Texas LLC hires its first staff in 2026. It pays USD 4,200 of wages in the first quarter, more than USD 1,500, so it is a liable employer and must register within 10 days. Its account is new, so its rate is 2.70%. Wages for the year: employee A USD 40,000, employee B USD 7,500, employee C USD 12,000. Taxable wages: A USD 9,000, B USD 7,500, C USD 9,000, total USD 25,500. Tax for the year: USD 25,500 x 2.70% = USD 688.50, paid quarter by quarter as each employee's wages build up to USD 9,000.

```oa-check
name: New Texas employer, 2026 UI tax at 2.70%
inputs:
  q1_wages: 4200
  liability_test: 1500
  wages_a: 40000
  wages_b: 7500
  wages_c: 12000
  wage_base: 9000
  rate: 0.027
steps:
  - margin_over_test: q1_wages - liability_test
  - taxable: min(wages_a, wage_base) + min(wages_b, wage_base) + min(wages_c, wage_base)
  - tax: taxable * rate
expected:
  margin_over_test: 2700.00
  taxable: 25500.00
  tax: 688.50
```

**Case 2, an experience-rated employer: checking the rate notice.** An employer has USD 3,000 of benefits charged to its account and USD 360,000 of taxable wages over the three years to 30 September 2025, and ten employees each paid more than USD 9,000 in 2026. Benefit ratio: USD 3,000 / USD 360,000 = 0.8333%. GTR: 0.8333% x 1.20 = 1.00%. Effective rate: 1.00% + 0.21% + 0.01% + 0% + 0.10% = 1.32%. Taxable wages: 10 x USD 9,000 = USD 90,000. Tax for 2026: USD 90,000 x 1.32% = USD 1,188.00. If the rate notice shows something else, the notice governs: TWC may round or adjust a component, and late payment raises the GTR.

```oa-check
name: Experience-rated Texas employer, 2026 rate and tax
inputs:
  chargebacks: 3000
  taxable_wages_3yr: 360000
  replenishment_ratio: 1.20
  rtr: 0.0021
  interest_rate: 0.0001
  dtr: 0
  etia: 0.0010
  employees: 10
  wage_base: 9000
steps:
  - gtr: chargebacks / taxable_wages_3yr * replenishment_ratio
  - effective_rate: gtr + rtr + interest_rate + dtr + etia
  - taxable: employees * wage_base
  - tax: taxable * effective_rate
expected:
  gtr: 0.01
  effective_rate: 0.0132
  taxable: 90000.00
  tax: 1188.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-TX-PR-CLASS | Whether a worker is an employee or a contractor is disputed | Refer: the TWC test (service, wages, direction and control) needs a reviewer |
| R-TX-PR-SPECIAL | Government, nonprofit reimbursing, agricultural or franchise employer | Refer: separate rules |
| R-TX-PR-SUCC | Acquisition, merger or partial transfer of experience | Refer: successor rules and forms C-82 and C-83 |
| R-TX-PR-AUDIT | TWC audit, assessment or penalty waiver request | Refer; waivers are requested through the TWC Contact Request Form |
| R-TX-PR-MULTI | Employees working in more than one state | Refer: which state's UI law covers each employee |

## Filing and payment

| Wages paid in | Quarter ends | Report and payment due by |
| --- | --- | --- |
| January to March 2026 | 31 March | 30 April 2026 |
| April to June 2026 | 30 June | 31 July 2026 |
| July to September 2026 | 30 September | 31 October 2026 |
| October to December 2026 | 31 December | 31 January 2027 |

Source: [TWC, Tax Report and Payment Due Dates](https://www.twc.texas.gov/programs/unemployment-tax/tax-report-payment-due-dates). A due date on a Saturday, Sunday or TWC holiday moves to the next business day, so the 31 October 2026 date (a Saturday) is met by 2 November 2026 and the 31 January 2027 date (a Sunday) by 1 February 2027. File and pay electronically through UTS or QuickFile. Paper payments go to Cashier, Texas Workforce Commission, P.O. Box 149037, Austin, TX 78714-9037, with the account number on the cheque.

Late filing (Labor Code 213.022): USD 15 if filed within 15 days after the due date; later in the first month, USD 30 plus 0.05% of unreported wages; in the second month, that amount plus USD 30 plus 0.1%; in the third month, those amounts plus USD 30 plus 0.2%. Late payment: interest of 1.5% a month or part month, capped at 37.5% (213.021). A waiver of penalty and interest may be requested; TWC replies within 30 days only if it refuses.

## Completion checklist

- Confirmed no Texas income tax is withheld from any employee.
- Liability tested on both 201.021 tests for this year and last; TWC account registered within 10 days.
- Rate taken from the 2026 rate notice, or 2.70% for a new account.
- USD 9,000 wage base applied per employee, restarting on 1 January.
- Quarterly report filed electronically by the last day of the following month, including No Wages quarters.
- Federal payroll handled under `us-form-941-940-payroll`; new hires reported under `us-state-new-hire-reporting-matrix`.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| TWC, Unemployment Insurance Tax Rates. Read for the $9,000 wage base, the 2.70% entry-level rate for all groups in 2026, new, interim and experience rates, the 2026 row of the rates table (0.32%, 6.32%, 1.20%, 0.99%), successor transfers, SUTA dumping and voluntary contributions. | https://www.twc.texas.gov/programs/unemployment-tax/tax-rates | 2026-11-13 |
| TWC, Your 2026 Tax Rates. Read for the five components, the 1.20 replenishment ratio, RTR 0.21%, no bond assessment, interest rate 0.01%, no deficit rate, ETIA 0.10% and the 0.32% and 6.32% limits. | https://www.twc.texas.gov/programs/unemployment-tax/your-tax-rates | 2026-11-13 |
| TWC, Unemployment Tax Basics. Read for tax not deducted from wages, quarterly reports due the last day of the following month, registration within 10 days and the 2 February 2026 annual domestic date. | https://www.twc.texas.gov/programs/unemployment-tax/unemployment-tax-basics | 2026-11-13 |
| TWC, Tax Report and Payment Due Dates. Read for the quarterly due date table, weekend and holiday rule, mailing address, annual domestic and reimbursing employer dates and penalty waivers. | https://www.twc.texas.gov/programs/unemployment-tax/tax-report-payment-due-dates | 2026-11-13 |
| TWC, Employer's Quarterly Wage Report Filing Options. Read for mandatory electronic filing (Rules 815.107 and 815.109), UTS, QuickFile and No Wages reports. | https://www.twc.texas.gov/programs/unemployment-tax/employers-quarterly-wage-report-filing-options | 2026-11-13 |
| TWC, Unemployment Tax Registration. Read for registration within 10 days, UTR, the account number and the Employer Liability Notice. | https://www.twc.texas.gov/businesses/unemployment-tax-registration | 2026-11-13 |
| Texas Labor Code Chapter 201. Read for 201.021 (liable employer: $1,500 a quarter or 20 weeks) and 201.082 (the $9,000 wage limit and excluded payments). | https://statutes.capitol.texas.gov/Docs/LA/htm/LA.201.htm | 2026-11-13 |
| Texas Labor Code Chapter 213. Read for 213.021 (interest 1.5% a month, 37.5% cap) and 213.022 (late report penalties). | https://statutes.capitol.texas.gov/Docs/LA/htm/LA.213.htm | 2026-11-13 |
| Texas Constitution Article 8. Read for Section 24-a (no tax on individuals' net incomes). | https://statutes.capitol.texas.gov/Docs/CN/htm/CN.8.htm | 2026-11-13 |

Not yet confirmed: the name and number of the quarterly report form (commonly called Form C-3) were not on the pages read; the penalty amounts for not filing or paying electronically (Labor Code 213.023 and 213.024) were not read; how TWC rounds the benefit ratio and GTR was not stated on the pages read, so Case 2 is a check, not a substitute for the notice.
