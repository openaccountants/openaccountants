---
name: quickbooks-integration
description: "Reconcile supplied quickbooks exports for bookkeeping in 2026. Establish the actual schema, account, dates and currency, preserve order/invoice/payment relationships, reject malformed or unreconciled data and prepare postings for human approval. Historical fields and sample data are retained, but current API, software and fee behaviour is not certified."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/quickbooks-integration"
  jurisdiction: "GLOBAL"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# QuickBooks Online import and ledger reconciliation v2.0

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

### QuickBooks Online-specific controls

This job covers supplied QBO bank-import proposals, general ledger/report exports and account/customer/supplier/product lists. QuickBooks Desktop/IIF is a different product/format; do not apply the Online bank map to it. Keep bank data distinct from existing GL and invoice/bill records, including payments, sales receipts, credit memos, deposits bundling several payments, transfers and manual journals. Cash receipts can clear receivables instead of creating another sale; bill payments can clear payables.

The retained three-column and four-column samples are alternative representations of the same eight bank movements, not sixteen transactions. Establish actual Date/Description/signed Amount versus Credit/Debit mapping, account type, local date convention and required empty cells from the target's supplied schema. A liability-card export can reverse the visual cash sign; test a known purchase and repayment against its statement. Do not assume a positive amount is income. Preserve summary rows for reconciliation, then exclude them from proposed transaction rows with a recorded reason.

Exact menu paths, accepted headings, maximum columns, file sizes, row limits, class/location capabilities, multicurrency activation/reversal and automatic tax/FX behaviour are held below. Do not promise those software rules from tax-authority sources or strip a richer export to four fields before retaining the evidence and proving the destination mapping. Keep home/foreign amounts and actual rates, configured tax agency/code detail and missing dimensions in the workpaper. An import error can arise from ambiguous quoting, locale, mapping or data grain, not just column count.

## Worked case

Both retained CSV layouts describe the same negative USD 1,794.55 movement. With an independently evidenced illustrative USD 10,000 opening, closing is USD 8,205.45. Importing both layouts would duplicate the movements. The period and currency remain supplied case assumptions; the file alone does not establish taxable income.

```oa-check
name: QuickBooks Online import and ledger reconciliation
inputs:
  receipts: 7030
  supplies: 234.56
  rent: 2800
  internet: 89.99
  payroll: 4500
  insurance: 1200
  opening: 10000
steps:
  - movement: receipts - supplies - rent - internet - payroll - insurance
  - closing: opening + movement
  - double_import_movement: movement * 2
expected:
  movement: -1794.55
  closing: 8205.45
  double_import_movement: -3589.1
```

## Retained supplied-data fixtures

These are the original illustrations, retained byte-for-byte inside their code blocks. They are not certified current platform exports, fee schedules or complete accounts. Use the worked control above and the validation method before using any record. A failed example must remain failed, not silently repaired.

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

Not yet confirmed: the live quickbooks API/schema, exact export/import column positions and availability, UI/report paths, region/plan capabilities, pricing and fee/refund conventions, automatic tax/FX behaviour, regulatory status and third-party document acceptance. The following literal table/path inventory records what the old file claimed, only to help locate and compare supplied data. Its fees, codes, timing, default settings and field meanings are historical and must not be treated as 2026 guidance. Known accounting/tax errors are replaced by the method and country boundaries above. No vendor source was used.

### Historical schema and claim inventory, not usable guidance

#### Historical 2 - Export Formats

```text
Historical item CSV. Use Case: Bank transaction import (3- or 4-column), list imports (chart of accounts, customers, vendors, products)
Historical item Excel (XLSX). Use Case: Report exports (P&L, Balance Sheet, GL, A/R, A/P), bulk data export
Historical item QBO. Use Case: Native bank feed format (OFX-based)
Historical item PDF. Use Case: Individual invoices, statements, reports
Historical item IIF. Use Case: Legacy import format (QuickBooks Desktop compatibility)
Historical item ZIP. Use Case: Bulk data export (all reports and lists in one download)
```

#### Historical Bank Transaction CSV - 3-Column Format (recommended)

```text
Historical item A. Header: Date; Required: Yes; Meaning: Transaction date. MM/DD/YYYY format (US). Leading zeros required.
Historical item B. Header: Description; Required: Yes; Meaning: Transaction narrative / memo. Plain text.
Historical item C. Header: Amount; Required: Yes; Meaning: Signed number. Positive = deposit/income. Negative = expense/withdrawal. Period decimal, no currency symbols.
```

#### Historical Bank Transaction CSV - 4-Column Format

```text
Historical item A. Header: Date; Required: Yes; Meaning: Transaction date. MM/DD/YYYY format.
Historical item B. Header: Description; Required: Yes; Meaning: Transaction narrative.
Historical item C. Header: Credit; Required: Conditional; Meaning: Money in. Positive number only. Leave blank if debit.
Historical item D. Header: Debit; Required: Conditional; Meaning: Money out. Positive number only. Leave blank if credit.
```

#### Historical Exported Report Columns (General Ledger export)

```text
Historical item Date. Meaning: Transaction date
Historical item Transaction Type. Meaning: Invoice, Payment, Expense, Journal Entry, Transfer, etc.
Historical item Num. Meaning: Document number (invoice #, check #)
Historical item Name. Meaning: Customer/vendor name
Historical item Memo/Description. Meaning: Transaction description
Historical item Account. Meaning: Chart of accounts name
Historical item Split. Meaning: Offsetting account
Historical item Debit. Meaning: Debit amount
Historical item Credit. Meaning: Credit amount
Historical item Balance. Meaning: Running balance
```

#### Historical 4 - Transaction Type Codes

```text
Historical item Invoice. Meaning: Sales invoice issued to customer
Historical item Payment. Meaning: Customer payment received against an invoice
Historical item Sales Receipt. Meaning: Sale with immediate payment (no invoice)
Historical item Credit Memo. Meaning: Credit issued to customer
Historical item Expense. Meaning: Direct expense/purchase recorded
Historical item Check. Meaning: Payment by check
Historical item Bill. Meaning: Purchase bill from vendor
Historical item Bill Payment. Meaning: Payment made against a vendor bill
Historical item Transfer. Meaning: Bank-to-bank transfer
Historical item Journal Entry. Meaning: Manual journal adjustment
Historical item Deposit. Meaning: Bank deposit (may bundle multiple payments)
Historical item Refund. Meaning: Refund issued to customer
```

#### Historical navigation and API descriptions

```text
QBO Settings > Export Data produces a ZIP file containing Excel workbooks for: Reports (P&L, Balance Sheet, A/R Ageing, A/P Ageing, etc.) and Lists (Chart of Accounts, Customers, Vendors, Products, Employees).
```

#### Historical tax-field names, definitions require actual supplied mapping

- Tax (historical location Report exports); retain as an investigation field, not proof of tax treatment.
- Tax Rate (historical location Invoice detail exports); retain as an investigation field, not proof of tax treatment.
- Tax Agency (historical location Sales Tax Liability report); retain as an investigation field, not proof of tax treatment.
- Tax Code (historical location International QBO (UK, AU)); retain as an investigation field, not proof of tax treatment.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `quickbooks-integration` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/quickbooks-integration. If neither is available, confirm every figure against the official source pages cited above before relying on it.
