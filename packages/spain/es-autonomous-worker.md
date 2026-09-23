---
name: es-autonomous-worker
description: Use this skill whenever asked about Spanish self-employed (autónomo) tax and social security obligations beyond IRPF computation. Trigger on phrases like "autonomo", "autónomo", "cuota de autonomos", "cuota seguridad social autonomo", "RETA", "tarifa plana", "alta autonomo", "baja autonomo", "cotizacion por ingresos reales", "obligaciones fiscales autonomo", "modelos autonomo", "Modelo 303", "Modelo 130", "Modelo 390", "Modelo 349", "calendario fiscal autonomo", "pluriactividad", "autonomo societario", "facturacion autonomo", "estimacion directa", "libro registro", "IGIC autonomo", "IPSI autonomo", "autonomo Canarias", "autonomo Ceuta Melilla", "cuanto paga un autonomo", or any question about the complete fiscal and social security picture for a self-employed worker in Spain. ALWAYS read this skill before advising on autónomo setup, ongoing obligations, or take-home pay calculations.
version: 1.0
jurisdiction: ES
tax_year: 2026
last_updated: 2026-09-23
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - es-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Being an autónomo in Spain: tax and social security obligations

The whole picture for a self-employed worker (autónomo) in Spain: registering with the tax office and with Social Security, which IRPF regime applies, what may be deducted, what clients withhold, which returns fall due, and how the RETA contribution is built. Figures are for tax year 2026, with two exceptions that say so where they appear: the reduced starting contribution (tarifa plana) has no 2026 amount in law, because Real Decreto-ley 13/2022 fixed it for 2023 to 2025 only and left later years to a Budget Law that has not been approved; and the Canary Islands IGIC rates are those in force since 1 January 2024.

## Spain Autónomo (Self-Employed Worker) Complete Obligations Guide v1.0

> Based on work by Nambu89 (Impuestify) and Pau March (larenta), licensed under MIT. Adapted for the OpenAccountants format.

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | Spain (Estado Español) |
| Subject | Trabajador Autónomo (self-employed worker, sole trader) |
| Currency | EUR only |
| Legal framework | Ley 20/2007 (Estatuto del trabajo autónomo); Real Decreto-ley 13/2022 (contributions on real income); Ley 35/2006 and RD 439/2007 (IRPF) |
| Social Security regime | RETA (Régimen Especial de Trabajadores por Cuenta Propia o Autónomos) |
| Tax regime | IRPF, estimación directa simplificada by default |
| Tax authority | Agencia Tributaria for tax, Tesorería General de la Seguridad Social for contributions |
| Key filing forms | Modelo 036 (census), 130 (quarterly IRPF), 303 (quarterly VAT), 100 (annual IRPF) |
| Contribution bands and rates | In the Guide `es-social-contributions` |
| Income tax scale | In the Guide `es-income-tax`. Half state, half autonomous community, so there is no single Spanish rate |

## Section 2: Cuota de Autónomos in 2026: Cotización por Ingresos Reales

Since January 2023 an autónomo contributes on actual net income. Each year the Budget Law sets a general and a reduced table of contribution bases, split into bands of monthly net income with a minimum and a maximum base each (art. 308.1.a LGSS). The worker picks a base inside the band matching their forecast; Social Security regularises it later against the income the tax office reports.

### The contribution bands (tramos)

The 2026 tables and rates are in the Guide `es-social-contributions` and are not repeated here. Two limits from the same 2026 order are used below.

**The two limits used in this Guide**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296 |
| Maximum monthly base, whatever the net income | EUR 5,101.20 | "5.101,20 euros mensuales" |
| Floor for company owners and working partners (art. 305.2.b and e LGSS) and family members (art. 305.2.k): group 7 of the General Regime scale | EUR 1,424.40 | "7 Auxiliares Administrativos. 1.424,40" |

The contribution is base times rate and the autónomo pays every rate in full: there is no employer share. No official page adds the rates together, so no Guide should state a single combined percentage.

### How to Calculate Net Monthly Income (Rendimiento Neto)

Art. 308.1.c LGSS: take the net income of all activities as computed for IRPF, add back the RETA contributions, apply the deduction below, then divide by the months registered. That is the direct estimation case. For an activity in the module method the figure the law takes is the net income before reductions, and for farming, livestock and forestry the reduced one.

**Deduction for generic expenses before banding**

| Who | Deduction | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724 |
| Ordinary self-employed person | 7% | "gastos genéricos del 7 por ciento" |
| Company directors and working partners (art. 305.2.b and e LGSS) | 3% | "la deducción será del 3 por ciento" |

Ninety days registered in the year is enough for the lower deduction to apply.

### Key Rules

- **Changing the base.** Several times a year, to follow income. The count and the dates are set by regulation and published by Social Security.
- **Annual regularisation.** Social Security compares the bases paid with the income the tax office reports. Overpayments are refunded, underpayments collected (art. 308.1.c LGSS).
- **The floor.** Company owners and family members cannot pick a base below the minimum above, and regularisation cannot take the final base below it.
- **Pluriactividad.** An employee who is also an autónomo can reclaim part of the excess. The threshold and the capped share are in `es-social-contributions`.

## Section 3: Tarifa Plana (Flat Rate for New Autónomos)

### Standard Tarifa Plana (art. 38 ter Ley 20/2007)

The reduced starting contribution (cuota reducida, the tarifa plana) is one monthly amount instead of base times rate. It runs for the twelve complete calendar months after the alta takes effect, with nothing paid in them for cessation of activity or vocational training. A second twelve months can follow if net income then is below the annual minimum wage.

**Amount of the reduced contribution**

| Period | Monthly amount | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482 |
| The reduced contribution of art. 38 ter, both twelve month periods, for 2023, 2024 and 2025 | EUR 80 | "será de 80 euros mensuales" |
| From month 25 in the cases in art. 38 ter(10), same years | EUR 160 | "160 euros a partir del mes vigesimoquinto" |

**There is no 2026 amount in law.** The provision linked above sets the amount for 2023 to 2025 and leaves later years to the Budget Law. None has been approved for 2026, so no allowed official page prints a 2026 amount. Treat the amounts above as the 2023 to 2025 amounts and check what Social Security is charging before quoting one. What Social Security is actually charging appears on the award letter and the monthly receipt. Read the amount from that document and name it as the source; do not state one from memory.

### Requirements

- **New to RETA.** A first registration, or none in the two years before the alta takes effect.
- **Three years, not two,** if the worker used these reductions in an earlier registration.
- **It must be asked for,** at the alta, and again before the second period starts. It is not automatic.
- **The second period** needs a declaration that net income will be below the annual minimum wage.
- **Not for family members** of an autónomo up to the second degree, nor for members of Catholic institutes of consecrated life (art. 38 ter(11)).
- **Company partners can use it.** Art. 38 ter(9) extends it to partners of capital and labour companies and to working members of worker cooperatives who fall into RETA.

### Extended Tarifa Plana (longer periods)

**Longer periods for particular situations**

| Situation | Effect | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409 |
| Recognised degree of disability at or above the level in art. 38 ter(10) | First period 24 complete months, second period 36 | "discapacidad igual o superior al 33 por ciento" |
| Victims of gender violence or of terrorism | The same longer periods | "víctimas de violencia de género" |

### Important Notes

- **No retroactive request,** and no claim for months already past.
- **A baja ends it,** and the worker may renounce it from the first day of the next month.
- **Hiring staff does not end it.**
- **Regularisation.** None in the first period; in the second, one if income turns out above the annual minimum wage.
- **Benefits** earned while it is paid use the minimum base of the lowest band of the general table.
- **After it ends,** all contingencies are paid for in the ordinary way.

## Section 4: Complete Fiscal Calendar for Autónomos

### Quarterly Obligations

Art. 111 RD 439/2007: the first three quarters between the 1st and the 20th of April, July and October, the fourth between the 1st and the 30th of January. A quarter with nothing to pay is still filed, as a negative return. https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820

| Quarter | Period | Deadline | Models to file |
| --- | --- | --- | --- |
| Q1 | January to March | 1 to 20 April | 130 (IRPF) and 303 (VAT) |
| Q2 | April to June | 1 to 20 July | 130 and 303 |
| Q3 | July to September | 1 to 20 October | 130 and 303 |
| Q4 | October to December | 1 to 30 January | 130 and 303 |

### Annual Obligations

| Model | Description | Deadline |
| --- | --- | --- |
| 100 | Declaración de la Renta, the annual IRPF return | Spring campaign, dates set by the order approving the model |
| 390 | Annual VAT summary | January |
| 347 | Operations with third parties above the threshold in Section 10 | February |
| 349 | Intra-EU operations, if any | Monthly or quarterly, by volume |

### Additional Models (if applicable)

| Model | Who | When |
| --- | --- | --- |
| 111 | Anyone who withholds from staff or from professional invoices | Quarterly |
| 115 | Anyone who withholds on rent for business premises | Quarterly |
| 131 | Instead of 130, for an activity in estimación objetiva (módulos) | Quarterly |
| 720 | Assets abroad above the threshold in Section 10 | Until 31 March |

## Section 5: Indirect Tax by Territory

### IVA (Common Territory + Baleares)

**Spanish VAT rates**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 |
| General rate (art. 90.Uno) | 21% | "al tipo del 21 por ciento" |
| Reduced rate (art. 91.Uno): food, water, passenger transport, hotels, restaurants, new housing | 10% | "el tipo del 10 por ciento" |
| Super-reduced rate (art. 91.Dos): plain bread, milk, cheese, eggs, fruit, vegetables, olive oil, books, medicines | 4% | "el tipo del 4 por ciento" |

Filed on modelo 303 each quarter, with modelo 390 as the annual summary. The rate is the one in force when the tax point arises, not when the invoice is issued. See `es-vat-return`.

### IGIC (Canarias)

The Canary Islands are outside the Spanish VAT territory. An autónomo established there charges IGIC and files the quarterly modelo 420 with the Agencia Tributaria Canaria. Rates are in art. 51 Ley 4/2012 of the Canary Islands, wording in force since 1 January 2024.

**IGIC rates**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2012-9282 |
| Zero rate, supplies listed in art. 52 | Zero rate | "El tipo cero, aplicable a las entregas de bienes" |
| Reduced rate, art. 54 | 3% | "El tipo reducido del 3 por ciento" |
| Reduced rate, art. 54 bis | 5% | "El tipo reducido del 5 por ciento" |
| General rate, everything not in another rate | 7% | "El tipo general del 7 por ciento" |
| Increased rate, art. 55 | 9.5% | "incrementado del 9,5 por ciento" |
| Increased rate, art. 56 | 15% | "incrementado del 15 por ciento" |
| Special rate, art. 57 | 20% | "El tipo especial del 20 por ciento" |

### IPSI (Ceuta and Melilla)

Ceuta and Melilla are outside both the VAT and the IGIC territories and charge their own IPSI on imports, production and services. Rates and forms are set by each city's ordinance, which is not published on any site this Guide may cite, so no IPSI rate is stated here.

## Section 6: Net Take-Home Calculation (Sueldo Neto Autónomo)

### Monthly Calculation Formula

1. Start from the fee for the month, without indirect tax.
2. Add the VAT, IGIC or IPSI charged to the client. That money is the tax authority's, not income.
3. Take off the IRPF withholding the client applies, if the activity is professional (Section 9).
4. What is left is the cash received; from it come the RETA contribution and the running costs.
5. Separately, the indirect tax to pay over is tax on sales less deductible tax on purchases, settled on modelo 303.

### Annual Calculation Formula

1. Gross fees for the year, without indirect tax.
2. Less the deductible expenses in Section 10, RETA contributions included.
3. Less, in estimación directa simplificada only, the hard to justify deduction in Section 10.
4. The result is the net income from the activity, which joins the general IRPF base with the client's other income.
5. The tax on that base uses the state scale plus the client's community scale: `es-income-tax`. This Guide states no income tax rate, because half of it is regional.
6. Deduct the withholdings suffered and the modelo 130 payments. The difference is paid or refunded on modelo 100.

### Worked Example: IT Freelancer, Madrid

The worked example with amounts was removed in this refresh: every figure in it was computed rather than read off an official page, and its last step cannot be computed without naming the autonomous community, whose scale is on no national page. Use the orders of operations above with the client's own numbers, the band from `es-social-contributions` and the tax from `es-income-tax`. The cash left each month is not the yearly result: withholdings and modelo 130 payments are prepayments that the annual return settles.

## Section 7: Territorial Regime Classification

| Fiscal residence | IRPF scale | Indirect tax | Social Security |
| --- | --- | --- | --- |
| Common territory | State plus community scale | VAT | Ordinary RETA rules |
| Canarias | State plus community scale | IGIC | Ordinary RETA rules |
| Ceuta | State plus community, with the credit below | IPSI, set by the city | Bonification below, listed sectors |
| Melilla | State plus community, with the credit below | IPSI, set by the city | Bonification below, listed sectors |
| País Vasco (Álava, Bizkaia, Gipuzkoa) | Foral: own income tax law and scale | VAT | Ordinary RETA rules |
| Navarra | Foral: own income tax law and scale | VAT | Ordinary RETA rules |

The foral scales are not in this Guide. Quoting a Spanish scale to a Basque or Navarrese client quotes the wrong law.

**Ceuta and Melilla: the two reliefs**

| Relief | Value | Note |
| --- | --- | --- |
| Source, IRPF credit, art. 68.4 Ley 35/2006 | see below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Credit against the tax on income earned in Ceuta or Melilla by someone habitually and effectively resident there | 60% | "se deducirán el 60 por ciento" |
| Source, contribution bonification to 30 September 2026, art. 36 Ley 20/2007 in the wording of Real Decreto-ley 1/2023 | see below | https://www.boe.es/buscar/act.php?id=BOE-A-2023-625 |
| Bonification of the common contingencies contribution, contributions accrued before 1 October 2026 | 50% | "bonificación del 50 por ciento de la cuota por contingencias comunes" |
| Bonification of the common contingencies contribution, contributions accrued from 1 October 2026 | 75% | "bonificación del 75 por ciento de la cuota" |

Art. 36 changed inside the tax year. The wording in force from 1 January 2023 was introduced by disposición final 2.Uno of Real Decreto-ley 1/2023 and it named building construction INSIDE the exception clause, so a builder in Ceuta or Melilla was out of the relief. The wording in force from 1 October 2026 does not name it at all, so a builder is in. That one sentence carries its exceptions inside it, so read art. 36 for the period in question before deciding a sector is in or out. The wording above is the one introduced by Real Decreto-ley 22/2026 of 1 September, which the law's own note says has effect for contributions accrued from 1 October 2026. For a contribution accrued earlier in 2026, use the earlier wording and the earlier sector list.

### Ceuta and Melilla: sectors with the contribution bonification

- **The sectors, in the words of art. 36.** Agriculture, fishing and aquaculture; industry except energy and water; commerce; tourism; hospitality and the rest of services, except fixed-wing air transport; financial and insurance activities; and real estate activities. The list that applied before 1 October 2026 also included building construction. One sentence with exceptions inside it, so read the article before relying on it.

## Section 8: Types of Autónomo

### 8.1 Autónomo Persona Física (Standard)

- **Autónomo persona física.** A sole trader or freelancer taxed as an individual under IRPF, in estimación directa simplificada unless another regime is chosen or imposed. Clients withhold on professional invoices only (Section 9).

### 8.2 Autónomo Societario

- **Who it is.** A partner or director who falls into RETA under art. 305.2.b LGSS. The law does not state the test as a percentage. Effective control is taken as given, with no proof to the contrary allowed, where the worker's own shares are at least half the capital. Below that it is presumed, and the presumption can be rebutted, where at least half the capital is held among relatives living with the worker, where the worker's holding is at least a third of the capital, or at least a quarter of it with management functions. Even outside all of these the administration may prove effective control by any means.
- **Contribution floor and deduction.** The floor and the lower generic deduction in the Section 2 tables both apply to them.
- **The reduced starting contribution is open to them,** by art. 38 ter(9) Ley 20/2007, on the ordinary conditions.
- **Their pay is employment income.** What the company pays them for their work is rendimientos del trabajo, not business income, so there is no modelo 130 for it.

### 8.3 Autónomo Colaborador (Family Member)

- **Who it is.** The spouse, registered partner or a relative up to the second degree who works regularly in the business, joins RETA in their own name and was not registered in RETA in the five years before.

**Bonification for a family member joining RETA**

| Period | Bonification of the common contingencies contribution | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409 |
| First eighteen months | 50% | "al 50 por ciento durante los primeros dieciocho meses" |
| The following six months | 25% | "al 25 por ciento durante los seis meses siguientes" |

It is worked out on the common contingencies contribution at the minimum base of band 1 of the general table. A family member has the Section 2 floor and cannot use the Section 3 reduction.

### 8.4 Autónomo Económicamente Dependiente (TRADE)

**When a worker is economically dependent**

| Test | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409 |
| Share of income from work and from economic or professional activities coming from one client | 75% | "75 por ciento de sus ingresos" |

- **And the other conditions.** Art. 11.2 Ley 20/2007 requires all of them at once: no employees and no subcontracting of the work, own premises and equipment where the activity needs them, own organisational criteria, and payment by the results of the work rather than a wage. A freelancer whose biggest client passes the share above is not a TRADE unless every one of these also holds.
- **What changes.** A written contract registered with the public employment service, and the protections in Ley 20/2007. Tax obligations are unchanged.

- **Pluriactividad.** Someone contributing as an employee and in RETA in the same year can reclaim part of the excess once the two sets of common contingencies contributions pass a yearly threshold, capped at a share of what was paid in RETA. The threshold and the share are in `es-social-contributions`: https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/CotizacionRecaudacionTrabajadores/36537

## Section 9: Registration Process (Alta de Autónomo)

### Steps

- **Step 1: Alta en Hacienda.** File the census declaration of alta in the Censo de Empresarios, Profesionales y Retenedores before the activity starts, choosing the IAE heading, the IRPF regime and the VAT regime. **The form is modelo 036 only.** Modelo 037, the simplified census declaration, was suppressed by Orden HAC/1526/2024, in force from 3 February 2025: https://www.boe.es/buscar/doc.php?id=BOE-A-2025-410 The census obligations are in RD 1065/2007: https://www.boe.es/buscar/act.php?id=BOE-A-2007-15984
- **Step 2: Alta en RETA.** Register with Social Security, declaring the forecast of average monthly net income so a base can be chosen in the right band (art. 308.1.a LGSS), and ask for the reduced starting contribution in the same application if the Section 3 conditions are met: https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724
- **Step 3: Licencia de actividad.** Some activities and any premises need a municipal licence: town hall law, not covered here.
- **Step 4: Libros registro.** Start the books on day one. Under art. 68 RD 439/2007 a non-mercantile activity in direct estimation keeps a sales and income book, a purchases and expenses book and a capital assets book; a professional activity also keeps a book of provisions and advances: https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820

### Key Decisions at Registration

| Decision | Options | Default |
| --- | --- | --- |
| Estimation regime | Directa simplificada, directa normal, objetiva (módulos) | Simplificada, unless turnover is over the Section 10 limit |
| IAE heading | Section one (business) or section two (professional) | Decides whether clients withhold |
| VAT regime | General, simplified, recargo de equivalencia | General |
| Reduced starting contribution | Ask at the alta or not at all | Ask if the Section 3 conditions are met |
| Contribution base | The minimum of the band, or higher | The minimum of the band |

**Withholding on professional invoices**

| Case | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Ordinary rate on a professional invoice to a business or another professional (art. 95.1) | 15% | "el tipo de retención del 15 por ciento" |
| Starting a professional activity: the year it starts and the two following years, if no professional activity was carried on in the year before | 7% | "será del 7 por ciento en el período impositivo de inicio" |

The reduced rate is notified to the payer in writing and the payer keeps the signed notice. Most business activities in section one of the IAE are not withheld on, but not all: art. 95.6 Reglamento IRPF withholds on a listed set of section one activities when they are in the module method, and arts. 95.4 and 95.5 withhold on farming, livestock and forestry. Check the activity against art. 95 before telling a client there is no withholding. The payer declares the withholding on modelo 111; the professional credits it in the return.

**Quarterly payment on account**

Modelo 130 is a fixed share of net income from 1 January to the end of the quarter, less the earlier quarters' payments and the withholdings suffered (art. 110.1.a RD 439/2007). A professional is released from filing it at all when enough of the previous calendar year's income from the activity bore withholding (art. 109.2). In the year the activity starts there is no previous year to look at, so art. 109.5 applies the same test to the period the payment on account itself covers. Módulos use modelo 131 at its own rates (art. 110.1.b). The rates and the release share are in `es-estimated-tax`: https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820

**Rate of the payment on account**

| Case | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Activity in direct estimation, on net income from 1 January to the end of the quarter (art. 110.1.a) | 20% | "el 20 por ciento del rendimiento neto" |

## Section 10: Deductible Expenses for Autónomos

An expense is deductible in direct estimation if it is linked to the activity, recorded in the books and supported by a proper invoice. Capital assets are depreciated, not deducted at once; the simplified table is in `es-income-tax`.

### Fully Deductible (with proper invoice)

| Expense | Notes |
| --- | --- |
| RETA contributions | The worker's own contributions |
| Rent of business premises | Withholding on the rent may apply, on modelo 115 |
| Professional services (gestoría, lawyer) | With an invoice |
| Software and subscriptions used in the activity | Business use |
| Advertising and marketing | With an invoice |
| Training related to the activity | With an invoice |
| Professional liability and other business insurance | With an invoice |
| Bank charges on the business account | With an invoice or statement |
| Payment processor fees | With an invoice |
| Depreciation of capital assets | See `es-income-tax` |
| Business travel and transport | Documented trips |

### Partially Deductible (Special Rules)

**Limits on particular expenses**

| Expense | Limit | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Water, gas, electricity, telephone and internet where the home is partly used for the activity: the deductible share is this percentage applied to the proportion of square metres used for the activity, unless a different share, higher or lower, is proved (art. 30.2.5.b) | 30% | "aplicar el 30 por ciento a la proporción" |
| Health insurance for the worker, the spouse and children under 25 living with them, per insured person per year (art. 30.2.5.a) | EUR 500 | "será de 500 euros" |
| The same, for an insured person with a disability (art. 30.2.5.a) | EUR 1,500 | "o de 1.500 euros por cada una de ellas con discapacidad" |

Art. 30.2.5.c Ley 35/2006 lets the worker deduct their own meals, up to the limits set for employees in art. 9 RD 439/2007, if the meal is taken in a restaurant or hotel and paid by electronic means.

| Meal limits taken from the employee rules | Daily limit | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| In Spain, no overnight stay | EUR 26.67 | "no excedan de 26,67" |
| Abroad, no overnight stay | EUR 48.08 | "26,67 ó 48,08 euros diarios" |
| With an overnight stay away | Higher limits, in the same article | "Por gastos de manutención" |

- **Vehicles.** For IRPF a car, moped or motorcycle counts as used in the activity only if it is used exclusively for it. Art. 22.4 Reglamento IRPF lifts that rule for five cases: mixed vehicles carrying goods, passenger transport for a fee, driving and flying instruction for a fee, the professional journeys of commercial representatives and agents, and vehicles habitually hired out for a fee. VAT is a separate rule with its own presumption, in the table below; do not carry one answer across to the other tax. The presumption can be displaced by proof either way, and the vehicles listed in the same rule, such as goods vans and driving school cars, are presumed wholly used in the business.

**Vehicle, the VAT side**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 |
| Share of a car, trailer, moped or motorcycle presumed used in the business, for deducting VAT (art. 95.Tres.2) | 50% | "en la proporción del 50 por 100" |

- **Mixed use items such as a mobile phone.** Only the business share, and only if it can be shown. The official pages give no default split, so nothing is deducted without evidence.
- **Entertaining clients.** The rule covers the worker's own meals only. Anything spent on a client is not in it.
- **Personal insurance.** Not deductible, apart from the health insurance above.
- **The tax itself.** Modelo 130 payments are prepayments of IRPF, not an expense.

### Gastos de Difícil Justificación (Simplificada only)

**Deduction for provisions and hard to justify expenses**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Percentage of net income before this item (art. 30.2 RD 439/2007) | 5% | "el porcentaje del 5 por ciento" |
| Yearly cap in cash | EUR 2,000 | "superar 2.000 euros anuales" |
| Net turnover of the preceding year above which estimación directa simplificada cannot be used (art. 28.1.b) | EUR 600,000 | "no supere los 600.000 euros" |

It is a cap, not an allowance: the deduction is the percentage of net income, up to the cash cap. It is not available to a taxpayer taking the new activity reduction of art. 26.1 RD 439/2007.

**Module method limits, and two reporting thresholds**

| Limit | Value | Note |
| --- | --- | --- |
| Source, module limits, art. 31.1.3 Ley 35/2006 | see below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Prior year income from all activities except farming, above which módulos cannot be used | EUR 150,000 | "150.000 euros anuales" |
| Of that, prior year income invoiced to businesses and professionals | EUR 75,000 | "supere 75.000 euros" |
| Prior year purchases, capital assets excluded | EUR 150,000 | "supere la cantidad de 150.000 euros" |
| Source, the higher limits the Agencia Tributaria still states for 2016 to 2026 | see below | https://sede.agenciatributaria.gob.es/Sede/empresarios-individuales-profesionales/contribuyentes-modulos/quien-se-aplica/irpf.html |
| Prior year income from all activities except farming, Agencia Tributaria page | EUR 250,000 | "los límites de 150.000 € y 75.000 € pasan a ser 250.000 € y 125.000 €" |
| Of that, invoiced to businesses and professionals, Agencia Tributaria page | EUR 125,000 | "pasan a ser 250.000 € y 125.000 € respectivamente" |
| Source, modelo 720 and modelo 347, RD 1065/2007 | see below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-15984 |
| Assets abroad: each reporting block is filed once it passes this figure (art. 42 bis) | EUR 50,000 | "conjuntamente, los 50.000 euros" |
| Operations with one third party in the calendar year, above which they go on modelo 347 | EUR 3,005.06 | "3.005,06 euros durante el año natural" |

The higher module limits people remember are in disposición transitoria 32 Ley 35/2006, whose heading still reads "en los ejercicios 2016 a 2024". Real Decreto-ley 9/2024, 16/2025 and 2/2026 each tried to extend them and the Congress of Deputies left each one without effect, which is why the statutory figures above are the ones the law now prints for 2026. The 2026 module order does not print a figure of its own: it sends the reader back to art. 31.1.3. But the Agencia Tributaria's own page on who the module method applies to still states the higher limits for the years 2016 to 2026 inclusive, and it was last updated in September 2026. The two sources disagree. Do not tell anyone they are inside or outside the module method on the statutory figures alone: check the position with the Agencia Tributaria for the year in question.

## Section 11: Obligación de Declarar (Filing Obligation)

An autónomo files the annual return. Art. 96 Ley 35/2006 says that anyone who was registered in RETA, or in the seafarers' self-employed scheme, at any moment in the tax year must file in any case, whatever they earned. The thresholds below therefore matter for the client's other income, not for the activity.

**Filing thresholds for the listed sources of income**

| Situation | Limit | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Employment income, one payer | EUR 22,000 | "con el límite de 22.000 euros anuales" |
| Employment income, more than one payer, where the later payers together pass the tolerance below | EUR 15,876 | "será de 15.876 euros" |
| Tolerance for second and later payers | EUR 1,500 | "la cantidad de 1.500 euros anuales" |
| Investment income and capital gains subject to withholding, together | EUR 1,600 | "con el límite conjunto de 1.600 euros" |
| Imputed property income, certain bills and grants, together | EUR 1,000 | "con el límite conjunto de 1.000 euros" |

- **Always file.** Anyone who held an alta in RETA at any point in the year files modelo 100, whatever the amount.

## Section 12: Conservative Defaults

| Ambiguity | Default |
| --- | --- |
| Unknown estimation regime | Directa simplificada |
| Unknown contribution band | Compute net income under art. 308.1.c LGSS as in Section 2, then read the band from `es-social-contributions` |
| Unknown eligibility for the reduced starting contribution | Not eligible, ordinary bands apply |
| Unknown whether the person is new to RETA | Not new |
| Unknown IAE section | Section two, professional, so the ordinary withholding in Section 9 applies |
| Unknown business use share of a mixed use item | Nothing deducted |
| Unknown territory | Common territory, with VAT |
| Unknown start date of the activity | Do not apply the reduced starting contribution |
| Unknown autonomous community | State no income tax figure at all |

## PROHIBITIONS

- **Prohibition 1.** Never tell someone actively working for themselves that they can skip the RETA contribution.
- **Prohibition 2.** Never say the reduced starting contribution is closed to company partners: art. 38 ter(9) Ley 20/2007 extends it to them. The excluded ones are family members and members of consecrated life institutes (art. 38 ter(11)).
- **Prohibition 3.** Never state a monthly amount for the reduced contribution as a 2026 figure.
- **Prohibition 4.** Never deduct client entertainment as a travel meal.
- **Prohibition 5.** Never swap the two generic deduction percentages in Section 2. The lower one is for company directors and working partners.
- **Prohibition 6.** Never treat withholdings or modelo 130 payments as business expenses.
- **Prohibition 7.** Never charge VAT for an autónomo established in the Canary Islands (IGIC) or in Ceuta and Melilla (IPSI).
- **Prohibition 8.** Never forget that modelo 130 is cumulative from 1 January, not the quarter alone.
- **Prohibition 9.** Never present a contribution as final. Regularisation happens after the year end.
- **Prohibition 10.** Never quote a total Spanish income tax rate. Half the scale is the community's, and the foral territories have their own law.
- **Prohibition 11.** Never advise on a baja without saying it can end the reduced contribution and lengthen the gap before claiming it again.

## The method, step by step

1. Fix the facts that decide the rest: the client's residence, whether the activity is in section one or two of the IAE, and whether they are a partner or director of a company (RETA test: art. 305.2.b LGSS): https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724
2. File the census declaration of alta on modelo 036 before the activity starts, choosing the IRPF and VAT regimes. Modelo 037 no longer exists: https://www.boe.es/buscar/doc.php?id=BOE-A-2025-410
3. Register in RETA with a forecast of average monthly net income, and ask for the reduced starting contribution in the same application if art. 38 ter Ley 20/2007 is met: https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409
4. Band the contribution: compute the income under art. 308.1.c LGSS, apply the Section 2 deduction, then take the band and base from `es-social-contributions`: https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724
5. Open the record books required by art. 68 RD 439/2007 and keep them from the first invoice: https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820
6. Invoice with the right indirect tax for the territory (Section 5) and, for a professional activity, the withholding in Section 9: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740
7. Each quarter file modelo 130 under arts. 110 and 111 RD 439/2007, unless the prior year withholding test releases the client, and modelo 303: https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820
8. After the year end file modelo 100, deducting the withholdings suffered and the modelo 130 payments: https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764
9. Check the Social Security regularisation against the income declared and pay or claim the difference (art. 308.1.c LGSS): https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724

## Ask the client first

- Where are you resident: common territory, Canarias, Ceuta or Melilla, or a foral territory? The indirect tax, the credit and the scale all change.
- Is the activity professional (section two of the IAE) or business (section one)? Only the first is withheld on.
- Were you registered in RETA at any time in the last three years, and did you use the reduced starting contribution then?
- Are you a partner or director of a company, or a family member of an autónomo? Each changes the floor, the generic deduction and the reduced contribution.
- Do you work from home, and what share of the square metres is used for the activity?
- Are you also an employee at the same time, and what did you and your employer pay in the year?

## When to refuse or refer

- Any figure for a Basque or Navarrese resident. Their income tax is foral law.
- Any autonomous community deduction, or the community half of the scale. No national page carries them.
- Any IPSI rate or return for Ceuta or Melilla: those ordinances are city law.
- The reduced starting contribution amount for 2026, until a Budget Law sets it.
- Whether a sector in Ceuta or Melilla is inside the bonification list, and which months of 2026 the current wording covers.
- Whether a client is inside or outside the module method on turnover between the statutory limit and the higher one the Agencia Tributaria still publishes.
- Taxing the company itself, or the choice between staying autónomo and incorporating: `es-corporate-tax`.
- Anything with a foreign element: a client abroad, work abroad, a treaty, or a move in or out of Spain.
- A licence, a permit or a local business tax. Those are municipal law.

## Sources

- Ley 35/2006, IRPF: https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764
- RD 439/2007, Reglamento del IRPF: https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820
- Ley 37/1992, IVA: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740
- RD 1065/2007, gestión e inspección: https://www.boe.es/buscar/act.php?id=BOE-A-2007-15984
- Orden HAC/1526/2024, suppressing modelo 037: https://www.boe.es/buscar/doc.php?id=BOE-A-2025-410
- Ley 20/2007, Estatuto del trabajo autónomo: https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409
- RDLeg 8/2015, LGSS: https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724
- Real Decreto-ley 13/2022: https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482
- Orden PJC/297/2026, contributions 2026: https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296
- Seguridad Social, bases y tipos 2026: https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/CotizacionRecaudacionTrabajadores/36537
- Ley 4/2012 de Canarias, IGIC rates: https://www.boe.es/buscar/act.php?id=BOE-A-2012-9282

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

> Contributed by OpenAccountants.

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
