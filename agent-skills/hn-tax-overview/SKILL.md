---
name: hn-tax-overview
description: "Use this skill for a first map of the Honduras tax system in 2026 and to route a question to the right Honduras skill. It names the authority (SAR), the territorial basis, the calendar tax year, the headline 2026 figures with their official sources (individual scale exempt to L228,324.32 then 15%, 20%, 25%; companies 25% plus 5% solidarity above L1,000,000; ISV 15% and 18%; 10% on dividends and capital gains), the 30 April return and the monthly returns, and which skill owns each job. Trigger phrases include Honduras taxes overview, impuestos Honduras, SAR Honduras and what taxes apply in Honduras."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/hn-tax-overview"
  jurisdiction: "HN"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Honduras tax overview, 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Honduran accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Honduras.

## Who this applies to

Anyone starting a Honduras question: individuals, companies, employers and foreign investors. The tax authority is the Servicio de Administracion de Rentas (SAR, www.sar.gob.hn); filing runs through its Oficina Virtual (OVI). The currency is the lempira (L, HNL). The tax year is the calendar year (LISR art. 27). Honduras taxes Honduran-source income: non-residents pay only on Honduran-source gross income (LISR art. 5).

Which skill owns which job:

| Job | Skill |
| --- | --- |
| Individual income tax, Form 102 | [honduras-income-tax](honduras-income-tax.md) |
| Company income tax, solidarity contribution, net assets, Form 103 | [hn-corporate-income-tax](hn-corporate-income-tax.md) |
| Sales tax (ISV) | [honduras-isv](honduras-isv.md) |
| Employer withholding, 13th and 14th month, minimum wage | [honduras-payroll](honduras-payroll.md) |
| IHSS and RAP | [honduras-social-contributions](honduras-social-contributions.md) |
| Forming a company and getting an RTN | [hn-company-formation](hn-company-formation.md) |

## Rates, bands and thresholds

Headline figures only; each owning skill holds the conditions.

| Item | 2026 figure | Source |
| --- | --- | --- |
| Individual scale, exempt band | L0.01 to L228,324.32 | SAR Acuerdo SAR-01-2026: https://www.sar.gob.hn/download/acuerdo-numero-sar-01-2026-publicado-en-fecha-23-de-enero-del-2026-en-la-gaceta-no-37051/?wpdmdl=22954 |
| Individual scale, top rate | 25% above L809,660.75 | same |
| Corporate income tax | 25% | SAR Generalidades 30 de abril (June 2026): https://www.sar.gob.hn/download/generalidades-impuestos-con-vencimiento-al-30-de-abril/?wpdmdl=23287 |
| Solidarity contribution, legal persons | 5% of renta neta gravable above L1,000,000 | same |
| Net total assets tax | 1% above L3,000,000 | same |
| ISV general rate | 15% | SAR LISV consolidated text: https://www.sar.gob.hn/download/texto-consolidado-ley-del-impuesto-sobre-ventas-decreto-ley-numero-24-actualizado-hasta-el-decreto-legislativo-no-59-2022/?wpdmdl=15324 |
| ISV increased rate | 18% on alcoholic drinks, cigarettes and air tickets above economy | same |
| Dividends and capital gains | 10% single tax | SAR LISR consolidated text: https://www.sar.gob.hn/download/ley-isr-texto-consolidado-hasta-el-acuerdo-no-sar-014-2023/?wpdmdl=17388 |
| Non-resident withholding | 10% or 25% by type of income | same |

## The base

- **Income tax (ISR):** individuals on the progressive scale after art. 13 deductions; companies at 25% of renta neta gravable plus solidarity, compared with 1% of net assets and, for the largest groups, 1% of gross income (art. 22-A).
- **ISV:** debit less credit on sales and imports, with an exemption list in LISV art. 15.
- **Payroll:** ISR withheld monthly; IHSS and RAP contributions.
- **Other taxes not covered by a skill here:** municipal taxes (industry and commerce, personal tax), customs duties, the tourism tax, the financial transactions contribution and the production and consumption tax.

## Deadlines and filing

| Return | Deadline |
| --- | --- |
| ISR annual return (Forms 102 and 103) for 2026 | 30 April 2027 |
| ISR pagos a cuenta | 30 June, 30 September, 31 December |
| ISV monthly return | First 10 calendar days of the following month |
| Retentions (salaries, fees, non-residents) | First 10 calendar days of the following month |
| ISV simplified regime annual return | 31 January |

## Penalties and interest

Codigo Tributario (Decreto 170-2016): late ISR return 5% to 25% of the tax by month of delay (art. 160.2); late ISV return 1% then 2% a month up to 24% (art. 160.4); late payment interest 3% a month up to 36%; retained tax not remitted 5% a month up to 60% (art. 163). Details in the owning skills.

## Cross-border points

Payments to non-residents bear final withholding under LISR art. 5 (25% on services, rents and royalties; 10% on dividends, interest, branch profits and other income). Exports are zero rated for ISV. No comprehensive double tax treaty was confirmed in this pass.

## Two worked examples that recompute

### Example 1: a Honduran company pays a dividend of L1,000,000 to a resident shareholder

The company retains 10% (L100,000) and pays it to SAR; the shareholder receives L900,000 and does not put the dividend on the scale (LISR art. 25).

```oa-check
name: HN 2026 dividend to a resident shareholder
inputs:
  dividend: 1000000
steps:
  - retention: dividend * 0.10
  - net_received: dividend - retention
expected:
  retention: 100000
  net_received: 900000
```

### Example 2: consultant, own name or a company (decision, first pass)

Profit L1,500,000 a year. As an individual (after the L40,000 deduction) the scale gives L272,860.61. Through a company: 25% plus 5% solidarity on L500,000 is L400,000, and paying the rest out as a dividend adds 10% of L1,100,000, L110,000, for L510,000. At this profit the individual route costs less tax; the company route also brings activo neto and Form 103 duties. Use the owning skills before advising.

```oa-check
name: HN 2026 individual against company at L1,500,000 profit
inputs:
  profit: 1500000
  flat_deduction: 40000
  top1: 228324.32
  top2: 348154.10
  top3: 809660.75
steps:
  - net: profit - flat_deduction
  - individual_tax: round((top2 - top1) * 0.15 + (top3 - top2) * 0.20 + (net - top3) * 0.25, 2)
  - company_tax: profit * 0.25 + (profit - 1000000) * 0.05
  - dividend_tax: (profit - company_tax) * 0.10
  - company_route: company_tax + dividend_tax
  - difference: company_route - individual_tax
expected:
  net: 1460000
  individual_tax: 272860.61
  company_tax: 400000
  dividend_tax: 110000
  company_route: 510000
  difference: 237139.39
```

## Ask the client first

1. Individual or company, and domiciled in Honduras or not?
2. What income (salary, fees, business, rent, dividends, gains) and from where?
3. RTN and the regimes registered (ISV, pagos a cuenta, simplified, special regimes).
4. Employees, and how many?
5. The tax year in question.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for the 2026 individual scale, Acuerdo SAR-01-2026 | https://www.sar.gob.hn/download/acuerdo-numero-sar-01-2026-publicado-en-fecha-23-de-enero-del-2026-en-la-gaceta-no-37051/?wpdmdl=22954 | 2026-11-14 |
| Read for SAR Generalidades 30 de abril (June 2026), corporate rate, solidarity and net assets | https://www.sar.gob.hn/download/generalidades-impuestos-con-vencimiento-al-30-de-abril/?wpdmdl=23287 | 2026-11-14 |
| Read for LISV consolidated text, arts. 6, 12 and 15 | https://www.sar.gob.hn/download/texto-consolidado-ley-del-impuesto-sobre-ventas-decreto-ley-numero-24-actualizado-hasta-el-decreto-legislativo-no-59-2022/?wpdmdl=15324 | 2026-11-14 |
| Read for LISR consolidated text, arts. 5, 10, 25, 27 and 28 | https://www.sar.gob.hn/download/ley-isr-texto-consolidado-hasta-el-acuerdo-no-sar-014-2023/?wpdmdl=17388 | 2026-11-14 |
| Read for Codigo Tributario consolidated, arts. 160 and 163 | https://www.sar.gob.hn/download/texto-consolidado-codigo-tributario-decreto-170-2016-segun-fe-de-errata-publicada-en-la-gaceta-de-fecha-25-de-mayo-del-2017-y-los-decretos-25-2017-7-2017-32-2017-93-2017-98-2018-55-2019-170-2/?wpdmdl=6987 | 2026-11-14 |

Not yet confirmed: double tax treaties and exchange agreements in force; municipal tax rates; any 2026 tax reform law passed after the consolidated texts read here.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `hn-tax-overview` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/hn-tax-overview. If neither is available, confirm every figure against the official source pages cited above before relying on it.
