---
name: global-payment-processors
description: "Use the 2026 payment-processor classification and reconciliation method to investigate supplied transactions, reconcile supporting documents, distinguish fees and transfers and apply the actual country rules. Historical merchant strings are lookup hints, not current tax or integration certification."
version: 1.0
jurisdiction: GLOBAL
tax_year: 2026
last_updated: 2026-11-14
category: bookkeeping
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: bookkeeping
type: cross-country-method
checked_on: 2026-11-14
---

# Payment-processor classification and reconciliation v1.0

## Scope

Use the method for the actual entity, period, accounting basis and supported documents. Checked on 2026-11-14. No merchant brand, payment currency or bank narrative establishes a tax result by itself.

## Ask the client first

Obtain legal entity, country, reporting period, accounting framework and cash/accrual basis; platform account and legal contract; principal/agent/merchant-of-record role; customer invoices, sales tax, refunds, disputes, reserves, fee documents and all payout/activity statements. Determine which invoices/receivables are already booked, which accounts are owned by the client, currencies/rate policy and who paid any fee. A bank line alone cannot resolve these facts.

## The method, step by step

1. Identify what the specific entry represents. A payout, own transfer, supplier purchase, SaaS subscription, incorporation service, hardware purchase, loan or fee can share the same brand. Match actual IDs, direction, account owner, invoice and contract. A bank descriptor and debit/credit direction cannot establish deductibility, revenue or an incorporation-cost election.
2. Reconcile opening processor funds plus actual gross cash activity, refunds/reversals, taxes/third-party collections, fees, retained/released reserves and funding transfers to the closing balance and bank payout. Gross less fees equals payout only in the simple case with no other movements or unsettled balance. Do not estimate current fees from historical percentage pricing. Separate a bank payout from the commercial sale; match an existing receivable rather than booking sales twice. [HMRC accurate transaction records](https://www.gov.uk/self-employed-records/what-records-to-keep).
3. Decide the financial-reporting role from each actual contract/specified supply. Under an applicable AASB 15/IFRS-equivalent policy, test control before transfer, not merely who issues the customer invoice or calls itself MoR. Principal revenue and agent commission differ; transaction price excludes amounts collected on behalf of others. A contract may contain more than one role. Net cash received is not automatically revenue, and a platform fee may still need separate treatment. [AASB 15 paragraphs 47,B34-B38](https://standards.aasb.gov.au/sites/default/files/2026-11/AASB15_12-14_COMPdec22_07-26.pdf).
4. Resolve VAT/GST/sales tax separately for the customer's supply, the client's supply to a reseller/MoR, and the platform's fee. An MoR handling retail tax does not mean the client has no VAT reporting or fee expense. UK VAT Notice 700 sections 22.1-22.6 distinguishes actual agency, separate agent/principal supplies and own-name agents; another jurisdiction needs its own law. Notice 741A supplies the UK cross-border-service conditions, not an all-country exemption. [Notice 700](https://www.gov.uk/guidance/vat-guide-notice-700); [Notice 741A](https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a).
5. Treat fees only when evidenced and economically borne by the client. Distinguish processor commissions, subscription, direct-debit service, card-reader hardware, incorporation/legal/start-up costs, connected-platform charges and supplier purchases collected through a platform. UK business financial charges have specific eligible-cost rules; loan principal is not one. Other countries and capital costs need their owning methods. [HMRC financial costs](https://www.gov.uk/expenses-if-youre-self-employed/legal-financial).
6. Pair owned transfers and conversion legs, retain each currency, document direction/units/rates and separate any genuine settlement difference. Under an applicable AASB 121 policy, translate initial recognition at the appropriate transaction-date rate and monetary balances/settlement as required; do not universally declare every difference taxable/deductible or every FX spread a fee. A sender-borne fee is not a recipient's expense merely because its amount appears in transfer details. [AASB 121 paragraphs 21-23,27-30](https://standards.aasb.gov.au/sites/default/files/2025-03/AASB121_08-15_COMPoct23_01-25.pdf).
7. Produce the source-linked commercial entry, fee/tax/clearing/FX workpapers and payout reconciliation, with duplicate controls and unresolved differences. If the ledger is read-only, output proposed postings or an import file for human approval. Do not silently post a reconciliation difference or call a payout-only reconstruction complete. Detailed supplied-file parsers are in the assigned brand integration methods; this lookup does not certify a live schema.

## Processor-specific investigation jobs

- Stripe standard/Connect/Billing: separate a merchant's customer receipts from platform-to-seller contracts and own-account settlement. Atlas is an incorporation/legal-service investigation, not a card fee. Pricing and capitalisation depend on actual documents and country rules.
- PayPal transfer versus merchant purchase versus receipt versus ambiguous PP reference: trace the underlying event; a purchase can be private, capital, a refund or liability settlement. Own-account transfers do not create income. Keep actual fee cells and separate fee rows.
- Wise currency conversions and transfers: distinguish receipt against an existing invoice, owned balance transfer, supplier payment and client-paid versus sender-paid charge. Do not assume every incoming Wise amount is a sale or every fee is a separate row.
- Square, SumUp and iZettle/Zettle: reconcile card activity/fees/refunds/payout; separate hardware and subscriptions from settlement. Exact ownership, current prices and fee-return policies are unconfirmed.
- Revolut: owned transfers, supplier card purchases, business/private plans and actual account/service charges require distinct evidence. A Premium/Metal narrative does not prove a business subscription.
- GoCardless: distinguish collections for the client from a vendor's direct debit taken from the client. Link customer invoices or supplier bills before posting.
- Paddle, Gumroad and LemonSqueezy: examine the actual MoR/reseller/agency contract and client's own supply. Do not use the old universal net-revenue/no-fee/no-VAT instruction. Retail tax collection does not settle every client obligation.
- Shopify Payments, Amazon Pay, Klarna, Adyen and Mollie: retain gross activity, refund/fee/reserve and bank links. Buy-now-pay-later payment timing does not alone establish revenue recognition or release of customer credit risk; test contract/performance under the applicable policy.

## When to refuse or refer

Hold missing commercial agreements, complete activity reports, unconfirmed gross/fee units, mixed currencies, reserve balances, client fee responsibility or payout gaps. No automatic gross-up from a bank line, MoR netting, universal input VAT deduction or current vendor price is supplied. Refer complex platform principal/agent, connected funds, related-party, withholding or cross-border tax treatment to its country/framework method.

## Worked cases

### Stripe, supported principal receipts

The old three invoices provide gross USD 2,500/1,800/575, actual fees 75.30/54.60/23.60 and net 2,424.70/1,745.40/551.40. Total gross 4,875 less fees 153.50 equals payout 4,721.50. If the invoices were already recognised, the commercial receipt clears receivables rather than recreating revenue. On the simple assumed same-period/no-other-adjustments facts, booking net only understates gross sales and expenses equally; it does not automatically overstate taxable profit by 153.50.

```oa-check
name: Stripe gross and fees, no invented phantom profit
inputs:
  client_a: 2500
  client_b: 1800
  client_c: 575
  fee_a: 75.3
  fee_b: 54.6
  fee_c: 23.6
steps:
  - gross: client_a + client_b + client_c
  - fees: fee_a + fee_b + fee_c
  - payout: gross - fees
  - profit_if_net_only: payout
  - profit_if_gross_less_fees: gross - fees
expected:
  gross: 4875
  fees: 153.5
  payout: 4721.5
  profit_if_net_only: 4721.5
  profit_if_gross_less_fees: 4721.5
```

### PayPal, explicit signed fees and conversion charge

The old report supplies EUR 1,000 and 950 receipts, fees 29.20 and 27.85 and an additional documented EUR 2.95 charge. Net payout is EUR 1,890. Keep the fee amounts as supplied assumptions, not a current PayPal price or evidence of universal VAT exemption.

```oa-check
name: PayPal report to bank bridge
inputs:
  one: 1000
  two: 950
  fee_one: 29.2
  fee_two: 27.85
  fx_charge: 2.95
steps:
  - gross: one + two
  - payment_fees: fee_one + fee_two
  - payout: gross - payment_fees - fx_charge
expected:
  gross: 1950
  payment_fees: 57.05
  payout: 1890
```

### Paddle, unresolved report versus bank

Retain the old supplied customer gross 1,200/1,500/1,100, stated tax 228/0/220 and fees 60/75/55 as report facts, not computed country VAT or certified current fees. Their net is USD 3,162, while the bank is USD 3,200. The unexplained USD 38 blocks the old proposed bank entry for 3,162. Do not invent income or post a mismatching bank amount. Neither this arithmetic nor the brand proves principal/agent or eliminates the client's own VAT reporting.

```oa-check
name: MoR arithmetic does not authorise a mismatching journal
inputs:
  gross_de: 1200
  gross_us: 1500
  gross_uk: 1100
  stated_tax_de: 228
  stated_tax_uk: 220
  fee_de: 60
  fee_us: 75
  fee_uk: 55
  bank: 3200
steps:
  - gross: gross_de + gross_us + gross_uk
  - tax_collections: stated_tax_de + stated_tax_uk
  - fees: fee_de + fee_us + fee_uk
  - report_net: gross - tax_collections - fees
  - unresolved_bank_gap: bank - report_net
expected:
  gross: 3800
  tax_collections: 448
  fees: 190
  report_net: 3162
  unresolved_bank_gap: 38
```

### Wise, rate direction and fee bearer

For the supplied USD 10,000 receipt and quotation1GBP=1.2739USD, division gives GBP 7,849.91 to two decimals, not the old GBP 7,850.03. The stated bank amount GBP 7,850 differs by GBP 0.09 from that rounded ratio; obtain the actual settlement calculation instead of naming it a fee. If the recipient rather than sender bore a separately evidenced USD 45 charge, the dollar amount after that charge would be9,955, but its sterling settlement must still come from the actual contract/rate. Invoice recognition and genuine FX settlement differences remain separate.

```oa-check
name: Wise supplied quotation and rounding control
inputs:
  usd: 10000
  usd_per_gbp: 1.2739
  bank_gbp: 7850
  recipient_fee_usd: 45
steps:
  - quoted_gbp: round(usd / usd_per_gbp, 2)
  - quoted_bank_gap: bank_gbp - quoted_gbp
  - recipient_net_usd: usd - recipient_fee_usd
expected:
  quoted_gbp: 7849.91
  quoted_bank_gap: 0.09
  recipient_net_usd: 9955
```

## Historical recognition hints

These are search candidates from the old library, not verified current merchant identities, fees or tax rules. Confirm the invoice, account and transaction before selecting an account.
- **Stripe**; candidate statement text `STRIPE PAYMENTS`, `STRIPE TRANSFER`, `STRIPE PAYOUT`. Investigate the actual purpose and direction.
- **Stripe**; candidate statement text `STRIPE CONNECT`. Investigate the actual purpose and direction.
- **Stripe**; candidate statement text `STRIPE ATLAS`. Investigate the actual purpose and direction.
- **Stripe**; candidate statement text `STRIPE *INVOICE`, `STRIPE BILLING`. Investigate the actual purpose and direction.
- **PayPal**; candidate statement text `PAYPAL TRANSFER`, `PAYPAL INST XFER`. Investigate the actual purpose and direction.
- **PayPal**; candidate statement text `PAYPAL *[MERCHANT]`. Investigate the actual purpose and direction.
- **PayPal**; candidate statement text `PAYPAL PAYMENT`. Investigate the actual purpose and direction.
- **PayPal**; candidate statement text `PP*[CODE]`. Investigate the actual purpose and direction.
- **Wise**; candidate statement text `WISE`, `TRANSFERWISE`. Investigate the actual purpose and direction.
- **Wise**; candidate statement text `WISE *FEE`, `TRANSFERWISE FEE`. Investigate the actual purpose and direction.
- **Wise**; candidate statement text `WISE CURRENCY`. Investigate the actual purpose and direction.
- **Square**; candidate statement text `SQ *`, `SQUARE`, `SQUAREUP`. Investigate the actual purpose and direction.
- **Square**; candidate statement text `SQUARE HARDWARE`. Investigate the actual purpose and direction.
- **SumUp**; candidate statement text `SUMUP`, `SUMUP *`. Investigate the actual purpose and direction.
- **iZettle**; candidate statement text `IZETTLE`, `ZETTLE`, `PAYPAL ZETTLE`. Investigate the actual purpose and direction.
- **Revolut Business**; candidate statement text `REVOLUT`, `REVOLUT *`. Investigate the actual purpose and direction.
- **Revolut Business**; candidate statement text `REVOLUT *PREMIUM`, `REVOLUT *METAL`. Investigate the actual purpose and direction.
- **GoCardless**; candidate statement text `GOCARDLESS`, `GOCARDLESS LTD`. Investigate the actual purpose and direction.
- **GoCardless**; candidate statement text `GOCARDLESS *[CLIENT]`. Investigate the actual purpose and direction.
- **Paddle**; candidate statement text `PADDLE.NET`, `PADDLE COM`. Investigate the actual purpose and direction.
- **Gumroad**; candidate statement text `GUMROAD`, `GUMROAD INC`. Investigate the actual purpose and direction.
- **LemonSqueezy**; candidate statement text `LEMONSQUEEZY`, `LEMON SQUEEZY`, `LMSQUEEZY`. Investigate the actual purpose and direction.
- **Shopify Payments**; candidate statement text `SHOPIFY *PAYMT`, `SHOPIFY PAYOUT`. Investigate the actual purpose and direction.
- **Amazon Pay**; candidate statement text `AMZN *PAY`, `AMAZON PAY`. Investigate the actual purpose and direction.
- **Klarna**; candidate statement text `KLARNA`, `KLARNA AB`. Investigate the actual purpose and direction.
- **Adyen**; candidate statement text `ADYEN`, `ADYEN N.V.`. Investigate the actual purpose and direction.
- **Mollie**; candidate statement text `MOLLIE`, `MOLLIE B.V.`. Investigate the actual purpose and direction.

## Existing review requirement

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Sources

| Official source | Read on | Read scope |
|---|---|---|
| https://www.gov.uk/self-employed-records/what-records-to-keep | 2026-11-14 | Read for sales/expense proof, accurate records, distinguishing business transactions and accrual records. |
| https://www.gov.uk/expenses-if-youre-self-employed/legal-financial | 2026-11-14 | Read for eligible UK business financial charges, non-deductible loan principal and bad-debt distinction by accounting basis. |
| https://www.gov.uk/guidance/vat-guide-notice-700 | 2026-11-14 | Read for Notice 700 sections 22.1-22.6 for actual agency, separate underlying/agent supplies and own-name agents. |
| https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a | 2026-11-14 | Read for sections 2-6 and 13, actual supply, belonging, reverse-charge conditions, input-tax limits and unregistered recipients. |
| https://standards.aasb.gov.au/sites/default/files/2026-11/AASB15_12-14_COMPdec22_07-26.pdf | 2026-11-14 | Read for paragraphs 47 and 105-108,B34-B38,B44-B47 for third-party collections, contracts, principal-agent control and unexercised rights; conditional reporting scope. |
| https://standards.aasb.gov.au/sites/default/files/2025-03/AASB121_08-15_COMPoct23_01-25.pdf | 2026-11-14 | Read for paragraphs 20-23 and 27-30, initial recognition, monetary closing balances and settlement exchange differences; Australian IFRS-equivalent financial reporting, not universal tax translation. |

Not yet confirmed: Vendor-specific MoR/reseller contracts, current fee tables, legal billing entities, settlement timings and country deductions/tax returns cannot be inferred from a descriptor. The historical examples are supplied-data controls, not certification of country tax rates or current platform terms.  Current platform billing identities, prices, plans, live descriptors and automatic tax arrangements are not certified. Old row claims below are historical comparison only, not usable tax or fee guidance. No vendor source was used.

- Historical claim, not usable guidance, **Stripe**: What it IS: Net payout after Stripe fees (typically 2.9% + 30c per transaction, varies by country/product); What it is NOT: NOT gross revenue. NOT a Stripe subscription fee.; Classification rule: Book gross revenue from Stripe dashboard. Book Stripe fees as "Bank charges / Payment processing fees". The bank deposit is merely the settlement.
- Historical claim, not usable guidance, **Stripe**: What it IS: Payout from a Stripe Connect platform (e.g., marketplace payout); What it is NOT: NOT revenue from YOUR customers. The platform is paying you.; Classification rule: Revenue = payout + platform fees withheld. Check platform dashboard for gross amounts.
- Historical claim, not usable guidance, **Stripe**: What it IS: Stripe Atlas incorporation service fee ($500 one-time + optional ongoing); What it is NOT: NOT a payment processing charge.; Classification rule: One-time: Capitalize as incorporation cost or expense as startup cost. Ongoing: Office expenses / Legal services.
- Historical claim, not usable guidance, **Stripe**: What it IS: Stripe's invoicing/billing product collecting payment on your behalf; What it is NOT: NOT revenue , same net-payout rule applies.; Classification rule: Same as standard Stripe payout rule.
- Historical claim, not usable guidance, **PayPal**: What it IS: Net payout from PayPal balance to bank account; What it is NOT: NOT revenue. This is a transfer between your own accounts.; Classification rule: The revenue was already recorded when the customer paid into your PayPal account. This transfer is a balance movement, not income.
- Historical claim, not usable guidance, **PayPal**: What it IS: Payment TO a merchant via PayPal (expense); What it is NOT: NOT revenue. NOT a PayPal fee.; Classification rule: Classify based on the merchant name after the asterisk. This is an expense paid via PayPal.
- Historical claim, not usable guidance, **PayPal**: What it IS: A payment received via PayPal (shows on PayPal statement, not always on bank); What it is NOT: The net amount (after PayPal's fee of ~2.9% + fixed).; Classification rule: Gross revenue = net received + PayPal fee. Obtain PayPal transaction report for exact fee breakdown.
- Historical claim, not usable guidance, **PayPal**: What it IS: PayPal charge , could be incoming or outgoing; What it is NOT: Ambiguous , must check direction and reference.; Classification rule: Check debit/credit. If debit: expense. If credit: net payout (not revenue).
- Historical claim, not usable guidance, **Wise**: What it IS: Currency conversion / international transfer; What it is NOT: NOT revenue. NOT an expense (unless the Wise fee itself).; Classification rule: If sending money: the transfer is a payment for an expense (classify the underlying expense). If receiving: it is a client payment arriving via Wise. The Wise fee is a separate deductible "Bank charges / FX fees" expense.
- Historical claim, not usable guidance, **Wise**: What it IS: Wise's transfer fee; What it is NOT: NOT the transfer amount itself.; Classification rule: Deductible as "Bank charges / Transfer fees".
- Historical claim, not usable guidance, **Wise**: What it IS: FX conversion within Wise multi-currency account; What it is NOT: NOT revenue or expense. It is a balance conversion.; Classification rule: Book the FX gain/loss. The conversion itself is not income or expense , only the exchange rate difference matters.
- Historical claim, not usable guidance, **Square**: What it IS: Net payout from Square card reader; What it is NOT: NOT gross revenue.; Classification rule: Same pattern as Stripe. Gross revenue = payout + Square processing fee (typically 2.6% + 10c US). Obtain Square dashboard report.
- Historical claim, not usable guidance, **Square**: What it IS: Purchase of Square card reader hardware; What it is NOT: NOT a payment processing fee.; Classification rule: Capitalize as equipment (if material) or expense as office supplies.
- Historical claim, not usable guidance, **SumUp**: What it IS: Net payout from SumUp card reader; What it is NOT: NOT gross revenue.; Classification rule: Same pattern. SumUp fee varies by country (1.69% EU typical). Check SumUp dashboard.
- Historical claim, not usable guidance, **iZettle**: What it IS: Net payout from Zettle (now PayPal Zettle) card reader; What it is NOT: NOT gross revenue.; Classification rule: Same pattern. Now owned by PayPal. Fee typically 1.75% EU.
- Historical claim, not usable guidance, **Revolut Business**: What it IS: Transfer between Revolut and external bank, or Revolut account fee; What it is NOT: NOT revenue. NOT an expense (unless it is the account fee).; Classification rule: If a transfer to/from your own account: ignore for P&L (balance movement). If a fee: "Bank charges". If a payment to a supplier: classify by supplier.
- Historical claim, not usable guidance, **Revolut Business**: What it IS: Revolut subscription fee; What it is NOT: NOT a transfer.; Classification rule: "Bank charges / Account fees". Verify business vs. personal plan.
- Historical claim, not usable guidance, **GoCardless**: What it IS: Direct debit collection payout; What it is NOT: NOT gross revenue. GoCardless deducts its fee before payout.; Classification rule: Gross revenue = payout + GoCardless fees (1% + 20p typical UK). Obtain GoCardless report.
- Historical claim, not usable guidance, **GoCardless**: What it IS: A direct debit payment collected FROM you by a vendor using GoCardless; What it is NOT: This is an EXPENSE, not revenue.; Classification rule: Classify based on the vendor name. Common for recurring SaaS bills collected via DD.
- Historical claim, not usable guidance, **Paddle**: What it IS: Payout from Paddle as Merchant of Record (MoR); What it is NOT: NOT your gross revenue. Paddle invoiced the customer, not you. YOUR revenue is the net payout from Paddle.; Classification rule: Paddle is the legal seller. They handle VAT, refunds, chargebacks. Your revenue = Paddle payout. Paddle's cut includes their fee + taxes they remitted. Do NOT also record the customer's gross payment as your revenue.
- Historical claim, not usable guidance, **Gumroad**: What it IS: Payout from Gumroad as MoR; What it is NOT: NOT your gross revenue. Same MoR pattern as Paddle.; Classification rule: Revenue = Gumroad payout. Gumroad handles sales tax/VAT and takes their commission.
- Historical claim, not usable guidance, **LemonSqueezy**: What it IS: Payout from LemonSqueezy as MoR; What it is NOT: NOT your gross revenue. Same MoR pattern.; Classification rule: Revenue = LemonSqueezy payout. They handle all tax obligations as MoR.
- Historical claim, not usable guidance, **Shopify Payments**: What it IS: Net payout from Shopify Payments; What it is NOT: NOT gross revenue.; Classification rule: Same as Stripe pattern. Shopify Payments fee is separate. Note: Shopify subscription fee is a different charge (SaaS expense).
- Historical claim, not usable guidance, **Amazon Pay**: What it IS: Payout from Amazon Pay; What it is NOT: NOT gross revenue.; Classification rule: Revenue = payout + Amazon Pay fees.
- Historical claim, not usable guidance, **Klarna**: What it IS: Payout from Klarna (buy-now-pay-later); What it is NOT: NOT gross revenue. Klarna pays you in full (minus fee) even though customer pays in installments.; Classification rule: Revenue = Klarna payout + Klarna merchant fee. You recognize full revenue at sale, not when customer completes installments.
- Historical claim, not usable guidance, **Adyen**: What it IS: Payout from Adyen payment platform; What it is NOT: NOT gross revenue.; Classification rule: Same net-payout pattern. Adyen fees deducted.
- Historical claim, not usable guidance, **Mollie**: What it IS: Payout from Mollie payment platform; What it is NOT: NOT gross revenue.; Classification rule: Same pattern. Common in NL/EU.
