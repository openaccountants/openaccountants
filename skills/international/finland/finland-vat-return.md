---
name: finland-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Finland VAT return (ALV-ilmoitus) for any client. Trigger on phrases like "prepare VAT return", "do the ALV", "fill in ALV", "Finnish VAT", "OmaVero", or any request involving Finland VAT filing. This skill covers Finland only and standard ALV registration. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Finnish VAT work.
version: 2.0
jurisdiction: FI
tax_year: 2026
last_updated: 2026-09-24
authored_by: OpenAccountants team
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Finland VAT return — 2026 editorial draft

**Status:** **Source-cited draft** by the OpenAccountants team. It is not accountant-authored, accountant-verified, or an attestation.

Figures are for tax year 2026.
## Key figures

| Figure | Value | Official source |
| --- | --- | --- |
| Registration threshold | €20,000 | [Vero small-business exemption guidance](https://www.vero.fi/en/detailed-guidance/guidance/48658/vat-exemption-for-small-businesses/) |
| General VAT rate | 25.5% | [Vero rates](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/rates-of-vat/) |
| Reduced VAT rate from 2026 | 13.5% | [Vero rates](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/rates-of-vat/) |
| Small correction threshold | €500 | [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/) |
| Former general rate (supplies up to 31 August 2024) | 24% | [Vero rates](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/rates-of-vat/) |

### Figure basis for worked cases

This table distinguishes legal figures from case-only assumptions. It does **not** present the hypothetical transaction amounts as figures published by Vero.

| Value used in this draft | Status | Legal basis or calculation route |
| --- | --- | --- |
| €100,000; €30,000 | Official turnover limits for applying for a longer VAT tax period | [Vero tax-period guidance](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/tax-period/) |
| 14%; 10%; 2025; 2026 | Official rate-transition context | [Vero rates](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/rates-of-vat/) |
| €4,000; €1,020; €800; €108; €700; €100; €94.50; €25.50; €120; €19,700; €900; €20,600; €229.50; €12,000; €1,000; €2,000; €510; €0; 70%; 30%; €255; €178.50; €76.50; €400; €501; €200; €27; €80; €20.40 | Hypothetical inputs or results in the worked cases. Each result is arithmetic from the stated input and the cited rate; the €400/€501 comparison uses the official €500 correction threshold. | [Vero rates](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/rates-of-vat/); [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/) |


**Scope:** An operational workflow for an ordinary Finnish business making taxable domestic sales and receiving ordinary business purchases. It covers registration, rate selection, VAT-return entries, ordinary EU purchase reverse charge, import reporting, input deductions, filing and corrections. The term “return” means the VAT return in MyTax. Facts are current administrative guidance retrieved on **25 September 2026**.

**Do not use this draft as an automatic classifier.** The invoice, contract, dispatch/customs evidence, customer status and MyTax tax period decide the entry. A sale does not become domestic merely because the customer name is Finnish, and a supplier’s trading name does not establish VAT treatment.

## The method, step by step

1. Collect the documents and period facts.
2. Decide registration and classify every sale/purchase route.
3. Reconcile the return, submit it and correct from the MyTax decision.

## Ask the client first

- Who are the legal seller and buyer, where are they established, and is the customer a business with a valid VAT ID or a consumer?
- What was supplied, when was it supplied, and what invoice, contract and rate-category evidence supports that treatment?
- Did goods move across a border or enter Finland under a Customs decision, and what dispatch or import evidence is available?
- What are current and preceding calendar-year turnover, including the sales Vero includes or excludes for the €20,000 small-business exemption test?
- What is the allocated MyTax period, what was previously filed for it, and is the task an original return or a correction?
- For each purchase, what evidence shows the taxable-business-use proportion and any private, mixed or vehicle use?

## 1. Required record before calculating

Create one row for each supply or purchase, retaining the original evidence.

| Capture | Why it changes the return |
| --- | --- |
| Seller and buyer legal entity, address, VAT IDs, and customer business/consumer status | Identifies domestic treatment, EU reporting and reverse-charge screens. |
| Invoice/credit note date, supply date, contract, what was supplied, currency and taxable amount | Supports the tax point, classification and euro amount. |
| Rate/category evidence for each domestic sale | 25.5%, 13.5%, 10%, zero rate and exemption have different bases and consequences. |
| Dispatch/transport evidence, import declaration and Customs decision | Supports goods leaving/entering Finland and import VAT. |
| Purchase purpose, seller VAT-registration details, receipt and private/mixed use | Determines whether input VAT is deductible and in what proportion. |
| Reporting period and prior submitted return | Determines deadline and whether a correction replaces a previous return. |

If any fact is absent, leave the transaction in a reconciliation exception and obtain the document before filing. Do not infer the rate, country, customer status or deductibility from a merchant category or prior-bookkeeping pattern.

## 2. Registration and reporting period

1. To use the Finnish small-business VAT exemption, test turnover in **both the current and preceding calendar years**. Each must be no more than **€20,000**, and the seller must not have registered voluntarily. If preceding-year turnover exceeded the threshold, do not treat a still-low current year as exempt while waiting for a new current-year crossing. Map taxable sales and the specified VAT-exempt sales Vero includes (such as intra-EU supplies, exports, financial/insurance services and property rental); exclude fixed-asset sales and the other exclusions Vero lists. Sales whose place of supply is not Finland (for example consulting sold to businesses established abroad under the general place-of-supply rule) are not Finnish turnover, and purchases, including intra-EU acquisitions, are never turnover. Do not annualise a short year; a non-calendar accounting year is split into calendar years. The exemption is **not available** to a business established outside the EU, even if it has a permanent establishment in Finland. [Vero small-business exemption guidance](https://www.vero.fi/en/detailed-guidance/guidance/48658/vat-exemption-for-small-businesses/)
2. The start-date rule is separate: if **current-year** counted turnover exceeds €20,000, register and calculate liability from the crossing sale/date. That crossing sale is taxable in full at its supported rate. [Vero registration](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/how-to-register-for-vat/)
3. A business below €20,000 may voluntarily register if it conducts business. Voluntary registration means VAT is due on all taxable sales from the registration date; it is not a registration only for selected invoices. Registration takes effect at the earliest from the date the application is received or submitted; it cannot be backdated. A business whose only activity is VAT-exempt (for example financial or insurance services) cannot register, and intra-EU acquisitions of goods can require registration even for a business not otherwise VAT-liable. [Vero small-business exemption guidance](https://www.vero.fi/en/detailed-guidance/guidance/48658/vat-exemption-for-small-businesses/); [Vero registration](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/how-to-register-for-vat/)
4. Deregistration because of lower turnover is a separate workflow. An already registered business may seek deregistration only after turnover is below €20,000 in **two consecutive calendar years**; Vero describes this as the current and preceding years. The request is not retroactive. [Vero small-business exemption guidance](https://www.vero.fi/en/detailed-guidance/guidance/48658/vat-exemption-for-small-businesses/)
5. The normal tax period is one calendar month. A business with annual turnover of no more than €100,000 may request a quarter; one with annual turnover of no more than €30,000 may request a quarter or a calendar year. Conditions: a longer period is refused if the business has failed to file VAT returns on time or failed to pay its taxes; a granted longer period starts at the beginning of the year after the request; a tax period must stay unchanged for at least 12 months; and if turnover goes over the limit for the longer period, the business must tell Vero immediately so the period is shortened (Vero can shorten it on its own decision). Until Vero's decision on a new period arrives, file on the current period. Agricultural and forestry operators, primary producers and visual artists with no other VAT-liable activity use a calendar-year period whatever their turnover. [Vero tax-period guidance](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/tax-period/)
6. File a VAT return for **every** allocated period. For a period with no VAT activity, select the no-activity declaration in MyTax rather than omitting the return. Do **not** file a no-activity return if the period had zero-rate sales on which related purchases are deductible; report them under “Turnover taxable at zero VAT rate”. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/)
7. The former VAT relief for small businesses (the reduction for accounting-period turnover under €30,000) is **abolished**: it is not available for accounting periods starting on or after 1 January 2025. Do not claim it for any 2026 period. An accounting period that began before 1 January 2025 is an old-period question; refer it. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/); [Vero small-business exemption guidance](https://www.vero.fi/en/detailed-guidance/guidance/48658/vat-exemption-for-small-businesses/)

**Deadlines (filing and payment are due on the same day).** The due date is the 12th, moved to the next business day if the 12th is a Saturday, Sunday or public holiday. VAT-return due dates cannot be extended. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/)

| Tax period | Due date |
| --- | --- |
| Month | 12th day of the second month after the month (March → 12 May) |
| Quarter | January–March → 12 May; April–June → 12 August; July–September → 12 November; October–December → 12 February |
| Calendar year | End of February of the following year. For 2026 this is 28 February 2027, a Sunday, so the due date moves to Monday 1 March 2027 (Vero's own example: 2025 was due 2 March 2026). |

A return filed after the due date attracts a late-filing penalty; late payment attracts late-payment charges. Quantifying them is out of scope here. The MyTax period and deadline shown for the business are controlling. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/)

## 3. Classify domestic sales before choosing a rate

For each Finnish domestic taxable sale, match the statutory category and retain the support for it.

| Classification | 2026 treatment | Return treatment |
| --- | --- | --- |
| Ordinary taxable domestic sale | **25.5%** general rate (from 1 September 2024; a supply made up to 31 August 2024 was at 24%, which matters when correcting an old period) | Calculate VAT from the supported tax base, then enter the **VAT amount** in “Tax on domestic sales by tax rate” at 25.5%. [Vero rates](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/rates-of-vat/); [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/) |
| Listed reduced category | **13.5%** from 1 January 2026 (14% up to 31 December 2025). Vero's examples: groceries and food, animal feed, restaurant services and meal services, books (printed and electronic), pharmaceuticals, sanitary protection products and baby diapers, sports and fitness services, admission to cultural, entertainment and sports events, passenger transport, accommodation, and, from 2026, public broadcasting services (previously 10%). **Exception:** the 13.5% rate does **not** apply to alcohol, tobacco products or the serving of alcoholic drinks; these stay at 25.5% even when sold by a restaurant or shop. | Calculate VAT from the supported tax base and enter the VAT amount in the 13.5% domestic-sales row when the category evidence fits. Do not move a 2025 supply to 13.5% merely because it is reported in 2026. [Vero rates](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/rates-of-vat/); [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/) |
| Newspapers and magazines within the statutory category | **10%** remains for newspapers and magazines (print and electronic) only. | Enter the calculated VAT amount in the 10% domestic-sales row with category evidence. [Vero rates](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/rates-of-vat/) |
| Zero-rated or exempt transaction | A separate legal classification. Zero rate (for example exports outside the EU and sales of goods to VAT-liable buyers in other EU countries) keeps the right to deduct related input VAT. Exempt sales (for example health and medical services, social services, financial and insurance services) carry no VAT and give no deduction for related purchases. | Use only the specific zero-rate/exemption line supported by Vero guidance. [Vero rates](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/rates-of-vat/); [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/) |

Current Vero instructions give examples, not a safe “industry default.” If a supply combines items, a membership, access, freight, digital content or a cross-border element, pause the rate decision and resolve the legal supply classification.

## 4. Build the return from the transaction map

Reconcile the return to the accounts, invoices, credit notes, import documents and VAT-ID checks. The following are current MyTax/Vero field labels and screens, not an assertion of permanent numeric box codes.

| Transaction after evidence check | VAT-return entry / calculation |
| --- | --- |
| Domestic taxable sale | Calculate VAT from the tax base in the workpaper, then enter the **VAT amount** by domestic rate (25.5%, 13.5% or 10%). Domestic sales can include own use, private withdrawal or other deemed domestic supply when Vero’s rules apply. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/) |
| Goods acquired from another EU country for the Finnish business | Enter “Purchases of goods from other EU countries”; calculate Finnish acquisition VAT under “Tax on purchases of goods from other EU countries”; claim the corresponding deductible VAT only if ordinary deduction conditions are met. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/) |
| General service purchased by a Finnish business from another EU business | Enter “Purchases of services from other EU countries”; calculate Finnish reverse-charge VAT under “Tax on purchases of services from other EU countries”; take input VAT only to the qualifying business-use extent. This row is **only** for services taxed under the general place-of-supply rule. A service from an EU business that is not under the general rule but is supplied in Finland (for example a service relating to Finnish real estate, passenger transport, or travel agency services) goes in “Tax on domestic sales by tax rate”, with no entry in the EU-services rows. Construction services (including leased construction workers) bought from an EU seller go in the construction/scrap-metal reverse-charge rows, not here. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/) |
| Service bought from a business established outside the EU | Calculate Finnish VAT from the supported purchase base and enter that **VAT amount** in “Tax on domestic sales by tax rate”, whether or not the service is under the general place-of-supply rule. The purchase base is **not** entered anywhere on the return. This applies to every business supplier established outside the EU, whatever its size: Vero's English page says “small business”, but the Finnish original says *elinkeinonharjoittaja* (any business operator) and the Finnish version prevails. If deductible, also enter the VAT in “Tax deductible for the tax period”. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/); [Vero return instructions in Finnish](https://www.vero.fi/yritykset-ja-yhteisot/verot-ja-maksut/arvonlisaverotus/ilmoitus-ja-maksuohjeet/) |
| Goods imported into Finland | Enter the customs-supported base in “Imports of goods from outside the EU”, VAT in “Tax on imports of goods from outside the EU”, and qualifying input VAT in “Tax deductible for the tax period”. Report it in the return for the tax period in which the customs clearance decision was issued (the date printed on the decision), and put the deduction in the same month. If the customs decision later changes, correct the return. For a tax-exempt import, retain the import-base entry and leave the import-tax/deduction entries blank. Goods moving between the Åland Islands and mainland Finland are imports/exports for VAT: refer them. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/) |
| Export/other zero-rate sale or exempt sale | Use the named treatment only after preserving conditions and evidence. Sales of goods to VAT-liable buyers in other EU countries (goods transported out of Finland) go in “Sales of goods to other EU Member States”; B2B services taxed in the buyer's EU country under the general rule go in “Sales of services to other EU Member States”; exports outside the EU and other zero-rate sales go in “Turnover taxable at zero VAT rate”. EU goods and service sales must also be reported on the VAT recapitulative statement. Sales to consumers in other EU countries are not zero-rated EU sales; whether Finnish VAT or the other country's VAT applies depends on distance-selling and OSS rules, which this Guide refers. Exempt sales with no deduction right (health, social services) are not reported as zero-rate turnover. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/) |
| Construction reverse charge, property, margin scheme, OSS/IOSS or special place-of-supply result | **Refer for a transaction-specific determination.** Do not force it into an ordinary domestic or EU-purchase row. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/) |

The ordinary net result is:

    VAT payable / refundable = output VAT and self-accounted VAT − deductible input VAT

This is a reconciliation aid. It does not establish a right to deduct, and it must be calculated from the field-level treatment above. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/)

## 5. Input VAT: apply the route-specific purchase screen

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

## 6. File, pay and correct

1. Lock the period ledger and reconcile every return entry to source documents. Resolve exceptions before submission.
2. In MyTax, choose the allocated period and enter the amount required in each applicable field: for domestic sales, the calculated **VAT amount** by rate; for EU purchases and imports, the purchase/import base and self-assessed VAT where the named fields require them. Select no activity only where there was no reportable VAT activity. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/)
3. Submit the VAT return by its MyTax deadline and pay any liability using the tax account/payment details in MyTax. A refund/credit must still be supported by the same reconciliation. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/)
4. If a submitted return is wrong, file a replacement VAT return for that tax period in MyTax. The corrected return replaces the earlier return, so re-enter the complete corrected period rather than only the delta. A difference of no more than €500 in the VAT amount (whatever the length of the tax period) may instead be corrected directly in the VAT amount of the next return that falls due after the error is noticed, provided it is done before that return's due date; after that date the alternative is lost. It cannot be used for data-only errors that do not affect the tax amount, including zero-rate turnover, EU tax-exempt sales and construction/scrap reverse-charge turnover; use a replacement return for every other error. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/)
5. Correct errors within 3 years from the accounting period or tax year the VAT concerns; the 3 years start at the beginning of the following calendar year. A replacement return filed after the original due date may attract a late-filing penalty, but not if 45 days or less have passed since the original due date. Pay any VAT that was under-declared. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/)
6. Preserve the submitted return, payment receipt, period reconciliation, and documents supporting zero rate, EU status, import, reverse charge and deductions.

## 7. Worked cases — calculations and decisions

All amounts below are net of VAT unless stated. They are operational examples, not classifications for a real invoice.

### Case A — ordinary domestic 25.5% sale

Finnish taxable consulting: €4,000. Category evidence supports general-rate domestic treatment.

    Output VAT = €4,000 × 25.5% = €1,020
    Return: €1,020 VAT in the domestic 25.5% row; retain €4,000 tax base in the workpaper.

### Case B — 13.5% supply after the rate transition

A qualifying restaurant service is supplied on 15 January 2026 for €800.

    Output VAT = €800 × 13.5% = €108
    Return: €108 VAT in the domestic 13.5% row; retain €800 tax base in the workpaper.

Variant: if €100 of the €800 bill was wine served with the meal, the wine is not at the reduced rate.

    Food: €700 × 13.5% = €94.50 (13.5% row)
    Wine: €100 × 25.5% = €25.50 (25.5% row)
    Total output VAT = €120

The date and category matter. A 2025 supply must be tested under the rate then in force; reporting date alone does not create the 2026 rate. [Vero rates](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/rates-of-vat/)

### Case C — threshold crossed

Current-year counted turnover is €19,700 and preceding-year turnover was no more than €20,000, so the business initially fits the small-business exemption. A €900 general-rate taxable sale on 20 May makes current-year turnover €20,600. Register from 20 May and report the crossing sale in full: €900 × 25.5% = €229.50 output VAT. [Vero small-business exemption guidance](https://www.vero.fi/en/detailed-guidance/guidance/48658/vat-exemption-for-small-businesses/); [Vero registration](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/how-to-register-for-vat/)

### Case D — voluntary registration

A €12,000-turnover business voluntarily registers on 1 February and makes a €1,000 ordinary taxable domestic sale on 10 February.

    Output VAT = €1,000 × 25.5% = €255

It reports the taxable sale because voluntary registration covers taxable sales from its registration date, even though annual turnover remains below €20,000. [Vero registration](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/how-to-register-for-vat/)

### Case E — EU goods purchase

A Finnish VAT-registered business buys business inventory for €2,000 from an EU seller. Evidence supports an intra-EU acquisition and wholly taxable onward use.

    Self-accounted acquisition VAT = €2,000 × 25.5% = €510
    Potential deductible input VAT = €510
    Net VAT effect = €0 if all deduction conditions are met.

Enter the purchase base and acquisition VAT in their EU-goods fields, then the deductible €510 in the input-VAT field. It is not a zero entry merely because the net effect is zero. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/); [Vero purchase deductions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/deducting-vat-on-purchases/)

### Case F — EU general service purchase, mixed use

A €1,000 ordinary general service is bought from an EU business. The business can support 70% VAT-liable use and 30% non-deductible use.

    Reverse-charge VAT = €1,000 × 25.5% = €255
    Deductible input VAT = €255 × 70% = €178.50
    Net VAT cost = €76.50

Report both the EU-service purchase base and €255 self-accounted VAT, then claim only €178.50. The 70% must come from records, not an assumed split. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/); [Vero purchase deductions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/deducting-vat-on-purchases/)

### Case G — service bought from a business outside the EU

A €1,000 general-rate service invoice is from a business established outside the EU (any size). Do not enter the €1,000 purchase base anywhere on the return. Calculate Finnish VAT at the supported domestic rate and enter €255 in “Tax on domestic sales” at 25.5%. Enter €255 in “Tax deductible for the tax period” only if business-use conditions are met. Keep the invoice showing where the supplier is established. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/); [Vero purchase deductions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/deducting-vat-on-purchases/)

### Case H — import

Customs evidence gives a €4,000 taxable import base. Goods are supported at 25.5% and wholly used in taxable business.

    Import VAT = €4,000 × 25.5% = €1,020
    Imports from outside EU base €4,000; tax on imports €1,020; tax deductible €1,020.

For a tax-exempt import, keep the €4,000 import-base entry and leave both €1,020 fields blank. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/); [Vero purchase deductions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/deducting-vat-on-purchases/)

### Case I — private use of ordinary passenger car

The company owns a passenger car used for customer visits and occasional private trips. The private use means none of the car’s VAT is deductible under the ordinary passenger-car rule: not on the purchase price or leasing payments, and not on fuel, charging or maintenance either. A proportionate claim is not available merely because business use is substantial. [Vero vehicles](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/vat-on-vehicles/)

### Case J — no activity period

There are no sales, purchases, imports or reportable VAT entries in the allocated period. Submit MyTax’s no-activity VAT return by the deadline; do not leave the period unfiled. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/)

### Case K — correction

After filing, a €4,000 ordinary domestic sale in Case A was omitted. File a replacement for that whole period that includes the €1,020 VAT for that sale and all other correct period entries. Retain the €4,000 base in the workpaper; do not send only €1,020 as a standalone correction. The €500 small-correction alternative is not available because €1,020 exceeds €500. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/)

### Case L — small correction alternative boundary

A €400 output-VAT difference is discovered before the next return’s deadline and does not concern zero-rate turnover, EU tax-exempt sales or construction/scrap reverse-charge turnover. It may be included in the next return under Vero’s limited alternative. A €501 difference or an excluded data-only error requires a replacement return. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/)

### Case M — client entertainment at a restaurant

A company hosts customers at a restaurant. The invoice shows food €200 plus VAT at 13.5% (€27) and wine €80 plus VAT at 25.5% (€20.40). Because the purchase is for entertainment, deductible input VAT is €0 on both lines. There is no half-deduction for representation. [Vero purchase deductions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/deducting-vat-on-purchases/); [Vero rates](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/rates-of-vat/)

### Case N — deadlines by tax period

A quarterly filer's January–March 2026 return and payment are due 12 May 2026. An annual filer's 2026 return and payment are due at the end of February 2027; 28 February 2027 is a Sunday, so the due date is Monday 1 March 2027. A monthly filer's March 2026 return is due 12 May 2026. None of these can be extended. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/)

### Case O — former small-business VAT relief

A sole trader registered for VAT with a calendar-year accounting period asks to claim the old small-business VAT relief (turnover under €30,000) on the last 2026 return. Refuse: the relief is not available for accounting periods starting on or after 1 January 2025. File the return with the full VAT. [Vero return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/)

## When to refuse or refer

This draft deliberately does not resolve:

- Åland treatment, customs-border facts or an Åland-specific VAT return;
- EU/third-country sales, consumer place-of-supply, OSS/IOSS and marketplace deemed-supplier rules;
- financial, insurance, health, education, property, cultural/digital and other exemption or special-rate boundary questions;
- VAT groups, margin schemes, travel schemes, second-hand goods, agriculture and construction reverse charge;
- partial exemption, fixed-establishment allocation and complex mixed use;
- a vehicle that may fit a rental/taxi/tuition/resale or commercial-vehicle exception; and
- late-payment consequences, penalties, taxable-period changes or a disputed registration effective date.

## Official sources
- [Vero: VAT registration](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/how-to-register-for-vat/)
- [Vero: VAT exemption for small businesses](https://www.vero.fi/en/detailed-guidance/guidance/48658/vat-exemption-for-small-businesses/)
- [Vero: VAT rates](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/rates-of-vat/)
- [Vero: VAT return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/)
- [Vero: VAT tax periods](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/tax-period/)
- [Vero: deducting VAT on purchases](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/deducting-vat-on-purchases/)
- [Vero: VAT on vehicles](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/vat-on-vehicles/)

Except for statutory thresholds, euro amounts in the worked cases are hypothetical arithmetic inputs. Their calculations use the legal rates and administrative routes linked above; Vero does not publish the invented example transaction amounts as official facts.

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
