---
name: el-salvador-social-contributions
description: "Use this skill for El Salvador social contributions on salaries in 2026. It gives the ISSS health regime rates (employer 7.5%, employee 3%) on salary up to the maximum contributory salary of USD 1,000 a month, and the pension rate of the Ley Integral del Sistema de Pensiones (Decreto 614 of 2022), 16% of the ingreso base de cotizacion (employee 7.25%, employer 8.75%), the base rules (aguinaldo, occasional bonuses and per diems excluded, not below the minimum wage, each job separately) and the split of the 16% (9% individual account, 6% guarantee account, 1% insurance and fees). Trigger phrases include ISSS El Salvador, AFP cotizacion, salario maximo cotizable, planilla unica, ingreso base de cotizacion and aportes patronales."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/el-salvador-social-contributions"
  jurisdiction: "SV"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# El Salvador social contributions (ISSS and pensions), 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Salvadoran accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in El Salvador.

## Who this applies to

Private sector employers and employees in El Salvador in 2026, for the Instituto Salvadoreno del Seguro Social (ISSS, health regime) and the pension system (AFP accounts under the Ley Integral del Sistema de Pensiones). ISR retention, aguinaldo and minimum wages are in [el-salvador-payroll](el-salvador-payroll.md).

Refer: self-employed voluntary affiliation, domestic workers, public sector, INSAFORP (rate not confirmed), occupational risk rules, arrears and AFP collection actions.

Conservative defaults:

| Ambiguity | Default |
| --- | --- |
| Salary above USD 1,000 | ISSS on USD 1,000 only; pension on the full salary |
| Aguinaldo | Not part of the pension base (LISP art. 14) |
| Two jobs | Contributions on each salary |
| Salary below the minimum wage | Pension base not below the minimum wage, except apprentices, farm and domestic workers |

## Rates, bands and thresholds

| Item | Rate or amount | Base and condition | Source |
| --- | --- | --- | --- |
| ISSS health regime, employer | 7.5% | Salary up to the maximum contributory salary | ISSS, salario maximo cotizable notice (transparency portal): https://www.transparencia.gob.sv/descarga_archivo.php?id=MTA4MDkz&inst=108093 |
| ISSS health regime, employee | 3% | Same base | same |
| ISSS maximum contributory salary | USD 1,000.00 a month | In force from August 2015 (raised from USD 685.71) | same |
| Pension contribution, total (LISP art. 16) | 16% of the ingreso base de cotizacion | Dependent workers | Asamblea Legislativa, Ley Integral del Sistema de Pensiones (Decreto 614): https://www.asamblea.gob.sv/sites/default/files/documents/decretos/F94AF319-257C-4A85-97B7-4D03A6C65A48.pdf |
| Pension, employee share | 7.25% | Of the base | same |
| Pension, employer share | 8.75% | Of the base | same |
| Split: individual savings account | 9.0% of the base | 7.25% from the worker plus 1.75% from the employer | same |
| Split: guarantee account (Cuenta de Garantia Solidaria) | 6.0% of the base | Employer | same |
| Split: insurance and AFP fee | 1.0% of the base | Employer | same |

## The base

- **ISSS:** monthly remuneration up to USD 1,000; above it the contribution is fixed at USD 75.00 (employer) and USD 30.00 (employee).
- **Pension (LISP art. 14):** the monthly salary or the sickness, accident or maternity subsidy; not below the legal minimum wage except apprentices, farm, domestic and similar workers. Salary includes everything paid in money for services, including vacation, commissions and sales percentages. Excluded: occasional bonuses and gratuities, the aguinaldo, per diems, representation expenses and statutory benefits. With two or more jobs the worker contributes on each salary. Calendar days of each month are used.
- **No pension ceiling** was found in art. 14 of the text read; the old file's referential cap is not used.
- **Income tax:** employee contributions reduce the ISR retention base (LISR art. 29.7, see the payroll skill).

## Deadlines and filing

| Obligation | Deadline | Channel |
| --- | --- | --- |
| ISSS contributions | Monthly; due date not confirmed in this pass | ISSS online employer service (OVISSS) |
| Pension contributions | Monthly, through the single payroll (planilla unica) | AFP |

## Penalties and interest

Pension law: AFPs must pursue unpaid contributions and employers have set periods to answer (LISP arts. 19 onward, not fully read). ISSS surcharges for late payment were not confirmed. Income tax retention penalties: see the payroll skill.

## Cross-border points

Foreign employees under a Salvadoran contract contribute like nationals. Totalisation agreements were not checked.

## Two worked examples that recompute

### Example 1: salary of USD 800

ISSS USD 24.00 (employee) and USD 60.00 (employer); pension USD 58.00 and USD 70.00. Employee total USD 82.00, employer total USD 130.00.

```oa-check
name: SV 2026 ISSS and pension, USD 800 salary
inputs:
  salary: 800
  isss_cap: 1000
steps:
  - isss_employee: min(salary, isss_cap) * 0.03
  - isss_employer: min(salary, isss_cap) * 0.075
  - afp_employee: salary * 0.0725
  - afp_employer: salary * 0.0875
  - employee_total: isss_employee + afp_employee
  - employer_total: isss_employer + afp_employer
expected:
  isss_employee: 24
  isss_employer: 60
  afp_employee: 58
  afp_employer: 70
  employee_total: 82
  employer_total: 130
```

### Example 2: salary of USD 2,500, where the ISSS cap bites (decision on cost)

ISSS stops at USD 1,000: USD 30.00 and USD 75.00. Pension has no cap: USD 181.25 and USD 218.75. Employer cost USD 293.75; without the ISSS cap it would be USD 112.50 higher. For pricing a senior hire, the employer's marginal rate above USD 1,000 is 8.75%, not 16.25%.

```oa-check
name: SV 2026 ISSS cap at USD 2,500
inputs:
  salary: 2500
  isss_cap: 1000
steps:
  - isss_employer: min(salary, isss_cap) * 0.075
  - afp_employer: salary * 0.0875
  - employer_total: isss_employer + afp_employer
  - saving_from_cap: salary * 0.075 - isss_employer
  - employee_total: min(salary, isss_cap) * 0.03 + salary * 0.0725
expected:
  isss_employer: 75
  afp_employer: 218.75
  employer_total: 293.75
  saving_from_cap: 112.5
  employee_total: 211.25
```

## Ask the client first

1. Monthly salary of each worker, and what is variable (commissions, bonuses, per diems).
2. Number of jobs each worker holds.
3. Sector and any apprentice, farm or domestic workers.
4. AFP of each worker and ISSS employer number.
5. Any arrears with ISSS or the AFP.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for the ISSS notice on the maximum contributory salary: 7.5% and 3% rates and the USD 1,000 ceiling from August 2015 | https://www.transparencia.gob.sv/descarga_archivo.php?id=MTA4MDkz&inst=108093 | 2026-11-14 |
| Read for Ley Integral del Sistema de Pensiones (Decreto 614 of 2022), arts. 14 (base) and 16 (rate and split) | https://www.asamblea.gob.sv/sites/default/files/documents/decretos/F94AF319-257C-4A85-97B7-4D03A6C65A48.pdf | 2026-11-14 |
| Read for LISR consolidated art. 29.7 (contributions in the retention) | https://www.asamblea.gob.sv/sites/default/files/documents/decretos/F326A5D9-F56E-4FCA-81D6-60088ABB52BF.pdf | 2026-11-14 |

Not yet confirmed: INSAFORP training levy (the old file said about 1% of payroll for employers with 10 or more workers; no official INSAFORP page read); ISSS and AFP payment deadlines and late surcharges; occupational risk contributions; whether a pension ceiling applies in 2026; self-employed affiliation rules.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `el-salvador-social-contributions` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/el-salvador-social-contributions. If neither is available, confirm every figure against the official source pages cited above before relying on it.
