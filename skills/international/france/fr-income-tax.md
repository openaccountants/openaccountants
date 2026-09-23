---
name: fr-income-tax
description: Use this skill whenever asked about French income tax for self-employed individuals (auto-entrepreneurs, micro-entrepreneurs, or professions libérales). Trigger on phrases like "impôt sur le revenu France", "déclaration 2042", "micro-entrepreneur", "auto-entrepreneur", "BNC", "BIC", "professions libérales France", "abattement forfaitaire", "Urssaf", "cotisations sociales", "régime micro", "régime réel", "IR France", "acomptes provisionnels", "Revenu fiscal de référence", "Crédit d'impôt", "BNP Paribas statement", "Qonto expense", "Shine business", "Stripe France", or any question about filing or computing French income tax for a self-employed individual. This skill covers progressive brackets (0--45%), micro-entrepreneur abattements, BNC/BIC regimes, social charges, tax credits, filing deadlines, and withholding (prélèvement à la source). ALWAYS read this skill before touching any French income tax work.
version: 2.0
jurisdiction: FR
tax_year: 2026
last_updated: 2026-09-23
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# French income tax for self-employed individuals (impôt sur le revenu)

France taxes the income of the previous calendar year: the scale applied in 2026 is charged on the income of 2025, declared in spring 2026. Figures are for tax year 2026. Where a limit governs income received in 2026 instead, the table row says so. Urssaf social contributions are a separate charge and are not computed here: use `fr-social-contributions`. Local business property tax is in `fr-cfe`, and the full income tax computation for a household that is not self-employed is in `fr-personal-income-tax`.

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | France (République française) |
| Tax | Impôt sur le revenu (IR) |
| Currency | EUR only |
| Tax year | Calendar year (1 January to 31 December) |
| Primary legislation | Code général des impôts (CGI) |
| Tax authority | Direction générale des Finances publiques (DGFiP) |
| Filing portal | impots.gouv.fr (espace particulier) |
| Filing deadline | Set by département each year: see Section 5.6 |
| Contributor | Open Accountants Community |
| Validated by | Pending: no French Expert-Comptable or Avocat Fiscaliste has attested this Guide |
| Guide version | 3.0 (September 2026 refresh) |

### Progressive Rate Table (2025 Tranches) [T1]

Applied in 2026 to the income of 2025, on taxable income per family-quotient share: never on gross salary, never on turnover. The tax found for one share is multiplied back by the number of shares, and the top rate is marginal.

| Band, per share | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://www.service-public.fr/particuliers/vosdroits/F1419 |
| Up to EUR 11,600 | 0% | Jusqu'à 11 600 € |
| EUR 11,601 to EUR 29,579 | 11% | De 11 601 € à 29 579 € |
| EUR 29,580 to EUR 84,577 | 30% | De 29 580 € à 84 577 € |
| EUR 84,578 to EUR 181,917 | 41% | De 84 578 € à 181 917 € |
| Above EUR 181,917 | 45% | Plus de 181 917 € |

### Micro-Entrepreneur / Auto-Entrepreneur Abattements [T1]

The allowance replaces every actual expense: nothing else is deducted, and Urssaf contributions are never subtracted.

| Activity | Flat allowance | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F23267 |
| Goods and accommodation, other than furnished tourist lets | 71% | abattement est de 71 % |
| Commercial services taxed as BIC | 50% | abattement est de 50 % |
| Liberal and other non-commercial activity (BNC) | 34% | abattement est de 34 % |
| Classified furnished tourist lets, income of 2025 | 50% | déclarés en 2026 : il s’élève à 50 % |
| Unclassified furnished tourist lets, income of 2025 | 30% | déclarés en 2026 : il s’élève à 30 % |
| Minimum allowance, any activity | EUR 305 | pas être inférieur à 305 € |
| Minimum allowance, mixed activity | EUR 610 | minimal est doublé et passe à 610 € |

Taxable profit is the gross receipts cashed in the year less the allowance above, with the floor applied. Declare the gross on form 2042-C-PRO: the tax office applies the allowance.

### Micro-Entrepreneur Revenue Thresholds (2025) [T1]

Two pairs of limits are live at once: the lower pair governs income received in 2025 and declared in 2026, the higher pair income received in 2026.

| Limit | Amount | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F23267 |
| Goods, income of 2025 | EUR 188,700 | pas avoir dépassé 188 700 € |
| Services and liberal activity, income of 2025 | EUR 77,700 | pas avoir dépassé 77 700 € |
| Goods, income received in 2026 | EUR 203,100 | n’a pas dépassé 203 100 € |
| Services and liberal activity, income received in 2026 | EUR 83,600 | n’a pas dépassé 83 600 € |
| Classified furnished tourist lets and chambres d'hôtes, income of 2025 | EUR 77,700 | de location de meublés de tourisme classés ne doit pas avoir dépassé 77 700 € |
| Classified furnished tourist lets and chambres d'hôtes, income received in 2026 | EUR 83,600 | Meublé de tourisme classé et chambre d'hôtes (BIC) … n’a pas dépassé 83 600 € |
| Unclassified furnished tourist lets | EUR 15,000 | n’a pas dépassé 15 000 € |
| Reference income of year N-2 to opt for the flat payment, single | EUR 29,579 | 29 579 € pour une personne seule |
| Reference income of year N-2, couple in the same household | EUR 59,158 | 59 158 € pour une personne en couple |
| Reference income of year N-2, couple with one child in the same household | EUR 73,947.5 | 73 947,5 € pour une personne en couple avec 1 enfant |
| Reference income of year N-2, couple with two children in the same household | EUR 88,737 | 88 737 € pour une personne en couple avec 2 enfants |
| Flat income tax payment, trade, catering and lodging, other than furnished lets | 1% | 1 % pour les activités de commerce, restauration et logement (sauf location de meublés) |
| Flat income tax payment, other BIC activities, including commercial services and classified furnished lets | 1.7% | 1,7 % pour les autres activités relevant des BIC (notamment prestations de services commerciales, location de meublés classés...) |
| Flat income tax payment, BNC activities | 2.2% | ce taux est de 2,2 % |

**Crossing a limit once does not end the regime.** Income from 1 January of year N leaves the micro regime only if a limit was exceeded in **both** previous years, N-1 and N-2: "dépassé pendant 2 années consécutives, en N-1 et en N-2".

The flat income tax payment (versement forfaitaire libératoire) is an option, not the default. It is paid with the Urssaf turnover declaration each month or quarter at the rates above and replaces the income tax on that turnover, if the household reference income of year N-2 is below the limit above. The option is taken, and given up, by telling Urssaf: before 30 September of the year before the one in which it is to start or to stop, or, for a business created during the year, before the last day of the third month after it was created.

### Conservative Defaults [T1]

| Ambiguity | Default |
| --- | --- |
| Regime unknown | Micro-entrepreneur, then test both limits above |
| Activity type unknown | Liberal profession (BNC), the smallest allowance |
| Parts familiales unknown | 1 part (single) |
| Crédit d'impôt eligibility unknown | No credit applied |
| Withholding rate unknown | Ask for the rate in the client's espace particulier; do not guess |

## Section 2: Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable**: Bank statement for the full calendar year; the regime (micro or réel) and the activity type (BIC ventes, BIC services, BNC).
- **Recommended**: Urssaf turnover declarations, client invoices, Urssaf receipts, and the prior avis d'imposition showing the revenu fiscal de référence.
- **Ideal**: Full comptabilité for a réel filer, pièces justificatives for every expense, the family situation, and the withholding rate and instalments in the espace particulier.

### Refusal Catalogue

- **R-FR-1**: Corporate entities file Impôt sur les Sociétés (IS). Out of scope. (Sociétés (SARL, SAS, SA, etc.))  _(R-FR-1)_
- **R-FR-2**: Non-resident taxation uses different rates, withholding and treaty analysis. Out of scope: escalate. (Non-residents with French income)  _(R-FR-2)_
- **R-FR-3**: Régime réel with depreciation, asset registers and full accounting needs an Expert-Comptable. This Guide handles the micro allowance method and basic BNC déclaration contrôlée. (Régime réel simplifié / normal (complex))  _(R-FR-3)_
- **R-FR-4**: Capital gains on securities, real estate or business assets need specialist computation. Escalate. (Plus-values (capital gains))  _(R-FR-4)_
- **R-FR-5**: Double taxation treaty analysis with non-French income is outside scope. Escalate. (Foreign income and DTAA)  _(R-FR-5)_

## Section 3: Transaction Pattern Library

The deterministic pre-classifier. When a statement line matches, apply the treatment; if nothing matches, fall through to Section 5.

### 3.1 Income Patterns (Crédits)

| Pattern | Tax Line | Treatment and notes |
| --- | --- | --- |
| VIREMENT [client] / VIR [client] | Chiffre d'affaires (CA) / Recettes | Gross receipts: professional fee or service income |
| VIREMENT SEPA [client] | Recettes BNC/BIC | Revenue: standard SEPA transfer from a client |
| STRIPE PAYOUT / STRIPE TRANSFER | Recettes | Revenue: gross back up to the invoiced amount before fees |
| PAYPAL VIREMENT / PAYPAL PAYOUT | Recettes | Revenue: international client payments |
| SUMERIA PAYOUT / LYDIA PRO SETTLEMENT | Recettes | Revenue: fintech payout |
| QONTO VIREMENT ENTRANT | Recettes | Revenue: business account transfer in |
| SHINE PAIEMENT [client] | Recettes | Revenue: business account receipt |
| PAYFIT SALAIRE / VIREMENT SALAIRE [employer] | Traitements et salaires | Not professional income: fiche de paie required |
| AIDES CAF / RSA / ALLOCATIONS | EXCLUDE | CAF benefits are generally not taxable |
| REMBOURSEMENT TVA / CRÉDIT TVA | EXCLUDE | VAT refund, not income |
| REMBOURSEMENT IMPÔTS / TRÉSOR PUBLIC REMB | EXCLUDE | Tax refund, not income |
| PRÊT [bank] / CRÉDIT CONSO | EXCLUDE | Loan proceeds, not income |
| DIVIDENDES [company] | Revenus de capitaux mobiliers | Not professional income: route to `fr-capital-gains` |
| INTÉRÊTS [bank] / LIVRET A | Revenus de capitaux mobiliers | Not professional income: route to `fr-capital-gains` |

### 3.2 Expense Patterns (Débits) Régime Réel Filers Only

| Pattern | Tax Category | Treatment and notes |
| --- | --- | --- |
| LOYER BUREAU / BAIL PROFESSIONNEL | Loyers et charges locatives | Fully deductible: dedicated business premises |
| EDF / ENGIE / ÉLECTRICITÉ | Charges de bureau | Business portion: home office apportioned by floor area |
| FREE / SFR / ORANGE / BOUYGUES (internet) | Frais de télécommunications | Business portion only, mixed use apportioned |
| FREE MOBILE / SFR / ORANGE (mobile) | Frais de télécommunications | Business portion only, mixed use apportioned |
| SNCF / TGV / OUI.SNCF | Frais de déplacement | Deductible if business travel: keep the billets |
| AIR FRANCE / TRANSAVIA / EASY JET | Frais de déplacement | Deductible if business travel |
| RESTAURANT [name] / REPAS AFFAIRES | Frais de repas / réception | Business portion: document purpose and attendees |
| FNAC / AMAZON (books/tech) | Fournitures / matériel | Deductible if professional: split from personal orders |
| ADOBE / MICROSOFT / GOOGLE WORKSPACE | Abonnements logiciels | Fully deductible business software |
| EXPERT-COMPTABLE / COMPTABLE | Honoraires | Fully deductible accounting fees |
| AVOCAT / NOTAIRE | Honoraires | Deductible if the matter is a business matter |
| ASSURANCE RC PRO / MUTUELLE PRO | Assurances professionnelles | Fully deductible professional liability cover |
| URSSAF COTISATIONS | Not an income tax deduction for a micro filer | Social charges sit outside the income tax computation |
| IMPÔT SUR LE REVENU / PRÉLÈVEMENT À LA SOURCE | EXCLUDE | Tax payment, never deductible |
| CFE (COTISATION FONCIÈRE DES ENTREPRISES) | Impôts et taxes professionnelles | Deductible for a réel filer, not for a micro filer |
| MUTUELLE SANTÉ / PRÉVOYANCE | Not a business expense for a micro filer | Madelin deduction for a réel BNC filer only |
| BANQUE FRAIS / FRAIS TENUE DE COMPTE | Frais bancaires | Deductible business account charges |
| STRIPE FEE / PAYPAL FEE | Commissions bancaires | Deductible payment gateway fees |

(Micro-entrepreneurs do NOT deduct actual expenses: the flat allowance covers all of them.)

### 3.3 Urssaf / Social Charges Patterns

| Pattern | Treatment | Notes |
| --- | --- | --- |
| URSSAF PRÉLÈVEMENT / URSSAF AUTO ENTREPRENEUR | Social contributions, not income tax | Charged on gross turnover: rates are in `fr-social-contributions` |
| CIPAV COTISATIONS | Social contributions | Pension fund for the regulated liberal professions attached to it |
| CARPIMKO / CARMF / CARCDSF | Social contributions | Mandatory pension for specific professions |
| PRÉLÈVEMENT À LA SOURCE | Income tax prepayment | Instalment credited against the annual tax |

## Section 4: Worked Examples

Amounts are not printed: what decides each case is the rate or limit in the tables above.

### Example 1: Freelance Professional Fee (BNC Micro)

`15/03/2025 | VIR SEPA ABC CONSULTING SARL | credit`

A client transfer for consulting work, taxpayer under micro-BNC. Taxable income is the gross receipt less the BNC allowance. Urssaf runs separately on the gross receipt and is not deducted again. Declare the gross on form 2042-C-PRO.

### Example 2: Stripe Payout

`22/05/2025 | STRIPE PAYMENTS EUROPE | credit`

The payout arrives net of Stripe's fees. Gross it back up to what the clients paid. For a micro filer, Urssaf and income tax both run on the gross and the fee is not separately deductible; for a réel filer the fee is deductible.

### Example 3: Loyer Bureau Payment

`01/04/2025 | PRÉLÈVEMENT LOYER BUREAU SARL IMMOPRO | debit`

Rent on dedicated professional premises is fully deductible for a réel filer as "loyers et charges locatives". For a micro filer it is not separately deductible.

### Example 4: Urssaf Auto-Entrepreneur Contribution

`15/06/2025 | PRÉLÈVEMENT URSSAF AUTO ENT | debit`

A social contribution debit charged on declared turnover. Not deductible from BIC or BNC income for a micro filer: it reduces cash, not taxable income. Exclude it, and reconcile against the Urssaf account.

### Example 5: Salary Credit (Mixed Income)

`28/02/2025 | VIREMENT SALAIRE SOCIÉTÉ XYZ | credit`

Salary is traitements et salaires, a different category from BIC or BNC. Declared on form 2042 in box 1AJ or 1BJ, with the standard deduction in Section 5.3 unless actual expenses are elected.

### Example 6: Prélèvement à la Source (Monthly Tax Withholding)

`27/01/2025 | PRÉLÈVEMENT FISCAL DGFIP PAS | debit`

No employer withholds for a self-employed person, so the tax office debits instalments computed on the income last declared. They are prepayments, not expenses: sum the year's debits and set the total against the final bill.

## Section 5: Tier 1 Rules (When Data Is Clear)

### 5.1 Micro-Entrepreneur / Micro-BNC / Micro-BIC Regime

- **Legislation**: CGI art. 50-0 for micro-BIC, CGI art. 102 ter for micro-BNC; both declared on form 2042-C-PRO.  _(CGI art. 50-0; CGI art. 102 ter)_
- **Taxable income**: Gross receipts cashed in the year less the flat allowance for the activity, with the floor applied. No actual expense on top.
- **Which limit applies**: Test the turnover of the two previous years against the pair for the income year concerned. One year over a limit does not end the regime.
- **Mixed activity**: Each activity keeps its own allowance rate on its own slice of turnover, and the minimum allowance is doubled.
- **Nil turnover**: The periodic Urssaf declaration is still compulsory: enter "néant".

### 5.2 BNC Régime Réel Simplifié (Déclaration 2035)

A liberal professional above the micro limit, or one who opts out, is under the déclaration contrôlée: form 2035 with annexes 2035-A and 2035-B, no later than 15 days after the second working day following 1 May. Real expenses are deductible: rent, telecommunications on the business share, travel, professional insurance, accounting fees, depreciation, software. Income tax itself is never deductible, and Madelin contributions are.

For BIC the boundaries are turnover based, for income received in 2026:

| Activity | Regime by turnover excluding VAT | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F32919 |
| Goods and accommodation | Réel simplifié, EUR 203,100 to EUR 945,000 | entre 203 100 € et 945 000 € |
| Goods and accommodation | Réel normal above EUR 945,000 | supérieur à 945 000 € |
| Services, including long-term furnished letting | Réel simplifié, EUR 83,600 to EUR 286,000 | entre 83 600 € et 286 000 € |
| Services, including long-term furnished letting | Réel normal above EUR 286,000 | supérieur à 286 000 € |
| Classified furnished tourist lets and chambres d'hôtes | Réel simplifié, EUR 83,600 to EUR 945,000 | compris entre 83 600 € et 945 000 € |
| Unclassified furnished tourist lets | Réel simplifié, EUR 15,000 to EUR 286,000 | compris entre 15 000 € et 286 000 € |

A BIC réel filer files form 2031 with annexes 2033-A to 2033-G (simplified) or 2050 to 2059 (normal). Whichever result return is filed, the result is carried to form 2042-C-PRO in the box for its category. A micro filer files no result return: the turnover goes straight onto form 2042-C-PRO.

### 5.3 Tax Computation Flow

1. Professional result: gross receipts less the flat allowance (micro), or receipts less actual expenses (réel).
2. Add the household's other income: salaries after the standard deduction below, pensions, rental income.
3. Subtract the household's deductible charges (alimony, certain pension contributions) to get the revenu net global.
4. Divide by the number of shares, apply the scale, multiply back, then cap the benefit of the extra shares (Section 6.2).
5. Apply the décote, then the CEHR if the reference income reaches its threshold.
6. Subtract tax reductions and credits, then the instalments already paid.

| Standard deduction on salaries | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/10855-PGP.html/identifiant=BOI-BAREME-000035-20260217 |
| Rate, unless actual expenses are elected | 10% | Déduction forfaitaire de 10 % |
| Minimum per person, income of 2025 | EUR 509 | Minimum |
| Ceiling per person, income of 2025 | EUR 14,555 | Plafond |

The contribution exceptionnelle sur les hauts revenus sits on top of the scale, on slices of the household's revenu fiscal de référence:

| Slice of reference income | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/7804-PGP.html/identifiant=BOI-IR-CHR-20170711 |
| Above EUR 250,000, single, widowed, separated, divorced | 3% | fraction de revenu fiscal de référence supérieure à 250 000 € |
| Above EUR 500,000, single, widowed, separated, divorced | 4% | supérieure à 500 000 € pour les contribuables célibataires |
| Above EUR 500,000, couple taxed jointly | 3% | 3 % à la fraction de revenu fiscal de référence |
| Above EUR 1,000,000, couple taxed jointly | 4% | supérieure à 1 000 000 € pour les contribuables soumis à imposition commune |

A second surcharge, the contribution différentielle sur les hauts revenus, can apply from the same reference-income levels where the household's average rate is low. Its formula is in `fr-personal-income-tax`.

### 5.4 Prélèvement à la Source (PAS) Monthly Withholding

An employee or pensioner has tax withheld by the payer. A self-employed person, a farmer, and anyone with rental income, alimony or foreign income pays instead by instalments (acomptes) debited by the tax office each month, or every three months where the taxpayer opts with the service des impôts des entreprises by the date in Section 5.6. They are computed on the income declared the year before, so a business in its first year has no instalment computed from a declared figure; check the espace particulier for what is actually programmed. The personalised rate is recalculated each September from the spring return, and a married or PACS couple taxed jointly gets an individualised rate automatically. It applies only to each spouse's own income; the household's common income stays on the household rate.

Where no personalised rate exists, a default grid applies to the monthly base. The page below prints it in full in three versions: metropolitan France and abroad, Guadeloupe with La Réunion and Martinique, and Guyane with Mayotte. The extremes of the metropolitan grid:

| Monthly base, metropolitan grid from 1 May 2026 | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/11255-PGP.html |
| Below EUR 1,635 | 0% | Inférieure à 1 635 euros 0 % |
| EUR 1,635 to EUR 1,698 | 0.5% | inférieure à 1 698 euros 0,5 % |
| EUR 55,558 and above | 43% | égale à 55 558 euros 43 % |

A micro-entrepreneur who opted for the flat payment pays the tax with the Urssaf turnover declaration instead, and must switch off any instalment already programmed in the espace particulier.

| Balance after the spring return | Collection | Note |
| --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/les-modalites-de-la-declaration-de-revenus-en-2026 |
| Below EUR 300 | One debit in September 2026 | un seul prélèvement en septembre 2026 |
| Above that amount | Four monthly debits, September to December | quatre prélèvements mensuels |

### 5.5 Cotisation Foncière des Entreprises (CFE)

Local business property tax, due by the self-employed including micro-entrepreneurs. Deductible for a réel filer, not for a micro filer. Base, exemptions and payment date are in `fr-cfe`. Each commune sets its own minimum base within a statutory range, so never state a single CFE amount.

### 5.6 Filing Deadlines

| Item | Deadline | Note |
| --- | --- | --- |
| Source | the filing dates below | https://www.impots.gouv.fr/les-modalites-de-la-declaration-de-revenus-en-2026 |
| Online, départements 01 to 19 and non-residents | Thursday 21 May 2026, 23h59 | jeudi 21 mai au plus tard |
| Online, départements 20 to 54 | Thursday 28 May 2026, 23h59 | jeudi 28 mai au plus tard |
| Online, départements 55 to 974 and 976 | Thursday 4 June 2026, 23h59 | jeudi 4 juin au plus tard |
| Paper return, including residents abroad | Tuesday 19 May 2026, midnight | mardi 19 mai 2026 à minuit |
| Correcting an online return after the avis | Mid-August to mid-December 2026 | Corriger ma déclaration en ligne |
| Result return of a réel filer (2031, 2035) | 15 days after the second working day following 1 May | au plus tard 15 jours après le 2 e jour ouvré suivant le 1 er mai (F32105, F32919) |
| Urssaf turnover declaration (micro) | Monthly or quarterly, as opted | déposée auprès de l’Urssaf chaque mois ou trimestre (selon la périodicité choisie) (F23267) |
| Source | acompte and instalment-option dates below | https://entreprendre.service-public.fr/vosdroits/F32105 |
| Monthly acompte of a self-employed filer | The 15th of each month | au plus tard le 15 du mois |
| Quarterly acompte, where the option is taken | 15 February, 15 May, 15 August, 15 November | au plus tard le 15 février, le 15 mai, le 15 août et le 15 novembre |
| Taking or ending the option for quarterly acomptes | 1 October of the year before | opter au plus tard le 1 er octobre de l'année précédent |

Online filing is the rule where the home has internet access.

### 5.7 Penalties

| Offence | Surcharge | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/4911-PGP.html |
| Return filed late | 10% | la majoration de 10 % prévue par l’article 1728 |
| Deliberate breach (manquement délibéré) | 40% | la majoration de 40 % pour manquement délibéré |
| Abuse of law as main beneficiary, fraudulent manoeuvres, concealment | 80% | 80 % sur les droits résultant des rappels |

| Charge | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/1458-PGP.html |
| Late payment interest, per month of delay | 0.2% | intérêt de retard de 0,2 % par mois |

Late payment interest is not a penalty: it is due on top of any surcharge.

## Section 6: Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Regime Optimisation (Micro vs Réel)

Micro is simpler, not always cheaper. Réel wins when real costs exceed the flat allowance, so compare actual costs against the allowance rate in the abattement table. The option for the déclaration contrôlée is made within the time allowed for filing the return of the year to be taxed that way. Flag for the reviewer to compute both.

### 6.2 Quotient Familial (Family Quotient)

A single person has 1 share, a couple taxed jointly 2 shares, with extra shares for dependants. The benefit of the extra shares is capped, and the cap depends on the kind of share:

| Cap on the tax saving, income of 2025 | Amount | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/2494-PGP.html/identifiant=BOI-IR-LIQ-20-20-20-20260407 |
| Each extra half-share for a dependent child | EUR 1,807 | fixé à 1 807 € par demi-part supplémentaire |
| Each extra half-share for a child in equally shared custody | Half of the amount above | Ce montant est divisé par deux pour les enfants dont la charge est également partagée |
| The whole extra share for the first child of a parent living alone | EUR 4,262 | Son montant est fixé à 4 262 € |
| Each half-share for the first two children in equally shared custody, taxpayer living alone | EUR 2,131 | soit 2 131 € (4 262 € / 2) |
| The extra half-share of a person living alone with no dependants who raised a child alone for at least five years | EUR 1,079 | est fixé à 1 079 € |

The number of shares itself is on https://www.service-public.fr/particuliers/vosdroits/F2705

A small bill is then reduced by the décote. It works on the tax, not on the income, and it fades out: the décote is the fixed amount in the table below, less the share of the gross tax in the table below, so it shrinks to nothing as the gross tax reaches the threshold.

| Décote, income of 2025 | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/2495-PGP.html/identifiant=BOI-IR-LIQ-20-20-30-20260407 |
| Gross tax must be below this, single, divorced, widowed | EUR 1,982 | inférieure à 1 982 € pour les contribuables célibataires |
| Gross tax must be below this, couple taxed jointly | EUR 3,277 | et à 3 277 € pour les contribuables soumis à imposition commune |
| Fixed amount in the formula, single, divorced, widowed | EUR 897 | 897 € pour les contribuables célibataires |
| Fixed amount in the formula, couple taxed jointly | EUR 1,483 | 1 483 € pour les contribuables soumis à imposition commune |
| Share of the gross tax subtracted from that fixed amount | 45.25% | 45,25 % pour l’imposition des revenus de 2025 |

### 6.3 Crédits d'Impôt (Tax Credits)

Credits are subtracted from the tax, never from the income.

| Employing help at home | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.service-public.fr/particuliers/vosdroits/F12 |
| Rate of the credit | 50% | s'élève à 50 % des dépenses supportées |
| Annual ceiling on the expenses, general case | EUR 12,000 | dans la limite de 12 000 € par an |
| Maximum credit, general case | EUR 6,000 | un avantage maximal de 6 000 € |
| Uplift per dependent child, per household member over 65, per ascendant | EUR 1,500 | plafond est majoré de 1 500 € |
| Ceiling once the uplifts are counted, general case | EUR 15,000 | sans pouvoir dépasser au total 15 000 € |
| Uplift per dependent child in equally shared custody | EUR 750 | 750 € en cas de garde alternée |
| Small handyman work of at most two hours, inside the ceiling above | EUR 500 | Intervention pour petit bricolage d'une durée maximale de 2 heures 500 € |
| Computer and internet help at home, inside the ceiling above | EUR 3,000 | Assistance informatique et internet à domicile 3 000 € |
| Small gardening work, inside the ceiling above | EUR 5,000 | Petits travaux de jardinage 5 000 € |
| Ceiling on the expenses, first year of directly employing someone at home | EUR 15,000 | Pour la 1 re année où vous employez directement un salarié à domicile, les dépenses sont retenues dans la limite de 15 000 € |
| Maximum credit, first year of directly employing someone at home | EUR 7,500 | soit un avantage maximal de 7 500 € |
| Ceiling on the expenses, taxpayer or dependant invalid | EUR 20,000 | Les dépenses sont retenues dans la limite de 20 000 € par an |
| Maximum credit, taxpayer or dependant invalid | EUR 10,000 | soit un avantage maximal de 10 000 € |

Aid received towards the cost, such as the personalised autonomy allowance, the childcare supplement or help from an employer, comes off the expenses before the credit is worked out.

| Childcare outside the home, child under 6 on 1 January of the tax year | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.service-public.fr/particuliers/vosdroits/F8 |
| Rate of the credit | 50% | égal à 50 % des sommes versées |
| Costs that may be declared, per child | EUR 3,500 | Frais de garde à déclarer 3 500 € maximum |
| Costs that may be declared, per child in equally shared custody | EUR 1,750 | Frais de garde à déclarer … 1 750 € maximum |
| Maximum credit, per child | EUR 1,750 | Crédit d'impôt 1 750 € maximum |
| Maximum credit, per child in shared custody | EUR 875 | 875 € maximum |

Aid received for the childcare, such as the childcare supplement paid by the family allowance fund or help from an employer, comes off the costs first.

**The credit for training a company director has ended**, for training taken after 31 December 2024, with no extension in force: https://entreprendre.service-public.fr/vosdroits/F23460

### 6.4 Madelin Deductions (Régime Réel BNC Only)

Madelin health, disability, provident and pension contributions are deductible from BNC income for a réel filer, within the ceilings of CGI art. 154 bis. Not available to a micro-entrepreneur. This Guide does not print the ceiling formula: flag it for the reviewer.

### 6.5 Home Office Deduction (Régime Réel)

For a réel BNC filer working from home, a share of rent, electricity, internet and heating may be deducted on the floor-area ratio of the office to the whole home. Document it and keep it consistent year to year.

## Section 7: Excel Working Paper Template

~~~
IMPÔT SUR LE REVENU, WORKING PAPER, INCOME OF 2025.
Contribuable: _______________  Numéro fiscal: ___________
Régime: Micro-entrepreneur (BNC/BIC) / Régime réel (BNC) [circle one]
Situation familiale: Célibataire / Marié(e) / PACS / Divorcé(e) / Veuf(ve)
Nombre de parts: ___________

A. REVENUS PROFESSIONNELS.
  A1. CA brut encaissé (micro)                 ___________
  A2. Abattement (rate from the table)         ___________
  A3. Revenu net imposable (A1 minus A2)       ___________
  A4. Recettes brutes (réel, form 2035)        ___________
  A5. Total charges déductibles                ___________
  A6. Revenu net imposable (A4 minus A5)       ___________

B. AUTRES REVENUS.
  B1. Salaires bruts (box 1AJ / 1BJ)           ___________
  B2. Moins déduction forfaitaire (see 5.3)    ___________
  B3. Salaires nets imposables                 ___________
  B4. Pensions de retraite                     ___________
  B5. Revenus fonciers                         ___________
  B6. Total autres revenus                     ___________

C. REVENU BRUT GLOBAL (A3 or A6, plus B6)      ___________

D. CHARGES DÉDUCTIBLES.
  D1. Pensions alimentaires versées            ___________
  D2. Autres charges                           ___________

E. REVENU NET GLOBAL (C minus D)               ___________

F. QUOTIENT FAMILIAL.
  F1. Revenu imposable par part (E / parts)    ___________
  F2. Impôt sur E/parts (apply the scale)      ___________
  F3. Impôt total (F2 times parts)             ___________
  F4. Plafonnement du quotient (see 6.2)       ___________
  F5. Décote if the tax is below the threshold ___________

G. RÉDUCTIONS / CRÉDITS D'IMPÔT.
  G1. Emploi à domicile                        ___________
  G2. Garde d'enfants hors du domicile         ___________
  G3. Autres crédits                           ___________

H. IMPÔT NET (F3, adjusted, minus G)           ___________

I. ACOMPTES ET RETENUES DÉJÀ PRÉLEVÉS          ___________

J. SOLDE À PAYER / À REMBOURSER (H minus I)    ___________

REVIEWER FLAGS.
  [ ] Regime confirmed (micro vs réel)?
  [ ] Turnover tested against BOTH previous years?
  [ ] Number of parts verified?
  [ ] Urssaf reconciled, and NOT deducted for income tax?
  [ ] Instalments summed from the bank statement?
  [ ] Crédits d'impôt identified?
  [ ] Madelin deductions applicable (réel BNC only)?
~~~

## Section 8: Bank Statement Reading Guide

### French Bank Statement Formats

| Bank | Format | Key Fields |
| --- | --- | --- |
| BNP Paribas | CSV / PDF | Date opération, Libellé, Débit, Crédit, Solde |
| Société Générale | CSV | Date, Libellé, Montant, Devise |
| Crédit Agricole | CSV | Date, Libellé, Débit, Crédit, Solde |
| LCL | CSV / PDF | Date, Libellé, Débit, Crédit, Solde |
| Crédit Mutuel | CSV | Date, Libellé, Montant (negative is a debit) |
| Caisse d'Épargne | CSV | Date de l'opération, Libellé, Montant, Devise |
| Boursorama / BoursoBank | CSV | Date, Catégorie, Label, Débit, Crédit |
| Qonto (business) | CSV | Date, Label, Amount, Currency, VAT, Category |
| Shine | CSV | Date, Libellé, Montant, Solde |
| Revolut FR | CSV | Date started, Description, Amount, Currency |

### Key French Banking Narrations

| Narration | Meaning | Classification Hint |
| --- | --- | --- |
| VIR SEPA / VIREMENT | Bank transfer credit | Potential professional income |
| PRÉLÈVEMENT / PRÉLÈV | Direct debit | Expense or tax payment |
| PRÉLÈVEMENT FISCAL DGFIP PAS | Prélèvement à la source | Tax prepayment: exclude |
| PRÉLÈVEMENT URSSAF | Social charge payment | Separate Urssaf tracking |
| CB [merchant] | Card payment | Identify payee |
| VIREMENT SALAIRE [employer] | Salary credit | Employment income |
| REMBOURSEMENT / REMB | Refund | May reduce expense |
| INTÉRÊTS | Interest | Other income |
| AIDES CAF / ALLOCATION | Social benefits | Generally not taxable |

## Section 9: Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all VIR SEPA credits from non-personal sources as potential professional income
2. Identify all URSSAF PRÉLÈVEMENT debits: social charges, not income tax
3. Identify all DGFIP prélèvement à la source debits: income tax instalments
4. Apply the conservative defaults in Section 1
5. Flag all salary credits as a separate income category
6. Generate the working paper with PENDING flags

Present these questions:

~~~
ONBOARDING QUESTIONS: FRANCE, IMPÔT SUR LE REVENU.
1. Régime fiscal: micro-entrepreneur (auto-entrepreneur) or régime réel?
2. Type d'activité: BNC (professions libérales), BIC ventes, or BIC services?
3. Total CA brut encaissé (before any Urssaf deduction)?
4. CA of the two previous years, to test the micro limits?
5. Situation familiale: célibataire, marié(e)/PACS, enfants?
6. Aussi salarié(e)? Si oui, salaire brut total?
7. Option pour le versement forfaitaire libératoire: oui ou non?
8. Montant des acomptes déjà prélevés par la DGFiP?
9. Avez-vous un Expert-Comptable qui prépare la déclaration 2035?
10. Charges Madelin payées (mutuelle santé, prévoyance)?
11. Crédits d'impôt potentiels (garde d'enfants, emploi à domicile)?
~~~

## Section 10: Reference Material

### Key Legislation / Forms

| Topic | Reference |
| --- | --- |
| Micro-BNC | CGI art. 102 ter; form 2042-C-PRO |
| Micro-BIC | CGI art. 50-0; form 2042-C-PRO |
| BNC déclaration contrôlée | CGI art. 93; form 2035 with annexes 2035-A, 2035-B |
| BIC réel simplifié | Form 2031 with annexes 2033-A to 2033-G |
| BIC réel normal | Form 2031 with annexes 2050 to 2059 |
| Progressive rates | CGI art. 197 |
| Quotient familial | CGI art. 193 to 196 B |
| CEHR | CGI art. 223 sexies |
| Prélèvement à la source | CGI art. 204 A and following |
| Crédit emploi à domicile | CGI art. 199 sexdecies |
| Crédit garde d'enfants | CGI art. 200 quater B |
| Madelin | CGI art. 154 bis |

Declaration forms for each millésime, including 2042, 2042-C, 2042-C-PRO and 2042-RICI: https://www.impots.gouv.fr/formulaire/2042/declaration-des-revenus

### Known Gaps / Out of Scope

- Corporate taxation (IS)
- Non-resident French-source income
- Capital gains and investment income, including the flat tax on dividends and interest
- SCI / real estate entities
- Foreign income and DTAA
- TVA (VAT) computation
- Social contribution rates and bases: see `fr-social-contributions`

### Changelog

| Version | Date | Change |
| --- | --- | --- |
| 3.0 | September 2026 | Every figure reproved on an official page; withholding grid, réel boundaries and the two-year micro test added; invented example amounts removed |
| 2.0 | April 2026 | Full rewrite to v2.0 structure; French bank formats; worked examples; micro vs réel regime table |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] Allowance applied to gross receipts, not to receipts net of Urssaf?
- [ ] Urssaf contributions NOT subtracted as an income tax deduction for a micro filer?
- [ ] Micro limits tested against BOTH previous years, and the right year's pair used?
- [ ] Instalments identified as prepayments, not expenses?
- [ ] Quotient familial computed, and its cap applied?
- [ ] Décote checked before credits?
- [ ] CEHR checked where the reference income is high?
- [ ] Credits applied against the tax, not the income?

## PROHIBITIONS

- NEVER deduct Urssaf social contributions as a business expense for a micro-entrepreneur: the allowance covers all costs
- NEVER compute a micro-entrepreneur's taxable income without applying the allowance
- NEVER treat a prélèvement à la source instalment as a deductible expense: it is a prepayment
- NEVER end the micro regime on a single year over the limit: the test is two consecutive years
- NEVER mix the two live sets of micro limits: name the income year first
- NEVER omit the quotient familial for a taxpayer with a spouse or children, and never omit its cap
- NEVER allow income tax itself as a deductible expense
- NEVER advise on non-resident French income: escalate
- NEVER present a computation as definitive: label it estimated and send the client to an Expert-Comptable

## The method, step by step

1. Fix the income year and the regime, then read the matching pair of micro limits, tested against the two previous years: https://entreprendre.service-public.fr/vosdroits/F23267
2. Classify the activity: commercial, craft and industrial work is BIC, independent work that is none of those is BNC. BIC boundaries: https://entreprendre.service-public.fr/vosdroits/F32919 . BNC rule: https://entreprendre.service-public.fr/vosdroits/F32105
3. Compute the professional result: gross receipts less the allowance (micro), or receipts less actual expenses on form 2035 for BNC or form 2031 for BIC (réel).
4. Build the household income, divide by the shares, apply the scale, multiply back, then cap the benefit of the extra shares: https://www.service-public.fr/particuliers/vosdroits/F1419
5. Apply the décote, then the CEHR where the reference income reaches its threshold, then the credits.
6. Deduct the instalments already taken and settle the balance on the autumn schedule: https://www.impots.gouv.fr/les-modalites-de-la-declaration-de-revenus-en-2026
7. File form 2042 with 2042-C-PRO by the deadline for the client's département, and a réel filer's result return by its own earlier deadline.

## Ask the client first

- Which regime are you in, and did you ever opt out of micro? The option changes the whole computation.
- What was your turnover, excluding VAT, in each of the two previous years? One year over a limit does not lose the micro regime; two consecutive years does.
- Is any part of the turnover furnished letting, and is the property a classified meublé de tourisme? The limit and the allowance both change.
- Have you opted for the flat income tax payment with Urssaf? If yes, the instalment must be switched off.
- What is your family situation on 31 December, and who is a dependant?
- Are you also employed, and did you keep a household rate or an individualised rate for the withholding?
- What did the tax office debit last year, and what rate shows in your espace particulier?

## When to refuse or refer

- Refuse a company subject to corporation tax: this Guide is for individuals under the income tax.
- Refuse non-resident cases: different rates, different withholding, treaty analysis.
- Refuse capital gains and the taxation of dividends and interest: separate rules, separate Guides.
- Refer a réel filer with depreciation, an asset register or stock to an Expert-Comptable before filing.
- Refer any Madelin ceiling question: the ceiling formula is not in this Guide.
- Refer anything turning on a CFE amount: the commune sets it and no national figure exists.
- Stop and ask rather than guess a withholding rate or an instalment total: both are in the espace particulier.

## Sources

- https://www.service-public.fr/particuliers/vosdroits/F1419
- https://www.service-public.fr/particuliers/vosdroits/F2705
- https://www.service-public.fr/particuliers/vosdroits/F34009
- https://www.service-public.fr/particuliers/vosdroits/F12
- https://www.service-public.fr/particuliers/vosdroits/F8
- https://entreprendre.service-public.fr/vosdroits/F23267
- https://entreprendre.service-public.fr/vosdroits/F32919
- https://entreprendre.service-public.fr/vosdroits/F32105
- https://entreprendre.service-public.fr/vosdroits/F23460
- https://bofip.impots.gouv.fr/bofip/2494-PGP.html/identifiant=BOI-IR-LIQ-20-20-20-20260407
- https://bofip.impots.gouv.fr/bofip/2495-PGP.html/identifiant=BOI-IR-LIQ-20-20-30-20260407
- https://bofip.impots.gouv.fr/bofip/10855-PGP.html/identifiant=BOI-BAREME-000035-20260217
- https://bofip.impots.gouv.fr/bofip/7804-PGP.html/identifiant=BOI-IR-CHR-20170711
- https://bofip.impots.gouv.fr/bofip/11255-PGP.html
- https://bofip.impots.gouv.fr/bofip/4911-PGP.html
- https://bofip.impots.gouv.fr/bofip/1458-PGP.html
- https://www.impots.gouv.fr/les-modalites-de-la-declaration-de-revenus-en-2026
- https://www.impots.gouv.fr/formulaire/2042/declaration-des-revenus
- https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/lessentiel-du-statut.html

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as an Expert-Comptable, Avocat Fiscaliste, or equivalent licensed practitioner in France) before filing or acting upon.

The most up-to-date version of this Guide is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

> Contributed by OpenAccountants.

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
