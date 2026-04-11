---
name: croatia-vat-return
description: Use this skill whenever asked to prepare, review, or create a Croatian VAT return (PDV form / PDV-S / Obrazac PDV) for any client. Trigger on phrases like "prepare VAT return", "do the PDV", "fill in PDV", "create the return", "Croatian VAT", or any request involving Croatia VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Croatian VAT classification rules, box mappings, deductibility rules, reverse charge treatment, fiscalization requirements, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any VAT-related work for Croatia.
---

# Croatia VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Croatia |
| Jurisdiction Code | HR |
| Primary Legislation | Zakon o porezu na dodanu vrijednost (VAT Act, OG 73/13, as amended through OG 33/23 and subsequent) |
| Supporting Legislation | Pravilnik o PDV-u (VAT Regulation, OG 79/13 as amended); Zakon o fiskalizaciji (Fiscalization Act, OG 133/12); EU VAT Directive 2006/112/EC |
| Tax Authority | Porezna uprava (Tax Administration), Ministry of Finance |
| Filing Portal | https://e-porezna.porezna-uprava.hr (ePorezna) |
| Contributor | Auto-generated draft -- requires validation |
| Validated By | Deep research verification, April 2026 |
| Validation Date | 2026-04-10 |
| Skill Version | 1.0 |
| Status | validated |
| Confidence Coverage | Tier 1: box assignment, reverse charge, deductibility blocks, derived calculations. Tier 2: partial exemption pro-rata, sector-specific deductibility, real estate options, fiscalization compliance. Tier 3: complex group structures, non-standard supplies, cross-border triangulation. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified accountant.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and OIB (Personal Identification Number)** [T1] -- 11-digit number, used as VAT ID with HR prefix for VIES
2. **VAT registration status** [T1] -- Registered (obavezni = mandatory / dobrovoljni = voluntary) or exempt (small business under EUR 60,000 threshold)
3. **Filing frequency** [T1] -- Monthly (default); Quarterly (turnover < EUR 110,000 prior year, no intra-EU acquisitions); from 2026 filing deadline extended to last day of following month
4. **Industry/sector** [T2] -- impacts deductibility (hospitality, tourism, construction, agriculture)
5. **Does the business make exempt supplies?** [T2] -- If yes, partial attribution required (pro-rata); reviewer must confirm
6. **Does the business trade goods for resale?** [T1] -- impacts classification
7. **Excess credit brought forward** [T1] -- from prior period
8. **Fiscalization compliance** [T1] -- mandatory for all invoices (domestic)
9. **Annual turnover** [T1] -- determines registration obligation

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output PDV / obracunani PDV) or Purchase (input PDV / pretporez)
- Salaries, social contributions (HZZO, HZMO), income tax, loan repayments, dividends, bank charges = OUT OF SCOPE
- **Legislation:** VAT Act Art. 4 (taxable transactions), Art. 7 (supply of goods), Art. 8 (supply of services)

### 1b. Determine Counterparty Location [T1]
- Croatia (domestic): supplier/customer country is HR
- EU: AT, BE, BG, CY, CZ, DK, EE, FI, FR, DE, GR, HU, IE, IT, LV, LT, LU, MT, NL, PL, PT, RO, SK, SI, ES, SE
- Non-EU: everything else (US, UK, AU, CH, etc.)
- **Note:** UK is Non-EU post-Brexit. Bosnia-Herzegovina, Serbia, Montenegro are Non-EU.

### 1c. Determine VAT Rate [T1]

| Rate | Category | Legislation |
|------|----------|-------------|
| 25% | Standard rate -- most goods and services | VAT Act Art. 38(1) |
| 13% | Reduced -- accommodation services (hotels, guesthouses, camping), restaurant and catering services (food and non-alcoholic beverages), newspapers (print), water supply, certain pharmaceuticals, entrance to cultural/sporting events, funeral services, firewood | VAT Act Art. 38(2), Annex II |
| 5% | Super-reduced -- basic foodstuffs (bread, milk, eggs, cooking oil, baby food), books (printed and electronic), medical equipment/prosthetics, scientific journals, menstrual hygiene products | VAT Act Art. 38(3), Annex I |
| 0% | Zero-rated -- intra-EU supplies of goods (Art. 41), exports outside EU (Art. 45) | VAT Act Art. 41-46 |
| Exempt with credit | International transport, supplies related to international trade | VAT Act Art. 42-44 |
| Exempt without credit | Financial services (Art. 40(1)(a-g)), insurance (Art. 40(1)(h)), healthcare (Art. 39(1)(a)), education (Art. 39(1)(b)), postal services, gambling, residential rental (> 2 years, or permanent housing), transfer of going concern | VAT Act Art. 39-40 |

### 1d. Determine Expense Category [T1]
- Capital goods: tangible assets used for business, subject to adjustment if change in deductible proportion
- Immovable property: 10-year adjustment period (VAT Act Art. 65)
- Movable capital goods (> EUR 6,636): 5-year adjustment period
- Resale: goods bought to resell
- Overhead/services: everything else
- **Legislation:** VAT Act Art. 64-65 (adjustment of deduction for capital goods)

---

## Step 2: VAT Return Form Structure (Obrazac PDV / PDV-S) [T1]

**Legislation:** VAT Act Art. 85-86; VAT Regulation Art. 174-175.

### Section I -- Transactions Not Subject to VAT and Exempt Transactions

| Row | Description | Notes |
|-----|-------------|-------|
| I.1 | Supplies of goods and services outside Croatia (place of supply not HR) | Intermediary services, B2B services to EU |
| I.2 | Supplies exempt without right of deduction | Financial, insurance, healthcare, education |
| I.3 | Supplies exempt with right of deduction | Intra-EU supplies, exports, international transport |
| I.4 | Intra-Community supply of goods | EU B2B with valid VIES number |
| I.5 | Exports of goods outside EU | With customs documentation |

### Section II -- Taxable Transactions (Output PDV)

| Row | Description | Rate | Tax Column |
|-----|-------------|------|------------|
| II.1 | Domestic supplies at 5% -- taxable base | 5% | PDV at 5% |
| II.2 | Domestic supplies at 13% -- taxable base | 13% | PDV at 13% |
| II.3 | Domestic supplies at 25% -- taxable base | 25% | PDV at 25% |
| II.4 | Intra-Community acquisitions of goods -- taxable base | Self-assessed | PDV at applicable rate |
| II.5 | Services received from EU (reverse charge) -- taxable base | Self-assessed | PDV at applicable rate |
| II.6 | Services received from non-EU (reverse charge) -- taxable base | Self-assessed | PDV at applicable rate |
| II.7 | Domestic reverse charge supplies received -- taxable base | Self-assessed | PDV at applicable rate |
| II.8 | Import of goods -- taxable base | Customs | PDV at applicable rate |
| II.9 | Self-supply / deemed supply | Applicable | At applicable rate |
| II.10 | Total output PDV | -- | Sum of all output PDV |

### Section III -- Input VAT (Pretporez -- Deductible)

| Row | Description | Notes |
|-----|-------------|-------|
| III.1 | Input PDV on domestic purchases at 5% | Domestic reduced |
| III.2 | Input PDV on domestic purchases at 13% | Domestic intermediate |
| III.3 | Input PDV on domestic purchases at 25% | Domestic standard |
| III.4 | Input PDV on intra-Community acquisitions | Mirrors II.4 output |
| III.5 | Input PDV on services received from EU | Mirrors II.5 output |
| III.6 | Input PDV on services received from non-EU | Mirrors II.6 output |
| III.7 | Input PDV on domestic reverse charge | Mirrors II.7 output |
| III.8 | Input PDV on imports | From customs declaration |
| III.9 | Adjustments to input PDV | Corrections, pro-rata adjustments |
| III.10 | Total input PDV (deductible) | Sum |

### Section IV -- VAT Liability

| Row | Description | Notes |
|-----|-------------|-------|
| IV.1 | PDV liability (II.10 minus III.10) -- if positive | TO PAY |
| IV.2 | PDV excess credit -- if negative | TO REFUND or carry forward |
| IV.3 | Deductible proportion (%) | For partial exemption |

---

## Step 3: Transaction Classification Matrix [T1]

### Purchases -- Domestic (Croatian Supplier)

| VAT Rate | Category | Input Row | Notes |
|----------|----------|-----------|-------|
| 25% | Overhead/services | III.3 | Standard domestic |
| 13% | Overhead/services | III.2 | Accommodation, restaurant, water |
| 5% | Overhead/services | III.1 | Food, books, medical equipment |
| 0% | Any | -- | No PDV to claim |
| Any | Capital goods | III.3/III.2/III.1 | Track separately for 5/10-year adjustment |
| Any | Vehicle (mixed use 50%) | III.3 at 50% | Art. 61(2) restriction |
| Any | Representation (50%) | III.3/III.2 at 50% | Art. 61(2) restriction |
| Any | Blocked category (0%) | -- | No deduction |

### Purchases -- EU Supplier (Reverse Charge)

| Type | Output Row | Input Row | Notes |
|------|-----------|-----------|-------|
| Physical goods | II.4 | III.4 | Intra-EU acquisition |
| Services (B2B) | II.5 | III.5 | EU service RC |
| Out-of-scope (wages etc.) | -- | -- | NEVER reverse charge |
| Local consumption (hotel, restaurant abroad) | -- | -- | Foreign VAT at source |

### Purchases -- Non-EU Supplier

| Type | Output Row | Input Row | Notes |
|------|-----------|-----------|-------|
| Services (B2B) | II.6 | III.6 | Non-EU service import |
| Physical goods (customs) | II.8 | III.8 | Import via customs |
| Out-of-scope | -- | -- | NEVER reverse charge |

### Sales -- Domestic

| Rate | Row | Notes |
|------|-----|-------|
| 25% | II.3 | Standard-rated supply |
| 13% | II.2 | Accommodation, restaurant, water |
| 5% | II.1 | Food, books, medical |
| Exempt with credit | I.3 | International transport |
| Exempt without credit | I.2 | Financial, insurance, healthcare |

### Sales -- EU / Non-EU

| Location | Type | Row | Notes |
|----------|------|-----|-------|
| EU B2B goods | Intra-EU supply | I.4 | Zero-rated, report on EC Sales List |
| EU B2B services | Place of supply in customer MS | I.1 | B2B services to EU |
| Non-EU | Export | I.5 | Zero-rated, customs docs |
| Domestic RC supply made | Seller side | Row 25 equivalent | No PDV charged by seller |

---

## Step 4: Reverse Charge Mechanics [T1]

**Legislation:** VAT Act Art. 75-79 (reverse charge); Art. 17 (place of supply for services).

### Intra-EU Acquisitions of Goods (Art. 9)
1. Report net amount in II.4 (taxable base)
2. Self-assess output PDV at applicable Croatian rate (25%, 13%, or 5%)
3. Claim input PDV in III.4
4. Net effect: zero for fully taxable businesses
5. Report on ZP (Zbirna prijava -- EC Sales List)

### EU Services Received -- B2B (Art. 17(1))
1. Report in II.5 (taxable base)
2. Self-assess output PDV at applicable rate
3. Claim in III.5
4. Net effect: zero

### Non-EU Services Received
1. Report in II.6 (taxable base)
2. Self-assess output PDV at applicable rate
3. Claim in III.6
4. Net effect: zero

### Domestic Reverse Charge [T1]
**Legislation:** VAT Act Art. 75(3).

| Supply Type | Legislation | Notes |
|-------------|-------------|-------|
| Construction services (building, renovation, maintenance) | Art. 75(3)(a) | All construction, both parties must be PDV registered |
| Supply of waste and scrap materials | Art. 75(3)(b) | Metals, paper, glass, plastic |
| Supply of immovable property where seller opts to tax | Art. 75(3)(c) | Option to tax after exempt period |
| CO2 emission allowances | Art. 75(3)(d) | Greenhouse gas permits |
| Supply of gold material | Art. 75(3)(e) | Raw gold, semi-finished |

Domestic reverse charge procedure:
1. Report in II.7 (taxable base)
2. Self-assess output PDV at applicable rate
3. Claim in III.7
4. Net effect: zero

### Exceptions to Reverse Charge [T1]
- Out-of-scope categories (wages, bank charges, dividends): NEVER reverse charge
- Local consumption abroad (hotel, restaurant, taxi, conference): NOT reverse charge; foreign VAT at source
- EU supplier charged their local VAT > 0%: NOT reverse charge; foreign VAT is part of expense
- Construction services where one party is not PDV-registered: normal VAT applies

---

## Step 5: Deductibility Check

### Blocked / Restricted Categories [T1]
**Legislation:** VAT Act Art. 61 (restrictions on input tax deduction).

| Category | VAT Recovery | Legislation | Notes |
|----------|-------------|-------------|-------|
| Passenger vehicles (mixed business/private) | 50% | Art. 61(2)(a) | Unless exclusively business or benefit-in-kind calculated |
| Passenger vehicles (no BIK calculated) | 0% | Art. 61(2)(a) | If no BIK, no deduction |
| Passenger vehicles (exclusively business) | 100% | Art. 61(2)(a) exception | Taxi, rental, driving school, delivery (must prove) |
| Fuel for 50%-restricted vehicles | 50% | Art. 61(2)(a) | Follows vehicle rule |
| Maintenance/repairs for restricted vehicles | 50% | Art. 61(2)(a) | Follows vehicle rule |
| Representation/entertainment expenses | 50% | Art. 61(2)(b) | Client hospitality, gifts, events |
| Yachts and pleasure craft | 0% | Art. 61(1)(b) | Unless rental/charter business |
| Aircraft | 0% | Art. 61(1)(c) | Unless transport business |
| Personal use items | 0% | Art. 61(1)(a) | No deduction |
| Supplies for exempt-without-credit activities | 0% | Art. 58(1) | Financial, insurance, education inputs |

### Vehicle Rules [T1]
**Legislation:** VAT Act Art. 61(2)(a).

| Scenario | PDV Deduction | Evidence Required |
|----------|--------------|-------------------|
| Passenger car, mixed use, BIK calculated | 50% | BIK in salary records |
| Passenger car, mixed use, no BIK | 0% | No deduction at all |
| Passenger car, exclusively business | 100% | Trip sheets, GPS, contracts [T2] |
| Taxi / car rental / driving school vehicle | 100% | Qualifying business activity |
| Delivery / courier vehicle | 100% | Must be core business activity |
| Van / truck (N1+ category) | 100% | If for business purposes |
| Fuel for 50% vehicle | 50% | Follows vehicle classification |
| Fuel for 100% vehicle | 100% | Follows vehicle classification |

### Registration-Based Recovery [T1]

| Registration Type | Input VAT Recovery | Legislation |
|-------------------|-------------------|-------------|
| Registered (mandatory/voluntary) | Recovery subject to rules above | Art. 57-65 |
| Small business (under EUR 60,000) | NO recovery | Art. 90(1) |
| Non-established without HR registration | Must register or use refund procedure | Art. 73 |

### Partial Exemption [T2]
**Legislation:** VAT Act Art. 62.

If business makes both taxable and exempt supplies:

`Recovery % = (Taxable Supplies / Total Supplies) * 100`

| Rule | Detail | Legislation |
|------|--------|-------------|
| Rounding | Round to nearest whole percent | Art. 62(3) |
| Provisional | Use prior year proportion during current year | Art. 62(4) |
| Annual adjustment | True-up at year-end on annual return | Art. 62(5) |
| Excluded | Incidental financial/property transactions | Art. 62(2) |

**Flag for reviewer: pro-rata calculation must be confirmed by qualified accountant before applying. Annual adjustment required.**

---

## Step 6: Fiscalization (e-Invoicing / Fiskalizacija) [T1]

**Legislation:** Zakon o fiskalizaciji u prometu gotovinom (Fiscalization Act, OG 133/12, as amended).

| Feature | Detail |
|---------|--------|
| Scope | All invoices (B2B and B2C) must be fiscalized through Tax Administration system |
| B2B e-invoicing | Mandatory from 1 January 2026 (structured electronic invoicing) |
| Real-time reporting | Cash register receipts must be reported in real time via internet connection |
| Unique Invoice Number (JIR) | Assigned by Tax Administration for each invoice |
| QR code | Required on all receipts from 2023 |
| Penalty for non-fiscalization | EUR 266 - EUR 66,361 |

---

## Step 7: Key Thresholds

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Small business exemption | EUR 60,000 annual turnover (from 2025) | VAT Act Art. 90(1) |
| EU SME scheme (from 2025) | EUR 85,000 domestic + EUR 100,000 EU-wide | EU Directive 2020/285 |
| EU distance selling threshold | EUR 10,000/calendar year | EU Directive 2017/2455 |
| Intrastat arrivals | EUR 400,000 | CBS regulation |
| Intrastat dispatches | EUR 250,000 | CBS regulation |
| Capital goods -- movable | 5-year adjustment | VAT Act Art. 64 |
| Capital goods -- immovable | 10-year adjustment | VAT Act Art. 65 |
| Filing frequency | Monthly (default); quarterly if turnover < EUR 110,000 and no intra-EU acquisitions | VAT Act Art. 85 |
| Fiscalization (B2B e-invoicing) | Mandatory from 1 January 2026 | Fiscalization Act |

---

## Step 8: VAT Registration [T1]

| Feature | Detail | Legislation |
|---------|--------|-------------|
| VAT number format | HR + OIB (11 digits) | VAT Act Art. 77 |
| Mandatory registration | Turnover > EUR 60,000 in calendar year | VAT Act Art. 76 |
| Registration deadline | Before exceeding threshold | VAT Act Art. 76(1) |
| Voluntary registration | May register at any time | VAT Act Art. 77(2) |
| Group registration | Not available in Croatia | -- |
| Deregistration | If turnover stays below threshold | VAT Act Art. 78 |
| Fiscal representative | Required for non-EU businesses | VAT Act Art. 79 |
| Croatia joined EU | 1 July 2013 | Treaty of Accession |
| Croatia adopted EUR | 1 January 2023 | Council Decision 2022/1211 |

---

## Step 9: Filing Deadlines and Penalties

### Filing Deadlines [T1]

| Filing | Period | Deadline | Legislation |
|--------|--------|----------|-------------|
| PDV return (until end 2025) | Monthly | 20th of month following tax period | VAT Act Art. 85(5) |
| PDV return (from 2026) | Monthly | Last day of month following tax period | VAT Act Art. 85(5) (amended) |
| EC Sales List (ZP) | Monthly | Same as VAT return deadline | VAT Act Art. 85(6) |
| Annual PDV return | Annual | 28 February of following year | VAT Act Art. 85(7) |
| Intrastat | Monthly | 15th of following month | CBS regulation |
| PDV payment | Same as return | Same as filing deadline | General Tax Act Art. 61 |

### Penalties [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing of PDV return | EUR 260 - EUR 6,600 (first offense); EUR 660 - EUR 13,300 (repeat) | General Tax Act Art. 208(1) |
| Late payment of PDV | Interest at 5.89% p.a. (reference rate + 5%) | General Tax Act Art. 115 |
| Tax shortfall (additional assessment) | Up to 20% of additional tax | General Tax Act Art. 210 |
| Failure to register for PDV | EUR 2,600 - EUR 66,000 + back-assessment | General Tax Act Art. 208 |
| Fiscalization non-compliance | EUR 266 - EUR 66,361 | Fiscalization Act Art. 34 |
| EC Sales List late/missing | EUR 260 - EUR 13,300 | General Tax Act Art. 208 |
| Failure to issue invoice | EUR 660 - EUR 33,180 per invoice | General Tax Act Art. 209 |

---

## Step 10: Derived Box Calculations [T1]

```
II.10 = PDV on II.1 + PDV on II.2 + PDV on II.3 + PDV on II.4 + PDV on II.5 + PDV on II.6 + PDV on II.7 + PDV on II.8 + PDV on II.9
III.10 = III.1 + III.2 + III.3 + III.4 + III.5 + III.6 + III.7 + III.8 + III.9

IF II.10 > III.10 THEN
  IV.1 = II.10 - III.10  -- Tax Payable
  IV.2 = 0
ELSE
  IV.1 = 0
  IV.2 = III.10 - II.10  -- Excess Credit (refund or carry forward)
END
```

---

## Step 11: Edge Case Registry

### EC1 -- EU hotel / restaurant / taxi booked abroad [T1]
**Situation:** Croatian PDV-registered client pays for a hotel in Germany via credit card. Invoice shows German 7% VAT.
**Resolution:** NOT reverse charge. Foreign VAT was charged and paid at source. No PDV boxes. German VAT is irrecoverable cost.
**Legislation:** VAT Act Art. 19 -- place of supply for accommodation is where property is located.

### EC2 -- SaaS subscription from non-EU provider (Google, AWS) [T1]
**Situation:** Monthly charge from a US company, no VAT shown on invoice.
**Resolution:** Reverse charge. II.6 (net base) / self-assessed output PDV at 25%. III.6 (input PDV at 25%). Net effect zero.
**Legislation:** VAT Act Art. 17(1) -- place of supply for B2B services is customer's establishment.

### EC3 -- Construction services (domestic reverse charge) [T1]
**Situation:** Croatian construction company provides building services to another Croatian PDV-registered business. EUR 50,000.
**Resolution:** Domestic reverse charge applies. Supplier invoices without PDV. Recipient: II.7 (base EUR 50K) / self-assessed output PDV EUR 12,500 at 25%. III.7 = EUR 12,500. Net zero.
**Legislation:** VAT Act Art. 75(3)(a).

### EC4 -- Passenger vehicle purchase, mixed use (50%) [T1]
**Situation:** Client purchases a car used for business and private. BIK is calculated for employee.
**Resolution:** Input PDV deductible at 50% only (Art. 61(2)(a)).
**Legislation:** VAT Act Art. 61(2)(a).

### EC5 -- Passenger vehicle, no BIK calculated (0%) [T1]
**Situation:** Company car used partly private, but no benefit-in-kind is reported on payroll.
**Resolution:** Input PDV is NOT deductible at all (0%). Must calculate BIK to claim 50%.
**Legislation:** VAT Act Art. 61(2)(a) -- no BIK means no deduction.

### EC6 -- Representation dinner with clients (50%) [T1]
**Situation:** Client takes business partners to dinner. EUR 500 gross, PDV EUR 100 (25%).
**Resolution:** Input PDV deductible at 50% only. III.3 += EUR 50. Other EUR 50 is non-deductible.
**Legislation:** VAT Act Art. 61(2)(b).

### EC7 -- Export sale outside EU [T1]
**Situation:** Client sells goods to a US customer. EUR 10,000.
**Resolution:** Zero-rated supply. Report in I.5 (exports). No output PDV. Input PDV on related costs is fully recoverable.
**Legislation:** VAT Act Art. 45.

### EC8 -- Credit notes [T1]
**Situation:** Client receives a credit note from a supplier.
**Resolution:** Reverse the original entry. Reduce the applicable input PDV row. Net figures reported.
**Legislation:** VAT Act Art. 33(7) (correction of tax base).

### EC9 -- Intra-Community acquisition of goods [T1]
**Situation:** Client purchases goods from Italian supplier at 0% with valid VIES numbers.
**Resolution:** Reverse charge. II.4 (base + self-assessed output PDV at 25%). III.4 (input PDV at 25%). Net zero. Report on EC Sales List (ZP).
**Legislation:** VAT Act Art. 9.

### EC10 -- Fiscalization non-compliance (from 2026) [T2]
**Situation:** B2B domestic invoice not issued as structured e-invoice from 1 January 2026.
**Resolution:** Flag for reviewer: ensure client's invoicing system is compliant with new fiscalization requirements. Penalties: EUR 266 - EUR 66,361. Non-compliant invoices may face deduction issues.
**Legislation:** Fiscalization Act Art. 34.

### EC11 -- Yacht purchase (blocked) [T1]
**Situation:** Company buys a pleasure yacht for EUR 200,000 + PDV EUR 50,000.
**Resolution:** Input PDV BLOCKED (Art. 61(1)(b)). Full EUR 250,000 is cost. Exception only for charter/rental as business activity.
**Legislation:** VAT Act Art. 61(1)(b).

### EC12 -- Accommodation at 13% (business trip) [T1]
**Situation:** Business trip, hotel in Croatia. EUR 200 + EUR 26 PDV (13%). Not client entertainment.
**Resolution:** III.2 += EUR 26. Fully deductible as business overhead.
**Legislation:** VAT Act Art. 38(2).

### EC13 -- Small business exceeds EUR 60,000 threshold [T1]
**Situation:** Small business (exempt) turnover exceeds EUR 60,000 during the year.
**Resolution:** Must register for PDV from the supply that causes the breach. Must charge PDV on all subsequent supplies. Can claim input PDV from registration date.
**Legislation:** VAT Act Art. 90(2).

### EC14 -- Import of physical goods via customs [T2]
**Situation:** Client imports goods from China via the port of Rijeka.
**Resolution:** PDV assessed by customs at the border. Import PDV appears on customs declaration. Report in II.8 (base) and III.8 (input PDV). Flag for reviewer: confirm customs documentation and that amounts match.
**Legislation:** VAT Act Art. 32-33.

### EC15 -- Mixed invoice from EU supplier (goods + installation) [T1]
**Situation:** Italian supplier invoice covers both physical goods and installation services.
**Resolution:** Split by line item. Physical goods go to II.4/III.4 (intra-EU acquisition). Installation services go to II.5/III.5 (EU services). If line items not separated, [T2] flag for reviewer.
**Legislation:** VAT Act Art. 9 (goods acquisition) and Art. 17 (services).

### EC16 -- Domestic reverse charge (waste/scrap) [T1]
**Situation:** Croatian company sells scrap metal to another Croatian PDV-registered company. EUR 8,000.
**Resolution:** Domestic reverse charge. Seller invoices without PDV. Buyer: II.7 = EUR 8,000, output PDV = EUR 2,000 (25%). III.7 = EUR 2,000. Net zero.
**Legislation:** VAT Act Art. 75(3)(b).

### EC17 -- Sale of immovable property (option to tax) [T2]
**Situation:** Company sells a building more than 2 years after first occupation. Default: exempt without credit.
**Resolution:** Seller may opt to tax the supply (Art. 40(1)(j) option) with buyer's agreement, in which case domestic reverse charge applies. Flag for reviewer: confirm if option to tax is exercised and buyer agrees.
**Legislation:** VAT Act Art. 40(1)(j) and Art. 75(3)(c).

---

## Step 12: VAT Rates -- Detailed Supply Classification [T1]

### 25% Standard Rate (Art. 38(1))

| Supply Category | Examples |
|----------------|----------|
| General goods | Electronics, furniture, clothing, household items, motor vehicles |
| Professional services | Legal, accounting, consulting, IT, advertising |
| Telecommunications | Mobile, fixed-line, internet |
| Alcohol | Beer, wine, spirits |
| Tobacco | Cigarettes, cigars |
| Construction materials | Cement, steel, timber |
| Energy | Electricity, gas, fuel |

### 13% Reduced Rate (Art. 38(2), Annex II)

| Supply Category | Specific Items |
|----------------|----------------|
| Accommodation | Hotel rooms, guesthouses, camping, Airbnb (commercial) |
| Restaurant/catering | Dine-in meals, takeaway food (excluding alcohol) |
| Newspapers (print) | Daily and weekly newspapers |
| Water supply | Drinking water distribution |
| Pharmaceuticals (certain) | Non-prescription medicines on approved list |
| Cultural events | Theatre, concerts, cinema, museums |
| Sporting events | Admission to sports matches, facilities |
| Funeral services | Cremation, burial, undertaker |
| Firewood | Firewood, wood chips for heating |

### 5% Super-Reduced Rate (Art. 38(3), Annex I)

| Supply Category | Specific Items |
|----------------|----------------|
| Basic foodstuffs | White and black bread, milk, eggs, cooking oil, butter |
| Baby food | Infant formula, baby cereals, baby food jars |
| Books | Printed and electronic books |
| Scientific journals | Academic and research publications |
| Medical equipment | Hearing aids, prosthetics, wheelchairs, orthopedic devices |
| Menstrual products | Tampons, pads, menstrual cups |

---

## Step 13: Comparison with Malta

| Feature | Croatia (HR) | Malta (MT) |
|---------|-------------|------------|
| Standard rate | 25% | 18% |
| Reduced rates | 13%, 5% | 12%, 7%, 5% |
| Return form | PDV form (~4 sections) | VAT3 (45 boxes) |
| Filing frequency | Monthly | Quarterly (Art. 10), Annual (Art. 11) |
| Filing deadline | 20th (until 2025) / last day (from 2026) | 21st of month after quarter |
| Payment deadline | Same as filing | Same as filing |
| Small enterprise threshold | EUR 60,000 | EUR 35,000 |
| Capital goods movable | 5-year adjustment | > EUR 1,160 gross |
| Capital goods immovable | 10-year adjustment | No specific adjustment period |
| Blocked: passenger cars | 50% (mixed use with BIK); 0% (no BIK) | Fully blocked (10th Schedule) |
| Blocked: entertainment | 50% deductible | Fully blocked (10th Schedule) |
| Blocked: yachts/aircraft | Fully blocked | Blocked (10th Schedule) |
| Domestic reverse charge | Construction, waste, emissions, gold | No domestic reverse charge |
| Fiscalization | Mandatory e-invoicing (from 2026 for B2B) | No fiscalization |
| Partial exemption | Annual adjustment required | No de minimis |
| Refund mechanism | Carry forward or refund request | Carry forward / refund request |
| Currency | EUR (adopted 1 January 2023) | EUR |
| Tax authority | Porezna uprava | CFR |
| Filing portal | ePorezna | cfr.gov.mt |

---

## Step 14: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Qualified accountant must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to qualified accountant. Document gap.
```

---

## Step 15: Test Suite

### Test 1 -- Standard domestic purchase, 25% PDV [T1]
**Input:** Croatian supplier, office supplies, gross EUR 250, PDV EUR 50, net EUR 200. Registered taxpayer.
**Expected output:** III.3 += EUR 50. Fully recoverable.

### Test 2 -- EU service subscription, reverse charge [T1]
**Input:** Irish supplier, consulting services EUR 1,000, no VAT on invoice. Registered taxpayer.
**Expected output:** II.5 = EUR 1,000, output PDV = EUR 250 (25%). III.5 = EUR 250. Net = zero.

### Test 3 -- Representation expense (50%) [T1]
**Input:** Croatian restaurant, business dinner EUR 500 gross, PDV EUR 100 (25%), net EUR 400.
**Expected output:** III.3 += EUR 50 (50% of EUR 100). Only 50% recoverable.

### Test 4 -- EU B2B sale, zero rated [T1]
**Input:** Registered taxpayer sells goods to German company EUR 5,000, 0% PDV.
**Expected output:** I.4 = EUR 5,000. No output PDV. Report on EC Sales List (ZP).

### Test 5 -- Small business, purchase [T1]
**Input:** Small business (under EUR 60,000) purchases supplies EUR 1,000 + PDV EUR 250.
**Expected output:** No PDV return entry. Small business cannot recover input PDV.

### Test 6 -- Passenger vehicle, mixed use (50%) [T1]
**Input:** Registered taxpayer purchases car EUR 30,000 + PDV EUR 7,500 (25%). BIK calculated.
**Expected output:** III.3 += EUR 3,750 (50% of EUR 7,500). Only 50% deductible.

### Test 7 -- Non-EU software (US), reverse charge [T1]
**Input:** US supplier (AWS), monthly fee EUR 100, no VAT on invoice. Registered taxpayer.
**Expected output:** II.6 = EUR 100, output PDV = EUR 25 (25%). III.6 = EUR 25. Net = zero.

### Test 8 -- Construction services (domestic RC) [T1]
**Input:** Croatian subcontractor, construction work EUR 20,000. Both parties PDV registered.
**Expected output:** Buyer: II.7 = EUR 20,000, output PDV = EUR 5,000 (25%). III.7 = EUR 5,000. Net = zero.

### Test 9 -- Export of goods [T1]
**Input:** Croatian company exports to US client, EUR 15,000.
**Expected output:** I.5 = EUR 15,000. No output PDV. Zero-rated.

### Test 10 -- Passenger vehicle, no BIK (0%) [T1]
**Input:** Company car EUR 20,000 + PDV EUR 5,000. Private use portion exists but no BIK calculated.
**Expected output:** III.3 += EUR 0. PDV NOT deductible (no BIK = no deduction under Art. 61(2)(a)).

### Test 11 -- Accommodation at 13% (business trip) [T1]
**Input:** Hotel in Croatia, EUR 150 + EUR 19.50 PDV (13%). Business purpose.
**Expected output:** III.2 += EUR 19.50. Fully deductible.

### Test 12 -- Yacht purchase (blocked) [T1]
**Input:** Pleasure yacht EUR 100,000 + PDV EUR 25,000. Not a charter business.
**Expected output:** III.3 += EUR 0. PDV BLOCKED (Art. 61(1)(b)). Full EUR 125,000 is cost.

---

## Step 16: Annual PDV Return [T1]

**Legislation:** VAT Act Art. 85(7); VAT Regulation Art. 175.

The annual PDV return is a reconciliation filing submitted by 28 February of the following year. It contains:

| Section | Content |
|---------|---------|
| Summary of all periodic returns | Totals for each row across all 12 monthly returns |
| Turnover by rate | Breakdown of taxable supplies by 25%, 13%, 5% |
| Total input PDV for the year | Sum of all deductions claimed |
| Pro-rata adjustment | Final pro-rata calculation (if partial exemption applies) |
| Capital goods adjustment | Annual review of capital goods deduction proportions |
| Final settlement | Reconciliation of all periodic payments/credits against annual total |

The annual return does NOT replace periodic (monthly) returns. It is an additional filing for reconciliation purposes.

---

## Step 17: Refund Process [T1]

| Feature | Detail | Legislation |
|---------|--------|-------------|
| Refund request | Automatic if excess credit (IV.2) on return | VAT Act Art. 67 |
| Refund timeline | Within 30 days of filing deadline | General Tax Act Art. 112 |
| Audit delay | Tax authority may audit before releasing refund | General Tax Act Art. 113 |
| Carry forward | Credit can be carried forward to next period | VAT Act Art. 67(2) |
| Offset | Tax authority may offset credit against other tax liabilities | General Tax Act Art. 110 |

---

## Step 18: Out of Scope -- Direct Tax (Reference Only) [T3]

This skill does not compute income tax. The following is reference information only. Escalate to qualified adviser.

- **Corporate income tax (porez na dobit):** 10% (profit up to EUR 1M) / 18% (profit over EUR 1M)
- **Personal income tax:** Progressive: 20% up to EUR 50,400 / 30% above EUR 50,400
- **Dividend tax:** 10% withholding
- **Social contributions:** employer ~16.5%, employee ~20%
- **Surtax (prirez):** Local municipality surcharge on income tax (varies by city, up to 18% in Zagreb)
- **Tourist tax (boravisna pristojba):** Applicable to accommodation providers
- **Local self-government tax (prirez porezu na dohodak):** Surcharge on income tax, varies by municipality

### Key Croatia-Specific Notes
- Croatia adopted the euro (EUR) on 1 January 2023, replacing the kuna (HRK)
- Croatia joined the Schengen area on 1 January 2023
- Historical amounts in HRK should be converted at the fixed rate: 1 EUR = 7.53450 HRK
- All VAT amounts from 2023 onward are in EUR

---

## PROHIBITIONS [T1]

- NEVER let AI guess PDV box -- it is 100% deterministic from facts
- NEVER apply reverse charge to out-of-scope categories (wages, dividends, bank charges)
- NEVER apply reverse charge to local consumption services abroad (hotel, restaurant, taxi)
- NEVER allow small business (exempt) clients to claim input PDV
- NEVER confuse zero-rated (exports/intra-EU, input PDV deductible) with exempt without credit (financial, input PDV NOT deductible)
- NEVER apply reverse charge when EU supplier charged local VAT > 0%
- NEVER apply 100% input deduction on passenger vehicles without confirming exclusive business use
- NEVER apply any deduction on passenger vehicles if no BIK is calculated (Art. 61(2)(a))
- NEVER apply 100% input deduction on representation expenses -- always 50%
- NEVER claim input PDV on yachts/aircraft unless proven business exception
- NEVER ignore fiscalization requirements for invoices
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude

---

## Contribution Notes

This skill covers Croatia's VAT system based on the Zakon o porezu na dodanu vrijednost (OG 73/13 as amended). Key distinctive features include: the 25%/13%/5% three-tier rate structure, the 50% restriction on passenger vehicles (with BIK requirement) and representation expenses, the mandatory fiscalization of all invoices, the domestic reverse charge for construction and waste, and Croatia's 2023 adoption of the euro. Validation by a qualified Croatian ovlasteni revizor or porezni savjetnik is required before production use.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
