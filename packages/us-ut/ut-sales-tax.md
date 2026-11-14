---
name: ut-sales-tax
description: "Utah sales/use computation, grocery versus prepared food, current remote nexus and sourcing, SaaS, exemptions and electronic TC-62S/TC-62M filing."
version: "1.1"
jurisdiction: US-UT
category: state-tax
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: computation
---

# Utah sales and use tax, tax year 2026

> **General reference only.** Written by Codex. Not reviewed by an accountant. Obtain qualified professional review before filing, paying or taking a tax position.

> **Circular 230 section 10.37:** Apply relevant law to the taxpayer's facts, evaluate reasonable assumptions and relevant circumstances, and obtain professional review of federal tax implications. Federal figures and computations belong to the linked federal owner skills.

**Answer first.** Classify the sale, establish Utah collection responsibility, source it under the correct rule, and use the dated combined rate for that location. Qualifying grocery food is uniformly **3%**, including ordinary packaged candy/soft drinks that meet the food definition and are not prepared food. The old 7.5% maximum, 200-transaction nexus test and annual-filing thresholds must not be used. Source: [Publication 25 revision 09/26](https://tax.utah.gov/forms-pubs/pub-25/).

**Contributor:** Open Accounting Skills Registry.

## Scope

Ordinary retail sales/use tax for Utah stores, remote sellers, marketplace sellers and purchasers. Includes existing food, clothing, medical, services, digital/SaaS, manufacturing, agriculture, resale and exempt-organization topics. Tourism/lodging, vehicle, energy and telecom levies may be separate; full specialist administration is outside this core job. `us-sales-tax` owns multistate/federal context; `ut-income-tax`, `ut-corporate-tax` and `ut-payroll` own the other state jobs. Utah taxability does not establish Oregon/Idaho treatment merely because a seller is based there.

## Ask the client first

1. Utah sales-tax account, assigned frequency, locations, employees, inventory and nexus history.
2. Current/prior calendar-year Utah sales, marketplace-collected versus direct sales and collection contracts.
3. Item/service description, food ingredients/preparation/utensils, software rights and invoice bundles.
4. Order-receipt, seller, delivery and user locations, dates and dated rate lookup evidence.
5. Exemption certificates, resale/manufacturing/farm/medical use and supporting qualifications.
6. Period sales/refunds, exempt sales, purchases/withdrawals subject to use tax, payments and EFT status.

## The method, step by step

### Rates, bands and thresholds

| Item | Rate or amount and conditions | Official source |
|---|---|---|
| General state sales/use component | 4.85% in current Pub 25; rate charts split 4.70% plus 0.15% components; add applicable local/transit/special components | [Chart 2](https://tax.utah.gov/forms-pubs/pub-25/); [2026 combined charts](https://tax.utah.gov/business/sales-tax/sales/rates/) |
| Qualifying grocery food | 3% combined statewide: 1.75% state +1% local +0.25% county | [Food and Chart 2](https://tax.utah.gov/forms-pubs/pub-25/) |
| General combined rate | Dated jurisdiction/address lookup; no statewide 7.5% ceiling | [2026 charts and TAP address lookup](https://tax.utah.gov/business/sales-tax/sales/rates/) |
| Remote economic nexus | **More than USD 100,000** qualifying Utah sales in current or prior calendar year; do not use old 200-transaction alternative | [Sales Tax License registration/nexus section](https://tax.utah.gov/forms-pubs/pub-25/) |
| Sales-tax filing frequency | Annual liability below USD 50,000 may file quarterly; USD 50,000 or more monthly; assigned frequency controls | [Filing Frequency](https://tax.utah.gov/forms-pubs/pub-25/) |
| Monthly seller discount | 1.31% of combined tax, subject to eligibility/timeliness; food discount uses full combined rate; quarterly not eligible | [Seller Discount and Penalties](https://tax.utah.gov/forms-pubs/pub-25/) |
| Mandatory EFT | Annual sales-tax liability USD 96,000 or more | [Electronic Funds Transfer](https://tax.utah.gov/forms-pubs/pub-25/) |

1. Register through TAP using the tax-account application if liable. Physical or other statutory nexus can apply independently of remote sales volume. For an ordinary remote seller, apply the current **more-than** USD 100,000 current/prior-year test; do not trigger registration solely because transaction count exceeds 200. Marketplace facilitator collection and seller direct-sales obligations require reconciliation so the same sale is not remitted twice; confirm the actual facilitator's responsibility and any remaining registration. Source: [registration, nexus and marketplace sections](https://tax.utah.gov/forms-pubs/pub-25/).
2. Classify the taxable base. Tangible personal property, clothing, rentals/leases, taxable electronically transferred products and listed services are generally taxed unless exempt. Repair/renovation/cleaning of TPP, assisted laundry, certain admissions, short-term lodging and in-state telecom are taxable categories. Exempt-property repairs, unassisted laundry and specific admission exceptions qualify only under their rules. The old generic parking, all-IT-services and broad professional/medical/education/finance/personal-care lists are **Not yet confirmed** as universal rules; use the exact transaction authority. Source: [Definitions, Taxable Transactions, Product/Use Exemptions and Labor](https://tax.utah.gov/forms-pubs/pub-25/).
3. Food means human ingestion/chewing for taste/nutrition, excluding alcohol, tobacco and prepared food. Ordinary packaged candy/soft drinks can meet this definition, correcting the old full-rate rule. Prepared food includes food sold heated, two or more ingredients mixed/combined by the seller, or food sold with seller-provided eating utensils, with statutory exceptions such as qualifying bakery items/raw-food preparation. A cold salad mixed by the seller is not automatically 3% merely because unheated and no utensils. An uncut birthday cake can qualify under bakery exceptions; confirm preparation and utensils. Source: [Food and Prepared Food definitions](https://tax.utah.gov/forms-pubs/pub-25/).
4. Prescription drugs and prescribed DME/mobility equipment can be exempt; OTC items without a qualifying prescription are not automatically exempt. Prosthetic-device exemption requires prescription-required device or purchase by a hospital/medical facility; eyeglasses/contact lenses are excluded from that definition. Do not apply the old unconditional prosthetics exemption. Source: [Product-Based Exemptions](https://tax.utah.gov/forms-pubs/pub-25/).
5. Prewritten/canned software is taxable whether physical, electronic or remotely accessed. Remotely accessed prewritten software is sourced to the user's location; a documented reasonable consistent allocation may split use among locations. Remotely accessed custom software fees are not taxable under Pub 64. Distinguish genuinely custom from modified prewritten software; separate taxable software/repair from qualifying nontaxable services. Downloaded products taxable in physical form, streaming subscriptions and games can be taxable; database information access has a specific exemption that excludes digital books/audio/audiovisual works. Sources: [Software, remote-access examples and Computer Services](https://tax.utah.gov/forms-pubs/pub-64/); [electronic products, streaming and database exemption](https://tax.utah.gov/forms-pubs/pub-25/).
6. Apply **Chart 1 sourcing**, not a universal origin/destination slogan. Ordinary TPP orders received at a Utah fixed seller location generally use that seller location even when shipped within Utah. Orders received outside Utah for delivery in Utah generally use the buyer's receipt location. Services, no-copy prewritten software, leases, special events, vehicles and real-property installation have distinct rules. An out-of-Utah delivery by seller/common carrier can be exempt with shipment proof; the buyer collecting in Utah and taking goods elsewhere is different. Sources: [Chart 1 and interstate-delivery exemption](https://tax.utah.gov/forms-pubs/pub-25/); [remote software sourcing](https://tax.utah.gov/forms-pubs/pub-64/).
7. Save rate lookup for the exact quarter/address/jurisdiction. Do not reuse old Salt Lake City 7.75% or Provo 7.25% as current named-city rates. Rate charts include special districts and separate prepared-food/lodging/lease taxes that may add to ordinary combined sales tax. Separately stated qualifying delivery/installation charges can be excluded; freight-in and taxable repair charges are different. Source: [rate types and address lookup](https://tax.utah.gov/business/sales-tax/sales/rates/); [delivery, installation and related taxes](https://tax.utah.gov/forms-pubs/pub-25/).
8. Apply exemption only after checking purchaser, use, product and evidence. Resale/components can qualify; manufacturing machinery/equipment/repair parts/materials require a **qualified facility/use** and exclude office equipment/supplies. Agriculture machinery/feed/seed and breeding/production livestock are not a blanket all-farm-purchase exemption; confirm primary farming use and category. Government/nonprofit status alone does not prove each purchase exempt: charitable purchases have Tax Commission exemption-number and point-of-sale/refund conditions. Retain signed TC-721/TC-721G or complete electronic equivalent when required; require a new certificate after more than 12 months since last purchase. Sources: [exemption certificates and entity/use/product rules](https://tax.utah.gov/forms-pubs/pub-25/).
9. Compute each category/location's taxable receipts and tax, rounding to nearest cent as Pub 25 instructs (third decimal greater than 4 rounds up). Assess use tax on untaxed taxable purchases or inventory withdrawals at cost, reduced only by eligible other-state sales/use tax credit up to Utah liability. Grocery use remains 3%. Do not automatically tax spoilage/discards as consumption. Source: [Goods Consumed, Reminders and other-state-tax exemption](https://tax.utah.gov/forms-pubs/pub-25/).

### Existing edge cases and tests, corrected

| Existing item | Retained decision/example and correction |
|---|---|
| EC1 food/produce/chips/candy/drinks | Qualifying produce, packaged snacks, candy/soft drinks 3%; prepared deli food full combined; verify actual definition |
| EC2 Oregon SaaS seller / EC5 Idaho SaaS seller | Utah remotely accessed prewritten software taxable at user locations; apply current 100,000 threshold and physical nexus; no unsupported home-state comparison |
| EC3 SLC to Park City / Test 7 SLC to Provo | Ordinary intrastate TPP order at fixed Utah store uses seller location; software/services differ; current named-city rates require dated lookup |
| EC4 food uniformity / Test 2 | USD 200 qualifying groceries x 3%=USD 6, total USD 206, independent of local general rate |
| EC6 birthday cake/hot sandwich/cold salad | Bakery exception can apply to cake; hot sandwich prepared; salad mixed by seller may be prepared even without heat/utensils |
| EC7 USD 500,000 production line / Test 8 USD 100,000 equipment | USD 0 tax only when qualified manufacturing facility/use and certificate established; otherwise compute normal tax; office/nonqualifying property not automatically exempt |
| Test 1 USD 1,000 electronics | At an **illustrative verified invoice rate** 7.75%, tax USD 77.50, total USD 1,077.50; this is not a current SLC rate assertion |
| Test 3 USD 10 packaged candy | Qualifying grocery candy 3%=USD 0.30, total USD 10.30; old USD 0.78/full-rate result wrong |
| Test 4 USD 800 SaaS | At illustrative invoice/user-location 7.25%, tax USD 58, total USD 858; no claim this is current Provo rate |
| Test 5 USD 105,000 prior-year remote sales | Above 100,000 current threshold; register/collect subject to actual qualifying-sales and marketplace analysis |
| Test 6 USD 8 hot sandwich +USD 5 cold salad | If seller mixed salad, both prepared: at illustrative 7.25%, tax USD 0.9425 rounds USD 0.94, total USD 13.94 before separate restaurant levies. If salad independently qualifies grocery, tax USD 0.58+0.15=0.73; facts must establish exception |
| SST/SSTRS/CSP | State official rate page links Streamlined boundary files; full member/status, registration and CSP eligibility details Not yet confirmed here |
| Penalty abatement/audit/voluntary disclosure | Professional referral, not automatic waiver; retain notices and underlying source facts |

Sources: [definitions, Chart 1, exemptions and rounding](https://tax.utah.gov/forms-pubs/pub-25/); [remote software examples](https://tax.utah.gov/forms-pubs/pub-64/). Rates labeled illustrative are arithmetic inputs, not official locality assertions.

## Worked cases

**Case 1, ordinary seller with use tax.** Invented quarterly retailer has USD 10,000 general taxable receipts at an independently verified illustrative combined rate 8%, USD 2,000 qualifying grocery receipts and USD 500 untaxed taxable business purchases at 8%. Tax USD 800+60+40=900; quarterly filer has no seller discount. Rate 8% is a case input and does not claim a locality's current rate.

```oa-check
name: Utah general food and use tax quarterly
inputs:
  general_sales: 10000
  groceries: 2000
  untaxed_purchases: 500
  general_rate: 0.08
steps:
  - general_tax: general_sales * general_rate
  - food_tax: groceries * 0.03
  - use_tax: untaxed_purchases * general_rate
  - total_due: general_tax + food_tax + use_tax
expected:
  general_tax: 800
  food_tax: 60
  use_tax: 40
  total_due: 900
```

**Case 2, food and nexus boundary.** Invented remote seller has exactly USD 100,000 qualifying prior-year sales and 250 transactions, no physical/other nexus, then USD 105,000 current-year qualifying sales. Exactly 100,000/250 alone does not satisfy the current more-than 100,000 test; 105,000 exceeds it. A USD 10 ordinary packaged grocery-candy sale uses 3%, yielding USD 0.30, not the general 8% illustrative rate's USD 0.80. Collection commencement mechanics for the precise crossing date remain a gap, so this case does not prescribe a retroactive collection date.

```oa-check
name: Utah grocery candy and strict economic threshold
inputs:
  candy_price: 10
  prior_sales: 100000
  current_sales: 105000
steps:
  - candy_tax: candy_price * 0.03
  - candy_total: candy_price + candy_tax
  - prior_excess: max(prior_sales - 100000, 0)
  - current_excess: max(current_sales - 100000, 0)
expected:
  candy_tax: 0.3
  candy_total: 10.3
  prior_excess: 0
  current_excess: 5000
```

## When to refuse or refer

Refer unclear product/service classification, manufacturing/farm qualifications, mixed food/bakery facts, complex remote software allocation, marketplace responsibility disputes, multistate nexus, audit defense, voluntary disclosure and penalty abatement. Do not assume all intrastate services use origin or all SaaS is exempt.

## Filing and payment

Register/file/pay at https://tap.tax.utah.gov. **Current Pub 25 revision 09/26** requires electronic returns each assigned period, including zero tax. Below USD 50,000 annual liability may be quarterly; 50,000 or more monthly; the Commission assigns frequency. The old annual-return/<USD 250 and quarterly-average USD 1,000 scheme is superseded. Return/payment due last day following period, next business day if weekend/legal holiday. **TC-62S** is for one fixed Utah business location; **TC-62M** all others, including remote/no-fixed-location filers, with A/AG seller-location, J/JG customer-location, and X special-exemption schedules as applicable. File complete locality allocations. Payment alone does not file a return. Source: [Filing and Reporting Requirements](https://tax.utah.gov/forms-pubs/pub-25/).

Reconcile gross receipts, exemptions, food/general/location bases, use tax, discount and deposits before submission. Monthly eligible filers may deduct 1.31% combined tax; food sellers compute discount as if full combined rate collected. Quarterly filers cannot claim it. Annual liability USD 96,000 or more requires EFT; wrong current-payment method, late filing or underpayment can lose discount. Retain both accepted return and payment confirmation. Keep complete records/certificates for at least three years from filing and longer where another applicable rule requires. Notify account/location changes and closure; license is not transferable. Source: [Seller Discount, EFT, Records and Reminders](https://tax.utah.gov/forms-pubs/pub-25/).

## Penalties and interest

Pub 25 provides graduated late-file/late-pay penalties generally greater of USD 20 or up to 10%, with another failure-to-pay charge if unpaid 90 days after due; it is not always a flat 10%. Interest runs from original due date until paid. The old quarterly interest-reset assertion is **Not yet confirmed**; obtain current Pub 58 before computing any dated assessment. Source: [Penalties and Interest](https://tax.utah.gov/forms-pubs/pub-25/).

## Completion checklist

- Nexus/marketplace responsibility, product category and transaction sourcing documented.
- Dated rate evidence and food/prepared/software/exemption decisions retained.
- Assigned electronic return/schedules, zero periods, use tax and discount eligibility checked.
- Return/payment accepted separately and records retained; special levies/referrals recorded.

## Sources

| Official source and scope actually read | URL | Read on |
|---|---|---|
| Read for Current Pub 25 rev 09/26: registration/nexus, Food and Prepared Food definitions, Chart 1 sourcing, Chart 2 rates, entity/use/product exemptions, taxable services/digital/streaming, filing frequency and TC-62 forms/schedules, discount/EFT, penalties, records and adjacent service sections. | https://tax.utah.gov/forms-pubs/pub-25/ | 2026-11-13 |
| Read for 2026 rate-chart headings, combined versus other/simplified rate descriptions, address/ZIP+4 lookup and locality/special-district rows; no unsupported maximum or current city rate inferred. | https://tax.utah.gov/business/sales-tax/sales/rates/ | 2026-11-13 |
| Read for Pub 64 rev 05/12 currently linked by Pub 25: prewritten/custom software, remote user-location sourcing and multi-location/direct-pay examples, computer service/invoice distinctions; old publication caveat retained. | https://tax.utah.gov/forms-pubs/pub-64/ | 2026-11-13 |

Not yet confirmed: precise economic-nexus collection commencement after threshold crossing, facilitator-specific registration exceptions, full SST/SSTRS/CSP terms, parking and universal professional/personal/financial service classifications, all agriculture/livestock qualifications, complex bundles/custom software, current Pub 58 interest/penalty arithmetic and full lodging/restaurant/vehicle/telecom specialist administration. Use current quarter/address lookup for every actual locality rate.
