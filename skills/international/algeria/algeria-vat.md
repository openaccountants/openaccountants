---
name: algeria-vat
description: Use this skill whenever asked to prepare, review, or create an Algeria VAT (TVA) return for any client. Trigger on phrases like "prepare VAT return", "TVA Algérie", "DGI return", "declaration TVA", or any request involving Algeria VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Algeria VAT classification rules with its two-rate structure (19%/9%), return form mappings, deductibility rules, reverse charge treatment, registration thresholds, and filing deadlines. ALWAYS read this skill before touching any Algeria VAT-related work.
---

# Algeria VAT (TVA) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Algeria (People's Democratic Republic of Algeria) |
| Jurisdiction Code | DZ |
| Primary Legislation | Code des Taxes sur le Chiffre d'Affaires (Code des TCA), Ordonnance 76-104 as amended |
| Supporting Legislation | Code des Procédures Fiscales; Loi de Finances annuelle; Code des Douanes |
| Tax Authority | Direction Générale des Impôts (DGI) |
| Filing Portal | https://jibayatic.mf.gov.dz (Jibayatic portal) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by a licensed commissaire aux comptes in Algeria |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate application (19%/9%), return mapping, registration, deadlines, blocked categories. Tier 2: partial exemption, mixed supplies, petroleum sector, précompte. Tier 3: foreign oil companies, military procurement, special conventions. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag for commissaire aux comptes.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate.

---

## Step 0: Client Onboarding Questions

1. **Entity name and NIF (Numéro d'Identification Fiscale)** [T1]
2. **Article d'imposition** [T1] -- tax article number
3. **VAT registration status** [T1] -- assujetti or non-assujetti
4. **Filing regime** [T1] -- régime réel (monthly) or régime simplifié
5. **Industry/sector** [T2] -- impacts classification (hydrocarbons, mining, agriculture)
6. **Does the business make exempt supplies?** [T2] -- if yes, prorata required
7. **Does the business import goods?** [T1] -- customs TVA
8. **Crédit de TVA reporté** [T1] -- credit brought forward
9. **Does the business benefit from investment incentives (ANDI)?** [T2] -- may affect TVA on capital goods

**If items 1-3 are unknown, STOP.**

---

## Step 1: VAT Rate Structure [T1]

| Rate | Description | Key Supplies | Legislation |
|------|-------------|-------------|-------------|
| 19% | Standard rate (taux normal) | Most goods and services | Code TCA, Art. 21 |
| 9% | Reduced rate (taux réduit) | Basic foodstuffs, pharmaceutical products, agricultural inputs, tourism/hotel, IT equipment, renewable energy equipment | Code TCA, Art. 23 |
| Exempt | Exonérations | Financial services (interest), bread, semolina, milk, exports, medical, education | Code TCA, Art. 8-9 |

### Exempt Supplies [T1]
**Legislation:** Code TCA, Art. 8-9.
- Bread, semolina, flour (basic staples)
- Fresh milk
- Financial services (loan interest, life insurance premiums)
- Medical and healthcare (public sector)
- Educational services (authorized institutions)
- Exports (exempt with right to deduct -- similar to zero-rating)
- Agricultural production at primary stage
- Operations carried out by small artisans (below threshold)

### Export Treatment [T1]
Exports are exempt with full right to deduct input TVA. Effectively zero-rated. Must have customs export documentation.

---

## Step 2: Transaction Classification Rules

### 2a. Transaction Type [T1]
- Sale (TVA collectée) or Purchase (TVA déductible)
- Salaries, CNAS/CASNOS, dividends, loan repayments = OUT OF SCOPE

### 2b. Counterparty Location [T1]
- Domestic (Algeria)
- Maghreb: Morocco, Tunisia, Libya, Mauritania
- Rest of World
- **Note:** Algeria has no common VAT area with any regional bloc.

### 2c. Supply Type [T1]
- Goods / Services / Import of goods (customs) / Import of services (autoliquidation)
- **Legislation:** Code TCA, Art. 2-3 (champ d'application)

---

## Step 3: VAT Return Form Structure [T1]

Filed monthly (G50 declaration) via Jibayatic portal.

### Output Section

| Line | Description | Mapping |
|------|-------------|---------|
| 1 | CA taxable à 19% | Standard-rated sales |
| 2 | CA taxable à 9% | Reduced-rated sales |
| 3 | CA exonéré | Exempt supplies |
| 4 | Exportations | Export sales (exempt with deduction) |
| 5 | Total CA | 1 + 2 + 3 + 4 |
| 6 | TVA collectée à 19% | 19% on Line 1 |
| 7 | TVA collectée à 9% | 9% on Line 2 |
| 8 | TVA sur autoliquidation | Reverse charge output |
| 9 | Régularisations | Adjustments |
| 10 | Total TVA brute | 6 + 7 + 8 + 9 |

### Input Section

| Line | Description | Mapping |
|------|-------------|---------|
| 11 | TVA sur achats de biens et services | Input TVA on operating purchases |
| 12 | TVA sur immobilisations | Input TVA on capital goods |
| 13 | TVA sur importations | Customs TVA |
| 14 | TVA autoliquidation (input) | Reverse charge input |
| 15 | Exclusions | Blocked items |
| 16 | Total TVA déductible | 11 + 12 + 13 + 14 - 15 |

### Net Calculation

| Line | Description | Formula |
|------|-------------|---------|
| 17 | TVA due | 10 - 16 |
| 18 | Précomptes | Advance payments of TVA |
| 19 | Crédit reporté | Prior period |
| 20 | TVA à payer / Crédit | 17 - 18 - 19 |

**Note:** The G50 (Série G50) is a comprehensive monthly declaration that includes TVA, TAP (Taxe sur l'Activité Professionnelle), IRPP withholding, and other taxes. The TVA section is one part of the G50.

---

## Step 4: Reverse Charge (Autoliquidation) [T1]

**Legislation:** Code TCA, Art. 14 (autoliquidation).

When an Algerian VAT-registered person receives services from a non-resident:
1. Self-assess output TVA at applicable rate (19% or 9%) -- Line 8
2. Claim input TVA -- Line 14
3. Net effect: zero for fully taxable businesses

---

## Step 5: Précompte TVA [T1]

**Legislation:** Code TCA, Art. 41 bis.

Certain designated entities (government, state enterprises, large taxpayers) must apply a précompte (advance withholding) of TVA:
- Rate: varies (typically 25% of TVA on the invoice, or specific rates per sector)
- Supplier claims credit on G50 (Line 18)
- Agent remits to DGI

---

## Step 6: Deductibility Check

### Blocked Input Tax [T1]
**Legislation:** Code TCA, Art. 29-33 (exclusions).
- Vehicles for personal transport (< 9 seats), unless taxi/hire (Art. 30)
- Accommodation and lodging (Art. 30)
- Entertainment and reception (Art. 30)
- Personal use goods and services (Art. 31)
- Petroleum products for blocked vehicles (Art. 30)
- Purchases without proper invoice with NIF (Art. 33)

### Partial Exemption (Prorata) [T2]
**Legislation:** Code TCA, Art. 34.
`Prorata = (Taxable + Export Turnover) / Total Turnover * 100`
**Flag for reviewer: annual recalculation required. DGI may challenge.**

---

## Step 7: Taxe sur l'Activité Professionnelle (TAP) [T1]

**Note:** TAP is NOT a VAT/TVA. It is a separate turnover tax at 1% (production) or 2% (services/commerce). It is reported on the same G50 form but is a completely separate obligation. Do NOT confuse TAP with TVA. TAP is not recoverable as input tax.

---

## Step 8: Key Thresholds [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory registration | DZD 15,000,000 annual turnover (services) or DZD 15,000,000 (goods) | Code TCA, Art. 3 |
| Régime simplifié (IFU) | Below DZD 15,000,000 -- pays Impôt Forfaitaire Unique instead of TVA | Code TCA |
| Capital goods deduction | Immediate in month of acquisition/payment | Code TCA, Art. 28 |

---

## Step 9: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|-----------|--------|----------|-------------|
| G50 declaration (includes TVA) | Monthly | 20th of following month | Code TCA, Art. 36 |
| Payment | Monthly | Same as filing | Code TCA |

### Penalties [T1]
- Late filing: 25% surcharge on tax due
- Late payment: 10% surcharge + 3% interest per month
- Failure to register: penalties per Code des Procédures Fiscales

---

## PROHIBITIONS [T1]

- NEVER confuse TVA with TAP -- they are separate taxes on the same G50 form
- NEVER let AI guess return line assignment or rate
- NEVER allow recovery on blocked categories
- NEVER apply wrong rate -- two rates exist (19% and 9%)
- NEVER apply reverse charge to out-of-scope categories
- NEVER compute numbers -- engine handles arithmetic
- NEVER file without checking crédit reporté
- NEVER confuse IFU (forfaitaire) regime with TVA regime
- NEVER accept invoices without valid NIF
- NEVER ignore précompte credits when computing net liability

---

## Step 10: Edge Case Registry

### EC1 -- Import of services (SaaS) [T1]
**Situation:** Company subscribes to Oracle Cloud. Monthly USD 500.
**Resolution:** Autoliquidation at 19%. Output Line 8, Input Line 14. Net zero.
**Legislation:** Code TCA, Art. 14.

### EC2 -- Export of hydrocarbons [T3]
**Situation:** Oil company exports crude oil.
**Resolution:** Escalate. Hydrocarbon sector has specific tax regime under the Hydrocarbons Law. Do not apply standard TVA rules.
**Legislation:** Law on Hydrocarbons No. 19-13.

### EC3 -- Pharmaceutical product (9%) [T1]
**Situation:** Pharmacy sells medicines DZD 500,000.
**Resolution:** TVA at 9%. Line 2 for turnover. Line 7 for output.
**Legislation:** Code TCA, Art. 23.

### EC4 -- Motor vehicle (blocked) [T1]
**Situation:** Company buys sedan. DZD 3,000,000 + DZD 570,000 TVA.
**Resolution:** Input TVA = 0 (BLOCKED). Cost = DZD 3,570,000.
**Legislation:** Code TCA, Art. 30.

### EC5 -- IFU taxpayer boundary [T1]
**Situation:** Small business under IFU (forfaitaire) exceeds DZD 15,000,000 turnover.
**Resolution:** Must register for TVA and switch to régime réel within legal timeframe. Notify DGI.
**Legislation:** Code TCA, Art. 3.

### EC6 -- ANDI investment incentive [T2]
**Situation:** Company with ANDI investment certificate imports production equipment.
**Resolution:** May benefit from TVA exemption on capital goods imports. Flag for reviewer: verify ANDI certificate validity and scope.
**Legislation:** Investment Promotion Law 2022; Code TCA.

### EC7 -- Précompte by state enterprise [T1]
**Situation:** Sonatrach pays VAT-registered supplier. Invoice DZD 10,000,000 + DZD 1,900,000 TVA.
**Resolution:** Précompte at 25% of TVA = DZD 475,000 withheld. Supplier claims credit Line 18.
**Legislation:** Code TCA, Art. 41 bis.

### EC8 -- Mixed supply (prorata) [T2]
**Situation:** Bank provides taxable advisory (19%) and exempt interest-based services.
**Resolution:** Prorata applies. Flag for reviewer.
**Legislation:** Code TCA, Art. 34.

---

## Step 11: Reviewer Escalation Protocol

```
REVIEWER FLAG / ESCALATION REQUIRED
[Standard format]
```

---

## Step 12: Test Suite

### Test 1 -- Standard sale (19%) [T1]
**Input:** Company sells goods DZD 1,000,000 net.
**Expected output:** Line 1 = DZD 1,000,000. Line 6 = DZD 190,000 (19%).

### Test 2 -- Reduced rate (9%) [T1]
**Input:** Hotel revenue DZD 500,000.
**Expected output:** Line 2 = DZD 500,000. Line 7 = DZD 45,000 (9%).

### Test 3 -- Reverse charge [T1]
**Input:** Company receives IT services from French firm. DZD 2,000,000.
**Expected output:** Line 8 = DZD 380,000 (19% output). Line 14 = DZD 380,000 (input). Net zero.

### Test 4 -- Export [T1]
**Input:** Exporter ships goods DZD 50,000,000.
**Expected output:** Line 4 = DZD 50,000,000. TVA = 0. Input TVA recoverable.

### Test 5 -- Blocked (entertainment) [T1]
**Input:** Company hosts reception. DZD 500,000 + DZD 95,000 TVA.
**Expected output:** Input TVA = 0 (BLOCKED). Cost = DZD 595,000.

### Test 6 -- Précompte [T1]
**Input:** State enterprise pays supplier. Invoice DZD 5,000,000 + DZD 950,000 TVA. Précompte 25%.
**Expected output:** Withholding = DZD 237,500. Supplier claims Line 18.

---

## Step 13: Out of Scope -- Direct Tax [T3]

- **Corporate Income Tax (IBS):** 19% (production), 23% (construction/public works/tourism), 26% (other).
- **IRPP:** Progressive rates 0%-35%.
- **Social charges (CNAS/CASNOS):** Employer ~26%, employee ~9%. Separate from TVA.
- **TAP:** 1%-2% turnover tax. Separate from TVA but on same G50.

---

## Contribution Notes

Algeria-specific elements include the dual-rate structure (19%/9%), the G50 multi-tax declaration, TAP distinction, IFU forfaitaire boundary, précompte mechanism, and ANDI investment incentives.

**A skill may not be published without sign-off from a licensed commissaire aux comptes in Algeria.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
