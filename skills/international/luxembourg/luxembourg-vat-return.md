---
name: luxembourg-vat-return
description: Use this skill whenever asked to prepare, review, or create a Luxembourg VAT return (TVA declaration) for any client. Trigger on phrases like "prepare VAT return", "do the TVA", "fill in TVA return", "create the return", "Luxembourg VAT", or any request involving Luxembourg VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Luxembourg VAT classification rules, box mappings, deductibility rules, reverse charge treatment, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any VAT-related work for Luxembourg.
---

# Luxembourg VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Luxembourg |
| Jurisdiction Code | LU |
| Primary Legislation | Loi du 12 fevrier 1979 concernant la taxe sur la valeur ajoutee (TVA Law, as amended through 2025) |
| Supporting Legislation | Grand-Ducal regulations on TVA; Reglement grand-ducal on filing; EU VAT Directive 2006/112/EC; Abgabenordnung (AO, adapted) |
| Tax Authority | Administration de l'enregistrement, des domaines et de la TVA (AED) |
| Filing Portal | https://ecdf.b2g.etat.lu (eCDF -- Electronic Collection of Financial Data) |
| Contributor | Auto-generated draft -- requires validation |
| Validated By | Claude deep-research cross-check (web-verified 2026-04-10) |
| Validation Date | 2026-04-10 |
| Skill Version | 1.0 |
| Status | web-verified |
| Confidence Coverage | Tier 1: box assignment, reverse charge, deductibility blocks, derived calculations. Tier 2: partial exemption pro-rata, real estate options, holding company structures. Tier 3: complex fund structures, SOPARFI/SIF arrangements, non-standard financial supplies, securitization vehicles. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified expert-comptable must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified adviser.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and TVA number** [T1] -- LU + 8 digits
2. **VAT registration status** [T1] -- Standard registered, small business exemption (under EUR 50,000 from 2025), or non-registered
3. **Filing frequency** [T1] -- Monthly (turnover > EUR 620,000), quarterly (EUR 112,000 - EUR 620,000), or annual (< EUR 112,000)
4. **Industry/sector** [T2] -- critical in Luxembourg: financial sector, holding companies, fund management, insurance have very high exempt proportions
5. **Does the business make exempt supplies?** [T2] -- Extremely important given Luxembourg's financial sector dominance
6. **Does the business trade goods for resale?** [T1] -- impacts classification
7. **Excess credit brought forward** [T1] -- from prior period
8. **Is the business a holding company?** [T3] -- SOPARFI/SIF/RAIF/SICAR structures require specialist advice
9. **Is the business in the financial sector?** [T2] -- determines pro-rata rate and deductibility

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output TVA / TVA due) or Purchase (input TVA / TVA deductible)
- Salaries, social contributions (CCSS), income tax, loan repayments, dividends, bank charges = OUT OF SCOPE
- **Legislation:** TVA Law Art. 1-2 (scope of tax), Art. 12 (supply of goods), Art. 14 (supply of services)

### 1b. Determine Counterparty Location [T1]
- Luxembourg (domestic): supplier/customer country is LU
- EU: AT, BE, BG, HR, CY, CZ, DK, EE, FI, FR, DE, GR, HU, IE, IT, LV, LT, MT, NL, PL, PT, RO, SK, SI, ES, SE
- Non-EU: everything else
- **Note:** UK is Non-EU post-Brexit. Switzerland is Non-EU but has bilateral agreements.

### 1c. Determine VAT Rate [T1]

**Luxembourg has the lowest standard VAT rate in the EU.**

| Rate | Category | Legislation |
|------|----------|-------------|
| 17% | Standard rate -- most goods and services (lowest standard rate in the EU) | TVA Law Art. 39-1(1) |
| 14% | Intermediate reduced rate -- certain wines (not sparkling), advertising printed matter, management and safekeeping of credit, certain heating fuels (mineral oils for heating), certain investment gold transactions | TVA Law Art. 39-1(2) |
| 8% | Reduced rate -- gas, electricity, district heating, hairdressing, minor repair of clothing/shoes/bicycles, window cleaning, domestic care services, certain construction labor for renovating private dwellings (> 10 years old), live plants and cut flowers | TVA Law Art. 39-1(3) |
| 3% | Super-reduced rate -- food and non-alcoholic beverages, pharmaceutical products, books (printed and electronic), newspapers and periodicals, water supply, children's clothing/shoes (up to size 32 shoes / 152cm clothes), medical equipment, passenger transport, accommodation, social housing construction | TVA Law Art. 39-1(4) |
| 0% | Zero-rated -- intra-EU supplies of goods, exports | TVA Law Art. 43-44 |
| Exempt with credit | International transport of goods, certain financial services to non-EU recipients | TVA Law Art. 44(1) |
| Exempt without credit | Financial services (Art. 44(1)(d)), insurance (Art. 44(1)(f)), healthcare (Art. 44(1)(a)), education (Art. 44(1)(r)), postal services, residential rental, gambling, management of UCITS/AIF/ELTIF (Art. 44(1)(d)), letting of immovable property | TVA Law Art. 44 |

### 1d. Determine Expense Category [T1]
- Capital goods: tangible assets used for business, subject to adjustment on change of use
- Immovable property: 10-year adjustment period (TVA Law Art. 49(3))
- Movable capital goods: 5-year adjustment period (TVA Law Art. 49(2))
- Resale: goods bought to resell
- Overhead/services: everything else
- **Legislation:** TVA Law Art. 49 (adjustment of deduction for capital goods)

---

## Step 2: VAT Return Form Structure (Declaration TVA) [T1]

**Legislation:** TVA Law Art. 61-65; Grand-Ducal regulation on returns.

### Periodic Return (Monthly / Quarterly)

#### Section A -- Output TVA

| Box | Description | Rate | Notes |
|-----|-------------|------|-------|
| 001 | Domestic supplies at 17% -- taxable base | 17% | Standard-rated sales |
| 002 | TVA on box 001 | 17% | Calculated |
| 003 | Domestic supplies at 14% -- taxable base | 14% | Wines, advertising, credit management |
| 004 | TVA on box 003 | 14% | Calculated |
| 005 | Domestic supplies at 8% -- taxable base | 8% | Gas, electricity, hairdressing, repairs |
| 006 | TVA on box 005 | 8% | Calculated |
| 007 | Domestic supplies at 3% -- taxable base | 3% | Food, books, pharma, transport, housing |
| 008 | TVA on box 007 | 3% | Calculated |
| 009 | Intra-Community supply of goods | 0% | Report on EC Sales List |
| 010 | Intra-Community supply of services | 0% | B2B services to EU |
| 011 | Exports outside EU | 0% | Customs documentation required |
| 012 | Exempt supplies without right of deduction | -- | Financial, insurance, healthcare |
| 013 | Intra-Community acquisitions of goods -- base | Self-assessed | Reverse charge |
| 014 | TVA on box 013 (self-assessed at applicable rate) | Applicable | Output side |
| 015 | Services received from EU (reverse charge) -- base | Self-assessed | B2B services from EU |
| 016 | TVA on box 015 (self-assessed) | Applicable | Output side |
| 017 | Imports / non-EU acquisitions -- base | Self-assessed | Non-EU goods and services |
| 018 | TVA on box 017 (self-assessed) | Applicable | Output side |
| 019 | Domestic reverse charge supplies received -- base | Self-assessed | Metals, emissions |
| 020 | TVA on box 019 (self-assessed) | Applicable | Output side |
| 021 | Total output TVA | Sum | All output TVA |
| 022 | Self-supply / deemed supply | -- | Private use, free distributions |

#### Section B -- Input TVA

| Box | Description | Notes |
|-----|-------------|-------|
| 031 | Input TVA on domestic purchases | All domestic input (all rates) |
| 032 | Input TVA on intra-Community acquisitions | Mirrors Box 014 (if deductible) |
| 033 | Input TVA on services from EU (reverse charge) | Mirrors Box 016 |
| 034 | Input TVA on imports / non-EU (reverse charge) | Mirrors Box 018 |
| 035 | Input TVA on domestic reverse charge | Mirrors Box 020 |
| 036 | Adjustments to input TVA | Corrections, pro-rata, capital goods |
| 037 | Total deductible input TVA | Sum |

#### Section C -- Settlement

| Box | Description | Notes |
|-----|-------------|-------|
| 041 | TVA payable (Box 021 - Box 037, if positive) | Pay to AED |
| 042 | TVA credit / refund (Box 037 - Box 021, if positive) | Request refund or carry forward |

---

## Step 3: Transaction Classification Matrix [T1]

### Purchases -- Domestic (Luxembourg Supplier)

| VAT Rate | Category | Input Box | Notes |
|----------|----------|-----------|-------|
| 17% | Overhead/services | Box 031 | Standard domestic |
| 14% | Overhead/services | Box 031 | Wines, advertising, credit management |
| 8% | Overhead/services | Box 031 | Gas, electricity, hairdressing |
| 3% | Overhead/services | Box 031 | Food, books, pharma |
| 0% | Any | -- | No TVA to claim |
| Any | Capital goods | Box 031 | Track for 5/10-year adjustment |
| Any | Blocked (entertainment) | -- | No deduction |
| Any | Vehicle (private-use portion) | Box 031 at business % | Normal value method [T2] |

### Purchases -- EU Supplier (Reverse Charge)

| Type | Output Box | Input Box | Notes |
|------|-----------|-----------|-------|
| Physical goods | Box 013/014 | Box 032 | Intra-EU acquisition |
| Services (B2B) | Box 015/016 | Box 033 | EU service RC |
| Out-of-scope | -- | -- | NEVER reverse charge |
| Local consumption abroad | -- | -- | Foreign VAT at source |

### Purchases -- Non-EU Supplier

| Type | Output Box | Input Box | Notes |
|------|-----------|-----------|-------|
| Services (B2B) | Box 017/018 | Box 034 | Non-EU service import |
| Physical goods (customs) | Box 017/018 | Box 034 | Import |
| Out-of-scope | -- | -- | NEVER reverse charge |

### Sales -- Domestic

| Rate | Box | Notes |
|------|-----|-------|
| 17% | Box 001/002 | Standard-rated |
| 14% | Box 003/004 | Intermediate |
| 8% | Box 005/006 | Reduced |
| 3% | Box 007/008 | Super-reduced |
| Exempt with credit | Box 009/010/011 | IC supply, exports, int. transport |
| Exempt without credit | Box 012 | Financial, insurance, healthcare |

### Sales -- EU / Non-EU

| Location | Type | Box | Notes |
|----------|------|-----|-------|
| EU B2B goods | Intra-EU supply | Box 009 | Zero-rated, EC Sales List |
| EU B2B services | Art. 17(1) services | Box 010 | Place of supply in customer MS |
| Non-EU | Export | Box 011 | Zero-rated, customs docs |

---

## Step 4: Annual Return (Declaration Annuelle) [T1]

**Legislation:** TVA Law Art. 64; Grand-Ducal regulation.

The annual return provides a summary reconciliation of all periodic returns for the year. It is filed:
- By 1 May following year (if also filing periodic returns)
- By 1 March following year (if annual-only filer with no periodic returns)

| Section | Content |
|---------|---------|
| Turnover by rate | Breakdown of taxable supplies at 17%, 14%, 8%, 3% |
| Total input TVA | Sum of all input TVA claimed during the year |
| Pro-rata adjustment | Final pro-rata calculation (if partial exemption applies) |
| Capital goods adjustment | Annual review of capital goods deduction proportions |
| Final settlement | Reconciliation of all periodic payments/credits against annual total |
| Regularization | Any corrections to prior periods |

The annual return does NOT replace periodic (monthly/quarterly) returns. It is an additional reconciliation filing.

---

## Step 5: Reverse Charge Mechanics [T1]

**Legislation:** TVA Law Art. 44 and related provisions; Art. 17 (place of supply).

### Intra-EU Acquisitions of Goods (Art. 25)
1. Report taxable base in Box 013 and self-assessed output TVA in Box 014
2. Claim input TVA in Box 032
3. Net effect: zero for fully taxable businesses
4. Report on EC Sales List

### EU Services Received -- B2B (Art. 17(1))
1. Report in Box 015 (base) / Box 016 (output TVA)
2. Claim in Box 033
3. Net effect: zero

### Non-EU Services/Goods Received
1. Report in Box 017 (base) / Box 018 (output TVA)
2. Claim in Box 034
3. Net effect: zero

### Domestic Reverse Charge [T1]
**Legislation:** TVA Law, specific provisions.

| Supply Type | Legislation | Threshold | Notes |
|-------------|-------------|-----------|-------|
| CO2 emission allowances | Art. 44bis(1) | No threshold | Greenhouse gas permits |
| Gas and electricity certificates | Art. 44bis(2) | No threshold | Energy certificates |
| Raw and semi-manufactured metals (incl. precious metals) | Art. 44bis(3) | >= EUR 10,000 per supply (from 2024) | Gold, silver, platinum, steel |
| Supplies by non-established persons to LU taxable persons | Art. 44bis(4) | No threshold (mandatory from 1 July 2028, Art. 194 mechanism) | Currently optional |

Domestic reverse charge procedure:
1. Report in Box 019 (base) / Box 020 (output TVA)
2. Claim in Box 035
3. Net effect: zero

### Exceptions to Reverse Charge [T1]
- Out-of-scope categories: NEVER reverse charge
- Local consumption abroad: NOT reverse charge; foreign VAT at source
- EU supplier charged local VAT > 0%: NOT reverse charge
- Domestic metal supplies below EUR 10,000: normal TVA applies (not domestic RC)

---

## Step 6: Deductibility Check

### Blocked / Restricted Categories [T1]
**Legislation:** TVA Law Art. 49-50 (restrictions).

| Category | TVA Recovery | Legislation | Notes |
|----------|-------------|-------------|-------|
| Business entertainment (client hospitality, gifts, events) | 0% | Art. 49(2)(a) | Generally not deductible |
| Passenger vehicles (private use portion) | Business % only | Art. 49(2)(b); AED Circular | Normal value method for private use [T2] |
| Personal use items | 0% | Art. 49(1) | No deduction |
| Goods/services not related to taxable outputs | 0% | Art. 49(1) | Must be linked to taxable activity |
| Supplies for exempt-without-credit activities | 0% | Art. 49(1) | Financial, insurance, fund management inputs |

### Company Cars -- Special Treatment [T2]
**Legislation:** AED Circular on company vehicles; TVA Law Art. 49(2)(b).

| Scenario | TVA Deduction | Notes |
|----------|--------------|-------|
| Vehicle used 100% for business | 100% deduction | Must be provable (rare) |
| Vehicle with private use component | Business % only | "Normal value" calculation applies |
| Benefit-in-kind calculated | Business % deduction | BIK amount determines private portion |
| Activities outside scope of TVA or exempt | 0% | No deduction on vehicle costs |
| Fuel for business-use vehicle | Business % | Follows vehicle split |
| Maintenance/repairs | Business % | Follows vehicle split |

**Flag for reviewer: confirm private/business split and that activities qualify for deduction. Normal value method must be properly documented.**

### Registration-Based Recovery [T1]

| Registration Type | Input TVA Recovery | Legislation |
|-------------------|-------------------|-------------|
| Standard registered | Full recovery (subject to blocks) | Art. 48-50 |
| Small business (under EUR 50,000) | NO recovery | Art. 57(1) |
| Non-established without LU registration | 8th Directive refund (EU) or 13th Directive refund (non-EU) | Art. 57bis |

### Partial Exemption (Pro-Rata) [T2]
**Legislation:** TVA Law Art. 49(2).

If business makes both taxable and exempt supplies:

`Recovery % = (Taxable Supplies / Total Supplies) * 100`

| Rule | Detail | Legislation |
|------|--------|-------------|
| Rounding | Round to nearest whole percent | Art. 49(3) |
| De minimis | If >= 95%, treated as 100% (in some interpretations) [T2] | AED practice |
| Provisional | Use prior year proportion during year | Art. 49(4) |
| Annual adjustment | True-up at year-end in annual return | Art. 49(5) |
| Excluded | Incidental financial/property transactions | Art. 49(2) |

**Critical for Luxembourg financial sector:** Banks, insurance companies, and fund managers typically have very low pro-rata rates (often < 10%). This dramatically reduces recoverable input TVA.

**Flag for reviewer: proportion must be confirmed. Annual adjustment required in annual return.**

---

## Step 7: Luxembourg Financial Sector -- Special Considerations [T2/T3]

**Luxembourg's economy is dominated by the financial sector. Special TVA rules apply:**

| Entity Type | TVA Status | Notes |
|-------------|-----------|-------|
| Banks | Mostly exempt (Art. 44(1)(d)) | Very low pro-rata; management of credit at 14% [T2] |
| Insurance companies | Exempt (Art. 44(1)(f)) | No right to deduct input TVA on most costs |
| UCITS management companies | Exempt (Art. 44(1)(d)) | Management of UCITS/AIF/ELTIF is exempt |
| SOPARFI (holding companies) | Mixed/exempt [T3] | Depends on whether holding is active or passive |
| SIF / RAIF / SICAR | Complex [T3] | Requires specialist analysis |
| Securitization vehicles | Complex [T3] | Requires specialist analysis |
| PSF (Professionals du Secteur Financier) | Depends on activity [T2] | Some activities taxable, some exempt |

**For all financial sector entities: ESCALATE to T3 unless the entity has a clearly documented pro-rata rate from a qualified adviser.**

---

## Step 8: Key Thresholds

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Small business exemption | EUR 50,000 annual turnover (from 2025) | Art. 57(1) |
| EU SME scheme (from 2025) | EUR 85,000 domestic + EUR 100,000 EU-wide | EU Directive 2020/285 |
| Monthly filing threshold | Annual turnover > EUR 620,000 | Art. 61(2) |
| Quarterly filing threshold | Annual turnover EUR 112,000 - EUR 620,000 | Art. 61(3) |
| Annual filing (only) | Annual turnover < EUR 112,000 | Art. 61(4) |
| EU distance selling threshold | EUR 10,000/calendar year | EU Directive 2017/2455 |
| Domestic reverse charge (metals) | >= EUR 10,000 per supply (from 2024) | Art. 44bis(3) |
| Capital goods -- movable | 5-year adjustment | Art. 49(2) |
| Capital goods -- immovable | 10-year adjustment | Art. 49(3) |
| Immovable property exempt period | 5 years after first occupation (option to tax available) | Art. 44(1)(q) |

---

## Step 9: VAT Registration [T1]

| Feature | Detail | Legislation |
|---------|--------|-------------|
| TVA number format | LU + 8 digits | Art. 52 |
| Mandatory registration | Anyone making taxable supplies in Luxembourg | Art. 52(1) |
| Small business exemption | Turnover < EUR 50,000 (opt out of TVA) | Art. 57(1) |
| Voluntary registration | May register even below threshold | Art. 52(2) |
| Group registration | Available for economically, financially, and organizationally linked entities (TVA group / unite fiscale) | Art. 60ter |
| Deregistration | If no longer making taxable supplies | Art. 55 |
| Fiscal representative | Required for non-EU businesses without LU establishment (from 1 July 2028 under Art. 194 mechanism, optional earlier) | Art. 56 |
| EU establishments | May register directly without fiscal representative | Art. 56(2) |

---

## Step 10: Filing Deadlines and Penalties

### Filing Deadlines [T1]

| Filing | Period | Deadline | Legislation |
|--------|--------|----------|-------------|
| Monthly TVA return | Monthly | 15th of month following tax period | Art. 61(2) |
| Quarterly TVA return | Quarterly | 15th of month following quarter end | Art. 61(3) |
| Annual TVA return (stand-alone) | Annual | 1 March of following year | Art. 64(1) |
| Annual TVA return (with periodic) | Annual | 1 May of following year | Art. 64(2) |
| EC Sales List (recapitulatif) | Monthly/Quarterly | Same as periodic return deadline | Art. 63 |
| TVA payment | Same as return | Same as filing deadline | Art. 61 |

### Penalties [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing of TVA return | EUR 500 - EUR 5,000 per return | AO Art. 396(1) |
| Late payment of TVA | Late interest at legal rate (currently ~3.75% p.a.) | AO Art. 397 |
| Tax shortfall (additional assessment) | Up to 50% of additional tax as surcharge | AO Art. 396 |
| Failure to register | EUR 250 - EUR 5,000 + back-assessment | AO Art. 396 |
| EC Sales List late/missing | EUR 500 - EUR 5,000 | Art. 63 |
| Failure to issue invoice | EUR 250 - EUR 2,500 per invoice | AO Art. 396 |
| Fraudulent TVA conduct | Criminal penalties under fiscal criminal law | Code penal, AO |

---

## Step 11: Derived Box Calculations [T1]

```
Box 021 = Box 002 + Box 004 + Box 006 + Box 008 + Box 014 + Box 016 + Box 018 + Box 020
Box 037 = Box 031 + Box 032 + Box 033 + Box 034 + Box 035 + Box 036

IF Box 021 > Box 037 THEN
  Box 041 = Box 021 - Box 037  -- Tax Payable
  Box 042 = 0
ELSE
  Box 041 = 0
  Box 042 = Box 037 - Box 021  -- Credit / Refund
END
```

---

## Step 12: Edge Case Registry

### EC1 -- EU hotel / restaurant / taxi booked abroad [T1]
**Situation:** Luxembourg TVA-registered client pays for hotel in Belgium. Invoice shows Belgian 6% VAT.
**Resolution:** NOT reverse charge. Foreign VAT was charged at source. No TVA boxes. Belgian VAT is irrecoverable.
**Legislation:** TVA Law Art. 18 -- place of supply for accommodation is where property is located.

### EC2 -- SaaS subscription from non-EU provider (AWS, Google) [T1]
**Situation:** Monthly charge from US company, no VAT on invoice.
**Resolution:** Reverse charge. Box 017 (net base) / Box 018 (output TVA at 17%). Box 034 (input TVA at 17%). Net zero.
**Legislation:** TVA Law Art. 17(1) -- place of supply for B2B services is customer's establishment.

### EC3 -- Domestic supply of precious metals (>= EUR 10,000) [T1]
**Situation:** Luxembourg company sells gold material worth EUR 15,000 to another LU TVA-registered business.
**Resolution:** Domestic reverse charge applies (from 2024). Buyer: Box 019 (base EUR 15K) / Box 020 (output TVA) / Box 035 (input TVA). Net zero.
**Legislation:** TVA Law Art. 44bis(3).

### EC4 -- Domestic supply of metals (< EUR 10,000) [T1]
**Situation:** Luxembourg company sells metal parts worth EUR 5,000 to another LU business.
**Resolution:** Normal TVA applies. Domestic reverse charge threshold not met. Supplier charges TVA at 17%.
**Legislation:** TVA Law Art. 44bis(3) -- threshold not met.

### EC5 -- Company car, mixed use [T2]
**Situation:** Client provides car to employee for business and private use.
**Resolution:** TVA deduction limited to business-use portion based on "normal value" calculation. Flag for reviewer: confirm private/business split using the normal value method.
**Legislation:** TVA Law Art. 49(2)(b); AED Circular on company vehicles.

### EC6 -- Financial services company (high exempt proportion) [T2]
**Situation:** Luxembourg bank with mostly exempt financial services. Pro-rata 3%.
**Resolution:** Only 3% of input TVA is recoverable. Flag for reviewer: confirm annual pro-rata rate from prior year.
**Legislation:** TVA Law Art. 49(2).

### EC7 -- Export sale outside EU [T1]
**Situation:** Client sells goods to US customer. EUR 20,000.
**Resolution:** Box 011 = EUR 20,000. No output TVA. Input TVA on related costs fully recoverable.
**Legislation:** TVA Law Art. 43.

### EC8 -- Credit notes [T1]
**Situation:** Client receives a credit note from supplier.
**Resolution:** Reverse the original entry. Reduce applicable input TVA box.
**Legislation:** TVA Law Art. 36 (correction of tax base).

### EC9 -- Intra-Community acquisition of goods [T1]
**Situation:** Client purchases goods from German supplier at 0% with valid VIES.
**Resolution:** Box 013 (acquisition base) / Box 014 (output TVA at 17%) / Box 032 (input TVA at 17%). Net zero.
**Legislation:** TVA Law Art. 25.

### EC10 -- SOPARFI / holding company [T3]
**Situation:** Client is a Luxembourg SOPARFI with mixed taxable/exempt activities (management services + passive holding).
**Resolution:** ESCALATE. Holding company TVA treatment is complex. Passive holding of participations is outside the scope of TVA; active management services may be taxable. Do not classify without specialist advice.
**Legislation:** TVA Law Art. 2; ECJ case law (C-60/90 Polysar, C-142/99 Floridienne).

### EC11 -- Fund management (UCITS/AIF) [T3]
**Situation:** Client provides management services to a UCITS.
**Resolution:** ESCALATE. Management of UCITS/AIF is exempt under Art. 44(1)(d). This impacts the provider's pro-rata rate significantly. Specialist analysis required.
**Legislation:** TVA Law Art. 44(1)(d); ECJ case law (C-169/04 Abbey National).

### EC12 -- Small business, purchase [T1]
**Situation:** Small business (under EUR 50,000) purchases supplies including TVA.
**Resolution:** No TVA return entry. Small business cannot recover input TVA.
**Legislation:** TVA Law Art. 57(1).

### EC13 -- Entertainment expense (blocked) [T1]
**Situation:** Business dinner with clients EUR 300 + TVA EUR 51 (17%).
**Resolution:** Input TVA of EUR 51 is NOT deductible. Full EUR 351 is cost.
**Legislation:** TVA Law Art. 49(2)(a).

### EC14 -- Article 194 mechanism (from July 2028) [T2]
**Situation:** Non-established supplier (EU or non-EU) makes a taxable supply in Luxembourg to a LU-registered buyer.
**Resolution:** From 1 July 2028, mandatory domestic reverse charge under Art. 194. Buyer self-assesses. Before that date: supplier must register or appoint fiscal representative, unless optional RC applies. Flag for reviewer.
**Legislation:** TVA Law Art. 44bis(4); EU Directive Art. 194.

---

## Step 13: VAT Rates -- Detailed Supply Classification [T1]

### 17% Standard Rate (Art. 39-1(1))

| Supply Category | Examples |
|----------------|----------|
| General goods | Electronics, furniture, motor vehicles, household items |
| Professional services | Legal, consulting, IT, management (taxable portion) |
| Telecommunications | Mobile, fixed-line, internet |
| Alcohol | Beer, spirits (not certain wines which are 14%) |
| Tobacco | Cigarettes, cigars |
| Construction materials | Cement, steel, timber |
| Energy (non-reduced) | Fuel |

### 14% Intermediate Reduced Rate (Art. 39-1(2))

| Supply Category | Examples |
|----------------|----------|
| Certain wines | Still wines (not sparkling/champagne) |
| Advertising printed matter | Flyers, catalogs, advertising brochures |
| Management and safekeeping of credit | Certain credit management services |
| Heating fuels | Mineral oils for heating (mazout) |
| Certain investment gold transactions | Specified gold operations |

### 8% Reduced Rate (Art. 39-1(3))

| Supply Category | Examples |
|----------------|----------|
| Gas and electricity | Supply of gas, electricity for all consumers |
| District heating | Central heating supply |
| Hairdressing | Haircuts, salon services |
| Minor repairs | Clothing, shoes, bicycles, leather goods |
| Window cleaning | Professional window cleaning |
| Domestic care services | Home care, assistance services |
| Renovation labor (private dwellings > 10 years) | Labor portion of qualifying renovation |
| Live plants and cut flowers | Decorative plants, bouquets |

### 3% Super-Reduced Rate (Art. 39-1(4))

| Supply Category | Examples |
|----------------|----------|
| Food and non-alcoholic beverages | All food items, soft drinks, juice, water |
| Pharmaceutical products | Prescription and OTC medicines |
| Books | Printed and electronic books |
| Newspapers and periodicals | Daily newspapers, magazines, journals |
| Water supply | Drinking water distribution |
| Children's clothing and shoes | Up to size 152cm clothing / size 32 shoes |
| Medical equipment | Hearing aids, prosthetics, wheelchairs |
| Passenger transport | Bus, train, taxi |
| Accommodation | Hotels, guesthouses, camping, Airbnb |
| Social housing construction | Qualifying social/affordable housing projects |

---

## Step 14: Comparison with Malta

| Feature | Luxembourg (LU) | Malta (MT) |
|---------|-----------------|------------|
| Standard rate | 17% (lowest in EU) | 18% |
| Number of rates | 4 rates: 17%, 14%, 8%, 3% | 4 rates: 18%, 12%, 7%, 5% |
| Return form | TVA Declaration (~42 boxes) | VAT3 (45 boxes) |
| Filing frequency | Monthly / Quarterly / Annual | Quarterly (Art. 10), Annual (Art. 11) |
| Filing deadline | 15th of following month | 21st of month after quarter |
| Payment deadline | Same as filing | Same as filing |
| Annual return | Mandatory (30 April or 28 Feb) | Not required for Art. 10 |
| Small enterprise threshold | EUR 50,000 (from 2025) | EUR 35,000 |
| Capital goods movable | 5-year adjustment | > EUR 1,160 gross |
| Capital goods immovable | 10-year adjustment | No specific adjustment period |
| Blocked: entertainment | Yes (generally not deductible) | Yes (10th Schedule) |
| Blocked: passenger cars | Partial (business % only) | Fully blocked (10th Schedule) |
| Domestic reverse charge | Metals >= EUR 10K, emissions, energy certs | No domestic reverse charge |
| Financial sector impact | Dominant; most entities have low pro-rata | Smaller financial sector |
| Holding company complexity | High (SOPARFI/SIF/RAIF -- T3) | Low (few holding structures) |
| Currency | EUR | EUR |
| Tax authority | AED | CFR |
| Filing portal | eCDF | cfr.gov.mt |

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
Action Required: Expert-comptable or reviseur d'entreprises must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to expert-comptable or reviseur d'entreprises agree. Document gap.
```

---

## Step 16: Test Suite

### Test 1 -- Standard domestic purchase, 17% TVA [T1]
**Input:** Luxembourg supplier, office supplies, gross EUR 234, TVA EUR 34, net EUR 200. Registered taxpayer, fully taxable.
**Expected output:** Box 031 += EUR 34. Fully recoverable.

### Test 2 -- EU service, reverse charge [T1]
**Input:** French supplier, consulting EUR 1,000, no VAT. Registered taxpayer.
**Expected output:** Box 015 = EUR 1,000, Box 016 = EUR 170 (17%). Box 033 = EUR 170. Net = zero.

### Test 3 -- Super-reduced rate domestic sale [T1]
**Input:** Luxembourg bookshop sells books EUR 103 gross, TVA EUR 3 (3%), net EUR 100.
**Expected output:** Box 007 = EUR 100. Box 008 = EUR 3.

### Test 4 -- EU B2B sale [T1]
**Input:** Registered client sells goods to Belgian company EUR 5,000, 0% TVA.
**Expected output:** Box 009 = EUR 5,000. No output TVA. Report on EC Sales List.

### Test 5 -- Small business, purchase [T1]
**Input:** Small business (under EUR 50,000) purchases supplies including TVA.
**Expected output:** No TVA return entry. Small business cannot recover input TVA.

### Test 6 -- Non-EU software, reverse charge [T1]
**Input:** US supplier (AWS), EUR 100/month, no VAT. Registered taxpayer.
**Expected output:** Box 017 = EUR 100, Box 018 = EUR 17 (17%). Box 034 = EUR 17. Net = zero.

### Test 7 -- Intermediate rate domestic purchase [T1]
**Input:** Luxembourg supplier, advertising material EUR 228 gross, TVA EUR 28 (14%), net EUR 200.
**Expected output:** Box 031 += EUR 28. Fully recoverable (if for taxable business use).

### Test 8 -- Domestic metal supply (RC, >= EUR 10,000) [T1]
**Input:** LU company buys gold bars EUR 25,000 from another LU registered company.
**Expected output:** Box 019 = EUR 25,000. Box 020 = EUR 4,250 (17%). Box 035 = EUR 4,250. Net = zero.

### Test 9 -- Domestic metal supply (no RC, < EUR 10,000) [T1]
**Input:** LU company buys metal parts EUR 5,000 from another LU company.
**Expected output:** Normal TVA. Seller charges 17%. Buyer: Box 031 += EUR 850.

### Test 10 -- Financial services company (low pro-rata) [T2]
**Input:** Luxembourg bank, pro-rata 5%. Buys consulting EUR 10,000 + TVA EUR 1,700. Mixed use.
**Expected output:** Box 031 += EUR 85 (5% of EUR 1,700). Remaining EUR 1,615 is cost. Flag for reviewer.

### Test 11 -- Entertainment (blocked) [T1]
**Input:** Client dinner EUR 200 + TVA EUR 34 (17%). Business entertainment.
**Expected output:** Box 031 += EUR 0. TVA blocked. Full EUR 234 is cost.

### Test 12 -- Export of goods [T1]
**Input:** Luxembourg company exports to US client EUR 10,000.
**Expected output:** Box 011 = EUR 10,000. No output TVA. Zero-rated.

---

## Step 17: Refund Process [T1]

| Feature | Detail | Legislation |
|---------|--------|-------------|
| Refund request | Via periodic return (Box 042) or annual return | Art. 61 |
| Refund timeline | Generally within 3 months of filing | Art. 61(6) |
| Carry forward | Credit can be carried forward indefinitely | Art. 61 |
| 8th Directive | Refund for EU businesses not established in LU | Art. 57bis |
| 13th Directive | Refund for non-EU businesses | Art. 57bis |
| Offset | AED may offset credit against other tax liabilities | AO Art. 155 |

---

## Step 18: Out of Scope -- Direct Tax (Reference Only) [T3]

This skill does not compute income tax. The following is reference information only. Escalate to qualified adviser.

- **Corporate income tax (impot sur le revenu des collectivites, IRC):** 17% (+ solidarity surcharge 7% of IRC = effective ~18.19%) for income > EUR 200,000
- **Municipal business tax (impot commercial communal, ICC):** varies by municipality (Luxembourg City: 6.75%)
- **Combined effective rate (IRC + ICC, Luxembourg City):** ~24.94%
- **Net wealth tax:** 0.5% on net assets > EUR 500M; minimum EUR 535 - EUR 32,100
- **Dividend withholding tax:** 15% (reduced by DTTs)
- **IP box regime:** 80% exemption on qualifying IP income
- **SOPARFI participation exemption:** Dividends and capital gains exempt if conditions met (min 10% holding or EUR 1.2M acquisition, 12-month holding period)
- **Social contributions (CCSS):** employer ~12-15%, employee ~12-13% (includes pension, sickness, dependency)
- **Communal surcharge:** 7% of IRC (solidarity surcharge)
- **Special regimes:** Securitization vehicles (exempt from net wealth tax), investment funds (subscription tax), family wealth management (SPF)

### Key Luxembourg-Specific Notes
- Luxembourg is a trilingual jurisdiction (Luxembourgish, French, German)
- TVA returns and communication with AED are typically in French or German
- The financial sector accounts for over 25% of GDP, making partial exemption a dominant concern

---

## PROHIBITIONS [T1]

- NEVER let AI guess VAT box -- it is 100% deterministic from facts
- NEVER apply reverse charge to out-of-scope categories (wages, dividends, bank charges)
- NEVER apply reverse charge to local consumption services abroad (hotel, restaurant, taxi)
- NEVER allow small business (exempt) clients to claim input TVA
- NEVER confuse zero-rated (exports/intra-EU, input TVA deductible) with exempt without credit (financial, insurance)
- NEVER apply reverse charge when EU supplier charged local VAT > 0%
- NEVER allow entertainment expenses to be deducted (Art. 49(2)(a))
- NEVER apply domestic reverse charge on metal supplies below EUR 10,000 (Art. 44bis(3))
- NEVER attempt to handle holding company / fund structures without T3 escalation
- NEVER apply a pro-rata rate for financial sector entities without confirmed rate from qualified adviser
- NEVER confuse the four TVA rates (17%/14%/8%/3%) -- Luxembourg has more rate tiers than most EU countries
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude

---

## Contribution Notes

This skill covers Luxembourg's VAT system based on the Loi du 12 fevrier 1979 as amended. Luxembourg has the lowest standard VAT rate in the EU at 17% and a unique four-tier rate structure (17%/14%/8%/3%). Key distinctive features include: the dominant financial sector creating widespread partial exemption challenges, the SOPARFI/fund management complexity (T3 territory), the domestic reverse charge for metals above EUR 10,000, the mandatory annual return alongside periodic returns, the Art. 194 mechanism from July 2028 for non-established suppliers, and the normal value method for company car private use. Validation by a qualified Luxembourg expert-comptable or reviseur d'entreprises agree is required before production use.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
