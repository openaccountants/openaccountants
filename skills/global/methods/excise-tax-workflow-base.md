---
name: excise-tax-workflow-base
description: "Tier 1 workflow base for excise duty skills covering harmonised excise on energy products, alcohol, and tobacco (EU Directives 2003/96/EC, 92/83/EEC, 2011/64/EU) and non-harmonised excise (sugar, plastics, single-use plastic, gambling, environmental). Workflow architecture only — no country rate tables or product-specific guidance. MUST be loaded alongside a country excise content skill. Assumes a licensed excise warehouse keeper or authorised consignor / consignee operates under bond and EMCS (Excise Movement and Control System). Does NOT cover: customs duty (see customs-duties-workflow-base), VAT on excise products (see country VAT skills), excise on cannabis where legalised (specialist), or licensing process for excise warehouse."
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
category: foundation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# Excise Tax Workflow Base

## What this file is

Tier 1 workflow base for excise duty skills. Country content skills load on top.

## Section 1 — Scope and assumptions

Excise duty is a tax on the production or sale of specific goods, typically:
- Energy products (motor fuel, heating fuel, gas, coal, electricity)
- Alcoholic beverages
- Tobacco products
- Sugar-sweetened beverages (UK, Norway, Hungary, others)
- Plastic / single-use plastic packaging
- Gambling
- Vehicle registration / luxury vehicle (some countries)

This workflow base assumes:
- The taxpayer is a producer, importer, distributor, or retailer of excisable goods
- Excisable goods are stored under bond in authorised warehouses until release for consumption
- The country has implemented EMCS (Excise Movement and Control System) or equivalent (EU) — or the US bonded warehouse / Form 5000 series equivalent

## Section 2 — Lifecycle runbook

### Step 1 — Determine excisable status

- **Determine excisable status** — For each product: Is it listed in the country's excise legislation? What is the applicable rate / tariff classification? Are there reduced rates (e.g., red diesel, agricultural fuel)? Are there exemptions (e.g., scientific use, denatured alcohol)? ([T1])  _([T1])_

### Step 2 — Determine the chargeable event

- **Chargeable event = release for consumption** — Excise becomes due on the release for consumption — typically: Departure from a tax warehouse (other than under duty-suspension arrangement); Manufacture outside a tax warehouse; Importation outside a duty-suspension arrangement; Holding outside a duty-suspension arrangement; Irregularity during a duty-suspended movement (deemed release) ([T1])  _([T1])_

### Step 3 — Compute the duty

- **Duty computation methods** — Depending on product type: Specific duty — per litre, per kg, per pack, per stick; Ad valorem — % of retail price (typical for tobacco); Combined — both (e.g., EU tobacco minimum specific + ad valorem). For alcohol: typically per hectolitre of pure alcohol (ethanol) for spirits; per hectolitre and degree of strength for beer/wine/intermediate products. Reduced rates for small breweries, small wine producers, low-alcohol products. ([T1])  _([T1])_

### Step 4 — Apply duty-suspension and movements

- **EU EMCS duty-suspension movement rules** — EU EMCS (Excise Movement and Control System): Electronic Administrative Document (eAD) accompanies suspended movements; Authorised Warehouse Keeper / Registered Consignor / Registered Consignee status required; Closure of movement upon arrival at destination triggers chargeable event in destination MS (if released) or duty suspension continues; Movement guarantee covers the duty during transit ([T1])  _([T1])_

### Step 5 — Pay the duty

- **Periodic excise return and payment** — Periodic excise return — typically monthly. Payment generally within 1 month of the chargeable event. Bond / guarantee covers deferred payment. ([T1])  _([T1])_

### Step 6 — Track exemptions and reliefs

- **Common exemptions** — Common exemptions: Diplomatic / consular use; Visiting forces (NATO SOFA); Research / scientific use; Denatured alcohol; Domestic production for personal use (limited); Renewable energy / biofuels (variable); Industrial use (e.g., energy products for non-fuel use) ([T1])  _([T1])_

## Section 3 — EU harmonised excise framework

### 3.1 Energy products (Directive 2003/96/EC)

- **Unleaded petrol minimum rate** — EUR 359 per 1,000L EUR per 1,000L  _(Directive 2003/96/EC)_
- **Diesel (commercial use) minimum rate** — EUR 330 per 1,000L EUR per 1,000L  _(Directive 2003/96/EC)_
- **Heating gas oil minimum rate** — EUR 21 per 1,000L EUR per 1,000L  _(Directive 2003/96/EC)_
- **Heavy fuel oil minimum rate** — EUR 15 per 1,000kg EUR per 1,000kg  _(Directive 2003/96/EC)_
- **LPG (heating) minimum rate** — EUR 0 per 1,000kg EUR per 1,000kg  _(Directive 2003/96/EC)_
- **Natural gas (heating) minimum rate** — EUR 0.15/0.30 per GJ (commercial / non-commercial) EUR per GJ  _(Directive 2003/96/EC)_
- **Coal and coke minimum rate** — EUR 0.15/0.30 per GJ EUR per GJ  _(Directive 2003/96/EC)_
- **Electricity minimum rate** — EUR 0.50/1.00 per MWh EUR per MWh  _(Directive 2003/96/EC)_
- **Member state discretion above minima** — Member States set rates above these minima; some derogations / reduced rates approved by Council.  _(Directive 2003/96/EC)_

### 3.2 Alcohol (Directives 92/83/EEC and 92/84/EEC)

- **Beer minimum rate** — EUR 1.87 per hectolitre / degree Plato OR EUR 0.748 per hectolitre / degree of alcohol (chosen MS basis) EUR per hectolitre/degree  _(Directives 92/83/EEC and 92/84/EEC)_
- **Wine (still and sparkling) minimum rate** — EUR 0 (minimum) — many MS set zero EUR  _(Directives 92/83/EEC and 92/84/EEC)_
- **Intermediate products (sherry, port, fortified) minimum rate** — EUR 45 per hectolitre EUR per hectolitre  _(Directives 92/83/EEC and 92/84/EEC)_
- **Spirits minimum rate** — EUR 550 per hectolitre of pure alcohol EUR per hectolitre pure alcohol  _(Directives 92/83/EEC and 92/84/EEC)_
- **Small independent brewery reduced rates** — Reduced rates available for small independent breweries (typically up to 50% reduction).  _(Directives 92/83/EEC and 92/84/EEC)_

### 3.3 Tobacco (Directive 2011/64/EU)

- **Cigarettes minimum excise duty** — at least 60% of weighted average retail selling price (WARSP); minimum EUR 90 per 1,000 cigarettes (or 115% of weighted average retail selling price) % WARSP / EUR per 1,000 cigarettes  _(Directive 2011/64/EU)_
- **Fine-cut tobacco minimum excise duty** — 48% of weighted average retail selling price; minimum EUR 60 per kg % WARSP / EUR per kg  _(Directive 2011/64/EU)_
- **Cigars / cigarillos minimum excise duty** — 5% of weighted average retail selling price OR EUR 12 per 1,000 / EUR 12 per kg % WARSP / EUR  _(Directive 2011/64/EU)_
- **Other smoking tobacco minimum excise duty** — 20% of weighted average retail selling price OR EUR 22 per kg % WARSP / EUR per kg  _(Directive 2011/64/EU)_
- **Combination of specific and ad valorem** — Combination of specific and ad valorem; minimum total varies.  _(Directive 2011/64/EU)_

### 3.4 EMCS data flow

**EMCS data flow**

| Stage | Document |
| --- | --- |
| Dispatch | e-AD (electronic Administrative Document) with Administrative Reference Code (ARC) |
| In transit | ARC referenced on transport documents |
| Receipt at destination | Report of Receipt (RoR) by consignee |
| Closure | EMCS auto-closes upon successful RoR |
| Discrepancy / shortage | Excise becomes chargeable in destination MS |

## Section 4 — Non-EU regimes (selected)

### 4.1 United States

- Excise tax under IRC Subtitle E (Alcohol, Tobacco, and Other Excise Taxes)
- TTB (Alcohol and Tobacco Tax and Trade Bureau) administers
- Federal alcohol per-proof-gallon and per-barrel rates
- Federal tobacco per-stick rates
- Federal fuel excise (Highway Trust Fund)
- Plus state excise (variable by state)

### 4.2 United Kingdom

- Post-Brexit: outside EU EMCS but mirrors substantive rules
- Excise Notice 197 (alcohol production), 196 (tobacco)
- New Spirit Drink, Wine and Beer Duty rates reformed February 2023 (alcohol-by-volume based; draught relief)
- ETDS (Excise Movement and Control System UK)

### 4.3 Other

- Australia — excise on petroleum, alcohol, tobacco under Excise Act 1901
- Canada — federal + provincial excise; cannabis excise under Cannabis Act
- Japan — alcohol, tobacco, oil under Alcohol Tax Law et al
- India — central excise replaced largely by GST 2017 except petroleum and tobacco
- Brazil — IPI (Federal Industrialised Products Tax) applies functions analogous to excise

## Section 5 — Non-traditional excise

### 5.1 Sugar-sweetened beverages

**Sugar-sweetened beverages**

| Country | Status |
| --- | --- |
| UK | Soft Drinks Industry Levy from April 2018 — 18p/L (5g-8g sugar/100mL) or 24p/L (>8g sugar/100mL) |
| Norway | Sukkeravgift; abolished but discussed for reintroduction |
| Hungary, France, Spain (Catalonia), Mexico, Philippines, Ireland | Various rates / structures |

### 5.2 Plastic packaging tax

**Plastic packaging tax**

| Country | Status |
| --- | --- |
| UK | Plastic Packaging Tax from April 2022 — GBP 217.85 per tonne (2024 rate) of plastic packaging with < 30% recycled plastic |
| Spain | Impuesto Especial sobre los Envases de Plástico no Reutilizables from January 2023 — EUR 0.45 per kg non-reusable plastic |
| Italy | Plastic tax deferred multiple times; expected 2026 |
| Germany | One-Way Plastic Fund Act effective 2025 |

### 5.3 EU Single-Use Plastic Directive

- **EU Single-Use Plastic Directive** — Directive (EU) 2019/904 — bans certain single-use plastic products and mandates extended producer responsibility for others. National implementations vary.  _(Directive (EU) 2019/904)_

## Section 6 — Reviewer brief

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
   - Active eADs
   - Closed eADs
   - Discrepancies / irregularities

5. Bond / guarantee status
   - Movement guarantee
   - Warehouse guarantee
   - Deferment account

6. Reviewer questions — [T2]/[T3] items

## Section 7 — Self-checks (12)

1. [ ] Product correctly classified within the excise framework
2. [ ] Duty rate current and bracket / strength / volume correctly applied
3. [ ] Chargeable event identified (release for consumption / equivalent)
4. [ ] Duty-suspension status documented per movement
5. [ ] EMCS / equivalent eADs aligned with physical movements
6. [ ] Exemption / reduced rate claims supported by evidence
7. [ ] Small producer reliefs verified against turnover / production limits
8. [ ] Stock reconciliation completed (opening + production + receipts − releases = closing)
9. [ ] Losses within allowable tolerance
10. [ ] Periodic return prepared with payment within deadline
11. [ ] Bond / guarantee value adequate for risk
12. [ ] Output flags every [T2]/[T3] item for reviewer judgement

## Section 8 — Refusal catalogue

**Refusal catalogue**

| Refusal | Trigger |
| --- | --- |
| R-EXC-1 | Production / movement of excisable goods without authorised warehouse keeper status |
| R-EXC-2 | EMCS unavailability for required movement |
| R-EXC-3 | Suspected fraud / illicit movement |
| R-EXC-4 | Loss exceeding allowable tolerance |
| R-EXC-5 | Tobacco / alcohol traceability requirements not met (Tobacco Products Directive 2014/40/EU traceability since 2019) |
| R-EXC-6 | Cross-border movement to country with restrictive measures |

- **R-EXC-1** — Production / movement of excisable goods without authorised warehouse keeper status
- **R-EXC-2** — EMCS unavailability for required movement
- **R-EXC-3** — Suspected fraud / illicit movement
- **R-EXC-4** — Loss exceeding allowable tolerance
- **R-EXC-5** — Tobacco / alcohol traceability requirements not met (Tobacco Products Directive 2014/40/EU traceability since 2019)  _(Tobacco Products Directive 2014/40/EU)_
- **R-EXC-6** — Cross-border movement to country with restrictive measures

## Section 9 — Slot contract for country excise skills

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
- Customs duty workflow (this skill)
- VAT on excise products (country VAT skill)
- CBAM (EU energy product imports — this skill)

## Section 10 — Disclaimer

This workflow base produces working papers for review by licensed excise practitioners. Excise duty involves criminal as well as civil penalties for misstatement. Every output must be reviewed and signed off by a licensed practitioner before lodgement.

The most up-to-date, verified version of this workflow base is maintained at [openaccountants.com](https://openaccountants.com).
