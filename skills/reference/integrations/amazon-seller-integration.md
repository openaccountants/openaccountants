---
name: amazon-seller-integration
version: 1.0
category: integration
description: >
  Integration skill for Amazon Seller Central settlement reports and date range reports. Activate when the user
  uploads an Amazon settlement report, Amazon seller CSV, or mentions Amazon Seller Central, FBA, or Amazon payouts.
jurisdiction: GLOBAL
tier: 2
last_updated: 2026-06-12
---

# Amazon Seller Central Integration Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Section 1 — Platform Overview

Amazon Seller Central is the platform used by third-party sellers on Amazon's marketplace. It handles product listings, order management, fulfilment (FBA or FBM), advertising, and financial settlements. Amazon operates marketplaces in 20+ countries including the US, UK, Germany, France, Italy, Spain, Japan, Australia, India, and Canada.

Amazon's financial data is exceptionally complex because every order generates multiple line items: product price, shipping credits, gift wrap, promotional rebates, FBA fees, referral fees, taxes, and more. Each line item is a separate row in the settlement report.

---

## Section 2 — Export Formats

| Format | Use Case |
|--------|----------|
| TSV (Tab-separated) | Settlement Report V2 (GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2). The primary financial report. |
| CSV | Date Range Reports (custom period exports from Payments dashboard). |
| XML | Settlement Report XML version (legacy). |
| PDF | Summary reports, account activity PDFs (for overview, not line-item data). |

The **Settlement Report V2** is the most important export for bookkeeping. It covers one settlement period (typically 14 days) and includes every financial event. Date Range Reports allow custom period selection but use a slightly different format.

---

## Section 3 — Column Mapping

### Settlement Report V2 (Flat File)

| Column Header | Meaning |
|---------------|---------|
| settlement-id | Unique settlement period identifier. All rows in one settlement share this ID. |
| settlement-start-date | Start of the settlement period (ISO 8601). |
| settlement-end-date | End of the settlement period (ISO 8601). |
| deposit-date | Date Amazon deposited funds to the seller's bank account. |
| total-amount | Total settlement amount deposited. Only populated on the first row. |
| currency | Three-letter ISO currency code (USD, GBP, EUR). |
| transaction-type | Order, Refund, Service Fee, Adjustment, Transfer, Liquidations, other (see Section 4). |
| order-id | Amazon order ID (e.g., 111-1234567-1234567). Blank for non-order transactions. |
| merchant-order-id | Seller's own order reference (if set). |
| adjustment-id | Identifier for adjustment transactions. |
| shipment-id | FBA shipment ID. |
| marketplace-name | Which Amazon marketplace (amazon.com, amazon.co.uk, amazon.de, etc.). |
| amount-type | Category of the amount: ItemPrice, ItemFees, Promotion, ItemWithheldTax, other. |
| amount-description | Specific fee/charge name (see Section 4 for complete list). |
| amount | The monetary value. Positive = credit to seller, negative = debit from seller. |
| fulfillment-id | AFN (Fulfilled by Amazon / FBA) or MFN (Merchant Fulfilled). |
| posted-date | Date the transaction was posted. |
| posted-date-time | Full timestamp of posting (ISO 8601). |
| order-item-code | Amazon's internal line item identifier. |
| merchant-order-item-id | Seller's own line item reference. |
| merchant-adjustment-item-id | Seller's adjustment reference. |
| sku | Product SKU. |
| quantity-purchased | Number of units in the order. |
| promotion-id | Promotion identifier if a promotion was applied. |

---

## Section 4 — Transaction Type Codes

### transaction-type values

| Value | Meaning |
|-------|---------|
| Order | Revenue from a customer order |
| Refund | Refund issued to customer (reverses order amounts) |
| Service Fee | Amazon service charges (subscription, advertising, FBA storage) |
| Adjustment | Manual adjustments (reimbursements, corrections) |
| Transfer | Settlement deposit to seller's bank account |
| Liquidations | FBA liquidation proceeds |
| other | Catch-all for miscellaneous events |

### amount-type values

| Value | Meaning |
|-------|---------|
| ItemPrice | Revenue components: Principal (product price), Shipping, GiftWrap, etc. |
| ItemFees | Amazon fees: Commission (referral fee), FBAPerUnitFulfillmentFee, ShippingHB, etc. |
| Promotion | Promotional discounts funded by the seller |
| ItemWithheldTax | Tax withheld by Amazon on behalf of the seller |
| other | Miscellaneous amounts |

### Key amount-description values

| amount-description | Meaning |
|-------------------|---------|
| Principal | Product sale price (revenue) |
| Shipping | Shipping credit from buyer |
| ShippingTax | Tax on shipping |
| Tax | Product tax collected |
| GiftWrap | Gift wrapping fee |
| Commission | Amazon referral fee (percentage of sale price) |
| FBAPerUnitFulfillmentFee | FBA pick, pack, and ship fee per unit |
| FBAPerOrderFulfillmentFee | FBA per-order fee |
| FBAWeightBasedFee | FBA weight-based shipping fee |
| ShippingHB | Shipping handling fee |
| StorageRenewalBilling | FBA monthly/long-term storage fees |
| Subscription | Professional seller subscription ($39.99/mo) |
| PromotionShipping | Seller-funded free shipping promotion |

---

## Section 5 — Fee Structure

| Fee Type | How It Appears |
|----------|---------------|
| Referral fee (Commission) | transaction-type = Order, amount-type = ItemFees, amount-description = Commission. Typically 8–15% depending on category. Negative amount. |
| FBA fulfilment fee | transaction-type = Order, amount-type = ItemFees, amount-description = FBAPerUnitFulfillmentFee. Per-unit fee based on size/weight. |
| FBA storage fee | transaction-type = Service Fee, amount-description = StorageRenewalBilling. Monthly and long-term storage charges. |
| Professional seller subscription | transaction-type = Service Fee, amount-description = Subscription. $39.99/month. |
| Advertising fees | Separate report (Sponsored Products). Not in the settlement report. |
| Refund administration fee | When Amazon refunds a customer, the original referral fee may be partially retained. Appears as a positive ItemFees amount on the Refund row. |

Multiple fee rows per order are normal. A single order may generate 5–10 rows: Principal, Shipping, Tax, Commission, FBAPerUnitFulfillmentFee, Promotion, etc.

---

## Section 6 — Tax-Relevant Fields

| Field | Notes |
|-------|-------|
| amount-description = Tax | Sales tax / VAT collected on the product price. |
| amount-description = ShippingTax | Tax on shipping charges. |
| amount-type = ItemWithheldTax | Tax withheld and remitted by Amazon (Marketplace Tax Collection). Applies in US states where Amazon collects tax on behalf of sellers. |
| marketplace-name | Determines which country's tax rules apply. |
| currency | Tax currency matches the marketplace currency. |
| Shipping address (not in settlement) | Full address needed for US sales tax nexus determination. Available in the Orders report, not the settlement report. |

In the US, Amazon collects and remits sales tax in Marketplace Facilitator states. The seller sees ItemWithheldTax but does NOT owe this tax — Amazon pays it. In the EU/UK, Amazon may collect VAT under certain schemes (IOSS, OSS). Always cross-reference with the Amazon VAT Transaction Report for EU sellers.

---

## Section 7 — Multi-Currency Handling

| Scenario | How It Appears |
|----------|---------------|
| Single marketplace | All rows in one currency matching the marketplace (USD for .com, GBP for .co.uk, EUR for .de/.fr/.it/.es). |
| Multiple marketplaces | Separate settlement reports per marketplace. Each in its own currency. |
| Amazon Currency Converter | If enabled, Amazon converts foreign marketplace revenue to the seller's home currency. Settlement total-amount is in home currency. Individual rows are in marketplace currency. |
| Cross-border FBA | Inventory in one country, sold in another. Settlement reports are per-marketplace regardless of inventory location. |

Amazon does NOT show exchange rates in the settlement report. If using Amazon Currency Converter, the effective rate must be calculated from the marketplace-currency amounts vs the total-amount in home currency.

---

## Section 8 — Reconciliation Tips

1. **One settlement report per settlement period.** Typically 14-day cycles. You need all settlement reports to cover a full accounting period.
2. **total-amount = bank deposit.** The total-amount on the first row should match the bank deposit from Amazon. This is the anchor for reconciliation.
3. **Multiple rows per order.** A single order generates rows for Principal, Shipping, Commission, FBA fees, Tax, Promotions. Sum all rows for a given order-id to get the net impact.
4. **Aggregate by amount-type for P&L.** Sum all ItemPrice amounts = Revenue. Sum all ItemFees amounts = Amazon fees (cost of sales). Sum all Promotion amounts = Promotional discounts.
5. **Refund rows mirror order rows.** A refund generates the same row types (Principal, Shipping, Commission) but with reversed signs. The Commission refund may be less than the original (Amazon retains a refund admin fee).
6. **Service Fee rows are separate from orders.** Storage fees, subscription fees, and other service charges have no order-id. Group these as operating expenses.
7. **Transfer row = settlement total.** The row with transaction-type = Transfer and a negative amount represents the payout to your bank. Its absolute value should equal total-amount.

---

## Section 9 — Common Gotchas

1. **Hundreds of rows per settlement.** A settlement with 50 orders may have 300+ rows because each order has 5–10 amount lines. Do not count rows as transactions.
2. **EU decimal format.** European marketplace exports use comma as decimal separator (95,00 not 95.00). Check the locale before parsing.
3. **Tax collected ≠ tax owed (US).** In Marketplace Facilitator states, Amazon collects and remits. The tax rows are informational, not money owed by the seller.
4. **Promotional rebates reduce revenue.** Seller-funded promotions (free shipping, percentage-off coupons) appear as negative Promotion amounts. Subtract from gross revenue.
5. **FBA reimbursements.** When Amazon loses or damages inventory, reimbursements appear as Adjustment rows. These are not revenue — they are compensation for lost inventory.
6. **Currency Converter hides FX risk.** If using Amazon's converter, the settlement is in your home currency but individual rows are in the marketplace currency. The FX spread is Amazon's profit, not visible in the report.
7. **Advertising costs are in a separate report.** Sponsored Products, Sponsored Brands, and Sponsored Display fees do NOT appear in the settlement report. They are deducted in a separate settlement or charged to a card.
8. **Negative settlements.** If refunds + fees exceed revenue in a period, Amazon may charge the seller's card or carry a negative balance forward. The total-amount will be negative.

---

## Section 10 — Sample Data

```tsv
settlement-id	settlement-start-date	settlement-end-date	deposit-date	total-amount	currency	transaction-type	order-id	merchant-order-id	adjustment-id	shipment-id	marketplace-name	amount-type	amount-description	amount	fulfillment-id	posted-date	posted-date-time	order-item-code	merchant-order-item-id	merchant-adjustment-item-id	sku	quantity-purchased	promotion-id
18906543210	2026-03-01T00:00:00+00:00	2026-03-15T00:00:00+00:00	2026-03-17	1847.32	GBP								
18906543210	2026-03-01T00:00:00+00:00	2026-03-15T00:00:00+00:00	2026-03-17		GBP	Order	206-1234567-8901234			FBA12345	amazon.co.uk	ItemPrice	Principal	29.99	AFN	2026-03-02	2026-03-02T14:23:00+00:00	12345678901234		WIDGET-001	1
18906543210	2026-03-01T00:00:00+00:00	2026-03-15T00:00:00+00:00	2026-03-17		GBP	Order	206-1234567-8901234			FBA12345	amazon.co.uk	ItemPrice	Shipping	3.99	AFN	2026-03-02	2026-03-02T14:23:00+00:00	12345678901234		WIDGET-001	1
18906543210	2026-03-01T00:00:00+00:00	2026-03-15T00:00:00+00:00	2026-03-17		GBP	Order	206-1234567-8901234			FBA12345	amazon.co.uk	ItemFees	Commission	-4.50	AFN	2026-03-02	2026-03-02T14:23:00+00:00	12345678901234		WIDGET-001	1
18906543210	2026-03-01T00:00:00+00:00	2026-03-15T00:00:00+00:00	2026-03-17		GBP	Order	206-1234567-8901234			FBA12345	amazon.co.uk	ItemFees	FBAPerUnitFulfillmentFee	-3.21	AFN	2026-03-02	2026-03-02T14:23:00+00:00	12345678901234		WIDGET-001	1
18906543210	2026-03-01T00:00:00+00:00	2026-03-15T00:00:00+00:00	2026-03-17		GBP	Refund	206-9876543-2109876			FBA12346	amazon.co.uk	ItemPrice	Principal	-19.99	AFN	2026-03-05	2026-03-05T09:15:00+00:00	98765432109876		GADGET-002	1
18906543210	2026-03-01T00:00:00+00:00	2026-03-15T00:00:00+00:00	2026-03-17		GBP	Refund	206-9876543-2109876			FBA12346	amazon.co.uk	ItemFees	Commission	2.40	AFN	2026-03-05	2026-03-05T09:15:00+00:00	98765432109876		GADGET-002	1
18906543210	2026-03-01T00:00:00+00:00	2026-03-15T00:00:00+00:00	2026-03-17		GBP	Service Fee					amazon.co.uk	other	Subscription	-25.00		2026-03-01	2026-03-01T00:00:00+00:00
18906543210	2026-03-01T00:00:00+00:00	2026-03-15T00:00:00+00:00	2026-03-17		GBP	Transfer								-1847.32		2026-03-17	2026-03-17T06:00:00+00:00
```

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.
