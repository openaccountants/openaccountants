---
name: es-estimated-tax
description: Use this skill whenever asked about Spanish estimated income tax payments (pagos fraccionados) for self-employed individuals (autonomos). Trigger on phrases like "Modelo 130", "pagos fraccionados", "estimated tax Spain", "IRPF quarterly", "Spanish advance tax", "autonomo tax payments", "estimacion directa", "Modelo 131", or any question about quarterly income tax prepayment obligations under the IRPF. Covers the quarterly filing schedule (Apr 20, Jul 20, Oct 20, Jan 30), the 20% cumulative computation method, the 70% withholding exemption, penalties for late filing, and payment procedures. ALWAYS read this skill before touching any estimated tax work for Spain.
version: 2.0
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

# Spain: quarterly IRPF payments for the self-employed (pagos fraccionados)

How a self-employed person in Spain pays income tax during the year: who must file modelo 130 in estimacion directa, who files modelo 131 under the module method, the percentage on each, the exemption for professionals whose invoices are withheld, the box by box computation, the quarterly deadlines, what happens when a quarter is late, and how the year's payments come back in the annual return. Figures are for tax year 2026. Two of the pages used carry their own dating and are named where used: the Agencia Tributaria page giving the 2026 late payment interest sits inside the Renta 2025 manual, and the Agencia Tributaria page on who the module method applies to states limits that the statute does not, which Section 5.6 prints side by side.

## Section 1: Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Spain |
| Tax | Quarterly IRPF payments on account (pagos fraccionados) |
| Primary legislation | Ley 35/2006 del IRPF, article 101; Real Decreto 439/2007 (Reglamento del IRPF), articles 109 to 112 |
| Supporting legislation | Ley 58/2003 General Tributaria, articles 27, 28 and 191; Orden EHA/672/2007; Orden HAP/2194/2013 |
| Authority | Agencia Estatal de Administracion Tributaria (AEAT) |
| Portal | sede.agenciatributaria.gob.es |
| Currency | EUR only |
| Form | Modelo 130 (estimacion directa); Modelo 131 (estimacion objetiva, the module method) |
| Filing schedule | Quarterly: 1 to 20 April, 1 to 20 July, 1 to 20 October, 1 to 30 January |
| Computation, modelo 130 | 20% of net income from 1 January to the quarter end, less earlier quarters and less withholding suffered |
| Exemption | A professional files nothing if at least 70% of last year's activity income bore withholding |
| Negative quarter | File a negative return. There is no refund inside the year |
| Status | Drafted from the official pages. No accountant has reviewed it yet |

**Filing schedule summary**

| Quarter | Period covered | Deadline |
| --- | --- | --- |
| Q1 (1T) | January to March | 1 to 20 April |
| Q2 (2T) | January to June, cumulative | 1 to 20 July |
| Q3 (3T) | January to September, cumulative | 1 to 20 October |
| Q4 (4T) | January to December, cumulative | 1 to 30 January of the next year |

Farming, livestock, forestry and fishing are the exception to the cumulative rule: those sections of both forms are worked on the QUARTER's income, not on the year to date. A deadline falling on a Saturday or a non-working day moves to the next working day.

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Modelo 130 or modelo 131 uncertain | Confirm the estimation method on the census declaration. Do not assume |
| Exemption status unclear | File modelo 130. The exemption is tested on last year's figures and must be evidenced |
| Cumulative or quarterly confusion | Cumulative from 1 January for the non-farming sections. Quarter only for the farming section |
| Low prior year income | Check the prior year net income against the reduction table in 5.2 |
| Someone in their first year of activity | There is no reduced percentage. See 5.5 |
| Activity in Ceuta, Melilla or La Palma | Use the reduced percentages in 5.1, and check the period they cover |

## Section 2: Required inputs and refusal catalogue

### Required inputs

**Minimum viable.** Income and deductible expenses from 1 January to the end of the quarter, withholding suffered over the same period, and the results of the earlier modelo 130 returns of the same year.

**Recommended.** Prior year net income from economic activities (for the reduction in 5.2), the share of last year's activity income that bore withholding (for the exemption in 5.4), and written confirmation of the estimation method.

**Ideal.** The complete libro registro de ingresos and libro registro de gastos, the asset and depreciation register, copies of every modelo 130 or modelo 131 filed this year, the certificados de retenciones, and last year's modelo 100.

**Refusal policy if the minimum is missing: SOFT WARN.** Without the year to date figures the computation cannot be made. Ask at minimum for a summary of income and expenses from 1 January.

### Refusal catalogue

- **R-ES-ET-1, estimacion objetiva (modulos).** Trigger: the client is on the module method. Message: "An activity on the module method pays on modelo 131, not modelo 130, and the percentage depends on the number of employees. Section 5.6 of this Guide covers modelo 131 in outline; the module amounts themselves are set by the annual module order and are not in this Guide."
- **R-ES-ET-2, cross-border income.** Trigger: the client is not resident in Spain, or has treaty income. Message: "A non-resident does not file modelo 130. Cross-border IRPF is outside this Guide."
- **R-ES-ET-3, an empresario claiming the exemption.** Trigger: a business activity, not a professional one, claims the withholding exemption. Message: "Article 109.2 Real Decreto 439/2007 gives the exemption to professional activities. Articles 109.3 and 109.4 give the same test to farming, livestock and forestry. A business activity in seccion primera of the IAE tariffs has no exemption."
- **R-ES-ET-4, a company.** Trigger: the client is an SL or another taxpayer of the corporate tax. Message: "A company pays its instalments on modelo 202 under the corporate tax, not on modelo 130. See the pointer in Section 7.3."
- **R-ES-ET-5, foral territory.** Trigger: the client is taxed in Bizkaia, Araba, Gipuzkoa or Navarra. Message: "Those territories run their own IRPF and their own instalment forms. This Guide is common territory only."

## Section 3: Payment pattern library

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as a pago fraccionado payment.

### 3.1 AEAT quarterly payment debits

**AEAT quarterly payment debits**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| AEAT, AGENCIA TRIBUTARIA | Pago fraccionado payment | Match with April, July, October or January timing |
| HACIENDA, MINISTERIO DE HACIENDA | Pago fraccionado payment | Government payee |
| MODELO 130 | Modelo 130 payment | Explicit form reference |
| MODELO 131 | Modelo 131 payment | Module method, same quarterly pattern |
| PAGO FRACCIONADO, IRPF TRIMESTRAL | Pago fraccionado payment | Explicit description |
| DOMICILIACION AEAT | Pago fraccionado payment | Direct debit taken by the AEAT |

### 3.2 Timing-based identification

**Timing-based identification**

| Debit date range | Likely quarter | Confidence |
| --- | --- | --- |
| 1 April to 25 April | Q1 (1T) filing | High if the payee is the AEAT |
| 1 July to 25 July | Q2 (2T) filing | High |
| 1 October to 25 October | Q3 (3T) filing | High |
| 1 January to 5 February | Q4 (4T) filing | High, the deadline is 30 January |

### 3.3 Related but NOT Modelo 130 payments

**Related but NOT Modelo 130 payments**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IVA, MODELO 303 | EXCLUDE | The quarterly VAT self-assessment, a different tax |
| MODELO 111 | EXCLUDE | Withholding the client has deducted from OTHERS and pays over |
| SEGURIDAD SOCIAL, RETA, AUTONOMO CUOTA | EXCLUDE | Social Security contribution |
| RENTA, DECLARACION ANUAL, MODELO 100 | EXCLUDE | Balance payable on the annual return |
| RECARGO, SANCION | EXCLUDE | Surcharge or penalty, see Section 6 |

### 3.4 NRC and payment references

**NRC and payment references**

| Reference pattern | Treatment | Notes |
| --- | --- | --- |
| NRC followed by digits | AEAT payment confirmed | Numero de Referencia Completo, issued by the bank |
| CSV followed by alphanumeric | Filing receipt reference | Codigo Seguro de Verificacion on the justificante |
| 130-1T, 130-2T, 130-3T, 130-4T | Modelo 130, that quarter | Self-identified |
| 131-1T, 131-2T, 131-3T, 131-4T | Modelo 131, that quarter | Self-identified |

## Section 4: Worked examples

Amounts in these examples are illustrative. The percentages used are the ones in the tables in Section 5.

### Example 1: Q2 filing (cumulative Jan-Jun)

**Input table**

| Item | Amount |
| --- | --- |
| Cumulative income, January to June | 30,000 |
| Cumulative deductible expenses, January to June | 10,000 |
| Withholding suffered on professional invoices, year to date | 500 |
| Q1 box 07 result, with no box 16 deduction taken in Q1 | 1,500 |

- Box 03, cumulative net income: 30,000 less 10,000, giving 20,000.
- Box 04, at 20% of box 03: 4,000.
- Box 05, the positive box 07 of the earlier quarter less its box 16: 1,500.
- Box 06, withholding year to date: 500.
- Box 07, box 04 less box 05 less box 06: 4,000 less 1,500 less 500, giving 2,000.
- Nothing in Section II, so box 12 equals box 07. No reduction applies, so box 19 is 2,000 payable.

### Example 2: 70% exemption applies

**Input.** An architect. Last calendar year, 80 per cent of the income of the professional activity bore withholding, above the share in the table in 5.1.

**Output.** No modelo 130 at all for that activity this year, not even a negative one. The withholding on the invoices does the job of the instalment, and it is credited in the annual return. The test is redone on each new year's figures.

### Example 3: negative cumulative result

**Input.** Losses year to date. Box 03 is negative 3,000.

**Output.** Box 04 is zero, because the percentage applies only to a positive box 03. Nothing is payable, and a negative return is filed. The negative figure is not refunded inside the year: it stays in the cumulative computation, so the next quarter starts from the year to date position again.

### Example 4: Low-income deduction

**Input.** Prior year net income from economic activities of 8,500, which is at or below the lowest band in the table in 5.2. Q1 box 03 of 5,000.

**Computation.** Box 04, at 20% of 5,000: 1,000. Box 12 is 1,000. Box 13 takes the top amount in the table in 5.2, 100. Box 14 is 1,000 less 100, giving 900 payable. Note where the reduction sits: AFTER withholding and earlier payments, not before them.

### Example 5: bank statement classification

**Input line:** `18.04.2026 ; DOMICILIACION AEAT MODELO 130 ; DEBIT ; 1T 2026 ; EUR -1.200,00`

**Classification:** modelo 130 payment, Q1 (1T) 2026. It is a payment on account of the person's own income tax, so it is not a deductible business expense; it is credited in the annual return.

## Section 5: Computation rules

### 5.1 The 20% cumulative method

Article 110.1 Real Decreto 439/2007 sets one percentage per situation. The percentage is a floor. Article 110.4 lets the taxpayer choose a HIGHER percentage, and the modelo 131 instructions say in as many words that lower percentages are not allowed.

**Percentages and the exemption (articles 109 and 110 Real Decreto 439/2007)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Modelo 130, estimacion directa, on net income from 1 January to the last day of the quarter | 20% | "el 20 por ciento del rendimiento neto correspondiente al período de tiempo transcurrido" |
| Modelo 131, module method, activity whose employee units are above one | 4% | "el 4 por ciento de los rendimientos netos resultantes de la aplicación de dicho método" |
| Modelo 131, module method, activity whose employee units are above zero and at most one | 3% | "en el supuesto de actividades que tengan sólo una persona asalariada el porcentaje anterior será el 3 por ciento" |
| Modelo 131, module method, activity with no employee units | 2% | "en el supuesto de que no disponga de personal asalariado dicho porcentaje será el 2 por ciento" |
| Modelo 131, module method, where no data-base can be fixed: on the QUARTER's sales or income | 2% | "el pago fraccionado consistirá en el 2 por ciento del volumen de ventas o ingresos del trimestre" |
| Farming, livestock, forestry and fishing, either method: on the QUARTER's income | 2% | "el 2 por ciento del volumen de ingresos del trimestre, excluidas las subvenciones de capital" |
| Share of last calendar year's activity income that must have borne withholding, for the exemption | 70% | "al menos el 70 por ciento de los ingresos de la actividad fueron objeto de retención" |
| Cut applied to every percentage above where the activity qualifies for the Ceuta and Melilla credit | 60% | "Los porcentajes señalados en el apartado anterior se reducirán en un 60 por ciento" |

The reduced percentages the form itself prints, and the one 2026 extension, are in the box table in 5.3. The three module rows above are worded in employee units because the modelo 131 instructions resolve a fractional headcount into units: the quotes here are the statute's, which speaks of whole persons, and the table in 5.6 carries the form's own band table. The cumulative rule applies to the non-farming sections only: for farming, livestock, forestry and fishing the base is the quarter's gross income, capital grants and compensation excluded.

What is deducted from the result differs by activity. Article 110.3.a lets the year to date withholding be deducted only for a professional activity in estimacion directa, for the letting of urban property that amounts to an economic activity, and for image rights. A pure business activity in estimacion directa normally suffers no withholding and deducts none. Article 110.3.b lets the QUARTER's withholding be deducted under the module method and for farming, livestock and forestry, and where that withholding is larger than the payment the difference carries to a later quarter of the same year.

### 5.2 Low-income deduction

Article 110.3.c Real Decreto 439/2007 gives a fixed cash reduction where the prior year was small. It is a band table, not a taper, and the top figure is a cliff: one euro over it and the reduction is nil.

**The reduction in box 13 of modelo 130 and box 09 of modelo 131**

| Prior year net income from economic activities | Reduction per quarter | Note |
| --- | --- | --- |
| Source | all figures below | https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html |
| At or below EUR 9,000 | EUR 100 | "Igual o inferior a 9.000 100" |
| Between EUR 9,000.01 and EUR 10,000 | EUR 75 | "Entre 9.000,01 y 10.000 75" |
| Between EUR 10,000.01 and EUR 11,000 | EUR 50 | "Entre 10.000,01 y 11.000 50" |
| Between EUR 11,000.01 and EUR 12,000 | EUR 25 | "Entre 11.000,01 y 12.000 25" |
| Above EUR 12,000 | none | "haya sido igual o inferior a 12.000 euros" |

Four points a reader gets wrong. The prior year figure is net income from economic activities BEFORE the reduction for irregular income and the other reductions on net income. Someone who carried on no activity at all last year is treated as having nil, so they take the top amount. Where the same person files both forms in the same quarter, the reduction may be split between box 13 of modelo 130 and box 09 of modelo 131, and the two together may not exceed the amount for the quarter. And where the reduction is larger than what is left to pay, the excess carries to a later quarter of the same year whose positive amount allows it.

### 5.3 Modelo 130 form key lines

The boxes below are the ones the Agencia Tributaria instructions describe. Section I is the non-farming activities in estimacion directa, Section II is farming, livestock, forestry and fishing in estimacion directa, and Section III adds them up.

**Modelo 130 boxes and the percentages the form applies**

| Box | What goes in it | Value where the form states one |
| --- | --- | --- |
| Source | all figures below | https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html |
| 01 | Gross income of the Section I activities, 1 January to the quarter end | |
| 02 | Deductible expenses of the same period, depreciation and provisions included | |
| 03 | Box 01 less box 02. A negative figure is entered with a minus sign. Net income to which article 32.1 Ley 35/2006 applies is taken after the reduction that article gives, for the instalment as well as for the year | |
| 04 | The percentage on a POSITIVE box 03. Zero where box 03 is negative | 20% |
| 04 | Where the activity qualifies for the Ceuta and Melilla credit | 8% |
| 05 | Positive box 07 amounts of earlier quarters of the same year, less their box 16 amounts | |
| 06 | Withholding and payments on account suffered, 1 January to the quarter end | |
| 07 | Box 04 less box 05 less box 06. May be negative | |
| 08 | The QUARTER's income from farming, livestock, forestry and fishing, current grants included, capital grants and compensation excluded | |
| 09 | The percentage on box 08 | 2% |
| 09 | Where that activity qualifies for the Ceuta and Melilla credit | 0.8% |
| 10 | Withholding for the SAME quarter on the farming, livestock and forestry activities only. A fishing activity has nothing to enter here | |
| 11 | Box 09 less box 10 | |
| 12 | Box 07 plus box 11, signs respected. A negative total is entered as zero | |
| 13 | The reduction for a small prior year, from the table in 5.2 | |
| 14 | Box 12 less box 13 | |
| 15 | Negative box 19 results of earlier quarters of the same year not yet used, entered without a sign, only where box 14 is positive, and never more than box 14 | |
| 16 | The home loan deduction, on box 03 | 2% |
| 16 | Cap on that deduction, per quarter and for the year | EUR 660.14 |
| 16 | Foreseeable annual gross income at or above which the deduction is not available | EUR 33,007.20 |
| 16 | Where only the farming section is filled, the same percentage on box 08 instead of box 03. For that case the instructions give the cap above as an annual cap only | 2% |
| 17 | Box 14 less box 15 less box 16 | |
| 18 | On a complementary return only: the amount payable on the earlier return for the same quarter | |
| 19 | Box 17 less box 18, the result carried to the payment box. Where box 17 is negative, box 19 carries the same negative amount | |

Notes on the boxes that catch people. Box 04 takes the reduced percentage only for the Ceuta and Melilla credit under article 68.4 Ley 35/2006, and, for the third and fourth quarters of 2026 only, for the Isla de La Palma under disposicion adicional 57 of the same law as written by Real Decreto-Ley number 23 of 2026, of 8 September. Where the person also runs activities that do not qualify, the general percentage applies to those. Box 16 is only for a loan on a main home bought, or a refurbishment already being paid for, before 1 January 2013, it is not available at all where the money goes to building or extending the home, and the instructions rule it out entirely for someone who also files modelo 131, for someone running both farming and non-farming activities, and for someone who has told an employer about the same loan on modelo 145. A negative box 19 in the first three quarters is marked "A deducir" and used against a later quarter; a negative box 19 in the fourth quarter is marked "Negativa" and the position is settled in the annual return instead. Box 16 needs a positive box 14 and may never be more than box 14 less box 15.

### 5.4 The 70% withholding exemption

Article 109.2 Real Decreto 439/2007 releases a PROFESSIONAL activity from the pago fraccionado altogether, filing included, where at least the share in the table in 5.1 of the income of that activity bore withholding or a payment on account in the IMMEDIATELY PRECEDING calendar year. Articles 109.3 and 109.4 give the same test to farming and livestock, and to forestry, measured on the income of the holding with grants and compensation left out.

Four things the test is not. It is not tested on the current year: it looks back one calendar year, so the position can flip each January. It is not available to a business activity. It is not a partial relief: it removes the obligation for that activity, and it does not reduce anything. And in the year the activity starts there is no preceding year, so article 109.5 measures the share over the period the payment itself covers, which means the answer can differ quarter by quarter in the first year.

Where a person runs one activity that is exempt and another that is not, only the non-exempt one goes on the form.

### 5.5 New autonomo reduction

There is no reduced pago fraccionado percentage for a new self-employed person. Article 110.4 Real Decreto 439/2007 allows a taxpayer to apply a HIGHER percentage than the one in the table in 5.1, and the modelo 131 instructions say in as many words that lower percentages are not allowed. What does change in the early years is the WITHHOLDING on a professional's own invoices, which is a different thing: it is tax the payer takes off the client's invoices, not a payment the client makes.

**Withholding on a professional's invoices (article 95 Real Decreto 439/2007)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Ordinary rate the payer withholds on a professional fee | 15% | "se aplicará el tipo de retención del 15 por ciento sobre los ingresos íntegros satisfechos" |
| Rate in the tax year the professional activity starts and the two following years | 7% | "el tipo de retención será del 7 por ciento en el período impositivo de inicio de actividades" |

The reduced rate runs only if no professional activity was carried on in the year before the start date, and the professional must tell the payer in writing. A lower rate withheld means a smaller box 06, so it makes the modelo 130 payment LARGER, not smaller. That is the part people misread as a reduction.

### 5.6 Modelo 131 and the module method

An activity whose net income is fixed by the module method pays on modelo 131, on the same four dates, under its own [modelo 131 instructions](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-131-irpf______sionales-estimacion-objetiva-fraccionado_/instrucciones.html). Box 01 is the net income the modules produce from the data-base at 1 January, or at the start date where the activity was not carried on in the previous year, after the employment and investment incentives and the correcting indices, and after the general reduction on module net income that the annual module order sets for the year. The reduction for 2026 is in the table below. Box 02 applies the percentage that matches the number of employees, from the table in 5.1. Box 03 and box 04 are for an activity where no data-base can be fixed, worked on the quarter's sales. Box 05 and box 06 are the farming section. Box 07 adds them, box 08 takes off the quarter's withholding, box 09 is the reduction from the table in 5.2, and box 10 is box 07 less box 08 less box 09. Box 11 to box 15 then run as boxes 15 to 19 of modelo 130 do, with one difference: the home loan deduction in box 12 uses the lower percentage in the table below on box 01, the modelo 130 percentage on box 03, or the modelo 130 percentage on box 05 where only the farming section is filled, and its cap is a yearly one measured across all four returns of the year. For an activity qualifying for the Ceuta and Melilla credit, and exceptionally in the third and fourth quarters of 2026 for the Isla de La Palma, the instructions multiply the percentages by the factor zero point four rather than printing a separate rate.

**The employee bands and the reduction the modelo 131 instructions apply**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below except the general reduction, which names its own | https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-131-irpf______sionales-estimacion-objetiva-fraccionado_/instrucciones.html |
| Employee units above one, at the date the data-base is taken | 4% | "1,01 o más ... el 4 por 100" |
| Employee units above zero and at most one | 3% | "0,01 a 1 ... el 3 por 100" |
| No employee units | 2% | "0,00 ... el 2 por 100" |
| General reduction on module net income for 2026, applied in working the instalment | 5% | Orden HAC/1425/2025, https://www.boe.es/buscar/act.php?id=BOE-A-2025-25272 "una reducción del 5 por ciento sobre el rendimiento neto de módulos" |
| Modelo 131 box 12, percentage of box 01 for a pre-2013 main home loan | 0.5% | "el porcentaje del 0,5 por 100 sobre la cantidad consignada en la casilla 01" |
| Cut in modelo 131 box 06 for a young farmer or agricultural employee meeting disposicion adicional 6 Ley 35/2006 | 25% | "podrán reducir dicha cantidad en un 25 por 100" |

Employee units are counted by the annual hours per worker set in the applicable collective agreement, following Tribunal Supremo judgment 1667/2023, and are taken to two decimals. A part time employee therefore falls in the middle band, not the bottom one.

Whether a client may use the module method at all rests on income limits that two official sources state differently, and the answer decides which form they file.

**Module method income limits, measured on the preceding year**

| Limit | Value | Note |
| --- | --- | --- |
| Source, the statute, article 31.1.3 Ley 35/2006 | see below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| All activities except farming, livestock and forestry | EUR 150,000 | "excepto las agrícolas, ganaderas y forestales, 150.000 euros anuales" |
| Of that, income from operations for which an invoice must be issued to a business or professional | EUR 75,000 | "supere 75.000 euros" |
| Farming, livestock and forestry together | EUR 250,000 | "Para el conjunto de sus actividades agrícolas, ganaderas y forestales, 250.000 euros anuales" |
| Purchases of goods and services in the preceding year, capital assets excluded | EUR 150,000 | "excluidas las adquisiciones de inmovilizado, en el ejercicio anterior supere la cantidad de 150.000 euros" |
| Source, the Agencia Tributaria page on who the module method applies to | see below | https://sede.agenciatributaria.gob.es/Sede/empresarios-individuales-profesionales/contribuyentes-modulos/quien-se-aplica/irpf.html |
| All activities except farming, on that page, for 2016 to 2026 inclusive | EUR 250,000 | "los límites de 150.000 € y 75.000 € pasan a ser 250.000 € y 125.000 € respectivamente" |
| Of that, invoiced to businesses and professionals, on that page, for 2016 to 2026 inclusive | EUR 125,000 | "pasan a ser 250.000 € y 125.000 € respectivamente" |
| Purchases, on that page, for 2016 to 2026 inclusive | EUR 250,000 | "el volumen de compras en bienes y servicios en el año inmediato anterior no puede superar los 250.000 €" |

The two official sources disagree, and this Guide prints both. The higher limits come from disposicion transitoria 32 Ley 35/2006, whose heading still reads "en los ejercicios 2016 a 2024". Three Real Decreto-ley in turn tried to extend them and the Congress of Deputies left each one without effect, which is why the statute now prints the lower figures for 2026. The Agencia Tributaria's own page, updated in September 2026, still states the higher limits for 2016 to 2026 inclusive. Do not tell anyone they are inside or outside the module method on one of these sources: check the position with the Agencia Tributaria for the year in question, because the answer decides whether they file modelo 130 or modelo 131.

## Section 6: Penalties and interest

### 6.1 Voluntary late filing surcharges

Article 27 Ley 58/2003 governs a return filed late WITHOUT a prior demand from the tax office. It is not a fixed ladder of bands: it is one per cent, plus the same again for each complete month of delay, and a single higher figure once twelve months have passed. The surcharge replaces any penalty, and no late payment interest is charged for the first twelve months.

**Late filing without a demand, and the penalties if there was one (Ley 58/2003)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186 |
| Filed and paid late without a demand, and the same again for each complete month of delay, to twelve months | 1% | "El recargo será un porcentaje igual al 1 por ciento más otro 1 por ciento adicional por cada mes completo de retraso" |
| Filed more than twelve months late without a demand, with interest running from the end of month twelve | 15% | "el recargo será del 15 por ciento y excluirá las sanciones que hubieran podido exigirse" |
| Cut in that surcharge where the rest of it and the tax are both paid inside the article 62.2 period | 25% | "El importe de los recargos a que se refiere el apartado 2 anterior se reducirá en el 25 por ciento" |
| Source, the row below | the row below | https://sede.agenciatributaria.gob.es/Sede/deudas-apremios-embargos-subastas/apremios/tipos-recargos.html |
| Recargo ejecutivo, the whole debt paid before the demand for payment is served, with no interest on top | 5% | "Recargo ejecutivo: es el 5% del importe principal de la deuda" |
| Recargo de apremio reducido, paid inside the period opened by the demand for payment | 10% | "El recargo de apremio reducido será del 10 por ciento" |
| Recargo de apremio ordinario, every other enforcement case, and interest on top | 20% | "El recargo de apremio ordinario será del 20 por ciento" |

An older ladder of one, two, three, five, ten and fifteen per cent bands is still widely quoted for this. It is a previous wording of article 27 and it is not what the consolidated law now says.

### 6.2 Late filing after AEAT request

Once the tax office has asked, article 27 no longer applies and the case moves to the penalty regime of article 191 Ley 58/2003.

**Penalty for failing to pay the self-assessed tax (article 191 Ley 58/2003)**

| Severity | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186 |
| Minor (leve) | 50% | "La sanción por infracción leve consistirá en multa pecuniaria proporcional del 50 por ciento" |
| Base of penalty at or below which the failure is minor | EUR 3,000 | "La infracción tributaria será leve cuando la base de la sanción sea inferior o igual a 3.000 euros" |
| Serious (grave), top of the band | 100% | "multa pecuniaria proporcional del 50 al 100 por ciento" |
| Very serious (muy grave), top of the band | 150% | "multa pecuniaria proporcional del 100 al 150 por ciento" |
| Cut where the taxpayer accepts the assessment (art. 188.1.b) | 30% | "Un 30 por ciento en los supuestos de conformidad" |
| Further cut, applied after that one, where the remaining penalty is paid in the article 62.2 period or under a guaranteed instalment agreement and nothing is appealed (art. 188.3) | 40% | "se reducirá en el 40 por ciento si concurren las siguientes circunstancias" |

How the band is picked. At or below the base figure above the failure is minor. Above it, it is still minor where there was no concealment, and serious where there was. It is never minor where false invoices were used, where bad record keeping affected more than a tenth of the base, or where tax withheld from others was not paid over. Fraudulent means make it very serious in every case.

### 6.3 Late payment interest (interes de demora)

**Interest for 2026 (Agencia Tributaria, Renta 2025 manual, page on other points of interest)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/guia-principales-novedades/otras-cuestiones-interes.html |
| Interes de demora tributario for 2026 | 4.0625% | "Para 2026, se mantiene el interés legal en el 3,25 por 100 y el interés de demora en el 4,0625 por 100" |

The rate holds only because the budget was rolled over. It changes on the day a 2026 budget law takes effect, so date any computation that uses it.

## Section 7: Filing and payment procedure

### 7.1 Filing methods

**Filing methods**

| Method | Details |
| --- | --- |
| Sede electronica of the AEAT | Online with a recognised electronic certificate or with Cl@ve |
| Printed predeclaracion | Printed ONLY through the Agencia Tributaria's own print service, then taken to a bank. Not available where electronic filing is compulsory |
| Asesor fiscal or gestor | Files on the client's behalf through the same portal |

Both forms are filed under Orden HAP/2194/2013. A quarter with nothing to pay still needs a return: a negative one, or one marked "A deducir" where the result carries forward.

### 7.2 Payment methods

**Payment methods**

| Method | Details |
| --- | --- |
| Domiciliacion bancaria | Direct debit. Give the full IBAN of an account at a collaborating entity, or at another entity inside the single euro payments area |
| Obtener NRC | Get the Numero de Referencia Completo from the bank, then file with it |
| Cargo en cuenta | Charged to the account at the moment of filing |
| Tarjeta or Bizum | Card or instant transfer through a secure commerce platform, available since the 2025 exercise |
| Reconocimiento de deuda | Acknowledge the debt and ask for deferral, offset, transfer or a tax current account |

The instructions do not state the cut-off date for setting up a direct debit. Check it on the Agencia Tributaria page for the period before promising a client a date. Keep the justificante de presentacion with its Codigo Seguro de Verificacion.

### 7.3 How a pago fraccionado meets the annual return, and the other forms

The pago fraccionado is a payment on account of the person's own IRPF, not a separate tax and not an expense. In the annual return, modelo 100, the year's payments are set against the tax finally due together with the withholding on the certificates, and any excess comes back as a refund. This is the only route by which an overpaid year comes back: there is no refund inside the year, only a negative result carried to a later quarter. The annual computation itself is in the `es-income-tax` Guide.

Two neighbouring obligations run on the same quarterly calendar and are not this form. VAT is self-assessed on modelo 303: the mechanics are in the `es-vat-return` Guide, and the form's own [modelo 303 instructions for 2026](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html) carry the boxes. A company pays instalments of the corporate tax on modelo 202, on a different calendar and a different computation; the [modelo 202 instructions](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-sociedades/modelo-202-is-i_____resencia-territorio-fraccionado_/instrucciones/Instrucciones-para-2025.html) on the sede are headed "Instrucciones periodo 2025 y siguientes", so the same page governs 2026 and there is no newer page to look for. Neither form is covered here.

## Section 8: Edge cases

**EC1, negative cumulative result.** Box 04 is zero where box 03 is negative, so nothing is payable and a negative return is filed. A negative box 12 is entered as zero, so the loss itself never becomes a box 19 amount to carry: it works through the cumulative base instead, because the next quarter starts again from 1 January. The only figure that goes into box 15 of a later quarter is a negative box 19, which arises when the reduction in box 13 is larger than box 12. Nothing is refunded inside the year.

**EC2, professional exempt from modelo 130.** Where last year's share of withheld income cleared the figure in the table in 5.1, the activity files nothing at all this year.

**EC3, activity started mid-year.** Someone registering in May first files for Q2, by 20 July, on the period from the start date. In a start year the exemption test of article 109.5 is measured over the period the payment covers, not over a preceding year.

**EC4, modelo 131 instead of modelo 130.** The module method uses modelo 131 and a percentage set by the number of employees. Which method applies turns on limits two official sources state differently: see 5.6.

**EC5, the fourth quarter has a longer window.** The fourth quarter is filed between 1 and 30 January of the next year, against the 20th for the other three.

**EC6, first year of activity.** There is no reduced percentage. What is lower in the first years is the withholding rate on a professional's invoices, in the table in 5.5, and a lower withholding makes the modelo 130 payment larger.

**EC7, Ceuta, Melilla and La Palma.** An activity with the right to the credit of article 68.4 Ley 35/2006 uses the reduced percentages in 5.3. The Isla de La Palma extension applies only to the third and fourth quarters of 2026.

**EC8, income attributed through a comunidad de bienes.** Article 112 Real Decreto 439/2007 puts the pago fraccionado on each member in proportion to their share of the profit. The entity itself does not file modelo 130.

**EC9, a quarter with tax due but no cash.** Ask for a deferral or an instalment agreement when the return is filed, rather than filing late: the article 27 surcharges in 6.1 apply to the filing, not to the cash position.

## Section 9: Self-checks

Before delivering output, verify:

- [ ] The estimation method is confirmed, so the right form is used
- [ ] The exemption in 5.4 was tested on the PRIOR calendar year, or on the period covered where the activity started this year
- [ ] The non-farming figures are cumulative from 1 January, and the farming figures are the quarter only
- [ ] Earlier quarters' positive results were deducted in box 05
- [ ] Withholding was deducted only where article 110.3 allows it for this activity
- [ ] The reduction in 5.2 was checked against the prior year figure, and applied after withholding, not before
- [ ] A negative result was carried forward, not claimed as a refund
- [ ] The deadline used is the 20th, or the 30th for the fourth quarter, moved on for a non-working day
- [ ] Ceuta, Melilla or La Palma was checked before the percentage was applied
- [ ] Box references match the current form, not an older numbering
- [ ] The output is labelled an estimate until an asesor fiscal confirms it

## Section 10: Test suite

### Test 1: Q2 standard computation

**Input:** cumulative income 30,000, expenses 10,000, withholding 500, Q1 result 1,500.
**Expected:** box 03 of 20,000. Box 04 at 20% is 4,000. Less 1,500 and less 500, giving 2,000 payable.

### Test 2: 70% exemption

**Input:** a professional, 80 per cent of last year's activity income withheld.
**Expected:** no modelo 130 at all, not even a negative return.

### Test 3: negative result

**Input:** box 03 of negative 3,000.
**Expected:** box 04 zero, box 12 zero, a negative return filed, and the loss recovered through the cumulative base of the next quarter rather than through box 15.

### Test 4: Low-income deduction

**Input:** prior year net income 8,500, Q1 box 03 of 5,000.
**Expected:** box 04 at 20% is 1,000, box 13 takes the top amount in 5.2, and 900 is payable.

### Test 5: activity started mid-year

**Input:** registered in May 2026, income from May to June 6,000, expenses 2,000.
**Expected:** box 03 of 4,000, box 04 at 20% is 800, due by 20 July 2026.

### Test 6: Q4 longer deadline

**Input:** the Q4 return for 2026.
**Expected:** the window is 1 to 30 January 2027.

### Test 7: module method, one employee

**Input:** an activity on the module method with exactly one employee.
**Expected:** modelo 131, and box 02 uses the middle employee band in 5.6, because one whole employee is inside the band that ends at one unit, not the top band.

## The method, step by step

1. Fix the estimation method and the activity type. Estimacion directa goes on modelo 130, the module method on modelo 131, and which one is available turns on the limits in 5.6, on which two official sources disagree. [Ley 35/2006](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764)
2. Test the exemption before doing any arithmetic. For a professional activity, article 109.2 asks whether at least the share in the table in 5.1 of LAST calendar year's activity income bore withholding; articles 109.3 and 109.4 ask the same of farming, livestock and forestry; article 109.5 covers a start year. If it is met, that activity files nothing. [Real Decreto 439/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820)
3. Build the base. For modelo 130, income less deductible expenses from 1 January to the last day of the quarter, under the rules of the estimacion directa modality in use; for the farming section, the quarter's gross income with capital grants and compensation excluded. [Real Decreto 439/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820)
4. Apply the percentage from the table in 5.1, using the reduced figure only for a Ceuta and Melilla activity or, in the third and fourth quarters of 2026, for the Isla de La Palma. [Modelo 130 instructions](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html)
5. Deduct, in the order the form uses: earlier quarters' positive results, then the withholding article 110.3 allows for this activity, then the reduction in 5.2, then any unused negative result of an earlier quarter, then the home loan deduction if it is available. [Modelo 130 instructions](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html)
6. File and pay between the 1st and the 20th of April, July and October, and between the 1st and the 30th of January for the fourth quarter, moving a non-working day on. File a negative return where nothing is due. [Pagos fraccionados, plazos](https://sede.agenciatributaria.gob.es/Sede/irpf/retenciones-ingresos-cuenta-pagos-fraccionados/pagos-fraccionados/plazos-declaracion-ingreso.html)
7. Carry the year's payments into the annual return, modelo 100, together with the withholding certificates. Article 99 Ley 35/2006 makes a pago fraccionado a payment on account of the same tax, so the final position, refund included, is settled there and nowhere else. [Ley 35/2006](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764)

## Ask the client first

- Estimacion directa or the module method, and is the activity professional or business? The pair decides the form, the percentage and whether the exemption can exist.
- What share of LAST calendar year's income from this activity had withholding taken off it? That one number can remove the obligation entirely.
- Is this the first year of the activity? If it is, there is no preceding year for the exemption test, and the withholding rate on the invoices is the reduced one in 5.5.
- What was your net income from economic activities last year? Below the top figure in 5.2 there is a fixed reduction each quarter.
- Is the activity carried on in Ceuta, Melilla or the Isla de La Palma, and from which quarter? The percentage changes, and the La Palma extension covers only the third and fourth quarters of 2026.
- Are you paying a loan on a main home bought, or a refurbishment already started, before 1 January 2013? Only then does box 16 exist.
- Did you file every earlier quarter of this year, and what was the result of each? Box 05 and box 15 both need them.

## When to refuse or refer

- A non-resident, or anyone with treaty income. They do not file modelo 130 at all.
- A company, or any other taxpayer of the corporate tax. Its instalments are modelo 202, a different tax with its own computation: see the pointer in 7.3.
- Anyone taxed in Bizkaia, Araba, Gipuzkoa or Navarra. Those territories run their own IRPF and their own forms, and none of the figures here are theirs.
- A client whose module method position is near the limits in 5.6. Two official sources give different limits and the form they must file depends on which one is right. Refer, and check with the Agencia Tributaria for the year.
- The module amounts themselves, and the module method's own net income computation. They are set by the annual module order and are not in this Guide.
- The withholding a client deducts from OTHERS and pays over on modelo 111. That is a different obligation with a different form.
- Anything past a demand from the tax office: an inspection, a penalty file or an enforcement notice. Section 6 gives the figures, not the procedure.

## Prohibitions

- NEVER compute the non-farming sections quarter by quarter. They are cumulative from 1 January, and earlier quarters come off in box 05.
- NEVER forget to deduct the earlier quarters' positive results.
- NEVER apply a percentage BELOW the one in 5.1. Article 110.4 allows a higher one only.
- NEVER give the withholding exemption to a business activity, and never test it on the current year.
- NEVER deduct withholding in estimacion directa for an activity article 110.3.a does not list.
- NEVER treat a pago fraccionado as a deductible business expense.
- NEVER tell a client they are inside or outside the module method on one of the two sources in 5.6.
- NEVER treat a negative quarter as a refund claim.
- NEVER confuse the fourth quarter deadline, the 30th of January, with the 20th that applies to the other three.
- NEVER present a computation as definitive. Label it an estimate for review.

## Sources

- Real Decreto 439/2007, Reglamento del IRPF, consolidated: https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820
- Ley 35/2006 del IRPF, consolidated: https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764
- Ley 58/2003, General Tributaria, consolidated: https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186
- Agencia Tributaria, modelo 130 instructions: https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html
- Agencia Tributaria, modelo 131 instructions: https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-131-irpf______sionales-estimacion-objetiva-fraccionado_/instrucciones.html
- Agencia Tributaria, pagos fraccionados, deadlines: https://sede.agenciatributaria.gob.es/Sede/irpf/retenciones-ingresos-cuenta-pagos-fraccionados/pagos-fraccionados/plazos-declaracion-ingreso.html
- Agencia Tributaria, who the module method applies to: https://sede.agenciatributaria.gob.es/Sede/empresarios-individuales-profesionales/contribuyentes-modulos/quien-se-aplica/irpf.html
- Agencia Tributaria, other points of interest, Renta 2025 manual: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/guia-principales-novedades/otras-cuestiones-interes.html

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
