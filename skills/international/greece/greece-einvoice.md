---
name: greece-einvoice
description: Use this skill whenever asked about e-invoicing in Greece, myDATA platform, AADE electronic books, MARK unique registration number, real-time tax book reporting, e-invoicing providers in Greece, myDATA API, income/expense classification, QR code on Greek invoices, or any question about issuing, transmitting, validating, or archiving electronic invoices under Greek law. Trigger on phrases like "myDATA", "AADE", "MARK number", "Greek e-invoice", "electronic books Greece", "myDATA API", "SendInvoices", "e-timologio", "AFM tax number", "income classification", "expense classification", or "Greek VAT invoice". ALWAYS read this skill before touching any Greece invoicing compliance work.
version: 1.0
jurisdiction: GR
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - einvoice-workflow-base
category: invoicing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Greece Einvoice

## Greece E-Invoicing Compliance Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Greece (Ελληνική Δημοκρατία) |
| Currency | EUR |
| E-invoicing system name | myDATA (My Digital Accounting and Tax Application) |
| Governing body | AADE (Ανεξάρτητη Αρχή Δημοσίων Εσόδων -- Independent Authority for Public Revenue) |
| Key legislation | Law 4308/2014 (Greek Accounting Standards); Decision A.1138/2020 (myDATA launch); Law 5073/2023 (penalties); Law 5222/2025 (penalty updates); Decision 1128/2025 (B2B/B2C/B2G e-invoicing via providers) |
| Implementation timeline | myDATA platform launched July 2020; mandatory data transmission phased from 2021; B2G Peppol adopted; B2B/B2C mandatory electronic book reporting; MARK validation in force |
| Current status (2026) | All businesses must transmit invoice summaries in real-time to myDATA; MARK (Unique Registration Number) required on all invoices; AADE cross-checks myDATA vs VAT returns; escalating penalty regime active |
| Skill version | 1.0 |

## Section 2 -- Mandate Scope

### Who Must Comply

- **Who must comply with myDATA transmission** — All Greek businesses -- every entity with a Greek AFM (Tax Identification Number) that issues revenue or expense documents must transmit data to myDATA. This includes: Sole proprietors (ατομική επιχείρηση); Companies of all legal forms (ΑΕ, ΕΠΕ, ΟΕ, ΕΕ, ΙΚΕ); Freelancers and professionals; Farmers under the special or normal regime. B2G (Business-to-Government): Greece has adopted the Peppol four-corner model for B2G. Structured e-invoices (EN 16931) are transmitted via Peppol to public entities. Data also flows to myDATA. B2B (Business-to-Business): Suppliers must transmit invoice summary data to myDATA in real-time or near-real-time. The transmitted data receives a MARK from AADE, which must appear on the invoice delivered to the buyer. Invoices issued through a certified e-invoicing provider are automatically transmitted. B2C (Business-to-Consumer): Retail transactions reported via electronic tax registers (eTax Register Machines / EAFΔΣΣ) are transmitted to myDATA. For invoices (not receipts), same rules as B2B apply.

### Transmission Methods (By Entity Type)

**Transmission Methods (By Entity Type)**

| Method | Description | Who Uses It |
| --- | --- | --- |
| Certified e-invoicing provider (Πάροχος Ηλεκτρονικής Τιμολόγησης) | Automatic real-time transmission; provider handles XML formatting and AADE communication | Businesses using certified providers |
| ERP integration via myDATA API | Business transmits directly via AADE REST API | Businesses with in-house or commercial ERP systems |
| Electronic tax registers (EAFΔΣΣ) | POS/cash register data transmitted automatically | Retail businesses |
| Special Data Entry Form (Ειδική Φόρμα Καταχώρησης) | Manual entry on myDATA web portal | Small businesses with few documents and no software |

### Exemptions

- **Exemptions from myDATA compliance** — There is no turnover threshold -- all taxable entities must comply. Small entities issuing very few documents can use the Special Data Entry Form instead of software integration.

## Section 3 -- Technical Format

### myDATA XML Schema

- **myDATA XML schema description** — myDATA uses a proprietary XML schema defined by AADE, not UBL or CII. The current schema version is governed by AADE technical specifications.

**myDATA XML Schema Components**

| Schema Component | File |
| --- | --- |
| Invoice document | `InvoicesDoc.xsd` |
| Expense classification | `expensesClassification.xsd` |
| Income classification | `incomeClassification.xsd` |
| Response | `response.xsd` |
| Detailed invoice (for providers) | `InvoicesDoc_detailed.xsd` |
| Delivery notes | `RegisterTransfer.xsd`, `GetDeliveryStatusResponse.xsd` |

- **Current API versions** — Current API versions: v1.0.12 (for ERP/provider) and v2.0.1 (with digital delivery notes).

### B2G Format

- **B2G e-invoicing format** — For B2G transactions, Greece uses EN 16931 with Peppol BIS Billing 3.0 (UBL 2.1 XML), transmitted via the Peppol network. The data also flows into myDATA for electronic book purposes.

### Key Data Elements (myDATA Schema)

**Key Data Elements (myDATA Schema)**

| Element | Description |
| --- | --- |
| `invoiceHeader` | Invoice type, series, AA (sequential number), issue date, currency |
| `issuer` | Supplier AFM, country, branch |
| `counterpart` | Buyer AFM, country, branch (for B2B) |
| `paymentMethods` | Payment method type, amount, payment info |
| `invoiceDetails` | Line items: line number, net value, VAT category, VAT amount, classification codes |
| `invoiceSummary` | Total net value, total VAT amount, total withheld amount, total gross value |
| `taxesTotals` | Tax type, tax category, underlying value, tax amount |
| `invoiceClassification` | Income/expense classification type and category per line |

## Section 4 -- Mandatory Fields

### Fields Required on Every Greek Invoice

**Fields Required on Every Greek Invoice**

| Field | Description |
| --- | --- |
| Issuer AFM (ΑΦΜ) | Greek tax identification number |
| Issuer name and address | Full legal name, DOY (tax office) |
| Issuer DOY (ΔΟΥ) | Tax office of the issuer |
| Buyer AFM | Required for B2B; "retail" indicator for B2C |
| Invoice series and number | Unique sequential identifier |
| Invoice date | Date of issuance |
| Invoice type | myDATA type code (e.g., 1.1 = Sales Invoice, 2.1 = Service Invoice, 5.1 = Credit Invoice) |
| MARK (Μ.ΑΡ.Κ.) | Unique Registration Number from AADE -- mandatory on the issued document |
| QR code | Encodes the MARK verification URL; mandatory on printed/PDF invoices |
| Description of goods/services | Line-level detail |
| Quantity and unit | Per line item |
| Net value per line | Before VAT |
| VAT category and rate | Per line (code + percentage) |
| VAT amount per line |  |
| Income classification | Revenue type and category code per line |
| Total net value | Sum of line net values |
| Total VAT | Sum of line VAT amounts |
| Total gross value | Net + VAT |
| Payment method | Cash, bank transfer, card, cheque, etc. |
| Withholding tax | If applicable (type, rate, amount) |
| Stamp duty | If applicable |
| Fees/charges | If applicable |

### MARK (Μοναδικός Αριθμός Καταχώρησης)

- **MARK definition and role** — The MARK is the critical fiscal identifier. It is: Assigned by AADE upon successful data transmission to myDATA; A unique numeric registration number (long integer); Required on the invoice before delivery to the buyer; Used to generate the QR code verification URL. Without a valid MARK, the document is not fiscally recognized under Greek law.

### QR Code

**QR Code sources by channel**

| Channel | QR Code Source |
| --- | --- |
| E-invoicing provider | `downloadingInvoiceUrl` returned by the provider, supporting `/pdf`, `/myDATA`, `/EN16931` endpoints |
| ERP (direct API) | `qrCodeUrl` returned by the `SendInvoices` API call |

## Section 5 -- Transmission Method

### myDATA REST API

**myDATA REST API details**

| Component | Detail |
| --- | --- |
| API type | RESTful web services |
| Authentication | AADE user credentials (AFM + API key) or e-invoicing provider credentials |
| Environment URLs | Production: `mydata-api.aade.gr`; Testing: `mydata-dev.aade.gr` |
| Key methods (ERP) | `SendInvoices`, `SendExpensesClassification`, `SendIncomeClassification`, `RequestDocs`, `RequestTransmittedDocs`, `CancelInvoice` |
| Key methods (Provider) | Same as ERP plus `SendInvoices` with provider signature block |
| Response | MARK (on success) or error codes (on failure) |
| Real-time requirement | Transmission should occur at or near the time of invoice issuance |

### Workflow (ERP Integration)

1. Issue invoice in ERP system
2. Map data to myDATA XML schema (InvoicesDoc.xsd)
3. Call SendInvoices API endpoint
4. Receive response: MARK + QR code URL (success) or error codes (failure)
5. Print/embed MARK and QR code on the invoice
6. Deliver invoice to buyer

### Workflow (Certified E-Invoicing Provider)

1. Issue invoice through the provider's platform
2. Provider transmits data to AADE automatically
3. Provider receives MARK from AADE in real-time
4. Provider embeds MARK, QR code, and provider identification on the document
5. Document delivered to buyer electronically (with `downloadingInvoiceUrl`)

### Connection Loss Handling

- **Handling loss of connection to myDATA during invoice issuance** — If the connection to myDATA is lost during invoice issuance, the transaction continues normally. The invoice is issued with a "loss of connection" indicator and transmitted with a slight delay. The MARK is obtained shortly after connectivity is restored.

## Section 6 -- Validation Rules

### AADE Validation (on SendInvoices)

- **AADE validation checks on SendInvoices** — XML schema validation against the current InvoicesDoc XSD version; AFM validation for issuer and counterpart; Invoice type code validity (must match allowed type codes); Classification code validity (income/expense codes must exist in the designation combinations); Tax category and rate consistency; Arithmetic validation (line totals, VAT calculations, summary totals); Duplicate detection (same series/AA from the same issuer).

### Pre-Submission Checks

- **Pre-submission validation checks** — Validate XML locally against the current InvoicesDoc.xsd before API call; Verify AFM validity using AADE's public AFM verification service; Confirm income classification codes match the designation combinations spreadsheet (published by AADE); Ensure all line items have valid VAT category codes; Verify arithmetic: sum of line net values = total net value; sum of line VAT = total VAT.

### Common Rejection Reasons

**Common Rejection Reasons**

| Reason | Detail |
| --- | --- |
| Invalid AFM | Issuer or counterpart AFM fails check-digit validation or is inactive |
| Schema violation | XML does not conform to the current InvoicesDoc.xsd |
| Invalid invoice type | Type code not recognized or not applicable for the transaction |
| Classification error | Income or expense classification code invalid or mismatched with invoice type |
| Arithmetic mismatch | Line totals do not sum to invoice summary values |
| Duplicate submission | Same series/AA already has a MARK for this issuer |
| Invalid VAT rate | Rate does not match the declared VAT category |

## Section 7 -- Tax Computation Rules

### Greek VAT Rates (2026)

**Greek VAT Rates (2026)**  _(Annex to Greek VAT Code (Law 2859/2000))_

| Rate | Mainland | Aegean Islands (reduced jurisdiction) |
| --- | --- | --- |
| Standard | 24% | 17% |
| Reduced | 13% | 9% |
| Super-reduced | 6% | 4% |

- **Aegean island reduced rate scope** — Aegean island reduced rates apply to specific islands listed in Annex to Greek VAT Code (Law 2859/2000).  _(Annex to Greek VAT Code (Law 2859/2000))_

### Rounding Rules

- **VAT rounding rules** — VAT amounts calculated per line, rounded to 2 decimal places (EUR cents). Summary totals are the sum of rounded line-level amounts. myDATA validates arithmetic consistency with a tolerance of ±0.01 per line.

### Multi-Rate Invoice Handling

- **Multi-rate invoice handling** — Each VAT rate appears as a separate element in the `taxesTotals` section. Line items must each declare their own VAT category and rate. Mixed-rate invoices are fully supported.

### Withholding Tax

- **Withholding tax types** — Greek invoices frequently include withholding tax (παρακράτηση φόρου). Withholding types include: Income tax withholding (e.g., 20% on professional services); Solidarity contribution (where applicable); Stamp duty (χαρτόσημο). These are declared in the `taxesTotals` element with specific tax type codes.

### Income and Expense Classification

- **Income classification requirement** — Every invoice line must carry an income classification code. The designation combinations are published by AADE in a spreadsheet and map invoice types to allowed classification categories.

**Common income classification categories**

| Code | Category |
| --- | --- |
| category1_1 | Revenue from sale of goods |
| category1_2 | Revenue from sale of products |
| category1_3 | Revenue from provision of services |
| category1_5 | Revenue from sale of goods/services on behalf of third parties |
| category1_7 | Revenue from subsidies/grants |

## Section 8 -- Archiving Requirements

**Archiving Requirements**

| Requirement | Detail |
| --- | --- |
| Retention period | 5 years from the end of the fiscal year (general rule under Greek Accounting Standards, Law 4308/2014); extended to 6 years for VAT purposes; indefinite if litigation is pending |
| Format | Electronic format; myDATA data is maintained on AADE servers; businesses must retain their own records |
| MARK record | The MARK and associated QR code URL must be retained with the invoice |
| Accessibility | Must be available for tax audit within 48 hours of request |
| E-invoicing provider records | Providers must maintain all transmitted data and make it available to both issuer and AADE |
| Integrity | No modification to issued documents; corrections via credit notes or modification invoices |
| AADE platform | myDATA retains all transmitted data; businesses can query their electronic books via the API |

## Section 9 -- Penalties for Non-Compliance

### myDATA Penalty Framework (Law 5073/2023, updated by Law 5222/2025)

**myDATA Penalty Framework**  _(Law 5073/2023, updated by Law 5222/2025)_

| Violation | Penalty |
| --- | --- |
| First violation (failure to transmit or late transmission) | 50% of the VAT amount on the untransmitted documents, minimum EUR 250 |
| Repeat violation | 100% of the VAT amount |
| Failure to transmit data for an entire period | EUR 2,500 per month of non-compliance |
| Discrepancy between myDATA and VAT return | Triggers automatic audit; potential reassessment of VAT + 50% surcharge |

### AADE Cross-Checks

- **AADE cross-check sources and audit trigger** — AADE actively cross-references myDATA electronic books against: VAT returns (Φ2/periodic and annual); Income tax declarations; Third-party data (banks, card payments). Businesses with zero VAT declarations but active myDATA data face targeted audits. In 2025, AADE identified approximately 400 businesses with zero-turnover declarations despite active transaction data in myDATA.

### Additional Consequences

- **Additional consequences of non-compliance** — Untransmitted invoices are not fiscally valid -- buyers cannot claim VAT deductions. AADE may impose precautionary tax assessments based on myDATA data alone. Persistent non-compliance triggers classification as high-risk taxpayer.

## Section 10 -- Interaction with Tax Skills

### myDATA → VAT Return (Φ2)

- **myDATA feeds into VAT return preparation** — myDATA electronic books are the primary source for VAT return preparation. AADE pre-fills VAT return data from myDATA. The taxpayer must reconcile any differences between their accounting records and the myDATA data before filing.

### Expense Classification → Input VAT

- **Expense classification and input VAT deductibility** — Buyers must classify received invoices in myDATA as expenses with the appropriate classification codes. This classification determines: Deductibility of input VAT; Allocation to the correct income tax expense category; Reconciliation with the VAT return. Buyers who do not classify counterpart invoices within the deadline risk having AADE auto-classify them.

### myDATA → Income Tax

- **myDATA feeds into income tax return** — Income data transmitted to myDATA feeds into the annual income tax return. AADE cross-references declared revenue against myDATA totals. Significant discrepancies trigger audit procedures.

### B2G → Peppol → myDATA

- **B2G transaction flow via Peppol to myDATA** — For B2G transactions, the e-invoice travels via Peppol to the public entity. The invoice data is simultaneously transmitted to myDATA. The public entity's payment system references the myDATA MARK.

### Electronic Tax Registers → myDATA

- **POS transmission via electronic tax registers** — POS transactions from electronic tax registers (EAFΔΣΣ) are transmitted to myDATA as retail income. This data feeds into both VAT returns and income tax declarations.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — no liability on either side until you and the accountant sign
a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

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
