---
name: latvia-vat-return
description: Use this skill whenever asked to prepare, review, or create a Latvian VAT return (PVN deklaracija) for any client. Trigger on phrases like "prepare VAT return", "do the PVN", "fill in PVN1", "create the return", "Latvian VAT", "pievienotas vertibas nodoklis", or any request involving Latvia VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data for Latvian entities. This skill contains the complete Latvian PVN classification rules, row mappings, deductibility rules, reverse charge treatment, capital goods thresholds, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any VAT-related work for Latvia.
---

# Latvia VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Latvia (Latvija) |
| Jurisdiction Code | LV |
| Primary Legislation | Pievienotas vertibas nodokla likums (PVN likums) -- Law on Value Added Tax, as amended |
| Supporting Legislation | EU VAT Directive 2006/112/EC; Cabinet of Ministers Regulations; Likums par nodokliem un nodevam (Law on Taxes and Duties) |
| Tax Authority | Valsts ienemumu dienests (VID -- State Revenue Service) |
| Filing Portal | https://eds.vid.gov.lv (EDS -- Electronic Declaration System) |
| Local Tax Name | Pievienotas vertibas nodoklis (PVN) |
| Return Form | PVN deklaracija (PVN 1 form) |
| Contributor | Awaiting local practitioner |
| Validated By | Claude deep-research cross-check (web-verified 2026-04-10) |
| Validation Date | 2026-04-10 |
| Skill Version | 1.0-draft |
| Status | web-verified |
| Confidence Coverage | Tier 1: row assignment, reverse charge, deductibility blocks, derived calculations. Tier 2: partial exemption pro-rata, luxury vehicle rules, representation expense caps, real estate reverse charge. Tier 3: complex group structures, timber reverse charge edge cases, non-standard supplies, triangulation. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A qualified accountant (zverinats revidents or licensed tax consultant) must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and PVN registration number** [T1] -- LV + 11 digits (e.g., LV12345678901)
2. **VAT registration status** [T1] -- Standard registered or micro-enterprise tax regime or exempt (small business under EUR 50,000)
3. **VAT period** [T1] -- Monthly (intra-EU trade or turnover > EUR 50,000), quarterly (turnover EUR 14,228.72 - EUR 50,000), or bi-annual (turnover < EUR 14,228.72)
4. **Industry/sector** [T2] -- impacts deductibility and exempt supply status
5. **Does the business make exempt supplies?** [T2] -- If yes, partial attribution required (healthcare, financial services, education, insurance, real estate)
6. **Does the business trade goods for resale?** [T1] -- impacts classification
7. **Excess credit brought forward** [T1] -- from prior period
8. **Does the business have vehicles valued over EUR 50,000 (pre-June 2023) or EUR 75,000 (post-June 2023)?** [T2] -- luxury vehicle restrictions apply
9. **Does the business engage in timber/forestry transactions?** [T1] -- domestic reverse charge applies
10. **First 6 months after registration?** [T1] -- mandatory monthly filing regardless of turnover

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until confirmed.**

---

## VAT Return Form Structure (PVN 1 -- PVN Deklaracija) [T1]

The Latvian PVN 1 form is filed via EDS. Every field on the official form is listed below.

### Part A -- Output PVN (Apreikinatajs nodoklis)

| Row | Field Description | Rate / Basis | Legislation |
|-----|-------------------|--------------|-------------|
| 40 | Domestic taxable supplies at 21% -- taxable base | 21% standard rate | PVN likums Section 41(1) |
| 41 | PVN amount on Row 40 | Calculated at 21% | PVN likums Section 41(1) |
| 42 | Domestic taxable supplies at 12% -- taxable base | 12% reduced rate | PVN likums Section 41(2) |
| 43 | PVN amount on Row 42 | Calculated at 12% | PVN likums Section 41(2) |
| 44 | Domestic taxable supplies at 5% -- taxable base | 5% super-reduced rate | PVN likums Section 41(3) |
| 45 | PVN amount on Row 44 | Calculated at 5% | PVN likums Section 41(3) |
| 46 | Intra-Community supply of goods (exempt with credit) -- base | 0% | PVN likums Section 43 |
| 47 | Export of goods outside EU -- base | 0% | PVN likums Section 44 |
| 48 | Exempt supplies without right of deduction -- base | Exempt | PVN likums Section 52 |
| 49 | Intra-Community acquisitions of goods -- base | Self-assessed | PVN likums Section 32 |
| 50 | PVN amount on Row 49 (self-assessed) | At 21% (or applicable rate) | PVN likums Section 32 |
| 51 | Services received from EU taxable persons (reverse charge) -- base | Self-assessed | PVN likums Section 33 |
| 52 | PVN amount on Row 51 (self-assessed) | At 21% | PVN likums Section 33 |
| 53 | Services/goods received from non-EU (reverse charge) -- base | Self-assessed | PVN likums Section 34 |
| 54 | PVN amount on Row 53 (self-assessed) | At 21% | PVN likums Section 34 |
| 55 | Domestic reverse charge supplies received -- base | Self-assessed | PVN likums Section 141 |
| 56 | PVN amount on Row 55 (self-assessed) | At 21% | PVN likums Section 141 |
| 57 | Total output PVN | Sum of all output PVN rows | Derived |

### Part B -- Input PVN (Atskaitamais prieksnodoklis)

| Row | Field Description | Notes | Legislation |
|-----|-------------------|-------|-------------|
| 60 | Input PVN on domestic purchases | Standard domestic input | PVN likums Section 92 |
| 61 | Input PVN on intra-Community acquisitions | Reverse charge -- EU goods | PVN likums Section 92(2) |
| 62 | Input PVN on services from EU (reverse charge) | Reverse charge -- EU services | PVN likums Section 92(2) |
| 63 | Input PVN on non-EU purchases (reverse charge services) | Reverse charge -- non-EU | PVN likums Section 92(3) |
| 64 | Input PVN on imports (customs) | VAT paid at customs (SAD/C88) | PVN likums Section 92(4) |
| 65 | Input PVN on domestic reverse charge | Timber, scrap metal, construction, CO2 | PVN likums Section 92(5) |
| 66 | Adjustment of input PVN | Annual adjustments, corrections, capital goods | PVN likums Section 100 |
| 67 | Total deductible input PVN | Sum of Rows 60-66 | Derived |

### Part C -- PVN Liability (Nodokla samaksa/parmaksa)

| Row | Field Description | Calculation | Legislation |
|-----|-------------------|-------------|-------------|
| 70 | PVN payable | Row 57 - Row 67, if positive | PVN likums Section 111 |
| 71 | PVN overpayment / refund | Row 67 - Row 57, if positive | PVN likums Section 112 |

### Annexes

| Annex | Description | Threshold | Legislation |
|-------|-------------|-----------|-------------|
| PVN 1-I | Domestic input PVN detail (purchases by supplier) | EUR 150 per supplier per period | PVN likums Section 113 |
| PVN 1-II | Intra-Community acquisitions detail | All EU acquisitions | PVN likums Section 113 |
| PVN 1-III | Domestic output PVN detail (sales by customer) | EUR 150 per customer per period | PVN likums Section 113 |
| PVN 2 | EU Sales List (ES precu piegazu/pakalpojumu parskats) | All intra-EU B2B supplies | PVN likums Section 114 |

---

## Transaction Classification Matrix [T1]

### 1a. Determine Transaction Type [T1]

- Sale (output PVN / apreikinatajs nodoklis) or Purchase (input PVN / prieksnodoklis)
- Salaries, tax payments, loan repayments, dividends, bank charges, equity contributions = OUT OF SCOPE (never on PVN declaration)
- **Legislation:** PVN likums Section 1 (scope), Section 2 (definitions)

### 1b. Determine Counterparty Location [T1]

- Latvia (domestic): supplier/customer country is LV
- EU: AT, BE, BG, HR, CY, CZ, DK, EE, FI, FR, DE, GR, HU, IE, IT, LT, LU, MT, NL, PL, PT, RO, SK, SI, ES, SE
- Non-EU: everything else (US, UK, AU, CH, NO, etc.)
- **Note:** UK is Non-EU post-Brexit. Norway, Switzerland, Iceland are Non-EU (EEA but not EU VAT area).

### 1c. Classification Lookup -- Domestic Purchases [T1]

| VAT Rate | Category | PVN Input Row | Notes |
|----------|----------|---------------|-------|
| 21% | Overhead / services | 60 | Standard domestic input |
| 12% | Reduced rate goods (food, pharma, accommodation) | 60 | Reduced rate input |
| 5% | Super-reduced (books, media) | 60 | Super-reduced input |
| 0% | Zero-rated (exempt with credit) | -- | No input PVN to claim |
| 0% | Exempt without credit | -- | No input PVN; no entry |
| Any | Standard passenger vehicle (mixed use, value <= threshold) | 60 (at 50%) | 50% restriction |
| Any | Luxury vehicle (> EUR 50,000 pre-Jun 2023 / > EUR 75,000 post-Jun 2023) | -- | 0% recovery, fully blocked |

### 1d. Classification Lookup -- EU Purchases (Reverse Charge) [T1]

| Type | Acquisition Row | Output PVN Row | Input PVN Row | Notes |
|------|----------------|----------------|---------------|-------|
| Physical goods | 49 | 50 | 61 | Self-assess at 21% |
| Services (B2B) | 51 | 52 | 62 | Self-assess at 21% |
| Out-of-scope (wages, etc.) | -- | -- | -- | NEVER reverse charge |
| Local consumption (hotel/restaurant/taxi abroad) | -- | -- | -- | Foreign VAT paid at source |

### 1e. Classification Lookup -- Non-EU Purchases (Reverse Charge) [T1]

| Type | Acquisition Row | Output PVN Row | Input PVN Row | Notes |
|------|----------------|----------------|---------------|-------|
| Services (B2B) | 53 | 54 | 63 | Self-assess at 21% |
| Physical goods (imported) | -- | -- | 64 | VAT paid at customs (SAD) |
| Out-of-scope | -- | -- | -- | NEVER reverse charge |
| Local consumption abroad | -- | -- | -- | Foreign PVN irrecoverable |

### 1f. Classification Lookup -- Sales [T1]

| Type | Rate | PVN Output Row | PVN in Row 57 | Notes |
|------|------|----------------|---------------|-------|
| Domestic standard | 21% | 40 / 41 | Yes | PVN likums Section 41(1) |
| Domestic reduced (food, pharma, accommodation) | 12% | 42 / 43 | Yes | PVN likums Section 41(2) |
| Domestic super-reduced (books, media) | 5% | 44 / 45 | Yes | PVN likums Section 41(3) |
| Export (non-EU) | 0% | 47 | No | PVN likums Section 44 |
| Intra-EU goods (B2B) | 0% | 46 | No | Report on PVN 2 |
| Intra-EU services (B2B) | 0% | 46 | No | Report on PVN 2 |
| Exempt without credit | 0% | 48 | No | Input PVN NOT deductible |

---

## VAT Rates -- Complete Schedule [T1]

**Legislation:** PVN likums Section 41 and Annexes.

| Rate | Description | Specific Supplies | Legislation |
|------|-------------|-------------------|-------------|
| 21% | Standard rate | Most goods and services not listed elsewhere | PVN likums Section 41(1) |
| 12% | Reduced rate | Foodstuffs (defined list in Cabinet Regulation), pharmaceutical products, medical devices, hotel accommodation, domestic passenger transport, baby products (nappies, car seats), fresh fruits and vegetables | PVN likums Section 41(2); Cabinet Regulation No. 255 |
| 5% | Super-reduced rate | Books (printed and electronic) in Latvian and other specified languages, non-periodical publications, periodical publications, specified fresh produce (certain categories) | PVN likums Section 41(3) |
| 0% | Zero rate | Intra-EU supplies of goods to VAT-registered recipients, exports of goods outside EU, international transport of passengers and goods, supplies to diplomatic missions, supplies to NATO forces | PVN likums Sections 43-44 |
| Exempt | Exempt without credit | Financial and insurance services, healthcare, education (accredited institutions), postal services (universal service), immovable property (unless option to tax), lottery and gambling, cultural services by public bodies | PVN likums Section 52 |

### Rate History (Recent Changes)

| Date | Change | Legislation |
|------|--------|-------------|
| 1 January 2018 | Reduced rate for accommodation decreased from 12% to 5% (temporary) | PVN likums transitional provision |
| 1 January 2024 | Accommodation rate restored to 12% | PVN likums amendment |
| 1 January 2025 | Baby products added to 12% reduced rate | PVN likums amendment |
| 1 January 2026 | Fresh fruits and vegetables permanently at 12%; books and media at 5% confirmed | PVN likums amendment |

**IMPORTANT:** When processing transactions, always check the invoice date to determine the applicable rate. Transitional rules per PVN likums Section 176 apply at rate change boundaries.

---

## Blocked Input Tax -- Complete List [T1]

**Legislation:** PVN likums Sections 92-100 (input tax deduction restrictions); Uznemumu ienakuma nodokla likums (Corporate Income Tax Law).

| Category | Recovery % | Legislation | Notes |
|----------|------------|-------------|-------|
| Passenger vehicles -- mixed business/private use (value <= luxury threshold) | 50% | PVN likums Section 100(5) | Applies to purchase/lease AND all running costs |
| Passenger vehicles -- luxury (value > EUR 50,000 pre-June 2023 / > EUR 75,000 post-June 2023 excl. VAT) | 0% | PVN likums Section 100(6) | ALL costs non-business; 0% PVN recovery; subject to 20% CIT on deemed personal benefit |
| Representation expenses (reprezentacijas izdevumi) | Limited | PVN likums Section 100(7); CIT Law Section 8 | PVN recovery limited proportionally; CIT: 40% deductible, capped at 5% of gross wages |
| Entertainment expenses (izklaides izdevumi) | 0% | PVN likums Section 100(7) | Fully blocked for PVN purposes |
| Personal use goods and services | 0% | PVN likums Section 100(1) | Any item for private consumption of owner/employees |
| Goods/services used solely for exempt supplies | 0% | PVN likums Section 92(3) | Healthcare, education, financial services |
| Alcohol (unless for resale or hospitality business) | 0% | PVN likums Section 100(8) | Exception: restaurants, bars, retailers |
| Tobacco (unless for resale) | 0% | PVN likums Section 100(8) | Exception: retailers |
| Residential property costs (unless for taxable rental) | 0% | PVN likums Section 100(9) | Unless property used for taxable supply |
| Gifts exceeding EUR 15 per item | 0% | PVN likums Section 100(10) | Business gifts under EUR 15 deductible |

### Passenger Vehicle -- Detailed Rules [T1]

**Legislation:** PVN likums Section 100(5)-(6); CIT Law Section 8(6).

| Scenario | Input PVN Recovery | PVN Row | CIT Treatment |
|----------|--------------------|---------|---------------|
| Standard vehicle, mixed use (value <= threshold) | 50% | 60 (at 50%) | Vehicle operating costs partially deductible |
| Standard vehicle, 100% business use (documented) | 100% | 60 | Full deduction with documentation [T2] |
| Luxury vehicle (value > threshold) | 0% | -- | All costs = non-business expense; 20% CIT payable |
| Fuel for mixed-use standard vehicle | 50% | 60 (at 50%) | Follows vehicle rule |
| Fuel for luxury vehicle | 0% | -- | 20% CIT on total cost |
| Maintenance/repairs for standard vehicle | 50% | 60 (at 50%) | Follows vehicle rule |
| Maintenance/repairs for luxury vehicle | 0% | -- | 20% CIT on total cost |
| Commercial vehicles (vans, trucks > 3,500 kg) | 100% | 60 | Not subject to restrictions |
| Taxis (licensed taxi service) | 100% | 60 | Full deduction |
| Driving school vehicles | 100% | 60 | Full deduction |
| Car rental fleet (rental as primary business) | 100% | 60 | Full deduction |
| Emergency vehicles (ambulance, fire) | 100% | 60 | Full deduction |

### Luxury Vehicle Threshold Detail [T1]

| Period | Threshold (excl. VAT) | Legislation |
|--------|-----------------------|-------------|
| Before 1 June 2023 | EUR 50,000 | PVN likums Section 100(6) (old) |
| From 1 June 2023 | EUR 75,000 | PVN likums Section 100(6) (amended) |

**Note:** For vehicles acquired before 1 June 2023, the EUR 50,000 threshold continues to apply. The EUR 75,000 threshold applies only to vehicles acquired on or after 1 June 2023.

---

## Registration [T1]

### Mandatory Registration Threshold

| Criterion | Value | Legislation |
|-----------|-------|-------------|
| Annual taxable turnover threshold | EUR 50,000 | PVN likums Section 61 |
| Registration deadline after threshold exceeded | Within 15 days | PVN likums Section 62 |
| Penalty for late registration | Fine per Likums par nodokliem un nodevam | LNN Section 34 |

### VAT Number Format

| Element | Format |
|---------|--------|
| Country prefix | LV |
| Digits | 11 digits |
| Example | LV12345678901 |
| VIES validation | Required for intra-EU transactions |

### Voluntary Registration [T1]

- Businesses below EUR 50,000 may register voluntarily (PVN likums Section 63)
- Must remain registered for at least 1 year
- Voluntary registration grants full input PVN deduction rights (subject to restrictions)

### Small Business / Micro-Enterprise Regime [T1]

Latvia has a micro-enterprise tax regime (mikrouznemumu nodoklis):
- Micro-enterprise tax rate: 25% of turnover (from 2024)
- Micro-enterprises paying micro-enterprise tax CANNOT register for PVN
- If turnover exceeds EUR 50,000, must exit micro-enterprise regime and register for PVN
- Micro-enterprise tax replaces PVN, CIT, PIT, and social contributions
- **Legislation:** Mikrouznemumu nodokla likums (Micro-Enterprise Tax Law)

Businesses below EUR 50,000 that are not in micro-enterprise regime are simply not required to register. If not registered:
- Cannot charge PVN on supplies
- Cannot recover input PVN
- No PVN declaration filing obligation

### Non-Resident Registration [T2]

- Non-established taxable persons making taxable supplies in Latvia must register for PVN or appoint a fiscal representative (PVN likums Section 65)
- EU businesses can register directly
- Non-EU businesses must appoint a fiscal representative
- **Flag for reviewer: confirm registration requirements and fiscal representative obligations**

---

## Filing Deadlines and Penalties [T1]

### Filing Schedule

| Form | Period | Deadline | Legislation |
|------|--------|----------|-------------|
| PVN 1 (VAT return) -- monthly filer | Monthly | 20th of month following tax period | PVN likums Section 116 |
| PVN 1 -- quarterly filer | Quarterly | 20th of month following quarter end | PVN likums Section 116 |
| PVN 1 -- bi-annual filer | Half-yearly | 20th of month following half-year end | PVN likums Section 116 |
| PVN 1-I (domestic input detail) | Same as PVN 1 | Same as PVN 1 | PVN likums Section 113 |
| PVN 1-II (EU acquisitions detail) | Same as PVN 1 | Same as PVN 1 | PVN likums Section 113 |
| PVN 1-III (domestic output detail) | Same as PVN 1 | Same as PVN 1 | PVN likums Section 113 |
| PVN 2 (EC Sales List) | Monthly | 20th of month following period | PVN likums Section 114 |
| Intrastat (arrivals) | Monthly | 10th working day of following month | CSB (Central Statistical Bureau) |
| Intrastat (dispatches) | Monthly | 10th working day of following month | CSB |

**Payment deadline:** Same as filing deadline. Electronic filing via EDS is mandatory for all PVN-registered taxpayers.

### Filing Frequency Determination [T1]

| Annual Turnover | Filing Frequency | Legislation |
|-----------------|------------------|-------------|
| > EUR 50,000 or intra-EU trade | Monthly | PVN likums Section 116(1) |
| EUR 14,228.72 to EUR 50,000 | Quarterly | PVN likums Section 116(2) |
| < EUR 14,228.72 | Bi-annual (half-yearly) | PVN likums Section 116(3) |
| First 6 months after new registration | Monthly (mandatory) | PVN likums Section 116(4) |

### Penalties

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing of PVN declaration | Warning or fine EUR 30 - EUR 700 | LNN Section 34; LAPK Section 159.8 |
| Late payment of PVN | Late payment interest at 0.05% per day | LNN Section 29 |
| Failure to register when required | Fine per administrative violation procedure | LNN Section 34 |
| Incorrect PVN declaration (negligent) | Fine up to EUR 700 | LAPK Section 159.8 |
| Incorrect PVN declaration (intentional / tax evasion) | Criminal liability possible | Kriminallikums Section 218 |
| Failure to submit annexes | Fine EUR 30 - EUR 350 | LAPK Section 159.8 |
| Missing PVN 2 (EC Sales List) | Fine EUR 30 - EUR 350 | LAPK Section 159.8 |

### Refund Timeline [T1]

- Standard refund: within 30 calendar days of filing (PVN likums Section 112(1))
- If VID initiates an audit, refund may be delayed up to 90 days
- If taxpayer has tax debts, refund is offset against debts first (LNN Section 28)
- New registrants: refund may be withheld for up to 60 days during first year

---

## Reverse Charge -- Complete Rules [T1]

### Intra-Community Acquisitions (EU) [T1]

**Legislation:** PVN likums Sections 32-33.

| Step | Action | PVN Row |
|------|--------|---------|
| 1 | Report net amount as acquisition base | Row 49 (goods) or Row 51 (services) |
| 2 | Self-assess output PVN at 21% | Row 50 (goods) or Row 52 (services) |
| 3 | Claim input PVN at 21% | Row 61 (goods) or Row 62 (services) |
| 4 | Net effect for fully taxable business | Zero |

### Non-EU Services (Reverse Charge) [T1]

**Legislation:** PVN likums Section 34.

| Step | Action | PVN Row |
|------|--------|---------|
| 1 | Report net amount as acquisition base | Row 53 |
| 2 | Self-assess output PVN at 21% | Row 54 |
| 3 | Claim input PVN at 21% | Row 63 |
| 4 | Net effect for fully taxable business | Zero |

### Physical Goods Imports (Non-EU) [T1]

**Legislation:** PVN likums Section 36.

Physical goods imported from non-EU countries are subject to import PVN at customs (SAD/C88 document). This is NOT reverse charge.

| Step | Action | PVN Row |
|------|--------|---------|
| 1 | PVN assessed and paid at customs | -- |
| 2 | Claim input PVN from customs document | Row 64 |

### Domestic Reverse Charge [T1]

**Legislation:** PVN likums Section 141.

Latvia applies domestic reverse charge for the following:

| Supply Type | Notes | Legislation |
|-------------|-------|-------------|
| Timber and timber-related services | Extended through 31 December 2026 | PVN likums Section 141(1)(1); Cabinet Reg. extended |
| Scrap metal (ferrous and non-ferrous) | Permanent provision | PVN likums Section 141(1)(2) |
| Construction services (to VAT-registered persons) | Applies to construction and demolition | PVN likums Section 141(1)(3) |
| CO2 emission allowances (EU ETS) | Permanent provision | PVN likums Section 141(1)(4) |
| Supply of immovable property (where seller opts to tax) | Seller exercises option to apply PVN | PVN likums Section 141(1)(5) |
| Household appliances and electronics (specific categories) | Where invoice > EUR 10,000 | PVN likums Section 141(1)(6) |
| Cereals and industrial crops (temporary measure) | Periodic extension | PVN likums Section 141(1)(7) |

### Exceptions to Reverse Charge [T1]

- Out-of-scope categories (wages, bank charges, dividends, equity): NEVER reverse charge
- Local consumption abroad (hotel, restaurant, taxi, conference): NOT reverse charge -- foreign VAT paid at source
- EU supplier charged their local VAT > 0%: NOT reverse charge -- foreign VAT is irrecoverable cost
- B2C supplies: NOT reverse charge

---

## Derived Box Calculations [T1]

```
Total Output PVN (Row 57) = Row 41 + Row 43 + Row 45 + Row 50 + Row 52 + Row 54 + Row 56

Total Input PVN (Row 67) = Row 60 + Row 61 + Row 62 + Row 63 + Row 64 + Row 65 + Row 66

IF Row 57 > Row 67 THEN
  Row 70 = Row 57 - Row 67  -- Tax Payable
  Row 71 = 0
ELSE
  Row 70 = 0
  Row 71 = Row 67 - Row 57  -- Overpayment / Refund
END
```

---

## Key Thresholds [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory PVN registration | EUR 50,000 annual taxable turnover | PVN likums Section 61 |
| Monthly filing required | Intra-EU trade or turnover > EUR 50,000 | PVN likums Section 116(1) |
| Quarterly filing | Turnover EUR 14,228.72 - EUR 50,000 | PVN likums Section 116(2) |
| Bi-annual filing | Turnover < EUR 14,228.72 | PVN likums Section 116(3) |
| First 6 months after registration | Monthly filing mandatory | PVN likums Section 116(4) |
| EU distance selling threshold (OSS) | EUR 10,000/calendar year (all EU combined) | PVN likums Section 64; EU Directive Art. 34 |
| Luxury vehicle threshold (pre-June 2023) | EUR 50,000 excl. VAT | PVN likums Section 100(6) |
| Luxury vehicle threshold (post-June 2023) | EUR 75,000 excl. VAT | PVN likums Section 100(6) amended |
| PVN 1-I / 1-III detail threshold | EUR 150 per partner per period | PVN likums Section 113 |
| Business gift deductibility | EUR 15 per item | PVN likums Section 100(10) |
| Domestic reverse charge -- electronics | EUR 10,000 per invoice | PVN likums Section 141(1)(6) |
| Intrastat arrivals (2026) | EUR 350,000 | CSB regulation |
| Intrastat dispatches (2026) | EUR 200,000 | CSB regulation |
| Micro-enterprise turnover limit | EUR 50,000 | Mikrouznemumu nodokla likums |

---

## Partial Exemption (PVN likums Section 97) [T2]

**Legislation:** PVN likums Sections 97-100.

If a business makes both taxable and exempt supplies:

```
Recovery % = (Taxable Supplies / Total Supplies) * 100
```

Rules:
- Pro-rata calculated based on previous year's ratio as provisional rate
- Annual adjustment required at year-end based on actual current year ratio
- Directly attributable costs: allocated 100% to taxable or 0% to exempt
- Mixed costs: allocated using the pro-rata percentage
- Capital goods adjustment period: 10 years for immovable property; 5 years for other capital goods
- De minimis: if exempt turnover is less than 5% of total, 100% recovery may be permitted [T2]
- Row 66 used for annual adjustments

**Flag for reviewer: pro-rata calculation must be confirmed by qualified accountant. Annual adjustment is mandatory. Capital goods scheme adjustments must be tracked separately.**

---

## Edge Case Registry

### EC1 -- EU hotel / restaurant / taxi booked abroad [T1]
**Situation:** PVN-registered client pays for hotel in Estonia. Invoice shows Estonian VAT at 13%.
**Resolution:** NOT reverse charge. Foreign VAT was charged and paid at source. No PVN rows. Estonian VAT is an irrecoverable cost embedded in the expense. Treat as gross overhead in P&L.
**Legislation:** PVN likums Section 20 -- place of supply for accommodation is where property is located.

### EC2 -- Subscription software from non-EU provider (e.g., AWS, Microsoft 365) [T1]
**Situation:** Monthly charge from US company, no VAT shown on invoice.
**Resolution:** Reverse charge applies. Row 53 (net base) / Row 54 (output PVN at 21%) / Row 63 (input PVN at 21%). Net effect zero for fully taxable PVN-registered business.
**Legislation:** PVN likums Section 19(3) -- B2B electronic services place of supply is customer's country.

### EC3 -- Timber supply (domestic reverse charge) [T1]
**Situation:** Latvian company supplies timber to another LV PVN-registered business.
**Resolution:** Domestic reverse charge (extended through 31 December 2026). Supplier invoices without PVN (must note "PVN apgriesta iekasesana" on invoice). Buyer reports Row 55 (base) / Row 56 (output PVN) and Row 65 (input PVN).
**Legislation:** PVN likums Section 141(1)(1); Cabinet Regulation extension.

### EC4 -- Luxury vehicle purchase (blocked) [T1]
**Situation:** Client purchases car worth EUR 80,000 excl. VAT (acquired after June 2023).
**Resolution:** Exceeds EUR 75,000 threshold. ALL costs are non-business expenses. NO input PVN recovery (0%). Subject to 20% CIT on the expense amount as deemed personal benefit.
**Legislation:** PVN likums Section 100(6); CIT Law Section 8(6).

### EC5 -- Standard vehicle, mixed use (50% restriction) [T1]
**Situation:** Client purchases car worth EUR 30,000 excl. VAT + PVN EUR 6,300 (21%), for mixed business/private use.
**Resolution:** Input PVN deductible at 50% only. Row 60 includes EUR 3,150 (50% of EUR 6,300). All running costs also at 50%.
**Legislation:** PVN likums Section 100(5).

### EC6 -- Representation expenses [T2]
**Situation:** Client hosts business dinner for clients at a Riga restaurant, EUR 500 gross.
**Resolution:** Representation expenses have limited PVN recovery. CIT: 40% deductible, capped at 5% of gross employee wages for the year. PVN: recovery proportional to CIT-deductible share. Flag for reviewer: confirm exact PVN treatment, calculate wage-based cap, differentiate from entertainment (which is fully blocked).
**Legislation:** PVN likums Section 100(7); CIT Law Section 8(3).

### EC7 -- Credit notes received [T1]
**Situation:** Client receives a credit note from a Latvian supplier for returned goods.
**Resolution:** Reverse the original entry. Reduce Row 60 by the PVN amount on the credit note. Net figures are reported.
**Legislation:** PVN likums Section 95.

### EC8 -- EU B2B sale of goods [T1]
**Situation:** PVN-registered client sells goods to Lithuanian company EUR 5,000, 0% PVN, Lithuanian VAT number verified on VIES.
**Resolution:** Row 46 = EUR 5,000. No output PVN. Report on PVN 2 (EC Sales List). Proof of transport required.
**Legislation:** PVN likums Section 43.

### EC9 -- Import of goods at customs [T2]
**Situation:** Client imports goods from China. PVN paid to customs on SAD document.
**Resolution:** Input PVN from customs document in Row 64. Flag for reviewer: confirm customs declaration (SAD/C88) matches invoice and customs value includes correct adjustments (freight, insurance, duties).
**Legislation:** PVN likums Section 36; Section 92(4).

### EC10 -- Construction services (domestic reverse charge) [T1]
**Situation:** Latvian construction company provides services to another LV PVN-registered business.
**Resolution:** Domestic reverse charge applies. Supplier invoices without PVN. Buyer reports Row 55 (base) / Row 56 (output PVN at 21%) / Row 65 (input PVN at 21%). Net effect zero.
**Legislation:** PVN likums Section 141(1)(3).

### EC11 -- Immovable property sale with option to tax [T2]
**Situation:** Client sells commercial property. Default treatment is PVN-exempt. Seller has exercised option to tax.
**Resolution:** Domestic reverse charge applies when seller opts to tax. Buyer self-assesses PVN in Row 55/56/65. Flag for reviewer: confirm option to tax was properly notified to VID before transaction date.
**Legislation:** PVN likums Section 141(1)(5); Section 52(2).

### EC12 -- Micro-enterprise attempting PVN registration [T1]
**Situation:** Client is under micro-enterprise tax regime and wants to register for PVN.
**Resolution:** Micro-enterprises CANNOT register for PVN. Must exit micro-enterprise regime first. If turnover exceeds EUR 50,000, automatic exit from micro regime and mandatory PVN registration.
**Legislation:** Mikrouznemumu nodokla likums Section 6; PVN likums Section 61.

### EC13 -- Bad debt relief [T2]
**Situation:** Client has unpaid sales invoice older than 6 months.
**Resolution:** Latvia allows PVN bad debt relief after debtor is declared insolvent or debt is written off per CIT requirements. Output PVN previously declared can be adjusted downward. Flag for reviewer: confirm insolvency proceedings or write-off criteria are met.
**Legislation:** PVN likums Section 105.

### EC14 -- Scrap metal purchase (domestic reverse charge) [T1]
**Situation:** PVN-registered client purchases scrap metal from another Latvian company, EUR 3,000, invoice shows 0% PVN.
**Resolution:** Domestic reverse charge. Self-assess output PVN at 21% in Row 55/56 = EUR 630. Input PVN in Row 65 = EUR 630. Net = zero.
**Legislation:** PVN likums Section 141(1)(2).

### EC15 -- Cereals / industrial crops (domestic reverse charge) [T1]
**Situation:** PVN-registered agricultural trader sells cereals to another LV PVN-registered business, EUR 15,000.
**Resolution:** Domestic reverse charge applies (temporary measure, periodically extended). Supplier invoices without PVN. Buyer reports Row 55/56/65. Verify extension is in force for current period.
**Legislation:** PVN likums Section 141(1)(7).

### EC16 -- Triangulation (ABC transaction) [T3]
**Situation:** Latvian company (B) buys goods from Estonian company (A), goods shipped directly to Lithuanian company (C).
**Resolution:** Escalate to qualified accountant. Triangulation simplification rules may apply under EU VAT Directive Art. 141. Complex rules require expert review.
**Legislation:** PVN likums Section 43a; EU VAT Directive Art. 141.

### EC17 -- B2G e-invoicing (from 2026) [T1]
**Situation:** PVN-registered client supplies services to Latvian government entity.
**Resolution:** From 2026, B2G (business-to-government) invoicing must use structured electronic format submitted via VID. Paper or PDF invoices are no longer accepted for government contracts. Ensure client's invoicing system supports the required format.
**Legislation:** PVN likums Section 113a (from 2026).

### EC18 -- Fuel for luxury vehicle (blocked) [T1]
**Situation:** Client purchases fuel for a luxury vehicle (value > EUR 75,000).
**Resolution:** ALL costs related to luxury vehicles are blocked. Input PVN on fuel = EUR 0. Additionally, 20% CIT applies on the fuel expense amount.
**Legislation:** PVN likums Section 100(6); CIT Law Section 8(6).

---

## Test Suite

### Test 1 -- Standard domestic purchase, 21% PVN [T1]
**Input:** Latvian supplier, office supplies, gross EUR 242, PVN EUR 42, net EUR 200, PVN-registered taxpayer.
**Expected output:** Row 60 includes EUR 42. Fully recoverable.

### Test 2 -- EU service, reverse charge [T1]
**Input:** German supplier, consulting EUR 1,000, no VAT on invoice, PVN-registered taxpayer.
**Expected output:** Row 51 = EUR 1,000. Row 52 = EUR 210 (self-assessed at 21%). Row 62 = EUR 210 (input PVN). Net = zero.

### Test 3 -- Luxury vehicle purchase (blocked) [T1]
**Input:** PVN-registered client purchases car EUR 90,000 excl. VAT + PVN EUR 18,900, acquired December 2024.
**Expected output:** Input PVN = EUR 0. Luxury vehicle exceeds EUR 75,000 threshold. All costs non-business. No recovery. Subject to 20% CIT.

### Test 4 -- Standard vehicle, mixed use (50%) [T1]
**Input:** PVN-registered client purchases car EUR 25,000 excl. VAT + PVN EUR 5,250 (21%), mixed business/private use.
**Expected output:** Row 60 includes EUR 2,625 (50% of EUR 5,250). Only 50% deductible.

### Test 5 -- EU B2B sale of goods [T1]
**Input:** PVN-registered client sells goods to Estonian company EUR 5,000, 0% PVN, Estonian VAT number verified on VIES.
**Expected output:** Row 46 = EUR 5,000. No output PVN. Report on PVN 2.

### Test 6 -- Non-EU software, reverse charge [T1]
**Input:** US supplier (AWS), EUR 100/month, no VAT, PVN-registered taxpayer.
**Expected output:** Row 53 = EUR 100. Row 54 = EUR 21 (self-assessed at 21%). Row 63 = EUR 21 (input PVN). Net = zero.

### Test 7 -- Reduced rate domestic purchase (food) [T1]
**Input:** Latvian supplier, foodstuffs at 12%, gross EUR 112, PVN EUR 12, net EUR 100, PVN-registered taxpayer.
**Expected output:** Row 60 includes EUR 12. Fully recoverable.

### Test 8 -- Timber purchase, domestic reverse charge [T1]
**Input:** PVN-registered client purchases timber from Latvian supplier, EUR 8,000, invoice shows 0% PVN (reverse charge noted).
**Expected output:** Row 55 = EUR 8,000. Row 56 = EUR 1,680 (self-assessed at 21%). Row 65 = EUR 1,680 (input PVN). Net = zero.

### Test 9 -- Non-registered entity, purchase [T1]
**Input:** Non-registered business (turnover under EUR 50,000, not micro-enterprise) purchases supplies including PVN.
**Expected output:** No PVN declaration entry. Non-registered entity cannot file PVN declaration or recover input PVN. PVN is embedded cost.

### Test 10 -- EU hotel (local consumption exception) [T1]
**Input:** PVN-registered client stays at hotel in Lithuania, EUR 400 including Lithuanian PVM EUR 43 (12%).
**Expected output:** No PVN declaration entry. Lithuanian PVM is irrecoverable. Expense is EUR 400 gross in P&L. NOT reverse charge.

### Test 11 -- Import of goods from China [T1]
**Input:** PVN-registered client imports electronics from China, customs value EUR 10,000, import PVN assessed at customs EUR 2,100 (21%), SAD document obtained.
**Expected output:** Row 64 = EUR 2,100. Input PVN recoverable from customs document. NOT reverse charge.

### Test 12 -- Domestic sale at 5% (books) [T1]
**Input:** PVN-registered Latvian bookstore sells books, net EUR 1,000, PVN EUR 50 (5%).
**Expected output:** Row 44 = EUR 1,000. Row 45 = EUR 50. Output PVN included in Row 57.

### Test 13 -- Entertainment expense (blocked) [T1]
**Input:** PVN-registered client takes clients to concert (entertainment), gross EUR 250, PVN EUR 43 (21%), net EUR 207.
**Expected output:** Input PVN = EUR 0. Entertainment is fully blocked for PVN purposes. No recovery.

### Test 14 -- Construction services, domestic reverse charge [T1]
**Input:** PVN-registered client receives building renovation services from Latvian construction company, EUR 20,000, invoice shows 0% PVN with reverse charge noted.
**Expected output:** Row 55 = EUR 20,000. Row 56 = EUR 4,200 (self-assessed at 21%). Row 65 = EUR 4,200 (input PVN). Net = zero.

### Test 15 -- Fuel for standard mixed-use vehicle (50%) [T1]
**Input:** PVN-registered client purchases fuel for mixed-use car (value EUR 20,000), fuel cost EUR 200 + PVN EUR 42 (21%).
**Expected output:** Row 60 includes EUR 21 (50% of EUR 42). Only 50% deductible -- follows vehicle restriction.

---

## Comparison with Malta

| Feature | Latvia (LV) | Malta (MT) |
|---------|------------|------------|
| Local tax name | Pievienotas vertibas nodoklis (PVN) | VAT |
| Primary legislation | PVN likums | VAT Act Chapter 406 |
| Tax authority | Valsts ienemumu dienests (VID) | Commissioner for Revenue (CFR) |
| Filing portal | EDS | CFR VAT Online |
| Standard rate | 21% | 18% |
| Reduced rates | 12%, 5% | 12%, 7%, 5% |
| Return form | PVN 1 (row-based) | VAT3 (box-based) |
| Filing frequency | Monthly / Quarterly / Bi-annual | Quarterly (Art 10), Annual (Art 11), Monthly (Art 12) |
| Small business scheme | No formal scheme; below EUR 50,000 not registered; micro-enterprise tax alternative | Article 11 exemption (EUR 35,000 threshold) |
| Registration threshold | EUR 50,000 | EUR 35,000 (Art 11) |
| Capital goods scheme | 10 years immovable / 5 years movable | EUR 1,160 gross threshold |
| Vehicle restriction | 50% mixed use; 0% luxury (> EUR 75,000) | Fully blocked under 10th Schedule (exceptions: taxi, rental) |
| Entertainment deductibility | Blocked (0%) | Blocked under 10th Schedule |
| Representation expenses | Limited (40% CIT, capped at 5% wages) | Blocked under 10th Schedule |
| Invoice-level reporting | PVN 1-I, 1-II, 1-III (EUR 150 threshold) | Not required on VAT3 |
| Domestic reverse charge | Timber, scrap metal, construction, CO2, property, electronics, cereals | Not applicable |
| Reverse charge -- EU services | Row 51/52/62 | Box 9a/6/13a |
| Reverse charge -- non-EU services | Row 53/54/63 | Box 11/7/15 |
| Bad debt relief | Available (insolvency/write-off) | Available under certain conditions |
| VAT number format | LV + 11 digits | MT + 8 digits |
| Micro-enterprise tax | Available (25% of turnover, replaces PVN) | Not available |
| B2G e-invoicing | Mandatory from 2026 | Not yet mandatory |

---

## PROHIBITIONS [T1]

- NEVER let AI guess PVN row -- it is 100% deterministic from facts
- NEVER apply reverse charge to out-of-scope categories (wages, dividends, bank charges, equity, loan repayments)
- NEVER apply reverse charge to local consumption services abroad (hotel, restaurant, taxi in another country)
- NEVER allow non-registered or micro-enterprise entities to claim input PVN
- NEVER confuse zero-rated (Row 46/47, exports/intra-EU -- input PVN deductible) with exempt without credit (Row 48 -- input PVN NOT deductible)
- NEVER apply reverse charge when EU supplier charged their local VAT > 0%
- NEVER allow input PVN deduction on luxury vehicle costs (over EUR 75,000 post-June 2023 / over EUR 50,000 pre-June 2023)
- NEVER allow 100% input PVN on mixed-use passenger vehicles (50% cap applies)
- NEVER allow input PVN deduction on entertainment expenses
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude
- NEVER file PVN 1 without also filing required annexes (PVN 1-I, 1-II, 1-III where applicable)
- NEVER allow micro-enterprise taxpayers to register for PVN simultaneously
- NEVER confuse import PVN (paid at customs, Row 64) with reverse charge PVN (self-assessed, Rows 61/62/63/65)

---

## Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Qualified accountant (zverinats revidents / licensed tax consultant) must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to qualified accountant. Document gap.
```

---

## Contribution Notes

This skill was generated from publicly available sources including the PVN likums, VID guidance, Cabinet of Ministers Regulations, and EU VAT Directive 2006/112/EC. It requires validation by a Latvian zverinats revidents (certified auditor) or licensed tax consultant before use in production. All row mappings should be verified against the current official PVN 1 form from VID / EDS.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
