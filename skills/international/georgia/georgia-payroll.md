---
name: georgia-payroll
description: "Payroll for employers in the country of Georgia (Sakartvelo, GE, currency GEL; not the US state) for tax year 2026. Covers who must withhold income tax from salary (Tax Code art. 154), the flat 20% rate, the employee's 2% funded pension contribution and why it comes off the income tax base, the employer's 2% contribution on top of pay, the state co-contribution (2% on the first GEL 24,000 a year, 1% up to GEL 60,000, nothing above), who must join the scheme and the age-40 opt-out, benefits in kind and the company car charge, salary paid by small businesses, non-resident employers, gross-to-net, the monthly return and payments by the 15th, and the fines (GEL 300 for a missed pension contribution, GEL 200 per unregistered employee, 0.05% a day interest). Trigger on: Georgia payroll, gross to net Georgia, salary tax Georgia, khelpasi, pension contribution Georgia employer, rs.ge monthly declaration. Out of scope: the annual return and other income (georgia-income-tax), self-employed pension contributions (georgia-social-contributions), VAT (georgia-vat)."
version: 0.2
jurisdiction: GE
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Georgia (country): payroll for employers (2026) v0.2

An employer in Georgia withholds 20% income tax from each salary payment and pays it to the budget when the salary is paid. For staff in the funded pension scheme it also withholds the employee's 2% contribution and adds its own 2%. The state adds up to 2% on top. Both are reported on the monthly return to the Revenue Service by the 15th of the next month. Figures below are from the Tax Code of Georgia, consolidated on matsne.gov.ge to the law of 15 October 2026 (publication 247), and the Law of Georgia on Funded Pension (No 3303, 21 July 2018), Georgian consolidated text to the law of 16 September 2026.

## Who this applies to

- **Tax agents.** A legal person, an enterprise or organisation, or an entrepreneur natural person that pays salary to an employee must withhold the tax at source (Tax Code art. 154(1)(a)). The same duty covers payments for services to an individual who is not registered as an individual entrepreneur, unless he or she is VAT-registered, a notary, an enforcement officer, or holds micro, small or fixed tax status (art. 154(1)(d)).
- **Exceptions.** No withholding by a Free Industrial Zone enterprise on salary to a Georgian resident employee (art. 154(1)(a.a)), or by a non-resident whose salary cost is not borne by a Georgian permanent establishment (art. 154(1)(a.b)). In the second case the employee may compute, report and pay the tax himself, and the employer is then released (art. 154(5)).
- **Salary** is any pay or benefit from employment, including pension from a former employment and pay for future employment (art. 101(1)).
- **Funded pension.** Joining the scheme and paying contributions is mandatory for every employee on salary, except an employee who was 60 (men) or 55 (women) before the Law came into force; for them, and for the self-employed, it is voluntary (Law on Funded Pension art. 3(2)-(3)). The Law applies to Georgian citizens and to foreign citizens and stateless persons holding a permanent residence permit in Georgia (art. 1(4)). An employer for the scheme is a person other than a non-resident who pays for an employee's work or services (art. 2 e)).
- Not here: the annual return and income other than salary (see [georgia-income-tax](georgia-income-tax.md)); contributions of the self-employed and how the pension is paid out (see [georgia-social-contributions](georgia-social-contributions.md)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Income tax on salary | 20% | 2026 | Tax Code art. 81(1), 154(1)(a), https://matsne.gov.ge/en/document/view/1043717?publication=247 |
| Non-resident's salary from a Georgian source | 20% at source | 2026 | art. 134(1)(f), same URL |
| Employee funded pension contribution, withheld | 2% of taxable salary | 2026 | Law on Funded Pension art. 3(6)(b), https://matsne.gov.ge/ka/document/view/4280127?publication=13 |
| Employer funded pension contribution, at its own cost | 2% of taxable salary | 2026 | art. 3(6)(a), same URL |
| State contribution, first GEL 24,000 of annual salary | 2% | 2026 | art. 3(6)(e.a), same URL |
| State contribution, GEL 24,000 to GEL 60,000 | 1% | 2026 | art. 3(6)(e.b), same URL |
| State contribution above GEL 60,000 | none | 2026 | art. 3(6)(f), same URL |
| Employer and state pension contributions | not salary of the employee | 2026 | Tax Code art. 101(3)(d) |
| Employee's pension contribution to the individual account | exempt from income tax | 2026 | Tax Code art. 82(1)(b3) |
| Personal use of the employer's car: tax a year by engine size | over 3,500 cm3: GEL 300; 2,500-3,500 cm3: GEL 200; under 2,500 cm3: GEL 100; hybrid: GEL 60; electric: none | 2026 | Tax Code art. 101(2^1), (2^3) |
| Salary paid by a small business, not taxed at source | up to GEL 6,000 in a year in total, if the business got the status this year or had gross income up to GEL 50,000 last year | 2026 | Tax Code art. 94(4) |
| Salary paid in farming, not taxed | if the employer's gross income from farming is up to GEL 200,000, until 1 January 2028 | 2026 | Tax Code art. 82(1)(z1) |
| Missed pension contribution | GEL 300 fine per breach | 2026 | Law on Funded Pension art. 37^3(1) |
| Employee not entered in the Register of Hired Employees | GEL 200 per employee | 2026 | Tax Code art. 288^5 |
| Penalty interest on late tax | 0.05% a day | 2026 | Tax Code art. 272(4) |

## The taxable base

**Order of the calculation for an employee in the scheme.**
1. Gross salary for the month, including benefits valued under art. 101(2) (for example the market price of goods or services given, reimbursed personal expenses, the employer's life or health insurance premiums, a cheap loan).
2. Employee pension contribution: 2% of the taxable salary, withheld by the employer on the employee's behalf (Law on Funded Pension art. 3(6)(b)).
3. Income tax: 20% of gross salary less the employee's pension contribution. The contribution made to the individual pension account is exempt from income tax (Tax Code art. 82(1)(b3)). The Law confirms this from the other side: if an employee leaves the scheme under art. 22, the contributions made on his behalf are taxed when they are returned to him (Law on Funded Pension art. 22(3)(a); Tax Code art. 82(1)(b3.b)).
4. Net pay = gross - employee contribution - income tax, which is 78.4% of gross.
5. Employer contribution: 2% of the taxable salary at the employer's own cost (art. 3(6)(a)). It is not salary of the employee (Tax Code art. 101(3)(d)).
6. State contribution: paid by the state into the account, 2% on the first GEL 24,000 of the year's salary, 1% from there to GEL 60,000, none above (art. 3(6)(e)-(f)). It costs the employer nothing.

The Law sets no ceiling on the employee's or employer's 2% (art. 3(6)(a)-(b)). Only the state contribution stops at GEL 60,000.

**Employee outside the scheme.** For an employee who was 60 (men) or 55 (women) before the Law came into force and has not joined voluntarily (Law on Funded Pension art. 3(2)-(3)), or who left under the age-40 opt-out (art. 22), drop steps 2, 5 and 6: income tax is 20% of gross and net pay is 80% of gross. The employer pays no pension contribution.

**Net to gross.** Where only a net figure is agreed, gross = net / 0.784 for an employee in the scheme and net / 0.80 for one outside it. Both follow from the order above.

**No other payroll tax.** The national taxes are income tax, profit tax, VAT, excise and import duty, and the only local tax is property tax (Tax Code art. 6(5)-(6)). None is charged on the payroll, so the employer's statutory cost on top of gross pay is the 2% pension contribution alone. The company car tax in art. 101(2^1) is income tax on the employee's benefit, which the employer pays as tax agent (art. 101(2^2)).

**Not salary.** Business travel reimbursed within Ministry of Finance limits, reimbursed entertainment expenses, employer transport to work where public transport cannot reasonably be used, employer and state pension contributions, compulsory insurance premiums paid by the employer, and accommodation or food that the job requires and that is not part of the agreed pay (art. 101(3)).

**Company car.** An employee's personal use of the employer's car is taxed as a fixed amount of tax a year by engine size (table above). The reporting period is the calendar year and the employer pays it by the 15th of the month after the reporting month (art. 101(2^1)-(2^2)). Personal use of an electric car is not taxed (art. 101(2^3)).

**Opt-out at 40.** An employee who was 40 or older when the Law came into force may leave the scheme by writing to the Pension Fund within 5 months of automatic enrolment, but not earlier than 3 months after it (art. 22(1)). The employer may not persuade or dissuade the employee (art. 22(2)). An employee who left may rejoin at any time (art. 22(4)).

**Breaks in pay.** A participant whose salary stops for a time also stops contributions, and restarts when salary restarts (art. 23(1)).

**Groups with a personal exemption.** The first GEL 3,000 or GEL 6,000 of taxable income a year is not taxed for the groups in Tax Code art. 82(2) (for example single parents, persons with a disability from childhood). See [georgia-income-tax](georgia-income-tax.md). Where the employer gets this wrong because of a wrong monthly return, art. 288^4 fines it double the amount wrongly refunded.

## Deadlines and filing

| What | Deadline | Source |
|---|---|---|
| Pay withheld income tax to the budget | when the salary is paid; for non-cash benefits, on the last day of the month | Tax Code art. 154(3)(a) |
| Monthly return of salaries paid and tax withheld | by the 15th of the month after the month | art. 153(5), 154(3)(c.a), 154(4) |
| Employer and employee pension contributions | no later than the day the income tax return is filed, on the basis of that return | Law on Funded Pension art. 3(6)(a)-(b) |
| Tax on personal use of a company car (calendar-year period) | by the 15th of the month after the reporting month | Tax Code art. 101(2^2) |
| Salary statement to an employee | on the employee's request | art. 154(3)(b) |
| Opt-out request (employees 40+ at the Law's start) | between 3 and 5 months after enrolment | Law on Funded Pension art. 22(1) |

An employee whose only income is salary taxed at source does not file an annual return (Tax Code art. 153(1)(a)).

## Penalties and interest

| Breach | Penalty | Source |
|---|---|---|
| Tax not withheld | the payer pays the tax itself, with penalties | Tax Code art. 154(2)(b) |
| Late monthly return, up to 2 months | 5% of the tax on the return for each month or part month, at most 30% | art. 274(1) |
| Late monthly return, more than 2 months | 10% of the tax on the return | art. 274(2) |
| Understated tax | 10%, 25% or 50% of the understated tax, by size | art. 275 |
| Late payment | 0.05% of the unpaid tax a day | art. 272(4) |
| Wrong monthly return leading to an excess refund of a non-taxable minimum | double the excess | art. 288^4 |
| Employee not registered in the Register of Hired Employees | GEL 200 per employee | art. 288^5 |
| Pension contribution not made, or late | GEL 300 fine, cancelled if the contribution and lost benefit are paid in full within 10 working days | Law on Funded Pension art. 37^3(1)-(2) |
| Lost benefit of the participant | charged on top of any fine until the contribution is paid; the employer pays the missed contribution at its own cost | art. 37^2(5), 37^4 |
| Not a breach | a corrected return after which the contribution is paid on time; total contributions for a month of GEL 1 or less | art. 37^3(3) |

## Cross-border points

- **Non-resident employees** are taxed at 20% on Georgian-source salary (Tax Code art. 134(1)(f)).
- **Foreign employees without a permanent residence permit** are outside the funded pension scheme; the Law applies to Georgian citizens and to foreigners and stateless persons with a permanent residence permit (Law on Funded Pension art. 1(4)).
- **Non-resident employers** with no Georgian permanent establishment bearing the cost do not withhold; the employee may self-report (Tax Code art. 154(1)(a.b), 154(5)). Such an employer is not an "employer" for the pension scheme (Law on Funded Pension art. 2 e)), and an employee whose employer need not withhold counts as self-employed for the scheme (art. 2 i)).
- **Leaving Georgia for good.** A participant who loses Georgian citizenship or the permanent residence permit may take the account as a lump sum, which is taxed (art. 34^1).

## Worked examples

**Example 1. Employee in the scheme on GEL 3,000 a month.** A Georgian company pays a resident employee GEL 3,000 gross every month of 2026, GEL 36,000 for the year. Each month it withholds the 2% contribution, GEL 60, and income tax of 20% x (3,000 - 60) = GEL 588. Net pay is GEL 2,352 a month. The company adds its own GEL 60, so the employee costs GEL 3,060 a month. For the year: contributions GEL 720 each, income tax GEL 7,056, net pay GEL 28,224, cost GEL 36,720. The state adds 2% of GEL 24,000 plus 1% of GEL 12,000, GEL 600. Tax is paid on each pay day; the return and the contributions go in by the 15th of the next month.

```oa-check
name: Georgia payroll, GEL 3,000 a month, funded pension, 2026
inputs:
  monthly_gross: 3000
  months: 12
  pension_rate: 0.02
  pit_rate: 0.20
  state_band_1: 24000
  state_band_2: 60000
steps:
  - employee_pension_month: monthly_gross * pension_rate
  - pit_month: (monthly_gross - employee_pension_month) * pit_rate
  - net_month: monthly_gross - employee_pension_month - pit_month
  - employer_cost_month: monthly_gross + monthly_gross * pension_rate
  - annual_gross: monthly_gross * months
  - pit_year: pit_month * months
  - net_year: net_month * months
  - employer_cost_year: employer_cost_month * months
  - state_contribution: min(annual_gross, state_band_1) * 0.02 + max(min(annual_gross, state_band_2) - state_band_1, 0) * 0.01
expected:
  employee_pension_month: 60
  pit_month: 588
  net_month: 2352
  employer_cost_month: 3060
  annual_gross: 36000
  pit_year: 7056
  net_year: 28224
  employer_cost_year: 36720
  state_contribution: 600
```

**Example 2. High earner with a company car.** A manager earns GEL 8,000 a month, GEL 96,000 in 2026, and is in the scheme. He also uses the company's 2,800 cm3 car privately. The 2% contributions have no ceiling: GEL 1,920 each from him and the employer. Income tax is 20% x (96,000 - 1,920) = GEL 18,816, and net pay is GEL 75,264. The state contribution stops at GEL 60,000: 2% of 24,000 plus 1% of 36,000, GEL 840. For the car, the employer pays a fixed GEL 200 of tax for the year (art. 101(2^1)). The employer's cost before the car charge is GEL 97,920.

```oa-check
name: Georgia payroll, GEL 96,000 a year, state cap and company car, 2026
inputs:
  annual_gross: 96000
  pension_rate: 0.02
  pit_rate: 0.20
  state_band_1: 24000
  state_band_2: 60000
  car_tax_2500_3500cc: 200
steps:
  - employee_pension: annual_gross * pension_rate
  - employer_pension: annual_gross * pension_rate
  - pit: (annual_gross - employee_pension) * pit_rate
  - net: annual_gross - employee_pension - pit
  - state_contribution: min(annual_gross, state_band_1) * 0.02 + max(min(annual_gross, state_band_2) - state_band_1, 0) * 0.01
  - employer_cost: annual_gross + employer_pension
  - car_tax: car_tax_2500_3500cc
expected:
  employee_pension: 1920
  employer_pension: 1920
  pit: 18816
  net: 75264
  state_contribution: 840
  employer_cost: 97920
  car_tax: 200
```

## Ask the client first

1. Is this the country of Georgia (GEL), not the US state?
2. On what date is salary paid each month? Income tax is due on the pay day (Tax Code art. 154(3)(a)).
3. For each person: employee or a contractor for services? Is the contractor a registered individual entrepreneur, VAT-registered, or on micro, small or fixed tax status?
4. Monthly gross pay (or only the agreed net), and any benefits: car, accommodation, insurance, loans, reimbursed expenses?
5. Is each employee a Georgian citizen or a holder of a permanent residence permit? Date of birth (60/55 and 40+ rules), and has anyone opted out?
6. Is the employer a small business, a farm, a Free Industrial Zone enterprise, or a non-resident without a permanent establishment?
7. Has every employee been entered in the Register of Hired Employees?

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Code of Georgia, English, consolidated publication 247 (to the law of 15 October 2026): arts. 6, 81, 82, 94, 101, 134, 153, 154, 272, 274, 275, 288^4, 288^5 | https://matsne.gov.ge/en/document/view/1043717?publication=247 | 2026-10-31 |
| Tax Code of Georgia, Georgian text, publication 247 (cross-check of arts. 81, 82, 94, 153, 272, 274) | https://matsne.gov.ge/ka/document/view/1043717?publication=247 | 2026-10-31 |
| Law of Georgia on Funded Pension No 3303, Georgian, consolidated to the law of 16 September 2026: arts. 1, 2, 3, 21, 22, 23, 34^1, 37^2-37^4, 39 | https://matsne.gov.ge/ka/document/view/4280127?publication=13 | 2026-10-31 |
| Law of Georgia on Funded Pension, English, consolidated to 26 June 2025 (translation of the same articles) | https://matsne.gov.ge/en/document/view/4280127?publication=12 | 2026-10-31 |

Not yet confirmed: no Pension Fund or Revenue Service guidance was read to confirm the gross-to-net order (it rests on Tax Code art. 82(1)(b3) and Law art. 22(3)(a)); the exact date for the 60/55 and 40+ age tests (the Law came into force on publication in August 2018, its art. 21 on 1 January 2019; art. 39); whether the 2% contributions are rounded per payment; the statutory minimum wage (the old version cited GEL 20 a month from a 1999 decree; not read); who bears the company car charge economically; the name and layout of the rs.ge monthly return; Ministry of Finance limits for travel allowances; posted workers and social security agreements.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
