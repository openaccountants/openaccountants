---
name: peru-igv
description: >
  Compute, classify and prepare Peru's monthly Impuesto General a las Ventas
  (IGV) and Impuesto de Promoción Municipal (IPM) for tax year 2026. Covers
  businesses and habitual suppliers, registration in the RUC, ordinary domestic
  goods and services, imports and exported services, output tax, documentary and
  substantive input-credit conditions, mixed-use purchases, carried credits,
  retenciones, percepciones and construction detracciones. Includes the 2026 rate
  composition, hospitality MYPE eligibility, SIRE records, Formulario Virtual 621
  fields, filing and payment, and the July 2026 imported-service payment module.
  Use for "Peruvian VAT", "IGV return", "SUNAT 621", "crédito fiscal", "RUC",
  "exportación de servicios", or "detracción". Produces a reconciled working paper
  and exceptions for a Peruvian professional to review before filing.
version: 2.1
jurisdiction: PE
tax_year: 2026
last_updated: 2026-11-11
depends_on:
  - vat-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: computation
---

# Peru IGV and IPM v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick reference:** ordinary taxable operations in 2026 bear a combined 18%, composed of 15.5% IGV and 2.5% IPM. Qualifying hospitality MYPE operations bear 10.5%. Compute monthly output tax less legally eligible input credit, then apply the distinct carried-credit, retention, perception and payment balances. A foreign payment, a bank narration or a supplier's name does not establish tax treatment. [LIGV arts. 11-17 and Ley 32387 transitional note](https://www.sunat.gob.pe/legislacion/igv/ley/capitul5.pdf); [SUNAT 2026 rate composition](https://emprender.sunat.gob.pe/principales-impuestos/impuesto-general-las-ventas-igv/impuesto-general-las-ventas).

**Required inputs:** period and RUC/regime; transaction and customer location; invoices and adjustment notes with SUNAT validity; use of each purchase; preceding return and credit balances; import, export, collection-system and payment evidence. Resolve these before applying a rate or claiming credit.

## Who this applies to

This guide loads on top of `vat-workflow-base` for Peru, in PEN (S/), for calendar-month periods in 2026. It covers ordinary sales of movable goods in Peru, domestic provision or use of services, construction contracts, builders' first property sales at the identification stage, and imports. Individuals, companies, estates and the other business forms in LIGV art. 9.1 are taxpayers when they carry out the listed activities. Nonbusiness persons can be taxable on imports and on habitual supplies; resale is habitual. There is no general turnover allowance below which a taxable business can simply ignore IGV. Classify the activity and regime before registering its tax obligations. [LIGV arts. 1-4](https://www.sunat.gob.pe/legislacion/igv/ley/capitul1.pdf), [art. 9](https://www.sunat.gob.pe/legislacion/igv/ley/capitul3.pdf).

Régimen Especial de Renta (RER), Régimen MYPE Tributario and Régimen General taxpayers ordinarily use the monthly IGV credit/debit mechanism. Nuevo RUS has its own unified payment and documents; it does not give a business buyer an IGV credit on a boleta. Being small or using RER does not turn taxable sales into exempt sales. Independent personal professional income must be distinguished from a business's third-category services before charging IGV. The LIGV service definition is tied to third-category income, not to the occupation's title. [LIGV art. 3(c)](https://www.sunat.gob.pe/legislacion/igv/ley/capitul1.pdf); [SUNAT FV621 scope](https://orientacion.sunat.gob.pe/01-formulario-virtual-ndeg-621-igv-renta-mensual); [Comprobantes Regulation art. 4](https://www.sunat.gob.pe/legislacion/comprob/regla/capituloI.pdf).

Ordinary mixed taxable/exempt businesses are covered by the credit allocation below. Specialist review is required for real-estate land valuation, detailed SPOT/agent administration, export refunds, early IGV recovery, Amazonía, ZED/ZOFRATACNA and nonresident consumer-digital registration. These are identified in this guide so that ordinary work routes to the correct process; this guide does not calculate those specialist regimes in full.

## Rates, bands and thresholds

Each figure is for 2026 unless another period is expressly stated. "IGV" in the computation and FV621 generally includes IPM; do not add IPM again to the combined rate.

| Item | Amount and adjacent conditions | Official source |
|---|---|---|
| Ordinary taxable goods, services, construction and imports | 18% combined throughout 2026: 15.5% IGV + 2.5% IPM. Ley 32387 changes the composition from 1 January 2026, not the combined burden. | LIGV art. 17, Ley 32387 art. 2 and fourth final provision, [consolidated note](https://www.sunat.gob.pe/legislacion/igv/ley/capitul5.pdf); [SUNAT rate table](https://emprender.sunat.gob.pe/principales-impuestos/impuesto-general-las-ventas-igv/impuesto-general-las-ventas) |
| Restaurant, hotel and tourist-accommodation MYPE | 10.5% combined in 2026: 8% IGV + 2.5% IPM; the business must meet the sales, principal-activity and economic-linkage tests below. Not a general reduced rate for every restaurant invoice. | Ley 31556 as amended by Ley 32219; [SUNAT eligibility and 2026 table](https://orientacion.sunat.gob.pe/reduccion-del-igv-para-restaurantes-hoteles-y-alojamiento-turisticos-1) |
| Hospitality eligibility limits | Annual sales up to 1,700 UIT; qualifying activity supplies at least 70% of total income. SUNAT specifies the twelve months preceding the previous month, or the period from starting activity, and aggregates income from the regimes used. Economically linked enterprises/groups are excluded. | Same [SUNAT eligibility page](https://orientacion.sunat.gob.pe/reduccion-del-igv-para-restaurantes-hoteles-y-alojamiento-turisticos-1), DS 237-2022-EF and DS 008-2008-TR art. 4 |
| UIT | S/ 5,500 for 2026. Use the UIT year prescribed by the specific rule; IGV Justo uses the preceding year's UIT for its turnover test. | DS 301-2025-EF, [SUNAT UIT table](https://www.sunat.gob.pe/indicestasas/uit.html) |
| Exports | No output IGV when LIGV art. 33 conditions are satisfied; legally "no están afectos", not an ordinary exempt domestic sale. Qualifying inputs can generate exporter credit under art. 34. | [LIGV arts. 33-35](https://www.sunat.gob.pe/legislacion/igv/ley/capitul9.pdf) |
| Appendix I and II exemptions | Specific listed goods/services remain exempt through 31 December 2028. Match the description/tariff line and conditions and check any effective Appendix I waiver. | LIGV arts. 5-7 as amended by Ley 32542, [chapter II](https://www.sunat.gob.pe/legislacion/igv/ley/capitul2.pdf); [Appendix I](https://www.sunat.gob.pe/legislacion/igv/ley/apendiceI.pdf); [Appendix II](https://www.sunat.gob.pe/legislacion/igv/ley/apendice2.pdf) |
| IGV retention received | 3% of the tax-inclusive payment by a designated agent. The S/ 700 exception requires both payment and total relevant invoice amounts not to exceed that amount. No retention on an operation subject to SPOT; inspect the other exclusions and partial payments. | RS 037-2002/SUNAT arts. 3, 5(f), 6 as amended by RS 033-2014; [retention rules](https://www.sunat.gob.pe/legislacion/superin/2002/037.htm); [SUNAT detailed FAQ, question 15](https://orientacion.sunat.gob.pe/06-preguntas-frecuentes-regimen-de-retenciones) |
| Import perceptions | 10% for listed importer-risk conditions, including first import as specified in the customs guidance; 5% for used goods where the higher rate does not apply; 3.5% otherwise. Check exclusions and sensitive-goods fixed-amount comparisons. These are advances, not extra input IGV. | Ley 29173 arts. 18-19, [SUNAT customs perception conditions](https://www.sunat.gob.pe/orientacionaduanera/pagosgarantias/) |
| Internal-goods/fuel perceptions | Listed domestic goods: 2% normally, 0.5% where credit-supporting document and the qualifying perception-agent customer condition apply. Fuel: 1% of price, subject to the customer exclusions, including final consumers who do not trade the fuel. | [SUNAT perception rates and exclusions](https://emprender.sunat.gob.pe/principales-impuestos/impuesto-general-las-ventas-igv/regimen-percepciones-igv); RS 128-2002 art. 4 [fuel rule](https://www.sunat.gob.pe/legislacion/superin/2002/128.htm) |
| Construction SPOT | 4% of the total operation for qualifying construction contracts, normally when greater than S/ 700 and no document/other exclusion applies. Equipment-with-operator rental alone is excluded from the construction definition in Annex 3 item 9. | RS 183-2004 arts. 12-16, [rules](https://www.sunat.gob.pe/legislacion/superin/2004/183.htm); [SUNAT Annex 3](https://orientacion.sunat.gob.pe/apendices-del-sistema-de-detracciones) |
| Ordinary business consulting SPOT | 12% of the total operation under Annex 3 item 5, subject to the greater-than-S/ 700 and document/population tests; residual domestic business services require the actual item 10 classification/exclusions. Do not apply a simultaneous 3% retention. | RS 183-2004 arts. 12-16; [current Annex 3 items 5/10, table effective 1 April 2018](https://orientacion.sunat.gob.pe/apendices-del-sistema-de-detracciones); [RS 037 art. 5(f)](https://www.sunat.gob.pe/legislacion/superin/2002/037.htm) |
| Required payment means | Obligations from S/ 2,000 or US$ 500 require qualifying payment means, including where split into smaller payments. Check statutory exceptions; failure can defeat IGV credit. | Ley 28194 TUO arts. 3-5, 8, amended by DL 1529, [official consolidation](https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf) |
| Ordinary purchase-record timing | Record eligible documents in the issue/payment month, as applicable, or one of the following twelve months and claim in the recorded period, subject to the qualifications below. | Ley 29215 art. 2 [gazette text](https://www.sunat.gob.pe/legislacion/nor_graf/2008/abril/nl20080423.pdf); [SUNAT interpretation 052-2018](https://www.sunat.gob.pe/legislacion/oficios/2018/informe-oficios/i052-2018-7T0000.pdf); [RS 047-2026 recitals](https://www.sunat.gob.pe/legislacion/superin/2026/000047-2026.pdf) |
| Representation expenditure supporting input credit | Qualifying expenditure, rather than the tax credit itself, is limited to 0.5% of accumulated calendar-year gross income through the month, capped cumulatively at 40 UIT annually. Compute credit on the eligible expenditure, subject to all general credit conditions. | IGV Regulation art. 6(10), [chapter V](https://www.sunat.gob.pe/legislacion/igv/regla/cap5.pdf) |

Hospitality eligibility must be tested month by month using the prescribed lookback. SUNAT states that failure or renewed satisfaction of the sales/activity limits changes the rate from the first day of the second month after the last month used for the check ("mes subsiguiente al último que se empleó"). Retain the income schedule and economic-group analysis. An invoice alone does not prove entitlement. Do not use the older 10% combined example in the FV621 help document for 2026; the current hospitality page expressly gives 10.5%.

## The base

### Output tax, timing and classification

1. Establish the taxable event before matching cash. Goods: earlier of the required invoice issue or delivery; services: earlier of required invoice issue or receipt of remuneration; electricity, water and final telephone services: earlier of payment or due date. Construction: earlier of required invoice issue or receipts, including progress payments. First builder property sale: each receipt. Imported services: earlier of recording the foreign invoice in the purchase register or paying the supplier. Tangible imports: customs clearance request. These rules prevent treating every bank receipt as the current month's sales. [LIGV art. 4](https://www.sunat.gob.pe/legislacion/igv/ley/capitul1.pdf).
2. Determine the net sale price, entire service consideration or construction value. The base includes ancillary charges and qualifying financing charges under art. 14; use credit/debit notes for changes. The first builder sale excludes land; seek the separate valuation computation rather than taxing the full property receipt. Tangible import base is customs value plus import duties and taxes other than IGV. [LIGV arts. 12-16](https://www.sunat.gob.pe/legislacion/igv/ley/capitul5.pdf); [Regulation art. 7 adjustments](https://www.sunat.gob.pe/legislacion/igv/regla/cap6.htm).
3. Apply the applicable combined rate to each base. For a confirmed ordinary tax-inclusive amount, net = total / 1.18 and tax = total - net. For confirmed eligible hospitality, divide by 1.105 instead. These are arithmetic consequences of the cited rates, not permission to infer a missing invoice or rate.
4. Separate exports, exempt operations and operations outside scope. Taxable withdrawals by an owner or the business can create output tax without a bank receipt, subject to art. 3(a) exclusions for specified production use, working conditions and duly evidenced loss. Tax on withdrawals does not give the recipient input credit. [LIGV arts. 3](https://www.sunat.gob.pe/legislacion/igv/ley/capitul1.pdf), [20](https://www.sunat.gob.pe/legislacion/igv/ley/capitul6.pdf).
5. Sum output IGV, subtract eligible adjusted input IGV, apply the preceding month's purchase-credit balance, then other statutory credits and payments in the return's order. Excess purchase credit carries to subsequent months; it is not generally an immediate cash refund. Keep retention/perception balances separate. [LIGV art. 11](https://www.sunat.gob.pe/legislacion/igv/ley/capitul4.htm), [25](https://www.sunat.gob.pe/legislacion/igv/ley/capitul6.pdf), [29-31](https://www.sunat.gob.pe/legislacion/igv/ley/capitul8.pdf).

### Input-credit conditions

A purchase must be an allowable business cost/expense for income-tax purposes and destined for taxable transactions or qualifying exports. The IGV must be separately identified in a document that legally supports credit; verify issuer identity, RUC, authorization at issue, transaction reality, and required invoice information. A bank debit or an unvalidated PDF alone proves neither the taxable purchase nor its credit. Authorized utility, customs and other special documents can support credit under their rules; a factura is not the only valid document. Retain the CPE/XML, SUNAT/OSE acceptance evidence, contracts, receipt/delivery and payment evidence. [LIGV arts. 18-19](https://www.sunat.gob.pe/legislacion/igv/ley/capitul6.pdf); [Regulation art. 6(2)](https://www.sunat.gob.pe/legislacion/igv/regla/cap5.pdf).

Record documents in the proper purchase register and period. Ley 29215 art. 2 provides the issue/payment month or following twelve months. If credit was exercised before registration, the late-recording protection and the limit of a SUNAT request must be checked; it is not unlimited late claiming. [SUNAT Informe 052-2018](https://www.sunat.gob.pe/legislacion/oficios/2018/informe-oficios/i052-2018-7T0000.pdf). DL 1669 proposes different timing, but its sole final provision makes commencement depend on an implementing SUNAT resolution; do not treat its publication or a SIRE enrollment postponement as the trigger. The current consolidated arts. 19/23 and the March 2026 RS 047 recitals read for this guide retain the existing rules. Its transitional provision preserves the old rules for documents issued before commencement. [DL 1669, final and transitional provisions](https://leyes.congreso.gob.pe/Documentos/2021_2026/Decretos/Legislativos/2024/DL-1669.pdf).

Further checks:

- **Boletas/Nuevo RUS:** no input credit. A separate income-tax allowance for certain Nuevo RUS boletas is not an IGV allowance. Do not claim a proportion of boleta expenditure as IGV. [Comprobantes Regulation art. 4(3.2)](https://www.sunat.gob.pe/legislacion/comprob/regla/capituloI.pdf).
- **Utilities:** art. 21 allows electricity, water and final telephone credit at earlier payment/due date, subject to the other conditions. A tenant can use a landlord-addressed utility document only under the lease/document conditions in Regulation art. 6(2.1)(d), not merely because the office uses the supply. [LIGV art. 21](https://www.sunat.gob.pe/legislacion/igv/ley/capitul6.pdf); [Regulation](https://www.sunat.gob.pe/legislacion/igv/regla/cap5.pdf).
- **Imported services:** pay the tax and record both the foreign document, if issued, and the payment document; credit cannot precede payment. Apply business-use and prorrata restrictions too. [LIGV arts. 18-21](https://www.sunat.gob.pe/legislacion/igv/ley/capitul6.pdf); [Regulation art. 6(11)](https://www.sunat.gob.pe/legislacion/igv/regla/cap5.pdf).
- **Payment means/SPOT:** enforce bancarización when payment occurs, and retain the required detracción deposit evidence before allowing the corresponding credit period. A supplier's Banco de la Nación balance is not a buyer's input-credit approval. [Ley 28194 art. 8](https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf); [DL 940 first final provision](https://www.sunat.gob.pe/legislacion/detracciones/).
- **Corrections and disposals:** use valid notes for returns, discounts and cancellations. Fixed assets sold below cost within two years of commissioning can require proportional credit repayment in the sale month. A shorter technological replacement cycle requires a technical report from the relevant sector Ministry; even in that case, sale before one year of operation still requires proportional repayment. A taxpayer's own report alone is insufficient. Loss/destruction can require repayment, subject to the duly supported statutory exclusions, including force majeure, crime, fully depreciated fixed assets and qualifying merma/desmedro. [LIGV art. 22](https://www.sunat.gob.pe/legislacion/igv/ley/capitul6.pdf).

### Mixed taxable/exempt operations and private use

First allocate purchases directly: taxable/export use is eligible if other conditions hold; exclusively exempt/out-of-scope use is ineligible. For genuinely common purchases, apply the statutory prorrata: (taxable operations + exports) / (taxable + exports + relevant nongraved operations), for the preceding twelve-month period including the current month. Express the percentage to two decimals and apply it to common input IGV. New/restarted businesses accumulate from starting/restarting until twelve months are available. Exclude imports and use of nonresident services from the turnover fraction; their common-use input tax is still subject to that fraction. Not every accounting receipt belongs in the denominator: apply the specific inclusions/exclusions in Regulation art. 6(6.2). Retain a reconciliation to FV621's ratio. [LIGV art. 23](https://www.sunat.gob.pe/legislacion/igv/ley/capitul6.pdf); [Regulation art. 6(6)](https://www.sunat.gob.pe/legislacion/igv/regla/cap5.pdf); [SUNAT Informe 016-2024](https://www.sunat.gob.pe/legislacion/oficios/2024/informe-oficios/i000016-2024-7T0000.pdf).

Private consumption, unproven business use and employee benefits do not become creditable just because the company paid. Obtain vehicle, telephone and premises-use evidence and the income-tax cost test; then apply direct allocation/prorrata as applicable. Hold unsubstantiated credit pending documents instead of inventing a business-use percentage.

### Supplier-pattern checks, including old bank-statement aliases

The names below are recognition keywords from earlier working papers, not proof of the named entity's current ownership, tax registration, service or rate. Classify each invoice line and the legal supplier.

| Transaction family and recognition keywords | Classification instruction and source |
|---|---|
| Banking: BCP, BBVA, Interbank, Scotiabank, BanBif, MiBanco; Yape, Plin | Match the exact credit/commission/remittance service and authorized financial entity to art. 2(r). Ordinary money transfers and loan principal are not sales consideration. Do not presume every bank or payment-app charge is exempt. Art. 2(r) was amended by Ley 32549 in January 2026 to add qualifying military/police housing-fund mortgage income. [LIGV art. 2(r)](https://www.sunat.gob.pe/legislacion/igv/ley/capitul1.pdf) |
| Card/POS/payment processing: VisaNet, Niubiz, Culqi | A separately charged business processing/terminal service is tested under ordinary domestic-service rules; the financial exclusion depends on the legal service and supplier, not the word "payment". Credit requires the supporting document and taxable use. [LIGV arts. 2(r), 3(c)](https://www.sunat.gob.pe/legislacion/igv/ley/capitul1.pdf), [18-19](https://www.sunat.gob.pe/legislacion/igv/ley/capitul6.pdf) |
| Electricity/water/gas: Luz del Sur, Enel/Edelnor, Hidrandina, Electrosur, SEDAPAL, Cálidda/Gas Natural Fenosa | Ordinary taxable utility supply; apply the electricity/water timing exception where relevant and credit only for qualifying use/documents. A bank payment does not replace the bill. [LIGV arts. 4(c)](https://www.sunat.gob.pe/legislacion/igv/ley/capitul1.pdf), [18-21](https://www.sunat.gob.pe/legislacion/igv/ley/capitul6.pdf) |
| Telecom: Entel, Movistar/Telefónica, Claro, Bitel, Win | Test business use, actual supplier, document and service type; final telephone services have the art. 21 timing rule, while other digital services follow their own rules. [LIGV arts. 3-4](https://www.sunat.gob.pe/legislacion/igv/ley/capitul1.pdf), [21](https://www.sunat.gob.pe/legislacion/igv/ley/capitul6.pdf) |
| Passenger transport: LATAM, Sky, Star Perú, Metropolitano, Metro de Lima, Uber, InDriver, Cruz del Sur | Domestic air transport is outside the Appendix II public-passenger exemption. Public ground passenger transport can qualify; railway is excluded except the expressly included Lima/Callao mass-electric system. Identify the actual taxi/transport service separately from a digital-platform commission. International flights are not automatically exports: art. 3(c) taxes qualifying tickets issued in Peru or bought abroad for use from Peru. [Appendix II(2)](https://www.sunat.gob.pe/legislacion/igv/ley/apendice2.pdf), [LIGV art. 3(c)](https://www.sunat.gob.pe/legislacion/igv/ley/capitul1.pdf) |
| Courier/freight/post: Olva, Urbano, DHL, FedEx, Serpost | Domestic courier is tested as domestic service. Appendix II(3) exempts qualifying inbound/outbound international freight; it does not make every international courier charge an export. Appendix II(14) covers the specified foreign postal-administration compensation, not all postal receipts. [Appendix II](https://www.sunat.gob.pe/legislacion/igv/ley/apendice2.pdf) |
| Fuel: Primax, Pecsa, Petroperú, Repsol | Separate taxable fuel, any ISC in the taxable base, and any eligible perception. Credit requires qualifying business cost/use and documentation; an ordinary end-user fuel purchase is excluded from the resale-fuel perception system. [LIGV art. 14](https://www.sunat.gob.pe/legislacion/igv/ley/capitul5.pdf); [SUNAT fuel exclusions](https://emprender.sunat.gob.pe/principales-impuestos/impuesto-general-las-ventas-igv/regimen-percepciones-igv) |
| Retail/office: Wong, Metro, Plaza Vea, Tottus, Sodimac, Office Depot, Falabella | Split mixed taxable/exempt invoice lines. Food, agricultural/fishing products or medical goods are exempt only when the precise description/tariff item or special law qualifies; a supermarket is not wholly exempt. [Appendix I](https://www.sunat.gob.pe/legislacion/igv/ley/apendiceI.pdf), [LIGV arts. 5-7](https://www.sunat.gob.pe/legislacion/igv/ley/capitul2.pdf) |
| Accounting/cloud/invoicing: Contasimple, Alegra, Facturador SUNAT, Efact; Microsoft/Azure/M365, Google/Workspace/Ads, Zoom, AWS | Identify domestic supplier versus nonresident invoice and business versus consumer user. Apply the imported-service method below where appropriate. A no-charge tool produces no charged input tax. A brand or Peruvian billing address does not establish a domestic invoice or foreign-provider collection. [LIGV arts. 3-4](https://www.sunat.gob.pe/legislacion/igv/ley/capitul1.pdf), [49-A](https://www.sunat.gob.pe/legislacion/igv/ley/capitul12.pdf) |
| Accountant/CPC, lawyers, advertising, consulting, notaries, medical/health providers | Distinguish independent personal services from third-category business services. There is no blanket exemption here for medical or professional services. A business's taxable invoice can support credit; a personal honorarium without IGV cannot. [LIGV art. 3(c)](https://www.sunat.gob.pe/legislacion/igv/ley/capitul1.pdf) |
| Insurance: Rimac, Pacífico, La Positiva, Mapfre | Do not exempt all policies. Art. 2(s) covers specified life policies issued by lawful Peruvian insurers to resident individuals and the stated related premiums; art. 2(j) separately addresses pension-system services. Business property/motor policies require their own tax/document review. [LIGV art. 2(j), (s)](https://www.sunat.gob.pe/legislacion/igv/ley/capitul1.pdf) |
| Education and rent | Education requires the qualifying institution, its own purposes and specified goods/services under art. 2(g). Rent outside scope under art. 2(a) depends on first/second-category income; a residential description alone does not exempt a company's third-category letting, and commercial use alone does not convert a personal landlord into a taxable company. [LIGV art. 2](https://www.sunat.gob.pe/legislacion/igv/ley/capitul1.pdf) |

## Deadlines and filing

### Registration and invoice controls

Register the person/entity in the RUC and obtain Clave SOL before doing the taxable business workflow. The RUC is an eleven-digit identifier; record the start date, fiscal address, activity, regime and tax obligations and download the CIR/registration evidence. Eligible natural persons can use SUNAT Virtual/App Personas; entities use the entity registration process or their registered representative. Confirm active status and tax affectation, not just that a number exists. [SUNAT RUC registration](https://www.gob.pe/284-sacar-ruc-persona-natural); [SUNAT updating business obligations](https://centrovirtual.sunat.gob.pe/tramites/actualizar-datos-ruc).

Issue the proper factura for credit-supporting business sales and exports, and boleta for the appropriate consumer sales; follow the designated SEE electronic system and contingency rules. Validate electronic acceptance and issuance/transmission. For SEE del Contribuyente, SFS and OSE facturas and linked notes, transmit on the issue date or within a maximum of three calendar days counted from the following calendar day; other document types have their own deadlines. Save the CDR/validation and invoice, not merely the bank reference. [Comprobantes Regulation art. 4](https://www.sunat.gob.pe/legislacion/comprob/regla/capituloI.pdf); [RS 003-2023 arts. 3-5](https://www.sunat.gob.pe/legislacion/superin/2023/000003-2023.pdf); [SUNAT CPE FAQ, including question 15 correcting the older one-day passage](https://cpe.sunat.gob.pe/informacion_general/preguntas_frecuentes).

### Monthly return, calendar and payment

IGV is declared for the preceding calendar month, with taxable/exempt operations, credits and retentions/perceptions. Filing and payment are ordinarily due within the following month on the RUC-specific SUNAT date. Zero payable does not itself end the filing obligation. Do not use a fixed "8th-22nd" range or a supposed first-twelve-business-days deadline. [LIGV arts. 29-30](https://www.sunat.gob.pe/legislacion/igv/ley/capitul8.pdf).

For the October 2026 period, the general due dates are: RUC 0: 16 November; 1: 17 November; 2/3: 18 November; 4/5: 19 November; 6/7: 20 November; 8/9: 23 November; Buenos Contribuyentes/UESP: 24 November. December 2026 falls due on the corresponding dates in January 2027. Read the taxpayer's actual calendar and any disaster-area extension for the period. [SUNAT 2026 calendar, RS 281-2022 Annex I](https://www.sunat.gob.pe/orientacion/cronogramas/2026/cObligacionMensual2026.html); [2026 emergency extensions](https://orientacion.sunat.gob.pe/Prorroga-de-vencimientos-de-declaraciones-y-pagos-mensuales-1).

1. Reconcile invoices, customs evidence, notes and bank movements to the sales/purchase registers. SIRE's RVIE and RCE proposal is a starting point: supplement, correct or replace it with proper supporting records. Retain generation and inconsistency evidence. The affected larger PRICOS' start was postponed to **October 2026**, for those designated at 31 December 2024 with 2024 net income above 2,300 UIT; RS 125 supersedes the earlier June start. [RS 000125-2026 arts. 1, 3-4](https://www.sunat.gob.pe/legislacion/superin/2026/000125-2026.pdf).
2. Enter SUNAT Virtual → Operaciones en Línea → Mis Declaraciones y Pagos → Formulario Virtual 621 IGV-Renta Mensual (Declara Fácil). Confirm RUC, month/year, original/substitute/rectifying status, registered income-tax regime and the question about nongraved sales in the preceding twelve months. Complete the applicable electronic registers before relying on their proposed amounts. [SUNAT FV621 help, sections I-II](https://orientacion.sunat.gob.pe/sites/default/files/inline-files/ayuda_621_igv_renta_mensual_ccv.pdf).
3. Review the sales, purchase and ratio fields below. Enter the legally correct 2026 rate/transactions; the help PDF still contains older hospitality-rate captions. Do not copy those superseded rates into a 2026 return. Investigate proposal differences and retain the working-paper explanation. Complete the separate income-tax part using `pe-corporate-income-tax`, not the IGV computation.
4. Review Determinación de la deuda, brought-forward purchase credits, perceptions, retentions, prior payments and any interest. Validate, add to the basket and submit/pay. Save the Constancia de Presentación and payment receipt; where using NPS for ordinary domestic IGV, retain the number and bank confirmation. Filing acceptance is not payment. An amount paid below the debt leaves the balance collectible. [FV621 help, section III](https://orientacion.sunat.gob.pe/sites/default/files/inline-files/ayuda_621_igv_renta_mensual_ccv.pdf); [SUNAT declaration submission](https://orientacion.sunat.gob.pe/declaracion-simplificada-personas).
5. Compare the accepted return to the signed working paper, allocate unused credit types separately to the next period, and resolve any corrections through the appropriate substitute/rectifying return. The current guide prepares a review package; it does not authorize submission without client authority.

| FV621 field | What it represents in SUNAT's help |
|---|---|
| 100 / 101 | Ordinary net taxable sales base / output tax. 105 is not output tax. |
| 154 / 155 | Qualifying hospitality sales base / tax; use the actual period's lawful rate. |
| 102 / 103; 131 | Prior-period sales discounts/returns and tax adjustments; aggregate sales tax. |
| 106 / 127 | Invoiced exports / exports shipped in the period, with the separate service treatment described by the help. 107 is not export sales. |
| 105 / 109 | Nongraved sales with ratio effect / without ratio effect, subject to the statutory classifications. |
| 107 / 108 | Domestic taxable purchases allocated to taxed sales / associated tax. |
| 110 / 111; 173 | Common domestic purchases / apportioned tax; prorrata coefficient. |
| 114 / 115; 116 / 117 | Taxable imports allocated exclusively to taxed/export operations, or to common use, and corresponding tax. |
| 113 / 119; 120 / 122 | Taxed purchases allocated to nongraved operations (domestic/imported); domestic/imported nongraved purchases. These do not simply equal claimable credit. |
| 140 / 145 / 184 | Current output less purchase credit; previous purchase-credit balance; resulting tax or balance. C184 = C140 - C145. |
| 171 / 179; 168 / 176 | Current/previous unused perceptions; current/previous unused retentions. |
| 185 / 187 / 188 / 189 | Prior payments of the same domestic IGV code; interest; total debt; chosen amount to pay. Tax code 1041 imported-service payments are not domestic prior payments. |

Source for every field: [SUNAT FV621 help, sections II-III](https://orientacion.sunat.gob.pe/sites/default/files/inline-files/ayuda_621_igv_renta_mensual_ccv.pdf). The ordinary total-debt formula is C188 = C184 - (C171 + C168 + C179 + C176 + C185) + C187, subject to allowed-credit limits and the separate balances the form retains. Casilla 189 is the amount chosen to pay; it is not "105 - 125 - 140". Do not use the old guide's casilla 125/190 map.

### IGV Justo, collection systems and working-paper deliverable

IGV Justo postpones payment, not the monthly declaration. Eligible MYPE selling goods/services or performing construction with annual sales up to 1,700 UIT may elect by the original return deadline for payment at the third following period's due date. The annual-sales test uses the previous calendar year's sales and UIT, with startup rules. Exclusions include enforceable debt above one UIT, tax-crime convictions of owner/partners, insolvency proceedings and prior IGV/renta noncompliance, subject to the stated regularization route. Check the SUNAT eligibility register and mark the option in FV621. Interest begins after the extended due date if unpaid. [LIGV art. 30](https://www.sunat.gob.pe/legislacion/igv/ley/capitul8.pdf); [SUNAT IGV Justo eligibility, exclusion and election rules](https://emprender.sunat.gob.pe/principales-impuestos/impuesto-general-las-ventas-igv/igv-justo).

Reconcile retenciones and percepciones to certificates, agents and prior returns; they offset payable IGV, not the purchase-tax total. Unused balances carry; art. 31 allows a refund request after at least three consecutive periods without use and subject to its declared-balance conditions, or the prescribed compensation route. Agent remittance/returns are a separate obligation, not discharged by recording a supplier credit in 621. [LIGV art. 31](https://www.sunat.gob.pe/legislacion/igv/ley/capitul8.pdf).

For a qualifying construction SPOT contract, the buyer normally deposits the percentage into the supplier's Banco de la Nación detracción account by the earlier of partial/full payment and the fifth business day of the month after annotation in the purchase register. If the supplier receives the full price without evidence of deposit, the supplier has its own deposit obligation. Check RS 183 arts. 12-16 and the actual Annex 3 classification. Reconcile invoice gross price to supplier cash plus detracción; never subtract the deposit from the invoice's output IGV. [SUNAT SPOT operation and timing guidance](https://emprender.sunat.gob.pe/principales-impuestos/impuesto-general-las-ventas-igv/sistema-detracciones-igv), [RS 183-2004](https://www.sunat.gob.pe/legislacion/superin/2004/183.htm).

Deliver tabs `Output_Sales`, `Input_Purchases`, `Retenciones_Percepciones`, `PDT621_Summary` and `Open_Items`. Columns: date/tax point, counterparty and RUC, invoice/credit-note identifier and type, PEN base, IGV/IPM rate and amount, export/exempt basis, business-use allocation, register period, SPOT evidence, credit category, source document and unresolved issue. Keep the old `Tier2_Items` tab name only as a legacy alias for `Open_Items`; an unanswered client fact is not a statutory trust tier.

For bank ingestion, "Abono" means money in and "Débito/Cargo" money out; match them to the invoice and receivable/payable, not automatically to output/input tax. "Detracción/Banco Nación" prompts the separate deposit reconciliation; "Transferencia Internacional" prompts export or imported-service tests. Read each bank export's numeric convention: illustrative `590.000,00` and `590,000.00` both denote 590000 where those respective formats are used. Do not treat the old BCP/BBVA/Interbank/Scotiabank display examples as mandatory bank formats.

If CPEs are missing, hold input credit and request document identifiers, XML/valid representations and validation. Back-calculate a bank amount only as a clearly labeled provisional reconciliation after establishing it is tax-inclusive ordinary consideration, excluding loans, transfers, deposits and settlement differences. Do not manufacture output classification, an exemption waiver or an export from a "conservative default". Quantify the potential tax effect of each unresolved classification and require professional review before filing.

## Penalties and interest

**First test the mandatory preventive-training gate.** Under [Tax Code arts. 165/180, amended by Law 32335](https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf), a qualifying microenterprise with annual sales up to 150 UIT, in any tax regime, must receive the first-infringement training process before the corresponding fine/closure sanction. This is separate from discretionary relief and ordinary graduality.

Apply [DS 288-2025-EF arts. 3-11](https://www.mef.gob.pe/es/por-instrumento/decreto-supremo/34781-decreto-supremo-n-288-2025-ef/file): test each independent infringement item in arts. 173-178, not one allowance for each broad art. 172 category. Check art. 5's actual alternatives involving fine/closure notification, non-sanction/100% relief, Table III note-3 payment, recognition act and course communication; do not reduce them to 'first ever error'. For 2026, ordinarily sum prior-year monthly declared net income for General/RMT/RER, or gross income for Nuevo RUS, including effective amendments by commission/detection date, using that year's UIT. With no prior-year activity, the business is presumed within the limit unless current-year expired-period declarations exceed it. More than one omitted required monthly return defeats the test unless a filing exemption applies. Check final proprietor/partner tax/customs convictions; RUC reactivation does not erase history. Same-day same-type first breaches get the course for only one, the most onerous where fines differ; the others remain sanctionable.

Under [RS 010-2026 arts. 5-8](https://www.sunat.gob.pe/legislacion/superin/2026/000010-2026.pdf), read the actual SOL buzón notification for the course URL, credentials and nonextendable five-business-day access window. The taxpayer or entity's legal representative completes the course and final activity, obtains and saves the constancia within that window. Incomplete attendance permits the applicable sanction. Training does not pay tax or interest; DS 288 art. 10(f) bars refund/compensation of relevant payments made before course completion. Record the gate's outcome before treating any table amount below as a payable fine.

| Failure | Rule and limits | Official source |
|---|---|---|
| Late payment of PEN tax | TIM currently 0.90% monthly; daily rate is monthly TIM / 30, applied to unpaid tax from the day after due date through payment. Check any applicable statutory suspension and effective rates over the delay. | Código Tributario art. 33; RS 044-2021 sole article; [SUNAT current TIM table](https://www.sunat.gob.pe/indicestasas/tim.html), [resolution](https://www.sunat.gob.pe/legislacion/superin/2021/044-2021.pdf) |
| Late determining return, Table I business | Art. 176(1) base fine: 1 UIT for Table I persons/entities, including RMT. Table II applies to its own taxpayers; the applicable graduality/discretion and correction date can reduce the actual fine. | [Código Tributario, art. 176 and Table I](https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf) |
| Under-declaration, Table I | Art. 178(1) base: 50% of omitted tax payable, or 100% of an improperly obtained refund, subject to the table notes including the applicable minimum and calculation method. Do not substitute a blanket percentage of all credit disallowed. | [Código Tributario, art. 178, Table I and note 21](https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf) |
| Records/invoices and agency defaults | Arts. 174-175 address documentary/register failures; art. 178(4) addresses unpaid retained/perceived tax. The exact table, act, period, notice stage and relief must be established before quoting a payable fine. | [Código Tributario, Book IV and sanction tables](https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf) |
| Interest on a fine | Since 1 January 2024, art. 181 uses Civil Code art. 1244 legal interest from the date payment of the fine is demanded; the tax TIM is not the fine-interest rate. | [Código Tributario art. 181](https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf); [SUNAT TIM note 3](https://www.sunat.gob.pe/indicestasas/tim.html) |

Compute the base sanction and then separately document any current graduality or non-sanction discretion and its correction/payment conditions. SIRE-specific relief does not waive monthly IGV payment or preserve an otherwise invalid input credit. A missing document or false invoice can cause credit denial independently of a monetary fine.

## Cross-border points

### Goods and service exports

An incoming foreign wire is not export proof. Goods need a domiciled seller, nonresident buyer and definitive customs export. Where title transfers in Peru before shipment, the normal shipment condition is sixty calendar days from invoice; the specified warehouse-document case uses 240 calendar days from that document. If the deadline fails, apply the resulting domestic classification. Services must be supplied for consideration from Peru abroad, documented in the sales register, by a domiciled exporter to a nonresident beneficiary, used/exploited abroad; the exporter must register in SUNAT's service-exporter register beforehand. Art. 33(12) separately covers qualifying partly foreign-performed services. [LIGV art. 33](https://www.sunat.gob.pe/legislacion/igv/ley/capitul9.pdf).

Issue the applicable export factura and retain contract, residency, service-use and performance evidence. Do not call it document "tipo 09" by default. Qualifying input tax can create saldo a favor del exportador; arts. 34-35 govern application against output, prescribed income/other tax offsets and ultimately refund. Drawback is a different customs mechanism and is not a synonym for an IGV refund. Detailed refund limits, PDB/export schedules and early-recovery applications require a separate specialist calculation. [LIGV arts. 34-36](https://www.sunat.gob.pe/legislacion/igv/ley/capitul9.pdf); [Comprobantes Regulation art. 4(1.1)(d)](https://www.sunat.gob.pe/legislacion/comprob/regla/capituloI.pdf).

### Foreign business services and consumer digital supplies

A business using a nonresident's taxable service in Peru generally determines the combined ordinary tax itself. Establish where the service is consumed/used, the tax point under art. 4(d), any exemption and contractual consideration. Input credit is available only after payment/qualifying compensation and required registration, subject to substantive credit rules. Foreign income-tax withholding is a separate question: do not automatically withhold a flat income-tax percentage merely because imported IGV applies. Route it to `peru-cross-border-tax` and the income-tax guide. [LIGV arts. 3-4](https://www.sunat.gob.pe/legislacion/igv/ley/capitul1.pdf), [9](https://www.sunat.gob.pe/legislacion/igv/ley/capitul3.pdf), [21](https://www.sunat.gob.pe/legislacion/igv/ley/capitul6.pdf), [32](https://www.sunat.gob.pe/legislacion/igv/ley/capitul8.pdf).

**For payments/compensations from 1 July 2026, including earlier tax periods**, RS 047-2026 applies, subject to its transitional rule for prior payments. Imported-service IGV has no separate determining declaration, but the information module must precede payment:

1. In SOL → Trámites y Consultas → Módulo de información de comprobantes de pago no domiciliados, enter the invoice issue period, series/number and total IGV payable. If no invoice exists yet, enter the remuneration-payment period and corresponding tax; the system assigns identifying fields. Submit using the module or its allowed flat file.
2. Download the information-declaration constancia immediately: it is available once. Link the service/invoice/operation to the subsequent tax payment.
3. In SUNAT Virtual's payment option, pay through **Formulario Virtual 1662, code 1041**. The new rule restricts this payment to SUNAT Virtual, rather than a bank NPS. Save its receipt; include proper interest for late tax.
4. Record the foreign document and tax-payment document correctly and take eligible credit in the permitted period. Do not put the 1041 payment into FV621's domestic prior-payment box 185. For exporter compensation with SFMB, art. 4.3 instead requires the specified paper communication at a SUNAT service center; retain it and the corresponding credit support.

[RS 000047-2026 arts. 4-7 and sole final/transitional provisions](https://www.sunat.gob.pe/legislacion/superin/2026/000047-2026.pdf); [SUNAT current module FAQ](https://cpe.sunat.gob.pe/informacion_general/preguntas_frecuentes).

Nonresident consumer digital supplies are different: LIGV art. 49-A makes the nonresident a collecting agent when the user/importer is a natural person **not conducting business**, with the prescribed Peru-consumption/residence indicators. That is not the default for a Peruvian business's foreign SaaS invoice. Platform commissions and the underlying transport/accommodation sale must be classified separately. [LIGV art. 49-A](https://www.sunat.gob.pe/legislacion/igv/ley/capitul12.pdf), [art. 3 digital definitions and consumption indicators](https://www.sunat.gob.pe/legislacion/igv/ley/capitul1.pdf). Detailed nonresident registration, fallback collection and returns are specialist work.

## Two worked examples that recompute

All amounts below are hypothetical PEN working-paper inputs. Rate authority: [2026 SUNAT table](https://emprender.sunat.gob.pe/principales-impuestos/impuesto-general-las-ventas-igv/impuesto-general-las-ventas); credit authority: [LIGV arts. 18-25](https://www.sunat.gob.pe/legislacion/igv/ley/capitul6.pdf). Calculations show the combined IGV/IPM amount.

### Example 1: consulting SPOT, electricity input and a separate carried retention

A Lima consulting company has a confirmed domestic business-advisory factura for S/ 500,000 net, S/ 90,000 tax and S/ 590,000 total, subject to Annex 3 item 5 with no exclusion. The customer deposits S/ 70,800 at 12% into the supplier's detracción account and pays S/ 519,200 to the supplier. No 3% retention applies to that operation. The company has qualifying electricity input of S/ 40,000 net plus S/ 7,200 tax and other qualifying inputs of S/ 160,000 plus S/ 28,800 tax. All credit and applicable payment conditions are met; no exempt/private use or preceding **purchase-credit** applies. Output S/ 90,000 less purchase credit S/ 36,000 gives S/ 54,000 before advance credits. [Annex 3 item 5](https://orientacion.sunat.gob.pe/apendices-del-sistema-de-detracciones); [RS 037 art. 5(f)](https://www.sunat.gob.pe/legislacion/superin/2002/037.htm).

Separately, the records establish a previously declared, unused retention balance of S/ 17,700 from a different eligible non-SPOT operation. The underlying historical payment was S/ 590,000: 3% was S/ 17,700 and net cash S/ 572,300. Those amounts do not describe the current consulting collection. With that documented carried retention available, current payable IGV is S/ 36,300; without it, S/ 54,000. FV621 uses 176 for the unused prior retention, not 168 for a current retention on the consulting invoice. Ordinary sales fields remain 100/101, not 100/105. [RS 037 arts. 3, 5-7, 11](https://www.sunat.gob.pe/legislacion/superin/2002/037.htm); [FV621 help, section III](https://orientacion.sunat.gob.pe/sites/default/files/inline-files/ayuda_621_igv_renta_mensual_ccv.pdf).

```oa-check
name: Consulting SPOT and separately documented carried retention, 2026
inputs:
  sales_net: 500000
  electricity_net: 40000
  other_inputs_net: 160000
  rate: 0.18
  retention_rate: 0.03
  spot_rate: 0.12
  historical_eligible_payment: 590000
  carried_retention: 17700
steps:
  output_tax: sales_net * rate
  invoice_total: sales_net + output_tax
  current_spot_deposit: invoice_total * spot_rate
  current_supplier_cash: invoice_total - current_spot_deposit
  historical_retention: historical_eligible_payment * retention_rate
  historical_supplier_cash: historical_eligible_payment - historical_retention
  electricity_credit: electricity_net * rate
  purchase_credit: electricity_credit + other_inputs_net * rate
  tax_before_retention: output_tax - purchase_credit
  payable: tax_before_retention - carried_retention
expected:
  output_tax: 90000
  invoice_total: 590000
  current_spot_deposit: 70800
  current_supplier_cash: 519200
  historical_retention: 17700
  historical_supplier_cash: 572300
  electricity_credit: 7200
  purchase_credit: 36000
  tax_before_retention: 54000
  payable: 36300
```

### Example 2: decide whether a common expense is fully creditable

For the relevant lookback, a mixed business has taxable sales of S/ 2,000,000, qualifying exports S/ 500,000 and relevant exempt sales S/ 200,000. Current output is S/ 360,000. Current qualifying taxed inputs of S/ 1,200,000 net comprise S/ 1,000,000 exclusively for taxable/export use and S/ 200,000 common use. The common-credit percentage is (2,000,000 + 500,000) / 2,700,000 = 92.59%, giving common credit S/ 33,332.40, plus direct credit S/ 180,000. After valid retention S/ 25,000, payable is S/ 121,667.60. Claiming every input at 100% would produce S/ 119,000 and understate tax by S/ 2,667.60. The choice is determined by supported use, not an election to minimize tax. [Regulation art. 6(6.1)-(6.2)](https://www.sunat.gob.pe/legislacion/igv/regla/cap5.pdf).

```oa-check
name: Direct allocation versus common-input prorrata, 2026
inputs:
  taxable_sales: 2000000
  exports: 500000
  exempt_sales: 200000
  direct_input_net: 1000000
  common_input_net: 200000
  valid_retention: 25000
  rate: 0.18
steps:
  ratio_percent: round((taxable_sales + exports) / (taxable_sales + exports + exempt_sales) * 100, 2)
  direct_credit: direct_input_net * rate
  common_credit: common_input_net * rate * ratio_percent / 100
  output_tax: taxable_sales * rate
  correct_payable: output_tax - direct_credit - common_credit - valid_retention
  full_claim_payable: output_tax - (direct_input_net + common_input_net) * rate - valid_retention
  understatement: correct_payable - full_claim_payable
expected:
  ratio_percent: 92.59
  direct_credit: 180000
  common_credit: 33332.40
  correct_payable: 121667.60
  full_claim_payable: 119000
  understatement: 2667.60
```

### Additional cases retained from earlier working papers

- **Software export:** S/ 1,850,000 consideration generates no output tax only if all art. 33 service-export conditions, prior exporter registration and foreign-use evidence are satisfied. If instead an ordinary taxable service is supplied for S/ 1,850,000 net, combined tax is S/ 333,000. No fixed foreign-exchange rate is assumed. [LIGV art. 33](https://www.sunat.gob.pe/legislacion/igv/ley/capitul9.pdf).
- **Construction detracción:** for an otherwise qualifying S/ 1,500,000 tax-inclusive contract, deposit S/ 60,000 at 4% and pay the supplier S/ 1,440,000. This allocates payment; it does not calculate or replace the invoice's IGV, and it does not establish the buyer's credit timing. [SUNAT Annex 3 item 9](https://orientacion.sunat.gob.pe/apendices-del-sistema-de-detracciones).
- **Nuevo RUS printing boleta:** S/ 3,500 paid gives S/ 0 IGV credit. Whether it is deductible for income tax is a different computation; do not label the whole amount automatically deductible. [Comprobantes Regulation art. 4(3)](https://www.sunat.gob.pe/legislacion/comprob/regla/capituloI.pdf).
- **Hospitality qualification:** on a hypothetical S/ 100,000 net eligible sale, tax is S/ 10,500 and gross S/ 110,500; an ordinary sale on the same net base has S/ 18,000 tax and S/ 118,000 gross. The S/ 7,500 difference is available only when the statutory conditions hold. [SUNAT 2026 eligibility table](https://orientacion.sunat.gob.pe/reduccion-del-igv-para-restaurantes-hoteles-y-alojamiento-turisticos-1).

## Ask the client first

1. Which month and RUC, business/person type, regime and recorded tax obligations apply; is the taxpayer a PRICO, qualifying good taxpayer or in an emergency-extension district?
2. What exactly was sold, delivered, consumed or paid, where and when; are there foreign customers/suppliers, export-use evidence, property/construction, exempt tariff items or hospitality income/group links?
3. Which issued/received CPEs, debit/credit notes, SUNAT/OSE validations, customs documents, contracts and delivery evidence support the registers; what is missing or contradicted?
4. Which purchases serve taxed/export activities, exempt activities or private use; what are the preceding lookback sales and direct/common allocation records?
5. What purchase-credit, exporter, retention and perception balances were declared previously; what certificates, bank payments, required payment means and detracción deposits support this month's claims?
6. Are there corrections, late payments, SUNAT notices, prior exemptions/waivers, IGV Justo elections or specialist-regime facts that change the ordinary result? For a proposed fine, obtain annual turnover declarations, same-type infringement/training history, relevant conviction-exclusion facts and the actual course notice/certificate before recommending payment.

## Sources

Read dates mean the operative portions named below were opened and read, not merely that a URL responded. Use the consolidated PDFs over the older HTML chapters where they differ; SUNAT's older FV621 hospitality-rate captions do not override the current 2026 rates.

| Source and portions read | Official URL | Read on |
|---|---|---|
| LIGV DS 055-99-EF, chapter I: read arts. 1-4, especially 2(a), (g), (j), (r), (s), 3(c) and tax points; compared current/previous passages | https://www.sunat.gob.pe/legislacion/igv/ley/capitul1.pdf | 2026-11-11 |
| LIGV chapter II: read arts. 5-7 and Ley 32542 extension through 2028 | https://www.sunat.gob.pe/legislacion/igv/ley/capitul2.pdf | 2026-11-11 |
| LIGV chapter III: read art. 9 taxpayer, import and habituality conditions | https://www.sunat.gob.pe/legislacion/igv/ley/capitul3.pdf | 2026-11-11 |
| LIGV chapter IV: read art. 11 monthly computation and import exception | https://www.sunat.gob.pe/legislacion/igv/ley/capitul4.htm | 2026-11-11 |
| LIGV chapter V: read arts. 12-17 base, ancillary charges, withdrawals and Ley 32387 rate/transitional note | https://www.sunat.gob.pe/legislacion/igv/ley/capitul5.pdf | 2026-11-11 |
| SUNAT general IGV: read 2026-2029 component table, current combined rate and credit carryforward | https://emprender.sunat.gob.pe/principales-impuestos/impuesto-general-las-ventas-igv/impuesto-general-las-ventas | 2026-11-11 |
| SUNAT hospitality: read 2026 rate, lookback, 1,700 UIT/70%, linkage, loss/re-entry and filing conditions | https://orientacion.sunat.gob.pe/reduccion-del-igv-para-restaurantes-hoteles-y-alojamiento-turisticos-1 | 2026-11-11 |
| SUNAT UIT: read 2026 row naming DS 301-2025-EF, and preceding-year row for IGV Justo distinction | https://www.sunat.gob.pe/indicestasas/uit.html | 2026-11-11 |
| LIGV chapter VI: read arts. 18-25 documentary/substantive credit, timing, reintegro, prorrata and carryforward | https://www.sunat.gob.pe/legislacion/igv/ley/capitul6.pdf | 2026-11-11 |
| IGV Regulation DS 029-94-EF, chapter V: read art. 6(2), (6), (7), (10)-(11) documents, prorrata, mistaken tax and foreign services | https://www.sunat.gob.pe/legislacion/igv/regla/cap5.pdf | 2026-11-11 |
| IGV Regulation chapter VI: read art. 7 timing of notes, adjustments and cancellations | https://www.sunat.gob.pe/legislacion/igv/regla/cap6.htm | 2026-11-11 |
| Ley 29215: read art. 2 issue/payment month plus twelve months in gazette p. 371118 | https://www.sunat.gob.pe/legislacion/nor_graf/2008/abril/nl20080423.pdf | 2026-11-11 |
| SUNAT Informe 052-2018: read conclusions and preceding explanation distinguishing late registration from credit exercise | https://www.sunat.gob.pe/legislacion/oficios/2018/informe-oficios/i052-2018-7T0000.pdf | 2026-11-11 |
| DL 1669: read art. 5, sole final commencement, transitional protection and SPOT amendment, gazette p. 18 | https://leyes.congreso.gob.pe/Documentos/2021_2026/Decretos/Legislativos/2024/DL-1669.pdf | 2026-11-11 |
| SUNAT Informe 016-2024: read prorrata conclusions for imported-service turnover versus input tax | https://www.sunat.gob.pe/legislacion/oficios/2024/informe-oficios/i000016-2024-7T0000.pdf | 2026-11-11 |
| LIGV chapter VIII: read arts. 29-32 monthly filing/payment, MYPE deferral, advance credits and foreign services | https://www.sunat.gob.pe/legislacion/igv/ley/capitul8.pdf | 2026-11-11 |
| LIGV chapter IX: read art. 33 goods/services conditions and arts. 34-36 exporter credit/offset/refund | https://www.sunat.gob.pe/legislacion/igv/ley/capitul9.pdf | 2026-11-11 |
| LIGV chapter XII: read art. 49-A consumer/nonbusiness condition and residence/collection mechanism | https://www.sunat.gob.pe/legislacion/igv/ley/capitul12.pdf | 2026-11-11 |
| Appendix I: read current heading, food/agricultural/fishing tariff descriptions and conditional exemption structure | https://www.sunat.gob.pe/legislacion/igv/ley/apendiceI.pdf | 2026-11-11 |
| Appendix II: read items 2-3, 8 and 14 passenger transport, freight, insurance and postal distinctions | https://www.sunat.gob.pe/legislacion/igv/ley/apendice2.pdf | 2026-11-11 |
| Comprobantes Regulation chapter I: read art. 4 factura/export, boleta-credit limitation and authorized-document cases | https://www.sunat.gob.pe/legislacion/comprob/regla/capituloI.pdf | 2026-11-11 |
| SUNAT RUC: read natural-person registration, eleven-digit identifier, start date, regime, SOL and confirmation steps | https://www.gob.pe/284-sacar-ruc-persona-natural | 2026-11-11 |
| SUNAT business RUC update: read Quiero abrir un negocio route, regime/IGV affectation and CIR download | https://centrovirtual.sunat.gob.pe/tramites/actualizar-datos-ruc | 2026-11-11 |
| SUNAT CPE FAQ: read transmission/acceptance, NRUS and imported-service module questions | https://cpe.sunat.gob.pe/informacion_general/preguntas_frecuentes | 2026-11-11 |
| RS 003-2023: read complete arts. 1-5 and final/transitional provisions; three-day factura/linked-note deadline across the three SEE systems, compared FAQ question 15 with superseded one-day passage | https://www.sunat.gob.pe/legislacion/superin/2023/000003-2023.pdf | 2026-11-11 |
| SUNAT FV621 overview: read covered regimes and SIRE proposal correction | https://orientacion.sunat.gob.pe/01-formulario-virtual-ndeg-621-igv-renta-mensual | 2026-11-11 |
| SUNAT FV621 help: read sections I-III field definitions, ratio, total-debt formula and old rate captions | https://orientacion.sunat.gob.pe/sites/default/files/inline-files/ayuda_621_igv_renta_mensual_ccv.pdf | 2026-11-11 |
| SUNAT declaration guidance: read basket, submission/payment and NPS steps | https://orientacion.sunat.gob.pe/declaracion-simplificada-personas | 2026-11-11 |
| SUNAT calendar: read all 2026 periods and RUC/status columns, especially October and December rows | https://www.sunat.gob.pe/orientacion/cronogramas/2026/cObligacionMensual2026.html | 2026-11-11 |
| SUNAT emergency extensions: read district/period extension conditions under RS 051-2019 | https://orientacion.sunat.gob.pe/Prorroga-de-vencimientos-de-declaraciones-y-pagos-mensuales-1 | 2026-11-11 |
| RS 000125-2026: read arts. 1, 3-4, July commencement and October PRICO SIRE start | https://www.sunat.gob.pe/legislacion/superin/2026/000125-2026.pdf | 2026-11-11 |
| SUNAT IGV Justo: read annual sales/preceding UIT, exclusions, regularization, election and deferral timing | https://emprender.sunat.gob.pe/principales-impuestos/impuesto-general-las-ventas-igv/igv-justo | 2026-11-11 |
| RS 037-2002: read arts. 3, 5-6 and exclusions; SUNAT FAQ: read 700 exception and current 3% payment calculation | https://www.sunat.gob.pe/legislacion/superin/2002/037.htm; https://orientacion.sunat.gob.pe/06-preguntas-frecuentes-regimen-de-retenciones | 2026-11-11 |
| SUNAT perceptions: read domestic/import/fuel rates, collection moment and exclusions; customs page: read first-import and sensitive-goods rules | https://emprender.sunat.gob.pe/principales-impuestos/impuesto-general-las-ventas-igv/regimen-percepciones-igv; https://www.sunat.gob.pe/orientacionaduanera/pagosgarantias/ | 2026-11-11 |
| RS 128-2002: read arts. 2-4 fuel scope, exclusions, agents and 1% | https://www.sunat.gob.pe/legislacion/superin/2002/128.htm | 2026-11-11 |
| RS 183-2004 and Annex 3: read arts. 12-16, items 5/9/10, current business-service rate and exclusions alongside construction definition/rate | https://www.sunat.gob.pe/legislacion/superin/2004/183.htm; https://orientacion.sunat.gob.pe/apendices-del-sistema-de-detracciones | 2026-11-11 |
| SUNAT SPOT: read construction/Annex 3 rate, buyer/supplier deposit timing and exceptions | https://emprender.sunat.gob.pe/principales-impuestos/impuesto-general-las-ventas-igv/sistema-detracciones-igv | 2026-11-11 |
| DL 940 TUO: read first final provision distinguishing deposit and input-credit timing | https://www.sunat.gob.pe/legislacion/detracciones/ | 2026-11-11 |
| Ley 28194 TUO: read arts. 3-5, 8 payment threshold, qualifying means and lost-credit effects | https://www.sunat.gob.pe/legislacion/itf/ds150_07.pdf | 2026-11-11 |
| Código Tributario DS 133-2013-EF: read arts. 33, 174-178, 181 and Tables I-II/note 21; consolidation through 26 June 2026 | https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf | 2026-11-11 |
| Tax Code arts. 165/180 as amended by Law 32335, preventive-training gate; DS 288-2025-EF regulation arts. 3-11 and transitions, actual MEF PDF read through web after direct download returned non-PDF HTML | https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf; https://www.mef.gob.pe/es/por-instrumento/decreto-supremo/34781-decreto-supremo-n-288-2025-ef/file | 2026-11-11 |
| RS 010-2026, complete four-page resolution, course notice, access period, completion/final activity and constancia | https://www.sunat.gob.pe/legislacion/superin/2026/000010-2026.pdf | 2026-11-11 |
| SUNAT TIM and RS 044-2021: read current PEN rate and note distinguishing legal interest on fines | https://www.sunat.gob.pe/indicestasas/tim.html; https://www.sunat.gob.pe/legislacion/superin/2021/044-2021.pdf | 2026-11-11 |
| RS 000047-2026: read arts. 4-8, July commencement and prior-payment transitional rule | https://www.sunat.gob.pe/legislacion/superin/2026/000047-2026.pdf | 2026-11-11 |

Not yet confirmed: transaction-specific eligibility, tariff classification, exporter/refund entitlement and exact penalty relief require the stated client documents. The old named-supplier tax registrations/ownership assertions and discretionary numerical risk flags have no primary-law support and are excluded. No universal medical/insurance/residential-rent exemption, automatic foreign SaaS income-tax percentage, boleta IGV allowance or international-flight zero rate is asserted.
