---
name: portugal-payroll
description: "Portuguese payroll for employees, tax year 2026: monthly IRS withholding under CIRS arts. 98 to 101 and the 2026 tables for the mainland (Despacho 233-A/2026), the Azores (Despacho 1179/2026) and Madeira (Despacho 19/2026), including the 50% cut for November 2026 pay; holiday and Christmas subsidies and twelfths; employee 11% and employer 23.75% Social Security; the 2026 meal allowance limits (EUR 6.15 cash, 70% more on a card); IRS Jovem in withholding; the DMR by the 10th, IRS paid by the 20th, Social Security from the 1st to the 25th; minimum wage; overtime; fines and interest. Trigger on: Portugal payroll, processamento de salários, retenção na fonte, tabelas de retenção 2026, TSU, subsídio de férias, subsídio de Natal, duodécimos, subsídio de refeição, DMR, salário líquido. Out of scope: the self-employed and contributions in depth (pt-social-contributions), the annual IRS return (pt-irs-employees-investment), non-residents (pt-cross-border), NHR and IFICI (pt-nhr-ifici)."
version: 1.1
jurisdiction: PT
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Portugal payroll (tax year 2026) v1.1

> **Source-cited draft.** No accountant has reviewed this skill yet. Figures come from the Código do IRS (CIRS) on the Portal das Finanças, the 2026 withholding despachos, the Código dos Regimes Contributivos and the Código do Trabalho in the Diário da República, read on 24 October 2026. It prepares working papers; it is not authority to file or pay.

> Contributed by Ryan Duguid.

Related skills:
- `pt-social-contributions`: Social Security in depth, the self-employed, members of corporate bodies (MOE), contribution fines and interest.
- `pt-irs-employees-investment`: the annual IRS return (Modelo 3), the annual bands, the specific deduction, deductions from tax and IRS Jovem on assessment.
- `pt-cross-border`: residence, non-residents and treaties.
- `pt-nhr-ifici`: the old non-habitual resident regime and IFICI.

## Who this applies to

Any employer (entidade devedora) that pays employment income (Category A) to an employee. The employer must withhold IRS when it pays or makes pay available (CIRS art. 99(1)(a)), report the pay monthly to the tax authority (art. 119(1)(c)) and declare and pay Social Security for each worker (Código dos Regimes Contributivos, the "Contributions Code", arts. 40 and 43).

**Which withholding table.** The tables depend on where the employee lives:
- Residents of the mainland: Despacho 233-A/2026 (point 2 of the despacho).
- Residents of the Azores: Despacho 1179/2026.
- Residents of Madeira: Despacho 19/2026 of the Regional Secretary of Finance (JORAM II série n.º 13, 20 January 2026, corrected by Declaração de Retificação 10/2026).

Inside each set, the table depends on the employee's situation: Table I (single without dependants, or married with two earners), Table II (single with one or more dependants), Table III (married, one earner), Tables IV to VII (employees with a disability) and Tables VIII to XI (pensions) (Despacho 233-A/2026, point 1). "Married, one earner" applies only when the spouse has no income that is aggregated, or one spouse earns 95% or more of the couple's aggregated income (CIRS art. 99-B(4); despacho point 9). Unmarried partners (união de facto) under CIRS art. 14 use the married tables (despacho point 8). If the employee gives no family details, the employer withholds as if there are no dependants (art. 99-B(3)).

**Special cases.**
- IFICI holders (EBF art. 58-A): 20% flat withholding on monthly Category A pay (CIRS art. 99(8)). See `pt-nhr-ifici`.
- Residents paid for work done abroad: no Portuguese withholding when that pay is effectively taxed in the source country by a tax similar to IRS (art. 99(5)).
- Non-residents: 25% final withholding (art. 71(4)(a)). See Cross-border points.
- Pay made only of variable amounts: the separate rate table of art. 100 applies, not the monthly tables.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Withholding formula, no dependants | Monthly pay x marginal rate - amount to deduct (parcela a abater); never below zero | 2026 | Despacho 233-A/2026, point 3(b): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Despacho-233-A-2026.pdf |
| Withholding formula, with dependants | Monthly pay x marginal rate - amount to deduct - (extra amount per dependant x number of dependants) | 2026 | Despacho 233-A/2026, point 3(a) |
| Mainland Table I: no withholding | Monthly pay up to EUR 920.00 | 2026 | Despacho 233-A/2026, Table I |
| Mainland Table I: pay up to EUR 1,819 | 24.10%, less EUR 193.33 | 2026 | Despacho 233-A/2026, Table I |
| Mainland Table I: pay up to EUR 2,499 | 34.90%, less EUR 401.19 | 2026 | Despacho 233-A/2026, Table I |
| Mainland Table I: top row | Over EUR 20,221: 47.17%, less EUR 1,272.31 | 2026 | Despacho 233-A/2026, Table I |
| Mainland Table III (married, one earner): no withholding | Monthly pay up to EUR 991.00 | 2026 | Despacho 233-A/2026, Table III |
| Extra deduction per dependant, employment | EUR 21.43 (Table I, married two earners), EUR 34.29 (Table II), EUR 42.86 (Table III) | 2026 | Despacho 233-A/2026, Tables I to III |
| Dependant with 60% or more disability | Add EUR 84.82 per dependant (single or married one earner), EUR 42.41 (married two earners) | 2026 | Despacho 233-A/2026, point 5(a) |
| Three or more dependants | Marginal rate cut by 1 percentage point (Tables I to VII) | 2026 | Despacho 233-A/2026, point 5(h) |
| Azores Table I: no withholding | Monthly pay up to EUR 966.00; first band 8.75% | 2026 | Despacho 1179/2026, as published in AT Circular 3/2026: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Circular-3-2026.pdf |
| Madeira Table I: no withholding | Monthly pay up to EUR 980.00; first band 8.72%; top row over EUR 21,411: 32.78%, less EUR 1,275.30 | 2026 | Despacho 19/2026 (JORAM), republished by Declaração de Retificação 10/2026: https://at.madeira.gov.pt/ficheiros/IISerie-016-2026-01-23Supl3.pdf |
| November 2026 pay (mainland and Azores) | Only 50% of the table amount is withheld, except where monthly pay exceeds the upper limit of the second-to-last row | Paid 1 to 30 Nov 2026 | Despacho 12523-A/2026, points 2 and 3: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/despacho-12523-a-2026.pdf ; Azores: Despacho 12610-A/2026: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/despacho-12610-a-2026.pdf |
| Overtime pay | Withheld at 50% of the effective rate on that month's regular pay | 2026 | CIRS art. 99-C(8); Despacho 233-A/2026, point 5(f) |
| Rounding | Amount withheld rounded down to the whole euro | 2026 | CIRS art. 99-E(1): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs99e.aspx |
| Variable-only pay | 0% up to EUR 5,269 a year, rising to 40% over EUR 506,343 | 2026 | CIRS art. 100(1): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs100.aspx |
| IFICI employees | 20% | 2026 | CIRS art. 99(8): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs99.aspx |
| Social Security, general regime | 34.75%: employer 23.75%, employee 11% | 2026 | Contributions Code art. 53: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575 |
| Members of corporate bodies (MOE) with management duties | 34.75%: entity 23.75%, member 11% | 2026 | Contributions Code art. 69(2) |
| Other MOE | 29.6%: entity 20.3%, member 9.3% | 2026 | Contributions Code art. 69(1) |
| Domestic workers | 28.3% (employer 18.9%, worker 9.4%) without unemployment cover; 33.3% (22.3% and 11%) with it | 2026 | Contributions Code art. 121(1) and (2) |
| Meal allowance exempt from IRS and Social Security, cash | Up to EUR 6.15 a day (the public-sector allowance) | From 1 Jan 2026 | CIRS art. 2(3)(b)(2): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs2.aspx ; Portaria 51-B/2026/1, art. 1 and 3: https://files.diariodarepublica.pt/1s/2026/01/02103/0001100011.pdf ; Contributions Code art. 46(2)(l) and (3) |
| Meal allowance exempt, meal card or vouchers | Up to 70% more than the cash limit: EUR 6.15 x 1.7 = EUR 10.455 a day | From 1 Jan 2026 | CIRS art. 2(3)(b)(2), wording of Lei 45-A/2024 |
| IRS Jovem exemption | 100% (year 1), 75% (years 2 to 4), 50% (years 5 to 7), 25% (years 8 to 10), capped at 55 x IAS = EUR 29,542.15 a year | 2026 | CIRS art. 12-B(1) and (5): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs12b.aspx |
| IRS Jovem cap in withholding | 55 x IAS / 14 = EUR 2,110.15 | 2026 | Despacho 233-A/2026, point 5(g) |
| IAS | EUR 537.13 | 2026 | Portaria 480-A/2025/1, art. 2: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_480_A_2025_1.pdf |
| Minimum wage, mainland | EUR 920 a month | From 1 Jan 2026 | Decreto-Lei 139/2025, as reported by DGERT: https://www.dgert.gov.pt/retribuicao-minima-mensal-garantida-para-2026 |
| Minimum wage, Madeira | EUR 980 a month | From 1 Jan 2026 | Decreto Legislativo Regional 1/2026/M, art. 2 and 4: https://www.madeira.gov.pt//Portals/25/Documentos/Legislacao/DLR_1_2026_M.pdf |
| Overtime premium, first 100 hours a year | Working day: 25% first hour, 37.5% after; rest day or holiday: 50% | 2026 | Código do Trabalho art. 268(1): https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34546475 |
| Overtime premium, over 100 hours a year | Working day: 50% first hour, 75% after; rest day or holiday: 100% | 2026 | Código do Trabalho art. 268(2) |
| Overtime limit | 175 hours a year (micro and small firms); 150 hours (medium and large) | 2026 | Código do Trabalho art. 228(1) |
| Night work premium | 25% | 2026 | Código do Trabalho art. 266(1) |
| Late-payment interest (tax and Social Security debts) | 7.221% a year | From 1 Jan 2026 | IGCP Aviso 18/2026/2: https://diariodarepublica.pt/dr/detalhe/aviso/18-2026-993315668 ; LGT art. 44(3); Contributions Code arts. 211 and 212 |

Each region has 11 tables. Use the despacho for the region where the employee lives; the rows above are the zero-withholding limits and the rows the examples use.

## The taxable base

**What counts as monthly pay for withholding.** Fixed pay plus any other employment income as defined in CIRS art. 2 paid in the month (art. 99-C(2)). Benefits in kind are not withheld on, unless the employee asks (art. 99(1)(a) and 99-C(3)). Pay for periods shorter than a month is added up for the month (art. 99-C(4)).

**Paid separately (autonomous withholding).** The holiday subsidy, the Christmas subsidy, overtime pay and pay for earlier years are always withheld on their own. They are never added to the month's pay to pick the table row (art. 99-C(5)). Apply the table to the subsidy as if it were a month's pay. Overtime gets 50% of the month's effective rate (art. 99-C(8)). Pay for earlier years is divided by the number of months it covers to find the rate, which then applies to the whole amount (art. 99-C(9)). When an employer pays several items in one month, the payslip shows the effective rate for each one separately (Despacho 233-A/2026, point 10; CIRS art. 99(9)).

**The 14 payments.** The Código do Trabalho gives a Christmas subsidy equal to one month's pay, paid by 15 December (art. 263(1)), and a holiday subsidy of base pay plus pay linked to how the work is done, for the minimum holiday (art. 264(2)), paid before the holiday starts unless agreed otherwise in writing (art. 264(3)). The Christmas subsidy is pro rata in the year of hiring, the year of leaving and when the contract is suspended for a reason on the worker's side (art. 263(2)). The minimum holiday is 22 working days (art. 238(1)).

**Twelfths (duodécimos).** Where the subsidies are paid in instalments, withhold in each payment the matching share of the tax worked out on the whole subsidy (CIRS art. 99-C(6)). The Labour Code sets the latest dates; paying the holiday subsidy in another way needs a written agreement (art. 264(3)).

**Meal allowance.** Taxed for IRS only on the part above EUR 6.15 a day in cash, or above EUR 10.455 a day on a meal card or vouchers (CIRS art. 2(3)(b)(2) with Portaria 51-B/2026/1). Social Security follows the same IRS limits (Contributions Code art. 46(2)(l) and (3)). Meals in the employer's canteen are outside the Social Security base (art. 48(f)).

**Social Security base.** Pay as defined in Contributions Code arts. 44 to 48. It includes base pay, holiday pay, and the Christmas and holiday subsidies (art. 46(2)(a), (g), (h)). There is no ceiling for employees under art. 53. The details of what is in and out, and MOE bases, are in `pt-social-contributions`.

**IRS Jovem in withholding.** An employee aged up to 35 who is not a dependant tells the employer the year of earning income they are in (CIRS art. 99-F(5)). The employer works out the withholding rate on all pay, exempt part included, and applies that rate only to the part that is not exempt (art. 99-F(4)). The exempt part taken through withholding is capped at 55 x IAS / 14 (Despacho 233-A/2026, point 5(g)). Former NHR or IFICI beneficiaries, people under the art. 12-A returnee regime and people with unpaid tax cannot use it (art. 12-B(9)). The final exemption is claimed on the annual return.

**Higher rate by choice.** An employee may ask in writing for a higher whole-number rate (CIRS art. 98(6)). Only the marginal rate changes; the deductions stay (Despacho 233-A/2026, point 5(e)).

**Corrections.** Errors by the employer can be corrected in the next withholdings, within the same year (CIRS art. 98(4)). For November 2026, an employer that did not apply the 50% cut may correct it by the end of December 2026 (Despacho 12523-A/2026, point 8).

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Ask the employee for family details | At the start of work, before the first payment | CIRS art. 99(2)(a) |
| Monthly pay declaration to AT (Declaração Mensal de Remunerações, DMR): pay, withholdings, compulsory contributions and union dues | By the 10th of the month after payment, including exempt or non-taxable employment income | CIRS art. 119(1)(c)(i): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs119.aspx |
| Corrected DMR | Within 30 days of the fact that changes the amounts | CIRS art. 119(1)(d) |
| Pay over IRS withheld | By the 20th of the month after it was withheld | CIRS art. 98(3): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs98.aspx |
| Annual statement to each employee (pay, tax withheld, deductions) | By 20 January of the next year | CIRS art. 119(1)(b) |
| Social Security pay declaration (new model): confirm or correct the figures the system computed | By the 20th of the following month; silence means acceptance | Contributions Code art. 40(7) and (8), wording of Decreto-Lei 127/2025 |
| Pay employee and employer Social Security | Between the 1st and the 25th of the following month | Contributions Code art. 43, wording of Decreto-Lei 127/2025, in force 1 January 2026 |
| Move to the new Social Security reporting model | Any time in 2026 on request; compulsory from 1 January 2027 | Decreto-Lei 127/2025, art. 5: https://diariodarepublica.pt/dr/detalhe/decreto-lei/127-2025-967317021 |
| Payslip | Before or at payment: employer, employee's name, Social Security number, category, base pay and other items, period, deductions, net pay | Código do Trabalho art. 276(3) |
| Christmas subsidy | By 15 December | Código do Trabalho art. 263(1) |
| Holiday subsidy | Before the holiday starts, unless agreed otherwise in writing | Código do Trabalho art. 264(3) |

The ISS practical guide on paying contributions gives the same 1st to 25th window for employers; the 10th to 20th window now applies to the self-employed (ISS, Guia Prático, Pagamento de Contribuições, F2.1 and F2.3).

## Penalties and interest

**Tax (IRS withheld).**
- Withheld tax not paid over: fine of one to two times the tax (RGIT art. 114(1)). If by negligence: 15% to half of the tax (art. 114(2)). The same fines apply to tax that should have been withheld but was not (art. 114(4)).
- Late or missing DMR: fine of EUR 150 to EUR 3,750 (RGIT art. 117(1)).
- Withheld tax over EUR 7,500 not paid more than 90 days after the deadline, and not paid within 30 days of notice: crime of breach of trust, up to three years in prison or a fine of up to 360 days (RGIT art. 105(1) and (4)); over EUR 50,000, one to five years (art. 105(5)).
- Compensatory interest runs day by day from the payment deadline for tax withheld or that should have been withheld (LGT art. 35(1) and (3)), at the legal interest rate (art. 35(10)). The employer owes it on late payment (Despacho 233-A/2026, point 13). An employee who wrongly used the "married, one earner" table owes compensatory interest on the shortfall (CIRS art. 99-F(3)).
- Late-payment interest: 7.221% a year for 2026 (LGT art. 44(1) and (3); IGCP Aviso 18/2026/2).

**Social Security.** The fine bands (light, serious, very serious, raised by 50% or 100% for companies) are set out in `pt-social-contributions` (Contributions Code art. 233). Not declaring a worker's pay is very serious (art. 40(10)). Not confirming or correcting by the 20th, where the error changes what the worker is owed, is light if put right within 60 days and serious otherwise (art. 40(11)). Late contributions carry interest for each calendar month or part (art. 211), 7.221% for 2026.

**Labour Code.** Not paying the Christmas or holiday subsidy as required is a very serious offence (arts. 263(3) and 264(4)). Not paying the overtime premiums is serious (art. 268(5)). A payslip missing the required details is light (art. 276(4)).

## Cross-border points

- **Non-resident employees** with Portuguese-source pay: 25% final withholding on gross (CIRS art. 71(4)(a)). Monthly pay from a single payer is free of withholding up to the minimum wage, with 25% on the excess, if the employee declares in writing that they have no similar income from other Portuguese payers (art. 71(5) and (6)). See `pt-cross-border`.
- **Residents working abroad**: no withholding where the pay is effectively taxed abroad (art. 99(5)).
- **Which region's table**: the employee's residence in the mainland, the Azores or Madeira decides the table (Despacho 233-A/2026, point 2; Despacho 1179/2026, point 2).
- **Social Security for posted or cross-border workers** (EU Regulation 883/2004, A1 certificates) is not covered here. See `pt-cross-border` and `pt-social-contributions`.
- **IFICI** newcomers: 20% withholding (art. 99(8)); see `pt-nhr-ifici`.

## Worked examples

### Example 1: mainland employee, single, no dependants, EUR 1,800 a month

An employee lives in Lisbon, is single with no dependants, and earns EUR 1,800 a month in October 2026. She also gets a meal card of EUR 9.00 for 22 working days (EUR 198), inside the EUR 10.455 limit, so it is exempt from IRS and Social Security. Table I, row "up to EUR 1,819": 24.10% less EUR 193.33. Tax is 1,800 x 24.10% = 433.80, less 193.33 = 240.47, rounded down to EUR 240. Social Security: employee 11% = EUR 198; employer 23.75% = EUR 427.50. Net salary is EUR 1,362, plus the EUR 198 meal card. The employer's cost is EUR 2,425.50. In June, her EUR 1,800 holiday subsidy is withheld on its own at the same row, another EUR 240, and is not added to June's pay.

```oa-check
name: Portugal 2026, mainland Table I, EUR 1,800 a month, single, no dependants
inputs:
  pay: 1800
  meal_days: 22
  meal_card_daily: 9
steps:
  - tax_raw: pay * 0.2410 - 193.33
  - withholding: floor(tax_raw)
  - ss_employee: pay * 0.11
  - ss_employer: pay * 0.2375
  - meal: meal_days * meal_card_daily
  - net_salary: pay - ss_employee - withholding
  - employer_cost: pay + ss_employer + meal
expected:
  tax_raw: 240.47
  withholding: 240
  ss_employee: 198
  ss_employer: 427.50
  meal: 198
  net_salary: 1362
  employer_cost: 2425.50
```

### Example 2: mainland employee in IRS Jovem year 3, EUR 2,400 a month

An employee aged 26, single with no dependants, never under NHR or IFICI, tells his employer he is in his third year of earning income. IRS Jovem exempts 75% in years 2 to 4. He earns EUR 2,400 in October 2026. First the rate on all pay: Table I, row "up to EUR 2,499", 34.90% less EUR 401.19, so 2,400 x 34.90% = 837.60, less 401.19 = 436.41, an effective rate of 18.18375%. The exempt part is 75% of 2,400 = EUR 1,800, under the EUR 2,110.15 monthly cap. Withholding is 18.18375% on the EUR 600 that is not exempt: 109.10, rounded down to EUR 109. IRS Jovem does not change Social Security: employee EUR 264, employer EUR 570. Net pay is EUR 2,027. Had this been paid in November 2026, only 50% of the withholding would apply, because EUR 2,400 is below the second-to-last row limit (Despacho 12523-A/2026); that step is left out of the check.

```oa-check
name: Portugal 2026, mainland Table I, IRS Jovem year 3, EUR 2,400 a month
inputs:
  pay: 2400
  exempt_share: 0.75
  ias: 537.13
steps:
  - tax_on_all: pay * 0.3490 - 401.19
  - effective_rate: tax_on_all / pay
  - monthly_cap: 55 * ias / 14
  - exempt: min(pay * exempt_share, monthly_cap)
  - taxable_part: pay - exempt
  - withholding: floor(taxable_part * effective_rate)
  - ss_employee: pay * 0.11
  - ss_employer: pay * 0.2375
  - net_pay: pay - ss_employee - withholding
expected:
  tax_on_all: 436.41
  effective_rate: 0.18183750
  monthly_cap: 2110.15
  exempt: 1800
  taxable_part: 600
  withholding: 109
  ss_employee: 264
  ss_employer: 570
  net_pay: 2027
```

## Ask the client first

1. Where does each employee live: mainland, Azores or Madeira? (Picks the table set and the November rule.)
2. Marital status, whether the spouse has income, number of dependants and any disability of 60% or more. (Picks Table I, II or III and the deductions.)
3. Is any employee aged 35 or under and claiming IRS Jovem, and which year of earning income are they in? Any NHR or IFICI status? (Changes the withholding base and rate.)
4. Are the holiday and Christmas subsidies paid in full or in twelfths, and is there a written agreement? (Changes timing and the per-payment withholding.)
5. How is the meal allowance paid (cash or card) and how much a day? (Decides the exempt part.)
6. Is the employer on the new Social Security reporting model yet, and are any workers MOE, domestic workers or non-residents? (Changes deadlines and rates.)

## Sources

| Source | URL | Read on |
|---|---|---|
| CIRS art. 2 (meal allowance limit, wording of Lei 45-A/2024) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs2.aspx | 2026-10-24 |
| CIRS art. 12-B (IRS Jovem) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs12b.aspx | 2026-10-24 |
| CIRS art. 71 (non-residents, 25%) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs71.aspx | 2026-10-24 |
| CIRS art. 98 (withholding, payment by the 20th) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs98.aspx | 2026-10-24 |
| CIRS art. 99 (Categories A and H) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs99.aspx | 2026-10-24 |
| CIRS art. 99-B (family situation) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs99b.aspx | 2026-10-24 |
| CIRS art. 99-C (Category A, subsidies, overtime) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs99c.aspx | 2026-10-24 |
| CIRS art. 99-E (rounding) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs99e.aspx | 2026-10-24 |
| CIRS art. 99-F (tables, IRS Jovem in withholding) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs99f.aspx | 2026-10-24 |
| CIRS art. 100 (variable-only pay) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs100.aspx | 2026-10-24 |
| CIRS art. 101 (other categories) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs101.aspx | 2026-10-24 |
| CIRS art. 119 (DMR, annual statement) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs119.aspx | 2026-10-24 |
| Despacho 233-A/2026 (mainland tables 2026), AT copy of the Diário da República text | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Despacho-233-A-2026.pdf | 2026-10-24 |
| Despacho 1179/2026 (Azores tables 2026), AT copy | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Despacho-1179-2026.pdf | 2026-10-24 |
| AT Circular 3/2026 (Azores tables in text form) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Circular-3-2026.pdf | 2026-10-24 |
| AT Circular 2/2026 (Madeira tables, Despacho 19/2026) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Circular_2_2026.pdf | 2026-10-24 |
| JORAM II série n.º 16, 3.º supl., 23 Jan 2026 (Declaração de Retificação 10/2026, Madeira tables) | https://at.madeira.gov.pt/ficheiros/IISerie-016-2026-01-23Supl3.pdf | 2026-10-24 |
| Despacho 12523-A/2026 (November 2026, mainland) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/despacho-12523-a-2026.pdf | 2026-10-24 |
| Despacho 12610-A/2026 (November 2026, Azores) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/despacho-12610-a-2026.pdf | 2026-10-24 |
| Portaria 51-B/2026/1 (meal allowance EUR 6.15 from 1 Jan 2026) | https://files.diariodarepublica.pt/1s/2026/01/02103/0001100011.pdf | 2026-10-24 |
| Portaria 480-A/2025/1 (IAS 2026), AT copy | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_480_A_2025_1.pdf | 2026-10-24 |
| Código dos Regimes Contributivos (Lei 110/2009, consolidated), arts. 40, 43, 46, 48, 53, 69, 121, 211, 233 | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575 | 2026-10-24 |
| Decreto-Lei 127/2025 (arts. 40 and 43, transition art. 5, in force 1 Jan 2026) | https://diariodarepublica.pt/dr/detalhe/decreto-lei/127-2025-967317021 | 2026-10-24 |
| ISS, Guia Prático, Pagamento de Contribuições à Segurança Social (deadlines F2, interest 7.221% for 2026) | https://www.seg-social.pt/ptss/pssd/documento/cmc1y95ap00dkkl2yk3g4tdla | 2026-10-24 |
| IGCP Aviso 18/2026/2 (late interest 7.221%) | https://diariodarepublica.pt/dr/detalhe/aviso/18-2026-993315668 | 2026-10-24 |
| Código do Trabalho (consolidated), arts. 228, 238, 263, 264, 266, 268, 276 | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34546475 | 2026-10-24 |
| DGERT, minimum wage 2026 (Decreto-Lei 139/2025, EUR 920) | https://www.dgert.gov.pt/retribuicao-minima-mensal-garantida-para-2026 | 2026-10-24 |
| Decreto Legislativo Regional 1/2026/M (Madeira minimum wage EUR 980) | https://www.madeira.gov.pt//Portals/25/Documentos/Legislacao/DLR_1_2026_M.pdf | 2026-10-24 |
| RGIT arts. 105, 114, 117 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit114.aspx | 2026-10-24 |
| LGT arts. 35 and 44 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt44.aspx | 2026-10-24 |

Not yet confirmed: the Diário da República text of Decreto-Lei 139/2025 itself (the EUR 920 figure is from DGERT and the preamble of Despacho 233-A/2026); the Azores 2026 minimum wage (EUR 966 in the old version of this skill; the regional decree was not found); whether Madeira adopted a November 2026 withholding cut (none found; the mainland and Azores despachos exclude Madeira); the Social Security declaration deadline during 2026 for employers still on the old reporting model (the old art. 40 text was not read); whether the IRS Jovem withholding cap in Despacho 233-A/2026 point 5(g) is per payment or cumulative over the year (the text speaks of the accumulated monthly exemptions); the mid-2026 cut to the first six IRS bands authorised by Proposta de Lei 108/XVII/2 (named in Despacho 12523-A/2026 but not read; it changes the annual assessment, not the January tables); the legal interest rate used for compensatory interest (LGT art. 35(10)); the rounding of the card limit to EUR 10.46 that the old version used; the remaining rows of each table and Tables IV to XI; the FCT and FGCT work compensation funds (the old version said contributions are suspended under Lei 13/2023); the 50% employer contribution cuts for first jobs and long-term unemployed hires; parental leave, sick pay (paid by Social Security from the 4th day at 55% to 75%), bereavement leave, 15 days marriage leave and compulsory work-accident insurance from the old version; record keeping periods (5 years labour, 10 years tax); the Relatório Único deadline (15 April); the annual return of income paid to others under CIRS art. 119(1)(c)(ii) by the end of February, wording of Decreto-Lei 49/2025.
