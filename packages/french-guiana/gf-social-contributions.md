---
name: gf-social-contributions
description: >
  French Guiana compulsory social contributions for calendar year 2026.
  Covers ordinary private employees and employers, social ceilings, CSG and
  CRDS, mandatory complementary pensions, national employer relief and the
  three LODEOM schedules with their Guyane eligibility conditions. Also
  covers ordinary artisan, trader and non-regulated liberal self-employed
  contributions, the reformed common social base, DOM startup exemption and
  later abatements, micro-social rates and payment and correction workflows.
  Trigger on Guyane cotisations sociales, CGSS, Urssaf, LODEOM, salaire brut net,
  plafond sécurité sociale, micro-entrepreneur outre-mer and indépendant DOM.
  Wage income tax withholding and DSN payroll fields belong to gf-payroll;
  investment income social levies and personal income tax belong to gf-income-tax.
  Profession-specific pension funds and agricultural insurance need their own schedules.
jurisdiction: GF
category: international
tax_year: 2026
tax_year_notes: "Calendar-year contribution periods; 2025 actual-income regularisation in 2026 uses its own 2025 ceiling"
tier: 2
type: situation-rules
last_updated: 2026-11-11
version: 0.1
---

# French Guiana compulsory social contributions 2026 v0.1

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.


## Who this applies to

French Guiana is a French overseas department covered by the French social system, with collection through the CGSS. Apply the appropriate national affiliation and DOM-specific relief; do not treat the territory as a foreign country, or apply Mayotte's different ceiling or rates. This Guide owns social contribution figures. [gf-payroll](gf-payroll.md) owns salary income tax withholding and the employer's DSN/PAS process. [gf-income-tax](gf-income-tax.md) owns annual income tax and investment-income social levies.

**Required inputs:** affiliation/status and profession; contribution period and work locations; all cash and noncash remuneration, hours and absences; establishment headcount/activity/turnover; actual notified accident and pension rates; relief eligibility and prior claims. For a self-employed person also obtain start date, legal/tax status, actual social income or turnover, and the latest assessment. An SAS president or minority/equal SARL manager generally falls under assimilated employment social security; a majority SARL manager is generally self-employed. A corporate mandate does not create unemployment cover as if it were a genuine employment contract. Confirm status before choosing a table (CSS L311-3/L611-1; official employer contribution guidance).

| Case | Treatment / boundary |
|---|---|
| Ordinary private employee affiliated in France | Employee and employer contributions below, with mandatory Agirc-Arrco. LODEOM never exempts the employee's share. |
| Eligible Guyane employer | Test LODEOM category and compliance before calculating it; compare lawful alternatives, do not stack LODEOM and RGDU. |
| Artisan, trader, non-regulated liberal in the ordinary self-employed regime | Actual-income rates and DOM exemption/abatements below. These are not turnover percentages. |
| Micro-social entrepreneur | Turnover method and DOM-stage percentages below; employee payroll is still a separate duty if staff are hired. |
| Regulated profession, agricultural business, artist-author, mariner or public scheme | Identify its actual statutory fund and schedule; do not apply the artisan retirement table. These profession-specific computations are outside the table. |
| Worker with valid foreign social-security coverage | Establish applicable legislation and certificate before applying French contributions; tax residence alone does not decide affiliation. |

## Rates, bands and thresholds

Unless a row states otherwise, rates apply to the 2026 contribution period and ordinary private-sector salary, before relief. Salary may need annual cumulative adjustment; the full-month ceiling is not automatically available for every partial month or part-time contract.

| Employee/employer parameter | Employee | Employer / base and conditions | Official source |
|---|---|---|---|
| Social security ceiling | EUR 4,005 monthly; EUR 48,060 annual | Ordinary French ceiling, not Mayotte ceiling | 2026 Agirc-Arrco circular p. 2, https://www.agirc-arrco.fr/storage/CirculaireAgircArrco2025-16sg-drj.pdf; CSS D242-17 et seq. |
| Basic old-age, capped | 6.90% | 8.55%; salary up to adjusted ceiling | Urssaf 2026 private-sector rate table, https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html |
| Basic old-age, uncapped | 0.40% | 2.11%; whole salary | same: https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html |
| CSG | 9.20%, of which 6.80% deductible and 2.40% non-deductible for income tax | Employee only; ordinary earned salary base 98.25% up to four annual ceilings, full salary above; add relevant employer-funded protection amounts without that salary allowance | Urssaf employee table, https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; https://entreprendre.service-public.gouv.fr/vosdroits/F2302 |
| CRDS | 0.50%, non-deductible | Same ordinary earned-income base as above; employee only | same: https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html |
| Health/maternity/disability/death | No ordinary employee contribution | 13% full; retained LODEOM reduction gives 7% where annual salary does not exceed 2.5 times the SMIC at 31 December 2023 | Urssaf 2026 transition, https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html; law 2025-1403 art.40 V |
| Family allowances | None | 5.25% full; retained LODEOM reduction gives 3.45% where annual salary does not exceed 3.5 times the SMIC at 31 December 2023 | same: https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html; law 2025-1403 art.40 VI |
| Solidarity autonomy | None | 0.30% whole salary | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html |
| FNAL | None | Under 50 employees: 0.10% up to adjusted ceiling; at least 50: 0.50% whole salary, subject to statutory headcount crossing rules | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html |
| Unemployment | No ordinary employee contribution | 4.00% up to four ceilings; use notified bonus-malus rate where employer falls under that mechanism | Urssaf 2026 table, https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html |
| AGS wage guarantee | None | 0.25% up to four ceilings; temporary-work special rate 0.03% | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html |
| Social dialogue | None | 0.016% whole salary | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html |
| Agirc-Arrco pension, tranche 1 | 3.15% | 4.72%; up to one adjusted ceiling, usual split | ANI arts.34-36; 2026 circular p. 2, https://www.agirc-arrco.fr/storage/CirculaireAgircArrco2025-16sg-drj.pdf |
| Agirc-Arrco pension, tranche 2 | 8.64% | 12.95%; fraction over one to eight ceilings, usual split | same: https://www.agirc-arrco.fr/storage/CirculaireAgircArrco2025-16sg-drj.pdf |
| CEG tranche 1 / tranche 2 | 0.86% / 1.08% | 1.29% / 1.62%, same respective tranches | ANI art.37; https://www.agirc-arrco.fr/storage/CirculaireAgircArrco2025-16sg-drj.pdf |
| CET where salary exceeds tranche 1 | 0.14% | 0.21% on both tranches1+2, not only the excess | ANI art.37; https://www.agirc-arrco.fr/storage/CirculaireAgircArrco2025-16sg-drj.pdf |
| Apec, cadres only | 0.024% | 0.036%, up to four ceilings | 2026 circular p. 3; 2024 Apec protocol, https://www.agirc-arrco.fr/storage/CirculaireAgircArrco2025-16sg-drj.pdf |
| Work accident and occupational disease | None | Actual notified establishment rate; no universal Guyane percentage | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html |
| Compulsory complementary health | Contract/collective agreement | Employer finances at least half of compulsory collective health cost; collective agreement may require more | https://www.service-public.gouv.fr/particuliers/vosdroits/F20739 |
| Vocational training, ordinary employer | None | 0.55% if fewer than 11; 1% from 11, subject to applicable scope and crossing rules | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html |
| CPF-CDD | None | 1% on covered fixed-term pay, subject to statutory exempt contract categories | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html |
| Apprenticeship tax, taxable employer | None | Main part 0.59% and balance0.09%; exemptions and allocation rules must be tested | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html |
| Mobility | None | At least11 employees in an applicable transport area; use the actual municipality's Urssaf lookup, not a national flat rate | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html |

Do not charge every row to every employer: unemployment coverage, training/apprenticeship liability, exempt contracts and local transport scope differ. Use the employer's pension affiliation agreement where a valid historical rate or more favourable allocation supersedes the ordinary Agirc-Arrco split. Supplementary health and provident premiums require the actual contract; their CSG and tax treatment can differ from salary.

### Employer relief parameters

| Relief | 2026 rule and conditions | Official source |
|---|---|---|
| LODEOM ordinary competitiveness | Full covered employer contributions below 1.3 SMIC; taper from 1.3 to below 2.2; zero at 2.2 | CSS L752-3-2 III A, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053280451; CSS D752-7 II1, https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006126865/2026-07-01 |
| LODEOM strengthened competitiveness | Full below 2 SMIC; taper from 2 to below 2.7; zero at 2.7; qualifying employer below 250 employees AND annual turnover below EUR50 million | CSS L752-3-2 III B, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053280451; D752-7 II2, https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006126865/2026-07-01 |
| LODEOM innovation/growth | Full below 1.7 SMIC; covered pay capped at 1.7 SMIC for pay from 1.7 to below 2.5; taper from 2.5 to below 3.5; zero at 3.5; below 250 employees AND turnover below EUR50 million, qualifying employee/project | CSS L752-3-2 III C, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053280451; D752-7 II3, https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006126865/2026-07-01 |
| LODEOM maximum T | 0.3201 with FNAL 0.10%; 0.3241 with FNAL 0.50%; actual sum may be lower | Urssaf 2026 Guyane coefficient detail, https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/exonerations-zonees/exoneration-lodeom.html |
| RGDU alternative | Pay below 3 current SMIC; Tmin 0.0200; Tdelta 0.3781 with FNAL 0.10%, or0.3821 with FNAL 0.50%; exponent1.75; maximum 0.3981/0.4021 | Urssaf 2026 transition, https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html; decrees2025-887 and 2025-1446 |

The current annual SMIC used for relief changes with the 2026 wage-floor revaluation: use the actual hours/period and both wage-floor periods in [gf-payroll](gf-payroll.md), not the December2023 frozen SMIC used only for retained health/family rate thresholds. LODEOM figures above apply to Guyane; the July2026 extension to Mayotte does not transfer Mayotte's rates to Guyane.

### Ordinary self-employed artisan, trader and non-regulated liberal

These are rates before applicable DOM relief, applied to the reformed social base. `P` below means the annual social ceiling for the contribution year owned by the first table, not the year the assessment is paid.

| Component | 2026 rate/base/condition | Official source |
|---|---|---|
| Common social base deduction | 26% of qualifying gross social income; deduction floor1.76% P, cap130% P; no duplicate deduction of personal social charges | CSS L136-3/L131-6, Urssaf reform, https://www.urssaf.fr/accueil/independant/comprendre-payer-cotisations/reforme-cotisations-independants.html; CSS D136-5, decree2024-688 art.1, https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000049888566 |
| Health/maternity1 in DOM | 8.50% up to 3 P, 6.50% on excess; separate low-income exemption where income below 13% P | Urssaf Outre-mer table, https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-ac-plnr.html; CSS D756-6, https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006126865/2026-07-01 |
| Daily sickness benefit2 | 0.50%, base floor40% P, cap5 P, unless DOM exemption applies | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-ac-plnr.html; decree2024-688 art.2, https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000049888566 |
| Basic pension | 17.87% up toP and 0.72% on excess; separate DOM low-income exemption if relevant activity income no more than EUR390 | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-ac-plnr.html; CSS D756-6, https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006126865/2026-07-01 |
| Complementary pension | 8.10% up toP, 9.10% on excess up to 4 P; no ordinary DOM startup exemption; separate DOM exemption applies to both basic and complementary retirement when relevant activity income is no more than EUR390 | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-ac-plnr.html; decree2024-688 art.3, https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000049888566; low-income exemption CSS D756-6, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000041968318 |
| Invalidity/death | 1.30% up toP; base floor11.5% P, subject to applicable exemptions | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-ac-plnr.html |
| Family allowances in DOM | 3.10% on relevant base before DOM exemption/abatement | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-ac-plnr.html |
| CSG/CRDS on ordinary professional income | 9.70% on relevant common base before DOM exemption/abatement; no employee salary98.25% allowance | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-ac-plnr.html; https://www.urssaf.fr/accueil/independant/comprendre-payer-cotisations/reforme-cotisations-independants.html |
| Annual CFP | 0.25% P trader or non-regulated liberal;0.29% P artisan;0.34% P trader/non-regulated liberal with collaborating spouse | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-ac-plnr.html, Outre-mer CFP panels |
| Minimum ordinary bases, absent exemption | Basic pension:450 hourly SMIC at 1 January (EUR5,409); sickness2:40% P; invalidity:11.5% P. RSA/prime-activité recipients can use actual income unless opting otherwise | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-ac-plnr.html, Outre-mer minimum panel |
| First24 months | Covered contributions exempt up to 110% P income; fixed exemption at 110% P for income110%-150% P; linearly tapers150%-250% P, zero at 250% P | CSS L756-2; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037063476; D756-4, https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006126865/2026-07-01 |
| After startup | Third calendar year:75% abatement on income up toP; fourth onward:50%; full rate of abatement below 150% P total income, taper to zero at 250% P. Complementary pension, invalidity/death and CFP excluded | CSS L756-4; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037063454; D756-4, https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006126865/2026-07-01 |

### Micro-social, DOM-stage rates

For qualifying activities started from 1 January2020, apply the following to collected turnover/receipts, not profit. Stage 1 runs through the end of the seventh calendar quarter following the affiliation quarter; stage 2 then runs to the end of the third calendar year; stage 3 begins in the fourth calendar year. Any elapsed stage can be short or absent depending on the start date; do not replace this with a simple24 month rule. Fractions of national rates are rounded **up to the next tenth of a percent** (CSS D756-5).

| Ordinary activity | Stage 1 | Stage 2 | Stage 3 | Official source |
|---|---|---|---|---|
| BIC goods sale | 2.1% | 6.2% | 8.2% | CNAV 2026-12 §2.3 pp. 6-8, https://legislation.lassuranceretraite.fr/Documents/Circulaires/Pdf/circulaire_cnav_2026_12_07042026.pdf; CSS D756-5, https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006126865/2026-07-01 |
| BIC services | 3.6% | 10.6% | 14.2% | same: https://legislation.lassuranceretraite.fr/Documents/Circulaires/Pdf/circulaire_cnav_2026_12_07042026.pdf |
| Non-regulated BNC under Assurance retraite | 4.3% | 12.8% | 17.1% | CNAV 2026-12 §2.3 pp. 7-8, https://legislation.lassuranceretraite.fr/Documents/Circulaires/Pdf/circulaire_cnav_2026_12_07042026.pdf |
| Cipav micro-social liberal activity | One third of national23.2%, rounded up =7.8% | One half, rounded up =11.6% | Two thirds, rounded up =15.5% | CSS D756-5, https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006126865/2026-07-01; 2026 national rate CSS D613-4 https://www.legifrance.gouv.fr/codes/id/LEGIARTI000049625445 |

CFP is additional to micro-social percentages; income-tax versement libératoire is also separate, never silently included. Mixed activities allocate turnover by actual category. Zero turnover still requires a declaration. The micro-fiscal eligibility limits and income-tax abatement are owned by [gf-income-tax](gf-income-tax.md). The non-micro startup exemption and abatement are not applied again on top of these reduced micro-social rates. Pre2020 entrants and tourist accommodation require their own category history, outside this ordinary activity table.

## The base

### Employee and employer computation

1. Start with all employment remuneration, including bonuses, benefits in kind and taxable salary maintenance. Exclude a genuine documented professional reimbursement only when its statutory conditions are met; relabelling salary as expenses does not exclude it. Apply the legal/conventional minimum, then actual social exemptions and each component's base. Do not equate the social base with the PAS base.
2. Establish the period's adjusted social ceiling for part-time, entry/exit, unpaid absence and concurrent employments; regularise capped amounts cumulatively. Split pension tranche 1 and tranche 2. Once the CET threshold is crossed it applies to the covered whole pay, with annual regularisation where necessary.
3. For ordinary CSG/CRDS, apply the salary deduction only to qualifying earned pay up to four annual ceilings. Add employer health/provident amounts that belong in its base at their proper full amount; do not apply the salary allowance to all employer contributions. A tax non-resident not satisfying French CSG affiliation conditions requires the non-resident health branch, not automatic ordinary CSG.
4. Withhold employee contributions, compute employer contributions, then apply the chosen employer relief only to its covered employer liabilities. LODEOM does not remove AGS, employee contributions, all accident premiums, training, apprenticeship or contractual health costs. Preserve the distinction between payroll cash net, taxable net and net social.

Sources: Urssaf rates and [official contribution-base guidance](https://entreprendre.service-public.gouv.fr/vosdroits/F24013); Agirc-Arrco 2026 circular; CSS L242-1 and D242-17 et seq.

### Select and compute LODEOM

First substantiate a qualifying Guyane establishment, actual employee assignment, headcount/activity and compliance. The establishment can qualify even where the registered head office is in mainland France. Public employers/EPIC and private household employers are excluded. The authority also excludes corporate officers combining a mandate and employment contract from this relief. Keep declarations and payments current, or honour a debt plan and current payments; disqualifying tax/labour offences require examination. Count employees across the business's establishments in the same territory. Mixed activities test the employee's activity; a generic business code alone does not prove every employee qualifies (CSS L752-3-2 II/V/VI).

**Ordinary category:** fewer than 11 employees in any sector, or the sectors/routes in L752-3-2 II2-4 as III A specifies. The Guyane II5 route alone does not independently confer ordinary III A relief if its strengthened conditions fail. These include construction/public works, industry, catering, press/audiovisual, environment, agronutrition, renewable energy, ICT/call centres, fishing/aquaculture/agriculture, tourism/associated leisure/nautical/hotels, R&D and inward processing. Air and sea/river transport have the specific routes and exclusively assigned staff conditions in II3-4. Reaching11 has a statutory continuation limited to the previously covered11 staff/replacements; do not apply an unconditional cliff to the entire existing workforce.

**Strengthened category:** both size and turnover conditions above, plus one of III B's alternative activity routes. III B1 admits II2 sectors except construction/public works; III B2 separately admits the Guyane II5 route for a principal activity eligible under CGI199undeciesB or accounting, business advice, engineering or technical studies; III B3 covers inward processing. The construction/public-works exclusion in B1 does not override the separate Guyane II5 route: eligible construction services are included under article199undeciesB as BOI-BIC-RICI-20-10-10-40 §170 confirms. Test actual activity and the applicable route; construction is not automatically excluded from strengthened Guyane relief. Sources: CSS L752-3-2 II5/III B; https://bofip.impots.gouv.fr/bofip/1434-PGP.html §170.

**Innovation:** the size/turnover conditions and an employee mainly implementing an innovative ICT project; administrative, finance, logistics and HR support are excluded. Qualifying project fields include telecoms, specified IT/programming/data/hosting, internet/software publishing, infographics and connected objects (D752-7 II3).

Let `R` be annual covered gross remuneration, `S` the legally adjusted annual current SMIC and `T` the actual sum of eligible employer rates, capped by the table. Annual relief is as follows, limited to the covered contributions actually due:

- Ordinary: below 1.3 S, covered contributions in full; from 1.3 S to below 2.2 S, coefficient `1.3*T/0.9*(2.2*S/R-1)` multiplied byR; at/above 2.2 S zero.
- Strengthened: below 2 S full; from 2 S to below 2.7 S, coefficient `2*T/0.7*(2.7*S/R-1)` multiplied byR; at/above 2.7 S zero.
- Innovation: below 1.7 S full; from 1.7 S to below 2.5 S relief on covered pay capped at 1.7 S; from 2.5 S to below 3.5 S, coefficient `1.7*T*(3.5*S/R-1)` multiplied byR; at/above 3.5 S zero.

**Source reconciliation:** the current Urssaf page describes innovation taper immediately after1.7 SMIC. Binding L752-3-2 III C expressly keeps the1.7-2.5 SMIC plateau; D752-7 II3 starts its taper at 2.5 SMIC. Apply the law. Do not calculate the taper across the plateau from the simplified webpage.

Compute by calendar year, employee and employment contract with progressive/year-end regularisation. Part-time and part-year `S` follows contractual hours and period; account for overtime and absences under the statutory SMIC method. Full exemption means full **covered** contributions, not every payroll cost. The T maximum includes only the mutualised accident slice, ordinary mandatory pension share and applicable FNAL. A lower actual employer pension allocation lowers T. Do not force an assumed T on an employee outside ordinary unemployment or pension coverage.

**RGDU alternative.** An eligible employer can choose RGDU instead of LODEOM; they do not cumulate. For pay below 3 S, ordinary RGDU coefficient is `Tmin + Tdelta * (0.5*(3*S/R-1))` raised to power1.75 on the bracketed factor **only**, meaning `Tmin + Tdelta * [0.5*(3*S/R-1)]^1.75`, capped atTmin+Tdelta and floored atzero. At/above 3 S no RGDU. The RGDU remuneration test includes PPV where legally required; ordinary health/family full rates apply rather than the separately retained LODEOM reductions. Compare total contributions after each lawful method, not just the relief percentage. Use the actual T parameters and scheme exceptions from the authority; special funds and premium arrangements can change the result (Urssaf 2026 transition, decrees cited in table).

### Ordinary self-employed computation

For actual-income cases, assemble the common base before applying DOM rules: qualifying receipts/products less business costs other than personal social charges and deductible CSG, with statutory tax-to-social adjustments. Deduct the common26% allowance within its floor/cap. For an IS company manager, remuneration/benefits and the statutory share of family dividends above 10% of the relevant capital/premiums/current-account reference enter the social base; do not assume all dividends are investment income. Micro-fiscal persons outside micro-social use their statutory fiscal abatement rather than an extra26% reduction (Urssaf reform; CSS L136-3/L131-6).

The 2026 assessment process regularises **2025** actual income with2025 parameters, then adjusts2026 provisional instalments. This table's2026 ceiling must not be used to recompute2025 liabilities merely because the notice is received in 2026. Reconcile the notice's separate years, component bases and DOM exemptions.

For the first 24 months, test each calendar year's income annualised as L756-2 requires. Apply the exemption to health1/2, basic retirement, invalidity/death, family and CSG/CRDS; complementary pension and CFP remain due. Below110% P it covers the eligible contributions; between 110%-150% P it is capped at the amount for 110% P; between 150%-250% P it falls linearly. For the taper use D756-4: `exemption = E/P*(2.5*P-R)`, whereE is the eligible exemption at income150% P, never a flat reduction of total turnover. No exemption at/above 250% P.

After the initial period, third-calendar-year abatement is75%, fourth onward50%, on the income slice up toP; the amount tapers between total income150%-250% P. RCI, invalidity/death and CFP receive no such abatement. Adjust the third-year relief for the fraction already covered by the24 month exemption; do not grant both on the same period. Apply each component's floor/ceiling and the separate low-income exclusions. The generic13% P health exemption and the separate EUR390 exemption for both basic and complementary pension do not waive all contributions. A deficit does not automatically eliminate minimum insurance or CFP (L756-4/5 and D756-4/6; Urssaf Outre-mer minima).

Regulated professionals use the common social base and applicable DOM statute but their own CNAVPL/Cipav/other professional basic and complementary retirement and disability rules. The artisan rate table does not purport to compute those profession-specific funds.

## Deadlines and filing

**Employers.** Register the hire and establishment, report and pay through monthly DSN as [gf-payroll](gf-payroll.md) specifies. In DSN the LODEOM aggregate CTP codes for Guyane are462 ordinary,463 strengthened and 473 innovation; reversals/regularisations use684,538 and 685 respectively. Lost health/family reduction is regularised using CTP635/430 as applicable. Reconcile individual bases, aggregate relief and actual remittances to CGSS and the complementary pension body. Codes are not proof of eligibility. Keep the annual headcount, turnover, sector, employee/project allocation, R/S/T calculation and relief comparison evidence (Urssaf LODEOM declaration section).

**Ordinary independent.** Register the business via the official one-stop business formalities service, identify the correct social status and activate the Urssaf/CGSS account. Complete the social section of the annual online income declaration at impots.gouv.fr, including the professional figures and social adjustments; DGFiP transfers them for contribution recalculation. Check the Urssaf detailed notice and revised instalments, not only the income-tax result. Pay the scheduled monthly direct debit on the5th or20th, or elected quarterly on5 February/May/August/November; CFP is collected inNovember for ordinary artisans/traders/non-regulated liberals. Adjust estimated income through the account if appropriate; a reduced provisional payment is not a permanent remission. Sources: Urssaf reform and rate table; https://entreprendre.service-public.gouv.fr/vosdroits/F31233, payment section.

**Micro-social.** Declare cash turnover separately by activity monthly or elected quarterly at autoentrepreneur.urssaf.fr; declare nil turnover too. Ordinary monthly deadline is last day of following month; quarterly deadlines30 April,31 July,31 October and 31 January. The first return is no earlier than 90 days after start, with its grouped opening period confirmed in the account. Check displayed DOM stage/rate against affiliation date and category before validating; retain declaration, payment and account receipt. CFP and any tax election must be reconciled separately. Do not enter taxable profit after fiscal abatement into the turnover fields. Source: https://entreprendre.service-public.gouv.fr/vosdroits/F36232 and CSS D756-5.

## Penalties and interest

| Failure | Ordinary charge / conditions | Official source |
|---|---|---|
| Late social payment | Initial5% plus0.2% per month or fraction from due date on unpaid contributions; assessed after full payment for final calculation. For monthly ordinary independents apply the R613-2 III exception below | CSS R243-16; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006186436/; https://entreprendre.service-public.gouv.fr/vosdroits/F38145 |
| Qualifying first short delay | No late charges where declarations current, payment or honoured plan within 30 days, no payment delay in prior 24 months and charges below one monthly ceiling | CSS R243-11, https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006186436/ |
| Qualifying prompt correction | Covered error corrected and paid at next deadline, or other statutory small-error condition; excluded omitted employees/repeated understated pay | CSS R243-10, https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006186436/ |
| Late/missing employer DSN; omitted staff; understated pay | Distinct declaration penalties, separate from payment charges | CSS R243-12/13; amounts owned by [gf-payroll](gf-payroll.md), https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006186436/ |

For an ordinary independent paying monthly, a first missed monthly payment is recovered with the following payment. R613-2 III starts R243-16 late charges only at the second consecutive payment incident in the same calendar year; two consecutive missed payments move remaining annual collection to quarterly instalments. This exception does not replace the separately conditioned first-short-delay rule above. Source: CSS R613-2 III, https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006126967/2026-03-14 .

Understatement can produce unpaid principal, late charges and loss/recovery of an ineligible exemption; deliberate concealed work has additional recovery and sanctions. Do not apply the innocent-correction protection to deliberate concealment. For each missing micro turnover return, CSS R613-9 imposes 1.50% of the monthly ceiling rounded up to a whole euro: ceil(4,005 × 1.50%) = EUR 61. Do not use a portal's rounded EUR 60 shorthand. Where returns remain absent at the year's last due date, R613-10 permits the statutory provisional turnover base with a15% quarterly or5% monthly uplift; declaring after notification regularises actual contributions and replaces the R613-9 penalty with3% of contributions due. The provisional base references the applicable statutory thresholds, not the client's assumed profit.

For an ordinary independent who has not timely supplied the required electronic social-income data, R613-1-1 III provides a5% contribution penalty; failure to provide the requested complete data within two months in the R613-1-2 II case raises it to 10%. Under R613-1-2 I the provisional base is the higher of the prior-two-year average (or first year in year two) and 50% of the contribution year's annual ceiling, increased25% for each consecutive undeclared year; specified final-year and professional-fund exceptions apply. The assessment is corrected when actual income is supplied. These are distinct from ordinary late-payment charges. Source: CSS R613-1-1/1-2 and R613-9/10, https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006126967/2026-03-14 .

## Cross-border points

Applicable social legislation is distinct from tax residence, payroll PAS and treaty salary exemption. Within the territorial/personal scope of EU coordination use Regulations883/2004 and 987/2009 and the actual A1 posting/multi-state certificate; otherwise examine the applicable bilateral agreement and certificate with CLEISS. Do not assume a short stay or foreign payroll removes French affiliation. A move from metropolitan France to Guyane does not itself create foreign coverage. For a person not fiscally domiciled in France but covered by a French compulsory health scheme, CLEISS's2026 activity-income schedule gives employee health contribution5.5% instead of ordinary resident CSG/CRDS. Establish the precise coverage and certificate first; employer and pension contributions remain separately tested. Source: https://www.cleiss.fr/docs/regimes/regime_france0.html, financing section. This Guide's resident example does not apply that alternative. Route status questions to [gf-cross-border-tax](gf-cross-border-tax.md); [CLEISS applicable-law guidance](https://www.cleiss.fr/reglements/883_index.html) supplies the coordination text.

## Two worked examples that recompute

### Example 1: ordinary employee below the monthly ceiling

Assume a French-affiliated, French-tax-resident non-cadre employee, full month, EUR3,000 salary, no benefits, no health/provident premiums in this simplified component calculation, no extra historical pension rate and no other employee deductions. Basic pension is207+12; Agirc-Arrco 94.50; CEG25.80; CET is absent because the ceiling is not exceeded. CSG/CRDS salary base is3,000×98.25%=2,947.50. CSG is271.17 and CRDS14.74 after cent rounding. Covered employee deductions total625.21; net before PAS is2,374.79. Actual contractual health and other payroll items must be added before issuing a payslip; income-tax withholding is computed by gf-payroll, not by reducing gross pay with a guessed annual tax percentage.

```oa-check
name: Guyane ordinary employee contribution components 2026
inputs:
  gross: 3000
steps:
  - basic_capped: round(gross * 6.9 / 100, 2)
  - basic_uncapped: round(gross * 0.4 / 100, 2)
  - supplementary: round(gross * 3.15 / 100, 2)
  - ceg: round(gross * 0.86 / 100, 2)
  - csg_base: gross * 98.25 / 100
  - csg: round(csg_base * 9.2 / 100, 2)
  - crds: round(csg_base * 0.5 / 100, 2)
  - deductions: basic_capped + basic_uncapped + supplementary + ceg + csg + crds
  - net_before_pas: gross - deductions
expected:
  csg_base: 2947.50
  deductions: 625.21
  net_before_pas: 2374.79
```

### Example 2: the turnover boundary changes the LODEOM schedule

A compliant Guyane industrial company has20 employees. Compare annual turnover EUR49 million with exactly EUR50 million, keeping the same eligible industrial activity and employee facts. Assume correctly adjusted annual SMIC `S=22,000`, salary `R=44,000`, ordinary full T=0.3201, and sufficient covered employer contributions. The S amount is a stipulated part-period/hour-adjusted case input, not the published full-year 2026 SMIC. At EUR49 million the strict below-EUR50-million condition is met, so strengthened relief at 2 S has coefficient0.3201 and gives EUR14,084.40. At exactly EUR50 million that condition fails; the industrial employer remains eligible under ordinary II2/III A, giving coefficient0.04623666... and relief EUR2,034.41. Difference EUR12,049.99. Turnover eligibility determines the schedule; these relief amounts exclude employee and uncovered employer liabilities. A full RGDU comparison would also recompute the health/family rates and is not established by this schedule-only example. Source: CSS L752-3-2 II2, III A/B, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053280451 .

```oa-check
name: Guyane 2026 strengthened versus ordinary LODEOM eligibility
inputs:
  salary: 44000
  adjusted_smic: 22000
  t: 0.3201
steps:
  - ordinary_coefficient: 1.3 * t / 0.9 * (2.2 * adjusted_smic / salary - 1)
  - strengthened_coefficient: 2 * t / 0.7 * (2.7 * adjusted_smic / salary - 1)
  - ordinary_relief: round(salary * ordinary_coefficient, 2)
  - strengthened_relief: round(salary * strengthened_coefficient, 2)
  - difference: strengthened_relief - ordinary_relief
expected:
  ordinary_relief: 2034.41
  strengthened_relief: 14084.40
  difference: 12049.99
```

## Ask the client first

1. Employee, corporate officer, ordinary independent or micro-social; exact profession/fund and social affiliation certificate?
2. Contribution year, actual work/pay periods, hours/absence, full cash/benefit/protection amounts and prior cumulative bases?
3. Guyane establishment's activities by employee, territory-wide headcount, annual turnover and eligibility evidence, including innovative project duties?
4. Notified accident, unemployment bonus-malus, complementary pension/health/provident and mobility parameters; chosen relief and earlier regularisations?
5. Independent start date, actual social income and tax-to-social adjustments or cash turnover by category, prior DOM stage and CFP/spouse facts?
6. Accepted DSN/assessment, payment election, account statements, arrears/debt plan and any correction/control history?

## Sources

| Source and portion actually read | URL | Read on |
|---|---|---|
| Urssaf private-sector2026 rates, read employer and employee panels for every ordinary rate used | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html | 2026-11-11 |
| Agirc-Arrco 2026 circular, read pp. 2-3 tables, footnotes and Apec base; statutory source is ANI arts.32/34-37 | https://www.agirc-arrco.fr/storage/CirculaireAgircArrco2025-16sg-drj.pdf | 2026-11-11 |
| Urssaf 2026 transition, read for expanded RGDU formula, full parameters, PPV and retained LODEOM health/family rate tests | https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html | 2026-11-11 |
| BOI-BIC-RICI-20-10-10-40 §170, read for construction-service eligibility under article199undeciesB and the separate Guyane II5 route | https://bofip.impots.gouv.fr/bofip/1434-PGP.html | 2026-11-11 |
| CSS L752-3-2, read II-VI for Guyane sectors, strengthened eligibility, innovation plateau and non-cumulation | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053280451 | 2026-11-11 |
| CSS D752-7 and D756-4/5/6, read for all three employer formulas and independent DOM stages, taper and low-income exceptions | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006126865/2026-07-01 | 2026-11-11 |
| Urssaf LODEOM page updated28 July2026, read for common conditions, all Guyane schedules, T coefficient scope, CTP declaration and RGDU choice; statute resolves innovation summary conflict | https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/exonerations-zonees/exoneration-lodeom.html | 2026-11-11 |
| Urssaf artisan/trader/PLNR 2026, read all Outre-mer rate panels, minimum panel and startup/third/fourth-year panels in ordinary browser after direct fetch failed | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-ac-plnr.html | 2026-11-11 |
| CSS L756-2, read for annualised-income first 24 month exemption and taper | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037063476 | 2026-11-11 |
| CSS L756-4, read for abatement limits, excluded funds and third-year overlap | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037063454 | 2026-11-11 |
| Decree 2024-688 arts.1-3, read for common base deduction floor/cap, insurance rates and non-agricultural effective period | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000049888566 | 2026-11-11 |
| Urssaf reform page, read for common gross social base, deduction and 2025-income regularisation in 2026 | https://www.urssaf.fr/accueil/independant/comprendre-payer-cotisations/reforme-cotisations-independants.html | 2026-11-11 |
| CNAV 2026-12, read §2.3 pp. 6-8 including both BNC stages on p. 8; original PDF cached and p. 7 visually checked | https://legislation.lassuranceretraite.fr/Documents/Circulaires/Pdf/circulaire_cnav_2026_12_07042026.pdf | 2026-11-11 |
| CSS D613-4 current2026, read for national Cipav micro23.2%; combine with DOM fractions in D756-5 | https://www.legifrance.gouv.fr/codes/id/LEGIARTI000049625445 | 2026-11-11 |
| CSS R243-6/6-1 and R243-10 to 16, read for collection, payment and correction/late-charge conditions | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006186436/ | 2026-11-11 |
| Service Public contribution-base and compulsory health pages, read for included pay, ceilings and employer half-health-cost minimum | https://entreprendre.service-public.gouv.fr/vosdroits/F24013; https://www.service-public.gouv.fr/particuliers/vosdroits/F20739 | 2026-11-11 |
| Service Public ordinary independent and micro payment pages, read for payment frequency, opening declaration, nil turnover and annual declaration route | https://entreprendre.service-public.gouv.fr/vosdroits/F31233; https://entreprendre.service-public.gouv.fr/vosdroits/F36232 | 2026-11-11 |
| CSS R613-1-1/1-2 and R613-8 to 12, read for missing-income assessments, statutory penalties and micro timing | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006126967/2026-03-14 | 2026-11-11 |
| CLEISS2026 financing, read for French-affiliated tax non-resident activity-income health contribution | https://www.cleiss.fr/docs/regimes/regime_france0.html | 2026-11-11 |
| CLEISS coordination register, read for Regulation 883/2004 applicable-law and posting context | https://www.cleiss.fr/reglements/883_index.html | 2026-11-11 |

Not yet confirmed: profession-specific regulated liberal/pension-fund contributions. Actual notified accident/mobility/contractual premiums must be obtained for each employer. Agricultural, public, maritime, artist-author, pre 2020 micro entrants and tourist accommodation computations are outside this ordinary private-employment and business schedule.
