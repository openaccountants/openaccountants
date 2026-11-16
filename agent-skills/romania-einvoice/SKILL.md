---
name: romania-einvoice
description: "Use this skill whenever asked about e-invoicing in Romania, RO e-Factura, ANAF electronic invoice system, SPV (Spațiul Privat Virtual), B2B e-invoice clearance model, UBL 2.1 Romania, CIUS-RO, XML invoice validation, or any question about issuing, transmitting, validating, or archiving electronic invoices under Romanian law. Trigger on phrases like \"e-Factura\", \"RO e-Factura\", \"ANAF invoice\", \"SPV portal\", \"CIUS-RO\", \"B2B clearance Romania\", \"B2C e-invoice Romania\", \"OUG 115/2023\", \"EN 16931 Romania\", or \"invoice validation ANAF\". ALWAYS read this skill before touching any Romania invoicing compliance work."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/romania-einvoice"
  jurisdiction: "RO"
  tax_year: "2026"
  last_updated: "2026-11-15"
---

# Romania RO e-Factura: classify, prepare, transmit and retain (2026)

## Scope

Use this skill to prepare an invoice classification, XML validation and transmission working paper for Romania's RO e-Factura system, administered by ANAF and the Ministry of Finance (MF). It does not submit invoices, authenticate to SPV, register a taxpayer, make payments or call a live API. The output records the legal route, invoice data, deadline, validation evidence, communication date, correction trail and archive location for professional review.

The system uses structured XML, rather than a PDF sent by email. The original electronic invoice is the XML with the MF electronic seal. The seal attests receipt by the system; structural, syntactic and semantic checks do not verify the reality of the transaction. Calling the system a clearance model must not imply that ANAF has approved the transaction, tax treatment or deduction (OUG 120/2021 art. 4; OMF 1365/2021 annex art. 3).

The current OUG 120/2021 portal version selects 1 June 2026. Law 88/2026 changed CNP suppliers, special-regime farmers and consumer identification from that date. The source clauses and relevant neighbours below were read on 15 November 2026. The failed current MF technical-page and EUR-Lex recoveries are identified under Not yet confirmed; this skill supplies no guessed screen, endpoint, credential or validator-release instruction.

## Ask the client first

1. Who issues the invoice, where are they established for VAT purposes, and do they identify fiscally by CNP? Are they a special-regime individual farmer, a non-VAT NGO/political party/religious body, or an optional-register participant?
2. Who buys: a taxable business, public institution or consumer? Obtain the buyer's actual VAT/fiscal identifier or record that an individual supplied none. Is the public contract covered by the procurement, concession or defence rules? Does the transaction have its place of supply in Romania?
3. What is supplied, at what tax point, quantity, price and tax treatment? Establish any exemption, reduced-rate conditions, advance, discount, return or self-invoice before assigning XML codes.
4. What are the issue date, legal issue deadline, currency, VAT chargeability date, contractual exchange-rate basis, payment terms and amount payable? Establish the transmission deadline independently of the commercial due date.
5. Is an original invoice already communicated? Obtain its XML, seal, index, dates, reference and any objection/error message before preparing a correction or retransmission. Identify the authorised SPV user and the separate accounting archive.

## The method, step by step

### 1. Decide the legal route before making XML

The ordinary established-taxpayer rules have no turnover exemption. Being outside VAT registration does not by itself remove the mandate. Apply the specific exclusions and optional categories below, rather than assuming all small taxpayers or all foreign businesses have the same route.

| Situation | Treatment in 2026 | Official source |
|---|---|---|
| Established supplier in a B2G public-procurement relationship | Apply B2G; non-established operators may opt in. Classified contracts and specified essential-security measures are excluded. Domestic supplies to public institutions outside the defined B2G contract relationship are also covered by art. 9^1. Apply the CNP/farmer exceptions below where relevant. | [OUG 120/2021 arts. 5–9^1 and 13](https://legislatie.just.ro/public/DetaliiDocument/247243) |
| Romanian-established taxable issuer, domestic B2B place of supply | Mandatory, whether VAT-registered or not; the art. 10(1) exceptions cover fiscal cash-register receipts meeting simplified-invoice conditions and intra-Community supplies where the buyer communicates another member state's VAT number. Do not equate all exports, OSS or foreign customers with an exclusion. | [OUG 120/2021 art. 10(1)](https://legislatie.just.ro/public/DetaliiDocument/247243) |
| Established issuer supplies a non-established customer registered for VAT in Romania | Included from 1 January 2026 for domestic supplies under art. 10(1^1); communicate the invoice to that customer as art. 10 requires. Romanian VAT registration alone does not make a non-established issuer automatically mandatory: art. 13 gives that issuer an option. | [OUG 120/2021 arts. 10 and 13; OUG 89/2025 X](https://legislatie.just.ro/public/DetaliiDocument/247243) |
| Established issuer issues a B2C invoice for a Romanian-place supply | Report the issued invoice; the mandate does not itself require an invoice for every retail receipt. The exception is fiscal cash-register receipts meeting simplified-invoice conditions, rather than every simplified invoice. Normally still send the consumer the invoice outside the system; apply the optional-register exception in art. 10^1(4). | [OUG 120/2021 art. 10^1](https://legislatie.just.ro/public/DetaliiDocument/247243) |
| Consumer gives no fiscal identifier | Use 13 zero digits in place of the buyer fiscal identifier. An individual identifying by CNP is B2C unless the stated optional-register case applies. Do not require a consumer to provide a CNP merely to populate the field. | [OUG 120/2021 art. 10^1(3); Law 88/2026 III.1](https://legislatie.just.ro/public/DetaliiDocument/247243) |
| Supplier/prestator identifies fiscally by CNP | From 1 June 2026, exempt from the listed mandatory B2G/B2B/B2C provisions and may opt in. The old 15 January enrolment rule and subsequent deferral to 1 June are not a current compulsory-enrolment instruction. | [OUG 120/2021 art. 10^10; Law 88/2026 III.8, IV](https://static.anaf.ro/static/10/Anaf/legislatie/L_88_2026.pdf) |
| Individual farmer applies the Fiscal Code art. 315^1 special regime | Exempt, with optional use, from 1 June 2026. The old blanket assertion that the farmer exemption expired in July 2025 must not be used. | [OUG 120/2021 art. 10^7; Law 88/2026 III.4, IV](https://static.anaf.ro/static/10/Anaf/legislatie/L_88_2026.pdf) |
| Non-VAT associations/foundations, other non-profit associations, political parties and religious bodies under art. 10^6 | Their temporary exemption ended on 30 June 2025; entities undertaking the covered economic activities enter the mandatory route from 1 July 2025. This is not a general small-taxpayer exemption. | [OUG 120/2021 art. 10^6](https://legislatie.just.ro/public/DetaliiDocument/247243) |
| Persons outside the VAT scope with no art. 319 invoice obligation; specified diplomatic/international bodies and cultural institutes | Apply the actual art. 10^3 exclusion or art. 10^5 optional conditions. Article 319(8) self-invoices are B2B documents under art. 10^4. | [OUG 120/2021 arts. 10^3–10^5](https://legislatie.just.ro/public/DetaliiDocument/247243) |

The historical rollout remains relevant to old invoices: the original recorded November 2021 launch, July 2022 B2G/high-risk B2B, January 2024 general B2B reporting, July 2024 structured B2B exchange and January 2025 B2C reporting. These dates do not replace the current route or prove an old invoice's exact deadline. The unverified historical high-risk product list and technical milestones are held below.

### 2. Establish tax treatment, amount and currency

| Treatment | Rate or amount | Conditions and period | Official source |
|---|---|---|---|
| Standard VAT | 21% | Taxable supplies outside a reduced rate or exemption; effective from 1 August 2025 | [Fiscal Code art. 291(1)](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Reduced VAT | 11% | Only an applicable art. 291(2) category with its conditions; the examples in the following paragraph are not a complete tariff or classification decision | [Fiscal Code art. 291(2)](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Historical qualifying home transition | 9% | Only the Law 141/2025 III conditions; individual delivery no later than 31 July 2026, and qualifying town-hall buildings until 1 August 2026. Neither window remains available for a new November 2026 supply. | [Law 141/2025 art. III](https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf) |

The original reduced-rate topics are retained: human medicines; food with its alcohol, NC 2202 drink, added-sugar and supplement exclusions; water/sewerage and irrigation; qualifying agricultural inputs/services; books/press subject to content exclusions; the specified museum/historic/zoo/botanical admissions; qualifying firewood with beneficiary/end-use conditions; cold-season heat for the listed users; the specified social-policy buildings; hotel/camping accommodation; and restaurant/catering excluding alcohol and NC 2202 drinks. Establish the exact statutory category and current amendment before using 11%. This summary does not turn all food, all buildings or all admissions into reduced-rate supplies.

For the historical individual-home transition, preserve the cumulative conditions: one qualifying home, at most 120 square metres and RON 600,000 excluding VAT, habitable at delivery by 31 July 2026, no other reduced-rate home since 1 January 2023, and a qualifying advance contract by 1 August 2025. Contracts concluded from 3 to 31 July 2025 also require the stated 20% advance paid by 31 July 2025. The town-hall transition requires the qualifying pre-1-August-2025 advance instrument. These are historical classification tests, not an offer of 9% on later sales. The former general 19%, 5% and 9% rates must not be used merely because an old software template contains them.

Treat exports/intra-Community supplies and financial, insurance, education or healthcare transactions under their actual exemption and deduction conditions. An exemption with or without deduction is not a numeric 0% VAT rate. This skill does not determine those conditions from a document code alone; the old blanket category outcomes are held below pending transaction-specific evidence.

An invoice may use any currency, including RON or EUR; collected or adjusted VAT must be expressed in RON (art. 319(23)). For non-import transactions, art. 290(2) allows the last applicable BNR or ECB rate at VAT chargeability, or the settlement-bank rate where the contract so provides; ECB cross-conversion uses the euro. The cash-accounting rule uses the chargeability date that would have applied outside that regime. Imports use their customs exchange rules under art. 290(1). Do not hard-code BNR as the sole permitted rate or apply an arbitrary invoice-date rate. Retain the currency, selected lawful rate, date and conversion evidence.

### 3. Build the legal data set, then the verified syntax

Fiscal Code art. 319(20) supplies the full-invoice data, with conditional fields and simplified-invoice rules in art. 319(21). Record the unique sequential number, issue date, actual supplier and buyer identification/name/address, supply/advance date where required, description, quantity and unit, taxable base, unit price and discounts, rate/tax or applicable exemption/reverse-charge wording, and totals. Do not label every old XML-table field universally mandatory. For a positive amount payable, the MF code guidance requires a payment due date **or** payment terms. CPV codes are obligatory for the public-procurement, concession and defence/security contracts listed in OUG 120 art. 4(2^1); a general B2B recommendation is not a universal legal requirement.

OMF 1366/2021 accepts UBL 2.1 and UN/CEFACT CII 16B under the European EN 16931 framework. Its legal specification identifier is `urn:cen.eu:en16931:2017#compliant#urn:efactura.mfinante.ro:RO_CIUS:1.0.0.2021`; this is distinct from a downloadable validator software release. The old assertion that `ro16931-ubl-1.0.9` is the latest release effective 5 June 2024 is not confirmed. Before implementation, obtain the current authoritative package and check its rules against the actual invoice or credit-note syntax. The old paths remain an unusable inventory below rather than a tested schema mapping.

### 4. Correct without cancelling or duplicating a communicated original

An invoice communicated through the system cannot be returned in it. The buyer can record an objection message; correction follows Fiscal Code art. 330 and uses the same system. For an already sent invoice, preserve the original reference and the statutory negative/correct-value correction trail. The MF code guidance distinguishes normal invoice 380, credit note 381, corrective invoice 384, self-invoice 389 and informative 751. Code 381 credit-note lines use positive values; a code 380 reversal uses negative values except for the unit price. This syntax distinction does not mean every correction must be 381. Do not copy an InvoiceLine XPath into a CreditNote document without validating that syntax.

Never assume the platform will reject a duplicate. MF guidance warns that a minor space or punctuation change can create a second invoice without technical cancellation. Identify the existing communication/index and use the documented correction trail rather than repeatedly uploading altered files. The legal original and any readable PDF remain separate; conversion does not turn the PDF into the sealed XML original.

### 5. Prepare transmission and retain its evidence

Under OMF 1365/2021, the issuer uses SPV in its own capacity or through its legal/designated representative or attorney. The procedure provides machine-to-machine APIs and the free MF application. Prepare the invoice, validate the supported structure, upload through the verified current route, retain the automatically assigned index, check the processing state, correct an error file and retransmit where appropriate, and download the resulting sealed XML/response. This is the legal workflow, not a claim that current buttons, OAuth settings, certificate provisioning or endpoint parameters were tested.

The system's publication/download-availability date is the legal communication date under OUG 120 art. 4(7), even if the buyer downloads later. XML and error files remain available for 60 days from publication, then are archived and released on request under OMF 1365 annex art. 8. Download promptly into the taxpayer's own archive; 60 days is a system availability period, not the taxpayer's retention period or a separately established universal buyer deadline.

Keep authenticity of origin, integrity of content and legibility under art. 319(25), with inspector access throughout lawful retention. Law 82/1991 art. 25 retains accounting registers and supporting documents for **5 years from 1 July following the financial year in which prepared**. Article 35(3) separately retains annual, consolidated and interim financial statements for **10 years**; that does not make every invoice a 10-year record. Fiscal Code art. 319(31)–(37) governs invoice copies, storage/access and notification of storage outside Romania. Apply its international-assistance and online-access conditions; neither a blanket EU-only storage rule nor an unconditional anywhere-storage rule is sufficient. Keep the original XML/seal and correction/evidence files; a readable PDF is an aid, with integrity preserved.

### 6. Reconcile the books and surviving reporting duties

Reconcile transmitted invoices, error/correction trails, VAT ledgers and D300 with the actual tax treatment. OUG 70/2024 art. 3 preserves the pre-filled RO e-TVA return, sent by the 5th of the month after the D300 filing deadline. It is not a tax assessment and does not relieve the taxpayer of checking the facts.

**Do not follow the obsolete e-TVA notice instructions in the linked passing sibling [ro-vat-return](ro-vat-return.md).** OUG 13/2026 IV repealed the whole of OUG 70 arts. 5, 8 and 16 from 9 March 2026. The former automatic statutory notice based on a difference of at least 20% and RON 5,000, and the old cash-accounting notice-resumption timetable, are historical and unusable as current instructions. The earlier January 2026 removal of the answer/fine duty alone is not the full current amendment. The surviving return still requires reconciliation.

Keep invoice data consistent with any independently applicable SAF-T/D406, RO e-Transport and corporate-tax records. The old limited SAF-T population, automatic matching/confiscation proposition and specific corporate-assessment feed mechanics have not been established here; they are held below. The e-invoice seal does not settle VAT deductibility or substantive revenue/expense treatment.

## Worked cases

### Case 1: foreign-currency invoice and partial credit

A qualifying domestic taxable supply has a net invoice of EUR 1,000 at the standard 21% rate. Assume the documented lawful art. 290 exchange basis at chargeability is RON 5.05 per EUR. VAT is EUR 210 and RON 1,060.50; gross is EUR 1,210. A later price reduction returns EUR 200 net at the same assumed rate/tax treatment: credit effect is EUR 42 VAT, RON 212.10 VAT and EUR 242 gross. The remaining net/VAT/gross are EUR 800/EUR 168/EUR 968. A code 381 representation uses positive credit values; a code 380 reversal represents the reversal with negative amounts, subject to the unit-price rule. Neither changes the economic reduction. Original reference, the actual art. 330 correction and the applicable currency evidence are required.

```oa-check
name: RO 2026 currency invoice and partial credit
inputs:
  net_eur: 1000
  credit_net_eur: 200
  rate: 0.21
  fx: 5.05
steps:
  - vat_eur: net_eur * rate
  - vat_ron: vat_eur * fx
  - gross_eur: net_eur + vat_eur
  - credit_vat_eur: credit_net_eur * rate
  - credit_vat_ron: credit_vat_eur * fx
  - credit_gross_eur: credit_net_eur + credit_vat_eur
  - remaining_net: net_eur - credit_net_eur
  - remaining_vat: vat_eur - credit_vat_eur
  - remaining_gross: gross_eur - credit_gross_eur
  - code380_reversal_gross: 0 - credit_gross_eur
expected:
  vat_eur: 210
  vat_ron: 1060.50
  gross_eur: 1210
  credit_vat_eur: 42
  credit_vat_ron: 212.10
  credit_gross_eur: 242
  remaining_net: 800
  remaining_vat: 168
  remaining_gross: 968
  code380_reversal_gross: -242
```

### Case 2: distinguish an invoice-value offence from monthly late reporting

Assume three otherwise in-scope established-party B2B invoices have gross values RON 12,100, RON 6,050 and RON 2,420. If the proven facts constitute the art. 13^2(1)(a) issuer offence, 15% of the total RON 20,570 is RON 3,085.50; the respective invoice amounts are RON 1,815, RON 907.50 and RON 363. The corresponding recipient offence requires its own statutory facts. If the facts instead constitute only the art. 13^2(1)(c) late-transmission offence, all three deadlines falling in one calendar month form the monthly category offence: for an ordinary small legal person the band is RON 1,000–2,500, not three times that band. These are alternative assumed legal classifications for comparison, not a taxpayer option, an automatic combined fine or a final enforcement decision.

```oa-check
name: RO invoice-value sanction and monthly deadline grouping
inputs:
  first: 12100
  second: 6050
  third: 2420
steps:
  - total: first + second + third
  - first_value_fine: first * 0.15
  - second_value_fine: second * 0.15
  - third_value_fine: third * 0.15
  - total_value_fine: first_value_fine + second_value_fine + third_value_fine
  - incorrect_three_minima: 3 * 1000
  - incorrect_three_maxima: 3 * 2500
  - monthly_minimum: incorrect_three_minima / 3
  - monthly_maximum: incorrect_three_maxima / 3
expected:
  total: 20570
  first_value_fine: 1815
  second_value_fine: 907.50
  third_value_fine: 363
  total_value_fine: 3085.50
  incorrect_three_minima: 3000
  incorrect_three_maxima: 7500
  monthly_minimum: 1000
  monthly_maximum: 2500
```

## When to refuse or refer

Stop before issuing a filing-ready XML or prescribing a live upload where establishment, place of supply, optional-register status, invoice obligation, tax category, current schema or representative authority is unresolved. Do not infer substantive deductibility from the seal, silently replace an already communicated original, invent a consumer CNP, assume duplicate protection, or use a failed technical URL as evidence of a current release. Refer transaction-specific exemptions, customs/OSS rules, SAF-T, e-Transport, cross-border currency exceptions and tax disputes to the appropriate professional with the actual records.

## Filing and payment

Fiscal Code art. 319(16) ordinarily requires issuance by the 15th of the month after the chargeable event, and for advances by the 15th after receipt, subject to its stated exception where already issued. OUG 120 art. 10(7) and art. 10^1(2^1) require B2B/B2C transmission within **5 working days from issue and no later than 5 working days from that legal issue deadline**, from 1 January 2026. The law expressly refers to Regulation 1182/71 for calculation; its actual calendar/holiday counting text was not recovered here, so do not manufacture a final dated deadline. Commercial payment terms do not extend the transmission deadline. Invoice transmission does not pay the tax or file D300.

| Offence | Figure | Scope | Official source |
|---|---|---|---|
| Art. 13^2(1)(a) issuer failure under art. 10(1), or (b) established B2B recipient receiving and recording a noncompliant invoice | 15% of total invoice value | Each statutory offence requires its own facts; distinguish late transmission | [OUG 120/2021 art. 13^2(1),(2)](https://legislatie.just.ro/public/DetaliiDocument/247243) |
| Art. 13^2(1)(c) late transmission or (d) B2C failure; large taxpayer | RON 5,000–10,000 | One or more invoice deadlines within a calendar month; B2C sanction from 1 July 2025 | [OUG 120/2021 art. 13^2(1)(c),(d),(3)](https://legislatie.just.ro/public/DetaliiDocument/247243) |
| Same monthly offence; medium taxpayer | RON 2,500–5,000 | Same monthly grouping | [OUG 120/2021 art. 13^2(3)](https://legislatie.just.ro/public/DetaliiDocument/247243) |
| Same monthly offence; other legal persons and individuals | RON 1,000–2,500 | Same monthly grouping; no generic per-incident multiplication | [OUG 120/2021 art. 13^2(3)](https://legislatie.just.ro/public/DetaliiDocument/247243) |

For a mandatory transaction paid at the time of supply, art. 10^9 permits the buyer who does not receive the invoice within the transmission deadline to notify the tax authority. Do not expand that conditional route to every late invoice or promise a particular enforcement outcome. The former universal permanent loss-of-VAT-deduction claim is not established here; substantive deduction conditions and correction remedies need their own analysis.

## Completion checklist

- Record issuer/buyer establishment, identifiers, supply location and exact mandatory/optional/excluded provision, including the current CNP/farmer rule.
- Retain the legal issue/transmission calculation, invoice data, tax point, category, rate, currency basis and professional resolution of exceptions.
- Validate against the verified authoritative syntax/package; keep the index, error/result, sealed XML and communication date. Preserve original references for corrections.
- Download into the taxpayer archive, record the 60-day system window separately from the 5-year accounting-record retention and the 10-year statement retention.
- Reconcile invoices/corrections with books and applicable returns. Use the surviving e-TVA return, with no repealed article 5 notice workflow. Keep technical and legal holds unresolved until evidence is obtained.

## Sources

| Official source and read scope | URL | Read on |
|---|---|---|
| OUG 120/2021, current selected 1 June 2026; definitions and arts. 4–10^10, 13–18, mandate, seal, exceptions, communication and sanctions | https://legislatie.just.ro/public/DetaliiDocument/247243 | 2026-11-15, read for those operative provisions and neighbours |
| Law 88/2026, III and IV; CNP/farmer choices, consumer identification and commencement | https://static.anaf.ro/static/10/Anaf/legislatie/L_88_2026.pdf | 2026-11-15, read for those provisions; operative law rather than a proposed deferral |
| OUG 89/2025 X–XIV and OG 6/2026 IX, deadline/recipient changes and the superseded CNP timeline | https://static.anaf.ro/static/10/Anaf/legislatie/OUG_89_2025.pdf ; https://static.anaf.ro/static/10/Anaf/legislatie/OG_6_2026.pdf | 2026-11-15, read for those provisions and later Law 88 interaction |
| Fiscal Code arts. 290–291, 319 and 330; currency, rates, required details, storage and correction | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm | 2026-11-15, read for those operative articles and neighbours; ANAF consolidation is not an official republication |
| Law 141/2025 II and III, VII; rate change and historical housing transition | https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf | 2026-11-15, read for those operative provisions and commencement |
| OMF 1365/2021 full annex arts. 1–8; SPV, submission, structural checks, corrections and availability | https://static.anaf.ro/static/10/Anaf/legislatie/OMF_1365_2021.pdf | 2026-11-15, read for the full operational annex |
| OMF 1366/2021 annex arts. 1–2 and start of art. 3; accepted syntaxes and legal specification identifier | https://static.anaf.ro/static/10/Anaf/legislatie/OMF_1366_2021.pdf | 2026-11-15, read for these clauses, not a claim to have tested every technical rule or current release |
| MF invoice-code guidance v2.9, sections 2.1–2.2 and 4–5; credit signs, codes, duplicate warning and payment terms | https://static.anaf.ro/static/10/Anaf/Informatii_R/Ghid%20cod%20facturi_final%20v2.9.pdf | 2026-11-15, read for those sections and relevant neighbours |
| Accounting Law 82/1991 arts. 25, 28 and 35; Law 36/2023 I.2 | https://legislatie.just.ro/Public/DetaliiDocument/38127 ; https://static.anaf.ro/static/10/Anaf/legislatie/L_36_2023.pdf | 2026-11-15, read for records/statement retention and the 5-year amendment |
| OUG 70/2024 arts. 3–9 current selected 9 March 2026, and OUG 13/2026 IV, VII | https://legislatie.just.ro/Public/DetaliiDocument/284214 ; https://static.anaf.ro/static/10/Anaf/legislatie/OUG_13_2026.pdf | 2026-11-15, read for the surviving pre-filled return and complete repeal of arts. 5, 8 and 16 |

Not yet confirmed:

### Technical inventory: preserved original assertions, unusable until recovered

The current MF technical page at `https://mfinante.gov.ro/web/efactura/informatii-tehnice` and its `/ro/` variant failed ordinary recovery, as did the cited `ro16931-ubl-1.0.9.zip` and API presentation. The original claims of latest release `ro16931-ubl-1.0.9`, effective 5 June 2024, current CUI/CIF format rules, national code lists and the exact following schema/component names are retained as an **unverified implementation inventory**, not a current validation contract:

- Historical literal: UBL 2.1 Invoice schema: `UBL-Invoice-2.1.xsd`
- Historical literal: UBL 2.1 CreditNote schema: `UBL-CreditNote-2.1.xsd`
- Historical literal: EN 16931 schematron: CEN/TC 434 base rules
- Historical literal: CIUS-RO schematron: `ro16931-ubl-1.0.9.sch`
- Historical literal: Primary namespace: `urn:oasis:names:specification:ubl:schema:xsd:Invoice-2`
- Historical literal: Common components: `urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2`

The full original field-path inventory follows. Its old Notes column is a historical assertion, **not a current requirement**: the present buyer/CNP, currency, payment-terms, tax-point and CPV conditions above control. None of these paths was validated against a current downloaded schema, and CreditNote syntax may differ. Do not use this table to generate filing-ready XML:

| Field | UBL Path | Notes |
| --- | --- | --- |
| Supplier tax ID (CUI/CIF) | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | Must be valid Romanian CUI or CIF |
| Buyer tax ID | `cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | Required for B2B; for B2C, use CNP or omit |
| Invoice number | `cbc:ID` | Unique, sequential |
| Issue date | `cbc:IssueDate` | ISO 8601 format |
| Due date | `cbc:DueDate` | Required if applicable |
| Invoice type code | `cbc:InvoiceTypeCode` | 380 (invoice), 381 (credit note), 389 (self-billed) |
| Currency code | `cbc:DocumentCurrencyCode` | RON or EUR; if non-RON, must include exchange rate |
| Tax point date | `cbc:TaxPointDate` | Date of supply |
| Supplier name and address | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress` | Full legal address |
| Buyer name and address | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress` | Full legal address |
| Line item description | `cac:InvoiceLine/cac:Item/cbc:Name` | Description of goods/services |
| Line quantity and unit | `cac:InvoiceLine/cbc:InvoicedQuantity` | With `@unitCode` |
| Line net amount | `cac:InvoiceLine/cbc:LineExtensionAmount` |  |
| Tax category and rate | `cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` + `cbc:Percent` | Per VAT rate |
| Total tax amount | `cac:TaxTotal/cbc:TaxAmount` |  |
| Payable amount | `cac:LegalMonetaryTotal/cbc:PayableAmount` |  |
| CPV code | `cac:InvoiceLine/cac:Item/cac:CommodityClassification/cbc:ItemClassificationCode` | Required for B2G; recommended for B2B |

The original popularity claims that UBL is the primary/most common syntax and CII is rarely used have not been established; do not use them as a compliance test. Additional unrecovered technical claims are the dedicated B2C upload endpoint allegedly mandatory since 31 March 2025; the exact web navigation `anaf.ro → Factura electronică → Trimitere Factură`; qualified digital-certificate enrolment and current REST authentication/endpoint parameters; response literals `ok`/`nok` and download-ID semantics; the current “Limite Apeluri API” quotas; CUI/CIF public-API checks; and exact automatic rejection behaviour for schema, CIUS, invalid CUI, duplicate invoice, invalid tax category, empty mandatory element and issue/tax-point date inconsistencies. The procedure supports validation/errors, but does not prove these implementation details or guarantee duplicate rejection. Do not call a live API to resolve them without the required authority and verified documentation.

The original per-line rounding to 2 decimals followed by summing rounded VAT, a universally separate `cac:TaxSubtotal` per VAT rate under `cac:TaxTotal`, and the universal credit-reference XPath `cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` remain untested technical propositions. Preserve the lawful taxable base/rate, currency and correction reference; obtain the exact current syntax and rounding rules before asserting acceptance.

### Other preserved boundaries and superseded assertions

- Historical timeline labels are not fully re-established here: November 2021 launch/voluntary B2B, July 2022 high-risk B2B list of fruit, vegetables, alcohol, mineral water, construction and new buildings; January 2024 reporting described as 5 working days; and the technical phrase “invoice legally valid only after ANAF validation” from July 2024. The current original/seal rule above replaces any suggestion that validation approves transaction reality. Exact historic scope/deadline requires the then-operative act. OUG 115/2023, 69/2024 and 138/2024 remain part of the historical amendment trail, not a substitute for the current consolidated articles.
- The old July 2025 “all remaining B2C exemptions expire” and January 2026 compulsory CNP enrolment conclusions are superseded as described above; the old B2C penalty grace ending 31 March 2025 is rejected by the current 1 July 2025 sanction commencement. Simplified invoices are not universally excluded; apply the exact fiscal-cash-register-receipt exception. Non-established issuers, exports, OSS and outside-Romania services require the actual establishment/place/transaction route rather than the old blanket exclusions.
- The old 0% labels for exempt exports/intra-Community supplies and financial/insurance/education/healthcare were not legal rates. Their transaction-specific exemption, deduction and invoicing conditions are not determined in this skill. Likewise, the exact reduced-rate category additions after the reproduced ANAF art. 291 list must be checked in the amending acts before category-specific advice; its list is not claimed exhaustive.
- Regulation 1182/71 calendar/holiday counting was not recovered from EUR-Lex. Do not invent a calendar deadline. The old universal buyer-download-within-60-days claim, 10-year invoice-record retention from year end, EU-only storage rule and permanently lost deduction conclusion are not usable current rules; apply the verified availability/retention/access rules and refer unresolved deduction conditions.
- SAF-T/D406 scope and commencement are not freshly established. The old statement that it concerns large and medium taxpayers does not exclude other categories. Specific automatic cross-check/audit thresholds, e-Transport matching references or confiscation outcomes, and an automatic corporate-tax assessment feed are unconfirmed. Do not use these unsupported assertions as filing instructions or sanctions.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

> Contributed by Michael Cutajar.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-15. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `romania-einvoice` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/romania-einvoice. If neither is available, confirm every figure against the official source pages cited above before relying on it.
