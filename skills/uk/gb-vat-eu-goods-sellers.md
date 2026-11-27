---
name: gb-vat-eu-goods-sellers
description: "UK VAT workflow for EU sellers not established in the UK who ship goods to customers in Great Britain in 2026. Covers the GBP 135 consignment test, direct sales against qualifying online marketplaces, goods already in UK stock and the deemed zero-rated supply, business customers with a UK VAT number and the reverse charge, registration with no threshold for a non-established seller and the zero-rated exemption, import VAT and its evidence, the 20% standard rate, returns and the 6 year record rule. Northern Ireland, services and excise goods are out of scope."
version: "2.1"
type: situation-rules
jurisdiction: GB
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
authored_by: Michael Cutajar and the OpenAccountants team
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
domain: vat-gst
---

# EU sellers sending goods to Great Britain: VAT decision workflow

## Scope

If your business sells goods from the EU to customers in Great Britain, who accounts for UK VAT depends on where the goods are when sold, who buys them and whether a marketplace handles the sale. The table below helps you identify your route before you set prices, configure checkout or prepare your VAT return. [HMRC direct sales](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk), [HMRC marketplace sales](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-to-customers-in-the-uk-using-online-marketplaces).

For tax year 2026, this Guide covers calendar-year sales by EU businesses not established in the UK to customers in England, Scotland and Wales. Northern Ireland, services, excise goods, gifts and special import arrangements need separate guidance. Your dispatch country's export treatment also needs its own assessment. A UK VAT number or warehouse address alone does not establish where your business is based for VAT. [HMRC scope](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk)

This is a calendar-year transaction scope, not an income-tax assessment year. Reassess when the rules or fulfilment arrangements change.

## Ask the client first

Identify the sales you want to assess:

- Are the goods outside the UK or already in a UK warehouse when sold?
- Are you selling directly or through a marketplace that accounts for VAT?
- Is the buyer a consumer or a business supplying a valid UK VAT number, and is delivery to Great Britain?

Keep one flow sheet per channel and stock location: seller identity and establishments; goods ownership at sale/import; dispatch and delivery territory; UK VAT status and customer number; warehouse and parcel records; order/payment/dispatch dates; original invoice, discounts, currency, transport/insurance/taxes; refunds/replacements; channel agreement and tax reports; Incoterms, carrier instructions, declarant, importer and recovery evidence. Mark missing facts unknown.

Different channels and stock locations can produce different answers for the same business. Work through each below; the supporting records you need are explained with the relevant decision.
- Does the seller have any establishment in the UK (an office, staff, a fixed place of business)? A UK VAT number or warehouse address alone does not establish it.
- Is any of the goods' VAT rate reduced or zero? Which product classification has been used?

## The method, step by step

1. Separate Great Britain from Northern Ireland

Check the delivery address on the order. Northern Ireland follows different rules, so a UK country code alone is not enough to choose this Great Britain route. [HMRC territorial distinctions](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk)

2. Decide whether the channel is a qualifying online marketplace

Do not treat a payment processor or a hosted web shop as automatically responsible for VAT. The platform must allow third-party offers and sale contracts. All three operator conditions must be met: involvement in supply terms, payment authorisation/facilitation and ordering or delivery. Payment processing alone, advertising/listing alone, or simple redirection alone is excluded. Check your marketplace agreement and tax reports: they should show whether the platform takes responsibility for the sale under these rules. [VATA section 95A](https://www.legislation.gov.uk/ukpga/1994/23/section/95A), [HMRC marketplace definition](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-to-customers-in-the-uk-using-online-marketplaces)

3. Locate the goods at sale and choose the route

Use your order and warehouse records to establish where the goods were when sold and who owned them. For a business customer, check the UK VAT number supplied for that sale; a company name or an EU VAT number is insufficient.

The route table is under Boundary and exception table below.

Sources: [VATA section 5A](https://www.legislation.gov.uk/ukpga/1994/23/section/5A), [section 7AA](https://www.legislation.gov.uk/ukpga/1994/23/section/7AA), [Schedule 8 Group 21](https://www.legislation.gov.uk/ukpga/1994/23/schedule/8), [direct sales](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk), [marketplace sales](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-to-customers-in-the-uk-using-online-marketplaces).

4. Calculate the consignment threshold correctly

The £135 test concerns the total intrinsic value of the imported consignment, rather than each item. Add items sent together. Exclude separately identified transport/insurance and identifiable taxes; transport/insurance embedded in the price and not separately shown remains included. A changed order that crosses the boundary must be reassessed before dispatch, including any VAT already charged. [HMRC valuation rules](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk)

Use the order invoice and parcel records to calculate the value of everything sent together, including discounts. Keep the threshold calculation separate from the amount on which VAT is charged. Excluding a separately shown delivery charge from intrinsic value does not itself exclude that charge from the VAT base. Determine the supply's consideration and ancillary-charge treatment under the ordinary VAT rules. For a foreign-currency order, retain the conversion method, rate and date; do not improvise a conversion solely to fit below the boundary. Resolve uncertain valuation with the customs/VAT adviser. [HMRC VAT Notice 700, consideration and value of supply](https://www.gov.uk/guidance/vat-guide-notice-700)

5. Establish registration and recovery separately

A seller with no UK business or fixed establishment must register when it makes taxable UK business supplies or reasonably expects them in the next 30 days; there is no monetary threshold. The ordinary UK-established £90,000 threshold does not apply. Once liability arises from actual supplies, notify HMRC within 30 days and registration runs from that liability date; for the prospective test, notify by the end of that 30-day period and registration runs from its beginning. [VATA Schedule 1A paragraphs 1, 5 and 6](https://www.legislation.gov.uk/ukpga/1994/23/schedule/1A)

For direct imported low-value B2B sales meeting section 7AA, the customer is treated as making the taxable supply; if all the seller's UK supplies are reverse charged, the seller is neither entitled nor liable to register on those supplies. Do not extend this to seller-imported consignments above £135: section 7(6) can make the seller's onward supply a UK supply. If the seller only makes qualifying overseas low-value sales through a marketplace, its deemed supply to that marketplace is outside the UK under section 7(5A). Test the whole sales population. [VATA sections 7 and 7AA](https://www.legislation.gov.uk/ukpga/1994/23/section/7), [reverse-charge law](https://www.legislation.gov.uk/ukpga/1994/23/section/7AA), [HMRC NETP rules](https://www.gov.uk/hmrc-internal-manuals/vat-registration-manual/vatreg37200)

Where all taxable supplies are, or would be, zero-rated, exemption requires the seller's request and HMRC's agreement; it is not automatic. Notify a material change in the nature of supplies within 30 days of the change, or, if no particular day can be identified, within 30 days of the quarter end. [Schedule 1A paragraph 13](https://www.legislation.gov.uk/ukpga/1994/23/schedule/1A/paragraph/13)

A seller making only deemed zero-rated supplies through a marketplace may register or apply for exemption. The overseas seller remains liable for import VAT/customs when it imports stock; marketplace collection on the eventual retail sale does not settle that import. Before importing, agree who will be the importer with your carrier or customs agent. Check the delivery terms, goods ownership and customs declaration. To recover import VAT, be registered, have the right to dispose of the goods (usually as owner), use them for deductible business activities and hold official evidence: the C79 for paid import VAT or the postponed import VAT statement for postponed VAT accounting (PVA). Apply normal deduction restrictions; marketplace statements and carrier payments alone do not establish entitlement. [HMRC import evidence, Notice 700 section 19.5.7](https://www.gov.uk/guidance/vat-guide-notice-700), [HMRC PVA conditions](https://www.gov.uk/guidance/check-when-you-can-account-for-import-vat-on-your-vat-return)

PVA is an option for eligible UK VAT-registered importers, not a new tax exemption or automatic full deduction. Include the VAT number on the declaration. A seller without a UK establishment needs a customs representative: instruct them in writing before declaration to select PVA and enter the seller as consignee. Reconcile the monthly statement to import entries. Postal imports above £135 through Royal Mail Group (including Parcelforce when not acting as an express operator) cannot use PVA; its commercial non-postal services can if requested. For special procedures or merchandise in baggage, do not use this ordinary PVA conclusion. Check this point with one of our partner accountants. [HMRC PVA](https://www.gov.uk/guidance/check-when-you-can-account-for-import-vat-on-your-vat-return)

6. Determine the rate, post and reconcile

Classify the product before selecting the rate. The standard rate is 20%, but reduced or zero rates may apply to particular goods; obtain the relevant product guidance before using an exception. [HMRC VAT rates](https://www.gov.uk/vat-rates)

Keep sales where you account for VAT separate from marketplace-accounted sales, deemed supplies, qualifying B2B reverse-charge sales and ordinary imports. This makes the return easier to reconcile. Compare gross orders with tax reports, refunds, fees, payments and stock movements: a platform's net payout is not your taxable sales total.

Assign the correct return period using the applicable tax-point rules. Prepare a return mapping only after the transaction classification is complete; use the UK VAT-return Guide and current return instructions for actual boxes and deadlines. Retain the decision, source version and evidence beside the transaction. For direct overseas sales, HMRC requires full VAT records for six years. [HMRC tax points and accounting](https://www.gov.uk/guidance/vat-guide-notice-700), [direct-sale record retention](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk)


### Rates, bands and thresholds

| Figure | Applicability | Official source |
|---|---|---|
| £135 | Consignment intrinsic-value limit (inclusive) for the low-value goods rules; applies to the total consignment, not each item | https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk |
| No NETP monetary threshold | Taxable UK business supplies made or expected in the next 30 days; assess reverse-charge/outside-UK routes and HMRC-agreed zero-rated exemption first | https://www.legislation.gov.uk/ukpga/1994/23/schedule/1A |
| £90,000 | Ordinary domestic registration threshold, not a relief for a non-established seller | https://www.gov.uk/register-for-vat |
| Exemption from registration | A non-established taxable person may ask HMRC for it only if all its taxable supplies are zero-rated | https://www.legislation.gov.uk/ukpga/1994/23/schedule/1A/paragraph/13 |
| 20% | Standard VAT rate; first classify the product | https://www.gov.uk/vat-rates |
| 5% | Reduced rate for some goods and services; check the product guidance before using it | same |
| 6 years | Full VAT records (including VAT invoices) kept from the date any goods are sold, direct overseas sales | https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk |
| One calendar month and 7 days | Usual deadline for the online VAT return and payment after the period ends | https://www.gov.uk/vat-returns/deadlines |

## Boundary and exception table

Which route the facts point to (step 3).

| Facts established | UK VAT route to investigate and record |
|---|---|
| Goods outside the UK; direct consumer sale; consignment intrinsic value no more than £135 | Seller accounts for supply VAT at sale and must address UK VAT registration. |
| Same goods/value, but sold through a qualifying marketplace to a consumer | Marketplace accounts for the VAT under the overseas-goods rules. Obtain its tax evidence. |
| Goods outside the UK; qualifying low-value sale to a UK VAT-registered business, direct or via marketplace | Verify the UK number; the Great Britain customer accounts under section 7AA reverse charge. An EU VAT number alone does not qualify. |
| Goods outside the UK; consignment exceeds £135 | Ordinary import VAT/customs route. Establish the importer and onward supply treatment before assigning liability or recovery. |
| Goods already in Great Britain; overseas seller sells directly | Seller registration and domestic supply VAT apply regardless of consignment value, subject to the separately assessed zero-rated-registration exemption. |
| Goods already in Great Britain; qualifying marketplace consumer sale by a seller not established in the UK | Marketplace accounts for the customer sale; the seller makes a deemed zero-rated supply to it. Import obligations remain a separate question. |
| Goods already in Great Britain; UK VAT-registered marketplace customer | Seller accounts only where the customer gives the marketplace its UK VAT number and the marketplace gives the seller that number and supply details within 7 days beginning with the tax-point day (or longer if HMRC allows). Otherwise the deemed marketplace route applies. Do not apply imported-low-value reverse charge to UK stock. |

Sources: [VATA section 5A](https://www.legislation.gov.uk/ukpga/1994/23/section/5A), [section 7AA](https://www.legislation.gov.uk/ukpga/1994/23/section/7AA), [Schedule 8 Group 21](https://www.legislation.gov.uk/ukpga/1994/23/schedule/8), [direct sales](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk), [marketplace sales](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-to-customers-in-the-uk-using-online-marketplaces).

## Worked cases

These are hypothetical decision checks, manually reasoned against the cited guidance; they are not client filings or professional sign-off. Numeric sales prices below are assumptions. Illustrative VAT arithmetic rounds only the final result to two decimal places.

### Direct sale below the boundary

A Netherlands-established seller has no UK establishment. It sends an ordinary standard-rated product from the Netherlands directly to a consumer in England. The merchandise is £100 excluding VAT; delivery is free; no marketplace is involved. Intrinsic value is £100. With the product's standard-rate classification confirmed, VAT is £100 × 20 / 100 = £20 and the customer total is £120. The seller-accounted low-value route applies. [HMRC direct-sale rule](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk), [standard rate](https://www.gov.uk/vat-rates)

```oa-check
name: Direct sale from the Netherlands to a consumer in England, GBP 100 at 20%
inputs:
  net_price: 100
  vat_rate: 0.20
  consignment_limit: 135
steps:
  - vat: round(net_price * vat_rate, 2)
  - customer_total: net_price + vat
  - headroom_under_limit: consignment_limit - net_price
expected:
  vat: 20.00
  customer_total: 120.00
  headroom_under_limit: 35.00
```

### Aggregate the parcel, then compare

Two items each priced at £70 excluding tax travel in the same consignment; delivery is free. Intrinsic value is £140. The low-value checkout route does not apply merely because each item is below £135. Identify the importer and apply the ordinary import workflow. An otherwise eligible consignment with intrinsic value exactly £135 remains on the low-value side. [HMRC consignment boundary](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk)

The decision: low-value checkout route or ordinary import route? Add the items in the consignment and compare with £135. Here the excess is £5, so the low-value route is closed; had the seller sent the two items as separate consignments on separate orders (a real commercial choice, not a split to avoid the limit), each £70 parcel would be on the low-value side with £65 of headroom.

```oa-check
name: Consignment of two GBP 70 items against the GBP 135 limit
inputs:
  item_price: 70
  items_in_parcel: 2
  consignment_limit: 135
steps:
  - intrinsic_value: item_price * items_in_parcel
  - excess_over_limit: intrinsic_value - consignment_limit
  - single_item_headroom: consignment_limit - item_price
expected:
  intrinsic_value: 140.00
  excess_over_limit: 5.00
  single_item_headroom: 65.00
```

A positive excess means the ordinary import route. Zero or positive headroom satisfies the value boundary only; all other eligibility conditions still apply. Do not split one order artificially to avoid the limit.

### Similar customer, different stock location

A UK VAT-registered customer supplies a valid UK VAT number. If its qualifying low-value parcel is outside the UK at sale, test the imported-goods B2B reverse charge. If the same seller's goods are already in Great Britain and the sale is through a marketplace, the seller accounts for UK VAT instead only when the marketplace passes the UK number and supply details to it within the statutory seven-day period (or permitted extension). Without that, the marketplace deemed-supply route applies. Preserve stock-location evidence: the two outcomes cannot be selected by looking only at the customer. [HMRC direct B2B rules](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk), [UK-stock marketplace B2B rules](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-to-customers-in-the-uk-using-online-marketplaces)

### Payment processor only

The seller controls its own shop; the third party only processes payment. Do not assign the seller's VAT to that provider. Document the marketplace definition and continue through the direct-sales route. [HMRC marketplace exclusions](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-to-customers-in-the-uk-using-online-marketplaces)

### Returned order

The original supplier charged UK VAT and subsequently refunds it when the goods are returned. Adjust that supplier's VAT return for the refunded VAT. If the seller did not originally charge the VAT, do not create a seller output-tax reversal merely because cash was refunded; reconcile the responsible marketplace's adjustment. Replacements with a changed value require an adjustment assessment. [HMRC returned-goods guidance](https://www.gov.uk/guidance/vat-and-overseas-goods-sent-to-the-uk-and-returned-to-the-seller)

## When to refuse or refer

Do not use an unresolved outcome below to file or configure checkout. Check this point with one of our partner accountants.

- Your business's UK establishment status, the marketplace's role, the importer, the consignment value or the product's VAT rate is unclear. These facts determine liability, registration and recovery.
- You have Northern Ireland movements, excise goods, mixed or bundled supplies, special customs procedures, gifts or earlier returns to correct.
- You intend to rely on a registration exclusion but cannot show that all relevant sales qualify.

Record the VAT-accountable party, registration decision, product rate, import/recovery evidence, ledger/return route, missing documents and responsible reviewer on the flow sheet. Keep the conclusion with the records supporting it. Where the sale crosses two tax systems, confirm both the UK treatment and the dispatch country's export treatment.

## Filing and payment

- **Register** under the liability dates and notification periods in step 5; a non-established seller has no monetary threshold. [HMRC registration](https://www.gov.uk/register-for-vat)
- **Returns** follow the ordinary UK rules: use the uk-vat-return Guide for the boxes and the return instructions. The online return and payment are usually due one calendar month and 7 days after the end of the period. [VAT Return deadlines](https://www.gov.uk/vat-returns/deadlines)
- **Records:** keep full VAT records, including VAT invoices, for 6 years from the date any goods are sold.

## Completion checklist

- Delivery addresses split between Great Britain and Northern Ireland.
- Each channel tested against the qualifying marketplace definition, with the agreement or tax report kept.
- Stock location at the time of sale recorded for every route.
- Consignment intrinsic value worked out per consignment, with the conversion method for foreign currency.
- UK VAT numbers of business customers checked for each sale.
- Registration decision recorded, including any exemption application.
- Product VAT rate classified before any reduced or zero rate is used.
- Seller-accounted, marketplace-accounted, deemed, reverse charge and import sales kept apart and reconciled to gross orders.

## Sources

| Source | What was read | URL | Read on |
| --- | --- | --- | --- |
| HMRC, VAT and overseas goods sold directly to customers in the UK | Read for the £135 consignment test, valuation, the B2B reverse charge and the 6 year record rule; registration exclusion qualified by the legislation below | https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk | 2026-11-27 |
| HMRC, VAT and overseas goods sold using online marketplaces | Read for the marketplace definition and exclusions, deemed zero-rated supplies and UK stock | https://www.gov.uk/guidance/vat-and-overseas-goods-sold-to-customers-in-the-uk-using-online-marketplaces | 2026-11-27 |
| HMRC, VAT and overseas goods sent to the UK and returned | Read for adjusting the return for refunded VAT and replacements | https://www.gov.uk/guidance/vat-and-overseas-goods-sent-to-the-uk-and-returned-to-the-seller | 2026-11-27 |
| GOV.UK, Register for VAT | Read for registration regardless of turnover for businesses based outside the UK, the £90,000 threshold and the zero-rated exemption | https://www.gov.uk/register-for-vat | 2026-11-27 |
| GOV.UK, VAT rates | Read for the 20% standard rate and the 5% reduced rate | https://www.gov.uk/vat-rates | 2026-11-27 |
| HMRC, VAT Notice 700 the VAT guide | Read for consideration and value of supply, tax points and input tax evidence | https://www.gov.uk/guidance/vat-guide-notice-700 | 2026-11-27 |
| GOV.UK, VAT Return deadlines | Read for one calendar month and 7 days | https://www.gov.uk/vat-returns/deadlines | 2026-11-27 |

| VATA 1994 sections 5A, 7, 7AA and 95A; Schedule 1A; Schedule 8 Group 21 | Operative marketplace, imported consignment, registration and zero-rating conditions | https://www.legislation.gov.uk/ukpga/1994/23 | 2026-11-27 |
| HMRC, postponed import VAT accounting | VAT registration, right to dispose, declaration and representative instructions, official statements and postal exclusion | https://www.gov.uk/guidance/check-when-you-can-account-for-import-vat-on-your-vat-return | 2026-11-27 |

Not yet confirmed: product classification, special arrangements and unresolved case facts remain non-usable until the specific referrals above are resolved. The dispatch country's export treatment is outside this Guide and is not checked here.
