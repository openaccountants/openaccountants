---
name: bm-payroll-social
description: >
  Bermuda payroll tax and social insurance for employers, employees and the self-employed
  for the payroll tax year 1 April 2026 to 31 March 2027 and the contribution year from
  3 August 2026. Covers the employer portion by class of taxpayer, the five employee
  portion bands, the BMD 1,000,000 cap, the dividend deductible, new hire and senior relief,
  quarterly e-tax filing, contributory pension contributions and occupational pension
  pointers. Trigger phrases include Bermuda payroll tax, employee portion, employer
  portion, etax.gov.bm, social insurance Bermuda, contributory pension, BMD 78.50 a week.
version: "1.0"
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

# Bermuda payroll tax and social insurance v1.0

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
| Employer rate, annual payroll under BMD 200,000 (under BMD 50,000 a quarter) | 0.5% | same |
| Employer rate, educational, sporting or scientific institutions | 1.00% | same |
| Employer rate, self-employed horticulturist | 1.75% | same |
| Employer rate, annual remuneration BMD 200,000 to 350,000 (under BMD 87,500 a quarter); Bermuda Hospitals Board and the Corporations of Hamilton and St. George's | 2.00% | same |
| Employer rate, Bermuda Hospitals Board, the two Corporations and licensed residential care homes with payroll over BMD 350,000 | 3.00% | same |
| Employer rate, restaurant or hotel with annual payroll BMD 350,000 or more | 4.00% | same |
| Employer rate, annual remuneration over BMD 350,000 to 500,000 | 4.75% | same |
| Employer rate, retail establishment over BMD 500,000 whose primary business is fashion, shoes, jewellery and perfume | 5.00% | same |
| Employer rate, annual payroll over BMD 500,000 up to 1,000,000 | 7.00% | same |
| Employer rate, annual payroll over BMD 1,000,000 (over BMD 250,000 a quarter) | 9.50% | same |
| Employer rate, all exempt undertakings | 9.75% | same |
| Employee portion band 1, annual remuneration 0 to 48,000 | 0.25% | same |
| Employee portion band 2, above the first 48,000 up to 96,000 | 7.75% | same |
| Employee portion band 3, 96,001 to 200,000 | 10.75% | same |
| Employee portion band 4, 200,001 to 500,000 | 11.50% | same |
| Employee portion band 5, 500,001 to 1,000,000 | 12.50% | same |
| Tax cap, remuneration per person per year | BMD 1,000,000; remuneration above it is not taxed | same |
| Dividend deductible, dividends to persons providing services to local companies not trading on a stock exchange, from 1 April 2026 | BMD 20,000 per person per year; each dividend dollar above it is gross remuneration, up to the cap | same |
| Bermudian aged 65 or over relief | Remuneration up to BMD 24k per tax period (quarter) not taxable; bonuses taxable; relief from the quarter the application is received | same |
| Social insurance, employed person over school-leaving age and under 65 | BMD 39.25 employee plus BMD 39.25 employer, BMD 78.50 a week, from 3 August 2026 | [Contribution calendar 2026-27](https://socialinsurance.gov.bm/Portals/0/calendars/Contribution-Calendar-2027.pdf) |
| Social insurance, employed person over 65 | BMD 39.25 a week, employer only | same |
| Social insurance, self-employed under 65 | BMD 78.50 a week | same |
| Social insurance, self-employed over 65 | BMD 39.25 a week | same |
| Social insurance, voluntary contributor under 65 | BMD 78.50 a week | same |
| Social insurance, yearly rate at the full weekly rate | BMD 4,082.00 | same |

### Steps

1. **Classify the employer.** Use annual remuneration for the year (or the quarterly equivalents shown above) and the class list. The class sets one employer rate on gross taxable remuneration; it is not a banded rate. An exempt undertaking pays 9.75% whatever its payroll size, unless a 0% class or relief applies to specific remuneration ([2026-27 rates](https://www.gov.bm/calculating-payroll-tax-2026)).
2. **Build taxable remuneration.** Wages, salaries and benefits in cash or kind for services provided in Bermuda. For a self-employed person or deemed employee it is the amount taken out of the business for personal use. Add dividends above BMD 20,000 per person per year paid to service providers of a local unlisted company and report them in section C of the return each time dividends are paid or declared. Exclude employer contributions to approved pension, life insurance and health insurance schemes, weekend or vacation work by students and certain lay-off allowances. A person under 16, or employed 16 hours or less in each month of a tax period, is not an employee (the 16-hour rule does not apply to the self-employed) ([Payroll tax](https://www.gov.bm/payroll-tax)).
3. **Apply the cap.** Stop at BMD 1,000,000 per person per year.
4. **Employer portion.** Taxable remuneration times the employer rate. New hire and special-situation remuneration is at 0% for the employer portion only.
5. **Employee portion.** Apply the five marginal bands to each person's annual rate of pay. For pay that fluctuates, recompute the annual rate each pay period (the Office publishes weekly, bi-weekly, semi-monthly and monthly calculators).
6. **Social insurance.** One weekly contribution per person for each week (Monday to Sunday) worked more than 4 hours. Employers deduct half from pay and remit both halves; employers are billed a month in arrears ([Employers](https://socialinsurance.gov.bm/Contributions/Employers)).
7. **File and pay** (see Filing and payment).

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Exempted company employing staff in Bermuda | Payroll tax applies; employer rate 9.75% as an exempt undertaking; exempted status under the Companies Act is not a payroll tax exemption | [2026-27 rates](https://www.gov.bm/calculating-payroll-tax-2026) |
| New Hire Relief 2026 | For exempted companies and other employers with remuneration over BMD 500,000 that increase full-time equivalents (15 hours or more a week) above the January to March 2025 baseline. Qualifying employees: hired 1 April 2025 to 31 March 2026 and still employed after 1 April 2026, or hired 1 April 2026 to 31 March 2028, not previously employed by a parent or affiliate. Employer portion exemption only. Apply by the end of the quarter in which the employee qualifies; no retroactive approval | same |
| Self-employed caregiver | 0% employer portion; returns still filed quarterly and the employee portion paid | same |
| Carer employed in the home of a person with a disability | Exempt on application to the Office of the Tax Commissioner for the Minister's approval | [Payroll tax](https://www.gov.bm/payroll-tax) |
| Approved training scheme for Bermudian employees | Not taxed once the National Training Board scheme is approved | same |
| Employee under 65 working 4 hours a week or less | No social insurance contribution | [Employees](https://socialinsurance.gov.bm/Contributions/Employees) |
| Person earning less than BMD 3,000 a year, a widow or widower receiving a widow's or widower's benefit, a vacation or public-holiday student worker, or a non-resident who worked less than 26 consecutive weeks in Bermuda | Can be exempted on application to the Director of Social Insurance; not automatic | same |
| Full-time student under 26 working Saturdays, public holidays or vacations | Not an employed person; no contributions from either side | [Contribution calendar 2026-27](https://socialinsurance.gov.bm/Portals/0/calendars/Contribution-Calendar-2027.pdf) |
| Unpaid leave | No contribution; notify the Department in writing within 30 days after the leave | [Employers](https://socialinsurance.gov.bm/Contributions/Employers) |
| Independent contractor | Payroll tax still applies to foreign contractors and subcontractors in Bermuda; a self-employed person pays on drawings | [Payroll tax](https://www.gov.bm/payroll-tax) |
| Reimbursement of documented business expenses | Not remuneration | Office practice; confirm with the Office for unusual items |

### Defaults when a fact is missing

| Missing fact | Default | Why |
|---|---|---|
| Employer class unknown | Ask; do not compute the employer portion | Rates run from 0% to 9.75% |
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

The company's annual payroll is under BMD 200,000, so its employer rate is 0.5%. Paid as salary, all 100,000 is remuneration: employer 500, employee 4,270, total 4,770. Paid as a dividend to the person providing services, the first 20,000 is deductible and 80,000 is remuneration: employer 400, employee 2,600, total 3,000. The dividend route saves 1,770 of payroll tax. The decision also turns on company law (distributable profits), social insurance (paid per week worked, not on dividends) and the owner's other tax position abroad; confirm those before choosing.

```oa-check
name: Salary or dividend, BMD 100,000, small local company, 2026-27
inputs:
  amount: 100000
  dividend_deductible: 20000
  employer_rate: 0.005
steps:
  - salary_employee: min(amount, 48000) * 0.0025 + max(0, min(amount, 96000) - 48000) * 0.0775 + max(0, min(amount, 200000) - 96000) * 0.1075
  - salary_total: amount * employer_rate + salary_employee
  - div_taxable: max(0, amount - dividend_deductible)
  - div_employee: min(div_taxable, 48000) * 0.0025 + max(0, min(div_taxable, 96000) - 48000) * 0.0775 + max(0, min(div_taxable, 200000) - 96000) * 0.1075
  - div_total: div_taxable * employer_rate + div_employee
  - saving: salary_total - div_total
expected:
  salary_total: 4770
  div_total: 3000
  saving: 1770
```

## When to refuse or refer

- Payroll tax concessions not on the published class list, or a dispute about class: refer to the Office of the Tax Commissioner.
- An employee's pay above BMD 1,000,000 with equity awards, or cross-border secondments with home-country social security: refer to a Bermuda practitioner.
- Occupational pension (National Pension Scheme) contribution rates and current relief from them: not confirmed in this skill; refer to the Pension Commission.
- A request to work out income tax for a Bermuda resident: Bermuda has no income tax; foreign income tax belongs to that country's skill.

## Filing and payment

1. Register the employer or self-employed tax account with the Office of the Tax Commissioner ([Payroll tax](https://www.gov.bm/payroll-tax)).
2. File quarterly. Remuneration for January to March is declared between 1 April and 15 April; April to June by 15 July; July to September by 15 October; October to December by 15 January. Payment is due on the same dates ([2026-27 rates](https://www.gov.bm/calculating-payroll-tax-2026)).
3. All exempted companies, and all employers with annual remuneration of BMD 200,000 or more, must e-file at www.etax.gov.bm; penalties apply where tax is not submitted in the required format.
4. Late filers are subject to late penalties and assessments. False returns, inadequate records under the Tax (Accounts and Records) Regulations 1991, or evasion are offences with fines up to BMD 500,000. The Commissioner may assess undeclared remuneration under section 16 of the Taxes Management Act.
5. Relief applications (new hire, Bermudian senior) go in by the end of the relevant quarter, on the 2026 templates on the Office's page.
6. Social insurance: register new employees who work 4 hours or more a week within 30 days; pay the monthly bill (billed a month in arrears) by online banking (HSBC, Butterfield, Clarien) or at the Department ([Employers](https://socialinsurance.gov.bm/Contributions/Employers)).

## Completion checklist

- Employer class and rate confirmed against the 2026-27 list.
- Every employee's annual rate of pay banded separately; cap applied.
- Dividends to service providers of local companies reported in section C, with the BMD 20,000 deductible.
- Relief applications filed in time.
- Social insurance weeks counted (more than 4 hours a week), age 65 checked.
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

Not yet confirmed: occupational pension contribution rates under the National Pension Scheme (Occupational Pensions) Act 1998 (the old file said 5% plus 5%; no official page opened); the late filing penalty amounts for payroll tax (the Office says penalties and assessments apply but does not publish the figures on the page read).
