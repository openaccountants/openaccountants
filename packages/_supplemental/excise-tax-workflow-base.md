---
name: excise-tax-workflow-base
description: "Shared 2026 preparation method for excise product classification, chargeable events, computations, duty suspension, movements, reliefs, returns and evidence. Includes bounded EU minimum-duty and UK levy examples; actual national rates, authorisations, exceptions and filing deadlines must come from the current country method. Customs duty, VAT, cannabis and warehouse licensing need their specialist methods."
version: 0.2
jurisdiction: GLOBAL
tax_year: 2026
last_updated: 2026-11-14
type: cross-country-method
category: foundation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# Excise Tax Workflow Base

## What this file is

Shared excise working-paper method. Country content supplies actual product coverage, rates, authorisations and filing rules. EU minima below are not national payable rates. A product can fall under customs, VAT, excise and environmental reporting separately. Internal [T1]/[T2]/[T3] tags are workpaper flags, not professional approval.

## Ask the client first

Obtain the country/territory, product specification and tariff code, composition and strength, quantities/measurement conditions, event date, supplier/customer, movement route and purpose, authorisations, warehouse and guarantee records, duty-paid/suspended status, stock losses and any relief evidence. For packaging obtain the taxable component and recycled mass evidence; for drinks obtain added-sugar status and sugar per volume. Missing classification, date or liable-person facts stop the affected calculation.

## Section 1 : Scope and assumptions

Excise duty is a tax on the production or sale of specific goods, typically:
- Energy products (motor fuel, heating fuel, gas, coal, electricity)
- Alcoholic beverages
- Tobacco products
- Sugar-sweetened beverages (UK and other country-specific regimes); standalone sugar duties are a separate product test
- Plastic / single-use plastic packaging
- Gambling
- Vehicle registration / luxury vehicle (some countries)

This workflow base assumes:
- The taxpayer is a producer, importer, distributor, or retailer of excisable goods
- Establish whether the particular goods and movement qualify for authorised warehousing or duty suspension; not every levy or retailer uses a bonded warehouse
- Use the actual local movement and reporting system where required. EU harmonised excise uses EMCS for covered suspended and commercial duty-paid movements; a US or other-country procedure is not an automatic equivalent. [EU common provisions](https://taxation-customs.ec.europa.eu/taxation/excise-duties/common-excise-duty-provisions_en).

## The method, step by step

### Step 1 : Determine excisable status

- **Determine excisable status:** preserve a line per product and date: actual statutory scope/classification, liable person, units and strength, national rate, reduced-rate eligibility and exemption evidence. Red diesel/agricultural fuel, scientific use and denatured alcohol are investigation topics, not worldwide exemptions. A minimum rate or proposal does not establish a national liability.

### Step 2 : Determine the chargeable event

- **Determine the chargeable event:** for EU harmonised excise, distinguish release for consumption from a valid suspended movement. Investigate warehouse departure, manufacture/import/holding outside suspension and movement irregularities against the applicable law. For other levies identify their actual production, import, removal or supply event. Do not apply the EU release rule to every environmental levy. [EU common provisions](https://taxation-customs.ec.europa.eu/taxation/excise-duties/common-excise-duty-provisions_en).

### Step 3 : Compute the duty

- **Compute the duty:** confirm whether the charge is specific per litre/kg/pack/stick, ad valorem on the prescribed price base, or combined. Never swap finished-product litres, pure-alcohol litres, hectolitres, degrees Plato and percentage ABV. EU beer may use Plato or ABV; wine/intermediate product minima below are per hectolitre, not automatically per degree. Test actual small-brewery/wine/distillery and low-strength relief conditions rather than assume entitlement. [EU alcohol](https://taxation-customs.ec.europa.eu/taxation/excise-duties/excise-duties-alcohol_en), [tobacco](https://taxation-customs.ec.europa.eu/taxation/excise-duties/excise-duties-tobacco_en).

### Step 4 : Apply duty-suspension and movements

- **Apply suspension and movements:** establish dispatch/receipt roles, destination eligibility, guarantee and actual eAD for suspended movements; distinguish the eSAD and certified consignor/consignee for covered commercial duty-paid EU movements. Reconcile physical receipt, document acceptance, discrepancy and tax-accounting status; successful arrival alone does not prove payment or create a universal destination tax charge. [EU common provisions](https://taxation-customs.ec.europa.eu/taxation/excise-duties/common-excise-duty-provisions_en).

### Step 5 : Pay the duty

- **Prepare return and payment:** obtain the actual regime's filing period, event, due date, payment/deferment authorisation and reference. There is no worldwide monthly return or one-month payment rule. A movement guarantee is not permission to defer payment. For example, HMRC requires payment/accounting before a warehouse removal for consumption unless the actual authorised procedure permits otherwise. [HMRC movements and payment](https://www.gov.uk/guidance/receiving-storing-and-moving-excise-goods).

### Step 6 : Track exemptions and reliefs

- **Track exemptions and reliefs:** retain separate eligibility/evidence questions for diplomatic/consular use, visiting forces, research, denatured alcohol, permitted personal production, renewable/biofuels and industrial/non-fuel use. Confirm the actual country/product law, authorisation, recipient and proof; the list grants no general exemption. Reconcile relief quantities to stock and movement records.

## Section 3 : EU harmonised excise framework

### 3.1 Energy products (Directive 2003/96/EC)

EU minima only, not national payable rates. Check product, actual use, national rates and any lawful derogation. The motor-fuel gasoil minimum does not replace the separate specific industrial/commercial-use category. [EC energy framework](https://taxation-customs.ec.europa.eu/taxation/excise-duties/excise-duties-energy_en).

| Product/use | EU minimum | Official source |
|---|---|---|
| Unleaded petrol, motor fuel | EUR 359 per 1,000 litres | [EC energy](https://taxation-customs.ec.europa.eu/taxation/excise-duties/excise-duties-energy_en) |
| Gasoil, ordinary motor fuel | EUR 330 per 1,000 litres | [EC energy](https://taxation-customs.ec.europa.eu/taxation/excise-duties/excise-duties-energy_en) |
| Gasoil, specified industrial/commercial motor uses | EUR 21 per 1,000 litres, only for the applicable category | [EC energy](https://taxation-customs.ec.europa.eu/taxation/excise-duties/excise-duties-energy_en) |
| Heating gasoil; heavy fuel oil; heating LPG | Respectively EUR 21 per 1,000 litres; EUR 15 per 1,000 kg; EUR 0 per 1,000 kg | [EC energy](https://taxation-customs.ec.europa.eu/taxation/excise-duties/excise-duties-energy_en) |
| Heating natural gas; coal/coke | Each EUR 0.15/GJ business, EUR 0.30/GJ non-business | [EC energy](https://taxation-customs.ec.europa.eu/taxation/excise-duties/excise-duties-energy_en) |
| Electricity | EUR 0.50/MWh business, EUR 1.00/MWh non-business | [EC energy](https://taxation-customs.ec.europa.eu/taxation/excise-duties/excise-duties-energy_en) |

### 3.2 Alcohol (Directives 92/83/EEC and 92/84/EEC)

| Product | EU minimum and basis | Official source |
|---|---|---|
| Beer | EUR 0.748 per hectolitre per degree Plato OR EUR 1.87 per hectolitre per degree of alcohol, according to the member state's basis | [EC alcohol](https://taxation-customs.ec.europa.eu/taxation/excise-duties/excise-duties-alcohol_en) |
| Still and sparkling wine | EUR 0 per hectolitre; a zero EU minimum does not establish a zero national rate | [EC alcohol](https://taxation-customs.ec.europa.eu/taxation/excise-duties/excise-duties-alcohol_en) |
| Intermediate products, including relevant fortified wines | EUR 45 per hectolitre | [EC alcohol](https://taxation-customs.ec.europa.eu/taxation/excise-duties/excise-duties-alcohol_en) |
| Ethyl alcohol/spirits | EUR 550 per hectolitre of pure alcohol | [EC alcohol](https://taxation-customs.ec.europa.eu/taxation/excise-duties/excise-duties-alcohol_en) |

Small independent producer and low-alcohol reliefs remain a country eligibility task. Do not apply an assumed across-the-board half-rate to every small producer. [EC alcohol](https://taxation-customs.ec.europa.eu/taxation/excise-duties/excise-duties-alcohol_en).

### 3.3 Tobacco (Directive 2011/64/EU)

| Product | EU minimum structure | Official source |
|---|---|---|
| Cigarettes | Overall excise at least EUR 90 per 1,000 AND 60% of weighted average retail selling price; member states charging at least EUR 115 per 1,000 need not meet the percentage minimum | [EC tobacco](https://taxation-customs.ec.europa.eu/taxation/excise-duties/excise-duties-tobacco_en) |
| Fine-cut smoking tobacco | 50% of weighted average retail selling price OR EUR 60/kg | [EC tobacco](https://taxation-customs.ec.europa.eu/taxation/excise-duties/excise-duties-tobacco_en) |
| Cigars/cigarillos | 5% of retail selling price OR EUR 12 per 1,000 items or kg | [EC tobacco](https://taxation-customs.ec.europa.eu/taxation/excise-duties/excise-duties-tobacco_en) |
| Other smoking tobacco | 20% of retail selling price OR EUR 22/kg | [EC tobacco](https://taxation-customs.ec.europa.eu/taxation/excise-duties/excise-duties-tobacco_en) |

For cigarettes apply the actual national specific-plus-ad-valorem structure and relevant base. The EU minimum is not a taxpayer's elected national rate; do not implement a pending directive proposal as enacted law. [EC tobacco](https://taxation-customs.ec.europa.eu/taxation/excise-duties/excise-duties-tobacco_en).

### 3.4 EMCS data flow

**EMCS data flow**

| Stage | Document |
| --- | --- |
| Dispatch | Validate the required eAD for suspension or eSAD for covered duty-paid movement, participant status and reference before dispatch |
| In transit | ARC referenced on transport documents |
| Receipt at destination | Match the applicable receipt report to physical quantities, shortages, rejection and evidence |
| Closure | Record actual accepted receipt/export or lawful alternative proof and system status; no assumed automatic tax clearance |
| Discrepancy / shortage | Establish actual loss/irregularity, evidence, competent territory, liable person and relief; do not automatically charge destination tax |

## Section 4 : Non-EU regimes (selected)

### 4.1 United States

- Route the federal alcohol/tobacco, fuel/other excise and separate state tasks to current US product methods. Establish the actual administering authority (TTB and IRS are not interchangeable), operative law and return. Preserve proof-gallon/barrel, tobacco-unit, fuel and state-tax questions; no US rates or forms are certified here.

### 4.2 United Kingdom

- The UK retained EMCS; its EU link remains for Northern Ireland. Notice 197 covers warehouse receipt/removal and Notice 196 covers authorisation, not separate alcohol-production/tobacco notices. Use the actual country method for alcohol strength bands and conditional draught relief. Alcohol Duty switched to pure-alcohol litres on 1 August 2023, not February. [HMRC historic duty basis](https://www.gov.uk/government/statistics/alcohol-bulletin/alcohol-bulletin-historic-duty-rates).
- Notice 197 includes EMCS exceptions, including lawful fallback/simplified procedures and specified domestic energy movements using W8 or its commercial equivalent. A system outage does not justify an undocumented movement or necessarily require refusing a lawful fallback. [HMRC Notice 197, sections 1 to 3](https://www.gov.uk/guidance/receive-goods-into-and-remove-goods-from-an-excise-warehouse-excise-notice-197).

### 4.3 Other

- Preserve separate country investigations for Australian petroleum/alcohol/tobacco; Canadian federal/provincial products and cannabis; Japanese alcohol/tobacco/oil; Indian central/state excise and GST interaction; and Brazilian IPI and transition. Do not treat a Cannabis Act reference as the charging authority for Canadian cannabis excise or infer current Indian/Brazilian scope from a historical summary. Obtain the actual current country source, authority and return before giving a result.

## Section 5 : Non-traditional excise

### 5.1 Sugar-sweetened beverages

**Sugar-sweetened beverages**

| Country | Status |
| --- | --- |
| UK | For liable drinks, lower band is at least 5 but less than 8 g sugar/100 ml; higher is at least 8. From 1 April 2026: GBP 2.08 and GBP 2.78 per 10 litres respectively. For January to March 2026: GBP 1.94 and GBP 2.59 per 10 litres. First apply the product/additional-sugar/exemption tests. [HMRC SDIL](https://www.gov.uk/guidance/check-if-your-drink-is-liable-for-the-soft-drinks-industry-levy) |
| Norway | Standalone sugar duty still exists; it is not the same as a tax on finished sugar-sweetened beverages. Check product and commercial-use exceptions instead of describing Sukkeravgift as abolished. [Skatteetaten sugar duty](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/excise-duties/about-the-excise-duties/sugar/) |
| Hungary, France, Spain (Catalonia), Mexico, Philippines, Ireland | Retain these country/subnational beverage-scope investigations; current enactment, rates, liable person and returns require their official country methods |

### 5.2 Plastic packaging tax

**Plastic packaging tax**

| Country | Status |
| --- | --- |
| UK | From 1 April 2026: GBP 228.82 per tonne; January to March 2026: GBP 223.69. Test finished-component, recycled-content and exemption rules; the ordinary recycled-content threshold is 30%. [HMRC PPT](https://www.gov.uk/green-taxes-and-reliefs/plastic-packaging-tax), [Finance Act 2026 s.104](https://www.legislation.gov.uk/ukpga/2026/11/section/104/2026-09-16) |
| Spain | EUR 0.45 per kg of non-recycled plastic within the taxable non-reusable-packaging scope, not all packaging weight. Establish certified recycled content and applicable exclusions. [AEAT base and rate](https://sede.agenciatributaria.gob.es/Sede/impuestos-especiales-medioambientales/impuesto-especial-sobre-envases-plastico-reutilizables/base-imponible-tipo-impositivo-cuota-tributaria.html) |
| Italy | Track actual plastic-tax commencement and any deferral from current Italian law; no assumed 2026 start is certified here |
| Germany | Manufacturer cost responsibility began in 2024; first payments in 2025 used 2024 data. This is a producer levy with its own product/registration rules, not a generic packaging excise. [UBA historical commencement](https://www.umweltbundesamt.de/en/press/pressinformation/manufacturers-of-single-use-plastic-products-must) |

### 5.3 EU Single-Use Plastic Directive

- **EU Single-Use Plastic Directive:** keep a separate product-ban/producer-responsibility compliance check from the tax computation. Obtain the actual national implementation of Directive (EU) 2019/904 and scope for the product; the German fund example above does not establish another country's charge or deadline.

## Section 6 : Reviewer brief

1. Product register
   - Tariff classification per product line
   - Duty rates (specific + ad valorem)
   - Exemptions claimed

2. Movements log
   - Inbound (production / import / receipt under suspension)
   - Outbound (release for consumption / dispatch under suspension)
   - In-warehouse stock movements
   - Losses (allowable vs disallowable)

3. Duty payable schedule
   - By product / period
   - By movement (EMCS-tracked)
   - Reduced-rate / exemption support

4. EMCS / equivalent compliance
   - Active eADs/eSADs where required and any documented lawful fallback
   - Accepted receipt/export and actual closed eAD/eSAD status
   - Discrepancies / irregularities

5. Bond / guarantee status
   - Movement guarantee
   - Warehouse guarantee
   - Deferment account

6. Reviewer questions : [T2]/[T3] items

## Self-check

1. [ ] Product correctly classified within the excise framework
2. [ ] Duty rate current and bracket / strength / volume correctly applied
3. [ ] Chargeable event identified (release for consumption / equivalent)
4. [ ] Duty-suspension status documented per movement
5. [ ] Actual EMCS / local eAD/eSAD or lawful fallback records aligned with physical movements
6. [ ] Exemption / reduced rate claims supported by evidence
7. [ ] Small producer reliefs verified against turnover / production limits
8. [ ] Stock reconciliation completed (opening + production + receipts − releases = closing)
9. [ ] Losses within allowable tolerance
10. [ ] Periodic return prepared with payment within deadline
11. [ ] Bond / guarantee value adequate for risk
12. [ ] Output flags every [T2]/[T3] item for reviewer judgement

## Stop and escalate

**Refusal catalogue**

| Refusal | Trigger |
| --- | --- |
| R-EXC-1 | Required production, warehouse or movement authorisation absent; do not demand warehousekeeper status from every trader or levy |
| R-EXC-2 | EMCS unavailable for a required movement and no lawful, documented fallback/simplified route established |
| R-EXC-3 | Suspected fraud / illicit movement |
| R-EXC-4 | Loss exceeds an evidenced applicable tolerance or lacks the actual irregularity/relief determination |
| R-EXC-5 | Applicable tobacco/alcohol traceability or fiscal-mark requirements not met; establish actual product/date scope, not a universal 2019 start |
| R-EXC-6 | Cross-border movement to country with restrictive measures |

- **R-EXC-1** : Required production, warehouse or movement authorisation absent; do not demand warehousekeeper status from every trader or levy
- **R-EXC-2** : EMCS unavailable for a required movement and no lawful, documented fallback/simplified route established
- **R-EXC-3** : Suspected fraud / illicit movement
- **R-EXC-4** : Loss exceeds an evidenced applicable tolerance or lacks the actual irregularity/relief determination
- **R-EXC-5** : Applicable tobacco/alcohol traceability or fiscal-mark requirements not met; establish actual product/date scope, not a universal 2019 start  _(Tobacco Products Directive 2014/40/EU)_
- **R-EXC-6** : Cross-border movement to country with restrictive measures

## Section 9 : Slot contract for country excise skills

[FRAMEWORK]
- Excise legislation citations
- Regulator name
- Filing portal

[PRODUCT TARIFF]
- Energy products rates
- Alcohol rates by category
- Tobacco rates by category
- Non-traditional excise (sugar, plastic, gambling) if applicable

[REDUCED RATES]
- Small producer reliefs (brewery, winery, distillery)
- Industrial use exemptions
- Renewable / biofuel reductions

[EMCS / EQUIVALENT]
- System name
- Authorised participant categories
- Movement guarantee

[RETURNS]
- Filing frequency
- Filing portal
- Payment terms

[CROSS-REFERENCES]
- Customs duty: `customs-duties-workflow-base` plus actual country procedure
- VAT on excise products (country VAT skill)
- CBAM: load the actual available CBAM method, test covered goods/date and separate obligations; this excise method does not supply CBAM rules

## Section 10 : Disclaimer

This workflow base produces working papers for review by licensed excise practitioners. Excise duty involves criminal as well as civil penalties for misstatement. Every output must be reviewed and signed off by a licensed practitioner before lodgement.

The most up-to-date, verified version of this workflow base is maintained at [openaccountants.com](https://openaccountants.com).


## Worked cases

**UK SDIL, April 2026 removal.** Assume product liability and no exemption are confirmed, with 1,000 litres at 6 g sugar/100 ml and 500 litres at exactly 8 g/100 ml. The second product is in the higher band. Apply the per-10-litre units: GBP 208 + GBP 139 = GBP 347. A January 2026 movement instead uses its own period's rates, not these April rates. [HMRC bands and dated rates](https://www.gov.uk/guidance/check-if-your-drink-is-liable-for-the-soft-drinks-industry-levy).

```oa-check
name: UK 2026 SDIL exact upper-band boundary and volume units
inputs:
  lower_litres: 1000
  higher_litres: 500
  lower_per_ten_litres: 2.08
  higher_per_ten_litres: 2.78
steps:
  - lower_levy: lower_litres / 10 * lower_per_ten_litres
  - higher_levy: higher_litres / 10 * higher_per_ten_litres
  - total: lower_levy + higher_levy
expected:
  lower_levy: 208
  higher_levy: 139
  total: 347
```

**Spain plastic mass.** Assume 2,000 kg is within taxable packaging scope, with 500 kg recycled content proved to the applicable standard. The tax base is 1,500 kg, not gross 2,000 kg. At EUR 0.45/kg, tax is EUR 675, subject to actual country exclusions/reliefs. Reconcile to prior-taxed components instead of taxing them again. [AEAT base/rate](https://sede.agenciatributaria.gob.es/Sede/impuestos-especiales-medioambientales/impuesto-especial-sobre-envases-plastico-reutilizables/base-imponible-tipo-impositivo-cuota-tributaria.html).

```oa-check
name: Spain plastic tax uses non-recycled mass
inputs:
  in_scope_kg: 2000
  certified_recycled_kg: 500
  rate_per_kg: 0.45
steps:
  - non_recycled_kg: in_scope_kg - certified_recycled_kg
  - tax: non_recycled_kg * rate_per_kg
expected:
  non_recycled_kg: 1500
  tax: 675
```

## Sources

| Source | Official URL | Read on |
|---|---|---|
| EC energy excise. Read for motor/heating/electricity minimum tables, uses and distinction between enacted framework and recast proposal | https://taxation-customs.ec.europa.eu/taxation/excise-duties/excise-duties-energy_en | 2026-11-14 |
| EC alcohol excise. Read for Plato/ABV minimum units, wine/intermediate/ethyl-alcohol minima and conditional reliefs | https://taxation-customs.ec.europa.eu/taxation/excise-duties/excise-duties-alcohol_en | 2026-11-14 |
| EC tobacco excise. Read for cigarette dual minima and euro exception, fine-cut OR test and other tobacco price bases | https://taxation-customs.ec.europa.eu/taxation/excise-duties/excise-duties-tobacco_en | 2026-11-14 |
| EC common excise provisions. Read for chargeability, suspended versus duty-paid movements, eAD/eSAD and participant roles; not every article of the linked directives | https://taxation-customs.ec.europa.eu/taxation/excise-duties/common-excise-duty-provisions_en | 2026-11-14 |
| HMRC goods movements. Read for UK authorisation, movement security, EMCS and pre-removal payment/accounting | https://www.gov.uk/guidance/receiving-storing-and-moving-excise-goods | 2026-11-14 |
| HMRC Notice 197, opening and sections 1 to 3. Read for scope, NI/EU system distinction, authorisation-notice cross-reference and exceptions/fallback; not the entire notice | https://www.gov.uk/guidance/receive-goods-into-and-remove-goods-from-an-excise-warehouse-excise-notice-197 | 2026-11-14 |
| HMRC historic alcohol bulletin. Read for actual August 2023 switch to pure-alcohol litre basis; no historic rate adopted as current | https://www.gov.uk/government/statistics/alcohol-bulletin/alcohol-bulletin-historic-duty-rates | 2026-11-14 |
| HMRC SDIL. Read for product liability, sugar boundary, April 2025/2026 rates and chargeable-event qualifications | https://www.gov.uk/guidance/check-if-your-drink-is-liable-for-the-soft-drinks-industry-levy | 2026-11-14 |
| HMRC PPT. Read for recycled-content threshold, charge and current rate; FA 2026 s.104 read for old/new amount and April commencement | https://www.gov.uk/green-taxes-and-reliefs/plastic-packaging-tax ; https://www.legislation.gov.uk/ukpga/2026/11/section/104/2026-09-16 | 2026-11-14 |
| AEAT plastic base/rate. Read for non-recycled mass, recycled certification and incremental previously-taxed components | https://sede.agenciatributaria.gob.es/Sede/impuestos-especiales-medioambientales/impuesto-especial-sobre-envases-plastico-reutilizables/base-imponible-tipo-impositivo-cuota-tributaria.html | 2026-11-14 |
| Skatteetaten sugar duty. Read for current standalone-sugar duty and commercial-product exclusions, disproving blanket abolition | https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/excise-duties/about-the-excise-duties/sugar/ | 2026-11-14 |
| UBA December 2024 notice. Read for 2024 responsibility/2025 arrears chronology only; not current 2026 fee tables/deadlines | https://www.umweltbundesamt.de/en/press/pressinformation/manufacturers-of-single-use-plastic-products-must | 2026-11-14 |

Not yet confirmed: each country's actual payable excise rates and special reductions, EU small-producer percentage ceilings and precise eligibility, tax treatment of losses/irregularities and complete EMCS receipt deadlines; 2026 tobacco/alcohol product-specific traceability dates; US, Australia, Canada, Japan, India and Brazil current charging legislation/rates/filing rules; the listed other beverage regimes; Italian plastic-tax commencement; current German fund rates and filing dates; national single-use-plastic implementation; other levy return/payment frequencies. These subjects remain in the intake and slot contract but are not certified by the bounded examples or EU minima. The original universal one-month payment rule, assumed 2026 Italian start, February 2023 UK reform, stale UK levy rates, automatic destination shortage charge and blanket warehouse requirement are not usable rules.
