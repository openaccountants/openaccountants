---
name: cross-border-vat-gst
description: "VAT, GST, and sales tax compliance for international digital businesses. Use when the user asks about: VAT, GST, sales tax, value added tax, goods and services tax, EU VAT, UK VAT, VAT OSS, One-Stop Shop, VAT registration, reverse charge, Merchant of Record, Paddle, Lemon Squeezy, Stripe Tax, digital services tax, DST, IOSS, Import One-Stop Shop, B2C digital VAT, B2B reverse charge, VIES validation, Australia GST, Singapore GST, Japan JCT, consumption tax, Canada GST/HST, US sales tax, economic nexus, SaaS tax, digital product tax, VAT compliance, VAT threshold, EU B2C sales, cross-border VAT, international VAT, when to register for VAT, VAT penalties, late registration, Mehrwertsteuer, TVA, IVA, 消費税, or any question about indirect tax compliance for businesses selling digital products or services internationally."
version: 1.2
jurisdiction: INTL
tax_year: 2026
last_updated: 2026-11-27
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: cross-country-method
---

# Cross-border VAT/GST for international digital businesses v1.2

> **Based on work by [Artin (@ar-gen-tin)](https://github.com/ar-gen-tin/panrise)**, licensed under MIT. Adapted for the OpenAccountants format.

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction. Errors can cause retrospective assessments, penalties and interest.

## Scope

Determine whether an international digital business must investigate customer-country VAT, GST or state sales tax, who accounts for it, and which country procedure to load next. Coverage: calendar 2026; historical inputs below remain attached to their original periods. Apply the linked law to the actual tax point and territory. This is an obligation screen and working-paper method, not a worldwide registration or return-filing service. It covers SaaS, downloads, e-books, courses, software, consulting, platform receipts, Merchant of Record (MoR) arrangements, related physical-goods imports, and the original seven DST comparisons. Product exemptions, detailed national returns, provincial sales taxes, income-tax nexus and customs classification need their own country analysis.

### Quick reference: customer-country tax

There is no worldwide revenue amount below which monitoring alone is safe. Start with customer location, the actual product, business/private use, the contracting seller and each jurisdiction's turnover test. The EU exception below is a place-of-supply rule, not a universal registration threshold. The following rows are screening rules with their conditions, not instructions to charge every digital sale.

| Market | 2026 screen and rate | Official basis |
|---|---|---|
| EU | B2C telecommunications, broadcasting and electronically supplied services normally follow the consumer's location. EUR 10,000 net combined qualifying TBE services and intra-Community distance goods in both the current and preceding calendar year is a narrow exception for a supplier established/resident in only one Member State; it is unavailable to an ordinary non-EU supplier. Standard rates and exceptions below. | VAT Directive arts 58, 59c, [current consolidated text](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1) |
| UK | A non-established supplier making UK taxable B2C digital supplies has no ordinary registration threshold. UK-established businesses generally test taxable turnover over GBP 90,000 in the last 12 months or expected in the next 30 days alone. Standard VAT 20%; exemptions/rate classification still matter. | [HMRC registration](https://www.gov.uk/register-for-vat), [VAT rates](https://www.gov.uk/vat-rates), [Notice 741A](https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a) |
| US | Check each state's physical/economic nexus, sourcing, product, exemption and marketplace rules separately. No national USD 100,000/200-transactions safe harbour. South Dakota removed its transaction-count limb from 1 July 2023; its sales-only test is gross sales exceeding USD 100,000 in the current or preceding calendar year. | [South Dakota DOR, 2023 legislative updates](https://dor.sd.gov/businesses/taxes/sales-use-tax/2023-legislative-updates) |
| Australia | Ordinary business AUD 75,000 relevant-turnover screen and 10% taxable-value rate only; connection/platform/reverse-charge and reporting outcomes held in §5. | [GST Act](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html) and [threshold regulation](https://www.legislation.gov.au/F2019L00417/2025-11-01/2025-11-01/text/original/epub/OEBPS/document_1/document_1.html#navPoint_8) linked in §5 |
| Singapore | Country-specific registration, rate, recipient/platform and return conclusions held in §6; original comparison figures retained there. | [IRAS starting point](https://www.iras.gov.sg/taxes/goods-services-tax-(gst)/gst-and-digital-economy/overseas-businesses); not proof of a tax outcome |
| Japan | Country-specific exemption, classification, rate, platform and return conclusions held in §7; original comparison figures retained there. | [NTA starting point](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6635.htm); not proof of a tax outcome |
| New Zealand | Foreign remote-services registration/rate/evidence/platform outcome held in §8; original figures retained there. | [IRD starting point](https://www.ird.govt.nz/gst-on-remote-services); not proof of a tax outcome |
| Canada | Specified non-resident suppliers not carrying on business in Canada and outside normal GST/HST registration test applicable non-zero-rated supplies to specified Canadian recipients exceeding CAD 30,000 over any 12-month period. Qualifying supplies deemed made by a registered platform are excluded from the underlying supplier's test. Simplified registration is conditional; normal registration may instead apply. | [CRA threshold rules](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/digital-economy-gsthst/find-out-need-register/cross-border-threshold-amounts.html), [registration regimes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/digital-economy-gsthst/register-gst-hst.html) |

## Ask the client first

Obtain these facts from the records before asking for anything missing:

1. Seller entity, actual business establishment, fixed establishments, staff/stock and countries of tax registration; supply dates and prior-period obligations.
2. Product and delivery: automated SaaS/download, human-led course, live event, bespoke advice or physical goods; contract, bundle and tax-inclusive/exclusive price.
3. Customer country and state/province, location evidence, business status and use, and any VAT/GST number and validation evidence.
4. Turnover by legal supplier, jurisdiction, product, channel and the specific current/prior/projected period, with refunds and statutory exclusions identified.
5. Platform/MoR contract, checkout seller, invoices, settlement statements and tax reports; who determines the supply terms, charges and delivery.
6. Registrations/elections, notices/audits, unpaid returns/tax and payment receipts; for goods, importer, origin, destination, value, excise status, transport and customs declaration.

## The method, step by step

### 1. Identify the supply and the person making it

Separate selling a digital service from receiving advertising income, platform fees or royalties. Do not label every internet-delivered service electronic: the EU test requires essentially automated delivery with minimal human intervention; teacher-led delivery is excluded from that electronic-service definition. Human-led virtual activities can have their own customer-location rule. [Implementing Regulation 282/2011 art 7 and Annex I](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1); [Directive arts 44, 45, 54, 58](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1).

MoR is a commercial description, not a universal tax exemption. Establish whether the intermediary actually resells as principal or is deemed supplier by the applicable law. In the EU electronic-service chain, art 9a presumes an intermediary acts in its own name, subject to the express identification and contractual/documentary rebuttal conditions; authorising the charge/delivery or setting general terms prevents that rebuttal. A business processing only payments without participating in the supply is excluded. Keep the customer sale and any separate supply to the intermediary distinct. [Implementing Regulation art 9a](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).

Paddle, Lemon Squeezy, FastSpring, Gumroad, Stripe Tax, TaxJar and Avalara remain examples from the original Guide, not verified recommendations or evidence of a particular contract's tax coverage. Compare the actual agreement, covered countries/products, excluded obligations, price, refunds and reporting. Current fee and “handles everything” claims remain individually reserved under Sources. Original vendor information links, not tax-law evidence: [Stripe Tax](https://stripe.com/tax), [Paddle](https://www.paddle.com), [Lemon Squeezy](https://www.lemonsqueezy.com).

### 2. Apply the EU place, liability and optional-scheme tests

For ordinary B2B services, the place is the business customer's receiving establishment; a qualifying non-established supplier's art 44 service is normally accounted for by that customer under art 196. A valid VIES result is evidence, not an automatic zero rate or proof that every supply qualifies. Check actual status/use, relevant fixed establishments and special rules first. Art 18 also permits other evidence where an EU number has been applied for and reasonable verification is performed; wholly private use is B2C. Invoice “Reverse charge” where legally applicable, rather than calling this a zero-rated supply. [Directive arts 43, 44, 192a, 196, 226(11a)](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Regulation arts 17–22](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1); [VIES](https://ec.europa.eu/taxation_customs/vies/).

B2C automated SaaS, downloads, software, streaming and qualifying electronic courses follow art 58, whatever the supplier's incorporation country. Human consulting to an EU consumer starts with art 45; listed professional/advisory services to a non-EU consumer instead follow art 59 at the customer, subject to applicable art 59a use-and-enjoyment rules. Streamed or virtually available educational and similar activities follow art 54 at the consumer. Check the actual service, exemption and national implementation before deciding liability. E-books and education can have reduced rates or exemptions depending on the actual supply and national law. [Directive arts 45, 47–59a](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Regulation art 7](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).

For art 59c, aggregate the supplier's qualifying cross-border TBE services and qualifying intra-Community distance goods across countries and channels, net of VAT, in both relevant calendar years. The goods must depart from the supplier's sole Member State. At equality the exception can still apply; the full supply that takes the total above the limit follows destination rules from that time, not merely the excess and not retrospectively for the whole year. A destination election binds for at least two calendar years. [Directive art 59c](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1).

OSS is optional. The Union scheme can cover qualifying intra-Community distance goods; its services limb requires an EU-established supplier supplying consumers in Member States where it is not established; non-Union OSS covers qualifying consumer services of suppliers with no EU business/fixed establishment. Apply the chosen scheme to all its covered supplies; local registration remains an alternative. OSS does not replace every domestic return or create a tax liability where an exemption applies. Check national/qualifying cross-border SME exemptions separately: EU establishment, current and preceding Union turnover within EUR 100,000, national limits/exclusions and transition rules, prior notification and confirmed EX identification/effective date must be established. Relief is not automatic. [Directive arts 284 onwards, 358a–369k](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Commission OSS overview](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en).

#### Customer-location evidence

Apply the specific presumptions first: required physical presence at a hotspot/booth, intra-EU passenger-transport departure, fixed-line installation, mobile SIM country, or decoder/viewing-card location. Otherwise art 24b(d) requires two non-contradictory items: billing address, IP/geolocation, bank details, SIM/MCC, fixed-line location or other commercially relevant information. Billing address does not automatically outrank contradictory evidence.

For that residual rule only, supplies from an EU business/fixed establishment with relevant VAT-exclusive value not exceeding EUR 100,000 in both current and preceding calendar years may use one art 24f(a)–(e) item supplied by another participant, neither supplier nor customer. This concession ends on crossing and is separate from the EUR 10,000 place rule. Supplier rebuttal of the specific art 24a/24b(a)–(c) presumptions requires three non-contradictory items; authorities may rebut misuse or abuse. Unresolved location is not a permission to pick the cheaper rate. [Regulation arts 24a, 24b, 24d, 24f](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).

#### EU standard rates retained from the original

These are standard rates for a taxable supply classified at that rate, not a statement that every e-book, course or digital product bears the standard rate.

| Country | Standard rate, 2026 | Official source |
|---|---|---|
| Germany | 19% | [EU official national-rate table](https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm) |
| France | 20% | [EU official national-rate table](https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm) |
| Netherlands | 21% | [EU official national-rate table](https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm) |
| Spain | 21% | [EU official national-rate table](https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm) |
| Italy | 22% | [EU official national-rate table](https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm) |
| Ireland | 23% | [EU official national-rate table](https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm) |
| Sweden | 25% | [EU official national-rate table](https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm) |

### 3. Apply the UK rule independently

The UK is a separate jurisdiction from EU OSS. Determine the customer's location and whether the service is electronic or a different service under Notice 741A; check whether a platform is the supplier. An unregistered supplier with no UK business/fixed establishment making taxable supplies in its business can require registration from the first supply, or on reasonable grounds to expect taxable supplies in the next 30 days; the prospective going-concern-transfer exception needs its own review. [VATA Schedule1A paras1–2](https://www.legislation.gov.uk/ukpga/1994/23/schedule/1A/paragraph/1). Supplies wholly exempt or outside scope are different, and HMRC permits a conditional registration exemption for a NETP whose taxable supplies are all zero-rated. The domestic threshold is not available simply because a foreign seller has obtained a UK number. [HMRC registration](https://www.gov.uk/register-for-vat); [Notice 741A, services and digital supplies](https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a).

### 4. Screen US states individually

US sales/use tax operates at state/local level. Physical connections can create obligations independently of economic turnover; South Dakota identifies offices, property, sales staff and company vehicles as examples. Establish nexus before deciding whether the particular product and location are taxable; marketplace collection and exemption certificates are separate questions. A purchaser may owe use tax even where the seller does not collect. [South Dakota DOR](https://dor.sd.gov/businesses/taxes/sales-use-tax/2023-legislative-updates); [California purchaser use tax](https://cdtfa.ca.gov/taxes-and-fees/use-tax/business-use.htm).

| Original state comparison | Correct product-specific screen | Official source |
|---|---|---|
| Texas | Taxable data-processing receipts have a 20% exemption; the remaining 80% is subject to tax. Merely using a computer in a professional service is different. Classify the actual SaaS service and applicable exemptions first. | [Texas Comptroller, Tax Code §151.351](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm), [Comptroller data processing](https://comptroller.texas.gov/taxes/publications/96-259.php) |
| New York | Prewritten software, including a licence to access it remotely, can be taxable; custom software and reasonable separately stated qualifying services have different rules. User location affects sourcing. | [NY DTF, TB-ST-128](https://www.tax.ny.gov/pubs_and_bulls/tg_bulletins/st/computer_software.htm) |
| Pennsylvania | Canned software can be taxable when remotely accessed or licensed as SaaS. Custom software is different; associated services and out-of-state users need the authority's detailed analysis. | [PA Revenue, canned software/digital goods](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/sales-use-and-hotel-occupancy-tax/canned-computer-software-digital-goods) |
| California | Electronic-only transfers are generally not taxable. For nontaxable transferred prewritten software, no-additional-charge manuals do not themselves tax the software; separately charged manuals are taxable. Other tangible copies/backups can change treatment; classify the actual supply. | [Regulation1502(f)(1)(D)](https://cdtfa.ca.gov/lawguides/vol1/sutr/1502.html), [CDTFA publication109](https://cdtfa.ca.gov/formspubs/pub109/nontaxable-sales.htm) |
| Georgia | Rule 560-12-2-.118 excludes defined SaaS: online subscription rather than bought/installed software. A download-and-retain digital subscription can confer permanent use even if continued payment is required, so not every subscription is excluded. | [Georgia rules, .118(2)–(5)](https://rules.sos.ga.gov/gac/560-12-2) |
| Missouri | The sale of SaaS is not subject to tax under the cited rule; property the provider uses can still bear sales/use tax. | [12 CSR 10-109.050(3)(I)](https://www.sos.mo.gov/cmsimages/adrules/csr/current/12csr/12c10-109.pdf) |

Washington's product-specific outcome and the original national state counts are explicitly non-usable under the holds below. Check this point with one of our partner accountants. Software/payment automation does not establish nexus, file a return or remove an existing registration.

### 5. Australia: bounded comparison

For an ordinary for-profit business, the registration turnover amount is AUD 75,000. Test relevant Australia-connected GST turnover: current turnover at/above the amount unless the Commissioner is satisfied projected turnover is below it, or projected turnover at/above it. Check whether a qualifying marketplace bears responsibility instead. Standard GST on an ordinary taxable supply is 10% of taxable value. [GST turnover and threshold](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html#navPoint_289); [threshold regulation](https://www.legislation.gov.au/F2019L00417/2025-11-01/2025-11-01/text/original/epub/OEBPS/document_1/document_1.html#navPoint_8); [ATO relevant-turnover/platform screen](https://www.ato.gov.au/api/public/content/0-f0676a52-df3e-4d50-a25e-940c2103c562); [rate, GST Act s 9-70](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html).

**Non-usable Australian outcomes:** the original Australian-consumer digital-supply connection, registered-business-use treatment, standard versus simplified registration/BAS, no-input-credit simplified route, and Divisions 83/84 reverse charge require the country Guide and actual supplier/platform/recipient facts. The earlier s 84-5 items 1/2 versus 3/5 distinction and enterprise/non-solely-creditable purpose are not a supplied filing decision here. Check this point with one of our partner accountants.

### 6. Singapore: country handoff

**Non-usable Singapore comparison inputs:** SGD 1 million global/domestic and SGD 100,000 local OVR figures; 9% and historical 8%/1 January 2024; remote-service/low-value-goods aggregation, digital/non-digital expansion from 1 January 2023, calendar-year/next-twelve-month tests and exceptions, registered-recipient/location evidence, platform liability, voluntary registration and pay-only/no-input-credit route. Do not use these retained figures or conditions to decide a 2026 registration, charge or return without the country proof. Check this point with one of our partner accountants. [IRAS country starting point](https://www.iras.gov.sg/taxes/goods-services-tax-(gst)/gst-and-digital-economy/overseas-businesses).

### 7. Japan: country handoff

**Non-usable Japan comparison inputs:** JPY 10 million base-period figure, specified-period/new-business/capital/foreign-business and qualified-invoice exceptions; 10%/8% standard/reduced claims; electronic-service B2B/B2C contractual classification and reverse charge (including the 95% issue); designated-platform/consideration change from 1 April 2025. Neither the original “regardless of revenue” statement nor these retained alternatives supplies a current tax conclusion. Check this point with one of our partner accountants. [NTA country starting point](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6635.htm).

### 8. New Zealand and Canada: recipient and platform boundaries

**Non-usable NZ remote-services inputs:** NZD 60,000 relevant past/expected-next-twelve-month supplies, 15% rate, two non-conflicting residence items, GST-number/NZ-business-number or registration statement, business-use exclusion, marketplace supplier and quarterly remote/low-value/listed-service route. These retained comparisons do not establish a foreign seller's actual registration, tax or filing frequency. Check this point with one of our partner accountants. [IRD country starting point](https://www.ird.govt.nz/gst-on-remote-services).

Canadian simplified registration applies to a specified non-resident supplier (not carrying on the supplies in a Canadian business and not normally registered), with relevant threshold amounts exceeding CAD 30,000 over any qualifying twelve-month period including the time tested, including reasonable expectations. It is not just a trailing-year cash-receipts test. The electronic application is due by the first day registration is required. Normal registration may apply instead. Exclude qualifying supplies legally deemed made by a registered distribution platform from the underlying supplier's threshold. [ETA ss 211.1, 211.12](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-211.12.html); [platform rule, s211.13](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-211.13.html).

A specified Canadian recipient has not provided satisfactory evidence of normal GST/HST registration and has usual residence in Canada. The Canadian-residence test ordinarily requires two Canadian indicators, no more than one foreign indicator, or Canadian indicators reasonably more reliable where both sets have two or more; a Minister-allowed alternative can apply. For province, apply the home/business-address hierarchy and then the statutory indicator rules; conflicting province evidence needs those rules, not a guess from the payment address. Ordinary specified digital supplies not related to real property follow that established residence province. Check the specified-supply exclusions (foreign-only use/foreign property, foreign litigation and other statutory exclusions) before charging. [ETA s211.1 definitions](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-211.1.html), [s211.11 evidence](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-211.11.html), [s211.14 place](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-211.14.html).

Simplified registration does not allow ordinary input tax credits; specified deduction/refund exceptions are separate. Use the combined HST rate once, with no extra “provincial HST”. Separate PST/QST remains a country/province handoff. [ETA s211.17](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-211.17.html); [CRA charge/collect](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/digital-economy-gsthst/charge-collect/cross-border.html).

| Taxable specified Canadian digital supply | Rate applicable in 2026 | Official source |
|---|---|---|
| Alberta, British Columbia, Manitoba, Northwest Territories, Nunavut, Quebec, Saskatchewan, Yukon | 5% GST; separate provincial taxes are outside this row | [CRA current rate list](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/digital-economy-gsthst/charge-collect/cross-border.html) |
| Ontario | 13% combined HST | [CRA current rate list](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/digital-economy-gsthst/charge-collect/cross-border.html) |
| Nova Scotia | 14% combined HST from 1 April 2025, subject to transition rules | [CRA current rate/decrease notice](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate.html) |
| New Brunswick, Newfoundland and Labrador, Prince Edward Island | 15% combined HST | [CRA current rate list](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/digital-economy-gsthst/charge-collect/cross-border.html) |

Use the applicable supply/tax point and transition conditions; the older Nova Scotia illustration is not the 2026 rate authority.

### 9. Screen DST and successor taxes separately

These taxes are separate from VAT/GST. Identify the defined activity, group aggregation, local attribution and taxable revenue/profit proxy before computing anything. Selling one's own SaaS does not by itself establish liability for every DST. The original assertion that high thresholds make DST irrelevant to all small businesses ignores group membership and different national bases.

| Original country row | Current screen, 2026 | Official source |
|---|---|---|
| UK | Normal DST 2% on UK digital-services revenues above the GBP 25 million annual allowance, when group in-scope worldwide revenues exceed GBP 500 million and UK revenues exceed GBP 25 million. Covers defined social-media, search and online-marketplace activities; short accounting periods proportionately reduce the thresholds and allowance; alternative-basis and qualifying cross-border relief can alter liability. | [Finance Act2020 ss39–48](https://www.legislation.gov.uk/ukpga/2020/14/part/2), [HMRC registration scope](https://www.gov.uk/guidance/check-if-you-need-to-register-for-digital-services-tax), [DST01200](https://www.gov.uk/hmrc-internal-manuals/digital-services-tax/dst01200) |
| France | 3% on the nationally weighted taxable consideration for defined digital intermediation/targeted advertising. Prior-calendar-year group/business taxable-service receipts must exceed BOTH EUR 750 million worldwide and EUR 25 million nationally. | CIBS arts L453-45–74, particularly 46, 47, 52, 64–66, 70, [current code](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000048626177) |
| Italy | 3% of taxable digital-service revenue; previous-calendar-year worldwide total revenue at least EUR 750 million, individually or as a group, plus Italian in-scope receipts. The old EUR 5.5 million Italian threshold was removed from 2025. Use Law 145/2018 as amended for 2026; Decree 174/2024 was deferred to 2027. | Law 145/2018 art 1(35)–(50), [current law](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=18G00172&atto.dataPubblicazioneGazzetta=2018-12-31&bloccoAggiornamentoBreadCrumb=true&classica=true&dataVigenza=&generaTabId=true&qId=&tabID=0.9037336842842527&tipoDettaglio=vigente&title=lbl.dettaglioAtto); Law 207/2024 art 1(21)–(22), [threshold amendment](https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticoloDefault/originario?atto.codiceRedazionale=24G00229&atto.dataPubblicazioneGazzetta=2024-12-31&atto.tipoProvvedimento=LEGGE); DL 200/2025 art 4(2), [2027 deferral](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.articolo.numero=4&atto.codiceRedazionale=25G00213&atto.dataPubblicazioneGazzetta=2025-12-31) |
| Spain | 3%; previous-year net turnover exceeding EUR 750 million AND taxable digital-service revenues attributable to Spain exceeding EUR 3 million, with group/annualisation rules. Defined online advertising, intermediation and data transmission, with art 6 exclusions. | Law 4/2020 arts 4–11, [consolidated BOE](https://www.boe.es/buscar/act.php?id=BOE-A-2020-12355) |
| Turkey | 5% for 2026 (published 2.5% from 2027; old 7.5% is historical). Law7194 art4(1) exempts where prior-accounting-period covered receipts are **below either** TRY20million locally or EUR750million worldwide; consolidate group covered receipts. Subject to statutory exclusions/documentation, current-period loss of exemption tests both limits exceeded at quarter-end cumulatively, with liability from the fourth following tax period. Two consecutive periods below either limit restore exemption in the next period. The summary table’s “not exceeding” wording is not substituted for the law. Exact-equality and case-specific commencement outcomes are non-usable here: Check this point with one of our partner accountants. | [Official law7194 arts1–6](https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Ffileadmin%2Fuser_upload%2FKanunlar%2F7194.pdf), [2026/2027 rate note](https://cdn.gib.gov.tr/api/gibportal-file/file/getFile?objectKey=DUYURU%2FUNIVERSAL%2F2025%2FCK10767_abn.pdf) |
| India | **Non-usable:** original Equalisation Levy 2%, no-global-threshold, INR 2 crore (~USD 240,000) and quarterly-registration/filing claim; earlier revision’s before-1-August-2024 supply cutoff and 1-April-2025 sunset need dated country proof before any current or historical decision. Check this point with one of our partner accountants. | [Income Tax Department starting point](https://www.incometaxindia.gov.in/equalisation-levy3); not a supplied tax outcome |
| Kenya | **Non-usable:** old DST 1.5%/KES 0/no-global-threshold/all-digital-services and quarterly filing; later SEPT comparison (27 December 2024, 10% deemed profit ×30%=3%, PE/ss9(2)/10/airline exclusions, s12E(5) following-month20th), regulations and iTax mapping need country proof. Arithmetic alone does not establish liability. Check this point with one of our partner accountants. | [KRA 2026 Act starting point](https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf); not a supplied tax outcome |

India/Kenya revenue-based enforcement bands are held below. No small-revenue enforcement assurance is supplied.

### 10. Physical goods: separate sale VAT, import VAT and customs duty

Digital delivery can be immediate; goods involve shipping/customs. Complexity is fact-dependent, not automatically “medium” for services and “high” for goods. A goods sale's VAT place can depend on location, dispatch, distance-sale or installation rules; import VAT is a distinct event. Digital services can also interact with income taxes, and physical-goods marketplaces can enter DST scope, so “DST only digital/customs only physical” is not a complete tax analysis. [Directive arts 30–61](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [HMRC DST marketplace scope](https://www.gov.uk/guidance/check-if-you-need-to-register-for-digital-services-tax).

The EU abolished the former EUR 22 low-value import VAT relief from 1 July 2021; specific import exemptions still exist. IOSS is optional for eligible distance sales of imported goods in consignments of intrinsic value not exceeding EUR 150, excluding excise products. A non-EU seller normally needs an intermediary unless the mutual-assistance exception applies. The IOSS tax point is acceptance of payment. With a valid IOSS identification number provided no later than lodging the import declaration, the import is exempt from import VAT; sale VAT is accounted for through IOSS. Without IOSS, standard import rules or qualifying special collection arrangements apply, according to the liable importer and declaration, not invariably a carrier collecting from the buyer. [Directive arts 143(1)(ca), 201, 369l–369x](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Commission OSS explanation](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en); [Commission EUR 22 abolition and 1 July 2021 date](https://vat-one-stop-shop.ec.europa.eu/index_en).

| Customs issue | Dated current rule | Official source |
|---|---|---|
| EU former EUR 150 duty relief | Removed from 1 July 2026. A temporary EUR 3 per item charge applies to qualifying consignments of intrinsic value not exceeding EUR 150 from 1 July 2026 to 1 July 2028, under the IOSS/import-exemption limb or the amended postal-consignment limb; the latter excludes specified preferential measures. “Postal” has the amended distance-goods meaning, not just a traditional post-office carrier. | Regulations 2026/382 arts 1–3 and 2026/1022 art 1, [original duty act](https://publications.europa.eu/resource/cellar/2ae65d0b-0c6b-11f1-8870-01aa75ed71a1.0006.03/DOC_1), [amending act](https://publications.europa.eu/resource/cellar/3b9f822b-74e8-11f1-bf5e-01aa75ed71a1.0006.03/DOC_1) |
| EU item/base | An item is one or more goods sharing tariff classification, description and origin where provided, within the applicable declaration dataset; not universally one parcel or physical piece. Duty recovered from the buyer forms part of the sale consideration under IOSS; standard import VAT bases include customs duty. | [Regulation 2026/1022](https://publications.europa.eu/resource/cellar/3b9f822b-74e8-11f1-bf5e-01aa75ed71a1.0006.03/DOC_1), [Commission 6 October 2026 VAT guidance, pp 1–4](https://vat-one-stop-shop.ec.europa.eu/document/download/3086db0e-7b4a-4202-9f38-d32bd774f5a8_en?filename=VAT+treatment+of+the+EUR+3+customs+duty+and+of+the+EUR+2+Customs+Union+handling+fee+%E2%80%93+Revised+version+06+October+2026.pdf) |
| US former Section 321 relief | The former USD 800 per-person/day rule is unavailable for ordinary 2026 commercial imports. Following the 2025 executive suspension, CBP independently suspended this exemption indefinitely for postal and non-postal merchandise from 24 June 2026. Separate gift/traveller relief needs its own statutory review; no eligibility conclusion is supplied here. Determine actual entry treatment and duties for the goods; the historical 50 USC 1702(b) executive-order carve-out must not be assumed to exempt goods from these regulations. | 19 CFR 10.151(b), [non-postal IFR](https://www.govinfo.gov/content/pkg/FR-2026-06-24/html/2026-12670.htm); 19 CFR 145.31(b), [postal IFR](https://www.govinfo.gov/content/pkg/FR-2026-06-24/html/2026-12669.htm) |

### 11. Aggregate the actual supplier's platform receipts

Reconcile YouTube, Patreon, Substack, Gumroad, Paddle, Stripe and AdSense receipts to contracts and invoices. Aggregate qualifying supplies of the same supplier under the relevant jurisdiction's rule, not all platform payouts indiscriminately. EU art 59c uses qualifying TBE/distance-goods turnover across channels, not all income or a separate allowance per platform. For legally deemed/reselling platforms, analyse the separate supplier-to-platform supply; the consumer sale may be the platform's. A payment processor's involvement alone is insufficient. [Directive arts 28, 58, 59c](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Regulation art 9a](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1). The original blanket brand-by-brand responsibility claims are reserved under Sources.

## Boundary and exception table

| Fact that changes the answer | Required treatment | Official basis |
|---|---|---|
| Low revenue but foreign supplier | Test the actual local rule; neither the old revenue-strategy bands nor the EU threshold gives worldwide relief. | [UK first taxable supply](https://www.gov.uk/register-for-vat), [EU art 59c](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1) |
| Business number supplied | Establish recipient status, use, service type and relevant establishment; keep validation and supporting evidence. | [EU Regulation arts 17–22](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1), [IRAS OVR recipient rules](https://www.iras.gov.sg/taxes/goods-services-tax-(gst)/gst-and-digital-economy/overseas-businesses) |
| Live teaching/advice bundled with videos | Identify the actual supply/components; do not apply automated-service treatment just because delivery is online. | [EU Regulation art 7/Annex I](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1) |
| MoR adopted after unregistered sales | Separate prospective contracting changes from existing obligations; a new platform arrangement does not determine the historical seller or erase earlier VAT. | [EU Directive arts 28, 63, 193, 213](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1), [HMRC late registration](https://www.gov.uk/register-for-vat) |
| Simplified foreign registration | Do not assume input tax credits, a domestic form or every local supply is covered. | [IRAS OVR](https://www.iras.gov.sg/taxes/goods-services-tax-(gst)/gst-and-digital-economy/overseas-businesses), [CRA simplified return](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/digital-economy-gsthst/file-return.html), [ATO route distinction](https://softwaredevelopers.ato.gov.au/GSTintangibles) |

## Worked cases

### Case 1: the EU crossing supply, not just the excess

Assume a German sole-establishment supplier of fully automated, standard-rated software, no destination election or exemption, only qualifying cross-border TBE supplies, prior-calendar-year total EUR 9,000. Current-year sales of EUR 9,400 direct plus EUR 400 through an agent that does not become the supplier total EUR 9,800. The next French consumer sale is EUR 400 net. It takes the total to EUR 10,200, so the whole crossing sale follows France: EUR 80 VAT and EUR 480 gross. Taxing only the EUR 200 excess would wrongly yield EUR 40. If instead this sale kept the qualifying total within the threshold, origin taxation would give EUR 76 at Germany's standard rate, absent an election. Optional OSS versus local registration changes the reporting route, not France's tax due on the crossing sale. [Directive arts 58, 59c](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [official rates](https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm).

```oa-check
name: EU qualifying threshold and full crossing supply
inputs:
  direct_sales: 9400
  agent_sales: 400
  next_sale: 400
  threshold: 10000
  france_rate: 0.20
  germany_rate: 0.19
steps:
  before: direct_sales + agent_sales
  after: before + next_sale
  excess: max(0, after - threshold)
  destination_vat: next_sale * france_rate
  destination_gross: next_sale + destination_vat
  erroneous_excess_only_vat: excess * france_rate
  origin_counterfactual_vat: next_sale * germany_rate
expected:
  before: 9800
  after: 10200
  destination_vat: 80
  destination_gross: 480
  erroneous_excess_only_vat: 40
  origin_counterfactual_vat: 76
```

### Case 2: Canadian province and inclusive-price reconciliation

Assume a registered simplified supplier makes a taxable digital sale to a specified Nova Scotia consumer in 2026, with reliable usual-residence evidence, no exemption, and no transition issue. On CAD 1,000 net, combined HST is CAD 140 and gross CAD 1,140. If CAD 1,000 is instead the agreed tax-inclusive total, HST is CAD 122.81 and net CAD 877.19. The same net sale to Ontario bears CAD 130 HST, not Nova Scotia's amount. The supplier must establish the province before choosing the rate. [CRA current rates/place rules](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/digital-economy-gsthst/charge-collect/cross-border.html); [dated Nova Scotia decrease](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate.html).

```oa-check
name: Canada Nova Scotia 2026 versus Ontario and inclusive pricing
inputs:
  price: 1000
  nova_scotia: 0.14
  ontario: 0.13
steps:
  ns_hst: price * nova_scotia
  ns_gross: price + ns_hst
  inclusive_hst: round(price * nova_scotia / (1 + nova_scotia), 2)
  inclusive_net: price - inclusive_hst
  ontario_hst: price * ontario
expected:
  ns_hst: 140
  ns_gross: 1140
  inclusive_hst: 122.81
  inclusive_net: 877.19
  ontario_hst: 130
```

## When to refuse or refer

Do not produce a filing-ready amount where the legal seller, product, customer location/status, turnover period or historical effective date is unresolved. Refer multi-country arrears, disputed classifications, platform contracts, tax-inclusive historic pricing and customs origin/classification to an appropriate specialist. There is no verified EUR 5,000 referral threshold or universal engagement fee in this Guide.

Do not use a valid VAT number as automatic zero rating, the EU threshold for a non-EU seller, a national US nexus shortcut, the held India/Kenya current or historical comparisons, a former US de minimis amount, or an unconfirmed fee/penalty discount. Do not claim accountant approval, registration, a filed return, authority contact or payment without actual evidence. This method produces an obligations schedule and a review brief, not an executed filing or contact instruction.

### Penalties and remediation

Penalties and interest require the applicable country/state, period, failure and behaviour. The old EU-wide minimum/maximum and voluntary-disclosure percentages are not reliable legal rules. HMRC distinguishes unprompted/prompted disclosures using whether the taxpayer had reason to believe discovery was imminent; starting a check does not invariably eliminate every reduction or an unrelated unprompted disclosure. Do not promise a discount or immunity. [HMRC CC/FS11, disclosure and penalty factors](https://www.gov.uk/government/publications/compliance-checks-penalties-for-failure-to-notify-ccfs11/compliance-checks-penalties-for-failure-to-notify-ccfs11).

For remediation, preserve sales, contracts, location evidence, returns and correspondence; reconstruct liability from the legally applicable effective dates and tax points, not an assumed universal threshold-crossing date. Prepare tax, interest and any penalty separately. Assess correction/disclosure eligibility and the right registration date before any submission/contact; obtain professional review and the user's authority for the external action. Determine lawful prospective sales arrangements rather than automatically ordering all sales to stop or treating a new MoR as a cure for past liability. Late UK registration, for example, can require VAT for sales since registration should have begun. [HMRC registration/arrears](https://www.gov.uk/register-for-vat); [CC/FS11](https://www.gov.uk/government/publications/compliance-checks-penalties-for-failure-to-notify-ccfs11/compliance-checks-penalties-for-failure-to-notify-ccfs11); [EU Directive arts 63, 193, 213](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1).

## Filing and payment

Use this calendar only after establishing the actual registration scheme and period. It is not a substitute for the taxpayer's account, national form/field mapping, extension decision or payment receipt.

| Regime | Frequency and ordinary deadline | Official source |
|---|---|---|
| EU Union/non-Union OSS | Calendar quarters; return and payment by end of following month, including nil returns. IOSS is monthly, with the same following-month rule. Use the Member State of identification's actual portal and issued return/payment reference. | Directive arts 364–367, 369f–i, 369s–v, [law](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1), [Commission declare/pay](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/declare-and-pay-oss_en) |
| UK VAT | Usually every three months; online return/payment ordinarily one calendar month plus seven days after period end. Annual accounting and other arrangements need their own calendar; payment must reach HMRC by its deadline. | [HMRC Sending a VAT Return](https://www.gov.uk/submit-vat-return) |
| Australia GST | **Non-usable filing comparison:** original quarterly BAS/28-days claim; later simplified-quarterly versus standard route and 28 October/28 February/28 April/28 July dates/extensions require the actual country scheme. Check this point with one of our partner accountants. | Country handoff under §5 |
| Singapore OVR | **Non-usable filing comparison:** quarterly/one month after accounting period, ordinary approved-period and payment-arrangement alternatives require country proof. Check this point with one of our partner accountants. | Country handoff under §6 |
| Japan JCT | **Non-usable filing comparison:** annual/semi-annual, corporate two months/extensions, individual 31 March and prior-liability-based interim filings require country proof; none is a universal calendar. Check this point with one of our partner accountants. | Country handoff under §7 |
| Canada simplified GST/HST | Calendar quarters; return within one month after quarter end, using the simplified GST/HST return through GST/HST NETFILE. Net positive tax is remitted. Normal registration has its own annual/quarterly/monthly reporting calendar and must be routed separately. | [CRA digital return obligations](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/digital-economy-gsthst/file-return.html), [normal reporting periods](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html) |
| US state sales tax | State-assigned periods may be monthly, quarterly or annual; no common national filing deadline. Obtain the actual state account/return instructions before setting a date; the specific filing outcome is non-usable here. Check this point with one of our partner accountants. | [South Dakota DOR state-specific starting point](https://dor.sd.gov/businesses/taxes/sales-use-tax/2023-legislative-updates) |
| Kenya SEPT | **Non-usable filing comparison:** s12E(5) twentieth of following month, regulations and live return fields require country proof. Check this point with one of our partner accountants. | Country handoff under §9 |

For each handoff, provide the established seller/registration regime, taxable base by country and rate, evidence and exclusions, actual period, proposed due date, and missing national form/portal/payment fields. The country filing Guide must establish those fields and the post-submission acknowledgement/payment reference before anyone represents the work as completed.

## Completion checklist

- Reconcile the seller's receipts across all platforms to the correct legal supplies; distinguish consumer proceeds from a B2B supply to a platform.
- Record customer-country/state evidence, recipient status/use, product classification and relevant establishment for each branch.
- Apply the exact local turnover definition and period, including platform treatment, refunds, prior-year and projected tests.
- Record tax-inclusive/exclusive pricing, chosen schemes/elections, rate classification, exemptions and customs treatment separately.
- Produce an obligations calendar and country handoffs; list unresolved figures without estimating them into tax due.
- Keep the source/read scope and effective date beside each conclusion, and retain actual filings/payments/approvals as separate evidence.

## Sources

New operative passages read on 2026-11-27: [Canadian electronic-commerce definitions, threshold and linked sections](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-211.12.html); [UK non-established registration](https://www.legislation.gov.uk/ukpga/1994/23/schedule/1A/paragraph/1); [UK DST Part2](https://www.legislation.gov.uk/ukpga/2020/14/part/2); [French DST section](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000048626177); [Spanish DST law](https://www.boe.es/buscar/act.php?id=BOE-A-2020-12355); [Italian DST law, amended art1(35)–(50)](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=18G00172&atto.dataPubblicazioneGazzetta=2018-12-31&tipoDettaglio=vigente); [Turkish DST law arts1–6](https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Ffileadmin%2Fuser_upload%2FKanunlar%2F7194.pdf); [US non-postal customs operative rule](https://www.govinfo.gov/content/pkg/FR-2026-06-24/html/2026-12670.htm) and [postal rule](https://www.govinfo.gov/content/pkg/FR-2026-06-24/html/2026-12669.htm). Other new authority passages are linked beside their statements. Unchanged EU, UK, Canadian rate/credit, US state and bounded Australian proof was reused after applicability checks on 2026-11-27; this is not a claim of a fresh page read. Country starting points attached to holds are routing links only.

Not yet confirmed: no usable tax or commercial conclusion is supplied for the following bounded holds. Check this point with one of our partner accountants.

The linked law/authority passages support the usable screens above. Vendor links are product context only. The following retained historical inputs are **non-usable**: they confer no tax treatment, threshold, fee quote, enforcement assurance or permission to file. Obtain the specific country/contract decision before using one.

- **Revenue strategy A:** “<EUR 10,000 from any single jurisdiction, monitor only, below most thresholds, cost USD 0.” No worldwide legal basis; contradicted by the UK first-taxable-supply and narrow EU rules above. Check this point with one of our partner accountants.
- **Revenue strategy B:** “EUR 10,000–100,000 global customers: Paddle/Lemon Squeezy handle all tax, cost 5–10%.” No current customer contract or fee proof was obtained; no legal revenue band supports this recommendation. Check this point with one of our partner accountants.
- **Revenue strategy C:** “>EUR 100,000: self-register top 2–3 markets plus Stripe Tax, accounting USD 2,000–5,000/year.” Neither market count nor budget is an established legal/commercial rule. Check this point with one of our partner accountants.
- **MoR decision A:** “<USD 50,000, any complexity tolerance: use Paddle/Lemon Squeezy.” Unsupported revenue-based recommendation. Check this point with one of our partner accountants.
- **MoR decision B:** “USD 50,000–200,000, low tolerance: use MoR.” Unsupported revenue-based recommendation. Check this point with one of our partner accountants.
- **MoR decision C:** “USD 50,000–200,000, high tolerance: self-register top markets plus Stripe Tax.” Unsupported revenue-based recommendation. Check this point with one of our partner accountants.
- **MoR decision D:** “>USD 200,000, any tolerance: self-register plus accountant and Stripe Tax.” Unsupported revenue-based recommendation. Check this point with one of our partner accountants.
- **MoR contract/price claims:** Paddle, Lemon Squeezy and FastSpring invariably being the legal seller, collecting, filing/remitting in each country, paying the seller net and charging 5–10% inclusive of processing have not been confirmed for every product, contract and jurisdiction. A particular agreement may support some of these features; brand alone does not. Check this point with one of our partner accountants.
- **US tools:** Stripe Tax's old USD 0.50/transaction cost; automatic calculation AND collection for every use; TaxJar/Avalara “full compliance automation”; Paddle/Lemon Squeezy “5–10%, handles everything.” The original “varies” TaxJar/Avalara price is not a verified quote either. Current contract, service scope and pricing are required. The original vendor information links are retained in the vendor paragraph above, without endorsement. Check this point with one of our partner accountants.
- **US counts/Washington:** “45 states plus DC”, “TX/NY/PA/WA and about 20 others taxable”, “most states USD 100,000 OR 200 transactions.” No national-count or Washington product/2026-service conclusion is supplied here. The old federal/state shorthand is not a clearance of federal excise/import taxes. Check this point with one of our partner accountants.
- **India history:** the old 2% row, “no global threshold”, INR 2 crore (~USD 240,000), and “register/file quarterly” supply no usable 2026 obligation. The USD conversion, historical legal cutoff and case-specific registration/payment/return deadlines are held with the country row. Preserve historical exposure for a dated India review. Check this point with one of our partner accountants.
- **Kenya history/implementation:** the old 1.5%, “no global threshold”, KES 0/all digital services and current quarterly-filing implication cannot be used as current DST rules. The later statutory SEPT comparison and exclusions are also non-usable here; the operative 2026 implementing regulations, complete registration steps and live iTax fields were not read. Do not substitute the official 2025 draft for enacted regulations. Check this point with one of our partner accountants.
- **India/Kenya revenue action A:** “<USD 10,000/year: monitor; enforcement limited.” No authority-supported enforcement assurance or relief was found. Check this point with one of our partner accountants.
- **India/Kenya revenue action B:** “USD 10,000–50,000/year: weigh registration costs against exposure.” No legal permission to defer compliance at this revenue was established. Check this point with one of our partner accountants.
- **India/Kenya revenue action C:** “>USD 50,000/year: register because enforcement risk becomes real.” Neither this threshold nor the suggested below-threshold absence of risk was established. Check this point with one of our partner accountants.
- **EU late registration:** old “most countries” minimum about EUR 500, maximum about 5% of unpaid VAT, and a universal interest start under one EUR 10,000 threshold. No EU-wide support; country/period-specific law is required for each penalty and interest computation. Check this point with one of our partner accountants.
- **EU voluntary correction:** old blanket 50–75% penalty reduction. No current Member-State-by-Member-State basis established. Check this point with one of our partner accountants.
- **UK voluntary disclosure:** old “best terms about 30% of maximum.” This is not a general discount; HMRC's actual behaviour, timing, disclosure-quality and reasonable-excuse rules control. Check this point with one of our partner accountants.
- **Australia voluntary disclosure:** old “significant reduction, no penalty if minor.” No unconditional minor-error immunity or case-specific amount established here. Check this point with one of our partner accountants.
- **US voluntary disclosure:** old “generally 50%+ reduction.” No state-by-state programme/eligibility inventory established. Check this point with one of our partner accountants.
- **Audit/disclosure generalisation:** old “unprompted means before authority contact” and “all terms lost once audit begins.” These are not worldwide rules; HMRC's actual test differs, and other countries need their own law. Check this point with one of our partner accountants.
- **Remediation shortcuts:** automatic stop-selling/switch-MoR instruction; retrospective tax from one universal threshold date; file disclosure then pay a promised reduced penalty; register only going forward. None is an unconditional legal workflow. Use the dated liability and authority-specific remediation method above. Check this point with one of our partner accountants.
- **Professional-help costs:** old EUR 5,000 exposure trigger and EUR 500–2,000 per engagement. No legal threshold or current fee evidence; country complexity and unresolved facts determine referral. Check this point with one of our partner accountants.
- **Goods generalisations:** old service/goods complexity ranking, “all imports taxable without exception”, “all non-IOSS VAT collected by carrier from buyer” and “poor customer experience.” Correct legal distinctions are above; commercial experience is not a tax rule. Check this point with one of our partner accountants.
- **Platform brand allocation:** old “Gumroad/Paddle handle VAT; Stripe/Patreon/AdSense do not.” Current product terms and legal-supplier facts were not established for each brand. YouTube/Patreon/Substack/Gumroad receipts cannot all be assumed to be the seller's EU B2C supplies. Preserve names, reconcile contracts, apply the actual supplier and local aggregation rule. Check this point with one of our partner accountants.
- **Further country detail:** local exemptions and reduced rates, complete US state nexus/filing inventory, Canadian PST/QST, national registration/return fields and payment arrangements, historical remediation terms, and a live customs entry/rate/classification decision are outside this screen. No present EUR 2 EU handling-fee liability is inferred from the October guidance's expected date. Check this point with one of our partner accountants.

### closing-notes

The original 2024–2026 and 2025–2026 context is historical; it has not been silently changed into a different case year. Apply the 2026 screens only to matching facts and dates.

*Original content: [Artin (@ar-gen-tin)](https://github.com/ar-gen-tin/panrise) - MIT License.*
*OpenAccountants - open-source accounting skills for AI - info@openaaccountants.com*
