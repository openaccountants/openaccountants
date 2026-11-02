---
name: quickbooks-integration
version: 1.0
category: integration
description: >
  Integration skill for QuickBooks Online CSV exports and imports. Activate when the user uploads a QuickBooks
  transaction export, bank transaction CSV, or mentions QuickBooks, QBO, or Intuit.
jurisdiction: GLOBAL
tier: 2
last_updated: 2026-06-12
---

# QuickBooks Online Integration Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Section 1 — Platform Overview

QuickBooks Online (QBO) is a cloud-based accounting platform by Intuit, dominant in the US and Canada with significant adoption in the UK, Australia, and India. It serves small to mid-sized businesses with invoicing, expense tracking, bank reconciliation, payroll, and tax preparation. QuickBooks Desktop (separate product) has a different export format — this skill covers QBO only.

QBO data commonly appears as: **bank transaction CSVs** (imported into QBO from a bank), **exported report data** (P&L, Balance Sheet, General Ledger as Excel/CSV), and **list exports** (chart of accounts, customers, vendors, products).

---

## Section 2 — Export Formats

| Format | Use Case |
|--------|----------|
| CSV | Bank transaction import (3- or 4-column), list imports (chart of accounts, customers, vendors, products) |
| Excel (XLSX) | Report exports (P&L, Balance Sheet, GL, A/R, A/P), bulk data export |
| QBO | Native bank feed format (OFX-based) |
| PDF | Individual invoices, statements, reports |
| IIF | Legacy import format (QuickBooks Desktop compatibility) |
| ZIP | Bulk data export (all reports and lists in one download) |

Bank transaction CSV import is the most common user interaction requiring this skill.

---

## Section 3 — Column Mapping

### Bank Transaction CSV — 3-Column Format (recommended)

| Column | Header | Required | Meaning |
|--------|--------|----------|---------|
| A | Date | Yes | Transaction date. MM/DD/YYYY format (US). Leading zeros required. |
| B | Description | Yes | Transaction narrative / memo. Plain text. |
| C | Amount | Yes | Signed number. Positive = deposit/income. Negative = expense/withdrawal. Period decimal, no currency symbols. |

### Bank Transaction CSV — 4-Column Format

| Column | Header | Required | Meaning |
|--------|--------|----------|---------|
| A | Date | Yes | Transaction date. MM/DD/YYYY format. |
| B | Description | Yes | Transaction narrative. |
| C | Credit | Conditional | Money in. Positive number only. Leave blank if debit. |
| D | Debit | Conditional | Money out. Positive number only. Leave blank if credit. |

### Exported Report Columns (General Ledger export)

| Column | Meaning |
|--------|---------|
| Date | Transaction date |
| Transaction Type | Invoice, Payment, Expense, Journal Entry, Transfer, etc. |
| Num | Document number (invoice #, check #) |
| Name | Customer/vendor name |
| Memo/Description | Transaction description |
| Account | Chart of accounts name |
| Split | Offsetting account |
| Debit | Debit amount |
| Credit | Credit amount |
| Balance | Running balance |

### Bulk Data Export

QBO Settings > Export Data produces a ZIP file containing Excel workbooks for: Reports (P&L, Balance Sheet, A/R Ageing, A/P Ageing, etc.) and Lists (Chart of Accounts, Customers, Vendors, Products, Employees).

---

## Section 4 — Transaction Type Codes

QBO uses descriptive transaction type names in exports:

| Type | Meaning |
|------|---------|
| Invoice | Sales invoice issued to customer |
| Payment | Customer payment received against an invoice |
| Sales Receipt | Sale with immediate payment (no invoice) |
| Credit Memo | Credit issued to customer |
| Expense | Direct expense/purchase recorded |
| Check | Payment by check |
| Bill | Purchase bill from vendor |
| Bill Payment | Payment made against a vendor bill |
| Transfer | Bank-to-bank transfer |
| Journal Entry | Manual journal adjustment |
| Deposit | Bank deposit (may bundle multiple payments) |
| Refund | Refund issued to customer |

---

## Section 5 — Fee Structure

QBO does not charge per-transaction fees that appear in CSV exports. Subscription fees are billed to the user's payment method separately.

If the user processes payments through QuickBooks Payments (Intuit's payment processor), processing fees appear in the bank feed as separate transactions or as deductions from deposits. Standard rates: 2.9% + $0.25 for online card payments, 1% for ACH/bank transfers (min $1).

---

## Section 6 — Tax-Relevant Fields

| Field | Location | Notes |
|-------|----------|-------|
| Tax | Report exports | Tax amount on invoices and bills. Depends on sales tax configuration. |
| Tax Rate | Invoice detail exports | The rate applied to line items. |
| Tax Agency | Sales Tax Liability report | Which tax authority the tax is owed to. |
| Tax Code | International QBO (UK, AU) | Maps to VAT/GST codes. US QBO uses location-based sales tax instead. |

US QBO uses automated sales tax based on product taxability and customer location. UK/AU QBO uses manual VAT/GST codes similar to Xero.

---

## Section 7 — Multi-Currency Handling

QBO supports multi-currency (must be enabled; cannot be disabled once turned on).

- Bank transaction CSVs are in the currency of the bank account. No currency column in the import format.
- Invoice exports include a Currency column when multi-currency is enabled.
- Exchange rates are managed inside QBO. Home currency and foreign currency amounts both appear in report exports.
- Realised gains/losses are posted to an Exchange Gain or Loss account automatically.

---

## Section 8 — Reconciliation Tips

1. **Strict column count.** QBO rejects CSVs with more than 4 columns. Stripe (9+ columns), PayPal (41 columns), and other platform exports must be trimmed to 3 or 4 columns before import.
2. **Date format must be MM/DD/YYYY for US orgs.** DD/MM/YYYY for UK/AU orgs. No mixed formats within a file.
3. **Zero-amount cells must be blank, not "0".** In 4-column format, leave Credit or Debit blank — do not put 0.
4. **File size limit: 350 KB.** For larger datasets, split by date range.
5. **Max 1,000 lines per upload.**
6. **Deposit bundling.** QBO may group multiple customer payments into a single bank deposit. Match the bank deposit total to the sum of individual payments in QBO.
7. **Credit card sign reversal.** Credit card account CSVs show charges as positive (increases balance) and payments as negative (reduces balance) — opposite of bank accounts.

---

## Section 9 — Common Gotchas

1. **Numbers in Description column cause errors.** QBO may misinterpret description fields that contain only numbers as amounts. Add text context.
2. **Duplicate imports.** QBO has limited duplicate detection. If re-uploading, transactions may be doubled.
3. **"Columns aren't mapped correctly" error.** Usually means the file has more than 4 columns or extra header rows. Strip to exactly 3 or 4 columns.
4. **Reversed CSV for credit cards.** Bank exports for credit card accounts often have debits as positive (purchases) and credits as negative (payments). QBO expects the same convention only when uploading to a credit card account, not a bank account.
5. **Opening/closing balance rows.** Remove any summary rows from bank exports before uploading.
6. **The word "amount" in headers.** Do not use "Amount" as a header for Credit or Debit columns in 4-column format — QBO may misparse.
7. **Class and Location tracking.** These QBO features are not included in bank CSV imports. They must be assigned during the reconciliation step inside QBO.

---

## Section 10 — Sample Data

### 3-Column Format

```csv
Date,Description,Amount
01/15/2026,Client payment - Acme Corp,5000.00
01/16/2026,Office supplies - Staples,-234.56
01/16/2026,Monthly rent payment,-2800.00
01/17/2026,Freelance income - Widget project,1250.00
01/18/2026,Internet service - Comcast,-89.99
01/20/2026,Payroll - January 2026,-4500.00
01/22/2026,Sales revenue - Online store,780.00
01/25/2026,Insurance premium - Q1,-1200.00
```

### 4-Column Format

```csv
Date,Description,Credit,Debit
01/15/2026,Client payment - Acme Corp,5000.00,
01/16/2026,Office supplies - Staples,,234.56
01/16/2026,Monthly rent payment,,2800.00
01/17/2026,Freelance income - Widget project,1250.00,
01/18/2026,Internet service - Comcast,,89.99
01/20/2026,Payroll - January 2026,,4500.00
01/22/2026,Sales revenue - Online store,780.00,
01/25/2026,Insurance premium - Q1,,1200.00
```

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.
