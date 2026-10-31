---
name: revolut-business-integration
version: 1.0
category: integration
description: >
  Integration skill for Revolut Business statement CSV exports. Activate when the user uploads a Revolut Business
  CSV, Revolut statement, or mentions Revolut Business transactions.
jurisdiction: GLOBAL
tier: 2
last_updated: 2026-06-12
---

# Revolut Business Integration Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Section 1 — Platform Overview

Revolut Business is a fintech banking platform offering multi-currency business accounts, corporate cards, expense management, and international payments. Headquartered in London, Revolut operates across the EEA, UK, US, Australia, and Japan. It is popular with startups, freelancers, and SMEs that need multi-currency capabilities without traditional banking overhead.

Revolut Business provides per-currency account statements and an aggregated transaction export. Unlike traditional banks, Revolut uses a neobank model with real-time transaction data and card-level spending controls.

---

## Section 2 — Export Formats

| Format | Use Case |
|--------|----------|
| CSV | Transaction statements (per account or all accounts). Downloaded from Transactions > Export. |
| Excel (XLSX) | Same data as CSV but formatted for Excel. |
| PDF | Official bank statements. Per-currency, monthly. Required for formal purposes. |
| MT940 | SWIFT standard for accounting software integration. |
| CAMT.053 | European XML banking standard. |
| QIF | Quicken import format. |

CSV exports are available per-currency account or aggregated. Column headers vary slightly by region and timezone setting.

---

## Section 3 — Column Mapping

### Transaction Statement CSV

| Column Header | Meaning |
|---------------|---------|
| Date started (UTC) | Timestamp when the transaction was initiated. Format: YYYY-MM-DD HH:MM:SS. Timezone depends on account settings — may say "(UTC)" or "(Europe/Amsterdam)" etc. |
| Date completed (UTC) | Timestamp when the transaction was completed/settled. Same timezone note as above. |
| ID | Unique Revolut transaction identifier. |
| Type | Transaction type code (see Section 4). |
| Description | Transaction narrative: counterparty name, merchant, transfer reference. |
| Reference | Payment reference or memo. |
| Payer | Name of the person/entity who initiated the payment (incoming transfers). |
| Card number | Last 4 digits of the card used (for card payments). Blank for non-card transactions. |
| Orig currency | Original currency of the transaction (before any conversion). |
| Orig amount | Original amount in the original currency. |
| Payment currency | Currency the payment was settled in. |
| Amount | Settlement amount in the payment currency. Positive = money in, negative = money out. |
| Fee | Fee charged by Revolut for this transaction. Usually 0.00 for standard transactions. |
| Balance | Running balance after this transaction in the payment currency. |
| Account | Name/identifier of the Revolut account (e.g., "Main GBP", "EUR account"). |
| Beneficiary account number | Recipient's account number (for outgoing transfers). |
| Beneficiary sort code or routing number | Recipient's sort code (UK) or routing number (US). |
| Beneficiary IBAN | Recipient's IBAN (for SEPA/international transfers). |
| Beneficiary BIC | Recipient's BIC/SWIFT code. |

Note: Some regional exports may include additional columns like "Date started (Europe/London)" or omit "Date started (UTC)" depending on the account's timezone settings.

---

## Section 4 — Transaction Type Codes

| Type | Meaning |
|------|---------|
| CARD_PAYMENT | Debit card purchase at a merchant |
| CARD_REFUND | Refund to the debit card |
| TRANSFER | Bank transfer sent or received (SWIFT, SEPA, Faster Payments, ACH) |
| EXCHANGE | Currency conversion between Revolut balances |
| TOPUP | Money added from an external bank account or card |
| ATM | Cash withdrawal from ATM |
| FEE | Revolut service fee (subscription, card replacement, etc.) |
| REWARD | Cashback or promotional credit |
| DIRECT_DEBIT | UK/SEPA direct debit payment |
| TAX | Tax withholding (applies in some jurisdictions for interest) |
| INTEREST | Interest earned on balance |
| LOAN | Loan disbursement or repayment |

---

## Section 5 — Fee Structure

| Fee Type | How It Appears |
|----------|---------------|
| FX conversion (within allowance) | Zero fee. Exchange at interbank rate during market hours. |
| FX conversion (over allowance or weekend) | 0.4%–1% markup on exchange rate. Appears as implicit spread, NOT as a separate fee. |
| International transfer (SWIFT) | Fee in the Fee column. Typically £3–5 per transfer. |
| SEPA transfer | Free on most plans. |
| UK Faster Payments | Free. |
| Card payment (domestic) | Free. |
| Card payment (cross-currency) | Exchange rate spread applies. No explicit fee in the Fee column. |
| ATM withdrawal (over limit) | Fee appears in the Fee column. £2 per withdrawal over the monthly limit. |
| Monthly subscription | Separate row with Type = FEE. Free, Grow (£25/mo), Scale (£100/mo), Enterprise (custom). |
| Card replacement | Separate row with Type = FEE. |

---

## Section 6 — Tax-Relevant Fields

| Field | Notes |
|-------|-------|
| Orig currency / Payment currency | Needed for FX gain/loss calculations and determining tax jurisdiction. |
| Fee | Deductible business expense. |
| Type = INTEREST | Taxable income. |
| Type = TAX | Tax withholding already deducted (e.g., interest withholding tax in some jurisdictions). |
| Beneficiary details | IBAN, BIC, account number — needed for cross-border payment reporting (CRS/FATCA). |
| Account | Identifies which currency balance the transaction belongs to. |

Revolut does not collect VAT/GST on behalf of merchants. Revolut's own subscription fees include VAT where applicable (shown on Revolut's invoice, not in the transaction CSV).

---

## Section 7 — Multi-Currency Handling

| Scenario | How It Appears |
|----------|---------------|
| Single-currency account | All rows share the same Payment currency. Straightforward. |
| Currency exchange | Type = EXCHANGE. Two rows: one debit in the source currency, one credit in the target currency. Orig currency/Orig amount show the source; Payment currency/Amount show the target. |
| Cross-currency card payment | Single row. Orig currency shows the merchant's currency (e.g., EUR). Payment currency shows the account currency (e.g., GBP). Orig amount and Amount differ by the exchange rate. |
| Implicit exchange rate | Not shown as a column. Calculate: Amount ÷ Orig amount = effective rate. |
| Weekend/out-of-hours FX | Revolut applies a markup (0.4–1%) on weekends. The rate is worse but appears the same way in the CSV — only the effective rate reveals the markup. |

---

## Section 8 — Reconciliation Tips

1. **Timezone in column headers.** Check whether the export says "(UTC)" or a local timezone. All dates within a file use the same timezone.
2. **"Date started" vs "Date completed".** Use "Date completed" for bookkeeping purposes — this is when the transaction settled. "Date started" may be earlier for pending transfers.
3. **EXCHANGE transactions are internal.** Currency exchanges between your own Revolut balances are not income or expense — they are inter-account transfers.
4. **Card payments may have different Orig and Payment currencies.** A EUR purchase on a GBP account will show Orig currency = EUR and Payment currency = GBP. The FX conversion happens automatically.
5. **Fee column is usually zero.** Most Revolut transactions are fee-free. When fees do appear, they are in the same row (unlike Wise where fees are separate rows).
6. **Balance column is per-currency.** The running balance only makes sense within a single payment currency. Multi-currency exports may interleave currencies, making the Balance column confusing.
7. **Match to bank.** Revolut IS the bank — there is no separate bank statement to reconcile against. Reconcile the Revolut CSV directly as your bank statement.

---

## Section 9 — Common Gotchas

1. **Column headers vary by region.** UK accounts may show "(UTC)", Dutch accounts "(Europe/Amsterdam)". The data is the same but header strings differ, which breaks parsers.
2. **EXCHANGE rows create two entries.** Like Wise, a currency conversion creates two rows. If you only export one currency account, you see only one side. Export all accounts to see both.
3. **Orig amount vs Amount confusion.** For domestic transactions, these are identical. For cross-currency, Orig amount is in the foreign currency and Amount is in your account currency. Revenue/expense should use Amount (your currency).
4. **Interbank rate vs Revolut rate.** Revolut advertises the interbank rate but adds a markup outside market hours and above monthly allowances. The CSV does not flag when a markup was applied.
5. **Card number column for card disputes.** When reconciling disputed card payments, the Card number (last 4 digits) is essential for matching.
6. **TOPUP is not income.** Money added from your own external bank account is an inter-account transfer, not revenue.
7. **Fee rows (Type = FEE) are service charges.** These are deductible business expenses but are not payment processing fees — they are subscription/service fees.
8. **Empty Payer field for outgoing.** The Payer column is only populated for incoming transfers. For outgoing, look at the Description field for the recipient name.

---

## Section 10 — Sample Data

```csv
Date started (UTC),Date completed (UTC),ID,Type,Description,Reference,Payer,Card number,Orig currency,Orig amount,Payment currency,Amount,Fee,Balance,Account,Beneficiary account number,Beneficiary sort code or routing number,Beneficiary IBAN,Beneficiary BIC
2026-03-15 09:23:45,2026-03-15 09:23:45,rev-abc123def456,TRANSFER,From Acme Ltd,INV-1042,Acme Ltd,,GBP,2500.00,GBP,2500.00,0.00,12500.00,Main GBP,,,,
2026-03-15 14:30:00,2026-03-15 14:30:12,rev-ghi789jkl012,CARD_PAYMENT,Amazon Business,,,,GBP,156.99,GBP,-156.99,0.00,12343.01,Main GBP,,,,
2026-03-16 08:00:00,2026-03-16 08:00:05,rev-mno345pqr678,EXCHANGE,Exchanged to EUR,,,,,1000.00,GBP,-1000.00,0.00,11343.01,Main GBP,,,,
2026-03-16 08:00:00,2026-03-16 08:00:05,rev-stu901vwx234,EXCHANGE,Exchanged from GBP,,,,GBP,1000.00,EUR,1152.30,0.00,1152.30,EUR account,,,,
2026-03-17 11:15:00,2026-03-17 11:15:33,rev-yza567bcd890,CARD_PAYMENT,Uber Eats,,,,EUR,23.50,EUR,-23.50,0.00,1128.80,EUR account,,,,
2026-03-18 09:00:00,2026-03-18 09:01:22,rev-efg123hij456,TRANSFER,To Jane Smith Contractor,March payment,,,GBP,3200.00,GBP,-3200.00,0.00,8143.01,Main GBP,12345678,040050,,
2026-03-19 00:00:00,2026-03-19 00:00:00,rev-klm789nop012,FEE,Revolut monthly plan,,,,GBP,25.00,GBP,-25.00,0.00,8118.01,Main GBP,,,,
2026-03-20 15:45:00,2026-03-20 15:45:00,rev-qrs345tuv678,CARD_PAYMENT,Hotel Marais Paris,,,*4521,EUR,189.00,GBP,-163.74,0.00,7954.27,Main GBP,,,,
```

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.
