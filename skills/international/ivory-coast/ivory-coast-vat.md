---
name: ivory-coast-vat
description: Use this skill whenever asked to prepare, review, or create an Ivory Coast (Côte d'Ivoire) VAT (TVA) return for any client. Trigger on phrases like "prepare VAT return", "TVA Côte d'Ivoire", "DGI return", "declaration TVA", or any request involving Ivory Coast VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Côte d'Ivoire VAT classification rules, return form mappings, deductibility rules, reverse charge treatment, registration thresholds, and filing deadlines. ALWAYS read this skill before touching any Ivory Coast VAT-related work.
---

# Côte d'Ivoire VAT (TVA) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Côte d'Ivoire (Republic of Côte d'Ivoire / Ivory Coast) |
| Jurisdiction Code | CI |
| Primary Legislation | Code Général des Impôts (CGI), Livre II -- Taxe sur la Valeur Ajoutée |
| Supporting Legislation | WAEMU (UEMOA) Directive 02/98/CM on VAT harmonization; Livre des Procédures Fiscales |
| Tax Authority | Direction Générale des Impôts (DGI) |
| Filing Portal | https://e-impots.gouv.ci |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by a licensed expert-comptable in Côte d'Ivoire |
| Validation Date | Pending |
| Last Verified | 2026-04-10 (web-verified against PWC, DGI, Trading Economics) |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: rate application, return mapping, registration, deadlines, blocked categories. Tier 2: partial exemption, mixed supplies, WAEMU provisions, capital goods adjustment. Tier 3: petroleum sector, mining conventions, customs valuation, investment code benefits. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag for expert-comptable.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate.

---

## Step 0: Client Onboarding Questions

1. **Entity name and NCC (Numéro de Compte Contribuable)** [T1]
2. **VAT registration status** [T1] -- assujetti or non-assujetti
3. **Filing regime** [T1] -- régime réel normal (monthly), régime réel simplifié (quarterly), or régime des micro-entreprises
4. **Industry/sector** [T2] -- impacts classification
5. **Does the business make exempt supplies?** [T2] -- if yes, prorata required
6. **Does the business import goods?** [T1] -- customs TVA at port of Abidjan/San Pedro
7. **Crédit de TVA reporté** [T1] -- credit brought forward

**If items 1-2 are unknown, STOP.**

---

## Step 1: VAT Rate Structure [T1]

| Rate | Description | Legislation |
|------|-------------|-------------|
| 18% | Standard rate (taux normal) | CGI, Art. 340 |
| 9% | Reduced rate (certain goods: milk, pasta) | CGI, Art. 341 |
| 0% | Export and assimilated | CGI, Art. 355 |
| Exempt | Exonérations | CGI, Art. 348-354 |

### Zero-Rated Supplies [T1]
**Legislation:** CGI, Art. 355.
- Export of goods (with customs documentation)
- International transport services
- Supplies to diplomats and international organizations (with DGI authorization)
- Services directly linked to export operations

### Exempt Supplies [T1]
**Legislation:** CGI, Art. 348-354.
- Basic foodstuffs (rice, maize, millet, yams, cassava, plantain, bread)
- Financial services (interest on loans, life insurance premiums, foreign exchange)
- Medical and pharmaceutical services
- Educational services (authorized institutions)
- Residential rental (unfurnished)
- Solar energy production equipment (exempt since 2024 Annexe Fiscale, Art. 18 -- previously 9% reduced rate)
- Agricultural inputs (fertilizers, seeds, pesticides)
- Water and electricity (domestic use below thresholds)
- Newspapers and periodicals
- Public passenger transport

---

## Step 2: Transaction Classification Rules

### 2a. Transaction Type [T1]
- Sale (TVA collectée) or Purchase (TVA déductible)
- Salaries, charges patronales, dividends, loan repayments = OUT OF SCOPE

### 2b. Counterparty Location [T1]
- Domestic (Côte d'Ivoire)
- WAEMU (UEMOA): Benin, Burkina Faso, Guinea-Bissau, Mali, Niger, Senegal, Togo
- Rest of World
- **Note:** WAEMU has harmonized VAT principles but no common VAT area.

### 2c. Supply Type [T1]
- Goods / Services / Import of goods (customs) / Import of services (autoliquidation)
- **Legislation:** CGI, Art. 336 (champ d'application)

---

## Step 3: VAT Return Form Structure [T1]

### Output Section (TVA Collectée)

| Line | Description | Mapping |
|------|-------------|---------|
| 1 | CA taxable au taux normal (18%) | Standard-rated sales |
| 2 | CA taxable au taux réduit (9%) | Reduced-rate sales |
| 3 | Opérations exonérées | Exempt supplies |
| 4 | Exportations (0%) | Zero-rated supplies |
| 5 | Total CA | 1 + 2 + 3 + 4 |
| 6 | TVA collectée (18% on Line 1) | Output VAT at 18% |
| 7 | TVA collectée (9% on Line 2) | Output VAT at 9% |
| 8 | TVA sur prestations de services étrangers (autoliquidation) | Reverse charge output |
| 9 | Régularisations | Credit notes, adjustments |
| 10 | Total TVA brute | 6 + 7 + 8 + 9 |

### Input Section (TVA Déductible)

| Line | Description | Mapping |
|------|-------------|---------|
| 11 | TVA sur achats locaux de biens | VAT on local goods purchases |
| 12 | TVA sur prestations de services locaux | VAT on local services |
| 13 | TVA sur importations | VAT from customs documents |
| 14 | TVA sur immobilisations | VAT on capital goods |
| 15 | TVA sur autoliquidation (services étrangers) | Reverse charge input |
| 16 | Régularisations (exclusions) | Blocked items, adjustments |
| 17 | Total TVA déductible | 11 + 12 + 13 + 14 + 15 - 16 |

### Net Calculation

| Line | Description | Formula |
|------|-------------|---------|
| 18 | TVA nette | 10 - 17 |
| 19 | Crédit reporté | Prior period credit |
| 20 | Précompte TVA | Withholding if applicable |
| 21 | TVA à payer / Crédit à reporter | 18 - 19 - 20 |

---

## Step 4: Reverse Charge (Autoliquidation) [T1]

**Legislation:** CGI, Art. 344 (autoliquidation).

When a Côte d'Ivoire VAT-registered person receives services from a non-resident:
1. Self-assess output TVA at 18% (Line 8)
2. Claim input TVA at 18% (Line 15) if for taxable supplies
3. Net effect: zero for fully taxable businesses

**Exceptions:** Out-of-scope payments; services consumed entirely outside Côte d'Ivoire.

---

## Step 5: Deductibility Check

### Blocked Input Tax [T1]
**Legislation:** CGI, Art. 360-363 (exclusions du droit à déduction).
- Vehicles for personal transport (< 9 seats), unless taxi/hire (Art. 361)
- Accommodation for personnel (Art. 361)
- Entertainment, reception, and gifts exceeding FCFA 500,000/year per recipient (Art. 361)
- Petroleum products for blocked vehicles (Art. 361)
- Personal use goods and services (Art. 362)
- Purchases not evidenced by proper invoices (Art. 363)

### Partial Exemption (Prorata) [T2]
**Legislation:** CGI, Art. 359.
`Prorata = (Taxable + Zero-Rated Turnover) / Total Turnover * 100`
Rounded up to next whole percentage. Applied to common costs.
**Flag for reviewer: annual recalculation required. DGI may challenge method.**

---

## Step 6: Key Thresholds [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory VAT registration (régime réel normal) | FCFA 500,000,000 annual turnover | CGI |
| Régime réel simplifié | FCFA 200,000,000 - 500,000,000 | CGI |
| Régime des micro-entreprises | Below FCFA 200,000,000 | CGI |
| Capital goods adjustment period (immovable) | 10 years | CGI, Art. 364 |
| Capital goods adjustment period (movable) | 5 years | CGI, Art. 364 |

---

## Step 7: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|-----------|--------|----------|-------------|
| TVA return (régime réel normal) | Monthly | 10th of following month (large enterprises), 15th (others) | CGI |
| TVA return (simplifié) | Quarterly | 15th of month following quarter | CGI |
| Payment | Same as return | Same deadline | CGI |

### Penalties [T1]
- Late filing: 25% surcharge on tax due (minimum FCFA 100,000)
- Late payment: interest at 1% per month
- Failure to register: 100% of tax due

---

## PROHIBITIONS [T1]

- NEVER let AI guess return line assignment
- NEVER allow recovery on blocked categories
- NEVER confuse zero-rated (0%) with exempt
- NEVER apply reverse charge to out-of-scope categories
- NEVER allow unregistered persons to claim input TVA
- NEVER treat WAEMU transactions as intra-community
- NEVER compute numbers -- engine handles arithmetic
- NEVER file without checking crédit reporté
- NEVER accept invoices without valid NCC for input VAT

---

## Step 8: Edge Case Registry

### EC1 -- Import of services (US SaaS) [T1]
**Situation:** Company subscribes to Salesforce. Monthly USD 200. No VAT.
**Resolution:** Autoliquidation. Self-assess 18% output and input. Net zero if fully taxable.
**Legislation:** CGI, Art. 344.

### EC2 -- Export of cocoa (zero-rated) [T1]
**Situation:** Exporter ships cocoa beans to Netherlands.
**Resolution:** Zero-rated. Line 4. No output TVA. Input TVA fully recoverable.
**Legislation:** CGI, Art. 355.

### EC3 -- Motor vehicle (blocked) [T1]
**Situation:** Company purchases sedan for director.
**Resolution:** Input TVA BLOCKED. < 9 seats personal transport. Cost includes irrecoverable VAT.
**Legislation:** CGI, Art. 361.

### EC4 -- Reduced rate supply (milk) [T1]
**Situation:** Manufacturer sells processed milk at 9%.
**Resolution:** Line 2. TVA at 9%. Line 7 = 9% of Line 2. Input TVA on production costs recoverable at full 18%.
**Legislation:** CGI, Art. 341.

### EC5 -- WAEMU import (from Senegal) [T1]
**Situation:** Company imports goods from Senegal.
**Resolution:** VAT at 18% charged at Ivorian customs. No intra-community mechanism. Customs TVA recoverable.
**Legislation:** CGI; UEMOA Directive 02/98.

### EC6 -- Mixed supply (taxable + exempt) [T2]
**Situation:** Company provides both taxable IT services and exempt financial advisory.
**Resolution:** Prorata applies. Flag for reviewer.
**Legislation:** CGI, Art. 359.

### EC7 -- Capital goods sale within adjustment period [T2]
**Situation:** Company sells office building purchased 4 years ago. Original TVA recovered.
**Resolution:** Capital goods adjustment. 6/10 of input TVA must be repaid to DGI. Flag for reviewer.
**Legislation:** CGI, Art. 364.

### EC8 -- Investment Code benefit [T3]
**Situation:** Company under Code des Investissements receives TVA exemption on imported equipment.
**Resolution:** Escalate. Investment Code benefits are negotiated individually. Specific decree must be verified.
**Legislation:** Code des Investissements 2012; specific company decree.

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

### Test 1 -- Standard local sale (18%) [T1]
**Input:** Company sells goods for FCFA 20,000,000 net. Standard-rated.
**Expected output:** Line 1 = FCFA 20,000,000. Line 6 = FCFA 3,600,000 (18%).

### Test 2 -- Reduced rate sale (9%) [T1]
**Input:** Company sells processed milk for FCFA 5,000,000 net.
**Expected output:** Line 2 = FCFA 5,000,000. Line 7 = FCFA 450,000 (9%).

### Test 3 -- Local purchase, input recovery [T1]
**Input:** Company buys raw materials. Invoice: FCFA 10,000,000 + FCFA 1,800,000 TVA.
**Expected output:** Line 11 = FCFA 1,800,000. Recoverable.

### Test 4 -- Reverse charge [T1]
**Input:** Company receives IT services from French firm. FCFA 15,000,000. No VAT.
**Expected output:** Line 8 = FCFA 2,700,000 (output). Line 15 = FCFA 2,700,000 (input). Net zero.

### Test 5 -- Export (zero-rated) [T1]
**Input:** Exporter ships rubber worth FCFA 100,000,000.
**Expected output:** Line 4 = FCFA 100,000,000. TVA = 0. Input TVA recoverable.

### Test 6 -- Blocked (motor vehicle) [T1]
**Input:** Company buys car. Invoice: FCFA 15,000,000 + FCFA 2,700,000 TVA.
**Expected output:** Input TVA = 0 (BLOCKED). Cost = FCFA 17,700,000.

### Test 7 -- Exempt supply [T1]
**Input:** Bank earns interest FCFA 200,000,000.
**Expected output:** Line 3 = FCFA 200,000,000. No output TVA. Related input TVA NOT recoverable.

### Test 8 -- Import from WAEMU [T1]
**Input:** Company imports goods from Burkina Faso. Customs value FCFA 30,000,000.
**Expected output:** Line 13 = FCFA 5,400,000 (18% customs TVA). Recoverable if taxable.

---

## Step 11: Out of Scope -- Direct Tax [T3]

- **Corporate Income Tax (BIC):** 25%. Reduced rates under investment code.
- **PAYE (ITS):** Progressive rates. Employer obligation.
- **Social charges (CNPS):** Employer contributions. Separate from TVA.

---

## Contribution Notes

Côte d'Ivoire-specific elements include the 9% reduced rate, WAEMU harmonization, capital goods adjustment periods, and investment code interactions.

**A skill may not be published without sign-off from a licensed expert-comptable in Côte d'Ivoire.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
