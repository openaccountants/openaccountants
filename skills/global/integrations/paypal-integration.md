---
name: paypal-integration
version: 2.0
category: bookkeeping
description: >
  Reconcile supplied paypal exports for bookkeeping in 2026. Establish the actual schema, account, dates and currency, preserve order/invoice/payment relationships, reject malformed or unreconciled data and prepare postings for human approval. Historical fields and sample data are retained, but current API, software and fee behaviour is not certified.
jurisdiction: GLOBAL
last_updated: 2026-11-14
tier: 2
domain: bookkeeping
tax_year: 2026
type: cross-country-method
checked_on: 2026-11-14
---

# PayPal activity and multi-currency reconciliation v2.0

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

### PayPal-specific controls

Distinguish Activity Download, balance-reconciliation data, monthly statement and transaction receipt. Parse actual headings, including locale variants such as `Datum`, `Brutto` and `Gebühr`, and confirm timezones before translating a cutoff. Preserve selected/omitted-field status as supplied; a remembered column position or maximum column count cannot identify the file. Counterparty email can help matching but is not a guaranteed unique legal-person identifier or reverse-charge proof.

Keep invoice references, original/refund reference IDs, balance impact and separate monthly/dispute fees alongside per-payment fees. Test `Gross + Fee = Net` only where the actual signed-fee mapping supports it. Do not restrict books to `Completed` labels or assume holds/releases cancel within the period. Pair conversion legs without treating their principal as revenue, but retain actual FX differences. Link withdrawals to bank deposits by evidence, not by summing every row between two withdrawals. Shipping charged to a buyer is not automatically deducted from revenue. Obtain tax detail and official reporting rules separately; the old universal PayPal DAC7 assertion is not confirmed.

## Worked case

In the supplied fixture, an independently supported illustrative GBP 3,100 opening balance gives GBP 2,927.23 closing; the EUR balance separately returns to zero. The GBP 415 conversion leg is not new sales revenue. Do not combine GBP and EUR totals into one balance.

```oa-check
name: PayPal activity and multi-currency reconciliation
inputs:
  opening_gbp: 3100
  receipt_one: 145.05
  receipt_two: 87.02
  refund_gbp: 150
  bank_transfer: 3000
  conversion_gbp: 415
  last_receipt: 2330.16
  eur_received_net: 485.1
  eur_converted: 485.1
steps:
  - closing_gbp: opening_gbp + receipt_one + receipt_two - refund_gbp - bank_transfer + conversion_gbp + last_receipt
  - closing_eur: eur_received_net - eur_converted
expected:
  closing_gbp: 2927.23
  closing_eur: 0
```

## Retained supplied-data fixtures

These are the original illustrations, retained byte-for-byte inside their code blocks. They are not certified current platform exports, fee schedules or complete accounts. Use the worked control above and the validation method before using any record. A failed example must remain failed, not silently repaired.

```csv
Date,Time,TimeZone,Name,Type,Status,Currency,Gross,Fee,Net,From Email Address,To Email Address,Transaction ID,Item Title,Invoice Number,Reference Txn ID,Balance,Balance Impact
03/15/2026,14:23:45,GMT,Alice Johnson,Web Accept Payment Received,Completed,GBP,150.00,-4.95,145.05,alice@example.com,merchant@business.com,5TY89012ABCD3456E,Web Development Services,INV-1042,,3245.05,Credit
03/15/2026,16:00:12,GMT,Bob Smith,Express Checkout Payment Received,Completed,GBP,89.99,-2.97,87.02,bob@example.com,merchant@business.com,6UV01234EFGH5678I,Monthly Subscription,,, 3332.07,Credit
03/16/2026,09:30:00,GMT,Alice Johnson,Refund,Completed,GBP,-150.00,0.00,-150.00,merchant@business.com,alice@example.com,7WX23456IJKL7890M,,INV-1042,5TY89012ABCD3456E,3182.07,Debit
03/17/2026,11:15:22,GMT,,Transfer to Bank,Completed,GBP,-3000.00,0.00,-3000.00,,merchant@business.com,8YZ34567MNOP8901Q,,,, 182.07,Debit
03/18/2026,08:45:33,GMT,Acme GmbH,Express Checkout Payment Received,Completed,EUR,500.00,-14.90,485.10,acme@example.de,merchant@business.com,9AB45678QRST0123U,Consulting Package,,, 485.10,Credit
03/18/2026,08:45:34,GMT,,Currency Conversion,Completed,EUR,-485.10,0.00,-485.10,,merchant@business.com,0CD56789UVWX1234Y,,,9AB45678QRST0123U,0.00,Debit
03/18/2026,08:45:34,GMT,,Currency Conversion,Completed,GBP,415.00,0.00,415.00,,merchant@business.com,1EF67890XYZA2345B,,,9AB45678QRST0123U,597.07,Credit
03/19/2026,10:00:00,GMT,Widget Corp,Payment Received,Completed,GBP,2400.00,-69.84,2330.16,widget@example.com,merchant@business.com,2GH78901BCDE3456F,Enterprise License,INV-1043,,2927.23,Credit
```

## Existing review requirement

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

## Sources

| Official source | Read on | Read scope |
|---|---|---|
| https://www.gov.uk/self-employed-records/what-records-to-keep | 2026-11-14 | Read for sales/expense proof, accurate records, distinguishing business transactions and accrual records. |
| https://www.gov.uk/expenses-if-youre-self-employed/legal-financial | 2026-11-14 | Read for business bank/credit-card charges, loan principal exclusion and bad debts/cash-basis distinction for UK sole traders and partners. |
| https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a | 2026-11-14 | Read for sections 2-6 and 13, actual supply, belonging, reverse-charge conditions, input-tax limits and unregistered recipients. |
| https://standards.aasb.gov.au/sites/default/files/2026-11/AASB 15_12-14_COMPdec22_07-26.pdf | 2026-11-14 | Read for paragraphs 47,105-108,B34-B38 and B44-B47 for third-party collections, receivables/contract liabilities, principal-agent control and unexercised rights. Conditional Australian IFRS-equivalent financial-reporting scope, not worldwide tax law. |
| https://standards.aasb.gov.au/sites/default/files/2025-03/AASB 121_08-15_COMPoct23_01-25.pdf | 2026-11-14 | Read for paragraphs 20-23 and 27-30, initial recognition, monetary closing balances and settlement exchange differences; Australian IFRS-equivalent financial reporting, not universal tax translation. |

Not yet confirmed: the live paypal API/schema, exact export/import column positions and availability, UI/report paths, region/plan capabilities, pricing and fee/refund conventions, automatic tax/FX behaviour, regulatory status and third-party document acceptance. The following literal table/path inventory records what the old file claimed, only to help locate and compare supplied data. Its fees, codes, timing, default settings and field meanings are historical and must not be treated as 2026 guidance. Known accounting/tax errors are replaced by the method and country boundaries above. No vendor source was used.

### Historical schema and claim inventory, not usable guidance

#### Historical 2 - Export Formats

```text
Historical item CSV. Use Case: Activity Download Report (up to 41 columns, max 50,000 rows, max 12 months per export, 7-year history)
Historical item TAB. Use Case: Tab-separated alternative to CSV
Historical item PDF. Use Case: Monthly statements, individual transaction receipts
Historical item QIF. Use Case: Quicken import format
Historical item IIF. Use Case: QuickBooks Desktop import format (US only)
```

#### Historical Activity Download CSV - All Available Columns

```text
Historical item 1. Column Header: Date; State: Mandatory; Meaning: Completion date. MM/DD/YYYY (US), DD/MM/YYYY (non-US). Locale-dependent.
Historical item 2. Column Header: Time; State: Mandatory; Meaning: Completion time. HH:MM:SS format.
Historical item 3. Column Header: TimeZone; State: Mandatory; Meaning: Timezone string (e.g., "PST", "GMT", "CET").
Historical item 4. Column Header: Name; State: Mandatory; Meaning: Counterparty name (buyer/seller/recipient).
Historical item 5. Column Header: Type; State: Mandatory; Meaning: Transaction type description (see Section 4).
Historical item 6. Column Header: Status; State: Mandatory; Meaning: Completed, Pending, Denied, Reversed, Refunded, etc.
Historical item 7. Column Header: Currency; State: Mandatory; Meaning: Three-letter ISO code (USD, GBP, EUR).
Historical item 8. Column Header: Gross; State: Mandatory; Meaning: Gross transaction amount including tax/shipping. Positive = received, negative = sent.
Historical item 9. Column Header: Fee; State: Mandatory; Meaning: PayPal fee. Negative number (deducted from gross). Zero for non-fee transactions.
Historical item 10. Column Header: Net; State: Mandatory; Meaning: Net amount (Gross + Fee, since Fee is negative).
Historical item 11. Column Header: From Email Address; State: Mandatory; Meaning: Sender's PayPal email.
Historical item 12. Column Header: To Email Address; State: Mandatory; Meaning: Recipient's PayPal email.
Historical item 13. Column Header: Transaction ID; State: Mandatory; Meaning: Unique 17-character PayPal transaction ID.
Historical item 14. Column Header: Counterparty Status; State: Mandatory; Meaning: Verified / Unverified.
Historical item 15. Column Header: Shipping Address; State: Unselected; Meaning: Full shipping address (single field).
Historical item 16. Column Header: Address Status; State: Unselected; Meaning: Confirmed / Unconfirmed.
Historical item 17. Column Header: Item Title; State: Selected; Meaning: Product/service name from the payment.
Historical item 18. Column Header: Item ID; State: Selected; Meaning: Product/item identifier.
Historical item 19. Column Header: Shipping and Handling Amount; State: Unselected; Meaning: Shipping cost.
Historical item 20. Column Header: Insurance Amount; State: Unselected; Meaning: Insurance cost.
Historical item 21. Column Header: Sales Tax; State: Unselected; Meaning: Tax amount on the transaction.
Historical item 22. Column Header: Option 1 Name; State: Unselected; Meaning: Custom field name (e.g., "Size").
Historical item 23. Column Header: Option 1 Value; State: Unselected; Meaning: Custom field value (e.g., "Large").
Historical item 24. Column Header: Option 2 Name; State: Unselected; Meaning: Additional custom field name.
Historical item 25. Column Header: Option 2 Value; State: Unselected; Meaning: Additional custom field value.
Historical item 26. Column Header: Reference Txn ID; State: Selected; Meaning: Original transaction ID for refunds/reversals. Links refund to original payment.
Historical item 27. Column Header: Invoice Number; State: Selected; Meaning: Your invoice reference.
Historical item 28. Column Header: Custom Number; State: Unselected; Meaning: Merchant-defined custom field.
Historical item 29. Column Header: Quantity; State: Unselected; Meaning: Item quantity.
Historical item 30. Column Header: Receipt ID; State: Unselected; Meaning: PayPal receipt identifier.
Historical item 31. Column Header: Balance; State: Selected; Meaning: Running balance after transaction.
Historical item 32. Column Header: Address Line 1; State: Unselected; Meaning: Street address.
Historical item 33. Column Header: Address Line 2; State: Unselected; Meaning: Address line 2.
Historical item 34. Column Header: Town/City; State: Unselected; Meaning: City.
Historical item 35. Column Header: State/Province; State: Unselected; Meaning: State or province.
Historical item 36. Column Header: Zip/Postal Code; State: Unselected; Meaning: Postal code.
Historical item 37. Column Header: Country; State: Unselected; Meaning: Country name.
Historical item 38. Column Header: Contact Phone Number; State: Unselected; Meaning: Buyer's phone number.
Historical item 39. Column Header: Subject; State: Selected; Meaning: Payment subject/memo.
Historical item 40. Column Header: Note; State: Unselected; Meaning: Payment note from buyer.
Historical item 41. Column Header: Country Code; State: Unselected; Meaning: Two-letter country code (US, GB, DE).
Historical item 42. Column Header: Balance Impact; State: Selected; Meaning: "Credit" (money in) or "Debit" (money out).
```

#### Historical 4 - Transaction Type Codes

```text
Historical item Web Accept Payment Received. Meaning: Payment received via PayPal button/checkout; Balance Impact: Credit
Historical item Express Checkout Payment Received. Meaning: Payment via Express Checkout; Balance Impact: Credit
Historical item Mobile Payment Received. Meaning: Payment received via mobile; Balance Impact: Credit
Historical item Payment Received. Meaning: Generic incoming payment; Balance Impact: Credit
Historical item Invoice Received. Meaning: Payment received against a PayPal invoice; Balance Impact: Credit
Historical item Recurring Payment Received. Meaning: Subscription/recurring charge collected; Balance Impact: Credit
Historical item Payment Sent. Meaning: Outgoing payment to another PayPal user; Balance Impact: Debit
Historical item Refund. Meaning: Refund issued to buyer (reverses a previous payment); Balance Impact: Debit
Historical item Payment Reversal. Meaning: Chargeback or dispute reversal; Balance Impact: Debit
Historical item Temporary Hold. Meaning: Funds temporarily held by PayPal (disputes, reviews); Balance Impact: Debit
Historical item Payment Release. Meaning: Held funds released; Balance Impact: Credit
Historical item Transfer to Bank. Meaning: Withdrawal to linked bank account; Balance Impact: Debit
Historical item Bank Deposit to PayPal. Meaning: Deposit from linked bank account; Balance Impact: Credit
Historical item Currency Conversion. Meaning: FX conversion between currencies; Balance Impact: Both
Historical item General Authorization. Meaning: Pre-authorisation (no funds moved yet); Balance Impact: None
Historical item PayPal fee. Meaning: Monthly/service fee charged by PayPal; Balance Impact: Debit
```

#### Historical 5 - Fee Structure

```text
Historical item Domestic payment processing. Typical Rate: 2.99% + $0.49 (US standard); How It Appears: Negative value in Fee column of the payment row
Historical item International payment processing. Typical Rate: 4.49% + fixed fee; How It Appears: Negative value in Fee column
Historical item Micropayment rate. Typical Rate: 5% + $0.05 (for transactions under $10); How It Appears: Negative value in Fee column
Historical item Currency conversion spread. Typical Rate: ~3-4% above mid-market rate; How It Appears: NOT shown as a fee. Embedded in the exchange rate.
Historical item Chargeback fee. Typical Rate: $20; How It Appears: Separate transaction row with Type = "Payment Reversal"
Historical item Withdrawal fee. Typical Rate: Usually free for standard, $0.25 for instant; How It Appears: Separate row or deducted from withdrawal
Historical item Monthly fee. Typical Rate: Varies by plan; How It Appears: Separate row with Type = "PayPal fee"
Historical item Invoicing fee. Typical Rate: 2.99% + $0.49; How It Appears: In Fee column of the invoice payment row
```

#### Historical 7 - Multi-Currency Handling

```text
Historical item Single-currency. How It Appears: All rows share the same Currency value. Straightforward.
Historical item Received in foreign currency, held. How It Appears: Payment row shows Currency = foreign currency, Gross = foreign amount. Balance Impact = Credit.
Historical item Received and auto-converted. How It Appears: Two rows: (1) Payment received in foreign currency, (2) "Currency Conversion" row showing the conversion. Both share a related Transaction ID.
Historical item Currency conversion. How It Appears: Two rows: a debit in the source currency and a credit in the target currency. The exchange rate is NOT shown as a separate column , it must be calculated from the two amounts.
Historical item Withdrawal in non-default currency. How It Appears: PayPal converts to the bank's currency. Conversion row appears before the withdrawal row.
```

#### Historical navigation and API descriptions

```text
The Activity Download CSV is accessed via: Activity page > Statements > Activity Download > Select date range > Choose CSV format > Download.
```

#### Historical tax-field names, definitions require actual supplied mapping

- Sales Tax; retain as an investigation field, not proof of tax treatment.
- Country / Country Code; retain as an investigation field, not proof of tax treatment.
- Invoice Number; retain as an investigation field, not proof of tax treatment.
- Gross vs Net; retain as an investigation field, not proof of tax treatment.
- Currency; retain as an investigation field, not proof of tax treatment.
- 1099-K reporting (US); retain as an investigation field, not proof of tax treatment.
- DAC7 reporting (EU); retain as an investigation field, not proof of tax treatment.
