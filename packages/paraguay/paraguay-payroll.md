---
name: paraguay-payroll
description: "Paraguay payroll for private-sector employees in 2026: the two minimum wages of the year (G 2,899,048 a month to 30 June under Decreto N° 4122/2025 and G 3,044,000 from 1 July 2026 under Decreto N° 6225/2026 and Resolución MTESS N° 670/2026), the daily, hourly, night, part-time and apprentice minimums, working hours, overtime at 50%, night work at 30%, night overtime and holidays at 100%, the aguinaldo (13th salary, one twelfth of the year's pay, before 31 December, free of IPS and IRP), the family allowance (5% of the minimum wage per child), the payslip, permitted deductions, gross-to-net with the 9% IPS withholding, the employer's cost, and why a private employer withholds no income tax (IRP) from salaries. Also holidays, notice and the dismissal indemnity. Trigger on: Paraguay payroll, planilla de sueldos, salario mínimo 2026 Paraguay, aguinaldo, sueldo neto, horas extras Paraguay, bonificación familiar, asignación familiar, costo del empleado Paraguay. Out of scope: IPS rates in detail (paraguay-social-contributions), the employee's own IRP return (paraguay-income-tax)."
version: 0.4
jurisdiction: PY
tax_year: 2026
last_updated: 2026-11-14
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
type: computation
tier: 2
domain: payroll
---

# Paraguay payroll: minimum wage, overtime, aguinaldo and gross-to-net, 2026 v0.4

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Employment in the private sector is governed by the Código del Trabajo, Ley N° 213/1993, as amended by Ley N° 496/1995, read in the texts published by the Biblioteca y Archivo Central del Congreso Nacional (BACN). The minimum wage is fixed by decree of the Executive on the proposal of the Consejo Nacional de Salarios Mínimos (CONASAM) and set out in detail by a resolution of the Ministerio de Trabajo, Empleo y Seguridad Social (MTESS). Amounts are in guaraníes (G). The pay year is the calendar year 2026, which has **two minimum wages**: one to 30 June and one from 1 July.

The social security rates (9% worker, 16.5% employer) and the IPS rules belong to [paraguay-social-contributions](paraguay-social-contributions.md); this skill uses them in gross-to-net. The employee's own income tax (IRP) belongs to [paraguay-income-tax](paraguay-income-tax.md).

**Quick answer.** In 2026 the monthly minimum wage for unspecified activities is G 2,899,048 to 30 June and G 3,044,000 from 1 July. Net pay is gross pay less the employee's 9% IPS contribution; a private employer withholds no income tax. The employer pays 16.5% IPS on top. The aguinaldo is one twelfth of everything earned in the calendar year, paid before 31 December, with no IPS and no IRP.

## Who this applies to

- Employees of private employers in Paraguay, paid monthly (mensualizados), by the day (jornaleros), by the hour, by the piece or on commission (Labour Code art. 230).
- Domestic workers, who are entitled to the full minimum wage for unspecified activities; those on shorter or broken hours may not be paid proportionally less (Ley 5407/2015 art. 10 as replaced by Ley 6338/2019).
- Part-time workers and apprentices, who have their own minimum hourly and monthly amounts (Resolución MTESS 670/2026 arts. 2 and 3).

Out of scope: public servants, bank employees' pension contributions (Caja Bancaria, see [paraguay-social-contributions](paraguay-social-contributions.md)), occupation-specific minimum wages in the annex of Resolución 670/2026 (look them up there), collective agreements, and the IRP return of the employee.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Minimum monthly wage, unspecified activities, day work, 1 January to 30 June 2026 (Decreto 4122/2025; Resolución MTESS 677/2025) | G 2,899,048; day wage for jornaleros G 111,502; daily wage of monthly paid G 96,635; hourly G 12,080 | 2026 (to 30 June) | https://www.mtess.gov.py/?p=30682 |
| Same, night work, to 30 June 2026 | monthly G 3,768,763; jornal G 144,952; daily G 125,625; hourly G 17,947 | 2026 (to 30 June) | same |
| Part-time hourly minimum and apprentice minimum, to 30 June 2026 | part-time G 13,937 day hour, G 20,708 night hour; apprentice G 1,739,429 a month, G 66,901 a day | 2026 (to 30 June) | same |
| Minimum monthly wage, unspecified activities, day work, from 1 July 2026 (Decreto 6225/2026 art. 2; Resolución MTESS 670/2026 art. 1) | G 3,044,000 (5% increase); jornal G 117,077; daily wage of monthly paid G 101,467; hourly G 12,683 | 2026 (from 1 July) | https://www.mtess.gov.py/wp-content/uploads/2026/07/Resolucion-MTESS-N%C2%B0-670-REGLAMENTACION-SALARIO-2026.pdf |
| Same, night work, from 1 July 2026 (Res. 670 art. 1) | monthly G 3,957,200; jornal G 152,200; daily G 131,907; hourly G 18,844 | 2026 (from 1 July) | same |
| Part-time hourly minimum from 1 July 2026 (Res. 670 art. 2) | G 14,635 day hour; G 21,743 night hour | 2026 (from 1 July) | same |
| Apprentice and dual apprenticeship minimum from 1 July 2026 (Res. 670 art. 3) | G 1,826,400 a month; G 70,246 a day | 2026 (from 1 July) | same |
| How the minimum daily and hourly amounts are derived (Res. 670 art. 1) | monthly paid: monthly / 30 per day, then / 8 per day hour or / 7 per night hour; jornaleros and piece work: monthly / 26 per day | 2026 | same |
| Maximum ordinary hours (Labour Code art. 194 as replaced by Ley 496; arts. 195 and 196) | day work (06:00 to 20:00) 8 a day, 48 a week; night work (20:00 to 06:00) 7 a day, 42 a week; mixed 7.5 a day, 45 a week | 2026 | [Ley 496, amended hours](https://www.bacn.gov.py/leyes-paraguayas/2514/ley-n-496-modifica-amplia-y-deroga-articulos-de-la-ley-213-93-codigo-del-trabajo); [Labour Code art. 195, times](https://www.bacn.gov.py/leyes-paraguayas/2608/ley-n-213-establece-el-codigo-del-trabajo) |
| Overtime, night work, night overtime, holidays (art. 234) | overtime at least +50% of the ordinary rate; night work +30% over day pay; night overtime +100% of the night hourly rate; hours on public holidays +100% of the ordinary working-day hourly rate | 2026 | https://www.bacn.gov.py/leyes-paraguayas/2608/ley-n-213-establece-el-codigo-del-trabajo |
| Aguinaldo (arts. 243 to 245) | one twelfth of all pay earned in the calendar year (salary, overtime, commissions and other); before 31 December, or on leaving; cannot be attached | 2026 | same |
| Family allowance (arts. 261 to 263, 268 and 269) | 5% of the minimum wage per child under 17 (no age limit if fully disabled), living in Paraguay, under the worker's parental authority and maintained by the worker; lost if the worker's salary exceeds 200% of the minimum wage; if both parents are employees, paid to only one and not payable if either parent's wage exceeds that threshold (art. 266); not salary for the aguinaldo or IPS; paid with the salary | 2026 | same |
| Pay in kind (art. 231) | exceptionally at most 30% of pay, with fair and reasonable valuation, and only where suited to the worker's and family's personal use | 2026 | same |
| Recovery of debts to the employer (art. 242) | at most 30% of the month's pay | 2026 | same |
| Paid holidays (art. 218 as replaced by Ley 496) | after each completed continuous year with the same employer: up to 5 years' service 12 working days; over 5 to 10 years 18; over 10 years 30 | 2026 | https://www.bacn.gov.py/leyes-paraguayas/2514/ley-n-496-modifica-amplia-y-deroga-articulos-de-la-ley-213-93-codigo-del-trabajo |
| Notice for an open-ended contract (art. 87) | after probation up to 1 year 30 days; over 1 to 5 years 45; over 5 to 10 years 60; over 10 years 90 | 2026 | https://www.bacn.gov.py/leyes-paraguayas/2608/ley-n-213-establece-el-codigo-del-trabajo |
| Dismissal without just cause (art. 91 as replaced by Ley 496; art. 92 b) | 15 daily wages for each year of service or fraction over six months, on the average pay of the last six months | 2026 | https://www.bacn.gov.py/leyes-paraguayas/2514/ley-n-496-modifica-amplia-y-deroga-articulos-de-la-ley-213-93-codigo-del-trabajo |

## The base

**Gross pay.** Salary, overtime, night and holiday premiums, commissions, bonuses and pay in kind. The family allowance is paid on top and is not salary for the aguinaldo or IPS (art. 268). Meal allowances, transfer and travel costs and other items given to make the work possible are not salary (art. 230, last paragraph).

**Minimum wage check.** Full-time pay may not be below the minimum for the period: G 2,899,048 a month for January to June 2026 and G 3,044,000 from July. A worker paid by the day may not receive less than the monthly minimum divided by 26 (art. 232 a as replaced by Ley 496). Night work is paid on the minimum plus 30% (Res. 670 art. 1).

**Hourly rate for overtime.** Resolución 670 art. 1 expressly derives minimum hourly rates from the monthly minimum: /30 per day, then /8 for day work or /7 for night work. Its application to an agreed above-minimum monthly salary was not established from a primary provision here. Use the verified applicable minimum hourly amount in the example below; obtain the correct contractual/legal hourly base before computing above-minimum overtime.

**Full-time general-regime gross to net, each month.**

For part-time or special pension regimes, use the corresponding base and rates in [paraguay-social-contributions](paraguay-social-contributions.md); this algorithm's floor and 9%/16.5% are not universal.

1. Gross pay for the month (without the family allowance).
2. Employee's IPS: 9% of gross pay, never on less than the minimum wage (rate and base rules in [paraguay-social-contributions](paraguay-social-contributions.md)).
3. **No income tax withholding.** Ley 6380/2019 art. 54 lets the tax authority designate IRP withholding agents, and the IRP regulation, Decreto 3184/2019, designates them only for particular cases: diplomatic and consular staff and military personnel posted abroad (art. 64), some capital income and gaming prizes. It designates no private employer for salaries. The employee files and pays any IRP on Form 515 ([paraguay-income-tax](paraguay-income-tax.md)).
4. Other deductions only as art. 240 allows: salary advances, compulsory social insurance, union, cooperative or mutual dues with written consent, court-ordered amounts, and judicially established damage. Debts to the employer are recovered at no more than 30% of the month's pay (art. 242).
5. Net pay = gross pay less the deductions, plus the family allowance.
6. **Employer cost** = gross pay + employer IPS of 16.5% + the family allowance.

**Aguinaldo.** One twelfth of all pay earned in the calendar year, in every form (salary, overtime, commissions and other); the family allowance is not counted (art. 268). Paid before 31 December, or in proportion when the worker leaves (arts. 243 and 244). It bears no IPS (it is outside the IPS salary definition) and is exempt from IRP ([paraguay-income-tax](paraguay-income-tax.md)). It cannot be attached (art. 245).

**Payslip.** With each payment the worker receives a liquidation sheet signed by the employer stating the base salary, the days or pieces paid, the amounts due beyond the base salary, and each deduction. The employer keeps the original signed by the worker as receipt; the worker keeps the copy (art. 235).

## Deadlines and filing

1. **Pay day.** Pay by week, fortnight or month; daily, weekly or fortnightly for workers not employed every day; piece work every 15 days (art. 232). Pay on working days, at the workplace, within two hours of the end of the shift unless agreed otherwise in writing (art. 236). Holiday pay is paid in advance (art. 220).
2. **Aguinaldo** before 31 December 2026, or on leaving (art. 243).
3. **IPS.** The monthly REI planilla and payment of the 9% and 16.5%: see [paraguay-social-contributions](paraguay-social-contributions.md).
4. **Minimum wage notice.** The 2026 increase applies to July pay; the MTESS takes complaints from workers not paid the new minimum ([MTESS, 18 June 2026](https://www.mtess.gov.py/?p=36166)).
5. **On leaving.** The employer gives the worker a signed certificate with the start and end dates, the type of work and the pay for the last period (art. 93), and pays the proportional aguinaldo (art. 244).

## Penalties and interest

- **Unpaid minimum wage, aguinaldo or premiums** are labour claims the worker may bring before the MTESS or the labour courts. Labour Code fines were not read for this skill; see Not yet confirmed.
- **IPS** penalties (late registration, contributions withheld and not paid, the crime of evasión de aportes) are in [paraguay-social-contributions](paraguay-social-contributions.md#penalties-and-interest).
- **Notice not given** (art. 90): the employer pays the salary for the notice period; a worker who leaves without notice owes half of it.

## Cross-border points

- **Foreign employees** working in Paraguay for a Paraguayan employer are paid under the same Labour Code rules and insured with IPS.
- **Pay to a non-resident** for work in Paraguay may bear the non-resident income tax (INR) withheld by the payer; that is outside this skill.
- **Currency.** Wages are paid in legal tender (art. 231). Convert a salary agreed in another currency before applying the minimum-wage check.

## Two worked examples that recompute

### Example 1: monthly employee in July 2026 with overtime

Carla is a full-time monthly employee earning the unspecified-activities day minimum of G 3,044,000 in July 2026. She works 8 day overtime hours and has no children. The official Res. 670 art. 1 minimum hourly amount is G 12,683; this example uses that published amount rather than an unverified above-minimum division rule.

- Overtime at +50%: 8 × G 12,683 × 1.5 = G 152,196.
- Gross pay G 3,196,196, above the July minimum.
- Employee IPS 9%: G 287,657.64; no IRP withheld.
- Net pay G 2,908,538.36.
- Employer IPS 16.5%: G 527,372.34; employer cost G 3,723,568.34.

Fractional guaraníes show exact arithmetic; the filing/payment rounding convention is not established here.

```oa-check
name: PY payroll July 2026, official minimum hourly input and 8 overtime hours
inputs:
  salary: 3044000
  official_hourly: 12683
  overtime_hours: 8
  ips_worker: 0.09
  ips_employer: 0.165
steps:
  - overtime_pay: overtime_hours * official_hourly * 1.5
  - gross: salary + overtime_pay
  - employee_ips: gross * ips_worker
  - net_pay: gross - employee_ips
  - employer_ips: gross * ips_employer
  - employer_cost: gross + employer_ips
expected:
  overtime_pay: 152196
  gross: 3196196
  employee_ips: 287657.64
  net_pay: 2908538.36
  employer_ips: 527372.34
  employer_cost: 3723568.34
```

### Example 2: minimum-wage worker, aguinaldo across the July increase, and a leaver

Diego works on the minimum wage for unspecified activities all of 2026, with two children who qualify for the family allowance.

- **Monthly pay.** G 2,899,048 for January to June and G 3,044,000 from July.
- **Family allowance from July.** 5% of 3,044,000 per child: G 152,200 each, G 304,400 for two. Assume the child/support conditions are met and either the other parent is not an employee or neither employed parent earns more than 200% of the minimum; only Diego claims the allowance. His own salary alone would not establish eligibility if the other employed parent exceeded that threshold. It is paid on top and not counted for the aguinaldo.
- **Aguinaldo.** Pay earned in 2026: 6 x 2,899,048 + 6 x 3,044,000 = G 35,658,288. One twelfth: G 2,971,524, paid before 31 December, with no IPS and no IRP.
- **Edge case: he leaves on 30 September.** Pay earned to then: 6 x 2,899,048 + 3 x 3,044,000 = G 26,526,288. Proportional aguinaldo on leaving: G 2,210,524.

```oa-check
name: PY aguinaldo 2026 for a minimum-wage worker across the July increase, full year and leaver
inputs:
  mw_first_half: 2899048
  mw_second_half: 3044000
  allowance_rate: 0.05
  children: 2
steps:
  - allowance_per_child_july: mw_second_half * allowance_rate
  - allowance_two_children_july: allowance_per_child_july * children
  - pay_full_year: 6 * mw_first_half + 6 * mw_second_half
  - aguinaldo_full_year: pay_full_year / 12
  - pay_to_30_september: 6 * mw_first_half + 3 * mw_second_half
  - aguinaldo_leaver: pay_to_30_september / 12
expected:
  allowance_per_child_july: 152200
  allowance_two_children_july: 304400
  pay_full_year: 35658288
  aguinaldo_full_year: 2971524
  pay_to_30_september: 26526288
  aguinaldo_leaver: 2210524
```

## Ask the client first

1. Is the worker paid monthly, by the day, by the hour (part-time) or by the piece, and is the work by day, night or mixed?
2. The month and year of the pay (before or from 1 July 2026), the agreed salary in guaraníes and any occupation-specific minimum in Resolución MTESS 670/2026.
3. Overtime, night and holiday hours worked, commissions, bonuses and pay in kind.
4. Children under 17 (or disabled) living in Paraguay, under the worker's parental authority and maintained by the worker, whether both parents are employees, each parent's wage, and whether the other parent already receives the allowance.
5. Start date (for holidays, notice and indemnity) and, for a leaver, the end date and the reason.
6. Whether the employer is a bank (Caja Bancaria) or a household employing a domestic worker.

## Sources

| Source | URL | Read on |
|---|---|---|
| MTESS, news of Resolución 677/2025 under Decreto 4122/2025: minimum wages from 1 July 2025 (in force to 30 June 2026) | https://www.mtess.gov.py/?p=30682 | 2026-11-11 |
| Resolución MTESS N° 670/2026 under Decreto 6225/2026: considerandos and arts. 1 to 3 read (minimum wages from 1 July 2026); the occupation annex not read | https://www.mtess.gov.py/wp-content/uploads/2026/07/Resolucion-MTESS-N%C2%B0-670-REGLAMENTACION-SALARIO-2026.pdf | 2026-11-11 |
| MTESS, news of Decreto 6225/2026 (5% increase from 1 July 2026, complaints) | https://www.mtess.gov.py/?p=36166 | 2026-11-11 |
| Ley N° 213/1993, Código del Trabajo, BACN text: arts. 87, 90, 92, 93, 195, 220, 230, 231, 234 to 245, 261 to 269 | https://www.bacn.gov.py/leyes-paraguayas/2608/ley-n-213-establece-el-codigo-del-trabajo | 2026-11-11 |
| Ley N° 496/1995, BACN text: new arts. 91, 194, 196, 218 and 232 of the Labour Code | https://www.bacn.gov.py/leyes-paraguayas/2514/ley-n-496-modifica-amplia-y-deroga-articulos-de-la-ley-213-93-codigo-del-trabajo | 2026-11-11 |
| Ley N° 6338/2019, BACN text: art. 1 (domestic workers on the full minimum wage) | https://www.bacn.gov.py/leyes-paraguayas/8840/ley-n-6338-modifica-el-articulo-10-de-la-ley-n-5407-15 | 2026-11-11 |
| Ley N° 6380/2019, BACN text: art. 54 (IRP withholding agents) | https://www.bacn.gov.py/leyes-paraguayas/9332/ley-n-6380-de-modernizacion-y-simplificacion-del-sistema-tributario-nacional | 2026-11-11 |
| Decreto N° 3184/2019 (IRP regulation), DNIT copy: arts. 63 and 64 and every article naming an agente de retención | https://www.dnit.gov.py/documents/47797/47809/Decreto+N%C2%B0+3184-19.pdf/6eaa47e9-504b-fc0b-6a03-4dc2b267e2a8 | 2026-11-11 |

Not yet confirmed: the text of Decreto 4122/2025 and Decreto 6225/2026 themselves (read through the MTESS resolution and news pages); the occupation-specific minimums in the annex of Resolución 670/2026; whether the hourly rate for overtime of a monthly worker on more than the minimum must use 30 days and 8 hours as for the minimum (the Code says only "salario convenido para la jornada ordinaria"); Labour Code fines for unpaid wages and the labour inspection procedure; whether any law after Ley 496/1995 changed the articles used here (the BACN texts are the original laws, not a consolidation; Ley 1416 and Ley 3384 change other articles); the next minimum-wage adjustment; whether the 2026 IPS contributions table on the IPS portal has been updated for the July minimum wage. The earlier skill's IRP rate table and G 80,000,000 threshold are moved to [paraguay-income-tax](paraguay-income-tax.md), which owns them.

> Contributed by OpenAccountants.
