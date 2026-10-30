---
name: hungary-einvoice
description: "Hungarian invoicing and real-time invoice data reporting to NAV (Online Számla) for tax year 2026. Covers who must report (every invoice and invoice-equivalent document issued under Hungarian invoicing rules: B2B, B2C, EU and export, but not OSS or IOSS supplies), immediate machine-to-machine reporting from invoicing software under NGM decree 23/2014 13/A. §, the 24-hour and 48-hour outage rules, printed invoices within 4 days or by the next day at HUF 500,000 VAT, the Online Számla 3.0 schema and API (token, 100 invoices per request, SHA3-512), the optional e-invoice delivered through NAV (completenessIndicator), invoice content and issue deadlines (Áfa tv. 163., 169. §), e-receipts and receipt reporting from 1 September 2026, retention, and the fines in Art. 220., 228. and 229. §. Trigger phrases: NAV Online Számla, online számlaadat-szolgáltatás, RTIR Hungary, invoiceData.xsd, ManageInvoiceRequest, completenessIndicator, e-nyugta. Out of scope: hu-vat-return (rates, returns), hungary-vat-return (form 2665), hu-corporate-tax."
version: 1.1
jurisdiction: HU
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - einvoice-workflow-base
category: invoicing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Hungary Einvoice

Tax year 2026. Law read on 30 October 2026: the VAT Act (Áfa tv., time state 15 September to 31 December 2026), the Tax Procedure Act (Art., time state 1 October to 31 December 2026), NGM decree 23/2014 (time state from 1 January 2026) and NAV's Online Számla 3.0 interface specification of 12 February 2026. VAT rates, returns, payment deadlines and late interest are in [hu-vat-return](hu-vat-return.md). Row-by-row form 2665 is in [hungary-vat-return](hungary-vat-return.md).

## Section 1 -- Quick Reference

| Field | Value |
| --- | --- |
| Country | Hungary (Magyarország) |
| Currency | HUF. An invoice may be in a foreign currency, but the VAT charged must also be shown in forints (Áfa tv. 172. §) |
| E-invoicing system name | Online Számla Rendszer (Online Invoicing System), https://onlineszamla.nav.gov.hu |
| Governing body | Nemzeti Adó- és Vámhivatal (NAV, National Tax and Customs Administration) |
| Key legislation | Áfa tv. (Act CXXVII of 2007) 158/A.-180. § (invoicing and records), 257/G. § and Annexes 10 and 11 (data reporting); 23/2014. (VI. 30.) NGM rendelet 8. § and 13/A.-13/C. § (invoicing software and its data reporting); Art. (Act CL of 2017) 220., 228. and 229. § (fines); Számv. tv. (Act C of 2000) 169. § (retention) |
| Model | Real-time invoice data reporting. The XML sent to NAV is a data report about the invoice, not the invoice, unless the seller chooses to deliver the e-invoice itself through NAV (decree 13/C. §) |
| Schema in use | Online Számla 3.0 (data, api, base and annul schemas, plus NTCA common 1.0) |
| Current status (2026) | Every invoice issued under Hungarian invoicing rules is reported, except supplies taxed under OSS or IOSS. Receipts not issued on a cash register are reported from 1 September 2026 |
| Skill version | 1.1 |

## Section 2 -- Mandate Scope

### Who Must Comply

- **The duty.** A taxable person reports to NAV the data of every invoice and invoice-equivalent document (számlával egy tekintet alá eső okirat) it issues for its own supplies, where Hungarian invoicing rules apply under Áfa tv. 158/A. § (Áfa tv. 257/G. § (2), Annex 10 point 1). Annex 10 makes no exception by customer type or amount.
- **What is covered.** Domestic B2B and B2C invoices, invoices to EU and non-EU customers, advance-payment invoices, self-billed invoices, and modifying and cancelling documents. For a supply outside Hungary the report states that the transaction is outside the territorial scope of the Áfa tv. (Annex 10 point 5/A).
- **The one exclusion.** Supplies whose place of supply is another member state and on which the seller pays VAT under the OSS or IOSS special schemes (Áfa tv. chapters XIX/A and XIX/B) are not reported (Annex 10 point 1).
- **Cash registers.** Invoices issued on an online cash register or an e-cash register are not reported through Online Számla. Their data reaches NAV through cash register reporting (Áfa tv. 257/G. § (2), (3), Annex 11).
- **Private customers.** For an invoice to a non-taxable natural person, the report leaves out the customer's name and address (Annex 10 points 2 and 4).
- **Extra data.** The report also covers deemed supplies under 11. § and 14. § (and whether the customer must pay the VAT back), the advance already paid on a final invoice, the legal predecessor's tax number, and the member's tax number on an invoice issued by a VAT group (Annex 10 points 4/A, 5, 5/B, 5/C).
- **Who may send it.** The taxable person or anyone it names on NAV's electronic interface; reports sent by that person count as the taxable person's own declarations (Annex 10 points 6 and 7). The decree applies to taxable persons registered in Hungary (decree 1/A. §).

### Timeline Phases

| Date | Milestone | Source |
| --- | --- | --- |
| 1 July 2018 | Online reporting starts for invoices issued after 30 June 2018 | Áfa tv. 317. § (1) |
| 1 July 2020 | The VAT value limit for reporting is abolished; every domestic B2B invoice is reported | NAV Online Számla CHANGELOG 3.0 |
| 4 January 2021 | Reporting extended to EU, export and private-person invoices; schema 3.0 lets an e-invoice itself be the data report from this date at the earliest | Áfa tv. 339. §; NAV CHANGELOG 3.0; NAV interface specification |
| 1 September 2026 | Receipts not issued on an online or e-cash register must also be reported, within 3 calendar days, summed per day and VAT rate | NAV information booklet 18 (2 March 2026); Áfa tv. Annex 11 B) |

### RTIR vs E-Invoicing Distinction

- **A data report, not an invoice.** Hungary runs a real-time reporting model, not a clearance model. The invoice itself can be paper or electronic (Áfa tv. 174. § (1)). An electronic invoice needs the customer's consent unless a law says otherwise (175. § (3) b)).
- **The optional NAV route.** A seller may meet its reporting duty by making the electronic invoice available to the customer through NAV's infrastructure. The report then counts as made when it was sent with the special flag (completenessIndicator = true) and a technically valid hash, and NAV confirmed successful processing (decree 13/C. § (1)-(2)). A customer with a Hungarian tax number can then download the XML exactly as uploaded (13/C. § (5)).
- **Limits of the NAV route.** It cannot be used where the customer is a non-taxable natural person, or for a document that modifies or cancels an invoice that was not itself delivered through NAV (decree 13/C. § (4)). The file must stay under NAV's published size limit (13/C. § (3)). Using it does not change either party's invoicing or retention duties (13/C. § (6)).

## Section 3 -- Technical Format

### XML Schema (Online Számla 3.0)

- **Version.** NAV's public repository and the 12 February 2026 interface specification describe version 3.0 of the schemas. In the 3.0 changelog NAV said it planned no further major version except for law changes or significant demand.

| Schema | Namespace | Purpose |
| --- | --- | --- |
| `invoiceData.xsd` | `http://schemas.nav.gov.hu/OSA/3.0/data` | Invoice data content |
| `invoiceApi.xsd` | `http://schemas.nav.gov.hu/OSA/3.0/api` | API request and response messages |
| `invoiceBase.xsd` | `http://schemas.nav.gov.hu/OSA/3.0/base` | Types shared across the Online Számla schemas |
| `invoiceAnnulment.xsd` | `http://schemas.nav.gov.hu/OSA/3.0/annul` | Technical annulment |
| NTCA common | `http://schemas.nav.gov.hu/NTCA/1.0/common` | NAV-wide common types |

### Key Schema Structures

| Structure | Description |
| --- | --- |
| `InvoiceData` | Root element: `invoiceNumber`, `invoiceIssueDate`, `completenessIndicator`, `invoiceMain` |
| `invoiceMain` | Contains `invoice` (one invoice or one modifying document) or `batchInvoice` (several modifying documents under one invoice number) |
| `invoiceReference` | For a modifying document: `originalInvoiceNumber`, `modifyWithoutMaster`, `modificationIndex` |
| `invoiceHead` | `supplierInfo`, `customerInfo`, `invoiceDetail` |
| `invoiceDetail` | Category, delivery date, currency, exchange rate, payment method and date, appearance |
| `invoiceLines` | Line data: description, quantity, unit, unit price, net amount, VAT rate, VAT amount |
| `invoiceSummary` | Totals per VAT rate (`summaryByVatRate`) and gross totals |

### API Request Types

| Request | Purpose |
| --- | --- |
| `TokenExchangeRequest` | Obtain a single-use data reporting token |
| `ManageInvoiceRequest` | Submit invoice operations: CREATE, MODIFY or STORNO |
| `ManageAnnulmentRequest` | Technical annulment (ANNUL) of an earlier, wrong data report |
| `QueryTransactionStatusRequest` | Check the processing result of a submission |
| `QueryTransactionListRequest` | List the taxpayer's transactions with their status |
| `QueryInvoiceDataRequest`, `QueryInvoiceDigestRequest`, `QueryInvoiceCheckRequest`, `QueryInvoiceChainDigestRequest` | Query reported invoices (issued and received) and modification chains |
| `QueryTaxpayerRequest` | Look up a Hungarian taxpayer by tax number |

## Section 4 -- Mandatory Fields

### Invoice content required by the Áfa tv.

The report carries the invoice's content as the Áfa tv. requires it, plus the currency and, for a foreign currency, the forint amounts and the exchange rate used (Annex 10 points 2 and 4). The mandatory invoice content is in Áfa tv. 169. §:

- date of issue; a serial number that identifies the invoice beyond doubt;
- the seller's tax number; the buyer's tax number where the buyer pays the VAT (reverse charge) or receives an exempt intra-EU supply, or the first eight digits of a domestic taxable buyer's tax number;
- names and addresses of seller and buyer;
- description and quantity of goods or services (customs tariff number or TESZOR'15 code at the issuer's choice);
- the supply date if it differs from the issue date;
- "pénzforgalmi elszámolás" for cash accounting; "önszámlázás" for self-billing; "fordított adózás" for reverse charge;
- taxable amount, unit price net of VAT, discounts; the VAT rate; the VAT charged;
- for an exemption, a reference to the law or the VAT Directive;
- margin scheme wording where relevant; the fiscal representative's name, address and tax number.

**Simplified invoices** (176. §) may be issued for advances, for cross-border supplies under 159. § (2) c) and d), for invoices up to the forint value of EUR 100 including VAT (other than intra-EU supplies of goods and distance sales), and by a subjectively exempt business.

### Invoice data fields (schema 3.0)

| Field | Element (within `InvoiceData`) | Notes |
| --- | --- | --- |
| Invoice number | `invoiceNumber` | Must be unique per supplier (error INVOICE_NUMBER_NOT_UNIQUE) |
| Issue date | `invoiceIssueDate` | |
| Invoice category | `invoiceDetail/invoiceCategory` | NORMAL, SIMPLIFIED, AGGREGATE |
| Appearance | `invoiceDetail/invoiceAppearance` | PAPER, ELECTRONIC, EDI, UNKNOWN |
| Supplier data | `invoiceHead/supplierInfo` | Tax number, name, address |
| Customer status | `customerInfo/customerVatStatus` | DOMESTIC, OTHER, PRIVATE_PERSON |
| Customer data | `invoiceHead/customerInfo` | Tax number, name and address; name and address left out for PRIVATE_PERSON |
| Supply date | `invoiceDetail/invoiceDeliveryDate` | Teljesítés dátuma |
| Currency | `invoiceDetail/currencyCode` | ISO 4217 code |
| Exchange rate | `invoiceDetail/exchangeRate` | Value of one unit of the currency in HUF; 1 for a HUF invoice |
| Payment method | `invoiceDetail/paymentMethod` | TRANSFER, CASH, CARD, VOUCHER, OTHER |
| Payment date | `invoiceDetail/paymentDate` | Optional in the schema |
| Line description, unit | `invoiceLines/line/lineDescription`, `unitOfMeasure` | |
| Line amounts and VAT rate | `lineAmountsNormal` (net amount, `lineVatRate`, VAT amount) | Simplified invoices use `lineAmountsSimplified` |
| Totals per VAT rate | `invoiceSummary/.../summaryByVatRate` | One per rate |
| Gross total | `invoiceGrossAmount`, `invoiceGrossAmountHUF` | |

### Modification Invoice Fields

| Field | Notes |
| --- | --- |
| `originalInvoiceNumber` | Number of the invoice being modified or cancelled |
| `modifyWithoutMaster` | `true` where the original invoice has no data report in the system |
| `modificationIndex` | Sequence number of the modification; NAV flags values above 1000 |

A modifying or cancelling document must carry its own date, its own serial number, a reference to the invoice it changes, and what changes and by how much (Áfa tv. 170. § (1)).

### Electronic Invoice Through NAV (completenessIndicator = true)

| Field | Location | Notes |
| --- | --- | --- |
| `completenessIndicator` | Element of `InvoiceData` | `true` declares that the data report is the invoice itself |
| `electronicInvoiceHash` | `ManageInvoiceRequest/invoiceOperations/invoiceOperation` | Required when the indicator is `true` |
| `cryptoType` | Attribute of `electronicInvoiceHash` | Only SHA3-512 when the indicator is `true` (upper-case hash); SHA3-512 or SHA-256 otherwise |

- **Restrictions (interface specification).** The appearance must be ELECTRONIC; the customer cannot be PRIVATE_PERSON, nor OTHER without a tax number; an invoice with merged line items cannot use it; a modifying document cannot use it unless the original invoice did; such a report cannot be technically annulled.
- **Buyer access.** The customer's tax number must be right, or the customer cannot download the invoice.

## Section 5 -- Transmission Method

### The legal deadline

- **Invoicing software.** The software must send at least the Annex 10 points 4 to 5/C data in XML "immediately" when the invoice is issued (kiállításakor azonnal), in the way and structure NAV publishes (decree 13/A. § (1)). An invoice counts as issued when the software closes its data (8. § (6)). Sending the data this way is one of the requirements every invoicing program must meet (8. § (1) d)).
- **A report counts as made** only when it was submitted and NAV's system confirmed successful processing (13/A. § (3)). If NAV rejects it, it must be resent once the error is fixed (13/A. § (4)).
- **Printed (pre-printed pad) invoices.** Report the data by the next calendar day if the invoice VAT is HUF 500,000 or more; otherwise within four calendar days of issue (Áfa tv. Annex 10 point 3). They are entered manually on NAV's interface (Annex 10 point 6).
- **Self-billing by a foreign buyer.** Where the issuer's agent is a buyer with no Hungarian seat and no Hungarian registration for that supply, the report is due within 6 days of issue (decree 13/A. § (8)-(9)).

### Outages

| Situation | Rule | Source |
| --- | --- | --- |
| NAV's system down (outage, maintenance) or internet failure at issue | Send within 24 hours after the problem ends | Decree 13/B. § (3) |
| Taxpayer's own system or internet down | Send within 24 hours after the problem ends | Decree 13/B. § (4) |
| Taxpayer's own outage over 48 hours | Flag it in NAV's system by the end of the 48 hours, then enter the data manually within 24 hours; extend by a new notice every 24 hours while it lasts | Decree 13/B. § (5) |
| Error found after NAV confirmed processing | Resend after fixing; if not fixed within 3 working days, enter the data manually until it is | Decree 13/A. § (5)-(7) |

### NAV Online Számla API

| Component | Detail |
| --- | --- |
| API type | XML over HTTPS, context root `/invoiceService/v3` |
| Production API | `https://api.onlineszamla.nav.gov.hu/invoiceService/v3/` |
| Test API | `https://api-test.onlineszamla.nav.gov.hu/invoiceService/v3/` |
| Web portal | `https://onlineszamla.nav.gov.hu` (test: `https://onlineszamla-test.nav.gov.hu`) |
| Authentication | Technical user login and password hash (SHA-512), request signature (SHA3-512) built with the signing key, token decoded with the exchange key |

### API Workflow

1. **Token.** Call `/tokenExchange`. The token is single-use, tied to one taxpayer, and valid for the period stated in the reply (currently 5 minutes; NAV says this may change). It arrives encoded with the technical user's exchange key.
2. **Build the data.** Generate `InvoiceData` XML that validates against schema 3.0 and BASE64-encode it (compression optional, flagged by `compressedContent`).
3. **Submit.** Call `/manageInvoice` with up to 100 invoice operations (CREATE, MODIFY or STORNO), each with its index and encoded data, plus the request signature.
4. **Transaction ID.** NAV returns a `transactionId`. Processing is asynchronous.
5. **Check the result.** Call `/queryTransactionStatus`. Request status values: RECEIVED, PROCESSING, SAVED, FINISHED, NOTIFIED. Per-invoice status values: RECEIVED, PROCESSING, SAVED, DONE, ABORTED.

### Request Signature

- **Composition.** NAV recalculates `requestSignature` from the stored and received data and runs the operation only if the values match. For `/manageInvoice` and `/manageAnnulment` it is built by partial authentication: the request ID, the UTC timestamp (YYYYMMDDhhmmss) and the signing key are concatenated; then, for each index in order, the upper-case SHA3-512 hash of the operation type plus its BASE64 content is appended; the upper-case SHA3-512 hash of the whole string is the signature.

### Batch Submission

- **Limit.** Up to 100 invoice operations per `ManageInvoiceRequest` (schema `maxOccurs="100"`), and up to 100 annulment operations per `ManageAnnulmentRequest`. NAV recommends keeping the limit as a parameter in client software.

### Technical User Management

- **Primary user.** The taxpayer's statutory or permanent representative is the primary user on the Online Számla web interface. Only primary users can create technical users; web users cannot use the reporting interface.
- **Keys.** The primary user generates a signing key (aláírókulcs, for `requestSignature`) and an exchange key (cserekulcs, for decoding the token) for each technical user, on the web interface only. The primary user decides whether a technical user may query invoice data.
- **Separate environments.** Registration, technical users and keys in the test system do not work in production.

## Section 6 -- Validation Rules

### NAV-Side Validation

NAV checks every submission in layers: schema validation against version 3.0; the technical user, password hash and request signature; then business validation. Business results come back as blocking errors (ERROR: the data report is not accepted and must be resent) or warnings (WARN: the report is accepted but may be wrong). NAV updated the ERROR and WARN lists on 24 July 2025 and 8 December 2025, with further WARN updates published in January and February 2026.

Examples of business checks from the specification: the supplier tax number matches the authenticated taxpayer; the invoice number is unique per supplier; line numbers run in sequence; the referenced original invoice exists unless `modifyWithoutMaster` is `true`; exemption codes are from the list (TAM, AAM, KBAET, KBAUK, EAM, NAM); the exchange rate is 1 for HUF; the rate for a foreign currency sits inside NAV's stored range; line HUF amounts are within 1% (at least HUF 1 and 0.01 of the invoice currency) of amount times rate.

### Pre-Submission Checks

- Validate the XML against the 3.0 schemas locally.
- Check the signature calculation, and that the technical user's keys are the current ones (keys regenerated on the portal must be updated in the software).
- Check the customer's tax number with `/queryTaxpayer`.
- Make sure the invoice number has not been reported before.
- For modifications, check that the original invoice exists and the modification index follows on.

### Common Rejection Reasons

| Reason | Detail |
| --- | --- |
| Schema error | XML does not validate against schema 3.0 |
| Invalid request signature | Signing key mismatch or calculation error |
| Supplier tax number mismatch | Tax number in the data differs from the authenticated taxpayer |
| Duplicate invoice number | Same invoice number already reported by the same supplier |
| Modification reference error | Original invoice not found and `modifyWithoutMaster` is `false` |
| completenessIndicator conflict | `true` with an appearance other than ELECTRONIC, a PRIVATE_PERSON customer or merged items |
| Invalid exemption code | `vatExemption` case not in the allowed list |
| Rate or amount mismatch | Exchange rate not 1 for HUF; VAT content and VAT rate mixed across normal and simplified data |

### Technical Annulment

A technical annulment (ANNUL) withdraws a wrong data report where the invoice itself was right. It is not a cancellation invoice. It works only on a report that reached DONE with warnings or nothing, must be approved by an authorised user in the Online Számla system, and at most one can be pending per invoice. A report that is itself the e-invoice (completenessIndicator = true) cannot be annulled.

## Section 7 -- Tax Computation Rules

### Hungarian VAT Rates (2026)

The rates come from Áfa tv. 82. §. The full lists are in [hu-vat-return](hu-vat-return.md), which governs if the two ever differ.

| Rate | Percentage | Application |
| --- | --- | --- |
| Standard | 27% | Most goods and services (82. § (1)) |
| Reduced, Annex 3 | 5% | For example books, certain medicines, pork, poultry, eggs, milk, district heating, internet access, restaurant food, commercial accommodation, certain new homes (82. § (2)) |
| Reduced, Annex 3/A | 18% | Milk products, flour and cereal bakery products, admission to certain open-air events (82. § (3)) |
| Zero rate, Annex 3/B | 0% | Daily newspapers; prescription-only medicines from 1 September 2026 (82. § (4)) |
| Exempt or out of scope | no VAT | Reported with `vatExemption` (code and reason) or `vatOutOfScope`, not as a 0% rate |

### Rounding and Tolerances

The invoice shows the VAT charged in forints even where other data are in a foreign currency (Áfa tv. 172. §). NAV warns where a line's HUF amount differs from amount times rate by more than 1% of the HUF value (at least HUF 1 and 0.01 of the invoice currency).

### Multi-Rate Invoice Handling

Each line declares its own VAT rate (`lineVatRate`). The summary has one `summaryByVatRate` element per rate with the net, VAT and gross amounts at that rate.

### Currency Handling

- `currencyCode` is the ISO 4217 code and `exchangeRate` is the HUF value of one unit; for a HUF invoice it must be 1.
- **Which rate.** The rate is the one valid at the supply date (or when VAT becomes due for advances and intra-EU acquisitions, or at issue in the 58. § cases). It is the last selling rate quoted by a Hungarian bank with an exchange licence, or the MNB rate if the business chose it and told NAV in advance, or the ECB's last published rate (Áfa tv. 80. § (1)-(2), 80/A. §). The MNB choice binds until the end of the year after the year of choice (80. § (4)).

### Reverse Charge

Domestic reverse charge lines are reported with `vatDomesticReverseCharge` = true, and the invoice says "fordított adózás" (Áfa tv. 169. § n)). Intra-EU exempt supplies use `vatExemption` with case KBAET (KBAUK for new means of transport); exports use EAM.

## Section 8 -- Archiving Requirements

| Requirement | Detail |
| --- | --- |
| Retention under the VAT Act | Keep invoices issued and received at least until the right to assess the tax lapses (Áfa tv. 179. § (1)) |
| Limitation period | Five years from the end of the calendar year in which the return was due (Art. 202. § (1)) |
| Retention under the Accounting Act | Accounting vouchers that support the books, kept readable and traceable, for at least 8 years (Számv. tv. 169. § (2)) |
| Paper invoice | The issuer keeps the copy, the recipient the original or, where allowed, a certified copy (Áfa tv. 179. § (2)) |
| Electronic invoice | Keep it electronically under the digital archiving rules, so all data can be produced without delay and later change is excluded (Számv. tv. 169. § (5)) |
| Integrity | From issue to the end of retention, authenticity of origin, integrity of content and legibility must be assured (Áfa tv. 168/A. § (1)) |
| Software documentation | Keep the invoicing software's user documentation until the right to assess the VAT on its invoices lapses (decree 10. § (4)) |
| Audit export | The software must have an "adóhatósági ellenőrzési adatszolgáltatás" export function by date or number range (decree 11/A. §) |
| NAV portal | NAV does not store an e-invoice sent through it under archiving rules; the taxpayer must always keep its own (interface specification) |
| NAV use of the data | NAV may use Annex 10 and 11 data to check taxpayers and select them for audit within the limitation period (Áfa tv. 257/G. § (5)) |

## Section 9 -- Penalties for Non-Compliance

### Invoice Data Reporting

Áfa tv. Annex 10 is titled "Összesítő jelentés" (summary report), and Art. 229. § sets the fine for breaches of that reporting duty.

| Violation | Penalty (HUF) | Source |
| --- | --- | --- |
| Data report missed, late, incomplete, wrong or untrue | Up to the number of invoices affected times the general maximum: HUF 1,000,000 per invoice for a company, HUF 400,000 for an individual | Art. 229. §, 220. § (1) |
| Any other breach of a tax-law duty (general fine) | Up to HUF 400,000 (individual) or HUF 1,000,000 (others) | Art. 220. § (1) |
| Lateness excused | No fine where the taxpayer fulfils the duty and shows it acted as reasonably expected | Art. 220. § (3) |

### General Invoicing and VAT Penalties

| Violation | Penalty | Source |
| --- | --- | --- |
| Failure to issue an invoice, simplified invoice or receipt, or issuing one not for the real consideration | Up to HUF 2,000,000 | Art. 228. § (1) a) |
| Failure to keep records | Up to HUF 2,000,000 | Art. 228. § (1) b) |
| Printed invoice or receipt pads not kept | Up to HUF 200,000 (individual) or HUF 500,000 (others) times the number missing | Art. 228. § (3) |
| Tax shortfall found by NAV | 50% of the shortfall; 200% where linked to hidden income or false or destroyed records | Art. 215. § (3)-(4) |
| Late VAT payment | Late payment interest at the central bank base rate plus 5 percentage points, per day / 365; see [hu-vat-return](hu-vat-return.md) | Art. 209. § (1) |

### Practical Consequences

NAV uses the reported invoice data to build the eÁfa draft VAT return and to select taxpayers for audit (Áfa tv. 184. § (2) b)-c), 257/G. § (5)). Wrong reports flow straight into a wrong draft return. NAV also tells the developer of the invoicing software, by tax number, the technical causes of faulty reports (without business data), copying the invoice issuer (Art. 131. § (30)).

## Section 10 -- Interaction with Tax Skills

### Invoice Data → VAT Return (eÁfa)

A business can file its VAT return by completing and approving the draft NAV builds on its electronic interface, or by sending invoice-level data and approving the draft by machine interface; approving the draft counts as filing (Áfa tv. 184. § (2) b)-c), (3)). If a machine-built draft is not approved, NAV deletes it on the last day of the month after the filing deadline (184. § (4)). Form 2665 and its rows are in [hungary-vat-return](hungary-vat-return.md).

### Received Invoices (M sheets)

For each received invoice on which it deducts VAT, a business declares in the return the first eight digits of the supplier's tax number, the base and VAT, the invoice number and the supply date (Annex 10 point 9). A business that files through eÁfa under 184. § (2) b) or c) is exempt from this (point 15). The "Számla befogadása" rules (points 9 to 15) were rewritten by Act XXXV of 2026, and the new text may already be applied to returns for the period that includes 1 July 2026 (Áfa tv. 380. §).

### Electronic Invoice Through NAV → Buyer AP

When the seller uses completenessIndicator = true, the buyer downloads the structured XML from NAV and can book it automatically.

### Invoice Data → Corporate Tax

NAV may use the reported data for checks and audit selection within the limitation period (Áfa tv. 257/G. § (5)). Corporate tax is in [hu-corporate-tax](hu-corporate-tax.md).

### Receipts and e-Receipts (e-nyugta)

- **Who issues receipts.** A business that does not issue an invoice because the customer paid in full and did not ask for one must issue a receipt (Áfa tv. 165. § (1) b), 166. § (1)). This route is closed for supplies to another taxable person or a legal person, and for consumer supplies of HUF 900,000 or more including VAT (165. § (3)).
- **e-nyugta.** An e-receipt is issued only electronically, on an e-cash register; it counts as issued when it reaches NAV's receipt store (nyugtatár), where the buyer sees it through an app (Áfa tv. 166. § (1a), 174. § (2)). Data from e-cash registers goes to NAV as they are issued (Annex 11 A)).
- **Other receipts from 1 September 2026.** Receipts not issued on an online cash register or e-cash register (for example from a computer or a printed pad) are reported on NAV's interface within 3 calendar days of issue, summed per day and per VAT rate (Annex 11 B) point 1; NAV booklet 18).

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Áfa tv., Act CXXVII of 2007 on VAT, consolidated text (time state 15 September to 31 December 2026): 80., 80/A., 82., 158/A.-180., 184., 257/G., 317., 339., 380. §, Annexes 10 and 11 | https://net.jogtar.hu/jogszabaly?docid=a0700127.tv | 2026-10-30 |
| Áfa tv., same act on the Nemzeti Jogszabálytár (articles; the annexes did not load) | https://njt.jog.gov.hu/jogszabaly/2007-127-00-00 | 2026-10-30 |
| 23/2014. (VI. 30.) NGM rendelet (invoice and receipt identification; invoicing software and its data reporting), time state from 1 January 2026: 1., 1/A., 2., 8., 10., 11/A., 13/A.-13/C., 17. § | https://net.jogtar.hu/jogszabaly?docid=a1400023.ngm | 2026-10-30 |
| Art., Act CL of 2017 on the rules of taxation (time state 1 October to 31 December 2026): 78., 131., 202., 209., 215., 220., 228., 229. § | https://net.jogtar.hu/jogszabaly?docid=a1700150.tv | 2026-10-30 |
| Számv. tv., Act C of 2000 on accounting: 169. § | https://net.jogtar.hu/jogszabaly?docid=a0000100.tv | 2026-10-30 |
| NAV, Online Invoice System 3.0 Interface Specification (English, 12 February 2026) | https://github.com/nav-gov-hu/Online-Invoice/tree/master/docs/API%20docs/en | 2026-10-30 |
| NAV, Online Számla 3.0 schemas (invoiceData, invoiceApi, invoiceBase, invoiceAnnulment) and CHANGELOG_3.0 | https://github.com/nav-gov-hu/Online-Invoice/tree/master/src/schemas/nav/gov/hu/OSA | 2026-10-30 |
| NAV, Online-Invoice repository README (production and test endpoints) | https://github.com/nav-gov-hu/Online-Invoice | 2026-10-30 |
| NAV information booklet 18, "A számla, nyugta kibocsátásának alapvető szabályai" (2 March 2026) | https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/18.-A-szamla-nyugta-kibocsatasanak-alapveto-szabalyai-2026.-03.-02. | 2026-10-30 |

Not yet confirmed: the VAT value limit that applied from 1 July 2018 to 30 June 2020 (the old version said HUF 100,000; it is not in the texts read today); the dates on which NAV stopped accepting schema versions 1.0 and 2.0 (the old version gave 1 April 2021, 1 June 2021 and 15 May 2025, which conflict and were not found in an official source today); whether NAV runs the 15-day call procedure of Art. 221. § before an Art. 229. § fine for missing invoice data; whether invoicing software must still be declared to NAV (the old version said so; the 2026 decree text has no such duty); the forint rounding rules for line and summary VAT beyond NAV's 1% tolerance; Hungary's plans under the EU ViDA package (Directive (EU) 2025/516) for structured e-invoicing or a move away from the current reporting model (EUR-Lex refused the download today, and no Hungarian law read today makes structured e-invoices mandatory); the start date of eÁfa draft returns (the old version said 2024); NAV's current size limit for e-invoices sent through NAV under decree 13/C. § (3).

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
