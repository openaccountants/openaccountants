---
name: nicaragua-income-tax
description: >
  Use this skill for Nicaragua income tax (Impuesto sobre la Renta, IR) on employment
  income (rentas del trabajo) of residents for tax year 2026. It gives the art. 23 Ley de
  Concertacion Tributaria (Ley 822) scale (exempt to C$100,000 of annual net income, then
  15%, 20%, 25% and 30% with base amounts of C$15,000, C$45,000 and C$82,500), the
  deduction of INSS and savings fund contributions, exempt items (13th month, severance up
  to five months and C$500,000, social security benefits, expense reimbursements), the
  definitive retentions (15% on severance above C$500,000, 25% on board fees, 20% on
  non-residents), the filing rule for two or more employers and the 90-day annual return.
  Trigger phrases include IR rentas del trabajo, tabla progresiva articulo 23, salario
  Nicaragua impuesto, DGI and declaracion anual IR asalariados.
version: "1.0"
jurisdiction: NI
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Nicaragua income tax on employment income (rentas del trabajo), tax year 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Nicaraguan accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Nicaragua. "NI" here is Nicaragua, not Northern Ireland or UK National Insurance.

## Who this applies to

Resident individuals who earn employment income (rentas del trabajo) in Nicaragua in the calendar fiscal period 2026 (1 January to 31 December; employment income cannot use a special period, LCT art. 22). The authority is the Direccion General de Ingresos (DGI); the currency is the cordoba (C$).

Out of scope: business income of individuals (rentas de actividades economicas, see [ni-corporate-income-tax](ni-corporate-income-tax.md) for the 30% rate and the pago minimo definitivo); rents, interest, dividends and gains (15% definitive retention, see the overview); the cuota fija regime for small traders; non-residents beyond the 20% retention. Employer mechanics: [nicaragua-payroll](nicaragua-payroll.md). INSS: [nicaragua-social-contributions](nicaragua-social-contributions.md).

Conservative defaults:

| Ambiguity | Default |
| --- | --- |
| Residence unknown | Stop; non-residents bear 20% definitive retention (art. 24.3) |
| Two employers | The employee must file an annual return if the combined net exceeds C$100,000 |
| Bonus, overtime or vacation pay | Taxable (not listed as exempt) |
| Per diems and reimbursements | Exempt only if they are not disguised pay |

## Rates, bands and thresholds

**Art. 23 LCT progressive scale, annual net employment income (C$).** In force since 1 January 2013 and not changed by Ley 987 of 2019; it applies to 2026.

| From | To | Base amount | Rate on excess | Over | Source |
| --- | --- | --- | --- | --- | --- |
| 0.01 | 100,000.00 | 0 | 0% | 0 | DGI FAQ, Periodo fiscal y tarifa del impuesto: https://www.dgi.gob.ni/FAQ/periodo_fiscal_y_tarifa_del_im.htm |
| 100,000.01 | 200,000.00 | 0 | 15% | 100,000.00 | same |
| 200,000.01 | 350,000.00 | 15,000.00 | 20% | 200,000.00 | same |
| 350,000.01 | 500,000.00 | 45,000.00 | 25% | 350,000.00 | same |
| 500,000.01 | and above | 82,500.00 | 30% | 500,000.00 | same |

**Definitive retentions and other figures.**

| Item | Rate or amount | Condition | Source |
| --- | --- | --- | --- |
| Severance above five months' pay (art. 24.1) | 15% definitive | On the excess over C$500,000 | La Gaceta 41 of 28 Feb 2019, Ley 987 (copy at MEM): https://www.mem.gob.ni/wp-content/uploads/2023/08/2019.02.28-Ley-987-Reforma-a-Ley-822-G-41.pdf |
| Board and council fees, residents (art. 24.2) | 25% definitive | Directors and similar bodies | same |
| Municipal and regional councillors' fees (art. 24.2) | 12.5% definitive | Attendance at sessions | same |
| Employment income of non-residents (art. 24.3) | 20% definitive | No scale | same |
| Retention codes for the same items | 15%, 25%, 12.5%, 20% | DGI retention catalogue codes 31 to 35 | DGI catalogue of retention codes and rates (Aviso 005-01-2024): https://www.dgi.gob.ni/pdfNoticia/3175 |
| Exempt: 13th month (aguinaldo) | Exempt | LCT art. 19 | DGI FAQ, Materia imponible y hecho generador: https://www.dgi.gob.ni/FAQ/materia_imponible_y_hecho_gene.htm |
| Exempt: severance | Up to five months of salary, plus additional severance up to C$500,000 | LCT art. 19.3 | same |
| Annual return, two or more employers | Required when combined income exceeds the exempt amount | Within 90 days after the period ends | DGI FAQ, Obligacion de retener, liquidar, declarar y pagar: https://www.dgi.gob.ni/FAQ/obligacion_de_retener__liquida.htm |

## The base

1. **Gross employment income:** salary, overtime, vacation pay, bonuses and incentives are taxable (LCT arts. 11 and 19; DGI FAQ).
2. **Exempt (art. 19):** the first C$100,000 of net income (built into the scale), the 13th month, severance up to five months of salary and additional severance up to C$500,000 (above that, 15% definitive), benefits in kind under a collective agreement given to all workers, social security subsidies, pensions and retirement pay, and per diems, representation, phone, vehicle and fuel reimbursements that are not disguised pay (art. 19.8).
3. **Deductions:** the employee's INSS contribution and contributions to savings funds (DGI FAQ, art. 21).
4. **Annual net income** = gross less exempt items and deductions; apply the art. 23 scale. The employer projects the year monthly (see the payroll skill).
5. **Filing:** a single-source employee does not file; one with two or more employers whose combined income exceeds the exempt amount, part-year workers and those who want to claim authorised deductions file the annual return within 90 days after 31 December (arts. 21, 28, 29).

## Deadlines and filing

| Obligation | Deadline | Channel |
| --- | --- | --- |
| Employer monthly retention | Monthly declaration of retentions | DGI Ventanilla Electronica Tributaria (VET) |
| Annual employee return (when required) | Within 90 days after 31 December 2026, about 31 March 2027 | VET |
| Employer annual report of retentions | Not confirmed in this pass | DGI |

## Penalties and interest

The Codigo Tributario (Ley 562) lists the sanctions: fines, closure of premises, loss of benefits (art. 124). Fines are in unidades de multa, for example 110 to 130 units for late books (art. 127.4), halved for cuota fija taxpayers. Surcharges for late payment: see Not yet confirmed.

## Cross-border points

Non-residents pay a 20% definitive retention on employment income from Nicaragua (art. 24.3). Payments to tax havens bear 30% (art. 49). Nicaragua's territorial rule taxes income from Nicaraguan sources; no tax treaty was confirmed in this pass.

## Two worked examples that recompute

### Example 1: employee earning C$40,000 a month, 2026

INSS 7% = C$2,800; net C$37,200 a month, C$446,400 a year. Band 350,000 to 500,000: C$45,000 + 25% of C$96,400 = C$69,100 a year, C$5,758.33 a month.

```oa-check
name: NI 2026 rentas del trabajo, C$40,000 a month
inputs:
  monthly_gross: 40000
  inss_rate: 0.07
steps:
  - monthly_net: monthly_gross - monthly_gross * inss_rate
  - annual_net: monthly_net * 12
  - annual_ir: 45000 + (annual_net - 350000) * 0.25
  - monthly_ir: round(annual_ir / 12, 2)
expected:
  monthly_net: 37200
  annual_net: 446400
  annual_ir: 69100
  monthly_ir: 5758.33
```

### Example 2: two part-time jobs, file or not (decision)

Two employers each pay C$60,000 of net income in the year. Each applies the scale alone and retains nothing (each is below C$100,000). Combined, the employee has C$120,000 and must file within 90 days: tax C$3,000. With one job of C$60,000 there is nothing to file or pay.

```oa-check
name: NI 2026 two employers, combined income above C$100,000
inputs:
  job_a: 60000
  job_b: 60000
steps:
  - retained_a: max(job_a - 100000, 0) * 0.15
  - retained_b: max(job_b - 100000, 0) * 0.15
  - combined: job_a + job_b
  - tax_due: (combined - 100000) * 0.15
  - to_pay_with_return: tax_due - retained_a - retained_b
expected:
  retained_a: 0
  retained_b: 0
  combined: 120000
  tax_due: 3000
  to_pay_with_return: 3000
```

## Ask the client first

1. Resident in Nicaragua in 2026?
2. How many employers, and the monthly gross from each?
3. Any severance, board fees, vacation pay or bonuses in the year?
4. INSS and savings fund contributions withheld.
5. Any business, rental or investment income (other skills apply).

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for DGI FAQ, Periodo fiscal y tarifa del impuesto (rentas del trabajo): art. 23 scale, period, 90-day return, monthly projection method | https://www.dgi.gob.ni/FAQ/periodo_fiscal_y_tarifa_del_im.htm | 2026-11-14 |
| Read for DGI FAQ, Materia imponible y hecho generador: art. 19 exemptions, taxable bonuses and vacations | https://www.dgi.gob.ni/FAQ/materia_imponible_y_hecho_gene.htm | 2026-11-14 |
| Read for DGI FAQ, Obligacion de retener, liquidar, declarar y pagar: filing with two or more employers, arts. 21, 28, 29 | https://www.dgi.gob.ni/FAQ/obligacion_de_retener__liquida.htm | 2026-11-14 |
| Read for Ley 987 (La Gaceta 41, 28 Feb 2019), reformed arts. 24, 49 and the list of reformed articles (art. 23 not among them) | https://www.mem.gob.ni/wp-content/uploads/2023/08/2019.02.28-Ley-987-Reforma-a-Ley-822-G-41.pdf | 2026-11-14 |
| Read for DGI catalogue of retention codes and rates, Aviso 005-01-2024 | https://www.dgi.gob.ni/pdfNoticia/3175 | 2026-11-14 |
| Read for DGI FAQ, Infracciones, sanciones y delitos: CTr arts. 124 and 127 | https://www.dgi.gob.ni/FAQ/infracciones__sanciones_y_deli.htm | 2026-11-14 |

Not yet confirmed: any amendment to Ley 822 after Ley 987 (2019) affecting employment income; the late payment surcharge (a DGI FAQ cites 2.5% a month under CTr art. 131, possibly outdated); the value of the unidad de multa; the employer's annual retention report and date; the DGI FAQ pages are dated about 2015 and were read only where Ley 987 did not change the article.
