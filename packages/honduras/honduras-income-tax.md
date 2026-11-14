---
name: honduras-income-tax
description: >
  Use this skill for Honduras personal income tax (Impuesto Sobre la Renta, ISR) of
  resident individuals and self-employed professionals for tax year 2026. It gives the
  SAR 2026 progressive scale (exempt to L228,324.32, then 15%, 20% and 25%), the art. 13
  deductions (L40,000 flat, L80,000 over 65), the 13th and 14th month exemption, the 10%
  dividend and capital gains taxes, the 10% housing rent tax, the 12.5% art. 50 retention
  on fees, the four pagos a cuenta, filing of Form 102 by 30 April and the Codigo
  Tributario penalties. Trigger phrases include ISR Honduras, Declaracion Jurada 102,
  tabla progresiva 2026, renta neta gravable, pagos a cuenta, retencion 12.5% honorarios
  and SAR Oficina Virtual. Companies go to hn-corporate-income-tax; employer withholding
  to honduras-payroll.
version: "1.0"
jurisdiction: HN
tax_year: 2026
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
depends_on:
  - income-tax-workflow-base
---

# Honduras personal income tax (ISR), individuals, tax year 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Honduran accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Honduras.

## Who this applies to

Individuals (personas naturales) domiciled in Honduras who earn Honduran-source income from work, a profession, a trade, rents or capital, for the calendar tax year 2026 (1 January to 31 December, LISR art. 27). Honduras taxes Honduran-source income: art. 5 taxes non-residents only on Honduran-source gross income, at the flat rates in Cross-border points below.

In scope: salaried individuals with more than one source, self-employed professionals and comerciantes individuales, landlords, recipients of dividends and capital gains.

Out of scope, refer:

- **R-HN-1 Domicile unknown.** Non-domiciled persons pay the art. 5 flat rates by withholding and do not use the scale. Do not compute until domicile is confirmed.
- **R-HN-2 Legal persons.** Companies file Form 103 and pay 25% plus the solidarity contribution: use [hn-corporate-income-tax](hn-corporate-income-tax.md).
- **R-HN-3 Special regimes.** Export, free zone (ZOLI, ZOLITUR), tourism and other exempt regimes have their own rules. Refer to a Honduran accountant.
- **R-HN-4 Capital gains computation.** The 10% single tax applies (art. 10), but basis and proceeds need specialist work. Flag and refer.
- **R-HN-5 Arrears or SAR enforcement.** Refer immediately; do not advise on settlement.
- **R-HN-6 Sales tax (ISV).** Use [honduras-isv](honduras-isv.md).

Conservative defaults when a fact is missing:

| Ambiguity | Default |
| --- | --- |
| Domicile unknown | Stop (R-HN-1) |
| Business use share of a vehicle, phone or home unknown | 0% deductible until documented |
| Expense without a factura bearing the supplier's RTN | Not deductible |
| Source of a receipt unclear (foreign client, platform) | Treat as Honduran-source until the place of service is confirmed |
| Gross income of the prior year above L1,000,000,000 | Flag the art. 22-A minimum tax for review |
| Fees received from a legal person | Assume 12.5% was retained unless the client is in pagos a cuenta |
| Pagos a cuenta or ISR paid | A credit against the final tax, never an expense |

Red flags: deductions over half of gross fees, rent received in cash without receipts, fees from abroad booked as exempt, pagos a cuenta not paid for the previous year, a Form 102 not filed although gross income exceeded the exempt amount, ISV collected on sales booked as income.

## Rates, bands and thresholds

**Progressive scale, art. 22(b), tax year 2026 (annual renta neta gravable, HNL).** SAR adjusted the scale by 4.98% (2025 interannual CPI) under Acuerdo SAR-01-2026, La Gaceta 37,051 of 23 January 2026. Employers use the same table for monthly withholding from 1 January 2026.

| Band | From (L) | To (L) | Rate | Source |
| --- | --- | --- | --- | --- |
| 1 | 0.01 | 228,324.32 | Exempt | SAR Acuerdo SAR-01-2026: https://www.sar.gob.hn/download/acuerdo-numero-sar-01-2026-publicado-en-fecha-23-de-enero-del-2026-en-la-gaceta-no-37051/?wpdmdl=22954 |
| 2 | 228,324.33 | 348,154.10 | 15% | same |
| 3 | 348,154.11 | 809,660.75 | 20% | same |
| 4 | 809,660.76 | and above | 25% | same |

Tax at the top of band 2 is L17,974.47 and at the top of band 3 L110,275.80 (computed: 119,829.78 x 15%; plus 461,506.65 x 20%).

**Tax year 2025 scale (for 2025 returns filed in 2026).** Acuerdo SAR-07-2025, La Gaceta 36,735 of 9 January 2025.

| Band | From (L) | To (L) | Rate | Source |
| --- | --- | --- | --- | --- |
| 1 | 0.01 | 217,493.16 | Exempt | SAR Acuerdo SAR-07-2025: https://www.sar.gob.hn/download/acuerdo-numero-sar-07-2025-publicado-en-fecha-9-de-enero-del-2025-en-la-gaceta-no-36735/?wpdmdl=22996 |
| 2 | 217,493.17 | 331,638.50 | 15% | same |
| 3 | 331,638.51 | 771,252.38 | 20% | same |
| 4 | 771,252.39 | and above | 25% | same |

**Other amounts and rates for individuals.**

| Item | Amount or rate | Condition | Source |
| --- | --- | --- | --- |
| Flat deduction for education and medical fees (art. 13 a) | L40,000 a year | No receipts needed; services from professionals resident in Honduras | SAR Ayuda Form 102 (2026): https://www.sar.gob.hn/download/ayuda-declaracion-jurada-impuesto-sobre-la-renta-102/?wpdmdl=22532 |
| Same deduction, taxpayer over 65 | L80,000 a year | Art. 13 a) as reformed by Decreto 59-2020 | same |
| Donations (art. 13 d) | Up to 10% of renta neta gravable | Legally recognised state, municipal, educational, charitable or sports bodies | same |
| 13th month (aguinaldo) and 14th month salary | Exempt up to 10 average minimum wages each | Art. 10 h); the excess is taxable | same |
| Average minimum wage 2026 (salario minimo promedio) | L14,917.20 a month | So the 2026 exempt cap is L149,172.00 for each of the 13th and 14th month | Secretaria de Trabajo, Tabla 2026: https://www.trabajo.gob.hn/wp-content/uploads/2026/05/TABLA-SALARIO-MINIMO-2026-.pdf |
| Dividends and profit shares received by residents (art. 25) | 10% single tax, retained by the company | Excluded from the scale | SAR LISR consolidated text: https://www.sar.gob.hn/download/ley-isr-texto-consolidado-hasta-el-acuerdo-no-sar-014-2023/?wpdmdl=17388 |
| Capital gains (art. 10) | 10% single tax | Domiciled or not; not on the scale | same |
| Retention on fees, commissions and technical services paid by legal persons (art. 50) | 12.5% | Not applied to persons in the pagos a cuenta regime; remitted within 10 days of the following month | same |
| Gross income below which a domiciled individual need not file (art. 28) | L199,039.47 in the 2023 text | The law says amounts tied to the scale are adjusted with it; see Not yet confirmed | same |
| Pagos a cuenta below which one single payment is made | L200 a year | Paid by 30 November | same |
| Housing rent received by individuals (Decreto 17-2010 art. 5) | 10% single cedular tax | Rent above L15,000 a month | SAR Ayuda Form 102 (2026): https://www.sar.gob.hn/download/ayuda-declaracion-jurada-impuesto-sobre-la-renta-102/?wpdmdl=22532 |
| Minimum tax on gross income (art. 22-A, 3) | 1% of gross income (0.5% for listed sectors) | Only if gross income of the prior year exceeded L1,000,000,000 and the scale gives less; salary earners excluded | SAR Generalidades 30 de abril (June 2026): https://www.sar.gob.hn/download/generalidades-impuestos-con-vencimiento-al-30-de-abril/?wpdmdl=23287 |

The solidarity contribution (5% over L1,000,000) is charged on legal persons only: SAR's June 2026 guide opens "Las personas juridicas ... pagaran una Aportacion Solidaria del 5%". It does not apply to an individual's Form 102.

## The base

1. **Gross income (renta bruta, art. 10).** All Honduran-source receipts in money or kind: salary, fees, business income, rent and interest. Dividends (10%), capital gains (10%) and housing rent above L15,000 a month (10%) are taxed separately and stay out of the scale.
2. **Exempt items (art. 10 h).** Labour severance benefits, vacation bonus up to 30 extra days, pensions and the 13th and 14th month up to 10 average minimum wages each. Contributions to the institutions paying these benefits are deductible, which is how SAR's Form 102 guide lets RAP contributions of 1.5% in.
3. **Deductions (art. 13).** The flat L40,000 (L80,000 over 65) for education and medical fees, without receipts; documented costs of a profession, art, trade or workshop; farm costs for farmers and ranchers; donations up to 10% of renta neta gravable. A business expense needs a valid factura with the supplier's RTN. Mixed-use costs (home office, vehicle, phone) are deductible only for the documented business share. Private living costs, fines and surcharges, ISR itself and drawings are never deductible.
4. **Renta neta gravable** = gross taxable income less exempt items and deductions. Apply the 2026 scale.
5. **Credits.** Art. 50 retentions (12.5%) suffered, pagos a cuenta paid and other retentions shown in the SAR current account reduce the tax due on Form 102.
6. **Minimum tax.** Only for a person whose prior-year gross income exceeded L1,000,000,000: pay 1% of gross income if the scale gives less. Salary earners are outside art. 22-A.

Each tax year stands alone (art. 30): results of earlier or later years do not offset. A bad debt is deductible only if the income was declared before, recovery was attempted and the debt is truly lost. ISV collected on sales belongs to SAR and is not income; input ISV of a non-registered person is part of the cost.

## Deadlines and filing

| Obligation | Form or channel | Deadline | Source |
| --- | --- | --- | --- |
| Annual return, persona natural | Declaracion Jurada ISR Persona Natural, Form 102, Oficina Virtual (OVI) | 1 January to 30 April 2027 for tax year 2026 (next working day if a holiday) | LISR art. 28; SAR Ayuda Form 102 |
| Pagos a cuenta for 2026 | Three quarterly quotas, each a quarter of the prior year's tax | 30 June, 30 September and 31 December 2026; the fourth is the balance with the return by 30 April 2027 | LISR art. 34 |
| Manifestacion de pagos a cuenta for 2027 | Declared in the last month of the year | December 2026; new taxpayers within 30 days of starting | LISR art. 29 |
| Art. 50 retention suffered | Credit on Form 102 | With the return | LISR art. 50 |
| Notice of suspension | Escrito de notificacion de suspension, for those below the exempt amount who filed before | Before 30 April | SAR ISR page |

Who need not file (art. 28): a domiciled individual whose gross income does not exceed the exempt amount, and a salary earner with a single employer whose ISR was fully withheld. Anyone else with Honduran income files Form 102. Businesses attach a balance sheet and income statement certified by a Honduran accountant.

## Penalties and interest

| Default | Charge | Source |
| --- | --- | --- |
| ISR return filed late or not filed (CT art. 160.2) | 5% of the tax in month 1, 10% month 2, 15% month 3, 20% month 4, 25% month 5 onward, in proportion to days, not cumulative | Codigo Tributario consolidated text |
| Late payment of tax or pagos a cuenta (CT art. 163.1) | 3% interest a month or part month, up to 36% | same |
| Retained tax not remitted by an agent (CT art. 163.2) | 5% interest a month or part month, up to 60% | same |
| Formal faults (CT art. 160.1) | From 10% of one average minimum wage (gross income up to L250,000) up to 10 average minimum wages and more | same |
| Voluntary regularisation (CT art. 162) | Penalty cut by 50% before any SAR action, 30% after action but before notice, 10% before judicial demand; small taxpayers a further 20% | same |

A missing Manifestacion de pagos a cuenta is fined as a late return (LISR art. 29).

## Cross-border points

Non-residents and non-domiciled persons pay a final tax on Honduran-source gross income, withheld by the payer (LISR art. 5): 25% on rents of movable or immovable property, mining royalties, salaries, fees and other pay for services, royalties for patents, trademarks and copyright, public shows and films; 10% on branch and subsidiary profits, dividends, interest, transport, telecoms and software, insurance premiums and any other income not listed. The payer retains under arts. 50 and 51 and is jointly liable if it does not.

A person in Honduras only temporarily may file before leaving and ask SAR to settle (art. 4). Non-residents who must file get up to three extra months (art. 28). Foreign-source income of a resident is outside the territorial base, but source is a question of where the service is rendered and used: confirm before excluding.

Treaties: no comprehensive double tax treaty was confirmed on an official page in this pass (see Not yet confirmed).

## Two worked examples that recompute

### Example 1: self-employed engineer, tax year 2026

Gross fees L900,000, documented professional costs L250,000, flat art. 13 deduction L40,000. Renta neta gravable L610,000, in band 3. Tax L70,343.65.

```oa-check
name: HN 2026 self-employed professional, three bands
inputs:
  gross: 900000
  costs: 250000
  flat_deduction: 40000
  top1: 228324.32
  top2: 348154.10
  top3: 809660.75
steps:
  - net: gross - costs - flat_deduction
  - band15: (min(net, top2) - top1) * 0.15
  - band20: (min(net, top3) - top2) * 0.20
  - tax: round(band15 + band20, 2)
expected:
  net: 610000
  tax: 70343.65
```

### Example 2: fees from companies, retention or pagos a cuenta (decision)

A consultant bills L600,000 to Honduran companies, has costs of L150,000 and takes the L40,000 deduction. Net L410,000, tax L30,343.65.

- **Route A, retention.** Clients retain 12.5%, L75,000. The retention exceeds the tax by L44,656.35, which the consultant recovers only through the return, after 30 April.
- **Route B, pagos a cuenta.** Retentions do not apply to persons in the pagos a cuenta regime (art. 50). With a prior-year tax of L28,000, the three quotas are L7,000 each (L21,000 during 2026) and the balance at 30 April is L9,343.65.

The figure that decides it is the gap between 12.5% of fees and the real tax. Route B keeps L54,000 more cash in the consultant's hands during the year (L75,000 less L21,000).

```oa-check
name: HN 2026 fees, art. 50 retention against pagos a cuenta
inputs:
  fees: 600000
  costs: 150000
  flat_deduction: 40000
  prior_year_tax: 28000
  top1: 228324.32
  top2: 348154.10
steps:
  - net: fees - costs - flat_deduction
  - tax: round((top2 - top1) * 0.15 + (net - top2) * 0.20, 2)
  - retention: fees * 0.125
  - refund_route_a: round(retention - tax, 2)
  - quotas_in_year: prior_year_tax / 4 * 3
  - balance_route_b: round(tax - quotas_in_year, 2)
  - cash_kept: retention - quotas_in_year
expected:
  net: 410000
  tax: 30343.65
  retention: 75000
  refund_route_a: 44656.35
  quotas_in_year: 21000
  balance_route_b: 9343.65
  cash_kept: 54000
```

## Ask the client first

1. **Domicile.** Are you domiciled in Honduras, and since when? If not, the art. 5 flat rates apply instead.
2. **Sources.** Salary from one employer only, or also fees, a business, rents, dividends or sales of assets?
3. **RTN and regime.** What is your RTN, and are you registered for pagos a cuenta or do your clients retain 12.5%?
4. **Credits.** What did you pay in pagos a cuenta for 2026 and what retentions appear in your SAR current account?
5. **Deductions.** Are you over 65? Which professional costs do you hold facturas for, what share of home, vehicle and phone is business use, and any donations?
6. **Size.** Did your gross income for 2025 exceed L1,000,000,000 (art. 22-A)?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for the 2026 progressive scale and the 4.98% adjustment, Acuerdo SAR-01-2026, La Gaceta 37,051, arts. primero and segundo | https://www.sar.gob.hn/download/acuerdo-numero-sar-01-2026-publicado-en-fecha-23-de-enero-del-2026-en-la-gaceta-no-37051/?wpdmdl=22954 | 2026-11-14 |
| Read for the 2025 progressive scale, Acuerdo SAR-07-2025, La Gaceta 36,735 | https://www.sar.gob.hn/download/acuerdo-numero-sar-07-2025-publicado-en-fecha-9-de-enero-del-2025-en-la-gaceta-no-36735/?wpdmdl=22996 | 2026-11-14 |
| Read for LISR consolidated text to Acuerdo SAR-014-2023, arts. 2, 4, 5, 10, 13, 22, 22-A, 25, 27 to 30, 34, 50 and 51 | https://www.sar.gob.hn/download/ley-isr-texto-consolidado-hasta-el-acuerdo-no-sar-014-2023/?wpdmdl=17388 | 2026-11-14 |
| Read for SAR Ayuda Form 102 (updated August 2026), the art. 13 deductions, 13th and 14th month cap, RAP 1.5% deduction, housing rent 10% above L15,000 and the 30 April deadline | https://www.sar.gob.hn/download/ayuda-declaracion-jurada-impuesto-sobre-la-renta-102/?wpdmdl=22532 | 2026-11-14 |
| Read for SAR Generalidades impuestos con vencimiento al 30 de abril (June 2026), art. 22-A minimum tax and the solidarity contribution on legal persons | https://www.sar.gob.hn/download/generalidades-impuestos-con-vencimiento-al-30-de-abril/?wpdmdl=23287 | 2026-11-14 |
| Read for Codigo Tributario Decreto 170-2016 consolidated, arts. 160, 162 and 163 | https://www.sar.gob.hn/download/texto-consolidado-codigo-tributario-decreto-170-2016-segun-fe-de-errata-publicada-en-la-gaceta-de-fecha-25-de-mayo-del-2017-y-los-decretos-25-2017-7-2017-32-2017-93-2017-98-2018-55-2019-170-2/?wpdmdl=6987 | 2026-11-14 |
| Read for the 2026 minimum wage table and the salario minimo promedio, Acuerdo SETRASS-233-2026 | https://www.trabajo.gob.hn/wp-content/uploads/2026/05/TABLA-SALARIO-MINIMO-2026-.pdf | 2026-11-14 |
| Read for the SAR ISR page, list of 2026 forms and the notice of suspension | https://www.sar.gob.hn/impuesto-sobre-renta-isr/ | 2026-11-14 |

Not yet confirmed: the indexed 2026 figure for the art. 28 filing exemption (the 2023 text shows L199,039.47 and says amounts tied to the scale move with it; L228,324.32 is the inference, not a published figure); the art. 50 retention exemption amount for 2026 (L239,039.47 in the 2023 text); any amendment to the LISR after Acuerdo SAR-014-2023 other than the scale; whether housing rent of L15,000 a month or less is exempt or goes on the scale; the list of tax information exchange or double tax agreements in force; ZOLI, ZOLITUR and other special regimes.
