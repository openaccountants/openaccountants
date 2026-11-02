---
name: freeagent-integration
version: 1.0
category: integration
description: >
  Integration skill for FreeAgent accounting software CSV exports and imports. Activate when the user uploads a
  FreeAgent CSV, FreeAgent bank statement, or mentions FreeAgent. Popular UK accounting software for freelancers
  and micro-businesses.
jurisdiction: GLOBAL
tier: 2
last_updated: 2026-06-12
---

# FreeAgent Integration Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Section 1 — Platform Overview

FreeAgent is a UK-based cloud accounting software designed for freelancers, sole traders, micro-businesses, and their accountants. Acquired by NatWest Group in 2018, it is offered free to NatWest, Royal Bank of Scotland, and Ulster Bank business account holders. FreeAgent is MTD (Making Tax Digital) compatible and handles self-assessment, corporation tax estimates, VAT returns, and payroll.

FreeAgent is primarily used in the UK and Ireland, with limited use in the US. It is simpler than Xero/QuickBooks but covers the full accounting cycle for small entities.

---

## Section 2 — Export Formats

| Format | Use Case |
|--------|----------|
| CSV | Bank statement import (3-column, no header row), Trial Balance export (Summary, Transactions, Chart of Accounts), Profit & Loss export |
| OFX | Bank statement import (preferred format — preserves transaction IDs for duplicate detection) |
| QIF | Bank statement import (Quicken format) |
| PDF | Trial Balance, Profit & Loss, Balance Sheet, invoices, estimates |
| Excel (XLSX) | Trial Balance exports |

The bank statement CSV is the most common import format. FreeAgent's CSV format is unusual — it does NOT include a header row.

---

## Section 3 — Column Mapping

### Bank Statement CSV Import (the format FreeAgent accepts)

FreeAgent's CSV import uses a strict 3-column format with **no header row**:

| Position | Column | Format | Notes |
|----------|--------|--------|-------|
| A | Date | DD/MM/YYYY | UK date format only. No other format accepted. |
| B | Amount | Number (2 decimal places) | Positive = money in, negative (with minus sign) = money out. No currency symbols. No thousand separators. Period decimal. |
| C | Description | Plain text | Invoice reference or brief narrative. No commas within the text. No quotation marks. Single line only. |

**Critical rules:**
- NO header row. FreeAgent rejects files with headers.
- Comma delimiter only. Semicolons (common in European locales) are rejected.
- No blank rows.
- File extension must be .csv (not .xls or .xlsx).
- Despite documentation, FreeAgent does accept commas within double-quoted strings in the Description field. However, the > character renders incorrectly (known FreeAgent bug).

### FreeAgent API Bank Transaction Fields

When accessing data via the FreeAgent API, transactions have these fields:

| Field | Meaning |
|-------|---------|
| dated_on | Transaction date (YYYY-MM-DD format in the API). |
| amount | Transaction amount in the company's native currency. |
| description | Transaction narrative. |
| fitid | Unique transaction ID (from OFX imports; null for CSV imports). |
| transaction_type | Defaults to "OTHER" for CSV imports. |
| unexplained_amount | Portion of the transaction not yet allocated to an explanation. |
| bank_account | URL reference to the bank account. |

### Trial Balance Export CSV

| Column | Meaning |
|--------|---------|
| Account Code | FreeAgent's nominal code (e.g., 001, 002, 100, 200). |
| Account Name | Account description (e.g., "Sales", "Cost of Sales", "Bank Account"). |
| Debit | Debit balance (positive number or blank). |
| Credit | Credit balance (positive number or blank). |

The Trial Balance export is available in three variants:
- **Summary CSV** — account balances only.
- **Transactions CSV** — full transaction breakdown per account.
- **Chart of Accounts CSV** — account codes and names only (no balances).

---

## Section 4 — Transaction Type Codes

FreeAgent uses "explanation categories" rather than transaction type codes. When a bank transaction is "explained" in FreeAgent, it is linked to one of these categories:

| Category URL Pattern | Meaning |
|---------------------|---------|
| /categories/001 | Sales/Revenue |
| /categories/100–199 | Cost of Sales categories |
| /categories/200–299 | Operating expenses |
| /categories/300–399 | Assets |
| /categories/400–499 | Liabilities |
| /categories/500–599 | Equity/Capital |

FreeAgent also uses special explanation types:
- **Invoice payment** — links a bank receipt to an outstanding invoice.
- **Bill payment** — links a bank payment to an outstanding bill.
- **Transfer** — money movement between bank accounts.
- **Owner's drawings** — personal withdrawals (sole traders).
- **Owner's capital** — personal contributions (sole traders).
- **Corporation tax** — company tax payments.
- **Salary** — payroll payments.

---

## Section 5 — Fee Structure

FreeAgent's own fees do not appear in exported data. Subscription pricing:

| Plan | Price | Notes |
|------|-------|-------|
| FreeAgent (standard) | £29/month (£24/month annual) | Full features. |
| FreeAgent (NatWest/RBS/Ulster) | Free | Included with NatWest Group business banking. |

Bank fees, payment processor fees, and other charges appear as regular transactions in the bank statement CSV with the bank's own descriptions.

---

## Section 6 — Tax-Relevant Fields

| Field | Location | Notes |
|-------|----------|-------|
| VAT amount | Explanation detail (not in bank CSV) | When a transaction is explained in FreeAgent, the VAT amount is calculated based on the explanation category's tax rate. |
| gross_value | API explanation field | Gross amount of the explained transaction. |
| sales_tax_value | API explanation field | VAT/sales tax portion. |
| EC status | Invoice/bill level | For EU reverse-charge VAT (pre/post-Brexit). |
| CIS deductions | Payroll/subcontractor | Construction Industry Scheme deductions (UK-specific). |
| MTD VAT | Report export | FreeAgent generates MTD-compatible VAT returns with 9-box breakdown. |

FreeAgent automatically calculates VAT based on the explanation category and the configured VAT rate. The bank statement CSV itself contains no tax information — tax is applied during the explanation step inside FreeAgent.

---

## Section 7 — Multi-Currency Handling

FreeAgent has limited multi-currency support:

- The company's base currency is set at setup and cannot be changed.
- Foreign-currency bank accounts can be added (paid plans only).
- Foreign-currency invoices are supported.
- Exchange rates are fetched automatically from the ECB feed or entered manually.
- FX gains/losses are calculated automatically when foreign-currency invoices are paid.
- Bank statement CSVs for foreign-currency accounts should contain amounts in that currency. FreeAgent converts to the base currency at the prevailing rate on import.

Multi-currency is less mature in FreeAgent than in Xero or QuickBooks. Users with significant multi-currency needs often use Xero instead.

---

## Section 8 — Reconciliation Tips

1. **No header row.** This is the most common import failure. Remove any header row before uploading.
2. **Date format is DD/MM/YYYY only.** FreeAgent does not accept MM/DD/YYYY or YYYY-MM-DD in CSV imports (though the API uses YYYY-MM-DD).
3. **OFX is preferred over CSV.** OFX files include transaction IDs (fitid) which enable duplicate detection. CSV imports have no duplicate protection — uploading the same file twice doubles all transactions.
4. **Commas break descriptions.** If a bank description contains commas (e.g., "Amazon.co.uk, Marketplace"), the CSV parser splits it into additional columns. Avoid commas in column C or wrap the description in double quotes.
5. **FreeAgent "explains" transactions.** After import, each bank transaction needs to be "explained" (categorised). This is where the accounting happens — the CSV is just the raw bank data.
6. **Bank rules automate explanations.** FreeAgent can auto-explain recurring transactions using bank rules. Set these up for common payees.
7. **Reconciliation is per-bank-account.** Each bank account in FreeAgent is reconciled independently. Match the CSV import totals to the bank statement balance.

---

## Section 9 — Common Gotchas

1. **Header row rejection.** FreeAgent silently drops the first row if it looks like a header, or rejects the file entirely. Always remove headers.
2. **Duplicate imports.** CSV uploads have no duplicate detection. If a user uploads the same file twice, every transaction is duplicated. Check transaction counts before and after import.
3. **Negative amounts need minus sign.** Parentheses for negatives (100.00) are not accepted. Use -100.00.
4. **NatWest bank feed vs manual upload.** NatWest customers get automatic bank feeds. If they also upload CSVs manually, they get duplicates. Ensure they use one method only.
5. **The > character bug.** Greater-than signs in descriptions render as literal HTML entities in FreeAgent's UI. Avoid them in CSV descriptions.
6. **Semicolon delimiter.** European-locale machines may save CSVs with semicolon delimiters. FreeAgent only accepts comma-delimited files. Check the regional settings or open in a text editor to verify.
7. **Opening balances.** FreeAgent requires an opening balance when creating a bank account. If the first CSV import doesn't start from that date, there will be a gap in the transaction history.
8. **Explanation ≠ reconciliation.** In FreeAgent, "explaining" a transaction categorises it. "Reconciliation" is the separate step of matching the FreeAgent balance to the bank balance. Both must be done.

---

## Section 10 — Sample Data

### Bank Statement CSV (FreeAgent format — no header row)

```csv
15/03/2026,2500.00,Acme Ltd INV-1042 payment
16/03/2026,-64.99,Adobe Creative Cloud monthly
16/03/2026,-1200.00,HMRC VAT Q4 2025
17/03/2026,890.50,Widget Corp consulting fee
18/03/2026,-45.00,Vodafone UK mobile March
18/03/2026,-12.50,NatWest bank charges
19/03/2026,150.00,John Smith expense claim
20/03/2026,-3200.00,Jane Doe salary March
20/03/2026,-450.00,NEST pension contribution
21/03/2026,-89.99,Amazon Business supplies
```

### Trial Balance Summary Export

```csv
Account Code,Account Name,Debit,Credit
001,Sales,,42350.00
002,Other Income,,125.00
100,Cost of Materials,8200.00,
101,Subcontractor Costs,6400.00,
200,Advertising,1200.00,
201,Bank Charges,150.00,
202,Computer Equipment,2500.00,
203,Insurance,960.00,
204,Internet & Phone,540.00,
205,Office Supplies,380.00,
206,Travel & Subsistence,1450.00,
207,Wages & Salaries,19200.00,
300,Bank Account,8395.00,
400,HMRC VAT,,1200.00
401,HMRC PAYE,,2400.00
500,Drawings,5500.00,
501,Capital Introduced,,8800.00
```

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.
