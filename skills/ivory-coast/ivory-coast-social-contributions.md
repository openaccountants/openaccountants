---
name: ivory-coast-social-contributions
description: >
  Use this Côte d'Ivoire (Ivory Coast) reference for CNPS contributions and CMU
  in 2026, for employers, salaried employees and travailleurs indépendants
  (RSTI). Match requests such as CNPS contributions, cotisations sociales Côte
  d'Ivoire, Ivory Coast social security, retraite CNPS, prestations familiales,
  accident du travail rate, CMU contribution, how much CNPS do I pay, employer
  social charges Ivory Coast, assiette plafonnée, plafond CNPS, a DISA/DASC
  annual declaration, an appel de cotisations, and CNPS débits on SGCI, BICICI,
  Ecobank, NSIA or Coris statements. It ties each rate to its text, holds the
  ceiling decrees and sends ITS, FDFP and other payroll taxes to
  ivory-coast-payroll. Read it before any CNPS-related work. This Tier 2 draft
  supports source checking and reviewer questions; it does not authorise
  filing, payment or a tax position.
version: 0.5
jurisdiction: CI
tax_year: 2026
tax_year_notes: "Calendar 2026. Statutory rates are as read in the Code de Prévoyance Sociale, Ordonnance 2012-03 (unofficial copy), the RSTI texts and Décret 2017-123. The ceilings and the floor from 1 January 2023 (retirement 3,375,000, other branches 75,000, floor 75,000 a month) are as stated in the CNPS Direction Générale communiqué of January 2023, read on 14 November 2026; the decrees behind them were not read. The ordonnance adopted on 23 September 2026 amending the Code was not read."
last_updated: 2026-11-14
type: computation
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: payroll
---

# Côte d'Ivoire (Ivory Coast) Social Contributions (CNPS) v0.5

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

This reference covers contributions to the Caisse Nationale de Prévoyance Sociale (CNPS, www.cnps.ci, portal https://e.cnps.ci/) by employers and salaried workers, the Régime Social des Travailleurs Indépendants (RSTI) and its complementary regime, and the Couverture Maladie Universelle (CMU) contribution owed to the Caisse Nationale d'Assurance Maladie (IPS-CNAM). Amounts are in West African CFA francs (XOF, FCFA), XOF only. Tax year: calendar 2026.

Impôt sur les Traitements et Salaires (ITS), the employer contribution under the tax code and the Fonds de Développement de la Formation Professionnelle (FDFP) are taxes or levies paid to other bodies, not social contributions. They appear here only so that they are not confused with CNPS: `ivory-coast-payroll` owns them.

| Person | Position | Basis and limit |
| --- | --- | --- |
| Employer | Every employer of salaried workers as defined in Code du Travail art 2 is compulsorily affiliated, from the first hire | Code Art 5. Code du Travail art 2 was not read, so who is a worker at the margin is R-CI-CNPS-7 |
| Domestic employer (gens de maison) | An employer. The registration file omits the commerce register and fiscal documents | CNPS leaflet, edition 2021, administrative |
| Salaried worker | All 3 branches, and CMU. The worker's share is deducted at each pay and the worker cannot object | Code Art 21; CNPS Employeur page |
| Occasional worker (hourly, daily, seasonal, fixed term) | Same rules as other workers. The employer agrees the practical declaration with its CNPS agency | CNPS Employeur page and leaflet, edition 2021, administrative |
| Apprentice | Notional base: half the SMIG with an apprenticeship contract, the SMIG without one | CNPS page and leaflets, administrative. Code Art 67 4° names apprentices for work-injury cover. Whether all branches or only AT/MP apply is Needs Input |
| Members of workers' production cooperatives and non-salaried cooperative managers with their staff (préposés); PDG and DG of an SA; pupils of technical education and people in training or rehabilitation centres; prisoners doing penal work | AT/MP only, on the salary in Art 16 | Code Art 67, which limits pupils, trainees and prisoners to accidents in that teaching, training or work and leaves some conditions to decrees not read. The AT/MP-only limit comes from the CNPS Employeur page, not Art 67, and which categories its 'citées ci-dessus' reaches depends on a screen layout: this list is an inference from the page. A person who is also a salaried worker is Needs Input |
| Gérant of a SARL | Same AT/MP treatment only where all 3 limbs hold: the statutes appoint for a limited term, even if renewable; powers are subject to general-meeting authorisation for certain acts; and the gérants together hold no more than half the capital. Shares of a gérant's ascendants, spouse and minor children count as that gérant's | Code Art 67 2°. If a limb fails, Needs Input |
| Self-employed (travailleur indépendant) | Compulsory RSTI: anyone with a professional activity yielding income, on their own account or as a non-salaried mandataire. Ministers of religion and religious are assimilated | Ordonnance 2019-636 Arts 2, 6. Affiliate within 1 month of becoming subject; CNPS can affiliate of its own motion (Art 7) |
| Ivorian working abroad | Voluntary affiliation to the RSTI retirement branch, only where the country has signed no social security convention with Côte d'Ivoire. Complementary regime compulsory above the ceiling | Ordonnance 2019-636 Art 9; Arrêté 2020-065 Art 7 |
| Other voluntary members | Code Art 6 allows voluntary adherence and Art 70 voluntary work-injury cover at the person's own cost, each on a decree | Decrees not read. No rate is stated here. Ordonnance 2019-636 Arts 30 to 32 gave earlier voluntary members a 1-year option that now sends a non-opting self-employed person to RSTI |
| Civil servants and State agents | Outside this file: R-CI-CNPS-5 | IPS-CGRAE. CMU for them runs under Décret 2017-123 Arts 14 to 17 |

### What this file is

This is a Tier 2 source-cited draft. It has no accountant sign-off, and no accountant has reviewed this version. Treat every working it produces as a working paper only: label it estimated and direct the client to their CNPS appel de cotisations. The appel and the CNPS statement settle what a client pays.

The law is read in 5 layers, and a figure is only as strong as its layer. Enacted text: the Code, Ordonnance 2019-636, Décret 2020-308, Arrêté 2020-065, Décret 2017-123 and Loi 2014-131. Unofficial copy of enacted text: Ordonnance 2012-03. CNPS board decision: Délibération 004. Official announcement, not the text announced: the Conseil des ministres communiqués, which carry the SMIG and the 2026 reform. Administrative statement: the CNPS communiqué of January 2023, which gives the ceilings and floor from 1 January 2023, and the CNPS page and leaflets, which give the periodicity, the 31 March date and the daily majoration, because the decrees that Code Arts 21, 23 and 24 call for were not found. The CNPS page is partly stale: it still prints a SMIG of 60,000, a retirement ceiling of 1,647,315 and an other-branch ceiling of 70,000, all superseded by the communiqué.

The Code and several decrees are scans read through local OCR, which is not qualified for French. Checked by eye on the page image: Code Arts 4 to 37, 71, 164, 166 and 167; Arrêté 2020-065 Arts 4 to 9; Délibération 004 Arts 2 to 7; all of Décret 2017-123; and Loi 2014-131 Arts 58 to 72. So no CMU figure rests on OCR alone. Every other article rests on OCR or a text layer, including Code Arts 66, 67, 70 and 174 and all of Ordonnance 2019-636. CivLII item pages returned 404. cotedivoire.eregulations.org, fratmat.info, issa.int, dg-cmu.ci, africa-laws.org and comptrasec.fr refused the request with a 403, and juriafrica.com reset the connection. No archive copy was used. What depended on those sources is held below.

**Status against `social-contributions-workflow-base` Section 6.** Slots filled: 1 (programmes and rates), 4 (categories), 5 (registration), 9 (patterns, as conditioned), 10 (refusals and defaults), 12 (examples). Partly filled: 2 (the hourly SMIG and the transport figure are held), 3 (ceilings rest on administrative statements; pro-ration and multiple employment are held), 6 (the CMU date for a quarterly payer is held), 7 (the Art 29 fine, moratory interest and RSTI penalties are held), 8 (held to the owning guides), 11 (no rounding rule read). Optional slots: 13 voluntary and 14 cross-border are partly filled; 15 sector schemes: none read; 16 benefits: only as they bear on contributions; 17: `ivory-coast-payroll` owns the payslip. A figure resting on a partly filled slot is Needs Input.

### Refusals and boundaries

A refusal is a full stop: give the message and classify nothing further on that point.

- **R-CI-CNPS-1, wrong scheme.** Trigger: a request to apply régime général rates to a self-employed person's own income, or RSTI rates to a salaried worker. Message: 'These are separate regimes. RSTI uses a declared income, a category floor from XOF 30,000 to 150,000, a XOF 180,000 ceiling, 12% (9% retirement and 3% other risks) and 9% complementary above the ceiling. I will not mix them. Give me the worker's status, then I can use the right one.'
- **R-CI-CNPS-2, outdated ceiling.** Trigger: a request to use a retirement ceiling of XOF 1,647,315 or 2,700,000 for a period from 1 January 2023, without a CNPS document for that period. Message: 'Those figures are 45 times an older SMIG: 36,607 and 60,000. CNPS states the ceiling as 45 times the SMIG, and its communiqué of January 2023 sets the retirement ceiling at 3,375,000 a month from 1 January 2023. I will use 3,375,000 for a period from that date, and I will not apply either older figure without a CNPS document for the period.'
- **R-CI-CNPS-3, arrears.** Trigger: the client has unpaid contributions and wants an amount for arrears or penalties. Message: 'Do not estimate arrears without the official CNPS statement. The Code separates the 10% penalty for a missing declaration from late-payment majorations, and CMU has its own rate. Get the CNPS statement and escalate to a warranted accountant. I can show the arithmetic of a stated amount and period only.'
- **R-CI-CNPS-4, AT/MP rate.** Trigger: a request to assign the work-injury rate or category. Message: 'The AT/MP rate runs from 2% to 5% by the risk of the employer's activity, and CNPS notifies it with the matricule. It cannot be self-assigned, and the risk arrêté was not read here. Send the CNPS notification.'
- **R-CI-CNPS-5, public sector.** Trigger: the worker is a civil servant or State agent. Message: 'This file does not cover IPS-CGRAE. Escalate to a warranted accountant.' A contract employee of a State body is Needs Input, not this refusal.
- **R-CI-CNPS-6, pay unknown.** Trigger: for a salaried worker, gross pay by component or the period is missing. Message: 'For a salaried worker, gross pay by component and the period are mandatory. I cannot compute that worker's CNPS contributions without them.' It does not apply to a self-employed person.
- **R-CI-CNPS-7, status.** Trigger: a question whether a contractor, mandataire or director is a salaried worker or an independant. Message: 'That is a legal question on the facts, and Code du Travail art 2 was not read here. Escalate to a warranted Ivorian adviser.'
- **R-CI-CNPS-8, convention.** Trigger: a request to exempt a foreign or seconded worker, or to transfer or total periods across countries. Message: 'No social security convention text was read here. I will not state an exemption or a transfer. Ask CNPS or a warranted adviser which convention applies.'

### Missing facts

Questions come before output: ask them at Step 4 of `social-contributions-workflow-base`, before any computation. What stays unanswered is Needs Input and is listed in the working paper. A default below stands only where a text read fixes the result.

| Missing fact | Action |
| --- | --- |
| Salaried worker's gross pay by component, or the period | R-CI-CNPS-6 |
| AT/MP rate | Needs Input: ask for the CNPS notification. No default. 2% is the lowest rate, so it is not conservative, and no text read fixes 5%. The range is XOF 1,500 to 3,750 a month per worker at the 75,000 ceiling, for scale only |
| Employer contribution under Code Art 10 2° | Needs Input: look for any separate line on the CNPS appel. The decree was not read, so employer figures here are subtotals of the known components |
| Headcount | Needs Input: it sets the date, not the amount. CNPS says 'occupe 20 salariés ou plus'; no text read says whether occasional workers count or on what date headcount is measured. Do not assume either periodicity |
| CMU covered persons | Needs Input: count the worker, the spouse, children under 21 and any disabled adult child, and ask whether the spouse has income. Show the worker's own 500 and 500, label it as that alone and do not report it as the total |
| Character of an allowance | Needs Input: ask what it pays for and for its evidence. Missing evidence does not prove it is pay. Show both cases (Example 1) |
| Salary below the SMIG | Default stands: Code Art 23 fixes the floor for a salaried worker. The apprentice and Art 16 cases are separate rows |
| Pay above 3,375,000 a month | Default stands: the retirement base stops at 3,375,000 a month (CNPS communiqué, from 1 January 2023), subject to the annual regularisation. Check the ceiling on the appel; a different figure there is Needs Input |
| Period before 1 January 2023 | Needs Input: the CNPS page prints a SMIG of 60,000 with no date, and the 2021 leaflet a ceiling of 2,700,000. No period table was read |
| Hourly SMIG; amount exempted by the tax authority for transport | Needs Input. Neither was read, so the exclusion limits cannot be computed |
| Value of a benefit in kind | Needs Input: real value, or for housing the fiscal rule with the scale as a minimum |
| Part-month, part-time or agricultural worker | Needs Input. No pro-ration of the floor was read. The SMIG is stated for 40 hours a week. A SMAG figure was seen only in a digest |
| More than 1 employer | Needs Input. No text read says how ceilings or the floor apply across employers |
| Apprenticeship contract; Art 16 status | Needs Input: the base differs, and the Art 95 annual minimum was not read |
| Self-employed category, declared income, period or date of first declaration | Needs Input, not R-CI-CNPS-6: RSTI runs on declared income (Décret 2020-308 Art 4), so no payslip is needed. Several activities: the highest floor applies (Arrêté 2020-065 Art 2). A change of activity alters the base from the first of the following month (Art 3) |
| CMU route of a self-employed person | Needs Input: agricultural income (Décret 2017-123 Arts 21, 22), impôt synthétique, taxe forfaitaire, taxe communale de l'entreprenant, or an IPS-CNAM delegated manager |
| Unmatched, bundled or unreferenced remittance | Credit nothing to a period until the appel or CNPS statement splits it |
| Tier 2 question threshold | XOF 0: no row is filtered on amount, as no floor is supported |

### Rules for using this file

- Compute on assiette, with the floor and ceiling in 'The base'. The ceilings are annual: a monthly clamp alone is not the final answer.
- Never deduct family benefits, maternity or AT/MP from the worker. Code Arts 10 and 13 void any contrary agreement, save voluntary insurance.
- The worker's deductions are 6.3% retirement and CMU: 500 for each person whose cost the employer shares, and 1,000 for each child beyond the sixth.
- Never compute CMU as a percentage. It is a flat amount per person.
- Never invent the AT/MP rate or category.
- Never apply the 3,375,000 ceiling to family benefits, maternity or AT/MP. Those use 75,000.
- Never contribute on a salary below the SMIG for a salaried worker, save the apprentice and Art 16 cases.
- Never tie a penalty to the wrong text: 'Penalties and interest' names each one.
- Never present figures as definitive: label them estimated and direct the client to their CNPS appel de cotisations.

## Rates, bands and thresholds

Ordinary rates are in the first table. By date: retirement was 8% in the 1999 text, 12% from signature of Ordonnance 2012-03 (11 January 2012) to 31 December 2012, and 14% after. The Code rates for the other branches have no later change in the texts read.

| Item | Figure | Applies to | Source and limit |
| --- | --- | --- | --- |
| Retirement (Assurance Vieillesse) | 14.00%: employer 7.70%, worker 6.30% | Base up to the retirement ceiling | [CNPS Employeur page](https://www.cnps.ci/employeur) states the rate and split; worker share 6.3% 'depuis le 1er Janvier 2013'. Ordonnance 2012-03 Art 22 sets 14% and 55% employer, 45% worker, as read only in an unofficial copy on loidici.biz with no gazette check. Official [Conseil des ministres, 11 January 2012](https://www.gouv.ci/uploads/publications/1372331568CCM_11_01_2012.pdf) agrees on 14% from January 2013 |
| Family benefits (Prestations Familiales) | 5.00%, employer only | Base up to 75,000 | [Code Arts 10, 12](https://www.cnps.ci/wp-content/uploads/2020/08/Loi-n%C2%B0-99-477-du-02-ao%C3%BBt-1999-portant-modification-du-Code-de-Pr%C3%A9voyance-Sociale-Amendment-to-the-Social-Security-Code.pdf): 5.75% in all, of which 0.75% maternity. The 5% is that total less maternity, as CNPS states. Art 10 2° also has an employer contribution for the daily allowance and medical care in Arts 53 and 54, at a rate set separately by decree. That decree was not read, so whether it adds to or sits within the 0.75% is held |
| Maternity (Assurance Maternité) | 0.75%, employer only | Base up to 75,000 | same |
| Work injury (AT/MP) | 2.00% to 5.00%, employer only, by risk of the activity | Base up to 75,000 | [Code Arts 13, 15, 17](https://www.cnps.ci/wp-content/uploads/2020/08/Loi-n%C2%B0-99-477-du-02-ao%C3%BBt-1999-portant-modification-du-Code-de-Pr%C3%A9voyance-Sociale-Amendment-to-the-Social-Security-Code.pdf). CNPS notifies the rate with the matricule. The risk arrêté and the tariff decree, which can add ristournes or supplements, were not read. The legacy '4 categories' is unverified |
| Ceiling, family benefits, maternity and AT/MP | 75,000 a month from 1 January 2023; 225,000 a quarter and 900,000 a year (computed: 3 and 12 times the month, as CNPS splits the annual ceiling by pay period) | Those 3 branches | [CNPS communiqué, January 2023](https://www.cnps.ci/wp-content/uploads/2023/01/NOUVEAU-PLAFOND-DES-COTISATIONS-SOCIALES-DE-LA-CNPS.pdf): 'Le nouveau salaire mensuel plafond des autres branches ... est fixé à 75 000 FCFA'. Administrative: the decree under Code Art 23 was not read. The ceiling now equals the SMIG floor, so Art 23's 'en aucun cas' and the ceiling no longer conflict |
| Retirement ceiling | 3,375,000 a month from 1 January 2023; 10,125,000 a quarter and 40,500,000 a year (computed: 3 and 12 times the month) | Retirement | [CNPS communiqué, January 2023](https://www.cnps.ci/wp-content/uploads/2023/01/NOUVEAU-PLAFOND-DES-COTISATIONS-SOCIALES-DE-LA-CNPS.pdf): 'Le nouveau salaire mensuel plafond de la branche retraite s'établit à 3 375 000 FCFA'. Administrative. 45 times 75,000 is 3,375,000 |
| Retirement ceiling rule | 45 times the SMIG, annual and split by pay period | Retirement | [CNPS Employeur page](https://www.cnps.ci/employeur). Administrative. Code Arts 21 and 23 leave the ceiling to a decree, which was not read. The CNPS communiqué of January 2023 ties the new ceilings to Décret 2022-986 on the SMIG; that decree's text was not read, so whether it fixes the ceiling itself is not shown |
| Earlier printed ceilings | Retirement: 2,700,000 a month (45 times 60,000); 1,647,315 a month (45 times 36,607, computed: 1,647,315 divided by 45). Other branches: 70,000 a month, 210,000 a quarter, 840,000 a year | Periods before 1 January 2023 only | [Leaflet, edition 2021](https://www.cnps.ci/wp-content/uploads/2021/04/RECOUVREMENT-R.pdf) for 2,700,000 and 70,000. The [CNPS Employeur page](https://www.cnps.ci/employeur) still prints 1,647,315, with 19,767,780 a year, and 70,000. The date each applied from was not read |
| SMIG | 75,000 a month from 1 January 2023, up from 60,000 | Floor | Official [Conseil des ministres, 21 December 2022](https://www.gouv.ci/uploads/publications/1671692497Communique-du-Conseil-des-Ministres-du-mercredi-21-decembre-2022.pdf): decree adopted, amount and date stated. The CNPS communiqué of January 2023 names it Décret 2022-986 of 21 December 2022 and sets the floor for all branches at 75,000 from 1 January 2023. The decree text was not read. CLEISS adds 40 hours a week. No later SMIG decree was found, but the search was not complete: held |
| Apprentice base | 37,500 with an apprenticeship contract; 75,000 without (computed: half the SMIG, or the SMIG, on the 75,000 SMIG) | Notional salary | [CNPS Employeur page](https://www.cnps.ci/employeur): half the SMIG or the SMIG, arithmetic on 75,000. Administrative |
| CMU | XOF 1,000 a month per person, whatever the age. For a salaried worker: employer 500, worker 500 | Every person under Art 3. A self-employed person pays the 1,000 by the routes in Arts 21 to 29. The employer's share covers the worker, spouse and up to 6 children under 21 (Art 9) | [Décret 2017-123 Arts 3, 9, 10](https://extranet.who.int/cpcd/sites/default/files/public_file_repository/CIV_Cote-d-Ivoire_Decret-No-2017-123-fixant-le-montant-et-les-modalites-de-recouvrement-des-cotisations_2017.pdf), JO 30 May 2017, due from 1 October 2017 (Art 30), read in the WHO copy and checked on the page images. Art 3 puts the assistance regime for the economically weak or destitute on the State budget. Enacted, under Loi 2014-131 Art 40. Amendments not checked |
| CMU beyond 6 children | XOF 1,000 per further child, all from the worker | Seventh child onwards | same |
| RSTI | 12% of declared income: 9% old age, 3% maternity, sickness and accident | Between the category floor and the ceiling | [Décret 2020-308 Art 6](https://www.cnps.ci/wp-content/uploads/2020/08/Decret-n-%C2%A62020-308-du-4-mars-2020-fixant-les-modalit%C3%A9s-de-fonctionnement-des-r%C3%A9gimes-de-pr%C3%A9voyance-sociale-des-travailleurs-2.pdf); [Arrêté 2020-065 Art 7](https://www.cnps.ci/wp-content/uploads/2020/08/Arr%C3%AAt%C3%A9-revenu-plancher-RSTI.pdf). The person alone owes it, even where payment is delegated (Délibération 004 Art 4) |
| RSTI ceiling | 180,000 a month | RSTI | [Arrêté 2020-065 Art 5](https://www.cnps.ci/wp-content/uploads/2020/08/Arr%C3%AAt%C3%A9-revenu-plancher-RSTI.pdf). The legacy 'no pension ceiling' is wrong for this regime. CLEISS's 'pas de plafond' fits the complementary regime only |
| RSTI complementary | 9% of declared income above the RSTI ceiling (cent quatre-vingt mille francs CFA a month, Arrêté 2020-065 Art 5), with no ceiling | Compulsory above the ceiling | [Décret 2020-308 Arts 5, 6](https://www.cnps.ci/wp-content/uploads/2020/08/Decret-n-%C2%A62020-308-du-4-mars-2020-fixant-les-modalit%C3%A9s-de-fonctionnement-des-r%C3%A9gimes-de-pr%C3%A9voyance-sociale-des-travailleurs-2.pdf); Ordonnance 2019-636 Arts 8, 16; [Arrêté 2020-065 Arts 5, 8](https://www.cnps.ci/wp-content/uploads/2020/08/Arr%C3%AAt%C3%A9-revenu-plancher-RSTI.pdf) |
| Reform of the Code, 2026 | Ordonnance amending Loi 99-477 adopted, with a ratification bill | Pension calculation and orphan's pension, as described | Official [Conseil des ministres, 23 September 2026](https://www.presidence.ci/communiques-ministres/communique-du-conseil-des-ministres-du-mercredi-23-septembre-2026/). Its number and text were not obtained, and the communiqué is silent on contributions. That silence does not show Arts 12 to 23 are unchanged: held. The communiqué says the Conseil adopted these reforms on 1 October 2025 and that CNPS and IPS-CGRAE already apply them, so pension calculation may already differ from the 1999 text |

### Self-employed floors

Arrêté 2020-065 of 16 July 2020, table checked on the page image. The minimum monthly contribution is floor times 12%; for Ivorians abroad it is floor times 9%, as the 3% does not apply to them (Art 7).

| Category | Revenu plancher | Minimum monthly contribution | Source |
| --- | --- | --- | --- |
| Commerçants | 30,000 | 3,600 | [Arrêté 2020-065 Art 4](https://www.cnps.ci/wp-content/uploads/2020/08/Arr%C3%AAt%C3%A9-revenu-plancher-RSTI.pdf) |
| Sportifs | 30,000 | 3,600 | same |
| Artisans | 45,000 | 5,400 | same |
| Artistes et professionnels des médias et de l'évènementiel | 45,000 | 5,400 | same |
| Exploitants agricoles | 45,000 | 5,400 | same |
| Religieux et assimilés | 50,000 | 6,000 | same |
| Exploitants miniers | 50,000 | 6,000 | same |
| Transporteurs | 75,000 | 9,000 | same |
| Consultants | 100,000 | 12,000 | same |
| Professions libérales et mandataires sociaux | 150,000 | 18,000 | same |
| Ivoiriens travaillant à l'étranger | 150,000 | 13,500 | same |

The legacy range of 30,000 to 150,000 is confirmed. The maximum in the base regime is 180,000 times 12% = 21,600, as the CNPS Indépendant page states.

## The base

Code Art 23 is common to all 3 branches: contributions run on all salaries, including benefits in kind and various indemnities paid by the employer to its salaried staff, except indemnities in the nature of a reimbursement of expenses. CNPS adds the items below as administrative practice. Only Art 23 and the rates are enacted text, and the 14% retirement rate rests on an unofficial copy of the ordonnance.

| Pay item | Treatment | Basis and limit |
| --- | --- | --- |
| Base salary, supplements, bonuses, gratifications and other indemnities | In | Code Art 23; CNPS page: all other bonuses, gratifications or indemnities are subject |
| Benefit in kind | In, at real value | CNPS page |
| Housing as a benefit | In, at real value. If unknown, under the fiscal rules. The fiscal scale is a minimum in every case | CNPS page. The scale was not read |
| Expense reimbursement | Out | Code Art 23. No text read names the documents that prove it: ask for receipts or the policy and let a reviewer decide. Missing evidence is Needs Input |
| Family allowances | Out | CNPS page, on gross salary |
| Prime de panier | Out, up to 3 times the hourly SMIG | CNPS page, 'déductions autorisées'. Hourly SMIG not read. The page does not say per meal or per month |
| Monthly prime de salissure | Out, up to 13 times the hourly SMIG | same |
| Monthly indemnité de tenue de travail | Out, up to 7 times the hourly SMIG | same |
| Monthly prime d'outillage | Out, up to 10 times the hourly SMIG | same |
| Monthly indemnité de transport | Out, up to once the amount exempted by the tax authority | CNPS page. Figure not read |

For a salaried worker on a full month:

```
assiette = cash pay + benefits in kind + indemnities
           - expense reimbursements - excluded items within their limits
retirement_base = min(max(assiette, SMIG), retirement_ceiling)
other_base      = min(max(assiette, SMIG), 75,000)
retirement_worker   = retirement_base * 6.3%
retirement_employer = retirement_base * 7.7%
family     = other_base * 5%      employer
maternity  = other_base * 0.75%   employer
at_mp      = other_base * notified rate   employer
cmu_employer = 500 * min(1 + spouse + children, 1 + spouse + 6)
cmu_worker   = 500 * min(1 + spouse + children, 1 + spouse + 6)
               + 1,000 * max(children - 6, 0)
```

SMIG 75,000 and ceiling 75,000 mean `other_base` is 75,000 for any salaried worker in that formula, whatever the pay. An apprentice or Art 16 person uses their own base. 'spouse' is 1 for a spouse without income, whose cost Décret 2017-123 Art 5 charges to the earning spouse. Art 9's employer share says 'son époux' with no income condition, so a spouse with income is Needs Input. 'children' are children under 21 charged to this worker (Arts 4, 9). A disabled adult child is outside this formula: Art 4 charges that person's XOF 1,000 to the parents, and the employer share is Needs Input (Example 7).

**Annual ceilings.** CNPS states that the ceiling is annual, split by pay period so that each pay can be calculated, and that the employer must regularise over all pay between the first and last days of the year. The reason it gives is so that bonuses paid at long intervals, and pay that varies, are not cut by one month's ceiling. Regularisation runs through the DISA. Example 5 shows the effect. No text read says how a part-year worker's annual ceiling is set, or when any extra must be paid.

**RSTI base.** Declared flat income, not profit. It cannot be below the category floor. It is declared at affiliation, by the online enrolment form (Délibération 004 Art 2), and CNPS gives the amount due at that point. Arrêté 2020-065 Art 6 lets the person change it at any time, and Art 7 says the base for a month is the income declared at the start of that month. Délibération 004 Art 2 makes a change effective from the quarter after a request that leaves a written trace. The 2 texts differ, so the date a mid-year change takes effect is Needs Input.

### Income tax interaction

Code Art 8(2) exempts contributions paid to CNPS by employers, workers or users, compulsory or voluntary, from all taxes. Loi 2014-131 Art 48 does the same for CMU, and Ordonnance 2019-636 Art 24 gives RSTI contributions the same tax treatment as salaried contributions. These provisions do not set the ITS base, a deduction in business income or a TVA entry. Held: whether employer contributions are a deductible cost, how penalties are treated, whether worker contributions reduce the ITS base and any TVA entry belong to `ivory-coast-payroll`, `ivory-coast-income-tax` and `ivory-coast-vat`. The tax code was not read here.

### Bank narrations

Treat these as an unverified guide, not an official list: no text read gives bank wording. Test in this order:

1. **Direction.** A contribution is a débit. A credit is never a contribution: PENSION CNPS and RENTE go to the last row, and any other incoming CNPS line stays unmatched until it is explained.
2. **Match.** Use case-insensitive substrings on the counterparty or reference, but match ITS, TVA, PAIE, CMU and RENTE as whole words, so that PAIEMENT CNPS stays a CNPS line.
3. **Collision.** A débit that matches both a CNPS row and a 'Not CNPS' row stays unmatched until the appel explains it.

A match identifies the payee only: it does not split a payment by branch, credit a period or settle a tax treatment. Code Art 8(2) and Loi 2014-131 Art 48 exempt these contributions from taxes, but the tax code was not read, so this file states no TVA return entry. `ivory-coast-vat` owns that: its pattern library lists CNPS as EXCLUDE and does not list CMU.

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CNPS, PREVOYANCE SOCIALE | CNPS contribution | Monthly or quarterly appel de cotisations |
| COTISATION SOCIALE, COTISATIONS CNPS, COTIS SOCIALES | CNPS contribution | Same |
| RETRAITE CNPS, ASSURANCE VIEILLESSE (outgoing) | CNPS, retirement branch | A branch word in a narration does not prove the split |
| PRESTATIONS FAMILIALES, ALLOC FAMILIALES | CNPS, family-benefits branch | Employer only |
| ACCIDENT TRAVAIL, AT/MP | CNPS, work-injury branch | Employer only |
| APPEL DE COTISATIONS, APPEL COTISATIONS | CNPS contribution | The CNPS billing reference |
| CMU, COUVERTURE MALADIE UNIVERSELLE | CMU contribution | XOF 1,000 per person in general; see the CMU rows |
| CNAM | CMU contribution | Caisse Nationale d'Assurance Maladie, the CMU manager |
| DGI, DIRECTION GENERALE DES IMPOTS | Not CNPS: tax | Income or payroll tax (ITS and others), not social security |
| ITS, IMPOT SUR SALAIRES | Not CNPS: payroll tax | Send to `ivory-coast-payroll` |
| TVA | Not CNPS: VAT | Send to `ivory-coast-vat` |
| SALAIRE, PAIE, VIREMENT SALAIRE (outgoing) | Not CNPS: payroll | Not a contribution payment |
| PENSION CNPS, RENTE (incoming) | Not CNPS: benefit received | Not a contribution paid. CNPS contribution débits are outgoing |

Legacy wording by bank, unverified: SGCI (Société Générale CI) 'CNPS COTISATIONS' or 'PREVOYANCE SOCIALE'; BICICI 'CNPS' or 'COTIS SOCIALES'; Ecobank CI 'CNPS COTISATION' or 'PREVOYANCE'; NSIA Banque 'CNPS' or 'COTISATION SOCIALE'; Coris Bank 'CNPS' or 'APPEL COTISATIONS'. Timing follows the appel, and the amount should match it. A 'REGULARISATION' lump sum may bundle principal with the 10% penalty and majorations: credit nothing until CNPS splits it.

If a client gives a bank statement but no payroll detail, this is intake only: identify the CNPS and CMU débits and ask the questions in 'Ask the client first' before any output. Do not back-solve salary, the AT/MP rate or headcount from a débit, because the débit may be bundled, cover several periods or include penalties. What stays unanswered is Needs Input.

## Deadlines and filing

Filing runs through the e-CNPS portal (https://e.cnps.ci/): the appel for CNPS and CMU and payment are made online from an activated account, and the 2021 leaflet says declarations are made exclusively there. Payment can also be by bank transfer, by cheque at a CNPS agency or in cash at financial institutions, with the appel.

| Item | Deadline | Basis and limit |
| --- | --- | --- |
| Contributions, 20 or more salaried workers | Monthly: within the first 15 days after the month ended | CNPS Employeur page; leaflets 2018 and 2021. Administrative: Code Art 24 leaves the due date to a decree, not read. Contributions are due monthly; only the payment period differs |
| Contributions, fewer than 20 | Quarterly: within the first 15 days after the quarter ended | same |
| CMU through CNPS | Monthly payer: the same date. Quarterly payer: held | Décret 2017-123 Art 6 says sums deducted in a month are paid by the 15th of the following month, and Art 13 has CNPS collect them. CNPS bills CMU on the same appel. Whether a quarterly payer follows the quarter or Art 6 is Needs Input |
| Déclaration Individuelle des Salaires Annuels (DISA), with the Déclaration Annuelle des Salaires et Cotisations (DASC) | By 31 March of the following year | CNPS leaflets 2018 and 2021; the CNPS page says the end of the first quarter. Not in Code Art 26, which leaves periodicity and form to the CNPS board; that decision was not read |
| DISA medium | An electronic file (USB key, CD, email), not write-protected, or online on e-CNPS. The free e-DISA program produces it. The signed, stamped DASC goes on paper whatever the route | Leaflet 2021, which elsewhere says declarations are exclusively online. Confirm the route with CNPS |
| Employer registration | Affiliation takes effect from the first hire | Code Art 5. 'Déclaration aux fins d'immatriculation' through GUFE or a CNPS agency. CNPS issues the matricule and notifies the AT/MP rate |
| Worker declaration | First day of work | CNPS page and leaflets: 'fiche de déclaration du travailleur' through CEPICI, e-CNPS or an agency. The CNPS number is unique and permanent. Late declaration calls for the earlier DISAs |
| CMU nominal state | No date read | Décret 2017-123 Arts 7, 8: names, CMU numbers, dependants, amount and date, on paper or electronically. CNAM can regularise an understated count (Art 8), and the employer must be able to show it is up to date (Art 12). The arrêté on detail was not read |
| Change or departure | Immediately | Leaflets: 'fiche de déclaration de cessation d'emploi' on departure; written notice of closure |
| Accident or occupational disease | 48 hours | Code Art 71 |
| RSTI affiliation | Within 1 month of becoming subject | Ordonnance 2019-636 Art 7 |
| RSTI contributions | Quarterly, by the 15th of the month after the quarter: 15 April, 15 July, 15 October and 15 January | Décret 2020-308 Art 7; Arrêté 2020-065 Art 9. First declaration in the first month of a calendar quarter: that quarter is due. In the last 2 months: the next quarter (Délibération 004 Art 3) |
| RSTI part-payments and advances | Instalments are allowed up to the due date. An advance may cover no more than 12 months and only months of the current year. Liquidation of retirement rights ends any further payment | Délibération 004 Art 5; Arrêté 2020-065 Art 9. Modes: cheque at a CNPS agency, bank transfer on the CNPS payment platform, Mobile Money through partners, cash through partner institutions |
| RSTI unvalidated periods | Can be regularised within a limit of 2 years, base regime only, on the terms of the original due date | Délibération 004 Art 6. Complementary periods cannot be regularised. Art 7 lets a person who meets the age condition but has under 40 quarters buy back up to 8 quarters |

No text read moves a due date that falls on a non-working day. Treat that as Needs Input.

### Working paper

```
CÔTE D'IVOIRE CNPS COMPUTATION: WORKING PAPER ONLY, ESTIMATED
Employer: [name]                 Matricule CNPS: [____]
Employee: [name]                 Period: [month or quarter, year]
Prepared: [date]                 Currency: XOF

INPUT DATA
  Gross monthly salary (brut):        XOF [____]
  Benefits in kind and indemnities:   XOF [____]  (contributory? Y/N)
  Expense reimbursements:             XOF [____]  (excluded; evidence: ____)
  Excluded items within limits:       XOF [____]
  Assiette (contribution base):       XOF [____]
  AT/MP rate, CNPS notification:      [__%, ref ____]
  Headcount and date measured:        [____]
  CMU persons: worker + spouse (income? Y/N) + children: [____]

BASES
  SMIG floor:                         XOF 75,000
  Retirement ceiling, from appel:     XOF [____]  (3,375,000 from 1 January 2023, CNPS communiqué)
  Retirement base:                    XOF [____]
  Other-branch base:                  XOF [____]  (75,000 ceiling)

COMPUTATION                         Worker        Employer
  Retirement 6.3% / 7.7%            XOF [____]    XOF [____]
  Prestations familiales 5%              -        XOF [____]
  Maternité 0.75%                        -        XOF [____]
  AT/MP __%                              -        XOF [____]
  CMU                               XOF [____]    XOF [____]
  SUBTOTAL, KNOWN COMPONENTS        XOF [____]    XOF [____]

PAYMENT
  Periodicity:                       [Monthly / Quarterly / Needs Input]
  Deadline:                          [first 15 days after period end]
  Known subtotal (worker + employer): XOF [____]  (check the appel for other lines)

ANNUAL
  Year's base against annual ceiling: XOF [____]
  DISA and DASC due:                 31 March [year + 1]

NEEDS INPUT
  [Every unanswered fact and what it changes]

REVIEWER FLAGS
  [Tier 2 flags, held figures, defaults applied and their impact]
```

## Penalties and interest

Each charge belongs to the text that creates it. The Code's penalties attach to duties under the Code. CMU duties sit in Loi 2014-131 and Décret 2017-123, and RSTI duties in Ordonnance 2019-636. A charge under one does not reach a duty in another unless the text says so. Legacy said late payment attracted 10% of contributions due under Art 30: that was wrong.

| Failure | Consequence | Text and limit |
| --- | --- | --- |
| Late payment of CNPS contributions | Majoration of 0.050% per day of delay on sums unpaid at the due date | CNPS Employeur page, administrative, the only retained source that prints this rate, on a page partly stale. Code Art 24 leaves majorations and moratory interest to a decree, not read, so the rate has no enacted text here. The page does not say how days are counted. No moratory interest rate was read |
| Retirement: who bears it | The employer; it applies to both worker and employer shares | Code Art 21 |
| Relief | Majorations can be reduced or cancelled for good faith or force majeure, by reasoned board decision on a recours gracieux | CNPS Employeur page, administrative |
| No declaration under Art 26 by the due dates | Penalty of 10% of the employer's total monthly contributions due | Code Art 30, a penalty for the declaration, not for late payment. CNPS applies it to the DISA. Which month sets the base is Needs Input. Nothing in Art 30 reaches CMU |
| Same failure, administrative | No attestation de mise à jour for the business, and no attestation d'immatriculation for the dirigeant | CNPS leaflets, administrative |
| Breach of the recovery rules; non-payment | Contravention fines set by decree, once per worker affected, with total fines capped at 10 times the maximum fine | Code Arts 21, 29, 166. Decree not read, so no amount. Art 31 requires a mise en demeure first, giving 15 days to 3 months |
| Other breaches of the Code | Contravention penalties by decree | Code Art 174. Decree not read |
| Family contributions unpaid by the due date | On top of the Art 29 sanctions, arrears and majorations, CNPS can recover from the employer all family benefits the recipients could claim between the due date and full settlement | Code Art 32. By reasoned decision the board can reduce these claims for a debtor in a precarious position, but not contributions or majorations. Art 33 disapplies for work injury the 'dernier alinéa' of Art 32 'relatives à la poursuite auprès de l'employeur'. Those words describe Art 32's first paragraph, not its last, so the reach of Art 33 is held. The CNPS Employeur page, administrative, adds that a worker who loses benefits through the employer's default can sue for damages |
| Worker share not withheld | After a mise en demeure under Art 31, the regularisation covers both shares, withheld or not. In good faith the employer can later recover it from pay, within the attachable portion. Penalties and interest stay with the employer | Code Art 167 |
| Recovery | Contrainte, opposition within 15 days; civil action prescribes in 5 years from the due date, unless interrupted | Code Arts 34 to 37. Art 18 gives a 5-year privilege for AT/MP |
| CMU, late payment | Majoration of 1% per month of delay. The employer owes all of it | Décret 2017-123 Art 12. Part months are not addressed |
| CMU, knowingly false declarations by an employer or insured person | Imprisonment of 1 to 5 years and a fine of XOF 100,000 to 1,000,000 | Loi 2014-131 Art 67 |
| CMU, employer not affiliated | Fine of XOF 100,000 to 1,000,000, with an order to affiliate within 1 month | Loi 2014-131 Art 68 |
| CMU, no registration of workers | Fine of XOF 100,000 to 1,000,000, with an order to register within 1 month | Loi 2014-131 Art 69 |
| CMU, undue deduction made knowingly | Fine of XOF 100,000 to 1,000,000 | Loi 2014-131 Art 70. Art 55 sends breaches of the Act and its texts to the criminal courts, Art 71 keeps other sanctions, and Art 72 allows damages |
| CMU, recovery | 5 years from the end of the set time limits | Loi 2014-131 Art 59 |
| RSTI, late or no payment | Penalties under a decree taken after board advice | Ordonnance 2019-636 Art 29. Decree not read, so no rate is stated |
| RSTI, recovery | 5 years from the 16th day of the quarter after the period. Undue payment: 3 years | Ordonnance 2019-636 Art 27 |

`ivory-coast-payroll` reports a CLEISS rate of 5% for the first month and 1% for each further month. The CLEISS page read here shows no such rate. Do not use it. The hold list at the end records this.

## Cross-border points

Code Art 5 turns on employing workers under Code du Travail art 2. The texts read contain no exemption for a foreign national, and the leaflets list documents for foreign workers; that absence is held, not a rule. Art 164 tells CNPS to make coordination conventions with other States' retirement bodies, and Ordonnance 2019-636 Art 9 refers to countries that have signed a social security convention. No convention text was read, and no multilateral regime such as CIPRES's was read. A convention position is R-CI-CNPS-8. CIPRES appears in the texts read only as a management-ratio limit (Loi 2014-131 Art 42), and UEMOA only through Règlement 07/2009 on mutual bodies (Loi 2014-131 Art 36). Neither supports a contribution rule here. No OHADA text was read. CMU care is covered only if prescribed and given in Côte d'Ivoire, save under social security conventions (Loi 2014-131 Art 8).

## Two worked examples that recompute

Each block below was recomputed separately in exact decimal arithmetic. Unless stated, examples assume an employer in Abidjan, a full-time worker on a full month of 2026, and an AT/MP rate of 3% taken from the CNPS notification. Figures are estimates for a reviewer. Every employer figure is a subtotal of the known components: if the unread Code Art 10 2° decree adds a charge, it understates the liability, so check it against the CNPS appel. Slot 12 of the workflow base maps to Example 1 (within limits), Example 2 (above the ceiling), Example 3 (below the floor) and Example 4 (self-employed). No rounding rule was read, so these figures are unrounded; a result with a fraction of a franc is Needs Input.

### Example 1: employee within limits, allowance undecided

A worker earns XOF 500,000 and also receives XOF 30,000 described as 'frais'. The worker alone is covered for CMU. Nobody has shown what the 30,000 pays for.

```oa-check
name: Salary 500,000 with an undecided allowance of 30,000
inputs:
  salary: 500000
  allowance: 30000
  smig: 75000
  other_ceiling: 75000
  retirement_ceiling: 3375000
  worker_rate: 0.063
  employer_rate: 0.077
  other_rate: 0.0875
  cmu_each: 500
steps:
  - base_a: min(max(salary, smig), retirement_ceiling)
  - worker_a: base_a * worker_rate + cmu_each
  - employer_a: base_a * employer_rate + other_ceiling * other_rate + cmu_each
  - base_b: min(max(salary + allowance, smig), retirement_ceiling)
  - worker_b: base_b * worker_rate + cmu_each
  - employer_b: base_b * employer_rate + other_ceiling * other_rate + cmu_each
  - total_a: worker_a + employer_a
  - total_b: worker_b + employer_b
  - gap: total_b - total_a
expected:
  base_a: 500000
  worker_a: 32000
  employer_a: 45562.5
  base_b: 530000
  worker_b: 33890
  employer_b: 47872.5
  total_a: 77562.5
  total_b: 81762.5
  gap: 4200
```

If receipts show a reimbursement of expenses, Art 23 leaves it out: the worker bears XOF 32,000 and the employer subtotal is XOF 45,562.50. If it is pay, the worker bears XOF 33,890 and the employer subtotal is XOF 47,872.50. The file does not choose: the XOF 4,200 gap stays Needs Input until the evidence is seen. The retirement ceiling plays no part here, as the base is below 3,375,000.

### Example 2: above the ceiling

A worker earns XOF 5,000,000 in a month of 2026. The block uses the retirement ceiling of 3,375,000 and the other-branch ceiling of 75,000 from the CNPS communiqué of January 2023. If the appel shows another figure, the difference is Needs Input.

```oa-check
name: Salary 5,000,000 above the retirement ceiling
inputs:
  salary: 5000000
  retirement_ceiling: 3375000
  other_ceiling: 75000
  worker_rate: 0.063
  employer_rate: 0.077
  family: 0.05
  maternity: 0.0075
  at_mp: 0.03
  cmu_each: 500
steps:
  - base: min(salary, retirement_ceiling)
  - retirement_worker: base * worker_rate
  - retirement_employer: base * employer_rate
  - family_due: other_ceiling * family
  - maternity_due: other_ceiling * maternity
  - at_mp_due: other_ceiling * at_mp
  - worker_total: retirement_worker + cmu_each
  - employer_subtotal: retirement_employer + family_due + maternity_due + at_mp_due + cmu_each
expected:
  base: 3375000
  retirement_worker: 212625
  retirement_employer: 259875
  family_due: 3750
  maternity_due: 562.5
  at_mp_due: 2250
  worker_total: 213125
  employer_subtotal: 266937.5
```

Pay above the ceiling carries no retirement contribution for that month, subject to the annual regularisation in Example 5. The worker bears XOF 213,125 and the employer subtotal is XOF 266,937.50.

### Example 3: below the floor

A full-time worker is paid XOF 50,000 for the month. Art 23 fixes the base at the SMIG, so this is a default that stands. The pay itself is a wage issue for `ivory-coast-payroll`. Since 1 January 2023 the other-branch ceiling is 75,000, equal to the floor, so the 3 employer branches also run on 75,000. The last 2 steps show what the stale 70,000 on the CNPS Employeur page would understate.

```oa-check
name: Pay 50,000 below the SMIG floor
inputs:
  pay: 50000
  smig: 75000
  other_ceiling: 75000
  stale_ceiling: 70000
  worker_rate: 0.063
  employer_rate: 0.077
  other_rate: 0.0875
  cmu_each: 500
steps:
  - base: max(pay, smig)
  - worker_total: base * worker_rate + cmu_each
  - other_branches: min(base, other_ceiling) * other_rate
  - employer_subtotal: base * employer_rate + other_branches + cmu_each
  - other_on_stale_ceiling: min(base, stale_ceiling) * other_rate
  - understated_by_stale: other_branches - other_on_stale_ceiling
expected:
  base: 75000
  worker_total: 5225
  other_branches: 6562.5
  employer_subtotal: 12837.5
  other_on_stale_ceiling: 6125
  understated_by_stale: 437.5
```

On the 75,000 ceiling in the CNPS communiqué, the contributions are XOF 5,225 on the worker's side and an employer subtotal of XOF 12,837.50. The stale 70,000 still printed on the CNPS Employeur page would understate the employer by XOF 437.50 a month: do not use it for a period from 1 January 2023. Art 21 makes the worker's share a deduction from pay and Art 23 sets the base at the SMIG, so the block shows 6.3% of 75,000 as the worker's share. No text read deals with a floor above actual pay: flag it.

### Example 4: decision, self-employed consultant

A consultant affiliates to RSTI and makes a first declaration of XOF 300,000 a month in January 2026. A second consultant asks to declare XOF 80,000. CMU is separate and depends on the person's route, so it is outside these totals.

```oa-check
name: RSTI consultant at 300,000 and a declaration below the floor
inputs:
  declared: 300000
  floor: 100000
  ceiling: 180000
  old_age: 0.09
  other_risks: 0.03
  complementary: 0.09
  second_declared: 80000
steps:
  - base: min(max(declared, floor), ceiling)
  - old_age_due: base * old_age
  - other_due: base * other_risks
  - rsti_monthly: old_age_due + other_due
  - above_ceiling: max(declared - ceiling, 0)
  - complementary_monthly: above_ceiling * complementary
  - monthly: rsti_monthly + complementary_monthly
  - quarterly: monthly * 3
  - second_base: min(max(second_declared, floor), ceiling)
  - second_monthly: second_base * (old_age + other_risks)
expected:
  base: 180000
  rsti_monthly: 21600
  above_ceiling: 120000
  complementary_monthly: 10800
  monthly: 32400
  quarterly: 97200
  second_base: 100000
  second_monthly: 12000
```

The first consultant owes XOF 97,200 for the first quarter of 2026 by 15 April 2026, because the first declaration fell in the first month of that quarter (Délibération 004 Art 3). Had it fallen in February or March, the second quarter would be the first one due, by 15 July 2026. The second cannot declare XOF 80,000: Arrêté 2020-065 Art 6 sets the category floor as the minimum, so the declaration must be at least XOF 100,000 and the amount is XOF 12,000 a month. Neither position is a salaried calculation: R-CI-CNPS-1.

### Example 5: decision, annual regularisation

A worker earns XOF 3,000,000 a month throughout the year and a XOF 6,000,000 bonus in December. A month-by-month clamp at the 3,375,000 ceiling loses part of the base. CNPS requires the year to be tested against the annual ceiling through the DISA.

```oa-check
name: Annual retirement ceiling against a monthly clamp
inputs:
  monthly_pay: 3000000
  bonus: 6000000
  month_ceiling: 3375000
  months: 12
  worker_rate: 0.063
  employer_rate: 0.077
steps:
  - year_pay: monthly_pay * months + bonus
  - annual_ceiling: month_ceiling * months
  - clamped: monthly_pay * (months - 1) + min(monthly_pay + bonus, month_ceiling)
  - annual_base: min(year_pay, annual_ceiling)
  - extra_base: max(annual_base - clamped, 0)
  - extra_worker: extra_base * worker_rate
  - extra_employer: extra_base * employer_rate
  - extra_total: extra_worker + extra_employer
expected:
  year_pay: 42000000
  annual_ceiling: 40500000
  clamped: 36375000
  annual_base: 40500000
  extra_base: 4125000
  extra_worker: 259875
  extra_employer: 317625
  extra_total: 577500
```

The extra base of XOF 4,125,000 carries XOF 577,500: XOF 259,875 worker and XOF 317,625 employer. Without the regularisation, that base escapes. When it is payable, and how the worker's part is recovered outside the Art 167 good-faith case, are Needs Input.

### Example 6: decision, each penalty under its own text

An employer with 40 workers has CNPS contributions of XOF 2,000,000, both shares, for March 2026 and CMU of XOF 80,000, and pays both on 15 May 2026 rather than by 15 April 2026. That is 30 days and exactly 1 month late. Separately, if its DISA for 2025 had not been produced by 31 March 2026, Art 30 would apply. The block takes XOF 2,000,000 as the monthly total on that assumption, as the text does not say which month.

```oa-check
name: Late payment and missing declaration, by text
inputs:
  cnps_due: 2000000
  cmu_due: 80000
  days_late: 30
  months_late: 1
  daily_rate: 0.0005
  cmu_monthly_rate: 0.01
  art30_rate: 0.10
  monthly_total: 2000000
steps:
  - majoration_cnps: cnps_due * daily_rate * days_late
  - majoration_cmu: cmu_due * cmu_monthly_rate * months_late
  - art30_penalty: monthly_total * art30_rate
  - late_only: majoration_cnps + majoration_cmu
  - if_disa_also_missing: late_only + art30_penalty
expected:
  majoration_cnps: 30000
  majoration_cmu: 800
  art30_penalty: 200000
  late_only: 30800
  if_disa_also_missing: 230800
```

Late payment alone costs XOF 30,800: XOF 30,000 on the administrative CNPS rate, assuming simple daily accrual, which the page does not state, and XOF 800 under Décret 2017-123 Art 12. The XOF 200,000 arises only if the declaration is missing, and only on CNPS contributions. Legacy's 10% on late payment would have given XOF 200,000 for a failure that Art 30 does not cover. A client wanting a real figure gets R-CI-CNPS-3.

### Example 7: decision, CMU with 7 children

A worker has a spouse without income and 7 children under 21, all charged to this worker.

```oa-check
name: CMU beyond 6 children
inputs:
  spouse: 1
  children: 7
  per_person: 1000
  share: 0.5
steps:
  - shared_persons: 1 + spouse + min(children, 6)
  - employer_cmu: shared_persons * per_person * share
  - worker_shared: shared_persons * per_person * share
  - worker_beyond: max(children - 6, 0) * per_person
  - worker_cmu: worker_shared + worker_beyond
  - total_cmu: employer_cmu + worker_cmu
expected:
  shared_persons: 8
  employer_cmu: 4000
  worker_cmu: 5000
  total_cmu: 9000
```

The employer bears XOF 4,000 and the worker XOF 5,000, and the employer owes all XOF 9,000 to IPS-CNAM through CNPS (Arts 12, 13). Art 4 also charges disabled adult children to their parents, whilst Art 9's employer share names only children under 21. CLEISS reads the employer share as covering them, but the decree does not say so. For such a child, the employer share is Needs Input.

### Test cases

Calculation table, full month, one CMU person, on the ceilings from 1 January 2023.

| Gross | Retirement base | Worker retirement | Employer retirement | Other branches on 75,000 | CMU each side |
| --- | --- | --- | --- | --- | --- |
| 75,000 | 75,000 | 4,725.00 | 5,775.00 | 6,562.50 at 3% | 500 |
| 200,000 | 200,000 | 12,600.00 | 15,400.00 | 5,812.50 at 2% | 500 |
| 500,000 | 500,000 | 31,500.00 | 38,500.00 | 6,562.50 at 3% | 500 |
| 3,375,000 | 3,375,000 | 212,625.00 | 259,875.00 | 6,562.50 at 3% | 500 |
| 5,000,000 | 3,375,000 | 212,625.00 | 259,875.00 | 6,562.50 at 3% | 500 |

Other branches: 75,000 times 8.75% is 6,562.50 at 3%, and 75,000 times 7.75% is 5,812.50 at 2%. At 200,000 and 2%, the worker bears 13,100.00 and the employer subtotal is 21,712.50.

| Input | Result |
| --- | --- |
| Source quotes a ceiling of 1,647,315 for a 2026 period | R-CI-CNPS-2: use 3,375,000 unless a CNPS document for the period says otherwise |
| Source quotes an other-branch ceiling of 70,000 for a 2026 period | Use 75,000 (CNPS communiqué, from 1 January 2023) |
| RSTI consultant with declared income, the period and a January 2026 first declaration, but no payslip | Not R-CI-CNPS-6. Compute from declared income, as in Example 4 |
| The same consultant, first declaration in February 2026 | The second quarter is the first one due, by 15 July 2026 (Délibération 004 Art 3) |
| Salaried worker with a disabled adult child | XOF 1,000 is owed for that person (Décret 2017-123 Arts 3, 4). Whether the employer bears 500 of it is Needs Input, and whether that person counts towards the 6 children is held |
| Employer with 30 workers | Monthly, within 15 days of month end, subject to the headcount row |
| Employer with 8 workers | Quarterly, within 15 days of quarter end; DISA and DASC by 31 March |
| Gross pay exactly 3,375,000 | No excess; the same result as the ceiling row |
| `15.04.2025 ; DIRECTION GENERALE DES IMPOTS ; DEBIT ; ITS MARS 2025 ; -185,000 ; XOF` | Not CNPS: payroll tax to the DGI. Send to `ivory-coast-payroll` |
| `20.07.2025 ; CNPS PREVOYANCE SOCIALE ; DEBIT ; REGULARISATION ; -1,450,000 ; XOF` | CNPS payee, amount unsplit. Credit nothing; ask for the CNPS breakdown of principal, penalty and majorations |
| Incoming credit `PENSION CNPS` | Not CNPS: benefit received. The direction test comes first |
| Outgoing débit `PAIEMENT CNPS T1` | CNPS contribution. PAIE is matched as a whole word, so the payroll row does not apply |
| Outgoing débit `SALAIRE CNPS` | Unmatched: it hits both a CNPS row and a 'Not CNPS' row. Ask for the appel |

## Ask the client first

Ask these before any output, as grouped questions, at Step 4 of the workflow base.

1. **Status and period.** Which period, and is each person a salaried worker, apprentice, assimilated person, self-employed person or State agent?
2. **Pay.** Gross pay by component for each worker, with benefits in kind and evidence for any allowance described as expenses. Any worker part-month, part-time, agricultural or with another employer?
3. **CNPS documents.** The CNPS notification of the AT/MP rate, the matricule and the latest appel de cotisations, showing the ceiling used and every employer line.
4. **Headcount.** How many salaried workers, including occasional ones, and on what date? Does the employer pay monthly or quarterly now?
5. **CMU.** For each worker: the spouse and whether the spouse has income, children under 21 charged to the worker, and any disabled adult child.
6. **Self-employed, if relevant.** Category under Arrêté 2020-065, declared income, date of the first declaration and the CMU route.

Also useful, not required: prior DISA and DASC, and the CNPS statement. Without these answers, the affected items are Needs Input.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Loi 99-477, Code de Prévoyance Sociale, JO 2 September 1999, CNPS copy, OCR. Read: Arts 1 to 37 in full, Arts 66, 67, 70, 71, 164, 166, 167, 174. Arts 4 to 37, 71, 164, 166 and 167 checked on the page image. Later amendments other than Ord 2012-03 not established | https://www.cnps.ci/wp-content/uploads/2020/08/Loi-n%C2%B0-99-477-du-02-ao%C3%BBt-1999-portant-modification-du-Code-de-Pr%C3%A9voyance-Sociale-Amendment-to-the-Social-Security-Code.pdf | 2026-11-05 |
| Ordonnance 2012-03, unofficial copy on a private site with no gazette check. Read in part: Arts 22, 50, 95, 168 bis, 168 ter, and Arts 2, 3 of the ordonnance | https://loidici.biz/2018/08/26/ordonnance-n-2012-03-du-11-janvier-2012-modifiant-les-articles-22-50-95-149-a-163-ter-et-completant-larticle-168-de-la-loi-n-99-477-du-02-aout-1999-portant-modification-du-code-de-pr/lois-article-par-article/codes/le-code-de-prevoyance-sociale/1698/naty/ | 2026-11-05 |
| Conseil des ministres, 11 January 2012. Read in part: the retirement item | https://www.gouv.ci/uploads/publications/1372331568CCM_11_01_2012.pdf | 2026-11-05 |
| Conseil des ministres, 21 December 2022. Read in part: the SMIG item | https://www.gouv.ci/uploads/publications/1671692497Communique-du-Conseil-des-Ministres-du-mercredi-21-decembre-2022.pdf | 2026-11-05 |
| Conseil des ministres, 23 September 2026, Présidence. Read in part: the Code de Prévoyance Sociale item. Same text on gouv.ci | https://www.presidence.ci/communiques-ministres/communique-du-conseil-des-ministres-du-mercredi-23-septembre-2026/ | 2026-11-05 |
| CNPS, Employeur page, read in full. Administrative, and partly stale on SMIG and ceiling figures | https://www.cnps.ci/employeur | 2026-11-05 |
| CNPS Direction Générale, communiqué 'Nouveau plafond des cotisations sociales de la CNPS', January 2023, 1 page, read in full for the floor (75,000, all branches), the retirement ceiling (3,375,000) and the other-branch ceiling (75,000) from 1 January 2023 under Décret 2022-986. No later ceiling notice was found in the CNPS media library searched the same day | https://www.cnps.ci/wp-content/uploads/2023/01/NOUVEAU-PLAFOND-DES-COTISATIONS-SOCIALES-DE-LA-CNPS.pdf | 2026-11-14 |
| CNPS leaflet Recouvrement, edition 2021, read in full. Administrative | https://www.cnps.ci/wp-content/uploads/2021/04/RECOUVREMENT-R.pdf | 2026-11-05 |
| CNPS leaflet Recouvrement, edition 2018, read in full. Administrative. Layout read in columns | https://www.cnps.ci/wp-content/uploads/2020/08/Recouvrement.pdf | 2026-11-05 |
| CNPS, Indépendant page. Read in part: rates and cover. Administrative | https://www.cnps.ci/independant/ | 2026-11-05 |
| Ordonnance 2019-636, RSTI, CNPS copy, OCR. Read in part: Arts 2, 6 to 10, 12, 16, 23, 24, 27, 29 to 34 | https://www.cnps.ci/wp-content/uploads/2020/08/ORDON-N-%C2%A6-2019-636-DU-17-07-2019-TRAVAILLEUR-INDEP.pdf | 2026-11-05 |
| Décret 2020-308, RSTI, CNPS copy, JO 18 May 2020. Read in part: Arts 4 to 7 | https://www.cnps.ci/wp-content/uploads/2020/08/Decret-n-%C2%A62020-308-du-4-mars-2020-fixant-les-modalit%C3%A9s-de-fonctionnement-des-r%C3%A9gimes-de-pr%C3%A9voyance-sociale-des-travailleurs-2.pdf | 2026-11-05 |
| Arrêté 2020-065/MEPS/CAB, 16 July 2020, OCR, read in full. Arts 4 to 9 checked on the page image | https://www.cnps.ci/wp-content/uploads/2020/08/Arr%C3%AAt%C3%A9-revenu-plancher-RSTI.pdf | 2026-11-05 |
| CNPS Délibération 004 of 8 July 2024, DRA and payment, OCR, read in full. Arts 2 to 7 checked on the page image | https://www.cnps.ci/wp-content/uploads/2024/07/DELIBERATION-N%C2%B0-004-FIXANT-LES-MODALITES-PRATIQUES-DE-DECLARATION-DE-REVENU-DACTIVITE-DRA-ET-DE-PAIEMENT-DES-COTISATIONS-DES-TI.pdf | 2026-11-05 |
| Décret 2017-123, CMU, JO 30 May 2017, WHO copy, OCR, Arts 1 to 32 read in full and checked on the page images | https://extranet.who.int/cpcd/sites/default/files/public_file_repository/CIV_Cote-d-Ivoire_Decret-No-2017-123-fixant-le-montant-et-les-modalites-de-recouvrement-des-cotisations_2017.pdf | 2026-11-05 |
| Loi 2014-131, CMU, JO 10 April 2014, WHO copy, embedded text layer with OCR artefacts. Read in part: Arts 2, 3, 8, 26, 30 to 36, 39 to 42, 47 to 51, 53 to 56, 58 to 72. Arts 58 to 72 checked on the page image | https://extranet.who.int/cpcd/sites/default/files/public_file_repository/CIV_Cote-d_Ivoire-Law-No.131of2014_on-Instituting-Universal-Healthcare_2014.pdf | 2026-11-05 |
| Service-public.gouv.ci, CMU payment procedure. Read in part: the contribution section. Administrative | https://servicepublic.gouv.ci/accueil/detaildemarcheparticulier/2/189/14 | 2026-11-05 |
| CLEISS, French liaison body for social security conventions, table at 1 January 2025. Read in part: the contributions page. Secondary, not Ivorian | https://www.cleiss.fr/docs/cotisations/cotedivoire.html | 2026-11-05 |
| Abidjan.net (CICG), 14 March 2025, report of a CMU decree on the taxe communale de l'entreprenant. Read in full. Press report, not the decree | https://sports.abidjan.net/actualites/740147/cmu-taxe-communale-de-l-entreprenant-le-gouvernement-fixe-les-modalites-de-recouvrement-des-cotisations-dues-au-titre-du-regime-general-de-base | 2026-11-05 |

Not yet confirmed: the decree or decrees under Code Arts 21, 23 and 24 fixing the ceilings, split, assiette, due date, majorations and moratory interest, so the 75,000 and 3,375,000 ceilings of the CNPS communiqué, 45 times the SMIG, the 20-worker test, the 15-day date and 0.050% stay administrative; whether any CNPS notice after January 2023 changed the ceilings; the Ordonnance of 23 September 2026 (number, text, gazette, ratification), whether it touches Arts 12 to 23, and what CNPS has applied since the decision of 1 October 2025; an official copy of Ordonnance 2012-03; the text of the SMIG decree (Décret 2022-986, number from the CNPS communiqué), any SMIG decree after it, the hourly SMIG and the SMAG; the Art 95 annual minimum; the Art 17 risk arrêté, the 4 categories in legacy and the Art 15 tariff decree; the decree under Code Art 10 2° and whether its rate is separate from the 0.75%; the source of the 5% and 1% late rate that `ivory-coast-payroll` attributes to CLEISS; the Art 29 and Art 174 fines; the CNPS board decision under Art 26 on the 31 March date and the form; the RSTI penalty decree under Ordonnance 2019-636 Art 29; the fiscal transport exemption and housing scale; decrees under Code Arts 6 and 70 on voluntary cover; any amendment to Décret 2017-123, Décret 2020-308 or Arrêté 2020-065; a CMU spouse with income under Décret 2017-123 Art 9; the date a mid-year change of RSTI declared income takes effect; the reach of Code Art 33; the CMU decree on the taxe communale de l'entreprenant reported on 14 March 2025 and the joint arrêtés on CMU recovery; the CNPS and IPS-CNAM convention under Décret 2017-123 Art 13 and the CMU date for a quarterly payer; multiple-employer, part-month, part-time and part-year rules; any rounding rule; every social security convention; the income tax and TVA treatment, which the owning guides hold; and the date CMU collection began in practice, as Art 30 says 1 October 2017 whilst later sources give later dates; the Art 16 base row (annual minimum salary under Code Art 95, amount not read) was moved out of the rates table on 2026-11-14. The retirement ceiling row moved out the same day is back in the table, confirmed by the CNPS communiqué of January 2023.

## Changelog

| Version | Date | Change |
| --- | --- | --- |
| 0.5 | 2026-11-14 | Confirmed the retirement ceiling of 3,375,000 and the floor of 75,000 from the CNPS communiqué of January 2023 and restored the ceiling row. Corrected the other-branch ceiling from 70,000 to 75,000 (same communiqué), which ends the floor-and-ceiling conflict; reworked Examples 1, 2, 3 and the test table on 75,000. |
| 0.4 | 2026-11-14 | Declared type computation. Moved the two unverified rows (retirement ceiling 3,375,000; Art 16 base) out of the rates table to the Not yet confirmed line; worked examples still label 3,375,000 unverified. |
| 0.3 | 2026-11-05 | Converted to the upstream template. Corrected the late-payment penalty, which had wrongly used 10% under Art 30; moved the 31 March date from Art 26 to CNPS leaflets; removed the claim that Décret 2022-986 sets the ceiling; marked 3,375,000 unverified; made ceilings annual with regularisation; corrected the CMU rule beyond 6 children; corrected the RSTI ceiling and added RSTI, apprentice, assimilated and pay-item rules; added CMU's own penalties; removed the 2%, quarterly and single-person defaults; replaced the bank fallback with intake only. |
| 0.2 | 2026-11-01 | Legacy version. |

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an expert-comptable, CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
