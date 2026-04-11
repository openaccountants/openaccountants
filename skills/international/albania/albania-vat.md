---
name: albania-vat
description: Use this skill whenever asked to prepare, review, or advise on an Albanian VAT (TVSH) return or any transaction classification for Albanian VAT purposes. Trigger on phrases like "Albania VAT", "Albanian TVSH", "TVSH return", "DPT filing", "Albanian tax", or any request involving Albanian VAT obligations. This skill contains the complete Albanian TVSH classification rules, rate structure, return form mappings, deductibility rules, reverse charge treatment, and filing deadlines. ALWAYS read this skill before touching any Albanian VAT-related work.
---

# Albania VAT (TVSH) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Republic of Albania |
| Jurisdiction Code | AL |
| Tax Name | TVSH (Tatimi mbi Vleren e Shtuar / VAT) |
| Primary Legislation | Law No. 92/2014 "On Value Added Tax in the Republic of Albania" (as amended) |
| Supporting Legislation | Council of Ministers Decisions on implementation; Customs Code; Law on Tax Procedures |
| Tax Authority | General Directorate of Taxation (DPT -- Drejtoria e Pergjithshme e Tatimeve) |
| Filing Portal | https://e-filing.tatime.gov.al (e-Filing system) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by licensed Albanian tax practitioner |
| Validation Date | April 2026 (web-verified; practitioner sign-off still pending) |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: rate application, standard classification, basic input deductions. Tier 2: tourism reduced rate, partial deduction, free zones. Tier 3: transfer pricing, complex group structures. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified tax practitioner must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified practitioner and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and NUIS/NIPT (Unique Identification Number)** [T1] -- tax identification number
2. **TVSH registration status** [T1] -- registered TVSH payer, small business (exempt), or non-registered
3. **TVSH period** [T1] -- monthly (standard for all TVSH payers)
4. **Industry/sector** [T2] -- impacts reduced rate eligibility (especially tourism/accommodation)
5. **Does the business make exempt supplies?** [T2] -- partial deduction rules apply
6. **Does the business trade cross-border?** [T1] -- impacts import/export treatment
7. **Accumulated TVSH credit** [T1] -- from prior periods
8. **Is the business in a free economic zone?** [T2] -- special TVSH benefits may apply
9. **Does the business provide tourism/accommodation services?** [T2] -- 6% reduced rate applies

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until registration status and period are confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output TVSH) or Purchase (input TVSH)
- Salaries, social/health insurance, dividends, loan repayments, penalties = OUT OF SCOPE
- **Legislation:** Law No. 92/2014, Article 3-6 (taxable supply definitions)

### 1b. Determine Counterparty Location [T1]
- Albania (domestic): supplier/customer registered in Albania
- EU: all 27 EU member states (Albania is EU candidate; customs apply)
- CEFTA: Serbia, North Macedonia, Bosnia, Montenegro, Kosovo, Moldova
- Other foreign: all remaining countries

### 1c. Determine TVSH Rate [T1]

| Rate | Application | Legislation |
|------|-------------|-------------|
| 20% | Standard rate -- most goods and services | Article 56 |
| 6% | Reduced rate -- accommodation/tourism services (hotels, agritourism, certified structures) | Article 56(1.1) |
| 10% | Reduced rate -- agricultural inputs (fertilisers, pesticides, seeds, seedlings) | Article 56 |
| 0% | Zero rate -- exports of goods, international transport, supplies to diplomatic missions | Article 51-55 |
| Exempt | Financial, insurance, medical, educational, and others (Article 51) | Article 51 |

### 1d. Reduced Rate (6%) Categories [T1]

The 6% reduced rate applies specifically to:
- Accommodation services provided by certified tourism structures (hotels, resorts, guesthouses, agritourism)
- The reduced rate was introduced to promote Albania's tourism sector
- Applies ONLY to the accommodation component; restaurant/bar services within hotels are at 20%
- The service provider must hold a valid tourism license/certification

**Legislation:** Article 56(1.1), as amended by Law No. 71/2017 and subsequent amendments

### 1e. Additional Reduced Rate Categories [T2]

Albania has introduced other reduced/special rates for specific sectors:
- Advertising services by audio-visual media: 6% [T2]
- Supply of agricultural inputs (chemical fertilisers, pesticides, seeds, seedlings): 10% [T1]
- Medical equipment and medicines: some items zero-rated on import [T2]

**Flag for reviewer: reduced rate categories are subject to frequent legislative changes. Verify current applicability.**

### 1f. Exempt Supplies (Article 51) [T1]

The following are exempt from TVSH:
- Financial and banking services (interest, currency exchange)
- Insurance and reinsurance
- Medical and dental services (by licensed practitioners)
- Educational services (state-accredited institutions)
- Residential property rental (first transfer of new residential, if applicable, may be taxable)
- Postal services (universal)
- Cultural/artistic events (public interest, under conditions)
- Gambling/lottery (separately taxed)
- Burial services
- Social welfare services
- Agricultural land transactions
- Gold supplied to Bank of Albania

### 1g. Determine Expense Category [T1]
- Fixed assets: per Albanian accounting standards, useful life > 12 months
- Goods for resale: purchased for direct resale
- Raw materials: consumed in production
- Services/overheads: everything else

---

## Step 2: TVSH Return Form Structure [T1]

**The TVSH declaration is filed monthly via the DPT e-Filing portal. All TVSH payers must file electronically.**

**Legislation:** Law No. 92/2014 Article 105-107; Instruction of the Minister of Finance

### Part I -- Output TVSH (Sales)

| Box | Description | Rate |
|-----|-------------|------|
| 1 | Taxable supplies at 20% -- tax base | 20% |
| 2 | Output TVSH at 20% | calculated |
| 3 | Taxable supplies at 6% -- tax base | 6% |
| 4 | Output TVSH at 6% | calculated |
| 5 | Zero-rated supplies (exports) | 0% |
| 6 | Exempt supplies | - |
| 7 | Self-assessed TVSH on services from abroad (reverse charge) -- base | varies |
| 8 | Output TVSH on reverse charge | calculated |
| 9 | Total output TVSH (2 + 4 + 8) | sum |

### Part II -- Input TVSH (Purchases)

| Box | Description |
|-----|-------------|
| 10 | Domestic purchases -- tax base |
| 11 | Input TVSH on domestic purchases |
| 12 | Imports -- customs value + duties |
| 13 | TVSH paid on imports |
| 14 | Fixed asset acquisitions -- tax base |
| 15 | Input TVSH on fixed assets |
| 16 | Input TVSH on reverse charge (deductible) |
| 17 | Adjustments to input TVSH |
| 18 | Total input TVSH (11 + 13 + 15 + 16 + 17) |

### Part III -- Settlement

| Box | Description |
|-----|-------------|
| 19 | TVSH payable (if 9 > 18) |
| 20 | TVSH credit (if 18 > 9) |
| 21 | TVSH credit from prior period |
| 22 | TVSH credit for refund |
| 23 | Net TVSH payable |

---

## Step 3: Reverse Charge and Import Mechanisms

### 3a. Services from Non-Residents [T1]

When an Albanian entity purchases services from a non-resident with no Albanian registration:
- Place of supply: determined under Article 25-30 of the Law on TVSH
- If place of supply is Albania, buyer self-assesses TVSH at 20% (or applicable rate)
- Report in Box 7 (tax base) and Box 8 (output TVSH)
- Claim input TVSH in Box 16 (if entitled to deduction)
- Net effect: zero for fully taxable businesses

**Legislation:** Article 25-30, Article 86

### 3b. Imports of Goods [T1]

Goods imported into Albania:
- TVSH collected by Customs Administration at the border
- Rate: 20% (or 6% if applicable, or 0% for specific medical/agricultural imports)
- Tax base: customs value + import duties + excise (if applicable)
- Customs TVSH is recoverable as input TVSH
- Requires customs declaration as documentary evidence

### 3c. Exports [T1]

Exports of goods outside Albania:
- Zero-rated under Article 54
- Requires customs export declaration
- Related input TVSH is fully deductible

### 3d. Supplies to Free Zones [T2]

Albania has designated free economic zones (e.g., Spitalla, Koplik, Vlora):
- Goods entering free zones may be exempt from import TVSH
- Sales from free zones to domestic market are subject to standard TVSH
- Free zone operators may have specific TVSH obligations

**Flag for reviewer: free zone treatment requires case-by-case analysis.**

---

## Step 4: Input TVSH Deduction Rules

### 4a. General Conditions (Article 68-72) [T1]

Input TVSH is deductible if ALL conditions are met:
1. Goods/services acquired for use in taxable operations
2. A valid tax invoice (fature tatimore) is available
3. Goods/services recorded in accounting
4. For imports: customs declaration and payment proof available

### 4b. Tax Invoice (Fature Tatimore) Requirements [T1]

A valid fature tatimore must contain:
- Sequential number and date
- Seller's name, address, NUIS/NIPT
- Buyer's name, address, NUIS/NIPT
- Description of goods/services
- Quantity and unit price (excl. TVSH)
- TVSH rate and amount
- Total amount including TVSH

**Albania has implemented mandatory electronic invoicing (fiskalizimi) since 2021. All invoices must be issued through the fiscalization platform and receive a unique invoice identification code (NUIS).**

### 4c. Fiscalization (Fiskalizimi) [T1]

Since January 2021 (B2G and B2B) and September 2021 (B2C):
- All invoices must be electronically registered through the fiscalization system
- Each invoice receives a unique identification code (NIVF -- Numri Identifikues i Veprimit Fiskale)
- Cash transactions require electronic fiscal devices
- Non-fiscalized invoices may result in denial of input TVSH deduction

**Legislation:** Law No. 87/2019 on E-Invoicing and Fiscalization

### 4d. Blocked Input TVSH (Non-Deductible) [T1]

Input TVSH is NOT deductible for:

| Category | Legislation |
|----------|-------------|
| Goods/services used for exempt operations | Article 71 |
| Passenger vehicles (acquisition, rental, fuel) unless for business fleet | Article 71(2) |
| Entertainment, hospitality, and representation expenses | Article 71(3) |
| Personal consumption of employees/directors | Article 71(4) |
| Goods/services without valid fiscal invoice | Article 69 |
| Goods lost/destroyed (except force majeure with documentation) | Article 71 |
| Accommodation/catering for staff (unless remote work site) | Article 71 |

### 4e. Proportional Deduction (Article 73) [T2]

If a business makes both taxable and exempt supplies:
- Separate accounting of input TVSH required
- Direct attribution first
- Mixed-use costs: proportional deduction

**Pro-rata formula:**
```
Deductible % = (Taxable supplies + Zero-rated supplies) /
               (Taxable supplies + Zero-rated supplies + Exempt supplies) * 100
```

Round up to nearest whole percentage. Annual adjustment required.

**Flag for reviewer: confirm pro-rata calculation and allocation methodology.**

---

## Step 5: Derived Calculations [T1]

```
Total Output TVSH (Box 9) = Box 2 + Box 4 + Box 8

Total Input TVSH (Box 18) = Box 11 + Box 13 + Box 15 + Box 16 + Box 17

IF Box 9 > Box 18 THEN
    Box 19 = Box 9 - Box 18 (TVSH payable)
    Box 20 = 0
ELSE
    Box 19 = 0
    Box 20 = Box 18 - Box 9 (TVSH credit)
END

Box 23 = Box 19 - Box 21 (net payable after credit)
IF Box 23 < 0 THEN Box 23 = 0; excess remains as credit
```

---

## Step 6: Key Thresholds

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory TVSH registration | Annual turnover > ALL 10,000,000 | Article 11 |
| Voluntary registration | Below threshold, may register voluntarily | Article 11 |
| Small business tax (alternative) | Turnover ALL 0-8,000,000: exempt; ALL 8-14,000,000: simplified | Small Business Tax Law |
| TVSH refund eligibility | Credit accumulated for 3+ consecutive months | Article 76 |
| Export refund (expedited) | Within 30 days for exporters with >70% exports | Article 76 |
| Fixed asset threshold | Per accounting standards | Accounting standards |

---

## Step 7: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|------------|--------|----------|-------------|
| TVSH declaration | Monthly | 14th of the month following the reporting month | Article 107 |
| TVSH payment | Monthly | 14th of the month following the reporting month | Article 107 |
| Import TVSH | Per import | At customs clearance | Customs Code |
| Purchase/Sales books | Monthly | Submitted with declaration | Article 107 |
| Annual pro-rata adjustment | Annual | With December declaration | Article 73 |

---

## Step 8: Fiscalization and Digital Compliance [T1]

Albania's fiscalization system is one of the most advanced in the region:

### Key Requirements:
1. **B2B invoices:** Must be issued electronically through the DPT platform
2. **B2C invoices:** Must be issued through electronic fiscal devices
3. **Real-time reporting:** All transactions reported to DPT in real time
4. **QR codes:** Each invoice carries a QR code for verification
5. **Self-billing:** Allowed under specific conditions with written agreement

### Penalties for Non-Compliance:
- Issuing invoices without fiscalization: ALL 500,000 fine per invoice
- Operating without fiscal device (B2C): ALL 500,000 per instance
- Repeated violations: business closure for 30 days

---

## Step 9: Edge Case Registry

### EC1 -- Hotel accommodation at 6% [T1]

**Situation:** A certified hotel charges for room accommodation.
**Resolution:** The accommodation component is at 6%. Restaurant, bar, spa, and other services within the hotel are at 20%. The hotel must separate accommodation from other services on the invoice. If a package rate is offered without separation, the entire amount may be subject to 20%. Flag for reviewer if breakdown is unclear.
**Legislation:** Article 56(1.1)

### EC2 -- Services from non-resident software provider [T1]

**Situation:** Albanian company subscribes to a US-based SaaS platform.
**Resolution:** Reverse charge at 20%. Box 7 = net amount, Box 8 = TVSH at 20%, Box 16 = deductible TVSH. Net effect zero for fully taxable business. Invoice must be registered in purchase books.
**Legislation:** Article 25-30, Article 86

### EC3 -- Tourism operator with mixed services [T2]

**Situation:** Tour operator provides a package including accommodation (6%), meals (20%), and transport (20% or exempt if urban).
**Resolution:** Each component must be separated and taxed at the correct rate. The accommodation component at 6% requires the operator to be a certified tourism structure. Package tours may fall under the special margin scheme. Flag for reviewer: determine if the margin scheme applies and verify tourism certification.
**Legislation:** Article 56(1.1), Article 90 (special schemes)

### EC4 -- Construction of residential property [T2]

**Situation:** Construction company builds and sells new residential apartments.
**Resolution:** The first sale of new residential property may be subject to TVSH at 20% (or exempt under certain conditions for social housing). Subsequent resales of residential property are generally exempt. Flag for reviewer: determine if exemption applies and verify property classification.
**Legislation:** Article 51, specific government decisions

### EC5 -- Blocked passenger vehicle expense [T1]

**Situation:** Company purchases a sedan for director's use.
**Resolution:** Input TVSH on passenger vehicles is BLOCKED under Article 71(2). No deduction. Exception: vehicles used exclusively as taxis, rental fleet, driving school, or delivery vehicles. If claimed as business-only, flag for reviewer.
**Legislation:** Article 71(2)

### EC6 -- Credit note / return of goods [T1]

**Situation:** Buyer returns goods; seller issues a credit note.
**Resolution:** Seller reduces output TVSH in the current period. Buyer reduces input TVSH in the current period. Credit note must be fiscalized (registered through the fiscalization system). Both adjust current declarations.
**Legislation:** Article 82

### EC7 -- Agricultural producer with reduced regime [T2]

**Situation:** A farmer sells produce directly. Registered as a small agricultural producer.
**Resolution:** Agricultural producers below certain thresholds may benefit from a compensation scheme (flat-rate TVSH). Buyers from registered farmers may claim a deemed input TVSH. Flag for reviewer: verify if the compensation scheme applies and the current rate.
**Legislation:** Article 92 (agricultural scheme)

### EC8 -- Non-fiscalized invoice received [T1]

**Situation:** Company receives an invoice from a supplier that was not fiscalized (no NIVF code).
**Resolution:** Input TVSH deduction may be denied if the invoice lacks the fiscalization code. The buyer should request a properly fiscalized invoice. If the supplier refuses, report the non-compliance to DPT. Do not claim input TVSH on non-fiscalized invoices.
**Legislation:** Law No. 87/2019, Article 69

---

## PROHIBITIONS [T1]

- NEVER let AI guess TVSH treatment -- classification is deterministic from facts and legislation
- NEVER apply input TVSH deduction without a valid fiscalized invoice
- NEVER allow non-registered entities to claim input TVSH deductions
- NEVER apply 0% rate on exports without customs documentation
- NEVER ignore reverse charge on services from non-residents
- NEVER apply the 6% rate to non-accommodation services or uncertified tourism providers
- NEVER allow input TVSH on passenger vehicles (unless specific fleet exception)
- NEVER allow input TVSH on entertainment expenses
- NEVER accept non-fiscalized invoices for input TVSH deduction
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

### Test 1 -- Standard domestic sale at 20%

**Input:** Albanian company sells consulting services to local client. Net ALL 500,000. TVSH at 20%.
**Expected output:** Box 1 = ALL 500,000. Box 2 = ALL 100,000. Fiscalized invoice issued.

### Test 2 -- Domestic purchase with input TVSH

**Input:** Albanian company purchases office supplies. Gross ALL 120,000 including TVSH ALL 20,000. Fiscalized invoice received.
**Expected output:** Box 10 includes ALL 100,000. Box 11 = ALL 20,000. Fully deductible.

### Test 3 -- Import of goods

**Input:** Company imports machinery from Italy. Customs value ALL 2,000,000. Customs duty ALL 100,000. No excise.
**Expected output:** TVSH base = ALL 2,100,000. Import TVSH = ALL 420,000 (20%). Box 12 = ALL 2,100,000. Box 13 = ALL 420,000. Deductible.

### Test 4 -- Hotel accommodation at 6%

**Input:** Certified hotel provides accommodation. Net ALL 300,000. TVSH at 6%.
**Expected output:** Box 3 = ALL 300,000. Box 4 = ALL 18,000.

### Test 5 -- Services from non-resident (reverse charge)

**Input:** Albanian company engages a UK consulting firm. Fee EUR 3,000 (equivalent ALL 330,000). No AL registration.
**Expected output:** Box 7 = ALL 330,000. Box 8 = ALL 66,000 (20%). Box 16 = ALL 66,000. Net zero.

### Test 6 -- Export of goods

**Input:** Albanian company exports textiles to Germany. Invoice ALL 800,000. Customs declaration confirmed.
**Expected output:** Box 5 = ALL 800,000. TVSH = 0%. Related input TVSH fully deductible.

### Test 7 -- Blocked entertainment expense

**Input:** Company hosts a client dinner. Gross ALL 36,000 including TVSH ALL 6,000.
**Expected output:** Input TVSH of ALL 6,000 is NOT deductible. Blocked. Expense at gross ALL 36,000.

### Test 8 -- Non-fiscalized invoice

**Input:** Supplier provides goods with an invoice lacking the NIVF fiscalization code. TVSH shown as ALL 15,000.
**Expected output:** Input TVSH of ALL 15,000 is NOT deductible until a properly fiscalized invoice is obtained.

---

## Step 12: Penalties and Interest [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing of TVSH declaration | ALL 10,000 per day of delay (max ALL 500,000) | Law on Tax Procedures |
| Late payment of TVSH | 0.06% per day of outstanding amount | Law on Tax Procedures |
| Understatement of TVSH | 100% of understated amount (plus interest) | Law on Tax Procedures |
| Failure to register | Back-assessment + ALL 50,000-100,000 | Law on TVSH |
| Non-fiscalized invoice | ALL 500,000 per invoice | Law No. 87/2019 |
| Operating without fiscal device | ALL 500,000 per instance; repeated = 30-day closure | Law No. 87/2019 |
| Issuing false invoices | Criminal liability | Criminal Code |

---

## Step 13: Currency and Exchange Rate Rules [T1]

- Albania uses the Albanian Lek (ALL) as national currency
- All TVSH returns filed in ALL
- Foreign currency transactions: official Bank of Albania middle rate on the transaction date
- Imports: Bank of Albania rate on date of customs declaration
- Services from non-residents: Bank of Albania rate on the date of payment or accrual
- Exports: Bank of Albania rate on the date of supply

---

## Contribution Notes

This skill requires validation by a licensed Albanian tax practitioner. Key areas requiring local expertise:

1. Current reduced rate categories (subject to frequent changes)
2. Fiscalization system technical requirements
3. Tourism certification requirements for 6% rate
4. Agricultural compensation scheme details
5. Free economic zone specific rules

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
