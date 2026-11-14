---
name: us-sales-tax
description: The US sales and use tax framework for tax year 2026, read before any state sales tax work. Covers how sales tax and use tax fit together, physical and economic nexus after Wayfair, marketplace facilitators, the five states with no general sales tax, the statewide base rate of each of the 45 sales tax states and DC (each linked to that state's own source), sourcing, exemption and resale certificates, taxability patterns for SaaS, food, clothing and digital goods, Streamlined Sales Tax registration and voluntary disclosure. Trigger on "sales tax", "use tax", "nexus", "Wayfair", "resale certificate", "exemption certificate", "sales tax rate", "marketplace facilitator", "Streamlined Sales Tax". Load the state's own sales tax skill for that state's base and filing, and us-sales-tax-nexus-50-state-matrix for thresholds.
version: "3.1"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: cross-country-method
---

# US sales and use tax: the framework, tax year 2026

> **Source-cited draft.** Built from each state's own revenue department page or statute for its base rate, and from the 13 November 2026 state sales tax skills where they exist, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** There is no federal sales tax. 45 states and DC charge a statewide sales tax; Alaska, Delaware, Montana, New Hampshire and Oregon do not (see `no-sales-tax-states`). Each state sets its own base, rate, nexus test and returns, and most add local taxes. A seller must collect in a state once it has physical presence or passes that state's economic nexus threshold. A buyer owes use tax at the same rate when no sales tax was charged. Never carry one state's rule into another.

## Scope and who this is for

In scope: the shared US framework and the statewide base rate of every sales tax state for 2026. Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Economic nexus threshold of each state | `us-sales-tax-nexus-50-state-matrix` |
| The five states with no general sales tax | `no-sales-tax-states` |
| A state's own base, local rates, exemptions and returns | that state's sales tax skill (for example `texas-sales-tax`, `california-sales-tax`, `ny-sales-tax`, `wa-sales-tax`) |
| State income tax nexus for remote sellers | `us-pl-86-272-income-tax-nexus` |

Refused outright: customs duties (R-US-1), federal excise taxes on fuel, alcohol, tobacco and firearms (R-US-2), and property tax (R-US-3).

## Ask the client first

1. Which states do you sell into, and which do you ship from? (Which state skills to load; origin or destination sourcing.)
2. What do you sell: goods, services, digital goods, SaaS? (Taxability differs by state.)
3. Sales in dollars and number of transactions per state, by year and by month. (Economic nexus.)
4. Where do you or related companies have employees, offices, warehouses or inventory, including marketplace fulfilment centres? (Physical nexus.)
5. How much goes through marketplaces such as Amazon, eBay, Etsy or Walmart? (Facilitators collect on those sales.)
6. Are you registered anywhere already, and since when?
7. Do your buyers give you resale or exemption certificates?

## The method, step by step

### Rates, bands and thresholds

Statewide base rate only. Local rates are added in most states; the state's own skill or rate lookup gives the combined rate for an address.

| State | Statewide base rate, 2026 | Source |
| --- | --- | --- |
| Arizona (transaction privilege tax, retail) | 5.6% (derived: 5% plus the 0.6% increment, both in words on the page) | [A.R.S. 42-5010](https://www.azleg.gov/ars/42/05010.htm), [A.R.S. 42-5010.01](https://www.azleg.gov/ars/42/05010-01.htm) |
| Arkansas | 6.5% | [Arkansas 2026 Tax Handbook, section 1.7](https://webftp.blr.arkansas.gov/Home/FTPDocument?path=Assembly%2F2027%2FSummary+Budget+Manuals%2F2026+Tax+Handbook.pdf) |
| California | 7.25% | [CDTFA, rate description](https://www.cdtfa.ca.gov/taxes-and-fees/sut-rates-description.htm) |
| Connecticut | 6.35% | [CT DRS, sales tax information](https://portal.ct.gov/drs/sales-tax/tax-information) |
| District of Columbia | 6% | [DC OTR, sales and use tax FAQ](https://otr.cfo.dc.gov/page/sales-and-use-tax-faqs) |
| Florida | 6% | [Florida DOR, sales tax](https://floridarevenue.com/taxes/taxesfees/Pages/sales_tax.aspx) |
| Georgia | 4% | [Georgia DOR, rate chart from 1 October 2026](https://dor.georgia.gov/document/document/httpsdorgeorgiagovdocumentdocumentgeneral-rate-chart-effective-october-1-2026/download) |
| Hawaii (general excise tax) | 4% | [Hawaii DOTAX, GET brochure](https://files.hawaii.gov/tax/legal/brochures/GE_brochure-25.pdf) |
| Idaho | 6% | [Idaho State Tax Commission, sales and use tax guide](https://tax.idaho.gov/taxes/sales-use/online-guide/) |
| Illinois (general merchandise) | 6.25% | [IDOR PIO-115](https://tax.illinois.gov/research/publications/pio-115.html) |
| Indiana | 7% | [Indiana DOR, sales tax](https://www.in.gov/dor/business-tax/sales-tax/) |
| Iowa | 6% | [Iowa DOR, sales and use tax guide](https://revenue.iowa.gov/taxes/tax-guidance/sales-use-excise-tax/sales-use-tax-guide) |
| Kansas | 6.5% | [K.S.A. 79-3603](https://www.kslegislature.gov/li/b2025_26/statute/079_000_0000_chapter/079_036_0000_article/079_036_0003_section/079_036_0003_k/) |
| Kentucky | 6% | [Kentucky DOR, sales and use tax](https://revenue.ky.gov/Business/Sales-Use-Tax/Pages/default.aspx) |
| Louisiana | 5% | [Louisiana DOR, general sales and use tax](https://revenue.louisiana.gov/businesses/general-sales-and-use-taxes/general-sales-use-tax) |
| Maine (general sales) | 5.5% | [Maine Revenue Services, rates and due dates](https://www.maine.gov/revenue/taxes/sales-use-service-provider-tax/rates-due-dates) |
| Maryland | 6% (6 cents for each exact dollar) | [Md. Tax-General 11-104](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=11-104&enactments=false) |
| Massachusetts | 6.25% | [Mass. DOR, sales and use tax guide](https://www.mass.gov/guides/sales-and-use-tax) |
| Michigan | 6% | [Michigan Treasury, sales and use tax](https://www.michigan.gov/taxes/business-taxes/sales-use-tax) |
| Minnesota | 6.875% (derived: 6.5% plus the 0.375% constitutional tax) | [Minn. Stat. 297A.62](https://www.revisor.mn.gov/statutes/cite/297A.62) |
| Mississippi (general retail) | 7% | [Mississippi DOR, sales tax rates](https://www.dor.ms.gov/business/sales-use-tax/sales-tax-rates) |
| Missouri | 4.225% | [Missouri DOR, sales and use tax](https://dor.mo.gov/taxation/business/tax-types/sales-use/) |
| Nebraska | 5.5% | [Nebraska DOR, sales and use tax](https://revenue.nebraska.gov/businesses/sales-and-use-tax) |
| Nevada | 6.85% | [Nevada Department of Taxation, sales and use tax](https://tax.nv.gov/tax-types/sales-use-tax/) |
| New Jersey | 6.625% | [NJ Division of Taxation, sales tax rate history](https://www.nj.gov/treasury/taxation/salestax.shtml) |
| New Mexico (gross receipts tax, state part) | 4.875% | [New Mexico TRD, FYI-105](https://realfile.tax.newmexico.gov/FYI-105.pdf) |
| New York | 4% | [NY Tax Department, sales tax rates](https://www.tax.ny.gov/bus/st/rates.htm) |
| North Carolina | 4.75% | [N.C.G.S. 105-164.4(a)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.4.html) |
| North Dakota | 5% | [N.D.C.C. 57-39.2-02.1](https://ndlegis.gov/cencode/t57c39-2.pdf) |
| Ohio | 5.75% | [Ohio DOT, sales and use tax](https://tax.ohio.gov/business/sales-and-use-tax) |
| Pennsylvania | 6% | [Pennsylvania DOR, sales, use and hotel occupancy tax](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/sales-use-and-hotel-occupancy-tax) |
| Rhode Island | 7% | [RI Division of Taxation, sales and use tax](https://tax.ri.gov/tax-sections/sales-excise-taxes/sales-use-tax) |
| South Carolina | 6% | [SCDOR, sales tax](https://dor.sc.gov/sales-use-tax-index/sales-tax) |
| South Dakota | 4.2% (in words on the page) | [SDCL 10-45-2](https://sdlegislature.gov/api/Statutes/10-45-2.html) |
| Tennessee | 7% | [Tennessee DOR, sales and use tax](https://www.tn.gov/revenue/taxes/sales-and-use-tax.html) |
| Texas | 6.25% | [Texas Comptroller, sales and use tax](https://comptroller.texas.gov/taxes/sales/) |
| Vermont | 6% | [32 V.S.A. 9771](https://legislature.vermont.gov/statutes/section/32/233/09771) |
| Virginia (combined state and statewide local rate, outside the regions with extra regional tax) | 5.3% | [Virginia Tax, retail sales and use tax](https://www.tax.virginia.gov/retail-sales-and-use-tax) |
| Washington | 6.5% (in words on the page) | [RCW 82.08.020](https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.020) |
| West Virginia | 6% | [West Virginia Tax Division, sales and use tax](https://tax.wv.gov/Business/SalesAndUseTax/Pages/SalesAndUseTax.aspx) |
| Wisconsin | 5% | [Wisconsin DOR, tax rates FAQ](https://www.revenue.wi.gov/Pages/FAQS/pcs-taxrates.aspx) |
| Wyoming | 4% | [Wyo. Stat. 39-15-104](https://wyoleg.gov/statutes/compress/title39.pdf) |

Alabama, Colorado, Oklahoma and Utah: base rate not confirmed for this version (see "Not yet confirmed:"). Use the state's own skill or revenue page.

### The framework, in order

1. **Sales tax or use tax.** Sales tax is collected by the seller at the sale. Use tax is owed by the buyer when no sales tax was collected, at the same rate. One or the other is due on a transaction, never both. Most states credit sales tax paid to another state against their use tax (Michigan, for example: a $1,000 item with 4% paid elsewhere owes 2% Michigan use tax; see `mi-sales-tax`).
2. **Nexus.** A seller must register where it has physical nexus (employees, offices, inventory, property, representatives, including inventory in a marketplace warehouse) or economic nexus. Since *South Dakota v. Wayfair* (2018) every sales tax state and DC has an economic nexus rule; the threshold, the period and which sales count differ by state (see `us-sales-tax-nexus-50-state-matrix`). Affiliate and click-through rules can still create nexus in some states.
3. **Marketplace facilitators.** Every sales tax state and DC requires marketplace facilitators to collect on the sales they facilitate. The seller still files for its direct sales and, in some states, must register once its total including marketplace sales passes the threshold.
4. **The tax base.** Sales tax mainly applies to retail sales of tangible personal property. Services, digital goods and SaaS are taxed differently in each state: check the state skill.
5. **Sourcing.** Most states source an interstate sale to the delivery address (destination). Some source intrastate sales to the seller's location (origin). Check the state skill.
6. **Rate.** State base rate (table above) plus any local rates for the sourced address.
7. **Certificates.** A sale for resale, or to an exempt buyer, is exempt only with a valid certificate in the form the state accepts, kept on file.
8. **Registration and returns.** Each state has its own registration and return. Streamlined Sales Tax (SST) member states can be registered at once through the SST registration system ([Streamlined Sales Tax Governing Board](https://www.streamlinedsalestax.org/Shared-Pages/faqs/faqs---about-streamlined)).
9. **Past exposure.** Most states offer voluntary disclosure agreements, usually with a penalty waiver and a limited lookback. Terms differ by state: refer.

### Taxability patterns to check

These are starting points only. They were not re-read state by state for 2026: confirm in the state's own skill before advising.

| Item | Pattern |
| --- | --- |
| SaaS | Taxed in some states and not in others (California treats hosted software as not a sale of goods, per `california-sales-tax`; Illinois refers SaaS, per `illinois-sales-tax`). Never assume one answer |
| Grocery food | Exempt in most states; taxed at a reduced rate in some (Mississippi 5% on qualifying groceries, per `ms-sales-tax`; Virginia 1% statewide, per [Virginia Tax](https://www.tax.virginia.gov/retail-sales-and-use-tax)); Arkansas state rate 0% from 1 January 2026 with local tax remaining, per `ar-sales-tax` |
| Clothing | Taxable in most states; exempt or partly exempt in some (Massachusetts exempts up to $175 per item, per [Mass. DOR](https://www.mass.gov/guides/sales-and-use-tax)) |
| Digital goods | Varies widely; check the state skill |
| Professional services | Not taxed in most states; broadly taxed in a few (Hawaii GET and New Mexico GRT reach most services) |
| Manufacturing equipment | Exempt or partly exempt in most states |

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Seller ships to all 50 states | Test nexus state by state; never use one national total |
| Seller has inventory in an Amazon warehouse | Physical nexus in that state, whatever the sales |
| Oregon or other no-sales-tax seller ships elsewhere | Collects where it has nexus |
| Drop shipment (seller in A, supplier in B, buyer in C) | Depends on nexus of each party and the certificates given: check state C's rules; refer if material |
| Marketplace sales plus own website | Facilitator collects on marketplace sales; the seller collects on direct sales once it has nexus |
| Buyer charged no tax by a remote seller | Buyer owes use tax |
| Exempt sale with no certificate | Treat as taxable until a valid certificate is on file |
| Past sales in a state where nexus existed and nothing was filed | Voluntary disclosure: refer |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Product type | Treat as taxable tangible goods until classified |
| Delivery address | Do not choose a rate; ask |
| Marketplace share of sales | Treat all as direct for the nexus count; ask |
| Certificate on file | None; tax applies |

## Worked cases

**Case 1, Massachusetts clothing.** A Massachusetts store sells a $200 jacket. The first $175 is exempt; tax is 6.25% on the $25 excess = $1.5625, rounded to $1.56. A $150 shirt is fully exempt.

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

**Case 2, a decision: collect Michigan tax or leave the buyer to pay use tax?** A Michigan business buys a $1,000 machine from a seller who charged 4% tax for another state. Michigan use tax is 6% less the 4% already paid: $60 - $40 = $20. Had nothing been charged, the full $60 would be due. Paying another state's tax does not remove Michigan use tax; it reduces it.

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

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-US-1 | Import duties and customs | Refer to a customs broker |
| R-US-2 | Federal excise taxes (fuel, alcohol, tobacco, firearms) | Outside scope |
| R-US-3 | Real and personal property tax | Outside scope |
| R-US-4 | Voluntary disclosure for past exposure | Refer |
| R-US-5 | SaaS or digital goods taxability where the amount matters | Use the state skill; refer or seek a ruling if the state has not spoken |

## Filing and payment

Each state sets its own return, frequency and due dates, usually based on the tax collected. Common contents: gross sales, exempt sales, taxable sales, tax by local jurisdiction, and use tax. File through the state's portal; SST states share registration but keep their own returns. Penalties and interest are set by each state. See the state skill for its return and dates.

## Completion checklist

- Physical presence checked in every state, including warehouses.
- Economic nexus tested per state with that state's measure (`us-sales-tax-nexus-50-state-matrix`).
- Product taxability confirmed in each state skill.
- Rate = state base plus local for the sourced address.
- Certificates on file for every exempt sale.
- Use tax accrued on untaxed purchases.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| CDTFA, rate description. Read for the 7.25% statewide base rate. The rates for AZ, AR, CA, GA, HI, ID, IL, IA, LA, MA, MI, MS, NM, NY, NC, OH, PA, RI, TX, VT and WA are taken from the 13 Nov 2026 state skills and the links in their rows; ND and SD from the state skills on main. | https://www.cdtfa.ca.gov/taxes-and-fees/sut-rates-description.htm | 2026-11-13 |
| CT DRS, sales tax information. Read for "The sales tax rate of 6.35% applies to the retail sale, lease, or rental of most goods". | https://portal.ct.gov/drs/sales-tax/tax-information | 2026-11-13 |
| DC OTR FAQ. Read for "General Sale ... Tax Rate: 6%". | https://otr.cfo.dc.gov/page/sales-and-use-tax-faqs | 2026-11-13 |
| Florida DOR. Read for "Florida's general state sales tax rate is 6%". | https://floridarevenue.com/taxes/taxesfees/Pages/sales_tax.aspx | 2026-11-13 |
| Indiana DOR. Read for "register to collect a seven percent sales tax". | https://www.in.gov/dor/business-tax/sales-tax/ | 2026-11-13 |
| K.S.A. 79-3603. Read for "a tax at the rate of 6.5%". | https://www.kslegislature.gov/li/b2025_26/statute/079_000_0000_chapter/079_036_0000_article/079_036_0003_section/079_036_0003_k/ | 2026-11-13 |
| Kentucky DOR. Read for "imposed at the rate of 6 percent of gross receipts". | https://revenue.ky.gov/Business/Sales-Use-Tax/Pages/default.aspx | 2026-11-13 |
| Maine Revenue Services. Read for General Sales 5.5% effective 01/01/2026. | https://www.maine.gov/revenue/taxes/sales-use-service-provider-tax/rates-due-dates | 2026-11-13 |
| Md. Tax-General 11-104. Read for "6 cents for each exact dollar". | https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=11-104&enactments=false | 2026-11-13 |
| Minn. Stat. 297A.62. Read for "a sales tax of 6.5 percent" and "an additional sales tax of 0.375 percent". | https://www.revisor.mn.gov/statutes/cite/297A.62 | 2026-11-13 |
| Missouri DOR. Read for "The state sales tax rate is 4.225%". | https://dor.mo.gov/taxation/business/tax-types/sales-use/ | 2026-11-13 |
| Nebraska DOR. Read for "The Nebraska state sales and use tax rate is 5.5%". | https://revenue.nebraska.gov/businesses/sales-and-use-tax | 2026-11-13 |
| Nevada Department of Taxation. Read for "The base state sales tax rate in Nevada is 6.85%". | https://tax.nv.gov/tax-types/sales-use-tax/ | 2026-11-13 |
| NJ Division of Taxation. Read for "6.625% on January 1, 2018". | https://www.nj.gov/treasury/taxation/salestax.shtml | 2026-11-13 |
| SCDOR. Read for "The statewide Sales & Use Tax rate is 6%". | https://dor.sc.gov/sales-use-tax-index/sales-tax | 2026-11-13 |
| Tennessee DOR. Read for "The general state tax rate is 7%". | https://www.tn.gov/revenue/taxes/sales-and-use-tax.html | 2026-11-13 |
| Virginia Tax. Read for "5.3% Everywhere else" and "Grocery Tax ... 1% statewide". | https://www.tax.virginia.gov/retail-sales-and-use-tax | 2026-11-13 |
| West Virginia Tax Division. Read for "in lieu of the 6% sales tax". | https://tax.wv.gov/Business/SalesAndUseTax/Pages/SalesAndUseTax.aspx | 2026-11-13 |
| Wisconsin DOR FAQ. Read for "The Wisconsin sales tax is a 5% tax". | https://www.revenue.wi.gov/Pages/FAQS/pcs-taxrates.aspx | 2026-11-13 |
| Wyo. Stat. 39-15-104. Read for the 3% plus additional 1% (4%). | https://wyoleg.gov/statutes/compress/title39.pdf | 2026-11-13 |
| Streamlined Sales Tax Governing Board FAQ. Read for central registration. | https://www.streamlinedsalestax.org/Shared-Pages/faqs/faqs---about-streamlined | 2026-11-13 |

Not yet confirmed: the statewide base rates of Alabama (old file 4%), Colorado (2.9%), Oklahoma (4.5%) and Utah (old file 6.10%, which is a combined figure); the state-group taxability lists for SaaS, digital goods and clothing in the old file (NY under $110, VT under $110, RI under $250 clothing thresholds; Texas 20% data processing exemption; Alabama 2% food rate; Missouri 1.225% and Tennessee 4% food rates); the old file's typical penalty ranges (5% to 10% late filing, 25% to 100% fraud) and the 3 to 4 year voluntary disclosure lookback.
