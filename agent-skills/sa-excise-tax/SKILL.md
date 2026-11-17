---
name: sa-excise-tax
description: "Saudi Arabia excise computation and compliance for 2026: tobacco, energy drinks, electronic-smoking devices/liquids and the sugar-tier volumetric model for sweetened drinks. Determine product composition, exclusions, retail-price tax status, release from suspension, registration and the correct return period before computing. Covers imports, licensed warehouses, movement/loss evidence, records and penalties. Preserves the original 2025 tobacco, cola and dairy examples as historical cases and supplies current-year beverage comparisons. Read before Saudi excise work; uncertain composition or price evidence stops filing."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/sa-excise-tax"
  jurisdiction: "SA"
  tax_year: "2026"
  last_updated: "2026-11-16"
---

# Saudi Arabia excise tax: 2026

## Scope

Read before Saudi excise classification, computation, registration or return work. The **Excise Tax Law is Royal Decree M/86 dated 27/8/1438H**, not the old skill's A/86. Use the current implementing regulation including decision **25-06-06**, and the product/dilution decision linked by ZATCA. The 2026 amendments apply from **1 January 2026**. [Law cover](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Excise%20Goods%20Tax%20Law.pdf); [current regulation cover and arts. 1-4](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf); [effective-date announcement](https://zatca.gov.sa/en/MediaCenter/News/Pages/excise-tax-regulation-2026.aspx).

**Quick reference:** in **2026**, tobacco, energy drinks and the defined electronic-smoking devices/liquids retain ad-valorem treatment; sweetened drinks, including qualifying sweetened carbonated drinks, use **total sugar per volume and a tax per litre**. Read the table below. The old flat sweetened/carbonated percentage is historical, not the current beverage computation. Licensed warehouse returns cover two-month periods and are due by the end of the following month. An importer declaring at customs follows a separate path.

Work at SKU/product and release level. This skill does not compute VAT or customs, foreign GCC excise, alcohol/other-product assumptions, private rulings or a live disputed assessment. Load [VAT](saudi-arabia-vat.md) for the separate VAT base including any applicable excise, and obtain destination-country rules for cross-border movements. Outputs remain working papers requiring qualified Saudi review.

## Ask the client first

1. Entity, ZATCA excise registration, importer/producer/licensed-keeper role, actual activity, warehouse licences and period under review.
2. Each SKU's composition, label/marketing, total and added sugar/sweeteners, milk/plant-alternative percentage, nutritional/lab evidence, tariff classification and product registration.
3. Unit size, litres, dilution instructions/yield, actual quantities imported/produced/released, movements, remaining suspension stock and loss/destruction reports.
4. For ad-valorem goods: documented final-consumer price, whether it includes VAT/excise, ZATCA reference/standard price and the precise basis/date for each comparison.
5. Customs entries, warehouse movement receipts, export/discharge evidence, stamps, guarantees and reconciliation of physical versus electronic records.
6. Prior returns/payments, adjustments/refunds, authority notices, disputed classifications and any penalty-initiative eligibility.

Missing SKU, composition, price basis or movement evidence is a hold. Do not invent an energy-drink classification, assume an old sweetened-drink rate or apply an authority-only default dilution as the taxpayer's established facts.

## The method, step by step

### 1. Identify the product and current rate

Apply the operative product definitions and tariff descriptions, not a broad “sin tax” label. Tobacco includes the specified chapter/tariff products; check exclusions for the listed cessation/medical products rather than assuming every nicotine-related item has identical treatment. Energy drinks follow the marketed/sold-as-energy definition and specified stimulants and preparations; a coffee-style drink is not an energy drink solely because it contains caffeine. Electronic-smoking goods follow their specified devices, parts and liquid classifications, including the stated nicotine/tobacco-independent scope. A medical nebuliser is not automatically a smoking device. [IR arts. 1-3](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf); [product decision, tobacco/energy/device/liquid sections](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/DecisionRegardingExciseTax-Dec2025.pdf).

| Product or sweetened-drink tier | 2026 rate and exact conditions | Official source |
|---|---|---|
| Defined tobacco products | 100% of the statutory tax-exclusive base | IR art. 3(1), [regulation](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf) |
| Defined energy drinks | 100% of the statutory tax-exclusive base; not the sweetened-drink volumetric model | IR art. 3(2), [regulation](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf) |
| Defined electronic-smoking devices/tools | 100% of the statutory tax-exclusive base | IR art. 3(4), [regulation](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf) |
| Defined liquids for electronic-smoking devices | 100% of the statutory tax-exclusive base | IR art. 3(5), [regulation](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf) |
| Sweetened tier 1: sugar-free, only artificial sweeteners | SAR 0 per litre; an in-scope zero-rate tier is not the same as an excluded product | IR arts. 2(1)(c), 3(3), [regulation](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf) |
| Sweetened tier 2: total sugar **below 5 g/100 ml** | SAR 0 per litre | IR arts. 2(1)(c), 3(3), [regulation](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf) |
| Sweetened tier 3: total sugar **5 through 7.99 g/100 ml** | SAR 0.79 per litre | IR arts. 2(1)(c), 3(3), [regulation](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf) |
| Sweetened tier 4: total sugar **8 g/100 ml or more** | SAR 1.09 per litre | IR arts. 2(1)(c), 3(3), [regulation](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf) |
| Milk-content exclusion | At least 75% qualifying milk in the ready-to-drink content; apply the milk definition and other product conditions | Product decision, sweetened-drink exclusions/definitions, [decision](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/DecisionRegardingExciseTax-Dec2025.pdf) |
| Qualifying manufactured plant-milk alternative exclusion | At least 75% of the ready-to-drink content and the full applicable alternative definition; do not treat every plant drink as qualifying milk | Product decision, exclusions/definitions, [decision](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/DecisionRegardingExciseTax-Dec2025.pdf) |

For a drink with added sugar or another sweetener, the volumetric classification uses **total sugar**, including natural and added sugar and sugar from other sweeteners. Artificial sweetener added alongside sugar does not remove the sugar measurement. Simply mixing unsweetened natural fruit/vegetable juices or concentrates is not necessarily adding a sweetener. Carbonation alone is not a separate current flat-rate class; classify the actual sweetened product and exclusions. [Product decision, sweetened-drink definition and sugar sections](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/DecisionRegardingExciseTax-Dec2025.pdf).

### 2. Read the neighboring exclusions and definitions

The sweetened-drink exclusion list includes energy drinks taxed separately, qualifying **100% natural fruit/vegetable juice without added sugar/other sweetener**, specified milk/dairy/plant alternatives, infant products, defined dietary/medical products and specified personal/non-commercial or open-container restaurant preparation. Do not label a packaged sweetened product exempt merely because it is sold by a restaurant or contains fruit. The relevant GCC technical definitions remain conditions, not marketing claims. [Product decision, sweetened-drink exclusions](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/DecisionRegardingExciseTax-Dec2025.pdf).

Qualifying milk types include animal/reconstituted/powdered milk, yoghurt and whey as defined; **cream is excluded from that milk definition**. A plant milk-alternative classification also requires the combined conditions: **120 mg calcium per 100 ml**, plant source, milk-like uses and density, and no carbonated component. Keep composition and lab/label evidence. “Chocolate milk” by itself does not establish the milk-content exemption. [Product decision, milk and alternative definitions](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/DecisionRegardingExciseTax-Dec2025.pdf).

Concentrates, powders, gels and extracts are within the relevant energy/sweetened definitions. For sweetened preparations, determine total sugar in the **final prepared drink**, using supported label dilution and final litres, not only the concentrate's container volume. Preserve the preparation instructions and yield calculation. ZATCA may demand approved-laboratory evidence, reject unsubstantiated product registration and require corrected data. [IR arts. 4(3)-(4), 22 bis](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf); [dilution decision](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/DecisionRegardingExciseTax-Dec2025.pdf).

Where dilution instructions are absent, unreliable or inconsistent with comparable products, the decision gives **ZATCA**, not the writer, authority to adopt an alternative. Its stated default is at least **6 parts diluent to 1 part concentrate**, with the high-sugar tier and the stated exceptions where actual liquid-concentrate nutrition shows an artificial-only or low-sugar product. Do not silently misread that as 6 total parts or treat it as a taxpayer's elective ratio. Hold unsupported inputs for classification/authority resolution. [Dilution decision, alternative/default-ratio paragraphs](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/DecisionRegardingExciseTax-Dec2025.pdf).

If more than one actual statutory rate applies, IR art. 4(6) prescribes the higher rate; that rule does not authorise inventing a classification because facts are missing. [IR art. 4(5)-(6)](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf).

### 3. Identify release, suspension and liable person

Excise becomes due on the defined release for consumption: import outside suspension, production outside suspension, release from suspension, possession outside suspension of goods with unpaid tax and the specified loss/destruction cases. Identify the liable importer/producer/licensee/other releaser or commercial possessor, including the statutory knowledge/stamp rule and joint liability where applicable. Not every retail sale creates a second charge. [IR arts. 5, 7](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf).

Suspension applies only under the licensed regime and controlled movements: licensed production/holding and qualifying movements between authorised warehouses, import to an authorised warehouse or export movements under the stated rules. A warehouse is not a suspension facility merely because stock is physically stored there. Obtain current licences, movement documents, destination receipt and discharge/export evidence and reconcile the electronic inventory. [Law arts. 6, 10-13](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Excise%20Goods%20Tax%20Law.pdf); [IR arts. 6, 20-30 and movement provisions](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf).

Loss/destruction under suspension is not automatically exempt or automatically taxable merely from whether a supervisor was present. IR art. 5(5) requires evidence of causes beyond the licensee's control and the prescribed notice: **within 7 days**, authority decision **within 14 days**, with its stated one-time extension and no-response consequence. Missing notice or insufficient/untrue evidence can make the loss a release at that time. Preserve the full report and authority response; do not simply write stock off. [IR art. 5(5)](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf).

Exports under suspension are not generic “zero-rated sales”; establish non-release/discharge or the applicable refund route. Prior excise paid on inputs, exports and overpayments have specific deduction/refund conditions. Do not offset tax merely because an accounting credit note or damaged-stock entry exists. Read the actual applicable return/refund route and keep proof. [Law arts. 16-17](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Excise%20Goods%20Tax%20Law.pdf); [IR arts. 46-51](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf).

### 4. Compute the appropriate base

**Ad-valorem classes:** IR art. 1 compares the relevant declared retail, authority reference and GCC standard prices on the required basis **excluding excise and VAT**, using the highest applicable amount. IR art. 8 defines retail consumer price as including taxes/fees/burdens, so first reconcile each price's tax status. Do not multiply a tax-inclusive shelf price as though it were a tax-exclusive base. Keep price lists, actual retail invoices and the authority price/effective date. Authority reference/standard prices in an example are hypothetical unless the SKU's official price record has been obtained. [IR arts. 1, 4(1), 8](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf).

If a supported consumer price is already net of VAT but includes ad-valorem excise, the **derived** tax-exclusive base is that price divided by **1 + the excise rate**. If VAT is also included, first apply the separate [VAT](saudi-arabia-vat.md) rules to establish the comparable net-of-VAT amount; do not assume the quoted price's tax basis. Compare consistently established values and multiply the statutory base by the applicable ad-valorem rate.

**Sweetened drinks:** release litres × the legally established tier's SAR-per-litre rate. Convert actual unit volume to litres; for concentrates use supported finished-drink yield. Do not use the retail-price maximum for this volumetric calculation. An excluded product, an in-scope tier with no charge and a suspended taxable product have different legal reasons for a zero current amount. [IR arts. 2-4](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf).

Apply the rate in force at the **actual release date**. Carry stock in suspension by quantity and SKU and classify a later release under the then-current law; do not tax an entire imported consignment merely because it arrived, if valid suspension applies. For transitional stock already released, obtain the actual transition instrument/notice before any extra charge or refund. [IR arts. 4-7, 54](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf).

### 5. Reconcile and produce the return workpaper

For each licensed warehouse: opening stock + imports/production/receipts − approved outward suspension movements − releases − documented losses/destruction = closing stock, with the actual classification of each movement. Investigate every unexplained variance before filing. Track stamps separately, including issued, applied, activated, unused and cancelled quantities where required. Tobacco and energy drinks are specified stamped classes under the current art. 9; use the actual implementation/activation requirements rather than assuming every electronic-smoking product has the same stamp obligation. [IR arts. 9-14, 16, 22](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf).

The liability schedule must show SKU, composition/tier or ad-valorem base, unit volume/yield, period, release quantity, rate, tax, prior payment/deduction and supporting document. Link that schedule to the excise return's product calculation, warehouse-licence/release data and stamp information. Customs-import declarations and corrections remain separately reconciled to avoid taxing the same release twice. [IR arts. 15-18](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf).

## Boundary and exception table

| Boundary | Required result |
|---|---|
| Borderline energy/ordinary drink or sweetened/unsweetened product | Obtain composition, marketing and statutory classification; no automatic high-rate guess. |
| Flavoured milk/plant drink, juice, diet or medical product | Apply the complete definition/exclusion and evidence; flavour/sugar alone does not settle liability. |
| Missing price/reference or inconsistent tax inclusions | Hold the ad-valorem base until comparable evidence exists. |
| Missing dilution/lab evidence | Do not invent the yield or tier; obtain the approved evidence/authority resolution. |
| Unlicensed warehouse or unverifiable destination licence | Do not claim suspension from storage alone; refer the actual release and registration exposure. |
| Unexplained loss/export/inventory movement | Preserve records and test the relevant legal conditions, not a generic write-off or zero-rating. |
| Another GCC country | Verify destination law and actual movement controls; a GCC framework is not proof of identical national rates/dates. |
| Confectionery/composite food or an old “distilled beverages” label | Verify whether the actual product is within the operative definition; no invented new excise category. |

## Worked cases

The original entities, products, quantities and **2025 dates** are preserved below. These are **2025-2026 filing-cycle** cases, not a retroactive application of the new 2026 drink rates. Price/reference amounts are **illustrative inputs**, not verified current ZATCA SKU prices.

### A. Riyadh Tobacco Imports LLC: price basis and release quantity

Preserve **October 2025**, **1,000,000 cigarettes = 50,000 packs of 20**, declared price **SAR 25/pack**, reference price **SAR 24/pack**, **40,000 packs released** and **10,000 left under valid licensed suspension**. The original SAR 1,000,000 tax is arithmetically correct **only if** the price inputs are confirmed tax-exclusive comparable bases under the historical rule. If instead both are retail amounts net of VAT but inclusive of excise, the resulting base is SAR 12.50/pack and excise **SAR 500,000** on the released packs. The original facts did not establish the price inclusions, so no unconditional tax result is justified. Do not tax the suspended 10,000 packs until the relevant release or other chargeable event. [IR arts. 1, 4-8](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf).

```oa-check
name: Riyadh Tobacco Imports LLC price-basis decision and suspended stock
inputs:
  cigarettes: 1000000
  cigarettes_per_pack: 20
  released_packs: 40000
  declared_price: 25
  reference_price: 24
  excise_rate: 1.00
steps:
  - total_packs: cigarettes / cigarettes_per_pack
  - suspended_packs: total_packs - released_packs
  - base_if_inputs_tax_exclusive: max(declared_price, reference_price)
  - tax_if_inputs_tax_exclusive: released_packs * base_if_inputs_tax_exclusive * excise_rate
  - base_if_inputs_include_excise_only: max(declared_price, reference_price) / (1 + excise_rate)
  - tax_if_inputs_include_excise_only: released_packs * base_if_inputs_include_excise_only * excise_rate
expected:
  total_packs: 50000
  suspended_packs: 10000
  tax_if_inputs_tax_exclusive: 1000000
  base_if_inputs_include_excise_only: 12.50
  tax_if_inputs_include_excise_only: 500000
```

### B. Jeddah Beverages Co.: retain the 2025 cola case and compare a 2026 release

Preserve **November 2025**, **5,000,000 cans**, **330 ml/can**, declared price **SAR 2** and reference **SAR 1.80**. Under the historical carbonated-drink class, the old **SAR 5,000,000** tax requires confirmed tax-exclusive price inputs; if those amounts instead include excise but exclude VAT, the old percentage applied to the tax-exclusive base gives **SAR 3,333,333.33**. Neither price inclusion can be invented. The November activity belongs with the applicable two-month return, not a standalone monthly return. [Historical goods description, carbonated class](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Commodities%20Subject%20to%20Excise%20Tax_ENG_v.01.pdf); [2025/2026 amendment comparison](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/%D8%AA%D8%B9%D8%AF%D9%8A%D9%84%D8%A7%D8%AA%20%D8%B9%D9%84%D9%89%20%D8%A7%D9%84%D9%84%D8%A7%D9%8A%D9%94%D8%AD%D8%A9%20%D8%A7%D9%84%D8%AA%D9%86%D9%81%D9%8A%D8%B0%D9%8A%D8%A9%20%D9%84%D9%86%D8%B8%D8%A7%D9%85%20%D8%A7%D9%84%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%A7%D9%86%D8%AA%D9%82%D8%A7%D9%8A%D9%94%D9%8A%D8%A9.pdf).

For a **separate illustrative 2026 release of the same quantity/volume**, assume the product is an in-scope sweetened drink, no energy/milk/other exclusion applies and approved evidence shows **7 g total sugar/100 ml**. Released volume is **1,650,000 litres** and tax **SAR 1,303,500**. If the evidence instead shows **8 g/100 ml**, the tax is **SAR 1,798,500**. The sugar evidence decides the tier; the old retail price is irrelevant to this current volumetric base. [IR arts. 2-4](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf).

```oa-check
name: Jeddah Beverages Co current 2026 sugar-tier decision
inputs:
  released_cans: 5000000
  ml_per_can: 330
  ml_per_litre: 1000
steps:
  - released_litres: released_cans * ml_per_can / ml_per_litre
  - medium_sugar_tax: released_litres * 0.79
  - high_sugar_tax: released_litres * 1.09
  - difference: high_sugar_tax - medium_sugar_tax
expected:
  released_litres: 1650000
  medium_sugar_tax: 1303500
  high_sugar_tax: 1798500
  difference: 495000
```

### C. Dammam Dairy: the missing milk proportion matters before sugar tier

Preserve **December 2025**, chocolate-flavoured milk with added sugar, **250 ml/unit**, declared price **SAR 3**, no assumed SKU reference and **2,000,000 units released**. The original unconditional **SAR 3,000,000** charge is unsupported: the milk-content exclusion was already part of the historical goods definitions. Obtain the ready-drink milk percentage, the actual milk definition and price basis before a historical computation. Merely being sweetened or not being pure unsweetened milk does not prove taxability. [Historical milk exclusions](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Commodities%20Subject%20to%20Excise%20Tax_ENG_v.01.pdf).

For a **separate illustrative 2026 release** of the same units/volume, there are **500,000 litres**. If qualifying milk reaches the statutory exclusion, the product is excluded and no sweetened-drink charge is computed. If it fails that exclusion, is otherwise in scope and supported total sugar is **6 g/100 ml**, medium-tier tax is **SAR 395,000**; at **8 g/100 ml** it is **SAR 545,000**. Do not choose the taxable branch without composition evidence. [Product decision, milk definition/exclusion](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/DecisionRegardingExciseTax-Dec2025.pdf); [IR arts. 2-4](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf).

```oa-check
name: Dammam Dairy 2026 conditional taxable-branch volume and tier calculation
inputs:
  released_units: 2000000
  ml_per_unit: 250
  ml_per_litre: 1000
steps:
  - released_litres: released_units * ml_per_unit / ml_per_litre
  - tax_if_not_excluded_and_medium_sugar: released_litres * 0.79
  - tax_if_not_excluded_and_high_sugar: released_litres * 1.09
expected:
  released_litres: 500000
  tax_if_not_excluded_and_medium_sugar: 395000
  tax_if_not_excluded_and_high_sugar: 545000
```

For the **November-December 2025** return covering the historical cola/dairy period, ZATCA's official **2026 calendar expressly states 31 January 2026**. Do not resurrect the old monthly/15th deadline for that return. IR art. 57(2) extends a procedure deadline falling on an official holiday to the first following working day. Preserve the calendar statement and establish the actual notified/portal due date and applicable holiday treatment in the live workpaper; no substituted date is inferred here. [Official calendar](https://zatca.gov.sa/en/MediaCenter/Publications/Documents/Zakat%20Declaration%20and%20Tax%20Returns%20Calendar%20(EN).pdf); [IR art. 57(2)](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf).

## When to refuse or refer

Preserve all original refusal subjects:

- Importing/producing/holding under suspension without required registration or licence: do not prepare a purported compliant unregistered return; establish registration, historical releases and exposure with a specialist.
- Uncertain product, sweetener, energy, dairy/medical or new-scope classification: obtain the missing composition/label/tariff evidence and authority classification where necessary.
- Mixed consignment with no SKU breakdown: no unsupported apportionment.
- No documented retail price and no established reference/standard base: no ad-valorem figure.
- Unexplained warehouse reconciliation or unsupported loss/destruction: investigate, notify and test the actual charge/suspension conditions.
- Intra-GCC transfer: obtain both jurisdictions' operative movement treatment and discharge evidence.
- Customs clearance before registration: preserve customs records and refer retrospective compliance/exposure.
- Incomplete export or unverified receiving-warehouse licence: no assumed suspension/refund entitlement.
- Possible extension to sugar-containing food/composite products: check the current statutory definition; do not invent a broader tax or repeat an old flat drink rate.

Do not file on a guessed deadline, tier, price inclusion or guarantee. A difficult classification does not automatically justify the highest possible rate. Live disputes, evasion allegations, private rulings and non-Saudi GCC computations require specialist handling with the original documents.

## Filing and payment

1. **Register before the relevant activity:** law art. 6 covers import, production and holding under suspension. Submit the approved registration application with role/product information; obtain the actual approval, licence and guarantee conditions. Product registration under **IR art. 22 bis** is separate: register before release and update changed data by the next release as prescribed. Keep any approved-laboratory results and product records. [Law arts. 6-13](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Excise%20Goods%20Tax%20Law.pdf); [IR arts. 20-22 bis](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf).
2. **Import declaration:** declare the required tax calculation and information at import unless valid suspension or an actual approved deferral applies. Customs clearance does not certify the correctness of declared classification/value. Reconcile customs tax to warehouse releases; a licence does not automatically waive import tax. [IR arts. 15, 18](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf).
3. **Licensed warehouse return:** each tax period is **2 calendar months**, making **6 periods** in the financial year. File and pay by the **last day of the following month** under current IR arts. 16(1), 18(4). The official-holiday extension in art. 57(2) applies where its conditions are met; document the actual due date. Complete the approved excise return with licensee, product calculations, warehouse licence/releases and required stamps. The regulation permits the stated one-time first-short-period combination; obtain the actual authority treatment before combining periods. [IR arts. 16, 18](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf).
4. **Corrections/other disclosures:** apply the actual **15-day** correction/notification and non-suspension-possession rules in IR art. 17; these are not the current normal warehouse-return deadline. Reconcile an assessment to its written reasons, principal, penalty and due date before paying or objecting. [IR arts. 17-19](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf).
5. **Payment and evidence:** use the issued ZATCA payment reference and accepted channel; retain the return, tax calculation and payment receipt. Keep electronic commercial, product, stamp, production/import, inventory, release, movement, export, loss, guarantee and authority correspondence records that enable verification. Do not use a VAT retention period as proof of the excise period or destroy records during an open matter. [IR arts. 16, 18, 22 and audit provisions](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf).

### Statutory penalties and the separate temporary initiative

| Breach | Statutory sanction and conditions | Official source |
|---|---|---|
| Failure to submit the required excise return | 5%-25% of the tax that should have been declared | Excise Law art. 21, [law](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Excise%20Goods%20Tax%20Law.pdf) |
| Late payment | 5% of unpaid tax for each month or part month unpaid; no generic cap is stated in this article | Excise Law art. 22, [law](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Excise%20Goods%20Tax%20Law.pdf) |
| Tax evasion | Minimum the tax due; maximum **3 times the value of the excise goods involved**, not 3 times the unpaid tax | Excise Law arts. 19-20, [law](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Excise%20Goods%20Tax%20Law.pdf) |
| Obstruction, failure to provide requested information or other covered breach | Up to SAR 50,000 under the applicable classification/procedure | Excise Law art. 23, [law](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Excise%20Goods%20Tax%20Law.pdf) |
| Repeat same violation | Within 3 years after the earlier penalty decision becomes final, possible doubling or licence suspension up to 6 months | Excise Law art. 25, [law](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Excise%20Goods%20Tax%20Law.pdf) |

Unregistered performance of the listed activities is expressly addressed in the law's evasion provisions. Actual sanctions and procedure must follow the statutory conditions and decision; do not combine fictional administrative amounts with a generic penalty multiplier. Tax principal remains payable in addition to a sanction. Objections follow the current tax-committee procedural rules; preserve the notice and obtain specialist review. [Law arts. 19, 24-27](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Excise%20Goods%20Tax%20Law.pdf).

The **1 July-31 December 2026** initiative is a separate check for eligible unpaid fines, registration, required returns and principal settlement/approved adhered-to instalments. It excludes returns due **after 30 June 2026**, evasion, already-paid fines and the specified VAT fines; it does not waive principal or future defaults. Keep proof of the actual account treatment. [Initiative guideline pp. 3-9](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Cancellation-of-Fines-Exemption%20of-Financial-Penalties.pdf).

## Completion checklist

- Current product definition, exclusions, sugar/lab evidence and release date determine the rate; zero-tier and excluded goods are distinguished.
- Litres and supported dilution/yield recompute, or ad-valorem prices have a consistent tax-exclusive basis and effective date.
- Suspension, stamps, inventory, exports/losses, customs payments and current releases reconcile without duplicate tax.
- The correct role, registration, product data, two-month period and deadline are established; notices/corrections have their separate clock.
- Every original case and refusal has a destination; unresolved inputs and any historical rule are explicitly labelled before professional sign-off.

## Sources

| Official text | Actual reading |
|---|---|
| [Excise Tax Law, official Arabic consolidation](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Excise%20Goods%20Tax%20Law.pdf) | Read on 2026-11-16. Read for full text arts. 1-30 and cover/amendment notes: legal identity, liability, registration/licensing, returns/refunds, penalties and disputes. |
| [Current Excise Implementing Regulation](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Regulations-of-Excise-Tax.pdf) | Read on 2026-11-16. Read for arts. 1-9, 15-22 bis and relevant warehouse/movement/refund/audit boundaries. Product/rate/base and current deadline paragraphs were read with neighboring exceptions; this is not a claim to have reviewed every specialised warehouse procedure. |
| [2025 amendment comparison for 2026](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/%D8%AA%D8%B9%D8%AF%D9%8A%D9%84%D8%A7%D8%AA%20%D8%B9%D9%84%D9%89%20%D8%A7%D9%84%D9%84%D8%A7%D9%8A%D9%94%D8%AD%D8%A9%20%D8%A7%D9%84%D8%AA%D9%86%D9%81%D9%8A%D8%B0%D9%8A%D8%A9%20%D9%84%D9%86%D8%B8%D8%A7%D9%85%20%D8%A7%D9%84%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%A7%D9%86%D8%AA%D9%82%D8%A7%D9%8A%D9%94%D9%8A%D8%A9.pdf) | Read on 2026-11-16. Read for old/new product/rate/base definitions, return/payment timing and associated changes; old percentage rules are used only to identify the historical cases' limits. |
| [Product definitions and dilution/reference-price decision](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/DecisionRegardingExciseTax-Dec2025.pdf) | Read on 2026-11-16. Read for tobacco/energy/device/liquid definitions, sweetened exclusions, milk/alternative conditions and dilution/default powers. |
| [ZATCA effective-date announcement](https://zatca.gov.sa/en/MediaCenter/News/Pages/excise-tax-regulation-2026.aspx) | Read on 2026-11-16. Read for the operative 1 January 2026 change date and sugar-based methodology. The older overview pages' percentage/deadline descriptions do not override the amended regulation. |
| [Historical goods definitions, English](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Commodities%20Subject%20to%20Excise%20Tax_ENG_v.01.pdf) | Read on 2026-11-16. Read for historical carbonated/sweetened classes and milk-content exceptions; not a source for 2026 volumetric rates. |
| [Zakat Declaration and Tax Returns Calendar 2026](https://zatca.gov.sa/en/MediaCenter/Publications/Documents/Zakat%20Declaration%20and%20Tax%20Returns%20Calendar%20(EN).pdf) | Read on 2026-11-16. Read for the named November-December 2025 excise deadline and the 2026 excise period entries. |
| [Penalty initiative effective July 2026](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Cancellation-of-Fines-Exemption%20of-Financial-Penalties.pdf) | Read on 2026-11-16. Read for pp. 3-11 for period, exclusions, principal and instalment conditions. |

**Not yet confirmed:** the original GCC-agreement/GAZT-merger chronology and early-adopter claims, June 2017 commencement dates, a generic guarantee multiple of average monthly tax, automatic seizure or criminal-referral claims, licence-life-plus-retention guarantee rule, and unidentified SOCPA commentary; the old general 6-year record-retention claim and any longer record-class requirement before disposal; historical start dates for the 2019 device/sweetened extensions beyond the historical definition evidence; other GCC states' old implementation-date/rate table (UAE, Bahrain, Oman, Qatar, Kuwait); a general expansion to sugar-containing foods or an independent “distilled beverages” class; actual SKU reference/standard prices in the cases; case-specific price inclusions, dairy composition, guarantees and approved cross-border discharge; current portal box identifiers and specialised refund/transition entitlements. None of those old claims is a usable current rate, exemption or filing shortcut. Source/lab/authority evidence must resolve the relevant item before filing.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-16. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `sa-excise-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/sa-excise-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
