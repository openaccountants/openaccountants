---
name: shopify-integration
version: 1.0
category: integration
description: >
  Integration skill for Shopify Payments and Orders CSV exports. Activate when the user uploads a Shopify CSV,
  Shopify payments export, Shopify orders export, or mentions Shopify transactions.
jurisdiction: GLOBAL
tier: 2
last_updated: 2026-06-12
---

# Shopify Integration Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Section 1 — Platform Overview

Shopify is an e-commerce platform used by merchants in 175+ countries to sell products online, in-store, and across social media channels. Headquartered in Canada, Shopify powers businesses from single-product stores to large enterprises. Shopify Payments is the integrated payment processor (powered by Stripe).

Shopify produces two distinct CSV exports relevant to bookkeeping: the **Payments export** (financial transactions from Shopify Payments) and the **Orders export** (order-level data including line items, shipping, and customer details). These serve different purposes and have different column structures.

---

## Section 2 — Export Formats

| Format | Use Case |
|--------|----------|
| CSV (Plain) | Payments transactions (from Finance > Payouts > View Transactions > Export > Plain CSV). The correct format for accounting. |
| CSV for Excel | Payments transactions with extra formatting rows. Breaks most import tools — avoid for accounting. |
| CSV | Orders export (from Orders page > Export). Order-level data with line items. |
| PDF | Individual order invoices, packing slips. |
| Excel (XLSX) | Financial summary reports. |

**Critical: Always use "Plain CSV" for payment data.** "CSV for Excel" adds summary rows that break column header detection in accounting software.

---

## Section 3 — Column Mapping

### Shopify Payments CSV (Plain — Finance > Payouts)

| Column Header | Meaning |
|---------------|---------|
| Transaction Date | Timestamp with timezone. Format: YYYY-MM-DD HH:MM:SS ±HHMM (e.g., 2026-03-15 14:23:45 -0500). |
| Type | Transaction type (see Section 4). |
| Order | Shopify order number (e.g., #1001). Blank for non-order transactions. |
| Card Brand | Card brand used (visa, mastercard, amex, etc.). Blank for non-card payments. |
| Card Source | How the card was used (direct, online, swipe, chip, contactless). |
| Payout Status | pending, paid, in_transit, failed. |
| Payout Date | Date the payout was sent to the bank. |
| Available On | Date the funds become available. |
| Amount | Transaction amount in settlement currency. Positive for charges, negative for refunds. |
| Fee | Shopify Payments processing fee. Stored as a POSITIVE number (unlike PayPal which uses negative). |
| Net | Net amount (Amount - Fee). This is what gets deposited. |
| Currency | Three-letter ISO code (USD, GBP, EUR, CAD). Uppercase. |
| Checkout | Shopify checkout token (internal reference). |
| Payment Method | Payment method type (shopify_payments, manual, gift_card, etc.). |
| Payout ID | Identifier linking to a specific bank payout. |

### Shopify Orders Export CSV

| Column Header | Meaning |
|---------------|---------|
| Name | Order number (e.g., #1001). |
| Email | Customer email address. |
| Phone | Customer phone number. |
| Financial Status | paid, authorized, partially_paid, partially_refunded, refunded, pending, voided. |
| Paid at | Date payment was captured. |
| Fulfillment Status | fulfilled, partial, unfulfilled, restocked. |
| Fulfilled at | Date order was shipped. |
| Currency | Order currency (ISO code). |
| Subtotal | Order total before shipping and taxes. |
| Shipping | Shipping amount charged. |
| Taxes | Total tax amount. |
| Total | Grand total (Subtotal + Shipping + Taxes - Discounts). |
| Discount Code | Discount code applied (if any). |
| Discount Amount | Discount value applied. |
| Shipping Method | Shipping method name. |
| Created at | Order creation timestamp. |
| Lineitem quantity | Quantity of the line item. |
| Lineitem name | Product name. |
| Lineitem price | Unit price of the line item. |
| Lineitem sku | Product SKU. |
| Lineitem requires shipping | true/false. |
| Lineitem taxable | true/false. |
| Lineitem fulfillment status | fulfilled/unfulfilled. |
| Billing Name | Customer billing name. |
| Billing Address1 | Billing street address. |
| Billing City | Billing city. |
| Billing Province | Billing state/province. |
| Billing Country | Billing country. |
| Billing Zip | Billing postal code. |
| Payment Method | How the order was paid. |
| Payment ID(s) | Unique payment IDs for matching to Shopify Payments data. |

Multi-line-item orders: each line item is a separate row. Order-level fields (Name, Total, Taxes) are repeated on each row.

---

## Section 4 — Transaction Type Codes

### Shopify Payments CSV types

| Type | Meaning |
|------|---------|
| charge | Successful payment collected from customer |
| refund | Full or partial refund to customer |
| dispute | Chargeback initiated by cardholder |
| reserve_payout | Funds released from Shopify's reserve |
| adjustment | Manual adjustment by Shopify |
| payout | Transfer to merchant's bank account |

### Orders CSV Financial Status values

| Status | Meaning |
|--------|---------|
| paid | Fully paid |
| authorized | Card authorized but not captured |
| partially_paid | Deposit or partial payment received |
| partially_refunded | Some items refunded |
| refunded | Fully refunded |
| pending | Awaiting payment |
| voided | Authorization voided |

---

## Section 5 — Fee Structure

| Fee Type | Typical Rate | How It Appears |
|----------|-------------|----------------|
| Shopify Payments (online, domestic) | 2.9% + $0.30 (Basic), 2.6% + $0.30 (Shopify), 2.4% + $0.30 (Advanced) | Positive value in Fee column per charge row |
| Shopify Payments (in-person) | 2.7% + $0.00 (Basic), 2.5% + $0.00 (Shopify), 2.4% + $0.00 (Advanced) | Positive value in Fee column |
| International card surcharge | +1.5% | Added to base fee |
| Currency conversion fee | +1.5% | Added when customer currency ≠ store currency |
| Chargeback fee | $15 (US) | Separate charge on the dispute row |
| Third-party payment provider fee | 2% / 1% / 0.5% | Not in Payments CSV — billed separately by Shopify |
| Shopify subscription | $39–399/month | Not in transaction exports — billed to account |
| Refund fee | Processing fee NOT returned | Original Fee remains; no fee on refund row |

**Key: Fee is stored as a POSITIVE number.** Net = Amount - Fee. This is the opposite of PayPal where Fee is negative.

---

## Section 6 — Tax-Relevant Fields

| Field | Location | Notes |
|-------|----------|-------|
| Taxes | Orders CSV | Total tax on the order. Sum of all line-item taxes. |
| Lineitem taxable | Orders CSV | Whether tax was charged on this line item. |
| Billing Country | Orders CSV | Customer's country — critical for cross-border tax obligations. |
| Billing Province | Orders CSV | State/province for US/Canadian sales tax nexus. |
| Currency | Both CSVs | Tax jurisdiction may depend on the transaction currency. |
| Tax lines (not in CSV) | Shopify admin/API | Detailed tax breakdown by jurisdiction (available via API, not in standard CSV export). |

Shopify can be configured to collect taxes automatically based on product taxability and customer location. Tax amounts in the Orders CSV reflect what was actually charged. For detailed tax reporting by jurisdiction, use Shopify's Tax report in Finance > Reports, not the Orders CSV.

---

## Section 7 — Multi-Currency Handling

| Scenario | How It Appears |
|----------|---------------|
| Single-currency store | All transactions in one currency. Currency column is consistent. |
| Multi-currency store (Shopify Payments) | Amount and Fee are in the store's settlement (payout) currency. Customer may have paid in a different currency. |
| Customer-facing currency | Not visible in the Payments CSV. Available in the Orders CSV via Currency column. |
| Exchange rate | Not shown in CSV exports. Shopify converts at its own rate (includes 1.5% conversion fee). |
| International pricing | Shopify Markets may show different prices per country. The Orders CSV shows what the customer paid in their currency; the Payments CSV shows the settlement amount. |

---

## Section 8 — Reconciliation Tips

1. **Use the Payments CSV for bank reconciliation, not the Orders CSV.** The Payments CSV shows what actually moved to/from the bank. The Orders CSV shows what customers ordered, which is different due to timing, partial payments, and multi-tender orders.
2. **Match payouts to bank deposits.** Filter by Payout Date and sum Net amounts for each Payout ID. This total should match the bank deposit.
3. **Fee is POSITIVE.** Unlike PayPal/Stripe. Net = Amount - Fee. If Amount = 100 and Fee = 3.20, Net = 96.80.
4. **Refunds reduce payout amount.** Refunds in a payout period reduce the total deposited. A payout with $1000 in charges and $200 in refunds deposits $800 minus fees.
5. **"CSV for Excel" breaks imports.** Always export "Plain CSV". The Excel variant adds summary rows at the top.
6. **Multi-line orders in Orders CSV.** An order with 3 items has 3 rows. Total/Subtotal/Taxes are the same on each row — do not sum them or you'll triple-count.
7. **Gift cards are not revenue when sold.** Gift card purchases are a liability. Revenue is recognized when the gift card is redeemed. Shopify handles this differently in the Payments vs Orders export.

---

## Section 9 — Common Gotchas

1. **Orders CSV vs Payments CSV confusion.** Users often export from Orders instead of Finance > Payouts. The Orders CSV does not include processing fees and does not match bank deposits.
2. **Fee sign convention.** Shopify Fees are positive numbers (unusual). Most tools expect negative fees. When converting for QuickBooks import, negate the Fee values.
3. **Timestamp timezone offset.** Transaction Date includes timezone (e.g., -0500). If comparing to bank dates in a different timezone, convert first.
4. **Duplicate rows in Orders CSV.** Each line item is a row. Order-level amounts (Total, Taxes) repeat on every line-item row. Do not sum Totals across line-item rows for the same order.
5. **Partial refunds create new rows.** A partial refund appears as a new row in the Payments CSV with Type = refund. The original charge row is unchanged.
6. **Discount codes reduce Subtotal.** If a 20% discount is applied, Subtotal reflects the discounted price. The Discount Amount column shows the discount value for reference.
7. **POS vs online transactions.** In-person (POS) transactions use the same Payments CSV format but have different fee rates. Card Source distinguishes them (chip, contactless, swipe vs online).
8. **Shopify shipping labels.** If the merchant buys shipping labels through Shopify, these charges appear as deductions in the payout but are NOT in the Payments transaction CSV. Check the payout summary.

---

## Section 10 — Sample Data

### Shopify Payments CSV (Plain)

```csv
Transaction Date,Type,Order,Card Brand,Card Source,Payout Status,Payout Date,Available On,Amount,Fee,Net,Currency,Checkout,Payment Method,Payout ID
2026-03-15 14:23:45 -0500,charge,#1001,visa,online,paid,2026-03-17,2026-03-17,49.99,1.75,48.24,USD,abc123def456,shopify_payments,pay_1234
2026-03-15 16:10:00 -0500,charge,#1002,mastercard,online,paid,2026-03-17,2026-03-17,129.99,4.07,125.92,USD,ghi789jkl012,shopify_payments,pay_1234
2026-03-16 09:30:22 -0500,charge,#1003,amex,contactless,paid,2026-03-18,2026-03-18,24.99,1.03,23.96,USD,mno345pqr678,shopify_payments,pay_1235
2026-03-16 11:45:00 -0500,refund,#1001,visa,,paid,2026-03-18,2026-03-18,-49.99,0.00,-49.99,USD,,shopify_payments,pay_1235
2026-03-17 08:00:00 -0500,charge,#1004,visa,online,paid,2026-03-19,2026-03-19,299.00,8.97,290.03,USD,stu901vwx234,shopify_payments,pay_1236
2026-03-17 14:15:33 -0500,charge,#1005,mastercard,chip,paid,2026-03-19,2026-03-19,15.00,0.68,14.32,USD,yza567bcd890,shopify_payments,pay_1236
2026-03-18 10:00:00 -0500,dispute,#1002,mastercard,,pending,,,−129.99,15.00,−144.99,USD,,shopify_payments,
```

### Shopify Orders Export CSV (excerpt)

```csv
Name,Email,Financial Status,Paid at,Currency,Subtotal,Shipping,Taxes,Total,Discount Code,Discount Amount,Lineitem quantity,Lineitem name,Lineitem price,Lineitem sku,Payment Method
#1001,alice@example.com,paid,2026-03-15,USD,39.99,5.00,5.00,49.99,,,1,Wireless Mouse,39.99,WM-001,Shopify Payments
#1002,bob@example.com,paid,2026-03-15,USD,99.99,10.00,20.00,129.99,SAVE10,10.00,1,Mechanical Keyboard,99.99,KB-002,Shopify Payments
#1002,bob@example.com,paid,2026-03-15,USD,99.99,10.00,20.00,129.99,SAVE10,10.00,1,USB-C Hub,29.99,HUB-003,Shopify Payments
```

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.
