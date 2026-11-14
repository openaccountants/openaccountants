---
name: stripe-integration
description: "Reconcile supplied stripe exports for bookkeeping in 2026. Establish the actual schema, account, dates and currency, preserve order/invoice/payment relationships, reject malformed or unreconciled data and prepare postings for human approval. Historical fields and sample data are retained, but current API, software and fee behaviour is not certified."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/stripe-integration"
  jurisdiction: "GLOBAL"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Stripe balance, payout and invoice reconciliation v2.0

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

### Stripe-specific controls

Keep balance-activity and itemised-payout jobs separate, plus invoice/receipt/API evidence. Match balance transaction IDs, source IDs, invoice IDs and payout IDs using the actual file. Connected-account transfers, application fees, reserve funds, uncaptured reversals, top-ups, dispute reversals and issuing holds need distinct mapping; a recurring invoice and a one-time charge cannot be classified from `charge` alone. Preserve created, available and arrival dates without imposing an unverified T+2/T+7 settlement rule. A settlement date does not replace accrual recognition.

The old assertion that every fee is positive conflicts with its own dispute row. The retained example is not importable as a reconciled payout. It also does not establish output VAT, customer business status or the current platform fee invoice's VAT treatment. A customer name/email or the payment currency cannot supply those facts. Normalise currency-case only in a derived field and retain the original. API and CSV units require separate supplied mappings; do not assume both use cents or both major units.

## Worked case

The seven-row historical fixture has six non-payout net movements totalling USD 2,354.82, against a USD 2,831.82 payout. The USD 477 gap and USD 30 signed-fee formula contradiction must stop posting; they are not extra revenue or an invented fee.

```oa-check
name: Stripe balance, payout and invoice reconciliation
inputs:
  gross: -150
  fee: -15
  reported_net: -165
  activity_net: 2354.82
  payout: 2831.82
steps:
  - formula_net: gross - fee
  - fee_formula_gap: reported_net - formula_net
  - payout_gap: payout - activity_net
expected:
  formula_net: -135
  fee_formula_gap: -30
  payout_gap: 477
```

## Retained supplied-data fixtures

These are the original illustrations, retained byte-for-byte inside their code blocks. They are not certified current platform exports, fee schedules or complete accounts. Use the worked control above and the validation method before using any record. A failed example must remain failed, not silently repaired.

```csv
balance_transaction_id,created (UTC),available_on (UTC),currency,gross,fee,net,reporting_category,description
txn_3PQ2aR4bCdE5fG6h,2026-03-15 14:23,2026-03-17,usd,150.00,4.65,145.35,charge,Payment for Invoice #1042
txn_7HI8jK9lMnO0pQ1r,2026-03-15 16:45,2026-03-17,usd,89.99,2.91,87.08,charge,Subscription renewal - Pro plan
txn_2ST3uV4wXyZ5aB6c,2026-03-16 09:12,2026-03-18,usd,-89.99,0.00,-89.99,refund,Refund for ch_xxx - customer request
txn_8DE9fG0hIjK1lM2n,2026-03-16 11:30,2026-03-18,usd,2400.00,69.90,2330.10,charge,Enterprise license - Acme Corp
txn_4OP5qR6sT7uV8wXy,2026-03-17 08:00,2026-03-19,usd,49.00,1.72,47.28,charge,One-time setup fee
txn_9ZA0bC1dE2fG3hIj,2026-03-17 14:15,2026-03-19,usd,-150.00,-15.00,-165.00,dispute,Chargeback - order #4501
txn_5KL6mN7oP8qR9sTu,2026-03-18 10:00,2026-03-18,usd,-2831.82,0.00,-2831.82,payout,STRIPE PAYOUT
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

Not yet confirmed: the live stripe API/schema, exact export/import column positions and availability, UI/report paths, region/plan capabilities, pricing and fee/refund conventions, automatic tax/FX behaviour, regulatory status and third-party document acceptance. The following literal table/path inventory records what the old file claimed, only to help locate and compare supplied data. Its fees, codes, timing, default settings and field meanings are historical and must not be treated as 2026 guidance. Known accounting/tax errors are replaced by the method and country boundaries above. No vendor source was used.

### Historical schema and claim inventory, not usable guidance

#### Historical 2 - Export Formats

```text
Historical item CSV. Use Case: Balance transactions (itemised), payouts (itemised), balance summary. Downloaded from Dashboard or via Reporting API.
Historical item PDF. Use Case: Individual invoices, receipts
Historical item JSON. Use Case: API responses (for developers)
Historical item Excel. Use Case: Not native , users convert CSV to Excel manually
```

#### Historical Balance Change from Activity - Itemised (Dashboard download)

```text
Historical item balance_transaction_id. Default: Yes; Meaning: Unique ID for the balance transaction (e.g., txn_1MiN3gLk...)
Historical item created (UTC). Default: Yes; Meaning: Timestamp when the transaction was created. Format: YYYY-MM-DD HH:MM
Historical item available_on (UTC). Default: Yes; Meaning: Date when net funds become available for payout.
Historical item currency. Default: Yes; Meaning: Three-letter ISO code (usd, gbp, eur). Lowercase.
Historical item gross. Default: Yes; Meaning: Gross amount in major currency units (e.g., 100.00 not 10000).
Historical item fee. Default: Yes; Meaning: Stripe fees deducted. Always positive or zero.
Historical item net. Default: Yes; Meaning: Net amount after fees (gross - fee).
Historical item reporting_category. Default: Yes; Meaning: Accounting-style category: charge, refund, dispute, transfer, fee, etc.
Historical item description. Default: Yes; Meaning: One-line description (e.g., "Payment for Invoice #1234").
Historical item customer_facing_amount. Default: No; Meaning: Amount in customer's currency (for cross-currency payments).
Historical item customer_facing_currency. Default: No; Meaning: Customer's currency if different from settlement currency.
Historical item automatic_payout_id. Default: No; Meaning: ID of the payout this transaction was included in.
Historical item automatic_payout_effective_at (UTC). Default: No; Meaning: Date the payout reached the bank.
Historical item source_id. Default: No; Meaning: ID of the source object (ch_xxx for charge, re_xxx for refund).
Historical item customer_id. Default: No; Meaning: Stripe customer ID.
Historical item customer_email. Default: No; Meaning: Customer email address.
Historical item customer_name. Default: No; Meaning: Customer name.
Historical item payment_method_type. Default: No; Meaning: Card brand/type (visa, mastercard, amex, sepa_debit, etc.).
Historical item invoice_id. Default: No; Meaning: Stripe Invoice ID if applicable.
```

#### Historical Payouts - Itemised

```text
Historical item payout_id. Meaning: Unique payout identifier (po_xxx).
Historical item payout_expected_arrival_date. Meaning: Date the payout should arrive at the bank.
Historical item payout_status. Meaning: paid, pending, in_transit, canceled, failed.
Historical item payout_description. Meaning: Payout description (often "STRIPE PAYOUT" or "STRIPE TRANSFER").
Historical item balance_transaction_id. Meaning: Links to balance transaction itemised report.
Historical item currency. Meaning: Settlement currency.
Historical item gross. Meaning: Gross per transaction.
Historical item fee. Meaning: Fee per transaction.
Historical item net. Meaning: Net per transaction.
Historical item reporting_category. Meaning: Category (charge, refund, etc.).
```

#### Historical 4 - Transaction Type Codes

```text
Historical item charge. Meaning: Successful payment from a customer
Historical item refund. Meaning: Full or partial refund to customer
Historical item dispute. Meaning: Chargeback initiated by cardholder
Historical item dispute_reversal. Meaning: Chargeback reversed (won by merchant)
Historical item transfer. Meaning: Payout to connected account (Stripe Connect)
Historical item fee. Meaning: Stripe platform fees
Historical item connect_reserved_funds. Meaning: Funds held in reserve
Historical item payout. Meaning: Transfer to the merchant's bank account
Historical item payout_reversal. Meaning: Payout reversed/returned by bank
Historical item other_adjustment. Meaning: Manual adjustments by Stripe
Historical item partial_capture_reversal. Meaning: Uncaptured portion of an authorisation
Historical item issuing_authorization_hold. Meaning: Stripe Issuing card hold
Historical item topup. Meaning: Balance top-up
```

#### Historical 5 - Fee Structure

```text
Historical item Card processing. Typical Rate: 2.9% + $0.30 (US) / 1.4% + £0.20 (UK/EEA); How It Appears: Deducted per transaction in the `fee` column
Historical item International card surcharge. Typical Rate: +1.5%; How It Appears: Added to the base fee
Historical item Currency conversion. Typical Rate: +1%; How It Appears: Added when customer currency differs from settlement currency
Historical item Dispute (chargeback) fee. Typical Rate: $15.00; How It Appears: Separate line with reporting_category = dispute
Historical item Refund fee. Typical Rate: Processing fee not returned; How It Appears: Original fee remains; refund appears as negative gross
Historical item Stripe Tax. Typical Rate: Varies; How It Appears: Separate line items on Stripe-issued invoices
Historical item Connect platform fee. Typical Rate: Custom; How It Appears: Separate line for platform/marketplace setups
```

#### Historical 7 - Multi-Currency Handling

```text
Historical item Single-currency. How It Appears: All rows in one currency. `currency` column is consistent.
Historical item Multi-currency settlement. How It Appears: Separate balance per currency. Each CSV download is per-currency.
Historical item Cross-currency payment. How It Appears: `customer_facing_amount` and `customer_facing_currency` show original charge. `gross`/`fee`/`net` are in settlement currency.
Historical item Exchange rate. How It Appears: Not shown as a column in the standard CSV. Calculate from customer_facing_amount ÷ gross. Available via API as `exchange_rate` on the BalanceTransaction object.
Historical item Presentment vs settlement. How It Appears: A €50 charge settled in USD appears as gross = $54.50 (at Stripe's rate), customer_facing_amount = 50.00, customer_facing_currency = eur.
```

#### Historical identifiers

```text
automatic_payout_id
charge
connect_reserved_funds
created
created (UTC)
currency
customer_facing_amount
customer_facing_currency
dispute_reversal
exchange_rate
fee
gross
invoice_id
net
reporting_category
type
```

#### Historical navigation and API descriptions

```text
Stripe provides two main CSV export paths: **Dashboard exports** (Balance > Download CSV) and **Reporting API exports** (programmatic, customisable columns). Most users export from the Dashboard.
3. **Amounts in major units.** Stripe CSV exports amounts in dollars/pounds (100.00), but the API uses minor units/cents (10000). Ensure consistency when mixing sources.
```

#### Historical tax-field names, definitions require actual supplied mapping

- currency; retain as an investigation field, not proof of tax treatment.
- customer_facing_currency; retain as an investigation field, not proof of tax treatment.
- customer_email / customer_name; retain as an investigation field, not proof of tax treatment.
- Stripe Tax; retain as an investigation field, not proof of tax treatment.
- Stripe-issued invoices; retain as an investigation field, not proof of tax treatment.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `stripe-integration` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/stripe-integration. If neither is available, confirm every figure against the official source pages cited above before relying on it.
