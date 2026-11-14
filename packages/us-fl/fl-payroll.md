---
name: fl-payroll
description: Florida payroll for an employer in 2026. Florida has no state income tax to withhold, so the state payroll job is reemployment tax (Florida's name for state unemployment insurance) administered by the Florida Department of Revenue. Covers who is a liable employer (USD 1,500 of wages in a quarter or one worker in 20 weeks), the USD 7,000 taxable wage base, the 2.7% initial rate for the first 10 quarters, the 0.1% minimum and 5.4% maximum rates for 2026, the quarterly Form RT-6 with its due dates, electronic filing for 10 or more employees, penalties and the first-three-quarters installment option. Trigger on "Florida payroll", "Florida reemployment tax", "Florida SUTA", "RT-6", "Florida unemployment tax", "Florida withholding". Federal payroll taxes are in us-form-941-940-payroll.
version: "1.0"
jurisdiction: US-FL
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Florida payroll and reemployment tax, tax year 2026

> **Source-cited draft.** Built from the Florida Department of Revenue reemployment tax pages (overview, rate information, report and payment information) and Florida Statutes 443.1215 and 443.1217, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Florida has no state income tax on individuals, so a Florida employer withholds no state income tax. The state payroll tax is **reemployment tax**, paid by the employer only, on the first **USD 7,000** of each employee's wages in 2026. A new employer pays **2.7%** for its first 10 quarters; after that the rate is experience-rated between **0.1%** (USD 7 per employee) and **5.4%** (USD 378 per employee) for 2026. Wages and tax are reported each quarter on **Form RT-6**, due by 30 April, 31 July, 31 October and 31 January.

## Scope and who this is for

In scope: a private employer with workers in Florida in 2026, its liability for Florida reemployment tax, the taxable wages, the rate, the quarterly report and payment.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Federal income tax withholding, FICA, Form 941 and FUTA Form 940 (including the FUTA credit for state tax paid) | `us-form-941-940-payroll` |
| Whether a worker is an employee or a contractor for federal purposes, and 1099-NEC | `us-1099-nec-issuance` |
| Florida corporate income tax | `fl-corporate-income-tax` |
| Florida sales and use tax | `fl-sales-use-tax` |
| A Florida resident working for an employer in a state with an income tax | that state's payroll or income tax skill |

## Ask the client first

1. **When did the business first pay wages in Florida**, and in any calendar quarter of 2025 or 2026 did wages reach USD 1,500? In how many different calendar weeks did at least one person work?
2. **Is it already registered** for Florida reemployment tax, and what rate is on its latest Reemployment Tax Rate Notice (Form RT-20)?
3. **Did it buy a business** or substantially all of another employer's assets? A successor can take over the predecessor's rate and liability.
4. **Each employee's wages paid so far in 2026**, including any paid by a predecessor, so the USD 7,000 base is not counted twice.
5. **How many employees did it have in any quarter from 1 July 2025 to 30 June 2026?** Ten or more means electronic filing and payment.
6. **Is it an employee leasing company, a PEO client or an LLC** whose members are paid? These have their own rules (see the refusal table).

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| State income tax to withhold | None (no personal income tax) | [Florida Constitution, Article VII, section 5](https://www.flsenate.gov/Laws/Constitution) |
| Taxable wage base per employee per calendar year | USD 7,000 | [DOR, Florida Reemployment Tax](https://floridarevenue.com/taxes/taxesfees/Pages/reemployment.aspx); [F.S. 443.1217(2)(a)2](http://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0400-0499/0443/Sections/0443.1217.html) |
| Initial rate for a new employer (first 10 quarters) | 2.7% (0.0270) | [DOR, Reemployment Tax Rate Information](https://floridarevenue.com/taxes/taxesfees/Pages/rt_rate.aspx) |
| Minimum rate, wages paid in 2026 | 0.1% (0.0010), USD 7 per employee | [DOR, Reemployment Tax Rate Information](https://floridarevenue.com/taxes/taxesfees/Pages/rt_rate.aspx) |
| Maximum rate, wages paid in 2026 | 5.4% (0.0540), USD 378 per employee | [DOR, Reemployment Tax Rate Information](https://floridarevenue.com/taxes/taxesfees/Pages/rt_rate.aspx) |
| Liability test: wages in a calendar quarter of the current or preceding year | at least USD 1,500 | [F.S. 443.1215(1)(a)1](http://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0400-0499/0443/Sections/0443.1215.html) |
| Liability test: weeks with at least one worker, current or preceding year | 20 different calendar weeks | [F.S. 443.1215(1)(a)2](http://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0400-0499/0443/Sections/0443.1215.html) |
| Electronic filing and payment required | 10 or more employees in any quarter of the preceding state fiscal year (1 July to 30 June) | [DOR, Report and Payment Information](https://floridarevenue.com/taxes/taxesfees/Pages/rt_return_pay.aspx) |
| Late filing penalty | USD 25 for each 30 days or fraction late | [DOR, Report and Payment Information](https://floridarevenue.com/taxes/taxesfees/Pages/rt_return_pay.aspx) |
| Erroneous or incomplete report penalty | greater of USD 50 or 10% of tax due, at most USD 300 per report | [DOR, Report and Payment Information](https://floridarevenue.com/taxes/taxesfees/Pages/rt_return_pay.aspx) |
| Failure to file electronically when required | USD 25 per report plus USD 1 per employee, at most USD 300 | [DOR, Report and Payment Information](https://floridarevenue.com/taxes/taxesfees/Pages/rt_return_pay.aspx) |
| Failure to pay electronically when required | USD 25 per remittance | [DOR, Report and Payment Information](https://floridarevenue.com/taxes/taxesfees/Pages/rt_return_pay.aspx) |
| Installment fee (quarters 1 to 3 only) | USD 5 once per calendar year | [DOR, Report and Payment Information](https://floridarevenue.com/taxes/taxesfees/Pages/rt_return_pay.aspx) |

### Is the business a liable employer?

1. Under F.S. 443.1215(1)(a), an employing unit is liable if, in the current or preceding calendar year, it paid at least USD 1,500 of wages in a calendar quarter, **or** employed at least one individual for any part of a day in each of 20 different calendar weeks (not necessarily consecutive). Either test is enough.
2. A business that acquires another employer's trade or substantially all its assets is liable from the acquisition (F.S. 443.1215(1)(e) and (f)). Agricultural labor and domestic service have their own thresholds in the same section: refer.
3. A liable employer registers with the Department, which "registers employers, collects the tax and wage reports due, assigns tax rates, and audits employers" ([DOR overview](https://floridarevenue.com/taxes/taxesfees/Pages/reemployment.aspx)).

### Taxable wages

4. Wages are "all remuneration for employment", including commissions, bonuses, back pay awards, the cash value of non-cash pay, and tips reported to the employer in writing (F.S. 443.1217(1)).
5. Excluded from wages (F.S. 443.1217(2), as listed by the Department): accident and health benefits, workers' compensation payments, life insurance, sick pay more than six months after the last month worked, FICA, meals and lodging on the premises for the employer's convenience, qualified retirement plan contributions (401, 403(a), 403(b), SEP, 3121(v)(3) plans), cafeteria plans under section 125 and educational assistance under section 127.
6. Taxable wages per employee = the smaller of wages paid in 2026 and USD 7,000, less what was already taxed earlier in the year (by this employer or a predecessor). Wages above the base are reported as excess wages.
7. The Department may treat a distribution as wages where a corporate officer works for the corporation, reports zero wages and takes a significant distribution.

### Rate

8. A new employer uses 2.7% until it has reported for 10 quarters. After that the Department computes the rate from benefit charges over taxable payroll, plus the variable adjustment factor, the fund size factor and the final adjustment factor. The result for 2026 is between 0.1% and 5.4%. Use the rate on the employer's Form RT-20 notice; do not compute it.
9. A rate can be protested in writing within 20 days of the "Mailed On or Before" date on Form RT-20.
10. Tax for the quarter = taxable wages for the quarter times the rate.

### The quarterly report (Form RT-6)

11. Report every quarter, even with no wages or no tax: total wages to covered workers, excess wages, taxable wages, tax due, and for each employee the name, Social Security number and total wages. An ITIN (starts with 9) is not a valid SSN for this report.
12. File and pay through the Department's Reemployment Tax eFile and Pay site, by import or XML upload, or on a paper RT-6 if electronic filing is not required.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Wages under USD 1,500 in every quarter and fewer than 20 weeks with a worker | Not liable under 443.1215(1)(a); check again each quarter |
| Employee paid over USD 7,000 by a predecessor earlier in the year | Predecessor wages count toward the USD 7,000 (443.1217(2)(a)2) |
| Employee also worked for an unrelated Florida employer this year | Each employer has its own USD 7,000 base for that employee |
| New employer in its first 10 quarters | 2.7%, whatever its claims experience |
| Successor that chooses to adopt the predecessor's rate | Rate from the predecessor's record; it also takes on any outstanding tax liabilities |
| Employer delinquent more than one year, or failing to provide records on audit | May be assigned 5.4% |
| Two related employers wanting to combine payrolls | Not allowed ("payrolling"); each reports its own unless an approved common paymaster or employee leasing company |
| Second business unit with 10 or more employees | File Form BLS-3020 (Multiple Worksite Report) with the Department of Commerce |
| Last day of the month falls on a weekend or legal holiday | The filing period runs to the end of the next working day |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Rate notice not available, employer under 10 quarters old | 2.7%; ask for the RT-20 |
| Rate notice not available, older employer | Do not guess a rate; ask for the RT-20 or the eFile account |
| Prior wages paid this year to a new hire by a predecessor | Zero; ask if there was an acquisition |
| Number of employees in the last fiscal year | Assume electronic filing is required if near 10; ask |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Officer of a corporation with zero wages and large distributions | The Department may reclassify distributions as wages |
| Workers paid as contractors | Classification audit; refer worker status questions |
| Employee SSN beginning with 9, 000 or 666 | Invalid on the RT-6; the report can attract the erroneous report penalty |
| No RT-6 filed for quarters with no wages | A report is required even with no wages |

## Worked cases

**Case 1, a new employer's first quarter.** A business first hires in January 2026 and is liable from the first quarter. In the first quarter it pays three employees USD 40,000, USD 5,000 and USD 9,000. It is a new employer, so its rate is 2.7%.

```oa-check
name: Florida reemployment tax, new employer, first quarter 2026
inputs:
  wage_a: 40000
  wage_b: 5000
  wage_c: 9000
  wage_base: 7000
  rate: 0.027
steps:
  - taxable_a: min(wage_a, wage_base)
  - taxable_b: min(wage_b, wage_base)
  - taxable_c: min(wage_c, wage_base)
  - taxable_total: taxable_a + taxable_b + taxable_c
  - excess_wages: wage_a + wage_b + wage_c - taxable_total
  - tax_due: taxable_total * rate
expected:
  taxable_total: 19000
  excess_wages: 35000
  tax_due: 513.00
```

The RT-6 for the quarter shows total wages USD 54,000, excess wages USD 35,000, taxable wages USD 19,000 and tax USD 513.00, due by 30 April 2026. Employee B's remaining USD 2,000 of base is taxed in a later quarter as more wages are paid.

**Case 2, a decision: is a small business liable, and should it pay by installments?** A shop paid one part-time worker USD 1,200 in its best quarter of 2025 and had the worker on 22 different calendar weeks. The wages test fails but the weeks test passes, so it is liable. Its first-quarter 2026 tax is USD 513.00 (as in case 1). Paying by installments, the first quarter's tax is divided into four equal payments, with the USD 5 fee paid once with the first.

```oa-check
name: Florida liability test and first-quarter installment (2026)
inputs:
  best_quarter_wages: 1200
  weeks_with_worker: 22
  quarter_tax: 513
  installment_fee: 5
steps:
  - wages_test: min(floor(best_quarter_wages / 1500), 1)
  - weeks_test: min(floor(weeks_with_worker / 20), 1)
  - liable: max(wages_test, weeks_test)
  - installment: quarter_tax / 4
  - first_payment: installment + installment_fee
  - cost_of_installments: installment_fee
expected:
  wages_test: 0
  weeks_test: 1
  liable: 1
  installment: 128.25
  first_payment: 133.25
  cost_of_installments: 5
```

The installment option costs USD 5 for the year and spreads the first quarter's tax over four payments. It is open only if the RT-6 and the minimum installment are on time; there is no installment option for the fourth quarter.

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-FL-PR-ELC | Employee leasing company, PEO or common paymaster arrangement | Refer: the Department has separate rules for these |
| R-FL-PR-AGDOM | Agricultural labor or domestic service employers | Refer: separate thresholds in F.S. 443.1215 |
| R-FL-PR-RATE | Client asks to compute its experience rate | Refuse: use the RT-20 notice; protests go to the Department within 20 days |
| R-FL-PR-NONPROFIT | Nonprofit or government employer choosing reimbursement instead of tax | Refer |
| R-FL-PR-BENEFITS | Benefit claims, benefit charges or fraud reports | Refer to the Florida Department of Commerce |
| R-FL-PR-OTHERSTATE | Employee works in more than one state | Refer: localization rules decide which state's unemployment tax applies |

## Filing and payment

| Quarter | Form RT-6 and payment due by |
| --- | --- |
| 1st (January to March 2026) | 30 April 2026 |
| 2nd (April to June 2026) | 31 July 2026 |
| 3rd (July to September 2026) | 31 October 2026 |
| 4th (October to December 2026) | 31 January 2027 |

The report is due on the 1st day of the month after the quarter ends and is late if not postmarked by the last day of that month. An electronic payment must be initiated, with a confirmation number, by 5:00 p.m. ET on the business day before the due date. Installments: first quarter in four equal payments, second in three, third in two. Source: [DOR, Report and Payment Information](https://floridarevenue.com/taxes/taxesfees/Pages/rt_return_pay.aspx). The federal Form 940 and its credit for state reemployment tax paid are in `us-form-941-940-payroll`.

## Completion checklist

- Liability tested on both 443.1215(1)(a) tests for the current and preceding year.
- Registered with the Department; rate taken from the RT-20 (or 2.7% for a new employer).
- USD 7,000 base applied per employee, counting predecessor wages.
- Excluded payments (section 125, retirement plan contributions, and the others in step 5) left out of wages.
- Every SSN checked; RT-6 filed for every quarter, including quarters with no wages.
- Electronic filing used if 10 or more employees in any quarter of the last state fiscal year.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Florida Department of Revenue, Florida Reemployment Tax. Read for "Only the first $7,000 of wages paid to each employee by their employer in a calendar year is taxable" and the Department's role. | https://floridarevenue.com/taxes/taxesfees/Pages/reemployment.aspx | 2026-11-13 |
| Florida Department of Revenue, Reemployment Tax Rate Information. Read for the 2.7% initial rate for 10 quarters, the 2026 minimum 0.1% ($7) and maximum 5.4% ($378), the rate factors and the 20-day protest. | https://floridarevenue.com/taxes/taxesfees/Pages/rt_rate.aspx | 2026-11-13 |
| Florida Department of Revenue, Reemployment Tax Report and Payment Information. Read for Form RT-6 contents and due dates, electronic filing for 10 or more employees, penalties, wage exclusions and the installment option. | https://floridarevenue.com/taxes/taxesfees/Pages/rt_return_pay.aspx | 2026-11-13 |
| Florida Statutes 443.1215, Employers. Read for (1)(a) the $1,500 per quarter and 20-week tests and (1)(e) and (f) successors. | http://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0400-0499/0443/Sections/0443.1215.html | 2026-11-13 |
| Florida Statutes 443.1217, Wages. Read for (1) the definition of wages and (2)(a)2 the $7,000 base from 1 January 2015. | http://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0400-0499/0443/Sections/0443.1217.html | 2026-11-13 |
| Florida Constitution, Article VII, section 5. Read for no tax on the income of natural persons who are residents. | https://www.flsenate.gov/Laws/Constitution | 2026-11-13 |

Not yet confirmed: none of the figures above; the 2026 interest rate on late payments is published by the Department in Tax Information Publications and is not stated here.
