---
name: cameroon-vat
description: Use this skill whenever asked to prepare, review, or create a Cameroon VAT (TVA) return for any client. Trigger on phrases like "prepare VAT return", "TVA Cameroun", "DGI return", "declaration TVA", or any request involving Cameroon VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Cameroon VAT classification rules including the municipal surcharge (CAC), return form mappings, deductibility rules, reverse charge treatment, registration thresholds, and filing deadlines. ALWAYS read this skill before touching any Cameroon VAT-related work.
---

# Cameroon VAT (TVA) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Cameroon (Republic of Cameroon) |
| Jurisdiction Code | CM |
| Primary Legislation | Code Général des Impôts (CGI), Titre III -- Taxe sur la Valeur Ajoutée |
| Supporting Legislation | Loi de Finances annuelle; CEMAC Directive on VAT harmonization |
| Tax Authority | Direction Générale des Impôts (DGI) |
| Filing Portal | https://fiscalis.minfi.cm |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by a licensed expert-comptable in Cameroon |
| Validation Date | Pending |
| Last Research Update | April 2026 |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: rate application (including CAC), return mapping, registration, deadlines, blocked categories. Tier 2: partial exemption, mixed supplies, CEMAC provisions. Tier 3: oil & gas, mining conventions, free zone regimes. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag for expert-comptable.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate.

---

## Step 0: Client Onboarding Questions

1. **Entity name and NIU (Numéro Identifiant Unique)** [T1]
2. **VAT registration status** [T1] -- assujetti or non-assujetti
3. **Filing regime** [T1] -- régime réel (monthly), régime simplifié (quarterly), or régime de base
4. **Industry/sector** [T2] -- impacts classification
5. **Does the business make exempt supplies?** [T2] -- if yes, prorata required
6. **Does the business import goods?** [T1] -- customs TVA at port of Douala/Kribi
7. **Crédit de TVA reporté** [T1] -- credit brought forward

**If items 1-2 are unknown, STOP.**

---

## Step 1: VAT Rate Structure [T1]

### Effective Rate Composition

| Component | Rate | Legislation |
|-----------|------|-------------|
| TVA (standard) | 17.5% | CGI, Art. 127 |
| CAC (Centimes Additionnels Communaux) | 10% of TVA amount (i.e., 1.75% of taxable base) | CGI, Art. 152 |
| **Effective total rate** | **19.25%** | -- |

**Critical rule:** The CAC is a 10% surcharge calculated on the TVA amount, NOT on the taxable base. It is collected together with TVA and remitted to municipalities. Both TVA and CAC are shown on invoices.

### Calculation Example [T1]
- Taxable base: FCFA 1,000,000
- TVA: 17.5% x 1,000,000 = FCFA 175,000
- CAC: 10% x 175,000 = FCFA 17,500
- Total tax: FCFA 192,500 (effective 19.25%)
- Total invoice: FCFA 1,192,500

### Reduced Rate (2026 Finance Law) [T1]

| Component | Rate | Legislation |
|-----------|------|-------------|
| TVA (reduced -- social housing) | 10% | 2026 Finance Law |

**Note:** Under the 2026 Finance Law, operations related to social housing (sale and rental of social housing units, interest on mortgage loans) are subject to a reduced TVA rate of 10%, replacing the previous exemption. [T2 -- Flag for practitioner: confirm specific transactions qualifying as social housing under the decree.]

### Zero-Rated Supplies [T1]
**Legislation:** CGI, Art. 128.
- Export of goods (with customs documentation)
- International transport services
- Supplies to diplomats (with authorization)

### Exempt Supplies [T1]
**Legislation:** CGI, Art. 128-131.
- Basic foodstuffs (as specified by decree: rice, flour, bread, fresh fish, meat, vegetables)
- Financial services (interest on loans, life insurance premiums)
- Medical services and pharmaceutical products (authorized)
- Educational services (authorized institutions)
- Residential rental (unfurnished)
- Agricultural inputs and equipment (as specified)
- Newspapers and books
- Petroleum products (subject to specific excise)

---

## Step 2: Transaction Classification Rules

### 2a. Transaction Type [T1]
- Sale (TVA collectée + CAC) or Purchase (TVA déductible + CAC)
- Salaries, CNPS contributions, dividends, loan repayments = OUT OF SCOPE

### 2b. Counterparty Location [T1]
- Domestic (Cameroon)
- CEMAC: Central African Republic, Chad, Congo-Brazzaville, Equatorial Guinea, Gabon
- Rest of World
- **Note:** CEMAC has a common customs union but NO common VAT area.

### 2c. Supply Type [T1]
- Goods / Services / Import of goods (customs) / Import of services (autoliquidation)
- **Legislation:** CGI, Art. 125 (champ d'application)

---

## Step 3: VAT Return Form Structure [T1]

### Output Section

| Line | Description | Mapping |
|------|-------------|---------|
| A1 | CA taxable au taux normal | Standard-rated sales (base) |
| A2 | Opérations exonérées | Exempt supplies |
| A3 | Exportations (0%) | Zero-rated |
| A4 | Total CA | A1 + A2 + A3 |
| A5 | TVA collectée (17.5% on A1) | Output TVA |
| A6 | CAC (10% of A5) | Municipal surcharge |
| A7 | TVA sur autoliquidation | Reverse charge output |
| A8 | CAC sur autoliquidation | CAC on reverse charge |
| A9 | Régularisations | Credit notes, adjustments |
| A10 | Total TVA + CAC brute | A5 + A6 + A7 + A8 + A9 |

### Input Section

| Line | Description | Mapping |
|------|-------------|---------|
| B1 | TVA sur achats locaux | Input TVA on local purchases |
| B2 | CAC sur achats locaux | Input CAC on local purchases |
| B3 | TVA sur importations | TVA from customs |
| B4 | CAC sur importations | CAC from customs |
| B5 | TVA + CAC sur immobilisations | VAT + CAC on capital goods |
| B6 | TVA + CAC autoliquidation (input) | Reverse charge input |
| B7 | Exclusions et régularisations | Blocked items |
| B8 | Total TVA + CAC déductible | B1 + B2 + B3 + B4 + B5 + B6 - B7 |

### Net Calculation

| Line | Description | Formula |
|------|-------------|---------|
| C1 | TVA + CAC nette | A10 - B8 |
| C2 | Crédit reporté | Prior period |
| C3 | Montant à payer / Crédit à reporter | C1 - C2 |

---

## Step 4: Reverse Charge (Autoliquidation) [T1]

**Legislation:** CGI, Art. 135 (autoliquidation).

When a Cameroon VAT-registered person receives services from a non-resident:
1. Self-assess output TVA at 17.5% + CAC at 10% of TVA
2. Claim input TVA + CAC if for taxable supplies
3. Net effect: zero for fully taxable businesses

**Both TVA and CAC must be self-assessed on imported services.**

---

## Step 5: Deductibility Check

### Blocked Input Tax [T1]
**Legislation:** CGI, Art. 144-147 (exclusions).
- Vehicles for personal transport (< 9 seats), unless taxi/hire (Art. 145)
- Accommodation and lodging for staff (Art. 145)
- Entertainment, reception, and gifts (Art. 145)
- Petroleum products for blocked vehicles (Art. 145)
- Personal use goods and services (Art. 146)
- Purchases not supported by proper invoices with NIU (Art. 147)

**Both TVA and CAC are blocked together. You cannot recover TVA but not CAC or vice versa.**

### Partial Exemption (Prorata) [T2]
**Legislation:** CGI, Art. 143.
`Prorata = (Taxable + Export Turnover) / Total Turnover * 100`
**Flag for reviewer: DGI must approve. Annual recalculation required.**

---

## Step 6: Key Thresholds [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Régime réel | FCFA 100,000,000+ annual turnover | CGI |
| Régime simplifié | FCFA 50,000,000 - 100,000,000 | CGI |
| Régime de base | Below FCFA 50,000,000 (patente/forfait) | CGI |
| Capital goods adjustment (immovable) | 10 years | CGI, Art. 148 |
| Capital goods adjustment (movable) | 5 years | CGI, Art. 148 |

---

## Step 7: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|-----------|--------|----------|-------------|
| TVA return (régime réel) | Monthly | 15th of following month | CGI, Art. 150 |
| TVA return (simplifié) | Quarterly | 15th of month following quarter | CGI |
| Payment | Same as return | Same deadline | CGI |

### Penalties [T1]
- Late filing: 30% surcharge on tax due
- Late payment: interest at 1.5% per month
- Failure to register: 100% of tax due plus penalties

---

## PROHIBITIONS [T1]

- NEVER separate TVA recovery from CAC recovery -- they are always blocked or allowed together
- NEVER let AI guess return line assignment
- NEVER allow recovery on blocked categories
- NEVER confuse zero-rated with exempt
- NEVER apply reverse charge to out-of-scope categories
- NEVER forget the CAC when computing self-assessed reverse charge
- NEVER treat CEMAC transactions as intra-community
- NEVER compute numbers -- engine handles arithmetic
- NEVER file without checking crédit reporté
- NEVER accept invoices without valid NIU for input purposes

---

## Step 8: Edge Case Registry

### EC1 -- Import of services (SaaS from US) [T1]
**Situation:** Company subscribes to AWS. Monthly USD 300. No VAT.
**Resolution:** Autoliquidation. Self-assess TVA 17.5% + CAC 10% of TVA (= effective 19.25%). Claim input if taxable. Net zero.
**Legislation:** CGI, Art. 135.

### EC2 -- Export of timber (zero-rated) [T1]
**Situation:** Exporter ships processed timber to China.
**Resolution:** Zero-rated. Line A3. No TVA/CAC. Input TVA + CAC fully recoverable.
**Legislation:** CGI, Art. 128.

### EC3 -- Motor vehicle (blocked) [T1]
**Situation:** Company purchases sedan for director.
**Resolution:** Both TVA and CAC BLOCKED. Cost includes irrecoverable tax.
**Legislation:** CGI, Art. 145.

### EC4 -- CEMAC import (from Gabon) [T1]
**Situation:** Company imports goods from Gabon.
**Resolution:** TVA 17.5% + CAC charged at Cameroon customs. No intra-community mechanism. Recoverable if taxable.
**Legislation:** CGI; CEMAC Directive.

### EC5 -- Mixed supply [T2]
**Situation:** Company provides taxable IT services and exempt financial advisory.
**Resolution:** Prorata applies. Flag for reviewer.
**Legislation:** CGI, Art. 143.

### EC6 -- Free zone enterprise [T3]
**Situation:** Company operates in Douala Free Zone.
**Resolution:** Free zone enterprises may have VAT exemptions under specific regime. Escalate. Specific decree must be verified.
**Legislation:** Free Zone Law 1990; specific enterprise decree.

### EC7 -- Excise interaction [T2]
**Situation:** Company sells beverages subject to both excise duty and TVA.
**Resolution:** TVA is calculated on the base price PLUS excise duty. The excise is included in the TVA base. Flag for reviewer: confirm excise rate applicable to the specific product.
**Legislation:** CGI, Art. 127; Excise provisions.

### EC8 -- Bad debt relief [T2]
**Situation:** Client unpaid for 2 years. TVA + CAC were remitted.
**Resolution:** Bad debt relief available under strict conditions. Court judgment or insolvency proof required. Flag for reviewer.
**Legislation:** CGI, Art. 149.

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
**Input:** Company sells goods for FCFA 10,000,000 net. Standard-rated.
**Expected output:** A1 = FCFA 10,000,000. A5 = FCFA 1,750,000 (17.5%). A6 = FCFA 175,000 (CAC = 10% of 1,750,000). Total = FCFA 1,925,000.

### Test 2 -- Local purchase, input recovery [T1]
**Input:** Company buys supplies. Invoice: FCFA 5,000,000 + FCFA 875,000 TVA + FCFA 87,500 CAC = FCFA 5,962,500.
**Expected output:** B1 = FCFA 875,000. B2 = FCFA 87,500. Both recoverable.

### Test 3 -- Reverse charge (autoliquidation) [T1]
**Input:** Company receives IT services from French firm. FCFA 8,000,000. No VAT.
**Expected output:** A7 = FCFA 1,400,000 (17.5%). A8 = FCFA 140,000 (CAC). B6 = FCFA 1,540,000 (input TVA + CAC). Net zero.

### Test 4 -- Export (zero-rated) [T1]
**Input:** Exporter ships cocoa worth FCFA 200,000,000.
**Expected output:** A3 = FCFA 200,000,000. TVA = 0. CAC = 0. Input TVA + CAC recoverable.

### Test 5 -- Blocked (entertainment) [T1]
**Input:** Company hosts event. Invoice: FCFA 3,000,000 + FCFA 525,000 TVA + FCFA 52,500 CAC.
**Expected output:** Input TVA = 0 and Input CAC = 0 (BLOCKED). Cost = FCFA 3,577,500.

### Test 6 -- Exempt supply [T1]
**Input:** School provides educational services for FCFA 50,000,000.
**Expected output:** A2 = FCFA 50,000,000. No TVA/CAC. Related input TVA + CAC NOT recoverable.

---

## Step 11: Out of Scope -- Direct Tax [T3]

- **Corporate Income Tax (IS):** 33% (including 10% surcharge on principal tax).
- **PAYE (IRPP):** Progressive rates 10%-35%. Employer obligation.
- **Social charges (CNPS):** Family allowances 7%, work injury 1.75%-5%. Separate from TVA.

---

## Contribution Notes

Cameroon-specific elements include the CAC municipal surcharge (10% of TVA), CEMAC customs union, the interaction between excise and TVA bases, and the 2026 Finance Law reduced 10% TVA rate for social housing.

**A skill may not be published without sign-off from a licensed expert-comptable in Cameroon.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
