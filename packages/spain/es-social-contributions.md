---
name: es-social-contributions
description: Use this skill whenever asked about Spanish self-employed social contributions (cuota de autonomos / RETA). Trigger on phrases like "cuota autonomos", "RETA", "social contributions Spain", "autónomo contributions", "how much do I pay as autonomo", "tarifa plana", "cese de actividad", "regularizacion cuotas", "base de cotización", "TGSS direct debit", "cuota mensual", or any question about Spanish self-employed social security. Also trigger when classifying bank statement transactions showing TGSS direct debits, cuota autonomos debits, or Seguridad Social payments. ALWAYS read this skill before touching any Spanish social contributions work.
version: 2.0
jurisdiction: ES
tax_year: 2026
last_updated: 2026-09-26
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spanish social contributions: self-employed (RETA) and employer payroll

## Scope

This Guide covers Spanish social security contributions for tax year 2026. It deals with two groups:

- **Self-employed people (autónomos) in RETA**, the special regime for self-employed workers. It covers the income bands that set the monthly base, the rates, the reduced starting fee (tarifa plana), the yearly regularisation against actual net income, family collaborators, company members and pluriactividad.
- **Employers and employees in the Régimen General.** It covers the employer and employee rates, the minimum and maximum bases, the intergenerational equity contribution (MEI) and the solidarity contribution on pay above the maximum base.

The figures for 2026 come from [Orden PJC/297/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296), the yearly contribution order. It was published in the BOE on 31 March 2026, and its bases and rates apply "desde el 1 de enero de 2026". No 2026 State Budget Law has been approved. The 2023 budget has been rolled over, and the order says so: "se ha producido automáticamente la prórroga presupuestaria". Two things in this Guide have no 2026 figure set in law, and each is marked where it is used:

- the amount of the reduced starting fee;
- the sick-pay percentages, which come from the Social Security page on temporary incapacity, not from the order.

A short dated section gives the 2025 figures, because 2025 is being regularised during 2026 and 2027.

**Out of scope.** The following are covered elsewhere:

- income tax on the same person: es-income-tax;
- quarterly income tax instalments: es-estimated-tax;
- VAT: es-vat-return;
- the whole picture of self-employment in Spain: es-autonomous-worker.

This Guide does not cover the foral territories' own tax administrations. It also does not cover EU coordination for posted or cross-border workers. For both, see "When to refuse or refer".

## Ask the client first

- **Are you an individual autónomo, a company director or working member, or a family member who works in a relative's business?** The answer decides the generic expenses deduction (7% or 3%) and whether the group 7 minimum base applies. ([source](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724))
- **Have you been in RETA in the last two years? Have you ever had the reduced starting fee?** This decides eligibility for the fee, and whether the wait is two years or three.
- **What net income do you expect this year, and has it changed since you chose your base?** An estimate is needed to pick a band. Do not work without one.
- **Are you also an employee in the Régimen General at the same time?** That is pluriactividad, and it can open a partial refund.
- **When did you register (alta)? Was it on time? Did you choose the start date?** This changes the base for the first period and whether that period is regularised.
- **Have you received a regularisation notice? Did you pay it, or receive a refund?**
- **Do you live and work in Ceuta or Melilla? In which sector?** The reduction of the common-contingencies cuota changed on 1 October 2026.
- **For employers: how many staff do you have, on which contract type (permanent or fixed-term), and in which contribution group? Does anyone earn more than the maximum base?** These set the unemployment rate, the minimum base and the solidarity contribution.
- **Did you file an IRPF return for the year being regularised?** If not, a special rule applies (step 8 of the method below).

## The method, step by step

**Self-employed (RETA)**

1. **Classify the person** under article 305.2 of the [LGSS](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724):
   - an individual;
   - a company director or working member (letters b and e);
   - a family collaborator (letter k).
   The class decides the deduction in step 2 and the floor in step 4.
2. **Work out computable net income** under article 308.1.c:
   - Start from net income of every activity under the IRPF rules.
   - Under direct estimation, add back the person's own social security cuotas.
   - Under the module method (estimación objetiva), use the prior net income (rendimiento neto previo). For farming, forestry and livestock, use the reduced figure.
   - Company members and partners also add the work and capital income they draw from the company, as article 308.1.c lists for their letter.
   - Deduct generic expenses: 7% in general, or 3% for letters b and e. The 3% applies once the person has been registered for ninety days under one of those letters in the period being regularised. ([source](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724))
   - Divide by the months in the period to get the monthly average.
3. **Find the band.** Use the reduced or general table for 2026 (in "Figures by year"). If the monthly average is below EUR 1,166.70, use the reduced table. Otherwise use the general table. ([source](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296))
4. **Choose a base inside that band**, between its minimum and its maximum. Company members and family collaborators may not choose below the group 7 minimum of EUR 1,424.40. The exception is that they may keep a provisional base carried from 2025 (see the boundary table). ([source](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724))
5. **Apply the RETA rates to the base.** Show each rate on its own line. Do not quote a combined official rate.
6. **Check for a reduced fee or bonus:**
   - the tarifa plana for a first registration;
   - the family-collaborator bonus;
   - the Ceuta and Melilla reduction.
   Each has conditions and must be applied for or awarded. Read the amount from the TGSS award, not from memory.
7. **Pay and adjust during the year.**
   - The cuota is paid by direct debit within the same month. It is charged on the last working day.
   - The base can be changed six times a year, in the windows in the boundary table.
   - Re-estimate income whenever it changes.
8. **Regularise.**
   - After the IRPF return, the TGSS compares the bases paid with the actual income the tax agency sends. It regularises automatically.
   - If the base paid was below the minimum for the actual band, the difference is due by the last day of the month after notification. No interest or surcharge is added. For a large demand, the client can apply for a deferral (aplazamiento) under LGSS article 23.
   - If the base paid was above the band maximum, the TGSS refunds the difference without interest. It pays before 30 April of the year after the tax agency sends it the income. For 2025 income, sent in 2026, that means before 30 April 2027.
   - Surcharges and interest are never refunded. Debts already run up on the provisional bases stand and are not changed.
   - If no IRPF return was filed, or no activity income was declared under direct estimation, the final base is the general-regime group 7 minimum (EUR 1,424.40). This applies from 2026; for 2025, see the previous-year section. ([source](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724))
9. **Book it in IRPF.** The regularisation is booked in the year it is settled, not the year it relates to (see the filing section).

**Employers (Régimen General)**

1. **Put each employee in a contribution group** (1 to 11). Take the monthly common-contingencies base from their pay. Keep it between the group's minimum and the EUR 5,101.20 ceiling. ([source](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296))
2. **Apply the rates**, split between employer and employee:
   - common contingencies and MEI go on the common-contingencies base;
   - unemployment (by contract type), FOGASA and training go on the accident and occupational disease base, which includes overtime (order article 33.1).
   Add the occupational accident premium, which the employer pays alone at the tariff rate for the activity.
3. **Add the solidarity contribution** on any part of pay above EUR 5,101.20 a month. ([source](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296))
4. **File through the Sistema RED** and pay within the month after the month the pay accrues (see the filing section).

## Figures by year: 2026

All 2026 figures in this section come from [Orden PJC/297/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296) unless a row says otherwise.

### RETA: tables of bases by monthly net income, 2026 (order, article 18) ([Orden PJC/297/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296))

Each table is numbered from band 1, as the order numbers it. Older working papers numbered the general table from band 4, so re-read any band number taken from them.

**Reduced table**

| Band, monthly net income | Minimum base | Maximum base |
| --- | --- | --- |
| 1: EUR 670 or less | EUR 653.59 | EUR 718.94 |
| 2: over EUR 670, up to EUR 900 | EUR 718.95 | EUR 900.00 |
| 3: over EUR 900, below EUR 1,166.70 | EUR 849.67 | EUR 1,166.70 |

**General table**

| Band, monthly net income | Minimum base | Maximum base |
| --- | --- | --- |
| 1: EUR 1,166.70 up to EUR 1,300.00 | EUR 950.98 | EUR 1,300.00 |
| 2: over EUR 1,300.00 up to EUR 1,500.00 | EUR 960.78 | EUR 1,500.00 |
| 3: over EUR 1,500.00 up to EUR 1,700.00 | EUR 960.78 | EUR 1,700.00 |
| 4: over EUR 1,700.00 up to EUR 1,850.00 | EUR 1,143.79 | EUR 1,850.00 |
| 5: over EUR 1,850.00 up to EUR 2,030.00 | EUR 1,209.15 | EUR 2,030.00 |
| 6: over EUR 2,030.00 up to EUR 2,330.00 | EUR 1,274.51 | EUR 2,330.00 |
| 7: over EUR 2,330.00 up to EUR 2,760.00 | EUR 1,356.21 | EUR 2,760.00 |
| 8: over EUR 2,760.00 up to EUR 3,190.00 | EUR 1,437.91 | EUR 3,190.00 |
| 9: over EUR 3,190.00 up to EUR 3,620.00 | EUR 1,519.61 | EUR 3,620.00 |
| 10: over EUR 3,620.00 up to EUR 4,050.00 | EUR 1,601.31 | EUR 4,050.00 |
| 11: over EUR 4,050.00 up to EUR 6,000 | EUR 1,732.03 | EUR 5,101.20 |
| 12: over EUR 6,000 | EUR 1,928.10 | EUR 5,101.20 |

- The upper figure of each band is included in that band. EUR 1,166.70 exactly is general band 1, not reduced band 3.
- No RETA base may exceed EUR 5,101.20 a month. The lowest base in either table is EUR 653.59.
- The law pegs the edge of the reduced table to the general-regime minimum base, but the order fixes it at EUR 1,166.70. Use the order's figure, not the group 7 minimum.
- All minimum bases are the same as in 2025. Only the top two maximum bases moved, to the new ceiling.

### RETA: rates, 2026 (order, article 18) ([Orden PJC/297/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296))

There is no employer share in RETA. The self-employed person pays all of each rate.

| Concept | Rate |
| --- | --- |
| Common contingencies (contingencias comunes) | 28.30% |
| Occupational contingencies (accident at work and occupational disease) | 1.30% |
| of which temporary incapacity | 0.66% |
| of which permanent incapacity, death and survivors | 0.64% |
| Cessation of activity (cese de actividad) | 0.90% |
| Cessation of activity, agrarian special system | 2.20% |
| Vocational training (formación profesional) | 0.10% |
| MEI (intergenerational equity) | 0.90% |
| Extra charge where occupational cover is not taken | 0.10% |

No official page prints a combined RETA percentage, so this Guide gives none. Read the total from the TGSS receipt. Where temporary incapacity is covered in another regime and the person does not opt in here, the order applies a reduction coefficient to the common-contingencies cuota.

### RETA: reduced starting fee (tarifa plana) ([Real Decreto-ley 13/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482))

| What | Amount | Source |
| --- | --- | --- |
| Monthly reduced fee set by law, 2023 to 2025 only | EUR 80 | [Real Decreto-ley 13/2022, transitional provision 5](https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482): "será de 80 euros mensuales" |
| From month twenty-five, in the article 38 ter(10) cases | EUR 160 | same: "de 160 euros a partir del mes vigesimoquinto" |
| 2026 amount | Not set in law | see below |

**The 2026 position.** Transitional provision 5 of Real Decreto-ley 13/2022 fixed the fee for 2023 to 2025. It leaves later years to each State Budget Law: "A partir del año 2026, el importe de dichas cuotas será fijado por la Ley de Presupuestos Generales del Estado de cada ejercicio". Article 38 ter(1) of [Ley 20/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409) says the same. No 2026 Budget Law has been approved, and the 2026 order does not mention the reduced fee. The TGSS Importass guide still shows EUR 80 a month plus MEI at 0.9%, for a total of EUR 88.64. That total does not reconcile with the base the guide describes, so do not certify it. Read the amount from the TGSS award and the receipt, and name that document as the source.

### Régimen General: minimum and maximum bases, 2026 (order, articles 2 and 3) ([Orden PJC/297/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296))

| Group | Categories | Minimum | Maximum |
| --- | --- | --- | --- |
| 1 | Engineers and graduates, senior management | EUR 1,989.30 a month | EUR 5,101.20 a month |
| 2 | Technical engineers, experts and qualified assistants | EUR 1,649.70 a month | EUR 5,101.20 a month |
| 3 | Administrative and workshop heads | EUR 1,435.20 a month | EUR 5,101.20 a month |
| 4 to 7 | Unqualified assistants, administrative officers, junior staff, administrative assistants | EUR 1,424.40 a month | EUR 5,101.20 a month |
| 8 to 11 | First, second and third class tradespeople, specialists, labourers, workers under eighteen | EUR 47.48 a day | EUR 170.04 a day |

- The ceiling on the base (tope máximo) is EUR 5,101.20 a month from 1 January 2026.
- The floor for accident and occupational disease contributions is the minimum wage plus one sixth, and never below EUR 1,424.40.

### Régimen General: rates, 2026 (order, articles 4, 16 and 33) ([Orden PJC/297/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296))

| Concept | Total | Employer | Employee |
| --- | --- | --- | --- |
| Common contingencies | 28.30% | 23.60% | 4.70% |
| Unemployment, permanent contracts (including part-time, fixed-discontinuous, and workers with a disability of at least 33%) | 7.05% | 5.5% | 1.55% |
| Unemployment, fixed-term contracts | 8.30% | 6.70% | 1.60% |
| FOGASA (wage guarantee fund) | 0.20% | 0.20% | none |
| Vocational training | 0.70% | 0.60% | 0.10% |
| MEI (intergenerational equity) | 0.90% | 0.75% | 0.15% |
| Accident at work and occupational disease | tariff by activity (LGSS, additional provision 61) | all | none |

- Several contract types count as permanent for the unemployment rate, including replacement (sustitución) and relief (relevo) contracts. A fixed-term contract converted to permanent moves to the permanent rate from the date of conversion.
- The MEI is charged on the common-contingencies base. It cannot be reduced by any bonus or reduction (LGSS article 127 bis).
- No official page prints a combined employer percentage. The parts are given as the order prints them.

### Régimen General: solidarity contribution (cotización adicional de solidaridad), from 2025 (order, article 17) ([Orden PJC/297/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296))

The solidarity contribution is charged on the part of an employee's monthly pay above the maximum base. It applies from 1 January 2025 (LGSS article 19 bis). It covers employees only; it does not apply to RETA. The rates rise each year to 2045 under LGSS transitional provision 42. The employer and employee shares follow the same proportion as common contingencies.

| Part of monthly pay, 2026 | Total | Employer | Employee |
| --- | --- | --- | --- |
| EUR 5,101.21 to EUR 5,611.32 | 1.15% | 0.96% | 0.19% |
| EUR 5,611.33 to EUR 7,651.80 | 1.25% | 1.04% | 0.21% |
| Above EUR 7,651.80 | 1.46% | 1.22% | 0.24% |

- The three bands run from the ceiling to 10% above it, then up to 50% above it, then beyond.
- The final rates for 2045 are 5.50%, 6.00% and 7.00%.
- For artists and bullfighting professionals, the order makes the contribution final for the employer and provisional for the worker, with a year-end regularisation.

### Pluriactividad refund, 2026 (order, article 18) ([Orden PJC/297/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296))

A person who is both an employee in the Régimen General and self-employed in RETA pays in both regimes. If their combined common-contingencies contributions in the year exceed EUR 17,323.68, the TGSS refunds 50% of the excess. The refund is capped at 50% of the RETA common-contingencies cuotas paid. The TGSS pays it within four months of the regularisation, or later where the case has particular features or the worker must supply data. No application is needed.

### Surcharges for late payment (LGSS article 30) ([LGSS](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724))

These apply to RETA and to employers alike.

| Situation | Surcharge |
| --- | --- |
| Contribution documents filed on time, paid in the first calendar month after the deadline | 10% |
| Filed on time, paid from the second calendar month after the deadline | 20% |
| Not filed on time, paid before the deadline in the TGSS demand (reclamación de deuda) or assessment | 20% |
| Not filed on time, paid after that deadline | 35% |

- "Filed on time" means the duties in article 29 were met: sending the contribution data within the payment period.
- Debts other than contributions carry 20%.
- Interest (article 31) is added where the debt is still unpaid fifteen days after the enforcement order (providencia de apremio) is notified, or fifteen days after the start of the deduction procedure is communicated.

## Previous year: 2025 figures (for the 2025 regularisation) ([Orden PJC/178/2025](https://www.boe.es/buscar/act.php?id=BOE-A-2025-3780))

The 2025 regularisation is issued after the 2025 IRPF return, so it arrives in the second half of 2026 and into 2027. The figures below come from [Orden PJC/178/2025](https://www.boe.es/buscar/act.php?id=BOE-A-2025-3780).

| Item | 2025 |
| --- | --- |
| Maximum base (tope máximo), Régimen General and top RETA bands | EUR 4,909.50 a month |
| MEI in the Régimen General | 0.80% (employer 0.67%, employee 0.13%) |
| MEI in RETA | 0.80% |
| Pluriactividad threshold | EUR 16,672.66 |
| Solidarity, EUR 4,909.51 to EUR 5,400.45 | 0.92% (employer 0.77%, employee 0.15%) |
| Solidarity, EUR 5,400.46 to EUR 7,364.25 | 1% (employer 0.83%, employee 0.17%) |
| Solidarity, above EUR 7,364.25 | 1.17% (employer 0.98%, employee 0.19%) |

- The RETA minimum bases and the other rates were the same in 2025 as in 2026.
- For 2025, three groups had a floor of EUR 1,000 instead of the group 7 minimum (order 2025, article 18.4, and Real Decreto-ley 13/2022, transitional provision 7):
  - company members (art. 305.2 b and e), once the ninety days were met;
  - family collaborators (art. 305.2 k);
  - people who filed no 2025 IRPF return, or declared no activity income under direct estimation (art. 308.1.c, rule 5.ª).
  So in the 2025 regularisation, a non-filer's final base is EUR 1,000. The group 7 base of EUR 1,424.40 applies only from 2026.

**The 2026 order was retroactive.** It was published on 31 March 2026 but applies from 1 January. Its transitional provisions gave catch-up windows, and those windows have now closed:

- Differences on self-assessed contributions made from 1 January 2026 could be paid without a surcharge. The deadline was the last day of the second month after publication.
- Differences on direct-settlement assessments made from 1 February 2026 could be paid without a surcharge. The deadline was the last day of the month after the TGSS reported the updated assessments.
- RETA workers already on the maximum base could choose a higher base, effective from 1 January 2026. The deadline was the last day of the month after publication.

Look at these only if a client asks about a catch-up assessment they received in 2026.

## Boundaries and exceptions ([Orden PJC/297/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296))

| Situation | Rule | Source |
| --- | --- | --- |
| Monthly average exactly at a band's upper figure | It belongs to that band ("up to and including"). EUR 2,330.00 is general band 6, and EUR 6,000 is band 11, not 12. | [Order, art. 18](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296) |
| Company director or working member (art. 305.2 b, e) or family collaborator (art. 305.2 k) | Rule 4.ª of art. 308.1.a: the base chosen, and the final base at regularisation, may not be below the group 7 minimum (EUR 1,424.40). Ninety days registered in the year is enough for the floor to apply. They may keep during 2026 a provisional base carried from 2025 (order art. 18.4). Importass gives that base as at least EUR 1,000. | [LGSS](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724); [Importass guide](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/trabajo%2Bautonomo/guia) |
| Tarifa plana: who qualifies | First registration, or not in RETA in the two years before the date of effect. The wait is three years for anyone who has had the fee before. Relatives of an autónomo up to the second degree, by blood, marriage or adoption, who join RETA are excluded (art. 38 ter.11). It must be applied for at registration. | [Ley 20/2007, art. 38 ter](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409) |
| Tarifa plana: how long | Twelve full calendar months from the date of effect. A further twelve months if net income in that second period is below the annual minimum wage; this is applied for again before the second period. Where the second period spans two calendar years, the income test must be met in each year ("se deberá cumplir en cada uno de ellos", art. 38 ter.2). When the reduced fee ends, contributions for every contingency start on the first day of the month after it ends (art. 38 ter.8). That applies whether it ends after the first period (extension refused or not sought) or after the second. For a disability of at least 33%, or victims of gender violence or terrorism, the periods are 24 and 36 months. The right ends on deregistering from RETA during either period. | same |
| Tarifa plana: what it covers | No cessation-of-activity or training contribution is paid during it. Benefits are worked out on the general band 1 minimum. The first period is not regularised. The second period is regularised only for a year in which income exceeded the annual minimum wage. | same |
| Family collaborator bonus | A spouse, registered partner or relative up to the second degree who joins RETA, works in the activity, and has not been in RETA in the last five years. Bonus of 50% for eighteen months, then 25% for six months, of the common-contingencies cuota on the general band 1 minimum base. | [Ley 20/2007, art. 35](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409) |
| Registering part way through a month | The start date can be chosen three times a year, and those registrations run from the start day. Other registrations take effect on the first day of the month; the whole month is paid. Deregistrations work the same way. | [Importass guide](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/trabajo%2Bautonomo/guia) |
| Late registration | From the start of activity to the end of the month the registration is made, the base is the general band 1 minimum (EUR 950.98 in 2026). That period is left out of the regularisation. A late registration also loses cuota reductions and carries a penalty. | same |
| Changing the base | Six changes a year. A request made 1 Jan to end Feb takes effect 1 Mar. 1 Mar to 30 Apr: 1 May. 1 May to 30 Jun: 1 Jul. 1 Jul to 31 Aug: 1 Sep. 1 Sep to 31 Oct: 1 Nov. 1 Nov to 31 Dec: 1 Jan. A change requested during sick leave takes effect the day after discharge. | [Importass, base and income service](https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Altas,+bajas+y+modificaciones/Bajas+y+modificaciones/BCRendimientos) |
| Contributing since before 2023 on a high base | A person on a base above what their income would now give, unchanged since before 1 January 2023, may keep it during 2026 or choose a lower one. The right is lost once the base changes. There is no age-47 limit on choosing a base any more. That rule ended with the old system on 1 January 2023. | [Order, art. 18.5](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296); [Real Decreto-ley 13/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482) |
| Ceuta and Melilla | Residents working there in the listed sectors get a reduction of the common-contingencies cuota. It is 50% for cuotas accrued before 1 October 2026 and 75% from 1 October 2026 (Real Decreto-ley 22/2026, art. 36). The sector list also changed on that date: the old text excluded building construction, the new one does not mention it. Split the year at 1 October and read article 36 for each part. A decree-law must be validated by Congress, so check it has been validated. | [Real Decreto-ley 1/2023](https://www.boe.es/buscar/act.php?id=BOE-A-2023-625); [Ley 20/2007, art. 36](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409); [Real Decreto-ley 22/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-18429) |
| No IRPF return, or no income declared under direct estimation | From 2026, the final base is the group 7 minimum (EUR 1,424.40). For 2025 it is EUR 1,000; see the previous-year section. | [LGSS art. 308.1.c, rule 5.ª](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724) |
| Months left out of regularisation | Months for which a benefit was already granted, the reduced-fee first period, and a late-registration period. | same |

## Worked cases ([Orden PJC/297/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296))

These cases use made-up client figures to show the method. The rates and bases are the 2026 ones above. Do not copy a case amount into a client file.

**Case 1: individual autónomo, finding the band and the cuota lines.**

- The client's IRPF net income from the activity is EUR 30,000. Their own RETA cuotas of EUR 4,800 were deducted in reaching it.
- Add back the cuotas: EUR 34,800.
- Deduct 7%: EUR 2,436.00, leaving EUR 32,364.00.
- Monthly average: EUR 2,697.00. That falls in general band 7 (over EUR 2,330.00, up to EUR 2,760.00).
- The client chooses the band minimum, EUR 1,356.21. The monthly lines are:
  - common contingencies at 28.30%: EUR 383.81;
  - occupational contingencies at 1.30%: EUR 17.63;
  - cessation at 0.90%: EUR 12.21;
  - training at 0.10%: EUR 1.36;
  - MEI at 0.90%: EUR 12.21.
- The rounded lines add up to EUR 427.22. That is the sum of this client's lines, not an official combined rate. Check it against the TGSS receipt.

**Case 2: base too low, regularisation demand.**

- The client paid all 2026 on EUR 960.78, the band 2 minimum.
- Their final income falls in general band 7, whose minimum is EUR 1,356.21.
- The base shortfall is EUR 395.43 a month, or EUR 4,745.16 for the year.
- The TGSS applies each rate to that difference. The common-contingencies part alone is EUR 1,342.88.
- The demand is payable by the last day of the month after notification, with no surcharge or interest.
- If the final income had fallen in band 2 or 3, where EUR 960.78 is inside the range, the base would stand and nothing would change.

**Case 3: employer, one permanent employee in group 1 earning EUR 6,000 a month.**

- The base is capped at EUR 5,101.20.
- Employer lines:
  - common contingencies at 23.60%: EUR 1,203.88;
  - unemployment at 5.5%: EUR 280.57;
  - FOGASA at 0.20%: EUR 10.20;
  - training at 0.60%: EUR 30.61;
  - MEI at 0.75%: EUR 38.26;
  - plus the accident premium for the activity.
- Employee lines:
  - common contingencies at 4.70%: EUR 239.76;
  - unemployment at 1.55%: EUR 79.07;
  - training at 0.10%: EUR 5.10;
  - MEI at 0.15%: EUR 7.65.
- Solidarity is due on the EUR 898.80 above the ceiling:
  - EUR 510.12 is in the first band. The employer pays EUR 4.90 and the employee EUR 0.97.
  - EUR 388.68 is in the second band. The employer pays EUR 4.04 and the employee EUR 0.82.

**Case 4: pluriactividad refund.**

- In 2026 a client's common-contingencies contributions across both regimes total EUR 20,000. Of that, EUR 3,500 was RETA common-contingencies cuotas.
- The excess over EUR 17,323.68 is EUR 2,676.32.
- Half of it is EUR 1,338.16. The cap is half the RETA cuotas, EUR 1,750.
- The refund is EUR 1,338.16, paid within four months of the regularisation.

**Case 5: family collaborator bonus.**

- A client's son joins RETA to work in the family shop. He has never been registered.
- The bonus is worked out on the common-contingencies cuota at the general band 1 minimum: 28.30% of EUR 950.98, which is EUR 269.13.
- The reduction is EUR 134.56 a month for eighteen months, then EUR 67.28 a month for six months.
- His own base still cannot be below the group 7 minimum at regularisation. The tarifa plana is not available to him, because he is a first-degree relative.

**Case 6: bank statement only.**

- A client sends only statements showing an identical small TGSS debit each month.
- Do not infer a band or assume a reduced fee.
- Ask for the TGSS contribution base report (Informe de bases de cotización) and any award notice.
- Flag the file: "RETA base not read from a TGSS document."

## When to refuse or refer

- **The exact 2026 reduced-fee amount.** No law sets it. Give the conditions and periods, and read the amount from the TGSS award.
- **Posted or cross-border workers**, or anyone contributing in two EU states. EU coordination rules apply. Escalate.
- **Disability-specific contribution rules**, beyond the longer tarifa plana periods. These need a case-specific TGSS assessment.
- **A particular mutual insurer's (mutua) benefits, cover or claim.** Refer to that mutua.
- **The employer's accident premium for a given activity.** This is the tariff in LGSS additional provision 61. It needs the activity code (CNAE) and the occupation.
- **The foral territories** (Álava, Bizkaia, Gipuzkoa, Navarra) for the income tax side. Social security itself is state-wide, but the IRPF figures used for regularisation come from those administrations.
- **Ceuta.** The extraordinary cessation benefit and other support measures in Real Decreto-ley 22/2026 are outside this Guide.
- **Whether a late-payment surcharge is deductible in IRPF.** No official page read for this Guide answers it. Keep surcharges and interest out of the deductible expense until an accountant rules on it.
- **Any request for a combined RETA percentage, an "effective rate", or a cuota without a named base.** Refuse the shortcut and ask for the base.
- **Pluriactividad planning, special regimes (sea workers, agrarian, domestic employees, artists) and bonus schemes for hiring.** Refer to a reviewer.

## Filing and payment ([Reglamento General de Recaudación](https://www.boe.es/buscar/act.php?id=BOE-A-2004-11836))

**Self-employed (RETA)**

- **When.** Cuotas are paid "dentro del mismo mes al que aquéllas correspondan": within the same month they relate to ([Reglamento General de Recaudación, art. 56.1.b](https://www.boe.es/buscar/act.php?id=BOE-A-2004-11836)).
- **How.** By direct debit through a bank or other collaborating institution, charged on the last working day of the month ([Importass guide](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/trabajo%2Bautonomo/guia)).
- **Quarterly option.** The Importass guide describes a quarterly option chosen at registration: January to March is paid in April, April to June in July, July to September in October, and October to December the next January. It appears in the guide's paragraph on self-employed artists. Confirm with the TGSS that it is open to the client's activity before relying on it.
- **Electronic channel.** RETA workers must deal with the TGSS electronically. They can use the Sistema RED through an authorised representative (for example a gestoría), or the Social Security electronic office (SEDESS) and Importass ([Orden ESS/484/2013, art. 2.2.b](https://www.boe.es/buscar/act.php?id=BOE-A-2013-3362)).
- **Registration, base changes, reduced fee.** All are done through Importass, including the base and income service.

**Employers (Régimen General)**

- **Sistema RED is compulsory.** Every employer in the Régimen General must join it, "con independencia del número de trabajadores". The exceptions in article 2.3.a are household employers of domestic staff and bullfighting professionals ([Orden ESS/484/2013, art. 2.2.a](https://www.boe.es/buscar/act.php?id=BOE-A-2013-3362)).
- **Direct settlement.** Contributions are calculated by the TGSS under the direct settlement system (Sistema de Liquidación Directa). The employer or its authorised RED user sends the workers' data and receives the draft and final assessments. The files are exchanged through the TGSS's SILTRA application ([TGSS, direct settlement procedure](https://www.seg-social.es/descarga/es/196843)).
- **When.** Contributions are paid "dentro del mes siguiente al que corresponda su devengo": for example, April pay is paid by 31 May ([Reglamento General de Recaudación, art. 56.1](https://www.boe.es/buscar/act.php?id=BOE-A-2004-11836)).
- **How.** By direct debit or bank charge through the collaborating institutions. Late payment brings the article 30 surcharges.
- **Filing the data on time matters.** Filing within the period and paying late costs 10% or 20%. Not filing on time costs 20% or 35%.

**Booking the RETA regularisation in IRPF (return for 2025, filed in 2026)**

- RETA cuotas for the activity are a deductible expense of the activity.
- The regularisation is booked in the year it is settled. For the 2025 return, that means the regularisation made in 2025 for 2024:
  - an amount paid is a higher social security expense (box 0196);
  - an amount refunded reduces that expense (box 0197);
  - any refund above the cuotas paid that year is extra income (box 0178).
- Source: [Agencia Tributaria, IRPF 2025 manual](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-ayuda-presentacion/irpf-2025/7-cumplimentacion-irpf/7_4-rendimientos-actividades-economicas/7_4_2-regimen-estimacion-directa/7_4_2_3-gastos-fiscalmente-deducibles/cotizaciones-reta.html).
- Keep principal, surcharges and interest on separate lines.

## Benefits the contributions pay for ([temporary incapacity](https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/PrestacionesPensionesTrabajadores/10952/28362/28365))

**Temporary incapacity (sick leave).** These percentages are from the [Social Security page on temporary incapacity](https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/PrestacionesPensionesTrabajadores/10952/28362/28365), not from the order.

- **Common illness or non-work accident:**
  - The subsidy is paid at 60% of the regulatory base from day 4 to day 20, then 75% from day 21.
  - The self-employed person must be registered and up to date with cuotas.
  - For common illness, the general regime requires 180 days of contributions in the five years before the leave ([LGSS article 172](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724)). Confirm with the mutua how this applies to the self-employed person; this Guide does not restate the RETA provision.
  - Article 321 of the LGSS confirms the self-employed subsidy starts on the fourth day of leave, unless the leave comes from a work accident or occupational disease.
- **Accident at work or occupational disease:** 75% from the day after the sick note, with no minimum contribution period.
- **Regulatory base:** the common-contingencies base of the month before the leave. A higher base gives a higher benefit.
- **Cuotas during long leave:** once sixty days have passed from the sick note, the mutua (or the state employment service) pays the cuotas for every contingency ([order 2026, article 37.4](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296)). A base change asked for during the leave takes effect the day after discharge.

**Cessation of activity (cese de actividad).** Under LGSS articles 338 and 339:

- The regulatory base is the average of the bases in the twelve continuous months before the cessation.
- The benefit is 70% of the regulatory base, or 50% in the partial cases in article 331.1.a.
- It needs at least twelve months of cessation contributions in the last twenty-four.
- Duration runs from four months (for twelve to seventeen months contributed) up to twenty-four months (for forty-eight or more).
- A new award can be claimed only once eighteen months have passed since the last one was recognised (article 338.3).
- The maximum and minimum amounts are set as percentages of the IPREM (indicador público de rentas de efectos múltiples) in article 339.3, and they depend on dependent children.
- Giving up the activity voluntarily, where there is no legal cause, does not qualify.

## Reading bank statements

| Pattern on the statement | What it is |
| --- | --- |
| TGSS, TESORERIA GENERAL, SEGURIDAD SOCIAL, CUOTA AUTONOMOS, RETA, on the last working day | Monthly RETA cuota. A deductible expense. |
| TGSS REGULARIZACION, COMPLEMENTO CUOTAS | Regularisation demand. A higher expense in the year paid. |
| TGSS DEVOLUCION, TGSS REINTEGRO (credit) | Regularisation refund or pluriactividad refund. It reduces the expense; any excess is income. |
| Small identical monthly TGSS debit | Possibly a reduced fee. Confirm on the award; do not assume the amount. |
| TGSS REGIMEN GENERAL, TC1/TC2 or RLC references | Employer contributions for staff, not the owner's own RETA. |
| AEAT, AGENCIA TRIBUTARIA, HACIENDA | Tax (IRPF instalments, VAT), not social security. |

Do not read the band off the debit: a reduced fee, a bonus or a mid-month registration breaks the pattern.

## Completion checklist ([Orden PJC/297/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296))

- [ ] Class under article 305.2 confirmed (individual, company member, family collaborator).
- [ ] Net income worked out under article 308.1.c: owner's cuotas added back, 7% or 3% deducted, monthly average found.
- [ ] Band and table (reduced or general) identified. Base chosen inside it, and not below EUR 1,424.40 for company members and family collaborators.
- [ ] Each 2026 rate applied as its own line. No combined rate quoted.
- [ ] Tarifa plana, family bonus or Ceuta and Melilla reduction checked against the TGSS award. No 2026 reduced-fee amount stated from memory.
- [ ] Registration date and any late registration checked.
- [ ] Base-change window noted for any change.
- [ ] Regularisation checked: IRPF return filed, notice read, payment due by the end of the following month or refund expected before 30 April.
- [ ] Pluriactividad checked against EUR 17,323.68 (2026) or EUR 16,672.66 (2025).
- [ ] For employers: group, contract type, base between the group minimum and EUR 5,101.20, solidarity on pay above the ceiling, RED filing, and payment within the following month.
- [ ] Late payments separated into principal, surcharge and interest.
- [ ] IRPF boxes 0196, 0197 and 0178 used for a regularisation settled in the year.

This Guide is general information on Spanish social security contributions. It is not advice for a particular person. Before a figure is filed or paid, a qualified professional (asesor fiscal, graduado social or gestor administrativo) should check it against the client's TGSS documents.

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
