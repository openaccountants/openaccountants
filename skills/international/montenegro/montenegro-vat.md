---
name: montenegro-vat
description: Use this skill whenever asked to prepare, review, or advise on a Montenegro VAT (PDV) return or any transaction classification for Montenegrin VAT purposes. Trigger on phrases like "Montenegro VAT", "Montenegrin PDV", "Montenegro tax return", "Tax Administration Montenegro", or any request involving Montenegrin VAT obligations. This skill contains the complete Montenegrin PDV classification rules, rate structure (21% standard, 15% intermediate reduced, 7% lower reduced), return form mappings, deductibility rules, reverse charge treatment, and filing deadlines. ALWAYS read this skill before touching any Montenegrin VAT-related work.
---

# Montenegro VAT (PDV) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Montenegro (Crna Gora) |
| Jurisdiction Code | ME |
| Tax Name | PDV (Porez na Dodatu Vrijednost / VAT) |
| Primary Legislation | Law on Value Added Tax (Zakon o Porezu na Dodatu Vrijednost), Official Gazette of Montenegro No. 65/2001 (as amended, including No. 73/2010, 40/2011, 29/2013, 9/2015, 53/2016, 67/2023) |
| Supporting Legislation | Rulebook on PDV implementation; Customs Law; Law on Fiscal Cash Registers |
| Tax Authority | Tax Administration of Montenegro (Poreska Uprava Crne Gore) |
| Filing Portal | https://eprijava.tax.gov.me (e-Filing portal) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by licensed Montenegrin tax practitioner |
| Validation Date | April 2026 (web-verified; practitioner sign-off still pending) |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: rate application, standard classification, basic input deductions. Tier 2: tourism sector treatment, partial deduction, EU accession impact. Tier 3: transfer pricing, complex structures. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified tax practitioner must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified practitioner and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and PIB (Tax Identification Number)** [T1]
2. **PDV registration number** [T1] -- assigned upon registration
3. **PDV registration status** [T1] -- registered PDV payer, small enterprise (exempt), or non-registered
4. **PDV period** [T1] -- monthly (turnover > EUR 500,000) or quarterly (turnover <= EUR 500,000)
5. **Industry/sector** [T2] -- impacts reduced rate and exemptions
6. **Does the business make exempt supplies?** [T2] -- partial deduction rules apply
7. **Does the business trade cross-border?** [T1] -- impacts import/export treatment
8. **Accumulated PDV credit** [T1] -- from prior periods
9. **Tourism sector?** [T2] -- 7% reduced rate on accommodation and food services

**If any of items 1-4 are unknown, STOP. Do not classify any transactions.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output PDV) or Purchase (input PDV)
- Salaries, social contributions, dividends, loan repayments = OUT OF SCOPE
- **Legislation:** Law on PDV, Article 3-4

### 1b. Determine Counterparty Location [T1]
- Montenegro (domestic): supplier/customer registered in ME
- EU: all 27 EU member states (ME is EU candidate; customs apply)
- CEFTA: Serbia, North Macedonia, Bosnia, Kosovo, Albania, Moldova
- Other foreign: all remaining countries

### 1c. Determine PDV Rate [T1]

| Rate | Application | Legislation |
|------|-------------|-------------|
| 21% | Standard rate -- most goods and services | Article 24(1) |
| 15% | Intermediate reduced rate -- books, publications, accommodation, food/beverage services (excl. alcohol, sugary drinks, coffee) (effective 1 January 2025) | Article 24, as amended |
| 7% | Lower reduced rate -- basic foodstuffs, medicines, textbooks, water supply, public transport, and others (see below) | Article 24(2) |
| 0% | Zero rate -- exports, international transport, diplomatic supplies | Article 25 |
| Exempt | Financial, insurance, medical, educational, and others | Article 26 |

### 1d. Intermediate Reduced Rate (15%) Categories (effective 1 January 2025) [T1]

The 15% rate applies to:
- Books, monographic and serial publications
- Accommodation services (hotels, motels, tourist resorts, guesthouses, camps, tourist apartments, villas)
- Food and beverage services in hospitality facilities (excluding alcoholic beverages, carbonated and non-carbonated drinks with added sugar, and coffee)

**Note:** These categories were previously subject to 7%. The reclassification to 15% was part of Montenegro's EU VAT Directive alignment.

**Legislation:** Article 24, as amended (Official Gazette 67/2023, amendments effective 1 January 2025)

### 1e. Lower Reduced Rate (7%) Categories [T1]

The 7% rate continues to apply to:
- Bread, flour, milk, and sugar
- Medicines, orthotic and prosthetic devices
- Textbooks and educational materials
- Drinking water from public supply (excluding bottled water)
- Daily and periodic newspapers
- Public passenger transport services
- Funeral services
- Animal food, fertilizers, plant protection products
- Seeds, planting materials, and live animals
- Menstrual products and baby diapers
- Public hygiene services

**Legislation:** Article 24(2), as amended

### 1e. Exempt Supplies (Article 26) [T1]

The following are exempt from PDV:
- Financial and banking services (interest, deposits, currency exchange)
- Insurance and reinsurance
- Medical and dental services (licensed)
- Educational services (state-accredited)
- Residential property rental
- Cultural, artistic, and sporting events (public interest)
- Postal services (universal)
- Gambling/lottery (separately taxed)
- Burial services
- Social welfare services
- Sale of agricultural land

### 1f. Determine Expense Category [T1]
- Fixed assets: per accounting standards, useful life > 12 months
- Goods for resale: purchased for direct resale
- Raw materials: consumed in production
- Services/overheads: everything else

---

## Step 2: PDV Return Form Structure [T1]

**The PDV return is filed monthly via the Tax Administration e-Filing portal.**

### Part I -- Output PDV

| Box | Description | Rate |
|-----|-------------|------|
| 1 | Taxable supplies at 21% -- tax base | 21% |
| 2 | Output PDV at 21% | calculated |
| 3a | Taxable supplies at 15% -- tax base | 15% |
| 3b | Output PDV at 15% | calculated |
| 3 | Taxable supplies at 7% -- tax base | 7% |
| 4 | Output PDV at 7% | calculated |
| 5 | Zero-rated supplies (exports) | 0% |
| 6 | Exempt supplies | - |
| 7 | Reverse charge -- services from abroad (tax base) | varies |
| 8 | Output PDV on reverse charge | calculated |
| 9 | Total output PDV (2 + 4 + 8) | sum |

### Part II -- Input PDV

| Box | Description |
|-----|-------------|
| 10 | Domestic purchases -- tax base |
| 11 | Input PDV on domestic purchases |
| 12 | Imports -- customs value + duties |
| 13 | PDV paid on imports |
| 14 | Fixed asset acquisitions |
| 15 | Input PDV on fixed assets |
| 16 | Input PDV on reverse charge (deductible) |
| 17 | Adjustments |
| 18 | Total input PDV (11 + 13 + 15 + 16 + 17) |

### Part III -- Settlement

| Box | Description |
|-----|-------------|
| 19 | PDV payable (if 9 > 18) |
| 20 | PDV credit (if 18 > 9) |
| 21 | PDV credit from prior period |
| 22 | PDV credit for refund |
| 23 | Net PDV payable |

---

## Step 3: Reverse Charge and Import Mechanisms

### 3a. Services from Non-Residents [T1]

When a Montenegrin entity purchases services from a non-resident with no ME registration:
- Place of supply: determined under Law on PDV place of supply rules
- If place of supply is Montenegro, buyer self-assesses PDV at 21% (or 7%)
- Report in Box 7 and Box 8 (output), Box 16 (input deduction)
- Net effect: zero for fully taxable businesses

### 3b. Imports of Goods [T1]

- PDV collected by Customs at the border
- Rate: 21% or 7% depending on goods classification
- Tax base: customs value + import duties + excise (if applicable)
- Customs PDV is recoverable as input PDV

### 3c. Exports [T1]

- Zero-rated under Article 25
- Customs export declaration required
- Related input PDV fully deductible

---

## Step 4: Input PDV Deduction Rules

### 4a. General Conditions [T1]

Input PDV is deductible if ALL conditions are met:
1. Goods/services acquired for use in taxable operations
2. A valid tax invoice (porezna faktura) is available
3. Goods/services recorded in accounting
4. For imports: customs declaration and payment proof

### 4b. Invoice Requirements [T1]

A valid invoice must contain:
- Sequential number and date
- Seller's name, address, PIB, PDV number
- Buyer's name, address, PIB, PDV number
- Description of goods/services
- Quantity and unit price (excl. PDV)
- PDV rate and amount
- Total including PDV

### 4c. Blocked Input PDV (Non-Deductible) [T1]

| Category | Legislation |
|----------|-------------|
| Goods/services for exempt operations | Article 37 |
| Passenger vehicles (purchase, lease, fuel, maintenance) | Article 37(3) |
| Entertainment, hospitality, representation | Article 37(3) |
| Personal consumption of employees/directors | Article 37(3) |
| Goods/services without valid invoice | Article 37(1) |
| Accommodation and meals for staff (unless remote site) | Article 37(3) |

### 4d. Proportional Deduction [T2]

If business makes both taxable and exempt supplies:

```
Deductible % = (Taxable + Zero-rated supplies) / Total supplies * 100
```

Round to nearest whole percentage. Annual adjustment.

**Flag for reviewer: confirm calculation.**

---

## Step 5: Derived Calculations [T1]

```
Total Output PDV (Box 9) = Box 2 + Box 4 + Box 8

Total Input PDV (Box 18) = Box 11 + Box 13 + Box 15 + Box 16 + Box 17

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
| Mandatory PDV registration | Annual turnover > EUR 30,000 | Article 43 |
| Voluntary registration | Below threshold | Article 43 |
| Small enterprise exemption | <= EUR 30,000 | Article 43 |
| Monthly filing threshold | Annual turnover > EUR 500,000 | Article 46 |
| Quarterly filing | Annual turnover <= EUR 500,000 | Article 46 |
| PDV refund eligibility | 3+ months credit or exporters | Article 40 |

---

## Step 7: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|------------|--------|----------|-------------|
| PDV return (monthly filers) | Monthly | 15th of the month following the reporting month | Article 46 |
| PDV payment (monthly filers) | Monthly | 15th of the month following the reporting month | Article 46 |
| PDV return (quarterly filers) | Quarterly | 15th of the month following the quarter end | Article 46 |
| PDV payment (quarterly filers) | Quarterly | 15th of the month following the quarter end | Article 46 |
| Import PDV | Per import | At customs clearance | Customs Law |
| Annual reconciliation | Annual | With annual financial statements | Article 46 |

---

## Step 8: Tourism Sector Special Rules [T2]

Montenegro's economy is heavily dependent on tourism. Special PDV considerations:

1. **Accommodation services:** 15% intermediate reduced rate for certified tourism structures (changed from 7% on 1 January 2025)
2. **Restaurant/food services:** 15% intermediate reduced rate for food and non-alcoholic beverages (changed from 7% on 1 January 2025; alcoholic beverages, sugary drinks, and coffee remain at 21%)
3. **Tour operator margin scheme:** Tour operators may use a special margin scheme where PDV is calculated on the margin (selling price minus cost of bought-in services)
4. **Seasonal considerations:** Many businesses operate seasonally; PDV returns must still be filed monthly even in off-season (nil returns if no activity)

**Flag for reviewer: tourism margin scheme requires specialist analysis.**

---

## Step 9: Edge Case Registry

### EC1 -- Hotel accommodation at 15% [T1]

**Situation:** Certified hotel charges for room accommodation.
**Resolution:** Accommodation at 15% (changed from 7% effective 1 January 2025). Spa, minibar, parking, conference rooms at 21%. Separation required on invoice. If bundled without separation, flag for reviewer.
**Legislation:** Article 24, as amended

### EC2 -- Restaurant food services at 15% [T1]

**Situation:** Restaurant charges for food and beverages.
**Resolution:** Food and non-alcoholic beverage service at 15% (changed from 7% effective 1 January 2025). Alcoholic beverages, carbonated/non-carbonated drinks with added sugar, and coffee are at 21%. Separation required on invoice.
**Legislation:** Article 24, as amended

### EC3 -- Services from non-resident (reverse charge) [T1]

**Situation:** Montenegrin company engages a UK IT firm for software development. No ME registration.
**Resolution:** Reverse charge at 21%. Box 7 = net amount, Box 8 = PDV at 21%, Box 16 = deductible PDV. Net zero for fully taxable business.

### EC4 -- CEFTA export to Serbia [T1]

**Situation:** Montenegrin company exports goods to Serbia.
**Resolution:** Zero-rated export. Customs declaration required. Box 5. Input PDV deductible.

### EC5 -- Passenger vehicle blocked [T1]

**Situation:** Company purchases a car.
**Resolution:** Input PDV blocked. No deduction. Exception for taxis, rental fleet, driving school only.
**Legislation:** Article 37(3)

### EC6 -- Credit note [T1]

**Situation:** Goods returned; credit note issued.
**Resolution:** Both parties adjust current period. Seller reduces output; buyer reduces input.

### EC7 -- Tour operator margin scheme [T2]

**Situation:** Tour operator packages hotel, transport, and excursions for tourists.
**Resolution:** May use margin scheme: PDV on margin only (selling price minus bought-in costs). Input PDV on bought-in travel services is NOT separately deductible under the margin scheme. Flag for reviewer: confirm margin scheme eligibility and calculation.
**Legislation:** Special scheme provisions in Law on PDV

### EC8 -- Real property sale [T2]

**Situation:** Company sells commercial premises.
**Resolution:** Sale of new commercial property generally subject to PDV at 21%. "New" typically means first transfer within a defined period of completion. Used commercial property may be exempt. Flag for reviewer: verify property status.

---

## PROHIBITIONS [T1]

- NEVER let AI guess PDV treatment -- deterministic from facts
- NEVER apply input PDV without valid invoice
- NEVER allow non-registered entities to claim input PDV
- NEVER apply 0% without customs documentation
- NEVER ignore reverse charge on non-resident services
- NEVER apply 7% or 15% to categories not listed in the applicable rate schedules
- NEVER allow input PDV on passenger vehicles or entertainment
- NEVER assume EU intra-community rules -- Montenegro is NOT an EU member
- NEVER skip monthly filing even in off-season (nil return required)
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

### Test 1 -- Standard domestic sale at 21%

**Input:** Montenegrin company sells IT services. Net EUR 5,000. PDV at 21%.
**Expected output:** Box 1 = EUR 5,000. Box 2 = EUR 1,050.

### Test 2 -- Domestic purchase with input PDV

**Input:** Company purchases office equipment. Gross EUR 2,420 including PDV EUR 420. Valid invoice.
**Expected output:** Box 10 includes EUR 2,000. Box 11 = EUR 420. Deductible.

### Test 3 -- Import of goods

**Input:** Import from China. Customs value EUR 10,000. Duty EUR 500. No excise.
**Expected output:** PDV base = EUR 10,500. Import PDV = EUR 10,500 * 21% = EUR 2,205. Deductible.

### Test 4 -- Hotel accommodation at 15%

**Input:** Certified hotel provides accommodation. Net EUR 3,000. PDV at 15%.
**Expected output:** Box 3a = EUR 3,000. Box 3b = EUR 450.

### Test 5 -- Reverse charge on non-resident services

**Input:** Montenegrin company engages a German law firm. Fee EUR 2,000. No ME registration.
**Expected output:** Box 7 = EUR 2,000. Box 8 = EUR 420 (21%). Box 16 = EUR 420. Net zero.

### Test 6 -- Export

**Input:** Export furniture to Italy. EUR 8,000. Customs declaration confirmed.
**Expected output:** Box 5 = EUR 8,000. PDV = 0%. Input PDV deductible.

### Test 7 -- Blocked entertainment

**Input:** Client dinner. Gross EUR 500 including PDV EUR 87.
**Expected output:** Input PDV EUR 87 NOT deductible. Blocked.

### Test 8 -- Restaurant food service at 15%

**Input:** Restaurant bills customers for meals (non-alcoholic food and beverages). Net EUR 1,500. PDV at 15%.
**Expected output:** Box 3a = EUR 1,500. Box 3b = EUR 225.

---

## Step 12: Penalties and Interest [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing of PDV return | EUR 500-20,000 per return | Law on Tax Administration |
| Late payment of PDV | 0.03% per day of outstanding amount | Law on Tax Administration |
| Understatement of PDV | 50% of understated amount plus interest | Law on Tax Administration |
| Failure to register | Back-assessment + EUR 500-5,000 penalty | Law on PDV |
| Failure to issue invoice | EUR 500-3,000 per instance | Law on PDV |
| False invoice | Criminal liability for amounts exceeding threshold | Criminal Code |

---

## Step 13: Currency and Exchange Rate Rules [T1]

- Montenegro uses the Euro (EUR) as its official currency (adopted unilaterally, not through Eurozone membership)
- All PDV returns filed in EUR
- No foreign currency conversion needed for EUR-denominated transactions
- Non-EUR foreign currency: Central Bank of Montenegro (CBCG) middle rate on transaction date

---

## Step 14: Place of Supply Rules for Services [T1]

| Service Type | Place of Supply |
|-------------|----------------|
| B2B general services | Where recipient is established |
| B2C general services | Where supplier is established |
| Immovable property | Where property is located |
| Transport | Where transport takes place |
| Cultural/entertainment | Where event takes place |
| Restaurant/catering | Where services performed |
| Electronic services (B2C) | Where recipient is located |

---

## Step 15: Record Keeping [T1]

PDV payers must maintain records for a minimum of 10 years:

| Record | Requirement |
|--------|-------------|
| Tax invoices (issued and received) | Sequential, chronological |
| Purchase and sales ledgers | With PDV calculations |
| Import/export customs documents | Originals retained |
| PDV returns (filed copies) | With Tax Administration confirmation |
| Contracts for significant transactions | Retained with supporting docs |
| Bank statements | Payment trail |
| Fiscal cash register records | Daily Z-reports for B2C |

---

## Step 16: EU Accession and PDV Alignment [T2]

Montenegro opened EU accession negotiations in 2012 and has made progress on Chapter 16 (Taxation):
- The PDV system is largely aligned with the EU VAT Directive
- The standard rate (21%) exceeds the EU minimum (15%)
- The reduced rate (7%) exceeds the EU minimum for reduced rates (5%)
- Upon accession, intra-community supply/acquisition rules will replace current import/export treatment for EU trade
- The transition will require significant administrative and IT system changes
- Current reverse charge mechanisms will be replaced by EU-standard rules

**Flag for reviewer: monitor Chapter 16 negotiations and legislative changes.**

---

## Contribution Notes

This skill requires validation by a licensed Montenegrin tax practitioner. Key areas:

1. Current reduced rate (7%) categories (subject to amendments)
2. Tourism margin scheme details
3. EU accession progress and PDV alignment
4. Seasonal business PDV obligations
5. Real property classification

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**

---

## Step 17: Fiscal Cash Register Requirements [T1]

Montenegro requires fiscal cash registers for B2C transactions:

| Requirement | Detail |
|-------------|--------|
| Mandatory for | All businesses conducting cash sales to consumers |
| Fiscal device | Must be certified by Tax Administration |
| Daily Z-report | Must be generated and stored daily |
| Fiscal receipts | Must be issued for every B2C cash transaction |
| Records retention | Minimum 5 years for fiscal memory data |
| Connection to Tax Admin | Real-time or periodic electronic reporting may be required |
| Penalties for non-compliance | EUR 500-5,000 per violation |

**B2B transactions via bank transfer do not require fiscal cash register receipts, but standard PDV invoices must be issued.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
