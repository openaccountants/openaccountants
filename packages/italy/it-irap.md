---
name: it-irap
description: Use this skill whenever asked about Italian IRAP (Imposta Regionale sulle Attività Produttive) for self-employed professionals. Trigger on phrases like "IRAP", "imposta regionale", "IRAP professionista", "IRAP autonomo", "valore della produzione", "regional production tax Italy", or any question about IRAP obligations for a self-employed client in Italy. Covers the standard 3.9% rate, valore della produzione netta, regional variations, and the landmark exemption for autonomous professionals without autonomous organisation. ALWAYS read this skill before touching any Italy IRAP work.
---

# Italy IRAP (Imposta Regionale sulle Attività Produttive) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Italy |
| Jurisdiction Code | IT |
| Primary Legislation | D.Lgs. 15 dicembre 1997, n. 446 (IRAP decree) |
| Supporting Legislation | L. 190/2014 (Legge di Stabilità 2015); D.L. 73/2022 (IRAP reform); annual Legge di Bilancio |
| Tax Authority | Agenzia delle Entrate (national) + Regioni (regional) |
| Contributor | Open Accountants |
| Validated By | Pending -- requires validation by Italian commercialista |
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

1. **Activity type** [T1] -- lavoratore autonomo (professional), impresa individuale (sole proprietor), or società?
2. **Autonomous organisation (autonoma organizzazione)?** [T1] -- critical: professionals WITHOUT autonomous organisation may be EXEMPT
3. **Region of activity** [T1] -- rates vary by region
4. **Tax regime** [T1] -- regime forfettario? (exempt from IRAP)
5. **Use of employees or significant capital goods?** [T1] -- determines autonomous organisation
6. **Gross revenue and deductible IRAP costs** [T1]

**If activity type and autonomous organisation status are unknown, STOP. IRAP liability depends on these.**

---

## Step 1: Who Is Subject to IRAP? [T1]

**Legislation:** D.Lgs. 446/1997, art. 2-3

### Subject to IRAP

| Category | IRAP Applies? |
|----------|--------------|
| Imprese individuali (sole proprietors with a business) | YES -- always |
| Società (partnerships, corporations) | YES -- always |
| Lavoratori autonomi (professionals) WITH autonomous organisation | YES |
| Lavoratori autonomi WITHOUT autonomous organisation | **NO -- EXEMPT** |
| Regime forfettario taxpayers | **NO -- EXEMPT** |
| Contribuenti minimi | **NO -- EXEMPT** |

### The "Autonomous Organisation" Test (Autonoma Organizzazione) [T1/T2]

**Landmark: Corte di Cassazione, Sezioni Unite, sent. 9451/2016**

A professional (lavoratore autonomo) is subject to IRAP **only if** they have an "autonomous organisation" of production factors. The test:

| Indicator | Points Toward IRAP Liability |
|-----------|------------------------------|
| Employs staff (dipendenti or collaboratori) | YES -- strong indicator |
| Uses significant capital goods (beni strumentali) beyond minimal/personal tools | YES |
| Has a dedicated office/studio (not home-based) | Weak indicator alone |
| Works purely with personal skills, no employees, minimal equipment | NO -- likely exempt |

**[T2] -- The boundary is fact-specific. If there is any doubt, flag for reviewer. The Cassazione case law is extensive but not perfectly bright-line.**

---

## Step 2: Standard Rate [T1]

**Legislation:** D.Lgs. 446/1997, art. 16

| Standard Rate | 3.90% |
|---------------|-------|

Regions may increase or decrease the rate within statutory limits (typically +/- 0.92 percentage points):

### Regional Rate Variations (2025 -- Selected Regions)

| Region | Rate | Notes |
|--------|------|-------|
| Standard (most regions) | 3.90% | Default rate |
| Lombardia | 3.90% | Standard |
| Lazio | 3.90% | Standard (some sectors higher) |
| Campania | 4.82% | Often applies maximum surcharge |
| Calabria | 4.82% | Maximum surcharge |
| Sicilia | 3.90% | Standard |
| Trentino-Alto Adige | 2.98% | Reduced (autonomous region) |
| Friuli-Venezia Giulia | 2.98% | Reduced (autonomous region) |

**[T2] -- Regional rates change annually. Verify the specific region's current rate before computing.**

---

## Step 3: Tax Base (Valore della Produzione Netta) [T1]

**Legislation:** D.Lgs. 446/1997, art. 5-5bis

### For Imprese Individuali (Sole Proprietors -- Business)

```
valore_produzione_netta = ricavi (revenue)
                        + variazioni rimanenze (inventory changes)
                        + altri proventi (other operating income)
                        - costi della produzione (production costs)
                        + costo del lavoro (labour costs added back)
                        + interessi passivi (interest added back)
                        + compensi occasionali (occasional compensation added back)
```

**Key: IRAP base is NOT the same as income tax base. Labour costs, interest, and some other items are added back.**

### For Lavoratori Autonomi (Professionals)

```
valore_produzione_netta = compensi (fees/revenue)
                        - costi inerenti (deductible costs)
                        + costo del personale (employee costs added back)
```

### Simplified Computation for Small Businesses (Art. 5-bis)

Businesses that opt for simplified accounting (contabilità semplificata) can compute IRAP on the difference between revenue and costs as reported for income tax, with specific add-backs.

---

## Step 4: Computation Steps [T1]

### Step 4.1 -- Verify IRAP liability

```
IF regime_forfettario OR contribuente_minimo:
    IRAP = 0 (EXEMPT)
ELIF lavoratore_autonomo AND no_autonomous_organisation:
    IRAP = 0 (EXEMPT)
ELSE:
    proceed to calculation
```

### Step 4.2 -- Compute valore della produzione netta

```
# For sole proprietor (impresa):
vpn = revenue + inventory_changes + other_income
    - production_costs
    + labour_costs_addback
    + interest_addback

# For professional (autonomo with organisation):
vpn = fees - deductible_costs + employee_costs_addback
```

### Step 4.3 -- Apply deductions

```
# Deduction for employees (deduzione per dipendenti)
# Various cuneo fiscale deductions for permanent employees
vpn_adjusted = vpn - employee_deductions
```

### Step 4.4 -- Apply regional rate

```
IRAP = vpn_adjusted × regional_rate (typically 3.90%)
```

### Step 4.5 -- Deductions from IRAP itself

A portion of IRAP attributable to labour costs is deductible from IRPEF/IRES:
- 10% of IRAP paid is deductible from income tax base (as per D.L. 201/2011)
- Additional deduction for IRAP on employee costs

---

## Step 5: Payment Schedule [T1]

**Legislation:** D.Lgs. 446/1997, art. 30-31

| Payment | Deadline |
|---------|----------|
| Saldo (balance for prior year) + 1st acconto (advance for current year) | **30 June** (or 31 July with 0.40% surcharge) |
| 2nd acconto (second advance for current year) | **30 November** |

### Advance Payment (Acconti)

| Method | Amount |
|--------|--------|
| Historical method (metodo storico) | 100% of prior-year IRAP, split 40% (1st) / 60% (2nd) |
| Forecast method (metodo previsionale) | Based on estimated current-year IRAP |

```
1st_acconto = prior_year_IRAP × 40% (due 30 June)
2nd_acconto = prior_year_IRAP × 60% (due 30 November)
```

If prior-year IRAP <= EUR 51.65: no advance payments required.

---

## Step 6: IRAP Declaration [T1]

**Legislation:** D.Lgs. 446/1997, art. 19

| Obligation | Detail |
|------------|--------|
| Form | Dichiarazione IRAP (filed with income tax return) |
| Deadline | Same as Redditi PF/SP: **30 November** of the following year |
| Filing | Telematic (via Entratel or Fisconline) |

---

## Step 7: Tax Deductibility of IRAP [T1]

**Legislation:** D.L. 201/2011, art. 6

| Deduction | Amount |
|-----------|--------|
| IRAP on labour costs (cuneo fiscale) | Fully deductible from IRPEF base |
| IRAP on other components | 10% of total IRAP paid is deductible from IRPEF base |
| Regional tax deduction | Applied in the Redditi PF declaration |

---

## Step 8: Edge Case Registry

### EC1 -- Freelance professional, no employees, minimal equipment [T1]
**Situation:** Avvocato (lawyer) working alone from home with a laptop and phone.
**Resolution:** Likely NO autonomous organisation. IRAP exempt per Cassazione Sezioni Unite 9451/2016. Document the factual basis (no employees, no significant beni strumentali).

### EC2 -- Professional with one employee [T2]
**Situation:** Architect with one part-time employee (segretaria).
**Resolution:** Having even one employee generally constitutes autonomous organisation. IRAP likely applies. [T2] -- confirm with case law. Some case law allows an exception if the employee's role is merely administrative and marginal.

### EC3 -- Regime forfettario [T1]
**Situation:** Client is under regime forfettario (flat-rate tax regime).
**Resolution:** IRAP exempt. No declaration, no payment. Forfettario exclusion is clear and absolute.

### EC4 -- Sole proprietor with a shop [T1]
**Situation:** Impresa individuale operating a retail shop with two employees.
**Resolution:** IRAP applies. This is an impresa (business), not a profession. Autonomous organisation test is not relevant for imprese -- they are always subject.

### EC5 -- Multiple regions [T2]
**Situation:** Client has business activity in both Lombardia and Campania.
**Resolution:** IRAP must be apportioned between regions based on where value is produced (typically by employee/payroll location). Each region's rate applies to its portion. [T2] -- confirm apportionment methodology.

### EC6 -- IRAP and IRPEF interaction [T1]
**Situation:** Client asks if IRAP reduces income tax.
**Resolution:** 10% of IRAP paid is deductible from IRPEF taxable income. Additionally, the portion of IRAP on employee costs (cuneo fiscale deductions) is fully deductible from IRPEF base.

### EC7 -- First year of activity [T1]
**Situation:** New impresa individuale, started in April 2025.
**Resolution:** IRAP applies from the first year of activity (no first-year exemption like CFE in France). Advance payments based on forecast method (no prior year). First payment with saldo by 30 June 2026.

### EC8 -- Cessation mid-year [T1]
**Situation:** Client closes business in August 2025.
**Resolution:** IRAP applies on valore della produzione for the period of activity (Jan-Aug). Final declaration due by 30 November 2026. No advance payments for the following year.

### EC9 -- Contribuente minimo switching to ordinary [T2]
**Situation:** Client was contribuente minimo (exempt) and switches to ordinary regime.
**Resolution:** IRAP applies from the year of regime change. The autonomous organisation test applies if the client is a professional. [T2] -- assess organisation status.

---

## Step 9: Test Suite

### Test 1 -- Professional exempt (no autonomous organisation)
**Input:** Freelance consultant, works alone, home office, EUR 80,000 fees, EUR 15,000 costs.
**Expected output:** IRAP = EUR 0. Exempt -- no autonomous organisation.

### Test 2 -- Professional with organisation
**Input:** Dentist with 2 employees, studio rental, EUR 200,000 fees, EUR 60,000 deductible costs, EUR 40,000 employee costs.
**Expected output:** VPN = EUR 200,000 - EUR 60,000 + EUR 40,000 = EUR 180,000. Less employee deductions (assume EUR 15,000): EUR 165,000. IRAP = EUR 165,000 x 3.90% = EUR 6,435.

### Test 3 -- Sole proprietor (impresa), standard rate
**Input:** Retail business, revenue EUR 300,000, production costs EUR 200,000, labour EUR 50,000, interest EUR 5,000. Lombardia.
**Expected output:** VPN = EUR 300,000 - EUR 200,000 + EUR 50,000 + EUR 5,000 = EUR 155,000. Less employee deductions (assume EUR 20,000): EUR 135,000. IRAP = EUR 135,000 x 3.90% = EUR 5,265.

### Test 4 -- Regime forfettario
**Input:** Auto-entrepreneur equivalent, regime forfettario, EUR 50,000 revenue.
**Expected output:** IRAP = EUR 0 (exempt).

### Test 5 -- High-rate region (Campania)
**Input:** Professional with organisation in Campania, VPN EUR 100,000.
**Expected output:** IRAP = EUR 100,000 x 4.82% = EUR 4,820.

### Test 6 -- Advance payments
**Input:** Prior-year IRAP = EUR 8,000.
**Expected output:** 1st acconto (30 June) = EUR 8,000 x 40% = EUR 3,200. 2nd acconto (30 November) = EUR 8,000 x 60% = EUR 4,800.

### Test 7 -- Low IRAP, no advances
**Input:** Prior-year IRAP = EUR 40.
**Expected output:** Below EUR 51.65 threshold. No advance payments required. Only saldo due.

---

## PROHIBITIONS

- NEVER apply IRAP to regime forfettario taxpayers -- they are exempt
- NEVER assume all professionals owe IRAP -- the autonomous organisation test must be applied
- NEVER use the income tax base as the IRAP base -- they are different (labour costs and interest are added back for IRAP)
- NEVER apply the standard 3.90% rate without checking the specific region -- rates vary
- NEVER forget the 10% IRAP deduction from IRPEF -- it materially reduces income tax
- NEVER determine autonomous organisation status without examining the factual circumstances (employees, beni strumentali)
- NEVER present IRAP advance payments as optional -- they are mandatory if prior-year IRAP exceeds EUR 51.65
- NEVER ignore the employee cost add-back -- it is a fundamental difference from income tax computation
- NEVER advise on multi-region apportionment without flagging for reviewer

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
