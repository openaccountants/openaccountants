---
name: xero-integration
version: 1.1
category: integration
description: >
  Integration skill for Xero accounting software exports. Activate when the user uploads a Xero bank statement CSV,
  Xero invoice export, or mentions Xero, bank statement import, or Xero CSV.
jurisdiction: GLOBAL
tier: 2
last_updated: 2026-10-21
---

# Xero Integration Skill v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Section 1 — Platform Overview

Xero is a cloud-based accounting platform used primarily by small and medium businesses and their accountants. Headquartered in New Zealand, Xero is dominant in AU, NZ, and the UK, with growing adoption in the US, Canada, Singapore, Hong Kong, and South Africa. Xero provides invoicing, bank reconciliation, payroll (in some regions), expense claims, and financial reporting.

Users interact with Xero data in two main export contexts: **bank statement CSVs** (for importing transactions into Xero or exported from Xero) and **invoice/bill CSVs** (for bulk import/export of sales invoices and purchase bills).

---

## Section 2 — Export Formats

| Format | Use Case |
|--------|----------|
| CSV | Bank statement import/export, invoice import/export, contact lists, chart of accounts |
| PDF | Individual invoices, statements, financial reports |
| Excel (XLSX) | Reports (P&L, Balance Sheet, Aged Receivables, Trial Balance) |
| Google Sheets | Reports (direct export option) |

Bank statement CSVs are the most common data a user will upload for bookkeeping purposes. Invoice CSVs are used for bulk operations.

---

## Section 3 — Column Mapping

### Bank Statement CSV

Xero reads bank statement CSVs **positionally**, not by header name. Column order is critical.

| Position | Column | Required | Meaning |
|----------|--------|----------|---------|
| A | Date | Yes | Transaction date. DD/MM/YYYY for UK/AU/NZ orgs, MM/DD/YYYY for US orgs. YYYY-MM-DD works universally. |
| B | Amount | Yes | Signed number. Positive = money in, negative = money out. No currency symbols, no thousand separators. |
| C | Payee | No | Counterparty name. Used for contact matching and bank rule triggers. |
| D | Description | No | Memo/narrative. Max 500 characters. Appears in transaction notes. |
| E | Reference | No | Check number, transaction ID, or external reference. |
| F | Cheque Number | No | For check transactions only. |

### Precoded Bank Statement CSV (extended format)

Adds three columns to the standard format for auto-classification:

| Position | Column | Required | Meaning |
|----------|--------|----------|---------|
| G | AccountCode | Precoded only | Must match a nominal code in the Xero chart of accounts exactly. |
| H | TaxType | Precoded only | Must match a Xero tax rate name exactly (e.g., "20% (VAT on Income)"). |
| I | ContactName | Precoded only | Must match an existing Xero contact name exactly. |

### Invoice/Bill Import CSV

| Column Header | Required | Meaning |
|---------------|----------|---------|
| ContactName | Yes | Must match an existing Xero contact or Xero creates a new one. |
| InvoiceNumber | Yes | Unique invoice identifier. Duplicates are rejected. |
| InvoiceDate | Yes | Date format must match org region settings. |
| DueDate | Yes | Must be on or after InvoiceDate. |
| Description | Yes | Line item description. |
| Quantity | Yes | Line item quantity. |
| UnitAmount | Yes | Line item price excluding tax. |
| AccountCode | Yes | Must match a Xero chart of accounts code. |
| TaxType | Recommended | Must match Xero tax rate name exactly. |
| Reference | No | PO number or external reference. |
| Currency | No | Three-letter ISO code (GBP, AUD, USD). |
| Total | Auto | Calculated by Xero from line items. |
| TaxTotal | Auto | Calculated from TaxType and amounts. |

Multi-line invoices: each line item is a separate CSV row. Rows with the same InvoiceNumber are grouped into one invoice.

---

## Section 4 — Transaction Type Codes

Xero does not use explicit transaction type codes in CSV imports. Transaction direction is determined by the sign of the Amount field:

| Sign | Meaning |
|------|---------|
| Positive (+) | Money received / deposit / credit to bank |
| Negative (-) | Money paid out / withdrawal / debit from bank |

During reconciliation inside Xero, transactions are categorized as: Spend Money, Receive Money, Transfer, or matched to existing invoices/bills.

---

## Section 5 — Fee Structure

Xero itself does not charge transaction fees that appear in exported data. Xero's subscription fees are billed separately and do not appear in bank statement exports.

Bank fees, payment processor fees, and other charges appear as regular negative-amount transactions in bank statement CSVs with the bank's own description.

---

## Section 6 — Tax-Relevant Fields

| Field | Location | Notes |
|-------|----------|-------|
| TaxType | Invoice CSV, Precoded bank CSV | Must exactly match a configured Xero tax rate (e.g., "20% (VAT on Income)", "Tax on Purchases", "GST on Income", "BAS Excluded"). |
| TaxAmount | Invoice CSV | Per-line-item tax amount. Auto-calculated if TaxType is set. |
| TaxTotal | Invoice CSV | Invoice-level total tax. |
| AccountCode | Invoice CSV, Precoded bank CSV | Determines which P&L/BS account and indirectly which tax treatment applies. |

Xero tax rate names are region-specific. UK orgs use VAT rates, AU/NZ orgs use GST rates, US orgs use sales tax rates. The TaxType string must be copied verbatim from Settings > Tax Rates in the user's Xero org.

---

## Section 7 — Multi-Currency Handling

Xero supports multi-currency on paid plans. In CSV exports:

- Bank statement CSVs are always in the currency of the bank account they belong to. No currency column exists in the standard format.
- Invoice CSVs include an optional `Currency` column (three-letter ISO code). If omitted, the org's base currency is assumed.
- Exchange rates are managed inside Xero, not in the CSV. Xero applies the rate from its feed or a manually entered rate at reconciliation time.
- Unrealised and realised currency gains/losses are calculated by Xero automatically and posted to a Currency Gains/Losses account.

When processing a user's Xero CSV that contains foreign-currency transactions, note that the amounts are already in the bank account's currency — no conversion is needed at the CSV level.

---

## Section 8 — Reconciliation Tips

1. **Date format is the #1 import failure.** Confirm the user's Xero region before processing. UK/AU/NZ = DD/MM/YYYY. US = MM/DD/YYYY. When in doubt, use YYYY-MM-DD (works everywhere).
2. **Column order matters more than column names.** Xero reads positionally. If a bank CSV has Description in column A and Date in column B, the import will silently misread everything.
3. **No opening/closing balance rows.** Remove any summary rows, running balance columns, or opening/closing balance lines before import. Xero calculates balances internally.
4. **Max 1,000 transactions per file.** Split larger datasets into multiple files by date range.
5. **Duplicate detection is weak.** Xero checks for duplicate imports within the same bank account using date + amount + payee, but edge cases slip through. Cross-check after import.
6. **Bank rules accelerate reconciliation.** If the user has set up bank rules in Xero, many transactions will auto-match. Precoded CSVs bypass rules entirely by specifying the account directly.

---

## Section 9 — Common Gotchas

1. **Wrong sign convention.** Some bank CSVs use positive for debits and negative for credits (the opposite of what Xero expects). Always verify: positive = money IN.
2. **Comma in amounts.** Xero expects a period as the decimal separator and no thousand separators. "1,234.56" breaks the import; use "1234.56".
3. **Currency symbols in Amount.** "$100.00" fails. Use "100.00".
4. **AccountCode typos in precoded CSVs fail silently.** Xero skips the precoding for that row without warning. The transaction imports but without the account assignment.
5. **TaxType must be an exact string match.** "VAT on Income" is not the same as "20% (VAT on Income)". Copy from Xero's tax rate settings exactly.
6. **Line breaks in Description.** Carriage returns inside a description field break the CSV parser. Ensure descriptions are single-line.
7. **UTF-8 encoding required.** Non-UTF-8 files cause character corruption, especially with accented names or currency symbols in descriptions.

---

## Section 10 — Sample Data

### Bank Statement CSV (standard)

```csv
Date,Amount,Payee,Description,Reference
15/03/2026,2500.00,Acme Ltd,Invoice 1042 payment,INV-1042
16/03/2026,-64.99,Adobe Inc,Creative Cloud monthly subscription,SUB-2251
16/03/2026,-1200.00,HMRC,VAT Q4 2025 payment,VAT-Q4
17/03/2026,890.50,Widget Corp,Project consulting fee March,PO-8891
18/03/2026,-45.00,Vodafone UK,Mobile phone March,DD-MOB
18/03/2026,-12.50,Barclays,Monthly account fee,BANKFEE
19/03/2026,150.00,John Smith,Expense reimbursement,EXP-034
20/03/2026,-3200.00,Jane Doe,Salary March 2026,PAY-MAR
```

### Invoice Import CSV

```csv
ContactName,InvoiceNumber,InvoiceDate,DueDate,Description,Quantity,UnitAmount,AccountCode,TaxType,Currency
Acme Ltd,INV-1042,01/03/2026,31/03/2026,Web development services,40,62.50,200,20% (VAT on Income),GBP
Widget Corp,INV-1043,05/03/2026,04/04/2026,SEO audit report,1,890.50,200,20% (VAT on Income),GBP
Widget Corp,INV-1043,05/03/2026,04/04/2026,Keyword research addon,1,200.00,200,20% (VAT on Income),GBP
```

---

## Section 11 - Worked month-end review from exports

This is an offline preparation workflow, not an instruction to post journals, change supplier
details, lock a period or approve a close. Use only authorised exports and fabricated data for
testing. Xero reports reflect the selected organisation, settings and current ledger. A balanced
trial balance alone does not establish completeness, correct coding or a reconciled subledger.

### Input manifest

Before comparing amounts, record the organisation, base currency, financial year end, report name,
period or as-at date, cash/accrual basis, tracking/status filters, export time and file reference.
Keep account codes as text, including leading zeros. Separate missing values from explicit zero.
Do not silently sum formatted headers, subtotal rows or spreadsheet formula caches as transactions.

| Required evidence | Purpose |
| --- | --- |
| Current and prior month-end trial balances, plus chart of accounts | Account identity, debit/credit convention, closing balances and movements |
| Period general ledger and month/YTD profit and loss | Explain movements, journals, cut-off and P&L year resets |
| Bank reconciliation and independent statements for every account | Reconcile statement, ledger and outstanding items at the same date |
| Aged receivables and payables on a matching basis/date | Reconcile subledgers to the corresponding control accounts |
| Relevant payroll, GST/VAT, fixed-asset, loan and accrual schedules | Support the balances actually present; record applicability and gaps |

If dates, entity, currency or filters differ, obtain comparable exports before calculating an
unexplained difference. Re-export affected reports after an approved adjustment and retain the
earlier versions and adjustment reference. The human reviewer controls postings and period locks.

### Fabricated Australian example: July 2026, AUD, accrual basis, 30 June year end

These are selected report lines, not a complete trial balance. Assume the manifest confirms the
same organisation, basis, dates and unfiltered creditors population.

| Check | Evidence supplied | Expected finding |
| --- | --- | --- |
| Trade creditors | 31 July TB: credit $12,000; aged payables: amount owed $11,750 | Open difference $250; obtain GL, credit-note, timing and filter explanations before proposing any adjustment |
| Bank balance | TB and bank reconciliation both debit $8,000; independent bank statement absent | Ledger-to-report match only; statement check not performed, so bank reconciliation remains unverified |
| Revenue movement | June P&L YTD $108,000; July P&L YTD $9,000; July GL revenue $9,000 | July starts a new financial year; July revenue is $9,000, not $9,000 minus $108,000 |
| Supplier payment control | Invoice and supplier master show the same recently changed bank details; independent verification absent | Open verification exception; matching records do not establish that the change was authorised |

Use one documented sign convention in comparisons. In this example, show credit balances as
positive amounts owed for the payables reconciliation; under debit-positive/credit-negative TB
normalisation, the same $12,000 control balance is -$12,000. Compare like with like. For balance
sheet accounts, current minus prior closing balance is a movement to explain. For P&L YTD columns,
subtract only within the same financial year and comparable scope; obtain period GL/P&L evidence
when the financial year resets.

### Reviewer output

Produce the manifest, account movement table, reconciliation register and an exception list with
evidence references, amount, owner, next action and open/resolved status. Label every applicable
check performed, not performed or not applicable with a reason. This example remains incomplete:
the $250 creditors difference and unavailable bank statement require follow-up. Do not mark the
close approved, infer a correction journal from the difference alone or treat an empty automated
exception list as evidence that an unavailable check passed.

Source: [Xero, Do a year end in Xero](https://central.xero.com/0/article/Do-a-year-end-in-Xero-GL)
describes financial-year reporting, review of balances, adjustments and lock dates. The manifest,
register and fabricated cases above are preparation controls, not a claim about a particular CSV
layout or an automated Xero approval feature. Source checked 21 October 2026.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.
