---
name: shopify-integration
description: "Reconcile supplied shopify exports for bookkeeping in 2026. Establish the actual schema, account, dates and currency, preserve order/invoice/payment relationships, reject malformed or unreconciled data and prepare postings for human approval. Historical fields and sample data are retained, but current API, software and fee behaviour is not certified."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/shopify-integration"
  jurisdiction: "GLOBAL"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Shopify orders, payments and payout reconciliation v2.0

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
6. **Prepare the commercial accounting.** Link the invoice/order/bill and payment, preserve tax and shipping detail, and separate amounts collected for others. A customer shipping charge can be part of the seller's consideration; it is not automatically removed from revenue. Gross cash does not always equal revenue, and a net payout is not by itself proof of agency. Under an applicable AASB 15/IFRS-equivalent reporting policy, assess control of each specified good/service, principal versus agent and third-party collections using paragraphs 47 and B34-B38. That conditional financial-reporting test does not replace local tax law. [AASB 15](https://standards.aasb.gov.au/sites/default/files/2026-11/AASB15_12-14_COMPdec22_07-26.pdf).
7. **Apply the owning country's tax method.** Currency, marketplace suffix, email, billing country or a configured software tax code alone does not establish tax jurisdiction, business status, nexus or recoverability. Read the actual supply, establishment, customer, product, destination and registrations; link the official rule used. A payment-only file may lack the tax breakdown. UK sole-trader/partner records must identify business transactions and preserve receipts, invoices and statements; traditional accounting also tracks amounts owed/unpaid. Eligible UK business bank charges are distinct from non-deductible loan principal. [HMRC records](https://www.gov.uk/self-employed-records/what-records-to-keep); [financial charges](https://www.gov.uk/expenses-if-youre-self-employed/legal-financial).
8. **Handle foreign currency without losing either leg.** Keep original, settlement and functional-currency amounts and rate directions. Pair own-account conversion/transfer legs using documented IDs and accounts, not timestamp proximity alone. Transfer principal is not a sale, but settlement/translation differences and separately evidenced charges require their own treatment. For an applicable AASB 121/IFRS-equivalent reporting policy, use recognition-date rates, closing rates for monetary balances and the stated settlement-difference exceptions. An average is acceptable only when it reasonably approximates actual rates. Tax translation follows its own country's method. [AASB 121 paragraphs 21-23,27-30](https://standards.aasb.gov.au/sites/default/files/2025-03/AASB121_08-15_COMPoct23_01-25.pdf).
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

### Shopify-specific controls

Keep order-level/line-level data, payment balance activity and payout summaries separate. Preserve order/payment/checkout/payout IDs, fulfilment and financial status, partial captures, multi-tender orders, POS/online distinctions and partial refunds. Validate actual plain versus spreadsheet CSV headings; the old menu path and blanket rejection of an Excel variant are not verified current software behaviour. Do not infer payout membership from a date alone.

For multi-line orders, count an order-level Total, Taxes or Shipping only once after confirming consistent repeated values. Establish whether Subtotal already includes discounts; subtracting a separate discount again can understate revenue. In the retained sample, #1002 has Total 129.99 repeated on two rows. Its 99.99 subtotal plus 10 shipping plus 20 tax already equals 129.99, so subtracting the shown 10 discount again gives the wrong 119.99. The item-price detail does not fully bridge to that subtotal; obtain the full order before final posting.

The payments fixture includes a Unicode minus sign on the dispute. Preserve raw bytes, normalise only in a logged calculation field and retain the unsettled dispute in the balance control. Fees in this supplied fixture are positive, but test the actual file rather than asserting a universal sign. Obtain shipping-label/subscription/third-party-provider charges and payout summaries where relevant; do not presume every fee is in one export. For an applicable AASB 15 policy, customer prepayments create a contract liability before performance, and gift-card breakage/unclaimed-property treatment requires paragraphs 106 and B44-B47 plus applicable law. Never treat all gift-card cash as immediate sales or omit later redemption. Tax configuration, billing province and currency do not prove the correct tax liability or nexus.

## Worked case

The retained #1002 order contributes USD 129.99 once, not USD 259.98 and not USD 119.99. The first payout group totals USD 174.16. Other supplied payout groups total negative USD 26.03 and positive USD 304.35; the unallocated dispute is negative USD 144.99 and requires its own cutoff/balance control.

```oa-check
name: Shopify orders, payments and payout reconciliation
inputs:
  subtotal: 99.99
  shipping: 10
  tax: 20
  discount_already_reflected: 10
  repeated_rows: 2
  payout_one_a: 48.24
  payout_one_b: 125.92
steps:
  - order_total: subtotal + shipping + tax
  - naive_double_total: order_total * repeated_rows
  - wrong_discount_total: order_total - discount_already_reflected
  - first_payout: payout_one_a + payout_one_b
expected:
  order_total: 129.99
  naive_double_total: 259.98
  wrong_discount_total: 119.99
  first_payout: 174.16
```

## Retained supplied-data fixtures

These are the original illustrations, retained byte-for-byte inside their code blocks. They are not certified current platform exports, fee schedules or complete accounts. Use the worked control above and the validation method before using any record. A failed example must remain failed, not silently repaired.

```csv
Transaction Date,Type,Order,Card Brand,Card Source,Payout Status,Payout Date,Available On,Amount,Fee,Net,Currency,Checkout,Payment Method,Payout ID
2026-03-15 14:23:45 -0500,charge,#1001,visa,online,paid,2026-03-17,2026-03-17,49.99,1.75,48.24,USD,abc123def456,shopify_payments,pay_1234
2026-03-15 16:10:00 -0500,charge,#1002,mastercard,online,paid,2026-03-17,2026-03-17,129.99,4.07,125.92,USD,ghi789jkl012,shopify_payments,pay_1234
2026-03-16 09:30:22 -0500,charge,#1003,amex,contactless,paid,2026-03-18,2026-03-18,24.99,1.03,23.96,USD,mno345pqr678,shopify_payments,pay_1235
2026-03-16 11:45:00 -0500,refund,#1001,visa,,paid,2026-03-18,2026-03-18,-49.99,0.00,-49.99,USD,,shopify_payments,pay_1235
2026-03-17 08:00:00 -0500,charge,#1004,visa,online,paid,2026-03-19,2026-03-19,299.00,8.97,290.03,USD,stu901vwx234,shopify_payments,pay_1236
2026-03-17 14:15:33 -0500,charge,#1005,mastercard,chip,paid,2026-03-19,2026-03-19,15.00,0.68,14.32,USD,yza567bcd890,shopify_payments,pay_1236
2026-03-18 10:00:00 -0500,dispute,#1002,mastercard,,pending,,,−129.99,15.00,−144.99,USD,,shopify_payments,
```

```csv
Name,Email,Financial Status,Paid at,Currency,Subtotal,Shipping,Taxes,Total,Discount Code,Discount Amount,Lineitem quantity,Lineitem name,Lineitem price,Lineitem sku,Payment Method
#1001,alice@example.com,paid,2026-03-15,USD,39.99,5.00,5.00,49.99,,,1,Wireless Mouse,39.99,WM-001,Shopify Payments
#1002,bob@example.com,paid,2026-03-15,USD,99.99,10.00,20.00,129.99,SAVE10,10.00,1,Mechanical Keyboard,99.99,KB-002,Shopify Payments
#1002,bob@example.com,paid,2026-03-15,USD,99.99,10.00,20.00,129.99,SAVE10,10.00,1,USB-C Hub,29.99,HUB-003,Shopify Payments
```

## Existing review requirement

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

## Sources

| Official source | Read on | Read scope |
|---|---|---|
| https://www.gov.uk/self-employed-records/what-records-to-keep | 2026-11-14 | Read for sales/expense proof, accurate records, distinguishing business transactions and accrual records. |
| https://www.gov.uk/expenses-if-youre-self-employed/legal-financial | 2026-11-14 | Read for business bank/credit-card charges, loan principal exclusion and bad debts/cash-basis distinction for UK sole traders and partners. |
| https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a | 2026-11-14 | Read for sections 2-6 and 13, actual supply, belonging, reverse-charge conditions, input-tax limits and unregistered recipients. |
| https://standards.aasb.gov.au/sites/default/files/2026-11/AASB15_12-14_COMPdec22_07-26.pdf | 2026-11-14 | Read for paragraphs 47 and 105-108,B34-B38 and B44-B47 for third-party collections, receivables/contract liabilities, principal-agent control and unexercised rights. Conditional Australian IFRS-equivalent financial-reporting scope, not worldwide tax law. |
| https://standards.aasb.gov.au/sites/default/files/2025-03/AASB121_08-15_COMPoct23_01-25.pdf | 2026-11-14 | Read for paragraphs 20-23 and 27-30, initial recognition, monetary closing balances and settlement exchange differences; Australian IFRS-equivalent financial reporting, not universal tax translation. |

Not yet confirmed: the live shopify API/schema, exact export/import column positions and availability, UI/report paths, region/plan capabilities, pricing and fee/refund conventions, automatic tax/FX behaviour, regulatory status and third-party document acceptance. The following literal table/path inventory records what the old file claimed, only to help locate and compare supplied data. Its fees, codes, timing, default settings and field meanings are historical and must not be treated as 2026 guidance. Known accounting/tax errors are replaced by the method and country boundaries above. No vendor source was used.

### Historical schema and claim inventory, not usable guidance

#### Historical 2 - Export Formats

```text
Historical item CSV (Plain). Use Case: Payments transactions (from Finance > Payouts > View Transactions > Export > Plain CSV). The correct format for accounting.
Historical item CSV for Excel. Use Case: Payments transactions with extra formatting rows. Breaks most import tools , avoid for accounting.
Historical item CSV. Use Case: Orders export (from Orders page > Export). Order-level data with line items.
Historical item PDF. Use Case: Individual order invoices, packing slips.
Historical item Excel (XLSX). Use Case: Financial summary reports.
```

#### Historical Shopify Payments CSV (Plain - Finance > Payouts)

```text
Historical item Transaction Date. Meaning: Timestamp with timezone. Format: YYYY-MM-DD HH:MM:SS ±HHMM (e.g., 2026-03-15 14:23:45 -0500).
Historical item Type. Meaning: Transaction type (see Section 4).
Historical item Order. Meaning: Shopify order number (e.g., #1001). Blank for non-order transactions.
Historical item Card Brand. Meaning: Card brand used (visa, mastercard, amex, etc.). Blank for non-card payments.
Historical item Card Source. Meaning: How the card was used (direct, online, swipe, chip, contactless).
Historical item Payout Status. Meaning: pending, paid, in_transit, failed.
Historical item Payout Date. Meaning: Date the payout was sent to the bank.
Historical item Available On. Meaning: Date the funds become available.
Historical item Amount. Meaning: Transaction amount in settlement currency. Positive for charges, negative for refunds.
Historical item Fee. Meaning: Shopify Payments processing fee. Stored as a POSITIVE number (unlike PayPal which uses negative).
Historical item Net. Meaning: Net amount (Amount - Fee). This is what gets deposited.
Historical item Currency. Meaning: Three-letter ISO code (USD, GBP, EUR, CAD). Uppercase.
Historical item Checkout. Meaning: Shopify checkout token (internal reference).
Historical item Payment Method. Meaning: Payment method type (shopify_payments, manual, gift_card, etc.).
Historical item Payout ID. Meaning: Identifier linking to a specific bank payout.
```

#### Historical Shopify Orders Export CSV

```text
Historical item Name. Meaning: Order number (e.g., #1001).
Historical item Email. Meaning: Customer email address.
Historical item Phone. Meaning: Customer phone number.
Historical item Financial Status. Meaning: paid, authorized, partially_paid, partially_refunded, refunded, pending, voided.
Historical item Paid at. Meaning: Date payment was captured.
Historical item Fulfillment Status. Meaning: fulfilled, partial, unfulfilled, restocked.
Historical item Fulfilled at. Meaning: Date order was shipped.
Historical item Currency. Meaning: Order currency (ISO code).
Historical item Subtotal. Meaning: Order total before shipping and taxes.
Historical item Shipping. Meaning: Shipping amount charged.
Historical item Taxes. Meaning: Total tax amount.
Historical item Total. Meaning: Grand total (Subtotal + Shipping + Taxes - Discounts).
Historical item Discount Code. Meaning: Discount code applied (if any).
Historical item Discount Amount. Meaning: Discount value applied.
Historical item Shipping Method. Meaning: Shipping method name.
Historical item Created at. Meaning: Order creation timestamp.
Historical item Lineitem quantity. Meaning: Quantity of the line item.
Historical item Lineitem name. Meaning: Product name.
Historical item Lineitem price. Meaning: Unit price of the line item.
Historical item Lineitem sku. Meaning: Product SKU.
Historical item Lineitem requires shipping. Meaning: true/false.
Historical item Lineitem taxable. Meaning: true/false.
Historical item Lineitem fulfillment status. Meaning: fulfilled/unfulfilled.
Historical item Billing Name. Meaning: Customer billing name.
Historical item Billing Address1. Meaning: Billing street address.
Historical item Billing City. Meaning: Billing city.
Historical item Billing Province. Meaning: Billing state/province.
Historical item Billing Country. Meaning: Billing country.
Historical item Billing Zip. Meaning: Billing postal code.
Historical item Payment Method. Meaning: How the order was paid.
Historical item Payment ID(s). Meaning: Unique payment IDs for matching to Shopify Payments data.
```

#### Historical Shopify Payments CSV types

```text
Historical item charge. Meaning: Successful payment collected from customer
Historical item refund. Meaning: Full or partial refund to customer
Historical item dispute. Meaning: Chargeback initiated by cardholder
Historical item reserve_payout. Meaning: Funds released from Shopify's reserve
Historical item adjustment. Meaning: Manual adjustment by Shopify
Historical item payout. Meaning: Transfer to merchant's bank account
```

#### Historical Orders CSV Financial Status values

```text
Historical item paid. Meaning: Fully paid
Historical item authorized. Meaning: Card authorized but not captured
Historical item partially_paid. Meaning: Deposit or partial payment received
Historical item partially_refunded. Meaning: Some items refunded
Historical item refunded. Meaning: Fully refunded
Historical item pending. Meaning: Awaiting payment
Historical item voided. Meaning: Authorization voided
```

#### Historical 5 - Fee Structure

```text
Historical item Shopify Payments (online, domestic). Typical Rate: 2.9% + $0.30 (Basic), 2.6% + $0.30 (Shopify), 2.4% + $0.30 (Advanced); How It Appears: Positive value in Fee column per charge row
Historical item Shopify Payments (in-person). Typical Rate: 2.7% + $0.00 (Basic), 2.5% + $0.00 (Shopify), 2.4% + $0.00 (Advanced); How It Appears: Positive value in Fee column
Historical item International card surcharge. Typical Rate: +1.5%; How It Appears: Added to base fee
Historical item Currency conversion fee. Typical Rate: +1.5%; How It Appears: Added when customer currency ≠ store currency
Historical item Chargeback fee. Typical Rate: $15 (US); How It Appears: Separate charge on the dispute row
Historical item Third-party payment provider fee. Typical Rate: 2% / 1% / 0.5%; How It Appears: Not in Payments CSV , billed separately by Shopify
Historical item Shopify subscription. Typical Rate: $39 to 399/month; How It Appears: Not in transaction exports , billed to account
Historical item Refund fee. Typical Rate: Processing fee NOT returned; How It Appears: Original Fee remains; no fee on refund row
```

#### Historical 7 - Multi-Currency Handling

```text
Historical item Single-currency store. How It Appears: All transactions in one currency. Currency column is consistent.
Historical item Multi-currency store (Shopify Payments). How It Appears: Amount and Fee are in the store's settlement (payout) currency. Customer may have paid in a different currency.
Historical item Customer-facing currency. How It Appears: Not visible in the Payments CSV. Available in the Orders CSV via Currency column.
Historical item Exchange rate. How It Appears: Not shown in CSV exports. Shopify converts at its own rate (includes 1.5% conversion fee).
Historical item International pricing. How It Appears: Shopify Markets may show different prices per country. The Orders CSV shows what the customer paid in their currency; the Payments CSV shows the settlement amount.
```

#### Historical navigation and API descriptions

```text
### Shopify Payments CSV (Plain , Finance > Payouts)
Shopify can be configured to collect taxes automatically based on product taxability and customer location. Tax amounts in the Orders CSV reflect what was actually charged. For detailed tax reporting by jurisdiction, use Shopify's Tax report in Finance > Reports, not the Orders CSV.
1. **Orders CSV vs Payments CSV confusion.** Users often export from Orders instead of Finance > Payouts. The Orders CSV does not include processing fees and does not match bank deposits.
```

#### Historical tax-field names, definitions require actual supplied mapping

- Taxes (historical location Orders CSV); retain as an investigation field, not proof of tax treatment.
- Lineitem taxable (historical location Orders CSV); retain as an investigation field, not proof of tax treatment.
- Billing Country (historical location Orders CSV); retain as an investigation field, not proof of tax treatment.
- Billing Province (historical location Orders CSV); retain as an investigation field, not proof of tax treatment.
- Currency (historical location Both CSVs); retain as an investigation field, not proof of tax treatment.
- Tax lines (not in CSV) (historical location Shopify admin/API); retain as an investigation field, not proof of tax treatment.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `shopify-integration` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/shopify-integration. If neither is available, confirm every figure against the official source pages cited above before relying on it.
