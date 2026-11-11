---
name: colombia-income-tax
description: "Colombian income tax for individuals (impuesto sobre la renta de personas naturales) for año gravable 2026, filed in August to October 2027. Covers residence (ET art. 10), the cédula system (arts. 330 to 336), the art. 241 progressive table in UVT with the 2026 UVT of COP 52,374 (DIAN Resolución 000238 de 2025), ingresos no constitutivos for mandatory pension and health contributions, the 25% labour exemption capped at 790 UVT, the 40% / 1,340 UVT cap on exempt income and deductions, the 72 UVT dependant addition, the 1% e-invoice purchases deduction, the choice between costs and the 25% exemption for independents, AFC/FVP, mortgage interest, prepaid medicine, GMF, dividends (art. 242 and 254-1), ganancias ocasionales at 15%, filing thresholds (arts. 592 to 594-3), Form 210, deadlines by NIT, anticipo, penalties and non-residents at 35%. Trigger on: declaración de renta 2026, renta personas naturales, Formulario 210, cédula general, UVT 2026, rentas exentas 25%, 1.340 UVT, independient"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/colombia-income-tax"
  jurisdiction: "CO"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Colombia: income tax for individuals, año gravable 2026 v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Tax year.** Año gravable 2026 (1 January to 31 December 2026), declared on Form 210 between August and October 2027. All thresholds are in UVT; for 2026 one UVT is **COP 52,374**, fixed by DIAN Resolución 000238 of 15 December 2025.

**Which text of the law.** The Estatuto Tributario (ET, Decreto 624 de 1989) as consolidated on the Senate's official site, last updated there on 15 October 2026 (Diario Oficial 53.651 of 7 October 2026). Ley 2277 de 2022 set the current caps. The 2026 emergency decrees (Decretos Legislativos 150, 173 and 240 de 2026) changed the wealth tax, IVA on online gambling and other items; none of them changes the arts. 241, 206 or 336 rules used here. Deadlines come from the Decreto Único Reglamentario 1625 de 2016 (DUR), art. 1.6.1.13.2.15, as substituted by Decreto 2229 de 2023.

Related Colombia skills, linked rather than repeated:

- [co-corporate-income-tax](co-corporate-income-tax.md): companies and the dividend rules from the company side.
- [co-vat-return](co-vat-return.md): IVA. An individual who is responsable de IVA must file income tax whatever their income (art. 592(1)).
- [co-social-contributions](co-social-contributions.md): pension, health and ARL for the self-employed, including the IBC. This skill uses only the contributions actually paid.
- [formalizing-small-informal-businesses-in-colombia](formalizing-small-informal-businesses-in-colombia.md): RUT, Régimen Simple and formalising a business (approved by Mauro Escudero; not repeated here).

## Who this applies to

- **Residents** (art. 10): a person present in Colombia more than 183 calendar days, counting entry and exit days, in any 365-day period (resident from the second year when the stay spans two years); Colombian diplomats abroad; and Colombian nationals whose spouse or dependent minor children are resident, or who have 50% or more of their income from Colombian sources, 50% or more of their assets administered or held in Colombia, or who live in a tax haven. A national is not resident under the third test if 50% or more of their income or assets are in the country where they live (art. 10, second parágrafo). Residents are taxed on worldwide income (art. 9).
- **Non-residents**: Colombian-source income only (art. 9), at a flat 35% (art. 247), without the cédula reliefs. Dividends to non-residents are at 20% (art. 245). See Cross-border points.
- **Employees** (rentas de trabajo from a labour relationship), **independents** (fees and services without a labour relationship), **landlords and investors** (rentas de capital), **other income** (rentas no laborales), **pensioners** and **shareholders**: all are covered here.
- **Out of scope**: Régimen Simple de Tributación members (they file the SIMPLE return; see the approved formalising skill), companies, and the wealth tax (impuesto al patrimonio).

## Rates, bands and thresholds

| Item | Figure | Year | Source URL |
|---|---|---|---|
| UVT for 2026 | COP 52,374 (DIAN Resolución 000238 of 15 Dec 2025, art. 1.2.1 Resolución 000227 de 2025) | 2026 | https://normograma.dian.gov.co/dian/compilacion/docs/resolucion_dian_0238_2025.htm |
| Table, 0 to 1,090 UVT (COP 0 to 57,087,660) | 0% | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr010.html (art. 241) |
| Table, over 1,090 to 1,700 UVT | 19% of (base in UVT minus 1,090) | 2026 | same |
| Table, over 1,700 to 4,100 UVT | 28% of (base minus 1,700) plus 116 UVT | 2026 | same |
| Table, over 4,100 to 8,670 UVT | 33% of (base minus 4,100) plus 788 UVT | 2026 | same |
| Table, over 8,670 to 18,970 UVT | 35% of (base minus 8,670) plus 2,296 UVT | 2026 | same |
| Table, over 18,970 to 31,000 UVT | 37% of (base minus 18,970) plus 5,901 UVT | 2026 | same |
| Table, over 31,000 UVT | 39% of (base minus 31,000) plus 10,352 UVT | 2026 | same |
| Cap on exempt income plus deductions in the cédula general | 40% of (income minus ingresos no constitutivos), never more than 1,340 UVT a year (COP 70,181,160) | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr014.html (art. 336(3)) |
| Dependant addition, outside the cap, for anyone with rentas de trabajo | 72 UVT per dependant (COP 3,770,928), up to 4 dependants | 2026 | same (art. 336(3)) |
| Purchases deduction, outside the cap | 1% of purchases paid electronically and backed by an e-invoice in the buyer's name, max 240 UVT (COP 12,569,760) | 2026 | same (art. 336(5)) |
| Labour exemption (also for independents who do not deduct costs) | 25% of labour payments after other reliefs, max 790 UVT a year (COP 41,375,460) | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr008.html (art. 206(10), par. 5) |
| Pension income exemption | first 1,000 UVT a month (COP 52,374,000) | 2026 | same (art. 206(5)) |
| Dependant deduction for employees (art. 387) | 10% of gross labour income, max 32 UVT a month (384 UVT a year, COP 20,111,616); inside the cap | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr015.html (art. 387) |
| Prepaid medicine and health insurance (art. 387) | max 16 UVT a month (192 UVT a year, COP 10,055,808); inside the cap | 2026 | same |
| Home loan interest (art. 119) | max 1,200 UVT a year (COP 62,848,800); ICETEX student loan interest max 100 UVT; inside the cap | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr005.html (art. 119) |
| Voluntary pension (FVP) plus AFC savings (arts. 126-1, 126-4) | exempt up to 30% of the year's labour or tax income and 3,800 UVT (COP 199,021,200); 10-year stay or housing use; inside the cap | 2026 | same (arts. 126-1, 126-4) |
| GMF (4 x 1,000) paid | 50% deductible, certified by the withholding bank | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr004.html (art. 115) |
| Mandatory pension and health contributions | ingreso no constitutivo de renta, outside the cap | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr002.html (arts. 55, 56) |
| Voluntary contributions to the mandatory pension fund (RAIS) | ingreso no constitutivo up to 25% of annual income, max 2,500 UVT | 2026 | same (art. 55) |
| Dividends cédula, discount | 19% of (dividends cédula in UVT minus 1,090 UVT), credited against the tax | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr010.html (art. 254-1) |
| Withholding on dividends to resident individuals | 0% up to 1,090 UVT; 15% above | 2026 | same (art. 242, parágrafo) |
| Ganancias ocasionales of resident individuals (fixed assets held 2 years or more and other occasional gains) | 15% | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr013.html (art. 314); holding rule art. 300 at http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr012.html |
| Gain on sale of the home, exempt part | first 5,000 UVT (COP 261,870,000) if the money goes to an AFC account for another home or to pay its mortgage | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr013.html (art. 311-1) |
| Renta presuntiva | 0% from año gravable 2021 | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr007.html (art. 188) |
| Non-resident individuals | 35% flat on Colombian-source taxable income | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr010.html (art. 247) |
| Filing threshold: gross income | 1,400 UVT (COP 73,323,600) or more | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr024.html (art. 592(1)) |
| Filing threshold: gross assets on 31 Dec | more than 4,500 UVT (COP 235,683,000) | 2026 | same (arts. 592(1), 593(1)) |
| Filing threshold: credit card spending, total purchases, bank deposits and investments | each more than 1,400 UVT | 2026 | same (art. 594-3) |
| Anticipo for the next year | 75% of net tax (or of the 2-year average); 25% in the first year of filing, 50% in the second; minus withholding | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr032.html (art. 807) |

**How the table works.** Convert the taxable base to UVT (divide by 52,374), apply the row, then multiply the UVT tax by 52,374. Form values are rounded to the nearest COP 1,000 (art. 577). Tax on a base B (in UVT) between 1,700 and 4,100 is (B minus 1,700) x 28% + 116 UVT.

## The base

**Cédulas (art. 330).** Income is worked out in three separate cédulas: (a) the cédula general (rentas de trabajo, de capital and no laborales), (b) pensions and (c) dividends. A relief used in one cédula cannot be used in another. A loss in a cédula is carried forward only against the same cédula; losses from years before 2019 go only against the cédula general. The renta líquida of the cédulas is added and taxed on the art. 241 table; cédula losses are not added (art. 331).

**Cédula general, in order (art. 336).**

1. Add all income except dividends and ganancias ocasionales: labour, independent services, interest, rent, royalties and other income (art. 335).
2. Subtract ingresos no constitutivos de renta: mandatory pension and health contributions paid (arts. 55, 56), voluntary RAIS contributions within 25% / 2,500 UVT (art. 55), and the others the law lists.
3. Costs and expenses: allowed against rentas de capital, rentas no laborales, and rentas de trabajo that do **not** come from a labour relationship (independents). They need an invoice meeting arts. 617 and 618 (art. 771-2). For work income, the law sets an indicative ceiling of 60% of gross income for costs; above it the costs are still deductible if they meet the rules, but the box on Form 210 must be ticked and the costs backed by electronic invoices or payroll documents (art. 336-1).
4. **An independent chooses: costs or the 25% exemption, not both** (arts. 336(4), 206 par. 5). See Example 1.
5. Subtract exempt income and deductions, all together capped at 40% of step 1 minus step 2, and never above 1,340 UVT (art. 336(3)). Inside the cap: the 25% exemption (max 790 UVT), FVP and AFC (30% / 3,800 UVT), home loan interest (1,200 UVT), prepaid medicine (16 UVT a month), the art. 387 dependant deduction (32 UVT a month), 50% of GMF, and other deductions.
6. Outside the cap: 72 UVT per dependant (up to 4) for anyone with rentas de trabajo, and the 1% e-invoice purchases deduction (max 240 UVT, cannot create a loss, not used for withholding). DIAN's Form 210 instructions add that one dependant supports only one of the two dependant reliefs (art. 387 or the 72 UVT), except for an employee in a labour relationship, who may claim both for the same dependant; and that the 72 UVT addition cannot exceed the net labour income in boxes 42 and 57.
7. The **25% exemption is computed last** within labour income: after subtracting ingresos no constitutivos, deductions and the other exemptions from the labour payments (art. 206(10)). It does not apply to severance (cesantías), to income exempt under other rules or to the taxable part of pensions (art. 206 par. 2).

**Who is a dependant (art. 387 par. 2).** Children up to 18; children 18 to 25 whose higher or accredited technical education the taxpayer pays; children over 18 dependent for certified physical or psychological reasons; a spouse or partner with no income or less than 260 UVT in the year (certified by a contador público) or certified dependent; parents and siblings on the same terms.

**Other labour exemptions (art. 206).** Work accident and maternity indemnities and funeral payments are exempt. Cesantías and their interest are exempt in full where average monthly pay in the last six months is up to 350 UVT, then partly on a sliding scale (90% up to 410 UVT down to 0% from 650 UVT). Exemptions for the armed forces, judges and public university rectors (art. 206(6) to (9)) sit outside the cap (par. 4).

**Pensions cédula.** Pensions are exempt up to 1,000 UVT a month (art. 206(5)); the rest is taxable. The taxpayer must meet the Ley 100 de 1993 pension requirements, and foreign pensions get the same treatment (art. 206 par. 3).

**Dividends cédula (arts. 242, 254-1).** Dividends from profits taxed at company level (art. 49(3)) are added to the base and taxed on the art. 241 table; the taxpayer then subtracts the discount of 19% of the dividends above 1,090 UVT (art. 254-1). Dividends from profits not taxed at company level (art. 49 par. 2) first bear the company rate in art. 240 for the year paid, and the rest then follows the same route. Dividends from foreign companies are taxed at the art. 240 rate (art. 242, last sentence), 35% on Form 210 box 120 (boxes 109 minus 110), with the art. 254 foreign tax credit. The dividends cédula takes no costs or deductions (art. 330). The payer withholds 15% above 1,090 UVT (art. 242 parágrafo), credited in the return.

**Ganancias ocasionales.** A gain on a fixed asset held two years or more is the sale price minus tax cost; held under two years, it is ordinary income (art. 300). Resident individuals pay 15% (art. 314). The first 5,000 UVT of gain on selling the taxpayer's home is exempt if the proceeds go to an AFC account and then to another home, or straight to the home's mortgage (art. 311-1).

**Renta presuntiva** is 0% from año gravable 2021 (art. 188), so no comparison is needed for 2026.

**Classifying bank receipts.** For the working paper, receipts from clients (bank transfer, Nequi, Daviplata, PSE, Mercado Pago, Stripe, PayPal) are gross income at their **pre-withholding** amount; client withholding is a credit, not a reduction of income. A DIAN refund is not income. Interest and rent go to rentas de capital; dividends to their own cédula. Loan proceeds, transfers between own accounts and tax payments are not income or expenses. Income tax paid is never deductible; other taxes linked to the activity are, and 50% of GMF (art. 115). Pension and health payments made through PILA go to step 2, not to costs.

## Deadlines and filing

| What | When | Rule |
|---|---|---|
| Form 210 for año gravable 2026, and payment in one instalment of tax plus anticipo | From the 7th business day of August 2027 (NIT ending 01-02) to the 17th business day of October 2027 (ending 99-00), by the last two digits of the NIT in the RUT, ignoring the check digit; two digits per business day | DUR art. 1.6.1.13.2.15 (calendar for August to October "2024 y en adelante para cada año subsiguiente") |
| Residents abroad | same calendar | same, parágrafo |
| Withholding by employers and clients during 2026 | monthly, on the art. 383 table for labour income and, "mensualized", for work income without a labour relationship | art. 383 and its par. 2 |

**Form 210, step by step.** Fill in and file the form online with DIAN's filing service (SI de Diligenciamiento), using the instructions for "año gravable 2023 y siguientes". The main boxes:

| Step | Form 210 boxes |
|---|---|
| Assets and debts at 31 December | 29 gross assets, 30 debts, 31 net assets |
| Labour income (employee) | 32 gross, 33 ingresos no constitutivos, 34 renta líquida, 35 and 36 exempt income (AFC/FVP, other), 38 and 39 deductions (home interest, other), 41 limited reliefs, 42 net |
| Independent work income | 43 gross, 45 costs (if chosen; tick box 140 if over the 60% indicative ceiling), 47 and 48 exempt income, 50 and 51 deductions, 53 limited reliefs, 57 net |
| Rentas de capital / no laborales | 58 to 73 / 74 to 90 |
| Cédula general totals | 91 renta líquida, 92 limited reliefs (= 28 + 41 + 53 + 69 + 86 + 139, capped at 40% / 1,340 UVT), 93 net, 97 taxable; 28 the 1% purchases deduction; 138 number of dependants, 139 the 72 UVT addition |
| Pensions | 99 to 103 |
| Dividends | 104 to 111 |
| Ganancias ocasionales | 112 to 115, tax 127 |
| Tax and credits | 116 to 121 tax on the bases, 122 foreign tax, 124 dividends discount, 125 total discounts, 126 net income tax, 129 total tax |
| Settlement | 130 last year's anticipo, 131 last year's credit balance, 132 withholding, 133 next year's anticipo, 134 balance due on tax, 135 penalties, 136 total to pay or 137 credit balance |

After filing, pay any balance with Form 490 (Recibo Oficial de Pago Impuestos Nacionales) by the same deadline. A credit balance can be refunded or carried to the next year (box 131).

## Penalties and interest

- **Late filing (art. 641).** 5% of the tax for each month or part month late, up to 100%. With no tax due: 0.5% of gross income per month, capped at the lowest of 5% of income, twice any credit balance, or 2,500 UVT if there is no credit balance.
- **Not filing after a DIAN summons (art. 643(1)).** 20% of the higher of the bank deposits or gross income found by DIAN, or the gross income in the last return filed.
- **Own correction (art. 644).** 10% of the extra tax (or reduced credit) if corrected after the deadline and before a DIAN summons; 20% after a summons or inspection order and before a special requirement. Add 5% a month from the deadline when the first return was late, up to 100%.
- **Inaccuracy (art. 648).** 100% of the difference found by DIAN; 200% where assets are omitted or false debts declared; reduced under arts. 709 and 713 when accepted.
- **Minimum penalty (art. 639).** 10 UVT (COP 523,740 in 2026).
- **Late payment interest (arts. 634, 635).** Daily, for each calendar day late, at the consumer-credit usury rate certified by the Superintendencia Financiera minus 2 points; DIAN publishes the rate.

## Cross-border points

- **Foreign income of a resident** goes in the same cédulas. Foreign income tax paid on it is a credit capped at the Colombian tax on that income (art. 254), entered in box 122.
- **Non-residents** pay 35% on Colombian-source income (art. 247), and 20% on dividends (art. 245). A non-resident whose whole income bore the withholding of arts. 407 to 411 need not file (art. 592(2)). A foreign professor hired for up to 182 days by a Colombian university pays 7%, withheld (art. 247 par.).
- **Becoming resident.** The 183-day count runs over any 365 days; when the stay spans two years, residence starts in the second year (art. 10(1)).
- Treaty relief, CFC (ECE) rules and the foreign-assets return are outside this skill.

## Two worked examples that recompute

### Example 1: independent consultant, costs or the 25% exemption (a decision)

Laura is resident and works as an independent consultant with no employees. In 2026 she bills COP 180,000,000. Her PILA payments were COP 11,520,000 to pension and COP 9,000,000 to health. She has COP 40,000,000 of business costs backed by e-invoices, and saved COP 10,000,000 in an AFC account. She has filed for many years, and clients withheld COP 6,000,000.

Ingresos netos: 180,000,000 minus 20,520,000 = COP 159,480,000. The cap on limited reliefs is the lower of 40% x 159,480,000 = 63,792,000 and 1,340 UVT = 70,181,160, so COP 63,792,000.

- **Option A, deduct costs.** Renta líquida 119,480,000; AFC 10,000,000 is within the cap, 30% and 3,800 UVT. Taxable COP 109,480,000 = 2,090.35 UVT. Tax: (2,090.35 minus 1,700) x 28% + 116 = 225.30 UVT = **COP 11,799,760**.
- **Option B, 25% exemption.** No costs. The 25% is on the labour income after other reliefs: 25% x (159,480,000 minus 10,000,000) = 37,370,000, under 790 UVT. Reliefs 47,370,000, under the cap. Taxable COP 112,110,000. Tax **COP 12,536,160**.

What decides it: costs of COP 40,000,000 beat an exemption of COP 37,370,000, so Option A saves COP 736,400. If her costs were below the 25% figure, Option B would win.

Settlement on Option A: anticipo for 2027 is 75% x 11,799,760 minus 6,000,000 withheld = COP 2,849,820. Total to pay = 11,799,760 + 2,849,820 minus 6,000,000 = COP 8,649,580 (COP 8,650,000 on the form, art. 577), by her NIT date in August to October 2027.

```oa-check
name: CO renta 2026, independent, costs vs 25% exemption
inputs:
  uvt: 52374
  fees: 180000000
  pension_health: 20520000
  costs: 40000000
  afc: 10000000
  withheld: 6000000
steps:
  - net_income: fees - pension_health
  - cap: min(net_income * 0.40, 1340 * uvt)
  - taxable_a: net_income - costs - min(afc, cap)
  - base_a_uvt: taxable_a / uvt
  - tax_a: ((base_a_uvt - 1700) * 0.28 + 116) * uvt
  - exempt25_b: min((net_income - afc) * 0.25, 790 * uvt)
  - reliefs_b: min(afc + exempt25_b, cap)
  - taxable_b: net_income - reliefs_b
  - tax_b: ((taxable_b / uvt - 1700) * 0.28 + 116) * uvt
  - saving_with_costs: tax_b - tax_a
  - anticipo: max(0, tax_a * 0.75 - withheld)
  - to_pay: tax_a + anticipo - withheld
expected:
  net_income: 159480000
  cap: 63792000
  taxable_a: 109480000
  tax_a: 11799760
  exempt25_b: 37370000
  taxable_b: 112110000
  tax_b: 12536160
  saving_with_costs: 736400
  anticipo: 2849820
  to_pay: 8649580
```

### Example 2: employee hitting the 1,340 UVT cap

Andrés is an employee in Bogotá. His 2026 labour payments are COP 300,000,000 and his certificate of income and withholding shows COP 25,500,000 of mandatory pension and health contributions. He paid COP 20,000,000 of home loan interest and COP 6,000,000 of prepaid medicine, saved COP 15,000,000 in AFC, and has one dependent child aged 10. His employer withheld COP 38,000,000.

- Ingresos netos: 300,000,000 minus 25,500,000 = COP 274,500,000.
- Dependant deduction (art. 387): 10% of 300,000,000 = 30,000,000, capped at 384 UVT = COP 20,111,616. Prepaid medicine 6,000,000 is under 192 UVT. Home interest 20,000,000 is under 1,200 UVT.
- 25% exemption: 25% x (274,500,000 minus 20,000,000 minus 20,111,616 minus 6,000,000 minus 15,000,000) = 53,347,096, capped at 790 UVT = COP 41,375,460.
- Limited reliefs claimed: COP 102,487,076. Cap: lower of 40% (109,800,000) and 1,340 UVT (70,181,160), so only **COP 70,181,160** counts.
- As an employee he may also take 72 UVT (COP 3,770,928) for the same child, outside the cap (box 139).
- Taxable: 274,500,000 minus 70,181,160 minus 3,770,928 = COP 200,547,912 = 3,829.15 UVT. Tax: (3,829.15 minus 1,700) x 28% + 116 = 712.16 UVT = **COP 37,298,775** (COP 37,299,000 on the form).
- Withholding of 38,000,000 exceeds 75% of the tax, so the anticipo is nil; he has a credit balance of about COP 701,225 (box 137), which he can ask DIAN to refund.

```oa-check
name: CO renta 2026, employee capped at 1,340 UVT with dependant addition
inputs:
  uvt: 52374
  salary: 300000000
  contributions: 25500000
  home_interest: 20000000
  prepaid_medicine: 6000000
  afc: 15000000
  withheld: 38000000
steps:
  - net_income: salary - contributions
  - dependant_387: min(salary * 0.10, 384 * uvt)
  - exempt25: min((net_income - home_interest - dependant_387 - prepaid_medicine - afc) * 0.25, 790 * uvt)
  - claimed: home_interest + dependant_387 + prepaid_medicine + afc + exempt25
  - cap: min(net_income * 0.40, 1340 * uvt)
  - allowed: min(claimed, cap)
  - taxable: net_income - allowed - 72 * uvt
  - tax: ((taxable / uvt - 1700) * 0.28 + 116) * uvt
  - anticipo: max(0, tax * 0.75 - withheld)
  - credit_balance: withheld - tax - anticipo
expected:
  net_income: 274500000
  dependant_387: 20111616
  exempt25: 41375460
  claimed: 102487076
  cap: 70181160
  allowed: 70181160
  taxable: 200547912
  tax: 37298775.36
  anticipo: 0
  credit_balance: 701224.64
```

## Ask the client first

1. Residence: days in Colombia in any 365-day period across 2025 and 2026, nationality, where the family lives, and where income and assets are. Non-residents use the 35% rate.
2. Kinds of income: salary (certificate of income and withholding), independent fees, rent, interest, pensions, dividends (with the company's certificate saying which part comes from taxed profits), and assets sold or inherited.
3. For an independent: gross fees, costs backed by e-invoices, and which is larger, the costs or the 25% exemption. Pension and health paid through PILA.
4. Reliefs: dependants and their ages, studies, income or certified dependency; home loan interest certificate; prepaid medicine; AFC, FVP and voluntary RAIS statements; GMF certificate; e-invoiced purchases paid electronically.
5. Withholding certificates from every payer, last year's return (anticipo paid, credit balance) and how many years they have filed.
6. Gross assets and debts on 31 December 2026, credit card spending, purchases and bank deposits (filing thresholds), and whether they were responsable de IVA.

## Sources

| Source | URL | Read on |
|---|---|---|
| DIAN Resolución 000238 of 15 Dec 2025: UVT 2026 = COP 52,374 (art. 1) | https://normograma.dian.gov.co/dian/compilacion/docs/resolucion_dian_0238_2025.htm | 2026-11-11 |
| Estatuto Tributario arts. 9 and 10 (scope, residence), Senate consolidated text | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario.html | 2026-11-11 |
| ET arts. 55, 56 (pension and health contributions) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr002.html | 2026-11-11 |
| ET art. 115 (taxes and GMF) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr004.html | 2026-11-11 |
| ET arts. 119, 126-1, 126-4 (home interest, FVP, AFC) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr005.html | 2026-11-11 |
| ET art. 188 (renta presuntiva) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr007.html | 2026-11-11 |
| ET art. 206 (labour exemptions) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr008.html | 2026-11-11 |
| ET arts. 241 (table, read from the image on the page), 242, 245, 247, 254, 254-1 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr010.html | 2026-11-11 |
| ET art. 300 (ganancias ocasionales on fixed assets) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr012.html | 2026-11-11 |
| ET arts. 311-1, 314 (home sale, 15% rate) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr013.html | 2026-11-11 |
| ET arts. 330, 331, 335, 336, 336-1 (cédulas, caps) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr014.html | 2026-11-11 |
| ET arts. 383 (withholding table and par. 2), 387 (dependants, prepaid medicine) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr015.html | 2026-11-11 |
| ET arts. 577, 592, 593, 594-3 (rounding, who files) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr024.html | 2026-11-11 |
| ET arts. 634, 635, 639, 641, 643, 644, 648 (interest and penalties) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr026.html | 2026-11-11 |
| ET art. 771-2 (invoices for costs) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr031.html | 2026-11-11 |
| ET art. 807 (anticipo) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr032.html | 2026-11-11 |
| DUR 1625 de 2016, art. 1.6.1.13.2.15 (deadlines for individuals, as substituted by Decreto 2229 de 2023), DIAN normograma | https://normograma.dian.gov.co/dian/compilacion/docs/decreto_1625_2016.htm | 2026-11-11 |
| DIAN, Form 210 and instructions "año gravable 2023 y siguientes" (boxes 28 to 140, box 139 dependant rule, box 980 and Form 490) | https://www.dian.gov.co/atencionciudadano/formulariosinstructivos/Formularios/2025/Formulario_210_2025.pdf | 2026-11-11 |

Not yet confirmed: the calendar dates in August to October 2027 (they depend on 2027 business days; only the business-day rule was read); whether DIAN prescribes a new Form 210 for año gravable 2026 (the current instructions say 2023 and following); the DUR withholding rates on fees other than the art. 383 table; the current usury rate for late interest; the foreign-assets return and the wealth tax for individuals.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `colombia-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/colombia-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
