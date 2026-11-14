---
name: ri-sales-tax
description: "Rhode Island 7% sales/use tax, first-250-dollar clothing exemption, digital and software supplies, meals, 2026 lodging change, registration, RI-STR filing and explicit unresolved service/nexus details."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ri-sales-tax"
  jurisdiction: "US-RI"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Rhode Island sales and use tax, tax year 2026

> **General reference only.** Written by Codex. Not reviewed by an accountant. Apply the official sources to the taxpayer's facts and obtain qualified professional review before filing, paying or taking a tax position.

> **Circular 230 section 10.37:** Consider relevant facts, reasonable assumptions and applicable law. Evaluate federal tax implications using the federal owner skills and obtain professional review where needed.

**Answer first.** Rhode Island's general sales/use rate is 7%. Qualifying clothing and footwear receive an exemption for the **first USD 250 per item**, so only the excess is taxable. Meals and lodging have separate levies: prepared meals from qualifying establishments add 1%; ordinary short-term room or whole-home rentals generally total **14% from 1 January 2026**. Sources: [sales/use FAQ](https://tax.ri.gov/tax-sections/sales-excise-taxes/sales-use-tax); [active clothing rule 6.4](https://rules.sos.ri.gov/Regulations/part/280-20-70-6); [section 44-18-36.1, effective 2026 text](https://webserver.rilegislature.gov/Statutes/TITLE44/44-18/44-18-36.1_44-18-36.1.htm); [meals FAQ](https://tax.ri.gov/tax-sections/sales-excise-taxes/meals-beverage-tax).

## Scope

RI sellers, remote sellers with nexus, marketplace transactions, and purchasers owing use tax on taxable RI use without collected tax. Statewide general sales/use is separate from the local meals tax and hotel/whole-home rental taxes. Income and employer taxes belong to `ri-income-tax`, `ri-corporate-tax` and `ri-payroll`; multistate sales principles route to `us-sales-tax`. Preserve the existing `ri-sales-tax` slug. Original contributor attribution retained: **Open Accounting Skills Registry**.

## Ask the client first

1. Physical presence, employees, inventory, channels, marketplace collection and prior/current RI receipts/transaction counts.
2. Itemized product/service description, delivery/use location and date, including software access and digital subscriptions.
3. Per-item clothing price, accessories/protective use, alterations, shipping and bundled charges.
4. Exemption/resale certificates, manufacturing use and other-state tax paid on purchases.
5. Meals establishment status, lodging type/location/length, platform receipts and separate tax accounts.
6. Permit, assigned filing frequency, gross/taxable sales, deductions, collections and outstanding periods.

## The method, step by step

### Rates, bands and thresholds

| Item | Rate, amount and effective period | Official source |
|---|---|---|
| General retail sales/use | 7% statewide, no additional general municipal sales rate used in this computation | [sales/use FAQ](https://tax.ri.gov/tax-sections/sales-excise-taxes/sales-use-tax) |
| Qualifying clothing/footwear | First USD 250 of each item's sales price exempt; excess at 7%; accessories, athletic/protective exceptions apply | [active rule 6.3 to 6.4](https://rules.sos.ri.gov/Regulations/part/280-20-70-6) |
| Local meals/beverage | 1% of qualifying eating/drinking establishment taxable food receipts, in addition to general 7% | [rate and coverage](https://tax.ri.gov/tax-sections/sales-excise-taxes/meals-beverage-tax) |
| Short-term room lodging, 2026 | 5% hotel + 2% local hotel + 7% sales = 14%, subject to coverage/special rules | [2026 subsections a/b](https://webserver.rilegislature.gov/Statutes/TITLE44/44-18/44-18-36.1_44-18-36.1.htm) |
| Whole dwelling short-term rental, 2026 | New 5% whole-home + 2% local hotel + 7% sales = 14%, subject to coverage/special rules | [2026 subsections b/d](https://webserver.rilegislature.gov/Statutes/TITLE44/44-18/44-18-36.1_44-18-36.1.htm); [January 2026 advisory](https://tax.ri.gov/sites/g/files/xkgbur541/files/2026-01/ADV_2026_02_Tax-Changes.pdf) |
| Quarterly sales filing permission | Average monthly liability below USD 200 for six consecutive months plus written approval; not automatic | [filing frequency FAQ](https://tax.ri.gov/tax-sections/sales-excise-taxes/sales-use-tax) |

1. Determine nexus and account registration before collecting. The current remote-seller webpage still frames USD 100,000 receipts or 200 transactions using **calendar 2018**. That is a historical implementation paragraph, not sufficient evidence of the recurring **2026** measurement period or every marketplace exclusion. The old current/prior-year claim and exact 2026 remote thresholds are **Not yet confirmed** from a current operative statute; physically present sellers cannot treat the remote threshold as a general exemption. Source: [remote sellers page, historical 2018 wording](https://tax.ri.gov/tax-sections/sales-excise-taxes/remote-sellers).
2. Register through the Division's Business Application and Registration (BAR)/online route, select the correct sales account and location, and retain permit/account confirmation. Streamlined Sales Tax registration is another registration route identified by the Division; it does not itself determine product taxability. Keep resale/exemption certificates and match the purchaser/use/transaction to their conditions. Source: [registration, resale and exemption FAQ](https://tax.ri.gov/tax-sections/sales-excise-taxes/sales-use-tax).
3. Classify goods and taxable services, calculate taxable receipts after supported exemptions/returns, and collect 7%. A retail resale purchase can qualify under the certificate process, while consumption by the business can create use tax. Accrual reporting generally follows sales, rather than waiting for customer cash. Zero returns remain required while the account is open. Source: [retail sale, use tax, accrual and zero-return FAQ](https://tax.ri.gov/tax-sections/sales-excise-taxes/sales-use-tax).
4. For qualifying clothing/footwear, compute max(item sales price less USD 250, zero) **per item**, rather than taxing an entire USD 260 item. Clothing accessories such as jewelry, handbags and watches, and special athletic/protective items, do not automatically qualify. Count normally sold single units together; include taxable alterations/delivery in item sales price and allocate mixed-shipment delivery under the active rule. Source: [definitions and worked allocation examples](https://rules.sos.ri.gov/Regulations/part/280-20-70-6).
5. Food/food ingredients can be exempt, but candy, soft drinks, supplements, alcohol, vending and prepared-food exclusions require the statutory definitions and exceptions. Prescription drugs, insulin/medical oxygen, home-use DME, prescription prosthetics and hearing/mobility equipment have specific statutory conditions; the old blanket medical-device exemption is too broad. Qualifying manufacturing components and machinery require the statutory manufacturing/use conditions, not merely a manufacturer's purchase. Source: [section 44-18-30, paragraphs 7, 9 to 11 and 27](https://webserver.rilegislature.gov/Statutes/TITLE44/44-18/44-18-30.HTM).
6. RI taxes vendor-hosted **prewritten** software; the 2020-03 ruling confirms that result for its stated facts. Do not classify all cloud services as taxable merely because delivered online. Specified digital books, movies, music and streaming subscriptions fall within the digital-products levy. The old claim that all custom programming is exempt is **Not yet confirmed** for a transaction without reading its contract and applicable rule. Sources: [ruling 2020-03, facts and conclusion](https://tax.ri.gov/guidance/declaratory-rulings/ruling-request-no-2020-03); [ADV 2019-22, definitions and 7% rate](https://tax.ri.gov/sites/g/files/xkgbur541/files/Advisory/ADV_2019_22.pdf).
7. Keep separate meals and lodging workpapers and accounts. Qualifying meals add 1% to 7%. For 2026 lodging, replace the old 13% room example: enacted law increases local hotel tax to 2% and imposes a new 5% whole-home tax. An undated hotel FAQ still says whole-home 1%; the dated statute and January 2026 advisory control this skill's 2026 computation. Newport collection and longer stays require the applicable route/definitions. Source: [current effective statutory text](https://webserver.rilegislature.gov/Statutes/TITLE44/44-18/44-18-36.1_44-18-36.1.htm); [dated 2026 change advisory](https://tax.ri.gov/sites/g/files/xkgbur541/files/2026-01/ADV_2026_02_Tax-Changes.pdf).
8. Calculate use tax for taxable in-state use where seller did not collect the correct RI tax; assess allowable credit for tax properly paid elsewhere under the applicable rule. Individuals may report personal use tax on RI-1040 as described by the FAQ. Retain invoices, tax evidence and business/personal allocation. Source: [use-tax FAQ](https://tax.ri.gov/tax-sections/sales-excise-taxes/sales-use-tax).

## Boundary and exception table

| Legacy topic retained | Confirmed treatment or explicit limit |
|---|---|
| SaaS, downloaded prewritten software, custom software, mixed digital bundle | Prewritten vendor-hosted software and specified digital products supported above; custom and mixed-service allocation need transaction-specific confirmation |
| Groceries versus prepared food | Statutory food exemptions have exclusions; restaurant qualifying food generally 7% +1% |
| Professional services: legal, accounting, medical, engineering; haircuts, education, financial advice | **Not yet confirmed** as blanket exemptions; distinguish service from taxable goods/software/bundles |
| Telecommunications/cable, storage, pet grooming, commercial cleaning, laundry/dry cleaning, pest control, security, printing | **Not yet confirmed** individually from current rules; old blanket 7% list must not decide a return |
| Manufacturing machinery, raw materials, components, resale | Preserve topic; apply statutory use conditions and certificate evidence; do not exempt all operating purchases |
| Marketplace collection | Reconcile platform statements and direct sales; seller nexus/reporting exclusions require current confirmation |
| VDA and old three-year lookback/interest nonwaiver | **Not yet confirmed**; obtain current Division terms before assuming relief or period limitation |
| Old penalty 10% or USD 50; fraud 50% | **Not yet confirmed**; not usable as an automatic penalty calculation |
| Interest | Calendar 2026 published delinquency rate is 18% for trust-fund taxes and 12% for nontrust taxes; use actual tax classification and accrual period, not 2027 assumptions |

Interest source: [calendar-year interest table](https://tax.ri.gov/guidance/information-and-faqs/interest-rates).

## Worked cases

**Case 1, ordinary mixed retail sale.** Invented sale has USD 1,000 taxable electronics plus one USD 200 qualifying jacket. Taxable receipts are USD 1,000; 7% tax USD 70 and invoice USD 1,270. With no seller collection, the same taxable electronics could create USD 70 use tax before allowable credits.

```oa-check
name: Rhode Island ordinary retail and clothing exemption
inputs:
  electronics: 1000
  jacket: 200
steps:
  - tax: electronics * 0.07
  - invoice: electronics + jacket + tax
expected:
  tax: 70
  invoice: 1270
```

**Case 2, clothing boundary decision.** Compare otherwise qualifying everyday footwear USD 249 and USD 260. First pair is exempt, second has only USD 10 taxable, tax **USD 0.70**, not USD 18.20. A USD 300 qualifying pair has USD 50 taxable, tax USD 3.50, not the old USD 21. Accessories/protective footwear can change the eligibility decision entirely.

```oa-check
name: Rhode Island first 250 dollars exempt per clothing item
inputs:
  below: 249
  above: 260
  higher: 300
steps:
  - below_tax: max(below - 250, 0) * 0.07
  - above_tax: max(above - 250, 0) * 0.07
  - higher_tax: max(higher - 250, 0) * 0.07
expected:
  below_tax: 0
  above_tax: 0.7
  higher_tax: 3.5
```

### Other old examples, corrected or bounded

| Invented transaction | Result and limit |
|---|---|
| Qualifying coat USD 240 and dress USD 260 | Only USD 10 taxable; USD 0.70 tax |
| Qualifying clothing USD 50 +100 +260 +249 | Only USD 10 taxable; USD 0.70 tax, item-by-item |
| Vendor-hosted prewritten taxable SaaS USD 500 | USD 35 tax, subject to RI sourcing and contract classification |
| Qualifying meal USD 80 | Sales USD 5.60 + meals USD 0.80 = USD 6.40; total USD 86.40 |
| Three short-term hotel nights USD 200 each in 2026 | USD 600 x14% = USD 84; total USD 684, replacing old USD 78/678 |
| Taxable digital book USD 25 | USD 1.75 tax; total USD 26.75 |
| Taxable prewritten SaaS USD 200 + streaming USD 50 + taxable goods USD 100 | If each is separately confirmed taxable and RI sourced, USD 350 x7% = USD 24.50 |
| VDA hypothetical | No automatic three-year lookback or penalty waiver assumed; refer with actual facts |

## When to refuse or refer

Refer unresolved remote nexus, marketplace exclusions, service/custom-software classification, bundled transactions, special certificates, hotel/platform/Newport exceptions, VDA and penalty disputes. Do not use an unsupported historical FAQ as confirmation of 2026 nexus measurement. Ordinary retail and qualifying clothing calculations above have current primary support.

## Filing and payment

Use https://taxportal.ri.gov, choose sales/use and period, reconcile gross sales, exempt/deductible sales, taxable sales, use-tax purchases and tax, submit **RI-STR** and retain acceptance. Pay the correct account/period and retain separate payment confirmation. General monthly sales returns/payment are due by the **20th** following month; approved quarterly sales returns/payment by the **last day** of April, July, October and January. Quarterly permission requires written approval after the below-USD-200 six-month test; the old assumption of annual filing for small taxpayers is **Not yet confirmed**. Source: [filing and payment FAQ](https://tax.ri.gov/tax-sections/sales-excise-taxes/sales-use-tax).

Form **T-204R-Annual** is discontinued from tax year 2023 onward; RI-STR includes periodic reconciliation. Do not follow the old annual-reconciliation instruction for current general sales. Alcohol/writer special reconciliations have their own later changes, outside the ordinary retailer computation. Source: [official form discontinuance](https://tax.ri.gov/sites/g/files/xkgbur541/files/2024-01/T-204R%20Discontinuance%20Effective%20TY2023.pdf).

Meals follow sales-account frequency, but their page specifies monthly due 20th and quarterly due **30th**, so do not substitute the general-sales quarter-end rule. Hotel returns are monthly, generally 20th following month, with HOM/RI-8478 by lodging type; exact 2026 whole-home forms and Newport route require final-period confirmation. Source: [meals due dates](https://tax.ri.gov/tax-sections/sales-excise-taxes/meals-beverage-tax); [collection law](https://webserver.rilegislature.gov/Statutes/TITLE44/44-18/44-18-36.1_44-18-36.1.htm).

## Completion checklist

- Nexus/registration and product-specific taxability documented; unresolved classifications referred.
- Clothing exemption applied per item; food, medical, manufacturing and resale conditions evidenced.
- 2026 meals/lodging levies separated; old 13% lodging and entire-item clothing errors removed.
- RI-STR sales/use workpaper reconciled, assigned frequency followed, acceptance/payment retained.

## Sources

| Official source and scope actually read | URL | Read on |
|---|---|---|
| Read for Sales/use FAQ: general rate, registration, retail/resale/use, accrual, monthly/approved quarterly and zero returns. | https://tax.ri.gov/tax-sections/sales-excise-taxes/sales-use-tax | 2026-11-13 |
| Read for Active 280-RICR-20-70-6: definitions, USD 250 excess-only rule, alterations/delivery and examples; inactive archived version not used as current authority. | https://rules.sos.ri.gov/Regulations/part/280-20-70-6 | 2026-11-13 |
| Read for Section 44-18-30: manufacturing paragraph 7, food paragraph 9, medical paragraphs 10/11 and clothing paragraph 27, neighboring exceptions read. | https://webserver.rilegislature.gov/Statutes/TITLE44/44-18/44-18-30.HTM | 2026-11-13 |
| Read for Section 44-18-36.1: both pre-2026 and effective-2026 texts, hotel/local/whole-home levies and Newport exceptions. | https://webserver.rilegislature.gov/Statutes/TITLE44/44-18/44-18-36.1_44-18-36.1.htm | 2026-11-13 |
| Read for ADV 2026-02: January 2026 hotel/local/whole-home changes and neighboring credit changes; dated primary source overrides stale FAQ. | https://tax.ri.gov/sites/g/files/xkgbur541/files/2026-01/ADV_2026_02_Tax-Changes.pdf | 2026-11-13 |
| Read for Meals FAQ: coverage, 1%, registration, frequency, separate monthly 20th/quarterly 30th rules. | https://tax.ri.gov/tax-sections/sales-excise-taxes/meals-beverage-tax | 2026-11-13 |
| Read for ADV 2019-22: specified digital definitions, subscriptions, rate and nexus/registration paragraphs; historical filing/payment wording not treated as current. | https://tax.ri.gov/sites/g/files/xkgbur541/files/Advisory/ADV_2019_22.pdf | 2026-11-13 |
| Read for Ruling 2020-03: taxpayer facts, vendor-hosted prewritten software classification, RI sourcing, conclusion and reliance limitation. | https://tax.ri.gov/guidance/declaratory-rulings/ruling-request-no-2020-03 | 2026-11-13 |
| Read for T-204R official discontinuance: 2023-onward general annual reconciliation replaced by periodic RI-STR. | https://tax.ri.gov/sites/g/files/xkgbur541/files/2024-01/T-204R%20Discontinuance%20Effective%20TY2023.pdf | 2026-11-13 |
| Read for Remote sellers page: USD 100,000 /200 tests expressly tied to calendar 2018; current 2026 measurement not established. | https://tax.ri.gov/tax-sections/sales-excise-taxes/remote-sellers | 2026-11-13 |
| Read for Interest-rates table: calendar 2026 trust/nontrust delinquency and refund rates, neighboring years distinguished. | https://tax.ri.gov/guidance/information-and-faqs/interest-rates | 2026-11-13 |

Not yet confirmed: final 2026 RI-STR and lodging form line mapping; operative 2026 remote nexus measurement/marketplace exclusions; custom software and each service classification in the exception table; exact general-sales penalties/fraud/VDA relief; current resale/manufacturing certificate variants; special lodging duration/platform/Newport mechanics. Old annual small-filer assertion and broad exempt-service list remain unconfirmed. Old TaxJar and SalesTaxHandbook vendor sources are replaced by primary state materials; their claims are retained only where supported or explicitly limited above.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ri-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ri-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
