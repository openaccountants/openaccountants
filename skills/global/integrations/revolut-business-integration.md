---
name: revolut-business-integration
version: 2.0
category: bookkeeping
description: >
  Reconcile supplied revolut-business exports for bookkeeping in 2026. Establish the actual schema, account, dates and currency, preserve order/invoice/payment relationships, reject malformed or unreconciled data and prepare postings for human approval. Historical fields and sample data are retained, but current API, software and fee behaviour is not certified.
jurisdiction: GLOBAL
last_updated: 2026-11-14
tier: 2
domain: bookkeeping
tax_year: 2026
type: cross-country-method
checked_on: 2026-11-14
---

# Revolut Business account and currency reconciliation v2.0

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
6. **Prepare the commercial accounting.** Link the invoice/order/bill and payment, preserve tax and shipping detail, and separate amounts collected for others. A customer shipping charge can be part of the seller's consideration; it is not automatically removed from revenue. Gross cash does not always equal revenue, and a net payout is not by itself proof of agency. Under an applicable AASB 15/IFRS-equivalent reporting policy, assess control of each specified good/service, principal versus agent and third-party collections using paragraphs 47 and B34-B38. That conditional financial-reporting test does not replace local tax law. [AASB 15](https://standards.aasb.gov.au/sites/default/files/2026-11/AASB 15_12-14_COMPdec22_07-26.pdf).
7. **Apply the owning country's tax method.** Currency, marketplace suffix, email, billing country or a configured software tax code alone does not establish tax jurisdiction, business status, nexus or recoverability. Read the actual supply, establishment, customer, product, destination and registrations; link the official rule used. A payment-only file may lack the tax breakdown. UK sole-trader/partner records must identify business transactions and preserve receipts, invoices and statements; traditional accounting also tracks amounts owed/unpaid. Eligible UK business bank charges are distinct from non-deductible loan principal. [HMRC records](https://www.gov.uk/self-employed-records/what-records-to-keep); [financial charges](https://www.gov.uk/expenses-if-youre-self-employed/legal-financial).
8. **Handle foreign currency without losing either leg.** Keep original, settlement and functional-currency amounts and rate directions. Pair own-account conversion/transfer legs using documented IDs and accounts, not timestamp proximity alone. Transfer principal is not a sale, but settlement/translation differences and separately evidenced charges require their own treatment. For an applicable AASB 121/IFRS-equivalent reporting policy, use recognition-date rates, closing rates for monetary balances and the stated settlement-difference exceptions. An average is acceptable only when it reasonably approximates actual rates. Tax translation follows its own country's method. [AASB 121 paragraphs 21-23,27-30](https://standards.aasb.gov.au/sites/default/files/2025-03/AASB 121_08-15_COMPoct23_01-25.pdf).
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

### Revolut Business-specific controls

Distinguish aggregated transaction exports from statements for each currency/account. Record the actual Revolut legal entity and product; a brand-level claim that it is always the bank, or that no separate closing statement is needed, is unsupported. Reconcile to account evidence even where the provider maintains the account. Keep original/payment currencies, payer and beneficiary details, card suffix and account identity; an empty payer field on an outgoing payment does not prove an unknown recipient.

Preserve started and completed timestamps, actual pending/settled status and period cutoff. Completed date can establish a cash movement; it is not always the accrual recognition date. Pair exchange legs and own-account top-ups, separate loan proceeds/principal/interest and withheld tax, and investigate rewards and interest by the actual product and tax jurisdiction. Fee rows and fee cells can coexist; test for duplication. Orig/payment currency does not determine tax residence or make every fee deductible. An implicit conversion ratio cannot prove a weekend markup or its amount.

## Worked case

The eight retained rows reconcile separately to GBP 7,954.27 and EUR 1,128.80 on the stated illustrative openings. Jane Smith Contractor, the GBP 25 plan charge and all other narratives remain sample facts, not evidence of current prices, deductibility or service-provider status.

```oa-check
name: Revolut Business account and currency reconciliation
inputs:
  opening_gbp: 10000
  receipt: 2500
  amazon: 156.99
  exchange_gbp: 1000
  contractor: 3200
  plan: 25
  hotel_gbp: 163.74
  opening_eur: 0
  exchange_eur: 1152.3
  meal_eur: 23.5
steps:
  - closing_gbp: opening_gbp + receipt - amazon - exchange_gbp - contractor - plan - hotel_gbp
  - closing_eur: opening_eur + exchange_eur - meal_eur
expected:
  closing_gbp: 7954.27
  closing_eur: 1128.8
```

## Retained supplied-data fixtures

These are the original illustrations, retained byte-for-byte inside their code blocks. They are not certified current platform exports, fee schedules or complete accounts. Use the worked control above and the validation method before using any record. A failed example must remain failed, not silently repaired.

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

## Existing review requirement

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

## Sources

| Official source | Read on | Read scope |
|---|---|---|
| https://www.gov.uk/self-employed-records/what-records-to-keep | 2026-11-14 | Read for sales/expense proof, accurate records, distinguishing business transactions and accrual records. |
| https://www.gov.uk/expenses-if-youre-self-employed/legal-financial | 2026-11-14 | Read for business bank/credit-card charges, loan principal exclusion and bad debts/cash-basis distinction for UK sole traders and partners. |
| https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a | 2026-11-14 | Read for sections 2-6 and 13, actual supply, belonging, reverse-charge conditions, input-tax limits and unregistered recipients. |
| https://standards.aasb.gov.au/sites/default/files/2026-11/AASB 15_12-14_COMPdec22_07-26.pdf | 2026-11-14 | Read for paragraphs 47,105-108,B34-B38 and B44-B47 for third-party collections, receivables/contract liabilities, principal-agent control and unexercised rights. Conditional Australian IFRS-equivalent financial-reporting scope, not worldwide tax law. |
| https://standards.aasb.gov.au/sites/default/files/2025-03/AASB 121_08-15_COMPoct23_01-25.pdf | 2026-11-14 | Read for paragraphs 20-23 and 27-30, initial recognition, monetary closing balances and settlement exchange differences; Australian IFRS-equivalent financial reporting, not universal tax translation. |

Not yet confirmed: the live revolut-business API/schema, exact export/import column positions and availability, UI/report paths, region/plan capabilities, pricing and fee/refund conventions, automatic tax/FX behaviour, regulatory status and third-party document acceptance. The following literal table/path inventory records what the old file claimed, only to help locate and compare supplied data. Its fees, codes, timing, default settings and field meanings are historical and must not be treated as 2026 guidance. Known accounting/tax errors are replaced by the method and country boundaries above. No vendor source was used.

### Historical schema and claim inventory, not usable guidance

#### Historical 2 - Export Formats

```text
Historical item CSV. Use Case: Transaction statements (per account or all accounts). Downloaded from Transactions > Export.
Historical item Excel (XLSX). Use Case: Same data as CSV but formatted for Excel.
Historical item PDF. Use Case: Official bank statements. Per-currency, monthly. Required for formal purposes.
Historical item MT940. Use Case: SWIFT standard for accounting software integration.
Historical item CAMT.053. Use Case: European XML banking standard.
Historical item QIF. Use Case: Quicken import format.
```

#### Historical Transaction Statement CSV

```text
Historical item Date started (UTC). Meaning: Timestamp when the transaction was initiated. Format: YYYY-MM-DD HH:MM:SS. Timezone depends on account settings , may say "(UTC)" or "(Europe/Amsterdam)" etc.
Historical item Date completed (UTC). Meaning: Timestamp when the transaction was completed/settled. Same timezone note as above.
Historical item ID. Meaning: Unique Revolut transaction identifier.
Historical item Type. Meaning: Transaction type code (see Section 4).
Historical item Description. Meaning: Transaction narrative: counterparty name, merchant, transfer reference.
Historical item Reference. Meaning: Payment reference or memo.
Historical item Payer. Meaning: Name of the person/entity who initiated the payment (incoming transfers).
Historical item Card number. Meaning: Last 4 digits of the card used (for card payments). Blank for non-card transactions.
Historical item Orig currency. Meaning: Original currency of the transaction (before any conversion).
Historical item Orig amount. Meaning: Original amount in the original currency.
Historical item Payment currency. Meaning: Currency the payment was settled in.
Historical item Amount. Meaning: Settlement amount in the payment currency. Positive = money in, negative = money out.
Historical item Fee. Meaning: Fee charged by Revolut for this transaction. Usually 0.00 for standard transactions.
Historical item Balance. Meaning: Running balance after this transaction in the payment currency.
Historical item Account. Meaning: Name/identifier of the Revolut account (e.g., "Main GBP", "EUR account").
Historical item Beneficiary account number. Meaning: Recipient's account number (for outgoing transfers).
Historical item Beneficiary sort code or routing number. Meaning: Recipient's sort code (UK) or routing number (US).
Historical item Beneficiary IBAN. Meaning: Recipient's IBAN (for SEPA/international transfers).
Historical item Beneficiary BIC. Meaning: Recipient's BIC/SWIFT code.
```

#### Historical 4 - Transaction Type Codes

```text
Historical item CARD_PAYMENT. Meaning: Debit card purchase at a merchant
Historical item CARD_REFUND. Meaning: Refund to the debit card
Historical item TRANSFER. Meaning: Bank transfer sent or received (SWIFT, SEPA, Faster Payments, ACH)
Historical item EXCHANGE. Meaning: Currency conversion between Revolut balances
Historical item TOPUP. Meaning: Money added from an external bank account or card
Historical item ATM. Meaning: Cash withdrawal from ATM
Historical item FEE. Meaning: Revolut service fee (subscription, card replacement, etc.)
Historical item REWARD. Meaning: Cashback or promotional credit
Historical item DIRECT_DEBIT. Meaning: UK/SEPA direct debit payment
Historical item TAX. Meaning: Tax withholding (applies in some jurisdictions for interest)
Historical item INTEREST. Meaning: Interest earned on balance
Historical item LOAN. Meaning: Loan disbursement or repayment
```

#### Historical 5 - Fee Structure

```text
Historical item FX conversion (within allowance). How It Appears: Zero fee. Exchange at interbank rate during market hours.
Historical item FX conversion (over allowance or weekend). How It Appears: 0.4% to 1% markup on exchange rate. Appears as implicit spread, NOT as a separate fee.
Historical item International transfer (SWIFT). How It Appears: Fee in the Fee column. Typically £3 to 5 per transfer.
Historical item SEPA transfer. How It Appears: Free on most plans.
Historical item UK Faster Payments. How It Appears: Free.
Historical item Card payment (domestic). How It Appears: Free.
Historical item Card payment (cross-currency). How It Appears: Exchange rate spread applies. No explicit fee in the Fee column.
Historical item ATM withdrawal (over limit). How It Appears: Fee appears in the Fee column. £2 per withdrawal over the monthly limit.
Historical item Monthly subscription. How It Appears: Separate row with Type = FEE. Free, Grow (£25/mo), Scale (£100/mo), Enterprise (custom).
Historical item Card replacement. How It Appears: Separate row with Type = FEE.
```

#### Historical 7 - Multi-Currency Handling

```text
Historical item Single-currency account. How It Appears: All rows share the same Payment currency. Straightforward.
Historical item Currency exchange. How It Appears: Type = EXCHANGE. Two rows: one debit in the source currency, one credit in the target currency. Orig currency/Orig amount show the source; Payment currency/Amount show the target.
Historical item Cross-currency card payment. How It Appears: Single row. Orig currency shows the merchant's currency (e.g., EUR). Payment currency shows the account currency (e.g., GBP). Orig amount and Amount differ by the exchange rate.
Historical item Implicit exchange rate. How It Appears: Not shown as a column. Calculate: Amount ÷ Orig amount = effective rate.
Historical item Weekend/out-of-hours FX. How It Appears: Revolut applies a markup (0.4 to 1%) on weekends. The rate is worse but appears the same way in the CSV , only the effective rate reveals the markup.
```

#### Historical tax-field names, definitions require actual supplied mapping

- Orig currency / Payment currency; retain as an investigation field, not proof of tax treatment.
- Fee; retain as an investigation field, not proof of tax treatment.
- Type = INTEREST; retain as an investigation field, not proof of tax treatment.
- Type = TAX; retain as an investigation field, not proof of tax treatment.
- Beneficiary details; retain as an investigation field, not proof of tax treatment.
- Account; retain as an investigation field, not proof of tax treatment.
