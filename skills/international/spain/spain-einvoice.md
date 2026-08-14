---
name: spain-einvoice
description: Use this skill whenever asked about Spanish e-invoicing, factura electrónica Spain, FACe, Facturae, Veri*factu, VERI*FACTU, SII (Suministro Inmediato de Información), AEAT e-invoicing, B2B e-invoicing mandate Spain, RD 1007/2023, RD 238/2026, Ley Crea y Crece, QR tributario, anti-fraud invoicing software, SPFE (Solución Pública de Facturación Electrónica), or any question about issuing, receiving, validating, or archiving electronic invoices in Spain. Also trigger when configuring Veri*factu-compliant billing software, setting up SII real-time reporting, submitting B2G invoices via FACe, or advising on the transition from SII to Veri*factu. This skill covers FACe B2G, SII reporting, Veri*factu anti-fraud system, B2B mandate timeline, accepted formats (Facturae, UBL, CII), mandatory fields, validation rules, archiving, penalties, and interaction with Spanish VAT returns. ALWAYS read this skill before touching any Spanish e-invoicing work.
version: 1.0
jurisdiction: ES
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - einvoice-workflow-base
category: invoicing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spain Einvoice

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Spain (Reino de España) |
| Currency | EUR |
| B2G platform | FACe (Punto General de Entrada de Facturas Electrónicas) |
| B2G format | Facturae 3.2.x (XML) |
| Real-time reporting | SII (Suministro Inmediato de Información) -- since 2017 |
| Anti-fraud system | Veri\*factu (RD 1007/2023 -- RRSIF) |
| B2B e-invoicing system | SPFE (Solución Pública de Facturación Electrónica) + private platforms |
| Governing body | Agencia Estatal de Administración Tributaria (AEAT) |
| Key legislation | Ley 25/2013 (B2G); Ley 18/2022 (Ley Crea y Crece, B2B); RD 1007/2023 (RRSIF/Veri\*factu); RD 238/2026 (B2B technical rules) |
| FACe URL | https://face.gob.es |
| AEAT Veri\*factu | https://www.agenciatributaria.gob.es (sede electrónica) |
| B2G mandatory since | 15 January 2015 |
| SII mandatory since | 1 July 2017 (large taxpayers, monthly filers) |
| Veri\*factu effective | 1 January 2027 (companies); 1 July 2027 (self-employed) |
| B2B e-invoicing Phase 1 | 1 October 2027 (turnover > EUR 8M) |
| B2B e-invoicing Phase 2 | 1 October 2028 (all businesses) |
| Current status | B2G and SII fully operational; Veri\*factu services in production (voluntary since April 2025); B2B mandate pending ministerial order |
| Skill version | 1.0 |

## Section 2 -- Mandate Scope

### Three Parallel Systems

Spain operates three distinct but overlapping e-invoicing/reporting systems:

1. **FACe (B2G)**: Mandatory electronic invoicing to public administrations since 2015
2. **SII (Real-Time Reporting)**: Near real-time VAT ledger reporting to AEAT for large taxpayers since 2017
3. **Veri\*factu + B2B E-Invoicing**: Anti-fraud certified invoicing software and mandatory B2B structured invoice exchange (phasing in 2026--2028)

### Who Must Comply

**Who Must Comply**

| System | Who | Since/From |
| --- | --- | --- |
| FACe (B2G) | All suppliers to Spanish public entities | 15 January 2015 |
| SII | Companies with annual turnover > EUR 6M, monthly VAT filers, REDEME members, large corporate groups | 1 July 2017 |
| Veri\*factu (RRSIF) | Corporate income tax payers (Impuesto sobre Sociedades) | 1 January 2027 |
| Veri\*factu (RRSIF) | Self-employed (IRPF economic activities) and other obligados tributarios | 1 July 2027 |
| B2B e-invoicing | Businesses with turnover > EUR 8M | 1 October 2027 |
| B2B e-invoicing | All remaining businesses and professionals | 1 October 2028 |

### Veri*factu vs Non-Veri*factu

Under RD 1007/2023 (RRSIF), all invoicing software must be certified in one of two modes:

SII participants may continue using SII instead of Veri\*factu, but their software must still comply with RRSIF technical requirements.

**Veri*factu vs Non-Veri*factu Modes**

| Mode | Description |
| --- | --- |
| Veri\*factu | Real-time online transmission of invoice records (registros de facturación) to AEAT; includes QR tributario on every invoice; automatic chain integrity via hash linking |
| Non-Veri\*factu | Offline storage of invoice records with strict integrity, inalterability, traceability, and completeness guarantees; no real-time transmission but audit-ready on demand |

### B2B E-Invoicing (RD 238/2026)

**B2B E-Invoicing Requirements**

| Requirement | Detail |
| --- | --- |
| Structured format | EN 16931-based: CII, UBL, Facturae, or EDIFACT |
| Exchange channel | SPFE (public solution, free) or certified private platforms |
| Invoice lifecycle | Must report: acceptance/rejection, full payment date/amount |
| Payment reporting | Recipients must report payment within 4 calendar days (excluding weekends/holidays) |
| Interoperability | Private platforms must support all accepted formats and transform between them |

## Section 3 -- Technical Format

### B2G: Facturae Format

**B2G Facturae Format**

| Parameter | Value |
| --- | --- |
| Format | Facturae 3.2.2 (XML) |
| Schema | Defined by Spanish Ministry of Finance |
| Namespace | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2_2.xml` |
| Digital signature | XAdES-EPES mandatory (enveloped XML signature) |
| Certificate | Qualified electronic certificate issued by a recognised Spanish CA |

### B2B: Accepted Formats (RD 238/2026)

**B2B Accepted Formats**

| Format | Standard | Notes |
| --- | --- | --- |
| UBL 2.1 | EN 16931 semantic model | With adaptations for Spanish requirements |
| CII | EN 16931 (UN/CEFACT Cross-Industry Invoice) | Interoperable with other EU systems |
| Facturae | Spanish national format | Widely used domestically, accepted for B2B |
| EDIFACT | UN/EDIFACT | Legacy format, accepted for interoperability |

Private platforms must transform invoices between all accepted formats while preserving data integrity and origin.

### Veri*factu Invoice Records

**Veri*factu Invoice Records Fields**

| Field | Description |
| --- | --- |
| NIF emisor | Seller tax ID (NIF) |
| Número factura | Invoice number |
| Fecha expedición | Issue date |
| Tipo factura | Invoice type (F1 standard, F2 simplified, R1--R5 credit notes) |
| Descripción operación | Transaction description |
| Base imponible | Taxable amount per rate |
| Tipo impositivo | Tax rate |
| Cuota | Tax amount |
| Huella (hash) | SHA-256 hash of the invoice record, chained to previous record |
| QR tributario | QR code containing verification URL for AEAT check |

## Section 4 -- Mandatory Fields

### FACe (B2G) Mandatory Fields

**FACe (B2G) Mandatory Fields**

| Facturae XML Path | Field | Required |
| --- | --- | --- |
| `FileHeader/SchemaVersion` | Schema version (3.2.2) | Yes |
| `FileHeader/Modality` | Individual or batch | Yes |
| `Parties/SellerParty/TaxIdentification` | Seller NIF and name | Yes |
| `Parties/BuyerParty/TaxIdentification` | Buyer CIF and name | Yes |
| `Parties/BuyerParty/AdministrativeCentres` | Órgano Gestor, Unidad Tramitadora, Oficina Contable codes | Yes |
| `Invoices/Invoice/InvoiceHeader/InvoiceNumber` | Invoice number | Yes |
| `Invoices/Invoice/InvoiceHeader/InvoiceDocumentType` | Document type (FC, FA, AF) | Yes |
| `Invoices/Invoice/InvoiceIssueData/IssueDate` | Issue date | Yes |
| `Invoices/Invoice/InvoiceIssueData/TaxCurrencyCode` | Currency | Yes |
| `Invoices/Invoice/TaxesOutputs/Tax/TaxTypeCode` | Tax type (01 = IVA) | Yes |
| `Invoices/Invoice/TaxesOutputs/Tax/TaxRate` | Tax rate | Yes |
| `Invoices/Invoice/TaxesOutputs/Tax/TaxableBase/TotalAmount` | Taxable base | Yes |
| `Invoices/Invoice/TaxesOutputs/Tax/TaxAmount/TotalAmount` | Tax amount | Yes |
| `Invoices/Invoice/InvoiceTotals/TotalGrossAmount` | Gross total | Yes |
| `Invoices/Invoice/InvoiceTotals/TotalExecutableAmount` | Amount to pay | Yes |
| `Invoices/Invoice/PaymentDetails` | Payment terms | Yes |

### B2B EN 16931 Mandatory Fields (Spanish CIUS)

**B2B EN 16931 Mandatory Fields**

| Field | Description | Required |
| --- | --- | --- |
| Seller NIF | Spanish tax identification number | Yes |
| Buyer NIF | Recipient tax identification number | Yes |
| Invoice type | Must map to Spanish invoice types (F1, F2, etc.) | Yes |
| Tax breakdown | Separate lines per IVA rate + IRPF withholding if applicable | Yes |
| IRPF retention | Professional withholding (retención) details if applicable | Conditional |

In addition to EN 16931 core requirements:

## Section 5 -- Transmission Method

### FACe (B2G)

**FACe (B2G) Transmission Methods**

| Method | Description |
| --- | --- |
| FACe Web Portal | Upload via https://face.gob.es |
| FACe Web Services | SOAP-based automated submission |
| Peppol | Under development for interoperability |

FACe requires three administrative centre codes for routing: Órgano Gestor, Unidad Tramitadora, and Oficina Contable. These are obtained from the contracting public entity.

### SII (Real-Time Reporting)

**SII Real-Time Reporting Transmission**

| Parameter | Detail |
| --- | --- |
| Endpoint | AEAT sede electrónica web services |
| Protocol | SOAP with mutual TLS (client certificate required) |
| Submission deadline | 4 calendar days from invoice date (8 days during 2017 transitional period) |
| Content | Summary invoice data (not full XML invoice) -- libro registro de facturas emitidas/recibidas |
| Certificate | Qualified electronic certificate |

### B2B E-Invoicing (SPFE + Private Platforms)

**B2B E-Invoicing SPFE + Private Platforms**

| Method | Description |
| --- | --- |
| SPFE (Public Solution) | Free public platform operated by AEAT; acts as universal repository |
| Certified private platforms | Must be authorised, interoperable, and connected to SPFE |
| Platform interoperability | All platforms must exchange invoices in any accepted format |
| Invoice statuses | Must report acceptance/rejection and payment status to SPFE within 4 calendar days |

### Veri*factu Transmission

**Veri*factu Transmission**

| Parameter | Detail |
| --- | --- |
| Endpoint | AEAT sede electrónica (production since April 2025) |
| Protocol | REST API with certificate authentication |
| Submission | Real-time, automatic, consecutive transmission of invoice records |
| QR verification | Third parties can scan QR to verify invoice with AEAT |
| Offline fallback | If connectivity fails, records queue with automatic retry |

## Section 6 -- Validation Rules

### FACe Pre-Checks

**FACe Pre-Checks**

| Check | Description |
| --- | --- |
| Schema validation | XML against Facturae 3.2.2 XSD |
| Digital signature | XAdES-EPES signature must be valid and from recognised CA |
| Administrative centre codes | Must match FACe directory entries |
| NIF validation | Seller and buyer tax IDs verified |
| Duplicate detection | Same seller NIF + invoice number + issue date = duplicate |

### SII Validation

**SII Validation**

| Check | Description |
| --- | --- |
| Submission deadline | Must be within 4 calendar days of invoice/registration date |
| NIF validation | Counterparty NIFs verified against census |
| Amount consistency | Tax base × rate must equal reported tax amount |
| Invoice type codes | Must use valid tipo factura codes (F1--F6, R1--R5) |

### Veri*factu Validation

**Veri*factu Validation**

| Check | Description |
| --- | --- |
| Hash chain integrity | SHA-256 hash must reference previous record correctly |
| QR code validity | QR must encode correct AEAT verification URL with invoice reference |
| Sequential numbering | Invoice records must be consecutive without gaps |
| NIF format | Must conform to Spanish NIF/CIF format rules |
| Tax calculations | Base × rate = amount, rounded correctly |

### Common Rejection Reasons

**Common Rejection Reasons**

| Issue | Resolution |
| --- | --- |
| Invalid or expired certificate | Renew qualified electronic certificate |
| Wrong administrative centre codes | Verify codes with the contracting public entity |
| Missing XAdES signature (B2G) | All FACe invoices must be digitally signed |
| Hash chain break (Veri\*factu) | Regenerate chain from last valid record |
| SII late submission | File within 4 days; late submissions incur penalties |

## Section 7 -- Tax Computation Rules

### IVA Rates (2025/2026)

**IVA Rates 2025/2026**

| Rate | Application |
| --- | --- |
| 21% | Standard rate (tipo general) |
| 10% | Reduced rate (tipo reducido) -- food, water, hospitality, transport |
| 4% | Super-reduced rate (tipo superreducido) -- bread, milk, medicines, books |
| 0% | Temporarily applied to essential food items (extended through 2025) |

### IRPF Withholding (Retención)

**IRPF Withholding Rates**

| Scenario | Rate |
| --- | --- |
| Standard professional withholding | 15% |
| New professional (first 3 years) | 7% |

Professional service invoices may include IRPF withholding:

The invoice must show gross amount, IVA, IRPF retention, and net payable separately.

### Rounding

- **Tax per line calculation** — Tax per line: base imponible × tipo impositivo / 100, rounded to 2 decimal places (Standard arithmetic rounding)
- **Invoice total formula** — Invoice total = sum of taxable bases + sum of IVA amounts − sum of retenciones
- **SII/Veri*factu consistency check** — SII and Veri*factu validate that reported amounts are arithmetically consistent

### Multi-Rate Invoice Handling

- **Separate tax block per rate** — Each IVA rate must appear as a separate TaxesOutputs/Tax block (Facturae) or BG-23 group (EN 16931)
- **Exempt operations** — Exempt operations require the applicable exemption cause (e.g., Art. 20 LIVA)  _(Art. 20 LIVA)_
- **Reverse charge** — Reverse charge (inversión del sujeto pasivo) requires explicit mention and IVA = 0%

### Equivalence Surcharge (Recargo de Equivalencia)

**Equivalence Surcharge Rates**

| IVA Rate | Surcharge |
| --- | --- |
| 21% | 5.2% |
| 10% | 1.4% |
| 4% | 0.5% |

For retail businesses under the equivalence surcharge regime:

The surcharge must appear as a separate line in the invoice.

## Section 8 -- Archiving Requirements

**Archiving Requirements**

| Requirement | Detail |
| --- | --- |
| Tax retention | 4 years (Art. 66 Ley General Tributaria) |
| Commercial retention | 6 years (Art. 30 Código de Comercio) |
| Fixed assets | 9 years (extended retention for capital goods IVA adjustments) |
| Format | Original electronic format with integrity and authenticity preserved |
| Digital signature | Archived invoices must retain valid digital signatures or equivalent integrity mechanisms |
| Veri\*factu records | Invoice records (registros de facturación) must be stored immutably with hash chain intact for the full prescription period |
| SPFE archive | The public e-invoicing solution acts as a legal repository for B2B invoices |
| Audit access | Tax authorities may request full access during inspections |

## Section 9 -- Penalties for Non-Compliance

**Penalties for Non-Compliance**

| Violation | Penalty |
| --- | --- |
| Failure to issue/provide B2B e-invoice (Ley 18/2022) | Up to EUR 10,000 per incident (6-month grace period after mandate start) |
| Using non-certified invoicing software (Art. 201 bis LGT) | Up to EUR 50,000 per year for the user |
| Developing/selling non-compliant software | Up to EUR 150,000 per year for the vendor |
| SII late submission | 0.5% of invoice amount per late/incorrect record (min EUR 300, max EUR 6,000 per quarter) |
| SII failure to report | EUR 150 per missing record (max EUR 6,000 per quarter) |
| Failure to maintain archives / tampering | EUR 150 per missing or flawed invoice; higher for serious violations |
| Tax fraud via invoice manipulation | Criminal penalties under Ley General Tributaria |
| Failure to report payment status (B2B) | Subject to penalties under RD 238/2026 (specific amounts pending ministerial order) |

## Section 10 -- Interaction with Tax Skills

### VAT (IVA) Return Integration

- **SII participants**: Invoice data is reported in near real-time via SII, replacing quarterly Modelo 303 informational annexes. SII data pre-populates the annual Modelo 390 summary and feeds into compliance risk assessment.
- **Veri\*factu participants**: Invoice records transmitted to AEAT provide a parallel real-time view of all transactions. AEAT can cross-reference Veri\*factu data with Modelo 303 declarations.
- **B2B e-invoicing**: Invoice data flowing through SPFE will progressively feed into pre-filled VAT returns, similar to Italy's SDI model.

### Income Tax Integration

- Self-employed professionals (autónomos): Invoice data, including IRPF withholdings reported via SII/Veri\*factu, feeds into the annual Modelo 100 (IRPF return)
- The Modelo 130 (quarterly IRPF prepayment) relies on accurate invoice records
- Companies: Corporate income tax (Impuesto sobre Sociedades, Modelo 200) is reconciled against SII/Veri\*factu transaction records

### Withholding Tax Reporting

- IRPF retenciones reported on invoices must reconcile with Modelo 111 (quarterly withholding return) and Modelo 190 (annual summary)
- Veri\*factu invoice records capture retention amounts, enabling automated cross-checks

### Intra-EU and Cross-Border

- Intra-EU supplies are reported via Modelo 349 (recapitulative statement)
- SII captures intra-EU transaction details in the libro registro de facturas
- Cross-border import VAT is managed through customs declarations (DUA) linked to invoice records

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal, gestor administrativo, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
