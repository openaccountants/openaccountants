---
name: cl-vat-return
description: "Chile IVA (impuesto al valor agregado) and the monthly Formulario 29 for 2026 under DL 825, Ley sobre Impuesto a las Ventas y Servicios. Covers who is a taxpayer, the 19% rate, what is a taxable sale or service after the widening of services, place of supply and the remote-services presumption, the main exemptions of arts. 12 and 13 (exports, international transport, interest, unfurnished property rent, professional fees under LIR art. 42, health, education, passenger transport), the non-resident digital services regime and reverse charge, low-value imports up to USD 500, input credit and its blocks (cars, fuel, false invoices), the remanente carried forward in UTM, exporter recovery, electronic documents (DTE codes), F29 codes, the day 12 and day 20 deadlines, the two-month deferral for small firms, the temporary new-housing exemption of Ley 21.850, additional taxes on alcohol, sugary drinks and luxury goods, and penalties. Trigger on: IVA Chile 2026, Formulario 29, F29, débito fiscal"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/cl-vat-return"
  jurisdiction: "CL"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Chile: IVA and the monthly Formulario 29 (2026) v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill prepares Chile's monthly IVA return, Formulario 29 (F29), for periods in 2026: the output tax (débito fiscal), the input tax (crédito fiscal), the carried-forward credit (remanente), and where each lands on the form. The tax period is the calendar month (DL 825 art. 2 No. 5).

Linked skills, not repeated here:

- [cl-income-tax](cl-income-tax.md): the boleta de honorarios withholding and PPM, which are also paid through F29.
- [cl-corporate-income-tax](cl-corporate-income-tax.md): first category PPM in F29 and the Pro Pyme regime.

**Which text of the law.** DL 825, Ley sobre Impuesto a las Ventas y Servicios, LeyChile version of 5 February 2026. Ley 21.850 (published 17 October 2026) adds a temporary exemption for new housing (art. 4 transitorio) and does not change the rate.

## Who this applies to

- **Taxpayers.** Any person or entity, including communities and de facto partnerships, that makes sales, provides services or carries out any other operation taxed by DL 825 (art. 3). There is no registration threshold in the law.
- **Sales.** Transfers for value of movable goods and of built real estate by a habitual seller; land is not taxed (art. 2 No. 1, No. 3). Habituality is judged by SII (art. 2 No. 3).
- **Services.** Any action or service one person provides to another for a fee, interest, premium or commission (art. 2 No. 2); a service provider may act habitually or occasionally (art. 2 No. 4). Mixed services are split; inseparable mixed services are taxed in full (art. 2 No. 2).
- **Place of supply.** Services provided or used in Chile are taxed wherever paid. A remote service is presumed used in Chile when two of these point to Chile: the user's IP or geolocation, the card or account used to pay, the billing address, or the SIM country code (art. 5).
- **Operations treated as sales or services** (art. 8), including imports (a), withdrawals for the owner's use (d), construction contracts (e), rent of movable goods, furnished property or property with installations for a business (g), rent of trademarks and patents (h), parking (i), sales of fixed assets on which credit was taken (m), and digital services from abroad (n): intermediation, digital entertainment, software, storage, platforms and infrastructure, and advertising.
- **Who pays instead of the seller.** The importer; the buyer when the seller has no residence in Chile; the VAT-registered recipient of a service from a provider abroad (reverse charge, art. 11 b) and e)); digital platforms that intermediate taxable sales to non-taxpayers (art. 3 bis); and buyers designated by SII to withhold (cambio de sujeto, art. 3).
- **Non-resident sellers to consumers** use the simplified regime of arts. 35 A to 35 N.
- **Out of scope.** Professional fees taxed under LIR art. 42 No. 2 (exempt, see below), real-estate developers' special credit, proportional credit calculations under the Reglamento, the art. 29 simplified regime, and the exporter refund procedure in detail. Refer these.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| IVA standard rate | 19% of the taxable base | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=6369 (DL 825 art. 14) |
| Exports of goods | Exempt (export recovery under art. 36) | 2026 | same, art. 12 D, art. 36 |
| Services to non-residents that Customs qualifies as exports | Exempt, with recovery of input IVA | 2026 | same, art. 12 E No. 16, art. 36 |
| International freight and international passenger tickets | Exempt | 2026 | same, art. 12 E No. 2 |
| Interest on financial operations and credits | Exempt (except interest on sale balances, art. 15 No. 1) | 2026 | same, art. 12 E No. 10 |
| Rent of property (unfurnished, without business installations) | Exempt; furnished property or property with business installations is taxed (art. 8 g) | 2026 | same, art. 12 E No. 11 |
| Income under LIR arts. 42 and 48 (wages, professional fees, directors' fees), including societies of professionals | Exempt | 2026 | same, art. 12 E No. 8 |
| Independent workers working alone where physical effort predominates | Exempt (not freight transport) | 2026 | same, art. 12 E No. 12 |
| Health services by law financed by FONASA or ISAPRE, up to the FONASA tariff; outpatient health services without lodging (not laboratories) | Exempt | 2026 | same, art. 12 E Nos. 19, 20 |
| Passenger transport by shipping, air, rail and urban, intercity and rural transport companies | Exempt (passenger income only) | 2026 | same, art. 13 No. 3 |
| Educational establishments | Exempt (teaching income only) | 2026 | same, art. 13 No. 4 |
| Used motor vehicles | Exempt, with exceptions (imports, fixed-asset sales under art. 8 m), leasing options) | 2026 | same, art. 12 A No. 1 |
| Low-value remote purchases of goods by non-taxpayers | Taxed when price including charges is up to USD 500 | 2026 | same, art. 4 last paragraph |
| Additional tax on luxury goods (gold, jewels, fine furs, fine carpets, caviar, air guns) | 15% on first sale or import; pyrotechnics 50% | 2026 | same, art. 37 |
| Additional tax on non-alcoholic drinks | 10%; 18% if high sugar (over 15 g per 240 ml) | 2026 | same, art. 42 a) |
| Additional tax on spirits (liquor, pisco, whisky) | 31.5% | 2026 | same, art. 42 b) |
| Additional tax on wine, sparkling wine, cider, beer and other alcoholic drinks | 20.5% | 2026 | same, art. 42 c) |
| Two-month deferral of IVA payment (Pro Pyme or other firms with average income up to 100,000 UF over 3 years) | Payment up to two months after the due date, if on e-mail notification, no repeated arrears and 36 F29 and 3 F22 filed on time | 2026 | same, art. 64 second paragraph |
| Temporary exemption, first sale of a new home with final municipal reception before 17 Oct 2026 | Optional exemption, with credit kept, for one year from the first business day of December 2026 | Dec 2026-Nov 2027 | https://www.bcn.cl/leychile/navegar?idNorma=1229250 (Ley 21.850, art. 4 transitorio) |
| F29 due date | 12th of the following month | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=6369 (DL 825 art. 64) |
| F29 due date, filed and paid online by electronic invoicers (or boleta de honorarios issuers) | 20th of the following month; 28th for an online return without payment; a Saturday, holiday or 31 December moves to the next business day | 2026 | https://www.sii.cl/preguntas_frecuentes/impuestos_mensuales/001_130_1060.htm |
| UTM used to update the remanente (art. 27), October to December 2026 | Oct 72,151; Nov 72,440; Dec 72,802 | 2026 | https://www.sii.cl/valores_y_fechas/utm/utm2026.htm |
| Penal interest on late payment, 1 July to 31 December 2026 | 7.70% a year, 0.0213888889% a day | Jul-Dec 2026 | https://www.sii.cl/valores_y_fechas/otros_valores/tasa_interes_penal_diario.html |

## The base

**When the tax arises (art. 9).** Sales and services: on the date the invoice or boleta is issued; for goods delivered earlier, on delivery; for services with no document, when the fee is received or made available. Periodic services: at the end of each billing period. Imports: when the import is completed. Construction contracts and real-estate sales: when the invoice is issued.

**When to issue the document (art. 55).** For goods, at delivery (or a guía de despacho at delivery and the invoice by the 10th day after the month end, dated in the month of the operation); for services, in the month the fee is received. Boletas for consumers at delivery or receipt of payment.

**Output tax (débito fiscal, art. 20).** The sum of the IVA charged on sales and services of the month, less IVA on credit notes for discounts and returns, plus debit notes (art. 21). In a boleta the IVA is included in the price: IVA = price x 19 / 119.

**Input tax (crédito fiscal, art. 23).** The IVA charged on invoices for purchases and services, or paid on imports, for goods and services that relate to the business (stock, fixed assets, general expenses). Blocks:

- No credit for purchases used in exempt or non-taxed operations, or unrelated to the business (No. 2). Mixed use: proportional credit under the Reglamento (No. 3); refer.
- **No credit on cars, station wagons and similar vehicles, or their fuel, lubricants, spare parts and repairs**, whether bought, imported or leased, unless the business is selling or renting them (No. 4). Supermarket purchases count only if they meet LIR art. 31 (No. 4).
- No credit on false or non-compliant invoices, unless paid by nominative cheque or bank transfer to the issuer with the issuer's RUT and invoice number recorded, or the IVA was in fact paid by the seller (No. 5).
- An electronic invoice gives credit in the month the buyer acknowledges receipt or it is deemed received (No. 7). Late-received documents may be used within the next two periods (art. 24).

**IVA to pay (art. 20).** Débito fiscal less crédito fiscal. A negative result is the remanente, carried to the next months. To keep its value, convert it to UTM at the UTM of the month when the tax was due and reconvert at the UTM of the month it is used; a difference not claimed in time is lost (art. 27).

**Exporters (art. 36).** Exporters recover the IVA on purchases for export, by setting it against débitos or by refund (arts. 80 onward). The same applies to services qualified as exports (art. 12 E No. 16).

**Electronic documents.** SII's DTE format gives the type codes: 33 factura electrónica, 34 factura no afecta o exenta electrónica, 39 boleta electrónica, 41 boleta exenta electrónica, 43 liquidación-factura electrónica, 46 factura de compra electrónica, 52 guía de despacho electrónica, 56 nota de débito electrónica, 61 nota de crédito electrónica, 110 factura de exportación electrónica, 111 and 112 export debit and credit notes. The purchase and sales register (RCV) built from these documents feeds the F29 proposal (DL 825 art. 59). Input credit needs an invoice: the law grants crédito fiscal on "el impuesto ... recargado en las facturas" (art. 23 No. 1), so a boleta (39, 41), which shows no separate IVA, gives the buyer no credit.

**Withholding by buyers (cambio de sujeto, art. 3).** SII can make the buyer withhold all or part of the IVA. The DTE format lists the codes and usual rates: code 15, total IVA withheld on purchase invoices (types 45, 46); legumes (30), rice (36) and hydrobiological products (37) usually 10%; cattle (32) and timber (33) usually 8%; wheat (34) usually 4%; raspberries and raisins (48) 14%; scrap (38), PPA (39), construction (41), gold (46), cartons (47) and wild products (31) total withholding. Confirm the rate in the SII resolution for the sector before applying it.

**IVA anticipado.** Sellers of meat and flour charge an advance IVA to the buyer, shown on the invoice under its own DTE tax code: slaughter (faenamiento) of meat 5% on the base amount (code 17), meat 5% (code 18), flour 12% (code 19). Source: SII DTE format, tax code table; the underlying SII resolutions were not read.

**Conservative defaults when facts are missing.** Treat a sale as taxed at 19% until the exemption is shown (arts. 8, 12, 13); treat an export as domestic until the export document (DUS, or Customs qualification of a service under art. 12 E No. 16) is in hand; give no credit on a purchase without an electronic invoice to the buyer's RUT (art. 23 Nos. 1, 5), or for cars and their fuel (No. 4), or for a business-use share that is not documented (No. 2).

## Deadlines and filing

| What | When | Rule |
|---|---|---|
| F29 for a month, with payment | By the 12th of the next month | DL 825 art. 64 |
| F29 filed and paid online by an electronic invoicer | By the 20th of the next month | D.S. 1.001 of 2006 art. 1, as SII applies it |
| F29 online without payment, or "sin movimiento" | By the 28th of the next month | SII FAQ 001.130.1060 |
| Due date on a Saturday, holiday or 31 December | Next business day | SII FAQ 001.130.1060 |
| Import IVA | Before goods leave Customs | DL 825 art. 64 |
| Late electronic documents | Credit or adjustment within the next two periods | DL 825 art. 24 |

**How to file.** Log in at sii.cl with RUT and Clave Tributaria, open Servicios Online, Impuestos mensuales, Declaración mensual (F29). SII offers a proposal from the RCV. Check, in order:

1. **Débitos:** invoices issued (line 7, code 503 count, code 502 IVA), boletas (line 10, codes 110 and 111), electronic payment receipts (line 11, codes 758 and 759), debit notes issued (line 12, codes 512 and 513), credit notes issued (line 13, codes 509 and 510, subtracted); exports (line 1, codes 585 and 20) and exempt sales (line 2, codes 586 and 142) as information. Total débitos: code 538.
2. **Créditos:** invoices received for the business (line 28, codes 519 and 520), fixed assets (line 31, codes 524 and 525), credit notes received (line 32, codes 527 and 528, subtracted), debit notes received (line 33, codes 531 and 532), import declarations (line 34, codes 534 and 535), remanente from last month, updated (line 36, code 504). Purchases without credit go on lines 25 to 27 (codes 564 and 521; 566 and 560; 584 and 562). Total créditos: code 537.
3. **Result:** IVA determined (code 89) or remanente for next month (line 50, code 77).
4. **Same form, other taxes:** IUSC withheld (code 48), boleta withholding (code 151), PPM (codes 62 and 152), additional taxes of arts. 37 and 42.
5. **Pay:** total to pay in time (code 91), online (PEL) or by bank mandate (PEC). After the due date the form adds CPI (code 92) and interest and fines (code 93), total code 94.

Keep the F29 folio and payment receipt. The codes above are from SII's published F29 form image; check the on-screen form for any new code.

## Penalties and interest

Under the Código Tributario (DL 830):

- **Late payment of IVA** (a tax charged to the buyer, "sujeto a recargo"): fine of 10% of the tax, plus 2% for each month or part of a month, up to 30%; 20% and 60% when SII detects the omission in an audit (CT art. 97 No. 11).
- **Late return that is the basis of a tax:** 10% of the tax if up to 5 months late, then 2% more a month, up to 30%; it is not added where the No. 11 fine applies and the return could not be filed without payment (art. 97 No. 2). A late return with no tax to pay: 1 UTM to 1 UTA.
- **Wrong or incomplete return** that could lower the tax: 5% to 20% of the difference (art. 97 No. 3). **Malicious maneuvers to increase credits:** prison and fines (art. 97 No. 4).
- **Not issuing an invoice, boleta, credit or debit note or guía, or not sending it to SII:** 50% to 500% of the operation, at least 2 UTM and at most 40 UTA, and closure for up to 20 days (art. 97 No. 10).
- **Interest:** CPI update and daily penal interest at the CMF one-year rate plus 3.5%: 7.70% a year, 0.0213888889% a day, for 1 July to 31 December 2026 (CT art. 53).

## Cross-border points

- **Imports** are taxed at 19% on the customs value plus duties, paid before release (arts. 8 a), 64).
- **Services from abroad to a VAT-registered business:** the Chilean recipient pays the IVA (art. 11 e)) and, if the service relates to taxed operations, takes it as crédito fiscal in the same F29.
- **Services and goods from abroad to consumers:** the foreign provider registers in the simplified regime (arts. 35 A to 35 N); remote goods up to USD 500 are taxed (art. 4); SII may make card issuers withhold for providers outside the regime (art. 3).
- **Exports** and services qualified as exports are exempt with input-IVA recovery (arts. 12 D, 12 E No. 16, 36). Services provided and used wholly abroad also give recovery where the other country has a similar tax (art. 36).

## Two worked examples that recompute

### Example 1: services company, November 2026 F29

Estudio Austral SpA is an electronic invoicer. In November 2026 it issued electronic invoices for CLP 20,000,000 net (IVA CLP 3,800,000), boletas for CLP 2,380,000 including IVA, and an export-qualified service of CLP 5,000,000. It received supplier invoices for CLP 8,000,000 net (IVA CLP 1,520,000) and fuel invoices for the manager's car of CLP 300,000 net (IVA CLP 57,000). The October return left a remanente of CLP 200,000.

- Débitos: 3,800,000 (code 502) + 380,000 on boletas (2,380,000 x 19 / 119, code 111) = CLP 4,180,000 (code 538). The export is information only (code 20), no IVA.
- Créditos: 1,520,000 (code 520). The car fuel gives no credit (art. 23 No. 4): its CLP 57,000 IVA goes on line 25 as without credit. The remanente is updated: October's tax was due in November, the November return is filed in December, so 200,000 x 72,802 / 72,440 = CLP 200,999 (code 504).
- IVA to pay: 4,180,000 - 1,520,000 - 200,999 = CLP 2,459,001 (code 89).
- Due date: filed and paid online by the 20th, which is Sunday 20 December 2026, so Monday 21 December 2026; on paper or without the online benefit, the 12th, a Saturday, so Monday 14 December 2026.

```oa-check
name: CL F29 November 2026, services company with boletas, blocked car fuel and updated remanente
inputs:
  invoices_net: 20000000
  boletas_gross: 2380000
  purchases_net: 8000000
  car_fuel_net: 300000
  remanente: 200000
  utm_nov: 72440
  utm_dec: 72802
steps:
  - debito_invoices: invoices_net * 0.19
  - debito_boletas: round(boletas_gross * 19 / 119, 0)
  - total_debitos: debito_invoices + debito_boletas
  - credito_purchases: purchases_net * 0.19
  - blocked_fuel_iva: car_fuel_net * 0.19
  - remanente_updated: round(remanente * utm_dec / utm_nov, 0)
  - iva_to_pay: total_debitos - credito_purchases - remanente_updated
expected:
  debito_invoices: 3800000
  debito_boletas: 380000
  total_debitos: 4180000
  credito_purchases: 1520000
  blocked_fuel_iva: 57000
  remanente_updated: 200999
  iva_to_pay: 2459001
```

### Example 2: rent an office furnished or unfurnished?

A company owns an office and will spend CLP 10,000,000 net (IVA CLP 1,900,000) furnishing it. The rent is CLP 1,000,000 a month net. Unfurnished office rent is exempt (art. 12 E No. 11); furnished property, or property with installations for a business, is taxed (art. 8 g). Which should it choose?

- **Furnished (taxed):** the company charges IVA of CLP 190,000 a month, CLP 2,280,000 a year, and recovers the CLP 1,900,000 on the furnishing (art. 23 No. 1). Its net cost of furnishing is CLP 10,000,000.
- **Unfurnished (exempt):** no IVA on the rent; any IVA on works for the exempt rental is not creditable (art. 23 No. 2), so the same spend costs CLP 11,900,000.

The figure that decides is whether the tenant can recover IVA. A VAT-registered tenant using the office for taxed sales recovers the CLP 2,280,000, so the furnished rent costs it nothing extra and the landlord saves CLP 1,900,000. A tenant that cannot recover IVA (an individual, or an exempt business) pays CLP 2,280,000 more a year, which is more than the landlord's CLP 1,900,000 saving; for that tenant, unfurnished at the same net rent is cheaper overall.

```oa-check
name: CL IVA 2026, furnished taxed rent against unfurnished exempt rent
inputs:
  furnishing_net: 10000000
  monthly_rent: 1000000
steps:
  - furnishing_iva: furnishing_net * 0.19
  - annual_rent_iva: monthly_rent * 0.19 * 12
  - landlord_cost_furnished: furnishing_net
  - landlord_cost_unfurnished: furnishing_net + furnishing_iva
  - landlord_saving_furnished: landlord_cost_unfurnished - landlord_cost_furnished
  - extra_cost_non_vat_tenant: annual_rent_iva - landlord_saving_furnished
expected:
  furnishing_iva: 1900000
  annual_rent_iva: 2280000
  landlord_cost_furnished: 10000000
  landlord_cost_unfurnished: 11900000
  landlord_saving_furnished: 1900000
  extra_cost_non_vat_tenant: 380000
```

## Ask the client first

1. What does the business sell, to whom (businesses, consumers, foreign clients), and does any of it fall under an exemption of arts. 12 or 13 (professional fees, unfurnished rent, interest, health, education, passenger transport, exports)?
2. Is it an electronic invoicer filing and paying online (day 20), and is it in Pro Pyme or under 100,000 UF average income (the two-month deferral)?
3. Which invoices, boletas, credit and debit notes were issued and received in the month (the RCV), and were the received invoices acknowledged in the month?
4. Are any purchases for cars, their fuel or repairs, for exempt activity, or for mixed use (proportional credit)?
5. What remanente came from last month, and from which period?
6. Any imports, services bought from abroad, or sales to consumers abroad or from abroad (reverse charge, simplified regime, USD 500 rule)?

**Documents to collect:** the RUT and start-of-activities record; the month's RCV, or the XML of every DTE issued and received; last month's F29 (for the remanente); import declarations (DIN) and export declarations (DUS) with transport documents; bank statements only to reconcile.

**Refer to an accountant, do not compute here:** proportional credit for mixed taxed and exempt activity (art. 23 No. 3 and the Reglamento); IVA on real estate and construction contracts (arts. 8 e), 8 l), 23 No. 6); buyer withholding (cambio de sujeto) as withholding agent; the exporter refund procedure (art. 36, arts. 80 onward); leasing and leaseback; free-trade zones (Iquique, Punta Arenas); a foreign provider's own registration in the simplified regime (arts. 35 A to 35 N).

## Sources

| Source | URL | Read on |
|---|---|---|
| DL 825, Ley sobre Impuesto a las Ventas y Servicios, LeyChile version of 5 Feb 2026 (LeyChile XML export): arts. 2, 3, 3 bis, 4, 5, 8, 9, 11, 12, 13, 14, 20, 21, 23, 24, 27, 35 A, 35 B, 36, 37, 42, 55, 59, 64 | https://www.bcn.cl/leychile/navegar?idNorma=6369 | 2026-11-11 |
| Ley 21.850, Reconstrucción Nacional (DO 17 Oct 2026): art. 4 transitorio (new-housing exemption) | https://www.bcn.cl/leychile/navegar?idNorma=1229250 | 2026-11-11 |
| DL 830, Código Tributario, version of 17 Oct 2026: arts. 53, 97 Nos. 2, 3, 4, 10, 11 | https://www.bcn.cl/leychile/navegar?idNorma=6374 | 2026-11-11 |
| Read for the figures named: SII FAQ 001.130.1060 (updated 17 Jun 2025), F29 due dates 12, 20 and 28 | https://www.sii.cl/preguntas_frecuentes/impuestos_mensuales/001_130_1060.htm | 2026-11-11 |
| Read for the figures named: SII MIPYME portal, F29 by day 20 (who qualifies, D.S. 1.001 of 2006) | https://www.sii.cl/portales/mipyme/f29/ | 2026-11-11 |
| Read for the figures named: SII Formulario 29 form image (lines 1 to 144, codes) | https://www.sii.cl/formularios/imagen/F29.pdf | 2026-11-11 |
| Read for the figures named: SII, Formato Documentos Tributarios Electrónicos v2.2 (DTE type codes; withholding codes and usual rates) | https://www.sii.cl/factura_electronica/factura_mercado/formato_dte.pdf | 2026-11-11 |
| Read for the figures named: SII UTM/UTA 2026 (October to December UTM) | https://www.sii.cl/valores_y_fechas/utm/utm2026.htm | 2026-11-11 |
| Read for the figures named: SII daily penal interest (7.70%, Jul to Dec 2026) | https://www.sii.cl/valores_y_fechas/otros_valores/tasa_interes_penal_diario.html | 2026-11-11 |
| Read for the figures named: SII news of 19 Oct 2026 on Ley 21.850 (new-housing IVA exemption from the first business day of December 2026, for one year) | https://www.sii.cl/noticias/2026/191026noti01pcr.htm | 2026-11-11 |

Not yet confirmed: the text of D.S. 1.001 of 2006 itself (the day 20 rule is taken from SII's pages); the current sector withholding rates for cambio de sujeto (the DTE format gives the usual rates; each sector has its own SII resolution); the proportional credit rules of the Reglamento (D.S. 55 of 1977), not read; the construction companies' special credit (DL 910 art. 21), not read; whether the F29 form image on sii.cl matches every code of the 2026 on-screen form; the rounding SII applies to the updated remanente.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `cl-vat-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/cl-vat-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
