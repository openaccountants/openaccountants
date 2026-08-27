---
name: belgium-einvoice
description: Use this skill whenever asked about e-invoicing in Belgium, Peppol B2B mandate, Mercurius platform for B2G, Hermes platform, EN 16931 Belgium, Peppol BIS Billing 3.0 Belgium, structured electronic invoices, Belgian VAT e-invoicing, Peppol Access Points, or any question about issuing, transmitting, validating, or archiving electronic invoices under Belgian law. Trigger on phrases like "Peppol Belgium", "e-invoicing Belgium 2026", "Mercurius", "Hermes platform", "B2B e-invoice Belgium", "structured invoice Belgium", "Belgian VAT Code invoicing", "Peppol BIS", "UBL Belgium", or "e-facturatie". ALWAYS read this skill before touching any Belgium invoicing compliance work.
version: 1.0
jurisdiction: BE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - einvoice-workflow-base
category: invoicing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Belgium Einvoice

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Belgium (Koninkrijk België / Royaume de Belgique) |
| Currency | EUR |
| E-invoicing system name | Peppol network (B2B); Mercurius platform (B2G); Hermes bridge (transitional) |
| Governing body | FPS Finance (Federale Overheidsdienst Financiën / Service Public Fédéral Finances) |
| Key legislation | Law of 6 February 2024 amending the Belgian VAT Code (Art. 53 §1/1); Royal Decree of 8 July 2025 on structured e-invoicing (technical standards and penalties); EU Directive 2014/55/EU (B2G); Belgian VAT Code Art. 44 (exemptions) |
| Implementation timeline | B2G via Mercurius since 2015+; B2B mandate 1 Jan 2026; Grace period ended 31 Mar 2026; Full enforcement from 1 Apr 2026; Self-billing tolerance until 30 Jun 2026 |
| Current status (2026) | Fully enforced -- all Belgian VAT-registered businesses must send and receive Peppol BIS Billing 3.0 invoices for domestic B2B transactions; progressive penalties in effect |
| Skill version | 1.0 |

## Section 2 -- Mandate Scope

### Who Must Comply

- **B2G compliance requirement** — All suppliers to Belgian contracting authorities must issue structured e-invoices via the Mercurius platform (aligned with Peppol). In effect since the transposition of EU Directive 2014/55/EU. All federal, regional, and local public entities receive through Mercurius.  _(EU Directive 2014/55/EU)_
- **B2B compliance requirement** — From 1 January 2026, all Belgian enterprises liable to VAT must use structured e-invoices for domestic B2B transactions. A PDF sent by email or paper invoice no longer satisfies the legal invoicing requirement for in-scope transactions.
- **Suppliers in scope** — All Belgian VAT taxpayers including: Taxable entities established in Belgium; Belgian permanent establishments of foreign entities; Members of Belgian VAT groups; Taxable Belgian entities with special VAT schemes in agriculture
- **Suppliers excluded** — Foreign entities solely registered for VAT in Belgium (without establishment); Belgian entities conducting only VAT-exempt activities (Art. 44 VAT Code); Bankrupt entities; Entities under the special flat-rate scheme (to be abolished in 2028)  _(Art. 44 VAT Code)_
- **Customers in scope** — Taxable entities providing their Belgian VAT number for local transactions.
- **Customers excluded** — VAT-exempt entities and foreign taxpayers with a Belgian VAT number.
- **B2C treatment** — Remains voluntary. No mandatory e-invoicing obligation for B2C transactions.

### Transaction Scope

- **In scope transactions** — E-invoicing applies to all domestic B2B VAT transactions in Belgium, including: Supplies of goods and services with Belgian place of supply; Supplies under local reverse charge
- **Not in scope transactions** — Intra-community supplies; Services taxed in another EU country; Transactions exempt under Art. 44 of the Belgian VAT Code  _(Art. 44 of the Belgian VAT Code)_

### Timeline

**Timeline**

| Date | Milestone |
| --- | --- |
| 2015+ | Mercurius platform deployed for B2G e-invoicing |
| 1 February 2024 | Parliament approves law for mandatory B2B e-invoicing from 2026 |
| 8 July 2025 | Royal Decree published with technical standards and penalty regime |
| 1 January 2026 | B2B e-invoicing mandate takes effect; 3-month tolerance period begins |
| 31 March 2026 | Tolerance period ends; full enforcement begins |
| 30 June 2026 | Self-billing tolerance period ends |
| 1 January 2028 | Peppol five-corner e-reporting model anticipated (near real-time VAT e-reporting) |

## Section 3 -- Technical Format

### Standard and Syntax

**Standard and Syntax**

| Component | Value |
| --- | --- |
| Semantic standard | EN 16931 (European standard for electronic invoicing) |
| Default syntax | UBL 2.1 XML (OASIS Universal Business Language) |
| Business specification | Peppol BIS Billing 3.0 |
| Self-billing specification | Peppol BIS Self-Billing 3.0.1 (hotfix March 2026) |
| CIUS | No separate Belgian CIUS beyond Peppol BIS Billing 3.0 |
| CII syntax | Accepted via Mercurius but rarely used in practice; UBL is the default |

### Key Peppol Identifiers

**Key Peppol Identifiers**

| Field | Value |
| --- | --- |
| CustomizationID | `urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0` |
| ProfileID | `urn:fdc:peppol.eu:2017:poacc:billing:01:1.0` |
| Document type (Invoice) | `urn:oasis:names:specification:ubl:schema:xsd:Invoice-2::Invoice##urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0::2.1` |
| Document type (Credit Note) | `urn:oasis:names:specification:ubl:schema:xsd:CreditNote-2::CreditNote##urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0::2.1` |

### Namespaces

**Namespaces**

| Namespace | URI |
| --- | --- |
| UBL Invoice | `urn:oasis:names:specification:ubl:schema:xsd:Invoice-2` |
| UBL CreditNote | `urn:oasis:names:specification:ubl:schema:xsd:CreditNote-2` |
| Common Basic Components | `urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2` |
| Common Aggregate Components | `urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2` |

## Section 4 -- Mandatory Fields

### Peppol BIS Billing 3.0 Required Fields

**Peppol BIS Billing 3.0 Required Fields**

| Field | UBL Path | Notes |
| --- | --- | --- |
| Invoice number | `cbc:ID` | Unique, sequential |
| Issue date | `cbc:IssueDate` | ISO 8601 |
| Invoice type code | `cbc:InvoiceTypeCode` | 380 (invoice), 381 (credit note) |
| Currency code | `cbc:DocumentCurrencyCode` | EUR for domestic |
| Buyer reference | `cbc:BuyerReference` | Mandatory in Peppol BIS; can be PO number or free text |
| Supplier name | `cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationName` |  |
| Supplier VAT number | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | Belgian VAT number format: BE0XXX.XXX.XXX |
| Supplier address | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress` | Including country code |
| Supplier Peppol endpoint | `cac:AccountingSupplierParty/cac:Party/cbc:EndpointID` | With `@schemeID` (e.g., 0208 for Belgian enterprise number) |
| Buyer name | `cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationName` |  |
| Buyer VAT number | `cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | Belgian VAT number |
| Buyer address | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress` | Including country code |
| Buyer Peppol endpoint | `cac:AccountingCustomerParty/cac:Party/cbc:EndpointID` | Must be registered in Peppol SMP |
| Line item description | `cac:InvoiceLine/cac:Item/cbc:Name` |  |
| Line quantity | `cac:InvoiceLine/cbc:InvoicedQuantity` | With `@unitCode` (UN/ECE Rec. 20) |
| Line net amount | `cac:InvoiceLine/cbc:LineExtensionAmount` |  |
| Line VAT category | `cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:ID` | S, Z, E, AE, K, G, O, L, M |
| Line VAT rate | `cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` |  |
| Tax subtotals | `cac:TaxTotal/cac:TaxSubtotal` | Per VAT category |
| Total tax amount | `cac:TaxTotal/cbc:TaxAmount` |  |
| Payable amount | `cac:LegalMonetaryTotal/cbc:PayableAmount` |  |
| Payment means | `cac:PaymentMeans/cbc:PaymentMeansCode` | 30 (credit transfer), 58 (SEPA), etc. |
| Payment account (IBAN) | `cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` |  |

### Peppol VAT Category Codes (Belgian Relevance)

**Peppol VAT Category Codes (Belgian Relevance)**

| Code | Meaning |
| --- | --- |
| S | Standard rate (21%), reduced (12%, 6%) |
| Z | Zero rated |
| E | Exempt from VAT |
| AE | VAT Reverse Charge |
| K | Intra-community supply |
| G | Export outside the EU |
| O | Not subject to VAT |

## Section 5 -- Transmission Method

### B2B: Peppol Network

**B2B: Peppol Network**

| Component | Detail |
| --- | --- |
| Network | Peppol eDelivery Network (4-corner model) |
| Sender Access Point | Certified Peppol Access Point used by the supplier |
| Receiver Access Point | Certified Peppol Access Point used by the buyer |
| Endpoint lookup | Peppol SMP (Service Metadata Publisher) directory |
| Participant ID | Belgian enterprise number (KBO/BCE) with scheme 0208, or VAT number with scheme 9925 |
| Protocol | Peppol AS4 profile |
| Authentication | Peppol PKI certificates issued by OpenPeppol CA |

### B2G: Mercurius Platform

**B2G: Mercurius Platform**

| Component | Detail |
| --- | --- |
| Platform | Mercurius -- central mailroom for all Belgian public entities |
| Alignment | Fully integrated into the Peppol ecosystem |
| Web portal | Manual invoice submission available via Mercurius web portal |
| Automated submission | Via Peppol Access Point to the Mercurius endpoint |
| Track and trace | Mercurius portal provides delivery tracking for senders and receivers |
| Alternative | Hermes platform (transitional bridge for entities not yet able to process structured invoices; converts to PDF) |

### Hermes Bridge (Transitional)

Hermes is a temporary platform that converts structured Peppol e-invoices into human-readable formats (PDF) for recipients not yet technically equipped. Hermes is designed to be phased out as digital maturity increases. It also includes a web portal with tracking features.

## Section 6 -- Validation Rules

### Peppol Validation Layers

- **Validation layers** — 1. XML schema validation against UBL 2.1 XSD. 2. EN 16931 business rules (CEN/TC 434 schematrons). 3. Peppol BIS Billing 3.0 rules (OpenPeppol schematrons). 4. Access Point validation (transport-level checks: endpoint existence in SMP, document type support)

### Pre-Submission Checks

- **Pre-submission checks** — Validate XML against UBL 2.1 schema and Peppol BIS 3.0 schematron before sending; Verify buyer Peppol endpoint is registered in the SMP directory; Confirm VAT category codes match the correct Belgian VAT treatment; Ensure BuyerReference is populated (mandatory in Peppol BIS); Verify Belgian VAT number format (BE + 10 digits, check digit valid)

### Common Rejection Reasons

**Common Rejection Reasons**

| Reason | Detail |
| --- | --- |
| Endpoint not found | Buyer is not registered in the Peppol SMP directory |
| Schema violation | XML does not conform to UBL 2.1 XSD |
| Business rule failure | Peppol BIS or EN 16931 schematron rule violated |
| Missing BuyerReference | `cbc:BuyerReference` is empty or absent |
| Invalid VAT category | Tax category code does not match the VAT rate or transaction type |
| Invalid VAT number | Belgian VAT number fails format or check-digit validation |
| Unsupported document type | Document type ID not registered for the receiver in SMP |
| Duplicate invoice | Invoice number already sent to the same buyer |

## Section 7 -- Tax Computation Rules

### Belgian VAT Rates (2026)

**Belgian VAT Rates (2026)**

| Rate | Percentage | Application |
| --- | --- | --- |
| Standard | 21% | Most goods and services |
| Reduced (parking) | 12% | Certain social housing, restaurant meals (food portion), margarine, tyres |
| Reduced | 6% | Basic necessities, water, pharmaceuticals, books, cultural events, renovations (conditions apply), passenger transport |
| Zero | 0% | Intra-community supplies, exports, newspapers/periodicals (from 2023) |

### Rounding Rules

- **Rounding rules** — VAT calculated per line, rounded to 2 decimal places (EUR cents). Totals are the algebraic sum of rounded line-level amounts. cac:TaxTotal/cbc:TaxAmount must equal the sum of all cac:TaxSubtotal/cbc:TaxAmount values. Peppol BIS enforces rounding tolerance: ±0.01 per tax subtotal.

### Multi-Rate Invoice Handling

- **Multi-rate invoice handling** — Each VAT rate requires a separate cac:TaxSubtotal element. Each invoice line must reference exactly one cac:ClassifiedTaxCategory. Mixed-rate invoices must not combine rates within a single line.

### Self-Billing

- **Self-billing rule** — Under Peppol BIS Self-Billing 3.0.1, the buyer issues the invoice on behalf of the supplier. The AccountingSupplierParty is still the supplier (the entity providing goods/services), and the AccountingCustomerParty is the buyer who created the document. The InvoiceTypeCode must indicate self-billing (389).

## Section 8 -- Archiving Requirements

**Archiving Requirements**  _(Belgian VAT Code Art. 60)_

| Requirement | Detail |
| --- | --- |
| Retention period | 7 years from the end of the year in which the VAT return was due (Belgian VAT Code Art. 60) |
| Extended retention | 10 years for immovable property adjustments; 15 years for new buildings |
| Format | Structured XML (original Peppol BIS format) must be retained; a human-readable rendering should also be stored |
| Integrity | Tamper-proof audit trail required; no modification to the original XML permitted |
| Accessibility | Must be available for tax inspection within Belgium or with immediate electronic access if stored elsewhere in the EU |
| Audit trail | Both sender and receiver must maintain records of transmission, receipt, and processing |
| Mercurius/Hermes | B2G invoices routed through Mercurius are archived by the platform; businesses should maintain their own copy |

## Section 9 -- Penalties for Non-Compliance

### E-Invoicing Specific Penalties (Royal Decree, July 2025)

**E-Invoicing Specific Penalties (Royal Decree, July 2025)**  _(Royal Decree, July 2025)_

| Infringement | Penalty (EUR) |
| --- | --- |
| First infringement | 1,500 |
| Second infringement | 3,000 |
| Third infringement (within 3 months of previous) | 5,000 |

### E-Invoicing Specific Penalties (Royal Decree, July 2025)

Penalties are per infringement, not per invoice. A "subsequent" infringement is only classified as new if identified at least 3 months after the previous penalty, giving businesses a remediation window.

### Existing VAT Penalties (Unchanged)

**Existing VAT Penalties (Unchanged)**

| Violation | Penalty |
| --- | --- |
| Late issuance of invoice | Administrative fine under Belgian VAT Code |
| Incorrect VAT treatment on invoice | Administrative fine + potential VAT reassessment |
| Failure to archive | Administrative fine |
| Fraud | Criminal penalties under Belgian VAT Code |

### Practical Consequences

Inability to send/receive Peppol invoices blocks the legal invoicing flow for domestic B2B; Suppliers who cannot issue structured invoices risk losing business relationships; Buyers who cannot receive structured invoices violate the mandate by accepting non-compliant documents

## Section 10 -- Interaction with Tax Skills

### E-Invoice → VAT Return (BTW-aangifte / Déclaration TVA)

Structured e-invoice data is the primary source for VAT return preparation. From 2028, Belgium anticipates a Peppol five-corner e-reporting model enabling near real-time VAT reporting. This aligns with the EU ViDA (VAT in the Digital Age) initiative.

### Automated Bookkeeping

Peppol BIS invoices in UBL 2.1 XML are machine-readable and can be automatically booked into accounting systems. This enables straight-through processing for accounts payable and accounts receivable.

### Purchase Order Matching

Peppol supports the full procure-to-pay chain. Invoices can reference Peppol order documents (cac:OrderReference), enabling automated 3-way matching (order → receipt → invoice).

### Cross-Border Interoperability

Belgium's Peppol-based framework is inherently interoperable with other Peppol-connected countries (Italy, France, Netherlands, Germany, Nordics, etc.). Cross-border invoices between Peppol participants follow the same technical specification.

### Corporate Tax (Vennootschapsbelasting / Impôt des sociétés)

Invoice data from Peppol invoices feeds into corporate tax computations. FPS Finance can cross-reference e-invoice data against reported revenue and deduction claims.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).

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
