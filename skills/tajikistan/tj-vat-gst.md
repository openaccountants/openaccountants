---
name: tj-vat-gst
description: "Compute ordinary 2026 Tajikistan VAT, registration exposure, documented export zero rating and reverse taxation of foreign services. Distinguishes exemptions, reduced rates, restricted input credit, monthly filing and the separate foreign distance-service regime."
jurisdiction: TJ
tax_year: 2026
last_updated: 2026-11-15
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
category: international
type: computation
version: 0.1
---

# Tajikistan VAT v0.1

> **General reference only.** This skill prepares a working paper for review by a qualified Tajikistan professional. Confirm the facts, source version and filing procedure before filing, paying or taking a tax position.

**Built from the law. Not yet approved.** Tax year 2026; checked on 2026-11-15.


## Scope

For ordinary domestic VAT, taxable imports and the specific foreign-service tax-agent rules. VAT is separate from income tax. Foreign suppliers serving individuals under the distance-services chapter, special regimes and complicated mixed/imported-goods reduced-rate cases need a separate review before applying this ordinary computation. [Arts. 245, 260, 264, 272-273](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).


## Ask the client first

- Supplier/customer legal identity, residence, permanent establishment, VAT registration and tax regime.
- Gross income by month, related-party income, imported transactions and any special mandatory-registration category.
- Supply description, place, invoice/tax-point dates, net/gross contract price and exemption/reduced-rate basis.
- Input invoices, customs payment evidence, intended use, fixed assets and mixed/exempt activity.
- Export goods classification, customs date, destination, export proof and banking evidence.
- Reporting period, prior adjustments, foreign-service payments and current official VAT declaration.


## The method, step by step


### Check registration before calculating

| Item and conditions | Rate or threshold | Official provision |
|---|---|---|
| Ordinary income-based VAT registration | Gross income exceeding TJS 1,000,000 over no more than 12 full consecutive calendar months; aggregate related persons' gross income. This is not merely taxable turnover | [Art. 245(1)-(2)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) |
| Start after the ordinary threshold is exceeded | First day of the reporting period after the month of exceedance | [Art. 245(6)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) |
| Standard taxable turnover and imports | 14% from 1 January 2024 through 31 December 2026; scheduled 13% from 1 January 2027. The transition overrides the printed 15% standard rate in art. 264(1)(1) | [Arts. 264(1)(1), 397(4)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) |
| Qualifying domestic construction, hotel and catering services | 7%; reduced-rate rules exclude taxable imports and subsequent supply of imported goods | [Art. 264(1)(2)-(5)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) |
| Qualifying domestic agricultural goods/processing excluding cotton processing, education, and medical services in sanatoria/resorts | 5%, with the stated no-input-credit treatment; do not confuse this with the narrower state-institution exemptions | [Art. 264(1)(2)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) |
| Qualifying documented goods exports | 0%, subject to the excluded goods list and export-proof rules | [Arts. 254-255, 264(2)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) |

Art. 245 also identifies mandatory categories independent of the ordinary threshold, including taxable importers, specified foreign suppliers, successors and tax agents. Voluntary registration requires an identifiable permanent business place, business activity and accounting, and no connection with companies lacking economic substance. Registration on application is automatic for the specified categories and produces an electronic certificate; do not assume a below-threshold foreign-service recipient has no VAT duty. [Art. 245(1), (3)-(7)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).


### Separate standard, reduced, exempt and export transactions

Exempt financial services are the fee-based financial services on the list set by the National Bank with the finance/tax authorities. State medical services exclude cosmetic, dental and sanatorium/resort services. The education exemption is for the listed education services of state institutions financed by the state budget. A private school, dentist or financial business is not exempt merely by its broad sector label. Other art. 251 listed exemptions require their own exact conditions. [Art. 251(2)(2), (5)-(6)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).

Reduced-rate operators need separate accounting; imported goods and their subsequent supply remain subject to the standard-rate rules, and transformed imported goods need the proportional split in art. 264(4). Check the no-credit restrictions before treating a reduced rate as equivalent to standard VAT with full input recovery. [Arts. 264(3)-(5), 266(6)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).

For exports, the zero-rate exclusion list includes precious metals/stones and jewellery, primary aluminium, natural-resource concentrates, commodity ores, ferrous/non-ferrous scrap and other Tajik-produced metals, central-bank precious-metal measured bars, and goods produced in free economic zones. The current list includes the June 2026 amendment. A zero rate is not available for every export. [Art. 254(1)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).

Retain customs export declaration, supply contract, invoice/transport documents with customs evidence, and payment/bank evidence; additional CIS, barter and outward-processing evidence can apply under art. 255. If proof is not provided within 90 calendar days after export customs clearance, apply the positive rate under art. 254(2). Submission within 120 calendar days permits recovery under art. 255(5); outside that window the statutory recovery right is lost. [Arts. 254(2), 255](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).


### Compute output less eligible input VAT

At the standard rate, compute output VAT from the taxable value, add any required reverse-tax amount, then deduct only eligible input VAT. Invoice and customs evidence, actual taxable transactions and business use are required. Mixed business/private use needs apportionment; exempt activity and mixed taxable/exempt activity require arts. 266(7) and 268, not automatic full credit. [Arts. 264(7), 265, 266(1)-(7), 268](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).

Art. 266(6) denies credit in specified cases including ordinary passenger-car acquisition outside the principal resale/rental exception, charitable/social/entertainment expenditure, invalid invoice details, geological preparation, depreciable fixed/intangible asset acquisition/construction/installation/restoration, reduced-rate purchases outside the import exception, and specified foreign distance services. Fictitious transactions are prohibited. Wholesale/retail and the other listed trading businesses have the special timing rule in art. 266(11). Never infer recoverability from VAT registration alone. [Art. 266(6)-(11)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).


### Foreign services: reverse taxation is not automatic input credit

For the art. 260 foreign-supplier conditions, the Tajik legal-entity buyer acts as tax agent. Calculate the tax using the applicable art. 264 rate on the amount payable to the supplier after withholding, rather than assuming every foreign payment is a standard-rated gross amount. Confirm the place and nature of work/services and any internal foreign-branch conditions. [Art. 260(1)-(3), (6)-(7)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).

A registered agent pays the withheld tax and reports it in the transaction month as payable without input credit. An unregistered agent pays within 5 days after payment to the foreign supplier (in words on the page) and files by the 15th of the following month. [Art. 260(4)-(5)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).


### Filing and payment

Ordinary VAT uses a calendar-month period; return and payment are due by the 15th of the following month. Import collection follows customs law. Foreign suppliers of distance services to individuals instead have a calendar-quarter period and a return/information deadline of the 20th after the quarter; this does not make domestic VAT quarterly. [Arts. 272-273](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).

Prepare separate schedules for standard/reduced/zero/exempt sales, taxable imports, reverse-tax payments, eligible input VAT, disallowed amounts and adjustments. Reconcile sales invoices, customs records and the tax account. Obtain the current official declaration and attachments through the Tax Committee [personal cabinet](https://www.andoz.tj/) or local office, map the schedules to current fields, and retain acceptance and payment evidence. Current fields, tax-point exceptions and refund processing are not verified for submission in this skill.


## Worked cases


### Standard domestic VAT with eligible input

Illustrative standard-rated domestic sales excluding VAT TJS 100,000; separately evidenced eligible input VAT TJS 2,800, with no fixed asset, exempt-use, reduced-rate or other credit restriction. Output VAT is TJS 14,000 and payable VAT is TJS 11,200. The customer invoice total is TJS 114,000.

```oa-check
name: Ordinary standard-rate VAT
inputs:
  net_sales: 100000
  eligible_input_vat: 2800
steps:
  output_vat: net_sales * 0.14
  invoice_total: net_sales + output_vat
  payable: max(0, output_vat - eligible_input_vat)
expected:
  output_vat: 14000
  invoice_total: 114000
  payable: 11200
```


### Export proof changes the output tax

Illustrative TJS 50,000 export of ordinary goods outside the exclusion list. With all required timely proof, output tax is zero. Without proof within the statutory period, assuming the goods would otherwise carry the standard rate, output VAT becomes TJS 7,000. Keep the separate recovery-window review if proof arrives later; do not treat a missing export dossier as zero-rated by default.

```oa-check
name: Export evidence decision
inputs:
  export_value: 50000
steps:
  supported_export_vat: export_value * 0
  unproved_export_vat: export_value * 0.14
  difference: unproved_export_vat - supported_export_vat
expected:
  supported_export_vat: 0
  unproved_export_vat: 7000
  difference: 7000
```


### Reverse tax on the supplier net amount

Illustrative art. 260 taxable standard-rate service: contract provides TJS 10,000 payable to the foreign supplier after withholding. VAT is TJS 1,400 on that amount and total funding is TJS 11,400. For a registered tax agent, the reverse-tax input credit is zero under art. 260(4), so the TJS 1,400 remains payable.

```oa-check
name: Foreign-service reverse taxation without credit
inputs:
  supplier_net: 10000
steps:
  reverse_tax: supplier_net * 0.14
  total_funding: supplier_net + reverse_tax
  input_credit: 0
  payable: reverse_tax - input_credit
expected:
  reverse_tax: 1400
  total_funding: 11400
  input_credit: 0
  payable: 1400
```


## When to refuse or refer

Refer disputed place of supply, special exemptions and lists, mixed/reduced/imported-goods allocations, tax-point disputes, customs/import relief, digital platforms, special regimes and late export proof. Do not credit reverse tax automatically or classify every medical, education or financial supply as exempt. Stop before submission without the current declaration and supporting invoice/customs evidence.


## Sources

| Official source | Read for | Date read |
|---|---|---|
| [Tax Committee, current consolidated Tax Code](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) | Read for arts. 244-245, 251(1)-(2), 254-255, 260, 264-266, 268, 272-273, 397(4); rates, exceptions, registration, export proof and credit restrictions. | 2026-11-15 |

Not yet confirmed: Live VAT declaration fields, sector-specific financial-service/other exemption lists, detailed tax-point exceptions, refund processing and foreign distance-service filing/payment mechanics. The scheduled post-2026 standard rate must be rechecked before use in a later year; it is not a 2026 rate.

