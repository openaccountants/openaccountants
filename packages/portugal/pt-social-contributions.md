---
name: pt-social-contributions
description: "Portuguese social security contributions (Segurança Social) for tax year 2026 under the Código dos Regimes Contributivos (Lei 110/2009). Covers self-employed workers (trabalhadores independentes): 21.4% (25.2% for empresários em nome individual and EIRL holders), relevant income at 70% of services and 20% of goods, the quarterly declaration and the monthly payment from the 10th to the 20th, the EUR 20 minimum, the first-12-months rule, the 4 x IAS exemption with employment and the 12 x IAS ceiling on the 2026 IAS of EUR 537.13, organised accounts, the 25% option, and contracting entities (10% or 7%). Also the headline employee and employer rates (11% and 23.75%), special rates, members of corporate bodies (MOE), employer deadlines, fines and late interest. Trigger on: 'Segurança Social independente', 'declaração trimestral', 'recibos verdes contribuições', 'entidade contratante', 'MOE gerente', 'TSU'. Out of scope: payroll computation (portugal-payroll), IRS (pt-income-tax), cross-border cover (pt-cross-border)."
version: 2.1
jurisdiction: PT
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Portugal: social security contributions (tax year 2026)

> Source-cited draft: not reviewed by an accountant.

This skill computes Portuguese social security contributions for 2026. Its core is the self-employed regime (trabalhadores independentes, recibos verdes). It also gives the headline rates for employees, employers and members of corporate bodies, and the duty of companies that buy most of a freelancer's work (entidades contratantes).

The law is the Código dos Regimes Contributivos do Sistema Previdencial de Segurança Social (the Code), approved by Lei n.º 110/2009 and last amended by Decreto-Lei n.º 127/2025 with effect from 1 January 2026. Articles were read in the consolidated text on the Diário da República on 2026-10-24. The 2026 IAS (indexante dos apoios sociais) is EUR 537.13 (Portaria n.º 480-A/2025/1, art. 2).

Sibling skills, which this one links to and does not repeat:

- `portugal-payroll`: the monthly payroll run, what pay is subject to contributions, IRS withholding, net pay and employer cost.
- `pt-income-tax`: IRS on self-employed income, including how contributions reduce taxable income.
- `pt-cross-border`: residence, people arriving and leaving, and which country's social security applies.

## Who this applies to

**Self-employed workers.** A person who carries on a profession or business on their own account is covered by the self-employed regime (Code art. 132 and following). This includes recibos verdes freelancers, empresários em nome individual and EIRL holders, and their spouses or partners who work with them regularly.

**Not covered** (Code art. 139 and the ISS Guia Prático): lawyers and solicitadores in their own pension fund; people temporarily working in Portugal who already have compulsory cover elsewhere for invalidity, old age and death (they must ask for exclusion, form RV 1025); small farmers producing mainly for own use with yearly income up to 4 x IAS (EUR 2,148.52, form RV 1027); farmers whose only such income is Common Agricultural Policy subsidies below 4 x IAS a year; owners of local and coastal fishing boats who work as crew, marine harvesters and shore fishers (they have their own regime, Code art. 97 to 99); Category B income only from small renewable power production or from rent and local lodging (alojamento local) in a house or flat. A person who works for the same entity, or the same group, both as employee or MOE and as a freelancer is treated as an employee for that work; the employee or MOE rates apply to the fees.

**When cover starts.** The AT tells Segurança Social when someone opens activity. The person is registered automatically. For a first-ever start, cover takes effect on the first day of the 12th month after the month activity started (Code art. 145(1)). Activity started in January 2026 means contributions from 1 January 2027. If activity stops during those 12 months, the count is suspended and resumes on restart within 12 months (art. 145(4)). On a restart after an earlier period of activity, cover takes effect on the first day of the month of restart (art. 145(3)). A person may ask to start earlier through a quarterly declaration; cover then starts on the first day of that declaration month and the EUR 20 minimum applies until the first declared base.

**Exempt while covered** (Code art. 157(1)). No self-employed contributions are due:

- with employment for a different, unrelated employer that gives full social protection, at an average salary of at least 1 x IAS (EUR 537.13), while monthly average relevant income is below 4 x IAS (EUR 2,148.52). Above that, contributions are due on the excess only (art. 163(4));
- for a person receiving an invalidity or old-age pension, national or foreign, where the work is compatible with the pension;
- for a person receiving an occupational-risk pension with incapacity of 70% or more;
- from January, for a person who in the previous year only paid the EUR 20 minimum (art. 157(1)(d) with 163(2)), while that stays true.

Exemption is automatic when Segurança Social already knows the facts; otherwise the person files form RC 3001 and it starts the month after the request (art. 157(2), ISS Guia Prático).

**Employees and companies.** Employers pay contributions on pay under the general regime (art. 53). Members of corporate bodies (membros dos órgãos estatutários, MOE) such as gerentes and directors are covered by Code art. 61 and following. Unpaid MOE of for-profit companies are excluded if they have other compulsory cover with pay above 1 x IAS, or are invalidity or old-age pensioners (art. 64). The payroll run is in `portugal-payroll`.

**Contracting entities** (entidades contratantes, art. 140). A company, or an individual with business activity, that in one calendar year receives more than 50% of a self-employed worker's total activity value pays its own contribution. This applies only where the worker is liable to contribute and has yearly service income of at least 6 x IAS (EUR 3,222.78). Group companies count as one entity.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| IAS | EUR 537.13 | 2026 | Portaria 480-A/2025/1, art. 2: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_480_A_2025_1.pdf |
| Self-employed rate | 21.4% | 2026 | Code art. 168(1): https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575 |
| Empresário em nome individual, EIRL holder and their spouses | 25.2% | 2026 | Code art. 168(4) |
| Relevant income: services | 70% of the quarter's service income | 2026 | Code art. 162(1)(a) |
| Relevant income: goods, and hotel, restaurant and drinks services declared as such | 20% | 2026 | Code art. 162(1)(b) and (2) |
| Relevant income with organised accounts | prior-year taxable profit; monthly base = 1/12, minimum 1.5 x IAS (EUR 805.70) | 2026 | Code art. 162(3), 163(3); ISS Guia Prático |
| Monthly base | 1/3 of the quarter's relevant income, for the declaration month and the next two | 2026 | Code art. 163(1) |
| Minimum contribution | EUR 20.00 a month when there is no income or the result is below EUR 20 | 2026 | Code art. 163(2); ISS Guia Prático (2026 edition) |
| Ceiling on the monthly base | 12 x IAS = EUR 6,445.56 | 2026 | Code art. 163(5) |
| Exemption with employment | monthly average relevant income below 4 x IAS = EUR 2,148.52; above it, base = excess | 2026 | Code art. 157(1)(a), 163(4) |
| Option on the base | up to 25% above or below, in 5% steps | 2026 | Code art. 164(1)-(2) |
| Contracting entity, dependency over 80% | 10% of services bought in the year | 2026 | Code art. 167, 168(7)(a) |
| Contracting entity, dependency over 50% up to 80% | 7% | 2026 | Code art. 140(1), 168(7)(b) |
| Contracting entity: worker's yearly service income at least | 6 x IAS = EUR 3,222.78 | 2026 | Code art. 140(2) |
| Employees, general regime | 34.75%: employer 23.75%, employee 11% | 2026 | Code art. 53 |
| MOE with management or administration duties (gerência, administração) | 34.75%: entity 23.75%, member 11% | 2026 | Code art. 69(2) |
| Other MOE | 29.6%: entity 20.3%, member 9.3% | 2026 | Code art. 69(1) |
| MOE base | pay actually received, minimum 1 x IAS (EUR 537.13) unless covered elsewhere at IAS or more | 2026 | Code art. 66 |
| Special rate: employers without profit motive | 33.3%: employer 22.3%, employee 11% | 2026 | Code art. 112 |
| Special rate: workers with disability | 22.9%: employer 11.9%, employee 11% | 2026 | Code art. 109(1) |
| Special rate: professional sportspeople | 33.3%: employer 22.3%, employee 11% | 2026 | Code art. 79(1) |
| Special rate: domestic workers | 28.3% (18.9% + 9.4%) without unemployment cover; 33.3% (22.3% + 11%) with it | 2026 | Code art. 121 |
| Late-payment interest | 7.221% a year, charged per calendar month or part | 2026 | Code art. 211-212; IGCP Aviso 18/2026/2: https://diariodarepublica.pt/dr/detalhe/aviso/18-2026-993315668 |

## The taxable base

**Self-employed, quarterly regime.** Each quarter the worker declares gross service income and gross sales of goods for the previous three months (art. 151-A). Segurança Social computes relevant income: 70% of services plus 20% of goods (art. 162(1)). Hotel, restaurant and drinks services declared as such for tax use the 20% factor (art. 162(2)). Mixed activity applies each factor to its own income.

Monthly base = relevant income / 3. It applies to the declaration month and the next two (art. 163(1)). The April declaration (January to March income) sets the base for April, May and June.

Then, in this order:

1. If the worker is in the employment exemption and the monthly average is at or above 4 x IAS, the base is the excess over EUR 2,148.52 (art. 163(4)). The ISS Guia Prático says a resulting contribution below EUR 5 is ignored.
2. The worker may move the base up or down by up to 25% in 5% steps when declaring (art. 164(1)-(2)). The option does not apply to the excess base of a worker with employment (art. 163(4)).
3. The base is capped at EUR 6,445.56 (art. 163(5)).
4. Contribution = base x 21.4% (25.2% for an ENI or EIRL holder). If there is no income, or the result is under EUR 20, the contribution is EUR 20 (art. 163(2)).

**Income left out.** Unless the worker chooses to include them, relevant income excludes investment grants and subsidies, capital gains, and income from intellectual or industrial property. Income from small renewable power production and from rent or local lodging in a house or flat never counts (art. 162(4) and the ISS Guia Prático).

**Organised accounts.** Relevant income is the prior-year taxable profit declared on Anexo SS of the IRS Modelo 3 (art. 162(3)). The monthly base is 1/12 of it, at least 1.5 x IAS (EUR 805.70). Segurança Social sets it in October for the next calendar year (art. 163(3)). These workers file no quarterly declaration. After the October notice they may ask to move to the quarterly regime, from January (art. 164(3)); the ISS Guia Prático gives 1 to 30 November as the window.

**Spouses and partners** of a self-employed worker pay on 70% of that worker's relevant income, adjustable from 20% lower up to the full amount, with the same EUR 20 minimum and 12 x IAS ceiling (art. 166, ISS Guia Prático).

**Annual review.** In January the worker confirms or corrects the previous year's declared income (art. 151-A(5)). Segurança Social also reviews the year against AT data and notifies the worker of any difference (art. 164-A(1)). A difference over EUR 20 is charged in January of the following year (ISS Guia Prático), and contributions paid as a result of the review count as paid late (art. 164-A(2)). For 2025 income the ISS Guia Prático gives 20 February 2026 as the date for any extra payment; after that, interest runs. Overpayments are credited to future contributions, or refunded on form RC 3041.

**Employees and MOE.** The base is pay as defined in Code art. 44 to 48. Which items are in or out, and the monthly payroll figures, are in `portugal-payroll`. MOE pay is subject at the MOE rates above, with the 1 x IAS minimum base (art. 66).

**Contracting entities.** The base is the total value of services the worker supplied to the entity in the calendar year (art. 167). Dependency is the entity's share of the worker's total activity value for the year (art. 140).

**Effect on IRS.** In the IRS simplified regime, for income taxed at the 0.75 and 0.35 coefficients, compulsory contributions linked to the activity are deducted, up to the net income, only for the part above 10% of the gross income (CIRS art. 31(2)). In the 15% expenses test, the part not deducted that way counts where it is higher than the specific deduction (CIRS art. 31(13)(a)). The method is in `pt-income-tax`.

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Self-employed quarterly declaration | Last day of January, April, July and October, for the previous three months' income | Code art. 151-A(3) |
| Correction of a quarterly declaration | Within 15 days after the deadline (ISS Guia Prático). A late declaration can be filed online until the last day of the month before the next declaration month | ISS Guia Prático |
| Annual confirmation of last year's income | January | Code art. 151-A(5) |
| Self-employed monthly payment | Between the 10th and the 20th of the month after the month it relates to | Code art. 155(2) |
| Contracting-entity contribution | By the 20th of the month after Segurança Social issues the payment notice; it relates to the previous calendar year | Code art. 155(3) |
| Employer: confirm the monthly pay declaration (new model) | By the 20th of the following month; silence counts as acceptance of the figures the system computed | Code art. 40(7)-(8), as amended by DL 127/2025 |
| Employer: pay employee and employer contributions | Between the 1st and the 25th of the following month | Code art. 43, as amended by DL 127/2025, in force 1 January 2026 |
| Move of all employers to the new reporting model | During 2026 by request; compulsory from 1 January 2027 | DL 127/2025, art. 5 |

The quarterly declaration is filed on Segurança Social Direta. Workers exempt under art. 157(1)(a) to (c) and workers on organised accounts do not file it. A worker who stops or suspends activity files the declaration in the next window (art. 151-A(4)).

Payment is by Multibanco reference, homebanking or direct debit set up on Segurança Social Direta (ISS Guia Prático).

To receive benefits, the worker's contributions must be paid up to the end of the third month before the month of the event that gives rise to the benefit (ISS Guia Prático).

## Penalties and interest

**Fines** (Code art. 233). Light offence (leve): EUR 50 to 250 for negligence, EUR 100 to 500 if intentional. Serious (grave): EUR 300 to 1,200, or EUR 600 to 2,400. Very serious (muito grave): EUR 1,250 to 6,250, or EUR 2,500 to 12,500. Limits rise by 50% for a company with fewer than 50 workers, and by 100% for one with 50 or more (art. 233(4)).

**Which class applies:**

- Self-employed or contracting entity paying late: light if paid within 30 days after the deadline, serious otherwise (art. 155(4)).
- Self-employed failing to file the quarterly declaration: light (art. 151-A(8)).
- Employer not declaring a worker's pay: very serious (art. 40(10)). Not confirming or correcting by the 20th, where the error changes what the worker is owed: light if put right within 60 days, serious otherwise (art. 40(11)).

**Interest.** Late contributions carry interest for each calendar month or part of a month (art. 211). The rate is the one for debts to the State (art. 212): 7.221% for 2026 (IGCP Aviso 18/2026/2).

**Benefits.** Unpaid contributions suspend benefits until the debt is settled (ISS Guia Prático).

## Cross-border points

- A self-employed worker who goes to work abroad for a set period may keep Portuguese cover. The limit is one year, extendable by one more year on request, unless an international agreement says otherwise (Code art. 138). While the income is not declared in Portugal, the last base stays in force (ISS Guia Prático).
- A self-employed person working temporarily in Portugal who already has compulsory cover elsewhere for invalidity, old age and death is outside the regime once excluded on form RV 1025 (ISS Guia Prático).
- A foreign invalidity or old-age pension gives the same exemption as a Portuguese one (art. 157(1)(b)).
- Which state's legislation applies to people working in more than one EU state, and A1 certificates, are in `pt-cross-border`. This skill does not set those rules.

## Worked examples

### Example 1: freelance designer, services only, first quarter 2026

Rita has been self-employed since 2022. She has no other job. From January to March 2026 she invoiced EUR 9,000 of design services. She files the declaration in April and does not use the 25% option.

1. Relevant income: 9,000 x 70% = EUR 6,300.
2. Monthly base: 6,300 / 3 = EUR 2,100. This is under the EUR 6,445.56 ceiling.
3. Monthly contribution: 2,100 x 21.4% = EUR 449.40 for April, May and June. She pays each between the 10th and the 20th of May, June and July.
4. For the quarter: 449.40 x 3 = EUR 1,348.20.

Over 2026 Rita invoices EUR 36,000, all to one Lisbon company. The company received 100% of her activity, which is over 80%, and her service income is over 6 x IAS. So the company owes 10% of EUR 36,000 = EUR 3,600 as a contracting entity. It pays this in 2027, by the 20th of the month after Segurança Social's notice. This is the company's own cost, not deducted from Rita.

```oa-check
name: PT self-employed services EUR 9,000 in Q1 2026, plus contracting entity
inputs:
  services: 9000
  goods: 0
  ias: 537.13
  rate: 0.214
  annual_services_to_client: 36000
  entity_rate: 0.10
steps:
  - relevant: services * 0.70 + goods * 0.20
  - base: min(relevant / 3, 12 * ias)
  - monthly: max(20, round(base * rate, 2))
  - quarter: monthly * 3
  - entity_contribution: annual_services_to_client * entity_rate
expected:
  relevant: 6300
  base: 2100
  monthly: 449.40
  quarter: 1348.20
  entity_contribution: 3600
```

### Example 2: employee with a side business above 4 x IAS

João is employed full-time by an unrelated company at EUR 1,400 a month, which is above 1 x IAS. He also has recibos verdes activity and sells goods online. From April to June 2026 he invoiced EUR 15,000 of services and sold EUR 6,000 of goods. He files the declaration in July.

1. Relevant income: 15,000 x 70% + 6,000 x 20% = 10,500 + 1,200 = EUR 11,700.
2. Monthly average: 11,700 / 3 = EUR 3,900. This is at least 4 x IAS (EUR 2,148.52), so the employment exemption does not cover all of it.
3. Base: 3,900 - 2,148.52 = EUR 1,751.48 (art. 163(4)). This is under the ceiling. The 25% option does not apply to this base (art. 163(4)).
4. Monthly contribution: 1,751.48 x 21.4% = EUR 374.82 for July, August and September. He pays each between the 10th and the 20th of the following month.

If his next quarter's monthly average falls below EUR 2,148.52, he owes nothing as self-employed for those three months.

```oa-check
name: PT employee with side activity, Q2 2026 services 15,000 and goods 6,000
inputs:
  services: 15000
  goods: 6000
  ias: 537.13
  rate: 0.214
steps:
  - relevant: services * 0.70 + goods * 0.20
  - monthly_avg: relevant / 3
  - threshold: 4 * ias
  - base: min(max(0, monthly_avg - threshold), 12 * ias)
  - monthly: round(base * rate, 2)
  - quarter: monthly * 3
expected:
  relevant: 11700
  monthly_avg: 3900
  threshold: 2148.52
  base: 1751.48
  monthly: 374.82
  quarter: 1124.46
```

## Ask the client first

1. When did the activity first start, and has it stopped and restarted? This decides whether contributions are due yet (art. 145).
2. Is the client employed elsewhere, by whom, and at what monthly pay? Or do they receive an invalidity, old-age or occupational-risk pension? These decide the exemptions (art. 157).
3. How much of last quarter's income was services, and how much was goods or hotel and restaurant services? Is the client on organised accounts?
4. Is the client an empresário em nome individual or EIRL holder (25.2%), and is a spouse working in the business?
5. Who are the clients, and did any one of them (or one group) take more than 50% or more than 80% of the year's work? This sets the contracting-entity charge.
6. Is the client also a gerente or director of a company, and is that role paid? This brings in the MOE rules.

## Sources

| Source | URL | Read on |
|---|---|---|
| Código dos Regimes Contributivos (Lei 110/2009, consolidated), art. 40, 43, 53, 64, 66, 69, 79, 109, 112, 121, 138, 139, 140, 145, 151-A, 155, 157, 162, 163, 164, 167, 168, 211, 212, 233 | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575 | 2026-10-24 |
| Decreto-Lei 127/2025 (new reporting model, art. 40 and 43, transition art. 5, in force 1 January 2026) | https://diariodarepublica.pt/dr/detalhe/decreto-lei/127-2025-967317021 | 2026-10-24 |
| Portaria 480-A/2025/1, art. 2 (IAS 2026 EUR 537.13; AT's copy of the Diário da República text) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_480_A_2025_1.pdf | 2026-10-24 |
| IGCP Aviso 18/2026/2 (late interest 7.221% from 1 January 2026) | https://diariodarepublica.pt/dr/detalhe/aviso/18-2026-993315668 | 2026-10-24 |
| ISS, Guia Prático, Novo Regime dos Trabalhadores Independentes (v1.09, 2026 figures) | https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw | 2026-10-24 |
| ISS, Guia Prático, Pagamento de Contribuições à Segurança Social | https://www.seg-social.pt/ptss/pssd/documento/cmc1y95ap00dkkl2yk3g4tdla | 2026-10-24 |
| ISS, Guia Prático, Inscrição, Vinculação e Cessação de Atividade de Trabalhador por Conta de Outrem (rate tables) | https://www.seg-social.pt/ptss/pssd/documento/cmc1xlxpq00d9kl2y0p3inyft | 2026-10-24 |
| CIRS art. 31(2) and 31(13)(a) (contributions in the simplified regime) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx | 2026-10-24 |

Not yet confirmed: Code art. 163(8) says the EUR 20 minimum is updated in line with the IAS, but no updated figure was found and the 2026 ISS Guia Prático still gives EUR 20.00, which this skill uses; the employer deadlines that apply during 2026 to employers not yet moved to the new reporting model under DL 127/2025 art. 5 (the old model's declaration date was not read); the regulation (Decreto Regulamentar 1-A/2011) that lists income left out of relevant income, which was read only through the ISS Guia Prático; the EUR 5 de minimis for the excess base, from the ISS Guia Prático only; the EUR 20 threshold for the annual review is in the ISS Guia Prático, not in art. 164-A; other special rates (for example very short contracts, pensioners in work, rural workers) and the contribution reductions for first jobs and long-term unemployed were not read and are left to `portugal-payroll`; EU coordination under Regulation 883/2004 (EUR-Lex did not load) is left to `pt-cross-border`.

> Contributed by Ryan Duguid.

> Contributed by Michael Cutajar.

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
