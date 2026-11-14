---
name: amazon-seller-integration
version: 2.0
category: bookkeeping
description: >
  Reconcile supplied amazon-seller exports for bookkeeping in 2026. Establish the actual schema, account, dates and currency, preserve order/invoice/payment relationships, reject malformed or unreconciled data and prepare postings for human approval. Historical fields and sample data are retained, but current API, software and fee behaviour is not certified.
jurisdiction: GLOBAL
last_updated: 2026-11-14
tier: 2
domain: bookkeeping
tax_year: 2026
type: cross-country-method
checked_on: 2026-11-14
---

# Amazon Seller settlement and order-component reconciliation v2.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Apply this method to the client's supplied files and supporting documents. It prepares a reconciled workpaper and proposed import/postings; it does not operate a live integration or certify a destination schema. Checked on 2026-11-14. Country tax positions remain with their own current skills.

## Ask the client first

1. Which entity owns the account, which country and reporting period apply, and what accounting framework, cash/accrual basis and functional currency are used?
2. Which product, region, account, export/report variant and file-generation date produced the supplied data? Obtain the actual headers or authenticated mapping, all pages/files, account identifiers and opening/closing statements.
3. Does this file describe orders, invoices, authorisations, settled balance activity, payouts, a general ledger or a trial balance? Which overlapping feeds/imports are already in the ledger?
4. What are the actual delimiter, encoding, header status, date order, timezone, decimal separator, units and signed-amount conventions? For an ambiguous date or missing currency, stop before import.
5. Which invoices, contracts, refunds, reserve movements, tax reports and supplier fee documents support the transactions? Who is principal, agent or merchant of record for each specified supply?
6. Is the ledger read-only? Who will approve the proposed import or postings and confirm the result? No live write access is assumed.

## The method, step by step

1. **Keep the evidence.** Preserve original bytes and record file identity, owner/account, report type, currency, covered dates and row count. Parse CSV/TSV with a real delimiter/quote-aware parser, not a split on commas. Preserve leading-zero identifiers, quoted narratives and original timestamps. Validate field count on every row. Treat spreadsheet formatting, headings, blank/footer/summary rows and BOMs explicitly; never remove a first data row merely because the old map expected a header. The historical inventory below is a starting question, not a certified current schema.
2. **Define the record grain.** Distinguish order, line item, invoice, payment, fee, balance event and payout. Use a stable source ID plus account, event kind and relevant line/currency identity. A repeated order ID can represent legitimate lines; a payment and its invoice are two records of one commercial event. Keep the mapping and a rejected-row report. Do not deduplicate by date/amount alone or silently discard unknown event codes.
3. **Test signs and units against evidence.** Recompute the supplied gross/fee/net relationship for every row where those fields exist. A signed deduction may be added; a positive charge may be subtracted. Do not force a platform-wide formula on contradictory data. Establish major/minor units from the actual report or supplied schema, including currencies that do not use two decimal places. Reject a conversion based only on an assumed divide-by-100 rule.
4. **Reconcile each account and currency.** Start from a supported opening balance, add signed balance movements and compare to the closing statement. Prove row-by-row balances where supplied. Include refunds, reversed payments, disputes, reserves, releases, fees, adjustments and transfers according to their actual balance impact and reporting cutoff. An authorisation without movement is different from a posted reversal. A pending label alone is not proof of either outcome. Holds and releases can fall in different periods; keep unmatched reserves on a balance-sheet control.
5. **Match settlement to the bank.** Group by supported payout/settlement references, currency and completed movement; reconcile settlement components, fees, retained amounts, negative settlements and timing differences. A bank deposit is a transfer from a clearing account, not another sale. Do not assume every intervening row between payouts belongs to the next deposit. Record opening/closing unsettled funds; obtain missing statements instead of inserting a balancing sale. Reconcile a card-funded negative settlement to the funding account.
6. **Prepare the commercial accounting.** Link the invoice/order/bill and payment, preserve tax and shipping detail, and separate amounts collected for others. A customer shipping charge can be part of the seller's consideration; it is not automatically removed from revenue. Gross cash does not always equal revenue, and a net payout is not by itself proof of agency. Under an applicable AASB 15/IFRS-equivalent reporting policy, assess control of each specified good/service, principal versus agent and third-party collections using paragraphs 47 and B34-B38. That conditional financial-reporting test does not replace local tax law. [AASB 15](https://standards.aasb.gov.au/sites/default/files/2026-11/AASB 15_12-14_COMPdec22_07-26.pdf).
7. **Apply the owning country's tax method.** Currency, marketplace suffix, email, billing country or a configured software tax code alone does not establish tax jurisdiction, business status, nexus or recoverability. Read the actual supply, establishment, customer, product, destination and registrations; link the official rule used. A payment-only file may lack the tax breakdown. UK sole-trader/partner records must identify business transactions and preserve receipts, invoices and statements; traditional accounting also tracks amounts owed/unpaid. Eligible UK business bank charges are distinct from non-deductible loan principal. [HMRC records](https://www.gov.uk/self-employed-records/what-records-to-keep); [financial charges](https://www.gov.uk/expenses-if-youre-self-employed/legal-financial).
8. **Handle foreign currency without losing either leg.** Keep original, settlement and functional-currency amounts and rate directions. Pair own-account conversion/transfer legs using documented IDs and accounts, not timestamp proximity alone. Transfer principal is not a sale, but settlement/translation differences and separately evidenced charges require their own treatment. For an applicable AASB 121/IFRS-equivalent reporting policy, use recognition-date rates, closing rates for monetary balances and the stated settlement-difference exceptions. An average is acceptable only when it reasonably approximates actual rates. Tax translation follows its own country's method. [AASB 121 paragraphs 21-23,27-30](https://standards.aasb.gov.au/sites/default/files/2025-03/AASB 121_08-15_COMPoct23_01-25.pdf).
9. **Deliver a controlled proposal.** Output a source-to-journal map, reconciliations by currency/account, unique IDs, proposed accounts/tax codes, debit/credit totals, outstanding differences and approvals required. For a read-only ledger, provide an import file or list of postings for a human to approve. Retain a manifest of approved/imported IDs and amounts, check existing feeds and earlier imports before re-running, then compare actual ledger counts and balances to the approved proposal. Never describe a draft as posted or change live bank-feed rules as part of reading a file.

## Country and framework boundaries

- **United Kingdom.** The HMRC source supports the UK recordkeeping and sole-trader/partner financial-charge points above. VAT on the platform's service and the client's sale are separate questions. Where an overseas service is involved, test actual belonging, establishment, exemption and input entitlement under Notice 741A sections 3-6, including unregistered-recipient registration consequences. A partly exempt buyer's reverse charge need not be neutral. [Notice 741A](https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a).
- **Australia or another entity using an IFRS-equivalent policy.** The cited AASB documents support only the conditional reporting treatments stated above. Confirm the framework and effective compilation for the entity's period. They do not set every country's income-tax deduction or VAT/GST result.
- **EU, US, Canada and other tax jurisdictions.** Load the current country/subnational sales-tax, income-tax and reporting methods. No global tax rate, marketplace exemption, information-reporting threshold or customer-location conclusion is certified from this export. EU consolidated VAT/DAC7 law was not readable during the current EUR-Lex outage; those obligations remain with the owning country method, not an inferred universal platform rule.

## When to refuse or refer

- Unknown owner, incomplete date range, missing currency, inconsistent field count, duplicate identity, ambiguous locale/units or a reconciliation difference: hold the import and identify the missing evidence. Never manufacture an opening balance or fee to make it fit.
- Do not filter away real money movements merely because their narrative says refund, reversal or conversion. Do not post transfers, loan principal, payroll liabilities or tax payments as new sales/ordinary expenses based solely on sign.
- Unsupported legal tax treatment, principal-agent contract, stock reimbursement, gift-card breakage or regulatory status: preserve the item and hand it to the relevant accounting/country method. Processor legal status and deposit protection depend on the actual entity and product.
- Exact live API endpoints, current platform export/import rules, software plan capabilities, pricing, fee-return policies and default codes have not been verified under this wave's official-authority-only restriction. No vendor page was used, and this method is not certification of a working live connection.

### Amazon Seller-specific controls

Keep settlement report, custom date-range report, order/shipment data, inventory records, advertising/fee documents and country-specific tax reports separate. Confirm FBA/FBM, inventory location, marketplace, settlement period and currency from evidence. The historical V2 report/API name and assumed fourteen-day cycle are not certified current behaviour.

Do not count amount lines as separate orders or deduplicate them by order ID. Principal, shipping, gift-wrap, promotions, collected tax, commissions, fulfilment/storage fees and refunds need their actual line identities and linked documentation. A refund can reverse both sales and some fees without returning every fee. Stock-loss reimbursement or liquidation requires its own accounting/tax analysis; it is not automatically excluded from taxable income. Advertising can be invoiced or collected in different ways, so test documents and avoid both omission and duplication instead of asserting it never reaches settlement data.

A marketplace suffix or currency does not establish the seller's tax jurisdiction. Stock location, seller/customer establishments, destination, product and marketplace role all matter. A tax-withheld label does not establish that every seller filing/registration/payment obligation is discharged. Cross-reference actual marketplace tax reports and owning country law. Under an applicable reporting framework, separate own revenue, agency collections and the settlement transfer. Do not automatically classify every `ItemPrice` amount as revenue or every `Adjustment` as non-revenue.

The retained TSV has a 24-field header but rows of 14, 18 or 22 fields. It must be rejected before field-position mapping. The visible illustrative amount components also do not bridge to the stated GBP1,847.32 settlement. Do not pad shifted columns, guess missing identifiers, invent sales or certify a balanced import.

## Worked case

These are manually identified illustrative amounts in a malformed retained fixture, not a successful parse. Visible activity is negative GBP16.32, leaving GBP1,863.64 unexplained against the header settlement. One order row is two fields short. The import must stop and request a complete, correctly aligned export.

```oa-check
name: Amazon Seller settlement and order-component reconciliation
inputs:
  sale: 29.99
  shipping: 3.99
  commission: 4.5
  fulfilment: 3.21
  refund: 19.99
  commission_return: 2.4
  subscription: 25
  stated_settlement: 1847.32
  header_fields: 24
  order_row_fields: 22
steps:
  - visible_activity: sale + shipping - commission - fulfilment - refund + commission_return - subscription
  - unexplained_settlement: stated_settlement - visible_activity
  - missing_fields: header_fields - order_row_fields
expected:
  visible_activity: -16.32
  unexplained_settlement: 1863.64
  missing_fields: 2
```

## Retained supplied-data fixtures

These are the original illustrations, retained byte-for-byte inside their code blocks. They are not certified current platform exports, fee schedules or complete accounts. Use the worked control above and the validation method before using any record. A failed example must remain failed, not silently repaired.

```tsv
settlement-id	settlement-start-date	settlement-end-date	deposit-date	total-amount	currency	transaction-type	order-id	merchant-order-id	adjustment-id	shipment-id	marketplace-name	amount-type	amount-description	amount	fulfillment-id	posted-date	posted-date-time	order-item-code	merchant-order-item-id	merchant-adjustment-item-id	sku	quantity-purchased	promotion-id
18906543210	2026-03-01T00:00:00+00:00	2026-03-15T00:00:00+00:00	2026-03-17	1847.32	GBP
18906543210	2026-03-01T00:00:00+00:00	2026-03-15T00:00:00+00:00	2026-03-17		GBP	Order	206-1234567-8901234			FBA12345	amazon.co.uk	ItemPrice	Principal	29.99	AFN	2026-03-02	2026-03-02T14:23:00+00:00	12345678901234		WIDGET-001	1
18906543210	2026-03-01T00:00:00+00:00	2026-03-15T00:00:00+00:00	2026-03-17		GBP	Order	206-1234567-8901234			FBA12345	amazon.co.uk	ItemPrice	Shipping	3.99	AFN	2026-03-02	2026-03-02T14:23:00+00:00	12345678901234		WIDGET-001	1
18906543210	2026-03-01T00:00:00+00:00	2026-03-15T00:00:00+00:00	2026-03-17		GBP	Order	206-1234567-8901234			FBA12345	amazon.co.uk	ItemFees	Commission	-4.50	AFN	2026-03-02	2026-03-02T14:23:00+00:00	12345678901234		WIDGET-001	1
18906543210	2026-03-01T00:00:00+00:00	2026-03-15T00:00:00+00:00	2026-03-17		GBP	Order	206-1234567-8901234			FBA12345	amazon.co.uk	ItemFees	FBAPerUnitFulfillmentFee	-3.21	AFN	2026-03-02	2026-03-02T14:23:00+00:00	12345678901234		WIDGET-001	1
18906543210	2026-03-01T00:00:00+00:00	2026-03-15T00:00:00+00:00	2026-03-17		GBP	Refund	206-9876543-2109876			FBA12346	amazon.co.uk	ItemPrice	Principal	-19.99	AFN	2026-03-05	2026-03-05T09:15:00+00:00	98765432109876		GADGET-002	1
18906543210	2026-03-01T00:00:00+00:00	2026-03-15T00:00:00+00:00	2026-03-17		GBP	Refund	206-9876543-2109876			FBA12346	amazon.co.uk	ItemFees	Commission	2.40	AFN	2026-03-05	2026-03-05T09:15:00+00:00	98765432109876		GADGET-002	1
18906543210	2026-03-01T00:00:00+00:00	2026-03-15T00:00:00+00:00	2026-03-17		GBP	Service Fee					amazon.co.uk	other	Subscription	-25.00		2026-03-01	2026-03-01T00:00:00+00:00
18906543210	2026-03-01T00:00:00+00:00	2026-03-15T00:00:00+00:00	2026-03-17		GBP	Transfer								-1847.32		2026-03-17	2026-03-17T06:00:00+00:00
```

## Existing review requirement

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

## Sources

| Official source | Read on | Read scope |
|---|---|---|
| https://www.gov.uk/self-employed-records/what-records-to-keep | 2026-11-14 | Read for sales/expense proof, accurate records, distinguishing business transactions and accrual records. |
| https://www.gov.uk/expenses-if-youre-self-employed/legal-financial | 2026-11-14 | Read business bank/credit-card charges, loan principal exclusion and bad debts/cash-basis distinction for UK sole traders and partners. |
| https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a | 2026-11-14 | Read for sections2-6 and13, actual supply, belonging, reverse-charge conditions, input-tax limits and unregistered recipients. |
| https://standards.aasb.gov.au/sites/default/files/2026-11/AASB 15_12-14_COMPdec22_07-26.pdf | 2026-11-14 | Read paragraphs 47,105-108,B34-B38 and B44-B47 for third-party collections, receivables/contract liabilities, principal-agent control and unexercised rights. Conditional Australian IFRS-equivalent financial-reporting scope, not worldwide tax law. |
| https://standards.aasb.gov.au/sites/default/files/2025-03/AASB 121_08-15_COMPoct23_01-25.pdf | 2026-11-14 | Read for paragraphs20-23 and27-30, initial recognition, monetary closing balances and settlement exchange differences; Australian IFRS-equivalent financial reporting, not universal tax translation. |

Not yet confirmed: the live amazon-seller API/schema, exact export/import column positions and availability, UI/report paths, region/plan capabilities, pricing and fee/refund conventions, automatic tax/FX behaviour, regulatory status and third-party document acceptance. The following literal table/path inventory records what the old file claimed, only to help locate and compare supplied data. Its fees, codes, timing, default settings and field meanings are historical and must not be treated as 2026 guidance. Known accounting/tax errors are replaced by the method and country boundaries above. No vendor source was used.

### Historical schema and claim inventory, not usable guidance

#### Historical 2 - Export Formats

```text
Historical item TSV (Tab-separated). Use Case: Settlement Report V2 (GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2). The primary financial report.
Historical item CSV. Use Case: Date Range Reports (custom period exports from Payments dashboard).
Historical item XML. Use Case: Settlement Report XML version (legacy).
Historical item PDF. Use Case: Summary reports, account activity PDFs (for overview, not line-item data).
```

#### Historical Settlement Report V2 (Flat File)

```text
Historical item settlement-id. Meaning: Unique settlement period identifier. All rows in one settlement share this ID.
Historical item settlement-start-date. Meaning: Start of the settlement period (ISO 8601).
Historical item settlement-end-date. Meaning: End of the settlement period (ISO 8601).
Historical item deposit-date. Meaning: Date Amazon deposited funds to the seller's bank account.
Historical item total-amount. Meaning: Total settlement amount deposited. Only populated on the first row.
Historical item currency. Meaning: Three-letter ISO currency code (USD, GBP, EUR).
Historical item transaction-type. Meaning: Order, Refund, Service Fee, Adjustment, Transfer, Liquidations, other (see Section 4).
Historical item order-id. Meaning: Amazon order ID (e.g., 111-1234567-1234567). Blank for non-order transactions.
Historical item merchant-order-id. Meaning: Seller's own order reference (if set).
Historical item adjustment-id. Meaning: Identifier for adjustment transactions.
Historical item shipment-id. Meaning: FBA shipment ID.
Historical item marketplace-name. Meaning: Which Amazon marketplace (amazon.com, amazon.co.uk, amazon.de, etc.).
Historical item amount-type. Meaning: Category of the amount: ItemPrice, ItemFees, Promotion, ItemWithheldTax, other.
Historical item amount-description. Meaning: Specific fee/charge name (see Section 4 for complete list).
Historical item amount. Meaning: The monetary value. Positive = credit to seller, negative = debit from seller.
Historical item fulfillment-id. Meaning: AFN (Fulfilled by Amazon / FBA) or MFN (Merchant Fulfilled).
Historical item posted-date. Meaning: Date the transaction was posted.
Historical item posted-date-time. Meaning: Full timestamp of posting (ISO 8601).
Historical item order-item-code. Meaning: Amazon's internal line item identifier.
Historical item merchant-order-item-id. Meaning: Seller's own line item reference.
Historical item merchant-adjustment-item-id. Meaning: Seller's adjustment reference.
Historical item sku. Meaning: Product SKU.
Historical item quantity-purchased. Meaning: Number of units in the order.
Historical item promotion-id. Meaning: Promotion identifier if a promotion was applied.
```

#### Historical transaction-type values

```text
Historical item Order. Meaning: Revenue from a customer order
Historical item Refund. Meaning: Refund issued to customer (reverses order amounts)
Historical item Service Fee. Meaning: Amazon service charges (subscription, advertising, FBA storage)
Historical item Adjustment. Meaning: Manual adjustments (reimbursements, corrections)
Historical item Transfer. Meaning: Settlement deposit to seller's bank account
Historical item Liquidations. Meaning: FBA liquidation proceeds
Historical item other. Meaning: Catch-all for miscellaneous events
```

#### Historical amount-type values

```text
Historical item ItemPrice. Meaning: Revenue components: Principal (product price), Shipping, GiftWrap, etc.
Historical item ItemFees. Meaning: Amazon fees: Commission (referral fee), FBAPerUnitFulfillmentFee, ShippingHB, etc.
Historical item Promotion. Meaning: Promotional discounts funded by the seller
Historical item ItemWithheldTax. Meaning: Tax withheld by Amazon on behalf of the seller
Historical item other. Meaning: Miscellaneous amounts
```

#### Historical Key amount-description values

```text
Historical item Principal. Meaning: Product sale price (revenue)
Historical item Shipping. Meaning: Shipping credit from buyer
Historical item ShippingTax. Meaning: Tax on shipping
Historical item Tax. Meaning: Product tax collected
Historical item GiftWrap. Meaning: Gift wrapping fee
Historical item Commission. Meaning: Amazon referral fee (percentage of sale price)
Historical item FBAPerUnitFulfillmentFee. Meaning: FBA pick, pack, and ship fee per unit
Historical item FBAPerOrderFulfillmentFee. Meaning: FBA per-order fee
Historical item FBAWeightBasedFee. Meaning: FBA weight-based shipping fee
Historical item ShippingHB. Meaning: Shipping handling fee
Historical item StorageRenewalBilling. Meaning: FBA monthly/long-term storage fees
Historical item Subscription. Meaning: Professional seller subscription ($39.99/mo)
Historical item PromotionShipping. Meaning: Seller-funded free shipping promotion
```

#### Historical 5 - Fee Structure

```text
Historical item Referral fee (Commission). How It Appears: transaction-type = Order, amount-type = ItemFees, amount-description = Commission. Typically 8 to 15% depending on category. Negative amount.
Historical item FBA fulfilment fee. How It Appears: transaction-type = Order, amount-type = ItemFees, amount-description = FBAPerUnitFulfillmentFee. Per-unit fee based on size/weight.
Historical item FBA storage fee. How It Appears: transaction-type = Service Fee, amount-description = StorageRenewalBilling. Monthly and long-term storage charges.
Historical item Professional seller subscription. How It Appears: transaction-type = Service Fee, amount-description = Subscription. $39.99/month.
Historical item Advertising fees. How It Appears: Separate report (Sponsored Products). Not in the settlement report.
Historical item Refund administration fee. How It Appears: When Amazon refunds a customer, the original referral fee may be partially retained. Appears as a positive ItemFees amount on the Refund row.
```

#### Historical 7 - Multi-Currency Handling

```text
Historical item Single marketplace. How It Appears: All rows in one currency matching the marketplace (USD for .com, GBP for .co.uk, EUR for .de/.fr/.it/.es).
Historical item Multiple marketplaces. How It Appears: Separate settlement reports per marketplace. Each in its own currency.
Historical item Amazon Currency Converter. How It Appears: If enabled, Amazon converts foreign marketplace revenue to the seller's home currency. Settlement total-amount is in home currency. Individual rows are in marketplace currency.
Historical item Cross-border FBA. How It Appears: Inventory in one country, sold in another. Settlement reports are per-marketplace regardless of inventory location.
```
