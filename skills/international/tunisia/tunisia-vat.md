---
name: tunisia-vat
description: Use this skill whenever asked to prepare, review, or create a Tunisia VAT (TVA) return for any client. Trigger on phrases like "prepare VAT return", "TVA Tunisie", "DGI return", "declaration TVA", or any request involving Tunisia VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Tunisia VAT classification rules with its three-rate structure (19%/13%/7%), return form mappings, deductibility rules, droit de consommation interaction, reverse charge, registration thresholds, and filing deadlines. ALWAYS read this skill before touching any Tunisia VAT-related work.
---

# Tunisia VAT (TVA) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Tunisia (Republic of Tunisia) |
| Jurisdiction Code | TN |
| Primary Legislation | Code de la Taxe sur la Valeur Ajoutée (Code de la TVA), as amended |
| Supporting Legislation | Code des Droits et Procédures Fiscaux; Loi de Finances annuelle; Code des Douanes |
| Tax Authority | Direction Générale des Impôts (DGI) |
| Filing Portal | https://www.impots.finances.gov.tn |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by a licensed expert-comptable in Tunisia |
| Validation Date | Pending |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: rate application (19%/13%/7%), return mapping, registration, deadlines, blocked categories. Tier 2: partial exemption, mixed supplies, droit de consommation interaction, suspension regime. Tier 3: offshore companies, free trade zones, oil & gas. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag for expert-comptable.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate.

---

## Step 0: Client Onboarding Questions

1. **Entity name and Matricule Fiscal** [T1] -- 7+1+3 digit tax identifier
2. **VAT registration status** [T1] -- assujetti obligatoire, assujetti volontaire, or non-assujetti
3. **Filing regime** [T1] -- mensuelle (monthly) or trimestrielle (quarterly)
4. **Industry/sector** [T2] -- impacts rate classification
5. **Does the business make exempt or suspended supplies?** [T2] -- suspension regime is distinct from exemption
6. **Does the business import goods?** [T1] -- customs TVA
7. **Crédit de TVA reporté** [T1] -- credit brought forward
8. **Does the business benefit from any investment incentive?** [T2] -- Code d'Incitations aux Investissements

**If items 1-2 are unknown, STOP.**

---

## Step 1: VAT Rate Structure [T1]

| Rate | Description | Key Supplies | Legislation |
|------|-------------|-------------|-------------|
| 19% | Standard rate (taux normal) | Most goods and services | Code TVA, Art. 7 |
| 13% | Intermediate rate | Hotel/tourism, certain construction materials, legal/accounting services. **Note (2025 Finance Law):** For real estate developers, the 13% rate has been replaced by a tiered structure: 7% for properties at or below TND 400,000 and 19% for those exceeding TND 400,000 | Code TVA, Art. 7; Loi de Finances 2025 |
| 7% | Reduced rate | Basic foodstuffs, pharmaceutical products, agricultural equipment, IT equipment, low-voltage domestic electricity (up to 300 kWh/month, reduced from 13% by 2025 Finance Law), buses for employee transport by industrial enterprises (reduced from 19% by 2025 Finance Law) | Code TVA, Art. 7; Loi de Finances 2025 |
| Exempt | Exonérations | Financial services, education, medical, bread, cereals | Code TVA, Art. 8-9 |
| Suspended | Suspension de TVA | Exports, inputs for exporters (with certificate), investment goods under incentive code | Code TVA, Art. 10-11 |

### Suspension Regime [T1]
**Legislation:** Code TVA, Art. 10-11.

The suspension regime is unique to Tunisia. It is NOT zero-rating. Businesses that qualify can purchase goods/services without TVA being charged (en suspension), provided they hold a valid suspension certificate (attestation de suspension) issued by the DGI.

Qualifying businesses:
- Exporters (who export at least 80% of production)
- Businesses making supplies under investment incentive code
- Businesses purchasing inputs destined for export production

**The supplier must verify the buyer's attestation de suspension before issuing an invoice without TVA.**

---

## Step 2: Transaction Classification Rules

### 2a. Transaction Type [T1]
- Sale (TVA collectée) or Purchase (TVA déductible)
- Salaries, CNSS, CNRPS, dividends, loan repayments = OUT OF SCOPE

### 2b. Counterparty Location [T1]
- Domestic (Tunisia)
- Maghreb: Morocco, Algeria, Libya, Mauritania
- EU: trading partner (Association Agreement) but no common VAT
- Rest of World

### 2c. Supply Type [T1]
- Goods / Services / Import of goods (customs) / Import of services (autoliquidation)
- **Legislation:** Code TVA, Art. 3 (territoriality)

---

## Step 3: VAT Return Form Structure [T1]

### Output Section

| Line | Description | Mapping |
|------|-------------|---------|
| 1 | CA taxable à 19% | Standard-rated sales |
| 2 | CA taxable à 13% | Intermediate-rated sales |
| 3 | CA taxable à 7% | Reduced-rated sales |
| 4 | CA en suspension | Supplies under suspension regime |
| 5 | CA exonéré | Exempt supplies |
| 6 | Exportations | Export sales |
| 7 | Total CA | Sum of 1-6 |
| 8 | TVA collectée à 19% | 19% on Line 1 |
| 9 | TVA collectée à 13% | 13% on Line 2 |
| 10 | TVA collectée à 7% | 7% on Line 3 |
| 11 | TVA sur autoliquidation | Reverse charge output |
| 12 | Régularisations | Adjustments |
| 13 | Total TVA brute | 8 + 9 + 10 + 11 + 12 |

### Input Section

| Line | Description | Mapping |
|------|-------------|---------|
| 14 | TVA sur achats de marchandises | VAT on goods for resale |
| 15 | TVA sur achats de matières et fournitures | VAT on materials/supplies |
| 16 | TVA sur services | VAT on services |
| 17 | TVA sur immobilisations | VAT on capital goods |
| 18 | TVA sur importations | Customs VAT |
| 19 | TVA autoliquidation (input) | Reverse charge input |
| 20 | Exclusions | Blocked items |
| 21 | Total TVA déductible | 14 + 15 + 16 + 17 + 18 + 19 - 20 |

### Net Calculation

| Line | Description | Formula |
|------|-------------|---------|
| 22 | TVA due | 13 - 21 |
| 23 | Crédit reporté | Prior period |
| 24 | Retenue à la source TVA | Withholding (if applicable) |
| 25 | TVA à payer / Crédit | 22 - 23 - 24 |

---

## Step 4: Reverse Charge (Autoliquidation) [T1]

**Legislation:** Code TVA, Art. 19 (autoliquidation sur services importés).

When a Tunisia VAT-registered person receives services from a non-resident:
1. Self-assess output TVA at applicable rate (usually 19%) -- Line 11
2. Claim input TVA -- Line 19
3. Net effect: zero for fully taxable businesses

---

## Step 5: Withholding VAT (Retenue à la Source) [T1]

**Legislation:** Code TVA, Art. 19 bis.

Certain entities (government, public enterprises, large companies designated by Finance Ministry) must withhold TVA at source:
- Rate: 25% of the TVA amount on the invoice
- Supplier claims credit on Line 24
- Agent remits to DGI

### Example [T1]
Invoice: TND 10,000 + TND 1,900 TVA = TND 11,900.
Withholding: 25% of TND 1,900 = TND 475.
Supplier receives: TND 11,425. Claims TND 475 credit.

---

## Step 6: Deductibility Check

### Blocked Input Tax [T1]
**Legislation:** Code TVA, Art. 10-12 (exclusions).
- Vehicles for personal transport (< 9 seats), unless taxi/hire (Art. 10)
- Accommodation and lodging for personnel (Art. 10)
- Reception, entertainment, and gifts (Art. 10)
- Petroleum products for blocked vehicles (Art. 10)
- Personal use (Art. 10)
- Purchases without valid invoice with matricule fiscal (Art. 12)

### Partial Exemption (Prorata) [T2]
**Legislation:** Code TVA, Art. 9.
`Prorata = (Taxable + Suspended + Export Turnover) / Total Turnover * 100`
Rounded up. **Suspension turnover counts as "with right to deduct" for prorata purposes.**
**Flag for reviewer: annual recalculation required.**

---

## Step 7: Droit de Consommation (DC) Interaction [T1]

**Legislation:** Code du Droit de Consommation.

Droit de Consommation is an excise-type tax on specific goods (alcohol, tobacco, vehicles, cosmetics, etc.). When DC applies:
- TVA is calculated on the price INCLUDING the DC amount
- DC is part of the TVA taxable base
- This increases the effective tax burden

Example: Good at TND 1,000 + DC at 25% (TND 250) = TVA base TND 1,250. TVA at 19% = TND 237.50.

---

## Step 8: Key Thresholds [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory registration | TND 100,000 annual turnover (goods) or TND 50,000 (services) | Code TVA, Art. 2 |
| Voluntary registration | Below threshold (with approval) | Code TVA, Art. 2 |
| Monthly filing | Turnover >= TND 1,000,000 | Code TVA, Art. 18 |
| Quarterly filing | Below TND 1,000,000 | Code TVA, Art. 18 |
| Withholding rate | 25% of TVA amount | Art. 19 bis |

---

## Step 9: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|-----------|--------|----------|-------------|
| TVA return (monthly) | Monthly | 15th of following month (paper) / 28th (electronic) | Code TVA, Art. 18 |
| TVA return (quarterly) | Quarterly | 15th/28th of month following quarter | Code TVA, Art. 18 |
| Payment | Same as return | Same deadline | Code TVA |

### Penalties [T1]
- Late filing: 1% per month of tax due (minimum TND 50)
- Late payment: 0.75% per month interest
- Failure to register: penalties per Code des Droits et Procédures Fiscaux

---

## PROHIBITIONS [T1]

- NEVER confuse suspension regime with exemption -- they are entirely different
- NEVER let AI guess return line assignment or rate
- NEVER allow recovery on blocked categories
- NEVER apply wrong rate -- three rates exist
- NEVER apply reverse charge to out-of-scope categories
- NEVER compute numbers -- engine handles arithmetic
- NEVER file without checking crédit reporté
- NEVER issue invoice en suspension without verifying buyer's attestation
- NEVER forget to include DC in the TVA base when applicable
- NEVER accept invoices without valid matricule fiscal

---

## Step 10: Edge Case Registry

### EC1 -- Import of services (SaaS) [T1]
**Situation:** Company subscribes to Slack. Monthly USD 30. No VAT.
**Resolution:** Autoliquidation at 19%. Output Line 11, Input Line 19. Net zero.
**Legislation:** Code TVA, Art. 19.

### EC2 -- Export (suspension) [T1]
**Situation:** Manufacturer exports 100% of production to EU.
**Resolution:** Sales reported under suspension (Line 4/6). Input TVA fully recoverable. Must hold attestation de suspension for purchases.
**Legislation:** Code TVA, Art. 10-11.

### EC3 -- Hotel services (13%) [T1]
**Situation:** Hotel charges room TND 200/night.
**Resolution:** TVA at 13%. Line 2 for turnover. Line 9 for output TVA.
**Legislation:** Code TVA, Art. 7.

### EC4 -- Pharmaceutical product (7%) [T1]
**Situation:** Pharmacy sells medicines TND 50,000.
**Resolution:** TVA at 7%. Line 3. Line 10.
**Legislation:** Code TVA, Art. 7.

### EC5 -- Product subject to DC [T1]
**Situation:** Importer of cosmetics. CIF value TND 100,000. DC at 25%.
**Resolution:** DC = TND 25,000. TVA base = TND 125,000. TVA at 19% = TND 23,750. Total tax = TND 48,750.
**Legislation:** Code TVA; Code DC.

### EC6 -- Withholding TVA by public entity [T1]
**Situation:** Ministry pays VAT-registered supplier. Invoice TND 50,000 + TND 9,500 TVA.
**Resolution:** Withhold 25% of TND 9,500 = TND 2,375. Supplier claims credit Line 24.
**Legislation:** Code TVA, Art. 19 bis.

### EC7 -- Supplier with suspension certificate buying inputs [T2]
**Situation:** Exporter with attestation de suspension purchases raw materials locally.
**Resolution:** Supplier issues invoice without TVA (en suspension). Buyer does not charge or pay TVA. Flag for reviewer: verify attestation validity and scope.
**Legislation:** Code TVA, Art. 10-11.

### EC8 -- Mixed supply (prorata) [T2]
**Situation:** Company provides taxable consulting (19%) and exempt financial services.
**Resolution:** Prorata applies. Include suspension turnover in numerator. Flag for reviewer.
**Legislation:** Code TVA, Art. 9.

---

## Step 11: Reviewer Escalation Protocol

```
REVIEWER FLAG / ESCALATION REQUIRED
[Standard format as per other skills]
```

---

## Step 12: Test Suite

### Test 1 -- Standard sale (19%) [T1]
**Input:** Company sells goods TND 100,000 net.
**Expected output:** Line 1 = TND 100,000. Line 8 = TND 19,000 (19%).

### Test 2 -- Hotel sale (13%) [T1]
**Input:** Hotel revenue TND 50,000.
**Expected output:** Line 2 = TND 50,000. Line 9 = TND 6,500 (13%).

### Test 3 -- Pharmaceutical (7%) [T1]
**Input:** Pharmacy sales TND 30,000.
**Expected output:** Line 3 = TND 30,000. Line 10 = TND 2,100 (7%).

### Test 4 -- Reverse charge [T1]
**Input:** Company receives services from French firm. TND 20,000.
**Expected output:** Line 11 = TND 3,800 (19% output). Line 19 = TND 3,800 (input). Net zero.

### Test 5 -- Export [T1]
**Input:** Exporter ships goods TND 500,000.
**Expected output:** Line 6 = TND 500,000. TVA = 0. Input TVA recoverable.

### Test 6 -- Blocked (vehicle) [T1]
**Input:** Company buys sedan. TND 50,000 + TND 9,500 TVA.
**Expected output:** Input TVA = 0 (BLOCKED). Cost = TND 59,500.

---

## Step 13: Out of Scope -- Direct Tax [T3]

- **Corporate Income Tax (IS):** 15% standard (reduced from 25% in 2021 reform). Specific sectors may have different rates.
- **PAYE (IRPP):** Progressive 0%-35%.
- **CNSS/CNRPS:** Social security contributions. Separate from TVA.

---

## Contribution Notes

Tunisia-specific elements include the suspension regime, three VAT rates, droit de consommation interaction, withholding TVA (25% of TVA amount), and attestation de suspension requirements.

**A skill may not be published without sign-off from a licensed expert-comptable in Tunisia.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
