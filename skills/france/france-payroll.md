---
name: france-payroll
description: Use this skill whenever asked about French payroll processing for employees. Trigger on phrases like "French payroll", "bulletin de paie", "fiche de paie", "prélèvement à la source", "PAS", "URSSAF cotisations", "cotisations sociales France", "CSG CRDS", "SMIC", "AGIRC-ARRCO", "retraite complémentaire", "DSN", "net imposable", "net à payer", "salaire brut net France", "charges patronales", "charges salariales", "PMSS", "plafond sécurité sociale", "minimum wage France", "congés payés", "13ème mois", "mutuelle obligatoire", or any question about computing employee pay, income tax withholding, or social contributions in France. This skill covers prélèvement à la source (PAS), URSSAF contributions, AGIRC-ARRCO, CSG/CRDS, mandatory benefits, payslip (bulletin de paie) requirements, DSN filing, and employer cost analysis. ALWAYS read this skill before processing any French employee payroll.
version: 1.0
jurisdiction: FR
tax_year: 2026
last_updated: 2026-10-19
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# French payroll: pay, contributions, PAS and DSN

How a French employer runs a monthly payroll for an employee: the social contributions taken from gross pay, the employer contributions on top, the single degressive relief that now sits over them, income tax withheld at source (prélèvement à la source), the mandatory payslip, and the monthly DSN filing. Figures are for tax year 2026. The income tax scale in Section 2 is the one applied in 2026 to income of 2025 declared in 2026; every other figure in this skill (the withholding grid, social contributions, the Smic, the ceilings and the payroll reliefs) is the one in force during 2026, and where a figure changed inside 2026 the row gives its start date. The rules on contributions and the DSN are those in force on 19 October 2026. The Smic rose on 1 June 2026, so this skill gives both the January value and the June value, and the default withholding grid shown is the one in force from 1 May 2026.

## Section 1: Quick Reference

| Field | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/plafonds-securite-sociale.html |
| Country | France (République française) | |
| Currency | EUR only | |
| Standard pay frequency | Monthly (mensuel), almost universal | |
| Tax year | Calendar year, 1 January to 31 December | |
| Income tax withholding | Prélèvement à la source, rate sent by DGFiP to the employer | |
| Social contribution authority | Urssaf, which collects for all branches | |
| Supplementary pension | Agirc-Arrco, one scheme since 2019 | |
| Tax authority | Direction générale des Finances publiques (DGFiP) | |
| Key legislation | Code de la Sécurité sociale; Code du travail; Code général des impôts art. 204 A to 204 M for the withholding | |
| Monthly social security ceiling (plafond mensuel, PMSS) | EUR 4,005 | "Mois 4 005 €" |
| Annual social security ceiling (PASS) | EUR 48,060 | "2026 Année 48 060 €" |
| Daily ceiling, used to prorate a part month | EUR 220 | "Jour 220 €" |
| Hourly ceiling | EUR 30 | "Heure 30 €" |
| Electronic declaration | DSN, filed on net-entreprises.fr | |
| Review status | Not yet reviewed by a French expert-comptable | |

Mayotte has its own ceiling and its own Smic. This skill covers mainland France and the overseas departments other than Mayotte unless a row says otherwise.

## Section 2: Income Tax Withholding (Prélèvement à la Source)

Since 1 January 2019 the employer withholds income tax from the employee's **net imposable** each month, declares it in the DSN and pays it to the tax administration. Every business that pays salaries taxable in France must collect and pay over the withholding, a foreign employer included.

### How PAS Works

| Step | Detail | Source |
| --- | --- | --- |
| Rate source | The tax office works out the personalised rate from the employee's own income tax return and sends it to the employer. The employee can see it in their space on impots.gouv.fr | https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 |
| When the rate changes | The personalised rate is changed every year in September, from the return filed in the spring | https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 |
| Married or PACS couples | A couple taxed jointly gets an individualised rate automatically. It applies only to each person's own income; income common to the household keeps the household rate | https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 |
| Rate change on request | A new rate applies at the latest in the third month after the request | https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 |
| Change of family situation | The employee must tell the tax administration within 60 days of a marriage, PACS, birth, adoption, death, divorce or end of a PACS | https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 |
| No personalised rate | Where the employee has never filed a return, the tax office applies a default rate set by a published grid on the monthly withholding base. See the grid below | https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 |
| Calculation | The rate is applied to the monthly withholding base (base mensuelle de prélèvement). On the payslip that base is the net taxable amount shown in zone 6 (Section 7) | https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 |
| Remittance | Paid to the tax administration (DGFiP), not to Urssaf, by a SEPA B2B direct debit entered in the financial block of the DSN. The bank account debited is the one the employer registered in its professional space on impots.gouv.fr, and the signed SEPA B2B mandate must reach the bank before the first payment | https://www.impots.gouv.fr/les-modalites-du-prelevement-la-source-0 |

The employer never works out the bands. It applies the rate it is given, or the default grid.

### Income Tax Brackets (2026, progressive scale for annual declaration)

This scale is what the tax office uses to set the rate. The employer does not use it. It is measured on taxable income per family-quotient share, not on gross salary.

| Taxable income per share | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://www.service-public.gouv.fr/particuliers/vosdroits/F1419 |
| Up to EUR 11,600 | 0% | "Jusqu'à 11 600 € 0 %" |
| EUR 11,601 to EUR 29,579 | 11% | "De 11 601 € à 29 579 € 11 %" |
| EUR 29,580 to EUR 84,577 | 30% | "De 29 580 € à 84 577 € 30 %" |
| EUR 84,578 to EUR 181,917 | 41% | "De 84 578 € à 181 917 € 41 %" |
| Above EUR 181,917 | 45% | "Plus de 181 917 € 45 %" |

These bands apply to the income of 2025 declared in 2026. A payroll run in 2026 does not use them.

### Taux Neutre (Default Rate Grid, 2026: Metropolitan France)

This is the grid in force from 1 May 2026 for taxpayers living in mainland France or outside France. It is read on the monthly withholding base, which is the net imposable for the month.

| Monthly withholding base | Default rate | Page wording |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/11255-PGP.html |
| Below EUR 1,635 | 0% | "Inférieure à 1 635 euros 0 %" |
| EUR 1,635 and below EUR 1,698 | 0.5% | "Supérieure ou égale à 1 635 euros et inférieure à 1 698 euros 0,5 %" |
| EUR 1,698 and below EUR 1,807 | 1.3% | "Supérieure ou égale à 1 698 euros et inférieure à 1 807 euros 1,3 %" |
| EUR 1,807 and below EUR 1,928 | 2.1% | "Supérieure ou égale à 1 807 euros et inférieure à 1 928 euros 2,1 %" |
| EUR 1,928 and below EUR 2,060 | 2.9% | "Supérieure ou égale à 1 928 euros et inférieure à 2 060 euros 2,9 %" |
| EUR 2,060 and below EUR 2,170 | 3.5% | "Supérieure ou égale à 2 060 euros et inférieure à 2 170 euros 3,5 %" |
| EUR 2,170 and below EUR 2,315 | 4.1% | "Supérieure ou égale à 2 170 euros et inférieure à 2 315 euros 4,1 %" |
| EUR 2,315 and below EUR 2,738 | 5.3% | "Supérieure ou égale à 2 315 euros et inférieure à 2 738 euros 5,3 %" |
| EUR 2,738 and below EUR 3,135 | 7.5% | "Supérieure ou égale à 2 738 euros et inférieure à 3 135 euros 7,5 %" |
| EUR 3,135 and below EUR 3,571 | 9.9% | "Supérieure ou égale à 3 135 euros et inférieure à 3 571 euros 9,9 %" |
| EUR 3,571 and below EUR 4,019 | 11.9% | "Supérieure ou égale à 3 571 euros et inférieure à 4 019 euros 11,9 %" |
| EUR 4,019 and below EUR 4,690 | 13.8% | "Supérieure ou égale à 4 019 euros et inférieure à 4 690 euros 13,8 %" |
| EUR 4,690 and below EUR 5,624 | 15.8% | "Supérieure ou égale à 4 690 euros et inférieure à 5 624 euros 15,8 %" |
| EUR 5,624 and below EUR 7,037 | 17.9% | "Supérieure ou égale à 5 624 euros et inférieure à 7 037 euros 17,9 %" |
| EUR 7,037 and below EUR 8,789 | 20% | "Supérieure ou égale à 7 037 euros et inférieure à 8 789 euros 20 %" |
| EUR 8,789 and below EUR 12,200 | 24% | "Supérieure ou égale à 8 789 euros et inférieure à 12 200 euros 24 %" |
| EUR 12,200 and below EUR 16,523 | 28% | "Supérieure ou égale à 12 200 euros et inférieure à 16 523 euros 28 %" |
| EUR 16,523 and below EUR 25,937 | 33% | "Supérieure ou égale à 16 523 euros et inférieure à 25 937 euros 33 %" |
| EUR 25,937 and below EUR 55,558 | 38% | "Supérieure ou égale à 25 937 euros et inférieure à 55 558 euros 38 %" |
| EUR 55,558 and above | 43% | "Supérieure ou égale à 55 558 euros 43 %" |

Guadeloupe, La Reunion and Martinique have their own grid, and Guyane and Mayotte a third grid. Both are on the same page as the table above. Do not apply the mainland grid to an employee living in those territories.

**Short contracts: the abattement**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/11255-PGP.html |
| Monthly net taxable Smic at 1 June 2026, the basis of the abattement | EUR 1,531.12 | "Le montant mensuel net imposable du salaire minimum de croissance s’élève, au 1 er juin 2026, à 1 531,12 euros." |
| Abattement applied to a short contract before the default grid is read | EUR 766 | "est égal à 766 euros (1 531,12 / 2)" |

## Section 3: Social Security: Employee Deductions (2026)

### URSSAF Contributions (Employee Share)

| Contribution | Employee rate | Base and page wording |
| --- | --- | --- |
| Source | all figures below | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html |
| Vieillesse deplafonnee (old age, uncapped) | 0.40% | Total gross. "Assurance vieillesse 0,40 % sur la totalité et 6,90 % dans la limite du plafond" |
| Vieillesse plafonnee (old age, capped) | 6.90% | Up to the monthly ceiling. "0,40 % sur la totalité et 6,90 % dans la limite du plafond" |
| CSG non imposable (deductible from taxable pay) | 6.80% | "CSG non imposable 6,80 % sur 98,25 % du salaire brut dans la limite de 192 240 € en 2026" |
| CSG imposable (not deductible) | 2.40% | "CSG imposable 2,40 % sur 98,25 % du salaire brut dans la limite de 192 240 € en 2026" |
| CRDS | 0.50% | "CRDS 0,50 % sur 98,25 % du salaire brut dans la limite de 192 240 € en 2026" |
| Extra employee health contribution, Haut-Rhin, Bas-Rhin and Moselle only | 1.30% | "Moselle 1,30 %" |

The employee table on that page carries no general health contribution and no unemployment contribution. Do not enter a rate for either.

**The CSG and CRDS base**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/csg-crds.html |
| CSG rate on earned income, the two employee lines added by the page | 9.20% | "ce taux est de : 9,20 % pour la CSG ; 0,50 % pour la CRDS" |
| CRDS rate on earned income | 0.50% | "9,20 % pour la CSG ; 0,50 % pour la CRDS" |
| Allowance for professional costs taken off the base | 1.75% | "elle est généralement réduite de 1,75 % au titre des frais professionnels" |
| Share of earned income that is therefore charged | 98.25% | "les CSG-CRDS sont calculées sur 98,25 % des revenus d’activité" |
| Limit beyond which the allowance stops | Four annual social security ceilings. The amount is in the employee table above | "La réduction de 1,75 % ne s’applique toutefois que dans la limite de 4 plafonds annuels de la Sécurité sociale" |
| Employee health contribution where the person is not tax resident in France but is in the French health scheme | 5.50% | "Cette cotisation, au taux de 5,50 %, est à déclarer" |

Conditions that change the answer. The allowance is taken off only up to four annual ceilings; above that the charge is on the whole amount. The employer's contribution to the company health cover is itself charged to CSG and CRDS with no allowance. The charges are due only where the person is resident in France for income tax **and** is covered by a compulsory French health scheme: if only the health test is met, the charges are not due and an employee health contribution is due instead, at the rate in the table above.

### AGIRC-ARRCO (Supplementary Pension: Employee Share)

| Contribution | Employee rate | Base and page wording |
| --- | --- | --- |
| Source | all figures below | https://www.service-public.gouv.fr/particuliers/vosdroits/F15396 |
| Retraite complementaire, tranche 1 | 3.15% | Annual pay up to EUR 48,060. "7,87 % (part salariale : 3,15 % / part patronale : 4,72 % )" |
| Retraite complementaire, tranche 2 | 8.64% | Annual pay between EUR 48,060 and EUR 384,480. "21,59 % (part salariale : 8,64 % / part patronale : 12,95 % )" |
| Combined rate, tranche 1 | 7.87% | "7,87 % (part salariale : 3,15 % / part patronale : 4,72 % )" |
| Combined rate, tranche 2 | 21.59% | "21,59 % (part salariale : 8,64 % / part patronale : 12,95 % )" |
| Rate used to buy pension points, tranche 1 | 6.20% | "Tranche 1 : jusqu'à 48 060 € 6,20 % 20,1877 €" |
| Rate used to buy pension points, tranche 2 | 17% | "Tranche 2 : entre 48 060 € et 384 480 € 17 %" |
| Price of one pension point in 2026 | EUR 20.1877 | "6,20 % 20,1877 €" |

The rate charged and the rate that buys points are different rates. Points are bought at the point rates in the table, not at the contribution rates: the difference funds the scheme and buys nothing. Tranche 2 stops at the ceiling in the table, which is eight annual ceilings.

**CEG and CET (employee share)**

| Contribution | Employee rate | Base and page wording |
| --- | --- | --- |
| Source | all figures below | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-particuliers.html |
| CEG, tranche 1 | 0.86% | "Contribution d'équilibre générale (CEG) tranche 1 (3) 0,86 % dans la limite du plafond" |
| CEG, tranche 2 | 1.08% | "CEG tranche 2 : 1,08 % part salariale et 1,62 % en part patronale" |
| CET | 0.14% | "Part salariale à 0,14 % et part patronale à 0,21 %" |

The CET condition is easy to get wrong. The page says the CET applies to every employee whose pay is above the social security ceiling, and that it is charged from the first euro, not only on the slice above the ceiling. The page that prints these three rates is the Urssaf rates page for household employers; the general CEG tranche 1 employee rate is confirmed on the Urssaf page for the overtime relief, at https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/exonerations-heures/reduction-cotisations-salariales.html

### Chômage (Unemployment: Employee Share)

There is no employee unemployment contribution. The Urssaf employee rate table for the private sector lists none, and the Urssaf page on the unemployment and AGS contributions says they are due by employers: https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/assurance-chomage-ags.html Enter nothing for the employee.

### Total Employee Deductions (Approximate)

No official page prints a single total for employee deductions, so this skill does not state one. Add the lines in the tables above that apply to the employee, then apply the overtime relief below where overtime was worked.

**Relief on overtime (employee share)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/exonerations-heures/reduction-cotisations-salariales.html |
| Reduction of employee old-age contributions on overtime and complementary hours, capped | 11.31% | "dans la limite de 11,31 %" |
| Employee old-age contributions inside that cap | 7.30% | "7,30 % (cotisations salariales vieillesse dont 0,40 % sur la totalité de la rémunération et 6,90 % dans la limite du plafond)" |
| Agirc-Arrco tranche 1 employee contribution inside that cap | 3.15% | "3,15 % (cotisations salariales de retraite complémentaire sur la tranche 1 (= plafond))" |
| CEG tranche 1 employee contribution inside that cap | 0.86% | "0,86 % (contribution d’équilibre général (CEG) sur la tranche 1 (= plafond))" |

The relief is a reduction of the employee's old-age contributions on the overtime pay only. It is not an exemption from CSG or CRDS. The reduction must appear on the payslip.

## Section 4: Social Security: Employer Contributions (2026)

### URSSAF Contributions (Employer Share)

| Contribution | Employer rate | Base and page wording |
| --- | --- | --- |
| Source | all figures below | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html |
| Maladie, maternite, invalidite, deces, full rate | 13% | Total gross. "Taux réduit à 7 % Taux plein à 13 %" |
| Maladie, reduced rate, only in the cases in the note below the table | 7% | "Taux réduit à 7 % Taux plein à 13 %" |
| Pay condition for the reduced 7% maladie rate, where the employer qualifies at all, on https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html | Annual pay at or below 2.5 times the Smic in force on 31 December 2023, a frozen Smic, not the current one | "le taux de la cotisation d’assurance maladie sera de 7 % si la rémunération annuelle du salarié est inférieure ou égale à 2,5 fois le Smic en vigueur au 31/12/2023" |
| Contribution solidarite autonomie (CSA) | 0.30% | Total gross. "Contribution solidarité autonomie (CSA) 0,30 %" |
| Vieillesse deplafonnee | 2.11% | Total gross. "Assurance vieillesse 2,11 % sur la totalité et 8,55 % dans la limite du plafond" |
| Vieillesse plafonnee | 8.55% | Up to the monthly ceiling. "2,11 % sur la totalité et 8,55 % dans la limite du plafond" |
| Allocations familiales, full rate | 5.25% | Total gross. "Allocations familiales Taux réduit à 3,45 % Taux plein à 5,25 %" |
| Allocations familiales, reduced rate, only in the cases in the note below the table | 3.45% | "Taux réduit à 3,45 % Taux plein à 5,25 %" |
| Pay condition for the reduced 3.45% allocations familiales rate, where the employer qualifies at all, on https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html | Annual pay at or below 3.5 times the Smic in force on 31 December 2023, a frozen Smic, not the current one | "le taux de la cotisation d’allocations familiales sera de 3,45 % si la rémunération annuelle du salarié est inférieure ou égale à 3,5 fois le Smic en vigueur au 31/12/2023" |
| Contribution au dialogue social | 0.016% | Total gross. "Contribution au dialogue social 0,016 %" |
| Fnal, employer with fewer than 50 employees | 0.10% | Up to the monthly ceiling. "Fnal (effectif de moins de 50 salariés) 0,10 % dans la limite du plafond" |
| Fnal, employer with 50 employees or more | 0.50% | Total gross. "Fnal (effectif de 50 salariés et plus) 0,50 %" |
| Contribution formation professionnelle, fewer than 11 employees | 0.55% | "Pour une entreprise de moins de 11 salariés : 0,55 %" |
| Contribution formation professionnelle, 11 employees or more | 1% | "Pour une entreprise de 11 salariés et plus : 1 %" |
| Contribution CPF-CDD, on fixed-term contract pay | 1% | "Contribution CPF-CDD 1 %" |
| Taxe d'apprentissage, main part | 0.59% | "Taxe d'apprentissage Part principale à 0,59 % Solde à 0,09 %" |
| Taxe d'apprentissage, balance | 0.09% | "Part principale à 0,59 % Solde à 0,09 %" |
| Taxe d'apprentissage, establishments in Haut-Rhin, Bas-Rhin and Moselle, main part, no balance due | 0.44% | "Part principale à 0,44 % Solde - Néant" |
| Accident du travail (AT/MP) | Rate notified to the employer by the Carsat | "Accident du travail Taux notifié par la Carsat" |
| Versement mobilite, employer with 11 employees or more | Rate set locally, look it up with the Urssaf search tool | "Versement mobilité (effectif de 11 salariés et plus)" |

There is no published national range for the AT/MP rate. Use the rate on the Carsat notification for the establishment and nothing else.

**Two official pages disagree about the reduced maladie and allocations familiales rates.** The Urssaf rates page above prints them as if they were ordinary alternatives. The Urssaf page on what changed for 2026 says that from 2026 the reduced rates were withdrawn and merged into the single degressive relief below, and survive only for employers using a zoned exemption (ZRR and ZFRR, ZRD, ZFU), the overseas Lodeom exemption, or the exemption for home-help staff placed with a fragile person, and for employees in certain special schemes for whom the single relief is not available. That page is at https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html Where the two conflict, do not assume the reduced rate applies to an ordinary private employer. The same page gives the pay condition, and it is measured against the Smic frozen at 31 December 2023, so it does not move when the Smic rises.

### Réduction Générale Dégressive Unique (RGDU)

New for 2026 and the largest single item in French employer cost. The old degressive relief and the reduced maladie and allocations familiales rates were merged into one relief.

| Item | Value | Page wording |
| --- | --- | --- |
| Source | all figures below unless a row names another page | https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html |
| Pay ceiling for eligibility, at the Smic in force on 1 January 2026 | 3 Smic | "a une rémunération inférieure : à 3 Smic applicable au 1 er janvier 2026" |
| Same ceiling expressed against the Smic in force on 1 June 2026 | 2.9293 Smic | "(ou 2,9293 Smic applicable au 1 er juin 2026)" |
| Smic value that governs the 2026 coefficient, mainland and overseas departments other than Mayotte | The Smic in force on 1 January 2026 | "En 2026, la valeur du Smic à prendre en compte est celle en vigueur au 1 er janvier 2026" |
| Official worked example: employer with 70 employees, June 2026, full-time 35 hours, no overtime, monthly gross pay EUR 2,000 | Coefficient 0.3178 | "une rémunération mensuelle brute de 2 000 €, la valeur maximale du coefficient de réduction générale est de 0,3178" |
| Pay ceiling in Mayotte | 1.6 Smic | "à 1,6 Smic applicable à Mayotte en 2026" |
| What the Urssaf 2026-news page (informations-nouvelle-annee.html) says the 3-Smic ceiling replaced | 1.6 Smic, the pre-2026 figure | "qui sont inférieurs à 3 Smic en vigueur au lieu de 1,6 Smic auparavant" |
| What entreprendre.service-public.fr F559, Vérifié le 01 juin 2026, still prints for the general relief | Below 1.6 Smic, EUR 2,987.23 | "Allègements généraux dont bénéficient les employeurs au titre des salariés dont les rémunérations brutes sont inférieures à 1,6 Smic ( 2 987,23 € )" |
| What the same F559 page prints for the allocations familiales rate reduction, measured against the current Smic rather than the frozen Smic that governs the rate in Section 4 | Below 3.5 Smic, EUR 6,534.56, which is 3.5 times the June 2026 Smic | "Réduction du taux de cotisations allocations familiales, dont bénéficient les employeurs au titre des salariés dont les rémunérations brutes sont inférieures à 3,5 Smic ( 6 534,56 € )" |
| Maladie rate covered by the relief | 13.00% | "d’assurances sociales (maladie, maternité, invalidité, décès) au taux de 13,00 %" |
| Vieillesse rate covered | 10.66% | "de vieillesse au taux de 10,66 %" |
| Allocations familiales rate covered | 5.25% | "d’allocations familiales au taux de 5,25 %" |
| AT/MP rate covered, capped at the pooled part | 0.49% | "pour sa partie mutualisée au taux de 0,49 %" |
| Agirc-Arrco rate covered | 6.01% | "de retraite complémentaire légalement obligatoire (Agirc-Arrco) au taux de 6,01 %" |
| Fnal rate covered, employer with fewer than 50 employees | 0.10% | "de fonds national d’aide au logement (Fnal) au taux de 0,10 % pour les entreprises de moins de 50 salariés" |
| Fnal rate covered, employer with 50 employees or more | 0.50% | "ou 0,50 % pour les entreprises de 50 salariés et plus ; de solidarité pour l’autonomie" |
| CSA rate covered | 0.30% | "de solidarité pour l’autonomie (CSA) au taux de 0,30 %" |
| Unemployment rate covered | 4.00% | "d’assurance chômage au taux de 4,00 %" |

Two official pages give different ceilings for the general relief. entreprendre.service-public.gouv.fr/vosdroits/F559, Vérifié le 01 juin 2026, still prints 1.6 Smic and EUR 2,987.23. The Urssaf relief and 2026 news pages give 3 Smic, and the news page says the 3 Smic figure replaced 1.6 Smic. Both are in the table above. The Urssaf pages are the ones that describe the 2026 reform by name, but do not treat that as settled without checking the client's own Urssaf account.

The same F559 page's allocations familiales figure is a second instance of the same problem, not a fresh one: the amount in the row above is 3.5 times the Smic in force on 1 June 2026, while the pay condition for the reduced 3.45% rate above is measured against the Smic frozen at 31 December 2023. F559 has not been updated for the 2026 freeze, the same way it has not been updated for the 1.6-to-3-Smic change. Use the frozen-Smic test in the row above for the reduced rate; treat the F559 figure as the stale, pre-freeze measurement.

**Coefficient parameters**

| Item | Employer with fewer than 50 employees | Employer with 50 employees or more |
| --- | --- | --- |
| Source | all figures below | https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html |
| T min | 0.0200 | 0.0200 |
| T delta | 0.3781 | 0.3821 |
| Maximum coefficient | 0.3981 | 0.4021 |
| Exponent P | 1.75 | 1.75 |

The formula on the Urssaf pages is: coefficient equals T min plus T delta multiplied by the bracketed term raised to the exponent P, where the bracketed term is one half multiplied by (three times the annual Smic, the Smic being increased by the hourly Smic times the number of overtime or complementary hours, divided by annual gross pay, minus one). The relief page says the Smic value may be adjusted for part-time work, a collective working time below the legal one, and suspensions of the contract. For mainland France and the overseas departments other than Mayotte, the Smic to use for the whole of 2026 is the Smic in force on 1 January 2026, so the June rise does not move the relief. The relief page allows the same result with 2.9293 times the annual Smic at its 1 June 2026 value instead of 3 times the January value. The relief page says the Bulletin officiel de la Sécurité sociale (Boss) allows an employer not to apply these formulas to pay of employees whose contract ended between 1 and 30 June 2026, but they apply to the whole of 2026 for every employee still under contract on 1 July 2026. Only in Mayotte are the Smic rises taken into account. Annual gross pay includes a prime de partage de la valeur where one was paid, both for the eligibility test and for the coefficient.

**Employer relief on overtime**

| Item | Value | Page wording |
| --- | --- | --- |
| Source | all figures below | https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html |
| Flat employer deduction per overtime hour, employer with fewer than 20 employees | EUR 1.50 | "1,50 € pour les employeurs dont l’effectif est inférieur à 20 salariés" |
| Flat employer deduction per overtime hour, employer with 20 employees or more | EUR 0.50 | "0,50 € par heure supplémentaire pour les employeurs d’au moins 20 salariés" |

From 1 January 2026 the old headcount limit for this deduction was removed, so every employer eligible for the single relief can claim it whatever its size. It also covers days bought back from an employee on a forfait-jours contract above the cap of 218 days.

### AGIRC-ARRCO (Employer Share)

| Contribution | Employer rate | Base and page wording |
| --- | --- | --- |
| Source | all figures below | https://www.service-public.gouv.fr/particuliers/vosdroits/F15396 |
| Retraite complementaire, tranche 1 | 4.72% | Annual pay up to EUR 48,060. "7,87 % (part salariale : 3,15 % / part patronale : 4,72 % )" |
| Retraite complementaire, tranche 2 | 12.95% | Annual pay between EUR 48,060 and EUR 384,480. "21,59 % (part salariale : 8,64 % / part patronale : 12,95 % )" |

| Contribution | Employer rate | Base and page wording |
| --- | --- | --- |
| Source | all figures below | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-particuliers.html |
| CEG, tranche 1 | 1.29% | "Contribution d'équilibre générale (CEG) tranche 1 (3) 1,29 % dans la limite du plafond" |
| CEG, tranche 2 | 1.62% | "CEG tranche 2 : 1,08 % part salariale et 1,62 % en part patronale" |
| CET | 0.21% | "Part salariale à 0,14 % et part patronale à 0,21 %" |
| Employer share of the Agirc-Arrco contribution, on https://entreprendre.service-public.gouv.fr/vosdroits/F24013 | 60% | "60 % par l'employeur et 40 % par le salarié" |
| Employee share of the Agirc-Arrco contribution, on https://entreprendre.service-public.gouv.fr/vosdroits/F24013 | 40% | "60 % par l'employeur et 40 % par le salarié" |

The same warning as on the employee table applies here. The only allowed page that prints the employer CEG tranche 2 and CET rates is the Urssaf rates page for household employers, in a footnote that states the Agirc-Arrco rules generally. The private-sector rates page prints neither. Confirm the tranche 2 and CET rates against the Agirc-Arrco circular before signing. The 60/40 Agirc-Arrco employer/employee split is confirmed separately, for all private-sector employees and not just household employees, on entreprendre.service-public.gouv.fr/vosdroits/F24013, which is a better source for that split than the household-employer page.

An Apec contribution is also due for cadres. No allowed official page prints its rate: entreprendre.service-public.gouv.fr/vosdroits/F24013 names "Cotisation Apec (pour les cadres uniquement)" without giving one, which is the evidence for that. This skill does not state one.

### Unemployment and Other Employer-Only

| Contribution | Employer rate | Base and page wording |
| --- | --- | --- |
| Source | all figures below | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html |
| Assurance chomage | 4.00% | "Contribution assurance chômage 4,00 % dans la limite de 192 240 € en 2026" |
| Annual pay ceiling for the unemployment and AGS contributions | EUR 192,240 | "dans la limite de 192 240 € en 2026" |
| AGS | 0.25% | "Dans la limite de 192 240 € en 2026 : 0,25 %" |
| AGS, temporary work agencies | 0.03% | "0,03 % pour les entreprises de travail temporaire" |

| Contribution | Employer rate | Page wording |
| --- | --- | --- |
| Source | all figures below | https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html |
| Employer contribution on the part of a rupture conventionnelle or forced retirement payment that is outside the contribution base, for a contract whose end falls after 1 January 2026 | 40% | "Le taux de cette contribution patronale passe de 30 % à 40 %" |

### Total Employer Cost (Approximate)

No official page prints a single percentage for total employer cost, so this skill does not state one. Build the cost from the tables above, then deduct the single degressive relief. For pay at or near the Smic the relief cancels most of the employer social cost, and it runs out at the pay ceiling in the relief table.

## Section 5: Minimum Wage and Overtime

### SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026)

The minimum wage changed inside the year. Use the value in force on the day the work was done.

| Item | Value | Page wording |
| --- | --- | --- |
| Source | all figures below | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/montant-smic.html |
| Gross hourly, 1 January 2026 to 31 May 2026 | EUR 12.02 | "Smic horaire brut 12,02 € 12,31 €" |
| Gross monthly on a 35 hour week, 1 January 2026 to 31 May 2026 | EUR 1,823.03 | "Du 1 er janvier 2026 au 31 mai 2026 Smic horaire brut 12,02 € Smic brut mensuel (base 35 heures par semaine) 1 823,03 €" |
| Gross hourly from 1 June 2026 | EUR 12.31 | "Smic horaire brut 12,02 € 12,31 €" |
| Gross monthly on a 35 hour week from 1 June 2026 | EUR 1,867.02 | "Au 1 er juin 2026 Smic horaire brut 12,31 € Smic brut mensuel (base 35 heures par semaine) 1 867,02 €" |
| Gross hourly from 1 June 2026, employee aged 17 to 18 without six months in the trade | EUR 11.08 | "Smic horaire brut 10,82 € 11,08 €" |
| Gross hourly from 1 June 2026, employee under 17 without six months in the trade | EUR 9.85 | "Smic horaire brut 9,62 € 9,85 €" |

| Item | Value | Page wording |
| --- | --- | --- |
| Source | all figures below | https://www.urssaf.fr/accueil/actualites/augmentation-smic.html |
| Gross hourly in Mayotte from 1 June 2026 | EUR 9.56 | "le Smic horaire brut est porté à 9,56 € soit un montant mensuel brut de 1 449,93 €" |
| Minimum garanti from 1 June 2026 | EUR 4.35 | "Le minimum garanti s'établit à 4,35 €" |

Conditions. The reduced youth rates apply only to an employee under 18 who does not yet have six months of practice in the trade. A collective agreement rate that is higher than the Smic wins. The Smic covers mainland France, Guadeloupe, Guyane, Martinique, La Reunion, Saint-Barthelemy, Saint-Martin and Saint-Pierre-et-Miquelon; Mayotte has its own rate. The June 2026 rise came from the ministerial order of 22 May 2026. No allowed page states the automatic revaluation trigger, so this skill does not state one: check the Urssaf page before each run.

Net monthly pay at the Smic is not published as a figure on any allowed page and has been removed from this skill. The monthly net **taxable** Smic at 1 June 2026 is published, in the short-contract table in Section 2.

### Working Hours and Overtime

| Rule | Value | Page wording |
| --- | --- | --- |
| Source | all figures below | https://www.service-public.gouv.fr/particuliers/vosdroits/F1911 |
| Legal weekly hours (duree legale) | 35 hours per week | "35 heures par semaine" |
| Legal monthly hours | 151.67 hours | "151,67 heures par mois" |
| Legal annual hours | 1,607 hours | "1 607 heures par an" |
| Maximum daily working time | 10 hours | "ne doit pas dépasser la durée maximale de 10 heures par jour" |
| Maximum daily working time where activity rises or the business needs it | 12 hours | "la durée maximale quotidienne de travail est limitée à 12 heures par jour" |
| Maximum in a single week | 48 hours | "Soit 48 heures sur une même semaine" |
| Maximum average over 12 consecutive weeks | 44 hours | "Soit 44 heures par semaine en moyenne sur une période de 12 semaines consécutives" |

| Rule | Value | Page wording |
| --- | --- | --- |
| Source | all figures below | https://www.service-public.gouv.fr/particuliers/vosdroits/F2391 |
| Overtime premium, first 8 overtime hours in the week, 36th to 43rd hour, where no collective agreement sets a rate | 25% | "25 % pour les 8 premières heures supplémentaires travaillées dans la même semaine (de la 36 e à la 43 e heure)" |
| Overtime premium, hours after that, from the 44th hour, where no collective agreement sets a rate | 50% | "50 % pour les heures suivantes (à partir de la 44 e heure)" |
| Floor for any premium rate set by a collective agreement | 10% | "Chaque taux est au minimum fixé à 10 %" |
| Part-time complementary hours, within one tenth of the contract hours | 10% | "Soit 10 % pour chaque heure complémentaire accomplie dans la limite de 1/10 e" |
| Part-time complementary hours, beyond one tenth | 25% | "Soit 25 % pour chaque heure accomplie au-delà de 1/10 e" |
| Annual overtime quota where no collective agreement sets one | 220 hours | "le nombre maximal d'heures supplémentaires est de 220 heures par salarié et par an" |

Conditions that change the answer. The premiums above are the fallback. Where a collective agreement, a company agreement or an extended branch agreement sets rates, those rates apply and only the floor above binds them. Overtime is counted by calendar week. Where working time is counted by the week or over two weeks, paid leave taken in that period counts as time worked for the overtime count, so the hours the employee would have worked count towards the threshold. Pay for overtime can be replaced in whole or in part by equivalent compensatory rest, and the rest must equal the premium-inclusive pay. The annual quota is also set by agreement first, and the figure above applies only where none of the three kinds of agreement exists.

## Section 6: Mandatory Benefits

### Congés Payés (Paid Annual Leave)

| Entitlement | Value | Page wording |
| --- | --- | --- |
| Source | all figures below | https://www.service-public.gouv.fr/particuliers/vosdroits/F2258 |
| Accrual per month of actual work | 2.5 working days | "ouvre droit à un congé de 2,5 jours ouvrables" |
| Full year | 30 working days, five weeks | "30 jours ouvrables (5 semaines) pour une année complète de travail" |
| Accrual during sick leave that is not work related | 2 working days per month, 24 a year | "dans la limite de 2 jours ouvrables par mois (soit 24 jours ouvrables par an)" |
| Reference period | 1 June of year N-1 to 31 May of year N, unless an agreement sets another | "du 1 er juin de l'année N-1 au 31 mai de l'année N" |
| Main leave period | 1 May to 31 October | "du 1 er mai au 31 octobre de l'année en cours" |
| Leave that must be taken in the main period to earn fractionnement days | 12 working days, two weeks | "un congé d'au moins 12 jours ouvrables (soit 2 semaines)" |

A part-day of accrued leave is rounded up to the next whole day. The fractionnement rules themselves are set by the collective agreement.

### Sick Leave (Arrêt Maladie)

| Item | Value | Page wording |
| --- | --- | --- |
| Source | all figures below | https://www.service-public.gouv.fr/particuliers/vosdroits/F3053 |
| Daily allowance from the health scheme | 50% of the daily base salary | "Les indemnités journalières (IJ) sont égales à 50 % du salaire journalier de base" |
| Daily base salary for a monthly paid employee | The last three gross salaries before the stoppage, divided by 91.25 | "au total des 3 derniers salaires bruts perçus avant l'arrêt de travail, divisé par 91,25" |
| Pay taken into account, capped | 1.4 times the Smic in force on the last day of the month before the stoppage. The page states the 2026 cap as EUR 2,613.82 a month, which is built on the Smic in force from 1 June 2026, so it governs a stoppage beginning on or after 1 July 2026 | "est plafonné à 1,4 fois le montant du Smic en vigueur, lors du dernier jour du mois qui précède l'arrêt (soit 2 613,82 € par mois en 2026)" |
| Cap for a stoppage that began before 1 April 2025 | 1.8 times the Smic, the old ceiling | "Pour les arrêts ayant débuté avant le 1ᵉʳ avril 2025, l’ancien plafond reste applicable" |
| Maximum daily allowance | EUR 42.97 | "Les IJ ne peuvent pas dépasser 42,97 € bruts" |
| Waiting period before the allowance starts | 3 days | "Les IJ sont versées après un délai de carence de 3 jours" |

**Employer top-up (indemnites complementaires)**

| Seniority | Maximum period paid | Page wording |
| --- | --- | --- |
| Source | all figures below | https://www.service-public.gouv.fr/particuliers/vosdroits/F3053 |
| 1 to 5 years | 60 days: 30 days at 90% then 30 days at 66.66% | "De 1 à 5 ans 60 jours (30 jours à 90 % et 30 jours à 66,66 % )" |
| 6 to 10 years | 80 days: 40 days at 90% then 40 days at 66.66% | "De 6 à 10 ans 80 jours (40 jours à 90 % et 40 jours à 66,66 % )" |
| 11 to 15 years | 100 days: 50 days at 90% then 50 days at 66.66% | "De 11 à 15 ans 100 jours (50 jours à 90 % et 50 jours à 66,66 % )" |
| 16 to 20 years | 120 days: 60 days at 90% then 60 days at 66.66% | "De 16 à 20 ans 120 jours (60 jours à 90 % et 60 jours à 66,66 % )" |
| 21 to 25 years | 140 days: 70 days at 90% then 70 days at 66.66% | "De 21 à 25 ans 140 jours (70 jours à 90 % et 70 jours à 66,66 % )" |
| 26 to 30 years | 160 days: 80 days at 90% then 80 days at 66.66% | "De 26 à 30 ans 160 jours (80 jours à 90 % et 80 jours à 66,66 % )" |
| 31 years and more | 180 days: 90 days at 90% then 90 days at 66.66% | "31 ans et plus 180 jours (90 jours à 90 % et 90 jours à 66,66 % )" |
| Waiting period before the employer top-up starts, every stoppage | 7 days, so the top-up begins on the 8th day | "Ainsi le versement des indemnités complémentaires commence au 8 e jour de l'arrêt maladie sauf dispositions conventionnelles" |

Conditions. The top-up needs at least one year of service at the first day of absence, and the medical certificate must reach **the employer** within 48 hours. Two different waiting periods run at once and must not be confused: three days on the health scheme allowance and seven days on the employer top-up, the top-up beginning on the eighth day unless a collective agreement is more favourable. There is no waiting period on the health scheme allowance where there was a return to work between two stoppages and that return did not exceed 48 hours ("reprise d'activité entre 2 arrêts de travail n'ayant pas dépassé 48 heures"), or where the stoppages follow an affection de longue duree. Where the stoppage follows a work accident or an occupational illness, the allowance runs from the first day of absence. Periods already paid in the previous twelve months reduce what is left. The Smic used for the cap is the one in force on the last day of the month before the stoppage. A stoppage beginning in June 2026 still takes the last day of May, which is inside the January to May Smic period, so its cap is 1.4 times the January 2026 monthly Smic in the Smic table in Section 5, not the monthly cap printed in the table above. No allowed page prints that January-based cap as an amount, so work it from the two figures and show the working. Only a stoppage beginning on or after 1 July 2026 takes the printed cap.

### Maternity Leave (Congé de Maternité)

| Case | Duration | Page wording |
| --- | --- | --- |
| Source | all figures below | https://www.service-public.gouv.fr/particuliers/vosdroits/F2265 |
| First child | 6 weeks before, 10 weeks after, 16 weeks in total | "1 er enfant 6 semaines 10 semaines 16 semaines" |
| Second child | 6 weeks before, 10 weeks after, 16 weeks in total | "2 e enfant 6 semaines 10 semaines 16 semaines" |
| Third child or more | 8 weeks before, 18 weeks after, 26 weeks in total | "3 e enfant ou plus 8 semaines 18 semaines 26 semaines" |
| Twins | 12 weeks before, 22 weeks after, 34 weeks in total | "2 12 semaines 22 semaines 34 semaines" |
| Three or more babies | 24 weeks before, 22 weeks after, 46 weeks in total | "3 ou plus 24 semaines 22 semaines 46 semaines" |

The count for a first or second child is by the number of children already dependent before the birth, not by birth order alone. The employee may give up part of the leave but must stop work for at least eight weeks, six of them after the birth. Pay during the leave comes from the health scheme as daily maternity allowances; the contract is suspended and the employer pays no salary unless an agreement says otherwise. No allowed page prints a cap for the maternity allowance, so this skill does not state one. After the maternity leave the employee may take the congé supplémentaire de naissance; its length and pay are on its own service-public page and are not covered here.

### Paternity Leave (Congé de Paternité)

| Item | Duration | Page wording |
| --- | --- | --- |
| Source | all figures below | https://www.service-public.gouv.fr/particuliers/vosdroits/F3156 |
| Conge de naissance, which must come first | 3 working days | "précédé du congé de naissance d'une durée de 3 jours ouvrables" |
| Conge de paternite et d'accueil de l'enfant, one child | 25 calendar days | "La durée du congé de paternité et d'accueil de l'enfant est de 25 jours calendaires" |
| Conge de paternite et d'accueil de l'enfant, more than one child | 32 calendar days | "La durée du congé de paternité et d'accueil de l'enfant est de 32 jours calendaires" |
| Period the employee must take straight after the conge de naissance | 4 calendar days | "il doit prendre la 1 re période de 4 jours calendaires" |

The leave must be taken within six months of the birth or arrival of the child. After it the employee may take the congé supplémentaire de naissance; its length and pay are on its own service-public page and are not covered here.

### 13th Month (Treizième Mois)

No statutory obligation. It is common under collective agreements or company policy. Where it is contractual it is pay: it bears all contributions and it goes into the withholding base.

### Mutuelle Obligatoire (Compulsory Health Insurance)

| Item | Value | Page wording |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F33754 |
| Minimum employer share of the premium | 50% | "La participation financière de l'employeur doit être au moins égale à 50 % de la cotisation" |
| Dental cover in the minimum basket | 125% of the agreed tariff | "Frais dentaires (prothèses et orthodontie) à hauteur de 125 % du tarif conventionnel" |

The cover must meet a minimum basket of care: the whole of the ticket moderateur on consultations, acts and services reimbursed by the health scheme, with exceptions; the whole of the daily hospital charge; and the dental and optical minimums. Cover is compulsory for employees except in the cases where an employee is allowed to refuse. Cover carries on after the contract ends, for the length of the last contract and not more than twelve months. The employer's contribution to this cover is itself charged to CSG and CRDS, with no professional-costs allowance.

### Avantages en Nature and Frais Professionnels

These are the pay elements most often mis-entered. A benefit in kind is pay and bears contributions; an expense allowance inside the limit does not. The company-car forfait depends on the date the vehicle was first made available to the employee, not the date of the payroll run: a car handed over before 1 February 2025 and still in use is valued on the older, lower schedule below, not on the newer one, even in a 2026 payroll.

| Item | Value | Page wording |
| --- | --- | --- |
| Source | all figures below | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html |
| Meal provided, one meal | EUR 5.50 | "Montant de l'avantage en 2026 1 repas 5,50 €" |
| Meal provided, two meals | EUR 11.00 | "2 repas 11,00 €" |
| Luncheon voucher, maximum exempt employer share | EUR 7.32 | "Exonération maximale de la part patronale 7,32 €" |
| Luncheon voucher face value that carries the maximum exemption, lower end | EUR 12.20 | "Entre 12,20 € et 14,64 €" |
| Luncheon voucher face value that carries the maximum exemption, upper end | EUR 14.64 | "Entre 12,20 € et 14,64 €" |
| Company car, vehicle made available since 1 February 2025, bought, five years old or less | 15% of the purchase cost | "Véhicule acheté âgé de 5 ans ou moins 15 % du coût d'achat" |
| Same car, employer pays the private fuel | 20% of the purchase cost | "15 % du coût d'achat + frais réels sur factures de carburant utilisé à des fins personnelles ou 20 % du coût d'achat" |
| Company car, vehicle made available since 1 February 2025, bought, more than five years old | 10% of the purchase cost | "Véhicule acheté de plus de 5 ans 10 % du coût d'achat" |
| Same car, employer pays the private fuel | 15% of the purchase cost | "10 % du coût d'achat + frais réels sur factures de carburant utilisé à des fins personnelles ou 15 % du coût d'achat" |
| Company car, vehicle made available since 1 February 2025, leased | 50% of the yearly total cost | "Véhicule loué ou en location avec option d’achat (LOA) 50 % du coût global annuel (location, entretien, assurance)" |
| Same car, employer pays the private fuel | 67% of the yearly total cost | "50 % du coût global annuel (location, entretien, assurance) + frais réels sur factures de carburant utilisé à des fins personnelles ou 67 % du coût global" |
| Company car, vehicle made available before 1 February 2025, bought, five years old or less | 9% of the purchase cost | "Véhicule acheté âgé de 5 ans ou moins 9 % du coût d'achat" |
| Same car, employer pays the private fuel | 12% of the purchase cost | "9 % du coût d'achat + frais réels sur factures de carburant utilisé à des fins personnelles ou 12 % du coût d'achat" |
| Company car, vehicle made available before 1 February 2025, bought, more than five years old | 6% of the purchase cost | "Véhicule acheté de plus de 5 ans 6 % du coût d'achat" |
| Same car, employer pays the private fuel | 9% of the purchase cost | "6 % du coût d'achat + frais réels sur factures de carburant utilisé à des fins personnelles ou 9 % du coût d'achat" |
| Company car, vehicle made available before 1 February 2025, leased | 30% of the yearly total cost | "Véhicule loué ou en location avec option d’achat (LOA) 30 % du coût global annuel TTC (location, entretien, assurance)" |
| Same car, employer pays the private fuel | 40% of the yearly total cost | "30 % du coût global annuel TTC (location, entretien, assurance) + frais de carburant sur facture o u 4 0 % du coût global" |
| Leased company car, either schedule, cap | Capped at the amount the benefit would have been if the employer had bought the vehicle instead of leasing it | "L'avantage évalué pour un véhicule loué est plafonné au montant de l'avantage en nature qui aurait été évalué si l'employeur avait acheté le véhicule" |
| Electric vehicle, made available since 1 February 2025, meeting the environmental score required for the bonus écologique | 70% reduction of the benefit on the schedule above, the reduction being limited to EUR 4,641.60 a year in 2026 | "Si le véhicule respecte le score environnemental requis pour bénéficier du bonus écologique, vous utilisez le barème ci-dessus auquel vous appliquez une réduction de 70 % sur le montant de l’avantage en nature, dans la limite de 4 641,60 € par an en 2026" |
| Electric vehicle made available before 1 February 2025 | 50% reduction of the benefit on the schedule above, the reduction being limited to EUR 2,026.30 a year in 2026 | "Vous utilisez le barème ci-dessus auquel vous appliquez une réduction de 50 %, dans la limite de 2 026,30 € par an en 2026" |
| Electric vehicle, either schedule | Electricity the employer pays for is excluded from the benefit-in-kind calculation | "Les frais d'électricité pris en charge par l’employeur n’entrent pas en compte dans le calcul de l’avantage en nature" |

| Item | Value | Page wording |
| --- | --- | --- |
| Source | all figures below | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/frais-professionnels.html |
| Meal allowance, employee forced to eat at the workplace | EUR 7.50 | "Salarié contraint de prendre son repas sur le lieu de travail 7,50 €" |
| Meal allowance, employee travelling and forced to eat in a restaurant | EUR 21.40 | "Salarié en situation de déplacement contraint de prendre son repas au restaurant 21,40 €" |
| Meal allowance, employee travelling but not forced to eat in a restaurant | EUR 10.40 | "non contraint de prendre son repas au restaurant 10,40 €" |
| Telework allowance, no collective agreement, per day | EUR 2.70 | "Par jour de télétravail 2,70 € dans la limite de 59,40 € par mois" |
| Telework allowance, no collective agreement, monthly cap | EUR 59.40 | "2,70 € dans la limite de 59,40 € par mois" |
| Telework allowance under a collective agreement, per day | EUR 3.30 | "Par jour de télétravail 3,30 € dans la limite de 72,60 € par mois" |
| Telework allowance under a collective agreement, monthly cap | EUR 72.60 | "3,30 € dans la limite de 72,60 € par mois" |

| Item | Value | Page wording |
| --- | --- | --- |
| Source | all figures below | https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/prime-partage-valeur.html |
| Prime de partage de la valeur, exempt from contributions up to | EUR 3,000 | "exonérée de cotisations et contributions sociales dans la limite de 3 000 €" |
| Same cap where the employer has a profit-sharing scheme in the conditions on the page | EUR 6,000 | "Cette limite d’exonération passe à 6 000 € par bénéficiaire et par an" |
| Forfait social on the prime, employer with the headcount stated on the page | 20% | "le forfait social au taux de 20 % est dû si l’effectif de votre entreprise est égal ou sup" |

The prime de partage de la valeur counts in annual gross pay for the single degressive relief, whether or not it is paid into a savings plan.

## Section 7: Payslip Requirements

The bulletin de paie is governed by the Code du travail. The list below is the list the official page gives.

### Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023)

| Zone | Required fields |
| --- | --- |
| Zone 1, identification of employer and employee | Employer name and address, and the establishment the employee belongs to; the APE or NAF activity code and the employer's Siret; the applicable branch collective agreement, or a reference to the Code du travail on leave and notice; the employee's name, job and position in the agreement's classification; the period and the number of hours worked, separating normal hours from overtime and showing the rate applied to each; the nature and volume of the forfait for an employee on a forfait contract; the nature of the basis of pay where that basis is not working time; and the nature and amount of any salary accessories bearing contributions |
| Zone 2, pay | The employee's gross pay; the base and amount of the employer's and the employee's contributions before exemptions are deducted; the employee's contribution rates before exemptions are deducted; the nature and amount of other payments and deductions, in particular the home-to-work transport reimbursement; the amount actually received by the employee; the date of payment; and, where a period of annual leave falls in the pay period, the leave dates and the amount of the holiday pay |
| Zone 3, contributions and reliefs | Contributions and contributions grouped under five headings, health, work accidents and occupational illness, retirement, family and unemployment, with base, rate and amount; the total of exemptions and reliefs; the total paid by the employer; and the line for the change in pay caused by removing the employee unemployment and health contributions |
| Zone 4, net to pay and net taxable | Net to pay before income tax, and the income tax withheld at source |
| Zone 5, montant net social | Net income after all compulsory social deductions, the figure the employee reports to the family allowance fund |
| Zone 6, income tax | Net taxable amount used as the withholding base, its year to date total, the tax withheld, its year to date total, and the net exempt amount of overtime and complementary hours with its year to date total |
| Zone 7, final wording | A pointer to the payslip page on the service-public portal, the wording telling the employee to keep the payslip with no time limit, and, where short-time working applies, the number of hours compensated |

Source for this list: https://entreprendre.service-public.gouv.fr/vosdroits/F559

The montant net social line and the seven-zone layout came in with the version of the payslip that applies since 1 July 2023. The page also sets out the earlier layout that applies since 2022. Special rules apply to employees in the local health scheme of Haut-Rhin, Bas-Rhin and Moselle: only the employee rate and the employee share are shown.

### Delivery

- Electronic delivery is the rule and paper the exception, since 2017. This is the opposite of the old position. The employee can refuse electronic delivery and must tell the employer.
- The employer must keep a copy at the business for five years, on paper or electronically.
- After those five years the payslips need not be reachable inside the business, but they must not be destroyed, and the employer must guarantee the employee can get them either for fifty years from issue or for six years after the employee retires.
- The employee can challenge the amount or the accuracy of a payslip for three years from the day it was handed over.
- There is no legal duty on the employer to issue a duplicate of a lost payslip.

| Item | Value | Page wording |
| --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F559 |
| Fine the employer can be ordered to pay for each payslip not handed over | EUR 450 | "une amende pouvant atteindre 450 € par fiche non remise" |

## Section 8: Filing Obligations

### Monthly: DSN (Déclaration Sociale Nominative)

| Obligation | Deadline | Page wording |
| --- | --- | --- |
| Source | all figures below unless a row names another page | https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html |
| Employer with 50 employees or more, pay run in the same month as the work | The 5th of the following month | "vous devez transmettre votre DSN liée à la paie du mois en cours, le 5 du mois suivant (M+1)" |
| Employer with 50 employees or more, pay run in the month after the work (decalage de paie) | At the latest the 15th of the following calendar month | "au plus tard le 15 du mois civil suivant" |
| Employer with fewer than 50 employees | At the latest the 15th of the following calendar month | "Vous devez transmettre votre DSN liée à la paie du mois en cours, au plus tard le 15 du mois civil suivant" |
| Employer with fewer than 11 employees, quarterly option | F24013 says such a business may choose to file the DSN each quarter instead of each month, at the latest the 15th of the month after the work period; the same page also says it may exceptionally choose to pay each quarter. Confirm with Urssaf which of the two the client has opted for before moving any monthly filing. Source: entreprendre.service-public.gouv.fr/vosdroits/F24013 | "Les entreprises de moins de 11 salariés peuvent choisir d'effectuer la DSN chaque trimestre et non chaque mois." / "Les entreprises de moins de 11 salariés qui déclarent en DSN chaque trimestre, doivent aussi le faire au plus tard le 15 du mois suivant la période de travail effectuée." |
| Deadline falling on a public holiday or a non-working day | Extended to the next working day | "il est prolongé" |
| Event report (signalement d'evenement): sick leave, end of contract | Within 5 days of the event | "vous êtes tenu d’envoyer une DSN de signalement d'événement dans les 5 jours suivants" |

The condition the live text used to miss: the 5th is not simply the large-employer date. It applies only where the employer has 50 employees or more **and** pays in the same month as the work. An employer of that size that pays in the following month is on the 15th, like a smaller employer. An employer with fewer than 11 employees may, on the wording of F24013, choose to file quarterly, also by the 15th of the month after the work period (see the warning in the row above).

**Penalties**

| Failure | Penalty | Page wording |
| --- | --- | --- |
| Source | all figures below | https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html |
| Filing outside the DSN channel | 0.5% of the monthly social security ceiling per employee | "0,5 % du plafond mensuel de la Sécurité sociale (PMSS) par salarié" |
| Same, cap where the employer has at least 2,000 employees | EUR 10,000 | "montant plafonné à 10 000 € si vous employez au moins 2 000 salariés" |
| Same, cap where the employer has fewer than 2,000 employees | EUR 750 | "montant plafonné à 750 € par entreprise si vous employez un nombre inférieur à 2 000 salariés" |
| Late filing | 1.5% of the monthly ceiling per employee per month or part month late | "1,5 % du plafond mensuel de la Sécurité sociale par salarié et par mois ou fraction de mois de retard" |
| Late filing, cap where the delay is five days or less | 150% of the monthly ceiling per business, once a calendar year | "Montant plafonné à 150 % PMSS par entreprise si défaut de production inférieur ou égal à 5 jours" |
| Employees left out of the filing | 1.5% of the monthly ceiling per employee per month or part month, capped at 150% of the monthly ceiling per business if the failure is corrected within 5 days, once a calendar year | "omission de salariés ou assimilés : 1,5 % du plafond mensuel de la Sécurité sociale par salarié" / "Montant plafonné à 150 % PMSS par entreprise si défaut de production inférieur ou égal à 5 jours" |
| Other omissions, including employer identification data | 0.5% of the monthly ceiling per employee | "autres cas : 0,5 % du plafond mensuel de la Sécurité sociale par salarié" |
| Pay reported wrongly so that contributions come out too low | 1% of the monthly ceiling per employee | "1 % du plafond mensuel de la Sécurité sociale par salarié ou assimilé" |
| Other inaccuracies | 0.33% of the monthly ceiling per employee | "autres cas : 0,33 % du plafond mensuel de la Sécurité sociale par salarié" |
| Correcting figure below which late interest and the penalty are not applied, where errors are not repeated | 5% of the total initial contributions | "le versement régularisateur est inférieur à 5 % du montant total des cotisations initiales" |

The EUR 10,000 and EUR 750 caps on filing outside the DSN channel apply to employers within the scope of the décret of 24 September 2014. A third cap applies to employers within the scope of the décret of 18 May 2016: EUR 750 per business, per month.

An omission or an inaccuracy carries no penalty where the employer corrects it within 30 days of the filing that carried it. Urssaf sends a compte-rendu metier within four hours of the filing, and more anomalies can be flagged five days after the deadline. Separately, the droit à l'erreur applies only where the employer corrects the pay at the nearest declarative deadline and pays the top-up contributions and social charges at the same time; on that condition it removes the majorations and the penalty where either limb is met, provided the inaccuracies are not repetitive: the majorations and penalty that would otherwise apply come to less than one monthly value of the social security ceiling, or the regularising payment is below 5% of the total initial contributions.

**Penalties on the employer as collector of the income tax withheld**

Those Urssaf penalties are about the social contributions. The income tax withheld carries a separate set of penalties under the tax code, which the tax administration's own doctrine sets out. The administrative fines in the first six rows below are exclusive of one another and do not stack. That exclusivity covers only those fines, the ones under CGI art. 1759-0 A. The late-payment surcharge and the criminal penalties are separate charges and the page does not say they are excluded by them.

| Failure | Penalty | Page wording |
| --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/11471-PGP.html |
| Inaccuracy or omission, where the return was filed on time | 5% of the withholding that should have been made or declared | "l’amende est de 5 % des retenues qui auraient dû être effectuées ou déclarées lorsque la déclaration a été déposée dans les délais" |
| Inaccuracy or omission that was deliberate | 40% | "Le taux de l’amende est porté à 40 % en cas d'inexactitudes ou d'omissions délibérées" |
| Return not filed by the deadline | 10% of the withholding that should have been made or declared | "l’amende s’élève à 10 % des retenues qui auraient dû être effectuées ou déclarées" |
| Still not filed within thirty days of a formal notice | 40% | "L’amende est portée à 40 % des retenues qui auraient dû être effectuées ou déclarées en cas de non-dépôt de la déclaration dans les trente jours suivant une mise en demeure" |
| Withholding made but deliberately not declared and not paid over | 80% of the withholding made | "une amende égale à 80 % des retenues effectuées" |
| Floor for any of these fines | EUR 250 per return | "l’amende est au minimum égale à 250 € par déclaration" |
| Late payment of the withholding | The surcharge in CGI art. 1731. The worked example on the page applies 5% of the unpaid amount | "une majoration égale à 5 % du montant non payé" |
| Withholding kept back deliberately, delay over one month, criminal fine | EUR 1,500 | "passible d’une amende de 1 500 €" |
| Repeat within three years | Two years imprisonment and a fine of EUR 3,750, or one of the two | "punissable de deux ans d'emprisonnement et de 3 750 € d'amende" |

The two deliberate-breach fines in the table above apply only where the administration shows the breach was deliberate. Where only part of a return is filed late, the on-time inaccuracy fine applies to that part and the non-filing fine does not. The converse also holds: where the administration finds an omission or an inaccuracy on a return that was itself filed late, only the 10% non-filing fine applies to the whole of the withholding not declared in time.

### Annual

| Obligation | Deadline | Notes |
| --- | --- | --- |
| DADS | Not applicable, fully replaced by the DSN since 2019 | Historical reference only |
| Index de l'égalité professionnelle | Each year, at the latest 1 March, on the company website and on Égapro | Businesses with at least 50 employees over the past year. A business that has just reached 50 employees has three years before it must publish. Source: https://entreprendre.service-public.gouv.fr/vosdroits/F35103 |

### Employee Obligations

| Item | Detail |
| --- | --- |
| Declaration de revenus | Annual, in the spring, pre-filled with the withholding data |
| Adjustment | Where the rate was wrong, the balance is settled through the avis d'imposition |
| Rate maintenance | The employee, not the employer, tells the tax office about a change of family situation, within 60 days |

## Section 9: Common Payroll Patterns

### Typical Bank Statement Descriptions (Salary Credits)

| Pattern | Classification |
| --- | --- |
| VIREMENT SALAIRE, VIR SALAIRE | Net salary payment |
| SALAIRE plus the employer name | Net salary payment |
| INDEMNITE CONGES PAYES | Holiday pay, where paid separately |
| PRIME 13E MOIS | Thirteenth month bonus |
| PRIME PARTICIPATION, INTERESSEMENT | Profit sharing, separate tax and social rules |
| IJSS, CPAM INDEMNITE | Sickness or maternity daily allowance from the health scheme |
| PRIME PARTAGE VALEUR, PPV | Prime de partage de la valeur |

### Typical Employer Debit Patterns

| Pattern | Classification |
| --- | --- |
| URSSAF COTISATIONS | Monthly social contribution payment |
| AGIRC-ARRCO COTISATIONS | Supplementary pension contributions |
| DGFIP PAS, PRELEVEMENT SOURCE | Income tax withheld and paid over |
| MUTUELLE plus the insurer name | Compulsory health cover premium |
| PREVOYANCE plus the insurer name | Provident insurance premium |

## Section 10: Interaction with Other Skills

| Scenario | Skill to use |
| --- | --- |
| Employee payroll, contributions and withholding | This skill, `france-payroll` |
| Self-employed income tax, including auto-entrepreneur and micro-entrepreneur | `fr-income-tax` |
| Income tax for an employee's own household return | `fr-personal-income-tax` |
| Social contributions of a self-employed person | `fr-social-contributions` |
| TVA, French VAT | `france-vat-return` |
| Bookkeeping | `france-bookkeeping` |
| Electronic invoicing, Factur-X and Chorus Pro | `france-einvoice` |

### Key Handoff Points

- **Payroll to bookkeeping.** Gross wages and employer charges are profit and loss expenses. Employee deductions and the tax withheld are liabilities in the 43x accounts until the DSN payment clears. Employer contributions are booked to 645xxx.
- **Payroll to income tax.** Withholding settles most of the employee's income tax in real time. The annual return may still produce an adjustment. The net imposable on the payslip is the reference figure.
- **Payroll to the DSN.** All payroll data feeds the DSN. Accurate payslips give an accurate DSN. Errors produce anomaly reports through net-entreprises.fr.

## The method, step by step

1. **Fix the gross and the pay elements.** Add base pay, overtime at the premium in the overtime table in Section 5 or at the collective agreement rate, bonuses, and benefits in kind at the values in Section 6. Check the result against the Smic in force on the days worked, using the table at https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/montant-smic.html Expense allowances inside the limits on https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/frais-professionnels.html stay out of the base.
2. **Split the gross across the ceilings.** Work out tranche 1 and tranche 2 against the monthly ceiling at https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/plafonds-securite-sociale.html and prorate the ceiling with the daily and hourly values in the same table for a part month or a short contract.
3. **Apply the employee contributions.** Use the employee table in Section 3 and the Agirc-Arrco tables, from https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html and https://www.service-public.gouv.fr/particuliers/vosdroits/F15396 Charge CSG and CRDS on the reduced base in the CSG table, watching the four-ceiling limit. Apply the overtime relief from https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/exonerations-heures/reduction-cotisations-salariales.html
4. **Apply the employer contributions, then the single degressive relief.** Use the employer table in Section 4, then compute the relief with the coefficient parameters at https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html Check eligibility against the pay ceiling in that table before computing anything.
5. **Compute the net imposable and withhold the income tax.** Net imposable is the gross less the deductible social contributions. Apply the rate the tax office sent through the DSN feedback, or, where there is none, the grid at https://bofip.impots.gouv.fr/bofip/11255-PGP.html taking the grid for the territory where the employee lives. The tax withheld is paid to the tax administration by the SEPA B2B debit set in the DSN, as described at https://www.impots.gouv.fr/les-modalites-du-prelevement-la-source-0
6. **Issue the payslip.** Build the seven zones listed in Section 7 from https://entreprendre.service-public.gouv.fr/vosdroits/F559 including the montant net social line and the year to date totals.
7. **File the DSN and pay.** File on net-entreprises.fr by the date in the DSN table in Section 8, from https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html Read the compte-rendu metier and correct by an annule et remplace before the due date. Send an event report within five days of a sick leave or an end of contract.

## Ask the client first

- **How many employees does the business have, and does it pay in the month of the work or the month after?** This decides the DSN date, the Fnal rate, the training contribution rate, the flat overtime deduction, and which coefficient row of the single degressive relief applies.
- **Is the employee resident in France for income tax, and in a compulsory French health scheme?** Both tests must be met for CSG and CRDS. If only the health test is met, an employee health contribution replaces them.
- **Where does the employee live and work?** Mayotte has its own ceiling and its own Smic. Guadeloupe, La Reunion, Martinique, Guyane and Mayotte have their own default withholding grids. Haut-Rhin, Bas-Rhin and Moselle carry an extra employee health contribution and a different apprenticeship tax.
- **Which collective agreement applies?** It can raise the minimum pay above the Smic, change the overtime premiums and the annual quota, change the reference period for leave, and require the employer to keep paying during maternity or sickness.
- **Does the employer use a zoned exemption, the overseas Lodeom exemption, or the home-help exemption, and is the employee's annual pay at or below the pay ceiling in Section 4 (2.5 times the frozen Smic for maladie, 3.5 times for allocations familiales)?** Both the exemption and the pay ceiling must be met; that is now the only ordinary route to the reduced maladie and allocations familiales rates.
- **Was any pay paid in a month when the Smic changed, or any prime de partage de la valeur paid in the year?** Both change the single degressive relief.

## When to refuse or refer

- Any payroll for a special scheme, for example SNCF, RATP, the electricity and gas industries, the mines, the clercs et employes de notaires, or seafarers. The rates and the relief are different and are not in this skill.
- Payroll in Mayotte beyond the ceiling and the Smic quoted here. The contribution rates are a separate schedule.
- Household employers, childminders and home-help staff: they use the Urssaf schedule for particuliers employeurs, not the private-sector schedule.
- Apprentices, professionalisation contracts, interns and company officers, where the base and the exemptions are not the ones in this skill.
- Cadres benefits: the Apec contribution and the minimum provident cover for cadres come from national agreements, not from the pages allowed here. Ask the expert-comptable or read the collective agreement.
- Termination pay: severance, rupture conventionnelle and transactional payments have their own exemption limits. Only the employer contribution rate is in this skill.
- Any case where a collective agreement, an extended branch agreement or a company agreement is in play and has not been read.
- Any figure a client wants to rely on without a French expert-comptable signing it off.

## PROHIBITIONS

- Never work out income tax bands by hand for the withholding. Use the rate the tax office sends, or the default grid in Section 2.
- Never apply the professional-costs allowance to CSG and CRDS above four annual ceilings, and never apply it to the employer's contribution to the company health cover.
- Never mix up tranche 1 and tranche 2 for Agirc-Arrco, and never charge the CET only on the slice above the ceiling: it is charged from the first euro once pay passes the ceiling.
- Never leave the compulsory health cover out of employer cost.
- Never enter an employee unemployment contribution. The private-sector employee table lists none.
- Never assume the reduced maladie or allocations familiales rate for an ordinary private employer in 2026. Check the exemption list and the pay ceiling against the Smic frozen at 31 December 2023 first.
- Never quote a total employer cost or a total employee deduction percentage. No allowed page prints one.
- Never issue a payslip missing a field from the seven zones in Section 7.
- Never miss a DSN deadline. The penalties are shares of the monthly ceiling, set out in Section 8.
- Never forget that the Smic changed on 1 June 2026. Check which rate covers the days worked.
- Never present a payroll computation as final. Send it to an expert-comptable for sign-off.

## Sources

- https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/plafonds-securite-sociale.html
- https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/montant-smic.html
- https://www.urssaf.fr/accueil/actualites/augmentation-smic.html
- https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html
- https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-particuliers.html
- https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/csg-crds.html
- https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/assurance-chomage-ags.html
- https://www.impots.gouv.fr/les-modalites-du-prelevement-la-source-0
- https://entreprendre.service-public.gouv.fr/vosdroits/F35103
- https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html
- https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/exonerations-heures/reduction-cotisations-salariales.html
- https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/prime-partage-valeur.html
- https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html
- https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html
- https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/frais-professionnels.html
- https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html
- https://entreprendre.service-public.gouv.fr/vosdroits/F559
- https://entreprendre.service-public.gouv.fr/vosdroits/F24013
- https://entreprendre.service-public.gouv.fr/vosdroits/F33754
- https://www.service-public.gouv.fr/particuliers/vosdroits/F34009
- https://www.service-public.gouv.fr/particuliers/vosdroits/F1419
- https://www.service-public.gouv.fr/particuliers/vosdroits/F15396
- https://www.service-public.gouv.fr/particuliers/vosdroits/F1911
- https://www.service-public.gouv.fr/particuliers/vosdroits/F2391
- https://www.service-public.gouv.fr/particuliers/vosdroits/F2258
- https://www.service-public.gouv.fr/particuliers/vosdroits/F3053
- https://www.service-public.gouv.fr/particuliers/vosdroits/F2265
- https://www.service-public.gouv.fr/particuliers/vosdroits/F3156
- https://bofip.impots.gouv.fr/bofip/11255-PGP.html
- https://bofip.impots.gouv.fr/bofip/11471-PGP.html

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an expert-comptable in France) before implementation.

The most up-to-date version of this skill is maintained by OpenAccountants. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
