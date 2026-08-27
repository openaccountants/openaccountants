---
name: fr-return-assembly
description: Final orchestrator skill that assembles the complete French filing package for France-resident self-employed individuals, micro-entrepreneurs, and sole proprietors. Consumes outputs from all French content skills (france-tva for TVA CA3/CA12, france-income-tax for 2042/2042-C-PRO/2035/2031, france-cotisations for URSSAF/SSI, fr-estimated-tax for prélèvement à la source) to produce a single unified reviewer package containing every worksheet, every form, every brief section, all cross-skill reconciliations, and the final action list with payment instructions, filing instructions, and next-year planning. This is the capstone skill that runs last and produces the final deliverable. MUST be loaded alongside all French content skills listed above. France full-year residents only. Self-employed individuals, micro-entrepreneurs, and sole proprietors only.
version: 1.0
jurisdiction: FR
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# FR Return Assembly

## France Return Assembly Skill v1.0

## CRITICAL EXECUTION DIRECTIVE -- READ FIRST

- **Execute all steps without pausing for permission** — When this skill is invoked, you have already passed through intake. The user has consented to the full workflow. Execute all steps without pausing for permission. Do NOT ask the user "how deep do you want me to go" or "do you want the full package" or any variant. The user asked for their tax returns. They want their tax returns. Produce them. Do NOT announce how many tokens or tool calls this will take. Execute. Do NOT ask which deliverables to prioritise. Produce all deliverables listed in Section 4. If you run out of context mid-execution, finish the computation work first (numbers, positions, flags) then produce whatever formatted outputs you can, and at the very end state clearly which deliverables were not produced and why. Do NOT re-validate scope that intake already validated. If fr-freelance-intake produced an intake package, trust it. You can cross-check specific numbers during reconciliation but do not re-interrogate the user about residency, business structure, or anything else intake already captured. Do NOT pause between content skills to check in. Run them in dependency order (Section 2) without prose status updates between each one. A single status message at the end is fine. Self-checks are targets, not blockers. If a self-check fails, note it in the reviewer brief's open flags section and continue. Do NOT halt the entire workflow because one self-check had an ambiguous answer. Primary source citations go in the final reviewer brief, not in intermediate computation steps. The user has already been told (by the intake skill) that the final package requires expert-comptable signoff before filing. State it once in the final output and move on. Failure mode to avoid: The skill halts mid-execution and asks the user a meta-question about workflow pacing. If you feel the urge to ask "how should I proceed," the correct action is to pick the most defensible path and proceed, flagging the decision in the reviewer brief so the reviewer can challenge it.

## What this file is

The final capstone skill for French self-employed returns. Every French content skill feeds into this one. The output is the complete reviewer package that an expert-comptable can review, sign off on, and deliver to the client along with filing instructions.

This skill coordinates execution of the content skills, verifies cross-skill consistency, and assembles the final deliverable.

## Section 1 -- Scope

- **Scope of package** — Produces the complete French filing package for: Full-year France residents; Self-employed individuals: micro-entrepreneurs, entreprises individuelles au réel, professions libérales, EURL at IR; Tax year 2025 (revenus 2025, déclaration printemps 2026); Filing déclaration de revenus (2042 / 2042-C-PRO), TVA returns (CA3 / CA12 or franchise verification), cotisations sociales reconciliation (URSSAF), CFE, prélèvement à la source (PAS) rate update.

## Section 2 -- Execution order and dependency chain

The skill enforces the following execution order:

0. **france-tva step** — TVA return or franchise en base verification. Runs first because TVA turnover figures feed into the income tax declaration. For réel normal: verify or prepare CA3 returns (monthly/quarterly). For réel simplifié: verify or prepare CA12 (annual + 2 acomptes semestriels in July and December). For franchise en base: verify threshold compliance (€36,800 basic / €39,100 tolérance for services; €91,900 / €101,000 for goods -- Article 293 B CGI). Flag if franchise threshold exceeded: mandatory TVA registration required. Output: TVA position (collectée, déductible, solde), turnover HT confirmed, any crédit de TVA.
0. **france-income-tax step** — Déclaration de revenus (2042 / 2042-C-PRO) and liasse fiscale if au réel. Depends on TVA output: chiffre d'affaires HT must be consistent between TVA and income declarations. Micro-entrepreneur path: 2042-C-PRO cases 5KO/5KP (BIC micro ventes), 5KI/5KJ (BIC micro services), 5HQ/5HB (BNC micro) with abattement forfaitaire (71% BIC ventes, 50% BIC services, 34% BNC). Réel BNC path: 2035 (déclaration contrôlée) + 2042-C-PRO cases 5QC/5QI. Réel BIC path: 2031 + 2042-C-PRO cases 5KC/5KI. Quotient familial calculation using parts fiscales. Barème progressif application (0%, 11%, 30%, 41%, 45% -- 2025 tranches). Décote, plafonnement du quotient familial. Output: revenu net imposable, impôt brut, impôt net, solde à payer ou remboursement.
0. **france-cotisations step** — Cotisations sociales (URSSAF micro-social or TNS réel). Depends on income: micro-social base = chiffre d'affaires; TNS réel base = bénéfice. Micro-social rates (2025): 12.3% BIC vente de marchandises, 21.1% BIC prestations de services, 21.1% BNC, 21.2% professions libérales CIPAV. ACRE: 50% reduction on cotisations for eligible créateurs (first 4 quarters). Versement libératoire de l'IR: 1.0% (BIC ventes), 1.7% (BIC services), 2.2% (BNC) -- eligibility requires RFR N-2 per part ≤ €27,478. TNS réel: cotisations provisionnelles based on prior year + régularisation. Includes maladie-maternité, indemnités journalières, retraite de base, retraite complémentaire, invalidité-décès, allocations familiales, CSG-CRDS. Output: total cotisations due, payments made, shortfall/overpayment, deductible portion for IR.
0. **fr-estimated-tax step** — Prélèvement à la source (PAS) and acomptes contemporains. Depends on income tax: updated PAS rate based on 2025 revenu. Self-employed pay PAS via acomptes contemporains (monthly or quarterly debits from bank account by DGFiP). New rate calculated and applicable from September 2026 (after 2025 return processed). Output: updated PAS rate, projected monthly/quarterly acompte amounts for 2026-2027.

- **Upstream failure handling** — If any upstream content skill fails to produce validated output, the assembly skill notes the failure in the reviewer brief and continues with available data rather than halting entirely.

## Section 3 -- Cross-skill reconciliation

### Cross-check 1: TVA turnover matches income declaration

**Cross-check 1: TVA turnover matches income declaration**

| TVA Output | Income Tax Input | Rule |
| --- | --- | --- |
| CA3/CA12 total CA HT | 2042-C-PRO declared CA or 2035/2031 recettes | Must match within €1 |
| Franchise en base: declared CA | 2042-C-PRO micro cases (5KO/5KP/5HQ etc.) | CA reported to URSSAF = CA on 2042-C-PRO |
| Réel: CA HT from TVA returns | 2035 ligne GA / 2031 ligne FL | TVA-declared and income-declared turnover must reconcile |

If mismatch: Flag for reviewer. Common causes: encaissements vs créances (cash vs accrual basis timing), avoir (credit notes), foreign income not subject to French TVA.

### Cross-check 2: Chiffre d'affaires declared to URSSAF matches income declaration

**Cross-check 2: Chiffre d'affaires declared to URSSAF matches income declaration**

| URSSAF Input | Income Tax Input | Rule |
| --- | --- | --- |
| Micro-social: total CA declared quarterly/monthly | 2042-C-PRO micro cases | Must match exactly |
| TNS réel: bénéfice used for cotisations base | 2035/2031 résultat fiscal | Cotisations base = bénéfice + CSG non déductible + Madelin - some adjustments (Article L.131-6 CSS) |

If mismatch: Verify timing. Micro-social declarations are cash-basis (encaissements). If 2042-C-PRO matches URSSAF total, good. If not, reconcile and explain the difference.

### Cross-check 3: Cotisations sociales deductibility

**Cross-check 3: Cotisations sociales deductibility**

| Item | Micro Regime | Réel Regime |
| --- | --- | --- |
| URSSAF cotisations | Included in abattement forfaitaire -- NOT separately deductible | Deductible from bénéfice (charges de l'exercice) |
| CSG déductible (6.8% of 9.2% total) | Included in abattement | Deductible on 2042 case 6DE (for TNS réel) |
| CSG non déductible (2.4%) + CRDS (0.5%) | Included in abattement | NOT deductible -- must be reintegrated |
| Cotisations Madelin (prévoyance, retraite) | NOT deductible (micro has no expense deduction) | Deductible from BNC/BIC within ceilings (Article 154 bis CGI) |

If inconsistency: An expense deducted on 2035/2031 that is also covered by the micro abattement is double-counted. Flag for reviewer.

### Cross-check 4: TVA input tax and income tax deductions consistency

**Cross-check 4: TVA input tax and income tax deductions consistency**

| Item | TVA Treatment | Income Tax Treatment |
| --- | --- | --- |
| Reclaimable TVA (réel simplifié/normal) | Claimed on CA3/CA12 as TVA déductible | NOT a deduction on 2035/2031 (expense recorded HT) |
| Non-reclaimable TVA (franchise en base) | No TVA recovery | IS part of cost -- expense recorded TTC |
| Non-reclaimable TVA (blocked: véhicules de tourisme, cadeaux >€73 TTC per person per year) | Not claimed | Added to cost (TTC amount deducted) |
| Immobilisations TVA (réel regime) | TVA déductible on immobilisations (CA3 ligne 19 / CA12 ligne 15) | Capital asset recorded HT, amortised over useful life |

If inconsistency: An expense claimed HT on the income side while TVA was not recovered means the TVA portion is lost. Flag for reviewer.

### Cross-check 5: CFE and other local taxes

**Cross-check 5: CFE and other local taxes**

| Tax | Treatment |
| --- | --- |
| CFE (Cotisation Foncière des Entreprises) | Deductible charge for réel regime (2035/2031). Not deductible for micro (included in abattement). |
| CVAE (Cotisation sur la Valeur Ajoutée des Entreprises) | Only if CA > €500,000. Rare for individual freelancers. |

If micro-entrepreneur claims CFE as a deduction: Error. Micro regime uses forfaitaire abattement only.

### Cross-check 6: Versement libératoire de l'IR coherence

**Cross-check 6: Versement libératoire de l'IR coherence**

| Check | Rule |
| --- | --- |
| VL opted in | Verify RFR N-2 per part ≤ €27,478 (2025 threshold, based on 2023 revenus) |
| VL payments made | Must equal 1.0% / 1.7% / 2.2% of declared CA (per activity type) |
| VL and 2042-C-PRO | CA still reported on 2042-C-PRO (cases 5TE/5UE for BIC ventes, 5TB/5UB for BIC services, 5TE/5UE for BNC) but NOT included in barème calculation |
| VL and quotient familial | If VL opted in, the self-employment income does NOT enter the progressive scale. But it IS included in RFR. |

If VL opted in but RFR N-2 exceeds threshold: VL is void. Income reverts to progressive scale for 2025. Flag immediately.

## Section 4 -- Final reviewer package contents

### Documents

1. Executive summary -- one-page overview: filing status, income, impôt net, TVA position, cotisations, PAS update, solde dû/remboursement
2. TVA worksheet -- CA3/CA12 box-by-box or franchise verification with threshold analysis
3. Income tax worksheet -- 2042 / 2042-C-PRO line-by-line, plus 2035 or 2031 if réel
4. Quotient familial and barème calculation -- parts, tranches, décote, plafonnement
5. Cotisations sociales reconciliation -- micro-social quarterly breakdown or TNS réel annual with régularisation
6. CFE verification -- amount paid, deductibility
7. PAS rate update -- current rate, projected new rate, acomptes contemporains for 2026-2027
8. Cross-skill reconciliation summary -- all six cross-checks with pass/fail and notes
9. Reviewer brief -- comprehensive narrative with positions, citations, flags, self-check results
10. Client action list -- what the client needs to do, with dates and amounts

### Reviewer brief contents

```markdown
# Complete Return Package: [Client Name] -- Revenus 2025

## Executive Summary
- Filing status: [Single / Married-joint / PACSé / Single parent]
- Parts fiscales: X
- Residence: France (full-year)
- Business: [Micro-entrepreneur / EI au réel / Profession libérale]
- Regime fiscal: [Micro-BNC / Micro-BIC / Déclaration contrôlée / Réel simplifié]
- Regime TVA: [Franchise en base / Réel simplifié / Réel normal]
- Chiffre d'affaires HT: €X
- Revenu net imposable (foyer): €X
- Impôt brut: €X
- Impôt net (after crédits/réductions): €X
- PAS already withheld (acomptes contemporains 2025): €X
- Solde à payer / Remboursement: €X
- TVA position: €X due / €X crédit
- Cotisations sociales paid: €X / due: €X
- CFE: €X
- PAS rate for 2026-2027: X%

## TVA Return
[Content from france-tva output]
- Registration type and regime
- Chiffre d'affaires HT by period
- TVA collectée summary (20%, 10%, 5.5% rates)
- TVA déductible summary (biens et services, immobilisations)
- Crédit de TVA position
- Franchise en base threshold analysis (if applicable)
- DEB/DES obligations (EU transactions)
- Box-by-box CA3 or CA12 summary

## Income Tax Return (2042 / 2042-C-PRO)
[Content from france-income-tax output]
### Micro-entrepreneur path:
- 2042-C-PRO cases: CA declared, abattement applied, revenu net micro
- Versement libératoire: amount paid, eligibility check
### Réel path:
- 2035/2031 summary: recettes, charges déductibles, résultat fiscal
- Amortissements schedule (immobilisations)
- Plus/moins-values professionnelles (if any)
### Common:
- 2042 foyer income: all income categories
- Quotient familial computation
- Barème progressif application (tranches 2025: 0% up to €11,294, 11% up to €28,797, 30% up to €82,341, 41% up to €177,106, 45% above)
- Décote (if impôt brut < €1,929 single / €3,191 couple)
- Plafonnement du quotient familial (€1,759 per demi-part 2025)
- Réductions d'impôt (dons, etc.)
- Crédits d'impôt (emploi à domicile, garde enfants, etc.)
- Impôt net
- PAS acomptes contemporains paid during 2025
- Solde: due or refund

## Cotisations Sociales (URSSAF)
[Content from france-cotisations output]
### Micro-social path:
- Quarterly/monthly CA declared
- Rate applied (12.3% / 21.1% / 21.2%)
- ACRE reduction (if applicable)
- Total cotisations paid
- Contribution formation professionnelle (CFP): 0.1% (commerce) / 0.2% (services/libéral) / 0.3% (artisan)
### TNS réel path:
- Assiette de cotisations (bénéfice + CSG/CRDS non déductible ± ajustements)
- Cotisations provisionnelles 2025 (based on 2024 revenus)
- Régularisation 2024 (if final 2024 figures now available)
- Breakdown: maladie-maternité, IJ, retraite base, retraite complémentaire, invalidité-décès, AF, CSG-CRDS
- Total due vs total paid
- CSG déductible amount (for 2042 case 6DE)
- Cotisations Madelin within ceilings (Article 154 bis CGI)

## CFE
- Commune and base d'imposition
- Amount paid for 2025
- Deductibility: yes (réel) / no (micro, included in abattement)
- Exonération première année (if applicable)

## Prélèvement à la Source (PAS)
[Content from fr-estimated-tax output]
- Current PAS rate: X%
- Acomptes contemporains paid during 2025: €X
- Projected new PAS rate (effective September 2026): X%
- Projected monthly/quarterly acompte for 2026-2027: €X
- Option to modulate PAS rate if significant income change

## Cross-skill Reconciliation
- TVA turnover vs 2042-C-PRO / 2035 / 2031: [pass/fail]
- URSSAF declared CA vs income declaration: [pass/fail]
- Cotisations deductibility coherence: [pass/fail]
- TVA input tax vs income deductions: [pass/fail]
- CFE treatment: [pass/fail]
- Versement libératoire coherence: [pass/fail]

## Reviewer Attention Flags
[Aggregated from all upstream skills]
- Franchise en base threshold exceeded (mandatory TVA registration)
- Versement libératoire eligibility (RFR N-2 per part check)
- ACRE period verification
- Mixed-use expense percentages (home office, vehicle, phone)
- EU services and DES declaration obligation
- Micro regime threshold approaching (€77,700 services / €188,700 goods)
- Any déficits reportables to carry forward
- Cotisations Madelin within deductibility ceilings
- Plafonnement du quotient familial impact

## Positions Taken
[List with legislation citations]
- e.g., "Franchise en base maintained per Article 293 B CGI -- CA €34,200 remains below €36,800 seuil de base"
- e.g., "Abattement forfaitaire micro-BNC at 34% applied per Article 102 ter CGI"
- e.g., "Home office deduction at 20% of surface -- prorata applied per BOI-BNC-BASE-40-60-60"
- e.g., "ACRE 50% reduction applied for first 4 quarters per Article L.131-6-4 CSS"
- e.g., "Cotisations Madelin retraite €4,200 deducted within ceiling per Article 154 bis CGI (plafond: 10% of bénéfice + 15% fraction between 1 and 8 PASS)"

## Planning Notes for 2026
- PAS rate update and acomptes contemporains schedule
- URSSAF cotisations provisionnelles for 2026 (based on 2025 income)
- TVA threshold monitoring (franchise en base or micro regime limits)
- Capital asset amortissement continuing into 2026
- Versement libératoire IR eligibility re-check (2024 RFR per part for 2026)
- CFE: any base change, dégrèvement, or new commune
- Any legislative changes affecting 2026 (loi de finances, PLFSS)

## Client Action List

### Immediate (déclaration de revenus -- spring 2026):
1. Review this return package with your expert-comptable
2. File déclaration de revenus via impots.gouv.fr (zones: April-June 2026 depending on département)
   - Zone 1 (départements 01-19 + non-residents): late May
   - Zone 2 (départements 20-54): early June
   - Zone 3 (départements 55-976): mid-June
3. Pay solde d'IR if any (September 2026 direct debit, or earlier if >€300)
4. File CA12 by 2nd working day of May 2026 (if réel simplifié)
5. File remaining CA3 returns by the 15th-24th of following month (if réel normal)

### TVA filing calendar (if réel):
- CA3 (réel normal): monthly by 15th-24th of following month (depending on DGFIP calendar)
- CA12 (réel simplifié): annual return by 2nd working day of May 2026
  - 1er acompte: July 2026 (55% of prior year TVA nette)
  - 2ème acompte: December 2026 (40% of prior year TVA nette)

### URSSAF (micro-social):
- Monthly or quarterly declarations continue on autoentrepreneur.urssaf.fr
- Monthly: due last day of following month
- Quarterly: due 31 January (Q4), 30 April (Q1), 31 July (Q2), 31 October (Q3)

### URSSAF (TNS réel):
- Cotisations provisionnelles 2026 debited monthly or quarterly
- Régularisation 2025 after DSI filed (included in updated échéancier)

### CFE:
- Acompte: 15 June 2026 (if prior year CFE > €3,000)
- Solde: 15 December 2026

### PAS:
- New PAS rate effective September 2026 after DGFiP processes 2025 return
- Option to request modulation if income changed significantly (via impots.gouv.fr > Gérer mon prélèvement à la source)

### Ongoing:
1. Issue TVA-compliant invoices (numéro SIRET, mentions obligatoires per Article 242 nonies A annexe II CGI)
2. Retain all purchase invoices and receipts (6-year retention for fiscal, 10-year commercial -- Articles L.102 B and L.123-22 Code de commerce)
3. Maintain FEC-ready bookkeeping if au réel (fichier des écritures comptables -- Article L.47 A LPF)
4. Monitor franchise en base threshold monthly
5. File DES (déclaration européenne de services) if providing services to EU clients
6. Monitor micro-entrepreneur thresholds for potential régime change
```

## Section 5 -- Refusals

- **R-FR-A1** — Upstream skill did not run. Name the specific skill. Note: this is a warning, not a hard stop. Continue with available data and flag the gap.  _(R-FR-A1)_
- **R-FR-A2** — Upstream self-check failed. Name the specific check and note it in the reviewer brief. Continue.  _(R-FR-A2)_
- **R-FR-A3** — Cross-skill reconciliation failed. Name the specific reconciliation and describe the discrepancy. Flag for reviewer but continue.  _(R-FR-A3)_
- **R-FR-A4** — Intake incomplete. Specific missing intake items prevent computation. List what is missing and ask the user for the specific data point.  _(R-FR-A4)_
- **R-FR-A5** — Out-of-scope item discovered during assembly. E.g., SCI income, agricultural activity, or foreign pension. Flag and exclude from computation.  _(R-FR-A5)_
- **R-FR-A6** — Franchise en base threshold exceeded. This is a critical flag, not a refusal. The computation continues, but the reviewer brief must prominently warn that TVA registration is legally required and prior invoices may need correction.  _(R-FR-A6)_

## Section 6 -- Self-checks

- **Check FR1** — All upstream skills executed. france-tva, france-income-tax, france-cotisations all produced output. fr-estimated-tax produced output or PAS was computed from income tax output.  _(Check FR1)_
- **Check FR2** — TVA turnover matches income declaration. CA HT within €1 tolerance across TVA and 2042-C-PRO / 2035 / 2031.  _(Check FR2)_
- **Check FR3** — URSSAF CA matches income declaration. Micro-social total declared CA = 2042-C-PRO micro cases. Or TNS réel bénéfice correctly flows to cotisation base.  _(Check FR3)_
- **Check FR4** — Correct abattement applied for micro. 71% for BIC ventes, 50% for BIC services, 34% for BNC. No mixing.  _(Check FR4)_
- **Check FR5** — Quotient familial correctly computed. Parts match marital status + children + single parent bonus.  _(Check FR5)_
- **Check FR6** — Barème applied to correct revenu. Revenu net imposable / parts = revenu par part. Each tranche applied correctly.  _(Check FR6)_
- **Check FR7** — Versement libératoire eligibility verified. If opted in, RFR N-2 per part ≤ €27,478. If ineligible, income reverts to barème.  _(Check FR7)_
- **Check FR8** — CSG déductible correctly identified. Only 6.8% of total 9.2% CSG is déductible (for TNS réel). Non-déductible CSG (2.4%) + CRDS (0.5%) not deducted on 2042.  _(Check FR8)_
- **Check FR9** — Cotisations Madelin within ceilings. Article 154 bis CGI ceiling respected for prévoyance, retraite, perte d'emploi.  _(Check FR9)_
- **Check FR10** — CFE treatment correct. Deductible for réel, not for micro. Not double-counted.  _(Check FR10)_
- **Check FR11** — PAS acomptes contemporains reconciled. Total paid during 2025 applied against impôt net to compute solde.  _(Check FR11)_
- **Check FR12** — Filing calendar is complete. All deadlines for TVA, 2042, URSSAF, CFE, and PAS are listed with specific dates and amounts.  _(Check FR12)_
- **Check FR13** — Reviewer brief contains legislation citations. Every position taken references the specific article of CGI, CSS, or LPF.  _(Check FR13)_

## Section 7 -- Output files

- **Three output files** — The final output is three files: 1. [client_slug]_2025_france_master.xlsx -- Single master workbook containing every worksheet and form. Sheets include: Cover, TVA (CA3/CA12 or franchise check), 2042-C-PRO (micro or réel), Barème & Quotient Familial, 2035/2031 (if réel), Cotisations Sociales, CFE, PAS Update, Cross-Check Summary. Use live formulas where possible -- e.g., 2042-C-PRO CA references the TVA turnover cell; micro abattement computed automatically; barème tranches calculated from revenu net imposable. Verify no #REF! errors. Verify computed values match the Python/computation model within €1 before shipping. 2. reviewer_brief.md -- Single markdown file covering all sections from Section 4 above: executive summary, TVA, income tax, cotisations, CFE, PAS, cross-skill reconciliation, flags, positions, planning notes. 3. client_action_list.md -- Single markdown file with step-by-step actions: immediate filings and payments, TVA calendar, URSSAF calendar, CFE dates, PAS updates, ongoing compliance reminders. If execution runs out of context mid-build: produce whatever is complete, then state at the end which of the three files were not produced or are partial. All files are placed in /mnt/user-data/outputs/ and presented to the user via the present_files tool at the end.

## Section 8 -- Cross-skill references

- **Inputs and Outputs** — Inputs: fr-freelance-intake -- structured intake package (JSON); france-tva -- TVA return box values and classification output; france-income-tax -- 2042/2042-C-PRO/2035/2031 computation output; france-cotisations -- URSSAF micro-social or TNS réel reconciliation output; fr-estimated-tax -- PAS rate update and acomptes schedule. Outputs: The final reviewer package. No downstream skill.

## Section 9 -- Known gaps

1. PDF form filling is not automated. The reviewer uses the worksheets to fill official forms on impots.gouv.fr.
2. E-filing is handled by the reviewer or client via impots.gouv.fr, not by this skill.
3. Payment execution is the client's responsibility; the skill only provides instructions and amounts.
4. EURL at IR assembly is supported but not deeply tested. EURL-specific liasse (2031 or 2035 depending on BIC/BNC) may require manual adjustment for gérant rémunération and charges sociales.
5. Multi-year amortissement tracking assumes the prior year schedule is provided. If not, only current-year acquisitions are amortised.
6. Foreign source income (revenus de source étrangère) and convention fiscale application are out of scope.
7. Revenus fonciers (2044) are noted in the foyer income total but the detailed 2044 preparation is out of scope.
8. Plus-values immobilières (capital gains on property) are out of scope.
9. ISF/IFI (wealth tax) is out of scope.
10. SCI or multi-entity structures are out of scope.
11. The package is complete only for the 2025 tax year; 2026 appears only as prospective planning.

### Change log

v1.0 (May 2026): Initial draft. Modelled on mt-return-assembly v0.1 adapted for France jurisdiction with four content skills (TVA, income tax, cotisations sociales, PAS/estimated tax).

## End of skill

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
