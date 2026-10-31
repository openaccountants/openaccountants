# france-payroll: figure and rule ledger

Independent AI source/calculation review: completed31October2026. The writer-status sentence below records the earlier handover; the [pack review](../docs/research/2026-10-31-france-pack-review.md) records the final outcome. This is not accountant attestation.

Guide SHA256 `4418cb6353997816b4e392ab7a4f6078ba88c63f548d1527c99fd74527903455`. Bounded writer repair31October2026; independent successor review pending. Completed whole20 and all accepted earlier repair evidence remain immutable. Each exact quotation is printed once. Original read dates and representation provenance remain; selected new rereads are separately recorded.

## Current units

| Unit / section / native LF | Current rule, figure or non-rule | Source quotation anchors | Classification |
|---|---|---|---|
| france-payroll-unit-0001 / French payroll: pay, contributions, PAS and DSN (2026, v1.1) / 20 | How a French employer runs a monthly payroll for an employee: the social contributions taken from gross pay, the employer contributions on top, the single degressive relief that now sits over them, income tax withheld at source (prélèvement à la source), the mandatory payslip, and the monthly DSN filing. Figures are for tax year 2026. The income tax scale in Section 2 is the one applied in 2026 to income of 2025 declared in 2026; every other figure in this skill (the withholding grid, social contributions, the Smic, the ceilings and the payroll reliefs) is the one in force during 2026, and where a figure changed inside 2026 the row gives its start date. The rules on contributions and the DSN are those checked on 29 October 2026. The Smic rose on 1 June 2026, so this skill gives both the January value and the June value, and the default withholding grid shown is the one in force from 1 May 2026. | [PAS2019](#pas2019); [PASS](#pass); [RGDUFREEZE](#rgdufreeze) | legal/official selected rule |
| france-payroll-unit-0002 / Section 1: Quick Reference / 24 | \| Field \| Value \| Note \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0003 / Section 1: Quick Reference / 26 | \| Source \| all figures below \| https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/plafonds-securite-sociale.html \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0004 / Section 1: Quick Reference / 27 | \| Country \| France (République française) \| \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0005 / Section 1: Quick Reference / 28 | \| Currency \| EUR only \| \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0006 / Section 1: Quick Reference / 29 | \| Standard pay frequency \| Monthly (mensuel), almost universal \| \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0007 / Section 1: Quick Reference / 30 | \| Tax year \| Calendar year, 1 January to 31 December \| \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0008 / Section 1: Quick Reference / 31 | \| Income tax withholding \| Prélèvement à la source, rate sent by DGFiP to the employer \| \| | [PASRATE](#pasrate) | legal/official selected rule |
| france-payroll-unit-0009 / Section 1: Quick Reference / 32 | \| Social contribution authority \| Urssaf, which collects for all branches \| \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0010 / Section 1: Quick Reference / 33 | \| Supplementary pension \| Agirc-Arrco, one scheme since 2019 \| \| | [UNIFIED](#unified) | legal/official selected rule |
| france-payroll-unit-0011 / Section 1: Quick Reference / 34 | \| Tax authority \| Direction générale des Finances publiques (DGFiP) \| \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0012 / Section 1: Quick Reference / 35 | \| Key legislation \| Code de la Sécurité sociale; Code du travail; Code général des impôts art. 204 A to 204 M for the withholding \| \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0013 / Section 1: Quick Reference / 36 | \| Monthly social security ceiling (plafond mensuel, PMSS) \| EUR 4,005 \| "Mois 4 005 €" \| | [PASS](#pass) | legal/official selected rule |
| france-payroll-unit-0014 / Section 1: Quick Reference / 37 | \| Annual social security ceiling (PASS) \| EUR 48,060 \| "2026 Année 48 060 €" \| | [T37_0](#t37_0) | legal/official selected rule |
| france-payroll-unit-0015 / Section 1: Quick Reference / 38 | \| Published daily ceiling, not the ordinary part-month proration method \| EUR 220 \| "Jour 220 €" \| | [PASS](#pass) | legal/official selected rule |
| france-payroll-unit-0016 / Section 1: Quick Reference / 39 | \| Hourly ceiling \| EUR 30 \| "Heure 30 €" \| | [PASS](#pass) | legal/official selected rule |
| france-payroll-unit-0017 / Section 1: Quick Reference / 40 | \| Electronic declaration \| DSN, filed on net-entreprises.fr \| \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0018 / Section 1: Quick Reference / 41 | \| Review status \| Not yet reviewed by a French expert-comptable \| \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0019 / Section 1: Quick Reference / 43 | Mayotte has its own ceiling and its own Smic. This skill covers mainland France and the overseas departments other than Mayotte unless a row says otherwise. | [MAYOTTE](#mayotte); [SMICGEOG](#smicgeog) | legal/official selected rule |
| france-payroll-unit-0020 / Section 2: Income Tax Withholding (Prélèvement à la Source) / 47 | Since 1 January 2019 the employer withholds income tax from the employee's **net imposable** each month, declares it in the DSN and pays it to the tax administration. Every business that pays salaries taxable in France must collect and pay over the withholding, a foreign employer included. | [PAS2019](#pas2019); [FOREIGNPAY](#foreignpay); [PASRATE](#pasrate) | legal/official selected rule |
| france-payroll-unit-0021 / How PAS Works / 51 | \| Step \| Detail \| Source \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0022 / How PAS Works / 53 | \| Rate source \| The tax office works out the personalised rate from the employee's own income tax return and sends it to the employer. The employee can see it in their space on impots.gouv.fr \| https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 \| | [PASRATE](#pasrate); [PASREQUEST](#pasrequest); [FAMILY](#family); [REMIT](#remit) | legal/official selected rule |
| france-payroll-unit-0023 / How PAS Works / 54 | \| When the rate changes \| The personalised rate is changed every year in September, from the return filed in the spring \| https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 \| | [PASRATE](#pasrate); [PASREQUEST](#pasrequest); [FAMILY](#family); [REMIT](#remit) | legal/official selected rule |
| france-payroll-unit-0024 / How PAS Works / 55 | \| Married or PACS couples \| A couple taxed jointly gets an individualised rate automatically. It applies only to each person's own income; income common to the household keeps the household rate \| https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 \| | [PASRATE](#pasrate); [PASREQUEST](#pasrequest); [FAMILY](#family); [REMIT](#remit) | legal/official selected rule |
| france-payroll-unit-0025 / How PAS Works / 56 | \| Rate change on request \| A new rate applies at the latest in the third month after the request \| https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 \| | [PASRATE](#pasrate); [PASREQUEST](#pasrequest); [FAMILY](#family); [REMIT](#remit) | legal/official selected rule |
| france-payroll-unit-0026 / How PAS Works / 57 | \| Change of family situation \| The employee must tell the tax administration within 60 days of a marriage, PACS, birth, adoption, death, divorce or end of a PACS \| https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 \| | [PASRATE](#pasrate); [PASREQUEST](#pasrequest); [FAMILY](#family); [REMIT](#remit) | legal/official selected rule |
| france-payroll-unit-0027 / How PAS Works / 58 | \| No personalised rate \| Where the employee has never filed a return, the tax office applies a default rate set by a published grid on the monthly withholding base. See the grid below \| https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 \| | [PASRATE](#pasrate); [PASREQUEST](#pasrequest); [FAMILY](#family); [REMIT](#remit) | legal/official selected rule |
| france-payroll-unit-0028 / How PAS Works / 59 | \| Calculation \| The rate is applied to the monthly withholding base (base mensuelle de prélèvement). On the payslip that base is the net taxable amount shown in zone 6 (Section 7) \| https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 \| | [PASRATE](#pasrate); [PASREQUEST](#pasrequest); [FAMILY](#family); [REMIT](#remit) | legal/official selected rule |
| france-payroll-unit-0029 / How PAS Works / 60 | \| Remittance \| Paid to the tax administration (DGFiP), not to Urssaf, by a SEPA B2B direct debit entered in the financial block of the DSN. The bank account debited is the one the employer registered in its professional space on impots.gouv.fr, and the signed SEPA B2B mandate must reach the bank before the first payment \| https://www.impots.gouv.fr/les-modalites-du-prelevement-la-source-0 \| | [PASRATE](#pasrate); [PASREQUEST](#pasrequest); [FAMILY](#family); [REMIT](#remit) | legal/official selected rule |
| france-payroll-unit-0030 / How PAS Works / 62 | The employer never works out the bands. It applies the rate it is given, or the default grid. | [PASRATE](#pasrate) | legal/official selected rule |
| france-payroll-unit-0031 / Income Tax Brackets (2026, progressive scale for annual declaration) / 66 | This scale is what the tax office uses to set the rate. The employer does not use it. It is measured on taxable income per family-quotient share, not on gross salary. | [SCALERULE](#scalerule); [SCALEYEAR](#scaleyear) | legal/official selected rule |
| france-payroll-unit-0032 / Income Tax Brackets (2026, progressive scale for annual declaration) / 68 | \| Taxable income per share \| Rate \| Note \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0033 / Income Tax Brackets (2026, progressive scale for annual declaration) / 70 | \| Source \| all figures below \| https://www.service-public.gouv.fr/particuliers/vosdroits/F1419 \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0034 / Income Tax Brackets (2026, progressive scale for annual declaration) / 71 | \| Up to EUR 11,600 \| 0% \| "Jusqu'à 11 600 € 0 %" \| | [T71_0](#t71_0) | legal/official selected rule |
| france-payroll-unit-0035 / Income Tax Brackets (2026, progressive scale for annual declaration) / 72 | \| EUR 11,601 to EUR 29,579 \| 11% \| "De 11 601 € à 29 579 € 11 %" \| | [T72_0](#t72_0) | legal/official selected rule |
| france-payroll-unit-0036 / Income Tax Brackets (2026, progressive scale for annual declaration) / 73 | \| EUR 29,580 to EUR 84,577 \| 30% \| "De 29 580 € à 84 577 € 30 %" \| | [T73_0](#t73_0) | legal/official selected rule |
| france-payroll-unit-0037 / Income Tax Brackets (2026, progressive scale for annual declaration) / 74 | \| EUR 84,578 to EUR 181,917 \| 41% \| "De 84 578 € à 181 917 € 41 %" \| | [T74_0](#t74_0) | legal/official selected rule |
| france-payroll-unit-0038 / Income Tax Brackets (2026, progressive scale for annual declaration) / 75 | \| Above EUR 181,917 \| 45% \| "Plus de 181 917 € 45 %" \| | [T75_0](#t75_0) | legal/official selected rule |
| france-payroll-unit-0039 / Income Tax Brackets (2026, progressive scale for annual declaration) / 77 | These bands apply to the income of 2025 declared in 2026. A payroll run in 2026 does not use them. | [SCALEYEAR](#scaleyear) | legal/official selected rule |
| france-payroll-unit-0040 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 81 | This is the grid in force from 1 May 2026 for taxpayers living in mainland France or outside France. It is read on the monthly withholding base, which is the net imposable for the month. | [GRIDDATE](#griddate) | legal/official selected rule |
| france-payroll-unit-0041 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 83 | \| Monthly withholding base \| Default rate \| Page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0042 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 85 | \| Source \| all figures below \| https://bofip.impots.gouv.fr/bofip/11255-PGP.html \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0043 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 86 | \| Below EUR 1,635 \| 0% \| "Inférieure à 1 635 euros 0 %" \| | [T86_0](#t86_0) | legal/official selected rule |
| france-payroll-unit-0044 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 87 | \| EUR 1,635 and below EUR 1,698 \| 0.5% \| "Supérieure ou égale à 1 635 euros et inférieure à 1 698 euros 0,5 %" \| | [T87_0](#t87_0) | legal/official selected rule |
| france-payroll-unit-0045 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 88 | \| EUR 1,698 and below EUR 1,807 \| 1.3% \| "Supérieure ou égale à 1 698 euros et inférieure à 1 807 euros 1,3 %" \| | [T88_0](#t88_0) | legal/official selected rule |
| france-payroll-unit-0046 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 89 | \| EUR 1,807 and below EUR 1,928 \| 2.1% \| "Supérieure ou égale à 1 807 euros et inférieure à 1 928 euros 2,1 %" \| | [T89_0](#t89_0) | legal/official selected rule |
| france-payroll-unit-0047 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 90 | \| EUR 1,928 and below EUR 2,060 \| 2.9% \| "Supérieure ou égale à 1 928 euros et inférieure à 2 060 euros 2,9 %" \| | [T90_0](#t90_0) | legal/official selected rule |
| france-payroll-unit-0048 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 91 | \| EUR 2,060 and below EUR 2,170 \| 3.5% \| "Supérieure ou égale à 2 060 euros et inférieure à 2 170 euros 3,5 %" \| | [T91_0](#t91_0) | legal/official selected rule |
| france-payroll-unit-0049 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 92 | \| EUR 2,170 and below EUR 2,315 \| 4.1% \| "Supérieure ou égale à 2 170 euros et inférieure à 2 315 euros 4,1 %" \| | [T92_0](#t92_0) | legal/official selected rule |
| france-payroll-unit-0050 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 93 | \| EUR 2,315 and below EUR 2,738 \| 5.3% \| "Supérieure ou égale à 2 315 euros et inférieure à 2 738 euros 5,3 %" \| | [T93_0](#t93_0) | legal/official selected rule |
| france-payroll-unit-0051 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 94 | \| EUR 2,738 and below EUR 3,135 \| 7.5% \| "Supérieure ou égale à 2 738 euros et inférieure à 3 135 euros 7,5 %" \| | [T94_0](#t94_0) | legal/official selected rule |
| france-payroll-unit-0052 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 95 | \| EUR 3,135 and below EUR 3,571 \| 9.9% \| "Supérieure ou égale à 3 135 euros et inférieure à 3 571 euros 9,9 %" \| | [T95_0](#t95_0) | legal/official selected rule |
| france-payroll-unit-0053 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 96 | \| EUR 3,571 and below EUR 4,019 \| 11.9% \| "Supérieure ou égale à 3 571 euros et inférieure à 4 019 euros 11,9 %" \| | [T96_0](#t96_0) | legal/official selected rule |
| france-payroll-unit-0054 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 97 | \| EUR 4,019 and below EUR 4,690 \| 13.8% \| "Supérieure ou égale à 4 019 euros et inférieure à 4 690 euros 13,8 %" \| | [T97_0](#t97_0) | legal/official selected rule |
| france-payroll-unit-0055 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 98 | \| EUR 4,690 and below EUR 5,624 \| 15.8% \| "Supérieure ou égale à 4 690 euros et inférieure à 5 624 euros 15,8 %" \| | [T98_0](#t98_0) | legal/official selected rule |
| france-payroll-unit-0056 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 99 | \| EUR 5,624 and below EUR 7,037 \| 17.9% \| "Supérieure ou égale à 5 624 euros et inférieure à 7 037 euros 17,9 %" \| | [T99_0](#t99_0) | legal/official selected rule |
| france-payroll-unit-0057 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 100 | \| EUR 7,037 and below EUR 8,789 \| 20% \| "Supérieure ou égale à 7 037 euros et inférieure à 8 789 euros 20 %" \| | [T100_0](#t100_0) | legal/official selected rule |
| france-payroll-unit-0058 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 101 | \| EUR 8,789 and below EUR 12,200 \| 24% \| "Supérieure ou égale à 8 789 euros et inférieure à 12 200 euros 24 %" \| | [T101_0](#t101_0) | legal/official selected rule |
| france-payroll-unit-0059 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 102 | \| EUR 12,200 and below EUR 16,523 \| 28% \| "Supérieure ou égale à 12 200 euros et inférieure à 16 523 euros 28 %" \| | [T102_0](#t102_0) | legal/official selected rule |
| france-payroll-unit-0060 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 103 | \| EUR 16,523 and below EUR 25,937 \| 33% \| "Supérieure ou égale à 16 523 euros et inférieure à 25 937 euros 33 %" \| | [T103_0](#t103_0) | legal/official selected rule |
| france-payroll-unit-0061 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 104 | \| EUR 25,937 and below EUR 55,558 \| 38% \| "Supérieure ou égale à 25 937 euros et inférieure à 55 558 euros 38 %" \| | [T104_0](#t104_0) | legal/official selected rule |
| france-payroll-unit-0062 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 105 | \| EUR 55,558 and above \| 43% \| "Supérieure ou égale à 55 558 euros 43 %" \| | [T105_0](#t105_0) | legal/official selected rule |
| france-payroll-unit-0063 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 107 | Guadeloupe, La Reunion and Martinique have their own grid, and Guyane and Mayotte a third grid. Both are on the same page as the table above. Do not apply the mainland grid to an employee living in those territories. | [GRIDTERR1](#gridterr1); [GRIDTERR2](#gridterr2) | legal/official selected rule |
| france-payroll-unit-0064 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 109 | **Short contracts: the abattement** |  | presentation subheading |
| france-payroll-unit-0065 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 111 | \| Item \| Value \| Note \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0066 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 113 | \| Source \| all figures below \| https://bofip.impots.gouv.fr/bofip/11255-PGP.html \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0067 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 114 | \| Monthly net taxable Smic at 1 June 2026, the basis of the abattement \| EUR 1,531.12 \| "Le montant mensuel net imposable du salaire minimum de croissance s’élève, au 1 er juin 2026, à 1 531,12 euros." \| | [T114_0](#t114_0) | legal/official selected rule |
| france-payroll-unit-0068 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 115 | \| Abattement applied to a short contract before the default grid is read \| EUR 766 \| "est égal à 766 euros (1 531,12 / 2)" \| | [T115_0](#t115_0) | legal/official selected rule |
| france-payroll-unit-0069 / Taux Neutre (Default Rate Grid, 2026: Metropolitan France) / 117 | The EUR 766 allowance applies only when no personal PAS rate has been transmitted, to CDD or mission contracts whose initial term does not exceed two months, or an imprecise term whose contractual minimum does not exceed two months, and only during the first two months of employment. A renewal does not restart that period; an interrupted new contract has its own test. Subtract the allowance from the withholding base, then use the monthly grid without adjusting its bands for a shorter pay period and apply that rate to the base after the allowance. Source: BOI-IR-PAS-20-20-30-10 §230–270, https://bofip.impots.gouv.fr/bofip/11252-PGP.html/identifiant%3DBOI-IR-PAS-20-20-30-10-20181228 . | [SHORTGATE](#shortgate); [SHORTRENEW](#shortrenew); [SHORTCALC](#shortcalc) | legal/official selected rule |
| france-payroll-unit-0070 / URSSAF Contributions (Employee Share) / 123 | \| Contribution \| Employee rate \| Base and page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0071 / URSSAF Contributions (Employee Share) / 125 | \| Source \| all figures below \| https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0072 / URSSAF Contributions (Employee Share) / 126 | \| Vieillesse deplafonnee (old age, uncapped) \| 0.40% \| Total gross. "Assurance vieillesse 0,40 % sur la totalité et 6,90 % dans la limite du plafond" \| | [T126_0](#t126_0) | legal/official selected rule |
| france-payroll-unit-0073 / URSSAF Contributions (Employee Share) / 127 | \| Vieillesse plafonnee (old age, capped) \| 6.90% \| Up to the monthly ceiling. "0,40 % sur la totalité et 6,90 % dans la limite du plafond" \| | [T127_0](#t127_0) | legal/official selected rule |
| france-payroll-unit-0074 / URSSAF Contributions (Employee Share) / 128 | \| CSG non imposable (deductible from taxable pay) \| 6.80% \| "CSG non imposable 6,80 % sur 98,25 % du salaire brut dans la limite de 192 240 € en 2026" \| | [T128_0](#t128_0) | legal/official selected rule |
| france-payroll-unit-0075 / URSSAF Contributions (Employee Share) / 129 | \| CSG imposable (not deductible) \| 2.40% \| "CSG imposable 2,40 % sur 98,25 % du salaire brut dans la limite de 192 240 € en 2026" \| | [T129_0](#t129_0) | legal/official selected rule |
| france-payroll-unit-0076 / URSSAF Contributions (Employee Share) / 130 | \| CRDS \| 0.50% \| "CRDS 0,50 % sur 98,25 % du salaire brut dans la limite de 192 240 € en 2026" \| | [T130_0](#t130_0) | legal/official selected rule |
| france-payroll-unit-0077 / URSSAF Contributions (Employee Share) / 131 | \| Extra employee health contribution, Haut-Rhin, Bas-Rhin and Moselle only \| 1.30% \| "Moselle 1,30 %" \| | [T131_0](#t131_0) | legal/official selected rule |
| france-payroll-unit-0078 / URSSAF Contributions (Employee Share) / 133 | The employee table on that page carries no general health contribution and no unemployment contribution. Do not enter a rate for either. | [NOCHOMAGE](#nochomage) | legal/official selected rule |
| france-payroll-unit-0079 / URSSAF Contributions (Employee Share) / 135 | **The CSG and CRDS base** |  | presentation subheading |
| france-payroll-unit-0080 / URSSAF Contributions (Employee Share) / 137 | \| Item \| Value \| Note \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0081 / URSSAF Contributions (Employee Share) / 139 | \| Source \| all figures below \| https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/csg-crds.html \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0082 / URSSAF Contributions (Employee Share) / 140 | \| CSG rate on earned income, the two employee lines added by the page \| 9.20% \| "ce taux est de : 9,20 % pour la CSG ; 0,50 % pour la CRDS" \| | [T140_0](#t140_0) | legal/official selected rule |
| france-payroll-unit-0083 / URSSAF Contributions (Employee Share) / 141 | \| CRDS rate on earned income \| 0.50% \| "9,20 % pour la CSG ; 0,50 % pour la CRDS" \| | [T141_0](#t141_0) | legal/official selected rule |
| france-payroll-unit-0084 / URSSAF Contributions (Employee Share) / 142 | \| Allowance for professional costs taken off the base \| 1.75% \| "elle est généralement réduite de 1,75 % au titre des frais professionnels" \| | [T142_0](#t142_0) | legal/official selected rule |
| france-payroll-unit-0085 / URSSAF Contributions (Employee Share) / 143 | \| Share of earned income that is therefore charged \| 98.25% \| "les CSG-CRDS sont calculées sur 98,25 % des revenus d’activité" \| | [T143_0](#t143_0) | legal/official selected rule |
| france-payroll-unit-0086 / URSSAF Contributions (Employee Share) / 144 | \| Limit beyond which the allowance stops \| Four annual social security ceilings. The amount is in the employee table above \| "La réduction de 1,75 % ne s’applique toutefois que dans la limite de 4 plafonds annuels de la Sécurité sociale" \| | [T144_0](#t144_0) | legal/official selected rule |
| france-payroll-unit-0087 / URSSAF Contributions (Employee Share) / 145 | \| Employee health contribution where the person is not tax resident in France but is in the French health scheme \| 5.50% \| "Cette cotisation, au taux de 5,50 %, est à déclarer" \| | [T145_0](#t145_0) | legal/official selected rule |
| france-payroll-unit-0088 / URSSAF Contributions (Employee Share) / 147 | Conditions that change the answer. The allowance is taken off only up to four annual ceilings; above that the charge is on the whole amount. The employer's contribution to the company health cover is itself charged to CSG and CRDS with no allowance. The charges are due only where the person is resident in France for income tax **and** is covered by a compulsory French health scheme: if only the health test is met, the charges are not due and an employee health contribution is due instead, at the rate in the table above. | [CSGGATES](#csggates); [CSGEXTRA](#csgextra); [CSGHEALTH](#csghealth) | legal/official selected rule |
| france-payroll-unit-0089 / AGIRC-ARRCO (Supplementary Pension: Employee Share) / 151 | \| Contribution \| Employee rate \| Base and page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0090 / AGIRC-ARRCO (Supplementary Pension: Employee Share) / 153 | \| Source \| all figures below \| https://www.service-public.gouv.fr/particuliers/vosdroits/F15396 \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0091 / AGIRC-ARRCO (Supplementary Pension: Employee Share) / 154 | \| Retraite complementaire, tranche 1 \| 3.15% \| Annual pay up to EUR 48,060. "7,87 % (part salariale : 3,15 % / part patronale : 4,72 % )" \| | [T154_0](#t154_0) | legal/official selected rule |
| france-payroll-unit-0092 / AGIRC-ARRCO (Supplementary Pension: Employee Share) / 155 | \| Retraite complementaire, tranche 2 \| 8.64% \| Annual pay between EUR 48,060 and EUR 384,480. "21,59 % (part salariale : 8,64 % / part patronale : 12,95 % )" \| | [T155_0](#t155_0) | legal/official selected rule |
| france-payroll-unit-0093 / AGIRC-ARRCO (Supplementary Pension: Employee Share) / 156 | \| Combined rate, tranche 1 \| 7.87% \| "7,87 % (part salariale : 3,15 % / part patronale : 4,72 % )" \| | [T156_0](#t156_0) | legal/official selected rule |
| france-payroll-unit-0094 / AGIRC-ARRCO (Supplementary Pension: Employee Share) / 157 | \| Combined rate, tranche 2 \| 21.59% \| "21,59 % (part salariale : 8,64 % / part patronale : 12,95 % )" \| | [T157_0](#t157_0) | legal/official selected rule |
| france-payroll-unit-0095 / AGIRC-ARRCO (Supplementary Pension: Employee Share) / 158 | \| Rate used to buy pension points, tranche 1 \| 6.20% \| "Tranche 1 : jusqu'à 48 060 € 6,20 % 20,1877 €" \| | [T158_0](#t158_0) | legal/official selected rule |
| france-payroll-unit-0096 / AGIRC-ARRCO (Supplementary Pension: Employee Share) / 159 | \| Rate used to buy pension points, tranche 2 \| 17% \| "Tranche 2 : entre 48 060 € et 384 480 € 17 %" \| | [T159_0](#t159_0) | legal/official selected rule |
| france-payroll-unit-0097 / AGIRC-ARRCO (Supplementary Pension: Employee Share) / 160 | \| Price of one pension point in 2026 \| EUR 20.1877 \| "6,20 % 20,1877 €" \| | [PPOINTVALUE](#ppointvalue) | legal/official selected rule |
| france-payroll-unit-0098 / AGIRC-ARRCO (Supplementary Pension: Employee Share) / 162 | The rate charged and the rate that buys points are different rates. Points are bought at the point rates in the table, not at the contribution rates: the difference funds the scheme and buys nothing. Tranche 2 stops at the ceiling in the table, which is eight annual ceilings. | [POINTS](#points) | legal/official selected rule |
| france-payroll-unit-0099 / AGIRC-ARRCO (Supplementary Pension: Employee Share) / 164 | **CEG and CET (employee share)** |  | presentation subheading |
| france-payroll-unit-0100 / AGIRC-ARRCO (Supplementary Pension: Employee Share) / 166 | \| Contribution \| Employee rate \| Base and page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0101 / AGIRC-ARRCO (Supplementary Pension: Employee Share) / 168 | \| Source \| all figures below \| https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-particuliers.html \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0102 / AGIRC-ARRCO (Supplementary Pension: Employee Share) / 169 | \| CEG, tranche 1 \| 0.86% \| "Contribution d'équilibre générale (CEG) tranche 1 (3) 0,86 % dans la limite du plafond" \| | [T169_0](#t169_0) | legal/official selected rule |
| france-payroll-unit-0103 / AGIRC-ARRCO (Supplementary Pension: Employee Share) / 170 | \| CEG, tranche 2 \| 1.08% \| "CEG tranche 2 : 1,08 % part salariale et 1,62 % en part patronale" \| | [T170_0](#t170_0) | legal/official selected rule |
| france-payroll-unit-0104 / AGIRC-ARRCO (Supplementary Pension: Employee Share) / 171 | \| CET \| 0.14% \| "Part salariale à 0,14 % et part patronale à 0,21 %" \| | [T171_0](#t171_0) | legal/official selected rule |
| france-payroll-unit-0105 / AGIRC-ARRCO (Supplementary Pension: Employee Share) / 173 | The CET condition is easy to get wrong. The page says the CET applies to every employee whose pay is above the social security ceiling, and that it is charged from the first euro, not only on the slice above the ceiling. The page that prints these three rates is the Urssaf rates page for household employers; the general CEG tranche 1 employee rate is confirmed on the Urssaf page for the overtime relief, at https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/exonerations-heures/reduction-cotisations-salariales.html | [CEGCET](#cegcet); [OVERTIMECALC](#overtimecalc) | legal/official selected rule |
| france-payroll-unit-0106 / Chômage (Unemployment: Employee Share) / 177 | There is no employee unemployment contribution. The Urssaf employee rate table for the private sector lists none, and the Urssaf page on the unemployment and AGS contributions says they are due by employers: https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/assurance-chomage-ags.html Enter nothing for the employee. | [NOCHOMAGE](#nochomage) | legal/official selected rule |
| france-payroll-unit-0107 / Total Employee Deductions (Approximate) / 181 | No official page prints a single total for employee deductions, so this skill does not state one. Add the lines in the tables above that apply to the employee, then apply the overtime relief below where overtime was worked. |  | explicit retained source/method boundary, not a positive default amount |
| france-payroll-unit-0108 / Total Employee Deductions (Approximate) / 183 | **Relief on overtime (employee share)** |  | presentation subheading |
| france-payroll-unit-0109 / Total Employee Deductions (Approximate) / 185 | \| Item \| Value \| Note \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0110 / Total Employee Deductions (Approximate) / 187 | \| Source \| all figures below \| https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/exonerations-heures/reduction-cotisations-salariales.html \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0111 / Total Employee Deductions (Approximate) / 188 | \| Reduction of employee old-age contributions on overtime and complementary hours, capped \| 11.31% \| "dans la limite de 11,31 %" \| | [T188_0](#t188_0) | legal/official selected rule |
| france-payroll-unit-0112 / Total Employee Deductions (Approximate) / 189 | \| Employee old-age contributions inside that cap \| 7.30% \| "7,30 % (cotisations salariales vieillesse dont 0,40 % sur la totalité de la rémunération et 6,90 % dans la limite du plafond)" \| | [T189_0](#t189_0) | legal/official selected rule |
| france-payroll-unit-0113 / Total Employee Deductions (Approximate) / 190 | \| Agirc-Arrco tranche 1 employee contribution inside that cap \| 3.15% \| "3,15 % (cotisations salariales de retraite complémentaire sur la tranche 1 (= plafond))" \| | [T190_0](#t190_0) | legal/official selected rule |
| france-payroll-unit-0114 / Total Employee Deductions (Approximate) / 191 | \| CEG tranche 1 employee contribution inside that cap \| 0.86% \| "0,86 % (contribution d’équilibre général (CEG) sur la tranche 1 (= plafond))" \| | [T191_0](#t191_0) | legal/official selected rule |
| france-payroll-unit-0115 / Total Employee Deductions (Approximate) / 193 | The relief is a reduction of the employee's old-age contributions on the overtime pay only. It is not an exemption from CSG or CRDS. The reduction must appear on the payslip. Apply eligible overtime/complementary pay × min(the employee’s actually due mandatory legal/conventional old-age contribution rate,11.31%);11.31% is a cap, not every employee’s rate. Eligibility requires legal/conventional working-time compliance, no substitution for suppressed remuneration unless twelve months elapsed, and no complete replacement of the overtime pay by compensatory rest. | [OVERTIMECALC](#overtimecalc); [OVERTIMEGATE](#overtimegate); [OVERTIMECOND](#overtimecond) | legal/official selected rule |
| france-payroll-unit-0116 / URSSAF Contributions (Employer Share) / 199 | \| Contribution \| Employer rate \| Base and page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0117 / URSSAF Contributions (Employer Share) / 201 | \| Source \| all figures below \| https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0118 / URSSAF Contributions (Employer Share) / 202 | \| Maladie, maternite, invalidite, deces, full rate \| 13% \| Total gross. "Taux réduit à 7 % Taux plein à 13 %" \| | [T202_0](#t202_0) | legal/official selected rule |
| france-payroll-unit-0119 / URSSAF Contributions (Employer Share) / 203 | \| Maladie, reduced rate, only in the cases in the note below the table \| 7% \| "Taux réduit à 7 % Taux plein à 13 %" \| | [T203_0](#t203_0) | legal/official selected rule |
| france-payroll-unit-0120 / URSSAF Contributions (Employer Share) / 204 | \| Pay condition for the reduced 7% maladie rate, where the employer qualifies at all, on https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html \| Annual pay at or below 2.5 times the Smic in force on 31 December 2023, a frozen Smic, not the current one \| "le taux de la cotisation d’assurance maladie sera de 7 % si la rémunération annuelle du salarié est inférieure ou égale à 2,5 fois le Smic en vigueur au 31/12/2023" \| | [T204_0](#t204_0) | legal/official selected rule |
| france-payroll-unit-0121 / URSSAF Contributions (Employer Share) / 205 | \| Contribution solidarite autonomie (CSA) \| 0.30% \| Total gross. "Contribution solidarité autonomie (CSA) 0,30 %" \| | [T205_0](#t205_0) | legal/official selected rule |
| france-payroll-unit-0122 / URSSAF Contributions (Employer Share) / 206 | \| Vieillesse deplafonnee \| 2.11% \| Total gross. "Assurance vieillesse 2,11 % sur la totalité et 8,55 % dans la limite du plafond" \| | [T206_0](#t206_0) | legal/official selected rule |
| france-payroll-unit-0123 / URSSAF Contributions (Employer Share) / 207 | \| Vieillesse plafonnee \| 8.55% \| Up to the monthly ceiling. "2,11 % sur la totalité et 8,55 % dans la limite du plafond" \| | [T207_0](#t207_0) | legal/official selected rule |
| france-payroll-unit-0124 / URSSAF Contributions (Employer Share) / 208 | \| Allocations familiales, full rate \| 5.25% \| Total gross. "Allocations familiales Taux réduit à 3,45 % Taux plein à 5,25 %" \| | [T208_0](#t208_0) | legal/official selected rule |
| france-payroll-unit-0125 / URSSAF Contributions (Employer Share) / 209 | \| Allocations familiales, reduced rate, only in the cases in the note below the table \| 3.45% \| "Taux réduit à 3,45 % Taux plein à 5,25 %" \| | [T209_0](#t209_0) | legal/official selected rule |
| france-payroll-unit-0126 / URSSAF Contributions (Employer Share) / 210 | \| Pay condition for the reduced 3.45% allocations familiales rate, where the employer qualifies at all, on https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html \| Annual pay at or below 3.5 times the Smic in force on 31 December 2023, a frozen Smic, not the current one \| "le taux de la cotisation d’allocations familiales sera de 3,45 % si la rémunération annuelle du salarié est inférieure ou égale à 3,5 fois le Smic en vigueur au 31/12/2023" \| | [T210_0](#t210_0) | legal/official selected rule |
| france-payroll-unit-0127 / URSSAF Contributions (Employer Share) / 211 | \| Contribution au dialogue social \| 0.016% \| Total gross. "Contribution au dialogue social 0,016 %" \| | [T211_0](#t211_0) | legal/official selected rule |
| france-payroll-unit-0128 / URSSAF Contributions (Employer Share) / 212 | \| Fnal, employer with fewer than 50 employees \| 0.10% \| Up to the monthly ceiling. "Fnal (effectif de moins de 50 salariés) 0,10 % dans la limite du plafond" \| | [T212_0](#t212_0) | legal/official selected rule |
| france-payroll-unit-0129 / URSSAF Contributions (Employer Share) / 213 | \| Fnal, employer with 50 employees or more \| 0.50% \| Total gross. "Fnal (effectif de 50 salariés et plus) 0,50 %" \| | [T213_0](#t213_0) | legal/official selected rule |
| france-payroll-unit-0130 / URSSAF Contributions (Employer Share) / 214 | \| Contribution formation professionnelle, fewer than 11 employees \| 0.55% \| "Pour une entreprise de moins de 11 salariés : 0,55 %" \| | [T214_0](#t214_0) | legal/official selected rule |
| france-payroll-unit-0131 / URSSAF Contributions (Employer Share) / 215 | \| Contribution formation professionnelle, 11 employees or more \| 1% \| "Pour une entreprise de 11 salariés et plus : 1 %" \| | [T215_0](#t215_0) | legal/official selected rule |
| france-payroll-unit-0132 / URSSAF Contributions (Employer Share) / 216 | \| Contribution CPF-CDD, on fixed-term contract pay \| 1% \| "Contribution CPF-CDD 1 %" \| | [T216_0](#t216_0) | legal/official selected rule |
| france-payroll-unit-0133 / URSSAF Contributions (Employer Share) / 217 | \| Taxe d'apprentissage, main part \| 0.59% \| "Taxe d'apprentissage Part principale à 0,59 % Solde à 0,09 %" \| | [T217_0](#t217_0) | legal/official selected rule |
| france-payroll-unit-0134 / URSSAF Contributions (Employer Share) / 218 | \| Taxe d'apprentissage, balance \| 0.09% \| "Part principale à 0,59 % Solde à 0,09 %" \| | [T218_0](#t218_0) | legal/official selected rule |
| france-payroll-unit-0135 / URSSAF Contributions (Employer Share) / 219 | \| Taxe d'apprentissage, establishments in Haut-Rhin, Bas-Rhin and Moselle, main part, no balance due \| 0.44% \| "Part principale à 0,44 % Solde - Néant" \| | [T219_0](#t219_0) | legal/official selected rule |
| france-payroll-unit-0136 / URSSAF Contributions (Employer Share) / 220 | \| Accident du travail (AT/MP) \| Rate notified to the employer by the Carsat \| "Accident du travail Taux notifié par la Carsat" \| | [T220_0](#t220_0) | legal/official selected rule |
| france-payroll-unit-0137 / URSSAF Contributions (Employer Share) / 221 | \| Versement mobilite, employer with 11 employees or more \| Rate set locally, look it up with the Urssaf search tool \| "Versement mobilité (effectif de 11 salariés et plus)" \| | [T221_0](#t221_0) | legal/official selected rule |
| france-payroll-unit-0138 / URSSAF Contributions (Employer Share) / 223 | There is no published national range for the AT/MP rate. Use the rate on the Carsat notification for the establishment and nothing else. | [CARSAT](#carsat) | legal/official selected rule |
| france-payroll-unit-0139 / URSSAF Contributions (Employer Share) / 225 | **Two official pages disagree about the reduced maladie and allocations familiales rates.** The Urssaf rates page above prints them as if they were ordinary alternatives. The Urssaf page on what changed for 2026 says that from 2026 the reduced rates were withdrawn and merged into the single degressive relief below, and survive only for employers using a zoned exemption (ZRR and ZFRR, ZRD, ZFU), the overseas Lodeom exemption, or the exemption for home-help staff placed with a fragile person, and for employees in certain special schemes for whom the single relief is not available. That page is at https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html Where the two conflict, do not assume the reduced rate applies to an ordinary private employer. The same page gives the pay condition, and it is measured against the Smic frozen at 31 December 2023, so it does not move when the Smic rises. | [REDUCEDAM](#reducedam); [REDUCEDAF](#reducedaf); [REDUCEDELIG](#reducedelig); [RGDUSTALE](#rgdustale) | legal/official selected rule |
| france-payroll-unit-0140 / Réduction Générale Dégressive Unique (RGDU) / 229 | New for 2026 and the largest single item in French employer cost. The old degressive relief and the reduced maladie and allocations familiales rates were merged into one relief. | [RGDUELIG](#rgduelig); [RGDUPARAM](#rgduparam) | legal/official selected rule |
| france-payroll-unit-0141 / Réduction Générale Dégressive Unique (RGDU) / 231 | \| Item \| Value \| Page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0142 / Réduction Générale Dégressive Unique (RGDU) / 233 | \| Source \| all figures below unless a row names another page \| https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0143 / Réduction Générale Dégressive Unique (RGDU) / 234 | \| Pay ceiling for eligibility, at the Smic in force on 1 January 2026 \| 3 Smic \| "a une rémunération inférieure : à 3 Smic applicable au 1 er janvier 2026" \| | [T234_0](#t234_0) | legal/official selected rule |
| france-payroll-unit-0144 / Réduction Générale Dégressive Unique (RGDU) / 235 | \| Same ceiling expressed against the Smic in force on 1 June 2026 \| 2.9293 Smic \| "(ou 2,9293 Smic applicable au 1 er juin 2026)" \| | [T235_0](#t235_0) | legal/official selected rule |
| france-payroll-unit-0145 / Réduction Générale Dégressive Unique (RGDU) / 236 | \| Smic value that governs the 2026 coefficient, mainland and overseas departments other than Mayotte \| The Smic in force on 1 January 2026 \| "En 2026, la valeur du Smic à prendre en compte est celle en vigueur au 1 er janvier 2026" \| | [T236_0](#t236_0) | legal/official selected rule |
| france-payroll-unit-0146 / Réduction Générale Dégressive Unique (RGDU) / 237 | \| Official worked example: employer with 70 employees, June 2026, full-time 35 hours, no overtime, monthly gross pay EUR 2,000 \| Coefficient 0.3178 \| "une rémunération mensuelle brute de 2 000 €, la valeur maximale du coefficient de réduction générale est de 0,3178" \| | [T237_0](#t237_0) | legal/official selected rule |
| france-payroll-unit-0147 / Réduction Générale Dégressive Unique (RGDU) / 238 | \| Pay ceiling in Mayotte \| 1.6 Smic \| "à 1,6 Smic applicable à Mayotte en 2026" \| | [T238_0](#t238_0) | legal/official selected rule |
| france-payroll-unit-0148 / Réduction Générale Dégressive Unique (RGDU) / 239 | \| What the Urssaf 2026-news page (informations-nouvelle-annee.html) says the 3-Smic ceiling replaced \| 1.6 Smic, the pre-2026 figure \| "qui sont inférieurs à 3 Smic en vigueur au lieu de 1,6 Smic auparavant" \| | [T239_0](#t239_0) | legal/official selected rule |
| france-payroll-unit-0149 / Réduction Générale Dégressive Unique (RGDU) / 240 | \| What entreprendre.service-public.fr F559, Vérifié le 01 juin 2026, still prints for the general relief \| Below 1.6 Smic, EUR 2,987.23 \| "Allègements généraux dont bénéficient les employeurs au titre des salariés dont les rémunérations brutes sont inférieures à 1,6 Smic ( 2 987,23 € )" \| | [T240_0](#t240_0) | legal/official selected rule |
| france-payroll-unit-0150 / Réduction Générale Dégressive Unique (RGDU) / 241 | \| What the same F559 page prints for the allocations familiales rate reduction, measured against the current Smic rather than the frozen Smic that governs the rate in Section 4 \| Below 3.5 Smic, EUR 6,534.56, which is 3.5 times the June 2026 Smic \| "Réduction du taux de cotisations allocations familiales, dont bénéficient les employeurs au titre des salariés dont les rémunérations brutes sont inférieures à 3,5 Smic ( 6 534,56 € )" \| | [T241_0](#t241_0) | legal/official selected rule |
| france-payroll-unit-0151 / Réduction Générale Dégressive Unique (RGDU) / 242 | \| Maladie rate covered by the relief \| 13.00% \| "d’assurances sociales (maladie, maternité, invalidité, décès) au taux de 13,00 %" \| | [T242_0](#t242_0) | legal/official selected rule |
| france-payroll-unit-0152 / Réduction Générale Dégressive Unique (RGDU) / 243 | \| Vieillesse rate covered \| 10.66% \| "de vieillesse au taux de 10,66 %" \| | [T243_0](#t243_0) | legal/official selected rule |
| france-payroll-unit-0153 / Réduction Générale Dégressive Unique (RGDU) / 244 | \| Allocations familiales rate covered \| 5.25% \| "d’allocations familiales au taux de 5,25 %" \| | [T244_0](#t244_0) | legal/official selected rule |
| france-payroll-unit-0154 / Réduction Générale Dégressive Unique (RGDU) / 245 | \| AT/MP rate covered, capped at the pooled part \| 0.49% \| "pour sa partie mutualisée au taux de 0,49 %" \| | [T245_0](#t245_0) | legal/official selected rule |
| france-payroll-unit-0155 / Réduction Générale Dégressive Unique (RGDU) / 246 | \| Agirc-Arrco rate covered \| 6.01% \| "de retraite complémentaire légalement obligatoire (Agirc-Arrco) au taux de 6,01 %" \| | [T246_0](#t246_0) | legal/official selected rule |
| france-payroll-unit-0156 / Réduction Générale Dégressive Unique (RGDU) / 247 | \| Fnal rate covered, employer with fewer than 50 employees \| 0.10% \| "de fonds national d’aide au logement (Fnal) au taux de 0,10 % pour les entreprises de moins de 50 salariés" \| | [T247_0](#t247_0) | legal/official selected rule |
| france-payroll-unit-0157 / Réduction Générale Dégressive Unique (RGDU) / 248 | \| Fnal rate covered, employer with 50 employees or more \| 0.50% \| "ou 0,50 % pour les entreprises de 50 salariés et plus ; de solidarité pour l’autonomie" \| | [T248_0](#t248_0) | legal/official selected rule |
| france-payroll-unit-0158 / Réduction Générale Dégressive Unique (RGDU) / 249 | \| CSA rate covered \| 0.30% \| "de solidarité pour l’autonomie (CSA) au taux de 0,30 %" \| | [T249_0](#t249_0) | legal/official selected rule |
| france-payroll-unit-0159 / Réduction Générale Dégressive Unique (RGDU) / 250 | \| Unemployment rate covered \| 4.00% \| "d’assurance chômage au taux de 4,00 %" \| | [T250_0](#t250_0) | legal/official selected rule |
| france-payroll-unit-0160 / Réduction Générale Dégressive Unique (RGDU) / 252 | Two official pages give different ceilings for the general relief. entreprendre.service-public.gouv.fr/vosdroits/F559, Vérifié le 01 juin 2026, still prints 1.6 Smic and EUR 2,987.23. The Urssaf relief and 2026 news pages give 3 Smic, and the news page says the 3 Smic figure replaced 1.6 Smic. Both are in the table above. The Urssaf pages are the ones that describe the 2026 reform by name, but do not treat that as settled without checking the client's own Urssaf account. | [RGDUELIG](#rgduelig); [RGDUSTALE](#rgdustale) | legal/official selected rule |
| france-payroll-unit-0161 / Réduction Générale Dégressive Unique (RGDU) / 254 | The same F559 page's allocations familiales figure is a second instance of the same problem, not a fresh one: the amount in the row above is 3.5 times the Smic in force on 1 June 2026, while the pay condition for the reduced 3.45% rate above is measured against the Smic frozen at 31 December 2023. F559 has not been updated for the 2026 freeze, the same way it has not been updated for the 1.6-to-3-Smic change. Use the frozen-Smic test in the row above for the reduced rate; treat the F559 figure as the stale, pre-freeze measurement. | [REDUCEDAF](#reducedaf); [RGDUSTALE](#rgdustale) | legal/official selected rule |
| france-payroll-unit-0162 / Réduction Générale Dégressive Unique (RGDU) / 256 | **Coefficient parameters** |  | presentation subheading |
| france-payroll-unit-0163 / Réduction Générale Dégressive Unique (RGDU) / 258 | \| Item \| Employer with fewer than 50 employees \| Employer with 50 employees or more \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0164 / Réduction Générale Dégressive Unique (RGDU) / 260 | \| Source \| all figures below \| https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0165 / Réduction Générale Dégressive Unique (RGDU) / 261 | \| T min \| 0.0200 \| 0.0200 \| | [RGDUPARAM](#rgduparam) | legal/official selected rule |
| france-payroll-unit-0166 / Réduction Générale Dégressive Unique (RGDU) / 262 | \| T delta \| 0.3781 \| 0.3821 \| | [RGDUPARAM](#rgduparam) | legal/official selected rule |
| france-payroll-unit-0167 / Réduction Générale Dégressive Unique (RGDU) / 263 | \| Maximum coefficient \| 0.3981 \| 0.4021 \| | [RGDUPARAM](#rgduparam) | legal/official selected rule |
| france-payroll-unit-0168 / Réduction Générale Dégressive Unique (RGDU) / 264 | \| Exponent P \| 1.75 \| 1.75 \| | [RGDUPARAM](#rgduparam) | legal/official selected rule |
| france-payroll-unit-0169 / Réduction Générale Dégressive Unique (RGDU) / 266 | The formula on the Urssaf pages is: coefficient equals T min plus T delta multiplied by the bracketed term raised to the exponent P, where the bracketed term is one half multiplied by (three times the annual Smic, the Smic being increased by the hourly Smic times the number of overtime or complementary hours, divided by annual gross pay, minus one). The relief page says the Smic value may be adjusted for part-time work, a collective working time below the legal one, and suspensions of the contract. For mainland France and the overseas departments other than Mayotte, the Smic to use for the whole of 2026 is the Smic in force on 1 January 2026, so the June rise does not move the relief. The relief page allows the same result with 2.9293 times the annual Smic at its 1 June 2026 value instead of 3 times the January value. The relief page says the Bulletin officiel de la Sécurité sociale (Boss) allows an employer not to apply these formulas to pay of employees whose contract ended between 1 and 30 June 2026, but they apply to the whole of 2026 for every employee still under contract on 1 July 2026. Only in Mayotte are the Smic rises taken into account. Annual gross pay includes a prime de partage de la valeur where one was paid, both for the eligibility test and for the coefficient. | [RGDUFORM1](#rgduform1); [RGDUHOURS](#rgduhours); [RGDUFREEZE](#rgdufreeze); [RGDUPPV](#rgduppv); [RGDUTRANS](#rgdutrans) | legal/official selected rule |
| france-payroll-unit-0170 / Réduction Générale Dégressive Unique (RGDU) / 268 | **Employer relief on overtime** |  | presentation subheading |
| france-payroll-unit-0171 / Réduction Générale Dégressive Unique (RGDU) / 270 | \| Item \| Value \| Page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0172 / Réduction Générale Dégressive Unique (RGDU) / 272 | \| Source \| all figures below \| https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0173 / Réduction Générale Dégressive Unique (RGDU) / 273 | \| Flat employer deduction per overtime hour, employer with fewer than 20 employees \| EUR 1.50 \| "1,50 € pour les employeurs dont l’effectif est inférieur à 20 salariés" \| | [T273_0](#t273_0) | legal/official selected rule |
| france-payroll-unit-0174 / Réduction Générale Dégressive Unique (RGDU) / 274 | \| Flat employer deduction per overtime hour, employer with 20 employees or more \| EUR 0.50 \| "0,50 € par heure supplémentaire pour les employeurs d’au moins 20 salariés" \| | [T274_0](#t274_0) | legal/official selected rule |
| france-payroll-unit-0175 / Réduction Générale Dégressive Unique (RGDU) / 276 | From 1 January 2026 the old headcount limit for this deduction was removed, so every employer eligible for the single relief can claim it whatever its size. It also covers days bought back from an employee on a forfait-jours contract above the cap of 218 days. Under CSSL241-18II and L241-18-1II, each qualifying surrendered forfait day carries SEVEN times the relevant hourly amount: EUR10.50 for the under20 branch or EUR3.50 for the20+ branch, before the actual contribution cap. Establish the applicable headcount branch, a qualifying annual forfait and surrender beyond218 days under the statutory conditions, working-time compliance and remuneration at least equal to an unenhanced hour; exclude recent remuneration substitution unless twelve months elapsed. Apply after other eligible reliefs and cap at the relevant employer contributions still due for that employee’s remuneration at payment. Keep the control document required by V. IV also conditions relief on its named EU1407/2013 de-minimis reference: establish the applicable aid-rule succession and undertaking’s aid facts before claiming; the retained agency’s200000/100000 amounts are not a verified universal2026 ceiling. The amounts here are conditional on those eligibility/remaining-dues inputs, not automatic relief for every purchased day. | [OTEMPLOYER](#otemployer); [OTEMPLOYERALL](#otemployerall); [PAY_DAY20PLUS](#pay_day20plus); [PAY_DAYUNDER20](#pay_dayunder20) | legal/official selected rule |
| france-payroll-unit-0176 / AGIRC-ARRCO (Employer Share) / 280 | \| Contribution \| Employer rate \| Base and page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0177 / AGIRC-ARRCO (Employer Share) / 282 | \| Source \| all figures below \| https://www.service-public.gouv.fr/particuliers/vosdroits/F15396 \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0178 / AGIRC-ARRCO (Employer Share) / 283 | \| Retraite complementaire, tranche 1 \| 4.72% \| Annual pay up to EUR 48,060. "7,87 % (part salariale : 3,15 % / part patronale : 4,72 % )" \| | [T283_0](#t283_0) | legal/official selected rule |
| france-payroll-unit-0179 / AGIRC-ARRCO (Employer Share) / 284 | \| Retraite complementaire, tranche 2 \| 12.95% \| Annual pay between EUR 48,060 and EUR 384,480. "21,59 % (part salariale : 8,64 % / part patronale : 12,95 % )" \| | [T284_0](#t284_0) | legal/official selected rule |
| france-payroll-unit-0180 / AGIRC-ARRCO (Employer Share) / 286 | \| Contribution \| Employer rate \| Base and page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0181 / AGIRC-ARRCO (Employer Share) / 288 | \| Source \| all figures below \| https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-particuliers.html \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0182 / AGIRC-ARRCO (Employer Share) / 289 | \| CEG, tranche 1 \| 1.29% \| "Contribution d'équilibre générale (CEG) tranche 1 (3) 1,29 % dans la limite du plafond" \| | [T289_0](#t289_0) | legal/official selected rule |
| france-payroll-unit-0183 / AGIRC-ARRCO (Employer Share) / 290 | \| CEG, tranche 2 \| 1.62% \| "CEG tranche 2 : 1,08 % part salariale et 1,62 % en part patronale" \| | [T290_0](#t290_0) | legal/official selected rule |
| france-payroll-unit-0184 / AGIRC-ARRCO (Employer Share) / 291 | \| CET \| 0.21% \| "Part salariale à 0,14 % et part patronale à 0,21 %" \| | [T291_0](#t291_0) | legal/official selected rule |
| france-payroll-unit-0185 / AGIRC-ARRCO (Employer Share) / 292 | \| Employer share of the Agirc-Arrco contribution, on https://entreprendre.service-public.gouv.fr/vosdroits/F24013 \| 60% \| "60 % par l'employeur et 40 % par le salarié" \| | [T292_0](#t292_0) | legal/official selected rule |
| france-payroll-unit-0186 / AGIRC-ARRCO (Employer Share) / 293 | \| Employee share of the Agirc-Arrco contribution, on https://entreprendre.service-public.gouv.fr/vosdroits/F24013 \| 40% \| "60 % par l'employeur et 40 % par le salarié" \| | [T293_0](#t293_0) | legal/official selected rule |
| france-payroll-unit-0187 / AGIRC-ARRCO (Employer Share) / 295 | The same warning as on the employee table applies here. The only allowed page that prints the employer CEG tranche 2 and CET rates is the Urssaf rates page for household employers, in a footnote that states the Agirc-Arrco rules generally. The private-sector rates page prints neither. Confirm the tranche 2 and CET rates against the Agirc-Arrco circular before signing. The 60/40 Agirc-Arrco employer/employee split is confirmed separately, for all private-sector employees and not just household employees, on entreprendre.service-public.gouv.fr/vosdroits/F24013, which is a better source for that split than the household-employer page. | [CEGCET](#cegcet) | legal/official selected rule |
| france-payroll-unit-0188 / AGIRC-ARRCO (Employer Share) / 297 | Apec is also due on cadres’ salary up to four social-security ceilings: 0.06% in total, split 0.024% employee and 0.036% employer. This ordinary contribution is separate from Agirc-Arrco pension-point contributions. Source: the official Agirc-Arrco points page, https://www.agirc-arrco.fr/particuliers/ma-retraite/comprendre-ma-retraite/points-de-retraite-comment-sont-ils-obtenus/ . F24013 (entreprendre.service-public.gouv.fr/vosdroits/F24013) names Cotisation Apec without a figure; the official Agirc-Arrco source supplies it. The distinct cadre provident-cover minimum still requires the applicable agreement; it is not inferred from the Apec rate. | [APEC](#apec) | legal/official selected rule |
| france-payroll-unit-0189 / Unemployment and Other Employer-Only / 301 | \| Contribution \| Employer rate \| Base and page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0190 / Unemployment and Other Employer-Only / 303 | \| Source \| all figures below \| https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0191 / Unemployment and Other Employer-Only / 304 | \| Assurance chomage \| 4.00% \| "Contribution assurance chômage 4,00 % dans la limite de 192 240 € en 2026" \| | [T304_0](#t304_0) | legal/official selected rule |
| france-payroll-unit-0192 / Unemployment and Other Employer-Only / 305 | \| Annual pay ceiling for the unemployment and AGS contributions \| EUR 192,240 \| "dans la limite de 192 240 € en 2026" \| | [T305_0](#t305_0) | legal/official selected rule |
| france-payroll-unit-0193 / Unemployment and Other Employer-Only / 306 | \| AGS \| 0.25% \| "Dans la limite de 192 240 € en 2026 : 0,25 %" \| | [T306_0](#t306_0) | legal/official selected rule |
| france-payroll-unit-0194 / Unemployment and Other Employer-Only / 307 | \| AGS, temporary work agencies \| 0.03% \| "0,03 % pour les entreprises de travail temporaire" \| | [T307_0](#t307_0) | legal/official selected rule |
| france-payroll-unit-0195 / Unemployment and Other Employer-Only / 309 | \| Contribution \| Employer rate \| Page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0196 / Unemployment and Other Employer-Only / 311 | \| Source \| all figures below \| https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0197 / Unemployment and Other Employer-Only / 312 | \| Employer contribution on the excluded social-contribution-base part of ordinary rupture conventionnelle or employer-initiated retirement indemnities \| 40% under CSS L137-12. Urssaf dates the increase to the January 2026 employment period, not simply a contract end after 1 January; its stated qualifying contrat de valorisation de l’expérience retirement exception must be checked separately \| "Le taux de cette contribution patronale passe de 30 % à 40 % à compter de la période d’emploi de janvier 2026." \| | [T312_0](#t312_0) | legal/official selected rule |
| france-payroll-unit-0198 / Unemployment and Other Employer-Only / 314 | Date boundary: the selected current L137-12 display says its amended 40% text entered into force immediately on 31 December 2025, while the Urssaf operational note refers to the January 2026 employment period. A December 2025/January 2026 straddling indemnity needs that precise effect-date reconciliation; the old after-1-January contract-end shortcut is not used here. Source: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053282399/2026-06-16 . | [TERMRATE](#termrate); [TERMLAW](#termlaw) | legal/official selected rule |
| france-payroll-unit-0199 / Total Employer Cost (Approximate) / 318 | No official page prints a single percentage for total employer cost, so this skill does not state one. Build the cost from the tables above, then deduct the single degressive relief. For pay at or near the Smic the relief cancels most of the employer social cost, and it runs out at the pay ceiling in the relief table. |  | explicit retained source/method boundary, not a positive default amount |
| france-payroll-unit-0200 / SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) / 324 | The minimum wage changed inside the year. Use the value in force on the day the work was done. | [SMICGEOG](#smicgeog) | legal/official selected rule |
| france-payroll-unit-0201 / SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) / 326 | \| Item \| Value \| Page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0202 / SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) / 328 | \| Source \| all figures below \| https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/montant-smic.html \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0203 / SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) / 329 | \| Gross hourly, 1 January 2026 to 31 May 2026 \| EUR 12.02 \| "Smic horaire brut 12,02 € 12,31 €" \| | [T329_0](#t329_0) | legal/official selected rule |
| france-payroll-unit-0204 / SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) / 330 | \| Gross monthly on a 35 hour week, 1 January 2026 to 31 May 2026 \| EUR 1,823.03 \| "Du 1 er janvier 2026 au 31 mai 2026 Smic horaire brut 12,02 € Smic brut mensuel (base 35 heures par semaine) 1 823,03 €" \| | [T330_0](#t330_0) | legal/official selected rule |
| france-payroll-unit-0205 / SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) / 331 | \| Gross hourly from 1 June 2026 \| EUR 12.31 \| "Smic horaire brut 12,02 € 12,31 €" \| | [T331_0](#t331_0) | legal/official selected rule |
| france-payroll-unit-0206 / SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) / 332 | \| Gross monthly on a 35 hour week from 1 June 2026 \| EUR 1,867.02 \| "Au 1 er juin 2026 Smic horaire brut 12,31 € Smic brut mensuel (base 35 heures par semaine) 1 867,02 €" \| | [T332_0](#t332_0) | legal/official selected rule |
| france-payroll-unit-0207 / SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) / 333 | \| Gross hourly from 1 June 2026, employee aged 17 to 18 without six months in the trade \| EUR 11.08 \| "Smic horaire brut 10,82 € 11,08 €" \| | [T333_0](#t333_0); [PAY_YOUTH_17_18](#pay_youth_17_18) | legal/official selected rule |
| france-payroll-unit-0208 / SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) / 334 | \| Gross hourly from 1 June 2026, employee under 17 without six months in the trade \| EUR 9.85 \| "Smic horaire brut 9,62 € 9,85 €" \| | [T334_0](#t334_0); [PAY_YOUTH_UNDER17](#pay_youth_under17) | legal/official selected rule |
| france-payroll-unit-0209 / SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) / 336 | \| Item \| Value \| Page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0210 / SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) / 338 | \| Source \| all figures below \| https://www.urssaf.fr/accueil/actualites/augmentation-smic.html \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0211 / SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) / 339 | \| Gross hourly in Mayotte from 1 June 2026 \| EUR 9.56 \| "le Smic horaire brut est porté à 9,56 € soit un montant mensuel brut de 1 449,93 €" \| | [T339_0](#t339_0) | legal/official selected rule |
| france-payroll-unit-0212 / SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) / 340 | \| Minimum garanti from 1 June 2026 \| EUR 4.35 \| "Le minimum garanti s'établit à 4,35 €" \| | [T340_0](#t340_0) | legal/official selected rule |
| france-payroll-unit-0213 / SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) / 342 | Conditions. The reduced youth rates apply only to an employee under 18 who does not yet have six months of practice in the trade. A collective agreement rate that is higher than the Smic wins. The Smic covers mainland France, Guadeloupe, Guyane, Martinique, La Reunion, Saint-Barthelemy, Saint-Martin and Saint-Pierre-et-Miquelon; Mayotte has its own rate. The June 2026 rise came from the ministerial order of 22 May 2026. No allowed page states the automatic revaluation trigger, so this skill does not state one: check the Urssaf page before each run. | [SMICYOUTH](#smicyouth); [SMICGEOG](#smicgeog) | legal/official selected rule |
| france-payroll-unit-0214 / SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) / 344 | Net monthly pay at the Smic is not published as a figure on any allowed page and has been removed from this skill. The monthly net **taxable** Smic at 1 June 2026 is published, in the short-contract table in Section 2. |  | explicit retained source/method boundary, not a positive default amount |
| france-payroll-unit-0215 / Working Hours and Overtime / 348 | \| Rule \| Value \| Page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0216 / Working Hours and Overtime / 350 | \| Source \| all figures below \| https://www.service-public.gouv.fr/particuliers/vosdroits/F1911 \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0217 / Working Hours and Overtime / 351 | \| Legal weekly hours (duree legale) \| 35 hours per week \| "35 heures par semaine" \| | [T351_0](#t351_0) | legal/official selected rule |
| france-payroll-unit-0218 / Working Hours and Overtime / 352 | \| Legal monthly hours \| 151.67 hours \| "151,67 heures par mois" \| | [T352_0](#t352_0) | legal/official selected rule |
| france-payroll-unit-0219 / Working Hours and Overtime / 353 | \| Legal annual hours \| 1,607 hours \| "1 607 heures par an" \| | [T353_0](#t353_0) | legal/official selected rule |
| france-payroll-unit-0220 / Working Hours and Overtime / 354 | \| Maximum daily working time \| 10 hours \| "ne doit pas dépasser la durée maximale de 10 heures par jour" \| | [T354_0](#t354_0) | legal/official selected rule |
| france-payroll-unit-0221 / Working Hours and Overtime / 355 | \| Maximum daily working time under the stated derogation \| 12 hours where the collective-agreement derogation covers increased activity or organisational need; other departures require the inspector’s approval or the stated emergency route \| "Soit si une convention collective ... le prévoit" / "limitée à 12 heures par jour" \| | [T355_0](#t355_0) | legal/official selected rule |
| france-payroll-unit-0222 / Working Hours and Overtime / 356 | \| Ordinary maximum in a single week \| 48 hours; up to60 only for exceptional circumstances with inspection approval \| "Soit 48 heures sur une même semaine" \| | [T356_0](#t356_0); [PAY_WEEKLY_DEROG](#pay_weekly_derog) | legal/official selected rule |
| france-payroll-unit-0223 / Working Hours and Overtime / 357 | \| Ordinary maximum average over 12 consecutive weeks \| 44 hours; up to46 over12 consecutive weeks under the stated collective/company agreement or inspection authorisation \| "Soit 44 heures par semaine en moyenne sur une période de 12 semaines consécutives" \| | [T357_0](#t357_0); [PAY_WEEKLY_DEROG](#pay_weekly_derog) | legal/official selected rule |
| france-payroll-unit-0224 / Working Hours and Overtime / 359 | \| Rule \| Value \| Page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0225 / Working Hours and Overtime / 361 | \| Source \| all figures below \| https://www.service-public.gouv.fr/particuliers/vosdroits/F2391 \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0226 / Working Hours and Overtime / 362 | \| Overtime premium, first 8 overtime hours in the week, 36th to 43rd hour, where no collective agreement sets a rate \| 25% \| "25 % pour les 8 premières heures supplémentaires travaillées dans la même semaine (de la 36 e à la 43 e heure)" \| | [T362_0](#t362_0) | legal/official selected rule |
| france-payroll-unit-0227 / Working Hours and Overtime / 363 | \| Overtime premium, hours after that, from the 44th hour, where no collective agreement sets a rate \| 50% \| "50 % pour les heures suivantes (à partir de la 44 e heure)" \| | [T363_0](#t363_0) | legal/official selected rule |
| france-payroll-unit-0228 / Working Hours and Overtime / 364 | \| Floor for any premium rate set by a collective agreement \| 10% \| "Chaque taux est au minimum fixé à 10 %" \| | [T364_0](#t364_0) | legal/official selected rule |
| france-payroll-unit-0229 / Working Hours and Overtime / 365 | \| Part-time complementary hours, within one tenth of the contract hours \| 10% \| "Soit 10 % pour chaque heure complémentaire accomplie dans la limite de 1/10 e" \| | [T365_0](#t365_0) | legal/official selected rule |
| france-payroll-unit-0230 / Working Hours and Overtime / 366 | \| Part-time complementary hours, beyond one tenth \| 25% \| "Soit 25 % pour chaque heure accomplie au-delà de 1/10 e" \| | [T366_0](#t366_0) | legal/official selected rule |
| france-payroll-unit-0231 / Working Hours and Overtime / 367 | \| Annual overtime quota where no collective agreement sets one \| 220 hours \| "le nombre maximal d'heures supplémentaires est de 220 heures par salarié et par an" \| | [T367_0](#t367_0) | legal/official selected rule |
| france-payroll-unit-0232 / Working Hours and Overtime / 369 | Conditions that change the answer. The premiums above are the fallback. Where a collective agreement, a company agreement or an extended branch agreement sets rates, those rates apply and only the floor above binds them. Overtime is counted by calendar week. Where working time is counted by the week or over two weeks, paid leave taken in that period counts as time worked for the overtime count, so the hours the employee would have worked count towards the threshold. Pay for overtime can be replaced in whole or in part by equivalent compensatory rest, and the rest must equal the premium-inclusive pay. The annual quota is also set by agreement first, and the figure above applies only where none of the three kinds of agreement exists. | [OVERTIMEPREM](#overtimeprem); [OVERTIMEWEEK](#overtimeweek); [LEAVEOVERTIME](#leaveovertime) | legal/official selected rule |
| france-payroll-unit-0233 / Congés Payés (Paid Annual Leave) / 375 | \| Entitlement \| Value \| Page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0234 / Congés Payés (Paid Annual Leave) / 377 | \| Source \| all figures below \| https://www.service-public.gouv.fr/particuliers/vosdroits/F2258 \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0235 / Congés Payés (Paid Annual Leave) / 378 | \| Accrual per month of actual work \| 2.5 working days \| "ouvre droit à un congé de 2,5 jours ouvrables" \| | [T378_0](#t378_0) | legal/official selected rule |
| france-payroll-unit-0236 / Congés Payés (Paid Annual Leave) / 379 | \| Full year \| 30 working days, five weeks \| "30 jours ouvrables (5 semaines) pour une année complète de travail" \| | [T379_0](#t379_0) | legal/official selected rule |
| france-payroll-unit-0237 / Congés Payés (Paid Annual Leave) / 380 | \| Accrual during sick leave that is not work related \| 2 working days per month, 24 a year \| "dans la limite de 2 jours ouvrables par mois (soit 24 jours ouvrables par an)" \| | [LEAVEYEAR](#leaveyear) | legal/official selected rule |
| france-payroll-unit-0238 / Congés Payés (Paid Annual Leave) / 381 | \| Reference period \| 1 June of year N-1 to 31 May of year N, unless an agreement sets another \| "du 1 er juin de l'année N-1 au 31 mai de l'année N" \| | [T381_0](#t381_0) | legal/official selected rule |
| france-payroll-unit-0239 / Congés Payés (Paid Annual Leave) / 382 | \| Main leave period \| 1 May to 31 October \| "du 1 er mai au 31 octobre de l'année en cours" \| | [T382_0](#t382_0) | legal/official selected rule |
| france-payroll-unit-0240 / Congés Payés (Paid Annual Leave) / 383 | \| Leave that must be taken in the main period to earn fractionnement days \| 12 working days, two weeks \| "un congé d'au moins 12 jours ouvrables (soit 2 semaines)" \| | [FRACTION](#fraction) | legal/official selected rule |
| france-payroll-unit-0241 / Congés Payés (Paid Annual Leave) / 385 | A part-day of accrued leave is rounded up to the next whole day. The fractionnement rules themselves are set by the collective agreement. If the applicable convention or agreement does not stipulate the rules, Code du travail L3141-23 supplies the fallback: a continuous minimum twelve working days between 1 May and 31 October; for the part of principal leave beyond twelve days taken outside that period, one extra working day for three to five days, or two for at least six. Principal leave above twenty-four working days does not count for that supplement, and an individual agreement may derogate. Source: https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000033020705/2026-03-03 . | [LEAVEYEAR](#leaveyear); [FRACTION](#fraction) | legal/official selected rule |
| france-payroll-unit-0242 / Sick Leave (Arrêt Maladie) / 389 | \| Item \| Value \| Page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0243 / Sick Leave (Arrêt Maladie) / 391 | \| Source \| all figures below \| https://www.service-public.gouv.fr/particuliers/vosdroits/F3053 \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0244 / Sick Leave (Arrêt Maladie) / 392 | \| Daily allowance from the health scheme \| 50% of the daily base salary \| "Les indemnités journalières (IJ) sont égales à 50 % du salaire journalier de base" \| | [T392_0](#t392_0) | legal/official selected rule |
| france-payroll-unit-0245 / Sick Leave (Arrêt Maladie) / 393 | \| Daily base salary for a monthly paid employee \| The last three gross salaries before the stoppage, divided by 91.25 \| "au total des 3 derniers salaires bruts perçus avant l'arrêt de travail, divisé par 91,25" \| | [T393_0](#t393_0) | legal/official selected rule |
| france-payroll-unit-0246 / Sick Leave (Arrêt Maladie) / 394 | \| Pay taken into account, capped \| 1.4 times the Smic in force on the last day of the month before the stoppage. The page states the 2026 cap as EUR 2,613.82 a month, which is built on the Smic in force from 1 June 2026, so it governs a stoppage beginning on or after 1 July 2026 \| "est plafonné à 1,4 fois le montant du Smic en vigueur, lors du dernier jour du mois qui précède l'arrêt (soit 2 613,82 € par mois en 2026)" \| | [T394_0](#t394_0) | legal/official selected rule |
| france-payroll-unit-0247 / Sick Leave (Arrêt Maladie) / 395 | \| Cap for a stoppage that began before 1 April 2025 \| 1.8 times the Smic, the old ceiling \| "Pour les arrêts ayant débuté avant le 1ᵉʳ avril 2025, l’ancien plafond reste applicable" \| | [T395_0](#t395_0) | legal/official selected rule |
| france-payroll-unit-0248 / Sick Leave (Arrêt Maladie) / 396 | \| Maximum daily allowance using the June-based monthly cap, for a stoppage beginning from 1 July 2026 \| EUR 42.97; for an earlier 2026 stoppage recompute from the prior-month Smic gate above \| "Les IJ ne peuvent pas dépasser 42,97 € bruts" \| | [T396_0](#t396_0) | legal/official selected rule |
| france-payroll-unit-0249 / Sick Leave (Arrêt Maladie) / 397 | \| Waiting period before the allowance starts \| 3 days \| "Les IJ sont versées après un délai de carence de 3 jours" \| | [SICKWAIT](#sickwait) | legal/official selected rule |
| france-payroll-unit-0250 / Sick Leave (Arrêt Maladie) / 399 | Ordinary sickness IJ entitlement is separate from the amount calculation. For the first six months, CSS R313-3(1) requires either 150 salaried or assimilated hours in the preceding three calendar months or 90 days, or six-month insurance contributions equivalent to those on 1,015 hourly Smic valued at the first day of the reference period; assess at the work-interruption date under R313-1(2). Beyond six continuous months, R313-3(2) requires twelve months of affiliation plus either 600 hours in the preceding twelve months or 365 days, or the stated twelve-month contributions equivalent to 2,030 hourly Smic valued at the 1 January preceding the reference period. Seasonal/discontinuous and other special histories must follow their own source rules. Do not substitute stale fixed-euro thresholds for those statutory Smic gates. Source: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047983348/2026-09-29 . | [SICKGATES](#sickgates); [SICKLONG](#sicklong); [SICKDATE](#sickdate) | legal/official selected rule |
| france-payroll-unit-0251 / Sick Leave (Arrêt Maladie) / 401 | **Employer top-up (indemnites complementaires)** |  | presentation subheading |
| france-payroll-unit-0252 / Sick Leave (Arrêt Maladie) / 403 | \| Seniority \| Maximum period paid \| Page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0253 / Sick Leave (Arrêt Maladie) / 405 | \| Source \| all figures below \| https://www.service-public.gouv.fr/particuliers/vosdroits/F3053 \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0254 / Sick Leave (Arrêt Maladie) / 406 | \| 1 to 5 years \| 60 days: 30 days at 90% then 30 days at 66.66% \| "De 1 à 5 ans 60 jours (30 jours à 90 % et 30 jours à 66,66 % )" \| | [T406_0](#t406_0) | legal/official selected rule |
| france-payroll-unit-0255 / Sick Leave (Arrêt Maladie) / 407 | \| 6 to 10 years \| 80 days: 40 days at 90% then 40 days at 66.66% \| "De 6 à 10 ans 80 jours (40 jours à 90 % et 40 jours à 66,66 % )" \| | [T407_0](#t407_0) | legal/official selected rule |
| france-payroll-unit-0256 / Sick Leave (Arrêt Maladie) / 408 | \| 11 to 15 years \| 100 days: 50 days at 90% then 50 days at 66.66% \| "De 11 à 15 ans 100 jours (50 jours à 90 % et 50 jours à 66,66 % )" \| | [T408_0](#t408_0) | legal/official selected rule |
| france-payroll-unit-0257 / Sick Leave (Arrêt Maladie) / 409 | \| 16 to 20 years \| 120 days: 60 days at 90% then 60 days at 66.66% \| "De 16 à 20 ans 120 jours (60 jours à 90 % et 60 jours à 66,66 % )" \| | [T409_0](#t409_0) | legal/official selected rule |
| france-payroll-unit-0258 / Sick Leave (Arrêt Maladie) / 410 | \| 21 to 25 years \| 140 days: 70 days at 90% then 70 days at 66.66% \| "De 21 à 25 ans 140 jours (70 jours à 90 % et 70 jours à 66,66 % )" \| | [T410_0](#t410_0) | legal/official selected rule |
| france-payroll-unit-0259 / Sick Leave (Arrêt Maladie) / 411 | \| 26 to 30 years \| 160 days: 80 days at 90% then 80 days at 66.66% \| "De 26 à 30 ans 160 jours (80 jours à 90 % et 80 jours à 66,66 % )" \| | [T411_0](#t411_0) | legal/official selected rule |
| france-payroll-unit-0260 / Sick Leave (Arrêt Maladie) / 412 | \| 31 years and more \| 180 days: 90 days at 90% then 90 days at 66.66% \| "31 ans et plus 180 jours (90 jours à 90 % et 90 jours à 66,66 % )" \| | [T412_0](#t412_0) | legal/official selected rule |
| france-payroll-unit-0261 / Sick Leave (Arrêt Maladie) / 413 | \| Waiting period before the ordinary sickness employer top-up starts \| 7 days, so the top-up begins on the 8th day; work accidents and occupational disease start on the first absence day, excluding commuting accidents \| "au-delà de sept jours d’absence" / "premier jour d’absence" (Code du travail D1226-3) \| | [T413_0](#t413_0); [T413_1](#t413_1) | legal/official selected rule |
| france-payroll-unit-0262 / Sick Leave (Arrêt Maladie) / 415 | Conditions. The top-up needs at least one year of service at the first day of absence, and the medical certificate must reach **the employer** within 48 hours. The employee must qualify for social-security daily benefits, be treated in France or the EEA, and not be a home worker, seasonal, intermittent or temporary worker. The 90% and two-thirds levels are total replacement targets: subtract the full nominal social-security daily allowance even if its actual payment is reduced for hospitalisation or a CPAM sanction, and the employer-funded share of provident benefits to obtain the employer top-up (Code du travail D1226-1 and D1226-5). Two different waiting periods run at once and must not be confused: three days on the health scheme allowance and seven days on the employer top-up, the top-up beginning on the eighth day unless a collective agreement is more favourable. There is no waiting period on the health scheme allowance where there was a return to work between two stoppages and that return did not exceed 48 hours ("reprise d'activité entre 2 arrêts de travail n'ayant pas dépassé 48 heures"), or where the stoppages follow an affection de longue duree. The employer top-up starts on the first absence day for a work accident or occupational disease, excluding a commuting accident. This is distinct from the health-scheme work-accident benefit: the employer pays the accident day and the caisse benefit starts the day after the resulting stoppage (CSS L433-1). Sources: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000019225874/2026-03-07 and https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000053283560/2026-02-15 . Periods already paid in the previous twelve months reduce what is left. The Smic used for the cap is the one in force on the last day of the month before the stoppage. A stoppage beginning in June 2026 still takes the last day of May, which is inside the January to May Smic period, so its cap is 1.4 times the January 2026 monthly Smic in the Smic table in Section 5, not the monthly cap printed in the table above. No allowed page prints that January-based cap as an amount, so work it from the two figures and show the working. Only a stoppage beginning on or after 1 July 2026 takes the printed cap. | [TOPUPGATES](#topupgates); [TOPUPOFFSET](#topupoffset); [TOPUPHISTORY](#topuphistory); [TOPUPDAY](#topupday); [ATDAY](#atday); [SICKEXCEPT](#sickexcept); [SICKBASE](#sickbase); [SICKLAW](#sicklaw) | legal/official selected rule |
| france-payroll-unit-0263 / Maternity Leave (Congé de Maternité) / 419 | \| Case \| Duration \| Page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0264 / Maternity Leave (Congé de Maternité) / 421 | \| Source \| all figures below \| https://www.service-public.gouv.fr/particuliers/vosdroits/F2265 \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0265 / Maternity Leave (Congé de Maternité) / 422 | \| First child \| 6 weeks before, 10 weeks after, 16 weeks in total \| "1 er enfant 6 semaines 10 semaines 16 semaines" \| | [T422_0](#t422_0) | legal/official selected rule |
| france-payroll-unit-0266 / Maternity Leave (Congé de Maternité) / 423 | \| Second child \| 6 weeks before, 10 weeks after, 16 weeks in total \| "2 e enfant 6 semaines 10 semaines 16 semaines" \| | [T423_0](#t423_0) | legal/official selected rule |
| france-payroll-unit-0267 / Maternity Leave (Congé de Maternité) / 424 | \| Third child or more \| 8 weeks before, 18 weeks after, 26 weeks in total \| "3 e enfant ou plus 8 semaines 18 semaines 26 semaines" \| | [T424_0](#t424_0) | legal/official selected rule |
| france-payroll-unit-0268 / Maternity Leave (Congé de Maternité) / 425 | \| Twins \| 12 weeks before, 22 weeks after, 34 weeks in total \| "2 12 semaines 22 semaines 34 semaines" \| | [T425_0](#t425_0) | legal/official selected rule |
| france-payroll-unit-0269 / Maternity Leave (Congé de Maternité) / 426 | \| Three or more babies \| 24 weeks before, 22 weeks after, 46 weeks in total \| "3 ou plus 24 semaines 22 semaines 46 semaines" \| | [T426_0](#t426_0) | legal/official selected rule |
| france-payroll-unit-0270 / Maternity Leave (Congé de Maternité) / 428 | The count for a first or second child is by the number of children already dependent before the birth, not by birth order alone. The employee may give up part of the leave but must stop work for at least eight weeks, six of them after the birth. Pay during the leave comes from the health scheme as daily maternity allowances; the contract is suspended and the employer pays no salary unless an agreement says otherwise. For an eligible monthly-paid employee, F2265 now supplies the daily benefit calculation: take the sum of the three preceding gross monthly salaries, each within the applicable PMSS, divide by 91.25 and apply the 21% forfait deduction. The page prints a minimum EUR 11.12 and maximum EUR 104.02 per day for its current 2026 presentation; use the prior-month ceiling gate, not an assumed unchanged prior-year PMSS. Ordinary eligibility requires six months of affiliation at the presumed delivery date and, under R313-3(1), either 150 salaried/assimilated hours in the preceding three calendar months or 90 days, or sufficient six-month insurance contributions measured against 1,015 hourly Smic at the start of the reference period. Assess the work/contribution tests at the maternity dates in R313-1(3); cessation for at least eight weeks including six post-birth weeks remains required. Seasonal/discontinuous and unemployed cases have their own alternative histories on the source page and are not established by the ordinary test alone. Sources: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047983348/2026-09-29 and https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006156797/?anchor=LEGIARTI000006749178 . After the maternity leave the employee may take the congé supplémentaire de naissance; its length and pay are on its own service-public page and are not covered here. | [MATERNITYSTOP](#maternitystop); [MATERNITYCONTRACT](#maternitycontract); [MATERNITYCALC](#maternitycalc); [SICKGATES](#sickgates); [MATDATE](#matdate) | legal/official selected rule |
| france-payroll-unit-0271 / Paternity Leave (Congé de Paternité) / 432 | \| Item \| Duration \| Page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0272 / Paternity Leave (Congé de Paternité) / 434 | \| Source \| all figures below \| https://www.service-public.gouv.fr/particuliers/vosdroits/F3156 \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0273 / Paternity Leave (Congé de Paternité) / 435 | \| Conge de naissance, which must come first \| 3 working days \| "précédé du congé de naissance d'une durée de 3 jours ouvrables" \| | [T435_0](#t435_0) | legal/official selected rule |
| france-payroll-unit-0274 / Paternity Leave (Congé de Paternité) / 436 | \| Conge de paternite et d'accueil de l'enfant, one child \| 25 calendar days \| "La durée du congé de paternité et d'accueil de l'enfant est de 25 jours calendaires" \| | [T436_0](#t436_0) | legal/official selected rule |
| france-payroll-unit-0275 / Paternity Leave (Congé de Paternité) / 437 | \| Conge de paternite et d'accueil de l'enfant, more than one child \| 32 calendar days \| "La durée du congé de paternité et d'accueil de l'enfant est de 32 jours calendaires" \| | [T437_0](#t437_0) | legal/official selected rule |
| france-payroll-unit-0276 / Paternity Leave (Congé de Paternité) / 438 | \| Period the employee must take straight after the conge de naissance \| 4 calendar days \| "il doit prendre la 1 re période de 4 jours calendaires" \| | [T438_0](#t438_0) | legal/official selected rule |
| france-payroll-unit-0277 / Paternity Leave (Congé de Paternité) / 440 | The leave must be taken within six months of the birth or arrival of the child. After it the employee may take the congé supplémentaire de naissance; its length and pay are on its own service-public page and are not covered here. | [PATERNITY](#paternity) | legal/official selected rule |
| france-payroll-unit-0278 / 13th Month (Treizième Mois) / 444 | No statutory obligation. It is common under collective agreements or company policy. Where it is contractual it is pay: it bears all contributions and it goes into the withholding base. | [PRIMES](#primes); [PRIMESCONTRIB](#primescontrib); [PASRATE](#pasrate) | legal/official selected rule |
| france-payroll-unit-0279 / Mutuelle Obligatoire (Compulsory Health Insurance) / 448 | \| Item \| Value \| Page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0280 / Mutuelle Obligatoire (Compulsory Health Insurance) / 450 | \| Source \| all figures below \| https://entreprendre.service-public.gouv.fr/vosdroits/F33754 \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0281 / Mutuelle Obligatoire (Compulsory Health Insurance) / 451 | \| Minimum employer share of the premium \| 50% \| "La participation financière de l'employeur doit être au moins égale à 50 % de la cotisation" \| | [T451_0](#t451_0) | legal/official selected rule |
| france-payroll-unit-0282 / Mutuelle Obligatoire (Compulsory Health Insurance) / 452 | \| Dental cover in the minimum basket \| 125% of the agreed tariff \| "Frais dentaires (prothèses et orthodontie) à hauteur de 125 % du tarif conventionnel" \| | [T452_0](#t452_0) | legal/official selected rule |
| france-payroll-unit-0283 / Mutuelle Obligatoire (Compulsory Health Insurance) / 454 | The cover must meet a minimum basket of care: the whole of the ticket moderateur on consultations, acts and services reimbursed by the health scheme, with exceptions; the whole of the daily hospital charge; and the dental and optical minimums. Cover is compulsory for employees except in the cases where an employee is allowed to refuse. Free continued cover requires a termination other than faute lourde that opens unemployment-insurance entitlement and cover rights already opened with the last employer. It lasts during compensated unemployment, capped by the last contract or consecutive contracts with that employer, rounded up to whole months, and at most twelve months. The former employee must evidence continuing eligibility; the employer records portability on the employment certificate and informs the insurer (CSS L911-8: https://www.legifrance.gouv.fr/codes/id/LEGIARTI000006745464/2026-07-11). The employer's contribution to this cover is itself charged to CSG and CRDS, with no professional-costs allowance. | [MUTUELLEGATES](#mutuellegates); [MUTUELLEBASKET](#mutuellebasket); [PORTABILITY](#portability); [CSGHEALTH](#csghealth) | legal/official selected rule |
| france-payroll-unit-0284 / Avantages en Nature and Frais Professionnels / 458 | These are the pay elements most often mis-entered. A benefit in kind is pay and bears contributions; an expense allowance inside the limit does not. The company-car forfait depends on the date the vehicle was first made available to the employee, not the date of the payroll run: a car handed over before 1 February 2025 and still in use is valued on the older, lower schedule below, not on the newer one, even in a 2026 payroll. | [EXPENSEGATE](#expensegate); [PRIMES](#primes) | legal/official selected rule |
| france-payroll-unit-0285 / Avantages en Nature and Frais Professionnels / 460 | \| Item \| Value \| Page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0286 / Avantages en Nature and Frais Professionnels / 462 | \| Source \| all figures below \| https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0287 / Avantages en Nature and Frais Professionnels / 463 | \| Meal provided, one meal \| EUR 5.50 \| "Montant de l'avantage en 2026 1 repas 5,50 €" \| | [T463_0](#t463_0) | legal/official selected rule |
| france-payroll-unit-0288 / Avantages en Nature and Frais Professionnels / 464 | \| Meal provided, two meals \| EUR 11.00 \| "2 repas 11,00 €" \| | [T464_0](#t464_0) | legal/official selected rule |
| france-payroll-unit-0289 / Avantages en Nature and Frais Professionnels / 465 | \| Luncheon voucher, maximum exempt employer share \| EUR 7.32 \| "Exonération maximale de la part patronale 7,32 €" \| | [T465_0](#t465_0) | legal/official selected rule |
| france-payroll-unit-0290 / Avantages en Nature and Frais Professionnels / 466 | \| Luncheon voucher face value that carries the maximum exemption, lower end \| EUR 12.20 \| "Entre 12,20 € et 14,64 €" \| | [T466_0](#t466_0) | legal/official selected rule |
| france-payroll-unit-0291 / Avantages en Nature and Frais Professionnels / 467 | \| Luncheon voucher face value that carries the maximum exemption, upper end \| EUR 14.64 \| "Entre 12,20 € et 14,64 €" \| | [T467_0](#t467_0) | legal/official selected rule |
| france-payroll-unit-0292 / Avantages en Nature and Frais Professionnels / 468 | \| Company car, vehicle made available since 1 February 2025, bought, five years old or less \| 15% of the purchase cost \| "Véhicule acheté âgé de 5 ans ou moins 15 % du coût d'achat" \| | [T468_0](#t468_0) | legal/official selected rule |
| france-payroll-unit-0293 / Avantages en Nature and Frais Professionnels / 469 | \| Same car, employer pays the private fuel \| 20% of the purchase cost \| "15 % du coût d'achat + frais réels sur factures de carburant utilisé à des fins personnelles ou 20 % du coût d'achat" \| | [T469_0](#t469_0) | legal/official selected rule |
| france-payroll-unit-0294 / Avantages en Nature and Frais Professionnels / 470 | \| Company car, vehicle made available since 1 February 2025, bought, more than five years old \| 10% of the purchase cost \| "Véhicule acheté de plus de 5 ans 10 % du coût d'achat" \| | [T470_0](#t470_0) | legal/official selected rule |
| france-payroll-unit-0295 / Avantages en Nature and Frais Professionnels / 471 | \| Same car, employer pays the private fuel \| 15% of the purchase cost \| "10 % du coût d'achat + frais réels sur factures de carburant utilisé à des fins personnelles ou 15 % du coût d'achat" \| | [T471_0](#t471_0) | legal/official selected rule |
| france-payroll-unit-0296 / Avantages en Nature and Frais Professionnels / 472 | \| Company car, vehicle made available since 1 February 2025, leased \| 50% of annual lease, maintenance and insurance costs \| "Véhicule loué ou en location avec option d’achat (LOA) 50 % du coût global annuel (location, entretien, assurance)" \| | [T472_0](#t472_0) | legal/official selected rule |
| france-payroll-unit-0297 / Avantages en Nature and Frais Professionnels / 473 | \| Same car, employer pays the private fuel \| 50% of annual lease/maintenance/insurance PLUS actual invoiced private fuel, OR67% of global annual lease/maintenance/insurance plus private AND professional fuel and all related taxes \| "50 % du coût global annuel (location, entretien, assurance) + frais réels sur factures de carburant utilisé à des fins personnelles ou 67 % du coût global" \| | [T473_0](#t473_0) | legal/official selected rule |
| france-payroll-unit-0298 / Avantages en Nature and Frais Professionnels / 474 | \| Company car, vehicle made available before 1 February 2025, bought, five years old or less \| 9% of the purchase cost \| "Véhicule acheté âgé de 5 ans ou moins 9 % du coût d'achat" \| | [T474_0](#t474_0) | legal/official selected rule |
| france-payroll-unit-0299 / Avantages en Nature and Frais Professionnels / 475 | \| Same car, employer pays the private fuel \| 12% of the purchase cost \| "9 % du coût d'achat + frais réels sur factures de carburant utilisé à des fins personnelles ou 12 % du coût d'achat" \| | [T475_0](#t475_0) | legal/official selected rule |
| france-payroll-unit-0300 / Avantages en Nature and Frais Professionnels / 476 | \| Company car, vehicle made available before 1 February 2025, bought, more than five years old \| 6% of the purchase cost \| "Véhicule acheté de plus de 5 ans 6 % du coût d'achat" \| | [T476_0](#t476_0) | legal/official selected rule |
| france-payroll-unit-0301 / Avantages en Nature and Frais Professionnels / 477 | \| Same car, employer pays the private fuel \| 9% of the purchase cost \| "6 % du coût d'achat + frais réels sur factures de carburant utilisé à des fins personnelles ou 9 % du coût d'achat" \| | [T477_0](#t477_0) | legal/official selected rule |
| france-payroll-unit-0302 / Avantages en Nature and Frais Professionnels / 478 | \| Company car, vehicle made available before 1 February 2025, leased \| 30% of the yearly total cost \| "Véhicule loué ou en location avec option d’achat (LOA) 30 % du coût global annuel TTC (location, entretien, assurance)" \| | [T478_0](#t478_0) | legal/official selected rule |
| france-payroll-unit-0303 / Avantages en Nature and Frais Professionnels / 479 | \| Same car, employer pays the private fuel \| 40% of the yearly total cost \| "30 % du coût global annuel TTC (location, entretien, assurance) + frais de carburant sur facture o u 4 0 % du coût global" \| | [T479_0](#t479_0) | legal/official selected rule |
| france-payroll-unit-0304 / Avantages en Nature and Frais Professionnels / 480 | \| Leased company car, either schedule, cap \| Capped at the hypothetical purchased-car benefit under the applicable schedule. Its reference purchase price is the lessor’s actual VAT-inclusive price, with the discount capped at30% of the manufacturer’s advised price at contract start \| "L'avantage évalué pour un véhicule loué est plafonné au montant de l'avantage en nature qui aurait été évalué si l'employeur avait acheté le véhicule" \| | [T480_0](#t480_0) | legal/official selected rule |
| france-payroll-unit-0305 / Avantages en Nature and Frais Professionnels / 481 | \| Electric vehicle, made available since 1 February 2025, meeting the environmental score required for the bonus écologique \| 70% reduction of the benefit on the schedule above, the reduction being limited to EUR 4,641.60 a year in 2026 \| "Si le véhicule respecte le score environnemental requis pour bénéficier du bonus écologique, vous utilisez le barème ci-dessus auquel vous appliquez une réduction de 70 % sur le montant de l’avantage en nature, dans la limite de 4 641,60 € par an en 2026" \| | [T481_0](#t481_0) | legal/official selected rule |
| france-payroll-unit-0306 / Avantages en Nature and Frais Professionnels / 482 | \| Electric vehicle made available before 1 February 2025 \| 50% reduction of the benefit on the schedule above, the reduction being limited to EUR 2,026.30 a year in 2026 \| "Vous utilisez le barème ci-dessus auquel vous appliquez une réduction de 50 %, dans la limite de 2 026,30 € par an en 2026" \| | [T482_0](#t482_0) | legal/official selected rule |
| france-payroll-unit-0307 / Avantages en Nature and Frais Professionnels / 483 | \| Electric vehicle, either schedule \| Electricity the employer pays for is excluded from the benefit-in-kind calculation \| "Les frais d'électricité pris en charge par l’employeur n’entrent pas en compte dans le calcul de l’avantage en nature" \| | [T483_0](#t483_0) | legal/official selected rule |
| france-payroll-unit-0308 / Avantages en Nature and Frais Professionnels / 485 | \| Item \| Value \| Page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0309 / Avantages en Nature and Frais Professionnels / 487 | \| Source \| all figures below \| https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/frais-professionnels.html \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0310 / Avantages en Nature and Frais Professionnels / 488 | \| Meal allowance, employee forced to eat at the workplace \| EUR 7.50 \| "Salarié contraint de prendre son repas sur le lieu de travail 7,50 €" \| | [T488_0](#t488_0) | legal/official selected rule |
| france-payroll-unit-0311 / Avantages en Nature and Frais Professionnels / 489 | \| Meal allowance, employee travelling and forced to eat in a restaurant \| EUR 21.40 \| "Salarié en situation de déplacement contraint de prendre son repas au restaurant 21,40 €" \| | [T489_0](#t489_0) | legal/official selected rule |
| france-payroll-unit-0312 / Avantages en Nature and Frais Professionnels / 490 | \| Meal allowance, employee travelling but not forced to eat in a restaurant \| EUR 10.40 \| "non contraint de prendre son repas au restaurant 10,40 €" \| | [T490_0](#t490_0) | legal/official selected rule |
| france-payroll-unit-0313 / Avantages en Nature and Frais Professionnels / 491 | \| Telework allowance, no collective agreement, per day \| EUR 2.70 \| "Par jour de télétravail 2,70 € dans la limite de 59,40 € par mois" \| | [T491_0](#t491_0) | legal/official selected rule |
| france-payroll-unit-0314 / Avantages en Nature and Frais Professionnels / 492 | \| Telework allowance, no collective agreement, monthly cap \| EUR 59.40 \| "2,70 € dans la limite de 59,40 € par mois" \| | [T492_0](#t492_0) | legal/official selected rule |
| france-payroll-unit-0315 / Avantages en Nature and Frais Professionnels / 493 | \| Telework allowance under a collective agreement, per day \| EUR 3.30 \| "Par jour de télétravail 3,30 € dans la limite de 72,60 € par mois" \| | [T493_0](#t493_0) | legal/official selected rule |
| france-payroll-unit-0316 / Avantages en Nature and Frais Professionnels / 494 | \| Telework allowance under a collective agreement, monthly cap \| EUR 72.60 \| "3,30 € dans la limite de 72,60 € par mois" \| | [T494_0](#t494_0) | legal/official selected rule |
| france-payroll-unit-0317 / Avantages en Nature and Frais Professionnels / 496 | \| Item \| Value \| Page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0318 / Avantages en Nature and Frais Professionnels / 498 | \| Source \| all figures below \| https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/prime-partage-valeur.html \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0319 / Avantages en Nature and Frais Professionnels / 499 | \| Prime de partage de la valeur, exempt from contributions up to \| EUR 3,000 \| "exonérée de cotisations et contributions sociales dans la limite de 3 000 €" \| | [T499_0](#t499_0) | legal/official selected rule |
| france-payroll-unit-0320 / Avantages en Nature and Frais Professionnels / 500 | \| Same cap where the employer has a profit-sharing scheme in the conditions on the page \| EUR 6,000 \| "Cette limite d’exonération passe à 6 000 € par bénéficiaire et par an" \| | [T500_0](#t500_0) | legal/official selected rule |
| france-payroll-unit-0321 / Avantages en Nature and Frais Professionnels / 501 | \| Forfait social on the prime, employer with at least 250 employees \| 20% \| "le forfait social au taux de 20 % est dû si l’effectif de votre entreprise est égal ou supérieur à 250 salariés" \| | [T501_0](#t501_0) | legal/official selected rule |
| france-payroll-unit-0322 / Avantages en Nature and Frais Professionnels / 503 | The EUR 3,000/6,000 contribution exemption is per beneficiary and calendar year. For the ordinary EUR 6,000 route, an employer subject to compulsory participation needs intéressement; an employer not subject to it may use intéressement or participation, implemented by payment or concluded for the same financial year. The page separately exempts specified public-interest associations/foundations and Esat from that scheme condition. Through 31 December 2026, the wider CSG/CRDS and income-tax exemption requires both fewer than 50 employees and pay below three annual Smic; do not infer it from the basic social-contribution exemption. The prime de partage de la valeur counts in annual gross pay for the single degressive relief, whether or not it is paid into a savings plan. | [PPVGATES](#ppvgates); [PPVWIDE](#ppvwide); [RGDUPPV](#rgduppv) | legal/official selected rule |
| france-payroll-unit-0323 / Section 7: Payslip Requirements / 507 | The bulletin de paie is governed by the Code du travail. The list below is the list the official page gives. | [PAYSLIPZONES](#payslipzones) | legal/official selected rule |
| france-payroll-unit-0324 / Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) / 511 | \| Zone \| Required fields \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0325 / Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) / 513 | \| Zone 1, identification of employer and employee \| Employer name and address, and the establishment the employee belongs to; the APE or NAF activity code and the employer's Siret; the applicable branch collective agreement, or a reference to the Code du travail on leave and notice; the employee's name, job and position in the agreement's classification; the period and the number of hours worked, separating normal hours from overtime and showing the rate applied to each; the nature and volume of the forfait for an employee on a forfait contract; the nature of the basis of pay where that basis is not working time; and the nature and amount of any salary accessories bearing contributions \| | [PAYSLIPZONES](#payslipzones) | legal/official selected rule |
| france-payroll-unit-0326 / Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) / 514 | \| Zone 2, pay \| The employee's gross pay; the base and amount of the employer's and the employee's contributions before exemptions are deducted; the employee's contribution rates before exemptions are deducted; the nature and amount of other payments and deductions, in particular the home-to-work transport reimbursement; the amount actually received by the employee; the date of payment; and, where a period of annual leave falls in the pay period, the leave dates and the amount of the holiday pay \| | [PAYSLIPZONES](#payslipzones) | legal/official selected rule |
| france-payroll-unit-0327 / Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) / 515 | \| Zone 3, contributions and reliefs \| Contributions and contributions grouped under five headings, health, work accidents and occupational illness, retirement, family and unemployment, with base, rate and amount; the total of exemptions and reliefs; the total paid by the employer; and the line for the change in pay caused by removing the employee unemployment and health contributions \| | [PAYSLIPZONES](#payslipzones) | legal/official selected rule |
| france-payroll-unit-0328 / Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) / 516 | \| Zone 4, net to pay and net taxable \| Net to pay before income tax, and the income tax withheld at source \| | [PAYSLIPZONES](#payslipzones) | legal/official selected rule |
| france-payroll-unit-0329 / Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) / 517 | \| Zone 5, montant net social \| Net income after all compulsory social deductions, the figure the employee reports to the family allowance fund \| | [PAYSLIPZONES](#payslipzones) | legal/official selected rule |
| france-payroll-unit-0330 / Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) / 518 | \| Zone 6, income tax \| Net taxable amount used as the withholding base, its year to date total, the tax withheld, its year to date total, and the net exempt amount of overtime and complementary hours with its year to date total \| | [PAYSLIPZONES](#payslipzones) | legal/official selected rule |
| france-payroll-unit-0331 / Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) / 519 | \| Zone 7, final wording \| A pointer to the payslip page on the service-public portal, the wording telling the employee to keep the payslip with no time limit, and, where short-time working applies, the number of hours compensated \| | [PAYSLIPZONES](#payslipzones) | legal/official selected rule |
| france-payroll-unit-0332 / Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) / 521 | Source for this list: https://entreprendre.service-public.gouv.fr/vosdroits/F559 |  | source pointer |
| france-payroll-unit-0333 / Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) / 523 | The montant net social line and the seven-zone layout came in with the version of the payslip that applies since 1 July 2023. The page also sets out the earlier layout that applies since 2022. Special rules apply to employees in the local health scheme of Haut-Rhin, Bas-Rhin and Moselle: only the employee rate and the employee share are shown. | [PAYSLIPZONES](#payslipzones); [PAYSLIPCHALLENGE](#payslipchallenge) | legal/official selected rule |
| france-payroll-unit-0334 / Delivery / 527 | - Electronic delivery is the rule and paper the exception, since 2017. This is the opposite of the old position. The employee can refuse electronic delivery and must tell the employer. | [PAYSLIPDELIVERY](#payslipdelivery) | legal/official selected rule |
| france-payroll-unit-0335 / Delivery / 528 | - The employer must keep a copy at the business for five years, on paper or electronically. | [PAYSLIPDELIVERY](#payslipdelivery) | legal/official selected rule |
| france-payroll-unit-0336 / Delivery / 529 | - After those five years the payslips need not be reachable inside the business, but they must not be destroyed, and the employer must guarantee the employee can get them either for fifty years from issue or for six years after the employee retires. | [PAYSLIPDELIVERY](#payslipdelivery) | legal/official selected rule |
| france-payroll-unit-0337 / Delivery / 530 | - The employee can challenge the amount or the accuracy of a payslip for three years from the day it was handed over. | [PAYSLIPCHALLENGE](#payslipchallenge) | legal/official selected rule |
| france-payroll-unit-0338 / Delivery / 531 | - There is no legal duty on the employer to issue a duplicate of a lost payslip. | [PAYSLIPDUP](#payslipdup) | legal/official selected rule |
| france-payroll-unit-0339 / Delivery / 533 | \| Item \| Value \| Page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0340 / Delivery / 535 | \| Source \| all figures below \| https://entreprendre.service-public.gouv.fr/vosdroits/F559 \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0341 / Delivery / 536 | \| Fine the employer can be ordered to pay for each payslip not handed over \| EUR 450 \| "une amende pouvant atteindre 450 € par fiche non remise" \| | [T536_0](#t536_0) | legal/official selected rule |
| france-payroll-unit-0342 / Monthly: DSN (Déclaration Sociale Nominative) / 542 | \| Obligation \| Deadline \| Page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0343 / Monthly: DSN (Déclaration Sociale Nominative) / 544 | \| Source \| all figures below unless a row names another page \| https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0344 / Monthly: DSN (Déclaration Sociale Nominative) / 545 | \| Employer with 50 employees or more, pay run in the same month as the work \| The 5th of the following month \| "vous devez transmettre votre DSN liée à la paie du mois en cours, le 5 du mois suivant (M+1)" \| | [T545_0](#t545_0) | legal/official selected rule |
| france-payroll-unit-0345 / Monthly: DSN (Déclaration Sociale Nominative) / 546 | \| Employer with 50 employees or more, pay run in the month after the work (decalage de paie) \| At the latest the 15th of the following calendar month \| "au plus tard le 15 du mois civil suivant" \| | [T546_0](#t546_0) | legal/official selected rule |
| france-payroll-unit-0346 / Monthly: DSN (Déclaration Sociale Nominative) / 547 | \| Employer with fewer than 50 employees \| At the latest the 15th of the following calendar month \| "Vous devez transmettre votre DSN liée à la paie du mois en cours, au plus tard le 15 du mois civil suivant" \| | [T547_0](#t547_0) | legal/official selected rule |
| france-payroll-unit-0347 / Monthly: DSN (Déclaration Sociale Nominative) / 548 | \| Employer with fewer than 11 employees, quarterly payment option \| The ordinary DSN remains monthly, by the 15th. CSS R243-6-1 permits eligible employers to opt for quarterly contribution payment, within the first 15 days of the next quarter, by notifying the collection body before 31 December or when employing the first employee. It renews unless renounced by 31 December. Simplified declaration schemes listed in that article are excluded. \| "versement trimestriel des cotisations" / "L’employeur reste tenu d’adresser la déclaration sociale nominative à la date prévue"; contrary F24013 agency text: entreprendre.service-public.gouv.fr/vosdroits/F24013 \| | [T548_0](#t548_0); [T548_1](#t548_1) | legal/official selected rule |
| france-payroll-unit-0348 / Monthly: DSN (Déclaration Sociale Nominative) / 549 | \| Deadline falling on a public holiday or a non-working day \| Extended to the next working day \| "il est prolongé" \| | [T549_0](#t549_0) | legal/official selected rule |
| france-payroll-unit-0349 / Monthly: DSN (Déclaration Sociale Nominative) / 550 | \| Event report: sickness, early return or end of contract \| Ordinarily within five working days after the payroll manager learns of it. Net-entreprises states exceptions for subrogated sickness or delayed payroll recognition of sickness, and no return report when the actual return is not earlier than that already declared. \| "dans les 5 jours ouvrés suivant leur connaissance"; https://www.net-entreprises.fr/declaration/mentions-legales/ \| | [T550_0](#t550_0) | legal/official selected rule |
| france-payroll-unit-0350 / Monthly: DSN (Déclaration Sociale Nominative) / 552 | The condition the live text used to miss: the 5th is not simply the large-employer date. It applies only where the employer has 50 employees or more **and** pays in the same month as the work. An employer of that size that pays in the following month is on the 15th, like a smaller employer. CSS R133-14 I expressly requires a DSN each month; R243-6-1 preserves that duty even when payment is quarterly. Source: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000039222527 and https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038681470 . Contrary administrative text is retained as a source discrepancy: F24013 says a business below 11 employees may file quarterly, but that wording does not displace these monthly statutory filing rules. | [DSNDATE](#dsndate); [R133MONTH](#r133month); [R243QUARTER](#r243quarter) | legal/official selected rule |
| france-payroll-unit-0351 / Monthly: DSN (Déclaration Sociale Nominative) / 554 | **Penalties** |  | presentation subheading |
| france-payroll-unit-0352 / Monthly: DSN (Déclaration Sociale Nominative) / 556 | \| Failure \| Penalty \| Page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0353 / Monthly: DSN (Déclaration Sociale Nominative) / 558 | \| Source \| all figures below \| https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0354 / Monthly: DSN (Déclaration Sociale Nominative) / 559 | \| Filing outside the DSN channel \| 0.5% of the monthly social security ceiling per employee \| "0,5 % du plafond mensuel de la Sécurité sociale (PMSS) par salarié" \| | [T559_0](#t559_0) | legal/official selected rule |
| france-payroll-unit-0355 / Monthly: DSN (Déclaration Sociale Nominative) / 560 | \| Same, cap where the employer has at least 2,000 employees \| EUR 10,000 \| "montant plafonné à 10 000 € si vous employez au moins 2 000 salariés" \| | [T560_0](#t560_0) | legal/official selected rule |
| france-payroll-unit-0356 / Monthly: DSN (Déclaration Sociale Nominative) / 561 | \| Same, cap where the employer has fewer than 2,000 employees \| EUR 750 \| "montant plafonné à 750 € par entreprise si vous employez un nombre inférieur à 2 000 salariés" \| | [T561_0](#t561_0) | legal/official selected rule |
| france-payroll-unit-0357 / Monthly: DSN (Déclaration Sociale Nominative) / 562 | \| Late filing \| 1.5% of the monthly ceiling per employee per month or part month late \| "1,5 % du plafond mensuel de la Sécurité sociale par salarié et par mois ou fraction de mois de retard" \| | [T562_0](#t562_0) | legal/official selected rule |
| france-payroll-unit-0358 / Monthly: DSN (Déclaration Sociale Nominative) / 563 | \| Late filing, cap where the delay is five days or less \| 150% of the monthly ceiling per business, once a calendar year \| "Montant plafonné à 150 % PMSS par entreprise si défaut de production inférieur ou égal à 5 jours" \| | [T563_0](#t563_0) | legal/official selected rule |
| france-payroll-unit-0359 / Monthly: DSN (Déclaration Sociale Nominative) / 564 | \| Employees left out of the filing \| 1.5% of the monthly ceiling per employee per month or part month, capped at 150% of the monthly ceiling per business if the failure is corrected within 5 days, once a calendar year \| "omission de salariés ou assimilés : 1,5 % du plafond mensuel de la Sécurité sociale par salarié" / "Montant plafonné à 150 % PMSS par entreprise si défaut de production inférieur ou égal à 5 jours" \| | [T564_0](#t564_0); [T564_1](#t564_1) | legal/official selected rule |
| france-payroll-unit-0360 / Monthly: DSN (Déclaration Sociale Nominative) / 565 | \| Other omissions, including employer identification data \| 0.5% of the monthly ceiling per employee \| "autres cas : 0,5 % du plafond mensuel de la Sécurité sociale par salarié" \| | [T565_0](#t565_0) | legal/official selected rule |
| france-payroll-unit-0361 / Monthly: DSN (Déclaration Sociale Nominative) / 566 | \| Pay reported wrongly so that contributions come out too low \| 1% of the monthly ceiling per employee \| "1 % du plafond mensuel de la Sécurité sociale par salarié ou assimilé" \| | [T566_0](#t566_0) | legal/official selected rule |
| france-payroll-unit-0362 / Monthly: DSN (Déclaration Sociale Nominative) / 567 | \| Other inaccuracies \| 0.33% of the monthly ceiling per employee \| "autres cas : 0,33 % du plafond mensuel de la Sécurité sociale par salarié" \| | [T567_0](#t567_0) | legal/official selected rule |
| france-payroll-unit-0363 / Monthly: DSN (Déclaration Sociale Nominative) / 568 | \| Correcting figure below which late interest and the penalty are not applied, where errors are not repeated \| 5% of the total initial contributions \| "le versement régularisateur est inférieur à 5 % du montant total des cotisations initiales" \| | [T568_0](#t568_0) | legal/official selected rule |
| france-payroll-unit-0364 / Monthly: DSN (Déclaration Sociale Nominative) / 570 | The EUR 10,000 and EUR 750 caps on filing outside the DSN channel apply to employers within the scope of the décret of 24 September 2014. A third cap applies to employers within the scope of the décret of 18 May 2016: EUR 750 per business, per month. | [DSNCAP](#dsncap) | legal/official selected rule |
| france-payroll-unit-0365 / Monthly: DSN (Déclaration Sociale Nominative) / 572 | The 30-day correction exception on the Urssaf page covers other omissions and inaccuracies; it does not give a blanket exemption for an employee omitted from the DSN, which has its separate penalty above. Read the compte-rendu métier and Suivi DSN anomaly reports promptly and correct the declaration. Not yet confirmed: universal four-hour CRM delivery and five-day later-anomaly service levels formerly stated here; the selected current Urssaf text promises rapid feedback without those exact timings. Separately, the droit à l'erreur applies only where the employer corrects the pay at the nearest declarative deadline and pays the top-up contributions and social charges at the same time; on that condition it removes the majorations and the penalty where either limb is met, provided the inaccuracies are not repetitive: the majorations and penalty that would otherwise apply come to less than one monthly value of the social security ceiling, or the regularising payment is below 5% of the total initial contributions. | [DSNOMISSION](#dsnomission); [DSNINACCURATE](#dsninaccurate); [DSNCORRECT](#dsncorrect); [DSNCRM](#dsncrm) | legal/official selected rule |
| france-payroll-unit-0366 / Monthly: DSN (Déclaration Sociale Nominative) / 574 | **Penalties on the employer as collector of the income tax withheld** |  | presentation subheading |
| france-payroll-unit-0367 / Monthly: DSN (Déclaration Sociale Nominative) / 576 | Those Urssaf penalties are about the social contributions. The income tax withheld carries a separate set of penalties under the tax code, which the tax administration's own doctrine sets out. The administrative fines in the first six rows below are exclusive of one another and do not stack. That exclusivity covers only those fines, the ones under CGI art. 1759-0 A. The late-payment surcharge and the criminal penalties are separate charges and the page does not say they are excluded by them. | [PASEXCLUSIVE](#pasexclusive) | legal/official selected rule |
| france-payroll-unit-0368 / Monthly: DSN (Déclaration Sociale Nominative) / 578 | \| Failure \| Penalty \| Page wording \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0369 / Monthly: DSN (Déclaration Sociale Nominative) / 580 | \| Source \| all figures below \| https://bofip.impots.gouv.fr/bofip/11471-PGP.html \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0370 / Monthly: DSN (Déclaration Sociale Nominative) / 581 | \| Inaccuracy or omission, where the return was filed on time \| 5% of the withholding that should have been made or declared \| "l’amende est de 5 % des retenues qui auraient dû être effectuées ou déclarées lorsque la déclaration a été déposée dans les délais" \| | [T581_0](#t581_0) | legal/official selected rule |
| france-payroll-unit-0371 / Monthly: DSN (Déclaration Sociale Nominative) / 582 | \| Inaccuracy or omission that was deliberate \| 40% \| "Le taux de l’amende est porté à 40 % en cas d'inexactitudes ou d'omissions délibérées" \| | [T582_0](#t582_0) | legal/official selected rule |
| france-payroll-unit-0372 / Monthly: DSN (Déclaration Sociale Nominative) / 583 | \| Return not filed by the deadline \| 10% of the withholding that should have been made or declared \| "l’amende s’élève à 10 % des retenues qui auraient dû être effectuées ou déclarées" \| | [T583_0](#t583_0) | legal/official selected rule |
| france-payroll-unit-0373 / Monthly: DSN (Déclaration Sociale Nominative) / 584 | \| Still not filed within thirty days of a formal notice \| 40% \| "L’amende est portée à 40 % des retenues qui auraient dû être effectuées ou déclarées en cas de non-dépôt de la déclaration dans les trente jours suivant une mise en demeure" \| | [T584_0](#t584_0) | legal/official selected rule |
| france-payroll-unit-0374 / Monthly: DSN (Déclaration Sociale Nominative) / 585 | \| Withholding made but deliberately not declared and not paid over \| 80% of the withholding made \| "une amende égale à 80 % des retenues effectuées" \| | [T585_0](#t585_0) | legal/official selected rule |
| france-payroll-unit-0375 / Monthly: DSN (Déclaration Sociale Nominative) / 586 | \| Floor for any of these fines \| EUR 250 per return \| "l’amende est au minimum égale à 250 € par déclaration" \| | [T586_0](#t586_0) | legal/official selected rule |
| france-payroll-unit-0376 / Monthly: DSN (Déclaration Sociale Nominative) / 587 | \| Late payment of the withholding \| The surcharge in CGI art. 1731. The worked example on the page applies 5% of the unpaid amount \| "une majoration égale à 5 % du montant non payé" \| | [T587_0](#t587_0) | legal/official selected rule |
| france-payroll-unit-0377 / Monthly: DSN (Déclaration Sociale Nominative) / 588 | \| Withholding kept back deliberately, delay over one month, criminal fine \| EUR 1,500 \| "passible d’une amende de 1 500 €" \| | [T588_0](#t588_0) | legal/official selected rule |
| france-payroll-unit-0378 / Monthly: DSN (Déclaration Sociale Nominative) / 589 | \| Repeat within three years \| Two years imprisonment and a fine of EUR 3,750, or one of the two \| "punissable de deux ans d'emprisonnement et de 3 750 € d'amende" \| | [T589_0](#t589_0) | legal/official selected rule |
| france-payroll-unit-0379 / Monthly: DSN (Déclaration Sociale Nominative) / 591 | The two deliberate-breach fines in the table above apply only where the administration shows the breach was deliberate. Where only part of a return is filed late, the doctrine applies the 5% fine to that late-filed part, instead of the 10% non-filing fine. The converse also holds: where the administration finds an omission or an inaccuracy on a return that was itself filed late, only the 10% non-filing fine applies to the whole of the withholding not declared in time. | [PASDELIBERATE](#pasdeliberate); [PASEXCLUSIVE](#pasexclusive) | legal/official selected rule |
| france-payroll-unit-0380 / Annual / 595 | \| Obligation \| Deadline \| Notes \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0381 / Annual / 597 | \| DADS \| Not applicable, fully replaced by the DSN since 2019 \| Historical reference only \| | [DADS](#dads) | legal/official selected rule |
| france-payroll-unit-0382 / Annual / 598 | \| Bilan social, retained reporting handoff \| Under Code du travail L2312-28, the annual social-policy consultation also covers the social report for a business with at least 300 employees, and an establishment report for each distinct establishment with at least 300. \| Apply L2312-29’s threshold transition: the first report concerns the year after reaching the threshold; the first may cover one year and the second two; a drop below threshold still requires the current-year report. Current consultation terms follow the applicable agreement or statutory fallback. Source: https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072050/LEGISCTA000035609798/2026-06-14/ \| | [BILAN](#bilan); [BILANTRANS](#bilantrans) | legal/official selected rule |
| france-payroll-unit-0383 / Annual / 599 | \| Index de l'égalité professionnelle \| Each year, at the latest 1 March, on the company website and on Égapro \| Businesses with at least 50 employees over the past year. A business that has just reached 50 employees has three years before it must publish. Source: https://entreprendre.service-public.gouv.fr/vosdroits/F35103 \| | [INDEX](#index); [INDEXTRANS](#indextrans); [INDEXPUBLISH](#indexpublish) | legal/official selected rule |
| france-payroll-unit-0384 / Employee Obligations / 603 | \| Item \| Detail \| |  | presentation/context/source metadata, no separate rate/entitlement |
| france-payroll-unit-0385 / Employee Obligations / 605 | \| Declaration de revenus \| Annual, in the spring, pre-filled with the withholding data \| | [PASYEAR](#pasyear); [FAMILY](#family); [PREFILL](#prefill); [PREFILLCORRECT](#prefillcorrect) | legal/official selected rule |
| france-payroll-unit-0386 / Employee Obligations / 606 | \| Adjustment \| Where the rate was wrong, the balance is settled through the avis d'imposition \| | [PASYEAR](#pasyear); [FAMILY](#family); [PREFILL](#prefill); [PREFILLCORRECT](#prefillcorrect) | legal/official selected rule |
| france-payroll-unit-0387 / Employee Obligations / 607 | \| Rate maintenance \| The employee, not the employer, tells the tax office about a change of family situation, within 60 days \| | [PASYEAR](#pasyear); [FAMILY](#family); [PREFILL](#prefill); [PREFILLCORRECT](#prefillcorrect) | legal/official selected rule |
| france-payroll-unit-0388 / Typical Bank Statement Descriptions (Salary Credits) / 613 | \| Pattern \| Classification \| |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0389 / Typical Bank Statement Descriptions (Salary Credits) / 615 | \| VIREMENT SALAIRE, VIR SALAIRE \| Net salary payment \| |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0390 / Typical Bank Statement Descriptions (Salary Credits) / 616 | \| SALAIRE plus the employer name \| Net salary payment \| |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0391 / Typical Bank Statement Descriptions (Salary Credits) / 617 | \| INDEMNITE CONGES PAYES \| Holiday pay, where paid separately \| |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0392 / Typical Bank Statement Descriptions (Salary Credits) / 618 | \| PRIME 13E MOIS \| Thirteenth month bonus \| |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0393 / Typical Bank Statement Descriptions (Salary Credits) / 619 | \| PRIME PARTICIPATION, INTERESSEMENT \| Profit sharing, separate tax and social rules \| |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0394 / Typical Bank Statement Descriptions (Salary Credits) / 620 | \| IJSS, CPAM INDEMNITE \| Sickness or maternity daily allowance from the health scheme \| |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0395 / Typical Bank Statement Descriptions (Salary Credits) / 621 | \| PRIME PARTAGE VALEUR, PPV \| Prime de partage de la valeur \| |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0396 / Typical Employer Debit Patterns / 625 | \| Pattern \| Classification \| |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0397 / Typical Employer Debit Patterns / 627 | \| URSSAF COTISATIONS \| Monthly social contribution payment \| |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0398 / Typical Employer Debit Patterns / 628 | \| AGIRC-ARRCO COTISATIONS \| Supplementary pension contributions \| |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0399 / Typical Employer Debit Patterns / 629 | \| DGFIP PAS, PRELEVEMENT SOURCE \| Income tax withheld and paid over \| |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0400 / Typical Employer Debit Patterns / 630 | \| MUTUELLE plus the insurer name \| Compulsory health cover premium \| |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0401 / Typical Employer Debit Patterns / 631 | \| PREVOYANCE plus the insurer name \| Provident insurance premium \| |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0402 / Section 10: Interaction with Other Skills / 635 | \| Scenario \| Skill to use \| |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0403 / Section 10: Interaction with Other Skills / 637 | \| Employee payroll, contributions and withholding \| This skill, `france-payroll` \| |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0404 / Section 10: Interaction with Other Skills / 638 | \| Self-employed income tax, including auto-entrepreneur and micro-entrepreneur \| `fr-income-tax` \| |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0405 / Section 10: Interaction with Other Skills / 639 | \| Income tax for an employee's own household return \| `fr-personal-income-tax` \| |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0406 / Section 10: Interaction with Other Skills / 640 | \| Social contributions of a self-employed person \| `fr-social-contributions` \| |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0407 / Section 10: Interaction with Other Skills / 641 | \| TVA, French VAT \| `france-vat-return` \| |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0408 / Section 10: Interaction with Other Skills / 642 | \| Bookkeeping \| `france-bookkeeping` \| |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0409 / Section 10: Interaction with Other Skills / 643 | \| Electronic invoicing, Factur-X and Chorus Pro \| `france-einvoice` \| |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0410 / Key Handoff Points / 647 | - **Payroll to bookkeeping.** Gross wages use account 641 and employer social contributions 645. Social-contribution liabilities use 43x; income tax withheld at source uses 4421, not 43x, until the respective payments clear. Source: the ANC January 2026 PCG account plan, https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/recueil/2026/Recueil-PCG-Janvier-2026.pdf . | [PCGLIABILITY](#pcgliability); [PCGEXPENSE](#pcgexpense) | legal/official selected rule |
| france-payroll-unit-0411 / Key Handoff Points / 648 | - **Payroll to income tax.** Withholding settles most of the employee's income tax in real time. The annual return may still produce an adjustment. The net imposable on the payslip is the reference figure. | [PASYEAR](#pasyear); [PASRATE](#pasrate); [PREFILL](#prefill); [PREFILLCORRECT](#prefillcorrect) | legal/official selected rule |
| france-payroll-unit-0412 / Key Handoff Points / 649 | - **Payroll to the DSN.** All payroll data feeds the DSN. Accurate payslips give an accurate DSN. Errors produce anomaly reports through net-entreprises.fr. | [DSNCRM](#dsncrm); [PAYSLIPZONES](#payslipzones) | legal/official selected rule |
| france-payroll-unit-0413 / The method, step by step / 653 | 1. **Fix the gross and the pay elements.** Add base pay, overtime at the premium in the overtime table in Section 5 or at the collective agreement rate, bonuses, and benefits in kind at the values in Section 6. Check the result against the Smic in force on the days worked, using the table at https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/montant-smic.html Expense allowances inside the limits on https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/frais-professionnels.html stay out of the base. | [SMICGEOG](#smicgeog); [OVERTIMEWEEK](#overtimeweek); [EXPENSEGATE](#expensegate) | legal/official selected rule |
| france-payroll-unit-0414 / The method, step by step / 654 | 2. **Split the gross across the ceilings.** Work out tranche 1 and tranche 2 against the monthly ceiling at https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/plafonds-securite-sociale.html For an ordinary monthly employee employed for only part of a month, use the monthly ceiling multiplied by the calendar days covered by the employment period and divided by the actual calendar days in that month, also deducting whole unpaid absence days under CSS R242-2. EUR 220 per day and EUR 30 per hour are not substitutes for that formula. For the part-time employees covered by CSSR242-2, the employer has the right to correct the ceiling. If that optional correction is exercised, use contractual hours plus complementary hours divided by the applicable legal or shorter collective full-time duration, capped at the full ceiling; perform the cumulative payroll regularisation it requires. Source: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000039222466/2026-03-26 | [PASS](#pass); [R242MONTH](#r242month); [R242PART](#r242part); [R242REG](#r242reg); [CALENDAR](#calendar) | legal/official selected rule |
| france-payroll-unit-0415 / The method, step by step / 655 | 3. **Apply the employee contributions.** Use the employee table in Section 3 and the Agirc-Arrco tables, from https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html and https://www.service-public.gouv.fr/particuliers/vosdroits/F15396 Charge CSG and CRDS on the reduced base in the CSG table, watching the four-ceiling limit. Apply the overtime relief from https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/exonerations-heures/reduction-cotisations-salariales.html Apply its actual eligibility and rate-cap gates in Section3 before calculating the reduction. | [PASS](#pass); [CSGGATES](#csggates); [CSGHEALTH](#csghealth); [OVERTIMECALC](#overtimecalc); [OVERTIMECOND](#overtimecond) | legal/official selected rule |
| france-payroll-unit-0416 / The method, step by step / 656 | 4. **Apply the employer contributions, then the single degressive relief.** Use the employer table in Section 4, then compute the relief with the coefficient parameters at https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html Check eligibility against the pay ceiling in that table before computing anything. | [RGDUELIG](#rgduelig); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze) | legal/official selected rule |
| france-payroll-unit-0417 / The method, step by step / 657 | 5. **Compute the net imposable and withhold the income tax.** Start the net imposable with gross taxable remuneration, add the taxable employer contribution for health-cost cover if it is not already included, and subtract only deductible employee social contributions within their applicable limits. Employer health contributions are taxable remuneration; CSG/CRDS that are not deductible must not be subtracted. Source: https://bofip.impots.gouv.fr/bofip/5956-PGP.html/identifiant%3DBOI-RSA-BASE-30-10-20-20260217 . Apply the rate the tax office sent through the DSN feedback, or, where there is none, the grid at https://bofip.impots.gouv.fr/bofip/11255-PGP.html taking the grid for the territory where the employee lives. The tax withheld is paid to the tax administration by the SEPA B2B debit set in the DSN, as described at https://www.impots.gouv.fr/les-modalites-du-prelevement-la-source-0 | [HEALTHTAX](#healthtax); [PASRATE](#pasrate); [SHORTCALC](#shortcalc); [REMIT](#remit) | legal/official selected rule |
| france-payroll-unit-0418 / The method, step by step / 658 | 6. **Issue the payslip.** Build the seven zones listed in Section 7 from https://entreprendre.service-public.gouv.fr/vosdroits/F559 including the montant net social line and the year to date totals. | [PAYSLIPZONES](#payslipzones) | legal/official selected rule |
| france-payroll-unit-0419 / The method, step by step / 659 | 7. **File the DSN and pay.** File on net-entreprises.fr by the date in the DSN table in Section 8, from https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html Read the compte-rendu metier and correct by an annule et remplace before the due date. Send event reports within the five-working-day rule and its exceptions in Section 8, rather than assuming every event has the same calendar-day deadline. | [DSNDATE](#dsndate); [DSNEVENTS](#dsnevents) | legal/official selected rule |
| france-payroll-unit-0420 / Worked examples / 663 | **Example 1. Ordinary part-month ceiling, March 2026.** Fictional monthly-paid employee, employed for ten calendar days in March (31 days), gross pay EUR 2,000, no unpaid absence or part-time reduction and no earlier employment-period regularisation balance. PMSS is EUR 4,005. The prorated ceiling is 4,005 × 10 / 31 = EUR 1,291.94 when illustrated to cents. Capped employee old-age contributions at 6.90% are EUR 89.14; uncapped employee old-age at 0.40% on the full EUR 2,000 is EUR 8.00. Multiplying EUR 220 by ten gives EUR 2,200 and is not the ordinary monthly proration rule. This example computes those two contribution lines, not a complete net payslip. Sources: CSS R242-2, the ceiling and private-sector contribution tables cited above. | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0421 / Worked examples / 665 | ```oa-check | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0422 / Worked examples / 666 | name: France ordinary monthly ceiling for ten calendar days in March2026 | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0423 / Worked examples / 667 | inputs: | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0424 / Worked examples / 668 |   monthly_ceiling: 4005 | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0425 / Worked examples / 669 |   calendar_employment_days: 10 | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0426 / Worked examples / 670 |   calendar_month_days: 31 | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0427 / Worked examples / 671 |   gross: 2000 | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0428 / Worked examples / 672 | steps: | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0429 / Worked examples / 673 |   - ceiling: round(monthly_ceiling * calendar_employment_days / calendar_month_days, 2) | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0430 / Worked examples / 674 |   - capped_employee_old_age: round(min(gross, ceiling) * 0.069, 2) | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0431 / Worked examples / 675 |   - uncapped_employee_old_age: round(gross * 0.004, 2) | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0432 / Worked examples / 676 | expected: | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0433 / Worked examples / 677 |   ceiling: 1291.94 | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0434 / Worked examples / 678 |   capped_employee_old_age: 89.14 | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0435 / Worked examples / 679 |   uncapped_employee_old_age: 8.00 | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0436 / Worked examples / 680 | ``` | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0437 / Worked examples / 682 | **Example 2. Published ordinary RGDU monthly calculation, June 2026.** Fictional eligible private employer with 70 employees, an employee paid EUR 2,000 for a full 35-hour week throughout June, no absence, overtime or PPV, employment continuing on 1 July, and the same pay/hour pattern over the year. Use the January hourly Smic EUR 12.02 for RGDU, not the June minimum wage: 12.02 × 35 × 52 / 12 = EUR 1,823.0333… reference monthly Smic. With T min 0.0200, T delta 0.3821 and P 1.75, the coefficient is 0.317818…; to the four-decimal precision used in the Urssaf June example it is 0.3178, giving EUR 635.60. The full-year corresponding relief is EUR 7,627.20 on these unchanged fictional inputs, subject to the required actual annual/progressive regularisation. The EUR 635.60 matches the agency’s published monthly result. The executable block uses its published 0.3178 coefficient as an input; the ledger’s supplementary control independently recomputes the fractional-power formula, which the oa-check parser does not support. It is not a complete employer-cost calculation, and different pay, hours, PPV or absence require recomputation. Source: https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html , current July 2026 method and June example. | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0438 / Worked examples / 684 | ```oa-check | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0439 / Worked examples / 685 | name: France published RGDU2026 full-month seventy-employee example | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0440 / Worked examples / 686 | inputs: | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0441 / Worked examples / 687 |   january_smic_hourly: 12.02 | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0442 / Worked examples / 688 |   weekly_hours: 35 | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0443 / Worked examples / 689 |   gross_month: 2000 | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0444 / Worked examples / 690 |   t_min: 0.02 | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0445 / Worked examples / 691 |   t_delta: 0.3821 | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0446 / Worked examples / 692 |   published_coefficient: 0.3178 | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0447 / Worked examples / 693 | steps: | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0448 / Worked examples / 694 |   - reference_smic: january_smic_hourly * weekly_hours * 52 / 12 | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0449 / Worked examples / 695 |   - eligibility_ceiling: reference_smic * 3 | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0450 / Worked examples / 696 |   - coefficient: clamp(published_coefficient, t_min, t_min + t_delta) | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0451 / Worked examples / 697 |   - monthly_relief: round(gross_month * coefficient, 2) | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0452 / Worked examples / 698 |   - unchanged_year_relief: round(monthly_relief * 12, 2) | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0453 / Worked examples / 699 | expected: | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0454 / Worked examples / 700 |   coefficient: 0.3178 | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0455 / Worked examples / 701 |   monthly_relief: 635.60 | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0456 / Worked examples / 702 |   unchanged_year_relief: 7627.20 | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0457 / Worked examples / 703 | ``` | [PASS](#pass); [R242MONTH](#r242month); [CALENDAR](#calendar); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [RGDUCASE](#rgducase); [OVERTIMECALC](#overtimecalc) | computed: fictional facts and independently recomputed sourced arithmetic; published RGDUcoefficient is identified input |
| france-payroll-unit-0458 / Ask the client first / 707 | - **How many employees does the business have, and does it pay in the month of the work or the month after?** This decides the DSN date, the Fnal rate, the training contribution rate, the flat overtime deduction, and which coefficient row of the single degressive relief applies. | [PASS](#pass); [CSGGATES](#csggates); [DSNDATE](#dsndate); [REDUCEDAM](#reducedam); [REDUCEDAF](#reducedaf); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [WORKDEROG](#workderog) | operational intake tied to actual rules |
| france-payroll-unit-0459 / Ask the client first / 708 | - **Is the employee resident in France for income tax, and in a compulsory French health scheme?** Both tests must be met for CSG and CRDS. If only the health test is met, an employee health contribution replaces them. | [PASS](#pass); [CSGGATES](#csggates); [DSNDATE](#dsndate); [REDUCEDAM](#reducedam); [REDUCEDAF](#reducedaf); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [WORKDEROG](#workderog) | operational intake tied to actual rules |
| france-payroll-unit-0460 / Ask the client first / 709 | - **Where does the employee live and work?** Mayotte has its own ceiling and its own Smic. Guadeloupe, La Reunion, Martinique, Guyane and Mayotte have their own default withholding grids. Haut-Rhin, Bas-Rhin and Moselle carry an extra employee health contribution and a different apprenticeship tax. | [PASS](#pass); [CSGGATES](#csggates); [DSNDATE](#dsndate); [REDUCEDAM](#reducedam); [REDUCEDAF](#reducedaf); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [WORKDEROG](#workderog) | operational intake tied to actual rules |
| france-payroll-unit-0461 / Ask the client first / 710 | - **Which collective agreement applies?** It can raise the minimum pay above the Smic, change the overtime premiums and the annual quota, change the reference period for leave, and require the employer to keep paying during maternity or sickness. | [PASS](#pass); [CSGGATES](#csggates); [DSNDATE](#dsndate); [REDUCEDAM](#reducedam); [REDUCEDAF](#reducedaf); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [WORKDEROG](#workderog) | operational intake tied to actual rules |
| france-payroll-unit-0462 / Ask the client first / 711 | - **Does the employer use a zoned exemption, the overseas Lodeom exemption, or the home-help exemption, and is the employee's annual pay at or below the pay ceiling in Section 4 (2.5 times the frozen Smic for maladie, 3.5 times for allocations familiales)?** Both the exemption and the pay ceiling must be met; that is now the only ordinary route to the reduced maladie and allocations familiales rates. | [PASS](#pass); [CSGGATES](#csggates); [DSNDATE](#dsndate); [REDUCEDAM](#reducedam); [REDUCEDAF](#reducedaf); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [WORKDEROG](#workderog) | operational intake tied to actual rules |
| france-payroll-unit-0463 / Ask the client first / 712 | - **What are the paid hours, absences and any prime de partage de la valeur in the year?** These affect the single degressive relief. Ordinary 2026 RGDU uses the Smic frozen at 1 January, with the adjustments in Section 4, while actual minimum pay changes on 1 June. | [PASS](#pass); [CSGGATES](#csggates); [DSNDATE](#dsndate); [REDUCEDAM](#reducedam); [REDUCEDAF](#reducedaf); [RGDUPARAM](#rgduparam); [RGDUFREEZE](#rgdufreeze); [WORKDEROG](#workderog) | operational intake tied to actual rules |
| france-payroll-unit-0464 / When to refuse or refer / 716 | - Any payroll for a special scheme, for example SNCF, RATP, the electricity and gas industries, the mines, the clercs et employes de notaires, or seafarers. The rates and the relief are different and are not in this skill. |  | explicit scope/referral boundary, not a supplied special-regime rate |
| france-payroll-unit-0465 / When to refuse or refer / 717 | - Payroll in Mayotte beyond the ceiling and the Smic quoted here. The contribution rates are a separate schedule. |  | explicit scope/referral boundary, not a supplied special-regime rate |
| france-payroll-unit-0466 / When to refuse or refer / 718 | - Household employers, childminders and home-help staff: they use the Urssaf schedule for particuliers employeurs, not the private-sector schedule. |  | explicit scope/referral boundary, not a supplied special-regime rate |
| france-payroll-unit-0467 / When to refuse or refer / 719 | - Apprentices, professionalisation contracts, interns and company officers, where the base and the exemptions are not the ones in this skill. |  | explicit scope/referral boundary, not a supplied special-regime rate |
| france-payroll-unit-0468 / When to refuse or refer / 720 | - Additional cadre benefits, including the minimum provident cover, require the actual applicable agreement. The ordinary Apec contribution is supplied above; it does not establish a provident-cover premium. | [APEC](#apec) | explicit scope/referral boundary, not a supplied special-regime rate |
| france-payroll-unit-0469 / When to refuse or refer / 721 | - Termination pay: severance, rupture conventionnelle and transactional payments have their own exemption limits. Only the employer contribution rate is in this skill. |  | explicit scope/referral boundary, not a supplied special-regime rate |
| france-payroll-unit-0470 / When to refuse or refer / 722 | - Any case where a collective agreement, an extended branch agreement or a company agreement is in play and has not been read. |  | explicit scope/referral boundary, not a supplied special-regime rate |
| france-payroll-unit-0471 / When to refuse or refer / 723 | - Any figure a client wants to rely on without a French expert-comptable signing it off. |  | explicit scope/referral boundary, not a supplied special-regime rate |
| france-payroll-unit-0472 / PROHIBITIONS / 727 | - Never work out income tax bands by hand for the withholding. Use the rate the tax office sends, or the default grid in Section 2. | [PASRATE](#pasrate); [CSGHEALTH](#csghealth); [CEGCET](#cegcet); [MUTUELLEGATES](#mutuellegates); [NOCHOMAGE](#nochomage); [REDUCEDAM](#reducedam); [REDUCEDAF](#reducedaf); [PAYSLIPZONES](#payslipzones); [DSNDATE](#dsndate); [SMICGEOG](#smicgeog) | operational prohibition grounded in cited rules |
| france-payroll-unit-0473 / PROHIBITIONS / 728 | - Never apply the professional-costs allowance to CSG and CRDS above four annual ceilings, and never apply it to the employer's contribution to the company health cover. | [PASRATE](#pasrate); [CSGHEALTH](#csghealth); [CEGCET](#cegcet); [MUTUELLEGATES](#mutuellegates); [NOCHOMAGE](#nochomage); [REDUCEDAM](#reducedam); [REDUCEDAF](#reducedaf); [PAYSLIPZONES](#payslipzones); [DSNDATE](#dsndate); [SMICGEOG](#smicgeog) | operational prohibition grounded in cited rules |
| france-payroll-unit-0474 / PROHIBITIONS / 729 | - Never mix up tranche 1 and tranche 2 for Agirc-Arrco, and never charge the CET only on the slice above the ceiling: it is charged from the first euro once pay passes the ceiling. | [PASRATE](#pasrate); [CSGHEALTH](#csghealth); [CEGCET](#cegcet); [MUTUELLEGATES](#mutuellegates); [NOCHOMAGE](#nochomage); [REDUCEDAM](#reducedam); [REDUCEDAF](#reducedaf); [PAYSLIPZONES](#payslipzones); [DSNDATE](#dsndate); [SMICGEOG](#smicgeog) | operational prohibition grounded in cited rules |
| france-payroll-unit-0475 / PROHIBITIONS / 730 | - Never leave the compulsory health cover out of employer cost. | [PASRATE](#pasrate); [CSGHEALTH](#csghealth); [CEGCET](#cegcet); [MUTUELLEGATES](#mutuellegates); [NOCHOMAGE](#nochomage); [REDUCEDAM](#reducedam); [REDUCEDAF](#reducedaf); [PAYSLIPZONES](#payslipzones); [DSNDATE](#dsndate); [SMICGEOG](#smicgeog) | operational prohibition grounded in cited rules |
| france-payroll-unit-0476 / PROHIBITIONS / 731 | - Never enter an employee unemployment contribution. The private-sector employee table lists none. | [PASRATE](#pasrate); [CSGHEALTH](#csghealth); [CEGCET](#cegcet); [MUTUELLEGATES](#mutuellegates); [NOCHOMAGE](#nochomage); [REDUCEDAM](#reducedam); [REDUCEDAF](#reducedaf); [PAYSLIPZONES](#payslipzones); [DSNDATE](#dsndate); [SMICGEOG](#smicgeog) | operational prohibition grounded in cited rules |
| france-payroll-unit-0477 / PROHIBITIONS / 732 | - Never assume the reduced maladie or allocations familiales rate for an ordinary private employer in 2026. Check the exemption list and the pay ceiling against the Smic frozen at 31 December 2023 first. | [PASRATE](#pasrate); [CSGHEALTH](#csghealth); [CEGCET](#cegcet); [MUTUELLEGATES](#mutuellegates); [NOCHOMAGE](#nochomage); [REDUCEDAM](#reducedam); [REDUCEDAF](#reducedaf); [PAYSLIPZONES](#payslipzones); [DSNDATE](#dsndate); [SMICGEOG](#smicgeog) | operational prohibition grounded in cited rules |
| france-payroll-unit-0478 / PROHIBITIONS / 733 | - Never quote a total employer cost or a total employee deduction percentage. No allowed page prints one. | [PASRATE](#pasrate); [CSGHEALTH](#csghealth); [CEGCET](#cegcet); [MUTUELLEGATES](#mutuellegates); [NOCHOMAGE](#nochomage); [REDUCEDAM](#reducedam); [REDUCEDAF](#reducedaf); [PAYSLIPZONES](#payslipzones); [DSNDATE](#dsndate); [SMICGEOG](#smicgeog) | operational prohibition grounded in cited rules |
| france-payroll-unit-0479 / PROHIBITIONS / 734 | - Never issue a payslip missing a field from the seven zones in Section 7. | [PASRATE](#pasrate); [CSGHEALTH](#csghealth); [CEGCET](#cegcet); [MUTUELLEGATES](#mutuellegates); [NOCHOMAGE](#nochomage); [REDUCEDAM](#reducedam); [REDUCEDAF](#reducedaf); [PAYSLIPZONES](#payslipzones); [DSNDATE](#dsndate); [SMICGEOG](#smicgeog) | operational prohibition grounded in cited rules |
| france-payroll-unit-0480 / PROHIBITIONS / 735 | - Never miss a DSN deadline. The penalties are shares of the monthly ceiling, set out in Section 8. | [PASRATE](#pasrate); [CSGHEALTH](#csghealth); [CEGCET](#cegcet); [MUTUELLEGATES](#mutuellegates); [NOCHOMAGE](#nochomage); [REDUCEDAM](#reducedam); [REDUCEDAF](#reducedaf); [PAYSLIPZONES](#payslipzones); [DSNDATE](#dsndate); [SMICGEOG](#smicgeog) | operational prohibition grounded in cited rules |
| france-payroll-unit-0481 / PROHIBITIONS / 736 | - Never forget that the Smic changed on 1 June 2026. Check which rate covers the days worked. | [PASRATE](#pasrate); [CSGHEALTH](#csghealth); [CEGCET](#cegcet); [MUTUELLEGATES](#mutuellegates); [NOCHOMAGE](#nochomage); [REDUCEDAM](#reducedam); [REDUCEDAF](#reducedaf); [PAYSLIPZONES](#payslipzones); [DSNDATE](#dsndate); [SMICGEOG](#smicgeog) | operational prohibition grounded in cited rules |
| france-payroll-unit-0482 / PROHIBITIONS / 737 | - Never present a payroll computation as final. Send it to an expert-comptable for sign-off. | [PASRATE](#pasrate); [CSGHEALTH](#csghealth); [CEGCET](#cegcet); [MUTUELLEGATES](#mutuellegates); [NOCHOMAGE](#nochomage); [REDUCEDAM](#reducedam); [REDUCEDAF](#reducedaf); [PAYSLIPZONES](#payslipzones); [DSNDATE](#dsndate); [SMICGEOG](#smicgeog) | operational prohibition grounded in cited rules |
| france-payroll-unit-0483 / Sources / 741 | - https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/plafonds-securite-sociale.html Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0484 / Sources / 742 | - https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/montant-smic.html Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0485 / Sources / 743 | - https://www.urssaf.fr/accueil/actualites/augmentation-smic.html Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0486 / Sources / 744 | - https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0487 / Sources / 745 | - https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-particuliers.html Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0488 / Sources / 746 | - https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/csg-crds.html Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0489 / Sources / 747 | - https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/assurance-chomage-ags.html Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0490 / Sources / 748 | - https://www.impots.gouv.fr/les-modalites-du-prelevement-la-source-0 Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0491 / Sources / 749 | - https://entreprendre.service-public.gouv.fr/vosdroits/F35103 Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0492 / Sources / 750 | - https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0493 / Sources / 751 | - https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/exonerations-heures/reduction-cotisations-salariales.html Selected overtime, nominal-IJ, optional part-time ceiling, weekly derogation, leased-car basket/cap and age/date SMIC scopes reread31October2026 from the retained sources. Selected own-law indexed II–V for forfait days: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038610232/2026-01-01 ; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053278678/2026-10-09 . Exact source representations and short scopes are in the ledger; no full lawHTML or full Urssaf-body acquisition is claimed. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0494 / Sources / 752 | - https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/prime-partage-valeur.html Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0495 / Sources / 753 | - https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0496 / Sources / 754 | - https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0497 / Sources / 755 | - https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/frais-professionnels.html Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0498 / Sources / 756 | - https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0499 / Sources / 757 | - https://entreprendre.service-public.gouv.fr/vosdroits/F559 Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0500 / Sources / 758 | - https://entreprendre.service-public.gouv.fr/vosdroits/F24013 Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0501 / Sources / 759 | - https://entreprendre.service-public.gouv.fr/vosdroits/F33754 Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0502 / Sources / 760 | - https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0503 / Sources / 761 | - https://www.service-public.gouv.fr/particuliers/vosdroits/F1419 Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0504 / Sources / 762 | - https://www.service-public.gouv.fr/particuliers/vosdroits/F15396 Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0505 / Sources / 763 | - https://www.service-public.gouv.fr/particuliers/vosdroits/F1911 Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0506 / Sources / 764 | - https://www.service-public.gouv.fr/particuliers/vosdroits/F2391 Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0507 / Sources / 765 | - https://www.service-public.gouv.fr/particuliers/vosdroits/F2258 Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0508 / Sources / 766 | - https://www.service-public.gouv.fr/particuliers/vosdroits/F3053 Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0509 / Sources / 767 | - https://www.service-public.gouv.fr/particuliers/vosdroits/F2265 Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0510 / Sources / 768 | - https://www.service-public.gouv.fr/particuliers/vosdroits/F3156 Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0511 / Sources / 769 | - https://bofip.impots.gouv.fr/bofip/11255-PGP.html Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0512 / Sources / 770 | - https://bofip.impots.gouv.fr/bofip/11471-PGP.html Selected cited scope read 2026-10-29. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0513 / Sources / 773 | Source-reading note, 29 October 2026: the selected current CSS R242-2, R133-14 I and R243-6-1 clauses, Code du travail D1226-1 to D1226-5, CSS L433-1 and L911-8, BOI-RSA-BASE-30-10-20 §200 and BOI-IR-PAS-20-20-30-10 §230–270 support the narrow corrections above. Where direct official HTTP access failed, the ledger preserves the actual official indexed display and its selected reading, not a claim that a whole statute was downloaded. The latest retrieved R133-14 display did not include its event-report subsection; the administrative five-day event wording is retained as that source’s wording, with no invented full current subsection reading. Ordinary methods and remaining precise source limits are recorded in the figure ledger. |  | source bibliography/read-scope disclosure, not additional financial rule |
| france-payroll-unit-0514 / Disclaimer / 777 | This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an expert-comptable in France) before implementation. |  | operational label/routing/disclaimer, not tax entitlement |
| france-payroll-unit-0515 / Disclaimer / 779 | The most up-to-date version of this skill is maintained by OpenAccountants. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes. |  | operational label/routing/disclaimer, not tax entitlement |

## Exact original-language quotations

### PASS

URSSAF2026 own annual/monthly/daily/hourly ceiling table; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/plafonds-securite-sociale.html; read2026-10-29; nativeLF1112–1126; readerSHA256 `43a49e769f4c79d8462c47a78c9a4fad51e84d2b88d37693befe0e9eb8b17458`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
 2026
 Année
 48 060 €
 Trimestre
 12 015 €
 Mois
 4 005 €
 Quinzaine
 2 003 €
 Semaine
 924 €
 Jour
 220 €
 Heure
 30 €
```

### MAYOTTE

URSSAF2026 Mayotte own ceiling table; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/plafonds-securite-sociale.html; read2026-10-29; nativeLF1147–1153; readerSHA256 `43a49e769f4c79d8462c47a78c9a4fad51e84d2b88d37693befe0e9eb8b17458`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
 2026
 Année
 36 264 €
 Trimestre
 9 066 €
 Mois
 3 022 €
```

### UNIFIED

Selected Official indexed selected original-language display; UNIFIED; https://www.agirc-arrco.fr/storage/2024/09/201809dc_ANI_du_17_novembre_2017.pdf; read2026-10-29; nativeLF19–19; readerSHA256 `c43041a656111fc171d24abbc15d7ad8cec81ac7dfe20ce823367467d50adc8e`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Conformément à l’article R. 922-4 du code de la sécurité sociale, la fusion des institutions de retraite complémentaire relevant de la Fédération AGIRC-ARRCO mentionnée à l’article 1er est opérée au 1er janvier 2019.
```

### PASRATE

Selected https://www.service-public.gouv.fr/particuliers/vosdroits/F34009; PASRATE; https://www.service-public.gouv.fr/particuliers/vosdroits/F34009; read2026-10-29; nativeLF167–172; readerSHA256 `c7bfe5559488e7363fac6c1dcaae57820aa53bdc5f70a5635a90896d40e5b6ae`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
 Ce taux personnalisé est communiqué à votre employeur ou votre caisse de retraite pour mettre en place le prélèvement.
 Le taux de prélèvement est modifié chaque année en septembre , en fonction de la déclaration des revenus effectuée au printemps.
Vous êtes marié ou pacsé
 Si vous êtes marié ou pacsé et imposé en commun , vous bénéficiez automatiquement d'un taux individualisé de prélèvement à la source.
 Votre taux individualisé s’applique exclusivement aux revenus dont vous disposez personnellement.
 Les revenus communs de votre foyer fiscal : titleContent sont soumis à un taux de prélèvement calculé pour l’ensemble des revenus du foyer.
```

### PASREQUEST

Selected https://www.service-public.gouv.fr/particuliers/vosdroits/F34009; PASREQUEST; https://www.service-public.gouv.fr/particuliers/vosdroits/F34009; read2026-10-29; nativeLF190–190; readerSHA256 `c7bfe5559488e7363fac6c1dcaae57820aa53bdc5f70a5635a90896d40e5b6ae`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
 Le nouveau taux s'applique au plus tard le 3 e mois qui suit votre demande.
```

### FAMILY

Selected https://www.service-public.gouv.fr/particuliers/vosdroits/F34009; FAMILY; https://www.service-public.gouv.fr/particuliers/vosdroits/F34009; read2026-10-29; nativeLF197–204; readerSHA256 `c7bfe5559488e7363fac6c1dcaae57820aa53bdc5f70a5635a90896d40e5b6ae`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
 Signalez à l'administration fiscale dans les 60 jours tout changement dans votre situation :
 Mariage
 Signature d'un Pacs : titleContent 
 Naissance, adoption ou recueil d'un enfant mineur
 Décès de l'un des époux(se) ou partenaire de Pacs
 Divorce ou rupture de Pacs.
 Vous pouvez signaler le changement directement dans votre espace Particulier en ligne .
 Impôts : accéder à votre espace Finances publiques 
```

### PAS2019

Selected https://www.impots.gouv.fr/les-modalites-du-prelevement-la-source-0; PAS2019; https://www.impots.gouv.fr/les-modalites-du-prelevement-la-source-0; read2026-10-29; nativeLF62–62; readerSHA256 `799123f5961e91f33d5de53b17199ed7a6cb92d13c3814e97b0099e64915e001`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
L’entrée en vigueur du prélèvement à la source de l’impôt sur le revenu est fixée au 1er janvier 2019. Le prélèvement à la source (PAS) de l’impôt sur le revenu vise à adapter le recouvrement de l'impôt d’une année à la situation réelle de l'usager (revenus, événements de vie) au titre de cette même année, sans en modifier les règles de calcul. Il a pour objectif de supprimer le décalage d'un an entre la perception des revenus et le paiement de l’impôt sur ces revenus.
```

### REMIT

Selected https://www.impots.gouv.fr/les-modalites-du-prelevement-la-source-0; REMIT; https://www.impots.gouv.fr/les-modalites-du-prelevement-la-source-0; read2026-10-29; nativeLF55–57; readerSHA256 `799123f5961e91f33d5de53b17199ed7a6cb92d13c3814e97b0099e64915e001`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Le reversement du PAS s'effectue au moyen d'un prélèvement SEPA B2B renseigné dans le bloc financier de la déclaration DSN ou PASRAU.
Les employeurs établis à l'étranger versant des salaires imposables en France doivent donc obligatoirement disposer d'un compte bancaire en zone SEPA. Ce compte bancaire devra être celui qui a été renseigné dans l'espace professionnel d'impots.gouv.fr.
Une fois les coordonnées bancaires renseignées, vous devez imprimer le mandat SEPA B2B, le signer et l'envoyer préalablement à tout reversement de PAS à votre établissement bancaire pour qu'il puisse l'enregistrer dans son système d'information. Tout incident de paiement entraînera le rejet du prélèvement SEPA B2B et l'application de sanctions.
```

### FOREIGNPAY

Selected https://www.impots.gouv.fr/les-modalites-du-prelevement-la-source-0; FOREIGNPAY; https://www.impots.gouv.fr/les-modalites-du-prelevement-la-source-0; read2026-10-29; nativeLF60–60; readerSHA256 `799123f5961e91f33d5de53b17199ed7a6cb92d13c3814e97b0099e64915e001`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Toutes les entreprises qui versent des salaires imposables en France doivent collecter et reverser le prélèvement à la source.
```

### PASYEAR

F34009 annualspringreturn/complementonavis; example facts not copied as rules; https://www.service-public.gouv.fr/particuliers/vosdroits/F34009; read2026-10-29; nativeLF236–245; readerSHA256 `c7bfe5559488e7363fac6c1dcaae57820aa53bdc5f70a5635a90896d40e5b6ae`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
 Quand faut-il payer un complément d'impôt ? 
 Si l'impôt calculé à partir de votre déclaration est plus élevé que le total des prélèvements réalisés l'année précédente, il vous reste un complément d'impôt à payer.
 Exemple :
 En 2025, vous avez versé 150 € par mois de prélèvement à source, soit un total annuel de 1 800 € .
 L'impôt calculé à partir de votre déclaration effectuée au printemps 2026 est de 2 100 € .
 Vous devrez verser un complément d'impôt de 300 € ( 2 100 € - 1 800 € ).
 Plusieurs raisons peuvent expliquer cet écart, notamment les suivantes :
 Vos revenus ont augmenté et vous n'avez pas demandé à changer votre taux de prélèvement 
 Vous avez touché un acompte de réductions ou crédits d'impôt trop élevé.
 Le complément (solde) d'impôt à payer est indiqué sur votre avis d'impôt.
```

### SCALEYEAR

Selected https://www.service-public.gouv.fr/particuliers/vosdroits/F1419; SCALEYEAR; https://www.service-public.gouv.fr/particuliers/vosdroits/F1419; read2026-10-29; nativeLF84–84; readerSHA256 `47ba2276514f0e7744c51dc863cadc485755cab30bd5f97319e6dcbe4f875c7f`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
 Le barème de l'impôt est fixé chaque année . Par exemple, le barème de 2026 (applicable aux revenus de 2025) est fixé par la loi de finances pour 2026.
```

### SCALERULE

Selected https://www.service-public.gouv.fr/particuliers/vosdroits/F1419; SCALERULE; https://www.service-public.gouv.fr/particuliers/vosdroits/F1419; read2026-10-29; nativeLF82–82; readerSHA256 `47ba2276514f0e7744c51dc863cadc485755cab30bd5f97319e6dcbe4f875c7f`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
 Pour appliquer le barème de l'impôt à votre revenu imposable, il faut tenir compte du quotient familial : titleContent , c'est-à-dire de votre nombre de parts, qui dépend de votre situation et du nombre de personnes dans votre foyer fiscal.
```

### GRIDDATE

Selected https://bofip.impots.gouv.fr/bofip/11255-PGP.html; GRIDDATE; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF71–71; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
 Grille des taux par défaut applicables aux contribuables domiciliés en métropole et hors de France à compter du 1 er mai 2026 Base mensuelle de prélèvement
```

### GRIDTERR1

Selected https://bofip.impots.gouv.fr/bofip/11255-PGP.html; GRIDTERR1; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF113–113; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
 II. Grille des taux par défaut applicables aux contribuables domiciliés en Guadeloupe, à La Réunion et en Martinique
```

### GRIDTERR2

Selected https://bofip.impots.gouv.fr/bofip/11255-PGP.html; GRIDTERR2; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF157–157; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
 III. Grille des taux par défaut applicables aux contribuables domiciliés en Guyane et à Mayotte
```

### SHORTGATE

BOI-IR-PAS-20-20-30-10§230 actualno-rate/initial≤2months/first2months clause; https://bofip.impots.gouv.fr/bofip/11252-PGP.html/identifiant%3DBOI-IR-PAS-20-20-30-10-20181228; read2026-10-29; nativeLF43–43; readerSHA256 `ab9c111e2a8568912ea2ce8643f7778bb16697b6014c80b713f4615d2736cbff`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Le deuxième alinéa du d du 1 du III de l'article 204 H du CGI prévoit que, pour les salaires versés au titre d'un contrat à durée déterminée ou d'un contrat de mission dont le terme initial n'excède pas deux mois ou dont le terme est imprécis, s'il s'agit d'un contrat à terme imprécis dont la durée minimale n'excède pas deux mois, les grilles mensuelles de taux par défaut s'appliquent, en l'absence de transmission du taux de prélèvement et dans la limite des deux premiers mois d'embauche, aux versements effectués au titre ou au cours d'un mois après un abattement égal à la moitié du montant mensuel du salaire minimum de croissance, quelle que soit la quotité de travail ou la durée du contrat dès lors qu'elle est inférieure à deux mois ou imprécise.
```

### SHORTRENEW

Selected Official selected indexed/web display: IR - Prélèvement à la source de l'impôt sur le revenu - Calcul du prélèvement - Taux du prélèvement - Taux par défaut - Situations et modalités d'application | bofip.impots.gouv.fr; SHORTRENEW; https://bofip.impots.gouv.fr/bofip/11252-PGP.html/identifiant%3DBOI-IR-PAS-20-20-30-10-20181228; read2026-10-29; nativeLF71–77; readerSHA256 `ab9c111e2a8568912ea2ce8643f7778bb16697b6014c80b713f4615d2736cbff`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
En cas de renouvellement ou de prolongation de ces contrats, l'abattement reste limité aux deux premiers mois de salaire.

En cas d'interruption entre deux CDD, le décompte du délai de deux mois est effectué séparément pour chaque contrat.

Exemple : Soit un salarié embauché en CDD pour une durée de deux semaines le 10 juin N. Avant son expiration, son CDD est prolongé jusqu'au 15 juillet. L'abattement « contrat court » reste applicable dans la limite des deux premiers mois.

S'il conclut un nouveau contrat d'une durée de deux mois avec le même employeur à compter du 1^{er} août et jusqu'au 30 septembre, l'abattement « contrat court » s'applique au titre de ce contrat pour deux mois si l'employeur ne dispose pas du taux transmis par l'administration fiscale.
```

### SHORTCALC

Selected Official selected indexed/web display: IR - Prélèvement à la source de l'impôt sur le revenu - Calcul du prélèvement - Taux du prélèvement - Taux par défaut - Situations et modalités d'application | bofip.impots.gouv.fr; SHORTCALC; https://bofip.impots.gouv.fr/bofip/11252-PGP.html/identifiant%3DBOI-IR-PAS-20-20-30-10-20181228; read2026-10-29; nativeLF97–107; readerSHA256 `ab9c111e2a8568912ea2ce8643f7778bb16697b6014c80b713f4615d2736cbff`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
L'abattement est appliqué à l'assiette du prélèvement. L'assiette après abattement est ensuite comparée aux limites de revenus de la grille de taux mensuelle afin de déterminer le taux par défaut correspondant, sans aucune correction.

En effet, pour les contrats courts, les grilles de taux par défaut ne sont jamais ajustées à la périodicité du versement.

La grille de taux par défaut établie en fonction des bases mensuelles de prélèvement s'applique dans tous les cas, y compris pour des revenus versés avec une périodicité usuelle de versement différente du mois, notamment pour ceux versés au titre d'une période inférieure.

Exemple : Un employeur recrute en contrat à durée déterminée, pour une durée de trois semaines, un salarié domicilié en métropole. Le montant imposable du salaire versé est de 1 500 euros. Il est supposé que le montant de l'abattement « contrats courts » en vigueur lors du versement du salaire est égal à 615 euros. Après abattement, l'assiette du prélèvement est de 885 euros (1 500 – 615).

L'employeur ne prélève aucune retenue à la source, dans la mesure où le taux proportionnel prévu par la grille de taux par défaut pour un montant de revenu mensuel imposable de 885 euros est nul.

Le taux par défaut, déterminé à partir de la grille de taux par défaut applicable, est ensuite appliqué au montant de l'assiette après abattement.
```

### CSGGATES

Selected Official selected indexed/web display: La CSG-CRDS - Urssaf.fr; CSGGATES; https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/csg-crds.html; read2026-10-29; nativeLF45–48; readerSHA256 `7dfc62b0ca19222b2edbfbc7c187436d4fc369a79bd2dda59ea856972f69ce6e`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Les CSG-CRDS sont dues sur les revenus d’activité des personnes qui remplissent les deux conditions cumulatives suivantes : 

  * condition n° 1 : elles doivent être domiciliées en France pour l’établissement de l’impôt sur le revenu (critère fiscal) ;
  * condition n° 2 : elles bénéficient d’un régime obligatoire français d’assurance maladie (critère social).
```

### CSGEXTRA

URSSAF fiscal-no/social-yes case and5.50% employee illness contribution; https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/csg-crds.html; read2026-10-29; nativeLF62–66; readerSHA256 `7dfc62b0ca19222b2edbfbc7c187436d4fc369a79bd2dda59ea856972f69ce6e`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
### Critère fiscal non satisfait MAIS critère social satisfait

Les CSG-CRDS ne sont pas dues MAIS une cotisation salariale d’assurance maladie est alors due. 

Cette cotisation, au taux de 5,50 %, est à déclarer à l'aide du code type de personnel (CTP) 206.
```

### CSGHEALTH

URSSAF employerhealth noallowance/fourPASS cap; https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/csg-crds.html; read2026-10-29; nativeLF98–106; readerSHA256 `7dfc62b0ca19222b2edbfbc7c187436d4fc369a79bd2dda59ea856972f69ce6e`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
La contribution patronale qui finance la complémentaire santé d’entreprise est soumise aux CSG-CRDS sans abattement pour frais professionnels.

### Pour aller plus loin

Pour connaître les revenus d’activité auxquels cette réduction de 1,75% n’est pas applicable, consultez le Bulletin officiel de la Sécurité sociale.

La réduction de 1,75 % ne s’applique toutefois que dans la limite de 4 plafonds annuels de la Sécurité sociale.

Une fois ce plafond atteint, les CSG-CRDS sont calculées sans réduction.
```

### POINTS

Selected https://www.service-public.gouv.fr/particuliers/vosdroits/F15396; POINTS; https://www.service-public.gouv.fr/particuliers/vosdroits/F15396; read2026-10-29; nativeLF124–124; readerSHA256 `8f294db2acf3a0f568d55465e1e5c61422545d24577a31c195cfd2de2a6543d6`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
La différence entre le taux de cotisation et le taux de calcul des points ne permet pas d'obtenir des points de retraite. Sa fonction est de contribuer au financement du régime de l'Agirc-Arrco.
```

### CEGCET

Selected Official selected original-language indexed display; CEGCET; https://www.agirc-arrco.fr/particuliers/ma-retraite/comprendre-ma-retraite/points-de-retraite-comment-sont-ils-obtenus/; read2026-10-29; nativeLF4–4; readerSHA256 `dff86eed36f07bf5bc1b01dad0833200083ae27c7bbc300d9e1bfe9ba56f219e`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
À ces taux de cotisations s’ajoutent : la contribution d’équilibre général (CEG) et la contribution d’équilibre technique (CET). Ces deux cotisations sont réparties à hauteur de 40 % à la charge du salarié et 60 % à la charge de l’employeur. La CET s’applique sur la tranche 1 et la tranche 2 pour tout salarié dont la rémunération dépasse le plafond de la Sécurité sociale.
```

### APEC

Selected Official selected original-language indexed display; APEC; https://www.agirc-arrco.fr/particuliers/ma-retraite/comprendre-ma-retraite/points-de-retraite-comment-sont-ils-obtenus/; read2026-10-29; nativeLF6–6; readerSHA256 `dff86eed36f07bf5bc1b01dad0833200083ae27c7bbc300d9e1bfe9ba56f219e`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Seules les cotisations correspondant aux taux de calcul des points (part salariale +part employeur) servent au calcul des points de retraite. La part supplémentaire des cotisations générées par l’application du taux d’appel, la contribution d’équilibre général (CEG) et la contribution d’équilibre technique (CET) servent à financer l’équilibre du régime et à la solidarité. Les caisses de retraite Agirc-Arrco recouvrent également, pour le compte de l’Association pour l’emploi des cadres (Apec), une cotisation au taux de 0,06 % (part salariale : 0,024 % ; part employeur : 0,036 %) sur les salaires des cadres, dans la limite de quatre plafonds de la Sécurité sociale.
```

### NOCHOMAGE

Selected Official selected indexed/web display: L’assurance chômage et l’AGS - Urssaf.fr; NOCHOMAGE; https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/assurance-chomage-ags.html; read2026-10-29; nativeLF18–18; readerSHA256 `c355a004945f5d3cc6e6f16489b72bba3a10e63bb870eb2829a9eb524bebc359`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Les cotisations d’assurance chômage et d’assurance de garantie des salaires (AGS) sont dues par les employeurs à l’Urssaf. Elles permettent le financement des allocations de chômage et le paiement des salariés en cas de liquidation ou redressement judiciaire de l’entreprise.
```

### OVERTIMEGATE

Selected Official selected indexed/web display: Réduction de cotisations salariales - Urssaf.fr; OVERTIMEGATE; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/exonerations-heures/reduction-cotisations-salariales.html; read2026-10-29; nativeLF18–18; readerSHA256 `d6cd9e5a4b17580843e31437c01934ec3b91bae2930244f49a65f8ecc0f0f6ac`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Lorsque vos salariés font des heures supplémentaires ou complémentaires, ils peuvent bénéficier d’une exonération : il s’agit de la réduction de cotisations salariales d’assurance vieillesse et veuvage de base. Elle s’applique à la rémunération des heures supplémentaires ou complémentaires, dans la limite de 11,31 %.
```

### OVERTIMECALC

Selected Official selected indexed/web display: Réduction de cotisations salariales - Urssaf.fr; OVERTIMECALC; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/exonerations-heures/reduction-cotisations-salariales.html; read2026-10-29; nativeLF81–81; readerSHA256 `d6cd9e5a4b17580843e31437c01934ec3b91bae2930244f49a65f8ecc0f0f6ac`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Rémunération versée au salarié au titre des heures supplémentaires ou complémentaires × taux des cotisations d’assurance vieillesse d’origine légale et conventionnelle obligatoires effectivement dues par le salarié, dans la limite de 11,31 %.
```

### OVERTIMECOND

Selected Official selected indexed/web display: Réduction de cotisations salariales - Urssaf.fr; OVERTIMECOND; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/exonerations-heures/reduction-cotisations-salariales.html; read2026-10-29; nativeLF69–71; readerSHA256 `d6cd9e5a4b17580843e31437c01934ec3b91bae2930244f49a65f8ecc0f0f6ac`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
  * respecter les règles légales et conventionnelles relatives à la durée du travail ;
  * ne pas remplacer le versement d’un élément de rémunération par le paiement d’heures supplémentaires ou complémentaires. Cette condition est respectée si un délai de douze mois s’est écoulé entre le dernier versement de l'élément de rémunération en tout ou partie supprimé et le premier paiement d’heures supplémentaires ou complémentaires ;
  * ne pas remplacer la rémunération de l’heure supplémentaire en totalité par un repos compensateur.
```

### REDUCEDAM

Selected Official selected indexed/web display: Ce qu’il faut savoir au 1er janvier 2026 - Urssaf.fr; REDUCEDAM; https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html; read2026-10-29; nativeLF91–91; readerSHA256 `565c80d230c5c770d3c1ed7b7596c5a380826e335d6ce25a7c68bd301e9fdc9b`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Pour les employeurs concernés bénéficiant d’exonérations spécifiques citées ci-dessus, le taux de la cotisation d’assurance maladie sera de 7 % si la rémunération annuelle du salarié est inférieure ou égale à 2,5 fois le Smic en vigueur au 31/12/2023. Au-delà de cette limite, le taux de la cotisation d’assurance maladie applicable sera de 13 %.
```

### REDUCEDAF

Selected Official selected indexed/web display: Ce qu’il faut savoir au 1er janvier 2026 - Urssaf.fr; REDUCEDAF; https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html; read2026-10-29; nativeLF99–99; readerSHA256 `565c80d230c5c770d3c1ed7b7596c5a380826e335d6ce25a7c68bd301e9fdc9b`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Pour les employeurs concernés bénéficiant d’exonérations spécifiques citées ci-dessus, le taux de la cotisation d’allocations familiales sera de 3,45 % si la rémunération annuelle du salarié est inférieure ou égale à 3,5 fois le Smic en vigueur au 31/12/2023. Au-delà de cette limite, le taux de la cotisation d’allocations familiales sera de 5,25 %.
```

### REDUCEDELIG

Selected Official selected indexed/web display: Ce qu’il faut savoir au 1er janvier 2026 - Urssaf.fr; REDUCEDELIG; https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html; read2026-10-29; nativeLF79–83; readerSHA256 `565c80d230c5c770d3c1ed7b7596c5a380826e335d6ce25a7c68bd301e9fdc9b`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
    * pour les employeurs bénéficiaires d’exonérations spécifiques dégressives à savoir :
      * les dispositifs zonés : zones de revitalisation rurale et zones France ruralités revitalisation (ZRR-ZFRR), zones de restructuration de la défense (ZRD), zones franches urbaines (ZFU) ;
      * le dispositif d’exonération de cotisations patronales applicables dans les territoires d’Outre-mer dit Lodéom ;
      * le dispositif d’exonération de cotisations patronales applicable aux aides à domicile employées par une entreprise prestataire de droit privé auprès d’une personne dite fragile (AAD prestataire) ;
    * pour les salariés, de certains employeurs, affiliés à un régime spécial pour lesquels la RGDU n’est pas applicable.
```

### RGDUELIG

Selected Official selected indexed/web display: La réduction générale dégressive unique - Urssaf.fr; RGDUELIG; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html; read2026-10-29; nativeLF43–46; readerSHA256 `91b41f59cde469dd2de147527b948d449d53f48df61ec32f5210c9623176e389`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
  * a une rémunération inférieure :
    * à 3 Smic applicable au 1^{er} janvier 2026 (ou 2,9293 Smic applicable au 1^{er} juin 2026) en métropole et dans les Drom (hors Mayotte) ;
    * à 1,6 Smic applicable à Mayotte en 2026 ;
  * est assuré contre le risque de perte d’emploi selon les modalités devant être retenues par l’employeur (notamment affiliation obligatoire au régime d’assurance chômage s’il s’agit du secteur privé).
```

### RGDUPARAM

Selected Official selected indexed/web display: Ce qu’il faut savoir au 1er janvier 2026 - Urssaf.fr; RGDUPARAM; https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html; read2026-10-29; nativeLF37–63; readerSHA256 `565c80d230c5c770d3c1ed7b7596c5a380826e335d6ce25a7c68bd301e9fdc9b`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Les paramètres sont les suivants :
Les valeurs de « T min » et « T delta » : la valeur maximale du coefficient est égale à la somme des valeurs T min et T delta.

Valeurs de « T min » et « T delta »
 | Employeurs de moins de 50 salariés  | Employeurs de 50 salariés et plus
--- | --- | ---
T min  | 0,0200  | 0,0200
T delta  | 0,3781  | 0,3821
Coefficient maximum  | 0,3981  | 0,4021
Valeurs de « T min » et « T delta »
 | Employeurs de moins de 50 salariés
--- | ---
T min  | 0,0200
T delta  | 0,3781
Coefficient maximum  | 0,3981
Valeurs de « T min » et « T delta »
 | Employeurs de 50 salariés et plus
--- | ---
T min  | 0,0200
T delta  | 0,3821
Coefficient maximum  | 0,4021

Le Smic à prendre en compte : la valeur du Smic à prendre en compte en 2026 pour le calcul du coefficient de la réduction générale est la valeur du Smic en vigueur ; les éventuelles revalorisations sont prises en compte. Le Smic est majoré le cas échéant des heures supplémentaires et complémentaires.

La rémunération brute annuelle : la rémunération prise en compte pour la détermination du coefficient reste celle définie à l'article L242-1 du CSS, majorée le cas échéant du montant de la prime de partage de la valeur.

Exposant ^{P} : il est égal à 1,75 et s’applique à [(½) × (3 × Smic annuel ÷ rémunération annuelle brute - 1)].
```

### RGDUFORM1

Selected Official selected indexed/web display: La réduction générale dégressive unique - Urssaf.fr; RGDUFORM1; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html; read2026-10-29; nativeLF110–110; readerSHA256 `91b41f59cde469dd2de147527b948d449d53f48df61ec32f5210c9623176e389`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
T min + (T delta × [(½) × (3 × ((Smic calculé pour un an + (Smic horaire × nombre d'heures supplémentaires ou complémentaires)) ÷ rémunération annuelle brute) - 1)]^{P}) = 0,0200 + (0,3781 × [(½) × (3 × ((Smic calculé pour un an + (Smic horaire × nombre d'heures supplémentaires ou complémentaires)) ÷ rémunération annuelle brute) - 1)]^{P})
```

### RGDUHOURS

Selected Official selected indexed/web display: La réduction générale dégressive unique - Urssaf.fr; RGDUHOURS; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html; read2026-10-29; nativeLF122–130; readerSHA256 `91b41f59cde469dd2de147527b948d449d53f48df61ec32f5210c9623176e389`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Smic horaire × 35 × 52 ÷ 12

Elle est applicable à votre salarié rémunéré à temps plein sur le mois.

Dans certains cas, elle est également applicable si votre salarié est rémunéré en dessous du Smic (par exemple pour les contrats d’apprentissage).

La valeur du Smic peut être ajustée pour tenir compte des temps partiels, des durées collectives de travail inférieures à la durée légale, de suspensions du contrat de travail.

En 2026, la valeur du Smic à prendre en compte est celle en vigueur au 1^{er} janvier 2026.
```

### RGDUFREEZE

Selected Official selected indexed/web display: La réduction générale dégressive unique - Urssaf.fr; RGDUFREEZE; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html; read2026-10-29; nativeLF130–136; readerSHA256 `91b41f59cde469dd2de147527b948d449d53f48df61ec32f5210c9623176e389`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
En 2026, la valeur du Smic à prendre en compte est celle en vigueur au 1^{er} janvier 2026.

Pour calculer le coefficient de la réduction de l’année 2026, vous devez donc utiliser l’une des deux formules suivantes :

     * T min + (T delta × [(½) × (3 × Smic calculé sur un an sur la base de sa valeur en vigueur au 1^{er} janvier 2026 ÷ rémunération annuelle brute - 1) ] ^{P}) ;
     * T min + (T delta × [(½) × (2,9293 × Smic calculé pour un an sur la base de sa valeur en vigueur au 1^{er} juin 2026 ÷ rémunération annuelle brute - 1)] ^{P}).

```

### RGDUPPV

Selected Official selected indexed/web display: La réduction générale dégressive unique - Urssaf.fr; RGDUPPV; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html; read2026-10-29; nativeLF87–95; readerSHA256 `91b41f59cde469dd2de147527b948d449d53f48df61ec32f5210c9623176e389`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Depuis 2025, la prime de partage de la valeur (PPV) est désormais prise en compte dans le calcul de la réduction générale.

Cette prise en compte doit être faite :

  * pour vérifier que la rémunération annuelle, PPV incluse est inférieure à 3 Smic ;
  * déterminer le coefficient de la réduction ;
  * calculer le montant de la réduction.

Cette prise en compte doit être faite dans tous les cas, que la PPV soit placée ou non sur un plan d’épargne.
```

### RGDUTRANS

Selected Official selected indexed/web display: La réduction générale dégressive unique - Urssaf.fr; RGDUTRANS; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html; read2026-10-29; nativeLF139–139; readerSHA256 `91b41f59cde469dd2de147527b948d449d53f48df61ec32f5210c9623176e389`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Le Boss indique que ces formules peuvent ne pas être appliquées aux cotisations et contributions dues au titre des rémunérations des salariés dont le contrat de travail aura pris fin entre le 1^{er} et le 30 juin 2026. Elles devront en revanche s’appliquer aux cotisations et contributions dues sur l’ensemble de l’année 2026 au titre de tous les salariés ayant encore un contrat de travail en cours au 1^{er} juillet 2026.
```

### RGDUCASE

Selected Official selected indexed/web display: La réduction générale dégressive unique - Urssaf.fr; RGDUCASE; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html; read2026-10-29; nativeLF143–147; readerSHA256 `91b41f59cde469dd2de147527b948d449d53f48df61ec32f5210c9623176e389`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Votre entreprise a 70 salariés et vous souhaitez calculer la réduction générale au titre de votre salarié sur le mois de juin 2026. Il travaille 35 heures par semaine, est présent tout le mois et n’a pas fait d’heure supplémentaire.

Pour un Smic brut mensuel de 1 867,02 € au 1^{er} juin 2026 et une rémunération mensuelle brute de 2 000 €, la valeur maximale du coefficient de réduction générale est de 0,3178.
Soit : 0,0200 + (0,3821 × [(½) × (2,9293 × 1 867,02 ÷ 2 000) - 1)]^{1,75}) = 0,3178.

```

### RGDUSTALE

Selected https://entreprendre.service-public.gouv.fr/vosdroits/F559; RGDUSTALE; https://entreprendre.service-public.gouv.fr/vosdroits/F559; read2026-10-29; nativeLF305–306; readerSHA256 `1ec936d34e56a20c42e49c2c96da2cad88eaa33475e4c39a85f8311c9931cc1a`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Allègements généraux dont bénéficient les employeurs au titre des salariés dont les rémunérations brutes sont inférieures à 1,6 Smic (2 987,23 €).
Réduction du taux de cotisations allocations familiales, dont bénéficient les employeurs au titre des salariés dont les rémunérations brutes sont inférieures à 3,5 Smic (6 534,56 €).
```

### OTEMPLOYER

Selected Official selected indexed/web display: Ce qu’il faut savoir au 1er janvier 2026 - Urssaf.fr; OTEMPLOYER; https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html; read2026-10-29; nativeLF135–136; readerSHA256 `565c80d230c5c770d3c1ed7b7596c5a380826e335d6ce25a7c68bd301e9fdc9b`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
    * 1,50 € pour les employeurs dont l’effectif est inférieur à 20 salariés ;
    * 0,50 € par heure supplémentaire pour les employeurs d’au moins 20 salariés et plus.
```

### OTEMPLOYERALL

URSSAF2026 all-headcount statutory eligibility and actual1.50/.50 rates; https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html; read2026-10-29; nativeLF129–136; readerSHA256 `565c80d230c5c770d3c1ed7b7596c5a380826e335d6ce25a7c68bd301e9fdc9b`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
À compter du 1^{er} janvier 2026, tous les employeurs éligibles à la réduction générale dégressive unique (RGDU) peuvent, quel que soit leur effectif, appliquer la déduction forfaitaire patronale sur les heures supplémentaires et les jours de repos auxquels renoncent les salariés en convention de forfait en jours, au-delà du plafond de 218 jours.

Le seuil de 250 salariés pour l’application de la déduction patronale sur les heures supplémentaires et les rachats des jours de RTT est donc supprimé.

Le montant de cette déduction est de :

    * 1,50 € pour les employeurs dont l’effectif est inférieur à 20 salariés ;
    * 0,50 € par heure supplémentaire pour les employeurs d’au moins 20 salariés et plus.
```

### TERMRATE

URSSAF2026 actual40% rate/January employment-period scope; https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html; read2026-10-29; nativeLF144–155; readerSHA256 `565c80d230c5c770d3c1ed7b7596c5a380826e335d6ce25a7c68bd301e9fdc9b`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
  * ## Indemnités de mise à la retraite et de rupture conventionnelle individuelle : hausse du taux de la contribution patronale

Indemnités de mise à la retraite et de rupture conventionnelle individuelle : hausse du taux de la contribution patronale

Une contribution patronale s’applique sur :

    * l’indemnité versée en cas de rupture conventionnelle individuelle ;
    * l’indemnité versée à l’occasion de la mise à la retraite à l’initiative de l’employeur (hors contrat de valorisation de l’expérience respectant les conditions prévues de mises à la retraite).

Cette contribution est due sur la part exclue de l’assiette des cotisations de Sécurité sociale qu’elle soit assujettie ou non à la CSG.

Le taux de cette contribution patronale passe de 30 % à 40 % à compter de la période d’emploi de janvier 2026.
```

### TERMLAW

Selected Official selected indexed display, not whole-source HTTP reading; TERMLAW; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053282399/2026-06-16; read2026-10-29; nativeLF14–18; readerSHA256 `9d75d2fc5b31f773341400d9eb17f050abc45f05c0d00098b754d4e150c272fa`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Est instituée, à la charge de l'employeur et au profit de la Caisse nationale d'assurance vieillesse, une contribution assise sur les indemnités versées à l'occasion de :
1° La mise à la retraite d'un salarié à l'initiative de l'employeur mentionnée à l'article L. 1237-5 du code du travail, pour la part exclue de l'assiette des cotisations de sécurité sociale en application du 7° du II de l'article L. 242-1 du présent code ;
2° La rupture conventionnelle mentionnée aux articles L. 1237-11 à L. 1237-15 du code du travail, pour leur part exclue de l'assiette des cotisations de sécurité sociale en application du 7° du II de l'article L. 242-1 du présent code.
Le taux de cette contribution est fixé à 40 %.

```

### SMICYOUTH

Selected Official selected indexed/web display: Montant du Smic - Urssaf.fr; SMICYOUTH; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/montant-smic.html; read2026-10-29; nativeLF13–13; readerSHA256 `67255c339b8d7ddbfcbe32f162b1c96b67cf41b7d7c363af3eb5ea965228dad6`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Un salarié de moins de 18 ans qui n’a pas encore 6 mois de pratique professionnelle dans sa branche d’activité peut percevoir un Smic minoré.
```

### SMICGEOG

Selected Official selected indexed/web display: Le Smic et le minimum garanti augmentent au 1er juin 2026 - Urssaf.fr; SMICGEOG; https://www.urssaf.fr/accueil/actualites/augmentation-smic.html; read2026-10-29; nativeLF21–25; readerSHA256 `2f90ca41e4d8d7d874162855cf7bc4d119527dc8d62605e09149ae999de270e8`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
À compter du 1^{er} juin 2026, le Smic horaire brut est fixé à 12,31 € soit un montant mensuel brut à 1 867,02 € sur la base de la durée légale du travail de 35 heures hebdomadaires en métropole, Guadeloupe, Guyane, Martinique, à La Réunion, Saint-Barthélemy, Saint-Martin et Saint-Pierre-et-Miquelon.

À Mayotte, le Smic horaire brut est porté à 9,56 € soit un montant mensuel brut de 1 449,93 € sur la base de la durée légale du travail de 35 heures hebdomadaires.

Le minimum garanti s'établit à 4,35 €.
```

### WORKDEROG

Selected https://www.service-public.gouv.fr/particuliers/vosdroits/F1911; WORKDEROG; https://www.service-public.gouv.fr/particuliers/vosdroits/F1911; read2026-10-29; nativeLF110–113; readerSHA256 `44f04e7087f6d573887b75b4fd33c975de664eb9eec806f65d76bff0ccaeafa2`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Cependant, des dérogations sont accordées dans les cas suivants :
Soit à la demande de l'employeur, qui doit solliciter l'accord de l'inspecteur du travail
Soit en cas d'urgence liée à un surcroît temporaire d'activité
Soit si une convention collective: titleContent le prévoit. En cas d'activité accrue ou pour des motifs liés à l'organisation de l'entreprise, la durée maximale quotidienne de travail est limitée à 12 heures par jour de travail effectif.
```

### OVERTIMEPREM

F2391 collective≥10% versus default25%/50% overtime remuneration; https://www.service-public.gouv.fr/particuliers/vosdroits/F2391; read2026-10-29; nativeLF130–149; readerSHA256 `261857ea17b01f9b14e6c61fafe479ca64379019cd58a9a66b4710db9a55a71c`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Le taux de rémunération des heures supplémentaires dépend de l'application ou non d'une convention collective: titleContent ou d'un accord collectif d'entreprise: titleContent ou d'un accord de branche étendu: titleContent.
Répondez aux questions successives et les réponses s’afficheront automatiquement
Dispositions conventionnelles prévues
La convention collective ou l'accord collectif d'entreprise ou l'accord de branche étendu fixe le taux de rémunération des heures supplémentaires accomplies au-delà de la durée légale hebdomadaire.
Un simulateur permet de connaitre le taux de majoration des heures supplémentaires dans une convention collective :
Savoir ce que la convention collective prévoit concernant les contreparties en cas d’heures supplémentaires d’un salarié
La rémunération fait l'objet d'un ou plusieurs taux de majoration en fonction du nombre d'heures effectuées.
Chaque taux est au minimum fixé à 10 %.
La majoration s'applique sur le montant brut du salaire.
À noter
Les heures supplémentaires (effectuées de jour ou de nuit) sont décomptées par semaine civile: titleContent.
La rémunération des heures supplémentaires peut être remplacée, en tout ou partie, par un repos compensateur: titleContent équivalent.
Dans ce cas, la durée de ce repos est équivalente à la rémunération majorée.
Exemple :
Une heure supplémentaire payée en principe à un taux majoré de 50 % donne lieu à un repos compensateur équivalent (soit 1 heure 30).
En l'absence de dispositions conventionnelles prévues
En l'absence de dispositions conventionnelles: titleContent, les heures accomplies au-delà de la durée légale hebdomadaire sont majorées de :
25 % pour les 8 premières heures supplémentaires travaillées dans la même semaine (de la 36e à la 43e heure)
50 % pour les heures suivantes (à partir de la 44e heure)
La majoration s'applique sur le montant brut du salaire.
```

### OVERTIMEWEEK

Selected https://www.service-public.gouv.fr/particuliers/vosdroits/F2391; OVERTIMEWEEK; https://www.service-public.gouv.fr/particuliers/vosdroits/F2391; read2026-10-29; nativeLF140–144; readerSHA256 `261857ea17b01f9b14e6c61fafe479ca64379019cd58a9a66b4710db9a55a71c`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Les heures supplémentaires (effectuées de jour ou de nuit) sont décomptées par semaine civile: titleContent.
La rémunération des heures supplémentaires peut être remplacée, en tout ou partie, par un repos compensateur: titleContent équivalent.
Dans ce cas, la durée de ce repos est équivalente à la rémunération majorée.
Exemple :
Une heure supplémentaire payée en principe à un taux majoré de 50 % donne lieu à un repos compensateur équivalent (soit 1 heure 30).
```

### LEAVEOVERTIME

Selected https://www.service-public.gouv.fr/particuliers/vosdroits/F2391; LEAVEOVERTIME; https://www.service-public.gouv.fr/particuliers/vosdroits/F2391; read2026-10-29; nativeLF181–182; readerSHA256 `261857ea17b01f9b14e6c61fafe479ca64379019cd58a9a66b4710db9a55a71c`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Lorsque la durée du travail est décomptée à la semaine ou sur 2 semaines dans l’entreprise, les congés payés pris durant cette période sont considérés comme du temps de travail effectif pour le décompte des heures supplémentaires.
Cela signifie que, si le salarié a été absent une partie de la semaine du fait de congés payés, les heures qu’il aurait dû effectuer s’il n’avait pas été en congés payés sont prises en compte pour le calcul des heures supplémentaires.
```

### LEAVEYEAR

Selected https://www.service-public.gouv.fr/particuliers/vosdroits/F2258; LEAVEYEAR; https://www.service-public.gouv.fr/particuliers/vosdroits/F2258; read2026-10-29; nativeLF103–104; readerSHA256 `2f2a69d967d21ca2deef3d2cfbd08ab9651d90fbc9a0f9cf71c2868ab7069ee0`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
En cas d'arrêt de travail en raison de maladie non professionnelle, le salarié bénéficie des droits à congés payés, dans la limite de 2 jours ouvrables: titleContent par mois (soit 24 jours ouvrables par an) pendant la période d'acquisition des congés dite période de référence: titleContent. La période de référence est fixée du 1er juin de l'année N-1 au 31 mai de l'année N (sauf si une convention collective: titleContent ou un accord collectif d'entreprise: titleContent prévoit une autre période).
Lorsque le nombre de jours de congés acquis n'est pas un nombre entier, la durée du congé est portée au nombre entier immédiatement supérieur. Par exemple, si le salarié a travaillé 5 mois au cours de l'année, il bénéficie d'un congé de 2,5 × 5 = 12,5, arrondi à 13 jours ouvrables.
```

### FRACTION

Selected Official selected original-language indexed display; FRACTION; https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000033020705/2026-03-03; read2026-10-29; nativeLF20–30; readerSHA256 `3482f8bbd2d434a1faacf736ef34af9975717172bdd8939d3f767b22603460bc`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
A défaut de stipulation dans la convention ou l'accord conclu en application de l'article L. 3141-22 :

1° La fraction continue d'au moins douze jours ouvrables est attribuée pendant la période du 1er mai au 31 octobre de chaque année ;

2° Le fractionnement des congés au delà du douzième jour est effectué dans les conditions suivantes :

a) Les jours restant dus en application du second alinéa de l'article L. 3141-19 peuvent être accordés en une ou plusieurs fois en dehors de la période du 1er mai au 31 octobre de chaque année ;

b) Deux jours ouvrables de congé supplémentaire sont attribués lorsque le nombre de jours de congé pris en dehors de cette période est au moins égal à six et un seul lorsque ce nombre est compris entre trois et cinq jours. Les jours de congé principal dus au delà de vingt-quatre jours ouvrables ne sont pas pris en compte pour l'ouverture du droit à ce supplément.

Il peut être dérogé au présent article après accord individuel du salarié.
```

### SICKBASE

Selected https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; SICKBASE; https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; read2026-10-29; nativeLF138–143; readerSHA256 `0b86b2957a0c12bcfc52bf23f74098f379cb098bf9b30243347015dffd70a60f`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Votre salaire pris en compte pour calculer votre gain journalier de base, est plafonné à 1,4 fois le montant du Smic en vigueur, lors du dernier jour du mois qui précède l'arrêt (soit 2 613,82 € par mois en 2026).
Si vous touchez un salaire supérieur, le calcul de vos IJ sera le suivant :
Salaire journalier de base = 85,93 € [(2 613,82 € x 3) / 91,25]
IJ = 42,97 € (85,93 x 50 %).
Attention
Pour les arrêts ayant débuté avant le 1ᵉʳ avril 2025, l’ancien plafond reste applicable : le salaire pris en compte pour le calcul du gain journalier de base est plafonné à 1,8 fois le montant du Smic en vigueur, lors du dernier jour du mois qui précède l'arrêt.
```

### SICKWAIT

Selected https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; SICKWAIT; https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; read2026-10-29; nativeLF148–148; readerSHA256 `0b86b2957a0c12bcfc52bf23f74098f379cb098bf9b30243347015dffd70a60f`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Les IJ sont versées après un délai de carence: titleContent de 3 jours.
```

### SICKEXCEPT

Selected https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; SICKEXCEPT; https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; read2026-10-29; nativeLF153–158; readerSHA256 `0b86b2957a0c12bcfc52bf23f74098f379cb098bf9b30243347015dffd70a60f`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Il n'y a pas de délai de carence en cas de reprise d'activité entre 2 arrêts de travail n'ayant pas dépassé 48 heures. De même, il n'y a pas de délai de carence en cas d'arrêts de travail successifs dus à une affection de longue durée (ALD): titleContent.
Les jours de carence sont comptés dans le calcul de votre retraite dans la mesure où c'est la durée de l'arrêt qui est prise en compte.
Pour les arrêts de courte durée, il n'y a pas d'impact sur le calcul de votre retraite.
En revanche, si les arrêts sont de longue durée, ils sont pris en compte également comme suit : 1 trimestre est validé pour chaque période de 60 jours d'indemnisation dans la limite de 4 trimestre par an.
Comment s'effectue le versement des indemnités journalières suite à un arrêt maladie d'un salarié ?
Jours indemnisés
```

### SICKGATES

Selected Official indexed selected original-language display; SICKGATES; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047983348/2026-09-29; read2026-10-29; nativeLF25–31; readerSHA256 `a585d85a83024ac87a4a5fff45b066f58ce4fb20bd2447e83b01adfb8a3181c7`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
1° Pour avoir droit aux indemnités journalières de l'assurance maladie pendant les six premiers mois d'interruption de travail, aux allocations journalières de maternité et aux indemnités journalières de l'assurance maternité, l'assuré social doit justifier aux dates de référence prévues aux 2°, 3 et 5° de l'article cite5†R. 313-1 :

a) Soit que le montant des cotisations dues au titre des assurances maladie, maternité, invalidité et décès assises sur les rémunérations qu'il a perçues pendant les six mois civils précédents est au moins égale au montant des mêmes cotisations dues pour un salaire égal à 1 015 fois la valeur du salaire minimum de croissance au premier jour de la période de référence ;

b) Soit avoir effectué au moins 150 heures de travail salarié ou assimilé au cours des trois mois civils ou des quatre-vingt-dix jours précédents.

L'assuré doit en outre justifier de six mois d'affiliation à la date présumée de l'accouchement pour bénéficier des indemnités journalières de l'assurance maternité.
```

### SICKLONG

Selected Official indexed selected original-language display; SICKLONG; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047983348/2026-09-29; read2026-10-29; nativeLF33–39; readerSHA256 `a585d85a83024ac87a4a5fff45b066f58ce4fb20bd2447e83b01adfb8a3181c7`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
2° Lorsque l'arrêt de travail se prolonge sans interruption au-delà du sixième mois, l'assuré social, pour avoir droit aux indemnités journalières après le sixième mois d'incapacité de travail, doit avoir été affilié depuis douze mois au moins à la date de référence prévue au 2° de l'article R. 313-1.

Il doit justifier en outre :

a) Soit que le montant des cotisations dues au titre des assurances maladie, maternité, invalidité et décès assises sur les rémunérations qu'il a perçues pendant les douze mois civils précédant l'interruption de travail est au moins égal au montant des mêmes cotisations dues pour un salaire égal à 2 030 fois la valeur du salaire minimum de croissance au 1er janvier qui précède immédiatement le début de cette période ;

b) Soit qu'il a effectué au moins 600 heures de travail salarié ou assimilé au cours des douze mois civils ou des 365 jours précédant l'interruption de travail.
```

### SICKDATE

Selected Official indexed selected original-language display; SICKDATE; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006156797/?anchor=LEGIARTI000006749178; read2026-10-29; nativeLF46–48; readerSHA256 `be56be84c531f7e750e6549676e3f2dce700c3100cc499538e205a2274726250`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
2°) les prestations en espèces de l'assurance maladie, au jour de l'interruption de travail ;

3°) les prestations en espèces de l'assurance maternité, au début du 9e mois avant la date présumée de l'accouchement ou à la date du début du repos prénatal ;
```

### TOPUPGATES

Selected https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; TOPUPGATES; https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; read2026-10-29; nativeLF191–196; readerSHA256 `0b86b2957a0c12bcfc52bf23f74098f379cb098bf9b30243347015dffd70a60f`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Avoir 1 an au moins d'ancienneté dans l'entreprise (calculée à partir de votre 1er jour d'absence)
Avoir transmis à l'employeur le certificat médical dans les 48 heures
Être assuré social et relever d’un régime de Sécurité sociale ouvrant droit au versement d’indemnités journalières: titleContent
Être soigné en France ou dans l'un des États membres de l'Espace économique européen (EEE): titleContent
Ne pas être travailleur à domicile ou salarié saisonnier, intermittent ou temporaire.
Le versement effectif des indemnités journalières par la Sécurité sociale n’est pas une condition pour bénéficier des indemnités complémentaires versées par l’employeur.
```

### TOPUPOFFSET

Selected https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; TOPUPOFFSET; https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; read2026-10-29; nativeLF225–227; readerSHA256 `0b86b2957a0c12bcfc52bf23f74098f379cb098bf9b30243347015dffd70a60f`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Pour calculer le montant versé par l'employeur, il faut déduire les IJ versées par votre organisme de Sécurité sociale (CPAM, MSA,...) et, si c'est le cas, les prestations résultant des versements de l'employeur dans le cadre d'un régime complémentaire de prévoyance.
Votre convention collective peut prévoir des dispositions plus favorables (comme par exemple le maintien intégral de votre salaire).
Si les IJ versées par votre organisme de Sécurité sociale (CPAM, MSA,...) sont réduites (par exemple, en raison d'une hospitalisation ou d'une sanction de la CPAM: titleContent pour non-respect de son règlement), le montant versé par l'employeur reste calculé en tenant compte du montant intégral des IJ.
```

### TOPUPHISTORY

Selected https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; TOPUPHISTORY; https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; read2026-10-29; nativeLF221–221; readerSHA256 `0b86b2957a0c12bcfc52bf23f74098f379cb098bf9b30243347015dffd70a60f`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Si vous avez déjà bénéficié d'une ou plusieurs périodes d'indemnisation pour maladie par l'employeur dans les 12 mois précédents, la durée de versement est déduite du nombre de jours déjà indemnisés.
```

### TOPUPDAY

Selected Official selected indexed/web display: Article D1226-3 - Code du travail - Légifrance; TOPUPDAY; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000019225874/2026-03-07; read2026-10-29; nativeLF16–18; readerSHA256 `3dc5167f3a120a657ec7756bce70b1ce7759a51c58172cfc00e0a18b9a582fff`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Lors de chaque arrêt de travail, les durées d'indemnisation courent à compter du premier jour d'absence si celle-ci est consécutive à un accident du travail ou à une maladie professionnelle, à l'exclusion des accidents de trajet.

Toutefois, dans tous les autres cas, le délai d'indemnisation court au-delà de sept jours d'absence.
```

### ATDAY

Selected Official selected indexed/web display: Article L433-1 - Code de la sécurité sociale - Légifrance; ATDAY; https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000053283560/2026-02-15; read2026-10-29; nativeLF20–22; readerSHA256 `b8a9330797fa892af334569a6fa093cffe0fcc6da9611f7cf71b8ccd04262cae`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
La journée de travail au cours de laquelle l'accident s'est produit, quel que soit le mode de paiement du salaire, est intégralement à la charge de l'employeur.

Une indemnité journalière est payée à la victime par la caisse primaire, à partir du premier jour qui suit l'arrêt du travail consécutif à l'accident sans distinction entre les jours ouvrables et les dimanches et jours fériés. L'indemnité journalière est servie pendant une période d'une durée maximale fixée par décret, calculée de date à date. Cette durée maximale ne peut être plus courte que la période mentionnée au 1° de l'article L. 323-1. Dans le cas d'une interruption suivie d'une reprise du travail, cette période court à nouveau dès le jour où la reprise du travail a atteint une durée minimale fixée par décret.
```

### MATERNITYSTOP

Selected https://www.service-public.gouv.fr/particuliers/vosdroits/F2265; MATERNITYSTOP; https://www.service-public.gouv.fr/particuliers/vosdroits/F2265; read2026-10-29; nativeLF131–131; readerSHA256 `2ded1aba372608f34bf664c592123bf9fce595b1eb1b275ab08931d585e50bd9`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Vous pouvez renoncer à une partie de votre congé de maternité, mais vous devez obligatoirement cesser de travailler au moins 8 semaines dont 6 après l'accouchement.
```

### MATERNITYCONTRACT

Selected https://www.service-public.gouv.fr/particuliers/vosdroits/F2265; MATERNITYCONTRACT; https://www.service-public.gouv.fr/particuliers/vosdroits/F2265; read2026-10-29; nativeLF237–240; readerSHA256 `2ded1aba372608f34bf664c592123bf9fce595b1eb1b275ab08931d585e50bd9`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Pendant votre congé de maternité, votre contrat de travail est suspendu: titleContent.
Vous ne percevez pas votre salaire durant cette période.
Toutefois, vous avez droit aux indemnités journalières (IJ) pour maternité selon votre situation personnelle.
Répondez aux questions successives et les réponses s’afficheront automatiquement
```

### MATERNITYCALC

Selected https://www.service-public.gouv.fr/particuliers/vosdroits/F2265; MATERNITYCALC; https://www.service-public.gouv.fr/particuliers/vosdroits/F2265; read2026-10-29; nativeLF269–272; readerSHA256 `2ded1aba372608f34bf664c592123bf9fce595b1eb1b275ab08931d585e50bd9`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Calcul du salaire journalier de base : somme des 3 derniers salaires bruts perçus avant la date d'interruption du travail, divisé par un coefficient de 91,25.
Montant maximal du salaire journalier de base : Le salaire pris en compte ne peut pas dépasser le plafond mensuel de la sécurité sociale en vigueur lors du dernier jour du mois qui précède l'arrêt (soit 4 005 € par mois en 2026 ou 3 925 € en 2025).
Taux forfaitaire appliqué par la CPAM : la CPAM retire à ce salaire journalier de base un taux forfaitaire de 21 %.
Montant minimal et montant maximal des IJ : le montant ne peut pas être inférieur à 11,12 € ni supérieur à 104,02 € par jour.
```

### MATDATE

Selected Official indexed selected original-language display; MATDATE; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006156797/?anchor=LEGIARTI000006749178; read2026-10-29; nativeLF48–48; readerSHA256 `be56be84c531f7e750e6549676e3f2dce700c3100cc499538e205a2274726250`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
3°) les prestations en espèces de l'assurance maternité, au début du 9e mois avant la date présumée de l'accouchement ou à la date du début du repos prénatal ;
```

### PATERNITY

Selected https://www.service-public.gouv.fr/particuliers/vosdroits/F3156; PATERNITY; https://www.service-public.gouv.fr/particuliers/vosdroits/F3156; read2026-10-29; nativeLF150–150; readerSHA256 `ff172456cc952a865b582d6faf81aedd021bbf26bf6245ea5f0e15bd7674de3e`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Le congé doit être pris dans les 6 mois suivant la naissance ou l'accueil de l'enfant.
```

### PRIMES

F2301 compulsorysource/13th-month salary nature; https://www.service-public.gouv.fr/telecharger-pdf?path=aHR0cHM6Ly93d3cuc2VydmljZS1wdWJsaWMuZ291di5mci9wYXJ0aWN1bGllcnMvdm9zZHJvaXRzL0YyMzAxP2xhbmc9ZW4%3D; read2026-10-29; nativeLF3–3; readerSHA256 `21cec525b0f93bcc759b878e9d68f465496275775b1bd923754637d367697f4b`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Les primes et les gratifications viennent en complément du salaire. Leur versement est obligatoire s'il est prévu par l'un des dispositifs suivants : Contrat de travail Accord collectif Usage Engagement unilatéral de l'employeur. Un simulateur permet de connaître les primes prévues par certaines conventions collectives : Connaître les primes prévues par la convention collective (https://code.travail.gouv.fr/contribution/quelles-sont-les-primes-prevues-par-la-convention-collective?src_url=https://service- public.gouv.fr/particuliers/vosdroits/F2301) Ces sommes constituent un élément du salaire. Il s'agit par exemple des primes suivantes : Primes et gratifications annuelles (primes de fin d'année, de 13e mois, de vacances, de bilan, de participation, etc.) 
```

### MUTUELLEGATES

Selected https://entreprendre.service-public.gouv.fr/vosdroits/F33754; MUTUELLEGATES; https://entreprendre.service-public.gouv.fr/vosdroits/F33754; read2026-10-29; nativeLF100–100; readerSHA256 `50413f1995dc2bd279f48c73f071771fffcc172dea0d7aeb97c682e97e7a1ac7`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Tout employeur du secteur privé (entreprise et association) a l'obligation de proposer une couverture complémentaire santé collective à ses salariés, sauf exceptions. Cette couverture peut être assurée notamment par une mutuelle. Un particulier employant un salarié à domicile n'est pas concerné. Certains salariés en contrat court peuvent être dispensés d'adhérer à la complémentaire santé collective et bénéficier d'un versement santé par l'employeur. Nous vous présentons les règles à connaître.
```

### MUTUELLEBASKET

Selected https://entreprendre.service-public.gouv.fr/vosdroits/F33754; MUTUELLEBASKET; https://entreprendre.service-public.gouv.fr/vosdroits/F33754; read2026-10-29; nativeLF137–143; readerSHA256 `50413f1995dc2bd279f48c73f071771fffcc172dea0d7aeb97c682e97e7a1ac7`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
La complémentaire santé d'entreprise doit prendre en charge au minimum les garanties suivantes (panier de soins) :
Intégralité du ticket modérateur sur les consultations, actes et prestations remboursables par l'Assurance maladie. Cependant, des exceptions peuvent exister.
Totalité du forfait journalier hospitalier en cas d'hospitalisation
Frais dentaires (prothèses et orthodontie) à hauteur de 125 % du tarif conventionnel: titleContent
Frais d'optique de manière forfaitaire par période de 2 ans (annuellement pour les enfants ou en cas d'évolution de la vue) avec un minimum de prise en charge fixé à 100 € pour une correction simple, 150 € (voire 200 €) pour une correction complexe.
Garanties d'un contrat dit responsable
La complémentaire santé peut être un contrat dit responsable.
```

### PORTABILITY

Selected Official selected indexed/web display: Chapitre 1 : Détermination des garanties complémentaires des salariés (Articles L911-1 à L911-9) - Légifrance; PORTABILITY; https://www.legifrance.gouv.fr/codes/id/LEGIARTI000006745464/2026-07-11; read2026-10-29; nativeLF15–27; readerSHA256 `da316c033e1c3077edc8f0cea00a1ee2c05057d7e67687472d63d07317de29c7`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Les salariés garantis collectivement, dans les conditions prévues à l'article L. 911-1, contre le risque décès, les risques portant atteinte à l'intégrité physique de la personne ou liés à la maternité ou les risques d'incapacité de travail ou d'invalidité bénéficient du maintien à titre gratuit de cette couverture en cas de cessation du contrat de travail, non consécutive à une faute lourde, ouvrant droit à prise en charge par le régime d'assurance chômage, selon les conditions suivantes :

1° Le maintien des garanties est applicable à compter de la date de cessation du contrat de travail et pendant une durée égale à la période d'indemnisation du chômage, dans la limite de la durée du dernier contrat de travail ou, le cas échéant, des derniers contrats de travail lorsqu'ils sont consécutifs chez le même employeur. Cette durée est appréciée en mois, le cas échéant arrondie au nombre supérieur, sans pouvoir excéder douze mois ;

2° Le bénéfice du maintien des garanties est subordonné à la condition que les droits à remboursements complémentaires aient été ouverts chez le dernier employeur ;

3° Les garanties maintenues au bénéfice de l'ancien salarié sont celles en vigueur dans l'entreprise ;

4° Le maintien des garanties ne peut conduire l'ancien salarié à percevoir des indemnités d'un montant supérieur à celui des allocations chômage qu'il aurait perçues au titre de la même période ;

5° L'ancien salarié justifie auprès de son organisme assureur, à l'ouverture et au cours de la période de maintien des garanties, des conditions prévues au présent article ;

6° L'employeur signale le maintien de ces garanties dans le certificat de travail et informe l'organisme assureur de la cessation du contrat de travail mentionnée au premier alinéa.
```

### HEALTHTAX

CGI83(1quater), BOI-RSA-BASE-30-10-20§200 employer health contribution taxable; https://bofip.impots.gouv.fr/bofip/5956-PGP.html/identifiant%3DBOI-RSA-BASE-30-10-20-20260217; read2026-10-29; nativeLF20–25; readerSHA256 `1c0a9d53caba9249b54ccb28d9624ef5cf8c1f5c63b52d859b1958d11ac293a6`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Le 1° quater de l’article 83 du CGI autorise la déduction, sous plafond :

  * des cotisations ou primes à la charge des salariés ;
  * de la part des cotisations à la charge des employeurs et, le cas échéant, du comité d’entreprise, correspondant à des garanties autres que celles portant sur le remboursement et l’indemnisation de frais de santé. Il s’agit, en pratique, des cotisations versées au titre des garanties incapacité, invalidité, décès et dépendance, versées aux régimes de prévoyance complémentaire mis en place dans l’entreprise dans les conditions prévues à l’article L. 911-1 du CSS auxquels le salarié est affilié à titre obligatoire.

Remarque : Les cotisations à la charge de l’employeur et, le cas échéant, du comité d’entreprise qui correspondent à des garanties portant sur le remboursement ou l’indemnisation de frais de santé (maladie, maternité ou accident) constituent des compléments de rémunération qui sont compris dans la rémunération imposable du salarié (BOI-RSA-CHAMP-20-30-50).
```

### PPVGATES

Selected Official selected indexed/web display: La prime de partage de la valeur - Urssaf.fr; PPVGATES; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/prime-partage-valeur.html; read2026-10-29; nativeLF134–148; readerSHA256 `0fd1801bfc678e9f8f76d7b3c7c83766a4273bc024b142bfc0cc19a099fa01c7`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
La prime de partage de la valeur peut être exonérée dans la limite de 3 000 € par bénéficiaire et par an.

Cette limite d’exonération passe à 6 000 € par bénéficiaire et par an si vous mettez en œuvre :

  * soit un dispositif d’intéressement alors même que vous êtes soumis à l’obligation de mettre en place de la participation ;
  * soit un dispositif d’intéressement ou de participation alors même que vous n’êtes pas soumis à l’obligation de mettre en place de la participation.

Ces dispositifs doivent être mis en œuvre à la date de versement de la prime ou être conclus au titre du même exercice que celui du versement de la prime.

#### Bon à savoir

Vous n’êtes pas soumis au respect de cette condition de mise en place d’un dispositif d’intéressement ou de participation volontaire si vous êtes :

  * une association ou fondation reconnue d’utilité publique ou d’intérêt général ;
  * un Ésat, pour les primes versées à vos travailleurs handicapés.
```

### PPVWIDE

Selected Official selected indexed/web display: La prime de partage de la valeur - Urssaf.fr; PPVWIDE; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/prime-partage-valeur.html; read2026-10-29; nativeLF156–176; readerSHA256 `0fd1801bfc678e9f8f76d7b3c7c83766a4273bc024b142bfc0cc19a099fa01c7`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Du 1^{er} janvier 2024 au 31 décembre 2026, ce régime particulier continue à s’appliquer si, d’une part, l’effectif de votre entreprise est inférieur à 50 salariés et si, d’autre part, la rémunération de votre salarié est inférieure à 3 Smic annuels.

En effet, à compter du 1^{er} janvier 2024, si l’effectif de votre entreprise est égal ou supérieur à 50 salariés, l’exonération appliquée à la prime versée au salarié est réduite même si sa rémunération est inférieure à 3 Smic annuels.

Entreprise de moins de 50 salariés et rémunération inférieure à 3 Smic annuels Entreprise d’au moins 50 salariés et quelle que soit la rémunération

#### Entreprise de moins de 50 salariés et rémunération inférieure à 3 Smic annuels

La prime est exonérée de cotisations de Sécurité sociale.

Elle est aussi exonérée des CSG-CRDS, ou de la contribution sociale spécifique (Mayotte), d’impôt sur le revenu, de taxe sur les salaires ainsi que de forfait social.

Selon les cas exposés ci-dessus, l’exonération s’applique dans la limite de 3 000 € ou 6 000 €.

#### Entreprise d’au moins 50 salariés et quelle que soit la rémunération

La prime est exonérée de cotisations de Sécurité sociale.

Elle est par contre soumise à CSG-CRDS, ou à la contribution sociale spécifique (Mayotte), à l’impôt sur le revenu et à la taxe sur les salaires.

De plus, le forfait social au taux de 20 % est dû si l’effectif de votre entreprise est égal ou supérieur à 250 salariés.
```

### EXPENSEGATE

Selected Official selected indexed/web display: Frais professionnels - Urssaf.fr; EXPENSEGATE; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/frais-professionnels.html; read2026-10-29; nativeLF19–19; readerSHA256 `2f95557a1778591113fbc0039ac414b3afdbc9661b974826bc4890e315a0d021`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Les dépenses engagées par le salarié pour les besoins de son activité professionnelle sont des frais professionnels que l’employeur est tenu de lui rembourser. Les frais professionnels justifiés ne sont pas soumis à cotisations de Sécurité sociale et à CSG-CRDS.
```

### PAYSLIPZONES

Selected https://entreprendre.service-public.gouv.fr/vosdroits/F559; PAYSLIPZONES; https://entreprendre.service-public.gouv.fr/vosdroits/F559; read2026-10-29; nativeLF119–157; readerSHA256 `1ec936d34e56a20c42e49c2c96da2cad88eaa33475e4c39a85f8311c9931cc1a`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Depuis le 1er juillet 2023
La fiche doit mentionner les éléments suivants :
Zone 1 : identification de l'employeur et du salarié
Nom et adresse de l'employeur (éventuellement la désignation de l'établissement dont dépend le salarié)
Numéro de la nomenclature d'activité de l'établissement d'emploi (code APE ou code NAF) et numéro d'inscription de l'employeur au répertoire national des entreprises et des établissements (numéro Siret)
Convention collective de branche applicable au salarié ou référence au code du travail concernant la durée des congés payés et des délais de préavis en cas de cessation de la relation de travail
Nom et emploi du salarié, sa position dans la classification conventionnelle (niveau ou coefficient hiérarchique)
Période et nombre d'heures de travail en distinguant les heures au taux normal et les heures supplémentaires (en mentionnant les taux appliqués aux heures correspondantes)
Nature et volume du forfait auquel se rapporte le salaire des salariés au forfait (forfait hebdomadaire ou mensuel en heures, ou forfait annuel en heures ou en jours)
Nature de la base de calcul du salaire lorsque, par exception, cette base de calcul n'est pas la durée du travail
Nature et montant des accessoires de salaire soumis aux cotisations salariales et patronales
Zone 2 : salaire
Rémunération brute du salarié
Montant et assiette: titleContent des cotisations et contributions sociales à la charge de l'employeur et du salarié avant déduction des exonérations et exemptions
Taux des cotisations et contributions sociales à la charge du salarié avant déduction des exonérations et exemptions
Nature et montant des autres versements et retenues (notamment prise en charge des frais de transport domicile-travail)
Montant effectivement reçu par le salarié
Date de paiement
Dates de congé et montant de l'indemnité de congés payés, lorsqu'une période de congé annuel est comprise dans la période de paie considérée
Zone 3 : cotisations et contributions sociales
Montant des cotisations de protection sociale réunies au sein de 5 rubriques (santé, accidents du travail et maladies professionnelles, retraite, famille et chômage)
Montant total des exonérations et exemptions de cotisations et contributions sociales
Montant total versé par l'employeur (rémunération brute versée au salarié, cotisations et contributions à la charge de l'employeur, déduction faite des exonérations et allégements de charges sociales)
Montant correspondant à l'évolution de la rémunération liée à la suppression des cotisations chômages et maladie
Zone 4 : net à payer et net imposable
Montant net à payer avant impôt sur le revenu et montant de l'impôt sur le revenu prélevé à la source
Zone 5 : montant net social
Montant du revenu net après déduction de l’ensemble des prélèvements sociaux obligatoires.
Zone 6 : impôt sur le revenu
Montant net imposable servant de base au calcul du prélèvement à la source
Cumul annuel des montants nets imposables servant de base au calcul du prélèvement à la source
Montant de l'impôt sur le revenu prélevé à la source
Cumul annuel des montants de l'impôt sur le revenu prélevé à la source
Montant net des heures complémentaire et/ou supplémentaire exonérées
Cumul annuel des montant d'heures complémentaire et/ou supplémentaire exonérées
Zone 7 : mentions finales
Mention de la rubrique dédiée au bulletin de paie sur le portail www.service-public.fr, rubrique cotisations salariales
Mention incitant le salarié à conserver le bulletin de paie sans limitation de durée
En cas d'activité partielle, nombre d'heures indemnisées
```

### PAYSLIPDELIVERY

Selected https://entreprendre.service-public.gouv.fr/vosdroits/F559; PAYSLIPDELIVERY; https://entreprendre.service-public.gouv.fr/vosdroits/F559; read2026-10-29; nativeLF105–110; readerSHA256 `1ec936d34e56a20c42e49c2c96da2cad88eaa33475e4c39a85f8311c9931cc1a`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Depuis 2017, la dématérialisation de la fiche de paie est devenue le principe et le format papier l'exception, sauf en cas de désaccord du salarié.
Pour la remise de la fiche de paie électronique, l'employeur doit indiquer au salarié les conditions dans lesquelles la fiche de paie est disponible. Le salarié peut refuser de recevoir sa fiche de paie de manière dématérialisée. Il le signale à l'employeur.
L'employeur doit conserver dans les locaux de l'entreprise un double de la fiche de paie (sous forme papier ou électronique) pendant une durée de 5 ans.
Au-delà de ces 5 années, les fiches de paie peuvent ne pas être accessibles directement dans l’entreprise (bien qu’elles ne doivent pas pour autant être effacées). Si c'est le cas, l'employeur doit garantir au salarié la disponibilité de ses fiches de paie :
soit pendant une durée de 50 ans à compter de son émission
soit pendant 6 ans après le départ à la retraite du salarié.
```

### PAYSLIPCHALLENGE

Selected https://entreprendre.service-public.gouv.fr/vosdroits/F559; PAYSLIPCHALLENGE; https://entreprendre.service-public.gouv.fr/vosdroits/F559; read2026-10-29; nativeLF158–159; readerSHA256 `1ec936d34e56a20c42e49c2c96da2cad88eaa33475e4c39a85f8311c9931cc1a`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Le salarié peut contester le montant ou l'exactitude de sa fiche de paie pendant 3 ans à compter de sa remise.
À savoir
```

### PAYSLIPDUP

Selected https://entreprendre.service-public.gouv.fr/vosdroits/F559; PAYSLIPDUP; https://entreprendre.service-public.gouv.fr/vosdroits/F559; read2026-10-29; nativeLF116–116; readerSHA256 `1ec936d34e56a20c42e49c2c96da2cad88eaa33475e4c39a85f8311c9931cc1a`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Le salarié qui a perdu sa fiche de paie peut demander un double à l'employeur, mais aucune disposition légale n'oblige l'employeur à le transmettre.
```

### R133MONTH

Selected Official selected indexed/web display: Article R133-14 - Code de la sécurité sociale - Légifrance; R133MONTH; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000039222527; read2026-10-29; nativeLF40–40; readerSHA256 `9fcb58cddc7e31d855846680e75c9c28303b35f9f4be6ff9799fd7ffe8ab273f`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
I. – La déclaration sociale nominative mentionnée au I de l'article L. 133-5-3 est adressée chaque mois au plus tard aux dates mentionnées à l'article R. 243-6.
```

### R243QUARTER

Selected Official selected indexed/web display: Article R243-6-1 - Code de la sécurité sociale - Légifrance; R243QUARTER; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038681470; read2026-10-29; nativeLF19–25; readerSHA256 `c3851bbd7f8789cf0e290989913150d00d3e4ae95a240b1020f048fd023024e9`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Sous réserve des dispositions de l'article R. 243-7, et à l'exception des employeurs mentionnés aux 1°, 2°, 3° et 4° de l'article L. 133-5-6 qui utilisent un dispositif simplifié de déclaration et de recouvrement des cotisations et contributions sociales l'employeur dont l'effectif est de moins de onze salariés peut opter pour le versement trimestriel des cotisations afin de verser les cotisations dues au titre des périodes de travail d'un trimestre civil dans les quinze premiers jours du trimestre civil suivant.

Lorsqu'il entend opter pour ce versement trimestriel, l'employeur en informe par écrit l'organisme de recouvrement dont dépend son établissement avant le 31 décembre ou au moment de l'emploi de son premier salarié.

A défaut de renonciation par l'employeur au plus tard le 31 décembre, elle est reconduite pour l'année suivante.

L'employeur reste tenu d'adresser la déclaration sociale nominative à la date prévue au 2° du II de l'article R. 243-6.
```

### DSNDATE

Selected Official selected indexed/web display: Déclarer en DSN - Urssaf.fr; DSNDATE; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html; read2026-10-29; nativeLF86–95; readerSHA256 `b3338e62164cc0c170ad3b3fcb2cc1df19d86ad9d0cf137d57ab71c2cd7d6daa`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
vous devez transmettre votre DSN liée à la paie du mois en cours, le 5 du mois suivant (M+1).

##### Exemple

Une entreprise de 52 salariés qui paie les salaires d'avril 2026 le 28 avril 2026 devra transmettre la DSN le 5 mai 2026.

Votre paie est effectuée au cours du mois suivant la période travaillée :
vous devez transmettre votre DSN liée à la paie du mois en cours, au plus tard le 15 du mois civil suivant.

##### Exemple
```

### DSNNEXTDAY

Selected Official selected indexed/web display: Déclarer en DSN - Urssaf.fr; DSNNEXTDAY; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html; read2026-10-29; nativeLF107–107; readerSHA256 `b3338e62164cc0c170ad3b3fcb2cc1df19d86ad9d0cf137d57ab71c2cd7d6daa`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Si le délai fixé pour effectuer votre DSN expire un jour férié ou non ouvré, il est prolongé jusqu’au jour ouvrable suivant.
```

### DSNEVENTS

Selected Official selected indexed/web display: Conditions générales d’utilisation de net-entreprises.fr - net-entreprises.fr; DSNEVENTS; https://www.net-entreprises.fr/declaration/mentions-legales/; read2026-10-29; nativeLF375–377; readerSHA256 `2258c0e20a595ad34442338ae40a2f0453f702be9f0392c7fd0782346abb96ce`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Transmettre un signalement dans les 5 jours ouvrés suivant leur connaissance, à savoir : arrêt de travail (en l’absence de subrogation), reprise anticipée après arrêt, ou fin de contrat de travail.
Des cas de dispense sont possibles (vous devez vous référer aux conditions prévues).  | Vous dispenser d’adresser le signalement relatif à l’arrêt de travail dans les 5 jours si vous pratiquez la subrogation ou bien le décalage de la prise en compte en paie d’une absence maladie.
Vous dispenser d’adresser le signalement relatif à la reprise du travail si la date réelle n’est pas antérieure à la date prévisionnelle transmise dans l’arrêt de travail.
```

### DSNCORRECT

Selected Official selected indexed/web display: Déclarer en DSN - Urssaf.fr; DSNCORRECT; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html; read2026-10-29; nativeLF127–133; readerSHA256 `b3338e62164cc0c170ad3b3fcb2cc1df19d86ad9d0cf137d57ab71c2cd7d6daa`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Vous avez fait une erreur sur votre DSN ? Si vous corrigez les rémunérations lors de l'échéance déclarative la plus proche, tout en versant le complément de cotisations et de contributions sociales, alors le droit à l'erreur s'applique. Vous ne serez pas sanctionné.

En pratique, les majorations de retard et la pénalité ne sont pas appliquées si :

  * le montant des majorations et pénalités qui seraient applicables est inférieur à la valeur mensuelle du plafond de la Sécurité sociale ou le versement régularisateur est inférieur à 5 % du montant total des cotisations initiales ;
  * les inexactitudes n’ont pas un caractère « répétitif ».

```

### DSNOMISSION

Selected Official selected indexed/web display: Déclarer en DSN - Urssaf.fr; DSNOMISSION; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html; read2026-10-29; nativeLF158–162; readerSHA256 `b3338e62164cc0c170ad3b3fcb2cc1df19d86ad9d0cf137d57ab71c2cd7d6daa`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
    * omission de salariés ou assimilés : 1,5 % du plafond mensuel de la Sécurité sociale par salarié et par mois ou fraction de mois de retard.
Montant plafonné à 150 % PMSS par entreprise si défaut de production inférieur ou égal à 5 jours. Plafonnement une fois par année civile maximum.
La pénalité est calculée en fonction de l’effectif connu ou transmis lors de votre dernière déclaration ;
    * autres cas : 0,5 % du plafond mensuel de la Sécurité sociale par salarié ou pour les données d’identification de l’employeur.
Pénalité non applicable en cas de régularisation de votre part dans les 30 jours suivant la transmission de la déclaration portant les données omises.
```

### DSNINACCURATE

Selected Official selected indexed/web display: Déclarer en DSN - Urssaf.fr; DSNINACCURATE; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html; read2026-10-29; nativeLF170–172; readerSHA256 `b3338e62164cc0c170ad3b3fcb2cc1df19d86ad9d0cf137d57ab71c2cd7d6daa`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
    * inexactitude des rémunérations déclarées ayant pour effet de minorer le montant des cotisations dues : 1 % du plafond mensuel de la Sécurité sociale par salarié ou assimilé ;
    * autres cas : 0,33 % du plafond mensuel de la Sécurité sociale par salarié ou pour vos données d’identification.
Pénalité non applicable en cas de régularisation de votre part dans les 30 jours suivant la transmission de la déclaration portant les données inexactes.
```

### DSNCRM

Selected Official selected indexed/web display: Déclarer en DSN - Urssaf.fr; DSNCRM; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html; read2026-10-29; nativeLF196–196; readerSHA256 `b3338e62164cc0c170ad3b3fcb2cc1df19d86ad9d0cf137d57ab71c2cd7d6daa`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
L’Urssaf effectue des contrôles automatiques. En cas d’anomalie, vous êtes informé rapidement via un compte-rendu métier (CRM) et le service Suivi DSN, afin de corriger votre déclaration.
```

### DSNCAP

Selected Official selected indexed/web display: Déclarer en DSN - Urssaf.fr; DSNCAP; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html; read2026-10-29; nativeLF141–144; readerSHA256 `b3338e62164cc0c170ad3b3fcb2cc1df19d86ad9d0cf137d57ab71c2cd7d6daa`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
    * pour les entreprises relevant du champ de la DSN en application du décret du 24 septembre 2014 fixant les seuils de l’obligation anticipée d’effectuer la DSN :
      * montant plafonné à 10 000 € si vous employez au moins 2 000 salariés ;
      * montant plafonné à 750 € par entreprise si vous employez un nombre inférieur à 2 000 salariés ;
    * pour les entreprises relevant du champ de la DSN en application du décret du 18 mai 2016 fixant les dates limites pour la transmission obligatoire de la déclaration sociale nominative : montant plafonné à 750 € par entreprise et par mois.
```

### PASEXCLUSIVE

Selected https://bofip.impots.gouv.fr/bofip/11471-PGP.html; PASEXCLUSIVE; https://bofip.impots.gouv.fr/bofip/11471-PGP.html; read2026-10-29; nativeLF84–87; readerSHA256 `0373e989f70f4fc21944c2734b4aea14e3cf1ccf5569e543af13c011bebcaa43`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Les différentes amendes prévues par l'article 1759-0 A du CGI sont exclusives les unes des autres. Il ne peut donc pas y avoir de cumul entre elles.
L'amende de 10 % n'a vocation à s'appliquer que lorsque le collecteur n'a déposé aucune déclaration (DSN ou PASRAU) ou l'a déposée tardivement.
Dans l'hypothèse où un collecteur ne déposerait qu'une partie de sa déclaration dans les délais, ce dernier se verra appliquer la seule sanction de 5 % pour la partie déposée hors délais et non celle de 10 % pour non-dépôt de la déclaration.
Dans l'hypothèse où l'administration relèverait une omission ou une inexactitude sur une déclaration tardive, seule l'amende de 10 % s'appliquera à l’ensemble des retenues non déclarées dans les délais.
```

### PASDELIBERATE

Selected https://bofip.impots.gouv.fr/bofip/11471-PGP.html; PASDELIBERATE; https://bofip.impots.gouv.fr/bofip/11471-PGP.html; read2026-10-29; nativeLF78–78; readerSHA256 `0373e989f70f4fc21944c2734b4aea14e3cf1ccf5569e543af13c011bebcaa43`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Remarque : Les amendes de 40 % pour inexactitudes ou omissions et de 80 % pour rétention ne peuvent être appliquées que si l'administration établit le caractère délibéré de l'infraction (III § 30 à 50 du BOI-CF-INF-10-20-20).
```

### DADS

Selected Official indexed selected original-language display; DADS; https://www.net-entreprises.fr/media/documentation/guide-utilisateur/dsn-guide-dadsu.pdf; read2026-10-29; nativeLF3–12; readerSHA256 `a19e385c31e8afa8d116e69ede35531ba20a2581614956d1004b44109842b566`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Quel est le principe général ?La DSN étant généralisée et considérée comme le seul canal de transmission des données par défaut
pour tous les employeurs du secteur privé, vous ne devrez pas produire de DADS-U en janvier 2020
concernant les salaires 2019.Le dépôt d’une DADSU sera autorisé uniquement pour les cas particuliers suivants :○  Les établissements entrés en DSN employant des populations hors périmètre DSN
○  Les établissements non soumis à l’obligation DSN
○  La transmission des éléments annuels des populations exclues de ce traitement en DSN
   (fonctionnaires …)
○  Les établissements entrés en DSN n’ayant pas été en capacité de transmettre les données des
   organismes complémentaires en DSNComment corriger ou régulariser les  
données ?Il relève de la responsabilité du déclarant de se mettre en capacité de transmettre et/ou régulariser
l’ensemble de ses transmissions/données, via la DSN, sans que le dépôt d’une DADS-U ne puisse être utilisé
```

### INDEX

Selected https://entreprendre.service-public.gouv.fr/vosdroits/F35103; INDEX; https://entreprendre.service-public.gouv.fr/vosdroits/F35103; read2026-10-29; nativeLF100–100; readerSHA256 `c77a0f9b44e56e098ea2bfce32e0ee89d4c65eb71dab686b3e2a86c35cc68c81`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
L'index de l'égalité professionnelle est un outil visant à calculer les écarts de rémunération entre les femmes et les hommes dans l'entreprise. Il est obligatoire pour toute entreprise présentant au moins 50 salariés au cours de l’année écoulée. Il doit être publié chaque année, au plus tard le 1er mars.
```

### INDEXTRANS

Selected https://entreprendre.service-public.gouv.fr/vosdroits/F35103; INDEXTRANS; https://entreprendre.service-public.gouv.fr/vosdroits/F35103; read2026-10-29; nativeLF119–119; readerSHA256 `c77a0f9b44e56e098ea2bfce32e0ee89d4c65eb71dab686b3e2a86c35cc68c81`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Une entreprise de moins de 50 salariés dont l'effectif atteint 50 salariés a 3 ans pour déclarer l'index de l'égalité professionnelle.
```

### INDEXPUBLISH

Selected https://entreprendre.service-public.gouv.fr/vosdroits/F35103; INDEXPUBLISH; https://entreprendre.service-public.gouv.fr/vosdroits/F35103; read2026-10-29; nativeLF160–170; readerSHA256 `c77a0f9b44e56e098ea2bfce32e0ee89d4c65eb71dab686b3e2a86c35cc68c81`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Toutes les entreprises d'au moins 50 salariés doivent publier les résultats obtenus lors du calcul de l'index sur Égapro. Cette publication doit avoir lieu chaque année, au plus tard le 1er mars.
L'ensemble des informations est ainsi transmis aux services du ministre chargé du travail.
Calculer et déclarer l'index de l'égalité professionnelle Égapro
À savoir
L'entreprise qui ne déclare pas son index de l'égalité professionnelle peut être sanctionnée.
La sanction peut atteindre 1 % des rémunérations et gains versés aux travailleurs salariés ou assimilés au cours de la période où l'entreprise n'a pas respecté cette obligation.
Intégration de l'index à la BDESE et au site internet de l'entreprise
L'index de l'égalité professionnelle et les résultats de chacun de ses indicateurs doivent être intégrés à la base de données économiques, sociales et environnementales (BDESE) afin d'être mis à disposition du comité social et économique (CSE).
Les résultats sont présentés par catégorie socio-professionnelle, niveau ou coefficient hiérarchique ou selon les niveaux de la méthode de cotation des postes de l'entreprise. Toutes les précisions utiles à la compréhension doivent accompagner cette publication, notamment concernant la méthodologie appliquée.
Les indicateurs ne pouvant pas être calculés doivent également être intégrés. Ils doivent alors être accompagnés de toutes les précisions expliquant les raisons pour lesquelles les indicateurs n'ont pas pu être calculés.
L'index et les résultats obtenus à chaque indicateur doivent également être publiés sur le site internet de l'entreprise, au plus tard le 1er mars de chaque année. Cette publication doit être visible et lisible.
```

### BILAN

Selected Official indexed selected original-language display; BILAN; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072050/LEGISCTA000035609798/2026-06-14/; read2026-10-29; nativeLF10–11; readerSHA256 `91e51aca80d100825e73be95743517dc994d0ff114258adb2cfbc3e5d0d2ef6a`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Dans les entreprises et organismes mentionnés au premier alinéa de l'article L. 2311-1 ainsi que dans les entreprises mentionnées à l'article L. 2312-35, la consultation sur la politique sociale de l'entreprise, les conditions de travail et l'emploi prévue au 3° de l'article L. 2312-17 porte, en outre, sur le bilan social de l'entreprise lorsque l'entreprise compte au moins trois cents salariés. A cette fin, l'employeur met à la disposition du comité social et économique, dans les conditions prévues par l'accord mentionné à l'article L. 2312-21 ou à défaut d'accord au sous-paragraphe 4, les données relatives à ce bilan social.
Dans les entreprises comportant des établissements distincts, le comité social et économique d'établissement est consulté sur le bilan social particulier à chaque établissement dont l'effectif est au moins de trois cents salariés.
```

### BILANTRANS

Selected Official indexed selected original-language display; BILANTRANS; https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072050/LEGISCTA000035609798/2026-06-14/; read2026-10-29; nativeLF21–23; readerSHA256 `91e51aca80d100825e73be95743517dc994d0ff114258adb2cfbc3e5d0d2ef6a`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Lorsque l'effectif de l'entreprise ou de l'établissement atteint le seuil d'assujettissement de trois cents salariés conformément aux dispositions de l'article L. 2312-34, le premier bilan social de l'entreprise ou de l'établissement porte sur l'année suivant celle au cours de laquelle le seuil a été atteint.
Le premier bilan social peut ne concerner que l'année écoulée. Le deuxième bilan peut ne concerner que les deux dernières années écoulées.
Lorsque l'effectif de l'entreprise ou de l'établissement devient inférieur au seuil d'assujettissement de trois cents salariés, un bilan social est néanmoins présenté pour l'année en cours.
```

### R242MONTH

Selected Official selected indexed/web display: Javascript est desactivé dans votre navigateur.; R242MONTH; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000039222466/2026-03-26; read2026-10-29; nativeLF145–145; readerSHA256 `b0fb776e78ec834fceb04e272887fc64ee4fa764e97ec9581e68bdf83a5f1d16`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Lorsque le contrat de travail d'un salarié ne couvre pas l'intégralité des périodes mentionnées aux deux précédents alinéas, les plafonds mentionnés aux mêmes alinéas sont réduits à due proportion du nombre de jours de la période pendant laquelle les personnes sont employées.
```

### R242PART

CSSR242-2 actual unpaid-absence and part-time/complementary-hours adjustment; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000039222466/2026-03-26; read2026-10-29; nativeLF147–151; readerSHA256 `b0fb776e78ec834fceb04e272887fc64ee4fa764e97ec9581e68bdf83a5f1d16`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Le plafond est également réduit :
– pour tenir compte des périodes d'activités partielles indemnisées dans les conditions fixées à l'article 【37†L. 5122-1】 du code du travail, en cas d'intempéries, indemnisées dans les conditions fixées par les articles 【38†L. 5424-6 et suivants】 du code du travail ainsi que des périodes d'absence pour congés payés, lorsque les indemnités correspondantes sont versées à l'assuré par une caisse de congés payés créée en application de l'article 【39†L. 3141-30】 du même code ;
– pour tenir compte de périodes d'absence n'ayant pas donné lieu à rémunération.
Pour les salariés mentionnés à l'article 【40†L. 3123-1】 du code du travail autres que ceux mentionnés à l'article 【41†L. 242-10】, l'employeur est en droit de corriger le plafond, sans pouvoir augmenter sa valeur mensuelle, à due proportion de la durée de travail inscrite à leur contrat de travail au titre de la période où ils sont présents dans l'entreprise, majorée du nombre d'heures complémentaires au sens des articles 【42†L. 3123-8】, 【43†L. 3123-20, L. 3123-21】 et 【44†L.
3123-28】 du code du travail effectuées au cours de la période mentionnée aux deux premiers alinéas, rapportée à celle correspondant à la plus courte des durées mentionnées au 1° de l'article L. 3123-1 du code du travail.
```

### R242REG

Selected Official selected indexed/web display: Javascript est desactivé dans votre navigateur.; R242REG; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000039222466/2026-03-26; read2026-10-29; nativeLF152–156; readerSHA256 `b0fb776e78ec834fceb04e272887fc64ee4fa764e97ec9581e68bdf83a5f1d16`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
II. – Les cotisations calculées dans la limite d'un plafond annuel sont régularisées chaque mois.

L'employeur fait masse, à chaque échéance de cotisations, des sommes dues au titre des périodes de travail comprises entre cette échéance et le premier jour de l'année ou le jour de l'embauche, si elle est postérieure, et calcule les cotisations sur la partie de cette masse qui ne dépasse pas la somme des plafonds périodiques applicables à ces mêmes périodes.
La différence éventuelle, entre le montant des cotisations ainsi déterminé et le montant de celles qui ont été précédemment versées, fait l'objet d'un versement complémentaire.

```

### CALENDAR

Selected Official selected indexed/web display: Rémunérations soumises à cotisations de retraite complémentaire; CALENDAR; https://reglementation.agirc-arrco.fr/home/liste-fiche-reglementaires/listes-area/liste-de-fiches-reglementaires/remunerations-soumises-a-cotisations-de-retraite-complementaire.html; read2026-10-29; nativeLF6–6; readerSHA256 `c3a7bbe54ba73558497814cb91129aba25cc29095500f9cc01e50d844310bcc2`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Le plafond de la tranche 1 du mois considéré est alors déterminé à due proportion du nombre de jours de la période pendant laquelle le salarié est employé, en tenant compte du nombre de jours calendaires de la période considérée par rapport au nombre de jours que compte le mois.
```

### PCGLIABILITY

Selected ANC PCG January2026, selected account-plan labels; PCGLIABILITY; https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/recueil/2026/Recueil-PCG-Janvier-2026.pdf; read2026-10-29; nativeLF27758–27769; readerSHA256 `6e93de1acbc27475dfbb8dad93292e84972c2f7815fc89a28eca6471d9cc5d17`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
43   Sécurité sociale et autres organismes sociaux
     431     Sécurité sociale
     437     Autres organismes sociaux
     438     Organismes sociaux - Charges à payer
             4382     Charges sociales sur congés à payer
             4386     Autres charges à payer
     439     Organismes sociaux - Produits à recevoir

44   État et autres collectivités publiques
     441      État - Subventions et aides à recevoir
     442      Contributions, impôts et taxes recouvrés pour le compte de l'État
             4421     Prélèvements à la source (Impôt sur le revenu)
```

### PCGEXPENSE

Selected ANC PCG January2026, selected account-plan labels; PCGEXPENSE; https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/recueil/2026/Recueil-PCG-Janvier-2026.pdf; read2026-10-29; nativeLF28110–28128; readerSHA256 `6e93de1acbc27475dfbb8dad93292e84972c2f7815fc89a28eca6471d9cc5d17`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
64   Charges de personnel
     641    Rémunérations du personnel
             6411 Salaires, appointements
             6412 Congés payés
             6413 Primes et gratifications
             6414 Indemnités et avantages divers
             6415 Supplément familial
     644     Rémunération du travail de l'exploitant
     645     Cotisations de sécurité sociale et de prévoyance
             6451 Cotisations à l'Urssaf
             6452 Cotisations aux mutuelles
             6453 Cotisations aux caisses de retraites
             6454 Cotisations à Pôle emploi
             6458 Cotisations aux autres organismes sociaux
     646     Cotisations sociales personnelles de l'exploitant
     647     Autres cotisations sociales
             6471     Prestations directes
             6472     Versements au comité social et économique
             6474     Versements aux autres œuvres sociales
```

### CARSAT

Selected CSS; official URSSAF own table / administrative guidance; CARSAT; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1146–1146; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
 Taux notifié par la Carsat
```

### PPOINTVALUE

Agirc-Arrco2026 T1point rate and20.1877 reference price; https://www.service-public.gouv.fr/particuliers/vosdroits/F15396; read2026-10-29; nativeLF113–115; readerSHA256 `8f294db2acf3a0f568d55465e1e5c61422545d24577a31c195cfd2de2a6543d6`. Actual selected-clause read by writer A, 29 October 2026 Representation: original retained body

```text
Tranche 1 : jusqu'à 48 060 €
6,20 %
20,1877 €
```

### PRIMESCONTRIB

F2301 wage/primes/kind contribution base; https://www.service-public.gouv.fr/telecharger-pdf?path=aHR0cHM6Ly93d3cuc2VydmljZS1wdWJsaWMuZ291di5mci9wYXJ0aWN1bGllcnMvdm9zZHJvaXRzL0YyMzAxP2xhbmc9ZW4%3D; read2026-10-29; nativeLF3–3; readerSHA256 `21cec525b0f93bcc759b878e9d68f465496275775b1bd923754637d367697f4b`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Pour le calcul des cotisations sociales, toutes les sommes suivantes versées au salarié font partie de la rémunération : Salaires ou gains Indemnités de congés payés Indemnités, primes, gratifications et tous autres avantages en argent Avantages en nature, les commissions et les pourboires. 
```

### SICKLAW

Selected Actual selected official indexed display, not whole acquired PDF/law body; SICKLAW; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043356754; read2026-10-29; nativeLF48–48; readerSHA256 `17410dc5ff148a3861d7cd8759a52475718e6a4bd01767445480eaa80fd1ceb8`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Pour l'application des dispositions qui précèdent, il est tenu compte du revenu d'activité antérieur servant de base, lors de chaque paie, au calcul de la cotisation due pour les risques maladie, maternité, invalidité et décès dans la limite d'un plafond égal à 1,4 fois le salaire minimum de croissance en vigueur le dernier jour du mois civil précédant celui de l'interruption de travail et calculé pour un mois sur l'ensemble des revenus, et sur la base de la durée légale du travail. Toutefois, lorsque l'assiette des cotisations fait l'objet d'un abattement par application des dispositions des articles R. 242-7 à R. 242-11, il est tenu compte du revenu d'activité antérieur brut perçu par l'assuré, sans abattement, dans la limite du plafond ainsi défini.
```

### PREFILL

Selected Actual selected official indexed display, not whole acquired PDF/law body; PREFILL; https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_integral/Brochure-IR-2026.pdf; read2026-10-29; nativeLF19–19; readerSHA256 `e712eef3672c59c1eba9656e3d4bda56d82bf6ccb36783aeab2c7a45aa0ec7b6`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Le montant imposable des traitements, salaires, indemnités journalières de maladie, maternité ou paternité déclaré par les parties versantes (employeurs, caisses de sécurité sociale) pour l’ensemble de l’année 2025 est prérempli au-dessus des cases 1AJ et 1BJ ou 1AA et 1BA.
```

### PREFILLCORRECT

Selected Actual selected official indexed display, not whole acquired PDF/law body; PREFILLCORRECT; https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_integral/Brochure-IR-2026.pdf; read2026-10-29; nativeLF28–28; readerSHA256 `e712eef3672c59c1eba9656e3d4bda56d82bf6ccb36783aeab2c7a45aa0ec7b6`. Actual selected-clause read by writer A, 29 October 2026 Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Lorsque les montants préremplis sont inexacts, vous devez les rayer et indiquer le montant imposable exact dans les cases 1AJ/1BJ, 1AA/1BA, 1AP/1BP.  
```

### T37_0

Official table/operative selected clause for current Guide LF37; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/plafonds-securite-sociale.html; read2026-10-29; nativeLF1112–1114; readerSHA256 `43a49e769f4c79d8462c47a78c9a4fad51e84d2b88d37693befe0e9eb8b17458`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 2026
 Année
 48 060 €
```

### T71_0

Official table/operative selected clause for current Guide LF71; https://www.service-public.gouv.fr/particuliers/vosdroits/F1419; read2026-10-29; nativeLF87–88; readerSHA256 `47ba2276514f0e7744c51dc863cadc485755cab30bd5f97319e6dcbe4f875c7f`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Jusqu'à 11 600 € 
 0 % 
```

### T72_0

Official table/operative selected clause for current Guide LF72; https://www.service-public.gouv.fr/particuliers/vosdroits/F1419; read2026-10-29; nativeLF89–90; readerSHA256 `47ba2276514f0e7744c51dc863cadc485755cab30bd5f97319e6dcbe4f875c7f`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 De 11 601 € à 29 579 € 
 11 % 
```

### T73_0

Official table/operative selected clause for current Guide LF73; https://www.service-public.gouv.fr/particuliers/vosdroits/F1419; read2026-10-29; nativeLF91–92; readerSHA256 `47ba2276514f0e7744c51dc863cadc485755cab30bd5f97319e6dcbe4f875c7f`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 De 29 580 € à 84 577 € 
 30 % 
```

### T74_0

Official table/operative selected clause for current Guide LF74; https://www.service-public.gouv.fr/particuliers/vosdroits/F1419; read2026-10-29; nativeLF93–94; readerSHA256 `47ba2276514f0e7744c51dc863cadc485755cab30bd5f97319e6dcbe4f875c7f`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 De 84 578 € à 181 917 € 
 41 % 
```

### T75_0

Official table/operative selected clause for current Guide LF75; https://www.service-public.gouv.fr/particuliers/vosdroits/F1419; read2026-10-29; nativeLF95–96; readerSHA256 `47ba2276514f0e7744c51dc863cadc485755cab30bd5f97319e6dcbe4f875c7f`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Plus de 181 917 € 
 45 % 
```

### T86_0

Official table/operative selected clause for current Guide LF86; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF73–74; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Inférieure à 1 635 euros
 0 %
```

### T87_0

Official table/operative selected clause for current Guide LF87; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF75–76; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Supérieure ou égale à 1 635 euros et inférieure à 1 698 euros
 0,5 %
```

### T88_0

Official table/operative selected clause for current Guide LF88; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF77–78; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Supérieure ou égale à 1 698 euros et inférieure à 1 807 euros
 1,3 %
```

### T89_0

Official table/operative selected clause for current Guide LF89; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF79–80; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Supérieure ou égale à 1 807 euros et inférieure à 1 928 euros
 2,1 %
```

### T90_0

Official table/operative selected clause for current Guide LF90; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF81–82; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Supérieure ou égale à 1 928 euros et inférieure à 2 060 euros
 2,9 %
```

### T91_0

Official table/operative selected clause for current Guide LF91; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF83–84; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Supérieure ou égale à 2 060 euros et inférieure à 2 170 euros
 3,5 %
```

### T92_0

Official table/operative selected clause for current Guide LF92; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF85–86; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Supérieure ou égale à 2 170 euros et inférieure à 2 315 euros
 4,1 %
```

### T93_0

Official table/operative selected clause for current Guide LF93; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF87–88; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Supérieure ou égale à 2 315 euros et inférieure à 2 738 euros
 5,3 %
```

### T94_0

Official table/operative selected clause for current Guide LF94; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF89–90; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Supérieure ou égale à 2 738 euros et inférieure à 3 135 euros
 7,5 %
```

### T95_0

Official table/operative selected clause for current Guide LF95; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF91–92; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Supérieure ou égale à 3 135 euros et inférieure à 3 571 euros
 9,9 %
```

### T96_0

Official table/operative selected clause for current Guide LF96; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF93–94; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Supérieure ou égale à 3 571 euros et inférieure à 4 019 euros
 11,9 %
```

### T97_0

Official table/operative selected clause for current Guide LF97; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF95–96; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Supérieure ou égale à 4 019 euros et inférieure à 4 690 euros
 13,8 %
```

### T98_0

Official table/operative selected clause for current Guide LF98; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF97–98; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Supérieure ou égale à 4 690 euros et inférieure à 5 624 euros
 15,8 %
```

### T99_0

Official table/operative selected clause for current Guide LF99; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF99–100; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Supérieure ou égale à 5 624 euros et inférieure à 7 037 euros
 17,9 %
```

### T100_0

Official table/operative selected clause for current Guide LF100; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF101–102; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Supérieure ou égale à 7 037 euros et inférieure à 8 789 euros
 20 %
```

### T101_0

Official table/operative selected clause for current Guide LF101; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF103–104; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Supérieure ou égale à 8 789 euros et inférieure à 12 200 euros
 24 %
```

### T102_0

Official table/operative selected clause for current Guide LF102; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF105–106; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Supérieure ou égale à 12 200 euros et inférieure à 16 523 euros
 28 %
```

### T103_0

Official table/operative selected clause for current Guide LF103; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF107–108; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Supérieure ou égale à 16 523 euros et inférieure à 25 937 euros
 33 %
```

### T104_0

Official table/operative selected clause for current Guide LF104; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF109–110; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Supérieure ou égale à 25 937 euros et inférieure à 55 558 euros
 38 %
```

### T105_0

Official table/operative selected clause for current Guide LF105; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF111–112; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Supérieure ou égale à 55 558 euros
 43 %
```

### T114_0

Official table/operative selected clause for current Guide LF114; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF203–203; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Le montant mensuel net imposable du salaire minimum de croissance s’élève, au 1 er juin 2026, à 1 531,12 euros. Par suite, le montant de l’abattement applicable aux contrats courts en vigueur à compter de cette même date est égal à 766 euros (1 531,12 / 2).
```

### T115_0

Official table/operative selected clause for current Guide LF115; https://bofip.impots.gouv.fr/bofip/11255-PGP.html; read2026-10-29; nativeLF203–203; readerSHA256 `aca48b06a7306d40c3fba8b460cd4d192f0c6bcd6e23bf9b4a684a883c17b298`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Le montant mensuel net imposable du salaire minimum de croissance s’élève, au 1 er juin 2026, à 1 531,12 euros. Par suite, le montant de l’abattement applicable aux contrats courts en vigueur à compter de cette même date est égal à 766 euros (1 531,12 / 2).
```

### T126_0

Official table/operative selected clause for current Guide LF126; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1194–1195; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Assurance vieillesse 
 0,40 % sur la totalité et 6,90 % dans la limite du plafond
```

### T127_0

Official table/operative selected clause for current Guide LF127; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1195–1195; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 0,40 % sur la totalité et 6,90 % dans la limite du plafond
```

### T128_0

Official table/operative selected clause for current Guide LF128; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1198–1199; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 CSG non imposable 
 6,80 % sur 98,25 % du salaire brut dans la limite de 192 240 € en 2026
```

### T129_0

Official table/operative selected clause for current Guide LF129; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1196–1197; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 CSG imposable 
 2,40 % sur 98,25 % du salaire brut dans la limite de 192 240 € en 2026
```

### T130_0

Official table/operative selected clause for current Guide LF130; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1200–1201; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 CRDS 
 0,50 % sur 98,25 % du salaire brut dans la limite de 192 240 € en 2026
```

### T131_0

Official table/operative selected clause for current Guide LF131; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-particuliers.html; read2026-10-29; nativeLF286–286; readerSHA256 `ddc8dee15df0872c2ecbc595c6c4b30595febd51d866836699789bdf3cde0ccc`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Cotisation salariale maladie supplémentaire pour les départements du Haut-Rhin, Bas-Rhin et de la Moselle  | 1,30 %
```

### T140_0

Official table/operative selected clause for current Guide LF140; https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/csg-crds.html; read2026-10-29; nativeLF87–90; readerSHA256 `7dfc62b0ca19222b2edbfbc7c187436d4fc369a79bd2dda59ea856972f69ce6e`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Concernant les revenus d’activité, ce taux est de :

  * 9,20 % pour la CSG ;
  * 0,50 % pour la CRDS.
```

### T141_0

Official table/operative selected clause for current Guide LF141; https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/csg-crds.html; read2026-10-29; nativeLF89–90; readerSHA256 `7dfc62b0ca19222b2edbfbc7c187436d4fc369a79bd2dda59ea856972f69ce6e`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
  * 9,20 % pour la CSG ;
  * 0,50 % pour la CRDS.
```

### T142_0

Official table/operative selected clause for current Guide LF142; https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/csg-crds.html; read2026-10-29; nativeLF92–92; readerSHA256 `7dfc62b0ca19222b2edbfbc7c187436d4fc369a79bd2dda59ea856972f69ce6e`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Quant à la base, elle est généralement réduite de 1,75 % au titre des frais professionnels.
```

### T143_0

Official table/operative selected clause for current Guide LF143; https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/csg-crds.html; read2026-10-29; nativeLF94–94; readerSHA256 `7dfc62b0ca19222b2edbfbc7c187436d4fc369a79bd2dda59ea856972f69ce6e`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Autrement dit, les CSG-CRDS sont calculées sur 98,25 % des revenus d’activité qui sont soumis à ces contributions.
```

### T144_0

Official table/operative selected clause for current Guide LF144; https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/csg-crds.html; read2026-10-29; nativeLF104–104; readerSHA256 `7dfc62b0ca19222b2edbfbc7c187436d4fc369a79bd2dda59ea856972f69ce6e`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
La réduction de 1,75 % ne s’applique toutefois que dans la limite de 4 plafonds annuels de la Sécurité sociale.
```

### T145_0

Official table/operative selected clause for current Guide LF145; https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/csg-crds.html; read2026-10-29; nativeLF66–66; readerSHA256 `7dfc62b0ca19222b2edbfbc7c187436d4fc369a79bd2dda59ea856972f69ce6e`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Cette cotisation, au taux de 5,50 %, est à déclarer à l'aide du code type de personnel (CTP) 206.
```

### T154_0

Official table/operative selected clause for current Guide LF154; https://www.service-public.gouv.fr/particuliers/vosdroits/F15396; read2026-10-29; nativeLF103–103; readerSHA256 `8f294db2acf3a0f568d55465e1e5c61422545d24577a31c195cfd2de2a6543d6`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
7,87 % (part salariale : 3,15 % / part patronale : 4,72 %)
```

### T155_0

Official table/operative selected clause for current Guide LF155; https://www.service-public.gouv.fr/particuliers/vosdroits/F15396; read2026-10-29; nativeLF105–105; readerSHA256 `8f294db2acf3a0f568d55465e1e5c61422545d24577a31c195cfd2de2a6543d6`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
21,59 % (part salariale : 8,64 % / part patronale : 12,95 %)
```

### T156_0

Official table/operative selected clause for current Guide LF156; https://www.service-public.gouv.fr/particuliers/vosdroits/F15396; read2026-10-29; nativeLF103–103; readerSHA256 `8f294db2acf3a0f568d55465e1e5c61422545d24577a31c195cfd2de2a6543d6`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
7,87 % (part salariale : 3,15 % / part patronale : 4,72 %)
```

### T157_0

Official table/operative selected clause for current Guide LF157; https://www.service-public.gouv.fr/particuliers/vosdroits/F15396; read2026-10-29; nativeLF105–105; readerSHA256 `8f294db2acf3a0f568d55465e1e5c61422545d24577a31c195cfd2de2a6543d6`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
21,59 % (part salariale : 8,64 % / part patronale : 12,95 %)
```

### T158_0

Official table/operative selected clause for current Guide LF158; https://www.service-public.gouv.fr/particuliers/vosdroits/F15396; read2026-10-29; nativeLF113–115; readerSHA256 `8f294db2acf3a0f568d55465e1e5c61422545d24577a31c195cfd2de2a6543d6`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Tranche 1 : jusqu'à 48 060 €
6,20 %
20,1877 €
```

### T159_0

Official table/operative selected clause for current Guide LF159; https://www.service-public.gouv.fr/particuliers/vosdroits/F15396; read2026-10-29; nativeLF116–117; readerSHA256 `8f294db2acf3a0f568d55465e1e5c61422545d24577a31c195cfd2de2a6543d6`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Tranche 2 : entre 48 060 € et 384 480 €
17 %
```

### T169_0

Official table/operative selected clause for current Guide LF169; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-particuliers.html; read2026-10-29; nativeLF293–293; readerSHA256 `ddc8dee15df0872c2ecbc595c6c4b30595febd51d866836699789bdf3cde0ccc`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Contribution d'équilibre générale (CEG) tranche 1^{(3)}  | 0,86 % dans la limite du plafond
```

### T170_0

Official table/operative selected clause for current Guide LF170; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-particuliers.html; read2026-10-29; nativeLF316–316; readerSHA256 `ddc8dee15df0872c2ecbc595c6c4b30595febd51d866836699789bdf3cde0ccc`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
CEG tranche 2 : 1,08 % part salariale et 1,62 % en part patronale.
```

### T171_0

Official table/operative selected clause for current Guide LF171; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-particuliers.html; read2026-10-29; nativeLF317–317; readerSHA256 `ddc8dee15df0872c2ecbc595c6c4b30595febd51d866836699789bdf3cde0ccc`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
La CET (contribution d’équilibre technique) s’applique à tous les salariés dont la rémunération est supérieure au plafond de la Sécurité sociale et dès le 1^{er} euro. Part salariale à 0,14 % et part patronale à 0,21 %.
```

### T188_0

Official table/operative selected clause for current Guide LF188; https://www.service-public.gouv.fr/particuliers/vosdroits/F2391; read2026-10-29; nativeLF198–198; readerSHA256 `261857ea17b01f9b14e6c61fafe479ca64379019cd58a9a66b4710db9a55a71c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Les heures supplémentaires effectuées sont exonérées des cotisations salariales d'assurance vieillesse de base et complémentaire dans la limite de 11,31 % du salaire.
```

### T189_0

Official table/operative selected clause for current Guide LF189; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/exonerations-heures/reduction-cotisations-salariales.html; read2026-10-29; nativeLF87–87; readerSHA256 `d6cd9e5a4b17580843e31437c01934ec3b91bae2930244f49a65f8ecc0f0f6ac`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
  * 7,30 % (cotisations salariales vieillesse dont 0,40 % sur la totalité de la rémunération et 6,90 % dans la limite du plafond) ;
```

### T190_0

Official table/operative selected clause for current Guide LF190; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/exonerations-heures/reduction-cotisations-salariales.html; read2026-10-29; nativeLF88–88; readerSHA256 `d6cd9e5a4b17580843e31437c01934ec3b91bae2930244f49a65f8ecc0f0f6ac`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
  * 3,15 % (cotisations salariales de retraite complémentaire sur la tranche 1 (= plafond)) ;
```

### T191_0

Official table/operative selected clause for current Guide LF191; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/exonerations-heures/reduction-cotisations-salariales.html; read2026-10-29; nativeLF89–89; readerSHA256 `d6cd9e5a4b17580843e31437c01934ec3b91bae2930244f49a65f8ecc0f0f6ac`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
  * 0,86 % (contribution d’équilibre général (CEG) sur la tranche 1 (= plafond)).
```

### T202_0

Official table/operative selected clause for current Guide LF202; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1113–1114; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Taux réduit à 7 %
 Taux plein à 13 %
```

### T203_0

Official table/operative selected clause for current Guide LF203; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1113–1114; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Taux réduit à 7 %
 Taux plein à 13 %
```

### T204_0

Official table/operative selected clause for current Guide LF204; https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html; read2026-10-29; nativeLF91–91; readerSHA256 `565c80d230c5c770d3c1ed7b7596c5a380826e335d6ce25a7c68bd301e9fdc9b`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Pour les employeurs concernés bénéficiant d’exonérations spécifiques citées ci-dessus, le taux de la cotisation d’assurance maladie sera de 7 % si la rémunération annuelle du salarié est inférieure ou égale à 2,5 fois le Smic en vigueur au 31/12/2023. Au-delà de cette limite, le taux de la cotisation d’assurance maladie applicable sera de 13 %.
```

### T205_0

Official table/operative selected clause for current Guide LF205; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1115–1116; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Contribution solidarité autonomie (CSA)
 0,30 %
```

### T206_0

Official table/operative selected clause for current Guide LF206; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1117–1118; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Assurance vieillesse
 2,11 % sur la totalité et 8,55 % dans la limite du plafond
```

### T207_0

Official table/operative selected clause for current Guide LF207; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1118–1118; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 2,11 % sur la totalité et 8,55 % dans la limite du plafond
```

### T208_0

Official table/operative selected clause for current Guide LF208; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1119–1121; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Allocations familiales
 Taux réduit à 3,45 %
 Taux plein à 5,25 %
```

### T209_0

Official table/operative selected clause for current Guide LF209; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1120–1121; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Taux réduit à 3,45 %
 Taux plein à 5,25 %
```

### T210_0

Official table/operative selected clause for current Guide LF210; https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html; read2026-10-29; nativeLF99–99; readerSHA256 `565c80d230c5c770d3c1ed7b7596c5a380826e335d6ce25a7c68bd301e9fdc9b`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Pour les employeurs concernés bénéficiant d’exonérations spécifiques citées ci-dessus, le taux de la cotisation d’allocations familiales sera de 3,45 % si la rémunération annuelle du salarié est inférieure ou égale à 3,5 fois le Smic en vigueur au 31/12/2023. Au-delà de cette limite, le taux de la cotisation d’allocations familiales sera de 5,25 %.
```

### T211_0

Official table/operative selected clause for current Guide LF211; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1122–1123; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Contribution au dialogue social
 0,016 %
```

### T212_0

Official table/operative selected clause for current Guide LF212; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1130–1131; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Fnal (effectif de moins de 50 salariés)
 0,10 % dans la limite du plafond
```

### T213_0

Official table/operative selected clause for current Guide LF213; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1132–1133; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Fnal (effectif de 50 salariés et plus)
 0,50 %
```

### T214_0

Official table/operative selected clause for current Guide LF214; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1135–1135; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Pour une entreprise de moins de 11 salariés : 0,55 %
```

### T215_0

Official table/operative selected clause for current Guide LF215; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1136–1136; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Pour une entreprise de 11 salariés et plus : 1 %
```

### T216_0

Official table/operative selected clause for current Guide LF216; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1137–1138; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Contribution CPF-CDD
 1 %
```

### T217_0

Official table/operative selected clause for current Guide LF217; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1139–1141; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Taxe d'apprentissage
 Part principale à 0,59 %
 Solde à 0,09 %
```

### T218_0

Official table/operative selected clause for current Guide LF218; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1140–1141; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Part principale à 0,59 %
 Solde à 0,09 %
```

### T219_0

Official table/operative selected clause for current Guide LF219; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1143–1144; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Part principale à 0,44 %
 Solde - Néant
```

### T220_0

Official table/operative selected clause for current Guide LF220; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1145–1146; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Accident du travail
 Taux notifié par la Carsat
```

### T221_0

Official table/operative selected clause for current Guide LF221; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1147–1147; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Versement mobilité (effectif de 11 salariés et plus)
```

### T234_0

Official table/operative selected clause for current Guide LF234; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html; read2026-10-29; nativeLF43–44; readerSHA256 `91b41f59cde469dd2de147527b948d449d53f48df61ec32f5210c9623176e389`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
  * a une rémunération inférieure :
    * à 3 Smic applicable au 1^{er} janvier 2026 (ou 2,9293 Smic applicable au 1^{er} juin 2026) en métropole et dans les Drom (hors Mayotte) ;
```

### T235_0

Official table/operative selected clause for current Guide LF235; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html; read2026-10-29; nativeLF44–44; readerSHA256 `91b41f59cde469dd2de147527b948d449d53f48df61ec32f5210c9623176e389`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
    * à 3 Smic applicable au 1^{er} janvier 2026 (ou 2,9293 Smic applicable au 1^{er} juin 2026) en métropole et dans les Drom (hors Mayotte) ;
```

### T236_0

Official table/operative selected clause for current Guide LF236; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html; read2026-10-29; nativeLF130–130; readerSHA256 `91b41f59cde469dd2de147527b948d449d53f48df61ec32f5210c9623176e389`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
En 2026, la valeur du Smic à prendre en compte est celle en vigueur au 1^{er} janvier 2026.
```

### T237_0

Official table/operative selected clause for current Guide LF237; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html; read2026-10-29; nativeLF145–145; readerSHA256 `91b41f59cde469dd2de147527b948d449d53f48df61ec32f5210c9623176e389`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Pour un Smic brut mensuel de 1 867,02 € au 1^{er} juin 2026 et une rémunération mensuelle brute de 2 000 €, la valeur maximale du coefficient de réduction générale est de 0,3178.
```

### T238_0

Official table/operative selected clause for current Guide LF238; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html; read2026-10-29; nativeLF45–45; readerSHA256 `91b41f59cde469dd2de147527b948d449d53f48df61ec32f5210c9623176e389`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
    * à 1,6 Smic applicable à Mayotte en 2026 ;
```

### T239_0

Official table/operative selected clause for current Guide LF239; https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html; read2026-10-29; nativeLF32–32; readerSHA256 `565c80d230c5c770d3c1ed7b7596c5a380826e335d6ce25a7c68bd301e9fdc9b`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
La RGDU s’applique aux revenus d’activité majorés, le cas échéant, des primes de partage de la valeur (PPV), qui sont inférieurs à 3 Smic en vigueur au lieu de 1,6 Smic auparavant.
```

### T240_0

Official table/operative selected clause for current Guide LF240; https://entreprendre.service-public.gouv.fr/vosdroits/F559; read2026-10-29; nativeLF305–305; readerSHA256 `1ec936d34e56a20c42e49c2c96da2cad88eaa33475e4c39a85f8311c9931cc1a`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Allègements généraux dont bénéficient les employeurs au titre des salariés dont les rémunérations brutes sont inférieures à 1,6 Smic (2 987,23 €).
```

### T241_0

Official table/operative selected clause for current Guide LF241; https://entreprendre.service-public.gouv.fr/vosdroits/F559; read2026-10-29; nativeLF306–306; readerSHA256 `1ec936d34e56a20c42e49c2c96da2cad88eaa33475e4c39a85f8311c9931cc1a`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Réduction du taux de cotisations allocations familiales, dont bénéficient les employeurs au titre des salariés dont les rémunérations brutes sont inférieures à 3,5 Smic (6 534,56 €).
```

### T242_0

Official table/operative selected clause for current Guide LF242; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html; read2026-10-29; nativeLF56–56; readerSHA256 `91b41f59cde469dd2de147527b948d449d53f48df61ec32f5210c9623176e389`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
  * d’assurances sociales (maladie, maternité, invalidité, décès) au taux de 13,00 % ;
```

### T243_0

Official table/operative selected clause for current Guide LF243; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html; read2026-10-29; nativeLF57–57; readerSHA256 `91b41f59cde469dd2de147527b948d449d53f48df61ec32f5210c9623176e389`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
  * de vieillesse au taux de 10,66 % ;
```

### T244_0

Official table/operative selected clause for current Guide LF244; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html; read2026-10-29; nativeLF58–58; readerSHA256 `91b41f59cde469dd2de147527b948d449d53f48df61ec32f5210c9623176e389`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
  * d’allocations familiales au taux de 5,25 % ;
```

### T245_0

Official table/operative selected clause for current Guide LF245; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html; read2026-10-29; nativeLF59–59; readerSHA256 `91b41f59cde469dd2de147527b948d449d53f48df61ec32f5210c9623176e389`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
  * d’accidents du travail et maladies professionnelles (AT-MP) pour sa partie mutualisée au taux de 0,49 % ;
```

### T246_0

Official table/operative selected clause for current Guide LF246; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html; read2026-10-29; nativeLF60–60; readerSHA256 `91b41f59cde469dd2de147527b948d449d53f48df61ec32f5210c9623176e389`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
  * de retraite complémentaire légalement obligatoire (Agirc-Arrco) au taux de 6,01 % ;
```

### T247_0

Official table/operative selected clause for current Guide LF247; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html; read2026-10-29; nativeLF61–61; readerSHA256 `91b41f59cde469dd2de147527b948d449d53f48df61ec32f5210c9623176e389`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
  * de fonds national d’aide au logement (Fnal) au taux de 0,10 % pour les entreprises de moins de 50 salariés ou 0,50 % pour les entreprises de 50 salariés et plus ;
```

### T248_0

Official table/operative selected clause for current Guide LF248; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html; read2026-10-29; nativeLF61–62; readerSHA256 `91b41f59cde469dd2de147527b948d449d53f48df61ec32f5210c9623176e389`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
  * de fonds national d’aide au logement (Fnal) au taux de 0,10 % pour les entreprises de moins de 50 salariés ou 0,50 % pour les entreprises de 50 salariés et plus ;
  * de solidarité pour l’autonomie (CSA) au taux de 0,30 % ;
```

### T249_0

Official table/operative selected clause for current Guide LF249; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html; read2026-10-29; nativeLF62–62; readerSHA256 `91b41f59cde469dd2de147527b948d449d53f48df61ec32f5210c9623176e389`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
  * de solidarité pour l’autonomie (CSA) au taux de 0,30 % ;
```

### T250_0

Official table/operative selected clause for current Guide LF250; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html; read2026-10-29; nativeLF63–63; readerSHA256 `91b41f59cde469dd2de147527b948d449d53f48df61ec32f5210c9623176e389`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
  * d’assurance chômage au taux de 4,00 %.
```

### T273_0

Official table/operative selected clause for current Guide LF273; https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html; read2026-10-29; nativeLF135–135; readerSHA256 `565c80d230c5c770d3c1ed7b7596c5a380826e335d6ce25a7c68bd301e9fdc9b`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
    * 1,50 € pour les employeurs dont l’effectif est inférieur à 20 salariés ;
```

### T274_0

Official table/operative selected clause for current Guide LF274; https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html; read2026-10-29; nativeLF136–136; readerSHA256 `565c80d230c5c770d3c1ed7b7596c5a380826e335d6ce25a7c68bd301e9fdc9b`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
    * 0,50 € par heure supplémentaire pour les employeurs d’au moins 20 salariés et plus.
```

### T283_0

Official table/operative selected clause for current Guide LF283; https://www.service-public.gouv.fr/particuliers/vosdroits/F15396; read2026-10-29; nativeLF103–103; readerSHA256 `8f294db2acf3a0f568d55465e1e5c61422545d24577a31c195cfd2de2a6543d6`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
7,87 % (part salariale : 3,15 % / part patronale : 4,72 %)
```

### T284_0

Official table/operative selected clause for current Guide LF284; https://www.service-public.gouv.fr/particuliers/vosdroits/F15396; read2026-10-29; nativeLF105–105; readerSHA256 `8f294db2acf3a0f568d55465e1e5c61422545d24577a31c195cfd2de2a6543d6`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
21,59 % (part salariale : 8,64 % / part patronale : 12,95 %)
```

### T289_0

Official table/operative selected clause for current Guide LF289; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-particuliers.html; read2026-10-29; nativeLF260–260; readerSHA256 `ddc8dee15df0872c2ecbc595c6c4b30595febd51d866836699789bdf3cde0ccc`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Contribution d'équilibre générale (CEG) tranche 1^{(3)}  | 1,29 % dans la limite du plafond
```

### T290_0

Official table/operative selected clause for current Guide LF290; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-particuliers.html; read2026-10-29; nativeLF316–316; readerSHA256 `ddc8dee15df0872c2ecbc595c6c4b30595febd51d866836699789bdf3cde0ccc`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
CEG tranche 2 : 1,08 % part salariale et 1,62 % en part patronale.
```

### T291_0

Official table/operative selected clause for current Guide LF291; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-particuliers.html; read2026-10-29; nativeLF317–317; readerSHA256 `ddc8dee15df0872c2ecbc595c6c4b30595febd51d866836699789bdf3cde0ccc`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
La CET (contribution d’équilibre technique) s’applique à tous les salariés dont la rémunération est supérieure au plafond de la Sécurité sociale et dès le 1^{er} euro. Part salariale à 0,14 % et part patronale à 0,21 %.
```

### T292_0

Official table/operative selected clause for current Guide LF292; https://entreprendre.service-public.gouv.fr/vosdroits/F24013; read2026-10-29; nativeLF126–126; readerSHA256 `76f212ae2e2f5004cf0ab510ac1fb0908f8c0811ed3afd801557736d2860bea2`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Cotisation de retraite complémentaire (obligatoire), qui est reversée aux caisses Arrco (pour tous les salariés cadres et non-cadres du secteur privé) et Agirc (en supplément pour le personnel cadre), avec les taux suivants : 60 % par l'employeur et 40 % par le salarié
```

### T293_0

Official table/operative selected clause for current Guide LF293; https://entreprendre.service-public.gouv.fr/vosdroits/F24013; read2026-10-29; nativeLF126–126; readerSHA256 `76f212ae2e2f5004cf0ab510ac1fb0908f8c0811ed3afd801557736d2860bea2`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Cotisation de retraite complémentaire (obligatoire), qui est reversée aux caisses Arrco (pour tous les salariés cadres et non-cadres du secteur privé) et Agirc (en supplément pour le personnel cadre), avec les taux suivants : 60 % par l'employeur et 40 % par le salarié
```

### T304_0

Official table/operative selected clause for current Guide LF304; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1124–1125; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Contribution assurance chômage
 4,00 % dans la limite de 192 240 € en 2026
```

### T305_0

Official table/operative selected clause for current Guide LF305; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1127–1127; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Dans la limite de 192 240 € en 2026 :
```

### T306_0

Official table/operative selected clause for current Guide LF306; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1127–1128; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 Dans la limite de 192 240 € en 2026 :
 0,25 %
```

### T307_0

Official table/operative selected clause for current Guide LF307; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html; read2026-10-29; nativeLF1129–1129; readerSHA256 `8f8c0bdd94bd0e24cc74545f911793e37495e7c7db16cf14a93451c632639b72`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
 0,03 % pour les entreprises de travail temporaire
```

### T312_0

Official table/operative selected clause for current Guide LF312; https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html; read2026-10-29; nativeLF155–155; readerSHA256 `565c80d230c5c770d3c1ed7b7596c5a380826e335d6ce25a7c68bd301e9fdc9b`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Le taux de cette contribution patronale passe de 30 % à 40 % à compter de la période d’emploi de janvier 2026.
```

### T329_0

Official table/operative selected clause for current Guide LF329; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/montant-smic.html; read2026-10-29; nativeLF24–24; readerSHA256 `67255c339b8d7ddbfcbe32f162b1c96b67cf41b7d7c363af3eb5ea965228dad6`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Smic horaire brut  | 12,02 €  | 12,31 €
```

### T330_0

Official table/operative selected clause for current Guide LF330; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/montant-smic.html; read2026-10-29; nativeLF27–30; readerSHA256 `67255c339b8d7ddbfcbe32f162b1c96b67cf41b7d7c363af3eb5ea965228dad6`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
 | Du 1^{er} janvier 2026 au 31 mai 2026
--- | ---
Smic horaire brut  | 12,02 €
Smic brut mensuel (base 35 heures par semaine)  | 1 823,03 €
```

### T331_0

Official table/operative selected clause for current Guide LF331; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/montant-smic.html; read2026-10-29; nativeLF24–24; readerSHA256 `67255c339b8d7ddbfcbe32f162b1c96b67cf41b7d7c363af3eb5ea965228dad6`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Smic horaire brut  | 12,02 €  | 12,31 €
```

### T332_0

Official table/operative selected clause for current Guide LF332; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/montant-smic.html; read2026-10-29; nativeLF32–35; readerSHA256 `67255c339b8d7ddbfcbe32f162b1c96b67cf41b7d7c363af3eb5ea965228dad6`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
 | Au 1^{er} juin 2026
--- | ---
Smic horaire brut  | 12,31 €
Smic brut mensuel (base 35 heures par semaine)  | 1 867,02 €
```

### T333_0

Official table/operative selected clause for current Guide LF333; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/montant-smic.html; read2026-10-29; nativeLF42–42; readerSHA256 `67255c339b8d7ddbfcbe32f162b1c96b67cf41b7d7c363af3eb5ea965228dad6`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Smic horaire brut  | 10,82 €  | 11,08 €
```

### T334_0

Official table/operative selected clause for current Guide LF334; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/montant-smic.html; read2026-10-29; nativeLF60–60; readerSHA256 `67255c339b8d7ddbfcbe32f162b1c96b67cf41b7d7c363af3eb5ea965228dad6`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Smic horaire brut  | 9,62 €  | 9,85 €
```

### T339_0

Official table/operative selected clause for current Guide LF339; https://www.urssaf.fr/accueil/actualites/augmentation-smic.html; read2026-10-29; nativeLF23–23; readerSHA256 `2f90ca41e4d8d7d874162855cf7bc4d119527dc8d62605e09149ae999de270e8`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
À Mayotte, le Smic horaire brut est porté à 9,56 € soit un montant mensuel brut de 1 449,93 € sur la base de la durée légale du travail de 35 heures hebdomadaires.
```

### T340_0

Official table/operative selected clause for current Guide LF340; https://www.urssaf.fr/accueil/actualites/augmentation-smic.html; read2026-10-29; nativeLF25–25; readerSHA256 `2f90ca41e4d8d7d874162855cf7bc4d119527dc8d62605e09149ae999de270e8`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Le minimum garanti s'établit à 4,35 €.
```

### T351_0

Official table/operative selected clause for current Guide LF351; https://www.service-public.gouv.fr/particuliers/vosdroits/F1911; read2026-10-29; nativeLF95–95; readerSHA256 `44f04e7087f6d573887b75b4fd33c975de664eb9eec806f65d76bff0ccaeafa2`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
35 heures par semaine: titleContent
```

### T352_0

Official table/operative selected clause for current Guide LF352; https://www.service-public.gouv.fr/particuliers/vosdroits/F1911; read2026-10-29; nativeLF96–96; readerSHA256 `44f04e7087f6d573887b75b4fd33c975de664eb9eec806f65d76bff0ccaeafa2`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
151,67 heures par mois
```

### T353_0

Official table/operative selected clause for current Guide LF353; https://www.service-public.gouv.fr/particuliers/vosdroits/F1911; read2026-10-29; nativeLF97–97; readerSHA256 `44f04e7087f6d573887b75b4fd33c975de664eb9eec806f65d76bff0ccaeafa2`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
1 607 heures par an.
```

### T354_0

Official table/operative selected clause for current Guide LF354; https://www.service-public.gouv.fr/particuliers/vosdroits/F1911; read2026-10-29; nativeLF109–109; readerSHA256 `44f04e7087f6d573887b75b4fd33c975de664eb9eec806f65d76bff0ccaeafa2`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
La durée de travail effectif: titleContent ne doit pas dépasser la durée maximale de 10 heures par jour.
```

### T355_0

Official table/operative selected clause for current Guide LF355; https://www.service-public.gouv.fr/particuliers/vosdroits/F1911; read2026-10-29; nativeLF113–113; readerSHA256 `44f04e7087f6d573887b75b4fd33c975de664eb9eec806f65d76bff0ccaeafa2`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Soit si une convention collective: titleContent le prévoit. En cas d'activité accrue ou pour des motifs liés à l'organisation de l'entreprise, la durée maximale quotidienne de travail est limitée à 12 heures par jour de travail effectif.
```

### T356_0

Official table/operative selected clause for current Guide LF356; https://www.service-public.gouv.fr/particuliers/vosdroits/F1911; read2026-10-29; nativeLF118–118; readerSHA256 `44f04e7087f6d573887b75b4fd33c975de664eb9eec806f65d76bff0ccaeafa2`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Soit 48 heures sur une même semaine
```

### T357_0

Official table/operative selected clause for current Guide LF357; https://www.service-public.gouv.fr/particuliers/vosdroits/F1911; read2026-10-29; nativeLF119–119; readerSHA256 `44f04e7087f6d573887b75b4fd33c975de664eb9eec806f65d76bff0ccaeafa2`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Soit 44 heures par semaine en moyenne sur une période de 12 semaines consécutives.
```

### T362_0

Official table/operative selected clause for current Guide LF362; https://www.service-public.gouv.fr/particuliers/vosdroits/F2391; read2026-10-29; nativeLF147–147; readerSHA256 `261857ea17b01f9b14e6c61fafe479ca64379019cd58a9a66b4710db9a55a71c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
25 % pour les 8 premières heures supplémentaires travaillées dans la même semaine (de la 36e à la 43e heure)
```

### T363_0

Official table/operative selected clause for current Guide LF363; https://www.service-public.gouv.fr/particuliers/vosdroits/F2391; read2026-10-29; nativeLF148–148; readerSHA256 `261857ea17b01f9b14e6c61fafe479ca64379019cd58a9a66b4710db9a55a71c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
50 % pour les heures suivantes (à partir de la 44e heure)
```

### T364_0

Official table/operative selected clause for current Guide LF364; https://www.service-public.gouv.fr/particuliers/vosdroits/F2391; read2026-10-29; nativeLF137–137; readerSHA256 `261857ea17b01f9b14e6c61fafe479ca64379019cd58a9a66b4710db9a55a71c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Chaque taux est au minimum fixé à 10 %.
```

### T365_0

Official table/operative selected clause for current Guide LF365; https://www.service-public.gouv.fr/particuliers/vosdroits/F2391; read2026-10-29; nativeLF220–220; readerSHA256 `261857ea17b01f9b14e6c61fafe479ca64379019cd58a9a66b4710db9a55a71c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Soit 10 % pour chaque heure complémentaire accomplie dans la limite de 1/10e de la durée de travail fixé dans le contrat
```

### T366_0

Official table/operative selected clause for current Guide LF366; https://www.service-public.gouv.fr/particuliers/vosdroits/F2391; read2026-10-29; nativeLF221–221; readerSHA256 `261857ea17b01f9b14e6c61fafe479ca64379019cd58a9a66b4710db9a55a71c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Soit 25 % pour chaque heure accomplie au-delà de 1/10e (et dans la limite de 1/3)
```

### T367_0

Official table/operative selected clause for current Guide LF367; https://www.service-public.gouv.fr/particuliers/vosdroits/F2391; read2026-10-29; nativeLF121–121; readerSHA256 `261857ea17b01f9b14e6c61fafe479ca64379019cd58a9a66b4710db9a55a71c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Si aucun de ces 3 accords n'existe dans l'entreprise, le nombre maximal d'heures supplémentaires est de 220 heures par salarié et par an.
```

### T378_0

Official table/operative selected clause for current Guide LF378; https://www.service-public.gouv.fr/particuliers/vosdroits/F2258; read2026-10-29; nativeLF87–87; readerSHA256 `2f2a69d967d21ca2deef3d2cfbd08ab9651d90fbc9a0f9cf71c2868ab7069ee0`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Le salarié a droit à des congés payés. Chaque mois de travail effectif: titleContent ouvre droit à un congé de 2,5 jours ouvrables: titleContent, sauf cas particulier. Pendant les congés, l’employeur verse au salarié une indemnité de congés payés. Nous vous présentons les informations à connaître.
```

### T379_0

Official table/operative selected clause for current Guide LF379; https://www.service-public.gouv.fr/particuliers/vosdroits/F2258; read2026-10-29; nativeLF100–100; readerSHA256 `2f2a69d967d21ca2deef3d2cfbd08ab9651d90fbc9a0f9cf71c2868ab7069ee0`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Cela correspond à 30 jours ouvrables (5 semaines) pour une année complète de travail.
```

### T381_0

Official table/operative selected clause for current Guide LF381; https://www.service-public.gouv.fr/particuliers/vosdroits/F2258; read2026-10-29; nativeLF232–232; readerSHA256 `2f2a69d967d21ca2deef3d2cfbd08ab9651d90fbc9a0f9cf71c2868ab7069ee0`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Lorsque le salarié est en arrêt de travail pendant toute la période d'acquisition des congés (période dite de référence du 1er juin de l'année N-1 au 31 mai de l'année N), le point de départ du délai du report de 15 mois est fixé à la fin de cette période.
```

### T382_0

Official table/operative selected clause for current Guide LF382; https://www.service-public.gouv.fr/particuliers/vosdroits/F2258; read2026-10-29; nativeLF179–179; readerSHA256 `2f2a69d967d21ca2deef3d2cfbd08ab9651d90fbc9a0f9cf71c2868ab7069ee0`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Oui, le congé principal (soit 4 semaines consécutives maximum) peut ne pas être pris dans son intégralité durant la période légale de prise de congés (du 1er mai au 31 octobre de l'année en cours).
```

### T392_0

Official table/operative selected clause for current Guide LF392; https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; read2026-10-29; nativeLF130–130; readerSHA256 `0b86b2957a0c12bcfc52bf23f74098f379cb098bf9b30243347015dffd70a60f`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Les indemnités journalières (IJ) sont égales à 50 % du salaire journalier de base.
```

### T393_0

Official table/operative selected clause for current Guide LF393; https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; read2026-10-29; nativeLF131–131; readerSHA256 `0b86b2957a0c12bcfc52bf23f74098f379cb098bf9b30243347015dffd70a60f`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Si vous êtes payé au mois, votre salaire journalier de base est égal au total des 3 derniers salaires bruts perçus avant l'arrêt de travail, divisé par 91,25.
```

### T394_0

Official table/operative selected clause for current Guide LF394; https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; read2026-10-29; nativeLF138–138; readerSHA256 `0b86b2957a0c12bcfc52bf23f74098f379cb098bf9b30243347015dffd70a60f`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Votre salaire pris en compte pour calculer votre gain journalier de base, est plafonné à 1,4 fois le montant du Smic en vigueur, lors du dernier jour du mois qui précède l'arrêt (soit 2 613,82 € par mois en 2026).
```

### T395_0

Official table/operative selected clause for current Guide LF395; https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; read2026-10-29; nativeLF143–143; readerSHA256 `0b86b2957a0c12bcfc52bf23f74098f379cb098bf9b30243347015dffd70a60f`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Pour les arrêts ayant débuté avant le 1ᵉʳ avril 2025, l’ancien plafond reste applicable : le salaire pris en compte pour le calcul du gain journalier de base est plafonné à 1,8 fois le montant du Smic en vigueur, lors du dernier jour du mois qui précède l'arrêt.
```

### T396_0

Official table/operative selected clause for current Guide LF396; https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; read2026-10-29; nativeLF137–137; readerSHA256 `0b86b2957a0c12bcfc52bf23f74098f379cb098bf9b30243347015dffd70a60f`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Les IJ ne peuvent pas dépasser 42,97 € bruts.
```

### T406_0

Official table/operative selected clause for current Guide LF406; https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; read2026-10-29; nativeLF207–208; readerSHA256 `0b86b2957a0c12bcfc52bf23f74098f379cb098bf9b30243347015dffd70a60f`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
De 1 à 5 ans
60 jours (30 jours à 90 % et 30 jours à 66,66 %)
```

### T407_0

Official table/operative selected clause for current Guide LF407; https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; read2026-10-29; nativeLF209–210; readerSHA256 `0b86b2957a0c12bcfc52bf23f74098f379cb098bf9b30243347015dffd70a60f`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
De 6 à 10 ans
80 jours (40 jours à 90 % et 40 jours à 66,66 %)
```

### T408_0

Official table/operative selected clause for current Guide LF408; https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; read2026-10-29; nativeLF211–212; readerSHA256 `0b86b2957a0c12bcfc52bf23f74098f379cb098bf9b30243347015dffd70a60f`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
De 11 à 15 ans
100 jours (50 jours à 90 % et 50 jours à 66,66 %)
```

### T409_0

Official table/operative selected clause for current Guide LF409; https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; read2026-10-29; nativeLF213–214; readerSHA256 `0b86b2957a0c12bcfc52bf23f74098f379cb098bf9b30243347015dffd70a60f`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
De 16 à 20 ans
120 jours (60 jours à 90 % et 60 jours à 66,66 %)
```

### T410_0

Official table/operative selected clause for current Guide LF410; https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; read2026-10-29; nativeLF215–216; readerSHA256 `0b86b2957a0c12bcfc52bf23f74098f379cb098bf9b30243347015dffd70a60f`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
De 21 à 25 ans
140 jours (70 jours à 90 % et 70 jours à 66,66 %)
```

### T411_0

Official table/operative selected clause for current Guide LF411; https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; read2026-10-29; nativeLF217–218; readerSHA256 `0b86b2957a0c12bcfc52bf23f74098f379cb098bf9b30243347015dffd70a60f`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
De 26 à 30 ans
160 jours (80 jours à 90 % et 80 jours à 66,66 %)
```

### T412_0

Official table/operative selected clause for current Guide LF412; https://www.service-public.gouv.fr/particuliers/vosdroits/F3053; read2026-10-29; nativeLF219–220; readerSHA256 `0b86b2957a0c12bcfc52bf23f74098f379cb098bf9b30243347015dffd70a60f`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
31 ans et plus
180 jours (90 jours à 90 % et 90 jours à 66,66 %)
```

### T413_0

Official table/operative selected clause for current Guide LF413; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000019225874/2026-03-07; read2026-10-29; nativeLF18–18; readerSHA256 `3dc5167f3a120a657ec7756bce70b1ce7759a51c58172cfc00e0a18b9a582fff`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Toutefois, dans tous les autres cas, le délai d'indemnisation court au-delà de sept jours d'absence.
```

### T413_1

Official table/operative selected clause for current Guide LF413; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000019225874/2026-03-07; read2026-10-29; nativeLF16–16; readerSHA256 `3dc5167f3a120a657ec7756bce70b1ce7759a51c58172cfc00e0a18b9a582fff`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Lors de chaque arrêt de travail, les durées d'indemnisation courent à compter du premier jour d'absence si celle-ci est consécutive à un accident du travail ou à une maladie professionnelle, à l'exclusion des accidents de trajet.
```

### T422_0

Official table/operative selected clause for current Guide LF422; https://www.service-public.gouv.fr/particuliers/vosdroits/F2265; read2026-10-29; nativeLF119–122; readerSHA256 `2ded1aba372608f34bf664c592123bf9fce595b1eb1b275ab08931d585e50bd9`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
1er enfant
6 semaines
10 semaines
16 semaines
```

### T423_0

Official table/operative selected clause for current Guide LF423; https://www.service-public.gouv.fr/particuliers/vosdroits/F2265; read2026-10-29; nativeLF123–126; readerSHA256 `2ded1aba372608f34bf664c592123bf9fce595b1eb1b275ab08931d585e50bd9`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
2e enfant
6 semaines
10 semaines
16 semaines
```

### T424_0

Official table/operative selected clause for current Guide LF424; https://www.service-public.gouv.fr/particuliers/vosdroits/F2265; read2026-10-29; nativeLF127–130; readerSHA256 `2ded1aba372608f34bf664c592123bf9fce595b1eb1b275ab08931d585e50bd9`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
3e enfant ou plus
8 semaines
18 semaines
26 semaines
```

### T425_0

Official table/operative selected clause for current Guide LF425; https://www.service-public.gouv.fr/particuliers/vosdroits/F2265; read2026-10-29; nativeLF141–144; readerSHA256 `2ded1aba372608f34bf664c592123bf9fce595b1eb1b275ab08931d585e50bd9`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
2
12 semaines
22 semaines
34 semaines
```

### T426_0

Official table/operative selected clause for current Guide LF426; https://www.service-public.gouv.fr/particuliers/vosdroits/F2265; read2026-10-29; nativeLF145–148; readerSHA256 `2ded1aba372608f34bf664c592123bf9fce595b1eb1b275ab08931d585e50bd9`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
3 ou plus
24 semaines
22 semaines
46 semaines
```

### T435_0

Official table/operative selected clause for current Guide LF435; https://www.service-public.gouv.fr/particuliers/vosdroits/F3156; read2026-10-29; nativeLF102–102; readerSHA256 `ff172456cc952a865b582d6faf81aedd021bbf26bf6245ea5f0e15bd7674de3e`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Le congé de paternité et d'accueil de l'enfant est obligatoirement précédé du congé de naissance d'une durée de 3 jours ouvrables: titleContent.
```

### T436_0

Official table/operative selected clause for current Guide LF436; https://www.service-public.gouv.fr/particuliers/vosdroits/F3156; read2026-10-29; nativeLF103–103; readerSHA256 `ff172456cc952a865b582d6faf81aedd021bbf26bf6245ea5f0e15bd7674de3e`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
La durée du congé de paternité et d'accueil de l'enfant est de 25 jours calendaires: titleContent.
```

### T437_0

Official table/operative selected clause for current Guide LF437; https://www.service-public.gouv.fr/particuliers/vosdroits/F3156; read2026-10-29; nativeLF126–126; readerSHA256 `ff172456cc952a865b582d6faf81aedd021bbf26bf6245ea5f0e15bd7674de3e`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
La durée du congé de paternité et d'accueil de l'enfant est de 32 jours calendaires: titleContent.
```

### T438_0

Official table/operative selected clause for current Guide LF438; https://www.service-public.gouv.fr/particuliers/vosdroits/F3156; read2026-10-29; nativeLF107–107; readerSHA256 `ff172456cc952a865b582d6faf81aedd021bbf26bf6245ea5f0e15bd7674de3e`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Immédiatement après le congé de naissance, il doit prendre la 1re période de 4 jours calendaires: titleContent de son congé de paternité et d'accueil de l'enfant.
```

### T451_0

Official table/operative selected clause for current Guide LF451; https://entreprendre.service-public.gouv.fr/vosdroits/F33754; read2026-10-29; nativeLF126–126; readerSHA256 `50413f1995dc2bd279f48c73f071771fffcc172dea0d7aeb97c682e97e7a1ac7`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
La participation financière de l'employeur doit être au moins égale à 50 % de la cotisation (le reste à la charge du salarié)
```

### T452_0

Official table/operative selected clause for current Guide LF452; https://entreprendre.service-public.gouv.fr/vosdroits/F33754; read2026-10-29; nativeLF140–140; readerSHA256 `50413f1995dc2bd279f48c73f071771fffcc172dea0d7aeb97c682e97e7a1ac7`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Frais dentaires (prothèses et orthodontie) à hauteur de 125 % du tarif conventionnel: titleContent
```

### T463_0

Official table/operative selected clause for current Guide LF463; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html; read2026-10-29; nativeLF35–37; readerSHA256 `9037c17dbb86a65ccbe214cbd9477a338d0e4db2f06b9e592d53942a1a19259c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Nombre de repas  | Montant de l'avantage en 2026
--- | ---
1 repas  | 5,50 €
```

### T464_0

Official table/operative selected clause for current Guide LF464; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html; read2026-10-29; nativeLF38–38; readerSHA256 `9037c17dbb86a65ccbe214cbd9477a338d0e4db2f06b9e592d53942a1a19259c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
2 repas  | 11,00 €
```

### T465_0

Official table/operative selected clause for current Guide LF465; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html; read2026-10-29; nativeLF72–72; readerSHA256 `9037c17dbb86a65ccbe214cbd9477a338d0e4db2f06b9e592d53942a1a19259c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Exonération maximale de la part patronale  | 7,32 €
```

### T466_0

Official table/operative selected clause for current Guide LF466; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html; read2026-10-29; nativeLF73–73; readerSHA256 `9037c17dbb86a65ccbe214cbd9477a338d0e4db2f06b9e592d53942a1a19259c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Valeur du titre restaurant ouvrant droit à l’exonération maximale  | Entre 12,20 € et 14,64 €
```

### T467_0

Official table/operative selected clause for current Guide LF467; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html; read2026-10-29; nativeLF73–73; readerSHA256 `9037c17dbb86a65ccbe214cbd9477a338d0e4db2f06b9e592d53942a1a19259c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Valeur du titre restaurant ouvrant droit à l’exonération maximale  | Entre 12,20 € et 14,64 €
```

### T468_0

Official table/operative selected clause for current Guide LF468; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html; read2026-10-29; nativeLF161–161; readerSHA256 `9037c17dbb86a65ccbe214cbd9477a338d0e4db2f06b9e592d53942a1a19259c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Véhicule acheté âgé de 5 ans ou moins  | 15 % du coût d'achat
```

### T469_0

Official table/operative selected clause for current Guide LF469; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html; read2026-10-29; nativeLF167–167; readerSHA256 `9037c17dbb86a65ccbe214cbd9477a338d0e4db2f06b9e592d53942a1a19259c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Véhicule acheté âgé de 5 ans ou moins  | 15 % du coût d'achat + frais réels sur factures de carburant utilisé à des fins personnelles ou 20 % du coût d'achat
```

### T470_0

Official table/operative selected clause for current Guide LF470; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html; read2026-10-29; nativeLF162–162; readerSHA256 `9037c17dbb86a65ccbe214cbd9477a338d0e4db2f06b9e592d53942a1a19259c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Véhicule acheté de plus de 5 ans  | 10 % du coût d'achat
```

### T471_0

Official table/operative selected clause for current Guide LF471; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html; read2026-10-29; nativeLF168–168; readerSHA256 `9037c17dbb86a65ccbe214cbd9477a338d0e4db2f06b9e592d53942a1a19259c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Véhicule acheté de plus de 5 ans  |  10 % du coût d'achat + frais réels sur factures de carburant utilisé à des fins personnelles ou 15 % du coût d'achat
```

### T472_0

Official table/operative selected clause for current Guide LF472; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html; read2026-10-29; nativeLF163–163; readerSHA256 `9037c17dbb86a65ccbe214cbd9477a338d0e4db2f06b9e592d53942a1a19259c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Véhicule loué ou en location avec option d’achat (LOA)  | 50 % du coût global annuel (location, entretien, assurance)
```

### T473_0

Official table/operative selected clause for current Guide LF473; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html; read2026-10-29; nativeLF169–169; readerSHA256 `9037c17dbb86a65ccbe214cbd9477a338d0e4db2f06b9e592d53942a1a19259c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Véhicule loué ou en location avec option d’achat (LOA)  | 50 % du coût global annuel (location, entretien, assurance) + frais réels sur factures de carburant utilisé à des fins personnelles ou 67 % du coût global (location, entretien, assurance, carburant utilisé à titre privé et professionnel et toutes les taxes afférentes)
```

### T474_0

Official table/operative selected clause for current Guide LF474; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html; read2026-10-29; nativeLF189–189; readerSHA256 `9037c17dbb86a65ccbe214cbd9477a338d0e4db2f06b9e592d53942a1a19259c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Véhicule acheté âgé de 5 ans ou moins  | 9 % du coût d'achat
```

### T475_0

Official table/operative selected clause for current Guide LF475; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html; read2026-10-29; nativeLF195–195; readerSHA256 `9037c17dbb86a65ccbe214cbd9477a338d0e4db2f06b9e592d53942a1a19259c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Véhicule acheté âgé de 5 ans ou moins  | 9 % du coût d'achat + frais réels sur factures de carburant utilisé à des fins personnelles ou 12 % du coût d'achat
```

### T476_0

Official table/operative selected clause for current Guide LF476; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html; read2026-10-29; nativeLF190–190; readerSHA256 `9037c17dbb86a65ccbe214cbd9477a338d0e4db2f06b9e592d53942a1a19259c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Véhicule acheté de plus de 5 ans  | 6 % du coût d'achat
```

### T477_0

Official table/operative selected clause for current Guide LF477; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html; read2026-10-29; nativeLF196–196; readerSHA256 `9037c17dbb86a65ccbe214cbd9477a338d0e4db2f06b9e592d53942a1a19259c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Véhicule acheté de plus de 5 ans  | 6 % du coût d'achat + frais réels sur factures de carburant utilisé à des fins personnelles ou 9 % du coût d'achat
```

### T478_0

Official table/operative selected clause for current Guide LF478; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html; read2026-10-29; nativeLF191–191; readerSHA256 `9037c17dbb86a65ccbe214cbd9477a338d0e4db2f06b9e592d53942a1a19259c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Véhicule loué ou en location avec option d’achat (LOA)  | 30 % du coût global annuel TTC (location, entretien, assurance)
```

### T479_0

Official table/operative selected clause for current Guide LF479; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html; read2026-10-29; nativeLF197–197; readerSHA256 `9037c17dbb86a65ccbe214cbd9477a338d0e4db2f06b9e592d53942a1a19259c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Véhicule loué ou en location avec option d’achat (LOA)  | 30 % du coût global annuel TTC (location, entretien, assurance) + frais de carburant sur facture o u 4 0 % du coût global
```

### T480_0

Official table/operative selected clause for current Guide LF480; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html; read2026-10-29; nativeLF171–171; readerSHA256 `9037c17dbb86a65ccbe214cbd9477a338d0e4db2f06b9e592d53942a1a19259c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
L'avantage évalué pour un véhicule loué est plafonné au montant de l'avantage en nature qui aurait été évalué si l'employeur avait acheté le véhicule. Le prix de référence du véhicule retenu correspond à son prix d'achat TTC par le loueur, rabais compris dans la limite de 30 % du prix conseillé par le constructeur à la date de début du contrat.
```

### T481_0

Official table/operative selected clause for current Guide LF481; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html; read2026-10-29; nativeLF175–175; readerSHA256 `9037c17dbb86a65ccbe214cbd9477a338d0e4db2f06b9e592d53942a1a19259c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
  * Si le véhicule respecte le score environnemental requis pour bénéficier du bonus écologique, vous utilisez le barème ci-dessus auquel vous appliquez une réduction de 70 % sur le montant de l’avantage en nature, dans la limite de 4 641,60 € par an en 2026 ;
```

### T482_0

Official table/operative selected clause for current Guide LF482; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html; read2026-10-29; nativeLF203–203; readerSHA256 `9037c17dbb86a65ccbe214cbd9477a338d0e4db2f06b9e592d53942a1a19259c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
  * Vous utilisez le barème ci-dessus auquel vous appliquez une réduction de 50 %, dans la limite de 2 026,30 € par an en 2026 ;
```

### T483_0

Official table/operative selected clause for current Guide LF483; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html; read2026-10-29; nativeLF176–176; readerSHA256 `9037c17dbb86a65ccbe214cbd9477a338d0e4db2f06b9e592d53942a1a19259c`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
  * Les frais d'électricité pris en charge par l’employeur n’entrent pas en compte dans le calcul de l’avantage en nature.
```

### T488_0

Official table/operative selected clause for current Guide LF488; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/frais-professionnels.html; read2026-10-29; nativeLF37–37; readerSHA256 `2f95557a1778591113fbc0039ac414b3afdbc9661b974826bc4890e315a0d021`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Salarié contraint de prendre son repas sur le lieu de travail  | 7,50 €
```

### T489_0

Official table/operative selected clause for current Guide LF489; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/frais-professionnels.html; read2026-10-29; nativeLF38–38; readerSHA256 `2f95557a1778591113fbc0039ac414b3afdbc9661b974826bc4890e315a0d021`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Salarié en situation de déplacement contraint de prendre son repas au restaurant  | 21,40 €
```

### T490_0

Official table/operative selected clause for current Guide LF490; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/frais-professionnels.html; read2026-10-29; nativeLF39–39; readerSHA256 `2f95557a1778591113fbc0039ac414b3afdbc9661b974826bc4890e315a0d021`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Salarié en situation de déplacement non contraint de prendre son repas au restaurant  | 10,40 €
```

### T491_0

Official table/operative selected clause for current Guide LF491; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/frais-professionnels.html; read2026-10-29; nativeLF276–276; readerSHA256 `2f95557a1778591113fbc0039ac414b3afdbc9661b974826bc4890e315a0d021`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Par jour de télétravail  | 2,70 € dans la limite de 59,40 € par mois
```

### T492_0

Official table/operative selected clause for current Guide LF492; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/frais-professionnels.html; read2026-10-29; nativeLF276–276; readerSHA256 `2f95557a1778591113fbc0039ac414b3afdbc9661b974826bc4890e315a0d021`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Par jour de télétravail  | 2,70 € dans la limite de 59,40 € par mois
```

### T493_0

Official table/operative selected clause for current Guide LF493; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/frais-professionnels.html; read2026-10-29; nativeLF289–289; readerSHA256 `2f95557a1778591113fbc0039ac414b3afdbc9661b974826bc4890e315a0d021`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Par jour de télétravail  | 3,30 € dans la limite de 72,60 € par mois
```

### T494_0

Official table/operative selected clause for current Guide LF494; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/frais-professionnels.html; read2026-10-29; nativeLF289–289; readerSHA256 `2f95557a1778591113fbc0039ac414b3afdbc9661b974826bc4890e315a0d021`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Par jour de télétravail  | 3,30 € dans la limite de 72,60 € par mois
```

### T499_0

Official table/operative selected clause for current Guide LF499; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/prime-partage-valeur.html; read2026-10-29; nativeLF18–18; readerSHA256 `0fd1801bfc678e9f8f76d7b3c7c83766a4273bc024b142bfc0cc19a099fa01c7`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Depuis le 1er juillet 2022, vous pouvez verser à vos salariés une prime de partage de la valeur (PPV) exonérée de cotisations et contributions sociales dans la limite de 3 000 €. Si un dispositif d’intéressement ou de participation volontaire est mis en place dans votre entreprise, la prime peut être exonérée dans la limite de 6 000 €.
```

### T500_0

Official table/operative selected clause for current Guide LF500; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/prime-partage-valeur.html; read2026-10-29; nativeLF136–136; readerSHA256 `0fd1801bfc678e9f8f76d7b3c7c83766a4273bc024b142bfc0cc19a099fa01c7`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Cette limite d’exonération passe à 6 000 € par bénéficiaire et par an si vous mettez en œuvre :
```

### T501_0

Official table/operative selected clause for current Guide LF501; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/prime-partage-valeur.html; read2026-10-29; nativeLF176–176; readerSHA256 `0fd1801bfc678e9f8f76d7b3c7c83766a4273bc024b142bfc0cc19a099fa01c7`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
De plus, le forfait social au taux de 20 % est dû si l’effectif de votre entreprise est égal ou supérieur à 250 salariés.
```

### T536_0

Official table/operative selected clause for current Guide LF536; https://entreprendre.service-public.gouv.fr/vosdroits/F559; read2026-10-29; nativeLF113–113; readerSHA256 `1ec936d34e56a20c42e49c2c96da2cad88eaa33475e4c39a85f8311c9931cc1a`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
L'employeur peut être condamné à une amende pouvant atteindre 450 € par fiche non remise.
```

### T545_0

Official table/operative selected clause for current Guide LF545; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html; read2026-10-29; nativeLF86–86; readerSHA256 `b3338e62164cc0c170ad3b3fcb2cc1df19d86ad9d0cf137d57ab71c2cd7d6daa`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
vous devez transmettre votre DSN liée à la paie du mois en cours, le 5 du mois suivant (M+1).
```

### T546_0

Official table/operative selected clause for current Guide LF546; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html; read2026-10-29; nativeLF93–93; readerSHA256 `b3338e62164cc0c170ad3b3fcb2cc1df19d86ad9d0cf137d57ab71c2cd7d6daa`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
vous devez transmettre votre DSN liée à la paie du mois en cours, au plus tard le 15 du mois civil suivant.
```

### T547_0

Official table/operative selected clause for current Guide LF547; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html; read2026-10-29; nativeLF93–93; readerSHA256 `b3338e62164cc0c170ad3b3fcb2cc1df19d86ad9d0cf137d57ab71c2cd7d6daa`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
vous devez transmettre votre DSN liée à la paie du mois en cours, au plus tard le 15 du mois civil suivant.
```

### T548_0

Official table/operative selected clause for current Guide LF548; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038681470; read2026-10-29; nativeLF19–19; readerSHA256 `c3851bbd7f8789cf0e290989913150d00d3e4ae95a240b1020f048fd023024e9`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Sous réserve des dispositions de l'article R. 243-7, et à l'exception des employeurs mentionnés aux 1°, 2°, 3° et 4° de l'article L. 133-5-6 qui utilisent un dispositif simplifié de déclaration et de recouvrement des cotisations et contributions sociales l'employeur dont l'effectif est de moins de onze salariés peut opter pour le versement trimestriel des cotisations afin de verser les cotisations dues au titre des périodes de travail d'un trimestre civil dans les quinze premiers jours du trimestre civil suivant.
```

### T548_1

Official table/operative selected clause for current Guide LF548; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038681470; read2026-10-29; nativeLF25–25; readerSHA256 `c3851bbd7f8789cf0e290989913150d00d3e4ae95a240b1020f048fd023024e9`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
L'employeur reste tenu d'adresser la déclaration sociale nominative à la date prévue au 2° du II de l'article R. 243-6.
```

### T549_0

Official table/operative selected clause for current Guide LF549; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html; read2026-10-29; nativeLF107–107; readerSHA256 `b3338e62164cc0c170ad3b3fcb2cc1df19d86ad9d0cf137d57ab71c2cd7d6daa`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Si le délai fixé pour effectuer votre DSN expire un jour férié ou non ouvré, il est prolongé jusqu’au jour ouvrable suivant.
```

### T550_0

Official table/operative selected clause for current Guide LF550; https://www.net-entreprises.fr/declaration/mentions-legales/; read2026-10-29; nativeLF375–375; readerSHA256 `2258c0e20a595ad34442338ae40a2f0453f702be9f0392c7fd0782346abb96ce`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Transmettre un signalement dans les 5 jours ouvrés suivant leur connaissance, à savoir : arrêt de travail (en l’absence de subrogation), reprise anticipée après arrêt, ou fin de contrat de travail.
```

### T559_0

Official table/operative selected clause for current Guide LF559; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html; read2026-10-29; nativeLF139–139; readerSHA256 `b3338e62164cc0c170ad3b3fcb2cc1df19d86ad9d0cf137d57ab71c2cd7d6daa`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
0,5 % du plafond mensuel de la Sécurité sociale (PMSS) par salarié : 
```

### T560_0

Official table/operative selected clause for current Guide LF560; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html; read2026-10-29; nativeLF142–142; readerSHA256 `b3338e62164cc0c170ad3b3fcb2cc1df19d86ad9d0cf137d57ab71c2cd7d6daa`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
      * montant plafonné à 10 000 € si vous employez au moins 2 000 salariés ;
```

### T561_0

Official table/operative selected clause for current Guide LF561; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html; read2026-10-29; nativeLF143–143; readerSHA256 `b3338e62164cc0c170ad3b3fcb2cc1df19d86ad9d0cf137d57ab71c2cd7d6daa`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
      * montant plafonné à 750 € par entreprise si vous employez un nombre inférieur à 2 000 salariés ;
```

### T562_0

Official table/operative selected clause for current Guide LF562; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html; read2026-10-29; nativeLF149–149; readerSHA256 `b3338e62164cc0c170ad3b3fcb2cc1df19d86ad9d0cf137d57ab71c2cd7d6daa`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
1,5 % du plafond mensuel de la Sécurité sociale par salarié et par mois ou fraction de mois de retard.
```

### T563_0

Official table/operative selected clause for current Guide LF563; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html; read2026-10-29; nativeLF150–150; readerSHA256 `b3338e62164cc0c170ad3b3fcb2cc1df19d86ad9d0cf137d57ab71c2cd7d6daa`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Montant plafonné à 150 % PMSS par entreprise si défaut de production inférieur ou égal à 5 jours. Plafonnement une fois par année civile maximum.
```

### T564_0

Official table/operative selected clause for current Guide LF564; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html; read2026-10-29; nativeLF158–158; readerSHA256 `b3338e62164cc0c170ad3b3fcb2cc1df19d86ad9d0cf137d57ab71c2cd7d6daa`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
    * omission de salariés ou assimilés : 1,5 % du plafond mensuel de la Sécurité sociale par salarié et par mois ou fraction de mois de retard.
```

### T564_1

Official table/operative selected clause for current Guide LF564; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html; read2026-10-29; nativeLF150–150; readerSHA256 `b3338e62164cc0c170ad3b3fcb2cc1df19d86ad9d0cf137d57ab71c2cd7d6daa`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
Montant plafonné à 150 % PMSS par entreprise si défaut de production inférieur ou égal à 5 jours. Plafonnement une fois par année civile maximum.
```

### T565_0

Official table/operative selected clause for current Guide LF565; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html; read2026-10-29; nativeLF161–161; readerSHA256 `b3338e62164cc0c170ad3b3fcb2cc1df19d86ad9d0cf137d57ab71c2cd7d6daa`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
    * autres cas : 0,5 % du plafond mensuel de la Sécurité sociale par salarié ou pour les données d’identification de l’employeur.
```

### T566_0

Official table/operative selected clause for current Guide LF566; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html; read2026-10-29; nativeLF170–170; readerSHA256 `b3338e62164cc0c170ad3b3fcb2cc1df19d86ad9d0cf137d57ab71c2cd7d6daa`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
    * inexactitude des rémunérations déclarées ayant pour effet de minorer le montant des cotisations dues : 1 % du plafond mensuel de la Sécurité sociale par salarié ou assimilé ;
```

### T567_0

Official table/operative selected clause for current Guide LF567; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html; read2026-10-29; nativeLF171–171; readerSHA256 `b3338e62164cc0c170ad3b3fcb2cc1df19d86ad9d0cf137d57ab71c2cd7d6daa`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
    * autres cas : 0,33 % du plafond mensuel de la Sécurité sociale par salarié ou pour vos données d’identification.
```

### T568_0

Official table/operative selected clause for current Guide LF568; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html; read2026-10-29; nativeLF131–131; readerSHA256 `b3338e62164cc0c170ad3b3fcb2cc1df19d86ad9d0cf137d57ab71c2cd7d6daa`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: Retained official web-tool/indexed representation; raw artifact is a tool response, not original HTTP body; exact source_identity provenance preserved

```text
  * le montant des majorations et pénalités qui seraient applicables est inférieur à la valeur mensuelle du plafond de la Sécurité sociale ou le versement régularisateur est inférieur à 5 % du montant total des cotisations initiales ;
```

### T581_0

Official table/operative selected clause for current Guide LF581; https://bofip.impots.gouv.fr/bofip/11471-PGP.html; read2026-10-29; nativeLF75–75; readerSHA256 `0373e989f70f4fc21944c2734b4aea14e3cf1ccf5569e543af13c011bebcaa43`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
En cas d'inexactitudes ou d'omissions, l’amende est de 5 % des retenues qui auraient dû être effectuées ou déclarées lorsque la déclaration a été déposée dans les délais. Le taux de l’amende est porté à 40 % en cas d'inexactitudes ou d'omissions délibérées. Pour plus de précisions sur l'appréciation du caractère délibéré de l'infraction, il convient de se reporter au III § 30 à 50 du BOI-CF-INF-10-20-20.
```

### T582_0

Official table/operative selected clause for current Guide LF582; https://bofip.impots.gouv.fr/bofip/11471-PGP.html; read2026-10-29; nativeLF75–75; readerSHA256 `0373e989f70f4fc21944c2734b4aea14e3cf1ccf5569e543af13c011bebcaa43`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
En cas d'inexactitudes ou d'omissions, l’amende est de 5 % des retenues qui auraient dû être effectuées ou déclarées lorsque la déclaration a été déposée dans les délais. Le taux de l’amende est porté à 40 % en cas d'inexactitudes ou d'omissions délibérées. Pour plus de précisions sur l'appréciation du caractère délibéré de l'infraction, il convient de se reporter au III § 30 à 50 du BOI-CF-INF-10-20-20.
```

### T583_0

Official table/operative selected clause for current Guide LF583; https://bofip.impots.gouv.fr/bofip/11471-PGP.html; read2026-10-29; nativeLF76–76; readerSHA256 `0373e989f70f4fc21944c2734b4aea14e3cf1ccf5569e543af13c011bebcaa43`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
En cas de non-dépôt de la déclaration dans les délais prescrits, l’amende s’élève à 10 % des retenues qui auraient dû être effectuées ou déclarées. L’amende est portée à 40 % des retenues qui auraient dû être effectuées ou déclarées en cas de non-dépôt de la déclaration dans les trente jours suivant une mise en demeure.
```

### T584_0

Official table/operative selected clause for current Guide LF584; https://bofip.impots.gouv.fr/bofip/11471-PGP.html; read2026-10-29; nativeLF76–76; readerSHA256 `0373e989f70f4fc21944c2734b4aea14e3cf1ccf5569e543af13c011bebcaa43`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
En cas de non-dépôt de la déclaration dans les délais prescrits, l’amende s’élève à 10 % des retenues qui auraient dû être effectuées ou déclarées. L’amende est portée à 40 % des retenues qui auraient dû être effectuées ou déclarées en cas de non-dépôt de la déclaration dans les trente jours suivant une mise en demeure.
```

### T585_0

Official table/operative selected clause for current Guide LF585; https://bofip.impots.gouv.fr/bofip/11471-PGP.html; read2026-10-29; nativeLF77–77; readerSHA256 `0373e989f70f4fc21944c2734b4aea14e3cf1ccf5569e543af13c011bebcaa43`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Les retenues qui ont été effectuées mais délibérément non déclarées et non versées au comptable public donnent lieu à une amende égale à 80 % des retenues effectuées.
```

### T586_0

Official table/operative selected clause for current Guide LF586; https://bofip.impots.gouv.fr/bofip/11471-PGP.html; read2026-10-29; nativeLF79–79; readerSHA256 `0373e989f70f4fc21944c2734b4aea14e3cf1ccf5569e543af13c011bebcaa43`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Dans tous les cas, l’amende est au minimum égale à 250 € par déclaration.
```

### T587_0

Official table/operative selected clause for current Guide LF587; https://bofip.impots.gouv.fr/bofip/11471-PGP.html; read2026-10-29; nativeLF98–98; readerSHA256 `0373e989f70f4fc21944c2734b4aea14e3cf1ccf5569e543af13c011bebcaa43`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
L’entreprise encourt ainsi une majoration égale à 5 % du montant non payé, soit 500 €.
```

### T588_0

Official table/operative selected clause for current Guide LF588; https://bofip.impots.gouv.fr/bofip/11471-PGP.html; read2026-10-29; nativeLF106–106; readerSHA256 `0373e989f70f4fc21944c2734b4aea14e3cf1ccf5569e543af13c011bebcaa43`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
Conformément aux dispositions combinées de l'article 1771 A du CGI et de l'article 131-13 du code pénal, le fait pour un collecteur d’effectuer la retenue à la source mais de s’abstenir délibérément de la déclarer et de la verser au comptable public constitue, si le retard excède un mois, une contravention de cinquième classe, passible d’une amende de 1 500 €.
```

### T589_0

Official table/operative selected clause for current Guide LF589; https://bofip.impots.gouv.fr/bofip/11471-PGP.html; read2026-10-29; nativeLF107–107; readerSHA256 `0373e989f70f4fc21944c2734b4aea14e3cf1ccf5569e543af13c011bebcaa43`. Exact source slice located by text, then actually read in finite196-clause native-source display batches by writer A29October2026; contextual applicability separately anchored. No whole-source-reading claim. Representation: original retained body

```text
La récidive dans un délai de trois ans de la rétention constitue un délit punissable de deux ans d'emprisonnement et de 3 750 € d'amende ou de l'une de ces deux peines seulement.
```

### PAY_WEEKLY_DEROG

ServicePublicF1911 ordinary48/44 and exceptional60/agreed-or-authorised46 branches; https://www.service-public.gouv.fr/particuliers/vosdroits/F1911; read2026-10-31; nativeLF117–126; readerSHA256 `44f04e7087f6d573887b75b4fd33c975de664eb9eec806f65d76bff0ccaeafa2`. Root personally reread actual retained selected scope31October2026. Source identity/provenance from original independent receipt retained; no new whole-body acquisition. Representation: Root personally reread actual retained selected scope31October2026. Source identity/provenance from original independent receipt retained; no new whole-body acquisition.

```text
La durée de travail effectif: titleContent hebdomadaire ne doit pas dépasser l’une des 2 limites suivantes :
Soit 48 heures sur une même semaine
Soit 44 heures par semaine en moyenne sur une période de 12 semaines consécutives.
Exemple :
Si le salarié est amené à travailler 48 heures hebdomadaires pendant 6 semaines d'affilée, puis 40 heures les 6 semaines suivantes, le salarié aura travaillé en moyenne 44 heures hebdomadaires sur la période de 12 semaines consécutives. Son temps de travail ne dépasse donc pas les durées maximales hebdomadaires de travail autorisées.
Par dérogation, la durée maximale sur une semaine (48 heures) peut être augmentée, en cas de circonstances exceptionnelles, jusqu'à 60 heures maximum.
Pour cela, l'inspection du travail doit donner son accord.
Le dépassement de la durée moyenne de 44 heures est possible, dans la limite de 46 heures sur une période de 12 semaines consécutives, dans l'un des cas suivants :
Soit une convention collective: titleContent ou un accord collectif d'entreprise: titleContent le prévoit
Soit après autorisation de l'inspection du travail
```

### PAY_YOUTH_17_18

Urssaf2026SMIC age17–18 plus Jan/June headers and hourly rates; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/montant-smic.html; read2026-10-31; nativeLF37–43; readerSHA256 `67255c339b8d7ddbfcbe32f162b1c96b67cf41b7d7c363af3eb5ea965228dad6`. Root personally reread actual retained selected scope31October2026. Source identity/provenance from original independent receipt retained; no new whole-body acquisition. Representation: Root personally reread actual retained selected scope31October2026. Source identity/provenance from original independent receipt retained; no new whole-body acquisition.

```text
  * ### Pour les salariés entre 17 ans et 18 ans

Pour les salariés entre 17 ans et 18 ans
 | Du 1^{er} janvier 2026 au 31 mai 2026  | Au 1^{er} juin 2026
--- | --- | ---
Smic horaire brut  | 10,82 €  | 11,08 €
Smic brut mensuel (base 35 heures par semaine)  | 1 640,73 €  | 1 680,32 €
```

### PAY_YOUTH_UNDER17

Urssaf2026SMIC under17 plus Jan/June headers and hourly rates; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/montant-smic.html; read2026-10-31; nativeLF55–61; readerSHA256 `67255c339b8d7ddbfcbe32f162b1c96b67cf41b7d7c363af3eb5ea965228dad6`. Root personally reread actual retained selected scope31October2026. Source identity/provenance from original independent receipt retained; no new whole-body acquisition. Representation: Root personally reread actual retained selected scope31October2026. Source identity/provenance from original independent receipt retained; no new whole-body acquisition.

```text
  * ### Pour les salariés de moins de 17 ans

Pour les salariés de moins de 17 ans
 | Du 1^{er} janvier 2026 au 31 mai 2026  | Au 1^{er} juin 2026
--- | --- | ---
Smic horaire brut  | 9,62 €  | 9,85 €
Smic brut mensuel (base 35 heures par semaine)  | 1 458,43 €  | 1 493,62 €
```

### PAY_DAY20PLUS

Article L241-18-1 II–V:sevenfold day route/cap/compliance/remuneration/substitution/de-minimis/records; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053278678/2026-10-09; read2026-10-31; nativeLF20–33; readerSHA256 `e2a24d26214ea577a04d41cb68b9020a431c953f6551a77b031c1885c60b65a0`. Retained exact official indexed/tool response JSON decoded once to its original string, not HTTPHTML. Only the named article II–V is quoted/read for this repair; other search results are not a code reading. Representation: Retained exact official indexed/tool response JSON decoded once to its original string, not HTTPHTML. Only the named article II–V is quoted/read for this repair; other search results are not a code reading.

```text
II. - Dans les mêmes entreprises, une déduction forfaitaire égale à sept fois le montant défini au I du présent article est également applicable pour chaque jour de repos auquel renonce un salarié relevant d'une convention de forfait en jours sur l'année, au-delà de la limite mentionnée au 3° du I de l'article L. 3121-64 du code du travail, dans les conditions prévues à l'article L. 3121-59 du même code.

III. - Les déductions mentionnées aux I et II du présent article sont imputées sur les sommes dues par les employeurs aux organismes de recouvrement mentionnés à l'article L. 213-1 du code de la sécurité sociale et à l'article L. 725-3 du code rural et de la pêche maritime pour chaque salarié concerné au titre de l'ensemble de sa rémunération versée au moment du paiement de cette durée de travail supplémentaire et ne peuvent dépasser ce montant.

IV. - Les déductions mentionnées aux I et II du présent article sont cumulables avec des exonérations de cotisations patronales de sécurité sociale dans la limite du montant des cotisations patronales de sécurité sociale et des contributions patronales recouvrées suivant les mêmes règles, restant dues par l'employeur au titre de l'ensemble de la rémunération du salarié concerné.

Les mêmes I et II sont applicables sous réserve du respect par l'employeur des dispositions légales et conventionnelles relatives à la durée du travail et sous réserve que l'heure supplémentaire effectuée fasse l'objet d'une rémunération au moins égale à celle d'une heure non majorée.

Ils ne sont pas applicables lorsque ces revenus d'activité se substituent à des sommes soumises à cotisations de sécurité sociale en application du I de l'article L. 242-1 du code de la sécurité sociale, à moins qu'un délai de douze mois ne se soit écoulé entre le dernier versement de l'élément de rémunération en tout ou partie supprimé et le premier versement des revenus mentionnés aux I et II du présent article.

Le bénéfice des déductions mentionnées aux mêmes I et II est subordonné au respect du règlement (UE) n° 1407/2013 de la Commission du 18 décembre 2013 relatif à l'application des articles 107 et 108 du traité sur le fonctionnement de l'Union européenne aux aides de minimis.

V. - Le bénéfice des déductions mentionnées aux I et II est subordonné, pour l'employeur, à la mise à la disposition des agents chargés du contrôle mentionnés à l'article L. 243-7 du code de la sécurité sociale et à l'article L. 724-7 du code rural et de la pêche maritime d'un document en vue du contrôle de l'application du présent article.

```

### PAY_DAYUNDER20

Article L241-18 II–V:sevenfold day route/cap/compliance/remuneration/substitution/de-minimis/records; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038610232/2026-01-01; read2026-10-31; nativeLF61–76; readerSHA256 `e2a24d26214ea577a04d41cb68b9020a431c953f6551a77b031c1885c60b65a0`. Retained exact official indexed/tool response JSON decoded once to its original string, not HTTPHTML. Only the named article II–V is quoted/read for this repair; other search results are not a code reading. Representation: Retained exact official indexed/tool response JSON decoded once to its original string, not HTTPHTML. Only the named article II–V is quoted/read for this repair; other search results are not a code reading.

```text
II.-Dans les mêmes entreprises, une déduction forfaitaire égale à sept fois le montant défini au I est également applicable pour chaque jour de repos auquel renonce un salarié relevant d'une convention de forfait en jours sur l'année, au-delà du plafond de deux cent dix-huit jours mentionné au 3° du I de l'article L. 3121-64 du code du travail, dans les conditions prévues à l'article L. 3121-59 du même code.

III.-Les déductions mentionnées aux I et II sont imputées sur les sommes dues par les employeurs aux organismes de recouvrement mentionnés aux articles L. 213-1 du présent code et L. 725-3 du code rural et de la pêche maritime pour chaque salarié concerné au titre de l'ensemble de sa rémunération versée au moment du paiement de cette durée de travail supplémentaire et ne peuvent dépasser ce montant.

IV.-Les déductions mentionnées aux I et II sont cumulables avec des exonérations de cotisations patronales de sécurité sociale dans la limite des cotisations patronales de sécurité sociale, ainsi que des contributions patronales recouvrées suivant les mêmes règles, restant dues par l'employeur au titre de l'ensemble de la rémunération du salarié concerné.

Les I et II sont applicables sous réserve du respect par l'employeur des dispositions légales et conventionnelles relatives à la durée du travail et sous réserve que l'heure supplémentaire effectuée fasse l'objet d'une rémunération au moins égale à celle d'une heure non majorée.

Ils ne sont pas applicables lorsque ces revenus d'activité se substituent à des sommes soumises à cotisations de sécurité sociale en application du premier alinéa de l'article L. 242-1 du présent code, à moins qu'un délai de douze mois ne se soit écoulé entre le dernier versement de l'élément de rémunération en tout ou partie supprimé et le premier versement des revenus mentionnés aux I et II du présent article.

Le bénéfice des déductions mentionnées aux I et II du présent article est subordonné au respect du règlement (UE) n° 1407/2013 de la Commission, du 18 décembre 2013, relatif à l'application des articles 107 et 108 du traité sur le fonctionnement de l'Union européenne aux aides de minimis.

V.-Le bénéfice des déductions mentionnées aux I et II est subordonné, pour l'employeur, à la mise à la disposition des agents chargés du contrôle mentionnés à l'article L. 243-7 du présent code et à l'article L. 724-7 du code rural et de la pêche maritime d'un document en vue du contrôle de l'application du présent article.

V bis.-Abrogé.

```

## Old topics carried

| Origin / old LF | Old wording | Current destination or explicit disposition |
|---|---|---|
| 11eb01a4 / 20 | **Section 1 -- Quick Reference** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 22 | &#124; Field &#124; Value &#124; | Presentation-only table header; current same-topic table supplies the substantive cells. |
| 11eb01a4 / 24 | &#124; Country &#124; France (République française) &#124; | Current exact semantic Quick Reference destination LF27. Metadata/administrative scope preserved; old almost-universal frequency is descriptive, not a legal mandate. |
| 11eb01a4 / 25 | &#124; Currency &#124; EUR only &#124; | Current exact semantic Quick Reference destination LF28. Metadata/administrative scope preserved; old almost-universal frequency is descriptive, not a legal mandate. |
| 11eb01a4 / 26 | &#124; Standard pay frequency &#124; Monthly (mensuel) -- almost universal &#124; | Current exact semantic Quick Reference destination LF29. Metadata/administrative scope preserved; old almost-universal frequency is descriptive, not a legal mandate. |
| 11eb01a4 / 27 | &#124; Tax year &#124; Calendar year (1 January -- 31 December) &#124; | Current exact semantic Quick Reference destination LF30. Metadata/administrative scope preserved; old almost-universal frequency is descriptive, not a legal mandate. |
| 11eb01a4 / 28 | &#124; Income tax withholding &#124; Prélèvement à la Source (PAS) -- rate communicated by DGFiP to employer &#124; | Current exact semantic Quick Reference destination LF31. Metadata/administrative scope preserved; old almost-universal frequency is descriptive, not a legal mandate. |
| 11eb01a4 / 29 | &#124; Social contribution authority &#124; URSSAF (collects contributions for all social security branches) &#124; | Current exact semantic Quick Reference destination LF32. Metadata/administrative scope preserved; old almost-universal frequency is descriptive, not a legal mandate. |
| 11eb01a4 / 30 | &#124; Supplementary pension &#124; AGIRC-ARRCO (single unified scheme since 2019) &#124; | Current exact semantic Quick Reference destination LF33. Metadata/administrative scope preserved; old almost-universal frequency is descriptive, not a legal mandate. |
| 11eb01a4 / 31 | &#124; Tax authority &#124; Direction Générale des Finances Publiques (DGFiP) &#124; | Current exact semantic Quick Reference destination LF34. Metadata/administrative scope preserved; old almost-universal frequency is descriptive, not a legal mandate. |
| 11eb01a4 / 32 | &#124; Key legislation &#124; Code de la Sécurité sociale; Code du Travail; Code Général des Impôts (Art. 204 A--M for PAS) &#124; | Current exact semantic Quick Reference destination LF35. Metadata/administrative scope preserved; old almost-universal frequency is descriptive, not a legal mandate. |
| 11eb01a4 / 33 | &#124; Social Security Ceiling (PMSS, 2026) &#124; EUR 4,005/month (EUR 48,060/year) &#124; | Current exact semantic Quick Reference destination LF36. Metadata/administrative scope preserved; old almost-universal frequency is descriptive, not a legal mandate. |
| 11eb01a4 / 34 | &#124; Electronic declaration &#124; DSN (Déclaration Sociale Nominative) via net-entreprises.fr &#124; | Current exact semantic Quick Reference destination LF40. Metadata/administrative scope preserved; old almost-universal frequency is descriptive, not a legal mandate. |
| 11eb01a4 / 35 | &#124; Validated by &#124; Pending -- requires sign-off by a French expert-comptable &#124; | Current exact semantic Quick Reference destination LF41. Metadata/administrative scope preserved; old almost-universal frequency is descriptive, not a legal mandate. |
| 11eb01a4 / 36 | &#124; Skill version &#124; 1.0 &#124; | Historical version presentation1.0; current metadata/H1version1.1; no tax rule. |
| 11eb01a4 / 40 | Since 1 January 2019, France operates a PAYE system where the employer withholds income tax from the employee's **net imposable** (net taxable salary) each month. | Current How PAS Works, opening sentence and net-imposable/personal-rate method LF55–68; actual1January2019 commencement preserved. |
| 11eb01a4 / 44 | **How PAS Works** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 46 | &#124; Step &#124; Detail &#124; | Presentation-only table header; current same-topic table supplies the substantive cells. |
| 11eb01a4 / 48 | &#124; Rate source &#124; DGFiP transmits the employee's personalised PAS rate to the employer via the DSN feedback loop &#124; | Actual current component destinations LF53, LF657. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 49 | &#124; Default rate &#124; If no personalised rate is available, a statutory "taux neutre" (barème par défaut) applies, based on monthly net imposable &#124; | Actual current component destinations LF58, LF79, LF117, LF657. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 50 | &#124; Calculation &#124; PAS = Net imposable x PAS rate &#124; | Actual current component destinations LF59, LF657. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 51 | &#124; Deducted from &#124; Net salary (after social contributions, before payment) &#124; | Actual current component destinations LF59, LF657. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 52 | &#124; Remittance &#124; Monthly via DSN + URSSAF collection &#124; | Corrected: DGFiP SEPA B2Bremittance; DSN is the channel, not Urssaf as income-tax payee. Current LF51; LF53; LF54; LF55. |
| 11eb01a4 / 56 | **Income Tax Brackets (2026, progressive scale for annual declaration)** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 58 | &#124; Taxable Income (EUR, per part) &#124; Rate &#124; | Current same substantive Income Tax Brackets (2026, progressive scale for annual declaration) at LF66,LF68,LF70,LF71,LF72,LF73. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 60 | &#124; 0 -- 11,600 &#124; 0% &#124; | Current same substantive Income Tax Brackets (2026, progressive scale for annual declaration) at LF66,LF68,LF70,LF71,LF72,LF73. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 61 | &#124; 11,601 -- 29,579 &#124; 11% &#124; | Current same substantive Income Tax Brackets (2026, progressive scale for annual declaration) at LF66,LF68,LF70,LF71,LF72,LF73. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 62 | &#124; 29,580 -- 84,577 &#124; 30% &#124; | Current same substantive Income Tax Brackets (2026, progressive scale for annual declaration) at LF66,LF68,LF70,LF71,LF72,LF73. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 63 | &#124; 84,578 -- 181,917 &#124; 41% &#124; | Current same substantive Income Tax Brackets (2026, progressive scale for annual declaration) at LF66,LF68,LF70,LF71,LF72,LF73. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 64 | &#124; 181,918+ &#124; 45% &#124; | Current same substantive Income Tax Brackets (2026, progressive scale for annual declaration) at LF66,LF68,LF70,LF71,LF72,LF73. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 66 | The PAS rate already accounts for the quotient familial (family coefficient) system when personalised. The employer does NOT compute tax brackets -- they simply apply the rate received from DGFiP. | Current same substantive Income Tax Brackets (2026, progressive scale for annual declaration) at LF66,LF68,LF70,LF71,LF72,LF73. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 70 | Used when no personalised rate is available. Based on monthly net imposable. Progressive grid from 0% (low income) to 43% (high income). Consult the CGI Article 204 H barème for exact thresholds. | Current same substantive Taux Neutre (Default Rate Grid, 2026: Metropolitan France) at LF81,LF83,LF85,LF86,LF87,LF88. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 76 | **URSSAF Contributions (Employee Share)** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 78 | &#124; Contribution &#124; Employee Rate &#124; Base &#124; | Presentation-only table header; current same-topic table supplies the substantive cells. |
| 11eb01a4 / 80 | &#124; Maladie, maternité, invalidité, décès &#124; 0% &#124; Total gross &#124; | Actual current component destinations LF133. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 81 | &#124; Vieillesse plafonnée (old-age, capped) &#124; 6.90% &#124; Up to 1 PMSS (EUR 4,005/month) &#124; | Actual current component destinations LF127. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 82 | &#124; Vieillesse déplafonnée (old-age, uncapped) &#124; 0.40% &#124; Total gross &#124; | Actual current component destinations LF126. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 83 | &#124; CSG déductible &#124; 6.80% &#124; 98.25% of gross &#124; | Actual current component destinations LF128, LF147. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 84 | &#124; CSG non-déductible &#124; 2.40% &#124; 98.25% of gross &#124; | Actual current component destinations LF129, LF147. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 85 | &#124; CRDS &#124; 0.50% &#124; 98.25% of gross &#124; | Actual current component destinations LF130, LF147. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 87 | - **98.25% abattement threshold** — The 98.25% abattement (1.75% deduction for professional expenses) applies only up to 4 PMSS (EUR 192,240/year in 2026). Above that threshold, CSG/CRDS apply on 100% of gross. | Corrected terminology: fourANNUAL ceilings,192240 annual, not fourmonthly ceilings. Current LF123; LF125; LF126; LF127. |
| 11eb01a4 / 91 | **AGIRC-ARRCO (Supplementary Pension -- Employee Share)** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 93 | &#124; Contribution &#124; Employee Rate &#124; Base &#124; | Presentation-only table header; current same-topic table supplies the substantive cells. |
| 11eb01a4 / 95 | &#124; Retraite complémentaire Tranche 1 (T1) &#124; 3.15% &#124; Up to 1 PMSS &#124; | Actual current component destinations LF154. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 96 | &#124; Retraite complémentaire Tranche 2 (T2) &#124; 8.64% &#124; From 1 to 8 PMSS (EUR 4,005 -- EUR 32,040) &#124; | Actual current component destinations LF155. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 97 | &#124; CEG (Contribution d'Équilibre Général) T1 &#124; 0.86% &#124; Up to 1 PMSS &#124; | Actual current component destinations LF169, LF173. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 98 | &#124; CEG T2 &#124; 1.08% &#124; From 1 to 8 PMSS &#124; | Actual current component destinations LF170, LF173. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. Preserve the actual household-employer-source/general-rule confirmation limitation; this route does not silently certify every private-sector tranche2/CET rate. |
| 11eb01a4 / 99 | &#124; CET (Contribution d'Équilibre Technique) &#124; 0.14% &#124; From 1 to 8 PMSS (cadres/non-cadres above PMSS) &#124; | Actual current component destinations LF171, LF173. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. Preserve the actual household-employer-source/general-rule confirmation limitation; this route does not silently certify every private-sector tranche2/CET rate. |
| 11eb01a4 / 101 | - **Appelés rates** — AGIRC-ARRCO rates shown are appelés (call rates = 127% of contractual rates). Pension points are calculated on the contractual rate (e.g., T1 contractual = 6.20% total). | Current actual call-rate versus points-rate distinction retained; historical127% factor retained here, not asserted from rounded7.87/6.20 as an exact new ratio. Current LF151; LF153; LF154; LF155. |
| 11eb01a4 / 105 | **Chômage (Unemployment -- Employee Share)** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 107 | &#124; Contribution &#124; Employee Rate &#124; Base &#124; | Presentation-only table header; current same-topic table supplies the substantive cells. |
| 11eb01a4 / 109 | &#124; Assurance chômage &#124; 0% &#124; Up to 4 PMSS &#124; | Current same substantive Chômage (Unemployment: Employee Share) at LF177. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 111 | - **Employee unemployment contribution abolished** — Employee unemployment contribution was abolished in October 2018. Only the employer pays. | Current no-employee-unemployment method retained; historical abolition date is not used as a new current rate proof. Current LF177. |
| 11eb01a4 / 115 | - **Total employee deductions at PMSS** — For a salary at the PMSS (EUR 4,005/month): employee social contributions total approximately 21--23% of gross, plus PAS income tax. | Not yet confirmed: historical blanket21–23% estimate is not a universal liability; current actual contribution lines and worked cases replace it. Current LF181; LF183; LF185; LF187. |
| 11eb01a4 / 121 | **URSSAF Contributions (Employer Share)** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 123 | &#124; Contribution &#124; Employer Rate &#124; Base &#124; | Presentation-only table header; current same-topic table supplies the substantive cells. |
| 11eb01a4 / 125 | &#124; Maladie, maternité, invalidité, décès &#124; 13.00% &#124; Total gross &#124; | Actual current component destinations LF202, LF203, LF204, LF225. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 126 | &#124; Vieillesse plafonnée &#124; 8.55% &#124; Up to 1 PMSS &#124; | Actual current component destinations LF207. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 127 | &#124; Vieillesse déplafonnée &#124; 2.11% &#124; Total gross &#124; | Actual current component destinations LF206. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 128 | &#124; Allocations familiales &#124; 5.25% &#124; Total gross &#124; | Actual current component destinations LF208, LF209, LF210, LF225. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 129 | &#124; Accidents du travail (AT/MP) &#124; Variable (0.5%--7%+) &#124; Total gross &#124; | Not yet confirmed: historical nationalAT/MP range; actual notified Carsat rate is required. Current LF199; LF201; LF202; LF203. |
| 11eb01a4 / 130 | &#124; Contribution Solidarité Autonomie (CSA) &#124; 0.30% &#124; Total gross &#124; | Actual current component destinations LF205. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 131 | &#124; FNAL (Fonds National d'Aide au Logement) &#124; 0.10% (< 50 employees) or 0.50% (≥ 50) &#124; Up to 1 PMSS or total gross &#124; | Actual current component destinations LF212, LF213. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 132 | &#124; Contribution au dialogue social &#124; 0.016% &#124; Total gross &#124; | Actual current component destinations LF211. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 136 | **AGIRC-ARRCO (Employer Share)** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 138 | &#124; Contribution &#124; Employer Rate &#124; Base &#124; | Presentation-only table header; current same-topic table supplies the substantive cells. |
| 11eb01a4 / 140 | &#124; Retraite complémentaire T1 &#124; 4.72% &#124; Up to 1 PMSS &#124; | Actual current component destinations LF283. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 141 | &#124; Retraite complémentaire T2 &#124; 12.95% &#124; From 1 to 8 PMSS &#124; | Actual current component destinations LF284. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 142 | &#124; CEG T1 &#124; 1.29% &#124; Up to 1 PMSS &#124; | Actual current component destinations LF289, LF295. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. Preserve the actual household-employer-source/general-rule confirmation limitation; this route does not silently certify every private-sector tranche2/CET rate. |
| 11eb01a4 / 143 | &#124; CEG T2 &#124; 1.62% &#124; From 1 to 8 PMSS &#124; | Actual current component destinations LF290, LF295. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. Preserve the actual household-employer-source/general-rule confirmation limitation; this route does not silently certify every private-sector tranche2/CET rate. |
| 11eb01a4 / 144 | &#124; CET &#124; 0.21% &#124; From 1 to 8 PMSS &#124; | Actual current component destinations LF291, LF295. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. Preserve the actual household-employer-source/general-rule confirmation limitation; this route does not silently certify every private-sector tranche2/CET rate. |
| 11eb01a4 / 145 | &#124; APEC (cadres only) &#124; 0.036% &#124; Up to 4 PMSS &#124; | Current own Agirc-Arrco source now supplies.06total/.024employee/.036employer up to4PSS; distinct provident minimum remains a precise agreement handoff. Current LF280; LF282; LF283; LF284. |
| 11eb01a4 / 149 | **Unemployment and Other Employer-Only** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 151 | &#124; Contribution &#124; Employer Rate &#124; Base &#124; | Presentation-only table header; current same-topic table supplies the substantive cells. |
| 11eb01a4 / 153 | &#124; Assurance chômage &#124; 4.05% &#124; Up to 4 PMSS (EUR 16,020/month) &#124; | Corrected: actual2026 employer4.00%, with192240 annual cap. Current LF301; LF303; LF304; LF305. |
| 11eb01a4 / 154 | &#124; AGS (Association pour la Gestion du régime d'assurance des créances des Salariés) &#124; 0.25% &#124; Up to 4 PMSS &#124; | Current same substantive Unemployment and Other Employer-Only at LF301,LF303,LF304,LF305,LF306,LF307. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 155 | &#124; Prévoyance cadres (minimum) &#124; 1.50% &#124; Up to 1 PMSS (Convention collective nationale des cadres) &#124; | Not yet confirmed: historical cadre provident1.5% minimum needs actual applicable agreement; current precise provident handoff retained, Apec separately supplied. Current LF716; LF717; LF718; LF719. |
| 11eb01a4 / 159 | - **Total employer cost approximate** — Total employer contributions typically amount to 45--55% on top of gross salary, depending on industry (AT/MP rate), company size, and whether the employee is cadre or non-cadre. | Not yet confirmed: historical blanket45–55% cost shortcut; current per-line rates and RGDU method replace it. Current LF318. |
| 11eb01a4 / 165 | **SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026)** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 167 | &#124; Item &#124; Value &#124; | Presentation-only table header; current same-topic table supplies the substantive cells. |
| 11eb01a4 / 169 | &#124; Gross hourly (from 1 June 2026) &#124; EUR 12.31 &#124; | Actual current component destinations LF331. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 170 | &#124; Gross monthly (35 hrs/week) &#124; EUR 1,867.02 &#124; | Actual current component destinations LF332. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 171 | &#124; Net monthly (approximate) &#124; EUR 1,477.93 &#124; | Not yet confirmed: historical net-Smic1477.93 is not the current sourced net-taxable Smic1531.12; gross/year tables retained. Current LF324; LF326; LF328; LF329. |
| 11eb01a4 / 172 | &#124; Prior rate (1 Jan -- 31 May 2026) &#124; EUR 12.02/hour (EUR 1,823.03/month gross) &#124; | Actual current component destinations LF329, LF330. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 174 | - **SMIC revalorisation rule** — The SMIC is revalorised automatically when CPI rises 2%+ since the last revaluation, and annually on 1 January. | Not yet confirmed: historical automatic-revaluation CPI2%/January assertion; current date-specific sourced rates and recheck rule retained. Current LF324; LF326; LF328; LF329. |
| 11eb01a4 / 178 | **Working Hours and Overtime** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 180 | &#124; Rule &#124; Detail &#124; | Presentation-only table header; current same-topic table supplies the substantive cells. |
| 11eb01a4 / 182 | &#124; Legal weekly hours (durée légale) &#124; 35 hours &#124; | Current same substantive Working Hours and Overtime at LF348,LF350,LF351,LF352,LF353,LF354. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 183 | &#124; Maximum daily hours &#124; 10 hours (extendable to 12 by agreement) &#124; | Current same substantive Working Hours and Overtime at LF348,LF350,LF351,LF352,LF353,LF354. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 184 | &#124; Maximum weekly hours &#124; 48 hours absolute; 44 hours average over 12 weeks &#124; | Current same substantive Working Hours and Overtime at LF348,LF350,LF351,LF352,LF353,LF354. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 185 | &#124; Overtime: 36th--43rd hour &#124; +25% of hourly rate &#124; | Current same substantive Working Hours and Overtime at LF348,LF350,LF351,LF352,LF353,LF354. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 186 | &#124; Overtime: 44th hour and above &#124; +50% of hourly rate &#124; | Current same substantive Working Hours and Overtime at LF348,LF350,LF351,LF352,LF353,LF354. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 187 | &#124; Annual overtime contingent &#124; 220 hours default (modifiable by collective agreement) &#124; | Current same substantive Working Hours and Overtime at LF348,LF350,LF351,LF352,LF353,LF354. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 188 | &#124; Alternative to payment &#124; Repos compensateur (compensatory time off) per agreement &#124; | Current same substantive Working Hours and Overtime at LF348,LF350,LF351,LF352,LF353,LF354. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 190 | - **Collective agreements may adjust rates** — Collective agreements (conventions collectives) may adjust these rates and thresholds. | Current same substantive Working Hours and Overtime at LF348,LF350,LF351,LF352,LF353,LF354. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 196 | **Congés Payés (Paid Annual Leave)** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 198 | &#124; Entitlement &#124; Detail &#124; | Presentation-only table header; current same-topic table supplies the substantive cells. |
| 11eb01a4 / 200 | &#124; Statutory &#124; 2.5 working days per month worked = 30 working days (5 weeks) per year &#124; | Current same substantive Congés Payés (Paid Annual Leave) at LF375,LF377,LF378,LF379,LF380,LF381. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 201 | &#124; Accrual period &#124; 1 June -- 31 May (reference period, unless otherwise agreed) &#124; | Current same substantive Congés Payés (Paid Annual Leave) at LF375,LF377,LF378,LF379,LF380,LF381. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 202 | &#124; Main leave &#124; Minimum 2 consecutive weeks between 1 May and 31 October &#124; | Current same substantive Congés Payés (Paid Annual Leave) at LF375,LF377,LF378,LF379,LF380,LF381. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 203 | &#124; Fractionnement bonus &#124; 1--2 extra days if leave is split outside the main period &#124; | Restored exact one/two-day fallback underL3141-23, 3–5/6+days, main24daylimit andagreement/individualderogation gates. Current LF375; LF377; LF378; LF379. |
| 11eb01a4 / 207 | **Sick Leave (Arrêt Maladie)** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 209 | &#124; Entitlement &#124; Detail &#124; | Presentation-only table header; current same-topic table supplies the substantive cells. |
| 11eb01a4 / 211 | &#124; Social security daily allowance (IJSS) &#124; 50% of daily base salary (capped at 1/720 of 3x PASS); 3-day waiting period &#124; | Corrected: prior-month1.4SMIC and3salary/91.25 method, not historical3PASS/720. Current LF389; LF391; LF392; LF393. |
| 11eb01a4 / 212 | &#124; Employer top-up (maintien de salaire) &#124; Per Code du Travail L1226-1: after 1 year seniority, employer pays 90% of gross for 30 days, then 66.66% for 30 days (periods increase with seniority) &#124; | Current same substantive Sick Leave (Arrêt Maladie) at LF389,LF391,LF392,LF393,LF394,LF395. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 213 | &#124; Medical certificate &#124; Required; sent to CPAM within 48 hours &#124; | Corrected employer-certificate gate; actualCPAM entitlement and separate employer top-up conditions supplied. Current LF389; LF391; LF392; LF393. |
| 11eb01a4 / 217 | **Maternity Leave (Congé de Maternité)** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 219 | &#124; Entitlement &#124; Detail &#124; | Presentation-only table header; current same-topic table supplies the substantive cells. |
| 11eb01a4 / 221 | &#124; Duration (1st/2nd child) &#124; 16 weeks (6 pre-natal + 10 post-natal) &#124; | Current same substantive Maternity Leave (Congé de Maternité) at LF419,LF421,LF422,LF423,LF424,LF425. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 222 | &#124; Duration (3rd+ child) &#124; 26 weeks (8 + 18) &#124; | Current same substantive Maternity Leave (Congé de Maternité) at LF419,LF421,LF422,LF423,LF424,LF425. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 223 | &#124; Twins &#124; 34 weeks; triplets+ 46 weeks &#124; | Current same substantive Maternity Leave (Congé de Maternité) at LF419,LF421,LF422,LF423,LF424,LF425. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 224 | &#124; Pay &#124; IJSS maternité (daily allowance from Sécurité sociale, capped at PMSS net equivalent) &#124; | Current same substantive Maternity Leave (Congé de Maternité) at LF419,LF421,LF422,LF423,LF424,LF425. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 225 | &#124; Employer top-up &#124; Many collective agreements provide 100% maintien de salaire &#124; | Current same substantive Maternity Leave (Congé de Maternité) at LF419,LF421,LF422,LF423,LF424,LF425. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 229 | **Paternity Leave (Congé de Paternité)** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 231 | &#124; Entitlement &#124; Detail &#124; | Presentation-only table header; current same-topic table supplies the substantive cells. |
| 11eb01a4 / 233 | &#124; Duration &#124; 25 calendar days (32 for multiple births) + 3 days congé de naissance &#124; | Current same substantive Paternity Leave (Congé de Paternité) at LF432,LF434,LF435,LF436,LF437,LF438. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 234 | &#124; Pay &#124; IJSS from Sécurité sociale; employer top-up per agreement &#124; | Current same substantive Paternity Leave (Congé de Paternité) at LF432,LF434,LF435,LF436,LF437,LF438. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 238 | No statutory obligation. Very common per collective agreements or company policy. Where contractual, it is subject to all cotisations and PAS. | Current same substantive 13th Month (Treizième Mois) at LF444. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 242 | **Mutuelle Obligatoire (Compulsory Health Insurance)** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 244 | &#124; Item &#124; Detail &#124; | Exact retained currentLF603: Employee Obligations |
| 11eb01a4 / 246 | &#124; Requirement &#124; Employer must offer a complémentaire santé to all employees (since 2016, ANI) &#124; | Current same substantive Mutuelle Obligatoire (Compulsory Health Insurance) at LF448,LF450,LF451,LF452,LF454. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 247 | &#124; Minimum employer contribution &#124; 50% of the premium &#124; | Current same substantive Mutuelle Obligatoire (Compulsory Health Insurance) at LF448,LF450,LF451,LF452,LF454. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 248 | &#124; Minimum coverage &#124; Panier de soins (basket of care): optician, dental, hospital &#124; | Current same substantive Mutuelle Obligatoire (Compulsory Health Insurance) at LF448,LF450,LF451,LF452,LF454. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 252 | The bulletin de paie is governed by Code du Travail Articles L3243-1 to L3243-4 and R3243-1. | Current Section7 Payslip Requirements and seven-zone fields; current official F559 display/selected Code references, delivery and retention subsection preserve the payslip obligation. |
| 11eb01a4 / 256 | **Mandatory Payslip Fields (Simplified Format since 2018)** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 258 | &#124; Section &#124; Required Fields &#124; | Presentation-only table header; current same-topic table supplies the substantive cells. |
| 11eb01a4 / 260 | &#124; Header &#124; Employer name, SIRET, APE/NAF code, convention collective applicable &#124; | Current same substantive Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) at LF511,LF513,LF514,LF515,LF516,LF517. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 261 | &#124; Employee &#124; Name, position, classification, date of entry &#124; | Current same substantive Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) at LF511,LF513,LF514,LF515,LF516,LF517. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 262 | &#124; Period &#124; Pay period, hours worked (normal + overtime + supplementary) &#124; | Current same substantive Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) at LF511,LF513,LF514,LF515,LF516,LF517. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 263 | &#124; Gross pay &#124; Base salary, overtime, bonuses, premiums, in-kind benefits &#124; | Current same substantive Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) at LF511,LF513,LF514,LF515,LF516,LF517. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 264 | &#124; Social contributions &#124; Grouped by risk: Santé, Accidents du travail, Retraite, Famille, Chômage, CSG/CRDS -- showing base, employee rate, employer rate, employee amount, employer amount &#124; | Current same substantive Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) at LF511,LF513,LF514,LF515,LF516,LF517. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 265 | &#124; Net imposable &#124; Gross minus deductible social contributions &#124; | Current same substantive Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) at LF511,LF513,LF514,LF515,LF516,LF517. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 266 | &#124; PAS &#124; PAS rate, PAS base, PAS amount withheld &#124; | Current same substantive Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) at LF511,LF513,LF514,LF515,LF516,LF517. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 267 | &#124; Net à payer avant PAS &#124; Net after all social contributions, before income tax &#124; | Current same substantive Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) at LF511,LF513,LF514,LF515,LF516,LF517. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 268 | &#124; Net à payer &#124; Final amount paid to employee (after PAS) &#124; | Current same substantive Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) at LF511,LF513,LF514,LF515,LF516,LF517. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 269 | &#124; Cumuls annuels &#124; Year-to-date totals: gross, net imposable, PAS withheld, hours worked &#124; | Current same substantive Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) at LF511,LF513,LF514,LF515,LF516,LF517. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 270 | &#124; Footer &#124; Payment date, leave balance, mention "conserver le bulletin de paie sans limitation de durée" &#124; | Current same substantive Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) at LF511,LF513,LF514,LF515,LF516,LF517. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 274 | - Paper or electronic (with employee consent or company agreement for digital) | Corrected: electronic default since2017, employee refusal; actual5yearbusiness/50yearor6afterretirement access rules supplied. Current LF527; LF528; LF529; LF530. |
| 11eb01a4 / 275 | - Employer must retain a copy for 5 years minimum | Current same substantive Delivery at LF527,LF528,LF529,LF530,LF531,LF533. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 276 | - Simplified format groups contributions by risk category rather than line-by-line | Current same substantive Delivery at LF527,LF528,LF529,LF530,LF531,LF533. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 282 | **Monthly -- DSN (Déclaration Sociale Nominative)** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 284 | &#124; Obligation &#124; Deadline &#124; Notes &#124; | Exact retained currentLF595: Annual |
| 11eb01a4 / 286 | &#124; DSN (≥ 50 employees) &#124; 5th of the month following the pay period &#124; Single electronic declaration to all social bodies &#124; | Current Monthly: DSN table and adjacent monthly/quarterly-payment explanation. Corrected:5th requires≥50 and salary paid in corresponding work month;15th otherwise; nonworking-day extension supplied. |
| 11eb01a4 / 287 | &#124; DSN (< 50 employees) &#124; 15th of the month following the pay period &#124; Same format, later deadline &#124; | Current Monthly: DSN table and adjacent monthly/quarterly-payment explanation. Corrected:5th requires≥50 and salary paid in corresponding work month;15th otherwise; nonworking-day extension supplied. |
| 11eb01a4 / 288 | &#124; DSN signalement d'événement &#124; Within 5 days of event &#124; Arrêt maladie, accident du travail, fin de contrat &#124; | Current Monthly: DSN event row and method step7. Corrected:5WORKINGdays after knowledge, actual subrogation/delayed-payroll exceptions and early-return-only event; not every event/date universally. |
| 11eb01a4 / 289 | &#124; PAS payment &#124; With DSN transmission &#124; Collected by URSSAF on behalf of DGFiP &#124; | Corrected same DGFiP payee/SEPA B2B; original workflow topic preserved. Current LF51; LF53; LF54; LF55. |
| 11eb01a4 / 290 | &#124; Social contribution payment &#124; With DSN transmission &#124; URSSAF debits after DSN acceptance &#124; | Current Monthly: DSN payment row and under11quarterly-payment explanation; electronic payment obligation retained, universal debit-on-acceptance assertion not repeated as a guaranteed2026 time. |
| 11eb01a4 / 292 | - **DSN replaces declarations** — The DSN replaced 25+ separate declarations and is the single channel for URSSAF, AGIRC-ARRCO, France Travail, CPAM, and DGFiP. | Current Monthly: DSN centralised-declaration paragraph and Sections8/9. Not yet confirmed: historical exact25+ replacement count is not established as a current total; channel/agency handoffs retained. |
| 11eb01a4 / 296 | **Annual** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 298 | &#124; Obligation &#124; Deadline &#124; Notes &#124; | Exact retained currentLF595: Annual |
| 11eb01a4 / 300 | &#124; DADS (replaced by DSN) &#124; N/A -- fully replaced since 2019 &#124; Historical reference only &#124; | Current same substantive Annual at LF595,LF597,LF598,LF599. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 301 | &#124; Bilan social &#124; Varies &#124; Companies ≥ 300 employees &#124; | Restored current300employee business/distinct establishment/CSE consultation andL2312-29 transition; no guessed filingdate. Current LF66; LF68; LF70; LF71. |
| 11eb01a4 / 302 | &#124; Index égalité professionnelle &#124; 1 March &#124; Companies ≥ 50 employees; gender pay gap index &#124; | Current same substantive Annual at LF595,LF597,LF598,LF599. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 306 | **Employee Obligations** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 308 | &#124; Item &#124; Detail &#124; | Exact retained currentLF603: Employee Obligations |
| 11eb01a4 / 310 | &#124; Déclaration de revenus &#124; Annual (April--June); pre-filled with PAS data &#124; | Current same substantive Employee Obligations at LF603,LF605,LF606,LF607. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 311 | &#124; Adjustment &#124; If PAS rate was incorrect, balance settled via avis d'imposition &#124; | Current same substantive Employee Obligations at LF603,LF605,LF606,LF607. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 317 | **Typical Bank Statement Descriptions (Salary Credits)** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 319 | &#124; Pattern &#124; Classification &#124; | Exact retained currentLF613: Typical Bank Statement Descriptions (Salary Credits) |
| 11eb01a4 / 321 | &#124; VIREMENT SALAIRE, VIR SALAIRE &#124; Net salary payment &#124; | Exact retained currentLF615: Typical Bank Statement Descriptions (Salary Credits) |
| 11eb01a4 / 322 | &#124; SALAIRE [EMPLOYER NAME] &#124; Net salary payment &#124; | Current same substantive Typical Bank Statement Descriptions (Salary Credits) at LF613,LF615,LF616,LF617,LF618,LF619. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 323 | &#124; INDEMNITE CONGES PAYES &#124; Holiday pay (if paid separately) &#124; | Current same substantive Typical Bank Statement Descriptions (Salary Credits) at LF613,LF615,LF616,LF617,LF618,LF619. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 324 | &#124; PRIME 13EME MOIS &#124; 13th month bonus &#124; | Current same substantive Typical Bank Statement Descriptions (Salary Credits) at LF613,LF615,LF616,LF617,LF618,LF619. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 325 | &#124; PRIME PARTICIPATION, INTERESSEMENT &#124; Profit-sharing (separate tax/social rules) &#124; | Current same substantive Typical Bank Statement Descriptions (Salary Credits) at LF613,LF615,LF616,LF617,LF618,LF619. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 326 | &#124; IJSS, CPAM INDEMNITE &#124; Sickness/maternity daily allowance from Sécurité sociale &#124; | Current same substantive Typical Bank Statement Descriptions (Salary Credits) at LF613,LF615,LF616,LF617,LF618,LF619. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 330 | **Typical Employer Debit Patterns** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 332 | &#124; Pattern &#124; Classification &#124; | Exact retained currentLF613: Typical Bank Statement Descriptions (Salary Credits) |
| 11eb01a4 / 334 | &#124; URSSAF COTISATIONS &#124; Monthly social contribution payment &#124; | Exact retained currentLF627: Typical Employer Debit Patterns |
| 11eb01a4 / 335 | &#124; AGIRC-ARRCO COTISATIONS &#124; Supplementary pension contributions &#124; | Exact retained currentLF628: Typical Employer Debit Patterns |
| 11eb01a4 / 336 | &#124; DGFIP PAS, PRELEVEMENT SOURCE &#124; PAS income tax remittance &#124; | Current same substantive Typical Employer Debit Patterns at LF625,LF627,LF628,LF629,LF630,LF631. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 337 | &#124; MUTUELLE [NAME] &#124; Compulsory health insurance premium &#124; | Current same substantive Typical Employer Debit Patterns at LF625,LF627,LF628,LF629,LF630,LF631. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 338 | &#124; PREVOYANCE [NAME] &#124; Provident insurance premium &#124; | Current same substantive Typical Employer Debit Patterns at LF625,LF627,LF628,LF629,LF630,LF631. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 342 | **Section 10 -- Interaction with Other Skills** | Presentation-only repeated heading; current same-topic section retains the substantive rules. |
| 11eb01a4 / 344 | &#124; Scenario &#124; Skill to Use &#124; | Presentation-only table header; current same-topic table supplies the substantive cells. |
| 11eb01a4 / 346 | &#124; Employee payroll (cotisations + PAS) &#124; **This skill (france-payroll.md)** &#124; | Current Section10 Interaction with Other Skills, matching actual payroll/PIT/social/VAT/bookkeeping/e-invoice routing row. Old filename labels are historical routing, not a tax method; current actual companion slugs replace them. |
| 11eb01a4 / 347 | &#124; Self-employed income tax &#124; france-income-tax.md &#124; | Current Section10 Interaction with Other Skills, matching actual payroll/PIT/social/VAT/bookkeeping/e-invoice routing row. Old filename labels are historical routing, not a tax method; current actual companion slugs replace them. |
| 11eb01a4 / 348 | &#124; Auto-entrepreneur / micro-enterprise &#124; france-micro-enterprise.md &#124; | Current Section10 Interaction with Other Skills, matching actual payroll/PIT/social/VAT/bookkeeping/e-invoice routing row. Old filename labels are historical routing, not a tax method; current actual companion slugs replace them. |
| 11eb01a4 / 349 | &#124; TVA (French VAT) &#124; france-vat-return.md &#124; | Current Section10 Interaction with Other Skills, matching actual payroll/PIT/social/VAT/bookkeeping/e-invoice routing row. Old filename labels are historical routing, not a tax method; current actual companion slugs replace them. |
| 11eb01a4 / 350 | &#124; Bookkeeping &#124; france-bookkeeping.md &#124; | Current Section10 Interaction with Other Skills, matching actual payroll/PIT/social/VAT/bookkeeping/e-invoice routing row. Old filename labels are historical routing, not a tax method; current actual companion slugs replace them. |
| 11eb01a4 / 351 | &#124; E-invoicing (Factur-X / Chorus Pro) &#124; france-einvoice.md &#124; | Current Section10 Interaction with Other Skills, matching actual payroll/PIT/social/VAT/bookkeeping/e-invoice routing row. Old filename labels are historical routing, not a tax method; current actual companion slugs replace them. |
| 11eb01a4 / 355 | - **Payroll → Bookkeeping:** Gross wages + employer charges are P&L expenses. Employee deductions (cotisations + PAS) are liabilities (comptes 43x) until DSN payment. Employer cotisations are booked to 645xxx. | Corrected: social liabilities43x, PAS4421; exact PCG labels linked. Current LF647; LF648; LF649. |
| 11eb01a4 / 356 | - **Payroll → Income Tax:** The PAS system means employees' income tax is largely settled in real time. Year-end déclaration may result in adjustments. The net imposable on the bulletin de paie is the reference figure. | Current same substantive Key Handoff Points at LF647,LF648,LF649. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 357 | - **Payroll → DSN:** All payroll data feeds directly into DSN. Accurate bulletins de paie = accurate DSN. Errors in DSN trigger anomaly reports from net-entreprises.fr. | Current same substantive Key Handoff Points at LF647,LF648,LF649. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 11eb01a4 / 361 | - **Prohibitions list** — - NEVER compute income tax brackets manually for withholding -- use the PAS rate provided by DGFiP - NEVER forget to apply the 98.25% abattement on gross for CSG/CRDS (and 100% above 4 PMSS) - NEVER confuse Tranche 1 (up to 1 PMSS) and Tranche 2 (1--8 PMSS) ceilings for AGIRC-ARRCO - NEVER omit the mutuelle obligatoire (compulsory health insurance) from employer cost calculations - NEVER apply employee chômage contributions -- they were abolished in 2018 - NEVER issue a bulletin de paie missing any mandatory field under Code du Travail - NEVER miss a DSN deadline -- penalties of EUR 7.50 per employee per month of delay - NEVER forget that SMIC changed mid-year (1 June 2026) -- verify which rate applies - NEVER present payroll computations as definitive -- direct to expert-comptable for sign-off | Actual current component destinations LF727, LF728, LF729, LF730, LF731, LF732, LF733, LF734, LF735, LF736, LF737. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 11eb01a4 / 365 | This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an expert-comptable in France) before implementation. | Exact retained currentLF777: Disclaimer |
| 11eb01a4 / 367 | The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes. | Historical disclaimer/platform presentation; current protected CTA exact; no financial claim dropped. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 20 | How a French employer runs a monthly payroll for an employee: the social contributions taken from gross pay, the employer contributions on top, the single degressive relief that now sits over them, income tax withheld at source (prélèvement à la source), the mandatory payslip, and the monthly DSN filing. Figures are for tax year 2026. The income tax scale in Section 2 is the one applied in 2026 to income of 2025 declared in 2026; every other figure in this skill (the withholding grid, social contributions, the Smic, the ceilings and the payroll reliefs) is the one in force during 2026, and where a figure changed inside 2026 the row gives its start date. The rules on contributions and the DSN are those in force on 19 October 2026. The Smic rose on 1 June 2026, so this skill gives both the January value and the June value, and the default withholding grid shown is the one in force from 1 May 2026. | Current same substantive French payroll: pay, contributions, PAS and DSN (2026, v1.1) at LF20. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 24 | &#124; Field &#124; Value &#124; Note &#124; | Exact retained currentLF24: Section 1: Quick Reference |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 26 | &#124; Source &#124; all figures below &#124; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/plafonds-securite-sociale.html &#124; | Exact retained currentLF26: Section 1: Quick Reference |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 27 | &#124; Country &#124; France (République française) &#124; &#124; | Exact retained currentLF27: Section 1: Quick Reference |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 28 | &#124; Currency &#124; EUR only &#124; &#124; | Exact retained currentLF28: Section 1: Quick Reference |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 29 | &#124; Standard pay frequency &#124; Monthly (mensuel), almost universal &#124; &#124; | Exact retained currentLF29: Section 1: Quick Reference |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 30 | &#124; Tax year &#124; Calendar year, 1 January to 31 December &#124; &#124; | Exact retained currentLF30: Section 1: Quick Reference |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 31 | &#124; Income tax withholding &#124; Prélèvement à la source, rate sent by DGFiP to the employer &#124; &#124; | Exact retained currentLF31: Section 1: Quick Reference |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 32 | &#124; Social contribution authority &#124; Urssaf, which collects for all branches &#124; &#124; | Exact retained currentLF32: Section 1: Quick Reference |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 33 | &#124; Supplementary pension &#124; Agirc-Arrco, one scheme since 2019 &#124; &#124; | Exact retained currentLF33: Section 1: Quick Reference |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 34 | &#124; Tax authority &#124; Direction générale des Finances publiques (DGFiP) &#124; &#124; | Exact retained currentLF34: Section 1: Quick Reference |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 35 | &#124; Key legislation &#124; Code de la Sécurité sociale; Code du travail; Code général des impôts art. 204 A to 204 M for the withholding &#124; &#124; | Exact retained currentLF35: Section 1: Quick Reference |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 36 | &#124; Monthly social security ceiling (plafond mensuel, PMSS) &#124; EUR 4,005 &#124; "Mois 4 005 €" &#124; | Exact retained currentLF36: Section 1: Quick Reference |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 37 | &#124; Annual social security ceiling (PASS) &#124; EUR 48,060 &#124; "2026 Année 48 060 €" &#124; | Exact retained currentLF37: Section 1: Quick Reference |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 38 | &#124; Daily ceiling, used to prorate a part month &#124; EUR 220 &#124; "Jour 220 €" &#124; | Corrected: ordinary monthly ceiling is monthlyPMSS×calendar-employment-days/calendar-month-days; daily220/hourly30 are not that formula. Current LF653; LF654; LF655; LF656. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 39 | &#124; Hourly ceiling &#124; EUR 30 &#124; "Heure 30 €" &#124; | Exact retained currentLF39: Section 1: Quick Reference |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 40 | &#124; Electronic declaration &#124; DSN, filed on net-entreprises.fr &#124; &#124; | Exact retained currentLF40: Section 1: Quick Reference |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 41 | &#124; Review status &#124; Not yet reviewed by a French expert-comptable &#124; &#124; | Exact retained currentLF41: Section 1: Quick Reference |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 43 | Mayotte has its own ceiling and its own Smic. This skill covers mainland France and the overseas departments other than Mayotte unless a row says otherwise. | Exact retained currentLF43: Section 1: Quick Reference |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 47 | Since 1 January 2019 the employer withholds income tax from the employee's **net imposable** each month, declares it in the DSN and pays it to the tax administration. Every business that pays salaries taxable in France must collect and pay over the withholding, a foreign employer included. | Exact retained currentLF47: Section 2: Income Tax Withholding (Prélèvement à la Source) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 51 | &#124; Step &#124; Detail &#124; Source &#124; | Exact retained currentLF51: How PAS Works |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 53 | &#124; Rate source &#124; The tax office works out the personalised rate from the employee's own income tax return and sends it to the employer. The employee can see it in their space on impots.gouv.fr &#124; https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 &#124; | Exact retained currentLF53: How PAS Works |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 54 | &#124; When the rate changes &#124; The personalised rate is changed every year in September, from the return filed in the spring &#124; https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 &#124; | Exact retained currentLF54: How PAS Works |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 55 | &#124; Married or PACS couples &#124; A couple taxed jointly gets an individualised rate automatically. It applies only to each person's own income; income common to the household keeps the household rate &#124; https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 &#124; | Exact retained currentLF55: How PAS Works |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 56 | &#124; Rate change on request &#124; A new rate applies at the latest in the third month after the request &#124; https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 &#124; | Exact retained currentLF56: How PAS Works |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 57 | &#124; Change of family situation &#124; The employee must tell the tax administration within 60 days of a marriage, PACS, birth, adoption, death, divorce or end of a PACS &#124; https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 &#124; | Exact retained currentLF57: How PAS Works |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 58 | &#124; No personalised rate &#124; Where the employee has never filed a return, the tax office applies a default rate set by a published grid on the monthly withholding base. See the grid below &#124; https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 &#124; | Exact retained currentLF58: How PAS Works |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 59 | &#124; Calculation &#124; The rate is applied to the monthly withholding base (base mensuelle de prélèvement). On the payslip that base is the net taxable amount shown in zone 6 (Section 7) &#124; https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 &#124; | Exact retained currentLF59: How PAS Works |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 60 | &#124; Remittance &#124; Paid to the tax administration (DGFiP), not to Urssaf, by a SEPA B2B direct debit entered in the financial block of the DSN. The bank account debited is the one the employer registered in its professional space on impots.gouv.fr, and the signed SEPA B2B mandate must reach the bank before the first payment &#124; https://www.impots.gouv.fr/les-modalites-du-prelevement-la-source-0 &#124; | Exact retained currentLF60: How PAS Works |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 62 | The employer never works out the bands. It applies the rate it is given, or the default grid. | Exact retained currentLF62: How PAS Works |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 66 | This scale is what the tax office uses to set the rate. The employer does not use it. It is measured on taxable income per family-quotient share, not on gross salary. | Exact retained currentLF66: Income Tax Brackets (2026, progressive scale for annual declaration) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 68 | &#124; Taxable income per share &#124; Rate &#124; Note &#124; | Exact retained currentLF68: Income Tax Brackets (2026, progressive scale for annual declaration) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 70 | &#124; Source &#124; all figures below &#124; https://www.service-public.gouv.fr/particuliers/vosdroits/F1419 &#124; | Exact retained currentLF70: Income Tax Brackets (2026, progressive scale for annual declaration) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 71 | &#124; Up to EUR 11,600 &#124; 0% &#124; "Jusqu'à 11 600 € 0 %" &#124; | Exact retained currentLF71: Income Tax Brackets (2026, progressive scale for annual declaration) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 72 | &#124; EUR 11,601 to EUR 29,579 &#124; 11% &#124; "De 11 601 € à 29 579 € 11 %" &#124; | Exact retained currentLF72: Income Tax Brackets (2026, progressive scale for annual declaration) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 73 | &#124; EUR 29,580 to EUR 84,577 &#124; 30% &#124; "De 29 580 € à 84 577 € 30 %" &#124; | Exact retained currentLF73: Income Tax Brackets (2026, progressive scale for annual declaration) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 74 | &#124; EUR 84,578 to EUR 181,917 &#124; 41% &#124; "De 84 578 € à 181 917 € 41 %" &#124; | Exact retained currentLF74: Income Tax Brackets (2026, progressive scale for annual declaration) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 75 | &#124; Above EUR 181,917 &#124; 45% &#124; "Plus de 181 917 € 45 %" &#124; | Exact retained currentLF75: Income Tax Brackets (2026, progressive scale for annual declaration) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 77 | These bands apply to the income of 2025 declared in 2026. A payroll run in 2026 does not use them. | Exact retained currentLF77: Income Tax Brackets (2026, progressive scale for annual declaration) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 81 | This is the grid in force from 1 May 2026 for taxpayers living in mainland France or outside France. It is read on the monthly withholding base, which is the net imposable for the month. | Exact retained currentLF81: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 83 | &#124; Monthly withholding base &#124; Default rate &#124; Page wording &#124; | Exact retained currentLF83: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 85 | &#124; Source &#124; all figures below &#124; https://bofip.impots.gouv.fr/bofip/11255-PGP.html &#124; | Exact retained currentLF85: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 86 | &#124; Below EUR 1,635 &#124; 0% &#124; "Inférieure à 1 635 euros 0 %" &#124; | Exact retained currentLF86: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 87 | &#124; EUR 1,635 and below EUR 1,698 &#124; 0.5% &#124; "Supérieure ou égale à 1 635 euros et inférieure à 1 698 euros 0,5 %" &#124; | Exact retained currentLF87: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 88 | &#124; EUR 1,698 and below EUR 1,807 &#124; 1.3% &#124; "Supérieure ou égale à 1 698 euros et inférieure à 1 807 euros 1,3 %" &#124; | Exact retained currentLF88: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 89 | &#124; EUR 1,807 and below EUR 1,928 &#124; 2.1% &#124; "Supérieure ou égale à 1 807 euros et inférieure à 1 928 euros 2,1 %" &#124; | Exact retained currentLF89: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 90 | &#124; EUR 1,928 and below EUR 2,060 &#124; 2.9% &#124; "Supérieure ou égale à 1 928 euros et inférieure à 2 060 euros 2,9 %" &#124; | Exact retained currentLF90: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 91 | &#124; EUR 2,060 and below EUR 2,170 &#124; 3.5% &#124; "Supérieure ou égale à 2 060 euros et inférieure à 2 170 euros 3,5 %" &#124; | Exact retained currentLF91: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 92 | &#124; EUR 2,170 and below EUR 2,315 &#124; 4.1% &#124; "Supérieure ou égale à 2 170 euros et inférieure à 2 315 euros 4,1 %" &#124; | Exact retained currentLF92: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 93 | &#124; EUR 2,315 and below EUR 2,738 &#124; 5.3% &#124; "Supérieure ou égale à 2 315 euros et inférieure à 2 738 euros 5,3 %" &#124; | Exact retained currentLF93: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 94 | &#124; EUR 2,738 and below EUR 3,135 &#124; 7.5% &#124; "Supérieure ou égale à 2 738 euros et inférieure à 3 135 euros 7,5 %" &#124; | Exact retained currentLF94: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 95 | &#124; EUR 3,135 and below EUR 3,571 &#124; 9.9% &#124; "Supérieure ou égale à 3 135 euros et inférieure à 3 571 euros 9,9 %" &#124; | Exact retained currentLF95: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 96 | &#124; EUR 3,571 and below EUR 4,019 &#124; 11.9% &#124; "Supérieure ou égale à 3 571 euros et inférieure à 4 019 euros 11,9 %" &#124; | Exact retained currentLF96: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 97 | &#124; EUR 4,019 and below EUR 4,690 &#124; 13.8% &#124; "Supérieure ou égale à 4 019 euros et inférieure à 4 690 euros 13,8 %" &#124; | Exact retained currentLF97: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 98 | &#124; EUR 4,690 and below EUR 5,624 &#124; 15.8% &#124; "Supérieure ou égale à 4 690 euros et inférieure à 5 624 euros 15,8 %" &#124; | Exact retained currentLF98: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 99 | &#124; EUR 5,624 and below EUR 7,037 &#124; 17.9% &#124; "Supérieure ou égale à 5 624 euros et inférieure à 7 037 euros 17,9 %" &#124; | Exact retained currentLF99: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 100 | &#124; EUR 7,037 and below EUR 8,789 &#124; 20% &#124; "Supérieure ou égale à 7 037 euros et inférieure à 8 789 euros 20 %" &#124; | Exact retained currentLF100: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 101 | &#124; EUR 8,789 and below EUR 12,200 &#124; 24% &#124; "Supérieure ou égale à 8 789 euros et inférieure à 12 200 euros 24 %" &#124; | Exact retained currentLF101: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 102 | &#124; EUR 12,200 and below EUR 16,523 &#124; 28% &#124; "Supérieure ou égale à 12 200 euros et inférieure à 16 523 euros 28 %" &#124; | Exact retained currentLF102: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 103 | &#124; EUR 16,523 and below EUR 25,937 &#124; 33% &#124; "Supérieure ou égale à 16 523 euros et inférieure à 25 937 euros 33 %" &#124; | Exact retained currentLF103: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 104 | &#124; EUR 25,937 and below EUR 55,558 &#124; 38% &#124; "Supérieure ou égale à 25 937 euros et inférieure à 55 558 euros 38 %" &#124; | Exact retained currentLF104: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 105 | &#124; EUR 55,558 and above &#124; 43% &#124; "Supérieure ou égale à 55 558 euros 43 %" &#124; | Exact retained currentLF105: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 107 | Guadeloupe, La Reunion and Martinique have their own grid, and Guyane and Mayotte a third grid. Both are on the same page as the table above. Do not apply the mainland grid to an employee living in those territories. | Exact retained currentLF107: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 109 | **Short contracts: the abattement** | Exact retained currentLF109: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 111 | &#124; Item &#124; Value &#124; Note &#124; | Exact retained currentLF111: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 113 | &#124; Source &#124; all figures below &#124; https://bofip.impots.gouv.fr/bofip/11255-PGP.html &#124; | Exact retained currentLF85: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 114 | &#124; Monthly net taxable Smic at 1 June 2026, the basis of the abattement &#124; EUR 1,531.12 &#124; "Le montant mensuel net imposable du salaire minimum de croissance s’élève, au 1 er juin 2026, à 1 531,12 euros." &#124; | Exact retained currentLF114: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 115 | &#124; Abattement applied to a short contract before the default grid is read &#124; EUR 766 &#124; "est égal à 766 euros (1 531,12 / 2)" &#124; | Exact retained currentLF115: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 121 | &#124; Contribution &#124; Employee rate &#124; Base and page wording &#124; | Exact retained currentLF123: URSSAF Contributions (Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 123 | &#124; Source &#124; all figures below &#124; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html &#124; | Exact retained currentLF125: URSSAF Contributions (Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 124 | &#124; Vieillesse deplafonnee (old age, uncapped) &#124; 0.40% &#124; Total gross. "Assurance vieillesse 0,40 % sur la totalité et 6,90 % dans la limite du plafond" &#124; | Exact retained currentLF126: URSSAF Contributions (Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 125 | &#124; Vieillesse plafonnee (old age, capped) &#124; 6.90% &#124; Up to the monthly ceiling. "0,40 % sur la totalité et 6,90 % dans la limite du plafond" &#124; | Exact retained currentLF127: URSSAF Contributions (Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 126 | &#124; CSG non imposable (deductible from taxable pay) &#124; 6.80% &#124; "CSG non imposable 6,80 % sur 98,25 % du salaire brut dans la limite de 192 240 € en 2026" &#124; | Exact retained currentLF128: URSSAF Contributions (Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 127 | &#124; CSG imposable (not deductible) &#124; 2.40% &#124; "CSG imposable 2,40 % sur 98,25 % du salaire brut dans la limite de 192 240 € en 2026" &#124; | Exact retained currentLF129: URSSAF Contributions (Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 128 | &#124; CRDS &#124; 0.50% &#124; "CRDS 0,50 % sur 98,25 % du salaire brut dans la limite de 192 240 € en 2026" &#124; | Exact retained currentLF130: URSSAF Contributions (Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 129 | &#124; Extra employee health contribution, Haut-Rhin, Bas-Rhin and Moselle only &#124; 1.30% &#124; "Moselle 1,30 %" &#124; | Exact retained currentLF131: URSSAF Contributions (Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 131 | The employee table on that page carries no general health contribution and no unemployment contribution. Do not enter a rate for either. | Exact retained currentLF133: URSSAF Contributions (Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 133 | **The CSG and CRDS base** | Exact retained currentLF135: URSSAF Contributions (Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 135 | &#124; Item &#124; Value &#124; Note &#124; | Exact retained currentLF111: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 137 | &#124; Source &#124; all figures below &#124; https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/csg-crds.html &#124; | Exact retained currentLF139: URSSAF Contributions (Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 138 | &#124; CSG rate on earned income, the two employee lines added by the page &#124; 9.20% &#124; "ce taux est de : 9,20 % pour la CSG ; 0,50 % pour la CRDS" &#124; | Exact retained currentLF140: URSSAF Contributions (Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 139 | &#124; CRDS rate on earned income &#124; 0.50% &#124; "9,20 % pour la CSG ; 0,50 % pour la CRDS" &#124; | Exact retained currentLF141: URSSAF Contributions (Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 140 | &#124; Allowance for professional costs taken off the base &#124; 1.75% &#124; "elle est généralement réduite de 1,75 % au titre des frais professionnels" &#124; | Exact retained currentLF142: URSSAF Contributions (Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 141 | &#124; Share of earned income that is therefore charged &#124; 98.25% &#124; "les CSG-CRDS sont calculées sur 98,25 % des revenus d’activité" &#124; | Exact retained currentLF143: URSSAF Contributions (Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 142 | &#124; Limit beyond which the allowance stops &#124; Four annual social security ceilings. The amount is in the employee table above &#124; "La réduction de 1,75 % ne s’applique toutefois que dans la limite de 4 plafonds annuels de la Sécurité sociale" &#124; | Exact retained currentLF144: URSSAF Contributions (Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 143 | &#124; Employee health contribution where the person is not tax resident in France but is in the French health scheme &#124; 5.50% &#124; "Cette cotisation, au taux de 5,50 %, est à déclarer" &#124; | Exact retained currentLF145: URSSAF Contributions (Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 145 | Conditions that change the answer. The allowance is taken off only up to four annual ceilings; above that the charge is on the whole amount. The employer's contribution to the company health cover is itself charged to CSG and CRDS with no allowance. The charges are due only where the person is resident in France for income tax **and** is covered by a compulsory French health scheme: if only the health test is met, the charges are not due and an employee health contribution is due instead, at the rate in the table above. | Exact retained currentLF147: URSSAF Contributions (Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 149 | &#124; Contribution &#124; Employee rate &#124; Base and page wording &#124; | Exact retained currentLF123: URSSAF Contributions (Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 151 | &#124; Source &#124; all figures below &#124; https://www.service-public.gouv.fr/particuliers/vosdroits/F15396 &#124; | Exact retained currentLF153: AGIRC-ARRCO (Supplementary Pension: Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 152 | &#124; Retraite complementaire, tranche 1 &#124; 3.15% &#124; Annual pay up to EUR 48,060. "7,87 % (part salariale : 3,15 % / part patronale : 4,72 % )" &#124; | Exact retained currentLF154: AGIRC-ARRCO (Supplementary Pension: Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 153 | &#124; Retraite complementaire, tranche 2 &#124; 8.64% &#124; Annual pay between EUR 48,060 and EUR 384,480. "21,59 % (part salariale : 8,64 % / part patronale : 12,95 % )" &#124; | Exact retained currentLF155: AGIRC-ARRCO (Supplementary Pension: Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 154 | &#124; Combined rate, tranche 1 &#124; 7.87% &#124; "7,87 % (part salariale : 3,15 % / part patronale : 4,72 % )" &#124; | Exact retained currentLF156: AGIRC-ARRCO (Supplementary Pension: Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 155 | &#124; Combined rate, tranche 2 &#124; 21.59% &#124; "21,59 % (part salariale : 8,64 % / part patronale : 12,95 % )" &#124; | Exact retained currentLF157: AGIRC-ARRCO (Supplementary Pension: Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 156 | &#124; Rate used to buy pension points, tranche 1 &#124; 6.20% &#124; "Tranche 1 : jusqu'à 48 060 € 6,20 % 20,1877 €" &#124; | Exact retained currentLF158: AGIRC-ARRCO (Supplementary Pension: Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 157 | &#124; Rate used to buy pension points, tranche 2 &#124; 17% &#124; "Tranche 2 : entre 48 060 € et 384 480 € 17 %" &#124; | Exact retained currentLF159: AGIRC-ARRCO (Supplementary Pension: Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 158 | &#124; Price of one pension point in 2026 &#124; EUR 20.1877 &#124; "6,20 % 20,1877 €" &#124; | Exact retained currentLF160: AGIRC-ARRCO (Supplementary Pension: Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 160 | The rate charged and the rate that buys points are different rates. Points are bought at the point rates in the table, not at the contribution rates: the difference funds the scheme and buys nothing. Tranche 2 stops at the ceiling in the table, which is eight annual ceilings. | Exact retained currentLF162: AGIRC-ARRCO (Supplementary Pension: Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 162 | **CEG and CET (employee share)** | Exact retained currentLF164: AGIRC-ARRCO (Supplementary Pension: Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 164 | &#124; Contribution &#124; Employee rate &#124; Base and page wording &#124; | Exact retained currentLF123: URSSAF Contributions (Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 166 | &#124; Source &#124; all figures below &#124; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-particuliers.html &#124; | Exact retained currentLF168: AGIRC-ARRCO (Supplementary Pension: Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 167 | &#124; CEG, tranche 1 &#124; 0.86% &#124; "Contribution d'équilibre générale (CEG) tranche 1 (3) 0,86 % dans la limite du plafond" &#124; | Exact retained currentLF169: AGIRC-ARRCO (Supplementary Pension: Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 168 | &#124; CEG, tranche 2 &#124; 1.08% &#124; "CEG tranche 2 : 1,08 % part salariale et 1,62 % en part patronale" &#124; | Exact retained currentLF170: AGIRC-ARRCO (Supplementary Pension: Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 169 | &#124; CET &#124; 0.14% &#124; "Part salariale à 0,14 % et part patronale à 0,21 %" &#124; | Exact retained currentLF171: AGIRC-ARRCO (Supplementary Pension: Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 171 | The CET condition is easy to get wrong. The page says the CET applies to every employee whose pay is above the social security ceiling, and that it is charged from the first euro, not only on the slice above the ceiling. The page that prints these three rates is the Urssaf rates page for household employers; the general CEG tranche 1 employee rate is confirmed on the Urssaf page for the overtime relief, at https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/exonerations-heures/reduction-cotisations-salariales.html | Exact retained currentLF173: AGIRC-ARRCO (Supplementary Pension: Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 175 | There is no employee unemployment contribution. The Urssaf employee rate table for the private sector lists none, and the Urssaf page on the unemployment and AGS contributions says they are due by employers: https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/assurance-chomage-ags.html Enter nothing for the employee. | Exact retained currentLF177: Chômage (Unemployment: Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 179 | No official page prints a single total for employee deductions, so this skill does not state one. Add the lines in the tables above that apply to the employee, then apply the overtime relief below where overtime was worked. | Exact retained currentLF181: Total Employee Deductions (Approximate) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 181 | **Relief on overtime (employee share)** | Exact retained currentLF183: Total Employee Deductions (Approximate) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 183 | &#124; Item &#124; Value &#124; Note &#124; | Exact retained currentLF111: Taux Neutre (Default Rate Grid, 2026: Metropolitan France) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 185 | &#124; Source &#124; all figures below &#124; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/exonerations-heures/reduction-cotisations-salariales.html &#124; | Exact retained currentLF187: Total Employee Deductions (Approximate) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 186 | &#124; Reduction of employee old-age contributions on overtime and complementary hours, capped &#124; 11.31% &#124; "dans la limite de 11,31 %" &#124; | Exact retained currentLF188: Total Employee Deductions (Approximate) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 187 | &#124; Employee old-age contributions inside that cap &#124; 7.30% &#124; "7,30 % (cotisations salariales vieillesse dont 0,40 % sur la totalité de la rémunération et 6,90 % dans la limite du plafond)" &#124; | Exact retained currentLF189: Total Employee Deductions (Approximate) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 188 | &#124; Agirc-Arrco tranche 1 employee contribution inside that cap &#124; 3.15% &#124; "3,15 % (cotisations salariales de retraite complémentaire sur la tranche 1 (= plafond))" &#124; | Exact retained currentLF190: Total Employee Deductions (Approximate) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 189 | &#124; CEG tranche 1 employee contribution inside that cap &#124; 0.86% &#124; "0,86 % (contribution d’équilibre général (CEG) sur la tranche 1 (= plafond))" &#124; | Exact retained currentLF191: Total Employee Deductions (Approximate) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 191 | The relief is a reduction of the employee's old-age contributions on the overtime pay only. It is not an exemption from CSG or CRDS. The reduction must appear on the payslip. | Exact retained currentLF193: Total Employee Deductions (Approximate) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 197 | &#124; Contribution &#124; Employer rate &#124; Base and page wording &#124; | Exact retained currentLF199: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 199 | &#124; Source &#124; all figures below &#124; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html &#124; | Exact retained currentLF125: URSSAF Contributions (Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 200 | &#124; Maladie, maternite, invalidite, deces, full rate &#124; 13% &#124; Total gross. "Taux réduit à 7 % Taux plein à 13 %" &#124; | Exact retained currentLF202: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 201 | &#124; Maladie, reduced rate, only in the cases in the note below the table &#124; 7% &#124; "Taux réduit à 7 % Taux plein à 13 %" &#124; | Exact retained currentLF203: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 202 | &#124; Pay condition for the reduced 7% maladie rate, where the employer qualifies at all, on https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html &#124; Annual pay at or below 2.5 times the Smic in force on 31 December 2023, a frozen Smic, not the current one &#124; "le taux de la cotisation d’assurance maladie sera de 7 % si la rémunération annuelle du salarié est inférieure ou égale à 2,5 fois le Smic en vigueur au 31/12/2023" &#124; | Exact retained currentLF204: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 203 | &#124; Contribution solidarite autonomie (CSA) &#124; 0.30% &#124; Total gross. "Contribution solidarité autonomie (CSA) 0,30 %" &#124; | Exact retained currentLF205: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 204 | &#124; Vieillesse deplafonnee &#124; 2.11% &#124; Total gross. "Assurance vieillesse 2,11 % sur la totalité et 8,55 % dans la limite du plafond" &#124; | Exact retained currentLF206: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 205 | &#124; Vieillesse plafonnee &#124; 8.55% &#124; Up to the monthly ceiling. "2,11 % sur la totalité et 8,55 % dans la limite du plafond" &#124; | Exact retained currentLF207: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 206 | &#124; Allocations familiales, full rate &#124; 5.25% &#124; Total gross. "Allocations familiales Taux réduit à 3,45 % Taux plein à 5,25 %" &#124; | Exact retained currentLF208: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 207 | &#124; Allocations familiales, reduced rate, only in the cases in the note below the table &#124; 3.45% &#124; "Taux réduit à 3,45 % Taux plein à 5,25 %" &#124; | Exact retained currentLF209: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 208 | &#124; Pay condition for the reduced 3.45% allocations familiales rate, where the employer qualifies at all, on https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html &#124; Annual pay at or below 3.5 times the Smic in force on 31 December 2023, a frozen Smic, not the current one &#124; "le taux de la cotisation d’allocations familiales sera de 3,45 % si la rémunération annuelle du salarié est inférieure ou égale à 3,5 fois le Smic en vigueur au 31/12/2023" &#124; | Exact retained currentLF210: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 209 | &#124; Contribution au dialogue social &#124; 0.016% &#124; Total gross. "Contribution au dialogue social 0,016 %" &#124; | Exact retained currentLF211: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 210 | &#124; Fnal, employer with fewer than 50 employees &#124; 0.10% &#124; Up to the monthly ceiling. "Fnal (effectif de moins de 50 salariés) 0,10 % dans la limite du plafond" &#124; | Exact retained currentLF212: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 211 | &#124; Fnal, employer with 50 employees or more &#124; 0.50% &#124; Total gross. "Fnal (effectif de 50 salariés et plus) 0,50 %" &#124; | Exact retained currentLF213: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 212 | &#124; Contribution formation professionnelle, fewer than 11 employees &#124; 0.55% &#124; "Pour une entreprise de moins de 11 salariés : 0,55 %" &#124; | Exact retained currentLF214: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 213 | &#124; Contribution formation professionnelle, 11 employees or more &#124; 1% &#124; "Pour une entreprise de 11 salariés et plus : 1 %" &#124; | Exact retained currentLF215: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 214 | &#124; Contribution CPF-CDD, on fixed-term contract pay &#124; 1% &#124; "Contribution CPF-CDD 1 %" &#124; | Exact retained currentLF216: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 215 | &#124; Taxe d'apprentissage, main part &#124; 0.59% &#124; "Taxe d'apprentissage Part principale à 0,59 % Solde à 0,09 %" &#124; | Exact retained currentLF217: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 216 | &#124; Taxe d'apprentissage, balance &#124; 0.09% &#124; "Part principale à 0,59 % Solde à 0,09 %" &#124; | Exact retained currentLF218: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 217 | &#124; Taxe d'apprentissage, establishments in Haut-Rhin, Bas-Rhin and Moselle, main part, no balance due &#124; 0.44% &#124; "Part principale à 0,44 % Solde - Néant" &#124; | Exact retained currentLF219: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 218 | &#124; Accident du travail (AT/MP) &#124; Rate notified to the employer by the Carsat &#124; "Accident du travail Taux notifié par la Carsat" &#124; | Exact retained currentLF220: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 219 | &#124; Versement mobilite, employer with 11 employees or more &#124; Rate set locally, look it up with the Urssaf search tool &#124; "Versement mobilité (effectif de 11 salariés et plus)" &#124; | Exact retained currentLF221: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 221 | There is no published national range for the AT/MP rate. Use the rate on the Carsat notification for the establishment and nothing else. | Exact retained currentLF223: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 223 | **Two official pages disagree about the reduced maladie and allocations familiales rates.** The Urssaf rates page above prints them as if they were ordinary alternatives. The Urssaf page on what changed for 2026 says that from 2026 the reduced rates were withdrawn and merged into the single degressive relief below, and survive only for employers using a zoned exemption (ZRR and ZFRR, ZRD, ZFU), the overseas Lodeom exemption, or the exemption for home-help staff placed with a fragile person, and for employees in certain special schemes for whom the single relief is not available. That page is at https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html Where the two conflict, do not assume the reduced rate applies to an ordinary private employer. The same page gives the pay condition, and it is measured against the Smic frozen at 31 December 2023, so it does not move when the Smic rises. | Exact retained currentLF225: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 227 | New for 2026 and the largest single item in French employer cost. The old degressive relief and the reduced maladie and allocations familiales rates were merged into one relief. | Exact retained currentLF229: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 229 | &#124; Item &#124; Value &#124; Page wording &#124; | Exact retained currentLF231: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 231 | &#124; Source &#124; all figures below unless a row names another page &#124; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html &#124; | Exact retained currentLF233: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 232 | &#124; Pay ceiling for eligibility, at the Smic in force on 1 January 2026 &#124; 3 Smic &#124; "a une rémunération inférieure : à 3 Smic applicable au 1 er janvier 2026" &#124; | Exact retained currentLF234: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 233 | &#124; Same ceiling expressed against the Smic in force on 1 June 2026 &#124; 2.9293 Smic &#124; "(ou 2,9293 Smic applicable au 1 er juin 2026)" &#124; | Exact retained currentLF235: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 234 | &#124; Smic value that governs the 2026 coefficient, mainland and overseas departments other than Mayotte &#124; The Smic in force on 1 January 2026 &#124; "En 2026, la valeur du Smic à prendre en compte est celle en vigueur au 1 er janvier 2026" &#124; | Exact retained currentLF236: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 235 | &#124; Official worked example: employer with 70 employees, June 2026, full-time 35 hours, no overtime, monthly gross pay EUR 2,000 &#124; Coefficient 0.3178 &#124; "une rémunération mensuelle brute de 2 000 €, la valeur maximale du coefficient de réduction générale est de 0,3178" &#124; | Exact retained currentLF237: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 236 | &#124; Pay ceiling in Mayotte &#124; 1.6 Smic &#124; "à 1,6 Smic applicable à Mayotte en 2026" &#124; | Exact retained currentLF238: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 237 | &#124; What the Urssaf 2026-news page (informations-nouvelle-annee.html) says the 3-Smic ceiling replaced &#124; 1.6 Smic, the pre-2026 figure &#124; "qui sont inférieurs à 3 Smic en vigueur au lieu de 1,6 Smic auparavant" &#124; | Exact retained currentLF239: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 238 | &#124; What entreprendre.service-public.fr F559, Vérifié le 01 juin 2026, still prints for the general relief &#124; Below 1.6 Smic, EUR 2,987.23 &#124; "Allègements généraux dont bénéficient les employeurs au titre des salariés dont les rémunérations brutes sont inférieures à 1,6 Smic ( 2 987,23 € )" &#124; | Exact retained currentLF240: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 239 | &#124; What the same F559 page prints for the allocations familiales rate reduction, measured against the current Smic rather than the frozen Smic that governs the rate in Section 4 &#124; Below 3.5 Smic, EUR 6,534.56, which is 3.5 times the June 2026 Smic &#124; "Réduction du taux de cotisations allocations familiales, dont bénéficient les employeurs au titre des salariés dont les rémunérations brutes sont inférieures à 3,5 Smic ( 6 534,56 € )" &#124; | Exact retained currentLF241: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 240 | &#124; Maladie rate covered by the relief &#124; 13.00% &#124; "d’assurances sociales (maladie, maternité, invalidité, décès) au taux de 13,00 %" &#124; | Exact retained currentLF242: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 241 | &#124; Vieillesse rate covered &#124; 10.66% &#124; "de vieillesse au taux de 10,66 %" &#124; | Exact retained currentLF243: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 242 | &#124; Allocations familiales rate covered &#124; 5.25% &#124; "d’allocations familiales au taux de 5,25 %" &#124; | Exact retained currentLF244: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 243 | &#124; AT/MP rate covered, capped at the pooled part &#124; 0.49% &#124; "pour sa partie mutualisée au taux de 0,49 %" &#124; | Exact retained currentLF245: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 244 | &#124; Agirc-Arrco rate covered &#124; 6.01% &#124; "de retraite complémentaire légalement obligatoire (Agirc-Arrco) au taux de 6,01 %" &#124; | Exact retained currentLF246: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 245 | &#124; Fnal rate covered, employer with fewer than 50 employees &#124; 0.10% &#124; "de fonds national d’aide au logement (Fnal) au taux de 0,10 % pour les entreprises de moins de 50 salariés" &#124; | Exact retained currentLF247: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 246 | &#124; Fnal rate covered, employer with 50 employees or more &#124; 0.50% &#124; "ou 0,50 % pour les entreprises de 50 salariés et plus ; de solidarité pour l’autonomie" &#124; | Exact retained currentLF248: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 247 | &#124; CSA rate covered &#124; 0.30% &#124; "de solidarité pour l’autonomie (CSA) au taux de 0,30 %" &#124; | Exact retained currentLF249: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 248 | &#124; Unemployment rate covered &#124; 4.00% &#124; "d’assurance chômage au taux de 4,00 %" &#124; | Exact retained currentLF250: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 250 | Two official pages give different ceilings for the general relief. entreprendre.service-public.gouv.fr/vosdroits/F559, Vérifié le 01 juin 2026, still prints 1.6 Smic and EUR 2,987.23. The Urssaf relief and 2026 news pages give 3 Smic, and the news page says the 3 Smic figure replaced 1.6 Smic. Both are in the table above. The Urssaf pages are the ones that describe the 2026 reform by name, but do not treat that as settled without checking the client's own Urssaf account. | Exact retained currentLF252: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 252 | The same F559 page's allocations familiales figure is a second instance of the same problem, not a fresh one: the amount in the row above is 3.5 times the Smic in force on 1 June 2026, while the pay condition for the reduced 3.45% rate above is measured against the Smic frozen at 31 December 2023. F559 has not been updated for the 2026 freeze, the same way it has not been updated for the 1.6-to-3-Smic change. Use the frozen-Smic test in the row above for the reduced rate; treat the F559 figure as the stale, pre-freeze measurement. | Exact retained currentLF254: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 254 | **Coefficient parameters** | Exact retained currentLF256: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 256 | &#124; Item &#124; Employer with fewer than 50 employees &#124; Employer with 50 employees or more &#124; | Exact retained currentLF258: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 258 | &#124; Source &#124; all figures below &#124; https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html &#124; | Exact retained currentLF260: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 259 | &#124; T min &#124; 0.0200 &#124; 0.0200 &#124; | Exact retained currentLF261: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 260 | &#124; T delta &#124; 0.3781 &#124; 0.3821 &#124; | Exact retained currentLF262: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 261 | &#124; Maximum coefficient &#124; 0.3981 &#124; 0.4021 &#124; | Exact retained currentLF263: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 262 | &#124; Exponent P &#124; 1.75 &#124; 1.75 &#124; | Exact retained currentLF264: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 264 | The formula on the Urssaf pages is: coefficient equals T min plus T delta multiplied by the bracketed term raised to the exponent P, where the bracketed term is one half multiplied by (three times the annual Smic, the Smic being increased by the hourly Smic times the number of overtime or complementary hours, divided by annual gross pay, minus one). The relief page says the Smic value may be adjusted for part-time work, a collective working time below the legal one, and suspensions of the contract. For mainland France and the overseas departments other than Mayotte, the Smic to use for the whole of 2026 is the Smic in force on 1 January 2026, so the June rise does not move the relief. The relief page allows the same result with 2.9293 times the annual Smic at its 1 June 2026 value instead of 3 times the January value. The relief page says the Bulletin officiel de la Sécurité sociale (Boss) allows an employer not to apply these formulas to pay of employees whose contract ended between 1 and 30 June 2026, but they apply to the whole of 2026 for every employee still under contract on 1 July 2026. Only in Mayotte are the Smic rises taken into account. Annual gross pay includes a prime de partage de la valeur where one was paid, both for the eligibility test and for the coefficient. | Exact retained currentLF266: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 266 | **Employer relief on overtime** | Exact retained currentLF268: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 268 | &#124; Item &#124; Value &#124; Page wording &#124; | Exact retained currentLF231: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 270 | &#124; Source &#124; all figures below &#124; https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html &#124; | Exact retained currentLF260: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 271 | &#124; Flat employer deduction per overtime hour, employer with fewer than 20 employees &#124; EUR 1.50 &#124; "1,50 € pour les employeurs dont l’effectif est inférieur à 20 salariés" &#124; | Exact retained currentLF273: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 272 | &#124; Flat employer deduction per overtime hour, employer with 20 employees or more &#124; EUR 0.50 &#124; "0,50 € par heure supplémentaire pour les employeurs d’au moins 20 salariés" &#124; | Exact retained currentLF274: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 274 | From 1 January 2026 the old headcount limit for this deduction was removed, so every employer eligible for the single relief can claim it whatever its size. It also covers days bought back from an employee on a forfait-jours contract above the cap of 218 days. | Exact retained currentLF276: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 278 | &#124; Contribution &#124; Employer rate &#124; Base and page wording &#124; | Exact retained currentLF199: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 280 | &#124; Source &#124; all figures below &#124; https://www.service-public.gouv.fr/particuliers/vosdroits/F15396 &#124; | Exact retained currentLF153: AGIRC-ARRCO (Supplementary Pension: Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 281 | &#124; Retraite complementaire, tranche 1 &#124; 4.72% &#124; Annual pay up to EUR 48,060. "7,87 % (part salariale : 3,15 % / part patronale : 4,72 % )" &#124; | Exact retained currentLF283: AGIRC-ARRCO (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 282 | &#124; Retraite complementaire, tranche 2 &#124; 12.95% &#124; Annual pay between EUR 48,060 and EUR 384,480. "21,59 % (part salariale : 8,64 % / part patronale : 12,95 % )" &#124; | Exact retained currentLF284: AGIRC-ARRCO (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 284 | &#124; Contribution &#124; Employer rate &#124; Base and page wording &#124; | Exact retained currentLF199: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 286 | &#124; Source &#124; all figures below &#124; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-particuliers.html &#124; | Exact retained currentLF168: AGIRC-ARRCO (Supplementary Pension: Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 287 | &#124; CEG, tranche 1 &#124; 1.29% &#124; "Contribution d'équilibre générale (CEG) tranche 1 (3) 1,29 % dans la limite du plafond" &#124; | Exact retained currentLF289: AGIRC-ARRCO (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 288 | &#124; CEG, tranche 2 &#124; 1.62% &#124; "CEG tranche 2 : 1,08 % part salariale et 1,62 % en part patronale" &#124; | Exact retained currentLF290: AGIRC-ARRCO (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 289 | &#124; CET &#124; 0.21% &#124; "Part salariale à 0,14 % et part patronale à 0,21 %" &#124; | Exact retained currentLF291: AGIRC-ARRCO (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 290 | &#124; Employer share of the Agirc-Arrco contribution, on https://entreprendre.service-public.gouv.fr/vosdroits/F24013 &#124; 60% &#124; "60 % par l'employeur et 40 % par le salarié" &#124; | Exact retained currentLF292: AGIRC-ARRCO (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 291 | &#124; Employee share of the Agirc-Arrco contribution, on https://entreprendre.service-public.gouv.fr/vosdroits/F24013 &#124; 40% &#124; "60 % par l'employeur et 40 % par le salarié" &#124; | Exact retained currentLF293: AGIRC-ARRCO (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 293 | The same warning as on the employee table applies here. The only allowed page that prints the employer CEG tranche 2 and CET rates is the Urssaf rates page for household employers, in a footnote that states the Agirc-Arrco rules generally. The private-sector rates page prints neither. Confirm the tranche 2 and CET rates against the Agirc-Arrco circular before signing. The 60/40 Agirc-Arrco employer/employee split is confirmed separately, for all private-sector employees and not just household employees, on entreprendre.service-public.gouv.fr/vosdroits/F24013, which is a better source for that split than the household-employer page. | Exact retained currentLF295: AGIRC-ARRCO (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 295 | An Apec contribution is also due for cadres. No allowed official page prints its rate: entreprendre.service-public.gouv.fr/vosdroits/F24013 names "Cotisation Apec (pour les cadres uniquement)" without giving one, which is the evidence for that. This skill does not state one. | Current own Agirc-Arrco source now supplies.06total/.024employee/.036employer up to4PSS; distinct provident minimum remains a precise agreement handoff. Current LF280; LF282; LF283; LF284. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 299 | &#124; Contribution &#124; Employer rate &#124; Base and page wording &#124; | Exact retained currentLF199: URSSAF Contributions (Employer Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 301 | &#124; Source &#124; all figures below &#124; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html &#124; | Exact retained currentLF125: URSSAF Contributions (Employee Share) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 302 | &#124; Assurance chomage &#124; 4.00% &#124; "Contribution assurance chômage 4,00 % dans la limite de 192 240 € en 2026" &#124; | Exact retained currentLF304: Unemployment and Other Employer-Only |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 303 | &#124; Annual pay ceiling for the unemployment and AGS contributions &#124; EUR 192,240 &#124; "dans la limite de 192 240 € en 2026" &#124; | Exact retained currentLF305: Unemployment and Other Employer-Only |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 304 | &#124; AGS &#124; 0.25% &#124; "Dans la limite de 192 240 € en 2026 : 0,25 %" &#124; | Exact retained currentLF306: Unemployment and Other Employer-Only |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 305 | &#124; AGS, temporary work agencies &#124; 0.03% &#124; "0,03 % pour les entreprises de travail temporaire" &#124; | Exact retained currentLF307: Unemployment and Other Employer-Only |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 307 | &#124; Contribution &#124; Employer rate &#124; Page wording &#124; | Exact retained currentLF309: Unemployment and Other Employer-Only |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 309 | &#124; Source &#124; all figures below &#124; https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html &#124; | Exact retained currentLF260: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 310 | &#124; Employer contribution on the part of a rupture conventionnelle or forced retirement payment that is outside the contribution base, for a contract whose end falls after 1 January 2026 &#124; 40% &#124; "Le taux de cette contribution patronale passe de 30 % à 40 %" &#124; | Actual current component destinations LF312, LF314. Exact old wording/figures remain historical; actual current population, year, cap and source limitations control. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 314 | No official page prints a single percentage for total employer cost, so this skill does not state one. Build the cost from the tables above, then deduct the single degressive relief. For pay at or near the Smic the relief cancels most of the employer social cost, and it runs out at the pay ceiling in the relief table. | Exact retained currentLF318: Total Employer Cost (Approximate) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 320 | The minimum wage changed inside the year. Use the value in force on the day the work was done. | Exact retained currentLF324: SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 322 | &#124; Item &#124; Value &#124; Page wording &#124; | Exact retained currentLF231: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 324 | &#124; Source &#124; all figures below &#124; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/montant-smic.html &#124; | Exact retained currentLF328: SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 325 | &#124; Gross hourly, 1 January 2026 to 31 May 2026 &#124; EUR 12.02 &#124; "Smic horaire brut 12,02 € 12,31 €" &#124; | Exact retained currentLF329: SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 326 | &#124; Gross monthly on a 35 hour week, 1 January 2026 to 31 May 2026 &#124; EUR 1,823.03 &#124; "Du 1 er janvier 2026 au 31 mai 2026 Smic horaire brut 12,02 € Smic brut mensuel (base 35 heures par semaine) 1 823,03 €" &#124; | Exact retained currentLF330: SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 327 | &#124; Gross hourly from 1 June 2026 &#124; EUR 12.31 &#124; "Smic horaire brut 12,02 € 12,31 €" &#124; | Exact retained currentLF331: SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 328 | &#124; Gross monthly on a 35 hour week from 1 June 2026 &#124; EUR 1,867.02 &#124; "Au 1 er juin 2026 Smic horaire brut 12,31 € Smic brut mensuel (base 35 heures par semaine) 1 867,02 €" &#124; | Exact retained currentLF332: SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 329 | &#124; Gross hourly from 1 June 2026, employee aged 17 to 18 without six months in the trade &#124; EUR 11.08 &#124; "Smic horaire brut 10,82 € 11,08 €" &#124; | Exact retained currentLF333: SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 330 | &#124; Gross hourly from 1 June 2026, employee under 17 without six months in the trade &#124; EUR 9.85 &#124; "Smic horaire brut 9,62 € 9,85 €" &#124; | Exact retained currentLF334: SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 332 | &#124; Item &#124; Value &#124; Page wording &#124; | Exact retained currentLF231: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 334 | &#124; Source &#124; all figures below &#124; https://www.urssaf.fr/accueil/actualites/augmentation-smic.html &#124; | Exact retained currentLF338: SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 335 | &#124; Gross hourly in Mayotte from 1 June 2026 &#124; EUR 9.56 &#124; "le Smic horaire brut est porté à 9,56 € soit un montant mensuel brut de 1 449,93 €" &#124; | Exact retained currentLF339: SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 336 | &#124; Minimum garanti from 1 June 2026 &#124; EUR 4.35 &#124; "Le minimum garanti s'établit à 4,35 €" &#124; | Exact retained currentLF340: SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 338 | Conditions. The reduced youth rates apply only to an employee under 18 who does not yet have six months of practice in the trade. A collective agreement rate that is higher than the Smic wins. The Smic covers mainland France, Guadeloupe, Guyane, Martinique, La Reunion, Saint-Barthelemy, Saint-Martin and Saint-Pierre-et-Miquelon; Mayotte has its own rate. The June 2026 rise came from the ministerial order of 22 May 2026. No allowed page states the automatic revaluation trigger, so this skill does not state one: check the Urssaf page before each run. | Exact retained currentLF342: SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 340 | Net monthly pay at the Smic is not published as a figure on any allowed page and has been removed from this skill. The monthly net **taxable** Smic at 1 June 2026 is published, in the short-contract table in Section 2. | Exact retained currentLF344: SMIC (Salaire Minimum Interprofessionnel de Croissance, 2026) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 344 | &#124; Rule &#124; Value &#124; Page wording &#124; | Exact retained currentLF348: Working Hours and Overtime |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 346 | &#124; Source &#124; all figures below &#124; https://www.service-public.gouv.fr/particuliers/vosdroits/F1911 &#124; | Exact retained currentLF350: Working Hours and Overtime |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 347 | &#124; Legal weekly hours (duree legale) &#124; 35 hours per week &#124; "35 heures par semaine" &#124; | Exact retained currentLF351: Working Hours and Overtime |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 348 | &#124; Legal monthly hours &#124; 151.67 hours &#124; "151,67 heures par mois" &#124; | Exact retained currentLF352: Working Hours and Overtime |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 349 | &#124; Legal annual hours &#124; 1,607 hours &#124; "1 607 heures par an" &#124; | Exact retained currentLF353: Working Hours and Overtime |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 350 | &#124; Maximum daily working time &#124; 10 hours &#124; "ne doit pas dépasser la durée maximale de 10 heures par jour" &#124; | Exact retained currentLF354: Working Hours and Overtime |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 351 | &#124; Maximum daily working time where activity rises or the business needs it &#124; 12 hours &#124; "la durée maximale quotidienne de travail est limitée à 12 heures par jour" &#124; | Current same substantive Working Hours and Overtime at LF348,LF350,LF351,LF352,LF353,LF354. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 352 | &#124; Maximum in a single week &#124; 48 hours &#124; "Soit 48 heures sur une même semaine" &#124; | Exact retained currentLF356: Working Hours and Overtime |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 353 | &#124; Maximum average over 12 consecutive weeks &#124; 44 hours &#124; "Soit 44 heures par semaine en moyenne sur une période de 12 semaines consécutives" &#124; | Exact retained currentLF357: Working Hours and Overtime |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 355 | &#124; Rule &#124; Value &#124; Page wording &#124; | Exact retained currentLF348: Working Hours and Overtime |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 357 | &#124; Source &#124; all figures below &#124; https://www.service-public.gouv.fr/particuliers/vosdroits/F2391 &#124; | Exact retained currentLF361: Working Hours and Overtime |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 358 | &#124; Overtime premium, first 8 overtime hours in the week, 36th to 43rd hour, where no collective agreement sets a rate &#124; 25% &#124; "25 % pour les 8 premières heures supplémentaires travaillées dans la même semaine (de la 36 e à la 43 e heure)" &#124; | Exact retained currentLF362: Working Hours and Overtime |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 359 | &#124; Overtime premium, hours after that, from the 44th hour, where no collective agreement sets a rate &#124; 50% &#124; "50 % pour les heures suivantes (à partir de la 44 e heure)" &#124; | Exact retained currentLF363: Working Hours and Overtime |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 360 | &#124; Floor for any premium rate set by a collective agreement &#124; 10% &#124; "Chaque taux est au minimum fixé à 10 %" &#124; | Exact retained currentLF364: Working Hours and Overtime |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 361 | &#124; Part-time complementary hours, within one tenth of the contract hours &#124; 10% &#124; "Soit 10 % pour chaque heure complémentaire accomplie dans la limite de 1/10 e" &#124; | Exact retained currentLF365: Working Hours and Overtime |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 362 | &#124; Part-time complementary hours, beyond one tenth &#124; 25% &#124; "Soit 25 % pour chaque heure accomplie au-delà de 1/10 e" &#124; | Exact retained currentLF366: Working Hours and Overtime |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 363 | &#124; Annual overtime quota where no collective agreement sets one &#124; 220 hours &#124; "le nombre maximal d'heures supplémentaires est de 220 heures par salarié et par an" &#124; | Exact retained currentLF367: Working Hours and Overtime |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 365 | Conditions that change the answer. The premiums above are the fallback. Where a collective agreement, a company agreement or an extended branch agreement sets rates, those rates apply and only the floor above binds them. Overtime is counted by calendar week. Where working time is counted by the week or over two weeks, paid leave taken in that period counts as time worked for the overtime count, so the hours the employee would have worked count towards the threshold. Pay for overtime can be replaced in whole or in part by equivalent compensatory rest, and the rest must equal the premium-inclusive pay. The annual quota is also set by agreement first, and the figure above applies only where none of the three kinds of agreement exists. | Exact retained currentLF369: Working Hours and Overtime |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 371 | &#124; Entitlement &#124; Value &#124; Page wording &#124; | Exact retained currentLF375: Congés Payés (Paid Annual Leave) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 373 | &#124; Source &#124; all figures below &#124; https://www.service-public.gouv.fr/particuliers/vosdroits/F2258 &#124; | Exact retained currentLF377: Congés Payés (Paid Annual Leave) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 374 | &#124; Accrual per month of actual work &#124; 2.5 working days &#124; "ouvre droit à un congé de 2,5 jours ouvrables" &#124; | Exact retained currentLF378: Congés Payés (Paid Annual Leave) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 375 | &#124; Full year &#124; 30 working days, five weeks &#124; "30 jours ouvrables (5 semaines) pour une année complète de travail" &#124; | Exact retained currentLF379: Congés Payés (Paid Annual Leave) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 376 | &#124; Accrual during sick leave that is not work related &#124; 2 working days per month, 24 a year &#124; "dans la limite de 2 jours ouvrables par mois (soit 24 jours ouvrables par an)" &#124; | Exact retained currentLF380: Congés Payés (Paid Annual Leave) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 377 | &#124; Reference period &#124; 1 June of year N-1 to 31 May of year N, unless an agreement sets another &#124; "du 1 er juin de l'année N-1 au 31 mai de l'année N" &#124; | Exact retained currentLF381: Congés Payés (Paid Annual Leave) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 378 | &#124; Main leave period &#124; 1 May to 31 October &#124; "du 1 er mai au 31 octobre de l'année en cours" &#124; | Exact retained currentLF382: Congés Payés (Paid Annual Leave) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 379 | &#124; Leave that must be taken in the main period to earn fractionnement days &#124; 12 working days, two weeks &#124; "un congé d'au moins 12 jours ouvrables (soit 2 semaines)" &#124; | Exact retained currentLF383: Congés Payés (Paid Annual Leave) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 381 | A part-day of accrued leave is rounded up to the next whole day. The fractionnement rules themselves are set by the collective agreement. | Current same substantive Congés Payés (Paid Annual Leave) at LF375,LF377,LF378,LF379,LF380,LF381. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 385 | &#124; Item &#124; Value &#124; Page wording &#124; | Exact retained currentLF231: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 387 | &#124; Source &#124; all figures below &#124; https://www.service-public.gouv.fr/particuliers/vosdroits/F3053 &#124; | Exact retained currentLF391: Sick Leave (Arrêt Maladie) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 388 | &#124; Daily allowance from the health scheme &#124; 50% of the daily base salary &#124; "Les indemnités journalières (IJ) sont égales à 50 % du salaire journalier de base" &#124; | Exact retained currentLF392: Sick Leave (Arrêt Maladie) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 389 | &#124; Daily base salary for a monthly paid employee &#124; The last three gross salaries before the stoppage, divided by 91.25 &#124; "au total des 3 derniers salaires bruts perçus avant l'arrêt de travail, divisé par 91,25" &#124; | Exact retained currentLF393: Sick Leave (Arrêt Maladie) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 390 | &#124; Pay taken into account, capped &#124; 1.4 times the Smic in force on the last day of the month before the stoppage. The page states the 2026 cap as EUR 2,613.82 a month, which is built on the Smic in force from 1 June 2026, so it governs a stoppage beginning on or after 1 July 2026 &#124; "est plafonné à 1,4 fois le montant du Smic en vigueur, lors du dernier jour du mois qui précède l'arrêt (soit 2 613,82 € par mois en 2026)" &#124; | Exact retained currentLF394: Sick Leave (Arrêt Maladie) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 391 | &#124; Cap for a stoppage that began before 1 April 2025 &#124; 1.8 times the Smic, the old ceiling &#124; "Pour les arrêts ayant débuté avant le 1ᵉʳ avril 2025, l’ancien plafond reste applicable" &#124; | Exact retained currentLF395: Sick Leave (Arrêt Maladie) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 392 | &#124; Maximum daily allowance &#124; EUR 42.97 &#124; "Les IJ ne peuvent pas dépasser 42,97 € bruts" &#124; | Current same substantive Sick Leave (Arrêt Maladie) at LF389,LF391,LF392,LF393,LF394,LF395. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 393 | &#124; Waiting period before the allowance starts &#124; 3 days &#124; "Les IJ sont versées après un délai de carence de 3 jours" &#124; | Exact retained currentLF397: Sick Leave (Arrêt Maladie) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 395 | **Employer top-up (indemnites complementaires)** | Exact retained currentLF401: Sick Leave (Arrêt Maladie) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 397 | &#124; Seniority &#124; Maximum period paid &#124; Page wording &#124; | Exact retained currentLF403: Sick Leave (Arrêt Maladie) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 399 | &#124; Source &#124; all figures below &#124; https://www.service-public.gouv.fr/particuliers/vosdroits/F3053 &#124; | Exact retained currentLF391: Sick Leave (Arrêt Maladie) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 400 | &#124; 1 to 5 years &#124; 60 days: 30 days at 90% then 30 days at 66.66% &#124; "De 1 à 5 ans 60 jours (30 jours à 90 % et 30 jours à 66,66 % )" &#124; | Exact retained currentLF406: Sick Leave (Arrêt Maladie) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 401 | &#124; 6 to 10 years &#124; 80 days: 40 days at 90% then 40 days at 66.66% &#124; "De 6 à 10 ans 80 jours (40 jours à 90 % et 40 jours à 66,66 % )" &#124; | Exact retained currentLF407: Sick Leave (Arrêt Maladie) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 402 | &#124; 11 to 15 years &#124; 100 days: 50 days at 90% then 50 days at 66.66% &#124; "De 11 à 15 ans 100 jours (50 jours à 90 % et 50 jours à 66,66 % )" &#124; | Exact retained currentLF408: Sick Leave (Arrêt Maladie) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 403 | &#124; 16 to 20 years &#124; 120 days: 60 days at 90% then 60 days at 66.66% &#124; "De 16 à 20 ans 120 jours (60 jours à 90 % et 60 jours à 66,66 % )" &#124; | Exact retained currentLF409: Sick Leave (Arrêt Maladie) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 404 | &#124; 21 to 25 years &#124; 140 days: 70 days at 90% then 70 days at 66.66% &#124; "De 21 à 25 ans 140 jours (70 jours à 90 % et 70 jours à 66,66 % )" &#124; | Exact retained currentLF410: Sick Leave (Arrêt Maladie) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 405 | &#124; 26 to 30 years &#124; 160 days: 80 days at 90% then 80 days at 66.66% &#124; "De 26 à 30 ans 160 jours (80 jours à 90 % et 80 jours à 66,66 % )" &#124; | Exact retained currentLF411: Sick Leave (Arrêt Maladie) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 406 | &#124; 31 years and more &#124; 180 days: 90 days at 90% then 90 days at 66.66% &#124; "31 ans et plus 180 jours (90 jours à 90 % et 90 jours à 66,66 % )" &#124; | Exact retained currentLF412: Sick Leave (Arrêt Maladie) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 407 | &#124; Waiting period before the employer top-up starts, every stoppage &#124; 7 days, so the top-up begins on the 8th day &#124; "Ainsi le versement des indemnités complémentaires commence au 8 e jour de l'arrêt maladie sauf dispositions conventionnelles" &#124; | Corrected: ordinary seven-day waiting excludes the stated work-accident/occupational-disease top-up case. Current same-named section. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 409 | Conditions. The top-up needs at least one year of service at the first day of absence, and the medical certificate must reach **the employer** within 48 hours. Two different waiting periods run at once and must not be confused: three days on the health scheme allowance and seven days on the employer top-up, the top-up beginning on the eighth day unless a collective agreement is more favourable. There is no waiting period on the health scheme allowance where there was a return to work between two stoppages and that return did not exceed 48 hours ("reprise d'activité entre 2 arrêts de travail n'ayant pas dépassé 48 heures"), or where the stoppages follow an affection de longue duree. Where the stoppage follows a work accident or an occupational illness, the allowance runs from the first day of absence. Periods already paid in the previous twelve months reduce what is left. The Smic used for the cap is the one in force on the last day of the month before the stoppage. A stoppage beginning in June 2026 still takes the last day of May, which is inside the January to May Smic period, so its cap is 1.4 times the January 2026 monthly Smic in the Smic table in Section 5, not the monthly cap printed in the table above. No allowed page prints that January-based cap as an amount, so work it from the two figures and show the working. Only a stoppage beginning on or after 1 July 2026 takes the printed cap. | Current same substantive Sick Leave (Arrêt Maladie) at LF389,LF391,LF392,LF393,LF394,LF395. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 413 | &#124; Case &#124; Duration &#124; Page wording &#124; | Exact retained currentLF419: Maternity Leave (Congé de Maternité) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 415 | &#124; Source &#124; all figures below &#124; https://www.service-public.gouv.fr/particuliers/vosdroits/F2265 &#124; | Exact retained currentLF421: Maternity Leave (Congé de Maternité) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 416 | &#124; First child &#124; 6 weeks before, 10 weeks after, 16 weeks in total &#124; "1 er enfant 6 semaines 10 semaines 16 semaines" &#124; | Exact retained currentLF422: Maternity Leave (Congé de Maternité) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 417 | &#124; Second child &#124; 6 weeks before, 10 weeks after, 16 weeks in total &#124; "2 e enfant 6 semaines 10 semaines 16 semaines" &#124; | Exact retained currentLF423: Maternity Leave (Congé de Maternité) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 418 | &#124; Third child or more &#124; 8 weeks before, 18 weeks after, 26 weeks in total &#124; "3 e enfant ou plus 8 semaines 18 semaines 26 semaines" &#124; | Exact retained currentLF424: Maternity Leave (Congé de Maternité) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 419 | &#124; Twins &#124; 12 weeks before, 22 weeks after, 34 weeks in total &#124; "2 12 semaines 22 semaines 34 semaines" &#124; | Exact retained currentLF425: Maternity Leave (Congé de Maternité) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 420 | &#124; Three or more babies &#124; 24 weeks before, 22 weeks after, 46 weeks in total &#124; "3 ou plus 24 semaines 22 semaines 46 semaines" &#124; | Exact retained currentLF426: Maternity Leave (Congé de Maternité) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 422 | The count for a first or second child is by the number of children already dependent before the birth, not by birth order alone. The employee may give up part of the leave but must stop work for at least eight weeks, six of them after the birth. Pay during the leave comes from the health scheme as daily maternity allowances; the contract is suspended and the employer pays no salary unless an agreement says otherwise. No allowed page prints a cap for the maternity allowance, so this skill does not state one. After the maternity leave the employee may take the congé supplémentaire de naissance; its length and pay are on its own service-public page and are not covered here. | Corrected: actual F2265 publishes91.25/PMSS/21% calculation and current104.02; eligibility/datedceiling gates supplied. Current LF419; LF421; LF422; LF423. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 426 | &#124; Item &#124; Duration &#124; Page wording &#124; | Exact retained currentLF432: Paternity Leave (Congé de Paternité) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 428 | &#124; Source &#124; all figures below &#124; https://www.service-public.gouv.fr/particuliers/vosdroits/F3156 &#124; | Exact retained currentLF434: Paternity Leave (Congé de Paternité) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 429 | &#124; Conge de naissance, which must come first &#124; 3 working days &#124; "précédé du congé de naissance d'une durée de 3 jours ouvrables" &#124; | Exact retained currentLF435: Paternity Leave (Congé de Paternité) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 430 | &#124; Conge de paternite et d'accueil de l'enfant, one child &#124; 25 calendar days &#124; "La durée du congé de paternité et d'accueil de l'enfant est de 25 jours calendaires" &#124; | Exact retained currentLF436: Paternity Leave (Congé de Paternité) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 431 | &#124; Conge de paternite et d'accueil de l'enfant, more than one child &#124; 32 calendar days &#124; "La durée du congé de paternité et d'accueil de l'enfant est de 32 jours calendaires" &#124; | Exact retained currentLF437: Paternity Leave (Congé de Paternité) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 432 | &#124; Period the employee must take straight after the conge de naissance &#124; 4 calendar days &#124; "il doit prendre la 1 re période de 4 jours calendaires" &#124; | Exact retained currentLF438: Paternity Leave (Congé de Paternité) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 434 | The leave must be taken within six months of the birth or arrival of the child. After it the employee may take the congé supplémentaire de naissance; its length and pay are on its own service-public page and are not covered here. | Exact retained currentLF440: Paternity Leave (Congé de Paternité) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 438 | No statutory obligation. It is common under collective agreements or company policy. Where it is contractual it is pay: it bears all contributions and it goes into the withholding base. | Exact retained currentLF444: 13th Month (Treizième Mois) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 442 | &#124; Item &#124; Value &#124; Page wording &#124; | Exact retained currentLF231: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 444 | &#124; Source &#124; all figures below &#124; https://entreprendre.service-public.gouv.fr/vosdroits/F33754 &#124; | Exact retained currentLF450: Mutuelle Obligatoire (Compulsory Health Insurance) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 445 | &#124; Minimum employer share of the premium &#124; 50% &#124; "La participation financière de l'employeur doit être au moins égale à 50 % de la cotisation" &#124; | Exact retained currentLF451: Mutuelle Obligatoire (Compulsory Health Insurance) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 446 | &#124; Dental cover in the minimum basket &#124; 125% of the agreed tariff &#124; "Frais dentaires (prothèses et orthodontie) à hauteur de 125 % du tarif conventionnel" &#124; | Exact retained currentLF452: Mutuelle Obligatoire (Compulsory Health Insurance) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 448 | The cover must meet a minimum basket of care: the whole of the ticket moderateur on consultations, acts and services reimbursed by the health scheme, with exceptions; the whole of the daily hospital charge; and the dental and optical minimums. Cover is compulsory for employees except in the cases where an employee is allowed to refuse. Cover carries on after the contract ends, for the length of the last contract and not more than twelve months. The employer's contribution to this cover is itself charged to CSG and CRDS, with no professional-costs allowance. | Current same substantive Mutuelle Obligatoire (Compulsory Health Insurance) at LF448,LF450,LF451,LF452,LF454. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 452 | These are the pay elements most often mis-entered. A benefit in kind is pay and bears contributions; an expense allowance inside the limit does not. The company-car forfait depends on the date the vehicle was first made available to the employee, not the date of the payroll run: a car handed over before 1 February 2025 and still in use is valued on the older, lower schedule below, not on the newer one, even in a 2026 payroll. | Exact retained currentLF458: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 454 | &#124; Item &#124; Value &#124; Page wording &#124; | Exact retained currentLF231: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 456 | &#124; Source &#124; all figures below &#124; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html &#124; | Exact retained currentLF462: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 457 | &#124; Meal provided, one meal &#124; EUR 5.50 &#124; "Montant de l'avantage en 2026 1 repas 5,50 €" &#124; | Exact retained currentLF463: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 458 | &#124; Meal provided, two meals &#124; EUR 11.00 &#124; "2 repas 11,00 €" &#124; | Exact retained currentLF464: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 459 | &#124; Luncheon voucher, maximum exempt employer share &#124; EUR 7.32 &#124; "Exonération maximale de la part patronale 7,32 €" &#124; | Exact retained currentLF465: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 460 | &#124; Luncheon voucher face value that carries the maximum exemption, lower end &#124; EUR 12.20 &#124; "Entre 12,20 € et 14,64 €" &#124; | Exact retained currentLF466: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 461 | &#124; Luncheon voucher face value that carries the maximum exemption, upper end &#124; EUR 14.64 &#124; "Entre 12,20 € et 14,64 €" &#124; | Exact retained currentLF467: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 462 | &#124; Company car, vehicle made available since 1 February 2025, bought, five years old or less &#124; 15% of the purchase cost &#124; "Véhicule acheté âgé de 5 ans ou moins 15 % du coût d'achat" &#124; | Exact retained currentLF468: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 463 | &#124; Same car, employer pays the private fuel &#124; 20% of the purchase cost &#124; "15 % du coût d'achat + frais réels sur factures de carburant utilisé à des fins personnelles ou 20 % du coût d'achat" &#124; | Exact retained currentLF469: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 464 | &#124; Company car, vehicle made available since 1 February 2025, bought, more than five years old &#124; 10% of the purchase cost &#124; "Véhicule acheté de plus de 5 ans 10 % du coût d'achat" &#124; | Exact retained currentLF470: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 465 | &#124; Same car, employer pays the private fuel &#124; 15% of the purchase cost &#124; "10 % du coût d'achat + frais réels sur factures de carburant utilisé à des fins personnelles ou 15 % du coût d'achat" &#124; | Exact retained currentLF471: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 466 | &#124; Company car, vehicle made available since 1 February 2025, leased &#124; 50% of the yearly total cost &#124; "Véhicule loué ou en location avec option d’achat (LOA) 50 % du coût global annuel (location, entretien, assurance)" &#124; | Exact retained currentLF472: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 467 | &#124; Same car, employer pays the private fuel &#124; 67% of the yearly total cost &#124; "50 % du coût global annuel (location, entretien, assurance) + frais réels sur factures de carburant utilisé à des fins personnelles ou 67 % du coût global" &#124; | Exact retained currentLF473: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 468 | &#124; Company car, vehicle made available before 1 February 2025, bought, five years old or less &#124; 9% of the purchase cost &#124; "Véhicule acheté âgé de 5 ans ou moins 9 % du coût d'achat" &#124; | Exact retained currentLF474: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 469 | &#124; Same car, employer pays the private fuel &#124; 12% of the purchase cost &#124; "9 % du coût d'achat + frais réels sur factures de carburant utilisé à des fins personnelles ou 12 % du coût d'achat" &#124; | Exact retained currentLF475: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 470 | &#124; Company car, vehicle made available before 1 February 2025, bought, more than five years old &#124; 6% of the purchase cost &#124; "Véhicule acheté de plus de 5 ans 6 % du coût d'achat" &#124; | Exact retained currentLF476: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 471 | &#124; Same car, employer pays the private fuel &#124; 9% of the purchase cost &#124; "6 % du coût d'achat + frais réels sur factures de carburant utilisé à des fins personnelles ou 9 % du coût d'achat" &#124; | Exact retained currentLF477: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 472 | &#124; Company car, vehicle made available before 1 February 2025, leased &#124; 30% of the yearly total cost &#124; "Véhicule loué ou en location avec option d’achat (LOA) 30 % du coût global annuel TTC (location, entretien, assurance)" &#124; | Exact retained currentLF478: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 473 | &#124; Same car, employer pays the private fuel &#124; 40% of the yearly total cost &#124; "30 % du coût global annuel TTC (location, entretien, assurance) + frais de carburant sur facture o u 4 0 % du coût global" &#124; | Exact retained currentLF479: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 474 | &#124; Leased company car, either schedule, cap &#124; Capped at the amount the benefit would have been if the employer had bought the vehicle instead of leasing it &#124; "L'avantage évalué pour un véhicule loué est plafonné au montant de l'avantage en nature qui aurait été évalué si l'employeur avait acheté le véhicule" &#124; | Exact retained currentLF480: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 475 | &#124; Electric vehicle, made available since 1 February 2025, meeting the environmental score required for the bonus écologique &#124; 70% reduction of the benefit on the schedule above, the reduction being limited to EUR 4,641.60 a year in 2026 &#124; "Si le véhicule respecte le score environnemental requis pour bénéficier du bonus écologique, vous utilisez le barème ci-dessus auquel vous appliquez une réduction de 70 % sur le montant de l’avantage en nature, dans la limite de 4 641,60 € par an en 2026" &#124; | Exact retained currentLF481: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 476 | &#124; Electric vehicle made available before 1 February 2025 &#124; 50% reduction of the benefit on the schedule above, the reduction being limited to EUR 2,026.30 a year in 2026 &#124; "Vous utilisez le barème ci-dessus auquel vous appliquez une réduction de 50 %, dans la limite de 2 026,30 € par an en 2026" &#124; | Exact retained currentLF482: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 477 | &#124; Electric vehicle, either schedule &#124; Electricity the employer pays for is excluded from the benefit-in-kind calculation &#124; "Les frais d'électricité pris en charge par l’employeur n’entrent pas en compte dans le calcul de l’avantage en nature" &#124; | Exact retained currentLF483: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 479 | &#124; Item &#124; Value &#124; Page wording &#124; | Exact retained currentLF231: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 481 | &#124; Source &#124; all figures below &#124; https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/frais-professionnels.html &#124; | Exact retained currentLF487: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 482 | &#124; Meal allowance, employee forced to eat at the workplace &#124; EUR 7.50 &#124; "Salarié contraint de prendre son repas sur le lieu de travail 7,50 €" &#124; | Exact retained currentLF488: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 483 | &#124; Meal allowance, employee travelling and forced to eat in a restaurant &#124; EUR 21.40 &#124; "Salarié en situation de déplacement contraint de prendre son repas au restaurant 21,40 €" &#124; | Exact retained currentLF489: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 484 | &#124; Meal allowance, employee travelling but not forced to eat in a restaurant &#124; EUR 10.40 &#124; "non contraint de prendre son repas au restaurant 10,40 €" &#124; | Exact retained currentLF490: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 485 | &#124; Telework allowance, no collective agreement, per day &#124; EUR 2.70 &#124; "Par jour de télétravail 2,70 € dans la limite de 59,40 € par mois" &#124; | Exact retained currentLF491: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 486 | &#124; Telework allowance, no collective agreement, monthly cap &#124; EUR 59.40 &#124; "2,70 € dans la limite de 59,40 € par mois" &#124; | Exact retained currentLF492: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 487 | &#124; Telework allowance under a collective agreement, per day &#124; EUR 3.30 &#124; "Par jour de télétravail 3,30 € dans la limite de 72,60 € par mois" &#124; | Exact retained currentLF493: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 488 | &#124; Telework allowance under a collective agreement, monthly cap &#124; EUR 72.60 &#124; "3,30 € dans la limite de 72,60 € par mois" &#124; | Exact retained currentLF494: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 490 | &#124; Item &#124; Value &#124; Page wording &#124; | Exact retained currentLF231: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 492 | &#124; Source &#124; all figures below &#124; https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/prime-partage-valeur.html &#124; | Exact retained currentLF498: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 493 | &#124; Prime de partage de la valeur, exempt from contributions up to &#124; EUR 3,000 &#124; "exonérée de cotisations et contributions sociales dans la limite de 3 000 €" &#124; | Exact retained currentLF499: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 494 | &#124; Same cap where the employer has a profit-sharing scheme in the conditions on the page &#124; EUR 6,000 &#124; "Cette limite d’exonération passe à 6 000 € par bénéficiaire et par an" &#124; | Exact retained currentLF500: Avantages en Nature and Frais Professionnels |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 495 | &#124; Forfait social on the prime, employer with the headcount stated on the page &#124; 20% &#124; "le forfait social au taux de 20 % est dû si l’effectif de votre entreprise est égal ou sup" &#124; | Current same substantive Avantages en Nature and Frais Professionnels at LF458,LF460,LF462,LF463,LF464,LF465. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 497 | The prime de partage de la valeur counts in annual gross pay for the single degressive relief, whether or not it is paid into a savings plan. | Current same substantive Avantages en Nature and Frais Professionnels at LF458,LF460,LF462,LF463,LF464,LF465. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 501 | The bulletin de paie is governed by the Code du travail. The list below is the list the official page gives. | Exact retained currentLF507: Section 7: Payslip Requirements |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 505 | &#124; Zone &#124; Required fields &#124; | Exact retained currentLF511: Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 507 | &#124; Zone 1, identification of employer and employee &#124; Employer name and address, and the establishment the employee belongs to; the APE or NAF activity code and the employer's Siret; the applicable branch collective agreement, or a reference to the Code du travail on leave and notice; the employee's name, job and position in the agreement's classification; the period and the number of hours worked, separating normal hours from overtime and showing the rate applied to each; the nature and volume of the forfait for an employee on a forfait contract; the nature of the basis of pay where that basis is not working time; and the nature and amount of any salary accessories bearing contributions &#124; | Exact retained currentLF513: Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 508 | &#124; Zone 2, pay &#124; The employee's gross pay; the base and amount of the employer's and the employee's contributions before exemptions are deducted; the employee's contribution rates before exemptions are deducted; the nature and amount of other payments and deductions, in particular the home-to-work transport reimbursement; the amount actually received by the employee; the date of payment; and, where a period of annual leave falls in the pay period, the leave dates and the amount of the holiday pay &#124; | Exact retained currentLF514: Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 509 | &#124; Zone 3, contributions and reliefs &#124; Contributions and contributions grouped under five headings, health, work accidents and occupational illness, retirement, family and unemployment, with base, rate and amount; the total of exemptions and reliefs; the total paid by the employer; and the line for the change in pay caused by removing the employee unemployment and health contributions &#124; | Exact retained currentLF515: Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 510 | &#124; Zone 4, net to pay and net taxable &#124; Net to pay before income tax, and the income tax withheld at source &#124; | Exact retained currentLF516: Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 511 | &#124; Zone 5, montant net social &#124; Net income after all compulsory social deductions, the figure the employee reports to the family allowance fund &#124; | Exact retained currentLF517: Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 512 | &#124; Zone 6, income tax &#124; Net taxable amount used as the withholding base, its year to date total, the tax withheld, its year to date total, and the net exempt amount of overtime and complementary hours with its year to date total &#124; | Exact retained currentLF518: Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 513 | &#124; Zone 7, final wording &#124; A pointer to the payslip page on the service-public portal, the wording telling the employee to keep the payslip with no time limit, and, where short-time working applies, the number of hours compensated &#124; | Exact retained currentLF519: Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 515 | Source for this list: https://entreprendre.service-public.gouv.fr/vosdroits/F559 | Exact retained currentLF521: Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 517 | The montant net social line and the seven-zone layout came in with the version of the payslip that applies since 1 July 2023. The page also sets out the earlier layout that applies since 2022. Special rules apply to employees in the local health scheme of Haut-Rhin, Bas-Rhin and Moselle: only the employee rate and the employee share are shown. | Exact retained currentLF523: Mandatory Payslip Fields (Seven-Zone Layout since 1 July 2023) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 521 | - Electronic delivery is the rule and paper the exception, since 2017. This is the opposite of the old position. The employee can refuse electronic delivery and must tell the employer. | Exact retained currentLF527: Delivery |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 522 | - The employer must keep a copy at the business for five years, on paper or electronically. | Exact retained currentLF528: Delivery |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 523 | - After those five years the payslips need not be reachable inside the business, but they must not be destroyed, and the employer must guarantee the employee can get them either for fifty years from issue or for six years after the employee retires. | Exact retained currentLF529: Delivery |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 524 | - The employee can challenge the amount or the accuracy of a payslip for three years from the day it was handed over. | Exact retained currentLF530: Delivery |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 525 | - There is no legal duty on the employer to issue a duplicate of a lost payslip. | Exact retained currentLF531: Delivery |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 527 | &#124; Item &#124; Value &#124; Page wording &#124; | Exact retained currentLF231: Réduction Générale Dégressive Unique (RGDU) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 529 | &#124; Source &#124; all figures below &#124; https://entreprendre.service-public.gouv.fr/vosdroits/F559 &#124; | Exact retained currentLF535: Delivery |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 530 | &#124; Fine the employer can be ordered to pay for each payslip not handed over &#124; EUR 450 &#124; "une amende pouvant atteindre 450 € par fiche non remise" &#124; | Exact retained currentLF536: Delivery |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 536 | &#124; Obligation &#124; Deadline &#124; Page wording &#124; | Exact retained currentLF542: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 538 | &#124; Source &#124; all figures below unless a row names another page &#124; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html &#124; | Exact retained currentLF544: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 539 | &#124; Employer with 50 employees or more, pay run in the same month as the work &#124; The 5th of the following month &#124; "vous devez transmettre votre DSN liée à la paie du mois en cours, le 5 du mois suivant (M+1)" &#124; | Exact retained currentLF545: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 540 | &#124; Employer with 50 employees or more, pay run in the month after the work (decalage de paie) &#124; At the latest the 15th of the following calendar month &#124; "au plus tard le 15 du mois civil suivant" &#124; | Exact retained currentLF546: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 541 | &#124; Employer with fewer than 50 employees &#124; At the latest the 15th of the following calendar month &#124; "Vous devez transmettre votre DSN liée à la paie du mois en cours, au plus tard le 15 du mois civil suivant" &#124; | Exact retained currentLF547: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 542 | &#124; Employer with fewer than 11 employees, quarterly option &#124; F24013 says such a business may choose to file the DSN each quarter instead of each month, at the latest the 15th of the month after the work period; the same page also says it may exceptionally choose to pay each quarter. Confirm with Urssaf which of the two the client has opted for before moving any monthly filing. Source: entreprendre.service-public.gouv.fr/vosdroits/F24013 &#124; "Les entreprises de moins de 11 salariés peuvent choisir d'effectuer la DSN chaque trimestre et non chaque mois." / "Les entreprises de moins de 11 salariés qui déclarent en DSN chaque trimestre, doivent aussi le faire au plus tard le 15 du mois suivant la période de travail effectuée." &#124; | Corrected monthly filing versus quarterly payment, same sources. Current LF542; LF544; LF545; LF546. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 543 | &#124; Deadline falling on a public holiday or a non-working day &#124; Extended to the next working day &#124; "il est prolongé" &#124; | Exact retained currentLF549: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 544 | &#124; Event report (signalement d'evenement): sick leave, end of contract &#124; Within 5 days of the event &#124; "vous êtes tenu d’envoyer une DSN de signalement d'événement dans les 5 jours suivants" &#124; | Current same substantive Monthly: DSN (Déclaration Sociale Nominative) at LF542,LF544,LF545,LF546,LF547,LF548. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 546 | The condition the live text used to miss: the 5th is not simply the large-employer date. It applies only where the employer has 50 employees or more **and** pays in the same month as the work. An employer of that size that pays in the following month is on the 15th, like a smaller employer. An employer with fewer than 11 employees may, on the wording of F24013, choose to file quarterly, also by the 15th of the month after the work period (see the warning in the row above). | Corrected: monthly filing underR133-14/R243-6-1, separate quarterly payment; F24013 contrary wording retained. Current LF542; LF544; LF545; LF546. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 548 | **Penalties** | Exact retained currentLF554: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 550 | &#124; Failure &#124; Penalty &#124; Page wording &#124; | Exact retained currentLF556: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 552 | &#124; Source &#124; all figures below &#124; https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html &#124; | Exact retained currentLF558: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 553 | &#124; Filing outside the DSN channel &#124; 0.5% of the monthly social security ceiling per employee &#124; "0,5 % du plafond mensuel de la Sécurité sociale (PMSS) par salarié" &#124; | Exact retained currentLF559: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 554 | &#124; Same, cap where the employer has at least 2,000 employees &#124; EUR 10,000 &#124; "montant plafonné à 10 000 € si vous employez au moins 2 000 salariés" &#124; | Exact retained currentLF560: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 555 | &#124; Same, cap where the employer has fewer than 2,000 employees &#124; EUR 750 &#124; "montant plafonné à 750 € par entreprise si vous employez un nombre inférieur à 2 000 salariés" &#124; | Exact retained currentLF561: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 556 | &#124; Late filing &#124; 1.5% of the monthly ceiling per employee per month or part month late &#124; "1,5 % du plafond mensuel de la Sécurité sociale par salarié et par mois ou fraction de mois de retard" &#124; | Exact retained currentLF562: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 557 | &#124; Late filing, cap where the delay is five days or less &#124; 150% of the monthly ceiling per business, once a calendar year &#124; "Montant plafonné à 150 % PMSS par entreprise si défaut de production inférieur ou égal à 5 jours" &#124; | Exact retained currentLF563: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 558 | &#124; Employees left out of the filing &#124; 1.5% of the monthly ceiling per employee per month or part month, capped at 150% of the monthly ceiling per business if the failure is corrected within 5 days, once a calendar year &#124; "omission de salariés ou assimilés : 1,5 % du plafond mensuel de la Sécurité sociale par salarié" / "Montant plafonné à 150 % PMSS par entreprise si défaut de production inférieur ou égal à 5 jours" &#124; | Exact retained currentLF564: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 559 | &#124; Other omissions, including employer identification data &#124; 0.5% of the monthly ceiling per employee &#124; "autres cas : 0,5 % du plafond mensuel de la Sécurité sociale par salarié" &#124; | Exact retained currentLF565: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 560 | &#124; Pay reported wrongly so that contributions come out too low &#124; 1% of the monthly ceiling per employee &#124; "1 % du plafond mensuel de la Sécurité sociale par salarié ou assimilé" &#124; | Exact retained currentLF566: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 561 | &#124; Other inaccuracies &#124; 0.33% of the monthly ceiling per employee &#124; "autres cas : 0,33 % du plafond mensuel de la Sécurité sociale par salarié" &#124; | Exact retained currentLF567: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 562 | &#124; Correcting figure below which late interest and the penalty are not applied, where errors are not repeated &#124; 5% of the total initial contributions &#124; "le versement régularisateur est inférieur à 5 % du montant total des cotisations initiales" &#124; | Exact retained currentLF568: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 564 | The EUR 10,000 and EUR 750 caps on filing outside the DSN channel apply to employers within the scope of the décret of 24 September 2014. A third cap applies to employers within the scope of the décret of 18 May 2016: EUR 750 per business, per month. | Exact retained currentLF570: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 566 | An omission or an inaccuracy carries no penalty where the employer corrects it within 30 days of the filing that carried it. Urssaf sends a compte-rendu metier within four hours of the filing, and more anomalies can be flagged five days after the deadline. Separately, the droit à l'erreur applies only where the employer corrects the pay at the nearest declarative deadline and pays the top-up contributions and social charges at the same time; on that condition it removes the majorations and the penalty where either limb is met, provided the inaccuracies are not repetitive: the majorations and penalty that would otherwise apply come to less than one monthly value of the social security ceiling, or the regularising payment is below 5% of the total initial contributions. | Not yet confirmed: historical four-hour/five-day CRM service levels; current actual rapid-feedback wording retained. Current LF542; LF544; LF545; LF546. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 568 | **Penalties on the employer as collector of the income tax withheld** | Exact retained currentLF574: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 570 | Those Urssaf penalties are about the social contributions. The income tax withheld carries a separate set of penalties under the tax code, which the tax administration's own doctrine sets out. The administrative fines in the first six rows below are exclusive of one another and do not stack. That exclusivity covers only those fines, the ones under CGI art. 1759-0 A. The late-payment surcharge and the criminal penalties are separate charges and the page does not say they are excluded by them. | Exact retained currentLF576: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 572 | &#124; Failure &#124; Penalty &#124; Page wording &#124; | Exact retained currentLF556: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 574 | &#124; Source &#124; all figures below &#124; https://bofip.impots.gouv.fr/bofip/11471-PGP.html &#124; | Exact retained currentLF580: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 575 | &#124; Inaccuracy or omission, where the return was filed on time &#124; 5% of the withholding that should have been made or declared &#124; "l’amende est de 5 % des retenues qui auraient dû être effectuées ou déclarées lorsque la déclaration a été déposée dans les délais" &#124; | Exact retained currentLF581: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 576 | &#124; Inaccuracy or omission that was deliberate &#124; 40% &#124; "Le taux de l’amende est porté à 40 % en cas d'inexactitudes ou d'omissions délibérées" &#124; | Exact retained currentLF582: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 577 | &#124; Return not filed by the deadline &#124; 10% of the withholding that should have been made or declared &#124; "l’amende s’élève à 10 % des retenues qui auraient dû être effectuées ou déclarées" &#124; | Exact retained currentLF583: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 578 | &#124; Still not filed within thirty days of a formal notice &#124; 40% &#124; "L’amende est portée à 40 % des retenues qui auraient dû être effectuées ou déclarées en cas de non-dépôt de la déclaration dans les trente jours suivant une mise en demeure" &#124; | Exact retained currentLF584: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 579 | &#124; Withholding made but deliberately not declared and not paid over &#124; 80% of the withholding made &#124; "une amende égale à 80 % des retenues effectuées" &#124; | Exact retained currentLF585: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 580 | &#124; Floor for any of these fines &#124; EUR 250 per return &#124; "l’amende est au minimum égale à 250 € par déclaration" &#124; | Exact retained currentLF586: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 581 | &#124; Late payment of the withholding &#124; The surcharge in CGI art. 1731. The worked example on the page applies 5% of the unpaid amount &#124; "une majoration égale à 5 % du montant non payé" &#124; | Exact retained currentLF587: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 582 | &#124; Withholding kept back deliberately, delay over one month, criminal fine &#124; EUR 1,500 &#124; "passible d’une amende de 1 500 €" &#124; | Exact retained currentLF588: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 583 | &#124; Repeat within three years &#124; Two years imprisonment and a fine of EUR 3,750, or one of the two &#124; "punissable de deux ans d'emprisonnement et de 3 750 € d'amende" &#124; | Exact retained currentLF589: Monthly: DSN (Déclaration Sociale Nominative) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 585 | The two deliberate-breach fines in the table above apply only where the administration shows the breach was deliberate. Where only part of a return is filed late, the on-time inaccuracy fine applies to that part and the non-filing fine does not. The converse also holds: where the administration finds an omission or an inaccuracy on a return that was itself filed late, only the 10% non-filing fine applies to the whole of the withholding not declared in time. | Current same substantive Monthly: DSN (Déclaration Sociale Nominative) at LF542,LF544,LF545,LF546,LF547,LF548. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 589 | &#124; Obligation &#124; Deadline &#124; Notes &#124; | Exact retained currentLF595: Annual |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 591 | &#124; DADS &#124; Not applicable, fully replaced by the DSN since 2019 &#124; Historical reference only &#124; | Exact retained currentLF597: Annual |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 592 | &#124; Index de l'égalité professionnelle &#124; Each year, at the latest 1 March, on the company website and on Égapro &#124; Businesses with at least 50 employees over the past year. A business that has just reached 50 employees has three years before it must publish. Source: https://entreprendre.service-public.gouv.fr/vosdroits/F35103 &#124; | Exact retained currentLF599: Annual |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 596 | &#124; Item &#124; Detail &#124; | Exact retained currentLF603: Employee Obligations |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 598 | &#124; Declaration de revenus &#124; Annual, in the spring, pre-filled with the withholding data &#124; | Exact retained currentLF605: Employee Obligations |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 599 | &#124; Adjustment &#124; Where the rate was wrong, the balance is settled through the avis d'imposition &#124; | Exact retained currentLF606: Employee Obligations |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 600 | &#124; Rate maintenance &#124; The employee, not the employer, tells the tax office about a change of family situation, within 60 days &#124; | Exact retained currentLF607: Employee Obligations |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 606 | &#124; Pattern &#124; Classification &#124; | Exact retained currentLF613: Typical Bank Statement Descriptions (Salary Credits) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 608 | &#124; VIREMENT SALAIRE, VIR SALAIRE &#124; Net salary payment &#124; | Exact retained currentLF615: Typical Bank Statement Descriptions (Salary Credits) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 609 | &#124; SALAIRE plus the employer name &#124; Net salary payment &#124; | Exact retained currentLF616: Typical Bank Statement Descriptions (Salary Credits) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 610 | &#124; INDEMNITE CONGES PAYES &#124; Holiday pay, where paid separately &#124; | Exact retained currentLF617: Typical Bank Statement Descriptions (Salary Credits) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 611 | &#124; PRIME 13E MOIS &#124; Thirteenth month bonus &#124; | Exact retained currentLF618: Typical Bank Statement Descriptions (Salary Credits) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 612 | &#124; PRIME PARTICIPATION, INTERESSEMENT &#124; Profit sharing, separate tax and social rules &#124; | Exact retained currentLF619: Typical Bank Statement Descriptions (Salary Credits) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 613 | &#124; IJSS, CPAM INDEMNITE &#124; Sickness or maternity daily allowance from the health scheme &#124; | Exact retained currentLF620: Typical Bank Statement Descriptions (Salary Credits) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 614 | &#124; PRIME PARTAGE VALEUR, PPV &#124; Prime de partage de la valeur &#124; | Exact retained currentLF621: Typical Bank Statement Descriptions (Salary Credits) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 618 | &#124; Pattern &#124; Classification &#124; | Exact retained currentLF613: Typical Bank Statement Descriptions (Salary Credits) |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 620 | &#124; URSSAF COTISATIONS &#124; Monthly social contribution payment &#124; | Exact retained currentLF627: Typical Employer Debit Patterns |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 621 | &#124; AGIRC-ARRCO COTISATIONS &#124; Supplementary pension contributions &#124; | Exact retained currentLF628: Typical Employer Debit Patterns |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 622 | &#124; DGFIP PAS, PRELEVEMENT SOURCE &#124; Income tax withheld and paid over &#124; | Exact retained currentLF629: Typical Employer Debit Patterns |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 623 | &#124; MUTUELLE plus the insurer name &#124; Compulsory health cover premium &#124; | Exact retained currentLF630: Typical Employer Debit Patterns |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 624 | &#124; PREVOYANCE plus the insurer name &#124; Provident insurance premium &#124; | Exact retained currentLF631: Typical Employer Debit Patterns |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 628 | &#124; Scenario &#124; Skill to use &#124; | Exact retained currentLF635: Section 10: Interaction with Other Skills |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 630 | &#124; Employee payroll, contributions and withholding &#124; This skill, `france-payroll` &#124; | Exact retained currentLF637: Section 10: Interaction with Other Skills |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 631 | &#124; Self-employed income tax, including auto-entrepreneur and micro-entrepreneur &#124; `fr-income-tax` &#124; | Exact retained currentLF638: Section 10: Interaction with Other Skills |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 632 | &#124; Income tax for an employee's own household return &#124; `fr-personal-income-tax` &#124; | Exact retained currentLF639: Section 10: Interaction with Other Skills |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 633 | &#124; Social contributions of a self-employed person &#124; `fr-social-contributions` &#124; | Exact retained currentLF640: Section 10: Interaction with Other Skills |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 634 | &#124; TVA, French VAT &#124; `france-vat-return` &#124; | Exact retained currentLF641: Section 10: Interaction with Other Skills |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 635 | &#124; Bookkeeping &#124; `france-bookkeeping` &#124; | Exact retained currentLF642: Section 10: Interaction with Other Skills |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 636 | &#124; Electronic invoicing, Factur-X and Chorus Pro &#124; `france-einvoice` &#124; | Exact retained currentLF643: Section 10: Interaction with Other Skills |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 640 | - **Payroll to bookkeeping.** Gross wages and employer charges are profit and loss expenses. Employee deductions and the tax withheld are liabilities in the 43x accounts until the DSN payment clears. Employer contributions are booked to 645xxx. | Corrected: social liabilities43x, PAS4421; exact PCG labels linked. Current LF647; LF648; LF649. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 641 | - **Payroll to income tax.** Withholding settles most of the employee's income tax in real time. The annual return may still produce an adjustment. The net imposable on the payslip is the reference figure. | Exact retained currentLF648: Key Handoff Points |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 642 | - **Payroll to the DSN.** All payroll data feeds the DSN. Accurate payslips give an accurate DSN. Errors produce anomaly reports through net-entreprises.fr. | Exact retained currentLF649: Key Handoff Points |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 646 | 1. **Fix the gross and the pay elements.** Add base pay, overtime at the premium in the overtime table in Section 5 or at the collective agreement rate, bonuses, and benefits in kind at the values in Section 6. Check the result against the Smic in force on the days worked, using the table at https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/montant-smic.html Expense allowances inside the limits on https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/frais-professionnels.html stay out of the base. | Exact retained currentLF653: The method, step by step |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 647 | 2. **Split the gross across the ceilings.** Work out tranche 1 and tranche 2 against the monthly ceiling at https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/plafonds-securite-sociale.html and prorate the ceiling with the daily and hourly values in the same table for a part month or a short contract. | Corrected: ordinary monthly ceiling is monthlyPMSS×calendar-employment-days/calendar-month-days; daily220/hourly30 are not that formula. Current LF653; LF654; LF655; LF656. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 648 | 3. **Apply the employee contributions.** Use the employee table in Section 3 and the Agirc-Arrco tables, from https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html and https://www.service-public.gouv.fr/particuliers/vosdroits/F15396 Charge CSG and CRDS on the reduced base in the CSG table, watching the four-ceiling limit. Apply the overtime relief from https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/exonerations-heures/reduction-cotisations-salariales.html | Exact retained currentLF655: The method, step by step |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 649 | 4. **Apply the employer contributions, then the single degressive relief.** Use the employer table in Section 4, then compute the relief with the coefficient parameters at https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html Check eligibility against the pay ceiling in that table before computing anything. | Exact retained currentLF656: The method, step by step |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 650 | 5. **Compute the net imposable and withhold the income tax.** Net imposable is the gross less the deductible social contributions. Apply the rate the tax office sent through the DSN feedback, or, where there is none, the grid at https://bofip.impots.gouv.fr/bofip/11255-PGP.html taking the grid for the territory where the employee lives. The tax withheld is paid to the tax administration by the SEPA B2B debit set in the DSN, as described at https://www.impots.gouv.fr/les-modalites-du-prelevement-la-source-0 | Current same substantive The method, step by step at LF653,LF654,LF655,LF656,LF657,LF658. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 651 | 6. **Issue the payslip.** Build the seven zones listed in Section 7 from https://entreprendre.service-public.gouv.fr/vosdroits/F559 including the montant net social line and the year to date totals. | Exact retained currentLF658: The method, step by step |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 652 | 7. **File the DSN and pay.** File on net-entreprises.fr by the date in the DSN table in Section 8, from https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html Read the compte-rendu metier and correct by an annule et remplace before the due date. Send an event report within five days of a sick leave or an end of contract. | Current same substantive The method, step by step at LF653,LF654,LF655,LF656,LF657,LF658. Earlier wording is preserved here; current source/figure/year qualifiers control, not a claim every old number is unchanged. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 656 | - **How many employees does the business have, and does it pay in the month of the work or the month after?** This decides the DSN date, the Fnal rate, the training contribution rate, the flat overtime deduction, and which coefficient row of the single degressive relief applies. | Exact retained currentLF707: Ask the client first |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 657 | - **Is the employee resident in France for income tax, and in a compulsory French health scheme?** Both tests must be met for CSG and CRDS. If only the health test is met, an employee health contribution replaces them. | Exact retained currentLF708: Ask the client first |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 658 | - **Where does the employee live and work?** Mayotte has its own ceiling and its own Smic. Guadeloupe, La Reunion, Martinique, Guyane and Mayotte have their own default withholding grids. Haut-Rhin, Bas-Rhin and Moselle carry an extra employee health contribution and a different apprenticeship tax. | Exact retained currentLF709: Ask the client first |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 659 | - **Which collective agreement applies?** It can raise the minimum pay above the Smic, change the overtime premiums and the annual quota, change the reference period for leave, and require the employer to keep paying during maternity or sickness. | Exact retained currentLF710: Ask the client first |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 660 | - **Does the employer use a zoned exemption, the overseas Lodeom exemption, or the home-help exemption, and is the employee's annual pay at or below the pay ceiling in Section 4 (2.5 times the frozen Smic for maladie, 3.5 times for allocations familiales)?** Both the exemption and the pay ceiling must be met; that is now the only ordinary route to the reduced maladie and allocations familiales rates. | Exact retained currentLF711: Ask the client first |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 661 | - **Was any pay paid in a month when the Smic changed, or any prime de partage de la valeur paid in the year?** Both change the single degressive relief. | Current actualJanuary/June gross rates retained; RGDU uses ownJanuaryfreeze. Current LF324; LF326; LF328; LF329. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 665 | - Any payroll for a special scheme, for example SNCF, RATP, the electricity and gas industries, the mines, the clercs et employes de notaires, or seafarers. The rates and the relief are different and are not in this skill. | Exact retained currentLF716: When to refuse or refer |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 666 | - Payroll in Mayotte beyond the ceiling and the Smic quoted here. The contribution rates are a separate schedule. | Exact retained currentLF717: When to refuse or refer |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 667 | - Household employers, childminders and home-help staff: they use the Urssaf schedule for particuliers employeurs, not the private-sector schedule. | Exact retained currentLF718: When to refuse or refer |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 668 | - Apprentices, professionalisation contracts, interns and company officers, where the base and the exemptions are not the ones in this skill. | Exact retained currentLF719: When to refuse or refer |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 669 | - Cadres benefits: the Apec contribution and the minimum provident cover for cadres come from national agreements, not from the pages allowed here. Ask the expert-comptable or read the collective agreement. | Current own Agirc-Arrco source now supplies.06total/.024employee/.036employer up to4PSS; distinct provident minimum remains a precise agreement handoff. Current LF280; LF282; LF283; LF284. |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 670 | - Termination pay: severance, rupture conventionnelle and transactional payments have their own exemption limits. Only the employer contribution rate is in this skill. | Exact retained currentLF721: When to refuse or refer |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 671 | - Any case where a collective agreement, an extended branch agreement or a company agreement is in play and has not been read. | Exact retained currentLF722: When to refuse or refer |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 672 | - Any figure a client wants to rely on without a French expert-comptable signing it off. | Exact retained currentLF723: When to refuse or refer |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 676 | - Never work out income tax bands by hand for the withholding. Use the rate the tax office sends, or the default grid in Section 2. | Exact retained currentLF727: PROHIBITIONS |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 677 | - Never apply the professional-costs allowance to CSG and CRDS above four annual ceilings, and never apply it to the employer's contribution to the company health cover. | Exact retained currentLF728: PROHIBITIONS |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 678 | - Never mix up tranche 1 and tranche 2 for Agirc-Arrco, and never charge the CET only on the slice above the ceiling: it is charged from the first euro once pay passes the ceiling. | Exact retained currentLF729: PROHIBITIONS |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 679 | - Never leave the compulsory health cover out of employer cost. | Exact retained currentLF730: PROHIBITIONS |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 680 | - Never enter an employee unemployment contribution. The private-sector employee table lists none. | Exact retained currentLF731: PROHIBITIONS |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 681 | - Never assume the reduced maladie or allocations familiales rate for an ordinary private employer in 2026. Check the exemption list and the pay ceiling against the Smic frozen at 31 December 2023 first. | Exact retained currentLF732: PROHIBITIONS |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 682 | - Never quote a total employer cost or a total employee deduction percentage. No allowed page prints one. | Exact retained currentLF733: PROHIBITIONS |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 683 | - Never issue a payslip missing a field from the seven zones in Section 7. | Exact retained currentLF734: PROHIBITIONS |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 684 | - Never miss a DSN deadline. The penalties are shares of the monthly ceiling, set out in Section 8. | Exact retained currentLF735: PROHIBITIONS |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 685 | - Never forget that the Smic changed on 1 June 2026. Check which rate covers the days worked. | Exact retained currentLF736: PROHIBITIONS |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 686 | - Never present a payroll computation as final. Send it to an expert-comptable for sign-off. | Exact retained currentLF737: PROHIBITIONS |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 690 | - https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/plafonds-securite-sociale.html | Exact retained currentLF741: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 691 | - https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/montant-smic.html | Exact retained currentLF742: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 692 | - https://www.urssaf.fr/accueil/actualites/augmentation-smic.html | Exact retained currentLF743: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 693 | - https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html | Exact retained currentLF744: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 694 | - https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-particuliers.html | Exact retained currentLF745: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 695 | - https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/csg-crds.html | Exact retained currentLF746: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 696 | - https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/assurance-chomage-ags.html | Exact retained currentLF747: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 697 | - https://www.impots.gouv.fr/les-modalites-du-prelevement-la-source-0 | Exact retained currentLF748: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 698 | - https://entreprendre.service-public.gouv.fr/vosdroits/F35103 | Exact retained currentLF749: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 699 | - https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html | Exact retained currentLF750: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 700 | - https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/exonerations-heures/reduction-cotisations-salariales.html | Exact retained currentLF751: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 701 | - https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/prime-partage-valeur.html | Exact retained currentLF752: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 702 | - https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html | Exact retained currentLF753: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 703 | - https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/avantages-en-nature.html | Exact retained currentLF754: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 704 | - https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/frais-professionnels.html | Exact retained currentLF755: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 705 | - https://www.urssaf.fr/accueil/employeur/gerer-entreprise/declaration-sociale-nominative.html | Exact retained currentLF756: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 706 | - https://entreprendre.service-public.gouv.fr/vosdroits/F559 | Exact retained currentLF757: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 707 | - https://entreprendre.service-public.gouv.fr/vosdroits/F24013 | Exact retained currentLF758: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 708 | - https://entreprendre.service-public.gouv.fr/vosdroits/F33754 | Exact retained currentLF759: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 709 | - https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 | Exact retained currentLF760: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 710 | - https://www.service-public.gouv.fr/particuliers/vosdroits/F1419 | Exact retained currentLF761: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 711 | - https://www.service-public.gouv.fr/particuliers/vosdroits/F15396 | Exact retained currentLF762: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 712 | - https://www.service-public.gouv.fr/particuliers/vosdroits/F1911 | Exact retained currentLF763: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 713 | - https://www.service-public.gouv.fr/particuliers/vosdroits/F2391 | Exact retained currentLF764: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 714 | - https://www.service-public.gouv.fr/particuliers/vosdroits/F2258 | Exact retained currentLF765: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 715 | - https://www.service-public.gouv.fr/particuliers/vosdroits/F3053 | Exact retained currentLF766: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 716 | - https://www.service-public.gouv.fr/particuliers/vosdroits/F2265 | Exact retained currentLF767: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 717 | - https://www.service-public.gouv.fr/particuliers/vosdroits/F3156 | Exact retained currentLF768: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 718 | - https://bofip.impots.gouv.fr/bofip/11255-PGP.html | Exact retained currentLF769: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 719 | - https://bofip.impots.gouv.fr/bofip/11471-PGP.html | Exact retained currentLF770: Sources |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 723 | This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an expert-comptable in France) before implementation. | Exact retained currentLF777: Disclaimer |
| 62b7639a5a68324a83a96bb0190fff8b7c76f8c5 / 725 | The most up-to-date version of this skill is maintained by OpenAccountants. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes. | Exact retained currentLF779: Disclaimer |
