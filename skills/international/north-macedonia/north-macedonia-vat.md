---
name: north-macedonia-vat
description: Use this skill whenever asked to prepare, review, or advise on a North Macedonia VAT (DDV) return or any transaction classification for Macedonian VAT purposes. Trigger on phrases like "Macedonia VAT", "North Macedonia VAT", "DDV", "PRO filing", "Macedonian tax", or any request involving North Macedonian VAT obligations. This skill contains the complete DDV classification rules, rate structure (18% standard, 10% food services, 5% reduced, 0% basic foodstuffs), return form mappings, deductibility rules, reverse charge treatment, and filing deadlines. ALWAYS read this skill before touching any North Macedonian VAT-related work.
---

# North Macedonia VAT (DDV) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Republic of North Macedonia |
| Jurisdiction Code | MK |
| Tax Name | DDV (Danok na Dodadena Vrednost / VAT) |
| Primary Legislation | Law on Value Added Tax (Zakon za Danok na Dodadena Vrednost), Official Gazette No. 44/1999 (as amended) |
| Supporting Legislation | Rulebook on DDV implementation; Customs Law; Law on Excise Duties |
| Tax Authority | Public Revenue Office (PRO -- Upravata za Javni Prihodi / UJP) |
| Filing Portal | https://e-ujp.ujp.gov.mk (e-Taxes portal) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by licensed Macedonian tax practitioner |
| Validation Date | April 2026 (web-verified; practitioner sign-off still pending) |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: rate application, standard classification, basic input deductions. Tier 2: partial deduction, EU accession impact, special schemes. Tier 3: transfer pricing, complex group structures. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified tax practitioner must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified practitioner and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and EDB (Identification Number for DDV)** [T1]
2. **DDV registration status** [T1] -- registered DDV payer or non-registered (small enterprise)
3. **DDV period** [T1] -- monthly (turnover > MKD 25,000,000) or quarterly (turnover <= MKD 25,000,000)
4. **Industry/sector** [T2] -- impacts exemptions and reduced rate eligibility
5. **Does the business make exempt supplies?** [T2] -- partial deduction rules apply
6. **Does the business trade cross-border?** [T1] -- impacts import/export treatment
7. **Accumulated DDV credit** [T1] -- from prior periods
8. **Is the business in a technological industrial development zone (TIDZ)?** [T2] -- special DDV incentives

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until registration status and period are confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output DDV) or Purchase (input DDV)
- Salaries, social contributions, dividends, loan repayments = OUT OF SCOPE
- **Legislation:** Law on DDV, Article 2-3 (taxable supply)

### 1b. Determine Counterparty Location [T1]
- North Macedonia (domestic): supplier/customer registered in MK
- EU: all 27 EU member states (MK is not yet an EU member; EU accession negotiations ongoing)
- CEFTA: Serbia, Bosnia, Montenegro, Kosovo, Albania, Moldova (CEFTA trade agreement)
- Other foreign: all remaining countries

### 1c. Determine DDV Rate [T1]

| Rate | Application | Legislation |
|------|-------------|-------------|
| 18% | Standard rate -- most goods and services | Article 29(1) |
| 10% | Reduced rate -- food/beverage services for immediate consumption (excl. alcohol) | Article 29, as amended |
| 5% | Reduced rate -- specific categories (see below) | Article 29(2) |
| 0% | Zero rate -- exports of goods, international transport; also basic foodstuffs (bread, flour, sugar, sunflower oil, eggs, milk, fresh meat, rice) | Article 30, as amended |
| Exempt | Financial, insurance, medical, educational, and others (Article 23-28) | Articles 23-28 |

### 1d. Zero-Rated Basic Foodstuffs [T1]

The following basic foodstuffs are subject to 0% DDV:
- Bread and flour
- Sugar
- Sunflower oil
- Eggs
- Milk
- Fresh meat
- Rice

**Legislation:** Article 30, as amended

### 1e. Reduced Rate (10%) -- Food/Beverage Services [T1]

The 10% rate applies to:
- Supply of food and beverages (excluding alcoholic beverages) for immediate consumption at the place of supply (restaurant and catering services)

**Legislation:** Article 29, as amended

### 1f. Reduced Rate (5%) Categories [T1]

The 5% rate applies to:
- Medicines and medical devices
- Computers and computer equipment (for educational institutions)
- Public transport (urban and intercity passenger transport)
- Water supply (piped water from public systems)
- Books, textbooks, and school supplies
- Agricultural inputs (seeds, fertilizers, pesticides), agricultural material and equipment
- Accommodation/hotel services
- Heating energy (central heating, wood pellets, pellet stoves and boilers)
- Baby food and hygiene products
- Food for livestock

**Legislation:** Article 29(2), as amended

### 1g. Exempt Supplies (Articles 23-28) [T1]

The following are exempt from DDV:
- Financial and banking services (interest, currency exchange, securities trading)
- Insurance and reinsurance
- Medical and dental services (licensed practitioners)
- Educational services (state-accredited institutions)
- Residential property rental
- Postal services (universal, by state operator)
- Cultural, artistic, and sporting events (under conditions)
- Gambling and lottery
- Burial services
- Social welfare services
- Agricultural land sales

### 1h. Determine Expense Category [T1]
- Fixed assets: per accounting standards, useful life > 12 months
- Goods for resale: purchased for direct resale
- Raw materials: consumed in production
- Services/overheads: everything else

---

## Step 2: DDV Return Form Structure [T1]

**The DDV return (DDV-04 form) is filed electronically via the UJP e-Taxes portal.**

**Legislation:** Law on DDV Article 44; PRO instructions

### Part I -- Output DDV

| Box | Description | Rate |
|-----|-------------|------|
| 11 | Taxable supplies at 18% -- tax base | 18% |
| 12 | Output DDV at 18% | calculated |
| 13 | Taxable supplies at 5% -- tax base | 5% |
| 14 | Output DDV at 5% | calculated |
| 15 | Zero-rated supplies (exports) | 0% |
| 16 | Exempt supplies | - |
| 17 | Self-assessed DDV on imports of services (reverse charge) -- tax base | varies |
| 18 | Output DDV on reverse charge | calculated |
| 19 | Total output DDV (12 + 14 + 18) | sum |

### Part II -- Input DDV

| Box | Description |
|-----|-------------|
| 21 | Domestic purchases -- tax base |
| 22 | Input DDV on domestic purchases |
| 23 | Imports -- customs value + duties |
| 24 | DDV paid on imports |
| 25 | Fixed asset purchases -- tax base |
| 26 | Input DDV on fixed assets |
| 27 | Input DDV on reverse charge (deductible) |
| 28 | Input DDV corrections/adjustments |
| 29 | Total input DDV (22 + 24 + 26 + 27 + 28) |

### Part III -- Settlement

| Box | Description |
|-----|-------------|
| 31 | DDV payable (if 19 > 29) |
| 32 | DDV credit (if 29 > 19) |
| 33 | DDV credit carried forward from prior period |
| 34 | DDV credit for refund |
| 35 | Net DDV payable |

---

## Step 3: Reverse Charge and Import Mechanisms

### 3a. Services from Non-Residents [T1]

When a Macedonian entity purchases services from a non-resident with no MK registration:
- Place of supply determined under Article 12-13 of the Law on DDV
- If place of supply is North Macedonia, buyer self-assesses DDV at 18% (or 5%)
- Report in Box 17 (tax base) and Box 18 (output DDV)
- Claim input DDV in Box 27 (if entitled to deduction)
- Net effect: zero for fully taxable businesses

**Legislation:** Law on DDV Article 12-13, Article 32

### 3b. Imports of Goods [T1]

Goods imported into North Macedonia:
- DDV collected by Customs Administration at the border
- Rate: 18% or 5% depending on goods classification
- Tax base: customs value + import duties + excise duties (if applicable)
- Customs DDV is recoverable as input DDV
- Requires customs declaration (ECD) as documentary evidence

### 3c. Exports [T1]

Exports of goods outside North Macedonia:
- Zero-rated under Article 30
- Requires customs export declaration as evidence
- Related input DDV is fully deductible

### 3d. CEFTA Trade [T2]

Trade with CEFTA members (Serbia, Bosnia, Montenegro, Kosovo, Albania, Moldova):
- Treated as standard imports/exports (customs apply)
- CEFTA reduces/eliminates customs duties on qualifying goods
- DDV still applies on imports (like non-EU imports)
- Exports are zero-rated with customs documentation

---

## Step 4: Input DDV Deduction Rules

### 4a. General Conditions (Article 33-35) [T1]

Input DDV is deductible if ALL conditions are met:
1. Goods/services acquired for use in taxable operations
2. A valid tax invoice (faktura) is available
3. Goods/services recorded in accounting
4. For imports: customs declaration and payment proof available

### 4b. Invoice Requirements [T1]

A valid DDV invoice (faktura) must contain:
- Sequential number and date
- Seller's name, address, EDB number
- Buyer's name, address, EDB number
- Description of goods/services
- Quantity and unit price (excl. DDV)
- DDV rate and amount
- Total amount including DDV
- Date of supply (if different from invoice date)

### 4c. Blocked Input DDV (Non-Deductible) [T1]

Input DDV is NOT deductible for:

| Category | Legislation |
|----------|-------------|
| Goods/services used for exempt operations | Article 34 |
| Passenger vehicles and fuel for non-business purposes | Article 34(1)(4) |
| Entertainment, hospitality, and representation expenses | Article 34(1)(3) |
| Goods/services for personal use of employees/directors | Article 34(1)(5) |
| Goods/services not used for economic activity | Article 34(1)(1) |
| Purchases without valid tax invoice | Article 33 |

### 4d. Partial Deduction (Article 35) [T2]

If a business makes both taxable and exempt supplies:
- Separate accounting of input DDV required
- Direct attribution first
- Mixed-use costs: proportional deduction

**Pro-rata formula:**
```
Deductible % = (Taxable supplies + Zero-rated supplies) /
               (Taxable supplies + Zero-rated supplies + Exempt supplies) * 100
```

Round up to the nearest whole percentage.

**Flag for reviewer: confirm pro-rata calculation and allocation methodology.**

---

## Step 5: Derived Calculations [T1]

```
Total Output DDV (Box 19) = Box 12 + Box 14 + Box 18

Total Input DDV (Box 29) = Box 22 + Box 24 + Box 26 + Box 27 + Box 28

IF Box 19 > Box 29 THEN
    Box 31 = Box 19 - Box 29 (DDV payable)
    Box 32 = 0
ELSE
    Box 31 = 0
    Box 32 = Box 29 - Box 19 (DDV credit)
END

Box 35 = Box 31 - Box 33 (net payable after credit brought forward)
IF Box 35 < 0 THEN Box 35 = 0; excess remains as credit
```

---

## Step 6: Key Thresholds

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory DDV registration | Annual turnover > MKD 2,000,000 | Article 40 |
| Voluntary registration | Below threshold, may register voluntarily | Article 40 |
| Monthly filing threshold | Annual turnover > MKD 25,000,000 | Article 44 |
| Quarterly filing | Annual turnover <= MKD 25,000,000 | Article 44 |
| DDV refund eligibility | Credit accumulated for 3+ periods, or exporters | Article 47 |
| Small enterprise scheme | Below MKD 2,000,000 | Article 40-41 |

---

## Step 7: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|------------|--------|----------|-------------|
| DDV return (monthly filers) | Monthly | 25th of the month following the reporting month | Article 44 |
| DDV payment (monthly filers) | Monthly | 25th of the month following the reporting month | Article 44 |
| DDV return (quarterly filers) | Quarterly | 25th of the month following the quarter end | Article 44 |
| DDV payment (quarterly filers) | Quarterly | 25th of the month following the quarter end | Article 44 |
| Import DDV | Per import | At customs clearance | Customs Law |
| Annual DDV reconciliation | Annual | With annual financial statements | Article 44 |

---

## Step 8: EU Accession Impact [T2]

North Macedonia is an EU candidate country with accession negotiations ongoing:
- Current DDV law is largely aligned with EU VAT Directive 2006/112/EC
- Upon EU accession, intra-community supply/acquisition rules will apply
- The standard rate (18%) meets the EU minimum (15%)
- The reduced rate (5%) meets the EU minimum for reduced rates (5%)
- Transition to EU VAT system will require significant administrative changes

**Flag for reviewer: monitor legislative changes related to EU accession chapters on taxation.**

---

## Step 9: Edge Case Registry

### EC1 -- Purchase of software from US company [T1]

**Situation:** Macedonian company subscribes to a US-based SaaS platform. No DDV charged.
**Resolution:** Reverse charge applies. Place of supply is North Macedonia (buyer's location for B2B electronic services). Self-assess DDV at 18%. Box 17 = net amount, Box 18 = DDV at 18%, Box 27 = deductible DDV. Net effect zero for fully taxable business.
**Legislation:** Law on DDV Article 12, Article 32

### EC2 -- Export to Serbia (CEFTA) [T1]

**Situation:** Macedonian company exports goods to Serbia.
**Resolution:** Zero-rated export. Customs export declaration required. Report in Box 15. Related input DDV fully deductible. CEFTA may reduce customs duty on the Serbian side, but that does not affect MK DDV treatment.
**Legislation:** Article 30, CEFTA Agreement

### EC3 -- Mixed taxable and exempt operations [T2]

**Situation:** Company provides both taxable IT services and exempt financial advisory services.
**Resolution:** Separate accounting required. Direct attribution first. Mixed costs split using pro-rata formula. Flag for reviewer: confirm allocation methodology and pro-rata percentage.
**Legislation:** Article 35

### EC4 -- TIDZ resident [T2]

**Situation:** Company operates from a Technological Industrial Development Zone (TIDZ).
**Resolution:** TIDZ residents may benefit from DDV exemptions on certain imports and operations. Specifically, goods imported for use in TIDZ activities may be exempt from import DDV. However, domestic sales by TIDZ residents to non-TIDZ entities are generally subject to standard DDV. Flag for reviewer: verify TIDZ agreement terms and specific DDV benefits.
**Legislation:** Law on TIDZ, Government agreements with TIDZ investors

### EC5 -- Passenger vehicle purchase [T1]

**Situation:** Company purchases a passenger car for business use.
**Resolution:** Input DDV on passenger vehicles is BLOCKED under Article 34(1)(4). No deduction available regardless of business use. Exception: vehicles used exclusively as taxis, driving school cars, or rental vehicles (must demonstrate exclusive business use).
**Legislation:** Article 34(1)(4)

### EC6 -- Credit note / return of goods [T1]

**Situation:** Buyer returns defective goods; seller issues credit note.
**Resolution:** Seller reduces output DDV in the current period. Buyer reduces input DDV in the current period. Corrective invoice required. Both parties adjust their current DDV-04 returns.
**Legislation:** Article 17, Article 33

### EC7 -- Advance payment received [T1]

**Situation:** Company receives an advance payment before delivery of goods.
**Resolution:** DDV is due on advance payments at the time of receipt. Output DDV must be charged and reported in the period the advance is received. When goods are delivered, the advance DDV is adjusted against the final invoice DDV.
**Legislation:** Article 14(3)

### EC8 -- Construction services with subcontractors [T2]

**Situation:** Construction company engages multiple subcontractors on a building project.
**Resolution:** Each subcontractor charges DDV at 18% on their services. The main contractor claims input DDV. If the main contractor also sells the completed property (which may be exempt for residential), partial deduction rules apply. Flag for reviewer: determine if the final sale is taxable or exempt.
**Legislation:** Article 23 (property exemptions), Article 35 (partial deduction)

---

## PROHIBITIONS [T1]

- NEVER let AI guess DDV treatment -- classification is deterministic from facts and legislation
- NEVER apply input DDV deduction without a valid tax invoice (faktura)
- NEVER allow non-registered entities to claim input DDV deductions
- NEVER apply 0% rate on exports without customs documentation
- NEVER ignore reverse charge on services from non-residents
- NEVER apply the 5% rate to categories not specifically listed
- NEVER allow input DDV deduction on passenger vehicles (unless specific exception applies)
- NEVER allow input DDV deduction on entertainment/representation expenses
- NEVER assume EU intra-community rules apply -- North Macedonia is NOT yet an EU member
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 10: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Qualified tax practitioner must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to qualified practitioner. Document gap.
```

---

## Step 11: Test Suite

### Test 1 -- Standard domestic sale at 18%

**Input:** Macedonian company sells IT consulting to local client. Net MKD 100,000. DDV at 18%.
**Expected output:** Box 11 = MKD 100,000. Box 12 = MKD 18,000. Invoice issued.

### Test 2 -- Domestic purchase with input DDV

**Input:** Macedonian company purchases office equipment. Gross MKD 59,000 including DDV MKD 9,000. Valid invoice received.
**Expected output:** Box 21 includes MKD 50,000. Box 22 = MKD 9,000. Fully deductible.

### Test 3 -- Import of goods

**Input:** Company imports raw materials from Turkey. Customs value MKD 500,000. Customs duty MKD 25,000. No excise.
**Expected output:** DDV base = MKD 525,000. Import DDV = MKD 525,000 * 18% = MKD 94,500. Box 23 = MKD 525,000. Box 24 = MKD 94,500. Deductible.

### Test 4 -- Sale of bread at 5%

**Input:** Bakery sells bread products. Net MKD 200,000. DDV at 5%.
**Expected output:** Box 13 = MKD 200,000. Box 14 = MKD 10,000.

### Test 5 -- Services from non-resident (reverse charge)

**Input:** Macedonian company engages a UK law firm. Fee EUR 2,000 (equivalent MKD 123,000). No MK registration.
**Expected output:** Box 17 = MKD 123,000. Box 18 = MKD 22,140 (18%). Box 27 = MKD 22,140 (deductible). Net zero.

### Test 6 -- Export of goods

**Input:** Macedonian company exports textiles to Germany. Invoice MKD 400,000. Customs declaration confirmed.
**Expected output:** Box 15 = MKD 400,000. DDV = 0%. Related input DDV fully deductible.

### Test 7 -- Blocked passenger vehicle

**Input:** Company purchases a car. Gross MKD 900,000 including DDV MKD 137,288.
**Expected output:** Input DDV of MKD 137,288 is NOT deductible. Blocked under Article 34(1)(4). Full cost MKD 900,000 capitalized.

### Test 8 -- Accommodation at 5%

**Input:** Hotel provides accommodation services. Net MKD 50,000. DDV at 5%.
**Expected output:** Box 13 = MKD 50,000. Box 14 = MKD 2,500.

---

## Step 12: Penalties and Interest [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing of DDV return | MKD 500-2,000 per day of delay | Law on Tax Administration |
| Late payment of DDV | 0.03% per day of the outstanding amount | Law on Tax Administration |
| Understatement of DDV | 50% of understated amount | Law on Tax Administration |
| Failure to register for DDV | Back-assessment + penalty | Law on DDV Article 40 |
| Issuing false invoices | Criminal liability | Criminal Code |
| Failure to issue invoice | MKD 2,000-3,000 per instance | Law on DDV |

---

## Step 13: Currency and Exchange Rate Rules [T1]

- North Macedonia uses the Macedonian Denar (MKD)
- All DDV returns filed in MKD
- Foreign currency: official National Bank of North Macedonia (NBRM) middle rate on the transaction date
- Imports: NBRM rate on date of customs declaration
- Services from non-residents: NBRM rate on date of tax point
- Exports: NBRM rate on date of supply

---

## Step 14: Place of Supply Rules for Services [T1]

| Service Type | Place of Supply | Legislation |
|-------------|----------------|-------------|
| B2B general services | Where recipient is established | Article 12 |
| B2C general services | Where supplier is established | Article 12 |
| Immovable property services | Where property is located | Article 12(3) |
| Passenger transport | Where transport takes place | Article 12(4) |
| Cultural/entertainment events | Where event takes place | Article 12(5) |
| Restaurant/catering | Where services provided | Article 12(6) |
| Telecommunications/electronic (B2C) | Where recipient located | Article 12(7) |

---

## Step 15: Record Keeping [T1]

DDV payers must maintain records for a minimum of 10 years:

| Record | Requirement |
|--------|-------------|
| Tax invoices (issued and received) | Sequential filing |
| Purchase/Sales ledgers | DDV details with invoice references |
| Import/Export customs documents | Originals or certified copies |
| DDV returns (filed copies) | With PRO confirmation |
| Contracts | For significant transactions |
| Bank statements | Payment evidence |

---

## Contribution Notes

This skill requires validation by a licensed North Macedonian tax practitioner. Key areas requiring local expertise:

1. Current reduced rate (5%) categories (subject to legislative updates)
2. TIDZ-specific DDV rules
3. EU accession progress and impact on DDV law
4. CEFTA preferential treatment implementation
5. Annual threshold updates

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
