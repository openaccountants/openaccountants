---
name: gt-corporate-income-tax
description: "Use this Guatemala reference for company income tax (ISR on rentas de actividades lucrativas) in tax year 2026 for sociedades, branches and other entities. Match requests such as Guatemala corporate tax, ISR empresas, régimen sobre utilidades 25%, régimen opcional simplificado 5% 7%, pagos trimestrales ISR, SAT-1361, SAT-1411, Impuesto de Solidaridad ISO, dividendos 5%, retención no residentes, partes relacionadas precios de transferencia, intereses deducibles and depreciación Guatemala. It gives the rates, quarterly payments, deduction limits, depreciation rates, dividend and non-resident withholding rates and transfer pricing rules of Decreto 10-2012, with SAT forms and deadlines. This Tier 2 draft supports source checking and reviewer questions; it does not authorise filing, payment or a tax position."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/gt-corporate-income-tax"
  jurisdiction: "GT"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Guatemala Corporate Income Tax v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Sociedades anónimas, sociedades de responsabilidad limitada, branches and permanent establishments of foreign entities, and other entes or patrimonios with rentas de actividades lucrativas from Guatemalan sources in 2026 (Ley de Actualización Tributaria, Decreto 10-2012, LAT, arts 1 to 4, 10 to 12). Amounts in quetzales (GTQ, Q). Authority: SAT.

Every entity is in one of two regimes (LAT art 14): the Régimen Sobre las Utilidades de Actividades Lucrativas (25% of profit) or the Régimen Opcional Simplificado Sobre Ingresos (5% and 7% of monthly income). The pack's individual rules are in `guatemala-income-tax`; IVA in `guatemala-iva`; payroll in `guatemala-payroll`.

### Refusals and boundaries

- Banks, insurers and financial groups (special dividend rule in art 93; interest limit exclusions in art 24): refer.
- Free zones, maquila and other incentive laws: refer.
- Mining, construction and natural resource rules (arts 31 to 34): refer.
- Transfer pricing studies and advance pricing agreements: the rules are summarised below; the analysis goes to a reviewer.
- ISO computations: the rate and base were not opened; refer.

### Required inputs

1. RTU: regime of ISR, and whether the entity is an agent of retention or a special taxpayer.
2. Trial balance and financial statements for 2026; renta bruta, exempt income and costs with their documents.
3. Related-party transactions, including those with non-residents.
4. Interest paid, loan currency and lender, and average net assets.
5. Quarterly payments made (SAT-1361) and the option used (partial closings or 8%).
6. Dividends declared and payments to non-residents.

## Rates, bands and thresholds

| Item | 2026 figure | Conditions | Source |
| --- | --- | --- | --- |
| Profit regime rate | 25% of renta imponible | Régimen Sobre las Utilidades | [LAT art 36](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| Profit regime quarterly payment, estimated option | Renta imponible estimated at 8% of the quarter's renta bruta, less exempt income | The other option is partial closings each quarter | [LAT art 38](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| Simplified regime, first band | 5% of monthly renta imponible up to Q30,000.00 | Renta bruta less exempt income | [LAT art 44](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| Simplified regime, second band | Q1,500.00 plus 7% of the excess over Q30,000.00 | Monthly | same |
| Salaries to partners, directors, spouses and relatives | Deductible up to 10% of renta bruta in total | Art 21.4 | [LAT art 21](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| Donations to non-profits, churches, parties | Up to 5% of renta bruta and at most Q500,000.00 a year | Donee registered with fiscal solvency; State, universities, cultural or scientific bodies not capped | [LAT art 21.22](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| Interest deduction cap | Junta Monetaria tax rate x 3 x average total net assets | Not for banks, financial companies, cooperatives | [LAT art 24](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| Junta Monetaria tax interest rate, 2026 | 12.88% first half, 12.97% second half | Código Tributario art 58; also the art 24 rate ceiling for quetzal loans | [Banguat](https://banguat.gob.gt/page/tasas-de-interes-para-efectos-tributarios-determinada-por-la-junta-monetaria) |
| Depreciation, buildings | 5% a year, straight line maximum | Art 28.1 | [LAT art 28](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| Depreciation, fruit-bearing plants | 15% | Art 28.2 | same |
| Depreciation, furniture, office equipment, vessels, machinery, vehicles | 20% | Art 28.3 and 28.4 | same |
| Depreciation, computer equipment | 33.33% | Art 28.5 | same |
| Depreciation, tools, crockery and similar; breeding animals | 25% | Art 28.6 and 28.7 | same |
| Depreciation, other movables | 10% | Art 28.8 | same |
| Dividends and profit distributions | 5% withheld | Whatever the name; financial groups only on distribution to the holding | [LAT art 93](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| Rentas de capital and capital gains | 10% | Art 92 | [LAT art 92](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| Non-residents: international transport, insurance premiums, international telecoms, branch remittances to head office | 5% definitive | Art 104.1 | [LAT art 104](https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf) |
| Non-residents: international news, films, recordings and broadcasts | 3% | Art 104.1, exception | same |
| Non-residents: interest | 10% | Except loans from regulated banks and multilaterals (art 104.2) | same |
| Non-residents: salaries, artists and sportspeople, royalties, fees, technical, economic or financial advice | 15% | Art 104.3 | same |
| Non-residents: other income | 25% | Art 104.4 | same |

## The base

### Profit regime

1. **Renta bruta**: all income and gains of the period, exempt or taxed (art 20).
2. Less exempt income (art 11) and rentas de capital, which are taxed apart (art 15).
3. Less deductible costs and expenses (art 21): cost of goods, services, transport and fuel, wages, aguinaldo and Bono 14, IGSS cuotas, interest within art 24, depreciation within art 28, donations within art 21.22, losses from destruction of goods with proof, fees for services in or from abroad, exchange losses on currency bought for the business, and the rest of the list.
4. Each deduction must be useful and necessary, booked by those keeping full accounts, with withholding done where due, wages on the IGSS planilla, and the documents of art 22 (facturas, facturas especiales, foreign invoices, deeds, bank notes, IGSS planillas, customs declarations).
5. Not deductible (art 23): costs not from the business, undocumented costs, costs where withholding was not made, profit-based bonuses, returns on capital, owners' drawings, permanent improvements to assets (capitalise), recreation investments, exchange losses from revaluations, and the rest of the list.
6. Tax at 25% (art 36), for the year 1 January to 31 December, which must match the accounting year; SAT may authorise special periods at start or end (art 37).

### Simplified regime

Monthly renta bruta less exempt income, taxed at the art 44 scale, mostly by withholding of the payers that keep full accounts (arts 46 to 48). No costs are deducted. Monthly SAT-1311 and annual informative SAT-1411 (art 49). Not subject to ISO (Decreto 73-2008 art 4 f, as reformed by LAT art 178).

### Impuesto de Solidaridad (ISO)

Paid by entities in the profit regime that have their own assets, carry on commercial or farm activity and have a gross margin above 4% of gross income; quarterly (SAT, principales impuestos). Form SAT-1608, within the month after each calendar quarter (SAT FAQ). Rate, base and crediting against ISR: Not yet confirmed.

### Transfer pricing (LAT arts 54 to 67)

Operations with related parties resident abroad are valued at the arm's length price (art 54). Art 56 defines related parties; art 57 sets the scope (operations with non-resident related parties that affect the Guatemalan tax base); art 58 the comparability analysis; art 59 the methods (comparable uncontrolled price, resale price, cost plus, profit split, transactional net margin); art 60 commodity imports and exports; art 61 recharacterisation; art 62 intra-group services; art 63 advance pricing agreements; arts 65 to 67 the documentation on the group and on the taxpayer. Refer any study.

### Bank-line patterns

| Pattern | Treatment |
| --- | --- |
| SAT, ISR TRIMESTRAL, SAT-1361 | Quarterly ISR paid: credit against the annual tax |
| RETENCION ISR from clients | Simplified regime tax withheld; credit on SAT-1311 |
| DIVIDENDOS, distribución de utilidades | 5% withheld and declared |
| Transfers to foreign suppliers (fees, royalties, licences, interest) | Withhold under art 104 and file SAT-1352 |
| PRESTAMO, interest to related parties | Test art 24 and arts 54 to 67 |
| IGSS, PLANILLA | Wages deductible only with the IGSS planilla (art 22.3) |

## Deadlines and filing

| Obligation | Form | When | Source |
| --- | --- | --- | --- |
| Profit regime quarterly payment | SAT-1361 | Within the month after each quarter; the fourth with the annual return | LAT art 38; SAT FAQ |
| Annual return, profit regime, with payment | SAT-1411 | 1 January to 31 March, also with exempt income or no activity | LAT art 39; SAT FAQ |
| Simplified regime monthly | SAT-1311 | First 10 business days of the following month | LAT art 49; SAT FAQ |
| Simplified regime annual informative | SAT-1411 | 1 January to 31 March | LAT art 49 |
| ISO | SAT-1608 | Within the month after each calendar quarter | SAT FAQ |
| Withholdings on residents (simplified regime suppliers, facturas especiales, employment) | SAT-1331 | First 10 business days of the following month | LAT arts 48, 80; SAT FAQ |
| Withholdings on non-residents | SAT-1352 | First 10 business days of the following month | LAT art 105; SAT FAQ |
| Capital income and dividends withheld | per SAT form | First 10 days of the month after payment | LAT art 94 |
| Change of quarterly option | Aviso to SAT | In December, effective from the next year's first quarter | LAT art 38 |

Entities required to keep full accounts keep the balance sheet, income statement, cash flow and cost of production statements available to SAT (art 40). Agents of retention of IVA and special taxpayers have further reporting duties (art 40.2).

## Penalties and interest

The Código Tributario (Decreto 6-91) was not opened in this pass, so the multa, mora and late-filing amounts are not stated. Confirmed: the interest rate for tax purposes is 12.88% (first half of 2026) and 12.97% (second half) (Banguat); the non-filing of the electronic purchases and sales report by special taxpayers costs Q5,000 the first time, Q10,000 the second and then Q10,000 plus 1% of the last month's gross income (Código Tributario art 94.13, quoted by SAT FAQ contribuyentes especiales); a payer that does not withhold stays jointly liable (LAT art 106).

## Cross-border points

- Territorial: only Guatemalan-source income is taxed (arts 3 and 4).
- A non-resident with a permanent establishment (art 7) is taxed like a resident on its establishment's income (art 102); without one, by definitive withholding on gross at the art 104 rates, declared by the payer on SAT-1352 or, if not withheld, by the non-resident on SAT-1371 (arts 105, 106).
- Branch profit remittances to the head office: 5% (art 104.1 e).
- Interest paid abroad: art 24 caps the deduction and lowers the rate ceiling on foreign currency loans by the exchange rate change; lenders must be regulated banks or financial entities.
- Transfer pricing applies to non-resident related parties (arts 54 to 67). Treaties: none checked.

## Two worked examples that recompute

### Worked case 1: sociedad anónima in the profit regime, 2026

Renta bruta Q2,000,000 (no exempt income), deductible costs Q1,500,000 excluding a Q150,000 donation to a registered foundation. Cap: min(5% x Q2,000,000, Q500,000) = Q100,000; Q50,000 is not deductible. Quarterly payments used the 8% option on Q500,000 of renta bruta a quarter.

```oa-check
name: SA profit regime with donation cap and 8% quarterly payments
inputs:
  renta_bruta: 2000000
  costs: 1500000
  donation: 150000
  quarter_gross: 500000
steps:
  - donation_cap: min(renta_bruta * 0.05, 500000)
  - donation_allowed: min(donation, donation_cap)
  - renta_imponible: renta_bruta - costs - donation_allowed
  - isr: renta_imponible * 0.25
  - quarterly_payment: quarter_gross * 0.08 * 0.25
  - paid_q1_to_q3: quarterly_payment * 3
  - due_with_annual: isr - paid_q1_to_q3
expected:
  donation_allowed: 100000
  renta_imponible: 400000
  isr: 100000
  quarterly_payment: 10000
  due_with_annual: 70000
```

### Worked case 2: decision, profit or simplified regime for a trading company

Monthly income before IVA Q500,000 (Q6,000,000 a year), deductible costs Q5,200,000. Simplified: Q1,500 + 7% x Q470,000 = Q34,400 a month, Q412,800 a year. Profit: 25% x Q800,000 = Q200,000, plus ISO (not confirmed). With a thin 13% margin the profit regime saves Q212,800 before ISO.

```oa-check
name: Trading company, profit or simplified regime
inputs:
  monthly_income: 500000
  annual_costs: 5200000
steps:
  - simplified_month: min(monthly_income, 30000) * 0.05 + max(monthly_income - 30000, 0) * 0.07
  - simplified_year: simplified_month * 12
  - profit_tax: (monthly_income * 12 - annual_costs) * 0.25
  - saving_profit_regime: simplified_year - profit_tax
expected:
  simplified_month: 34400
  simplified_year: 412800
  profit_tax: 200000
  saving_profit_regime: 212800
```

## Ask the client first

1. Which ISR regime is on the RTU, and since when?
2. Turnover and margin for 2026; any exempt income or rentas de capital?
3. Related-party operations with non-residents, and loans with their rates?
4. Quarterly option used (partial closings or 8%) and payments made?
5. Payments to non-residents and dividends declared?
6. Any incentive law, free zone or regulated financial activity?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Decreto 10-2012, Ley de Actualización Tributaria, TSE consolidated copy through web.archive.org (capture 29 October 2026). Read for arts 1 to 7, 10 to 49, 54 to 67, 83, 92 to 95, 97 to 107, 172, 173, 178 | https://web.archive.org/web/20261029214607/https://tse.org.gt/images/UECFFPP/leyes/decreto_10-2012_Ley_actualizacion_tributaria.pdf | 2026-11-14 |
| SAT, preguntas frecuentes, cumplimiento tributario (copy taken 14 November 2026). Read for SAT-1311, 1331, 1352, 1361, 1371, 1411 and 1608 with deadlines | https://portal.sat.gob.gt/portal/preguntas-frecuentes/cumplimiento-tributario/ | 2026-11-14 |
| SAT, preguntas frecuentes, contribuyentes especiales (copy taken 14 November 2026). Read for the art 94.13 sanction and agents of retention | https://portal.sat.gob.gt/portal/preguntas-frecuentes/contribuyentes-especiales/ | 2026-11-14 |
| SAT, principales impuestos en Guatemala. Read for who pays ISO and how often | https://portal.sat.gob.gt/portal/principales-impuestos-en-guatemala/ | 2026-11-14 |
| Banco de Guatemala, tasas de interés para efectos tributarios. Read for the 2026 rates 12.88% and 12.97% | https://banguat.gob.gt/page/tasas-de-interes-para-efectos-tributarios-determinada-por-la-junta-monetaria | 2026-11-14 |

Not yet confirmed: the ISO rate, base and crediting against ISR (Decreto 73-2008 not opened; legacy said 1% of the greater of net assets or gross income); whether LAT allows losses to be carried forward (no such article found in the Book I text read); the Código Tributario penalty amounts; reforms of Decreto 10-2012 after the TSE consolidation; whether the 5% dividend rate applies unchanged to non-resident shareholders (legacy cited up to 10%; art 93 states 5% without distinction); treaties; transfer pricing thresholds and filing forms.

## Changelog

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-11-14 | Full rewrite to the standard for 2026 from the law: canonical headings, every rate cited to Decreto 10-2012, deduction limits, depreciation, quarterly 8% option, non-resident table, transfer pricing summary, SAT forms, two recomputing cases; status needs_sources removed |

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `gt-corporate-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/gt-corporate-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
