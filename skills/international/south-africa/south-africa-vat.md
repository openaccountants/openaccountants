---
name: south-africa-vat
description: Use this skill whenever asked to prepare, review, or create a South Africa VAT return (VAT201 form) or any VAT-related filing for a South African vendor. Trigger on phrases like "prepare VAT return", "do the VAT", "fill in VAT201", "create the return", "SARS eFiling", or any request involving South Africa VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete South Africa VAT classification rules, VAT201 field mappings, input tax deductibility rules, reverse charge (imported services) treatment, zero-rated and exempt supply lists, diesel refund scheme, second-hand goods notional input tax, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any South Africa VAT-related work.
---

# South Africa VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | South Africa |
| Jurisdiction Code | ZA |
| Primary Legislation | Value-Added Tax Act 89 of 1991 (VAT Act) |
| Supporting Legislation | Tax Administration Act 28 of 2011 (TAA); Customs and Excise Act 91 of 1964; VAT Regulations; SARS Binding General Rulings |
| Tax Authority | South African Revenue Service (SARS) |
| Filing Portal | https://www.sarsefiling.co.za (SARS eFiling) |
| Standard VAT Rate | 15% (Section 7(1)(a), VAT Act 89/1991) |
| Currency | South African Rand (ZAR) |
| Skill Version | 1.0 |
| Validated By | Deep research verification, April 2026 |
| Confidence Coverage | Tier 1: field assignment, rate application, zero-rating, exemptions, blocked input tax, derived calculations. Tier 2: apportionment, second-hand goods valuation, bakkie classification edge cases, diesel refund eligibility. Tier 3: complex group structures, rulings applications, cross-border e-commerce. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A registered tax practitioner must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to registered tax practitioner and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and VAT registration number** [T1] -- 10-digit number (format: 4XXXXXXXXX)
2. **Registration category** [T1] -- Category A (bi-monthly), Category B (monthly), Category C (six-monthly for farming), Category D (six-monthly), Category E (twelve-monthly for farming)
3. **VAT period** [T1] -- confirm the specific tax period dates (start/end month)
4. **Industry/sector** [T2] -- impacts input tax apportionment and diesel refund eligibility (e.g., farming, mining, fishing)
5. **Does the business make exempt supplies?** [T2] -- If yes, apportionment required (Section 17(1)); practitioner must confirm method
6. **Does the business deal in second-hand goods?** [T2] -- If yes, notional input tax under Section 20(8) applies
7. **Does the business import services?** [T1] -- If yes, reverse charge under Section 7(1)(c) applies
8. **Is the business registered for the Diesel Refund Scheme?** [T2] -- If yes, DN/DC numbers required
9. **Turnover band** [T1] -- determines filing category and whether monthly filing is mandatory (> ZAR 30 million per annum)
10. **Does the client operate in a Special Economic Zone (SEZ)?** [T2] -- impacts zero-rating under Section 12R of Income Tax Act read with VAT provisions

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until registration category and period are confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- **Output supply** (output VAT -- Section 7(1)(a)): taxable supply of goods or services by the vendor
- **Input acquisition** (input tax -- Section 16(3)): goods or services acquired for making taxable supplies
- **Out of scope:** Salaries/wages, PAYE, UIF contributions, SDL, dividends, loan repayments, donations, income tax payments = NEVER on VAT return
- **Legislation:** VAT Act 89/1991, Section 1 (definitions), Section 7 (imposition of tax)

### 1b. Determine Counterparty Location [T1]
- **Domestic (South Africa):** supplier/customer is in the Republic of South Africa
- **Export (outside RSA):** customer is outside South Africa -- potential zero-rating under Section 11
- **Import:** goods imported from outside RSA (VAT at customs under Section 7(1)(b)) or imported services (reverse charge under Section 7(1)(c))
- **BLNS countries (Botswana, Lesotho, Namibia, eSwatini):** part of Southern African Customs Union (SACU) but separate VAT jurisdictions. Exports to BLNS are zero-rated under Section 11(1)(a) with proof of export.
- **Legislation:** VAT Act 89/1991, Section 11 (zero-rating), Section 7(1)(b)-(c) (imports)

### 1c. Determine VAT Rate [T1]
- **15%** -- standard rate (Section 7(1)(a))
- **0%** -- zero-rated supplies (Section 11, Schedule 2 to the VAT Act)
- **Exempt** -- exempt supplies (Section 12, no input tax recovery)
- Calculate from amounts: `rate = vat_amount / net_amount * 100`
- Normalize: <= 1% = 0% (zero-rated or exempt); 13-17% = 15%
- **Legislation:** VAT Act 89/1991, Section 7(1)(a), Section 11, Section 12

### 1d. Determine Expense Category [T1]
- **Capital goods:** assets of a capital nature (no monetary threshold unlike Malta -- all capital assets qualify for input tax if used in taxable supplies)
- **Trading stock:** goods acquired for resale
- **Overheads/services:** all other business expenses
- **Mixed-use assets:** require apportionment under Section 17(1) [T2]
- **Legislation:** VAT Act 89/1991, Section 16(3), Section 17(1)

---

## Step 2: VAT201 Form Field Assignment [T1]

**Legislation:** VAT Act 89/1991, Section 28 (returns and payments); SARS VAT201 form guide.

The VAT201 return has the following structure:

### Section A -- Vendor Information
| Field | Description |
|-------|-------------|
| Field 1 | VAT registration number |
| Field 2 | Tax period (from/to dates) |
| Field 3 | Vendor trade name |

### Section B -- Output Tax (VAT Charged on Supplies)

| Field | Description | Rate | Classification |
|-------|-------------|------|----------------|
| Field 1 | Standard-rated local supplies | 15% | Local sales of goods/services |
| Field 1A | Capital goods output | 15% | Capital goods supplied |
| Field 2 | Zero-rated local supplies | 0% | Section 11(1) supplies (basic foodstuffs, diesel, illuminating paraffin, etc.) |
| Field 3 | Zero-rated exports | 0% | Section 11(1)(a)-(c) exports of goods |
| Field 4 | Exempt supplies | 0% (exempt) | Section 12 supplies (financial services, residential rent, etc.) |
| Field 4A | Change in use output (non-taxable to taxable) | 15% | Section 18(1) adjustments |
| Field 4B | Other adjustments (output) | Various | Output tax adjustments |
| Field 5 | **Total supplies** | -- | Sum: Field 1 + 1A + 2 + 3 + 4 + 4A + 4B |
| Field 6 | **Total output tax** | -- | VAT on Fields 1 + 1A + 4A + 4B at 15% |

### Section C -- Input Tax (VAT Claimed on Acquisitions)

| Field | Description | Rate | Classification |
|-------|-------------|------|----------------|
| Field 7 | Standard-rated local purchases | 15% | Capital + non-capital purchases from SA vendors |
| Field 8 | Capital goods acquired | 15% | Capital assets acquired for taxable use |
| Field 9 | Goods imported | 15% | VAT paid at customs (Section 7(1)(b)) |
| Field 10 | Input tax on imported services | 15% | Reverse charge (Section 7(1)(c), Section 14(1)) |
| Field 11 | Change in use input (taxable to non-taxable) | 15% | Section 18(4) adjustments |
| Field 12 | Other adjustments (input) | Various | Bad debts recovered, notional input tax (second-hand goods) |
| Field 13 | **Total acquisitions** | -- | Sum: Field 7 + 8 + 9 + 10 + 11 + 12 |
| Field 14 | **Total input tax** | -- | VAT on Fields 7 + 8 + 9 + 10 + 11 + 12 |

### Section D -- Tax Calculation

| Field | Description |
|-------|-------------|
| Field 15 | Output tax (from Field 6) |
| Field 16 | Input tax (from Field 14) |
| Field 17 | **VAT payable (if Field 15 > Field 16)** = Field 15 minus Field 16 |
| Field 18 | **VAT refundable (if Field 16 > Field 15)** = Field 16 minus Field 15 |
| Field 19 | Diesel refund amount (if applicable) |
| Field 20 | **Total payable / refundable** |

---

## Step 3: Classification Matrix -- Purchases [T1]

### Local Purchases (South African Supplier)

| VAT on Invoice | Category | VAT201 Field (Value) | VAT201 Field (Tax) | Input Tax Recovery |
|----------------|----------|---------------------|--------------------|--------------------|
| 15% | Non-capital overhead | Field 7 | Field 14 | Yes (subject to Sec 17) |
| 15% | Capital asset | Field 8 | Field 14 | Yes (subject to Sec 17) |
| 15% | Blocked category | Field 7 | -- | NO (Section 17(2)) |
| 0% | Zero-rated purchase | Field 7 | -- | No VAT to claim |
| No VAT (exempt supplier) | Any | -- | -- | No VAT to claim |
| No VAT (non-vendor) | Second-hand goods | Field 12 | Field 14 | Notional input [T2] |

### Imports (Goods from Outside RSA)

| Type | VAT201 Field (Value) | VAT201 Field (Tax) | Notes |
|------|---------------------|--------------------|----|
| Physical goods (customs VAT paid) | Field 9 | Field 14 | Claim based on customs bill of entry |
| Imported services (reverse charge) | Field 10 | Field 14 (and Field 6 output) | Self-assess at 15% under Section 7(1)(c) |

### Classification Matrix -- Sales [T1]

| Supply Type | Rate | VAT201 Field |
|-------------|------|-------------|
| Standard-rated local supply | 15% | Field 1 |
| Capital goods disposed of | 15% | Field 1A |
| Zero-rated local supply (foodstuffs, fuel, etc.) | 0% | Field 2 |
| Zero-rated export of goods | 0% | Field 3 |
| Zero-rated export of services | 0% | Field 3 |
| Exempt supply | Exempt | Field 4 |

---

## Step 4: VAT Rates and Rate Schedule [T1]

### Standard Rate

| Rate | Application | Legislation |
|------|-------------|-------------|
| 15% | All taxable supplies unless specifically zero-rated or exempt | Section 7(1)(a), VAT Act 89/1991 |

### Zero-Rated Supplies (Section 11, Part A: Goods) [T1]

**Legislation:** VAT Act 89/1991, Section 11(1); Schedule 2, Part A.

#### 19 Basic Foodstuffs (Section 11(1)(j), Schedule 2, Part B, Item 1-19)

| # | Item | Notes |
|---|------|-------|
| 1 | Brown bread (whole wheat or brown) | White bread is standard-rated |
| 2 | Maize meal | Including samp |
| 3 | Samp | Dried corn kernels |
| 4 | Mealie rice | Coarsely ground maize |
| 5 | Dried mealies | Whole dried maize kernels |
| 6 | Dried beans | All varieties |
| 7 | Lentils | All varieties |
| 8 | Pilchards/sardinella (tinned) | In tins/cans only |
| 9 | Milk powder blend | As defined in regulations |
| 10 | Dairy powder blend | As defined in regulations |
| 11 | Rice | All varieties |
| 12 | Vegetable cooking oil | Sunflower, canola, etc. |
| 13 | Brown wheaten meal | Not white flour |
| 14 | Eggs | Whole eggs in shell |
| 15 | Edible legumes and pulses | Canned or dried |
| 16 | Fruit | Canned in fruit juice only |
| 17 | Vegetables | Canned in water/brine only |
| 18 | Cake flour | Plain, not self-raising mixes |
| 19 | White bread flour | Bread flour specifically |

**IMPORTANT:** White bread, meat, chicken, fish (except tinned pilchards), fresh fruit, fresh vegetables, sugar, tea, coffee are all STANDARD-RATED at 15%. Only the 19 items above are zero-rated. [T1]

#### Other Zero-Rated Goods (Section 11(1)(a)-(i), (k)-(w))

| Category | Section | Description |
|----------|---------|-------------|
| Exports | Section 11(1)(a) | Goods exported to any country outside RSA (including BLNS) |
| Goods to foreign-going ships/aircraft | Section 11(1)(b) | Stores, fuel for international transport |
| International transport | Section 11(1)(c) | Transport of goods/passengers to/from RSA |
| Farming inputs | Section 11(1)(g) | Animal feed, seed, fertiliser, pesticides for farming |
| Fuel levy goods | Section 11(1)(k) | Petrol and diesel (subject to fuel levy instead) |
| Illuminating paraffin | Section 11(1)(l) | Domestic paraffin |
| Gold coins | Section 11(1)(m) | Krugerrand and other gold coins |
| Going concern | Section 11(1)(e) | Sale of business as going concern [T2] |
| Goods used in SEZ | Section 12R/11 | Special Economic Zone supplies [T2] |

### Zero-Rated Supplies (Section 11, Part B: Services) [T1]

| Category | Section | Description |
|----------|---------|-------------|
| Services to non-residents | Section 11(2)(l) | Services physically performed for non-residents (not connected to SA land/goods) |
| International transport | Section 11(2)(a) | Transport of passengers/goods internationally |
| Repairs to foreign-going ships/aircraft | Section 11(2)(b) | Ship/aircraft repair services |
| Services relating to exported goods | Section 11(2)(c) | Arranging export, handling, clearing |
| Services to SEZ enterprises | Section 12R | Subject to conditions [T2] |

### Exempt Supplies (Section 12) -- No Input Tax Recovery [T1]

**Legislation:** VAT Act 89/1991, Section 12.

| Category | Section | Description |
|----------|---------|-------------|
| Financial services | Section 12(a) | Interest, insurance premiums, forex dealing, share trading |
| Residential accommodation | Section 12(b) | Long-term residential rental (dwelling) |
| Non-international public transport | Section 12(c) | Bus, rail, minibus taxi (domestic routes) |
| Educational services | Section 12(h) | Schools, universities, registered training |
| Childcare services | Section 12(i) | Creche, after-school care |
| Body corporates/share blocks | Section 12(d) | Levies by sectional title bodies |
| Employee organisations | Section 12(e) | Trade unions, employer organisations |
| Donated goods/services by PBOs | Section 12(b)(i) | Public Benefit Organisation donations |
| Supply of accommodation in a dwelling | Section 12(b) | Residential letting only; commercial/holiday accommodation is taxable |

**CRITICAL DISTINCTION [T1]:** Residential rental (exempt under Section 12(b)) vs. short-term/holiday accommodation (standard-rated at 15%). If rental period is typically less than 28 days and marketed as holiday accommodation, it is TAXABLE. If the dwelling is let for residential purposes, it is EXEMPT.

---

## Step 5: Blocked Input Tax (Section 17(2)) [T1]

**Legislation:** VAT Act 89/1991, Section 17(2).

The following input tax is BLOCKED and may NEVER be claimed, regardless of business use:

| Blocked Category | Section | Exception |
|------------------|---------|-----------|
| Entertainment | Section 17(2)(a) | UNLESS: (i) supplied to employees as taxable fringe benefit; (ii) vendor's main business is providing entertainment (hotel, restaurant, caterer, event organiser) |
| Motor cars | Section 17(2)(c) | UNLESS: (i) motor dealer acquiring for resale; (ii) car rental company; (iii) motor car used exclusively as a demo model by dealer. See bakkie classification rules below. |
| Club subscriptions | Section 17(2)(b) | No exception. Gym, golf club, social club -- always blocked |
| Non-taxable use | Section 17(1) | Portion used for exempt supplies or non-enterprise purposes |

### Motor Car vs. Bakkie Classification [T1/T2]

**Legislation:** VAT Act 89/1991, Section 1 (definition of "motor car").

A **"motor car"** is defined in Section 1 of the VAT Act as a motor vehicle designed primarily to carry passengers (9 or fewer including driver), with a gross vehicle mass (GVM) not exceeding 3,500 kg. Input tax on motor cars is BLOCKED under Section 17(2)(c).

**Exceptions -- NOT a "motor car" (input tax is claimable):** [T1]

| Vehicle Type | Why Not Blocked |
|--------------|-----------------|
| Double-cab bakkie with open load area > 1 tonne payload | Designed primarily to carry goods, not passengers |
| Single-cab bakkie | Designed primarily to carry goods |
| Truck (GVM > 3,500 kg) | Exceeds GVM threshold |
| Minibus (> 9 passengers) | Exceeds passenger limit |
| Motorcycle | Not a "motor car" per definition |
| Caravan/trailer | Not a motor vehicle |

**Double-cab bakkie classification:** [T2]
- If the open loading area is 1 metre or longer AND the vehicle has a payload capacity of 1 tonne or more, it is NOT a motor car -- input VAT is claimable.
- If the loading area is less than 1 metre or payload is under 1 tonne, it IS a motor car -- input VAT is BLOCKED.
- **Flag for reviewer: always confirm vehicle specifications from manufacturer data sheet before classifying a double-cab bakkie.**

---

## Step 6: Imported Services -- Reverse Charge Mechanics [T1]

**Legislation:** VAT Act 89/1991, Section 7(1)(c), Section 14(1).

When a South African vendor acquires services from a non-resident supplier who is not registered for VAT in South Africa:

1. The recipient vendor must self-assess output VAT at 15% on the value of the imported service.
2. The recipient vendor declares this in **Field 10** (imported services value) and the output tax portion in **Field 6**.
3. If the imported service is acquired for the purpose of making taxable supplies, the vendor may simultaneously claim input tax in **Field 14**.
4. Net effect for fully taxable vendors: zero (output = input).

### When Reverse Charge Applies [T1]

| Scenario | Reverse Charge? | Notes |
|----------|----------------|-------|
| SaaS subscription from US company (e.g., AWS, Google, Microsoft 365) | Yes | Section 7(1)(c) -- imported services |
| Legal/consulting services from UK firm | Yes | Section 7(1)(c) |
| Foreign supplier registered for SA VAT (e.g., Netflix, Spotify) | No | Supplier charges 15% -- claim as normal input tax |
| Physical goods imported | No | VAT paid to SARS Customs at border -- use Field 9 |
| Hotel/restaurant consumed abroad on business trip | No | Not a supply made in RSA |
| Royalties paid to non-resident | Yes | Section 7(1)(c) |
| Management fees from foreign parent company | Yes | Section 7(1)(c), but check transfer pricing [T3] |

### Non-Resident Supplier VAT Registration (Electronic Services)

**Legislation:** VAT Act 89/1991, Section 23(1A); Electronic Services Regulations (2019).

Non-resident suppliers of electronic services to South African consumers (B2C) must register for VAT once their supplies exceed ZAR 1,000,000 in any 12-month period. When they are registered, they charge 15% VAT directly. Common registered non-resident suppliers include Netflix, Spotify, Google, Apple, and Amazon. When a vendor receives an invoice from a registered non-resident supplier showing 15% SA VAT, treat it as a normal local purchase (Field 7), NOT as an imported service (Field 10). [T1]

---

## Step 7: Second-Hand Goods -- Notional Input Tax [T2]

**Legislation:** VAT Act 89/1991, Section 20(8); Section 16(2)(b).

When a VAT vendor acquires second-hand goods from a non-vendor (a person not registered for VAT):

1. The vendor may claim **notional input tax** equal to the tax fraction (15/115) of the purchase price.
2. This applies only if the goods are acquired for use in making taxable supplies.
3. The vendor must hold documentary proof: a statement by the seller (name, address, ID number, description of goods, consideration paid).
4. Report the notional input tax in **Field 12** (other adjustments -- input).

### Conditions [T2]
- The seller must be a **resident of South Africa** (or the goods must be situated in RSA).
- The goods must be **movable goods** (not fixed property -- fixed property from non-vendors requires transfer duty, not notional input).
- Fixed property acquired from a non-vendor: no notional input tax. Transfer duty paid instead [T1].
- The vendor must maintain a **declaration from the seller** per Section 20(8) requirements.
- **Flag for reviewer: confirm the purchase price reflects open market value. SARS may adjust if price is inflated to claim excessive notional input.**

---

## Step 8: Registration Thresholds and Categories [T1]

**Legislation:** VAT Act 89/1991, Section 23; Tax Administration Act 28 of 2011.

### Registration Thresholds

| Type | Threshold (current to 31 March 2026) | Threshold (from 1 April 2026) | Legislation |
|------|--------------------------------------|-------------------------------|-------------|
| Compulsory registration | ZAR 1,000,000 in any 12-month period | ZAR 2,300,000 in any 12-month period | Section 23(1) |
| Voluntary registration | ZAR 50,000 in any 12-month period | ZAR 120,000 in any 12-month period | Section 23(3) |

### Filing Categories [T1]

| Category | Period | Who Qualifies | Due Date |
|----------|--------|---------------|----------|
| Category A | Bi-monthly (two calendar months) | Standard -- most vendors | Last business day of the month following the end of the tax period |
| Category B | Monthly | Vendors with taxable supplies > ZAR 30 million per annum | Last business day of the month following the end of the tax period |
| Category C | Six-monthly (1 Mar - 31 Aug / 1 Sep - 28 Feb) | Farmers (by application) | Last business day of the month following the end of the tax period |
| Category D | Six-monthly (1 Apr - 30 Sep / 1 Oct - 31 Mar) | Small vendors (by application, turnover < ZAR 1.5 million) | Last business day of the month following the end of the tax period |
| Category E | Twelve-monthly (1 Mar - 28 Feb) | Farmers (by application) | Last business day of the month following the end of the tax period |
| Category F | Bi-monthly (aligned differently) | Specific sectors (by SARS assignment) | Last business day of the month following the end of the tax period |

### Category A Bi-Monthly Periods [T1]

| Period | Months | Return Due |
|--------|--------|------------|
| Period 1 | January - February | Last business day of March |
| Period 2 | March - April | Last business day of May |
| Period 3 | May - June | Last business day of July |
| Period 4 | July - August | Last business day of September |
| Period 5 | September - October | Last business day of November |
| Period 6 | November - December | Last business day of January |

---

## Step 9: Filing, Payment, and Penalties [T1]

**Legislation:** VAT Act 89/1991, Section 28; Tax Administration Act 28 of 2011, Sections 210-223.

### Filing Method [T1]
- **eFiling:** Submit VAT201 via SARS eFiling portal (https://www.sarsefiling.co.za). This is the standard method.
- **SARS branch:** Physical filing only in exceptional circumstances (SARS is phasing out branch submissions).

### Payment Deadlines [T1]
- Payment is due on the same date as the return: **last business day of the month following the tax period end**.
- Electronic payments (EFT): must clear into SARS bank account by the due date.
- Payments at bank: must be made by the due date.

### Penalties [T1]

| Penalty Type | Rate/Amount | Legislation |
|--------------|-------------|-------------|
| Late payment penalty | 10% of unpaid tax | Section 213, TAA |
| Late filing penalty (administrative non-compliance) | Fixed penalty based on assessed taxable income bracket: ZAR 250 to ZAR 16,000 per month, up to 35 months | Section 210-211, TAA |
| Understatement penalty | 10% to 200% of the shortfall, depending on behaviour (substantial understatement, reasonable care not taken, gross negligence, intentional tax evasion) | Section 222-223, TAA |
| Interest on late payment | Prescribed rate (currently linked to repo rate + 4.25%) compounded monthly | Section 187, TAA |
| Failure to register | Criminal offence; fine or imprisonment up to 2 years | Section 234, TAA |

### Refund Verification [T1]
- Refunds (Field 18 > 0) are subject to SARS verification/audit before payment.
- SARS has 21 business days to pay a verified refund (Section 190, TAA).
- Refund claims in excess of normal patterns will trigger a desk audit. Maintain all supporting documents. [T2]

---

## Step 10: Derived Field Calculations [T1]

```
Field 5  = Field 1 + Field 1A + Field 2 + Field 3 + Field 4 + Field 4A + Field 4B
               (Total value of supplies)

Field 6  = VAT on (Field 1 + Field 1A + Field 4A + Field 4B) at 15%
               (Total output tax)
           NOTE: Add imported services output tax (from Field 10 self-assessment)

Field 13 = Field 7 + Field 8 + Field 9 + Field 10 + Field 11 + Field 12
               (Total value of acquisitions)

Field 14 = Input tax on Fields 7 + 8 + 9 + 10 + 11 + 12
               (Total input tax, subject to apportionment and blocked categories)

IF Field 6 > Field 14 THEN
  Field 17 = Field 6 - Field 14        -- VAT payable to SARS
  Field 18 = 0
ELSE
  Field 17 = 0
  Field 18 = Field 14 - Field 6        -- VAT refundable from SARS
END

Field 20 = Field 17 - Field 18 - Field 19 (diesel refund)
               (Net amount payable / refundable)
```

---

## Step 11: Input Tax Apportionment (Section 17(1)) [T2]

**Legislation:** VAT Act 89/1991, Section 17(1); SARS Interpretation Note No. 39.

If a vendor makes BOTH taxable and exempt supplies, input tax must be apportioned:

### Standard Turnover-Based Method [T2]

```
Recovery % = (Taxable Supplies / Total Supplies) * 100
```

- Apply to all input tax that is not directly attributable to either taxable or exempt supplies.
- Directly attributable input tax: allocate 100% to the relevant supply category.
- Annual adjustment required at year-end (Section 17(1)(c)).

### Alternative Methods [T3]
- Floor area method, transaction count method, or other methods require prior written approval from SARS Commissioner.
- **Escalate to practitioner if alternative method is used or requested.**

**Flag for reviewer: apportionment ratio must be confirmed by registered tax practitioner before applying. Annual wash-up adjustment is mandatory.**

---

## Step 12: Diesel Refund Scheme [T2]

**Legislation:** VAT Act 89/1991, Section 16(3)(o); Customs and Excise Act 91 of 1964, Schedule 6 Part 3.

### Eligible Industries [T2]
- Primary production: farming, forestry, mining, fishing
- Vendor must be registered for the Diesel Refund Scheme with SARS (separate from VAT registration)
- Must hold a valid Customs and Excise registration (DA 185)

### How It Works [T2]
1. Eligible vendors purchase diesel at the pump, paying the full pump price (which includes the general fuel levy and Road Accident Fund levy).
2. A portion of the fuel levies is refundable via the VAT return in **Field 19**.
3. The refund rate is published by SARS and adjusted periodically (currently approximately ZAR 3.93 per litre for farming; ZAR 1.50 per litre for mining -- confirm current rates with SARS).
4. The vendor must maintain detailed records: litres purchased, purpose, logbooks.
5. SARS conducts regular audits of diesel refund claims.

### Documentation Required [T1]
- Tax invoices from fuel supplier
- Logbook or GPS records proving use in qualifying activities
- DN (Delivery Note) or DC (Diesel Card) numbers
- Customs registration certificate (DA 185)

**Flag for reviewer: diesel refund claims are high-audit-risk. Ensure all documentation is complete before filing.**

---

## Step 13: Edge Case Registry

These are known ambiguous situations and their confirmed resolutions. Each is tagged with its confidence tier.

### EC1 -- Zero-Rated Foodstuffs: Brown Bread vs White Bread [T1]
**Situation:** Client sells both brown bread and white bread.
**Resolution:** Brown bread (whole wheat bread, brown bread as defined in the Foodstuffs, Cosmetics and Disinfectants Act) is zero-rated under Section 11(1)(j), Schedule 2, Part B. White bread is STANDARD-RATED at 15%. The distinction is based on the flour composition per the regulatory definition. If bread contains at least 50% brown/whole wheat flour, it qualifies as brown bread.
**Legislation:** VAT Act 89/1991, Section 11(1)(j); Regulation R.2687 (definition of brown bread).

### EC2 -- Bakkie Double-Cab Classification [T2]
**Situation:** Client purchases a double-cab bakkie (e.g., Toyota Hilux 2.8 GD-6 double cab) and claims input VAT.
**Resolution:** Check: (1) Does the open load area measure 1 metre or more in length? (2) Does the vehicle have a payload of 1 tonne (1,000 kg) or more? If BOTH conditions are met, the vehicle is NOT a "motor car" under Section 1, and input tax is deductible. If either condition fails, it IS a motor car and input tax is BLOCKED. Most standard double-cab bakkies (Hilux, Ranger, Amarok) with the longer bed option meet both criteria, but luxury/sport variants with shorter beds may not.
**Flag for reviewer: obtain vehicle specification sheet from manufacturer. Do not rely on client's verbal confirmation.**
**Legislation:** VAT Act 89/1991, Section 1 (definition of "motor car"); Section 17(2)(c).

### EC3 -- SaaS Subscription from Foreign Provider (Already SA VAT Registered) [T1]
**Situation:** Client pays for Microsoft 365 subscription. Microsoft is registered for SA VAT and charges 15%.
**Resolution:** Treat as a NORMAL local purchase. Input tax is claimable in Field 7 / Field 14. Do NOT apply reverse charge. Microsoft, Google, Netflix, Spotify, Apple, Amazon, and other major digital platforms are registered for SA VAT under the Electronic Services Regulations.
**Legislation:** VAT Act 89/1991, Section 23(1A); Electronic Services Regulations (2019).

### EC4 -- SaaS Subscription from Non-Registered Foreign Provider [T1]
**Situation:** Client pays for a niche cloud service from a US-based startup that is NOT registered for SA VAT. Invoice shows no VAT.
**Resolution:** Reverse charge applies. Self-assess output VAT at 15% (Field 10 / Field 6). If acquired for taxable purposes, claim input tax (Field 14). Net effect: zero for fully taxable vendor.
**Legislation:** VAT Act 89/1991, Section 7(1)(c); Section 14(1).

### EC5 -- Second-Hand Motor Vehicle from Private Individual [T2]
**Situation:** Motor dealer (VAT vendor) purchases a used car from a private individual (non-vendor) for ZAR 150,000.
**Resolution:** Motor dealer may claim notional input tax: ZAR 150,000 x 15/115 = ZAR 19,565.22. Claimed in Field 12. Requires a signed declaration from the seller with full details (name, ID number, address, vehicle description, VIN, consideration). Private individual does NOT charge VAT. The dealer is not subject to the motor car input block because the dealer acquires the car for resale (Section 17(2)(c) exception for motor dealers).
**Legislation:** VAT Act 89/1991, Section 20(8); Section 16(2)(b); Section 17(2)(c)(i).

### EC6 -- Entertainment by a Hotel/Restaurant Business [T1]
**Situation:** A hotel claims input tax on food and beverages served to guests.
**Resolution:** Entertainment block under Section 17(2)(a) does NOT apply to vendors whose main business is providing entertainment, accommodation, or catering. A hotel, restaurant, or catering company may claim input tax on food, beverages, and entertainment supplies used in its business operations.
**Legislation:** VAT Act 89/1991, Section 17(2)(a) proviso (iii).

### EC7 -- Sale of Fixed Property (Commercial) [T1]
**Situation:** Vendor sells a commercial building for ZAR 5,000,000.
**Resolution:** Sale of commercial fixed property by a VAT vendor is a TAXABLE supply at 15%. Output VAT = ZAR 5,000,000 x 15% = ZAR 750,000. Report in Field 1A (capital goods output). Buyer claims input tax if acquiring for taxable purposes. Transfer duty is NOT payable when VAT is charged (Transfer Duty Act, Section 9(15)).
**Legislation:** VAT Act 89/1991, Section 7(1)(a); Transfer Duty Act 40 of 1949, Section 9(15).

### EC8 -- Sale of Fixed Property as a Going Concern [T2]
**Situation:** Vendor sells a tenanted commercial property as a going concern to another VAT vendor.
**Resolution:** Zero-rated at 0% under Section 11(1)(e) if ALL conditions are met: (1) seller and buyer are both VAT-registered vendors; (2) the enterprise is sold as a going concern (with existing lease agreements, employees, etc.); (3) a written agreement between parties confirms going concern treatment; (4) the enterprise or part thereof is an income-earning activity that will continue to operate. If any condition is not met, 15% VAT applies.
**Flag for reviewer: going concern zero-rating is frequently disputed by SARS. All conditions must be documented in the sale agreement. Legal review recommended.**
**Legislation:** VAT Act 89/1991, Section 11(1)(e); SARS Interpretation Note No. 57.

### EC9 -- Bad Debt Relief [T1]
**Situation:** Vendor issued a tax invoice 12 months ago for ZAR 115,000 (including ZAR 15,000 VAT). The debtor has not paid and the debt has been written off.
**Resolution:** The vendor may claim a deduction (input tax adjustment) for the VAT portion of the bad debt under Section 22(1). Requirements: (1) the debt must have been outstanding for at least 12 months from the date the supply was made; OR the debtor has been placed under sequestration/liquidation; (2) the debt must have been written off in the vendor's books. Claim ZAR 15,000 in Field 12. If the debtor later pays, output adjustment is required (Field 4B).
**Legislation:** VAT Act 89/1991, Section 22(1) (bad debt deduction); Section 22(3) (recovery of bad debts).

### EC10 -- Credit Notes [T1]
**Situation:** Vendor issues a credit note to a customer for returned goods.
**Resolution:** Reduce output tax in the period the credit note is issued. Net the credit note against Field 1 (reduce the value of standard-rated supplies). Reduce Field 6 (output tax) accordingly. Do NOT create a separate negative entry. Credit notes must comply with Section 21(3) requirements (reference original invoice number, reason for credit, VAT amount adjusted).
**Legislation:** VAT Act 89/1991, Section 21(3) (credit and debit notes).

### EC11 -- Promotional Gifts / Samples [T1]
**Situation:** Vendor gives away free product samples worth ZAR 50 each to potential customers.
**Resolution:** If the supply is made in the course of the vendor's enterprise and the total value of gifts to any one person does not exceed ZAR 100 in any 12-month period, no output VAT is due (de minimis rule). If gifts exceed ZAR 100 to a single recipient, output VAT must be accounted for at 15% on the open market value. Input tax on the purchase of promotional goods is deductible (not entertainment).
**Legislation:** VAT Act 89/1991, Section 18(3); SARS Interpretation Note No. 70.

### EC12 -- Farming: Zero-Rated Inputs [T1]
**Situation:** Farmer purchases animal feed, seeds, and fertiliser for farming operations.
**Resolution:** These are zero-rated under Section 11(1)(g) when supplied to a person who will use them for farming purposes. The farmer is charged 0% VAT on these inputs. No input VAT to claim (price already excludes VAT), but the supply counts toward the farmer's taxable (zero-rated) turnover for registration purposes.
**Legislation:** VAT Act 89/1991, Section 11(1)(g); Schedule 2, Part A, paragraph 2.

### EC13 -- Residential Rental vs Short-Term Accommodation [T1]
**Situation:** Property owner rents a furnished apartment on Airbnb for periods averaging 5-7 days.
**Resolution:** Short-term accommodation (less than 28 consecutive days, marketed as holiday/guest accommodation) is a TAXABLE supply at 15%. The property owner must register for VAT if turnover exceeds ZAR 1,000,000 (or ZAR 2,300,000 from 1 April 2026). Long-term residential rental (dwelling rented for residential purposes) is EXEMPT under Section 12(b). The key test is: is it a dwelling let for residential occupation, or is it commercial accommodation?
**Legislation:** VAT Act 89/1991, Section 12(b) (exempt dwelling); Section 1 (definition of "dwelling"); Section 7 (taxable supply).

### EC14 -- Mixed-Use Vehicle (Partial Business, Partial Private) [T2]
**Situation:** Sole proprietor uses a single-cab bakkie 60% for business and 40% for private purposes.
**Resolution:** Single-cab bakkie is NOT a "motor car" so input tax is not blocked. However, Section 17(1) requires apportionment for non-enterprise (private) use. Claim 60% of input VAT. The apportionment percentage must be supportable with a logbook. Output VAT adjustment may be required under Section 18(1) for the private-use portion.
**Flag for reviewer: confirm apportionment percentage. SARS may challenge without logbook evidence.**
**Legislation:** VAT Act 89/1991, Section 17(1); Section 18(1).

### EC15 -- Import of Goods: Customs VAT vs Reverse Charge [T1]
**Situation:** Client imports physical goods from China.
**Resolution:** VAT on imported goods is paid to SARS Customs at the border under Section 7(1)(b), NOT via reverse charge on the VAT return. The customs bill of entry is the tax invoice equivalent. Report the VAT paid in Field 9 (imported goods) and claim input tax in Field 14. This is different from imported SERVICES which use the reverse charge (Field 10).
**Legislation:** VAT Act 89/1991, Section 7(1)(b) (imported goods); Customs and Excise Act 91 of 1964.

### EC16 -- Vegetable Cooking Oil: Zero-Rated vs Standard-Rated [T1]
**Situation:** Retailer sells both sunflower cooking oil and olive oil.
**Resolution:** Vegetable cooking oil (sunflower, canola, soya) is zero-rated under Schedule 2, Part B, item 12. Olive oil is NOT included in the definition of "vegetable cooking oil" for zero-rating purposes -- it is STANDARD-RATED at 15%. Blended oils must be checked against the regulatory definition.
**Legislation:** VAT Act 89/1991, Section 11(1)(j); Schedule 2, Part B; SARS BGR 57.

### EC17 -- Vendor Deregistration and Closing Stock [T1]
**Situation:** Vendor deregisters from VAT. Has trading stock and capital assets on hand.
**Resolution:** Under Section 8(2), the vendor is deemed to have made a supply of all goods on hand at open market value on the date of deregistration. Output VAT at 15% must be accounted for on the final VAT201 return. This includes trading stock, capital assets, and any other goods forming part of the enterprise. The final return is filed for the period ending on the deregistration date.
**Legislation:** VAT Act 89/1991, Section 8(2); Section 24(5).

### EC18 -- Petrol and Diesel: Fuel Levy vs VAT [T1]
**Situation:** Vendor purchases petrol for company vehicles.
**Resolution:** Petrol and diesel are zero-rated for VAT purposes under Section 11(1)(k) because they are subject to the general fuel levy under the Customs and Excise Act. This means there is NO VAT on fuel purchases at the pump. The vendor cannot claim input VAT on fuel because none was charged. The diesel refund scheme (Step 12) is a separate mechanism relating to fuel LEVIES, not VAT. Do not confuse the two.
**Legislation:** VAT Act 89/1991, Section 11(1)(k); Customs and Excise Act 91/1964, Schedule 1 Part 5A.

### EC19 -- Tokens, Vouchers, and Gift Cards [T2]
**Situation:** Retailer sells gift cards/vouchers redeemable at its stores.
**Resolution:** The sale of a single-purpose voucher (redeemable for a specific identified supply) is treated as a supply at the time the voucher is issued -- output VAT is due at issuance. The sale of a multi-purpose voucher (redeemable for different types of supplies) is NOT a supply at issuance -- output VAT is due only when the voucher is redeemed. Determine voucher type before classifying.
**Flag for reviewer: confirm whether voucher is single-purpose or multi-purpose. Classification affects timing of output VAT.**
**Legislation:** VAT Act 89/1991, Section 10(19)-(20).

---

## Step 14: Comparison with EU VAT System

| Feature | South Africa | EU (Standard Model) |
|---------|-------------|---------------------|
| Standard rate | 15% (single rate) | Varies by member state (17%-27%) |
| Reduced rates | None (only 0% and exempt) | One or more reduced rates per member state (5%-13% typically) |
| Zero-rating | Extensive: 19 basic foodstuffs, exports, fuel, farming inputs | Limited: mainly exports; some member states zero-rate specific items (e.g., UK zero-rates food generally) |
| Exempt supplies | Financial services, residential rental, domestic transport, education | Similar categories; financial services exempt in most member states |
| Reverse charge (imports) | Section 7(1)(c) for services only; goods pay VAT at customs | EU uses reverse charge for intra-community acquisitions (goods and services B2B) |
| Intra-community supplies | N/A (no equivalent trade bloc) | Zero-rated intra-community supply to VAT-registered buyer in another member state |
| Registration threshold | ZAR 1,000,000 (~EUR 50,000) -- increasing to ZAR 2,300,000 (~EUR 115,000) from April 2026 | Varies: EUR 0 (Spain) to EUR 85,000 (UK historical); EU small business scheme harmonising at EUR 85,000 |
| Filing frequency | Bi-monthly (standard), monthly (> ZAR 30M), six-monthly/annual (farming) | Varies by member state: monthly, quarterly, annually |
| Return form | VAT201 (20 fields, single-page) | Varies by member state; typically more complex (e.g., Malta VAT3 has 45+ boxes) |
| Input tax block -- entertainment | Blocked (except hospitality businesses) | Varies by member state; Malta blocks under 10th Schedule |
| Input tax block -- motor cars | Blocked (except dealers/rental) | Varies; Malta blocks under 10th Schedule |
| Second-hand goods scheme | Notional input tax (15/115 of price) | Margin scheme (VAT on margin only) -- different mechanism |
| Capital goods scheme | No formal multi-year adjustment scheme like EU | EU requires 5-year (movable) or 10-20 year (immovable) adjustment |
| Invoice requirements | Tax invoice per Section 20; simplified invoice for < ZAR 5,000 | Per EU VAT Directive; thresholds vary by member state |
| Digital services by non-residents | Must register once exceeding ZAR 1M; Electronic Services Regulations | OSS/IOSS system for non-EU digital service providers |
| Diesel/fuel refund | Diesel refund scheme for farmers/miners via VAT return | No equivalent; EU member states handle fuel differently |

---

## Step 15: Tax Invoice Requirements [T1]

**Legislation:** VAT Act 89/1991, Section 20.

### Full Tax Invoice (Supply >= ZAR 5,000) [T1]

| Required Element | Section |
|-----------------|---------|
| Words "Tax Invoice" prominently displayed | Section 20(4)(a) |
| Vendor's name, address, and VAT number | Section 20(4)(b) |
| Recipient's name, address, and VAT number (if registered) | Section 20(4)(c) |
| Serial number and date of issue | Section 20(4)(d) |
| Description of goods or services | Section 20(4)(e) |
| Quantity or volume | Section 20(4)(e) |
| Value of supply (excluding VAT) | Section 20(4)(f) |
| VAT amount charged | Section 20(4)(f) |
| Consideration for the supply (VAT-inclusive) | Section 20(4)(f) |

### Abridged Tax Invoice (Supply < ZAR 5,000) [T1]

| Required Element | Section |
|-----------------|---------|
| Words "Tax Invoice" | Section 20(5)(a) |
| Vendor's name, address, and VAT number | Section 20(5)(b) |
| Serial number and date | Section 20(5)(c) |
| Description of goods/services | Section 20(5)(d) |
| VAT-inclusive consideration | Section 20(5)(e) |
| Statement that VAT is included (or show rate) | Section 20(5)(e) |

**No input tax may be claimed without a valid tax invoice. [T1]**

---

## Step 16: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Registered tax practitioner must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to registered tax practitioner. Document gap.
```

---

## Step 17: Test Suite

These reference transactions have known correct outputs. Use to validate skill execution.

### Test 1 -- Standard Local Purchase, 15% VAT Overhead [T1]
**Input:** South African supplier, office stationery, gross ZAR 1,150, VAT ZAR 150, net ZAR 1,000, not resale, not capital, fully taxable vendor.
**Expected output:** Field 7 = ZAR 1,000, Field 14 includes ZAR 150. Input VAT recoverable in full.

### Test 2 -- Capital Asset Purchase [T1]
**Input:** South African supplier, new computer server, gross ZAR 57,500, VAT ZAR 7,500, net ZAR 50,000, capital asset, fully taxable vendor.
**Expected output:** Field 8 = ZAR 50,000, Field 14 includes ZAR 7,500. Input VAT recoverable in full.

### Test 3 -- Imported Services, Reverse Charge [T1]
**Input:** US-based SaaS provider (not registered for SA VAT), monthly subscription USD 500 (~ZAR 9,000), no VAT on invoice, fully taxable vendor.
**Expected output:** Field 10 = ZAR 9,000. Output tax self-assessed: ZAR 9,000 x 15% = ZAR 1,350 (added to Field 6). Input tax: ZAR 1,350 (added to Field 14). Net VAT effect = zero.

### Test 4 -- Blocked Input Tax: Motor Car [T1]
**Input:** Fully taxable vendor (not a motor dealer) purchases a passenger sedan, gross ZAR 460,000, VAT ZAR 60,000, net ZAR 400,000.
**Expected output:** Field 7 = ZAR 400,000 (value recorded). Field 14 = ZAR 0 from this transaction. VAT BLOCKED under Section 17(2)(c). No input tax recovery.

### Test 5 -- Blocked Input Tax: Entertainment [T1]
**Input:** Consulting firm takes clients to dinner, gross ZAR 5,750, VAT ZAR 750, net ZAR 5,000.
**Expected output:** Field 7 = ZAR 5,000 (value recorded). Field 14 = ZAR 0 from this transaction. VAT BLOCKED under Section 17(2)(a). Consulting firm is not in the hospitality business, so no exception applies.

### Test 6 -- Zero-Rated Export [T1]
**Input:** Vendor exports manufactured goods to Namibia, invoice ZAR 200,000, 0% VAT. Proof of export (bill of lading) held.
**Expected output:** Field 3 = ZAR 200,000. Output tax = ZAR 0. All input tax on costs of producing these goods is fully deductible.

### Test 7 -- Zero-Rated Basic Foodstuff Sale [T1]
**Input:** Retailer sells brown bread, rice, and eggs. Total sales: ZAR 50,000.
**Expected output:** Field 2 = ZAR 50,000. Output tax = ZAR 0. Input tax on costs attributable to these sales is fully deductible.

### Test 8 -- Exempt Supply: Residential Rental [T1]
**Input:** Property owner rents a flat to a tenant for long-term residential use. Monthly rent: ZAR 12,000.
**Expected output:** Field 4 = ZAR 12,000. Output tax = ZAR 0. NO input tax recovery on expenses attributable to this exempt supply.

### Test 9 -- Second-Hand Goods from Non-Vendor [T2]
**Input:** Motor dealer (VAT vendor) purchases used vehicle from private individual for ZAR 230,000. Seller declaration obtained.
**Expected output:** Notional input tax = ZAR 230,000 x 15/115 = ZAR 30,000. Field 12 = ZAR 230,000 (value). Field 14 includes ZAR 30,000 (notional input). Motor dealer exception to Section 17(2)(c) applies -- not blocked.

### Test 10 -- Double-Cab Bakkie (Qualifying) [T2]
**Input:** Construction company purchases Toyota Hilux 2.8 GD-6 double cab (load bed > 1m, payload > 1 tonne). Gross ZAR 690,000, VAT ZAR 90,000, net ZAR 600,000. Used 100% for business.
**Expected output:** Vehicle is NOT a "motor car" per Section 1 definition. Field 8 = ZAR 600,000 (capital asset). Field 14 includes ZAR 90,000. Input VAT recoverable in full. Flag for reviewer: confirm vehicle specifications from manufacturer data sheet.

### Test 11 -- Bad Debt Relief [T1]
**Input:** Vendor wrote off a debt of ZAR 115,000 (ZAR 100,000 net + ZAR 15,000 VAT) after 14 months. Original tax invoice issued and output VAT was declared.
**Expected output:** Field 12 adjustment = ZAR 15,000 (input tax claim). Debt is over 12 months old and written off in books. Section 22(1) conditions met.

### Test 12 -- Diesel Refund: Farmer [T2]
**Input:** Registered farmer purchases 5,000 litres of diesel at ZAR 24.50/litre. Farmer is registered for diesel refund scheme. Current refund rate: ZAR 3.93/litre.
**Expected output:** Diesel refund = 5,000 x ZAR 3.93 = ZAR 19,650. Report in Field 19. All documentation (fuel slips, logbook) must be retained. Flag for reviewer: confirm current refund rate with SARS and verify logbook records.

---

## PROHIBITIONS [T1]

- **NEVER** let AI guess VAT201 field assignment -- it is deterministic from the transaction facts
- **NEVER** classify white bread, meat, chicken, fresh fruit, fresh vegetables, sugar, tea, or coffee as zero-rated -- only the 19 listed basic foodstuffs are zero-rated
- **NEVER** allow input tax recovery on motor cars unless the vendor is a motor dealer (resale), car rental company, or the vehicle qualifies as NOT a motor car (bakkie/truck per specifications)
- **NEVER** allow input tax recovery on entertainment unless the vendor's main business is hospitality (hotel, restaurant, caterer, event organiser)
- **NEVER** allow input tax recovery on club subscriptions under any circumstances
- **NEVER** apply reverse charge to imported physical goods -- goods pay VAT at customs (Field 9), not via reverse charge (Field 10)
- **NEVER** apply reverse charge when the foreign supplier is already registered for SA VAT and has charged 15%
- **NEVER** claim input tax without a valid tax invoice (or customs bill of entry for imports, or seller declaration for second-hand goods)
- **NEVER** confuse zero-rated (0% with input tax recovery) with exempt (no input tax recovery) -- these are fundamentally different
- **NEVER** file a VAT return without confirming the vendor's filing category and period
- **NEVER** claim diesel refund without confirmed registration on the Diesel Refund Scheme and supporting documentation
- **NEVER** claim notional input tax on second-hand goods without a signed seller declaration meeting Section 20(8) requirements
- **NEVER** zero-rate an export without proof of export documentation (bill of lading, airway bill, or equivalent)
- **NEVER** compute any number -- all arithmetic is handled by the deterministic engine, not Claude
- **NEVER** assume a double-cab bakkie qualifies for input tax without verifying load bed length (>= 1m) and payload (>= 1 tonne) from manufacturer specifications

---

## Contribution Notes (For Adaptation to Other Jurisdictions)

If you are adapting this skill for another country, you must:

1. Replace all legislation references with the equivalent national legislation.
2. Replace all VAT201 field numbers with the equivalent fields on your jurisdiction's VAT return form.
3. Replace VAT rates with your jurisdiction's standard, reduced, and zero rates.
4. Replace the registration threshold (ZAR 1,000,000 / ZAR 2,300,000) with your jurisdiction's equivalent.
5. Replace the zero-rated foodstuffs list with your jurisdiction's equivalent (if any).
6. Replace the blocked categories with your jurisdiction's equivalent non-deductible categories.
7. Replace the diesel refund scheme with your jurisdiction's equivalent fuel rebate/refund (if any).
8. Replace the second-hand goods notional input tax rules with your jurisdiction's equivalent (e.g., EU margin scheme).
9. Have a registered tax practitioner in your jurisdiction validate every T1 rule before publishing.
10. Add your own edge cases to the Edge Case Registry for known ambiguous situations in your jurisdiction.
11. Run all test suite cases against your jurisdiction's rules and replace expected outputs accordingly.

**A skill may not be published without sign-off from a registered practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
