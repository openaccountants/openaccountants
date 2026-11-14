---
name: honduras-isv
description: >
  Use this skill to prepare, review or classify a Honduras sales tax (Impuesto Sobre
  Ventas, ISV) position for 2026. ISV works as a VAT. It gives the 15% general rate, the
  18% rate for beer, spirits, other alcoholic drinks, cigarettes and air tickets above
  economy class, zero rate on exports, the art. 15 exemptions (basic food list, medicines,
  fuels, residential electricity up to 750 kWh, professional fees of individuals,
  financial services, housing rent, commercial rent up to L5,000 a month), credit rules
  and the proportional credit, the monthly return due in the first 10 calendar days, the
  L250,000 simplified regime and Codigo Tributario penalties. Trigger phrases include ISV
  Honduras, impuesto sobre ventas, credito fiscal, regimen simplificado, SAR, RTN and CAI.
version: "3.0"
jurisdiction: HN
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - vat-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: situation-rules
---

# Honduras sales tax (ISV), 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Honduran accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Honduras.

## Who this applies to

Every person who sells taxable goods or services in Honduras or imports them, registered with SAR (RTN) as a responsable of ISV. The law (Ley del Impuesto Sobre Ventas, Decreto-Ley 24, consolidated to Decreto 59-2022) taxes the sale of goods and services and imports; the tax is a debit less credit system with a monthly return.

Small traders with one establishment and taxable sales not above L250,000 a year are in the simplified regime (art. 11-A): they do not collect ISV and file only an annual sales return by 31 January.

Refer to a Honduran accountant (refusal catalogue): free zone (ZOLI), maquila and other special export regimes (no credit, own rules); ISV retention agent duties (cards, state, large taxpayers); sale of real estate; tourism activities and the hotel rate; non-resident digital service providers; any exoneration certificate.

Conservative defaults when a fact is missing:

| Ambiguity | Default |
| --- | --- |
| Rate of a sale unknown | 15% |
| Item on the basic food list (Acuerdo 005-2014 Anexo I) not confirmed | 15% until checked against the list |
| Export evidence incomplete | Treat as a domestic sale at 15% |
| Purchase without a valid fiscal document | No credit |
| Mixed taxable and exempt sales, costs not allocable | Proportional credit (art. 12 b) |
| Business use of a vehicle or phone unknown | No credit |

Red flags: credit claimed more than three months after the month it arose; a credit balance carried for many months; sales near L250,000 by a simplified trader; ISV booked as an expense by a registered person; a large single invoice from a free zone supplier.

## Rates, bands and thresholds

| Item | Rate or amount | Condition | Source |
| --- | --- | --- | --- |
| General rate (art. 6) | 15% | Sales of goods and services and imports not exempt | SAR LISV consolidated text: https://www.sar.gob.hn/download/texto-consolidado-ley-del-impuesto-sobre-ventas-decreto-ley-numero-24-actualizado-hasta-el-decreto-legislativo-no-59-2022/?wpdmdl=15324 |
| Increased rate, drinks and tobacco (art. 6) | 18% | Beer, aguardiente, licor compuesto and other alcoholic drinks, cigarettes; collected at producer or import | same |
| Increased rate, air tickets (art. 6) | 18% | Executive, first, business or similar class, domestic and international | same |
| Exports (art. 6) | 0% with right to credit or refund | Goods and services exported, including special export regimes | same |
| Simplified regime ceiling (art. 11-A) | L250,000 of taxable sales a year | One establishment; exempt sales left out of the count | same |
| Commercial rent exemption (art. 15 f) | Rent not above L5,000 a month | Above that, 15% on the rent | same |
| Residential electricity exemption (art. 15 d) | Up to 750 kWh a month | Residential users above 750 kWh pay ISV | same |
| Monthly return and payment (art. 12) | Within the first 10 calendar days of the following month | Filed even with nil or credit balance | same |
| Credit time limit (art. 12) | Month the credit arose or one of the next three months | Monthly filers | same |
| Late ISV return (CT art. 160.4) | 1% of the tax within 5 days; then 2% a month or part, up to 24% | Codigo Tributario | SAR Codigo Tributario consolidated: https://www.sar.gob.hn/download/texto-consolidado-codigo-tributario-decreto-170-2016-segun-fe-de-errata-publicada-en-la-gaceta-de-fecha-25-de-mayo-del-2017-y-los-decretos-25-2017-7-2017-32-2017-93-2017-98-2018-55-2019-170-2/?wpdmdl=6987 |
| Late payment interest (CT art. 163.1) | 3% a month or part, up to 36% | All taxes | same |
| Retained or collected tax not remitted (CT art. 163.2) | 5% a month or part, up to 60% | Agents | same |

## The base

**Taxed:** sales of goods and services in Honduras and imports, on the sale price (imports: the art. 3 base). Prepared food is taxed whether eaten in or taken away. Telecoms are taxed at 15% on the scales in art. 6.

**Exempt (art. 15), the main lines:**
- a) the essential consumer goods list in Annex I of Acuerdo Ejecutivo 005-2014;
- b) medicines for human use, surgical dressing, syringes;
- c) generation equipment already contracted, gasoline, diesel, bunker C, kerosene, LPG, Av-jet, crude oil, books, newspapers, scientific and cultural magazines, exercise books and school supplies, art, minor crafts, national flowers;
- d) residential electricity up to 750 kWh a month, water and sewerage, construction services, municipal services, professional fees earned by individuals, teaching, hospital, laboratory, radiology and medical services (not aesthetic treatments), land passenger transport, fuel transport, banking and financial services (not finance leases of movables), personal insurance and reinsurance;
- e) farm inputs, veterinary medicines, fertilisers and pesticides, live animals, seed, animal feed (not pet food);
- f) diplomats (reciprocity), constitutionally exempt institutions, mergers and liquidations, sale and finance lease of real estate, commercial rent up to L5,000 a month and housing rent (not hotels, motels and lodgings);
- g) and h) entry to sports events and to certain church events.

**Credit (art. 12):** ISV paid on purchases and imports linked to taxable production, on fixed assets used for taxable activity and on repair services, if paid and documented with a fiscal document meeting the invoicing regulation. No credit for own use, gifts, undocumented purchases or for companies in special export regimes. Creditable ISV is never a cost for income tax, unless it relates to exempt sales. A mixed seller uses 100% of the credit linked to taxable sales and, where costs cannot be identified, only the share equal to taxable sales over total sales; the rest is a cost. A credit balance carries forward month by month; refunds and credit notes run under CT arts. 129 and 131.

## Deadlines and filing

| Obligation | Who | When | Channel |
| --- | --- | --- | --- |
| Monthly ISV return and payment | Every registered responsable | First 10 calendar days of the following month (December 2026 by 10 January 2027) | SAR Oficina Virtual (OVI) |
| Annual sales return, simplified regime | Simplified traders | By 31 January of the following year | OVI |
| Declaracion Mensual de Compras (DMC) | Taxpayers obliged by SAR | Monthly (Acuerdo DEI-SG-276-2015, not read) | OVI |
| Retained ISV (agents) | Retention agents | First 10 calendar days of the following month | OVI |

Fiscal documents (facturas) come from SAR-authorised printers or systems and carry the CAI; SAR's verification tools check them.

## Penalties and interest

Late or missing ISV return: 1% of the tax if filed within five days of the due date, then 2% for each month or part, capped at 24% (CT art. 160.4). Late payment: 3% interest a month or part, capped at 36% (art. 163.1). An agent who does not remit retained or collected tax: 5% a month, capped at 60% (art. 163.2). Formal faults are fined by gross income band (art. 160.1), and voluntary correction cuts the fine by 50%, 30% or 10% (art. 162). Tax defrauding and failure to remit collected tax may also be offences (CT, not covered here).

## Cross-border points

Imports pay ISV at customs on each operation (art. 12). Exports of goods and services are zero rated with credit or refund. Services from a foreign provider without a Honduran presence: the collection mechanism was not confirmed in this pass (see Not yet confirmed). Free zone suppliers sell without ISV; their customers get no credit on those purchases.

## Two worked examples that recompute

### Example 1: mixed seller, monthly return for October 2026

Taxable sales at 15% L600,000, exempt sales (medicines) L400,000. ISV on purchases that cannot be split between the two: L30,000. Debit L90,000. Credit allowed 60% (600,000 of 1,000,000) = L18,000; the other L12,000 is a cost. ISV payable L72,000 by 10 November 2026.

```oa-check
name: HN 2026 ISV mixed seller, proportional credit
inputs:
  taxable_sales: 600000
  exempt_sales: 400000
  common_input_isv: 30000
steps:
  - debit: taxable_sales * 0.15
  - share: taxable_sales / (taxable_sales + exempt_sales)
  - credit: common_input_isv * share
  - cost_isv: common_input_isv - credit
  - payable: debit - credit
expected:
  debit: 90000
  share: 0.6
  credit: 18000
  cost_isv: 12000
  payable: 72000
```

### Example 2: landlord of a shop, exempt or taxed (decision)

A landlord lets one shop for L5,000 a month and is asked to accept L5,500. At L5,000 the rent is exempt (art. 15 f: not above L5,000). At L5,500 the whole rent is taxed at 15%: L825 a month, L9,900 a year, and the landlord must register and file monthly. The figure that decides it is the L5,000 monthly ceiling.

```oa-check
name: HN 2026 commercial rent, the L5,000 ceiling
inputs:
  rent_a: 5000
  rent_b: 5500
  ceiling: 5000
steps:
  - isv_a: rent_a * 0.15 * min(max(rent_a - ceiling, 0), 1)
  - isv_b_month: rent_b * 0.15
  - isv_b_year: isv_b_month * 12
expected:
  isv_a: 0
  isv_b_month: 825
  isv_b_year: 9900
```

## Ask the client first

1. RTN, regime (ordinary monthly or simplified) and number of establishments.
2. What you sell, item by item: is any on the basic food list, a medicine, a fuel, alcohol or tobacco, an air ticket?
3. Sales split between taxable, exempt and export for the month, with export documents.
4. Purchases with valid facturas (CAI) and which activity each serves.
5. Any special regime (ZOLI, maquila, tourism), exoneration or role as a retention agent.
6. Credit balance carried from the last return.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for LISV consolidated text to Decreto 59-2022, arts. 6 (rates), 11-A (simplified regime), 12 (return, credit, proportional credit) and 15 (exemptions) | https://www.sar.gob.hn/download/texto-consolidado-ley-del-impuesto-sobre-ventas-decreto-ley-numero-24-actualizado-hasta-el-decreto-legislativo-no-59-2022/?wpdmdl=15324 | 2026-11-14 |
| Read for Codigo Tributario Decreto 170-2016 consolidated, arts. 160, 162 and 163 | https://www.sar.gob.hn/download/texto-consolidado-codigo-tributario-decreto-170-2016-segun-fe-de-errata-publicada-en-la-gaceta-de-fecha-25-de-mayo-del-2017-y-los-decretos-25-2017-7-2017-32-2017-93-2017-98-2018-55-2019-170-2/?wpdmdl=6987 | 2026-11-14 |
| Read for the SAR home page menu: ISV, simplified regime, DMC, DMR and card retention agent pages | https://www.sar.gob.hn/ | 2026-11-14 |

Not yet confirmed: whether hotel and tourist services bear 18% ISV or 15% plus a separate tourism tax (the old file said 18%; not found in the LISV text read); ISV on services supplied by non-resident digital providers; the DMC obligation and who must file it; ISV retention by card processors and large taxpayers (Acuerdo SAR-240-2024 not read); the content of the Annex I basic food list; any LISV amendment after Decreto 59-2022; the form and box numbers of the monthly return on the Oficina Virtual.
