---
name: fr-income-tax
description: >
  Use this skill whenever asked about French income tax for self-employed individuals (auto-entrepreneurs, micro-entrepreneurs, or professions libérales). Trigger on phrases like "impôt sur le revenu France", "déclaration 2042", "micro-entrepreneur", "auto-entrepreneur", "BNC", "BIC", "professions libérales France", "abattement forfaitaire", "Urssaf", "cotisations sociales", "régime micro", "régime réel", "IR France", "acomptes provisionnels", "Revenu fiscal de référence", "Crédit d'impôt", "BNP Paribas statement", "Qonto expense", "Shine business", "Stripe France", or any question about filing or computing French income tax for a self-employed individual. This skill covers progressive brackets (0--45%), micro-entrepreneur abattements, BNC/BIC regimes, social charges, tax credits, filing deadlines, and withholding (prélèvement à la source). ALWAYS read this skill before touching any French income tax work.
version: 2.0
jurisdiction: FR
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# France Income Tax (Impôt sur le Revenu) -- Self-Employed Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | France (République française) |
| Tax | Impôt sur le Revenu (IR) + Prélèvements sociaux (social charges) |
| Currency | EUR only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Code Général des Impôts (CGI) |
| Tax authority | Direction Générale des Finances Publiques (DGFiP) |
| Filing portal | impots.gouv.fr (espace particulier) |
| Filing deadline | Late May / early June (varies by département, online) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a French Expert-Comptable or Avocat Fiscaliste |
| Skill version | 2.0 |

### Progressive Rate Table (2025 -- Tranches) [T1]

| Revenu net imposable (EUR/part) | Rate |
|---|---|
| 0 -- 11,497 | 0% |
| 11,498 -- 26,231 | 11% |
| 26,232 -- 74,545 | 30% |
| 74,546 -- 160,336 | 41% |
| Above 160,336 | 45% |

**France uses a family quotient system (quotient familial). Rates apply per "part" (share). A single person = 1 part; a married couple = 2 parts; each child = 0.5 additional part. Taxable income is divided by number of parts, rates applied, then multiplied back.**

**Contribution Exceptionnelle sur les Hauts Revenus (CEHR):** 3% on income between EUR 250,001--500,000 (single); 4% above EUR 500,000.

### Micro-Entrepreneur / Auto-Entrepreneur Abattements [T1]

| Activity Type | Abattement (flat deduction) | Minimum Abattement |
|---|---|---|
| Sale of goods (BIC ventes) | 71% | EUR 305 |
| Services commerciaux (BIC services) | 50% | EUR 305 |
| Professions libérales (BNC) | 34% | EUR 305 |

**Taxable income = Gross receipts x (100% - Abattement %).** No actual expense deduction for micro-entrepreneurs.

### Micro-Entrepreneur Revenue Thresholds (2025) [T1]

| Activity | Threshold for Micro Regime |
|---|---|
| Sales of goods | EUR 188,700 |
| Services / professions libérales | EUR 77,700 |

### Conservative Defaults [T1]

| Ambiguity | Default |
|---|---|
| Regime unknown | Micro-entrepreneur (simplest; check threshold) |
| Activity type unknown | Professions libérales (34% abattement -- most conservative) |
| Parts familiales unknown | 1 part (single) |
| Crédit d'impôt eligibility unknown | No credit applied |
| Prélèvement à la source rate unknown | Apply standard monthly withholding |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** Bank statement for the full calendar year (January--December) in CSV, PDF, or pasted text. Confirmation of regime (micro-entrepreneur or régime réel) and activity type (BIC ventes, BIC services, or BNC).

**Recommended:** Déclaration CA12 or CA3 (Urssaf monthly/quarterly turnover declarations), all client invoices, Urssaf social charge payment receipts, prior year avis d'imposition.

**Ideal:** Complete comptabilité (for régime réel), all Certificats de retenue à la source, pièces justificatives for expense deductions, family situation certificate.

### Refusal Catalogue

**R-FR-1 -- Sociétés (SARL, SAS, SA, etc.).** "Corporate entities file Impôt sur les Sociétés (IS). Out of scope."

**R-FR-2 -- Non-residents with French income.** "Non-resident taxation involves different rate schedules, withholding rates, and treaty analysis. Out of scope -- escalate."

**R-FR-3 -- Régime réel simplifié / normal (complex).** "The régime réel with complex depreciation, asset registers, and detailed accounting requires an Expert-Comptable. This skill handles micro-entrepreneur abattement method and basic BNC réel simplifié."

**R-FR-4 -- Plus-values (capital gains).** "Capital gains on securities, real estate, or business assets require specialist computation. Escalate."

**R-FR-5 -- Foreign income and DTAA.** "Double taxation treaty analysis with non-French income sources is outside scope. Escalate."

---

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement line matches a pattern, apply the treatment directly. If no pattern matches, fall through to Tier 1 rules in Section 5.

### 3.1 Income Patterns (Crédits)

| Pattern | Tax Line | Treatment | Notes |
|---|---|---|---|
| VIREMENT [client name] / VIR [client] | Chiffre d'affaires (CA) / Recettes | Gross receipts | Professional fee or service income |
| VIREMENT SEPA [client] | Recettes BNC/BIC | Revenue | Standard SEPA transfer from client |
| STRIPE PAYOUT / STRIPE TRANSFER | Recettes | Revenue | Stripe France payout -- match to invoices |
| PAYPAL VIREMENT / PAYPAL PAYOUT | Recettes | Revenue | International client payments via PayPal |
| SUMERIA PAYOUT / LYDIA PRO SETTLEMENT | Recettes | Revenue | Lydia/Sumeria fintech payout |
| QONTO VIREMENT ENTRANT | Recettes | Revenue | Qonto business account transfer in |
| SHINE PAIEMENT [client] | Recettes | Revenue | Shine business account receipt |
| PAYFIT SALAIRE / VIREMENT SALAIRE [employer] | Salaires (Traitements et salaires) | NOT professional income | Employment salary -- Fiche de paie required |
| AIDES CAF / RSA / ALLOCATIONS | EXCLUDE | Social benefits not taxable | CAF benefits are generally not taxable |
| REMBOURSEMENT TVA / CRÉDIT TVA | EXCLUDE | Not income | VAT refund -- not taxable |
| REMBOURSEMENT IMPÔTS / TRÉSOR PUBLIC REMB | EXCLUDE | Not income | Tax refund |
| PRÊT [bank] / CRÉDIT CONSO | EXCLUDE | Not income | Loan proceeds |
| DIVIDENDES [company] | Revenus de capitaux mobiliers | NOT professional income | Dividends -- subject to flat tax (PFU 30%) |
| INTÉRÊTS [bank] / LIVRET A | Revenus de capitaux mobiliers | NOT professional income | Interest income |

### 3.2 Expense Patterns (Débits) -- Régime Réel Filers Only

*(Micro-entrepreneurs do NOT deduct actual expenses -- abattement covers all expenses)*

| Pattern | Tax Category | Treatment | Notes |
|---|---|---|---|
| LOYER BUREAU / BAIL PROFESSIONNEL [landlord] | Loyers et charges locatives | Fully deductible | Dedicated business premises |
| EDF / ENGIE / ÉLECTRICITÉ | Charges de bureau | Business portion deductible | Home office: apportion by floor area |
| FREE / SFR / ORANGE / BOUYGUES (internet) | Frais de télécommunications | Business portion only | Mixed use: apportion |
| FREE MOBILE / SFR / ORANGE (mobile) | Frais de télécommunications | Business portion only | Mixed use: apportion |
| SNCF / TGV / OUI.SNCF | Frais de déplacement | Deductible if business travel | Keep billets as evidence |
| AIR FRANCE / TRANSAVIA / EASY JET | Frais de déplacement | Deductible if business | |
| RESTAURANT [name] / REPAS AFFAIRES | Frais de repas / réception | Business portion deductible | Must document business purpose, attendees |
| FNAC / AMAZON (books/tech) | Fournitures / matériel | Deductible if professional | Separate business from personal orders |
| ADOBE / MICROSOFT / GOOGLE WORKSPACE | Abonnements logiciels | Fully deductible | Business SaaS |
| EXPERT-COMPTABLE / COMPTABLE | Honoraires | Fully deductible | Accounting fees |
| AVOCAT / NOTAIRE | Honoraires | Deductible if business | Legal fees for business matters |
| ASSURANCE RC PRO / MUTUELLE PRO | Assurances professionnelles | Fully deductible | Professional liability |
| URSSAF COTISATIONS | NOT a deductible expense for micro | Special treatment | Urssaf social charges are separate from IR |
| IMPÔT SUR LE REVENU / PRÉLÈVEMENT À LA SOURCE | EXCLUDE | Tax payment | Not deductible |
| CFE (COTISATION FONCIÈRE DES ENTREPRISES) | Impôts et taxes professionnelles | Deductible for BIC/BNC réel | Professional property tax |
| MUTUELLE SANTÉ / PRÉVOYANCE | NOT business expense for micro | Déduction Madelin (réel BNC only) | Madelin deduction for eligible contributions |
| BANQUE FRAIS / FRAIS TENUE DE COMPTE [BNP/SG/CA/LCL] | Frais bancaires | Deductible | Business account charges |
| STRIPE FEE / PAYPAL FEE | Commissions bancaires | Deductible | Payment gateway fees |

### 3.3 Urssaf / Social Charges Patterns

| Pattern | Treatment | Notes |
|---|---|---|
| URSSAF PRÉLÈVEMENT / URSSAF AUTO ENTREPRENEUR | Social contributions (not IR) | Urssaf collects social charges on gross turnover; not an expense deduction for micro-entrepreneurs |
| CIPAV COTISATIONS | Social contributions | Mandatory pension for professions libérales (not regulated) |
| CARPIMKO / CARMF / CARCDSF | Social contributions | Mandatory pension for specific professions |
| PRÉLÈVEMENT À LA SOURCE / PAS | Income tax prepayment | Monthly/quarterly IR withholding -- credit against annual IR |

---

## Section 4 -- Worked Examples

### Example 1 -- Freelance Professional Fee (BNC Micro)

**Input line (BNP Paribas statement):**
`15/03/2025 | VIR SEPA ABC CONSULTING SARL | +3,500.00 | Solde 12,840.50`

**Reasoning:**
Client wire transfer EUR 3,500 for consulting services. Taxpayer is a micro-entrepreneur under BNC (profession libérale). Abattement = 34%. Net taxable income = EUR 3,500 x (1 - 34%) = EUR 2,310. This EUR 2,310 is added to total taxable income for the year. Urssaf social charges are computed separately on the gross EUR 3,500 (approximately 22% = EUR 770), not on the post-abattement amount.

**Classification:** Recettes brutes EUR 3,500. Taxable income contribution EUR 2,310 (after 34% abattement).

### Example 2 -- Stripe Payout

**Input line (Société Générale statement):**
`22/05/2025 | STRIPE PAYMENTS EUROPE | +4,650.00 | Solde 8,220.00`

**Reasoning:**
Stripe France settlement. Net of Stripe fees. Check Stripe dashboard: if Stripe collected EUR 4,800 from clients and deducted EUR 150 fees, gross turnover = EUR 4,800. For micro-entrepreneur, Urssaf and IR are based on the gross EUR 4,800. Stripe fee EUR 150 is irrelevant for micro (abattement covers all expenses). For régime réel, the Stripe fee EUR 150 is a deductible expense.

**Classification (micro):** Recettes brutes EUR 4,800. Abattement 34%/50% as applicable. Stripe fee not separately deductible.

### Example 3 -- Loyer Bureau Payment

**Input line (Crédit Mutuel statement):**
`01/04/2025 | PRÉLÈVEMENT VIREMENT LOYER BUREAU SARL IMMOPRO | -1,200.00 | Solde 5,640.00`

**Reasoning:**
Monthly office rent EUR 1,200. For régime réel BNC filers, rent for a dedicated professional premises is fully deductible as "loyers et charges locatives." For micro-entrepreneurs, this expense is NOT deductible separately -- covered by the abattement.

**Classification (réel):** Loyers EUR 1,200 fully deductible. (Micro: no separate deduction.)

### Example 4 -- Urssaf Auto-Entrepreneur Contribution

**Input line (LCL statement):**
`15/06/2025 | PRÉLÈVEMENT URSSAF AUTO ENT | -528.00 | Solde 4,210.00`

**Reasoning:**
Urssaf social contribution EUR 528 for micro-entrepreneur. This is a social charge payment based on gross turnover (~22% rate). For income tax purposes (IR), Urssaf contributions are NOT deductible from BNC/BIC income for micro-entrepreneurs. They reduce take-home pay but do not reduce the taxable income figure for IR.

**Classification:** EXCLUDE from income tax computation. Record for Urssaf reconciliation only.

### Example 5 -- Salary Credit (Mixed Income)

**Input line (Caisse d'Épargne statement):**
`28/02/2025 | VIREMENT SALAIRE SOCIÉTÉ XYZ | +2,800.00 | Solde 6,150.00`

**Reasoning:**
Monthly salary from an employer. This is traitements et salaires (employment income) -- a separate income category from BNC/BIC professional income. Declared on Déclaration 2042 separately. A standard 10% abattement for professional expenses applies to salary income (capped at EUR 14,171 or minimum EUR 504).

**Classification:** Salaires bruts EUR 2,800. NOT professional income. Declare on 2042 box 1AJ/1BJ.

### Example 6 -- Prélèvement à la Source (Monthly Tax Withholding)

**Input line (BNP Paribas statement):**
`27/01/2025 | PRÉLÈVEMENT FISCAL DGFIP PAS | -420.00 | Solde 7,890.00`

**Reasoning:**
Monthly "prélèvement à la source" (PAS) -- the monthly income tax prepayment deducted by the DGFiP from the bank account of self-employed persons. Based on the prior year's income declaration. It is NOT an expense. It is a prepayment of income tax credited against the annual IR bill.

**Classification:** EXCLUDE from income/expenses. Record: PAS paid EUR 420/month = EUR 5,040/year (credit against annual IR).

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Micro-Entrepreneur / Micro-BNC / Micro-BIC Regime

**Legislation:** CGI Art. 50-0 (BIC); CGI Art. 102 ter (BNC)

Taxable income = Gross receipts x (1 - abattement %).

- No actual expense deduction
- Minimum abattement EUR 305 (even if receipts are lower)
- Urssaf computed on GROSS receipts (not post-abattement)
- Income tax computed on POST-abattement income via standard IR brackets

### 5.2 BNC Régime Réel Simplifié (Déclaration 2035)

For professions libérales above EUR 77,700 or who opt out of micro:

- Declare actual receipts and actual expenses on Form 2035
- Deductible expenses: rent, telecommunications (business %), travel, professional insurance, accounting fees, equipment depreciation, software
- NOT deductible: personal expenses, income tax itself
- Partial deductibility of social charges: Madelin health/provident contributions ARE deductible from BNC income

### 5.3 Tax Computation Flow

```
Gross professional receipts (chiffre d'affaires)
x (1 - abattement %) for micro, OR
- Actual expenses (régime réel)
= Net professional income (BNC or BIC)
+ Other income (salaires, pensions, revenus fonciers)
= Revenu brut global
- Charges déductibles (alimony, certain pension contributions)
= Revenu net global
Divide by number of parts (quotient familial)
Apply progressive rate table
x Number of parts
= IR tentative
Cap benefit of quotient familial (plafonnement)
+ CEHR if applicable
- Crédits et réductions d'impôt
= IR net
```

### 5.4 Prélèvement à la Source (PAS) -- Monthly Withholding

Since 2019, French taxpayers pay income tax monthly via PAS (automatic bank debit). For self-employed:
- Rate based on prior year income (taux personnalisé) or neutral rate for first year
- Monthly debit from bank account
- At annual declaration time, actual tax is computed; if PAS exceeded, refund issued

PAS payments are NOT expenses -- they are advance payments of the annual IR.

### 5.5 Cotisation Foncière des Entreprises (CFE)

Local business property tax. Mandatory for all self-employed including micro-entrepreneurs. Deductible expense for régime réel filers. NOT deductible for micro-entrepreneurs.

### 5.6 Filing Deadlines

| Item | Deadline |
|---|---|
| Déclaration 2042 (online, most areas) | Late May / early June (varies by département) |
| Déclaration 2042 (paper) | Mid-May |
| Déclaration 2035 (BNC réel) | Same window as 2042 |
| Urssaf monthly declarations (micro) | 30th of the following month |
| CFE payment | 15 December |

### 5.7 Penalties

| Offence | Penalty |
|---|---|
| Late filing | 10% of tax due (without notice); 40% if filed after formal notice |
| Under-declaration (omission) | 40% if deliberate; 80% if fraudulent |
| Late payment | 0.20% per month (2.4% per year) |
| Non-declaration | 100% penalty on tax assessed by DGFiP |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Regime Optimisation (Micro vs Réel)

Micro is simpler but not always optimal. Réel is better when actual expenses exceed the abattement percentage. For BNC professions libérales: if actual costs > 34% of receipts, réel simplifié yields lower tax. For BIC services: if costs > 50% of receipts, réel is better.

Flag for reviewer to compute both and advise.

### 6.2 Quotient Familial (Family Quotient)

The number of fiscal parts significantly impacts tax. Changes to family situation (marriage, children, divorce) must be declared. The benefit of each additional 0.5 part is capped at EUR 1,751 reduction in tax per half-part (2025 figure).

Flag for reviewer to confirm family situation and number of parts.

### 6.3 Crédits d'Impôt (Tax Credits)

Several credits reduce IR directly:
- Crédit d'impôt garde d'enfants (children under 6): 50% of costs, max EUR 3,500 per child
- Crédit d'impôt emploi à domicile (home help): 50% of wages paid, max EUR 12,000
- Crédit d'impôt formation du dirigeant: EUR 40/hour of training

Flag for reviewer to identify applicable credits.

### 6.4 Madelin Deductions (Régime Réel BNC Only)

Contributions to Madelin-qualified health, disability, provident, and pension insurance contracts are fully deductible from BNC income (for régime réel filers). Not available to micro-entrepreneurs.

### 6.5 Home Office Deduction (Régime Réel)

For régime réel BNC filers working from home: proportionate rent, electricity, internet, and heating may be deducted based on floor area ratio of the office to total home area. Must be documented and consistent.

---

## Section 7 -- Excel Working Paper Template

```
IMPÔT SUR LE REVENU -- WORKING PAPER 2025
Contribuable: _______________  Numéro fiscal: ___________
Régime: Micro-entrepreneur (BNC/BIC) / Régime réel (BNC) [circle one]
Situation familiale: Célibataire / Marié(e) / PACS / Divorcé(e) / Veuf(ve)
Nombre de parts: ___________

A. REVENUS PROFESSIONNELS
  Régime Micro:
  A1. CA brut BNC (professions libérales)      ___________
  A2. Abattement 34%                           ___________
  A3. Revenu BNC net imposable (A1 x 66%)      ___________

  Régime Réel BNC (Form 2035):
  A4. Recettes brutes                          ___________
  A5. Total charges déductibles                ___________
  A6. Revenu BNC net imposable (A4 - A5)       ___________

B. AUTRES REVENUS
  B1. Salaires bruts (box 1AJ / 1BJ)          ___________
  B2. Moins abattement 10% (min 504, max 14,171) ___________
  B3. Salaires nets imposables                 ___________
  B4. Pensions de retraite                     ___________
  B5. Revenus fonciers                         ___________
  B6. Total autres revenus                     ___________

C. REVENU BRUT GLOBAL (A3 or A6 + B6)         ___________

D. CHARGES DÉDUCTIBLES
  D1. Pensions alimentaires versées            ___________
  D2. Autres charges                           ___________

E. REVENU NET GLOBAL (C - D)                   ___________

F. QUOTIENT FAMILIAL
  F1. Revenu imposable par part (E / parts)    ___________
  F2. IR sur E/parts (apply rate table)        ___________
  F3. IR total (F2 x parts)                    ___________

G. RÉDUCTIONS / CRÉDITS D'IMPÔT
  G1. Réduction emploi à domicile              ___________
  G2. Crédit garde d'enfants                   ___________
  G3. Autres crédits                           ___________

H. IR NET (F3 - G)                             ___________

I. PRÉLÈVEMENTS DÉJÀ EFFECTUÉS (PAS)           ___________

J. SOLDE IR DÛ / À REMBOURSER (H - I)         ___________

REVIEWER FLAGS:
  [ ] Regime confirmed (micro vs réel)?
  [ ] Number of parts verified (family situation)?
  [ ] Urssaf/social charges reconciled with Urssaf account?
  [ ] PAS monthly payments summed from bank statement?
  [ ] Crédits d'impôt identified?
  [ ] Madelin deductions applicable (réel BNC only)?
```

---

## Section 8 -- Bank Statement Reading Guide

### French Bank Statement Formats

| Bank | Format | Key Fields |
|---|---|---|
| BNP Paribas | CSV / PDF | Date opération, Libellé, Débit EUR, Crédit EUR, Solde EUR |
| Société Générale | CSV | Date, Libellé, Montant, Devise |
| Crédit Agricole | CSV | Date, Libellé, Débit, Crédit, Solde |
| LCL | CSV / PDF | Date, Libellé, Débit, Crédit, Solde |
| Crédit Mutuel | CSV | Date, Libellé, Montant (neg = debit) |
| Caisse d'Épargne | CSV | Date de l'opération, Libellé, Montant, Devise |
| Boursorama / BoursoBank | CSV | Date, Catégorie, Label, Débit, Crédit |
| Qonto (business) | CSV | Date, Label, Amount, Currency, VAT, Category |
| Shine | CSV | Date, Libellé, Montant, Solde |
| Revolut FR | CSV | Date started, Description, Amount, Currency |

### Key French Banking Narrations

| Narration | Meaning | Classification Hint |
|---|---|---|
| VIR SEPA / VIREMENT | Bank transfer credit | Potential professional income |
| PRÉLÈVEMENT / PRÉLÈV | Direct debit | Expense or tax payment |
| PRÉLÈVEMENT FISCAL DGFIP PAS | Prélèvement à la source | Tax prepayment -- exclude |
| PRÉLÈVEMENT URSSAF | Social charge payment | Separate Urssaf tracking |
| CB [merchant] | Card payment | Identify payee |
| VIREMENT SALAIRE [employer] | Salary credit | Employment income |
| REMBOURSEMENT / REMB | Refund | May reduce expense |
| INTÉRÊTS | Interest | Other income |
| AIDES CAF / ALLOCATION | Social benefits | Generally not taxable |

---

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all VIR SEPA credits from non-personal sources as potential professional income
2. Identify all URSSAF PRÉLÈVEMENT debits -- these are social charges, NOT IR payments
3. Identify all DGFIP PAS debits -- these are IR prepayments (credits)
4. Apply conservative defaults: micro-entrepreneur, BNC abattement 34%, 1 part
5. Flag all salary credits as separate income category
6. Generate working paper with PENDING flags

Present these questions:

```
ONBOARDING QUESTIONS -- FRANCE IMPÔT SUR LE REVENU
1. Régime fiscal: micro-entrepreneur (auto-entrepreneur) or régime réel?
2. Type d'activité: BNC (professions libérales), BIC ventes, or BIC services?
3. Total CA brut pour 2025 (before Urssaf deduction)?
4. Situation familiale: célibataire, marié(e)/PACS, enfants?
5. Aussi salarié(e)? Si oui, salaire brut total?
6. Montant PAS mensuel prélevé en 2025?
7. Contributions Urssaf totales payées en 2025?
8. Avez-vous un Expert-Comptable qui gère votre Déclaration 2035?
9. Avez-vous payé des charges Madelin (mutuelle santé, prévoyance)?
10. Crédits d'impôt potentiels (garde d'enfants, emploi à domicile)?
```

---

## Section 10 -- Reference Material

### Key Legislation / Forms

| Topic | Reference |
|---|---|
| Micro-BNC | CGI Art. 102 ter; Form 2042 C PRO |
| Micro-BIC | CGI Art. 50-0; Form 2042 C PRO |
| BNC régime réel simplifié | CGI Art. 93; Form 2035 |
| Progressive rates | CGI Art. 197 |
| Quotient familial | CGI Art. 193-196 B |
| CEHR | CGI Art. 223 sexies |
| Prélèvement à la source | CGI Art. 204A et seq. |
| Crédit emploi à domicile | CGI Art. 199 sexdecies |
| Crédit garde d'enfants | CGI Art. 200 quater B |
| Madelin | CGI Art. 154 bis |

### Known Gaps / Out of Scope

- Corporate taxation (IS)
- Non-resident French-source income
- Capital gains (plus-values mobilières et immobilières)
- SCI / real estate entities
- Foreign income and DTAA
- TVA (VAT) computation

### Changelog

| Version | Date | Change |
|---|---|---|
| 2.0 | April 2026 | Full rewrite to v2.0 structure; French bank formats; Qonto/Shine business bank patterns; worked examples; micro vs réel regime table |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] Micro-entrepreneur abattement applied to gross receipts (not net of Urssaf)?
- [ ] Urssaf contributions NOT subtracted as IR deductions?
- [ ] PAS monthly debits correctly identified as IR prepayments (credits), not expenses?
- [ ] Quotient familial calculated correctly (number of parts)?
- [ ] CEHR checked for income > EUR 250,000?
- [ ] Crédits d'impôt applied after computing IR (not as deductions from income)?

---

## PROHIBITIONS

- NEVER deduct Urssaf social contributions as a business expense for micro-entrepreneurs (abattement covers all costs)
- NEVER compute taxable income without applying the abattement for micro-entrepreneurs
- NEVER treat PAS (prélèvement à la source) as a deductible expense -- it is a tax prepayment (credit)
- NEVER omit the quotient familial calculation for taxpayers with spouses or children
- NEVER allow income tax (IR) itself as a deductible expense
- NEVER advise on non-resident French income -- escalate
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their Expert-Comptable for confirmation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an Expert-Comptable, Avocat Fiscaliste, or equivalent licensed practitioner in France) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
