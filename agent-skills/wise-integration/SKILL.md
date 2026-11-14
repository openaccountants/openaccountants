---
name: wise-integration
description: "Reconcile supplied wise exports for bookkeeping in 2026. Establish the actual schema, account, dates and currency, preserve order/invoice/payment relationships, reject malformed or unreconciled data and prepare postings for human approval. Historical fields and sample data are retained, but current API, software and fee behaviour is not certified."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/wise-integration"
  jurisdiction: "GLOBAL"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Wise statements and paired-currency reconciliation v2.0

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

### Wise-specific controls

Identify balance statement versus transfer-list data and obtain all relevant currency balances, account identifiers and source statements. Preserve original payer/payee, merchant and reference evidence. Support card purchases/refunds, direct debits, top-ups, own transfers, conversion legs, charges, interest and cashback with their actual commercial classification. A narrative search is a candidate, not a definitive type code.

The retained GBP example records transfer fees in signed cash movements and also repeats fee information in `Total fees`. Do not add a fee-column total to separate fee rows without proving it is a different charge. It contradicts the old claim that fees always have one fixed presentation. The EUR 1,153.20 counterpart described in the GBP conversion narrative has no complete EUR statement here; the second currency remains unreconciled. An effective conversion ratio is not proof of an FX spread, the provider's margin or a deductible fee. Do not infer VAT exemption, tax on interest, banking licence or document acceptance by a tax office from the Wise brand. Obtain the actual fee document and country's rule.

## Worked case

The retained nine-row GBP fixture implies an illustrative GBP 6,250 opening from its first balance less first movement and closes at GBP 8,285.07. Actual fee movements are GBP 6.66. Adding the repeated GBP 2.10 from the contractor row would incorrectly report GBP 8.76. This is a cash reconciliation, not proof that every receipt is revenue or every outgoing amount is deductible.

```oa-check
name: Wise statements and paired-currency reconciliation
inputs:
  opening: 6250
  receipts: 3390.5
  conversion: 1000
  contractor: 350
  fee_one: 4.56
  fee_two: 2.1
  purchase: 45.99
  refund: 45.99
  interest: 1.23
  repeated_fee: 2.1
steps:
  - cash_fees: fee_one + fee_two
  - naive_fee_total: cash_fees + repeated_fee
  - closing: opening + receipts - conversion - contractor - cash_fees - purchase + refund + interest
expected:
  cash_fees: 6.66
  naive_fee_total: 8.76
  closing: 8285.07
```

## Retained supplied-data fixtures

These are the original illustrations, retained byte-for-byte inside their code blocks. They are not certified current platform exports, fee schedules or complete accounts. Use the worked control above and the validation method before using any record. A failed example must remain failed, not silently repaired.

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

Not yet confirmed: the live wise API/schema, exact export/import column positions and availability, UI/report paths, region/plan capabilities, pricing and fee/refund conventions, automatic tax/FX behaviour, regulatory status and third-party document acceptance. The following literal table/path inventory records what the old file claimed, only to help locate and compare supplied data. Its fees, codes, timing, default settings and field meanings are historical and must not be treated as 2026 guidance. Known accounting/tax errors are replaced by the method and country boundaries above. No vendor source was used.

### Historical schema and claim inventory, not usable guidance

#### Historical 2 - Export Formats

```text
Historical item CSV. Use Case: Per-currency balance statements, transfer lists
Historical item XLSX (Excel). Use Case: Per-currency balance statements
Historical item PDF. Use Case: Official bank statements (accepted by HMRC, tax offices, lenders)
Historical item MT940. Use Case: Accounting software import (SWIFT standard)
Historical item QIF. Use Case: Quicken import format
Historical item CAMT.053. Use Case: European bank standard XML format (v10 only)
```

#### Historical Balance Statement CSV

```text
Historical item TransferWise ID. Meaning: Unique transaction identifier (numeric). Also labelled "ID" in some exports.
Historical item Date. Meaning: Transaction date. Format varies by account region: DD-MM-YYYY (UK), MM-DD-YYYY (US), YYYY-MM-DD (some regions).
Historical item Amount. Meaning: Transaction amount. Positive = money in, negative = money out. Decimal separator varies by region (period or comma).
Historical item Currency. Meaning: Three-letter ISO code for the balance currency (GBP, EUR, USD).
Historical item Description. Meaning: Transaction narrative: recipient name, transfer reference, card payment merchant, or fee description.
Historical item Payment Reference. Meaning: Payment reference or memo attached to the transfer.
Historical item Running Balance. Meaning: Balance after this transaction.
Historical item Exchange Rate. Meaning: FX rate applied if this transaction involved a currency conversion. Blank/null for same-currency transactions.
Historical item Payer Name. Meaning: Name of the person who sent the payment (for incoming transfers).
Historical item Payee Name. Meaning: Name of the recipient (for outgoing transfers).
Historical item Payee Account Number. Meaning: Recipient's account number (if available).
Historical item Merchant. Meaning: Merchant name for card payments.
Historical item Total fees. Meaning: Fee amount charged for this transaction. May be zero.
```

#### Historical Transfer List CSV (downloaded from Transactions page)

```text
Historical item ID. Meaning: Transfer ID
Historical item Date. Meaning: Creation date of the transfer
Historical item Amount. Meaning: Amount sent or received
Historical item Currency. Meaning: Source or target currency
Historical item Recipient. Meaning: Recipient name
Historical item Status. Meaning: Completed, Cancelled, Pending
Historical item Direction. Meaning: INCOMING or OUTGOING
Historical item Fee. Meaning: Fee charged for the transfer
Historical item Exchange Rate. Meaning: Rate applied
```

#### Historical 4 - Transaction Type Codes

```text
Historical item "Received money from [Name]". Meaning: Incoming transfer from another Wise user or external bank
Historical item "Sent money to [Name]". Meaning: Outgoing transfer
Historical item "Card payment to [Merchant]". Meaning: Debit card purchase
Historical item "Card refund from [Merchant]". Meaning: Card payment refund
Historical item "Converted [amount] [CCY] to [amount] [CCY]". Meaning: Currency conversion between balances
Historical item "Direct Debit to [Name]". Meaning: Direct debit payment
Historical item "Added money from [Bank]". Meaning: Top-up from linked bank account
Historical item "Wise fee for transfer [ID]". Meaning: Fee charged as a separate line item
Historical item "Interest". Meaning: Interest earned on balance
Historical item "Cashback". Meaning: Cashback reward
```

#### Historical 5 - Fee Structure

```text
Historical item Transfer fee. How It Appears: Separate line item in the CSV with negative amount and description "Wise fee for transfer [ID]". Always a distinct row , never deducted from the transfer amount in the same row.
Historical item Currency conversion fee. How It Appears: Included in the exchange rate spread. Not shown as a separate line. The mid-market rate vs Wise's rate difference is the implicit fee.
Historical item Card payment fee. How It Appears: Usually zero for standard payments. Cross-currency card payments include a conversion spread.
Historical item Monthly account fee. How It Appears: Wise Business: £0 for standard, varies for premium plans. Appears as a separate transaction.
Historical item ATM withdrawal fee. How It Appears: Free up to limits, then ~£1.50 per withdrawal. Separate line item.
```

#### Historical 7 - Multi-Currency Handling

```text
Historical item Single-currency statement. How It Appears: One CSV per currency balance. All amounts in that currency.
Historical item Currency conversion. How It Appears: Appears as **two entries across two statements**: a debit in the source currency statement and a credit in the destination currency statement. Both reference the same transfer ID.
Historical item Incoming foreign payment. How It Appears: May arrive in the sender's currency and auto-convert, or may credit the matching currency balance directly.
Historical item Exchange Rate column. How It Appears: Populated only for transactions involving FX conversion. Shows the rate applied.
Historical item Mid-market rate vs Wise rate. How It Appears: Wise advertises the mid-market rate but applies a slightly different rate including their margin. The Exchange Rate column shows the actual rate applied.
```

#### Historical tax-field names, definitions require actual supplied mapping

- Currency; retain as an investigation field, not proof of tax treatment.
- Exchange Rate; retain as an investigation field, not proof of tax treatment.
- Total fees; retain as an investigation field, not proof of tax treatment.
- Interest; retain as an investigation field, not proof of tax treatment.
- Payer/Payee details; retain as an investigation field, not proof of tax treatment.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `wise-integration` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/wise-integration. If neither is available, confirm every figure against the official source pages cited above before relying on it.
