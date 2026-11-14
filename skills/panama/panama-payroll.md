---
name: panama-payroll
description: >
  Use this skill to run Panama payroll (planilla) in 2026. It covers the employer's
  income tax withholding on salaries using the art. 700 table (0% to B/.11,000 a year,
  15% to B/.50,000, B/.5,850 plus 25% above), the separate table for representation
  allowances (10% to B/.25,000, then B/.2,500 plus 15%), the monthly DGI Planilla 03
  filed within 60 days of the CSS planilla and its fines, and the CSS rates on salaries
  and on the three 13th-month instalments that live in panama-social-contributions.
  Trigger phrases include planilla Panama, retencion ISR salarios, gastos de
  representacion, Planilla 03, decimotercer mes and salario neto Panama.
version: "1.0"
jurisdiction: PA
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - payroll-workflow-base
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Panama payroll, 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Panamanian accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Panama.

## Who this applies to

Employers in Panama paying salaries in 2026. Income tax withholding and the DGI Planilla 03 are here; CSS rates are owned by [panama-social-contributions](panama-social-contributions.md); the employee's own return by [panama-income-tax](panama-income-tax.md). Amounts are in balboas (B/.), at par with the US dollar.

Refer: special regimes (SEM, City of Knowledge, free zones), non-resident staff, termination settlements, educational insurance on salaries (rates not confirmed in this pass), minimum wage questions (MITRADEL site blocked to scripts).

Conservative defaults:

| Ambiguity | Default |
| --- | --- |
| Gross salary unknown | Stop |
| Representation allowance paid | Withhold on its own table, not added to salary |
| Employee has two employers | Each withholds; the employee files one return for all income |

## Rates, bands and thresholds

| Item | Rate or amount | Condition | Source |
| --- | --- | --- | --- |
| Annual taxable income up to B/.11,000 | 0% | Art. 700 Codigo Fiscal | DGI, Planilla 03: https://dgi.mef.gob.pa/DInforme/Planilla03.php |
| B/.11,000 to B/.50,000 | 15% of the excess over B/.11,000 | | same |
| Above B/.50,000 | B/.5,850 plus 25% of the excess | | same |
| Representation allowances up to B/.25,000 | 10% | Art. 701 l) | same |
| Representation allowances above B/.25,000 | B/.2,500 plus 15% of the excess | | same |
| Planilla 03 deadline | Monthly, within 60 calendar days after the CSS planilla | Resolucion 201-4853 of 2022 | same |
| Planilla 03 fine, employer income up to B/.150,000 | B/.100 | Decreto Ejecutivo 20 of 2022 | same |
| Planilla 03 fine, B/.150,000 to B/.500,000 | B/.500 | | same |
| Planilla 03 fine, above B/.500,000 | B/.1,000 | | same |
| Employee CSS | 9.75% (7.25% on each 13th-month instalment) | | Gaceta Oficial 30284-B, Ley 51 consolidated: http://gacetas.procuraduria-admon.gob.pa/30284-B_64831.pdf |
| Employer CSS | 13.25% to 28 February 2027 (10.75% on each 13th-month instalment) | | same |

## The base

1. Estimate the employee's annual taxable salary and apply the art. 700 table; divide the annual tax by the pay periods for the monthly withholding.
2. Representation allowances are withheld on their own table, never added to salary.
3. Deduct the employee's CSS (9.75%) from the salary; the employer pays 13.25%. On the 13th-month instalments use 7.25% and 10.75%.
4. Report salaries and withholding monthly on Planilla 03; rectifying the report carries no fine.
5. A single-employer employee whose tax was fully withheld need not file a return, but may file to claim school costs and other deductions.

## Deadlines and filing

| Obligation | Deadline | Channel |
| --- | --- | --- |
| CSS planilla and payment | Monthly (CSS regulation) | CSS |
| Planilla 03 | Within 60 calendar days after the CSS planilla | DGI e-Tax 2.0 |
| Annual salary certificate to employee | For the employee's return | Employer |

## Penalties and interest

Planilla 03: B/.100, B/.500 or B/.1,000 by the employer's annual income. CSS late payment: 2% to 15% surcharges plus 1% a month interest (Ley 51 art. 121).

## Cross-border points

Payments of Panama-source income to people abroad are withheld on 50% of the payment (Form 05, see the income tax skill). Foreign employees on a Panamanian payroll contribute to CSS like nationals.

## Two worked examples that recompute

### Example 1: salary of B/.2,000 a month (B/.24,000 a year)

Annual tax (B/.24,000 less B/.11,000) x 15% = B/.1,950, B/.162.50 a month. Employee CSS B/.195.00; employer CSS B/.265.00. The 13th month is left out of this projection (its tax treatment was not confirmed in this pass).

```oa-check
name: PA 2026 withholding on B/.2,000 a month
inputs:
  monthly: 2000
steps:
  - annual: monthly * 12
  - annual_tax: (annual - 11000) * 0.15
  - monthly_tax: annual_tax / 12
  - css_employee: monthly * 0.0975
  - css_employer: monthly * 0.1325
expected:
  annual: 24000
  annual_tax: 1950
  monthly_tax: 162.5
  css_employee: 195
  css_employer: 265
```

### Example 2: B/.30,000 extra as salary or as representation allowance (decision)

A manager earns B/.40,000 a year (tax B/.4,350). Paying B/.30,000 more as salary raises income to B/.70,000 and the tax to B/.10,850: B/.6,500 more. Paid as a representation allowance it is taxed on its own table: B/.2,500 plus 15% of B/.5,000 = B/.3,250. The allowance must be a real representation allowance; DGI's conditions (for example, the limit relative to salary) were not confirmed in this pass.

```oa-check
name: PA 2026 extra pay as salary or representation allowance
inputs:
  salary: 40000
  extra: 30000
steps:
  - tax_salary_only: (salary - 11000) * 0.15
  - tax_with_extra_salary: 5850 + (salary + extra - 50000) * 0.25
  - extra_as_salary: tax_with_extra_salary - tax_salary_only
  - extra_as_allowance: 2500 + (extra - 25000) * 0.15
  - saving: extra_as_salary - extra_as_allowance
expected:
  tax_salary_only: 4350
  tax_with_extra_salary: 10850
  extra_as_salary: 6500
  extra_as_allowance: 3250
  saving: 3250
```

## Ask the client first

1. Each employee's salary, pay periods and 13th-month instalments.
2. Any representation allowance, and the employment contract terms.
3. The employer's annual income (Planilla 03 fine band).
4. Second jobs or other income of the employee.
5. Non-resident or special-regime staff.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for DGI, Planilla 03: art. 700 table, representation allowance table, monthly filing within 60 days, fines by income band | https://dgi.mef.gob.pa/DInforme/Planilla03.php | 2026-11-14 |
| Read for Gaceta Oficial 30284-B, Ley 51 consolidated: art. 96 rates, art. 121 surcharges | http://gacetas.procuraduria-admon.gob.pa/30284-B_64831.pdf | 2026-11-14 |
| Read for DGI FAQ, Declaraciones e Informes: who need not file | https://dgi.mef.gob.pa/Preguntas/DeclaracionInformes.php | 2026-11-14 |

Not yet confirmed: whether the employer projects tax over 13 months including the decimotercer mes, and the income tax treatment of the 13th month; educational insurance on salaries; minimum wages for 2026 (Decreto Ejecutivo, MITRADEL); the 13th-month payment dates (old file: 15 April, 15 August, 15 December, Codigo de Trabajo not read); conditions for representation allowances.
