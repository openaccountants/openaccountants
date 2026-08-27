---
name: italy-einvoice
description: Use this skill whenever asked about Italian e-invoicing, FatturaPA, Sistema di Interscambio (SDI), electronic invoicing compliance in Italy, Codice Destinatario, PEC invoicing, fattura elettronica, TD document types, cross-border e-invoicing via SDI, conservazione sostitutiva, or any question about issuing, receiving, validating, or archiving electronic invoices in Italy. Also trigger when preparing or reviewing XML invoices for SDI submission, handling SDI rejection (scarto) errors, configuring Codice Destinatario or PEC routing, or advising on FatturaPA technical format compliance. This skill covers the FatturaPA XML schema, SDI transmission channels, mandatory fields, validation rules, archiving, penalties, and interaction with Italian VAT returns. ALWAYS read this skill before touching any Italian e-invoicing work.
version: 1.0
jurisdiction: IT
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - einvoice-workflow-base
category: invoicing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Italy Einvoice

## Italy E-Invoicing -- FatturaPA / SDI Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

placeholder

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Italy (Repubblica Italiana) |
| Currency | EUR |
| E-invoicing system | Sistema di Interscambio (SDI) |
| Invoice format | FatturaPA XML (proprietary Italian schema) |
| Governing body | Agenzia delle Entrate (AdE) |
| Technical operator | Sogei S.p.A. |
| Key legislation | Legislative Decree 127/2015; Ministerial Decree 55/2013; D.Lgs. 471/1997 (penalties); D.Lgs. 82/2005 (digital archiving) |
| Portal URL | https://www.fatturapa.gov.it |
| Current spec version | FatturaPA v1.9 (effective 1 April 2025) |
| B2G mandatory since | 6 June 2014 |
| B2B/B2C mandatory since | 1 January 2019 |
| Current status | Fully operational -- all VAT-registered taxpayers must issue and receive via SDI |
| EU derogation expires | 31 December 2027 (unless superseded by ViDA) |
| Skill version | 1.0 |

## Section 2 -- Mandate Scope

### Who Must Comply

**Who Must Comply**

| Scope | Requirement |
| --- | --- |
| B2G | Mandatory for all suppliers to public administrations since 2014 |
| B2B | Mandatory for all domestic transactions between VAT-registered businesses since 1 January 2019 |
| B2C | Mandatory since 2019 -- consumer invoices must transit SDI (consumer receives PDF copy) |
| Forfettari / micro-entities | Included since 1 January 2024 -- no remaining size-based exemptions |
| Non-resident businesses | Must issue via SDI for Italian-taxable supplies if registered for VAT in Italy |
| Cross-border | Reported via SDI using document types TD17, TD18, TD19, TD28 (replaced Esterometro from 1 July 2022) |

### Exemptions

- Invoices to/from entities in the Republic of San Marino follow a specific bilateral protocol (TD28)
- Healthcare B2C invoices to natural persons remain excluded from SDI (privacy restrictions) through 2025
- Invoices already transmitted through the NSO (Nodo Smistamento Ordini) for public healthcare orders

### Timeline Summary

**Timeline Summary**

| Date | Milestone |
| --- | --- |
| June 2014 | B2G mandate begins |
| January 2019 | B2B and B2C mandate for all except forfettari |
| July 2022 | Esterometro abolished -- cross-border reporting migrates to SDI |
| January 2024 | Forfettari / micro-entities brought into scope |
| April 2025 | FatturaPA v1.9 specifications effective (TD29, RF20 updates) |
| December 2027 | Current EU derogation expiry |

## Section 3 -- Technical Format

### Format Specification

**Format Specification**

| Parameter | Value |
| --- | --- |
| Format | FatturaPA XML (proprietary, not EN 16931) |
| Schema version | v1.9 (VFSM10.xsd) |
| Root element | `<FatturaElettronica>` |
| Versioning attribute | `versione="FPR12"` (B2B/B2C) or `versione="FPA12"` (B2G) |
| Encoding | UTF-8 |
| Max file size | 5 MB per XML file |
| Namespace | `http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.2.2` |

### XML Structure

The FatturaPA file consists of three top-level complex types:

1. **FatturaElettronicaHeader** (mandatory, single instance)
   - `DatiTrasmissione` -- transmission data (sender ID, recipient code, format)
   - `CedentePrestatore` -- seller/supplier identification
   - `CessionarioCommittente` -- buyer identification
   - `RappresentanteFiscale` -- tax representative (if applicable)
   - `TerzoIntermediarioOSoggettoEmittente` -- third-party intermediary

2. **FatturaElettronicaBody** (mandatory, repeatable for invoice lots)
   - `DatiGenerali` -- general data (invoice number, date, document type, currency)
   - `DatiBeniServizi` -- line items (goods/services description, quantity, price, VAT)
   - `DatiPagamento` -- payment terms and conditions
   - `DatiVeicoli` -- vehicle data (sector-specific)
   - `Allegati` -- attachments (embedded base64)

3. **ds:Signature** (optional -- XAdES-BES for XML or CAdES-BES for .p7m)

### Document Types (TipoDocumento)

**Document Types (TipoDocumento)**

| Code | Description |
| --- | --- |
| TD01 | Standard invoice |
| TD02 | Advance/down payment invoice |
| TD04 | Credit note |
| TD05 | Debit note |
| TD06 | Fee note (parcella) |
| TD07 | Simplified invoice |
| TD16 | Reverse charge integration |
| TD17 | Integration -- intra-EU purchases of services |
| TD18 | Integration -- intra-EU purchases of goods |
| TD19 | Integration -- imports (non-EU) |
| TD24 | Deferred invoice |
| TD25 | Deferred invoice from triangulation |
| TD26 | Sale of depreciable assets / internal transfers |
| TD27 | Self-billing for auto-consumption |
| TD28 | San Marino purchases |
| TD29 | Irregular supplier invoice reporting (new in v1.9) |

## Section 4 -- Mandatory Fields

### Header Fields (FatturaElettronicaHeader)

**Header Fields (FatturaElettronicaHeader)**

| XML Path | Field | Required |
| --- | --- | --- |
| `DatiTrasmissione/IdTrasmittente/IdPaese` | Sender country code | Yes |
| `DatiTrasmissione/IdTrasmittente/IdCodice` | Sender tax ID | Yes |
| `DatiTrasmissione/ProgressivoInvio` | Progressive sending number | Yes |
| `DatiTrasmissione/FormatoTrasmissione` | Format (FPR12 or FPA12) | Yes |
| `DatiTrasmissione/CodiceDestinatario` | Recipient routing code (7 chars B2B, 6 chars B2G) | Yes |
| `CedentePrestatore/DatiAnagrafici/IdFiscaleIVA` | Seller VAT number | Yes |
| `CedentePrestatore/DatiAnagrafici/RegimeFiscale` | Tax regime code (RF01--RF20) | Yes |
| `CedentePrestatore/Sede` | Seller registered address (full) | Yes |
| `CessionarioCommittente/DatiAnagrafici` | Buyer identification (Partita IVA or Codice Fiscale) | Yes |
| `CessionarioCommittente/Sede` | Buyer address | Yes |

### Body Fields (FatturaElettronicaBody)

**Body Fields (FatturaElettronicaBody)**

| XML Path | Field | Required |
| --- | --- | --- |
| `DatiGenerali/DatiGeneraliDocumento/TipoDocumento` | Document type (TD01, etc.) | Yes |
| `DatiGenerali/DatiGeneraliDocumento/Divisa` | Currency (ISO 4217) | Yes |
| `DatiGenerali/DatiGeneraliDocumento/Data` | Invoice date (YYYY-MM-DD) | Yes |
| `DatiGenerali/DatiGeneraliDocumento/Numero` | Invoice number | Yes |
| `DatiBeniServizi/DettaglioLinee/NumeroLinea` | Line number | Yes |
| `DatiBeniServizi/DettaglioLinee/Descrizione` | Line description | Yes |
| `DatiBeniServizi/DettaglioLinee/PrezzoUnitario` | Unit price | Yes |
| `DatiBeniServizi/DettaglioLinee/PrezzoTotale` | Line total | Yes |
| `DatiBeniServizi/DettaglioLinee/AliquotaIVA` | VAT rate (%) | Yes |
| `DatiBeniServizi/DatiRiepilogo/AliquotaIVA` | Summary VAT rate | Yes |
| `DatiBeniServizi/DatiRiepilogo/ImponibileImporto` | Taxable amount per rate | Yes |
| `DatiBeniServizi/DatiRiepilogo/Imposta` | VAT amount per rate | Yes |
| `DatiBeniServizi/DatiRiepilogo/EsigibilitaIVA` | VAT chargeability (I=immediate, D=deferred, S=split) | Yes |
| `DatiPagamento/CondizioniPagamento` | Payment terms code | Yes (if payment section present) |
| `DatiPagamento/DettaglioPagamento/ModalitaPagamento` | Payment method | Yes (if payment section present) |
| `DatiPagamento/DettaglioPagamento/ImportoPagamento` | Payment amount | Yes (if payment section present) |

## Section 5 -- Transmission Method

### SDI Channels

**SDI Channels**

| Channel | Description | Use Case |
| --- | --- | --- |
| SDICoop (Web Service) | SOAP-based web service | High-volume automated B2B |
| SDIFTP | Secure FTP with mutual TLS | Legacy system integration |
| SPCoop | Public connectivity system | B2G via PA network |
| PEC (Certified Email) | Posta Elettronica Certificata | Low-volume, initial setup |
| Web Portal | fatturapa.gov.it upload | Manual submission |
| Peppol | Via Peppol Access Point | Cross-border interoperability |

### Routing

- **CodiceDestinatario**: 7-character alphanumeric code registered with SDI (B2B). If unknown, use `0000000` and the invoice routes via PEC or the buyer's tax drawer (cassetto fiscale).
- **B2G**: 6-character CodiceUnivocoUfficio from the IPA (Indice delle Pubbliche Amministrazioni).
- **PEC fallback**: If CodiceDestinatario is `0000000`, the buyer's PEC address registered with AdE is used.

### Submission Deadlines

**Submission Deadlines**

| Invoice Type | Deadline |
| --- | --- |
| Immediate invoice | 12 days from transaction date |
| Deferred invoice (TD24) | 15th of month following the reference month |
| Cross-border (TD17--TD19) | 15th of month following receipt of foreign invoice |

### SDI Processing Flow

1. Sender transmits XML (signed or unsigned) to SDI
2. SDI performs format and content validation
3. If valid → SDI delivers to recipient and issues delivery receipt (Ricevuta di Consegna)
4. If invalid → SDI issues rejection notice (Notifica di Scarto) within 5 days
5. Rejected invoices are treated as never issued -- must be corrected and resubmitted within 5 days

## Section 6 -- Validation Rules

### SDI Pre-Checks (Automated)

**SDI Pre-Checks (Automated)**

| Check | Error Code Range | Description |
| --- | --- | --- |
| Schema validation | 00001--00100 | XML does not conform to FatturaPA XSD |
| Duplicate detection | 00404 | Same sender, invoice number, date, and recipient already processed |
| VAT number validation | 00301--00305 | IdFiscaleIVA not registered in Anagrafe Tributaria |
| CodiceDestinatario | 00311 | Invalid or unregistered routing code |
| Digital signature | 00200--00205 | Signature invalid, expired, or non-conformant |
| File naming | 00001 | File name does not follow convention: `IT{IdFiscale}_{progressive}.xml` |

### Common Rejection Reasons

**Common Rejection Reasons**

| Issue | Resolution |
| --- | --- |
| Invalid Partita IVA | Verify against VIES or AdE registry |
| Duplicate invoice number | Check progressive numbering; reissue with different number |
| Incorrect TipoDocumento | Match document type to transaction (e.g., TD04 for credit notes) |
| Missing Natura code | Required when AliquotaIVA = 0 (e.g., N1 for excluded, N2 for non-subject, N3 for non-taxable, N4 for exempt, N6 for reverse charge) |
| Rounding errors | VAT amount must match: ImponibileImporto × AliquotaIVA / 100, rounded to 2 decimal places |
| Expired digital certificate | Renew CAdES or XAdES certificate before submission |

## Section 7 -- Tax Computation Rules

### VAT Rates (2025/2026)

**VAT Rates (2025/2026)**

| Rate | Application |
| --- | --- |
| 22% | Standard rate |
| 10% | Reduced rate (hospitality, renovation, certain food) |
| 5% | Super-reduced (specific goods) |
| 4% | Minimum rate (essential food, books, first home) |
| 0% | Zero-rated (exports, intra-EU supplies with valid VIES) |

### Rounding

- **Line-level rounding** — PrezzoTotale = PrezzoUnitario × Quantita, rounded to 2 decimal places
- **Summary-level rounding** — Imposta = ImponibileImporto × AliquotaIVA / 100, rounded to 2 decimal places
- **Standard arithmetic rounding** — 0.5 rounds up
- **SDI rejection tolerance** — SDI rejects invoices where computed VAT differs from stated VAT by more than EUR 1.00 per rate summary line

### Multi-Rate Invoices

Each VAT rate on the invoice must have its own `DatiRiepilogo` block with separate `ImponibileImporto` and `Imposta` totals. Line items are grouped by `AliquotaIVA`. The `Natura` code is required for any line with AliquotaIVA = 0.

### Split Payment (Scissione dei Pagamenti)

- **Split Payment rule** — For B2G transactions and certain designated entities, the buyer withholds VAT and pays it directly to the Treasury. Set EsigibilitaIVA to S (split payment). The seller invoices the gross amount but receives only the net.

## Section 8 -- Archiving Requirements

**Archiving Requirements**

| Requirement | Detail |
| --- | --- |
| Retention period | 10 years (conservazione sostitutiva) |
| Format | Original XML as received/sent via SDI |
| Digital signature | Time-stamped qualified electronic signature required on archived documents |
| Metadata | Structured XML metadata per AGID (Agenzia per l'Italia Digitale) specifications |
| Manuale della Conservazione | Written archiving policy document required, describing procedures and responsibilities |
| Free AdE service | Agenzia delle Entrate offers free conservazione via "Fatture e Corrispettivi" portal -- covers invoices transiting SDI for 15 years (requires opt-in agreement) |
| Third-party archiving | Must use AGID-accredited conservators (Conservatori Accreditati) |
| Audit access | Tax authorities may request full read access to the archive at any time |

## Section 9 -- Penalties for Non-Compliance

**Penalties for Non-Compliance**

| Violation | Penalty |
| --- | --- |
| Failure to issue e-invoice via SDI | 90%--180% of VAT amount per invoice (Art. 6, D.Lgs. 471/1997) |
| Minimum fine (no VAT impact) | EUR 250--2,000 per invoice |
| Late submission to SDI (correct VAT settlement) | EUR 250--2,000 per document |
| Failure to report cross-border (TD17/TD18/TD19) | EUR 250--2,000 per transaction |
| Failure to maintain compliant digital archive | Penalties under D.Lgs. 82/2005 (Codice dell'Amministrazione Digitale) |
| Rejected invoice not corrected within 5 days | Invoice treated as never issued -- full non-issuance penalties apply |
| Reduced penalty (ravvedimento operoso) | Reduced to 1/9 if corrected within 90 days; 1/8 within annual return deadline |

## Section 10 -- Interaction with Tax Skills

### VAT Return Integration

- All invoices transiting SDI are automatically available in the taxpayer's "Fatture e Corrispettivi" portal
- AdE pre-populates quarterly VAT communications (LIPE) and the annual VAT return (Modello IVA) using SDI data
- The pre-filled draft VAT return (dichiarazione precompilata IVA) has been available since 2021 for taxpayers who exclusively use SDI
- Cross-border document types (TD17--TD19, TD28) automatically feed into the reverse charge and intra-EU acquisition sections of the VAT return
- Discrepancies between SDI data and filed VAT returns trigger automated compliance letters (lettere di compliance)

### Income Tax Integration

- SDI data feeds into the pre-compiled income tax return (Modello Redditi PF precompilato) for self-employed individuals
- Revenue figures from Box 1 of the income return should reconcile with total TD01/TD24 invoices issued via SDI
- Forfettari regime taxpayers have flat-rate income computed from SDI-reported revenue

### Withholding Tax

- For professional services (TD06 parcella), the `DatiRitenuta` block in FatturaPA records withholding tax (ritenuta d'acconto) details
- Withholding amount, rate, and payment type flow into the Certificazione Unica (CU) and Modello 770

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a commercialista, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
