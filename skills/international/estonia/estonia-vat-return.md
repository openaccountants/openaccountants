---
name: estonia-vat-return
description: Use this skill whenever asked to prepare, review, or create an Estonian VAT return (KMD form) for any client. Trigger on phrases like "prepare VAT return", "do the KMD", "fill in KMD", "create the return", "Estonian VAT", "kaibemaks", or any request involving Estonia VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data for Estonian entities. This skill contains the complete Estonian VAT classification rules, KMD box mappings, deductibility rules, reverse charge treatment, capital goods thresholds, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any VAT-related work for Estonia.
---

# Estonia VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Estonia (Eesti) |
| Jurisdiction Code | EE |
| Primary Legislation | Kaibemaksuseadus (KMS) -- Value Added Tax Act, RT I 2003, 82, 554, as amended |
| Supporting Legislation | EU VAT Directive 2006/112/EC; Minister of Finance regulations; Maksukorralduse seadus (Taxation Act) |
| Tax Authority | Maksu- ja Tolliamet (MTA -- Estonian Tax and Customs Board) |
| Filing Portal | https://maasikas.emta.ee (e-MTA) |
| Local Tax Name | Kaibemaks (KM) |
| Return Form | KMD (Kaibemaksudeklaratsioon) |
| Contributor | Awaiting local practitioner |
| Validated By | Claude deep-research cross-check (web-verified 2026-04-10) |
| Validation Date | 2026-04-10 |
| Skill Version | 1.0-draft |
| Status | web-verified |
| Confidence Coverage | Tier 1: box assignment, reverse charge, deductibility blocks, derived calculations. Tier 2: partial exemption pro-rata, vehicle use documentation, real estate option to tax, e-resident edge cases. Tier 3: complex group structures, non-standard supplies, triangulation, special schemes. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A qualified accountant (vandeaudiitor or maksunoukoja) must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and KMKR number (VAT ID)** [T1] -- EE + 9 digits (e.g., EE123456789)
2. **VAT registration status** [T1] -- Standard registered (KMKR holder) or not registered (mandatory threshold EUR 40,000)
3. **VAT period** [T1] -- Monthly (only frequency available in Estonia for standard KMD)
4. **Industry/sector** [T2] -- impacts deductibility and exempt status (e.g., healthcare, financial services, education)
5. **Does the business make exempt supplies?** [T2] -- If yes, partial attribution required (KMS Section 32); healthcare, financial services, education, insurance, real estate
6. **Does the business trade goods for resale?** [T1] -- impacts classification
7. **Excess credit brought forward** [T1] -- from prior period (refund requested or carried forward)
8. **Is the business an e-resident company?** [T2] -- special place-of-supply considerations may apply
9. **Does the business own/lease passenger vehicles?** [T2] -- 50% restriction applies unless proven 100% business use

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until registration type and period are confirmed.**

---

## VAT Return Form Structure (KMD -- Kaibemaksudeklaratsioon) [T1]

The Estonian KMD is filed monthly via e-MTA. Every field on the official form is listed below.

### Part I -- Output VAT (Kaibemaks)

| Line | Field Description | Rate / Basis |
|------|-------------------|--------------|
| 1 | Acts and transactions subject to tax at 22% rate -- taxable amount | 22% standard rate (KMS Section 15(1)) |
| 1.1 | Acts and transactions subject to tax at 13% rate -- taxable amount | 13% reduced rate (KMS Section 15(2), accommodation) |
| 1.2 | Acts and transactions subject to tax at 9% rate -- taxable amount | 9% reduced rate (KMS Section 15(2), books, pharma) |
| 2 | Total amount of tax (calculated output VAT) | Sum of VAT on Lines 1, 1.1, 1.2 + self-assessed on Lines 6, 7 |
| 3 | Intra-Community supply of goods and services (0%) -- total taxable amount | KMS Section 15(3) |
| 3.1 | Intra-Community supply of goods -- taxable amount (subset of Line 3) | KMS Section 15(3)(1) |
| 3.1.1 | Intra-Community supply of goods after processing -- taxable amount | KMS Section 15(3)(2) |
| 3.2 | Intra-Community supply of services -- taxable amount (subset of Line 3) | KMS Section 15(3)(3) |
| 4 | Exports and other supplies taxed at 0% -- taxable amount | KMS Section 15(4) -- exports, international transport |
| 5 | Tax-exempt supply -- taxable amount (total) | KMS Section 16 |
| 5.1 | Tax-exempt supply with right of deduction (subset of Line 5) | KMS Section 16(1) |
| 5.2 | Tax-exempt supply without right of deduction (subset of Line 5) | KMS Section 16(2) |
| 6 | Intra-Community acquisition of goods and services -- taxable amount | KMS Section 3(4) -- reverse charge base |
| 6.1 | Intra-Community acquisition of goods -- taxable amount (subset of Line 6) | KMS Section 3(4)(1) |
| 7 | Acquisition of other goods and services subject to VAT -- taxable amount | KMS Section 3(5) -- non-EU services, imports subject to RC |
| 8 | Supply subject to special arrangements (margin scheme) | KMS Sections 41-42 -- used goods, travel agents, art |

### Part II -- Input VAT (Sisendkaibemaks)

| Line | Field Description | Notes |
|------|-------------------|-------|
| 5.3 | Input VAT on acquisition of passenger car (50% restriction) | KMS Section 30(4) -- mixed use vehicles |
| 5.4 | Input VAT on acquisition of passenger car (100% -- documented business only) | KMS Section 30(4) exception -- MTA notification required |
| 9 | Total amount of deductible input VAT | Sum of Lines 9.1 through 9.4 |
| 9.1 | Input VAT on domestic acquisitions | Standard domestic purchases |
| 9.2 | Input VAT on intra-Community acquisitions | Reverse charge -- EU |
| 9.3 | Input VAT on imports | Customs-assessed VAT (SAD/C88) |
| 9.4 | Input VAT on acquisitions from non-EU (reverse charge services) | Reverse charge -- non-EU |

### Part III -- Settlement

| Line | Field Description | Calculation |
|------|-------------------|-------------|
| 10 | Amount of VAT payable | Line 2 - Line 9, if positive |
| 11 | Amount of VAT to be refunded | Line 9 - Line 2, if positive |

### KMD INF -- Annex (Invoice-Level Detail)

Filed monthly alongside KMD. Required when total per business partner >= EUR 1,000 (excl. VAT) per period.

| Part | Description |
|------|-------------|
| Part A | Invoices issued (sales) -- partner VAT ID, taxable amount, VAT amount |
| Part B | Invoices received (purchases) -- partner VAT ID, taxable amount, VAT amount |

**Legislation:** KMS Section 27(7); MTA regulation on KMD INF reporting.

---

## Transaction Classification Matrix [T1]

### 1a. Determine Transaction Type [T1]

- Sale (output VAT / kaibemaks) or Purchase (input VAT / sisendkaibemaks)
- Salaries, contractor wages, tax payments, loan repayments, dividends, bank charges, equity contributions = OUT OF SCOPE (never on KMD)
- **Legislation:** KMS Section 1 (scope), Section 2 (definitions of taxable supply)

### 1b. Determine Counterparty Location [T1]

- Estonia (domestic): supplier/customer country is EE
- EU: AT, BE, BG, HR, CY, CZ, DK, FI, FR, DE, GR, HU, IE, IT, LV, LT, LU, MT, NL, PL, PT, RO, SK, SI, ES, SE
- Non-EU: everything else (US, UK, AU, CH, NO, etc.)
- **Note:** UK is Non-EU post-Brexit. Norway, Switzerland, Iceland are Non-EU.

### 1c. Classification Lookup -- Domestic Purchases [T1]

| VAT Rate | Category | KMD Input Line | Notes |
|----------|----------|----------------|-------|
| 22% | Overhead / services | 9.1 | Standard domestic input |
| 13% | Accommodation | 9.1 | Reduced rate input |
| 9% | Books, pharma | 9.1 | Reduced rate input |
| 0% | Zero-rated (exempt with credit) | -- | No input VAT to claim |
| 0% | Exempt without credit | -- | No input VAT; no entry |
| Any | Passenger car (mixed use) | 5.3 | 50% restriction applies |
| Any | Passenger car (100% business) | 5.4 | Full deduction, MTA notified |

### 1d. Classification Lookup -- EU Purchases (Reverse Charge) [T1]

| Type | Acquisition Line | Output VAT | Input VAT Line | Notes |
|------|------------------|------------|----------------|-------|
| Physical goods | 6.1 (and 6) | Included in Line 2 | 9.2 | Self-assess at 22% |
| Services (B2B) | 6 | Included in Line 2 | 9.2 | Self-assess at 22% |
| Passenger car from EU | 6 | Included in Line 2 | 5.3 or 5.4 | 50% or 100% restriction |
| Out-of-scope (wages etc.) | -- | -- | -- | NEVER reverse charge |
| Local consumption (hotel/restaurant/taxi abroad) | -- | -- | -- | Foreign VAT paid at source |

### 1e. Classification Lookup -- Non-EU Purchases (Reverse Charge) [T1]

| Type | Acquisition Line | Output VAT | Input VAT Line | Notes |
|------|------------------|------------|----------------|-------|
| Services (B2B) | 7 | Included in Line 2 | 9.4 | Self-assess at 22% |
| Physical goods (imported) | -- | -- | 9.3 | VAT paid at customs (SAD) |
| Out-of-scope | -- | -- | -- | NEVER reverse charge |
| Local consumption abroad | -- | -- | -- | Foreign VAT irrecoverable |

### 1f. Classification Lookup -- Sales [T1]

| Type | Rate | KMD Output Line | VAT in Line 2 | Notes |
|------|------|-----------------|----------------|-------|
| Domestic standard | 22% | 1 | Yes | KMS Section 15(1) |
| Domestic accommodation | 13% | 1.1 | Yes | KMS Section 15(2) |
| Domestic books/pharma | 9% | 1.2 | Yes | KMS Section 15(2) |
| Export (non-EU) | 0% | 4 | No | KMS Section 15(4) |
| Intra-EU goods (B2B) | 0% | 3.1 | No | Report on EC Sales List |
| Intra-EU services (B2B) | 0% | 3.2 | No | Report on EC Sales List |
| Intra-EU goods after processing | 0% | 3.1.1 | No | Subset of 3.1 |
| Exempt with credit | 0% | 5.1 | No | Input VAT deductible |
| Exempt without credit | 0% | 5.2 | No | Input VAT NOT deductible |

---

## VAT Rates -- Complete Schedule [T1]

**Legislation:** KMS Section 15 (rates); as amended by RT I, 2023, 5 (2024 increase) and RT I, 2024 (2025 increase).

| Rate | Description | Effective Date | Legislation |
|------|-------------|----------------|-------------|
| 22% | Standard rate | From 1 January 2024 (increased from 20%) | KMS Section 15(1), as amended RT I, 08.03.2023, 5 |
| 13% | Accommodation and lodging services | From 1 January 2025 (increased from 9%) | KMS Section 15(2)(1), as amended |
| 9% | Books and periodicals (physical and electronic) | Ongoing | KMS Section 15(2)(2) |
| 9% | Pharmaceuticals listed by Minister of Social Affairs | Ongoing | KMS Section 15(2)(3) |
| 9% | Medical devices for disabled persons | Ongoing | KMS Section 15(2)(4) |
| 9% | Periodical publications (newspapers, magazines) | Ongoing | KMS Section 15(2)(5) |
| 0% | Intra-Community supplies of goods | Ongoing | KMS Section 15(3) |
| 0% | Exports of goods outside EU | Ongoing | KMS Section 15(4) |
| 0% | International transport of passengers and goods | Ongoing | KMS Section 15(4) |
| 0% | Supplies to diplomatic missions | Ongoing | KMS Section 15(4) |
| Exempt | Financial services (banking, insurance, securities) | Ongoing | KMS Section 16(1) |
| Exempt | Healthcare services | Ongoing | KMS Section 16(2) |
| Exempt | Educational services (accredited institutions) | Ongoing | KMS Section 16(3) |
| Exempt | Postal services (universal service obligation) | Ongoing | KMS Section 16(4) |
| Exempt | Real estate (land and buildings, unless option to tax) | Ongoing | KMS Section 16(2)(6) |
| Exempt | Insurance and reinsurance | Ongoing | KMS Section 16(1) |
| Exempt | Lottery and gambling services | Ongoing | KMS Section 16(5) |

### Rate History (Recent Changes)

| Date | Change | Legislation |
|------|--------|-------------|
| 1 January 2024 | Standard rate increased from 20% to 22% | RT I, 08.03.2023, 5 |
| 1 January 2025 | Accommodation rate increased from 9% to 13% | RT I, 2024 amendment |
| 1 July 2025 | Standard rate increases from 22% to 24% (scheduled) | RT I, 2024 amendment |

**IMPORTANT:** When processing transactions, always check the invoice date to determine the applicable rate. Transitional rules apply at rate change boundaries per KMS Section 46.

---

## Blocked Input Tax -- Complete List [T1]

**Legislation:** KMS Section 30 (restrictions on input tax deduction).

| Category | Recovery % | Legislation | Notes |
|----------|------------|-------------|-------|
| Passenger cars -- mixed business/private use | 50% | KMS Section 30(4) | Applies to purchase/lease price AND all running costs (fuel, maintenance, insurance, parking) |
| Passenger cars -- proven 100% business use | 100% | KMS Section 30(4) exception | Must notify MTA via e-MTA; vehicle must be registered as business-only; [T2] flag for reviewer |
| Entertainment and representation expenses | 0% | KMS Section 30(4)(1) | Not deductible; subject to fringe benefit tax (erisoodustusmaks) instead |
| Catering for entertainment purposes | 0% | KMS Section 30(4)(1) | Follows entertainment rule |
| Personal use goods and services | 0% | KMS Section 30(3) | Any item for private consumption |
| Goods/services used for exempt supplies only | 0% | KMS Section 30(2) | Healthcare, education, financial services exempt supplies |
| Gifts exceeding EUR 10 per item | 0% | KMS Section 30(4)(2) | Business gifts under EUR 10 are deductible; over EUR 10 blocked |
| Alcohol (unless for resale or production) | 0% | KMS Section 30(4)(3) | Exception: restaurants, bars, retailers |
| Tobacco (unless for resale) | 0% | KMS Section 30(4)(3) | Exception: retailers |
| Residential property acquisition (unless for taxable rental) | 0% | KMS Section 30(2) | Unless option to tax exercised |

### Passenger Car -- Detailed Rules [T1]

**Legislation:** KMS Section 30(4), as amended.

| Scenario | Input VAT Recovery | Line on KMD |
|----------|--------------------|-------------|
| Purchase/lease of car -- mixed use | 50% | 5.3 |
| Fuel for mixed-use car | 50% | 9.1 (at 50%) |
| Maintenance/repairs for mixed-use car | 50% | 9.1 (at 50%) |
| Insurance for mixed-use car | Exempt supply -- no VAT | -- |
| Purchase/lease -- 100% business, MTA notified | 100% | 5.4 |
| Fuel for 100% business car | 100% | 9.1 |
| Commercial vehicles (vans, trucks > 3,500 kg) | 100% | 9.1 |
| Taxis (licensed taxi business) | 100% | 9.1 |
| Driving school vehicles | 100% | 9.1 |
| Car rental fleet (rental as primary business) | 100% | 9.1 |

---

## Registration [T1]

### Mandatory Registration Threshold

| Criterion | Value | Legislation |
|-----------|-------|-------------|
| Annual taxable turnover threshold | EUR 40,000 | KMS Section 19(1) |
| Registration deadline after threshold exceeded | 3 business days | KMS Section 19(2) |
| Penalty for late registration | Up to EUR 3,200 | Maksukorralduse seadus Section 154 |

### VAT Number Format

| Element | Format |
|---------|--------|
| Country prefix | EE |
| Digits | 9 digits |
| Example | EE123456789 |
| VIES validation | Required for intra-EU transactions |

### Voluntary Registration [T1]

- Businesses below EUR 40,000 may register voluntarily (KMS Section 20)
- Must remain registered for at least 1 year after voluntary registration
- Voluntary registration grants full input VAT deduction rights

### Small Business Scheme [T1]

Estonia does NOT have a formal small business VAT exemption scheme comparable to Malta Article 11. Businesses below EUR 40,000 are simply not required to register. If not registered:

- Cannot charge VAT on supplies
- Cannot recover input VAT
- No KMD filing obligation
- Must register within 3 business days once EUR 40,000 threshold is exceeded in a calendar year

### Non-Resident Registration [T2]

- Non-established taxable persons making taxable supplies in Estonia must register for VAT or appoint a fiscal representative (KMS Section 20(1))
- EU businesses can register directly; non-EU businesses must appoint a fiscal representative
- E-resident companies with Estonian establishment follow standard rules

---

## Filing Deadlines and Penalties [T1]

### Filing Schedule

| Form | Period | Deadline | Legislation |
|------|--------|----------|-------------|
| KMD (VAT return) | Monthly | 20th of month following tax period | KMS Section 27(1) |
| KMD INF (invoice annex) | Monthly | 20th of month following tax period | KMS Section 27(7) |
| EC Sales List (VD report) | Monthly | 20th of month following period | KMS Section 28 |
| Intrastat (arrivals) | Monthly | 10th business day of following month | Statistics Estonia |
| Intrastat (dispatches) | Monthly | 10th business day of following month | Statistics Estonia |

**Payment deadline:** 20th of month following tax period (same as filing). **Legislation:** KMS Section 27(3).

**Estonia has ONLY monthly filing -- no quarterly or annual option for standard KMD.** KMD must be filed even if no taxable transactions occurred (nil return required).

Electronic filing via e-MTA is mandatory for all registered taxpayers.

### Penalties

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing of KMD | Up to EUR 3,200 | Maksukorralduse seadus (MKS) Section 154 |
| Late payment of VAT | Interest at 0.06% per day (annual rate ~22%) | MKS Section 117 |
| Failure to register when required | Up to EUR 3,200 | MKS Section 154 |
| Incorrect KMD (negligent) | Up to EUR 3,200 | MKS Section 154 |
| Incorrect KMD (intentional) | Up to EUR 32,000 | MKS Section 1531 |
| Failure to submit KMD INF | Separate penalty, up to EUR 3,200 | MKS Section 154 |
| Late submission of EC Sales List | Up to EUR 3,200 | MKS Section 154 |

### Refund Timeline [T1]

- Standard refund: within 30 calendar days of filing (KMS Section 34(1))
- MTA may extend review period to 60 days for verification
- If taxpayer has tax debts, refund is offset against debts first (MKS Section 105)

---

## Reverse Charge -- Complete Rules [T1]

### Intra-Community Acquisitions (EU) [T1]

**Legislation:** KMS Sections 3(4) and 29(4).

| Step | Action | KMD Line |
|------|--------|----------|
| 1 | Report net amount as acquisition base | Line 6 (total) / Line 6.1 (goods only) |
| 2 | Self-assess output VAT at 22% | Included in Line 2 |
| 3 | Claim input VAT at 22% | Line 9.2 |
| 4 | Net effect for fully taxable business | Zero |

### Non-EU Services (Reverse Charge) [T1]

**Legislation:** KMS Sections 3(5) and 10(5).

| Step | Action | KMD Line |
|------|--------|----------|
| 1 | Report net amount as acquisition base | Line 7 |
| 2 | Self-assess output VAT at 22% | Included in Line 2 |
| 3 | Claim input VAT at 22% | Line 9.4 |
| 4 | Net effect for fully taxable business | Zero |

### Physical Goods Imports (Non-EU) [T1]

**Legislation:** KMS Section 6.

Physical goods imported from non-EU countries are subject to import VAT at customs (SAD/C88 document). This is NOT reverse charge -- VAT is paid to customs at the border.

| Step | Action | KMD Line |
|------|--------|----------|
| 1 | VAT assessed and paid at customs | -- |
| 2 | Claim input VAT from customs document | Line 9.3 |

### Domestic Reverse Charge [T1]

**Legislation:** KMS Section 41(1).

Estonia applies domestic reverse charge for the following:

| Supply Type | Threshold | Legislation |
|-------------|-----------|-------------|
| Investment gold and gold material (purity >= 325/1000) | No threshold | KMS Section 41(1)(1) |
| Scrap metal (ferrous and non-ferrous) | No threshold | KMS Section 41(1)(2) |
| CO2 emission allowances | No threshold | KMS Section 41(1)(3) |
| Mobile phones and integrated circuits | Invoice exceeds EUR 10,000 | KMS Section 41(1)(4) |
| Immovable property (where option to tax exercised) | No threshold | KMS Section 16(3) option |

### Exceptions to Reverse Charge [T1]

- Out-of-scope categories (wages, bank charges, dividends, equity): NEVER reverse charge
- Local consumption abroad (hotel, restaurant, taxi, conference, car rental used abroad): NOT reverse charge -- foreign VAT paid at source
- EU supplier charged their local VAT > 0%: NOT reverse charge -- foreign VAT is irrecoverable cost
- B2C supplies from EU: NOT reverse charge (supplier charges their own country's VAT)

---

## Derived Box Calculations [T1]

```
Output VAT (Line 2) = (Line 1 * 22%) + (Line 1.1 * 13%) + (Line 1.2 * 9%)
                      + self-assessed VAT on Line 6 acquisitions (at 22%)
                      + self-assessed VAT on Line 7 acquisitions (at 22%)

Input VAT (Line 9) = Line 9.1 + Line 9.2 + Line 9.3 + Line 9.4

IF Line 2 > Line 9 THEN
  Line 10 = Line 2 - Line 9  -- Tax Payable
  Line 11 = 0
ELSE
  Line 10 = 0
  Line 11 = Line 9 - Line 2  -- Refundable
END
```

**Note:** Lines 5.3 and 5.4 are informational breakdowns of the passenger car input VAT already included in Line 9.1 or 9.2. They do not add separately to Line 9.

### Line 3 Breakdown [T1]

```
Line 3 = Line 3.1 + Line 3.2
Line 3.1 includes Line 3.1.1 (goods after processing is subset of goods)
```

### Line 5 Breakdown [T1]

```
Line 5 = Line 5.1 + Line 5.2
Line 5.1 = exempt supplies WITH right of input VAT deduction
Line 5.2 = exempt supplies WITHOUT right of input VAT deduction
```

### Line 6 Breakdown [T1]

```
Line 6 = Line 6.1 + (intra-Community services acquired)
Line 6.1 = intra-Community acquisition of goods only
```

---

## Key Thresholds [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory VAT registration | EUR 40,000 annual taxable turnover | KMS Section 19(1) |
| Registration deadline after exceeding threshold | 3 business days | KMS Section 19(2) |
| EU distance selling threshold (OSS) | EUR 10,000/calendar year (all EU combined) | KMS Section 19(3); EU Directive 2006/112/EC Art. 34 |
| KMD INF reporting threshold | EUR 1,000 per partner per period (excl. VAT) | MTA regulation |
| Vehicle 50% restriction | All passenger cars unless proven 100% business | KMS Section 30(4) |
| Business gift deductibility limit | EUR 10 per item | KMS Section 30(4)(2) |
| Domestic reverse charge -- mobile phones/circuits | EUR 10,000 per invoice | KMS Section 41(1)(4) |
| Intrastat arrivals threshold (2026) | EUR 700,000 | Statistics Estonia |
| Intrastat dispatches threshold (2026) | EUR 350,000 | Statistics Estonia |
| Penalty for late registration | Up to EUR 3,200 | MKS Section 154 |

---

## Partial Exemption (KMS Section 32) [T2]

**Legislation:** KMS Section 32.

If a business makes both taxable and exempt supplies:

```
Recovery % = (Taxable Supplies / Total Supplies) * 100
```

Rules:
- Pro-rata calculated annually based on previous year's ratio
- Adjusted at year-end based on actual ratio for current year
- Directly attributable costs: allocated 100% to taxable or 0% to exempt
- Mixed costs: allocated using the pro-rata percentage
- De minimis: if exempt turnover is less than 5% of total, 100% recovery may be permitted [T2]

**Flag for reviewer: pro-rata calculation must be confirmed by qualified accountant. Annual adjustment is mandatory.**

---

## Edge Case Registry

### EC1 -- EU hotel / restaurant / taxi booked abroad [T1]
**Situation:** KMKR-registered client pays for hotel in Finland via credit card. Invoice shows Finnish VAT at 14%.
**Resolution:** NOT reverse charge. Foreign VAT was charged and paid at source. No KMD lines. Finnish VAT is an irrecoverable cost embedded in the expense. Treat as gross overhead in P&L.
**Legislation:** KMS Section 10 -- place of supply for accommodation is where property is located; consumed locally.

### EC2 -- Subscription software from non-EU provider (e.g., AWS, Google Cloud, Notion) [T1]
**Situation:** Monthly charge from a US company, no VAT shown on invoice.
**Resolution:** Reverse charge applies. Line 7 (net base) / output VAT in Line 2 (at 22%) / Line 9.4 (input VAT at 22%). Net effect zero for fully taxable KMKR-registered business.
**Legislation:** KMS Section 10(5) -- place of supply for B2B electronic services is customer's country.

### EC3 -- Passenger car purchase, mixed business/private use [T1]
**Situation:** KMKR-registered client purchases a car for EUR 20,000 + VAT EUR 4,400 (22%), used for both business and private purposes.
**Resolution:** Input VAT restricted to 50%. Line 5.3 = EUR 2,200. All related running costs (fuel, maintenance, parking) also restricted to 50%.
**Legislation:** KMS Section 30(4).

### EC4 -- Passenger car, documented 100% business use [T2]
**Situation:** Client uses vehicle exclusively for business. Vehicle registered with MTA as business-only via e-MTA notification.
**Resolution:** Input VAT at 100%. Line 5.4 = EUR 4,400 (full amount). Flag for reviewer: confirm MTA notification is filed, vehicle is not used privately, and documentation (logbook or GPS tracking) is maintained.
**Legislation:** KMS Section 30(4) exception.

### EC5 -- Export sale outside EU [T1]
**Situation:** KMKR-registered client sells physical goods to a US customer.
**Resolution:** Line 4 (exports at 0%). No output VAT. Input VAT on related production/procurement costs is fully recoverable. Customs export declaration (EAD) must be retained as proof.
**Legislation:** KMS Section 15(4).

### EC6 -- Intra-Community supply of goods to Latvia [T1]
**Situation:** KMKR-registered client sells goods to a Latvian company. Latvian company provides valid VIES-verified VAT number.
**Resolution:** Line 3 / Line 3.1 (intra-Community supply at 0%). No output VAT. Must report on EC Sales List (VD report). Proof of transport required (CMR, bill of lading).
**Legislation:** KMS Section 15(3)(1).

### EC7 -- Credit notes received [T1]
**Situation:** Client receives a credit note from a domestic supplier for returned goods.
**Resolution:** Reverse the original entry. Reduce Line 9.1 by the VAT amount on the credit note. The credit note reduces both net amount and input VAT previously claimed.
**Legislation:** KMS Section 29(7).

### EC8 -- E-resident company providing global services [T2]
**Situation:** E-resident company registered in Estonia provides IT consulting to clients worldwide.
**Resolution:** Flag for reviewer. Place of supply rules must be confirmed:
- B2B services to EU customers = customer's country (reverse charge by customer). Report in Line 3.2.
- B2B services to non-EU customers = customer's country (out of scope of Estonian VAT). Report in Line 4.
- B2C electronic services to EU consumers = consumer's country. OSS registration may be needed.
- B2C services to non-EU consumers = outside EU VAT scope.
**Legislation:** KMS Section 10(4)-(5).

### EC9 -- Intra-Community acquisition of goods from Germany [T1]
**Situation:** Client purchases machinery from German supplier at 0% with valid VIES verification.
**Resolution:** Line 6 / Line 6.1 (acquisition base). Self-assessed output VAT at 22% in Line 2. Input VAT at 22% in Line 9.2. Net effect zero for fully taxable business.
**Legislation:** KMS Section 3(4)(1).

### EC10 -- KMD INF threshold partner reporting [T1]
**Situation:** Transactions with a single business partner total EUR 1,200 excl. VAT in the reporting month.
**Resolution:** Must include in KMD INF annex (Part A for sales, Part B for purchases). Threshold is EUR 1,000. Failure to report may trigger MTA audit query.
**Legislation:** KMS Section 27(7); MTA regulation.

### EC11 -- Real estate sale -- option to tax [T2]
**Situation:** Client sells commercial property. Default treatment is VAT-exempt.
**Resolution:** Seller may exercise option to tax under KMS Section 16(3). If option exercised, domestic reverse charge may apply (buyer self-assesses VAT). Flag for reviewer: confirm option was properly notified to MTA before transaction.
**Legislation:** KMS Section 16(3); Section 41(1).

### EC12 -- Gold investment (domestic reverse charge) [T1]
**Situation:** Client purchases investment gold from Estonian dealer.
**Resolution:** Domestic reverse charge applies. Supplier invoices without VAT. Buyer self-assesses VAT. No VAT recovery if gold is for investment (exempt).
**Legislation:** KMS Section 41(1)(1).

### EC13 -- Rate transition: invoice spanning rate change [T2]
**Situation:** Service contract spans the date of a rate change (e.g., 20% to 22% on 1 Jan 2024). Invoice issued after rate change.
**Resolution:** The rate applicable is determined by the tax point (time of supply). If supply completed before rate change, old rate applies. If supply completed after, new rate applies. For continuous supplies, apportionment may be required.
**Legislation:** KMS Section 11 (time of supply); Section 46 (transitional provisions).

### EC14 -- Bad debt relief [T2]
**Situation:** Client has an unpaid sales invoice older than 12 months.
**Resolution:** Estonia does NOT have automatic bad debt relief for VAT. Output VAT already declared cannot be reclaimed simply because the debtor has not paid. Exception: if debtor is formally declared bankrupt. Flag for reviewer.
**Legislation:** KMS Section 29(9).

### EC15 -- Fuel card purchases for mixed-use vehicle [T1]
**Situation:** KMKR-registered client uses a fuel card for a passenger car that is mixed business/private use. Monthly fuel invoice EUR 500 + VAT EUR 110 (22%).
**Resolution:** Input VAT restricted to 50%. Recoverable VAT = EUR 55. Included in Line 9.1 at 50%. The 50% restriction on fuel follows the vehicle restriction.
**Legislation:** KMS Section 30(4).

### EC16 -- Triangulation (ABC transaction) [T3]
**Situation:** Estonian company (B) buys goods from German company (A), goods shipped directly to Latvian company (C). Triangular transaction.
**Resolution:** Escalate to qualified accountant. Triangulation simplification rules may apply under EU VAT Directive Art. 141. B may be exempt from registration in Latvia if conditions are met. Complex rules -- do not attempt classification without expert review.
**Legislation:** KMS Section 22; EU VAT Directive Art. 141.

### EC17 -- VAT group registration [T3]
**Situation:** Client asks about forming a VAT group with related entities in Estonia.
**Resolution:** Estonia allows VAT grouping under KMS Section 22a. Intra-group supplies are generally outside the scope of VAT. Escalate -- VAT group rules are complex and require MTA approval.
**Legislation:** KMS Section 22a.

### EC18 -- Second-hand goods (margin scheme) [T2]
**Situation:** Client is a used car dealer. Purchases and resells used vehicles.
**Resolution:** Margin scheme may apply under KMS Sections 41-42 (special arrangements). VAT is charged only on the margin (selling price minus purchase price). Report in Line 8. Flag for reviewer: confirm margin scheme eligibility and correct margin calculation.
**Legislation:** KMS Sections 41-42.

---

## Test Suite

### Test 1 -- Standard domestic purchase, 22% VAT [T1]
**Input:** Estonian supplier, office supplies, gross EUR 244, VAT EUR 44, net EUR 200, KMKR-registered taxpayer.
**Expected output:** Line 9.1 includes EUR 44. Fully recoverable.

### Test 2 -- EU service, reverse charge [T1]
**Input:** Finnish supplier, consulting EUR 1,000, no VAT on invoice, KMKR-registered taxpayer.
**Expected output:** Line 6 = EUR 1,000. Self-assessed output VAT in Line 2 = EUR 220. Line 9.2 = EUR 220. Net = zero.

### Test 3 -- Passenger car, mixed use (50%) [T1]
**Input:** KMKR-registered client purchases car EUR 20,000 + VAT EUR 4,400 (22%), mixed use, MTA not notified as business-only.
**Expected output:** Line 5.3 = EUR 2,200 (50% of EUR 4,400). Only 50% deductible. Included within Line 9.1.

### Test 4 -- EU B2B sale of goods [T1]
**Input:** KMKR-registered client sells goods to Latvian company EUR 5,000, 0% VAT, Latvian VAT number verified on VIES.
**Expected output:** Line 3.1 = EUR 5,000. No output VAT. Report on EC Sales List.

### Test 5 -- Non-registered entity, purchase [T1]
**Input:** Non-registered business (turnover under EUR 40,000) purchases supplies including VAT.
**Expected output:** No KMD entry. Non-registered entity cannot file KMD or recover input VAT. VAT is embedded cost.

### Test 6 -- Non-EU software, reverse charge [T1]
**Input:** US supplier (Google Workspace), EUR 50/month, no VAT, KMKR-registered taxpayer.
**Expected output:** Line 7 = EUR 50. Self-assessed output VAT in Line 2 = EUR 11. Line 9.4 = EUR 11. Net = zero.

### Test 7 -- Accommodation sale at 13% [T1]
**Input:** Estonian hotel (the client) charges guest EUR 113 gross, VAT EUR 13 (13%), net EUR 100.
**Expected output:** Line 1.1 = EUR 100. Output VAT EUR 13 included in Line 2.

### Test 8 -- Entertainment expense (blocked) [T1]
**Input:** KMKR-registered client hosts dinner for business contacts at Tallinn restaurant, gross EUR 300, VAT EUR 49 (22%), net EUR 251.
**Expected output:** Input VAT = EUR 0. Entertainment is blocked under KMS Section 30(4)(1). No recovery. Subject to fringe benefit tax instead.

### Test 9 -- Domestic reverse charge, scrap metal [T1]
**Input:** KMKR-registered client purchases scrap metal from another Estonian company, EUR 5,000, invoice shows 0% VAT (domestic reverse charge).
**Expected output:** Self-assess output VAT at 22% = EUR 1,100 (included in Line 2). Input VAT = EUR 1,100 (in Line 9.1). Net = zero. Seller correctly invoiced without VAT per KMS Section 41(1)(2).

### Test 10 -- Import of goods from China [T1]
**Input:** KMKR-registered client imports electronics from China, customs value EUR 10,000, import VAT assessed at customs EUR 2,200 (22%), SAD document obtained.
**Expected output:** Line 9.3 = EUR 2,200. Input VAT recoverable from customs document. NOT reverse charge -- VAT paid at customs border.

### Test 11 -- Intra-EU acquisition of goods [T1]
**Input:** KMKR-registered client purchases machinery from German supplier for EUR 15,000, invoice shows 0% VAT, valid VIES.
**Expected output:** Line 6 = EUR 15,000. Line 6.1 = EUR 15,000. Self-assessed output VAT in Line 2 = EUR 3,300. Line 9.2 = EUR 3,300. Net = zero.

### Test 12 -- EU hotel (local consumption exception) [T1]
**Input:** KMKR-registered client stays at hotel in Germany, EUR 500 including German VAT EUR 35 (7%).
**Expected output:** No KMD entry. German VAT is irrecoverable. Expense is EUR 500 gross in P&L. NOT reverse charge.

### Test 13 -- Fuel for mixed-use vehicle (50%) [T1]
**Input:** KMKR-registered client purchases fuel via fuel card, EUR 500 + VAT EUR 110 (22%), for mixed-use passenger car.
**Expected output:** Line 9.1 includes EUR 55 (50% of EUR 110). Only 50% deductible. Vehicle is not registered as 100% business with MTA.

### Test 14 -- Business gift under EUR 10 [T1]
**Input:** KMKR-registered client purchases branded pens as business gifts, EUR 8 per pen (below EUR 10 threshold), total EUR 400 + VAT EUR 88.
**Expected output:** Line 9.1 includes EUR 88. Fully recoverable -- gifts under EUR 10 per item are deductible.

### Test 15 -- Business gift over EUR 10 (blocked) [T1]
**Input:** KMKR-registered client purchases wine bottles as business gifts, EUR 25 per bottle (above EUR 10 threshold), total EUR 500 + VAT EUR 110.
**Expected output:** Input VAT = EUR 0. Gifts exceeding EUR 10 per item are blocked under KMS Section 30(4)(2). No recovery.

---

## Comparison with Malta

| Feature | Estonia (EE) | Malta (MT) |
|---------|-------------|------------|
| Local tax name | Kaibemaks (KM) | VAT |
| Primary legislation | Kaibemaksuseadus (KMS) | VAT Act Chapter 406 |
| Tax authority | Maksu- ja Tolliamet (MTA) | Commissioner for Revenue (CFR) |
| Filing portal | e-MTA | CFR VAT Online |
| Standard rate | 22% (24% from July 2025) | 18% |
| Reduced rates | 13% (accommodation), 9% (books, pharma) | 12%, 7%, 5% |
| Return form | KMD (single form) | VAT3 (multi-box form) |
| Filing frequency | Monthly only | Quarterly (Art 10), Annual (Art 11), Monthly (Art 12) |
| Small business scheme | No formal scheme; below EUR 40,000 simply not registered | Article 11 exemption (EUR 35,000 threshold) |
| Registration threshold | EUR 40,000 | EUR 35,000 (Art 11) / EUR 10,000 (Art 12 for EU goods) |
| Capital goods threshold | No single threshold; standard depreciation rules | EUR 1,160 gross |
| Vehicle restriction | 50% for mixed use; 100% if proven business-only + MTA notification | Fully blocked under 10th Schedule (exceptions: taxi, rental) |
| Entertainment deductibility | Blocked (0%); fringe benefit tax instead | Blocked under 10th Schedule Item 3(1)(b) |
| Invoice-level reporting | KMD INF (EUR 1,000 threshold per partner) | Not required on VAT3 |
| Reverse charge -- EU services | Line 6 / Line 2 / Line 9.2 | Box 9a / Box 6 / Box 13a |
| Reverse charge -- non-EU services | Line 7 / Line 2 / Line 9.4 | Box 11 / Box 7 / Box 15 |
| Domestic reverse charge | Gold, scrap metal, CO2, mobile phones >EUR 10k | Not applicable in Malta |
| Bad debt relief | No automatic relief (only on formal bankruptcy) | Available under certain conditions |
| VAT number format | EE + 9 digits | MT + 8 digits |

---

## PROHIBITIONS [T1]

- NEVER let AI guess VAT line -- it is 100% deterministic from facts
- NEVER apply reverse charge to out-of-scope categories (wages, dividends, bank charges, equity)
- NEVER apply reverse charge to local consumption services abroad (hotel, restaurant, taxi in another country)
- NEVER allow non-registered entities to claim input VAT or file KMD
- NEVER confuse zero-rated (Line 4, exports/intra-EU -- input VAT deductible) with exempt without credit (Line 5.2 -- input VAT NOT deductible)
- NEVER apply reverse charge when EU supplier charged their local VAT > 0%
- NEVER apply 100% input VAT deduction on passenger cars without confirmed MTA notification and documented exclusive business use
- NEVER allow input VAT deduction on entertainment or representation expenses
- NEVER allow input VAT deduction on business gifts exceeding EUR 10 per item
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude
- NEVER file KMD without also considering KMD INF annex requirements (EUR 1,000 threshold)
- NEVER apply the wrong VAT rate for a transitional period -- always check invoice date against rate change dates
- NEVER confuse import VAT (paid at customs, Line 9.3) with reverse charge (self-assessed, Line 9.4)

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
Action Required: Qualified accountant (vandeaudiitor / maksunoukoja) must confirm before filing.
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

This skill was generated from publicly available sources including the Kaibemaksuseadus (KMS), MTA guidance, and EU VAT Directive 2006/112/EC. It requires validation by an Estonian vandeaudiitor (certified auditor) or licensed tax advisor (maksunoukoja) before use in production. All line mappings should be verified against the current official KMD form from MTA / e-MTA.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
