---
name: guatemala-income-tax
description: "Use this Guatemala reference for Impuesto Sobre la Renta (ISR) of individuals in tax year 2026, employees in relación de dependencia and self-employed people with rentas de actividades lucrativas. Match requests such as how much ISR do I pay, renta del trabajo, régimen opcional simplificado, régimen sobre utilidades, pequeño contribuyente, deducción personal Q48,000, Q3,024 deducción extraordinaria, planilla del IVA, SAT-1431, SAT-1311, SAT-1411, self-employed tax Guatemala, ISR empleados and freelancer Guatemala. It gives the article 73 employment scale (5% and 7%), the article 44 monthly scale for the simplified regime, the 25% profit regime, the 10% and 5% capital rates, the 2026 deductions, forms and deadlines from Decreto 10-2012 and SAT. This Tier 2 draft supports source checking and reviewer questions; it does not authorise filing, payment or a tax position."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/guatemala-income-tax"
  jurisdiction: "GT"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Guatemala Income Tax (ISR) for Individuals v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Individuals with Guatemalan-source income in calendar year 2026, in quetzales (GTQ, Q). The tax is ISR under Libro I of the Ley de Actualización Tributaria, Decreto 10-2012 (LAT), administered by the Superintendencia de Administración Tributaria (SAT).

| Item | 2026 position |
| --- | --- |
| Tax year | Calendar year, 1 January to 31 December (LAT arts 37 and 74) |
| Basis | Rentas de fuente guatemalteca (LAT arts 3 and 4). Foreign-source income is outside this file |
| Residence | More than 183 days in the calendar year, or centre of economic interests in Guatemala unless a foreign tax residence certificate is shown (LAT art 6) |
| Categories | Rentas de actividades lucrativas, rentas del trabajo, rentas de capital (LAT art 2). Each has its own base and rate |
| Authority and portal | SAT, Agencia Virtual and Declaraguate |

### What this file covers

- Employees resident in Guatemala (rentas del trabajo en relación de dependencia, LAT arts 68 to 82): the annual scale, deductions and the cases where the employee files SAT-1431. The employer's monthly withholding is in `guatemala-payroll`.
- Self-employed individuals and professionals (rentas de actividades lucrativas): the choice between the Régimen Opcional Simplificado Sobre Ingresos (5% and 7% on monthly income) and the Régimen Sobre las Utilidades (25% on profit).
- Rentas de capital and capital gains of individuals (10%) and dividends received (5%), at the level of rate and form only.
- The Régimen de Pequeño Contribuyente is an IVA regime that replaces ISR for those in it (Ley del IVA art 49). Its limit and rate are in `guatemala-iva`.

### Refusals and boundaries

- **R-GT-1, income type unknown.** Stop until you know whether the income is employment, self-employment, capital, or a mix. Each category has its own base and rate (LAT art 2).
- **R-GT-2, companies.** Sociedades and other entities: use `gt-corporate-income-tax`.
- **R-GT-3, foreign-source income or non-residents.** Guatemala taxes Guatemalan-source income only. Non-residents are taxed by withholding under LAT arts 97 to 107; see `gt-corporate-income-tax` for the rates and refer the person's own position to a reviewer.
- **R-GT-4, capital income computations.** Rate and form are given below; computing a capital gain base (LAT art 89) on property or shares goes to a reviewer.
- **R-GT-5, arrears and SAT enforcement.** Mora, multas and interest under the Código Tributario apply; the penalty figures are not confirmed here. Refer.
- **R-GT-6, IVA returns.** Use `guatemala-iva`.

### Required inputs

1. Income type and, for self-employed people, the ISR regime on the RTU (the SAT registration record).
2. Employment: gross ordinary pay, aguinaldo and Bono 14 paid, IGSS cuota laboral withheld, constancias de retención from every employer in the year.
3. Employment: the IVA paid on personal purchases listed in the planilla del IVA, donations with receipts, life insurance premiums.
4. Self-employed: monthly invoiced income without IVA, constancias de retención received, and, in the profit regime, the deductible costs with their documents.
5. Rentas de capital and dividends received, with any withholding.
6. Twelve months of bank statements.

### Conservative defaults

| Ambiguity | Default |
| --- | --- |
| Employment or self-employment unclear | Stop (R-GT-1) |
| Self-employed regime unknown | Ask; read the RTU constancia. Do not assume either regime |
| Planilla del IVA filed? | IVA deduction Q0 until the planilla is confirmed |
| Business-use share of a mixed cost (car, phone, home) | 0% until a log or reasonable basis is shown |
| Expense category unclear (profit regime) | Not deductible until documented under LAT arts 21 and 22 |
| Aguinaldo or Bono 14 above one month's ordinary pay | The excess is taxable |
| Bonificación incentivo (Q250 monthly) | Flag: its ISR treatment is not confirmed (see Sources) |

## Rates, bands and thresholds

| Item | 2026 figure | Conditions | Source |
| --- | --- | --- | --- |
| Employment income scale, first band | 5% of renta imponible from Q0.01 to Q300,000.00 | Annual, residents in relación de dependencia | [LAT art 73](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| Employment income scale, second band | Q15,000.00 plus 7% of the excess over Q300,000.00 | Same | same |
| Personal expenses deduction, 2026 | Q48,000.00 + Q3,024.00 = Q51,024.00 without proof | Employees; for the year 2026 | [SAT FAQ, contribuyentes especiales](https://portal.sat.gob.gt/portal/preguntas-frecuentes/contribuyentes-especiales/) |
| IVA paid on personal purchases | Up to Q12,000.00, proved by the planilla del IVA filed in the first 10 business days of January | Employees | [LAT art 72 a)](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| Donations to non-profits, churches, parties | Up to 5% of renta bruta | Employees; donee legally registered with fiscal solvency. Donations to the State, universities, cultural or scientific bodies are not capped in art 72 b) | same |
| Aguinaldo exempt | Up to 100% of the monthly ordinary salary | Employees | [LAT art 70.5](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| Bono 14 exempt | Up to 100% of the monthly ordinary salary | Employees | [LAT art 70.6](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| Simplified regime, first band | 5% of monthly renta imponible from Q0.01 to Q30,000.00 | Régimen Opcional Simplificado; renta imponible = renta bruta less exempt income, IVA excluded | [LAT arts 43 and 44](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| Simplified regime, second band | Q1,500.00 plus 7% of the excess over Q30,000.00 | Same, monthly | same |
| Simplified regime, no withholding below | Q2,500.00 per purchase, IVA excluded | Withholding agents need not withhold under this amount | [LAT art 48](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| Profit regime rate | 25% of renta imponible | Régimen Sobre las Utilidades de Actividades Lucrativas | [LAT art 36](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| Profit regime estimated quarterly base | 8% of quarterly renta bruta, if that option is chosen | Alternative is partial closings each quarter | [LAT art 38](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| Rentas de capital and capital gains | 10% | Mobiliarias, inmobiliarias and ganancias de capital | [LAT art 92](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| Dividends, ganancias and utilidades distributed | 5% | Whatever their name or booking | [LAT art 93](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| Residence day count | More than 183 days in the calendar year | Or centre of economic interests | [LAT art 6](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |

From 1 January 2027 the personal deduction becomes 12 monthly non-agricultural minimum wages including the bonificación incentivo, at the highest circunscripción figure; SAT publishes the value within 5 business days of the minimum wage publication ([DCA on Decreto 13-2026](https://dca.gob.gt/noticias-guatemala-diario-centro-america/oficializan-que-salario-minimo-esta-exento-de-isr/); [SAT FAQ](https://portal.sat.gob.gt/portal/preguntas-frecuentes/contribuyentes-especiales/)). It does not apply to 2026.

## The base

### Employees (rentas del trabajo)

1. **Renta bruta**: all employment income of the year, taxable and exempt (LAT art 72). Sueldos, bonificaciones, comisiones and aguinaldos are rentas del trabajo (art 68).
2. **Renta neta**: renta bruta less exempt income (art 70): death or incapacity indemnities and pensions under social security or insurance; indemnización por tiempo servido; documented viáticos and representation expenses; aguinaldo and Bono 14 each up to 100% of the monthly ordinary salary; pensions and jubilaciones.
3. **Renta imponible**: renta neta less (art 72): the personal deduction (Q51,024 for 2026), the IVA deduction up to Q12,000 if the planilla del IVA was filed, qualifying donations, IGSS and other social security cuotas, and life insurance premiums covering only the worker's death with no return or surrender value.
4. **Tax**: the art 73 scale. The period is the calendar year (art 74).

The Q12,000 IVA amount is a deduction from income, not a credit against the tax. Legacy subtracted it from the tax: that overstated the relief by up to 95% of Q12,000.

### Self-employed: two regimes (LAT art 14)

| Point | Régimen Opcional Simplificado Sobre Ingresos | Régimen Sobre las Utilidades |
| --- | --- | --- |
| Base | Monthly renta bruta less exempt income; no cost deductions (art 43) | Renta bruta less deductible costs and expenses (arts 20 to 23) |
| Rate | 5% to Q30,000 a month, then Q1,500 + 7% on the excess (art 44) | 25% (art 36) |
| Period | Monthly (art 45) | Annual, 1 January to 31 December (art 37), with quarterly payments (art 38) |
| How paid | By withholding by the payer (art 46); direct payment needs SAT authorisation and the invoice must say so | Quarterly payments, then the annual return |
| Monthly or quarterly form | SAT-1311 in the first 10 business days of the following month, even when everything was withheld (art 49) | SAT-1361 in the month after each quarter; the fourth quarter goes with the annual return |
| Annual form | SAT-1411 informativa in January to March (art 49) | SAT-1411 with payment in January to March (art 39) |
| Impuesto de Solidaridad | Not subject (Decreto 73-2008 art 4 f, as reformed by LAT art 178) | Subject if the gross margin exceeds 4% (SAT, principales impuestos); see `gt-corporate-income-tax` |

Profit regime deductions follow the corporate rules (arts 21 to 23): costs must be useful and necessary, booked, and backed by facturas or the other documents in art 22; withholding must have been made where due; wages must appear on the IGSS planilla. Non-deductible items include costs not from the business, undocumented costs and personal drawings (art 23).

### Bank-line patterns

| Pattern | Treatment |
| --- | --- |
| SALARIO, SUELDO, NOMINA, PLANILLA, employer name | Employment income: employee computation, not self-employment |
| AGUINALDO; BONO 14, BONO CATORCE | Employment income; exempt up to one month's ordinary salary each, the excess taxable |
| BONIFICACION INCENTIVO | Q250 a month; flag its ISR treatment (Not yet confirmed) |
| HONORARIOS, SERVICIOS PROFESIONALES, FACTURA, PAGO or DEPOSITO from a client | Self-employment income: apply the regime; match to FEL invoices and constancias de retención |
| STRIPE, PAYPAL, WISE, PAYONEER, UPWORK, FIVERR payouts | Self-employment income; gross up for platform fees; check source of the income (R-GT-3) |
| ALQUILER RECIBIDO, RENTA RECIBIDA | Renta de capital inmobiliaria, 10% (art 92), SAT-1321 |
| INTERESES | Renta de capital mobiliaria; banks withhold (art 94) |
| DIVIDENDOS | 5% withheld by the paying company (art 93) |
| DEVOLUCION SAT, REINTEGRO ISR | Exclude: a refund, not income |
| ALQUILER OFICINA, CONTADOR, ABOGADO, PAPELERIA, PUBLICIDAD, GOOGLE ADS, META ADS, COMISION BANCARIA | Deductible only in the profit regime, with FEL invoice; nothing is deductible in the simplified regime |
| ENERGUATE, EEGSA, CLARO, TIGO, internet | Profit regime only, business share only |
| IGSS, CUOTA LABORAL | Employee deduction (art 72 c) |
| SEGURO DE VIDA | Employee deduction only for a pure death cover of the worker (art 72 d) |
| RESTAURANTE, SUPERMERCADO, PAIZ, LA TORRE, MULTA, PAGO ISR, RETIRO, CAJERO | Not deductible |
| TRANSFERENCIA PROPIA, PRESTAMO, PAGO IVA | Exclude: own transfer, loan principal or IVA payment |
| ISR TRIMESTRAL, PAGO TRIMESTRAL | Credit against the annual liability (profit regime), not an expense |

Banks commonly seen: Banco Industrial (BI), Banrural, BAC Credomatic, G&T Continental, Banco Promerica. Statements use DD/MM/YYYY and Spanish terms: ABONO or DEPOSITO is a credit, CARGO or RETIRO a debit.

### Reviewer catalogue

- **Regime choice.** The simplified regime taxes turnover; the profit regime taxes profit and brings ISO. Worked case 2 shows the break-even. A change of the quarterly payment option is notified in December and takes effect from the next year (LAT art 38; SAT FAQ).
- **Home office and vehicles (profit regime).** Business share only, with a basis.
- **Planilla del IVA.** Filed in the first 10 business days of January, or the IVA deduction is lost for the year (art 72 a).
- **Aguinaldo and Bono 14 excess.** Confirm the monthly ordinary salary and tax the excess.
- **Donations cap.** Confirm the donee type and recompute the 5% cap.

## Deadlines and filing

| Obligation | Form | When | Source |
| --- | --- | --- | --- |
| Employee annual return, only where no or too little ISR was withheld | SAT-1431 | Within the first 3 months of the following year, with payment (art 81) | SAT FAQ cumplimiento tributario; LAT art 81 |
| Planilla del IVA (employee IVA deduction) | Planilla IVA-FEL | First 10 business days of January | LAT art 72 a) |
| Simplified regime monthly return | SAT-1311 | First 10 business days of the following month | SAT FAQ; LAT art 49 |
| Simplified regime annual informative return | SAT-1411 | 1 January to 31 March | SAT FAQ; LAT art 49 |
| Profit regime quarterly payment | SAT-1361 | Within the month after the quarter; the fourth quarter with the annual return | SAT FAQ; LAT art 38 |
| Profit regime annual return and payment | SAT-1411 | 1 January to 31 March | SAT FAQ; LAT art 39 |
| Rentas de capital and capital gains not withheld | SAT-1321 | First 10 business days of the following month | SAT FAQ; LAT art 95 |

Employees whose employer withheld correctly do not file (art 81). An employee with two employers tells the one paying the most, which projects and withholds on the total (art 77).

## Penalties and interest

The Código Tributario (Decreto 6-91) sets mora, multa por omisión and interés resarcitorio. Its text was not opened in this pass, so legacy's figures are not restated (see Sources). What was confirmed:

- The interest rate for tax purposes set by the Junta Monetaria under Código Tributario art 58 is 12.88% for the first half of 2026 and 12.97% for the second half ([Banguat](https://banguat.gob.gt/page/tasas-de-interes-para-efectos-tributarios-determinada-por-la-junta-monetaria)).
- An employer that does not hand over constancias de retención is reported by the worker to SAT (LAT art 78).
- A late aviso of change of ISR regime is accepted with the sanction of Código Tributario art 94 (SAT FAQ cumplimiento tributario).

## Cross-border points

- Only Guatemalan-source income is taxed (LAT arts 3 and 4). A resident with foreign income: R-GT-3.
- A non-resident employee or professional is not on this file's scale: payers withhold a definitive rate on gross under LAT art 104 (15% for salaries, fees, royalties and technical advice). See `gt-corporate-income-tax` for the full table and `guatemala-payroll` for non-resident staff.
- Residence under art 6 can be displaced by a foreign tax residence certificate for the centre-of-interests test.
- Treaties: none checked in this pass.

## Two worked examples that recompute

### Worked case 1: employee, salary Q8,000 a month, 2026

An employee in Guatemala City earns Q8,000 a month for all of 2026 plus aguinaldo and Bono 14 of one month each (exempt, art 70). IGSS withheld 4.83% of salary (rate owned by `guatemala-social-contributions`). She filed a planilla del IVA showing Q6,000 of IVA paid. No donations or life insurance.

Renta neta Q96,000; less Q51,024 personal deduction, Q4,636.80 IGSS and Q6,000 IVA, renta imponible Q34,339.20; tax at 5% is Q1,716.96. Without the planilla the tax would be Q2,016.96.

```oa-check
name: Employee Q8,000 a month, 2026, IVA planilla Q6,000
inputs:
  monthly_salary: 8000
  igss_rate: 0.0483
  personal_deduction: 51024
  iva_paid_planilla: 6000
  iva_cap: 12000
steps:
  - renta_neta: monthly_salary * 12
  - igss: renta_neta * igss_rate
  - iva_deduction: min(iva_paid_planilla, iva_cap)
  - renta_imponible: max(renta_neta - personal_deduction - igss - iva_deduction, 0)
  - isr: min(renta_imponible, 300000) * 0.05 + max(renta_imponible - 300000, 0) * 0.07
  - isr_without_planilla: min(renta_imponible + iva_deduction, 300000) * 0.05 + max(renta_imponible + iva_deduction - 300000, 0) * 0.07
expected:
  igss: 4636.80
  renta_imponible: 34339.20
  isr: 1716.96
  isr_without_planilla: 2016.96
```

### Worked case 2: decision, simplified or profit regime for a consultant

A consultant invoices Q40,000 a month before IVA, Q480,000 for the year, all Guatemalan clients. Deductible costs with FEL invoices are Q300,000.

- Simplified: each month Q1,500 + 7% x Q10,000 = Q2,200; Q26,400 for the year.
- Profit: 25% x (Q480,000 - Q300,000) = Q45,000, plus ISO (rate not confirmed here).
- The regimes tie when profit x 25% = Q26,400, that is profit Q105,600, or costs of Q374,400 (78% of turnover). Below that cost level the simplified regime is cheaper.

```oa-check
name: Simplified or profit regime, Q40,000 a month
inputs:
  monthly_income: 40000
  annual_costs: 300000
steps:
  - simplified_month: min(monthly_income, 30000) * 0.05 + max(monthly_income - 30000, 0) * 0.07
  - simplified_year: simplified_month * 12
  - annual_income: monthly_income * 12
  - profit_tax: (annual_income - annual_costs) * 0.25
  - breakeven_profit: simplified_year / 0.25
  - breakeven_costs: annual_income - breakeven_profit
  - saving_simplified: profit_tax - simplified_year
expected:
  simplified_month: 2200
  simplified_year: 26400
  profit_tax: 45000
  breakeven_profit: 105600
  breakeven_costs: 374400
  saving_simplified: 18600
```

The monthly bands apply to each month's income, so uneven months give a different simplified figure; recompute month by month. A client in the simplified regime who claims office costs: reject, as that regime allows no cost deductions (art 43).

## Ask the client first

1. Are you an employee, self-employed, or both, and which ISR regime does your RTU show?
2. For employees: did you file the planilla del IVA in January, and how much IVA does it show? Any other employer this year?
3. Did you receive aguinaldo or Bono 14 above one month's ordinary salary?
4. For the self-employed: monthly invoiced income without IVA, and the constancias de retención received?
5. In the profit regime: what deductible costs do you have, with FEL invoices?
6. Any rent, interest, dividends or sale of assets, and any income from abroad?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Decreto 10-2012, Ley de Actualización Tributaria, TSE copy consolidated with Decreto 19-2013 and 14-2013 notes, through web.archive.org (capture 29 October 2026; SAT and Congreso refuse scripted downloads). Read for arts 2 to 6, 14 to 17, 20 to 24, 36 to 49, 68 to 81, 83, 92 to 95, 104, 172 to 178 | https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf | 2026-11-14 |
| SAT, preguntas frecuentes, contribuyentes especiales (copy taken 14 November 2026). Read for the 2026 deduction "(Q48,000.00 + Q3,024.00 = Q51,024.00) ... para el año 2026", the 2027 update rule and the employee deduction list | https://portal.sat.gob.gt/portal/preguntas-frecuentes/contribuyentes-especiales/ | 2026-11-14 |
| SAT, preguntas frecuentes, cumplimiento tributario (copy taken 14 November 2026). Read for forms SAT-1311, 1321, 1361, 1411, 1431, their deadlines, the simplified-regime worked example and the December change of payment option | https://portal.sat.gob.gt/portal/preguntas-frecuentes/cumplimiento-tributario/ | 2026-11-14 |
| SAT, principales impuestos en Guatemala. Read for who pays ISO (profit regime, gross margin above 4%) and the ISR categories | https://portal.sat.gob.gt/portal/principales-impuestos-en-guatemala/ | 2026-11-14 |
| SAT, requisitos, régimen opcional simplificado opción pago directo. Read for the conditions for paying directly instead of by withholding | https://portal.sat.gob.gt/portal/requisitos-tramites-agencias/actualizacion-del-impuesto-sobre-la-renta-regimen-opcional-simplificado-opcion-pago-directo/ | 2026-11-14 |
| Diario de Centro América, 18 May 2026, on the publication of Decreto 13-2026. Read for the Q3,024 extraordinary deduction for 2026 (art 4 transitorio) and the rule from 1 January 2027 | https://dca.gob.gt/noticias-guatemala-diario-centro-america/oficializan-que-salario-minimo-esta-exento-de-isr/ | 2026-11-14 |
| Banco de Guatemala, tasas de interés para efectos tributarios (Código Tributario art 58). Read for the 2026 rates 12.88% and 12.97% | https://banguat.gob.gt/page/tasas-de-interes-para-efectos-tributarios-determinada-por-la-junta-monetaria | 2026-11-14 |

Not yet confirmed: the text of Decreto 13-2026 itself and the exact date its art 4 transitorio took effect (the DCA note says eight days after publication); the Código Tributario (Decreto 6-91) text, so the mora, multa por omisión, late-filing fine and voluntary-reduction figures legacy quoted (0.005 per day, Q150 a month, 100%, 85% and 50%) are left out; the Impuesto de Solidaridad rate and base (Decreto 73-2008 not opened); whether the Q250 bonificación incentivo is exempt from ISR (LAT art 68 lists bonificaciones as rentas del trabajo and art 70 does not exempt it, but Decretos 78-89 and 37-2001 were not opened); whether any article of LAT lets a loss be carried forward; the capital gain base rules beyond the rate; tax treaties; and later reforms of Decreto 10-2012 after the TSE consolidation, other than Decreto 13-2026.

## Changelog

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-11-14 | Full rewrite to the standard for 2026: official sources only, 2026 deduction Q51,024, Q30,000 threshold confirmed in LAT art 44, IVA planilla treated as a deduction from income (legacy took it off the tax), canonical headings, two recomputing cases |
| 0.1 | 2026-07-13 | Earlier draft from secondary sources |

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `guatemala-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/guatemala-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
