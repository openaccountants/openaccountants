---
name: global-payment-processors
description: >
  Classification rules for payment processor transactions — the number one source of
  bank statement classification errors. Covers Stripe, PayPal, Wise, Square, SumUp,
  iZettle, Revolut, GoCardless, Paddle, Gumroad, and LemonSqueezy with worked examples
  for reconstructing gross revenue from net payouts.
version: 0.1
category: patterns
depends_on: []
---

# Global Payment Processor Pattern Library v0.1

## What this file is

**Functional role:** Transaction classification rules for payment processor entries
**Status:** Active reference data

Payment processor transactions are the single largest source of classification errors in freelancer bookkeeping. The core problem: **a payout from Stripe/PayPal/etc. is NOT your revenue. It is your revenue MINUS their fees.** If you book the payout as revenue, you understate revenue AND miss a deductible expense.

This file provides deterministic rules for every major payment processor, explains what each transaction type actually represents, and includes worked examples for reconstructing the correct accounting entries.

---

## The golden rule

> **Bank deposit from a payment processor = Net payout = Gross revenue - Processing fees**
>
> You must record:
> 1. **Gross revenue** (what the customer paid)
> 2. **Processing fee** (deductible expense)
> 3. **Net payout** (what hit your bank — this is NOT a revenue figure)
>
> If you only have the bank statement (no processor dashboard), you are missing data. You MUST obtain the processor's transaction report to book correctly.

---

## Processor lookup table

| Processor | Bank statement text | What it IS | What it is NOT | Classification rule |
|---|---|---|---|---|
| **Stripe** | `STRIPE PAYMENTS`, `STRIPE TRANSFER`, `STRIPE PAYOUT` | Net payout after Stripe fees (typically 2.9% + 30c per transaction, varies by country/product) | NOT gross revenue. NOT a Stripe subscription fee. | Book gross revenue from Stripe dashboard. Book Stripe fees as "Bank charges / Payment processing fees". The bank deposit is merely the settlement. |
| **Stripe** | `STRIPE CONNECT` | Payout from a Stripe Connect platform (e.g., marketplace payout) | NOT revenue from YOUR customers. The platform is paying you. | Revenue = payout + platform fees withheld. Check platform dashboard for gross amounts. |
| **Stripe** | `STRIPE ATLAS` | Stripe Atlas incorporation service fee ($500 one-time + optional ongoing) | NOT a payment processing charge. | One-time: Capitalize as incorporation cost or expense as startup cost. Ongoing: Office expenses / Legal services. |
| **Stripe** | `STRIPE *INVOICE`, `STRIPE BILLING` | Stripe's invoicing/billing product collecting payment on your behalf | NOT revenue — same net-payout rule applies. | Same as standard Stripe payout rule. |
| **PayPal** | `PAYPAL TRANSFER`, `PAYPAL INST XFER` | Net payout from PayPal balance to bank account | NOT revenue. This is a transfer between your own accounts. | The revenue was already recorded when the customer paid into your PayPal account. This transfer is a balance movement, not income. |
| **PayPal** | `PAYPAL *[MERCHANT]` | Payment TO a merchant via PayPal (expense) | NOT revenue. NOT a PayPal fee. | Classify based on the merchant name after the asterisk. This is an expense paid via PayPal. |
| **PayPal** | `PAYPAL PAYMENT` | A payment received via PayPal (shows on PayPal statement, not always on bank) | The net amount (after PayPal's fee of ~2.9% + fixed). | Gross revenue = net received + PayPal fee. Obtain PayPal transaction report for exact fee breakdown. |
| **PayPal** | `PP*[CODE]` | PayPal charge — could be incoming or outgoing | Ambiguous — must check direction and reference. | Check debit/credit. If debit: expense. If credit: net payout (not revenue). |
| **Wise** | `WISE`, `TRANSFERWISE` | Currency conversion / international transfer | NOT revenue. NOT an expense (unless the Wise fee itself). | If sending money: the transfer is a payment for an expense (classify the underlying expense). If receiving: it is a client payment arriving via Wise. The Wise fee is a separate deductible "Bank charges / FX fees" expense. |
| **Wise** | `WISE *FEE`, `TRANSFERWISE FEE` | Wise's transfer fee | NOT the transfer amount itself. | Deductible as "Bank charges / Transfer fees". |
| **Wise** | `WISE CURRENCY` | FX conversion within Wise multi-currency account | NOT revenue or expense. It is a balance conversion. | Book the FX gain/loss. The conversion itself is not income or expense — only the exchange rate difference matters. |
| **Square** | `SQ *`, `SQUARE`, `SQUAREUP` | Net payout from Square card reader | NOT gross revenue. | Same pattern as Stripe. Gross revenue = payout + Square processing fee (typically 2.6% + 10c US). Obtain Square dashboard report. |
| **Square** | `SQUARE HARDWARE` | Purchase of Square card reader hardware | NOT a payment processing fee. | Capitalize as equipment (if material) or expense as office supplies. |
| **SumUp** | `SUMUP`, `SUMUP *` | Net payout from SumUp card reader | NOT gross revenue. | Same pattern. SumUp fee varies by country (1.69% EU typical). Check SumUp dashboard. |
| **iZettle** | `IZETTLE`, `ZETTLE`, `PAYPAL ZETTLE` | Net payout from Zettle (now PayPal Zettle) card reader | NOT gross revenue. | Same pattern. Now owned by PayPal. Fee typically 1.75% EU. |
| **Revolut Business** | `REVOLUT`, `REVOLUT *` | Transfer between Revolut and external bank, or Revolut account fee | NOT revenue. NOT an expense (unless it is the account fee). | If a transfer to/from your own account: ignore for P&L (balance movement). If a fee: "Bank charges". If a payment to a supplier: classify by supplier. |
| **Revolut Business** | `REVOLUT *PREMIUM`, `REVOLUT *METAL` | Revolut subscription fee | NOT a transfer. | "Bank charges / Account fees". Verify business vs. personal plan. |
| **GoCardless** | `GOCARDLESS`, `GOCARDLESS LTD` | Direct debit collection payout | NOT gross revenue. GoCardless deducts its fee before payout. | Gross revenue = payout + GoCardless fees (1% + 20p typical UK). Obtain GoCardless report. |
| **GoCardless** | `GOCARDLESS *[CLIENT]` | A direct debit payment collected FROM you by a vendor using GoCardless | This is an EXPENSE, not revenue. | Classify based on the vendor name. Common for recurring SaaS bills collected via DD. |
| **Paddle** | `PADDLE.NET`, `PADDLE COM` | Payout from Paddle as Merchant of Record (MoR) | NOT your gross revenue. Paddle invoiced the customer, not you. YOUR revenue is the net payout from Paddle. | Paddle is the legal seller. They handle VAT, refunds, chargebacks. Your revenue = Paddle payout. Paddle's cut includes their fee + taxes they remitted. Do NOT also record the customer's gross payment as your revenue. |
| **Gumroad** | `GUMROAD`, `GUMROAD INC` | Payout from Gumroad as MoR | NOT your gross revenue. Same MoR pattern as Paddle. | Revenue = Gumroad payout. Gumroad handles sales tax/VAT and takes their commission. |
| **LemonSqueezy** | `LEMONSQUEEZY`, `LEMON SQUEEZY`, `LMSQUEEZY` | Payout from LemonSqueezy as MoR | NOT your gross revenue. Same MoR pattern. | Revenue = LemonSqueezy payout. They handle all tax obligations as MoR. |
| **Shopify Payments** | `SHOPIFY *PAYMT`, `SHOPIFY PAYOUT` | Net payout from Shopify Payments | NOT gross revenue. | Same as Stripe pattern. Shopify Payments fee is separate. Note: Shopify subscription fee is a different charge (SaaS expense). |
| **Amazon Pay** | `AMZN *PAY`, `AMAZON PAY` | Payout from Amazon Pay | NOT gross revenue. | Revenue = payout + Amazon Pay fees. |
| **Klarna** | `KLARNA`, `KLARNA AB` | Payout from Klarna (buy-now-pay-later) | NOT gross revenue. Klarna pays you in full (minus fee) even though customer pays in installments. | Revenue = Klarna payout + Klarna merchant fee. You recognize full revenue at sale, not when customer completes installments. |
| **Adyen** | `ADYEN`, `ADYEN N.V.` | Payout from Adyen payment platform | NOT gross revenue. | Same net-payout pattern. Adyen fees deducted. |
| **Mollie** | `MOLLIE`, `MOLLIE B.V.` | Payout from Mollie payment platform | NOT gross revenue. | Same pattern. Common in NL/EU. |

---

## Worked examples

### Example 1: Stripe payout reconstruction

**Bank statement shows:**
```
2025-03-15  STRIPE TRANSFER  +$4,721.50
```

**Stripe dashboard shows for the same payout period:**

| Customer | Gross amount | Stripe fee | Net |
|---|---|---|---|
| Client A invoice #42 | $2,500.00 | $75.30 | $2,424.70 |
| Client B invoice #18 | $1,800.00 | $54.60 | $1,745.40 |
| Client C invoice #7 | $575.00 | $23.60 | $551.40 |
| **Total** | **$4,875.00** | **$153.50** | **$4,721.50** |

**Correct bookkeeping entries:**

| Date | Account | Debit | Credit | Description |
|---|---|---|---|---|
| 2025-03-15 | Revenue | | $4,875.00 | Gross client payments (3 invoices) |
| 2025-03-15 | Bank charges - Processing fees | $153.50 | | Stripe processing fees |
| 2025-03-15 | Bank (checking) | $4,721.50 | | Stripe payout received |

**WRONG approach (common error):**

| Date | Account | Debit | Credit |
|---|---|---|---|
| 2025-03-15 | Revenue | | $4,721.50 |
| 2025-03-15 | Bank (checking) | $4,721.50 | |

This understates revenue by $153.50 AND misses $153.50 in deductible expenses. The tax impact compounds: the missed deduction means the freelancer overpays tax on $153.50 of phantom income.

---

### Example 2: PayPal with embedded fees

**Bank statement shows:**
```
2025-04-01  PAYPAL INST XFER  +EUR 1,890.00
```

**PayPal transaction report shows:**

| Date | Type | Gross | Fee | Net |
|---|---|---|---|---|
| 2025-03-28 | Payment received | EUR 1,000.00 | -EUR 29.20 | EUR 970.80 |
| 2025-03-29 | Payment received | EUR 950.00 | -EUR 27.85 | EUR 922.15 |
| **Subtotal** | | **EUR 1,950.00** | **-EUR 57.05** | **EUR 1,892.95** |
| 2025-03-30 | Currency conversion fee | | -EUR 2.95 | -EUR 2.95 |
| **Transfer total** | | | | **EUR 1,890.00** |

**Correct entries:**

| Date | Account | Debit | Credit |
|---|---|---|---|
| 2025-04-01 | Revenue | | EUR 1,950.00 |
| 2025-04-01 | Bank charges - PayPal fees | EUR 57.05 | |
| 2025-04-01 | Bank charges - FX fees | EUR 2.95 | |
| 2025-04-01 | Bank (checking) | EUR 1,890.00 | |

---

### Example 3: Paddle as Merchant of Record

**Bank statement shows:**
```
2025-05-10  PADDLE.NET  +$3,200.00
```

**Paddle dashboard shows:**

| Customer | Country | Gross sale | VAT collected | Paddle fee (5%) | Net to you |
|---|---|---|---|---|---|
| Customer DE | Germany | $1,200.00 | $228.00 | $60.00 | $912.00 |
| Customer US | USA | $1,500.00 | $0.00 | $75.00 | $1,425.00 |
| Customer UK | UK | $1,100.00 | $220.00 | $55.00 | $825.00 |
| **Total** | | **$3,800.00** | **$448.00** | **$190.00** | **$3,162.00** |

Wait — the bank shows $3,200.00 but the table shows $3,162.00? Check if Paddle bundles multiple payouts or if there is a timing difference. Always reconcile.

**Key difference from Stripe/PayPal:** Paddle is the Merchant of Record. Paddle invoiced the customers, collected VAT, and remitted it. YOU do not report the $3,800 gross or the $448 VAT. Your revenue is the $3,162 payout. Paddle's fee is already deducted — you do NOT separately claim a Paddle fee expense.

**Correct entries:**

| Date | Account | Debit | Credit |
|---|---|---|---|
| 2025-05-10 | Revenue | | $3,162.00 |
| 2025-05-10 | Bank (checking) | $3,162.00 | |

That is it. No fee expense. No VAT. Paddle handled everything.

---

### Example 4: Wise international transfer with FX

**Bank statement shows:**
```
2025-06-01  WISE  +GBP 7,850.00
```

**Wise transfer details:**

| Field | Value |
|---|---|
| Client paid | USD 10,000.00 |
| Exchange rate | 1 GBP = 1.2739 USD |
| GBP equivalent at mid-market rate | GBP 7,850.03 |
| Wise fee (paid by sender) | USD 45.00 |
| Amount received | GBP 7,850.00 |

**If the client paid the Wise fee:** Your revenue is USD 10,000.00 (or GBP equivalent at invoice date rate). The Wise fee is the client's cost, not yours. Book revenue at the invoiced amount and any FX gain/loss between invoice date rate and settlement date rate.

**If you paid the Wise fee:** Revenue = USD 10,000.00. Wise fee = USD 45.00 (deductible as bank charges). Net received = USD 9,955.00 equivalent.

---

## Merchant of Record vs. Payment Processor — critical distinction

| | Payment Processor (Stripe, PayPal, Square) | Merchant of Record (Paddle, Gumroad, LemonSqueezy) |
|---|---|---|
| **Who invoices the customer?** | YOU do | THEY do |
| **Who collects sales tax/VAT?** | YOU must | THEY handle it |
| **Who handles refunds/chargebacks?** | YOU handle them, they process | THEY handle everything |
| **Your gross revenue** | Customer's full payment amount | The net payout you receive |
| **Fee treatment** | Separate deductible expense | Already deducted from your payout — do NOT double-deduct |
| **VAT on your sales** | You report and remit | MoR reports and remits — you do NOT include in your VAT return |
| **Your invoice** | Issued to customer | Issued to the MoR (or not needed — check your contract) |

---

## Common mistakes

1. **Booking net payouts as gross revenue.** This is the most common error. It understates revenue AND misses deductible fees. The net tax effect can be zero in simple cases, but it corrupts financial statements and can trigger issues if audited.

2. **Double-counting MoR revenue.** If Paddle/Gumroad pays you $3,000 and you ALSO record the customer's $3,500 gross payment as revenue, you have double-counted. The MoR already invoiced the customer.

3. **Missing the VAT obligation.** When using a payment processor (not MoR), YOU are responsible for collecting and remitting VAT/sales tax. When using an MoR, they handle it. Confusing the two creates VAT compliance failures.

4. **Treating inter-account transfers as income.** Moving money from PayPal to your bank account is NOT income. The income occurred when the customer paid. The transfer is just a balance movement.

5. **Ignoring FX gains/losses.** When you invoice in USD but receive in EUR (via Wise, PayPal, etc.), the exchange rate difference between invoice date and settlement date creates a taxable FX gain or deductible FX loss. This must be recorded.

6. **Not reconciling to processor reports.** Bank statements alone are insufficient for correct payment processor accounting. You MUST obtain and reconcile against the processor's own transaction reports (Stripe dashboard, PayPal activity download, etc.).

---

## Disclaimer

This file provides general guidance for classifying payment processor transactions. Processing fees, payout schedules, and MoR arrangements change frequently. Always verify against the processor's actual reports and invoices. This is not tax advice. A qualified professional should review all classifications before filing.
