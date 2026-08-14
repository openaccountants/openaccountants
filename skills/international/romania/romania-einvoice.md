---
name: romania-einvoice
description: Use this skill whenever asked about e-invoicing in Romania, RO e-Factura, ANAF electronic invoice system, SPV (Spațiul Privat Virtual), B2B e-invoice clearance model, UBL 2.1 Romania, CIUS-RO, XML invoice validation, or any question about issuing, transmitting, validating, or archiving electronic invoices under Romanian law. Trigger on phrases like "e-Factura", "RO e-Factura", "ANAF invoice", "SPV portal", "CIUS-RO", "B2B clearance Romania", "B2C e-invoice Romania", "OUG 115/2023", "EN 16931 Romania", or "invoice validation ANAF". ALWAYS read this skill before touching any Romania invoicing compliance work.
version: 1.0
jurisdiction: RO
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - einvoice-workflow-base
category: invoicing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Romania Einvoice

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Romania (România) |
| Currency | RON (domestic); EUR accepted for cross-border |
| E-invoicing system name | RO e-Factura (Sistemul național privind factura electronică) |
| Governing body | Agenția Națională de Administrare Fiscală (ANAF) / Ministry of Finance (MF) |
| Key legislation | OUG 120/2021 (system establishment); OUG 115/2023 (B2B mandate); OUG 69/2024, OUG 138/2024 (B2C extension); Ordinul MF 1.366/2021 (CIUS-RO); Codul Fiscal Art. 319 |
| Implementation timeline | B2G Nov 2021; High-risk B2B Jul 2022; All B2B Jan 2024 (reporting) / Jul 2024 (clearance); B2C Jan 2025 |
| Current status (2026) | Centralised clearance model: B2B and B2G fully mandatory; B2C mandatory for established taxpayers; XML-only invoicing through ANAF platform |
| Skill version | 1.0 |

## Section 2 -- Mandate Scope

### Who Must Comply

- **B2G (Business-to-Government)** — All suppliers to Romanian public institutions must issue e-invoices via RO e-Factura. Mandatory since November 2021 for voluntary adoption, compulsory since July 2022.
- **B2B (Business-to-Business)** — All taxable persons established in Romania (VAT-registered or not) must transmit invoices through RO e-Factura for domestic supplies of goods and services with place of supply in Romania. Non-resident entities registered for VAT in Romania must also comply. Since July 2024, this operates as a centralised exchange clearance model -- an invoice is not legally valid until ANAF validates it.
- **B2C (Business-to-Consumer)** — Mandatory from 1 January 2025 for Romanian-established taxpayers. Simplified invoices under Art. 319(12) of the Fiscal Code are exempt. Grace period for penalties ran until 31 March 2025. Certain entities (small taxpayers, non-profits, farmers under special regimes) had until 1 July 2025 to comply.  _(Art. 319(12) of the Fiscal Code)_

### Thresholds and Exemptions

- **No turnover threshold** — No turnover threshold -- all taxable persons established in Romania must comply.
- **Exempt intra-community/exports/outside-RO services** — Exempt: invoices for intra-community supplies, exports, services taxed outside Romania.
- **Exempt OSS transactions** — Exempt: transactions within the OSS (One-Stop Shop) regime.
- **Simplified invoices via electronic cash registers** — Simplified invoices issued via electronic cash registers are exempt from RO e-Factura but require fiscal memory compliance.

### Timeline Phases

**Timeline Phases**

| Date | Milestone |
| --- | --- |
| November 2021 | RO e-Factura launched for B2G and voluntary B2B |
| July 2022 | B2G and high-risk B2B (fruit, vegetables, alcohol, mineral water, construction, new buildings) mandatory |
| January 2024 | All B2B reporting mandatory (5 working day submission window) |
| July 2024 | B2B clearance model active -- invoice legally valid only after ANAF validation |
| January 2025 | B2C e-invoicing mandatory for established taxpayers |
| July 2025 | Remaining B2C exemptions expire (non-profits, small farmers) |

## Section 3 -- Technical Format

### Invoice Format

- **Accepted syntaxes** — Romania follows the European standard EN 16931 and accepts two syntaxes: - **UBL 2.1** (OASIS Universal Business Language) -- the primary and most common format - **CII** (UN/CEFACT Cross-Industry Invoice) -- accepted but rarely used  _(EN 16931)_

### National CIUS

- **CIUS-RO** — CIUS-RO (Core Invoice Usage Specification -- Romania) defines national business rules on top of EN 16931. Current version: ro16931-ubl-1.0.9 (effective from 5 June 2024). CIUS-RO specifies: - Mandatory Romanian fiscal identifiers (CUI/CIF) - Romanian-specific tax category codes - National validation schematrons (operational rules + VAT rules + code list rules) - Required document type codes for invoices and credit notes  _(CIUS-RO ro16931-ubl-1.0.9, effective 5 June 2024)_

### Schema and Namespaces

**Schema and Namespaces**

| Component | Value |
| --- | --- |
| UBL 2.1 Invoice schema | `UBL-Invoice-2.1.xsd` |
| UBL 2.1 CreditNote schema | `UBL-CreditNote-2.1.xsd` |
| EN 16931 schematron | CEN/TC 434 base rules |
| CIUS-RO schematron | `ro16931-ubl-1.0.9.sch` |
| Primary namespace | `urn:oasis:names:specification:ubl:schema:xsd:Invoice-2` |
| Common components | `urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2` |

## Section 4 -- Mandatory Fields

### Fields Required by CIUS-RO (Beyond EN 16931 Baseline)

**Fields Required by CIUS-RO (Beyond EN 16931 Baseline)**

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

### B2C-Specific Fields

- **B2C buyer identification and upload endpoint** — For B2C e-reporting (from 2025), the buyer identification uses a unique identifier. On the test/production platform, a dedicated B2C upload endpoint is used (mandatory since 31 March 2025).

## Section 5 -- Transmission Method

### RO e-Factura Platform (SPV)

**RO e-Factura Platform (SPV)**

| Channel | Detail |
| --- | --- |
| SPV web portal | Manual upload of XML invoices at anaf.ro → Factura electronică → Trimitere Factură |
| REST API | Automated submission via ANAF web services; separate endpoints for B2B/B2G and B2C |
| Authentication | Qualified digital certificate (semnătură electronică calificată) registered in SPV |
| Submission deadline | 5 calendar days from invoice issuance (but no later than 5 calendar days from the legal deadline for issuance under Art. 319(16) Fiscal Code) |
| Recipient download | Buyer must download validated invoice within 60 days |
| Download availability | Validated XML available for download for 60 days; after that, archived and available on request |

### API Workflow

- **API Workflow steps** — 1. **Authenticate** with qualified digital certificate via SPV 2. **Upload** XML invoice to the appropriate endpoint (B2B/B2G or B2C) 3. **Receive** upload confirmation with upload index ID 4. **ANAF validates** the invoice (schema + CIUS-RO + business rules) 5. **Download** validation result: status = "ok" (validated) or "nok" (rejected with error codes) 6. **For B2B clearance (post-July 2024):** validated invoice = legally issued invoice; buyer retrieves from RO e-Factura

### API Rate Limits

ANAF enforces API call limits. Consult the current "Limite Apeluri API" documentation on the MF technical page for throttling thresholds.

## Section 6 -- Validation Rules

### ANAF Validation Process

- **Validation steps** — Upon upload, ANAF performs: 1. **XML schema validation** against UBL 2.1 or CII XSD 2. **EN 16931 base rule validation** (CEN/TC 434 schematrons) 3. **CIUS-RO rule validation** (national schematrons for operational rules, VAT rules, code lists) 4. **Business rule validation** (NIF/CUI validity, duplicate check, date consistency) 5. **Return status**: validated (with download ID for buyer) or rejected (with error details)

### Pre-Submission Checks

- **Pre-submission checklist** — - Validate XML locally against UBL 2.1 XSD and CIUS-RO schematron before uploading - Verify CUI/CIF validity using ANAF's public API - Ensure invoice number uniqueness within your series - Confirm tax point date and issue date are consistent - Verify VAT rates match current Romanian rates

### Common Rejection Reasons

**Common Rejection Reasons**

| Reason | Detail |
| --- | --- |
| Schema violation | XML does not conform to UBL 2.1 XSD |
| CIUS-RO rule failure | National business rule violation (e.g., missing Romanian tax ID format) |
| Invalid CUI/CIF | Tax identification number fails ANAF validation |
| Duplicate invoice | Invoice number already submitted for the same supplier |
| Invalid tax category | Tax code does not match VAT treatment |
| Missing mandatory field | Required element absent or empty |
| Date inconsistency | Issue date after upload date, or tax point date mismatch |

## Section 7 -- Tax Computation Rules

### VAT Rates (2026)

**VAT Rates (2026)**

| Rate | Percentage | Application |
| --- | --- | --- |
| Standard | 19% | Most goods and services |
| Reduced 1 | 9% | Foodstuffs, water supply, medicines, hotel accommodation, restaurant services |
| Reduced 2 | 5% | Social housing (under thresholds), cultural events, certain children's products |
| Exempt with credit | 0% | Intra-community supplies, exports |
| Exempt without credit | 0% | Financial services, insurance, education, healthcare |

### Rounding Rules

- **VAT rounding and multi-currency** — - VAT amounts calculated per line, rounded to 2 decimal places (RON bani or EUR cents). - Line totals summed; total VAT is the sum of rounded line-level VAT amounts. - For multi-currency invoices: amounts must appear in the document currency; if not RON, the BNR (National Bank of Romania) exchange rate on the tax point date applies.

### Multi-Rate Invoice Handling

- **Multi-rate handling** — Each VAT rate requires a separate `cac:TaxSubtotal` element within `cac:TaxTotal`. Tax base and tax amount must be stated per rate category.

### Credit Notes

- **Credit note requirements** — Credit notes must reference the original invoice number in `cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID`. The invoice type code is 381. Negative amounts are expressed as positive values on the credit note (the document type signals the reversal).

## Section 8 -- Archiving Requirements

**Archiving Requirements**

| Requirement | Detail |
| --- | --- |
| Retention period | 10 years from the end of the fiscal year in which the invoice was issued |
| Format | Original XML as validated by ANAF (the validated XML is the legally binding document for B2B clearance) |
| Accessibility | Must be available for tax inspection on demand throughout retention period |
| ANAF download window | Validated invoices available on RO e-Factura for 60 days; after expiry, must be retrieved via archive request |
| Buyer obligation | Buyer must download and archive the validated XML within 60 days |
| Integrity | Digital certificate chain must remain verifiable; no modifications to the validated XML |
| Location | May be stored within the EU; storage outside Romania requires notification to ANAF |
| Conversion to PDF | ANAF provides XML-to-PDF conversion tools; the PDF is for human readability only and is not the legal document |

## Section 9 -- Penalties for Non-Compliance

### Late or Missing Submission Penalties

**Late or Missing Submission Penalties**

| Taxpayer Category | Fine per Incident (RON) |
| --- | --- |
| Large taxpayers (contribuabili mari) | 5,000 -- 10,000 |
| Medium taxpayers (contribuabili mijlocii) | 2,500 -- 5,000 |
| Small taxpayers and individuals | 1,000 -- 2,500 |

### Additional Penalties

**Additional Penalties**

| Violation | Penalty |
| --- | --- |
| Receiving/registering a B2B invoice not transmitted via RO e-Factura (buyer penalty) | 15% of the total invoice value |
| Failure to issue invoice via RO e-Factura for in-scope B2B transactions | Fine equal to the VAT amount on the invoice |
| B2C non-compliance (post-grace period) | Same graduated fines as above by taxpayer category |

### Consequences Beyond Fines

- **Non-fine consequences** — - Loss of VAT deduction rights for invoices not properly issued/received through RO e-Factura - Increased audit risk from ANAF's risk-analysis system - Buyer notification right: if a buyer does not receive the invoice via RO e-Factura within the legal deadline, they can notify ANAF, triggering enforcement action against the supplier

## Section 10 -- Interaction with Tax Skills

### RO e-Factura → VAT Return (Declarația 300)

- **e-Factura pre-populating VAT return** — ANAF uses RO e-Factura data to pre-populate the draft VAT return (RO e-TVA initiative). From 2024, ANAF cross-references e-Factura submissions against VAT declarations. Discrepancies trigger automated notifications and potential audits.

### RO e-Factura → RO e-TVA

- **RO e-TVA pre-filled VAT return** — The RO e-TVA system provides taxpayers with a pre-filled VAT return based on RO e-Factura data, RO e-Transport data, and customs declarations. Taxpayers must review and adjust before submission.

### RO e-Factura → SAF-T (D406)

- **SAF-T cross-checks** — Romania also requires SAF-T reporting (Declarația 406) for large and medium taxpayers. Invoice data from RO e-Factura should be consistent with SAF-T submissions. ANAF cross-checks between the two systems.

### RO e-Transport Integration

- **e-Transport consistency requirement** — For goods movements, RO e-Transport operates alongside RO e-Factura. Transport documents and invoices must carry consistent references. Goods in transit without matching e-Transport declarations face confiscation risk.

### Corporate Tax (Impozit pe profit)

- **Corporate tax data feed** — Invoice data feeds into corporate tax assessments. ANAF uses e-Factura data to verify revenue declarations and deduction claims.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
