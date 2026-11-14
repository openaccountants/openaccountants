---
name: sage-integration
version: 2.0
category: bookkeeping
description: >
  Reconcile supplied sage exports for bookkeeping in 2026. Establish the actual schema, account, dates and currency, preserve order/invoice/payment relationships, reject malformed or unreconciled data and prepare postings for human approval. Historical fields and sample data are retained, but current API, software and fee behaviour is not certified.
jurisdiction: GLOBAL
last_updated: 2026-11-14
tier: 2
domain: bookkeeping
tax_year: 2026
type: cross-country-method
checked_on: 2026-11-14
---

# Sage audit trail, bank and chart reconciliation v2.0

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

### Sage-specific controls

Identify product, release, country and configured chart: Sage 50 desktop and Sage Business Cloud are separate mappings. Preserve headings or an authenticated positional map, nominal versus customer/supplier account references, department, bank reference, posted/document dates, user/fund dimensions and all base/foreign amounts. Do not assume Account Ref and Nominal Ref mean the same account. Chart period columns, opening debit/credit and current-period balances are distinct; later empty/zero periods are not the current balance.

Read the actual SI/SC/SR/SA, PI/PC/PP/PA, BP/BR, JD/JC and card/cash mappings from supplied records. Invoice, credit note, allocated payment and payment on account have different roles. Match invoice-to-payment allocations and identify relationships absent from a flat export before reconstructing a journal. A bank receipt against an existing invoice is not additional revenue. Net/Tax/Gross fields are useful controls, but capital/personal/unrecoverable-tax items do not all become net P&L expense.

Tax codes are configuration and jurisdiction dependent. Do not certify T1 as a universal 20% code, T5 as 5%, or any code as a fixed VAT-return box. Zero-rated, exempt and outside-scope are different legal treatments; retrieve the actual tax-code definitions and owning VAT method. Likewise historical nominal ranges and bank 1200 are lookup candidates, not a universal chart. Preserve double-quoted commas and raw exchange-rate precision; apply the documented rounding policy. Do not certify an export is lossless or that every version supports a particular fund/foreign-currency feature.

## Worked case

The supplied Acme invoice has net 2,500 plus 500 stated tax and a matching 3,000 receipt. On a policy that already recognises the invoice, the receipt clears the 3,000 receivable, not another 2,500 sale. The Adobe sample also satisfies 54.16 + 10.83 = 64.99. These are given invoice amounts, not certification of a current tax rate or tax code.

```oa-check
name: Sage audit trail, bank and chart reconciliation
inputs:
  invoice_net: 2500
  invoice_tax: 500
  bank_receipt: 3000
  bill_net: 54.16
  bill_tax: 10.83
  bill_gross: 64.99
steps:
  - invoice_gross: invoice_net + invoice_tax
  - receipt_clears_invoice: bank_receipt - invoice_gross
  - bill_control: bill_gross - bill_net - bill_tax
  - wrong_duplicate_sales: invoice_net * 2
expected:
  invoice_gross: 3000
  receipt_clears_invoice: 0
  bill_control: 0
  wrong_duplicate_sales: 5000
```

## Retained supplied-data fixtures

These are the original illustrations, retained byte-for-byte inside their code blocks. They are not certified current platform exports, fee schedules or complete accounts. Use the worked control above and the validation method before using any record. A failed example must remain failed, not silently repaired.

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

Not yet confirmed: the live sage API/schema, exact export/import column positions and availability, UI/report paths, region/plan capabilities, pricing and fee/refund conventions, automatic tax/FX behaviour, regulatory status and third-party document acceptance. The following literal table/path inventory records what the old file claimed, only to help locate and compare supplied data. Its fees, codes, timing, default settings and field meanings are historical and must not be treated as 2026 guidance. Known accounting/tax errors are replaced by the method and country boundaries above. No vendor source was used.

### Historical schema and claim inventory, not usable guidance

#### Historical Sage 50 (Desktop)

```text
Historical item CSV. Use Case: Transaction audit trail (Transaction CSV, Transaction CSV Extended), chart of accounts (CHART.CSV), customer records, supplier records, product records. All via Reports > Export.
Historical item PDF. Use Case: Reports (P&L, Balance Sheet, Trial Balance, VAT return).
Historical item Excel. Use Case: Report exports (some reports can export directly to Excel).
Historical item CSV Import. Use Case: Bank statement import via File > Import or Bank Feeds module.
```

#### Historical Sage Business Cloud Accounting

```text
Historical item CSV. Use Case: Bank statement import (3 or 4 columns). Bank transaction export.
Historical item Excel (XLSX). Use Case: Report exports (P&L, Balance Sheet, Trial Balance, Aged Debtors/Creditors).
Historical item PDF. Use Case: Reports, invoices, statements.
Historical item OFX / QIF. Use Case: Bank statement import.
```

#### Historical Sage 50 - Transaction CSV (Audit Trail Export)

```text
Historical item Type. Meaning: Transaction type code (see Section 4).
Historical item Account Ref. Meaning: Nominal ledger code (e.g., 4000 for Sales, 7500 for Office Costs).
Historical item Nominal Ref. Meaning: Same as Account Ref for some export variants.
Historical item Department. Meaning: Department code (if departmental analysis is enabled).
Historical item Date. Meaning: Transaction date. DD/MM/YYYY format.
Historical item Reference. Meaning: Document reference (invoice number, check number, etc.).
Historical item Details. Meaning: Transaction description/narrative.
Historical item Net Amount. Meaning: Amount excluding VAT.
Historical item Tax Code. Meaning: VAT code (T0 = Zero Rated, T1 = Standard Rate, T2 = Exempt, T4 = EU Sales, T5 = Lower Rate, T9 = Not Applicable).
Historical item Tax Amount. Meaning: VAT amount.
Historical item Gross Amount. Meaning: Amount including VAT (Net + Tax).
Historical item Exchange Rate. Meaning: FX rate (for foreign-currency transactions). 1.000000 for base currency.
Historical item Base Net Amount. Meaning: Net amount in base currency.
Historical item Base Tax Amount. Meaning: Tax amount in base currency.
Historical item Base Gross Amount. Meaning: Gross amount in base currency.
```

#### Historical Sage 50 - Transaction CSV (Extended)

```text
Historical item Bank Ref. Meaning: Bank account reference (for bank transactions).
Historical item Extra Reference. Meaning: Additional reference field.
Historical item User Name. Meaning: User who posted the transaction.
Historical item Posted Date. Meaning: Date the transaction was posted (may differ from transaction date).
Historical item Fund. Meaning: Charitable fund code (added in v28.1+).
```

#### Historical Sage Business Cloud - Bank Statement Import CSV

```text
Historical item 1. Header: Date; Format: DD/MM/YYYY; Example: 15/03/2026
Historical item 2. Header: Description; Format: Text; Example: Direct Deposit - Payroll
Historical item 3. Header: Amount; Format: Number (negative = money out); Example: -150.00
Historical item Column. Header: Header; Format: Format; Example: Example
Historical item 1. Header: Date; Format: DD/MM/YYYY; Example: 15/03/2026
Historical item 2. Header: Description; Format: Text; Example: Direct Deposit - Payroll
Historical item 3. Header: Money In; Format: Number (positive); Example: 150.00
Historical item 4. Header: Money Out; Format: Number (positive); Example:
```

#### Historical Sage 50 - Chart of Accounts CSV (CHART.CSV)

```text
Historical item Account Ref. Meaning: Nominal code (e.g., 0010, 1100, 4000, 5000, 7000).
Historical item Account Name. Meaning: Account description.
Historical item Account Type. Meaning: Category identifier.
Historical item Begin Yr Debit-Total. Meaning: Opening balance (debit).
Historical item Begin Yr Credit-Total. Meaning: Opening balance (credit).
Historical item Debit-Period End xx/xx/xx. Meaning: Period-end debit balance (up to 13 periods).
Historical item Credit-Period End xx/xx/xx. Meaning: Period-end credit balance.
```

#### Historical Sage 50 Type Codes

```text
Historical item SI. Meaning: Sales Invoice
Historical item SC. Meaning: Sales Credit Note
Historical item SR. Meaning: Sales Receipt (payment received)
Historical item SA. Meaning: Sales Receipt on Account (also SR → SA in some exports)
Historical item PI. Meaning: Purchase Invoice
Historical item PC. Meaning: Purchase Credit Note
Historical item PP. Meaning: Purchase Payment (also PP → PA in some exports)
Historical item PA. Meaning: Purchase Payment on Account
Historical item BP. Meaning: Bank Payment
Historical item BR. Meaning: Bank Receipt
Historical item JD. Meaning: Journal Debit
Historical item JC. Meaning: Journal Credit
Historical item VP. Meaning: Visa/Card Payment
Historical item VR. Meaning: Visa/Card Receipt
Historical item CP. Meaning: Cash Payment
Historical item CR. Meaning: Cash Receipt
```

#### Historical 5 - Fee Structure

```text
Historical item Sage 50 (UK, per-seat). Price (typical): £20 to 75/month per user depending on tier.
Historical item Sage 50 (US). Price (typical): $48 to 72/month depending on tier.
Historical item Sage Business Cloud (Start). Price (typical): £12/month.
Historical item Sage Business Cloud (Standard). Price (typical): £26/month.
```

#### Historical Sage 50

```text
Historical item Foreign-currency accounts. Notes: Supported in Sage 50 Plus and above.
Historical item Exchange Rate column. Notes: Included in Transaction CSV. Shows the rate used for the transaction.
Historical item Base currency columns. Notes: Base Net, Base Tax, Base Gross show amounts converted to the company's base currency (usually GBP).
Historical item Revaluation. Notes: Exchange rate differences are posted via Revaluation function in Sage.
```

#### Historical Sage Business Cloud

```text
Historical item Multi-currency. Notes: Supported. Foreign-currency bank accounts and invoices.
Historical item Exchange rates. Notes: Fetched automatically.
Historical item CSV import. Notes: Bank statement CSVs are in the bank account's currency. Sage converts at the prevailing rate.
```

#### Historical navigation and API descriptions

```text
The Transaction CSV is exported from Transactions > Reports > Transaction CSV. Column headings are included only if "Include Headings" is checked in Export Options.
```

#### Historical tax-field names, definitions require actual supplied mapping

- Tax Code (historical location Sage 50 Transaction CSV); retain as an investigation field, not proof of tax treatment.
- Tax Amount (historical location Sage 50 Transaction CSV); retain as an investigation field, not proof of tax treatment.
- Net Amount (historical location Sage 50 Transaction CSV); retain as an investigation field, not proof of tax treatment.
- Gross Amount (historical location Sage 50 Transaction CSV); retain as an investigation field, not proof of tax treatment.
- EC flag (historical location Sage 50 (via T4, T7 codes)); retain as an investigation field, not proof of tax treatment.
