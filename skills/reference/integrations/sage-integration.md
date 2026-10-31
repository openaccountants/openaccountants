---
name: sage-integration
version: 1.0
category: integration
description: >
  Integration skill for Sage 50 and Sage Business Cloud (Sage Accounting) CSV exports. Activate when the user
  uploads a Sage CSV, Sage transaction export, or mentions Sage 50, Sage Accounting, or Sage Business Cloud.
jurisdiction: GLOBAL
tier: 2
last_updated: 2026-06-12
---

# Sage Integration Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Section 1 — Platform Overview

Sage is a UK-headquartered accounting software company offering products ranging from small business accounting to enterprise ERP. The two most common products that produce CSV exports are:

- **Sage 50 (Desktop)** — installed accounting software popular in the UK, US, and Canada. Known as Sage 50cloud Accounts (UK/Ireland) and Sage 50 Accounting (US/Canada). The workhorse of UK accounting practices.
- **Sage Business Cloud Accounting (Sage Accounting)** — cloud-based alternative for small businesses. Simpler than Sage 50 with a modern web interface.

Sage 50 and Sage Business Cloud have different export formats. This skill covers both.

---

## Section 2 — Export Formats

### Sage 50 (Desktop)

| Format | Use Case |
|--------|----------|
| CSV | Transaction audit trail (Transaction CSV, Transaction CSV Extended), chart of accounts (CHART.CSV), customer records, supplier records, product records. All via Reports > Export. |
| PDF | Reports (P&L, Balance Sheet, Trial Balance, VAT return). |
| Excel | Report exports (some reports can export directly to Excel). |
| CSV Import | Bank statement import via File > Import or Bank Feeds module. |

### Sage Business Cloud Accounting

| Format | Use Case |
|--------|----------|
| CSV | Bank statement import (3 or 4 columns). Bank transaction export. |
| Excel (XLSX) | Report exports (P&L, Balance Sheet, Trial Balance, Aged Debtors/Creditors). |
| PDF | Reports, invoices, statements. |
| OFX / QIF | Bank statement import. |

---

## Section 3 — Column Mapping

### Sage 50 — Transaction CSV (Audit Trail Export)

The Transaction CSV is exported from Transactions > Reports > Transaction CSV. Column headings are included only if "Include Headings" is checked in Export Options.

| Column Header | Meaning |
|---------------|---------|
| Type | Transaction type code (see Section 4). |
| Account Ref | Nominal ledger code (e.g., 4000 for Sales, 7500 for Office Costs). |
| Nominal Ref | Same as Account Ref for some export variants. |
| Department | Department code (if departmental analysis is enabled). |
| Date | Transaction date. DD/MM/YYYY format. |
| Reference | Document reference (invoice number, check number, etc.). |
| Details | Transaction description/narrative. |
| Net Amount | Amount excluding VAT. |
| Tax Code | VAT code (T0 = Zero Rated, T1 = Standard Rate, T2 = Exempt, T4 = EU Sales, T5 = Lower Rate, T9 = Not Applicable). |
| Tax Amount | VAT amount. |
| Gross Amount | Amount including VAT (Net + Tax). |
| Exchange Rate | FX rate (for foreign-currency transactions). 1.000000 for base currency. |
| Base Net Amount | Net amount in base currency. |
| Base Tax Amount | Tax amount in base currency. |
| Base Gross Amount | Gross amount in base currency. |

### Sage 50 — Transaction CSV (Extended)

Adds additional columns to the standard Transaction CSV:

| Additional Column | Meaning |
|-------------------|---------|
| Bank Ref | Bank account reference (for bank transactions). |
| Extra Reference | Additional reference field. |
| User Name | User who posted the transaction. |
| Posted Date | Date the transaction was posted (may differ from transaction date). |
| Fund | Charitable fund code (added in v28.1+). |

### Sage Business Cloud — Bank Statement Import CSV

Simple format matching other cloud accounting software:

| Column | Header | Format | Example |
|--------|--------|--------|---------|
| 1 | Date | DD/MM/YYYY | 15/03/2026 |
| 2 | Description | Text | Direct Deposit - Payroll |
| 3 | Amount | Number (negative = money out) | -150.00 |

Sage Business Cloud also accepts a 4-column format:

| Column | Header | Format | Example |
|--------|--------|--------|---------|
| 1 | Date | DD/MM/YYYY | 15/03/2026 |
| 2 | Description | Text | Direct Deposit - Payroll |
| 3 | Money In | Number (positive) | 150.00 |
| 4 | Money Out | Number (positive) | |

### Sage 50 — Chart of Accounts CSV (CHART.CSV)

| Column | Meaning |
|--------|---------|
| Account Ref | Nominal code (e.g., 0010, 1100, 4000, 5000, 7000). |
| Account Name | Account description. |
| Account Type | Category identifier. |
| Begin Yr Debit-Total | Opening balance (debit). |
| Begin Yr Credit-Total | Opening balance (credit). |
| Debit-Period End xx/xx/xx | Period-end debit balance (up to 13 periods). |
| Credit-Period End xx/xx/xx | Period-end credit balance. |

---

## Section 4 — Transaction Type Codes

### Sage 50 Type Codes

| Code | Meaning |
|------|---------|
| SI | Sales Invoice |
| SC | Sales Credit Note |
| SR | Sales Receipt (payment received) |
| SA | Sales Receipt on Account (also SR → SA in some exports) |
| PI | Purchase Invoice |
| PC | Purchase Credit Note |
| PP | Purchase Payment (also PP → PA in some exports) |
| PA | Purchase Payment on Account |
| BP | Bank Payment |
| BR | Bank Receipt |
| JD | Journal Debit |
| JC | Journal Credit |
| VP | Visa/Card Payment |
| VR | Visa/Card Receipt |
| CP | Cash Payment |
| CR | Cash Receipt |

### Sage Business Cloud

Sage Business Cloud does not use type codes in CSV imports. Transaction categorisation happens inside the application during the bank reconciliation step.

---

## Section 5 — Fee Structure

Sage does not charge transaction fees that appear in exported data. Software licensing:

| Product | Price (typical) |
|---------|-----------------|
| Sage 50 (UK, per-seat) | £20–75/month per user depending on tier. |
| Sage 50 (US) | $48–72/month depending on tier. |
| Sage Business Cloud (Start) | £12/month. |
| Sage Business Cloud (Standard) | £26/month. |

Bank fees, payment processing fees, and other charges appear as regular transactions in the exported data with the bank's description.

---

## Section 6 — Tax-Relevant Fields

| Field | Location | Notes |
|-------|----------|-------|
| Tax Code | Sage 50 Transaction CSV | T0 through T9 codes. T1 = Standard Rate (20% UK), T5 = Reduced Rate (5% UK), T0 = Zero Rated, T2 = Exempt, T4 = EU Sales, T7 = Zero Rated Purchases, T9 = Non-VAT. |
| Tax Amount | Sage 50 Transaction CSV | Actual VAT amount calculated. |
| Net Amount | Sage 50 Transaction CSV | Pre-VAT amount. Used for Box 6 (sales) and Box 7 (purchases) on the UK VAT return. |
| Gross Amount | Sage 50 Transaction CSV | VAT-inclusive amount. |
| EC flag | Sage 50 (via T4, T7 codes) | European Community sales/purchases for EC Sales List reporting. |

Sage 50 is deeply integrated with UK VAT reporting. The Tax Code field directly maps to VAT return boxes. Sage Business Cloud similarly handles VAT but through its web interface rather than CSV codes.

---

## Section 7 — Multi-Currency Handling

### Sage 50

| Feature | Notes |
|---------|-------|
| Foreign-currency accounts | Supported in Sage 50 Plus and above. |
| Exchange Rate column | Included in Transaction CSV. Shows the rate used for the transaction. |
| Base currency columns | Base Net, Base Tax, Base Gross show amounts converted to the company's base currency (usually GBP). |
| Revaluation | Exchange rate differences are posted via Revaluation function in Sage. |

### Sage Business Cloud

| Feature | Notes |
|---------|-------|
| Multi-currency | Supported. Foreign-currency bank accounts and invoices. |
| Exchange rates | Fetched automatically. |
| CSV import | Bank statement CSVs are in the bank account's currency. Sage converts at the prevailing rate. |

---

## Section 8 — Reconciliation Tips

1. **Sage 50: Check "Include Headings" when exporting.** Without it, the CSV has no column headers, making it difficult to parse. The first row would be data, not headers.
2. **Type codes are essential for Sage 50.** Every transaction has a type code (SI, PI, BP, BR, etc.) that determines how it posts. Misinterpreting type codes will corrupt the double-entry.
3. **Sage 50 nominal codes follow a standard pattern.** 0xxx = Fixed Assets, 1xxx = Current Assets, 2xxx = Current Liabilities, 3xxx = Capital/Equity, 4xxx = Sales, 5xxx = Purchases/Cost of Sales, 6xxx = Direct Expenses, 7xxx = Overheads, 8xxx = Bad Debts/Depreciation.
4. **Bank reconciliation in Sage 50 uses Bank Ref.** The Bank Ref column identifies which bank account the transaction belongs to (typically 1200 for Current Account).
5. **Sage Business Cloud: 3 or 4 column CSV.** Same rules as Xero/QuickBooks — either Date/Description/Amount or Date/Description/Money In/Money Out.
6. **DD/MM/YYYY date format.** Both Sage 50 and Sage Business Cloud use UK date format by default. US Sage 50 uses MM/DD/YYYY.
7. **Sage 50 exports commas in descriptions carefully.** If "Details" contains commas, Sage wraps the field in double quotes. However, some users open the CSV in Excel and re-save it, which can corrupt the quoting.

---

## Section 9 — Common Gotchas

1. **No headings by default (Sage 50).** The "Include Headings" checkbox is off by default. Many users export without it, producing headerless CSVs. If the first row looks like data (starts with a type code like "SI" or "BP"), there are no headers.
2. **SI/SC confusion.** SI = Sales Invoice (money coming in, eventually). SC = Sales Credit Note (reversal). Getting these backwards flips revenue positive/negative.
3. **PP vs PA.** PP (Purchase Payment) and PA (Purchase Payment on Account) are different. PP allocates to a specific invoice, PA is a payment on account without allocation. Some export variants transform PP to PA.
4. **Net vs Gross.** Sage 50 tracks Net, Tax, and Gross separately. Always use Net for P&L figures and Gross for bank reconciliation (since the bank sees the VAT-inclusive amount).
5. **Tax Code T9 is not zero-rated.** T9 = "Non-VATable / Outside Scope". T0 = "Zero-Rated" (still reportable on VAT return). These are frequently confused.
6. **Period-end columns in Chart of Accounts.** The CHART.CSV contains balance columns for each period. If the export is mid-year, later periods will be zero but earlier periods will have data.
7. **Sage 50 uses a proprietary data format internally.** The CSV export is a lossy translation. Some transaction relationships (allocations, disputes, memo links) are lost in CSV export.
8. **Exchange Rate precision.** Sage 50 stores exchange rates to 6 decimal places. Rounding differences can occur when comparing to bank rates.

---

## Section 10 — Sample Data

### Sage 50 — Transaction CSV (with headings)

```csv
Type,Account Ref,Date,Reference,Details,Net Amount,Tax Code,Tax Amount,Gross Amount
SI,4000,15/03/2026,INV-1042,Web development services - Acme Ltd,2500.00,T1,500.00,3000.00
SI,4000,16/03/2026,INV-1043,SEO audit report - Widget Corp,890.50,T1,178.10,1068.60
PI,5000,17/03/2026,SUP-2201,Server hosting - AWS March,450.00,T1,90.00,540.00
BP,7500,18/03/2026,DD-032026,Adobe Creative Cloud subscription,54.16,T1,10.83,64.99
BP,7502,18/03/2026,DD-032026,Vodafone UK mobile phone,37.50,T1,7.50,45.00
BR,1200,19/03/2026,BAC,Acme Ltd payment received,3000.00,T9,0.00,3000.00
BP,7000,20/03/2026,PAY-MAR,Salary - Jane Doe March,3200.00,T9,0.00,3200.00
JD,2201,20/03/2026,VAT-Q4,VAT liability Q4 2025,1200.00,T9,0.00,1200.00
JC,1200,20/03/2026,VAT-Q4,VAT payment from bank,1200.00,T9,0.00,1200.00
```

### Sage Business Cloud — Bank Statement Import CSV

```csv
Date,Description,Amount
15/03/2026,Acme Ltd BAC payment,3000.00
16/03/2026,Adobe Creative Cloud DD,-64.99
17/03/2026,HMRC VAT Q4 2025,-1200.00
18/03/2026,Vodafone UK DD,-45.00
18/03/2026,NatWest bank charges,-12.50
19/03/2026,Widget Corp BAC payment,1068.60
20/03/2026,Jane Doe salary BACS,-3200.00
20/03/2026,NEST pension DD,-450.00
```

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.
