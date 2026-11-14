---
name: el-salvador-iva
description: "Use this skill for El Salvador VAT (Impuesto a la Transferencia de Bienes Muebles y a la Prestacion de Servicios, IVA) in 2026. It gives the 13% rate (art. 54), zero rate on exports (art. 75), the art. 46 exempt services (housing rent, education, deposit and loan interest, life insurance, public passenger transport, public water), the art. 28 exclusion for very small traders (sales below 50,000 colones and assets below 20,000 colones), credit only on comprobantes de credito fiscal (art. 65) and the blocked items of art. 65-A, the proportional factor (art. 66), the 1% retention by large taxpayers (Codigo Tributario art. 162), the buyer's liability for non-domiciled suppliers (art. 161) and the monthly return within the first 10 working days. Trigger phrases include IVA El Salvador, F-07, credito fiscal, CCF, gran contribuyente retencion 1% and DGII."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/el-salvador-iva"
  jurisdiction: "SV"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# El Salvador VAT (IVA), 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Salvadoran accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in El Salvador.

## Who this applies to

Contributors of IVA in El Salvador: anyone who transfers movable goods, provides services, imports or exports, under the Ley de Impuesto a la Transferencia de Bienes Muebles y a la Prestacion de Servicios (Decreto Legislativo 296 of 1992, consolidated text of the Asamblea Legislativa). The authority is the DGII of the Ministerio de Hacienda; the currency is the US dollar.

Excluded (art. 28): a trader whose taxed and exempt sales in the previous 12 months were below 50,000 colones and whose total assets are below 20,000 colones (about USD 5,714.29 and USD 2,285.71 at the legal 8.75 colones per dollar). The exclusion never covers companies, importers, or a trader with several premises that together exceed the limits. Once either limit is passed, the trader becomes a contributor from the month after the next.

Refer: free zones and international services parks, real estate construction, the special regimes for fuel, tourism and cultural activities, and any DGII audit.

Conservative defaults:

| Ambiguity | Default |
| --- | --- |
| Rate of a sale unknown | 13% |
| Purchase supported only by a factura (consumer invoice), not a CCF | No credit |
| Mixed taxed and exempt sales | Proportional factor (art. 66) |
| Car, boat or aircraft costs not essential to the business | Blocked (art. 65-A c) |
| Food bought by a business that does not sell food | Blocked (art. 65-A a) |
| Supplier non-domiciled | Buyer pays the IVA (CT art. 161) |

## Rates, bands and thresholds

| Item | Rate or amount | Condition | Source |
| --- | --- | --- | --- |
| General rate (art. 54) | 13% | On the tax base | Asamblea Legislativa, Ley de IVA consolidated: https://www.asamblea.gob.sv/sites/default/files/documents/decretos/C710DA02-4727-485E-B8F4-B9CBF64152A6.pdf |
| Exports (art. 75) | 0% | Goods and services exported | same |
| Exclusion threshold, sales (art. 28) | Below 50,000 colones in 12 months | Together with the asset test; not for companies or importers | same |
| Exclusion threshold, assets (art. 28) | Below 20,000 colones | Together with the sales test | same |
| Monthly return and payment (art. 94) | Within the first 10 working days of the following month | Retained and collected IVA in the same period | same |
| Retention by large taxpayers (CT art. 162) | 1% of the price, before IVA | Purchases of USD 100 or more from contributors that are not large taxpayers | Asamblea Legislativa, Codigo Tributario consolidated: https://www.asamblea.gob.sv/sites/default/files/documents/decretos/297557B6-E5FD-4A41-B734-089751C41FDA.pdf |
| Late return (CT art. 238 b) | 5%, 10%, 15% or 20% of the tax by months late; at least two minimum wages | Not filing: 40% of the tax, at least one minimum wage | same |
| Retained IVA not remitted (CT art. 246 a) | Fine equal to the amount | Plus the tax | same |

## The base

**Taxed:** transfers of movable goods, services, imports and self-supply in El Salvador at 13%.

**Exempt services (art. 46):** health services of public and public-utility institutions; letting of housing; work under an employment relationship; qualified cultural shows; education at authorised institutions; interest on deposits and loans by supervised financial institutions and cooperatives; interest on public offered securities; water and sewerage from public bodies; public land passenger transport; life insurance premiums and reinsurance; AFP commissions; the national lottery; rural community water. Exempt imports (art. 45) cover diplomats, international bodies and travellers' baggage. The old goods exemption article (art. 44) was repealed by D.L. 877/2000: medicines, books and farm products are not exempt under the IVA law itself.

**Credit (art. 65):** only IVA shown on comprobantes de credito fiscal, for inventory, fixed assets that keep their identity, and services used in the business (not construction of real estate). **Blocked (art. 65-A):** food bought by a business that does not sell food, vehicles, boats and aircraft not strictly needed for the business and their fuel, parts and insurance, hotel and rented property use not shown to serve the business, and any purchase without the required document.

**Proportional factor (art. 66):** when a period has taxed, exempt and non-subject sales, the creditable share is taxed sales divided by all sales; later periods use the accumulated figures to the end of the year.

**Non-domiciled suppliers (CT art. 161):** the buyer is liable and pays the IVA by a payment order (mandamiento) from the DGII.

## Deadlines and filing

| Obligation | Deadline | Form or channel |
| --- | --- | --- |
| Monthly IVA return with payment (art. 94) | First 10 working days of the following month | DGII return (F-07), DGII online services, banks |
| Retained and collected IVA | Same return, same period | |
| Non-domiciled supplier | Mandamiento de pago issued by DGII | DGII |

Documents: CCF for sales to contributors (gives the buyer a credit), factura for final consumers. Electronic documents (DTE) apply under DGII rules not read in this pass.

## Penalties and interest

Codigo Tributario: return not filed, 40% of the tax determined, at least one monthly minimum wage (art. 238 a); filed late, 5% up to one month, 10% up to two, 15% up to three, 20% beyond, at least two minimum wages, one minimum wage if no tax due (art. 238 b). Retained or collected and not remitted: a fine equal to the amount (art. 246 a); not retained: 75% (art. 246 b); remitted late: 50% (art. 246 c).

## Cross-border points

Exports are zero rated with credit. Imports pay IVA at customs. Services from non-domiciled providers: the Salvadoran buyer pays the IVA (CT art. 161); the same payment also bears the 20% income tax retention (CT art. 158), see [el-salvador-income-tax](el-salvador-income-tax.md).

## Two worked examples that recompute

### Example 1: medium contributor selling to a large taxpayer, March 2026

Sales USD 10,000 to a large taxpayer (13% IVA USD 1,300); the buyer retains 1% of the price, USD 100. Credits on CCFs USD 500. Net IVA USD 800; after the retention credit, USD 700 is paid by the tenth working day of April.

```oa-check
name: SV 2026 IVA with 1% large-taxpayer retention
inputs:
  sales: 10000
  input_credit: 500
steps:
  - debit: sales * 0.13
  - retained_by_buyer: sales * 0.01
  - net: debit - input_credit
  - payable: net - retained_by_buyer
expected:
  debit: 1300
  retained_by_buyer: 100
  net: 800
  payable: 700
```

### Example 2: clinic with taxed and exempt income (decision on the factor)

A private clinic (not a public-utility institution, so its health services are taxed) also runs a training school authorised by the Ministry of Education (exempt). Taxed sales USD 60,000, exempt USD 40,000, IVA on common purchases USD 5,000. Factor 0.60: USD 3,000 creditable, USD 2,000 becomes a cost. If the school were split into a separate entity, the clinic could credit all IVA tied to its taxed services, so the decision turns on how much of the common IVA can be traced to one activity.

```oa-check
name: SV 2026 IVA proportional factor
inputs:
  taxed: 60000
  exempt: 40000
  common_credit: 5000
steps:
  - factor: taxed / (taxed + exempt)
  - creditable: common_credit * factor
  - cost: common_credit - creditable
  - debit: taxed * 0.13
  - payable: debit - creditable
expected:
  factor: 0.6
  creditable: 3000
  cost: 2000
  debit: 7800
  payable: 4800
```

## Ask the client first

1. Is the client a registered contributor, a large taxpayer, or excluded under art. 28 (sales and assets)?
2. What is sold, to whom (contributors with CCF or final consumers) and is any of it exported or exempt?
3. Purchases supported by CCFs, and which activity each serves.
4. Retentions suffered (1%) and collected.
5. Services or goods bought from non-domiciled suppliers.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for Ley de IVA consolidated text (Asamblea Legislativa), arts. 28, 45, 46, 54, 65, 65-A, 66, 75 and 94 | https://www.asamblea.gob.sv/sites/default/files/documents/decretos/C710DA02-4727-485E-B8F4-B9CBF64152A6.pdf | 2026-11-14 |
| Read for Codigo Tributario consolidated text, arts. 158, 161, 162, 238 and 246 | https://www.asamblea.gob.sv/sites/default/files/documents/decretos/297557B6-E5FD-4A41-B734-089751C41FDA.pdf | 2026-11-14 |

Not yet confirmed: exemptions in separate laws (medicines, farm products, fuel regimes) that the old file listed as IVA exemptions; the 1% perception (CT art. 163) conditions; DTE electronic invoicing timetable; F-07 line numbers on the current form; any IVA amendment after the consolidated text read; late payment interest.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `el-salvador-iva` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/el-salvador-iva. If neither is available, confirm every figure against the official source pages cited above before relying on it.
