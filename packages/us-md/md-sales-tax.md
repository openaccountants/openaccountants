---
name: md-sales-tax
description: "Maryland sales/use tax: ordinary 6%, technology 3%, remote nexus, 2026 affiliate exemption, taxable patterns, Form202 and Maryland Tax Connect."
version: "2.1"
jurisdiction: US-MD
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: computation
category: state-tax
---

# Maryland sales and use tax, 2026

> **General reference only.** Source-cited draft, not approved by an accountant. For US Treasury Circular 230 §10.37 purposes this is general reference material; a qualified professional must check the facts, current law and forms before filing or taking a position.

## Who this applies to

Maryland sellers, marketplace sellers/facilitators and purchasers with an untaxed Maryland use. Load `us-sales-tax` for the general nexus and marketplace method; this skill owns the Maryland rules. Maryland is not a Streamlined Sales Tax member. The ordinary state rate has no local sales-tax add-on, but it is not the maximum rate for every product. Digital Advertising Gross Revenues Tax is a separate regime and is not computed here.

## Rates, bands and thresholds

| Item | Rate / boundary | Official source |
| --- | --- | --- |
| Ordinary taxable tangible property, clothing, prepared meals and digital products outside a special rule | 6%; no county or city sales-tax increment | [Tax-General 11-104](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=11-104) |
| Alcoholic beverages | 9% | [11-104](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=11-104) |
| Specified data, IT and software publishing services | 3%; classify the service and use location, not merely the invoice label | [11-104](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=11-104); [TB56](https://www.marylandcomptroller.gov/content/dam/mdcomp/tax/legal-publications/technical-bulletins/tb-56.pdf) |
| Cannabis | 12% in 2026 | [11-104](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=11-104) |
| Remote-seller economic nexus | Prior or current calendar year: gross Maryland delivery revenue **exceeds USD 100,000**, OR **200 or more** separate transactions | [Comptroller nexus alert](https://www.marylandcomptroller.gov/legal-library/sut-ta-sep-01-2018.html) |
| Ordinary timely vendor credit | 1.2% of first USD 6,000 tax and 0.9% of excess, capped at USD 500 per return; excludes purchaser's own use tax | [11-105](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=11-105) |
| Assigned-period return/payment | Ordinarily the 20th of following month; use the account's monthly, quarterly or other assigned period | [Business Tax Tip22](https://www.marylandcomptroller.gov/content/dam/mdcomp/tax/legal-publications/tips/business/bustip22.pdf) |

## The base

Use Maryland delivery/use facts. Ordinary retail tangible personal property and clothing are taxable unless a specific exemption applies. Do not describe every professional service as exempt: the taxable-service list and the technology classifications control. Digital codes/products, canned software and SaaS require the TB56 classification: enterprise software/data/IT services can fall under 3%; individual-use digital products remain subject to 6%. The former custom-software exemption was repealed from July 1, 2025. A bundled mixed service needs the bulletin's primary-purpose/bundling analysis, not a blanket software rate. [TB56](https://www.marylandcomptroller.gov/content/dam/mdcomp/tax/legal-publications/technical-bulletins/tb-56.pdf).

Qualifying off-premises grocery food sold by a substantial grocery/market business is exempt. That requires at least 10% grocery/market food sales at the location. Heated food, suitable sandwiches, salad/soup/dessert bars, party platters and small frozen-dessert containers are immediate-consumption exceptions; candy, soft/carbonated drinks, alcohol and cannabinoid beverages are outside the statutory food definition. Food-stamp purchases and other special food exemptions have their own conditions. [11-206](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=11-206).

Medicine, including prescription and qualifying nonprescription medicine, is exempt; toiletries are not all medicine. The statute separately exempts listed medical devices and supplies and specified infant/oral/menstrual care products. Manufacturing exemption requires direct and predominant use in production and the statutory site/property conditions; it is not an exemption for every factory purchase. Resale requires a valid, properly completed resale certificate and a genuine resale rather than business consumption. [11-211](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=11-211); [11-210](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=11-210); [Comptroller business overview](https://www.marylandcomptroller.gov/content/dam/mdcomp/tax/legal-publications/tips/misc/taxtip30.pdf).

From **July 1, 2026**, specified data/IT/software publishing services, digital products and digital codes sold within the same affiliated group are exempt. The definition incorporates IRC1504 and related parties in IRC267(b)(10)-(12). This later enactment supersedes TB56's original statement that affiliate transactions lack a general exemption. For earlier periods apply the then-effective rule. The 2026 alert also introduces conditional in-person elementary/secondary-school book-fair relief, expands the greater-than-USD1,000 bullion/coin exemption beyond its former location restriction, and provides certified Washington County target-redevelopment relief. Do not assume their conditions apply to ordinary retail sales. [May2026 alert](https://www.marylandcomptroller.gov/content/dam/mdcomp/tax/legal-publications/alerts/tax-alert-sales-and-use-tax-updates-2026-2027.pdf).

Authorized multiple-points-of-use certificates can shift collection/remittance responsibility for qualifying multistate technology purchases; retain consistent, supportable Maryland-use allocation and authorization. The further per-vendor certificate and two-year renewal changes start **January1, 2027**, not during 2026. Optional qualifying cash rounding effective May12, 2026 applies **after** computing tax on the unrounded taxable price. [TB56](https://www.marylandcomptroller.gov/content/dam/mdcomp/tax/legal-publications/technical-bulletins/tb-56.pdf); [2026-2027 alert](https://www.marylandcomptroller.gov/content/dam/mdcomp/tax/legal-publications/alerts/tax-alert-sales-and-use-tax-updates-2026-2027.pdf).

## Deadlines and filing

Register through the Comptroller's Combined Registration Application and use Maryland Tax Connect for the sales/use account. A remote seller exceeding either nexus test registers by the first day of the next month and begins collecting on sales after that registration deadline, subject to the alert's implementation rules. Physical Maryland nexus does not wait for the economic threshold. Keep marketplace-collected sales separate, reconcile seller/facilitator reports, and pay consumer use tax when a taxable Maryland purchase escaped seller collection. [Nexus alert](https://www.marylandcomptroller.gov/legal-library/sut-ta-sep-01-2018.html); [Tip22](https://www.marylandcomptroller.gov/content/dam/mdcomp/tax/legal-publications/tips/business/bustip22.pdf).

File Form202 for every assigned period, including zero activity until the account is closed. Reconcile gross sales, deductions/exemptions, each rate category, tax collected and use tax; retain certificates and payment confirmations. Payments of USD10,000 or more require electronic payment. The broad electronic-return mandate applies to periods beginning after December31, 2026. A filing extension or provider handoff does not erase the original payment obligation. [Tip22](https://www.marylandcomptroller.gov/content/dam/mdcomp/tax/legal-publications/tips/business/bustip22.pdf); [2026-2027 alert](https://www.marylandcomptroller.gov/content/dam/mdcomp/tax/legal-publications/alerts/tax-alert-sales-and-use-tax-updates-2026-2027.pdf).

## Penalties and interest

Late returns, unpaid collected tax and unreported use tax can attract interest, penalties and assessment. Obtain the actual period's assessment/rate and reconcile tax, interest, penalty and payments separately. The timely-vendor discount is conditional on timely filing and does not reduce one's own purchaser use tax. Do not use the typographical “.12” multiplier in one Tip22 instruction: the statute and prose specify **1.2% = .012** on the first USD6,000. Exact late-charge schedules are not confirmed here. [11-105](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=11-105).

## Cross-border points

Destination/use in Maryland controls the core sale; out-of-state billing alone is not proof of exemption. Check purchaser use and digital primary-use location, resale/exemption evidence, marketplace collection and physical presence before applying the remote thresholds. No local sales-tax increment should be added. Digital advertising is a separate gross-revenues-tax analysis; this skill makes no digital-advertising filing or rate determination.

## Two worked examples that recompute

**Ordinary retail sale and timely-return credit.** A registered Maryland retailer has USD20,000 taxable ordinary sales, no exemption and no other tax categories or use tax. It collects USD1,200; the timely vendor credit is USD14.40, so it remits USD1,185.60. The seller keeps collection liability separate from the conditional credit.

```oa-check
name: Maryland ordinary sale and timely vendor credit
inputs:
  sales: 20000
  rate: 0.06
  credit_rate: 0.012
steps:
  - tax: sales * rate
  - credit: tax * credit_rate
  - remittance: tax - credit
expected:
  tax: 1200
  credit: 14.4
  remittance: 1185.6
```

**Affiliate decision at the effective date.** A qualifying same-affiliated-group enterprise IT sale priced USD10,000 occurs June30 or July1, 2026. Assume it is otherwise a 3% Maryland service and no alternative exemption applies. June tax is USD300; the identical July sale is exempt. Do not apply the exemption retroactively.

```oa-check
name: Maryland affiliated IT sale effective-date decision
inputs:
  price: 10000
  rate: 0.03
  june_exempt: 0
  july_exempt: 1
steps:
  - june_tax: price * rate * (1 - june_exempt)
  - july_tax: price * rate * (1 - july_exempt)
expected:
  june_tax: 300
  july_tax: 0
```

## Ask the client first

1. What is sold, contract/bundle wording, purchaser type, delivery/use location and relevant NAICS classification?
2. Prior/current calendar-year Maryland gross receipts and transaction counts, physical presence, and marketplace collection evidence?
3. Sale/invoice/payment/service dates, affiliate ownership, exemption/resale or MPU documents and actual Maryland use?
4. Account registration, assigned filing periods, gross-to-net sales reconciliation, tax collected, untaxed purchases and payment history?
5. Any alcohol, cannabis, vehicle, tobacco, digital advertising or special-industry activity needing a distinct treatment?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Tax-General11-104. Read for all core rate categories and hierarchy. | https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=11-104 | 2026-11-13 |
| Technical Bulletin56. Read for technology/digital classifications, custom software, bundles and MPU. | https://www.marylandcomptroller.gov/content/dam/mdcomp/tax/legal-publications/technical-bulletins/tb-56.pdf | 2026-11-13 |
| Sales and Use Tax Updates2026-2027. Read for all effective dates, affiliate/book-fair/bullion/redevelopment relief, cash rounding and electronic filing. | https://www.marylandcomptroller.gov/content/dam/mdcomp/tax/legal-publications/alerts/tax-alert-sales-and-use-tax-updates-2026-2027.pdf | 2026-11-13 |
| Remote seller alert. Read for strict revenue and transaction thresholds, registration/collection timing. | https://www.marylandcomptroller.gov/legal-library/sut-ta-sep-01-2018.html | 2026-11-13 |
| Business Tax Tip22. Read for assigned periods, Form202, zero returns and payment channels. | https://www.marylandcomptroller.gov/content/dam/mdcomp/tax/legal-publications/tips/business/bustip22.pdf | 2026-11-13 |
| 11-206. Read for grocery definition, location and immediate-consumption exceptions. | https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=11-206 | 2026-11-13 |
| 11-210. Read for direct/predominant production exemption. | https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=11-210 | 2026-11-13 |
| 11-211. Read for medicine, medical and listed care exemptions. | https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=11-211 | 2026-11-13 |
| 11-105. Read for timely credit rates, cap and own-use exclusion. | https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=11-105 | 2026-11-13 |
| Business overview. Read for resale documentation and core tangible-property scope only, not superseded rates. | https://www.marylandcomptroller.gov/content/dam/mdcomp/tax/legal-publications/tips/misc/taxtip30.pdf | 2026-11-13 |

Not yet confirmed: exact late-interest/penalty schedules; specialized vehicle, tobacco, telecommunications and digital-advertising computations; detailed pre-July2025 contract transition cases and purchaser-specific MPU allocation approval. No maximum-all-products 6% claim is retained.
