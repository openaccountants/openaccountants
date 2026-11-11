---
name: france-tax-optimization
description: >
  Use this skill whenever asked about reducing tax in France, tax planning,
  saving tax, optimizing tax, allowances, deductions the client might be
  missing, or any question about legal strategies to minimize income tax for
  self-employed individuals and owner-managers in France. Trigger on phrases
  like "reduce tax", "tax planning", "save tax", "optimize", "allowances",
  "deductions I'm missing", "payer moins d'impôts", "optimisation fiscale",
  "réduire ses impôts", "défiscalisation". It covers micro or réel, EI, EURL
  and SASU, salary or dividend, PER, reductions, losses, timing, TVA and the
  abuse of law limits (LPF L64 and L64 A), with filing on impots.gouv.fr and
  urssaf.fr. ALWAYS read this skill before advising on any French tax
  optimization strategy. This Tier 2 draft supports source checking and
  reviewer questions; it does not authorise a tax position.
version: 1.3
jurisdiction: FR
tax_year: 2026
tax_year_notes: "Planning for income of 2026, declared in 2027, read at 5 November 2026. Art. 197 as amended by LF 2026 art. 4 is the law at that date, and its note applies it to tax due for 2025 and later years. The final position for income of 2026 is held, because a loi de finances for 2027 can amend it and PLF 2027 is a bill."
last_updated: 2026-11-05
depends_on: []
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: tax-optimization
---

# France Tax Optimization v1.3
> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

French tax residents who are self-employed (micro-entrepreneur, entreprise individuelle at réel) or who own and run an EURL, SARL or SASU, and their households. Agricultural income is outside this guide. Tax residence (CGI art. 4 B) is a fact to establish, not a default.

### What this file is

**Coverage label: planning for income of 2026, declared in 2027, read at 5 November 2026.** Art. 197 as amended by LF 2026 art. 4 is the law at that date: its note applies it to income tax due for 2025 and later years, so it reaches income of 2026 unless a loi de finances for 2027 amends it. None is enacted, so the final position for income of 2026 is held. This file lists rules and the condition on which each one works. It does not say what a named client should do. Each comparison gives the arithmetic and leaves the choice to the client and a French adviser.

This guide has no `depends_on` base. It leans on these siblings, which own their figures:

- [fr-income-tax](fr-income-tax.md): the income tax computation, décote, single-parent and other art. 197 amounts, deadlines, late filing penalties.
- [fr-social-contributions](fr-social-contributions.md): every contribution rate. Its text was not yet converted when this guide was read, so no rate is taken from it here.
- [france-vat-return](france-vat-return.md): TVA return lines, rates and place of supply.
- [france-payroll](france-payroll.md): employer and employee charges on a salary.

### Refusals

Each refusal is a full stop. Give the message and do no partial planning.

| Trigger | Exact message |
| --- | --- |
| The client asks to design, paper over or defend an act that is fictitious; an act that seeks a literal application of a text against its authors' aims, with avoiding or reducing tax as its only or main motive; or an arrangement within CGI art. 205 A | I cannot design or support this arrangement. It may fall within LPF art. L. 64 or L. 64 A, or CGI art. 205 A, and it needs a qualified French adviser before anything is done. |
| French tax residence is unknown or denied | I cannot apply these planning rules until French tax residence is established. Please confirm it with a qualified French adviser. |
| The client wants a final tax figure at the barème for income of 2026 | Art. 197 as it stands at 5 November 2026 applies to tax due for 2025 and later years, but a loi de finances for 2027 can amend it, so any figure for income of 2026 is provisional. I can show that figure, labelled as subject to amendment, and nothing more. |

### Rules for every answer

1. Questions come first. Ask the facts in 'Ask the client first' before any figure or comparison. Whatever stays unanswered is **Needs Input**: do not fill it with an assumed rate, status or election.
2. Give each strategy with its condition. A strategy with an unmet condition is not available, and an unknown condition is Needs Input.
3. A bill is not law. PLF 2027 and PLFSS 2027 figures are never used; see 'Enactment position'.
4. Every comparison states whether social contributions are in it. Where they are not, say so: the answer is an income tax comparison only.
5. A tax motive alone does not trigger the first refusal. L. 64 needs a fictitious act, or a literal application against the text's aims with no other motive. L. 64 A, on BOFiP, needs that application with tax as the main motive. Art. 205 A needs a non-genuine arrangement whose advantage goes against the object or purpose of the tax law. A choice the law offers, such as a PER payment within its limit, stays available on its conditions. If the facts do not show whether a test is met, that point is Needs Input and goes to a qualified French adviser.

### Red flags

- The saving comes only from the tax result, with no business or family reason for the act. That alone is not abuse: test it under rule 5.
- A strategy is called 'automatic': ACRE, the réel option, the versement libératoire and the TVA option all need a step by a date.
- A figure is quoted for a year other than the one the text gives, above all the PER limit.

## Rates, bands and thresholds

Read each table for its named year. Figures a sibling owns are repeated only where a worked example needs them.

**Barème, art. 197 as it stands at 5 November 2026, for tax due for 2025 and later years (EUR per part)**

| Over | Up to | Rate on the fraction | Source |
| --- | --- | --- | --- |
| 0 | 11,600 | 0% | Art. 197 I 1 CGI, as amended by LF 2026 art. 4, read in DILA LEGI open data: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260730-222818.tar.gz |
| 11,600 | 29,579 | 11% | same |
| 29,579 | 84,577 | 30% | same |
| 84,577 | 181,917 | 41% | same |
| 181,917 | and above | 45% | same |

For income of 2026 these figures are the law as it stands, and the final position is held because a loi de finances for 2027 can amend them. The limits 11,497, 29,315, 83,823 and 180,294 are those for income of 2024.

**Quotient familial**

| Household | Parts | Source |
| --- | --- | --- |
| Single, no children | 1 | Art. 194 CGI, read in DILA LEGI open data: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260702-223445.tar.gz |
| Married or PACS, no children | 2 | same |
| Married or PACS, 1 child | 2.5 | same |
| Married or PACS, 2 children | 3 | same |
| Married or PACS, 3 children (1 full part from the 3rd child) | 4 | same |
| Cap on the reduction, per half part above 1 or 2 parts | EUR 1,807 | Art. 197 I 2 CGI: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260730-222818.tar.gz |

Other art. 197 amounts and the single-parent rules stay in fr-income-tax.

**Micro regimes**

| Activity | Limit, turnover excluding VAT | Abatement | Source |
| --- | --- | --- | --- |
| BIC: sale of goods, food to take away or eat in, lodging other than furnished dwellings (art. 50-0 1 1°) | EUR 203,100 | 71%, at least EUR 305 | Art. 50-0 1 CGI, version of 1 July 2026, read in DILA LEGI open data: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261104-214059.tar.gz |
| BIC: other activities, including services (art. 50-0 1 2°) | EUR 83,600 | 50%, at least EUR 305 | same |
| Furnished tourist lodging other than those in art. 1414 bis I 1° and 2°, which was not read (art. 50-0 1 1° bis) | EUR 15,000 | 30%, at least EUR 305 | same |
| BNC (art. 102 ter 1) | EUR 83,600 | 34%, at least EUR 305 | Art. 102 ter 1 CGI, version of 1 July 2026: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261103-214151.tar.gz |
| Earlier limits, shown for income of 2025 | EUR 188,700 and EUR 77,700 | as above | Brochure pratique 2026, part 11: https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/11-revenus_non_salaries_161a182.pdf |

The test is on the previous or the penultimate calendar year, pro rata to the time of activity in the reference year. Where an activity spans categories, total turnover must meet the 1° limit, and the 1° bis and 2° turnover must each meet its own limit. Several businesses are added together (art. 50-0 2 a). Art. 50-0 2 lists further exclusions, not summarised here. The limits other than EUR 15,000 are updated every 3 years. Arts 50-0 and 102 ter carry these figures in their versions of 1 July 2026. The LEGI record of each names décret n° 2026-562 art. 2 as the modifying text; the decree itself was not read.

**Versement libératoire**

| Item | Figure | Source |
| --- | --- | --- |
| Rate, goods (art. 50-0 1 1°) | 1% of turnover | Art. 151-0 II CGI, read in DILA LEGI open data: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260702-223445.tar.gz |
| Rate, other BIC activities (art. 50-0 1 2°) | 1.7% of turnover | same |
| Rate, BNC | 2.2% of receipts | same |
| Household income test, year N-2, as published: single | EUR 29,579 | Service-Public F23267: https://entreprendre.service-public.gouv.fr/vosdroits/F23267 |
| Same test, couple sharing a household | EUR 59,158 | same |
| Same test, couple with 1 child | EUR 73,947.50 | same |
| Same test, couple with 2 children | EUR 88,737 | same |

Art. 151-0 I sets 3 conditions, all required: the micro-fiscal regime; household income of the penultimate year, per part, of at most the upper limit of the second band of the barème of the year before the option year, plus 50% per extra half part or 25% per extra quarter part; and the micro-social regime (CSS art. L. 613-7).

**Corporate income tax**

| Item | Figure | Source |
| --- | --- | --- |
| Reduced rate | 15% on the first EUR 42,500 of profit per 12 months | Art. 219 I b CGI, read in DILA LEGI open data: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260907-214720.tar.gz |
| Normal rate | 25% | Art. 219 I CGI: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260907-214720.tar.gz |

Reduced rate conditions, all required: turnover of at most EUR 10 million for the period, annualised (for a group parent, the sum of the members' turnover); capital fully paid up; capital held continuously at 75% or more by natural persons, or by a company that meets the same test and is itself held at 75% or more by natural persons. Art. 219 I b gives a special rule for certain venture and fund holdings in this percentage: check its list.

**PER and Madelin limits**

| Item | Figure | Source |
| --- | --- | --- |
| General limit, contributions paid in 2026: maximum | EUR 37,680 | Art. 163 quatervicies I 2 a CGI: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260702-223445.tar.gz and brochure 2026, part 12: https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/12-charges_ded_rev_225a236.pdf |
| Same: minimum | EUR 4,710 | same |
| TNS limit, retirement (art. 154 bis II 1°) | Higher of: 10% of profit up to 8 PASS plus 15% of profit between 1 and 8 PASS; or 10% of PASS | Art. 154 bis II 1° CGI, read in DILA LEGI open data: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260602-214656.tar.gz |
| Same, arithmetic at PASS EUR 48,060 and profit of EUR 384,480 or more | EUR 88,911 | same |
| Same, floor at PASS EUR 48,060 | EUR 4,806 | same |
| Plafond annuel de la sécurité sociale (PASS), 2026 | EUR 48,060 | Service-Public F11677: https://entreprendre.service-public.gouv.fr/vosdroits/F11677 |
| Age limit | No deduction from the 70th birthday | Art. 163 quinvicies CGI: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260702-223445.tar.gz |

EUR 38,448 and EUR 4,806 are 10% of 8 PASS 2026 and 10% of PASS 2026. They are not the general limit for contributions paid in 2026: art. 163 quatervicies I 2 a looks at the previous year, and the brochure gives EUR 37,680 and EUR 4,710. Art. 154 bis does not say in the words read which year's PASS applies or whether profit is measured before the contribution. Example 1 assumes PASS 2026 and profit before it.

**Social contribution reference points**

| Item | Figure | Source |
| --- | --- | --- |
| Abatement on the unified base, non-micro TNS | 26%, between a floor and a ceiling set by decree | CSS art. L. 136-3 III, read in DILA LEGI open data: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260723-224400.tar.gz |
| CSG on activity income | 9.2% | CSS art. L. 136-8 I 1°, version of 27 June 2026: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260724-222927.tar.gz |
| Of which deductible from income tax | 6.8 points | Art. 154 quinquies I CGI: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260629-223234.tar.gz |
| CSG on L. 136-6 income from income of 2025 and L. 136-7 income from 1 January 2026 | 10.6%, with the exceptions in IV at 9.2% and those in LFSS 2026 art. 12 II | CSS art. L. 136-8 I 2° and IV: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260724-222927.tar.gz and LFSS 2026 art. 12: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260629-223234.tar.gz |
| ACRE, base up to 3/4 PASS | Exoneration of at most 25% of the listed contributions | CSS art. L. 131-6-4 II, in force 1 January 2026: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260724-222927.tar.gz |
| ACRE, base above 3/4 PASS | Falls linearly to nil at 1 PASS | same |

The floor and ceiling amounts and all contribution rates belong to fr-social-contributions. The exceptions in art. L. 136-8 IV include land income (art. L. 136-6 I a) and products of capitalisation contracts and like placements (art. L. 136-7 II 3°). Total social levies on capital are in 'Not yet confirmed'.

**Household reductions and credits**

| Item | Rate | Limit | Source |
| --- | --- | --- | --- |
| Emploi à domicile, credit | 50% | EUR 12,000; plus EUR 1,500 per child or per person over 65 (half for a shared child), up to EUR 15,000; EUR 15,000 and EUR 18,000 in the first year of the art. 199 sexdecies 1 a route only; EUR 20,000 for listed invalidity | Art. 199 sexdecies 3 and 4 CGI, read in DILA LEGI open data: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260915-211944.tar.gz |
| Same, sub-limit: gardening | same | EUR 5,000 per household | Code du travail art. D. 7233-5 3°: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260615-221231.tar.gz |
| Same, sub-limit: computer help at home | same | EUR 3,000 per household | same, 2° |
| Same, sub-limit: minor repairs | same | EUR 500 per household, 2 hours per visit | same, 1° |
| Donations, general | 66% | 20% of taxable income; excess carried 5 years | Art. 200 1 and 1 bis CGI: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260911-215706.tar.gz |
| Donations, art. 200 1 ter bodies | 75% | EUR 2,000, outside the 20% limit, for payments from 14 October 2025 | Art. 200 1 ter CGI: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260911-215706.tar.gz and LF 2026 art. 28 II: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261012-212534.tar.gz |
| IR-PME, general | 18% | EUR 50,000 single; EUR 100,000 joint | Art. 199 terdecies-0 A I and II CGI: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261021-213023.tar.gz |
| IR-PME, entreprises d'utilité sociale under art. 199 terdecies-0 AA | 25% on payments from 1 January 2026 to 31 December 2027. For payments from 1 October 2026 it applies only from the date set by décret n° 2026-968, 22 October 2026, so payments of 1 to 21 October 2026 are held | as above | LF 2026 art. 26 II and III and the decree, as noted on art. 199 terdecies-0 A: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261021-213023.tar.gz |
| Crédit d'impôt formation des dirigeants | Not available | Art. 244 quater M applied to hours to 31 December 2024 and was abrogated | LF 2026 art. 17: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261012-212534.tar.gz and last version of art. 244 quater M: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260701-222046.tar.gz |
| Plafonnement des niches, general | n/a | EUR 10,000 | Art. 200-0 A 1 CGI: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260223-224003.tar.gz |
| Same, with arts 199 undecies A, B and C, 199 unvicies and 199 novovicies XII | n/a | EUR 18,000 combined | same |

**Assurance-vie**

| Item | Figure | Source |
| --- | --- | --- |
| Annual allowance on proceeds, contract of 8 years or more | EUR 4,600, or EUR 9,200 for a couple filing jointly | Art. 125-0 A I CGI, read in DILA LEGI open data: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260702-223445.tar.gz |
| Rate after 8 years | 7.5%, subject to the EUR 150,000 premium test | Art. 125-0 A and art. 200 A CGI: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260702-223445.tar.gz |
| Death benefit, art. 990 I | EUR 152,500 per beneficiary, then 20% up to EUR 700,000 of the taxable part and 31.25% above | Art. 990 I CGI: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260505-215314.tar.gz |

**Depreciation, meals and mileage**

| Item | Figure | Source |
| --- | --- | --- |
| Dégressif coefficient, normal life 3 or 4 years | 1.25 | Art. 39 A 1 CGI, read in DILA LEGI open data: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260223-224003.tar.gz |
| Dégressif coefficient, 5 or 6 years | 1.75 | same |
| Dégressif coefficient, over 6 years | 2.25 | same |
| Small equipment and office items expensed, by tolerance | Unit value excluding VAT of at most EUR 500 | BOI-BIC-CHG-20-30-10: https://bofip.impots.gouv.fr/bofip/2109-PGP.html |
| Meal at home value, BNC, 2026 | EUR 5.50 | BOI-BNC-BASE-40-60-60: https://bofip.impots.gouv.fr/bofip/4628-PGP.html |
| Meal limit above which excessive, 2026 | EUR 21.40 | same |
| Maximum deductible per meal, 2026 | EUR 15.90 | same |
| Mileage, 6 CV thermal, hydrogen or hybrid, 5,001 to 20,000 km | (d × 0.374) + 1,457 | Brochure 2026, part 6, table 5: https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/06-traitements_salaires_85a114.pdf |
| Mileage, 6 CV fully electric, same band | (d × 0.473) + 1,818 | same |

**TVA**

| Item | Figure | Source |
| --- | --- | --- |
| Franchise, goods and lodging | EUR 85,000; ends in the year above EUR 93,500 | Art. 293 B I and II CGI, read in DILA LEGI open data: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260929-213457.tar.gz |
| Franchise, services | EUR 37,500; ends in the year above EUR 41,250 | same |
| Franchise, lawyers, authors and performers on their listed work | EUR 50,000 and EUR 35,000; EUR 55,000 and EUR 38,500 in the year | Art. 293 B I bis CGI: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260929-213457.tar.gz |
| Régime simplifié, previous year, base value | EUR 818,000 (sales, catering, lodging); EUR 247,000 (other) | CIBS art. L. 162-4: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260731-221216.tar.gz |
| Régime simplifié, current year, base value | EUR 901,000 and EUR 279,000 | CIBS art. L. 162-5: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260731-221216.tar.gz |
| Acomptes, régime simplifié | 55% in July and 40% in December, of the prior year's tax before deducting TVA on fixed assets | Art. 287 3 CGI: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261027-211214.tar.gz |
| Acompte exemption | Prior year's tax, before deducting TVA on fixed assets, below EUR 1,000 | same |
| Monthly returns instead (art. 287 3 bis): turnover below the art. L. 162-4 1° and 2° limits | Tax due for the prior year above EUR 15,000 | same |
| Monthly returns instead (art. 287 3 ter): régime simplifié | Intra-EU acquisitions, imports or exits from the suspensive regimes in art. 277 A I 2° | same |

The CIBS figures are the values for 2020 to 2022, indexed every 3 years. The values now applying are held, so EUR 840,000 and EUR 254,000 are not confirmed here. Art. 293 B, art. 302 septies A and CIBS arts L. 162-1, L. 162-4 and L. 162-5 show an end date of 1 January 2027, with no note read explaining it. Arts 269, 287 and 293 F carry a note that ordonnance n° 2025-1247 repeals them from 1 January 2027, except what the first column of its art. 15 table keeps. The notes say those kept parts are art. 293 F II and III, the first and last paragraphs of art. 269 2 c and all of art. 287, in force until regulations under the CIBS take them up. The art. 15 table and the successor text were not read, so the rules after 31 December 2026 are held.

### Enactment position

| Text | Status at 5 November 2026 | Effect here | Source |
| --- | --- | --- | --- |
| LF 2026, loi n° 2026-103 of 19 February 2026 | Enacted | Barème for tax due for 2025 and later years (art. 4, noted on art. 197); age 70 rule (art. 9); PER carry of 5 years (art. 10); donation cap (art. 28) | LF 2026 arts 9, 10 and 28 are separate Sources rows; art. 9, read in DILA LEGI open data: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261012-212534.tar.gz |
| LFSS 2026, loi n° 2025-1403 of 30 December 2025 | Enacted | CSG of 10.6% on capital income (art. 12); ACRE from 1 January 2026 (art. 23, noted on CSS art. L. 131-6-4) | LFSS 2026 art. 12: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260629-223234.tar.gz |
| Loi n° 2026-534 of 25 June 2026, art. 65 | Enacted | Art. 154 quinquies version, for income tax of 2026 onward | Art. 154 quinquies CGI, NOTA: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260629-223234.tar.gz |
| PLF 2027 (n° 3210) | Bill. Rejected by the Assemblée nationale on 4 November 2026 (T.A. n° 362); Senate stage not read | No figure used, including the tabled barème in its art. 2 | Assemblée nationale dossier: https://www.assemblee-nationale.fr/dyn/17/dossiers/plf_2027 |
| PLFSS 2027 (n° 3211) | Bill. Text n° 358 was considered rejected on 23 October 2026; text n° 138 went to the Senate on 2 November 2026 | No figure used | Sénat dossier: https://www.senat.fr/dossier-legislatif/plfss2027.html |

## The base

### Micro or réel

Compare deductible actual costs with the abatement, which replaces them. Réel is lower on income tax only when actual deductible costs exceed the abatement, and contributions must be compared separately. The micro-social charge is a global rate on turnover or receipts actually realised (CSS art. L. 613-7), with no abatement before that rate. A micro-fiscal person outside micro-social pays on the art. 50-0 or 102 ter profit (CSS art. L. 136-3 IV). Non-micro contributions run on the unified base below.

Option dates are in 'Deadlines and filing'. A micro business that does not opt must keep the records in art. 50-0 5.

### EI, EURL or SARL at IS, and SASU

| Point | EI or EURL at income tax | EURL or SARL at IS, majority gérant | SASU, président |
| --- | --- | --- | --- |
| Tax on profit | Barème on the whole profit | 15% and 25% if the art. 219 conditions are met | Same as the IS column |
| Pay | No deductible pay for the owner | Deductible if for real work and not excessive (art. 39 1 1°); taxed under art. 62 | Deductible on the same test; charges are in france-payroll |
| Social regime | Non-salaried (TNS) | Non-salaried; a gérant group holding at most half falls in CSS art. L. 311-3 11° | Assimilé salarié, CSS art. L. 311-3 23° |
| Dividends and social base | n/a | Part above 10% of the reference amount enters the TNS base | Levies on capital; see the check below |

No single profit level decides this. A trigger of EUR 60,000 and a social figure of 45% have no source read and are held. The comparison needs the actual contribution rates, the household's marginal rate and how much profit the owner must draw.

**Salary or dividend.** Dividends come from profit after IS. For an individual they bear 12.8% (art. 200 A 1 B 1°), or the barème on the global option (art. 200 A 2) with the 40% abatement of art. 158 3 2°, plus social levies. Salary is deductible under the art. 39 test and bears charges. Any figure is Needs Input until those charges are computed in france-payroll or fr-social-contributions.

**Dividends of a TNS.** CSS art. L. 136-3 II 2° brings into the base the part of dividends received by the TNS, spouse, PACS partner or unemancipated minor children above 10% of a reference amount: capital including share premiums held by those persons in full ownership or usufruct, plus their partner current accounts. An entrepreneur individuel has a different reference amount, set out in the same text. That rule addresses travailleurs indépendants. A SASU président sits in CSS art. L. 311-3 23°, and art. L. 242-1 bases contributions on activity income under art. L. 136-1-1. Art. L. 136-1-1 was not read, so confirm that dividends stay outside it before relying on the comparison.

### Deductions most people miss

Each applies only where the client is at réel for that head, or as stated for salaried frais réels.

| Item | Rule and condition | Basis |
| --- | --- | --- |
| Compulsory social contributions | Deductible from BIC and BNC profit | Art. 154 bis I |
| CSG déductible | 6.8 of the 9.2 points on activity income. Art. 154 quinquies I covers CSG only; the CRDS text was not read | Art. 154 quinquies I |
| Mileage | Salaried: within frais réels, replacing the 10% deduction, with the 40 km home to work limit unless justified. BNC: an option if the owned vehicle is on the immobilisations register, for the whole year and all vehicles, with no actual costs alongside, normally chosen at 1 January, with proof of kilometres. BIC use is held | Art. 83 3°; BOI-BNC-BASE-40-60-40-20 |
| Home office | Actual costs necessary for the business only. No text read fixes a floor area method, so that method is a condition for the adviser | Art. 39 1 1°, art. 93 1 |
| Training | Deductible only as a cost necessary for the current activity | Art. 39 1 1°, art. 93 1 |
| Professional dues | Orders, unions and associations, if necessary for the profession | Art. 93 1 |
| Solo meals, BNC | Actual cost less the home value, within the excessive limit, only if the meal was needed for the work and is justified | BOI-BNC-BASE-40-60-60 |
| Loan interest | A general expense where it is a real cost of the business; art. 39 1 1° does not itself name interest. Interest to partners on their advances is limited by art. 39 1 3° | Art. 39 1 1° and 3° |
| Insurance | Professional cover as a necessary cost. Madelin prévoyance within 7% of PASS plus 3.75% of profit, capped at 3% of 8 PASS | Art. 154 bis II 2° |

### Depreciation

Straight line is the default. Dégressif is for equipment of industrial businesses, other than dwellings, building sites and premises used for the profession, within the categories of annexe II art. 22, not already used when acquired, with a normal life of at least 3 years (art. 39 A; BOI-BIC-AMT-20-20-20). Annexe II was not read, so which IT assets qualify, use by BNC taxpayers and the rule that dégressif starts on the first day of the month of acquisition are all held. The start date for straight line, which the earlier version put at entry into service, has no text read and is held too. If that start rule is confirmed, a purchase early in the year gives more first-year months.

The EUR 500 tolerance covers small tools and equipment of the kind in accounts 2154 and 2155, and office items. The test takes the whole price of an item made of several parts. It does not cover the first fit-out of premises or a complete renewal, unless the total is itself within EUR 500. Above it, normal depreciation applies.

Super-depreciation is not a general 40% rule. Art. 39 decies covered acquisitions from 15 April 2015 to 14 April 2017. Arts 39 decies B, D, E and G have expired on their terms. Three schemes read as live cover named assets only, each at its own rates: art. 39 decies A (heavy low-emission vehicles, to 31 December 2030 by energy type), art. 39 decies C (ships, to 31 December 2027) and art. 39 decies F (listed machinery in named sectors, 2024 to 31 December 2026). None is a general robotics, digital or energy transition scheme; arts 39 decies A and C reach low-emission or decarbonised energy only for the named vehicles and ships.

Reliefs by area or status carry their own conditions: JEI (arts 44 sexies-0 A and 44 sexies A; art. 44 sexies-0 A shows an end date of 1 January 2029, with no note read explaining it), new businesses in regional aid zones (art. 44 sexies, created to 31 December 2027) and ZFU (art. 44 octies A, creations to 31 December 2025).

### Losses

| Loss | Treatment | Basis |
| --- | --- | --- |
| BIC with personal, continuous and direct participation; professional BNC | Against global income in the year. The excess carries to the 6th following year against global income, not only the same category | Art. 156 I |
| BIC without that participation | Only against income of the same kind of activity, that year and the next 6 | Art. 156 I 1° bis |
| BNC not from a regular profession | Only against income of the same nature, that year and the next 6 | Art. 156 I 2° |
| Non-professional furnished letting | Only against such income, next 10 years | Art. 156 I 1° ter |
| Land income, costs other than interest | Against global income up to EUR 10,700; EUR 15,300 for art. 31 I 1° f or o; up to EUR 21,400 for energy works taking a dwelling from E, F or G to A, B, C or D by 31 December 2027, with proof | Art. 156 I 3° |
| Land income, excess and interest | Exclusively against land income of the next 10 years | Art. 156 I 3° |

The rule for agricultural losses (other net income above EUR 128,826) is outside this guide. Art. 156 I 3° has monument and retention conditions not summarised here. Starting as a professional activity helps only if the participation or profession test is truly met. Non-professional losses are the common trap.

### Timing

- **Revenue.** Micro BNC tax is on annual gross receipts (art. 102 ter 1). Micro-social is on turnover or receipts actually realised (CSS art. L. 613-7). BNC at réel is receipts less expenses (art. 93 1), unless the art. 93 A option applies: profit is then receivables acquired less expenses incurred in the year, so paying later moves nothing. Micro BIC tax is on turnover (art. 50-0 1); whether that means cash is not stated in the text read, so 'recognised when received' is not confirmed for micro BIC. Réel BIC attaches sales to delivery and services to completion (art. 38 2 bis), so a later invoice does not move that profit. Any deferred invoice must carry its true commercial date, and TVA has its own timing.
- **Expenses.** BNC at réel takes expenses required by the profession (art. 93 1). Prepaying moves a cost only if it is a real payment of a necessary cost, and not at all under the art. 93 A option, which counts expenses incurred. For BIC at réel, accounting for the period applies, so prepayment is not a planning tool on the text read.
- **PER.** Payment must be made in the year. A general limit left unused may be used in one of the 5 following years (art. 163 quatervicies I 2 b, as amended by LF 2026 art. 10). Brochure 2026 still describes 3 years, so read the limits shown on the avis d'imposition. Couples filing jointly may pool limits (art. 163 quatervicies I 2 a; box 6QR). The deduction cannot create or increase a global deficit.
- **Marriage or PACS.** Joint taxation covers the whole year of the event (art. 6 5), but the couple may instead opt, irrevocably, for separate taxation of that year. Compare both. A date before 31 December helps only if joint taxation helps.
- **Versement libératoire.** Paid at the micro-social periodicity, monthly or quarterly (art. 151-0 V; CSS art. L. 613-7).
- **Exceptional income.** The quotient of art. 163-0 A applies on request. It covers income that by its nature is not annual and exceeds the average net income of the last 3 years, the items listed in its I, and deferred income in II, in each case only if taxed at the barème. Add one quarter of the net exceptional income to the other income, and multiply the tax increase by 4.

### TVA

- **Franchise.** Below the limits no TVA is charged and none is recovered. The first limit in the table looks to the previous year's turnover. Passing the second limit ends the franchise from that date (art. 293 B II). In B2C it can help the price. A B2B client that recovers TVA gains nothing from it, and the supplier loses input recovery.
- **Option.** Worth testing where input TVA is significant. It takes effect on the first day of the month of declaration, covers 2 years, including the year of declaration, renews tacitly unless cancelled, and renews automatically for 2 years after a refund (art. 293 F II).
- **Régime simplifié.** Annual return with July and December acomptes, not quarterly payments, unless art. 287 3 bis or 3 ter requires monthly returns. The base is before TVA on fixed assets: with prior year tax of EUR 2,000 before and EUR 500 after that TVA, the acomptes are EUR 1,100 and EUR 800 and the exemption does not apply. Art. 287 3 also has the new taxpayer rule and the 10% adjustment.
- **Services.** TVA falls due on payment received, or on debits by option (art. 269 2 c). Encaissements is the default, so a provider on it already defers. Art. 269 has other rules for goods.
- **Intra-EU B2B services.** Place of supply and reverse charge are in france-vat-return. DES and DEB reporting was not read here and is held.

### Social contributions

Non-micro TNS contributions and CSG run on the unified base of CSS arts L. 131-6 and L. 136-3 for periods from 1 January 2025: income built under CGI arts 34 to 40 and 42 septies or art. 93, before contributions and without long-term gains, less the 26% abatement. Contributions are provisional on the penultimate year's base, recalculated once the last year is known and regularised once the year's figures are known; on request they can use an estimate of the current year (art. L. 131-6-2). Urssaf's page says regularisation follows the income declaration. A fixed July adjustment is held.

The rates belong to fr-social-contributions. No total effective rate is given here, because the former approximate table was not confirmed. That covers maladie-maternité, allocations familiales, retraite de base, retraite complémentaire, invalidité-décès, CRDS and the CFP.

- **ACRE.** Not automatic and not 50%. From 1 January 2026 it needs a request at creation and lasts 12 months, for people in the categories of code du travail art. L. 5141-1, other than those in CSS art. L. 642-4-2, or creators in art. 44 quindecies A zones (CSS art. L. 131-6-4). Service-Public gives 60 days from opening the activity to file. It cannot be repeated within 3 years (art. L. 131-6-4 IV), and a company creator must keep effective control for at least 2 years, or Urssaf may withdraw it and ask for repayment (Service-Public F11677). It does not combine with other reductions except those in art. L. 131-6-4 III. For a micro-entrepreneur, the page read shows 75% of the normal rate.
- **Minimum contributions.** A micro-entrepreneur may ask for contributions no lower than the minimum (CSS art. L. 613-7). For non-micro TNS, a loss year can still bring contributions; the minimum bases are in fr-social-contributions.
- **Conjoint collaborateur.** For a spouse working regularly in the business (code de commerce art. L. 121-4, which says conjoint; any extension to a PACS partner is held). In a company, only for the spouse of a sole or majority gérant of an SARL or SELARL. The status must be declared and lasts at most 5 years in total across all businesses (IV bis). The cost is held.
- **PER and the social base.** The art. L. 136-3 base is built from arts 34 to 40, 42 septies or 93, not art. 154 bis, and the Urssaf notice asks the TNS to declare Madelin premiums and PER payments. No text read says this expressly: it is an inference that a PER contribution does not reduce the base, so count no social saving unless a text shows otherwise.

### PER and retirement

- **Which limit.** Salaried and others use art. 163 quatervicies. A TNS uses art. 154 bis II 1° or art. 163 quatervicies. The art. 163 quatervicies limit is reduced by art. 83 2° sums and by art. 154 bis II 1° and related sums, not counting the 15% fraction, and by listed employer sums. Art. 154 bis II 1° is reduced by firm sums under art. 81 18° a and a bis. So the 2 limits are not added together.
- **Income test.** Art. 163 quatervicies uses 10% of the previous year's professional income as defined in its II, not 'net taxable income'.
- **Value.** The saving is the marginal rate on each slice removed, so use the barème, not one rate. EUR 88,911 at 45% is EUR 40,009.95 only where the whole sum sits in the 45% band: for one part, profit of at least EUR 384,480, on art. 197 as it stands. More parts need more income.
- **After 70.** From 1 January 2026 (LF 2026 art. 9) art. 163 quinvicies bars the deduction for payments to a PER or PEPP sub-account from the 70th birthday, under arts 154 bis, 154 bis-0 A, 163 quatervicies I 1 d, 83 2° and 81. Whether older PERP or Madelin contracts stay outside it is held. No exception was read.
- **Exit.** The capital matching deducted payments is taxed at the barème without the 10% abatement. The product part follows art. 200 A (art. 158 5 b quinquies). Early release is limited to CMF art. L. 224-4: death of a spouse or partner; invalidity of the holder, a child, spouse or partner; serious illness, disability or accident of a dependent child; over-indebtedness; end of unemployment rights or the listed loss of a corporate office; business liquidation; main home purchase, except sums from compulsory payments; and holders under 18.
- **Non-deduction option.** Irrevocable, payment by payment, no later than the payment (CMF art. L. 224-20). The brochure treats the capital part matching undeducted payments as exempt, but the product part stays taxable, so 'tax-free capital' overstates it. It gives up the entry deduction, so it is worth testing where the marginal rate at entry is low, such as 0% or 11%. Social levies on exit are in 'Not yet confirmed'.

### Assurance-vie and reductions

Premiums are not deductible. The 8-year allowance and rate apply to all of a person's contracts together. The art. 990 I levy applies where art. 757 B does not. Art. 757 B, which the text links to the age rule, was not read, so the age 70 condition is held.

For IR-PME, shares must be kept to 31 December of the 5th year after subscription, and repayment before 31 December of the 7th year claws the relief back, unless it follows judicial liquidation. Company tests and fund routes are set out in art. 199 terdecies-0 A; FCPI payments have limits of EUR 12,000 and EUR 24,000 (VI). LF 2026 arts 22 and 26 changed named routes, so read the text for the year of payment. Other funds are not summarised here.

The niche cap does not cover every reduction. Art. 200-0 A 2 b excludes art. 200 donations, art. 199 septies, art. 199 quater C and others it lists. Emploi à domicile is not on that exclusion list as read. Any rule on the fate of an excess was not read, so 'lost forever' is held.

## Deadlines and filing

The income of 2025 return is closed: online deadlines were 21 May, 28 May and 4 June 2026 by département, and 19 May on paper (brochure pratique 2026, part 4). Dates for income of 2026 are held. File income tax on impots.gouv.fr and social declarations on urssaf.fr or autoentrepreneur.urssaf.fr. Corporate tax and TVA use the professional space on impots.gouv.fr.

| Date | Step | Basis |
| --- | --- | --- |
| At creation; Service-Public gives 60 days from opening the activity | Ask for ACRE | CSS art. L. 131-6-4 II; Service-Public F11677 |
| Last day of the 3rd month after creation | Choose versement libératoire or minimum contributions | Art. 151-0 IV; CSS art. L. 613-7 |
| 31 December of the prior year | Micro-entrepreneur's request for minimum contributions | CSS art. L. 613-7 |
| Before 1 February of the year; on a start, the art. 97 return deadline | BNC at réel: art. 93 A option; applies until cancelled in the same way | Art. 93 A I |
| Income return deadline for the year before; separate dates on a creation or for a business that was on réel by law | Micro BIC option for réel; 1 year, renewed tacitly | Art. 50-0 4 |
| Form 2035 deadline | Micro BNC option for déclaration contrôlée; 1 year, renewed tacitly | Art. 102 ter 5 |
| 30 September of the prior year; on a creation, the last day of the 3rd month after it | Versement libératoire option; continues until cancelled, unless art. 151-0 IV 1° or 2° ends it | Art. 151-0 IV |
| July and December | TVA acomptes at the régime simplifié, unless art. 287 3 bis or 3 ter requires monthly returns | Art. 287 3 |
| 31 December | PER payments, donations, home service payments and IR-PME subscriptions that count for the year | Each article's year of payment |

Other months in a yearly plan (reviewing documents, profit or headroom) are good habits with no legal date.

## Penalties and interest

| Item | Rule | Source |
| --- | --- | --- |
| Deliberate failure | 40% | Art. 1729 a CGI, read in DILA LEGI open data: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260702-223445.tar.gz |
| Abuse of law under LPF L. 64 | 80%; 40% if the taxpayer is not shown to be the main initiator or main beneficiary | Art. 1729 b CGI: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260702-223445.tar.gz |
| Fraudulent manoeuvres | 80% | Art. 1729 c CGI: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260702-223445.tar.gz |
| Abuse of law under LPF L. 64 A | No automatic surcharge, because art. 1729 b names L. 64 only. Ordinary penalties (art. 1729 a or c) need their own proof | BOI-CF-IOR-30-20: https://bofip.impots.gouv.fr/doctrine/pgp/12049-PGP |
| Late payment interest | 0.20% per month | Art. 1727 III CGI: https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260812-214541.tar.gz |

**LPF art. L. 64** lets the administration set aside acts that are fictitious, or that seek a literal application of texts against their authors' aims and can have had no motive other than avoiding or reducing tax. The taxpayer or the administration may take the dispute to the comité de l'abus de droit fiscal.

**LPF art. L. 64 A** was not read in its own words. On BOFiP it covers acts from 1 January 2020 under rectifications notified from 1 January 2021, with avoiding or reducing tax as their main objective, on the same literal application test. BOFiP also says it reaches every tax except corporate tax, and that the L. 64 B rescrit and the comité extend to it. **CGI art. 205 A** is a separate corporate tax rule: it ignores an arrangement set up with, as the main objective or one of them, a tax advantage against the object or purpose of the tax law, and not genuine in the light of all the facts. An arrangement is not genuine so far as it lacks valid commercial reasons reflecting economic reality.

**LPF art. L. 64 B.** Neither procedure applies if the taxpayer consulted the central administration in writing before the acts, gave all useful facts, and had no answer within 6 months.

BOFiP says neither L. 64 nor L. 64 A bars choosing the most favourable legal framework, provided that choice and its conditions show no artificiality. BOFiP adds that L. 64 A does not reach acts whose essential aim is a tax advantage without going against the object or purpose of the tax law, and that in principle it does not reach a scheme the legislator encouraged by a tax incentive, even if mainly tax driven, unless the scheme is manifestly diverted from its purpose (BOI-CF-IOR-30-20). This is doctrine, and each case turns on its facts.

## Cross-border points

- A person newly resident after 3 years abroad has a different art. 163 quatervicies test and an extra limit of 3 times the difference (I 2 a and d), on the conditions there.
- Dividends get the art. 158 3 2° abatement only from companies in the EU or in a state with a qualifying treaty, on the terms of that text.
- Leaving France is in leaving-france-exit-tax. TVA place of supply is in france-vat-return.

## Two worked examples that recompute

All tax uses art. 197 as it stands at 5 November 2026, which a loi de finances for 2027 can amend for income of 2026, with the whole household income as stated and no décote at these levels. Each shows the facts and the arithmetic. None is a recommendation.

### Example 1: PER, BNC of EUR 100,000, single

The limit under art. 154 bis II 1° at PASS EUR 48,060, with profit before the contribution and no firm sums, is `max(10% × min(profit, 8 PASS) + 15% × max(min(profit, 8 PASS) − PASS, 0), 10% × PASS)`. Income falls to 82,209, crossing the 41% limit, so the saving is below 41% of the payment. No social saving is shown.

```oa-check
name: fr-opt-per-tns
inputs:
  profit: 100000
  pass_amount: 48060
steps:
  - cap: min(profit, 8 * pass_amount)
  - formula: 0.10 * cap + 0.15 * max(cap - pass_amount, 0)
  - limit: max(formula, 0.10 * pass_amount)
  - after: profit - limit
  - tax_before: (29579 - 11600) * 0.11 + (84577 - 29579) * 0.30 + (profit - 84577) * 0.41
  - tax_after: (29579 - 11600) * 0.11 + (after - 29579) * 0.30
  - saving: tax_before - tax_after
expected:
  limit: 17791.00
  after: 82209.00
  tax_before: 24800.52
  tax_after: 17766.69
  saving: 7033.83
```

### Example 2: Which should I choose, micro-BNC or réel? Receipts EUR 60,000, costs EUR 25,000

Single, no other income. Costs include all deductible contributions. Micro income is `60,000 × (1 − 34%)`. Réel income is `60,000 − 25,000`.

```oa-check
name: fr-opt-micro-v-reel
inputs:
  receipts: 60000
  costs: 25000
steps:
  - micro_income: receipts * (1 - 0.34)
  - reel_income: receipts - costs
  - micro_tax: (29579 - 11600) * 0.11 + (micro_income - 29579) * 0.30
  - reel_tax: (29579 - 11600) * 0.11 + (reel_income - 29579) * 0.30
  - reel_saves: micro_tax - reel_tax
  - breakeven_costs: receipts * 0.34
expected:
  micro_income: 39600.00
  reel_income: 35000.00
  micro_tax: 4983.99
  reel_tax: 3603.99
  reel_saves: 1380.00
  breakeven_costs: 20400.00
```

Worked both ways: with costs of EUR 25,000, réel saves EUR 1,380 of income tax. With costs under EUR 20,400 the abatement is larger and micro gives the lower income tax. This compares income tax only. Social contributions under each regime are Needs Input until computed in fr-social-contributions, and they can reverse the answer.

### Example 3: Quotient familial and its cap, EUR 80,000

Couple with 2 children, 3 parts, compared with a couple at 2 parts on the same income. The gain from the 2 half parts exceeds `2 × 1,807`, so the cap governs. The single figure is a reference only, because it describes a different household.

```oa-check
name: fr-opt-qf-cap
inputs:
  income: 80000
steps:
  - single: (29579 - 11600) * 0.11 + (income - 29579) * 0.30
  - two_parts: 2 * ((29579 - 11600) * 0.11 + (income / 2 - 29579) * 0.30)
  - three_parts: 3 * ((income / 3 - 11600) * 0.11)
  - uncapped_gain: two_parts - three_parts
  - cap: 2 * 1807
  - tax: max(three_parts, two_parts - cap)
  - qf_saving: two_parts - tax
expected:
  single: 17103.99
  two_parts: 10207.98
  three_parts: 4972.00
  uncapped_gain: 5235.98
  cap: 3614.00
  tax: 6593.98
  qf_saving: 3614.00
```

### Example 4: Emploi à domicile, EUR 6,000

The credit is 50% of the payments allowed. Gardening is capped at EUR 5,000, so the mix matters. Payments are net of any aid, and the service must qualify.

```oa-check
name: fr-opt-domicile
inputs:
  all_gardening: 6000
  gardening: 4000
  cleaning: 2000
steps:
  - credit_all_gardening: min(all_gardening, 5000) * 0.50
  - credit_mixed: (min(gardening, 5000) + cleaning) * 0.50
expected:
  credit_all_gardening: 2500.00
  credit_mixed: 3000.00
```

### Example 5: CSG déductible, EUR 80,000 before contributions

Non-micro TNS, with the 26% abatement inside the decree's floor and ceiling. The 6.8 points apply to the base after abatement, not to EUR 80,000.

```oa-check
name: fr-opt-csg
inputs:
  income: 80000
steps:
  - base: income * (1 - 0.26)
  - deductible: base * 0.068
  - saving_at_30: deductible * 0.30
expected:
  base: 59200.00
  deductible: 4025.60
  saving_at_30: 1207.68
```

### Example 6: Barème kilométrique, 6 CV, 15,000 km

Table in brochure 2026, for income of 2025. The table for 2026 use is held.

```oa-check
name: fr-opt-km
inputs:
  km: 15000
  salary: 50000
steps:
  - thermal: km * 0.374 + 1457
  - electric: km * 0.473 + 1818
  - gross_value_at_30: thermal * 0.30
  - allowance: clamp(salary * 0.10, 509, 14555)
  - extra_deduction: max(thermal - allowance, 0)
  - net_value_at_30: extra_deduction * 0.30
expected:
  thermal: 7067.00
  electric: 8913.00
  gross_value_at_30: 2120.10
  allowance: 5000.00
  extra_deduction: 2067.00
  net_value_at_30: 620.10
```

`gross_value_at_30` is an illustrative gross figure at an assumed 30% rate, not a saving. An employee uses the table inside frais réels, which replace the 10% deduction of art. 83 3° (at least EUR 509, at most EUR 14,555 for pay of 2025). With pay of EUR 50,000 after the contributions art. 83 lists and no other real costs, EUR 7,067 beats the EUR 5,000 deduction by EUR 2,067, worth EUR 620.10 at 30%. A BNC on the option has no 10% deduction, but the table replaces actual car costs, so compare it with those.

### Example 7: Dividends of a TNS gérant, base only

EURL at IS, sole gérant, capital EUR 5,000, no premium or current account, dividend EUR 30,000. The part in the TNS base before the 26% abatement is below. The contributions on it are Needs Input.

```oa-check
name: fr-opt-dividend-base
inputs:
  dividend: 30000
  capital: 5000
steps:
  - free: capital * 0.10
  - in_base: max(dividend - free, 0)
expected:
  free: 500.00
  in_base: 29500.00
```

## Ask the client first

1. Tax residence, household status and parts, age of each adult, and any change of status planned this year.
2. Activity, legal form (micro, EI, EURL, SARL, SASU), whether taxed at income tax or IS, and date of creation.
3. Income for the current, previous and penultimate years, household income of year N-2, and turnover and costs of any business, with prior year TVA before and after TVA on fixed assets, and any intra-EU acquisitions or imports.
4. Who owns the company, with capital, premiums and current accounts, and salary and dividends paid.
5. Existing elections and payments: versement libératoire, art. 93 A option, TVA option, PER, Madelin, firm contributions, ACRE, carried limits on the avis d'imposition, and losses carried.
6. The non-tax reason for the proposed act, and its date.

## Sources

'Read in DILA LEGI open data' means the article's XML in the named daily delta archive, the official open data of the Direction de l'information légale et administrative, because Légifrance refuses scripted requests. Each row says what was read.

| Source | URL | Read on |
| --- | --- | --- |
| CGI art. 197, LEGIARTI000053542636, VIGUEUR from 2026-02-21: read in part, I 1 and I 2 and the note on LF 2026 art. 4, in DILA delta 20260730-222818 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260730-222818.tar.gz | 2026-11-05 |
| CGI art. 194, LEGIARTI000033817781, VIGUEUR from 2018-01-01: read in part, the part counts, in DILA delta 20260702-223445 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260702-223445.tar.gz | 2026-11-05 |
| CGI art. 50-0, LEGIARTI000054373853, VIGUEUR from 2026-07-01: read in part, 1, 2 a and c, 4, 5 and the LEGI link to décret n° 2026-562 art. 2, in DILA delta 20261104-214059 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261104-214059.tar.gz | 2026-11-05 |
| CGI art. 102 ter, LEGIARTI000054373747, VIGUEUR from 2026-07-01: read in part, 1, 5 and the LEGI link to décret n° 2026-562 art. 2, in DILA delta 20261103-214151 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261103-214151.tar.gz | 2026-11-05 |
| CGI art. 151-0, LEGIARTI000051765182, VIGUEUR from 2025-06-19: read in part, I, II, III, IV and V, in DILA delta 20260702-223445 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260702-223445.tar.gz | 2026-11-05 |
| CGI art. 219, LEGIARTI000053542939, VIGUEUR from 2026-02-21: read in part, I opening and I b, in DILA delta 20260907-214720 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260907-214720.tar.gz | 2026-11-05 |
| CGI art. 163 quatervicies, LEGIARTI000053542827, VIGUEUR from 2026-02-21: read in part, I 1 and I 2 and the note, in DILA delta 20260702-223445 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260702-223445.tar.gz | 2026-11-05 |
| CGI art. 163 quinvicies, LEGIARTI000053542708, VIGUEUR from 2026-01-01: read in part, the age 70 paragraph, in DILA delta 20260702-223445 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260702-223445.tar.gz | 2026-11-05 |
| CGI art. 154 bis, LEGIARTI000047288764, VIGUEUR from 2023-03-11: read in part, I and II, in DILA delta 20260602-214656 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260602-214656.tar.gz | 2026-11-05 |
| CGI art. 154 quinquies, LEGIARTI000054336634, VIGUEUR from 2026-06-27: read in full, I, II and the note, in DILA delta 20260629-223234 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260629-223234.tar.gz | 2026-11-05 |
| CSS art. L. 136-3, LEGIARTI000051284498, VIGUEUR from 2025-02-28: read in part, I 1°, II 2°, III and IV, in DILA delta 20260723-224400 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260723-224400.tar.gz | 2026-11-05 |
| CSS art. L. 136-8, LEGIARTI000054336623, VIGUEUR from 2026-06-27: read in part, I and IV, version in force, in DILA delta 20260724-222927 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260724-222927.tar.gz | 2026-11-05 |
| CSS art. L. 136-6, LEGIARTI000051218166, VIGUEUR from 2025-02-16: read in part, I a, read as the cross reference in art. L. 136-8 IV 1°, in DILA delta 20260708-215132 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260708-215132.tar.gz | 2026-11-05 |
| CSS art. L. 136-7, LEGIARTI000053584839, VIGUEUR from 2026-02-21: read in part, II 3°, read as the cross reference in art. L. 136-8 IV 4°, in DILA delta 20260629-223234 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260629-223234.tar.gz | 2026-11-05 |
| CSS art. L. 131-6, LEGIARTI000048683707, VIGUEUR from 2023-12-28: read in part, I, in DILA delta 20261103-214151 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261103-214151.tar.gz | 2026-11-05 |
| CSS art. L. 131-6-2, LEGIARTI000048683699, VIGUEUR from 2023-12-28: read in full, whole article, in DILA delta 20261103-214151 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261103-214151.tar.gz | 2026-11-05 |
| CSS art. L. 131-6-4, LEGIARTI000053282569, VIGUEUR from 2026-01-01: read in full, whole article, in DILA delta 20260724-222927 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260724-222927.tar.gz | 2026-11-05 |
| CSS art. L. 613-7, LEGIARTI000048683570, VIGUEUR from 2023-12-28: read in part, I, in DILA delta 20261103-214151 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261103-214151.tar.gz | 2026-11-05 |
| CSS art. L. 311-3, LEGIARTI000051284232, ABROGE_DIFF from 2025-02-28 to 2027-01-01: read in part, 11°, 12° and 23°, in DILA delta 20261103-214151 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261103-214151.tar.gz | 2026-11-05 |
| CSS art. L. 242-1, LEGIARTI000053282401, VIGUEUR from 2025-12-31: read in part, I, opening sentence only, in DILA delta 20261104-214059 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261104-214059.tar.gz | 2026-11-05 |
| CGI art. 199 sexdecies, LEGIARTI000054251333, VIGUEUR from 2026-06-14: read in part, 1, 3, 4 and 6, in DILA delta 20260915-211944 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260915-211944.tar.gz | 2026-11-05 |
| Code du travail art. D. 7233-5, LEGIARTI000033747497, VIGUEUR from 2016-12-30: read in full, whole article, in DILA delta 20260615-221231 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260615-221231.tar.gz | 2026-11-05 |
| CGI art. 200, LEGIARTI000053543932, ABROGE_DIFF from 2026-02-21 to 2027-01-01: read in part, 1 opening, 1 bis and 1 ter, in DILA delta 20260911-215706 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260911-215706.tar.gz | 2026-11-05 |
| CGI art. 199 terdecies-0 A, LEGIARTI000053543691, VIGUEUR from 2026-02-21: read in part, I A, II, retention rules, VI and the notes on LF 2026 arts 22 and 26, in DILA delta 20261021-213023 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261021-213023.tar.gz | 2026-11-05 |
| CGI art. 244 quater M, LEGIARTI000051217460, ABROGE from 2025-02-16 to 2026-02-21: read in part, last version, including IV, in DILA delta 20260701-222046 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260701-222046.tar.gz | 2026-11-05 |
| CGI art. 200-0 A, LEGIARTI000053543258, VIGUEUR from 2026-02-21: read in part, 1 and 2 b, in DILA delta 20260223-224003 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260223-224003.tar.gz | 2026-11-05 |
| CGI art. 125-0 A, LEGIARTI000044989424, VIGUEUR from 2022-01-01: read in part, I and II, the allowance and rates, in DILA delta 20260702-223445 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260702-223445.tar.gz | 2026-11-05 |
| CGI art. 200 A, LEGIARTI000053546896, VIGUEUR from 2026-02-21: read in part, 1 and 2, in DILA delta 20260702-223445 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260702-223445.tar.gz | 2026-11-05 |
| CGI art. 990 I, LEGIARTI000047288653, VIGUEUR from 2023-03-11: read in part, I, in DILA delta 20260505-215314 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260505-215314.tar.gz | 2026-11-05 |
| CGI art. 158, LEGIARTI000054373673, VIGUEUR from 2026-07-01: read in part, 3 2° and 5 b quinquies, in DILA delta 20260702-223445 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260702-223445.tar.gz | 2026-11-05 |
| CGI art. 39 A, LEGIARTI000037987291, VIGUEUR from 2018-12-31: read in part, 1, in DILA delta 20260223-224003 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260223-224003.tar.gz | 2026-11-05 |
| CGI art. 39, LEGIARTI000053542680, ABROGE_DIFF from 2026-02-21 to 2027-01-01: read in part, 1 1° and 1 3°, in DILA delta 20260731-221216 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260731-221216.tar.gz | 2026-11-05 |
| CGI art. 38, LEGIARTI000051203585, VIGUEUR from 2025-02-16: read in part, 2 bis, in DILA delta 20260612-215918 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260612-215918.tar.gz | 2026-11-05 |
| CGI art. 93, LEGIARTI000053559885, ABROGE_DIFF from 2026-01-01 to 2027-01-01: read in part, 1, in DILA delta 20260730-222818 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260730-222818.tar.gz | 2026-11-05 |
| CGI art. 93 A, LEGIARTI000048847605, VIGUEUR from 2023-12-31: read in full, whole article, in DILA global dump 20250713-140000 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/Freemium_legi_global_20250713-140000.tar.gz | 2026-11-05 |
| CGI art. 83, LEGIARTI000054373766, VIGUEUR from 2026-07-01: read in part, 3°, in DILA delta 20261002-214631 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261002-214631.tar.gz | 2026-11-05 |
| CGI art. 6, LEGIARTI000046197457, VIGUEUR from 2022-08-18: read in part, 5 and 6, in DILA delta 20260702-223445 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260702-223445.tar.gz | 2026-11-05 |
| CGI art. 62, LEGIARTI000019288260, VIGUEUR from 2008-08-06: read in part, opening paragraphs, in DILA delta 20261103-214151 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261103-214151.tar.gz | 2026-11-05 |
| CGI art. 156, LEGIARTI000054373682, VIGUEUR from 2026-07-01: read in part, I, 1° to 3°, in DILA delta 20260702-223445 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260702-223445.tar.gz | 2026-11-05 |
| CGI art. 163-0 A, LEGIARTI000044978385, VIGUEUR from 2022-01-01: read in part, I, II and III, in DILA delta 20260702-223445 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260702-223445.tar.gz | 2026-11-05 |
| CGI art. 39 decies, LEGIARTI000033817526, VIGUEUR from 2017-01-01: read in part, I, dates, in DILA delta 20250727-211228 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20250727-211228.tar.gz | 2026-11-05 |
| CGI art. 39 decies A, LEGIARTI000051217636, VIGUEUR from 2025-02-16: read in part, I, scope and dates, in DILA delta 20250727-211228 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20250727-211228.tar.gz | 2026-11-05 |
| CGI art. 39 decies B, LEGIARTI000037943779, VIGUEUR from 2019-01-01: read in part, dates, in DILA delta 20250727-211228 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20250727-211228.tar.gz | 2026-11-05 |
| CGI art. 39 decies C, LEGIARTI000054373968, VIGUEUR from 2026-07-01: read in part, I, scope and dates, in DILA delta 20260702-223445 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260702-223445.tar.gz | 2026-11-05 |
| CGI art. 39 decies D, LEGIARTI000037938203, VIGUEUR from 2018-12-31: read in part, dates, in DILA delta 20250727-211228 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20250727-211228.tar.gz | 2026-11-05 |
| CGI art. 39 decies E, LEGIARTI000051217535, VIGUEUR from 2025-02-16: read in part, dates, in DILA delta 20250727-211228 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20250727-211228.tar.gz | 2026-11-05 |
| CGI art. 39 decies F, LEGIARTI000051217543, VIGUEUR from 2025-02-16: read in part, I, scope and dates, in DILA delta 20250727-211228 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20250727-211228.tar.gz | 2026-11-05 |
| CGI art. 39 decies G, LEGIARTI000044873806, VIGUEUR from 2022-01-01: read in part, dates, in DILA delta 20250727-211228 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20250727-211228.tar.gz | 2026-11-05 |
| CGI art. 44 sexies, LEGIARTI000051217272, VIGUEUR from 2025-02-16: read in part, I, in DILA delta 20260907-214720 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260907-214720.tar.gz | 2026-11-05 |
| CGI art. 44 sexies A, LEGIARTI000051217257, VIGUEUR from 2025-02-16: read in part, I, in DILA delta 20260907-214720 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260907-214720.tar.gz | 2026-11-05 |
| CGI art. 44 sexies-0 A, LEGIARTI000053543750, ABROGE_DIFF from 2026-02-21 to 2029-01-01: read in part, opening, version status, in DILA delta 20260813-212523 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260813-212523.tar.gz | 2026-11-05 |
| CGI art. 44 octies A, LEGIARTI000051217764, VIGUEUR from 2025-02-16: read in part, I, in DILA delta 20260907-214720 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260907-214720.tar.gz | 2026-11-05 |
| CGI art. 293 B, LEGIARTI000052488142, ABROGE_DIFF from 2025-03-01 to 2027-01-01: read in part, I, I bis and II, in DILA delta 20260929-213457 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260929-213457.tar.gz | 2026-11-05 |
| CGI art. 293 F, LEGIARTI000006304492, ABROGE_DIFF from 1999-03-31 to 2222-02-22: read in full, whole article, in DILA delta 20261104-214059 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261104-214059.tar.gz | 2026-11-05 |
| CGI art. 287, LEGIARTI000048826856, ABROGE_DIFF from 2025-01-01 to 2027-01-01: read in part, 3, 3 bis, 3 ter and the notes on ordonnance n° 2025-1247, in DILA delta 20261027-211214 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261027-211214.tar.gz | 2026-11-05 |
| CGI art. 269, LEGIARTI000044983827, ABROGE_DIFF from 2023-01-01 to 2222-02-22: read in part, 2 c and the notes on ordonnance n° 2025-1247, in DILA delta 20261104-214059 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261104-214059.tar.gz | 2026-11-05 |
| CGI art. 302 septies A, LEGIARTI000044873380, ABROGE_DIFF from 2022-01-01 to 2027-01-01: read in full, whole article, in DILA delta 20260803-212828 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260803-212828.tar.gz | 2026-11-05 |
| CIBS art. L. 162-1, LEGIARTI000044604097, ABROGE_DIFF from 2022-01-01 to 2027-01-01: read in full, whole article, in DILA delta 20261009-214339 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261009-214339.tar.gz | 2026-11-05 |
| CIBS art. L. 162-4, LEGIARTI000051216656, ABROGE_DIFF from 2025-03-01 to 2027-01-01: read in full, whole article, in DILA delta 20260731-221216 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260731-221216.tar.gz | 2026-11-05 |
| CIBS art. L. 162-5, LEGIARTI000051216648, ABROGE_DIFF from 2025-03-01 to 2027-01-01: read in full, whole article, in DILA delta 20260731-221216 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260731-221216.tar.gz | 2026-11-05 |
| CGI art. 1729, LEGIARTI000020051904, VIGUEUR from 2009-01-01: read in full, whole article, in DILA delta 20260702-223445 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260702-223445.tar.gz | 2026-11-05 |
| CGI art. 1727, LEGIARTI000051213330, ABROGE_DIFF from 2025-02-16 to 2027-01-01: read in part, III, in DILA delta 20260812-214541 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260812-214541.tar.gz | 2026-11-05 |
| CGI art. 205 A, LEGIARTI000037956839, VIGUEUR from 2019-01-01: read in full, whole article, in DILA delta 20260813-212523 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260813-212523.tar.gz | 2026-11-05 |
| LPF art. L. 64, LEGIARTI000037993642, VIGUEUR from 2019-01-01: read in full, whole article, in DILA delta 20260220-221620 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260220-221620.tar.gz | 2026-11-05 |
| LPF art. L. 64 B, LEGIARTI000037990417, VIGUEUR from 2020-01-01: read in full, whole article, in DILA delta 20260728-220005 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260728-220005.tar.gz | 2026-11-05 |
| CMF art. L. 224-4, LEGIARTI000054251191, VIGUEUR from 2026-06-14: read in full, whole article, in DILA delta 20261030-214909 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261030-214909.tar.gz | 2026-11-05 |
| CMF art. L. 224-20, LEGIARTI000038818332, VIGUEUR from 2019-10-01: read in full, whole article, in DILA delta 20261030-214909 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261030-214909.tar.gz | 2026-11-05 |
| Code de commerce art. L. 121-4, LEGIARTI000044056252, VIGUEUR from 2023-01-01: read in part, I, II, IV and IV bis, in DILA delta 20261005-214539 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261005-214539.tar.gz | 2026-11-05 |
| LF 2026 art. 9, LEGIARTI000053511619: read in full, whole article, in DILA delta 20261012-212534 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261012-212534.tar.gz | 2026-11-05 |
| LF 2026 art. 10, LEGIARTI000053511639: read in full, whole article, in DILA delta 20261012-212534 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261012-212534.tar.gz | 2026-11-05 |
| LF 2026 art. 17, LEGIARTI000053511653: read in part, I and the art. 244 quater M limb, in DILA delta 20261012-212534 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261012-212534.tar.gz | 2026-11-05 |
| LF 2026 art. 28, LEGIARTI000053511254: read in full, whole article, in DILA delta 20261012-212534 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20261012-212534.tar.gz | 2026-11-05 |
| LFSS 2026 art. 12, LEGIARTI000053265270: read in full, whole article, in DILA delta 20260629-223234 | https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260629-223234.tar.gz | 2026-11-05 |
| Brochure pratique IR 2026, part 4: read in part, part 4, filing dates in 2026 | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/04-declaration_revenus_64a73.pdf | 2026-11-05 |
| Brochure pratique IR 2026, part 6: read in part, part 6, table 5 and the frais réels car text | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/06-traitements_salaires_85a114.pdf | 2026-11-05 |
| Brochure pratique IR 2026, part 7: read in part, part 7, PER capital exits | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/07-pensions_115a120.pdf | 2026-11-05 |
| Brochure pratique IR 2026, part 11: read in part, part 11, micro limits for 2025 | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/11-revenus_non_salaries_161a182.pdf | 2026-11-05 |
| Brochure pratique IR 2026, part 12: read in part, part 12, PER limits and box 6QR | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/12-charges_ded_rev_225a236.pdf | 2026-11-05 |
| Service-Public F23267, micro tax regime: read in part, read for the versement libératoire test and option dates | https://entreprendre.service-public.gouv.fr/vosdroits/F23267 | 2026-11-05 |
| Service-Public F11677, ACRE: read in part, read for conditions, the 60 days, the 2-year control period, rate and PASS 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F11677 | 2026-11-05 |
| Urssaf, payment schedule: read in part, read for regularisation, in an archived capture of 10 April 2026 | https://web.archive.org/web/20260410154205id_/https://www.urssaf.fr/accueil/independant/comprendre-payer-cotisations/comprendre-echeancier-paiement.html | 2026-11-05 |
| Urssaf notice for the 2025 income declaration: read in part, read for Madelin and PER lines, in an archived capture of 19 May 2026 | https://web.archive.org/web/20260519203440id_/https://www.urssaf.fr/files/live/sites/urssaffr/files/outils-documentation/formulaires-modeles/Independant-Notice-revenus-2025.pdf | 2026-11-05 |
| BOFiP BOI-CF-IOR-30-20, L. 64 A: read in part, read for scope, the free choice and tax incentive statements, start dates, the rescrit, the comité and penalties | https://bofip.impots.gouv.fr/doctrine/pgp/12049-PGP | 2026-11-05 |
| BOFiP ACTU-2020-00018, L. 64 A: read in full, read for the art. 109 summary | https://bofip.impots.gouv.fr/bofip/12182-PGP.html/identifiant=ACTU-2020-00018 | 2026-11-05 |
| BOFiP BOI-CF-INF-10-20-20, penalties: read in part, read for art. 1729 | https://bofip.impots.gouv.fr/bofip/2592-PGP.html | 2026-11-05 |
| BOFiP BOI-BIC-CHG-20-30-10, low-value items: read in part, read for parts I and II | https://bofip.impots.gouv.fr/bofip/2109-PGP.html | 2026-11-05 |
| BOFiP BOI-BIC-AMT-20-20-20, dégressif goods: read in full, read for the 4 conditions | https://bofip.impots.gouv.fr/bofip/4684-PGP.html | 2026-11-05 |
| BOFiP BOI-BIC-AMT-20-20-20-30, dégressif calculation: read in part, read for new goods and the 3-year life | https://bofip.impots.gouv.fr/bofip/4750-PGP.html | 2026-11-05 |
| BOFiP BOI-BNC-BASE-40-60-60, meals: read in part, read for the 2026 meal amounts | https://bofip.impots.gouv.fr/bofip/4628-PGP.html | 2026-11-05 |
| BOFiP BOI-BNC-BASE-40-60-40-20, car costs: read in part, read for part II, the BNC option | https://bofip.impots.gouv.fr/doctrine/pgp/4634-PGP | 2026-11-05 |
| Assemblée nationale, PLF 2027 dossier: read in part, read for the stage reached | https://www.assemblee-nationale.fr/dyn/17/dossiers/plf_2027 | 2026-11-05 |
| Sénat, PLFSS 2027 dossier: read in part, read for the stage reached | https://www.senat.fr/dossier-legislatif/plfss2027.html | 2026-11-05 |

Not yet confirmed: any loi de finances for 2027 and any change it makes to art. 197 for income of 2026; filing dates for income of 2026; the mileage table for 2026 use; the first year the micro limits of 203,100 and 83,600 govern, and any overlap with 188,700 and 77,700; the indexed régime simplifié limits; TVA text after the recodification, covering the franchise, the régime simplifié and arts 269, 287 and 293 F, and the art. 15 table of ordonnance n° 2025-1247; LPF art. L. 64 A in its own words; CGI annexe II arts 22 and 23 for dégressif; the straight line start date; total social levies on capital income (the 18.6% in the earlier version; only CSG was read, and CRDS and the solidarity levy were not); whether the 5-year PER carry reaches limits left unused before LF 2026; the PASS year and profit measure for art. 154 bis; older PERP and Madelin contracts after 70; CGI art. 757 B; CSS art. L. 136-1-1 for SASU dividends; whether PER or Madelin payments can reduce the social base, which is inferred here; any extension of conjoint collaborateur status to a PACS partner; the CRDS text; and Senate action on PLF 2027 and PLFSS 2027.
