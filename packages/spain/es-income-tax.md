---
name: es-income-tax
description: Use this skill whenever asked about Spanish personal income tax (IRPF -- Impuesto sobre la Renta de las Personas Fisicas) for self-employed individuals (autonomos). Trigger on phrases like "how much tax do I pay in Spain", "IRPF", "Modelo 100", "Modelo 130", "pago fraccionado", "estimacion directa", "retencion", "autonomo tax", "rendimientos de actividades economicas", "gastos deducibles", "amortizacion", "minimo personal", "cuota autonomica", or any question about filing or computing income tax for a self-employed or freelance client in Spain. Covers IRPF progressive rates, Modelo 100 structure, estimacion directa normal vs simplificada, deductible expenses, depreciation, quarterly payments (Modelo 130), withholding (retenciones), regional surcharges, personal and family allowances, and interaction with IVA and Social Security. ALWAYS read this skill before touching any Spanish income tax work.
version: 2.0
jurisdiction: ES
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spain: income tax (IRPF) for the self-employed (autonomo)

How Spain taxes a self-employed individual under IRPF: residence, the two tax bases, the state scale and the community half the state does not set, the minimums, deductible expenses, depreciation, withholding on invoices, and the modelo 100 return. Figures are for tax year 2026. Two pages carry another year and are named where used: the Agencia Tributaria page giving the return window is the Renta 2025 campaign page (2025 income, filed in 2026), and the page stating the 2026 legal and late payment interest sits in that same Renta 2025 manual. No figure set by an autonomous community is in this Guide: each community sets its own half of the general scale and no official page publishes the seventeen together, so this Guide gives the state half and routes.

## Spain income tax (IRPF): self-employed (autonomo). Guide version 2.0

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | Spain |
| Tax | IRPF (Impuesto sobre la Renta de las Personas Fisicas) |
| Currency | EUR only |
| Tax year | Calendar year (ano natural) |
| Legislation | Ley 35/2006 del IRPF; Real Decreto 439/2007 (Reglamento); Ley 58/2003 |
| Tax authority | Agencia Estatal de Administracion Tributaria (AEAT) |
| Annual return | Modelo 100, in the campaign of the following spring: see 5.6 |
| Status | Drafted from the official pages. No accountant has reviewed it yet |

### Residence: who this Guide covers [T1]

Article 9 Ley 35/2006 makes a person resident if ANY one test is met: more than 183 days in Spanish territory in the calendar year (sporadic absences count unless tax residence elsewhere is proved), or the main base or core of their activities or economic interests is in Spain, directly or indirectly. A rebuttable presumption also runs from the residence of a spouse and minor children. A resident is taxed on worldwide income and is inside this Guide. Someone meeting no test is not: they pay the non-resident tax (Real Decreto Legislativo 5/2004) on Spanish-source income at the rates in the routing table below, and file the non-resident forms, not the modelo 100. Which community a resident belongs to is settled separately by article 72: where they spent the greater number of days, failing that where their main centre of interests is, failing that the last declared residence.

### IRPF tax brackets: state portion (escala estatal) 2026 [T1]

This is HALF the tax. Article 63 sets the state scale; article 74 leaves a second scale to each community, and the resident pays both. There is no single "Spanish income tax rate", and this Guide prints no combined rate.

**State general scale, on the base liquidable general (article 63.1 Ley 35/2006)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Rate, first band | 9.5% | "12.450,00 9,50" |
| Top of the first band | EUR 12,450 | "12.450,00 9,50" |
| Rate, second band | 12% | "7.750,00 12,00" |
| Top of the second band | EUR 20,200 | "20.200,00" |
| Rate, third band | 15% | "15.000,00 15,00" |
| Top of the third band | EUR 35,200 | "35.200,00" |
| Rate, fourth band | 18.5% | "24.800,00 18,50" |
| Top of the fourth band | EUR 60,000 | "60.000,00" |
| Rate, fifth band | 22.5% | "240.000,00 22,50" |
| Top of the fifth band | EUR 300,000 | "300.000,00" |
| Rate above that | 24.5% | "adelante 24,50" |

- **Routing the other half.** Ask which community the client was resident in, then read that community's own scale in its own law. The 19, 24, 30, 37, 45 and 47 per cent figures sold as "the Spanish brackets" are the PAYROLL WITHHOLDING scale of article 101, not the tax scale, and doubling the state scale is not any community's tax either. The live Guide did both. Both are removed.

### Savings income rates (rentas del ahorro) 2026 [T1]

Savings income has its own base and scale. State law fixes both halves: article 66.1 the state half and article 76 the autonomous half, at the same rates. No community sets the savings scale, so these totals are the same across the common territory. Article 66.2 prints the same totals in one table, but it is written for a contributor habitually resident abroad, so cite articles 66.1 and 76 for a resident.

**Savings scale, on the base liquidable del ahorro (articles 66.1 and 76 Ley 35/2006, the two halves added)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Rate, first band | 19% | "0 0 6.000 19" |
| Top of the first band | EUR 6,000 | "6.000,00 1.140" |
| Rate, second band | 21% | "44.000 21" |
| Top of the second band | EUR 50,000 | "50.000,00" |
| Rate, third band | 23% | "150.000 23" |
| Top of the third band | EUR 200,000 | "200.000,00" |
| Rate, fourth band | 27% | "100.000 27" |
| Top of the fourth band | EUR 300,000 | "300.000,00" |
| Rate above that | 30% | "adelante 30" |

- **Which base.** Business and professional income, employment income, rent and most imputed income go in the general base. Interest, dividends, insurance returns and gains on transfers go in the savings base. Losses do not cross freely.

### Key allowances [T1]

The minimum is not a deduction from income: article 63.1 applies the scale twice, once to the base liquidable general and once to the minimum, and subtracts the second result. The effect is a band at nil.

**Personal and family minimums (articles 57 to 61 and article 20 Ley 35/2006)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Minimo del contribuyente | EUR 5,550 | "de 5.550 euros" |
| Increase, taxpayer over 65 | EUR 1,150 | "en 1.150 euros" |
| Further increase, taxpayer over 75 | EUR 1,400 | "en 1.400 euros" |
| Descendant, first child | EUR 2,400 | "2.400 euros" |
| Second child | EUR 2,700 | "2.700 euros" |
| Third child | EUR 4,000 | "4.000 euros" |
| Fourth and each later child | EUR 4,500 | "4.500 euros" |
| Increase for a descendant under three | EUR 2,800 | "en 2.800 euros" |
| Minimo por ascendientes | EUR 1,150 | "1.150 euros" |
| Annual income, exempt income excluded, a relative may not exceed and still count | EUR 8,000 | "no tenga rentas anuales, excluidas las exentas, superiores a 8.000 euros" |
| Minimo por discapacidad of the taxpayer | EUR 3,000 | "3.000 euros" |
| The same at the higher degree of disability | EUR 9,000 | "9.000 euros" |
| Assistance costs increase | EUR 3,000 | "3.000 euros" |
| Joint return, spouses together | EUR 3,400 | "3.400 euros" |
| Joint return, single parent unit | EUR 2,150 | "2.150 euros" |
| Employment income up to which the full work reduction is given | EUR 14,852 | "14.852 euros" |
| That full work reduction | EUR 7,302 | "iguales o inferiores a 14.852 euros: 7.302 euros anuales" |
| Net employment income at or above which no work reduction is given at all | EUR 19,747.5 | "rendimientos netos del trabajo inferiores a 19.747,5 euros" |
| Other income, exempt income excluded, above which no work reduction is given at all | EUR 6,500 | "distintas de las del trabajo superiores a 6.500 euros" |
| Income above which a relative filing their own return cancels the minimum | EUR 1,800 | "rentas superiores a 1.800 euros" |

- Each amount is annual and per person. Where two taxpayers are entitled for the same descendant or ascendant, article 61 splits it. The relative's income limit is a cliff, not a taper. The work reduction is for employment income, not for self-employment income, and it has two gates: net employment income must be below the upper figure above, and other income excluding exempt income must not be above the other-income figure above. Most autonomos with a business income above that figure get no work reduction at all, whatever their salary. Between the full-reduction threshold and the upper figure the reduction tapers rather than stopping. The live Guide's work reduction of "up to 6,498" is superseded and corrected above. A descendant or ascendant who files their own return with income above the article 61 threshold above gives no minimum at all, however low the figure in the table.

### Quarterly payments (modelo 130) [T1]

The quarter by quarter computation, the boxes and a carried-forward negative quarter are in the `es-estimated-tax` Guide. Rate and exemption only here.

**Pago fraccionado in estimacion directa (article 110 Real Decreto 439/2007) and the exemption (article 109 Real Decreto 439/2007)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Rate on net income from the start of the year, less earlier payments | 20% | "el 20 por ciento del rendimiento neto" |
| Share of last year's professional income that must have been withheld, to be exempt | 70% | "al menos el 70 por ciento de los ingresos" |

- **The exemption is in article 109.2 and is tested on the PREVIOUS calendar year.** A professional who cleared that share last year files no modelo 130 this year. A business activity in seccion primera of the IAE tariffs does not get it; articles 109.3 and 109.4 give the same test to agricultural, livestock and forestry activity. In the year an activity starts there is no previous year, and article 109.5 measures the share over the period the payment itself covers. Modulos uses modelo 131 and is out of scope.

### Retenciones (withholding on professional invoices) [T1]

**Withholding on professional activity income (article 95 Real Decreto 439/2007)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Standard rate on gross professional fees | 15% | "el tipo de retención del 15 por ciento sobre los ingresos íntegros" |
| Rate in the year activity starts and the two following | 7% | "será del 7 por ciento en el período impositivo de inicio de actividades" |

**Withholding on other income the client may receive (article 101 Ley 35/2006)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Rent of urban property | 19% | "inmuebles urbanos, cualquiera que sea su calificación, será del 19 por ciento" |
| Investment income (interest, dividends) | 19% | "capital mobiliario será del 19 por ciento" |

- **Scope.** These rates apply to consideration for a PROFESSIONAL activity. A business activity in seccion primera of the IAE tariffs is not withheld on the same way.
- **The reduced rate is not "the first three years" loosely.** Article 95 gives it for the period in which the activity starts and the TWO following, and only if no professional activity was carried on in the year before the start date. The client must tell the payer, who keeps the signed notice.
- **A retencion is a prepayment, never a cut in income.** Gross income is the full invoice before withholding.

### Non-resident rates, for routing only [T1]

**Non-resident tax (article 25 Real Decreto Legislativo 5/2004)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527 |
| General rate | 24% | "Con carácter general el 24 por 100" |
| Resident of another EU state, or of the EEA with exchange of information | 19% | "el 19 por ciento cuando se trate de contribuyentes residentes" |

### Conservative defaults [T1]

| Ambiguity | Default |
| --- | --- |
| Unknown autonomous community | State half only, and say the community half is missing. Never publish a combined general-scale rate |
| Unknown estimation regime | Estimacion directa simplificada |
| Unknown business-use share of a vehicle, phone or home | No deduction |
| Unknown expense category | Not deductible |
| Unknown whether professional or business activity | Professional |
| Unknown withholding rate | The standard professional rate above |
| Unknown residence | Ask. Never assume it from a Spanish address |

## Section 2: Required Inputs and Refusal Catalogue

### Required Inputs

Minimum: bank statement for the full tax year, the autonomous community of fiscal residence, the type of activity. Recommended: facturas emitidas and recibidas, modelo 130 filings, Social Security receipts. Ideal: complete libro registro de ingresos y de gastos, asset register, prior year modelo 100, all certificados de retenciones.

### Refusal Catalogue

- **R-ES-1, estimacion objetiva (modulos).** Estimacion directa only here. Modulos uses activity modules and modelo 131.
- **R-ES-2, non-resident.** Someone failing every test in article 9 files under the non-resident tax. Out of scope beyond the routing table.
- **R-ES-3, companies.** A company files Impuesto sobre Sociedades. Natural persons only here.
- **R-ES-4, foral territories.** Navarra, Araba, Bizkaia and Gipuzkoa run their own income tax, rates and forms.
- **R-ES-5, complex capital gains.** Property disposals, share sales and similar need their own computation. Escalate.
- **R-ES-6, the community half of the scale.** This Guide cannot supply it. Read the community's own law.

## Section 3: Transaction Pattern Library

### 3.1 Income Patterns (Credits on Bank Statement)

| Pattern | Tax Line | Treatment |
| --- | --- | --- |
| FACTURA EMITIDA, COBRO FACTURA | Actividades economicas | Business income, net of IVA if registered |
| RETENCION, RETENCION IRPF | Reduces cash, not income | Rate from the retenciones table; reconcile to the certificado |
| STRIPE PAYOUT, PAYPAL PAYOUT | Ingresos | Business income; match to invoices, gross up for fees withheld |
| NOMINA, SALARIO, SUELDO | Rendimientos del trabajo | NOT self-employment, separate category |
| INTERESES, DIVIDENDO | Rentas del ahorro | NOT self-employment, savings base |
| ALQUILER RECIBIDO, RENTA COBRADA | Capital inmobiliario | NOT self-employment, separate |
| DEVOLUCION HACIENDA, DEVOLUCION AEAT | EXCLUDE | Tax refund, not income |
| SUBVENCION, AYUDA | Check | Grants are generally taxable |

### 3.2 Expense Patterns (Debits on Bank Statement)

| Pattern | Tax Line | Tier | Treatment |
| --- | --- | --- | --- |
| ALQUILER OFICINA, RENTA LOCAL | Arrendamientos y canones | T1 | Deductible where the premises serve the activity |
| SUMINISTROS, LUZ, GAS, AGUA | Suministros | T2 | Home partly used: share rule in 5.2. Separate premises: full |
| TELEFONO, MOVISTAR, VODAFONE | Suministros | T2 | Business portion; nothing if the split is unknown |
| INTERNET, FIBRA | Suministros | T2 | Business portion; home share rule if working from home |
| GASOLINA, REPSOL, COMBUSTIBLE | Otros gastos (vehiculo) | T2 | Business portion, with records. Input IVA separate |
| COMIDA, RESTAURANTE (own meals) | Otros gastos deducibles | T2 | Only within the limits AND conditions in 5.2 |
| RESTAURANTE (entertaining a client) | Separate rule | T2 | Own ceiling, not covered here |
| CUOTA AUTONOMOS, SEGURIDAD SOCIAL | Gastos de personal | T1 | Contributions of the owner: deductible |
| ASESORIA, GESTORIA, ABOGADO, NOTARIO | Servicios profesionales | T1 | Deductible if related to the activity |
| MATERIAL OFICINA, PAPELERIA | Otros gastos | T1 | Deductible |
| SOFTWARE, SUSCRIPCION, LICENCIA | Otros gastos | T1 | Deductible if used in the activity |
| PUBLICIDAD, MARKETING, GOOGLE ADS | Publicidad | T1 | Deductible |
| FORMACION, CURSO, MASTER | Otros gastos | T1 | Deductible if related to the activity |
| SEGURO RESPONSABILIDAD, PROFESIONAL | Primas de seguros | T1 | Deductible |
| SEGURO SALUD (own health cover) | Primas de seguros | T1 | Capped: see 5.2 |
| SEGURO HOGAR, SEGURO COCHE (personal) | Not deductible | T2 | Vehicle: business portion only |
| COMISION BANCO, COMISION TPV, STRIPE FEE | Gastos financieros | T1 | Deductible |
| HACIENDA, AEAT, IRPF, MODELO 130 | EXCLUDE | T1 | Prepayments of tax, not expenses |
| IVA LIQUIDACION, IVA PAGO | EXCLUDE from IRPF | T1 | Separate tax; record net where registered |
| HIPOTECA, PRESTAMO | EXCLUDE | T1 | Loan principal |
| INTERESES PRESTAMO (business) | Gastos financieros | T1 | Deductible |

### 3.3 SaaS Subscriptions

| Pattern | Treatment |
| --- | --- |
| GOOGLE, MICROSOFT, ADOBE, SLACK, ZOOM, META | Otros gastos, deductible if used in the activity. The IVA reverse charge is separate |
| NOTION, GITHUB, FIGMA, CANVA, AWS, OPENAI | Otros gastos, deductible if used in the activity. The IVA reverse charge is separate |

### 3.4 Internal Transfers and Exclusions

| Pattern | Treatment |
| --- | --- |
| TRASPASO, TRANSFERENCIA PROPIA | EXCLUDE, internal movement |
| PRESTAMO, AMORTIZACION CAPITAL | EXCLUDE, loan principal |
| RETIRADA EFECTIVO, CAJERO | T2, ask. Default exclude |
| DONACION, DONATIVO | A credit in the tax computation, not a cost of the activity |

## Section 4: Worked Examples

Amounts here are sample data in euro, not figures from an official page. Rates come from the tables above.

### Example 1: standard autonomo (IT consultant)

Invoiced 55,000, all at the standard professional withholding. Costs: rent 6,000, Social Security 4,200, accountant 1,200, software 800, travel 2,000.

- Ingresos 55,000; withholding does not reduce income. Gastos 6,000 plus 4,200 plus 1,200 plus 800 plus 2,000, giving 14,200. Rendimiento neto previo 40,800.
- Hard-to-justify reduction at 5% of 40,800 is 2,040, above the ceiling, so use EUR 2,000. Rendimiento neto reducido 38,800.
- Withheld at 15% of 55,000: 8,250, credited against the final tax.

### Example 2: home office (suministros)

Home 80 square metres, room used for the activity 12 square metres. Supplies: electricity 1,200, gas 600, water 300, internet 480.

- Area proportion 12 divided by 80, giving 0.15. Deductible share: 30% of that, so 0.045 of each bill. Electricity 54, gas 27, water 13.50, internet 21.60, total 116.10.
- [T2] Flag: article 30.2 rule 5 letter b allows a higher OR lower percentage where proved. The table figure is a default, not a ceiling.

### Example 3: retencion reconciliation

Certificados total 8,250; modelo 130 payments total 4,000; final liability 10,500. Prepaid 8,250 plus 4,000, giving 12,250. Against 10,500, that is 1,750 repayable.

### Example 4: dietas (own meals while working)

- Capped at the per-day limit in 5.2; the day rate depends on an overnight stay and on whether the trip was inside Spain.
- Both conditions in article 30.2 rule 5 letter c must also hold: taken in a restaurant or hospitality establishment AND paid electronically. Cash fails.
- [T2] Flag: confirm the overnight stay and the payment method first.

## Section 5: Tier 1 Rules (When Data Is Clear)

### 5.1 Rendimientos de Actividades Economicas [T1]

- All business and professional income. Simplificada applies by default where prior-year turnover was under the limit in 5.4 and the taxpayer has not opted out. (Articles 27 to 32 Ley 35/2006; article 28 Real Decreto 439/2007.)

### 5.2 Gastos Deducibles [T1]

- An expense must be linked to the activity, evidenced by a proper invoice, and entered in the libro registro de gastos. (Article 28 Ley 35/2006; articles 28 to 30 Real Decreto 439/2007.)

**Special self-employed expense rules (article 30.2 Ley 35/2006)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Share of home supplies deductible, applied to the area proportion, unless another share is proved | 30% | "aplicar el 30 por ciento a la proporción" |
| Health insurance premium ceiling, per person covered | EUR 500 | "deducción será de 500 euros" |
| The same ceiling where that person has a disability | EUR 1,500 | "o de 1.500 euros por cada una de ellas" |

- Health cover may include the taxpayer, their spouse and children under twenty-five living with them. The ceiling is per person, per year.
- Home supplies: the share applies to the proportion the area used for the activity bears to total area. A higher or lower percentage is allowed where proved, so it is a default, not a cap.

**Own meal costs while working (article 30.2 rule 5 letter c Ley 35/2006, limits of article 9 Real Decreto 439/2007)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Per day in Spain, with an overnight stay | EUR 53.34 | "53,34 euros diarios" |
| Per day abroad, with an overnight stay | EUR 91.35 | "o 91,35 euros diarios" |
| Per day in Spain, no overnight stay | EUR 26.67 | "no excedan de 26,67" |
| Per day abroad, no overnight stay | EUR 48.08 | "26,67 ó 48,08 euros" |

- Both conditions are required: a restaurant or hospitality establishment AND electronic payment.

### 5.3 Amortizacion (Depreciation) [T1]

Under simplificada use the table below, which is the whole official table. Under normal use the corporate tax table.

**Tabla de amortizacion simplificada (Agencia Tributaria, Manual de actividades economicas)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/3-impuesto-sobre-renta-personas-fisicas/3_5-estimacion-directa-simplificada/3_5_4-tabla-amortizacion-simplificada.html |
| Grupo 1, buildings and constructions, max 68 years | 3% | "Edificios y otras construcciones" |
| Grupo 2, installations, furniture, fittings, other tangible assets, max 20 years | 10% | "Instalaciones, mobiliario, enseres" |
| Grupo 3, machinery, max 18 years | 12% | "Maquinaria" |
| Grupo 4, transport elements, max 14 years | 16% | "Elementos de Transporte" |
| Grupo 5, data processing equipment and computer systems and programs, max 10 years | 26% | "Equipos para tratamiento de la información" |
| Grupo 6, tools and implements, max 8 years | 30% | "herramientas 30 % 8" |
| Grupo 7, cattle, pigs, sheep, goats, max 14 years | 16% | "Ganado vacuno, porcino" |
| Grupo 8, horses and non-citrus fruit trees, max 25 years | 8% | "Ganado equino y frutales no cítricos" |
| Grupo 9, citrus trees and vines, max 50 years | 4% | "Frutales cítricos y viñedos" |
| Grupo 10, olive groves, max 100 years | 2% | "Olivar" |

- **There is no separate software line.** Computer programs sit in grupo 5 with the hardware. The live Guide's separate software rate, and its second lower transport line, are not in the official table and are removed.

### 5.4 Reduccion por Estimacion Directa Simplificada [T1]

**Turnover limit and the hard-to-justify reduction (articles 28 and 30 Real Decreto 439/2007)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Prior-year turnover under which simplificada applies | EUR 600,000 | "no supere los 600.000 euros" |
| Reduction for hard-to-justify expenses, on net income before it | 5% | "el porcentaje del 5 por ciento sobre el rendimiento neto" |
| Annual ceiling on that reduction | EUR 2,000 | "no pueda superar 2.000 euros" |

- **The ceiling covers more than the reduction.** That annual amount caps deductible provisions AND hard-to-justify expenses together, not the reduction alone.
- The turnover limit is a cliff, tested on the prior year, across all the taxpayer's activities together.

### 5.5 Modelo 130 Computation [T1]

- Rate and exemption are in the quarterly payments table above; the computation, the boxes and a negative quarter are in the `es-estimated-tax` Guide. A negative quarter produces no repayment: an overpayment comes back through the modelo 100.

### 5.6 Filing Deadlines [T1]

- **Modelo 130,** first three quarters: between the 1st and the 20th of April, July and October. Fourth quarter: between the 1st and the 30th of January of the following year. A due date on a Saturday or non-working day moves to the next working day. (Agencia Tributaria, pagos fraccionados: see Sources.)
- **Modelo 100:** the campaign window is set fresh for each year and is not a standing rule. For the Renta 2025 campaign, covering 2025 income, it ran from 8 April to 30 June 2026 inclusive, with direct debit closing on 25 June 2026. Read the Agencia Tributaria campaign page for the year you are filing: do not assume the same dates. (Agencia Tributaria, Renta 2025 manual: see Sources.)
- **Modelo 303 for IVA** follows the same quarterly pattern as the modelo 130.

### 5.7 Penalties [T1]

**Late filing and penalties (Ley 58/2003, articles 27, 28 and 191)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186 |
| Voluntary late filing, from the day the deadline passes, and the same again for each complete month of delay up to twelve | 1% | "igual al 1 por ciento más otro 1 por ciento adicional por cada mes" |
| Voluntary late filing after twelve months, plus interest, penalties excluded | 15% | "el recargo será del 15 por ciento y excluirá las sanciones" |
| Cut in that surcharge where it and the debt are paid on time | 25% | "se reducirá en el 25 por ciento" |
| Penalty for a minor (leve) failure to pay the self-assessed tax | 50% | "leve consistirá en multa pecuniaria proporcional del 50 por ciento" |
| Base of penalty at or below which a failure is minor | EUR 3,000 | "inferior o igual a 3.000 euros" |
| Top of the band for a grave failure | 100% | "proporcional del 50 al 100 por ciento" |
| Top of the band for a very grave failure | 150% | "proporcional del 100 al 150 por ciento" |
| Recargo de apremio reducido | 10% | "apremio reducido será del 10 por ciento" |
| Recargo de apremio ordinario | 20% | "apremio ordinario será del 20 por ciento" |

- **How the three bands are picked.** At or below that base the failure is minor. Above it, it is still minor where there was no concealment, and grave where there was. It is never minor where false invoices were used, where incorrect books affected more than a tenth of the base, or where amounts withheld were not paid over. Fraudulent means make it very grave in every case.

**Enforcement surcharge (Agencia Tributaria)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://sede.agenciatributaria.gob.es/Sede/deudas-apremios-embargos-subastas/apremios/tipos-recargos.html |
| Recargo ejecutivo | 5% | "Recargo ejecutivo: es el 5% del importe principal" |

**Interest for 2026 (Agencia Tributaria, Renta 2025 manual)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/guia-principales-novedades/otras-cuestiones-interes.html |
| Interes de demora | 4.0625% | "el interés de demora en el 4,0625 por 100" |
| Interes legal del dinero | 3.25% | "el interés legal en el 3,25 por 100" |

- **The old ladder is gone.** The live Guide's late-payment ladder of four rising percentages was the pre-2021 late-filing surcharge and no longer exists. Voluntary late filing uses the monthly surcharge above; in enforcement the apremio surcharges apply instead.
- **Both interest rates carry a condition.** They are held over from the last approved Budget and stay until a Budget Law for 2026 takes effect. Date them whenever you quote them.

## Section 6: Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office (Suministros) [T2]

- Deductible share equals the area used for the activity over total area, multiplied by the share in 5.2, and a different percentage is allowed in EITHER direction where proved. It covers water, gas, electricity, telephony and internet. Reviewer: the measurements, whether the room genuinely serves the activity, and whether another percentage can be evidenced.

### 6.2 Vehicle Expenses [T2]

- For IRPF, the portion used in the activity only, supported by records. Input IVA on a vehicle has its own restriction and belongs to the IVA Guide. Reviewer: the business share and the evidence for it.

### 6.3 Estimacion Directa Normal vs Simplificada [T2]

| Feature | Simplificada | Normal |
| --- | --- | --- |
| Turnover limit | The prior-year limit in 5.4 | None |
| Hard-to-justify reduction | Yes, subject to the ceiling in 5.4 | No |
| Depreciation table | Simplified table in 5.3 | Corporate tax table |
| Deductible provisions | Covered by the same ceiling | Computed separately |

Flag for the reviewer where turnover approaches the limit, or where provisions are material.

### 6.4 Minimo Personal y Familiar [T2]

- These amounts do not reduce the base imponible: the scale is applied to them separately and the result subtracted from the gross tax, producing a band taxed at nil. A community may set its own amounts for its half. Reviewer: family situation, ages, disability certificates, and who else claims the same relative.

## Section 7: Excel Working Paper Template

IRPF WORKING PAPER, tax year 2026

A. INGRESOS: A1 rendimientos de actividades economicas; A2 other business income; A3 total ingresos.

B. GASTOS DEDUCIBLES: B1 consumos de explotacion; B2 sueldos y salarios; B3 Seguridad Social del titular; B4 otros gastos de personal; B5 arrendamientos y canones; B6 suministros; B7 servicios profesionales; B8 primas de seguros; B9 gastos financieros; B10 amortizaciones; B11 publicidad; B12 otros gastos deducibles; B13 total gastos.

C. RENDIMIENTO NETO PREVIO (A3 less B13). D. REDUCCION, capped as in 5.4. E. RENDIMIENTO NETO REDUCIDO (C less D).

F. PREPAYMENTS: F1 retenciones; F2 modelo 130 payments; F3 total prepaid.

REVIEWER FLAGS: residence confirmed under article 9; community confirmed and its own scale read; estimation regime confirmed; home office area ratio verified; vehicle business use documented; retenciones certificates reconciled.

## Section 8: Bank Statement Reading Guide

### Spanish Bank Statement Formats

| Bank | Format | Key Fields |
| --- | --- | --- |
| CaixaBank, BBVA, Santander | CSV, PDF | Fecha, Concepto, Importe, Saldo |
| Sabadell, Bankinter | CSV, PDF | Fecha Valor, Descripcion, Cargo/Abono |
| N26, Revolut | CSV | Date, Counterparty, Amount |
| ING Direct | CSV | Fecha, Movimiento, Importe |

### Key Spanish Banking Terms

| Spanish Term | English | Classification Hint |
| --- | --- | --- |
| Ingreso | Credit (incoming) | Potential income |
| Cargo | Debit (outgoing) | Potential expense |
| Transferencia | Bank transfer | Check direction |
| Recibo / Domiciliacion | Direct debit | Regular expense |
| Bizum | Mobile payment | Could be income or expense |
| Reintegro | Cash withdrawal | Ask what it was for |
| Comisiones | Bank charges | Gastos financieros |
| Nomina | Salary payment | Employment income |

## Section 9: Onboarding Fallback

ONBOARDING QUESTIONS, SPAIN IRPF: (1) more than 183 days in Spain last year, or main economic base here? (2) which autonomous community? (3) professional or business activity? (4) directa simplificada or normal? (5) is this the year you started, or one of the two after it? (6) home used for the activity: dedicated room, area ratio? (7) vehicle business share and records? (8) all certificados de retenciones? (9) marital status and dependants, with ages and any disability certificate? (10) contribution amount per month, and prior year modelo 100?

## The method, step by step

1. Settle residence under article 9 Ley 35/2006, then the community under article 72. Someone failing every test is outside this Guide. [Ley 35/2006](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764)
2. Fix the regime. Simplificada applies by default under the prior-year turnover limit in 5.4 unless the taxpayer opted out; modulos is a separate method with its own form. [Real Decreto 439/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820)
3. Build net income: income in the libro registro, less expenses linked to the activity and evidenced, less depreciation from the simplified table in 5.3, then the hard-to-justify reduction under simplificada. (Agencia Tributaria simplified depreciation table: see Sources.)
4. Pay in during the year with modelo 130 by the quarterly deadlines in 5.6, unless the professional exemption applies; mechanics in the `es-estimated-tax` Guide. (Agencia Tributaria, pagos fraccionados: see Sources.)
5. Split income into the general base and the savings base, apply the state scale and the community's own scale to the general base, apply the savings scale, then subtract the tax on the personal and family minimum. [Ley 35/2006](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764)
6. Subtract the retenciones on the certificates and the modelo 130 payments, then file the modelo 100 inside the campaign window published for that year. (Agencia Tributaria, Renta 2025 manual: see Sources.)

## Ask the client first

- Which community were you tax resident in, and did you move during the year? The community half of the scale and its deductions both turn on it, and this Guide supplies neither.
- Professional or business activity? It decides the withholding on your invoices and whether the modelo 130 exemption can apply.
- Is this the year the activity started, or one of the two following it, and had you carried on any professional activity in the year before you started?
- More than 183 days in Spain, and is your main economic base here? If neither, you are on the non-resident tax and none of this applies.
- For meals claimed: taken in a restaurant or hospitality establishment, and paid electronically? Both are conditions, not good practice.
- For a home used for the activity: what are the two areas, and can you evidence a share other than the default?

## When to refuse or refer

- Estimacion objetiva (modulos) and its form. Different method, different rules, and the module limits are themselves contested.
- Anything in Navarra, Araba, Bizkaia or Gipuzkoa. Those territories run their own income tax and forms.
- A non-resident, or a year in which the client arrived or left. Split years, treaty tie-breakers and the inbound worker regime are all outside this Guide.
- Any request for one combined marginal rate for "Spain". Without a named community it cannot be answered, and inventing one is the commonest error in Spanish tax content.
- Property disposals, share sales and other gains needing their own computation.
- A company, or a person taxed through a company. Different tax entirely.

## Section 10: Reference Material

### Key Legislation

| Topic | Reference |
| --- | --- |
| Residence; community residence; filing obligation | Articles 9, 72 and 96 Ley 35/2006 |
| Self-employment income; deductible expenses | Articles 27 to 32, article 30.2 Ley 35/2006; articles 28 to 30 Real Decreto 439/2007 |
| Home supplies and own meals | Article 30.2 rule 5 Ley 35/2006; article 9 Real Decreto 439/2007 |
| Depreciation, simplificada | Agencia Tributaria simplified table |
| Retenciones; modelo 130 | Articles 95, 109 and 110 Real Decreto 439/2007; article 101 Ley 35/2006 |
| Minimums; work reduction | Articles 56 to 61 and article 20 Ley 35/2006 |
| General scale; savings scale | Articles 63, 74 and 66 Ley 35/2006 |
| Surcharges, penalties, interest | Articles 27, 28 and 191 Ley 58/2003 |
| Non-residents | Real Decreto Legislativo 5/2004 |

## PROHIBITIONS

- NEVER give a combined Spanish marginal rate, and never compute IRPF without knowing the community of residence. The community half is not here, and doubling the state scale is not any community's tax.
- NEVER present the payroll withholding scale of article 101 as the income tax brackets.
- NEVER deduct income tax payments (modelo 130, retenciones) as business expenses, and never treat a retencion as a reduction in income.
- NEVER apply modulos rules to a taxpayer in estimacion directa, or foral territory rules to a common territory taxpayer, or the reverse.
- NEVER allow a meal paid in cash, or taken outside a restaurant or hospitality establishment.
- NEVER treat the home supplies share as a fixed ceiling: it is a default, provable either way.
- NEVER allow vehicle costs in full without documented evidence of the business share.
- NEVER forget the hard-to-justify reduction under simplificada, subject to its ceiling, unless the taxpayer has taken the separate reduction that displaces it.
- NEVER present a computation as definitive. Label it an estimate for review.

## Sources

- Ley 35/2006, IRPF: https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764
- Real Decreto 439/2007, Reglamento del IRPF: https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820
- Ley 58/2003, General Tributaria: https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186
- Real Decreto Legislativo 5/2004, no residentes: https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527
- Tabla de amortizacion simplificada: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/3-impuesto-sobre-renta-personas-fisicas/3_5-estimacion-directa-simplificada/3_5_4-tabla-amortizacion-simplificada.html
- Pagos fraccionados, plazos: https://sede.agenciatributaria.gob.es/Sede/irpf/retenciones-ingresos-cuenta-pagos-fraccionados/pagos-fraccionados/plazos-declaracion-ingreso.html
- Plazo y forma de presentacion, Renta 2025: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c01-campana-declaracion-renta/confirmacion-borrador-presentacion-declaraciones/plazo-forma-presentacion.html
- Tipos de recargos del periodo ejecutivo: https://sede.agenciatributaria.gob.es/Sede/deudas-apremios-embargos-subastas/apremios/tipos-recargos.html
- Otras cuestiones de interes: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/guia-principales-novedades/otras-cuestiones-interes.html

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
