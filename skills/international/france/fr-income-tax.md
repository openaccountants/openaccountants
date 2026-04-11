---
name: fr-income-tax
description: >
  Use this skill whenever asked about French income tax for self-employed individuals (professions liberales, BNC). Trigger on phrases like "declaration de revenus", "2042", "2042-C-PRO", "BNC", "benefices non commerciaux", "quotient familial", "prelevement a la source", "impot sur le revenu France", "micro-BNC", "regime reel", "charges deductibles", "CSG deductible", "decote", "CEHR", or any question about filing or computing income tax for a French freelancer or profession liberale. Also trigger when preparing or reviewing a 2042/2042-C-PRO return, computing deductible charges, or advising on the micro-BNC vs regime reel decision. This skill covers progressive brackets, quotient familial, BNC micro vs reel, prelevement a la source, charges deductibles, reductions/credits d'impot, CEHR, decote, and penalties. ALWAYS read this skill before touching any French income tax work.
version: 1.0
jurisdiction: FR
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# France Income Tax -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | France |
| Jurisdiction Code | FR |
| Primary Legislation | Code General des Impots (CGI), Articles 1 A, 12, 13, 34, 92, 93, 197, 200, 199 quater B, 1417 |
| Supporting Legislation | CGI Art. 102 ter (micro-BNC); CGI Art. 197 (bareme); CGI Art. 223 sexies (CEHR); CGI Art. 204 A-N (prelevement a la source); CSS Art. L136-6 (CSG) |
| Tax Authority | Direction Generale des Finances Publiques (DGFiP) |
| Filing Portal | impots.gouv.fr |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a qualified French expert-comptable or commissaire aux comptes |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate table application, bracket calculation, quotient familial parts, micro-BNC abattement, filing deadlines. Tier 2: mixed-use expense apportionment, BNC vs micro-BNC optimisation, CSG deductibility allocation, decote calculation. Tier 3: international income, PEA/assurance-vie interactions, complex family situations, CDHR. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified expert-comptable must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Situation familiale** [T1] -- celibataire, marie/pacse, veuf/veuve, divorce. Determines number of parts fiscales.
2. **Nombre d'enfants a charge** [T1] -- each child adds 0.5 parts (first two) then 1 part (third and subsequent).
3. **Activity type** [T1] -- profession liberale (BNC), commercial (BIC), or mixed.
4. **Regime fiscal** [T1] -- micro-BNC (art. 102 ter) or regime de la declaration controlee (regime reel).
5. **Chiffre d'affaires / recettes brutes** [T1] -- total receipts for the year.
6. **Charges professionnelles** [T1/T2] -- nature and amount of each deductible expense (T2 for mixed-use items).
7. **Cotisations sociales payees** [T1] -- URSSAF, CIPAV, CARMF, etc. -- amounts paid during the year.
8. **Other income** [T1] -- salaires, pensions, revenus fonciers, revenus de capitaux mobiliers.
9. **Prelevement a la source already paid** [T1] -- acomptes mensuels or trimestriels already withheld during the year.
10. **Eligibility for reductions/credits** [T2] -- dons, emploi a domicile, frais de garde, investissements.

**If situation familiale is unknown, STOP. Do not apply quotient familial. Situation familiale is mandatory.**

---

## Step 1: Determine Quotient Familial (Parts Fiscales) [T1]

**Legislation:** CGI Art. 194, 195, 196, 196 bis

### Number of Parts

| Situation | Parts |
|-----------|-------|
| Celibataire, divorce, veuf (sans enfant) | 1 |
| Marie ou pacse (imposition commune) | 2 |
| Celibataire ou divorce avec 1 enfant | 1.5 (or 2 if parent isole) |
| Marie ou pacse avec 1 enfant | 2.5 |
| Marie ou pacse avec 2 enfants | 3 |
| Marie ou pacse avec 3 enfants | 4 |
| Each additional child beyond 3rd | +1 part |

### Plafonnement du Quotient Familial (2025 revenus)

| Situation | Plafond par demi-part |
|-----------|-----------------------|
| Droit commun | EUR 1,791 |
| Parent isole (premier enfant) | EUR 4,262 |
| Demi-part supplementaire (personne seule ayant eleve enfant 5+ ans) | EUR 1,079 |
| Garde alternee (demi-part par enfant) | EUR 2,131 |

**How the quotient works:** Divide revenu net imposable by number of parts. Apply the bareme to this quotient. Multiply the resulting tax by number of parts. This is the impot brut before decote and reductions.

---

## Step 2: Apply the Bareme Progressif [T1]

**Legislation:** CGI Art. 197 I.1 -- Bareme applicable aux revenus 2025

| Tranche de revenu net imposable (par part) | Taux |
|--------------------------------------------|------|
| Jusqu'a EUR 11,600 | 0% |
| De EUR 11,601 a EUR 29,579 | 11% |
| De EUR 29,580 a EUR 84,577 | 30% |
| De EUR 84,578 a EUR 181,917 | 41% |
| Au-dela de EUR 181,917 | 45% |

**Note (2025):** Brackets revalorised by +1.8% for inflation compared to 2024.

### Cumulative Tax per Part at Top of Each Band

| Top of Band | Cumulative Tax per Part |
|-------------|------------------------|
| EUR 11,600 | EUR 0 |
| EUR 29,579 | EUR 1,978 |
| EUR 84,577 | EUR 18,477 |
| EUR 181,917 | EUR 58,337 |

**NEVER compute final tax figures directly in Claude -- pass revenu net imposable and parts to the deterministic engine to apply the bareme and quotient familial.**

---

## Step 3: Micro-BNC vs Regime Reel (Declaration Controlee) [T1/T2]

**Legislation:** CGI Art. 102 ter (micro-BNC); CGI Art. 93 (regime reel)

### Micro-BNC (Art. 102 ter) [T1]

| Parameter | Value |
|-----------|-------|
| Plafond de recettes | EUR 77,700 HT |
| Abattement forfaitaire | 34% (minimum EUR 305) |
| Benefice imposable | 66% of recettes |
| Obligations comptables | Livre de recettes uniquement |
| Declaration | 2042-C-PRO, cases 5HQ/5IQ |

### Regime de la Declaration Controlee (Regime Reel) [T1]

| Parameter | Value |
|-----------|-------|
| Plafond de recettes | Aucun plafond |
| Deduction | Charges reelles justifiees |
| Benefice imposable | Recettes minus charges reelles |
| Obligations comptables | Comptabilite complete (recettes-depenses), bilan simplifie |
| Declaration | 2035 + 2042-C-PRO, cases 5QC/5RC |

### Decision Logic [T2]

- If total charges reelles exceed 34% of recettes: regime reel is more favourable
- If total charges reelles are below 34% of recettes: micro-BNC is more favourable
- [T2] Flag for reviewer: confirm that the client's actual expense ratio warrants the chosen regime
- Once opted for regime reel, minimum 2-year commitment

---

## Step 4: Determine Revenu Net Imposable (Regime Reel) [T1/T2]

**Legislation:** CGI Art. 93, 13, 83

### Computation Structure

| Line | Description | How to Populate |
|------|-------------|-----------------|
| A | Recettes encaissees | Total honoraires/fees received in the year |
| B | Debours et retrocessions | Amounts paid on behalf of clients, retroceded to confreres |
| C | Recettes nettes | A minus B |
| D | Charges professionnelles deductibles | See deductible charges below |
| E | Amortissements | Depreciation on professional assets |
| F | Benefice net (ou deficit) | C minus D minus E |
| G | Plus/moins-values professionnelles | Gains or losses on disposal of professional assets [T2] |
| H | Resultat fiscal | F +/- G, reported on 2042-C-PRO |

### Charges Professionnelles Deductibles [T1/T2]

| Charge | Tier | Treatment |
|--------|------|-----------|
| Loyer du cabinet/bureau (dedie) | T1 | Fully deductible |
| Fournitures de bureau | T1 | Fully deductible |
| Assurance professionnelle (RCP) | T1 | Fully deductible |
| Honoraires de l'expert-comptable | T1 | Fully deductible |
| Cotisations professionnelles (Ordre, syndicat) | T1 | Fully deductible |
| Formation professionnelle / CPD | T1 | Fully deductible |
| Frais de deplacement professionnel | T1 | Fully deductible if wholly professional |
| Logiciels / abonnements professionnels | T1 | Fully deductible |
| Telephone / internet | T2 | Business-use portion only -- client to confirm % |
| Frais de vehicule | T2 | Business portion only -- bareme kilometrique or frais reels |
| Usage professionnel du domicile | T2 | Proportional -- surface dediee / surface totale |
| Cotisations URSSAF, CIPAV, CARMF, CNBF | T1 | Deductible as charges sociales obligatoires |
| Cotisations Madelin / PER | T1/T2 | Deductible within specific ceilings (CGI Art. 154 bis) |
| CSG deductible (6.8%) | T1 | Deductible portion of CSG on professional income |

### NOT Deductible [T1]

| Charge | Reason |
|--------|--------|
| Impot sur le revenu | Tax on income cannot deduct itself |
| Amendes et penalites | Public policy |
| CSG non deductible (2.4%) + CRDS (0.5%) | Expressly non-deductible (CGI Art. 154 quinquies) |
| Depenses personnelles / train de vie | Not professional |
| Frais de reception/representation excessifs | Not wholly professional -- blocked |

---

## Step 5: CSG Deductible [T1]

**Legislation:** CGI Art. 154 quinquies; CSS Art. L136-6

| Prelevements Sociaux | Taux | Deductible IR? |
|----------------------|------|----------------|
| CSG | 9.2% | 6.8% deductible, 2.4% non deductible |
| CRDS | 0.5% | Non deductible |
| Total CSG/CRDS | 9.7% | 6.8% deductible |

**Rule:** The 6.8% deductible CSG paid on professional income in year N is deducted from taxable income in year N. This is separate from the charges sociales obligatoires (URSSAF etc.) which are deducted as professional charges.

---

## Step 6: Decote [T1]

**Legislation:** CGI Art. 197 I.4 -- applicable aux revenus 2025

The decote reduces tax for modest taxpayers.

### Eligibility Threshold

| Situation | Impot brut maximum pour beneficier |
|-----------|------------------------------------|
| Celibataire / imposition individuelle | EUR 1,982 |
| Couple / imposition commune | EUR 3,277 |

### Calculation Formula

| Situation | Formule |
|-----------|---------|
| Imposition individuelle | Decote = EUR 897 - (impot brut x 45.25%) |
| Imposition commune | Decote = EUR 1,483 - (impot brut x 45.25%) |

If the result is negative, the decote is zero (no additional tax). If the decote exceeds the impot brut, the tax is reduced to zero.

---

## Step 7: Contribution Exceptionnelle sur les Hauts Revenus (CEHR) [T1]

**Legislation:** CGI Art. 223 sexies

| Situation | RFR Threshold | Taux |
|-----------|---------------|------|
| Celibataire | EUR 250,001 -- EUR 500,000 | 3% |
| Celibataire | Au-dela de EUR 500,000 | 4% |
| Couple (imposition commune) | EUR 500,001 -- EUR 1,000,000 | 3% |
| Couple (imposition commune) | Au-dela de EUR 1,000,000 | 4% |

**Note (2025):** The CEHR coexists with a new Contribution Differentielle sur les Hauts Revenus (CDHR) for revenus 2025, which ensures a minimum 20% effective tax rate for high earners. The CDHR is [T3] -- escalate to expert-comptable.

---

## Step 8: Reductions et Credits d'Impot [T1/T2]

**Legislation:** CGI Art. 199 quater B, 200, 200 quater, 199 sexdecies, 199 sexvicies

| Type | Categorie | Taux / Plafond | Tier |
|------|-----------|----------------|------|
| Dons aux oeuvres d'interet general | Reduction | 66% dans la limite de 20% du revenu imposable | T1 |
| Dons aux organismes d'aide aux personnes en difficulte | Reduction | 75% dans la limite de EUR 1,000 (2025), puis 66% | T1 |
| Emploi d'un salarie a domicile | Credit | 50% dans la limite de EUR 12,000 (+EUR 1,500/enfant, max EUR 15,000) | T1 |
| Frais de garde d'enfants (moins de 6 ans) | Credit | 50% dans la limite de EUR 3,500/enfant | T1 |
| Investissement locatif (Pinel, Denormandie) | Reduction | Variable selon dispositif | T2 |
| Cotisations syndicales | Credit | 66% dans la limite de 1% du revenu | T1 |
| Adhesion CGA/AGA (regime reel) | Reduction | Plafond EUR 915 (2/3 des frais) | T1 |

**Distinction critique:** A reduction d'impot reduces the tax payable (non-refundable -- cannot create a refund). A credit d'impot is refundable -- if it exceeds the tax due, the excess is refunded.

---

## Step 9: Prelevement a la Source (PAS) [T1]

**Legislation:** CGI Art. 204 A a 204 N

### How It Works for Self-Employed (BNC)

| Element | Detail |
|---------|--------|
| Mechanism | Monthly or quarterly acomptes paid directly by the taxpayer |
| Rate | Taux personnalise calculated by DGFiP based on prior year return |
| Default rate | Applied if no prior year data available (taux neutre from the grille) |
| Adjustment | Taux updated in September each year based on the most recent return |
| Modulation | Taxpayer can request modulation if income varies significantly (>10% change required) |

### BNC Self-Employed Acomptes

- Acomptes are debited on the 15th of each month (or quarterly on 15 Feb, 15 May, 15 Aug, 15 Nov)
- Based on prior year's BNC result and the personalised rate
- Year-end reconciliation via the declaration de revenus filed in May/June

---

## Step 10: Filing Deadlines [T1]

**Legislation:** CGI Art. 170, 175; BOI-IR-DECLA

| Filing / Payment | Deadline |
|-----------------|----------|
| Declaration 2035 (regime reel BNC) | 2nd business day after 1 May (typically early May) |
| Declaration 2042 + 2042-C-PRO (online) | Late May / early June (varies by departement -- zones 1, 2, 3) |
| PAS acomptes | 15th of each month (or quarterly) -- ongoing |
| Solde d'impot (if balance due) | Debited in September (or spread Sep-Dec if > EUR 300) |
| Regularisation si trop-percu | Refunded in July/August |

**Zone deadlines (indicative for 2026 filing on 2025 revenus):**
- Zone 1 (departements 01-19 + non-residents): late May
- Zone 2 (departements 20-54): early June
- Zone 3 (departements 55-976): mid-June

---

## Step 11: Penalties [T1]

**Legislation:** CGI Art. 1728, 1729, 1731 bis; LPF Art. L66, L67

| Offence | Penalty |
|---------|---------|
| Late filing (first occurrence, within 30 days of mise en demeure) | 10% surcharge on tax due |
| Late filing (beyond 30 days after mise en demeure) | 40% surcharge |
| Non-filing after mise en demeure (taxation d'office) | 80% surcharge |
| Manquement delibere (intentional understatement) | 40% surcharge |
| Manoeuvres frauduleuses | 80% surcharge |
| Interet de retard | 0.20% per month (2.4% per year) on tax due |
| Late payment of acomptes PAS | 10% surcharge |

**WARNING:** The 40% and 80% surcharges for fraud are severe and may be accompanied by criminal prosecution. Any suspected fraud situation must be escalated immediately to a qualified expert-comptable or avocat fiscaliste.

---

## Step 12: Record Keeping [T1]

**Legislation:** LPF Art. L102 B

| Requirement | Detail |
|-------------|--------|
| Minimum retention period | 6 years from the end of the year to which the documents relate |
| What to keep | All invoices, receipts, bank statements, contracts, 2035 and supporting schedules, asset register |
| Format | Paper or digital (administration accepts digital copies since 2017) |
| Livre-journal des recettes et depenses | Mandatory for regime reel / declaration controlee |
| Registre des immobilisations et amortissements | Mandatory for regime reel |

---

## Step 13: Edge Case Registry

### EC1 -- Micro-BNC client with expenses above 34% [T2]
**Situation:** Client is under micro-BNC with EUR 60,000 recettes and EUR 25,000 in real charges (41.7%).
**Resolution:** Real charges exceed the 34% abattement. Regime reel would give a lower benefice imposable (EUR 35,000 vs EUR 39,600 under micro). [T2] Flag for reviewer: recommend switching to regime reel but confirm minimum 2-year commitment.

### EC2 -- Quotient familial plafonnement triggered [T1/T2]
**Situation:** Married couple with 3 children (4 parts), revenu net imposable EUR 120,000. The quotient familial advantage for the 2 extra parts (beyond the 2 for the couple) exceeds the plafond.
**Resolution:** Calculate tax both with and without the additional parts. If the difference exceeds EUR 1,791 per additional demi-part, cap the advantage at the plafond. [T2] Flag for reviewer: confirm the plafonnement calculation.

### EC3 -- CSG deductible vs non deductible confusion [T1]
**Situation:** Client deducts the full 9.2% CSG from taxable income.
**Resolution:** Only 6.8% is deductible. The remaining 2.4% CSG + 0.5% CRDS are NOT deductible. Correct the deduction to 6.8% only.

### EC4 -- Prelevement a la source acomptes not matching actual income [T2]
**Situation:** Client's BNC income has dropped 40% compared to prior year, but PAS acomptes are still based on last year's higher income.
**Resolution:** Client can request a modulation of the taux on impots.gouv.fr if the estimated year-end tax will differ by more than 10%. [T2] Flag for reviewer: confirm the modulation request is justified and correctly calculated.

### EC5 -- Mixed personal/professional use of vehicle [T2]
**Situation:** Client uses personal car 70% for professional visits, 30% personal. Claims full fuel and insurance.
**Resolution:** Only 70% of vehicle expenses deductible. Client must maintain a log of professional kilometres. Alternative: use the bareme kilometrique forfaitaire (based on fiscal horsepower and km). [T2] Flag for reviewer: confirm business percentage and chosen method.

### EC6 -- Credit d'impot vs reduction confusion [T1]
**Situation:** Client has EUR 800 reduction d'impot but only EUR 500 impot net after decote. Client expects a EUR 300 refund.
**Resolution:** A reduction d'impot can only reduce tax to zero -- no refund of the excess EUR 300. Only a credit d'impot would generate a refund. Explain the difference to the client.

### EC7 -- BNC client receives retrocession from confrere [T1]
**Situation:** An avocat retrocedes EUR 10,000 of fees to a collaborateur who helped on the case.
**Resolution:** The payer deducts the retrocession from their recettes (line B on the 2035). The receiver declares it as recettes. Both entries must net to zero across the two practitioners.

### EC8 -- First year of activity, no prior PAS rate [T1]
**Situation:** New freelancer starting in 2025. No prior year return exists.
**Resolution:** DGFiP applies the taux neutre (grille de taux par defaut) based on estimated income declared at registration. Client should declare estimated income on impots.gouv.fr to avoid under- or over-payment of acomptes.

### EC9 -- Cotisations Madelin/PER ceiling exceeded [T2]
**Situation:** Client contributes EUR 30,000 to a PER (Plan d'Epargne Retraite) in addition to mandatory cotisations.
**Resolution:** PER deduction is capped at the higher of: (a) 10% of benefice imposable (capped at 8 PASS) or (b) 10% of PASS. Excess contributions are not deductible. [T2] Flag for reviewer: confirm the applicable ceiling and available envelope.

### EC10 -- Couple with disparate incomes opting for taux individualise [T2]
**Situation:** Married couple: one spouse earns EUR 80,000 BNC, the other earns EUR 15,000 salary. Default taux PAS applied equally is disproportionate for the lower earner.
**Resolution:** Couple can opt for taux individualise on impots.gouv.fr, which allocates the PAS rate proportionally to each spouse's income. [T2] Flag for reviewer: confirm opt-in and that total yearly tax remains unchanged.

---

## Step 14: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified expert-comptable must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to expert-comptable or avocat fiscaliste. Document gap.
```

---

## Step 15: Test Suite

### Test 1 -- Single BNC freelancer, regime reel, mid-range income
**Input:** Celibataire (1 part), recettes EUR 60,000, charges reelles EUR 18,000, CSG deductible EUR 2,856, no other income, PAS acomptes paid EUR 4,000.
**Expected output:** Benefice net = EUR 42,000. Revenu net imposable = EUR 42,000 - EUR 2,856 = EUR 39,144. Quotient (1 part) = EUR 39,144. Tax per part: EUR 0 + EUR 1,978 + EUR 2,870 = EUR 4,848. Impot brut = EUR 4,848. No decote (exceeds EUR 1,982). PAS paid = EUR 4,000. Solde = EUR 848 due.

### Test 2 -- Married couple, micro-BNC, with children
**Input:** Marie (2 parts base), 2 enfants (+1 part = 3 parts total). Recettes micro-BNC EUR 70,000. Abattement 34% = EUR 23,800. Benefice imposable = EUR 46,200. No other income.
**Expected output:** Quotient = EUR 46,200 / 3 = EUR 15,400. Tax per part: EUR 0 + EUR 418 = EUR 418. Impot brut = EUR 418 x 3 = EUR 1,254. Check plafonnement: compare with tax at 2 parts. EUR 46,200 / 2 = EUR 23,100. Tax per part at 2 parts: EUR 0 + EUR 1,265 = EUR 1,265. Total at 2 parts: EUR 2,530. Advantage of 3rd part: EUR 2,530 - EUR 1,254 = EUR 1,276. Plafond = EUR 1,791. EUR 1,276 < EUR 1,791, so no cap. Final tax = EUR 1,254.

### Test 3 -- Decote applicable
**Input:** Celibataire, revenu net imposable EUR 16,000. Tax per bareme: EUR 0 + EUR 484 = EUR 484. Impot brut EUR 484.
**Expected output:** Decote = EUR 897 - (EUR 484 x 45.25%) = EUR 897 - EUR 219 = EUR 678. Decote exceeds impot brut (EUR 678 > EUR 484), so tax reduced to EUR 0.

### Test 4 -- CEHR applies
**Input:** Celibataire, RFR EUR 350,000. CEHR tranche: EUR 350,000 - EUR 250,000 = EUR 100,000 x 3% = EUR 3,000.
**Expected output:** CEHR = EUR 3,000, added on top of progressive tax and any decote.

### Test 5 -- Micro-BNC vs regime reel breakeven
**Input:** Recettes EUR 50,000. Charges reelles EUR 17,000 (34% of recettes exactly).
**Expected output:** Micro-BNC benefice = EUR 50,000 x 66% = EUR 33,000. Regime reel benefice = EUR 50,000 - EUR 17,000 = EUR 33,000. Both identical. Recommend micro-BNC for simplicity (no 2035 to file, no comptabilite requirement).

### Test 6 -- Credit d'impot emploi a domicile generates refund
**Input:** Celibataire, impot net EUR 1,000. Emploi a domicile expenses EUR 8,000. Credit = 50% x EUR 8,000 = EUR 4,000.
**Expected output:** Credit d'impot EUR 4,000 exceeds tax EUR 1,000. Refund of EUR 3,000 (credit is refundable).

### Test 7 -- CSG deductible correctly separated
**Input:** Total CSG/CRDS paid EUR 4,850 (of which CSG 9.2% = EUR 4,600, CRDS 0.5% = EUR 250). Deductible CSG = 6.8% portion.
**Expected output:** Deductible CSG = EUR 4,600 x (6.8/9.2) = EUR 3,400. Non-deductible = EUR 4,600 - EUR 3,400 + EUR 250 = EUR 1,450. Only EUR 3,400 reduces revenu imposable.

---

## PROHIBITIONS

- NEVER apply the bareme without knowing situation familiale and number of parts
- NEVER compute final tax figures directly -- pass revenu net imposable and parts to the deterministic engine
- NEVER deduct the full 9.2% CSG -- only 6.8% is deductible
- NEVER deduct CRDS (0.5%) -- it is expressly non-deductible
- NEVER deduct impot sur le revenu from professional charges
- NEVER deduct amendes or penalites
- NEVER treat a reduction d'impot as refundable -- only credits d'impot are refundable
- NEVER ignore the plafonnement du quotient familial for families with children
- NEVER advise on the CDHR (Contribution Differentielle sur les Hauts Revenus) -- escalate to T3
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their expert-comptable for confirmation
- NEVER ignore the minimum 2-year commitment when recommending a switch from micro-BNC to regime reel

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an expert-comptable, commissaire aux comptes, or avocat fiscaliste licensed in France) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
