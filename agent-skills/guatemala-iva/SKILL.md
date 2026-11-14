---
name: guatemala-iva
description: "Use this Guatemala reference for Impuesto al Valor Agregado (IVA) in tax year 2026, the Régimen General monthly return and the Régimen de Pequeño Contribuyente. Match requests such as prepare IVA return, Guatemala VAT, IVA Guatemala 12%, SAT-2237, SAT-2046, pequeño contribuyente límite Q500,285, factura especial, crédito fiscal, remanente, libro de compras y ventas, FEL, retención IVA, exportaciones IVA and exenciones IVA. It gives the 12% rate, what is taxed and exempt under Decreto 27-92, the conditions for input credit, the monthly deadline, the small taxpayer 5% regime with its 2026 limit and the factura especial rules. This Tier 2 draft supports source checking and reviewer questions; it does not authorise filing, payment or a tax position."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/guatemala-iva"
  jurisdiction: "GT"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Guatemala IVA v3.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Persons in Guatemala that sell goods, provide services, import or lease, in 2026, in quetzales (GTQ, Q). The tax is IVA under the Ley del Impuesto al Valor Agregado, Decreto 27-92 (LIVA), administered by SAT. Periods are monthly.

| Item | 2026 position |
| --- | --- |
| Régimen General | Monthly return SAT-2237: débito fiscal less crédito fiscal (LIVA arts 14, 15, 19, 40) |
| Régimen de Pequeño Contribuyente | 5% of gross monthly income, no credits, no ISR (LIVA arts 45 to 50) |
| Authority and tools | SAT, Agencia Virtual, Declaraguate, FEL electronic invoicing |

### Taxable events (LIVA art 3)

Sale or exchange of movable goods; services provided in Guatemala; imports; leasing of movable and immovable property (rent of property is taxed, legacy listed residential rent as exempt); adjudications in payment; withdrawals for own use; inventory shortfalls other than perishables, force majeure or proven crime; the first sale of immovable property; gifts between living persons; and contributions of immovable property to companies within art 7.3 d). For withdrawals, adjudications and gifts the base is never below cost (art 3, last paragraph).

### Refusals and boundaries

- **R-GT-1, free zones and special laws (ZOLIC, zonas francas, maquila).** Benefits need a valid authorisation; refer.
- **R-GT-2, partial exemption.** Mixed taxable and exempt activity needs an apportionment; flag for a reviewer.
- **R-GT-3, Régimen Primario, Régimen Pecuario (Decreto 31-2024).** Special regimes for farm and livestock producers with their own forms (SAT-2510, SAT-2520). Decreto 31-2024 was not opened; refer.
- **R-GT-4, export refunds (arts 23 to 25).** The refund procedure is outside this file.
- **R-GT-5, vehicles and real estate transfers (arts 55 to 57).** Special bases and payment rules not read here; refer.
- **R-GT-6, imported services from non-residents.** No self-assessment article was read; refer before booking any reverse charge.

### Required inputs

1. RTU constancia: régimen of IVA (General or Pequeño Contribuyente) and NIT.
2. FEL sales documents for the month, including exempt sales and exports.
3. FEL purchase documents and import receipts, entered in the libro de compras.
4. Constancias de retención de IVA received and issued; facturas especiales issued.
5. Prior month's remanente de crédito fiscal.
6. Bank statement for the month.

### Conservative defaults

| Ambiguity | Default |
| --- | --- |
| Rate on a sale unclear | 12% |
| Purchase not linked to the business | No credit (art 16) |
| Document is not a factura, factura especial, nota de débito or import receipt in the client's NIT | No credit (art 18) |
| Factura de pequeño contribuyente | Never a credit; it is a cost for ISR (art 49) |
| Invoice from more than two months back | No credit (art 20) |
| Business-use share of a mixed cost | 0% until shown |
| Counterparty country unclear | Domestic |

## Rates, bands and thresholds

| Item | 2026 figure | Conditions | Source |
| --- | --- | --- | --- |
| Standard rate | 12% of the base | Included in the price of the goods or service | [LIVA art 10](https://web.archive.org/web/20261030100915/https://tse.org.gt/images/UECFFPP/leyes/decreto_27-92-iva.pdf) |
| Pequeño Contribuyente rate | 5% of total gross income from sales and services each month | Registered in that regime | [LIVA art 47](https://web.archive.org/web/20261030100915/https://tse.org.gt/images/UECFFPP/leyes/decreto_27-92-iva.pdf) |
| Pequeño Contribuyente limit | Annual billing below Q500,285.00 (125 monthly non-agricultural minimum wages, Decreto 31-2024) | Calendar year | [SAT FAQ, cumplimiento tributario](https://portal.sat.gob.gt/portal/preguntas-frecuentes/cumplimiento-tributario/) |
| Pequeño Contribuyente invoice threshold | Invoice every sale over Q50.00; smaller sales may be grouped in one daily invoice | Art 49 | [LIVA art 49](https://web.archive.org/web/20261030100915/https://tse.org.gt/images/UECFFPP/leyes/decreto_27-92-iva.pdf) |
| IVA withholding, minimum invoice | Régimen General from Q2,500.00 IVA included (Q30,000.00 when the agent is a public body); Pequeño Contribuyente from Q2,500.01 | Agents of retention of IVA | [SAT FAQ, contribuyentes especiales](https://portal.sat.gob.gt/portal/preguntas-frecuentes/contribuyentes-especiales/) |
| Late input credit | At most the two months after the period of the operation | Then lost | [LIVA art 20](https://web.archive.org/web/20261030100915/https://tse.org.gt/images/UECFFPP/leyes/decreto_27-92-iva.pdf) |
| Exempt housing | Home up to 80 m² built and Q250,000.00; urbanised lot up to 120 m² and Q120,000.00 | Buyer and family own no home or other property; stated in the deed | [LIVA art 7.12](https://web.archive.org/web/20261030100915/https://tse.org.gt/images/UECFFPP/leyes/decreto_27-92-iva.pdf) |
| Exempt market retail | Fresh meat, fish, fruit, vegetables, cereals and basic grains to final consumers in cantonal and municipal markets, up to Q100.00 per transaction | Art 7.11 | same |

## The base

### Débito and crédito

- **Base**: the price of the sale or the value of the service (arts 11 to 13). The 12% is inside the price, so the IVA in an inclusive amount is amount x 12 / 112.
- **Débito fiscal**: the tax charged on taxable operations in the period (art 14).
- **Crédito fiscal**: tax on imports, purchases and services linked to the economic activity (arts 15, 16). Tax on fixed assets counts when they are directly linked to production or sale; it then does not form part of their cost for ISR depreciation (art 16). The reglamento lists non-creditable expenses (art 16, last paragraph; not read).
- **Documents** (art 18): factura, factura especial, nota de débito or crédito, import payment receipt or public deed, electronic documents through an authorised issuer; in the buyer's name and NIT; detailed; entered in the libro de compras; the credit balance booked as a receivable.
- **Timing** (art 20): report the credit in the month; at most the two following months.
- **Notes** (art 17): credit notes received reduce the credit; debit notes registered within two months of the invoice add to it.
- **Payable** (art 19): débitos less créditos. A remanente carries to the next period (art 21) until used; no refund, except for exporters and sales to exempt persons under art 23 (art 22).

### Exempt operations (art 7, general)

| Item | Note |
| --- | --- |
| Exports of goods and services | Art 7.2; with refund of related credit (arts 16, 23) |
| Imports by cooperatives (capital goods), temporary import regime, travellers' baggage, returning diplomats, missions, international bodies | Art 7.1, with the procedures stated there |
| Transfers in mergers, inheritance, contributions of movables and of immovables to companies | Art 7.3; not a contribution of property already contributed to a real estate developer |
| Services of institutions supervised by the Superintendencia de Bancos and of authorised stock exchanges | Art 7.4. For insurers and bonding companies only reinsurance and reaffiançamiento are exempt: ordinary insurance is taxed (legacy listed insurance as exempt) |
| Cooperatives with members; savings and credit cooperatives | Art 7.5 |
| Issue and transfer of títulos de crédito and shares, except the factura cambiaria | Art 7.6 |
| Interest on securities of companies traded on an authorised exchange | Art 7.7 |
| Constitution and return of trusts | Art 7.8 |
| Donations to educational, cultural, social or religious non-profits | Art 7.9 |
| Membership fees to associations, professional colleges, parties | Art 7.10 |
| Market retail up to Q100 | Art 7.11 |
| Social housing and lots within the limits | Art 7.12. Second and later transfers of homes pay stamp duty instead |
| Services of registered non-profits that distribute no profit | Art 7.13 |
| Sale of assets of banks under a regularisation plan | Art 7.14 |
| Generic and natural alternative medicines in the Registro Sanitario; antiretrovirals | Art 7.15 |

### Exempt persons (art 8, specific)

Public and private schools for enrolment, fees and exams of authorised courses; universities; CDAG and the Olympic Committee; IGSS; diplomatic missions on reciprocity; international bodies with an agreement. They receive the invoice but pay no IVA, handing over a constancia de exención (art 9).

Legacy errors corrected: medical services, residential rent, public transport, domestic electricity and water, books and the first sale of unprocessed farm produce are not in art 7 or 8 of the text read; treat them as taxed unless another law exempts them (see Not yet confirmed).

### Pequeño Contribuyente (arts 45 to 50)

- Who: individuals or entities with annual billing below the limit; registration by request or by SAT; leaving when the previous calendar year exceeded it, or SAT moves the taxpayer to the General regime (arts 46, 50).
- Tax: 5% of gross monthly income (art 47). Where an agent of retention pays, the retention is the definitive tax; otherwise the taxpayer pays with SAT-2046 within the following month, even with no activity (art 48).
- Books and invoices: only the libro de compras y ventas; invoice sales over Q50 (art 49).
- Effects: no credit for the buyer; no ISR returns or payments (art 49).
- The electronic small taxpayer regime (SAT-2241) was repealed from 31 July 2025 by Decreto 31-2024 (SAT FAQ).

### Factura especial (art 52; LAT art 16)

A taxpayer buying from an individual who does not issue invoices issues a factura especial in the seller's name and withholds the IVA. Not allowed between IVA taxpayers or for habitual operations between individuals, unless the issuer records that the seller refused to invoice. The IVA withheld is declared on SAT-2085 within the following month, and the ISR withheld at the simplified regime rates (LAT art 16) on SAT-1331 in the first 10 business days (SAT FAQ).

### Bank-line patterns

| Pattern | Treatment |
| --- | --- |
| BANCO INDUSTRIAL, BI, BANRURAL, BAM, G&T, BAC | Bank services: exempt (art 7.4); loan principal excluded |
| SAT, SUPERINTENDENCIA | Exclude: tax payment |
| IGSS | Exclude: social security; IGSS is an exempt person (art 8.4) |
| EEGSA, ENERGUATE, EMPAGUA, CLARO, TIGO, MOVISTAR | Domestic purchases at 12% with FEL in the client's NIT |
| GOOGLE, MICROSOFT, ADOBE, META, ZOOM, SLACK, NOTION, ANTHROPIC, OPENAI | Foreign supplier: R-GT-6, refer before any self-assessment |
| PAIZ, WALMART, LA TORRE, RESTAURANTE | Default: no credit (personal or not linked, art 16) until the business link is shown |
| ABOGADO, NOTARIO, CONTADOR | Domestic 12% with FEL |
| AUTOMOTRIZ, vehicle purchase | Flag: credit only if directly linked to production or sale (art 16) |
| TRANSFERENCIA PROPIA, PLANILLA, SALARIO | Exclude |

### Reviewer catalogue

- **Real estate**: first sale of a property is taxed (art 3.8); later transfers pay stamp duty (art 7.12). Ask which.
- **Central American services**: is the service consumed abroad and an export (art 7.2)?
- **Vehicles**: business link and the art 55 rules.
- **Purchases above sales for three periods**: the return must carry a documented explanation (art 40).

## Deadlines and filing

| Obligation | Form | When | Source |
| --- | --- | --- | --- |
| General regime monthly return and payment, including exempt operations | SAT-2237 | Within the calendar month after the period | LIVA art 40; SAT FAQ |
| Pequeño Contribuyente monthly return | SAT-2046 | Within the calendar month after the period | LIVA art 48; SAT FAQ |
| IVA withheld on facturas especiales | SAT-2085 | Within the calendar month after the period | SAT FAQ |
| Libros de compras y ventas | Physical or electronic | Kept current at the fiscal domicile | LIVA arts 37, 39 |

Steps for SAT-2237: open Declaraguate in Agencia Virtual, choose the period, enter sales (taxable, exempt, exports), purchases and imports with their IVA, retentions suffered and the prior remanente, validate and freeze, then pay through the SAT-2000 slip or online banking. A correction is a new form quoting the earlier form number in Rectificación (SAT FAQ).

## Penalties and interest

The Código Tributario (Decreto 6-91) sets the sanctions; its text was not opened in this pass. Confirmed items: special taxpayers that do not file the electronic purchases and sales report pay Q5,000 the first time, Q10,000 the second, then Q10,000 plus 1% of the last month's gross income (Código Tributario art 94.13, quoted by SAT FAQ contribuyentes especiales); the interest rate for tax purposes is 12.88% (first half of 2026) and 12.97% (second half) ([Banguat](https://banguat.gob.gt/page/tasas-de-interes-para-efectos-tributarios-determinada-por-la-junta-monetaria)). A Pequeño Contribuyente that does not demand or keep purchase invoices is sanctioned under the Código Tributario (art 49).

## Cross-border points

- Exports of goods and services are exempt with the right to recover the linked credit (arts 7.2, 16, 23).
- Imports are taxed (art 3.3); the customs receipt supports the credit (art 18).
- Services received from abroad: R-GT-6.
- Exporters with domestic sales show the two liquidations separately on the return (art 16).

## Two worked examples that recompute

### Example 1: General regime month

A company sells Q112,000 IVA included in March 2026. Purchases with FEL in its NIT, entered in the libro de compras, carry Q7,000 of IVA. It also finds a December 2025 invoice with Q500 of IVA never reported: more than two months late, so no credit (art 20). Prior remanente Q1,000.

```oa-check
name: SAT-2237 March 2026
inputs:
  sales_inclusive: 112000
  purchase_iva: 7000
  late_invoice_iva: 500
  prior_remanente: 1000
steps:
  - base: sales_inclusive / 1.12
  - debito: base * 0.12
  - credito: purchase_iva + prior_remanente
  - payable: max(debito - credito, 0)
  - remanente_next: max(credito - debito, 0)
  - lost_credit: late_invoice_iva
expected:
  base: 100000
  debito: 12000
  payable: 4000
  remanente_next: 0
  lost_credit: 500
```

### Example 2: decision, Pequeño Contribuyente or General regime

An individual shopkeeper sells Q30,000 a month to final consumers, Q360,000 a year, below Q500,285. Purchases carry Q1,600 of IVA a month.

- Pequeño Contribuyente: 5% x Q30,000 = Q1,500, and no ISR (art 49).
- General regime with the ISR simplified regime: IVA Q3,214.29 less Q1,600 = Q1,614.29; ISR 5% of Q26,785.71 = Q1,339.29; total Q2,953.57.
- Pequeño Contribuyente saves Q1,453.57 a month. It loses when customers are businesses that need a credit, because its invoices give none.

```oa-check
name: Pequeño Contribuyente or General, Q30,000 a month
inputs:
  monthly_sales: 30000
  purchase_iva: 1600
steps:
  - pc_tax: monthly_sales * 0.05
  - net_sales: monthly_sales / 1.12
  - debito: net_sales * 0.12
  - iva_general: debito - purchase_iva
  - isr_simplified: min(net_sales, 30000) * 0.05 + max(net_sales - 30000, 0) * 0.07
  - general_total: round(iva_general + isr_simplified, 2)
  - saving_pc: round(general_total - pc_tax, 2)
expected:
  pc_tax: 1500
  general_total: 2953.57
  saving_pc: 1453.57
```

## Ask the client first

1. Régimen General or Pequeño Contribuyente on the RTU, and the year's billing so far?
2. Are any sales exports, exempt operations or sales to exempt persons (art 8)?
3. Are all purchase documents FEL in the client's NIT and entered in the libro de compras?
4. Any purchases from individuals who do not invoice (factura especial)?
5. Is the client an agent of retention of IVA, or were retentions suffered?
6. Prior month's remanente?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Decreto 27-92, Ley del IVA, TSE consolidated copy through web.archive.org (capture 30 October 2026; SAT and Congreso refuse scripted downloads). Read for arts 1 to 22, 37 to 41, 45 to 54 | https://web.archive.org/web/20261030100915/https://tse.org.gt/images/UECFFPP/leyes/decreto_27-92-iva.pdf | 2026-11-14 |
| Decreto 10-2012, LAT, same route. Read for art 16 (ISR on facturas especiales) and arts 150 to 158 (IVA reforms) | https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf | 2026-11-14 |
| SAT, preguntas frecuentes, cumplimiento tributario (copy taken 14 November 2026). Read for SAT-2237, 2046, 2085, 2241 and their deadlines, the 125 minimum wages and Q500,285 limit, the repeal of the electronic regime from 31 July 2025, and rectification | https://portal.sat.gob.gt/portal/preguntas-frecuentes/cumplimiento-tributario/ | 2026-11-14 |
| SAT, preguntas frecuentes, contribuyentes especiales (copy taken 14 November 2026). Read for the IVA withholding minimums and the art 94.13 sanction | https://portal.sat.gob.gt/portal/preguntas-frecuentes/contribuyentes-especiales/ | 2026-11-14 |
| SAT, principales impuestos. Read for the 12% included in prices and monthly reporting | https://portal.sat.gob.gt/portal/principales-impuestos-en-guatemala/ | 2026-11-14 |
| Diario de Centro América, on the Decreto 31-2024 change of regime. Read for the move from the electronic small taxpayer regime and the art 20 transitorio | https://dca.gob.gt/noticias-guatemala-diario-centro-america/cambio-de-regimen-a-pequenos-contribuyentes-vence-hoy/ | 2026-11-14 |
| Banco de Guatemala, tasas de interés para efectos tributarios. Read for the 2026 rates | https://banguat.gob.gt/page/tasas-de-interes-para-efectos-tributarios-determinada-por-la-junta-monetaria | 2026-11-14 |

Not yet confirmed: the text of Decreto 31-2024, including whether it changed the 5% rate (the limit is from SAT's FAQ); the Reglamento (Acuerdo Gubernativo 5-2013) and its list of non-creditable expenses, so legacy's blocked entertainment and vehicles are only defaults; the IVA withholding percentages for agents (legacy 15% card processors, 25% State, 65% exporters; Decreto 20-2006 not opened); any rule for self-assessing IVA on services from non-residents; exemptions in laws other than Decreto 27-92 (books, medical services and others legacy listed); the SAT-2237 box numbers (legacy's line map); the Código Tributario sanctions for late returns; the art 55 to 57 vehicle and real estate rules.

## Changelog

| Version | Date | Change |
| --- | --- | --- |
| 3.0 | 2026-11-14 | Full rewrite to the standard for 2026 from the law: small taxpayer limit Q500,285 (legacy Q150,000), exemption list taken from arts 7 and 8 (legacy listed medical services, insurance, residential rent, transport, utilities and books), credit timing and document rules added, factura especial and Pequeño Contribuyente rules from the text, two recomputing cases |
| 2.0 | 2026-04 | Full rewrite to 10-section architecture |
| 1.0 | | Initial skill |

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `guatemala-iva` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/guatemala-iva. If neither is available, confirm every figure against the official source pages cited above before relying on it.
