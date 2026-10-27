---
name: finland-vat-return
description: >
  Prepare and review an ordinary Finland VAT return for 2026. Establish
  registration, supply location, tax point, taxable consideration and rate before
  assigning return fields. Covers domestic sales, ordinary EU goods and
  services, exports, import VAT including the Åland tax border, construction
  reverse charge, input deductions, mixed use, passenger vehicles and property
  investment adjustments. Includes the current and preceding-year small-business
  test, 2026 reduced rates, filing periods, corrections and statutory sanctions.
  Trigger on Finnish VAT, ALV-ilmoitus, OmaVero, reverse charge, EU sale, import
  or deductible input VAT. Use with vat-workflow-base and eu-vat-directive;
  special margin, travel, marketplace and other sector schemes need separately
  verified treatment.
version: 2.7
jurisdiction: FI
tax_year: 2026
last_updated: 2026-10-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Finland VAT return v2.7

## Who this applies to

Use for ordinary taxable-business VAT in Finland in 2026, including individuals and companies, foreign suppliers subject to Finnish rules and VAT-registered importers. Do not infer the place of supply or exemption from the supplier's name. Identify the legal parties, establishment receiving/supplying a service, customer business status, goods movement, transaction date and purpose of purchases first. [VAT Act 1501/1993 §§1–3,8c–9,63–69m][law].

The ordinary method covers registration, base/rates, return mapping, input deductions and filing. Special margin/travel schemes, VAT groups, deemed-supplier marketplaces and unusual sector exemptions require their own statutory scope; this skill does not assign them ordinary treatment by default. [VAT Act chapters 4–5,9–12a][law].

## Rates, bands and thresholds

| Item | 2026 rule | Act / official source |
|---|---|---|
| General rate | 25.5% from 1 September 2024 (24% for supplies up to 31 August 2024; use 24% when correcting an older period) | VAT Act §84 [text][law]; [Vero rates][rates] |
| Reduced rate | 13.5% from 1 January 2026, formerly 14%; listed food/feed, meals, passenger transport, accommodation, medicines, books, qualifying sport/culture, sanitary products and specified art/performance/copyright/broadcasting items | VAT Act §85, Acts 1358/2025 and 921/2024 [text][law] |
| Newspapers/magazines | 10%, subject to publication definition | VAT Act §85a [text][law] |
| Small-business exemption | Both current and preceding calendar-year counted turnover at most EUR 20,000; no voluntary registration | VAT Act §3 [text][law] |
| Longer period application | Quarterly turnover ceiling EUR 100,000; annual EUR 30,000 | Procedure Act §12 [text][procedure]; [Vero tax periods][period] |
| Cash basis ordinary domestic sales | Calendar turnover at most EUR 500,000 or other statutory qualifying accounting status; 12-month collection backstop | VAT Act §§137,143 [text][law] |
| Small-error correction alternative | Tax difference at most EUR 500, subject to timing/data exclusions | Procedure Act §25 [text][procedure]; [return instructions][return] |
| EU cross-border consumer distance-sale/TBE threshold | EUR 10,000 combined current and preceding-year test, with single-state establishment and other §69m conditions | VAT Act §§63a,69i,69m [text][law] |

Vero's 13.5% examples include groceries and food, animal feed, restaurant and meal services, printed and electronic books, pharmaceuticals, sanitary protection products and baby diapers, sports and fitness services (including gym, golf, ice-rink bookings and ski-lift tickets), admission to cultural, entertainment and sports events, passenger transport, accommodation and, from 2026, public broadcasting services (10% until 31 December 2025). [Vero rates][rates]. Alcohol, tobacco and the serving of alcoholic drinks retain the general rate, even when sold by a restaurant or shop. An advertising-dominated or principally video/music publication does not qualify as a reduced-rate book/newspaper just because it is called one. Use supply/advance-payment tax-point rules at a rate transition; filing date alone does not select the rate. [VAT Act §§15–16,84–85a][law].

## The base

### Registration and period eligibility

1. To use the Finnish small-business VAT exemption, test turnover in **both the current and preceding calendar years**. Each must be no more than **€20,000**, and the seller must not have registered voluntarily. If preceding-year turnover exceeded the threshold, do not treat a still-low current year as exempt while waiting for a new current-year crossing. Map taxable sales and the specified VAT-exempt sales Vero includes (such as intra-EU supplies, exports, financial/insurance services and property rental); exclude fixed-asset sales and the other exclusions Vero lists. Sales whose place of supply is not Finland (for example consulting sold to businesses established abroad under the general place-of-supply rule) are not Finnish turnover, and purchases, including intra-EU acquisitions, are never turnover. Do not annualise a short year; a non-calendar accounting year is split into calendar years. The exemption is **not available** to a business established outside the EU, even if it has a permanent establishment in Finland. [Vero small-business exemption guidance](https://www.vero.fi/en/detailed-guidance/guidance/48658/vat-exemption-for-small-businesses/)
2. The start-date rule is separate: if **current-year** counted turnover exceeds €20,000, register and calculate liability from the crossing sale/date. That crossing sale is taxable in full at its supported rate. [Vero registration](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/how-to-register-for-vat/)
3. A business below €20,000 may voluntarily register if it conducts business. Voluntary registration means VAT is due on all taxable sales from the registration date; it is not a registration only for selected invoices. Registration takes effect at the earliest from the date the application is received or submitted; it cannot be backdated. A business whose only activity is VAT-exempt (for example financial or insurance services) cannot register, and intra-EU acquisitions of goods can require registration even for a business not otherwise VAT-liable. [Vero small-business exemption guidance](https://www.vero.fi/en/detailed-guidance/guidance/48658/vat-exemption-for-small-businesses/); [Vero registration](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/how-to-register-for-vat/)
4. Deregistration because of lower turnover is a separate workflow. An already registered business may seek deregistration only after turnover is below €20,000 in **two consecutive calendar years**; Vero describes this as the current and preceding years. The request is not retroactive. [Vero small-business exemption guidance](https://www.vero.fi/en/detailed-guidance/guidance/48658/vat-exemption-for-small-businesses/)
5. The normal tax period is one calendar month. A business with annual turnover of no more than €100,000 may request a quarter; one with annual turnover of no more than €30,000 may request a quarter or a calendar year. Conditions: a longer period is refused if the business has failed to file VAT returns on time or failed to pay its taxes; a granted longer period starts at the beginning of the year after the request; a tax period must stay unchanged for at least 12 months; and if turnover goes over the limit for the longer period, the business must tell Vero immediately so the period is shortened (Vero can shorten it on its own decision). Until Vero's decision on a new period arrives, file on the current period. Agricultural and forestry operators, primary producers and visual artists with no other VAT-liable activity use a calendar-year period whatever their turnover. [Vero tax-period guidance](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/tax-period/)
6. File a VAT return for **every** allocated period. For a period with no VAT activity, select the no-activity declaration in MyTax rather than omitting the return. Do **not** file a no-activity return if the period had zero-rate sales on which related purchases are deductible; report them under “Turnover taxable at zero VAT rate”. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/)
7. The former VAT relief for small businesses (the reduction for accounting-period turnover under €30,000) is **abolished**: it is not available for accounting periods starting on or after 1 January 2025. Do not claim it for any 2026 period. An accounting period that began before 1 January 2025 is an old-period question; refer it. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/); [Vero small-business exemption guidance](https://www.vero.fi/en/detailed-guidance/guidance/48658/vat-exemption-for-small-businesses/)



### Taxable consideration, tax point and deductions

Under §73 the base is consideration **excluding VAT**, including price supplements and incidental charges forming part of the agreed supply. For a VAT-inclusive price, net base = gross / (1 + rate), tax = gross − net; do not multiply a gross receipt by the nominal rate. Allocate genuinely separate supplies to their own supported rates; a single composite supply requires its principal/ancillary classification rather than an arbitrary split. Discounts, cancellations, bad debts and recovered bad debts follow §78, with matching input adjustments. [VAT Act §§73,78,118][law].

Recognise ordinary delivery/performance and pre-delivery advances under §§15–16 and 135a. In-year invoice allocation under §136 is reconciled to the final financial-year month. A qualifying §137 cash-basis election uses receipts, but no later than 12 months after delivery/performance absent bad debt; eligible purchases follow §143 payment timing. General-rule reverse-charge cross-border services retain §138's performance/advance timing. These rules prevent an invoice-date shortcut from moving an advance, EU transaction or import to the wrong period. [VAT Act §§15–16,135a–143][law].

For imports, establish customs value plus applicable duties/taxes and freight, insurance and incidental costs to the first Finnish destination, or a further known EU destination, without double counting. Apply the Finnish product rate to that base. Retain customs decision and supporting invoice/transport documents, and distinguish Customs collection from VAT-registered business self-assessment. [VAT Act §§86–93,102a][law].

Ordinary exempt property transfers/rent (§27), qualifying healthcare (§§34–36), social welfare (§§37–38), statutory education (§§39–40), financial services (§§41–42) and insurance (§44) have their defined taxpayer/service conditions. A label such as coaching, therapy or finance is insufficient. Directly attributable inputs to exempt supplies are not deductible; exports and qualifying EU supplies have a separate deduction-preserving route. Property letting can opt into tax under §30 only where its continuous qualifying use and letting-chain conditions are met, for the specified property/part. [VAT Act §§27–44,102,117,131][law].

### Transaction map and input VAT

Reconcile the return to the accounts, invoices, credit notes, import documents and VAT-ID checks. The following are current MyTax/Vero field labels and screens, not an assertion of permanent numeric box codes.

| Transaction after evidence check | VAT-return entry / calculation |
| --- | --- |
| Domestic taxable sale | Calculate VAT from the tax base in the workpaper, then enter the **VAT amount** by domestic rate (25.5%, 13.5% or 10%). Domestic sales can include own use, private withdrawal or other deemed domestic supply when Vero’s rules apply. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/) |
| Goods acquired from another EU country for the Finnish business | Enter “Purchases of goods from other EU countries”; calculate Finnish acquisition VAT under “Tax on purchases of goods from other EU countries”; claim the corresponding deductible VAT only if ordinary deduction conditions are met. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/) |
| General service purchased by a Finnish business from another EU business | **Only after establishing Finnish place of supply and purchaser liability**, enter the purchase base in “Purchases of services from other EU countries”, reverse-charge VAT in “Tax on purchases of services from other EU countries”, and qualifying input VAT. These fields apply only to services under the general place-of-supply rule. For a special-rule service supplied in Finland (for example a service relating to Finnish real estate, passenger transport or travel agency services), use the domestic-sales VAT row only if the purchaser is liable, with no entry in the EU-services rows. Construction services, including leased construction workers, bought from an EU seller go in the construction/scrap reverse-charge rows, not the EU-services rows. Passenger transport is excluded from this foreign-seller reverse charge; do not self-account merely because the supplier is foreign. Construction/scrap reverse charge needs its own determination and rows. [VAT Act, sections 9 and 65](https://www.finlex.fi/fi/lainsaadanto/1993/1501); [Vero cross-border services, sections 6–6.1](https://www.vero.fi/en/detailed-guidance/guidance/48679/value-added-taxation-of-cross-border-supply-and-acquisition-of-services/); [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/) |
| Service bought from a business established outside the EU | **Only for a taxable service supplied in Finland for which the purchaser is liable**, calculate Finnish VAT and enter the VAT amount in “Tax on domestic sales by tax rate”; the purchase base is not entered on the return. This field route covers qualifying general- and special-rule services from business operators of any size: Vero's English page says "small business", but the Finnish original says *elinkeinonharjoittaja* (any business operator), and the Finnish version prevails. If deductible, also enter qualifying input VAT. Foreign establishment alone establishes neither Finnish supply nor purchaser liability: for example, accommodation at a hotel abroad is outside the Finnish place-of-supply rule. [VAT Act, sections 9, 65 and 67](https://www.finlex.fi/fi/lainsaadanto/1993/1501); [Vero return instructions in Finnish](https://www.vero.fi/yritykset-ja-yhteisot/verot-ja-maksut/arvonlisaverotus/ilmoitus-ja-maksuohjeet/) |
| Goods imported into Finland | Enter the customs-supported base in “Imports of goods from outside the EU”, VAT in “Tax on imports of goods from outside the EU”, and qualifying input VAT in “Tax deductible for the tax period”. Report it in the return for the tax period in which the customs clearance decision was issued (the date printed on the decision), and put the deduction in the same month. If the customs decision later changes, correct the return. For a tax-exempt import, retain the import-base entry and leave the import-tax/deduction entries blank. Goods moving across the Åland tax border are imports/exports; apply the ordinary Åland import procedure below. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/) |
| Export/other zero-rate sale or exempt sale | Use the named treatment only after preserving conditions and evidence. Sales of goods to VAT-liable buyers in other EU countries (goods transported out of Finland) go in “Sales of goods to other EU Member States”; B2B services taxed in the buyer's EU country under the general rule go in “Sales of services to other EU Member States”; exports outside the EU and other zero-rate sales go in “Turnover taxable at zero VAT rate”. EU goods and service sales must also be reported on the VAT recapitulative statement. Sales to consumers in other EU countries are not zero-rated EU sales; whether Finnish VAT or the other country's VAT applies depends on distance-selling and OSS rules, which this skill refers. Exempt sales with no deduction right (health, social services) are not reported as zero-rate turnover. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/) |
| Special schemes | OSS/IOSS sales use the relevant separate scheme return. Second-hand-goods margin-scheme VAT belongs in the **ordinary VAT return**, domestic-sales tax at the applicable rate, after a separate eligible-margin computation. Do not group its reporting with OSS/IOSS. [Vero return instructions][return]; [Vero used-goods guidance §5.2][margin] |

**Foreign-service gate:** establish the receiving establishment and applicable general/special place-of-supply rule, then determine who owes Finnish VAT. A participating Finnish fixed establishment or the foreign seller's voluntary Finnish VAT registration prevents the ordinary foreign-seller reverse charge; statutory transaction exceptions also apply. If the seller owes VAT, obtain its correctly issued invoice and test any input deduction. If the service is supplied outside Finland, do not create Finnish reverse-charge VAT merely from the supplier's country. [VAT Act, sections 9, 65 and 67](https://www.finlex.fi/fi/lainsaadanto/1993/1501); [Vero cross-border services, sections 6–6.1](https://www.vero.fi/en/detailed-guidance/guidance/48679/value-added-taxation-of-cross-border-supply-and-acquisition-of-services/)

The ordinary net result is:

    VAT payable / refundable = output VAT and self-accounted VAT − deductible input VAT

This is a reconciliation aid. It does not establish a right to deduct, and it must be calculated from the field-level treatment above. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/)

For an ordinary domestic purchase, establish:

1. the buyer carries on VAT-liable business;
2. the purchase is for that business and not private use;
3. the seller is VAT registered; 
4. the purchase is supported by the required invoice/receipt; and
5. any mixed use is apportioned to the deductible business extent.

For EU acquisition, EU/non-EU reverse-charge service or import, do not replace the route with a Finnish-seller VAT-registration test. Retain the supplier invoice/VAT ID or the Customs decision, evidence that the purchaser accounts for the correct self-assessed/import VAT, and the qualifying taxable-business-use analysis. Claim the conditional amount in “Tax deductible for the tax period”. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/); [Vero purchase deductions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/deducting-vat-on-purchases/)

Vero lists, among other exclusions, private costs, commuting, entertainment, residential premises and recreational premises. Apply proportionate treatment for mixed use; do not use a blanket half-deduction rule.

**Entertainment is fully non-deductible.** No VAT deduction is allowed on goods or services bought for an entertainment purpose (for example hosting customers or business contacts at a restaurant, with or without alcohol). There is **no** half-deduction for representation in Finnish VAT; older material that states one should not be followed. The seller's rate (13.5% on the food, 25.5% on alcohol) does not change this: the buyer deducts nothing. [Vero purchase deductions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/deducting-vat-on-purchases/)

### Passenger vehicles

For an ordinary passenger car (including dual-purpose vehicles, camper vans and pickups registered as passenger cars), even modest private use makes **all** VAT non-deductible: purchase price, leasing payments, fuel, charging, maintenance, spare parts and supplies. Commuting between home and work and driving for business entertainment count as non-deductible use. Full deduction requires exclusive use for VAT-deductible business, proved by a driver's log (per vehicle, kept for at least 6 years) or equivalent records. If a full deduction was claimed and the log later shows private or other non-deductible driving, the business must reduce the deduction afterwards, paying back the VAT it was not entitled to deduct. Different rules can apply to a vehicle acquired for rental, taxi use, driving instruction or resale; vans and lorries use the documented business-use proportion. Refer a vehicle that does not fit these ordinary screens. [Vero vehicles](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/vat-on-vehicles/)

These purchase restrictions come from VAT Act §§102–102a,114,117. Directly allocate inputs to taxable/exempt/private activity first; apportion only shared qualifying inputs by an evidenced use measure. There is no universal 50% deduction. Preserve invoices or the statutory substitute document and the required self-assessed declaration; a supplier's wrongly charged foreign VAT is not Finnish input VAT. [VAT Act §§102–102a,114,117][law].

### Construction reverse charge and property investments

Under §8c, a taxable construction service or leased labour for such work is reverse charged when the business buyer nonoccasionally sells the specified construction services/property, or resells to such a buyer. The goods-only/private-consumer cases do not qualify. Confirm buyer status before invoice: seller records net consideration with buyer VAT ID and reverse-charge reference, reports the construction/scrap-sales base; buyer reports the corresponding purchase base and 25.5% tax, deducting only its qualifying share. This differs from the foreign-seller §9 route. [VAT Act §§8c,31(3)][law]; [Vero construction reverse charge][construction].

For a qualifying property investment, track original input VAT, completion year and original/current deductible-use percentages over the **10-year** adjustment period. Annual adjustment = original VAT × (original deductible fraction − current deductible fraction) / 10; a positive result repays deduction and a negative result increases it. Permanent withdrawal, deregistration or transfer can require one adjustment for remaining years, unless statutory transfer of the adjustment right/duty applies. Preserve the required transfer evidence rather than simply resetting the history to the buyer's acquisition price. [VAT Act §§120–121e][law].

## Deadlines and filing

Monthly VAT is due on the 12th of the **second month after** the period; quarterly VAT on that day in the second month after the quarter; annual VAT at the end of February following the year. Filing and payment fall on the same day; if the 12th is not a bank day, the next bank day applies. Quarterly due dates: January–March 12 May, April–June 12 August, July–September 12 November, October–December 12 February. VAT-return due dates cannot be extended. Thus March and January–March 2026 are due 12 May 2026; annual 2026 is due **1 March 2027**, since 28 February is Sunday. The allotted period and decision control; do not shorten the normal monthly filing lag to the next month. [Procedure Act §§16–17][procedure]; [Vero periods][period]; [Vero return instructions][return].

1. Lock the period ledger and reconcile every return entry to source documents. Resolve exceptions before submission.
2. In MyTax, choose the allocated period and enter the amount required in each applicable field: for domestic sales, the calculated **VAT amount** by rate; for EU purchases and imports, the purchase/import base and self-assessed VAT where the named fields require them. Select no activity only where there was no reportable VAT activity. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/)
3. Submit the VAT return by its MyTax deadline and pay any liability using the tax account/payment details in MyTax. A refund/credit must still be supported by the same reconciliation. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/)
4. If a submitted return is wrong, file a replacement VAT return for that tax period in MyTax. The corrected return replaces the earlier return, so re-enter the complete corrected period rather than only the delta. A difference of no more than €500 in the VAT amount (whatever the length of the tax period) may instead be corrected directly in the VAT amount of the next return that falls due after the error is noticed, provided it is done before that return's due date; after that date the alternative is lost. It cannot be used for data-only errors that do not affect the tax amount, including zero-rate turnover, EU tax-exempt sales and construction/scrap reverse-charge turnover; use a replacement return for every other error. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/)
5. Correct errors within 3 years from the accounting period or tax year the VAT concerns; the 3 years start at the beginning of the following calendar year. A replacement return filed after the original due date may attract a late-filing penalty, but not if 45 days or less have passed since the original due date. Pay any VAT that was under-declared. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/)
6. Preserve the submitted return, payment receipt, period reconciliation, and documents supporting zero rate, EU status, import, reverse charge and deductions.

File the EU recapitulative statement for covered goods/general-rule services separately by the **20th of the following month**, even with a longer domestic VAT period. Validate VAT IDs, transport evidence and the statement required for intra-community supply relief; a VAT return alone does not complete it. [VAT Act §§72a–72b,162][law].

## Penalties and interest

Procedure Act §§35–36 imposes EUR 3 per day for an original late return, capped at EUR 135 for that component. After 45 days add 2% of late positive tax. The **tax-based component**, not the combined daily-plus-percentage charge, is capped at EUR 15,000 per tax type/period. Replacements within 45 days have no late fee; later positive-tax or overstated-refund corrections use the 2% route without another daily component. Apply valid-reason/non-taxpayer-cause and tax-increase exclusions. [Procedure Act §§35–36][procedure].

For deficient/omitted declarations or avoidance of the late-fee rules, §§37–38 provides ordinary 10% tax increase, repeated/manifest disregard 15–50%, estimated tax 25%, specified unclear/unreasonable case 3%; where no tax is imposed the maximum is EUR 200. These are conditional routes, not a choice of lowest percentage. Overdue-tax interest is **9.5% annually for days in 2026**, from the day after due date through payment; confirm 2027 rates separately. [Procedure Act §§37–38][procedure]; [Vero interest guidance][interest].

## Cross-border points

For goods apply dispatch/installation/destination rules in §§63–63a before an exemption. Exports require the §70 transport/export evidence. A qualifying intra-community goods sale requires movement to another EU VAT state, qualifying buyer/VAT ID and the recapitulative obligations under §§72a–72b. General B2B services follow the customer's receiving establishment under §65; general B2C services follow the supplier under §66. Property services follow property location (§67); passenger transport, events, restaurant, hire and electronic services have their own §§68–69m exceptions. A foreign invoice alone neither creates Finnish VAT nor removes it. [VAT Act §§63–72b][law].

EU consumer distance goods and telecommunications/broadcast/electronic services ordinarily follow destination, with the **EUR 10,000** combined current/preceding-year exception under §69m where all its conditions hold. Crossing changes treatment from that moment; a destination election binds at least two calendar years. Do not apply the added 2027 wording of Act 597/2026 to 2026. OSS is an optional central reporting route for qualifying foreign consumer VAT; amounts declared in it stay out of ordinary domestic VAT rows. IOSS, non-Union OSS, marketplace and stock-location complications need scheme-specific work. [VAT Act §§63a,69i,69m, chapter 12a][law]; [Vero OSS][oss].

Åland lies outside the EU VAT/excise territory. Goods across its tax border, including mainland Finland, use import/export procedures and customs declarations. A VAT-registered importer calculates import base/tax and reports import fields and qualifying deduction. For 2026, allocate to the period when the **customs clearance decision was issued**, for both one-step and periodical two-step declarations; the older approval-date examples on Vero's page precede the May 2023 change and are not the current rule. Customs collects for nonregistered/nonbusiness routes. [VAT Act §§86,135a][law]; [Vero Åland imports][aland].

## Two worked examples that recompute

Assume separate net food EUR 700 and wine EUR 100 supplies in 2026 with the stated supported classifications. It does not decide a mixed supply or establish whether prices include VAT.

```oa-check
name: Finland assumed 2026 restaurant separate rates
inputs:
  net_food_price: 700
  net_wine_price: 100
  food_rate: 0.135
  wine_rate: 0.255
steps:
  food_vat: net_food_price * food_rate
  wine_vat: net_wine_price * wine_rate
  output_vat: food_vat + wine_vat
expected:
  food_vat: 94.50
  wine_vat: 25.50
  output_vat: 120
```

### Supported mixed business use

Assume a general-rule service with confirmed Finnish place of supply and purchaser liability, a verified EUR 1,000 base and supported 70% deductible use. It supplies no universal partial-exemption formula.

```oa-check
name: Finland assumed reverse charge mixed use
inputs:
  established_service_base: 1000
  vat_rate: 0.255
  established_deductible_share: 0.70
steps:
  reverse_charge_vat: established_service_base * vat_rate
  deductible_vat: reverse_charge_vat * established_deductible_share
  net_vat_cost: reverse_charge_vat - deductible_vat
expected:
  reverse_charge_vat: 255
  deductible_vat: 178.50
  net_vat_cost: 76.50
```

### Decision checks without separate arithmetic blocks

These use the rates already checked above. [Vero return instructions][return]; [Vero small-business guidance][small]; [Vero purchase deductions][deduct].

- Threshold crossed: current-year counted turnover EUR 19,700, preceding year no more than EUR 20,000. A EUR 900 general-rate sale on 20 May brings the year to EUR 20,600. Register from 20 May and report the crossing sale in full: EUR 900 × 25.5% = EUR 229.50.
- Voluntary registration: a EUR 12,000-turnover business registers on 1 February and sells EUR 1,000 at the general rate on 10 February. Output VAT is EUR 255, though annual turnover stays below EUR 20,000.
- EU goods acquisition: EUR 2,000 inventory from an EU seller, wholly taxable use. Enter the base, self-assessed VAT EUR 510 and deductible VAT EUR 510; net effect EUR 0, but the fields are not left blank.
- Import: customs base EUR 4,000 at 25.5%. Import base EUR 4,000, import VAT EUR 1,020, deductible EUR 1,020. For a tax-exempt import keep the base and leave both VAT fields blank.
- Correction: an omitted EUR 4,000 general-rate sale (EUR 1,020 VAT) needs a full replacement return, since EUR 1,020 exceeds the EUR 500 small-correction limit. A EUR 400 difference found before the next due date can go in the next return; EUR 501 cannot.
- Client entertainment: restaurant bill food EUR 200 + EUR 27 VAT (13.5%) and wine EUR 80 + EUR 20.40 VAT (25.5%). Deductible VAT is EUR 0 on both lines.
- Passenger car with occasional private trips: no VAT deduction on purchase, leasing, fuel, charging or maintenance, however large the business share.

## Ask the client first

- Who are the legal seller and buyer, where are they established, and is the customer a business with a valid VAT ID or a consumer?
- What was supplied, when was it supplied, and what invoice, contract and rate-category evidence supports that treatment?
- Did goods move across a border or enter Finland under a Customs decision, and what dispatch or import evidence is available?
- What are current and preceding calendar-year turnover, including the sales Vero includes or excludes for the €20,000 small-business exemption test?
- What is the allocated MyTax period, what was previously filed for it, and is the task an original return or a correction?
- For each purchase, what evidence shows the taxable-business-use proportion and any private, mixed or vehicle use?

## Sources

| Official source | Scope read | Read date |
|---|---|---|
| [VAT Act 1501/1993][law] | §§3,8c–9,15–16,26a,27–44,63–78,84–93,102–102a,114–121e,135a–143,162; distinguish 2027 wording | 2026-10-26 |
| [Self-assessed Tax Procedure Act 768/2016][procedure] | §§12,16–17,25,35–38 | 2026-10-26 |
| [Vero rates][rates], [return instructions][return] | 2026 rate categories and field mapping | 2026-10-26 |
| [Vero periods][period], [small-business guidance][small] | Period elections and turnover scope | 2026-10-26 |
| [Vero construction reverse charge][construction] | Buyer/seller fields | 2026-10-26 |
| [Vero Åland import procedure][aland], [OSS][oss] | Tax-border period and special-scheme boundary | 2026-10-26 |
| [Vero used-goods guidance][margin] | §5.2: ordinary return reporting of margin VAT; full special scheme not computed here | 2026-10-26 |
| [Vero purchase deductions][deduct], [vehicles][vehicles] | Preserved purchase/vehicle controls | 2026-10-23 |
| [Vero interest guidance][interest] | 2026 overdue interest | 2026-10-26 |

Not yet confirmed: transaction-specific special margin/travel/group/marketplace schemes and exceptional sector exemptions; these require their separately scoped law. Ordinary VAT is not automatically extended to those cases. Independent review and remaining publication gates are recorded in the pack README.

[law]: https://www.finlex.fi/fi/lainsaadanto/1993/1501
[procedure]: https://www.finlex.fi/fi/lainsaadanto/2016/768
[rates]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/rates-of-vat/
[return]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/
[period]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/tax-period/
[small]: https://www.vero.fi/en/detailed-guidance/guidance/48658/vat-exemption-for-small-businesses/
[construction]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/vat-in-different-lines-of-business/vat-reverse-charge-in-the-construction-sector/
[aland]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/international-commerce/value-added-taxation-of-imported-goods/%C3%A5land-islands-tax-border-and-importing-goods/
[oss]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/international-commerce/arvonlis%C3%A4veron-erityisj%C3%A4rjestelm%C3%A4t-onestopshop/
[deduct]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/deducting-vat-on-purchases/
[vehicles]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/vat-on-vehicles/
[interest]: https://www.vero.fi/en/individuals/payments/paying-taxes/interest-on-late-payments/

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

[margin]: https://www.vero.fi/syventavat-vero-ohjeet/ohje-hakusivu/48682/kaytettyjen-tavaroiden-arvonlisaverotus3/
