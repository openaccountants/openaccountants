---
name: stripe-integration
version: 1.0
category: integration
description: >
  Integration skill for Stripe payment platform CSV exports. Activate when the user uploads a Stripe balance
  transaction report, payout report, or mentions Stripe, Stripe payments, or Stripe CSV.
jurisdiction: GLOBAL
tier: 2
last_updated: 2026-06-12
---

# Stripe Integration Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Section 1 — Platform Overview

Stripe is an online payment processing platform used by businesses of all sizes to accept card payments, manage subscriptions, send invoices, and handle payouts. Headquartered in the US (San Francisco/Dublin), Stripe operates in 47+ countries. It is the dominant payment processor for SaaS, e-commerce, and platform/marketplace businesses.

Stripe provides two main CSV export paths: **Dashboard exports** (Balance > Download CSV) and **Reporting API exports** (programmatic, customisable columns). Most users export from the Dashboard.

---

## Section 2 — Export Formats

| Format | Use Case |
|--------|----------|
| CSV | Balance transactions (itemised), payouts (itemised), balance summary. Downloaded from Dashboard or via Reporting API. |
| PDF | Individual invoices, receipts |
| JSON | API responses (for developers) |
| Excel | Not native — users convert CSV to Excel manually |

The **Balance change from activity (itemised)** CSV is the primary export for bookkeeping. The **Payouts (itemised)** CSV links transactions to specific bank payouts.

---

## Section 3 — Column Mapping

### Balance Change from Activity — Itemised (Dashboard download)

| Column Header | Default | Meaning |
|---------------|---------|---------|
| balance_transaction_id | Yes | Unique ID for the balance transaction (e.g., txn_1MiN3gLk...) |
| created (UTC) | Yes | Timestamp when the transaction was created. Format: YYYY-MM-DD HH:MM |
| available_on (UTC) | Yes | Date when net funds become available for payout. |
| currency | Yes | Three-letter ISO code (usd, gbp, eur). Lowercase. |
| gross | Yes | Gross amount in major currency units (e.g., 100.00 not 10000). |
| fee | Yes | Stripe fees deducted. Always positive or zero. |
| net | Yes | Net amount after fees (gross - fee). |
| reporting_category | Yes | Accounting-style category: charge, refund, dispute, transfer, fee, etc. |
| description | Yes | One-line description (e.g., "Payment for Invoice #1234"). |
| customer_facing_amount | No | Amount in customer's currency (for cross-currency payments). |
| customer_facing_currency | No | Customer's currency if different from settlement currency. |
| automatic_payout_id | No | ID of the payout this transaction was included in. |
| automatic_payout_effective_at (UTC) | No | Date the payout reached the bank. |
| source_id | No | ID of the source object (ch_xxx for charge, re_xxx for refund). |
| customer_id | No | Stripe customer ID. |
| customer_email | No | Customer email address. |
| customer_name | No | Customer name. |
| payment_method_type | No | Card brand/type (visa, mastercard, amex, sepa_debit, etc.). |
| invoice_id | No | Stripe Invoice ID if applicable. |

### Payouts — Itemised

| Column Header | Meaning |
|---------------|---------|
| payout_id | Unique payout identifier (po_xxx). |
| payout_expected_arrival_date | Date the payout should arrive at the bank. |
| payout_status | paid, pending, in_transit, canceled, failed. |
| payout_description | Payout description (often "STRIPE PAYOUT" or "STRIPE TRANSFER"). |
| balance_transaction_id | Links to balance transaction itemised report. |
| currency | Settlement currency. |
| gross | Gross per transaction. |
| fee | Fee per transaction. |
| net | Net per transaction. |
| reporting_category | Category (charge, refund, etc.). |

---

## Section 4 — Transaction Type Codes

Stripe uses the `reporting_category` field for accounting classification:

| reporting_category | Meaning |
|-------------------|---------|
| charge | Successful payment from a customer |
| refund | Full or partial refund to customer |
| dispute | Chargeback initiated by cardholder |
| dispute_reversal | Chargeback reversed (won by merchant) |
| transfer | Payout to connected account (Stripe Connect) |
| fee | Stripe platform fees |
| connect_reserved_funds | Funds held in reserve |
| payout | Transfer to the merchant's bank account |
| payout_reversal | Payout reversed/returned by bank |
| other_adjustment | Manual adjustments by Stripe |
| partial_capture_reversal | Uncaptured portion of an authorisation |
| issuing_authorization_hold | Stripe Issuing card hold |
| topup | Balance top-up |

The legacy `type` field uses older values: payment, refund, transfer, adjustment, payout, stripe_fee. Prefer `reporting_category` for new integrations.

---

## Section 5 — Fee Structure

| Fee Type | Typical Rate | How It Appears |
|----------|-------------|----------------|
| Card processing | 2.9% + $0.30 (US) / 1.4% + £0.20 (UK/EEA) | Deducted per transaction in the `fee` column |
| International card surcharge | +1.5% | Added to the base fee |
| Currency conversion | +1% | Added when customer currency differs from settlement currency |
| Dispute (chargeback) fee | $15.00 | Separate line with reporting_category = dispute |
| Refund fee | Processing fee not returned | Original fee remains; refund appears as negative gross |
| Stripe Tax | Varies | Separate line items on Stripe-issued invoices |
| Connect platform fee | Custom | Separate line for platform/marketplace setups |

Stripe always reports gross, fee, and net separately. The `fee` column is the total fee including all components (processing + international + currency conversion).

---

## Section 6 — Tax-Relevant Fields

| Field | Notes |
|-------|-------|
| currency | Determines which tax jurisdiction may apply. |
| customer_facing_currency | Original currency the customer was charged in. |
| customer_email / customer_name | May be needed for reverse-charge VAT on B2B cross-border sales. |
| Stripe Tax | If Stripe Tax is enabled, tax amounts appear as separate data via the Stripe Tax API/exports, not in the balance transaction CSV. |
| Stripe-issued invoices | Stripe charges VAT on its own fees to EU/UK businesses. This appears on Stripe's invoice to the merchant, not in the balance CSV. |

Stripe does NOT include the merchant's output VAT/GST in the balance transaction CSV. Tax on sales must be calculated separately using the order/invoice data, not the Stripe payout data.

---

## Section 7 — Multi-Currency Handling

| Scenario | How It Appears |
|----------|---------------|
| Single-currency | All rows in one currency. `currency` column is consistent. |
| Multi-currency settlement | Separate balance per currency. Each CSV download is per-currency. |
| Cross-currency payment | `customer_facing_amount` and `customer_facing_currency` show original charge. `gross`/`fee`/`net` are in settlement currency. |
| Exchange rate | Not shown as a column in the standard CSV. Calculate from customer_facing_amount ÷ gross. Available via API as `exchange_rate` on the BalanceTransaction object. |
| Presentment vs settlement | A €50 charge settled in USD appears as gross = $54.50 (at Stripe's rate), customer_facing_amount = 50.00, customer_facing_currency = eur. |

---

## Section 8 — Reconciliation Tips

1. **Match payouts to bank.** Each payout (po_xxx) groups multiple balance transactions. The bank statement shows one deposit; the Stripe CSV shows the individual transactions. Sum `net` for each `automatic_payout_id` to match the bank deposit.
2. **Payout timing.** Standard payouts arrive 2 business days after the transaction (US). T+7 for new accounts. Expect date mismatches between Stripe `created` date and bank statement date.
3. **Fees are already deducted.** The bank deposit equals the sum of `net` amounts, not `gross`. Do not double-count fees.
4. **Refunds reduce the payout.** A refund in a payout period reduces the total payout amount. The bank deposit is net of refunds.
5. **Disputes temporarily remove funds.** A dispute appears as a negative `gross`. If won, a `dispute_reversal` adds funds back.
6. **Rolling reserve.** New or high-risk accounts may have funds held in reserve. These appear as `connect_reserved_funds` with later release.
7. **Stripe CSV has 9+ columns.** Cannot be directly imported into QuickBooks (max 4 columns) or most accounting software without transformation.

---

## Section 9 — Common Gotchas

1. **Gross vs net confusion.** The Stripe payout equals the SUM of `net`, not `gross`. Booking `gross` as revenue and `fee` as expense is correct accounting but the bank deposit matches `net`.
2. **Fee on refund.** When a payment is refunded, Stripe does not return the original processing fee. The refund row shows the refund amount as negative gross, zero fee, and negative net.
3. **Amounts in major units.** Stripe CSV exports amounts in dollars/pounds (100.00), but the API uses minor units/cents (10000). Ensure consistency when mixing sources.
4. **Lowercase currency codes.** Stripe uses "usd" not "USD" in CSV exports. Normalise to uppercase for accounting software.
5. **Timezone sensitivity.** `created (UTC)` is in UTC. Bank statements use local time. A late-night transaction may appear on different dates.
6. **Connect platforms.** If the user operates a Stripe Connect marketplace, application fees and transfers to connected accounts create additional balance transaction rows.
7. **Subscription invoices vs one-time payments.** Both appear as `charge` in reporting_category. Use `invoice_id` to distinguish recurring from one-time.

---

## Section 10 — Sample Data

### Balance Change from Activity — Itemised

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

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.
