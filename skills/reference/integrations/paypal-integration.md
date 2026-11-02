---
name: paypal-integration
version: 1.0
category: integration
description: >
  Integration skill for PayPal activity download CSV exports. Activate when the user uploads a PayPal CSV,
  PayPal activity report, or mentions PayPal transactions. This is one of the messiest exports in common use.
jurisdiction: GLOBAL
tier: 2
last_updated: 2026-06-12
---

# PayPal Integration Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Section 1 — Platform Overview

PayPal is a global payment platform used by individuals and businesses for online payments, invoicing, and money transfers. Headquartered in the US, PayPal operates in 200+ markets and supports 25+ currencies. It serves everyone from eBay sellers and freelancers to enterprise e-commerce businesses.

PayPal's Activity Download CSV is notoriously complex — up to 41 columns, fees as separate transaction rows, multiple transaction types, and locale-dependent formatting. It is widely considered the most difficult payment platform export to reconcile.

---

## Section 2 — Export Formats

| Format | Use Case |
|--------|----------|
| CSV | Activity Download Report (up to 41 columns, max 50,000 rows, max 12 months per export, 7-year history) |
| TAB | Tab-separated alternative to CSV |
| PDF | Monthly statements, individual transaction receipts |
| QIF | Quicken import format |
| IIF | QuickBooks Desktop import format (US only) |

The Activity Download CSV is accessed via: Activity page > Statements > Activity Download > Select date range > Choose CSV format > Download.

For merchants with high volume, PayPal also offers the **Balance Reconciliation Report** (SFTP-delivered CSV with structured header/body/footer format).

---

## Section 3 — Column Mapping

### Activity Download CSV — All Available Columns

| Position | Column Header | State | Meaning |
|----------|---------------|-------|---------|
| 1 | Date | Mandatory | Completion date. MM/DD/YYYY (US), DD/MM/YYYY (non-US). Locale-dependent. |
| 2 | Time | Mandatory | Completion time. HH:MM:SS format. |
| 3 | TimeZone | Mandatory | Timezone string (e.g., "PST", "GMT", "CET"). |
| 4 | Name | Mandatory | Counterparty name (buyer/seller/recipient). |
| 5 | Type | Mandatory | Transaction type description (see Section 4). |
| 6 | Status | Mandatory | Completed, Pending, Denied, Reversed, Refunded, etc. |
| 7 | Currency | Mandatory | Three-letter ISO code (USD, GBP, EUR). |
| 8 | Gross | Mandatory | Gross transaction amount including tax/shipping. Positive = received, negative = sent. |
| 9 | Fee | Mandatory | PayPal fee. Negative number (deducted from gross). Zero for non-fee transactions. |
| 10 | Net | Mandatory | Net amount (Gross + Fee, since Fee is negative). |
| 11 | From Email Address | Mandatory | Sender's PayPal email. |
| 12 | To Email Address | Mandatory | Recipient's PayPal email. |
| 13 | Transaction ID | Mandatory | Unique 17-character PayPal transaction ID. |
| 14 | Counterparty Status | Mandatory | Verified / Unverified. |
| 15 | Shipping Address | Unselected | Full shipping address (single field). |
| 16 | Address Status | Unselected | Confirmed / Unconfirmed. |
| 17 | Item Title | Selected | Product/service name from the payment. |
| 18 | Item ID | Selected | Product/item identifier. |
| 19 | Shipping and Handling Amount | Unselected | Shipping cost. |
| 20 | Insurance Amount | Unselected | Insurance cost. |
| 21 | Sales Tax | Unselected | Tax amount on the transaction. |
| 22 | Option 1 Name | Unselected | Custom field name (e.g., "Size"). |
| 23 | Option 1 Value | Unselected | Custom field value (e.g., "Large"). |
| 24 | Option 2 Name | Unselected | Additional custom field name. |
| 25 | Option 2 Value | Unselected | Additional custom field value. |
| 26 | Reference Txn ID | Selected | Original transaction ID for refunds/reversals. Links refund to original payment. |
| 27 | Invoice Number | Selected | Your invoice reference. |
| 28 | Custom Number | Unselected | Merchant-defined custom field. |
| 29 | Quantity | Unselected | Item quantity. |
| 30 | Receipt ID | Unselected | PayPal receipt identifier. |
| 31 | Balance | Selected | Running balance after transaction. |
| 32 | Address Line 1 | Unselected | Street address. |
| 33 | Address Line 2 | Unselected | Address line 2. |
| 34 | Town/City | Unselected | City. |
| 35 | State/Province | Unselected | State or province. |
| 36 | Zip/Postal Code | Unselected | Postal code. |
| 37 | Country | Unselected | Country name. |
| 38 | Contact Phone Number | Unselected | Buyer's phone number. |
| 39 | Subject | Selected | Payment subject/memo. |
| 40 | Note | Unselected | Payment note from buyer. |
| 41 | Country Code | Unselected | Two-letter country code (US, GB, DE). |
| 42 | Balance Impact | Selected | "Credit" (money in) or "Debit" (money out). |

"State" column indicates whether the field is included in the default download (Mandatory/Selected) or must be manually enabled (Unselected).

---

## Section 4 — Transaction Type Codes

PayPal uses verbose, human-readable type descriptions:

| Type | Meaning | Balance Impact |
|------|---------|----------------|
| Web Accept Payment Received | Payment received via PayPal button/checkout | Credit |
| Express Checkout Payment Received | Payment via Express Checkout | Credit |
| Mobile Payment Received | Payment received via mobile | Credit |
| Payment Received | Generic incoming payment | Credit |
| Invoice Received | Payment received against a PayPal invoice | Credit |
| Recurring Payment Received | Subscription/recurring charge collected | Credit |
| Payment Sent | Outgoing payment to another PayPal user | Debit |
| Refund | Refund issued to buyer (reverses a previous payment) | Debit |
| Payment Reversal | Chargeback or dispute reversal | Debit |
| Temporary Hold | Funds temporarily held by PayPal (disputes, reviews) | Debit |
| Payment Release | Held funds released | Credit |
| Transfer to Bank | Withdrawal to linked bank account | Debit |
| Bank Deposit to PayPal | Deposit from linked bank account | Credit |
| Currency Conversion | FX conversion between currencies | Both |
| General Authorization | Pre-authorisation (no funds moved yet) | None |
| PayPal fee | Monthly/service fee charged by PayPal | Debit |

---

## Section 5 — Fee Structure

| Fee Type | Typical Rate | How It Appears |
|----------|-------------|----------------|
| Domestic payment processing | 2.99% + $0.49 (US standard) | Negative value in Fee column of the payment row |
| International payment processing | 4.49% + fixed fee | Negative value in Fee column |
| Micropayment rate | 5% + $0.05 (for transactions under $10) | Negative value in Fee column |
| Currency conversion spread | ~3-4% above mid-market rate | NOT shown as a fee. Embedded in the exchange rate. |
| Chargeback fee | $20 | Separate transaction row with Type = "Payment Reversal" |
| Withdrawal fee | Usually free for standard, $0.25 for instant | Separate row or deducted from withdrawal |
| Monthly fee | Varies by plan | Separate row with Type = "PayPal fee" |
| Invoicing fee | 2.99% + $0.49 | In Fee column of the invoice payment row |

Critical: PayPal fees appear in the **same row** as the payment (in the Fee column), unlike Wise where fees are separate rows.

---

## Section 6 — Tax-Relevant Fields

| Field | Notes |
|-------|-------|
| Sales Tax | Column 21. Contains the tax amount if the buyer paid tax through PayPal. Often blank — most merchants handle tax externally. |
| Country / Country Code | Buyer's country. Critical for determining cross-border VAT obligations (EU distance selling, UK import VAT). |
| Invoice Number | Links to your invoicing system for VAT/GST matching. |
| Gross vs Net | Gross includes tax and shipping if applicable. For VAT purposes, you need the net amount excluding shipping and tax. |
| Currency | Determines which country's tax rules may apply for FX transactions. |
| 1099-K reporting (US) | PayPal issues 1099-K forms for US sellers meeting thresholds. Data comes from these same transaction records. |
| DAC7 reporting (EU) | PayPal reports EU seller activity to tax authorities under DAC7. |

---

## Section 7 — Multi-Currency Handling

| Scenario | How It Appears |
|----------|---------------|
| Single-currency | All rows share the same Currency value. Straightforward. |
| Received in foreign currency, held | Payment row shows Currency = foreign currency, Gross = foreign amount. Balance Impact = Credit. |
| Received and auto-converted | Two rows: (1) Payment received in foreign currency, (2) "Currency Conversion" row showing the conversion. Both share a related Transaction ID. |
| Currency conversion | Two rows: a debit in the source currency and a credit in the target currency. The exchange rate is NOT shown as a separate column — it must be calculated from the two amounts. |
| Withdrawal in non-default currency | PayPal converts to the bank's currency. Conversion row appears before the withdrawal row. |

PayPal's multi-currency handling is messy. Conversion rows and payment rows are separate, linked by Reference Txn ID. You must match them to determine the effective exchange rate.

---

## Section 8 — Reconciliation Tips

1. **Filter by Status = "Completed" first.** Pending, Denied, and Reversed transactions should be excluded from the books. Only Completed transactions represent actual money movement.
2. **Match Transfer to Bank rows to bank deposits.** PayPal batches multiple transactions into one bank transfer. Sum all rows between "Transfer to Bank" entries to match bank deposits.
3. **Fees are in the payment row, not separate rows.** Unlike Wise, PayPal deducts fees in the same row. The Fee column is negative. Net = Gross + Fee.
4. **Temporary Holds and Releases net to zero.** A hold debits the balance, a release credits it back. They should cancel out and not appear in the P&L.
5. **Refunds reference the original transaction.** Use Reference Txn ID (column 26) to match refunds to their original payments.
6. **Currency Conversions are noise for bookkeeping.** They represent internal movement, not income or expense. Filter them out of P&L calculations.
7. **50,000-row limit.** Large accounts will receive a ZIP file with multiple CSVs. Process all files for a complete picture.
8. **Locale affects everything.** Date format, decimal separator, and even column names can change based on the user's PayPal locale setting. Always check the first row.

---

## Section 9 — Common Gotchas

1. **Fees as separate rows vs same row — inconsistent.** Most fees are in the Fee column of the payment row, but some (chargeback fees, monthly fees) are entirely separate rows. You must handle both patterns.
2. **Gross includes shipping and tax.** For revenue calculations, Gross is NOT your sales revenue if the buyer paid shipping through PayPal. Subtract Shipping and Sales Tax columns.
3. **Currency Conversion rows inflate totals.** If you sum all Credit-impact rows as revenue, currency conversions will double-count. Filter Type = "Currency Conversion" out.
4. **"General Authorization" has no money movement.** These rows show pre-auths that haven't captured. Exclude them.
5. **Email addresses as identifiers.** PayPal identifies counterparties by email, not by name. The same person may appear with different names but the same email (or vice versa).
6. **Balance column may not match your actual balance.** If you filtered the export by date range, the Balance column reflects only the filtered period, not the actual account balance.
7. **Negative Gross on refunds.** Refunds show as negative Gross with zero Fee. The original payment's fee is not returned.
8. **Time zones matter.** PayPal records times in the user's selected timezone. A transaction at 11:30 PM PST on March 31 is April 1 in UTC.
9. **Column names are locale-dependent.** A German PayPal account may export columns as "Datum", "Brutto", "Gebühr" instead of "Date", "Gross", "Fee".

---

## Section 10 — Sample Data

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

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.
