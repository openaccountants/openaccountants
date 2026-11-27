---
name: us-sales-tax
description: US sales and use tax framework for tax year 2026. Includes the general rate matrix for every sales-tax state and DC, distinguishes state components from combined bases and seller gross-receipts taxes, and gives the nexus, marketplace, sourcing, exemption and filing checks to perform before a state calculation. Preserves historical cases as explicit holds where the outcome is unsupported. Trigger on "sales tax", "use tax", "nexus", "Wayfair", "sales tax rate", "marketplace facilitator", "resale certificate", "exemption certificate" and "Streamlined Sales Tax". Load the state Guide for operative rules and us-sales-tax-nexus-50-state-matrix for thresholds.
version: "3.2"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: cross-country-method
---

# US sales and use tax: the framework, tax year 2026

**Answer first.** There is no federal general sales tax. The general state sales/use-tax population is 45 states plus DC, including the seller-tax regimes identified below. Alaska, Delaware, Montana, New Hampshire and Oregon have no general statewide sales tax; that does not mean all transactions there are tax-free. Alaska permits local sales taxes. Use the matrix as a starting rate reference, then establish the transaction's taxability, nexus, sourcing and local treatment before calculating. Sources: [federal explanation](https://www.budget.senate.gov/wp-content/uploads/media/doc/SFC%20Explanation%20of%20the%20Bill.pdf), [SST framework](https://www.streamlinedsalestax.org/Shared-Pages/faqs/faqs---about-streamlined), [five-state reference](https://www.fdic.gov/system/files/2024-08/16.pdf), [Alaska tax commission](https://arsstc.org/about/).

## Scope and who this is for

For a seller or purchaser checking US state sales/use tax in 2026. Read `us-sales-tax-nexus-50-state-matrix` for each state's economic-nexus test; `no-sales-tax-states` for the five-state exceptions; and the destination state's sales-tax Guide for taxability, local administration and return instructions. State income-tax nexus belongs in `us-pl-86-272-income-tax-nexus`. Customs (R-US-1), federal excise (R-US-2) and property tax (R-US-3) remain outside this Guide.

## Ask the client first

Obtain destination and ship-from addresses; product/service and contract details; sales and transaction counts by state and measurement period; offices, employees, agents, inventory and marketplace fulfilment locations; marketplace versus direct sales; registrations and their start dates; exemption documents; and tax already paid. Record related entities and temporary presence for the state nexus review. Do not invent a taxable product classification, count every sale as direct, or treat an absent certificate as conclusive proof that no statutory exemption exists.

## The method, step by step

### Rates, bands and thresholds

General rate reference, checked on **2026-11-27**. These are ordinary non-exempt retail-merchandise rates or the explicitly named equivalent. They do not establish taxability or the final address rate. Category-specific rates, holidays, special zones, exemptions and sourcing must be resolved separately. State components and combined bases are labelled so a local component is not added twice. For Nebraska Avenue One, New Jersey special zones and West Virginia in-lieu districts, do not use the general row to decide the special treatment. Check this point with one of our partner accountants.

| State | General rate reference | What it covers / qualification | Official source |
| --- | --- | --- | --- |
| Alabama | 4% | general merchandise | [Source](https://www.revenue.alabama.gov/sales-use/state-sales-use-tax-rates/) |
| Arizona | 5.6% (derived: 5% + 0.6%) | retail transaction privilege tax (seller tax) | [Source](https://www.azleg.gov/ars/42/05010.htm); [Source](https://www.azleg.gov/ars/42/05010-01.htm) |
| Arkansas | 6.5% | general merchandise | [Source](https://webftp.blr.arkansas.gov/Home/FTPDocument?path=Assembly%2F2027%2FSummary+Budget+Manuals%2F2026+Tax+Handbook.pdf) |
| California | 7.25% | statewide state/local base; district taxes additional | [Source](https://www.cdtfa.ca.gov/taxes-and-fees/sut-rates-description.htm) |
| Colorado | 2.9% | state component; check home-rule city administration separately | [Source](https://tax.colorado.gov/sales-tax-guide) |
| Connecticut | 6.35% | general rate; special product/service rates excluded | [Source](https://portal.ct.gov/drs/sales-tax/tax-information) |
| District of Columbia | 6% | general rate throughout 2026; special categories excluded | [Source](https://code.dccouncil.gov/us/dc/council/code/sections/47-2002) |
| Florida | 6% | general merchandise | [Source](https://floridarevenue.com/taxes/taxesfees/Pages/sales_tax.aspx) |
| Georgia | 4% | state component; use the current chart for the actual district | [Source](https://dor.georgia.gov/document/document/httpsdorgeorgiagovdocumentdocumentgeneral-rate-chart-effective-october-1-2026/download) |
| Hawaii | 4% | GET on retail business gross income; county surcharge and tax-on-tax pass-on calculation separate | [Source](https://files.hawaii.gov/tax/legal/brochures/GE_brochure-25.pdf) |
| Idaho | 6% | general merchandise | [Source](https://tax.idaho.gov/taxes/sales-use/online-guide/) |
| Illinois | 6.25% | general merchandise; not a grocery or special-category rate | [Source](https://tax.illinois.gov/research/publications/pio-115.html) |
| Indiana | 7% | general merchandise (rate in words on the page) | [Source](https://www.in.gov/dor/business-tax/sales-tax/) |
| Iowa | 6% | state component; local sales tax and use tax differ | [Source](https://revenue.iowa.gov/taxes/tax-guidance/sales-use-excise-tax/sales-use-tax-guide) |
| Kansas | 6.5% | general merchandise | [Source](https://www.kslegislature.gov/li/b2025_26/statute/079_000_0000_chapter/079_036_0000_article/079_036_0003_section/079_036_0003_k/) |
| Kentucky | 6% | general merchandise | [Source](https://revenue.ky.gov/Business/Sales-Use-Tax/Pages/default.aspx) |
| Louisiana | 5% | general merchandise | [Source](https://revenue.louisiana.gov/businesses/general-sales-and-use-taxes/general-sales-use-tax) |
| Maine | 5.5% | general sales, 2026 column | [Source](https://www11.maine.gov/revenue/taxes/sales-use-service-provider-tax/rates-due-dates) |
| Maryland | 6% | general rate; apply statutory cents schedule when rounding | [Source](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=11-104&enactments=false) |
| Massachusetts | 6.25% | general retail rate | [Source](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter64H/Section2) |
| Michigan | 6% | general taxable retail goods; residential fuel exception excluded | [Source](https://www.michigan.gov/taxes/business-taxes/sales-use-tax) |
| Minnesota | 6.875% (derived: 6.5% + 0.375%) | general retail rate | [Source](https://www.revisor.mn.gov/statutes/cite/297A.62) |
| Mississippi | 7% | general retail goods; groceries and other special rates excluded | [Source](https://www.dor.ms.gov/business/sales-use-tax/sales-tax-rates) |
| Missouri | 4.225% | general merchandise | [Source](https://dor.mo.gov/taxation/business/tax-types/sales-use/) |
| Nebraska | 5.5% | general rate; Avenue One elected-retailer special rate held for separate review | [Source](https://revenue.nebraska.gov/businesses/nebraska-sales-and-use-tax) |
| Nevada | 6.85% | statewide minimum/base; not a pure state-retained component | [Source](https://tax.nv.gov/news-publications/sales-use-tax-publications/) |
| New Jersey | 6.625% | standard rate; special-zone reductions require separate review | [Source](https://www.nj.gov/treasury/taxation/salestax.shtml) |
| New Mexico | 4.875% | GRT state component; gross-receipts regime, not a retail-buyer sales tax | [Source](https://www.tax.newmexico.gov/governments/municipal-county-governments/local-option-taxes/) |
| New York | 4% | state component; local and MCTD amounts separate | [Source](https://www.tax.ny.gov/bus/st/rates.htm) |
| North Carolina | 4.75% | general state rate | [Source](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.4.html) |
| North Dakota | 5% | general retail rate (in words on the page) | [Source](https://ndlegis.gov/cencode/t57c39-2.pdf) |
| Ohio | 5.75% | general retail rate (in words on the page) | [Source](https://codes.ohio.gov/ohio-revised-code/section-5739.02) |
| Oklahoma | 4.5% | general merchandise | [Source](https://oklahoma.gov/tax/businesses/sales-use-tax.html) |
| Pennsylvania | 6% | general merchandise | [Source](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/sales-use-and-hotel-occupancy-tax) |
| Rhode Island | 7% | general taxable retail sales | [Source](https://tax.ri.gov/tax-sections/sales-excise-taxes/sales-use-tax) |
| South Carolina | 6% | general rate | [Source](https://dor.sc.gov/sales-use-tax-index/sales-tax) |
| South Dakota | 4.2% | 2026 retail rate; later effective text not substituted (in words on the page) | [Source](https://sdlegislature.gov/api/Statutes/10-45-2.html) |
| Tennessee | 7% | general rate; food and single-article special rules separate | [Source](https://revenue.support.tn.gov/hc/en-us/articles/360058139672-SUT-13-Sales-and-Use-Tax-Rates-Overview) |
| Texas | 6.25% (derived: 6 + 1/4 percent) | state rate; combined local tax may not exceed 2% | [Source](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm) |
| Utah | 4.85% | state component; ordinary combined minimum 6.10% (derived: + 1% local + 0.25% county) | [Source](https://tax.utah.gov/forms-pubs/pub-25/) |
| Vermont | 6% | general rate (in words on the page) | [Source](https://legislature.vermont.gov/statutes/section/32/233/09771) |
| Virginia | 5.3% | general state/local base outside additional-tax localities; do not add the statewide local component again | [Source](https://hac.virginia.gov/subtopics/revenues/general-fund/) |
| Washington | 6.5% | state retail rate (in words on the page) | [Source](https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.020) |
| West Virginia | 6% | general rate; special in-lieu districts require separate treatment | [Source](https://tax.wv.gov/Business/SalesAndUseTax/Pages/SalesAndUseTax.aspx) |
| Wisconsin | 5% | state rate; local amounts separate | [Source](https://www.revenue.wi.gov/Pages/FAQS/pcs-taxrates.aspx) |
| Wyoming | 4% (derived: 3% + 1%) | general state rate | [Source](https://wyoleg.gov/statutes/compress/title39.pdf) |

### Apply the framework

1. **Nexus first.** *South Dakota v. Wayfair* removed physical presence as a necessary condition of substantial nexus; it did not create a nationwide threshold. Test the actual state law, measurement period, counted sales, transaction test, physical/affiliate/referral contacts and commencement date. A warehouse or marketplace inventory is a fact to examine, not an unconditional nationwide registration rule. [Court opinion, pp. 177–178 and 188–189](https://www.supremecourt.gov/opinions/17pdf/585us1r58_pok0.pdf).
2. **Separate marketplace and direct sales.** Obtain the facilitator's collection certification and the state-specific rule for threshold counting, registration and gross-versus-taxable return reporting. Do not assume all platforms always collect, that only direct sales are reported, or that marketplace stock always creates a permit requirement. Texas, for example, expressly provides a conditional temporary marketplace-inventory exception; other states must be checked separately. [Texas rule 3.286](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=197579).
3. **Classify before choosing a rate.** Resolve the product, service, delivery method, use and exemptions through the state's operative rules. The broad rate table is not a product-taxability matrix. The historical classifications listed below are held unless an expressly supported rule here applies.
4. **Source the transaction, then look up its address rate.** Identify where an order is received, fulfilled and delivered, and where possession/use occurs. Do not use the former origin/destination state-group list as a rule. New York describes its retail tax as a destination tax; Texas has several order/fulfilment branches, not one universal seller-location rule. [New York rates/sourcing](https://www.tax.ny.gov/bus/st/rates.htm), [Texas rule 3.334](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=219470).
5. **Exemptions and evidence.** Identify the actual statutory exemption and the evidence that state accepts; check the completed certificate, good faith, validity period, buyer status and record retention. Do not presume a certificate is required for every product exemption, that federal nonprofit status settles the state outcome, or that a permit number substitutes for a resale certificate. Keep unresolved resale, nonprofit, direct-pay and drop-shipment questions on hold. Check this point with one of our partner accountants.
6. **Check purchases for use tax.** For an otherwise taxable purchase, a seller's failure to collect does not establish exemption. Check storage/use, exclusions, the applicable use-tax rate and any credit for tax legally due and paid elsewhere. Do not assume combined sales and use rates always match: Iowa has a local option sales tax but no local option use tax. [Iowa guide](https://revenue.iowa.gov/taxes/tax-guidance/sales-use-excise-tax/sales-use-tax-guide).

### Product and historical-topic holds

Every row below is **non-usable for a tax outcome** until its state's operative rule and facts are established. The row is a destination for earlier coverage, not a confirmation of the old conclusion. For each row: **Check this point with one of our partner accountants.**

| Subject retained from earlier versions | Boundary of the hold |
| --- | --- |
| SaaS, cloud, canned/custom software and technology-transfer agreements | All former taxable/non-taxable state lists, download/hosting distinctions, state counts and rulings; retain customer, delivery and use details. Texas's supported conditional computation is below; no blanket exemption elsewhere is inferred. |
| Digital goods, downloads, streaming and subscription boxes | Former state-group lists, permanent versus subscription rights, digital codes, item allocation, shipping/handling and bundled deliveries. |
| Grocery food and prepared food | Former exempt/reduced/full-rate groups; candy, soft drinks, supplements, utensils and heating; Illinois local grocery tax, Arkansas, Alabama, Mississippi, Missouri, Tennessee, Kansas, Oklahoma, Utah and Virginia special food rules. No grocery rate is supplied here. |
| Clothing outside the Massachusetts example | Former Pennsylvania/New Jersey/Minnesota blanket exemptions; New York, Vermont and Rhode Island thresholds; fur, costumes, sports/protective goods and holidays. |
| Professional and other services | Former broad-tax/few-tax groups; legal/accounting/medical/engineering, education, financial, personal care, telecom, cable, landscaping, pest control, security, parking, laundry, grooming and repairs. |
| Medicines and medical devices | Former universal prescription exemption, OTC, DME and prosthetics assertions. No national exemption is inferred. |
| Manufacturing, R&D, packaging, agricultural, industrial and energy exemptions | All former full/partial/no-exemption groups and California's manufacturing reduction; qualifying use and evidence must be established. |
| Motor vehicles, trade-ins, real property, construction and leases | Separate tax regimes, registration tax, credit, lump-sum versus time/materials, financing versus rental and upfront versus periodic tax. |
| Exemption documents and buyer status | MTC/SST/state-specific forms, multi-state acceptance, blanket/single-sale certificates, government, nonprofit and direct pay; renewal, retention, misuse and seller protection. |
| Past exposure and administration | Voluntary disclosure, eligibility, lookback, penalty waiver, registration consequences, refunds, officer liability, penalties, interest, vendor discounts, prepayments, filing frequency and holiday extensions. Former national ranges and state thresholds are withdrawn. |
| Special places and comparison with VAT | Alaska local/resort/meals/rooms/Delaware seller taxes; special-zone and in-lieu rates; foreign VAT input-credit, invoice, reverse-charge and OSS comparisons. Do not import an EU VAT outcome into this method. |

## Boundary and exception table

| Situation | Required next step |
| --- | --- |
| All-state seller, including one based in Oregon or another no-general-sales-tax state | Run each relevant state's nexus and taxability tests; the seller's home-state treatment does not answer destination-state liability. |
| Employees, representatives, trade shows, delivery vehicles, related companies or marketplace inventory | Test that state's definitions and exceptions; do not use a national physical-presence shortcut. |
| Marketplace plus website sales | Reconcile both channels without assuming identical counting or return treatment. |
| Exempt product or buyer with missing evidence | Resolve the exemption and evidence rule before invoicing or filing; hold the result if unresolved. |
| Unknown product, address, period, marketplace share or prior tax | Obtain the missing facts; do not choose a rate or certify a nexus/exemption conclusion from assumptions. |
| Drop shipments or past unfiled exposure | Retain all parties, locations, periods and original amounts; apply the hold/referral above. |

## Worked cases

**Case 1 — Massachusetts clothing, 2026.** An ordinary $200 jacket qualifies under chapter 64H §6(k): it is not special athletic/protective clothing excluded by that paragraph. The exemption covers the first $175 per article. At the §2 rate of 6.25%, taxable excess is $25, tax is $1.5625, displayed to the nearest cent as $1.56, and total is $201.56. An ordinary qualifying $150 shirt is exempt. Sources: [§6(k)](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter64H/Section6), [§2](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter64H/Section2).

```oa-check
name: Massachusetts 200 jacket, 175 clothing exemption (2026)
inputs:
  price: 200
  exempt_amount: 175
  rate: 0.0625
steps:
  - taxable: max(price - exempt_amount, 0)
  - tax: round(taxable * rate, 2)
expected:
  taxable: 25
  tax: 1.56
```

**Case 2 — Michigan use tax, 2026.** Keep the original $1,000 machine and 4% tax paid elsewhere. Assume it is acquired for immediate taxable Michigan business use, no industrial-processing or other exemption applies, the earlier tax was legally due and paid on the same retail sale to the consumer, and the other jurisdiction accords the reciprocal exemption required by §4(1)(e). Michigan's 6% amount is $60; the qualifying earlier $40 leaves $20. With no earlier tax and the same taxable facts, $60 is due. An erroneous charge elsewhere is not automatically a credit. Sources: [MCL 205.93(1)](https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-205-93), [205.94(1)(e)](https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-205-94).

```oa-check
name: Michigan use tax after 4 percent paid elsewhere (2026)
inputs:
  price: 1000
  michigan_rate: 0.06
  other_state_rate: 0.04
steps:
  - michigan_tax: price * michigan_rate
  - credit: min(price * other_state_rate, michigan_tax)
  - use_tax_due: michigan_tax - credit
expected:
  michigan_tax: 60.00
  credit: 40.00
  use_tax_due: 20.00
```

### Earlier cases — inputs preserved, outcomes held

These earlier scenarios are **not redated as 2026 advice**. Version 2 was labelled 2025; version 1 had no tax-year field. Amounts and locations remain the original inputs. Arithmetic labelled conditional does not establish taxability, nexus, a current address rate, return treatment or an exemption. Every unresolved outcome below is non-usable: **Check this point with one of our partner accountants.**

| Original scenario | Preserved inputs and present disposition |
| --- | --- |
| v2 EC1 / EC4 / test 1 — nationwide seller / Oregon seller | $2M national sales, all 50 states; separate test $150K Florida, $90K New York, $80K California. Preserve each amount; no nexus outcome without the correct measurement period, counted sales, contacts and commencement rule. |
| v2 EC2 / test 2 — SaaS | Nationwide seller; customers in New York, California and Illinois. Former yes/no outcomes held, including whether the actual supply is hosted software or a different taxable service. |
| v2 EC3 — drop shipment | Seller A, supplier B, buyer C. Test all parties and certificate rules; no automatic supplier exemption. |
| v2 test 3 — groceries | Illinois, Texas and Alabama grocery sales. Former outcomes held under the food row above. |
| v2 test 4 — clothing | $200 jacket sold in New York, Pennsylvania and California; former whole-price/threshold outcomes held. |
| v2 test 5 — marketplace | $80K Amazon plus $30K direct, with a stated $100K threshold. Total is $110K; whether the threshold counts both, and the seller's collection/reporting duty, are unresolved. |
| v1 test 1 — Los Angeles furniture | $1,000, no certificate, supplied combined rate 9.50%. Conditional arithmetic: $95 tax and $1,095 total; the supplied address rate and actual tax outcome remain held. |
| v1 test 2 — Oregon remote seller | $120,000 Texas and $80,000 Florida sales in the trailing 12 months. Former blanket “no obligation” conclusion withdrawn; periods, contacts and counted sales still need testing. |
| v1 test 3 — New York clothing | $150 jacket; stipulated 8.875%; $109 and $111 shirts and former $110 boundary. If the entire $150 is taxable at the supplied rate, arithmetic is $13.31. Classification, boundary and local exemption outcome held. |
| v1 test 4 — Boston jacket | $200 jacket and 6.25%: arithmetic $25 taxable excess, $1.56 tax, $201.56 total under the qualifying-clothing assumptions in Case 1. Historical year remains unspecified. |
| v1 test 5 — Illinois use tax | $5,000 office supplies; no vendor tax; supplied combined sales rate 8.75%. Multiplication gives $437.50, but that does not prove the applicable Illinois use-tax rate. The old use-tax liability is withdrawn. |
| v1 test 6 — Tennessee marketplace | $50 taxable product; Amazon; supplied combined rate 9.75%. Conditional arithmetic rounds $4.875 to $4.88; facilitator duties and seller return reporting remain held. |
| v1 test 7 — Texas resale | $10,000 inventory; completed Form 01-339 and valid permit number. Retain facts, but establish the actual resale purpose and good-faith certificate requirements before concluding exemption. |
| v1 test 8 / EC4 — SaaS | California seller; $500/month; California, Texas, Washington and Florida customers; earlier comparison also Pennsylvania. Original assumed combined rates: Texas 8.25%, Washington/Seattle 10.25%. The old Texas “80% exempt” calculation is wrong: **if** the supply qualifies as Texas data processing, the statutory exemption is 20%, so the derived taxable fraction is 80% and conditional tax is $500 × 80% × 8.25% = $33, not $8.25. Washington's supplied-rate arithmetic is $51.25. Actual classifications, local rates and multi-state use remain held. [Texas §151.351](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm#151.351). |
| v1 test 9 — laptop brought to Massachusetts | $2,000 bought in New Hampshire with 0% tax, brought home to Massachusetts, supplied 6.25% rate: multiplication gives $125. Purchase/use timing, exemptions and return route remain held. |
| v1 test 10 — drop shipment | New York seller, California manufacturer, Ohio buyer; seller has Ohio nexus; supplied Ohio combined rate 7.50%, price unspecified. No invented price or supplier exemption; outcome held. |
| v1 test 11 — Texas food | Rice $3.00, rotisserie chicken $7.99, water $1.50, sandwich heated at request $5.99; supplied 8.25%. Old classification-based $1.15 outcome held. Multiplying just chicken and sandwich gives $0.66 and $0.49 after rounding; that arithmetic does not certify the classifications. |
| v1 test 12 — Texas holiday | $75 jeans and $200 laptop, supplied 8.25%, purported holiday $100 boundary. Date, eligible list and threshold must be proven; no holiday exemption inferred. |
| v1 EC3 / EC5 / EC6 | Oregon digital seller into 30 states; growing seller approaching $100,000 in several states; nonprofit with exemption letters in some states. Retain each situation; no common threshold, retroactive collection or automatic nonprofit outcome. |
| v1 EC7 / EC8 / EC10 | $500,000 construction contract including labour/materials; $800 computer plus $200 installation for $900 bundled price; 36-month copier/printer lease. Contract, bundling and timing outcomes held; no universal “10% means whole bundle taxable” rule. |
| v1 EC11 / use-tax credit illustrations | Supplies move New Jersey to Pennsylvania: supplied 6.625% paid and 6% destination before possible local tax, plus reverse transfer. Also former hypothetical 5%-to-7% and 7%-to-5% credit comparisons. No automatic net credit or refund conclusion. |
| v1 EC12 / EC13 / EC14 | Five states, three years unregistered; personal-use furniture bought under resale certificate; monthly book/candle/digital-code boxes. Preserve periods and contents; VDA, misuse liability/protection, product allocation and shipping outcomes held. |
| v1 EC1 / EC2 / EC9 | Three-party State X/Y/Z drop shipment; marketplace seller already filing; school/clothing holiday purchases. Do not infer certificate acceptance, universal exclusion from gross receipts, or a holiday exemption from the labels. |

## When to refuse or refer

R-US-1 customs: refer to a customs broker. R-US-2 federal excise and R-US-3 property tax: outside scope. R-US-4 past exposure and R-US-5 unresolved software/digital taxability: use the corresponding state Guide and keep the outcome on hold. All topic/case holds above use the same instruction: **Check this point with one of our partner accountants.**

## Filing and payment

Work state by state: confirm registration, the assigned reporting period, the current official form/portal, gross and exempt sales, marketplace presentation, jurisdiction-level tax, purchases/use tax, payment date and acknowledgement. Reconcile tax collected to tax reported; retain exemption evidence and confirmations. Do not use the old general frequency thresholds, due-date groups, prepayment limits, discount tables or penalty/lookback ranges.

SST provides central registration in the member states selected. That registration entails collection/remittance obligations in those selected states; do not assume it supplies one national return or eliminates state-specific returns. [SST FAQ](https://www.streamlinedsalestax.org/Shared-Pages/faqs/faqs---about-streamlined). Historical full/associate-member lists and free-CSP eligibility are not relied on here. Unresolved filing/payment and voluntary-disclosure points remain non-usable. Check this point with one of our partner accountants.

## Completion checklist

- State and relevant local administration identified; all nexus facts and measurement periods tested.
- Product, buyer/use exemption and supporting documents established.
- Sales versus use tax, sourcing and actual address rate resolved without double-counting a local component.
- Marketplace and direct transactions reconciled to the state's reporting instructions.
- Original case inputs retained; unresolved holds excluded from any filing or payment conclusion.

This Guide and its outputs are informational and do not constitute tax, legal or financial advice. All outputs must be reviewed by a qualified professional before filing. For written federal tax advice, apply reasonable factual and legal assumptions and consider the relevant facts and circumstances under [31 CFR §10.37](https://www.ecfr.gov/current/title-31/subtitle-A/part-10/subpart-B/section-10.37).

## Sources

Each rate-row URL was read for the stated rate, its nature and neighbouring exceptions on **2026-11-27**. Reads of long documents were limited to the operative portions identified below. Historical inputs are preserved data, not assertions that their old rates or outcomes are current.

| Source / passage actually read | Official URL | Read on |
| --- | --- | --- |
| State rates: each linked rate row above; Arizona §§42-5010(A)(1), 42-5010.01; Arkansas handbook §1.7; Minnesota §297A.62(1),(1a); North Dakota §57-39.2-02.1; Wyoming §39-15-104(a),(b). General merchandise only, with exceptions as identified. | [Arizona](https://www.azleg.gov/ars/42/05010.htm), [Arkansas](https://webftp.blr.arkansas.gov/Home/FTPDocument?path=Assembly%2F2027%2FSummary+Budget+Manuals%2F2026+Tax+Handbook.pdf), [Minnesota](https://www.revisor.mn.gov/statutes/cite/297A.62), [North Dakota](https://ndlegis.gov/cencode/t57c39-2.pdf), [Wyoming](https://wyoleg.gov/statutes/compress/title39.pdf); other individual URLs are on their rate rows | 2026-11-27 |
| Federal framework sentence (p. 318) and five-state background (FDIC p. 14); current no-general-tax statements also read from the individual state authorities/Alaska commission. | [Federal explanation](https://www.budget.senate.gov/wp-content/uploads/media/doc/SFC%20Explanation%20of%20the%20Bill.pdf), [FDIC](https://www.fdic.gov/system/files/2024-08/16.pdf), [Alaska](https://arsstc.org/about/), [Delaware](https://revenue.delaware.gov/business-tax-forms/doing-business-in-delaware/step-4-gross-receipts-taxes/), [Montana](https://revenue.mt.gov/taxes/general-sales-tax), [New Hampshire](https://www.revenue.nh.gov/faq/does-new-hampshire-have-sales-tax), [Oregon](https://www.oregon.gov/dor/programs/businesses/pages/sales-tax.aspx) | 2026-11-27 |
| Wayfair: opinion's physical-presence holding; not the historical South Dakota threshold as a current rule. | https://www.supremecourt.gov/opinions/17pdf/585us1r58_pok0.pdf | 2026-11-27 |
| Massachusetts clothing exemption and athletic/protective exclusion, §6(k); retail rate §2. | [§6](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter64H/Section6), [§2](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter64H/Section2) | 2026-11-27 |
| Michigan use-tax imposition and prior-tax/reciprocity conditions; Iowa local sales/use divergence. | [205.93](https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-205-93), [205.94](https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-205-94), [Iowa](https://revenue.iowa.gov/taxes/tax-guidance/sales-use-excise-tax/sales-use-tax-guide) | 2026-11-27 |
| Texas §§151.051, 151.351 and rules 3.286/3.334: applicable completed reads reused; temporary marketplace inventory exception, order/fulfilment distinction, data-processing exemption direction. | [Code](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm), [3.286](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=197579), [3.334](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=219470) | 2026-11-27 |
| SST general framework and selected-state registration consequences; New York delivery/possession sourcing. | [SST](https://www.streamlinedsalestax.org/Shared-Pages/faqs/faqs---about-streamlined), [New York](https://www.tax.ny.gov/bus/st/rates.htm) | 2026-11-27 |

Not yet confirmed: the product, procedural, special-place and historical-case outcomes explicitly held above. They are excluded from usable guidance. Check this point with one of our partner accountants.
