---
name: hungary-einvoice
description: Use this skill whenever asked about e-invoicing in Hungary, NAV Online Számla, real-time invoice reporting (RTIR), NAV Online Invoicing System, XML 3.0 schema, invoice data reporting to the Hungarian tax authority, electronic invoice hash, completenessIndicator, or any question about issuing, transmitting, validating, or archiving electronic invoices under Hungarian law. Trigger on phrases like "NAV Online Számla", "RTIR Hungary", "real-time invoice reporting", "NAV API", "XML 3.0 Hungary", "invoiceData.xsd", "Online Invoicing System", "e-számla", "Hungarian invoice reporting", or "ManageInvoiceRequest". ALWAYS read this skill before touching any Hungary invoicing compliance work.
version: 1.0
jurisdiction: HU
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - einvoice-workflow-base
category: invoicing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Hungary Einvoice

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Hungary (Magyarország) |
| Currency | HUF (domestic); EUR/USD accepted for cross-border with HUF conversion |
| E-invoicing system name | NAV Online Számla Rendszer (Online Invoicing System) |
| Governing body | Nemzeti Adó- és Vámhivatal (NAV -- National Tax and Customs Administration) |
| Key legislation | Act CXXVII of 2007 on VAT (Áfa tv.); Act LXXXIII of 2018 (Online Invoicing System); Government Decree 23/2014 on technical requirements |
| Implementation timeline | Jul 2018 (B2B, VAT ≥ 100k HUF); Jul 2020 (all B2B invoices); Jan 2021 (B2C included); Jun 2021 (XSD 3.0 mandatory); May 2025 (XSD 2.0 end of life) |
| Current status (2026) | Fully operational RTIR covering 100% of invoices issued by VAT-registered persons; XSD 3.0 only; optional e-invoice (XML as legal invoice) available; preparing for ViDA alignment |
| Skill version | 1.0 |

## Section 2 -- Mandate Scope

### Who Must Comply

- **Who must comply** — All Hungarian VAT-registered taxpayers who issue invoices must report invoice data in real-time to the NAV Online Számla system. This includes: Domestic B2B invoices (all VAT amounts, including zero); Domestic B2C invoices; Invoices issued to other EU member states (intra-community supplies); Export invoices to third countries; Self-billing invoices (buyer issues on behalf of supplier); Modification invoices (credit notes, corrections). The only invoices excluded from RTIR are those issued under the OSS (One-Stop Shop) regime for non-established sellers.

### Timeline Phases

**Timeline Phases**

| Date | Milestone |
| --- | --- |
| 1 July 2018 | RTIR launched for B2B invoices with VAT ≥ HUF 100,000 |
| 1 July 2020 | RTIR extended to all B2B invoices regardless of VAT amount (XSD 2.0 mandatory) |
| 4 January 2021 | B2C invoices included in RTIR; all invoices now reportable |
| 1 June 2021 | XSD 3.0 mandatory for all submissions; optional e-invoice feature activated |
| 1 April 2021 | XSD 2.0 and earlier rejected; 3.0 exclusively accepted |
| 15 May 2025 | NAV officially ends all support for XSD 2.0 |
| 2026--2028 | ViDA alignment: transition from RTIR (data reporting) to full structured e-invoicing (EN 16931 XML as the legally binding invoice) |

### RTIR vs E-Invoicing Distinction

- **RTIR vs E-Invoicing distinction** — Hungary operates a real-time invoice data reporting model, not a clearance model. The reported XML is a copy of the invoice data, not the invoice itself (unless completenessIndicator=true). The legal invoice can be paper, PDF, or (optionally) the XML itself. With XSD 3.0, businesses can opt to declare the XML as the actual electronic invoice by setting completenessIndicator=true. In this case, the XML becomes the legally binding document and is available to the buyer via NAV's system.

## Section 3 -- Technical Format

### XML Schema (XSD 3.0)

- **XSD version requirement** — The NAV Online Számla system uses a proprietary XML schema maintained by NAV. As of 2026, only XSD version 3.0 is accepted.

**XML Schema (XSD 3.0)**

| Schema | Namespace | Purpose |
| --- | --- | --- |
| `invoiceData.xsd` | `http://schemas.nav.gov.hu/OSA/3.0/data` | Invoice data content |
| `invoiceApi.xsd` | `http://schemas.nav.gov.hu/OSA/3.0/api` | API request/response envelopes |
| `base.xsd` | `http://schemas.nav.gov.hu/OSA/3.0/base` | Common base types |
| `common.xsd` | `http://schemas.nav.gov.hu/NTCA/1.0/common` | NTCA common types |

### Key Schema Structures

**Key Schema Structures**

| Structure | Description |
| --- | --- |
| `InvoiceData` | Root element for invoice data XML |
| `InvoiceMain` | Contains `Invoice` (for normal invoices) or `BatchInvoice` (for summary invoices) |
| `InvoiceHead` | Supplier data, customer data, fiscal representative |
| `InvoiceDetail` | Invoice-level detail: category, appearance, currency, exchange rate, payment method, dates |
| `InvoiceLines` | Line-level data: descriptions, quantities, amounts, VAT rates, product codes |
| `InvoiceSummary` | Summary totals per VAT rate, global totals |

### API Request Types

**API Request Types**

| Request | XML Root | Purpose |
| --- | --- | --- |
| `ManageInvoiceRequest` | `invoiceApi:ManageInvoiceRequest` | Submit new invoices or modifications |
| `TokenExchangeRequest` | `invoiceApi:TokenExchangeRequest` | Obtain session token |
| `QueryInvoiceDataRequest` | `invoiceApi:QueryInvoiceDataRequest` | Query submitted invoice data |
| `QueryTransactionStatusRequest` | `invoiceApi:QueryTransactionStatusRequest` | Check processing status |
| `ManageAnnulmentRequest` | `invoiceApi:ManageAnnulmentRequest` | Technical annulment of erroneous data |

## Section 4 -- Mandatory Fields

### Invoice Data Fields (XSD 3.0)

**Invoice Data Fields (XSD 3.0)**

| Field | XPath (within InvoiceData) | Notes |
| --- | --- | --- |
| Invoice number | `invoiceHead/invoiceDetail/invoiceNumber` | Unique identifier |
| Invoice category | `invoiceHead/invoiceDetail/invoiceCategory` | NORMAL, SIMPLIFIED, AGGREGATE |
| Invoice issue date | `invoiceHead/invoiceDetail/invoiceIssueDate` | ISO 8601 |
| Invoice appearance | `invoiceHead/invoiceDetail/invoiceAppearance` | PAPER, ELECTRONIC, EDI, UNKNOWN |
| Supplier tax number | `invoiceHead/supplierInfo/supplierTaxNumber/taxpayerId` | 8-digit Hungarian tax ID |
| Supplier name | `invoiceHead/supplierInfo/supplierName` |  |
| Supplier address | `invoiceHead/supplierInfo/supplierAddress` | Structured address |
| Customer status | `invoiceHead/customerInfo/customerVatStatus` | DOMESTIC, OTHER, PRIVATE_PERSON |
| Customer tax number | `invoiceHead/customerInfo/customerVatData/customerTaxNumber/taxpayerId` | Required for DOMESTIC; optional for PRIVATE_PERSON |
| Customer name | `invoiceHead/customerInfo/customerName` | Required for B2B |
| Customer address | `invoiceHead/customerInfo/customerAddress` | Required for B2B |
| Currency | `invoiceHead/invoiceDetail/currencyCode` | ISO 4217 |
| Exchange rate | `invoiceHead/invoiceDetail/exchangeRate` | Required if currency ≠ HUF |
| Supply date | `invoiceHead/invoiceDetail/invoiceDeliveryDate` | Teljesítés dátuma |
| Payment method | `invoiceHead/invoiceDetail/paymentMethod` | TRANSFER, CASH, CARD, VOUCHER, OTHER |
| Payment date | `invoiceHead/invoiceDetail/paymentDate` | Due date |
| Line description | `invoiceLines/line/lineDescription` | Description of goods/services |
| Line quantity | `invoiceLines/line/quantity` |  |
| Line unit of measure | `invoiceLines/line/unitOfMeasure` |  |
| Line unit price | `invoiceLines/line/unitPrice` |  |
| Line net amount | `invoiceLines/line/lineAmountsNormal/lineNetAmountData/lineNetAmount` |  |
| Line VAT rate | `invoiceLines/line/lineAmountsNormal/lineNetAmountData/lineVatRate/vatPercentage` |  |
| Line VAT amount | `invoiceLines/line/lineAmountsNormal/lineVatAmountData/lineVatAmount` |  |
| Summary per VAT rate | `invoiceSummary/summaryByVatRate` | Net, VAT, gross per rate |
| Invoice grand total | `invoiceSummary/summaryGrossData/invoiceGrossAmount` |  |

### Modification Invoice Fields

**Modification Invoice Fields**

| Field | Notes |
| --- | --- |
| `modificationReferenceNumber` | Original invoice number being modified |
| `modificationTimestamp` | When the modification was initiated |
| `modifyWithoutMaster` | `true` if original invoice was issued before RTIR or not in the system |
| `modificationIndex` | Sequential number of modifications to the same original |

### Electronic Invoice (completenessIndicator=true)

**Electronic Invoice (completenessIndicator=true)**

| Field | Location | Notes |
| --- | --- | --- |
| `completenessIndicator` | `ManageInvoiceRequest/invoiceOperations/compressedContent` (attribute) | Set to `true` to declare XML as the legal invoice |
| `electronicInvoiceHash` | `ManageInvoiceRequest/invoiceOperations/invoiceOperation/electronicInvoiceHash` | SHA3-512 or SHA-256 hash of the invoice XML |
| `cryptoType` | Attribute of `electronicInvoiceHash` | `SHA3-512` or `SHA-256` |

- **Buyer access when completenessIndicator=true** — When completenessIndicator=true, NAV makes the invoice XML available to the buyer for download, and the XML serves as the legally binding invoice.

## Section 5 -- Transmission Method

### NAV Online Számla API

**NAV Online Számla API**

| Component | Detail |
| --- | --- |
| API type | RESTful XML-based API |
| Production URL | `https://api.onlineszamla.nav.gov.hu/invoiceService/v3/` |
| Test URL | `https://api-test.onlineszamla.nav.gov.hu/invoiceService/v3/` |
| Web portal | `https://onlineszamla.nav.gov.hu` (manual queries and management) |
| Authentication | Technical user credentials (login + password) + XML signing key + XML exchange key |
| Submission deadline | Immediately upon invoice issuance; technically within 5 minutes |

### API Workflow

- **API Workflow steps** — 1. Token Exchange: Call TokenExchangeRequest to obtain a session token (valid for 5 minutes) 2. Prepare Invoice XML: Generate invoiceData XML conforming to XSD 3.0 3. Compress and encode: Base64-encode the invoice data; optionally compress 4. Submit: Call ManageInvoiceRequest with the encoded invoice data, operation type (CREATE, MODIFY, STORNO), and request signature 5. Receive transaction ID: NAV returns a transactionId 6. Query status: Call QueryTransactionStatusRequest to verify processing result (RECEIVED, PROCESSING, DONE, ABORTED)

### Request Signature

- **Request signature composition** — Every ManageInvoiceRequest must include a request signature computed from: Request ID; Timestamp; XML signing key; Invoice hash values. The signature algorithm uses SHA-512 and the technical user's signing key.

### Batch Submission

- **Batch submission limit** — Up to 100 invoice operations can be submitted in a single ManageInvoiceRequest (within the invoiceOperations element). Each operation has its own index, operation type, and invoice data.

### Technical User Management

- **Technical user management** — Each taxpayer registers an "elsődleges felhasználó" (primary user) on the NAV portal, who then creates technical users for API access. Each technical user has: Login name and password; XML signing key (cserekulcs); XML exchange key (aláírókulcs). If keys are regenerated on the portal, they must be updated in the invoicing software immediately.

## Section 6 -- Validation Rules

### NAV-Side Validation

- **NAV-side validation checks** — NAV validates every submitted invoice against: 1. XSD schema validation -- must conform to XSD 3.0; earlier versions rejected. 2. Request signature validation -- cryptographic signature must be valid. 3. Technical user validation -- credentials and keys must match. 4. Business rule validation: Tax number format and validity (8-digit taxpayer ID + VAT code + county code); Invoice number uniqueness per supplier; Modification references: original invoice must exist in the system (unless modifyWithoutMaster=true); completenessIndicator restrictions (cannot be true for paper invoices, private person invoices, merged invoices, or pre-2021 invoices); Currency and exchange rate consistency; VAT rate validity against current Hungarian VAT law.

### Pre-Submission Checks

- **Pre-submission checks** — Validate XML against XSD 3.0 locally before API call; Verify request signature computation is correct; Confirm technical user credentials and keys are current (keys must be refreshed if regenerated on the portal); Verify tax number validity using NAV's public tax number query service; Ensure invoice number has not been previously submitted; For modifications: verify original invoice exists and modification index is sequential.

### Common Rejection Reasons

**Common Rejection Reasons**

| Reason | Detail |
| --- | --- |
| XSD version mismatch | Submission uses XSD 1.x or 2.0 (rejected since April 2021) |
| Invalid request signature | Signing key mismatch or computation error |
| Invalid tax number | Supplier or customer tax number format invalid or not registered |
| Duplicate invoice number | Same invoice number already submitted by the same supplier |
| Modification reference error | Referenced original invoice not found and `modifyWithoutMaster=false` |
| CompletionIndicator conflict | `completenessIndicator=true` with non-electronic appearance or private person |
| Missing mandatory field | Required XSD element absent or empty |
| Rate validation failure | VAT percentage does not match known Hungarian rates |

## Section 7 -- Tax Computation Rules

### Hungarian VAT Rates (2026)

**Hungarian VAT Rates (2026)**

| Rate | Percentage | Application |
| --- | --- | --- |
| Standard | 27% | Most goods and services (one of the highest in the EU) |
| Reduced 1 | 18% | Dairy products, bakery products, commercial accommodation |
| Reduced 2 | 5% | Basic foodstuffs (meat, eggs, milk), books, newspapers, medicines, district heating, internet access, new residential property (conditions apply), live performances |
| Exempt | 0% | Intra-community supplies, exports, certain financial and insurance services |

### Rounding Rules

- **Rounding rules** — VAT amounts calculated per line in the invoice currency (HUF or foreign currency). HUF amounts rounded to the nearest whole forint (no decimals). EUR/foreign currency amounts rounded to 2 decimal places. Summary totals are the sum of rounded line-level amounts. NAV validates that line-level amounts sum to the summary totals (with tolerance).

### Multi-Rate Invoice Handling

- **Multi-rate invoice handling** — Each VAT rate has a separate summaryByVatRate element in the invoiceSummary. Each element contains: vatRateNetData (taxable base at this rate); vatRateVatData (VAT amount at this rate); vatRateGrossData (gross amount at this rate). Lines with different VAT rates must declare the rate individually.

### Currency Handling

- **Currency handling** — For invoices in foreign currency: currencyCode must be a valid ISO 4217 code; exchangeRate is the MNB (Magyar Nemzeti Bank) rate on the tax point date or a contractual rate; HUF equivalents are required in the summary for tax reporting purposes; If the invoice is in HUF, exchangeRate must be 1.

### Reverse Charge

- **Reverse charge reporting** — Domestic reverse charge (fordított adózás) invoices must be reported with: vatExemption or vatOutOfScope indicator on relevant lines; Specific VAT rate type VAT_RATE_EXEMPT with the appropriate exemption reason.

## Section 8 -- Archiving Requirements

**Section 8 -- Archiving Requirements**

| Requirement | Detail |
| --- | --- |
| Retention period | 8 years from the end of the year in which the invoice was issued (Számviteli törvény) |
| Format (paper invoice) | Paper original must be retained; RTIR XML is a data report, not the legal document |
| Format (PDF invoice) | Digitally signed PDF with timestamp is the legal document; must be archived with signature intact |
| Format (XML e-invoice, completenessIndicator=true) | The XML submitted to NAV is the legal document; buyer downloads from NAV; both parties must retain the XML |
| Integrity | No modification permitted to the archived document; audit trail required |
| Accessibility | Must be available for NAV audit within the territory of Hungary (or EU with immediate electronic access) |
| NAV portal | NAV retains all submitted RTIR data; businesses can query via the web portal or API; however, NAV data is a report, not an archive -- businesses must maintain their own records |
| Buyer obligation (XML e-invoice) | If `completenessIndicator=true`, the buyer retrieves the XML from NAV and archives it as the original invoice |

## Section 9 -- Penalties for Non-Compliance

### RTIR-Specific Penalties

**RTIR-Specific Penalties**

| Violation | Penalty (HUF) |
| --- | --- |
| Failure to report invoice data to NAV | Up to HUF 500,000 per invoice (approx. EUR 1,300) |
| Late reporting (beyond the real-time deadline) | Graduated fines based on delay duration |
| Incorrect data in RTIR submission | Up to HUF 500,000 per invoice |
| Use of non-compliant invoicing software | Fines per NAV decree; software must be registered with NAV |
| Systematic non-compliance | Triggers risk classification; increased audit probability |

### General VAT Penalties

**General VAT Penalties**

| Violation | Penalty |
| --- | --- |
| Failure to issue invoice | Up to HUF 500,000 per instance |
| Incorrect invoice content | Tax reassessment + penalty (50% of tax shortfall as default penalty; 200% if fraud) |
| Late VAT return filing | Late payment interest + administrative fine |
| VAT fraud | Criminal penalties under Hungarian Penal Code |

### Practical Consequences

NAV uses RTIR data for automated risk analysis; persistent errors trigger compliance audits. The planned e-ÁFA (pre-filled VAT return) system relies on correct RTIR data; incorrect submissions lead to discrepancies in the pre-filled return. Buyers increasingly verify supplier RTIR compliance before accepting invoices.

## Section 10 -- Interaction with Tax Skills

### RTIR → VAT Return (ÁFA bevallás)

NAV uses RTIR data to construct the e-ÁFA (electronic VAT) pre-filled return. From 2024, NAV offers taxpayers a draft VAT return based on: Supplier-reported outbound invoices; Buyer-received inbound invoices; Customs declarations. Taxpayers review, adjust, and submit the pre-filled return. Discrepancies between RTIR data and the filed return trigger automated queries.

### RTIR → e-ÁFA Pre-Filled Return

The e-ÁFA system pre-populates: Output VAT from the taxpayer's submitted invoices; Input VAT from suppliers' reported invoices where the taxpayer is the buyer; Adjustments for credit notes and modifications. This significantly reduces manual data entry for small and medium businesses.

### Electronic Invoice (completenessIndicator=true) → Buyer AP

When a supplier sets completenessIndicator=true, the buyer can retrieve the structured XML invoice from NAV's system. This enables automated accounts payable processing, booking, and reconciliation.

### RTIR → Corporate Tax (Társasági adó)

NAV cross-references RTIR data against corporate tax returns. Revenue and cost data from invoices feeds into NAV's risk-analysis algorithms for corporate tax audits.

### Future: ViDA Alignment

Hungary's RTIR is expected to evolve into a full structured e-invoicing system aligned with EU ViDA requirements by 2028--2030. The transition will shift from data reporting (XML as a copy) to clearance or exchange (XML as the legally binding invoice, EN 16931 format). Hungary's advanced RTIR infrastructure positions it well for this transition.

### NAV Online Számla → e-Nyugta (Electronic Receipt)

NAV is developing the e-nyugta system for electronic receipts, which will eventually replace traditional cash registers for retail B2C transactions. This system will integrate with the existing Online Számla infrastructure.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts. To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call: → [Book a call](https://calendly.com/openaccountants-info/30min) We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).

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
