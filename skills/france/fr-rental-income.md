---
name: fr-rental-income
description: "French rental income taxation: revenus fonciers, LMNP, LMP, and SCI à l'IR. Trigger on phrases like \"revenus fonciers\", \"location nue\", \"location meublée\", \"LMNP\", \"LMP\", \"meublé de tourisme\", \"micro-foncier\", \"régime réel foncier\", \"déficit foncier\", \"micro-BIC location\", \"amortissement LMNP\", \"SCI à l'IR\", \"SCI transparence fiscale\", \"Airbnb France impôts\", \"déclaration 2044\", \"déclaration 2031\", \"liasse BIC meublé\", \"charges déductibles location\", \"travaux déductibles foncier\", \"bascule LMP LMNP\", \"loi Le Meur meublé tourisme\", \"location saisonnière fiscalité\", \"déficit imputable revenu global\". Covers bare rental (micro-foncier and réel), furnished rental (LMNP micro-BIC and réel with amortisation), LMP status, SCI à l'IR, and déficit foncier rules."
version: 1.3
jurisdiction: FR
tax_year: 2026
last_updated: 2026-10-31
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# France: rental income (revenus fonciers, LMNP, LMP, SCI à l'IR)

> **Based on work by [Romain Simon (@romainsimon)](https://github.com/romainsimon/paperasse)**, licensed under MIT. Adapted for the OpenAccountants format.

This skill covers how an individual resident in France is taxed on letting property: unfurnished lets (revenus fonciers, micro-foncier or régime réel), furnished lets by a non-professional (LMNP, micro-BIC or réel), professional furnished letting (LMP), and property companies taxed at income tax (SCI à l'IR). Figures are for tax year 2026. France taxes the previous year's income, so each table says which figures govern rents received in 2025 and declared in 2026, and which govern rents received during 2026, declared in 2027; where a page prints no separate 2026 figure, the table says so. The rules stated are those printed on the official pages read between 19 September and 19 October 2026.

## Section 1: Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | France |
| Taxes covered | Income tax (impôt sur le revenu) on rental income, and the social levies (prélèvements sociaux) on it |
| Currency | EUR only |
| Tax year | Calendar year; rents of year N are declared in spring of year N+1 |
| Key forms | 2042 (box 4BE for micro-foncier, 4BA and following for réel), 2044 or 2044 spéciale, 2042-C-PRO, 2031 with the 2033 schedules where the simplified real regime applies, 2072-S or 2072-C for an SCI |
| Main law | CGI art. 14 and following and art. 32 (revenus fonciers), art. 156 I 3° (déficit foncier), art. 50-0 (micro-BIC), art. 155 IV (LMP), art. 156 I 1° ter (LMNP deficits), art. 39 C (amortisation limit), art. 8 (SCI) |
| Related skills | `fr-personal-income-tax` (the household computation), `fr-capital-gains`, `fr-social-contributions`, `fr-cfe`, `france-tax-optimization` |

## Section 2: Fundamental distinction

**Fundamental distinction**

| Type of rental | Income category | Regimes |
| --- | --- | --- |
| Bare / unfurnished (location nue) | Revenus fonciers | Micro-foncier or régime réel |
| Furnished, non-professional (LMNP) | BIC (bénéfices industriels et commerciaux) | Micro-BIC or réel |
| Furnished, professional (LMP) | BIC, professional | Micro-BIC if the type/year eligibility test is met and no réel election, or réel; see Sections 4.1 and 5 |
| SCI at IR (not liable to corporation tax) | Revenus fonciers, each partner on their share | As bare rental |
| SCI at IS | Corporation tax | Out of scope |

**Classic error:** declaring a furnished let as revenus fonciers. The impots.gouv.fr page on furnished letting (linked in Section 4) says the income from letting furnished accommodation is taxed "dans la catégorie des bénéfices industriels et commerciaux (BIC)". A let is furnished when it has all the furniture needed for normal occupation by the tenant (décret n°2015-981 du 31/07/2015, named on the same page).

## Section 3: Bare rental (location nue): revenus fonciers

### 3.1 Micro-foncier

**Micro-foncier parameters (BOFiP BOI-RFPI-DECLA-10)**

| Parameter | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/3973-PGP.html |
| Annual statutory gross bare-rental receipts, including the additions and eligible proportional gross shares below, whole tax household, must not exceed | EUR 15,000 | "revenu brut foncier annuel n’excède pas 15 000 €"; the Brochure chapters print it for rents received in 2025 and the pages read print no different limit for rents of 2026 |
| Flat allowance, applied automatically | 30% | "l’application d’un abattement de 30 %"; it stands for every charge |

- **Who and when.** Micro-foncier applies by right (de plein droit) to a household whose total gross rents from unfurnished letting in the year do not exceed the limit in the table above, and which does not let property under one of the special regimes listed below (BOFiP, linked above, § 20). The 2026 Brochure pratique, chapter on revenus fonciers (linked in Sources), says the limit is tested on rents received in the year, "charges non comprises", "quelle que soit la durée de la location", and is not applied pro rata. The statutory gross input also includes ancillary receipts, normally-landlord expenses contractually put on the tenant, and grants or indemnities financing deductible charges; exclude tenant payments for charges legally borne by the tenant. Where eligible under the direct-bare-property and other tests below, add the proportional **gross** SCI or FPI receipts, not merely the net distribution. If VAT applies, test the limit excluding VAT. Direct rents EUR 10,000 plus an eligible SCI gross share EUR 7,000 gives EUR 17,000 and fails micro, even if the SCI net taxable share is below EUR 5,000.
- **Cliff, not allowance.** If gross rents exceed the limit, the whole of the rental income goes to the régime réel; there is no partial micro regime.
- **How to declare.** Enter gross rents on form 2042, box 4BE. No form 2044 is filed. No deficit can arise under micro-foncier, because the flat allowance replaces every actual charge. After the 30% allowance, deduct eligible still-live prior réel-regime rental losses against the resulting net rental income under the Section 3.3 vintage ledger; micro prevents a new actual-expense loss, not use of those carried losses.
- **Who is excluded (BOFiP § 60 and § 70).** A household is outside micro-foncier when any member owns a classified historic monument (monument historique) whose deficit is set against global income; or a dwelling for which one of the art. 31 deductions is claimed (Périssol, Besson neuf, Robien, Borloo neuf, Besson ancien, Robien ZRR, Borloo ancien, Cosse); or property under the art. 199 decies EA or 199 decies F tourism reductions or the Loc'Avantages reduction (art. 199 tricies); or certain shares (parts of a non-transparent company letting such property, Robien SCPI or Borloo SCPI parts). A holder of SCI parts or FPI units who owns no directly let unfurnished property is also outside micro-foncier and reports the share of net income directly on form 2042.
- **Who is NOT excluded.** BOFiP § 60 says the Scellier, Duflot, Pinel, Denormandie and Malraux income tax reductions do not prevent micro-foncier. Partners of an art. 8 SCI letting bare property can use micro-foncier only if they also own at least one property let unfurnished directly (BOFiP § 50).

### 3.2 Régime réel

- **Mandatory or by option.** The régime réel applies when gross rents exceed the micro-foncier limit, or when a household within the limit opts for it by filing a form 2044. The 2026 Brochure pratique, chapter on revenus fonciers, says "Cette option est irrévocable pendant trois ans"; after those three years, each 2044 filed counts as the option for that year only.
- **Forms.** Net income or deficit is computed on form 2044 or form 2044 spéciale, then carried to form 2042, box 4BA and the boxes after it. The 2044 spéciale is needed for the special regimes (2026 Brochure pratique, chapter on form 2044, linked in Sources).

**Deductible charges (2026 Brochure pratique, chapter "Déclaration des revenus fonciers no 2044")**

| Charge | Deductible? | Notes from the chapter |
| --- | --- | --- |
| Loan interest for acquiring, building, repairing or improving the let property | Yes, from rental income | The part of a deficit that comes from interest cannot go against global income: see 3.3 |
| Repair and maintenance; improvement works on residential premises | Yes, subject to the relevant expense conditions | Construction, reconstruction, extension and works changing the building’s use are excluded. Improvements to professional/commercial premises qualify only for the stated disability-access or asbestos-protection cases; construction/reconstruction/extension remains excluded |
| Taxe foncière | Yes, unless the lease puts it on the tenant | The household waste tax (TEOM) on the same notice is not deductible: it is a charge paid for the tenant and recovered from them |
| Insurance premiums, including landlord's insurance | Yes | Premiums on crops, livestock, equipment or furniture are not |
| Administration and management fees paid to third parties (agency, managing agent) | Yes, actual amount | Other management costs: EUR 20 per qualifying local. A local includes its immediate dependencies let to the same tenant; two apartments each with a garage let to that apartment tenant give two locals/EUR 40, not four/EUR 80. Costs covered by that flat amount cannot also be deducted actually or topped up because actual correspondence, travel or telephone costs are higher. For bare land, count the letting to each tenant: adjacent parcels forming one lot let to the same tenant get one amount; non-adjacent parcels each get their own EUR 20 amount |
| Co-ownership provisions voted by the general meeting and paid to the syndic | Eligible collective provisions are deducted for their applicable payment year; separately paid non-provisioned works follow their own rules | On approval of the accounts, reconcile the prior deduction: add back the non-deductible-spending component, tenant-charge component and unused positive balance. A qualifying negative approved balance instead gives an additional deduction. Example: EUR 3,000 deducted, approved spending EUR 2,800 including EUR 400 non-deductible and EUR 300 tenant charges, unused EUR 200: add back EUR 900, not EUR 200. The 2026 brochure illustrates the 2025-return regularisation of 2024 provisions; its 2044 lines are not a promise of 2027 layout |
| Charges the landlord should have recovered from the tenant (charges locatives) | No, as a rule | Exception: tenant charges paid on the tenant’s behalf and still unrecovered at 31 December of the year of departure |

- **Construction, reconstruction and extension works are not deductible** from rental income. The Brochure chapter on form 2044 says these works must not affect "la structure de l’immeuble".

### 3.3 Déficit foncier (rental loss)

**Déficit foncier limit on global income (2026 Brochure pratique, chapter on form 2044)**

| Rule | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/19-decla_rev_fonciers_341a364.pdf |
| Yearly limit for setting the part of a deficit that does not come from loan interest against global income | EUR 10,700 | "est imputable sur le revenu global dans la limite de 10 700 €" |

**Raised limit for energy renovation works (2026 Brochure pratique, "Principales nouveautés")**

| Rule | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/nouveautes.pdf |
| Raised yearly limit where the deficit comes from energy renovation works moving a dwelling from class E, F or G to class A, B, C or D | EUR 21,400 | "global à hauteur de 21 400 € en cas de dépenses de rénovation"; the chapter on form 2044 ties it to works with a quote accepted from 5.11.2022 and paid from 1.1.2023 to 31.12.2025, and the nouveautés page says the limit is extended (prorogée) to 31.12.2027 (loi de finances 2026, art. 47) |

- **Which part goes where.** Only the part of the deficit made up of charges other than loan interest goes against global income, up to the limit in the first table above. The surplus over that limit, and the whole part that comes from loan interest, can be set only against rental income of the following 10 years (chapter on form 2044, deficits section). Keep each remaining loss by origin year and use the oldest eligible loss first, only against positive net rental income and never below zero. The ten following years include the tenth year: a 2016 rental-income carry remains usable in 2026, while a 2015 carry has expired before 2026. This also applies to still-live earlier réel losses after switching to micro: EUR 12,000 gross less 30% gives EUR 8,400, then a qualifying EUR 2,000 carried loss leaves EUR 6,400. The brochure's prior-year loss table is for 2025 income declared in 2026; preserve the legal vintage/expiry calculation separately for 2026 income, without assuming the 2027 box layout.
- **The letting condition.** Setting a deficit against global income is conditional on the property staying let until 31 December of the third year after that set-off. If the property is sold, or the letting stops, within that period, the rental income and global income of the years concerned are recomputed without the set-off. The chapter on form 2044 names the exceptions: dismissal, invalidity or death of the taxpayer or of the spouse, and expropriation of the property.
- **Raised limit, conditions.** The raised limit in the second table above needs proof of the energy class before the works (class E, F or G) and after them (class A, B, C or D). For works paid in 2026 or 2027, check the conditions of the extension with the impots.gouv.fr guidance for 2026 income before relying on it; the 2026 Brochure chapter describes the conditions as they stood for works paid by 31.12.2025.
- **Planning.** Bunching large works into one year to use the global income set-off is a lawful choice; this skill does not recommend it without the client's full picture. See `france-tax-optimization`.
- **New for 2026: a depreciation deduction for bare lets.** The nouveautés page says the 2026 finance law (art. 47, CGI art. 31) created a deduction of depreciation on part of the purchase price of a dwelling acquired for bare letting, with rent and tenant income ceilings and a nine-year letting commitment, for acquisitions or building permit requests between 21.2.2026 and 31.12.2028. This skill does not cover it: refer (see "When to refuse or refer").

### 3.4 Social levies on bare rental income

**Social levies on revenus fonciers (service-public.gouv.fr F2329)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.service-public.gouv.fr/particuliers/vosdroits/F2329 |
| Total social levies on rental income from unfurnished letting (revenus fonciers) | 17.2% | "Revenus fonciers ... TOTAL 17,2 %"; rental income was NOT moved to the higher rate |

- Revenus fonciers stay at the rate in the table above for income of 2025 declared in 2026 and for income of 2026. The 2026 Brochure pratique "Principales nouveautés" says the CSG rise on wealth income leaves "Les revenus fonciers, les plus-values immobilières, l’assurance-vie, l’épargne logement" at the old CSG rate. The higher rate that applies to furnished letting income is in Section 4.3. Never quote one rate for "rental income" without naming which kind.
- A French resident who works in another EEA state or in Switzerland and is affiliated to that country's compulsory social security owes only the solidarity levy, not CSG or CRDS (F2329, "À savoir").

## Section 4: Furnished rental: LMNP (location meublée non professionnelle)

### 4.1 Micro-BIC

- **Loi Le Meur.** The loi n° 2024-1039 of 19 November 2024 (art. 7) cut the micro-BIC limits and allowances for furnished tourist lets from income of 2025. The key split is now: chambres d'hôtes and classified tourist lets (meublés de tourisme classés); unclassified tourist lets (meublés de tourisme non classés); and all other furnished lets, including long-term furnished lets (location meublée de longue durée).

**Micro-BIC for furnished lets, income of 2025 declared in 2026 (impots.gouv.fr "Location meublée", modified 23/04/2026)**

| Type of furnished let | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/particulier/location-meublee |
| Receipts limit, chambres d'hôtes, classified tourist lets and other furnished lets (long-term) | EUR 77,700 | "77 700 € pour les locations de chambres d'hôtes et de meublés de tourisme classés ainsi que les autres activités de location meublée (location meublée de longue durée)" |
| Receipts limit, unclassified tourist lets | EUR 15,000 | "15 000 € pour les locations de meublés de tourisme non classés" |
| Flat allowance, chambres d'hôtes, classified tourist lets, and other furnished lets | 50% | "Un abattement forfaitaire de 50 % (avec un minimum de 305 €)" |
| Flat allowance, unclassified tourist lets | 30% | "Un abattement forfaitaire de 30 % (avec un minimum de 305 €)" |
| Minimum allowance in every case | EUR 305 | "minimum de 305 €" |

**Micro-BIC limits for income received in 2026, declared in 2027 (entreprendre.service-public.gouv.fr F23267, Vérifié le 13 mai 2026)**

| Type of furnished let | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F23267 |
| Turnover limit, classified tourist lets and chambres d'hôtes, tested on 2025 or 2024 | EUR 83,600 | "Meublé de tourisme classé et chambre d'hôtes (BIC) ... n’a pas dépassé 83 600 €" |
| Turnover limit, unclassified tourist lets, tested on 2025 or 2024 | EUR 15,000 | "Meublé de tourisme non classé (BIC) ... n’a pas dépassé 15 000 €"; unchanged from 2025 |
| Turnover limit, other furnished lets including long-term furnished lets (location meublée longue durée), tested on 2025 or 2024 | EUR 83,600 | "Activité de prestation de services, dont la location meublée longue durée (BIC) ... n’a pas dépassé 83 600 €" |

- **The test, and the two-year rule.** The impots.gouv.fr page says the micro regime applies when the receipts of the previous year "ou de l'avant-dernière année" do not exceed the limit. F23267 says crossing a limit in one year only does not end the regime: income of year N leaves micro-BIC only if the limit was exceeded in both N-1 and N-2. The allowances in the first table above apply from income of 2025 (nouveautés page: "À compter du 1.1.2025"); F23267 prints no different rate for 2026. BOFiP § 55 expressly makes this test depend on the type of letting, not whether the landlord is LMP or LMNP; annualise the receipts where its time-in-operation condition requires it.
- **Long-term furnished lets in 2026.** F23267 puts long-term furnished letting under its services tab: the micro regime applies to income received in 2026 if turnover in 2025 or in 2024 did not exceed the limit in the second table above.
- **2042-C-PRO boxes (LMNP, micro; 2025 income declared in 2026).** The impots.gouv.fr page lists them: 5NG, 5OG or 5PG for chambres d'hôtes and classified tourist lets; 5NH, 5OH, 5PH for unclassified tourist lets; 5NI, 5OI or 5PI for other furnished lets. Enter total receipts, including charges billed to the tenant; the allowance is applied automatically. Micro lets already charged social contributions by a social security body go on lines 5NJ to 5PL instead (2026 Brochure pratique, chapter on non-salaried income, linked in Sources).
- **Outside micro eligibility.** Where the actual two-prior-year test in this section fails, the réel regime applies (4.2). An otherwise eligible taxpayer may elect réel.

**Ordinary long-term LMP micro route.** Professional status does not force the réel regime. After testing the household LMP conditions in Section 5, test the same type-specific previous-two-year micro eligibility, applicable time-in-operation adjustment and any réel election in this section. For ordinary long-term furnished letting, use the 2025-income EUR 77,700 limit or the 2026-income EUR 83,600 limit as applicable. Micro taxable BIC is receipts less the 50% allowance, minimum EUR 305, floored at zero; do not also deduct actual charges or depreciation. With EUR 40,000 receipts, EUR 20,000 other compared household income and valid prior-year micro eligibility, no réel election and the LMP status gates met, taxable micro BIC is EUR 20,000 before the separate household and social-contribution computations. The 2026 brochure for 2025 income prints professional micro receipts in 5KP/5LP/5MP, with the allowance applied automatically. Those are dated campaign boxes, not a confirmed 2027 form layout. Do not extend this ordinary long-term branch to a different tourism category, a business-gain computation or an automatic micro-social rate. Sources: https://bofip.impots.gouv.fr/bofip/3610-PGP.html and https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/11-revenus_non_salaries_161a182.pdf
- **Micro-entrepreneur status is a different system.** A furnished let run as a micro-enterprise pays social contributions to Urssaf on turnover; see `fr-social-contributions`. Do not mix the micro-BIC income tax allowance with the micro-social rates.

### 4.2 Réel LMNP

- **Result.** Taxable profit = receipts minus deductible charges minus depreciation (amortissement), computed on form 2031 with the applicable real-regime schedules (2033 for the simplified real regime) and filed with the business tax office (SIE) of the property, or, with several properties, the SIE of the main home or of the largest furnished property (impots.gouv.fr page linked in 4.1). The profit goes to form 2042-C-PRO box 5NA, 5OA or 5PA; a deficit to 5NY, 5OY or 5PY.
- **Depreciation cannot create a loss.** BOFiP BOI-BIC-CHAMP-40-20 (§ 57, linked in Sources) says that under CGI art. 39 C, for an individual letting furnished property, the depreciation of the building and the furniture is deductible in a year only "dans la limite du montant du loyer acquis, diminué du montant des autres charges afférentes à ces biens". Current CGI art. 39 C II-3 expressly allows regularly booked depreciation not deductible because of this limit to be deducted in later years under the same conditions and ceiling. For an ongoing individual letting, track eligible prior deferred depreciation separately, combine it with otherwise eligible current depreciation and deduct no more than the positive rent-minus-other-charges capacity; retain the unused eligible balance for later years. This is a derived worksheet for the statutory carry-forward, not permission to carry permanently disallowed deductions under a different rule. Cessation and sale treatment require their separate art. 39 C II-3 checks and are not computed here. So depreciation can bring the result down to nil, but a deficit can come only from charges other than depreciation.
- **Land is never depreciated.** BOFiP § 58: land does not depreciate, and the landlord must split the value of the building from the value of the land on the balance sheet, on their own responsibility.
- **Depreciation rates and useful lives.** No allowed page read for this skill prints rates or lives for a furnished let (the legacy text gave ranges). Use the useful life of each component under the general BIC rules; see `france-bookkeeping`.
- **LMNP deficits.** A deficit of a non-professional furnished letting activity cannot go against global income (CGI art. 156 I 1° ter, BOFiP § 240). It can be set only against profits from the same activity over the following ten years, in the years in which the activity is not professional (BOFiP § 250; impots.gouv.fr page: "ne s’imputent que sur des revenus provenant de la même activité au cours des dix années suivantes"). Ordinary losses of an operating LMNP activity cannot be used against global income or LMP profits merely because the activity later becomes professional. The narrow first-letting exception below is separate.

**First-letting pre-completion exception.** BOFiP § 360 describes an immeuble acquired in VEFA with qualifying charges incurred before completion and before letting. If the taxpayer is LMP from the first letting, the unabsorbed deficit attributable to charges incurred for the direct or indirect letting before it begins can be deducted from global income by thirds over that local's first three letting years, while furnished letting continues professionally. Separate this amount from prior losses of an already operating LMNP activity. Stipulated eligible pre-letting charges EUR 9,000, first letting in 2026 with LMP status then and throughout 2026–2028: EUR 3,000 in each year. If the first-letting LMP gate fails, do not award this exception; do not invent rollover of a third when continued professional status fails. Wider startup/capitalisation qualification remains a separate factual test. Source: https://bofip.impots.gouv.fr/bofip/3610-PGP.html
- **Selling an LMNP property.** The gain is a private property gain (BOFiP § 290), not a business gain. For sales made from 15 February 2025, CGI art. 150 VB III reduces the acquisition price by depreciation admitted as a deduction under art. 39 C, subject to its specified expense and residence/establishment exceptions. This raises the gain, rather than adding depreciation to the cost. The broad F10864 phrase "réintégrés dans le prix d’acquisition" must not reverse that statutory direction. The holding period allowances then apply: full income tax exemption beyond the 22nd year and full social levy exemption beyond the 30th year (F10864). The gain computation is outside this skill: refer.

### 4.3 Social levies on LMNP income

**Social levies on wealth income and furnished letting income (service-public.gouv.fr F2329, Vérifié le 30 juin 2026)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.service-public.gouv.fr/particuliers/vosdroits/F2329 |
| Total social levies on wealth income (revenus du patrimoine), general case | 18.6% | "Revenus du patrimoine ... Cas général ... TOTAL 18,6 %"; F2329 lists "Revenus d'une location meublée (non professionnelle)" among the wealth income subject to the levies |
| Same total as printed for non-professional furnished letting income in the page's tab for people who live abroad | 18.6% | "Revenus de location meublée (non professionnelle) ... TOTAL 18,6 %" |

**Start date of the rise (2026 Brochure pratique, "Principales nouveautés")**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/nouveautes.pdf |
| CSG on wealth income, new rate, from income of 2025 for wealth income | 10.6% | "Le taux de la CSG est porté de 9,2 % à 10,6 % sur les revenus du patrimoine"; the same page says the rise applies from income of 2025 declared in 2026 for wealth income, and from 1.1.2026 for investment income (produits de placement) |

- **Rule.** LMNP income, micro or réel, bears the general wealth income rate in the first table above, from income of 2025 declared in 2026 (loi de financement de la sécurité sociale 2026, art. 12). The exception list in the nouveautés page names revenus fonciers, property gains, life insurance and housing savings, not furnished letting income. Bare rental income stays at the rate in Section 3.4.
- **No double charge.** The impots.gouv.fr page says LMNP income is charged the levies automatically, unless it has already borne social contributions through the social security bodies; in that case declare the profit on lines 5NM to 5PM (réel), or the micro receipts on lines 5NJ to 5PL, and the tax office does not charge the levies.

## Section 5: LMP (location meublée professionnelle)

**LMP receipts condition (impots.gouv.fr "Location meublée")**

| Condition | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/particulier/location-meublee |
| Annual furnished letting receipts of all members of the tax household must exceed | EUR 23,000 | "les recettes annuelles retirées de cette activité par l'ensemble des membres du foyer fiscal excèdent 23 000 €" |

### Conditions (both required)

- First, the household's annual receipts from furnished letting exceed the amount in the table above.
- And second, those receipts also exceed the household's other income taxed as salaries and wages (including pensions and life annuities, and the pay of managers and partners under CGI art. 62), BIC other than furnished letting, agricultural profits and BNC (CGI art. 155 IV, as worded on the impots.gouv.fr page).

The status is judged for the whole tax household and covers all its furnished lets together. If either condition fails, the activity is LMNP.

### Consequences of LMP status

**LMP vs LMNP**

| Feature | LMP | LMNP | Source |
| --- | --- | --- | --- |
| Deficits | Eligible réel loss against global income "sans limitation de montant" (BOFiP § 350); micro uses its fixed allowance and creates no actual-expense deficit | Only against furnished letting profits of the next ten years (Section 4.2) | BOFiP BOI-BIC-CHAMP-40-20 |
| Gain on sale | Business gains regime (short and long term, art. 39 duodecies); the art. 151 septies exemption is open only after at least five years of activity (BOFiP § 410) | Private property gains regime (BOFiP § 290) | BOFiP BOI-BIC-CHAMP-40-20 |
| Social charges | Social contributions under the applicable affiliation regime; see `fr-social-contributions` | Social levies (Section 4.3), unless already charged by the social security bodies | Official F34102 professional-landlord contribution route; impots.gouv.fr "Location meublée" for the LMNP no-double-charge rule. The old two-column brochure quotation belongs to adjacent income and is not LMP evidence |
| 2042-C-PRO boxes, réel | 5KC, 5LC or 5MC | 5NA, 5OA or 5PA | impots.gouv.fr "Location meublée" |

- **Involuntary switch.** Because the second condition compares rents with the household's other income, a fall in that income (job loss, retirement) can make the activity professional with unchanged rents. Check both conditions every year.
- **Wealth tax (IFI).** The legacy text said LMP property may be exempt from IFI as a professional asset. No allowed page read for this skill states it; refer.

## Section 6: SCI à l'IR (property company at income tax)

- **Default regime.** An SCI that is not liable to corporation tax is taxed under CGI art. 8: each partner is taxed on their share of the company's result in the revenus fonciers category (BOFiP micro-foncier page, § 50: "sociétés dont les résultats sont imposés dans les conditions prévues à l’ article 8 du CGI").
- **The company's return.** The SCI files form 2072-S or 2072-C online from the professional space on impots.gouv.fr (2026 Brochure pratique, chapter on form 2044: "doit obligatoirement être télédéclarée").
- **The partner's return.** A partner who also lets property directly reports the share on form 2044 (or 2044 spéciale where a special regime applies). A partner with only SCI parts cannot use micro-foncier and reports the share on form 2042 (Section 3.1).
- **Depreciation.** The art. 39 C method in Section 4.2 belongs to BIC and cannot be applied to ordinary revenus fonciers. The separately referred 2026 bare-let depreciation scheme in Section 3.3 is an express exception to the old blanket no-depreciation statement; its eligibility and computation are not supplied here.
- **Sale of the property or of the parts.** Private property gains regime, with the holding period exemptions in Section 4.2 (F10864). Refer the computation.
- **Furnished letting through an SCI** raises the question whether the company becomes liable to corporation tax. This skill does not settle it: refer.

### SCI at IS (out of scope)

An SCI liable to corporation tax is taxed as a company. See `fr-business-accounting` for company tax and refer.

## Section 7: Forms summary

**Forms summary**

| Regime | Form |
| --- | --- |
| Micro-foncier | 2042, box 4BE (gross rents) |
| Réel foncier | 2044 or 2044 spéciale, result to 2042 boxes 4BA and following |
| Micro-BIC LMNP | 2042-C-PRO, boxes 5NG/5OG/5PG, 5NH/5OH/5PH, 5NI/5OI/5PI |
| Réel LMNP | 2031 and applicable schedules (2033 under the simplified real regime) to the SIE; result to 2042-C-PRO boxes 5NA/5OA/5PA, deficit to 5NY/5OY/5PY, earlier deficits 5GA to 5GJ |
| Réel LMP | 2031 and schedules; result to 2042-C-PRO boxes 5KC/5LC/5MC |
| Ordinary long-term micro-BIC LMP, eligible/no réel election | 2025 income declared in 2026: 2042-C-PRO gross receipts 5KP/5LP/5MP; 50% allowance/minimum EUR 305 applied automatically. The legal method above is distinct from unconfirmed 2027 form layout |
| SCI at IR | 2072-S or 2072-C (company), and 2044 or 2042 (partner) |

## Section 8: Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Furnished or bare unclear | Ask; test against the furniture list in décret n°2015-981. Do not default to BIC and claim depreciation |
| Regime unknown | Apply the micro regime only if receipts are within the limit for the right year and the household has no excluded property; otherwise réel |
| LMP or LMNP unclear | Test both conditions on the household's figures; until shown, treat as LMNP for deficits (no global income set-off) |
| Déficit foncier set-off unclear | Do not set against global income |
| Tourist let classification unclear | Treat as unclassified until the classification certificate is seen |
| Which social levy rate | Bare rental: Section 3.4. Furnished, non-professional: Section 4.3 |

## Section 9: Key legal references

**Key legal references**

| Rule | Article |
| --- | --- |
| Revenus fonciers | CGI art. 14 and following |
| Micro-foncier and its exclusions | CGI art. 32 (BOI-RFPI-DECLA-10) |
| Déficit foncier | CGI art. 156 I 3° (BOI-RFPI-BASE-30-20) |
| Micro-BIC limits and allowances | CGI art. 50-0 |
| LMP definition | CGI art. 155 IV |
| LMNP deficits | CGI art. 156 I 1° ter (BOI-BIC-CHAMP-40-20) |
| Depreciation limit for furnished lets | CGI art. 39 C |
| SCI transparency | CGI art. 8 |
| Social levies on wealth income | CSS art. L136-6 and L136-8 |

These references are as named on the linked BOFiP and impots.gouv.fr pages. On 29 October 2026, selected current CGI art. 150 VB III and its effect note, and CGI art. 39 C I/II-2/II-3, were also read from the official Légifrance web extract; this is not a claim that every cited code article was read in full.

## The method, step by step

1. **Sort each let.** For each property, decide furnished or bare (impots.gouv.fr "Location meublée", https://www.impots.gouv.fr/particulier/location-meublee), and whether it is a classified tourist let, an unclassified tourist let, a chambre d'hôtes, or another furnished let. Bare lets go to steps 2 to 4; furnished lets to steps 5 to 7.
2. **Bare lets: micro-foncier or réel.** Reconcile the household's statutory gross input in Section 3.1, including ancillary receipts, contractual landlord expenses, qualifying grants/indemnities and eligible proportional gross SCI/FPI shares and check the exclusions (BOFiP BOI-RFPI-DECLA-10, https://bofip.impots.gouv.fr/bofip/3973-PGP.html). Within the limit and no exclusion: micro-foncier, box 4BE of form 2042, unless the client prefers the réel (three-year option).
3. **Bare lets, réel: form 2044.** Compute receipts, deductible charges and loan interest on form 2044 or 2044 spéciale (2026 Brochure pratique, chapter on form 2044, https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/19-decla_rev_fonciers_341a364.pdf). Leave out construction, reconstruction and extension works.
4. **Bare lets: deficit.** Split any deficit between the loan interest part and the rest. Set the rest against global income up to the limit in Section 3.3, or the raised limit where the energy renovation conditions are proved (nouveautés, https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/nouveautes.pdf). Carry the remainder forward ten years against rental income. Record the date until which the property must stay let. Track origin-year expiry and use oldest eligible losses first against current positive net rental income, including surviving réel losses after the micro allowance; no-prior-loss examples do not establish a bar on old losses.
5. **Furnished lets: LMP or LMNP.** Test the two LMP conditions for the whole household (Section 5, impots.gouv.fr "Location meublée").
6. **LMNP or LMP: micro-BIC or réel.** Check receipts of the previous two years against the limit for the right type and year (Section 4.1; F23267, https://entreprendre.service-public.gouv.fr/vosdroits/F23267). Micro: use the allowance/minimum for the actual letting category and the dated LMNP/LMP filing route in Section 4.1; do not also deduct actual charges/depreciation or invent 2027 form boxes. Réel: prepare form 2031 and the applicable schedules (2033 under the simplified real regime), apply the art. 39 C limit to depreciation, and carry the result to 2042-C-PRO (BOFiP BOI-BIC-CHAMP-40-20, https://bofip.impots.gouv.fr/bofip/3610-PGP.html).
7. **CFE and VAT.** A furnished landlord, professional or not, is liable to the CFE (cotisation foncière des entreprises) and must obtain a SIRET number (impots.gouv.fr "Location meublée"). See `fr-cfe` for the receipts threshold and the conditional home-letting exemptions. F23547's general summary broadly excludes a let inside the owner's main home, but its detailed list requires the actual branch: occasional reasonable-price letting of part of the personal home, or furnished letting as the subtenant's main home; classified tourism/chambres d'hôtes in the personal home have the stated commune-decision and tenant-home conditions. Location inside the main home alone does not establish the exemption (F23547, https://entreprendre.service-public.gouv.fr/vosdroits/F23547). See `france-vat-return` if VAT applies.
8. **Social levies.** Apply the right rate: Section 3.4 for bare rental income, Section 4.3 for LMNP income (F2329, https://www.service-public.gouv.fr/particuliers/vosdroits/F2329). For LMP, go to `fr-social-contributions`.
9. **Assemble the return.** Carry every result to form 2042 and 2042-C-PRO and run the household computation with `fr-personal-income-tax`.

**CFE threshold for furnished letting (entreprendre.service-public.gouv.fr F23547)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 |
| Furnished letting is within the CFE once turnover or gross receipts excluding VAT exceed | EUR 5,000 | "recettes brutes hors taxes doivent être supérieurs à 5 000 €"; general summary excludes a let inside the main home, but apply the conditional detailed home-letting branches in step 7 rather than infer exemption from that location alone |

## Worked examples

**Example 1. Ordinary micro-foncier.** A resident household has EUR 12,000 of gross bare rents in 2026, excluding tenant charges, no excluded property and no réel election. The EUR 15,000 limit is met. The 30% allowance is EUR 3,600, leaving EUR 8,400 taxable rental income. Social levies at 17.2% are EUR 1,444.80; income tax still requires the household computation.

**Prior-loss assumption for Example 1.** Its EUR 8,400 and EUR 1,444.80 computation assumes no eligible prior rental loss to deduct. If a documented unexpired EUR 2,000 earlier réel loss is available instead, apply the Section 3.3 vintage ledger after the allowance: net rental income EUR 6,400. The original no-prior-loss inputs and executable check below remain unchanged.

```oa-check
name: FR bare rental micro-foncier ordinary 2026
inputs:
  gross_rents: 12000
steps:
  - allowance: gross_rents * 0.30
  - taxable_rent: gross_rents - allowance
  - social_levies: taxable_rent * 0.172
expected:
  allowance: 3600.00
  taxable_rent: 8400.00
  social_levies: 1444.80
```

**Example 2. Real LMNP depreciation limit.** A non-professional furnished landlord has EUR 20,000 rent accrued, EUR 8,000 other deductible property charges and EUR 15,000 otherwise eligible current depreciation. Art. 39 C limits this year’s depreciation deduction to EUR 12,000. The taxable result is zero, not a EUR 3,000 depreciation-created deficit. EUR 3,000 is not deducted this year. If regularly booked and blocked only by art. 39 C, it joins the deferred-depreciation record and can be deducted later subject to the same limit; cessation and sale treatment remain separately referred. The fictional depreciation input is not an official useful life or rate.

```oa-check
name: FR real LMNP current depreciation ceiling
inputs:
  rent: 20000
  other_charges: 8000
  current_depreciation: 15000
steps:
  - depreciation_capacity: max(0, rent - other_charges)
  - deducted_depreciation: min(current_depreciation, depreciation_capacity)
  - taxable_profit: rent - other_charges - deducted_depreciation
  - not_deducted_currently: current_depreciation - deducted_depreciation
expected:
  depreciation_capacity: 12000.00
  deducted_depreciation: 12000.00
  taxable_profit: 0.00
  not_deducted_currently: 3000.00
```

## Ask the client first

- Is each property let furnished or bare, and for a tourist let, is it classified (ask for the classification decision)? The answer changes the income category, the micro limit and the allowance.
- What were the gross rents or receipts for each type of let in 2025 and in 2024 (and in 2026 so far)? The micro tests look at those years.
- Does anyone in the tax household own a historic monument, a property under an art. 31 deduction (Périssol, Besson, Robien, Borloo, Cosse) or Loc'Avantages, or SCI or SCPI parts? Any of these can shut micro-foncier.
- What are the household's salaries, pensions, other BIC, BNC and agricultural income? This decides LMP or LMNP.
- Is there a rental deficit from earlier years, or energy renovation works with a before-and-after energy certificate, and has a property that produced a deficit been sold or stopped being let within three years?
- Is any let already registered as a micro-enterprise with Urssaf, or already bearing social contributions through a social security body?

## When to refuse or refer

- SCI or any company liable to corporation tax (SCI à l'IS): refer.
- The capital gain on selling a let property, including the add-back of LMNP depreciation and the holding period allowances: refer the computation.
- The 2026 bare-let depreciation scheme (CGI art. 31, loi de finances 2026 art. 47), Pinel, Denormandie, Malraux, Loc'Avantages or historic monuments: refer, as this skill gives only their effect on micro-foncier.
- LMP social contributions, the IFI treatment of LMP property, and the art. 151 septies exemption calculation: refer.
- Furnished letting inside an SCI, and the question whether it makes the company liable to corporation tax: refer.
- Non-residents letting French property: the tax rate and social levy rules differ; refer.
- Para-hotel activity (furnished letting with hotel-type services), which may fall under VAT and different gain thresholds (BOFiP BOI-BIC-CHAMP-40-20 § 430): refer.
- Any year other than income of 2025 declared in 2026, or income of 2026: check the year's figures first.

## Sources

- Selected source checks, 29 October 2026: current CGI art. 150 VB III (cost reduction, specified exceptions and effect note): https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053544785 . Original agency shorthand is retained above as countertext. Other selected administrative clauses are recorded in the figure ledger. Selected current art. 39 C: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000029355753 ; simplified-real2033 scope: https://www.impots.gouv.fr/formulaire/2033-sd/liasse-bicsi-regime-rsi-tableaux-ndeg-2033-sd-2033-g-sd . Selected cited scope read 2026-10-29.

- BOFiP, revenus fonciers, régime micro-foncier (BOI-RFPI-DECLA-10): https://bofip.impots.gouv.fr/bofip/3973-PGP.html Selected cited scope read 2026-10-29.
- BOFiP, location meublée, régime fiscal (BOI-BIC-CHAMP-40-20): https://bofip.impots.gouv.fr/bofip/3610-PGP.html Selected cited scope read 2026-10-29.
- impots.gouv.fr, Location meublée (modified 23/04/2026): https://www.impots.gouv.fr/particulier/location-meublee Selected cited scope read 2026-10-29.
- Brochure pratique 2026, revenus fonciers: https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/10-rev_fonciers_157a160.pdf Selected cited scope read 2026-10-29.
- Brochure pratique 2026, déclaration des revenus fonciers no 2044: https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/19-decla_rev_fonciers_341a364.pdf Selected cited scope read 2026-10-29.
- Brochure pratique 2026, revenus et plus-values des professions non salariées: https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/11-revenus_non_salaries_161a182.pdf Selected cited scope read 2026-10-29.
- Brochure pratique 2026, principales nouveautés: https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/nouveautes.pdf Selected cited scope read 2026-10-29.
- Régime fiscal de la micro-entreprise (F23267): https://entreprendre.service-public.gouv.fr/vosdroits/F23267 Selected cited scope read 2026-10-29.
- Prélèvements sociaux sur les revenus du patrimoine et de placements (F2329): https://www.service-public.gouv.fr/particuliers/vosdroits/F2329 Selected cited scope read 2026-10-29.
- Plus-value immobilière (F10864): https://www.service-public.gouv.fr/particuliers/vosdroits/F10864 Selected cited scope read 2026-10-29.
- Cotisation foncière des entreprises (F23547): https://entreprendre.service-public.gouv.fr/vosdroits/F23547 Selected cited scope read 2026-10-29.
- Selected repair reads, 31 October 2026: actual gross-receipt and eligible gross-share inclusions, prior-loss micro/vintage rules, EUR 20 management-unit definition, full copropriété reconciliation, professional micro and narrow first-letting exception were read in the retained official clauses. The 2026 brochure is a 2025-income filing source, not a 2027 layout guarantee. The deficit page's two-column native extraction is kept distinct from its actually inspected printed page 363; source identity alone is not a reading claim.

## Disclaimer

This skill is for informational purposes only and does not constitute tax advice. All positions must be reviewed and signed off by a qualified expert-comptable or avocat fiscaliste before filing. The most up-to-date version of this skill is maintained at openaccountants.com.

*OpenAccountants: open-source accounting skills for AI. This output must be reviewed by a qualified professional before filing or acting upon. Report errors: github.com/openaccountants/openaccountants*

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
