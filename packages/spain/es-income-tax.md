---
name: es-income-tax
description: Use this skill whenever asked about Spanish personal income tax (IRPF -- Impuesto sobre la Renta de las Personas Fisicas) for self-employed individuals (autonomos). Trigger on phrases like "how much tax do I pay in Spain", "IRPF", "Modelo 100", "Modelo 130", "pago fraccionado", "estimacion directa", "retencion", "autonomo tax", "rendimientos de actividades economicas", "gastos deducibles", "amortizacion", "minimo personal", "cuota autonomica", or any question about filing or computing income tax for a self-employed or freelance client in Spain. Covers IRPF progressive rates, Modelo 100 structure, estimacion directa normal vs simplificada, deductible expenses, depreciation, quarterly payments (Modelo 130), withholding (retenciones), regional surcharges, personal and family allowances, and interaction with IVA and Social Security. ALWAYS read this skill before touching any Spanish income tax work.
version: 2.0
jurisdiction: ES
tax_year: 2026
last_updated: 2026-09-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spain: income tax (IRPF) for the self-employed (autónomo)

How Spain taxes a self-employed individual under IRPF (Impuesto sobre la Renta de las Personas Físicas) in common territory: residence, the state half of the general scale and where to find the regional half, the savings scale, the personal and family minimum, deductible expenses under estimación directa, the hard-to-justify reduction, módulos limits, withholding on invoices, modelo 130 instalments, the modelo 100 return, and surcharges and penalties.

Primary year: **2026** (calendar year, income earned 1 January to 31 December 2026, returned in spring 2027). A dated section covers the **2025 return**, filed from 8 April to 30 June 2026. Laws were read in the consolidated texts on boe.es in September 2026. No 2026 State Budget Law has been approved, so figures that a Budget Law would normally update (interest rates) are rolled over and dated where used.

## Scope

- **Who.** A natural person resident in Spain for tax purposes who carries on a business or professional activity (actividad económica) as an autónomo, in common territory.
- **Residence.** Article 9 of [Ley 35/2006](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764): resident if **either** (a) more than 183 days in Spain in the calendar year (sporadic absences count unless tax residence elsewhere is proved), **or** (b) the main base or centre of activities or economic interests is in Spain. There is also a rebuttable presumption where the spouse (not legally separated) and minor children live in Spain. A resident is taxed on worldwide income.
- **Which community.** Article 72: the community where the person spent more days of the year; failing that, where the main centre of interests is; failing that, the last declared residence. The community decides the regional half of the scale.
- **Who must file.** Everyone who was registered in RETA (the self-employed Social Security scheme) **at any time** in the year must file, whatever their income. Article 96.2 says they are "en cualquier caso obligadas a declarar".
- **Out of scope** (see "When to refuse or refer"): non-residents, who pay non-resident tax and do not file modelo 100 ([Real Decreto Legislativo 5/2004](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527)); the foral territories; companies; módulos computations.
- **Related Guides.** Social Security contributions (RETA bases, rates and the yearly regularisation): **es-social-contributions**. The box-by-box modelo 130 computation: **es-estimated-tax**.

There is **no single Spanish income tax rate**. The general base is taxed twice: once on the state scale (article 63) and once on the scale of the taxpayer's community (article 74). This Guide gives the state half only. Doubling it is not any community's tax.

## Ask the client first

- **Residence.** More than 183 days in Spain in the year, or main economic base here? Did you arrive or leave during the year? (If not resident, or a split year: refer.)
- **Community.** Which autonomous community did you live in for most of the year? Did you move? Is it Navarra or the Basque Country? (Foral: refer.)
- **Activity type.** Professional (Sections 2 and 3 of the IAE tariffs) or business (Section 1)? This decides withholding on invoices and whether the modelo 130 exemption can apply.
- **Start date.** Did the activity start this year or in the two years before? Did you carry on any professional activity in the year before you started? (Reduced withholding test.)
- **Method.** Estimación directa simplificada, normal, or módulos (estimación objetiva)? Last year's turnover for all activities together? Any renuncia (opt-out) filed?
- **Home.** Do you work from your **main home** (vivienda habitual)? Floor area of the home and of the part used for the activity? Can you prove a share other than the default?
- **Meals.** Were meals taken in restaurants or hospitality businesses, and paid by card or other electronic means? Overnight stay? In Spain or abroad?
- **Prepayments.** All withholding certificates from clients; modelo 130 filings and amounts for the year.
- **Family.** Marital status, joint or individual return, children and parents living with you (ages, their own income, any disability certificate), and who else claims them.
- **Other income.** Salary, rent, interest, dividends, gains. Each goes in its own category.

## The method, step by step

1. **Settle residence and community.** Apply article 9, then article 72, of [Ley 35/2006](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764). Not resident, a split year, or foral territory: stop and refer.
2. **Fix the method for the activity.**
   - Estimación directa simplificada applies by default when the net turnover of all activities together was not more than EUR 600,000 in the previous year, the person is not in módulos, and has not opted out ([Real Decreto 439/2007, art. 28](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820)).
   - Above that, or after an opt-out, estimación directa normal applies.
   - Módulos is a separate method with its own limits (see "Módulos limits" below) and modelo 131. Refer any módulos computation.
3. **Compute net activity income (rendimiento neto).**
   - Income: everything invoiced or earned in the activity, **gross of withholding**. Withholding is a prepayment, not a cost.
   - Less expenses linked to the activity, supported by a proper invoice and entered in the expense book. Special rules for home supplies, own meals and health insurance are in "Deductible expenses" below.
   - Less depreciation. Under simplificada use the simplified table below; under normal, the corporate tax table.
   - Own RETA contributions are a deductible expense of the activity. How the yearly RETA regularisation is booked is in **es-social-contributions**.
4. **Simplificada only: deduct the hard-to-justify reduction.** 5% of net income before this item, capped at EUR 2,000 a year for provisions and hard-to-justify expenses together ([Real Decreto 439/2007, art. 30](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820)). Not under normal. Not if the article 32.2 reduction (economically dependent self-employed and similar) is taken instead. Ceuta exception for 2026 below.
5. **Build the two bases.** Activity income, employment income, rent and most imputed income go to the **general base**. Interest, dividends, insurance returns and gains on transfers go to the **savings base**.
6. **Apply the scales and the minimum.**
   - General base: state scale (below) **and** the community's own scale.
   - From each result, subtract the same scale applied to the personal and family minimum (article 63.1.2º). The minimum is not a deduction from income. It creates a band taxed at nil.
   - Savings base: the savings scale (both halves are set by state law). The minimum sits in the general base first; only where the general base is smaller than the minimum does the rest go to the savings base (article 56.2).
7. **Deduct credits** (state and community deductions). Community deductions: read the community's law.
8. **Deduct prepayments.** Withholding on invoices (per the certificates) and modelo 130 instalments. A negative result is a refund.
9. **File modelo 100** in the campaign window published for that year. Pay in one go or in two instalments (see "Filing and payment").

## Figures by year

### State general scale, 2026 and 2025 (article 63.1, [Ley 35/2006](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764))

Unchanged since 2021. Same for the 2025 and 2026 years. This is the **state half only**.

| Base liquidable general, from | up to | State rate |
| --- | --- | --- |
| EUR 0 | EUR 12,450 | 9.5% |
| EUR 12,450 | EUR 20,200 | 12% |
| EUR 20,200 | EUR 35,200 | 15% |
| EUR 35,200 | EUR 60,000 | 18.5% |
| EUR 60,000 | EUR 300,000 | 22.5% |
| EUR 300,000 | no limit | 24.5% |

State tax at the top of each band (from the law's own table): EUR 1,182.75 at EUR 12,450; EUR 2,112.75 at EUR 20,200; EUR 4,362.75 at EUR 35,200; EUR 8,950.75 at EUR 60,000; EUR 62,950.75 at EUR 300,000.

**The regional half.** Each community approves its own scale under article 74. For **2025**, the Agencia Tributaria Renta 2025 manual prints every community's scale on one page: "Para el ejercicio 2025 cada contribuyente deberá aplicar la escala autonómica que corresponda" ([Agencia Tributaria, gravamen autonómico 2025](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/gravamen-base-liquidable-general/gravamen-autonomico.html)). Residents of Ceuta and Melilla use a scale set in the state law itself. For **2026**, read the community's own law in force for 2026; that manual covers 2025 only.

Do not confuse the tax scale with the payroll withholding scale of article 101. The 19, 24, 30, 37, 45 and 47 per cent steps often sold as "the Spanish brackets" are that withholding scale, not the tax.

### Savings scale, 2026 and 2025 (articles 66.1 and 76, [Ley 35/2006](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764))

State law sets both halves at the same rates: article 66.1 the state half and article 76 the regional half. So the total is the same everywhere in common territory. The top band applies from 2025 (Ley 7/2024).

| Base liquidable del ahorro, from | up to | State half | Regional half | Total |
| --- | --- | --- | --- | --- |
| EUR 0 | EUR 6,000 | 9.5% | 9.5% | 19% |
| EUR 6,000 | EUR 50,000 | 10.5% | 10.5% | 21% |
| EUR 50,000 | EUR 200,000 | 11.5% | 11.5% | 23% |
| EUR 200,000 | EUR 300,000 | 13.5% | 13.5% | 27% |
| EUR 300,000 | no limit | 15% | 15% | 30% |

### Personal and family minimum, 2026 and 2025 (articles 56 to 61, [Ley 35/2006](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764))

These are the **state** amounts. A community may set its own amounts for its half (article 56.3). All amounts are annual.

| Item | Amount | Condition |
| --- | --- | --- |
| Taxpayer | EUR 5,550 | Everyone |
| Taxpayer over 65 | plus EUR 1,150 | Age more than 65 |
| Taxpayer over 75 | plus a further EUR 1,400 | Age more than 75 |
| First descendant | EUR 2,400 | Under 25 (or disabled at any age), lives with the taxpayer, own income (exempt income excluded) not more than EUR 8,000 |
| Second descendant | EUR 2,700 | Same |
| Third descendant | EUR 4,000 | Same |
| Fourth and each later | EUR 4,500 | Same |
| Descendant under three | plus EUR 2,800 | Also for adoption or foster care, in the year of registration and the two following |
| Each ascendant | EUR 1,150 | Over 65 (or disabled at any age), lives with the taxpayer, own income not more than EUR 8,000 |
| Ascendant over 75 | plus EUR 1,400 | |
| Disability of taxpayer | EUR 3,000 | Recognised disability |
| Same, 65% or more | EUR 9,000 | Degree of disability 65% or more |
| Assistance costs | plus EUR 3,000 | Needs help of others or reduced mobility, or 65% or more |
| Disability of each descendant or ascendant | EUR 3,000, or EUR 9,000 at 65% or more | Only for a relative who already gives a minimum |

- **Cliffs, not tapers.** A relative with income above EUR 8,000 gives nothing.
- **Own return.** A descendant or ascendant who files their own return with income above EUR 1,800 gives no minimum at all (article 61).
- **Sharing.** Where two taxpayers qualify for the same relative, the amount is split equally; if their degree of kinship differs, it goes to the closer relative (article 61).

**Joint return reductions** (article 84): married couple unit, EUR 3,400 off the base; single-parent unit, EUR 2,150.

**Work reduction (employment income only, article 20).** It does not apply to activity income. EUR 7,302 where net employment income is at most EUR 14,852, tapering to nil at EUR 19,747.5. It is lost entirely where other income (exempt income excluded) is more than EUR 6,500. Most autónomos with a real activity get none.

### Deductible expenses: special rules for estimación directa (article 30.2 rule 5, [Ley 35/2006](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764))

The general rule: an expense is deductible if it is linked to the activity, backed by a proper invoice, and recorded in the expense book. Three special rules apply in **both** normal and simplificada.

**Home supplies (suministros).**
- Only where part of the taxpayer's **main home** (vivienda habitual) is used for the activity. A second home is not covered by this rule.
- Covers water, gas, electricity, telephone and internet of that home.
- Deductible share: **30%** of the proportion "entre los metros cuadrados de la vivienda destinados a la actividad respecto a su superficie total", "salvo que se pruebe un porcentaje superior o inferior". The 30% is a default, not a cap, and it can be lower too.
- Separate business premises: supplies of those premises are deductible in full under the general rule.

**Own meals (manutención) while working.**
- Both conditions must hold: the meal is taken "en establecimientos de restauración y hostelería", **and** it is paid "utilizando cualquier medio electrónico de pago". Cash fails.
- Capped at the employee per-diem limits of article 9 of [Real Decreto 439/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820):

| Situation | In Spain | Abroad |
| --- | --- | --- |
| With an overnight stay in another municipality | EUR 53.34 a day | EUR 91.35 a day |
| No overnight stay | EUR 26.67 a day | EUR 48.08 a day |

- Entertaining clients is a different expense with its own rules; it is not covered here.

**Health insurance.** Premiums for the taxpayer, spouse and children under 25 living with them: up to EUR 500 a person a year, or EUR 1,500 for a person with a disability.

**Vehicles, phones, other mixed use.** Only the part used in the activity, with records. If the split is unknown, deduct nothing.

**Not expenses.** Modelo 130 payments, withholding, IRPF itself, loan principal, and VAT paid to the tax office (VAT is a separate tax; record amounts net where VAT-registered).

### Hard-to-justify reduction (simplificada only), 2026 and 2025 ([Real Decreto 439/2007, art. 30](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820))

| Item | Figure |
| --- | --- |
| Rate, applied to net income before this item | 5% |
| Annual ceiling | EUR 2,000 |
| Previous-year turnover limit for simplificada | EUR 600,000 |

- **Which years.** The law sets 5%, "sin que la cuantía resultante pueda superar 2.000 euros anuales". The only year-specific change in Ley 35/2006 was for 2023 ("durante el período impositivo 2023, del 7 por ciento"). Nothing changes it for 2024, **2025** or **2026**. So both the 2025 return and 2026 use 5% capped at EUR 2,000.
- **The ceiling covers provisions too.** The EUR 2,000 caps deductible provisions and hard-to-justify expenses together.
- **Not with the article 32.2 reduction.** It does not apply where the taxpayer opts for the reduction in article 32.2 of the Ley (for economically dependent self-employed people and others meeting its conditions), which article 26.1 of the regulation governs. That reduction is outside this Guide: refer.
- **Ceuta, 2026 only.** For activities in Ceuta whose income qualifies for the article 68.4 deduction, the rate is **10%** for 2026 (Ley 35/2006, sixty-fourth additional provision, added by Real Decreto-ley 22/2026 of 1 September 2026, in force 3 September 2026). It counts for 2026 instalments whose filing period starts one month after that date. The EUR 2,000 ceiling is not changed by that provision. A decree-law must be validated by Congress: check that it has been.

### Módulos (estimación objetiva) limits: routing only

Módulos is outside this Guide. The limits matter because exceeding them forces the taxpayer into estimación directa for the following year.

| Limit, measured on the previous year | Permanent text (article 31 [Ley 35/2006](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764)) | Figures applied 2016 to 2024 |
| --- | --- | --- |
| Gross income, all activities except farming | EUR 150,000 | EUR 250,000 |
| Of which invoiced to business or professional customers | EUR 75,000 | EUR 125,000 |
| Farming, livestock and forestry | EUR 250,000 | EUR 250,000 |
| Purchases of goods and services (fixed assets excluded) | EUR 150,000 | EUR 250,000 |

- **2026: no extension is enacted in law.** Real Decreto-ley 16/2025 (23 December 2025) and Real Decreto-ley 2/2026 (3 February 2026) both extended the higher figures, and Congress repealed both. The consolidated law still headlines the transitional rule "ejercicios 2016 a 2024".
- **The Agencia Tributaria position for 2026.** Its note of 1 April 2026, following the Dirección General de Tributos: "Respecto al ejercicio 2026 se mantienen los límites para la aplicación del método de estimación objetiva vigentes en los ejercicios 2016 a 2024" ([Agencia Tributaria note](https://sede.agenciatributaria.gob.es/Sede/todas-noticias/2026/abril/1/nota-sobre-efectos-ambito-tributario-febrero.html)). Opt-outs and revocations filed while either decree-law was in force are valid.
- **2025: check.** The same note does not state the 2025 limits separately. Refer.
- **Módulos for 2026** is set by [Orden HAC/1425/2025](https://www.boe.es/buscar/act.php?id=BOE-A-2025-25272), which keeps a 5% reduction of the módulos net income for 2026.
- **Instalments in módulos** use modelo 131: 4% of módulos income, 3% with one employee, 2% with none ([Real Decreto 439/2007, art. 110](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820)).

### Simplified depreciation table ([Agencia Tributaria, activity manual](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/3-impuesto-sobre-renta-personas-fisicas/3_5-estimacion-directa-simplificada/3_5_4-tabla-amortizacion-simplificada.html))

Simplificada only. Under normal, use the corporate tax table.

| Group | Assets | Maximum straight-line rate | Maximum years |
| --- | --- | --- | --- |
| 1 | Buildings and other constructions | 3% | 68 |
| 2 | Installations, furniture, fittings, other tangible assets | 10% | 20 |
| 3 | Machinery | 12% | 18 |
| 4 | Transport | 16% | 14 |
| 5 | Data processing equipment **and software** | 26% | 10 |
| 6 | Tools and implements | 30% | 8 |
| 7 | Cattle, pigs, sheep, goats | 16% | 14 |
| 8 | Horses, non-citrus fruit trees | 8% | 25 |
| 9 | Citrus trees and vines | 4% | 50 |
| 10 | Olive groves | 2% | 100 |

There is no separate software line: programs sit in group 5 with the hardware.

### Withholding on invoices (retenciones), 2026 and 2025 ([Real Decreto 439/2007, art. 95](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820))

| Case | Rate on gross fees |
| --- | --- |
| Professional activity, standard | 15% |
| Professional starting activity: year of start and the two following | 7% |
| Either rate where the income qualifies for the Ceuta and Melilla deduction (article 68.4) | reduced by 60% |
| Certain módulos activities (article 95.6) | 1% |

- **Who withholds.** A business or professional client paying for **professional** services (Sections 2 and 3 of the IAE tariffs). Business activities in Section 1 are generally not withheld on this way. Private individuals do not withhold.
- **The reduced rate has two conditions.** It applies "en el período impositivo de inicio de actividades y en los dos siguientes", and only if the person did not carry on any professional activity in the year before the start date. The professional must tell the client in writing; the client keeps the signed notice.
- **Other listed activities** (municipal collectors, certain insurance intermediaries, certain artistic activities under EUR 15,000 that are more than 75% of income) also have a reduced rate. Refer.
- **Withholding is a prepayment.** Gross income is the full invoice before withholding. The amount withheld is credited against the final tax.
- **Other income the client may have** (article 101 [Ley 35/2006](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764)): rent of urban property and investment income are withheld at 19%.

### Quarterly instalments (modelo 130), 2026 and 2025 ([Real Decreto 439/2007, arts. 109 and 110](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820))

- **Rate.** 20% of net income from 1 January to the end of the quarter, less earlier instalments of the year and withholding. Box-by-box computation: **es-estimated-tax**.
- **Exemption for professionals.** No modelo 130 for a professional activity if, in the **previous calendar year**, at least 70% of the activity income was subject to withholding. In the year the activity starts, the 70% is measured over the period the instalment covers. A business activity does not get this exemption (farming and forestry have their own 70% test).
- **Deadlines** ([Agencia Tributaria, instalments](https://sede.agenciatributaria.gob.es/Sede/irpf/retenciones-ingresos-cuenta-pagos-fraccionados/pagos-fraccionados/plazos-declaracion-ingreso.html)): first three quarters between the 1st and 20th of April, July and October; fourth quarter between the 1st and 30th of January of the following year. A deadline on a non-working day moves to the next working day. A quarter with nothing to pay still needs a nil return.
- **A negative quarter** gives no refund. Any overpayment comes back through modelo 100.
- **VAT** (modelo 303) follows the same quarterly calendar. It is a separate tax.

### Non-resident rates (routing only, article 25, [Real Decreto Legislativo 5/2004](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527))

General rate 24%; 19% for residents of another EU state, or of an EEA state with effective exchange of tax information. Refer non-residents.

### Surcharges, penalties and interest, 2026 and 2025 ([Ley 58/2003](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186))

**Late filing without a prior request from the tax office (article 27).**

| Delay after the deadline | Surcharge on the amount due |
| --- | --- |
| Up to 12 months | 1%, plus 1% for each **complete** month of delay |
| More than 12 months | 15%, plus late-payment interest from the day after the 12 months end |

- The surcharge replaces penalties ("excluirá las sanciones").
- It is cut by 25% where the surcharge and the tax are paid in full on time (article 27.5).

**Late filing where no tax is lost** (for example a nil or refund return filed late), article 198: a fixed penalty of EUR 200, halved where the return is filed late without a prior request.

**Failure to pay tax due on a self-assessment (article 191).** The base is the tax not paid.

| Level | When | Penalty |
| --- | --- | --- |
| Minor (leve) | Base EUR 3,000 or less, or more but no concealment | 50% |
| Serious (grave) | Base more than EUR 3,000 **and** concealment; or false invoices; or books wrong by more than 10% and up to 50% of the base; or withholding not paid over of up to 50% of the base | 50% to 100% |
| Very serious (muy grave) | Fraudulent means, in every case; or withholding not paid over of more than 50% of the base | 100% to 150% |

- It is never minor where false invoices were used, books were wrong by more than 10% of the base, or withheld amounts were not paid over.
- **Reductions (article 188):** 30% for agreement (conformidad); then a further 40% for paying the penalty on time without appeal.

**Enforcement surcharges (article 28, and [Agencia Tributaria](https://sede.agenciatributaria.gob.es/Sede/deudas-apremios-embargos-subastas/apremios/tipos-recargos.html)).**

| Surcharge | Rate | When |
| --- | --- | --- |
| Recargo ejecutivo | 5% | Whole debt paid before the enforcement notice |
| Recargo de apremio reducido | 10% | Debt and surcharge paid within the period in the enforcement notice |
| Recargo de apremio ordinario | 20% | Otherwise, plus interest |

**Interest for 2026** ([Agencia Tributaria, Renta 2025 manual](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/guia-principales-novedades/otras-cuestiones-interes.html)): late-payment interest (interés de demora) 4.0625%; legal interest 3.25%. Same as 2025. They stay until a 2026 Budget Law takes effect, so date them when you quote them.

## Boundaries and exceptions ([Ley 35/2006](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764))

| Situation | Rule | Source |
| --- | --- | --- |
| Exactly 183 days in Spain | Not "more than 183": the day test is not met. Check the economic-interests test and the family presumption | [Ley 35/2006, art. 9](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764) |
| Previous-year turnover exactly EUR 600,000 | Simplificada still applies ("no supere"). One euro more and it does not, for the following year | [RD 439/2007, art. 28](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820) |
| 5% of net income is more than EUR 2,000 | Use EUR 2,000. The cap is annual and also covers provisions | [RD 439/2007, art. 30](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820) |
| Working from a second home or rented studio | The 30% home-supplies rule does not apply (main home only). Separate premises: general rule, supplies deductible where linked to the activity | [Ley 35/2006, art. 30.2](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764) |
| Meal paid in cash, or bought at a supermarket | Not deductible under the meals rule | [Ley 35/2006, art. 30.2](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764) |
| Meal costs more than the daily limit | Only the limit is deductible | [RD 439/2007, art. 9](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820) |
| Relative's own income exactly EUR 8,000 | Still counts ("superiores a 8.000"). One euro more and the minimum is lost | [Ley 35/2006, arts. 58 and 59](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764) |
| Professional who had a professional activity the year before starting again | No reduced withholding: standard rate | [RD 439/2007, art. 95](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820) |
| Exactly 70% of last year's professional income withheld | Exempt from modelo 130 ("al menos el 70 por ciento") | [RD 439/2007, art. 109](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820) |
| Return filed late, exactly 12 months after the deadline | Still the monthly scale; the 15% applies only once more than 12 months have passed | [Ley 58/2003, art. 27](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186) |
| Tax not paid, base exactly EUR 3,000 | Minor ("inferior o igual a 3.000 euros"), unless one of the aggravating cases applies | [Ley 58/2003, art. 191](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186) |
| Activity in Ceuta qualifying for the article 68.4 deduction, 2026 | Hard-to-justify rate 10% instead of 5%, and withholding reduced by 60%. Check the decree-law was validated | [Ley 35/2006, 64th additional provision](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764) |
| Módulos taxpayer whose previous-year income is between the permanent and the 2016-2024 limits | For 2026 the Agencia Tributaria keeps the higher limits; the law text has no extension. Refer | [Agencia Tributaria note](https://sede.agenciatributaria.gob.es/Sede/todas-noticias/2026/abril/1/nota-sobre-efectos-ambito-tributario-febrero.html) |

**Defaults when a fact is missing.** Unknown community: give the state half only and say the regional half is missing. Unknown method: simplificada. Unknown business-use share (car, phone, home): no deduction. Unknown expense type: not deductible. Unknown whether professional or business: professional. Unknown withholding rate: the standard rate. Unknown residence: ask; never assume it from a Spanish address.

**Classifying bank lines.** Salary (nómina) is employment income, not activity income. Interest and dividends go to the savings base. Rent received is property income. Tax refunds (devolución Hacienda), modelo 130 and IRPF payments, VAT payments, loan principal and transfers between own accounts are not income or expenses. Bank and card fees and business loan interest are expenses. Card processor payouts (Stripe, PayPal) are income gross of the fees they keep; the fees are expenses.

## Worked cases ([Ley 35/2006](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764); [Real Decreto 439/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820))

Amounts are sample data. Rates come from the tables above. Every case is an estimate for review, not a final computation.

**Case 1: IT consultant, simplificada, 2026.**
- Invoiced EUR 55,000 to business clients, all with 15% withholding.
- Expenses: office rent EUR 6,000; own RETA contributions EUR 4,200; accountant EUR 1,200; software EUR 800; travel EUR 2,000. Total EUR 14,200.
- Net income before the reduction: EUR 55,000 less EUR 14,200 = EUR 40,800.
- Reduction: 5% of EUR 40,800 is EUR 2,040, above the ceiling, so EUR 2,000.
- Net activity income: EUR 38,800. It goes to the general base.
- Withheld by clients: 15% of EUR 55,000 = EUR 8,250, credited against the final tax.

**Case 2: home office in the main home, 2026.**
- Home 80 square metres; room used only for the activity 12 square metres. Share of area: 12 / 80 = 15%.
- Deductible share: 30% of 15% = 4.5% of each bill.
- Bills: electricity EUR 1,200, gas EUR 600, water EUR 300, internet EUR 480.
- Deductible: EUR 54 + EUR 27 + EUR 13.50 + EUR 21.60 = EUR 116.10.
- If the client can prove a different share (for example a separate meter), use that instead, higher or lower.

**Case 3: meals, 2026.**
- Day 1, work trip in Spain, no overnight stay, lunch in a restaurant EUR 32 paid by card: deductible EUR 26.67 (the daily limit).
- Day 2, same trip type, lunch EUR 20 paid in cash: deductible nil (not paid electronically).
- Total deductible: EUR 26.67.

**Case 4: reconciling prepayments on the return.**
- Final tax (state and regional halves) EUR 10,500.
- Withholding certificates EUR 8,250; modelo 130 paid EUR 4,000. Total prepaid EUR 12,250.
- Result: EUR 12,250 less EUR 10,500 = EUR 1,750 refund.

**Case 5: new professional's invoice, 2026.**
- Started in March 2026, no professional activity in 2025, gave the client the signed notice. Invoice EUR 2,000.
- Withholding: 7% of EUR 2,000 = EUR 140.
- In 2027 and 2028 the 7% still applies; from 2029, 15%.

**Case 6: late return with tax to pay.**
- Modelo 100 with EUR 1,000 to pay, filed without any request 3 complete months after 30 June (plus some days).
- Surcharge: 1% + 3 x 1% = 4% of EUR 1,000 = EUR 40. No penalty.
- If the surcharge and the tax are paid in full on time: cut by 25%, so EUR 30.

## When to refuse or refer

- **Any request for one combined "Spanish rate"** without a named community. It cannot be answered; inventing one is the commonest error in Spanish tax content.
- **The regional half of the scale, regional minimums and regional deductions** for 2026. Read the community's own law.
- **Módulos (estimación objetiva)**: computations, modelo 131, and any case near the limits. The 2026 limits rest on an administrative position, not an enacted extension.
- **Foral territories**: Navarra, Araba/Álava, Bizkaia, Gipuzkoa.
- **Non-residents, arrival or departure years**, treaty tie-breakers, and the special regime for workers moving to Spain.
- **The article 32.2 reduction** for economically dependent self-employed people and similar.
- **Ceuta and Melilla** activities: the 60% withholding cut, the 10% Ceuta rate for 2026 and the article 68.4 deduction.
- **Property disposals, share sales** and other gains needing their own computation.
- **Companies**, or a person taxed through a company (corporate tax).
- **Penalty proceedings** already opened by the tax office, and any case involving false invoices or unpaid withholding.

## Filing and payment

### 2026 income (return filed in 2027)

- **Form:** modelo 100, filed online through the Agencia Tributaria electronic office (Renta WEB), by phone, or in person where the office allows.
- **When:** the campaign window is set each year by ministerial order. The window for the 2026 return had not been published when this Guide was written. Do not assume the 2025 dates.
- **Instalments during 2026:** modelo 130 by 20 April, 20 July and 20 October 2026, and 30 January 2027 (see above). 30 January 2027 is a Saturday, so under the non-working-day rule that period runs to the next working day.

### 2025 income (return filed in 2026) ([Agencia Tributaria, Renta 2025 manual](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c01-campana-declaracion-renta/confirmacion-borrador-presentacion-declaraciones/plazo-forma-presentacion.html))

- **Filing window:** "entre los días 8 de abril hasta el 30 de junio de 2026, ambos inclusive", whatever the result. The window has closed; a 2025 return filed now is late (see surcharges).
- **Direct debit:** "hasta el 25 de junio de 2026".
- **Two instalments** ([Agencia Tributaria, modelo 100 manual](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-ayuda-presentacion/irpf-2025/3-cuestiones-generales/3_3-declaracion-irpf/3_3_4-fraccionamiento-pago-domiciliacion.html)): 60% when filing and 40% "hasta el 5 de noviembre de 2026 inclusive", with no interest or surcharge. Only if the return was filed within the window and 60% was paid then. Not available for a supplementary return. If the first 60% is not paid on time, enforcement starts for the whole amount. The second instalment alone could be set up for direct debit until 30 June 2026.
- **Same rules as 2026** for the state scale, savings scale, minimums, 5% capped at EUR 2,000, withholding, modelo 130 and penalties. The 2025 regional scales are in the Agencia Tributaria page linked under "The regional half".
- **RETA regularisation** notices for 2025 arrive after this return: booking them is in **es-social-contributions**.
- **Mistakes on a filed 2025 return:** a supplementary return (autoliquidación complementaria) where more tax is due; a rectification request where too much was paid.

## Completion checklist ([Real Decreto 439/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820))

- [ ] Residence confirmed (article 9) and community confirmed (article 72); not foral, not a split year.
- [ ] Filing duty confirmed (RETA registration at any time in the year means a return).
- [ ] Method confirmed: simplificada, normal or módulos; previous-year turnover checked against EUR 600,000.
- [ ] Income taken gross of withholding and reconciled to invoices and certificates.
- [ ] Every expense linked to the activity, invoiced and recorded; mixed-use items split with evidence.
- [ ] Home supplies: main home only; areas measured; 30% default or proven share.
- [ ] Meals: restaurant or hospitality, electronic payment, within the daily limits.
- [ ] Depreciation from the simplified table (simplificada) or corporate table (normal).
- [ ] Hard-to-justify reduction 5%, capped at EUR 2,000 (simplificada only; Ceuta 2026: refer).
- [ ] Bases split: general and savings.
- [ ] State scale applied; community scale read from the community's law and applied; minimum applied through the scale, not deducted from income.
- [ ] Withholding certificates and modelo 130 payments deducted.
- [ ] Filing window and payment option (single or 60/40) confirmed for the year.
- [ ] Output labelled as an estimate for review by a qualified adviser (asesor fiscal).

## Disclaimer

This Guide is for information and computation only and is not tax, legal or financial advice. Outputs must be reviewed by a qualified professional (such as an asesor fiscal) before filing or acting on them.

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
