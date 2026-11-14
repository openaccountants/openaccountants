---
name: il-payroll
description: "Run Illinois employer payroll for 2026. State income tax withholding at 4.95% after the IL-W-4 allowances ($2,925 per Line 1 allowance and $1,000 per Line 2 allowance for 2026), the monthly or semi-weekly payment schedule set by the $12,000 look-back test, quarterly Form IL-941 due dates, W-2 filing, the reciprocal agreements with Iowa, Kentucky, Michigan and Wisconsin, and Illinois unemployment insurance with IDES (2026 wage base $14,250, rates 0.750% to 7.050%, new-employer rate 3.350%, quarterly Form UI-3/40). Also covers the Secure Choice retirement mandate and its penalties, the 40-hour statewide paid leave rule, final pay timing and the unemployment ABC test. Trigger on \"Illinois payroll\", \"IL-941\", \"IL-W-4\", \"IL-700-T\", \"IDES\", \"Illinois SUTA\", \"Illinois unemployment rate\", \"Secure Choice\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/il-payroll"
  jurisdiction: "US-IL"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Illinois payroll: withholding and unemployment insurance, tax year 2026

> **Source-cited draft.** Built from the 2026 Booklet IL-700-T, IDOR Publications 130, 131 and 131-D (2026), IDOR Informational Bulletin FY 2026-15, the IDES 2026 Historical Rate Chart and 2026 Form UI-3/40, and 820 ILCS 80/5, 80/85, 115/4, 115/5, 192/15, 405/205 and 405/212 (Illinois General Assembly), read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026, withhold Illinois income tax at **4.95%** of wages after subtracting the employee's allowances: **$2,925** for each allowance on IL-W-4 Line 1 and **$1,000** for each allowance on Line 2, divided by the number of pay periods (Booklet IL-700-T). Pay monthly by the 15th unless more than **$12,000** was withheld in the look-back period, which puts the employer on the semi-weekly schedule. File Form IL-941 every quarter: **30 April, 31 July and 2 November 2026, and 1 February 2027**. Illinois unemployment insurance for 2026 is due on the first **$14,250** of each worker's wages, at rates from **0.750%** to **7.050%**; a new employer pays **3.350%** (3.450% in NAICS sector 56) (IDES).

## Scope and who this is for

In scope: a private employer with employees working in Illinois in 2026: Illinois income tax withholding, payments and Form IL-941, Illinois W-2 filing, IL-W-4 and IL-W-5-NR, Illinois unemployment insurance contributions and Form UI-3/40, and the state rules that touch payroll (Secure Choice, statewide paid leave, pay timing, final pay, the unemployment ABC test).

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Federal withholding, FICA, FUTA, Forms 941, 940, W-2 and W-3 | `us-form-941-940-payroll` |
| New-hire reporting by state | `us-state-new-hire-reporting-matrix` |
| The employee's own Illinois return | `il-income-tax` |
| Withholding for the employee's other state, multi-state allocation | `us-multi-state-residency-and-allocation` |
| Chicago and Cook County leave and scheduling ordinances | not covered (see Not yet confirmed) |

## Ask the client first

1. **Where each employee works**, and where each lives. Residents of Iowa, Kentucky, Michigan and Wisconsin working in Illinois may file IL-W-5-NR.
2. **IL-W-4 for each employee**: allowances on Line 1, on Line 2, and any extra amount on Line 3. No IL-W-4 means withhold with no allowances.
3. **Pay frequency** (weekly, biweekly, semi-monthly, monthly).
4. **Illinois withholding reported in the look-back period** (1 July 2024 to 30 June 2025 for 2026), and whether more than $12,000 has been withheld in any quarter of 2026.
5. **IDES account number and the 2026 contribution rate** on the annual rate notice, or the date the business first paid Illinois wages (new employer).
6. **Number of Illinois employees in each quarter of 2025, years in business, and any qualified retirement plan** (Secure Choice).
7. **Anyone paid as a contractor** who works under the business's direction (ABC test).

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Withholding rate on wages after allowances (effective 1 January 2026) | 4.95% | [Booklet IL-700-T (2026)](https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/withholding/documents/currentyear/il-700-t.pdf) |
| Exemption allowance per IL-W-4 Line 1 allowance | $2,925 | [Booklet IL-700-T (2026)](https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/withholding/documents/currentyear/il-700-t.pdf) |
| Allowance per IL-W-4 Line 2 allowance (65 or older, blind) | $1,000 | [Booklet IL-700-T (2026)](https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/withholding/documents/currentyear/il-700-t.pdf) |
| Look-back withholding above which the employer pays semi-weekly | more than $12,000 | [IDOR Publication 131](https://tax.illinois.gov/research/publications/pubs/withholding-income-tax-payment-and-filing-requirements.html) |
| Monthly payers: payment due | 15th of the following month | [IDOR Publication 131-D (2026)](https://tax.illinois.gov/content/dam/soi/en/web/tax/research/publications/pubs/documents/2026-pub-131-d.pdf) |
| Form IL-941 due dates for 2026 quarters | 30 April 2026, 31 July 2026, 2 November 2026, 1 February 2027 | [IDOR Publication 131-D (2026)](https://tax.illinois.gov/content/dam/soi/en/web/tax/research/publications/pubs/documents/2026-pub-131-d.pdf) |
| Forms W-2 for 2025 due to IDOR (electronic) | 2 February 2026 | [IDOR Bulletin FY 2026-15](https://tax.illinois.gov/research/publications/bulletins/fy-2026-15.html) |
| Unemployment insurance taxable wage base per worker | $14,250 | [IDES 2026 Historical Rate Chart](https://ides.illinois.gov/content/dam/soi/en/web/ides/ides_forms_and_publications/UI_tax_rates_2026.pdf) |
| Minimum contribution rate (includes the fund builder) | 0.750% | [IDES 2026 Historical Rate Chart](https://ides.illinois.gov/content/dam/soi/en/web/ides/ides_forms_and_publications/UI_tax_rates_2026.pdf) |
| Maximum contribution rate (includes the fund builder) | 7.050% | [IDES 2026 Historical Rate Chart](https://ides.illinois.gov/content/dam/soi/en/web/ides/ides_forms_and_publications/UI_tax_rates_2026.pdf) |
| Standard rate for employers not yet experience rated (new employers) | 3.350% | [IDES 2026 Historical Rate Chart](https://ides.illinois.gov/content/dam/soi/en/web/ides/ides_forms_and_publications/UI_tax_rates_2026.pdf) |
| Standard rate, Administrative Support and Waste Management (NAICS 56) | 3.450% | [IDES 2026 Historical Rate Chart](https://ides.illinois.gov/content/dam/soi/en/web/ides/ides_forms_and_publications/UI_tax_rates_2026.pdf) |
| Fund builder rate (included in every rate) | 0.550% | [IDES 2026 Historical Rate Chart](https://ides.illinois.gov/content/dam/soi/en/web/ides/ides_forms_and_publications/UI_tax_rates_2026.pdf) |
| State experience factor | 102% | [IDES 2026 Historical Rate Chart](https://ides.illinois.gov/content/dam/soi/en/web/ides/ides_forms_and_publications/UI_tax_rates_2026.pdf) |
| Small employer rate cap: quarter's total wages under $50,000 | lesser of the assigned rate or 5.4% | [IDES 2026 Form UI-3/40, line 5A](https://ides.illinois.gov/content/dam/soi/en/web/ides/ides_forms_and_publications/UI-340.pdf) |
| UI-3/40 due: last day of the month after the quarter | 30 April, 31 July, 31 October, 31 January | [IDES 2026 Form UI-3/40 instructions](https://ides.illinois.gov/content/dam/soi/en/web/ides/ides_forms_and_publications/UI-340.pdf) |
| UI late payment interest | 2% per month | [IDES 2026 Form UI-3/40, line 6A](https://ides.illinois.gov/content/dam/soi/en/web/ides/ides_forms_and_publications/UI-340.pdf) |
| UI late report penalty | $5 per $10,000 of total wages (or fraction), or $2,500 a month if less; $50 minimum | [IDES 2026 Form UI-3/40, line 6B](https://ides.illinois.gov/content/dam/soi/en/web/ides/ides_forms_and_publications/UI-340.pdf) |
| UI coverage: wages paid in any calendar quarter of the current or preceding year | at least $1,500 | [820 ILCS 405/205(B)(3)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=082004050K205) |
| Secure Choice: employees in Illinois in every quarter of the previous year | at least 5 | [820 ILCS 80/5](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=082000800K5) |
| Secure Choice penalty, first noncompliant calendar year | $250 per employee | [820 ILCS 80/85(a)(1)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=082000800K85) |
| Secure Choice penalty, each later noncompliant calendar year | $500 per employee | [820 ILCS 80/85(a)(2)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=082000800K85) |
| Statewide paid leave: minimum per 12-month period, accrued 1 hour per 40 hours worked | 40 hours | [820 ILCS 192/15(a), (b)](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=082001920K15) |

The 4.95% rate and the $1,000 Line 2 allowance are fixed; the $2,925 allowance follows the individual exemption, which is indexed every year. The IDES wage base and rates are set each year.

### Withholding: the percentage formula (IL-700-T)

1. **Allowances**: Line 1 allowances x $2,925, plus Line 2 allowances x $1,000.
2. **Per pay period**: divide by the number of pay periods in the year (52 weekly, 26 biweekly, 24 semi-monthly, 12 monthly).
3. **Taxable amount** = wages for the period - the per-period allowances.
4. **Tax** = taxable amount x 4.95%. Add any Line 3 extra amount. The wage-bracket tables in the booklet give the same result.
5. **No IL-W-4**, or an IL-W-4 that must be disregarded (the employee claims total exemption without a matching federal W-4 exemption, or the IRS has told the employer to disregard the federal W-4): withhold with no allowances (Publication 130). An employee who is exempt from federal withholding can still owe Illinois withholding if pay exceeds the allowance. Ask each employee to review the IL-W-4 before 1 December.

### Withholding: who, when and where

6. **Who**: compensation paid in Illinois (services localized in Illinois) to anyone except qualifying residents of Iowa, Kentucky, Michigan and Wisconsin who file Form IL-W-5-NR, and military spouses (Publication 130). Without an IL-W-5-NR, withhold Illinois tax. An employee who moves must notify the employer within 10 days. Illinois has no reciprocal agreement with Indiana or Missouri: residents of those states working in Illinois are withheld at 4.95%.
7. **Payment schedule** (Publication 131): first-year employers, and employers who reported $12,000 or less in the look-back period (the year ending 30 June of the previous calendar year), pay monthly by the 15th. More than $12,000 in the look-back period: semi-weekly, by Wednesday for amounts withheld the previous Wednesday to Friday and by Friday for amounts withheld the previous Saturday to Tuesday, electronically. An employer that withholds more than $12,000 in a quarter pays semi-weekly from the next quarter for the rest of the year and the next year. A due date on a weekend or state holiday moves to the next business day.
8. **Form IL-941**: every quarter, electronically (waiver on Form IL-900-EW), with the withholding detail in Step 4. For 2026: 30 April, 31 July, 2 November 2026 and 1 February 2027 (Publication 131-D).
9. **W-2s**: send Forms W-2 to IDOR electronically; for 2025 forms the date was 2 February 2026 (Bulletin FY 2026-15). Box 16 shows wages paid in Illinois, or paid to an Illinois resident working in a reciprocal state.

### Unemployment insurance (IDES)

10. **Coverage**: an employing unit becomes liable once it pays at least $1,500 of wages in a calendar quarter, or employs at least one person on some part of a day in 20 or more weeks, in the current or preceding year (820 ILCS 405/205(B)(3)).
11. **Taxable wages**: each worker's first $14,250 of 2026 wages (UI-3/40 line 3 removes the excess).
12. **Rate**: the rate on the annual IDES rate notice. New employers pay the standard rate of 3.350% (3.450% in NAICS 56) until experience rated; experience-rated employers (three or more years) pay a rate based on their benefit ratio, between 0.750% and 7.050%. If the quarter's total wages are under $50,000, use the lesser of the assigned rate or 5.4%.
13. **Contribution** = taxable wages x rate. File Form UI-3/40 with the worker detail and pay through MyTax Illinois by the last day of the month after the quarter. Employers with 25 or more employees must file electronically.

### Other state rules that touch payroll

- **Secure Choice** (820 ILCS 80/5, 80/85): an employer with at least 5 Illinois employees in every quarter of the previous calendar year, in business at least 2 years, that does not offer or contribute to a qualified plan (401(a), 401(k), 403(a), 403(b), 408(k) SEP, 408(p) SIMPLE, 457(b)) must enroll its employees in the Illinois Secure Choice payroll-deduction IRA. An employer that fails without reasonable cause to enroll employees and remit contributions pays $250 per employee for the first noncompliant calendar year and $500 per employee for each later one, which need not be consecutive. IDOR counts employees by the annual average of employer-reported quarterly data, sends a notice of proposed assessment, and the employer has 120 days to protest or comply.
- **Paid leave** (820 ILCS 192/15): an employee working in Illinois earns at least 40 hours of paid leave in a 12-month period, 1 hour per 40 hours worked; overtime-exempt employees are treated as working 40 hours a week. The employer may front-load the 40 hours instead, and then need not carry over unused hours. The minimum increment the employer may set is no more than 2 hours a day.
- **Pay timing** (820 ILCS 115/4): wages for a semi-monthly or biweekly period are paid within 13 days after the period ends; weekly within 7 days; daily within 24 hours; executive, administrative and professional employees within 21 calendar days.
- **Final pay** (820 ILCS 115/5): at separation if possible, and no later than the next regularly scheduled payday. Earned, unused vacation under the employer's policy is paid as part of final compensation and cannot be forfeited.
- **ABC test for unemployment insurance** (820 ILCS 405/212): a person paid for services is in employment unless the business proves all three: (A) free from control or direction, under contract and in fact; (B) the work is outside the usual course of the business, or outside all its places of business; (C) the person is in an independently established trade or business.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Wisconsin, Iowa, Kentucky or Michigan resident working in Illinois with IL-W-5-NR on file | No Illinois withholding; the employer may, but need not, withhold for the home state |
| Indiana or Missouri resident working in Illinois | Withhold Illinois tax at 4.95%; no reciprocal agreement |
| Employee with no IL-W-4 | Withhold with no allowances |
| Employee exempt federally, wages above the allowance | Still withhold Illinois tax |
| Withholding passes $12,000 during a quarter | Semi-weekly from the next quarter |
| Worker paid more than $14,250 in 2026 | UI only on the first $14,250 |
| Quarter's total wages under $50,000 | UI at the lesser of the assigned rate or 5.4% |
| Retirement income paid to a retiree | Most is exempt from Illinois tax and needs no withholding; a voluntary agreement uses IL-W-4 |
| Employer with fewer than 5 employees in some quarter of 2025, or in business under 2 years | Not required to join Secure Choice; may join voluntarily as a small employer |
| Contractor directed like an employee, doing the business's core work | Fails the ABC test: report as an employee for unemployment insurance |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| IL-W-4 | No allowances |
| Look-back withholding | Monthly schedule if a first-year employer; otherwise ask for the IDOR schedule notice |
| 2026 IDES rate notice | Standard rate 3.350% for a new employer; ask for the notice for anyone else |
| Work location of a remote employee | Ask; localization decides whether Illinois withholding applies |
| Retirement plan status | Assume no qualified plan; check Secure Choice |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Payroll software still on the 2025 $2,850 allowance | Under-withholding all year |
| Semi-weekly employer paying monthly | Late-payment penalties |
| Five or more Illinois employees, no retirement plan | Secure Choice penalties of $250, then $500, per employee per year |
| Workers paid on 1099 forms | IDES applies the ABC test |
| UI-3/40 filed on paper with 25 or more employees | Electronic filing is required |

## Worked cases

**Case 1, withholding for one weekly pay.** IL-700-T's own example: an employee paid $800 a week claims two allowances on IL-W-4 Line 1 and two on Line 2, no extra amount.

Allowances: 2 x $2,925 + 2 x $1,000 = $7,850 a year, divided by 52 = $150.96 a week. Taxable amount $800 - $150.96 = $649.04. Tax at 4.95% = **$32.13**, the figure IDOR gives.

```oa-check
name: Illinois weekly withholding, IL-700-T example (2026)
inputs:
  weekly_wages: 800
  line1_allowances: 2
  line2_allowances: 2
steps:
  - annual_allowances: line1_allowances * 2925 + line2_allowances * 1000
  - weekly_allowances: annual_allowances / 52
  - taxable: weekly_wages - weekly_allowances
  - withholding: round(taxable * 0.0495, 2)
expected:
  annual_allowances: 7850.00
  withholding: 32.13
```

**Case 2, a new employer's 2026 unemployment insurance.** A new non-construction employer outside NAICS 56 (standard rate 3.350%) pays four workers $30,000 each and one worker $10,000 in 2026, and its total wages are $50,000 or more in the quarters where the wage base is reached.

Taxable wages: 4 x $14,250 + $10,000 = $67,000. Contribution at 3.350% = **$2,244.50** for the year. In any quarter where total wages are under $50,000, the rate is the lesser of 3.350% and 5.4%, so still 3.350%.

```oa-check
name: Illinois unemployment insurance, new employer (2026)
inputs:
  workers_over_base: 4
  wage_base: 14250
  other_worker_wages: 10000
  rate: 0.0335
steps:
  - taxable_wages: workers_over_base * wage_base + min(other_worker_wages, wage_base)
  - small_employer_rate: min(rate, 0.054)
  - contribution: taxable_wages * rate
expected:
  taxable_wages: 67000.00
  small_employer_rate: 0.0335
  contribution: 2244.50
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-PAY-MULTI | Employee works in Illinois and another state in the same period | Refer: localization and the other state's rules |
| R-PAY-SUCC | Business bought from another employer (UI experience transfer) | Refer: successor rules under 820 ILCS 405/205(C) and (D) are fact-heavy |
| R-PAY-CLASS | IDES or IDOL classification audit, or construction workers paid as contractors | Refer: penalties under several Acts |
| R-PAY-GOV | Government, school or nonprofit reimbursing employer | Refer |
| R-PAY-HH | Household employer | Refer: IDOR Publication 121 and the federal Schedule H |
| R-PAY-CHI | Chicago or Cook County leave, scheduling or minimum wage questions | Refer: local ordinances are outside this skill |

## Filing and payment

Register for withholding and for unemployment insurance through MyTax Illinois (mytax.illinois.gov). Pay withholding electronically or with Form IL-501 (semi-weekly payers must pay electronically); file Form IL-941 electronically each quarter; send Forms W-2 to IDOR electronically. File Form UI-3/40 and pay contributions through MyTax Illinois by the last day of the month after each quarter; a quarter with no wages still needs a report while the account is open.

## Completion checklist

- 2026 allowance of $2,925 (Line 1) and $1,000 (Line 2) loaded in payroll.
- IL-W-4 on file for every Illinois employee; IL-W-5-NR for each reciprocal-state resident.
- Payment schedule matches the $12,000 look-back test; IL-941 dates diarised.
- UI wage base $14,250 and the 2026 rate notice applied; UI-3/40 filed each quarter.
- Secure Choice status documented (enrolled, exempt, or qualified plan).
- Paid leave accrual (or front-loading) policy in writing; final pay by the next payday.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Booklet IL-700-T, 2026 Illinois Withholding Tax Tables (R-12/25). Read for the 4.95% rate, the $2,925 and $1,000 allowances, the formula steps and the $800 weekly example ($32.13). | https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/withholding/documents/currentyear/il-700-t.pdf | 2026-11-13 |
| IDOR Publication 131. Read for the monthly and semi-weekly schedules, the $12,000 look-back test and the look-back period definition. | https://tax.illinois.gov/research/publications/pubs/withholding-income-tax-payment-and-filing-requirements.html | 2026-11-13 |
| IDOR Publication 131-D (January 2026). Read for the 2026 payment dates and the IL-941 dates (30 April, 31 July, 2 November 2026, 1 February 2027) and the electronic filing rule. | https://tax.illinois.gov/content/dam/soi/en/web/tax/research/publications/pubs/documents/2026-pub-131-d.pdf | 2026-11-13 |
| IDOR Publication 130, Withholding Illinois Income Tax for My Employees. Read for localization, the four reciprocal states, IL-W-4 and IL-W-5-NR rules and W-2 box 16. | https://tax.illinois.gov/research/publications/pubs/who-is-required-to-withhold-illinois-income-tax/withholding-illinois-income-tax-for-my-employees.html | 2026-11-13 |
| IDOR Informational Bulletin FY 2026-15. Read for the 2026 withholding schedules and the W-2 date of 2 February 2026. | https://tax.illinois.gov/research/publications/bulletins/fy-2026-15.html | 2026-11-13 |
| IDES 2026 Historical Rate Chart. Read for the 2026 column: wage base $14,250, minimum 0.750%, maximum 7.050%, standard 3.350%, NAICS 56 3.450%, fund builder 0.550%, state experience factor 102%, small employer rate 5.4%. | https://ides.illinois.gov/content/dam/soi/en/web/ides/ides_forms_and_publications/UI_tax_rates_2026.pdf | 2026-11-13 |
| IDES Annual Employer Contribution Rates page. Read for the experience-rating rule (three or more years). | https://ides.illinois.gov/employer-resources/taxes-reporting/rates.html | 2026-11-13 |
| IDES Form UI-3/40 (Rev. 3/2026) and instructions. Read for the $14,250 line 3, the under-$50,000 rule, interest at 2% a month, the late penalty, the due dates and the 25-employee electronic rule. | https://ides.illinois.gov/content/dam/soi/en/web/ides/ides_forms_and_publications/UI-340.pdf | 2026-11-13 |
| 820 ILCS 405/205. Read for (B)(3) the $1,500 quarter and 20-week coverage tests. | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=082004050K205 | 2026-11-13 |
| 820 ILCS 405/212. Read for the three-part ABC test. | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=082004050K212 | 2026-11-13 |
| 820 ILCS 80/5. Read for the Secure Choice employer definition (5 employees every quarter, 2 years, no qualified plan). | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=082000800K5 | 2026-11-13 |
| 820 ILCS 80/85. Read for the $250 and $500 penalties, the reasonable-cause wording, the annual-average count and the 120-day protest. | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=082000800K85 | 2026-11-13 |
| 820 ILCS 192/15. Read for 40 hours, 1 per 40 worked, front-loading and the 2-hour increment. | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=082001920K15 | 2026-11-13 |
| 820 ILCS 115/4. Read for the 13-day, 7-day, 24-hour and 21-day pay timing rules. | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=082001150K4 | 2026-11-13 |
| 820 ILCS 115/5. Read for final pay by the next regular payday and vacation payout. | https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=082001150K5 | 2026-11-13 |

Illinois sites refused direct connections from this machine; every page above was read through a Firecrawl fetch of the official URL on 2026-11-13.

Not yet confirmed: the supplemental wage method (86 Ill. Adm. Code 100.7110, not read; IL-700-T says only that wages and other compensation are withheld at 4.95% after exemptions); the Secure Choice default contribution rate, auto-escalation and the enrollment deadlines in 820 ILCS 80/60 (not read); the 2026 W-2 and 1099 filing dates for 2026 forms (the 2 February 2026 date is for 2025 forms); the date the 2026 new-employer rate applies to construction employers (the chart shows no separate construction rate for 2026); Chicago Paid Leave and Paid Sick and Safe Leave Ordinance, Cook County Earned Sick Leave Ordinance and Chicago Fair Workweek Ordinance terms (municipal codes not read); One Day Rest in Seven Act (820 ILCS 140) rest day and meal period rules; the Employee Classification Act (820 ILCS 185) construction penalties; UI successor and voluntary contribution rules (820 ILCS 405/1500 and 1507, not read).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `il-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/il-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
