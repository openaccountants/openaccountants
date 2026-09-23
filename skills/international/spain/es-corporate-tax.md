---
name: es-corporate-tax
description: Use this skill whenever asked about Spanish corporate income tax (Impuesto sobre Sociedades, IS), Modelo 200, Modelo 202 (pagos fraccionados), corporate tax rates in Spain, SL tax obligations, company formation tax, deducciones empresariales, bases imponibles negativas (BINs), reserva de capitalizacion, reserva de nivelacion, or foral corporate tax. Trigger on phrases like "Impuesto de Sociedades", "Modelo 200", "Modelo 202", "IS Spain", "corporate tax Spain", "tipo gravamen sociedades", "SL taxes", "nueva creacion", "empresa reducida dimension", "microempresa fiscal", "BINs", "compensacion perdidas sociedad", "pago fraccionado empresa", "ZEC Canarias", "bonificacion Ceuta Melilla sociedades", "I+D deduccion sociedades", "donativos sociedad", "resultado contable", or any question about computing or filing corporate income tax in Spain. ALWAYS read this skill before touching any Spanish corporate tax work.
version: 1.0
jurisdiction: ES
tax_year: 2026
last_updated: 2026-09-23
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Corporate income tax in Spain (Impuesto sobre Sociedades)

How a Spanish company works out and files its corporate income tax: who is liable, the rate for a period beginning in 2026, the taxable base built from accounting profit, the reserves, loss relief, amortisation, the participation exemption, the minimum tax, withholding, the instalments on modelo 202 and the annual return on modelo 200. Figures are for tax year 2026. The rates for a period beginning in 2026 come from the consolidated text of Ley 27/2014, whose disposición transitoria 44 sets them year by year. Two Agencia Tributaria pages used here carry an earlier year in their title: the table of rates in force sits in the Manual práctico de Sociedades 2025 and prints the 2025 rates, so it is used only for the micro company turnover test, and the modelo 202 instructions are headed "2025 y siguientes", so they apply to 2026 as well.

## Spain Corporate Income Tax (Impuesto sobre Sociedades) Guide v1.0

> **Based on work by Nambu89 (Impuestify)** and **Pau March (larenta)**, licensed under MIT. Adapted for the OpenAccountants format. The two source links were on a code hosting site, which is not an official source, so the links are not reproduced here.

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | Spain (Estado Español) |
| Tax | Impuesto sobre Sociedades (IS) |
| Currency | EUR only |
| Who is liable | Legal persons resident in Spain, except civil-law partnerships with no commercial object, plus the funds and entities listed in art. 7 of Ley 27/2014. See Section 2 |
| Fiscal year | The company's own accounting period, which may differ from the calendar year and may not exceed twelve months |
| Primary legislation | Ley 27/2014 (LIS), as amended by Ley 7/2024 |
| Base | Accounting profit under the Código de Comercio, corrected by the rules of Ley 27/2014 (art. 10.3) |
| Tax authority | Agencia Tributaria for common territory; the Haciendas Forales for Álava, Bizkaia, Gipuzkoa and Navarra |
| Filing form | Modelo 200 (annual) |
| Instalments | Modelo 202 (pagos fraccionados) |
| Filing deadline | The 25 calendar days following the 6 months after the end of the period, so 25 July for a calendar year |
| Modelo 202 deadlines | The first 20 calendar days of April, October and December |
| Rates | See the rate tables in Section 2 |

## Section 2: Tax Rates (Tipos de Gravamen) 2026

Who is liable: art. 7 of Ley 27/2014 makes every legal person resident in Spain a taxpayer, apart from civil-law partnerships with no commercial object, and adds investment funds, temporary business unions, venture capital funds, pension funds, mortgage market regulation funds, securitisation funds and similar vehicles. A company is resident if it was incorporated under Spanish law, has its registered office in Spain, or has its effective place of management in Spain. Art. 8.1 sets that test.

### Common Territory (Territorio Común): Ley 7/2024

The rates in the body of art. 29.1 are the final ones. They do not apply yet. For a period beginning in 2026 the rates are the ones in disposición transitoria 44.2, in the first table below.

**Rates for a period beginning in 2026**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| General rate | 25% | Art. 29.1: "El tipo general de gravamen para los contribuyentes de este Impuesto será el 25 por ciento" |
| Micro company, part of the base in the band below | 19% | DT 44.2.a: "Por la parte de base imponible comprendida entre 0 y 50.000 euros, al tipo del 19 por ciento" |
| Micro company, rest of the base | 21% | DT 44.2.a: "Por la parte de base imponible restante, al tipo del 21 por ciento" |
| Band of the base that takes the lower micro rate | EUR 50,000 | Art. 29.1: "Por la parte de base imponible comprendida entre 0 y 50.000 euros" |
| Small company meeting art. 101 | 23% | DT 44.2.b: "Las entidades que cumplan las previsiones previstas en el artículo 101 de esta ley tributarán al 23 %" |
| Newly created company, first period with a positive base and the next one | 15% | Art. 29.1: "tributarán, en el primer período impositivo en que la base imponible resulte positiva y en el siguiente, al tipo del 15 por ciento" |
| Credit institutions, and hydrocarbon exploration and extraction | 30% | Art. 29.6: "Tributarán al tipo del 30 por ciento las entidades de crédito" |
| Entities under the regime of Ley 49/2002 | 10% | Art. 29.3: "Tributarán al 10 por ciento las entidades a las que sea de aplicación el régimen fiscal establecido en la Ley 49/2002" |

The staging is settled for 2026 on this page. Disposición transitoria 44 was added by Ley 7/2024 and the consolidated text carries no note leaving it without effect. The band is scaled down where the period is shorter than a year, in proportion to its days over 365. The micro rates, the small company rate and the new company rate are all shut out where the company is a patrimonial entity within art. 5.2. A newly created company takes the new company rate in its first period with a positive base and the one after, unless another rate in the same article is lower for it. Art. 29.1 says so in those terms, so compare the new company row with the micro row and take the lower.

**Which company counts as a micro company**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/manual-sociedades-2025/capitulo-06-liquidacion-is-determinacion-tributaria/cuota-integra-casilla-00562/tipo-gravamen/tipos-gravamen-vigentes.html |
| Net turnover of the immediately preceding period below which the micro rates apply | EUR 1,000,000 | The rate table on this page states the test as "INCN < 1.000.000" |

The statute itself writes this figure in words, as one million euros. The turnover is measured across the whole group where the company belongs to one, under art. 101.2 and 101.3. A small company under art. 101 is one whose net turnover in the immediately preceding period was below ten million euros, again measured group wide, and again shut out for a patrimonial entity. Those two turnover figures are written in words in the statute.

### ERD Transitional Calendar (Ley 7/2024)

**Rate for a small company, period by period**

| Period begins in | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| 2025 | 24% | DT 44.1.b: "tributarán al 24 %, salvo que deban tributar a un tipo diferente del general" |
| 2026 | 23% | DT 44.2.b: "Las entidades que cumplan las previsiones previstas en el artículo 101 de esta ley tributarán al 23 %" |
| 2027 | 22% | DT 44.3: "las entidades que cumplan las previsiones previstas en el artículo 101 de esta ley tributarán al 22 %" |
| 2028 | 21% | DT 44.4: "las entidades que cumplan las previsiones previstas en el artículo 101 de esta ley tributarán al 21 %" |
| 2029 and later | 20% | Art. 29.1: "las entidades que cumplan las previsiones previstas en el artículo 101 de esta ley tributarán al tipo del 20 por ciento" |

**Micro company rates, period by period**

| Period begins in | Rate on the first band | Rate on the rest | Note |
| --- | --- | --- | --- |
| Source | all figures below | see the note column | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| 2025 | 21% | 22% | DT 44.1.a: "al tipo del 21 por ciento" and "al tipo del 22 por ciento" |
| 2026 | 19% | 21% | DT 44.2.a: "al tipo del 19 por ciento" and "al tipo del 21 por ciento" |
| 2027 and later | 17% | 20% | Art. 29.1: "al tipo del 17 por ciento" and "al tipo del 20 por ciento" |

### Foral Territories

Álava, Bizkaia, Gipuzkoa and Navarra each charge their own corporate tax under their own norma foral or ley foral, with their own rates, their own reliefs and their own forms. A company taxed under one of those regimes is outside this Guide. The old rate table here has been removed because none of those rates was proved on an official page in this pass. Read the rules on the territory's own site: https://www.bizkaia.eus and https://www.araba.eus and https://www.gipuzkoa.eus and https://www.navarra.es

### Special Regimes

**Special regimes**

| Regime | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| Protected cooperatives, on cooperative results | The general rates less three percentage points, with the result capped at 20% | Art. 29.2: "minorar en tres puntos porcentuales los tipos de gravamen previstos en el apartado anterior, siempre que el tipo resultante no supere el 20 por ciento" |
| Credit cooperatives and rural savings banks, on extra cooperative results | 30% | Art. 29.2: "excepto por lo que se refiere a los resultados extracooperativos, que tributarán al tipo del 30 por ciento" |
| Collective investment vehicles within art. 29.4 | 1% | Art. 29.4: "Tributarán al tipo del 1 por ciento" |
| Income earned in Ceuta or Melilla | A bonificación of the share of the gross tax: see the table in Section 4.5 | Art. 33 |

The Zona Especial Canaria rate is in Section 7. The Canary Islands also have a reserve for investment (Reserva para Inversiones en Canarias) under art. 27 of Ley 19/1994, which reduces the base; it is not covered here. See https://www.gobiernodecanarias.org

## Section 3: Liquidation Pipeline (Modelo 200)

The computation follows this order.

~~~
1. Resultado contable (accounting profit under the Codigo de Comercio)
   + Ajustes positivos (non-deductible expenses, amortisation differences)
   - Ajustes negativos (exempt income, timing differences)
   = Base imponible previa
   - Reserva de capitalizacion (art. 25, Section 4.1, capped on the base imponible previa)
   - Compensacion de bases imponibles negativas (art. 26, Section 4.2, limited on the base imponible previa)
   - Reserva para Inversiones en Canarias where it applies
   = Base imponible (it cannot go below zero)
   - Reserva de nivelacion (art. 105, small companies only, Section 4.3)
   x Tipo de gravamen (the rate tables in Section 2)
   = Cuota integra
   - Deducciones (research and development, innovation, donations, employment, film)
   - Bonificaciones (Ceuta and Melilla, cooperatives)
   = Cuota liquida, subject to the minimum in Section 4.6
   - Retenciones e ingresos a cuenta (Section 5)
   - Pagos fraccionados already paid on modelo 202
   = Resultado de la liquidacion (to pay or to refund)
~~~

Art. 10.3 is the rule that makes this work: in direct assessment the base is the accounting profit determined under the Código de Comercio, corrected by the rules of the tax law. Everything in the pipeline above between the accounting profit and the base is one of those corrections. See https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328

## Section 4: Key Computations

### 4.1 Reserva de Capitalización (Art. 25 LIS)

**Capitalisation reserve**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| Reduction of the base, as a share of the increase in own funds | 20% | Art. 25.1: "tendrán derecho a una reducción en la base imponible del 20 por ciento del importe del incremento de sus fondos propios" |
| Reduction where the average headcount rose by at least 2% and not more than 5% | 23% | Art. 25.1: "del 23 por ciento del importe del incremento de los fondos propios, siempre que la plantilla media total del contribuyente" |
| Headcount increase band for the 23% rate | at least 2% and not more than 5% | Art. 25.1: "en un mínimo de un 2 por ciento sin superar un 5 por ciento" |
| Reduction where the headcount increase is between 5% and 10% | 26.5% | Art. 25.1: "el contribuyente tendrá derecho a una reducción en la base imponible del 26,5 por ciento" |
| Reduction where the headcount increase is above 10% | 30% | Art. 25.1: "Cuando el referido incremento resulte superior a un 10 por ciento, la reducción a la que tendrá derecho el contribuyente será del 30 por ciento" |
| Cap, as a share of the positive base before this reduction and before loss relief | 20% | Art. 25.1.i: "El 20 por ciento de la base imponible positiva del período impositivo previa a esta reducción" |
| Cap where net turnover in the preceding twelve months was below one million euros | 25% | Art. 25.1.ii: "El 25 por ciento de la base imponible positiva del período impositivo previa a esta reducción" |

The reduction is open only to a company that is taxed at a rate within art. 29.1 or art. 29.6. Art. 25.1 opens with that condition, so a body under art. 29.2, art. 29.3, art. 29.4, art. 29.5 or art. 29.7 does not get it. The bands are the law's own wording and they overlap at one point. An increase of exactly the figure that closes the lower band also sits inside the band above it, because the lower band is written as not going beyond that figure and the band above is written as running from it. No official page resolves the overlap. Where a headcount increase lands exactly there, take the lower reduction and put the question to the accountant rather than choosing the higher one. The increase in own funds must be held for three years, an undistributable reserve of the same amount must be booked and held for the same three years, and the headcount increase must also be held for three years. Amounts that do not fit in the base carry forward two years. Contributions by members, capital increases by set off of debts, legal and statutory reserves and the reserves booked for the levelling reserve and for the Canary investment reserve do not count as an increase in own funds.

### 4.2 Compensación de Bases Imponibles Negativas (BINs): Art. 26 LIS

**Loss relief limits**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| General limit, as a share of the base before the capitalisation reserve and before the losses | 70% | Art. 26.1: "podrán ser compensadas con las rentas positivas de los períodos impositivos siguientes con el límite del 70 por ciento" |
| Limit where net turnover in the previous twelve months was at least twenty million euros and below sixty million euros | 50% | DA 15.1: "El 50 por ciento, cuando en los referidos 12 meses el importe neto de la cifra de negocios sea al menos de 20 millones de euros" |
| Limit where net turnover in the previous twelve months was at least sixty million euros | 25% | DA 15.1: "El 25 por ciento, cuando en los referidos 12 meses el importe neto de la cifra de negocios sea al menos de 60 millones de euros" |
| Cap on the credits for international double taxation, for the same large companies, as a share of the gross tax | 50% | DA 15.2: "no podrá exceder conjuntamente del 50 por ciento de la cuota íntegra del contribuyente" |

Losses have no expiry date. Whatever the percentage limit, losses can always be used up to one million euros in the period, which the statute writes in words; that floor is scaled down for a period shorter than a year. The limit does not apply to income from a creditors' agreement, nor in the period in which the company is wound up, unless the winding up is part of a restructuring under the special regime of Chapter VII of Title VII, nor, for the first three periods with a positive base, to a newly created company within art. 29.1. The tax office may check a loss for ten years from the end of the filing period for the return that declared it. Losses cannot be used at all where the company changed hands after the loss year in the circumstances art. 26.4 lists, which turn on the buyer's earlier stake, on the company having stopped trading, on a changed line of business, on a patrimonial entity and on removal from the register of entities.

### 4.3 Reserva de Nivelación (Art. 105 LIS): ERD Only

**Levelling reserve**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| Reduction of the positive base | 10% | Art. 105.1: "podrán minorar su base imponible positiva hasta el 10 por ciento de su importe" |

Open only to a company that meets art. 101 in the period and applies the rate in the first paragraph of art. 29.1. For a period beginning in 2026 that company's rate comes from disposición transitoria 44.2.b, which is written as a speciality of art. 29.1, and no page says in terms whether the art. 105.1 condition is then met. The Agencia Tributaria still carries the levelling reserve boxes on the modelo 202 form for periods beginning in 2025 and later, under the same art. 29.1 wording. Do not rule the reserve out on the wording alone: put it to the accountant. The reduction may not exceed one million euros, which the statute writes in words, scaled down for a short period. The amount is added back to the base of the periods ending in the following five years, against a negative base as it arises, and whatever is left is added back at the end of that time. A reserve of the same amount must be booked out of the year's profit and left undistributable until the add back happens. The same amounts cannot fund both this reserve and the capitalisation reserve, nor the Canary investment reserve (art. 105.5). The reduction is taken into account when working out an instalment under art. 40.3 (art. 105.4).

### 4.4 Deducciones en Cuota

**Deductions against the gross tax**

| Deduction | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| Research and development, on the qualifying spend | 25% | Art. 35.1.c: "El 25 por ciento de los gastos efectuados en el período impositivo por este concepto" |
| Research and development, on the excess over the average of the two preceding years | 42% | Art. 35.1.c: "el 42 por ciento sobre el exceso respecto de ésta" |
| Extra deduction for qualified researchers working only on research and development | 17% | Art. 35.1.c: "se practicará una deducción adicional del 17 por ciento del importe de los gastos de personal" |
| Investment in assets used only for research and development, buildings and land excluded | 8% | Art. 35.1.c: "El 8 por ciento de las inversiones en elementos de inmovilizado material e intangible" |
| Technological innovation, on the qualifying spend | 12% | Art. 35.2.c: "El 12 por ciento de los gastos efectuados en el período impositivo por este concepto" |
| Increase in the average headcount of workers with a disability of at least 33% and under 65%, per person and year | EUR 9,000 | Art. 38.1: "Será deducible de la cuota íntegra la cantidad de 9.000 euros por cada persona/año de incremento del promedio de plantilla" |
| Increase in the average headcount of workers with a disability of 65% or more, per person and year | EUR 12,000 | Art. 38.2: "Será deducible de la cuota íntegra la cantidad de 12.000 euros por cada persona/año de incremento del promedio de plantilla" |
| Spanish film and audiovisual production, on the first million of the base | 30% | Art. 36.1.a: "Del 30 por ciento respecto del primer millón de base de la deducción" |
| Spanish film and audiovisual production, on the excess | 25% | Art. 36.1.b: "Del 25 por ciento sobre el exceso de dicho importe" |
| Joint cap on the deductions of this chapter, on the gross tax less the international double taxation credits and the bonificaciones | 25% | Art. 39.1: "no podrán exceder conjuntamente del 25 por ciento de la cuota íntegra minorada en las deducciones para evitar la doble imposición internacional y las bonificaciones" |
| Raised cap, where the art. 35 and art. 36 deductions of the period exceed the share in the row below | 50% | Art. 39.1: "el limite se elevará al 50 por ciento cuando el importe de las deducciones previstas en los artículos 35 y 36" |
| Share of the gross tax the art. 35 and art. 36 deductions must exceed for the raised cap | 10% | Art. 39.1: "exceda del 10 por ciento de la cuota íntegra, minorada en las deducciones para evitar la doble imposición internacional y las bonificaciones" |
| Discount where a company takes the research and innovation deduction outside the cap and asks for it in cash | 20% | Art. 39.2: "aplicarse con un descuento del 20 por ciento de su importe" |

The film deduction is capped at twenty million euros, and at ten million euros for each episode of a series; both figures are written in words in the statute. Unused deductions carry forward fifteen years, and eighteen years for the research and innovation deduction.

**Donations under Ley 49/2002**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2002-25039 |
| Deduction on the base of the donation | 40% | Art. 20.1: "el 40 % de la base de la deducción determinada según lo dispuesto en el artículo 18" |
| Deduction to the same body, where donations were made to it in each of the two preceding periods and neither this period's nor last period's amount was below the amount of the period before it | 50% | Art. 20.1: "el porcentaje de deducción aplicable a la base de la deducción en favor de esa misma entidad será el 50 %" |
| Cap on the base of the deduction, as a share of the taxable base of the period | 15% | Art. 20.2: "La base de esta deducción no podrá exceder del 15 % de la base imponible del período impositivo" |

Amounts above the cap carry forward ten years.

### 4.5 Bonificación Ceuta y Melilla (Art. 33 LIS)

**Ceuta and Melilla**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| Bonificación on the part of the gross tax matching income earned in Ceuta or Melilla | 60% | Art. 33.1: "Tendrá una bonificación del 60 por ciento, la parte de cuota íntegra que corresponda a las rentas obtenidas en Ceuta o Melilla" |
| Income presumed to be earned there, per full-time employee working there | EUR 60,000 | Art. 33.3: "hasta un importe de 60.000 euros por persona empleada con contrato laboral y a jornada completa" |
| Ceiling on that presumption | EUR 1,200,000 | Art. 33.3: "1.200.000 euros. En el supuesto de que se obtengan rentas superiores al citado importe" |
| Per employee figure for the first two periods after a fixed place of business is set up there | EUR 120,000 | Art. 33.3: "hasta un importe de 120.000 euros por persona empleada con contrato laboral y a jornada completa" |
| Ceiling for those first two periods | EUR 2,400,000 | Art. 33.3: "2.400.000 euros. En el supuesto de que se obtengan rentas superiores al citado importe" |

The bonificación covers a company with its tax domicile in those territories, a Spanish company operating there through a branch or establishment, and a non-resident company operating there through a permanent establishment. The income must come from an activity that closes a commercial cycle there. Above the presumed amounts the company has to show that closing of a cycle. This Guide does not state a combined rate for Ceuta or Melilla income, because no official page prints one.

### 4.6 Tributación Mínima (Art. 30 bis LIS)

**Minimum tax**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| Floor under the net tax, as a share of the taxable base | 15% | Art. 30 bis.1: "la cuota líquida no podrá ser inferior al resultado de aplicar el 15 por ciento a la base imponible" |
| Floor for a newly created company taxed at the new company rate | 10% | Art. 30 bis.1: "el porcentaje señalado en el mismo será el 10 por ciento en las entidades de nueva creación" |
| Floor for a credit institution or a hydrocarbon company within art. 29.6 | 18% | Art. 30 bis.1: "y el 18 por ciento si se trata de entidades que tributen al tipo de gravamen previsto" |
| Floor for a cooperative, as a share of its gross tax | 60% | Art. 30 bis.1: "la cuota líquida mínima no podrá ser inferior al resultado de aplicar el 60 por ciento a la cuota íntegra" |

The rule bites on a company whose net turnover was at least twenty million euros in the twelve months before the period started, which the statute writes in words, and on any company in a tax consolidation group whatever its turnover. It does not apply to companies taxed under art. 29.3, art. 29.4 or art. 29.5, nor to a listed property investment company under Ley 11/2009. For a micro company the floor is the scale multiplied by fifteen twenty-fifths, rounded up; for a small company within art. 101 it is that company's rate multiplied by fifteen twenty-fifths, rounded up. The scale and the rate to use are the ones for a period beginning in 2026 in the tables in Section 2, because disposición transitoria 44.2 states its rates as specialities of art. 29.1 and the rates printed in the body of that article are the final ones. No official page says how far that rounding up goes, to a whole percentage point or to a decimal, and the two give different answers. Put it to the accountant. The base used for the floor is adjusted for the levelling reserve and reduced by the Canary investment reserve, and a Zona Especial Canaria entity leaves the part of its base taxed at the special rate out of the calculation.

### 4.7 Amortización (Art. 12 LIS)

Amortisation is deductible where it reflects the real fall in value. The straight line table in art. 12.1.a is the safe harbour: an amount within the maximum coefficient and the maximum number of years is accepted without further proof. The other accepted methods are a constant percentage on the written down value, the sum of the digits method, an amortisation plan agreed with the tax office, and any amount the company can justify.

**Straight line table, selected rows**

| Type of asset | Maximum coefficient | Maximum years | Note |
| --- | --- | --- | --- |
| Source | all figures below | see the note column | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| General civil works | 2% | 100 | Art. 12.1.a: "Obra civil general 2% 100" |
| Industrial buildings | 3% | 68 | Art. 12.1.a: "Edificios industriales 3% 68" |
| Commercial, administrative, service and residential buildings | 2% | 100 | Art. 12.1.a: "Edificios comerciales, administrativos, de servicios y viviendas 2% 100" |
| Other installations | 10% | 20 | Art. 12.1.a: "Resto instalaciones 10% 20" |
| Machinery | 12% | 18 | Art. 12.1.a: "Maquinaria 12% 18" |
| External transport equipment | 16% | 14 | Art. 12.1.a: "Elementos de transporte externo 16% 14" |
| Lorries | 20% | 10 | Art. 12.1.a: "Autocamiones 20% 10" |
| Furniture | 10% | 20 | Art. 12.1.a: "Mobiliario 10% 20" |
| Data processing equipment | 25% | 8 | Art. 12.1.a: "Equipos para procesos de información 25% 8" |
| Computer systems and programs | 33% | 6 | Art. 12.1.a: "Sistemas y programas informáticos. 33% 6" |
| Other assets | 10% | 20 | Art. 12.1.a: "Otros elementos 10% 20" |

**Free and accelerated amortisation**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| Unit value of a new tangible asset that can be written off at once | EUR 300 | Art. 12.3.e: "cuyo valor unitario no exceda de 300 euros" |
| Ceiling on that write off for the period | EUR 25,000 | Art. 12.3.e: "hasta el límite de 25.000 euros referido al período impositivo" |
| Investment a small company may write off freely, per unit of increase in the average headcount | EUR 120,000 | Art. 102.1: "la que resulte de multiplicar la cifra de 120.000 euros por el referido incremento" |
| Bad debt provision a small company may deduct, as a share of the debtors at the end of the period | 1% | Art. 104.1: "hasta el límite del 1 por ciento sobre los deudores existentes a la conclusión del período impositivo" |

An intangible asset is written off over its useful life. Where that life cannot be estimated reliably, and for goodwill, the yearly maximum is a twentieth of the amount, which the statute writes in words. A small company within art. 101 may also amortise new tangible assets, new investment property and intangible assets at the maximum straight line coefficient multiplied by two (art. 103.1). The free amortisation tied to headcount needs the average headcount to rise in the 24 months after the asset starts being used, against the average of the previous 12 months, and to stay up for another 24 months.

### 4.8 Exención por participación (Art. 21 LIS)

**Participation exemption**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| Minimum direct or indirect holding in the capital or own funds of the other company | 5% | Art. 21.1.a: "Que el porcentaje de participación, directa o indirecta, en el capital o en los fondos propios de la entidad sea, al menos, del 5 por ciento" |
| Cut applied to the exempt amount for management expenses | 5% | Art. 21.10: "se reducirá, a efectos de la aplicación de dicha exención, en un 5 por ciento en concepto de gastos de gestión" |

Dividends and gains on selling a holding are exempt where the holding reaches the percentage in the table and has been held without a break for the year before the dividend falls due, or is held afterwards for long enough to complete that year. A non-resident subsidiary must also have borne a foreign tax of a like nature at a nominal rate of at least ten per cent, which the statute writes in words. The exempt amount is then cut by the percentage in the second row of the table. Art. 21.11 switches that cut off for a company whose net turnover in the immediately preceding period was below forty million euros, written in words in the statute, where the further conditions in that paragraph are met. This Guide does not state a net exempt percentage, because the statute does not print one.

## Section 5: Modelo 202: Pagos Fraccionados

### Two Modalities

**Instalment percentage under the art. 40.2 method**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| Percentage applied to the base, which is the gross tax of the last return whose filing period had ended, less that period's deductions, bonificaciones and amounts withheld | 18% | Art. 40.2: "La cuantía del pago fraccionado previsto en este apartado será el resultado de aplicar a la base el porcentaje del 18 por ciento" |

**When the art. 40.3 method is compulsory**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-sociedades/modelo-202-is-i_____resencia-territorio-fraccionado_/instrucciones/Instrucciones-para-2025.html |
| Net turnover of the twelve months before the period starts above which the art. 40.3 method is compulsory | EUR 6,000,000 | Instructions: "Importe neto de la cifra de negocios de los doce meses anteriores a la fecha de inicio del periodo impositivo es superior a 6.000.000 euros" |

Under art. 40.2, the default, the base is the gross tax of the last period whose filing period had closed on the first day of the payment window, less the deductions, the bonificaciones and the amounts already withheld for that period, and the percentage in the table is applied to it.

Under art. 40.3 the base is the actual taxable base of the first 3, 9 or 11 months of the calendar year, worked out under the ordinary rules. The percentage is five sevenths of the company's rate, rounded down, where net turnover in the previous twelve months was under ten million euros, and nineteen twentieths of the rate, rounded up, where it was at least ten million euros. The law writes those fractions and those turnover figures in words. This Guide does not print the resulting percentage for any rate, because the official pages do not print it either: work it out from the company's own rate. The art. 40.3 method is optional for a company below the turnover in the table, chosen on a censal return in February, and binding until it is withdrawn the same way. It is compulsory above that turnover, and then modelo 202 must be filed even when nothing is due.

### Calendar

**Calendar**

| Period | Deadline |
| --- | --- |
| 1/P | The first 20 calendar days of April |
| 2/P | The first 20 calendar days of October |
| 3/P | The first 20 calendar days of December |

Art. 40.1 sets those three windows: see https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 A company taxed under Navarra's rules marks 2P as the period key, and one taxed under Gipuzkoa, Bizkaia or Álava marks 0A.

### Pago Fraccionado Mínimo (DA 14ª LIS)

**Minimum instalment for large companies**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-sociedades/modelo-202-is-i_____resencia-territorio-fraccionado_/instrucciones/Instrucciones-para-2025.html |
| Floor under the amount payable, as a share of the positive profit and loss result for the 3, 9 or 11 months | 23% | Instructions: "la cantidad a ingresar no podrá ser inferior, en ningún caso, al 23%" |
| Floor for a credit institution or hydrocarbon company within art. 29.6 | 25% | Instructions: "25% para contribuyentes a los que resulte de aplicación el tipo de gravamen previsto en el primer párrafo del apartado 6 del artículo 29" |

The floor applies only under the art. 40.3 method, and only to a company whose net turnover in the twelve months before the period started was at least ten million euros, which the statute writes in words. The decree that first introduced this floor was annulled by the Constitutional Court in 2020, with the effects set out in the sixth ground of that judgment. Parliament had already amended the provision twice by Act, both times in 2018. Why the floor survives the judgment is not stated on any official page read for this Guide. What those pages do show is that the provision still stands in the consolidated law and that the Agencia Tributaria still sets the floor out in the modelo 202 instructions for periods beginning in 2025 and later. A company filing for a period beginning in 2026 applies the floor on that footing, and the figures here come from the Agencia Tributaria page rather than from the statute for that reason. Put the point to the accountant. The result used is the accounting one for the period, reduced only by the instalments already paid for the same period. Companies within art. 29.3, art. 29.4 and art. 29.5, listed property investment companies and venture capital entities are outside it.

### Retenciones e ingresos a cuenta (Art. 128 LIS)

**Withholding rates**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| General withholding on income subject to this tax | 19% | Art. 128.6.a: "Con carácter general, el 19 por ciento" |
| Income from licensing image rights | 24% | Art. 128.6.b: "el 24 por ciento" |
| Lottery and betting prizes that are taxed under the special charge | 20% | Art. 128.6.c: "el 20 por ciento" |

Whoever pays income subject to this tax withholds and pays it over, and files a return for the amounts withheld plus an annual summary, even when nothing was withheld. Rent of urban property in Ceuta or Melilla paid to a company based or operating there takes the general rate divided by two. There is no withholding on dividends inside a tax consolidation group, on dividends that qualify for the exemption in art. 21.1, or on the other income listed in art. 128.4. Amounts withheld are deducted from the tax on modelo 200.

## Section 6: Non-Deductible Expenses (Gastos No Deducibles)

**Non-deductible expenses and the interest limit**

| Expense | Article | Treatment |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| Payments that are a return on own funds, including participating loans inside a group | Art. 15.a | Never deductible |
| The charge for this tax and for the complementary tax in the accounts | Art. 15.b | Never deductible, and the credit side is not income |
| Criminal and administrative fines and penalties, enforcement period surcharges, and the surcharge for filing late without a demand | Art. 15.c | Never deductible |
| Gambling losses | Art. 15.d | Never deductible |
| Donations and gratuitous payments | Art. 15.e | Not deductible, except client and supplier entertainment, customary staff costs, sales promotion and costs correlated with income |
| Client and supplier entertainment | Art. 15.e | Deductible up to 1% of the net turnover of the period: "serán deducibles con el límite del 1 por ciento del importe neto de la cifra de negocios del período impositivo" |
| Expenses of acts contrary to the legal order | Art. 15.f | Never deductible |
| Service charges from, or paid through, persons in a listed tax haven | Art. 15.g | Not deductible unless the company proves the transaction was really carried out |
| Impairment of holdings in the capital or own funds of other entities, in the cases listed | Art. 15.k | Never deductible |
| Net financial expense | Art. 16.1 | Deductible up to 30% of the operating profit of the year: "Los gastos financieros netos serán deducibles con el límite del 30 por ciento del beneficio operativo del ejercicio" |

**Floor under the interest limit**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-sociedades/modelo-202-is-i_____resencia-territorio-fraccionado_/instrucciones/Instrucciones-para-2025.html |
| Net financial expense that is deductible whatever the operating profit limit | EUR 1,000,000 | The modelo 202 instructions set the floor out in the instalment calculation: "Si GFN (h + m + n) > (i), e i) > 1.000.000; k) = i) + j)" |

The statute writes that floor in words, as one million euros. It is scaled down for a period shorter than a year. Disallowed interest carries forward with no time limit.

## Section 7: ZEC Canarias (Zona Especial Canaria)

Treat this section as a pointer. A Zona Especial Canaria entity is registered in a special register and taxed under Ley 19/1994, and a real case needs that law and the Canary government's own guidance: https://www.gobiernodecanarias.org

**Zona Especial Canaria**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-1994-15794 |
| Special rate on the part of the base from operations really carried out in the zone | 4% | Art. 43: "El tipo de gravamen especial aplicable será del 4%" |
| Ceiling on the base under the job creation rule, for an entity meeting the minimum job creation | EUR 1,800,000 | Art. 44.6.b: "1.800.000 euros, para aquellas entidades de la Zona Especial Canaria que cumplan el requisito de creación mínima de empleo" |
| Added to that base for each job above the minimum, up to 50 jobs | EUR 500,000 | Art. 44.6.b: "500.000 euros adicionales por cada puesto de trabajo que exceda del mínimo señalado, hasta alcanzar 50 puestos de trabajo" |
| Ceiling on the resulting cut in the gross tax, as a share of the entity's net turnover | 30% | Art. 44.6.b: "no podrá ser superior al 30 por ciento del importe neto de la cifra de negocios de la entidad de la Zona Especial Canaria" |
| Minimum investment in the first two years, Gran Canaria and Tenerife | EUR 100,000 | Art. 31.2.d: "En las islas de Gran Canaria y Tenerife, 100.000 euros" |
| Minimum investment in the first two years, the other islands | EUR 50,000 | Art. 31.2.d: "En las islas de El Hierro, Fuerteventura, La Gomera, Lanzarote y La Palma, 50.000 euros" |

The special rate reaches only the smaller of two amounts: the share of the base fixed by the coefficient in art. 44.4, and the amount worked out under the job creation rule in the table. The minimum job creation is five jobs in Gran Canaria and Tenerife and three in El Hierro, Fuerteventura, La Gomera, Lanzarote and La Palma, created within six months of registration and kept as the average headcount for as long as the regime is used. The part of the base above the ceiling is taxed at the ordinary rate for the company. The special rate does not reach operations carried out with persons resident in non-cooperative jurisdictions.

## Section 8: Worked Example: Standard SL

The worked example that stood here used invented amounts and an effective rate worked out from them. No official page prints those numbers, so they have been removed. What follows is the same case as an order of operations. Take a Madrid SL on a calendar year, net turnover in 2025 below the micro company figure in Section 2, an accounting profit, some non-deductible expenses, an increase in own funds, carried forward losses and one employee with a disability of at least the lower grade in Section 4.4.

1. Start from the accounting profit for 2026 under the Código de Comercio.
2. Add the non-deductible expenses from Section 6 as positive adjustments, and take off any negative adjustments, including the amortisation difference where the tax coefficient in Section 4.7 differs from the accounting charge.
3. Take the capitalisation reserve off the result, at the percentage in Section 4.1 of the increase in own funds, within the cap in that same table.
4. Take off carried forward losses, within the limit in Section 4.2 for the company's turnover and never below the floor in that section. The result is the taxable base and it cannot be negative.
5. Apply the micro company rates in Section 2: the lower rate on the band shown there, the higher rate on the rest. That gives the gross tax.
6. Take off the deduction for the rise in the average headcount of workers with a disability, at the amount in Section 4.4, within the joint cap in that table. That gives the net tax.
7. Take off the amounts withheld and the instalments paid on modelo 202. What is left is the balance to pay or to refund.

This company is below the turnover in Section 4.6, so the minimum tax does not bite. Do not state an effective rate: no official page prints one.

## Section 9: Filing Obligations

**Filing obligations**

| Form | Who must file | Deadline |
| --- | --- | --- |
| Modelo 200 | Every taxpayer of this tax, except the fully exempt bodies in art. 9.1 | The 25 calendar days following the 6 months after the end of the period |
| Modelo 202 | A company whose art. 40.2 base is positive, and every company above the turnover in Section 5, which files even when nothing is due; entities within art. 29.4 and art. 29.5 make no instalment and file nothing | The first 20 calendar days of April, October and December |
| Modelo 220 | Tax consolidation groups | The same window as modelo 200 for the parent |
| Modelo 232 | Related party transactions above the thresholds below, and, whatever the amount, a taxpayer with operations or holdings in a listed tax haven or claiming the intangibles reduction | The month following the ten months after the end of the period |

The modelo 200 deadline is in art. 124.1 of Ley 27/2014: see https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 Where the form for the period has not been approved when that window opens, the return is due within 25 calendar days of the rule approving it. The modelo 232 deadline is in art. 4 of Orden HFP/816/2017: see https://www.boe.es/buscar/act.php?id=BOE-A-2017-10042

**Modelo 232 thresholds**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2017-10042 |
| All transactions with the same related party in the period, at market value | EUR 250,000 | Art. 2.1.a: "Operaciones realizadas con la misma persona o entidad vinculada siempre que el importe de la contraprestación del conjunto de operaciones en el período impositivo supere los 250.000 euros" |
| Specific transactions, each type counted separately | EUR 100,000 | Art. 2.1.b: "Operaciones específicas, siempre que el importe conjunto de cada una de este tipo de operaciones en el período impositivo supere los 100.000 euros" |
| Transactions of the same type valued by the same method, as a share of turnover, whatever the amount of the other thresholds | 50% | Art. 2.3: "siempre que el importe del conjunto de dichas operaciones en el período impositivo sea superior al 50% de la cifra de negocios de la entidad" |

### Exempt from filing Modelo 200:

- Bodies fully exempt under art. 9.1 of Ley 27/2014: the State, the autonomous communities, local authorities and the bodies listed with them.
- Partially exempt entities under art. 9.3 need not file where all three of the following hold together, under art. 124.3.

**Partially exempt entities: when no return is due**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 |
| Total income for the year not above | EUR 75,000 | Art. 124.3.a: "Que sus ingresos totales no superen 75.000 euros anuales" |
| Non-exempt income not above | EUR 2,000 | Art. 124.3.b: "Que los ingresos correspondientes a rentas no exentas no superen 2.000 euros anuales" |

The third condition is that all the non-exempt income was subject to withholding. Entities under art. 9.2, art. 9.3 and art. 9.4 otherwise declare all their income, exempt and non-exempt alike.

## Section 10: Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown territory | Common territory |
| Unknown turnover | The general rate in Section 2 |
| Unknown entity type | SL (standard) |
| Unknown period | The period beginning in 2026 |
| Unknown carried forward losses | None, so no loss relief |
| Tax amortisation unknown | The same as the accounting charge, so no adjustment |
| Unknown whether newly created | Not newly created, which is the higher rate |
| Small company status unknown | Not a small company, which is the higher rate |
| Unknown whether patrimonial | Ask: a patrimonial entity is shut out of the micro, small company and new company rates |

## The method, step by step

1. Fix the period and the territory. Check the accounting period in the articles of association, and check whether the company is taxed under common territory rules or under Álava, Bizkaia, Gipuzkoa or Navarra. Art. 27 of Ley 27/2014 sets the period and art. 7 sets who is liable: https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328
2. Work out which rate row applies. Test the previous period's net turnover, group wide, against the micro company figure in Section 2 and then against the small company figure; test whether the company is a patrimonial entity under art. 5.2; test whether it is in its first or second period with a positive base. Then read the rate off the 2026 row of the tables in Section 2, not off the body of art. 29.1: https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328
3. Build the base from the accounts. Start from the accounting profit under art. 10.3, add the non-deductible expenses in Section 6, apply the amortisation rules in Section 4.7 and the participation exemption in Section 4.8, then the capitalisation reserve and loss relief, both measured on the base imponible previa, and the levelling reserve on the base imponible that results: https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328
4. Work out the gross tax, take the deductions and bonificaciones in Section 4.4 and Section 4.5, then test the result against the minimum tax in Section 4.6 if the company is above that turnover or in a group: https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328
5. Deduct the amounts withheld and the instalments already paid on modelo 202, then file modelo 200 within the deadline in Section 9: https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328
6. Set up the next year's instalments. Decide or confirm the modelo 202 method, remembering that the art. 40.3 method is compulsory above the turnover in Section 5 and that the option is exercised on a censal return in February: https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-sociedades/modelo-202-is-i_____resencia-territorio-fraccionado_/instrucciones/Instrucciones-para-2025.html
7. Check the reporting forms. File modelo 232 where a related party threshold in Section 9 is crossed: https://www.boe.es/buscar/act.php?id=BOE-A-2017-10042

## Ask the client first

- What is the exact start and end date of the accounting period, and is this the company's first period, or its first period with a positive base?
- What was the net turnover of the immediately preceding period, and of every company in the same group under art. 42 of the Código de Comercio?
- Is the company a patrimonial entity, that is, is more than half its assets made up of securities or of assets not used in a business?
- Are there carried forward losses, and from which periods, and has the tax office already checked them?
- Did own funds rise during the period, and did the average headcount rise, and by how much against the previous period?
- Is any income earned in Ceuta, Melilla or the Zona Especial Canaria, or is the company registered in any special regime?
- Which modelo 202 method has the company been using, and was a censal option ever filed?

## When to refuse or refer

- A company taxed under Álava, Bizkaia, Gipuzkoa or Navarra. Their corporate tax is a different law with different rates and forms.
- Tax consolidation groups, mergers and demergers under the special restructuring regime, and the international fiscal transparency rules.
- Transfer pricing valuation. This Guide gives only the modelo 232 reporting thresholds, not the pricing method or the documentation content.
- The Canary Islands regimes, including the investment reserve and the Zona Especial Canaria beyond the pointer in Section 7.
- Any case that turns on a tax treaty, on a permanent establishment, or on the complementary tax for large groups.
- The global minimum tax for multinational groups, which is a separate law.
- Sector regimes: banking, hydrocarbons, shipping tonnage, listed property investment companies, cooperatives beyond the rate row in Section 2.

## PROHIBITIONS

- NEVER apply the micro company rates to a company whose previous period turnover reached the turnover figure in Section 2, and never to a patrimonial entity.
- NEVER apply the new company rate beyond the first period with a positive base and the one after it.
- NEVER compensate losses beyond the percentage limit for the company's turnover band in Section 4.2.
- NEVER exceed the joint cap on deductions in Section 4.4.
- NEVER forget the minimum tax for a company above the turnover in Section 4.6 or inside a consolidation group.
- NEVER apply the Zona Especial Canaria rate without checking the job creation condition and the base ceiling in Section 7.
- NEVER deduct fines, penalties or a return on own funds.
- NEVER apply the final rates in the body of art. 29.1 to a period beginning in 2026. Use the transitional rows in Section 2.
- NEVER apply common territory rates to a company taxed in a foral territory.
- NEVER confuse the personal income tax with this tax. They are separate regimes.

## Sources

- Ley 27/2014, del Impuesto sobre Sociedades, consolidated text: https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328
- Ley 19/1994, Régimen Económico y Fiscal de Canarias, consolidated text: https://www.boe.es/buscar/act.php?id=BOE-A-1994-15794
- Ley 49/2002, régimen fiscal de las entidades sin fines lucrativos, consolidated text: https://www.boe.es/buscar/act.php?id=BOE-A-2002-25039
- Orden HFP/816/2017, modelo 232, consolidated text: https://www.boe.es/buscar/act.php?id=BOE-A-2017-10042
- Agencia Tributaria, table of corporate tax rates in force: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/manual-sociedades-2025/capitulo-06-liquidacion-is-determinacion-tributaria/cuota-integra-casilla-00562/tipo-gravamen/tipos-gravamen-vigentes.html
- Agencia Tributaria, modelo 202 instructions for 2025 and later periods: https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-sociedades/modelo-202-is-i_____resencia-territorio-fraccionado_/instrucciones/Instrucciones-para-2025.html

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this Guide is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
