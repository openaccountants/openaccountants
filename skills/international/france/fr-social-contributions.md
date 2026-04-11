---
name: fr-social-contributions
description: >
  Use this skill whenever asked about French social contributions (cotisations sociales URSSAF) for self-employed individuals (travailleurs independants), including professions liberales and BNC taxpayers. Trigger on phrases like "cotisations URSSAF", "charges sociales independant", "CSG CRDS freelance France", "CIPAV retraite", "ACRE reduction", "social contributions France", "cotisations minimales", "how much social security in France", or any question about French self-employed social security obligations. Covers maladie-maternite, retraite de base, retraite complementaire (CIPAV), invalidite-deces, allocations familiales, CSG/CRDS, formation professionnelle, ACRE, cotisations minimales, payment schedule, and the unified declaration (ex-DSI). ALWAYS read this skill before touching any French social contribution work.
version: 1.0
jurisdiction: FR
tax_year: 2025
category: international
depends_on:
  - social-contributions-workflow-base
---

# France Social Contributions (Cotisations URSSAF) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | France |
| Jurisdiction Code | FR |
| Primary Legislation | Code de la Securite Sociale (CSS); Loi de financement de la Securite Sociale (LFSS) 2025 |
| Supporting Legislation | Code General des Impots (CGI) Art. 154 bis (deductibility); Decret n 2024-688 du 5 juillet 2024 (assiette reform) |
| Tax Authority | URSSAF (Union de Recouvrement des cotisations de Securite Sociale et d'Allocations Familiales) |
| Rate Publisher | URSSAF (publishes annual rate tables at urssaf.fr) |
| Contributor | Open Accountants |
| Validated By | Pending -- requires sign-off by a French expert-comptable |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate calculation, PASS thresholds, CSG/CRDS, payment schedule. Tier 2: CIPAV class selection, ACRE eligibility, progressive maladie rate computation. Tier 3: caisses professionelles hors CIPAV, disability exemptions, international social security treaties. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified expert-comptable must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any cotisation figure, you MUST know:

1. **Activity type** [T1] -- profession liberale reglementee (CIPAV), profession liberale non reglementee, artisan, or commercant
2. **BIC or BNC** [T1] -- determines which caisse and which rate table applies
3. **Prior year net professional income (benefice)** [T1] -- cotisations are based on prior year income (N-2 for acomptes, regularised on N-1 after declaration)
4. **Is this the first or second year of activity?** [T1] -- forfait provisoire applies
5. **ACRE eligibility** [T2] -- is the client in the first year with ACRE exoneration?
6. **CIPAV or SSI affiliation** [T1] -- determines retraite complementaire regime
7. **Other social coverage** [T1] -- dual activity with employment (salarie)?

**If activity type is unknown, STOP. Do not compute cotisations.**

---

## Step 1: Key Reference Values -- PASS 2025 [T1]

**Source:** Arrete du 19 decembre 2024 (Legifrance JORFTEXT000050854392)

| Reference | 2025 Value |
|-----------|------------|
| PASS (Plafond Annuel de la Securite Sociale) | EUR 47,100 |
| PMSS (Plafond Mensuel) | EUR 3,925 |
| PASS trimestriel | EUR 11,775 |
| 110% PASS | EUR 51,810 |
| 140% PASS | EUR 65,940 |
| 500% PASS | EUR 235,500 |

---

## Step 2: Cotisation Rate Table -- Artisans, Commercants, and Professions Liberales Non Reglementees (SSI) [T1]

**Legislation:** CSS Art. L.612-1 et seq.; URSSAF rate table 2025

**Assiette (base):** Net professional income (revenu d'activite non salariee) = gross revenue minus allowable business expenses, before social contributions deduction.

| Cotisation | Rate | Base / Plafond | Notes |
|------------|------|----------------|-------|
| Maladie-maternite 1 (indemnites journalieres) | 0.50% | Up to 500% PASS (EUR 235,500) | Flat rate |
| Maladie-maternite 2 | Progressive: 0% to 6.50% | On total income | 0% if income <= 40% PASS; progressive up to 6.50% at 110% PASS; 6.50% flat above 110% PASS |
| Retraite de base (plafonnee) | 17.75% | Up to 1 PASS (EUR 47,100) | CNAV |
| Retraite de base (deplafonnee) | 0.60% | On total income | No ceiling |
| Retraite complementaire (RCI) | 7.00% | Up to 1 PASS (EUR 47,100) | For artisans/commercants/PLNR |
| Retraite complementaire (RCI) | 8.00% | Income between 1 PASS and 4 PASS | EUR 47,100 to EUR 188,400 |
| Invalidite-deces | 1.30% | Up to 1 PASS (EUR 47,100) | |
| Allocations familiales | 0% | Income <= 110% PASS (EUR 51,810) | |
| Allocations familiales | Progressive: 0% to 3.10% | Income between 110% and 140% PASS | Linear interpolation |
| Allocations familiales | 3.10% | Income > 140% PASS (EUR 65,940) | |
| CSG | 9.20% | 100% of declared income + cotisations sociales obligatoires | 6.80% deductible + 2.40% non-deductible |
| CRDS | 0.50% | 100% of declared income + cotisations sociales obligatoires | Non-deductible |
| Formation professionnelle (CFP) | 0.25% | On 1 PASS (EUR 47,100) | Fixed annual amount = EUR 117.75 in 2025 |

### Maladie-Maternite Progressive Rate Detail [T1]

The maladie-maternite contribution (excluding indemnites journalieres) follows a progressive scale:

| Income Level | Rate |
|-------------|------|
| <= 40% PASS (EUR 18,840) | 0% |
| Between 40% PASS and 60% PASS (EUR 28,260) | Progressive from 0% to 4.00% |
| Between 60% PASS and 110% PASS (EUR 51,810) | Progressive from 4.00% to 6.50% |
| Above 110% PASS | 6.50% (flat) |

---

## Step 3: Cotisation Rate Table -- Professions Liberales Reglementees (CIPAV) [T1]

**Legislation:** CSS; CIPAV statutes; URSSAF rate table 2025

For professions liberales reglementees affiliated with CIPAV (architects, consultants, engineers, psychologists, etc.), the following rates differ from SSI:

| Cotisation | Rate | Base / Plafond | Notes |
|------------|------|----------------|-------|
| Maladie-maternite | Same progressive scale as Step 2 | Same | |
| Retraite de base (CNAVPL) | 8.23% | Up to 1 PASS (EUR 47,100) | Lower than SSI rate |
| Retraite de base (CNAVPL) | 1.87% | On total income | Deplafonnee |
| Retraite complementaire CIPAV tranche 1 | 9.00% | Up to 1 PASS | Was 9%, moves to 11% under reform for regularisation 2025+ |
| Retraite complementaire CIPAV tranche 2 | 22.00% | Above 1 PASS | Was 22%, moves to 21% under reform |
| Invalidite-deces CIPAV | 1.30% | Up to 1 PASS (EUR 47,100) | |
| Allocations familiales | Same as Step 2 | Same | |
| CSG | 9.20% | Same as Step 2 | |
| CRDS | 0.50% | Same as Step 2 | |
| Formation professionnelle | 0.25% | On 1 PASS | EUR 117.75 |

**Important:** Other caisses professionelles (CNBF for avocats, CARPIMKO for paramedics, CARMF for medecins, CNPADC for experts-comptables, etc.) have their OWN rate schedules. These are [T3] -- escalate to the relevant caisse or qualified expert-comptable.

---

## Step 4: CSG/CRDS Computation Detail [T1]

**Legislation:** CSS Art. L.136-1 et seq.; CGI Art. 154 bis

### Base de calcul (computation base)

```
CSG/CRDS base = Net professional income + mandatory social contributions (cotisations obligatoires)
```

The CSG/CRDS base includes the cotisations themselves in the base (circular reference resolved by URSSAF in their calculation engine).

| Component | Rate | Deductible from IRPF? |
|-----------|------|-----------------------|
| CSG | 9.20% | 6.80% deductible; 2.40% non-deductible |
| CRDS | 0.50% | Non-deductible |
| **Total CSG + CRDS** | **9.70%** | Partially |

### 2025 Assiette Reform Note

Starting with the regularisation of 2025 cotisations (processed in 2026), a new unified base applies: gross income reduced by a 26% flat abatement (minimum floor = 1.76% PASS = EUR 828.96). This replaces the prior system of deducting actual cotisations from the CSG/CRDS base. The new system simplifies computation but changes effective amounts. [T2] -- verify which base applies to the specific computation period.

---

## Step 5: Cotisations Minimales (Minimum Contributions) [T1]

**Legislation:** CSS Art. D.612-5 et seq.

Even with zero or very low income, minimum contributions apply:

| Cotisation | Minimum Base | Approximate Minimum Amount (2025) |
|------------|-------------|----------------------------------|
| Maladie (indemnites journalieres) | 40% PASS (EUR 18,840) | EUR 94 |
| Retraite de base | 450 x SMIC horaire (EUR 5,243) | EUR 930 |
| Invalidite-deces | 11.50% PASS (EUR 5,417) | EUR 70 |
| Formation professionnelle | 1 PASS (EUR 47,100) | EUR 118 |

**No minimum applies for:** allocations familiales, CSG/CRDS, retraite complementaire -- these are proportional to actual income (zero income = zero contribution).

**Total approximate minimum (2025):** approximately EUR 1,212 per year for a zero-income independent.

---

## Step 6: ACRE -- Aide a la Creation ou Reprise d'Entreprise [T2]

**Legislation:** CSS Art. L.131-6-4; Decret 2019-1215

### 2025 Rules (activities started in 2025)

| Parameter | Value |
|-----------|-------|
| Exoneration rate | 50% reduction on cotisations (maladie, retraite de base, invalidite-deces, allocations familiales) |
| Duration | First 4 quarters of activity (approximately 12 months) |
| Income ceiling | Exoneration applies on income up to 1 PASS (EUR 47,100); no exoneration on income above PASS |
| Excluded contributions | CSG, CRDS, formation professionnelle, and retraite complementaire are NOT reduced by ACRE |
| Eligibility | Automatic for first-time creators; must not have benefited from ACRE in the prior 3 years |

### 2026 Changes (activities started from 1 January 2026)

| Parameter | Value |
|-----------|-------|
| Exoneration rate | Reduced to 25% (from 50%) for micro-entrepreneurs starting from 1 July 2026 |
| Application | Mandatory request to URSSAF within 60 days of activity start date |
| Eligibility | Restricted to specific categories (unemployed registered 6+ months in last 18 months, etc.) |

**ACRE is [T2] because eligibility conditions must be verified case by case.**

---

## Step 7: Payment Schedule [T1]

**Legislation:** CSS Art. R.131-1 et seq.

### Acomptes provisionnels

Cotisations are paid via provisional instalments (acomptes) based on the most recently declared income, then regularised after the annual income declaration.

| Payment Option | Schedule |
|---------------|----------|
| Monthly | 12 monthly direct debits (prelevement automatique), typically on the 5th or 20th of each month |
| Quarterly | 4 quarterly payments: 5 Feb, 5 May, 5 Aug, 5 Nov |

### Regularisation

After the annual income declaration (ex-DSI, now integrated into the 2042 declaration on impots.gouv.fr), URSSAF recalculates cotisations based on actual income and adjusts the remaining instalments of the year.

### First Two Years (forfait provisoire)

| Year | Provisional Base | Approximate Total Cotisations |
|------|-----------------|------------------------------|
| Year 1 (without ACRE) | 19% PASS (EUR 8,949) | Approximately EUR 3,500 |
| Year 1 (with ACRE) | 19% PASS but 50% reduction | Approximately EUR 1,750 |
| Year 2 | 19% PASS (adjusted if Year 1 income declared) | Approximately EUR 3,500 |

**Regularisation of Year 1 and Year 2 happens retroactively once actual income is declared.**

---

## Step 8: Annual Declaration (ex-DSI) [T1]

**Legislation:** Decret n 2021-686 du 28 mai 2021; CSS Art. L.613-2

### Current Procedure (2025)

The standalone DSI (Declaration Sociale des Independants) was abolished in 2021. It is now replaced by a unified social and fiscal declaration integrated into the personal income tax return (declaration 2042) on impots.gouv.fr.

| Parameter | Detail |
|-----------|--------|
| Where | impots.gouv.fr -- volet social integrated into declaration 2042 |
| When | Same deadline as personal income tax: varies by departement (late May to early June 2025) |
| What is declared | Net professional income (BNC/BIC) used by URSSAF to compute cotisations |
| Consequence of non-filing | URSSAF applies a taxe d'office (forfait) at a punitive rate |

**Departement-based deadlines (2025):**
- Departements 01-19: 22 May 2025
- Departements 20-54: 28 May 2025
- Departements 55-976: 5 June 2025

---

## Step 9: Interaction with Income Tax (IRPF) [T1]

**Legislation:** CGI Art. 154 bis

| Question | Answer |
|----------|--------|
| Are cotisations sociales deductible? | YES -- mandatory cotisations (retraite, maladie, invalidite, allocations familiales) are fully deductible from professional income (BNC/BIC) |
| Is CSG deductible? | Partially: 6.80% of CSG is deductible; 2.40% is not |
| Is CRDS deductible? | NO -- CRDS is never deductible |
| Where deducted? | From the net professional income (benefice imposable) on the 2042-C-PRO |

---

## Step 10: Penalties [T1]

**Legislation:** CSS Art. R.243-18 et seq.

| Penalty | Rate |
|---------|------|
| Late payment of cotisations | 5% surcharge on unpaid amount + 0.2% per month interest |
| Late or missing declaration | URSSAF applies a provisional calculation on a forfait base (typically higher than actual income) |
| Repeated non-declaration | URSSAF can apply a majoration of 10% to 40% |
| Fraud | Criminal penalties possible under CSS Art. L.114-18 |

---

## Step 11: Edge Case Registry

### EC1 -- Dual activity: salarie + independant [T1]
**Situation:** Client is both a salaried employee (paying cotisations salariales) and self-employed on the side.
**Resolution:** Both sets of cotisations apply. The salarie cotisations do NOT exempt from independant cotisations. However, retraite de base is capped at 1 PASS across all regimes. CSG/CRDS apply separately to each income type. [T2] flag for reviewer to verify retraite base cap interaction.

### EC2 -- Income below cotisations minimales threshold [T1]
**Situation:** Client declares zero or negative net income.
**Resolution:** Cotisations minimales apply (approximately EUR 1,212 in 2025). There is no zero-cotisation outcome once registered.

### EC3 -- First year with ACRE, income exceeds PASS [T2]
**Situation:** Client has ACRE in first year but earns EUR 80,000.
**Resolution:** ACRE 50% exoneration applies only on income up to 1 PASS (EUR 47,100). Income above PASS is subject to full cotisations. [T2] flag -- compute the split.

### EC4 -- Profession liberale changing from CIPAV to SSI [T2]
**Situation:** Client was affiliated with CIPAV but their profession was transferred to SSI under the 2018 reform.
**Resolution:** Depends on the date of registration and whether the client exercised the opt-out. Pre-2019 CIPAV affiliates could stay; post-2019 registrations in non-listed professions go to SSI. [T2] escalate.

### EC5 -- Micro-entrepreneur switching to regime reel [T1]
**Situation:** Client crosses micro-entrepreneur thresholds and moves to regime reel.
**Resolution:** Cotisations switch from the simplified micro percentage to the full rate table above. URSSAF recalculates from the date of regime change. Prior micro cotisations are not refunded.

### EC6 -- Late registration (activite non declaree) [T2]
**Situation:** Client has been working independently for 2 years without URSSAF registration.
**Resolution:** URSSAF can claim cotisations retroactively for the entire period of unreported activity. Penalties and majorations apply. [T2] escalate to expert-comptable immediately.

### EC7 -- Non-resident EU freelancer working in France [T3]
**Situation:** Client is resident in another EU country but performs services in France.
**Resolution:** Depends on EU social security coordination rules (Regulation EC 883/2004) and the A1 certificate. [T3] escalate -- do not advise.

---

## Step 12: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified expert-comptable must confirm before advising client.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified expert-comptable. Document gap.
```

---

## Step 13: Test Suite

### Test 1 -- Standard BNC profession liberale (PLNR/SSI), mid-range income
**Input:** Activity type: PLNR (SSI). Prior year net income: EUR 40,000. Not first year. No ACRE.
**Expected output:**
- Maladie-maternite (IJ): EUR 40,000 x 0.50% = EUR 200
- Maladie-maternite (main): approximately 5.80% effective (progressive) on EUR 40,000 = approximately EUR 2,320
- Retraite de base plafonnee: EUR 40,000 x 17.75% = EUR 7,100
- Retraite de base deplafonnee: EUR 40,000 x 0.60% = EUR 240
- Retraite complementaire T1: EUR 40,000 x 7.00% = EUR 2,800
- Invalidite-deces: EUR 40,000 x 1.30% = EUR 520
- Allocations familiales: 0% (income < 110% PASS)
- CSG: 9.20% on (income + cotisations)
- CRDS: 0.50% on (income + cotisations)
- Formation professionnelle: EUR 118
- **Approximate total cotisations (excluding CSG/CRDS): EUR 13,298**

### Test 2 -- High income, above PASS
**Input:** Activity type: commercant (SSI). Prior year net income: EUR 80,000. Not first year.
**Expected output:**
- Retraite de base plafonnee: EUR 47,100 x 17.75% = EUR 8,360
- Retraite de base deplafonnee: EUR 80,000 x 0.60% = EUR 480
- Retraite complementaire T1: EUR 47,100 x 7.00% = EUR 3,297
- Retraite complementaire T2: (EUR 80,000 - EUR 47,100) x 8.00% = EUR 2,632
- Maladie-maternite (main): EUR 80,000 x 6.50% = EUR 5,200 (flat, income > 110% PASS)
- Maladie-maternite (IJ): EUR 80,000 x 0.50% = EUR 400
- Invalidite-deces: EUR 47,100 x 1.30% = EUR 612
- Allocations familiales: EUR 80,000 x 3.10% = EUR 2,480 (income > 140% PASS)
- Formation professionnelle: EUR 118

### Test 3 -- Zero income, cotisations minimales
**Input:** Activity type: profession liberale (SSI). Net income: EUR 0. Not first year.
**Expected output:**
- Retraite de base minimum: approximately EUR 930
- Maladie (IJ) minimum: approximately EUR 94
- Invalidite-deces minimum: approximately EUR 70
- Formation professionnelle: EUR 118
- CSG/CRDS: EUR 0 (proportional to actual income)
- Allocations familiales: EUR 0
- **Approximate total: EUR 1,212**

### Test 4 -- First year with ACRE
**Input:** Activity type: PLNR (SSI). First year. ACRE confirmed. No income yet (forfait provisoire applies).
**Expected output:**
- Provisional base: 19% PASS = EUR 8,949
- ACRE reduces cotisations (maladie, retraite base, invalidite, AF) by 50%
- CSG/CRDS and formation professionnelle: NOT reduced by ACRE
- Approximate total: approximately EUR 1,750

### Test 5 -- CIPAV-affiliated profession liberale reglementee
**Input:** Activity type: architect (CIPAV). Prior year net income: EUR 55,000. Not first year.
**Expected output:**
- Retraite de base CNAVPL: EUR 47,100 x 8.23% + EUR 55,000 x 1.87% = EUR 3,876 + EUR 1,029 = EUR 4,905
- Retraite complementaire CIPAV T1: EUR 47,100 x 9.00% = EUR 4,239
- Retraite complementaire CIPAV T2: (EUR 55,000 - EUR 47,100) x 22.00% = EUR 1,738
- Other cotisations: same progressive maladie, AF, CSG/CRDS as SSI

### Test 6 -- Dual salarie + independant
**Input:** Client is full-time salarie (Class 1 cotisations paid by employer). Also earns EUR 15,000 BNC freelance.
**Expected output:** Full independant cotisations due on the EUR 15,000 freelance income. Salarie cotisations do NOT exempt from independant obligations. Cotisations minimales may apply if EUR 15,000 is below certain thresholds.

### Test 7 -- Allocations familiales progressive zone
**Input:** Activity type: commercant (SSI). Prior year net income: EUR 60,000.
**Expected output:** Income is between 110% PASS (EUR 51,810) and 140% PASS (EUR 65,940). Progressive AF rate applies: approximately 1.80% effective. AF = approximately EUR 1,080.

---

## PROHIBITIONS

- NEVER compute cotisations without knowing the activity type and caisse affiliation
- NEVER assume CIPAV rates for a non-CIPAV profession or vice versa
- NEVER ignore cotisations minimales -- even zero income triggers minimum contributions once registered
- NEVER apply ACRE without verifying eligibility conditions -- ACRE is not automatic for all creators (post-2026 rules)
- NEVER tell a client that CSG/CRDS is fully deductible -- only 6.80% of CSG is deductible; 2.40% CSG and 0.50% CRDS are not
- NEVER conflate the 2025 rates with the reformed rates (effective on 2025 regularisation in 2026) -- clarify which regime applies
- NEVER advise on caisses professionelles other than CIPAV/SSI (CNBF, CARMF, CARPIMKO, CNPADC, etc.) -- these are [T3]
- NEVER compute cotisations for micro-entrepreneurs using this rate table -- micro-entrepreneurs pay a simplified percentage on turnover
- NEVER estimate penalties or arrears without escalating to a qualified expert-comptable
- NEVER advise on international social security coordination (EU A1, bilateral treaties) -- this is [T3]

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
