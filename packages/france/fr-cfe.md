---
name: fr-cfe
description: Use this skill whenever asked about the French Cotisation Foncière des Entreprises (CFE) for self-employed individuals. Trigger on phrases like "CFE France", "Cotisation Foncière", "cotisation foncière des entreprises", "CET France", "CFE auto-entrepreneur", "taxe professionnelle", "CFE micro-entreprise", or any question about local business tax obligations for a self-employed client in France. Covers the rental value base, municipal rates, first-year exemption, and minimum contribution. ALWAYS read this skill before touching any France CFE work.
---

# France CFE (Cotisation Foncière des Entreprises) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | France |
| Jurisdiction Code | FR |
| Primary Legislation | Code Général des Impôts (CGI), articles 1447 to 1478 |
| Supporting Legislation | CGI art. 1647 D (minimum contribution); art. 1449-1466 (exemptions) |
| Tax Authority | DGFiP (Direction Générale des Finances Publiques) |
| Contributor | Open Accountants |
| Validated By | Pending -- requires validation by French expert-comptable |
| Validation Date | Pending |
| Skill Version | 1.0 |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and present options.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess.

---

## Step 0: Client Onboarding Questions

Before computing, you MUST know:

1. **Activity type** [T1] -- entreprise individuelle, micro-entreprise / auto-entrepreneur, profession libérale, or société?
2. **Year of creation** [T1] -- first-year exemption applies in the year of business creation
3. **Location of business premises** [T1] -- municipality determines the rate and minimum
4. **Type of premises** [T1] -- home-based (domiciliation), rented office, owned premises?
5. **Chiffre d'affaires (turnover) or recettes** [T1] -- determines the minimum CFE bracket
6. **Any specific exemptions claimed?** [T2] -- ZFU, ZRR, ZRD, artisan, etc.

**If location is unknown, STOP. CFE rates are set by municipalities and vary widely.**

---

## Step 1: What is CFE? [T1]

**Legislation:** CGI art. 1447

CFE is a **local business tax** (part of the CET -- Contribution Économique Territoriale, which replaced the old taxe professionnelle). All persons exercising a professional activity on 1 January of the tax year are liable.

CFE consists of:

```
CFE = base_imposable × taux_communal + taxes_additionnelles
```

Where:
- **Base imposable** = valeur locative cadastrale (cadastral rental value) of business premises
- **Taux communal** = rate set by the municipality (commune)
- **Taxes additionnelles** = chamber of commerce/industry levy, frais de gestion

---

## Step 2: Tax Base (Base Imposable) [T1]

**Legislation:** CGI art. 1467

### Standard Base

```
base_imposable = valeur_locative_cadastrale × coefficient_de_revalorisation
```

The valeur locative cadastrale is the theoretical annual rental value of the business premises as assessed by the cadastre. It is NOT actual rent paid.

### For Home-Based Businesses

If the self-employed person works from home:
- The valeur locative of the portion of the home used for business applies
- In practice, this is often very low (a fraction of the home's cadastral value)
- If no identifiable business premises exist, the **cotisation minimum** applies

### Reduction for New Establishments

In the **second year** of activity (first year after the creation year exemption), the base is reduced by **50%**.

---

## Step 3: Municipal Rates [T2]

**Legislation:** CGI art. 1636 B sexies

- Each municipality sets its own CFE rate annually
- Rates typically range from **15% to 35%** of the base, but can be higher or lower
- Additional rates apply for EPCI (intercommunalité), department, and chamber of commerce

**[T2] -- The exact rate is municipality-specific. Cannot compute without the commune's rate. Use impots.gouv.fr to look up specific rates.**

---

## Step 4: Cotisation Minimum (Minimum CFE) [T1]

**Legislation:** CGI art. 1647 D

If the calculated CFE based on the actual valeur locative is below a threshold, a **cotisation minimum** applies. The minimum is set by the municipality based on the taxpayer's chiffre d'affaires:

### Minimum CFE Brackets (2025)

| Chiffre d'Affaires (CA) or Recettes | Minimum Base Range (set by commune within these bounds) |
|-------------------------------------|--------------------------------------------------------|
| CA <= EUR 10,000 | EUR 243 -- EUR 579 |
| EUR 10,001 -- EUR 32,600 | EUR 243 -- EUR 1,158 |
| EUR 32,601 -- EUR 100,000 | EUR 243 -- EUR 2,433 |
| EUR 100,001 -- EUR 250,000 | EUR 243 -- EUR 4,056 |
| EUR 250,001 -- EUR 500,000 | EUR 243 -- EUR 5,793 |
| CA > EUR 500,000 | EUR 243 -- EUR 7,533 |

**The commune chooses a specific amount within the range. Each commune's minimum is different.**

### Micro-Entrepreneurs / Auto-Entrepreneurs

Micro-entrepreneurs are subject to CFE on the same basis. The minimum contribution applies if they have no identified business premises.

---

## Step 5: Exemptions [T1]

**Legislation:** CGI art. 1449-1466

### First-Year Exemption (Année de création)

**The year of business creation is fully exempt from CFE.**

- If business is created on 15 March 2025, no CFE is due for 2025
- CFE begins in 2026 (with 50% base reduction in this second year)
- Client must file form 1447-C-SD (declaration) before 31 December of the creation year

### Other Exemptions

| Exemption | Duration | Legislation |
|-----------|----------|-------------|
| Artisans (no employees, manual work) | Permanent | CGI art. 1452 |
| Taxi drivers (1 vehicle) | Permanent | CGI art. 1453 |
| Artists (painters, sculptors, etc.) | Permanent | CGI art. 1460 |
| Vendors with CA < EUR 5,000 | Permanent | CGI art. 1647 D bis |
| ZFU (Zone Franche Urbaine) | 5 years (+ 3-9 degressive) | CGI art. 1466 A |
| ZRR (Zone de Revitalisation Rurale) | 5 years | CGI art. 1465 A |

### CA < EUR 5,000 Exemption

Since 2019, businesses with chiffre d'affaires or recettes not exceeding EUR 5,000 are **exempt from cotisation minimum CFE**.

---

## Step 6: Computation Steps [T1]

### Step 6.1 -- Verify liability

```
IF year_of_creation: EXEMPT (no CFE due)
IF CA <= 5,000: EXEMPT from cotisation minimum
IF artisan/taxi/artist exemption applies: EXEMPT
```

### Step 6.2 -- Determine base

```
IF identifiable_business_premises:
    base = valeur_locative × revalorisation_coefficient
    IF second_year_of_activity: base = base × 50%
ELSE:
    base = cotisation_minimum_of_commune (based on CA bracket)
```

### Step 6.3 -- Apply municipal rate

```
CFE_brut = base × taux_communal
CFE_brut = max(CFE_brut, cotisation_minimum)
```

### Step 6.4 -- Add additional taxes

```
total_CFE = CFE_brut + frais_de_gestion (1%) + taxe_CCI (if applicable)
```

### Step 6.5 -- Cap (plafonnement CET)

The total CET (CFE + CVAE) cannot exceed 1.625% of valeur ajoutée (value added). If it does, a cap (plafonnement) applies.

---

## Step 7: Payment Schedule [T1]

**Legislation:** CGI art. 1679 quinquies

| Obligation | Deadline |
|------------|----------|
| Acompte (advance, if prior-year CFE > EUR 3,000) | **15 June** (50% of prior-year CFE) |
| Solde (balance / full payment) | **15 December** |
| Payment method | Online via impots.gouv.fr (mandatory for all) |

- CFE notices (avis d'imposition) are available on the espace professionnel on impots.gouv.fr from November
- No paper notice is sent -- the taxpayer must check online
- Late payment: 10% penalty + interest at 0.20%/month

### First Year After Creation

No acompte in the second year (first year of CFE liability) since there is no prior-year reference.

---

## Step 8: Tax Deductibility [T1]

| Question | Answer |
|----------|--------|
| Is CFE deductible from taxable income? | YES -- as a charge d'exploitation (business expense) |
| For micro-entrepreneurs? | NO direct deduction (already covered by the micro-fiscal abatement) |
| For régime réel? | YES -- fully deductible |

---

## Step 9: Edge Case Registry

### EC1 -- Auto-entrepreneur, first year [T1]
**Situation:** Client registered as auto-entrepreneur in May 2025.
**Resolution:** Exempt from CFE for 2025 (creation year). Must file form 1447-C-SD before 31 December 2025. CFE begins in 2026 with 50% base reduction.

### EC2 -- Home-based freelancer, no separate premises [T1]
**Situation:** Software developer working from home apartment, no dedicated office space rented.
**Resolution:** Cotisation minimum applies (based on CA bracket). If CA is EUR 25,000, minimum base is between EUR 243 and EUR 1,158 (set by commune). CFE = minimum_base x commune_rate.

### EC3 -- Turnover below EUR 5,000 [T1]
**Situation:** Part-time freelancer with EUR 3,500 annual turnover.
**Resolution:** Exempt from cotisation minimum CFE (since CA <= EUR 5,000). No CFE due if also no identifiable business premises with cadastral value.

### EC4 -- Artisan exemption [T1]
**Situation:** Client is a self-employed carpenter working alone with no employees.
**Resolution:** Artisan exemption applies under CGI art. 1452 if: works principally with manual labour, registered with Chambre de Métiers, and has no salaried employees (apprentices are allowed). Permanent CFE exemption.

### EC5 -- Multiple establishments [T2]
**Situation:** Client has a registered office in Paris and a workshop in Lyon.
**Resolution:** CFE is due separately in each commune where the client has premises. Each commune applies its own rate to the valeur locative of premises in its territory. [T2] -- confirm each commune's rate.

### EC6 -- Closing business mid-year [T1]
**Situation:** Client ceases activity on 30 June 2025.
**Resolution:** CFE is due for the full year 2025 (assessed on 1 January status). No pro-rata reduction for cessation mid-year. CFE ceases from 1 January of the year FOLLOWING cessation.

### EC7 -- ZFU / ZRR zone location [T2]
**Situation:** Client is based in a Zone Franche Urbaine.
**Resolution:** Potential 5-year exemption (+ degressive period). Must meet employment and turnover conditions. [T2] -- confirm zone eligibility and conditions with local SIE (Service des Impôts des Entreprises).

### EC8 -- CFE + CVAE combined cap [T2]
**Situation:** Client's CET (CFE + CVAE) exceeds 1.625% of value added.
**Resolution:** Plafonnement applies. Request cap calculation from SIE. [T2] -- CVAE computation needed for businesses with CA > EUR 500,000.

---

## Step 10: Test Suite

### Test 1 -- Creation year, exempt
**Input:** Auto-entrepreneur registered June 2025, CA EUR 20,000.
**Expected output:** CFE 2025 = EUR 0 (creation year exemption). Must file 1447-C-SD.

### Test 2 -- Second year, 50% reduction
**Input:** Business created 2024, premises valeur locative EUR 2,000, commune rate 25%, CA EUR 40,000.
**Expected output:** Base = EUR 2,000 x 50% = EUR 1,000. CFE = EUR 1,000 x 25% = EUR 250. Check against cotisation minimum for CA EUR 40,000.

### Test 3 -- Home-based, cotisation minimum
**Input:** Freelancer at home, no separate premises, CA EUR 25,000, commune minimum EUR 800.
**Expected output:** CFE = EUR 800 x commune rate. If commune rate 22%, CFE = EUR 176. But if cotisation minimum is set as a fixed amount (EUR 800 after rate), then CFE = EUR 800.

### Test 4 -- CA below EUR 5,000
**Input:** Part-time consultant, CA EUR 4,500.
**Expected output:** Exempt from cotisation minimum. CFE = EUR 0 (if no identifiable premises).

### Test 5 -- Artisan exemption
**Input:** Self-employed plumber, works alone, registered with Chambre de Métiers.
**Expected output:** Permanent exemption under CGI art. 1452. CFE = EUR 0.

### Test 6 -- High turnover, advance payment
**Input:** Established business, prior-year CFE EUR 4,500, CA EUR 350,000.
**Expected output:** Acompte due 15 June = EUR 2,250 (50% of prior year). Solde due 15 December = remainder after recalculation.

---

## PROHIBITIONS

- NEVER compute CFE without knowing the commune -- rates vary enormously between municipalities
- NEVER forget the first-year exemption -- creation year is always exempt
- NEVER ignore the 50% base reduction in the second year of activity
- NEVER state that auto-entrepreneurs are exempt from CFE -- they are NOT (except creation year and CA < EUR 5,000)
- NEVER confuse valeur locative cadastrale with actual rent paid -- they are different amounts
- NEVER forget that CFE must be checked ONLINE on impots.gouv.fr -- no paper notice is sent
- NEVER apply pro-rata for mid-year cessation -- CFE is due for the full year
- NEVER advise on zone-based exemptions without confirming eligibility conditions
- NEVER present CFE as the total local business tax -- CET = CFE + CVAE

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
