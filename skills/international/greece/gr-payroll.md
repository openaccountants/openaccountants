---
name: gr-payroll
description: "Running Greek payroll for 2026 (calendar year): what an employer does each month and each year. Covers hiring in ERGANI II, the APD return and payment to e-EFKA, monthly gross-to-net (employee e-EFKA contributions of 13.37% under KPK 101, then income tax withholding on annualised pay using the 2026 scale of 9% to 44%, the youth and child rates and the art. 16 tax reduction), the Christmas and Easter bonuses, the 2026 minimum wage (EUR 880, then EUR 920 from 1 April 2026), overtime, night and Sunday premiums, the 20% withholding on extra pay, the monthly withholding return (ΦΜΥ) and its deadline, the digital work card and the fines. Trigger phrases: Greek payroll, μισθοδοσία, ΦΜΥ, παρακράτηση φόρου μισθωτών, gross to net Greece, δώρο Χριστουγέννων, κατώτατος μισθός 2026, ΕΡΓΑΝΗ, ψηφιακή κάρτα. Out of scope: contribution rates by branch (gr-employee-contributions), the employee's annual return (gr-income-tax), self-employed EFKA (gr-efka), postings and 5C (gr-cross-border)."
jurisdiction: GR
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Greece: running payroll, 2026

Source-cited draft. Built by Michael Cutajar and the OpenAccountants team.

This skill is the employer's monthly and yearly payroll routine in Greece for pay periods in 2026. It links to the pack's other skills instead of repeating them:

- Contribution rates by branch, the KPK codes, the EUR 7,761.94 ceiling and the APD rules in detail: `gr-employee-contributions`
- The employee's own annual income tax return (E1), the scale, the art. 16 reduction and card spending: `gr-income-tax`
- Self-employed EFKA contributions (for an IKE manager or a freelancer, not an employee): `gr-efka`
- Postings, A1 certificates, non-resident employees and the 5C inbound relief: `gr-cross-border`

The tax law is the Income Tax Code (Κώδικας Φορολογίας Εισοδήματος, ΚΦΕ, ν. 4172/2013), read in the Ministry of Finance codification up to ν. 5264/2025. Fines and interest are in the Tax Procedure Code (ΚΦΔ, ν. 5104/2024), read in AADE codification Ε.2109/2025. Labour rules come from the Ministry of Labour (ypergasias.gov.gr). Withholding tax goes to AADE; social contributions go to e-EFKA.

## Who this applies to

Every employer that pays salaries or wages in Greece: companies, sole traders with staff, and non-resident businesses with a Greek permanent establishment. A person or entity that pays employment income must withhold the tax and pay it to the State. If it does not withhold, it owes the tax that should have been withheld plus fines (art. 59(1)(α) and (2) ΚΦΕ).

Employment income for withholding includes monthly salary, daily wages, benefits in kind and lump-sum payments (art. 60(1)). Exempt income is not subject to withholding (art. 59(3)).

Out of this skill:

- Seafarers, aircraft crew and doctors' on-call pay, which have flat rates under art. 15(2) and art. 60(2).
- Public servants on public-law terms.
- The employee's year-end position. The employer's withholding is a prepayment; the employee's E1 return settles the year (see `gr-income-tax`).

## Rates, bands and thresholds

"Codification" is the Ministry of Finance codification of ν. 4172/2013 up to ν. 5264/2025, linked in Sources.

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Employee e-EFKA contributions, ordinary private-sector employee (KPK 101) | 13.37% of pay | 2026 | [e-EFKA circular 38/2024, KPK table](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-38-24122024) |
| Employer e-EFKA contributions, KPK 101 | 21.79% of pay | 2026 | same |
| Monthly ceiling on pay subject to contributions | EUR 7,761.94 | from 1.1.2026 | [e-EFKA circular 4/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-42026) |
| Tax scale on employment income: EUR 0 to 10,000 | 9% | 2026 | ΚΦΕ art. 15(1)(a), as replaced by ν. 5246/2025; Codification |
| EUR 10,000.01 to 20,000 | 20% | 2026 | same |
| EUR 20,000.01 to 30,000 | 26% | 2026 | same |
| EUR 30,000.01 to 40,000 | 34% | 2026 | same |
| EUR 40,000.01 to 60,000 | 39% | 2026 | same |
| Over EUR 60,000 | 44% | 2026 | same |
| 2nd band with 1, 2 or 3 dependent children | 18%, 16%, 9% | 2026 | ΚΦΕ art. 15(1)(b); Codification |
| 3rd band with 1, 2, 3 or 4 dependent children | 24%, 22%, 20%, 18%; 2 points lower for each child over 4 | 2026 | ΚΦΕ art. 15(1)(δ); Codification |
| First two bands with 4 or more dependent children | 0% | 2026 | ΚΦΕ art. 15(1)(γ); Codification |
| First two bands (income up to EUR 20,000), young employees | 0% up to age 25; 9% aged 26 to 30 | 2026 | ΚΦΕ art. 15(1)(ε); Codification |
| Tax reduction for 0, 1, 2, 3, 4, 5 dependent children | EUR 777, 900, 1,120, 1,340, 1,580, 1,780; EUR 220 more for each further child | 2026 | ΚΦΕ art. 16(1); Codification |
| Phase-out of the reduction | EUR 20 less per EUR 1,000 of taxable salary over EUR 12,000; not applied with 5 or more children | 2026 | ΚΦΕ art. 16(2); Codification |
| Withholding on back pay and on extra pay not part of regular pay | 20% of the amount paid | 2026 | ΚΦΕ art. 60(4); Codification |
| Withholding on net pay of daily-wage workers on fixed-term work of less than a year | 5% | 2026 | ΚΦΕ art. 60(4); Codification |
| Severance pay (taxed separately, final): up to EUR 60,000 | 0% | 2026 | ΚΦΕ art. 15(3); Codification |
| Severance: EUR 60,000.01 to 100,000 / 100,000.01 to 150,000 / over 150,000 | 10% / 20% / 30% | 2026 | same |
| Minimum monthly salary, white-collar, 1 January to 31 March 2026 | EUR 880.00 (decision 8233/27.3.2025) | 2026 | [Ministry of Labour, minimum wage](https://ypergasias.gov.gr/en/labour-relations/collective-employment-relations/minimum-wage/) |
| Minimum monthly salary, white-collar, from 1 April 2026 | EUR 920.00 (decision 8934/27.3.2026, Β' 1759) | 2026 | same |
| Minimum daily wage, blue-collar: to 31 March 2026 / from 1 April 2026 | EUR 39.30 / EUR 41.09 | 2026 | same |
| Seniority increments on the statutory minimum | White-collar 10% per 3 years, up to 30%; blue-collar 5% per 3 years, up to 30% | 2026 | same |
| Christmas bonus | One monthly salary, or 25 daily wages, for a full 1 May to 31 December | 2026 | [Ministry of Labour, holiday bonuses](https://ypergasias.gov.gr/ergasiakes-scheseis/syllogikes-ergasiakes-sxeseis/epidomata-eorton/) (ΚΥΑ 19040/1981) |
| Easter bonus | Half a monthly salary, or 15 daily wages, for a full 1 January to 30 April | 2026 | same |
| Extra work (υπερεργασία), hours 41 to 45 of a 5-day week | Hourly pay plus 20% | 2026 | [Ministry of Labour, working time](https://ypergasias.gov.gr/en/labour-relations/individual-employment-relations/working-time-limits/) |
| Legal overtime, up to 4 hours a day and 150 hours a year | Hourly pay plus 40% | 2026 | same (ν. 4808/2021 art. 58, ν. 5239/2025 art. 7) |
| Overtime above those limits, with Ministry approval | Hourly pay plus 60% | 2026 | same |
| Illegal overtime | Hourly pay plus 120% | 2026 | same |
| Sunday and public holiday work | 75% of 1/25 of monthly salary, or of the daily wage, per day | 2026 | same |
| Night work (10 pm to 6 am) | 25% on top of legal pay | 2026 | [Ministry of Labour, working time (Greek)](https://ypergasias.gov.gr/ergasiakes-scheseis/atomikes-ergasiakes-sxeseis/chronika-oria-ergasias/) |
| Annual paid leave, first full year | 20 working days (5-day week) or 24 (6-day week) | 2026 | [Ministry of Labour, leave](https://ypergasias.gov.gr/ergasiakes-scheseis/atomikes-ergasiakes-sxeseis/adeies-ergazomenon/) |

## The taxable base

**Step 1: gross pay.** Salary or daily wages for the month, plus premiums, plus benefits in kind. Pay may not be below the statutory minimum for full-time work, or the pro rata amount for part-time work (Ministry of Labour, citing art. 141A(1)(b) of Π.Δ. 62/2025). The minimum changed on 1 April 2026, so March and April payslips differ for minimum-wage staff.

**Step 2: employee contributions.** Apply the employee rate for the person's KPK (13.37% for KPK 101) to pay up to EUR 7,761.94 a month. The premium part of night, overtime, extra-hours and Sunday or holiday pay is exempt from contributions for full-time employees; the base pay is not. Details and other KPK codes: `gr-employee-contributions`.

**Step 3: taxable pay.** Gross pay minus the employee's compulsory social insurance contributions (art. 14(1)(δ) ΚΦΕ).

**Step 4: withholding.** Monthly employment income is annualised and taxed under art. 15(1) and art. 16 (art. 60(1)). From 2026 the reference is to the whole of art. 15(1), so the child rates and the under-30 rates apply in the monthly withholding, not only in the annual return (art. 60(1) as amended by ν. 5246/2025 art. 3(5), in force for income from tax year 2026). The Minister of Finance sets the annualisation method by decision (art. 60(3)). The worked examples annualise over the 14 payments a monthly-paid employee receives in a full year (12 salaries, the Christmas bonus and the Easter bonus, plus the holiday allowance) and spread the annual tax evenly over them. See "Not yet confirmed".

**Step 5: net pay.** Gross minus employee contributions minus tax withheld.

**Bonuses.** The Christmas bonus is one month's salary (or 25 daily wages) for a full 1 May to 31 December. The Easter bonus is half a month's salary (or 15 daily wages) for a full 1 January to 30 April. Someone employed for part of the period gets 2/25 of monthly salary (or 2 daily wages) for each 19 days for Christmas, and 1/15 of half a month's salary (or 1 daily wage) for each 8 days for Easter, with a pro rata fraction for a shorter stretch (ΚΥΑ 19040/1981 art. 1, Ministry of Labour). Both bonuses are regular pay: they carry contributions, with the ceiling applied to each separately (`gr-employee-contributions`), and they go into the annualised withholding.

**Extra pay at 20%.** An additional payment that is not part of regular pay, and back pay for earlier years, is withheld at a flat 20% when paid (art. 60(4)). This is a withholding rate, not the final tax: it is reconciled on the employee's return.

**Premiums.** Hourly pay is the basis for extra work (plus 20%) and overtime (plus 40%, or 60% with Ministry approval above the limits, or 120% if illegal). Sunday and holiday work earns 75% of 1/25 of monthly salary per day. Night work earns 25% on top (Ministry of Labour).

**Severance** on termination is taxed separately and finally on the art. 15(3) scale (0% up to EUR 60,000). It is not added to the annualised salary.

## Deadlines and filing

| Event | Deadline | Source |
|---|---|---|
| Hiring, change of terms, end of employment | Declared digitally in ERGANI II, which replaced the E3, E5, E6 and E7 forms from 16 February 2026 | [Ministry of Labour, ERGANI II](https://ypergasias.gov.gr/ergani/) |
| Overtime | Declared in ERGANI II before it is worked; employers on the digital work card with the ex post option declare it by the end of the month after the month it was worked | [Ministry of Labour, working time](https://ypergasias.gov.gr/en/labour-relations/individual-employment-relations/working-time-limits/) |
| Digital work card | Start and end of each shift sent to ERGANI II within 15 minutes, for employers in sectors brought into the system | [Ministry of Labour circular 25291/23-09-2026](https://ypergasias.gov.gr/wp-content/uploads/2026/09/90%CE%91%CE%9F46%CE%9D%CE%9B%CE%94%CE%93-%CE%9379.pdf) |
| Withholding return (ΦΜΥ, form Α.1099.19) and payment of tax withheld | By the end of the second month counting from the payment date, that is the last working day of the month after the month of payment. Example: tax on salaries paid in September 2026 is due by 2 November 2026 | ΚΦΕ art. 60(5); [AADE, withholding returns](https://www.aade.gr/exypiretisi-enimerosi/hristikoi-odigoi/enarxi-epiheirimatikis-drastiriotitas/ypoboli-diloseon-parakratoymenon-foron); [AADE deadlines calendar](https://www.aade.gr/) |
| ΦΜΥ return when no tax is due | Still filed | AADE, withholding returns |
| Stopping all employment | ΦΜΥ return with the box "Ολική παύση απασχόλησης προσωπικού" ticked | same |
| APD to e-EFKA | Pay month January 2026: 1 Feb to 2 Mar 2026; then each month from the 1st to the end of the next month (September pay: 1 Oct to 2 Nov 2026; December pay: 1 Jan to 1 Feb 2027) | [e-EFKA FAQ](https://www.e-efka.gov.gr/en/node/129) (general document 2034418/04.12.2025) |
| Payment of contributions | Last working day of the month after the pay month, with the employer's 23-digit RF code | same |
| Christmas bonus | Pay period 1 May to 31 December | ΚΥΑ 19040/1981 |
| Easter bonus | Pay period 1 January to 30 April | same |

The annual final ΦΜΥ return (form E7) no longer exists for tax years from 1 January 2014 ([AADE, Οριστική ΦΜΥ](https://www.aade.gr/oristiki-fmy)). The monthly returns are the record.

## Penalties and interest

| Breach | Penalty | Source |
|---|---|---|
| Tax not withheld | Employer pays the tax that should have been withheld, plus fines | ΚΦΕ art. 59(2) |
| Withholding return not filed or filed late | EUR 250 per breach (single-entry books) or EUR 500 (double-entry books) | ΚΦΔ art. 53(2) |
| Late amended withholding return where the original was on time | No fine under art. 53(1) or (2) | ΚΦΔ art. 53(7)(α) |
| Withholding return never filed where tax would be due | 50% of the tax on the missing return | ΚΦΔ art. 53(6) |
| Inaccurate withholding return | 50% of the difference | ΚΦΔ art. 54(2) |
| Late payment of tax withheld | Interest from the day after the deadline | ΚΦΔ art. 52(1) |
| Late contributions to e-EFKA | Statutory surcharges; see `gr-employee-contributions` | e-EFKA |
| Illegal overtime | Employee owed hourly pay plus 120%; employer criminal liability under ν. 3996/2011 arts. 24 and 28 | Ministry of Labour, working time |
| Digital work card breaches | Administrative fines in annexes V and VI of ministerial decision 80016/31-08-2022 (Β' 4629), imposed by the Labour Inspectorate | Ministry of Labour circular 25291/23-09-2026 |

## Cross-border points

- **Non-resident employees** working in Greece are taxed in Greece on that employment income, and the employer withholds in the same way. They do not get the art. 16 reduction unless they live in another EU or EEA state and meet the art. 20 test. See `gr-cross-border`.
- **5C inbound workers.** 50% of Greek employment income is exempt for 7 years under art. 5C. Contributions are still due in full. See `gr-cross-border`.
- **Postings.** An employee posted to Greece who holds an A1 from another EU state stays in that state's social security and is left off the Greek APD. See `gr-employee-contributions` and `gr-cross-border`.

## Worked examples

### Example 1: full-year employee, EUR 1,500 a month, no children

Eleni, aged 35, no dependent children, works full time all year under KPK 101 for EUR 1,500 a month. She receives 12 salaries, a Christmas bonus of one month's salary (EUR 1,500), an Easter bonus of half a month (EUR 750), and a holiday allowance of EUR 750 under her contract. Her gross pay for 2026 is EUR 21,000. No month is above the ceiling.

Employee contributions are 13.37% of EUR 21,000, so EUR 2,807.70. Taxable pay is EUR 18,192.30. Scale tax: 9% on 10,000 (EUR 900) plus 20% on 8,192.30 (EUR 1,638.46), so EUR 2,538.46. The reduction is EUR 777 minus EUR 20 for each EUR 1,000 above EUR 12,000: 777 minus 123.85, so EUR 653.15. Annual tax is EUR 1,885.31. Spread over 14 payments, the employer withholds EUR 134.66 from each. A normal month's payslip: 1,500 gross, minus EUR 200.55 contributions, minus EUR 134.66 tax, so EUR 1,164.79 net. Tax on the March salary goes on the ΦΜΥ return due by 30 April 2026.

```oa-check
name: GR payroll, EUR 1,500 a month, 14 payments, no children, 2026
inputs:
  monthly: 1500
  holiday_allowance: 750
  employee_rate_pct: 13.37
  payments: 14
steps:
  - gross_year: monthly * 12 + monthly + monthly / 2 + holiday_allowance
  - contrib_year: round(gross_year * employee_rate_pct / 100, 2)
  - taxable: gross_year - contrib_year
  - scale_tax: min(taxable, 10000) * 0.09 + max(min(taxable, 20000) - 10000, 0) * 0.20 + max(min(taxable, 30000) - 20000, 0) * 0.26 + max(min(taxable, 40000) - 30000, 0) * 0.34 + max(min(taxable, 60000) - 40000, 0) * 0.39 + max(taxable - 60000, 0) * 0.44
  - reduction: round(max(777 - max(taxable - 12000, 0) / 1000 * 20, 0), 2)
  - annual_tax: round(max(scale_tax - reduction, 0), 2)
  - withholding_per_payment: round(annual_tax / payments, 2)
  - monthly_contrib: round(monthly * employee_rate_pct / 100, 2)
  - net_month: monthly - monthly_contrib - withholding_per_payment
expected:
  gross_year: 21000.00
  contrib_year: 2807.70
  taxable: 18192.30
  scale_tax: 2538.46
  reduction: 653.15
  annual_tax: 1885.31
  withholding_per_payment: 134.66
  net_month: 1164.79
```

### Example 2: employee aged 28, EUR 2,200 a month, under-30 rate in withholding

Giorgos is 28, has no children and earns EUR 2,200 a month under KPK 101 all year, with the two bonuses and a contract holiday allowance of EUR 1,100. Gross pay is EUR 30,800. The edge case: from 2026 the monthly withholding uses all of art. 15(1), so his first EUR 20,000 is taxed at 9% instead of 9% and 20%.

Contributions are 13.37% of EUR 30,800, so EUR 4,117.96. Taxable pay is EUR 26,682.04. With the under-30 rate, scale tax is 9% on 20,000 (EUR 1,800) plus 26% on 6,682.04 (EUR 1,737.33), so EUR 3,537.33. On the ordinary scale it would be EUR 4,637.33, so the youth rate saves EUR 1,100. The reduction is 777 minus 293.64, so EUR 483.36. Annual tax is EUR 3,053.97, or EUR 218.14 per payment. Net for a normal month: 2,200 minus EUR 294.14 contributions minus EUR 218.14 tax, so EUR 1,687.72.

```oa-check
name: GR payroll, age 28, EUR 2,200 a month, under-30 rate, 2026
inputs:
  monthly: 2200
  holiday_allowance: 1100
  employee_rate_pct: 13.37
  payments: 14
steps:
  - gross_year: monthly * 12 + monthly + monthly / 2 + holiday_allowance
  - contrib_year: round(gross_year * employee_rate_pct / 100, 2)
  - taxable: gross_year - contrib_year
  - youth_tax: min(taxable, 20000) * 0.09 + max(min(taxable, 30000) - 20000, 0) * 0.26 + max(min(taxable, 40000) - 30000, 0) * 0.34 + max(min(taxable, 60000) - 40000, 0) * 0.39 + max(taxable - 60000, 0) * 0.44
  - ordinary_tax: min(taxable, 10000) * 0.09 + max(min(taxable, 20000) - 10000, 0) * 0.20 + max(min(taxable, 30000) - 20000, 0) * 0.26 + max(min(taxable, 40000) - 30000, 0) * 0.34 + max(min(taxable, 60000) - 40000, 0) * 0.39 + max(taxable - 60000, 0) * 0.44
  - youth_saving: ordinary_tax - youth_tax
  - reduction: round(max(777 - max(taxable - 12000, 0) / 1000 * 20, 0), 2)
  - annual_tax: round(max(youth_tax - reduction, 0), 2)
  - withholding_per_payment: round(annual_tax / payments, 2)
  - monthly_contrib: round(monthly * employee_rate_pct / 100, 2)
  - net_month: monthly - monthly_contrib - withholding_per_payment
expected:
  gross_year: 30800.00
  contrib_year: 4117.96
  taxable: 26682.04
  youth_tax: 3537.33
  youth_saving: 1100.00
  reduction: 483.36
  annual_tax: 3053.97
  withholding_per_payment: 218.14
  net_month: 1687.72
```

## Ask the client first

1. For each employee: monthly salary or daily wage, full or part time, white- or blue-collar, and years of prior service? This sets the minimum wage, seniority increments and the bonus amounts.
2. Age on 31 December 2026 and number of dependent children? Under-31s and parents get lower rates and a larger reduction in the monthly withholding.
3. Which KPK applies (BAE occupation, occupational risk, supplementary branch)? This sets the contribution rates.
4. Any overtime, night, Sunday or holiday work, and is the employer on the digital work card? This sets premiums, the exempt base for contributions and the ERGANI II declarations.
5. Any extra payments outside regular pay, back pay or severance in 2026? These are withheld at 20% or taxed on the severance scale, outside the monthly calculation.
6. Is anyone non-resident, on 5C, or posted with an A1? This changes withholding and contributions.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Code (ν. 4172/2013), Ministry of Finance codification up to ν. 5264/2025: arts. 14(1)(δ), 15(1) and (3), 16, 59, 60 and footnote 362 on ν. 5246/2025 | https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf | 2026-10-23 |
| Tax Procedure Code (ν. 5104/2024), AADE codification Ε.2109/2025: arts. 52, 53, 54 | https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf | 2026-10-23 |
| AADE, withholding returns (deadline, form Α.1099.19, nil returns, closing payroll) | https://www.aade.gr/exypiretisi-enimerosi/hristikoi-odigoi/enarxi-epiheirimatikis-drastiriotitas/ypoboli-diloseon-parakratoymenon-foron | 2026-10-23 |
| AADE home page, deadlines calendar (salary withholding for September 2026 due 02/11) | https://www.aade.gr/ | 2026-10-23 |
| AADE, final ΦΜΥ return E7 (abolished from tax year 2014) | https://www.aade.gr/oristiki-fmy | 2026-10-23 |
| e-EFKA circular 38/2024 and KPK table (KPK 101: 13.37% employee, 21.79% employer) | https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-38-24122024 | 2026-10-23 |
| e-EFKA circular 4/2026 (ceiling EUR 7,761.94 from 1.1.2026) | https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-42026 | 2026-10-23 |
| e-EFKA FAQ, ordinary businesses (APD periods 2026, payment deadline, RF code) | https://www.e-efka.gov.gr/en/node/129 | 2026-10-23 |
| Ministry of Labour, minimum wage (EUR 880 and EUR 920; EUR 39.30 and EUR 41.09; seniority) | https://ypergasias.gov.gr/en/labour-relations/collective-employment-relations/minimum-wage/ | 2026-10-23 |
| Ministry of Labour, holiday bonuses (ΚΥΑ 19040/1981) | https://ypergasias.gov.gr/ergasiakes-scheseis/syllogikes-ergasiakes-sxeseis/epidomata-eorton/ | 2026-10-23 |
| Ministry of Labour, working time limits (extra work, overtime, Sunday and holiday pay) | https://ypergasias.gov.gr/en/labour-relations/individual-employment-relations/working-time-limits/ | 2026-10-23 |
| Ministry of Labour, working time limits in Greek (night work 25%) | https://ypergasias.gov.gr/ergasiakes-scheseis/atomikes-ergasiakes-sxeseis/chronika-oria-ergasias/ | 2026-10-23 |
| Ministry of Labour, employee leave (annual leave) | https://ypergasias.gov.gr/ergasiakes-scheseis/atomikes-ergasiakes-sxeseis/adeies-ergazomenon/ | 2026-10-23 |
| Ministry of Labour, ERGANI II (live from 16 February 2026; digital hiring, changes and terminations) | https://ypergasias.gov.gr/ergani/ | 2026-10-23 |
| Ministry of Labour, digital work card page | https://ypergasias.gov.gr/apascholisi/psifiaki-karta-ergasias/ | 2026-10-23 |
| Ministry of Labour interpretive circular 25291/23-09-2026 on the digital work card | https://ypergasias.gov.gr/wp-content/uploads/2026/09/90%CE%91%CE%9F46%CE%9D%CE%9B%CE%94%CE%93-%CE%9379.pdf | 2026-10-23 |

Not yet confirmed: the Ministry of Finance decision under ΚΦΕ art. 60(3) that sets how monthly pay is annualised (the examples annualise over 14 payments and spread the tax evenly, which is our assumption); the statutory amount of the holiday allowance (επίδομα αδείας), so the examples take it from the contract; the payment dates of the Christmas and Easter bonuses; whether the employer must still give each employee an annual pay and withholding certificate, and its deadline; the 2026 APD periods for the bonuses; whether ERGANI II hiring must be declared before the first day of work; the amounts of the Labour Inspectorate fines (undeclared work, digital work card); the late-payment interest rate under ΚΦΔ art. 52 (set by ministerial decision); how employer registration with e-EFKA is done for a first-time employer.
