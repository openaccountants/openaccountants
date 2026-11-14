---
name: hn-corporate-income-tax
description: "Use this skill for Honduras corporate income tax (Impuesto Sobre la Renta of personas juridicas) for tax year 2026. It gives the 25% rate of art. 22(a), the 5% solidarity contribution on renta neta gravable above L1,000,000, the 1% tax on net total assets above L3,000,000, the art. 22-A minimum tax of 1% of gross income for groups with prior year gross income above L1,000,000,000 (0.5% for listed sectors), the 1% advance for repeated losses, the 10% deemed base for foreign transport companies, dividend and branch withholding, pagos a cuenta and Form 103 filed through the SAR Oficina Virtual by 30 April. Trigger phrases include ISR persona juridica, Formulario 103, aportacion solidaria, activo total neto, impuesto minimo 1% ingresos brutos and SAR Honduras."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/hn-corporate-income-tax"
  jurisdiction: "HN"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Honduras corporate income tax, tax year 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Honduran accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Honduras.

## Who this applies to

Legal persons (personas juridicas) domiciled in Honduras: sociedades anonimas, sociedades de responsabilidad limitada, branches of foreign companies and other mercantile entities with Honduran-source income, for the calendar year 2026 or an approved special period (LISR art. 27). Honduras taxes Honduran-source income only.

Out of scope, refer: entities in the export, free zone (ZOLI), ZOLITUR or tourism regimes (exempt from the solidarity contribution and with their own rules); cooperatives and the social sector of the economy (Decreto 131-2018); financial sector special contributions; transfer pricing documentation (Ley de Regulacion de Precios de Transferencia, Decreto 232-2011, and the annual Form 545 return, not read in this pass). Individuals use [honduras-income-tax](honduras-income-tax.md); sales tax [honduras-isv](honduras-isv.md); entity choice and registration [hn-company-formation](hn-company-formation.md).

## Rates, bands and thresholds

| Item | Rate or amount | Condition | Source |
| --- | --- | --- | --- |
| Corporate income tax, art. 22(a) | 25% of renta neta gravable | All domiciled legal persons | SAR Generalidades 30 de abril (June 2026): https://www.sar.gob.hn/download/generalidades-impuestos-con-vencimiento-al-30-de-abril/?wpdmdl=23287 |
| Solidarity contribution (aportacion solidaria) | 5% of renta neta gravable above L1,000,000 | Legal persons except export and tourism regimes; a surtax, not deductible, under pagos a cuenta | same |
| Tax on net total assets (activo total neto) | 1% of net total assets above L3,000,000 | Payable only to the extent it exceeds ISR plus solidarity contribution, which are a credit against it | same |
| Minimum tax on gross income, art. 22-A(3)(b) | 1% of gross income | Prior-year gross income above L1,000,000,000 and art. 22 tax lower than 1% of gross income | same |
| Reduced minimum tax, listed sectors | 0.5% of gross income | Cement, steel for construction, state public services, human medicines, bakery, coffee | same |
| Advance for repeated losses (Decreto 96-2012) | 1% of gross income | Operating losses in two non-prescribed years and gross income of L100,000,000 or more in the last year | SAR Ayuda Form 102 (2026): https://www.sar.gob.hn/download/ayuda-declaracion-jurada-impuesto-sobre-la-renta-102/?wpdmdl=22532 |
| Foreign air, land and sea transport companies, art. 22(c) | Deemed base of 10% of Honduran-source gross income, taxed at 25% | Companies constituted abroad operating in Honduras | SAR LISR consolidated text: https://www.sar.gob.hn/download/ley-isr-texto-consolidado-hasta-el-acuerdo-no-sar-014-2023/?wpdmdl=17388 |
| Dividends paid to residents, art. 25 | 10%, retained and paid by the company | Capitalisation of reserves or profits is exempt | same |
| Branch, subsidiary and agency profits of foreign companies, art. 5(4) | 10% | Withheld | same |
| Dividends to non-residents, art. 5(5) | 10% | Withheld | same |
| Interest to non-residents, art. 5(7) | 10% | Withheld | same |
| Royalties for patents, trademarks and copyright to non-residents, art. 5(6) | 25% | Withheld | same |
| Fees and pay for services of non-residents, art. 5(3) | 25% | Withheld | same |
| Retention on fees, commissions and technical services paid to residents, art. 50 | 12.5% | Not for payees in the pagos a cuenta regime; paid within 10 days of the following month | same |
| Capital gains, art. 10 | 10% single tax | Not on the 25% rate | same |
| Bad debt reserve deduction (art. 12 g) | Up to 1% of credit sales | Conditions in art. 12 | same |

## The base

1. **Renta bruta (art. 10):** all Honduran-source income in money or kind. Capital gains go to the 10% single tax; dividends received from other Honduran companies bear the 10% retention and are excluded from the 25% base.
2. **Deductions (art. 12 and art. 119 of the regulation as cited by SAR):** ordinary and necessary costs of producing taxable income in the period, documented, paid or accrued. Books follow the Ley sobre Normas de Contabilidad y de Auditoria (art. 30); importers keep a cost book; inventory records are mandatory (art. 30-A).
3. **Renta neta gravable** x 25% = ISR. Add 5% of the excess over L1,000,000 (solidarity).
4. **Compare** with art. 22-A (only above L1,000,000,000 of prior-year gross income): the higher of the art. 22 tax and 1% (or 0.5%) of gross income.
5. **Activo total neto:** total assets less the deductions the form allows (accumulated depreciation, provisions), less L3,000,000, x 1%. Pay only the excess over ISR plus solidarity.
6. **Credits:** pagos a cuenta, 1% advances, art. 50 retentions suffered, import advances and prior-year excess, as listed in the SAR current account.

Each year is settled on its own (art. 30); SAR may rebuild income from indicators when books are irregular (art. 31).

## Deadlines and filing

| Obligation | Channel | Deadline |
| --- | --- | --- |
| Informe de Estado de Situacion Financiera (Form 535) | Oficina Virtual (OVI) | Before Form 103; same 30 April window |
| Form 103, ISR, Activo Neto and Aportacion Solidaria, Persona Juridica (determinativa) | OVI only (Acuerdo SAR-236-2024) | 1 January to 30 April 2027 for 2026; special periods within three months of year end |
| Pagos a cuenta 2026 | Each a quarter of the prior year's tax | 30 June, 30 September, 31 December 2026; the balance with the return |
| Manifestacion de pagos a cuenta for 2027 | With the return or in December | Last month of the year; new companies within 30 days of starting |
| Retentions (art. 50, art. 5, dividends) | Declaracion mensual de retenciones (DMR) | Within the first 10 calendar days of the following month |
| Transfer pricing informative return (Form 545) | OVI | See Not yet confirmed |

Accounts attached to the return are certified by a Honduran accountant (art. 28).

## Penalties and interest

| Default | Charge |
| --- | --- |
| ISR return late or missing (CT art. 160.2) | 5%, 10%, 15%, 20% of the tax for months 1 to 4, 25% from month 5, proportional to days, not cumulative |
| Late payment of tax or pagos a cuenta (CT art. 163.1) | 3% interest a month or part, up to 36% |
| Retained tax not remitted (CT art. 163.2) | 5% interest a month or part, up to 60% |
| Formal faults (CT art. 160.1) | By gross income band: 10% of one average minimum wage up to L250,000; one wage for L1,000,000.01 to L5,000,000; ten wages above L50,000,000, plus 1% of a wage per L500,000 above L100,000,000 |
| Voluntary correction (CT art. 162) | Penalty reduced 50%, 30% or 10% depending on timing |

Source for all: the Codigo Tributario consolidated text in Sources. The average minimum wage for 2026 is L14,917.20 (see [honduras-payroll](honduras-payroll.md)).

## Cross-border points

Payments abroad bear the art. 5 final withholding (rates above); the payer retains and is jointly liable (art. 51). A Honduran branch pays 25% plus solidarity on its own profits and 10% on profits transferred. Foreign transport companies use the 10% deemed base. Related-party transactions with non-residents fall under the transfer pricing law and Form 545. No comprehensive double tax treaty was confirmed on an official page in this pass.

## Two worked examples that recompute

### Example 1: trading company, 2026

Renta neta gravable L5,000,000, net total assets L20,000,000, prior-year gross income well below L1,000,000,000. ISR L1,250,000, solidarity L200,000, total L1,450,000. Activo neto L170,000 is below that, so no activo neto is payable.

```oa-check
name: HN 2026 company, ISR, solidarity and net assets test
inputs:
  rng: 5000000
  net_assets: 20000000
steps:
  - isr: rng * 0.25
  - solidarity: (rng - 1000000) * 0.05
  - total_income_tax: isr + solidarity
  - activo_neto: (net_assets - 3000000) * 0.01
  - activo_neto_payable: max(activo_neto - total_income_tax, 0)
  - total_due: total_income_tax + activo_neto_payable
expected:
  isr: 1250000
  solidarity: 200000
  total_income_tax: 1450000
  activo_neto: 170000
  activo_neto_payable: 0
  total_due: 1450000
```

### Example 2: low-margin, asset-heavy company, which tax bites (decision)

Renta neta gravable L200,000 and net total assets L40,000,000. ISR is L50,000 and there is no solidarity contribution (below L1,000,000). Activo neto is L370,000, so L320,000 more is payable as activo neto. The figure that decides it: net assets above L3,000,000 times 1% against 25% of profit. Here the company would need renta neta gravable of L1,480,000 before ISR alone covered the activo neto charge.

```oa-check
name: HN 2026 asset-heavy company, activo neto exceeds ISR
inputs:
  rng: 200000
  net_assets: 40000000
steps:
  - isr: rng * 0.25
  - solidarity: max(rng - 1000000, 0) * 0.05
  - activo_neto: (net_assets - 3000000) * 0.01
  - extra_activo_neto: max(activo_neto - isr - solidarity, 0)
  - total_due: isr + solidarity + extra_activo_neto
  - profit_to_cover: activo_neto / 0.25
expected:
  isr: 50000
  solidarity: 0
  activo_neto: 370000
  extra_activo_neto: 320000
  total_due: 370000
  profit_to_cover: 1480000
```

The L1,480,000 assumes no solidarity contribution; above L1,000,000 the solidarity contribution also counts, so the true break-even is slightly lower.

## Ask the client first

1. Legal form, RTN, date of incorporation and whether any special regime (ZOLI, ZOLITUR, export, tourism) applies.
2. Renta neta gravable from the 2026 accounts, and the 2025 gross income (for art. 22-A and the 1% loss advance).
3. Net total assets at 31 December 2026, with depreciation and provisions.
4. Pagos a cuenta paid in 2026, retentions suffered, and the prior years' operating results.
5. Payments to non-residents (dividends, interest, royalties, services) and related-party transactions.
6. Dividends declared in 2026 and whether the 10% was retained and paid.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for SAR Generalidades impuestos con vencimiento al 30 de abril (June 2026): art. 22 rate, art. 22-A, solidarity contribution, activo total neto, Form 103 | https://www.sar.gob.hn/download/generalidades-impuestos-con-vencimiento-al-30-de-abril/?wpdmdl=23287 | 2026-11-14 |
| Read for SAR Ayuda Form 103 (2026), the solidarity calculation, the L3,000,000 net assets exemption, the activo neto credit rule and credits | https://www.sar.gob.hn/download/ayuda-declaracion-jurada-impuesto-sobre-la-renta-activo-neto-y-aportacion-solidaria-perona-juridica-codigo-103/?wpdmdl=21833 | 2026-11-14 |
| Read for SAR Ayuda Form 102 (2026), the Decreto 96-2012 1% advance for repeated losses | https://www.sar.gob.hn/download/ayuda-declaracion-jurada-impuesto-sobre-la-renta-102/?wpdmdl=22532 | 2026-11-14 |
| Read for LISR consolidated text to Acuerdo SAR-014-2023, arts. 5, 10, 12, 22, 22-A, 25, 27 to 31, 34, 50 and 51 | https://www.sar.gob.hn/download/ley-isr-texto-consolidado-hasta-el-acuerdo-no-sar-014-2023/?wpdmdl=17388 | 2026-11-14 |
| Read for Codigo Tributario Decreto 170-2016 consolidated, arts. 160, 162 and 163 | https://www.sar.gob.hn/download/texto-consolidado-codigo-tributario-decreto-170-2016-segun-fe-de-errata-publicada-en-la-gaceta-de-fecha-25-de-mayo-del-2017-y-los-decretos-25-2017-7-2017-32-2017-93-2017-98-2018-55-2019-170-2/?wpdmdl=6987 | 2026-11-14 |
| Read for the SAR ISR page, forms 103, 535 and 545 | https://www.sar.gob.hn/impuesto-sobre-renta-isr/ | 2026-11-14 |

Not yet confirmed: transfer pricing rules and the Form 545 deadline (Decreto 232-2011 not read); the exact list of deductions allowed in computing activo total neto; the art. 12 deduction list beyond the 1% bad debt reserve; whether any LISR reform after 2023 changed the rates; treaty or exchange agreements in force; the municipal industry and commerce tax (Ley de Municipalidades, not read).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `hn-corporate-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/hn-corporate-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
