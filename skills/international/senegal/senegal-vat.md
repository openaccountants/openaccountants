---
name: senegal-vat
description: Use this skill whenever asked to prepare, review, or create a Senegal VAT (TVA) return for any client. Trigger on phrases like "prepare VAT return", "TVA Senegal", "DGID return", "declaration TVA", or any request involving Senegal VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Senegal VAT classification rules, return form mappings, deductibility rules, reverse charge treatment, registration thresholds, and filing deadlines. ALWAYS read this skill before touching any Senegal VAT-related work.
---

# Senegal VAT (TVA) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Senegal (Republic of Senegal) |
| Jurisdiction Code | SN |
| Primary Legislation | Code Général des Impôts (CGI), Livre II -- Taxe sur la Valeur Ajoutée |
| Supporting Legislation | WAEMU (UEMOA) Directive 02/98/CM on VAT harmonization; Livre des Procédures Fiscales (LPF) |
| Tax Authority | Direction Générale des Impôts et des Domaines (DGID) |
| Filing Portal | https://eservices.dgid.sn |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by a licensed expert-comptable in Senegal |
| Validation Date | Pending |
| Last Verified | 2026-04-10 (web-verified against PWC, DGID, Trading Economics, Lovat Compliance) |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: rate application, return mapping, registration, deadlines, blocked categories. Tier 2: partial exemption, mixed supplies, WAEMU provisions. Tier 3: oil & gas sector, mining conventions, customs valuation. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag for expert-comptable confirmation.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate.

---

## Step 0: Client Onboarding Questions

1. **Entity name and NINEA** [T1] -- Numéro d'Identification Nationale des Entreprises et Associations
2. **VAT registration status** [T1] -- assujetti (liable) or non-assujetti
3. **Filing regime** [T1] -- régime réel normal (monthly) or régime du réel simplifié (quarterly)
4. **Industry/sector** [T2] -- impacts classification
5. **Does the business make exempt supplies?** [T2] -- if yes, prorata required
6. **Does the business import goods?** [T1] -- customs TVA at port
7. **Credit de TVA reporté** [T1] -- credit brought forward

**If items 1-2 are unknown, STOP.**

---

## Step 1: VAT Rate Structure [T1]

| Rate | Description | Legislation |
|------|-------------|-------------|
| 18% | Standard rate (taux normal) | CGI, Art. 361 |
| 10% | Reduced rate (accommodation and catering by approved tourist establishments) | CGI, Art. 361 |
| 0% | Export and assimilated | CGI, Art. 372 |
| Exempt | Exonérations | CGI, Art. 366-371 |

**Note:** WAEMU harmonization directive requires standard rate between 15%-20%. Senegal applies 18%. The 10% reduced rate applies exclusively to accommodation and catering services provided by tourist establishments approved by ministerial decree.

### Zero-Rated Supplies [T1]
**Legislation:** CGI, Art. 372.
- Export of goods (with customs export documentation)
- International maritime and air transport services
- Supplies to diplomats and international organizations
- Services directly linked to export of goods

### Exempt Supplies [T1]
**Legislation:** CGI, Art. 366-371.
- Basic foodstuffs (rice, millet, sorghum, maize, bread, milk, sugar as specified)
- Financial services (interest, foreign exchange, life insurance premiums)
- Medical and pharmaceutical services (by authorized practitioners)
- Educational services (by authorized institutions)
- Residential rental (unfurnished)
- Agricultural equipment and inputs (as specified)
- Water and electricity (domestic use below specified thresholds)
- Newspaper and book publishing
- Petroleum products (subject to specific taxes)

---

## Step 2: Transaction Classification Rules

### 2a. Transaction Type [T1]
- Sale (TVA collectée / output VAT) or Purchase (TVA déductible / input VAT)
- Salaries, charges sociales, dividends, loan repayments = OUT OF SCOPE

### 2b. Counterparty Location [T1]
- Domestic (Senegal)
- WAEMU (UEMOA): Benin, Burkina Faso, Côte d'Ivoire, Guinea-Bissau, Mali, Niger, Togo
- ECOWAS (but not WAEMU): Cabo Verde, Gambia, Ghana, Guinea, Liberia, Nigeria, Sierra Leone
- Rest of World
- **Note:** WAEMU has harmonized VAT rules but NO common VAT area like the EU. Each country charges its own VAT.

### 2c. Supply Type [T1]
- Goods / Services / Imports of goods (customs) / Imports of services (reverse charge)
- **Legislation:** CGI, Art. 355 (fait générateur); Art. 358 (lieu de taxation)

---

## Step 3: VAT Return Form Structure [T1]

The Senegal TVA return (Déclaration de TVA) is filed monthly or quarterly.

### Output Section (TVA Collectée)

| Line | Description | Mapping |
|------|-------------|---------|
| I.1 | Chiffre d'affaires taxable (18%) | Net value of standard-rated sales |
| I.2 | Opérations exonérées | Net value of exempt supplies |
| I.3 | Exportations | Net value of exports (0%) |
| I.4 | Total chiffre d'affaires | I.1 + I.2 + I.3 |
| I.5 | TVA collectée (18% on I.1) | Output VAT |
| I.6 | TVA sur acquisitions de services (reverse charge) | Self-assessed on imported services |
| I.7 | Régularisations de TVA collectée | Credit notes, adjustments |
| I.8 | Total TVA brute | I.5 + I.6 + I.7 |

### Input Section (TVA Déductible)

| Line | Description | Mapping |
|------|-------------|---------|
| II.1 | TVA sur achats locaux | VAT on local purchases |
| II.2 | TVA sur importations | VAT from customs |
| II.3 | TVA sur acquisitions de services (reverse charge) | Self-assessed input VAT |
| II.4 | TVA sur immobilisations | VAT on capital goods |
| II.5 | Régularisations | Blocked items, adjustments |
| II.6 | Total TVA déductible | II.1 + II.2 + II.3 + II.4 - II.5 |

### Net Calculation

| Line | Description | Formula |
|------|-------------|---------|
| III.1 | TVA nette | I.8 - II.6 |
| III.2 | Crédit reporté (brought forward) | From prior period |
| III.3 | Précompte de TVA (withholding) | If applicable |
| III.4 | TVA à payer / Crédit à reporter | III.1 - III.2 - III.3 |

---

## Step 4: Reverse Charge (Autoliquidation) [T1]

**Legislation:** CGI, Art. 364 (autoliquidation).

When a Senegalese VAT-registered person receives services from a non-resident:
1. Self-assess output TVA at 18% (Line I.6)
2. Claim input TVA at 18% if for taxable supplies (Line II.3)
3. Net effect: zero for fully taxable businesses

**Exceptions:** Out-of-scope payments; services consumed outside Senegal.

---

## Step 5: Deductibility Check

### Blocked Input Tax [T1]
**Legislation:** CGI, Art. 376-379 (exclusions du droit à déduction).
- Vehicles for personal transport (< 9 seats), unless taxi/hire (Art. 377)
- Accommodation and lodging for staff and directors (Art. 377)
- Entertainment, reception, and hospitality expenses (Art. 377)
- Petroleum products for vehicles where VAT is blocked (Art. 377)
- Personal use goods and services (Art. 377)
- Purchases not supported by valid invoices (Art. 378)

### Partial Exemption (Prorata) [T2]
**Legislation:** CGI, Art. 375.
`Prorata = (Taxable Turnover + Zero-Rated Turnover) / Total Turnover * 100`
Rounded up to the next whole number. Applied to common costs.
**Flag for reviewer: prorata must be recalculated annually. DGID may challenge.**

---

## Step 6: Key Thresholds [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory VAT registration | FCFA 100,000,000 annual turnover (goods) or FCFA 50,000,000 (services) | CGI, Art. 363 |
| Régime réel simplifié | Below normal threshold but above FCFA 50M (goods) / FCFA 25M (services) | CGI |
| Capital goods scheme | Apply over adjustment period for immovable property (20 years) and movable (5 years) | CGI, Art. 382 |

---

## Step 7: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|-----------|--------|----------|-------------|
| TVA return (régime réel normal) | Monthly | 15th of following month | CGI, Art. 383 |
| TVA return (régime réel simplifié) | Quarterly | 15th of month following quarter | CGI, Art. 383 |
| Payment | Same as return | Same deadline | CGI, Art. 383 |

### Penalties [T1]
- Late filing: 50% of tax due (minimum FCFA 200,000)
- Late payment: interest at 1% per month
- Failure to register: 100% of tax due plus penalties

---

## PROHIBITIONS [T1]

- NEVER let AI guess return line assignment
- NEVER allow recovery on blocked categories
- NEVER confuse zero-rated with exempt
- NEVER apply reverse charge to out-of-scope categories
- NEVER allow unregistered persons to claim input TVA
- NEVER treat WAEMU transactions as intra-community (no EU-style mechanism)
- NEVER compute numbers -- engine handles arithmetic
- NEVER file without checking crédit reporté
- NEVER accept invoices without valid NINEA for input VAT purposes

---

## Step 8: Edge Case Registry

### EC1 -- Import of services (SaaS from US) [T1]
**Situation:** Senegalese company uses Microsoft 365. Monthly USD 100. No VAT.
**Resolution:** Autoliquidation. Self-assess output and input TVA at 18%. Net zero if fully taxable.
**Legislation:** CGI, Art. 364.

### EC2 -- Export of groundnuts (zero-rated) [T1]
**Situation:** Senegalese exporter ships groundnuts to China.
**Resolution:** Zero-rated. Line I.3. No output TVA. Input TVA fully recoverable with export docs.
**Legislation:** CGI, Art. 372.

### EC3 -- Motor vehicle (blocked) [T1]
**Situation:** Company purchases sedan for director.
**Resolution:** Input TVA BLOCKED. Cost includes irrecoverable VAT.
**Legislation:** CGI, Art. 377.

### EC4 -- WAEMU supplier [T1]
**Situation:** Senegalese company imports goods from Côte d'Ivoire.
**Resolution:** VAT at 18% charged at Senegalese customs. No intra-community mechanism. Customs TVA recoverable if for taxable supplies.
**Legislation:** CGI; UEMOA Directive 02/98.

### EC5 -- Mixed supply (taxable + exempt) [T2]
**Situation:** Company provides both financial advisory (exempt) and IT consulting (taxable).
**Resolution:** Prorata applies to common costs. Direct costs allocated. Flag for reviewer.
**Legislation:** CGI, Art. 375.

### EC6 -- Précompte de TVA (VAT withholding) [T1]
**Situation:** Government entity pays VAT-registered supplier and applies précompte.
**Resolution:** The précompte is a VAT withholding mechanism. Supplier claims credit on Line III.3. Agent remits to DGID.
**Legislation:** CGI, Art. 385.

### EC7 -- Capital goods adjustment [T2]
**Situation:** Company sells a building purchased 3 years ago. Original VAT was recovered.
**Resolution:** Capital goods adjustment applies. For immovable property, 20-year adjustment period. 17/20 of the original input VAT must be repaid. Flag for reviewer: confirm calculation and any change of use adjustments.
**Legislation:** CGI, Art. 382.

### EC8 -- Bad debt relief [T2]
**Situation:** Client has not paid for 2 years. Output TVA was accounted for.
**Resolution:** Bad debt relief is available under specific conditions. The supplier must prove the debt is irrecoverable (court order or formal write-off). Flag for reviewer: documentation requirements are strict.
**Legislation:** CGI, Art. 380.

---

## Step 9: Reviewer Escalation Protocol

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

## Step 10: Test Suite

### Test 1 -- Standard local sale [T1]
**Input:** Company sells services for FCFA 10,000,000 net. Standard-rated.
**Expected output:** I.1 = FCFA 10,000,000. I.5 = FCFA 1,800,000 (18%).

### Test 2 -- Local purchase, input recovery [T1]
**Input:** Company buys equipment. Invoice: FCFA 5,000,000 + FCFA 900,000 TVA = FCFA 5,900,000.
**Expected output:** II.1 = FCFA 900,000. Recoverable.

### Test 3 -- Reverse charge [T1]
**Input:** Company receives consulting from French firm. FCFA 8,000,000. No VAT.
**Expected output:** I.6 = FCFA 1,440,000 (output). II.3 = FCFA 1,440,000 (input). Net zero.

### Test 4 -- Export (zero-rated) [T1]
**Input:** Exporter ships fish worth FCFA 50,000,000.
**Expected output:** I.3 = FCFA 50,000,000. Output TVA = 0. Input TVA recoverable.

### Test 5 -- Blocked (entertainment) [T1]
**Input:** Company hosts reception. Invoice: FCFA 3,000,000 + FCFA 540,000 TVA.
**Expected output:** Input TVA = 0 (BLOCKED). Cost = FCFA 3,540,000.

### Test 6 -- Exempt supply (financial) [T1]
**Input:** Bank earns interest income FCFA 100,000,000.
**Expected output:** I.2 = FCFA 100,000,000. No output TVA. Related input TVA NOT recoverable.

---

## Step 11: Out of Scope -- Direct Tax [T3]

- **Corporate Income Tax (IS):** 30%. Reduced rates for SMEs.
- **PAYE (IRPP/BRS):** Progressive rates. Employer obligation.
- **Social charges:** IPRES, CSS. Separate from TVA.

---

## Contribution Notes

Senegal-specific elements include the WAEMU harmonization framework, précompte de TVA, capital goods adjustment periods, and the régime réel simplifié.

**A skill may not be published without sign-off from a licensed expert-comptable in Senegal.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
