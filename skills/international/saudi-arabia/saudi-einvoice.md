---
name: saudi-einvoice
description: Use this skill whenever asked about Saudi Arabia e-invoicing, ZATCA FATOORA platform, Phase 1 generation, Phase 2 integration, e-invoice clearance, e-invoice reporting, ZATCA API, UBL 2.1 XML for Saudi invoices, cryptographic stamp, QR code TLV encoding, ECDSA signing, CSID certificate, onboarding OTP, Simplified vs Standard tax invoice, B2B clearance, B2C reporting, or any question about generating, submitting, or troubleshooting Saudi e-invoices. Also trigger when advising on ZATCA compliance waves, XML structure, digital signature requirements, or integration architecture. ALWAYS read this skill before touching any Saudi e-invoice work.
version: 1.0
jurisdiction: SA
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Mehran Habib
review_status: current
depends_on:
  - einvoice-workflow-base
category: invoicing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Saudi Einvoice

## Saudi Arabia ZATCA E-Invoice (FATOORA) Skill v1.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Mehran Habib** on 2026-06-06.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### E-Invoice (FATOORA)

- **Phase 1 (Generation)** — All VAT-registered since 4 Dec 2021  _(E-Invoicing Regulation, First: Scope of application)_
- **Phase 2 (Integration)** — Rolling waves from 1 Jan 2023 by revenue  _(E-Invoicing Regulation, Sixth: Integration)_
- **Format** — XML format or PDF/A-3 format (with embedded XML)  _(E-Invoicing Regulation, Second Requirements and details for Generation of Electronic Invoices and Electronic Notes - 2)_
- **Signing** — ECDSA secp256k1 + SHA-256  _(E-Invoicing Regulation, Annex 1 Technical Requirements of E-invoice Generation Solutions)_
- **B2B clearance** — Real-time before sharing with buyer  _(E-Invoicing Regulation, Annex 1 Technical Requirements of E-invoice Generation Solutions)_
- **B2C reporting** — Within 24 hours  _(E-Invoicing Regulation, Second Requirements and details for Generation of Electronic Invoices and Electronic Notes - 3(B))_
- **Non-issuance of e-invoice** — SAR 5,000–50,000 per violation  _(VAT Law, Article 45)_
- **Modification after issuance** — SAR 10,000–50,000 per violation  _(VAT Law, Article 45)_

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Kingdom of Saudi Arabia (KSA) |
| Currency | SAR (Saudi Riyal) |
| E-Invoicing System | FATOORA Platform |
| Governing Body | Zakat, Tax and Customs Authority (ZATCA) |
| Key Legislation | E-Invoicing Regulation (issued 4 December 2021); VAT Implementing Regulations |
| Schema Standard | UBL 2.1 (Universal Business Language) XML |
| Cryptographic Standard | ECDSA secp256k1 digital signature |
| Phase 1 (Generation) | Mandatory from 4 December 2021 (all VAT-registered taxpayers) |
| Phase 2 (Integration) | Rolling waves from 1 January 2023, based on revenue thresholds |
| Current Status | Phase 2 waves ongoing through 2026; smaller thresholds being added progressively |
| Portal | fatoora.zatca.gov.sa |

### Phase 2 Integration Waves

**Phase 2 Integration Waves**

| Wave | Effective Date | Revenue Threshold |
| --- | --- | --- |
| Wave 1 | 1 January 2023 | > SAR 3 billion |
| Wave 2 | 1 July 2023 | > SAR 500 million |
| Wave 3 | 1 October 2023 | > SAR 250 million |
| Wave 4 | 1 November 2023 | > SAR 150 million |
| Wave 5 | 1 December 2023 | > SAR 100 million |
| Wave 6 | 1 March 2024 | > SAR 70 million |
| Wave 7 | 1 June 2024 | > SAR 50 million |
| Wave 8 | 1 October 2024 | > SAR 40 million |
| Wave 9 | 1 December 2024 | > SAR 30 million |
| Wave 10+ | 2025-2026 | Progressively lower thresholds |

## Section 2 -- Mandate Scope

### Phase 1 -- Generation (All Taxpayers Since Dec 2021)

- **Phase 1 scope** — ALL VAT-registered taxpayers in KSA; Must generate e-invoices (and credit/debit notes) using a compliant electronic system; Paper invoices no longer legally valid; Basic QR code required on simplified (B2C) invoices; No system-to-system integration required

### Phase 2 -- Integration (Wave-Based)

- **Phase 2 requirements** — System must integrate with ZATCA's FATOORA platform via API; Standard Tax Invoice (B2B): Must be cleared by ZATCA before delivery to buyer; Simplified Tax Invoice (B2C): Must be reported to ZATCA within 24 hours; Cryptographic stamp (digital signature) required on all invoices; Enhanced QR code with TLV-encoded cryptographic data

### Document Types

**Document Types**

| Type | Code | SubType Code | Clearance Model |
| --- | --- | --- | --- |
| Standard Tax Invoice (B2B) | 388 | 0100000 | Real-time clearance (before sharing with buyer) |
| Simplified Tax Invoice (B2C) | 388 | 0200000 | Near-real-time reporting (within 24 hours) |
| Standard Credit Note | 381 | 0100000 | Clearance |
| Simplified Credit Note | 381 | 0200000 | Reporting |
| Standard Debit Note | 383 | 0100000 | Clearance |
| Simplified Debit Note | 383 | 0200000 | Reporting |

### Exemptions

- **Exemptions** — None for Phase 1 — all VAT-registered taxpayers must comply; Phase 2 integration is wave-based by revenue; ZATCA notifies targeted groups 6 months in advance

## Section 3 -- Technical Format

### XML Specification

**XML Specification**

| Aspect | Detail |
| --- | --- |
| Format | XML |
| Standard | UBL 2.1 (ISO/IEC 19845:2015) |
| Root Element | `<Invoice>` or `<CreditNote>` or `<DebitNote>` |
| Namespace (UBL) | urn:oasis:names:specification:ubl:schema:xsd:Invoice-2 |
| Namespace (cac) | urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2 |
| Namespace (cbc) | urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2 |
| Namespace (ext) | urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2 |
| CIUS | ZATCA Saudi Arabia CIUS (country-specific extensions within UBL) |
| Encoding | UTF-8 |

### Cryptographic Requirements (Phase 2)

**Cryptographic Requirements (Phase 2)**

| Component | Specification |
| --- | --- |
| Signing Algorithm | ECDSA with secp256k1 curve |
| Hash Algorithm | SHA-256 |
| Certificate | X.509 issued by ZATCA via CSR/CSID process |
| Invoice Hash | Base64-encoded SHA-256 of canonical XML (before signing) |
| Previous Invoice Hash | Hash of the previously issued invoice (chain integrity) |
| UUID | RFC 4122 v4 (randomly generated 128-bit identifier per document) |

### QR Code Structure (Phase 2)

**QR Code Structure (Phase 2)**

| Tag | Field | Data Type |
| --- | --- | --- |
| 1 | Seller Name | UTF-8 String |
| 2 | VAT Registration Number | UTF-8 String |
| 3 | Invoice Timestamp | ISO 8601 (YYYY-MM-DDThh:mm:ssZ) |
| 4 | Invoice Total (with VAT) | Decimal String |
| 5 | VAT Amount | Decimal String |
| 6 | Invoice Hash (SHA-256) | Base64 |
| 7 | ECDSA Signature | Base64 |
| 8 | Public Key | Base64 (DER-encoded) |
| 9 | Certificate Signature | Base64 |

### QR Code Structure (Phase 2)

TLV (Tag-Length-Value) encoding with Base64:

## Section 4 -- Mandatory Fields

### Invoice-Level Fields

**Invoice-Level Fields**

| UBL Path | Description | Example |
| --- | --- | --- |
| cbc:ID | Invoice number | INV-2026-001 |
| cbc:UUID | RFC 4122 UUID | 8d487816-... |
| cbc:IssueDate | Issue date | 2026-05-22 |
| cbc:IssueTime | Issue time | 14:30:00 |
| cbc:InvoiceTypeCode | Document type | 388 |
| cbc:InvoiceTypeCode/@name | SubType code | 0100000 (standard) or 0200000 (simplified) |
| cbc:DocumentCurrencyCode | Currency | SAR |
| cbc:TaxCurrencyCode | Tax currency | SAR |
| cac:AdditionalDocumentReference (ICV) | Invoice Counter Value | Sequential integer |
| cac:AdditionalDocumentReference (PIH) | Previous Invoice Hash | Base64 SHA-256 |

### Supplier (cac:AccountingSupplierParty)

**Supplier (cac:AccountingSupplierParty)**

| Path | Description |
| --- | --- |
| cac:Party/cac:PartyIdentification/cbc:ID (@schemeID="CRN") | Commercial Registration Number |
| cac:Party/cac:PartyTaxScheme/cbc:CompanyID | VAT Registration Number (15 digits) |
| cac:Party/cac:PartyLegalEntity/cbc:RegistrationName | Legal name (Arabic required) |
| cac:Party/cac:PostalAddress/cbc:StreetName | Street |
| cac:Party/cac:PostalAddress/cbc:BuildingNumber | Building number |
| cac:Party/cac:PostalAddress/cbc:CityName | City |
| cac:Party/cac:PostalAddress/cbc:PostalZone | Postal code |
| cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode | SA |

### Buyer (cac:AccountingCustomerParty) — Standard Invoice

**Buyer (cac:AccountingCustomerParty) — Standard Invoice**

| Path | Description |
| --- | --- |
| cac:Party/cac:PartyTaxScheme/cbc:CompanyID | Buyer VAT number |
| cac:Party/cac:PartyLegalEntity/cbc:RegistrationName | Buyer legal name |
| cac:Party/cac:PostalAddress | Full address (street, city, postal code) |

### Tax Total (cac:TaxTotal)

**Tax Total (cac:TaxTotal)**

| Path | Description |
| --- | --- |
| cbc:TaxAmount | Total VAT amount |
| cac:TaxSubtotal/cbc:TaxableAmount | Taxable amount per rate |
| cac:TaxSubtotal/cbc:TaxAmount | Tax amount per rate |
| cac:TaxSubtotal/cac:TaxCategory/cbc:ID | Tax category (S, Z, E, O) |
| cac:TaxSubtotal/cac:TaxCategory/cbc:Percent | VAT rate (15, 0, etc.) |

### Line Items (cac:InvoiceLine)

**Line Items (cac:InvoiceLine)**

| Path | Description |
| --- | --- |
| cbc:ID | Line number |
| cbc:InvoicedQuantity | Quantity |
| cbc:LineExtensionAmount | Line net amount |
| cac:Item/cbc:Name | Item name |
| cac:Item/cac:ClassifiedTaxCategory/cbc:ID | Tax category |
| cac:Item/cac:ClassifiedTaxCategory/cbc:Percent | VAT rate |
| cac:Price/cbc:PriceAmount | Unit price |

## Section 5 -- Transmission Method

### Onboarding Process

- **Onboarding steps** — 1. Register on FATOORA portal (fatoora.zatca.gov.sa) using ZATCA credentials 2. Generate OTP (One-Time Password) per EGS device 3. EGS generates ECDSA private key (secp256k1) and Certificate Signing Request (CSR) 4. Submit CSR + OTP to Compliance CSID API → receive Compliance CSID (temporary certificate) 5. Run 3 compliance checks (standard invoice, simplified invoice, credit note) 6. Submit compliance check results → receive Production CSID (permanent certificate) 7. Begin production clearance/reporting

### API Endpoints

**API Endpoints**

| Endpoint | Method | Purpose |
| --- | --- | --- |
| /compliance | POST | Onboarding — get Compliance CSID |
| /production/csids | POST | Get Production CSID |
| /compliance/invoices | POST | Submit compliance test invoices |
| /invoices/clearance | POST | Clear standard (B2B) invoices |
| /invoices/reporting | POST | Report simplified (B2C) invoices |

### Production Base URL

- **Production Base URL** — https://gw-fatoora.zatca.gov.sa/e-invoicing/developer-portal

### Authentication

- **Authentication requirements** — HTTP Basic Auth using Base64-encoded `{CSID_binary_token}:{secret}`; Each EGS device has its own certificate and credentials; Certificate renewal required before expiry

## Section 6 -- Validation Rules

### ZATCA Server-Side Validation

- **Validation checks** — 1. XML schema validation against UBL 2.1 + ZATCA CIUS 2. Cryptographic signature verification (ECDSA secp256k1) 3. Certificate chain validation (must be ZATCA-issued) 4. Invoice hash verification (SHA-256 of canonical form) 5. Previous invoice hash chain integrity 6. UUID uniqueness check 7. Invoice Counter Value (ICV) sequence validation 8. Tax calculation verification (line totals, tax amounts) 9. Seller VAT number validity 10. Buyer VAT number validity (standard invoices)

### Common Rejection Reasons

**Common Rejection Reasons**

| Code | Description | Resolution |
| --- | --- | --- |
| INVALID-SIGNATURE | Signature verification failed | Regenerate signature with correct private key |
| INVALID-CERTIFICATE | Certificate not issued by ZATCA | Re-onboard the EGS device |
| DUPLICATE-UUID | UUID already submitted | Generate new UUID per RFC 4122 |
| INVALID-HASH | Invoice hash does not match content | Recompute SHA-256 on canonical XML |
| PIH-MISMATCH | Previous invoice hash incorrect | Use hash of actual last invoice |
| TAX-CALC-ERROR | Tax amounts do not compute | Verify: TaxAmount = TaxableAmount × Rate |
| MISSING-FIELD | Required field absent | Add missing UBL element |

### Validation Statuses

**Validation Statuses**

| Status | Meaning |
| --- | --- |
| CLEARED | Standard invoice accepted (can share with buyer) |
| REPORTED | Simplified invoice acknowledged |
| REJECTED | Validation failed — must fix and resubmit |
| WARNING | Non-blocking issue — invoice accepted but flagged |

## Section 7 -- Tax Computation Rules

### VAT Rates in KSA

**VAT Rates in KSA**

| Category | Code | Rate | Description |
| --- | --- | --- | --- |
| Standard | S | 15% | Default rate |
| Zero-rated | Z | 0% | Exports, international transport |
| Exempt | E | 0% | Financial services, residential rent |
| Out of scope | O | 0% | Government services |

### Calculation Rules

- **Calculation rules** — Line Extension Amount = Quantity × Unit Price - Discount; Tax Amount per line = Line Extension Amount × Tax Rate / 100; Rounding: 2 decimal places (round half-up); Document-level TaxTotal must equal sum of all line tax amounts (tolerance: SAR 0.01); TaxInclusiveAmount = TaxExclusiveAmount + TaxTotal

### Multi-Rate Invoice

- **Multi-rate invoice handling** — Each line item carries its own TaxCategory and Percent; TaxTotal contains multiple TaxSubtotal elements (one per distinct rate); Each TaxSubtotal aggregates TaxableAmount and TaxAmount for that rate

## Section 8 -- Archiving Requirements

**Archiving Requirements**

| Requirement | Detail |
| --- | --- |
| Retention Period | Minimum 6 years from end of tax period (VAT Implementing Regulations Art. 66) |
| Format | Original XML (signed) + ZATCA response |
| Digital Signature | Must retain the signed XML with embedded UBL Extensions containing the signature |
| Integrity | Invoice hash chain provides tamper evidence |
| Medium | Electronic storage; must be accessible on demand by ZATCA |
| QR Code | Physical/PDF copies must display the complete TLV QR code |
| Language | Arabic required for invoice content; bilingual (Arabic + English) permitted |

## Section 9 -- Penalties for Non-Compliance

**Penalties for Non-Compliance**

| Violation | Penalty (SAR) |
| --- | --- |
| Not issuing e-invoices | 5,000 -- 50,000 per violation |
| Not including required fields | 5,000 -- 50,000 per violation |
| Not integrating with FATOORA (Phase 2) | 5,000 -- 50,000 per violation |
| Deleting or modifying e-invoices after issuance | 10,000 -- 50,000 per violation |
| Not storing e-invoices per requirements | 5,000 -- 50,000 per violation |
| Obstructing ZATCA officials | 5,000 -- 50,000 per violation |
| Repeated violations | Penalty doubled; potential business suspension |

## Section 9 -- Penalties for Non-Compliance

ZATCA may also publish violator names publicly and may suspend tax registration for severe/repeated non-compliance.

## Section 10 -- Interaction with Tax Skills

### VAT Return Integration

- **VAT return integration** — Cleared B2B invoices feed directly into ZATCA's VAT return pre-population; Reported B2C invoices aggregated for VAT return box totals; VAT return data (Box 1: standard-rated sales, Box 2: zero-rated, etc.) can be cross-referenced against FATOORA submission records; Discrepancies between submitted e-invoices and VAT return values trigger ZATCA risk-assessment flags

### Credit Note Handling

- **Credit note handling** — Credit notes must reference the original invoice UUID; Tax adjustments in VAT return derived from cleared credit notes; ZATCA validates that credit note does not exceed original invoice value

### Withholding Tax

- **Withholding tax interaction** — If withholding tax applies (certain services), the invoice must still show full VAT amount; Withholding is a separate mechanism; e-invoice shows gross amounts

### Audit Trail

- **Audit trail** — ZATCA maintains complete record of all cleared/reported invoices; Taxpayer's records must match ZATCA's records exactly; UUID + ICV provide unique identification for audit queries

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, SOCPA member, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
