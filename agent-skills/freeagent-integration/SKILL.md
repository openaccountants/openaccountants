---
name: freeagent-integration
description: "Reconcile supplied freeagent exports for bookkeeping in 2026. Establish the actual schema, account, dates and currency, preserve order/invoice/payment relationships, reject malformed or unreconciled data and prepare postings for human approval. Historical fields and sample data are retained, but current API, software and fee behaviour is not certified."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/freeagent-integration"
  jurisdiction: "GLOBAL"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# FreeAgent bank explanations and trial-balance reconciliation v2.0

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

### FreeAgent-specific controls

Keep supplied bank-import data, API bank transactions, trial-balance summary, transactions, chart and reports separate. The retained bank sample is explicitly headerless: its first row is real data. Preserve actual locale/quoting and test a comma-bearing narrative with a CSV parser; the old simultaneous claims that descriptions cannot contain commas/quotes and that quoted commas work do not establish a current import rule. The greater-than-character UI issue, rigid date/delimiter rules and header rejection behaviour remain historical, not certified live behaviour.

Preserve `fitid` and other IDs when present; absence of an ID does not justify duplicate imports. Use account/file/row provenance and a documented matching decision for CSV, feeds and OFX overlaps. Do not assume automatic duplicate protection exists or does not exist. Record an opening balance and full covered period. Categorising/explaining and proving reconciliation are different controls.

Treat invoice payment, bill payment, own transfer, owner drawings/capital, corporation tax, payroll and pension liabilities separately. A category URL or remembered nominal range does not prove legal treatment. Preserve `unexplained_amount`, tax/CIS detail and actual account-currency metadata, but do not infer VAT from a bank narrative. The positive 150 John Smith expense-claim row needs supporting evidence; its label alone cannot establish an outgoing expense. Subscription bank eligibility, plan charges, ECB rates, currency features and automated tax filing are not verified current claims.

The trial-balance fixture contains debit/credit balances, not cash movements. Test totals before use; do not post it in addition to its GL detail. The retained trial-balance illustration balances, but that alone does not prove completeness, correct classification or reconciliation to its bank statement. Obtain the actual full reports and supporting reconciliation; do not insert a suspense amount.

## Worked case

The retained trial-balance sample totals debit 54,875 and credit 54,875. Its zero difference is an arithmetic control, not a complete-ledger conclusion. The ten headerless bank rows separately total receipts 3,540.50 and payments 5,062.48, or a negative 1,521.98 movement. The illustrative bank closing uses a supported assumed opening of 10,000; the unrelated trial-balance bank balance 8,395 is not silently substituted.

```oa-check
name: FreeAgent bank explanations and trial-balance reconciliation
inputs:
  debits: 54875
  credits: 54875
  opening: 10000
  receipts: 3540.5
  outflows: 5062.48
steps:
  - trial_balance_gap: debits - credits
  - bank_movement: receipts - outflows
  - bank_closing: opening + bank_movement
expected:
  trial_balance_gap: 0
  bank_movement: -1521.98
  bank_closing: 8478.02
```

## Retained supplied-data fixtures

These are the original illustrations, retained byte-for-byte inside their code blocks. They are not certified current platform exports, fee schedules or complete accounts. Use the worked control above and the validation method before using any record. A failed example must remain failed, not silently repaired.

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

Not yet confirmed: the live freeagent API/schema, exact export/import column positions and availability, UI/report paths, region/plan capabilities, pricing and fee/refund conventions, automatic tax/FX behaviour, regulatory status and third-party document acceptance. The following literal table/path inventory records what the old file claimed, only to help locate and compare supplied data. Its fees, codes, timing, default settings and field meanings are historical and must not be treated as 2026 guidance. Known accounting/tax errors are replaced by the method and country boundaries above. No vendor source was used.

### Historical schema and claim inventory, not usable guidance

#### Historical 2 - Export Formats

```text
Historical item CSV. Use Case: Bank statement import (3-column, no header row), Trial Balance export (Summary, Transactions, Chart of Accounts), Profit & Loss export
Historical item OFX. Use Case: Bank statement import (preferred format , preserves transaction IDs for duplicate detection)
Historical item QIF. Use Case: Bank statement import (Quicken format)
Historical item PDF. Use Case: Trial Balance, Profit & Loss, Balance Sheet, invoices, estimates
Historical item Excel (XLSX). Use Case: Trial Balance exports
```

#### Historical Bank Statement CSV Import (the format FreeAgent accepts)

```text
Historical item A. Column: Date; Format: DD/MM/YYYY; Notes: UK date format only. No other format accepted.
Historical item B. Column: Amount; Format: Number (2 decimal places); Notes: Positive = money in, negative (with minus sign) = money out. No currency symbols. No thousand separators. Period decimal.
Historical item C. Column: Description; Format: Plain text; Notes: Invoice reference or brief narrative. No commas within the text. No quotation marks. Single line only.
```

#### Historical FreeAgent API Bank Transaction Fields

```text
Historical item dated_on. Meaning: Transaction date (YYYY-MM-DD format in the API).
Historical item amount. Meaning: Transaction amount in the company's native currency.
Historical item description. Meaning: Transaction narrative.
Historical item fitid. Meaning: Unique transaction ID (from OFX imports; null for CSV imports).
Historical item transaction_type. Meaning: Defaults to "OTHER" for CSV imports.
Historical item unexplained_amount. Meaning: Portion of the transaction not yet allocated to an explanation.
Historical item bank_account. Meaning: URL reference to the bank account.
```

#### Historical Trial Balance Export CSV

```text
Historical item Account Code. Meaning: FreeAgent's nominal code (e.g., 001, 002, 100, 200).
Historical item Account Name. Meaning: Account description (e.g., "Sales", "Cost of Sales", "Bank Account").
Historical item Debit. Meaning: Debit balance (positive number or blank).
Historical item Credit. Meaning: Credit balance (positive number or blank).
```

#### Historical 4 - Transaction Type Codes

```text
Historical item /categories/001. Meaning: Sales/Revenue
Historical item /categories/100 to 199. Meaning: Cost of Sales categories
Historical item /categories/200 to 299. Meaning: Operating expenses
Historical item /categories/300 to 399. Meaning: Assets
Historical item /categories/400 to 499. Meaning: Liabilities
Historical item /categories/500 to 599. Meaning: Equity/Capital
```

#### Historical 5 - Fee Structure

```text
Historical item FreeAgent (standard). Price: £29/month (£24/month annual); Notes: Full features.
Historical item FreeAgent (NatWest/RBS/Ulster). Price: Free; Notes: Included with NatWest Group business banking.
```

#### Historical navigation and API descriptions

```text
- Despite documentation, FreeAgent does accept commas within double-quoted strings in the Description field. However, the > character renders incorrectly (known FreeAgent bug).
### FreeAgent API Bank Transaction Fields
When accessing data via the FreeAgent API, transactions have these fields:
5. **The > character bug.** Greater-than signs in descriptions render as literal HTML entities in FreeAgent's UI. Avoid them in CSV descriptions.
```

#### Historical tax-field names, definitions require actual supplied mapping

- VAT amount (historical location Explanation detail (not in bank CSV)); retain as an investigation field, not proof of tax treatment.
- gross_value (historical location API explanation field); retain as an investigation field, not proof of tax treatment.
- sales_tax_value (historical location API explanation field); retain as an investigation field, not proof of tax treatment.
- EC status (historical location Invoice/bill level); retain as an investigation field, not proof of tax treatment.
- CIS deductions (historical location Payroll/subcontractor); retain as an investigation field, not proof of tax treatment.
- MTD VAT (historical location Report export); retain as an investigation field, not proof of tax treatment.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `freeagent-integration` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/freeagent-integration. If neither is available, confirm every figure against the official source pages cited above before relying on it.
