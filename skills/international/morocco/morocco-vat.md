---
name: morocco-vat
description: Use this skill whenever asked to prepare, review, or create a Morocco VAT (TVA) return for any client. Trigger on phrases like "prepare VAT return", "TVA Maroc", "DGI return", "declaration TVA", or any request involving Morocco VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Morocco VAT classification rules with its two-rate structure (20%/10%, converged from the former 20%/14%/10%/7% by 2026), return form mappings, deductibility rules, reverse charge treatment, registration thresholds, and filing deadlines. ALWAYS read this skill before touching any Morocco VAT-related work.
---

# Morocco VAT (TVA) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Morocco (Kingdom of Morocco) |
| Jurisdiction Code | MA |
| Primary Legislation | Code Général des Impôts (CGI), Titre III -- Taxe sur la Valeur Ajoutée (Art. 87-125) |
| Supporting Legislation | Loi de Finances annuelle; Code des Douanes et Impôts Indirects |
| Tax Authority | Direction Générale des Impôts (DGI) |
| Filing Portal | https://portail.tax.gov.ma (SIMPL portal) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by a licensed expert-comptable in Morocco |
| Validation Date | Pending |
| Skill Version | 2.0 |
| Confidence Coverage | Tier 1: rate application (2 rates: 20%/10%, from 2026), return mapping, registration, deadlines, blocked categories, rule of offset (décalage). Tier 2: partial exemption, mixed supplies, real estate, financial sector, transitional rate items. Tier 3: free zones (Casablanca Finance City, Tanger Med), oil & gas, mining. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag for expert-comptable.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate.

---

## Step 0: Client Onboarding Questions

1. **Entity name and ICE (Identifiant Commun de l'Entreprise)** [T1] -- 15-digit identifier
2. **IF (Identifiant Fiscal)** [T1] -- tax identification number
3. **VAT registration status** [T1] -- assujetti or exonéré
4. **Filing regime** [T1] -- déclaration mensuelle (monthly, turnover >= MAD 1,000,000) or trimestrielle (quarterly)
5. **Industry/sector** [T2] -- impacts rate and exemption classification
6. **Does the business make exempt supplies?** [T2] -- if yes, prorata required
7. **Does the business import goods?** [T1] -- customs TVA
8. **Crédit de TVA reporté** [T1] -- credit brought forward
9. **Does the business benefit from exonération avec droit à déduction?** [T1] -- critical distinction in Morocco

**If items 1-3 are unknown, STOP.**

---

## Step 1: VAT Rate Structure [T1]

Morocco has been progressively converging from four VAT rates to two rates (20% and 10%) over the period 2024-2026. As of 2026, the 7% and 14% rates have been phased out and only two standard rates remain:

| Rate | Description | Key Supplies | Legislation |
|------|-------------|-------------|-------------|
| 20% | Standard rate (taux normal) | Most goods and services, transport (previously 14%), items previously at 7% that have been moved up | CGI, Art. 98; Loi de Finances 2024-2026 |
| 10% | Reduced rate | Hotel/restaurant/tourism, certain food products, legal/accounting services, banking operations, water, electricity, pharmaceutical products, school supplies (items previously at 7% moved here) | CGI, Art. 99; Loi de Finances 2024-2026 |
| ~~14%~~ | **PHASED OUT** as of 2026 -- items moved to 20% or 10% | -- | Loi de Finances 2024 (transitional) |
| ~~7%~~ | **PHASED OUT** as of 2026 -- items moved to 10% | -- | Loi de Finances 2024 (transitional) |
| Exempt with right to deduct | 0% effective | Exports, international transport, fertilizers, agricultural equipment | CGI, Art. 92 |
| Exempt without right to deduct | Exempt | Financial services, medical, education, bread, flour, basic necessities | CGI, Art. 91 |

### Critical Distinction: Two Types of Exemption [T1]
- **Exonération avec droit à déduction (Art. 92):** Exempt from charging TVA but input TVA IS recoverable. Functions like zero-rating. Includes exports, diplomatic supplies, investment goods for newly registered businesses (36-month window).
- **Exonération sans droit à déduction (Art. 91):** Exempt from charging TVA AND input TVA is NOT recoverable. Includes financial services, medical, education.

**This distinction is critical and unique to Morocco. NEVER confuse the two.**

---

## Step 2: Transaction Classification Rules

### 2a. Transaction Type [T1]
- Sale (TVA facturée/collectée) or Purchase (TVA récupérable)
- Salaries, CNSS, AMO, dividends, loan repayments = OUT OF SCOPE

### 2b. Counterparty Location [T1]
- Domestic (Morocco)
- Maghreb: Algeria, Tunisia, Libya, Mauritania
- EU: trading partner but no special VAT agreement
- Rest of World
- **Note:** Morocco has no common VAT area with any regional bloc.

### 2c. Supply Type [T1]
- Goods / Services / Import of goods (customs) / Import of services (autoliquidation)
- **Legislation:** CGI, Art. 88 (territoriality)

### 2d. Rate Determination [T1]
Rate is determined by the nature of the supply, NOT the status of the supplier or customer. From 2026, only two rates apply:
- Tourism/hotel/restaurant: 10%
- Transport: 20% (previously 14%, phased out)
- Pharmaceutical/water/school supplies: 10% (previously 7%, phased out)
- Most other goods/services: 20%
- Exports: exempt with right to deduct

---

## Step 3: VAT Return Form Structure [T1]

Filed monthly (turnover >= MAD 1,000,000) or quarterly via SIMPL portal.

### Output Section (TVA Facturée)

| Line | Description | Mapping |
|------|-------------|---------|
| 1 | CA taxable à 20% | Standard-rated sales |
| 2 | CA taxable à 10% | Reduced-rated sales |
| 3 | ~~CA taxable à 14%~~ | **PHASED OUT** -- historically intermediate-rated sales (now moved to 20% or 10%) |
| 4 | ~~CA taxable à 7%~~ | **PHASED OUT** -- historically super-reduced-rated sales (now moved to 10%) |
| 5 | CA exonéré avec droit à déduction | Exports and assimilated |
| 6 | CA exonéré sans droit à déduction | Exempt (no recovery) |
| 7 | Total CA | Sum of 1-6 |
| 8 | TVA facturée à 20% | 20% on Line 1 |
| 9 | TVA facturée à 10% | 10% on Line 2 |
| 10 | ~~TVA facturée à 14%~~ | **PHASED OUT** |
| 11 | ~~TVA facturée à 7%~~ | **PHASED OUT** |
| 12 | TVA sur autoliquidation | Reverse charge output |
| 13 | Régularisations | Credit notes, adjustments |
| 14 | Total TVA brute | Sum of 8-13 |

### Input Section (TVA Récupérable)

| Line | Description | Mapping |
|------|-------------|---------|
| 15 | TVA sur achats non immobilisés | VAT on operating purchases |
| 16 | TVA sur achats immobilisés | VAT on capital goods |
| 17 | TVA sur importations | Customs VAT |
| 18 | TVA autoliquidation (input) | Reverse charge input |
| 19 | Exclusions et régularisations | Blocked items |
| 20 | Total TVA récupérable | 15 + 16 + 17 + 18 - 19 |

### Net Calculation

| Line | Description | Formula |
|------|-------------|---------|
| 21 | TVA due | 14 - 20 |
| 22 | Crédit reporté | Prior period |
| 23 | TVA à payer / Crédit à reporter | 21 - 22 |

---

## Step 4: Reverse Charge (Autoliquidation) [T1]

**Legislation:** CGI, Art. 115 (autoliquidation).

When a Morocco VAT-registered person receives services from a non-resident:
1. Self-assess output TVA at the applicable rate (usually 20%) on Line 12
2. Claim input TVA on Line 18 if for taxable supplies
3. Net effect: zero for fully taxable businesses

---

## Step 5: Rule of Offset (Règle du Décalage) [T1]

**Legislation:** CGI, Art. 101 (décalage d'un mois).

**IMPORTANT:** Morocco historically required a one-month delay (décalage) before input TVA could be deducted. This rule has been progressively abolished:
- **Capital goods (immobilisations):** No décalage -- deductible in the month of acquisition/payment
- **Operating purchases (charges):** Décalage abolished for most businesses. Check current Loi de Finances provisions.

**Flag for reviewer [T2]:** Confirm whether the décalage still applies to the specific business or transaction type. Recent Loi de Finances amendments have phased this out for most taxpayers.

---

## Step 6: Deductibility Check

### Blocked Input Tax [T1]
**Legislation:** CGI, Art. 106 (exclusions du droit à déduction).
- Vehicles for personal transport (< 9 seats), unless taxi/hire/leasing company (Art. 106-I-1)
- Petroleum products for blocked vehicles (Art. 106-I-2)
- Purchases of a personal nature (Art. 106-I-3)
- Representation and hospitality exceeding a normal level (Art. 106-I-4)
- Gifts exceeding MAD 100 per item per recipient (Art. 106-I-5)
- Purchases from non-registered suppliers (no valid invoice with IF/ICE)

### Partial Exemption (Prorata) [T2]
**Legislation:** CGI, Art. 104 (prorata de déduction).
`Prorata = (Taxable Turnover + Exempt-with-Deduction Turnover) / Total Turnover * 100`
Rounded up to next percentage point.
**Flag for reviewer: annual recalculation and annual regularization required.**

---

## Step 7: Key Thresholds [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory registration | MAD 500,000 annual turnover (goods) or MAD 200,000 (services) | CGI, Art. 89 |
| Monthly filing threshold | MAD 1,000,000 annual turnover | CGI, Art. 108 |
| Quarterly filing | Below MAD 1,000,000 or new businesses | CGI, Art. 108 |
| Gift deduction limit | MAD 100 per item per recipient | CGI, Art. 106 |
| Investment goods exemption window | 36 months from first acquisition | CGI, Art. 92-I-6 |

---

## Step 8: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|-----------|--------|----------|-------------|
| TVA return (monthly) | Monthly | Before 20th of following month | CGI, Art. 110 |
| TVA return (quarterly) | Quarterly | Before 20th of month following quarter | CGI, Art. 110 |
| Payment | Same as return | Same deadline | CGI, Art. 110 |

### Penalties [T1]
- Late filing: 15% surcharge + 0.5% interest per month (first month); 0.5% per month thereafter
- Late payment: 10% surcharge + 5% for first month + 0.5% per additional month
- Failure to register: 100% of tax due

---

## PROHIBITIONS [T1]

- NEVER confuse "exempt with right to deduct" (Art. 92) with "exempt without right to deduct" (Art. 91) -- this is the most critical distinction in Morocco VAT
- NEVER let AI guess return line assignment or rate selection
- NEVER allow recovery on blocked categories
- NEVER apply wrong rate -- from 2026, only two rates (20% and 10%) exist; 7% and 14% have been phased out
- NEVER apply reverse charge to out-of-scope categories
- NEVER compute numbers -- engine handles arithmetic
- NEVER file without checking crédit reporté
- NEVER accept invoices without valid IF/ICE for input purposes
- NEVER ignore the décalage rule without confirming it has been abolished for the specific case

---

## Step 9: Edge Case Registry

### EC1 -- Import of services (cloud software) [T1]
**Situation:** Moroccan company uses Google Workspace. Monthly USD 50.
**Resolution:** Autoliquidation at 20%. Self-assess output (Line 12) and input (Line 18). Net zero.
**Legislation:** CGI, Art. 115.

### EC2 -- Hotel/restaurant supply (10%) [T1]
**Situation:** Hotel charges room rate of MAD 1,500/night.
**Resolution:** TVA at 10%. Line 3 for turnover. Line 10 for output TVA.
**Legislation:** CGI, Art. 99.

### EC3 -- Pharmaceutical product sale (10%, previously 7%) [T1]
**Situation:** Pharmacy sells medicines for MAD 200,000.
**Resolution:** TVA at 10% (previously 7%, rate phased out by 2026). Line 2 for turnover. Line 9 for output TVA.
**Legislation:** CGI, Art. 99; Loi de Finances 2024-2026.

### EC4 -- Transport service (20%, previously 14%) [T1]
**Situation:** Transport company provides freight services for MAD 500,000.
**Resolution:** TVA at 20% (previously 14%, rate phased out by 2026). Line 1 for turnover. Line 8 for output TVA.
**Legislation:** CGI, Art. 99; Loi de Finances 2024-2026.

### EC5 -- Export (exempt with right to deduct) [T1]
**Situation:** Manufacturer exports textiles worth MAD 10,000,000.
**Resolution:** Line 5 (exempt with deduction). No output TVA. Input TVA fully recoverable.
**Legislation:** CGI, Art. 92.

### EC6 -- New business investment goods (36-month window) [T2]
**Situation:** Newly VAT-registered company purchases equipment within first 36 months.
**Resolution:** May benefit from exemption with right to deduct under Art. 92-I-6. Flag for reviewer: confirm eligibility, that goods are genuine investment goods, and that the 36-month window has not expired.
**Legislation:** CGI, Art. 92-I-6.

### EC7 -- Mixed supplies (partially exempt) [T2]
**Situation:** Bank provides both exempt financial services and taxable advisory services at 10%.
**Resolution:** Prorata applies to common costs. Direct costs allocated. Flag for reviewer.
**Legislation:** CGI, Art. 104.

### EC8 -- Casablanca Finance City (CFC) [T3]
**Situation:** Company holds CFC status.
**Resolution:** Escalate. CFC companies benefit from specific tax regime including potential VAT exemptions. Specific status must be verified.
**Legislation:** CFC Law; specific company decree.

---

## Step 10: Reviewer Escalation Protocol

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list treatments]
Recommended: [which and why]
Action Required: Expert-comptable must confirm before filing.
```

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [outside scope]
Action Required: Do not classify. Refer to expert-comptable.
```

---

## Step 11: Test Suite

### Test 1 -- Standard sale at 20% [T1]
**Input:** Company sells goods for MAD 100,000 net. Standard-rated.
**Expected output:** Line 1 = MAD 100,000. Line 8 = MAD 20,000 (20%).

### Test 2 -- Hotel sale at 10% [T1]
**Input:** Hotel earns room revenue MAD 500,000.
**Expected output:** Line 3 = MAD 500,000. Line 10 = MAD 50,000 (10%).

### Test 3 -- Pharmaceutical sale at 10% (previously 7%) [T1]
**Input:** Pharmacy sells medicines MAD 200,000.
**Expected output:** Line 2 = MAD 200,000. Line 9 = MAD 20,000 (10%).

### Test 4 -- Transport at 20% (previously 14%) [T1]
**Input:** Freight company invoices MAD 300,000 for transport.
**Expected output:** Line 1 = MAD 300,000. Line 8 = MAD 60,000 (20%).

### Test 5 -- Export (exempt with deduction) [T1]
**Input:** Exporter ships goods MAD 5,000,000.
**Expected output:** Line 5 = MAD 5,000,000. TVA = 0. Input TVA recoverable.

### Test 6 -- Reverse charge [T1]
**Input:** Company receives IT services from US firm. MAD 200,000.
**Expected output:** Line 12 = MAD 40,000 (20% output). Line 18 = MAD 40,000 (input). Net zero.

### Test 7 -- Blocked (motor vehicle) [T1]
**Input:** Company buys car. MAD 300,000 + MAD 60,000 TVA.
**Expected output:** Input TVA = 0 (BLOCKED). Cost = MAD 360,000.

### Test 8 -- Exempt without deduction (financial) [T1]
**Input:** Bank earns interest income MAD 10,000,000.
**Expected output:** Line 6 = MAD 10,000,000. No output TVA. Related input TVA NOT recoverable.

---

## Step 12: Out of Scope -- Direct Tax [T3]

- **Corporate Income Tax (IS):** Progressive rates: 10%/20%/31%. Export IS: reduced rate for 5 years.
- **PAYE (IR/Salaire):** Progressive rates 0%-38%. Employer obligation.
- **CNSS/AMO:** Social security and health insurance. Employer + employee contributions. Separate from TVA.

---

## Contribution Notes

Morocco-specific elements include the two-rate structure (20%/10%, converged from four rates by 2026 Loi de Finances reform), the critical distinction between two types of exemption (avec/sans droit à déduction), the décalage rule, the 36-month investment window, and CFC regime. Updated April 2026 to reflect completion of the 2024-2026 rate convergence eliminating 7% and 14% rates.

**A skill may not be published without sign-off from a licensed expert-comptable in Morocco.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
