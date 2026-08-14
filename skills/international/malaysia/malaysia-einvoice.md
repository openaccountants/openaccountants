---
name: malaysia-einvoice
description: Use this skill whenever asked about Malaysia e-invoicing, MyInvois system, LHDN/LHDNM/IRBM e-invoice, Inland Revenue Board Malaysia, UBL 2.1 for Malaysia, e-invoice mandatory timeline, RM threshold phases, MyInvois portal, MyInvois API, e-invoice validation, digital signature for Malaysian e-invoice, self-billed invoice, consolidated invoice, B2B/B2C/B2G e-invoice Malaysia, or any question about generating, submitting, validating, or troubleshooting Malaysian e-invoices. Also trigger when advising on compliance phases, relaxation periods, exemptions, or technical integration with IRBM. ALWAYS read this skill before touching any Malaysia e-invoice work.
version: 1.0
jurisdiction: MY
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: MUHAMMAD HANIS MAT HUSSIN
review_status: current
depends_on:
  - einvoice-workflow-base
category: invoicing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Malaysia Einvoice

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Malaysia |
| Currency | MYR (Malaysian Ringgit) |
| E-Invoicing System | MyInvois |
| Governing Body | Inland Revenue Board of Malaysia (IRBM / LHDNM / LHDN) |
| Key Legislation | Income Tax Act 1967 (Section 82C); Income Tax (Issuance of Electronic Invoice) Rules 2024 [P.U.(A) 265] |
| Schema Standard | UBL 2.1 (Universal Business Language) |
| Format | XML or JSON |
| Model | Continuous Transaction Control (CTC) — validation before use |
| Implementation Start | 1 August 2024 (Phase 1) |
| Current Status | Phase 4 active (RM1M-RM5M from 1 Jan 2026); full enforcement from 1 Jan 2027 |
| Portal | myinvois.hasil.gov.my |
| SDK Documentation | sdk.myinvois.hasil.gov.my |

### Implementation Timeline

**Implementation Timeline**

| Phase | Annual Revenue (FY2022) | Mandatory From | Relaxation Ends | Full Enforcement |
| --- | --- | --- | --- | --- |
| Phase 1 | > RM100 million | 1 August 2024 | 31 January 2025 | Active |
| Phase 2 | RM25M -- RM100M | 1 January 2025 | 30 June 2025 | Active |
| Phase 3 | RM5M -- RM25M | 1 July 2025 | 31 December 2025 | Active |
| Phase 4 | RM1M -- RM5M | 1 January 2026 | 31 December 2026 | 1 January 2027 |
| New businesses (2023-2025, ≥RM1M) | RM1M+ | 1 July 2026 | 31 December 2026 | 1 January 2027 |

### Exemption Threshold

- Businesses with annual turnover below RM1 million are currently exempt
- Revenue determination based on FY2022 Audited Financial Statements (or tax return if no audit required)
- For new businesses commencing from 2026 onwards: mandatory from 1 July 2026 or commencement date (unless first-year revenue < RM1M)

## Section 2 -- Mandate Scope

### Who Must Comply

- All taxpayers carrying on a business in Malaysia whose annual turnover/revenue meets the threshold for their implementation phase
- Covers: companies, sole proprietors, partnerships, LLPs, cooperatives, associations, trusts, and other entities
- Revenue measured from Statement of Comprehensive Income in FY2022 Audited Financial Statements

### Transaction Coverage

**Transaction Coverage**

| Transaction Type | E-Invoice Required |
| --- | --- |
| B2B (business to business) | Yes — individual e-invoice per transaction |
| B2G (business to government) | Yes — individual e-invoice per transaction |
| B2C (business to consumer) | Yes — individual e-invoice for transactions > RM10,000 (from 1 Jan 2026); consolidated for smaller |
| Cross-border (exports) | Yes — e-invoice required |
| Self-billed transactions | Yes — buyer issues self-billed e-invoice |
| Foreign income receipts | Yes — self-billed e-invoice by Malaysian recipient |

### Document Types

**Document Types**

| Type Code | Document | Description |
| --- | --- | --- |
| 01 | Invoice | Standard tax invoice |
| 02 | Credit Note | Adjustment reducing amount |
| 03 | Debit Note | Adjustment increasing amount |
| 04 | Refund Note | Refund document |
| 11 | Self-Billed Invoice | Buyer-issued invoice |
| 12 | Self-Billed Credit Note | Buyer-issued credit note |
| 13 | Self-Billed Debit Note | Buyer-issued debit note |
| 14 | Self-Billed Refund Note | Buyer-issued refund |

### Consolidated E-Invoice (B2C)

- Permitted for B2C transactions where individual e-invoice is not required
- Must be issued within 7 calendar days after month-end
- Aggregate all transactions for the period into a single submission
- From 1 January 2026: individual e-invoice mandatory for B2C transactions exceeding RM10,000

## Section 3 -- Technical Format

### UBL 2.1 Structure

**UBL 2.1 Structure**

| Aspect | Detail |
| --- | --- |
| Standard | Universal Business Language 2.1 (ISO/IEC 19845) |
| Submission Format | XML or JSON (both accepted) |
| Root Element (XML) | `<Invoice>` |
| UBL Namespace | urn:oasis:names:specification:ubl:schema:xsd:Invoice-2 |
| CAC Namespace | urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2 |
| CBC Namespace | urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2 |
| Document Version | v1.1 (current as of 2026) |
| Character Encoding | UTF-8 |

### Data Structure Categories (55 Fields in 8 Groups)

**Data Structure Categories (55 Fields in 8 Groups)**

| Category | Fields Included |
| --- | --- |
| 1. Address | Street, city, state, postal code, country |
| 2. Business Details | TIN, BRN/SST number, MSIC code, tourism tax number |
| 3. Contact Number | Telephone, email |
| 4. Invoice Details | Version, type, code/number, date, time, currency, tax calculation |
| 5. Parties | Supplier and Buyer identification |
| 6. Party Details | Names, addresses, contact information |
| 7. Payment Info | Payment mode, terms, prepayment details |
| 8. Products/Services | Description, quantity, unit price, tax type, tax rate, tax amount, subtotal |

### Digital Signature Requirement

- Every e-invoice must include an issuer's digital signature
- Certificate obtained from IRBM-approved certificate authority (PosDigicert or equivalent)
- Signature embedded in UBL `cac:Signature` element
- XAdES format for XML; equivalent JSON structure for JSON submissions

## Section 4 -- Mandatory Fields

### Invoice Header

**Invoice Header**

| UBL Path | Field Name | Description | Example |
| --- | --- | --- | --- |
| cbc:InvoiceTypeCode/@listVersionID | e-Invoice Version | Current version | 1.1 |
| cbc:InvoiceTypeCode | e-Invoice Type Code | Document type | 01 |
| cbc:ID | e-Invoice Code/Number | Unique reference | INV-2026-001 |
| cbc:IssueDate | Issue Date | UTC date | 2026-05-22 |
| cbc:IssueTime | Issue Time | UTC time | 15:30:00Z |
| cbc:DocumentCurrencyCode | Currency Code | ISO 4217 | MYR |
| cac:Signature | Digital Signature | Issuer signature | (embedded) |

### Supplier (cac:AccountingSupplierParty)

**Supplier (cac:AccountingSupplierParty)**

| Field | Description | Mandatory |
| --- | --- | --- |
| TIN | Tax Identification Number | Yes |
| BRN / NRIC / Passport | Registration/ID number | Yes |
| SST Registration Number | Sales & Service Tax number | If registered |
| Tourism Tax Registration | Tourism tax number | If applicable |
| MSIC Code | Malaysian Standard Industrial Classification | Yes |
| Name | Legal name | Yes |
| Address | Full address (street, city, state, postal code) | Yes |
| Contact (Phone) | Telephone number | Yes |
| Contact (Email) | Email address | Yes |
| Country | Country code | Yes (MY) |
| State | State code (per IRBM code table) | Yes |

### Buyer (cac:AccountingCustomerParty)

**Buyer (cac:AccountingCustomerParty)**

| Field | Description | Mandatory |
| --- | --- | --- |
| TIN | Tax Identification Number | Yes |
| BRN / NRIC / Passport | Registration/ID number | Yes |
| SST Registration Number | Sales & Service Tax number | If applicable |
| Name | Legal name or individual name | Yes |
| Address | Full address | Yes |
| Contact (Phone) | Telephone number | Yes |
| Country | Country code | Yes |

### Line Items (cac:InvoiceLine)

**Line Items (cac:InvoiceLine)**

| Field | Description | Mandatory |
| --- | --- | --- |
| Item Classification Code | IRBM classification code | Yes |
| Item Description | Product/service description | Yes |
| Unit Price | Price per unit | Yes |
| Quantity | Number of units | Yes |
| Measurement (Unit) | Unit of measure | Yes |
| Subtotal | Line amount (Qty × Unit Price) | Yes |
| Tax Type | Tax category (01=SST, 02=Service Tax, E=Exempt, etc.) | Yes |
| Tax Rate | Applicable percentage | Yes (if taxable) |
| Tax Amount | Calculated tax | Yes (if taxable) |
| Total Excluding Tax | Line total before tax | Yes |
| Total Including Tax | Line total with tax | Yes |

### Totals

**Totals**

| Field | Description |
| --- | --- |
| Total Excluding Tax | Sum of all line totals before tax |
| Total Tax Amount | Sum of all tax amounts |
| Total Including Tax | Grand total |
| Total Payable Amount | Amount due from buyer |

## Section 5 -- Transmission Method

### Submission Channels

**Submission Channels**

| Channel | Description | Use Case |
| --- | --- | --- |
| MyInvois Portal | Web-based manual submission | Low volume (< 50 invoices/month) |
| System-to-System API | Direct API integration | Medium-to-high volume |
| ERP/Accounting Software | Pre-built integration via middleware | Enterprise |

### API Endpoints (Production)

**API Endpoints (Production)**

| Endpoint | Method | Purpose |
| --- | --- | --- |
| /api/v1.0/login/taxpayer | POST | Authenticate via OAuth 2.0 (client credentials) |
| /api/v1.0/login/intermediary | POST | Authenticate as intermediary system |
| /api/v1.0/documentsubmissions | POST | Submit e-invoice(s) for validation |
| /api/v1.0/documents/{uuid}/details | GET | Retrieve validated document |
| /api/v1.0/documents/{uuid}/cancel | PUT | Cancel an e-invoice |
| /api/v1.0/documents/{uuid}/reject | PUT | Reject received e-invoice (buyer) |
| /api/v1.0/documents/search | GET | Search submitted documents |
| /api/v1.0/documents/{uuid}/qrcode | GET | Get QR code for document |

### Base URLs

**Base URLs**

| Environment | URL |
| --- | --- |
| Production | https://myinvois.hasil.gov.my |
| Sandbox | https://preprod-api.myinvois.hasil.gov.my |
| SDK Portal | https://sdk.myinvois.hasil.gov.my |

### Authentication

- OAuth 2.0 Client Credentials flow
- Client ID and Client Secret obtained from MyInvois portal
- Token validity: 1 hour
- Intermediary systems can act on behalf of multiple taxpayers

### Validation Flow

1. Supplier generates e-invoice in UBL 2.1 XML/JSON format
2. Supplier signs the document with digital signature
3. Submit to IRBM via API or portal
4. IRBM validates structure, data, digital signature
5. If valid: IRBM assigns unique identifier + validation timestamp
6. Validated e-invoice shared with buyer (via MyInvois or direct)
7. Buyer has 72 hours to reject (if disputed)

## Section 6 -- Validation Rules

### IRBM Validation Checks

1. **Schema validation** — Conforms to UBL 2.1 structure per MyInvois SDK specification
2. **Mandatory field completeness** — All 55 required fields present
3. **Digital signature verification** — Valid certificate from approved authority
4. **TIN validation** — Both supplier and buyer TIN must be valid and active
5. **BRN/NRIC consistency** — Must match IRBM records
6. **Tax calculation** — Tax amounts must equal rate × base (within tolerance)
7. **Code table validation** — MSIC codes, state codes, currency codes, tax types must be from valid lists
8. **Duplicate check** — Same document ID from same supplier not accepted twice
9. **Date/time validation** — Must be in UTC; not future-dated beyond tolerance

### Validation Statuses

**Validation Statuses**

| Status | Meaning |
| --- | --- |
| Submitted | Received, awaiting validation |
| Valid | Passed all checks; legally valid e-invoice |
| Invalid | Failed validation; must correct and resubmit |
| Cancelled | Cancelled by supplier (within permitted window) |
| Rejected | Rejected by buyer (within 72 hours of validation) |

### Common Rejection Reasons

**Common Rejection Reasons**

| Error | Description | Resolution |
| --- | --- | --- |
| Invalid TIN | TIN not found or inactive | Verify TIN at IRBM portal |
| Missing mandatory field | Required field absent | Add missing field per SDK spec |
| Invalid digital signature | Certificate expired or unrecognized | Renew certificate from approved CA |
| Tax calculation mismatch | Computed tax ≠ stated tax | Recalculate: TaxAmount = Rate × Base |
| Invalid classification code | Item code not in IRBM table | Look up correct code in classification list |
| Duplicate submission | Same ID already validated | Use unique invoice number |

## Section 7 -- Tax Computation Rules

### Applicable Taxes

**Applicable Taxes**

| Tax Type | Code | Rate | Applicable To |
| --- | --- | --- | --- |
| Sales Tax | 01 | 5% or 10% | Manufactured/imported goods |
| Service Tax | 02 | 6% or 8% | Prescribed services |
| Tourism Tax | 03 | RM10/room/night | Accommodation |
| Exempt | E | 0% | Exempted goods/services |
| Not Applicable | 06 | 0% | Out of scope |

### Calculation Rules

- **Line Tax Amount formula** — Line Tax Amount = Taxable Amount × Tax Rate / 100; Rounding: 2 decimal places (standard rounding); Document-level Tax Total = sum of all line tax amounts; Total Including Tax = Total Excluding Tax + Total Tax Amount; Multiple tax types can appear on same invoice (different lines)  _(Section 7 -- Tax Computation Rules)_

### Multi-Rate Invoice

- Each line item carries its own Tax Type and Tax Rate
- Invoice totals aggregate across all tax types
- Self-billed invoices follow same calculation rules

### Discount/Charge Handling

- Discounts applied at line level (reduce Unit Price or add discount element)
- Charges (e.g., freight, handling) added as separate line items or invoice-level charges
- Tax calculated on net amount (after discount, before charges where applicable)

### Foreign Currency

- If DocumentCurrencyCode ≠ MYR, include exchange rate
- Tax amounts may need to be expressed in MYR for SST purposes
- Use Bank Negara Malaysia published rates

## Section 8 -- Archiving Requirements

**Section 8 -- Archiving Requirements**

| Requirement | Detail |
| --- | --- |
| Retention Period | 7 years from end of the year of assessment (Income Tax Act 1967) |
| Format | Original validated XML/JSON (with IRBM validation response) |
| Accessibility | Must be retrievable from MyInvois portal; also maintain own copy |
| Digital Signature | Preserved within the document |
| QR Code | Generated by IRBM post-validation; contains link to verify e-invoice |
| Buyer Copy | Buyer can access validated e-invoice via MyInvois portal |
| Cancellation Records | Cancelled e-invoices remain in system with cancelled status |
| Medium | Electronic storage acceptable; no paper copy required for tax purposes |
| Audit | IRBM can request access to any e-invoice via MyInvois system directly |

## Section 9 -- Penalties for Non-Compliance

**Section 9 -- Penalties for Non-Compliance**

| Violation | Penalty | Legal Basis |
| --- | --- | --- |
| Failure to issue e-invoice | RM200 -- RM20,000 fine per instance OR up to 6 months imprisonment | Section 82C, Income Tax Act 1967 |
| Issuing e-invoice with incorrect information | RM200 -- RM20,000 fine per instance | Section 82C |
| Late submission | Subject to penalty after relaxation period ends | P.U.(A) 265 |
| Repeated non-compliance | Higher end of penalty range; potential prosecution | Income Tax Act 1967 |

### Relaxation Period

- During relaxation period for each phase, IRBM will not impose penalties
- Relaxation is for technical adaptation — taxpayers should still attempt compliance
- Phase 4 relaxation: 1 January 2026 -- 31 December 2026 (full enforcement from 1 January 2027)

### Buyer Impact

- Buyers may not claim tax deductions without valid e-invoice from supplier
- Self-billed e-invoices required for certain expense types (foreign services, employee benefits)

## Section 10 -- Interaction with Tax Skills

### Corporate Income Tax (Form C)

- Revenue reported in Form C must align with e-invoices issued via MyInvois
- IRBM can cross-reference declared revenue against total validated e-invoices
- Deductions must be supported by received/self-billed e-invoices

### SST Return

- Sales Tax and Service Tax amounts declared in SST-02 return derived from e-invoice data
- IRBM reconciles SST return against e-invoice tax totals
- Discrepancies may trigger audit or penalty

### Transfer Pricing

- Cross-border e-invoices provide documentation for transfer pricing compliance
- Self-billed e-invoices for foreign services create audit trail

### Withholding Tax (Section 109)

- Payments to non-residents requiring withholding tax must have corresponding e-invoice
- Self-billed e-invoice issued by Malaysian payer for non-resident service providers

### Real Property Gains Tax (RPGT)

- Property transactions require e-invoice issuance
- Captures transaction value for RPGT assessment

### Employer Obligations

- Benefits-in-kind and perquisites to employees may require e-invoice/self-billed e-invoice
- Medical benefits, club memberships, accommodation: reportable via e-invoice system
- Links to Form EA/EC employee reporting

### Audit Trail

- IRBM maintains centralized record of all validated e-invoices
- Full digital audit trail from issuance to payment
- Reduces paper-based audit requirements; enables data-driven risk assessment

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a tax agent, chartered accountant, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
