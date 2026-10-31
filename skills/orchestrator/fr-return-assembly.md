---
name: fr-return-assembly
description: Final orchestrator skill that assembles the complete French filing package for France-resident self-employed individuals, micro-entrepreneurs, and sole proprietors. Consumes outputs from all French content skills (france-tva for TVA CA3/CA12, france-income-tax for 2042/2042-C-PRO/2035/2031, france-cotisations for URSSAF/SSI, fr-estimated-tax for prélèvement à la source) to produce a single unified reviewer package containing every worksheet, every form, every brief section, all cross-skill reconciliations, and the final action list with payment instructions, filing instructions, and next-year planning. This is the capstone skill that runs last and produces the final deliverable. MUST be loaded alongside all French content skills listed above. France full-year residents only. Self-employed individuals, micro-entrepreneurs, and sole proprietors only.
version: 1.1
jurisdiction: FR
tax_year: 2026
last_updated: 2026-10-31
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# France: assembling the self-employed filing package (return assembly)

This skill runs last in the French self-employed stack. It takes the outputs of the content skills, checks them against each other, and assembles one reviewer package and one client action list for a France-resident micro-entrepreneur, entrepreneur individuel or profession libérale. Figures are for tax year 2026. The income tax return filed in spring 2026 (form 2042 with the 2042-C-PRO) covers income of 2025, so the income tax scale, the family-quotient cap, the décote, the micro limits tested on 2023 and 2024 turnover and the 2023 reference-income test for the flat income tax payment govern that return, while the VAT franchise thresholds, the micro-entrepreneur contribution rates, the micro limits for receipts of 2026, the CFE payment dates and the withholding rate applied from September 2026 are those in force during 2026. VAT and social contribution rules are stated as in force on 19 October 2026, read on official pages saved between 19 September and 19 October 2026. By that date the 2026 filing window for 2025 income has closed: a package built now serves a late return, a correction through the online correction service, or the planning of 2026 income that will be declared in 2027.

## How this workflow runs

- **Execute all steps without pausing for permission.** Intake and the content skills have already collected the facts for this working paper. Use what they captured, and ask the user again only where something is missing or contradicts itself. Do NOT ask the user "how deep do you want me to go" or "do you want the full package" or any variant. The user asked for their tax returns. Produce them. Do NOT announce how many tokens or tool calls this will take. Do NOT ask which deliverables to prioritise. Produce all deliverables listed in Section 4. If you run out of context mid-execution, finish the computation work first (numbers, positions, flags), then produce whatever formatted outputs you can, and at the very end state clearly which deliverables were not produced and why.
- **Do NOT re-validate scope that intake already validated.** If `fr-freelance-intake` produced an intake package, trust it. You can cross-check specific numbers during reconciliation, but do not re-interrogate the user about residency, business structure or anything else intake already captured.
- **Do NOT pause between content skills to check in.** Run them in dependency order (Section 2) without status updates between each one. A single status message at the end is fine.
- **Self-checks are targets, not blockers.** If a self-check fails, note it in the reviewer brief's open flags section and continue. Do NOT halt the whole workflow because one self-check had an ambiguous answer.
- **Citations go in the final reviewer brief**, not in intermediate computation steps. The user has already been told by the intake skill that the final package needs sign-off by an expert-comptable before filing. State it once in the final output and move on.
- **Failure mode to avoid:** the skill halts mid-execution and asks the user a meta-question about workflow pacing. If you feel the urge to ask "how should I proceed", pick the most defensible path, proceed, and flag the decision in the reviewer brief so the reviewer can challenge it.

## What this file is

The final capstone skill for French self-employed returns. Every French content skill feeds into this one. The output is the complete reviewer package that an expert-comptable can review, sign off and deliver to the client with filing instructions.

This skill coordinates the content skills, checks that their outputs agree, and assembles the final deliverable. It does not restate their rules in full: where a figure below is used for a cross-check, the content skill named next to it holds the full rule.

## Section 1: Scope

- **Who:** full-year France residents who are self-employed: micro-entrepreneurs (auto-entrepreneurs), entrepreneurs individuels au réel, professions libérales, and a single-member EURL taxed to income tax.
- **Which year:** income of 2025, declared in 2026 (revenus 2025). 2026 appears only as planning and as the rules in force today.
- **Which filings:** the déclaration de revenus (2042 and 2042-C-PRO), the VAT position (CA3, CA12 or the franchise en base check), the reconciliation of social contributions with URSSAF, the CFE, and the update of the prélèvement à la source (PAS) rate.

## Section 2: Execution order and dependency chain

The skill runs the content skills in this order.

1. **VAT step (`france-vat-return`).** VAT return or franchise en base check. It runs first because the turnover it confirms feeds the income tax declaration. Under the réel normal regime, check or prepare the CA3 returns. Under the réel simplifié regime, check or prepare the annual CA12 and the two instalments. Under the franchise en base, test turnover against the thresholds in the franchise table below and flag any business that crossed one, because VAT then applies (from 1 January of the next year for the basic threshold, from the first day of the overrun for the higher one). `france-vat-return` refuses franchise businesses for the return itself: it still holds the thresholds. Output: VAT collected, VAT deductible, balance, turnover excluding VAT confirmed, any VAT credit.
2. **Income tax step (`fr-income-tax`, with `fr-personal-income-tax` for the household computation).** The 2042 and 2042-C-PRO, and the professional return (2035 or 2031) if the business is au réel. The turnover excluding VAT must agree with the VAT step. Micro path: the box map in the 2042-C-PRO table below, with the flat allowance of the activity applied automatically. Réel path: the 2035 for BNC or the 2031 for BIC, carried to the 2042-C-PRO. Then the family quotient, the scale, the family-quotient cap and the décote. Output: revenu net imposable, impôt brut, impôt net, balance to pay or refund.
3. **Social contributions step (`fr-social-contributions`).** Micro-entrepreneur: a single rate on turnover collected, from the micro-entrepreneur table below. Self-employed au réel: provisional contributions based on earlier income, then a regularisation. From the regularisation of the 2025 contributions, after the 2025 income declaration filed in 2026, URSSAF computes contributions and the CSG-CRDS on one reformed base (see the reform table below). Output: contributions due, payments made, shortfall or overpayment, the deductible CSG from the URSSAF attestation.
4. **Withholding step (`fr-income-tax`, prélèvement à la source).** A self-employed person pays the tax on business income through instalments (acomptes) that the tax administration debits from the bank account, monthly or, under conditions, quarterly. The 2025 return updates the rate applied from September 2026. Output: updated PAS rate, the instalments for the rest of 2026 and for 2027, and whether a modulation request makes sense.

- **CFE (`fr-cfe`).** Run alongside the income tax step: amount, payment dates, first-year exemption.
- **Upstream failure handling.** If a content skill fails to produce validated output, note the failure in the reviewer brief and continue with the data available rather than halting.

**Micro regime: limits, allowances and the flat income tax payment**

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F23267 |  |
| Income received in 2025: overall turnover limit (tested on 2024 or 2023) | EUR 188,700 | "ne doit pas avoir dépassé 188 700 €" | https://entreprendre.service-public.gouv.fr/vosdroits/F23267 |
| Income received in 2025: services and BNC turnover limit (tested on 2024 or 2023) | EUR 77,700 | "ne doit pas avoir dépassé 77 700 €" | same |
| Income received in 2026: sales of goods and accommodation limit (tested on 2025 or 2024) | EUR 203,100 | "n’a pas dépassé 203 100 €" | same |
| Income received in 2026: services and BNC limit (tested on 2025 or 2024) | EUR 83,600 | "n’a pas dépassé 83 600 €" | same |
| Flat allowance, sales of goods and accommodation (BIC) | 71% | "Le taux d'abattement est de 71 %" | same (2026) |
| Flat allowance, services (BIC) | 50% | "Le taux d'abattement est de 50 %" | same (2026) |
| Flat allowance, liberal activity (BNC) | 34% | "Le taux d'abattement est de 34 %" | same (2026) |
| Minimum allowance | EUR 305 | "Le montant de l’abattement ne peut pas être inférieur à 305 €" | same (2026) |
| Flat income tax payment rate, trade, catering and accommodation | 1% | "1 % pour les activités de commerce, restauration et logement" | same (2026) |
| Flat income tax payment rate, other BIC activities | 1.7% | "1,7 % pour les autres activités relevant des BIC" | same (2026) |
| Flat income tax payment rate, BNC | 2.2% | "ce taux est de 2,2 %" | same (2026) |
| Flat income tax payment: household reference income of year N-2 must be below (page says 'inférieur à'), single person | EUR 29,579 | "29 579 € pour une personne seule" | same (2026) |
| Flat income tax payment: household reference income of year N-2 must be below, couple in one tax household | EUR 59,158 | "59 158 € pour une personne en couple" | same (2026) |

The micro regime is lost only where a limit was crossed in BOTH of the two earlier years: the page says the receipts of year N leave the micro regime "uniquement si l’un des seuils a été dépassé pendant 2 années consécutives, en N-1 et en N-2". The allowance replaces actual costs: "ce ne sont donc pas les charges réelles qui sont déduites".

The flat-payment limit is tied to the scale. The brochure defines it as the top of the second band of the scale of year N-2 ('la limite supérieure de la deuxième tranche du barème de l'impôt sur les revenus de l'année 2023, soit 28 797 €' for 2025 income). F23267 prints 29 579 € against 'l'année N-2' without naming the year of the option; impots.gouv.fr prints a different amount for the option taken in 2026, in the table below. Test each year against the brochure rule and the two pages, and flag the disagreement; `fr-freelance-intake` carries both figures.

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/particulier/questions/comment-declarer-les-revenus-provenant-de-mon-activite-dauto-entrepreneur |  |
| Option taken in 2026: 2024 reference income must be below, single person (1 share) | EUR 29,315 | "opter pour le « versement libératoire » auprès de l’Urssaf en 2026 ... Votre revenu fiscal de référence (RFR) de 2024 est inférieur au plafond suivant : 29 315 € pour une personne seule (1 part)" | https://www.impots.gouv.fr/particulier/questions/comment-declarer-les-revenus-provenant-de-mon-activite-dauto-entrepreneur |
| Option taken in 2026: same test, couple (2 shares) | EUR 58,630 | "58 630 € pour un couple (2 parts)" | same |

**The 2042-C-PRO for income of 2025: boxes and the flat-payment test**

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/11-revenus_non_salaries_161a182.pdf |  |
| Flat income tax payment on 2025 income: 2023 reference income per family-quotient share must not exceed | EUR 28,797 | "28 797 €. Cette limite est majorée de 50 % par demi-part" | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/11-revenus_non_salaries_161a182.pdf |
| Increase of that limit per extra half share | 50% | "28 797 €. Cette limite est majorée de 50 % par demi-part" | same (income of 2025) |

Box map from the same brochure chapter (declarant 1 shown; declarant 2 and dependants use the next letters):

- Micro-BIC without the flat payment: sales at 5KO, services and furnished lettings at 5KP (the brochure refers to the "chiffre d’affaires déclaré lignes 5KO à 5MO ou 5KP à 5MP").
- Micro-BNC without the flat payment: receipts collected in 2025 at 5HQ ("lignes 5HQ, 5IQ, 5JQ le montant des recettes encaissées en 2025").
- Micro-entrepreneur with the flat payment: BIC sales at 5TA, BIC services at 5TB, BNC at 5TE. For the BIC boxes the brochure says the turnover is the one already shown to URSSAF "dans les déclarations mensuelles ou trimestrielles souscrites".
- Réel BNC (déclaration contrôlée): revenus imposables at 5QC. Réel BIC: revenus imposables at 5KC.

The option for the flat payment is made with URSSAF before 30 September to apply the following year; the brochure's own example is that for 2026 income the option had to be made by 30 September 2025.

**Income tax scale applied in 2026 to income of 2025, per family-quotient share**

| Band of taxable income per share | Rate | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.service-public.gouv.fr/particuliers/vosdroits/F1419 |  |
| Up to EUR 11,600 | 0% | "Jusqu'à 11 600 € 0 %" | https://www.service-public.gouv.fr/particuliers/vosdroits/F1419 (income of 2025) |
| From EUR 11,601 to EUR 29,579 | 11% | "De 11 601 € à 29 579 € 11 %" | same (income of 2025) |
| From EUR 29,580 to EUR 84,577 | 30% | "De 29 580 € à 84 577 € 30 %" | same (income of 2025) |
| From EUR 84,578 to EUR 181,917 | 41% | "De 84 578 € à 181 917 € 41 %" | same (income of 2025) |
| Above EUR 181,917 | 45% | "Plus de 181 917 € 45 %" | same (income of 2025) |

**Family-quotient cap for income of 2025**

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/2494-PGP.html/identifiant=BOI-IR-LIQ-20-20-20-20260407 |  |
| Maximum tax saving per extra half share (general case) | EUR 1,807 | "Son montant est fixé à 1 807 € par demi-part supplémentaire" | https://bofip.impots.gouv.fr/bofip/2494-PGP.html/identifiant=BOI-IR-LIQ-20-20-20-20260407 (income of 2025) |

**Décote for income of 2025**

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/2495-PGP.html/identifiant=BOI-IR-LIQ-20-20-30-20260407 |  |
| Gross tax must be below, single, divorced or widowed | EUR 1,982 | "inférieure à 1 982 € pour les contribuables célibataires, divorcés ou veufs" | https://bofip.impots.gouv.fr/bofip/2495-PGP.html/identifiant=BOI-IR-LIQ-20-20-30-20260407 (income of 2025) |
| Gross tax must be below, couple taxed jointly | EUR 3,277 | "et à 3 277 € pour les contribuables soumis à imposition commune" | same (income of 2025) |

The other family-quotient caps (single parent, shared custody, the extra reductions) and the décote formula are in `fr-personal-income-tax`.

## Section 3: Cross-skill reconciliation

### Cross-check 1: VAT turnover matches the income declaration

| VAT output | Income tax input | Rule |
| --- | --- | --- |
| CA3 or CA12 total turnover excluding VAT | 2042-C-PRO declared turnover, or 2035 or 2031 receipts | Must match to the euro, or the difference is explained |
| Franchise en base: turnover declared | 2042-C-PRO micro boxes (5KO, 5KP, 5HQ, or 5TA, 5TB, 5TE with the flat payment) | Turnover declared to URSSAF equals turnover on the 2042-C-PRO |
| Réel: turnover excluding VAT from the VAT returns | 2035 receipts or 2031 turnover | VAT-declared and income-declared turnover must reconcile |

If they do not match, flag it for the reviewer. Common causes: receipts basis against invoice basis (cash against accrual timing), credit notes (avoirs), and foreign income outside French VAT.

**VAT franchise en base thresholds in force for 2026**

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F21746 |  |
| Trade and accommodation: prior-year turnover at or below | EUR 85,000 | "est inférieur ou égal à 85 000 € (seuil de la franchise en base de TVA)" | https://entreprendre.service-public.gouv.fr/vosdroits/F21746 (2026) |
| Trade and accommodation: current-year turnover at or below (higher threshold) | EUR 93,500 | "est inférieur ou égal à 93 500 € (seuil majoré de la franchise en base de TVA)" | same (2026) |
| Services and liberal professions: prior-year turnover at or below | EUR 37,500 | "est inférieur ou égal à 37 500 € (seuil de la franchise en base de TVA)" | same (2026) |
| Services and liberal professions: current-year turnover at or below (higher threshold) | EUR 41,250 | "est inférieur ou égal à 41 250 € (seuil majoré de la franchise en base de TVA)" | same (2026) |

The page says these thresholds are unchanged for 2026 and that the single lower threshold proposed by the 2025 finance law "a été abandonnée". Separate thresholds apply to lawyers, authors and performers: take them from `france-vat-return`. Crossing the higher threshold brings VAT "dès le 1 er jour de dépassement".

### Cross-check 2: turnover declared to URSSAF matches the income declaration

| URSSAF input | Income tax input | Rule |
| --- | --- | --- |
| Micro-entrepreneur: total turnover declared monthly or quarterly | 2042-C-PRO micro boxes | Must match exactly |
| Self-employed au réel: the income used for the contribution base | 2035 or 2031 result | From the 2025 regularisation the base is the reformed single base in the table below, not the old base that added the contributions back |

If they do not match, check timing first. The micro-entrepreneur declares turnover collected (encaissé) to URSSAF, monthly or quarterly, even when it is nil. If the 2042-C-PRO equals the URSSAF total, the check passes. If not, reconcile and explain the difference.

**Micro-entrepreneur contribution rates in force in 2026**

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/lessentiel-du-statut.html |  |
| Purchase and resale of goods (BIC) | 12.3% | "Achat/revente de marchandises (BIC) 12,3 %" | https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/lessentiel-du-statut.html (2026) |
| Commercial and craft services, including furnished lettings of all kinds and chambres d'hôtes, but not classified tourist lettings, which have their own rate on the page (BIC) | 21.2% | "Prestations de services commerciales et artisanales (BIC) 10,6% 15,9% 21,2%" | same (2026) |
| Other services (BNC), general scheme | 25.6% | "Autres prestations de services (BNC) 25,6 %" | same (2026) |
| Regulated liberal professions attached to the Cipav | 23.2% | "Professions libérales réglementées relevant de la Cipav (BIC et BNC) 23,2 %" | same (2026) |
| Acre rate, goods, activity started up to 30 June 2026 | 6.2% | "Vente de marchandises ( BIC ) 6,2% 9,3% 12,3%" | same |
| Acre rate, goods, activity started from 1 July 2026 | 9.3% | "Vente de marchandises ( BIC ) 6,2% 9,3% 12,3%" | same |
| Acre rate, BIC services, activity started up to 30 June 2026 | 10.6% | "Prestations de services commerciales et artisanales (BIC) 10,6% 15,9% 21,2%" | same |
| Acre rate, BIC services, activity started from 1 July 2026 | 15.9% | "Prestations de services commerciales et artisanales (BIC) 10,6% 15,9% 21,2%" | same |
| Acre rate, BNC, activity started up to 30 June 2026 | 12.8% | "Autres prestations de services ( BNC ) 12,8% 19,2% 25,6%" | same |
| Acre rate, BNC, activity started from 1 July 2026 | 19.2% | "Autres prestations de services ( BNC ) 12,8% 19,2% 25,6%" | same |
| Acre rate, Cipav, activity started up to 30 June 2026 | 13.4% | "Professions libérales relevant de la Cipav (BNC) 13,4%* 17,4% 23,2%" | same |
| Acre rate, Cipav, activity started from 1 July 2026 | 17.4% | "Professions libérales relevant de la Cipav (BNC) 13,4%* 17,4% 23,2%" | same |
| Training contribution, craftsmen | 0.3% | "Taux Artisans 0,3 % Commerçants 0,1 %" | same (2026) |
| Training contribution, traders | 0.1% | "Artisans 0,3 % Commerçants 0,1 %" | same (2026) |
| Training contribution, liberal professions | 0.2% | "Professions libérales réglementées et professions libérales non réglementées 0,2 %" | same (2026) |

The page heads the full rates "A compter du 1/01/2026": they are the rates in force during 2026, for mainland France (the page prints separate overseas rates). For turnover collected in 2025, take the rate from the client's URSSAF statements and `fr-social-contributions`, not from this table. The Acre column is chosen by the date the activity STARTED, and the reduced rate runs "Jusqu'à la fin du 3ème trimestre civil suivant celui de la date d'inscription". It is a reduced rate for that period, not a flat half reduction for four quarters.

**Self-employed au réel: the reformed base**

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.urssaf.fr/accueil/independant/comprendre-payer-cotisations/reforme-cotisations-independants.html |  |
| Flat allowance on the single base | 26% | "le revenu brut abattu de 26 %" | https://www.urssaf.fr/accueil/independant/comprendre-payer-cotisations/reforme-cotisations-independants.html (2026) |

The page says the new base and scales apply "à compter de la régularisation des cotisations de l’année 2025 (après la déclaration des revenus 2025, en 2026)". The rate scales are in `fr-social-contributions`.

### Cross-check 3: social contributions and income tax deductibility

| Item | Micro regime | Réel regime |
| --- | --- | --- |
| URSSAF contributions | Covered by the flat allowance, NOT deducted separately | Treated in the 2035 or 2031 as `fr-social-contributions` sets out |
| Deductible part of the CSG | Covered by the flat allowance | The amount on the URSSAF attestation de versement de la CSG-CRDS, not a split worked out from rates |
| Box 6DE on the 2042 | Not for professional CSG | Not for professional CSG: 6DE is the deductible CSG on investment and property income |
| Voluntary pension and protection contracts (Madelin, art. 154 bis CGI) | NOT deductible: the micro regime deducts no actual costs | Deductible within the art. 154 bis ceilings; take the ceiling from the 2035 or 2031 notice |

**CSG and CRDS for the self-employed, 2026**

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.urssaf.fr/accueil/independant/comprendre-payer-cotisations/vos-cotisations.html |  |
| CSG and CRDS on earned income | 9.70% | "Le taux de CSG-CRDS est fixé à 9,70 % (9,20 % + 0,50 %)" | https://www.urssaf.fr/accueil/independant/comprendre-payer-cotisations/vos-cotisations.html (2026) |

URSSAF prints no deductible and non-deductible split for earned income on that page. It says it sends an attestation de versement de la CSG-CRDS that "détaille les versements effectués et notamment le montant déductible de la CSG". Use that document. The 2042 brochure describes box 6DE as "CSG déductible connue, calculée sur les revenus du patrimoine" (https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/12-charges_ded_rev_225a236.pdf).

If an expense is deducted on the 2035 or 2031 and is also covered by a micro allowance, it is counted twice. Flag it for the reviewer.

### Cross-check 4: VAT input tax and income tax deductions agree

| Item | VAT treatment | Income tax treatment |
| --- | --- | --- |
| Recoverable VAT (réel simplifié or réel normal) | Claimed on the CA3 or CA12 as deductible VAT | NOT an income tax deduction: the expense is recorded excluding VAT |
| VAT under the franchise en base | No VAT recovery | Part of the cost: the expense is recorded including VAT |
| Blocked VAT (passenger cars, gifts above the low-value limit) | Not claimed | Added to the cost: the amount including VAT is deducted |
| VAT on fixed assets (réel regime) | Deductible on the CA3 or CA12 | The asset is recorded excluding VAT and depreciated |

The low-value gift limit is set by art. 28-00 A of annex IV to the CGI and is measured "toutes taxes comprises", per object and per year for one beneficiary (https://bofip.impots.gouv.fr/bofip/1196-PGP.html). That page does not print the amount: take it from `france-vat-return`. If an expense is claimed excluding VAT on the income side while the VAT was not recovered, the VAT is lost. Flag it for the reviewer.

### Cross-check 5: CFE and other local taxes

| Tax | Treatment |
| --- | --- |
| CFE (cotisation foncière des entreprises) | A cost of the business au réel (2035 or 2031). Not deductible for a micro business: the flat allowance covers it. |
| CVAE (cotisation sur la valeur ajoutée des entreprises) | Only above the thresholds in the CVAE table below. Rare for an individual freelancer. |

**CFE: exemption and payment**

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 |  |
| Exempt where turnover excluding VAT of year N-2 did not exceed | EUR 5,000 | "n'a pas dépassé 5 000 €" | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 (2026) |
| Prior-year CFE above which an instalment is due | EUR 3,000 | "CFE supérieure à 3 000 € L'entreprise doit verser un acompte égal à 50 %" | same (2026) |
| Instalment, as a share of the prior-year CFE | 50% | "L'entreprise doit verser un acompte égal à 50 % de la CFE versée l'année précédente" | same (2026) |

A business is exempt from CFE in the year it is created, and its base is halved the following year. Where the prior-year CFE was above the instalment threshold, the instalment is due "en général entre le 26 mai et le 16 juin (inclus)" and the balance by 15 December; otherwise the whole CFE is due by 15 December. A micro-entrepreneur pays the CCI part of the CFE through the URSSAF auto-entrepreneur account. The minimum base is a range set by the commune: `fr-cfe` holds it.

**CVAE thresholds**

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/839-PGP.html |  |
| Turnover above which a business is within the CVAE (page: 'supérieur à') | EUR 152,500 | "seuil d’assujettissement à la CVAE (152 500 €)" | https://bofip.impots.gouv.fr/bofip/839-PGP.html (2026) |
| Turnover below which the CVAE rate is nil | EUR 500,000 | "< 500 000 € 0 %" | same (2026) |

If a micro-entrepreneur claims the CFE as a deduction, it is an error: the micro regime uses the flat allowance only.

### Cross-check 6: the flat income tax payment (versement libératoire) is coherent

| Check | Rule |
| --- | --- |
| Option made | For 2025 income, the 2023 reference income per share is at or below the limit in the 2042-C-PRO table, raised per extra half share as that table states |
| Payments made | Equal the rate for the activity in the micro table times the turnover declared to URSSAF |
| 2042-C-PRO | Turnover still reported, at 5TA, 5TB or 5TE, but NOT taxed again on the scale |
| Household computation | The turnover subject to the flat payment does not enter the scale but is used for the reference income |

If the option was made but the reference-income test fails, flag it at once: the flat payment cannot apply and the income is taxed on the scale. Confirm the consequence in `fr-income-tax` before stating it to the client.

## Section 4: Final reviewer package contents

### Documents

1. Executive summary: one page with filing status, income, impôt net, VAT position, contributions, PAS update, balance due or refund.
2. VAT worksheet: CA3 or CA12 line by line, or the franchise check against the threshold table.
3. Income tax worksheet: 2042 and 2042-C-PRO line by line, plus the 2035 or 2031 if au réel.
4. Family quotient and scale: shares, bands, family-quotient cap, décote.
5. Social contributions reconciliation: micro-entrepreneur periods, or the self-employed annual regularisation.
6. CFE check: amount paid, deductibility.
7. PAS update: current rate, the rate applied from September 2026, instalments for the rest of 2026 and for 2027.
8. Reconciliation summary: all six cross-checks with pass or fail and notes.
9. Reviewer brief: narrative with positions, citations, flags, self-check results.
10. Client action list: what the client must do, with dates and amounts.

### Reviewer brief contents

~~~markdown
# Complete Return Package: [Client Name], Revenus 2025

## Executive Summary
- Filing status: [Single / Married-joint / PACS / Single parent]
- Parts fiscales: X
- Residence: France (full year)
- Business: [Micro-entrepreneur / EI au réel / Profession libérale]
- Income tax regime: [Micro-BNC / Micro-BIC / Déclaration contrôlée / Réel simplifié]
- VAT regime: [Franchise en base / Réel simplifié / Réel normal]
- Turnover excluding VAT: EUR X
- Revenu net imposable (household): EUR X
- Impôt brut: EUR X
- Impôt net (after credits and reductions): EUR X
- PAS instalments paid during 2025: EUR X
- Balance to pay / refund: EUR X
- VAT position: EUR X due / EUR X credit
- Social contributions paid: EUR X / due: EUR X
- CFE: EUR X
- PAS rate applied from September 2026: X

## VAT Return
[From france-vat-return]
- Regime and frequency
- Turnover excluding VAT by period
- VAT collected by rate
- VAT deductible (goods and services, fixed assets)
- VAT credit position
- Franchise en base threshold test (if applicable)
- Intra-EU statements (route to france-vat-return)
- CA3 or CA12 line summary

## Income Tax Return (2042 and 2042-C-PRO)
[From fr-income-tax and fr-personal-income-tax]
### Micro path:
- 2042-C-PRO boxes: turnover declared, allowance applied, net micro income
- Flat income tax payment: amount paid, eligibility check
### Réel path:
- 2035 or 2031 summary: receipts, deductible costs, tax result
- Depreciation schedule
- Professional gains and losses (if any)
### Common:
- 2042 household income: all categories
- Family quotient computation
- Scale applied (bands from the scale table in this skill)
- Décote (thresholds from the décote table)
- Family-quotient cap (from the cap table)
- Tax reductions (gifts and others)
- Tax credits (help at home, childcare and others)
- Impôt net
- PAS instalments paid during 2025
- Balance: due or refund

## Social Contributions (URSSAF)
[From fr-social-contributions]
### Micro-entrepreneur path:
- Turnover declared by month or quarter
- Rate applied (the rate for the year in which the turnover was collected)
- Acre (if applicable, chosen by start date)
- Total contributions paid
- Training contribution
### Self-employed au réel path:
- Base: reformed single base from the 2025 regularisation
- Provisional contributions paid in 2025
- Regularisation of 2025 after the income declaration
- Breakdown by contribution, as in fr-social-contributions
- Total due against total paid
- Deductible CSG from the URSSAF attestation
- Madelin contracts within the art. 154 bis CGI ceilings

## CFE
- Commune and base
- Amount paid
- Deductibility: yes (réel) / no (micro, covered by the allowance)
- First-year exemption or halved base (if applicable)

## Prélèvement à la Source (PAS)
[From fr-income-tax]
- Current PAS rate: X
- Instalments paid during 2025: EUR X
- Rate applied from September 2026: X
- Instalments for the rest of 2026 and for 2027: EUR X
- Option to modulate the rate after a significant change in income

## Cross-skill Reconciliation
- VAT turnover against 2042-C-PRO / 2035 / 2031: [pass/fail]
- URSSAF turnover against income declaration: [pass/fail]
- Contributions deductibility: [pass/fail]
- VAT input tax against income deductions: [pass/fail]
- CFE treatment: [pass/fail]
- Flat income tax payment coherence: [pass/fail]

## Reviewer Attention Flags
[Aggregated from all upstream skills]
- Franchise en base threshold crossed (VAT applies)
- Flat income tax payment eligibility (2023 reference income per share)
- Acre: start date and period
- Mixed-use expense percentages (home office, vehicle, phone)
- EU services and the intra-EU statements
- Micro limit crossed in one year (warning) or in two consecutive years (regime lost)
- Losses carried forward
- Madelin contracts within the deductibility ceilings
- Family-quotient cap effect
- Return filed after the 2026 deadline (surcharge and interest)

## Positions Taken
[List with legislation citations]
- e.g., "Franchise en base maintained under art. 293 B CGI: prior-year turnover at or below the services threshold in the franchise table"
- e.g., "Micro-BNC flat allowance applied under art. 102 ter CGI at the rate in the micro table"
- e.g., "Home office deduction on a surface pro rata, under the BOFiP chapter the reviewer names"
- e.g., "Acre reduced rate applied for the period URSSAF granted, chosen by the activity start date"
- e.g., "Madelin pension contributions deducted within the art. 154 bis CGI ceiling stated in the 2035 notice"

## Planning Notes for 2026
- PAS rate update and the instalment schedule
- URSSAF provisional contributions for 2026 (based on 2025 income)
- VAT franchise and micro limits for 2026 receipts (the 2026 rows of the tables)
- Depreciation continuing into 2026
- Flat income tax payment for 2027: option with URSSAF by 30 September 2026
- CFE: any base change, relief or new commune
- Electronic invoices: from 1 September 2026 every business must receive invoices in electronic form once its supplier is obliged to issue them that way (france-einvoice)
- Any 2026 finance law or social security financing law change

## Client Action List
[See the client action list section of this skill]
~~~

### Client action list

**Income tax return for 2025 income.** The online deadlines in 2026 were Thursday 21 May (départements 01 to 19 and non-residents), Thursday 28 May (départements 20 to 54) and Thursday 4 June (départements 55 to 974 and 976); the paper deadline was Tuesday 19 May 2026 (https://www.impots.gouv.fr/les-modalites-de-la-declaration-de-revenus-en-2026). Those dates have passed. After the tax notice arrives, "Corriger ma déclaration en ligne" is open for 2025 income from mid-August 2026 until mid-December 2026. A return not yet filed is late: see the surcharge and interest tables in the method below.

**Balance of income tax.** The balance is debited as set out in the table below, and the same return sets the PAS rate applied from September 2026.

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.impots.gouv.fr/les-modalites-de-la-declaration-de-revenus-en-2026 |  |
| Balance below this amount: one debit in September 2026 | EUR 300 | "en un seul prélèvement en septembre 2026 si le montant est inférieur à 300€" | https://www.impots.gouv.fr/les-modalites-de-la-declaration-de-revenus-en-2026 |
| Balance above this amount: four monthly debits, September to December | EUR 300 | "en quatre prélèvements mensuels (de septembre à décembre) si le montant est supérieur à 300€" | same (2026) |

**VAT.**
- CA3 (réel normal): monthly, or every three months where the VAT due each year is below the amount in the table below, on the date in the DGFiP schedule (`france-vat-return` holds the schedule).
- CA12 (réel simplifié): the annual return at the latest on the second working day after 1 May, or within three months of the year end where the accounting year does not end on 31 December. For a 31 December year end, instalments in July and December as shares of the prior year's VAT, with the balance paid with the return in May.

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://entreprendre.service-public.gouv.fr/vosdroits/F23566 |  |
| July instalment, share of prior-year VAT | 55% | "l'entreprise doit verser 55 % de la taxe due l'année précédente" | https://entreprendre.service-public.gouv.fr/vosdroits/F23566 (2026) |
| December instalment, share of prior-year VAT | 40% | "l'entreprise doit verser 40 % de la taxe due l'année précédente" | same (2026) |
| Prior-year VAT below which no instalments are due | EUR 1,000 | "un montant de TVA inférieur à 1 000 € l'année précédente est dispensée" | same (2026) |
| Annual VAT due below which a réel normal return is quarterly | EUR 4,000 | "le montant de la TVA exigible chaque année est inférieur à 4 000 €" | same (2026) |

**URSSAF, micro-entrepreneur.** Declare turnover collected each month or each quarter on the URSSAF auto-entrepreneur portal, even when it is nil. URSSAF's own example: the declaration for March is due on 30 April, moved to the next working day when that falls on a weekend or public holiday. On the quarterly option the page's first-declaration table gives the due dates 31 July (January to March), 31 October (April to June), 31 January of the next year (July to September) and 30 April of the next year (October to December) (https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/lessentiel-du-statut.html).

**URSSAF, self-employed au réel.** Provisional 2026 contributions are debited monthly or quarterly; the 2025 regularisation follows the income declaration and appears in the updated schedule (`fr-social-contributions`).

**CFE.** Instalment and balance dates as in the CFE section above.

**PAS.** The new rate applies from September 2026 after the 2025 return is processed. A change of rate can be requested in the "Gérer mon prélèvement à la source" area of the online account; a downward modulation is allowed only under conditions.

**Ongoing.**
1. Issue invoices with the mandatory mentions (`france-vat-return`, `france-einvoice`).
2. Keep the books and supporting documents for the periods in the retention table below.
3. Keep the accounting entries file (FEC) ready if au réel (`france-bookkeeping`).
4. Watch the franchise en base threshold during the year.
5. File the intra-EU statements if supplying services to EU businesses (`france-vat-return`).
6. Watch the micro limits for a possible change of regime.

**Retention of documents**

| Document | Period | Note |
| --- | --- | --- |
| Source | all periods below | https://entreprendre.service-public.gouv.fr/vosdroits/F10029 |
| Books and registers, and supporting documents such as invoices | 10 years from the close of the financial year | "10 ans à partir de la clôture de l'exercice" |
| Documents open to the tax administration's rights of inspection | 6 years | "doivent être conservés pendant un délai de 6 ans" |

## Section 5: Refusals

- **R-FR-A1.** An upstream skill did not run. Name it. This is a warning, not a hard stop: continue with the data available and flag the gap.
- **R-FR-A2.** An upstream self-check failed. Name the check and note it in the reviewer brief. Continue.
- **R-FR-A3.** A cross-skill reconciliation failed. Name it and describe the difference. Flag it for the reviewer but continue.
- **R-FR-A4.** Intake incomplete. Specific missing items prevent computation. List what is missing and ask the user for that data point.
- **R-FR-A5.** Out-of-scope item found during assembly, for example SCI income, agricultural activity or a foreign pension. Flag it and leave it out of the computation.
- **R-FR-A6.** Franchise en base threshold crossed. A critical flag, not a refusal. The computation continues, but the reviewer brief must warn prominently that VAT applies and that earlier invoices may need correcting.

## Section 6: Self-checks

- **Check FR-1.** All upstream skills ran: `france-vat-return`, `fr-income-tax`, `fr-social-contributions` produced output, and the PAS update was produced or computed from the income tax output.
- **Check FR-2.** VAT turnover matches the income declaration, to the euro or with the difference explained, across the VAT return and the 2042-C-PRO, 2035 or 2031.
- **Check FR-3.** URSSAF turnover matches the income declaration. Micro-entrepreneur: total turnover declared to URSSAF equals the 2042-C-PRO micro boxes. Self-employed au réel: the result flows into the reformed base.
- **Check FR-4.** The right micro allowance is applied, from the micro table, with the minimum allowance respected and no mixing between activities.
- **Check FR-5.** The family quotient is right: shares match marital status, children and the single-parent half share.
- **Check FR-6.** The scale is applied to the right income: revenu net imposable divided by shares, each band from the scale table, then multiplied back by the shares, then the cap and the décote.
- **Check FR-7.** Flat income tax payment eligibility checked: for 2025 income, the 2023 reference income per share at or below the limit in the 2042-C-PRO table. If not eligible, the income goes to the scale.
- **Check FR-8.** Deductible CSG taken from the URSSAF attestation, not computed from a rate split, and not put in box 6DE.
- **Check FR-9.** Madelin contracts within the art. 154 bis CGI ceilings.
- **Check FR-10.** CFE treatment right: deductible au réel, not for micro, not counted twice.
- **Check FR-11.** PAS instalments reconciled: the total paid during 2025 is set against impôt net to give the balance.
- **Check FR-12.** Filing calendar complete: every date for VAT, the 2042, URSSAF, CFE and PAS is listed, and any date already passed on the day the package is built is marked as passed.
- **Check FR-13.** Every position in the reviewer brief cites the article of the CGI, the social security code or the LPF, and the official page it was read on.

## Section 7: Output files

- **Three output files.**
  1. `[client_slug]_2025_france_master.xlsx`: one workbook holding every worksheet and form. Sheets: Cover, VAT (CA3 or CA12, or the franchise check), 2042-C-PRO (micro or réel), Scale and Family Quotient, 2035 or 2031 (if réel), Social Contributions, CFE, PAS Update, Cross-Check Summary. Use live formulas where possible: the 2042-C-PRO turnover references the VAT turnover cell, the micro allowance is computed automatically, and the bands are computed from the revenu net imposable. Check there are no #REF! errors. Check the computed values match the computation model to the euro before shipping.
  2. `reviewer_brief.md`: one markdown file covering every part of Section 4: executive summary, VAT, income tax, contributions, CFE, PAS, reconciliation, flags, positions, planning notes.
  3. `client_action_list.md`: one markdown file with the step-by-step actions: filings and payments still open, the VAT calendar, the URSSAF calendar, CFE dates, the PAS update and the ongoing reminders.
- If execution runs out of context mid-build, produce whatever is complete, then state at the end which of the three files were not produced or are partial. Place the files in the outputs folder of the environment and present them to the user at the end.

## Section 8: Cross-skill references

- **Inputs:** `fr-freelance-intake` (the structured intake package); `france-vat-return` (VAT return lines and classification); `fr-income-tax` (2042, 2042-C-PRO, 2035 or 2031, and the PAS); `fr-personal-income-tax` (the household computation); `fr-social-contributions` (URSSAF reconciliation); `fr-cfe` (CFE).
- **Related:** `france-bookkeeping` (records, FEC, depreciation); `france-einvoice` (electronic invoicing dates).
- **Output:** the final reviewer package. No downstream skill.

## Section 9: Known gaps

1. PDF form filling is not automated. The reviewer uses the worksheets to fill the official forms on impots.gouv.fr.
2. E-filing is done by the reviewer or the client on impots.gouv.fr, not by this skill.
3. Payment is the client's responsibility; the skill gives instructions and amounts only.
4. An EURL taxed to income tax is supported but not deeply tested. Its professional return (2031 or 2035 depending on BIC or BNC) may need manual adjustment for the manager's pay and contributions.
5. Depreciation over several years assumes the prior-year schedule is provided. If not, only the current year's acquisitions are depreciated.
6. Foreign-source income and tax treaty relief are out of scope.
7. Rental income (2044) is noted in the household total, but the 2044 itself is out of scope (`fr-rental-income`).
8. Gains on property are out of scope.
9. The real estate wealth tax (IFI) is out of scope.
10. SCI and multi-entity structures are out of scope.
11. The package is complete only for 2025 income; 2026 appears as planning and as the rules in force today.

## The method, step by step

1. **Confirm the regime for 2025 income.** Test turnover of 2024 and 2023 against the 2025 rows of the micro table; the regime is lost only after two consecutive years over a limit (https://entreprendre.service-public.gouv.fr/vosdroits/F23267).
2. **Fix the VAT position.** Test the franchise en base against the threshold table (https://entreprendre.service-public.gouv.fr/vosdroits/F21746); for a business liable to VAT, check the CA3 or CA12 and the instalments (https://entreprendre.service-public.gouv.fr/vosdroits/F23566).
3. **Reconcile URSSAF.** Micro-entrepreneur: turnover declared each period times the rate of the year (https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/lessentiel-du-statut.html). Self-employed au réel: the regularisation of 2025 on the reformed base (https://www.urssaf.fr/accueil/independant/comprendre-payer-cotisations/reforme-cotisations-independants.html), with the deductible CSG from the URSSAF attestation (https://www.urssaf.fr/accueil/independant/comprendre-payer-cotisations/vos-cotisations.html).
4. **Fill the 2042-C-PRO and the 2042.** Use the box map and the flat-payment test from the brochure (https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/11-revenus_non_salaries_161a182.pdf), then the scale (https://www.service-public.gouv.fr/particuliers/vosdroits/F1419), the family-quotient cap (https://bofip.impots.gouv.fr/bofip/2494-PGP.html/identifiant=BOI-IR-LIQ-20-20-20-20260407) and the décote (https://bofip.impots.gouv.fr/bofip/2495-PGP.html/identifiant=BOI-IR-LIQ-20-20-30-20260407).
5. **Set the balance and the PAS.** Balance debits and the September 2026 rate update as on the 2026 declaration page (https://www.impots.gouv.fr/les-modalites-de-la-declaration-de-revenus-en-2026); instalments for the self-employed and modulation as on the PAS page (https://www.service-public.gouv.fr/particuliers/vosdroits/F34009).
6. **Check the CFE.** Exemption, first-year rule and payment dates (https://entreprendre.service-public.gouv.fr/vosdroits/F23547).
7. **If the return is late or wrong.** Use the online correction service while it is open (https://www.impots.gouv.fr/les-modalites-de-la-declaration-de-revenus-en-2026). A return filed late of the taxpayer's own accord, before any formal demand, carries the surcharge in the table below on the tax it shows, plus interest for each month of delay; after a mise en demeure the rate is higher, and `fr-tax-audit` holds it.

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/4911-PGP.html |  |
| Surcharge on the tax shown by a return filed late (art. 1728 CGI), base rate | 10% | "la majoration de 10 % prévue par l’article 1728 du CGI" | https://bofip.impots.gouv.fr/bofip/4911-PGP.html (2026) |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://bofip.impots.gouv.fr/bofip/1458-PGP.html |  |
| Late payment interest (art. 1727 CGI), per month | 0.2% | "taux de l'intérêt de retard de 0,2 % par mois" | https://bofip.impots.gouv.fr/bofip/1458-PGP.html (2026) |

8. **Run the six cross-checks and the self-checks, then assemble the three output files.** Keep the records for the periods in the retention table (https://entreprendre.service-public.gouv.fr/vosdroits/F10029).

## Ask the client first

- Did you file your 2025 income return in spring 2026, and have you received the tax notice? (It decides between a correction and a late return.)
- Did your activity start before or after 1 July 2026, and did URSSAF grant Acre? (It picks the Acre column.)
- Did you opt for the flat income tax payment, and what was the reference income on your 2023 tax notice? (It decides whether the flat payment holds for 2025 income.)
- What was your turnover excluding VAT in 2023, 2024 and 2025, by activity (sales, services, liberal)? (It decides the micro regime and the VAT franchise.)
- Do you have the URSSAF attestation de versement de la CSG-CRDS and your CFE notices? (They give the deductible CSG and the CFE dates.)

## When to refuse or refer

- The client is not a full-year French resident, or has foreign-source income that needs treaty relief: refer.
- The business is a company taxed to corporation tax, an SCI, or more than one entity: refer.
- Agricultural income, property gains, the real estate wealth tax or a detailed 2044: out of scope (`fr-rental-income` for lettings).
- A tax audit is open or a reassessment notice has arrived: refer to `fr-tax-audit` and the reviewer.
- A figure the package needs is not in this skill or in the content skill named for it: say so and leave it blank; do not supply it from memory.
- Australian, US or other foreign returns of the same client: out of scope.

## Sources

- https://entreprendre.service-public.gouv.fr/vosdroits/F23267 (micro regime, checked 13 May 2026 by the site, read 2026-10-31)
- https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/11-revenus_non_salaries_161a182.pdf (2026 income tax brochure, self-employed income, read 2026-10-31)
- https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/12-charges_ded_rev_225a236.pdf (2026 income tax brochure, deductible charges, read 2026-10-31)
- https://www.service-public.gouv.fr/particuliers/vosdroits/F1419 (income tax scale, checked 15 April 2026 by the site, read 2026-10-31)
- https://bofip.impots.gouv.fr/bofip/2494-PGP.html/identifiant=BOI-IR-LIQ-20-20-20-20260407 (family-quotient cap, read 2026-10-31)
- https://bofip.impots.gouv.fr/bofip/2495-PGP.html/identifiant=BOI-IR-LIQ-20-20-30-20260407 (décote, read 2026-10-31)
- https://entreprendre.service-public.gouv.fr/vosdroits/F21746 (VAT franchise en base, checked 1 January 2026 by the site, read 2026-10-31)
- https://entreprendre.service-public.gouv.fr/vosdroits/F23566 (declaring and paying VAT, checked 21 February 2026 by the site, read 2026-10-31)
- https://bofip.impots.gouv.fr/bofip/1196-PGP.html (VAT on gifts, read 2026-10-31)
- https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/lessentiel-du-statut.html (micro-entrepreneur rates, Acre, training contribution, declarations, read 2026-10-31)
- https://www.urssaf.fr/accueil/independant/comprendre-payer-cotisations/reforme-cotisations-independants.html (reformed base, read 2026-10-31)
- https://www.urssaf.fr/accueil/independant/comprendre-payer-cotisations/vos-cotisations.html (CSG-CRDS and the attestation, read 2026-10-31)
- https://entreprendre.service-public.gouv.fr/vosdroits/F23547 (CFE, checked 2 April 2026 by the site, read 2026-10-31)
- https://bofip.impots.gouv.fr/bofip/839-PGP.html (CVAE, read 2026-10-31)
- https://www.impots.gouv.fr/les-modalites-de-la-declaration-de-revenus-en-2026 (2026 deadlines, balance, correction service, read 2026-10-31)
- https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 (prélèvement à la source, checked 15 April 2026 by the site, read 2026-10-31)
- https://www.impots.gouv.fr/particulier/questions/comment-declarer-les-revenus-provenant-de-mon-activite-dauto-entrepreneur (micro-entrepreneur declaring, flat-payment ceiling, read 2026-10-31)
- https://bofip.impots.gouv.fr/bofip/4911-PGP.html (late filing surcharge, read 2026-10-31)
- https://bofip.impots.gouv.fr/bofip/1458-PGP.html (late payment interest, read 2026-10-31)
- https://entreprendre.service-public.gouv.fr/vosdroits/F10029 (document retention, read 2026-10-31)
- https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation (electronic invoicing start dates, read 2026-10-31)

Not yet confirmed: the flat-payment ceiling for the option taken in 2026. F23267 prints EUR 29,579 for a single person against year N-2, and impots.gouv.fr prints EUR 29,315 against the 2024 reference income.

### Change log

v1.0 (May 2026): initial draft, modelled on mt-return-assembly.
v2.0 (October 2026): every figure re-read on official pages; sibling skill names corrected to live skills; 2042-C-PRO boxes, deadlines, CFE dates, VAT franchise thresholds and micro-entrepreneur rates corrected.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this skill is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
