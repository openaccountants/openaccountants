---
name: fr-social-contributions
description: >
  French social contributions for 2026, centred on the self-employed (travailleurs
  indépendants) who pay URSSAF: the 2026 social security ceiling (PASS EUR 48,060),
  the reformed single base (gross income less costs, then a 26% allowance) first used
  for the 2025 regularisation, the 2026 rates for artisans, commerçants and liberal
  professions (Cipav and non-Cipav), minimum and maximum contributions, provisional
  calls and regularisation, the first two years, Acre (now a quarter exemption from
  2026), micro-entrepreneur rates on turnover (12.3%, 21.2%, 25.6%, 23.2%), CSG and
  CRDS on activity income and on capital income (10.6% CSG on most capital income: 2025 income assessed with income tax, and income taxed at source from 1 January 2026),
  payment dates and late surcharges, and a summary of salaried rates. Trigger on
  "cotisations URSSAF", "charges sociales indépendant", "micro-entrepreneur taux",
  "Acre", "CSG CRDS", "prélèvements sociaux", "Cipav", "régularisation URSSAF". Out of
  scope: payroll for employees and assimilés salariés (france-payroll), income tax
  (fr-income-tax, fr-personal-income-tax), CFE (fr-cfe), cross-border residence
  (fr-cross-border).
version: 2.2
jurisdiction: FR
tax_year: 2026
last_updated: 2026-10-27
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# France: social contributions (cotisations sociales, CSG and CRDS)

This skill covers the social contributions a French travailleur indépendant pays to URSSAF, the micro-entrepreneur regime, the CSG and CRDS on activity and capital income, and a short summary of the rates on salaries. Figures are for 2026. Every figure was read on 24 October 2026 on Légifrance (Code de la sécurité sociale, CSS) or on urssaf.fr, autoentrepreneur.urssaf.fr or service-public.gouv.fr, as the Sources table shows.

**Two documents can be live at once in 2026.** The base and the scales were rewritten by loi n° 2023-1250 of 26 December 2023, art. 18 (CSS L. 131-6, L. 136-3) and décret n° 2024-688 of 5 July 2024 (CSS D. 621-1 to D. 621-3). They apply to contributions for periods from 1 January 2025, so URSSAF first used them when it regularised the 2025 year after the income declaration of spring 2026. Provisional calls made early in 2026 can still sit on the old base. Always ask which echeancier a figure comes from.

**Three changes for 2026 itself.** Acre for business creations from 1 January 2026 is an exemption of a quarter of the covered contributions, not a full exemption (CSS L. 131-6-4 as amended by loi n° 2025-1403 of 30 December 2025, LFSS 2026, art. 23; D. 131-6-1). Micro-entrepreneur rates were reset from 1 January 2026 (CSS D. 613-4, décret n° 2025-943). The CSG on most capital income is 10.6%, so the total social levy on it is 18.6% (CSS L. 136-8 I 2°, as amended by LFSS 2026 art. 12). It applies to income assessed with income tax from the 2025 income year, and to income taxed at source (dividends, interest) from 1 January 2026.

## Who this applies to

- **Travailleurs indépendants on the real base (this skill, rate tables below):** a sole trader (entreprise individuelle), the majority manager or majority board of managers of a SARL (more than 50% of the shares held by the managers together), the manager of an EURL, SELARL or SELARLU, and every member of an SNC. URSSAF lists these statuses on its page on choosing a legal form.
- **Micro-entrepreneurs (auto-entrepreneurs):** pay a single rate on turnover collected, monthly or quarterly (CSS L. 613-7). None of the real-base tables apply to them.
- **Not in this skill:** employees and assimilés salariés (a minority or equal SARL manager, an SAS or SASU president or directeur général): see `france-payroll`. Praticiens et auxiliaires médicaux conventionnés, artistes-auteurs and marins have their own URSSAF pages. For a regulated liberal profession outside Cipav (avocats, médecins, experts-comptables and others), URSSAF collects the common part; the supplementary pension and invalidité-décès are set by the profession's CnavPL section. Mayotte has its own ceiling and scales.
- **Which caisse decides the rates:** artisan, commerçant and unregulated liberal profession use the general self-employed table; a regulated liberal profession attached to Cipav uses the Cipav table; other regulated liberal professions use the non-Cipav table for the common part.
- **Capital income levies** (CSG, CRDS, prélèvement de solidarité) apply to French tax residents (CSS L. 136-6, L. 136-7), and to non-residents on French property income (L. 136-6 I bis).

## Rates, bands and thresholds

All URSSAF figures are mainland France and overseas except Mayotte, 2026, unless the row says otherwise. URSSAF's rate pages print euro thresholds on the 2026 ceiling; the law sets each threshold as a share of the ceiling. For the 2025 regularisation use the 2025 ceiling, EUR 47,100.

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Annual social security ceiling (PASS) | EUR 48,060 (quarter 12,015; month 4,005) | 2026 | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/plafonds-securite-sociale.html |
| PASS, previous year | EUR 47,100 | 2025 | same page |
| PASS, Mayotte | EUR 36,264 (month 3,022) | 2026 | same page |
| Single base: allowance on gross income (CSS L. 136-3 III) | 26% | from 2025 income | https://www.urssaf.fr/accueil/independant/comprendre-payer-cotisations/reforme-cotisations-independants.html |
| Allowance floor and ceiling (CSS D. 136-5) | floor 1.76% PASS (EUR 846); ceiling 130% PASS (EUR 62,478) | 2026 | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000049888566 |
| Micro-fiscal business that is not an auto-entrepreneur: allowance replacing the 26% | 71% sales, 50% BIC services, 34% BNC; 30% unclassified furnished letting; 87% micro-BA (URSSAF 2026 declaration notice: "30% (location meublée non classée) ou 87% (BA)") | from 2025 income | same page |
| Maladie-maternité 1, full rate (CSS D. 621-1) | 8.5% up to 3 PASS; 6.5% on the part above | 2026 | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-ac-plnr.html |
| Maladie 1, reduced rate below 3 PASS (CSS D. 621-2) | 0% below 20% PASS (EUR 9,612); rises linearly 0 to 1.5% (20-40%), 1.5 to 4% (40-60%), 4 to 6.5% (60-110%), 6.5 to 7.7% (110-200%), 7.7 to 8.5% (200-300%) | 2026 | same page |
| Maladie 2, daily benefits: artisan, commerçant, unregulated liberal (D. 621-3) | 0.50% up to 5 PASS (EUR 240,300); minimum base 40% PASS | 2026 | same page |
| Maladie 2, regulated liberal profession (D. 621-3) | 0.30% up to 3 PASS (EUR 144,180); minimum base 40% PASS | 2026 | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-plr-cipav.html |
| Retraite de base, artisan, commerçant, unregulated liberal | 17.87% up to 1 PASS; 0.72% on the part above | 2026 | ac-plnr page |
| Retraite complémentaire, same group | 8.10% up to 1 PASS; 9.10% from 1 to 4 PASS (EUR 192,240) | 2026 | ac-plnr page |
| Invalidité-décès, same group | 1.30% up to 1 PASS | 2026 | ac-plnr page |
| Retraite de base, Cipav and CnavPL | 8.73% up to 1 PASS plus 1.87% up to 5 PASS | 2026 | Cipav page; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-plr-hors-cipav.html |
| Retraite complémentaire, Cipav | 11% up to 1 PASS; 21% from 1 to 4 PASS | 2026 | Cipav page |
| Invalidité-décès, Cipav | 0.50% up to 1.85 PASS (EUR 88,911) | 2026 | Cipav page |
| Allocations familiales (CSS D. 613-1) | 0% up to 110% PASS (EUR 52,866); rising rate 110-140%; 3.10% above 140% (EUR 67,284) | 2026 | ac-plnr page |
| CSG and CRDS on activity income | 9.70% (CSG 9.20% + CRDS 0.50%) | 2026 | https://www.urssaf.fr/accueil/independant/comprendre-payer-cotisations/vos-cotisations.html |
| CSG and CRDS on replacement income of a travailleur indépendant | 6.70% | 2026 | ac-plnr page ("Revenus de remplacement 6,70 %") |
| Training levy (CFP), on 1 PASS | 0.25% commerçant and liberal (EUR 120); 0.29% artisan (EUR 139); 0.34% with conjoint collaborateur (EUR 163) | 2026, paid November 2026 | ac-plnr page |
| Minimum contributions, general group | daily benefits EUR 96 (base EUR 19,224); retraite de base EUR 967 (base EUR 5,409, 450 hourly Smic); invalidité-décès EUR 72 (base EUR 5,527, 11.5% PASS) | 2026 | ac-plnr page |
| Minimum contributions, Cipav | daily benefits EUR 58; retraite de base EUR 573 (base EUR 5,409); invalidité-décès EUR 89 (base EUR 17,782, 37% PASS) | 2026 | Cipav page |
| Minimum contributions, non-Cipav regulated | daily benefits EUR 58; retraite de base CnavPL EUR 573; 4 quarters need income of 600 hourly Smic (EUR 7,212) | 2026 | hors-Cipav page |
| Maximum contributions, general group (as URSSAF prints them) | daily benefits EUR 1,202; retraite complémentaire EUR 17,494; invalidité-décès EUR 625 | 2026 | ac-plnr page |
| Maximum contributions, Cipav | daily benefits EUR 433; retraite de base EUR 8,690; retraite complémentaire EUR 35,565; invalidité-décès EUR 445 | 2026 | Cipav page |
| First and second year flat base | 19% PASS: EUR 9,131 in 2026 | 2026 | ac-plnr page; CSS L. 131-6-2 |
| First year 2026 without Acre, general group, training levy excluded | EUR 3,473 | 2026 | ac-plnr page |
| First year 2026, Cipav: supplementary pension on the flat base (never exempted by Acre) | EUR 9,131 at 11% = EUR 1,004 | 2026 | Cipav page ("Taux 11 % ... Montant annuel 1 004 €") |
| Overseas (not Mayotte): maladie 1, fixed rate | 8.50% up to EUR 144,180 (3 PASS); 6.50% above | 2026 | ac-plnr page |
| Overseas (not Mayotte): allocations familiales, fixed | 3.10% on the whole income | 2026 | ac-plnr page |
| Overseas start-up exemption (24 months), by income | income EUR 52,866 to 72,090 (110-150% PASS): exemption worth 110% PASS; EUR 72,090 to 120,150 (150-250% PASS): tapering; above EUR 120,150: none | 2026 | ac-plnr page |
| Overseas, 3rd year / 4th year onward, income below EUR 72,090 | allowance of 75% / 50% of income, capped at 1 PASS | 2026 | ac-plnr page |
| Acre, base at or below 75% PASS (EUR 36,045) (CSS L. 131-6-4, D. 131-6-1) | exemption of one quarter of maladie, daily benefits, family, retraite de base and invalidité-décès contributions, 12 months | creations from 1 Jan 2026 | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006073189 |
| Acre, base between 75% PASS and 1 PASS | exemption = 0.25 x E / (0.25 x PASS) x (PASS - income), E = those contributions at 75% PASS; nil at 1 PASS | creations from 1 Jan 2026 | same |
| Micro-entrepreneur global rate (CSS D. 613-4) | sales BIC 12.3%; BIC services 21.2%; BNC (SSI) 25.6%; Cipav 23.2%; classified tourist lettings 6% | from 1 Jan 2026 | https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/lessentiel-du-statut.html |
| Micro-entrepreneur Acre rate, start up to 30 June 2026 | 6.2%; 10.6%; 12.8%; Cipav 13.4%; tourist lettings 3% (Cipav 3.5%) | 2026 | same page |
| Micro-entrepreneur Acre rate, start from 1 July 2026 | 9.3%; 15.9%; 19.2%; Cipav 17.4%; tourist lettings 4.5% | 2026 | same page |
| Micro-entrepreneur training levy | artisan 0.3%; commerçant 0.1%; liberal 0.2% of turnover | 2026 | same page |
| Micro-entrepreneur turnover ceilings | EUR 188,700 sales; EUR 77,700 services | 2026 | same page |
| CSG on capital income (CSS L. 136-8 I 2°) | 10.6% (total with CRDS 0.5% and solidarity levy 7.5%: 18.6%) | income assessed with income tax from 2025 income; income taxed at source from 1 Jan 2026 | https://www.service-public.gouv.fr/particuliers/vosdroits/F2329 |
| CSG on property income, property gains, life insurance, PEL, CEL (L. 136-8 IV) | 9.2% (total 17.2%) | 2026 | same page |
| Deductible part of capital-income CSG (progressive scale only) | 6.8% | 2026 | same page |
| Capital income of a resident insured in another EEA state or Switzerland | 7.5% solidarity levy only | 2026 | same page; CSS L. 136-6 I ter |
| Late payment surcharge (CSS R. 243-16) | 5% plus 0.2% per month or part month | 2026 | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006073189 |
| Salaried staff, employer (summary) | maladie 7% or 13%; vieillesse 8.55% capped + 2.11%; family 3.45% or 5.25%; unemployment 4.00% up to EUR 192,240; AGS 0.25% | 2026 | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html |
| Salaried staff, employee (summary) | vieillesse 6.90% capped + 0.40%; CSG 9.20% (6.80% deductible, 2.40% not) and CRDS 0.50% on 98.25% of gross pay | 2026 | same page |

## The taxable base

**Real-base self-employed: the single base (CSS L. 131-6, L. 136-3).**

1. **Gross income, business taxed to income tax:** BIC profit (produits less charges, excluding long-term gains and losses) or BNC receipts less expenses, without deducting the social contributions or the deductible CSG. The special CGI deductions listed in CSS R. 136-1 (for example art. 39 AB, 39 decies) are added back. Tax exemptions are not deducted socially: the 2026 URSSAF declaration notice says so in terms.
2. **Gross income, business taxed to corporation tax:** the manager's pay and benefits in kind or cash, plus the part of dividends and associate current account interest received by the manager, spouse or PACS partner and minor children that exceeds 10% of their capital, share premiums and current account balances. Capital and share premiums are taken on the last day of the financial year before the distribution; the current account at its annual average balance (sum of the monthly average balances divided by the number of months) (URSSAF 2026 declaration notice: "apprécié au dernier jour de l'exercice précédant la distribution des revenus"; "le solde moyen annuel"). For an entreprise individuelle taxed to IS the reference is 10% of net profit, or the affected assets if higher.
3. **Apply the allowance:** 26% of gross income (L. 136-3 III), never less than 1.76% PASS (EUR 846 in 2026) and never more than 130% PASS (EUR 62,478 in 2026) (CSS D. 136-5). The ceiling bites from gross income of EUR 240,300. A micro-fiscal business that is not an auto-entrepreneur uses its tax allowance (71%, 50% or 34%) instead.
4. **The same base serves every contribution and the CSG and CRDS.** Before the reform the CSG base added back the contributions; it no longer does. URSSAF says the overall levy is unchanged: CSG and CRDS fall, pension rises. The URSSAF page "Quelles sont vos cotisations", updated 5 October 2026, still describes the old CSG base. The statute (L. 136-3) wins.

**Applying the rates.**

- **Maladie 1 below 3 PASS is one rate on the whole base**, found by linear interpolation inside the band (D. 621-2). Example, band 60% to 110%: rate = 4% + 2.5% x (base - 0.6 PASS) / (0.5 PASS). From 3 PASS the base rate is 8.5% on the part up to 3 PASS and 6.5% above (D. 621-1).
- **Allocations familiales between 110% and 140% PASS** use rate = 3.10% x (base - 1.1 PASS) / (0.3 PASS) on the whole base (D. 613-1). This scale applies to every travailleur indépendant. The 5 October 2026 URSSAF page says a regulated liberal profession pays 3.10% on all income; the decree and the three URSSAF rate pages say the scale. Follow the decree.
- **Pension and invalidity lines are banded** at 1, 1.85, 4 and 5 PASS as the table shows. URSSAF's printed maximum supplementary pension for the general group (EUR 17,494) equals 9.10% on four PASS, which does not match its own two-band rates (8.10% on one PASS plus 9.10% on the next three gives EUR 17,013). Quote the page's figure, do not recompute a maximum, and take the amount due from the echeancier.
- **Minimums:** the daily benefit, retraite de base and invalidité-décès lines have a minimum base when income is low or negative, even for someone also employed or retired. They do not apply to a client on the RSA or the prime d'activité, who pays on real income unless they ask otherwise. Maladie 1, family, CSG-CRDS and supplementary pension have no minimum. URSSAF prints each minimum separately; do not add them into a single total. The minimum retraite de base validates three quarters of pension.
- **No employer half:** the self-employed person bears every line. There is no unemployment contribution on this list.

**Provisional and regularisation calls (CSS L. 131-6-2).** Contributions are annual. During year N they are called provisionally on the base of year N-2. Once the N-1 income is declared, the N-1 contributions are regularised and the N provisional calls are recalculated on N-1. On request, provisional calls can be based on an estimate of the current year. If no income is declared, URSSAF assesses under CSS L. 242-12-1.

**First years.** For the first two years provisional contributions use the flat base of 19% PASS (EUR 9,131 in 2026), prorated for a part year except the training levy; the second year uses 19% of the 2027 PASS. The first year is regularised on real income: URSSAF warns that a top-up can follow in 2027. The overseas departments have a 24-month start-up exemption and then a 75% (third year) and 50% (fourth year onward) allowance on income below 150% PASS; that regime is outside the tables above.

**Acre (CSS L. 131-6-4, D. 131-6-1), creations from 1 January 2026.** Twelve months from affiliation. Base at or below 75% PASS: one quarter of the maladie, daily benefit, family, retraite de base and invalidité-décès contributions is exempt. Between 75% PASS and one PASS the exemption tapers by the formula in the table and reaches nil at one PASS. CSG-CRDS, supplementary pension and the training levy are never exempt. Request it within 60 days of the start date on the guichet unique proof. No second Acre within three years of the last one, and no stacking with other reductions except those the article names.

**Micro-entrepreneurs (CSS L. 613-7, D. 613-4).** Contribution = turnover collected in the month or quarter x the global rate, plus the training levy. No turnover means nothing to pay. The amounts are final and never regularised. The Acre rate runs to the end of the third calendar quarter after the quarter of registration, and the column is chosen by the start date (before or from 1 July 2026). For Cipav micro-entrepreneurs the Acre rate is raised to the floor of CSG-CRDS plus supplementary pension (L. 613-7). A micro-entrepreneur can opt to pay the minimum contributions; the request is due by 31 December of the prior year, or by the end of the third month after creation. From 2026 URSSAF splits a BNC payment as 2.60% maladie, 1.50% daily benefits, 3.30% invalidité-décès, 46.40% retraite de base, 21.00% supplementary pension and 25.20% CSG-CRDS.

**CSG and CRDS on capital income.** Residents pay on property income, investment income and gains (CSS L. 136-6, L. 136-7) at 18.6% in total for most income (from the 2025 income year where assessed with income tax; from 1 January 2026 where taxed at source), and 17.2% for property income, property gains, life insurance, PEL and CEL (L. 136-8 IV). Livret A, LDD, LEP and livret jeune interest are exempt. Investment income suffers the levy at source; property income and gains are assessed with income tax. 6.8% of the CSG is deductible only when the taxpayer opts for the progressive scale.

**Deductibility for income tax.** Compulsory contributions paid are deductible from professional income (CGI art. 154 bis) in the year paid. The deductible part of the self-employed CSG comes from the attestation de versement URSSAF sends each year; the CRDS is not deductible. Deduct what was actually paid, after Acre.

## Deadlines and filing

| What | When | Where |
|---|---|---|
| Income declaration for social and tax purposes (déclaration des revenus des indépendants) | between April and June each year, with the income tax return | impots.gouv.fr |
| Monthly payment | 12 debits January to December, on the 5th or the 20th | URSSAF online account |
| Quarterly payment | 5 February, 5 May, 5 August, 5 November | URSSAF online account |
| Training levy (real base) | called once, with the November instalment; calculated finally, not regularised | URSSAF |
| First payments of a new business | no sooner than 90 days after the start | URSSAF |
| Cessation | balance within 30 days of the avis d'appel; deferred or spread amounts within 60 days | URSSAF |
| Change between monthly and quarterly | any time, once per calendar year | online account |
| Micro-entrepreneur | turnover and contributions declared monthly or quarterly | autoentrepreneur.urssaf.fr |
| Acre request | within 60 days of the start date | URSSAF |

After the income declaration URSSAF publishes a new echeancier with the regularisation of the closed year, the recalculated provisional calls for the current year and, for information, the first calls of the next year. An overpayment can be refunded.

A regulated liberal profession can ask, within 30 days of affiliation and before any payment, to defer the first 12 months of contributions, and then spread the first year over up to five years. An Acre beneficiary can ask to defer the training levy and to defer then spread the CSG-CRDS and supplementary pension.

**Reading the payments on a bank statement.** "URSSAF" or "URSSAF [region]" with PRELEVEMENT, COTISATIONS, ACOMPTE or REGULARISATION is a contribution debit; a larger November debit usually carries the training levy. "CIPAV" is a regulated liberal pension debit. CNBF, CARMF, CARPIMKO, CNPADC and IRCEC are other caisses: escalate. DGFIP, IMPOT or PRELEVEMENT A LA SOURCE is income tax, not a social contribution; TVA is VAT. A bank line cannot split the contributions; ask for the echeancier.

## Penalties and interest

- **Late payment of contributions collected by URSSAF:** a surcharge of 5% of the contributions not paid by the due date, plus 0.2% of the contributions due per month or part month from the due date (CSS R. 243-16). URSSAF's calendar page warns that missed quarterly dates trigger surcharges.
- **No income declared:** URSSAF assesses the contributions under CSS L. 242-12-1 (L. 131-6-2).
- **Capital-income CSG assessed with income tax:** collected like income tax; the 10% surcharge of CGI art. 1730 applies to amounts unpaid 45 days after the assessment (CSS L. 136-6 III).
- **Trading without registration:** contributions are claimed back with surcharges. Escalate to an expert-comptable.
- **Payment difficulties:** ask URSSAF for a payment plan before the due date, online or on 3698.

## Cross-border points

- **Which country's scheme applies** is decided by EU Regulation 883/2004 or a bilateral agreement, not by this skill. A person working in France on a posting with an A1 certificate stays in the home scheme. Escalate every A1, posting or multi-state case.
- **Capital-income levies:** a French resident who is insured in another EEA state or Switzerland, and not charged to a French scheme, pays only the 7.5% solidarity levy, not CSG or CRDS (CSS L. 136-6 I ter; service-public F2329).
- **Non-residents** pay the levies on French property income and property gains (L. 136-6 I bis). See `fr-cross-border` and `leaving-france-exit-tax` (exit-tax gains are within L. 136-6 I e bis).
- **Overseas departments** have their own fixed health and family rates and start-up exemptions; Mayotte has its own ceiling.

## Worked examples

**Example 1. Commerçant on the real base, 2026 income EUR 60,000 before contributions.** A sole trader taxed to income tax, mainland, in the fourth year of trading, no Acre, no conjoint collaborateur. The allowance is 15,600, inside the floor and ceiling, so the single base is 60,000 x 0.74 = 44,400. That is between 60% PASS (28,836) and 110% PASS (52,866), so maladie 1 is one rate on the whole base: 4% + 2.5% x (44,400 - 28,836) / 24,030 = 5.6192%, giving EUR 2,494.94. Daily benefits 0.5% = 222.00. The base is below one PASS, so retraite de base is 17.87% = 7,934.28 with nothing in the uncapped band, supplementary pension 8.10% = 3,596.40 and invalidité-décès 1.30% = 577.20. Family allowances are nil below 110% PASS. CSG-CRDS 9.70% = 4,306.80. The commerçant training levy is 0.25% of one PASS, 120.15 (URSSAF rounds to EUR 120). Definitive 2026 contributions: EUR 19,251.77. They are regularised in 2027 against the provisional calls made in 2026 on the 2024 base.

```oa-check
name: Commerçant 2026, gross income EUR 60,000, single base and 2026 rates
inputs:
  gross_income: 60000
  ceiling: 48060
steps:
  - base: gross_income * 0.74
  - maladie_rate: 0.04 + 0.025 * (base - 0.6 * ceiling) / (0.5 * ceiling)
  - maladie_1: round(base * maladie_rate, 2)
  - daily_benefits: base * 0.005
  - retraite_base: min(base, ceiling) * 0.1787 + max(base - ceiling, 0) * 0.0072
  - retraite_compl: min(base, ceiling) * 0.081 + max(min(base, 4 * ceiling) - ceiling, 0) * 0.091
  - invalidite_deces: min(base, ceiling) * 0.013
  - allocations_familiales: 0
  - csg_crds: base * 0.097
  - cfp: round(ceiling * 0.0025, 2)
  - total: maladie_1 + daily_benefits + retraite_base + retraite_compl + invalidite_deces + allocations_familiales + csg_crds + cfp
expected:
  base: 44400.00
  maladie_1: 2494.94
  retraite_base: 7934.28
  csg_crds: 4306.80
  total: 19251.77
```

**Example 2. Micro-entrepreneur in BNC services, started 15 May 2026 with Acre, plus dividends.** A consultant not attached to Cipav registers on 15 May 2026 and gets Acre. The start is before 1 July 2026, so the Acre rate is 12.8%, and it runs to the end of the third calendar quarter after the second quarter of 2026, that is 31 March 2027. All 2026 turnover is therefore at 12.8%. Turnover collected in 2026: EUR 30,000. Contributions 30,000 x 12.8% = 3,840. Training levy for a liberal profession 0.2% = 60. The client also received EUR 2,000 of dividends in 2026: the paying bank withholds social levies of 18.6% (CSG 10.6%, CRDS 0.5%, solidarity 7.5%), EUR 372. The edge: the same EUR 30,000 collected after the Acre period costs 25.6%, EUR 7,680, so the client should budget for the rate doubling from April 2027.

```oa-check
name: Micro-entrepreneur BNC 2026 with Acre (start before 1 July 2026) and dividends
inputs:
  turnover: 30000
  dividends: 2000
steps:
  - contributions_acre: turnover * 0.128
  - training_levy: turnover * 0.002
  - total_urssaf: contributions_acre + training_levy
  - levies_on_dividends: dividends * (0.106 + 0.005 + 0.075)
  - same_turnover_full_rate: turnover * 0.256
expected:
  contributions_acre: 3840.00
  total_urssaf: 3900.00
  levies_on_dividends: 372.00
  same_turnover_full_rate: 7680.00
```

## Ask the client first

- **Legal form and, for a SARL, the share held by all the managers together.** Above 50% the manager is in this skill; at 50% or below, or as an SAS or SASU president, the manager is on payroll (`france-payroll`).
- **Micro-entrepreneur or real base, which activity (sales, BIC services, BNC) and which caisse (general, Cipav, another CnavPL section).** This picks the rate table or the global rate.
- **Business start date, and whether Acre was granted and when.** The first two years use the flat base; Acre and the micro Acre column depend on the start date.
- **For a company taxed to IS: capital, share premiums, current account balances and dividends paid to the manager's household.** They set the dividend share added to the base.
- **Is the client on the RSA or the prime d'activité, or also employed or retired?** The first switches off the minimum contributions; the second does not.
- **Which document a figure comes from (provisional echeancier, regularised echeancier, avis) and for which year.** In 2026 the old and the reformed base can both appear.
- **Did the client's profession leave Cipav under the 2018 reform, or did the client exercise an option?** The pension rates then depend on the registration date and the option: escalate.
- **For co-managers near half the shares, or holdings that changed during the year:** get the share register with dates. Crossing 50% moves the manager between this skill and payroll.

Defaults while waiting: activity type or caisse unknown, do not compute; income unknown, apply the minimum bases; Acre unconfirmed in writing, no Acre; mainland or overseas unknown, ask; client both employed and self-employed, both sets of contributions apply and flag how the capped pension bands interact.

## Sources

| Source | URL | Read on |
|---|---|---|
| Code de la sécurité sociale, L. 131-6, L. 131-6-2, L. 131-6-4, L. 136-3, L. 136-6, L. 136-8, L. 613-7 (Légifrance, versions in force 24 Oct 2026) | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006073189 | 2026-10-24 |
| Code de la sécurité sociale, D. 131-6-1, D. 613-1, D. 613-4, D. 621-1, D. 621-2, D. 621-3, R. 136-1, R. 243-16 (Légifrance) | https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006073189 | 2026-10-24 |
| Décret n° 2024-688 of 5 July 2024 (CSS D. 136-5, D. 621-1 to D. 621-3) | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000049888566 | 2026-10-26 |
| CSS L. 136-8, version in force 31 Dec 2025 to 27 Jun 2026, with the application note of LFSS 2026 art. 12 II | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053278668/2026-05-26 | 2026-10-26 |
| Loi n° 2025-1403 of 30 December 2025 (LFSS 2026), art. 12 (capital-income CSG) and art. 23 (Acre) | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000053226384/ | 2026-10-24 |
| URSSAF, plafonds de la Sécurité sociale (updated 1 Jan 2026) | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/plafonds-securite-sociale.html | 2026-10-24 |
| URSSAF, taux artisan, commerçant, profession libérale non réglementée (updated 27 Feb 2026) | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-ac-plnr.html | 2026-10-24 |
| URSSAF, taux profession libérale réglementée Cipav (updated 27 Feb 2026) | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-plr-cipav.html | 2026-10-24 |
| URSSAF, taux profession libérale réglementée hors Cipav (updated 27 Feb 2026) | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-plr-hors-cipav.html | 2026-10-24 |
| URSSAF, réforme de l'assiette sociale (updated 7 May 2026) | https://www.urssaf.fr/accueil/independant/comprendre-payer-cotisations/reforme-cotisations-independants.html | 2026-10-24 |
| URSSAF, quelles sont vos cotisations (updated 5 Oct 2026) | https://www.urssaf.fr/accueil/independant/comprendre-payer-cotisations/vos-cotisations.html | 2026-10-24 |
| URSSAF, calendrier de paiement des indépendants | https://www.urssaf.fr/accueil/independant/comprendre-payer-cotisations/calendrier-paiement-cotisations.html | 2026-10-24 |
| URSSAF, déclaration des revenus 2026 des indépendants, notice | https://www.urssaf.fr/files/live/sites/urssaffr/files/outils-documentation/formulaires-modeles/independant-notice-revenus-2026.pdf | 2026-10-24 |
| URSSAF, choisir votre statut juridique | https://www.urssaf.fr/accueil/choisir-forme-juridique/creer-societe.html | 2026-10-24 |
| URSSAF, taux de cotisations secteur privé (updated 1 Jan 2026) | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html | 2026-10-24 |
| URSSAF auto-entrepreneur, l'essentiel du statut | https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/lessentiel-du-statut.html | 2026-10-24 |
| Service-public, prélèvements sociaux sur les revenus du patrimoine et de placements (checked 30 June 2026) | https://www.service-public.gouv.fr/particuliers/vosdroits/F2329 | 2026-10-24 |

Not yet confirmed: the decree article fixing the micro-entrepreneur Acre rates and the 1 July 2026 change (rates taken from the URSSAF auto-entrepreneur page only); the Cipav and non-Cipav overseas rates; the supplementary pension and invalidité-décès rates of the CnavPL sections other than Cipav; the 2027 PASS for second-year flat bases; the Mayotte scales.

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
