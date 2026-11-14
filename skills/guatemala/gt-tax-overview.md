---
name: gt-tax-overview
description: >
  Use this Guatemala reference for a first view of the tax system in tax year
  2026 and to find the right Guatemala skill. Match requests such as Guatemala
  taxes overview, what taxes are there in Guatemala, SAT Guatemala, ISR IVA
  ISO IGSS, territorial tax Guatemala, does Guatemala have VAT, quetzal tax
  year, filing calendar Guatemala and doing business in Guatemala tax. It
  names each tax, its law, the headline 2026 rate, the form and deadline, and
  the skill that owns the detail. This Tier 2 draft supports source checking
  and reviewer questions; it does not authorise filing, payment or a tax
  position.
version: 1.0
jurisdiction: GT
tax_year: 2026
tax_year_notes: "Calendar year 2026. Headline figures from Decreto 10-2012 and Decreto 27-92 (TSE consolidated copies through web.archive.org) and SAT pages read on 14 November 2026."
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# Guatemala Tax Overview v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone asking which Guatemalan taxes apply to them in 2026: individuals, self-employed people, companies and foreign businesses with Guatemalan-source income. The national tax authority is the Superintendencia de Administración Tributaria (SAT), which collects about 13 taxes (SAT, principales impuestos). The currency is the quetzal (GTQ, Q). The tax year is the calendar year (Ley de Actualización Tributaria, Decreto 10-2012, LAT, arts 37 and 74). Income tax is territorial: only Guatemalan-source income is taxed (LAT arts 3 and 4).

| Need | Skill |
| --- | --- |
| Individual income tax (employees, self-employed) | `guatemala-income-tax` |
| Company income tax, ISO, withholding on non-residents, transfer pricing | `gt-corporate-income-tax` |
| IVA (VAT) and the small taxpayer regime | `guatemala-iva` |
| Payroll withholding, bonuses, minimum wages | `guatemala-payroll` |
| IGSS, INTECAP, IRTRA | `guatemala-social-contributions` |
| Setting up a company | `gt-company-formation` |

This file does not compute any return. It routes, and states the headline figures with their sources.

## Rates, bands and thresholds

| Item | 2026 figure | Conditions | Source |
| --- | --- | --- | --- |
| ISR, employees | 5% to Q300,000 of annual renta imponible; Q15,000 + 7% above | Residents; detail in `guatemala-income-tax` | [LAT art 73](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| ISR, profit regime | 25% of profit | Companies and individuals who choose it | [LAT art 36](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| ISR, simplified regime | 5% of monthly income to Q30,000; Q1,500 + 7% above | Optional regime on income | [LAT art 44](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| ISR, capital income and gains | 10% | Art 92 | [LAT art 92](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| ISR, dividends | 5% | Art 93 | [LAT art 93](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| ISR, non-residents without a permanent establishment | 3%, 5%, 10%, 15% or 25% of gross by type of income | Table in `gt-corporate-income-tax` | [LAT art 104](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| IVA standard rate | 12%, included in the price | Decreto 27-92 | [LIVA art 10](https://web.archive.org/web/20261030100915/https://tse.org.gt/images/UECFFPP/leyes/decreto_27-92-iva.pdf) |
| IVA small taxpayer | 5% of gross monthly income, annual billing below Q500,285.00 | Replaces IVA credits and ISR | [SAT FAQ, cumplimiento tributario](https://portal.sat.gob.gt/portal/preguntas-frecuentes/cumplimiento-tributario/) |
| Fuel distribution tax | Gasolina superior Q4.70, regular Q4.60, aviación Q4.70, diesel and gas oil Q1.30, kerosene Q0.50, jet kerosene Q0.50, nafta Q0.50 a gallon | Decreto 38-92 | [SAT, principales impuestos](https://portal.sat.gob.gt/portal/principales-impuestos-en-guatemala/) |
| Cement distribution tax | Q1.50 per 42.5 kg bag or equivalent | Decreto 79-2000 | same |
| Vehicle circulation tax | Paid 1 January to 31 July each year | Decreto 70-94 | same |

Other taxes SAT lists: Impuesto de Solidaridad (ISO, Decreto 73-2008, quarterly, for the profit regime with a gross margin above 4%), Impuesto Único Sobre Inmuebles (IUSI, Decreto 15-98, mostly collected by municipalities, quarterly or annual), alcoholic drinks (Decreto 21-2004, on the suggested retail price), tobacco (Decreto 61-77) and the first registration of vehicles (IPRIMA, LAT Libro II). Their rates are not in this pack.

## The base

1. **Is the income Guatemalan-source?** If not, ISR does not reach it (LAT arts 3 and 4).
2. **Which ISR category?** Actividades lucrativas, trabajo or capital (LAT art 2). Employees are taxed by withholding; the self-employed and companies choose the profit or simplified regime (art 14).
3. **IVA status.** Anyone selling goods, providing services, leasing or importing is in the general IVA regime unless registered as a small taxpayer (LIVA arts 3, 45).
4. **Employer?** Payroll withholding and IGSS follow.
5. **Profit regime with a margin above 4%?** ISO applies.

## Deadlines and filing

| Obligation | Form | When |
| --- | --- | --- |
| IVA general regime | SAT-2237 | Within the month after each month (LIVA art 40) |
| IVA small taxpayer | SAT-2046 | Within the month after each month (LIVA art 48) |
| ISR simplified regime | SAT-1311 | First 10 business days of the following month (LAT art 49) |
| ISR profit regime, quarterly | SAT-1361 | Within the month after each quarter (LAT art 38) |
| ISR annual return | SAT-1411 | 1 January to 31 March (LAT art 39) |
| ISO | SAT-1608 | Within the month after each quarter |
| ISR withholdings | SAT-1331, SAT-1352 | First 10 business days of the following month |

Forms and deadlines as listed on SAT's FAQ, cumplimiento tributario. Returns are prepared in Declaraguate through Agencia Virtual and paid with the SAT-2000 slip or online banking.

## Penalties and interest

Sanctions are in the Código Tributario (Decreto 6-91), not opened in this pass. The interest rate for tax purposes under its art 58 is 12.88% for the first half of 2026 and 12.97% for the second half ([Banguat](https://banguat.gob.gt/page/tasas-de-interes-para-efectos-tributarios-determinada-por-la-junta-monetaria)). Vehicle circulation tax paid after 31 July attracts the multa por omisión, interest and mora (SAT FAQ).

## Cross-border points

- Residence for individuals: more than 183 days in the calendar year or the centre of economic interests (LAT art 6).
- Non-residents without a permanent establishment are taxed by withholding on gross (LAT arts 104 and 105).
- Exports of goods and services are exempt from IVA, with the related credit recoverable (LIVA arts 7.2, 16, 23).
- Treaties: none checked in this pack.

## Two worked examples that recompute

### Example 1: a freelancer's invoice

A designer in the simplified ISR regime and the general IVA regime invoices a company Q11,200 IVA included. IVA in the price: Q1,200. The company keeps full accounts and the invoice exceeds Q2,500, so it withholds ISR at 5% of the Q10,000 base: Q500 (LAT art 48). The designer receives Q10,700, reports the IVA on SAT-2237 and the withheld ISR on SAT-1311.

```oa-check
name: Freelancer invoice, IVA and simplified ISR withholding
inputs:
  invoice_inclusive: 11200
steps:
  - base: invoice_inclusive / 1.12
  - iva: base * 0.12
  - isr_withheld: min(base, 30000) * 0.05 + max(base - 30000, 0) * 0.07
  - cash_received: invoice_inclusive - isr_withheld
expected:
  base: 10000
  iva: 1200
  isr_withheld: 500
  cash_received: 10700
```

### Example 2: decision, take the company's profit as a dividend

A company in the profit regime makes Q100,000 of profit. ISR 25% is Q25,000. Distributing the rest, Q75,000, costs 5%, Q3,750. Total tax 28.75% of the profit. Whether a salary to the owner would cost less depends on the 10% cap on related-party salaries (LAT art 21.4) and IGSS; compare in `gt-corporate-income-tax` and `guatemala-payroll` before deciding.

```oa-check
name: Profit regime company, profit paid out as a dividend
inputs:
  profit: 100000
steps:
  - corporate_isr: profit * 0.25
  - dividend: profit - corporate_isr
  - dividend_tax: dividend * 0.05
  - total_tax: corporate_isr + dividend_tax
  - effective_rate: total_tax / profit
expected:
  corporate_isr: 25000
  dividend_tax: 3750
  total_tax: 28750
  effective_rate: 0.2875
```

## Ask the client first

1. Individual or entity, and resident in Guatemala?
2. What income, from where, and in which ISR regime?
3. Registered for IVA, and in which regime?
4. Any employees?
5. Any payments to or from abroad?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| SAT, principales impuestos en Guatemala. Read for the list of taxes, fuel and cement rates, ISO and IUSI timing, vehicle tax period | https://portal.sat.gob.gt/portal/principales-impuestos-en-guatemala/ | 2026-11-14 |
| Decreto 10-2012, LAT, TSE consolidated copy through web.archive.org (capture 29 October 2026). Read for arts 2 to 6, 14, 36 to 49, 73, 92, 93, 104 | https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf | 2026-11-14 |
| Decreto 27-92, Ley del IVA, TSE consolidated copy through web.archive.org (capture 30 October 2026). Read for arts 3, 7, 10, 40, 45 to 49 | https://web.archive.org/web/20261030100915/https://tse.org.gt/images/UECFFPP/leyes/decreto_27-92-iva.pdf | 2026-11-14 |
| SAT, preguntas frecuentes, cumplimiento tributario (copy taken 14 November 2026). Read for the forms and deadlines and the Q500,285 small taxpayer limit | https://portal.sat.gob.gt/portal/preguntas-frecuentes/cumplimiento-tributario/ | 2026-11-14 |
| Banco de Guatemala, tasas de interés para efectos tributarios. Read for the 2026 rates | https://banguat.gob.gt/page/tasas-de-interes-para-efectos-tributarios-determinada-por-la-junta-monetaria | 2026-11-14 |

Not yet confirmed: the ISO rate and base; IUSI, alcohol, tobacco, stamp duty (timbres) and IPRIMA rates; the Código Tributario penalty amounts; whether the fuel tax figures on SAT's page are current after any later reform; treaties.

## Changelog

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-11-14 | Full rewrite to the standard for 2026: official sources only, routing table to the pack, headline figures cited, two recomputing cases |
