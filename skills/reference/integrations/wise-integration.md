---
name: wise-integration
version: 1.0
category: integration
description: >
  Integration skill for Wise (formerly TransferWise) statement CSV exports. Activate when the user uploads a Wise
  statement, Wise CSV, or mentions Wise, TransferWise, or multi-currency transfers.
jurisdiction: GLOBAL
tier: 2
last_updated: 2026-06-12
---

# Wise Integration Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Section 1 — Platform Overview

Wise (formerly TransferWise) is a multi-currency money transfer and business account platform. Headquartered in London, it operates in 170+ countries and holds money in 40+ currencies. Wise is popular with freelancers receiving international payments, businesses paying overseas suppliers, and digital nomads.

Wise's key differentiator is its multi-currency account structure: each currency balance is a separate account with its own statement, IBAN/account details, and transaction history. A single Wise user may have GBP, EUR, USD, and other balances, each exported separately.

---

## Section 2 — Export Formats

| Format | Use Case |
|--------|----------|
| CSV | Per-currency balance statements, transfer lists |
| XLSX (Excel) | Per-currency balance statements |
| PDF | Official bank statements (accepted by HMRC, tax offices, lenders) |
| MT940 | Accounting software import (SWIFT standard) |
| QIF | Quicken import format |
| CAMT.053 | European bank standard XML format (v10 only) |

CSV and PDF are available on web and mobile. MT940, QIF, and CAMT.053 are web-only. Statements are always **per currency balance** — a user with GBP and EUR balances must download two separate files.

---

## Section 3 — Column Mapping

### Balance Statement CSV

| Column Header | Meaning |
|---------------|---------|
| TransferWise ID | Unique transaction identifier (numeric). Also labelled "ID" in some exports. |
| Date | Transaction date. Format varies by account region: DD-MM-YYYY (UK), MM-DD-YYYY (US), YYYY-MM-DD (some regions). |
| Amount | Transaction amount. Positive = money in, negative = money out. Decimal separator varies by region (period or comma). |
| Currency | Three-letter ISO code for the balance currency (GBP, EUR, USD). |
| Description | Transaction narrative: recipient name, transfer reference, card payment merchant, or fee description. |
| Payment Reference | Payment reference or memo attached to the transfer. |
| Running Balance | Balance after this transaction. |
| Exchange Rate | FX rate applied if this transaction involved a currency conversion. Blank/null for same-currency transactions. |
| Payer Name | Name of the person who sent the payment (for incoming transfers). |
| Payee Name | Name of the recipient (for outgoing transfers). |
| Payee Account Number | Recipient's account number (if available). |
| Merchant | Merchant name for card payments. |
| Total fees | Fee amount charged for this transaction. May be zero. |

Note: Column headers and their presence can vary slightly between Wise Personal and Wise Business accounts, and between web and app exports. Some exports combine Date and Time into a single column.

### Transfer List CSV (downloaded from Transactions page)

| Column Header | Meaning |
|---------------|---------|
| ID | Transfer ID |
| Date | Creation date of the transfer |
| Amount | Amount sent or received |
| Currency | Source or target currency |
| Recipient | Recipient name |
| Status | Completed, Cancelled, Pending |
| Direction | INCOMING or OUTGOING |
| Fee | Fee charged for the transfer |
| Exchange Rate | Rate applied |

---

## Section 4 — Transaction Type Codes

Wise does not use formal type codes in CSV exports. Transaction types are inferred from the Description field:

| Description Pattern | Meaning |
|---------------------|---------|
| "Received money from [Name]" | Incoming transfer from another Wise user or external bank |
| "Sent money to [Name]" | Outgoing transfer |
| "Card payment to [Merchant]" | Debit card purchase |
| "Card refund from [Merchant]" | Card payment refund |
| "Converted [amount] [CCY] to [amount] [CCY]" | Currency conversion between balances |
| "Direct Debit to [Name]" | Direct debit payment |
| "Added money from [Bank]" | Top-up from linked bank account |
| "Wise fee for transfer [ID]" | Fee charged as a separate line item |
| "Interest" | Interest earned on balance |
| "Cashback" | Cashback reward |

---

## Section 5 — Fee Structure

| Fee Type | How It Appears |
|----------|---------------|
| Transfer fee | Separate line item in the CSV with negative amount and description "Wise fee for transfer [ID]". Always a distinct row — never deducted from the transfer amount in the same row. |
| Currency conversion fee | Included in the exchange rate spread. Not shown as a separate line. The mid-market rate vs Wise's rate difference is the implicit fee. |
| Card payment fee | Usually zero for standard payments. Cross-currency card payments include a conversion spread. |
| Monthly account fee | Wise Business: £0 for standard, varies for premium plans. Appears as a separate transaction. |
| ATM withdrawal fee | Free up to limits, then ~£1.50 per withdrawal. Separate line item. |

Key: Wise fees are almost always **separate line items**, not deducted from the transfer amount. This is different from Stripe/PayPal where fees are deducted in the same row.

---

## Section 6 — Tax-Relevant Fields

| Field | Notes |
|-------|-------|
| Currency | Critical for determining which tax jurisdiction and FX gain/loss calculations apply. |
| Exchange Rate | Needed for FX gain/loss calculation vs the official rate on the transaction date. |
| Total fees | Deductible business expense if the account is used for business purposes. |
| Interest | Taxable income in most jurisdictions. |
| Payer/Payee details | May be needed for transfer pricing documentation and cross-border payment reporting. |

Wise does not collect or report VAT/GST on behalf of users. Wise itself is VAT-exempt as a financial service in the UK/EU. Wise does not issue invoices for fees — the CSV statement is the source document.

---

## Section 7 — Multi-Currency Handling

This is Wise's core complexity and the primary reason this skill exists.

| Scenario | How It Appears |
|----------|---------------|
| Single-currency statement | One CSV per currency balance. All amounts in that currency. |
| Currency conversion | Appears as **two entries across two statements**: a debit in the source currency statement and a credit in the destination currency statement. Both reference the same transfer ID. |
| Incoming foreign payment | May arrive in the sender's currency and auto-convert, or may credit the matching currency balance directly. |
| Exchange Rate column | Populated only for transactions involving FX conversion. Shows the rate applied. |
| Mid-market rate vs Wise rate | Wise advertises the mid-market rate but applies a slightly different rate including their margin. The Exchange Rate column shows the actual rate applied. |

### Reconciling multi-currency conversions

1. Find the debit row in the source currency statement (e.g., -1000.00 GBP).
2. Find the corresponding credit row in the destination currency statement (e.g., +1150.00 EUR).
3. The fee appears as a separate debit row in the source currency statement.
4. Match by transfer ID or by timestamp proximity.
5. Calculate effective rate: destination amount ÷ source amount = effective rate including fees.

---

## Section 8 — Reconciliation Tips

1. **One statement per currency.** You must download and process each currency balance separately. A GBP bank reconciliation uses only the GBP statement.
2. **Fees are separate rows.** Do not subtract fees from transfer amounts — they are already separate transactions.
3. **FX conversion = two legs.** A single currency conversion creates entries in two different currency statements. Always reconcile both sides.
4. **Date format varies by region.** UK accounts: DD-MM-YYYY. US accounts: MM-DD-YYYY. Some accounts: YYYY-MM-DD. Confirm before parsing.
5. **Decimal separator varies.** UK/US use period (1234.56). European accounts may use comma (1234,56). Check the CSV delimiter too — European locale may use semicolons.
6. **Running Balance column provides checksum.** Verify that the running balance progression matches Amount additions/subtractions from the opening balance.
7. **PDF is the official statement.** For HMRC, tax filings, and mortgage applications, the PDF is the accepted format. CSV is for working data only.

---

## Section 9 — Common Gotchas

1. **Two-leg FX conversions confuse bookkeepers.** A conversion from GBP to EUR creates a debit in GBP and a credit in EUR. If you only look at the GBP statement, it looks like money disappeared. Always check both currency statements.
2. **Fees as separate lines double-count risk.** If you sum all negative transactions as "expenses," you'll count transfer fees as expenses AND the transfer itself. Separate transfers from fees using the Description field.
3. **"Added money" is not income.** Top-ups from a linked bank account are inter-account transfers, not revenue. Exclude from P&L.
4. **Interest is taxable.** Small amounts of interest earned on Wise balances are taxable income. Easy to miss.
5. **Wise is not a bank in all jurisdictions.** Wise holds funds under e-money licenses in some countries and banking licenses in others. This affects deposit protection and regulatory reporting.
6. **Multiple IBANs per account.** A Wise Business account may have different IBANs for GBP (sort code + account number), EUR (Belgian IBAN), and USD (routing + account number). Bank statement matching must account for these different identifiers.

---

## Section 10 — Sample Data

### GBP Balance Statement CSV

```csv
TransferWise ID,Date,Amount,Currency,Description,Payment Reference,Running Balance,Exchange Rate,Total fees
TRANSFER-987654321,15-03-2026,2500.00,GBP,Received money from Acme Ltd,INV-1042,8750.00,,0.00
TRANSFER-987654322,16-03-2026,-1000.00,GBP,Converted 1000.00 GBP to 1153.20 EUR,,7750.00,1.15320,0.00
TRANSFER-987654322,16-03-2026,-4.56,GBP,Wise fee for transfer 987654322,,7745.44,,4.56
TRANSFER-987654323,17-03-2026,-350.00,GBP,Sent money to Jane Smith,Contractor March,7395.44,,2.10
TRANSFER-987654323,17-03-2026,-2.10,GBP,Wise fee for transfer 987654323,,7393.34,,2.10
CARD-123456789,18-03-2026,-45.99,GBP,Card payment to Amazon.co.uk,,7347.35,,0.00
CARD-123456790,18-03-2026,45.99,GBP,Card refund from Amazon.co.uk,,7393.34,,0.00
TRANSFER-987654324,19-03-2026,890.50,GBP,Received money from Widget Corp,PO-8891,8283.84,,0.00
INTEREST-001,20-03-2026,1.23,GBP,Interest,,8285.07,,0.00
```

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.
