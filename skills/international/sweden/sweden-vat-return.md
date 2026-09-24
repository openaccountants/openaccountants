---
name: sweden-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Swedish VAT return (momsdeklaration) for a self-employed individual or small business in Sweden. Trigger on phrases like "prepare VAT return", "do the Swedish VAT", "momsdeklaration", "moms", "skattedeklaration", or any request involving Swedish VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers Sweden only and only standard-registered businesses. VAT groups, fiscal representatives, and flat-rate schemes are in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later (for workflow architecture) AND eu-vat-directive v0.1 or later (for EU directive content). ALWAYS read this skill before touching any Swedish VAT work.
version: 2.0
jurisdiction: SE
tax_year: 2026
last_updated: 2026-09-24
authored_by: OpenAccountants team
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Sweden VAT return (`momsdeklaration`) — 2026 editorial draft

**Status:** **Source-cited draft** by the OpenAccountants team. It is not accountant-authored, accountant-verified or an attestation.

Figures are for tax year 2026. This Guide is an operational method for an ordinary business registered for Swedish VAT. It prepares a supported VAT return; it does not decide a transaction-specific exemption, place of supply, partial-deduction calculation, VAT group, margin scheme, property option, IOSS/OSS election or deemed-supplier analysis.

## Key figures and return fields

| Item | Current value or route | Official source |
| --- | --- | --- |
| Swedish small-business turnover limit | SEK 120,000 under the stated Swedish-seat, current-year and prior-two-year conditions | [Skatteverket: low-turnover exemption](https://www.skatteverket.se/foretag/moms/momsregistrering/momsbefrielseforarsomsattningpahogst80000kronor.4.3152d9ac158968eb8fd1efe.html) |
| EU-goods acquisition registration screen | SEK 90,000 under the stated conditions | [Skatteverket: VAT registration](https://www.skatteverket.se/foretag/moms/momsregistrering/registreradigformoms.4.deeebd105a602bfe38000256.html) |
| Swedish VAT rates | 25%, 12% and 6%; classify the supply before choosing a rate | [Skatteverket: VAT rates](https://www.skatteverket.se/foretag/moms/saljavarorochtjanster/momssatspavarorochtjanster.4.58d555751259e4d66168000409.html) |
| Temporary food rate | 6% from 1 April 2026 for qualifying food; restaurant/café service has its own classification | [Skatteverket: VAT rates](https://www.skatteverket.se/foretag/moms/saljavarorochtjanster/momssatspavarorochtjanster.4.58d555751259e4d66168000409.html) |
| Ordinary sales base | Field 05; fields 06, 07 and 08 are withdrawals, margin-scheme base and voluntarily taxed rent | [Skatteverket: complete the VAT return](https://www.skatteverket.se/foretag/moms/deklareramoms/fyllaimomsdeklarationen.4.3a2a542410ab40a421c80004214.html) |
| Output VAT on sales/purchases | Fields 10, 11, 12 and 30, 31, 32 by the applicable rate | [Skatteverket: complete the VAT return](https://www.skatteverket.se/foretag/moms/deklareramoms/fyllaimomsdeklarationen.4.3a2a542410ab40a421c80004214.html) |
| Buyer-accounted purchase bases | Fields 20, 21, 22, 23 and 24 for the distinct EU-goods, EU-service, non-EU-service and domestic reverse-charge routes | [Skatteverket: complete the VAT return](https://www.skatteverket.se/foretag/moms/deklareramoms/fyllaimomsdeklarationen.4.3a2a542410ab40a421c80004214.html) |
| Imports and deductible input VAT | Import base 50, import VAT 60, 61 or 62, qualifying input VAT 48 | [Skatteverket: complete the VAT return](https://www.skatteverket.se/foretag/moms/deklareramoms/fyllaimomsdeklarationen.4.3a2a542410ab40a421c80004214.html) |
| EU consumer-sales threshold | EUR 10,000, stated as SEK 99,680 by the authority, subject to current/prior-year and establishment conditions | [Skatteverket: EU consumer-sales threshold](https://www.skatteverket.se/foretag/moms/sarskildamomsregler/handelmedandralander/troskelvardevidforsaljningtillickebeskattningsbarapersoneriandraeulander.4.18e1b10334ebe8bc80005545.html) |
| Representation deduction base | SEK 300 excluding VAT per person and occasion for meals/drinks, under the stated conditions | [Skatteverket: representation](https://www.skatteverket.se/foretag/moms/kopavarorochtjanster/representation.4.15532c7b1442f256baec84b.html) |
| Passenger-car hire route | 50% deduction may apply when taxable use exceeds 100 Swedish miles, 1,000 km, in a year; a separate short-term-hire route exists | [Skatteverket: cars and VAT](https://www.skatteverket.se/foretag/moms/sarskildamomsregler/bilarochmoms.4.58d555751259e4d6616800010628.html) |
| Hypothetical Case A values | SEK 100,000 and SEK 25,000 are an assumption and a derived result, not authority figures | [Skatteverket: VAT rates](https://www.skatteverket.se/foretag/moms/saljavarorochtjanster/momssatspavarorochtjanster.4.58d555751259e4d66168000409.html) |
| Hypothetical Case B values | SEK 100,000, SEK 12,000 and SEK 6,000 are assumptions or derived results, not authority figures | [Skatteverket: VAT rates](https://www.skatteverket.se/foretag/moms/saljavarorochtjanster/momssatspavarorochtjanster.4.58d555751259e4d66168000409.html) |
| Hypothetical Case C values | SEK 20,000 and SEK 5,000 are an assumption and a derived result, not authority figures | [Skatteverket: VAT rates](https://www.skatteverket.se/foretag/moms/saljavarorochtjanster/momssatspavarorochtjanster.4.58d555751259e4d66168000409.html) |
| Hypothetical Case D values | SEK 40,000 and SEK 10,000 are an assumption and a derived result, not authority figures | [Skatteverket: VAT rates](https://www.skatteverket.se/foretag/moms/saljavarorochtjanster/momssatspavarorochtjanster.4.58d555751259e4d66168000409.html) |
| Hypothetical Case E values | SEK 10,000 and SEK 2,500 are an assumption and a derived result, not authority figures | [Skatteverket: VAT rates](https://www.skatteverket.se/foretag/moms/saljavarorochtjanster/momssatspavarorochtjanster.4.58d555751259e4d66168000409.html) |

Amounts in the worked cases are labelled assumptions. They demonstrate arithmetic and return workflow; they are not published statutory figures.

## The method, step by step

1. **Confirm registration, period and reporting method.** Obtain the Swedish VAT number, registration decision, assigned period, accounting method and prior filed return. Do not create an ordinary return before resolving whether registration applies. A business with its seat in Sweden can use the automatic low-turnover exemption only when all threshold-period conditions hold. A business seated in another EU state needs the stated identification decision and EU turnover conditions; a non-EU-seat business cannot use that Swedish exemption. A threshold crossing, voluntary registration, qualifying EU acquisition, qualifying cross-border service or covered domestic reverse-charge event can change the result. [Low-turnover exemption](https://www.skatteverket.se/foretag/moms/momsregistrering/momsbefrielseforarsomsattningpahogst80000kronor.4.3152d9ac158968eb8fd1efe.html) and [registration](https://www.skatteverket.se/foretag/moms/momsregistrering/registreradigformoms.4.deeebd105a602bfe38000256.html)
2. **Build a transaction record before putting an amount in a field.** For every sale, purchase, import, withdrawal, rent or adjustment retain the invoice or equivalent evidence; legal supplier/customer identity; VAT number where relevant; goods or services description; origin/destination; supply date; accounting date; taxable base; rate; VAT shown; business purpose; customs/transport evidence; and document identifier. A bank payment confirms payment, not tax treatment or a deduction. Reconcile the record to sales ledger, purchase ledger, bank, customs information and prior corrections.
3. **Classify each sale before calculating VAT.** Establish the Swedish place of taxation and whether the item is taxable, exempt, outside scope or subject to a special scheme. For ordinary taxable domestic sales, report the base in field 05 and output VAT in 10, 11 or 12 at the actual rate. Do not use fields 06 to 08 as alternative ordinary-sales rates. Use a special field only after the specific rule and evidence are established. [Return field instructions](https://www.skatteverket.se/foretag/moms/deklareramoms/fyllaimomsdeklarationen.4.3a2a542410ab40a421c80004214.html)
4. **Apply the food transition to supported ordinary deliveries, then preserve corrections.** Qualifying food delivered before 1 April 2026 uses the former rate; qualifying food delivered from that date uses 6%. A credit or return needs an amendment invoice that identifies the original invoice and is reported under the taxpayer’s accounting method. Preserve the original invoice, amendment invoice, delivery evidence and rate calculation. This packet does not decide food-rate timing for an advance payment, EU acquisition or a disputed credit: retain those facts for a current legal-guidance review. [Food rate guidance](https://www.skatteverket.se/foretag/moms/saljavarorochtjanster/momssatspavarorochtjanster.4.58d555751259e4d66168000409.html) and [amendment invoices](https://www.skatteverket.se/foretagochorganisationer/moms/saljavarorochtjanster/fakturering.4.58d555751259e4d66168000403.html)
5. **Test input VAT independently.** Put only deductible Swedish input VAT in field 48. Confirm taxable-business use, purchaser/seller and invoice evidence, then test restrictions and mixed/private/exempt allocation. Do not place foreign VAT in field 48. Passenger cars, representation, property adjustments and mixed use require their own evidence screen. [Business purchases](https://www.skatteverket.se/foretag/moms/kopavarorochtjanster/inkoptillforetaget.4.7459477810df5bccdd480005156.html), [invoicing](https://www.skatteverket.se/foretagochorganisationer/moms/saljavarorochtjanster/fakturering.4.58d555751259e4d66168000403.html), [cars](https://www.skatteverket.se/foretag/moms/sarskildamomsregler/bilarochmoms.4.58d555751259e4d6616800010628.html), and [representation](https://www.skatteverket.se/foretag/moms/kopavarorochtjanster/representation.4.15532c7b1442f256baec84b.html)
6. **Route buyer-accounted purchases and imports separately.** Use 20 for EU goods, 21 for qualifying general-rule EU business services, 22 for qualifying general-rule non-EU services, 23 for covered domestic reverse-charge goods and 24 for covered domestic reverse-charge services. Calculate buyer-accounted VAT in 30, 31 or 32 at the rate that actually applies, then assess field-48 deduction separately. For imports, use customs evidence for 50 and calculate import VAT in 60, 61 or 62. A construction invoice belongs in 41 for the seller and 24 for the buyer only after the listed service, buyer condition and the route-specific place test are documented. [EU service purchases](https://www.skatteverket.se/foretag/moms/kopavarorochtjanster/inkopfranandraeulander/kopatjansterfranandraeulander.4.361dc8c15312eff6fd1d011.html), [construction reverse charge](https://www.skatteverket.se/foretag/moms/sarskildamomsregler/byggverksamhet/omvandbetalningsskyldighetinombyggsektorn), and [return field instructions](https://www.skatteverket.se/foretag/moms/deklareramoms/fyllaimomsdeklarationen.4.3a2a542410ab40a421c80004214.html)
7. **Route sales outside ordinary domestic treatment.** A qualifying EU goods sale belongs in 35, export goods in 36, qualifying general-rule EU business services in 39, other foreign services in 40, domestic buyer-accounted sales in 41 and specified exempt/non-consideration items in 42. Confirm customer VAT status, transport, place of supply and any EC Sales List obligation. Consumer EU distance/digital sales require the threshold/OSS test before they are included as Swedish domestic VAT. [Return field instructions](https://www.skatteverket.se/foretag/moms/deklareramoms/fyllaimomsdeklarationen.4.3a2a542410ab40a421c80004214.html), [EC Sales List](https://www.skatteverket.se/foretag/moms/deklareramoms/periodisksammanstallningforvarorochtjanster.4.58d555751259e4d661680001093.html), [EU consumer-sales threshold](https://www.skatteverket.se/foretag/moms/sarskildamomsregler/handelmedandralander/troskelvardevidforsaljningtillickebeskattningsbarapersoneriandraeulander.4.18e1b10334ebe8bc80005545.html), and [OSS](https://www.skatteverket.se/foretag/moms/deklareramoms/ossredovisningavmomsenligtdesarskildaordningarna.4.5b35a6251761e691420b58e.html)
8. **Reconcile, file, pay and correct.** Recalculate field 49 from output VAT on sales, buyer-accounted purchases and imports less supported field-48 input VAT. Reconcile every field to schedules and the tax-control account. File each assigned period; when there is no VAT to report, use the e-service zero-return route or field 49 = 0 on paper, without inventing values elsewhere. Use the registration decision/current deadline calendar. A correction is a complete replacement return for the affected period, with original return, reason, changed records and calculation retained. [When to file](https://www.skatteverket.se/foretag/moms/deklareramoms/narskajagdeklareramoms.4.6d02084411db6e252fe80008988.html), [return fields](https://www.skatteverket.se/foretag/moms/deklareramoms/fyllaimomsdeklarationen.4.3a2a542410ab40a421c80004214.html), and [corrections](https://www.skatteverket.se/foretag/moms/deklareramoms/rattaenmomsdeklaration.4.3684199413c956649b552c4.html)

## Ask the client first

- What does the registration decision say about Swedish VAT registration, accounting method and this return period?
- For each cross-border item, what was supplied, where did goods move or service occur, and what proves the counterparty’s legal/VAT status?
- What documents establish the supply date, delivery/acquisition/import date, advance receipt and any credit/return?
- Which purchases support taxable activity, which have invoices, and which have private, exempt, car, representation or property restrictions?
- Are there imports, construction services, margin transactions, voluntarily taxed rent, VAT groups, OSS/IOSS transactions or EU consumer sales?
- Has an earlier return been filed, and is the task a complete correction rather than an original return?

## Worked preparation cases

### Case A — ordinary domestic sale

**Assumptions.** A VAT-registered seller makes a supported ordinary 25% domestic sale with a SEK 100,000 VAT-exclusive base.

**Calculation and route.** SEK 100,000 × 25 ÷ 100 = SEK 25,000 output VAT. Report 100,000 in 05 and 25,000 in 10, subject to the stated classification assumptions. [Return field instructions](https://www.skatteverket.se/foretag/moms/deklareramoms/fyllaimomsdeklarationen.4.3a2a542410ab40a421c80004214.html)

### Case B — food transition at ordinary delivery

**Assumptions.** A supported eligible-food delivery of SEK 100,000 occurs on 31 March 2026. A separate supported eligible-food delivery of SEK 100,000 occurs on 1 April. The facts establish food rather than a restaurant/café service.

**Calculation and route.** The March delivery VAT is 100,000 × 12 ÷ 100 = 12,000. The April delivery VAT is 100,000 × 6 ÷ 100 = 6,000. Record the deliveries separately. Hold an advance, EU acquisition or disputed cross-transition credit for the evidence review identified in step 4. [Food rate guidance](https://www.skatteverket.se/foretag/moms/saljavarorochtjanster/momssatspavarorochtjanster.4.58d555751259e4d66168000409.html)

### Case C — EU goods purchase with supported deduction

**Assumptions.** A registered Swedish buyer acquires qualifying EU goods for SEK 20,000. The transaction is taxable at 25% and wholly for supported taxable activity.

**Calculation and route.** Report 20,000 in 20. Buyer-accounted VAT is 20,000 × 25 ÷ 100 = 5,000 in 30. Report the same 5,000 in 48 only if the deduction screen is satisfied, giving zero net effect from this one item. [Return field instructions](https://www.skatteverket.se/foretag/moms/deklareramoms/fyllaimomsdeklarationen.4.3a2a542410ab40a421c80004214.html)

### Case D — import

**Assumptions.** Customs evidence establishes a SEK 40,000 import base; goods are 25%; full taxable-business use and deduction evidence are established.

**Calculation and route.** Report 40,000 in 50 and 40,000 × 25 ÷ 100 = 10,000 in 60. Field 48 is 10,000 only if the ordinary deduction test is met. A freight payment is not the import base. [Return field instructions](https://www.skatteverket.se/foretag/moms/deklareramoms/fyllaimomsdeklarationen.4.3a2a542410ab40a421c80004214.html)

### Case E — ordinary correction

**Assumptions.** A previously filed return omitted a supported SEK 10,000 ordinary standard-rated sale.

**Calculation and route.** Omitted VAT is 10,000 × 25 ÷ 100 = 2,500. Rebuild the complete return for that period and submit the replacement return; do not file a delta-only 2,500 entry. [Skatteverket correction instructions](https://www.skatteverket.se/foretag/moms/deklareramoms/rattaenmomsdeklaration.4.3684199413c956649b552c4.html)

## When to refuse or refer

- The evidence cannot establish the tax point, place of supply, buyer/seller status, goods movement, rate classification or deductible business use.
- The return needs a partial-exemption allocation, VAT-group analysis, property adjustment, margin scheme, voluntary-tax rent calculation, triangulation, IOSS/OSS election or platform/deemed-supplier conclusion.
- A construction reverse-charge condition, car exception, representation calculation, food exclusion, voucher or amendment-invoice timing is disputed or incomplete.
- The taxpayer has no registration decision/assigned period, Customs documentation or complete correction records.

## Official sources

The captured source text and claim-level locators are retained in this packet's `sources.json` and `quality-evidence.json`. Retrieval date: 24 September 2026.

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
