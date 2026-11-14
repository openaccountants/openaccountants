---
name: guatemala-payroll
description: >
  Use this Guatemala reference for running payroll in tax year 2026, the
  employer's ISR withholding on rentas del trabajo, the statutory bonuses and
  the 2026 minimum wages. Match requests such as Guatemala payroll, nómina
  Guatemala, retención ISR asalariados, proyección de renta, Retenciones WEB,
  SAT-1331, constancia de retención, Q51,024 deducción 2026, aguinaldo, Bono 14,
  bonificación incentivo Q250, salario mínimo 2026, horas extra, vacaciones,
  indemnización, gross to net Guatemala, non-resident salary 15%, and employer
  cost Guatemala. It gives the projection method of Decreto 10-2012 articles 75
  to 80, the 2026 deduction, the Acuerdo Gubernativo 256-2025 wages, the
  Código de Trabajo hours and premiums, and links IGSS, INTECAP and IRTRA to
  guatemala-social-contributions. This Tier 2 draft supports source checking
  and reviewer questions; it does not authorise filing, payment or a tax
  position.
version: 1.0
jurisdiction: GT
tax_year: 2026
tax_year_notes: "Calendar year 2026. Withholding rules from Decreto 10-2012 (TSE consolidated copy through web.archive.org); 2026 personal deduction Q51,024 from SAT; minimum wages from Acuerdo Gubernativo 256-2025 on the MINTRAB site, in force 1 January 2026."
last_updated: 2026-11-14
depends_on:
  - payroll-workflow-base
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Guatemala Payroll v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Employers in Guatemala paying employees in 2026, in quetzales (GTQ, Q). Every employer that pays residents for work in relación de dependencia must withhold ISR (Ley de Actualización Tributaria, Decreto 10-2012, LAT art 75). Public bodies withhold through the official who pays salaries. No withholding applies to diplomats and staff of foreign governments and international bodies paid for their official functions; resident employees of those missions still file their own return (art 75).

| Item | 2026 position |
| --- | --- |
| Tax year | Calendar year (LAT art 74) |
| Pay frequency | Monthly is the base; a quincenal pay run splits the same monthly figures |
| Income tax authority | SAT (Superintendencia de Administración Tributaria), Retenciones WEB, component Rentas del Trabajo |
| Social security | IGSS; rates, base, floor, registration and planilla are owned by `guatemala-social-contributions` |
| Labour authority | Ministerio de Trabajo y Previsión Social (MINTRAB) |

### What this file is

The employer's job each month: gross pay, statutory bonuses, ISR withholding, net pay, and the employer's own cost, plus the year-end reconciliation. The employee's own annual position and the self-employed regimes are in `guatemala-income-tax`.

### Refusals and boundaries

| Scenario | Why it is out of scope |
| --- | --- |
| Cross-border, posted workers, social security totalisation | Treaty or IGSS determination; see `cross-border-payroll-coordination` |
| Treaty relief, tax equalisation, residence tie-breaks | Refer |
| Benefits in kind, company cars, share plans | No valuation rule read for this file |
| Severance tax beyond the art 70 exemption of indemnización por tiempo servido | Refer |
| Self-employed or professional income | `guatemala-income-tax` |
| Penalty quantification | The Código Tributario text was not opened; refer |

### Conservative defaults

| Field | Default | Why |
| --- | --- | --- |
| Residence | Resident (scale with deductions) | Apply the 15% non-resident rate only when non-residence is shown (LAT arts 6 and 104) |
| IVA planilla, donations, life insurance | Not in the monthly projection | SAT FAQ: deductible at the end of the period if the worker proves them |
| Aguinaldo and Bono 14 | Out of the projection up to one monthly ordinary salary each; any excess in | LAT art 70.5 and 70.6 |
| Bonificación incentivo Q250 | Always paid on top of salary; ISR treatment flagged | Decreto 37-2001 per MINTRAB; AG 256-2025 art 8 e |
| IGSS figures | Take from `guatemala-social-contributions` | One figure, one home |
| Pay below minimum wage | Stop and flag | AG 256-2025 art 8 f |

## Rates, bands and thresholds

| Item | 2026 figure | Conditions | Source |
| --- | --- | --- | --- |
| ISR scale, first band | 5% of annual renta imponible up to Q300,000.00 | Residents, employment income | [LAT art 73](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| ISR scale, second band | Q15,000.00 plus 7% of the excess over Q300,000.00 | Same | same |
| Personal expenses deduction in the projection, 2026 | Q48,000.00 + Q3,024.00 = Q51,024.00 | For 2026; SAT adjusted the Rentas del Trabajo WEB tool | [SAT FAQ, contribuyentes especiales](https://portal.sat.gob.gt/portal/preguntas-frecuentes/contribuyentes-especiales/) |
| Aguinaldo exempt from ISR | Up to 100% of the monthly ordinary salary | Excess taxable | [LAT art 70.5](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| Bono 14 exempt from ISR | Up to 100% of the monthly ordinary salary | Excess taxable | same |
| Non-resident employment income | 15% definitive on gross, no deductions | Sueldos, salarios, dietas, comisiones, bonificaciones | [LAT art 104.3 a)](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| IGSS cuota laboral and cuota patronal | 4.83% worker, 10.67% employer, 15.5% together | Base, floor and programme split in `guatemala-social-contributions` | [IGSS notice, 3 October 2022](https://www.igssgt.org/noticias/2022/10/03/el-igss-fija-cuota-minima-de-contribuciones-a-la-seguridad-social/) |
| Bonificación incentivo | Q250.00 a month, paid with the monthly salary | All private-sector workers (Decreto 37-2001) | [MINTRAB, Guía para el Trabajador](https://www.mintrabajo.gob.gt/wp-content/uploads/2026/05/Guia-para-el-Trabajador.pdf) |
| Aguinaldo | 100% of the monthly ordinary salary per year of continuous service, or the proportional part | 50% in the first half of December, 50% in the second half of January | [Decreto 76-78 arts 1 and 2](https://mintrabajo.gob.gt/wp-content/uploads/2026/06/Ley-Reguladora-del-Aguinaldo-Decreto-76-78.pdf) |
| Bono 14 | 100% of the monthly ordinary salary, on the average for the year ending in June | Paid in the first half of July; proportional on leaving | [Decreto 42-92 arts 2 and 3](https://mintrabajo.gob.gt/wp-content/uploads/2026/06/Ley-de-Bonificacion-Anual-para-Trabajadores-del-Sector-Privado-y-Publico-Decreto-42-92.pdf) |
| Minimum wage CE1, agricultural | Q124.64 a day, Q3,791.20 a month | CE1 = Department of Guatemala, from 1 January 2026 | [AG 256-2025 art 2](https://mintrabajo.gob.gt/wp-content/uploads/2026/06/Acuerdo-Gubernativo-Numero-256-2025-Salario-Minino.pdf) |
| Minimum wage CE1, non-agricultural | Q131.58 a day, Q4,002.28 a month | Same | [AG 256-2025 art 3](https://mintrabajo.gob.gt/wp-content/uploads/2026/06/Acuerdo-Gubernativo-Numero-256-2025-Salario-Minino.pdf) |
| Minimum wage CE1, export and maquila | Q112.10 a day, Q3,409.73 a month | Same | [AG 256-2025 art 4](https://mintrabajo.gob.gt/wp-content/uploads/2026/06/Acuerdo-Gubernativo-Numero-256-2025-Salario-Minino.pdf) |
| Minimum wage CE2, agricultural | Q119.21 a day, Q3,625.89 a month | CE2 = all other departments | [AG 256-2025 art 5](https://mintrabajo.gob.gt/wp-content/uploads/2026/06/Acuerdo-Gubernativo-Numero-256-2025-Salario-Minino.pdf) |
| Minimum wage CE2, non-agricultural | Q125.49 a day, Q3,816.90 a month | Same | [AG 256-2025 art 6](https://mintrabajo.gob.gt/wp-content/uploads/2026/06/Acuerdo-Gubernativo-Numero-256-2025-Salario-Minino.pdf) |
| Minimum wage CE2, export and maquila | Q105.90 a day, Q3,221.10 a month | Same | [AG 256-2025 art 7](https://mintrabajo.gob.gt/wp-content/uploads/2026/06/Acuerdo-Gubernativo-Numero-256-2025-Salario-Minino.pdf) |
| Ordinary day shift | At most 8 hours a day and 48 a week | 06:00 to 18:00 | [Código de Trabajo art 116](https://mintrabajo.gob.gt/wp-content/uploads/2026/06/Codigo-de-Trabajo.pdf) |
| Ordinary night shift | At most 6 hours a day and 36 a week | 18:00 to 06:00 | same |
| Mixed shift | At most 7 hours a day and 42 a week; 4 or more night hours make it a night shift | Art 117 | [Código de Trabajo art 117](https://mintrabajo.gob.gt/wp-content/uploads/2026/06/Codigo-de-Trabajo.pdf) |
| Overtime premium | At least 50% more than the ordinary rate | Art 121 | [Código de Trabajo art 121](https://mintrabajo.gob.gt/wp-content/uploads/2026/06/Codigo-de-Trabajo.pdf) |
| Paid holidays | At least 15 business days after each year of continuous work | 150 days worked in the year for irregular contracts (art 131) | [Código de Trabajo art 130](https://mintrabajo.gob.gt/wp-content/uploads/2026/06/Codigo-de-Trabajo.pdf) |
| Indemnización por tiempo servido | One month's salary per year of continuous service, proportional below a year | Unjustified dismissal of an indefinite contract after probation | [Código de Trabajo art 82](https://mintrabajo.gob.gt/wp-content/uploads/2026/06/Codigo-de-Trabajo.pdf) |

The minimum wage applies where the workplace is; if none can be fixed, where the work is habitually done, then where the worker lives (AG 256-2025 art 8 c). The bonificación incentivo is paid on top of the minimum wage and may not be split (art 8 e). The 2025 wages (AG 264-2024) are not restated: use them only for 2025 pay periods, from that acuerdo.

## The base

### Monthly ISR withholding for a resident (LAT art 76)

1. At the start of the year, or when the job starts, project the worker's renta neta for the year: ordinary salary, commissions, bonificaciones and any aguinaldo or Bono 14 above one monthly ordinary salary. Exempt income (art 70) stays out.
2. If the worker had another employer earlier in the same year, add that income from the constancia de retención the worker hands over.
3. Deduct the personal expenses amount (Q51,024 for 2026) and the estimated IGSS cuota laboral for the year.
4. Apply the art 73 scale; withhold one twelfth each month. A projection made after the year started covers the months left.
5. When the expected pay changes, re-project for the remaining months without waiting for a declaration from the worker.
6. Donations and life insurance are not in the projection; the worker proves them at the end of the period (SAT FAQ). The IVA deduction up to Q12,000 comes from the worker's planilla del IVA, filed in the first 10 business days of January, which the employer reconciles (art 72 a).

The Q3,024 for 2026 arrived mid-year through Decreto 13-2026 (art 4 transitorio, in force eight days after publication per DCA, 18 May 2026). Projections made earlier used Q48,000; this draft reads art 76 as requiring a re-projection for the remaining months.

A worker with more than one employer tells the employer paying the most, which withholds on the total; the worker gives that employer a sworn statement of the other pay and copies it to the others (art 77).

### Year end and leaving (LAT art 79)

The employer works out the final tax with the planilla del IVA and the donation and insurance proofs. Over-withheld tax is refunded to the worker and reported to SAT within the first two months of the year; the employer recovers it by reducing its following remittances. When a contract ends before December, the employer settles the final tax at that point and refunds or withholds the difference.

### Gross to net and employer cost

| Line | Treatment |
| --- | --- |
| Ordinary salary | Taxable; IGSS base per `guatemala-social-contributions` |
| Overtime | Taxable; at least 1.5 times the ordinary hourly rate (Código de Trabajo art 121) |
| Bonificación incentivo Q250 | Paid on top; ISR and IGSS treatment per the Not yet confirmed line and the social contributions file |
| Aguinaldo, Bono 14 | Exempt up to one monthly ordinary salary each; the excess taxable |
| ISR withheld | One twelfth of the projected annual tax |
| IGSS cuota laboral | Withheld from the worker; deductible in the projection |
| Employer cost | Salary, Q250, IGSS cuota patronal, INTECAP and IRTRA (rates in `guatemala-social-contributions`), aguinaldo and Bono 14 accruals of one twelfth of a month's salary each, vacation accrual |

### Bank-line patterns

| Bank text | Classification |
| --- | --- |
| SALARIO, SUELDO, NOMINA, PAGO NOMINA, PLANILLA, PAYROLL | Net salary |
| ANTICIPO, ADELANTO DE SUELDO | Salary advance, not final pay |
| BONIFICACION INCENTIVO, BONO INCENTIVO | The Q250 monthly bonificación |
| AGUINALDO | Aguinaldo, December and January |
| BONO 14, BONIFICACION ANUAL | Bono 14, first half of July |
| DEVOLUCION ISR, REINTEGRO ISR | ISR refund at year end (art 79), not income |
| SAT, RETENCION ISR, ISR PLANILLA | ISR remitted with SAT-1331 |
| IGSS, CUOTA PATRONAL, CUOTA LABORAL | IGSS remittance (employer and withheld worker share) |
| INTECAP, IRTRA | Levies collected through the IGSS planilla |

### Reviewer catalogue

| Ref | Issue | What the reviewer resolves |
| --- | --- | --- |
| T2-1 | Re-projection after Decreto 13-2026 | Whether SAT expects Q48,000 for months before the decree and Q51,024 after, or a full-year Q51,024 at the year-end settlement |
| T2-2 | ISR on the Q250 bonificación incentivo | Whether Decreto 78-89 or 37-2001 exempts it from ISR |
| T2-3 | IGSS for non-resident staff | Whether IGSS applies alongside the 15% |
| T2-4 | Benefits in kind, per diems, severance beyond art 70 | Valuation and treatment |
| T2-5 | Night, Sunday and holiday premiums beyond art 121 | From the Código de Trabajo and any pacto colectivo |

## Deadlines and filing

| Obligation | Form or tool | When | Source |
| --- | --- | --- | --- |
| Declare and pay ISR withheld from employees, with the annex per worker (name, NIT, concept, pay, tax) | SAT-1331, Retenciones WEB | First 10 business days of the month after the pay month, even if nothing was withheld | LAT art 80; SAT FAQ cumplimiento tributario |
| Constancia de retención to the worker | Retenciones WEB | Within 10 days after the payment | LAT art 78 |
| Year-end refunds of over-withheld ISR, reported to SAT | Retenciones WEB | First two months of the year | LAT art 79 |
| Worker's planilla del IVA | Planilla IVA-FEL (worker files) | First 10 business days of January | LAT art 72 a) |
| Non-resident salary withholding | SAT-1352 | First 10 business days of the month after payment | LAT art 105; SAT FAQ |
| Aguinaldo | Payroll | 50% first half of December, 50% second half of January | Decreto 76-78 art 2 |
| Bono 14 | Payroll | First half of July | Decreto 42-92 art 3 |
| IGSS planilla, INTECAP, IRTRA | IGSS planilla electrónica | See `guatemala-social-contributions` | |

The aguinaldo payment must be recorded in writing; without the worker's signature or fingerprint on it, the labour authorities presume it was not paid (Decreto 76-78 art 7). It may not be paid in kind (art 8).

## Penalties and interest

- Late or missing ISR withholding: the payer stays jointly liable and the SAT-1331 is still due (LAT arts 80 and 106 for non-residents). The Código Tributario amounts were not opened in this pass.
- Interest for tax purposes under Código Tributario art 58: 12.88% for the first half of 2026 and 12.97% for the second half ([Banguat](https://banguat.gob.gt/page/tasas-de-interes-para-efectos-tributarios-determinada-por-la-junta-monetaria)).
- Paying below the minimum wage is sanctioned under Código de Trabajo art 272 a), and the shortfall stays owed (AG 256-2025 art 8 f).
- Legacy's penalty table (mora 0.005 a day, omisión 100%, Q50 a day to Q1,000, 85% and 50% reductions) came from a newspaper summary; it is not restated (see Sources).

## Cross-border points

- A non-resident employee is taxed at 15% definitive on gross pay, with no personal deduction or scale (LAT art 104.3 a); the payer withholds and declares it on SAT-1352 (art 105).
- Residence follows LAT art 6 (more than 183 days, or centre of economic interests). Test it each year.
- Posted workers, totalisation and treaties: refer (see boundaries).

## Two worked examples that recompute

### Worked case 1: resident, Q10,000 a month, 2026 projection

A non-agricultural worker in CE1 earns Q10,000 a month for all of 2026 (above the Q4,002.28 minimum). Aguinaldo and Bono 14 are one month each, so exempt. IGSS 4.83% per the social contributions file. Projection with the 2026 deduction of Q51,024.

```oa-check
name: Resident Q10,000 a month, 2026 withholding
inputs:
  monthly_salary: 10000
  igss_rate: 0.0483
  personal_deduction: 51024
steps:
  - projected_income: monthly_salary * 12
  - igss_year: projected_income * igss_rate
  - renta_imponible: max(projected_income - personal_deduction - igss_year, 0)
  - isr_year: min(renta_imponible, 300000) * 0.05 + max(renta_imponible - 300000, 0) * 0.07
  - isr_month: round(isr_year / 12, 2)
  - igss_month: monthly_salary * igss_rate
  - net_salary_month: monthly_salary - igss_month - isr_month
expected:
  igss_year: 5796
  renta_imponible: 63180
  isr_year: 3159
  isr_month: 263.25
  igss_month: 483
  net_salary_month: 9253.75
```

The worker also receives the Q250 bonificación incentivo. A minimum-wage worker on Q4,002.28 has projected income of Q48,027.36, below the Q51,024 deduction, so no ISR is withheld.

### Worked case 2: decision, resident or non-resident at Q50,000 a month

A foreign manager is paid Q50,000 a month for the year. If resident under art 6 (more than 183 days or centre of interests), the scale applies; if not, 15% of gross.

```oa-check
name: Resident scale or 15% non-resident, Q50,000 a month
inputs:
  monthly_pay: 50000
  igss_rate: 0.0483
  personal_deduction: 51024
  nonresident_rate: 0.15
steps:
  - annual_pay: monthly_pay * 12
  - igss_year: annual_pay * igss_rate
  - renta_imponible: max(annual_pay - personal_deduction - igss_year, 0)
  - resident_isr: min(renta_imponible, 300000) * 0.05 + max(renta_imponible - 300000, 0) * 0.07
  - resident_month: round(resident_isr / 12, 2)
  - nonresident_isr: annual_pay * nonresident_rate
  - difference: nonresident_isr - resident_isr
expected:
  igss_year: 28980
  renta_imponible: 519996
  resident_isr: 30399.72
  resident_month: 2533.31
  nonresident_isr: 90000
  difference: 59600.28
```

The status decides a Q59,600.28 difference, so the day count and the centre-of-interests facts must be on file before the first pay run. Whether IGSS applies to the non-resident is T2-3.

## Ask the client first

1. Monthly base salary in GTQ, and the pay frequency.
2. Is the worker resident in Guatemala under LAT art 6?
3. Workplace department (CE1 or CE2) and activity (agricultural, non-agricultural, export or maquila), to check the minimum wage.
4. Start date in 2026, and any earlier employer this year with its constancia de retención.
5. Aguinaldo and Bono 14 amounts paid above one monthly ordinary salary, and any overtime.
6. For the year end: the worker's planilla del IVA, donations and life insurance proofs.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Decreto 10-2012, Ley de Actualización Tributaria, TSE consolidated copy through web.archive.org (capture 29 October 2026). Read for arts 6, 68 to 81, 104 to 106 | https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf | 2026-11-14 |
| SAT, preguntas frecuentes, contribuyentes especiales (copy taken 14 November 2026). Read for the 2026 deduction Q51,024, the adjusted Rentas del Trabajo WEB tool, the projection excluding donations and insurance, and SAT-1331 for employment withholding | https://portal.sat.gob.gt/portal/preguntas-frecuentes/contribuyentes-especiales/ | 2026-11-14 |
| SAT, preguntas frecuentes, cumplimiento tributario (copy taken 14 November 2026). Read for SAT-1331 and SAT-1352 deadlines and users | https://portal.sat.gob.gt/portal/preguntas-frecuentes/cumplimiento-tributario/ | 2026-11-14 |
| Diario de Centro América, 18 May 2026, on Decreto 13-2026. Read for the Q3,024 for 2026, its entry into force eight days after publication, and the 2027 rule | https://dca.gob.gt/noticias-guatemala-diario-centro-america/oficializan-que-salario-minimo-esta-exento-de-isr/ | 2026-11-14 |
| Acuerdo Gubernativo 256-2025, salarios mínimos 2026, MINTRAB copy (scanned; read by OCR). Read for arts 1 to 8 | https://mintrabajo.gob.gt/wp-content/uploads/2026/06/Acuerdo-Gubernativo-Numero-256-2025-Salario-Minino.pdf | 2026-11-14 |
| Código de Trabajo, MINTRAB copy. Read for arts 82, 116 to 118, 121, 122, 126, 127, 130, 131 | https://mintrabajo.gob.gt/wp-content/uploads/2026/06/Codigo-de-Trabajo.pdf | 2026-11-14 |
| Decreto 76-78, Ley Reguladora del Aguinaldo, MINTRAB copy, read in full | https://mintrabajo.gob.gt/wp-content/uploads/2026/06/Ley-Reguladora-del-Aguinaldo-Decreto-76-78.pdf | 2026-11-14 |
| Decreto 42-92, Ley de Bonificación Anual (Bono 14), MINTRAB copy, read in full | https://mintrabajo.gob.gt/wp-content/uploads/2026/06/Ley-de-Bonificacion-Anual-para-Trabajadores-del-Sector-Privado-y-Publico-Decreto-42-92.pdf | 2026-11-14 |
| MINTRAB, Guía para el Trabajador (May 2026). Read for the Q250 bonificación incentivo under Decreto 37-2001 and the overtime example | https://www.mintrabajo.gob.gt/wp-content/uploads/2026/05/Guia-para-el-Trabajador.pdf | 2026-11-14 |
| IGSS notice of 3 October 2022 on the cuota mínima. Read for 4.83% and 10.67%, total 15.5% | https://www.igssgt.org/noticias/2022/10/03/el-igss-fija-cuota-minima-de-contribuciones-a-la-seguridad-social/ | 2026-11-14 |
| Banco de Guatemala, tasas de interés para efectos tributarios. Read for the 2026 rates | https://banguat.gob.gt/page/tasas-de-interes-para-efectos-tributarios-determinada-por-la-junta-monetaria | 2026-11-14 |

Not yet confirmed: the text of Decreto 13-2026 and how SAT wants the 2026 projection split before and after it took effect; whether the Q250 bonificación incentivo is subject to ISR (Decretos 78-89 and 37-2001 not opened; LAT art 68 lists bonificaciones as employment income); the Código Tributario (Decreto 6-91) penalty amounts; the monthly figure in AG 256-2025 differs slightly from the daily rate times 30.4167 (Q131.58 x 30.4167 = Q4,002.23 against the stated Q4,002.28), and this file uses the stated monthly figures; IGSS for non-resident staff; the 2025 minimum wages of AG 264-2024, not opened; night, Sunday and holiday premiums beyond art 121; treaties.

## Changelog

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-11-14 | Full rewrite to the standard for 2026: official sources only; 2026 deduction Q51,024 applied; IVA planilla, donations and insurance moved out of the monthly projection (art 76); aguinaldo and Bono 14 exempt up to one month (legacy said taxable); aguinaldo second half paid in the second half of January (legacy said by 15 January); CE2 export wage Q3,221.10 from the acuerdo itself; IGSS, INTECAP and IRTRA linked to the social contributions file |
| 0.1 | 2026-07-13 | Earlier draft from secondary sources |
