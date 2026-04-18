---
name: slovenia-vat-return
description: Use this skill whenever asked to prepare, review, or create a Slovenian VAT return (DDV-O form) for any client. Trigger on phrases like "prepare VAT return", "do the DDV", "fill in DDV-O", "create the return", "Slovenian VAT", or any request involving Slovenia VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Slovenian VAT classification rules, box mappings, deductibility rules, reverse charge treatment, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any VAT-related work for Slovenia.
---

# Slovenia VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Slovenia |
| Jurisdiction Code | SI |
| Primary Legislation | Zakon o davku na dodano vrednost (ZDDV-1, VAT Act, Official Gazette RS 13/11 as amended through 2025) |
| Supporting Legislation | Pravilnik o izvajanju ZDDV-1 (Implementing Regulation); EU VAT Directive 2006/112/EC; Act on Tax Procedure (ZDavP-2) |
| Tax Authority | Financna uprava Republike Slovenije (FURS -- Financial Administration of the Republic of Slovenia) |
| Filing Portal | https://edavki.durs.si (eDavki) |
| Contributor | Auto-generated draft -- requires validation |
| Validated By | Deep research verification, April 2026 |
| Validation Date | 2026-04-10 |
| Skill Version | 1.0 |
| Status | validated |
| Confidence Coverage | Tier 1: box assignment, reverse charge, deductibility blocks, derived calculations. Tier 2: partial exemption pro-rata, real estate options, vehicle use, flat-rate agriculture. Tier 3: complex group structures, non-standard supplies, financial services. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified davcni svetovalec must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified adviser.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and DDV ID** [T1] -- SI + 8 digits (for VIES)
2. **VAT registration status** [T1] -- Standard registered, flat-rate scheme (agriculture, Sec. 45), or exempt (small business under EUR 60,000)
3. **Filing frequency** [T1] -- Monthly (turnover > EUR 210,000) or quarterly (turnover <= EUR 210,000)
4. **Industry/sector** [T2] -- impacts deductibility (construction, transport, agriculture, tourism)
5. **Does the business make exempt supplies?** [T2] -- If yes, partial attribution required (sorazmerni delež); reviewer must confirm
6. **Does the business trade goods for resale?** [T1] -- impacts classification
7. **Excess credit brought forward** [T1] -- from prior period (presežek DDV)
8. **Deductible proportion (%)** [T2] -- if partial exemption applies
9. **New reporting obligations (from July 2025)** [T1] -- Record of Charged DDV and Record of DDV Deduction submitted with DDV-O

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (obračunani DDV -- output DDV) or Purchase (odbitni DDV -- input DDV / deductible DDV)
- Salaries, social contributions (ZPIZ, ZZZS), income tax, loan repayments, dividends, bank charges = OUT OF SCOPE
- **Legislation:** ZDDV-1 Art. 3-5 (taxable transactions), Art. 6 (supply of goods), Art. 14 (supply of services)

### 1b. Determine Counterparty Location [T1]
- Slovenia (domestic): supplier/customer country is SI
- EU: AT, BE, BG, HR, CY, CZ, DK, EE, FI, FR, DE, GR, HU, IE, IT, LV, LT, LU, MT, NL, PL, PT, RO, SK, ES, SE
- Non-EU: everything else
- **Note:** UK is Non-EU post-Brexit. Serbia, Bosnia-Herzegovina, North Macedonia are Non-EU.

### 1c. Determine VAT Rate [T1]

| Rate | Category | Legislation |
|------|----------|-------------|
| 22% | Standard rate -- most goods and services | ZDDV-1 Art. 41(1) |
| 9.5% | Reduced rate -- foodstuffs (Annex I), water supply, medicines, medical equipment, books, newspapers, accommodation, cultural/sporting events, renovation of private dwellings (conditions), funeral services, passenger transport, agricultural inputs | ZDDV-1 Art. 41(2), Annex I |
| 5% | Super-reduced rate -- books (printed and electronic), newspapers | ZDDV-1 Art. 41(3), Annex Ia |
| 0% | Zero-rated -- intra-EU supplies of goods (Art. 46), exports outside EU (Art. 52) | ZDDV-1 Art. 46-53 |
| Exempt with credit | International transport, supplies connected to international trade | ZDDV-1 Art. 52-57 |
| Exempt without credit | Financial services (Art. 44), insurance (Art. 43), healthcare (Art. 42(1)(a)), education (Art. 42(1)(b)), postal services, gambling, residential rental (Art. 44(2)), land except building plots, transfer of going concern | ZDDV-1 Art. 42-44 |

### 1d. Determine Expense Category [T1]
- Capital goods: tangible assets used for business, subject to adjustment on change of use
- Immovable property: 20-year adjustment period (ZDDV-1 Art. 69)
- Movable capital goods: 5-year adjustment period (ZDDV-1 Art. 68)
- Resale: goods bought to resell
- Overhead/services: everything else
- **Legislation:** ZDDV-1 Art. 68-69 (adjustment of deduction for capital goods)

---

## Step 2: VAT Return Form Structure (DDV-O) [T1]

**Legislation:** ZDDV-1 Art. 88-89; Implementing Regulation.

### Section A -- Output DDV (Obracunani DDV)

| Field | Description | Rate | Notes |
|-------|-------------|------|-------|
| 11 | Domestic supplies at 22% -- taxable base | 22% | Standard-rated sales |
| 12 | DDV on field 11 | 22% | Calculated |
| 13 | Domestic supplies at 9.5% -- taxable base | 9.5% | Reduced-rated sales |
| 14 | DDV on field 13 | 9.5% | Calculated |
| 14a | Domestic supplies at 5% -- taxable base | 5% | Super-reduced sales |
| 14b | DDV on field 14a | 5% | Calculated |
| 15 | Intra-Community acquisitions of goods -- taxable base | Self-assessed | Reverse charge |
| 16 | DDV on field 15 | Self-assessed | At applicable SI rate |
| 17 | Services received from EU (reverse charge) -- taxable base | Self-assessed | B2B services from EU |
| 18 | DDV on field 17 | Self-assessed | At applicable SI rate |
| 19 | Imports -- taxable base | Self-assessed | From customs / self-assessment |
| 20 | DDV on field 19 | Self-assessed | At applicable rate |
| 21 | Other taxable transactions (domestic reverse charge, non-EU services) -- base | Self-assessed | Construction, waste, emissions, non-EU |
| 22 | DDV on field 21 | Self-assessed | At applicable rate |
| 23 | Total output DDV | Sum | 12 + 14 + 14b + 16 + 18 + 20 + 22 |
| 24 | Exempt supplies with right of deduction (intra-EU supplies, exports) | -- | Zero-rated output |
| 25 | Exempt supplies without right of deduction (financial, insurance, healthcare) | -- | No DDV charged |

### Section B -- Input DDV (Odbitni DDV)

| Field | Description | Notes |
|-------|-------------|-------|
| 31 | Input DDV on domestic purchases | All domestic input at all rates |
| 32 | Input DDV on intra-Community acquisitions | Mirrors Field 16 (if deductible) |
| 33 | Input DDV on services from EU | Mirrors Field 18 |
| 34 | Input DDV on imports | Mirrors Field 20 |
| 35 | Input DDV on other (domestic reverse charge, non-EU services) | Mirrors Field 22 |
| 36 | Flat-rate compensation (agriculture, Sec. 45) | For purchases from flat-rate farmers |
| 37 | Adjustment of input DDV | Corrections, capital goods, pro-rata |
| 38 | Total input DDV (deductible) | Sum: 31 + 32 + 33 + 34 + 35 + 36 + 37 |

### Section C -- DDV Liability

| Field | Description | Notes |
|-------|-------------|-------|
| 41 | DDV to pay (Field 23 - Field 38, if positive) | Pay to FURS |
| 42 | DDV excess / refund claim (Field 38 - Field 23, if positive) | Request refund or carry forward |
| 51 | DDV liability (including any corrections/interest) | Final amount due |

---

## Step 3: Transaction Classification Matrix [T1]

### Purchases -- Domestic (Slovenian Supplier)

| VAT Rate | Category | Input Field | Notes |
|----------|----------|-------------|-------|
| 22% | Overhead/services | Field 31 | Standard domestic |
| 9.5% | Overhead/services | Field 31 | Food, accommodation, books |
| 5% | Overhead/services | Field 31 | Basic foodstuffs |
| 0% | Any | -- | No DDV to claim |
| Any | Capital goods | Field 31 | Track for 5/20-year adjustment |
| Any | Blocked category (vehicle, yacht, entertainment) | -- | No deduction |

### Purchases -- EU Supplier (Reverse Charge)

| Type | Output Field | Input Field | Notes |
|------|-------------|-------------|-------|
| Physical goods | Field 15/16 | Field 32 | Intra-EU acquisition |
| Services (B2B) | Field 17/18 | Field 33 | EU service RC |
| Out-of-scope (wages etc.) | -- | -- | NEVER reverse charge |
| Local consumption (hotel, restaurant abroad) | -- | -- | Foreign VAT at source |

### Purchases -- Non-EU Supplier

| Type | Output Field | Input Field | Notes |
|------|-------------|-------------|-------|
| Services (B2B) | Field 21/22 | Field 35 | Non-EU service import |
| Physical goods (customs) | Field 19/20 | Field 34 | Import via customs |
| Out-of-scope | -- | -- | NEVER reverse charge |

### Sales -- Domestic

| Rate | Field | Notes |
|------|-------|-------|
| 22% | Field 11/12 | Standard-rated |
| 9.5% | Field 13/14 | Reduced-rated |
| 5% | Field 14a/14b | Super-reduced |
| Exempt with credit | Field 24 | IC supply, exports |
| Exempt without credit | Field 25 | Financial, insurance, healthcare |

### Sales -- EU / Non-EU

| Location | Type | Field | Notes |
|----------|------|-------|-------|
| EU B2B goods | Intra-EU supply | Field 24 | Zero-rated, EC Sales List |
| EU B2B services | Place of supply in customer MS | Included in Field 24 | VIES |
| Non-EU | Export | Field 24 | Zero-rated, customs docs |

---

## Step 4: Reverse Charge Mechanics [T1]

**Legislation:** ZDDV-1 Art. 76-76c (reverse charge); Art. 25 (place of supply for services).

### Intra-EU Acquisitions of Goods (Art. 11)
1. Report taxable base in Field 15 and self-assessed output DDV in Field 16
2. Claim input DDV in Field 32
3. Net effect: zero for fully taxable businesses
4. Report on EC Sales List (RP-O form)

### EU Services Received -- B2B (Art. 25(1))
1. Report in Field 17 (base) / Field 18 (output DDV)
2. Claim in Field 33
3. Net effect: zero

### Non-EU Services Received
1. Report in Field 21 (base) / Field 22 (output DDV)
2. Claim in Field 35
3. Net effect: zero

### Domestic Reverse Charge [T1]
**Legislation:** ZDDV-1 Art. 76(1)(c)-(f), Art. 76a-76c.

| Supply Type | Legislation | Notes |
|-------------|-------------|-------|
| Construction services related to immovable property | Art. 76a(1) | All construction, renovation, maintenance |
| Supply of waste and scrap | Art. 76a(3), Annex III-a | Metals, paper, glass, plastic |
| CO2 emission allowances | Art. 76a(4) | Greenhouse gas permits |
| Supply of immovable property where seller opts to tax | Art. 76a(2) | Option to tax after exempt period |
| Supply of gold material (raw/semi-finished) | Art. 76a(5) | Raw gold |

Domestic reverse charge procedure:
1. Report in Field 21 (base) / Field 22 (output DDV)
2. Claim in Field 35 (input DDV)
3. Net effect: zero

### Exceptions to Reverse Charge [T1]
- Out-of-scope categories: NEVER reverse charge
- Local consumption abroad: NOT reverse charge; foreign VAT paid at source
- EU supplier charged local VAT > 0%: NOT reverse charge
- Construction services where one party is not DDV-registered: normal DDV applies

---

## Step 5: Deductibility Check

### Blocked Categories [T1]
**Legislation:** ZDDV-1 Art. 66 (restrictions on input tax deduction).

| Category | DDV Recovery | Legislation | Notes |
|----------|-------------|-------------|-------|
| Passenger cars and motorcycles | 0% | Art. 66(1)(1) | Unless for: passenger transport, goods transport, leasing/rental as business, driving schools, combined public transport vehicles, vehicles exclusively for transporting deceased |
| Fuel, lubricants, spare parts for blocked vehicles | 0% | Art. 66(1)(1) | Follows vehicle restriction |
| Yachts and boats for sport/recreation | 0% | Art. 66(1)(2) | Unless: transport, leasing/rental, resale |
| Aircraft | 0% | Art. 66(1)(3) | Unless: transport, leasing/rental, resale |
| Entertainment and representation | 0% | Art. 66(1)(4) | Fully blocked [T2 -- some case law suggests partial deduction in specific sectors; confirm with reviewer] |
| Personal use items | 0% | Art. 63(1) | No deduction for private use |
| Supplies for exempt-without-credit activities | 0% | Art. 63(1) | Financial, insurance, education inputs |

### Vehicle Exceptions (Art. 66(1)(1)) [T1]

| Exception | Deduction | Notes |
|-----------|-----------|-------|
| Taxi services | 100% | Vehicle used for licensed taxi |
| Driving school | 100% | Vehicle used for driving instruction |
| Car rental as business | 100% | Vehicles in rental fleet |
| Delivery / goods transport | 100% | Vehicle used for goods delivery |
| Public transport combined vehicles | 100% | Combined passenger/goods |
| Hearse / transport of deceased | 100% | Funeral vehicles |
| N1 category vans / trucks | 100% | Commercial vehicles (not blocked) |

### Registration-Based Recovery [T1]

| Registration Type | Input DDV Recovery | Legislation |
|-------------------|-------------------|-------------|
| Standard registered | Full recovery (subject to blocks) | Art. 63-66 |
| Small business (under EUR 60,000) | NO recovery | Art. 94 |
| Flat-rate agriculture (Sec. 45) | No standard input DDV; compensated via flat-rate mechanism | Art. 45 |

### Partial Exemption [T2]
**Legislation:** ZDDV-1 Art. 65.

If business makes both taxable and exempt supplies:

`Recovery % = (Taxable Supplies + Zero-Rated Supplies) / Total Supplies * 100`

| Rule | Detail | Legislation |
|------|--------|-------------|
| Rounding | Round to nearest whole percent | Art. 65(5) |
| De minimis | If >= 95%, treated as 100% | Art. 65(6) |
| Provisional | Use prior year proportion during year | Art. 65(7) |
| Annual adjustment | True-up at year-end in last period | Art. 65(8) |
| Excluded | Incidental financial/property transactions | Art. 65(4) |

**Flag for reviewer: proportion must be confirmed. Annual adjustment required.**

---

## Step 6: New Reporting Obligations (from July 2025) [T1]

**Legislation:** ZDDV-1 Art. 88a-88b (as amended 2025).

From 1 July 2025, taxable persons must submit two additional records alongside the DDV-O form:

| Record | Description | Deadline |
|--------|-------------|----------|
| Record of Charged DDV (Evidenca obracunanega DDV) | Detailed list of all output DDV transactions | Same as DDV-O |
| Record of DDV Deduction (Evidenca odbitka DDV) | Detailed list of all input DDV deductions claimed | Same as DDV-O |

### Key Requirements
- Electronic format submitted via eDavki
- Must reconcile with DDV-O totals
- Individual invoice-level detail required
- Replaces the previous summary-only approach
- Penalties for non-compliance: EUR 400 - EUR 10,000

---

## Step 7: Flat-Rate Agriculture Scheme (Sec. 45) [T2]

**Legislation:** ZDDV-1 Art. 45; Implementing Regulation Art. 125-128.

| Feature | Detail |
|---------|--------|
| Eligibility | Agricultural and forestry producers meeting criteria |
| How it works | Flat-rate farmers do not charge DDV but receive a flat-rate compensation from buyers |
| Compensation rate | 8% of purchase price (buyer pays on top of agreed price) |
| Buyer treatment | Buyer records compensation in Field 36 (input DDV equivalent) |
| Flat-rate farmer | Does not file DDV-O returns |
| Threshold | Can opt for standard registration if desired |

**Flag for reviewer: confirm farmer's registration status. If standard registered, flat-rate does not apply.**

---

## Step 8: Key Thresholds

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Small business exemption | EUR 60,000 annual turnover (from 2025) | ZDDV-1 Art. 94 |
| EU SME scheme (from 2025) | EUR 85,000 domestic + EUR 100,000 EU-wide | EU Directive 2020/285 |
| Monthly filing threshold | Annual turnover > EUR 210,000 | ZDDV-1 Art. 88(1) |
| EU distance selling threshold | EUR 10,000/calendar year | EU Directive 2017/2455 |
| Intrastat arrivals | EUR 220,000 | SURS regulation |
| Intrastat dispatches | EUR 270,000 | SURS regulation |
| Capital goods -- movable | 5-year adjustment | ZDDV-1 Art. 68 |
| Capital goods -- immovable | 20-year adjustment | ZDDV-1 Art. 69 |
| Flat-rate agriculture compensation | 8% | ZDDV-1 Art. 45 |
| Coefficient de minimis | >= 95% treated as 100% | ZDDV-1 Art. 65(6) |

---

## Step 9: VAT Registration [T1]

| Feature | Detail | Legislation |
|---------|--------|-------------|
| VAT number format | SI + 8 digits | ZDDV-1 Art. 78 |
| Mandatory registration | Turnover > EUR 60,000 in 12 months | ZDDV-1 Art. 78(1) |
| Registration deadline | Before exceeding threshold | ZDDV-1 Art. 78(2) |
| Voluntary registration | May register below threshold | ZDDV-1 Art. 78(3) |
| Flat-rate agriculture | Separate scheme, not standard registration | ZDDV-1 Art. 45 |
| Deregistration | If turnover stays below threshold for 12 months | ZDDV-1 Art. 81 |
| Fiscal representative | Required for non-EU businesses without Slovenian establishment | ZDDV-1 Art. 79 |
| Group registration | Not available in Slovenia | -- |

---

## Step 10: Filing Deadlines and Penalties

### Filing Deadlines [T1]

| Filing | Period | Deadline | Legislation |
|--------|--------|----------|-------------|
| DDV-O (monthly) | Monthly | Last business day of month following tax period | ZDDV-1 Art. 88(1) |
| DDV-O (quarterly) | Quarterly | Last business day of month following quarter end | ZDDV-1 Art. 88(2) |
| Record of Charged DDV (from July 2025) | Same as DDV-O | Same deadline | ZDDV-1 Art. 88a |
| Record of DDV Deduction (from July 2025) | Same as DDV-O | Same deadline | ZDDV-1 Art. 88b |
| EC Sales List (RP-O) | Monthly | 20th of month following period | ZDDV-1 Art. 90 |
| Intrastat | Monthly | 15th of following month | SURS regulation |
| DDV payment | Same as return | Same as filing deadline | ZDavP-2 Art. 64 |

### Penalties [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing of DDV-O | EUR 400 - EUR 10,000 (legal entity); EUR 200 - EUR 4,000 (individual) | ZDavP-2 Art. 396 |
| Late payment of DDV | Interest at reference rate + 2% p.a. (min 2%) | ZDavP-2 Art. 95 |
| Tax shortfall (additional assessment) | Up to 20% of additional tax | ZDavP-2 Art. 397 |
| Failure to register | EUR 2,000 - EUR 50,000 + back-assessment | ZDavP-2 Art. 394 |
| New records non-compliance (from July 2025) | EUR 400 - EUR 10,000 | ZDDV-1 Art. 88a-88b |
| EC Sales List late/missing | EUR 400 - EUR 10,000 | ZDavP-2 Art. 396 |
| Failure to issue invoice | EUR 1,000 - EUR 25,000 per invoice | ZDavP-2 Art. 395 |

---

## Step 11: Derived Box Calculations [T1]

```
Field 23 = Field 12 + Field 14 + Field 14b + Field 16 + Field 18 + Field 20 + Field 22
Field 38 = Field 31 + Field 32 + Field 33 + Field 34 + Field 35 + Field 36 + Field 37

IF Field 23 > Field 38 THEN
  Field 41 = Field 23 - Field 38  -- Tax Payable
  Field 42 = 0
ELSE
  Field 41 = 0
  Field 42 = Field 38 - Field 23  -- Excess Credit / Refund
END

Field 51 = Field 41 + corrections/interest (if any)
```

---

## Step 12: Edge Case Registry

### EC1 -- EU hotel / restaurant / taxi booked abroad [T1]
**Situation:** Slovenian DDV-registered client pays for hotel in Italy. Invoice shows Italian 10% VAT.
**Resolution:** NOT reverse charge. Foreign VAT was charged at source. No DDV fields. Italian VAT is irrecoverable cost.
**Legislation:** ZDDV-1 Art. 27 -- place of supply for accommodation is where property is located.

### EC2 -- SaaS subscription from non-EU provider (AWS, Google) [T1]
**Situation:** Monthly charge from US company, no VAT on invoice.
**Resolution:** Reverse charge. Field 21 (net base) / Field 22 (output DDV at 22%). Field 35 (input DDV at 22%). Net effect zero.
**Legislation:** ZDDV-1 Art. 25(1) -- place of supply for B2B services is customer's establishment.

### EC3 -- Construction services (domestic reverse charge) [T1]
**Situation:** Slovenian construction company provides building services to another SI DDV-registered business. EUR 40,000.
**Resolution:** Domestic reverse charge. Supplier invoices without DDV. Recipient: Field 21 = EUR 40,000, Field 22 = EUR 8,800 (22%). Field 35 = EUR 8,800. Net zero.
**Legislation:** ZDDV-1 Art. 76a(1).

### EC4 -- Passenger car purchase (blocked) [T1]
**Situation:** Client purchases a private car EUR 25,000 + DDV EUR 5,500 (22%). Mixed use.
**Resolution:** Input DDV is NOT deductible under Art. 66(1)(1). Full EUR 30,500 is cost. Exception only for: taxi, driving school, car rental, goods delivery, transport of deceased.
**Legislation:** ZDDV-1 Art. 66(1)(1).

### EC5 -- Fuel for blocked vehicle [T1]
**Situation:** Client purchases fuel EUR 100 + DDV EUR 22 (22%) for a blocked passenger car.
**Resolution:** Input DDV on fuel is also NOT deductible. Follows the vehicle restriction.
**Legislation:** ZDDV-1 Art. 66(1)(1).

### EC6 -- Export sale outside EU [T1]
**Situation:** Client sells goods to US customer. EUR 15,000.
**Resolution:** Zero-rated. Report in Field 24 (exempt with right of deduction). No output DDV. Input DDV on related costs fully recoverable.
**Legislation:** ZDDV-1 Art. 52.

### EC7 -- Credit notes [T1]
**Situation:** Client receives a credit note from supplier.
**Resolution:** Reverse the original entry. Reduce applicable input DDV field.
**Legislation:** ZDDV-1 Art. 39 (correction of tax base).

### EC8 -- Intra-Community acquisition of goods [T1]
**Situation:** Client purchases goods from German supplier at 0% with valid VIES numbers.
**Resolution:** Reverse charge. Field 15 (base) / Field 16 (output DDV at 22%). Field 32 (input DDV at 22%). Net zero. Report on EC Sales List (RP-O).
**Legislation:** ZDDV-1 Art. 11.

### EC9 -- New reporting obligations from July 2025 [T2]
**Situation:** From 1 July 2025, taxable persons must submit Record of Charged DDV and Record of DDV Deduction alongside the DDV-O form.
**Resolution:** Flag for reviewer: ensure client's accounting system can generate the required records in electronic format for eDavki submission. Penalties: EUR 400 - EUR 10,000.
**Legislation:** ZDDV-1 Art. 88a-88b.

### EC10 -- Flat-rate agriculture purchase [T1]
**Situation:** DDV-registered business buys produce from a flat-rate farmer for EUR 1,000.
**Resolution:** Business pays EUR 1,000 + EUR 80 flat-rate compensation (8%). Record EUR 80 in Field 36 as input DDV equivalent.
**Legislation:** ZDDV-1 Art. 45.

### EC11 -- Yacht purchase (blocked) [T1]
**Situation:** Company buys pleasure yacht EUR 50,000 + DDV EUR 11,000.
**Resolution:** Input DDV BLOCKED (Art. 66(1)(2)). Full EUR 61,000 is cost. Exception only for charter/rental/transport business.
**Legislation:** ZDDV-1 Art. 66(1)(2).

### EC12 -- Domestic reverse charge (waste/scrap) [T1]
**Situation:** Slovenian company sells scrap metal to another SI DDV-registered company. EUR 5,000.
**Resolution:** Domestic reverse charge. Seller invoices without DDV. Buyer: Field 21 = EUR 5,000, Field 22 = EUR 1,100 (22%). Field 35 = EUR 1,100. Net zero.
**Legislation:** ZDDV-1 Art. 76a(3).

### EC13 -- Immovable property sale (option to tax) [T2]
**Situation:** Company sells a building more than 2 years after first occupation. Default: exempt without credit.
**Resolution:** Seller may opt to tax (Art. 45(10)), in which case domestic reverse charge applies. Flag for reviewer: confirm option-to-tax election and buyer's agreement.
**Legislation:** ZDDV-1 Art. 45(10) and Art. 76a(2).

### EC14 -- Small business exceeds EUR 60,000 [T1]
**Situation:** Small business (exempt) turnover exceeds EUR 60,000 during the year.
**Resolution:** Must register for DDV from the supply that caused the breach. Must charge DDV on all subsequent supplies. Can claim input DDV from registration date.
**Legislation:** ZDDV-1 Art. 94(2).

### EC15 -- Import of physical goods via customs [T2]
**Situation:** Client imports goods from China via Koper port.
**Resolution:** DDV assessed by customs at the border. Import DDV appears on customs declaration. Report in Field 19 (base) / Field 20 (customs DDV) / Field 34 (input DDV). Flag for reviewer: confirm customs documentation.
**Legislation:** ZDDV-1 Art. 34-36.

### EC16 -- Mixed invoice from EU supplier [T1]
**Situation:** German supplier invoice covers physical goods and consulting services.
**Resolution:** Split by line item. Goods: Field 15/16/32. Services: Field 17/18/33. If not separated, [T2] flag for reviewer.
**Legislation:** ZDDV-1 Art. 11 (goods) and Art. 25 (services).

### EC17 -- Car rental business vehicle purchase [T1]
**Situation:** Car rental company buys passenger car EUR 20,000 + DDV EUR 4,400 for rental fleet.
**Resolution:** Full deduction: Field 31 += EUR 4,400. Car rental is an exception to Art. 66(1)(1) block.
**Legislation:** ZDDV-1 Art. 66(1)(1) exception.

### EC18 -- Super-reduced rate purchase (5%) [T1]
**Situation:** Restaurant buys bread and milk EUR 210 gross, DDV EUR 10 (5%), net EUR 200.
**Resolution:** Field 31 += EUR 10. Fully deductible (business input at 5% super-reduced rate).
**Legislation:** ZDDV-1 Art. 41(3), Annex Ia.

---

## Step 13: VAT Rates -- Detailed Supply Classification [T1]

### 22% Standard Rate (Art. 41(1))

| Supply Category | Examples |
|----------------|----------|
| General goods | Electronics, furniture, clothing, motor vehicles, household items |
| Professional services | Legal, accounting, consulting, IT, advertising |
| Telecommunications | Mobile, fixed-line, internet |
| Alcohol | Beer, wine, spirits |
| Tobacco | Cigarettes, cigars |
| Construction materials | Cement, steel, timber |
| Energy | Electricity, gas, fuel |

### 9.5% Reduced Rate (Art. 41(2), Annex I)

| Supply Category | Examples |
|----------------|----------|
| Foodstuffs | Processed foods, meat, dairy, vegetables, fruit (general) |
| Water supply | Drinking water distribution |
| Medicines | Prescription and OTC pharmaceuticals |
| Medical equipment | Hearing aids, prosthetics, wheelchairs |
| Books and newspapers | Printed and electronic books, newspapers, periodicals |
| Accommodation | Hotels, guesthouses, camping, Airbnb |
| Cultural/sporting events | Theatre, cinema, museums, concerts, sports matches |
| Funeral services | Cremation, burial, undertaker |
| Passenger transport | Bus, train, taxi |
| Renovation of private dwellings | Qualifying residential renovation work |
| Agricultural inputs | Seeds, fertilizers, animal feed |

### 5% Super-Reduced Rate (Art. 41(3), Annex Ia)

| Supply Category | Examples |
|----------------|----------|
| Basic foodstuffs | Bread, flour, milk, butter, fresh fruit, fresh vegetables, eggs |

---

## Step 14: Comparison with Malta

| Feature | Slovenia (SI) | Malta (MT) |
|---------|--------------|------------|
| Standard rate | 22% | 18% |
| Reduced rates | 9.5%, 5% | 12%, 7%, 5% |
| Return form | DDV-O (~25 fields + records from July 2025) | Malta periodic VAT return (~45 boxes) |
| Filing frequency | Monthly / Quarterly | Quarterly (Art. 10), Annual (Art. 11) |
| Filing deadline | Last business day of following month | 21st of month after quarter |
| Payment deadline | Same as filing | Same as filing |
| Small enterprise threshold | EUR 60,000 | EUR 35,000 |
| Capital goods movable | 5-year adjustment | > EUR 1,160 gross |
| Capital goods immovable | 20-year adjustment | No specific adjustment period |
| Blocked: passenger cars | Fully blocked (Art. 66(1)(1)) | Fully blocked (10th Schedule) |
| Blocked: entertainment | Fully blocked (Art. 66(1)(4)) | Fully blocked (10th Schedule) |
| Blocked: yachts/aircraft | Fully blocked | Blocked (10th Schedule) |
| Domestic reverse charge | Construction, waste, emissions, gold, immovable property | No domestic reverse charge |
| Flat-rate agriculture | 8% compensation scheme (Art. 45) | No equivalent |
| New records (July 2025) | Record of Charged DDV + Record of DDV Deduction | No equivalent |
| Coefficient de minimis | >= 95% treated as 100% | No de minimis |
| Currency | EUR | EUR |
| Tax authority | FURS | CFR |
| Filing portal | eDavki | cfr.gov.mt |

---

## Step 15: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Davcni svetovalec must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to davcni svetovalec. Document gap.
```

---

## Step 16: Test Suite

### Test 1 -- Standard domestic purchase, 22% DDV [T1]
**Input:** Slovenian supplier, office supplies, gross EUR 244, DDV EUR 44, net EUR 200. Registered taxpayer.
**Expected output:** Field 31 += EUR 44. Fully recoverable.

### Test 2 -- EU service, reverse charge [T1]
**Input:** Austrian supplier, legal services EUR 1,000, no VAT. Registered taxpayer.
**Expected output:** Field 17 = EUR 1,000, Field 18 = EUR 220 (22%). Field 33 = EUR 220. Net = zero.

### Test 3 -- Passenger car (blocked) [T1]
**Input:** Registered client purchases car EUR 25,000 + DDV EUR 5,500 (22%). Mixed use.
**Expected output:** Input DDV = EUR 0. Blocked under Art. 66(1)(1). Full EUR 30,500 is cost.

### Test 4 -- EU B2B sale [T1]
**Input:** Registered client sells goods to Croatian company EUR 5,000, 0% DDV.
**Expected output:** Field 24 = EUR 5,000. No output DDV. Report on EC Sales List (RP-O).

### Test 5 -- Small business, purchase [T1]
**Input:** Small business (under EUR 60,000) purchases supplies EUR 1,220 including DDV EUR 220.
**Expected output:** No DDV return entry. Small business cannot recover input DDV.

### Test 6 -- Non-EU software, reverse charge [T1]
**Input:** US supplier (Google), EUR 50/month, no VAT. Registered taxpayer.
**Expected output:** Field 21 = EUR 50, Field 22 = EUR 11 (22%). Field 35 = EUR 11. Net = zero.

### Test 7 -- Reduced rate domestic purchase [T1]
**Input:** Slovenian supplier, books EUR 109.50 gross, DDV EUR 9.50 (9.5%), net EUR 100.
**Expected output:** Field 31 += EUR 9.50. Fully recoverable.

### Test 8 -- Construction services (domestic RC) [T1]
**Input:** Slovenian subcontractor, renovation EUR 10,000. Both parties DDV registered.
**Expected output:** Buyer: Field 21 = EUR 10,000, Field 22 = EUR 2,200 (22%). Field 35 = EUR 2,200. Net = zero.

### Test 9 -- Flat-rate agriculture purchase [T1]
**Input:** Registered business buys vegetables from flat-rate farmer EUR 500.
**Expected output:** Pay EUR 500 + EUR 40 flat-rate compensation (8%). Field 36 += EUR 40.

### Test 10 -- Export of goods [T1]
**Input:** Slovenian company exports to US client EUR 8,000.
**Expected output:** Field 24 = EUR 8,000. No output DDV. Zero-rated.

### Test 11 -- Fuel for blocked vehicle [T1]
**Input:** Fuel EUR 80 + DDV EUR 17.60 (22%) for a blocked passenger car.
**Expected output:** Field 31 += EUR 0. DDV BLOCKED (follows vehicle rule). Full EUR 97.60 is cost.

### Test 12 -- Entertainment expense (blocked) [T1]
**Input:** Business dinner EUR 200 + DDV EUR 44 (22%). Client entertainment.
**Expected output:** Field 31 += EUR 0. DDV BLOCKED under Art. 66(1)(4). Full EUR 244 is cost.

---

## Step 17: Refund Process [T1]

| Feature | Detail | Legislation |
|---------|--------|-------------|
| Refund request | Filed via DDV-O Field 42 (excess/refund claim) | ZDDV-1 Art. 73 |
| Automatic refund | If excess DDV exists and no outstanding tax liabilities | ZDDV-1 Art. 73(1) |
| Refund timeline | Within 21 days for monthly filers; within 60 days for quarterly filers | ZDDV-1 Art. 73(2) |
| Carry forward | Credit can be carried forward to next period indefinitely | ZDDV-1 Art. 73(3) |
| Audit-conditioned | FURS may audit before releasing refund | ZDavP-2 Art. 129 |
| 8th Directive refund | EU businesses not established in SI | ZDDV-1 Art. 74 |
| 13th Directive refund | Non-EU businesses | ZDDV-1 Art. 74a |

---

## Step 18: Capital Goods Adjustment [T1]

**Legislation:** ZDDV-1 Art. 68-69.

| Type | Adjustment Period | Trigger | Legislation |
|------|-------------------|---------|-------------|
| Movable capital goods | 5 years from acquisition | Change in deductible proportion | Art. 68 |
| Immovable property | 20 years from acquisition or completion | Change in deductible proportion | Art. 69 |
| Change in use | From taxable to exempt (or vice versa) | Annual recalculation required | Art. 68(2) |
| Sale during adjustment | One-off adjustment required | Remaining period adjusted in year of sale | Art. 68(3) |
| Partial exemption change | New coefficient vs original coefficient | Difference > 10 percentage points triggers adjustment | Art. 68(4) |

---

## Step 19: Out of Scope -- Direct Tax (Reference Only) [T3]

This skill does not compute income tax. The following is reference information only. Escalate to qualified adviser.

- **Corporate income tax (davek od dohodkov pravnih oseb):** 22% on adjusted profit (ZDDPO-2)
- **Personal income tax:** Progressive 16% / 26% / 33% / 39% / 45% / 50%
- **Dividend tax:** 25% withholding (27.5% from 2023)
- **Social contributions:** employer ~16.1%, employee ~22.1%
- **Health insurance:** employer 6.56%, employee 6.36%
- **Local taxes:** Property tax (NUSZ), motor vehicle tax
- **Environmental contributions:** CO2 levy, packaging contributions
- **Tourism tax (turisticna taksa):** Charged by accommodation providers per guest per night

---

## PROHIBITIONS [T1]

- NEVER let AI guess VAT box -- it is 100% deterministic from facts
- NEVER apply reverse charge to out-of-scope categories (wages, dividends, bank charges)
- NEVER apply reverse charge to local consumption services abroad (hotel, restaurant, taxi)
- NEVER allow small business (exempt) clients to claim input DDV
- NEVER confuse zero-rated (exports/intra-EU, input DDV deductible) with exempt without credit (financial, input DDV NOT deductible)
- NEVER apply reverse charge when EU supplier charged local VAT > 0%
- NEVER allow input DDV deduction on passenger cars/motorcycles unless proven exception applies (Art. 66(1)(1))
- NEVER allow input DDV deduction on yachts/boats/aircraft unless proven business exception (Art. 66(1)(2-3))
- NEVER allow input DDV deduction on entertainment/representation (Art. 66(1)(4))
- NEVER ignore the new Record of Charged DDV / Record of DDV Deduction obligations from July 2025
- NEVER confuse flat-rate agriculture compensation (Field 36) with standard input DDV
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude

---

## Contribution Notes

This skill covers Slovenia's VAT system based on ZDDV-1 (Official Gazette RS 13/11 as amended). Key distinctive features include: the 22%/9.5%/5% three-tier rate structure, full blocking of passenger cars and entertainment, the flat-rate agriculture scheme (8% compensation), the new July 2025 record submission obligations (Record of Charged DDV and Record of DDV Deduction), domestic reverse charge for construction/waste/emissions, and quarterly filing for businesses under EUR 210,000. Validation by a qualified Slovenian davcni svetovalec or pooblasceni revizor is required before production use.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
