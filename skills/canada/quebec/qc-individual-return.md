---
name: qc-individual-return
description: >
  Quebec personal income tax return (TP-1, filed with Revenu Québec) for an individual resident in Quebec on 31 December, tax year 2026, with a dated section of full 2025 figures for the return being filed now. Covers the four Quebec brackets, the basic personal amount and main non-refundable credits at 14%, the worker deduction, QPP and QPIP for employees and the self-employed (Schedules U and R, line 248 deduction), the health services fund contribution (Schedule F, line 446), the drug insurance premium, deadlines, instalments, penalties and interest, and the 16.5% Quebec abatement on the federal T1. Trigger on "Quebec tax", "TP-1", "Revenu Québec", "impôt du Québec", "QPP self-employed", "RQAP", "FSS line 446", "Quebec abatement". Out of scope: the federal T1 computation (ca-fed-t1-return), CPP and EI (ca-fed-cpp-ei), business income rules (ca-fed-t2125), QST (qc-qst-return), employer payroll (qc-employer-contributions), companies (qc-corporate-tax-co17).
version: 2.1
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-08
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Quebec: individual income tax return (TP-1) v2.1

> **General reference only.** This skill is tax reference material for AI-assisted work. It has not been reviewed for any specific person's facts. Figures were read from Revenu Québec and canada.ca on 8 November 2026.

## Who this applies to

An individual who was resident in Quebec on 31 December of the tax year. Quebec is the only province that administers and collects its own personal income tax. A Quebec resident files two returns: the federal T1 with the CRA, and the TP-1 with Revenu Québec. There is no provincial tax form inside the federal return for Quebec, and the CRA does not collect Quebec tax. Compute Quebec income on its own: Quebec deductions (the worker deduction, the line 248 QPP and QPIP deduction) differ from the federal ones, so do not copy federal taxable income across.

The TP-1 guide (TP-1.G, 2025) says you must file if you were resident in Quebec on 31 December 2025 and you owe any of these: income tax, a QPP contribution, a QPIP premium or a health services fund (FSS) contribution. You must also file if, among other cases, you disposed of capital property, you owe the drug insurance premium, you were resident in Quebec on the day you stopped being resident in Canada, or you lived elsewhere in Canada and carried on a business in Quebec.

Out of this skill: the federal tax computation (see `ca-fed-t1-return`), CPP and EI (see `ca-fed-cpp-ei`), how business income is measured (see `ca-fed-t2125`), QST (see `qc-qst-return`), employer contributions (see `qc-employer-contributions`), companies, which file the CO-17 (see `qc-corporate-tax-co17`), and residency tests (see `ca-tax-residency`).

## Rates, bands and thresholds

### Tax year 2026 (primary)

Revenu Québec indexed the personal tax system by 2.05% for 2026. Rates did not change; thresholds did. The 2026 TP-1 forms are not yet published, so line references below follow the 2025 forms.

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Indexation rate of the personal tax system | 2.05% | 2026 | https://www.revenuquebec.ca/fr/entreprises/retenues-a-la-source-et-cotisations-de-lemployeur/employeur-principaux-changements-2026/ |
| Bracket 1: taxable income up to 54,345 $ | 14% | 2026 | https://www.revenuquebec.ca/fr/citoyens/declaration-de-revenus/produire-votre-declaration-de-revenus/taux-dimposition/ |
| Bracket 2: over 54,345 $ up to 108,680 $ | 19% | 2026 | https://www.revenuquebec.ca/fr/citoyens/declaration-de-revenus/produire-votre-declaration-de-revenus/taux-dimposition/ |
| Bracket 3: over 108,680 $ up to 132,245 $ | 24% | 2026 | https://www.revenuquebec.ca/fr/citoyens/declaration-de-revenus/produire-votre-declaration-de-revenus/taux-dimposition/ |
| Bracket 4: over 132,245 $ | 25.75% | 2026 | https://www.revenuquebec.ca/fr/citoyens/declaration-de-revenus/produire-votre-declaration-de-revenus/taux-dimposition/ |
| Basic personal amount (line 350) | 18,952 $ | 2026 | https://www.revenuquebec.ca/fr/entreprises/retenues-a-la-source-et-cotisations-de-lemployeur/employeur-principaux-changements-2026/ |
| Amount transferred from one spouse to the other | 18,952 $ | 2026 | same page |
| Amount for other dependants | 5,684 $ | 2026 | same page |
| Amount for a minor child in post-secondary studies, per term | 3,901 $ | 2026 | same page |
| Person living alone | 2,172 $ | 2026 | same page |
| Additional amount, person living alone (single-parent family) | 2,681 $ | 2026 | same page |
| Age amount (65 or over) | 3,986 $ | 2026 | same page |
| Retirement income amount (maximum) | 3,541 $ | 2026 | same page |
| Reduction threshold for the age, living-alone and retirement amounts (family income) | 42,955 $ | 2026 | same page |
| Severe and prolonged impairment amount | 4,208 $ | 2026 | same page |
| Career extension amount: first dollars excluded / maximum eligible work income / reduction threshold | 7,655 $ / 12,755 $ / 57,660 $ | 2026 | same page |
| Worker deduction (line 201), maximum | 1,450 $ | 2026 | same page |
| QPP: maximum pensionable earnings / basic exemption / maximum contributory earnings | 74,600 $ / 3,500 $ / 71,100 $ | 2026 | same page |
| QPP employee rate (base 5.30% + first additional 1%), employee maximum | 6.30%, 4,479.30 $ | 2026 | same page |
| QPP2 (second additional): additional maximum pensionable earnings / band / employee rate / employee maximum | 85,000 $ / 10,400 $ / 4% / 416 $ | 2026 | same page |
| QPP self-employed: base 10.6% + first additional 2% = 12.6%; second additional 8% | 12.6% and 8% | 2026 | https://www.revenuquebec.ca/fr/citoyens/declaration-de-revenus/payer-ou-etre-rembourse/paiement-des-cotisations/cotisations-du-travailleur-autonome-ou-du-membre-dune-societe-de-personnes/cotisation-du-travailleur-autonome-ou-du-membre-dune-societe-de-personnes-au-regime-de-rentes-du-quebec/ |
| QPP self-employed maximums (computed: 71,100 $ x 12.6%; 10,400 $ x 8%) | 8,958.60 $; 832.00 $ | 2026 | https://www.revenuquebec.ca/fr/citoyens/declaration-de-revenus/produire-votre-declaration-de-revenus/travailleurs-autonomes-preparez-votre-declaration/travailleurs-autonomes-tables-dimpot-et-de-cotisations/ (computed from the rates above; the 2026 estimate table shows 9,791 $ in total at high income) |
| QPIP: maximum insurable earnings / employee rate / employee maximum | 103,000 $ / 0.430% / 442.90 $ | 2026 | https://www.revenuquebec.ca/fr/entreprises/retenues-a-la-source-et-cotisations-de-lemployeur/calcul-des-retenues-et-des-cotisations/cotisations-au-rqap/maximum-de-revenus-assurables-et-taux-de-cotisation/ |
| QPIP self-employed rate, maximum premium (on up to 103,000 $) | 0.764%, 786.92 $ | 2026 | https://www.quebec.ca/entreprises-et-travailleurs-autonomes/administrer-gerer/embauche-gestion-personnel/assurance-parentale/taux-cotisations |
| FSS (health services fund) on non-employment income, caps shown in the 2026 estimate table | 150 $ in the middle band, 1,000 $ maximum | 2026 | same page |
| Interest on amounts owed to Revenu Québec, compounded daily | 8% (Jan to Mar), 7% (Apr to Dec) | 2026 | https://www.revenuquebec.ca/fr/une-mission-des-actions/assurer-la-conformite-fiscale/penalites-et-interets/taux-dinteret-sur-les-creances/ |
| Quebec abatement on the federal T1 (line 44000) | 16.5% of basic federal tax | 2026 | https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/pyrll/t4032/2026/t4032-qc-1-26e.pdf |

Credit rate. The basic personal amount and the other amounts on lines 350 to 376 are added at line 377 and multiplied by 14% (line 377.1 of the TP-1). The 14% is the lowest bracket rate. Other credit rates on the 2025 return: medical expenses 20% (line 389), union and professional dues 10% (line 397), donations 20% on the first 200 $ and 24% or 25.75% above it.

No separate QPP, QPIP or EI credit. Revenu Québec says the basic personal amount "tient compte des cotisations payées" to the QPP, QPIP, the FSS and EI. An employee's base QPP contributions and QPIP and EI premiums give no separate Quebec credit. Only the enhanced QPP parts and, for the self-employed, the employer-equivalent parts are deducted at line 248.

The line 248 factors are 2025 figures. The Schedule U factors (0.156250 for an employee; 0.421875 and 0.156250 for the self-employed) and the Schedule R share (43.736%) are on the 2025 forms and match the 2025 rates (6.4% employee QPP, 12.8% self-employed QPP, 0.878% self-employed QPIP). The 2026 rates differ (6.30%, 12.6%, 0.764%), so do not apply the 2025 factors to a 2026 contribution; the 2026 schedules are not yet published.

### Tax year 2025 (dated section: the return filed in 2026)

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Bracket 1: taxable income up to 53,255 $ | 14% | 2025 | https://www.revenuquebec.ca/fr/citoyens/declaration-de-revenus/produire-votre-declaration-de-revenus/taux-dimposition/ |
| Bracket 2: over 53,255 $ up to 106,495 $ | 19% | 2025 | same page |
| Bracket 3: over 106,495 $ up to 129,590 $ | 24% | 2025 | same page |
| Bracket 4: over 129,590 $ | 25.75% | 2025 | same page |
| Tax at the start of brackets 2, 3, 4 (grille de calcul 401) | 7,455.70 $; 17,571.30 $; 23,114.10 $ | 2025 | https://www.revenuquebec.ca/documents/fr/formulaires/tp/2025-12/TP-1.D.GR%282025-12%29.pdf |
| Basic personal amount (line 350) | 18,571 $ | 2025 | https://www.revenuquebec.ca/fr/citoyens/declaration-de-revenus/produire-votre-declaration-de-revenus/comment-remplir-votre-declaration-de-revenus/aide-par-ligne/350-a-398-1-credits-dimpot-non-remboursables/ligne-350/ |
| Non-refundable credit rate (line 377.1) | 14% | 2025 | https://www.revenuquebec.ca/documents/fr/formulaires/tp/2025-12/TP-1.D%282025-12%29.pdf |
| Person living alone (Schedule B, line 20) | 2,128 $ | 2025 | https://www.revenuquebec.ca/documents/fr/formulaires/tp/2025-12/TP-1.D.B%282025-12%29.pdf |
| Age amount, born before 1 January 1961 (Schedule B, line 22) | 3,906 $ | 2025 | same schedule |
| Retirement income amount: eligible income x 1.25, maximum | 3,470 $ | 2025 | same schedule |
| Reduction of the Schedule B amounts: 18.75% of family income over | 42,090 $ | 2025 | same schedule |
| Additional amount, single-parent family | 2,627 $ | 2025 | https://www.revenuquebec.ca/documents/fr/formulaires/tp/2025-12/TP-1.G%282025-12%29.pdf |
| Severe and prolonged impairment amount | 4,123 $ | 2025 | same guide |
| Worker deduction (line 201): 6% of eligible work income, maximum | 1,420 $ | 2025 | same guide; grille 201 |
| QPP: maximum pensionable earnings / exemption / additional maximum | 71,300 $ / 3,500 $ / 81,200 $ | 2025 | https://www.revenuquebec.ca/documents/fr/formulaires/tp/2025-12/TP-1.D.U%282025-12%29.pdf |
| QPP self-employed rate (base 10.8% + first additional 2%), Schedule U line 48 | 12.8% | 2025 | same schedule; rates also on the Revenu Québec self-employed QPP page |
| QPP self-employed second additional (Schedule U line 93) | 8% | 2025 | same schedule |
| QPP self-employed maximums (computed: 67,800 $ x 12.8%; 9,900 $ x 8%) | 8,678.40 $; 792.00 $ | 2025 | https://www.revenuquebec.ca/documents/fr/formulaires/tp/2025-12/TP-1.D.U%282025-12%29.pdf (computed from the Schedule U figures above) |
| QPP employee maximum (Schedule U line 10) | 4,339.20 $ | 2025 | same schedule |
| Line 248 QPP deduction factors, self-employed (Schedule U lines 101, 103) | 0.421875 and 0.156250 of the line 48 contribution, plus the full second additional contribution (line 115) | 2025 | same schedule |
| QPIP self-employed rate, maximum (Schedule R line 24) | 0.878%, 860.44 $ | 2025 | https://www.revenuquebec.ca/documents/fr/formulaires/tp/2025-12/TP-1.D.R%282025-12%29.pdf |
| QPIP maximum insurable earnings | 98,000 $ | 2025 | same schedule |
| QPIP deduction (Schedule R line 26), share of the self-employed premium | 43.736% | 2025 | same schedule |
| QPIP employee rate (also used for work outside Quebec, Schedule R Part B), employee maximum | 0.494%, 484.12 $ | 2025 | same schedule; RQAP rate page |
| No QPIP if net business income plus insurable employment income is under | 2,000 $ | 2025 | same schedule |
| FSS (Schedule F): no contribution if income is 18,130 $ or less | 18,130 $ | 2025 | https://www.revenuquebec.ca/documents/fr/formulaires/tp/2025-12/TP-1.D.F%282025-12%29.pdf |
| FSS: income up to 63,060 $: 1% of income over 18,130 $, maximum | 150 $ | 2025 | same schedule |
| FSS: income over 63,060 $: 150 $ plus 1% of income over 63,060 $, maximum | 1,000 $ | 2025 | same schedule |
| Drug insurance premium (line 447), maximum for the year | 755 $ | 2025 | https://www.revenuquebec.ca/fr/citoyens/declaration-de-revenus/produire-votre-declaration-de-revenus/principaux-changements-2025/ |
| No drug insurance premium if no spouse and line 275 does not exceed | 19,890 $ | 2025 | same page |
| Interest on amounts owed, compounded daily | 9% (Jan to Mar), 8% (Apr to Dec) | 2025 | https://www.revenuquebec.ca/fr/une-mission-des-actions/assurer-la-conformite-fiscale/penalites-et-interets/taux-dinteret-sur-les-creances/ |
| Solidarity tax credit, July 2026 to June 2027 (based on 31 December 2025): no credit at family income of | 64,545 $ single; 70,395 $ couple; 64,545 $ single parent; plus 2,634 $ per child for couples and single parents | 2025 | https://www.revenuquebec.ca/fr/citoyens/credits-dimpot/credit-dimpot-pour-solidarite/calcul-du-credit-dimpot-pour-solidarite/ |
| Quebec abatement on the federal T1 (line 44000) | 16.5% of basic federal tax | 2025 | https://www.canada.ca/en/department-finance/programs/federal-transfers/quebec-abatement.html |

## The base

The TP-1 builds up in this order (2025 line numbers):

1. Total income, line 199. Employment income from the RL-1 at line 101. Net business income from Schedule L (Schedule L line 27 is part of the net business income that goes to line 164). Business income is measured under the business-income rules (see `ca-fed-t2125`); Quebec uses form TP-80 for the statement of business income.
2. Deductions, lines 201 to 252. The worker deduction at line 201 is 6% of eligible work income (employment income plus net business income), capped at 1,420 $ for 2025 and 1,450 $ for 2026. Line 248 holds the QPP and QPIP deduction (box 248.1 says which case applies).
3. Net income, line 275. This is also the figure used for family income in Schedule B, the solidarity credit and the drug insurance premium.
4. Taxable income, line 299, after lines 276 to 297 (losses of other years, capital gains deduction, and other deductions).
5. Tax on taxable income, line 401, from grille de calcul 401 (the four brackets).
6. Non-refundable credits, line 399: the line 377 amounts x 14% (line 377.1), plus medical expenses x 20%, donations, dues and the others. Line 413 is line 401 minus line 406.
7. Line 432 is Quebec income tax after the remaining credits.
8. Contributions added on top (line 450 total): QPIP for self-employment or work outside Quebec (line 439, Schedule R), QPP for self-employment (line 445, Schedule U), FSS (line 446, Schedule F), drug insurance premium (line 447, Schedule K).

QPP for an employee. The employer withholds QPP on the RL-1. On the TP-1 the employee deducts at line 248 only the enhanced part: Schedule U Part B takes the smaller of the QPP contribution x 0.156250 (2025) and 1% of pensionable salary (capped at the maximum pensionable earnings) above the 3,500 $ exemption, plus the second additional contribution (4% band). For 2026 the first additional rate is still 1% of contributory earnings (the 2026 employee rate is 5.30% base plus 1% first additional).

QPP for the self-employed (Schedule U Part C). Quebec residents contribute to the QPP, never the CPP, on Quebec work. The contribution is 12.8% (2025) or 12.6% (2026) of net business income above 3,500 $, up to the maximum pensionable earnings, plus 8% on the band up to the additional maximum. It goes on line 445. The line 248 deduction is 0.421875 + 0.156250 of the line 48 contribution (the employer-equivalent base part plus the whole first additional part) plus the whole second additional contribution. If the client also had CPP earnings outside Quebec (lines 96 to 96.2), use form LE-35 instead.

QPIP for the self-employed (Schedule R). QPIP pays maternity, paternity, adoption and parental benefits in Quebec in place of those EI benefits. The 2025 premium is 0.878% of net business income up to 98,000 $ less insurable employment income already in RL-1 box I; for 2026 the self-employed rate is 0.764% on up to 103,000 $ (maximum 786.92 $). 43.736% of the premium is deductible at line 248.

FSS (Schedule F). The base is total income less employment income and less listed amounts (old age security, dividends grossed up, support, social assistance and others), less some deductions, including the QPIP deduction (Schedule R line 26) and the QPP deduction amounts (Schedule U lines 101, 103 and 115). Employment income is never in the FSS base. The FSS paid cannot be claimed as a medical expense.

QPP stops. Since 1 January 2024 a worker aged 65 or over who receives a QPP or CPP retirement pension can elect to stop contributing; the obligation stops for workers over 72.

## Deadlines and filing

- Return for 2025: file by 30 April 2026. If you or your spouse carried on a business in 2025, the filing deadline is 15 June 2026. The 2026 return follows the same pattern (30 April 2027, or 15 June 2027 with business income) once the 2026 guide confirms it.
- Payment: any balance for 2025 was due 30 April 2026, even for the self-employed. Interest runs from 1 May 2026.
- Electronic filing for 2025 opened mid-February 2026; processing began 9 March 2026.
- Instalments: four a year, by 15 March, 15 June, 15 September and 15 December. They are required for 2026 if the net tax you expect to owe for 2026 is over 1,800 $ and your net tax payable for 2025 or 2024 was over 1,800 $ (net tax payable is tax for the year less Quebec tax withheld and refundable credits). Revenu Québec sends form TPZ-1026.A in February and August; without it, compute instalments on form TP-1026. Instalments also cover QPP, QPIP, FSS and the drug insurance premium.
- Reassessment: Revenu Québec generally has three years from the notice of assessment.
- Refund or reduction requests: generally up to ten calendar years back (in 2026, years 2016 to 2025).
- Foreign property: from 2025, report specified foreign property costing more than 100,000 $ CA at any time in the year on form TP-1079.8.BE (line 25).

## Penalties and interest

- Late filing with a balance owing: 5% of the unpaid balance at the filing deadline, plus 1% for each full month late, up to 12 months. The guide's example: filed 20 July 2026, due 30 April 2026, penalty 7%.
- Interest on any balance owing, compounded daily, at the quarterly rate: 9% then 8% in 2025; 8% in January to March 2026, then 7% to 31 December 2026.
- Late or short instalments: interest at the same rate, plus 10% a year extra if an individual paid less than 75% of the amount required.
- Refund interest for 2025 runs from 15 June 2026 if filed before 1 May 2026, or from the 46th day after filing if filed later.

## Cross-border points

- Residence on 31 December decides Quebec tax for the whole year. A person resident in Quebec on the day they left Canada files a TP-1 for that year. Part-year residents of Canada prorate certain credits (Revenu Québec publication IN-119).
- Quebec resident with a business in Canada outside Quebec: tick box 403 and use form TP-22. The FSS is then Schedule F line 82 x the TP-22 line 35 percentage.
- Resident elsewhere in Canada with a business in Quebec: tick box 403 and use form TP-25.
- Federal side: the CRA gives a Quebec resident a refundable abatement of 16.5% of basic federal tax on line 44000 of the T1. Use form T2203 if the business has a permanent establishment outside Quebec, or if the person was not a Quebec resident on 31 December but the business has a permanent establishment in Quebec.
- Work outside Quebec without an RL-1: Schedule R Part B charges QPIP at the employee rate (0.494% for 2025) on that income.
- CPP contributions from work outside Quebec: compute QPP and the deduction on form LE-35, not Schedule U.
- Federal EI for Quebec employees is covered in `ca-fed-cpp-ei`.

## Two worked examples that recompute

Example 1 (2026, employee). A single employee under 65, not living alone, with 60,000 $ of salary on the RL-1, no other income, covered by a group drug plan. Worker deduction: 6% of 60,000 $ is 3,600 $, capped at 1,450 $. Line 248: the enhanced QPP part, 1% of (60,000 $ minus 3,500 $) = 565 $ (the 2025 Schedule U Part B method with 2026 figures). Taxable income (line 299) is 57,985 $. Line 401: 14% of 54,345 $ is 7,608.30 $, plus 19% of the 3,640 $ above it, 691.60 $, total 8,299.90 $. Line 377.1: 18,952 $ x 14% = 2,653.28 $. Quebec tax at line 432 is 5,646.62 $. No FSS: Schedule F takes out employment income. On the federal T1, if basic federal tax is 6,000 $, the Quebec abatement on line 44000 is 990 $.

```oa-check
name: Quebec employee, salary 60,000 (2026 figures)
inputs:
  salary: 60000
  basic_federal_tax: 6000
steps:
  - line201: min(salary * 0.06, 1450)
  - line248: (min(salary, 74600) - 3500) * 0.01
  - line299: salary - line201 - line248
  - line401: min(line299, 54345) * 0.14 + max(min(line299, 108680) - 54345, 0) * 0.19 + max(min(line299, 132245) - 108680, 0) * 0.24 + max(line299 - 132245, 0) * 0.2575
  - line3771: 18952 * 0.14
  - line432: line401 - line3771
  - abatement: basic_federal_tax * 0.165
expected:
  line201: 1450.00
  line248: 565.00
  line299: 57985.00
  line401: 8299.90
  line432: 5646.62
  abatement: 990.00
```

Example 2 (2025, self-employed). A single sole proprietor under 65, not living alone, with 50,000 $ of net business income (Schedule L) and no other income, covered by a private drug plan so line 447 is nil. Schedule U: QPP = 12.8% of (50,000 $ minus 3,500 $) = 5,952 $ on line 445; no second additional contribution below 71,300 $. Deduction: 5,952 $ x (0.421875 + 0.15625) = 3,441 $. Schedule R: QPIP = 0.878% of 50,000 $ = 439 $ on line 439; deduction 43.736% = 192 $. Line 248 = 3,633 $. Line 201 = 1,420 $ (the cap, since 6% is 3,000 $). Taxable income 44,947 $, all in the 14% bracket: line 401 = 6,292.58 $. Line 377.1 = 18,571 $ x 14% = 2,599.94 $. Line 432 = 3,692.64 $. Schedule F: 50,000 $ less 192 $ and 3,441 $ = 46,367 $; 1% of the part over 18,130 $ is 282.37 $, capped at 150 $. Line 450 = 3,692.64 $ + 439 $ + 5,952 $ + 150 $ = 10,233.64 $, payable by 30 April 2026 even though the return is due 15 June 2026.

```oa-check
name: Quebec sole proprietor, net business income 50,000 (2025 TP-1)
inputs:
  nbi: 50000
steps:
  - line445: (min(nbi, 71300) - 3500) * 0.128
  - qpp_ded: line445 * 0.421875 + line445 * 0.15625
  - line439: min(nbi, 98000) * 0.00878
  - qpip_ded: round(line439 * 0.43736, 2)
  - line248: qpp_ded + qpip_ded
  - line201: min(nbi * 0.06, 1420)
  - line299: nbi - line201 - line248
  - line401: min(line299, 53255) * 0.14 + max(min(line299, 106495) - 53255, 0) * 0.19 + max(min(line299, 129590) - 106495, 0) * 0.24 + max(line299 - 129590, 0) * 0.2575
  - line3771: 18571 * 0.14
  - line432: line401 - line3771
  - fss_base: nbi - qpip_ded - qpp_ded
  - line446: min(max(fss_base - 18130, 0) * 0.01, 150)
  - line450: line432 + line439 + line445 + line446
expected:
  line445: 5952.00
  line439: 439.00
  line248: 3633.00
  line299: 44947.00
  line401: 6292.58
  line432: 3692.64
  line446: 150.00
  line450: 10233.64
```

## Ask the client first

1. Where did you live on 31 December, and did you arrive in or leave Canada during the year?
2. What income did you have: RL-1 employment, net business income (TP-80), pension, investment? Did any business have a place of business outside Quebec?
3. Did you have a spouse on 31 December, and what was their net income (line 275)? Any dependants, and their ages? Did you live alone all year? Your age? Your address and rent or property tax situation (for the solidarity credit)?
4. Are you covered by a private group drug plan all year, or by the RAMQ public plan?
5. Did you pay CPP outside Quebec, or have you elected to stop QPP at 65 or over?
6. Did you pay instalments, and did you hold foreign property costing over 100,000 $ CA?

## Sources

| Source | URL | Read on |
|---|---|---|
| Revenu Québec, Taux d'imposition, read for the 2026 and 2025 brackets | https://www.revenuquebec.ca/fr/citoyens/declaration-de-revenus/produire-votre-declaration-de-revenus/taux-dimposition/ | 2026-11-08 |
| Revenu Québec, Employeur: principaux changements 2026, read for indexation, credit amounts, worker deduction, QPP and QPIP | https://www.revenuquebec.ca/fr/entreprises/retenues-a-la-source-et-cotisations-de-lemployeur/employeur-principaux-changements-2026/ | 2026-11-08 |
| Revenu Québec, Cotisation du travailleur autonome au RRQ, read for the 2025 and 2026 self-employed rates and the 65-plus election | https://www.revenuquebec.ca/fr/citoyens/declaration-de-revenus/payer-ou-etre-rembourse/paiement-des-cotisations/cotisations-du-travailleur-autonome-ou-du-membre-dune-societe-de-personnes/cotisation-du-travailleur-autonome-ou-du-membre-dune-societe-de-personnes-au-regime-de-rentes-du-quebec/ | 2026-11-08 |
| Revenu Québec, Maximum de revenus assurables et taux de cotisation au RQAP, read for the 2025 and 2026 rows | https://www.revenuquebec.ca/fr/entreprises/retenues-a-la-source-et-cotisations-de-lemployeur/calcul-des-retenues-et-des-cotisations/cotisations-au-rqap/maximum-de-revenus-assurables-et-taux-de-cotisation/ | 2026-11-08 |
| Revenu Québec, Travailleurs autonomes: tables d'impôt et de cotisations, read for the 2026 estimate tables (not an official calculation) | https://www.revenuquebec.ca/fr/citoyens/declaration-de-revenus/produire-votre-declaration-de-revenus/travailleurs-autonomes-preparez-votre-declaration/travailleurs-autonomes-tables-dimpot-et-de-cotisations/ | 2026-11-08 |
| Revenu Québec, Principaux changements 2025, read in full | https://www.revenuquebec.ca/fr/citoyens/declaration-de-revenus/produire-votre-declaration-de-revenus/principaux-changements-2025/ | 2026-11-08 |
| Revenu Québec, aide par ligne, read for lines 248, 350, 401, 439 and 446 | https://www.revenuquebec.ca/fr/citoyens/declaration-de-revenus/produire-votre-declaration-de-revenus/comment-remplir-votre-declaration-de-revenus/aide-par-ligne/ | 2026-11-08 |
| Revenu Québec, Guide de la déclaration de revenus TP-1.G (2025-12), read for filing, payment, penalty, instalment, foreign property and lines 201, 350, 395, 446 | https://www.revenuquebec.ca/documents/fr/formulaires/tp/2025-12/TP-1.G%282025-12%29.pdf | 2026-11-08 |
| Revenu Québec, TP-1.D return, grilles de calcul and Schedules B, F, L, R, U (2025-12), read in full for the lines cited | https://www.revenuquebec.ca/fr/services-en-ligne/formulaires-et-publications/details-courant/tp-1/ | 2026-11-08 |
| Revenu Québec, Taux d'intérêt sur les créances and intérêt supplémentaire sur acomptes, read for the 2025 and 2026 quarters | https://www.revenuquebec.ca/fr/une-mission-des-actions/assurer-la-conformite-fiscale/penalites-et-interets/taux-dinteret-sur-les-creances/ | 2026-11-08 |
| Revenu Québec, Calcul du crédit d'impôt pour solidarité, read for the July 2026 to June 2027 thresholds | https://www.revenuquebec.ca/fr/citoyens/credits-dimpot/credit-dimpot-pour-solidarite/calcul-du-credit-dimpot-pour-solidarite/ | 2026-11-08 |
| Gouvernement du Québec, Taux de cotisations au RQAP, read for the 2025 and 2026 employee, employer and self-employed rates | https://www.quebec.ca/entreprises-et-travailleurs-autonomes/administrer-gerer/embauche-gestion-personnel/assurance-parentale/taux-cotisations | 2026-11-08 |
| CRA, T4032-QC Payroll Deductions Tables, January 2026, read for the Quebec tax abatement part | https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/pyrll/t4032/2026/t4032-qc-1-26e.pdf | 2026-11-08 |
| Finance Canada, Quebec Abatement, read in full | https://www.canada.ca/en/department-finance/programs/federal-transfers/quebec-abatement.html | 2026-11-08 |
| CRA, Line 44000 Refundable Quebec abatement, read in full | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-44000-refundable-quebec-abatement.html | 2026-11-08 |

Not yet confirmed: the Taxation Act (CQLR c. I-3) and the Act respecting the RAMQ (c. R-5) articles behind these figures, because legisquebec.gouv.qc.ca returned 502 errors on 8 November 2026 (the old references, s. 750 for rates, s. 752 and following for credits, s. 1029.8.116.12 and following for the solidarity credit, R-5 s. 34 for the FSS, and ITA s. 120(2) for the abatement, are not re-checked). 2026 figures not yet on a 2026 form: the FSS thresholds (2025: 18,130 $ and 63,060 $), the drug insurance premium maximum, the Schedule U and R deduction factors, and the 2026 filing dates. Solidarity credit component amounts (QST, housing, northern village) and its reduction rate. Work premium (Schedule P) parameters. Other 2025 credit amounts not listed above (other dependants, post-secondary child). Detailed TP-22 and TP-25 allocation rules.
