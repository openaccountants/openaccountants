---
name: eu-ioss-gb-sellers
description: >
  Prepare the EU side of an IOSS sales workpaper for a Great Britain seller
  using an EU intermediary in 2026. Check imported consumer-sale eligibility,
  the inclusive consignment ceiling, marketplace responsibility and the actual
  registration start before applying destination VAT. Separate the temporary
  customs duty from the November Union handling fee and show how charges
  collected at checkout affect supply VAT. Reconcile monthly country and rate
  totals, corrections, payment references and retained records. Trigger on GB
  sales to EU consumers, IOSS intermediary, low-value imports, marketplace VAT,
  customs item charges and monthly IOSS reporting. Refer UK export, Northern
  Ireland, special customs, product-rate and unresolved national portal questions.
jurisdiction: EU-27
tax_year: 2026
last_updated: 2026-11-16
version: 0.1
category: international
type: filing-howto
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
---

# EU import VAT and IOSS for Great Britain sellers v0.1

> **General reference only.** Prepare a workpaper for qualified review before filing or deploying checkout changes.

## Scope

Tax year: 2026. Operative source paragraphs and current source versions checked on 16 November 2026. This Guide covers the EU side of direct sales by a Great Britain-established business shipping ordinary goods from Great Britain to EU consumers, using an IOSS registration administered by an EU Member State through an intermediary. It does not determine UK export VAT, the HMRC registration route, Northern Ireland treatment, product safety, sanctions or the destination country's product-specific VAT classification. Selecting this workflow does not imply that the EU registration route is the only available route.

### What this means for your business

If you sell goods from Great Britain to EU consumers, IOSS can let the seller responsible for the sale collect the destination country's VAT at checkout and report it through a single monthly import-scheme return. For the EU registration route covered here, a non-EU seller uses an intermediary. A qualifying marketplace may instead be responsible for the customer-facing VAT. IOSS does not cover every shipment and does not eliminate customs duty. [Commission scope and supplier roles](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en), [registration](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/register-oss_en)

The changes that matter most are the goods' location when sold, the consignment's value, whether the buyer is a consumer, and who is legally making the sale for VAT purposes. Moving stock into an EU warehouse changes the analysis. So does selling through a marketplace rather than your own store.

## Ask the client first

- Are the goods shipped from Great Britain after the sale, or already held in the EU?
- Are you selling to consumers through your own checkout or through a marketplace that accounts for VAT?
- Are the consignments within the IOSS value limit, and is an IOSS registration already active?
- What are the sale/payment-acceptance and customs-declaration dates, and which duty or fee is charged to the consumer at checkout?
- What are the product classification, origin, customs item grouping and current destination VAT-rate evidence?
- Who is the permitted customs declarant or indirect representative, and which national portal will the intermediary use?

Start with these answers. Obtain product, shipment and registration evidence at the relevant step below, where it determines the treatment.

## The method, step by step

1. **Separate the import scheme from other flows.** IOSS covers qualifying imported distance sales with consignment intrinsic value not exceeding €150. Excise goods cannot be declared in the import scheme. Goods already held in an EU warehouse are not imported distance sales when later dispatched from that warehouse. New means of transport and goods installed or assembled are excluded from this distance-sale definition. Business transactions outside the covered consumer-equivalent categories require separate analysis. [Commission scope](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en)

2. **Confirm the EU registration route and its effective date.** For this non-EU-established seller using an EU Member State as identification state, appoint an eligible intermediary and confirm the identification state follows the intermediary's establishment rules. The intermediary's own identification number is distinct from each represented seller's IOSS VAT number. Only one identification state is allowed per scheme. Import-scheme registration starts when the individual IOSS VAT number is allocated, not from the next quarter or the date the seller first wanted to use it. [Commission registration rules](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/register-oss_en)

3. **Determine intrinsic value for the actual consignment.** The boundary is inclusive, not “less than €150”. Retain the calculation and parcel evidence. Intrinsic value excludes separately identified transport/insurance and identifiable taxes; embedded transport/insurance not separately shown remains included. Goods packed together and sent simultaneously by the same consignor to the same consignee under the same transport contract are a consignment. Do not confuse an order line, customs item and consignment. Refer split-order or artificial-arrangement questions before making a declaration. [Commission customs guidance, section 5.1](https://taxation-customs.ec.europa.eu/document/download/053e5b4e-f0be-4f20-9a23-3e3b659a6676_en?filename=Customs+Guidance+on+EUR+3+customs+duty.pdf)

4. **Identify the accountable supplier and capture destination VAT.** A facilitating electronic interface may be the deemed supplier for qualifying low-value imports; determine that role from the transaction facts and retain its tax evidence. Do not declare the marketplace's customer VAT again as the underlying seller's IOSS VAT. Make sure the carrier uses the IOSS details belonging to the party accounting for that sale. Keep its declaration acceptance so a customer charged VAT again on delivery can be traced back to the shipment. For direct seller-accounted transactions, establish the destination Member State and product-specific rate before configuring checkout. IOSS supply VAT is collected when payment is accepted. Each rate conclusion needs current destination authority evidence; this Guide supplies no universal EU VAT rate. [Commission deemed-supplier and consumption concepts](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en), [payment acceptance and IOSS VAT](https://vat-one-stop-shop.ec.europa.eu/document/download/3086db0e-7b4a-4202-9f38-d32bd774f5a8_en?filename=20260821_VAT+guidelines-3+EUR+Customs+duty_revised.pdf)

5. **Calculate customs duty separately from IOSS VAT.** The former low-value customs-duty exemption was abolished from 1 July 2026. The temporary rule runs until 1 July 2028 under [Regulation 2026/382 arts. 1–4](https://eur-lex.europa.eu/eli/reg/2026/382/oj/eng). For the IOSS imports within this Guide, the temporary customs duty is €3 per customs item in a consignment not exceeding €150. An item may contain multiple physical units sharing the required tariff classification, description and, where required/provided, origin; it is neither automatically one charge per parcel nor one per retail unit. Ask the customs declarant to confirm the item grouping and duty charge before you promise the customer a landed price. The Commission guidance cites Regulation 2026/382 and the customs delegated/implementing provisions. Do not apply this simplified conclusion to non-IOSS, preferential or special-procedure flows without a separate customs review. [Commission operational customs guidance, sections 2–5](https://taxation-customs.ec.europa.eu/document/download/053e5b4e-f0be-4f20-9a23-3e3b659a6676_en?filename=Customs+Guidance+on+EUR+3+customs+duty.pdf)

6. **Apply the current duty/VAT interaction.** For a valid IOSS import, import VAT is exempt and no import VAT is charged on the customs duty. The duty arises when the declaration for release for free circulation is accepted. Ordinarily it is not included in the earlier IOSS supply VAT base merely because it will later become payable. However, if the supplier charges the customs duty to the consumer at sale, that charge forms part of the consideration and is included in the supply VAT base. Preserve the checkout terms and invoice. The live addendum is the revised 6 October 2026 text, despite the August date in its filename. It expressly makes this distinction. [Commission VAT addendum](https://vat-one-stop-shop.ec.europa.eu/document/download/3086db0e-7b4a-4202-9f38-d32bd774f5a8_en?filename=20260821_VAT+guidelines-3+EUR+Customs+duty_revised.pdf)

7. **Add the separate Union handling fee for the applicable period.** From 1 November 2026, the fee is €2 per customs item for distance-sale goods released for free circulation. It is separate from customs duty, applies regardless of consignment value and is non-refundable. The customs-debt debtor, or the person who would have been that debtor if no customs debt exists, owes it. A contract passing the cost to the buyer does not itself decide that statutory debtor. For valid IOSS imports, no import VAT is due on the fee at import; if the fee is charged to the consumer at sale, it is included in the IOSS supply VAT base. Do not add it to a pre-November period or promise a refund of the fee merely because goods are returned. [Regulation 2026/2152 arts. 1–2](https://eur-lex.europa.eu/eli/reg_del/2026/2152/oj/eng), [Regulation 2026/2108 art. 20(5)–(6), 287](https://eur-lex.europa.eu/eli/reg/2026/2108/oj/eng), [VAT addendum, handling-fee section](https://vat-one-stop-shop.ec.europa.eu/document/download/3086db0e-7b4a-4202-9f38-d32bd774f5a8_en?filename=20260821_VAT+guidelines-3+EUR+Customs+duty_revised.pdf)

8. **Confirm the customs handoff.** For the covered consignments not exceeding €150, the amended Annex B declaration hierarchy applies from 1 July 2026 under Regulation 2026/1022 art. 2(2), Annex point (2)(c): the IOSS user or its indirect representative is the declarant for the IOSS flow. Regulation 2026/2108 art. 85(2) applies from 20 September 2026 under art. 287(3)(e). The later statutory commencement does not defer the July data requirement. A non-EU IOSS holder uses an EU indirect representative under the Commission's stated operational route. Confirm the representative and the accepted declaration rather than treating the VAT intermediary as automatically appointed for customs. The two functions are distinct. From 1 November 2026, the product-identifier data requirement applies under Regulation 2026/1022 art. 2(3), Annex point (2)(a)–(b). Ask the declarant to verify those identifiers and the handling-fee data; this workpaper does not replace the national customs declaration. [Regulation 2026/1022 art. 2, Annex (2)(c)](https://eur-lex.europa.eu/eli/reg_del/2026/1022/oj/eng), [Regulation 2026/2108 arts. 85(2), 287(3)](https://eur-lex.europa.eu/eli/reg/2026/2108/oj/eng), [customs guidance sections 6.4 and 8](https://taxation-customs.ec.europa.eu/document/download/053e5b4e-f0be-4f20-9a23-3e3b659a6676_en?filename=Customs+Guidance+on+EUR+3+customs+duty.pdf)

9. **Give the intermediary a reconciled monthly sales total.** Include the scheme's covered sales across all destination Member States; do not selectively use IOSS for convenient countries. File the import-scheme return monthly, including nil returns where applicable, and pay by the end of the following month. Reconcile gross orders, refunds, rate/country totals, marketplace reports, carrier declarations and money paid. Input tax is not deducted in the IOSS return; address any recovery separately. Use the identification state's required reporting currency and the prescribed period-end ECB conversion for return figures; that return conversion does not itself establish the customs eligibility value. Preserve the return reference with its payment. [Commission declaration and payment rules](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/declare-and-pay-oss_en)

10. **Keep adjustments and records traceable.** Record corrections against the original supply period and Member State. The ordinary electronic OSS correction window is three years from the original return deadline; later corrections need the consumption state's national procedure. Retain scheme records for ten years from the end of the transaction year and make them electronically available on request. Keep the invoice, rate evidence, taxable amount/currency, payments, dispatch/destination evidence and returned-goods documents together. [Commission corrections](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/declare-and-pay-oss_en), [record requirements](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/record-keeping-and-audits-oss_en)

### Linked figures

| Figure | Scope and period | Source |
|---|---|---|
| €150 | Inclusive intrinsic-value limit for IOSS consignments | [Commission](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en) |
| €3 | Temporary customs duty per defined customs item on covered IOSS imports from 1 July 2026 until 1 July 2028 | [Customs guidance](https://taxation-customs.ec.europa.eu/document/download/053e5b4e-f0be-4f20-9a23-3e3b659a6676_en?filename=Customs+Guidance+on+EUR+3+customs+duty.pdf) |

| €2 | Separate non-refundable Union handling fee per customs item from 1 November 2026; distance-sale scope, not limited to consignments up to €150 | [Regulation 2026/2152 arts. 1–2](https://eur-lex.europa.eu/eli/reg_del/2026/2152/oj/eng); [Regulation 2026/2108 art. 20](https://eur-lex.europa.eu/eli/reg/2026/2108/oj/eng) |

## Worked cases

These are manually reasoned research checks, not signed client filings. The monetary example uses an assumed product rate only to demonstrate arithmetic; the actual destination rate must be sourced separately. Round the illustrative final result to two decimal places.

### Original duty-only comparison

This case isolates the duty/VAT interaction, including for the July–October period before the handling fee applied. It does not assert a current full landed cost.

**Duty charged at sale.** Assume net product price €100, an assumed rate of 20%, and €3 customs duty charged to the buyer at sale. The supply VAT base is €103 and VAT is €20.60. If that duty is not charged to the consumer at sale, the assumed product base remains €100 and illustrative VAT is €20; do not add the later customs duty automatically. These outcomes concern the IOSS supply calculation and do not decide who ultimately bears the customs cost. [Commission duty/VAT distinction](https://vat-one-stop-shop.ec.europa.eu/document/download/3086db0e-7b4a-4202-9f38-d32bd774f5a8_en?filename=20260821_VAT+guidelines-3+EUR+Customs+duty_revised.pdf)


```oa-check
name: Original IOSS duty charged at sale comparison
inputs:
  net_product_price: 100
  assumed_vat_rate: 0.20
  duty_charged_at_sale: 3
steps:
  base_with_duty: net_product_price + duty_charged_at_sale
  vat_with_duty: base_with_duty * assumed_vat_rate
  base_without_duty_charge: net_product_price
  vat_without_duty_charge: base_without_duty_charge * assumed_vat_rate
expected:
  base_with_duty: 103
  vat_with_duty: 20.60
  base_without_duty_charge: 100
  vat_without_duty_charge: 20
```

### November current-period comparison

Assume an eligible IOSS consignment, one confirmed customs item, net product price €100 and an independently established illustrative 20% product rate. Both €3 duty and €2 handling fee are charged to the consumer at sale. The supply VAT base is €105, VAT €21 and checkout total €126. If neither charge is passed on at sale, this isolated assumed product base stays €100 and supply VAT €20; the statutory customs charges still need payment by the proper debtor. This is not a universal VAT rate or permission to use IOSS. [Regulation 2026/2152 arts. 1–2](https://eur-lex.europa.eu/eli/reg_del/2026/2152/oj/eng), [current VAT addendum](https://vat-one-stop-shop.ec.europa.eu/document/download/3086db0e-7b4a-4202-9f38-d32bd774f5a8_en?filename=20260821_VAT+guidelines-3+EUR+Customs+duty_revised.pdf)

```oa-check
name: November IOSS duty and handling fee charged at sale
inputs:
  net_product_price: 100
  assumed_vat_rate: 0.20
  confirmed_customs_items: 1
  duty_per_item: 3
  handling_fee_per_item: 2
steps:
  customs_duty: confirmed_customs_items * duty_per_item
  handling_fee: confirmed_customs_items * handling_fee_per_item
  checkout_base: net_product_price + customs_duty + handling_fee
  supply_vat: checkout_base * assumed_vat_rate
  checkout_total: checkout_base + supply_vat
  supply_vat_without_checkout_charges: net_product_price * assumed_vat_rate
expected:
  customs_duty: 3
  handling_fee: 2
  checkout_base: 105
  supply_vat: 21
  checkout_total: 126
  supply_vat_without_checkout_charges: 20
```

### Other original boundary cases

**Exactly at the limit.** An otherwise eligible consignment with intrinsic value exactly €150 can qualify. One exceeding that limit cannot use IOSS merely because its individual items are cheaper. [Commission eligibility](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en)

**Multiple units in one customs item.** Do not multiply the duty by retail quantity before reviewing tariff classification, description and the applicable origin data. Conversely, a parcel with distinct customs items cannot automatically be treated as a single duty item. [Commission item definition](https://taxation-customs.ec.europa.eu/document/download/053e5b4e-f0be-4f20-9a23-3e3b659a6676_en?filename=Customs+Guidance+on+EUR+3+customs+duty.pdf)

**EU warehouse.** The seller bought stock into an EU warehouse before the consumer sale. Route the later sale under the relevant domestic or intra-EU rules, rather than IOSS. This VAT routing does not establish relief from duty or the handling fee for goods in a bonded customs warehouse; refer that separate route. [Commission imported-distance-sale definition](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en)

**Registration pending.** An application without allocation of the IOSS VAT number has not started the import scheme. Do not backdate an IOSS treatment from the next successful return. [Commission commencement rule](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/register-oss_en)

**Marketplace sale.** A marketplace is the deemed supplier and reports the consumer sale. Reconcile that record to the marketplace flow and avoid duplicate seller IOSS reporting. If the facts do not establish its role, do not select an outcome from the payout description. [Commission deemed-supplier definition](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en)

## When to refuse or refer

- Stop before filing or checkout deployment if the consumer/product category, destination rate, consignment value, intermediary registration, marketplace role or customs declaration is unresolved.
- Refer excise goods, installed goods, new means of transport, business sales, special fiscal territories, foreign-stock moves, special customs procedures and preferential-duty claims.
- Refer repeated VAT collection at import: obtain the accepted declaration and original checkout evidence before choosing a refund or correction. A customer complaint alone does not prove which return must change.
- Recheck the method for later periods. Do not apply January 2027 or other future OSS changes early. The original handling-fee uncertainty is resolved above by the published 2026/2152 commencement; do not treat the older expected date in October explanatory notes as the legal trigger.

Before launching the sales route, confirm who charges VAT, who files and pays it, who pays customs duty, and what the buyer will be charged at delivery. Give the intermediary the reconciled monthly sales and adjustment records, and retain the return and payment receipts. Check the UK export treatment separately.

## Filing and payment

The intermediary uses the Member State of identification's official OSS portal. Prepare the represented seller's IOSS identifier, intermediary identifier and calendar month; country-by-country taxable amounts, rates and VAT; corrections identifying the original period and consumption state; and the resulting VAT totals. The Commission's return layout separates general information, current country supplies, prior-period corrections, country balances and the total due. Negative corrections in one state do not offset another state's positive liability. Exempt and zero-rated supplies are excluded under the Commission's stated return rules. If there are no supplies and no corrections, submit the nil return rather than omit the period. Retain electronic acknowledgement and the unique return reference. Use that reference on payment, and ensure funds reach the identification state's account by the end of the following month; the weekend/public-holiday boundary does not extend the return deadline. The prescribed return currency and period-end ECB conversion apply; customs eligibility valuation is separate. Obtain the actual national field layout rather than inventing a common EU portal. [Commission filing, currency and payment FAQs](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/declare-and-pay-oss_en)

## Completion checklist

- Document consumer, goods-location, consignment-value and supplier-role eligibility.
- Bind sales to the allocated active IOSS number and correct customs representative.
- Reconcile duty, handling fee, VAT base and checkout charges to their applicable dates.
- Reconcile country/rate totals, corrections, nil reporting, payment reference and bank receipt.
- Preserve electronic records and source evidence; obtain qualified review before action.

## Sources

| Official source and exact scope read | URL | Read on |
|---|---|---|
| Commission OSS scope: import-scheme eligibility, deemed supplier, intermediary and all-covered-sales concepts | https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en | 2026-11-16 |
| Commission registration: intermediary/identification-state rules, separate identifiers and import-scheme allocation start | https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/register-oss_en | 2026-11-16 |
| Commission declaration/payment: monthly and nil returns, country/rate contents, corrections, currency, input-tax exclusion, deadline and payment-reference FAQs | https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/declare-and-pay-oss_en | 2026-11-16 |
| Commission records: ten-year clock, electronic access and article 63c content | https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/record-keeping-and-audits-oss_en | 2026-11-16 |
| Regulation 2026/382 arts. 1–4: abolished threshold, temporary duty scope and 1 July 2026 commencement | https://eur-lex.europa.eu/eli/reg/2026/382/oj/eng | 2026-11-16 |
| Customs guidance, actual 5 October 2026 version: sections 2–5, 6.4, 7.6 and 8; item/consignment, declarant and current data handoff; October expected handling-fee date superseded by final law below | https://taxation-customs.ec.europa.eu/document/download/053e5b4e-f0be-4f20-9a23-3e3b659a6676_en?filename=Customs+Guidance+on+EUR+3+customs+duty.pdf | 2026-11-16 |
| VAT addendum, actual revised 6 October 2026 version: IOSS duty and fee consideration versus import exemption, pp. 1 and 3; neighboring non-IOSS routes read to keep scope separate | https://vat-one-stop-shop.ec.europa.eu/document/download/3086db0e-7b4a-4202-9f38-d32bd774f5a8_en?filename=20260821_VAT+guidelines-3+EUR+Customs+duty_revised.pdf | 2026-11-16 |
| Regulation 2026/2108 arts. 5(15),(44),(78), 20, 85(2), 287: current definitions, fee debtor/nonrefundability and staggered commencement; later general provisions not applied early | https://eur-lex.europa.eu/eli/reg/2026/2108/oj/eng | 2026-11-16 |
| Regulation 2026/1022 art. 2(2)–(3), Annex point (2)(a)–(c): July declaration hierarchy and November product-identifier data commencement read; detailed carrier implementation remains referred | https://eur-lex.europa.eu/eli/reg_del/2026/1022/oj/eng | 2026-11-16 |
| Published Regulation 2026/2152 arts. 1–2, OJ 22 October: EUR 2 amount and 1 November 2026 application; supersedes the adopted draft's blank publication date | https://eur-lex.europa.eu/eli/reg_del/2026/2152/oj/eng | 2026-11-16 |

Not yet confirmed: product-specific destination VAT classification/rate, actual identification-state portal fields and national recovery/refund procedures, full customs/PID declaration implementation for a particular carrier, UK export/HMRC registration and Northern Ireland treatment, preferential/special-procedure or bonded-warehouse outcomes, and the detailed January 2027 changes referred to in the old version. These are non-usable holds: obtain the actual authority and transaction evidence before using such a result. Neither example is a complete landed-cost or customs filing instruction.
