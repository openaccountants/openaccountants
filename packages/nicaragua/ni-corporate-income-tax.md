---
name: ni-corporate-income-tax
description: >
  Use this skill for Nicaragua income tax on business income (IR de rentas de actividades
  economicas) of companies and individuals with income above C$12,000,000 for tax year
  2026. It gives the 30% rate, the pago minimo definitivo of Ley 987 (3% for large
  taxpayers, 2% for principal taxpayers, 1% for the rest) and its exceptions (first three
  years with new investment, maturation periods), monthly advances, the higher of IR or
  PMD, the 2% and 10% retentions received, definitive retentions to non-residents (20%,
  reduced 1.5% and 3% rates) and tax havens (30%), and the annual return due by the last
  day of February. Trigger phrases include IR anual Nicaragua, pago minimo definitivo,
  anticipo IR, rentas de actividades economicas, DGI VET and Ley 822.
version: "1.0"
jurisdiction: NI
tax_year: 2026
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Nicaragua income tax on business income, tax year 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Nicaraguan accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Nicaragua.

## Who this applies to

Residents (companies, individuals with a business, trusts, investment funds) and permanent establishments earning income from economic activities in Nicaragua in the fiscal period 2026 (calendar year unless DGI authorised a special 12-month period, LCT art. 50). The law is the Ley de Concertacion Tributaria (Ley 822) as reformed by Ley 987 of 2019.

Refer: taxpayers with gross income up to C$12,000,000 (they use the art. 52 progressive table, not read in this pass); cuota fija; financial institutions (capital income integrated, art. 38); free zones and incentive regimes; cooperatives (exempt up to C$60,000,000 of gross income, art. 32.5); fishing on the Caribbean coast (2% PMD). Employment income: [nicaragua-income-tax](nicaragua-income-tax.md).

## Rates, bands and thresholds

| Item | Rate or amount | Condition | Source |
| --- | --- | --- | --- |
| IR on business income | 30% of renta neta | Gross income above C$12,000,000 | DGI FAQ, Liquidacion del impuesto: https://www.dgi.gob.ni/FAQ/liquidacion_del_impuesto.htm |
| Threshold for the art. 52 table | C$12,000,000 of gross annual income | At or below: art. 52 table | same |
| Pago minimo definitivo, large taxpayers (art. 61.1) | 3% of gross taxable income | 2% for Caribbean coast fishing | La Gaceta 41 of 28 Feb 2019, Ley 987 (copy at MEM): https://www.mem.gob.ni/wp-content/uploads/2023/08/2019.02.28-Ley-987-Reforma-a-Ley-822-G-41.pdf |
| Pago minimo definitivo, principal taxpayers (art. 61.2) | 2% | DGI classification | same |
| Pago minimo definitivo, other taxpayers (art. 61.3) | 1% | | same |
| Cooperatives' exemption (art. 32.5) | Gross income up to C$60,000,000 | IR on the excess | same |
| Payments to tax havens (art. 49) | 30% definitive | Residents and permanent establishments paying | same |
| Non-residents, other economic activities (art. 53.3) | 20% definitive | | same |
| Capital income and gains (art. 87.2) | 15% | Residents and non-residents | same |
| Retention on purchases of goods and services (code 22) | 2% a cuenta | Paid by retention agents | DGI catalogue of retention codes and rates (Aviso 005-01-2024): https://www.dgi.gob.ni/pdfNoticia/3175 |
| Retention on card sales (code 21) | 1.5% a cuenta | | same |
| Retention on professional services by individuals (code 27) | 10% a cuenta | | same |
| Reinsurance to non-residents (code 43) | 1.5% definitive | | same |
| Insurance, transport and international telecoms to non-residents (codes 44 to 46) | 3% definitive | | same |
| Advance of PMD, due date | By the 15th of the following month | Next working day if a holiday | DGI FAQ, Anticipos a cuenta: https://www.dgi.gob.ni/FAQ/anticipos_a_cuenta.htm |

## The base

1. **Renta bruta** from economic activities with Nicaraguan source; capital income and gains are taxed separately at 15% (art. 34.1), except for financial institutions.
2. **Deductions (art. 39):** costs and expenses necessary to produce taxable income, including financial interest within the art. 48 limits. Mixed taxed and exempt income: only the proportion of taxable over total income is deductible unless costs can be traced (art. 41.1).
3. **IR** = 30% of renta neta.
4. **PMD** = 1%, 2% or 3% of gross taxable income (art. 61), paid as monthly advances; retentions on sales and tax credits are creditable against it (arts. 62, 63). Splitting operations to drop to a lower PMD rate has no effect (art. 61 bis).
5. **Tax payable** = the higher of annual IR and PMD (art. 61; DGI FAQ). Credits in order: advances, retentions, other authorised credits (art. 65).
6. **Exceptions from PMD (art. 59):** the first three years of operations made with new investment (not used assets bought locally, not consortia, not taxpayers moved from the simplified regime); approved maturation periods; other cases in art. 59.

Large ISC and fuel tax collectors and SIBOIF-supervised financial institutions pay as monthly advance the higher of 30% of monthly profit and the PMD rate on gross income (art. 63).

## Deadlines and filing

| Obligation | Deadline | Channel |
| --- | --- | --- |
| Annual IR return and payment (art. 69.1) | Last calendar day of the second month after the period: 28 February 2027 for 2026 | DGI VET |
| Monthly advance (anticipo or PMD) | 15th of the following month, even if nil (art. 69.4) | Declaracion mensual de recaudos y anticipos (form 124) |
| Retentions made | Monthly | Same monthly declaration |

The old version of this skill said 31 March; Ley 987 moved the date to the end of February.

## Penalties and interest

Codigo Tributario sanctions (art. 124): fines in unidades de multa, closure, loss of benefits. Late books: 110 to 130 units (art. 127.4). The late payment surcharge on advances is listed under Not yet confirmed.

## Cross-border points

Payments to non-residents bear definitive retentions: 20% on economic activities in general, 15% on capital income (10% for loans from investment-grade international banks), 3% on insurance, transport and international telecoms, 1.5% on reinsurance; 30% to tax havens. Transfer pricing rules of Ley 822 (arts. 93 onward) were not read. No tax treaty was confirmed.

## Two worked examples that recompute

### Example 1: trading company, other taxpayer (1% PMD)

Gross income C$40,000,000, renta neta C$3,000,000. IR 30% = C$900,000; PMD 1% = C$400,000. Pays C$900,000, less advances of C$400,000 already paid during the year: C$500,000 with the return by 28 February 2027.

```oa-check
name: NI 2026 IR against PMD, profitable company
inputs:
  gross: 40000000
  net: 3000000
  pmd_rate: 0.01
steps:
  - ir: net * 0.30
  - pmd: gross * pmd_rate
  - payable: max(ir, pmd)
  - balance_with_return: payable - pmd
expected:
  ir: 900000
  pmd: 400000
  payable: 900000
  balance_with_return: 500000
```

### Example 2: low margin, and the DGI classification (decision)

Same gross income, renta neta only C$500,000. IR is C$150,000, but the PMD decides: C$400,000 as an other taxpayer, C$800,000 if DGI classifies the company as a principal taxpayer, C$1,200,000 as a large taxpayer. At a 1.25% net margin the PMD, not profit, sets the tax; check the classification letter and art. 59 exceptions before budgeting.

```oa-check
name: NI 2026 PMD bites at low margin
inputs:
  gross: 40000000
  net: 500000
steps:
  - ir: net * 0.30
  - pmd_other: gross * 0.01
  - pmd_principal: gross * 0.02
  - pmd_large: gross * 0.03
  - payable_other: max(ir, pmd_other)
  - payable_principal: max(ir, pmd_principal)
expected:
  ir: 150000
  pmd_other: 400000
  pmd_principal: 800000
  pmd_large: 1200000
  payable_other: 400000
  payable_principal: 800000
```

## Ask the client first

1. DGI classification: large, principal or other taxpayer? Gross income for the year?
2. Date operations started and whether they came from new investment (PMD exception).
3. Renta neta from the 2026 accounts and any exempt or capital income.
4. Advances paid and retentions suffered (2%, 1.5%, 10%).
5. Payments to non-residents and any related party in a tax haven.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for Ley 987 (La Gaceta 41, 28 Feb 2019): reformed arts. 32.5, 34, 38, 39.15, 41.1, 49, 53.3, 59, 61, 61 bis, 62, 63, 69.1, 87 | https://www.mem.gob.ni/wp-content/uploads/2023/08/2019.02.28-Ley-987-Reforma-a-Ley-822-G-41.pdf | 2026-11-14 |
| Read for DGI FAQ, Liquidacion del impuesto: 30% rate, C$12,000,000 threshold, higher of IR and PMD, order of credits | https://www.dgi.gob.ni/FAQ/liquidacion_del_impuesto.htm | 2026-11-14 |
| Read for DGI FAQ, Anticipos a cuenta: monthly advance due by the 15th, nil returns | https://www.dgi.gob.ni/FAQ/anticipos_a_cuenta.htm | 2026-11-14 |
| Read for DGI FAQ, Pago minimo definitivo: who pays, exceptions (its 1% rate predates Ley 987) | https://www.dgi.gob.ni/FAQ/pago_minimo_definitivo.htm | 2026-11-14 |
| Read for DGI catalogue of retention codes and rates, Aviso 005-01-2024 | https://www.dgi.gob.ni/pdfNoticia/3175 | 2026-11-14 |
| Read for DGI FAQ, Infracciones, sanciones y delitos: CTr arts. 124 and 127 | https://www.dgi.gob.ni/FAQ/infracciones__sanciones_y_deli.htm | 2026-11-14 |

Not yet confirmed: the art. 52 progressive table for taxpayers up to C$12,000,000; the criteria for large and principal taxpayer status; late payment surcharges; transfer pricing; any reform of Ley 822 after Ley 987.
