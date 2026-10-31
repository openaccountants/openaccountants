---
name: fr-income-tax
description: Use this skill whenever asked about French income tax for self-employed individuals (auto-entrepreneurs, micro-entrepreneurs, or professions libérales). Trigger on phrases like "impôt sur le revenu France", "déclaration 2042", "micro-entrepreneur", "auto-entrepreneur", "BNC", "BIC", "professions libérales France", "abattement forfaitaire", "Urssaf", "cotisations sociales", "régime micro", "régime réel", "IR France", "acomptes provisionnels", "Revenu fiscal de référence", "Crédit d'impôt", "BNP Paribas statement", "Qonto expense", "Shine business", "Stripe France", or any question about filing or computing French income tax for a self-employed individual. This skill covers progressive brackets (0--45%), micro-entrepreneur abattements, BNC/BIC regimes, social charges, tax credits, filing deadlines, and withholding (prélèvement à la source). ALWAYS read this skill before touching any French income tax work.
version: 3.4
jurisdiction: FR
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# French income tax for self-employed individuals (impôt sur le revenu)

France taxes the income of the previous calendar year: the scale applied in 2026 is charged on the income of 2025, declared in spring 2026. Figures are for tax year 2026. Where a limit governs income received in 2026 instead, the table row says so. Urssaf social contributions are a separate charge and are not computed here: use `fr-social-contributions`. Local business property tax is in `fr-cfe`, and the full income tax computation for a household that is not self-employed is in `fr-personal-income-tax`. Selected source conditions were checked on29October2026. The2026 assessment scale below concerns2025 income; do not present it as a final enacted2027 assessment of2026 income.

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
| Guide version | 3.2 (October2026 ledger closeout; earlier version labels remain in the historical changelog) |

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

For the ordinary micro profit, the allowance replaces actual business expenses; do not deduct Urssaf or platform fees again. Use gross turnover/receipts excluding VAT, before those expenses, rather than the net bank payout. Professional asset gains/losses are a separate statutory calculation.

| Activity | Flat allowance | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.fr/vosdroits/F23267 |
| Goods and qualifying accommodation, excluding residential furnished letting | 71% | Apply the precise CGI50-0 activity category; a generic accommodation label is insufficient. |
| Commercial services taxed as BIC | 50% | abattement est de 50 % |
| Liberal and other non-commercial activity (BNC) | 34% | abattement est de 34 % |
| Classified furnished tourist lets, income of 2025 | 50% | déclarés en 2026 : il s’élève à 50 % |
| Unclassified furnished tourist lets, income of 2025 | 30% | déclarés en 2026 : il s’élève à 30 % |
| Minimum allowance, any activity | EUR 305 | pas être inférieur à 305 € |
| Minimum for two applicable allowance categories, each subject to its own EUR305 minimum | EUR 610 in that two-category case | This is not a flat allowance for every business with several activities; identify the statutory categories first. |

Ordinary micro profit is gross eligible turnover/receipts excluding VAT minus the applicable category allowance(s), with the EUR305 minimum applied to the relevant allowance. This method does not create a deficit; do not turn small or nil receipts into a negative taxable micro profit. For mixed activity, apply the relevant rate to each category’s actual slice, not one rate to the whole bank inflow. Declare the gross in the correct2042-C-PRO micro field; the administration applies the allowance. Asset gains/losses remain separate.

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
| Household RFR2024 for the2026 flat-payment option,1part | EUR 29,315 | Actual DGFiP2026 selector; general condition is not exceeding the ceiling. |
| Household RFR2024 for the2026 option, jointly taxed couple2parts | EUR 58,630 | Apply the actual N-2 share count. |
| Household RFR2024 for the2026 option,2.5parts | DGFiP’s published example requires RFR below EUR73,288 | Preserve this published strict example; do not silently replace it with an unqualified rounded or unrounded inequality. |
| Household RFR2024 for the2026 option,3parts | EUR 87,945 | For the2027 option, RFR2025 ceilings are29,579/59,158/88,737 for1/2/3parts; the published2.5part test is below73,948, versus an exact product73,947.50. |
| Flat income tax payment, trade, catering and lodging, other than furnished lets | 1% | 1 % pour les activités de commerce, restauration et logement (sauf location de meublés) |
| Flat income tax payment, other BIC activities, including commercial services and classified furnished lets | 1.7% | 1,7 % pour les autres activités relevant des BIC (notamment prestations de services commerciales, location de meublés classés...) |
| Flat income tax payment, BNC activities | 2.2% | ce taux est de 2,2 % |

**Crossing a limit once does not end the regime.** Income from 1 January of year N leaves the micro regime only if a limit was exceeded in **both** previous years, N-1 and N-2: "dépassé pendant 2 années consécutives, en N-1 et en N-2". Before that two-year comparison, adjust each short reference year’s turnover proportionally to its actual time of operation/activity as required by CGI arts. 50-0 and 102 ter. Compare the adjusted reference amounts, not automatically the raw cash totals. For a services case, independently established adjusted N-2 turnover EUR 120,000 (actual short-year receipts EUR 60,000) and full-year N-1 turnover EUR 100,000 both exceed EUR 83,600, so the 2026 micro gate fails; using unadjusted EUR 60,000 would give the wrong result. The EUR 120,000 here is a stipulated valid adjusted input, not a universal 365-day computation rule. This reference-year gate is distinct from the micro allowance/minimum and from VAT startup turnover rules.

The flat payment (versement forfaitaire libératoire) is an option, not the default. Apply the correct option-year/N-2 RFR and share tests above, the eligible micro and micro-social conditions, and the applicable1%/1.7%/2.2% rate to gross qualifying turnover excluding VAT. Tell Urssaf within the actual option/withdrawal timetable. The Service Public page says “before30September”, while the retained DGFiP method expressly permits option or withdrawal by30September for effect the following1January and by the last day of the third month following creation. Use that precise DGFiP deadline, not its dated2024 numerical threshold examples. Declare the turnover annually in the VFL fields even though IR has been paid through Urssaf: the net amount after the statutory allowance still affects RFR, the effective rate on other household income and the pension-saving ceiling. Do not tax that same micro turnover a second time through the ordinary scale.

### Conservative Defaults [T1]

| Ambiguity | Default |
| --- | --- |
| Regime unknown | Mark PENDING; obtain regime/election evidence and the two prior-year turnover figures before computing. Do not assume micro. |
| Activity type unknown | Mark PENDING; establish the actual activity/category. Do not assume BNC or choose an allowance from a bank label. |
| Parts familiales unknown | Obtain the household/share facts; a provisional1part illustration is not the taxpayer’s determined quotient. |
| Crédit d'impôt eligibility unknown | No credit applied |
| Withholding rate unknown | Ask for the rate in the client's espace particulier; do not guess |

## Section 2: Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable**: Bank statement for the full calendar year; the regime (micro or réel) and the activity type (BIC ventes, BIC services, BNC).
- **Recommended**: Urssaf turnover declarations, client invoices, Urssaf receipts, and the prior avis d'imposition showing the revenu fiscal de référence.
- **Ideal**: Full comptabilité for a réel filer, pièces justificatives for every expense, the family situation, and the withholding rate and instalments in the espace particulier.

### Refusal Catalogue

- **R-FR-1**: An entity actually subject to IS is outside this individual-IR Guide. Legal form alone does not prove IS: establish an IR-company/partner or sole-trader election route before classifying it. _(R-FR-1)_
- **R-FR-2**: Non-resident taxation uses different rates, withholding and treaty analysis. Out of scope: escalate. (Non-residents with French income)  _(R-FR-2)_
- **R-FR-3**: Régime réel with depreciation, asset registers and full accounting needs an Expert-Comptable. This Guide handles the micro allowance method and basic BNC déclaration contrôlée. (Régime réel simplifié / normal (complex))  _(R-FR-3)_
- **R-FR-4**: Capital gains on securities, real estate or business assets need specialist computation. Escalate. (Plus-values (capital gains))  _(R-FR-4)_
- **R-FR-5**: Double taxation treaty analysis with non-French income is outside scope. Escalate. (Foreign income and DTAA)  _(R-FR-5)_

## Section 3: Transaction Pattern Library

These are matching prompts for reconciliation, not automatic tax classifications. Identify the underlying invoice, settlement, loan, transfer, benefit and VAT/accounting basis before applying a treatment. A generic incoming transfer is not itself professional turnover.

### 3.1 Income Patterns (Crédits)

| Pattern | Tax Line | Treatment and notes |
| --- | --- | --- |
| VIREMENT [client] / VIR [client] | Chiffre d'affaires (CA) / Recettes | Gross receipts: professional fee or service income |
| VIREMENT SEPA [client] | Recettes BNC/BIC | Revenue: standard SEPA transfer from a client |
| STRIPE PAYOUT / STRIPE TRANSFER | Recettes | Revenue: gross back up to the invoiced amount before fees |
| PAYPAL VIREMENT / PAYPAL PAYOUT | Recettes | Revenue: international client payments |
| SUMERIA PAYOUT / LYDIA PRO SETTLEMENT | Recettes | Revenue: fintech payout |
| QONTO VIREMENT ENTRANT | PENDING underlying transaction | Could be a customer settlement, own-account transfer, capital or loan; classify from evidence. |
| SHINE PAIEMENT [client] | Recettes | Revenue: business account receipt |
| PAYFIT SALAIRE / VIREMENT SALAIRE [employer] | Traitements et salaires | Not professional income: fiche de paie required |
| AIDES CAF / RSA / ALLOCATIONS | Identify the exact benefit | The label alone does not establish exemption. Separate benefit treatment from taxable salary/replacement income using `fr-personal-income-tax`. |
| REMBOURSEMENT TVA / CRÉDIT TVA | Reconcile the VAT account/basis | Do not automatically treat every VAT refund as outside a real-BNC result without checking the adopted VAT/accounting basis and prior deduction. |
| REMBOURSEMENT IMPÔTS / TRÉSOR PUBLIC REMB | Identify the refunded tax and earlier posting | A refund of personal IR is separate from business revenue; do not extend that classification to every business-tax refund. |
| PRÊT [bank] / CRÉDIT CONSO | EXCLUDE | Loan proceeds, not income |
| DIVIDENDES [company] | Revenus de capitaux mobiliers | Not professional income: route to `fr-capital-gains` |
| INTÉRÊTS [bank] / LIVRET A | Separate investment/regulated-account analysis | Do not infer taxable interest from a bank label; use `fr-capital-gains` for the actual account and exemption. |

### 3.2 Expense Matching Prompts: Actual Real-Regime Conditions

For BNC, start from expenses necessitated by the profession, with actual evidence and the applicable paid/engaged timing. BIC has its separate actual-results rules. The descriptions below prompt a check; they do not make every bank debit deductible or turn capital expenditure into a current expense. Apply the asset and depreciation method in `france-bookkeeping` where relevant.

| Pattern | Tax Category | Treatment and notes |
| --- | --- | --- |
| LOYER BUREAU / BAIL PROFESSIONNEL | Professional rent | For BNC, actual paid rent/related charges qualify subject to the premises, use and statutory limits; mixed-use rent requires supported allocation. No automatic deduction from the label. |
| EDF / ENGIE / ÉLECTRICITÉ | Professional utilities portion | Establish actual professional use and evidence. The practical floor-area rent rule is not a universal fixed percentage for every utility bill. |
| FREE / SFR / ORANGE / BOUYGUES (internet) | Frais de télécommunications | Business portion only, mixed use apportioned |
| FREE MOBILE / SFR / ORANGE (mobile) | Frais de télécommunications | Business portion only, mixed use apportioned |
| SNCF / TGV / OUI.SNCF | Frais de déplacement | Deductible if business travel: keep the billets |
| AIR FRANCE / TRANSAVIA / EASY JET | Frais de déplacement | Deductible if business travel |
| RESTAURANT [name] / REPAS AFFAIRES | Distinguish business hospitality from the proprietor’s own extra meal cost | Business/client meals need a direct professional connection, actual justification and a normal amount. Own extra meals have the separate distance, necessity, private-home-meal and excessive-cost conditions described below. |
| FNAC / AMAZON (books/tech) | Professional materials or asset | Identify the purchased item, private portion and actual expense-versus-capital treatment; a merchant name is not an automatic current deduction. |
| ADOBE / MICROSOFT / GOOGLE WORKSPACE | Software subscription/licence or asset | Identify professional use, contract period and whether the transaction is a current service or capital item. Do not expense every software-labelled payment automatically. |
| EXPERT-COMPTABLE / COMPTABLE | Professional fees | Establish actual professional service, evidence and recognition period; payment alone does not prove the whole amount qualifies. |
| AVOCAT / NOTAIRE | Honoraires | Deductible if the matter is a business matter |
| ASSURANCE RC PRO / MUTUELLE PRO | Classify the insured risk | BNC professional-liability premiums are deductible under the actual professional-risk rule. Health/provident cover is a different CGI154bis eligibility/ceiling test, not interchangeable with RC professionnelle. |
| URSSAF COTISATIONS | Separate components and actual regime | No extra deduction for a micro filer. For a real filer, apply the compulsory/optional contribution provisions and the actual CSG/CRDS treatment; do not deduct every item on an Urssaf debit indiscriminately. |
| IMPÔT SUR LE REVENU / PRÉLÈVEMENT À LA SOURCE | EXCLUDE | Tax payment, never deductible |
| CFE (COTISATION FONCIÈRE DES ENTREPRISES) | Professional-tax posting | Establish the actual CFE and real-regime treatment with `fr-cfe`; a micro filer has no second deduction on top of the allowance. |
| MUTUELLE SANTÉ / PRÉVOYANCE | No extra micro expense deduction | For a real filer, test the actual qualifying contract and CGI154bis conditions/limits; this provision covers qualifying BIC as well as BNC. |
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

The six historical fictional bank-line amounts, dates and balances below are retained from the actual pre-refresh Guide. They are declared example inputs, not official figures or actual client records. The existing explanations are preserved; the added computations distinguish cash reconciliation, annual taxable categories, outdated results and unproved facts.

### Example 1: Freelance Professional Fee (BNC Micro)

`15/03/2025 | VIR SEPA ABC CONSULTING SARL | +3,500.00 | Solde 12,840.50`

Historical fictional amount restored: assume this EUR 3,500 is the entire annual eligible gross micro-BNC receipt, no VAT or fees in this receipt, no other category turnover and no VFL. The 34% allowance is EUR 1,190, above its EUR 305 minimum; taxable micro profit is EUR 2,310. If this were only one receipt among others, compute the allowance/minimum on the annual category total instead of applying an annual minimum separately per bank line. The former approximate EUR 770 social figure is historical and is not a current rate calculation; actual dated social liability is separate.

A supported client settlement for consulting work, taxpayer under micro-BNC. Use gross eligible receipts excluding VAT before fees/Urssaf, then the34% allowance with its minimum and no-deficit rule. Urssaf remains separate and is not deducted again. Declare the gross in the appropriate2042-C-PRO field; a valid VFL option follows its separate method.

### Example 2: Stripe Payout

`22/05/2025 | STRIPE PAYMENTS EUROPE | +4,650.00 | Solde 8,220.00`

Historical fictional reconciliation restored: independently verified eligible client receipts EUR 4,800 less actual platform fees EUR 150 equal the EUR 4,650 bank payout. Assume no separate VAT/refund adjustment on these inputs. The micro turnover input is EUR 4,800, with no additional EUR 150 fee deduction. A real filer still tests that actual fee’s professional purpose and timing; this receipt does not by itself establish the full annual taxable result.

The payout is net of platform fees. Reconcile it to the settlement report, actual client receipts, VAT and refunds; the bank net alone is not turnover. A micro filer declares the gross eligible amount excluding VAT before fees, with no second fee deduction. A real filer applies its actual expense/evidence and timing rules rather than automatically deducting every platform debit.

### Example 3: Loyer Bureau Payment

`01/04/2025 | PRÉLÈVEMENT VIREMENT LOYER BUREAU SARL IMMOPRO | -1,200.00 | Solde 5,640.00`

Historical fictional EUR 1,200 monthly rent is retained. If the full EUR 1,200 is actually paid eligible rent for dedicated professional BNC premises under the applicable recognition method, the potential professional deduction is EUR 1,200. If mixed/private use or another statutory restriction applies, recompute; for a micro filer the separate rent deduction is zero.

Rent on dedicated professional premises is tested as a professional expense under the actual real regime, evidence and recognition period; the payment label alone is not the test. A micro filer cannot deduct the rent again on top of the allowance.

### Example 4: Urssaf Auto-Entrepreneur Contribution

`15/06/2025 | PRÉLÈVEMENT URSSAF AUTO ENT | -528.00 | Solde 4,210.00`

The historical fictional EUR 528 debit remains a cash/social-account reconciliation input. For a micro filer, the additional business-expense deduction from that debit is zero; EUR 528 is not proof of a current contribution rate or of the turnover period that produced it.

A social contribution debit charged on declared turnover. Not deductible from BIC or BNC income for a micro filer: it reduces cash, not taxable income. Exclude it, and reconcile against the Urssaf account.

### Example 5: Salary Credit (Mixed Income)

`28/02/2025 | VIREMENT SALAIRE SOCIÉTÉ XYZ | +2,800.00 | Solde 6,150.00`

The historical fictional EUR 2,800 bank credit and EUR 6,150 balance are retained as cash inputs. They do not establish gross salary or annual net taxable salary. No annual salary deduction or 1AJ/1BJ amount is computed without the actual payroll/annual taxable statement; the old EUR 504/EUR 14,171 salary limits are superseded by the year-specific table above.

Salary is traitements et salaires, separate from BIC/BNC. Reconcile the bank net to the annual net taxable salary before the professional-expense deduction, ordinarily reported in1AJ/1BJ. Apply the10% deduction or the actual-expense election to that taxable base, not gross contractual pay or the cash received after withholding.

### Example 6: Prélèvement à la Source (Monthly Tax Withholding)

`27/01/2025 | PRÉLÈVEMENT FISCAL DGFIP PAS | -420.00 | Solde 7,890.00`

The historical fictional EUR 420 debit is retained. Only if twelve independently reconciled EUR 420 instalments belong to the same assessed income year is the credit total 420 × 12 = EUR 5,040. One January bank debit does not prove that annual total, and none of it is a professional-expense deduction.

The business-income acompte is collected directly by the tax administration; any separate employment still has payer withholding. Use the actual programmed instalments and reconciled annual tax records, including any VFL change. These debits are prepayments, not business expenses; offset the correct income-year amounts against the final bill.

```oa-check
name: France restored annual microBNC3500 receipt
inputs:
  annual_receipts: 3500
  allowance_rate: 0.34
  minimum_allowance: 305
steps:
  allowance: min(annual_receipts,max(annual_receipts*allowance_rate,minimum_allowance))
  taxable_micro: max(annual_receipts-allowance,0)
expected:
  allowance: 1190
  taxable_micro: 2310
```

```oa-check
name: France restored Stripe reconciliation and evidenced annual PAS
inputs:
  verified_gross_receipts: 4800
  actual_platform_fee: 150
  reconciled_monthly_PAS: 420
  verified_same_year_count: 12
steps:
  net_bank_payout: verified_gross_receipts-actual_platform_fee
  annual_tax_prepayments: reconciled_monthly_PAS*verified_same_year_count
expected:
  net_bank_payout: 4650
  annual_tax_prepayments: 5040
```

## Section 5: Tier 1 Rules (When Data Is Clear)

### 5.1 Micro-Entrepreneur / Micro-BNC / Micro-BIC Regime

- **Legislation**: CGI art. 50-0 for micro-BIC, CGI art. 102 ter for micro-BNC; both declared on form 2042-C-PRO.  _(CGI art. 50-0; CGI art. 102 ter)_
- **Taxable income**: Gross eligible turnover/receipts excluding VAT less the applicable allowance/minimum, with no micro deficit and no additional actual expenses. Keep asset gains/losses and any valid VFL treatment separate.
- **Which limit applies**: First make the statutory proportional adjustment for any short reference year’s time of operation/activity; then test the adjusted turnover of the two previous years against the pair for the income year concerned. One year over a limit does not end the regime.
- **Mixed activity**: Apply each relevant statutory allowance category to its own slice and its own minimum; the two-category minimum illustration is not a universal flat deduction for every multi-activity business. Test global and activity-specific turnover gates as well.
- **Nil turnover**: For the annual IR declaration, F23267 requires “néant” in the turnover box. Separately, the monthly/quarterly Urssaf turnover declaration remains compulsory even where the period’s turnover is zero; Urssaf instructs the taxpayer to validate it with EUR 0 in the turnover field, not to omit the declaration. These are different returns and periods. Source: https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/lessentiel-du-statut.html

### 5.2 BNC Déclaration Contrôlée (Déclaration2035)

A liberal professional falls under déclaration contrôlée if both prior years exceed the applicable micro limit or an effective election applies; one overrun alone is insufficient. Submit the actual2035/2035-A/2035-B route and carry the result to2042-C-PRO, using the stated electronic deadline. Expense deduction requires the actual professional purpose, evidence, timing and specific statutory treatment, including capitalisation/depreciation. CGI154bis separately governs compulsory and qualifying optional contributions; a “Madelin” bank label is not automatic deductibility.

**Cash or acquired-receivables election (CGI art. 93 A).** For an ordinary continuing déclaration-contrôlée BNC activity, default cash receipts/paid eligible expenses remain distinct from an evidenced art. 93 A option for acquired receivables/incurred eligible expenses. Exercise the option before 1 February of the year for which income tax is established; it continues until denounced within the same timetable. A business starting during the year can elect for its first activity year by the art. 97 results-return deadline. This is not the separate micro-to-déclaration-contrôlée election in Section 6.1. On stipulated continuing-year facts with no transition adjustments, cash receipts EUR 10,000 less paid eligible expenses EUR 1,000 give EUR 9,000; acquired receivables EUR 15,000 less incurred eligible expenses EUR 1,500 give EUR 13,500 only with a valid art. 93 A election. On exit from art. 102 ter into this elected method, art. 93 A separately adds the receivables held on 31 December of the preceding year, excluding VAT and less 34%: EUR 3,000 gives EUR 1,980 to add before the complete transition reconciliation. Obtain the actual election/denunciation, start date and opening balances; these continuing examples do not compute every change-of-method adjustment or an unsupported weekend extension. Source: https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000048847605/2026-03-15

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

1. Establish the professional result under the actual method: micro gross excluding VAT less the allowance/minimum with no deficit; real BNC under the evidenced cash/accrual selection and art. 93 A timetable in Section 5.2 and specific deductions; BIC under the applicable actual-results rules. A valid VFL option pays IR separately on the covered turnover: annual reporting still supplies RFR/effective-rate information, without taxing that result again through the ordinary scale.
2. Assemble each other category’s taxable net amount, including taxable salary before its professional-expense deduction and the separately established pension/rental figures. A bank credit is not itself the taxable salary base.
3. Apply global deficits/charges without duplicating a category deduction, then the applicable special age/invalidity or attached-family allowances to reach revenu net imposable. Keep revenu net global and revenu net imposable distinct; use the household companion’s actual conditions.
4. Divide by the number of shares, apply the scale, multiply back, then cap the benefit of the extra shares (Section 6.2).
5. Apply the quotient-cap complements and any DOM reduction in their prescribed order, then the décote and the separately computed CEHR/CDHR where their own reference-income and other conditions apply. Use `fr-personal-income-tax` for those complete household methods.
6. Apply eligible reductions/credits with their own refundability and global-cap rules, reconcile any advance already received, then the actual tax-year instalments/withholding. Do not deduct a received credit advance a second time or treat every tax reduction as refundable.

| Standard deduction on salaries | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/10855-PGP.html/identifiant=BOI-BAREME-000035-20260217 |
| Rate, unless actual expenses are elected | 10% | Déduction forfaitaire de 10 % |
| Minimum per person, income of 2025 | EUR 509 | Limited to the relevant declared remuneration if that is smaller |
| Ceiling per person, income of 2025 | EUR 14,555 | Plafond |

For the ordinary 2025 salary flat deduction, use `min(S, min(max(10% × S, 509), 14555))`, where S is the relevant declared remuneration before professional expenses. Salary EUR 200 therefore gives deduction EUR 200 and salary net EUR 0, not a negative EUR 309 to offset another category. Each household member’s actual-expense election is separate and cannot be combined with the flat deduction. This formula does not turn a bank credit into the taxable salary base. Source: https://www.impots.gouv.fr/particulier/questions/comment-puis-je-beneficier-de-la-deduction-forfaitaire-de-10

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

An employee or pensioner has tax withheld by the payer. A self-employed person, a farmer, and anyone with rental income, alimony or qualifying foreign income within the PAS collection field pays instead by instalments (acomptes) debited by the tax office each month, or every three months where the taxpayer opts with the service des impôts des entreprises by the date in Section 5.6. Foreign income entitled under the actual treaty to a credit equal to the corresponding French tax is excluded from PAS: reporting it on form 2047 does not make it an acompte base. Foreign income with another credit mechanism requires its own collection test, not an automatic exclusion. Source: https://bofip.impots.gouv.fr/bofip/11247-PGP.html/identifiant=BOI-IR-PAS-20-20-10-20260407 . They are computed on the income declared the year before, so a business in its first year has no instalment computed from a declared figure; check the espace particulier for what is actually programmed. The personalised rate is recalculated each September from the spring return, and a married or PACS couple taxed jointly gets an individualised rate automatically. It applies only to each spouse's own income; the household's common income stays on the household rate.

Where no personalised rate exists, a default grid applies to the monthly base. The page below prints it in full in three versions: metropolitan France and abroad, Guadeloupe with La Réunion and Martinique, and Guyane with Mayotte. The extremes of the metropolitan grid:

| Monthly base, metropolitan grid from 1 May 2026 | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/11255-PGP.html |
| Below EUR 1,635 | 0% | Inférieure à 1 635 euros 0 % |
| EUR 1,635 inclusive to BELOW EUR 1,698 | 0.5% | The upper endpoint is exclusive: inférieure à 1 698 euros 0,5 % |
| EUR 55,558 and above | 43% | égale à 55 558 euros 43 % |

A micro-entrepreneur who opted for the flat payment pays the tax with the Urssaf turnover declaration instead, and must switch off any instalment already programmed in the espace particulier.

| Balance after the spring return | Collection | Note |
| --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/les-modalites-de-la-declaration-de-revenus-en-2026 |
| Up to and including EUR300 | One debit in September2026 under the ordinary schedule | The exact300 boundary belongs here. |
| Strictly above EUR300 | Four ordinary monthly debits, September–December | Check the actual notice and any different recovery procedure. |

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
| Correcting an eligible2026 online return | 29July–30November2026 inclusive | Specific current correction calendar; the annual overview’s generic mid-August/mid-December wording is retained as contrary history, not the operative deadline. |
| Result return of a réel filer (2031, 2035) | 15 days after the second working day following 1 May | au plus tard 15 jours après le 2 e jour ouvré suivant le 1 er mai (F32105, F32919) |
| Urssaf turnover declaration (micro) | Monthly or quarterly, as opted | déposée auprès de l’Urssaf chaque mois ou trimestre (selon la périodicité choisie) (F23267) |
| Source | acompte and instalment-option dates below | https://entreprendre.service-public.fr/vosdroits/F32105 |
| Monthly acompte of a self-employed filer | The 15th of each month | au plus tard le 15 du mois |
| Quarterly acompte, where the option is taken | 15 February, 15 May, 15 August, 15 November | au plus tard le 15 février, le 15 mai, le 15 août et le 15 novembre |
| Taking or ending the option for quarterly acomptes | 1 October of the year before | opter au plus tard le 1 er octobre de l'année précédent |

Online filing is the ordinary rule where the home has internet access and the taxpayer can file online; preserve the express inability-to-file-online qualification.

### 5.7 Penalties

| Offence | Surcharge | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/4911-PGP.html |
| Late filing under CGI1728 | 10% in the ordinary initial branch | The40% notice/30-day branch and80% occult-activity branch have their own triggers; a deadline miss does not establish deliberate fraud. |
| Deliberate breach (manquement délibéré) | 40% | la majoration de 40 % pour manquement délibéré |
| Abuse of law/fraudulent manoeuvres/specified concealment under CGI1729 | 80% under the actual branch | Abuse falls to40% if the administration does not establish principal initiative or principal benefit; apply the provision’s exact conditions. |

| Charge | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/1458-PGP.html |
| Late payment interest, per month of delay | 0.2% | intérêt de retard de 0,2 % par mois |

CGI1727 interest and statutory surcharges are separate tests. The0.20% monthly rule has its own accrual dates, tolerance and relief provisions, including the specified good-faith spontaneous-correction reduction. Do not add it automatically to every delayed payment; CGI1730 and1729G have distinct conditions and nonduplication rules in `fr-personal-income-tax`.

## Section 6: Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Regime Optimisation (Micro vs Réel)

Compare both actual eligible methods using the complete household tax and contribution facts; costs exceeding an allowance do not alone establish that real taxation is better. The BNC declaration-controlled election deadline is the results-return deadline for the year concerned; the BIC option has its separate CGI50-0 timetable and renewal/renunciation conditions.

### 6.2 Quotient Familial (Family Quotient)

A single person has 1 share, a couple taxed jointly 2 shares, with extra shares for dependants. The benefit of the extra shares is capped, and the cap depends on the kind of share:

| Cap on the tax saving, income of 2025 | Amount | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/2494-PGP.html/identifiant=BOI-IR-LIQ-20-20-20-20260407 |
| Each extra half-share for a dependent child | EUR 1,807 | fixé à 1 807 € par demi-part supplémentaire |
| Each extra quarter-share for a child in equally shared custody | EUR 903.50 (EUR 1,807 / 2) | DGFiP aide-mémoire: par quart de part lié à un enfant en résidence alternée; two such quarters making an extra half-share have EUR 1,807 total, before any separately qualifying single-parent override. |
| The whole extra share for the first child of a parent living alone | EUR 4,262 | Son montant est fixé à 4 262 € |
| Each half-share for the first two children in equally shared custody, taxpayer living alone | EUR 2,131 | soit 2 131 € (4 262 € / 2) |
| The extra half-share of a person living alone with no dependants who raised a child alone for at least five years | EUR 1,079 | est fixé à 1 079 € |

The number of shares itself is on https://www.service-public.fr/particuliers/vosdroits/F2705

A small bill is then reduced by the décote. It works on the tax, not on the income, and it fades out: the décote is the fixed amount in the table below, less the share of the gross tax in the table below, so it shrinks to nothing as the gross tax reaches the threshold. For an eligible gross tax T after the prescribed quotient-cap complements and DOM reduction, the décote is `min(T, max(0, K − 45.25% × T))`, with the actual population’s K and threshold below. CGI art. 197 I-4-a limits the reduction to the tax it reduces: stipulated ordinary single-person T = EUR 500 gives raw EUR 670.75, allowed décote EUR 500 and remaining IR EUR 0, not negative EUR 170.75. This nonrefundable reduction is separate from later refundable credits. Source: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542636/2026-05-02

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
| General-case uplift per qualifying dependent child, household member over65 or ascendant over65 | EUR1,500 | Apply actual claimant/ascendant conditions; do not read this as an uplift for every ascendant of any age. |
| Ceiling once the uplifts are counted, general case | EUR 15,000 | sans pouvoir dépasser au total 15 000 € |
| Uplift per dependent child in equally shared custody | EUR 750 | 750 € en cas de garde alternée |
| Small handyman work of at most two hours, inside the ceiling above | EUR 500 | Intervention pour petit bricolage d'une durée maximale de 2 heures 500 € |
| Computer and internet help at home, inside the ceiling above | EUR 3,000 | Assistance informatique et internet à domicile 3 000 € |
| Small gardening work, inside the ceiling above | EUR 5,000 | Petits travaux de jardinage 5 000 € |
| Ceiling on the expenses, first year of directly employing someone at home | EUR 15,000 | Pour la 1 re année où vous employez directement un salarié à domicile, les dépenses sont retenues dans la limite de 15 000 € |
| Maximum credit, first year of directly employing someone at home | EUR7,500 before eligible uplifts | The first-direct-employment expense ceiling can reach18,000 after eligible uplifts, corresponding to9,000 at50%; do not apply this first-year branch to every intermediary contract. |
| Expense ceiling for the specifically qualifying invalidity cases | EUR20,000 | Actual daily-living-assistance, dependent person living at home, or qualifying child/AEEH-complement conditions; not every disability label. No further uplift in this branch. |
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

Only eligible actual childcare costs for the qualifying dependent child and approved care setting enter this credit; food costs are excluded. Deduct the specified CAF/employer aid first. The under-six test is at1January of the relevant income year.

**The credit for training a company director has ended**, for training taken after 31 December 2024, with no extension in force: https://entreprendre.service-public.fr/vosdroits/F23460

### 6.4 Qualifying Social/Optional Insurance Contributions under CGI154bis

CGI154bis covers qualifying BIC as well as BNC real profits. Micro expenses remain covered by the flat allowance, so this is not an additional micro deduction. Establish the actual compulsory contribution or qualifying insurance/PER component, taxpayer/contract conditions and insurer evidence first. Professional-liability insurance is separate from health/provident/pension coverage.

For the capped optional branches, let P be the applicable annual social-security ceiling and B the statutory professional profit before these same capped contributions/premiums. Include the exempt profits specified by154bis-II, exclude long-term professional gains/losses, and do not reduce B by carried-forward category deficits. For BNC the retained doctrine uses P at1January of the tax year; the cessation/short-period adjustment has its own rule. Establish those actual inputs before using a ceiling.

| Eligible risk branch | Ceiling under CGI154bis-II | Conditions |
| --- | --- | --- |
| Retirement and the specified related guarantees | max[10% × min(B,8P) +15% × max(min(B,8P)−P,0),10% × P] | Apply the required reduction for the specified exempt employer-plan contributions and the actual qualifying product. |
| Provident cover and the specified guarantee | min[7% × P +3.75% × B,3% ×8P] | Apply the actual qualifying guarantee/contract conditions, including health-cover requirements where relevant. |
| Involuntary unemployment and the specified guarantee | max[1.875% × min(B,8P),2.5% × P] | This is not ordinary professional-liability insurance. |

These expressions describe the ordinary nonnegative-profit ceiling branches, not a blanket deduction for every product named Madelin or PER. Deduct only qualifying amounts within the applicable ceiling; aggregate the relevant contributor/collaborator amounts and apply the separate partner and paid/engaged timing conditions. Do not deduct the same payment again from global household income, or substitute the household PER ceiling. Check current product/age eligibility and the complete pension/insurance treatment in the named companions; this Guide does not certify a contract from its bank narration alone.

### 6.5 Home Office Deduction (Régime Réel)

For real BNC mixed rented premises, divide total eligible rent, including an applicable professional-use surcharge, between actual professional and private use. BOI4659§70 permits the practical ratio of professional floor area to total area, with the taxpayer retaining the calculation/evidence. Do not allocate the entire rent surcharge automatically to business. Utilities and other mixed costs need their actual professional-use basis; this rent rule is not a universal percentage for every bill. Owned business premises, private-property “rent to oneself”, repairs and depreciation have distinct conditions: neither notional rental value nor a mortgage principal payment is an automatic current deduction.



For the proprietor’s own additional meals in2026, establish that professional work and the actual, not abnormally chosen, distance prevent eating at home; retain proof of the effective expense. The private home-meal value is EUR5.50 TTC and the ordinary excessive-cost boundary is EUR21.40 TTC, so the ordinary additional-cost maximum is EUR15.90. Start from the actual expense and exclude the private component; an amount above21.40 requires the stated exceptional-necessity/nearby-catering justification for a greater deduction. Without proof, no flat deduction is allowed. These2026 values are not asserted as the2025 income-year values. Business/client hospitality follows its own direct-professional-connection and normal-amount rule, rather than automatically applying the proprietor’s personal-meal formula.

Professional borrowing must also be split: the borrowed capital repayment is not itself a BNC expense; the qualifying professional interest follows its own rule. Professional order/union subscriptions and current professional study/training have direct provisions in BOI4628. Do not infer that every new qualification or retraining programme qualifies: the same source records the2026 removal of the specified sportsperson insertion/conversion deduction.

## Section 7: Excel Working Paper Template

**Working-paper operations.** In B2 use the remuneration-limited salary deduction in Section 5.3. Before F5, establish the tax after F4 and any qualifying cap complements/DOM reduction; enter only the capped décote from Section 6.2 and subtract it once. For H, use that resulting nonnegative ordinary IR before the separately eligible G reductions/credits, applying each reduction/credit’s own nonrefundability or refundability rules. The F3 shorthand does not authorise subtracting an uncapped raw décote or omitting F4. The worksheet’s real-BNC A4/A5 inputs must follow the evidenced Section 5.2 method and any separately established transition adjustments.

~~~
IMPÔT SUR LE REVENU, WORKING PAPER, INCOME OF 2025.
Contribuable: _______________  Numéro fiscal: ___________
Régime: Micro-entrepreneur (BNC/BIC) / Régime réel (BNC) [circle one]
Situation familiale: Célibataire / Marié(e) / PACS / Divorcé(e) / Veuf(ve)
Nombre de parts: ___________

A. REVENUS PROFESSIONNELS.
  A1. CA brut encaissé hors TVA (micro)        ___________
  A2. Abattement (rate from the table)         ___________
  A3. Revenu net imposable (A1 minus A2)       ___________
  A4. Recettes brutes (réel, form 2035)        ___________
  A5. Total charges déductibles                ___________
  A6. Revenu net imposable (A4 minus A5)       ___________

B. AUTRES REVENUS.
  B1. Salaire net imposable avant frais pro   ___________
  B2. Moins déduction forfaitaire (see 5.3)    ___________
  B3. Salaires nets imposables                 ___________
  B4. Pensions de retraite                     ___________
  B5. Revenus fonciers                         ___________
  B6. Total autres revenus                     ___________

C. REVENU BRUT GLOBAL (A3 or A6, plus B6)      ___________

D. CHARGES DÉDUCTIBLES.
  D1. Pensions alimentaires versées            ___________
  D2. Autres charges                           ___________

E. REVENU NET GLOBAL (C minus D, after actual global deficits) ___________
  E1. Special age/invalidity or attached-family allowances, if eligible ___________
  E2. REVENU NET IMPOSABLE (E minus applicable E1) ___________

F. QUOTIENT FAMILIAL.
  F1. Revenu imposable par part (E2 / parts)  ___________
  F2. Impôt sur E2/parts (apply the scale)     ___________
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
  [ ] Urssaf reconciled: no extra micro deduction; real-regime components tested?
  [ ] Instalments summed from the bank statement?
  [ ] Crédits d'impôt identified?
  [ ] Qualifying154bis contributions/limits checked (actual BIC/BNC real regime)?
~~~

## Section 8: Bank Statement Reading Guide

### French Bank Statement Formats

Historical illustrative fixtures from the predecessor, not verified current specifications for these banks. Confirm the actual client export. The labels and columns below do not establish a legal tax category.

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
| AIDES CAF / ALLOCATION | Identify the exact benefit | No automatic exemption from this narration alone. |

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
6. Aussi salarié(e)? Si oui, net imposable annuel avant frais professionnels?
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
3. Compute the professional result under the actual micro or real method and the correct category/form. For covered VFL turnover, follow the separate gross-HT payment and annual RFR/effective-rate method in Section1; do not add the already-liberated result to ordinary taxable income a second time.
4. Build the household income, divide by the shares, apply the scale, multiply back, then cap the benefit of the extra shares: https://www.service-public.fr/particuliers/vosdroits/F1419
5. Complete the quotient-cap/special-allowance/DOM/décote and separate CEHR/CDHR methods in `fr-personal-income-tax`, with each tax’s actual reference-income and eligibility conditions, before the eligible credit/advance and withholding reconciliation.
6. Deduct the instalments already taken and settle the balance on the autumn schedule: https://www.impots.gouv.fr/les-modalites-de-la-declaration-de-revenus-en-2026
7. File form 2042 with 2042-C-PRO by the deadline for the client's département, and a réel filer's result return by its own earlier deadline.

## Ask the client first

- Which regime are you in, and did you ever opt out of micro? The option changes the whole computation.
- What was your turnover, excluding VAT, in each of the two previous years? One year over a limit does not lose the micro regime; two consecutive years does.
- Is any part of the turnover furnished letting, and is the property a classified meublé de tourisme? The limit and the allowance both change.
- Have you opted for the flat income tax payment with Urssaf? If yes, the instalment must be switched off.
- Establish family situation at1January, the relevant year-end increase/change rules and any death-year periods;31December alone is not the universal household reference date.
- Are you also employed, and did you keep a household rate or an individualised rate for the withholding?
- Reconcile the instalments and withholding for the actual income year being assessed, the programmed current instalments and the rate in the espace particulier. Do not substitute another calendar year’s bank debits.

## When to refuse or refer

- Refuse a company subject to corporation tax: this Guide is for individuals under the income tax.
- Refuse non-resident cases: different rates, different withholding, treaty analysis.
- Refuse capital gains and the taxation of dividends and interest: separate rules, separate Guides.
- Refer a réel filer with depreciation, an asset register or stock to an Expert-Comptable before filing.
- For an optional-contribution claim, establish the actual154bis risk, qualifying contract, statutory profit base, applicable P and any partner/collaborator/employer-plan adjustments. Refer product eligibility, negative-profit and nonstandard-period questions not settled by the stated branch; do not refuse the ordinary sourced ceiling calculation merely because it was absent from the predecessor.
- Refer anything turning on a CFE amount: the commune sets it and no national figure exists.
- Stop and ask rather than guess a withholding rate or an instalment total: both are in the espace particulier.

## Sources

- https://www.service-public.fr/particuliers/vosdroits/F1419 Selected cited scope read 2026-10-29.
- https://www.service-public.fr/particuliers/vosdroits/F2705 Selected cited scope read 2026-10-29.
- https://www.service-public.fr/particuliers/vosdroits/F34009 Selected cited scope read 2026-10-29.
- https://www.service-public.fr/particuliers/vosdroits/F12 Selected cited scope read 2026-10-29.
- https://www.service-public.fr/particuliers/vosdroits/F8 Selected cited scope read 2026-10-29.
- https://entreprendre.service-public.fr/vosdroits/F23267 Selected cited scope read 2026-10-29.
- https://entreprendre.service-public.fr/vosdroits/F32919 Selected cited scope read 2026-10-29.
- https://entreprendre.service-public.fr/vosdroits/F32105 Selected cited scope read 2026-10-29.
- https://entreprendre.service-public.fr/vosdroits/F23460 Selected cited scope read 2026-10-29.
- https://bofip.impots.gouv.fr/bofip/2494-PGP.html/identifiant=BOI-IR-LIQ-20-20-20-20260407 Selected cited scope read 2026-10-29.
- https://bofip.impots.gouv.fr/bofip/2495-PGP.html/identifiant=BOI-IR-LIQ-20-20-30-20260407 Selected cited scope read 2026-10-29.
- https://bofip.impots.gouv.fr/bofip/10855-PGP.html/identifiant=BOI-BAREME-000035-20260217 Selected cited scope read 2026-10-29.
- https://bofip.impots.gouv.fr/bofip/7804-PGP.html/identifiant=BOI-IR-CHR-20170711 Selected cited scope read 2026-10-29.
- https://bofip.impots.gouv.fr/bofip/11255-PGP.html Selected cited scope read 2026-10-29.
- https://bofip.impots.gouv.fr/bofip/4911-PGP.html Selected cited scope read 2026-10-29.
- https://bofip.impots.gouv.fr/bofip/1458-PGP.html Selected cited scope read 2026-10-29.
- https://www.impots.gouv.fr/les-modalites-de-la-declaration-de-revenus-en-2026 Selected cited scope read 2026-10-29.
- https://www.impots.gouv.fr/formulaire/2042/declaration-des-revenus Historical/navigation URL retained; this URL body has no accepted direct read claim. Replacement DGFiP2026 return-calendar/annual-reporting quoted source read 2026-10-29.
- https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/lessentiel-du-statut.html Selected cited scope read 2026-10-29.

- https://bofip.impots.gouv.fr/bofip/4628-PGP.html Selected cited scope read 2026-10-29.
- https://bofip.impots.gouv.fr/bofip/4658-PGP.html Selected cited scope read 2026-10-29.
- https://bofip.impots.gouv.fr/bofip/4659-PGP.html Selected cited scope read 2026-10-29.
- https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047288764 Selected cited scope read 2026-10-29.
- https://bofip.impots.gouv.fr/bofip/4627-PGP.html/identifiant=BOI-BNC-BASE-40-60-50-20-20141007 Selected cited scope read 2026-10-29.
- https://entreprendre.service-public.gouv.fr/vosdroits/F32105 Selected cited scope read 2026-10-29.
- https://entreprendre.service-public.gouv.fr/vosdroits/F36249 Selected cited scope read 2026-10-29.

Not yet confirmed in this companion: the precise2025 own-meal parameters, any treatment requiring an unprovided VAT-inclusive real-BNC accounting election, negative-profit/nonstandard154bis cases, particular insurance/PER contract eligibility, and bank-specific current export layouts. Household, property, nonresident, capital-gain and social-base methods remain in their named companions. A source’s acquisition date is not its effective date or an accountant attestation.

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as an Expert-Comptable, Avocat Fiscaliste, or equivalent licensed practitioner in France) before filing or acting upon.

The most up-to-date version of this Guide is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

> Contributed by OpenAccountants.


Selected repair clauses read on 31 October 2026: CGI arts. 50-0/102 ter reference-year adjustment and art. 93 A continuing/startup/exit selection; DGFiP salary lower-remuneration limit and 2026 aide-mémoire half/quarter units; BOI-IR-PAS-20-20-10 foreign credit-equal-to-French-tax exclusion; Urssaf’s separate periodic EUR 0 field. CGI art. 197 I-4-a’s tax-amount limit is retained as an official indexed observation; its direct body request returned 403, so no full original HTML reading is claimed. The actual cited official URLs are printed beside these methods. These are selected-clause writer checks, not independent approval.

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
