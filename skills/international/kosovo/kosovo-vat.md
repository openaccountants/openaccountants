---
name: kosovo-vat
description: Use this skill whenever asked to prepare, review, or advise on a Kosovo VAT (TVSH) return or any transaction classification for Kosovo VAT purposes. Trigger on phrases like "Kosovo VAT", "Kosovo TVSH", "TAK filing", "Kosovo tax return", or any request involving Kosovo VAT obligations. This skill contains the complete Kosovo TVSH classification rules, rate structure (18% standard, 8% reduced), return form mappings, deductibility rules, reverse charge treatment, and filing deadlines. ALWAYS read this skill before touching any Kosovo VAT-related work.
---

# Kosovo VAT (TVSH) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Republic of Kosovo |
| Jurisdiction Code | XK |
| Tax Name | TVSH (Tatimi mbi Vleren e Shtuar / VAT) |
| Primary Legislation | Law No. 05/L-037 on Value Added Tax (as amended) |
| Supporting Legislation | Administrative Instructions on TVSH; Customs and Excise Code; Law on Tax Administration and Procedures |
| Tax Authority | Tax Administration of Kosovo (TAK -- Administrata Tatimore e Kosoves) |
| Filing Portal | https://edeklarimi.atk-ks.org (e-Declaration system) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by licensed Kosovo tax practitioner |
| Validation Date | April 2026 (web-verified; practitioner sign-off still pending) |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: rate application, standard classification, basic input deductions. Tier 2: partial deduction, CEFTA trade, recognition-related complications. Tier 3: transfer pricing, complex structures. |

---

## IMPORTANT: Recognition Status Note [T2]

Kosovo's international recognition status affects certain cross-border transactions:
- Kosovo is recognized by over 100 UN member states but not by all
- Serbia, Russia, China, and several other countries do not recognize Kosovo
- This may affect customs, trade documentation, and counterparty willingness
- Some international organizations and systems may not include Kosovo codes
- ISO country code is XK (user-assigned; not officially allocated by ISO)

**Cross-border transactions with non-recognizing states may require additional documentation or alternative arrangements. Flag for reviewer.**

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified tax practitioner must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified practitioner and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and fiscal number** [T1] -- issued by TAK
2. **TVSH registration number** [T1] -- begins with prefix
3. **TVSH registration status** [T1] -- registered TVSH payer, small business (exempt), or non-registered
4. **TVSH period** [T1] -- monthly (turnover > EUR 50,000) or quarterly (turnover <= EUR 50,000)
5. **Industry/sector** [T2] -- impacts reduced rate and exemptions
6. **Does the business make exempt supplies?** [T2] -- partial deduction rules
7. **Does the business trade cross-border?** [T1] -- import/export treatment
8. **Accumulated TVSH credit** [T1] -- from prior periods

**If any of items 1-4 are unknown, STOP.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output TVSH) or Purchase (input TVSH)
- Salaries, pension contributions, dividends, loan repayments = OUT OF SCOPE
- **Legislation:** Law on TVSH, Article 3-5

### 1b. Determine Counterparty Location [T1]
- Kosovo (domestic): registered in Kosovo
- EU: all 27 EU member states (customs apply; Kosovo is not EU member)
- CEFTA: Serbia, North Macedonia, Bosnia, Montenegro, Albania, Moldova
- Other foreign: all remaining countries
- **Note:** Trade with Serbia has specific complications due to non-recognition [T2]

### 1c. Determine TVSH Rate [T1]

| Rate | Application | Legislation |
|------|-------------|-------------|
| 18% | Standard rate -- most goods and services | Article 25(1) |
| 8% | Reduced rate -- specific categories (see below) | Article 25(2) |
| 0% | Zero rate -- exports, international transport, diplomatic supplies | Article 26 |
| Exempt | Financial, insurance, medical, educational, and others | Article 27 |

### 1d. Reduced Rate (8%) Categories [T1]

The 8% rate applies to:
- Water supply (piped water)
- Electricity supply (to households)
- Heating supply (central heating, fuel for heating)
- Cereals, flour, bread, and bakery products
- Milk and dairy products
- Cooking oil and fats
- Medicines and pharmaceutical products
- Medical equipment and devices
- Textbooks and educational materials
- IT equipment for educational institutions
- Agricultural inputs (seeds, fertilizers, animal feed)
- Infant food and products

**Legislation:** Article 25(2), Administrative Instruction

### 1e. Exempt Supplies (Article 27) [T1]

The following are exempt from TVSH:
- Financial and banking services
- Insurance and reinsurance
- Medical and dental services (licensed)
- Educational services (licensed institutions)
- Residential property rental
- Cultural and sporting events (public interest)
- Postal services (universal)
- Gambling/lottery (separately taxed)
- Burial services
- Social welfare services
- Import of goods by international organizations (KFOR, EU missions, etc.)

### 1f. Determine Expense Category [T1]
- Fixed assets: useful life > 12 months, above capitalization threshold
- Goods for resale: purchased for direct resale
- Raw materials: consumed in production
- Services/overheads: everything else

---

## Step 2: TVSH Return Form Structure [T1]

**The TVSH declaration is filed via the TAK e-Declaration portal.**

### Part I -- Output TVSH

| Box | Description | Rate |
|-----|-------------|------|
| 1 | Taxable supplies at 18% -- tax base | 18% |
| 2 | Output TVSH at 18% | calculated |
| 3 | Taxable supplies at 8% -- tax base | 8% |
| 4 | Output TVSH at 8% | calculated |
| 5 | Zero-rated supplies (exports) | 0% |
| 6 | Exempt supplies | - |
| 7 | Self-assessed TVSH on imports of services (reverse charge base) | varies |
| 8 | Output TVSH on reverse charge | calculated |
| 9 | Total output TVSH (2 + 4 + 8) | sum |

### Part II -- Input TVSH

| Box | Description |
|-----|-------------|
| 10 | Domestic purchases |
| 11 | Input TVSH on domestic purchases |
| 12 | Imports (customs) |
| 13 | TVSH paid on imports |
| 14 | Fixed assets |
| 15 | Input TVSH on fixed assets |
| 16 | Input TVSH on reverse charge (deductible) |
| 17 | Adjustments |
| 18 | Total input TVSH (11 + 13 + 15 + 16 + 17) |

### Part III -- Settlement

| Box | Description |
|-----|-------------|
| 19 | TVSH payable (if 9 > 18) |
| 20 | TVSH credit (if 18 > 9) |
| 21 | Credit from prior period |
| 22 | Credit for refund |
| 23 | Net TVSH payable |

---

## Step 3: Reverse Charge and Import Mechanisms

### 3a. Services from Non-Residents [T1]

When a Kosovo entity purchases services from a non-resident with no Kosovo registration:
- If place of supply is Kosovo, buyer self-assesses TVSH at 18% (or 8%)
- Report in Box 7/8 (output) and Box 16 (input deduction)
- Net effect: zero for fully taxable businesses

### 3b. Imports of Goods [T1]

- TVSH collected by Kosovo Customs at the border
- Rate: 18% or 8%
- Tax base: customs value + import duties + excise
- Customs TVSH recoverable as input TVSH

### 3c. Exports [T1]

- Zero-rated under Article 26
- Customs export declaration required
- Input TVSH fully deductible

### 3d. Trade with Serbia [T2]

Trade between Kosovo and Serbia has specific complications:
- Serbia does not recognize Kosovo customs stamps/documentation
- CEFTA-mediated arrangements exist for bilateral trade
- Goods may transit through UNMIK-endorsed channels
- Documentation requirements may differ from standard trade

**Flag for reviewer: any transaction with Serbian entities requires case-by-case analysis.**

---

## Step 4: Input TVSH Deduction Rules

### 4a. General Conditions [T1]

Input TVSH is deductible if ALL conditions are met:
1. Goods/services acquired for taxable operations
2. Valid tax invoice available
3. Recorded in accounting
4. For imports: customs declaration and payment confirmation

### 4b. Invoice Requirements [T1]

A valid TVSH invoice must contain:
- Number and date
- Seller's name, address, fiscal number, TVSH number
- Buyer's name, address, fiscal number, TVSH number
- Description of goods/services
- Quantity and unit price
- TVSH rate and amount
- Total including TVSH

### 4c. Blocked Input TVSH (Non-Deductible) [T1]

| Category | Legislation |
|----------|-------------|
| Goods/services for exempt operations | Article 30 |
| Passenger vehicles (purchase, lease, fuel) | Article 30 |
| Entertainment and hospitality | Article 30 |
| Personal consumption | Article 30 |
| Without valid invoice | Article 29 |
| Goods lost/destroyed (except force majeure) | Article 30 |

### 4d. Proportional Deduction [T2]

For mixed taxable/exempt operations:

```
Deductible % = (Taxable + Zero-rated) / Total supplies * 100
```

Annual adjustment required. Flag for reviewer.

---

## Step 5: Derived Calculations [T1]

```
Total Output TVSH (Box 9) = Box 2 + Box 4 + Box 8
Total Input TVSH (Box 18) = Box 11 + Box 13 + Box 15 + Box 16 + Box 17

IF Box 9 > Box 18 THEN
    Box 19 = Box 9 - Box 18
    Box 20 = 0
ELSE
    Box 19 = 0
    Box 20 = Box 18 - Box 9
END

Box 23 = Box 19 - Box 21
IF Box 23 < 0 THEN Box 23 = 0; excess = credit
```

---

## Step 6: Key Thresholds

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory TVSH registration | Annual turnover > EUR 30,000 | Article 4 |
| Voluntary registration | Below threshold | Article 4 |
| Monthly filing threshold | Annual turnover > EUR 50,000 | Article 38 |
| Quarterly filing | Annual turnover <= EUR 50,000 | Article 38 |
| TVSH refund eligibility | Credit for 3+ periods | Article 34 |
| Export refund (expedited) | Exporters with >25% export ratio | Article 34 |

---

## Step 7: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|------------|--------|----------|-------------|
| TVSH return (monthly) | Monthly | 20th of the month following | Article 38 |
| TVSH payment (monthly) | Monthly | 20th of the month following | Article 38 |
| TVSH return (quarterly) | Quarterly | 20th of the month following quarter end | Article 38 |
| TVSH payment (quarterly) | Quarterly | 20th of the month following quarter end | Article 38 |
| Import TVSH | Per import | At customs clearance | Customs Code |

---

## Step 8: International Presence in Kosovo [T2]

Kosovo has significant international presence affecting TVSH:
- **KFOR (NATO-led peacekeeping):** Exempt from TVSH on supplies
- **EULEX (EU Rule of Law Mission):** Exempt from TVSH
- **International organizations:** Various TVSH exemptions under bilateral agreements
- **UNMIK:** United Nations Mission in Kosovo -- exempt status

Supplies to these organizations may be zero-rated or exempt. **Documentation (exemption certificates) must be obtained from the organization.**

---

## Step 9: Edge Case Registry

### EC1 -- SaaS subscription from US provider [T1]

**Situation:** Kosovo company subscribes to US cloud software. No TVSH charged.
**Resolution:** Reverse charge at 18%. Box 7 = net, Box 8 = TVSH at 18%, Box 16 = deductible. Net zero.

### EC2 -- Trade with Serbia [T2]

**Situation:** Kosovo company sells goods to Serbian buyer.
**Resolution:** Treatment depends on current CEFTA/bilateral arrangements. Standard export treatment may not apply due to non-recognition. Flag for reviewer: determine applicable customs/trade channel and documentation.

### EC3 -- Sale of bread at 8% [T1]

**Situation:** Bakery sells bread products.
**Resolution:** Bread at 8% reduced rate. Box 3 = net, Box 4 = TVSH at 8%.

### EC4 -- Supply to KFOR [T1]

**Situation:** Company provides catering to KFOR.
**Resolution:** KFOR supplies are exempt/zero-rated. Must obtain KFOR exemption certificate. Report in Box 5 or 6 depending on specific arrangement. Input TVSH on related costs may be deductible if zero-rated (not if exempt).

### EC5 -- Passenger vehicle [T1]

**Situation:** Company purchases a car.
**Resolution:** Input TVSH blocked. No deduction. Exception: taxis, rental fleet, driving school.

### EC6 -- Credit note [T1]

**Situation:** Goods returned; credit note issued.
**Resolution:** Both parties adjust current period declarations.

### EC7 -- Mixed taxable and exempt [T2]

**Situation:** Company provides both taxable consulting and exempt financial services.
**Resolution:** Proportional deduction required. Direct attribution first, then pro-rata for mixed costs. Flag for reviewer.

### EC8 -- Import of medicines at 8% [T1]

**Situation:** Company imports pharmaceutical products.
**Resolution:** Import TVSH at 8% (reduced rate for medicines). Customs TVSH = (customs value + duties) * 8%. Input TVSH deductible if for taxable operations.

---

## PROHIBITIONS [T1]

- NEVER let AI guess TVSH treatment -- deterministic from facts
- NEVER apply input TVSH without valid invoice
- NEVER allow non-registered entities to claim input TVSH
- NEVER apply 0% without customs documentation
- NEVER ignore reverse charge on non-resident services
- NEVER apply 8% to unlisted categories
- NEVER allow input TVSH on passenger vehicles or entertainment
- NEVER treat Serbia trade as routine without specialist review [T2]
- NEVER assume KFOR/EULEX exemptions without certificate
- NEVER compute any number -- handled by deterministic engine

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

**Input:** Kosovo company sells consulting services. Net EUR 10,000. TVSH at 18%.
**Expected output:** Box 1 = EUR 10,000. Box 2 = EUR 1,800.

### Test 2 -- Domestic purchase with input TVSH

**Input:** Purchase office supplies. Gross EUR 590 including TVSH EUR 90. Valid invoice.
**Expected output:** Box 10 includes EUR 500. Box 11 = EUR 90. Deductible.

### Test 3 -- Import of goods

**Input:** Import machinery from Germany. Customs value EUR 20,000. Duty EUR 1,000.
**Expected output:** TVSH base = EUR 21,000. Import TVSH = EUR 21,000 * 18% = EUR 3,780. Deductible.

### Test 4 -- Sale of bread at 8%

**Input:** Bakery sells bread. Net EUR 2,000. TVSH at 8%.
**Expected output:** Box 3 = EUR 2,000. Box 4 = EUR 160.

### Test 5 -- Reverse charge on non-resident

**Input:** Kosovo company engages Austrian consulting firm. EUR 5,000. No XK registration.
**Expected output:** Box 7 = EUR 5,000. Box 8 = EUR 900 (18%). Box 16 = EUR 900. Net zero.

### Test 6 -- Export

**Input:** Export to Albania. EUR 15,000. Customs declaration confirmed.
**Expected output:** Box 5 = EUR 15,000. TVSH = 0%. Input TVSH deductible.

### Test 7 -- Blocked passenger vehicle

**Input:** Company buys a sedan. Gross EUR 12,000 including TVSH EUR 1,831.
**Expected output:** Input TVSH EUR 1,831 NOT deductible. Blocked.

### Test 8 -- Import of medicines at 8%

**Input:** Import pharmaceutical products. Customs value EUR 50,000. Duty EUR 0.
**Expected output:** TVSH base = EUR 50,000. Import TVSH = EUR 50,000 * 8% = EUR 4,000. Deductible.

---

## Step 12: Penalties and Interest [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing of TVSH return | EUR 500 per month of delay | Law on Tax Administration |
| Late payment of TVSH | Monthly interest at the Central Bank rate + 1% | Law on Tax Administration |
| Understatement of TVSH | 15-25% of the understated amount | Law on Tax Administration |
| Failure to register | Back-assessment + EUR 500 penalty | Law on TVSH |
| Failure to issue invoice | EUR 250-500 per instance | Law on TVSH |
| False/fraudulent invoice | Criminal liability | Criminal Code |

---

## Step 13: Currency and Exchange Rate Rules [T1]

- Kosovo uses the Euro (EUR) as its official currency
- All TVSH returns filed in EUR
- No currency conversion needed for EUR transactions
- Non-EUR transactions: Central Bank of Kosovo (CBK) exchange rate on transaction date

---

## Step 14: Place of Supply Rules [T1]

| Service Type | Place of Supply |
|-------------|----------------|
| B2B general services | Where recipient is established |
| B2C general services | Where supplier is established |
| Immovable property | Where property is located |
| Transport | Where transport takes place |
| Cultural/entertainment | Where event takes place |
| Restaurant/catering | Where performed |
| Electronic services (B2C) | Where recipient is located |

---

## Step 15: Record Keeping [T1]

TVSH payers must maintain records for a minimum of 6 years:

| Record | Requirement |
|--------|-------------|
| Tax invoices (issued and received) | Sequential filing, chronological |
| Purchase and sales ledgers | Full TVSH details |
| Import/export customs documents | Originals |
| TVSH returns (filed copies) | With TAK confirmation |
| Contracts | For significant transactions |
| Bank statements | Payment evidence |
| Fiscal register records | Daily Z-reports for B2C |

---

## Step 16: Withholding Tax on Payments to Non-Residents [T2]

While not a TVSH matter directly, payments to non-residents may trigger:
- 10% withholding tax on services, interest, royalties, rent paid to non-residents
- This is a corporate/income tax obligation, NOT a TVSH obligation
- However, the same transaction may trigger both TVSH reverse charge AND withholding tax
- Flag for reviewer: when a service from a non-resident triggers reverse charge, also check withholding tax obligations

**This is an income tax matter and out of scope for this TVSH skill, but noted for awareness.**

---

## Contribution Notes

This skill requires validation by a licensed Kosovo tax practitioner. Key areas:

1. Serbia trade arrangements and documentation
2. International organization exemption procedures
3. Current reduced rate (8%) list
4. CEFTA implementation specifics
5. Recognition-related trade barriers

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
