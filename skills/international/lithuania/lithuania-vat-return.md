---
name: lithuania-vat-return
description: Use this skill whenever asked to prepare, review, or create a Lithuanian VAT return (FR0600 form) for any client. Trigger on phrases like "prepare VAT return", "do the PVM", "fill in FR0600", "create the return", "Lithuanian VAT", "pridetines vertes mokestis", or any request involving Lithuania VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data for Lithuanian entities. This skill contains the complete Lithuanian PVM classification rules, box mappings, deductibility rules, reverse charge treatment, i.SAF requirements, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any VAT-related work for Lithuania.
---

# Lithuania VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Lithuania (Lietuva) |
| Jurisdiction Code | LT |
| Primary Legislation | Lietuvos Respublikos pridetines vertes mokescio istatymas (PVM istatymas) -- Law on VAT, No. IX-751, 5 March 2002, as amended |
| Supporting Legislation | EU VAT Directive 2006/112/EC; Government implementing regulations; Mokesciu administravimo istatymas (Tax Administration Law) |
| Tax Authority | Valstybine mokesciu inspekcija (VMI -- State Tax Inspectorate) |
| Filing Portal | https://www.vmi.lt (VMI EDS -- Electronic Declaration System); i.MAS / i.SAF |
| Local Tax Name | Pridetines vertes mokestis (PVM) |
| Return Form | FR0600 (PVM deklaracija) |
| Mandatory E-Invoicing | i.SAF (invoicing data) submitted monthly to VMI |
| Contributor | Awaiting local practitioner |
| Validated By | Claude deep-research cross-check (web-verified 2026-04-10) |
| Validation Date | 2026-04-10 |
| Skill Version | 1.0-draft |
| Status | web-verified |
| Confidence Coverage | Tier 1: box assignment, reverse charge, deductibility blocks, derived calculations, i.SAF requirements. Tier 2: partial exemption pro-rata, vehicle use exceptions, sector-specific rules, representation expense treatment. Tier 3: complex group structures, triangulation, special schemes, VAT grouping. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A qualified accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and PVM mokescio moketojo kodas (PVM ID)** [T1] -- LT + 9 or 12 digits (e.g., LT123456789 for entities, LT123456789012 for individuals)
2. **VAT registration status** [T1] -- Standard registered, small business scheme (turnover < EUR 45,000), or registered for intra-EU acquisitions only
3. **VAT period** [T1] -- Monthly (default), quarterly (annual turnover < EUR 300,000), or bi-annual (turnover < EUR 60,000)
4. **Industry/sector** [T2] -- impacts deductibility and exempt supply status (healthcare, financial, education, construction)
5. **Does the business make exempt supplies?** [T2] -- If yes, partial attribution required (PVM istatymas Article 60)
6. **Does the business trade goods for resale?** [T1] -- impacts classification
7. **Excess credit brought forward** [T1] -- from prior period (refund or carry forward)
8. **i.SAF filing status** [T1] -- mandatory monthly alongside FR0600; confirm i.SAF system is operational
9. **Does the business engage in construction?** [T1] -- domestic reverse charge for construction services
10. **Does the business own/lease passenger vehicles?** [T1] -- full input PVM block unless proven exception

For small businesses under EUR 45,000 [T1]: exempt from charging PVM, cannot recover input PVM. Must still register if making intra-EU acquisitions exceeding EUR 14,000.

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until registration type and period are confirmed.**

---

## VAT Return Form Structure (FR0600 -- PVM Deklaracija) [T1]

The Lithuanian FR0600 form is filed via VMI EDS. Every field on the official form is listed below.

### Output PVM Section (Apskaiciuotas PVM)

| Box | Field Description | Rate / Basis | Legislation |
|-----|-------------------|--------------|-------------|
| 11 | Taxable supplies at 21% -- taxable base | 21% standard rate | PVM istatymas Art. 19(1) |
| 12 | PVM amount on Box 11 | Calculated at 21% | PVM istatymas Art. 19(1) |
| 13 | Taxable supplies at 9% -- taxable base | 9% reduced rate (heating) | PVM istatymas Art. 19(3)(1) |
| 14 | PVM amount on Box 13 | Calculated at 9% | PVM istatymas Art. 19(3)(1) |
| 13a | Taxable supplies at 12% -- taxable base | 12% reduced rate (accommodation, events) | PVM istatymas Art. 19(3)(2) |
| 14a | PVM amount on Box 13a | Calculated at 12% | PVM istatymas Art. 19(3)(2) |
| 15 | Taxable supplies at 5% -- taxable base | 5% super-reduced rate (books, pharma) | PVM istatymas Art. 19(3)(3) |
| 16 | PVM amount on Box 15 | Calculated at 5% | PVM istatymas Art. 19(3)(3) |
| 17 | Zero-rated supplies (exports, intra-EU) -- taxable base | 0% | PVM istatymas Art. 41-49 |
| 18 | Exempt supplies without right of deduction | Exempt | PVM istatymas Art. 20-33 |
| 19 | Intra-Community acquisitions of goods -- taxable base | Self-assessed | PVM istatymas Art. 3(2) |
| 20 | PVM amount on Box 19 (self-assessed) | At applicable rate | PVM istatymas Art. 3(2) |
| 21 | Services received from EU taxable persons (reverse charge) -- base | Self-assessed | PVM istatymas Art. 95(2) |
| 22 | PVM amount on Box 21 (self-assessed) | At 21% | PVM istatymas Art. 95(2) |
| 23 | Services/goods received from non-EU (reverse charge) -- base | Self-assessed | PVM istatymas Art. 95(3) |
| 24 | PVM amount on Box 23 (self-assessed) | At 21% | PVM istatymas Art. 95(3) |
| 25 | Domestic reverse charge supplies received -- base | Self-assessed | PVM istatymas Art. 96 |
| 26 | PVM amount on Box 25 (self-assessed) | At 21% | PVM istatymas Art. 96 |
| 27 | Total output PVM | Sum of all output PVM boxes | Derived |

### Input PVM Section (Atskaitomas pirkimo PVM)

| Box | Field Description | Notes | Legislation |
|-----|-------------------|-------|-------------|
| 28 | Input PVM on domestic purchases | Standard domestic input | PVM istatymas Art. 57 |
| 29 | Input PVM on intra-Community acquisitions | Reverse charge -- EU goods | PVM istatymas Art. 57(2) |
| 30 | Input PVM on services from EU (reverse charge) | Reverse charge -- EU services | PVM istatymas Art. 57(2) |
| 31 | Input PVM on non-EU purchases (reverse charge services) | Reverse charge -- non-EU | PVM istatymas Art. 57(3) |
| 32 | Input PVM on imports | PVM paid at customs (SAD/C88) | PVM istatymas Art. 57(4) |
| 33 | Input PVM on domestic reverse charge | Construction, scrap metal, timber, etc. | PVM istatymas Art. 57(5) |
| 34 | Adjustment of input PVM | Annual adjustments, corrections, capital goods | PVM istatymas Art. 64 |
| 35 | Total deductible input PVM | Sum of Boxes 28-34 | Derived |

### Summary Section (PVM mokestine prievole)

| Box | Field Description | Calculation | Legislation |
|-----|-------------------|-------------|-------------|
| 36 | PVM payable (moketi) | Box 27 - Box 35, if positive | PVM istatymas Art. 83 |
| 37 | PVM overpayment / refund (grazinti/atskaityti) | Box 35 - Box 27, if positive | PVM istatymas Art. 87 |

---

## i.SAF -- Mandatory E-Invoicing System [T1]

**Legislation:** PVM istatymas Art. 78(1); VMI isaakymas No. VA-105 (i.SAF technical specifications).

Lithuania has mandatory e-invoicing through the i.SAF (Israsomų ir gaunamų PVM saskaitu-fakturu registru duomenys) system. This is a critical compliance requirement.

### i.SAF Requirements

| Requirement | Detail |
|-------------|--------|
| Who must file | All PVM-registered taxpayers |
| What is reported | All issued and received PVM invoices (saskaitos-fakturos) |
| Filing frequency | Monthly |
| Filing deadline | 20th of month following the reporting period |
| Format | XML file per VMI specification (i.SAF XSD schema) |
| Submission | Via VMI EDS portal or automated API |
| Threshold | ALL invoices -- no monetary threshold (every invoice reported) |

### i.SAF Data Fields (Per Invoice)

| Field | Description |
|-------|-------------|
| Invoice number | Unique invoice identifier |
| Invoice date | Date of issue |
| Counterparty name | Supplier or customer name |
| Counterparty PVM code | VAT identification number |
| Counterparty country | ISO country code |
| Taxable amount | Net amount per rate |
| PVM amount | Tax amount per rate |
| PVM rate | 21%, 12%, 9%, 5%, or 0% |
| Invoice type | Standard, credit note, debit note |
| Supply type code | Goods, services, mixed |

### i.MAS -- Broader Monitoring System [T1]

i.SAF is part of the broader i.MAS (Ismanieji mokesciu administravimo sprendimai -- Smart Tax Administration Solutions) system, which includes:

| Module | Purpose | Mandatory |
|--------|---------|-----------|
| i.SAF | Invoice-level reporting | Yes -- all PVM payers |
| i.VAZ | Transport waybills (vazbiniai) | Yes -- goods transport |
| i.APS | EKAER-equivalent cargo tracking | Sector-specific |

**CRITICAL:** FR0600 totals MUST reconcile with i.SAF invoice-level data. VMI runs automatic cross-checks. Any discrepancy will trigger an audit query. Always reconcile before submission.

---

## Transaction Classification Matrix [T1]

### 1a. Determine Transaction Type [T1]

- Sale (output PVM / pardavimo PVM) or Purchase (input PVM / pirkimo PVM)
- Salaries, tax payments, loan repayments, dividends, bank charges, equity contributions = OUT OF SCOPE (never on FR0600)
- **Legislation:** PVM istatymas Art. 2 (scope), Art. 3 (definitions of taxable supply)

### 1b. Determine Counterparty Location [T1]

- Lithuania (domestic): supplier/customer country is LT
- EU: AT, BE, BG, HR, CY, CZ, DK, EE, FI, FR, DE, GR, HU, IE, IT, LV, LU, MT, NL, PL, PT, RO, SK, SI, ES, SE
- Non-EU: everything else (US, UK, AU, CH, NO, etc.)
- **Note:** UK is Non-EU post-Brexit. Norway, Switzerland, Iceland are Non-EU.

### 1c. Classification Lookup -- Domestic Purchases [T1]

| VAT Rate | Category | FR0600 Input Box | Notes |
|----------|----------|------------------|-------|
| 21% | Overhead / services | 28 | Standard domestic input |
| 12% | Accommodation, events | 28 | Reduced rate input |
| 9% | Heating (residential) | 28 | Reduced rate input |
| 5% | Books, pharma | 28 | Super-reduced input |
| 0% | Zero-rated (exempt with credit) | -- | No input PVM to claim |
| 0% | Exempt without credit | -- | No input PVM; no entry |
| Any | Passenger car | -- | Fully blocked (0% recovery) unless exception |
| Any | Entertainment | -- | Fully blocked (0% recovery) |

### 1d. Classification Lookup -- EU Purchases (Reverse Charge) [T1]

| Type | Acquisition Box | Output PVM Box | Input PVM Box | Notes |
|------|-----------------|----------------|---------------|-------|
| Physical goods | 19 | 20 | 29 | Self-assess at 21% |
| Services (B2B) | 21 | 22 | 30 | Self-assess at 21% |
| Out-of-scope (wages, etc.) | -- | -- | -- | NEVER reverse charge |
| Local consumption (hotel/restaurant/taxi abroad) | -- | -- | -- | Foreign VAT paid at source |

### 1e. Classification Lookup -- Non-EU Purchases (Reverse Charge) [T1]

| Type | Acquisition Box | Output PVM Box | Input PVM Box | Notes |
|------|-----------------|----------------|---------------|-------|
| Services (B2B) | 23 | 24 | 31 | Self-assess at 21% |
| Physical goods (imported) | -- | -- | 32 | PVM paid at customs (SAD) |
| Out-of-scope | -- | -- | -- | NEVER reverse charge |
| Local consumption abroad | -- | -- | -- | Foreign PVM irrecoverable |

### 1f. Classification Lookup -- Sales [T1]

| Type | Rate | FR0600 Output Box | PVM in Box 27 | Notes |
|------|------|-------------------|---------------|-------|
| Domestic standard | 21% | 11 / 12 | Yes | PVM istatymas Art. 19(1) |
| Domestic accommodation / events | 12% | 13a / 14a | Yes | PVM istatymas Art. 19(3)(2) |
| Domestic heating (residential) | 9% | 13 / 14 | Yes | PVM istatymas Art. 19(3)(1) |
| Domestic books / pharma | 5% | 15 / 16 | Yes | PVM istatymas Art. 19(3)(3) |
| Export (non-EU) | 0% | 17 | No | PVM istatymas Art. 41 |
| Intra-EU goods (B2B) | 0% | 17 | No | Report on EC Sales List |
| Intra-EU services (B2B) | 0% | 17 | No | Report on EC Sales List |
| Exempt without credit | 0% | 18 | No | Input PVM NOT deductible |

---

## VAT Rates -- Complete Schedule [T1]

**Legislation:** PVM istatymas Art. 19, as amended.

| Rate | Description | Specific Supplies | Legislation |
|------|-------------|-------------------|-------------|
| 21% | Standard rate | Most goods and services not listed elsewhere | PVM istatymas Art. 19(1) |
| 12% | Reduced rate | Hotel accommodation (from 2026, previously 9%), catering services for events, restaurant and catering (from 2024), public transport of passengers, cultural and sporting events admission | PVM istatymas Art. 19(3)(2) |
| 9% | Reduced rate | Heating energy for residential premises (centralised heating, natural gas, firewood, wood pellets), certain domestic transport | PVM istatymas Art. 19(3)(1) |
| 5% | Super-reduced rate | Books and non-periodical publications (printed and electronic), periodical publications (newspapers, magazines), medicines and pharmaceutical products (listed), medical devices for disabled persons | PVM istatymas Art. 19(3)(3) |
| 0% | Zero rate | Intra-EU supplies of goods to VAT-registered recipients, exports of goods outside EU, international transport of passengers and goods, supplies to diplomatic missions | PVM istatymas Art. 41-49 |
| Exempt | Exempt without credit | Financial services (banking, insurance, securities), healthcare services, educational services (accredited), postal services (universal), immovable property (unless option to tax), lottery and gambling, funeral services, non-profit membership services | PVM istatymas Art. 20-33 |

### Rate History (Recent Changes)

| Date | Change | Legislation |
|------|--------|-------------|
| 1 January 2024 | Restaurant and catering services moved to 12% (from 21%) | PVM istatymas Art. 19(3)(2) amendment |
| 1 January 2025 | Passenger car input PVM: full block confirmed (no 50% partial) | PVM istatymas Art. 62 reconfirmed |
| 1 January 2026 | Accommodation rate moved from 9% to 12% | PVM istatymas Art. 19(3)(2) amendment |
| 1 January 2026 | Cultural and sporting events moved from 9% to 12% | PVM istatymas Art. 19(3)(2) amendment |

**IMPORTANT:** When processing transactions, always check the invoice date to determine the applicable rate. Transitional rules per PVM istatymas Art. 122 apply at rate change boundaries.

---

## Blocked Input Tax -- Complete List [T1]

**Legislation:** PVM istatymas Art. 62 (restrictions on input tax deduction).

| Category | Recovery % | Legislation | Notes |
|----------|------------|-------------|-------|
| Passenger cars -- purchase and lease | 0% | PVM istatymas Art. 62(1)(1) | Fully blocked; no partial deduction |
| Passenger cars -- fuel | 0% | PVM istatymas Art. 62(1)(1) | Follows vehicle block |
| Passenger cars -- maintenance and repairs | 0% | PVM istatymas Art. 62(1)(1) | Follows vehicle block |
| Passenger cars -- parking | 0% | PVM istatymas Art. 62(1)(1) | Follows vehicle block |
| Entertainment and hospitality (pramogos ir reprezentacija) | 0% | PVM istatymas Art. 62(1)(2) | Fully blocked |
| Catering for entertainment purposes | 0% | PVM istatymas Art. 62(1)(2) | Follows entertainment rule |
| Personal use goods and services | 0% | PVM istatymas Art. 62(1)(3) | Any item for private consumption |
| Goods/services used solely for exempt supplies | 0% | PVM istatymas Art. 58(2) | Healthcare, education, financial |
| Residential property (unless for taxable supply) | 0% | PVM istatymas Art. 62(1)(4) | Unless property used for taxable rental |

### Passenger Car Exceptions [T1]

**Legislation:** PVM istatymas Art. 62(2), as amended from 1 January 2025.

The following businesses may deduct input PVM on passenger cars:

| Exception | Recovery % | Condition | Legislation |
|-----------|------------|-----------|-------------|
| Car rental businesses (nuoma) | 100% | Vehicle used exclusively for rental to third parties | PVM istatymas Art. 62(2)(1) |
| Driving schools (vairavimo mokymo imone) | 100% | Vehicle used exclusively for driving instruction | PVM istatymas Art. 62(2)(2) |
| Transport services (keleiviu vezimas) | 100% | Vehicle used exclusively for passenger transport (taxi, ride-hailing) | PVM istatymas Art. 62(2)(3) |
| Emergency services | 100% | Ambulance, fire, police vehicles | PVM istatymas Art. 62(2)(4) |

**CRITICAL:** Unlike Estonia (50% mixed-use deduction) and Latvia (50% mixed-use deduction), Lithuania applies a FULL BLOCK on passenger car input PVM. There is NO 50% partial deduction for mixed use. Only the specific exceptions above allow recovery.

### Representation Expenses [T2]

**Legislation:** PVM istatymas Art. 62(1)(2); Pelno mokescio istatymas (CIT Law) Art. 22.

- PVM on representation expenses: NOT deductible (0%)
- CIT treatment: 50% of representation expenses deductible, capped at 2% of company's income
- Distinguish from business meetings (verslo susitikimai): reasonable business meeting costs (coffee, water, modest catering) may be treated as ordinary business expenses with PVM recovery [T2]
- **Flag for reviewer: confirm whether expense is entertainment/representation (blocked) or ordinary business meeting cost (potentially recoverable)**

---

## Registration [T1]

### Mandatory Registration Threshold

| Criterion | Value | Legislation |
|-----------|-------|-------------|
| Annual taxable turnover threshold | EUR 45,000 | PVM istatymas Art. 71(1) |
| Registration deadline after threshold exceeded | Within 10 working days | PVM istatymas Art. 71(2) |
| Intra-EU acquisition threshold (for non-registered) | EUR 14,000 | PVM istatymas Art. 71(3) |
| Penalty for late registration | Fine per Mokesciu administravimo istatymas | MAI Art. 139 |

### VAT Number Format

| Element | Format |
|---------|--------|
| Country prefix | LT |
| Digits (legal entities) | 9 digits |
| Digits (individuals) | 12 digits |
| Examples | LT123456789 (company), LT123456789012 (individual) |
| VIES validation | Required for intra-EU transactions |

### Voluntary Registration [T1]

- Businesses below EUR 45,000 may register voluntarily (PVM istatymas Art. 72)
- Must remain registered for at least 2 years after voluntary registration (PVM istatymas Art. 74)
- Voluntary registration grants full input PVM deduction rights (subject to restrictions)

### Small Business Scheme (Smulkaus verslo schema) [T1]

**Legislation:** PVM istatymas Art. 71-72.

| Feature | Detail |
|---------|--------|
| Threshold | EUR 45,000 annual taxable turnover (last 12 months) |
| Effect | Exempt from charging PVM |
| Input PVM recovery | NOT permitted |
| Filing obligation | No FR0600 or i.SAF if solely in small business scheme |
| Intra-EU acquisitions | Must register if intra-EU acquisitions exceed EUR 14,000 |
| Voluntary opt-in | Can voluntarily register for PVM at any time |
| Exit | Automatic when EUR 45,000 exceeded; must register within 10 working days |

### Non-Resident Registration [T2]

- Non-established taxable persons making taxable supplies in Lithuania must register for PVM or appoint a fiscal representative (PVM istatymas Art. 71(5))
- EU businesses can register directly with VMI
- Non-EU businesses must appoint a fiscal representative
- **Flag for reviewer: confirm registration requirements and fiscal representative obligations**

---

## Filing Deadlines and Penalties [T1]

### Filing Schedule

| Form | Period | Deadline | Legislation |
|------|--------|----------|-------------|
| FR0600 (PVM return) -- monthly filer | Monthly | 25th of month following tax period | PVM istatymas Art. 84 |
| FR0600 -- quarterly filer | Quarterly | 25th of month following quarter end | PVM istatymas Art. 84 |
| FR0600 -- bi-annual filer | Half-yearly | 25th of month following half-year end | PVM istatymas Art. 84 |
| i.SAF (invoice data) | Monthly | 20th of month following period | VMI regulation; PVM istatymas Art. 78 |
| EC Sales List | Monthly | 25th of month following period | PVM istatymas Art. 85 |
| Intrastat (arrivals) | Monthly | 10th working day of following month | Statistics Lithuania |
| Intrastat (dispatches) | Monthly | 10th working day of following month | Statistics Lithuania |

**Payment deadline:** Same as FR0600 filing deadline (25th). Electronic filing via VMI EDS is mandatory.

**Note:** i.SAF deadline (20th) is BEFORE FR0600 deadline (25th). i.SAF must be filed first to allow VMI cross-checking.

### Filing Frequency Determination [T1]

| Annual Turnover | Filing Frequency | Legislation |
|-----------------|------------------|-------------|
| Default (all registered taxpayers) | Monthly | PVM istatymas Art. 84(1) |
| < EUR 300,000 (may apply for quarterly) | Quarterly | PVM istatymas Art. 84(2) |
| < EUR 60,000 (may apply for bi-annual) | Bi-annual | PVM istatymas Art. 84(3) |

**Note:** Monthly filing is the default. Quarterly and bi-annual are optional and must be approved by VMI.

### Penalties

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing of FR0600 | EUR 200 to EUR 390 | MAI Art. 139 |
| Late payment of PVM | Daily interest at 0.03% on unpaid amount | MAI Art. 99 |
| Failure to register when required | Fine EUR 200 to EUR 390 | MAI Art. 139 |
| Incorrect FR0600 (negligent) | Fine EUR 200 to EUR 5,800 | MAI Art. 139 |
| Intentional tax evasion | Criminal liability; fine up to EUR 50,000 or imprisonment | Baudziamasis kodeksas Art. 219-220 |
| Failure to submit i.SAF | Separate fine EUR 200 to EUR 390 | MAI Art. 139 |
| i.SAF / FR0600 mismatch | Audit query; potential penalty as above | VMI practice |
| Missing EC Sales List | Fine EUR 200 to EUR 390 | MAI Art. 139 |

### Refund Timeline [T1]

- Standard refund: within 30 calendar days of filing (PVM istatymas Art. 87(1))
- VMI may extend review period to 90 days for verification (PVM istatymas Art. 87(3))
- If taxpayer has tax debts, refund is offset against debts first
- New registrants (first 12 months): refund may be subject to enhanced review

---

## Reverse Charge -- Complete Rules [T1]

### Intra-Community Acquisitions (EU) [T1]

**Legislation:** PVM istatymas Art. 3(2); Art. 95(2).

| Step | Action | FR0600 Box |
|------|--------|------------|
| 1 | Report net amount as acquisition base | Box 19 (goods) or Box 21 (services) |
| 2 | Self-assess output PVM at 21% | Box 20 (goods) or Box 22 (services) |
| 3 | Claim input PVM at 21% | Box 29 (goods) or Box 30 (services) |
| 4 | Net effect for fully taxable business | Zero |

### Non-EU Services (Reverse Charge) [T1]

**Legislation:** PVM istatymas Art. 95(3).

| Step | Action | FR0600 Box |
|------|--------|------------|
| 1 | Report net amount as acquisition base | Box 23 |
| 2 | Self-assess output PVM at 21% | Box 24 |
| 3 | Claim input PVM at 21% | Box 31 |
| 4 | Net effect for fully taxable business | Zero |

### Physical Goods Imports (Non-EU) [T1]

**Legislation:** PVM istatymas Art. 14.

Physical goods imported from non-EU countries are subject to import PVM at customs (SAD/C88 document). This is NOT reverse charge.

| Step | Action | FR0600 Box |
|------|--------|------------|
| 1 | PVM assessed and paid at customs | -- |
| 2 | Claim input PVM from customs document | Box 32 |

**Note:** Lithuania offers a deferred import PVM scheme (atidetas PVM mokejimas) for approved taxpayers. Under this scheme, import PVM is not paid at customs but self-assessed on FR0600. Flag as [T2] if client uses this scheme.

### Domestic Reverse Charge [T1]

**Legislation:** PVM istatymas Art. 96.

Lithuania applies domestic reverse charge for the following:

| Supply Type | Notes | Legislation |
|-------------|-------|-------------|
| Construction services (statybos darbai) | B2B only; applies to construction, renovation, demolition | PVM istatymas Art. 96(1)(1) |
| Scrap metal (ferrous and non-ferrous) | Permanent provision | PVM istatymas Art. 96(1)(2) |
| Timber and related services (mediena) | Extended measure | PVM istatymas Art. 96(1)(3) |
| CO2 emission allowances (EU ETS) | Permanent provision | PVM istatymas Art. 96(1)(4) |
| Mobile phones, tablets, portable electronic devices | Invoice exceeds EUR 1,000 (prior threshold); may be amended | PVM istatymas Art. 96(1)(5) |
| Immovable property (where option to tax is exercised) | Seller must notify VMI of option | PVM istatymas Art. 96(1)(6) |
| Gas and electricity (to dealers) | B2B, dealer-specific provision | PVM istatymas Art. 96(1)(7) |

### Exceptions to Reverse Charge [T1]

- Out-of-scope categories (wages, bank charges, dividends, equity, loan repayments): NEVER reverse charge
- Local consumption abroad (hotel, restaurant, taxi, conference): NOT reverse charge -- foreign VAT paid at source
- EU supplier charged their local VAT > 0%: NOT reverse charge -- foreign VAT is irrecoverable cost
- B2C supplies: NOT reverse charge (domestic reverse charge only applies B2B between PVM-registered persons)

---

## Derived Box Calculations [T1]

```
Total Output PVM (Box 27) = Box 12 + Box 14 + Box 14a + Box 16 + Box 20 + Box 22 + Box 24 + Box 26

Total Input PVM (Box 35) = Box 28 + Box 29 + Box 30 + Box 31 + Box 32 + Box 33 + Box 34

IF Box 27 > Box 35 THEN
  Box 36 = Box 27 - Box 35  -- Tax Payable
  Box 37 = 0
ELSE
  Box 36 = 0
  Box 37 = Box 35 - Box 27  -- Overpayment / Refund
END
```

---

## Key Thresholds [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory PVM registration | EUR 45,000 annual taxable turnover (last 12 months) | PVM istatymas Art. 71(1) |
| Intra-EU acquisition registration (non-registered) | EUR 14,000 | PVM istatymas Art. 71(3) |
| Quarterly filing eligibility | Annual turnover < EUR 300,000 | PVM istatymas Art. 84(2) |
| Bi-annual filing eligibility | Annual turnover < EUR 60,000 | PVM istatymas Art. 84(3) |
| EU distance selling threshold (OSS) | EUR 10,000/calendar year (all EU combined) | PVM istatymas Art. 71a; EU Directive Art. 34 |
| i.SAF submission | Monthly -- ALL invoices (no monetary threshold) | PVM istatymas Art. 78; VMI regulation |
| Domestic reverse charge -- electronics | EUR 1,000 per invoice | PVM istatymas Art. 96(1)(5) |
| Voluntary registration minimum period | 2 years | PVM istatymas Art. 74 |
| Capital goods adjustment -- immovable property | 10 years | PVM istatymas Art. 64(2) |
| Capital goods adjustment -- movable property | 5 years | PVM istatymas Art. 64(1) |
| Intrastat arrivals threshold (2026) | EUR 500,000 | Statistics Lithuania |
| Intrastat dispatches threshold (2026) | EUR 300,000 | Statistics Lithuania |

---

## Partial Exemption (PVM istatymas Art. 60) [T2]

**Legislation:** PVM istatymas Art. 58-64.

If a business makes both taxable and exempt supplies:

```
Recovery % = (Taxable Supplies / Total Supplies) * 100
```

Rules:
- Pro-rata calculated based on previous year's ratio as provisional rate
- Annual adjustment required at year-end based on actual current year ratio (Box 34)
- Directly attributable costs: allocated 100% to taxable or 0% to exempt
- Mixed costs: allocated using the pro-rata percentage
- Capital goods adjustment: 10 years for immovable property; 5 years for movable property exceeding EUR 14,481
- De minimis: if recovery percentage rounds to 100%, full recovery permitted
- Round pro-rata up to next whole number

**Flag for reviewer: pro-rata calculation must be confirmed by qualified accountant. Annual adjustment is mandatory. Capital goods scheme adjustments must be tracked separately. i.SAF must reflect correct allocation.**

---

## Edge Case Registry

### EC1 -- EU hotel / restaurant / taxi booked abroad [T1]
**Situation:** PVM-registered client pays for hotel in Poland. Invoice shows Polish VAT at 8%.
**Resolution:** NOT reverse charge. Foreign VAT was charged and paid at source. No FR0600 boxes. Polish VAT is an irrecoverable cost embedded in the expense. Treat as gross overhead in P&L.
**Legislation:** PVM istatymas Art. 13(4) -- place of supply for accommodation is where property is located.

### EC2 -- Subscription software from non-EU provider (e.g., AWS, Google Cloud) [T1]
**Situation:** Monthly charge from US company, no VAT shown on invoice.
**Resolution:** Reverse charge applies. Box 23 (net base) / Box 24 (output PVM at 21%) / Box 31 (input PVM at 21%). Net effect zero for fully taxable PVM-registered business. Must include in i.SAF as received invoice.
**Legislation:** PVM istatymas Art. 13(12) -- B2B electronic services place of supply is customer's country.

### EC3 -- Passenger car purchase (fully blocked) [T1]
**Situation:** PVM-registered client purchases a car for EUR 25,000 + PVM EUR 5,250 (21%) for mixed business/private use.
**Resolution:** Input PVM = EUR 0. Fully blocked under PVM istatymas Art. 62(1)(1). Unlike Estonia and Latvia, Lithuania does NOT allow ANY partial deduction for mixed-use passenger cars. Zero recovery.
**Legislation:** PVM istatymas Art. 62(1)(1).

### EC4 -- Passenger car for taxi business (exception) [T1]
**Situation:** Licensed taxi operator purchases vehicle for EUR 20,000 + PVM EUR 4,200 (21%), used exclusively for passenger transport.
**Resolution:** Input PVM = EUR 4,200 (100% recoverable). Taxi business exception under Art. 62(2)(3). Must document exclusive use for transport services.
**Legislation:** PVM istatymas Art. 62(2)(3).

### EC5 -- Entertainment expense (fully blocked) [T1]
**Situation:** PVM-registered client hosts entertainment event for clients, EUR 1,000 gross, PVM EUR 174 (21%), net EUR 826.
**Resolution:** Input PVM = EUR 0. Entertainment is fully blocked under Art. 62(1)(2). No recovery. For CIT: 50% deductible, capped at 2% of income.
**Legislation:** PVM istatymas Art. 62(1)(2).

### EC6 -- Construction services (domestic reverse charge) [T1]
**Situation:** Lithuanian construction company provides renovation services to another LT PVM-registered business, EUR 50,000.
**Resolution:** Domestic reverse charge. Supplier invoices without PVM (must note "Atvirkstinis apmokestinimas" on invoice). Buyer reports Box 25 = EUR 50,000 / Box 26 = EUR 10,500 (output PVM at 21%) / Box 33 = EUR 10,500 (input PVM). Net = zero.
**Legislation:** PVM istatymas Art. 96(1)(1).

### EC7 -- Scrap metal purchase (domestic reverse charge) [T1]
**Situation:** PVM-registered client purchases scrap metal from another Lithuanian company, EUR 5,000, invoice shows 0% PVM.
**Resolution:** Domestic reverse charge. Box 25 = EUR 5,000. Box 26 = EUR 1,050 (self-assessed at 21%). Box 33 = EUR 1,050 (input PVM). Net = zero.
**Legislation:** PVM istatymas Art. 96(1)(2).

### EC8 -- Credit notes received [T1]
**Situation:** Client receives a credit note from a Lithuanian supplier for returned goods.
**Resolution:** Reverse the original entry. Reduce Box 28 by the PVM amount on the credit note. Must also issue corrective entry in i.SAF.
**Legislation:** PVM istatymas Art. 83(3).

### EC9 -- i.SAF / FR0600 reconciliation mismatch [T2]
**Situation:** VMI system flags discrepancy between FR0600 totals and i.SAF invoice-level data.
**Resolution:** Flag for reviewer: reconcile FR0600 totals with i.SAF invoice-level data before submission. VMI automatic cross-checks will flag mismatches. Common causes: invoices not recorded in i.SAF, timing differences, credit notes, rounding.
**Action:** Re-examine all invoices for the period; correct i.SAF submission first (by 20th), then file FR0600 (by 25th).

### EC10 -- EU B2B service supply [T1]
**Situation:** PVM-registered client provides IT consulting to German company at 0%.
**Resolution:** Box 17 (zero-rated supply base). No output PVM. Report on EC Sales List. Must include in i.SAF as issued invoice.
**Legislation:** PVM istatymas Art. 13(2) -- B2B services place of supply is customer's country.

### EC11 -- Small business scheme client purchasing from EU [T1]
**Situation:** Small business (under EUR 45,000, not PVM-registered) purchases goods from EU supplier exceeding EUR 14,000 cumulative in calendar year.
**Resolution:** Must register for PVM within 10 working days for intra-EU acquisitions. Cannot remain unregistered once EUR 14,000 threshold exceeded.
**Legislation:** PVM istatymas Art. 71(3).

### EC12 -- Deferred import PVM [T2]
**Situation:** Client is approved for deferred import PVM scheme. Imports goods from China, customs value EUR 20,000.
**Resolution:** Import PVM is NOT paid at customs but self-assessed on FR0600. Report similarly to reverse charge. Flag for reviewer: confirm client's deferred PVM approval status with VMI. Must be correctly reflected in both FR0600 and i.SAF.
**Legislation:** PVM istatymas Art. 83(1a); VMI approval.

### EC13 -- Accommodation sale at 12% (from 2026) [T1]
**Situation:** Lithuanian hotel charges guest EUR 112 gross, PVM EUR 12 (12%), net EUR 100.
**Resolution:** Box 13a = EUR 100. Box 14a = EUR 12. Output PVM included in Box 27. Note: rate was 9% before 2026; verify invoice date.
**Legislation:** PVM istatymas Art. 19(3)(2), as amended.

### EC14 -- Transport waybill (i.VAZ) requirement [T1]
**Situation:** Client transports goods within Lithuania valued at EUR 500.
**Resolution:** Must issue electronic transport waybill (vazbinis) through i.VAZ system before goods are dispatched. Failure to issue i.VAZ document triggers penalties.
**Legislation:** PVM istatymas Art. 78a; VMI regulation on i.VAZ.

---

## Test Suite

### Test 1 -- Standard domestic purchase, 21% PVM [T1]
**Input:** Lithuanian supplier, office supplies, gross EUR 242, PVM EUR 42, net EUR 200, PVM-registered taxpayer.
**Expected output:** Box 28 includes EUR 42. Fully recoverable. Include in i.SAF Part B.

### Test 2 -- EU service, reverse charge [T1]
**Input:** German supplier, consulting EUR 1,000, no VAT on invoice, PVM-registered taxpayer.
**Expected output:** Box 21 = EUR 1,000. Box 22 = EUR 210 (self-assessed at 21%). Box 30 = EUR 210 (input PVM). Net = zero. Include in i.SAF as received invoice.

### Test 3 -- Passenger car purchase (blocked) [T1]
**Input:** PVM-registered client purchases car EUR 25,000 + PVM EUR 5,250 (21%), mixed use.
**Expected output:** Input PVM = EUR 0. Fully blocked under Art. 62(1)(1). No recovery. Car appears in i.SAF but PVM is non-deductible.

### Test 4 -- Entertainment expense (blocked) [T1]
**Input:** Lithuanian restaurant, client entertainment EUR 500 gross, PVM EUR 87 (21%), net EUR 413.
**Expected output:** Input PVM = EUR 0. Entertainment fully blocked under Art. 62(1)(2). No recovery.

### Test 5 -- EU B2B sale of goods [T1]
**Input:** PVM-registered client sells goods to Latvian company EUR 5,000, 0% PVM, Latvian VAT number verified on VIES.
**Expected output:** Box 17 = EUR 5,000. No output PVM. Report on EC Sales List. Include in i.SAF Part A.

### Test 6 -- Small business, purchase [T1]
**Input:** Small business (under EUR 45,000, not PVM-registered) purchases supplies including PVM.
**Expected output:** No FR0600 entry. Small business cannot recover input PVM. No i.SAF obligation.

### Test 7 -- Non-EU software, reverse charge [T1]
**Input:** US supplier (Notion), EUR 20/month, no VAT, PVM-registered taxpayer.
**Expected output:** Box 23 = EUR 20. Box 24 = EUR 4.20 (self-assessed at 21%). Box 31 = EUR 4.20 (input PVM). Net = zero. Include in i.SAF.

### Test 8 -- Accommodation sale at 12% (2026) [T1]
**Input:** Lithuanian hotel (the client), room charge EUR 112 gross, PVM EUR 12 (12%), net EUR 100.
**Expected output:** Box 13a = EUR 100. Box 14a = EUR 12. Output PVM included in Box 27. Include in i.SAF Part A.

### Test 9 -- Construction services, domestic reverse charge [T1]
**Input:** PVM-registered client receives renovation services from Lithuanian construction company, EUR 30,000, invoice shows 0% PVM with "Atvirkstinis apmokestinimas" noted.
**Expected output:** Box 25 = EUR 30,000. Box 26 = EUR 6,300 (self-assessed at 21%). Box 33 = EUR 6,300 (input PVM). Net = zero.

### Test 10 -- Import of goods from USA [T1]
**Input:** PVM-registered client imports machinery from USA, customs value EUR 15,000, import PVM assessed at customs EUR 3,150 (21%), SAD document obtained.
**Expected output:** Box 32 = EUR 3,150. Input PVM recoverable from customs document. NOT reverse charge.

### Test 11 -- Intra-EU acquisition of goods [T1]
**Input:** PVM-registered client purchases raw materials from Polish supplier for EUR 8,000, invoice shows 0% VAT, valid VIES.
**Expected output:** Box 19 = EUR 8,000. Box 20 = EUR 1,680 (self-assessed at 21%). Box 29 = EUR 1,680 (input PVM). Net = zero.

### Test 12 -- EU hotel (local consumption exception) [T1]
**Input:** PVM-registered client stays at hotel in Latvia, EUR 300 including Latvian PVN EUR 36 (12%).
**Expected output:** No FR0600 entry. Latvian PVN is irrecoverable. Expense is EUR 300 gross in P&L. NOT reverse charge.

### Test 13 -- Taxi business, car purchase (exception) [T1]
**Input:** Licensed taxi company (PVM-registered) purchases vehicle EUR 18,000 + PVM EUR 3,780 (21%), used exclusively for taxi services.
**Expected output:** Box 28 includes EUR 3,780. Fully recoverable under Art. 62(2)(3) exception. Must document exclusive use.

---

## Comparison with Malta

| Feature | Lithuania (LT) | Malta (MT) |
|---------|---------------|------------|
| Local tax name | Pridetines vertes mokestis (PVM) | VAT |
| Primary legislation | PVM istatymas (Law No. IX-751) | VAT Act Chapter 406 |
| Tax authority | Valstybine mokesciu inspekcija (VMI) | Commissioner for Revenue (CFR) |
| Filing portal | VMI EDS + i.MAS/i.SAF | CFR VAT Online |
| Standard rate | 21% | 18% |
| Reduced rates | 12%, 9%, 5% | 12%, 7%, 5% |
| Return form | FR0600 (box-based) | VAT3 (box-based) |
| Filing frequency | Monthly (default) / Quarterly / Bi-annual | Quarterly (Art 10), Annual (Art 11), Monthly (Art 12) |
| Mandatory e-invoicing | i.SAF -- ALL invoices reported monthly to VMI | No mandatory e-invoicing |
| Small business scheme | Under EUR 45,000 -- exempt, no PVM charging or recovery | Article 11 -- EUR 35,000 threshold, simplified 4-box declaration |
| Registration threshold | EUR 45,000 | EUR 35,000 (Art 11) |
| Capital goods scheme | 10 years immovable / 5 years movable (> EUR 14,481) | EUR 1,160 gross threshold |
| Vehicle restriction | FULL BLOCK (0%) -- no mixed-use partial deduction | Fully blocked under 10th Schedule (exceptions: taxi, rental) |
| Entertainment deductibility | Blocked (0%) | Blocked under 10th Schedule |
| Representation expenses | Blocked for PVM; CIT: 50% deductible, 2% cap | Blocked under 10th Schedule |
| Invoice-level reporting | i.SAF -- every invoice, no threshold | Not required on VAT3 |
| Domestic reverse charge | Construction, scrap metal, timber, CO2, electronics, property, gas/electricity | Not applicable |
| Reverse charge -- EU services | Box 21/22/30 | Box 9a/6/13a |
| Reverse charge -- non-EU services | Box 23/24/31 | Box 11/7/15 |
| Bad debt relief | Available under insolvency conditions | Available under certain conditions |
| VAT number format | LT + 9 digits (company) or LT + 12 digits (individual) | MT + 8 digits |
| Transport waybills | i.VAZ mandatory electronic waybills | Not required |
| Deferred import PVM | Available for approved taxpayers | Not available |
| Filing deadline | 25th of following month | 21st of following month (e-filing) |

---

## PROHIBITIONS [T1]

- NEVER let AI guess PVM box -- it is 100% deterministic from facts
- NEVER apply reverse charge to out-of-scope categories (wages, dividends, bank charges, equity, loan repayments)
- NEVER apply reverse charge to local consumption services abroad (hotel, restaurant, taxi in another country)
- NEVER allow small business scheme clients (under EUR 45,000, unregistered) to claim input PVM
- NEVER confuse zero-rated (Box 17, exports/intra-EU -- input PVM deductible) with exempt without credit (Box 18 -- input PVM NOT deductible)
- NEVER apply reverse charge when EU supplier charged their local VAT > 0%
- NEVER allow input PVM deduction on passenger cars (full block) unless one of the four specific exceptions applies (rental, driving school, transport, emergency)
- NEVER allow input PVM deduction on entertainment or hospitality expenses
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude
- NEVER file FR0600 without first ensuring i.SAF data is submitted and reconciled (i.SAF deadline 20th, FR0600 deadline 25th)
- NEVER omit invoices from i.SAF -- there is no monetary threshold; ALL invoices must be reported
- NEVER confuse import PVM (paid at customs, Box 32) with reverse charge PVM (self-assessed, Boxes 29/30/31/33)
- NEVER apply the old 9% rate to accommodation or events from 2026 onwards (now 12%)
- NEVER allow a voluntarily registered taxpayer to deregister within the first 2 years

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
Action Required: Qualified accountant must confirm before filing.
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

This skill was generated from publicly available sources including the PVM istatymas, VMI guidance, i.MAS/i.SAF specifications, and EU VAT Directive 2006/112/EC. It requires validation by a Lithuanian certified auditor or licensed tax consultant before use in production. All box mappings should be verified against the current official FR0600 form from VMI.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
