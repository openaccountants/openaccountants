---
name: spain-einvoice
description: Use this skill whenever asked about Spanish e-invoicing, factura electrónica Spain, FACe, Facturae, Veri*factu, VERI*FACTU, SII (Suministro Inmediato de Información), AEAT e-invoicing, B2B e-invoicing mandate Spain, RD 1007/2023, RD 238/2026, Ley Crea y Crece, QR tributario, anti-fraud invoicing software, SPFE (Solución Pública de Facturación Electrónica), or any question about issuing, receiving, validating, or archiving electronic invoices in Spain. Also trigger when configuring Veri*factu-compliant billing software, setting up SII real-time reporting, submitting B2G invoices via FACe, or advising on the transition from SII to Veri*factu. This skill covers FACe B2G, SII reporting, Veri*factu anti-fraud system, B2B mandate timeline, accepted formats (Facturae, UBL, CII), mandatory fields, validation rules, archiving, penalties, and interaction with Spanish VAT returns. ALWAYS read this skill before touching any Spanish e-invoicing work.
version: 2.1
jurisdiction: ES
tax_year: 2026
last_updated: 2026-11-27
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - einvoice-workflow-base
category: invoicing
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
type: filing-howto
domain: e-invoicing
---

# Spain: electronic invoicing, Veri*factu, FACe and the SII

## Scope

State-law e-invoicing for 2026, with the enacted later implementation stages read on 27 November 2026. Load this over `einvoice-workflow-base`. Classify each operation separately: an invoice exchange, an SII VAT-book entry and a software invoicing record are different obligations. The VAT return is `es-vat-return`; the books are `spain-bookkeeping`.

| Route | Who and operative date | Official source |
|---|---|---|
| B2G / FACe | The entity classes in Ley 25/2013 art. 4, from 15 January 2015, subject to an administration's permitted exclusions | https://www.boe.es/buscar/act.php?id=BOE-A-2013-13722#a4 |
| SII | Monthly VAT filers under RIVA art. 71.3; others may opt in. It supplies records, not the invoice document | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925#a62 |
| Invoicing software / RRSIF | In-scope software users under RD 1007/2023 art. 3.1: adaptation at the expiry of the second B2B-stage period, **6 October 2028**, derived from the amended final provision and the order below. This supersedes the previous 1 January / 1 July 2027 split | https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840#df-4 ; https://www.boe.es/buscar/act.php?id=BOE-A-2026-24701 ; https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295#df-4 |
| B2B / SPFE and private platforms | Previous-calendar-year volumen de operaciones above EUR 8 million: 6 October 2027; remaining businesses: 6 October 2028. These are derived from twelve / twenty-four months after the order entered into force on 6 October 2026 | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295#df-4 ; https://www.boe.es/buscar/act.php?id=BOE-A-2026-20587#df |

The software amendment is RD-ley 43/2026 final provision 1, published 25 November and effective 26 November 2026. It changes the user deadline, not the SII exclusion or the distinction between VERI*FACTU and non-VERI*FACTU. An SII participant is outside RD 1007/2023 under art. 3.3; it can still have B2G and B2B duties.

## Ask the client first

- VAT period, SII registration or voluntary election, and any departure from SII.
- Entity type, software use (including partial use), exempt status and any authorisation excluding operations.
- Public customer, correct entry point and its DIR3 routing codes.
- Previous-calendar-year volumen de operaciones under LIVA art. 121; recipient's establishment and the establishment receiving the supply.
- Full or simplified invoice, including whether the customer requires the art. 7.2 particulars.
- Mainland/Balearic, foral, Canary Islands, Ceuta or Melilla position; tax point and any special VAT/withholding regime.

## The method, step by step

### 1. Public-sector invoices: coverage, format and delivery

Ley 25/2013 art. 4 makes electronic invoicing compulsory for sociedades anónimas, sociedades de responsabilidad limitada, foreign legal persons and entities without legal personality, permanent establishments and branches of non-resident entities, temporary joint ventures, and the economic-interest groupings and funds listed in art. 4.1.f. Other suppliers may invoice electronically. This is not a rule that every individual supplier must do so. An administration may exclude by regulation invoices up to EUR 5,000; the overseas-services exclusion is conditional on the technical circumstances stated in art. 4.1, not a universal supplier exemption. Present the invoice within thirty days of effective delivery/service under art. 3. [Ley 25/2013 arts. 3-4](https://www.boe.es/buscar/act.php?id=BOE-A-2013-13722#a3).

Use the public body's appropriate punto general de entrada. FACe is the State entry point and also serves administrations that adhere to it. Submission may be through the web portal or an integrated web service. Get the Oficina Contable, Órgano Gestor and Unidad Tramitadora DIR3 codes from the contracting body; the optional Órgano Proponente is a separate role. Retain the electronic receipt with date/time and the accounting-registration identifier, and check processing status. [Ley 25/2013 arts. 6, 9](https://www.boe.es/buscar/act.php?id=BOE-A-2013-13722#a6); [HAP/1074/2014 arts. 3-7 and annex I](https://www.boe.es/buscar/act.php?id=BOE-A-2014-6662#ani).

Use the Facturae structured format and an advanced electronic signature based on a recognised certificate, or the qualifying advanced electronic seal. Do not restrict valid certificates to a Spanish issuer. The official format page publishes the 3.2, 3.2.1 and 3.2.2 schemas; the checklist here uses 3.2.2. [Ley 25/2013 art. 5 and additional provision 2](https://www.boe.es/buscar/act.php?id=BOE-A-2013-13722#a5); [Facturae schema page](https://www.facturae.gob.es/formato/ultima-version).

Facturae XML paths below are relative to the root. A tax-identification group does not itself contain the party's name: use the separate LegalEntity / Individual branch. Schema optionality is not permission to omit a legally required tax particular.

| Original field/checklist item | Correct use in Facturae 3.2.2 |
|---|---|
| FileHeader/SchemaVersion; Modality | Required; include the other required header fields, including InvoiceIssuerType and Batch |
| Parties/SellerParty and BuyerParty | TaxIdentification plus the applicable LegalEntity or Individual identity/address branch |
| BuyerParty/AdministrativeCentres | Optional in the generic schema, but the three DIR3 roles above are compulsory for public-sector routing |
| Invoices/Invoice/InvoiceHeader | InvoiceNumber, InvoiceDocumentType and InvoiceClass; InvoiceSeriesCode when applicable |
| InvoiceIssueData | IssueDate, InvoiceCurrencyCode, TaxCurrencyCode and LanguageName; OperationDate when different |
| TaxesOutputs/Tax | TaxTypeCode, TaxRate, TaxableBase/TotalAmount; TaxAmount is schema-optional, subject to the tax-law obligation to show tax separately |
| InvoiceTotals | TotalGrossAmount, TotalGrossAmountBeforeTaxes, TotalTaxOutputs, TotalTaxesWithheld, InvoiceTotal, TotalOutstandingAmount and TotalExecutableAmount |
| Items | Required invoice-detail group; split applicable tax treatments |
| PaymentDetails | Schema-optional, not universally mandatory |

Source for every field and occurrence condition: [official Facturae 3.2.2 XSD](https://www.facturae.gob.es/content/dam/facturae/formato/versiones/Facturaev3_2_2.xml). Validate the whole file against that XSD, then the applicable signature and routing rules. The entry point rejects incorrect format/signature under HAP/1074/2014 art. 3.5. A schema-valid file alone is not proof that its tax treatment is correct.

**Implementation hold:** this Guide does not establish a universal XAdES-EPES profile, a FACe duplicate key, SOAP binding or Peppol availability. Obtain the current integration/signature policy before configuring those features. Check this point with one of our partner accountants. [Official signature policies](https://www.facturae.gob.es/formato/politicas-firma-electronica).

### 2. SII: population and deadlines

SII keeps the VAT books through the AEAT Sede by supplying invoicing records via web service or form: issued invoices, received invoices, capital goods and specified intra-EU operations. Compulsory monthly filers include those above **EUR 6,010,121.04** previous-calendar-year volumen de operaciones; qualifying business acquirers whose combined turnover exceeds that amount; REDEME taxpayers; VAT groups; and the specified petrol, diesel and biofuel fiscal-deposit holders/extractors. It is not simply a rounded EUR 6 million test. Others may elect SII through the census declaration under art. 68 bis, effective from the first following filing period and for at least the calendar year elected; withdrawal is made in November before the year it takes effect. [RIVA arts. 62.6, 68 bis, 71.3](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925#a62).

For both the SII threshold and the B2B stage, use LIVA art. 121: supplies and services in the previous calendar year, including exempt supplies, excluding VAT, recargo and flat-rate compensation; add the transferred activity's relevant previous-year turnover on a business acquisition. Disregard occasional property sales, the supplier's capital goods and the specified non-habitual financial/investment-gold operations. This is not accounting revenue or cash collected. [LIVA art. 121](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a121).

| Record | Supply window under RIVA art. 69 bis |
|---|---|
| Issued invoice | Four calendar days from issue; eight if issued by the recipient or a third party. Both are capped before the 16th of the month after the VAT tax point; for non-taxable operations use the operation date for that cap |
| Received invoice / import document | Four calendar days from accounting registration; before the 16th of the month following the filing period in which included. For imports, register the customs tax document |
| Rectifying invoice | Four calendar days from issue/registration; where it increases previously deducted input VAT, use the received-invoice rule |
| Register correction | Before the 16th of the month after the period in which the error becomes known |
| Capital-goods book | Supply within the last filing period's submission window for the year; on census deregistration use the last required VAT-return window, except the ex officio deregistration case specified in art. 65.6 |

Exclude Saturdays, Sundays and national holidays from the first three rows' four/eight-day counts. The historic eight-day 2017 transition is not the current reason for eight days. Special intra-EU movement/call-off-stock and cash-accounting payment records have their own triggers under art. 69 bis. Do not reuse an invoice-date clock for them. Check this point with one of our partner accountants. [RIVA arts. 69 bis and 65](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925#a69bis).

SII technical NIF/type-code validation and message-level errors require the current SII specification. Do not assume that a positive transport response proves a correct VAT return. Check this point with one of our partner accountants.

### 3. Invoicing software: scope, records and QR

RD 1007/2023 art. 3 covers corporate-tax taxpayers, individuals carrying on economic activities, non-resident taxpayers operating through a permanent establishment and income-attribution entities with economic activities, when they use invoicing software even for only part of their activity. It does not require software from a wholly manual invoicer. Fully exempt corporate-tax entities under LIS art. 9.1 are excluded; partly exempt entities are covered only for operations generating taxable, non-exempt income. SII bookkeepers are excluded under art. 3.3. [RD 1007/2023 arts. 1, 3](https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840#a3).

Art. 4 also excludes the specified electricity-billing operations, invoices through foreign permanent establishments, and qualifying recipient/compulsory-third-party billing where that party keeps SII books. Art. 5 allows a reasoned non-application ruling on request, possibly temporary or conditional. Do not assume an entire sector is excluded without that ruling or the statutory exception. Check this point with one of our partner accountants. [Arts. 4-5](https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840#a4).

The **user adaptation date is 6 October 2028**, derived from the amended final provision 4 referring to RD 238/2026 final provision 4.1.b and the order's 6 October 2026 entry into force. The old January/July 2027 dates must not be used as current deadlines. Producers/commercialisers retain their separate nine-month requirement from the technical order's entry into force: HAC/1177/2024 entered into force on **29 October 2024**, so that ordinary period ended **29 July 2025** (derived). The current provision also says systems covered by pre-existing multi-year maintenance contracts must be adapted by the date in the preceding producer paragraph; do not preserve the old claim that those contracts extend to the former 2027 user dates. [Current final provision 4](https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840#df-4); [HAC/1177/2024 final provision](https://www.boe.es/buscar/act.php?id=BOE-A-2024-22138#df).

The producer, not the accountant or AEAT, certifies compliance through its written **declaración responsable**, visible in each software version and available to the customer and reseller on purchase. Obtain it for the version installed. [Art. 13](https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840#a1-5).

| Mode | Required behaviour |
|---|---|
| VERI*FACTU | Effectively sends all generated records automatically, consecutively and reliably to AEAT. It is presumed to meet the art. 8 requirements by design and need not electronically sign each record; it still calculates the hash. Starting systematic submission elects this mode at least through the end of the calendar year of the first effective transmission |
| Non-VERI*FACTU | Keeps accessible, legible, preserved and inalterable records with the required chain, signatures and event log; has export and transmission capability for an AEAT request |
| AEAT application | The application under art. 7.b is VERI*FACTU for these purposes |

[RD 1007/2023 arts. 7-8, 12, 14-16](https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840#a1-8); [HAC/1177/2024 art. 3](https://www.boe.es/buscar/act.php?id=BOE-A-2024-22138#a3). The two modes are lawful alternatives; continuous transmission is not compulsory for every software user.

Generate an alta record simultaneously with or immediately before each invoice. Art. 10 requires issuer and conditional recipient identity, who issues it, number/series, dates, invoice/rectification/replacement type and references, description, total, tax regime and reverse-charge status, taxable/exempt/non-taxable amounts and causes, VAT and recargo breakdown, preceding-record identifiers/hash, system/producer/installation identification, generation timestamp and additional generation circumstances. Monetary amounts in the record are in euros, converting a foreign-currency invoice. Anulación records have their own art. 11 fields. These are **records**, not a replacement for the invoice. [Arts. 9-11](https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840#a1-2).

Corrections require a later additional record preserving the original. **Do not regenerate or silently rewrite an existing chain** to repair an error. [Art. 8.2](https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840#a8). Build the hash from the prescribed data, including the previous hash; use the algorithm/encoding in the current AEAT technical document rather than treating a bare “SHA-256” label as a complete specification. [HAC/1177/2024 art. 13](https://www.boe.es/buscar/act.php?id=BOE-A-2024-22138#a1-5).

Full and simplified invoices issued using an in-scope system carry the QR information. For electronic invoices, the graphic may be replaced by the content it represents. Add “Factura verificable en la sede electrónica de la AEAT” or “VERI*FACTU” only when all records are actually remitted. SII exclusion means this RRSIF QR duty does not apply; it does not establish a blanket ban on every other QR a business might print. The QR identifies the issuer NIF, series/number, date and total through the prescribed AEAT URL; implement its exact presentation and encoding from HAC/1177/2024 and AEAT specifications. [RD 1619/2012 arts. 6.5, 7.5](https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696#a6); [HAC/1177/2024 art. 21](https://www.boe.es/buscar/act.php?id=BOE-A-2024-22138#a2-3).

VERI*FACTU submissions use the prescribed XML messages over secure communication with certificate authentication. Process the individual validation response; an affirmative response does not prevent later checks. If a technical incident prevents sending, preserve generation order, send as soon as possible, identify the incident and retry at least hourly while displaying the outstanding-record warning. The old unsupported REST instruction is not an integration contract. [HAC/1177/2024 arts. 4-5, 16](https://www.boe.es/buscar/act.php?id=BOE-A-2024-22138#a1-8). For exact endpoint bindings, invoice-type codes F1/F2/R1-R5, hash encoding and QR implementation, use the current technical package; do not deploy from this summary alone. Check this point with one of our partner accountants.

### 4. B2B mandate: stages and operative conditions

RD 238/2026 art. 3 applies where the supplier is obliged to issue/deliver an invoice and its business/professional customer has its business seat, permanent establishment or, in default, domicile/habitual residence in Spain, **and the operation is destined to that location**. A foreign head office with a Spanish receiving establishment is not automatically outside scope. Recipient/third-party issuance does not transfer the supplier's legal responsibility. Plain simplified invoices are excluded; art. 7.2 qualified simplified invoices remain included. The regulated electricity/gas market operations and qualifying IATA CASS, BSP and SIS-ICH settlements have the additional-provision-2 exclusions. [Arts. 3-4 and additional provision 2](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295#a3).

| Stage | Application, calculated from 6 October 2026 | Official source |
|---|---|---|
| Above EUR 8 million previous-year art. 121 turnover | Invoice exchange and states/payment duties from 6 October 2027 | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295#df-4 |
| Remaining businesses/professionals | Invoice exchange from 6 October 2028; legal persons also begin states/payment reporting then | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295#df-4 |
| Individuals and income-attribution entities at or below EUR 8 million | States/payment duties under arts. 10 and 12 from 6 October 2029; voluntary until then | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295#dt-3 |
| Private-platform operator duties specified in final provision 4.2 | Twelve months from the order, hence 6 October 2027 | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295#df-4 |

These are enacted deferred dates, not duties already compulsory in November 2026. The order HAC/1028/2026 was published on 5 October and entered into force on 6 October 2026, starting the periods. The public solution must be available at least two months before first application; this is a legal availability requirement, not a claim that every production feature is already available. [Order final provision](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20587#df); [RD additional provision 5](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295#da-5); [AEAT implementation note](https://sede.agenciatributaria.gob.es/Sede/informacion-institucional/puede-interesar/analisis/2026/octubre/29/facturacion-electronica-solucion-publica-facturacion-atras.html).

**EU prerequisite:** Ley 18/2022 final provision 8 retains its reference to an exception from Directive arts. 218 and 232. Read it with Directive (EU) 2025/516 art. 1(2)-(3), effective 14 April 2025, which now permits domestic electronic-invoice requirements for taxable persons established in the Member State and dispensing with domestic recipient acceptance. Do not describe that domestic permission as still awaiting an individual EU exception. The Spanish decree and order supply the timetable above. This does not establish an EU permission covering every non-established-supplier fact pattern; for that boundary, do not extend the domestic conclusion automatically. Check this point with one of our partner accountants. [Ley 18/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-15818#df-8); [official Spanish text of Directive 2025/516, arts. 1 and 7](https://www.boe.es/buscar/doc.php?id=DOUE-L-2025-80487).

Use a private platform, SPFE or both. Without an express private-platform agreement, SPFE is the default; a private receiving entry point must be published in business communications and on the website if there is one. If none is published, SPFE is the entry point. Private platforms publish an open customer-entry-point lookup. Where neither issuance nor interconnection uses SPFE, send a faithful, clearly marked UBL copy simultaneously with issue. **No extra copy** is sent when SPFE already issues or interconnects the invoice. [RD arts. 5-6, 11.9](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295#a6); [HAC/1028/2026 arts. 3-4](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20587#a4).

| Format / content | Requirement |
|---|---|
| Accepted structured syntaxes | EN16931 semantic model using CII, UBL, EDIFACT invoice or Facturae; SPFE uses UBL |
| Private-platform signature | Advanced electronic signature by the issuer or authorised delegate; transform into the agreed syntax before signing where necessary. In default of agreement use SPFE syntax/specifications |
| Unique invoice code | Issuer NIF, invoice series/number and issue date, in one field or concatenated fields |
| Invoice particulars | RD 1619/2012 art. 6 or 7.2, plus the relevant order annex. Both issuer and recipient NIF must be correctly informed for SPFE admission |
| Extra contractual fields | May be agreed; information required from the recipient must have been reliably sent to the issuer before the operation date |

[RD arts. 7 and 11](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295#a7); [HAC/1028/2026 art. 3 and annex I](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20587#a3). “Spanish CIUS” is not a substitute for those operative specifications. Do not impose an unverified universal F1/F2 mapping or a particular UBL version from this Guide.

Private platforms must transform between accepted formats preserving authenticity/integrity, interconnect on customer request and meet art. 13's security, signature, continuity, support and governance requirements. Interconnection/interoperability is free. The recipient cannot force a predetermined provider. A recipient may request a copy for four years after issue without extra cost. [RD arts. 7-9, 13](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295#a1-5); [Ley 56/2007 art. 2 bis.2-3 bis](https://www.boe.es/buscar/act.php?id=BOE-A-2007-22440#a2bis).

Under art. 10, recipients tell the issuer commercial acceptance/rejection and its date, and full effective payment and its date, within four calendar days of the state, excluding Saturdays, Sundays and national holidays. Partial acceptance/rejection, partial payment and assignment are optional states. Under art. 12, report full payment or rejection to SPFE regardless of exchange channel; full payment and effective date are due within the same four-day count, also informing the due date. Without rejection or later rectification, acceptance is presumed. A private platform may report when authorised and supplied the necessary data. SPFE communications are governed by art. 12 rather than duplicating art. 10. [RD arts. 10-12](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295#a1-2).

Authorised debit/credit-document arrangements use the corrected original invoice for reporting, rather than duplicating the rectifying invoice's states. Other rectification authorisations can change the state-reporting obligation. For those authorisations and unusual rejection/correction messages, use the actual authorisation and HAC/1028/2026 specifications. Check this point with one of our partner accountants. Payment-period calculation follows Ley 3/2004 art. 4, subject to special laws; where the invoice omits the operation date, RD art. 15 uses the issue date as the start. Check this point with one of our partner accountants. [RD arts. 10.5-7, 12.5 and 15](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295#a1-7).

During the first twelve months of the larger-business stage, accompany its electronic invoice with a readable PDF unless the recipient voluntarily and expressly accepts the original format; do not send that PDF to SPFE. The AEAT solution is free and provides the form/application route; automated exchange/copy submission uses its prescribed web services and validation responses. Keep the acknowledgement and correct identified errors without losing traceability. [RD transitional provision 2, arts. 11.10 and additional provision 1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295#dt-2); [HAC/1028/2026 arts. 3-5](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20587#a5).

### 5. Invoice particulars, VAT and withholding

For a full invoice, RD 1619/2012 art. 6 requires consecutive number/series, issue date, full issuer/recipient names and addresses, issuer NIF and the recipient NIF where required, description, unit prices/discounts needed for the taxable base, applicable rates, separately stated tax, and a different operation/advance-payment date. Recipient NIF is compulsory for exempt intra-EU supplies, recipient-liability operations and domestic operations by a supplier established in the VAT territory. Use the relevant establishment address. Specific series are mandatory for recipient/third-party billing, rectifications and the other art. 6.1.a cases. [Art. 6](https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696#a6).

State the exemption provision or that the operation is exempt; use “facturación por el destinatario”, “inversión del sujeto pasivo”, or the prescribed travel-agent, second-hand-goods/art/antiques/collectors' items or cash-accounting wording when relevant. New means of transport need their characteristics, first-use date and distance/hours. Split the taxable base for different rates, exempt/non-exempt mixtures and recipient-liability/ordinary mixtures. **Reverse charge is not a zero-rated supply** merely because the supplier charges no VAT. [Art. 6.1.j-p and 6.2](https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696#a6).

A simplified invoice is available up to **EUR 400 VAT included**, or for a rectifying invoice; the **EUR 3,000 VAT-inclusive** limit applies only to art. 4.2's listed operations: retail to final consumers, itinerant/home sales and services, passenger transport, hospitality/restaurants, dance halls, public telephone/anonymous cards, hairdressing/beauty, sports facilities, photographic services, parking, film hire, laundry/dry cleaning and toll motorways. Apply the prohibitions in art. 4.4: exempt intra-EU supplies, the specified distance sales outside the relevant special scheme, the specified non-established-supplier recipient-issued domestic invoices, and the other art. 2.3.b.b' operations. [Art. 4](https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696#a4).

Simplified content includes number/series, dates, supplier NIF/name, goods/services identification, rate (optionally “IVA incluido”), total and required correction/special-scheme wording. Different rates need separate bases. Where a business recipient requires it for deduction, add recipient NIF/address and separately stated tax under art. 7.2; art. 7.3 extends those extra particulars to other recipients asserting a tax right. The QR rules above still apply to in-scope software invoices. [Art. 7](https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696#a7).

Issue at the operation, or for a business customer before the 16th of the month after the VAT tax point. The intra-EU art. 75.Uno.8 supply rule instead refers to the month dispatch begins; cash-accounting invoices use the operation-date rule in art. 11.3. Remission to a business customer is before the 16th of the month following the tax point (cash scheme: following the operation; rectifying invoices: following their issue); other invoices are remitted when issued. [Arts. 11 and 18](https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696#a11). Public-sector registration has the separate thirty-day requirement in step 1.

| VAT rate in the original 2026 rate card | Application and conditions | Official source |
|---|---|---|
| 21% | General rate; use the rate at the VAT tax point, not automatically the invoice date | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a90 |
| 10% | Only operations satisfying art. 91.Uno: qualifying food (excluding alcohol and the specified sweetened drinks), water, listed medical equipment, passenger transport, hospitality/restaurants, qualifying housing and renovation | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a91 |
| 4% | Art. 91.Dos conditions apply: common bread/bread dough/flour, listed milk, cheese, eggs, natural produce/cereals, olive oil; qualifying books/newspapers/magazines, human medicines, disability equipment and protected housing | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a91 |

Do not reuse the historic “essential foods at 0% extended through 2025” claim for 2026. A zero rate can still exist for a different legal reason: art. 91.Cuatro applies to qualifying goods donations to Ley 49/2002 nonprofit entities for their general-interest purposes. Exemption and reverse charge have their own legal treatments. The table is not an exhaustive product-classification service. For medical/disability eligibility, housing and renovation facts, and the **1 December 2026** changes to furnished accommodation, renovation payment conditions and protected housing, do not infer a rate from the label alone. Check this point with one of our partner accountants. [LIVA art. 91](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a91); [RD-ley 29/2026 art. 7, explicit December effects](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20823#a7).

Professional fees paid by a withholding-obliged payer generally carry **15%** withholding on gross professional income. A private consumer is not automatically a withholding agent. For a new professional, **7%** applies in the starting tax period and the following two only if there was no professional activity in the year before starting; communicate the condition to the payer, who keeps the signed notice. These are not three rolling years. Special professional/artistic categories and the Ceuta/Melilla reduction need separate eligibility analysis. Check this point with one of our partner accountants. Withholding is distinct from VAT and must not be treated as reducing the VAT base. [RIRPF arts. 75-76 and 95.1](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a95).

For an ordinary invoice without extra charges/payments, the working reconciliation is taxable bases + VAT/recargo − withholding = amount due. Facturae also distinguishes discounts, charges, payments on account and amounts executable/outstanding; use the actual fields. Do not force every tax line to two-decimal intermediate rounding: the official schema specifies precision by field and permits up to eight decimals for several amounts. A rounding or tolerance implementation must follow the applicable format, not a universal convention from this Guide. Check this point with one of our partner accountants. [Official XSD, InvoiceTotalsType and TaxOutputType](https://www.facturae.gob.es/content/dam/facturae/formato/versiones/Facturaev3_2_2.xml).

For recargo de equivalencia, suppliers apply the appropriate surcharge to an in-scheme retailer, separately from VAT; the statutory ordinary rates are below. Retailers cannot deduct input VAT attributable to that scheme or add recargo to their own customers' VAT. The no-periodic-liquidation rule does not remove liabilities on relevant intra-EU acquisitions, reverse-charge transactions or taxable non-exempt property sales. Nor is invoice exemption absolute: RD 1619/2012 art. 3.1.b is subject to art. 2.2, including a business recipient acting as such. [LIVA art. 154](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a154); [RD art. 3](https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696#a3-2).

| Underlying VAT treatment | Ordinary recargo | Official source |
|---|---|---|
| General-rate goods | 5.2% | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a161 |
| Art. 91.Uno goods | 1.4% | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a161 |
| Art. 91.Dos goods | 0.50% | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a161 |

Tobacco has its separate art. 161.4 rate; do not apply the general row merely because VAT is at the general rate. Check this point with one of our partner accountants. Display VAT and recargo separately under LIVA art. 159.

### 6. Archive and preserve access

Keep received invoices, issued copies/matrices, the relevant accounting vouchers, agricultural receipts and import tax documents under RD 1619/2012 art. 19. Tax limitation is ordinarily four years under LGT art. 66, but **not a destruction date four years after issue**: interruption and obligations affected by earlier transactions can extend retention (arts. 68 and 70). Commercial books/supporting documents are kept six years from the last book entry under Código de Comercio art. 30. Capital-goods deduction adjustments run over the four following calendar years, or nine for land/buildings; delayed first use can shift the period. Preserve invoices through adjustment and the applicable tax limitation; “all fixed assets: nine years” is wrong. [RD art. 19](https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696#a19); [LGT arts. 66-70](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a70); [Código art. 30](https://www.boe.es/buscar/act.php?id=BOE-A-1885-6627#art30); [LIVA art. 107](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a107).

Keep original content ordered, authentic, intact and legible. Electronic archives preserve original-format readability and associated signature-verification data, with online access, selective search, copying/downloading and printing for AEAT without unjustified delay. Outsourcing leaves the taxpayer responsible; foreign storage/third-country outsourcing has communication/access conditions under arts. 19.4 and 22. Do not assume an SPFE repository discharges these duties. Invoicing-system audit access is governed by RD 1007/2023 art. 14, with its legal safeguards and the art. 16.2 exception for VERI*FACTU. [RD 1619/2012 arts. 19-23](https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696#a21); [RD 1007/2023 arts. 14, 16](https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840#a1-6).

### 7. Penalties: classify the conduct first

These are statutory starting penalties, not an automatic assessed liability. Establish responsibility and the applicable procedural reductions/gradation before advising on a payable sanction. Do not multiply them indiscriminately for the same conduct.

| Conduct | Statutory sanction and conditions | Official source |
|---|---|---|
| Invoicing requirements breached, LGT art. 201.2.a | One per cent of the operations giving rise to the breach, unless the more specific non-issue/non-retention or false-data provisions apply | https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a201 |
| Failure to issue/keep invoices, art. 201.2.b | Two per cent of those operations; if their amount cannot be known, EUR 300 for each operation without the invoice/document | https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a201 |
| False/falsified invoice data, art. 201.3 | 75% of the affected operations; the art. 201.5 increase is 100% where non-compliance is substantial | https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a201 |
| Late SII issued/received-invoice books | 0.5% of the relevant record's total, including applicable VAT, recargo and compensation, with quarterly minimum EUR 300 and maximum EUR 6,000 across the quarter's infringements | https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a200 ; https://www.boe.es/buscar/act.php?id=BOE-A-2004-18398#a16 |
| Late SII capital-goods / specified intra-EU books | EUR 150 per record; this is not the invoice-book percentage rule | https://www.boe.es/buscar/act.php?id=BOE-A-2004-18398#a16 |
| Other accounting/register breaches | Art. 200.3's default EUR 150 is displaced by its specific rules: omitted/inaccurate entries, failure to keep books, double books, prolonged delay and undiligenced books must be classified separately | https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a200 |
| Making/selling software with art. 201 bis.1.a-e defects | EUR 150,000 per financial year with sales and per distinct system/program type | https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a2-2 |
| Certification failure, art. 201 bis.1.f | EUR 1,000 per system/program sold without the required certificate | https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a2-2 |
| Possession under art. 201 bis.2 | EUR 50,000 per financial year where required certification is absent or certified devices have been altered; a person already sanctioned under paragraph 1 is not sanctioned again under paragraph 2 | https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a2-2 |
| Consumer electronic-invoice/access duties, Ley 56/2007 art. 2 bis.9 | Warning or fine up to EUR 10,000 for its specified consumer-facing failures. This is not a universal B2B fine per incident, and there is no six-month grace period in that provision | https://www.boe.es/buscar/act.php?id=BOE-A-2007-22440#a2bis |

The software sanctions depend on the applicable conduct and operative requirements; the postponed user adaptation date must not be ignored. There is no self-contained payment-status fine created by RD 238/2026. Do not invent an amount “pending ministerial order”, treat every missing SII invoice as a EUR 150 record, or describe criminal penalties as imposed by the LGT itself. For non-late-record SII breaches, substantial non-compliance, potential criminal conduct or competing sanctions, do not compute a final liability from this table. Check this point with one of our partner accountants.

### 8. Reconcile with the tax work

Keep invoice exchange, VAT books, software records and returns separately reconciled. Use the applicable VAT return workflow for modelo 303 and any modelo 390 obligation/exemption; SII supplies VAT-book records and does not itself file the return. Do not promise that SPFE pre-fills returns or that SII replaces a fictitious quarterly informational annex. [RIVA arts. 62 and 71](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925#a71).

As a working-paper control, reconcile professional withholding with the applicable modelo 111/190 payer reporting and the recipient's annual income-tax records; reconcile the relevant invoice income with applicable modelo 100/130 or corporate modelo 200 work. Do not treat an RRSIF alta as proof that withholding returns have been filed or that every professional owes quarterly instalments. Those filing decisions belong to the relevant tax Guide.

For intra-EU supplies, acquisitions and services, test the actual modelo 349 conditions rather than saying every intra-EU service belongs on it. For imports, reconcile the customs document (DUA) and import VAT with the received-record entry. SII's specified intra-EU book is not a substitute for every invoice book or recapitulative return. The B2B customer-location test remains step 4, including a Spanish establishment of a foreign customer. [RIVA arts. 66, 69 bis and 79](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925#a79). For a cross-border return classification not established by the facts, do not infer the result from the invoice channel. Check this point with one of our partner accountants.

## Worked cases

### Case 1: late supply of SII records for a quarter

Preserved 2026 inputs: a monthly VAT filer inside SII supplies late issued/received-invoice records totalling **EUR 200,000**, including the relevant taxes and surcharges, in one quarter. Assuming the late-record offence applies and no competing sanction displaces it, LGT art. 200.3 and RD 2063/2004 art. 16.3 give the unadjusted statutory calculation: **0.5% × EUR 200,000 = EUR 1,000**, within the quarterly **EUR 300 / EUR 6,000** bounds. Procedural liability, reductions and any competing sanction remain separate.

The original boundary inputs are retained: **EUR 40,000 × 0.5% = EUR 200**, increased to the quarterly minimum **EUR 300**. **EUR 1,200,000 × 0.5% = EUR 6,000** reaches the maximum; above that amount it remains capped. Do not use this computation for the capital-goods or specified intra-EU books, which have the different rule in step 7. [LGT art. 200.3](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a200); [RD 2063/2004 art. 16.3](https://www.boe.es/buscar/act.php?id=BOE-A-2004-18398#a16).

```oa-check
name: Spain 2026 SII late record fine for a quarter
inputs:
  late_invoices_total: 200000
  rate: 0.005
  quarterly_min: 300
  quarterly_max: 6000
steps:
  - raw_fine: late_invoices_total * rate
  - fine: min(max(raw_fine, quarterly_min), quarterly_max)
expected:
  raw_fine: 1000
  fine: 1000
```

```oa-check
name: Spain 2026 preserved SII quarterly boundaries
inputs:
  low_total: 40000
  cap_total: 1200000
  rate: 0.005
  quarterly_min: 300
  quarterly_max: 6000
steps:
  - low_raw: low_total * rate
  - low_fine: min(max(low_raw, quarterly_min), quarterly_max)
  - cap_raw: cap_total * rate
  - cap_fine: min(max(cap_raw, quarterly_min), quarterly_max)
expected:
  low_raw: 200
  low_fine: 300
  cap_raw: 6000
  cap_fine: 6000
```

## When to refuse or refer

- For Basque provincial/Navarre software systems including TicketBAI, do not apply this state-law software workflow as a foral determination. Check this point with one of our partner accountants.
- For Canary Islands IGIC or Ceuta/Melilla IPSI, do not apply this IVA rate card. Check this point with one of our partner accountants.
- For disputed turnover measurement, non-established-supplier EU scope, authorisations, technical integration or sanction liability, apply the specific holds in the relevant step. Check this point with one of our partner accountants.
- For deductibility of a late, defective or wrongly routed invoice, do not treat transmission acceptance as a VAT deduction ruling. Check this point with one of our partner accountants.

## Completion checklist

Record the 2026 tax point, recipient establishment, relevant entity/turnover conditions, SII status, software mode/version/declaration, public routing codes and correct B2B stage. Validate the chosen schema and response, preserve the receipt and immutable correction trail, reconcile books/returns and document every referred point as non-usable until resolved. This is a working-paper checklist, not professional certification of a software product.

## Sources

Read on 27 November 2026; article references above identify the operative provisions. The current software amendment and dated December VAT effects are distinguished from provisions already applicable at the tax point.

| Source | Provisions / material read | URL | Read on |
|---|---|---|---|
| Ley 25/2013 | Arts. 3-6, 9; additional provision 2; final provision 8 | https://www.boe.es/buscar/act.php?id=BOE-A-2013-13722 | 2026-11-27 |
| HAP/1074/2014 | Arts. 3-7 and annex I, public entry/routing | https://www.boe.es/buscar/act.php?id=BOE-A-2014-6662 | 2026-11-27 |
| Facturae format | Published versions and official 3.2.2 schema | https://www.facturae.gob.es/formato/ultima-version | 2026-11-27 |
| Facturae 3.2.2 XSD | Fields, occurrence conditions, monetary precision and totals | https://www.facturae.gob.es/content/dam/facturae/formato/versiones/Facturaev3_2_2.xml | 2026-11-27 |
| Facturae signature-policy index | Policy documents identified; detailed profile is held, not asserted | https://www.facturae.gob.es/formato/politicas-firma-electronica | 2026-11-27 |
| RD 1624/1992 (RIVA) | Arts. 62, 65-66, 68 bis, 69 bis, 71.3, 79; only operative 2026 conditions used | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925 | 2026-11-27 |
| RD 1007/2023 | Arts. 1-5, 7-16; amended final provision 4 | https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840 | 2026-11-27 |
| RD-ley 43/2026 | Final provisions 1 and 4: software deadline amendment and commencement | https://www.boe.es/buscar/act.php?id=BOE-A-2026-24701 | 2026-11-27 |
| HAC/1177/2024 | Arts. 3-5, 13, 16, 21; final provision, technical-order commencement | https://www.boe.es/buscar/act.php?id=BOE-A-2024-22138 | 2026-11-27 |
| Ley 18/2022 | Art. 12 and final provision 8 | https://www.boe.es/buscar/act.php?id=BOE-A-2022-15818 | 2026-11-27 |
| Directive (EU) 2025/516 | Arts. 1(2)-(3), 7; Spanish official text via BOE; primary EU reader returned a challenge page | https://www.boe.es/buscar/doc.php?id=DOUE-L-2025-80487 | 2026-11-27 |
| RD 238/2026 | Arts. 2-13, 15; additional provisions 1, 2, 5; transitional provisions 2-3; final provision 4 | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295 | 2026-11-27 |
| HAC/1028/2026 | Arts. 3-5; final provision; annex I content reference | https://www.boe.es/buscar/act.php?id=BOE-A-2026-20587 | 2026-11-27 |
| AEAT B2B implementation note | Actual October order and deferred dates, not a draft rollout | https://sede.agenciatributaria.gob.es/Sede/informacion-institucional/puede-interesar/analisis/2026/octubre/29/facturacion-electronica-solucion-publica-facturacion-atras.html | 2026-11-27 |
| RD 1619/2012 | Arts. 2-4, 6-7, 11, 18-23: particulars, issuing and archive | https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696 | 2026-11-27 |
| Ley 37/1992 (LIVA) | Arts. 90-91, 107, 121, 154, 159, 161 | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 | 2026-11-27 |
| RD-ley 29/2026 | Art. 7, expressly effective 1 December 2026 | https://www.boe.es/buscar/act.php?id=BOE-A-2026-20823 | 2026-11-27 |
| RD 439/2007 (RIRPF) | Arts. 75-76, 95.1: payer scope and professional withholding | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 | 2026-11-27 |
| Ley 58/2003 (LGT) | Arts. 66, 68, 70, 179, 188, 200, 201, 201 bis | https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186 | 2026-11-27 |
| RD 2063/2004 | Art. 16.3-4: SII sanction bases/registers and competing sanction | https://www.boe.es/buscar/act.php?id=BOE-A-2004-18398 | 2026-11-27 |
| Ley 56/2007 | Art. 2 bis: free interconnection/copies and consumer penalty | https://www.boe.es/buscar/act.php?id=BOE-A-2007-22440 | 2026-11-27 |
| Código de Comercio | Art. 30, six-year commercial retention | https://www.boe.es/buscar/act.php?id=BOE-A-1885-6627 | 2026-11-27 |

Not yet confirmed: no unsupported outcome is usable. The explicit partner-accountant holds above cover technical profiles/validation mappings, foral/local-tax rules, unusual VAT/withholding eligibility, authorisations, non-established-supplier EU boundaries and assessed sanctions; they do not postpone the ordinary source-backed routes and dates.

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal, gestor administrativo, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

> Contributed by OpenAccountants.
