---
name: bm-payroll-social
description: >
  Bermuda payroll tax and social insurance for employers, employees and the self-employed
  for the payroll tax year 1 April 2026 to 31 March 2027 and the contribution year from
  3 August 2026. Covers the employer portion by class of taxpayer, the five employee
  portion bands, the BMD 1,000,000 cap, the dividend deductible, new hire and senior relief,
  quarterly e-tax filing, contributory pension contributions and occupational pension
  membership, 5% contributions and remittance. Trigger phrases include Bermuda payroll tax, employee portion, employer
  portion, etax.gov.bm, social insurance Bermuda, contributory pension, BMD 78.50 a week.
version: "1.1"
jurisdiction: BM
tax_year: 2026
tax_year_notes: "Payroll tax year 1 April 2026 to 31 March 2027; contribution year from 3 August 2026"
last_updated: 2026-11-14
category: payroll
type: computation
domain: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Bermuda payroll tax and social insurance v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This skill computes Bermuda payroll tax (Payroll Tax Act 1995 and Payroll Tax Rates Act 1995, administered by the Office of the Tax Commissioner) and contributory pension (social insurance) contributions under the Contributory Pensions Act 1970 (Department of Social Insurance). Bermuda has no personal income tax: payroll tax is the tax on employment income, and it has an employer portion and an employee portion. The employer is liable for both portions; it may deduct the employee portion from pay.

Who is in: every employer, self-employed person and deemed employee paying remuneration for services provided in Bermuda, including exempted companies and foreign contractors and subcontractors working in Bermuda ([Payroll tax](https://www.gov.bm/payroll-tax)). Who is out of this skill: corporate income tax ([bm-corporate-income-tax](bm-corporate-income-tax.md)), customs, land tax and stamp duty ([bermuda-tax](bermuda-tax.md)).

Tax year: payroll tax runs 1 April to 31 March; this skill uses the 1 April 2026 to 31 March 2027 rates. Social insurance runs on a contribution year from the first Monday of August; this skill uses the rates with effect from 3 August 2026. Amounts are BMD, which trades at par with the US dollar.

## Ask the client first

1. Total annual remuneration of the employer (or quarterly remuneration), and whether it is an exempted undertaking, a hotel or restaurant, a fashion retailer or another named class. This picks the employer rate.
2. Each employee's annual rate of pay, including benefits in kind and bonuses. This sets the employee portion band.
3. Whether any employee qualifies for relief: new hire (exempted company or employer with remuneration above BMD 500,000), Bermudian aged 65 or over, approved training scheme, special situations.
4. Dividends paid to persons who provide services to a local (unlisted) company, per person per year.
5. Each worker's age and weekly hours (social insurance applies above 4 hours a week; employer only from age 65).
6. Whether the worker is self-employed, a deemed employee or a student in vacation work.

## The method, step by step

### Rates, bands and thresholds

| Item | 2026-27 figure and conditions | Official source |
|---|---|---|
| Employer rate, Government, parish councils, registered charities, religious and cultural bodies, new start-ups (4 quarters), Economic Empowerment Zone employer (9 quarters) | 0% | [Calculating payroll tax 2026-27](https://www.gov.bm/calculating-payroll-tax-2026) |
| Employer rate, new hire remuneration and special situations (jury duty, Regiment, farmers, fishermen, hotel and restaurant staff November to March, retail staff January to March, permanent disability, approved training, maternity or paternity leave, approved caregiver); excludes dividend and bonus payments | 0% | same |
| Employer rate, self-employed farmers and fishermen | 0% | same |
| Employer rate, Class B(f), annual payroll less than BMD 200,000 | 0.5% for the April to June and July to September 2026 quarters; 1.0% for October to December 2026 and later tax periods (Payroll Tax Rates Amendment Act 2026, 2026:31, s.2; the June 2026 calculation page still shows 0.5%) | [Payroll Tax Rates Act 1995 s.5](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1995/Payroll%20Tax%20Rates%20Act%201995); [Act 2026:31](https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2026/Payroll%20Tax%20Rates%20Amendment%20Act%202026) |
| Employer rate, educational, sporting or scientific institutions | 1.00% | same |
| Employer rate, self-employed horticulturist | 1.75% | same |
| Employer rate, Class BB(a), annual payroll not less than BMD 200,000 and not more than BMD 350,000 | 2.00% | [Payroll Tax Rates Act 1995 s.5](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1995/Payroll%20Tax%20Rates%20Act%201995) |
| Employer rate, Class B: Bermuda Hospitals Board, Corporation of Hamilton and Corporation of St George's (no payroll threshold); licensed residential care home with annual payroll more than BMD 350,000 | 3.00% | [Payroll Tax Rates Act 1995 s.5](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1995/Payroll%20Tax%20Rates%20Act%201995) |
| Employer rate, Class A, hotel or restaurant with annual payroll more than BMD 350,000 (the Act's test is strictly more than; the calculation page says 350,000 or more) | 4.00% | [Payroll Tax Rates Act 1995 s.5](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1995/Payroll%20Tax%20Rates%20Act%201995) |
| Employer rate, annual remuneration over BMD 350,000 to 500,000 | 4.75% | same |
| Employer rate, Class AA, qualifying retail store: payroll for the store or group of stores over BMD 500,000 and a Commissioner determination, on written application, that at least 50% of the period's sales are clothing, shoes, jewellery and perfume | 5.00% | [Payroll Tax Rates Act 1995 s.5A](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1995/Payroll%20Tax%20Rates%20Act%201995) |
| Employer rate, annual payroll over BMD 500,000 up to 1,000,000 | 7.00% | same |
| Employer rate, annual payroll over BMD 1,000,000 (over BMD 250,000 a quarter) | 9.50% | same |
| Employer rate, exempt undertakings (an exempted undertaking or a permit company under Payroll Tax Act s.2(3), not every exempted company) and the standard rate | 9.75% | [Payroll Tax Rates Act 1995 s.3](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1995/Payroll%20Tax%20Rates%20Act%201995) |
| Employee portion band 1, annual remuneration 0 to 48,000 | 0.25% | same |
| Employee portion band 2, above the first 48,000 up to 96,000 | 7.75% | same |
| Employee portion band 3, 96,001 to 200,000 | 10.75% | same |
| Employee portion band 4, 200,001 to 500,000 | 11.50% | same |
| Employee portion band 5, 500,001 to 1,000,000 | 12.50% | same |
| Tax cap, remuneration per person per year | BMD 1,000,000; remuneration above it is not taxed | same |
| Dividend deductible, from 1 April 2026: dividends on shares in a company to an employee or deemed employee of that company, where the company is not an exempt undertaking or a listed company (those dividends to the company's own employees are excluded in full by s.7(2)(h)) | First BMD 20,000 per person per year excluded (s.7(2)(i)); the excess is remuneration, up to the cap | [Payroll Tax Act 1995 s.7(2)](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1995/Payroll%20Tax%20Act%201995); [2026-27 rates](https://www.gov.bm/calculating-payroll-tax-2026) |
| Bermudian aged 65 or over relief | Employer portion relief on remuneration up to and including BMD 24,000 per tax period (quarter), excluding bonuses; employee portion still due; relief from the quarter the application is received | [Payroll Tax Act 1995 s.9AA](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1995/Payroll%20Tax%20Act%201995); [2026-27 rates](https://www.gov.bm/calculating-payroll-tax-2026) |
| Social insurance, employed person over school-leaving age and under 65 | BMD 39.25 employee plus BMD 39.25 employer, BMD 78.50 a week, from 3 August 2026 | [Contribution calendar 2026-27](https://socialinsurance.gov.bm/Portals/0/calendars/Contribution-Calendar-2027.pdf) |
| Social insurance, employed person over 65 | BMD 39.25 a week, employer only | same |
| Social insurance, self-employed under 65 | BMD 78.50 a week | same |
| Social insurance, self-employed over 65 | BMD 39.25 a week | same |
| Social insurance, voluntary contributor under 65 | BMD 78.50 a week | same |
| Social insurance, yearly rate at the full weekly rate | BMD 4,082.00 | same |
| Social insurance, small-income certificate | Annual income not exceeding BMD 3,000 (inclusive); only with a certificate granted by the Director on application, backdated by up to 13 weeks at the Director's discretion; covers the insured person's contribution for whole weeks only, not the employer's | [Exception from Liability Regulations 1973, regs 1-2](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1973/Contributory%20Pensions%20(Exception%20from%20Liability%20for%20Contributions)%20Regulations%201973) |
| Social insurance, payment due | Each contribution week's contributions by the last working day of the following month | [Contributory Pensions Act 1970 s.4(7)](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1970/Contributory%20Pensions%20Act%201970) |
| Social insurance, self-employed registration | Register with the Director within 7 days of becoming self-employed | [Contributory Pensions Act 1970 s.8](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1970/Contributory%20Pensions%20Act%201970) |
| Occupational pension, employee membership | Eligible employee (a Bermudian, or the spouse of a Bermudian, employed in Bermuda) aged 23 or over and below the plan's normal retirement age, with 720 or more hours with that employer in a calendar year; tested per employer, hours are not pooled | [National Pension Scheme (Occupational Pensions) Act 1998 ss.2 and 17](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1998/National%20Pension%20Scheme%20(Occupational%20Pensions)%20Act%201998) |
| Occupational pension, defined contribution rate | 5% of pensionable earnings each from member and employer (First Schedule, from 1 January 2004); pensionable earnings capped at BMD 200,000 a year and exclude overtime above 35 hours a week, severance and health premiums | same, ss.2 and 19 and First Schedule |
| Occupational pension, remittance | Withhold at least monthly; pay member and employer shares into the fund within 30 days following the month of withholding | same, s.19(5) |
| Occupational pension, self-employed | Register if aged 23 or over, below normal retirement age, with self-employment pensionable earnings exceeding BMD 20,000 a year; contribute twice the scheduled rate (10% at the 5% rate) within 60 days after the calendar year, capped at BMD 10,000 a year | [National Pension Scheme (General) Regulations 1999, regs 21-22](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1999/National%20Pension%20Scheme%20(General)%20Regulations%201999) |

### Steps

1. **Classify the employer.** Use annual remuneration for the year (or the quarterly equivalents shown above) and the class list. The class sets one employer rate on gross taxable remuneration; it is not a banded rate. An exempt undertaking pays 9.75% whatever its payroll size, unless a 0% class or relief applies to specific remuneration ([2026-27 rates](https://www.gov.bm/calculating-payroll-tax-2026)). "Exempt undertaking" is the Payroll Tax Act s.2(3) to (5) test, not the Companies Act label: an exempted company that needs a Companies Act licence or other statutory authority for any of its business is not an exempt undertaking unless the Commissioner directs otherwise. An unknown class means ask; 9.75% is not a fallback ([Payroll Tax Act 1995 s.2](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1995/Payroll%20Tax%20Act%201995)).
2. **Build taxable remuneration.** Wages, salaries and benefits in cash or kind for services provided in Bermuda. For a self-employed person or deemed employee it is the amount taken out of the business for personal use. Add dividends above BMD 20,000 per person per year paid to service providers of a local unlisted company and report them in section C of the return each time dividends are paid or declared. Exclude employer contributions to approved pension, life insurance and health insurance schemes, weekend or vacation work by students and certain lay-off allowances. A person under 16, or employed 16 hours or less in each month of a tax period, is not an employee (the 16-hour rule does not apply to the self-employed) ([Payroll tax](https://www.gov.bm/payroll-tax)).
3. **Apply the cap.** Stop at BMD 1,000,000 per person per year.
4. **Employer portion.** Taxable remuneration times the employer rate. New hire and special-situation remuneration is at 0% for the employer portion only.
5. **Employee portion.** Apply the five marginal bands to each person's annual rate of pay. For pay that fluctuates, recompute the annual rate each pay period (the Office publishes weekly, bi-weekly, semi-monthly and monthly calculators).
6. **Social insurance.** One weekly contribution per person for each contribution week (Monday to Sunday) in which the person works more than 4 hours for one employer; 4 hours or less for any one employer does not make the person insured by that work, and a person not ordinarily resident is not insured until gainfully occupied in Bermuda for 26 consecutive weeks ([Contributory Pensions Act 1970 s.2(5) and (6)](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1970/Contributory%20Pensions%20Act%201970)). Only one employee and one employer contribution per person per week; where there are several employers, the first employer that week pays. The employer may recover only the employee's contribution, from pay for the same week; its own contribution can never be recovered from the worker (s.7). Pay each week's contributions by the last working day of the following month (s.4(7)); employers are billed a month in arrears ([Employers](https://socialinsurance.gov.bm/Contributions/Employers)).
7. **Occupational pension.** For a Bermudian (or spouse of a Bermudian) employee who meets the age 23 and 720-hour tests, withhold 5% of pensionable earnings (capped at BMD 200,000) and add the employer's 5%, paid into the plan within 30 days after the month of withholding. Defined benefit and collective-agreement plans follow their own funding rules, not 5% plus 5%.
8. **File and pay** (see Filing and payment).

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Exempted company employing staff in Bermuda | Payroll tax applies. It is an exempt undertaking (9.75%) only if it meets Payroll Tax Act s.2(3) to (5); an exempted company needing a licence or statutory authority for any of its business is classified under the ordinary classes unless the Commissioner directs it is an exempt undertaking. Exempted status is never a payroll tax exemption | [Payroll Tax Act 1995 s.2](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1995/Payroll%20Tax%20Act%201995) |
| New Hire Relief 2026 | For exempted companies and other employers with remuneration over BMD 500,000 that increase full-time equivalents (15 hours or more a week) above the January to March 2025 baseline. Qualifying employees: hired 1 April 2025 to 31 March 2026 and still employed after 1 April 2026, or hired 1 April 2026 to 31 March 2028, not previously employed by a parent or affiliate. Employer portion exemption only. Apply by the end of the quarter in which the employee qualifies; no retroactive approval | same |
| Self-employed caregiver | 0% employer portion; returns still filed quarterly and the employee portion paid | same |
| Carer employed in the home of a person with a disability | Exempt on application to the Office of the Tax Commissioner for the Minister's approval | [Payroll tax](https://www.gov.bm/payroll-tax) |
| Approved training scheme for Bermudian employees | Not taxed once the National Training Board scheme is approved | same |
| Employee under 65 working 4 hours a week or less | No social insurance contribution | [Employees](https://socialinsurance.gov.bm/Contributions/Employees) |
| Person whose annual income does not exceed BMD 3,000, a widow or widower receiving a widow's or widower's benefit, a vacation or public-holiday student worker, or a non-resident who worked less than 26 consecutive weeks in Bermuda | Can be exempted on application to the Director of Social Insurance; not automatic | same |
| Full-time student under 26 working Saturdays, public holidays or vacations | Not an employed person; no contributions from either side | [Contribution calendar 2026-27](https://socialinsurance.gov.bm/Portals/0/calendars/Contribution-Calendar-2027.pdf) |
| Unpaid leave | No contribution; notify the Department in writing within 30 days after the leave | [Employers](https://socialinsurance.gov.bm/Contributions/Employers) |
| Independent contractor | Payroll tax still applies to foreign contractors and subcontractors in Bermuda; a self-employed person pays on drawings | [Payroll tax](https://www.gov.bm/payroll-tax) |
| Reimbursement of documented business expenses | Not remuneration | Office practice; confirm with the Office for unusual items |

### Defaults when a fact is missing

| Missing fact | Default | Why |
|---|---|---|
| Employer class unknown | Ask; do not compute the employer portion and do not fall back to the 9.75% standard rate | Rates run from 0% to 9.75% |
| Small employer, quarter not stated | Ask which quarter; Class B(f) is 0.5% to September 2026 and 1.0% from October 2026 | Act 2026:31 s.2 |
| Annual rate of pay unknown for a part-year employee | Annualise the pay-period rate | The Office applies bands to the annual rate of pay |
| Age unknown | Treat as under 65 for social insurance | Both halves are due under 65 |

## Worked cases

### Case 1: employee earning BMD 120,000, employer with payroll over BMD 1,000,000

The employer is not an exempt undertaking and has an annual payroll above BMD 1,000,000, so its rate is 9.50%. Employee portion: 48,000 at 0.25% (120), 48,000 at 7.75% (3,720), 24,000 at 10.75% (2,580), total 6,420. Employer portion 11,400. Social insurance for a full year under 65: 52 weeks at 39.25 each side, 2,041 employee and 2,041 employer.

```oa-check
name: Bermuda payroll tax, BMD 120,000 employee, large employer, 2026-27
inputs:
  pay: 120000
  employer_rate: 0.095
  weekly_half: 39.25
  weeks: 52
steps:
  - band1: min(pay, 48000) * 0.0025
  - band2: max(0, min(pay, 96000) - 48000) * 0.0775
  - band3: max(0, min(pay, 200000) - 96000) * 0.1075
  - employee_portion: band1 + band2 + band3
  - employer_portion: min(pay, 1000000) * employer_rate
  - si_employee: weekly_half * weeks
  - si_employer: weekly_half * weeks
expected:
  employee_portion: 6420
  employer_portion: 11400
  si_employee: 2041
  si_employer: 2041
```

### Case 2 (decision): owner of a small local company takes BMD 100,000 as salary or as dividend

The company's annual payroll is under BMD 200,000, so it is in Class B(f). For tax periods from October to December 2026 onward its employer rate is 1.0% (it was 0.5% for April to September 2026); this case uses 1.0% on a full year of pay in those later periods. The owner is an employee of the company and the company is neither an exempt undertaking nor listed. Paid as salary, all 100,000 is remuneration: employer 1,000, employee 4,270, total 5,270. Paid as a dividend, the first 20,000 is excluded (s.7(2)(i)) and 80,000 is remuneration: employer 800, employee 2,600, total 3,400. The dividend route saves 1,870 of payroll tax (derived). At the old 0.5% rate the saving would have been 1,770. The decision also turns on company law (distributable profits), social insurance (paid per week worked, not on dividends) and the owner's other tax position abroad; confirm those before choosing.

```oa-check
name: Salary or dividend, BMD 100,000, small local company, Class B(f) from October 2026
inputs:
  amount: 100000
  dividend_deductible: 20000
  employer_rate: 0.01
steps:
  - salary_employee: min(amount, 48000) * 0.0025 + max(0, min(amount, 96000) - 48000) * 0.0775 + max(0, min(amount, 200000) - 96000) * 0.1075
  - salary_total: amount * employer_rate + salary_employee
  - div_taxable: max(0, amount - dividend_deductible)
  - div_employee: min(div_taxable, 48000) * 0.0025 + max(0, min(div_taxable, 96000) - 48000) * 0.0775 + max(0, min(div_taxable, 200000) - 96000) * 0.1075
  - div_total: div_taxable * employer_rate + div_employee
  - saving: salary_total - div_total
expected:
  salary_total: 5270
  div_total: 3400
  saving: 1870
```

## When to refuse or refer

- Payroll tax concessions not on the published class list, or a dispute about class: refer to the Office of the Tax Commissioner.
- An employee's pay above BMD 1,000,000 with equity awards, or cross-border secondments with home-country social security: refer to a Bermuda practitioner.
- Occupational pension: defined benefit funding, late-payment interest (the Act caps it at 7% a year; the prescribed rate was not found), cap coordination across several employers and any temporary contribution relief for a period: refer to the Pension Commission.
- A request to work out income tax for a Bermuda resident: Bermuda has no income tax; foreign income tax belongs to that country's skill.

## Filing and payment

1. Register the employer or self-employed tax account with the Office of the Tax Commissioner ([Payroll tax](https://www.gov.bm/payroll-tax)).
2. File quarterly. Remuneration for January to March is declared between 1 April and 15 April; April to June by 15 July; July to September by 15 October; October to December by 15 January. Payment is due on the same dates ([2026-27 rates](https://www.gov.bm/calculating-payroll-tax-2026)).
3. All exempted companies, and employers above the BMD 200,000 annual remuneration line, must e-file at www.etax.gov.bm; penalties apply where tax is not submitted in the required format. The two official pages differ at exactly BMD 200,000: the payroll tax page (updated 3 November 2026) says "greater than" BMD 200,000, the 2026-27 calculation page says BMD 200,000 or more. At exactly 200,000, e-file and ask the Office to confirm ([Payroll tax](https://www.gov.bm/articles/payroll-tax)).
4. An employer that has deducted the employee portion and does not pay it within fifteen days beginning on the last day of the tax period commits a separate default (Payroll Tax Act s.19(5)); check that clock as well as the return date. Late filers are subject to late penalties and assessments. False returns, inadequate records under the Tax (Accounts and Records) Regulations 1991, or evasion are offences with fines up to BMD 500,000. The Commissioner may assess undeclared remuneration under section 16 of the Taxes Management Act.
5. Relief applications (new hire, Bermudian senior) go in by the end of the relevant quarter, on the 2026 templates on the Office's page.
6. Social insurance: register employees on entry into insurable employment (the employer page says within 30 days; the Act requires registration on entry and the employer's immediate number check); a self-employed person registers within 7 days; contributions are due by the last working day of the following month; pay the monthly bill (billed a month in arrears) by online banking (HSBC, Butterfield, Clarien) or at the Department ([Employers](https://socialinsurance.gov.bm/Contributions/Employers)).

## Completion checklist

- Employer class and rate confirmed against the 2026-27 list.
- Every employee's annual rate of pay banded separately; cap applied.
- Dividends to service providers of local companies reported in section C, with the BMD 20,000 deductible.
- Relief applications filed in time.
- Social insurance weeks counted (more than 4 hours for one employer), age 65 checked, paid by the last working day of the following month.
- Occupational pension membership (age 23, 720 hours per employer) checked; 5% plus 5% remitted within 30 days after the month.
- E-filing used where required; quarter-end plus 15 days met.

## Sources

| Source | URL | Read on |
|---|---|---|
| Office of the Tax Commissioner, payroll tax: read for the tax base, the cap, exemptions, the four due dates and the e-tax rule | https://www.gov.bm/payroll-tax | 2026-11-14 |
| Office of the Tax Commissioner, calculating payroll tax 1 April 2026 to 31 March 2027: read for every employer rate, the five employee bands, the cap, the dividend deductible, new hire and senior relief, filing dates and penalties | https://www.gov.bm/calculating-payroll-tax-2026 | 2026-11-14 |
| Department of Social Insurance, contribution calendar 2026-27 (PDF): read for the weekly rates with effect from 3 August 2026, the yearly rate and the notes for employees | https://socialinsurance.gov.bm/Portals/0/calendars/Contribution-Calendar-2027.pdf | 2026-11-14 |
| Department of Social Insurance, contribution calendar 2025-26 (PDF): read for the previous rate (BMD 75.30 a week from 4 August 2025) | https://socialinsurance.gov.bm/Portals/0/calendars/Contribution-Calendar-2026.pdf | 2026-11-14 |
| Department of Social Insurance, employers page: read for registration within 30 days, billing a month in arrears, the contribution week and unpaid leave | https://socialinsurance.gov.bm/Contributions/Employers | 2026-11-14 |
| Department of Social Insurance, employees page: read for the 4-hour rule and the cases that can be exempted on application | https://socialinsurance.gov.bm/Contributions/Employees | 2026-11-14 |
| Payroll Tax Rates Act 1995 (consolidated, bermudalaws.bm): read ss.3, 3A, 5 and 5A for the 9.75% standard rate, the employee bands and every employer class, including Class A (more than BMD 350,000), Class B (3.0%, no threshold for the Hospitals Board and Corporations), Class B(f) 1.0% and Class AA | https://www.bermudalaws.bm/Laws/Consolidated%20Law/1995/Payroll%20Tax%20Rates%20Act%201995 | 2026-11-14 |
| Payroll Tax Rates Amendment Act 2026 (2026:31): read s.2 for Class B(f) 0.5% to 1.0% from the October to December 2026 tax period | https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2026/Payroll%20Tax%20Rates%20Amendment%20Act%202026 | 2026-11-14 |
| Payroll Tax Act 1995 (consolidated): read s.2(3) to (5) for the exempt undertaking test, s.7(2)(h) and (i) for dividends, s.9AA for senior relief and s.19(5) for the deducted employee tax clock | https://www.bermudalaws.bm/Laws/Consolidated%20Law/1995/Payroll%20Tax%20Act%201995 | 2026-11-14 |
| Office of the Tax Commissioner, payroll tax article (updated 3 November 2026): read for the e-filing line "greater than BMD 200,000" | https://www.gov.bm/articles/payroll-tax | 2026-11-14 |
| Contributory Pensions Act 1970 (consolidated): read ss.1, 2(5) and (6), 4(7), 7 and 8 for school-leaving age, the 4-hour and 26-week rules, payment by the last working day of the following month, recovery and 7-day self-employed registration | https://www.bermudalaws.bm/Laws/Consolidated%20Law/1970/Contributory%20Pensions%20Act%201970 | 2026-11-14 |
| Contributory Pensions (Exception from Liability for Contributions) Regulations 1973: read regs 1 and 2 for the BMD 3,000 certificate and 13-week backdating | https://www.bermudalaws.bm/Laws/Consolidated%20Law/1973/Contributory%20Pensions%20(Exception%20from%20Liability%20for%20Contributions)%20Regulations%201973 | 2026-11-14 |
| National Pension Scheme (Occupational Pensions) Act 1998 (consolidated): read ss.2, 17, 19 and the First Schedule for membership, pensionable earnings, the 5% rate and 30-day remittance | https://www.bermudalaws.bm/Laws/Consolidated%20Law/1998/National%20Pension%20Scheme%20(Occupational%20Pensions)%20Act%201998 | 2026-11-14 |
| National Pension Scheme (General) Regulations 1999: read regs 21 and 22 for self-employed registration over BMD 20,000, twice the rate, 60 days and the BMD 10,000 cap | https://www.bermudalaws.bm/Laws/Consolidated%20Law/1999/National%20Pension%20Scheme%20(General)%20Regulations%201999 | 2026-11-14 |

Not yet confirmed: the payroll tax late filing penalty amounts (the Office says penalties and assessments apply but does not publish the figures on the page read); how the 1 August 2026 legal start of the new social insurance rates (BR 80/2026) applies to 1 and 2 August, before the calendar's 3 August first week; how a week that crosses a month end is allocated for the last-working-day payment rule; the prescribed late-interest rate on occupational pension contributions; whether any temporary occupational pension contribution relief applies to a 2026 period (only 2020 temporary legislation was found).
