---
name: italy-einvoice
description: Use this skill whenever asked about Italian e-invoicing, FatturaPA, Sistema di Interscambio (SDI), electronic invoicing compliance in Italy, Codice Destinatario, PEC invoicing, fattura elettronica, TD document types, cross-border e-invoicing via SDI, conservazione sostitutiva, or any question about issuing, receiving, validating, or archiving electronic invoices in Italy. Also trigger when preparing or reviewing XML invoices for SDI submission, handling SDI rejection (scarto) errors, configuring Codice Destinatario or PEC routing, or advising on FatturaPA technical format compliance. This skill covers the FatturaPA XML schema, SDI transmission channels, mandatory fields, validation rules, archiving, penalties, and interaction with Italian VAT returns. ALWAYS read this skill before touching any Italian e-invoicing work.
version: 2.0
jurisdiction: IT
tax_year: 2026
last_updated: 2026-11-14
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - einvoice-workflow-base
category: invoicing
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: e-invoicing
type: filing-howto
---

# E-invoicing in Italy (fattura elettronica, FatturaPA and the SdI)

Who in Italy must issue e-invoices through the Sistema di Interscambio (SdI) and from when, the FatturaPA XML file, routing (codice destinatario or PEC), deadlines, stamp duty (imposta di bollo), cross-border data (the old esterometro), storage and penalties. For Italian VAT-registered businesses, forfettari included. Figures are for tax year 2026. Sources: the Agenzia's technical specifications 1.9.1 (31 March 2026, usable from 15 May 2026), its e-invoice guide (December 2025) and compilation guide 1.10 (April 2025); stamp duty from its guide updated June 2026; statutes on Normattiva as in force on 30 June 2026.

## Scope

This skill is the how-to for issuing, receiving and storing Italian e-invoices in tax year 2026: who must use the Sistema di Interscambio (SdI) and from when, the FatturaPA XML file and its codes, routing by codice destinatario or PEC, the issue deadlines, stamp duty (imposta di bollo) on invoices without VAT, cross-border reporting (the old esterometro), storage and penalties.

Who is in: businesses and professionals resident or established in Italy and registered for VAT, forfettari and minimi included. Who is out: invoices to public administrations beyond the basics (CIG, CUP, NSO), health services to individuals that go to the Sistema tessera sanitaria, and VAT groups, fiscal representatives and VAT warehouses. Whether an operation is taxable at all, and VAT settlement, are in `italy-vat-return`.

### Quick reference

**Quick Reference**

| Field | Value | Source |
| --- | --- |---|
| E-invoicing system | Sistema di Interscambio (SdI), run by the Agenzia delle Entrate (art. 1(2) D.Lgs. 127/2015) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2015-08-05;127~art1!vig=2026-06-30 |
| Invoice format | FatturaPA XML (ordinary schema 1.2.3, simplified 1.0.2) | https://www.agenziaentrate.gov.it/portale/documents/d/guest/allegato-a-specifiche-tecniche-vers-1-9-1 |
| Key legislation | D.Lgs. 127/2015 art. 1; D.P.R. 633/1972 art. 21; D.L. 36/2022 art. 18; D.Lgs. 471/1997 arts. 6 and 11; Provvedimento 433608/2022 (private parties); D.M. 55/2013 (public administrations) | https://www.agenziaentrate.gov.it/portale/documents/d/guest/la_fattura_elettronica |
| Portal | "Fatture e Corrispettivi", in the Agenzia's reserved area | same |
| Current spec version | 1.9.1, usable from 15 May 2026 (version 1.9 was usable from 1 April 2025) | https://www.agenziaentrate.gov.it/portale/fatturazione-elettronica-e-dati-fatture-transfrontaliere-new |
| B2G mandatory since | 31 March 2015 for all public administrations | https://www.agenziaentrate.gov.it/portale/documents/d/guest/la_fattura_elettronica |
| B2B/B2C mandatory since | 1 January 2019 | same |
| Current status | In force for VAT persons resident or established in Italy, forfettari included (exceptions in section "Mandate Scope") | https://www.agenziaentrate.gov.it/portale/fattura-elettronica-per-i-forfettari |

## Ask the client first

- Is the customer an Italian business, a consumer, a public administration or foreign? Routing and reporting depend on it.
- Are you a forfettario, and was your prior-year revenue above the limit in the section "Mandate Scope" table? That sets when your duty began.
- Do you provide health services to individuals, or send data to the Sistema tessera sanitaria? Those invoices must not go through the SdI.
- Do your invoices include exempt, non-taxable or out-of-scope lines? Stamp duty may be due.
- Do goods travel with a transport document (DDT)? A deferred invoice may be possible.
- Did a supplier fail to invoice you, or send a wrong invoice? You have ninety days to report it by TD29.

## The method, step by step

1. **Check the SdI duty.** Both parties resident or established in Italy: yes (art. 1(3) D.Lgs. 127/2015). Forfettari, minimi and L. 398/1991 associations are in (art. 18 D.L. 36/2022). Health services to natural persons are out (art. 10-bis D.L. 119/2018). Foreign counterparty: go to step 6.
2. **Fix the deadline.** Immediate invoice within twelve days of the operation; deferred invoice (TD24) by the 15th of the next month (art. 21 D.P.R. 633/1972, section "Transmission Method" table).
3. **Build the XML.** Take document type, regime and nature sub-codes from the technical specifications 1.9.1 (Sources). Check the totals against the tolerances in section "Tax Computation Rules".
4. **Route it.** Buyer's 7-character code, or `0000000` with or without PEC (section "Transmission Method").
5. **Apply stamp duty.** If the invoice carries non-VAT lines (N2.1, N2.2, N3.5, N3.6, N4) above the limit in the stamp duty table, set `BolloVirtuale` to SI and pay by quarter (section "Tax Computation Rules").
6. **Report cross-border operations.** Sales: `XXXXXXX` invoice within the issue deadline. Purchases: TD17, TD18, TD19 or TD28 by the fifteenth day of the following month (art. 1(3-bis) D.Lgs. 127/2015).
7. **Watch the receipt.** RC or MC: issued. NS: correct and re-send. Store the file (section "Archiving Requirements", free storage service).

### Rates, bands and thresholds

| Item | Figure | Tax year | Source |
| --- | --- | --- | --- |
| Immediate invoice: send to the SdI within | 12 days of the operation | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art21!vig=2026-06-30 |
| Deferred invoice (TD24, goods with a DDT or services identified by documents): send by | the 15th of the following month | 2026 | same |
| Simplified invoice (TD07): maximum total | EUR 400 (no limit for forfettari and RF20) | 2026 | https://www.agenziaentrate.gov.it/portale/documents/d/guest/allegato-a-specifiche-tecniche-vers-1-9-1 |
| Stamp duty on an invoice with non-VAT lines | EUR 2 per invoice | 2026 | https://www.agenziaentrate.gov.it/portale/fattura-elettronica-per-i-forfettari |
| Stamp duty is due when the invoice's non-VAT amounts are above | EUR 77.47 | 2026 | https://www.agenziaentrate.gov.it/portale/documents/d/guest/l-imposta_di_bollo_sulle_fatture_elettronichegiugno2026 |
| Stamp duty, small amounts: Q1 paid by 30 September (Q1 and Q2 together by 30 November) if not above | EUR 5,000 | 2026 | same |
| Forfettari, minimi and L. 398/1991 associations: in the SdI from 1 July 2022 if prior-year revenue was above (all others from 1 January 2024) | EUR 25,000 | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2022-04-30;36~art18!vig=2026-06-30 |
| Cross-border purchases not territorially relevant in Italy, not reported if each is not above | EUR 5,000 | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2015-08-05;127~art1!vig=2026-06-30 |
| Taxable operation not invoiced or late (art. 6(1)) | Seventy per cent of the VAT (as art. 6 words it); EUR 250 to EUR 2,000 if the settlement was not affected | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art6!vig=2026-06-30 |
| Non-taxable, exempt or reverse-charge operation not invoiced (art. 6(2)) | 5% of the consideration | 2026 | same |
| Cross-border data omitted or wrong (art. 11(2-quater)) | EUR 2 per invoice, up to EUR 400 a month (EUR 200 if corrected within 15 days) | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art11!vig=2026-06-30 |

VAT rates are owned by `italy-vat-return`; the rates printed in "Tax Computation Rules" below are only the codes the XML carries.

### Mandate Scope

#### Who Must Comply

**Who Must Comply**

| Scope | Requirement | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2022-04-30;36~art18!vig=2026-06-30 |
| B2G | Mandatory, under D.M. 55/2013, format FPA12 | |
| B2B | Mandatory between parties resident or established in Italy since 1 January 2019 (art. 1(3) D.Lgs. 127/2015) | |
| B2C | Mandatory since 2019; consumer views it in the Agenzia's services, and the seller's copy may be refused | |
| Forfettari, minimi and associations under L. 398/1991 | From 1 July 2022 if 2021 revenue or fees, annualised, were above EUR 25,000; from 1 January 2024 for the rest | "superiori a euro 25.000" |
| Non-resident businesses | Not obliged when only identified for VAT in Italy (direct identification or fiscal representative); the duty covers parties resident or established in Italy. An Italian buyer from such a supplier still sends TD17 or TD19 | Spec 1.9.1, citing risoluzione 89/E of 25 August 2010 |
| Cross-border | E-invoicing optional; data go to the SdI (section "Transmission Method") | |

#### Exemptions

- Health services: operators who send data to the Sistema tessera sanitaria may not e-invoice through the SdI for those invoices, and the ban extends to other operators for health services to natural persons. The text in force on 30 June 2026 has no end year (the year limit, last set at 2025, was removed in June 2025) ([art. 10-bis D.L. 119/2018](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2018-10-23;119~art10bis!vig=2026-06-30)).
- People exempt from invoicing altogether, such as "piccoli produttori agricoli" (art. 34(6) D.P.R. 633/1972), and those excused under art. 36-bis D.P.R. 633/1972 for exempt operations ([Agenzia e-invoice guide](https://www.agenziaentrate.gov.it/portale/documents/d/guest/la_fattura_elettronica)).
- Invoices to or from foreign parties: e-invoicing optional, data reported instead (section "Transmission Method"). San Marino has its own rules (TD28).

#### Timeline Summary

**Timeline Summary**

| Date | Milestone |
| --- | --- |
| 31 March 2015 | B2G mandate for all public administrations |
| 1 January 2019 | B2B and B2C mandate, forfettari still exempt |
| 1 July 2022 | Esterometro moves into the SdI; larger forfettari and minimi brought into scope |
| 1 January 2024 | All remaining forfettari and minimi brought into scope |
| 1 April 2025 | Specifications 1.9 usable (TD29, RF20) |
| 15 May 2026 | Specifications 1.9.1 usable (new check 00327) |

### Technical Format

#### Format Specification

**Format Specification**

| Parameter | Value | Source |
| --- | --- |---|
| Root element | `FatturaElettronica` (ordinary) or `FatturaElettronicaSemplificata` (simplified) | https://www.agenziaentrate.gov.it/portale/documents/d/guest/allegato-a-specifiche-tecniche-vers-1-9-1 |
| Versioning attribute | `versione="FPR12"` (to private parties) or `versione="FPA12"` (to a public administration); simplified invoice `FSM10` | same |
| Encoding | UTF-8 | same |
| Max file size | 5MB per file (one invoice or a batch) | same |
| Namespace | `http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.2` (ordinary) |  |
| File name | Country code, sender's fiscal ID, underscore, unique progressive of up to 5 characters: `IT01234567890_00001.xml` | same |
| Signature | Optional: CAdES or XAdES Baseline B (qualified certificate), or CAdES with the Agenzia's certificate | same |

#### XML Structure

Three top-level parts, in this order (schema VFPR12):

1. **FatturaElettronicaHeader** (one): `DatiTrasmissione`, `CedentePrestatore` (seller), `RappresentanteFiscale` (optional), `CessionarioCommittente` (buyer), `TerzoIntermediarioOSoggettoEmittente` (optional).
2. **FatturaElettronicaBody** (repeatable for batches): `DatiGenerali`, `DatiBeniServizi` (lines and VAT summary), then optional `DatiVeicoli`, `DatiPagamento`, `Allegati`.
3. **ds:Signature** (optional).

#### Document Types (TipoDocumento)

**Document Types (TipoDocumento)**, field 2.1.1.1, as listed in specifications 1.9.1:

| Code | Description |
| --- | --- |
| TD01 | Invoice (Fattura) |
| TD02 | Advance or down payment on an invoice |
| TD03 | Advance or down payment on a fee note (parcella) |
| TD04 | Credit note |
| TD05 | Debit note |
| TD06 | Fee note (parcella) |
| TD07, TD08, TD09 | Simplified invoice, credit note, debit note (simplified schema only) |
| TD16 | Integration of an invoice under domestic reverse charge |
| TD17 | Integration or self-invoice, services from abroad |
| TD18 | Integration, intra-EU goods purchases |
| TD19 | Integration or self-invoice, goods under art. 17(2) D.P.R. 633/72 |
| TD20 | Self-invoice to regularise or integrate invoices |
| TD21 | Self-invoice for exceeding the plafond (splafonamento) |
| TD22 | Goods taken out of a VAT warehouse |
| TD23 | Goods taken out of a VAT warehouse, VAT paid |
| TD24 | Deferred invoice, art. 21(4)(a) D.P.R. 633/72 |
| TD25 | Deferred invoice, art. 21(4)(b) (goods sold to a third party via own supplier) |
| TD26 | Depreciable-asset sales and internal transfers (art. 36 D.P.R. 633/72) |
| TD27 | Self-consumption or free supplies without recharge |
| TD28 | Purchases from San Marino with VAT (paper invoice) |
| TD29 | Buyer's report of omitted or irregular invoicing (art. 6(8) D.Lgs. 471/97) |

The simplified invoice may not exceed the section "Tax Computation Rules" limit, except for a forfettario or the EU cross-border franchise (RF20).

#### Nature codes (Natura)

Required with a zero VAT rate (fields 2.2.1.14 and 2.2.2.2). Bare N2, N3 and N6 are no longer valid.

| Code | Meaning (official wording, shortened) |
| --- | --- |
| N1 | Excluded under art. 15 D.P.R. 633/72 |
| N2.1 | Not subject to VAT under arts. 7 to 7-septies D.P.R. 633/72 |
| N2.2 | Not subject, other cases (used by forfettari) |
| N3.1 to N3.6 | Non-taxable: exports (3.1); intra-EU supplies (3.2); San Marino supplies (3.3); export-assimilated ops (3.4); after a declaration of intent (3.5); other ops not counted in the plafond (3.6) |
| N4 | Exempt |
| N5 | Margin scheme, VAT not shown on the invoice |
| N6.1 to N6.9 | Reverse charge: scrap (6.1); gold and silver (6.2); construction subcontracting (6.3); buildings (6.4); mobile phones (6.5); electronics (6.6); construction and related services (6.7); energy (6.8); other (6.9) |
| N7 | VAT paid in another EU state (telecoms, broadcasting, electronic services) |

#### Tax regime codes (RegimeFiscale)

RF01 ordinary; RF02 contribuenti minimi; RF04 to RF18 special regimes (agriculture, travel agencies, second-hand goods, VAT for cash, others); RF19 forfettario; RF20 EU cross-border VAT franchise (Directive 2020/285); no RF03.

### Mandatory Fields

#### Header Fields (FatturaElettronicaHeader)

**Header Fields (FatturaElettronicaHeader)**

| XML Path | Field | Required |
| --- | --- | --- |
| `DatiTrasmissione/IdTrasmittente/IdPaese`, `IdCodice` (1.1.1.2) | Sender country and tax ID | Yes |
| `DatiTrasmissione/ProgressivoInvio` | Sender's own file progressive | Yes |
| `DatiTrasmissione/FormatoTrasmissione` (1.1.3) | FPR12 (private) or FPA12 (public administration) | Yes |
| `DatiTrasmissione/CodiceDestinatario` (1.1.4) | Routing code: 7 characters with FPR12, 6 with FPA12 | Yes |
| `DatiTrasmissione/PECDestinatario` (1.1.6) | Buyer's PEC address, used only with code `0000000` | No |
| `CedentePrestatore/DatiAnagrafici/IdFiscaleIVA` (1.2.1.1) | Seller VAT number | Yes |
| `CedentePrestatore/DatiAnagrafici/RegimeFiscale` | Tax regime code (RF01 to RF20) | Yes |
| `CedentePrestatore/Sede`, `CessionarioCommittente/Sede` | Seller and buyer addresses | Yes |
| `CessionarioCommittente/DatiAnagrafici` (1.4.1) | Buyer VAT number (1.4.1.1) or codice fiscale (1.4.1.2) | Yes |

#### Body Fields (FatturaElettronicaBody)

**Body Fields (FatturaElettronicaBody)**. `DGD` stands for `DatiGenerali/DatiGeneraliDocumento`; `DettaglioLinee` and `DatiRiepilogo` sit under `DatiBeniServizi`.

| XML Path | Field | Required |
| --- | --- | --- |
| `DGD/TipoDocumento` (2.1.1.1) | Document type (TD01 and so on) | Yes |
| `DGD/Divisa` | Currency (ISO standard 4217, alpha-3) | Yes |
| `DGD/Data` (2.1.1.3) | Invoice date (YYYY-MM-DD) | Yes |
| `DGD/Numero` (2.1.1.4) | Invoice number, up to 20 characters | Yes |
| `DGD/DatiRitenuta` (2.1.1.5) | Withholding (RT01 to RT06) | If a line is subject to withholding |
| `DGD/DatiBollo/BolloVirtuale` | "SI" when stamp duty is due (section "Tax Computation Rules") | When stamp duty applies |
| `DettaglioLinee/NumeroLinea`, `Descrizione`, `PrezzoUnitario` | Line number, description, unit price | Yes |
| `DettaglioLinee/PrezzoTotale` (2.2.1.11) | Line total | Yes |
| `DettaglioLinee/AliquotaIVA` (2.2.1.12) | VAT rate, written as a percentage (10.00, not 0.10) | Yes |
| `DettaglioLinee/Natura` (2.2.1.14) | Nature code | Only when the rate is zero |
| `DatiRiepilogo/AliquotaIVA` (2.2.2.1) | Summary VAT rate | Yes |
| `DatiRiepilogo/ImponibileImporto` (2.2.2.5) | Taxable amount per rate | Yes |
| `DatiRiepilogo/Imposta` (2.2.2.6) | VAT amount per rate | Yes |
| `DatiRiepilogo/EsigibilitaIVA` (2.2.2.7) | I immediate, D deferred, S split payment | No (optional in the schema) |
| `DatiPagamento/CondizioniPagamento`, `DettaglioPagamento/ModalitaPagamento`, `ImportoPagamento` | Payment terms, method, amount | If block used |

### Transmission Method

#### SDI Channels

**SDI Channels**

| Channel | Description | Use Case |
| --- | --- | --- |
| SdICoop | Web service over HTTPS, accredited channel | High-volume automated flows |
| SdIFtp | SFTP, accredited channel | Large batches |
| PEC | Posta Elettronica Certificata | Low volume |
| "Fatture e Corrispettivi" | Agenzia portal, free | Manual submission |

#### Routing

- **CodiceDestinatario**: a 7-character code the SdI gives to a subject with an accredited receiving channel (B2B).
- **`0000000`**: buyer receives by PEC (put it in `PECDestinatario`), channel unknown, or consumer.
- **`XXXXXXX`**: invoices to parties not established in Italy, sent to report cross-border data; buyer `IdPaese` not IT (error 00313).
- **B2G**: 6-character office code (IPA), format FPA12.
- `PECDestinatario` is used only if no channel is registered for the buyer's VAT number.
- **Delivery failure.** The SdI sends a receipt of impossible delivery and places the invoice in the buyer's reserved area: issued for the seller, received by the buyer only when viewed. Tell the buyer.

#### Submission Deadlines

**Submission Deadlines**

| Invoice Type | Deadline | Rule |
| --- | --- | --- |
| Immediate invoice | Within twelve days of the operation ("entro dodici giorni dall'effettuazione dell'operazione") | [art. 21(4) D.P.R. 633/1972](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art21!vig=2026-06-30) |
| Deferred invoice (TD24) | By the 15th of the next month, for goods with a transport document or documented services to the same customer in the same calendar month | art. 21(4)(a) |
| Deferred invoice (TD25) | By the end of the month after delivery or dispatch | art. 21(4)(b) |
| Services to EU taxable persons (art. 7-ter, not subject); or under art. 6, sixth paragraph, to or from a taxable person established outside the EU | By the 15th of the month after the operation | art. 21(4)(c) and (d) |
| Cross-border data, sales to non-established parties | Within the time limits for issuing the invoice | [art. 1(3-bis) D.Lgs. 127/2015](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2015-08-05;127~art1!vig=2026-06-30) |
| Cross-border data, purchases (TD17 to TD19) | By the fifteenth day of the month after receipt of the document or the operation | art. 1(3-bis)(b) |

#### Cross-border reporting (former esterometro)

| Item | Rule | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2015-08-05;127~art1!vig=2026-06-30 |
| What | Sales to and purchases from parties not established in Italy | Through the SdI since 1 July 2022 |
| Not reported | Operations with a customs bill (bolletta doganale); operations already e-invoiced via the SdI; purchases not territorially relevant in Italy (arts. 7 to 7-octies D.P.R. 633/1972) up to EUR 5,000 each | "di importo non superiore ad euro 5.000 per ogni singola operazione" |
| Sales | Code `XXXXXXX`, normal document type | Invoice deadline |
| Purchases | TD17 services, TD18 intra-EU goods, TD19 goods under art. 17(2), TD28 San Marino | Fifteenth day |

The compilation guide 1.10 shows how to fill and correct TD16 to TD29.

#### SDI Processing Flow

1. Sender transmits the XML file (signed or unsigned) to the SdI.
2. The SdI checks the file name, size, signature (if any), format and content.
3. If valid, the SdI delivers the file and sends a delivery receipt (RC), or a receipt of impossible delivery (MC).
4. If invalid, the SdI sends a rejection receipt (ricevuta di scarto, NS) within 5 days of receiving the file.
5. A rejected invoice is treated as never issued. Correct the error and resend, reusing the rejected invoice's date and number, with a new file name unless using the portal's web procedure.

### Validation Rules

#### SDI Pre-Checks (Automated)

**SDI Pre-Checks (Automated)**

| Check | Error Code | Description |
| --- | --- | --- |
| File name | 00001, 00002 | File name not valid; file name already used |
| File size | 00003 | File larger than allowed |
| Digital signature | 00100 to 00107 | Certificate or signature problems |
| Schema validation | 00200, 00201 | Not in the format; more than fifty format errors |
| Tax IDs | 00300, 00301, 00303, 00305 | IdCodice not valid (sender, seller, representative or intermediary, buyer) |
| CodiceDestinatario | 00311, 00312, 00313 | Code not valid; code not active; `XXXXXXX` used for an Italian buyer |
| Code length | 00427 | 7 characters with FPA12, or 6 with FPR12 |
| Missing Natura | 00400, 00429 | Zero VAT rate without a nature code (line; summary) |
| VAT amount | 00421 | `Imposta` differs from rate times taxable amount by more than one euro cent |
| Taxable amount | 00422 | `ImponibileImporto` off the sum of lines by more than one euro |
| Duplicate detection | 00404, 00409 | Already processed; duplicate in the batch |
| Simplified invoice total | 00460 | Total above the simplified-invoice limit (section "Tax Computation Rules") |

#### Common Rejection Reasons

**Common Rejection Reasons**

| Issue | Resolution |
| --- | --- |
| Invalid Partita IVA | Check it with the Agenzia's VAT number service or VIES |
| Duplicate invoice | Same seller, same year and same number is rejected; only a credit note (TD04, or TD08 simplified) may share it |
| Missing Natura code | Use a sub-code (N2.1, N3.2, N6.3 and so on), not the retired N2, N3 or N6 |
| Expired digital certificate | Renew the certificate, or send unsigned |

### Tax Computation Rules

#### VAT Rates (2025/2026)

**VAT Rates (2025/2026)**

| Rate | Application | Note | Source |
| --- | --- | --- |---|
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/web/guest/iva-regole-generali-aliquote-esenzioni-pagamento/norme-generali-e-aliquote |  |
| 22% | Standard rate | "l'aliquota ordinaria Iva è del 22%" | https://www.agenziaentrate.gov.it/portale/web/guest/iva-regole-generali-aliquote-esenzioni-pagamento/norme-generali-e-aliquote |
| 10% | Reduced rate (for example household electricity and gas, medicines, building renovation) | "10% , per esempio per la fornitura di energia elettrica" | same |
| 5% | Reduced rate (some foods) | "5% , per esempio per alcuni alimenti" | same |
| 4% | Super-reduced rate (basic food, drinks, agricultural products) | "4% , per esempio per alimentari, bevande e prodotti agricoli" | same |

For a line with no VAT, the rate field is set to "0%" with a nature code; for a forfettario the nature is "Non soggette - altri casi" (N2.2) ([forfettari page](https://www.agenziaentrate.gov.it/portale/fattura-elettronica-per-i-forfettari)).

#### Simplified invoice limit

| Item | Amount | Note | Source |
| --- | --- | --- |---|
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/documents/d/guest/allegato-a-specifiche-tecniche-vers-1-9-1 |  |
| Maximum total of a simplified invoice (TD07), error 00460 | EUR 400 | "non può eccedere il limite di euro 400"; no limit for forfettari and RF20 | https://www.agenziaentrate.gov.it/portale/documents/d/guest/allegato-a-specifiche-tecniche-vers-1-9-1 |

#### Rounding

- **Line level**: `PrezzoTotale` = (`PrezzoUnitario` plus or minus discounts) times `Quantita` (error 00423).
- **Summary level**: `Imposta` = `ImponibileImporto` times `AliquotaIVA` / 100, rounded half up to two decimals.
- **SdI tolerance**: one euro cent on `Imposta` (error 00421) and one euro on `ImponibileImporto` (error 00422).

#### Multi-Rate Invoices

Each VAT rate and each nature code needs its own `DatiRiepilogo` block. `Natura` is required with a zero rate and forbidden otherwise, except in a TD16.

#### Split Payment (Scissione dei Pagamenti)

- **Split Payment rule**: for public administrations and other designated buyers, the buyer pays the VAT to the Treasury. Set `EsigibilitaIVA` to S; not allowed with an N6 nature code.

#### Stamp duty (imposta di bollo) on e-invoices

| Item | Amount or rule | Note | Source |
| --- | --- | --- |---|
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/documents/d/guest/l-imposta_di_bollo_sulle_fatture_elettronichegiugno2026 |  |
| When due | The Agenzia flags an invoice as owing stamp duty (list B) when the sum of its line totals is above EUR 77.47, a line carries nature N2.1, N2.2, N3.5, N3.6 or N4, and no NB code is shown | "risulta maggiore di 77,47 euro" | https://www.agenziaentrate.gov.it/portale/documents/d/guest/l-imposta_di_bollo_sulle_fatture_elettronichegiugno2026 |
| Amount | EUR 2 per invoice | "i 2 euro dell'imposta di bollo" ([forfettari page](https://www.agenziaentrate.gov.it/portale/fattura-elettronica-per-i-forfettari)) |  |
| How shown | `BolloVirtuale` = "SI"; forfettari include the stamp in the document total | Forfettari page | https://www.agenziaentrate.gov.it/portale/fattura-elettronica-per-i-forfettari |
| Not subject | Line tag `TipoDato` (2.2.1.16.1): NB1 insurance, NB2 third sector, NB3 bank statement | Ordinary invoice only | https://www.agenziaentrate.gov.it/portale/documents/d/guest/l-imposta_di_bollo_sulle_fatture_elettronichegiugno2026 |
| Excluded from the check | TD16, TD17, TD18, TD19, TD28, and RegimeFiscale RF05 to RF11 | June 2026 guide | same |
| Quarterly check | Agenzia lists A (stamp shown) and B (stamp missing, editable) per quarter | Edit B by the end of the next month; Q2 by 10 September | same |
| Payment | Q1 31 May; Q2 30 September; Q3 30 November; Q4 28 February next year (29 in a leap year) | Portal, or F24 codes 2521 to 2524, 2525 penalties, 2526 interest | same |
| Small amounts | If Q1 is not above EUR 5,000, pay it by 30 September; if Q1 and Q2 together are not above EUR 5,000, pay them by 30 November | "non supera 5.000 euro" | same |
| Late or short payment | PEC notice: stamp, penalty cut to one third, interest | Reply within thirty days | same |
| Review | A stamp charged in error can be removed after a successful request for review (riesame); see the lists of excluded invoices in the portal | June 2026 guide | same |

### Archiving Requirements

**Archiving Requirements**

| Requirement | Detail |
| --- | --- |
| Who | Issuer and recipient both store the e-invoice "a norma" (art. 39 D.P.R. 633/1972), a process under the CAD, not a copy on a PC |
| Format | Original XML as sent or received through the SdI |
| Retention period | Ten years from the last entry, for books and for invoices ([art. 2220 Civil Code](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2220!vig=2026-06-30)) |
| Providers | Usually certified private operators |
| Free AdE service | Free storage of e-invoices issued and received, in "Fatture e Corrispettivi", after accepting the service agreement; past SdI invoices addable back to 1 January of the second year before joining ([free storage service](https://www.agenziaentrate.gov.it/portale/aree-tematiche/fatturazione-elettronica/guida-fatturazione-elettronica/i-servizi-dell-agenzia-fe/servizio-conservazione-elettronica)) |
| Audit access | Tax authorities may ask for the stored invoices at any time |

### Penalties for Non-Compliance

**Penalties for Non-Compliance**

| Violation | Penalty | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art6!vig=2026-06-30 |
| Taxable operation not invoiced or late, or VAT understated (art. 6(1)) | Seventy per cent of the VAT on the undocumented amount | "sanzione amministrativa del settanta per cento dell'imposta" |
| Same, when the VAT settlement was not affected (art. 6(1)) | EUR 250 to EUR 2,000 | "da euro 250 a euro 2.000 quando la violazione non ha inciso" |
| Non-taxable, exempt, out-of-scope or reverse-charge operation not invoiced (art. 6(2)) | Five per cent of the consideration; EUR 250 to EUR 2,000 if income is not affected either | "del cinque per cento dei corrispettivi non documentati" |
| Buyer who does not report a missing or irregular invoice within ninety days, by TD29 (art. 6(8)) | Seventy per cent of the VAT, minimum EUR 250 | "con un minimo di euro 250" |
| Buyer who skips reverse-charge steps, TD16 to TD19 (art. 6(9-bis)) | EUR 500 to EUR 10,000 | "compresa fra 500 euro e 10.000 euro" |
| Same, when the operation is not in the buyer's books | Five per cent of the taxable amount, minimum EUR 1,000 | "con un minimo di 1.000 euro" |
| Rejected invoice not re-sent | Never issued; penalties above apply | section "Transmission Method" |
| Reduced penalty (ravvedimento operoso) | Available; fractions not restated | Refer |

These rates apply to violations from 1 September 2024 (D.Lgs. 87/2024, art. 5); earlier violations follow the text then in force.

| Violation | Penalty | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art11!vig=2026-06-30 |
| Cross-border data omitted or wrong, operations from 1 July 2022 (art. 11(2-quater)) | EUR 2 per invoice, up to EUR 400 a month | "euro 2 per ciascuna fattura, entro il limite massimo di euro 400 mensili" |
| Same, corrected within fifteen days of the deadline | Halved, up to EUR 200 a month | "limite massimo di euro 200 per ciascun mese" |
| Stamp duty paid late or short | Art. 13(1) D.Lgs. 471/1997, cut to one third on the Agenzia's notice | section "Tax Computation Rules" |

### Interaction with other Guides

#### VAT Return Integration

- SdI invoices appear in the taxpayer's "Fatture e Corrispettivi" area.
- For operators in the group set by the provvedimento of 8 July 2021, the Agenzia drafts VAT registers, settlements and the annual return from SdI data. See `italy-vat-return`.
- Gaps between SdI data and VAT returns can trigger compliance letters.

#### Income Tax Integration

- SdI invoices are the record of a self-employed person's revenue, which also drives the forfettario limits. See `it-income-tax` and `italy-bookkeeping`.

#### Withholding Tax

- `DatiRitenuta` records withholding (ritenuta d'acconto) on fees: RT01 natural persons, RT02 legal persons, RT03 to RT06 social security contributions. Amounts flow to the CU and Modello 770 (see `italy-payroll`).
- A forfettario professional adds a causale that the fee is not subject to withholding under art. 1(67) L. 190/2014 ([forfettari page](https://www.agenziaentrate.gov.it/portale/fattura-elettronica-per-i-forfettari)).

## Worked cases

### Case 1: a forfettario's invoice, stamp duty and the quarterly payment

Facts. Giulia, a forfettario graphic designer, invoices an Italian company EUR 1,000 for a logo on 3 February 2026. The line carries nature N2.2 (no VAT, forfettario). In the first quarter she issues 30 such invoices, all above EUR 77.47.

Steps. She sends the XML (TD01) through "Fatture e Corrispettivi" within 12 days, by 15 February 2026, to the buyer's 7-character code. The invoice has no VAT and is above EUR 77.47, so she sets `BolloVirtuale` to SI and adds the EUR 2 stamp to the document total, EUR 1,002. The causale says the fee is not subject to withholding under art. 1(67) L. 190/2014. Her first-quarter stamp duty is 30 x EUR 2 = EUR 60; that is not above EUR 5,000, so she may pay it by 30 September 2026 with the second quarter instead of 31 May.

```oa-check
name: Italy 2026, forfettario invoice with stamp duty and Q1 stamp total
inputs:
  fee: 1000
  stamp: 2
  invoices_q1: 30
  small_amount_limit: 5000
steps:
  - document_total: fee + stamp
  - stamp_q1: invoices_q1 * stamp
  - headroom_small_amount: small_amount_limit - stamp_q1
expected:
  document_total: 1002.00
  stamp_q1: 60.00
  headroom_small_amount: 4940.00
```

### Case 2: cross-border data left out for one month

Facts. Beta S.r.l. forgot to send 300 TD17 self-invoices for services bought from foreign suppliers in March 2026, and corrects it two months later.

Working. The penalty is EUR 2 per invoice, capped at EUR 400 for the month: 300 x EUR 2 = EUR 600, so EUR 400 (D.Lgs. 471/1997 art. 11(2-quater)). Had it corrected within 15 days of the deadline, the cap would have been EUR 200.

```oa-check
name: Italy 2026, cross-border data penalty cap for one month
inputs:
  invoices: 300
  per_invoice: 2
  monthly_cap: 400
steps:
  - uncapped: invoices * per_invoice
  - penalty: min(uncapped, monthly_cap)
expected:
  uncapped: 600.00
  penalty: 400.00
```

## When to refuse or refer

- Invoices to public administrations (CIG, CUP, NSO orders): refer; this Guide covers private parties.
- An Agenzia notice on stamp duty, cross-border data or penalties: refer to a commercialista.
- Ravvedimento operoso calculations: refer; the fractions changed with D.Lgs. 87/2024 and are not restated here.
- VAT group, fiscal representative, VAT warehouse (TD22, TD23) or plafond (TD21) cases: refer to a specialist.
- Designing a certified storage system: refer to a certified provider.
- Whether an operation is taxable at all: see `italy-vat-return`.

## Sources

Every page below was opened on 2026-11-14 and the figures this skill takes from it were found in the text.

| Source | URL | Read on |
| --- | --- | --- |
| Agenzia: technical specifications 1.9.1. Read for the XML schema, document types, nature codes and the EUR 400 TD07 limit | https://www.agenziaentrate.gov.it/portale/documents/d/guest/allegato-a-specifiche-tecniche-vers-1-9-1 | 2026-11-14 |
| Agenzia: specification versions. Read for version 1.9.1 being usable from 15 May 2026 | https://www.agenziaentrate.gov.it/portale/fatturazione-elettronica-e-dati-fatture-transfrontaliere-new | 2026-11-14 |
| Agenzia: e-invoice guide (December 2025). Read for the B2G and B2B start dates and the portal | https://www.agenziaentrate.gov.it/portale/documents/d/guest/la_fattura_elettronica | 2026-11-14 |
| Agenzia: compilation guide 1.10. Read for TD16 to TD29 and cross-border reporting | https://www.agenziaentrate.gov.it/portale/documents/d/guest/guida_compilazione-fe-esterometro-v1-10_aprile_2025 | 2026-11-14 |
| Agenzia: e-invoices for forfettari. Read for the forfettari duty, the N2.2 code and the EUR 2 stamp | https://www.agenziaentrate.gov.it/portale/fattura-elettronica-per-i-forfettari | 2026-11-14 |
| Agenzia: stamp duty guide (June 2026). Read for the EUR 77.47 trigger, quarterly payment dates and the EUR 5,000 small-amount rule | https://www.agenziaentrate.gov.it/portale/documents/d/guest/l-imposta_di_bollo_sulle_fatture_elettronichegiugno2026 | 2026-11-14 |
| Agenzia: VAT rates. Read for the 22%, 10%, 5% and 4% rates | https://www.agenziaentrate.gov.it/portale/web/guest/iva-regole-generali-aliquote-esenzioni-pagamento/norme-generali-e-aliquote | 2026-11-14 |
| Agenzia: free storage service. Read for the free storage service | https://www.agenziaentrate.gov.it/portale/aree-tematiche/fatturazione-elettronica/guida-fatturazione-elettronica/i-servizi-dell-agenzia-fe/servizio-conservazione-elettronica | 2026-11-14 |
| D.Lgs. 127/2015, art. 1. Read for who must use the SdI and the EUR 5,000 cross-border purchase exclusion | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2015-08-05;127~art1!vig=2026-06-30 | 2026-11-14 |
| D.P.R. 633/1972, art. 21. Read for the 12-day and 15th-of-next-month deadlines | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art21!vig=2026-06-30 | 2026-11-14 |
| D.L. 36/2022, art. 18. Read for forfettari in the SdI from 1 July 2022 above EUR 25,000 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2022-04-30;36~art18!vig=2026-06-30 | 2026-11-14 |
| D.L. 119/2018, art. 10-bis. Read for the health services exclusion | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2018-10-23;119~art10bis!vig=2026-06-30 | 2026-11-14 |
| D.Lgs. 471/1997, art. 6. Read for penalties for invoices not issued (70%, EUR 250 to 2,000, 5%) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art6!vig=2026-06-30 | 2026-11-14 |
| D.Lgs. 471/1997, art. 11. Read for the EUR 2 and EUR 400 cross-border data penalty | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art11!vig=2026-06-30 | 2026-11-14 |

Not yet confirmed: that FatturaPA is not EN 16931; the schema file names VFPR12 and VFSM10 (not in the specifications 1.9.1 text).

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a commercialista, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

> Contributed by OpenAccountants.
