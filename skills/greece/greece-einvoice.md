---
name: greece-einvoice
description: Use this skill whenever asked about e-invoicing in Greece, myDATA platform, AADE electronic books, MARK unique registration number, real-time tax book reporting, e-invoicing providers in Greece, myDATA API, income/expense classification, QR code on Greek invoices, or any question about issuing, transmitting, validating, or archiving electronic invoices under Greek law. Trigger on phrases like "myDATA", "AADE", "MARK number", "Greek e-invoice", "electronic books Greece", "myDATA API", "SendInvoices", "e-timologio", "AFM tax number", "income classification", "expense classification", or "Greek VAT invoice", "mandatory e-invoicing Greece 2026", "timologio". Covers tax year 2026, including the mandatory B2B and B2G e-invoicing dates (2 March 2026 and 2 November 2026). VAT rates and returns are in greece-vat-return. ALWAYS read this skill before touching any Greece invoicing compliance work.
version: 1.3
jurisdiction: GR
tax_year: 2026
last_updated: 2026-11-16
depends_on:
  - einvoice-workflow-base
category: invoicing
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: e-invoicing
type: filing-howto
---

# Greece e-invoicing and myDATA v1.3

## Scope

Issue and transmit Greek invoices, reconcile AADE responses and retain evidence for tax year 2026. Greek accounting invoices, myDATA electronic-book reporting and the B2G public-procurement channel are related but distinct requirements. A successful myDATA upload alone does not prove use of a mandatory e-invoice channel or entitlement to deduct VAT. Load `einvoice-workflow-base` for the common workflow and `greece-vat-return` for VAT rates, island eligibility, input credit and return periods.

**Quick reference:** AADE administers myDATA (My Digital Accounting and Tax Application); amounts are in EUR. The current technical landing page offers ERP/provider/delivery specifications v2.0.2. First-period mandatory issue started 2 March 2026; second-period issue started 2 November 2026 with conditional parallel use through 31 January 2027. The phase, declaration and transaction conditions below matter. Position read on 16 November 2026, not a promise that later dates cannot change.

## Ask the client first

1. What are the invoice/supply dates, issuer legal form and tax/branch identity, customer country/status and B2B, B2C or public-contract route?
2. What was gross revenue on the 2023 income return, or the non-calendar tax year that began in 2023? Which mandatory cohort and start declaration/effective date are documented?
3. Which approved provider, AADE application, ERP, fiscal device or special-entry channel is in use, and is it lawful for this transaction and date?
4. What are the source invoice, VAT treatment, net amounts, withholding/other taxes, payment details and current classification combination? Establish these before building XML.
5. Is this original, correction, cancellation, self-billing or buyer-reported omission/deviation, and are there earlier MARKs or outage records?
6. Who retains the original invoice, XML, responses, evidence of delivery/acceptance and reconciliation, and is an audit or extended limitation period open?

## The method, step by step

### 1. Decide scope, cohort and lawful channel

| Item | Rule and conditions | Official source |
|---|---|---|
| Covered invoices | Sales inside Greece to Law 4308/2014 entities; business sales to non-EU countries except retail; public contracts and other General Government spending subject to the separate public-invoice provisions | A.1128/2025 art. 1, as replaced by A.1044/2026: https://www.aade.gr/sites/default/files/2026-02/a1044fek.pdf |
| Mandated issue | Licensed provider or AADE timologio; the timologio declaration also covers myDATAapp. The AADE press release says its free applications cover public-contract invoices too; check the actual B2G workflow rather than assuming an ERP upload is public-sector delivery | A.1128/2025 art. 1(2): https://www.aade.gr/sites/default/files/2025-09/a1128_2025fek.pdf; AADE: https://www.aade.gr/sites/default/files/2026-02/dt_17.02.2026.pdf |
| First period | Gross revenue over EUR 1,000,000 on the 2023 income return; for a non-calendar year, use the tax year that began in 2023. Start 2 March 2026. Parallel ERP/special entry to 3 May 2026 required the timely declaration with effective start no later than 2 March | A.1128/2025 art. 1(3), A.1044/2026: https://www.aade.gr/sites/default/files/2025-09/a1128_2025fek.pdf ; https://www.aade.gr/sites/default/files/2026-02/a1044fek.pdf |
| Second period | Remaining businesses from 2 November 2026. Parallel ERP/manual special entry from 2 November 2026 to 31 January 2027 only with a timely start declaration effective no later than 2 November | A.1197/2026 single article: https://www.aade.gr/sites/default/files/2026-10/A1197_2026_fek.pdf |
| Buyer acceptance | Law 4308/2014 buyers must accept the covered B2B/B2G e-invoices from 2 March 2026 | A.1044/2026: https://www.aade.gr/sites/default/files/2026-02/a1044fek.pdf |
| Outside this particular issue mandate | Intra-EU business sales and retail are outside art. 1's listed transactions, not automatically outside myDATA, fiscal-device or other invoice rules | A.1128/2025 art. 1: https://www.aade.gr/sites/default/files/2025-09/a1128_2025fek.pdf |
| Digital delivery notes, separate timeline | B1 loading/transshipment/receipt and stock checks from 1 January 2027; B2 Combined Nomenclature codes from 1 January 2028. These are not replacement invoice-mandate dates | A.1198/2026, same Gazette as A.1197: https://www.aade.gr/sites/default/files/2026-10/A1197_2026_fek.pdf |

The original 2 February and 1 October 2026 issue dates were superseded. Do not use them. Obtain the provider start declaration under A.1112/2025 art. 6 or the timologio declaration under A.1129/2025. The latter is filed through myAADE within 10 days of starting application use, identifying the entity, start date and selected transaction categories; retain its unique submission number. This operational declaration rule does not itself establish eligibility for tax incentives or cure a missed mandate-phase condition. [A.1129/2025 arts. 3-4](https://www.aade.gr/sites/default/files/2025-09/a1129-2025fek.pdf).

TPC art. 16 requires the accounting data of Law 4308/2014 entities to be transmitted regardless of invoice method or book category. That does not prove the former claim that every AFM holder, including every special-scheme farmer, transmits every document identically. Confirm the actual A.1138/2020 scope, exceptions and timing for the entity. Provider, ERP, fiscal-device retail transmission and the special entry form are distinct channels. ERP and special entry do not replace the required provider/AADE issue channel after any permitted transition. Special-form eligibility and fiscal-device model/sector exceptions remain held below; no blanket small-business or no-turnover exemption is asserted. [TPC art. 16](https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf).

For B2G, GSIS identifies itself as the national PEPPOL authority and requires providers to hold AADE certification, a certified PEPPOL Access Point and successful interoperability tests. EN 16931 is the European semantic invoice standard. Preserve public-contract routing/receipt evidence in addition to myDATA reporting. The exact Greek CIUS, BIS/UBL version and public-buyer identifiers must be checked for the actual channel; the earlier unsupported BIS Billing 3.0/UBL 2.1 statement is not treated as verified here. [GSIS provider requirements](https://www.gsis.gr/polites-epiheiriseis/pliromes-kai-eispraxeis/e-invoice/parohoi-ypiresion-ilektronikis-timologisis); [GSIS EN 16931](https://www.gsis.gr/peppol-eyropaiko-protypo-elot-en-16931).

### 2. Prepare the legal invoice and map its payload separately

A full invoice under Law 4308/2014 art. 9 includes issue date, unique sequential number, issuer and customer AFM and full name/address, goods quantity/type or services description, supply/payment date if different where required, net consideration by VAT rate/exemption, unit prices/discounts, VAT rate and VAT amount. Include the applicable self-billing, exemption, reverse-charge, new-vehicle, margin-scheme and fiscal-representative legends/details. VAT due is stated in euro. A signature is not required. Simplified invoices and special cases follow their own provisions; do not apply the full-invoice list as a universal retail receipt schema. [Law 4308/2014 arts. 9-10](https://minfin.gov.gr/wp-content/uploads/2024/02/%CE%9D-4308-2014.pdf).

The invoice's legal content is not identical to every XML field: the current API rejects domestic Greek party name/address fields in specified payload positions even though the invoice itself must carry those legal details. The old standalone DOY field, literal "retail" buyer indicator and universal payment/classification/QR requirements are not inferred from art. 9. Establish the channel-specific requirements. [API PartyType and document structures](https://www.aade.gr/sites/default/files/2026-09/myDATA%20API%20Documentation%20v2.0.2_official_erp_1.pdf).

| Payload area | Use and conditions | Source |
|---|---|---|
| `invoiceHeader` | Type, series, AA, issue date/currency and conditionally applicable header fields | API v2.0.2 sections 5.1, 5.3: https://www.aade.gr/sites/default/files/2026-09/myDATA%20API%20Documentation%20v2.0.2_official_erp_1.pdf |
| `issuer`, `counterpart` | Party AFM, country, branch, with domestic/foreign and type-specific acceptance rules | API sections 5.1-5.2: https://www.aade.gr/sites/default/files/2026-09/myDATA%20API%20Documentation%20v2.0.2_official_erp_1.pdf |
| `paymentMethods` | Conditional payment structures, not universally required for every document | API section 5.1: https://www.aade.gr/sites/default/files/2026-09/myDATA%20API%20Documentation%20v2.0.2_official_erp_1.pdf |
| `invoiceDetails` | Lines, net value, VAT category/amount and applicable taxes/classifications | API sections 5.1, 5.4: https://www.aade.gr/sites/default/files/2026-09/myDATA%20API%20Documentation%20v2.0.2_official_erp_1.pdf |
| `invoiceSummary` | Net, VAT, withholding, fees, digital transaction duty, other taxes, deductions and gross summary fields; amounts have two decimal places | API section 5.6: https://www.aade.gr/sites/default/files/2026-09/myDATA%20API%20Documentation%20v2.0.2_official_erp_1.pdf |
| `taxesTotals` | Applicable tax totals, with the specification's line-versus-summary consistency rules; not a separate VAT-rate bucket for every rate | API sections 5.1, 5.5-5.6: https://www.aade.gr/sites/default/files/2026-09/myDATA%20API%20Documentation%20v2.0.2_official_erp_1.pdf |
| Income/expense classifications | Supported line/summary structures or separate classification submissions. `invoiceClassification` is not a universal top-level mandatory field | API sections 4.2-4.3, 5.8-5.9: https://www.aade.gr/sites/default/files/2026-09/myDATA%20API%20Documentation%20v2.0.2_official_erp_1.pdf |

Use the current official XSD archive and designation-combination spreadsheet linked from the [technical landing page](https://www.aade.gr/mydata/tehnikes-prodiagrafes-ekdoseis-mydata). The old filename list (`InvoicesDoc.xsd`, `expensesClassification.xsd`, `incomeClassification.xsd`, `response.xsd`, `InvoicesDoc_detailed.xsd`, `RegisterTransfer.xsd`, `GetDeliveryStatusResponse.xsd`) remains a search aid only until the actual current archive files are checked. Do not pin old v1.0.12 or v2.0.1 as current: the page offers v2.0.2 for ERP, provider and digital-delivery interfaces.

### 3. Authenticate, transmit and check each response

Register through the myDATA REST API registration application using TAXISnet, create a user and obtain its subscription key. ERP calls use the headers `aade-user-id` (the registered username) and `ocp-apim-subscription-key`; this is not simply AFM plus key. Do not put credentials in the invoice or a public working paper. For ERP `SendInvoices`, POST the specified InvoicesDoc XML to production `https://mydatapi.aade.gr/myDATA/SendInvoices`; the development endpoint is `https://mydataapidev.aade.gr/SendInvoices`. The older `mydata-api.aade.gr` and `mydata-dev.aade.gr` hosts are not the current documented endpoints. Provider integration has separate specifications/credentials; do not assume its complete methods/signature contract equals ERP. [API sections 3-4.1](https://www.aade.gr/sites/default/files/2026-09/myDATA%20API%20Documentation%20v2.0.2_official_erp_1.pdf).

ERP methods include `SendInvoices`, `SendExpensesClassification`, `SendIncomeClassification`, `RequestDocs`, `RequestTransmittedDocs` and `CancelInvoice`. Cancellation uses the prior MARK and does not mean silently deleting the original accounting document. Receive a ResponseDoc with a response per submitted entity. Examine `statusCode`, errors, UID and applicable invoice/classification/cancellation MARK; success is `Success`. HTTP 200 can still contain XML/business validation errors. Save the exact request, response and selected environment. [API sections 4 and 6-7](https://www.aade.gr/sites/default/files/2026-09/myDATA%20API%20Documentation%20v2.0.2_official_erp_1.pdf).

1. Determine the lawful issue channel before creating the document. For a permitted ERP transaction map it to the current schema; for provider issue use the licensed provider workflow.
2. Validate locally, then submit or let the provider submit under its own protocol. Avoid blind retry after a timeout: check accepted documents/UID/MARK first to prevent duplicates.
3. Check every individual response; record successful MARKs and detailed rejections separately. Keep the emitted document and transmission identity linked.
4. For the response QR field use the actual interface field: the invoice structure contains `qrCodeUrl`, while submission responses document `qrUrl`, with response-type restrictions. Provider `downloadingInvoiceUrl` is distinct. Use returned URLs rather than inventing a MARK-derived verification URL.
5. Deliver through the lawful channel and preserve evidence. A provider workflow normally issues, transmits and supplies its final invoice/URL, but do not assume delivery or public-buyer acceptance from an AADE success alone.
6. For loss of connection use the actual channel's approved failure procedure. API `transmissionFailure` distinguishes provider/communication cases and ERP connection loss (value 3); it is not a general permission to issue first and send whenever convenient. Specific outage deadlines and the provider `/pdf`, `/myDATA`, `/EN16931` URL contract remain held below.

A MARK is AADE's registration number for accepted data. Absence of a MARK requires investigation and correction under the applicable channel/outage rules. It does not by itself establish that every underlying invoice is legally void or that the buyer automatically loses input VAT. Never use the old blanket claims to deny credit. [API document/response/failure structures](https://www.aade.gr/sites/default/files/2026-09/myDATA%20API%20Documentation%20v2.0.2_official_erp_1.pdf).

### 4. Validate arithmetic, classifications and corrections

Validate the actual current XML schema, issuer/counterparty identity and status, document type, accepted combinations, VAT category/exemption, applicable tax fields, line/summary arithmetic and duplicate identity. The API lists AFM, XML, document/classification, tax/arithmetic and duplicate errors. A check-digit calculation alone is not confirmation of a live registered counterparty; the exact public AFM verification service is not verified here. [API section 7](https://www.aade.gr/sites/default/files/2026-09/myDATA%20API%20Documentation%20v2.0.2_official_erp_1.pdf).

Route the actual VAT rate, island supply conditions, rounding of reduced rates and input-credit blocks to `greece-vat-return`. This file no longer repeats the 24/13/6/4 and island 17/9/4/3 rate table as another maintained source. Keep line VAT categories consistent for mixed-rate invoices and follow the API totals schema. Monetary fields require the specified precision; the old universal per-line EUR 0.01 validation tolerance and unconditional sum-of-rounded-lines rule were not confirmed. Do not silently adjust VAT to force acceptance.

Determine withholding separately under `gr-cross-border`/`gr-payroll` before coding it. A 20% professional-fee example is not universal. A stamp/duty field name is not proof that old stamp duty or a solidarity contribution is payable in 2026; the current API describes the former stamp-duty total as digital transaction duty. Identify applicable law rather than copying legacy tax-code examples. [API summary fields](https://www.aade.gr/sites/default/files/2026-09/myDATA%20API%20Documentation%20v2.0.2_official_erp_1.pdf).

| Common income category | Current description | Source |
|---|---|---|
| `category1_1` | Merchandise sales | API appendix 8.8: https://www.aade.gr/sites/default/files/2026-09/myDATA%20API%20Documentation%20v2.0.2_official_erp_1.pdf |
| `category1_2` | Products sales | API appendix 8.8: https://www.aade.gr/sites/default/files/2026-09/myDATA%20API%20Documentation%20v2.0.2_official_erp_1.pdf |
| `category1_3` | Services revenue | API appendix 8.8: https://www.aade.gr/sites/default/files/2026-09/myDATA%20API%20Documentation%20v2.0.2_official_erp_1.pdf |
| `category1_5` | Other revenue/profits, not third-party sales | API appendix 8.8: https://www.aade.gr/sites/default/files/2026-09/myDATA%20API%20Documentation%20v2.0.2_official_erp_1.pdf |
| `category1_7` | Third-party revenue, not an automatic subsidies/grants category | API appendix 8.8: https://www.aade.gr/sites/default/files/2026-09/myDATA%20API%20Documentation%20v2.0.2_official_erp_1.pdf |

Check the current designation combinations/E3 mapping for the transaction, including grants. Classifications may be supplied in the documented structures or separately; do not assert that every line must always carry income classification at original issue. Preserve any original, corrective invoice/credit note, cancellation MARK, classification update and correspondence as a traceable chain.

### 5. Retain records and reconcile to returns

Under accounting-law art. 7 retain records for the longer of five years from the end of the period and the period required by other legislation; any format must support searching, display and printing. Maintain invoice authenticity, content integrity and readability under arts. 14-15. Tax-procedure art. 13 uses its own minimum five-year clock from the end of the tax year in which the filing obligation arises, extended through applicable assessment periods or final resolution/full settlement of the tax claim. Apply the longer relevant period, not the old blanket six-year VAT or indefinite-litigation assertion. Preserve your own invoice/XML/response/MARK/URL/correction and delivery records rather than relying only on AADE or a provider. [Law 4308/2014 arts. 7, 15](https://minfin.gov.gr/wp-content/uploads/2024/02/%CE%9D-4308-2014.pdf); [TPC art. 13](https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf).

A written AADE information/copy request generally requires a response within **10 working days** of notification, subject to the documented difficulty/extension provisions of TPC art. 14. The old 48-hour claim was wrong. Provider storage/access obligations under A.1112/2025 still need the specific contractual and legal retention scope checked; appointing a provider does not remove the entity's own record duties. [TPC art. 14](https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf).

Reconcile issued/received invoices, fiscal-device retail streams, credit notes/cancellations, classification and myDATA totals against the ledger before preparing VAT or income returns. Preserve corrections and differences. TPC art. 16(2) sets a statutory floor for taxable transactions/revenue based on transmitted documents and says tax credits and deductible expenses are not taken into account if their supporting documents have not been transmitted under paragraph 1. Do not omit that restriction. A missing MARK alone, particularly with a documented outage, is not the same factual finding as a supporting document never transmitted. Apply the current implementing scope, correction/recipient remedies and VAT Code arts. 35-37 together with the owner skill to input VAT; use the actual current prefill/deviation and expense-classification instructions before filing. Do not claim automatic buyer classification, a universal loss of credit solely because a MARK is absent, precautionary assessment from myDATA alone or an automatic high-risk designation without the missing legal instructions. For B2G keep separate PEPPOL/public-buyer receipt status. RequestDocs/RequestTransmittedDocs include paginated retrieval; follow the continuation token until complete. [API section 6.2](https://www.aade.gr/sites/default/files/2026-09/myDATA%20API%20Documentation%20v2.0.2_official_erp_1.pdf).

## Worked cases

### Choose the invoice mandate cohort at the threshold

Two calendar-year businesses each issue an otherwise covered domestic business invoice. A reported EUR 1,000,001 gross revenue for 2023; B reported exactly EUR 1,000,000. The law says **over**, so A is in the first cohort and B in the second, not the first. Their legal start dates are 2 March and 2 November 2026 respectively. For parallel ERP use B must separately prove the timely declaration effective no later than 2 November; the arithmetic alone does not grant that transition. Non-calendar businesses use the tax year beginning in 2023. [A.1128/2025 art. 1(3)](https://www.aade.gr/sites/default/files/2025-09/a1128_2025fek.pdf); [A.1044/2026](https://www.aade.gr/sites/default/files/2026-02/a1044fek.pdf); [A.1197/2026](https://www.aade.gr/sites/default/files/2026-10/A1197_2026_fek.pdf).

```oa-check
name: Greece mandatory invoice cohort, strict 2023 turnover threshold
inputs:
  threshold: 1000000
  revenue_a: 1000001
  revenue_b: 1000000
steps:
  - a_excess: revenue_a - threshold
  - b_excess: revenue_b - threshold
expected:
  a_excess: 1
  b_excess: 0
```

## When to refuse or refer

Stop if the client's mandate cohort/declaration, source VAT treatment, accepted classification, channel or response is unresolved. Do not represent an ERP upload as mandatory e-invoice issue, a MARK as a legal tax opinion, a prepared file as filed, or a public-buyer invoice as accepted without evidence. Use the precise current source/channel for special-form eligibility, farmer/retail exceptions, B2G technical profiles and outage cures. Keep the unsupported items below out of an implementable compliance answer.

## Filing and payment

### Statutory sanctions, not an automatic assessment

| Breach and conditions | Statutory consequence | Source |
|---|---|---|
| Fiscal-device retail data not transmitted, VAT-bearing | 50% of related VAT, minimum EUR 250 single-entry/EUR 500 double-entry per audit | TPC art. 58(1)(α): https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf |
| Same without VAT | EUR 500 single-entry/EUR 1,000 double-entry per audit | TPC art. 58(1)(β): https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf |
| Repeat of those retail breaches | Double fine | TPC art. 58(2): https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf |
| Omitted issuer invoice/self-billing/purchase-title summaries | 10% net value, cap EUR 250 per day | TPC art. 58(3)(α): https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf |
| Payroll/depreciation/year-end entries or issuer/self-billing-recipient income classifications omitted, resulting in omission from the income-tax return | EUR 250 single-entry/EUR 500 double-entry per tax year per breach; the consequence condition matters | TPC art. 58(3)(β): https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf |
| Issuer sends only after buyer omission/deviation reporting and first understated value | 5% of each document's net value | TPC art. 58(3)(γ): https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf |
| Missing digital-delivery data | EUR 100 each, cap EUR 500/day and EUR 20,000/year, for the applicable obligation/period | TPC art. 58(3)(δ): https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf |
| Late rather than omitted art. 58(3)(α), (β), (δ) data | Half the respective omission fine | TPC art. 58(5): https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf |
| Required e-invoice not issued, VAT-bearing | Treated as non-issue; 50% VAT, minimum EUR 250/EUR 500 by book category per audit; repeat 100% minimum EUR 500/EUR 1,000; further repeat 200% minimum EUR 1,000/EUR 2,000 | TPC art. 57(6): https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf; AADE interpretation: https://www.aade.gr/sites/default/files/2026-02/dt_17.02.2026.pdf |
| Required e-invoice not issued, no VAT | EUR 500/EUR 1,000 by book category per audit | TPC art. 57(5): https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf; same AADE interpretation: https://www.aade.gr/sites/default/files/2026-02/dt_17.02.2026.pdf |

TPC art. 58(4) excludes the fine for the related other receipt documents where the revenue invoice to which those receipts relate was issued before any audit. Do not apply this as a blanket exception for every omitted invoice or classification under paragraph 3. Check the operative implementing decision and facts for the actual breach date before presenting the statutory table as an amount assessed; application details not read are held below. Do not combine fines without checking the statutory coordination/credit rules, including art. 57(8). E-invoice issue, myDATA transmission, return filing and late payment are different obligations. VAT return/payment and associated penalties are in `greece-vat-return`; income/withholding is in the relevant pack owner.

## Completion checklist

Retain the scope/cohort decision, filed declaration, approved channel, versioned schema/mapping, source invoice and legal tax treatment, exact XML/response and MARK/error status, QR/delivery evidence, corrections/outage log, complete retrieved records, ledger-to-myDATA-to-return reconciliation, retention date and unresolved tasks. Do not report success until both legal issue/delivery and data transmission requirements for this job are satisfied.

## Sources

| Source and actual scope read | URL | Read on |
|---|---|---|
| A.1128/2025 arts. 1-2: read for transactions, channels, revenue cohort and original dates; dates replaced by the later decisions below | https://www.aade.gr/sites/default/files/2025-09/a1128_2025fek.pdf | 2026-11-16 |
| A.1044/2026 single article: read for first cohort dates, conditional parallel use and B2G reservation | https://www.aade.gr/sites/default/files/2026-02/a1044fek.pdf | 2026-11-16 |
| A.1197/2026 and A.1198/2026: read for full four-page Gazette read for second cohort dates/declaration condition and separate delivery phases | https://www.aade.gr/sites/default/files/2026-10/A1197_2026_fek.pdf | 2026-11-16 |
| A.1129/2025 arts. 3-4: read for timologio declaration, timing/fields and multiple channels, not fresh verification of every incentive condition | https://www.aade.gr/sites/default/files/2025-09/a1129-2025fek.pdf | 2026-11-16 |
| AADE public e-invoicing page: read for current channel summary, declaration coverage and separate delivery timeline | https://www.aade.gr/node/15728 | 2026-11-16 |
| AADE 17 February release, both pages: read for dates, free applications including public-contract invoices, non-issue interpretation/fines | https://www.aade.gr/sites/default/files/2026-02/dt_17.02.2026.pdf | 2026-11-16 |
| AADE technical landing: read for current v2.0.2 and official specification/XSD/combination links, not the uninspected zip's filenames | https://www.aade.gr/mydata/tehnikes-prodiagrafes-ekdoseis-mydata | 2026-11-16 |
| ERP API v2.0.2: read for registration/headers/endpoints, methods, party/document/summary/failure/classification structures, response/error and retrieval rules, appendix income categories; selected relevant sections read, not the whole 121 pages | https://www.aade.gr/sites/default/files/2026-09/myDATA%20API%20Documentation%20v2.0.2_official_erp_1.pdf | 2026-11-16 |
| Ministry Law 4308/2014 text, arts. 7, 9-10, 14-15: read for records, invoice content and integrity; this 2024 text does not establish the later mandatory-issue amendment | https://minfin.gov.gr/wp-content/uploads/2024/02/%CE%9D-4308-2014.pdf | 2026-11-16 |
| TPC consolidation through Law 5259/2025: read for arts. 13-14, 16, 57(5)-(8), 58 and 83(50); retention, response, transmission and statutory fines, not all later implementing decisions | https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf | 2026-11-16 |
| GSIS provider requirements: read for AADE/PEPPOL certification and interoperability, not every B2G field/profile | https://www.gsis.gr/polites-epiheiriseis/pliromes-kai-eispraxeis/e-invoice/parohoi-ypiresion-ilektronikis-timologisis | 2026-11-16 |
| GSIS PEPPOL/EN 16931: read for national authority and European semantic standard | https://www.gsis.gr/peppol-eyropaiko-protypo-elot-en-16931 | 2026-11-16 |

Not yet confirmed: current A.1138/2020 consolidated entity/farmer exemptions, special-entry eligibility, transaction/channel-specific transmission/classification deadlines and VAT/income prefilling deviation tolerances; actual current XSD zip filenames and designation combinations/E3 mapping for the client; provider-specific credentials/signatures, archive/access periods and `/pdf`, `/myDATA`, `/EN16931` URL contract under A.1112/2025 (https://www.aade.gr/sites/default/files/2025-08/a1112_2025fek.pdf); actual outage cure deadlines; exact B2G CIUS/BIS/UBL profile, buyer references and receipt/payment workflow; standalone DOY/retail literal/QR print obligations by channel; a universal EUR 0.01 arithmetic tolerance; legal basis for blanket six-year VAT/indefinite litigation retention, a universal loss of VAT credit solely for a missing MARK (distinct from TPC art. 16(2)), automatic expense classification, myDATA-only precautionary assessment or automatic high-risk classification; current commencement/implementing rules for each art. 58 category and later TPC changes; any later mandate-date change. These are preserved evidence gaps, not operative instructions. VAT/island rate and source detail formerly repeated here lives in `greece-vat-return`, including VAT Code art. 26 and circular E.2113/2025: https://www.aade.gr/sites/default/files/2026-01/e2113_2025.pdf. The old joint-decision landing links are retained for lookup, not as extra freshly read sources: https://www.aade.gr/egkyklioi-kai-apofaseis/mydata-diataxeis/1128-15-09-2025 ; https://www.aade.gr/egkyklioi-kai-apofaseis/mydata-diataxeis/1044-17-02-2026 ; https://www.aade.gr/egkyklioi-kai-apofaseis/1197-30-09-2026 ; https://www.aade.gr/egkyklioi-kai-apofaseis/1198-30-09-2026.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
