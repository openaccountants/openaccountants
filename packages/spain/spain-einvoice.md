---
name: spain-einvoice
description: Use this skill whenever asked about Spanish e-invoicing, factura electrónica Spain, FACe, Facturae, Veri*factu, VERI*FACTU, SII (Suministro Inmediato de Información), AEAT e-invoicing, B2B e-invoicing mandate Spain, RD 1007/2023, RD 238/2026, Ley Crea y Crece, QR tributario, anti-fraud invoicing software, SPFE (Solución Pública de Facturación Electrónica), or any question about issuing, receiving, validating, or archiving electronic invoices in Spain. Also trigger when configuring Veri*factu-compliant billing software, setting up SII real-time reporting, submitting B2G invoices via FACe, or advising on the transition from SII to Veri*factu. This skill covers FACe B2G, SII reporting, Veri*factu anti-fraud system, B2B mandate timeline, accepted formats (Facturae, UBL, CII), mandatory fields, validation rules, archiving, penalties, and interaction with Spanish VAT returns. ALWAYS read this skill before touching any Spanish e-invoicing work.
version: 1.0
jurisdiction: ES
tax_year: 2026
last_updated: 2026-09-23
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - einvoice-workflow-base
category: invoicing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spain: electronic invoicing, Veri*factu, FACe and the SII

Spain runs four separate things that people call "e-invoicing", and they start on different dates. Figures are for tax year 2026. Electronic invoicing to public bodies has been compulsory since 15 January 2015. The immediate supply of invoice records to the Agencia Tributaria (the SII) has run since 2017 for monthly filers. The invoicing software rules of Real Decreto 1007/2023, known as Veri*factu, bite before 1 January 2027 for corporate income tax payers and before 1 July 2027 for everyone else. The business-to-business electronic invoice of Ley 18/2022 now has its regulation, Real Decreto 238/2026 of 25 March 2026, in force since 20 April 2026, but the duty itself has no calendar date yet: it runs twelve or twenty-four months from the entry into force of a ministerial order that has not been made. Any date you have seen for the business-to-business mandate, including 2027 and 2028 dates, is not printed on an official page. Some penalty amounts below come from Ley 58/2003 and are not year specific.

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | Spain (Reino de España) |
| Currency | EUR |
| Public sector platform | FACe, the punto general de entrada de facturas electrónicas of the Administración General del Estado |
| Public sector format | Facturae, current version 3.2.2 (XML) |
| Real-time reporting | SII (Suministro Inmediato de Información), compulsory for monthly filers |
| Invoicing software rules | Reglamento de sistemas informáticos de facturación (Real Decreto 1007/2023), with the Veri*factu option |
| Business-to-business system | Sistema español de factura electrónica: private exchange platforms plus the solución pública de facturación electrónica run by the Agencia Tributaria |
| Governing body | Agencia Estatal de Administración Tributaria |
| Key legislation | Ley 25/2013 (public sector); Ley 18/2022 Crea y Crece (business to business); Real Decreto 238/2026 (business-to-business technical rules); Real Decreto 1007/2023 (invoicing software); Real Decreto 1619/2012 (invoicing obligations) |
| Public sector compulsory since | 15 January 2015 |
| Immediate supply of information compulsory since | Monthly filers, under art. 62.6 of the VAT Regulation |
| Software adaptation deadline | Before 1 January 2027 for corporate income tax payers; before 1 July 2027 for the rest |
| Business-to-business mandate | No calendar date. Twelve months (larger turnover) or twenty-four months (everyone else) after a ministerial order that has not yet been made |
| Guide version | 2.0 |

Nothing in this Guide covers the Basque provincial systems (TicketBAI in Bizkaia, Araba and Gipuzkoa) or the Navarre system. Those territories legislate their own invoicing software rules.

## Section 2: Mandate Scope

### Four Parallel Systems

Spain operates distinct but overlapping systems:

1. **FACe and the public sector.** Compulsory electronic invoicing to public administrations since 15 January 2015, under [Ley 25/2013](https://www.boe.es/buscar/act.php?id=BOE-A-2013-13722).
2. **The SII.** Electronic supply of invoice records to the Agencia Tributaria through the Sede electrónica, compulsory for anyone whose VAT period is the calendar month, under art. 62.6 of the [VAT Regulation](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925).
3. **Veri*factu and the invoicing software rules.** Requirements that billing software must meet, under [Real Decreto 1007/2023](https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840), with a deadline in 2027.
4. **The business-to-business electronic invoice.** Structured invoices between businesses and professionals, under art. 12 of [Ley 18/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-15818) and [Real Decreto 238/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295), with no start date yet.

These are not stages of one reform. A business can be inside one and outside the others.

### Who Must Comply

**Public sector invoicing, Ley 25/2013**

| Rule | What the law says |
| --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2013-13722 |
| Who must use an electronic invoice | Art. 4.1: sociedades anónimas, sociedades de responsabilidad limitada, legal persons and entities without legal personality that are not Spanish, permanent establishments and branches of non-resident entities, temporary joint ventures, and the listed funds and economic interest groupings |
| Who may use one | Every other supplier that has delivered goods or supplied services to a public administration |
| Possible exclusion | Art. 4.1: administrations may by regulation exclude invoices of up to EUR 5,000, and invoices from suppliers to a public administration's services abroad |
| Where it goes | Art. 6: the punto general de entrada de facturas electrónicas of the State, the autonomous community or the local entity |
| Since | Art. 4 took effect on 15 January 2015 (disposición final octava) |

**The SII**

| Rule | What the regulation says |
| --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925 |
| Compulsory for | Art. 62.6: anyone whose VAT period is the calendar month under art. 71.3 |
| Monthly period | Art. 71.3: turnover in the previous calendar year above EUR 6,010,121.04; a buyer of a business whose combined turnover passed it; anyone in the registro de devolución mensual; anyone applying the special scheme for groups of entities; holders of fuel tax warehouses and anyone extracting those products from one |
| Optional for | Art. 68 bis: anyone else may opt in |

The turnover test and the deadlines here are the same as in the `es-vat-return` Guide, and they come from the same regulation.

**Veri*factu and the invoicing software rules**

| Who | Duty and date |
| --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840 |
| Corporate income tax payers (art. 3.1.a) | Systems adapted before 1 January 2027 |
| Everyone else in art. 3.1: income tax payers with an economic activity, non-resident income tax payers with a permanent establishment, and entities in the régimen de atribución de rentas with an economic activity | Systems operative before 1 July 2027 |
| Producers and sellers of invoicing software (art. 3.2) | Products fully adapted within nine months of the technical ministerial order taking effect |
| Not covered at all (art. 3.3) | Anyone who keeps the VAT registers under art. 62.6 of the VAT Regulation, that is, anyone inside the SII, whether compulsorily or by choice |
| Not covered (art. 3.1.a) | Entities exempt under art. 9.1 of the corporate income tax law. Partly exempt entities under art. 9.2, 9.3 and 9.4 are covered only for operations producing income that is subject and not exempt |
| Not covered, no software | Anyone who invoices exclusively by hand, without any invoicing system. The Agencia Tributaria states the scope as four conditions, the first being that the business does not invoice only manually ([FAQ](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes/cuestiones-generales-ambitos-aplicacion.html)) |
| Not covered, on a ruling | Art. 5: the head of the Departamento de Inspección Financiera y Tributaria may resolve, on application, that the regulation does not apply to a sector, to named taxpayers, or to operations with exceptional technical difficulties |

The two 2027 dates are confirmed on the Agencia Tributaria's own note, which says entities filing corporate income tax must have adapted before 1 January 2027 and the rest before 1 July 2027, and calls the period before each date a testing period ([nota informativa](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/nota-informativa-ampliacion-plazo-adaptacion-facturacion.html)). The technical ministerial order took effect on 29 July 2025, so the nine months allowed to software makers by disposición final cuarta ran out during 2026. The Agencia Tributaria gives that date on its frequently asked questions page ([FAQ](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes/cuestiones-generales-ambitos-aplicacion.html)). Systems inside a multi year maintenance contract are instead adapted by the two 2027 dates.

Art. 3.3 matters more than anything else on this page. A business inside the SII is outside the invoicing software rules. Do not tell an SII client that its software must also be certified under the 2023 regulation.

**The business-to-business electronic invoice**

| Rule | What the law and the decree say |
| --- | --- |
| Who | Art. 3 Real Decreto 238/2026: any business or professional obliged to issue an invoice, where the customer is a business or professional with its seat, permanent establishment or habitual residence in Spain and the operation is for that place |
| Start, larger businesses | Twelve months after the ministerial order in disposición final tercera takes effect, for those whose volumen de operaciones under art. 121 of the VAT law exceeded eight million euros in the previous calendar year |
| Start, everyone else | Twenty-four months after that order takes effect |
| State reporting, individuals below the turnover line | Disposición transitoria tercera: for individuals and entities in the régimen de atribución de rentas whose volumen de operaciones under art. 121 of the VAT law did not exceed eight million euros in the previous calendar year, arts. 10 and 12 apply only twelve months after the decree takes effect for the second stage. Until then reporting the states of an invoice is voluntary |
| Condition on the law itself | Disposición final octava Ley 18/2022: art. 12 comes into force only once Spain obtains the derogation from arts. 218 and 232 of Council Directive 2006/112/EC |
| Not in scope | Art. 4: operations documented by a simplified invoice, unless it is a qualified simplified invoice under art. 7.2 of the invoicing regulation |
| Excluded sectors | Disposición adicional segunda: the regulated activities of the electricity market operator, the functions of the organised gas market operator, and invoices settled through the IATA clearing and settlement systems CASS, BSP and SIS-ICH |
| Public solution availability | Disposición adicional quinta: it must be available at least two months before the decree first applies |

No allowed page prints a calendar date for either stage, because the ministerial order has not come into force. Disposición final octava of Ley 18/2022 words its own clock as running from the approval of the implementing regulation, which happened in March 2026, but Real Decreto 238/2026 is the implementing regulation and its own disposición final cuarta re-bases the clock on the ministerial order. Do not compute a date from the law. Read the two rows above as intervals, not as dates. The earlier belief that the reform would start on a fixed day in 2027 or 2028 has no official source.

### Veri*factu vs Non-Veri*factu

Under Real Decreto 1007/2023 an invoicing system may work in one of two ways. Both are lawful. Veri*factu is not compulsory; it is the mode that buys the lighter requirements.

| Mode | What the regulation requires |
| --- | --- |
| Veri*factu (arts. 15 and 16) | The system sends every invoicing record it generates to the Agencia Tributaria continuously, securely, correctly, completely, automatically, consecutively, instantly and reliably. Such a system is presumed to meet the art. 8 requirements by design, and it does not have to sign the records electronically: computing the hash is enough. Choosing it is done simply by starting to send, and the choice then lasts at least until the end of the calendar year of the first send |
| Not Veri*factu | Records are kept in the issuing system with integrity, preservation, accessibility, legibility, traceability and inalterability guaranteed. These systems must additionally sign the records electronically and keep an event log, and must be able to export and transmit the records on request |
| The free form on the Sede | The application the tax administration may develop under art. 7.b is a Veri*factu system for every purpose |

Inside Real Decreto 1007/2023 both modes put a QR code on every invoice, full or simplified. A business inside the SII is outside that regulation and does not put one on at all. Only a system that actually sends all its records adds the words "Factura verificable en la sede electrónica de la AEAT" or "VERI*FACTU" (art. 6.5 of the invoicing regulation). The Agencia Tributaria describes the two modes and the two record types, the registro de facturación de alta and the registro de facturación de anulación, on its [general questions page](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/cuestiones-generales.html).

An invoicing record is not an invoice. The Agencia Tributaria says so in as many words: the records do not carry all the invoice data and are in no case electronic invoices. Paper invoicing stays lawful under these rules.

### B2B E-Invoicing (RD 238/2026)

| Requirement | Detail |
| --- | --- |
| Structured format | A structured message following the EN16931 semantic data model, in one of the syntaxes in art. 7.1: CII, UBL, an EDIFACT invoice message, or a Facturae message |
| Exchange channel | Art. 5: private exchange platforms meeting the decree's requirements, the public solution run by the Agencia Tributaria, or a combination |
| Default channel | Art. 6.1: where the parties have not expressly agreed a private platform, the public solution is taken to be the choice, with nothing to sign |
| Entry point | Art. 6.3: a business receiving through a private platform must publish its entry point in its communications and on its website. If it publishes none, its entry point is the public solution |
| Copy to the public solution | Art. 6.2: a business that does not issue through the public solution must send a faithful electronic copy of each invoice, in the UBL syntax, to the public solution at the same time as it issues |
| Signature | Art. 7.3: every electronic invoice issued through a private platform must carry an advanced electronic signature, by the issuer or by an authorised delegated signature |
| Unique code | Art. 7.5: every electronic invoice carries a unique code that must include the issuer's tax identification number, the invoice number and series, and the issue date |
| Invoice states | Art. 10.1: the recipient must tell the business that issued the invoice of its commercial acceptance or rejection with the date, and of full effective payment with its effective date |
| Optional states | Art. 10.2: partial acceptance or rejection, partial payment, and assignment of the invoice to a third party for collection |
| Payment reporting | Art. 12: full payment or rejection must be reported to the public solution, whichever channel was used, together with the payment due date. Art. 12.1: where the invoice is not rejected and no later credit note is issued, the invoice is presumed accepted. |
| Interoperability | Art. 7.2: private platform operators must be able to convert an invoice message between every accepted format while preserving authenticity of origin and integrity of content |
| Transitional paper-readable copy | Disposición transitoria segunda: for the first twelve months of the larger-turnover stage, electronic invoices must be accompanied by a legible copy in PDF format unless the recipient expressly agrees otherwise. That copy is not sent to the public solution |

Art. 2 bis of Ley 56/2007 adds three duties the decree does not repeat: platform interconnection and interoperability must be free, a recipient may ask the issuer for a copy of an electronic invoice for four years at no extra cost, and a recipient may not force the issuer onto a chosen platform or provider.

The state and payment reports are due in the same short window.

| Report | Deadline |
| --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295 |
| Invoice states (art. 10.3) | Within four calendar days from the date the state arises, excluding Saturdays, Sundays and national holidays |
| Full payment to the public solution (art. 12.3) | Within four calendar days from the effective payment date, excluding Saturdays, Sundays and national holidays |

The payment period itself is worked out under art. 4 of Ley 3/2004 on late payment in commercial transactions, not under the invoicing rules (art. 15). Where the invoice does not state the date of the operations, the payment period starts on the issue date.

## Section 3: Technical Format

### B2G: Facturae Format

| Parameter | Value |
| --- | --- |
| Format | Facturae, current version 3.2.2 (XML). The [format page](https://www.facturae.gob.es/formato/Paginas/version-3-2.aspx) publishes the 3.2.2 schema and the earlier 3.2 and 3.2.1 schemas |
| Who fixes the format | Art. 5.1 Ley 25/2013: the structured format is set by ministerial order |
| Signature | Art. 5.1 Ley 25/2013: an advanced electronic signature based on a recognised certificate, as in art. 10.1.a of the invoicing regulation |
| Alternative | Art. 5.2 Ley 25/2013: an advanced electronic seal based on a recognised certificate identifying the legal person by name and tax identification number |

The live Guide named XAdES-EPES as the signature profile. The signature policies are published on facturae.gob.es, but no allowed page read for this refresh names that profile in those words, so this Guide states only what Ley 25/2013 states. Check the signature policy page before configuring a signer.

### B2B: Accepted Formats (RD 238/2026)

| Format | Where it comes from |
| --- | --- |
| CII | Art. 7.1.a. The UN/CEFACT cross-industry invoice |
| UBL | Art. 7.1.b, with the adaptations needed for invoicing between businesses and professionals. Art. 11.2: users of the public solution must use the UBL syntax |
| EDIFACT invoice message | Art. 7.1.c |
| Facturae message | Art. 7.1.d |

Art. 2 ties UBL to the syntax list in Commission Implementing Decision (EU) 2017/1870. The Minister of Economy, Trade and Enterprise may add syntaxes by order (disposición final tercera.3). Private platforms must be able to transform between all accepted formats.

### Veri*factu Invoice Records

The registro de facturación de alta is defined in art. 10 of Real Decreto 1007/2023. Its fields, in the decree's order:

| Field | Description |
| --- | --- |
| Issuer | Tax identification number and full name or company name of the person obliged to issue the invoice |
| Recipient | Where the invoicing regulation requires it, the recipient's tax identification number and full name or company name |
| Who issued it | Whether the invoice was issued by the supplier, by the recipient or by a third party, with that party's details |
| Invoice number | The number and, where used, the series |
| Dates | The issue date, and the date of the operations or of an advance payment where it differs |
| Invoice type | The type of invoice |
| Base and tax | The taxable amount, the rate and the tax charged, as required by the record specification |
| Huella (hash) | A hash computed over parts of the immediately preceding invoicing record, chaining the records together |
| Signature | An electronic signature of the record, except in a Veri*factu system, where the hash alone is enough (art. 16.3) |

The technical layout of the records is in the annex to Orden HAC/1177/2024. This Guide does not reproduce it; read the order and the Agencia Tributaria's technical pages before building to it. The live Guide listed a fixed set of invoice type codes (F1, F2 and the R series) as if they came from the decree. They come from the technical specification, not from the decree, so check them there.

## Section 4: Mandatory Fields

### Full invoice particulars (art. 6 of the invoicing regulation)

Every invoice and every copy must carry the following ([Real Decreto 1619/2012](https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696), art. 6.1):

| Letter | Particular |
| --- | --- |
| a | Number and, where used, series. Numbering within each series must be consecutive. Separate series are compulsory for invoices issued by the recipient or a third party, for credit notes, and in the listed special cases |
| b | Date of issue |
| c | Full name or company name of both the issuer and the recipient |
| d | The issuer's tax identification number. The recipient's is compulsory for exempt intra-EU supplies under art. 25 of the VAT law, where the recipient is the taxable person, and where the operation is in Spanish VAT territory and the issuer is established there |
| e | Address of both the issuer and the recipient |
| f | Description of the operations, with everything needed to work out the taxable amount, including the unit price before tax and any discount not already in it |
| g | The rate or rates applied |
| h | The tax charged, shown separately |
| i | The date of the operations, or of an advance payment, where it is not the issue date |
| j | For an exempt operation, a reference to the Directive or to the Spanish provision, or a statement that the operation is exempt |
| k | For new means of transport, the characteristics, first use date and distance or hours run |
| l | "facturación por el destinatario" where the customer issues the invoice |
| m | "inversión del sujeto pasivo" where the customer is the taxable person |
| n to p | The special scheme wording for travel agencies, for second-hand goods, art, antiques and collectors' items, and for the cash accounting scheme |

Art. 6.2 requires the taxable amount to be split where an invoice mixes exempt and non-exempt operations, or reverse-charged and ordinary ones. Art. 6.5 adds the QR code, and the verifiable-invoice wording where the system sends all its records, but only for an invoice issued with a system covered by art. 7 of Real Decreto 1007/2023. A business inside the SII is outside that regulation by art. 3.3 and puts no QR code on its invoices at all.

### Simplified invoices

| Rule | What it says |
| --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696 |
| General limit (art. 4.1) | A simplified invoice may be used where the amount, VAT included, does not exceed EUR 400, or where a credit note must be issued |
| Sector limit (art. 4.2) | Up to EUR 3,000, VAT included, in the listed sectors: retail sales, itinerant or mobile sales and services, sales and services at the consumer's home, passenger transport and baggage, hospitality and restaurants, dance halls and discotheques, public telephone boxes and anonymous cards, hairdressing and beauty, use of sports facilities, photograph developing and photographic studios, vehicle parking, film rental, dry cleaning and laundry, and toll motorways |
| Never allowed (art. 4.4) | Intra-EU supplies under art. 25 of the VAT law, and the distance sales in art. 68.Tres.a of the VAT law outside the special scheme, among others |
| Content (art. 7.1) | Number and series, issue date, date of the operations where different, the issuer's tax identification number and name, the kind of goods or services, the rate applied and optionally "IVA incluido", the total consideration, the reference to the corrected invoice on a credit note, and the art. 6.1 letters j to p wording where relevant |
| Qualified simplified invoice (art. 7.2) | Where the customer is a business or professional and asks, the issuer must also state the customer's tax identification number and address and the tax charged separately. This is the only kind of simplified invoice that falls inside the business-to-business electronic invoice duty |

### FACe (B2G) Mandatory Fields

The following paths are the Facturae fields a public-sector invoice is built from. They are a working checklist carried over from the previous version of this Guide, not a list printed on an allowed page; the authority for the field set is the Facturae schema on facturae.gob.es.

| Facturae XML Path | Field | Required |
| --- | --- | --- |
| `FileHeader/SchemaVersion` | Schema version | Yes |
| `FileHeader/Modality` | Individual or batch | Yes |
| `Parties/SellerParty/TaxIdentification` | Seller tax identification number and name | Yes |
| `Parties/BuyerParty/TaxIdentification` | Buyer tax identification number and name | Yes |
| `Parties/BuyerParty/AdministrativeCentres` | Órgano Gestor, Unidad Tramitadora and Oficina Contable codes | Yes |
| `Invoices/Invoice/InvoiceHeader/InvoiceNumber` | Invoice number | Yes |
| `Invoices/Invoice/InvoiceHeader/InvoiceDocumentType` | Document type | Yes |
| `Invoices/Invoice/InvoiceIssueData/IssueDate` | Issue date | Yes |
| `Invoices/Invoice/InvoiceIssueData/TaxCurrencyCode` | Currency | Yes |
| `Invoices/Invoice/TaxesOutputs/Tax/TaxTypeCode` | Tax type | Yes |
| `Invoices/Invoice/TaxesOutputs/Tax/TaxRate` | Tax rate | Yes |
| `Invoices/Invoice/TaxesOutputs/Tax/TaxableBase/TotalAmount` | Taxable base | Yes |
| `Invoices/Invoice/TaxesOutputs/Tax/TaxAmount/TotalAmount` | Tax amount | Yes |
| `Invoices/Invoice/InvoiceTotals/TotalGrossAmount` | Gross total | Yes |
| `Invoices/Invoice/InvoiceTotals/TotalExecutableAmount` | Amount to pay | Yes |
| `Invoices/Invoice/PaymentDetails` | Payment terms | Yes |

Art. 9.1 Ley 25/2013 requires the invoice to identify the administrative bodies it is addressed to. That is where the three routing codes come from; the public body gives them to the supplier.

### B2B EN 16931 Mandatory Fields (Spanish CIUS)

Real Decreto 238/2026 does not publish a core invoice usage specification under that name. It requires the EN16931 semantic model in one of four syntaxes, and adds the Spanish content below on top of the invoicing regulation. Treat "Spanish CIUS" as a convenient label, not as a document you can download.

| Field | Description | Required |
| --- | --- | --- |
| Issuer tax identification number | Part of the unique invoice code in art. 7.5 | Yes |
| Invoice number and series | Part of the unique invoice code in art. 7.5 | Yes |
| Issue date | Part of the unique invoice code in art. 7.5 | Yes |
| Recipient tax identification number | Where art. 6.1.d of the invoicing regulation requires it | Conditional |
| Tax breakdown | Separate amounts per rate, as art. 6.1.g and 6.1.h require | Yes |
| Income tax withholding | Where the payer must withhold on a professional or other fee. The rates are in Section 7 | Conditional |

Art. 7.6 lets the parties agree extra content beyond the legal minimum, but only information the recipient sent to the issuer reliably before the date of the operation may be required on the invoice.

## Section 5: Transmission Method

### FACe (B2G)

| Method | Description |
| --- | --- |
| Punto general de entrada | Art. 6 Ley 25/2013. The State, the autonomous communities and local entities each have one. Local entities may use their provincial council's, their community's or the State's; communities may use the State's |
| FACe | The punto general de entrada of the Administración General del Estado, described on [facturae.gob.es](https://www.facturae.gob.es/face/Paginas/FACE.aspx) |
| What happens on entry | Art. 6.4: an accepted invoice produces an automatic entry in the electronic register of the administration running the entry point, with an electronic acknowledgement stating date and time |
| Routing | Art. 9.1: the entry point passes the invoice automatically to the accounting register of the oficina contable named on it |
| Status | Art. 6.3: the supplier can look up the state of processing |

The previous version of this Guide said Peppol was under development for FACe. No allowed page read for this refresh says that, so the claim is removed.

### SII (Real-Time Reporting)

| Parameter | Detail |
| --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925 |
| How | Art. 62.6: the VAT registers are kept through the Sede electrónica of the Agencia Tributaria by supplying the invoicing records electronically |
| Deadline, invoices issued | Art. 69 bis: four calendar days from issue, eight where the customer or a third party issues it, and in both cases before the 16th of the month after the tax point. Saturdays, Sundays and national holidays do not count in the four or eight days |
| Deadline, invoices received | Art. 69 bis: four calendar days from the accounting entry, and before the 16th of the month after the filing period the invoice is included in. Saturdays, Sundays and national holidays do not count in the four days |
| Registers covered | Art. 62.1: invoices issued, invoices received, capital goods, and certain intra-EU operations |
| Content | Invoicing records, not the invoice document |

These deadlines are the same as those in the `es-vat-return` Guide and come from the same articles.

### B2B E-Invoicing (SPFE + Private Platforms)

| Method | Description |
| --- | --- |
| Public solution | Art. 11 Real Decreto 238/2026: developed and run by the Agencia Tributaria, it also acts as the invoice repository, and it is free for users |
| Free form | Disposición adicional primera: the Agencia Tributaria will develop a free application or form for issuing electronic invoices, generating state information including full payment, and making that information available |
| Private platforms | Arts. 8, 9 and 13: they must interconnect, meet the requirements for operating in the Spanish system, and publish an open lookup showing which businesses have chosen them as entry point |
| Copy to the repository | Art. 6.2: a faithful electronic copy in the UBL syntax goes to the public solution at the same time as the invoice is issued, marked clearly as a copy |
| Reporting window | Four calendar days, as in the table in Section 2 |

Art. 14 governs who may see invoice and payment information. Disposición final cuarta.2 delays the platform interconnection duties in arts. 6, 8, 9 and 13 until twelve months after the ministerial order takes effect.

### Veri*factu Transmission

| Parameter | Detail |
| --- | --- |
| Where | The Sede electrónica of the Agencia Tributaria. Disposición final cuarta of Real Decreto 1007/2023 required the reception service to be available within nine months of the technical ministerial order taking effect |
| What | Every invoicing record the system generates, sent continuously, securely, correctly, completely, automatically, consecutively, instantly and reliably (art. 16.1) |
| Choosing the mode | Art. 16.5: a taxpayer is taken to have chosen a Veri*factu system simply by starting to send records systematically, and the choice runs at least to the end of the calendar year in which the first records were actually sent |
| Technical specification | Orden HAC/1177/2024 and the Agencia Tributaria's [technical pages](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu.html) |
| Declaration of conformity | Art. 13: the producer certifies conformity by a written declaración responsable, shown visibly in each version of the system and given to the customer and the reseller on purchase |

The previous version of this Guide named a transport protocol and an offline retry behaviour for this service. Neither is stated on an allowed page read for this refresh, so both are removed. Build to the order and the technical pages.

## Section 6: Validation Rules

### FACe Pre-Checks

| Check | Description |
| --- | --- |
| Schema validation | The invoice must validate against the Facturae schema published on facturae.gob.es |
| Electronic signature | Art. 5 Ley 25/2013: an advanced electronic signature or seal based on a recognised certificate |
| Administrative centre codes | Art. 9.1 Ley 25/2013: the administrative bodies the invoice is addressed to must be identified |
| Format | Art. 5.1 Ley 25/2013: the invoice must be in the structured format set by ministerial order |

The previous version listed a duplicate-detection rule keyed on issuer, number and date. No allowed page read for this refresh states it, so it is removed as a rule; the unique invoice code in art. 7.5 Real Decreto 238/2026 is built from exactly those three things, which is the nearest thing in force.

### SII Validation

| Check | Description |
| --- | --- |
| Deadline | The supply must be inside the window in the table in Section 5 |
| Registers complete | Art. 62.6 covers the registers in art. 62.1, so a partial supply does not discharge the duty |
| Consistency with the return | The Agencia Tributaria builds its draft VAT return from the records supplied, so the return and the records must agree |

### Veri*factu Validation

| Check | Description |
| --- | --- |
| Hash chain | Art. 10 and the Agencia Tributaria's description: each record's hash is computed over parts of the immediately preceding record |
| No gaps or silent changes | Art. 8.1: integrity, preservation, accessibility, legibility, traceability and inalterability, with no interpolations, omissions or alterations left unrecorded |
| Event log | Required for systems that are not Veri*factu |
| QR code | Art. 6.5 of the invoicing regulation: a QR code goes on invoices issued with a system covered by art. 7 of Real Decreto 1007/2023, full or simplified. A business inside the SII is outside that regulation by art. 3.3 and must not put the QR code on its invoices |
| Verifiable wording | Only where the system sends all its records |

### Common Rejection Reasons

| Issue | Resolution |
| --- | --- |
| Invalid or expired certificate | Renew the qualified electronic certificate |
| Wrong administrative centre codes | Get the Órgano Gestor, Unidad Tramitadora and Oficina Contable codes from the contracting public body |
| Missing signature on a public-sector invoice | Art. 5 Ley 25/2013 requires an advanced signature or seal |
| Broken hash chain | Regenerate the chain from the last valid record and keep the event log entry |
| Late supply to the SII | File inside the window; the fine is in Section 9 |
| No published entry point | Art. 6.3 Real Decreto 238/2026: the public solution becomes the entry point by default |

## Section 7: Tax Computation Rules

### IVA Rates (2026)

| Rate | Application |
| --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 |
| 21% | Standard rate, art. 90.Uno |
| 10% | Reduced rate, art. 91.Uno: food other than the super-reduced list, water, medical equipment, passenger transport, hotels and restaurants, new housing, qualifying home renovation |
| 4% | Super-reduced rate, art. 91.Dos: plain bread and bread dough, bread flour, milk, cheese, eggs, natural fruit, vegetables, pulses, tubers and cereals, olive oil, books, newspapers and magazines, medicines for human use, certain disability aids and social housing |

No temporary rate is in force for 2026. The emergency food and electricity rates have ended, and the previous version's zero rate row is removed. Olive oil sits permanently in the super-reduced list from 1 January 2025. The rate to use is the one in force at the tax point, not at invoicing.

### IRPF Withholding (Retención)

Professional fee invoices normally carry an income tax withholding. The payer withholds and pays it over on modelo 111; the professional credits it in the annual return.

| Scenario | Rate |
| --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Professional fees, general (art. 95.1) | 15% |
| A professional starting an activity (art. 95.1) | 7% |

The reduced rate runs for the tax year in which the activity starts and the two following years, and only if no professional activity was carried on in the year before the start date. The professional must tell the payer in writing and the payer must keep the signed notice.

The invoice must show the amount before tax, the VAT, the withholding and the net payable separately. Withholding is not VAT and does not change the taxable amount.

### Rounding

- **Tax per line.** Taxable amount multiplied by the rate, divided by one hundred, rounded to two decimal places.
- **Invoice total.** Sum of taxable amounts, plus the sum of VAT amounts, less the sum of withholdings.
- **Consistency.** The invoicing record and the VAT return must be arithmetically consistent with the invoice.

No allowed page read for this refresh prints a rounding rule for an invoice line. The rounding behaviour required of a compliant system is in the technical specification, Orden HAC/1177/2024. Treat the three lines above as a working convention, not as a cited rule.

### Multi-Rate Invoice Handling

- **Separate block per rate.** Art. 6.1.g of the invoicing regulation requires each rate applied to be stated, and art. 6.2 requires the taxable amount to be split where exempt and non-exempt operations, or reverse-charged and ordinary operations, appear on one invoice.
- **Exempt operations.** Art. 6.1.j: give a reference to the Directive or to the Spanish provision, or state that the operation is exempt.
- **Reverse charge.** Art. 6.1.m: the invoice must carry the words "inversión del sujeto pasivo".
- **Simplified invoices.** Art. 7.1.f: where one simplified invoice covers operations at different rates, the taxable amount for each must be shown separately.

### Equivalence Surcharge (Recargo de Equivalencia)

A retailer inside this scheme is charged the surcharge by its supplier on top of VAT, files no VAT return on those sales and deducts no input VAT. The surcharge is shown separately on the supplier's invoice.

| VAT Rate | Surcharge |
| --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 |
| 21% | 5.2% |
| 10% | 1.4% |
| 4% | 0.5% |

Art. 3.1.b of the invoicing regulation excuses a retailer in this scheme from issuing invoices for its own sales, except that an invoice must always be issued for a taxable and non-exempt supply of immovable property.

## Section 8: Archiving Requirements

| Requirement | Detail |
| --- | --- |
| What must be kept (art. 19.1 of the invoicing regulation) | Invoices received; copies or matrices of invoices issued; the accounting vouchers in art. 97.Uno.4 of the VAT law; the receipts in art. 16.1; and the import documents in art. 97.Uno.3 |
| How long, tax | Art. 19.1 sets the period as the one in Ley 58/2003. Art. 66 of that law sets the limitation period at four years |
| How long, commercial | Art. 30.1 of the Código de Comercio: six years from the last entry in the books, unless another rule says otherwise ([Código de Comercio](https://www.boe.es/buscar/act.php?id=BOE-A-1885-6627)) |
| Capital goods | The VAT deduction on capital goods is regularised over the four calendar years after acquisition, or the nine years after it for land and buildings (art. 107 of the VAT law). Keep the invoices while that runs |
| Condition | Art. 19.2: documents are kept with their original content, in order, and within the periods and conditions the regulation sets |
| Who may do it | Art. 19.3: a third party may keep them, acting in the name and for the account of the business, which stays responsible |
| Invoicing records | Art. 8.1 Real Decreto 1007/2023: integrity, preservation, accessibility, legibility, traceability and inalterability, with the hash chain intact |
| Public repository | Art. 11.1 Real Decreto 238/2026: the public solution acts as the repository for electronic invoices. This does not replace the taxpayer's own retention duty |
| Audit access | Art. 14 Real Decreto 1007/2023 and art. 29.2.f of Ley 58/2003: the records and files must be produced to the tax administration on request |

## Section 9: Penalties for Non-Compliance

All the amounts below are in Ley 58/2003 unless the row says otherwise. Two of them are printed in the statute as words, not digits, and are written here as words for that reason.

| Violation | Penalty |
| --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186 |
| Breach of the invoicing requirements, art. 201.2.a | A proportional fine of one per cent of the total of the operations that gave rise to the breach |
| Failure to issue or to keep invoices, art. 201.2.b | A proportional fine of two per cent of the total of those operations. Where the amount cannot be known, EUR 300 for each operation with no invoice issued or kept |
| Invoices with false or falsified data, art. 201.3 | A proportional fine of 75% of the total of those operations |
| Graduation, art. 201.5 | The resulting amount is increased by 100% where the breach is substantial |
| Late supply of the invoicing records to the Sede electrónica, art. 200.3 | A proportional fine of 0.5% of the invoice in the record, with a quarterly minimum of EUR 300 and a maximum of EUR 6,000 |
| Other breaches of the accounting and register duties, art. 200.3 | A fixed fine of EUR 150, unless one of the specific rules in that paragraph applies |
| Making or selling non-compliant invoicing software, art. 201 bis.1 and 4 | A fixed fine of EUR 150,000 for each financial year in which sales occurred and for each distinct type of system or program involved |
| Selling a system without the certificate, art. 201 bis.1.f and 4 | A fixed fine of EUR 1,000 for each system or program sold without it |
| Holding an uncertified or altered system, art. 201 bis.2 and 4 | A fixed fine of EUR 50,000 for each financial year. Someone already fined under art. 201 bis.1 is not fined again under this paragraph |
| Source | figure below | https://www.boe.es/buscar/act.php?id=BOE-A-2022-15818 |
| A business that must offer electronic invoices to its customers and does not, or that blocks former customers from reaching their invoices (art. 2 bis.9 Ley 56/2007, as amended by Ley 18/2022) | A warning, or a fine of up to EUR 10,000, imposed by the Secretaría de Estado de Digitalización e Inteligencia Artificial |

The last row is narrower than it looks. It sits in the consumer-facing part of Ley 56/2007 and catches businesses supplying the public in sectors of special economic importance. Real Decreto 238/2026 sets no fine of its own, and Ley 18/2022 sets no separate fine for failing to issue a business-to-business electronic invoice. Until the mandate starts, the general art. 201 fines are the ones that apply to an invoicing failure.

The previous version of this Guide carried a row for failing to report a payment status under Real Decreto 238/2026 with "amounts pending ministerial order". The decree provides no such fine, so the row is removed.

## Section 10: Interaction with Other Tax Guides

### VAT (IVA) Return Integration

- **Inside the SII.** The registers are kept by supplying the invoicing records through the Sede electrónica (art. 62.6 of the VAT Regulation). The Agencia Tributaria builds its draft return from them, so the modelo 303 and the records must agree. See `es-vat-return`.
- **Under the invoicing software rules.** A business inside the SII is outside Real Decreto 1007/2023 (art. 3.3). A business outside the SII will, from its 2027 date, be producing invoicing records in its software instead.
- **Business to business.** Once the mandate starts, a faithful copy of each electronic invoice reaches the public solution (art. 6.2 Real Decreto 238/2026). No allowed page says the public solution will pre-fill a VAT return, so do not promise that.

### Income Tax Integration

- Self-employed professionals: the invoice data, including the withholding, feeds the annual income tax return and the quarterly modelo 130 where that applies.
- Companies: the corporate income tax return is reconciled against the same invoice records.

### Withholding Tax Reporting

- Withholdings shown on invoices must reconcile with the quarterly modelo 111 and the annual modelo 190.
- The registro de facturación de alta records the tax charged; the withholding is a separate reporting stream on those two forms.

### Intra-EU and Cross-Border

- Intra-EU supplies and services are reported on modelo 349.
- The SII captures intra-EU operations in the registers in art. 62.1 of the VAT Regulation.
- The business-to-business electronic invoice duty reaches only operations whose customer has its seat, permanent establishment or habitual residence in Spain (art. 3.1 Real Decreto 238/2026). A sale to a customer established abroad is outside it.

## The method, step by step

1. **Fix which systems the client is in.** Check the VAT period first: if it is the calendar month, the client is inside the SII under art. 62.6 of the [VAT Regulation](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925), and therefore outside the invoicing software rules by art. 3.3 of [Real Decreto 1007/2023](https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840). Then check whether the client invoices public bodies, which brings in [Ley 25/2013](https://www.boe.es/buscar/act.php?id=BOE-A-2013-13722).
2. **Date the software duty.** For a client outside the SII, the deadline is before 1 January 2027 if it files corporate income tax, and before 1 July 2027 otherwise, per the Agencia Tributaria's [note on the extended deadlines](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/nota-informativa-ampliacion-plazo-adaptacion-facturacion.html). Choose the Veri*factu mode or the other mode, and get the supplier's declaración responsable (art. 13).
3. **Do not date the business-to-business mandate.** Read disposición final cuarta of [Real Decreto 238/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295): the clock starts when the ministerial order in disposición final tercera comes into force, and runs twelve months for larger turnover and twenty-four for everyone else. Tell the client the interval and that no start date has been published. Check whether the order has appeared before repeating this.
4. **Fix the invoice content.** Work through art. 6 of the [invoicing regulation](https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696) for a full invoice, or arts. 4 and 7 for a simplified one, and, only if the client is inside Real Decreto 1007/2023, add the QR code required by art. 6.5. Issue by the deadline in art. 11: at the time of the operation, or, where the customer is a business, before the 16th of the month after the tax point.
5. **Set the withholding.** Apply the professional rates in art. 95.1 of the [income tax regulation](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820) and show the withholding as its own line, as set out in Section 7.
6. **For a public body, route it.** Get the Órgano Gestor, Unidad Tramitadora and Oficina Contable codes from the contracting body, build the Facturae file to the current schema on [facturae.gob.es](https://www.facturae.gob.es/formato/Paginas/version-3-2.aspx), sign it as art. 5 Ley 25/2013 requires, and file it through the right punto general de entrada.

## Ask the client first

- Is your VAT period the calendar month, or are you in the registro de devolución mensual? That decides whether you are in the SII, and being in the SII takes you out of the invoicing software rules.
- Do you file corporate income tax, or income tax on an economic activity? That decides whether your software deadline is 1 January 2027 or 1 July 2027.
- Do you invoice public bodies, and if so which ones? Their entry point and their three routing codes are not interchangeable.
- What was your volumen de operaciones last year, measured under art. 121 of the VAT law? It decides which of the two business-to-business stages you fall into when the clock starts.
- Do you issue simplified invoices, and does any customer ask for the extra content that makes one qualified? A plain simplified invoice is outside the business-to-business duty; a qualified one is not.
- Are you established in the Basque provinces or Navarre? Their invoicing software rules are their own and are not in this Guide.

## When to refuse or refer

- Any Basque provincial or Navarre invoicing system, including TicketBAI. This Guide covers state rules only.
- The Canary Islands general indirect tax and the Ceuta and Melilla local taxes. The VAT rates here do not apply there.
- Setting a start date for the business-to-business mandate. Until the ministerial order is published, there is none to give.
- Certifying that a particular software product complies. The producer signs the declaración responsable, not the accountant.
- Building to the record layout or the QR content. Those are in Orden HAC/1177/2024 and the Agencia Tributaria technical pages, which this Guide does not reproduce.
- Advising whether a late or wrongly routed invoice is still deductible. That is a VAT question and turns on the facts.
- Anything about the derogation Spain needs from arts. 218 and 232 of the VAT Directive. Its state is not on an allowed page.

## Sources

- [Ley 25/2013, factura electrónica en el sector público](https://www.boe.es/buscar/act.php?id=BOE-A-2013-13722)
- [Ley 18/2022, de creación y crecimiento de empresas](https://www.boe.es/buscar/act.php?id=BOE-A-2022-15818)
- [Real Decreto 238/2026, facturación electrónica obligatoria entre empresarios y profesionales](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295)
- [Real Decreto 1007/2023, sistemas informáticos de facturación](https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840)
- [Real Decreto 1619/2012, obligaciones de facturación](https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696)
- [Real Decreto 1624/1992, Reglamento del IVA](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925)
- [Ley 37/1992, del Impuesto sobre el Valor Añadido](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740)
- [Real Decreto 439/2007, Reglamento del IRPF](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820)
- [Ley 58/2003, General Tributaria](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186)
- [Código de Comercio](https://www.boe.es/buscar/act.php?id=BOE-A-1885-6627)
- [Agencia Tributaria: sistemas informáticos de facturación y Veri*factu](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu.html)
- [Agencia Tributaria: cuestiones generales](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/cuestiones-generales.html)
- [Agencia Tributaria: nota informativa sobre los nuevos plazos](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/nota-informativa-ampliacion-plazo-adaptacion-facturacion.html)
- [Agencia Tributaria: preguntas frecuentes sobre el ámbito de aplicación](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes/cuestiones-generales-ambitos-aplicacion.html)
- [Agencia Tributaria: novedades de normativa, Real Decreto 238/2026](https://sede.agenciatributaria.gob.es/Sede/iva/novedades-iva/novedades-normativa-2026/real-decreto-238-2026-25-marzo.html)
- [Formato Facturae, últimas versiones](https://www.facturae.gob.es/formato/Paginas/version-3-2.aspx)
- [FACe, punto general de entrada](https://www.facturae.gob.es/face/Paginas/FACE.aspx)

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal, gestor administrativo, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

> Contributed by OpenAccountants.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
