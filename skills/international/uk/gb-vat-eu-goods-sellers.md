---
name: gb-vat-eu-goods-sellers
description: "UK VAT workflow for EU sellers shipping goods to Great Britain: consignment valuation, direct versus marketplace sales, UK stock, business customers, registration and returns."
jurisdiction: GB
tax_year: 2026
last_updated: 2026-10-04
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# EU sellers sending goods to Great Britain: VAT decision workflow

## Scope and applicable period

Tax year: 2026. This label identifies the calendar-year transaction scope; it does not imply that VAT follows an income-tax assessment year.

Use this Guide for an EU-established business selling physical goods to customers in England, Scotland or Wales during 2026. Its purpose is to decide who accounts for UK VAT and assemble the evidence needed before configuring checkout or preparing a return. Confirm the seller is not established in the UK; incorporation, a VAT number and a warehouse address alone are not a complete establishment analysis.

This is the Great Britain side of the corridor. Commission a separate review of the dispatch country's export treatment and supporting documents. Do not infer that an EU export exemption satisfies UK obligations. Northern Ireland transactions, services, excise goods, non-commercial gifts and special import arrangements need separate methods. The HMRC overseas-goods guidance expressly distinguishes these routes. [HMRC direct-sales scope](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk)

Research date: 4 October 2026. Recheck the official guidance at the transaction date, when the fulfilment model changes and before applying this method to a later period. A future-policy announcement does not change this workflow until its operative rules apply.

## Ask the client first

Build a flow sheet for each channel and stock location. Request:

- The contracting seller's identity, actual business establishments, UK VAT status and who owns the goods at sale and import.
- Customer delivery address, consumer/business status, and any UK VAT number supplied for the transaction. A company name or EU VAT number does not answer the UK-number question.
- Physical stock location when sold, dispatch location, destination and parcel/consignment identifier. Retain warehouse movements and carrier records.
- Order, payment and dispatch dates; invoice currency; merchandise prices; discounts; transport and insurance; taxes; refunds and replacement orders. Obtain the original invoice rather than relying on a settlement total.
- Channel agreement and marketplace tax reports. Identify who sets supply terms, participates in payment, and participates in ordering or delivery.
- Incoterms, carrier instructions, customs declarant and importer details, import declarations, import-VAT evidence and the party authorised to claim input tax.

These are working-paper controls: missing facts remain marked unknown. Do not fill an unknown importer or marketplace role from the business's preferred outcome.

## The method, step by step

1. Separate Great Britain from Northern Ireland

Confirm the actual delivery address. A UK country code is insufficient. Stop this workflow for Northern Ireland rather than treating it as a Great Britain import. Preserve the transaction and route it to the Northern Ireland/EU method. [HMRC territorial distinctions](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk)

2. Decide whether the channel is a qualifying online marketplace

Do not treat a payment processor or a hosted web shop as automatically responsible for VAT. HMRC's marketplace test requires involvement in supply terms, payment authorisation/facilitation and ordering or delivery. Payment processing alone, advertising/listing alone, or simple redirection alone is excluded. Retain the contract and actual transaction evidence, then document the result. [HMRC marketplace definition](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-to-customers-in-the-uk-using-online-marketplaces)

3. Locate the goods at sale and choose the route

| Facts established | UK VAT route to investigate and record |
|---|---|
| Goods outside the UK; direct consumer sale; consignment intrinsic value no more than £135 | Seller accounts for supply VAT at sale and must address UK VAT registration. |
| Same goods/value, but sold through a qualifying marketplace to a consumer | Marketplace accounts for the VAT under the overseas-goods rules. Obtain its tax evidence. |
| Goods outside the UK; qualifying low-value sale to a customer that supplies its UK VAT number | Check the number and the B2B conditions; the Great Britain customer accounts under the reverse charge. |
| Goods outside the UK; consignment exceeds £135 | Ordinary import VAT/customs route. Establish the importer and onward supply treatment before assigning liability or recovery. |
| Goods already in Great Britain; overseas seller sells directly | Seller registration and domestic supply VAT apply regardless of consignment value, subject to the separately assessed zero-rated-registration exemption. |
| Goods already in Great Britain; qualifying marketplace consumer sale by a seller not established in the UK | Marketplace accounts for the customer sale; the seller makes a deemed zero-rated supply to it. Import obligations remain a separate question. |
| Goods already in Great Britain; marketplace customer supplies its UK VAT number | Seller accounts for the sale and must address registration. Do not apply the imported-low-value B2B reverse charge to UK stock. |

Sources: [direct sales](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk), [marketplace sales](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-to-customers-in-the-uk-using-online-marketplaces).

4. Calculate the consignment threshold correctly

The £135 test concerns the total intrinsic value of the imported consignment, rather than each item. Add items sent together. Exclude separately identified transport/insurance and identifiable taxes; transport/insurance embedded in the price and not separately shown remains included. A changed order that crosses the boundary must be reassessed before dispatch, including any VAT already charged. [HMRC valuation rules](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk)

Keep the threshold computation separate from the taxable consideration. Excluding a separately shown delivery charge from intrinsic value does not itself exclude that charge from the VAT base. Determine the supply's consideration and ancillary-charge treatment under the ordinary VAT rules. For a foreign-currency order, retain the conversion method, rate and date; do not improvise a conversion solely to fit below the boundary. Resolve uncertain valuation with the customs/VAT adviser. [HMRC VAT Notice 700, consideration and value of supply](https://www.gov.uk/guidance/vat-guide-notice-700)

5. Establish registration and recovery separately

Do not apply the ordinary domestic £90,000 threshold to a non-established seller's taxable UK supplies. An exemption from registration for a non-established taxable person requires all its taxable supplies to be zero-rated and an application to HMRC; record the decision rather than assuming an exemption. For the direct imported-goods model, HMRC states that sellers do not have to register if they only sell goods outside the UK at the point of sale to UK VAT-registered businesses. Confirm the complete sales population meets that exclusion; domestic UK stock or consumer sales need separate analysis. [HMRC B2B-only exclusion](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk) [HMRC registration rules](https://www.gov.uk/register-for-vat)

A seller making only deemed zero-rated supplies through a marketplace may register or apply for exemption. The overseas seller remains liable for import VAT/customs when it imports stock; marketplace collection on the eventual retail sale does not settle that import. Recovery of import VAT requires the normal conditions, including appropriate evidence, rather than just a marketplace statement or a carrier payment. [HMRC marketplace stock rules](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-to-customers-in-the-uk-using-online-marketplaces), [HMRC input-tax and import evidence rules](https://www.gov.uk/guidance/vat-guide-notice-700)

6. Determine the rate, post and reconcile

Classify the product before selecting the rate. The standard rate is 20%, but reduced or zero rates may apply to particular goods; obtain the relevant product guidance before using an exception. [HMRC VAT rates](https://www.gov.uk/vat-rates)

Create separate ledger buckets for seller-accounted supply VAT, marketplace-accounted customer VAT, deemed supplies, imported low-value B2B reverse-charge sales and ordinary imports. These are suggested control buckets, not statutory return box labels. Reconcile gross orders to tax reports, refunds, fees, payments and stock movements. A platform's net payout is not the taxable sales total.

Assign the correct return period using the applicable tax-point rules. Prepare a return mapping only after the transaction classification is complete; use the UK VAT-return Guide and current return instructions for actual boxes and deadlines. Retain the decision, source version and evidence beside the transaction. For direct overseas sales, HMRC requires full VAT records for six years. [HMRC tax points and accounting](https://www.gov.uk/guidance/vat-guide-notice-700), [direct-sale record retention](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk)

## Linked figures

| Figure | Applicability | Official source |
|---|---|---|
| £135 | Inclusive consignment intrinsic-value boundary for qualifying low-value goods | [HMRC direct-sales guidance](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk) |
| £90,000 | Ordinary domestic registration threshold, not a NETP relief | [HMRC registration](https://www.gov.uk/register-for-vat) |
| 20% | Standard VAT rate; first classify the product | [HMRC rates](https://www.gov.uk/vat-rates) |

## Worked examples and boundary checks

These are hypothetical decision checks, manually reasoned against the cited guidance; they are not client filings or professional sign-off. Numeric sales prices below are assumptions. Illustrative VAT arithmetic rounds only the final result to two decimal places.

### Direct sale below the boundary

A Netherlands-established seller has no UK establishment. It sends an ordinary standard-rated product from the Netherlands directly to a consumer in England. The merchandise is £100 excluding VAT; delivery is free; no marketplace is involved. Intrinsic value is £100. With the product's standard-rate classification confirmed, VAT is £100 × 20 / 100 = £20 and the customer total is £120. The seller-accounted low-value route applies. [HMRC direct-sale rule](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk), [standard rate](https://www.gov.uk/vat-rates)

### Aggregate the parcel, then compare

Two items each priced at £70 excluding tax travel in the same consignment; delivery is free. Intrinsic value is £140. The low-value checkout route does not apply merely because each item is below £135. Identify the importer and apply the ordinary import workflow. An otherwise eligible consignment with intrinsic value exactly £135 remains on the low-value side. [HMRC consignment boundary](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk)

### Similar customer, different stock location

A UK VAT-registered customer supplies a valid UK VAT number. If its qualifying low-value parcel is outside the UK at sale, test the imported-goods B2B reverse charge. If the same seller's goods are already in Great Britain and the sale is through a marketplace, the seller accounts for UK VAT instead. Preserve stock-location evidence: the two outcomes cannot be selected by looking only at the customer. [HMRC direct B2B rules](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk), [UK-stock marketplace B2B rules](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-to-customers-in-the-uk-using-online-marketplaces)

### Payment processor only

The seller controls its own shop; the third party only processes payment. Do not assign the seller's VAT to that provider. Document the marketplace definition and continue through the direct-sales route. [HMRC marketplace exclusions](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-to-customers-in-the-uk-using-online-marketplaces)

### Returned order

The original supplier charged UK VAT and subsequently refunds it when the goods are returned. Adjust that supplier's VAT return for the refunded VAT. If the seller did not originally charge the VAT, do not create a seller output-tax reversal merely because cash was refunded; reconcile the responsible marketplace's adjustment. Replacements with a changed value require an adjustment assessment. [HMRC returned-goods guidance](https://www.gov.uk/guidance/vat-and-overseas-goods-sent-to-the-uk-and-returned-to-the-seller)

## When to refuse or refer

Deliver a row per transaction flow with: seller and establishments; dispatch and delivery territories; goods location at sale; customer status and VAT-number evidence; channel classification; consignment valuation; VAT-accountable party; registration decision; product rate evidence; importer and recovery evidence; ledger/return route; missing documents; and responsible reviewer.

- Mark the conclusion provisional and refer before filing when establishment, marketplace role, importer identity, valuation or rate is unresolved. 
- Also refer Northern Ireland movements, excise goods, mixed or bundled supplies, special customs procedures, gifts and historic corrections. 
- Do not issue a definitive no-registration conclusion from incomplete facts. The UK and dispatch-country advisers should each confirm their own side of the transaction before the client changes its live checkout configuration.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
