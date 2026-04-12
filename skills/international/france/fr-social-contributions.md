---
name: fr-social-contributions
description: >
  Use this skill whenever asked about French social contributions (cotisations sociales URSSAF) for self-employed individuals (travailleurs independants), including professions liberales and BNC taxpayers. Trigger on phrases like "cotisations URSSAF", "charges sociales independant", "CSG CRDS freelance France", "CIPAV retraite", "ACRE reduction", "social contributions France", "cotisations minimales", "prelevement URSSAF", "cotisations trimestrielles", or any question about French self-employed social security. Also trigger when classifying bank statement transactions showing URSSAF prelevements, CIPAV debits, or cotisations trimestrielles. ALWAYS read this skill before touching any French social contribution work.
version: 2.0
jurisdiction: FR
tax_year: 2025
category: international
depends_on:
  - social-contributions-workflow-base
---

# France Social Contributions (Cotisations URSSAF) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

| Field | Value |
|---|---|
| Country | France |
| Primary Legislation | Code de la Securite Sociale (CSS); LFSS 2025 |
| Supporting Legislation | CGI Art. 154 bis (deductibility); Decret n 2024-688 (assiette reform) |
| Tax Authority | URSSAF |
| PASS 2025 | EUR 47,100 |
| Maladie-maternite (IJ) | 0.50% up to 500% PASS |
| Maladie-maternite (main) | Progressive: 0% to 6.50% |
| Retraite de base (plafonnee, SSI) | 17.75% up to 1 PASS |
| Retraite de base (deplafonnee, SSI) | 0.60% on total |
| Retraite complementaire (SSI) | 7.00% (up to PASS) + 8.00% (PASS to 4 PASS) |
| Invalidite-deces | 1.30% up to 1 PASS |
| Allocations familiales | 0% to 3.10% (progressive) |
| CSG | 9.20% (6.80% deductible + 2.40% non-deductible) |
| CRDS | 0.50% (non-deductible) |
| Formation professionnelle | EUR 117.75 (0.25% of PASS) |
| Payment options | Monthly (5th or 20th) or quarterly (Feb, May, Aug, Nov) |
| Cotisations minimales (zero income) | ~EUR 1,212/year |
| Currency | EUR only |
| Contributor | Open Accountants |
| Validated by | Pending -- requires sign-off by a French expert-comptable |
| Validation date | Pending |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown activity type | STOP -- do not compute |
| Unknown BIC or BNC | Ask -- determines caisse affiliation |
| Unknown CIPAV vs SSI | Ask -- retraite complementaire rates differ |
| Unknown income | Apply cotisations minimales |
| Unknown ACRE eligibility | Do not apply ACRE without verification |
| Unknown CSG/CRDS base method | Use current pre-reform method; flag for reviewer if 2025 regularisation |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- activity type (profession liberale reglementee/non reglementee, artisan, commercant), caisse affiliation (CIPAV or SSI), and prior year net professional income.

**Recommended** -- bank statements showing URSSAF prelevements, CIPAV statements, avis de cotisation URSSAF, 2042 declaration.

**Ideal** -- complete 2042-C-PRO, URSSAF echeancier, CIPAV releve de situation, ACRE confirmation letter.

### Refusal catalogue

**R-FR-SC-1 -- Activity type unknown.** *Trigger:* activity type not provided. *Message:* "Activity type and caisse affiliation are mandatory. CIPAV and SSI have different retraite rates. Cannot proceed."

**R-FR-SC-2 -- Caisses professionelles other than CIPAV/SSI.** *Trigger:* client is avocats (CNBF), medecins (CARMF), paramedics (CARPIMKO), experts-comptables (CNPADC), etc. *Message:* "This skill covers CIPAV and SSI only. Other caisses professionelles have their own rate schedules. Escalate to the relevant caisse or expert-comptable."

**R-FR-SC-3 -- Micro-entrepreneur.** *Trigger:* client is under micro-entrepreneur regime. *Message:* "Micro-entrepreneurs pay a simplified percentage on turnover. This skill covers regime reel rates only. Do not use this rate table for micro-entrepreneurs."

**R-FR-SC-4 -- International social security.** *Trigger:* EU A1 or bilateral treaty question. *Message:* "EU social security coordination (Regulation EC 883/2004) requires specialist advice. Escalate."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to French social contributions.

### 3.1 URSSAF prelevements (monthly or quarterly)

| Pattern | Treatment | Notes |
|---|---|---|
| URSSAF | EXCLUDE -- cotisations sociales | Monthly or quarterly prelevement |
| URSSAF IDF, URSSAF PACA, URSSAF RHONE-ALPES | EXCLUDE -- cotisations | Regional URSSAF entities |
| COTISATIONS SOCIALES | EXCLUDE -- cotisations | Generic reference |
| PRELEVEMENT URSSAF | EXCLUDE -- cotisations | Direct debit description |
| ACOMPTE PROVISIONNEL URSSAF | EXCLUDE -- cotisations | Provisional instalment |
| REGULARISATION URSSAF | EXCLUDE -- cotisations | Year-end regularisation adjustment |

### 3.2 CIPAV debits (profession liberale reglementee)

| Pattern | Treatment | Notes |
|---|---|---|
| CIPAV | EXCLUDE -- retraite complementaire | CIPAV pension contribution |
| CAISSE INTERPROFESSIONNELLE DE PREVOYANCE | EXCLUDE -- CIPAV | Full name |

### 3.3 Other caisses (escalate -- do not classify)

| Pattern | Treatment | Notes |
|---|---|---|
| CNBF | ESCALATE -- avocats caisse | Out of scope |
| CARMF | ESCALATE -- medecins caisse | Out of scope |
| CARPIMKO | ESCALATE -- paramedics caisse | Out of scope |
| CNPADC | ESCALATE -- experts-comptables | Out of scope |
| IRCEC | ESCALATE -- artistes-auteurs complementaire | Out of scope |

### 3.4 CSG/CRDS (collected via URSSAF)

| Pattern | Treatment | Notes |
|---|---|---|
| CSG, CRDS | EXCLUDE -- social levies | Typically included in URSSAF prelevement, not separate |

### 3.5 Formation professionnelle (CFP)

| Pattern | Treatment | Notes |
|---|---|---|
| CFP, CONTRIBUTION FORMATION | EXCLUDE -- training levy | EUR 117.75 annually, may be separate debit or included in URSSAF |

### 3.6 Tax authority (NOT social contributions)

| Pattern | Treatment | Notes |
|---|---|---|
| DGFIP, DIRECTION GENERALE DES FINANCES | EXCLUDE -- income tax | Not cotisations sociales |
| IMPOT, IMPOTS.GOUV | EXCLUDE -- income tax | Not cotisations |
| TVA, TAXE SUR LA VALEUR AJOUTEE | EXCLUDE -- VAT | Not cotisations |
| PRELEVEMENT A LA SOURCE | EXCLUDE -- income tax withholding | Not cotisations |

---

## Section 4 -- Worked examples

Six bank statement classifications for a hypothetical French self-employed IT consultant (PLNR/SSI, regime reel).

### Example 1 -- Monthly URSSAF prelevement

**Input line:**
`05.04.2025 ; URSSAF ILE DE FRANCE ; PRELEVEMENT ; COTISATIONS AVRIL 2025 ; -1,108.00 ; EUR`

**Reasoning:**
Matches "URSSAF" (pattern 3.1). Monthly prelevement on the 5th. This is the provisional acompte based on the most recently declared income. Covers maladie, retraite de base, invalidite-deces, allocations familiales, CSG/CRDS combined. Exclude from VAT.

**Classification:** EXCLUDE -- cotisations sociales (URSSAF prelevement). Deductible per CGI Art. 154 bis (mandatory cotisations fully deductible; CSG 6.80% deductible, 2.40% non-deductible; CRDS non-deductible).

### Example 2 -- Quarterly URSSAF payment

**Input line:**
`05.05.2025 ; URSSAF ; PRELEVEMENT ; ACOMPTE TRIMESTRIEL Q2 ; -3,324.00 ; EUR`

**Reasoning:**
Matches "URSSAF" (pattern 3.1). Quarterly payment (client opted for quarterly schedule -- 5 Feb, 5 May, 5 Aug, 5 Nov). Amount = approximately 3x monthly acompte.

**Classification:** EXCLUDE -- quarterly cotisations sociales.

### Example 3 -- URSSAF regularisation (adjustment)

**Input line:**
`20.09.2025 ; URSSAF RHONE-ALPES ; PRELEVEMENT ; REGULARISATION 2024 ; -1,850.00 ; EUR`

**Reasoning:**
Matches "URSSAF" + "REGULARISATION" (pattern 3.1). After the client declared actual 2024 income on the 2042 declaration, URSSAF recalculated and found an underpayment. This is the regularisation adjustment. Deductible in the year paid.

**Classification:** EXCLUDE -- cotisations regularisation. Deductible in 2025 (year paid, not 2024).

### Example 4 -- CIPAV retraite complementaire

**Input line:**
`15.06.2025 ; CIPAV ; PRELEVEMENT ; COTISATION RETRAITE S1 ; -4,239.00 ; EUR`

**Reasoning:**
Matches "CIPAV" (pattern 3.2). This is the first-semester CIPAV retraite complementaire payment for a profession liberale reglementee (e.g., architect, consultant). Amount EUR 4,239 = EUR 47,100 x 9% (tranche 1 rate for CIPAV 2025).

**Classification:** EXCLUDE -- CIPAV pension contribution. Fully deductible from professional income.

### Example 5 -- DGFIP income tax (NOT cotisations)

**Input line:**
`15.04.2025 ; DGFIP ; PRELEVEMENT ; PRELEVEMENT A LA SOURCE ; -1,200.00 ; EUR`

**Reasoning:**
Matches "DGFIP" (pattern 3.6). This is the monthly income tax withholding (prelevement a la source), NOT a social contribution. Do not classify as cotisations sociales.

**Classification:** EXCLUDE -- income tax. NOT cotisations sociales.

### Example 6 -- First-year forfait provisoire with ACRE

**Input line:**
`05.03.2025 ; URSSAF ; PRELEVEMENT ; COTISATIONS MARS 2025 ACRE ; -146.00 ; EUR`

**Reasoning:**
Matches "URSSAF" + "ACRE" (pattern 3.1). First-year self-employed with ACRE exoneration. Provisional base is 19% PASS. ACRE reduces cotisations (maladie, retraite base, invalidite, AF) by 50%. Amount EUR 146/month is approximately half of the normal first-year acompte. CSG/CRDS and formation professionnelle are NOT reduced by ACRE.

**Classification:** EXCLUDE -- ACRE-reduced cotisations. Deductible (the actual amount paid, not the pre-ACRE amount).

---

## Section 5 -- Tier 1 rules

### Rule 1 -- Cotisation rate table (SSI: artisans, commercants, PLNR)

| Cotisation | Rate | Base / Plafond |
|---|---|---|
| Maladie-maternite (IJ) | 0.50% | Up to 500% PASS (EUR 235,500) |
| Maladie-maternite (main) | Progressive: 0%-6.50% | See progressive scale below |
| Retraite de base (plafonnee) | 17.75% | Up to 1 PASS (EUR 47,100) |
| Retraite de base (deplafonnee) | 0.60% | Total income |
| Retraite complementaire (RCI T1) | 7.00% | Up to 1 PASS |
| Retraite complementaire (RCI T2) | 8.00% | 1 PASS to 4 PASS |
| Invalidite-deces | 1.30% | Up to 1 PASS |
| Allocations familiales | 0% to 3.10% | Progressive |
| CSG | 9.20% | Income + mandatory cotisations |
| CRDS | 0.50% | Income + mandatory cotisations |
| Formation professionnelle | EUR 117.75 | Fixed (0.25% of PASS) |

### Rule 2 -- Maladie-maternite progressive scale

| Income Level | Rate |
|---|---|
| <= 40% PASS (EUR 18,840) | 0% |
| 40% to 60% PASS (EUR 28,260) | Progressive 0% to 4.00% |
| 60% to 110% PASS (EUR 51,810) | Progressive 4.00% to 6.50% |
| Above 110% PASS | 6.50% flat |

### Rule 3 -- Allocations familiales progressive scale

| Income Level | Rate |
|---|---|
| <= 110% PASS (EUR 51,810) | 0% |
| 110% to 140% PASS (EUR 65,940) | Progressive 0% to 3.10% |
| Above 140% PASS | 3.10% flat |

### Rule 4 -- CIPAV rates (professions liberales reglementees)

| Cotisation | Rate | Base |
|---|---|---|
| Retraite de base CNAVPL | 8.23% up to 1 PASS + 1.87% total |
| Retraite complementaire CIPAV T1 | 9.00% up to 1 PASS |
| Retraite complementaire CIPAV T2 | 22.00% above 1 PASS |

Other cotisations (maladie, AF, CSG/CRDS) same as SSI.

### Rule 5 -- CSG/CRDS base

```
CSG/CRDS base = Net professional income + mandatory cotisations obligatoires
```

CSG: 6.80% deductible, 2.40% non-deductible. CRDS: non-deductible.

### Rule 6 -- Cotisations minimales (zero or very low income)

| Cotisation | Min Base | Approx. Min Amount (2025) |
|---|---|---|
| Maladie (IJ) | 40% PASS | EUR 94 |
| Retraite de base | 450 x SMIC horaire | EUR 930 |
| Invalidite-deces | 11.50% PASS | EUR 70 |
| Formation professionnelle | 1 PASS | EUR 118 |

Total minimum approximately EUR 1,212/year. No minimum for: AF, CSG/CRDS, retraite complementaire.

### Rule 7 -- ACRE (first year, 2025 activities)

50% reduction on maladie, retraite de base, invalidite-deces, and AF for first 4 quarters. NOT reduced: CSG, CRDS, formation professionnelle, retraite complementaire. Income ceiling: exoneration applies on income up to 1 PASS only.

### Rule 8 -- Payment schedule

Monthly: 12 debits on the 5th or 20th. Quarterly: 4 payments on 5 Feb, 5 May, 5 Aug, 5 Nov. Regularisation after annual declaration on impots.gouv.fr (ex-DSI, integrated into 2042).

### Rule 9 -- First two years (forfait provisoire)

Year 1 (without ACRE): provisional base 19% PASS (EUR 8,949), approximately EUR 3,500 total. Year 1 (with ACRE): approximately EUR 1,750. Regularised retroactively.

### Rule 10 -- Tax deductibility

Mandatory cotisations: fully deductible from professional income. CSG: 6.80% deductible, 2.40% non-deductible. CRDS: non-deductible. Deducted on 2042-C-PRO.

---

## Section 6 -- Tier 2 catalogue

### T2-1 -- ACRE eligibility

**Trigger:** Client claims ACRE exoneration.
**Issue:** Eligibility conditions must be verified case by case. Not automatic for all creators (post-2026 rules tightened).
**Action:** Flag for reviewer. Verify with URSSAF.

### T2-2 -- CIPAV to SSI transfer

**Trigger:** Client was CIPAV-affiliated but profession transferred to SSI under 2018 reform.
**Issue:** Depends on registration date and opt-out exercise.
**Action:** Escalate to expert-comptable.

### T2-3 -- Dual salarie + independant

**Trigger:** Client is both salaried and self-employed.
**Issue:** Both sets of cotisations apply. Retraite de base may be capped at 1 PASS across regimes.
**Action:** Flag for reviewer to verify retraite base cap interaction.

### T2-4 -- 2025 assiette reform (new unified base)

**Trigger:** Computing regularisation of 2025 cotisations (processed in 2026).
**Issue:** New unified base with 26% flat abatement replaces prior system of deducting actual cotisations from CSG/CRDS base.
**Action:** Flag for reviewer. Verify which base applies.

### T2-5 -- Late registration (activite non declaree)

**Trigger:** Client has been working independently without URSSAF registration.
**Issue:** URSSAF can claim cotisations retroactively with penalties.
**Action:** Escalate to expert-comptable immediately.

### T2-6 -- First year income exceeds PASS (ACRE)

**Trigger:** ACRE client earns above EUR 47,100 in first year.
**Issue:** ACRE 50% reduction only applies on income up to 1 PASS. Income above PASS subject to full cotisations.
**Action:** Flag for reviewer. Compute the split.

---

## Section 7 -- Excel working paper template

```
FRANCE COTISATIONS SOCIALES -- WORKING PAPER
Client: [name]
Tax Year: [year]
Prepared: [date]

INPUT DATA
  Activity type:                 [PLNR-SSI / PL reglementee-CIPAV / artisan / commercant]
  Caisse affiliation:            [SSI / CIPAV]
  Prior year net income:         EUR [____]
  First/second year:             [YES/NO]
  ACRE eligible:                 [YES/NO/UNKNOWN]
  Dual salarie + independant:    [YES/NO]

COTISATION COMPUTATION (SSI)
  Maladie IJ (0.50%):            EUR [____]
  Maladie main (progressive):    EUR [____]
  Retraite base plafonnee:       EUR [____]
  Retraite base deplafonnee:     EUR [____]
  Retraite complementaire T1:    EUR [____]
  Retraite complementaire T2:    EUR [____]
  Invalidite-deces:              EUR [____]
  Allocations familiales:        EUR [____]
  Formation professionnelle:     EUR 117.75
  Subtotal (excl. CSG/CRDS):     EUR [____]

  CSG base (income + cotisations): EUR [____]
  CSG (9.20%):                    EUR [____]
  CRDS (0.50%):                   EUR [____]

TOTAL COTISATIONS:                EUR [____]

TAX DEDUCTIBILITY
  Mandatory cotisations:         EUR [____] (fully deductible)
  CSG deductible (6.80%):        EUR [____]
  CSG non-deductible (2.40%):    EUR [____]
  CRDS (non-deductible):         EUR [____]

REVIEWER FLAGS
  [List any Tier 2 flags]
```

---

## Section 8 -- Bank statement reading guide

### How French social contribution debits appear

**URSSAF prelevements:**
- Description: "URSSAF" or "URSSAF [REGION]" + "PRELEVEMENT" or "COTISATIONS"
- Timing: 5th or 20th of each month (monthly) or 5 Feb/May/Aug/Nov (quarterly)
- Amount: Consistent monthly amount until regularisation adjusts remaining instalments
- Regularisation debits appear mid-year with "REGULARISATION" reference

**CIPAV debits:**
- Description: "CIPAV" or "CAISSE INTERPROFESSIONNELLE"
- Timing: Semi-annual or quarterly (varies)
- Amount: Based on declared income and CIPAV class

**Key identification tips:**
1. URSSAF debits are the most common -- monthly or quarterly on fixed dates
2. Regularisation debits can be large if income estimate was significantly wrong
3. CIPAV debits are separate from URSSAF (for profession liberale reglementee)
4. DGFIP debits are TAX (prelevement a la source), not cotisations
5. First-year amounts are low (forfait provisoire) -- expect large regularisation later

---

## Section 9 -- Onboarding fallback

If the client provides only a bank statement:

1. **Scan for URSSAF debits** -- identify monthly/quarterly prelevements and regularisations
2. **Scan for CIPAV debits** -- if present, client is profession liberale reglementee
3. **Sum annual cotisations paid** -- total URSSAF + CIPAV debits
4. **Identify regularisation adjustments** -- large mid-year debits or credits from URSSAF
5. **Flag:** "Cotisation classification derived from bank statement patterns. Actual caisse affiliation, ACRE status, and income base have not been independently verified. Reviewer must confirm before completing 2042-C-PRO."

---

## Section 10 -- Reference material

### Key reference values (2025)

| Reference | Value |
|---|---|
| PASS | EUR 47,100 |
| 110% PASS | EUR 51,810 |
| 140% PASS | EUR 65,940 |
| 500% PASS | EUR 235,500 |

### Test suite

**Test 1:** PLNR (SSI), income EUR 40,000, not first year. -> Maladie IJ: EUR 200. Maladie main: ~EUR 2,320. Retraite base plafonnee: EUR 7,100. Retraite base deplafonnee: EUR 240. RCI T1: EUR 2,800. Invalidite-deces: EUR 520. AF: 0%. CFP: EUR 118. Approx total excl CSG/CRDS: EUR 13,298.

**Test 2:** Commercant (SSI), income EUR 80,000. -> Retraite base: EUR 8,360 + EUR 480. RCI: EUR 3,297 + EUR 2,632. Maladie: EUR 5,200 + EUR 400. AF: EUR 2,480 (>140% PASS). Invalidite: EUR 612.

**Test 3:** Zero income, not first year. -> Minimales: ~EUR 1,212.

**Test 4:** First year with ACRE, forfait provisoire. -> Approximately EUR 1,750.

**Test 5:** Architect (CIPAV), income EUR 55,000. -> CNAVPL: EUR 4,905. CIPAV T1: EUR 4,239. CIPAV T2: EUR 1,738.

**Test 6:** Dual salarie + independant, EUR 15,000 BNC freelance. -> Full cotisations on EUR 15,000.

**Test 7:** AF progressive zone, income EUR 60,000. -> ~1.80% effective, ~EUR 1,080.

### Prohibitions

- NEVER compute without knowing activity type and caisse
- NEVER assume CIPAV rates for non-CIPAV professions
- NEVER ignore cotisations minimales
- NEVER apply ACRE without verifying eligibility
- NEVER tell client CSG/CRDS is fully deductible
- NEVER conflate 2025 rates with reformed rates
- NEVER advise on caisses other than CIPAV/SSI
- NEVER compute for micro-entrepreneurs using this rate table
- NEVER estimate penalties without escalating
- NEVER advise on international social security coordination

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
