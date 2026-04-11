---
name: sweden-vat-return
description: Use this skill whenever asked to prepare, review, or create a Swedish VAT return (momsdeklaration) for any client. Trigger on phrases like "prepare VAT return", "do the Swedish VAT", "momsdeklaration", "moms", "skattedeklaration", or any request involving Swedish VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Swedish VAT classification rules, ruta (box) mappings, deductibility rules, reverse charge treatment, representation limits, ROT/RUT interaction, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any VAT-related work for Sweden.
status: awaiting-validation
version: 1.0-draft
---

# Sweden VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Sweden |
| Jurisdiction Code | SE |
| Primary Legislation | Mervardeskattelagen (ML) 2023:200 (consolidated VAT Act, in force 1 July 2023, replacing ML 1994:200) |
| Supporting Legislation | Skatteforfarandelagen (SFL) 2011:1244 (filing, procedures, penalties); Inkomstskattelagen (IL) 1999:1229 (representation deduction limits); Lag (2009:194) om forfarandet vid skattereduktion for hushallsarbete (ROT/RUT) |
| Tax Authority | Skatteverket (Swedish Tax Agency) |
| Filing Portal | Skatteverket e-tjanster (https://www.skatteverket.se) -- electronic filing via Mina sidor or file upload (SRU/XML) |
| Filing Form | Skattedeklaration (momsdeklaration) -- sections for moms, arbetsgivaravgifter, and avdragen skatt combined in one declaration |
| Contributor | DRAFT -- awaiting practitioner validation |
| Validated By | Deep research verification, April 2026 |
| Validation Date | Pending |
| Skill Version | 1.0-draft |
| Rate Verification | Rates verified against PWC Tax Summaries (taxsummaries.pwc.com/sweden/corporate/other-taxes), April 2026 |
| Confidence Coverage | Tier 1: ruta assignment, reverse charge, deductibility rules, derived calculations, filing deadlines. Tier 2: partial deduction (pro-rata), sector-specific classification, representation borderline, ROT/RUT interaction. Tier 3: VAT groups (mervardesskattgrupp), complex financial sector, forest/agriculture flat-rate schemes, real estate option to tax (frivillig skattskyldighet) transitions. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude assigns, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. An auktoriserad revisor or godkand revisor must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to auktoriserad revisor and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and momsregistreringsnummer (VAT number)** [T1] -- Format: SE + 12 digits (organisationsnummer 10 digits + suffix "01", e.g., SE556012345601). Legislation: ML kapitel 2 &sect;1.
2. **VAT registration status** [T1] -- Standard registered (momsregistrerad), exempt (below threshold), or not registered. Legislation: ML kapitel 2 &sect;1-3.
3. **Filing frequency** [T1] -- Monthly (turnover > SEK 40M), quarterly (SEK 1M-40M), or annual (< SEK 1M). Legislation: SFL 26 kap. 26 &sect;.
4. **Industry/sector** [T2] -- Impacts partial deduction, blocked categories (e.g., construction triggers reverse charge; forestry may use flat-rate scheme). Legislation: ML kapitel 13.
5. **Does the business make exempt supplies (ML kapitel 10)?** [T2] -- If yes, partial deduction (proportionell avdragsratt) applies. Legislation: ML kapitel 13 &sect;29-30.
6. **F-skatt status** [T1] -- Confirms self-employment tax status (relevant for business legitimacy and subcontractor relationships, not VAT directly). Legislation: SFL 9 kap.
7. **Moms credit carried forward from prior period** [T1] -- Previous period's Ruta 49 if negative (overskjutande inganende moms).
8. **Does the business provide byggtjanster (construction services)?** [T1] -- Triggers domestic reverse charge (omvand skattskyldighet). Legislation: ML kapitel 8 &sect;8.
9. **Has the business opted for frivillig skattskyldighet on property rental?** [T2] -- Voluntary VAT on commercial property. Legislation: ML kapitel 9 &sect;1.
10. **Does the business perform ROT/RUT-eligible work?** [T2] -- Hushallsarbete eligible for tax reduction; impacts invoicing but NOT VAT base. Legislation: Lag 2009:194.

For small businesses (annual turnover < SEK 80,000): VAT registration is NOT required. From 1 January 2025, threshold raised to SEK 120,000. Legislation: ML kapitel 2 &sect;1; SFL.

**If items 1-3 are unknown, STOP. Do not classify any transactions until registration type and period are confirmed.**

---

## Section 1: VAT Return Form Structure -- Skattedeklaration (Momsdeklaration)

### 1.1 Overview [T1]

The Swedish VAT return is part of the Skattedeklaration, which is a combined declaration covering moms (VAT), arbetsgivaravgifter (employer contributions), and avdragen skatt (withheld tax). The moms section uses numbered boxes called "rutor" (singular: ruta). The form is filed electronically via Skatteverket e-tjanster.

**Legislation:** SFL 26 kap.; Skatteverkets foreskrifter om skattedeklaration.

### 1.2 Complete Ruta Reference [T1]

#### Section A -- Momspliktig forsaljning eller uttag (Taxable Sales or Deemed Supplies)

| Ruta | Swedish Name | English Translation | Notes |
|------|-------------|---------------------|-------|
| 05 | Momspliktig forsaljning som inte ingar i rutorna 06, 07 eller 08 | Taxable sales not included in boxes 06, 07, or 08 | Standard domestic taxable sales (net amount, excluding moms). ML kapitel 5 &sect;1. |
| 06 | Momspliktiga uttag | Taxable deemed supplies / withdrawals | Self-supply of goods or services for private use or non-business purposes. Net amount. ML kapitel 5 &sect;2-4. |
| 07 | Beskattningsunderlag vid vinstmarginalbeskattning | Tax base under margin scheme | Used by second-hand goods dealers, travel agents, art dealers. Reports the profit margin only. ML kapitel 20 &sect;1-5. |
| 08 | Hyra av verksamhetslokal -- frivillig skattskyldighet | Rental of business premises -- voluntary taxation | Commercial property rental where landlord has opted to charge moms. Net rental amount. ML kapitel 9 &sect;1. |

#### Section B -- Utganende moms pa forsaljning eller uttag (Output VAT on Sales)

Output VAT calculated on the amounts reported in Rutor 05-08:

| Ruta | Rate | Swedish Name | English Translation | Derivation |
|------|------|-------------|---------------------|------------|
| 10 | 25% | Utganende moms 25% | Output VAT at 25% | 25% of amounts in Rutor 05-08 taxed at standard rate. ML kapitel 9 &sect;2. |
| 11 | 12% | Utganende moms 12% | Output VAT at 12% | 12% of amounts in Rutor 05-08 taxed at reduced rate. ML kapitel 9 &sect;3. |
| 12 | 6% | Utganende moms 6% | Output VAT at 6% | 6% of amounts in Rutor 05-08 taxed at lower reduced rate. ML kapitel 9 &sect;4. |

#### Section C -- Momspliktiga inkop vid omvand skattskyldighet (Taxable Purchases -- Reverse Charge)

Net purchase amounts (excluding self-assessed VAT) where the buyer is liable for VAT:

| Ruta | Swedish Name | English Translation | When Used |
|------|-------------|---------------------|-----------|
| 20 | Inkop av varor fran annat EU-land | Intra-Community acquisition of goods | Physical goods purchased from EU supplier, shipped to Sweden. ML kapitel 6 &sect;1. |
| 21 | Inkop av tjanster fran annat EU-land enligt huvudregeln | Acquisition of services from another EU country (general rule) | B2B services from EU suppliers under the general place-of-supply rule. ML kapitel 6 &sect;2. |
| 22 | Inkop av tjanster fran land utanfor EU | Acquisition of services from non-EU country | Services from non-EU suppliers (e.g., US, UK, Norway, Iceland). ML kapitel 6 &sect;3. |
| 23 | Inkop av varor i Sverige som koparen ar skattskyldig for | Purchases of goods in Sweden where buyer is liable | Domestic reverse charge on goods (gold, mobile phones/tablets/laptops > SEK 100,000, emission rights). ML kapitel 8 &sect;6-7. |
| 24 | Ovriga inkop av tjanster | Other purchases of services | Domestic reverse charge on services (construction/byggtjanster). ML kapitel 8 &sect;8. |

#### Section D -- Utganende moms pa inkop (Output VAT on Reverse Charge Purchases)

Self-assessed output VAT on amounts in Rutor 20-24:

| Ruta | Rate | Swedish Name | English Translation | Derivation |
|------|------|-------------|---------------------|------------|
| 30 | 25% | Utganende moms 25% pa inkop | Output VAT at 25% on purchases | 25% of reverse charge base. ML kapitel 9 &sect;2. |
| 31 | 12% | Utganende moms 12% pa inkop | Output VAT at 12% on purchases | 12% of reverse charge base. ML kapitel 9 &sect;3. |
| 32 | 6% | Utganende moms 6% pa inkop | Output VAT at 6% on purchases | 6% of reverse charge base. ML kapitel 9 &sect;4. |

#### Section E -- Forsaljning som ar momsfri (Tax-Free / Exempt Sales)

Net amounts, no output VAT:

| Ruta | Swedish Name | English Translation | When Used |
|------|-------------|---------------------|-----------|
| 35 | Forsaljning av varor till annat EU-land | Supply of goods to another EU country | Intra-Community supply (IC supply). Buyer must be VAT-registered in another EU state. Zero-rated. ML kapitel 10 &sect;1. |
| 36 | Forsaljning av varor utanfor EU | Export of goods outside EU | Exports. Zero-rated with proof of export (customs documentation). ML kapitel 10 &sect;2. |
| 37 | Mellanmans inkop av varor vid trepartshandel | Intermediary's acquisition in triangular trade | Simplified triangulation. Intermediary reports acquisition here. ML kapitel 10 &sect;3. |
| 38 | Forsaljning av tjanster till naringsidkare i annat EU-land enligt huvudregeln | B2B service supply to another EU country (general rule) | Services where place of supply is customer's country. Zero-rated for Swedish seller. ML kapitel 6 &sect;2. |
| 39 | Ovrig forsaljning av varor och tjanster utanfor Sverige | Other sales of goods and services outside Sweden | Catch-all for other non-Swedish supplies (e.g., services to non-EU businesses). ML kapitel 6. |
| 40 | Forsaljning inom Sverige som ar undantagen fran moms | Domestic sales exempt from VAT | Exempt without credit (healthcare, education, financial services, insurance, social care). ML kapitel 10 &sect;4-36. |

#### Section F -- Inganende moms (Input VAT)

| Ruta | Swedish Name | English Translation | Notes |
|------|-------------|---------------------|-------|
| 48 | Inganende moms att dra av | Deductible input VAT | Total input VAT the business is entitled to deduct, including self-assessed reverse charge VAT. ML kapitel 13 &sect;1. |

#### Section G -- Moms att betala eller fa tillbaka (VAT Payable / Refundable)

| Ruta | Swedish Name | English Translation | Calculation |
|------|-------------|---------------------|-------------|
| 49 | Moms att betala eller fa tillbaka | VAT to pay or to receive back | (Ruta 10 + Ruta 11 + Ruta 12 + Ruta 30 + Ruta 31 + Ruta 32) MINUS Ruta 48 |

**If Ruta 49 is positive = moms att betala (VAT to pay to Skatteverket).**
**If Ruta 49 is negative = moms att fa tillbaka (VAT refund from Skatteverket).**

#### Section H -- Beskattningsunderlag vid import (Import Tax Base)

| Ruta | Swedish Name | English Translation | Notes |
|------|-------------|---------------------|-------|
| 50 | Beskattningsunderlag vid import | Tax base for imports | Customs value of imported goods from non-EU countries. Since 2015, import VAT is reported on the momsdeklaration (not paid to Tullverket at border). ML kapitel 7 &sect;8. |

### 1.3 Derived Calculation Formula [T1]

```
Total Output VAT on Sales       = Ruta 10 + Ruta 11 + Ruta 12
Total Output VAT on Purchases   = Ruta 30 + Ruta 31 + Ruta 32
Total Output VAT                = (Ruta 10 + Ruta 11 + Ruta 12) + (Ruta 30 + Ruta 31 + Ruta 32)
Total Deductible Input VAT      = Ruta 48
VAT Payable / Refundable        = Total Output VAT - Total Deductible Input VAT = Ruta 49

Ruta 49 = (Ruta 10 + Ruta 11 + Ruta 12 + Ruta 30 + Ruta 31 + Ruta 32) - Ruta 48

IF Ruta 49 > 0 THEN moms att betala (pay)
IF Ruta 49 < 0 THEN moms att fa tillbaka (refund)
IF Ruta 49 = 0 THEN no payment or refund
```

### 1.4 Periodisk sammanstallning (EC Sales List) [T1]

In addition to the momsdeklaration, businesses making intra-Community supplies of goods (Ruta 35) or B2B services to other EU countries (Ruta 38) must file a Periodisk sammanstallning (EC Sales List). Legislation: SFL 35 kap. 2 &sect;.

| Field | Detail |
|-------|--------|
| Frequency | Monthly (if goods) or quarterly (if services only) |
| Deadline | 25th of month following the reporting period |
| Content | Customer VAT numbers and values of IC supplies |

### 1.5 Intrastat [T1]

Businesses exceeding Intrastat thresholds must file monthly Intrastat declarations for physical goods movements to/from EU countries.

| Direction | Threshold (2025) | Deadline |
|-----------|------------------|----------|
| Dispatches (utforsel) | SEK 4,500,000 | 10th of following month |
| Arrivals (inforsel) | SEK 9,000,000 | 10th of following month |

Legislation: Forordning (2001:100) om den officiella statistiken; Skatteverket guidelines.

---

## Section 2: Transaction Classification Matrix [T1]

### 2.1 Sales Classification Lookup Table

| Transaction Type | Counterparty Location | B2B/B2C | Rate | Sales Ruta | Output VAT Ruta | Legislation |
|-----------------|----------------------|---------|------|-----------|----------------|-------------|
| Standard goods/services sale | Sweden | Any | 25% | 05 | 10 | ML kap. 5 &sect;1, kap. 9 &sect;2 |
| Food/beverage sale (not alcohol) | Sweden | Any | 12% | 05 | 11 | ML kap. 9 &sect;3 |
| Restaurant/catering | Sweden | Any | 12% | 05 | 11 | ML kap. 9 &sect;3 |
| Hotel accommodation | Sweden | Any | 12% | 05 | 11 | ML kap. 9 &sect;3 |
| Books, newspapers, magazines | Sweden | Any | 6% | 05 | 12 | ML kap. 9 &sect;4 |
| Passenger transport | Sweden | Any | 6% | 05 | 12 | ML kap. 9 &sect;4 |
| Cultural events admission | Sweden | Any | 6% | 05 | 12 | ML kap. 9 &sect;4 |
| Sporting events admission | Sweden | Any | 6% | 05 | 12 | ML kap. 9 &sect;4 |
| Deemed supply / private use | Sweden | N/A | Applicable rate | 06 | 10/11/12 | ML kap. 5 &sect;2-4 |
| Margin scheme goods | Sweden | Any | Applicable rate | 07 | 10/11/12 | ML kap. 20 &sect;1-5 |
| Commercial property rental (opted) | Sweden | B2B | 25% | 08 | 10 | ML kap. 9 &sect;1 |
| IC supply of goods | EU | B2B | 0% | 35 | -- | ML kap. 10 &sect;1 |
| Export of goods | Non-EU | Any | 0% | 36 | -- | ML kap. 10 &sect;2 |
| Triangular trade (intermediary) | EU | B2B | 0% | 37 | -- | ML kap. 10 &sect;3 |
| B2B services to EU | EU | B2B | 0% | 38 | -- | ML kap. 6 &sect;2 |
| Other sales outside Sweden | Non-EU/EU | Any | 0% | 39 | -- | ML kap. 6 |
| Exempt domestic sale | Sweden | Any | Exempt | 40 | -- | ML kap. 10 &sect;4-36 |

### 2.2 Purchases Classification Lookup Table -- Domestic (Swedish Supplier)

| Expense Type | Rate on Invoice | Input VAT Ruta | Deductible? | Legislation |
|-------------|----------------|---------------|-------------|-------------|
| General overheads / office supplies | 25% | 48 | Yes (full) | ML kap. 13 &sect;1 |
| Food for resale | 12% | 48 | Yes (full) | ML kap. 13 &sect;1 |
| Books / newspapers for resale | 6% | 48 | Yes (full) | ML kap. 13 &sect;1 |
| Capital asset (anlaggningstillgang) | Applicable rate | 48 | Yes (full, unless blocked) | ML kap. 13 &sect;1 |
| Entertainment / representation | 25% | -- | NO (blocked) | ML kap. 13 &sect;14 |
| Passenger car purchase (mixed use) | 25% | -- | NO (blocked) | ML kap. 13 &sect;18 |
| Passenger car lease (mixed use) | 25% | 48 (50%) | 50% deductible | ML kap. 13 &sect;18-20 |
| Accommodation for staff (permanent) | 25% | -- | NO (blocked) | ML kap. 13 &sect;15 |
| Personal use | Any | -- | NO (blocked) | ML kap. 13 &sect;1 |

### 2.3 Purchases Classification Lookup Table -- EU Supplier (Reverse Charge)

| Purchase Type | Purchase Base Ruta | Output VAT Ruta | Input VAT Ruta | Legislation |
|--------------|-------------------|----------------|---------------|-------------|
| Physical goods from EU | 20 | 30/31/32 | 48 | ML kap. 6 &sect;1, kap. 8 &sect;1 |
| Services from EU (general rule B2B) | 21 | 30/31/32 | 48 | ML kap. 6 &sect;2, kap. 8 &sect;2 |
| Capital assets from EU (>= threshold) | 20 or 21 | 30/31/32 | 48 | ML kap. 6, kap. 13 |
| Local consumption abroad (hotel, taxi) | -- (no entry) | -- | -- | Not reverse charge |

### 2.4 Purchases Classification Lookup Table -- Non-EU Supplier (Reverse Charge)

| Purchase Type | Purchase Base Ruta | Output VAT Ruta | Input VAT Ruta | Legislation |
|--------------|-------------------|----------------|---------------|-------------|
| Services from non-EU (B2B) | 22 | 30/31/32 | 48 | ML kap. 6 &sect;3, kap. 8 &sect;3 |
| Physical goods imported | 50 (import base) | 30/31/32 | 48 | ML kap. 7 &sect;8 |
| Local consumption abroad | -- (no entry) | -- | -- | Not reverse charge |

### 2.5 Domestic Reverse Charge Lookup Table

| Situation | Purchase Base Ruta | Output VAT Ruta | Input VAT Ruta | Legislation |
|-----------|-------------------|----------------|---------------|-------------|
| Construction services (byggtjanster) | 24 | 30/31/32 | 48 | ML kap. 8 &sect;8 |
| Gold (investment gold intermediary) | 23 | 30/31/32 | 48 | ML kap. 8 &sect;6 |
| Mobile phones, tablets, laptops (> SEK 100,000 per invoice) | 23 | 30/31/32 | 48 | ML kap. 8 &sect;7 |
| Emission rights (utslappsratter) | 23 | 30/31/32 | 48 | ML kap. 8 &sect;7 |
| Gaming consoles (> SEK 100,000 per invoice) | 23 | 30/31/32 | 48 | ML kap. 8 &sect;7 |
| Integrated circuits (> SEK 100,000 per invoice) | 23 | 30/31/32 | 48 | ML kap. 8 &sect;7 |

---

## Section 3: VAT Rates [T1]

### 3.1 Standard Rate

| Rate | Name | Scope | Legislation |
|------|------|-------|-------------|
| 25% | Normalskattesats (standard rate) | All goods and services not qualifying for a reduced rate or exemption | ML kapitel 9 &sect;2 |

### 3.2 Reduced Rates

| Rate | Name | Applicable Supplies | Legislation |
|------|------|-------------------|-------------|
| 12% | Reducerad skattesats (reduced rate) | Livsmedel (foodstuffs, excluding alcohol); restaurang- och cateringtjanster (restaurant and catering services); hotellovernatting (hotel accommodation); camping | ML kapitel 9 &sect;3 |
| 6% | Lagsta skattesats (lower reduced rate) | Bocker, tidningar, tidskrifter (books, newspapers, magazines, including e-books and e-newspapers); personbefordran (passenger transport); tilltraden till kulturella evenemang (admission to cultural events including concerts, theatre, cinema); tilltraden till idrottsevenemang (admission to sporting events); skidliftar (ski lifts) | ML kapitel 9 &sect;4 |

### 3.3 Zero-Rated Supplies

| Category | Legislation |
|----------|-------------|
| Export of goods outside EU (with proof of export) | ML kapitel 10 &sect;2 |
| Intra-Community supply of goods (with valid customer VAT number) | ML kapitel 10 &sect;1 |
| International transport services | ML kapitel 10 &sect;5 |
| Supply of ships and aircraft for commercial use | ML kapitel 10 &sect;6 |

### 3.4 Exempt Supplies (Without Credit) [T1]

No output VAT charged; input VAT on related costs is NOT deductible.

| Category | Legislation |
|----------|-------------|
| Sjukvard och tandvard (healthcare and dental care) | ML kapitel 10 &sect;4-5 |
| Social omsorg (social care) | ML kapitel 10 &sect;6 |
| Utbildning (education) | ML kapitel 10 &sect;7-8 |
| Fastighetsuthyrning (property rental -- unless opted for frivillig skattskyldighet) | ML kapitel 10 &sect;9-12 |
| Bank- och finansieringstjanster (banking and financial services) | ML kapitel 10 &sect;13-18 |
| Forsakringstjanster (insurance services) | ML kapitel 10 &sect;19 |
| Kulturell verksamhet (certain cultural activities when provided by public bodies) | ML kapitel 10 &sect;20 |
| Lotterier och vadslagning (lotteries and betting) | ML kapitel 10 &sect;21 |
| Begravningstjanster (funeral services) | ML kapitel 10 &sect;22 |

### 3.5 Rate Verification Note

Rates verified against PWC Tax Summaries (taxsummaries.pwc.com/sweden/corporate/other-taxes) as of April 2026. PWC confirms: 25% standard, 12% reduced (food, hotel, restaurant), 6% reduced (books, newspapers, passenger transport, cultural and sporting events, ski lifts).

---

## Section 4: Blocked Input Tax (Avdragsforbudsregler) [T1]

### 4.1 Blocked Categories Master Table

| Category | Rule | Deductible Amount | Legal Basis |
|----------|------|-------------------|-------------|
| Representation (entertainment) | Fully blocked since 2017. Moms on entertainment/client dining is NOT deductible regardless of amount. | SEK 0 (0%) | ML kapitel 13 &sect;14 |
| Representation -- deductible portion for income tax | For income tax purposes, SEK 300 per person per meal is deductible (excluding moms). But the MOMS on the meal is still NOT deductible for VAT purposes. | Moms: SEK 0 | IL kapitel 16 &sect;2; ML kapitel 13 &sect;14 |
| Personbilar -- purchase (mixed use) | Input VAT on purchase of passenger cars NOT deductible unless the car is used exclusively for business (taxi, driving school, car rental stock, ambulance) or purchased for resale. | SEK 0 (0%) | ML kapitel 13 &sect;18 |
| Personbilar -- lease/rental (mixed use) | 50% of input VAT deductible on lease/rental of passenger cars used for business. | 50% | ML kapitel 13 &sect;18-20 |
| Personbilar -- exclusively business use | 100% deductible if used exclusively for taxable business (taxi, driving school, rental fleet, delivery vehicles classified as lastbil/van). Must be documented. | 100% | ML kapitel 13 &sect;18 |
| Fuel (drivmedel) for blocked vehicles | Same deduction percentage as the underlying vehicle. 0% if car is purchased for mixed use; 50% if car is leased for mixed use; 100% if exclusively business. | Follows vehicle | ML kapitel 13 &sect;18 |
| Stadigvarande bostad (permanent accommodation for staff) | Input VAT on costs related to permanent housing/accommodation for employees is NOT deductible. | SEK 0 (0%) | ML kapitel 13 &sect;15 |
| Personal use (privat bruk) | Any goods or services used for non-business purposes -- input VAT NOT deductible. | SEK 0 (0%) | ML kapitel 13 &sect;1 |
| Exempt supply-related purchases | Input VAT on purchases used to make exempt supplies (ML kapitel 10) is NOT deductible. | SEK 0 (0%) | ML kapitel 13 &sect;7 |

### 4.2 Representation (Entertainment) -- Detailed Rules [T1]

**Critical distinction between income tax deduction and VAT deduction:**

| Aspect | Income Tax (IL) | VAT (ML) |
|--------|----------------|----------|
| Deductible amount per person per meal | SEK 300 (excluding moms) | SEK 0 -- fully blocked |
| Drinks (non-alcoholic, with meal) | Included in SEK 300 limit | Blocked |
| Alcohol | NOT deductible | Blocked |
| Internal representation (staff events) | Partially deductible (SEK 300/person for max 2 events/year) | Blocked |
| Simple business meal (arbetsmaltid, not entertainment) | Fully deductible for income tax | [T2] -- may be deductible if genuinely not entertainment; flag for reviewer |

**Legislation:** ML kapitel 13 &sect;14; IL kapitel 16 &sect;2; Skatteverkets stallningstagande 131 675997-14/111.

**Rule of thumb [T1]:** If the expense description contains words like "representation", "kundmiddag", "lunch med kund", "evenemang for kunder" -- classify as blocked for VAT. The SEK 300 per person limit relates ONLY to income tax deductibility, NOT to moms recovery.

### 4.3 Motor Vehicles -- Decision Tree [T1]

```
Is the vehicle a personbil (passenger car)?
  |
  +-- NO (lastbil, van, truck, motorcycle > 100cc for delivery) --> Full deduction (100%) [ML kap. 13 &sect;1]
  |
  +-- YES
       |
       +-- Purchased?
       |    |
       |    +-- Exclusively business use (taxi, driving school, rental fleet, ambulance)?
       |    |    --> 100% deductible [ML kap. 13 &sect;18]
       |    |
       |    +-- Mixed use or private use?
       |         --> 0% deductible (BLOCKED) [ML kap. 13 &sect;18]
       |
       +-- Leased / Rented?
            |
            +-- Exclusively business use?
            |    --> 100% deductible [ML kap. 13 &sect;18]
            |
            +-- Mixed use?
                 --> 50% deductible [ML kap. 13 &sect;18-20]
```

### 4.4 Electric and Hybrid Company Cars [T2]

Electric vehicles (elbilar) and plug-in hybrids used as company cars (formansbil) follow the same VAT deduction rules as conventional passenger cars. There is NO special VAT rate or enhanced deduction for electric vehicles. The formansvardeberakning (benefit-in-kind calculation) differs for income tax purposes but does NOT affect VAT deduction.

**Legislation:** ML kapitel 13 &sect;18 (no exception for electric vehicles). IL kapitel 61 &sect;5-11 (benefit value calculation -- income tax only, out of scope for VAT).

**Flag [T2]:** If client claims 100% deduction for an electric company car lease, verify that the car is used EXCLUSIVELY for business. The fact that it is electric does not change the 50% mixed-use rule.

---

## Section 5: VAT Registration [T1]

### 5.1 Registration Threshold

| Period | Threshold | Legislation |
|--------|-----------|-------------|
| Before 1 January 2025 | SEK 80,000 annual turnover | ML kapitel 2 &sect;1 (old) |
| From 1 January 2025 | SEK 120,000 annual turnover | ML kapitel 2 &sect;1 (amended by SFS 2024:XXX) |

### 5.2 Momsregistreringsnummer Format [T1]

| Element | Format | Example |
|---------|--------|---------|
| Country prefix | SE | SE |
| Organisationsnummer (10 digits) | NNNNNNNNNN | 5560123456 |
| Suffix | 01 | 01 |
| Full VAT number | SE + 12 digits | SE556012345601 |

**Legislation:** ML kapitel 2 &sect;1; EU Council Regulation 904/2010.

### 5.3 Registration Rules [T1]

| Situation | Registration Required? | Legislation |
|-----------|----------------------|-------------|
| Annual turnover >= SEK 120,000 (from 2025) | YES -- mandatory | ML kapitel 2 &sect;1 |
| Annual turnover < SEK 120,000 | NO -- optional (voluntary registration permitted) | ML kapitel 2 &sect;1 |
| Making intra-Community acquisitions exceeding SEK 120,000 | YES | ML kapitel 2 &sect;3 |
| Receiving services subject to reverse charge | YES (for reverse charge reporting only) | ML kapitel 8 |
| Non-established businesses making taxable supplies in Sweden | YES | ML kapitel 2 &sect;2 |

### 5.4 EU-Wide SME Scheme (from 2025) [T2]

From 2025, the EU SME scheme allows small businesses established in one EU member state to benefit from VAT exemption in other member states, subject to conditions (EU-wide turnover ceiling EUR 100,000 and domestic ceiling). This is a new mechanism. Flag for reviewer if client wishes to apply cross-border SME exemption.

**Legislation:** EU Directive 2020/285; Swedish implementing legislation pending full codification.

---

## Section 6: Filing Deadlines [T1]

### 6.1 Filing Frequency Determination

| Annual Turnover (Omsattning) | Filing Frequency | Legislation |
|------------------------------|-----------------|-------------|
| > SEK 40,000,000 | Monthly (manatlig) | SFL 26 kap. 26 &sect; |
| SEK 1,000,001 -- SEK 40,000,000 | Quarterly (kvartalsvis) -- may opt for monthly | SFL 26 kap. 26 &sect; |
| <= SEK 1,000,000 | Annual (arsvis) -- may opt for quarterly or monthly | SFL 26 kap. 26 &sect; |

### 6.2 Monthly Filing Deadlines [T1]

| Reporting Period | Deadline | Special Rule |
|-----------------|----------|-------------|
| January | 26 February | -- |
| February | 12 April | Extended to 12th (not 26th) |
| March | 26 April | -- |
| April | 26 May | -- |
| May | 26 June | -- |
| June | 17 August | Extended (July is semester/vacation) |
| July | 26 August | -- |
| August | 26 September | -- |
| September | 26 October | -- |
| October | 26 November | -- |
| November | 27 December | Extended by 1 day (26 Dec is holiday) |
| December | 26 January (following year) | -- |

**Note:** The 12th is the deadline for the February return specifically for large companies (turnover > SEK 40M). For smaller monthly filers, the 26th applies uniformly. Legislation: SFL 26 kap. 26-28 &sect;.

### 6.3 Quarterly Filing Deadlines [T1]

| Quarter | Period | Deadline | Legislation |
|---------|--------|----------|-------------|
| Q1 | January -- March | 12 May | SFL 26 kap. 26 &sect; |
| Q2 | April -- June | 17 August | SFL 26 kap. 26 &sect; |
| Q3 | July -- September | 12 November | SFL 26 kap. 26 &sect; |
| Q4 | October -- December | 12 February (following year) | SFL 26 kap. 26 &sect; |

### 6.4 Annual Filing Deadline [T1]

| Entity Type | Period | Deadline | Legislation |
|-------------|--------|----------|-------------|
| Sole proprietor (enskild firma) | Calendar year | 12 May of following year | SFL 26 kap. 26 &sect; |
| Limited company (aktiebolag) | Financial year | Varies by financial year-end; typically 12th of month 6 or 7 after year-end | SFL 26 kap. 26 &sect; |

### 6.5 Penalties for Late Filing and Payment [T1]

| Penalty Type | Swedish Name | Amount / Rate | Legislation |
|-------------|-------------|---------------|-------------|
| Late filing penalty | Forseningsavgift | SEK 625 per missed deadline (can accumulate: SEK 625 after 3 months, additional SEK 625 after 5 months) | SFL 48 kap. 1-3 &sect; |
| Tax surcharge (incorrect information) | Skattetillagg | 20% of the tax amount that would have been avoided due to incorrect information | SFL 49 kap. 4 &sect; |
| Tax surcharge (periodic returns) | Skattetillagg (periodiskt) | 5% for periodic returns (momsdeklaration) if the error is corrected before Skatteverket discovers it -- reduced surcharge may apply | SFL 49 kap. 11 &sect; |
| Late payment interest | Kostnadsranta | Reference rate + 15 percentage points per year (calculated daily) | SFL 65 kap. 4 &sect; |

### 6.6 Correction of Errors [T1]

Errors in previously filed momsdeklaration should be corrected in the next period's declaration (if the error is < SEK 500,000). For errors >= SEK 500,000, a separate correction declaration (rattad deklaration) must be filed. Legislation: SFL 26 kap. 31 &sect;.

---

## Section 7: Reverse Charge -- Omvand Skattskyldighet [T1]

### 7.1 Reverse Charge Mechanics

For all reverse charge situations, the buyer (not the seller) is liable for VAT:

1. Report net purchase amount in the relevant ruta (20-24 or 50)
2. Self-assess output moms at the applicable Swedish rate in Ruta 30/31/32
3. Deduct the same amount as input moms in Ruta 48 (if fully entitled to deduction)
4. Net effect: zero for fully taxable businesses

**Legislation:** ML kapitel 8 &sect;1-8.

### 7.2 Reverse Charge Situations Master Table

| Situation | Seller/Supplier | Buyer | Purchase Ruta | Output VAT Ruta | Input VAT Ruta | Legislation |
|-----------|----------------|-------|--------------|----------------|---------------|-------------|
| Intra-Community acquisition of goods | EU business | SE business | 20 | 30/31/32 | 48 | ML kap. 6 &sect;1, kap. 8 &sect;1 |
| B2B services from EU (general rule) | EU business | SE business | 21 | 30/31/32 | 48 | ML kap. 6 &sect;2, kap. 8 &sect;2 |
| Services from non-EU | Non-EU business | SE business | 22 | 30/31/32 | 48 | ML kap. 6 &sect;3, kap. 8 &sect;3 |
| Domestic -- goods (gold, electronics > SEK 100,000) | SE business | SE business | 23 | 30/31/32 | 48 | ML kap. 8 &sect;6-7 |
| Domestic -- construction services (byggtjanster) | SE subcontractor | SE main contractor | 24 | 30/31/32 | 48 | ML kap. 8 &sect;8 |
| Import of goods | Non-EU supplier | SE business | 50 | 30/31/32 | 48 | ML kap. 7 &sect;8 |

### 7.3 Construction Reverse Charge -- Byggtjanster (ROT) [T1]

**This is one of the most common Swedish-specific reverse charge situations.**

Conditions for domestic reverse charge on construction services:
1. The service must qualify as a byggtjanst (construction, renovation, repair, maintenance of buildings/land). ML kapitel 8 &sect;8.
2. The buyer must be a naringsidkare (business entity) that itself provides byggtjanster on more than an occasional basis.
3. The subcontractor invoices WITHOUT moms. The invoice must state "omvand skattskyldighet" (reverse charge).
4. The buyer self-assesses output VAT and claims input VAT.

**Services that ARE byggtjanster [T1]:**
- Building construction (nybyggnad)
- Renovation (renovering)
- Repair and maintenance of buildings (reparation och underhall)
- Demolition (rivning)
- Installation of heating, plumbing, electricity in buildings
- Road construction (vagbyggnad)
- Painting, plastering, flooring
- Scaffolding (stallningsbyggnad)
- Land preparation, excavation (markarbete, schaktning)

**Services that are NOT byggtjanster [T1]:**
- Architecture and engineering design (only advisory, not physical work)
- Cleaning (stadning) -- unless part of a construction project
- Landscaping/gardening (tradgardsarbete) -- classified separately
- Equipment rental without operator

### 7.4 Gold Reverse Charge [T1]

Applies to trading in investment gold (investeringsguld) between businesses. The seller does not charge moms; the buyer self-assesses. Legislation: ML kapitel 8 &sect;6; ML kapitel 20a.

### 7.5 Electronics Reverse Charge [T1]

Applies to B2B sales within Sweden of mobile phones (mobiltelefoner), tablets (surfplattor), laptops (barbare datorer), gaming consoles (spelkonsoler), and integrated circuits (integrerade kretsar) when the invoice amount (excluding VAT) exceeds SEK 100,000 per invoice. Below this threshold, normal VAT rules apply. Legislation: ML kapitel 8 &sect;7.

### 7.6 Reverse Charge Exceptions [T1]

| Situation | Treatment | Legislation |
|-----------|-----------|-------------|
| Out-of-scope (salaries, loans, dividends) | NEVER reverse charge | ML kap. 3 |
| Local consumption abroad (hotel, restaurant, taxi in another country) | NOT reverse charge -- foreign VAT paid at source, irrecoverable | ML kap. 6 |
| Non-registered buyer (below threshold, not registered) | Reverse charge does NOT apply -- supplier must charge Swedish moms | ML kap. 8 |
| EU supplier charged their local VAT > 0% | NOT reverse charge -- treat as cost including foreign VAT | ML kap. 8 |
| B2C services from EU/non-EU | Not reverse charge for consumer -- supplier must register or use OSS | ML kap. 6 |

---

## Section 8: Edge Case Registry

### EC1 -- EU hotel / restaurant abroad [T1]
**Situation:** Client pays hotel in Germany. Invoice shows German USt (Umsatzsteuer).
**Resolution:** NOT reverse charge. Foreign VAT was charged and paid at source. No entry on Swedish momsdeklaration. The German VAT is an irrecoverable cost embedded in the expense. Client can apply for refund via EU VAT refund portal (Directive 2008/9/EC) if the amount is material.
**Legislation:** ML kapitel 6 (place of supply for immovable property and restaurant services is where the property/restaurant is located).

### EC2 -- SaaS subscription from US provider [T1]
**Situation:** US company (e.g., AWS, Notion), SEK 1,000/month, no moms on invoice.
**Resolution:** Reverse charge applies. Non-EU B2B service.
- Ruta 22 = SEK 1,000 (non-EU services base)
- Ruta 30 = SEK 250 (output moms at 25%)
- Ruta 48 includes SEK 250 (input moms)
- Net effect = zero for fully taxable business.
**Legislation:** ML kapitel 6 &sect;3; ML kapitel 8 &sect;3.

### EC3 -- Construction subcontracting (byggtjanster) [T1]
**Situation:** Subcontractor provides byggtjanster to main contractor. Both are SE-registered businesses that regularly provide construction services.
**Resolution:** Domestic reverse charge (omvand skattskyldighet). Subcontractor invoices WITHOUT moms and states "Omvand skattskyldighet for byggtjanster" on invoice.
- Client (main contractor): Ruta 24 = net amount. Ruta 30 = output moms at 25%. Ruta 48 includes the same amount. Net = zero.
**Legislation:** ML kapitel 8 &sect;8.

### EC4 -- Passenger car lease, 50% deductible [T1]
**Situation:** Client leases a personbil. Monthly lease SEK 5,000 + SEK 1,250 moms (25%).
**Resolution:** 50% deductible (mixed business/private use).
- Ruta 48 includes SEK 625 (50% of SEK 1,250). Remaining SEK 625 is non-deductible (treated as a cost).
**Legislation:** ML kapitel 13 &sect;18-20.

### EC5 -- Entertainment / representation dinner [T1]
**Situation:** Client hosts dinner for customers. Bill SEK 3,000 + SEK 750 moms.
**Resolution:** Moms is NOT deductible. Since 2017, ALL entertainment moms is blocked.
- Ruta 48 = SEK 0 for this expense. The full SEK 3,750 is a cost.
- For income tax: SEK 300 per person is deductible as a business expense (up to a reasonable number of guests), but this does NOT affect VAT.
**Legislation:** ML kapitel 13 &sect;14; IL kapitel 16 &sect;2.

### EC6 -- Intra-Community supply of goods [T1]
**Situation:** Client sells goods to Finnish business (VAT-registered in Finland), ships SE to FI.
**Resolution:** Zero-rated IC supply.
- Ruta 35 = net sales amount. No output moms (Rutor 10/11/12 = 0 for this transaction).
- Must file Periodisk sammanstallning (EC Sales List) with Finnish customer's VAT number.
- Must retain proof of transport (CMR, bill of lading).
**Legislation:** ML kapitel 10 &sect;1.

### EC7 -- Norwegian customer (non-EU) [T1]
**Situation:** Client sells services to Norwegian business.
**Resolution:** Norway is NON-EU (EEA but NOT part of the EU VAT area). Report in Ruta 39 (other sales outside Sweden). No output moms.
- Do NOT report in Ruta 38 (which is for EU B2B services only).
- For goods: report in Ruta 36 (export) with customs documentation.
**Legislation:** ML kapitel 6; ML kapitel 10 &sect;2.

### EC8 -- Credit notes (kreditfaktura) [T1]
**Situation:** Client receives a credit note from a supplier for returned goods.
**Resolution:** Reduce Ruta 48 (input moms) by the credit note moms amount. Adjust the corresponding purchase base rutor accordingly. If the credit note relates to a reverse charge purchase, reduce BOTH the output VAT (Ruta 30/31/32) and input VAT (Ruta 48) by the same amount.
**Legislation:** ML kapitel 11 &sect;10-12.

### EC9 -- Voluntary taxation on property rental (frivillig skattskyldighet) [T2]
**Situation:** Client has opted for frivillig skattskyldighet on commercial property rental (verksamhetslokal).
**Resolution:** Report rental income in Ruta 08. Output moms at 25% in Ruta 10. Input moms on property-related expenses (maintenance, renovation, utilities) deductible in Ruta 48.
**Flag for reviewer:** Confirm opt-in is registered with Skatteverket. The property must be used by the tenant for taxable activities. If tenant makes exempt supplies, landlord's deduction may be restricted. The jamnkning (adjustment) rules apply for 10 years on capital expenditure.
**Legislation:** ML kapitel 9 &sect;1; ML kapitel 13 &sect;31-38 (jamnkning/adjustment).

### EC10 -- ROT-avdrag interaction with VAT [T2]
**Situation:** Client (a construction company) performs ROT-eligible renovation work for a private individual (konsument). The homeowner claims ROT-avdrag (tax reduction for renovation).
**Resolution:**
- The ROT-avdrag is a tax reduction for the BUYER (homeowner) against income tax. It does NOT reduce the VAT base.
- The construction company invoices the full amount INCLUDING moms at 25%.
- The ROT-avdrag portion is paid by Skatteverket directly to the company (after deduction from the homeowner's tax).
- For VAT purposes: the FULL net amount (before ROT reduction) is reported in Ruta 05. Output moms at 25% in Ruta 10.
- ROT-avdrag does NOT reduce the momspliktig forsaljning.
**Legislation:** Lag (2009:194) om forfarandet vid skattereduktion for hushallsarbete; ML kapitel 5 &sect;1.

### EC11 -- RUT-avdrag interaction with VAT [T2]
**Situation:** Client performs RUT-eligible household services (stadning, tradgardsarbete, barnpassning) for a private individual.
**Resolution:** Same principle as ROT. The RUT-avdrag reduces the homeowner's income tax, NOT the VAT base. The service company reports full net amount in Ruta 05 and output moms at 25% in Ruta 10.
**Legislation:** Lag (2009:194); ML kapitel 5 &sect;1.

### EC12 -- Forest and agriculture flat-rate scheme (skogbruk/jordbruk) [T3]
**Situation:** Client is a small forestry or agricultural business eligible for the EU flat-rate scheme for farmers.
**Resolution:** ESCALATE. Sweden has historically not implemented the EU flat-rate farmer scheme (Article 295-305 of the VAT Directive). Most Swedish farmers are standard VAT-registered. However, specific rules apply to timber sales from private forests (skogsavdrag). Complex interaction between income tax deductions and VAT.
**Legislation:** ML kapitel 9; IL kapitel 21 (skogsavdrag -- income tax); EU VAT Directive Articles 295-305.

### EC13 -- Electric company car -- formansvardering [T2]
**Situation:** Company provides an electric car (elbil) as a benefit to an employee. The company leases the car and claims 50% moms deduction.
**Resolution:**
- VAT: 50% of lease moms is deductible in Ruta 48 (standard mixed-use rule for personbilar). No enhanced deduction for electric vehicles.
- The charging costs (laddning) follow the vehicle: 50% deductible if the car is leased for mixed use.
- If the company installs a charging station at the employee's home: input VAT on installation may be blocked under ML kapitel 13 &sect;15 (stadigvarande bostad). Flag for reviewer.
- Formansvardeberakning (benefit value): different for income tax (lower value for electric cars) but IRRELEVANT for VAT.
**Legislation:** ML kapitel 13 &sect;18-20 (VAT deduction); IL kapitel 61 &sect;5-11 (income tax benefit value -- out of scope).

### EC14 -- Real estate option to tax -- transitioning in/out [T3]
**Situation:** Client is considering opting in or opting out of frivillig skattskyldighet on a commercial property.
**Resolution:** ESCALATE. The jamnkningsregler (adjustment rules) require adjustment of input VAT on capital expenditure over a 10-year period (korrigeringstid). Opting out triggers a potential repayment of previously deducted input VAT. Opting in triggers the right to deduct input VAT on future expenditure and potentially on past expenditure (within the 10-year window). This requires specialist property tax advice.
**Legislation:** ML kapitel 13 &sect;31-38 (jamnkning); ML kapitel 9 &sect;1 (frivillig skattskyldighet).

### EC15 -- VAT group (mervardesskattgrupp) [T3]
**Situation:** Client is a financial institution that is part of a VAT group.
**Resolution:** ESCALATE. Financial institutions (banks, insurance companies) can form VAT groups where intra-group supplies are disregarded for VAT purposes. The group is treated as a single taxable person. Complex registration and reporting rules apply. Only available for financial sector entities.
**Legislation:** ML kapitel 4 &sect;1-6 (mervardesskattgrupp).

### EC16 -- Margin scheme (vinstmarginalbeskattning) [T2]
**Situation:** Client is a second-hand goods dealer (begagnade varor) who purchased items from private individuals (without moms).
**Resolution:** Report the profit margin (not the full sales price) in Ruta 07. Output moms is calculated on the margin only. No input VAT was charged on the purchase from the private individual.
- Margin = selling price minus purchase price.
- Ruta 07 = margin amount. Output moms at applicable rate in Ruta 10/11/12.
- Cannot mix normal taxation and margin scheme on the same item.
**Legislation:** ML kapitel 20 &sect;1-5.

### EC17 -- Import VAT on momsdeklaration (since 2015) [T1]
**Situation:** Client imports goods from non-EU country (e.g., China, USA, UK).
**Resolution:** Since 1 January 2015, import VAT is reported on the momsdeklaration (not paid to Tullverket at the border for businesses registered for moms).
- Ruta 50 = customs value (tullvarde) including customs duty and other charges.
- Ruta 30/31/32 = output moms at applicable rate on the customs value.
- Ruta 48 = input moms (same amount, if fully deductible).
- Net effect = zero for fully taxable businesses.
**Legislation:** ML kapitel 7 &sect;8; SFL 26 kap.

### EC18 -- Distance sales to Swedish consumers (OSS) [T2]
**Situation:** Foreign EU seller makes distance sales of goods to Swedish consumers exceeding EUR 10,000 EU-wide threshold.
**Resolution:** The seller must either register for Swedish VAT or use the One-Stop Shop (OSS) mechanism to report and pay Swedish moms. If using OSS, the seller reports via their home country's portal. If the client IS the Swedish buyer (a business), normal IC acquisition rules apply (Ruta 20).
**Legislation:** ML kapitel 5 &sect;7-10; EU OSS rules (Council Directive 2017/2455).

---

## Section 9: Test Suite

### Test 1 -- Standard domestic purchase, 25% moms [T1]
**Input:** Swedish supplier, office supplies, gross SEK 2,500, moms SEK 500, net SEK 2,000. Fully taxable business.
**Expected output:** Ruta 48 = SEK 500 (input moms deductible). No entry in Rutor 05-12 or 20-32 (this is a purchase, not a sale, and not reverse charge).

### Test 2 -- US software subscription, reverse charge [T1]
**Input:** US provider (AWS), SEK 1,000/month, no moms on invoice. Fully taxable Article 10-equivalent SE business.
**Expected output:**
- Ruta 22 = SEK 1,000 (non-EU services base)
- Ruta 30 = SEK 250 (output moms at 25%)
- Ruta 48 includes SEK 250 (input moms)
- Net effect on Ruta 49 = zero

### Test 3 -- Intra-Community goods acquisition [T1]
**Input:** German supplier ships goods to SE, EUR 5,000 (~SEK 57,500), no moms on invoice. Fully taxable business.
**Expected output:**
- Ruta 20 = SEK 57,500 (IC acquisition base)
- Ruta 30 = SEK 14,375 (output moms at 25%)
- Ruta 48 includes SEK 14,375 (input moms)
- Net effect on Ruta 49 = zero

### Test 4 -- EU B2B sale of goods [T1]
**Input:** Client sells goods to Danish business SEK 30,000, ships SE to DK. Danish customer is VAT-registered.
**Expected output:**
- Ruta 35 = SEK 30,000 (IC supply of goods)
- No output moms (Rutor 10/11/12 = 0 for this transaction)
- Must file Periodisk sammanstallning with Danish customer's VAT number

### Test 5 -- Unregistered small business purchase [T1]
**Input:** Business with annual turnover SEK 80,000 (below SEK 120,000 threshold from 2025), NOT registered for moms, buys supplies SEK 5,000 + SEK 1,250 moms.
**Expected output:** No momsdeklaration filing. No moms recovery. The SEK 6,250 is a full cost.

### Test 6 -- Passenger car lease, 50% deductible [T1]
**Input:** Client leases a personbil. Monthly lease SEK 5,000 + SEK 1,250 moms. Mixed business/private use.
**Expected output:**
- Ruta 48 includes SEK 625 (50% of SEK 1,250)
- Remaining SEK 625 is a non-deductible cost

### Test 7 -- EU hotel, local consumption [T1]
**Input:** Client pays hotel in France SEK 3,000 including French TVA.
**Expected output:** No Swedish momsdeklaration entry. French TVA is irrecoverable (can apply via EU VAT refund portal separately). Expense = SEK 3,000 gross.

### Test 8 -- Entertainment / representation, blocked [T1]
**Input:** Client dinner with customers: food SEK 2,400 + moms SEK 600 (25%). 4 guests, SEK 600 per person net.
**Expected output:**
- Ruta 48 = SEK 0 for this expense. Moms BLOCKED since 2017.
- For income tax: SEK 300 per person x 4 = SEK 1,200 deductible. But moms on that portion is STILL not deductible for VAT.

### Test 9 -- Construction reverse charge (byggtjanster) [T1]
**Input:** Subcontractor invoices main contractor SEK 200,000 for renovation work (byggtjanst). Both are SE-registered construction businesses. Invoice states "Omvand skattskyldighet".
**Expected output:**
- Ruta 24 = SEK 200,000 (domestic reverse charge services)
- Ruta 30 = SEK 50,000 (output moms at 25%)
- Ruta 48 includes SEK 50,000 (input moms)
- Net effect on Ruta 49 = zero

### Test 10 -- ROT-avdrag, full VAT on full amount [T1]
**Input:** Construction company performs kitchen renovation for a homeowner. Total: net SEK 100,000 (labour SEK 60,000 + materials SEK 40,000). Moms 25% = SEK 25,000. Homeowner claims ROT-avdrag on labour (30% of SEK 60,000 = SEK 18,000 tax reduction).
**Expected output:**
- Ruta 05 = SEK 100,000 (FULL net amount, NOT reduced by ROT)
- Ruta 10 = SEK 25,000 (output moms at 25% on FULL amount)
- ROT-avdrag does NOT reduce VAT base

### Test 11 -- Food sale at 12% [T1]
**Input:** Restaurant sells meals, net SEK 50,000 for the period. 12% moms.
**Expected output:**
- Ruta 05 = SEK 50,000 (taxable sales)
- Ruta 11 = SEK 6,000 (output moms at 12%)

### Test 12 -- Book sale at 6% [T1]
**Input:** Bookshop sells books, net SEK 20,000 for the period. 6% moms.
**Expected output:**
- Ruta 05 = SEK 20,000 (taxable sales)
- Ruta 12 = SEK 1,200 (output moms at 6%)

### Test 13 -- Exempt sale (financial services) [T1]
**Input:** Financial advisory firm provides exempt advisory services to Swedish clients, SEK 500,000.
**Expected output:**
- Ruta 40 = SEK 500,000 (exempt domestic sales)
- No output moms
- Input VAT on related costs is NOT deductible (ML kapitel 13 &sect;7)

### Test 14 -- Import from China (since 2015 rules) [T1]
**Input:** Client imports goods from China. Customs value (including duty) SEK 100,000. Standard rate goods.
**Expected output:**
- Ruta 50 = SEK 100,000 (import base)
- Ruta 30 = SEK 25,000 (output moms at 25%)
- Ruta 48 includes SEK 25,000 (input moms, if fully deductible)
- Net effect on Ruta 49 = zero

### Test 15 -- Mixed taxable and exempt supplies, partial deduction [T2]
**Input:** Business makes SEK 800,000 taxable supplies and SEK 200,000 exempt supplies. Total input VAT for the period = SEK 50,000.
**Expected output:**
- Pro-rata recovery: 800,000 / 1,000,000 = 80%
- Ruta 48 = SEK 40,000 (80% of SEK 50,000)
- **Flag for reviewer:** Confirm pro-rata rate and method. Annual adjustment may be required.
**Legislation:** ML kapitel 13 &sect;29-30.

---

## Section 10: Comparison with Malta

| Feature | Sweden (SE) | Malta (MT) |
|---------|-------------|------------|
| **Primary legislation** | Mervardeskattelagen (ML) 2023:200 | VAT Act Chapter 406 |
| **Tax authority** | Skatteverket | Commissioner for Revenue (CFR) |
| **Standard rate** | 25% (ML kap. 9 &sect;2) | 18% |
| **Reduced rates** | 12% (food, hotel, restaurant); 6% (books, transport, culture, sports) (ML kap. 9 &sect;3-4) | 7% (accommodation); 5% (electricity, certain supplies); 12% (rare) |
| **VAT number format** | SE + 12 digits (organisationsnummer + 01) | MT + 8 digits |
| **Registration threshold** | SEK 120,000 (~EUR 10,500) from 2025 (ML kap. 2 &sect;1) | EUR 35,000 (Article 11); EUR 0 for Article 10 (no threshold for standard registration) |
| **Filing form** | Skattedeklaration (momsdeklaration) -- combined with employer contributions | VAT3 (quarterly) or Article 11 declaration (annual, simplified) |
| **Filing frequency** | Monthly (> SEK 40M), quarterly (SEK 1M-40M), annual (< SEK 1M) (SFL 26 kap. 26) | Quarterly (Article 10), Annual (Article 11), Monthly (Article 12) |
| **Filing portal** | Skatteverket e-tjanster | CFR Online (cfr.gov.mt) |
| **Box system** | Rutor (numbered boxes: 05-50) | Boxes (numbered 1-45) |
| **Derived calculation** | Ruta 49 = total output - Ruta 48 | Box 42 (excess credit) or Box 43 (tax payable) |
| **Capital goods threshold** | No specific threshold for VAT purposes (jamnkning applies to fastigheter over 10 years) (ML kap. 13 &sect;31-38) | EUR 1,160 gross (Article 24) |
| **Entertainment VAT** | Fully blocked since 2017 (ML kap. 13 &sect;14) | Blocked under 10th Schedule Item 3(1)(b) |
| **Motor vehicles** | Purchase: blocked (unless exclusively business). Lease: 50% deductible (ML kap. 13 &sect;18-20) | Blocked under 10th Schedule Item 3(1)(a)(iv-v), exceptions for taxi/delivery/rental |
| **Domestic reverse charge** | Construction (byggtjanster), gold, electronics > SEK 100,000, emission rights (ML kap. 8 &sect;6-8) | Not commonly used domestically |
| **Import VAT** | Reported on momsdeklaration since 2015 (ML kap. 7 &sect;8) | Paid at customs (C88 document), recoverable on VAT3 |
| **Late filing penalty** | Forseningsavgift SEK 625 (SFL 48 kap.) | Administrative penalty under CFR rules |
| **Tax surcharge** | Skattetillagg 20% / 5% reduced (SFL 49 kap.) | No direct equivalent at same rates |
| **Property rental opt-in** | Frivillig skattskyldighet -- landlord charges moms at 25% (ML kap. 9 &sect;1) | Not available in same form |
| **ROT/RUT equivalent** | ROT-avdrag (renovation) and RUT-avdrag (household services) -- tax reduction for buyer, does NOT reduce VAT base | No equivalent scheme |
| **Small enterprise scheme** | Below threshold: no registration required, no moms charged/recovered | Article 11: simplified 4-box annual declaration, no VAT recovery |
| **Partial exemption** | Proportionell avdragsratt (ML kap. 13 &sect;29-30) | Pro-rata under Article 22(4) |
| **EC Sales List** | Periodisk sammanstallning (SFL 35 kap.) | Recapitulative Statement |
| **Currency** | SEK (Swedish Krona) | EUR (Euro) |

---

## Section 11: PROHIBITIONS [T1]

1. **NEVER** let AI guess ruta numbers -- they are 100% deterministic from the facts of the transaction. ML kapitel 5-10 determine sales classification; ML kapitel 6, 8 determine reverse charge; ML kapitel 13 determines deductibility.
2. **NEVER** allow non-registered businesses (below SEK 120,000 threshold, not registered) to recover input moms. ML kapitel 2 &sect;1; ML kapitel 13 &sect;1.
3. **NEVER** apply reverse charge to out-of-scope categories (salaries, loans, dividends, social contributions). ML kapitel 3.
4. **NEVER** apply reverse charge to local consumption abroad (hotel, restaurant, taxi in another country). ML kapitel 6.
5. **NEVER** deduct moms on entertainment/representation -- fully blocked since 2017. ML kapitel 13 &sect;14.
6. **NEVER** deduct moms on passenger car purchases unless the car is used exclusively for business (taxi, driving school, rental fleet, ambulance) or purchased for resale. ML kapitel 13 &sect;18.
7. **NEVER** deduct more than 50% of moms on passenger car lease/rental without proving exclusive business use. ML kapitel 13 &sect;18-20.
8. **NEVER** confuse Norway or Iceland (Non-EU / EEA only) with EU member states for reverse charge purposes. They are treated as non-EU (Ruta 22 for services, Ruta 36/39 for sales). ML kapitel 6.
9. **NEVER** reduce the VAT base by ROT-avdrag or RUT-avdrag amounts. The tax reduction is an income tax matter for the buyer, NOT a moms reduction for the seller. Lag (2009:194); ML kapitel 5 &sect;1.
10. **NEVER** apply construction reverse charge (byggtjanster) when the buyer does NOT regularly provide construction services. ML kapitel 8 &sect;8.
11. **NEVER** apply electronics/gold domestic reverse charge when the invoice amount is below SEK 100,000 (excluding VAT). ML kapitel 8 &sect;7.
12. **NEVER** compute any number -- all arithmetic is handled by the deterministic engine, not Claude. Claude assigns rutor and flags issues; the engine calculates amounts.
13. **NEVER** report import VAT as paid to Tullverket for a moms-registered business -- since 2015, import VAT is reported on the momsdeklaration. ML kapitel 7 &sect;8.
14. **NEVER** mix margin scheme (vinstmarginalbeskattning, Ruta 07) with normal taxation on the same item. ML kapitel 20 &sect;1.
15. **NEVER** classify the representation SEK 300 per person limit as a VAT deduction threshold -- it is ONLY for income tax. ML kapitel 13 &sect;14; IL kapitel 16 &sect;2.

---

## Step 12: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Auktoriserad revisor or godkand revisor must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to auktoriserad revisor. Document gap.
```

---

## Step 13: Out of Scope -- Direct Tax (Reference Only) [T3]

This skill does not compute income tax. The following is reference information only. Do not execute any of these rules. Escalate to auktoriserad revisor.

- **Bolagsskatt (corporate tax):** 20.6% flat rate for aktiebolag (limited companies). IL kapitel 65.
- **Inkomstskatt (income tax):** Progressive for individuals: kommunalskatt ~30-34% + statlig inkomstskatt 20% above SEK 598,500 (2025). IL kapitel 65.
- **Arbetsgivaravgifter (employer social contributions):** ~31.42% of gross salary. Socialavgiftslagen (2000:980).
- **Egenavgifter (self-employment contributions):** ~28.97%. Socialavgiftslagen.
- **F-skatt:** Tax status for self-employed. Confirms responsibility for own preliminary tax payments. SFL 9 kap.
- **Kapitalinkomstskatt (capital gains tax):** 30% on capital income. IL kapitel 42.

---

## Step 14: F-skatt (Reference Only)

F-skatt (foretagarskatt) is a tax STATUS, not a tax type. It indicates the holder is responsible for paying their own preliminary tax and social contributions. It is NOT directly related to moms but is critical for business relationships -- customers prefer suppliers with F-skatt approval to avoid withholding obligations (payment liability risk). SFL 9 kap.

---

## Contribution Notes

Adapted from the Malta VAT Return Skill template. All legislation references, ruta numbers, thresholds, rates, blocked categories, and reverse charge rules are specific to Sweden. Rates verified against PWC Tax Summaries (April 2026).

**A skill may not be published without sign-off from an auktoriserad revisor or godkand revisor in Sweden.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
