---
name: bulgaria-tax-optimization
description: "Use this skill whenever asked about reducing tax in Bulgaria, tax planning, or legal strategies to minimise tax for a freelancer, sole trader, or small company in Bulgaria, for tax year 2026 (in euro). Trigger on phrases like \"reduce tax Bulgaria\", \"10% flat tax\", \"Bulgaria freelancer 7.5%\", \"svobodna profesiya\", \"normative expense deduction\", \"sole trader vs EOOD\", \"Bulgaria dividends 5%\", \"save tax Bulgaria\", \"Bulgaria tax haven\", \"tax planning Bulgaria\". This skill covers the freelancer statutory deduction (25%, or 40% for some professions) that taxes 75% of income at 10%, so 7.5% of gross before contributions; the choice between freelancer, sole trader (15%) and EOOD (10% plus 5% dividend tax, 14.5% on distributed profit); the self-insured contribution base and its annual reconciliation; voluntary insurance and other reliefs; and the anti-avoidance red lines. Out of scope, handled by sibling skills; computing the return (bulgaria-income-tax, bg-corporate-income-tax), contributions "
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bulgaria-tax-optimization"
  jurisdiction: "BG"
  tax_year: "2026"
  last_updated: "2026-11-16"
---

# Bulgaria Tax Optimization v0.3

> **General reference only.** This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Bulgaria) before acting upon.

## Scope

Tier 2, not yet approved. Built from the Bulgarian acts read on 16 November 2026 (listed under Sources). Figures must agree with `bulgaria-income-tax.md` and `bulgaria-social-contributions.md`; where they differ, those skills win. Aggressive positions are never advised; every suggestion must be reviewed.

Who this is for: a resident individual in Bulgaria working on their own account in tax year 2026 who is choosing between the freelancer regime, a sole trader (ET) and a single-member limited company (EOOD), and wants the legal levers: the statutory cost deduction, dividends, contributions, voluntary insurance and reliefs. Out of scope: computing the return (bulgaria-income-tax, bg-corporate-income-tax), contributions in detail (bulgaria-social-contributions), VAT (bulgaria-vat-return) and moves abroad (bg-cross-border).

Bulgaria adopted the euro on 1 January 2026. Lev amounts still in the laws convert at BGN 1.95583 = EUR 1, rounded to the cent (Euro Introduction Act arts. 11(2), 12, 13).

**Quick reference**

| Field | Value | Law | Source |
| --- | --- | --- | --- |
| Country and tax year | Republic of Bulgaria, 2026 (calendar year) | ZDDFL art. 53(1) | https://nra.bg/wps/wcm/connect/nra.bg25863/e0daae38-32b9-40b7-8c21-ff7feed98935/%D0%97%D0%94%D0%94%D0%A4%D0%9B+%D1%81%D0%B5%D0%BF%D1%82%D0%B5%D0%BC%D0%B2%D1%80%D0%B8+2026.docx?MOD=AJPERES |
| Currency | EUR from 1 January 2026; lev amounts convert at BGN 1.95583 = EUR 1 | Euro Introduction Act arts. 11(2), 12, 13 | https://dv.parliament.bg/DVWeb/showMaterialDV.jsp?idMat=224950 |
| Headline levers | Freelancer statutory deduction of 25% (40% for some professions), so **7.5%** of gross before contributions (6% at 40%, computed: 10% x 60%); freelancer vs sole trader vs EOOD; 5% dividend tax | ZDDFL arts. 29(1), 48(1), 46(3) | https://nra.bg/wps/wcm/connect/nra.bg25863/e0daae38-32b9-40b7-8c21-ff7feed98935/%D0%97%D0%94%D0%94%D0%A4%D0%9B+%D1%81%D0%B5%D0%BF%D1%82%D0%B5%D0%BC%D0%B2%D1%80%D0%B8+2026.docx?MOD=AJPERES |
| Personal income tax | **10% flat** on the general annual base; **15%** for sole traders | ZDDFL art. 48(1), (2) | same |
| Corporate tax (EOOD) | **10%**; dividend tax **5%**, so **14.5%** in total on profit that is fully paid out (computed: 10% + 5% x 90%) | ZKPO art. 20; ZDDFL arts. 38(1), 46(3) | https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/%D0%97%D0%9A%D0%9F%D0%9E+%D1%81%D0%B5%D0%BF%D1%82%D0%B5%D0%BC%D0%B2%D1%80%D0%B8+2026.docx?MOD=AJPERES https://nra.bg/wps/wcm/connect/nra.bg25863/e0daae38-32b9-40b7-8c21-ff7feed98935/%D0%97%D0%94%D0%94%D0%A4%D0%9B+%D1%81%D0%B5%D0%BF%D1%82%D0%B5%D0%BC%D0%B2%D1%80%D0%B8+2026.docx?MOD=AJPERES |
| Anti-avoidance | Deals that lead to tax evasion are disregarded; a freelancer must not be disguised employment | ZKPO art. 16(1); Labour Code arts. 1(2), 405a | https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/%D0%97%D0%9A%D0%9F%D0%9E+%D1%81%D0%B5%D0%BF%D1%82%D0%B5%D0%BC%D0%B2%D1%80%D0%B8+2026.docx?MOD=AJPERES https://nra.bg/wps/wcm/connect/nra.bg25863/63648ffc-3f9a-431c-86a1-3893043d2fbf/%D0%9A%D0%A2-082026.docx?MOD=AJPERES |

The Bulgarian headline is the FREELANCER regime (свободна професия, and also income under non-employment contracts). The law deducts a fixed share of income for costs, with no need to prove them: 25% for most liberal professions and contract income (ZDDFL art. 29(1)(3)). Only 75% of gross is taxable, and it is taxed at 10% (art. 48(1)), which is 7.5% of gross. The person's own social and health contributions then come off the base (art. 30, item 1), so the tax is lower than 7.5% of gross. Authors, performing artists, crafts outside the patent tax, lawyers and notaries get 40% (art. 29(1)(2)), which gives 6% of gross before contributions.

## Ask the client first

1. What is the work: a liberal profession, a non-employment contract, authorship or performance, a craft, law or notary practice? (This sets 25% or 40%.)
2. Expected gross income and real business costs for the year, as a share of gross.
3. Will the profit be paid out as dividends or kept in a company?
4. One client under employer-like control, or several independent clients?
5. Does the person have children under 18, or a child with 50% or more disability, and will the other parent claim the relief?
6. Is the person already insured elsewhere (employment, management contract), and which monthly insurable income do they plan to declare for advances?

## The method, step by step

### Step 1. Put the three structures side by side [ZDDFL, https://nra.bg/wps/wcm/connect/nra.bg25863/e0daae38-32b9-40b7-8c21-ff7feed98935/%D0%97%D0%94%D0%94%D0%A4%D0%9B+%D1%81%D0%B5%D0%BF%D1%82%D0%B5%D0%BC%D0%B2%D1%80%D0%B8+2026.docx?MOD=AJPERES; ZKPO, https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/%D0%97%D0%9A%D0%9F%D0%9E+%D1%81%D0%B5%D0%BF%D1%82%D0%B5%D0%BC%D0%B2%D1%80%D0%B8+2026.docx?MOD=AJPERES]

| Structure | Income tax | Best when | Law | Source |
| --- | --- | --- | --- | --- |
| **Freelancer** (свободна професия, self-insured) | 10% on gross less the 25% (or 40%) statutory deduction, less own contributions = **7.5% of gross** (6% at 40%, computed) before contributions; real expenses are not deducted | Solo professionals and consultants with low real expenses | ZDDFL arts. 29(1), 30, 48(1) | https://nra.bg/wps/wcm/connect/nra.bg25863/e0daae38-32b9-40b7-8c21-ff7feed98935/%D0%97%D0%94%D0%94%D0%A4%D0%9B+%D1%81%D0%B5%D0%BF%D1%82%D0%B5%D0%BC%D0%B2%D1%80%D0%B8+2026.docx?MOD=AJPERES |
| **Sole trader** (ET, едноличен търговец) | **15%** on the tax profit worked out under the Corporate Income Tax Act (real expenses), less own contributions | Rarely better than freelancer for solo work; the 15% rate is above the EOOD's 10% | ZDDFL arts. 26(1), 28(1), 48(2) | same |
| **EOOD** (single-member limited company) | **10% CIT**, then **5%** dividend tax on what is paid out = **14.5%** of profit if all is paid out (computed) | Real expenses are high, profit is kept in the company, there is a team, or liability and credibility matter | ZKPO art. 20; ZDDFL arts. 38(1), 46(3) | https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/%D0%97%D0%9A%D0%9F%D0%9E+%D1%81%D0%B5%D0%BF%D1%82%D0%B5%D0%BC%D0%B2%D1%80%D0%B8+2026.docx?MOD=AJPERES https://nra.bg/wps/wcm/connect/nra.bg25863/e0daae38-32b9-40b7-8c21-ff7feed98935/%D0%97%D0%94%D0%94%D0%A4%D0%9B+%D1%81%D0%B5%D0%BF%D1%82%D0%B5%D0%BC%D0%B2%D1%80%D0%B8+2026.docx?MOD=AJPERES |

### Step 2. Find where the lines cross (before contributions)

With gross income G and real costs C:

- Freelancer at 25%: tax = 10% x 75% x G = 7.5% of G.
- EOOD, all profit paid out: tax = 10% x (G - C) + 5% x 90% x (G - C) = 14.5% of (G - C). This beats the freelancer only when real costs exceed about 48.3% of gross (1 - 7.5 / 14.5).
- EOOD, all profit kept: tax = 10% of (G - C). This beats the freelancer once real costs exceed 25% of gross.
- Sole trader: tax = 15% of (G - C). This beats the freelancer only when real costs exceed 50% of gross.

### Step 3. Add the contributions before choosing

These lines ignore social and health contributions. A self-insured person pays advances on a monthly insurable income they choose between the minimum and the maximum set by the budget act (KSO art. 6(8)); after the year the final insurable income is fixed from the income declared in the annual return, within the same minimum and maximum, and the difference is paid (art. 6(9)). For a freelancer, `bulgaria-social-contributions.md` takes that income as gross less the statutory deduction, 75% of gross at 25%. A freelancer is insured as a self-insured person (KSO art. 4(3)(1)). An owner who works in the EOOD is self-insured as well (art. 4(3)(2)), and a company manager is insured for all risks, like an employee (art. 4(1)(7)). Model both structures with the contributions in `bulgaria-social-contributions.md` before choosing. We give no fixed revenue tipping point.

| Item | Amount and conditions | Law | Source |
| --- | --- | --- | --- |
| Minimum monthly insurable income, self-insured, 2026 | EUR 550.66 (1 January to 31 July); EUR 620.20 (1 August to 31 December) | 2026 State Social Insurance Budget Act art. 9 | https://nssi.bg/wp-content/uploads/zbdoo-2026.pdf |
| Maximum monthly insurable income, 2026 | EUR 2,111.64 (1 January to 31 July); EUR 2,300 (1 August to 31 December) | same | same |

### Step 4. Plan the profit extraction from an EOOD

- **EOOD profit taxation.** EOOD profit is taxed at 10% CIT (ZKPO art. 20). The 5% dividend tax arises only when a dividend is paid out, so profit kept in the company carries 10% until it is distributed (ZDDFL arts. 38(1), 46(3)).
- **Dividend tax.** 5% final tax on dividends and liquidation shares paid to an individual (ZDDFL arts. 38(1), 46(3)). The company withholds it and pays it by the end of the month after the quarter in which the decision to distribute the dividend was taken (art. 65(2)). Fully paid out, profit bears 14.5% in total.
- **Manager remuneration.** A manager under a management contract is insured for all risks (KSO art. 4(1)(7)). An owner who works in the company is self-insured (art. 4(3)(2)). A modest manager's remuneration can carry the social insurance while the rest is taken as dividends, but the role and the pay must be genuine. The minimum insurable income for a manager is not yet confirmed (see Sources).

### Step 5. Take the deductions and reliefs

| Item | Treatment and amount | Law | Source |
| --- | --- | --- | --- |
| Freelancer statutory deduction | 25% of gross (40% or 60% for the categories in art. 29(1)(1), (2)); no documents needed; real expenses cannot be deducted on top, because the law fixes the cost deduction | ZDDFL art. 29(1) | https://nra.bg/wps/wcm/connect/nra.bg25863/e0daae38-32b9-40b7-8c21-ff7feed98935/%D0%97%D0%94%D0%94%D0%A4%D0%9B+%D1%81%D0%B5%D0%BF%D1%82%D0%B5%D0%BC%D0%B2%D1%80%D0%B8+2026.docx?MOD=AJPERES |
| EOOD real expenses | Business costs reduce the 10% CIT base under the Corporate Income Tax Act; see `bg-corporate-income-tax.md` for what is not deductible | ZKPO art. 20 | https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/%D0%97%D0%9A%D0%9F%D0%9E+%D1%81%D0%B5%D0%BF%D1%82%D0%B5%D0%BC%D0%B2%D1%80%D0%B8+2026.docx?MOD=AJPERES |
| Social and health contributions | The contributions a self-insured person must pay for the year come off the taxable income (art. 30, item 1 for freelancers; art. 28(1) for sole traders). See Step 3 for the 2026 minimum and maximum. | ZDDFL arts. 28(1), 30 | https://nra.bg/wps/wcm/connect/nra.bg25863/e0daae38-32b9-40b7-8c21-ff7feed98935/%D0%97%D0%94%D0%94%D0%A4%D0%9B+%D1%81%D0%B5%D0%BF%D1%82%D0%B5%D0%BC%D0%B2%D1%80%D0%B8+2026.docx?MOD=AJPERES |
| Voluntary pension, health and life insurance | Personal contributions to voluntary supplementary pension insurance: deductible up to 10% of the annual bases. Personal voluntary health insurance contributions and life insurance premiums: deductible up to a further 10%. | ZDDFL art. 19(1); for sole traders art. 28(2)(1) | same |
| Children relief, 2026 | Annual base reduced by EUR 3,067.75 for one child under 18, EUR 6,135.50 for two and EUR 9,203.25 for three or more; a child with 50% or more disability adds EUR 6,135.50. Claimed only if the other parent does not claim it for the year. An employee may take EUR 255.65, 511.29 or 766.94 a month (EUR 511.29 for a disabled child) off the monthly employment base. Any part not used against the general base comes off a sole trader's base. How to claim is in `bulgaria-income-tax.md`. | ZDDFL arts. 22v(4), 22g; 2026 State Budget Act transitional and final provisions § 3(1) to (4) | https://www.parliament.bg/api/v1/act/167157 https://nra.bg/wps/wcm/connect/nra.bg25863/e0daae38-32b9-40b7-8c21-ff7feed98935/%D0%97%D0%94%D0%94%D0%A4%D0%9B+%D1%81%D0%B5%D0%BF%D1%82%D0%B5%D0%BC%D0%B2%D1%80%D0%B8+2026.docx?MOD=AJPERES |
| Early-filing discount | 5% of the tax still due, if the return is filed electronically and the tax paid by 31 March, with no debts under enforcement. It applies to both the 10% and the 15% tax; the total discount is capped at BGN 500, which is EUR 255.65 (computed: 500 / 1.95583). | ZDDFL art. 53(6) | https://nra.bg/wps/wcm/connect/nra.bg25863/e0daae38-32b9-40b7-8c21-ff7feed98935/%D0%97%D0%94%D0%94%D0%A4%D0%9B+%D1%81%D0%B5%D0%BF%D1%82%D0%B5%D0%BC%D0%B2%D1%80%D0%B8+2026.docx?MOD=AJPERES |
| Personal contributions | Mandatory contributions reduce the taxable base | ZDDFL arts. 28(1), 30 | same |
| Rounding | The annual tax is rounded to the whole euro after deductions and any discount | ZDDFL art. 48(8) | same |

## Boundary and exception table

| Situation | Treatment | Law |
| --- | --- | --- |
| Freelancer who is a lawyer or notary | 40% deduction, not 25% | ZDDFL art. 29(1)(2)(г) |
| Registered farmer selling unprocessed farm produce (not decorative plants) | 60% deduction | ZDDFL art. 29(1)(1) |
| Real costs above about 48.3% of gross, profit paid out | EOOD beats freelancer before contributions | Step 2 |
| Profit kept in the EOOD | Only the 10% CIT until distribution | ZKPO art. 20; ZDDFL art. 46(3) |
| Single client under employer-like control | Disguised employment risk: labour inspectorate may declare an employment relationship | Labour Code arts. 1(2), 405a(1) |
| Deals made only to cut tax | Tax base set without regard to them | ZKPO art. 16(1) |

## Worked cases

### Case 1. Decision: freelancer, sole trader or EOOD, gross EUR 50,000, real costs EUR 10,000

Real costs are 20% of gross, under both the 25% and the 48.3% lines. Before contributions: freelancer EUR 3,750 (7.5% x 50,000). EOOD paying out everything EUR 5,800 (14.5% x 40,000). EOOD keeping everything EUR 4,000. Sole trader EUR 6,000. Decision: the freelancer regime is cheapest at this cost level; it would lose to an EOOD keeping its profit only if real costs rose above EUR 12,500 (25% of gross), and to an EOOD paying everything out only above about EUR 24,138 (48.3% of gross). Then model the contributions (Step 3).

```oa-check
name: Bulgaria freelancer vs sole trader vs EOOD, gross EUR 50,000, costs EUR 10,000, 2026
inputs:
  gross: 50000
  costs: 10000
steps:
  - freelancer: gross * 0.75 * 0.10
  - profit: gross - costs
  - eood_paid_out: profit * 0.10 + profit * 0.90 * 0.05
  - eood_kept: profit * 0.10
  - sole_trader: profit * 0.15
  - breakeven_kept_costs: gross * 0.25
  - breakeven_paid_costs: round(gross * (1 - 0.075 / 0.145), 0)
expected:
  freelancer: 3750.00
  eood_paid_out: 5800.00
  eood_kept: 4000.00
  sole_trader: 6000.00
  breakeven_kept_costs: 12500.00
  breakeven_paid_costs: 24138.00
```

### Case 2. Author on 40%, own contributions and one child

A resident author earns EUR 30,000 of royalties in 2026, owes EUR 5,000 of own contributions for the year and has one child under 18; the other parent does not claim the relief. Taxable income 30,000 x 60% = EUR 18,000 (ZDDFL art. 29(1)(2)(б)). Less contributions: EUR 13,000 (art. 30, item 1). Less child relief EUR 3,067.75 (2026 State Budget Act § 3(1)): EUR 9,932.25. Tax at 10%: EUR 993.23 before the whole-euro rounding in art. 48(8). Effective rate on gross before rounding: about 3.3%.

```oa-check
name: Bulgaria author, royalties EUR 30,000, contributions EUR 5,000, one child, 2026
inputs:
  royalties: 30000
  own_contributions: 5000
  child_relief: 3067.75
steps:
  - taxable_income: royalties * (1 - 0.40)
  - after_contributions: taxable_income - own_contributions
  - tax_base: after_contributions - child_relief
  - tax_before_rounding: round(tax_base * 0.10, 2)
expected:
  taxable_income: 18000.00
  after_contributions: 13000.00
  tax_base: 9932.25
  tax_before_rounding: 993.23
```

## When to refuse or refer

**Red lines (do not cross)**

- **Disguised employment.** A "freelancer" working for a single client under employer-like control can be treated as an employee: labour must be supplied only under an employment relationship, and the labour inspectorate declares the employment relationship and its start date by an order (Labour Code arts. 1(2), 405a(1)). AUDIT FLASH POINT.
- **Substance requirement.** Where one or more deals, including between unrelated parties, lead to tax evasion, the tax base is set without regard to those deals, their terms or their legal form (ZKPO art. 16(1)). An EOOD used only to turn salary into dividends taxed at 5%, without a genuine business, can be challenged.
- **Minimum insurable income vs under-declaring.** Choosing the minimum monthly insurable income for advances is legal (KSO art. 6(8)). The final contributions still follow the income declared on the annual return (art. 6(9)). Under-declaring income is not legal.

**PROHIBITIONS**

- **Combining deductions.** NEVER combine the statutory deduction with real-expense deductions. It is one or the other.
- **Disguised employment presentation.** NEVER present the freelancer regime for what is really single-client employment.
- **Under-declaring income.** NEVER advise under-declaring income to cut tax or contributions.
- **Contradicting rates.** NEVER contradict the rates in `bulgaria-income-tax.md` / `bulgaria-social-contributions.md`.
- **Unconfirmed points.** NEVER present a "Not yet confirmed" point as settled, nor optimisation as definitive advice. Route the client to a licensed Bulgarian tax adviser.

Refer cross-border moves to bg-cross-border, VAT to bulgaria-vat-return, and the company tax computation to bg-corporate-income-tax.

## Filing and payment

- Freelancer: annual return 10 January to 30 April of the following year; sole trader 1 March to 30 June (ZDDFL arts. 51(1), 53(1)). The early-filing discount needs electronic filing and payment by 31 March (art. 53(6)).
- EOOD: dividend tax withheld and paid by the end of the month after the quarter of the distribution decision (ZDDFL art. 65(2)); corporate tax as in bg-corporate-income-tax.

## Sources

| Source | URL | Read on |
|---|---|---|
| Personal Income Taxes Act (ZDDFL), NRA consolidated text to State Gazette 85/2026: arts. 19, 22v, 22g, 26, 28, 29, 30, 38, 46, 48, 51, 53, 65 read (art. 22v still prints the old lev amounts; the 2026 amounts come from the State Budget Act below) | https://nra.bg/wps/wcm/connect/nra.bg25863/e0daae38-32b9-40b7-8c21-ff7feed98935/%D0%97%D0%94%D0%94%D0%A4%D0%9B+%D1%81%D0%B5%D0%BF%D1%82%D0%B5%D0%BC%D0%B2%D1%80%D0%B8+2026.docx?MOD=AJPERES | 2026-11-16 |
| Corporate Income Tax Act (ZKPO), NRA consolidated text to State Gazette 55/2026: arts. 16, 20 | https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/%D0%97%D0%9A%D0%9F%D0%9E+%D1%81%D0%B5%D0%BF%D1%82%D0%B5%D0%BC%D0%B2%D1%80%D0%B8+2026.docx?MOD=AJPERES | 2026-11-16 |
| Social Insurance Code (KSO), NRA consolidated text to State Gazette 68/2026: arts. 4(1)(7), 4(3)(1), (2), 6(8), (9) | https://nra.bg/wps/wcm/connect/nra.bg25863/8cd3cf0b-a0e9-4039-90c3-aa4c9d29425b/%D0%9A%D0%A1%D0%9E-082026.docx?MOD=AJPERES | 2026-11-16 |
| Labour Code, NRA consolidated text to State Gazette 69/2026: arts. 1(2), 405a(1) | https://nra.bg/wps/wcm/connect/nra.bg25863/63648ffc-3f9a-431c-86a1-3893043d2fbf/%D0%9A%D0%A2-082026.docx?MOD=AJPERES | 2026-11-16 |
| State Social Insurance Budget Act for 2026, State Gazette 68/2026, art. 9 (copy published by the National Social Security Institute) | https://nssi.bg/wp-content/uploads/zbdoo-2026.pdf | 2026-11-16 |
| State Budget Act of the Republic of Bulgaria for 2026, State Gazette 69/2026, transitional and final provisions § 3 (2026 child relief amounts), Parliament text (page; the same text is served as data at https://www.parliament.bg/api/v1/act/167157) | https://www.parliament.bg/bg/laws/ID/167157 | 2026-11-16 |
| Euro Introduction Act, State Gazette 70/2024 as published: arts. 11, 12, 13 | https://dv.parliament.bg/DVWeb/showMaterialDV.jsp?idMat=224950 | 2026-11-16 |
| Bulgarian National Bank, National Euro Changeover Plan (the fixed rate BGN 1.95583 = EUR 1) | https://www.bnb.bg/bnbweb/groups/public/documents/bnb_download/eurochangeoverplan_en.pdf | 2026-11-16 |

Not yet confirmed: the minimum insurable income for a manager under a management contract; the direction of the whole-euro rounding in ZDDFL art. 48(8) (the Act says the tax is rounded to the full euro without saying up or down); the old "EUR 100,000 to 150,000" freelancer-vs-EOOD tipping point (from a private adviser's site, no official source; replaced by the cost-share comparison in Step 2); the old claim that 7.5% is the lowest effective rate in the EU (no official source).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-16. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bulgaria-tax-optimization` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bulgaria-tax-optimization. If neither is available, confirm every figure against the official source pages cited above before relying on it.
