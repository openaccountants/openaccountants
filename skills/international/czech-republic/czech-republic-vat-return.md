---
name: czech-republic-vat-return
description: Use this skill whenever asked to prepare, review, or create a Czech Republic VAT return (Priznani k DPH) or VAT Control Statement (Kontrolni hlaseni) for any client. Trigger on phrases like "prepare VAT return", "do the VAT", "fill in DPH", "create the return", "Czech VAT", "kontrolni hlaseni", or any request involving Czech VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Czech VAT classification rules, box mappings, deductibility rules, reverse charge treatment, control statement requirements, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Czech VAT-related work.
---

# Czech Republic VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Czech Republic (Czechia) |
| Jurisdiction Code | CZ |
| Primary Legislation | Zakon o dani z pridane hodnoty (Act No. 235/2004 Coll., VAT Act, as amended) |
| Supporting Legislation | Act No. 280/2009 Coll. (Tax Code); Regulation on Control Statements; Act No. 563/1991 Coll. (Accounting Act) |
| Tax Authority | Financni sprava Ceske republiky (Financial Administration of the Czech Republic) |
| Filing Portal | https://www.mojedane.cz (Electronic submissions portal) |
| Contributor | Auto-generated draft -- requires validation |
| Validated By | Deep research verification, April 2026 |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Status | awaiting-validation |
| Confidence Coverage | Tier 1: box assignment, reverse charge, deductibility blocks, control statement mapping. Tier 2: partial exemption coefficient, mixed-use apportionment, immovable property adjustments. Tier 3: complex group registration, cross-border triangulation, special schemes. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A danovy poradce must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified adviser.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and DIC (tax ID)** [T1] -- CZ + 8-10 digits
2. **VAT registration status** [T1] -- Platce DPH (VAT payer), Identifikovana osoba (identified person for EU purposes only), or Non-registered
3. **Filing frequency** [T1] -- Monthly (default, and mandatory if turnover > CZK 15 million) or Quarterly (if turnover <= CZK 15 million for past 2 calendar years and not newly registered)
4. **Industry/sector** [T2] -- impacts specific reverse charge rules and deductibility
5. **Does the business make exempt supplies?** [T2] -- If yes, partial attribution required (koeficient); reviewer must confirm
6. **Does the business deal in construction?** [T1] -- domestic reverse charge applies to construction services (Sec. 92e)
7. **Excess credit brought forward** [T1] -- from prior period (nadmerny odpocet)
8. **Data box (datova schranka) ID** [T1] -- mandatory for electronic filing

**If any of items 1-3 are unknown, STOP. Do not classify any transactions.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (dan na vystupu -- output VAT) or Purchase (dan na vstupu -- input VAT)
- Salaries, social/health insurance (OSSZ/VZP), income tax, loan repayments, dividends = OUT OF SCOPE
- **Legislation:** VAT Act Sec. 2 (subject of tax), Sec. 13-14 (supply of goods/services)

### 1b. Determine Counterparty Location [T1]
- Czech Republic (domestic): supplier/customer country is CZ
- EU: AT, BE, BG, HR, CY, DK, EE, FI, FR, DE, GR, HU, IE, IT, LV, LT, LU, MT, NL, PL, PT, RO, SK, SI, ES, SE
- Non-EU: everything else
- **Note:** UK is Non-EU post-Brexit. Gibraltar is Non-EU. Channel Islands are Non-EU.

### 1c. Determine VAT Rate [T1]

**As of 1 January 2024 consolidation (Act No. 349/2023 Coll.):**

| Rate | Category | Legislation |
|------|----------|-------------|
| 21% | Standard rate -- most goods and services | VAT Act Sec. 47(1)(a) |
| 12% | Reduced rate (consolidated from former 15% and 10%) -- food, non-alcoholic beverages, water supply, restaurant/catering services, accommodation, books, medicines, medical devices, newspapers, passenger transport, heating, cultural/sporting events, cleaning, hairdressing, minor repairs of clothing/shoes/bicycles, funeral services | VAT Act Sec. 47(1)(b), Annexes 2-4 |
| 0% | Zero-rated -- exports (Sec. 66), intra-EU supplies of goods (Sec. 64) | VAT Act Sec. 63-66 |
| Exempt with credit | International transport of persons | VAT Act Sec. 70 |
| Exempt without credit | Financial services (Sec. 54), insurance (Sec. 55), healthcare (Sec. 58), education (Sec. 57), postal services (Sec. 52), residential rental > 2 years (Sec. 56a), gambling, transfer of immovable property > 5 years after first occupation | VAT Act Sec. 51-62 |

### 1d. Determine Expense Category [T1]
- Capital goods (dlouhodoby majetek): tangible assets with acquisition cost > CZK 80,000 and useful life > 1 year; or immovable property (any value)
- Movable capital goods: 5-year adjustment period (VAT Act Sec. 78(4))
- Immovable property: 10-year adjustment period (VAT Act Sec. 78(3))
- Resale: goods bought to resell
- Overhead/services: everything else
- **Legislation:** VAT Act Sec. 78-78e (adjustment of deduction for capital goods)

---

## Step 2: VAT Return Form Structure (Priznani k DPH) [T1]

**Legislation:** VAT Act Sec. 101; form prescribed by Ministry of Finance.

### Section I -- Taxable Supplies and Output VAT

| Row | Description | Rate | Notes |
|-----|-------------|------|-------|
| Row 1 | Domestic taxable supplies at 21% -- base and VAT | 21% | Standard-rated domestic sales |
| Row 2 | Domestic taxable supplies at 12% -- base and VAT | 12% | Reduced-rated domestic sales |
| Row 3 | Intra-EU acquisition of goods at 21% -- base and VAT | 21% RC | Self-assessed output DPH |
| Row 4 | Intra-EU acquisition of goods at 12% -- base and VAT | 12% RC | Self-assessed output DPH |
| Row 5 | Received services from EU (Sec. 24a) at 21% -- base and VAT | 21% RC | B2B services from EU |
| Row 6 | Received services from EU (Sec. 24a) at 12% -- base and VAT | 12% RC | B2B services from EU |
| Row 7 | Domestic reverse charge received (Sec. 92a) at 21% -- base and VAT | 21% RC | Construction, waste, etc. |
| Row 8 | Domestic reverse charge received (Sec. 92a) at 12% -- base and VAT | 12% RC | Domestic RC at reduced rate |
| Row 9 | Import of services from non-EU at 21% -- base and VAT | 21% RC | Non-EU service import |
| Row 10 | Import of services from non-EU at 12% -- base and VAT | 12% RC | Non-EU at reduced rate |
| Row 11 | Import of goods (Sec. 23(3-4)) at 21% -- base and VAT | 21% | Customs self-assessment |
| Row 12 | Import of goods (Sec. 23(3-4)) at 12% -- base and VAT | 12% | Customs at reduced rate |
| Row 13 | Other taxable supplies with obligation to declare VAT | -- | Special cases |

### Section II -- Other Supplies and Summary

| Row | Description | Notes |
|-----|-------------|-------|
| Row 20 | Intra-EU supply of goods (Sec. 64) | Zero-rated, report on VIES |
| Row 21 | Export of goods (Sec. 66) | Zero-rated export |
| Row 22 | Supply of services to EU person (Sec. 24a, place of supply in other MS) | B2B services to EU |
| Row 23 | Exempt supplies without credit (Sec. 51) | Financial, insurance, education etc. |
| Row 24 | Exempt supplies with credit | International transport |
| Row 25 | Domestic reverse charge supplies made (Sec. 92a) | Seller side of domestic RC |
| Row 26 | Supplies of new means of transport to EU non-taxable person | Special intra-EU rule |

### Section III -- Input VAT Deduction

| Row | Description | Notes |
|-----|-------------|-------|
| Row 40 | Full deduction -- domestic purchases at 21% | Standard-rated input DPH |
| Row 41 | Full deduction -- domestic purchases at 12% | Reduced-rated input DPH |
| Row 42 | Full deduction -- from intra-EU acquisitions at 21% | Mirrors Row 3 output |
| Row 43 | Full deduction -- from intra-EU acquisitions at 12% | Mirrors Row 4 output |
| Row 44 | Full deduction -- from imports at 21% | Mirrors Row 9/11 output |
| Row 45 | Full deduction -- from imports at 12% | Mirrors Row 10/12 output |
| Row 46 | Reduced deduction (partial, koeficient applied) at 21% | For mixed taxable/exempt businesses |
| Row 47 | Reduced deduction (partial, koeficient applied) at 12% | For mixed taxable/exempt businesses |

### Section IV -- Adjustments and Corrections

| Row | Description | Legislation |
|-----|-------------|-------------|
| Row 50 | Correction of deduction (Sec. 74-77) | Error corrections, credit notes |
| Row 51 | Adjustment of deduction for capital goods (Sec. 78-78e) | Change in use proportion |
| Row 52 | Refund of deduction for unpaid invoices (Sec. 74a) | Must reverse if unpaid > 6 months |
| Row 53 | Total output VAT (Section I total) | Sum of all output DPH |
| Row 54 | Total deductions claimed (Section III + IV) | Sum of all input DPH |
| Row 60 | Coefficient (koeficient) for partial deduction | Percentage applied to mixed inputs |

### Section V -- Settlement

| Row | Description | Notes |
|-----|-------------|-------|
| Row 62 | Tax payable (if Row 53 > Row 54) | Pay to Financni sprava |
| Row 63 | Excessive deduction / tax credit (if Row 54 > Row 53) | Refund or carry forward |
| Row 64 | Change in tax payable after adjustments | Corrections from prior periods |
| Row 65 | Credit brought forward from prior period | From previous return |
| Row 66 | Amount payable / credit to carry forward or refund | Final settlement |

---

## Step 3: Transaction Classification Matrix [T1]

### Purchases -- Domestic (Czech Supplier)

| VAT Rate | Category | Input Row | Notes |
|----------|----------|-----------|-------|
| 21% | Overhead/services (full deduction) | Row 40 | Standard domestic purchase |
| 12% | Overhead/services (full deduction) | Row 41 | Food, accommodation, books |
| 21% | Overhead/services (partial deduction) | Row 46 | Mixed taxable/exempt business |
| 12% | Overhead/services (partial deduction) | Row 47 | Mixed taxable/exempt business |
| 21% | Resale | Row 40 | Goods for resale |
| 12% | Resale | Row 41 | Goods for resale at reduced rate |
| Any | Capital > CZK 80,000 | Row 40/41 or 46/47 | Capital goods scheme applies |
| Any | Blocked category | -- | No input VAT (entertainment, gifts) |

### Purchases -- EU Supplier (Reverse Charge)

| Type | Output Row | Input Row | Notes |
|------|-----------|-----------|-------|
| Physical goods at 21% | Row 3 | Row 42 | Intra-EU acquisition |
| Physical goods at 12% | Row 4 | Row 43 | Intra-EU acquisition (reduced) |
| Services (B2B, Sec. 24a) at 21% | Row 5 | Row 42 | EU service reverse charge |
| Services (B2B, Sec. 24a) at 12% | Row 6 | Row 43 | EU service at reduced rate |
| Out-of-scope (wages etc.) | -- | -- | NEVER reverse charge |
| Local consumption (hotel, restaurant abroad) | -- | -- | Foreign VAT at source, not RC |

### Purchases -- Non-EU Supplier (Reverse Charge)

| Type | Output Row | Input Row | Notes |
|------|-----------|-----------|-------|
| Services at 21% | Row 9 | Row 44 | Non-EU service import |
| Services at 12% | Row 10 | Row 45 | Non-EU at reduced rate |
| Physical goods (customs) at 21% | Row 11 | Row 44 | Import via customs |
| Physical goods (customs) at 12% | Row 12 | Row 45 | Import at reduced rate |
| Out-of-scope | -- | -- | NEVER reverse charge |

### Sales -- Domestic

| Rate | Row | Notes |
|------|-----|-------|
| 21% | Row 1 | Standard-rated supply |
| 12% | Row 2 | Reduced-rated supply |
| Exempt with credit | Row 24 | International transport |
| Exempt without credit | Row 23 | Financial, insurance, education |

### Sales -- EU / Non-EU

| Location | Type | Row | Notes |
|----------|------|-----|-------|
| EU B2B goods | Intra-EU supply | Row 20 | Zero-rated, report on VIES |
| EU B2B services | Sec. 24a services | Row 22 | Place of supply in customer MS |
| Non-EU | Export | Row 21 | Zero-rated export |
| Domestic RC supply made | Sec. 92a | Row 25 | Seller side, no VAT charged |

---

## Step 4: Control Statement (Kontrolni Hlaseni) [T1]

**Legislation:** VAT Act Sec. 101c-101i.

The Control Statement is a SEPARATE filing from the VAT return, submitted on the same deadline. It provides transaction-level detail for automated cross-checking by Financni sprava.

### Structure

| Section | Content | Threshold | Detail Level |
|---------|---------|-----------|-------------|
| A.1 | Domestic reverse charge supplies made (matching B.1) | All amounts | Full invoice detail |
| A.2 | Supplies to VAT payers with DIC, single invoice > CZK 10,000 | > CZK 10,000 | Full invoice detail |
| A.3 | Supplies to VAT payers, single invoice <= CZK 10,000 | <= CZK 10,000 | Aggregated totals |
| A.4 | Supplies not fitting A.1-A.3 (B2C, exempt, etc.) | Aggregated | No invoice detail |
| A.5 | Supplies under special schemes | As applicable | Varies |
| B.1 | Domestic reverse charge received | All amounts | Full invoice detail |
| B.2 | Received supplies from VAT payers, single invoice > CZK 10,000 | > CZK 10,000 | Full invoice detail |
| B.3 | Received supplies from VAT payers, single invoice <= CZK 10,000 | <= CZK 10,000 | Aggregated totals |

### Required Data for A.2 / B.2 (Detail Sections)

| Field | Description |
|-------|-------------|
| DIC | Counterparty VAT ID (CZ + digits) |
| Invoice number | Supplier's invoice reference |
| DPPD / DUZP | Date of taxable supply (datum uskutecneni zdanitelneho plneni) |
| Taxable base | Net amount in CZK |
| VAT amount | DPH in CZK |
| Tax rate | 21% or 12% |
| Regime code | Normal / reverse charge / special scheme |

### Penalties for Non-Compliance [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing (voluntary, no summons) | CZK 1,000 | VAT Act Sec. 101h(1)(a) |
| Late filing (after first summons, within 5 days) | CZK 10,000 (CZK 5,000 for sole traders) | VAT Act Sec. 101h(1)(b) |
| Failure after formal request to amend | CZK 30,000 (CZK 15,000 for sole traders) | VAT Act Sec. 101h(1)(c) |
| Complete non-compliance after repeated summons | CZK 50,000 (CZK 25,000 for sole traders) | VAT Act Sec. 101h(1)(d) |
| Mismatch with trading partner (unresolved) | Summons issued, may lead to audit | VAT Act Sec. 101g |

### Key Rules [T1]
- Legal entities (s.r.o., a.s.) MUST file Control Statements monthly regardless of VAT return frequency
- Physical persons (sole traders) file Control Statements with the same frequency as their VAT return
- Mismatches between A.2/B.2 entries of trading partners trigger automated queries ("vyzva")
- Taxpayer has 5 calendar days to respond to a vyzva
- Control Statement filing is MANDATORY -- it is not optional even if no transactions occurred (submit nil return)

---

## Step 5: Reverse Charge Mechanics [T1]

**Legislation:** VAT Act Sec. 24a (EU services), Sec. 25 (intra-EU acquisitions), Sec. 92a-92i (domestic RC).

### Intra-EU Acquisitions of Goods (Sec. 25)
1. Report taxable base and output VAT in Row 3 (21%) or Row 4 (12%)
2. Claim input VAT in Row 42 (21%) or Row 43 (12%)
3. Net effect: zero for fully taxable businesses
4. Report on VIES (Souhrnne hlaseni)

### EU Services Received -- B2B (Sec. 24a)
1. Report taxable base and output VAT in Row 5 (21%) or Row 6 (12%)
2. Claim input VAT in Row 42/43
3. Net effect: zero for fully taxable businesses

### Non-EU Services Received
1. Report in Row 9 (21%) or Row 10 (12%)
2. Claim input VAT in Row 44/45
3. Net effect: zero

### Domestic Reverse Charge (Sec. 92a-92i)

| Supply Type | Section | Legislation | Notes |
|-------------|---------|-------------|-------|
| Construction and assembly work | Sec. 92e | VAT Act Sec. 92e | All construction, incl. subcontractors |
| Supply of waste and scrap | Sec. 92c | VAT Act Sec. 92c | Metals, paper, glass, plastic |
| Investment gold | Sec. 92b | VAT Act Sec. 92b | If seller opts to tax |
| Emission allowances (CO2) | Sec. 92d | VAT Act Sec. 92d | Greenhouse gas allowances |
| Gas and electricity to traders | Sec. 92f | VAT Act Sec. 92f | Wholesale energy |
| Immovable property (in certain cases) | Sec. 92d | VAT Act Sec. 56 | When seller opts to tax |
| Supply of staff for construction | Sec. 92e | VAT Act Sec. 92e | Staff leasing for construction |
| Certain metals (Annex 6) | Sec. 92c | VAT Act Sec. 92c, Annex 6 | Specified metal products |

Domestic reverse charge procedure:
1. Report in Row 7 (21%) or Row 8 (12%) on output side
2. Claim in Row 40/41 on input side
3. Report in Control Statement: seller in A.1, buyer in B.1

### Exceptions to Reverse Charge [T1]
- Out-of-scope categories (wages, bank charges, dividends): NEVER reverse charge
- Local consumption abroad (hotel, restaurant, taxi): NOT reverse charge; foreign VAT paid at source
- EU supplier charged their local VAT > 0%: NOT reverse charge; foreign VAT is part of expense
- Domestic non-construction services: normal VAT applies (not domestic RC)

---

## Step 6: Deductibility Check

### Blocked / Restricted Categories [T1]
**Legislation:** VAT Act Sec. 72-79.

| Category | VAT Recovery | Legislation | Notes |
|----------|-------------|-------------|-------|
| Business entertainment (client hospitality) | 0% | Sec. 72(4) | Gifts and entertainment never deductible |
| Business gifts > CZK 500 per item | 0% | Sec. 72(4) | Items > CZK 500 given free |
| Business gifts <= CZK 500 per item | Deductible | Sec. 72(4) | Small promotional items OK |
| Passenger cars | 100% deductible | Sec. 72 | Czech Republic does NOT block cars (unlike HU, PL, RO) |
| Fuel for business vehicles | 100% deductible | Sec. 72 | No restriction |
| Supplies used for exempt-without-credit activities | 0% | Sec. 72(1) | Financial, insurance, education inputs |
| Supplies for non-economic activity | 0% | Sec. 72(1) | Private use, non-business |
| Unpaid invoices > 6 months past due date | Must reverse | Sec. 74a | Previously claimed deduction reversed |

### Unpaid Invoice Rule (Sec. 74a) [T1]

| Feature | Detail | Legislation |
|---------|--------|-------------|
| Trigger | Invoice unpaid > 6 months after due date | Sec. 74a(1) |
| Action | Must reverse previously claimed input VAT | Sec. 74a(2) |
| Reporting | Report reversal in Row 52 | Sec. 74a(3) |
| Reinstatement | If subsequently paid, deduction can be re-claimed | Sec. 74a(4) |
| Applies to | All invoices from domestic and EU/non-EU suppliers | Sec. 74a |

### Registration-Based Recovery [T1]

| Registration Type | Input VAT Recovery | Legislation |
|-------------------|-------------------|-------------|
| Platce DPH (VAT payer) | Full recovery (subject to rules above) | Sec. 72 |
| Identifikovana osoba (identified person) | NO input VAT recovery (reporting obligations only) | Sec. 6g-6i |
| Non-registered | NO recovery | -- |

### Partial Deduction -- Coefficient (Koeficient) [T2]
**Legislation:** VAT Act Sec. 76.

If business makes both taxable and exempt-without-credit supplies:

`Koeficient = Taxable Supplies / (Taxable Supplies + Exempt Supplies)`

| Rule | Detail | Legislation |
|------|--------|-------------|
| Rounding | Round UP to nearest whole percent | Sec. 76(3) |
| De minimis | If >= 95%, treated as 100% | Sec. 76(4) |
| Provisional | Use prior year coefficient during current year | Sec. 76(5) |
| Annual adjustment | True-up at year-end, adjust in last period | Sec. 76(7) |
| Excluded from calculation | Sale of capital goods, incidental financial transactions | Sec. 76(2) |
| Applied in | Rows 46/47 for purchases used for both taxable and exempt | Sec. 76(1) |

**Flag for reviewer: annual adjustment required. Provisional coefficient used during year.**

---

## Step 7: Key Thresholds

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| VAT registration -- standard | CZK 2,000,000 annual turnover | Sec. 6(1) |
| VAT registration -- immediate (next-day) | CZK 2,536,500 annual turnover | Sec. 6(2) |
| EU SME scheme (from 2025) | EUR 85,000 domestic + EUR 100,000 EU-wide | EU Directive 2020/285 |
| Quarterly filing eligibility | Turnover <= CZK 15,000,000 (previous calendar year) | Sec. 99a |
| Control Statement detail threshold | CZK 10,000 per invoice (A.2/B.2 vs A.3/B.3) | Sec. 101c(1) |
| Business gift deduction block | CZK 500 per item | Sec. 72(4) |
| Capital goods -- movable | > CZK 80,000 acquisition cost (5-year adjustment) | Sec. 78(4) |
| Capital goods -- immovable | Any value (10-year adjustment period) | Sec. 78(3) |
| Unpaid invoice deduction reversal | 6 months past due date | Sec. 74a |
| EU distance selling (B2C) | EUR 10,000 (EU-wide OSS threshold) | EU Directive 2017/2455 |
| Deduction claim deadline | End of 3rd calendar year after right arose | Sec. 73(3) |
| Immovable property exempt period | 5 years from first occupation | Sec. 56(3) |

---

## Step 8: VAT Registration [T1]

| Feature | Detail | Legislation |
|---------|--------|-------------|
| VAT number format | CZ + 8-10 digits | Sec. 4(1) |
| Mandatory registration | CZK 2,000,000 turnover in 12 consecutive months | Sec. 6(1) |
| Registration deadline | 15 days after exceeding threshold | Sec. 6(1) |
| Immediate registration | CZK 2,536,500 -- registered from next day | Sec. 6(2) |
| Voluntary registration | May register at any time | Sec. 6f |
| Identifikovana osoba | For EU transactions only (no input VAT) | Sec. 6g |
| Group registration | Related entities may form VAT group | Sec. 5a-5c |
| Deregistration | After 1 year, if no longer obligated | Sec. 106b |
| Cancellation by authority | If unreachable, non-compliant, or shell entity | Sec. 106 |

---

## Step 9: Filing Deadlines and Penalties

### Filing Deadlines [T1]

| Filing | Period | Deadline | Legislation |
|--------|--------|----------|-------------|
| VAT return (monthly) | Monthly | 25th of following month | Sec. 101(1) |
| VAT return (quarterly) | Quarterly | 25th of month after quarter end | Sec. 101(1) |
| Control Statement (legal entities) | Monthly (always) | 25th of following month | Sec. 101e(1) |
| Control Statement (sole traders, quarterly VAT) | Quarterly | 25th of month after quarter end | Sec. 101e(2) |
| VIES (Souhrnne hlaseni) | Monthly | 25th of following month | Sec. 102(1) |
| VAT payment | Same as return | 25th of following month/quarter | Tax Code Sec. 135 |
| Annual settlement of coefficient | In last period return | With last return of year | Sec. 76(7) |

### Penalties [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing of VAT return | 0.05% of tax per day, max 5% of tax, min CZK 500 | Tax Code Sec. 250 |
| Late payment of VAT | Late interest at repo rate + 8% p.a., from 4th day | Tax Code Sec. 252 |
| Tax shortfall (additional assessment) | 20% of additional tax assessed | Tax Code Sec. 251 |
| Control Statement late (voluntary) | CZK 1,000 | Sec. 101h(1)(a) |
| Control Statement late (after summons) | CZK 10,000 / CZK 5,000 (sole trader) | Sec. 101h(1)(b) |
| Control Statement failure (after formal request) | CZK 30,000 / CZK 15,000 (sole trader) | Sec. 101h(1)(c) |
| Control Statement repeated non-compliance | CZK 50,000 / CZK 25,000 (sole trader) | Sec. 101h(1)(d) |
| Failure to register for VAT | Back-assessment + 20% penalty | Tax Code Sec. 251 |
| VIES late/missing | Up to CZK 50,000 | Tax Code Sec. 247a |

---

## Step 10: Derived Box Calculations [T1]

```
Row 53 = Sum of output VAT from Rows 1-13 (VAT columns only)
Row 54 = Sum of Rows 40-47 + Rows 50-52

IF Row 53 > Row 54 THEN
  Row 62 = Row 53 - Row 54  -- Tax Payable
  Row 63 = 0
ELSE
  Row 62 = 0
  Row 63 = Row 54 - Row 53  -- Excessive Deduction (Credit)
END

Row 66 = Row 62 - Row 65  -- Final payable after credit brought forward
```

---

## Step 11: Edge Case Registry

### EC1 -- Hotel in another EU country [T1]
**Situation:** Czech VAT payer pays for hotel in Austria. Invoice shows Austrian 13% VAT.
**Resolution:** NOT reverse charge. Austrian VAT was charged and paid at source. No Czech VAT entries. Austrian VAT is irrecoverable cost.
**Legislation:** VAT Act Sec. 10 -- place of supply for accommodation is where property is located.

### EC2 -- SaaS subscription from US provider [T1]
**Situation:** Monthly charge from US company (e.g., AWS, Notion), no VAT on invoice.
**Resolution:** Import of services from non-EU. Report in Row 9 (base + 21% output VAT) and claim in Row 44 (input VAT). Net effect zero.
**Legislation:** VAT Act Sec. 9(1) -- place of supply for B2B services is customer's establishment.

### EC3 -- Domestic construction services (reverse charge, Sec. 92e) [T1]
**Situation:** Czech subcontractor provides construction work to Czech VAT payer. CZK 500,000.
**Resolution:** Supplier invoices without VAT (reverse charge). Buyer reports in Row 7 (base CZK 500K + output VAT CZK 105K at 21%) and Row 40 (input VAT CZK 105K). Control Statement: seller in A.1, buyer in B.1.
**Legislation:** VAT Act Sec. 92e.

### EC4 -- Invoice unpaid for 7 months past due [T1]
**Situation:** Company claimed input VAT on an invoice. Invoice has been unpaid for 7 months past due date.
**Resolution:** Must reverse the previously claimed input VAT deduction. Report reversal in Row 52. If invoice is subsequently paid, deduction can be reinstated.
**Legislation:** VAT Act Sec. 74a.

### EC5 -- Business entertainment (client dinner, blocked) [T1]
**Situation:** Company pays for client entertainment dinner. CZK 3,000 + CZK 630 VAT (21%).
**Resolution:** Input VAT of CZK 630 is NOT deductible. Full CZK 3,630 is a cost. Entertainment is blocked under Sec. 72(4).
**Legislation:** VAT Act Sec. 72(4).

### EC6 -- EU B2B service sale (consulting) [T1]
**Situation:** Czech company provides IT consulting to German client (B2B).
**Resolution:** Report in Row 22 (services to EU person). No output VAT. Customer reverse charges in Germany. Report on VIES (Souhrnne hlaseni).
**Legislation:** VAT Act Sec. 9(1) -- place of supply in customer's MS.

### EC7 -- Intra-EU goods acquisition [T1]
**Situation:** Czech company buys goods from Polish supplier at 0% with PL VAT number.
**Resolution:** Report in Row 3 (base + 21% output VAT) and Row 42 (input VAT). Net effect zero. Report on VIES.
**Legislation:** VAT Act Sec. 25 -- intra-EU acquisition.

### EC8 -- Credit note received [T1]
**Situation:** Supplier issues credit note reducing an earlier invoice.
**Resolution:** Reduce original row values by credit note amount. Report in the period the credit note conditions are met. If original was Row 40, reduce Row 40.
**Legislation:** VAT Act Sec. 42-46 (correction of tax base).

### EC9 -- Capital goods adjustment (change in use) [T2]
**Situation:** Company purchased machinery for CZK 200,000 two years ago with full deduction. Now starts using 30% for exempt activities.
**Resolution:** Adjustment of deduction required under Sec. 78. Reduce deduction proportionally for remaining adjustment period (3 years remaining of 5). Flag for reviewer: confirm usage proportion and adjustment calculation.
**Legislation:** VAT Act Sec. 78-78e.

### EC10 -- Sale of immovable property (within 5 years) [T2]
**Situation:** Company sells a building 3 years after first occupation.
**Resolution:** Within 5 years of first occupation or substantial reconstruction: taxable at 21%. After 5 years: exempt without credit (but seller may opt to tax with buyer's agreement under Sec. 56(5)). Flag for reviewer: confirm occupation date and option-to-tax decision.
**Legislation:** VAT Act Sec. 56(3) and Sec. 56(5).

### EC11 -- Business gift under CZK 500 [T1]
**Situation:** Company distributes promotional pens worth CZK 50 each.
**Resolution:** Input VAT on purchase is deductible (under CZK 500 threshold). No output VAT on distribution if promotional purpose.
**Legislation:** VAT Act Sec. 72(4) -- gifts <= CZK 500 not blocked.

### EC12 -- Passenger car purchase (fully deductible in CZ) [T1]
**Situation:** Czech VAT payer buys a company car for CZK 600,000 + CZK 126,000 DPH (21%).
**Resolution:** Input DPH of CZK 126,000 is FULLY deductible in Czechia (unlike Hungary, Romania, Poland). Row 40 += CZK 126,000. No vehicle restriction in Czech VAT law.
**Legislation:** VAT Act Sec. 72 -- no vehicle-specific block.

### EC13 -- Identified person (identifikovana osoba) receives EU services [T1]
**Situation:** A non-VAT-payer registered only as identified person receives consulting from German supplier.
**Resolution:** Must self-assess output DPH in Row 5 at 21%. But CANNOT claim input DPH (identified persons have no right to deduction). Net: must pay the DPH.
**Legislation:** VAT Act Sec. 6g-6i, Sec. 72(1).

---

## Step 12: VAT Rates -- Detailed Supply Classification [T1]

### 21% Standard Rate (Sec. 47(1)(a))

| Supply Category | Examples |
|----------------|----------|
| General goods | Electronics, furniture, clothing, household items, motor vehicles |
| Professional services | Legal, accounting, consulting, IT, advertising |
| Telecommunications | Mobile, fixed-line, internet (not content) |
| Alcohol | Beer, wine, spirits |
| Tobacco | Cigarettes, cigars |
| Energy (non-household) | Electricity, gas for commercial use |
| Construction materials | Cement, steel, timber |

### 12% Reduced Rate (Sec. 47(1)(b), Annexes 2-4)

| Supply Category | Examples |
|----------------|----------|
| Food and non-alcoholic beverages | All food items, soft drinks, juice, water |
| Restaurant and catering services | Dine-in meals, takeaway food (not alcohol) |
| Accommodation | Hotels, guesthouses, camping, Airbnb |
| Books and periodicals | Printed and electronic books, newspapers, magazines |
| Medicines and medical devices | Prescription and OTC pharmaceuticals, hearing aids |
| Passenger transport | Bus, train, taxi, air (domestic) |
| Water supply | Drinking water distribution |
| Heating | District heating, firewood, pellets |
| Cultural and sporting events | Theatre, concerts, cinema, sports matches |
| Cleaning services | Window cleaning, industrial cleaning |
| Hairdressing | Haircuts and salon services |
| Minor repairs | Clothing, shoes, bicycles, leather goods |
| Funeral services | Cremation, burial, undertaker |
| Cut flowers and plants | Decorative plants, bouquets |

---

## Step 13: Comparison with Malta

| Feature | Czech Republic (CZ) | Malta (MT) |
|---------|---------------------|------------|
| Standard rate | 21% | 18% |
| Reduced rates | 12% (consolidated) | 12%, 7%, 5% |
| Return form | Priznani k DPH (~66 rows) | VAT3 (45 boxes) |
| Control Statement | Kontrolni hlaseni (mandatory, separate filing) | No equivalent |
| Filing frequency | Monthly / Quarterly | Quarterly (Art. 10), Annual (Art. 11) |
| Filing deadline | 25th of following month | 21st of month after quarter (e-filing) |
| Payment deadline | 25th of following month | Same as filing |
| Small enterprise threshold | CZK 2,000,000 (~EUR 80,000) | EUR 35,000 |
| Capital goods movable | > CZK 80,000 (5 years) | > EUR 1,160 gross |
| Capital goods immovable | 10-year adjustment | No specific adjustment period |
| Blocked: passenger cars | NOT blocked (full deduction) | Yes (10th Schedule) |
| Blocked: entertainment | Yes (Sec. 72(4)) | Yes (10th Schedule Item 3(1)(b)) |
| Unpaid invoice reversal | Must reverse after 6 months (Sec. 74a) | No equivalent rule |
| Domestic reverse charge | Construction, waste, gold, emissions, energy, metals | No domestic reverse charge |
| Coefficient de minimis | >= 95% treated as 100% | No de minimis |
| Refund mechanism | Automatic if credit on return | Carry forward / refund request |
| Tax authority | Financni sprava | CFR |
| Filing portal | mojedane.cz | cfr.gov.mt |
| Currency | CZK (Czech Koruna) | EUR |

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
Action Required: Danovy poradce must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to danovy poradce. Document gap.
```

---

## Step 15: Test Suite

### Test 1 -- Standard domestic purchase, 21% VAT [T1]
**Input:** Czech supplier, office equipment, CZK 10,000 net + CZK 2,100 VAT. VAT payer, no exempt activities.
**Expected output:** Row 40 += CZK 2,100. Fully deductible.

### Test 2 -- Import of services from US (SaaS) [T1]
**Input:** US supplier, monthly fee USD 20 (~CZK 460), no VAT. VAT payer.
**Expected output:** Row 9 base = CZK 460, output VAT = CZK 96.60 (21%). Row 44 = CZK 96.60. Net = zero.

### Test 3 -- Domestic reverse charge (construction, Sec. 92e) [T1]
**Input:** Czech subcontractor, construction services CZK 100,000 net. Both parties VAT payers.
**Expected output:** Buyer: Row 7 base = CZK 100,000, output VAT = CZK 21,000. Row 40 = CZK 21,000. Net = zero. Control Statement: B.1 (buyer), A.1 (seller).

### Test 4 -- EU B2B service sale [T1]
**Input:** Czech company invoices Slovak client EUR 1,000 for consulting. B2B.
**Expected output:** Row 22 = CZK equivalent. No output VAT. VIES filing required.

### Test 5 -- Business entertainment (blocked) [T1]
**Input:** Client dinner CZK 5,000 + CZK 1,050 VAT (21%).
**Expected output:** Row 40 += CZK 0. VAT BLOCKED under Sec. 72(4). Full CZK 6,050 is cost.

### Test 6 -- Unpaid invoice reversal (Sec. 74a) [T1]
**Input:** Invoice CZK 50,000 + CZK 10,500 VAT claimed 8 months ago. Still unpaid, 7 months past due.
**Expected output:** Row 52: reverse CZK 10,500 previously claimed.

### Test 7 -- Intra-EU goods acquisition [T1]
**Input:** German supplier, goods EUR 2,000, 0% invoice with DE VAT number.
**Expected output:** Row 3 base = CZK equivalent, output VAT = 21%. Row 42 = same input VAT. Net = zero.

### Test 8 -- Export of goods [T1]
**Input:** Czech company exports to US client, CZK 200,000.
**Expected output:** Row 21 = CZK 200,000. No output VAT. Zero-rated.

### Test 9 -- Passenger car purchase (fully deductible in CZ) [T1]
**Input:** Czech VAT payer buys car CZK 500,000 + CZK 105,000 DPH (21%). Business use.
**Expected output:** Row 40 += CZK 105,000. Fully deductible (no vehicle block in Czech law).

### Test 10 -- Business gift under CZK 500 [T1]
**Input:** Company buys promotional items CZK 400 each + CZK 84 DPH. Distributed to clients.
**Expected output:** Row 40 += CZK 84. Deductible (under CZK 500 threshold).

### Test 11 -- Business gift over CZK 500 (blocked) [T1]
**Input:** Company buys gift hampers CZK 800 each + CZK 168 DPH. Given to clients.
**Expected output:** Row 40 += CZK 0. DPH blocked (gift > CZK 500 under Sec. 72(4)).

### Test 12 -- Identified person receives EU services [T1]
**Input:** Identifikovana osoba receives German consulting EUR 500 (~CZK 12,500).
**Expected output:** Row 5 = CZK 12,500 (base), output DPH = CZK 2,625 (21%). NO input deduction (identified person). Must pay CZK 2,625.

---

## Step 16: Out of Scope -- Direct Tax (Reference Only) [T3]

This skill does not compute income tax. The following is reference information only. Escalate to qualified adviser.

- **Corporate income tax (dan z prijmu pravnickych osob):** 21% flat rate on adjusted profit (Act No. 586/1992 Coll.)
- **Personal income tax (dan z prijmu fyzickych osob):** 15% up to 48x average wage, 23% above (Act No. 586/1992 Coll.)
- **Social insurance (socialni pojisteni):** employer 24.8%, employee 6.5% (OSSZ)
- **Health insurance (zdravotni pojisteni):** employer 9%, employee 4.5% (VZP/other)
- **Road tax (silnicni dan):** based on vehicle type, for business vehicles
- **Real estate tax (dan z nemovitych veci):** annual, based on property area and location

---

## Step 17: Refund Process [T1]

| Feature | Detail | Legislation |
|---------|--------|-------------|
| Automatic refund | If excessive deduction (Row 63 > 0) | Tax Code Sec. 155 |
| Refund timeline | Within 30 days of filing deadline | Tax Code Sec. 155(3) |
| Audit hold | Tax authority may initiate procedure to verify (postupu k odstraneni pochybnosti) | Tax Code Sec. 89-90 |
| Audit extension | Can extend refund by up to 3 months (or longer in complex cases) | Tax Code Sec. 90 |
| Carry forward | Credit can be carried forward indefinitely | Sec. 105(1) |

---

## PROHIBITIONS [T1]

- NEVER let AI guess VAT box assignment -- it is deterministic from transaction facts
- NEVER claim input VAT on business entertainment or gifts > CZK 500 (Sec. 72(4))
- NEVER forget to reverse deduction for invoices unpaid > 6 months (Sec. 74a)
- NEVER omit Control Statement -- it is mandatory alongside the VAT return
- NEVER apply domestic reverse charge to construction work unless both parties are VAT payers (platce DPH)
- NEVER apply reverse charge to out-of-scope categories (wages, dividends, bank charges)
- NEVER apply reverse charge to local consumption services abroad (hotel, restaurant, taxi)
- NEVER allow identified persons (identifikovana osoba) to claim input VAT
- NEVER apply the old 15%/10% rates -- consolidated to 12% from 1 January 2024 (Act No. 349/2023 Coll.)
- NEVER confuse zero-rated (exports/intra-EU, input VAT deductible) with exempt without credit (financial, insurance)
- NEVER file Control Statement with stale data -- mismatches trigger automated queries
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Contribution Notes

This skill covers the Czech Republic's VAT system based on Act No. 235/2004 Coll. as amended. Key distinctive features include: the mandatory Control Statement (Kontrolni hlaseni) alongside the VAT return, the 2024 rate consolidation (15% + 10% merged to 12%), the unpaid invoice reversal rule (Sec. 74a), full deductibility of passenger cars, and extensive domestic reverse charge categories. Validation by a qualified Czech danovy poradce is required before production use.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
