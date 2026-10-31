---
name: france-tax-optimization
description: Use this skill whenever asked about reducing tax in France, tax planning, saving tax, optimizing tax, allowances, deductions the client might be missing, or any question about legal strategies to minimize income tax liability for self-employed individuals in France. Trigger on phrases like "reduce tax", "tax planning", "save tax", "optimize", "allowances", "deductions I'm missing", "payer moins d'impôts", "optimisation fiscale", "réduire ses impôts", "défiscalisation". ALWAYS read this skill before advising on any French tax optimization strategy.
version: 1.2
jurisdiction: FR
tax_year: 2026
last_updated: 2026-10-31
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# France: legal tax planning for the self-employed and small business owners

This skill helps an assistant compare the lawful choices a French self-employed person or small business owner can make: which income tax regime, which legal structure, when to spend, save or invoice, and which deductions and reliefs to claim. Figures are for tax year 2026. France taxes the previous year's income, so the income tax scale, the family quotient cap, the retirement savings ceilings and the credit and reduction limits marked "income of 2025" govern income of 2025 declared in 2026, while the micro turnover limits marked "income of 2026", the corporation tax rates, the VAT thresholds and the social contribution rates are those in force during 2026. VAT and social contribution rules are tied to the selected current sources actually read on 29 October 2026, with the start date where a rule changed during the year. Where a 2026 figure is not yet published, the table says so and gives the latest official figure with its year. Every recommendation below rests on a rule printed on an official page; a planning idea that depends on a figure no official page prints has been left out.

## Section 1: Quick reference

**Quick reference fields**

| Field | Value |
| --- | --- |
| Country | France (République française) |
| Authority | Direction générale des finances publiques (DGFiP), with URSSAF for social contributions |
| Main texts | Code général des impôts (CGI), social-security legislation and Livre des procédures fiscales (LPF). The figure ledger distinguishes actual selected statute representations, administrative doctrine, acquired bodies and failed direct routes; no whole-code reading is claimed |
| Tax year | Calendar year, taxed the following year |
| Return for income of 2025 | Filed in spring 2026; the deadlines are in Section 11 |
| Currency | EUR |
| Companion skills | `fr-income-tax` (self-employed income tax), `fr-personal-income-tax` (the full household computation), `fr-social-contributions`, `fr-capital-gains`, `fr-rental-income`, `france-vat-return`, `france-formation`, `france-bookkeeping`, `fr-tax-audit` |

Planning here means using the options and reliefs the law offers. Arrangements the tax authority can set aside, and their penalties, are in Section 10.

### Income tax scale applied in 2026 to the income of 2025

The scale applies to taxable income per family-quotient share (the household's net taxable income divided by its number of parts). The tax for one share is then multiplied by the number of shares.

**Income tax scale, income of 2025**

| Band | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.service-public.gouv.fr/particuliers/vosdroits/F1419 |
| Top of the 0% band, per share | EUR 11,600 | "Jusqu'à 11 600 € 0 %" |
| Rate of the first band | 0% | same quote |
| 11% band, first euro | EUR 11,601 | "De 11 601 € à 29 579 € 11 %" |
| 11% band, last euro | EUR 29,579 | same quote |
| Rate of the second band | 11% | same quote |
| 30% band, first euro | EUR 29,580 | "De 29 580 € à 84 577 € 30 %" |
| 30% band, last euro | EUR 84,577 | same quote |
| Rate of the third band | 30% | same quote |
| 41% band, first euro | EUR 84,578 | "De 84 578 € à 181 917 € 41 %" |
| 41% band, last euro | EUR 181,917 | same quote |
| Rate of the fourth band | 41% | same quote |
| Rate on the part per share above the fourth band | 45% | "Plus de 181 917 € 45 %" |

### The family quotient and its cap

Each extra half-share lowers the tax, but the saving each half-share may give is capped. The cap is the most common reason a "split the income" estimate is too optimistic.

**Family quotient cap, income of 2025**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/2494-PGP.html/identifiant=BOI-IR-LIQ-20-20-20-20260407 |
| Maximum saving per extra half-share for dependants, general case | EUR 1,807 | "Son montant est fixé à 1 807 € par demi-part supplémentaire" |

The number of parts by family situation, the larger caps for single parents and the other special cases are in `fr-personal-income-tax`. This skill does not repeat them.

## Section 2: Income splitting and structuring

### Micro-entreprise or régime réel

Under the micro regime the taxable profit is turnover less a flat allowance. Under the régime réel it is turnover less the actual deductible costs. The micro regime is better only while the real costs are lower than the flat allowance.

**Micro regime: limits, allowances and the flat income tax payment**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F23267 |
| Turnover limit, sales of goods and accommodation, governing income of 2025 | EUR 188,700 | "ne doit pas avoir dépassé 188 700 €" |
| Turnover limit, services and BNC, governing income of 2025 | EUR 77,700 | "ne doit pas avoir dépassé 77 700 €" |
| Turnover limit, goods and qualifying accommodation EXCLUDING furnished residential letting, governing income of 2026 | EUR 203,100 | "n’a pas dépassé 203 100 €" |
| Turnover limit, services/BNC and ordinary furnished residential letting; eligible classified tourist lets and chambres d’hôtes have their own stated branch, governing income of 2026 | EUR 83,600 | "n’a pas dépassé 83 600 €" |
| Flat allowance, sales of goods | 71% | "Le taux d'abattement est de 71 %" |
| Flat allowance, commercial services (BIC) | 50% | "Le taux d'abattement est de 50 %" |
| Flat allowance, non-commercial activities (BNC) | 34% | "Le taux d'abattement est de 34 %" |
| Floor of the flat allowance | EUR 305 | "Le montant de l’abattement ne peut pas être inférieur à 305 €" |
| Optional flat income tax payment, commerce/catering and qualifying accommodation EXCLUDING furnished residential letting | 1% | "1 % pour les activités de commerce, restauration et logement" |
| Optional flat income tax payment, other BIC activities | 1.7% | "1,7 % pour les autres activités relevant des BIC" |
| Optional flat income tax payment, BNC activities | 2.2% | "ce taux est de 2,2 %" |
| For the 2026 option: 2024 RFR, one share, must not exceed | EUR 29,315 | DGFiP’s current year selector expressly uses 2024 RFR for the 2026 option |
| For the 2026 option: 2024 RFR, couple with two shares, must not exceed | EUR 58,630 | The 29,579/59,158 amounts instead concern the 2027 option using 2025 RFR |

How the limits work, as the page states it: a business keeps the micro regime for year N if its turnover excluding VAT of year N-1 or of year N-2 stayed within the limit, so the regime is lost only when the limit is exceeded two years running. A new business is under the micro regime in its year of creation and the next year, and may opt for a real regime if it does not want the micro regime. The flat income tax payment must be requested from URSSAF before 30 September of the year before the one it is to apply to; a request made before 30 September 2026 applies to income received from 1 January 2027. A new business may instead request it before the last day of the third month after the month of creation. Above the reference-income limit for the household's situation, the option is closed. Use the option year and N-2 household shares explicitly: the published DGFiP example for 2.5 shares uses a strict rounded threshold below EUR 73,288 for 2026 (below EUR 73,948 for 2027), while its general rule says the limit must not be exceeded. Retain that published selector/rounding distinction rather than applying the 2027 amount to 2026.

Which way to choose:

- Compare the flat allowance in the table above with the real costs of the year, including depreciation (Section 4). If the real costs are higher, the régime réel gives the lower profit for income tax.
- The flat payment replaces the progressive income tax on that business income. It is worth it only where the household's marginal rate is higher than the flat payment rate would imply for that turnover; at a 0% marginal band it costs money. The comparison is the assistant's, not a figure on the page: show both computations.
- The régime réel brings bookkeeping duties: see `france-bookkeeping`. The micro thresholds are income tax limits; the VAT franchise limits in Section 7 are separate and lower.

### Social contributions under the micro-social regime

A micro-entrepreneur pays social contributions as a percentage of turnover collected, not of profit. In a year with large costs the micro-social charge does not fall; under the régime réel the contributions follow profit (Section 8).

**Micro-entrepreneur social contribution rates, 2026**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/lessentiel-du-statut.html |
| Purchase and resale of goods (BIC) | 12.3% | "Achat/revente de marchandises (BIC) 12,3 %" |
| Commercial and craft services (BIC) | 21.2% | "Prestations de services commerciales et artisanales (BIC) 10,6% 15,9% 21,2%" |
| Other services (BNC), general scheme | 25.6% | "Autres prestations de services (BNC) 25,6 %" |
| Regulated liberal professions under the Cipav | 23.2% | "Professions libérales réglementées relevant de la Cipav (BIC et BNC) 23,2 %" |
| Acre reduced rate, sales of goods, activity started up to 30 June 2026 | 6.2% | "Vente de marchandises ( BIC ) 6,2% 9,3% 12,3%" |
| Acre reduced rate, sales of goods, activity started on or after 1 July 2026 | 9.3% | same quote |
| Acre reduced rate, commercial and craft services, started up to 30 June 2026 | 10.6% | "Prestations de services commerciales et artisanales (BIC) 10,6% 15,9% 21,2%" |
| Acre reduced rate, commercial and craft services, started on or after 1 July 2026 | 15.9% | same quote |
| Acre reduced rate, other services (BNC), started up to 30 June 2026 | 12.8% | "Autres prestations de services ( BNC ) 12,8% 19,2% 25,6%" |
| Acre reduced rate, other services (BNC), started on or after 1 July 2026 | 19.2% | same quote |

The Acre rates depend on the date the activity started, not on the date of the return: a business started before 1 July 2026 keeps the lower set. The Cipav Acre rates and the length of the Acre period are in `fr-social-contributions`.

### Entreprise individuelle or a company at corporation tax

A company subject to corporation tax (IS) pays tax on its profit at the company rates below. The owner then pays income tax on the pay drawn from it, and on any dividend either the flat tax or the progressive scale, plus the social levies, as in the tables below. SARL, SAS, SA and the other capital companies are at IS by default from creation; an entrepreneur individuel can opt to be treated as an EURL (CGI art. 1655 sexies), which is listed on the same page.

**Corporation tax, 2026**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F23575 |
| Standard rate | 25% | "imposée au taux normal de 25 %" |
| Reduced rate, on the first slice of profit only | 15% | "un taux réduit fixé à 15 %" |
| Slice of profit the reduced rate covers | EUR 42,500 | "la part des bénéfices allant jusqu'à 42 500 €" |
| Reduced rate condition 1: turnover of the period at most | EUR 10,000,000 | "Chiffre d'affaires inférieur ou égal à 10 000 000 €" |
| Reduced rate condition 2: capital fully paid up and held at least this share by individuals | 75% | "détenu pour au moins 75 % par des personnes physiques" |

Both conditions must be met (AND). Use turnover restated to 12 months where needed and the EUR 42,500 reduced-rate slice per 12-month period, with the applicable period adjustment. The capital must be held continuously at least75% by individuals, or by an intermediary company itself meeting the same CGI219I-b conditions and at least75% individually held. Apply the specified fund exclusions only without the statutory dependence link; use `fr-corporate-tax` for group turnover and the complete eligibility method. If the ordinary reduced-rate conditions fail, use the ordinary standard rate rather than assuming this slice is available.

**Tax on a dividend paid to a resident individual**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.service-public.gouv.fr/particuliers/vosdroits/F2613 |
| Income tax part of the flat tax (prélèvement forfaitaire unique) | 12.8% | "l'impôt sur le revenu ( 12,8 % )" |
| Allowance on dividends, only if the household elects the progressive scale | 40% | "Abattement de 40 % sur les dividendes" |

A household that takes the flat tax gives up the 40% allowance on dividends and the deduction of part of the CSG; the deductible CSG applies only to income taxed at the progressive scale.

**Social levies on investment income**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.service-public.gouv.fr/particuliers/vosdroits/F2329 |
| Produits de placement received/levied from 1 January 2026, general case | 18.6% | "Revenus de 2026 Le taux des prélèvements sociaux dépend des revenus concernés : Cas général Tableau - Taux des contributions sociales applicables Prélèvements sociaux Taux Contribution sociale général" |
| Produits de placement received/levied in 2025 only; not the general revenus du patrimoine declared in 2026 | 17.2% | "Revenus de 2025 Tableau - Taux des contributions sociales applicables Prélèvements sociaux Taux Contribution sociale généralisée (CSG) 9,2 % Contribution au remboursement de la dette sociale (CRDS) 0," |

The page keeps the lower total for some products in 2026, including life insurance: always name the income before using either rate. Do not add the income tax part and the levies into one figure; the page does not print one. Distinguish the collection populations before selecting the year: the enacted increase also applies to general revenus du patrimoine of2025 declared in2026 (18.6%), whereas produits de placement received/levied in2025 retain17.2%. Keep the actual lower-rate product exceptions, including property-income/property-gain and assurance-vie branches, and use `fr-capital-gains` for the income-specific method. The 2026 brochure news page states the different commencement clocks.

How to compare: compute, for the same profit, (a) income tax and self-employed contributions on the whole profit as an entrepreneur individuel, and (b) corporation tax on the profit kept, plus income tax and contributions on the pay drawn, plus the flat tax and levies on any dividend. The live text suggested a profit level above which a company "should be considered"; no official page prints such a level, so it is gone. The answer depends on how much is drawn, on the household's bands, and on whether a dividend to this manager also bears social contributions, which is a question for `fr-social-contributions` before any figure is given.

## Section 3: Deductions most people miss

**Deductions most people miss**

| Deduction | Legislation | Notes |
| --- | --- | --- |
| Self-employed social contributions | CGI art. 154 bis | Compulsory contributions are a cost of the business under the régime réel. Under the micro regime they are covered by the flat allowance and are not deducted again. |
| Deductible CSG on investment and property income | CGI art. 154 quinquies | The known deductible CSG on patrimony income is preprinted and corrected in 6DE if wrong. CSG relating to investment income declared in 2BH/2DF is calculated automatically and is NOT to be added manually to 6DE. Apply the actual scale/relief and payment-year conditions; nothing is deductible on ordinary PFU income. The deductible rate is in the table below. |
| Vehicle costs (barème kilométrique) | CGI art. 39 and art. 93 | For BNC, use actual justified costs or the eligible annual mileage election under BOI-BNC-BASE-40-60-40-20, with its vehicle, full-year, evidence and no-double-cost gates. Do not transfer that BNC mileage election automatically to every BIC business. The dated six-CV historical population is recomputed in Section 12. |
| Business premises at home | CGI art. 39 and art. 93 | Under the real regime, deduct only actual qualifying professional costs. For mixed rented BNC premises, BOI-BNC-BASE-40-60-30 §70 expressly accepts the rent fraction based on professional floor area/total area, supported by the working. Do not extend that rent key automatically to every utility or insurance bill: allocate each actual mixed cost on its professional facts. No automatic notional rent for an owner-occupied home. |
| Training linked to the current activity | CGI art. 39 and art. 93 | A cost of the business under the régime réel. The tax credit for training of business managers has ended: see the note below. |
| Professional subscriptions | CGI art. 93 | Professional order/union dues are expressly deductible under BOI-BNC-BASE-40-60-60 §200; do not infer that every association or general-interest subscription qualifies. Professional documentation has its own actual-use rule. |
| Meals taken alone because of the work | CGI art. 93 | For ordinary BNC work-only additional meals in 2026, establish normal professional necessity/distance and actual receipts. Deduct only the extra over the EUR 5.50 home-meal value. Without proved exceptional circumstances, the paid cost is capped at EUR 21.40, so the ordinary maximum is EUR 15.90; a EUR 25 meal with no justified exceptional need gives 21.40 − 5.50 = 15.90. No receipts means no flat deduction. These are BNC rules, not a transplant of employee meal deductions. |
| Interest on business loans | CGI art. 39 | Qualifying interest on borrowing for the actual profession is deductible under the applicable regime; repaying the borrowed capital itself is not. BNC interest relating to asset acquisition can instead form part of the asset cost under its specific election; do not infer a universal immediate deduction. |
| Business insurance | CGI art. 39 and art. 93 | Professional liability, premises and similar policies. Optional Madelin-type cover is deductible only within its own limits. |
| Gifts to charities | CGI art. 200 | A reduction of tax, not a deduction from income: see Section 9. |

**Deductible CSG**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/nouveautes.pdf |
| Deductible share of the CSG on investment and property income taxed at the progressive scale (nothing is deductible under the flat tax), unchanged despite the CSG rise | 6.8% | "Le taux de CSG déductible reste à 6,8 %" |

The training tax credit for business managers (crédit d'impôt pour la formation des dirigeants) cannot be claimed for training carried out after 31 December 2024. Since 1 January 2025, training is no longer eligible (page checked 21 February 2026: https://entreprendre.service-public.gouv.fr/vosdroits/F23460). The live text still offered it for 2026.

### Small equipment expensed at once

**Small equipment**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/2109-PGP.html |
| Unit value excluding VAT at or below which tools and equipment may be expensed at once | EUR 500 | "d'une valeur unitaire hors taxes n'excédant pas 500 €" |

The tolerance covers equipment and tooling that would otherwise go to the fixed-asset accounts for "matériels et outillages", and the page lists its own exclusions. The test is per unit, at or below the amount, excluding VAT. Above it, the item is capitalised and depreciated. This choice applies under the régime réel only.

## Section 4: Capital allowances optimisation

### Straight-line or declining balance

Straight-line depreciation is the default. Declining balance (amortissement dégressif, CGI art. 39 A) front-loads the deduction, but only for the asset categories the law lists, only for assets that were new when bought, and only with a normal useful life of at least three years. Which assets qualify is set out in `france-bookkeeping`.

**Declining balance coefficients**

| Normal useful life | Coefficient | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/4699-PGP.html |
| Three or four years | 1.25 | "1,25 lorsque la durée normale d'utilisation est de trois ou quatre ans" |
| Five or six years | 1.75 | "1,75 lorsque cette durée normale est de cinq ou six ans" |
| More than six years | 2.25 | "2,25 lorsque cette durée normale est supérieure à six ans" |

The declining rate is the straight-line rate for the useful life multiplied by the coefficient. Some equipment carries a raised or lowered coefficient.

### Timing of purchases

Under declining balance, the first year's charge runs from the first day of the month of acquisition to the year end, in proportion to the length of the financial year (same BOFiP page). So an asset bought early in the financial year gives a larger first-year charge than the same asset bought in its last month. Buying earlier is worth it only if the asset is needed anyway: a purchase made for the deduction alone spends more than it saves.

### Super-depreciation

The live text recommended an extra depreciation for "industrial robotics, digital transformation equipment, energy transition assets". No allowed page read in this pass confirms that any such scheme is open for investments made in 2026, so the recommendation is removed. Check the current BOFiP chapter BIC-BASE-100 before relying on any extra deduction.

## Section 5: Loss utilisation

**Losses, as set out in the 2026 income tax brochure (income of 2025)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/12-charges_ded_rev_225a236.pdf |
| Property deficit from costs other than loan interest, deductible from global income up to | EUR 10,700 | "le revenu global à hauteur de : - 10 700 € ;" |

What the same page says about each kind of loss:

- **Property (déficit foncier).** The part of a property deficit that comes from costs other than loan interest is set against the household's global income within the limit in the table above, under conditions. The part above the limit, and the part that comes from loan interest, is set only against property income of the next ten years. The page also prints raised limits for some housing schemes and for energy renovation work; check that passage before using a raised limit. The live text said the property carry-forward was six years; the page says ten.
- **Non-professional commercial activities** (other than furnished lets): set only against income from non-professional commercial activities, in the same year and the next six years.
- **Non-professional furnished lets (LMNP):** set only against income from non-professional furnished lets, in the same year and the next ten years.
- **Non-professional non-commercial activities:** set only against profits of the same kind, in the same year and the next six years.
- **Global deficit:** a global deficit not yet used is reported on the 2042 at lines 6FA to 6FL, which carry the years 2019 to 2024 for income of 2025.

An eligible professional BIC/BNC loss has the ordinary global-income route under CGI 156(I), rather than the non-professional same-category restriction. Classify the actual activity and deductible loss first; do not turn the label “professional” into an exemption from every statutory restriction. An unused GLOBAL deficit has its own next-six-years route. Professional furnished letting uses its own actual participation/status gates and the supplied rental method; its ordinary deficit is set against global income without an amount cap (https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/11-revenus_non_salaries_161a182.pdf). The property-loss 10,700 route also requires the continuing-letting condition through 31 December of the third following year, with actual exceptions/recapture; `fr-rental-income` supplies it.

Strategy: before advising someone with a salary to start an activity that will make early losses, establish whether it is carried on professionally. If it is not, the losses wait for future profits of the same kind and do not reduce tax on the salary.

## Section 6: Timing strategies

**Timing strategies**

| Strategy | Detail |
| --- | --- |
| Defer receipts | Where the client's regime counts receipts when they are collected, moving a receipt from late December to January moves it into the next income year. It must be a genuine change of when the customer pays, not a backdated record. Confirm whether the regime is on a receipts basis or an accruals basis in `fr-income-tax` before advising. |
| Bring forward expenses | Where the regime counts costs when paid, a cost paid before 31 December counts in that year. Where it follows accruals, prepaying does not move the deduction. Same check as above. |
| Retirement savings timing | Payments into a retirement savings plan are deducted for the year they are paid, within the ceiling for that year (Section 9). Unused ceiling can be carried forward; the carry-forward period changes for 2026, see Section 9. |
| Flat income tax payment | The request deadline is the one in Section 2. Missing it delays the option by a year. |
| Exceptional income | A one-off income can sometimes be taxed under the "système du quotient" for exceptional income. The live text gave a fraction; that rule is in `fr-personal-income-tax`, which covers the quotient for exceptional income, and is not repeated here. |

For the year of marriage or PACS, the 2026 brochure states one joint declaration for the whole year, with an option for separate declarations in that event year. This is not an automatic tax saving: apply the actual household facts and compare the permitted choices. Spouses must instead declare separately when separated in property and not living under the same roof, authorised to live separately during separation/divorce proceedings, one has abandoned the home and each has own income, or divorced in the year. The brochure also gives the actual PACS separate-property/equivalent-regime, separate-home, abandonment/own-income and dissolution grounds. Use `fr-personal-income-tax` for the complete household method; its2026-return brochure concerns events/income of2025, not a claim that the2027 return form is published.

## Section 7: VAT optimisation (TVA)

**VAT franchise en base, thresholds for 2026**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F21746 |
| Sales of goods, catering and accommodation: previous-year turnover at most | EUR 85,000 | "est inférieur ou égal à 85 000 € (seuil de la franchise en base de TVA)" |
| Same activities: current-year turnover at most | EUR 93,500 | "est inférieur ou égal à 93 500 € (seuil majoré de la franchise en base de TVA)" |
| Services and liberal professions: previous-year turnover at most | EUR 37,500 | "est inférieur ou égal à 37 500 € (seuil de la franchise en base de TVA)" |
| Same activities: current-year turnover at most | EUR 41,250 | "est inférieur ou égal à 41 250 € (seuil majoré de la franchise en base de TVA)" |

The page (checked 1 January 2026) says the thresholds for 2026 are unchanged and that the proposed single threshold was abandoned. Lawyers and authors have their own thresholds; see `france-vat-return`.

**Simplified VAT regime band (régime réel simplifié), 2026**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F23575 |
| Trade, catering and accommodation: lower end of the previous-year turnover band | EUR 85,000 | "doit être compris entre : 85 000 € et 945 000 €" |
| Same: upper end | EUR 945,000 | "85 000 € et 945 000 €" |
| Other services: lower end | EUR 37,500 | "37 500 € et 286 000 €" |
| Other services: upper end | EUR 286,000 | "37 500 € et 286 000 €" |

**VAT optimisation table**

| Strategy | Detail |
| --- | --- |
| Stay in the franchise | No VAT is charged and no VAT on costs is recovered. It helps with private customers, who cannot recover VAT. It does not help with business customers, who recover the VAT anyway. |
| Opt out of the franchise | A business in the franchise that wants to recover VAT on its purchases must opt for the real VAT regime (F21746). This makes sense in a year of heavy investment. The option is valid for two calendar years and renews tacitly; to leave it, the business must denounce it at the end of a two-year period, and if it has received a refund of a VAT credit the option is compulsorily renewed for two years. |
| Simplified regime | Turnover alone does not establish eligibility. CGI 287(3 bis) requires monthly filing when prior-year VAT is strictly ABOVE EUR 15,000. Exactly EUR 15,000 does not trigger that provision alone; do not infer automatic RSI eligibility at equality, because the other statutory regime, transaction and option conditions still apply. The administrative summary’s “below EUR 15,000” wording is retained as countertext and does not itself settle equality. Apply the full turnover, taxable-activity, exclusion and startup/ongoing rules in `france-vat-return`, including its calendar-year CA12 versus CA12E distinction. Annual return and instalments are separate from eligibility. |
| VAT on receipts or on invoices | When VAT becomes due for services, and the option to pay it on invoices, are covered in `france-vat-return`. |
| Reverse charge on EU business services | For an ordinary service actually within the general B2B place rule, supplied to a qualifying EU taxable customer, apply the customer-place/reverse-charge method. Do not transfer it to a service with its own place-of-supply exception or to an establishment that changes the liability. The full scope and DES conditions are in `france-vat-return`. |

## Section 8: Social security optimisation

From the 2025 income declared in 2026, the ordinary non-micro self-employed base starts from receipts/products less the qualifying business costs BEFORE deducting personal social contributions, deductible CSG and the listed tax exemptions/154 bis payments. The ordinary contributions and CSG-CRDS share that starting method, subject to their own statutory exceptions; the 26% allowance has a floor and ceiling, so it is not universally a simple 74% of tax profit. The social-contributions Guide supplies the exact components and exceptions (https://www.urssaf.fr/accueil/independant/comprendre-payer-cotisations/reforme-cotisations-independants.html).

**Self-employed contribution base after the reform**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.urssaf.fr/accueil/independant/comprendre-payer-cotisations/reforme-cotisations-independants.html |
| Flat allowance on the single base | 26% | "le revenu brut abattu de 26 %" |
| Ordinary full health rate on the fraction up to three PASS, after the applicable lower-base progressive reduction | 8.5% | CSS D621-1/D621-2: the fraction above three PASS instead bears 6.5%; this is not a flat 8.5% on every worker’s whole base |

**Contributions of craftsmen, traders and unregulated liberal professions, 2026**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-ac-plnr.html |
| Basic pension, on income up to one annual social security ceiling | 17.87% | "Revenus dans la limite de 48 060 € (1 plafond annuel de la Sécurité sociale - Pa" |
| One annual social security ceiling, 2026 | EUR 48,060 | same quote |
| Basic pension, on the part of income above one ceiling | 0.72% | "Part des revenus supérieure à 48 060 € (1 Pass) 0,72 %" |
| Supplementary pension, up to one ceiling | 8.10% | "Revenus dans la limite de 48 060 € (1plafond annuel de la Sécurité sociale - Pas" |
| Supplementary pension, between one and four ceilings | 9.10% | "Part du revenus compris entre 48 060 € et 192 240 € (entre 1 et 4 Pass) 9,10 %" |
| Invalidity and death, up to one ceiling | 1.30% | "Invalidité - décès en métropole Base de calcul Taux Revenus dans la limite de 48" |
| CSG and CRDS on earned income | 9.70% | "Revenus d'activité 9,70 % Revenus de remplacement 6,70 %" |
| Minimum yearly basic pension contribution, due even with no profit | EUR 967 | "5 409 € (450 × Smic horaire) Taux 17,87 % Montant minimal annuel 967 €" |
| Acre, business created in 2026: income at or below which the exemption is a quarter of the listed contributions | EUR 36,045 | "Revenu inférieur ou égal à 36 045 € (75 % du Pass)" |

The health and family scales are progressive; their bands are in `fr-social-contributions`.

**Optimisation strategies**

| Strategy | Detail |
| --- | --- |
| Acre in the first year | For a business created in 2026 the Acre exemption may be granted, under conditions, for 12 months. At an income at or below the amount in the table above it equals a quarter of the health and maternity, daily benefit, family, basic pension and invalidity-death contributions; between that amount and one annual ceiling it tapers; above one annual ceiling there is none. Check eligibility and whether a request is needed in `fr-social-contributions`. The live text called it a flat half reduction, automatic for micro-entrepreneurs; that is not what the URSSAF page sets out. |
| Micro-social or real base | Micro-social contributions are a share of turnover (Section 2). Under the régime réel they follow profit after costs. With high costs, compare both. |
| Minimum contributions | Some contributions have a yearly minimum that is due even in a loss year; the basic pension minimum is in the table above. |
| Collaborating spouse | A spouse who works in the business without pay can be covered as a conjoint collaborateur; the cost and the options are in `fr-social-contributions`. |
| Retirement plan payments | Madelin-type and retirement plan payments deducted from the business profit reduce the profit that income tax is charged on. They must not be assumed to reduce the ordinary reformed social base: the actual 2026 declaration notice expressly adds back the tax-exempt/deducted 154 bis Madelin and PER amounts before the social allowance. Use the exact statutory base and exceptions in `fr-social-contributions`; do not promise the old illustrative 10% social saving. |

## Section 9: Investment and retirement

### Retirement savings plan (PER): CGI art. 163 quatervicies and art. 154 bis

**Retirement savings deduction ceilings**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/12-charges_ded_rev_225a236.pdf |
| Payments made in 2025 (income of 2025): 10% of 2024 net earned income, capped at | EUR 37,094 | "37 094 €) ou 10 % du plafond annuel de la sécurité sociale si ce" |
| Payments made in 2025: floor of the ceiling | EUR 4,637 | "(montant minimum : 4 637 €)" |
| Payments made in 2026 (income of 2026): 10% of 2025 net earned income, capped at | EUR 37,680 | "sécurité sociale (montant maximum : 37 680 €) ou 10 % du plafond" |
| Payments made in 2026: floor of the ceiling | EUR 4,710 | "annuel de la sécurité sociale (montant minimum : 4 710 €) si ce" |
| Share of earned income that sets each year's ceiling | 10% | "10 % des revenus d’activité nets de frais professionnels de l’an-" |
| Self-employed: part of the profit between one and eight social security ceilings used in the separate business-profit deduction | 15% | "15 % de la quote-part du bénéfice imposable comprise entre une" |

How the ceiling works, as the brochure states it:

- The ceiling for payments deducted from global income is the higher of the share of the previous year's net earned income (capped at eight annual social security ceilings) and the floor, reduced by the previous year's payments deducted from business profit (net of the 15 % part in the table) and by employer payments into company retirement plans. A person with no earned income still has the floor.
- Spouses and PACS partners taxed together may pool their ceilings (box 6QR).
- For income of 2025 the unused ceiling carries forward for the next three years. Current CGI 163 quatervicies has a five-year rule, and the Ministry explains its use from payments made in 2026 while expressly retaining a three-year limit for the unused ceilings of 2024 and 2025. Do not relabel all legacy vintages as five-year capacity. Current CGI 163 quinvicies removes the listed tax advantages for payments made by the owner into a modern PER or French PEPP sub-account FROM the seventieth birthday, effective 1 January 2026; do not extend that exact contract/owner gate to every legacy retirement product (https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/nouveautes.pdf). The earlier global-income ceilings were corrected. The separate business-profit formula below is derived from CGI154bis; it is not the global-income allowance or an automatic tax saving.
- Payments deducted from global income cannot create or increase a global deficit.
- For the separate CGI154bis business-profit retirement route, first establish a qualifying BIC/BNC owner, covered contract/payment and benefit under I/II1°, absence of the non-deduction election, and the applicable modern-PER/PEPP age gate above. With B the qualifying taxable profit and P the annual social-security ceiling, the gross limit is max(10% × min(B,8P) + 15% × max(0,min(B,8P) − P), 10% × P). Include the specified exempt business profits and exclude long-term professional gains/losses as the article directs. Reduce this limit by the enterprise-plan sums exempt under CGI81(18°a/a bis), and deduct only actual eligible payments within the resulting capacity. Use the2026 PASS of EUR48,060 in Section8 for this2026 business calculation. Do not deduct the same payment again from global income: for the global-income capacity reduction, the business deduction is taken net of the15% component, as the brochure states. A derived formula is not a universal precomputed allowance; the chosen EUR15,750 example remains a chosen payment, not a ceiling.

When the deduction pays: the deduction saves tax at the household's marginal band. At a 0% or low band, the option not to deduct, which leaves the capital taxed more lightly at exit, may be better. Exit taxation depends on whether the payments were deducted and on the form of exit; confirm it with `fr-capital-gains` before advising.

### Life insurance (assurance-vie)

**Life insurance: yearly allowance on gains**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/08-RCM_121a136.pdf |
| Yearly allowance on gains from contracts of at least 8 years, single person | EUR 4,600 | "les produits des contrats d'au moins 8 ans ... bénéficient d'un abattement de 4 600 € (personne seule) ou 9 200 € (couple soumis à imposition commune)" |
| Same, couple taxed together | EUR 9,200 | same quote |

Payments into life insurance are not deductible from income. Which gains the allowance covers, and the order in which it is used, are set out in that passage of the brochure; they depend on the age of the contract and the dates of the premiums. The income tax rate on the gains depends on the age of the contract and on when the premiums were paid, and the social levies keep the lower total in 2026 (Section 2): see `fr-capital-gains`. The live text also printed an inheritance allowance per beneficiary; inheritance is outside this skill and no allowed page was read for it, so it is removed.

### Tax credits and reductions

**Help at home and gifts, income of 2025**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/13-RICI_2042_237a256.pdf |
| Help at home (emploi à domicile), CGI art. 199 sexdecies: tax credit as a share of eligible spending | 50% | "égal à 50 % des dépenses retenues dans la" |
| Spending limit, general case | EUR 12,000 | "12 000 € majorée de 1 500 €" |
| Increase per dependent child and in the other listed cases | EUR 1,500 | same quote |
| Limit in the first year the household claims the credit for the direct employment of an employee at home | EUR 15,000 | "Le plafond de 12 000 € est porté à 15 000 € pour la première" |
| Ceiling once the increases are added, general case | EUR 15,000 | "sans pouvoir excéder 15 000 € (ou 18 000 €)" |
| Ceiling once the increases are added, first year | EUR 18,000 | same quote |
| Limit for the stated invalidity population, without extra increase | EUR 20,000 | The actual brochure names carte d’invalidité/CMI “invalidité”, third-category invalidity pension, or disabled-child special-education supplement; do not substitute any generic disability card |
| Gifts to organisations of general interest, CGI art. 200: reduction | 66% | "de 66 % dans la limite de 20 % du revenu" |
| Ceiling of those gifts, as a share of taxable income | 20% | same quote |
| Gifts to organisations giving free meals, care or housing to people in difficulty: reduction | 75% | "réduction d’impôt égale à 75 % des verse" |
| Gifts to those organisations made from 14 October to 31 December 2025, limit including earlier 2025 gifts | EUR 2,000 | "au 31.12.2025, dans la limite de 2 000 € (y compris les sommes" |

The first-year limit applies only to direct employment of an employee; it does not apply to spending through a service provider. The EUR 1,500 child increase is EUR 750 for alternating custody. Net any aid off the actual spending and apply each service subcap before the household cap, then the 50% credit.

The help-at-home relief is a tax credit (crédit d'impôt), not a reduction as the live text called it. Gifts at the higher rate above their limit fall into the general rate and its ceiling. For gifts to those organisations made from 1 January to 13 October 2025 the page prints a lower maximum than the limit in the table above (line 7UD). The 2026 brochure news page says the limit for the meals and care organisations was raised for gifts made from 14 October 2025 (finance law for 2026, art. 28), so it is the limit in force for gifts made during 2026 (https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/nouveautes.pdf). The live text gave a lower limit.

The live text also listed a reduction for subscriptions to the capital of small companies (IR-PME) with rates and caps. The 2026 brochure news page says that reduction is being reshaped for 2026; the rates and caps were not read on an allowed page in this pass, so they are removed. Use the 2042 RICI chapter of the brochure before advising on it.

### Overall cap on tax advantages (plafonnement des niches)

**Overall cap**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/plafonnement.pdf |
| Overall yearly cap on the advantages concerned | EUR 10,000 | "10 000 €, majorée de 8 000 € pour les réductions d'impôt en" |
| Increase for the overseas investment reductions and some capital subscriptions listed on the page | EUR 8,000 | same quote |

The cap (CGI art. 200-0 A) covers most reductions and credits that reward a spending or an investment, including help at home. It does not cover every relief: the page lists what is in and what is out. Any excess over the cap is added back to the tax due. Add up the client's capped advantages before recommending another one.

## Section 10: Red lines

**Penalties on a reassessment**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/4911-PGP.html |
| Deliberate breach (manquement délibéré), CGI art. 1729 | 40% | "la majoration de 40 % pour manquement délibéré prévue par l’article 1729 du CGI" |
| CGI1729(b) L64 abuse: principal initiative OR principal beneficiary; CGI1729(c) fraudulent manoeuvres | 80% | "80 % en cas d'abus de droit"; "initiative principale ... ou ... principal bénéficiaire" |

The 80% row on the BOFiP page reads "Rappels avec abus de droit (le service a établi que le contribuable est le bénéficiaire principal de l'abus de droit) ou manœuvres frauduleuses". The live text printed a separate surcharge for the "mini abuse of law" (LPF art. L64 A); no allowed page read in this pass prints one, so it is removed. Treat any arrangement whose main purpose is tax as a referral (see "When to refuse or refer"). That BOFiP comparison wording does not replace the complete CGI1729(b) test: the80% L64-abuse surcharge falls to40% when neither principal initiative nor principal-beneficiary status is established. Principal initiative alone can therefore retain80%. This is separate from1729(c) fraudulent manoeuvres and does not create an automatic L64A penalty; see `fr-tax-audit`.

**Red lines**

| Risk | Detail |
| --- | --- |
| Abuse of law (LPF art. L64) | An arrangement set aside under the abuse of law procedure bears the penalty in the table above at80% where principal initiative OR principal-beneficiary status is established, reduced to40% when neither is established under CGI1729(b). |
| Overall cap on tax advantages | Advantages above the cap in Section 9 are added back to the tax. Planning that stacks reliefs past the cap gains nothing. |
| Non-professional activities | Losses from non-professional activities only offset income of the same kind (Section 5). |
| Covered retirement-plan payments from the seventieth birthday | From 1 January 2026 apply the modern-PER/French-PEPP owner/payment gate in Section 9, rather than a universal rule for every old retirement contract. |
| Micro regime with high costs | Choosing the micro regime when real costs exceed the flat allowance means paying tax on profit that does not exist. Always compare. |
| VAT franchise with business customers | Staying in the franchise gives no price advantage with business customers and blocks recovery of VAT on costs. |
| Backdated invoices or payments | Moving income or costs between years works only when the payment date really moves. Changing documents to move a year is fraud. |

## Section 11: Annual tax planning calendar

The 2026 return for income of 2025 had these online deadlines: Thursday 21 May (départements 01 to 19 and non-residents), Thursday 28 May (départements 20 to 54) and Thursday 4 June (départements 55 to 974 and 976), and Tuesday 19 May for the paper return (https://www.impots.gouv.fr/les-modalites-de-la-declaration-de-revenus-en-2026). The dates for the 2027 return are not yet published; expect them in spring 2027 and confirm on impots.gouv.fr.

**Annual tax planning calendar**

| Month | Action |
| --- | --- |
| January | Review last year's profit. Plan this year's retirement plan payments against the ceiling in Section 9. Check Acre eligibility for a new business. |
| February | Gather documents: bank statements, invoices, contribution statements, retirement plan statements, gift receipts. |
| March | Decide whether the micro regime or a real regime suits this year, and when an option must be made; for a new business, see Section 2. |
| April | The online return service opens. Declare retirement plan payments, gifts and help at home. |
| May and June | Filing deadlines by département (see above). |
| July | Review the contribution instalments against the expected profit. |
| August | Mid-year profit review. Consider bringing forward or deferring costs and receipts within the rules of Section 6. |
| September | Request the micro flat income tax payment before 30 September for it to apply from next 1 January (Section 2). Review investment plans before December. |
| October | Work out the retirement plan ceiling still available. |
| November | Make retirement plan payments and gifts intended for this year. Arrange help at home. |
| December | 31 December: retirement plan payments, gifts and investments must be paid by this date to count for this year. Settle the invoicing timing for any receipt that can genuinely move to January. |

## Section 12: Worked method examples

The three method examples below remain. The six earlier numerical populations are also retained after them with their original inputs, corrected arithmetic and explicit eligibility/year assumptions. A result computed from sourced parameters is a calculation, not a figure that an official page must itself print. None is a complete tax or social-contribution assessment.

### Example 1: Micro-BNC or régime réel (hypothetical client)

A single consultant with BNC turnover inside the micro limit and real costs that are a large share of turnover. Step 1: micro profit is turnover less the BNC flat allowance (Section 2 table). Step 2: real profit is turnover less the real costs, including depreciation. Step 3: apply the income tax scale per share to each profit (Section 1). Step 4: compare the social contributions: the micro-social rate on turnover against the real-base contributions on profit (Sections 2 and 8). Step 5: choose the lower total and note the bookkeeping cost of the régime réel.

### Example 2: Retirement plan payment (hypothetical client)

A self-employed person asks how much to pay into a retirement plan before 31 December 2026. Step 1: take the ceiling for payments made in 2026 from Section 9, using the client's 2025 net earned income. Step 2: add any unused ceiling still available from earlier years. Step 3: subtract the previous year's payments deducted from the business profit (net of the 15 % part in the table) and employer payments into company retirement plans. Step 4: the tax saved is the deducted amount times the marginal band rate, and no more than the tax the household would otherwise pay. Step 5: check the client's age against the rule for people aged 70 and over.

### Example 3: Help at home (hypothetical client)

A household employing a cleaner directly at home. Step 1: take eligible spending net of any aid. Step 2: cap it at the limit in Section 9 for the household's situation; the first-year limit applies only because the employee is employed directly. Step 3: apply the credit rate. Step 4: add the advantage to the client's other capped advantages and test the overall cap.

### The six historical numerical populations, recomputed

1. **PER, BNC EUR 100,000 and a 41% marginal slice.** Keep the former EUR 15,750 as a CHOSEN eligible payment, not as the old unverified ceiling formula. Assume its actual available business/global deduction ceiling is independently established, the owner is below the applicable age gate, no double deduction, and all EUR 15,750 reduces income otherwise taxed at 41%. The income-tax effect is 15,750 × 41% = EUR 6,457.50 before assessment rounding, approximately the old EUR 6,458. The old EUR 1,575 social saving is not supported: the reformed ordinary social base adds back the covered 154 bis payments. A EUR 100,000 BNC label alone does not establish either the ceiling or this marginal-band assumption.

2. **Micro-BNC turnover EUR 60,000, actual deductible costs EUR 25,000.** For a single adult with no other income or relief, treating these as income of 2025 declared in 2026 and independently eligible for each compared regime: micro taxable profit is 60,000 × (1 − 34%) = EUR 39,600; real profit is 60,000 − 25,000 = EUR 35,000. The current scale gives EUR 4,983.99 versus EUR 3,603.99 before whole-euro assessment rounding, or EUR 4,984 versus EUR 3,604, an income-tax difference of EUR 1,380. The old EUR 5,510/EUR 4,130 estimates are superseded. This excludes social contributions, the costs’ tax/social timing and any opt-out eligibility or administration cost.

```oa-check
name: France optimization restored comparison 1
inputs:
  turnover: 60000
  allowance: 0.34
  costs: 25000
  zero_band: 11600
  band2_top: 29579
  band2_rate: 0.11
  band3_rate: 0.3
steps:
  - micro_profit: turnover*(1-allowance)
  - real_profit: turnover-costs
  - micro_tax: (band2_top-zero_band)*band2_rate+(micro_profit-band2_top)*band3_rate
  - real_tax: (band2_top-zero_band)*band2_rate+(real_profit-band2_top)*band3_rate
  - difference: micro_tax-real_tax
expected:
  micro_profit: 39600
  real_profit: 35000
  micro_tax: 4983.99
  real_tax: 3603.99
  difference: 1380
```

3. **EUR 80,000 taxable household income, single versus married with two dependent children.** These are two separate fictional household populations for income of 2025, not a tax saving that a single person can elect. One-share tax is EUR 17,103.99. For the eligible joint household, three-share tax before the quotient cap is EUR 4,972; the two-share baseline is EUR 10,207.98. Two additional half-shares permit at most 2 × 1,807 = EUR 3,614 of advantage, so capped tax is EUR 6,593.98, rounded EUR 6,594. The difference from rounded single tax EUR 17,104 is EUR 10,510. The old EUR 15,673/EUR 7,236/EUR 8,437 figures are superseded; other household gates, special caps, reductions and credits are excluded.

4. **EUR 6,000 eligible help-at-home spending.** Assume direct employment, no aid, no competing capped advantages and spending entirely on eligible cleaning within the applicable household ceiling. The refundable credit is 6,000 × 50% = EUR 3,000. The original gardening/cleaning label did not establish allocation: if any amount is gardening, first apply its own EUR 5,000 service subcap. Do not assume EUR 6,000 entirely on gardening qualifies.

```oa-check
name: France optimization restored comparison 2
inputs:
  eligible_cleaning: 6000
  household_cap: 12000
  credit_rate: 0.5
steps:
  - capped_spending: min(eligible_cleaning,household_cap)
  - credit: capped_spending*credit_rate
expected:
  capped_spending: 6000
  credit: 3000
```

5. **EUR 80,000 eligible CSG base, deduction at a 30% marginal slice.** Assume the precise income is eligible for the 6.8-point deduction, the CSG was paid in the deductible year, no excluded PFU or proportionate-relief adjustment, and the full deduction stays in the 30% slice. Then 80,000 × 6.8% = EUR 5,440 deducted, and 5,440 × 30% = EUR 1,632 income-tax effect. This is not an extra credit or a deduction of 6.8% of the CSG bill; the full CSG/CRDS levy is separate.

6. **BNC, one owned six-CV non-electric car entered on the professional asset register, 15,000 actual eligible business kilometres in 2025.** The official 2026 schedule for income of 2025 gives (d × 0.374) + 1,457 in the 5,001–20,000-km band. The computed amount is 15,000 × 0.374 + 1,457 = EUR 7,067; if all of that deduction reduces income in a 30% marginal slice, the illustrative income-tax effect is EUR 2,120.10. The old EUR 5,500/EUR 1,650 estimates are superseded. Assume the actual full-year BNC mileage election and required records are established; apply its exclusivity to all relevant vehicles/costs, with no duplicate actual-cost deduction; this dated 2025-income schedule is not asserted to be a future 2027-return schedule. Source: https://www.impots.gouv.fr/sites/default/files/media/3_Documentation/depliants/nid_4002_gp_120.pdf .

## The method, step by step

1. Fix the year. Decide whether the question is about income of 2025 declared in 2026, or about decisions taken during 2026 for income of 2026. Use the table that matches. Scale and limits: https://www.service-public.gouv.fr/particuliers/vosdroits/F1419
2. Fix the regime. Find whether the client is under the micro regime or a real regime, and whether it can or must change, using the two-year test and the turnover limits (CGI art. 50-0 and art. 102 ter; https://entreprendre.service-public.gouv.fr/vosdroits/F23267).
3. Compare micro and real. Compute the profit and the social contributions both ways (Sections 2 and 8; https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/lessentiel-du-statut.html and https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-ac-plnr.html).
4. Compare structures where the profit is large. Compute the entrepreneur individuel and the company at corporation tax side by side, including pay, dividends, levies and contributions (Section 2; https://entreprendre.service-public.gouv.fr/vosdroits/F23575 and https://www.service-public.gouv.fr/particuliers/vosdroits/F2613).
5. Claim the deductions. Go through Section 3 and Section 4 under the régime réel (https://bofip.impots.gouv.fr/bofip/2109-PGP.html and https://bofip.impots.gouv.fr/bofip/4699-PGP.html).
6. Use the losses. Classify each loss as professional or not and apply the matching rule (Section 5; https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/12-charges_ded_rev_225a236.pdf).
7. Size the retirement plan payment within the ceiling and the carry-forward (CGI art. 163 quatervicies; Section 9, same brochure chapter).
8. Add the credits and reductions, then test the overall cap (CGI art. 199 sexdecies, art. 200 and art. 200-0 A; https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/13-RICI_2042_237a256.pdf and https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/plafonnement.pdf).
9. Check VAT. Decide whether the franchise or an option suits the client's customers and investment plans (CGI art. 293 B; https://entreprendre.service-public.gouv.fr/vosdroits/F21746).
10. Check every idea against the red lines in Section 10 (LPF art. L64; https://bofip.impots.gouv.fr/bofip/4911-PGP.html). Give the client the estimate with its assumptions, and the dates by which each choice must be made.

## Ask the client first

- Is your business under the micro regime or a real regime, and what were your turnover excluding VAT and your real costs in 2024, 2025 and so far in 2026?
- Is the activity carried on professionally (it is your occupation, with the time and income that implies), or alongside a salary or pension?
- How many parts does your household have, and what other income does it have (salaries, pensions, rents, dividends)?
- When did the activity start, and did you claim Acre or the flat income tax payment?
- How much have you paid into retirement plans in the last five years, and how old are you and your spouse or partner?
- Who are your customers: private individuals or businesses, in France or abroad?

## When to refuse or refer

- Any arrangement whose main purpose is to obtain a tax advantage, or that relies on documents that do not match what happened. Refer; do not design it.
- Moving to a company, transferring a business or reorganising share ownership: the comparison in Section 2 is a starting point only. Refer to an accountant for the company law, social and transfer-tax effects (`france-formation` for the setup steps).
- A household that already uses several capped reliefs, or overseas, SOFICA or rental investment reductions: the overall cap must be computed by a professional.
- Leaving France, or arriving: the exit tax and residence rules are outside this skill; see `leaving-france-exit-tax`.
- Dividends paid to a manager who is also self-employed: check whether part of the dividend bears social contributions before giving any figure (`fr-social-contributions`).
- Agricultural income, professional furnished lets, property held through companies, and inheritance planning: outside this skill (`fr-rental-income` for lets).
- A tax audit under way: use `fr-tax-audit`.

## Sources

- Income tax scale, income of 2025: https://www.service-public.gouv.fr/particuliers/vosdroits/F1419
- Family quotient cap: https://bofip.impots.gouv.fr/bofip/2494-PGP.html/identifiant=BOI-IR-LIQ-20-20-20-20260407
- Micro regime, flat income tax payment: https://entreprendre.service-public.gouv.fr/vosdroits/F23267
- Micro-entrepreneur social rates and Acre rates: https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/lessentiel-du-statut.html
- Corporation tax and the simplified VAT band: https://entreprendre.service-public.gouv.fr/vosdroits/F23575
- Dividends and the flat tax: https://www.service-public.gouv.fr/particuliers/vosdroits/F2613
- Social levies on investment income: https://www.service-public.gouv.fr/particuliers/vosdroits/F2329
- VAT franchise en base: https://entreprendre.service-public.gouv.fr/vosdroits/F21746
- Self-employed contribution reform: https://www.urssaf.fr/accueil/independant/comprendre-payer-cotisations/reforme-cotisations-independants.html
- Self-employed contribution rates 2026: https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-ac-plnr.html
- Small equipment tolerance: https://bofip.impots.gouv.fr/bofip/2109-PGP.html
- Declining balance coefficients: https://bofip.impots.gouv.fr/bofip/4699-PGP.html
- Penalties: https://bofip.impots.gouv.fr/bofip/4911-PGP.html Selected CGI1729(b), CGI219I-b, CGI154bisI/II, household-brochure and capital-levy commencement scopes reread31October2026; exact original-language quotations and source URLs are in the ledger. CGI154bis: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047288764/2026-05-08 .
- Training credit for business managers ended: https://entreprendre.service-public.gouv.fr/vosdroits/F23460
- Return deadlines 2026: https://www.impots.gouv.fr/les-modalites-de-la-declaration-de-revenus-en-2026
- Brochure pratique 2026, news: https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/nouveautes.pdf
- Brochure pratique 2026, charges deductible from income (retirement savings, deficits): https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/12-charges_ded_rev_225a236.pdf
- Brochure pratique 2026, credits and reductions on the 2042 and 2042 RICI: https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/13-RICI_2042_237a256.pdf
- Brochure pratique 2026, overall cap: https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/plafonnement.pdf
- Brochure pratique 2026, investment income: https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/08-RCM_121a136.pdf
- Brochure pratique 2026, self-employed income: https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/11-revenus_non_salaries_161a182.pdf

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this skill is maintained at openaccountants.com.

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
