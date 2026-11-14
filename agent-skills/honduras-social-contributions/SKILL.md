---
name: honduras-social-contributions
description: "Use this skill for Honduras social contributions on salaries in 2026. It gives the IHSS disability, old age and death (IVM) rates of Decreto 48-2024 (employer 3.5%, employee 2.5%) on salary up to the contribution ceiling (L11,903.13 for 2025, the latest set in law), the RAP labour reserve fund of Decreto 47-2024 (employer 4% of ordinary salary capped at three highest minimum wages, L57,896.16 in 2026), the RAP savings of 1.5% employee and 1.5% employer on salary above the IVM ceiling paid within 15 days, and what is still open (IHSS sickness and maternity rates, the 2026 ceiling, INFOP). Trigger phrases include IHSS Honduras, techo de cotizacion, RAP reserva laboral, IVM, aportaciones patronales and planilla IHSS."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/honduras-social-contributions"
  jurisdiction: "HN"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Honduras social contributions (IHSS and RAP), 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Honduran accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Honduras.

## Who this applies to

Employers and employees in the Honduran private sector covered by the Instituto Hondureno de Seguridad Social (IHSS) and the Regimen de Aportaciones Privadas (RAP) in 2026. ISR withholding, the 13th and 14th month and minimum wages are in [honduras-payroll](honduras-payroll.md).

Refer: public sector and contract staff of state bodies (IHSS publishes separate rates), self-employed voluntary affiliation, occupational risk (riesgos profesionales) rates by class, employers with arrears (Decreto 40-2026 opened a six-month RAP regularisation window, not read), and employers whose collective agreements already pay annual severance (they may be exempt from the RAP reserve, Decreto 47-2024 art. 5).

Conservative defaults:

| Ambiguity | Default |
| --- | --- |
| Gross salary unknown | Stop |
| 2026 IVM ceiling not yet confirmed | Use L11,903.13 and label it the 2025 ceiling |
| Salary above the ceiling | IVM on the ceiling only; RAP 1.5% plus 1.5% on the excess |
| Salary above three highest minimum wages | RAP reserve 4% on L57,896.16 only |
| IHSS sickness and maternity (EM) rates | Do not compute; ask the employer for its IHSS invoice |

## Rates, bands and thresholds

| Item | Rate or amount | Base and condition | Source |
| --- | --- | --- | --- |
| IHSS IVM, employer (Decreto 48-2024 art. 1) | 3.5% | Salary up to the IVM ceiling | SAR copy of Decreto 48-2024, La Gaceta 36,545: https://www.sar.gob.hn/download/decreto-no-48-2024-no-36545-de-fecha-28-de-mayo-2025-contentivo-ley-para-la-regulacion-de-las-aportaciones-y-cotizaciones-del-instituto-hondureno-social-ihssde-seguridad-social-ihss/?wpdmdl=23132 |
| IHSS IVM, employee (Decreto 48-2024 art. 1) | Two point five per cent ("dos puntos cinco por ciento"; the Gazette PDF has a broken text layer here, read from the page image) | Salary up to the IVM ceiling | same |
| IVM ceiling (techo), 2025 (art. 2) | L11,903.13 a month | Later years set by the IHSS board on an actuarial study; 2026 not confirmed | same |
| EM ceiling (techo), 2025 (art. 2) | L11,903.13 a month | Same rule for later years | same |
| RAP labour reserve fund, employer only (Decreto 47-2024 art. 4) | 4% a month of ordinary salary | Ceiling of three minimum wages at the highest level | SAR copy of Decreto 47-2024, La Gaceta 36,545: https://www.sar.gob.hn/download/decreto-no-47-2024-no-36545-de-fecha-28-de-mayo-2025-contentivo-ley-del-fondo-de-reserva-laboral-de-capitalizacion-individual-administrado-por-el-regimen-de-aportaciones-privadas-rap/?wpdmdl=23131 |
| RAP savings, employee (RAP law art. 43 as reformed) | 1.5% | Salary above the IVM ceiling; retained by the employer | same |
| RAP savings, employer (RAP law art. 43 as reformed) | 1.5% | Same base; 3% in total to the worker's account | same |
| RAP payment | Within 15 calendar days of the retention | Paid to RAP or an authorised collector | same |
| Highest minimum wage 2026 | L19,298.72 a month | So the reserve ceiling is 3 x L19,298.72 = L57,896.16 | Secretaria de Trabajo, Tabla 2026: https://www.trabajo.gob.hn/wp-content/uploads/2026/05/TABLA-SALARIO-MINIMO-2026-.pdf |

## The base

- **IVM:** ordinary monthly salary up to the ceiling; 3.5% employer, 2.5% employee (Decreto 48-2024 art. 1). The decree set the 2024 and 2025 ceilings; from 2026 the IHSS board sets them (art. 2).
- **EM (sickness and maternity):** the 2025 ceiling is in the decree, the rates are in the Ley del Seguro Social and IHSS notices not read in this pass.
- **RAP reserve (Fondo de Reserva Laboral de Capitalizacion Individual):** 4% of ordinary salary up to three highest minimum wages, paid by the employer into the worker's individual account. On termination for any cause the worker receives the balance; for severance the employer tops up if the balance is below 35% of the severance due (art. 6). Employers already paying annual severance under an agreement or special law need not constitute it (art. 5).
- **RAP savings:** 1.5% retained from the worker and 1.5% from the employer, on the salary above the IVM ceiling (art. 43). The RAP board may change the percentages. RAP certifications of debts are enforceable titles. Contributions to RAP are deductible for ISR (SAR Form 102 guide).
- New hires and leavers are notified to RAP within 60 days.
- **13th and 14th month:** whether contributions apply to them was not confirmed (see Not yet confirmed).

## Deadlines and filing

| Obligation | Deadline | Channel |
| --- | --- | --- |
| IHSS contributions (IVM, EM) | Monthly | IHSS employer system (deadline not confirmed) |
| RAP reserve and savings | Within 15 calendar days of the retention | RAP or authorised collectors |
| RAP notice of new hires and leavers | Within 60 days | RAP |

## Penalties and interest

RAP debts certified by RAP's accounting department are enforceable (Decreto 47-2024, art. 43 as reformed). IHSS surcharges and interest were not read in this pass. ISR retention penalties are in honduras-payroll.

## Cross-border points

Foreign employees working in Honduras under a Honduran employment contract are in the IHSS and RAP regimes like nationals; posted workers and totalisation agreements were not confirmed in this pass.

## Two worked examples that recompute

### Example 1: salary of L40,000 a month (2025 ceiling used, labelled)

IVM employee L297.58, employer L416.61 on the L11,903.13 ceiling; RAP savings L421.45 each on the L28,096.87 above the ceiling; RAP reserve L1,600.00 (below the L57,896.16 cap). Employer cost before EM: L2,438.06.

```oa-check
name: HN 2026 IVM and RAP, L40,000 salary
inputs:
  salary: 40000
  ceiling: 11903.13
  reserve_cap: 57896.16
steps:
  - ivm_employee: round(min(salary, ceiling) * 0.025, 2)
  - ivm_employer: round(min(salary, ceiling) * 0.035, 2)
  - rap_savings_each: round(max(salary - ceiling, 0) * 0.015, 2)
  - rap_reserve: round(min(salary, reserve_cap) * 0.04, 2)
  - employer_total: ivm_employer + rap_savings_each + rap_reserve
  - employee_total: ivm_employee + rap_savings_each
expected:
  ivm_employee: 297.58
  ivm_employer: 416.61
  rap_savings_each: 421.45
  rap_reserve: 1600
  employer_total: 2438.06
  employee_total: 719.03
```

### Example 2: salary of L70,000, does the reserve cap bite (decision)

At L70,000 the RAP reserve stops at three highest minimum wages: 4% of L57,896.16 is L2,315.85, against L2,800.00 uncapped, so the cap saves the employer L484.15 a month. The RAP savings have no cap: L871.45 each. The figure that decides it is L57,896.16; below it, the reserve is simply 4% of salary.

```oa-check
name: HN 2026 RAP reserve cap at L70,000
inputs:
  salary: 70000
  ceiling: 11903.13
  reserve_cap: 57896.16
steps:
  - reserve_capped: round(min(salary, reserve_cap) * 0.04, 2)
  - reserve_uncapped: salary * 0.04
  - saving: reserve_uncapped - reserve_capped
  - rap_savings_each: round((salary - ceiling) * 0.015, 2)
expected:
  reserve_capped: 2315.85
  reserve_uncapped: 2800
  saving: 484.15
  rap_savings_each: 871.45
```

## Ask the client first

1. Gross ordinary monthly salary of each employee, and any variable pay.
2. Sector and size, public or private, and number of employees.
3. The IHSS invoice or notice for 2026 (ceiling and EM rates in force for the employer).
4. Whether a collective agreement already pays annual severance (RAP reserve art. 5).
5. RAP affiliation of each worker and any arrears.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for Decreto 48-2024, Ley para la Regulacion de las Aportaciones y Cotizaciones del IHSS, arts. 1 (IVM rates) and 2 (2024 and 2025 ceilings, later ceilings set by the board) | https://www.sar.gob.hn/download/decreto-no-48-2024-no-36545-de-fecha-28-de-mayo-2025-contentivo-ley-para-la-regulacion-de-las-aportaciones-y-cotizaciones-del-instituto-hondureno-social-ihssde-seguridad-social-ihss/?wpdmdl=23132 | 2026-11-14 |
| Read for Decreto 47-2024, Ley del Fondo de Reserva Laboral (RAP), arts. 4 to 6 and reformed art. 43 of the RAP law | https://www.sar.gob.hn/download/decreto-no-47-2024-no-36545-de-fecha-28-de-mayo-2025-contentivo-ley-del-fondo-de-reserva-laboral-de-capitalizacion-individual-administrado-por-el-regimen-de-aportaciones-privadas-rap/?wpdmdl=23131 | 2026-11-14 |
| Read for the 2026 minimum wage table, highest band | https://www.trabajo.gob.hn/wp-content/uploads/2026/05/TABLA-SALARIO-MINIMO-2026-.pdf | 2026-11-14 |
| Read for the IHSS transparency page (IAIP), list of 2026 notices on rates and ceilings; the documents themselves could not be opened | https://portalunico.iaip.gob.hn/356/83/ | 2026-11-14 |
| Read for the IHSS concepts page, definition of the contribution ceiling | https://www.ihss.hn/conceptos-importante/ | 2026-11-14 |

Not yet confirmed: the IVM and EM ceilings for 2026 (IHSS lists a notice "Tasas y Techos de cotizacion vigentes a 2026" that could not be opened); the EM rates (the old file said 5% employer and 2.5% employee, from secondary sources); the state IVM share; occupational risk rates; the INFOP training levy (the old file said 1% of payroll for employers with 5 or more workers; no official INFOP page was opened); IHSS payment deadline and surcharges; whether the 13th and 14th month bear IHSS and RAP; totalisation agreements.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `honduras-social-contributions` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/honduras-social-contributions. If neither is available, confirm every figure against the official source pages cited above before relying on it.
