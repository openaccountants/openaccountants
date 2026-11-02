---
name: greece-einvoice
description: Use this skill whenever asked about e-invoicing in Greece, myDATA platform, AADE electronic books, MARK unique registration number, real-time tax book reporting, e-invoicing providers in Greece, myDATA API, income/expense classification, QR code on Greek invoices, or any question about issuing, transmitting, validating, or archiving electronic invoices under Greek law. Trigger on phrases like "myDATA", "AADE", "MARK number", "Greek e-invoice", "electronic books Greece", "myDATA API", "SendInvoices", "e-timologio", "AFM tax number", "income classification", "expense classification", or "Greek VAT invoice", "mandatory e-invoicing Greece 2026", "timologio". Covers tax year 2026, including the mandatory B2B and B2G e-invoicing dates (2 March 2026 and 2 November 2026). VAT rates and returns are in greece-vat-return. ALWAYS read this skill before touching any Greece invoicing compliance work.
version: 1.2
jurisdiction: GR
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - einvoice-workflow-base
category: invoicing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Greece Einvoice

## Greece E-Invoicing Compliance Skill v1.1

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Greece (Ελληνική Δημοκρατία) |
| Currency | EUR |
| E-invoicing system name | myDATA (My Digital Accounting and Tax Application) |
| Governing body | AADE (Ανεξάρτητη Αρχή Δημοσίων Εσόδων -- Independent Authority for Public Revenue) |
| Key legislation | Law 4308/2014 (Greek Accounting Standards), art. 14 (e-invoice), par. 6 added by ν. 5222/2025 art. 239; Tax Procedure Code ν. 5104/2024, art. 16 (electronic transmission to AADE) and arts. 57-58 (fines); joint decision Α.1138/2020 (myDATA transmission); joint decision Α.1128/2025 (mandatory e-invoicing), amended by Α.1044/2026 and Α.1197/2026; AADE decision Α.1112/2025 (provider obligations) |
| Implementation timeline | myDATA transmission under Α.1138/2020. Mandatory e-invoicing (Α.1128/2025 as amended): first period, businesses with 2023 gross revenue over EUR 1,000,000, from 2 March 2026, with parallel use of ERP or the special form allowed to 3 May 2026; second period, all other businesses, from 2 November 2026, with parallel use allowed to 31 January 2027 |
| Current status (23 October 2026) | First-period businesses must issue domestic B2B, non-EU B2B and B2G invoices only electronically, through a certified provider or AADE's free timologio / myDATAapp. Second-period businesses must do the same from 2 November 2026. Buyers must accept e-invoices from 2 March 2026. All businesses transmit book data to myDATA (TPC art. 16) |
| Skill version | 1.1 |

## Section 2 -- Mandate Scope

### Mandatory e-invoicing (Α.1128/2025, as amended by Α.1044/2026 and Α.1197/2026)

| Item | Rule | Source |
| --- | --- | --- |
| Which invoices | Every sale of goods or services (a) inside Greece to an entity under ν. 4308/2014 (B2B), (b) to a business in a non-EU country, except retail (B2B), (c) for public contracts and other General Government spending (B2G) | Α.1128/2025 art. 1(1), as replaced by Α.1044/2026 |
| How | Only through a certified e-invoicing provider (Πάροχος Υπηρεσιών Ηλεκτρονικής Έκδοσης Στοιχείων) or AADE's timologio application (myDATAapp is covered by the timologio declaration) | Α.1128/2025 art. 1(2); AADE e-invoicing page |
| First period | Businesses with gross revenue over EUR 1,000,000 on their 2023 income tax return: e-invoices only from 2 March 2026; parallel use of ERP or the special form allowed 2 March to 3 May 2026 if a start declaration was filed with a start date no later than 2 March 2026 | Α.1128/2025 arts. 1(3)(α), 2(1), as amended by Α.1044/2026 |
| Second period | All other businesses: e-invoices only from 2 November 2026; parallel use allowed 2 November 2026 to 31 January 2027 if a start declaration was filed with a start date no later than 2 November 2026 | Α.1128/2025 art. 2(2), as replaced by Α.1197/2026 (ΦΕΚ Β' 5905/30.09.2026) |
| Buyer acceptance | From 2 March 2026 a buyer under ν. 4308/2014 must accept e-invoices for B2B and B2G transactions | Α.1128/2025 art. 2(3), as replaced by Α.1044/2026 |
| Not covered by the mandate | Intra-EU B2B invoices and retail (B2C) sales; these still follow the myDATA transmission rules in Α.1138/2020 | Α.1128/2025 art. 1(1) |

The earlier dates in Α.1128/2025 as first published (2 February 2026 and 1 October 2026) no longer apply. The 1 January 2027 date on AADE's e-invoicing page is not an e-invoicing date: it starts phase B1 of digital delivery notes (loading, transshipment and receipt data, and stock quantity checks), under Α.1122/2024 art. 4(5) as replaced by Α.1198/2026. Phase B2 (Combined Nomenclature item codes) starts 1 January 2028.

### Who Must Comply

- **Who must comply with myDATA transmission**: All Greek businesses -- every entity with a Greek AFM (Tax Identification Number) that issues revenue or expense documents must transmit data to myDATA. This includes: Sole proprietors (ατομική επιχείρηση); Companies of all legal forms (ΑΕ, ΕΠΕ, ΟΕ, ΕΕ, ΙΚΕ); Freelancers and professionals; Farmers under the special or normal regime. B2G (Business-to-Government): Greece has adopted the Peppol four-corner model for B2G. Structured e-invoices (EN 16931) are transmitted via Peppol to public entities. Data also flows to myDATA. B2B (Business-to-Business): Suppliers must transmit invoice summary data to myDATA in real-time or near-real-time. The transmitted data receives a MARK from AADE, which must appear on the invoice delivered to the buyer. Invoices issued through a certified e-invoicing provider are automatically transmitted. B2C (Business-to-Consumer): Retail transactions reported via electronic tax registers (eTax Register Machines / EAFΔΣΣ) are transmitted to myDATA. For invoices (not receipts), same rules as B2B apply.

### Transmission Methods (By Entity Type)

**Transmission Methods (By Entity Type)**

| Method | Description | Who Uses It |
| --- | --- | --- |
| Certified e-invoicing provider (Πάροχος Ηλεκτρονικής Τιμολόγησης) | Automatic real-time transmission; provider handles XML formatting and AADE communication | Businesses using certified providers |
| ERP integration via myDATA API | Business transmits directly via AADE REST API | Businesses with in-house or commercial ERP systems |
| Electronic tax registers (EAFΔΣΣ) | POS/cash register data transmitted automatically | Retail businesses |
| Special Data Entry Form (Ειδική Φόρμα Καταχώρησης) | Manual entry on myDATA web portal | Small businesses with few documents and no software |

### Exemptions

- **Exemptions from myDATA compliance**: There is no turnover threshold -- all taxable entities must comply. Small entities issuing very few documents can use the Special Data Entry Form instead of software integration.

## Section 3 -- Technical Format

### myDATA XML Schema

- **myDATA XML schema description**: myDATA uses a proprietary XML schema defined by AADE, not UBL or CII. The current schema version is governed by AADE technical specifications.

**myDATA XML Schema Components**

| Schema Component | File |
| --- | --- |
| Invoice document | `InvoicesDoc.xsd` |
| Expense classification | `expensesClassification.xsd` |
| Income classification | `incomeClassification.xsd` |
| Response | `response.xsd` |
| Detailed invoice (for providers) | `InvoicesDoc_detailed.xsd` |
| Delivery notes | `RegisterTransfer.xsd`, `GetDeliveryStatusResponse.xsd` |

- **Current API versions**: Current API versions: v1.0.12 (for ERP/provider) and v2.0.1 (with digital delivery notes).

### B2G Format

- **B2G e-invoicing format**: For B2G transactions, Greece uses EN 16931 with Peppol BIS Billing 3.0 (UBL 2.1 XML), transmitted via the Peppol network. The data also flows into myDATA for electronic book purposes.

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

- **MARK definition and role**: The MARK is the critical fiscal identifier. It is: Assigned by AADE upon successful data transmission to myDATA; A unique numeric registration number (long integer); Required on the invoice before delivery to the buyer; Used to generate the QR code verification URL. Without a valid MARK, the document is not fiscally recognized under Greek law.

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

- **Handling loss of connection to myDATA during invoice issuance**: If the connection to myDATA is lost during invoice issuance, the transaction continues normally. The invoice is issued with a "loss of connection" indicator and transmitted with a slight delay. The MARK is obtained shortly after connectivity is restored.

## Section 6 -- Validation Rules

### AADE Validation (on SendInvoices)

- **AADE validation checks on SendInvoices**: XML schema validation against the current InvoicesDoc XSD version; AFM validation for issuer and counterpart; Invoice type code validity (must match allowed type codes); Classification code validity (income/expense codes must exist in the designation combinations); Tax category and rate consistency; Arithmetic validation (line totals, VAT calculations, summary totals); Duplicate detection (same series/AA from the same issuer).

### Pre-Submission Checks

- **Pre-submission validation checks**: Validate XML locally against the current InvoicesDoc.xsd before API call; Verify AFM validity using AADE's public AFM verification service; Confirm income classification codes match the designation combinations spreadsheet (published by AADE); Ensure all line items have valid VAT category codes; Verify arithmetic: sum of line net values = total net value; sum of line VAT = total VAT.

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

**Greek VAT Rates (2026)**  _(VAT Code ν. 5144/2024, art. 26 and Annex III; ν. 2859/2000 is repealed)_

| Rate | General | Islands with the 30% reduction (art. 26(4A)) |
| --- | --- | --- |
| Standard | 24% | 17% |
| Reduced (Annex III) | 13% | 9% |
| Lower (where Annex III says so) | 6% | 4% |
| Lowest (where Annex III says so) | 4% | 3% |

- **Island reduction scope:** From 1 January 2026 the 30% reduction applies automatically on the islands of the North Aegean Region, Samothrace and the Dodecanese with up to 20,000 inhabitants at the latest census (art. 26(4A), added by ν. 5246/2025 art. 11). Lesvos, Kos, Samos and Chios get it under art. 26(4) through decision Α.1150/2021, still in force (AADE circular Ε.2113/2025). The islands are listed in the annex to Ε.2113/2025. Tobacco and means of transport are excluded (art. 26(4B)). Rates are rounded to the nearest whole number (art. 26(6)). Details and examples: greece-vat-return.

### Rounding Rules

- **VAT rounding rules**: VAT amounts calculated per line, rounded to 2 decimal places (EUR cents). Summary totals are the sum of rounded line-level amounts. myDATA validates arithmetic consistency with a tolerance of ±0.01 per line.

### Multi-Rate Invoice Handling

- **Multi-rate invoice handling**: Each VAT rate appears as a separate element in the `taxesTotals` section. Line items must each declare their own VAT category and rate. Mixed-rate invoices are fully supported.

### Withholding Tax

- **Withholding tax types**: Greek invoices frequently include withholding tax (παρακράτηση φόρου). Withholding types include: Income tax withholding (e.g., 20% on professional services); Solidarity contribution (where applicable); Stamp duty (χαρτόσημο). These are declared in the `taxesTotals` element with specific tax type codes.

### Income and Expense Classification

- **Income classification requirement**: Every invoice line must carry an income classification code. The designation combinations are published by AADE in a spreadsheet and map invoice types to allowed classification categories.

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

### myDATA and e-invoicing fines (Tax Procedure Code ν. 5104/2024, arts. 57 and 58)

| Violation | Penalty | Source |
| --- | --- | --- |
| Retail receipts not transmitted to myDATA through the fiscal device system, VAT-bearing | 50% of the VAT on them, minimum EUR 250 (single-entry books) or EUR 500 (double-entry books) per audit | TPC art. 58(1)(α) |
| Same, transaction without VAT | EUR 500 (single-entry) or EUR 1,000 (double-entry) per audit | TPC art. 58(1)(β) |
| Repeat of either | Double the fine | TPC art. 58(2) |
| Issuer does not transmit invoice summaries (sales invoices, self-billing, purchase titles) | 10% of the net value of each document, capped at EUR 250 a day | TPC art. 58(3)(α) |
| Payroll, depreciation and year-end adjustment entries, or income classifications, not transmitted | EUR 250 (single-entry) or EUR 500 (double-entry) per tax year per breach | TPC art. 58(3)(β) |
| Issuer transmits only after the buyer reports an omission or difference, and the value first sent was too low | 5% of the net value of each document | TPC art. 58(3)(γ) |
| Digital delivery notes not transmitted | EUR 100 each, capped at EUR 500 a day and EUR 20,000 a year | TPC art. 58(3)(δ) |
| Late (not missing) transmission under art. 58(3)(α), (β), (δ) | 50% of the fine for non-transmission | TPC art. 58(5) |
| Required e-invoice not issued | Treated as no invoice issued. With VAT: 50% of the VAT on it, at least EUR 250 (single-entry) or EUR 500 (double-entry) per audit, 100% on a repeat. Without VAT: EUR 500 (single-entry) or EUR 1,000 (double-entry) per audit | TPC art. 57(5), (6); AADE press release 17.2.2026 |

### AADE Cross-Checks

- **AADE cross-check sources and audit trigger**: AADE cross-references myDATA electronic books against periodic VAT returns (there is no annual VAT return under VAT Code art. 43), income tax declarations and third-party data.

### Additional Consequences

- **Additional consequences of non-compliance**: Untransmitted invoices are not fiscally valid -- buyers cannot claim VAT deductions. AADE may impose precautionary tax assessments based on myDATA data alone. Persistent non-compliance triggers classification as high-risk taxpayer.

## Section 10 -- Interaction with Tax Skills

### myDATA → VAT Return (Φ2)

- **myDATA feeds into VAT return preparation**: myDATA electronic books are the primary source for VAT return preparation. AADE pre-fills VAT return data from myDATA. The taxpayer must reconcile any differences between their accounting records and the myDATA data before filing.

### Expense Classification → Input VAT

- **Expense classification and input VAT deductibility**: Buyers must classify received invoices in myDATA as expenses with the appropriate classification codes. This classification determines: Deductibility of input VAT; Allocation to the correct income tax expense category; Reconciliation with the VAT return. Buyers who do not classify counterpart invoices within the deadline risk having AADE auto-classify them.

### myDATA → Income Tax

- **myDATA feeds into income tax return**: Income data transmitted to myDATA feeds into the annual income tax return. AADE cross-references declared revenue against myDATA totals. Significant discrepancies trigger audit procedures.

### B2G → Peppol → myDATA

- **B2G transaction flow via Peppol to myDATA**: For B2G transactions, the e-invoice travels via Peppol to the public entity. The invoice data is simultaneously transmitted to myDATA. The public entity's payment system references the myDATA MARK.

### Electronic Tax Registers → myDATA

- **POS transmission via electronic tax registers**: POS transactions from electronic tax registers (EAFΔΣΣ) are transmitted to myDATA as retail income. This data feeds into both VAT returns and income tax declarations.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| AADE, joint decision Α.1128/2025 (mandatory e-invoicing) | https://www.aade.gr/egkyklioi-kai-apofaseis/mydata-diataxeis/1128-15-09-2025 | 2026-10-23 |
| AADE, joint decision Α.1044/2026 (first period moved to 2.3.2026) | https://www.aade.gr/egkyklioi-kai-apofaseis/mydata-diataxeis/1044-17-02-2026 | 2026-10-23 |
| AADE, joint decision Α.1197/2026 (second period moved to 2.11.2026) | https://www.aade.gr/egkyklioi-kai-apofaseis/1197-30-09-2026 | 2026-10-23 |
| AADE press release 17.2.2026 | https://www.aade.gr/deltia-typoy-anakoinoseis/deltio-typoy-17022026 | 2026-10-23 |
| AADE, mandatory e-invoicing page | https://www.aade.gr/node/15728 | 2026-10-23 |
| AADE, joint decision Α.1198/2026 (digital delivery notes, phase B1 from 1.1.2027) | https://www.aade.gr/egkyklioi-kai-apofaseis/1198-30-09-2026 | 2026-10-23 |
| AADE circular Ε.2113/2025 (island VAT reduction) | https://www.aade.gr/sites/default/files/2026-01/e2113_2025.pdf | 2026-10-23 |
| Tax Procedure Code (ν. 5104/2024), AADE codification Ε.2109/2025, arts. 57-58 | https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf | 2026-10-23 |
| VAT Code (ν. 5144/2024), Ministry of Finance codification to ν. 5313/2026, art. 26 | https://minfin.gov.gr/wp-content/uploads/2026/10/Κοινοποίηση-Διοικητικής-Κωδικοποίησης-του-ν.5144-2024-γι.pdf | 2026-10-23 |

Not yet confirmed: the B2G format and channel rules outside Α.1128/2025 (Peppol and EN 16931 statements in this skill are not checked against an official source); the myDATA API and schema versions; the archiving periods in Section 8; whether the second-period date moves again.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
