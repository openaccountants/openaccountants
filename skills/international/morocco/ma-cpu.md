---
name: ma-cpu
description: Use this skill whenever asked about Morocco's Contribution Professionnelle Unique (CPU) — the single-tax regime that replaced the régime forfaitaire (régime du bénéfice forfaitaire) for small self-employed people and professionals who are not on the auto-entrepreneur status. Trigger on phrases like "CPU Maroc", "Contribution Professionnelle Unique", "régime forfaitaire Maroc", "contribution professionnelle unique calcul", "droit complémentaire AMO CPU", "coefficient bénéfice CPU", "المساهمة المهنية الموحدة", "CPU vs auto-entrepreneur Maroc". Covers eligibility and turnover ceilings, the CPU computation (turnover × profession coefficient → 10% liberatory IR), the effective minimum, the mandatory complementary health contribution (droit complémentaire) banded by profit for AMO, and the filing & payment calendar. Reply in the user's language (English, French, or Moroccan Arabic / Darija) and keep the native terms (CPU, IR, DGI, AMO, CNSS). Cross-reference ma-auto-entrepreneur (simpler, lower ceilings) and ma-income-tax (RNR/RNS) as alternatives.
version: 1.0
jurisdiction: MA
tax_year: 2026
last_updated: 2026-09-27
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Morocco: Contribution Professionnelle Unique (CPU) for small individual businesses

## Scope ([Code Général des Impôts, 2026 edition, Art. 40 and 41](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1))

Figures are for tax year 2026 (calendar year 2026, turnover declared before 1 April 2027). There is also a dated section for the 2025 returns that were due before 1 April 2026. The law is the Code Général des Impôts (CGI) in the 2026 edition published by the Direction Générale des Impôts (DGI). That edition includes the Finance Law for 2026 (loi de finances n° 50-25).

The CPU (*Contribution Professionnelle Unique*, المساهمة المهنية الموحدة) is an optional income tax regime for **individuals (personnes physiques)** with small professional income. It replaced the old *régime du bénéfice forfaitaire* from 1 January 2021 (Finance Law n° 65-20, Art. 6). One payment covers:

- **income tax (IR)** on the professional income, worked out as turnover x a coefficient for the trade, then taxed at a flat 10%; and
- a **droit complémentaire**, a fixed amount per band that funds basic mandatory health insurance (AMO).

CPU taxpayers are fully and permanently exempt from the *taxe professionnelle* (TP) and the *taxe de services communaux* (TSC) from 1 January 2021 (Loi 07-20 amending Loi 47-06, as stated in the [DGI CPU practical guide](https://www.tax.gov.ma/wps/wcm/connect/cecc3309-6ca8-494c-903b-160c1649cd9a/CPU+guide+pratique+Version+fran%C3%A7aise.pdf?MOD=AJPERES&CACHEID=cecc3309-6ca8-494c-903b-160c1649cd9a)). They must still register for TP under other laws.

Not covered here: the auto-entrepreneur regime (ma-auto-entrepreneur), the real-accounts regimes RNR and RNS (ma-income-tax), VAT, payroll and companies. Reply in the user's language and keep the native terms (CPU, IR, DGI, AMO, SIMPL).

## Ask the client first

- What exactly does the business do? Name the trade, not the sector. The coefficient depends on the sub-category in the Art. 40-I table, and some professions are excluded outright.
- Is the business run by an individual in their own name, or by a company? CPU is only for individuals and for the individual members of an *indivision* or *société de fait*.
- What was the turnover, **VAT included**, in each of the last three years? Is any of it sales of goods and any of it services?
- For service work, did any single client pay more than 80,000 dirhams (excluding VAT) in the year? If so, did that client withhold tax?
- Is the person enrolled in basic mandatory health insurance (AMO)? Get the membership number and date.
- Which regime is the person on now: CPU, auto-entrepreneur, RNS or RNR? Was the CPU option ever filed, and when?
- Did the business start, stop, move, or sell equipment or the goodwill (*fonds de commerce*) this year? Is the person 65 or over, and do they have a pension scheme?
- Did the person choose annual or quarterly payment on the last return? Are any payments late?

## The method, step by step

1. **Check the exclusions first.** If the activity is on the list in décret n° 2-08-124 (doctors, lawyers, IT service providers, importers, property developers and others; full list below), CPU is not available at any turnover. Stop and route to ma-income-tax. Doing the sums first wastes the client's time and invites a wrong filing.
2. **Check the ceiling for the right branch.** Compare turnover (VAT included) with the commercial/industrial/artisanal ceiling or the services ceiling. If there are two branches, apply the Art. 43-1° test (each branch within its own ceiling, or total within the ceiling of the main activity). Remember that exit happens only after **two consecutive years** over the ceiling.
3. **Check the entry conditions.** The person must hold AMO membership (Art. 41-II-B) and have filed the option in time (Art. 44). Someone coming from RNR or RNS must have stayed under the ceiling for three consecutive years (Art. 43).
4. **Pick the coefficient** from the Art. 40-I table for each activity. Do not use the old 2021 annex, which was abolished on 1 January 2022.
5. **Take out service turnover that a client has already taxed by withholding.** This is the part above 80,000 dirhams from one client. Then multiply each activity's remaining turnover by its coefficient and add the results. That total is the professional income.
6. **Apply the flat CPU rate** (Art. 73-II-B-6°, set out below) to get the IR component.
7. **Look up the droit complémentaire** band using the annual IR component. For a part year, annualise the IR to find the band, then pro-rate the annual amount.
8. **File the turnover return** before 1 April of the following year on SIMPL. It is pre-filled; correct it where needed. Pay annually or in four equal quarterly instalments, as chosen on the return.
9. **Deal with events.** On a sale or cessation, file the gains return within 45 days and pay the flat gains tax with it. On a move, a departure from Morocco or a death, use the special deadlines in the filing section.

## Figures with years ([2026 edition of the CGI, Art. 40, 41, 73](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1))

All figures below are in the 2026 edition of the CGI and apply to turnover of 2025 and 2026. None was changed by the Finance Laws for 2025 or 2026. The one CPU change in 2026 is the new relief on gains at retirement (see "Selling or closing the business").

| Item | Figure | Since | Source |
| --- | --- | --- | --- |
| Turnover ceiling, commercial, industrial and artisanal activities | MAD 2,000,000 a year | 2021 | Art. 41-II-A |
| Turnover ceiling, service providers | MAD 500,000 a year | 2021 | Art. 41-II-A |
| IR rate on CPU professional income | 10% | 2021 | Art. 73-II-B-6° |
| Withholding by a client on service turnover above MAD 80,000 from that client | 30% of the excess | 1 January 2023 | Art. 40-I, 45 bis-II, 73-II-G-8° |
| IR on business gains and indemnities | 20% | 2021 | Art. 40-II, 73-II-F-11° |
| Deemed depreciation on assets sold (equipment, tools, furniture / vehicles) | 10% / 20% a year | 2021 | Art. 40-II |
| Retirement relief on intangible gains (age 65+, no pension scheme) | 50% of the gain, on gains up to MAD 1,000,000 | disposals from 1 January 2026 | Art. 31-V |

The [DGI CPU practical guide](https://www.tax.gov.ma/wps/wcm/connect/cecc3309-6ca8-494c-903b-160c1649cd9a/CPU+guide+pratique+Version+fran%C3%A7aise.pdf?MOD=AJPERES&CACHEID=cecc3309-6ca8-494c-903b-160c1649cd9a) states that the ceilings are measured "taxe sur la valeur ajoutée comprise" (VAT included).

### Coefficients by trade, in force since 1 January 2022 ([CGI Art. 40-I table](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1))

The Finance Law for 2022 abolished the old annexed table of 795 professions. It replaced it with this grouped table in Art. 40-I ([Note circulaire n° 732](https://tax.gov.ma/wps/wcm/connect/982a0f63-09eb-4c60-8b44-2f2a474dc865/Note+Circulaire+n+732+relative+aux+mesures+fiscales+de+la+LF+2022.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-982a0f63-09eb-4c60-8b44-2f2a474dc865-nWihlos)). Coefficients quoted in the 2021 DGI guide (for example 8% for a general food shop or 40% for a hairdresser) come from the abolished table. Do not use them for 2022 onwards.

| Group | Category of profession | Coefficient |
| --- | --- | --- |
| Commerce | Alimentation générale (general food shop, grocer) | 6% |
| Commerce | Autres produits alimentaires (other food products) | 8% |
| Commerce | Matières premières; matériaux de construction | 8% |
| Commerce | Produits chimiques et engrais | 10% |
| Commerce | Autres produits non alimentaires (other non-food goods) | 12% |
| Services | Restauration légère ou rapide (snack, fast food) | 10% |
| Services | Exploitant de restaurant et débitant de boissons | 20% |
| Services | Transport de personnes et de marchandises | 10% |
| Services | Activités d'entretien (maintenance, cleaning) | 15% |
| Services | Location de biens meubles (renting movable goods) | 20% |
| Services | Autres activités de location et de gestion | 25% |
| Services | Coiffure et esthétique (hairdressing, beauty) | 20% |
| Services | Mécanicien réparateur; réparateur d'appareils électroniques; activités artistiques et de divertissement; exploitant de moulin | 30% |
| Services | Autres artisans de services | 12% |
| Services | Courtiers (brokers) | 45% |
| Services | Autres prestations (other services) | 20% |
| Fabrication | Produits alimentaires; produits non alimentaires | 10% |
| Specific trades | Chevillard (wholesale butcher) | 4% |
| Specific trades | Marchand de tabac | 3% |
| Specific trades | Marchand de gaz comprimé, liquéfié et dissous | 4.5% |
| Specific trades | Marchand de farine, fécules, semoules ou son | 5% |
| Specific trades | Armateur, adjudicataire ou fermier (pêche) | 7% |
| Specific trades | Boulanger (baker) | 8% |

- Several activities with different coefficients: the professional income is the total of the incomes worked out separately for each activity (Art. 40-I, wording added by the Finance Law for 2022).
- The DGI's system maps each registered activity to one of these categories. It shows the category when the taxpayer first registers or files ([Note circulaire n° 732](https://tax.gov.ma/wps/wcm/connect/982a0f63-09eb-4c60-8b44-2f2a474dc865/Note+Circulaire+n+732+relative+aux+mesures+fiscales+de+la+LF+2022.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-982a0f63-09eb-4c60-8b44-2f2a474dc865-nWihlos)). If the trade could fit two rows, check the pre-filled SIMPL return or ask the local tax office. Do not choose the lower coefficient on your own.

### Droit complémentaire (AMO health cover) ([CGI Art. 73-II-B-6°](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1))

The IR component is increased by a droit complémentaire. The band is set by the **annual IR component in dirhams**, not by turnover.

| Annual IR component (MAD) | Quarterly droit (MAD) | Annual droit (MAD) |
| --- | --- | --- |
| Less than 500 | 300 | 1,200 |
| 500 to 1,000 | 390 | 1,560 |
| 1,001 to 2,500 | 570 | 2,280 |
| 2,501 to 5,000 | 720 | 2,880 |
| 5,001 to 10,000 | 1,050 | 4,200 |
| 10,001 to 25,000 | 1,500 | 6,000 |
| 25,001 to 50,000 | 2,250 | 9,000 |
| More than 50,000 | 3,600 | 14,400 |

- The droit is paid according to the person's AMO membership status. By way of exception to Art. 173-I, the transitional rule of the Finance Law for 2021 says it "est versé selon la situation du redevable en matière d'adhésion" to AMO. The [DGI CPU notice](https://www.tax.gov.ma/wps/wcm/connect/66026b2b-3420-4719-9c8b-2b9cdf64a494/Notice+explicative+CPU+2021.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-66026b2b-3420-4719-9c8b-2b9cdf64a494-ouzv3A9) says it is paid once the taxpayer joins AMO. AMO membership is also a condition of the CPU option itself (Art. 41-II-B), so treat it as due.
- Part year (start or cessation): the DGI annualises the IR component to find the band, then pro-rates the annual droit by months. See worked case 5.
- The bands are written in whole dirhams. If an IR component with centimes falls between two rows, the law does not say which row applies. Flag it and confirm with the local tax office.

## Who can use the CPU ([CGI Art. 41, 43, 44](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1))

**Who is in.** Individuals with professional income who opt for CPU (Art. 41-I). The individual members of an *indivision* or *société de fait* are also covered (Art. 32). According to the [DGI CPU practical guide](https://www.tax.gov.ma/wps/wcm/connect/cecc3309-6ca8-494c-903b-160c1649cd9a/CPU+guide+pratique+Version+fran%C3%A7aise.pdf?MOD=AJPERES&CACHEID=cecc3309-6ca8-494c-903b-160c1649cd9a), this includes:

- people taxed under the old forfaitaire regime before 2021, who moved to CPU automatically with no formality ("aucune formalité n'est requise");
- people starting an activity; and
- people coming from RNR or RNS who meet the three-year rule below.

**Two conditions (Art. 41-II), both required:**

- annual turnover not above the ceiling for the branch: 2,000,000 dirhams for commercial, industrial and artisanal activities, and 500,000 dirhams for service providers;
- membership of basic mandatory health insurance (AMO).

**Two activities under different ceilings (Art. 43-1°).** The option is valid only if either:

- turnover in each category stays within its own ceiling; or
- total turnover stays within the ceiling of the main activity.

**Coming from RNS or RNR (Art. 43-2° and 3°).** A taxpayer on RNS or RNR may opt for CPU only when turnover has stayed below the relevant ceiling for **three consecutive financial years**. A single good year is not enough.

**How and when to opt (Art. 44-I).** Make a written request to the tax inspector for the tax domicile or main establishment. Send it by registered letter with acknowledgement of receipt, or hand it in against a receipt.

- *At the start of activity:* file the request before the deadline for the CPU turnover return (before 1 April of the year after the start year). The option then counts for the start year itself ("l'option est valable pour l'année du début d'activité").
- *During activity:* file the request within the deadline for the previous year's global income return (Art. 82), which the DGI guide gives as before 1 May of the current year. The DGI guide adds that such an option "ne prend effet qu'à partir de l'année suivante". If the timing matters, confirm with the tax office which year the option first covers.

**Staying in and leaving (Art. 41-II).** The option stays valid until turnover exceeds the ceiling for **two consecutive years**. RNR then applies to income from 1 January of the year after those two years. If the DGI spots two years over the ceiling, it sends a notified letter asking for corrective returns under the right regime within 30 days (Art. 221 bis-II).

### Excluded professions ([décret n° 2-08-124 of 28 May 2009](https://www.tax.gov.ma/wps/wcm/connect/24a95c1a-b857-432c-a516-8dc833bb445b/D%C3%A9cret+n%C2%B0+2-08-124+du+3+joumada+II+1430+%2828+mai+2009%29+relatif+aux+professions+ou+activit%C3%A9s+exclues+du+r%C3%A9gime+forfaitaire.pdf?MOD=AJPERES&CACHEID=24a95c1a-b857-432c-a516-8dc833bb445b))

Art. 41-III excludes professions "fixées par voie réglementaire". The DGI guide says these are the professions listed in décret n° 2-08-124, excluded "quel que soit le chiffre d'affaires réalisé". The decree was written for the forfaitaire regime, and the DGI applies it to CPU. The list:

- property managers (administrateurs de biens), business agents, travel agents, architects, insurers, insurance brokers and intermediaries, lawyers (avocats), money changers;
- surgeons, dental surgeons, doctors, radiologists, physiotherapists, veterinarians, pharmacists, operators of clinics and medical laboratories;
- goods commission agents, accountants (comptables), experts-comptables, legal and tax advisers, experts in any field, consulting engineers, operators of a design office (bureau d'études);
- publishers, printers, booksellers, film producers, cinema operators;
- contractors for miscellaneous works, IT works and surveying works; surveyors and géomètres; IT service providers;
- driving schools, private schools, hotels, event and reception organisers, aircraft and helicopter lessors;
- property developers and subdividers, property dealers, jewellers (retail and wholesale), importers, exporters, independent sales representatives, mandataires négociants, interpreters and translators, notaries, customs forwarders.

If the activity is close to one of these (for example "web design" against "prestataires de services informatiques"), treat it as excluded until the tax office confirms otherwise.

## Withholding by clients on large service contracts ([CGI Art. 40-I, 45 bis-II, 73-II-G](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1))

This rule has applied since 1 January 2023. When a CPU taxpayer's annual **service** turnover with **one client** exceeds MAD 80,000, the client withholds IR on the excess at 30%. The client pays the tax to the DGI ([Note circulaire n° 733](https://www.tax.gov.ma/wps/wcm/connect/070abc0f-a958-4cf9-84be-7e9b76434063/NC+N%C2%B0+733+relative+aux+mesures+fiscales+de+la+LF+2023+vf.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-070abc0f-a958-4cf9-84be-7e9b76434063-oq2C8BE)).

- **Who withholds:** legal persons (public or private) and individuals taxed under RNR or RNS. Private individuals and other CPU or auto-entrepreneur clients do not.
- **Base:** annual turnover with that client, **excluding VAT**, above MAD 80,000. Sales of goods, merchandise and equipment are outside the rule.
- **Timing:** the client pays the tax over before the end of the month after the month of withholding. The client also lists these payments in its annual declaration of fees paid (Art. 151-IV).
- **Effect on the CPU return:** the DGI's own example leaves the withheld excess out of the CPU base. The turnover return must show the service turnover above MAD 80,000 with the same client (Art. 82 quater-I-8°).
- The droit complémentaire is still due on the CPU part.

## Selling or closing the business ([CGI Art. 31-V, 40-II, 82 quater-II](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1))

Taxed at 20% (Art. 73-II-F-11°), separately from the turnover-based CPU:

- the net overall gain on selling business assets, whether during or at the end of the business, **excluding land and buildings**;
- the gain the administration assesses when such assets stop being used in the business;
- indemnities received for stopping the profession or for transferring the clientele.

**Gains on depreciable assets.** The gain is the sale price (or market value) minus cost. Cost is first reduced by the depreciation that would have been taken under RNR/RNS, or that is deemed taken under the forfaitaire regime or CPU, at 10% a year for equipment, tools and furniture and 20% a year for vehicles. The administration values the gains under Art. 220 and 221.

**Land and buildings.** A CPU taxpayer's gain on business land and buildings is taxed as a *profit foncier* (real-estate gain), not under the 20% CPU gains rule ([Note circulaire n° 737](https://www.tax.gov.ma/wps/wcm/connect/e48c5c9d-ae80-4b30-a1b3-80af7ec09be1/NC+737+LF+2026.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-e48c5c9d-ae80-4b30-a1b3-80af7ec09be1-pOvNbSq)). Route that part to the real-estate gains guide.

**New for 2026: retirement relief (Art. 31-V, Finance Law 2026).** A 50% reduction applies to the gain on the **intangible** elements of the *fonds de commerce* (clientele, trade name, sign, trademarks, leasehold right) and to cessation or clientele-transfer indemnities. It applies only up to a gain of 1,000,000 dirhams. All of these conditions must be met ([Note circulaire n° 737](https://www.tax.gov.ma/wps/wcm/connect/e48c5c9d-ae80-4b30-a1b3-80af7ec09be1/NC+737+LF+2026.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-e48c5c9d-ae80-4b30-a1b3-80af7ec09be1-pOvNbSq)):

- the person is taxed under CPU;
- the person has no pension scheme (*régime de retraite*);
- the person is at least 65 on the date of **final** cessation;
- the business stops for good.

The relief applies to sales or withdrawals of the *fonds de commerce* from 1 January 2026. Tangible assets are not covered. The reduced gain is taxed at 20%.

**Return.** File the gains and indemnities return (form ADP160B) with payment (bordereau RSP160B) within **45 days** of selling all or part of the business or clientele, or of ceasing activity (Art. 82 quater-II). Attach the evidence of sale and purchase prices. The turnover return for the part year is also due; see the filing section.

## Other rules that trip people up ([CGI Art. 144, 145, 146 bis, 247 ter](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1))

- **No real expenses.** The base is turnover x coefficient. Costs are not deducted, and the progressive IR scale is not applied to CPU income. The 10% flat rate replaces it.
- **No minimum contribution.** The cotisation minimale of Art. 144 applies to companies and to individuals under RNR or RNS ("selon le régime du résultat net réel ou du résultat net simplifié"), not to CPU.
- **Mobile-payment turnover.** Turnover received by mobile payment was left out of the base and the ceilings only for returns covering **2020 to 2024** (Art. 247 ter-II). For 2025 and 2026 turnover there is no such exclusion.
- **Books.** The accounting rules of Art. 145 do not apply to CPU taxpayers (Art. 145-XI). Two things still apply. The person must hold an email address and give it to the DGI (Art. 145-X). The purchase invoice rules of Art. 146 apply through Art. 146 bis, so keep invoices for purchases.
- **All CPU taxpayers must file**, including those whose tax was below 5,000 dirhams and who were exempt from filing under the old Art. 86-4° ([DGI CPU practical guide](https://www.tax.gov.ma/wps/wcm/connect/cecc3309-6ca8-494c-903b-160c1649cd9a/CPU+guide+pratique+Version+fran%C3%A7aise.pdf?MOD=AJPERES&CACHEID=cecc3309-6ca8-494c-903b-160c1649cd9a)). CPU is a self-declared regime and the DGI can audit it.

## Boundary and exception table ([CGI Art. 40 to 44](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1))

| Situation | Rule | What to do |
| --- | --- | --- |
| Turnover over the ceiling in one year only | Option stays valid; exit only after two consecutive years (Art. 41-II) | Stay on CPU; warn the client about next year |
| Over the ceiling two years running | RNR from 1 January of the following year (Art. 41-II) | Route to ma-income-tax; check VAT |
| On RNS/RNR, turnover now small | CPU only after three consecutive years below the ceiling (Art. 43) | Count the years before filing an option |
| Mixed goods and services | Each branch within its ceiling, or total within the main activity's ceiling (Art. 43-1°) | Split turnover by branch |
| Two trades with different coefficients | Compute each separately and add (Art. 40-I) | One line per activity on ADP150B |
| Services over MAD 80,000 to one client | Client withholds 30% on the excess (Art. 40-I, 73-II-G-8°) | Leave the excess out of the CPU base; report it on the return |
| Excluded profession (décret 2-08-124) | CPU not available at any turnover | Route to ma-income-tax |
| No AMO membership | Condition of the option not met (Art. 41-II-B) | Enrol in AMO; confirm status with the tax office |
| Sale of land or buildings used in the business | Real-estate gains rules, not the 20% CPU rate (Note circulaire n° 737) | Route to the real-estate gains guide |
| Owner 65+, no pension, final closure in 2026 | 50% relief on intangible gains up to MAD 1,000,000 (Art. 31-V) | Check all four conditions |
| Mobile-payment turnover in 2025 or 2026 | Taxable in full; the exclusion ended with 2024 returns (Art. 247 ter) | Include it |

## Worked cases ([CGI Art. 40 and 73-II-B-6°](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1))

Cases 1, 2 and 5 use invented client figures with the 2026 rates. Cases 3, 4, 6 and 7 are the DGI's own published examples; the year of each is stated.

**Case 1: general food shop, 2026 turnover.** The shop's turnover is MAD 375,000 and the owner is an AMO member. The category is *Alimentation générale*, coefficient 6%.

- Professional income: 375,000 x 6% = MAD 22,500. IR component: 22,500 x 10% = MAD 2,250.
- Band 1,001 to 2,500, so the droit complémentaire is MAD 2,280.
- CPU for 2026 = 2,250 + 2,280 = MAD 4,530, due before 1 April 2027 (or in four quarterly instalments during 2027).
- The 2021 DGI guide used 8% for this trade. That coefficient belongs to the table abolished in 2022.

**Case 2: men's hairdresser, 2026 turnover.** Turnover is MAD 60,000. The category is *Coiffure et esthétique*, coefficient 20%.

- Professional income: 60,000 x 20% = MAD 12,000. IR component: 12,000 x 10% = MAD 1,200.
- Band 1,001 to 2,500, so the droit is MAD 2,280. CPU = 1,200 + 2,280 = MAD 3,480.

**Case 3: maintenance business with one large client (DGI example, 2023 turnover, [Note circulaire n° 733](https://www.tax.gov.ma/wps/wcm/connect/070abc0f-a958-4cf9-84be-7e9b76434063/NC+N%C2%B0+733+relative+aux+mesures+fiscales+de+la+LF+2023+vf.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-070abc0f-a958-4cf9-84be-7e9b76434063-oq2C8BE)).** A CPU taxpayer in *activités d'entretien* (coefficient 15%) is paid MAD 8,500 a month by business Y, which is taxed under RNR. The threshold is passed in October.

- Withholding in October: ((8,500 x 10) - 80,000) x 30% = MAD 1,500. In November and December: 8,500 x 30% = MAD 2,550 each.
- Total 2023 turnover is MAD 192,000, of which MAD 102,000 is from Y. CPU base: (192,000 - (102,000 - 80,000)) x 15% = MAD 25,500. IR: 25,500 x 10% = MAD 2,550.
- The DGI gives total tax paid, including withholding, as MAD 9,150.
- Not in the DGI example: the droit complémentaire for an IR component of 2,550 is in band 2,501 to 5,000, which is MAD 2,880.

**Case 4: two trades (DGI example, 2021 turnover under the 2022 table, [Note circulaire n° 732](https://tax.gov.ma/wps/wcm/connect/982a0f63-09eb-4c60-8b44-2f2a474dc865/Note+Circulaire+n+732+relative+aux+mesures+fiscales+de+la+LF+2022.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-982a0f63-09eb-4c60-8b44-2f2a474dc865-nWihlos)).** The taxpayer has MAD 500,000 of general food retail and MAD 1,000,000 of tobacco sales. Both are commerce, and the total of MAD 1,500,000 is within the MAD 2,000,000 ceiling.

- Base: (500,000 x 6%) + (1,000,000 x 3%) = MAD 60,000. IR: 60,000 x 10% = MAD 6,000.
- Droit (band 5,001 to 10,000): MAD 4,200. Total MAD 10,200.
- Paid quarterly, that is MAD 2,550 before 1 April, 1 July and 1 October, and before 1 January of the next year.

**Case 5: closing mid-year (method of the DGI practical guide, invented 2026 figures).** A maker of non-food goods (*Fabrication*, coefficient 10%) is an AMO member. He stops on 30 June 2026 and sells the business at a net gain of MAD 100,000. He is under 65, so the retirement relief does not apply. Turnover for January to June is MAD 90,000.

- IR component: 90,000 x 10% x 10% = MAD 900.
- To find the band, annualise it: 900 x 12 / 6 = 1,800, which is in band 1,001 to 2,500 (annual MAD 2,280). Pro-rate the droit: 2,280 x 6 / 12 = MAD 1,140.
- CPU for the part year: 900 + 1,140 = MAD 2,040. Gains tax: 100,000 x 20% = MAD 20,000, with form ADP160B within 45 days of the sale.

**Case 6: retirement relief (DGI example, 2026, [Note circulaire n° 737](https://www.tax.gov.ma/wps/wcm/connect/e48c5c9d-ae80-4b30-a1b3-80af7ec09be1/NC+737+LF+2026.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-e48c5c9d-ae80-4b30-a1b3-80af7ec09be1-pOvNbSq)).** The owner is 66 with no pension scheme and closes a manufacturing business for good. He sells the *fonds de commerce* for MAD 1,300,000.

- Equipment: sold for MAD 200,000, bought in 2014 for MAD 450,000. Deemed depreciation is 450,000 x 10% x 10 years, which wipes out the cost, so the gain is MAD 200,000.
- Intangibles: MAD 1,100,000 of self-created goodwill. Relief: 1,000,000 x 50% = MAD 500,000. Taxable intangible gain: 1,100,000 - 500,000 = MAD 600,000.
- Total taxable gain: 200,000 + 600,000 = MAD 800,000. IR: 800,000 x 20% = MAD 160,000.

**Case 7: selling one machine during activity (DGI example, 2022, [DGI CPU practical guide](https://www.tax.gov.ma/wps/wcm/connect/cecc3309-6ca8-494c-903b-160c1649cd9a/CPU+guide+pratique+Version+fran%C3%A7aise.pdf?MOD=AJPERES&CACHEID=cecc3309-6ca8-494c-903b-160c1649cd9a)).** A machine bought on 1 January 2016 for MAD 60,000 is sold on 1 July 2022 for MAD 36,000.

- Deemed depreciation: (60,000 x 10% x 6) + (60,000 x 10% x 6/12) = MAD 39,000. Net value: 60,000 - 39,000 = MAD 21,000.
- Gain: 36,000 - 21,000 = MAD 15,000. It is declared with spontaneous payment. At the 20% rate the tax is MAD 3,000 (our arithmetic; the DGI example stops at the gain).

## When to refuse or refer

- The activity is on the décret 2-08-124 list, or close to it (IT services, consulting, medical, legal, import or export): refuse CPU and route to ma-income-tax, or ask the tax office in writing.
- The trade could sit in two rows of the coefficient table with different coefficients: do not pick one. Check the category on the pre-filled SIMPL return or with the tax office.
- Turnover is over a ceiling in the current or previous year, or the client is moving between regimes: refer. The two-year exit, the three-year re-entry and VAT registration interact.
- The client is not an AMO member, or has AMO arrears: refer to the tax office and the AMO body before filing. The option condition and the droit may both be affected.
- Sale of the business, of goodwill or of land and buildings, or a claim to the 2026 retirement relief: refer to a Moroccan expert-comptable. Asset valuation (Art. 220 and 221) and the real-estate gains rules are outside this Guide.
- Late returns, penalties already charged, a DGI letter under Art. 221 bis, or an audit: refer.
- A company (SARL, SA) or an auto-entrepreneur: not CPU. Use the right Guide.

## Filing and payment ([CGI Art. 82 quater, 148, 173, 184, 208](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1))

| Obligation | Deadline | Form or channel |
| --- | --- | --- |
| Existence declaration (new business) | Within 30 days of starting (Art. 148) | DGI form, registered letter or against receipt |
| Change of tax domicile or main establishment | Within 30 days of the change (DGI guide; Art. 149) | Letter or DGI form |
| Annual turnover return, one line per activity | Before 1 April of the year after the turnover year (Art. 82 quater-I) | ADP150B on SIMPL (pre-filled), or paper |
| Annual payment option | Before 1 April of the following year (Art. 173-I) | RSP150B bordereau-avis; e-payment allowed |
| Quarterly payment option | Four instalments of 25% each, before the end of the 3rd, 6th, 9th and 12th month of the following year (Art. 173-I) | RSP150B, one per quarter |
| Gains and indemnities return with payment | Within 45 days of the sale or cessation (Art. 82 quater-II) | ADP160B and RSP160B |
| Leaving Morocco | Turnover return at least 30 days before departure (Art. 85-I) | ADP150B |
| Death | Heirs file within 3 months (Art. 85-II) | ADP150B |

What the turnover return contains (Art. 82 quater-I):

- identity and tax number;
- each activity and where it is carried on;
- the choice of annual or quarterly payment, which holds for the whole tax year;
- the AMO membership number and date, if any;
- service turnover above MAD 80,000 with the same client.

**Filing on SIMPL.** The DGI pre-fills the turnover return ([DGI CPU notice](https://www.tax.gov.ma/wps/wcm/connect/66026b2b-3420-4719-9c8b-2b9cdf64a494/Notice+explicative+CPU+2021.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-66026b2b-3420-4719-9c8b-2b9cdf64a494-ouzv3A9)). The taxpayer logs in with the tax number and national ID card, checks the figures, chooses the payment mode, adds the AMO details and pays by card or through a payment provider using the reference generated. If the pre-filled return is missing or wrong, file with the local tax office.

**Penalties.**

- **Late filing** (Art. 184): a 5% surcharge if filed within 30 days late, 15% if later, and 20% on an assessment made because no return, or an incomplete return, was filed. The surcharge is at least MAD 500.
- **Late payment** (Art. 208): a 10% penalty, cut to 5% if paid within 30 days of the due date. On top of that, a 5% surcharge for the first month and 0.5% for each further month or part month.

### Returns being filed now: 2025 turnover ([CGI Art. 82 quater and 173](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1))

- The return for 2025 turnover was due **before 1 April 2026**, with the same coefficients, 10% rate and droit bands as above. Mobile-payment turnover of 2025 is included in full.
- Annual option: payment was due before 1 April 2026. Quarterly option: instalments of 25% before the end of March, June, September and December 2026. The September instalment is due before the end of September 2026 and the December instalment before the end of December 2026.
- If the 2025 return is not yet filed, the Art. 184 surcharge is already 15% (more than 30 days late), with a MAD 500 minimum. Late payment adds the Art. 208 charges. File now and refer if an assessment has been issued.
- The 2026 retirement relief applies only to disposals from 1 January 2026, not to 2025 sales.

## Completion checklist

- Activity checked against décret 2-08-124 and the exclusion list ([décret n° 2-08-124](https://www.tax.gov.ma/wps/wcm/connect/24a95c1a-b857-432c-a516-8dc833bb445b/D%C3%A9cret+n%C2%B0+2-08-124+du+3+joumada+II+1430+%2828+mai+2009%29+relatif+aux+professions+ou+activit%C3%A9s+exclues+du+r%C3%A9gime+forfaitaire.pdf?MOD=AJPERES&CACHEID=24a95c1a-b857-432c-a516-8dc833bb445b)).
- Turnover per branch, VAT included, compared with the ceilings for the last two years (and three years for anyone arriving from RNS/RNR).
- AMO membership number and date recorded.
- Coefficient taken from the current Art. 40-I table, one per activity. The category matches the SIMPL pre-fill.
- Service turnover above the one-client threshold identified, withholding certificates or client statements collected, excess left out of the base and shown on the return.
- IR component computed. Droit band read from the annual IR, and pro-rated for a part year.
- Payment option chosen, and dates diarised (1 April, or the four quarter-ends).
- Any sale or cessation: gains return within 45 days, land and buildings split out, retirement relief conditions checked.
- Email address on file with the DGI. Purchase invoices kept.

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
