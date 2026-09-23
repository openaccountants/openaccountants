---
name: spain-payroll
description: Use this skill whenever asked about Spanish payroll processing for employees. Trigger on phrases like "Spanish payroll", "nómina España", "IRPF retención", "retenciones nómina", "Seguridad Social cotización", "contingencias comunes", "base de cotización", "Salario Mínimo Interprofesional", "SMI", "paga extra", "tredicesima España", "Agencia Tributaria retención", "modelo 111", "modelo 190", "Sistema RED", "Siltra", "TC1 TC2", "RLC RNT", "MEI cotización", "cuota solidaridad", "bruto neto España", "despido indemnización", "FOGASA", or any question about computing employee pay, income tax withholding, or social security contributions in Spain. This skill covers IRPF withholding, Seguridad Social contributions (employee and employer), mandatory benefits, nómina (payslip) requirements, filing obligations, and employer cost analysis. ALWAYS read this skill before processing any Spanish employee payroll.
version: 1.0
jurisdiction: ES
tax_year: 2026
last_updated: 2026-09-23
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spain: running payroll for an employee (nómina)

How a Spanish employer turns gross pay into net pay: the payslip and the parts the law makes compulsory, the general regime contribution bases and rates on both sides, the minimum wage, the IRPF withholding rate and how it is worked out, the pagas extraordinarias, the finiquito, and the two filing channels, Sistema RED for Social Security and the Agencia Tributaria for withholding. Figures are for tax year 2026. Two pages carry another year and are named where used: the Agencia Tributaria page giving the annual summary window states "del 1 de enero al 2 de febrero de 2026", which is the summary of 2025 pay filed in 2026, and the Social Security page on temporary incapacity carries no year at all. There is no Budget Law for 2026, so the contribution ceiling and the solidarity rates come from Real Decreto-ley 3/2026 through Orden PJC/297/2026 and hold until a Budget Law is approved. This Guide does not carry any autonomous community figure: the communities set their own half of the income tax scale, and that half does not enter payroll withholding at all.

## Section 1: Quick reference

| Field | Value |
| --- | --- |
| Country | Spain |
| Currency | EUR only |
| Standard pay frequency | Monthly. The payslip refers to natural months (article 1.2 of the Orden of 27 December 1994) |
| Tax year | Calendar year, 1 January to 31 December |
| Income tax withheld from pay | IRPF retención, a personalised rate worked out under articles 82 to 87 of the IRPF regulation |
| Social insurance body | Tesorería General de la Seguridad Social (TGSS) |
| Tax authority | Agencia Estatal de Administración Tributaria (AEAT) |
| Contribution rules for this year | Orden PJC/297/2026, applying from 1 January 2026 |
| Minimum wage for this year | Real Decreto 126/2026, of 18 February, effects from 1 January to 31 December 2026 |
| Core labour law | Estatuto de los Trabajadores (Real Decreto Legislativo 2/2015) |
| Core social security law | Ley General de la Seguridad Social (Real Decreto Legislativo 8/2015) |
| Payslip model | Annex to the Orden of 27 December 1994, as amended by Orden ESS/2098/2014 |
| Contributor | Open Accountants |
| Validated by | Pending. Requires sign-off by a Spanish asesor fiscal, gestor administrativo or graduado social |
| Validation date | Pending |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown contribution group | Ask. The minimum base differs by group, Section 3 |
| Unknown contract type, permanent or fixed-term | Ask. The unemployment rate differs, Sections 3 and 4 |
| Unknown family situation for withholding | STOP. The rate cannot be worked out without it, Section 2 |
| Unknown collective agreement | Ask which convenio colectivo applies. It can raise every minimum here |
| Unknown activity for the accident premium | STOP. The premium comes from a tariff by activity, Section 4 |

## Section 2: Income tax withholding (IRPF retención)

The employer does not apply an income tax scale to the month's pay. It works out one personalised percentage for the year under the procedure in articles 82 to 87 of the IRPF regulation, applies that percentage to every payment, and regularises it when the facts change. The five steps in article 82 are: the base for calculating the rate (article 83), the personal and family minimum for calculating the rate (article 84), the withholding quota (article 85), the rate itself (article 86), and then the rate applied to the total pay.

The scale below is used only inside step three. It is the withholding reference scale of article 101 of Ley 35/2006, reproduced in article 85 of the regulation. **It is not the Spanish income tax scale.** The income tax scale is in two halves, a state half and an autonomous community half, and neither half is this table. The `es-income-tax` Guide sets that out. A Guide, or an assistant, that prints this table as "the Spanish tax brackets" is wrong.

### IRPF withholding scale, 2026 (not the income tax brackets)

**Scale applied to the base for calculating the rate (article 85 Real Decreto 439/2007)**

| Band of the base for calculating the rate | Rate on the band | Withholding quota at the foot of the previous bands |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Up to EUR 12,450 | 19.00% | EUR 0.00 |
| Over EUR 12,450 up to EUR 20,200 | 24.00% | EUR 2,365.50 |
| Over EUR 20,200 up to EUR 35,200 | 30.00% | EUR 4,225.50 |
| Over EUR 35,200 up to EUR 60,000 | 37.00% | EUR 8,725.50 |
| Over EUR 60,000 up to EUR 300,000 | 45.00% | EUR 17,901.50 |
| Over EUR 300,000 | 47.00% | EUR 125,901.50 |

Step three applies this scale twice: once to the base for calculating the rate, and once to the personal and family minimum, and subtracts the second result from the first. The difference cannot go below zero. Step four divides that quota by the total pay and multiplies by one hundred, expressed to two decimals. Where the base for calculating the rate minus the personal and family minimum is zero or negative, the rate is zero.

The Agencia Tributaria publishes a "Servicio de Cálculo de Retenciones" for payers of employment income, linked in Sources. Use it, or payroll software that implements articles 82 to 87, rather than working the scale by hand.

### Key IRPF parameters

**Minimum and maximum withholding rates, and the mortgage reduction (articles 85 and 86 Real Decreto 439/2007)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Floor, contracts or relationships of less than a year, and the special relationship of performing arts, audiovisual and music workers | 2% | "no podrá ser inferior al 2 por ciento cuando se trate de contratos o relaciones de duración inferior al año" |
| Floor, other special employment relationships of a dependent character | 15% | "ni inferior al 15 por ciento cuando los rendimientos del trabajo se deriven de otras relaciones laborales especiales" |
| First of those two floors for pay obtained in Ceuta and Melilla that qualifies for the article 68.4 credit | 0.8% | "Los citados porcentajes serán el 0,8 por ciento y el 6 por ciento" |
| The second Ceuta and Melilla floor | 6% | "serán el 0,8 por ciento y el 6 por ciento, respectivamente" |
| Cap on the withholding quota, applied to the excess of total pay over the worker's own no withholding threshold, where total pay does not exceed the figure in the next row | 43% | "tendrá como límite máximo el resultado de aplicar el porcentaje del 43 por ciento a la diferencia positiva entre el importe de la cuantía total de retribución y el que corresponda, según su situación, de los mínimos excluidos de retención previstos en el artículo 81" |
| Pay for the year at or below which that cap operates | EUR 35,200 | "no superior a 35.200 euros anuales" |
| Pay for the year below which a notified mortgage on the main home, where the worker still qualifies for the transitional housing investment deduction, cuts the rate by two points | EUR 33,007.2 | "sea inferior a 33.007,2 euros y el contribuyente" |

The fifteen per cent floor and its six per cent Ceuta and Melilla version do not apply to pay obtained by prisoners in penal institutions, nor to special employment relationships affecting people with a disability. The two per cent floor and its Ceuta and Melilla version are not disapplied by that paragraph. For pay obtained in Ceuta and Melilla that qualifies for the article 68.4 credit, the ordinary withholding percentage is itself cut by sixty per cent before the two floors above are tested. The cap in article 85.3 is not a cap on pay: it caps the withholding quota at forty three per cent of the amount by which the year's total pay exceeds the figure for that worker's family situation in the no withholding table below. For a worker on the minimum wage that is what keeps the rate near zero. The mortgage reduction is two whole points and cannot take the rate below zero.

**Personal and family minimum used in step two (Ley 35/2006)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Taxpayer, general amount | EUR 5,550 | "El mínimo del contribuyente será, con carácter general, de 5.550 euros anuales" |
| Increase where the taxpayer is over 65 | EUR 1,150 | "Cuando el contribuyente tenga una edad superior a 65 años, el mínimo se aumentará" |
| Further increase where the taxpayer is over 75 | EUR 1,400 | "Si la edad es superior a 75 años, el mínimo se aumentará adicionalmente en 1.400" |
| First descendant | EUR 2,400 | "2.400 euros anuales por el primero" |
| Second descendant | EUR 2,700 | "2.700 euros anuales por el segundo" |
| Third descendant | EUR 4,000 | "4.000 euros anuales por el tercero" |
| Fourth and later descendants | EUR 4,500 | "4.500 euros anuales por el cuarto y siguientes" |
| Increase for a descendant under three | EUR 2,800 | "el mínimo a que se refiere el apartado 1 anterior se aumentará en 2.800 euros" |
| Ascendant living with the taxpayer, over sixty five or with a disability at any age | EUR 1,150 | "El mínimo por ascendientes será de 1.150 euros anuales" |
| Disability of the taxpayer | EUR 3,000 | "El mínimo por discapacidad del contribuyente será de 3.000 euros anuales" |
| Disability of the taxpayer, degree of 65 per cent or more | EUR 9,000 | "9.000 euros anuales cuando sea una persona con discapacidad y acredite un grado" |
| Added to the disability minimum where the person needs help from others, has reduced mobility, or has a degree of disability of sixty five per cent or more | EUR 3,000 | "en concepto de gastos de asistencia, en 3.000 euros anuales cuando acredite" |
| Income ceiling above which a relative stops counting | EUR 8,000 | "no tenga rentas anuales, excluidas las exentas, superiores a 8.000 euros" |

Two rules change these amounts when they are used for withholding rather than for the annual return. Article 84 of the IRPF regulation says the payer ignores the circumstance in article 61.2.ª of Ley 35/2006, and that **descendants count by half, unless the worker is exclusively entitled to the whole family minimum for that child**. A married worker whose partner also works therefore carries half of each descendant amount above, not all of it. Using the full amounts sets the rate too low for the whole year and the shortfall lands on the worker's own return.

Each descendant amount requires the descendant to be under twenty five, or of any age with a disability, to live with the taxpayer and to have annual income within the ceiling in the last row.

**Employment income deductions that reduce the base in step one (Ley 35/2006)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Other expenses, flat amount | EUR 2,000 | "En concepto de otros gastos distintos de los anteriores, 2.000 euros anuales" |
| Increase for an active worker with a disability | EUR 3,500 | "trabajadores activos, se incrementará dicha cuantía en 3.500 euros anuales" |
| Net employment income at or below which the reduction is at its maximum | EUR 14,852 | "iguales o inferiores a 14.852 euros: 7.302 euros anuales" |
| That maximum reduction | EUR 7,302 | "iguales o inferiores a 14.852 euros: 7.302 euros anuales" |
| Net employment income above which the maximum reduction starts to taper, by one euro and seventy five cents for each euro above the previous row | EUR 17,673.52 | "superiores a 14.852 euros, pero iguales o inferiores a 17.673,52 euros: 7.302 euros menos el resultado de multiplicar por 1,75" |
| Reduction at that point, tapering by one euro and fourteen cents for each euro above it until the reduction reaches nil | EUR 2,364.34 | "comprendidos entre 17.673,52 y 19.747,5 euros: 2.364,34 euros menos el resultado de multiplicar por 1,14" |
| Net employment income at or above which no reduction is due | EUR 19,747.5 | "rendimientos netos del trabajo inferiores a 19.747,5 euros" |
| Ceiling on other income, above which the reduction is lost | EUR 6,500 | "siempre que no tengan rentas, excluidas las exentas, distintas de las del trabajo" |

Net employment income here means gross employment income less the expenses in article 19.2 letters a) to e), and the reduction may not turn the result negative.

The worker's own Social Security contributions are also subtracted in step one, which is why the contribution figures in Sections 3 and 5 feed the withholding rate as well as the payslip.

### SMI and IRPF exemption: the old rule no longer holds

**A full-time minimum-wage worker can now suffer IRPF withholding.** The annual minimum wage floor in Section 5 is above the "otras situaciones" threshold with no children in the table below. The previous version of this Guide said that minimum-wage earners are generally exempt. That is no longer safe to say. Compare the client's expected annual pay with the right cell below before telling anyone their rate is zero.

**Pay below which no withholding is made, by family situation (article 81 Real Decreto 439/2007)**

| Family situation and number of children | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Situation 1, single, widowed, divorced or legally separated, one child | EUR 17,644 | "17.644 18.694 2.ª Contribuyente cuyo cónyuge no obtenga rentas" |
| Situation 1, two or more children | EUR 18,694 | "18.694 2.ª Contribuyente cuyo cónyuge no obtenga rentas superiores" |
| Situation 2, spouse with income of EUR 1,500 or less, no children | EUR 17,197 | "excluidas las exentas. 17.197 18.130 19.262" |
| Situation 2, one child | EUR 18,130 | "excluidas las exentas. 17.197 18.130 19.262" |
| Situation 2, two or more children | EUR 19,262 | "excluidas las exentas. 17.197 18.130 19.262" |
| Situation 3, other situations, no children | EUR 15,876 | "3.ª Otras situaciones. 15.876 16.342 16.867" |
| Situation 3, one child | EUR 16,342 | "3.ª Otras situaciones. 15.876 16.342 16.867" |
| Situation 3, two or more children | EUR 16,867 | "3.ª Otras situaciones. 15.876 16.342 16.867" |
| Add for a pension or passive benefit | EUR 600 | "Los importes previstos en el cuadro anterior se incrementarán en 600 euros" |
| Add for an unemployment benefit or subsidy | EUR 1,200 | "y en 1.200 euros para prestaciones o subsidios por desempleo" |

This table does not help a worker who is inside one of the minimum rate cases. Article 81.3 says the exclusion does not apply where the fixed rates of article 80.1 numbers 3, 4 and 5 or the minimum rates of article 86.2 are the ones that govern. A worker on a contract of less than a year is therefore withheld at no less than the two per cent floor above even where the year's pay is below the figure in this table.

### From gross to net (bruto a neto)

Work in this order. Each step names where its figures come from.

1. **Total devengado.** Add the salary payments (salario base, complementos, overtime, pagas extraordinarias, pay in kind) and the non-salary payments (allowances, Social Security benefits paid on the employer's behalf, travel expenses). Article 26 of the Estatuto de los Trabajadores defines salary; pay in kind may not exceed thirty per cent of the worker's salary payments and may never cut the cash minimum wage.
2. **Base de cotización por contingencias comunes.** Article 147.1 of the Ley General de la Seguridad Social: the total monthly remuneration, in cash or in kind, with payments falling due at more than monthly intervals spread over the twelve months of the year. Article 147.2 lists the only items left out. Then apply the group minimum and the ceiling in Section 3.
3. **Base de cotización por contingencias profesionales.** The same computation, with overtime added, capped by the ceiling and floored by the accident and occupational disease minimum in Section 3.
4. **Employee deductions.** Apply the employee rates in Section 3 to the right base, plus the intergenerational equity mechanism, plus the solidarity contribution on any part of pay above the ceiling.
5. **IRPF retención.** Apply the rate from this section to the total devengado. The payslip must state the percentage applied.
6. **Back pay from earlier years.** Back pay that belongs to an earlier year is not part of the pay used to set the rate under article 83.2, and article 101.1 of Ley 35/2006 gives it a fixed withholding percentage of its own. Do not fold a convenio back payment into the year's rate.
7. **Other deductions.** Advances already paid, the value of goods received in kind, and anything else lawfully deducted.
8. **Líquido total a percibir.** Total devengado less the deductions in steps four to seven.

All tax and Social Security charges falling on the worker are paid by the worker, and any agreement to the contrary is void (article 26.4 of the Estatuto de los Trabajadores). The employer deducts the worker's share when it pays; if it fails to deduct then, it may not deduct later and must pay the whole contribution itself (article 142.2 of the Ley General de la Seguridad Social).

## Section 3: Social security, employee deductions (2026)

### Contribution rates (Régimen General: employee share)

**Employee share of each rate (Orden PJC/297/2026)**

| Concept | Employee share | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296 |
| Contingencias comunes | 4.70% | "el 23,60 por ciento será a cargo de la empresa y el 4,70 por ciento, a cargo de" |
| Desempleo, permanent contract, and the fixed-term cases listed below | 1.55% | "del que el 5,5 por ciento será a cargo de la empresa y el 1,55 por ciento, a cargo" |
| Desempleo, other fixed-term contracts | 1.60% | "8,30 por ciento, del que el 6,70 por ciento será a cargo del empresario y el 1,60" |
| Formación profesional | 0.10% | "el 0,70 por ciento, del que el 0,60 por ciento será a cargo de la empresa y el 0,10" |
| Mecanismo de equidad intergeneracional | 0.15% | "del que el 0,75 por ciento será a cargo del empleador y el 0,15 por ciento, a cargo" |

The lower rate is not only for permanent contracts. The order applies it to permanent contracts including part time and fijo discontinuo, and also to training in alternance and apprenticeship contracts still running, the contract for obtaining professional practice, the relevo contract, substitution contracts, interinidad contracts still running, and any contract whatever its form with a worker with a recognised disability of thirty three per cent or more. A fixed-term substitution contract is on the lower rate, not the higher one.

**This Guide states no employee total.** The order prints the total and both shares for every shared rate, and it prints no combined employee percentage. Adding the shares yourself produces a number no official page carries, and it will be wrong the moment one part does not apply. Read the total from the payslip.

The intergenerational equity mechanism applies to the base for common contingencies. Accident and occupational disease contributions are borne by the employer alone and are never deducted from the worker.

### Cotización adicional de solidaridad (2026)

This is charged on the part of pay above the monthly ceiling, not on the whole of pay. The rates below are the 2026 rates set by the order and by Real Decreto-ley 3/2026. Article 19 bis of the Ley General de la Seguridad Social prints a different, higher set of rates with bands expressed as percentages of the ceiling: those are the end point of a ramp that runs to 2045, not this year's figures. Always use the yearly order. The same table is used by the `es-social-contributions` Guide.

**Solidarity contribution 2026 (Orden PJC/297/2026)**

| Part of pay | Total rate | Employer and employee shares |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296 |
| From EUR 5,101.21 to EUR 5,611.32 | 1.15% | employer 0.96%, employee 0.19% |
| From EUR 5,611.33 to EUR 7,651.80 | 1.25% | employer 1.04%, employee 0.21% |
| Above EUR 7,651.80 | 1.46% | employer 1.22%, employee 0.24% |

For artists the order makes this contribution definitive for the employer and provisional for the worker, regularised at the end of the year. For bullfighting professionals it is regularised at the end of the year for employer and worker alike. For everyone else it says nothing of the kind.

### Bases de cotización (2026)

The base sits between a minimum that depends on the contribution group and a ceiling that does not. Groups 1 to 7 are expressed per month, groups 8 to 11 per day.

**Minimum and maximum bases by contribution group, from 1 January 2026 (article 3 Orden PJC/297/2026)**

| Contribution group | Minimum base | Maximum base |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296 |
| 1 Ingenieros y Licenciados, and senior management outside article 1.3.c) of the Estatuto | EUR 1,989.30 per month | EUR 5,101.20 per month |
| 2 Ingenieros Técnicos, Peritos y Ayudantes Titulados | EUR 1,649.70 per month | EUR 5,101.20 per month |
| 3 Jefes Administrativos y de Taller | EUR 1,435.20 per month | EUR 5,101.20 per month |
| 4 Ayudantes no Titulados | EUR 1,424.40 per month | EUR 5,101.20 per month |
| 5 Oficiales Administrativos | EUR 1,424.40 per month | EUR 5,101.20 per month |
| 6 Subalternos | EUR 1,424.40 per month | EUR 5,101.20 per month |
| 7 Auxiliares Administrativos | EUR 1,424.40 per month | EUR 5,101.20 per month |
| 8 Oficiales de primera y segunda | EUR 47.48 per day | EUR 170.04 per day |
| 9 Oficiales de tercera y Especialistas | EUR 47.48 per day | EUR 170.04 per day |
| 10 Peones | EUR 47.48 per day | EUR 170.04 per day |
| 11 Workers under eighteen, whatever their category | EUR 47.48 per day | EUR 170.04 per day |

The accident and occupational disease floor is the minimum wage increased by one sixth, subject to the amount the order names, and the Social Security table prints that floor as the same amount as the group 4 to 7 minimum above. Use the printed figure. The ceiling is the same figure for every group and is also the ceiling of the self-employed regime, so a number seen in a self-employed working paper may be this same ceiling wearing another label.

**Minimum hourly bases for part-time work, and the charge on very short contracts (Social Security, bases and rates 2026)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/CotizacionRecaudacionTrabajadores/36537 |
| Minimum hourly base, group 1 | EUR 11.98 | "GRUPO COTIZACIÓN BASE MÍNIMA/HORA 1 11,98" |
| Minimum hourly base, group 2 | EUR 9.94 | "1 11,98 2 9,94" |
| Minimum hourly base, group 3 | EUR 8.65 | "2 9,94 3 8,65" |
| Minimum hourly base, groups 4 to 11 | EUR 8.58 | "3 8,65 4 a 11 8,58" |
| One-off employer charge on a fixed-term contract of less than thirty days | EUR 33.62 | "Los contratos de duración determinada por tiempo inferior a 30 días tendrán una" |

Article 28.2 excepts a list of cases from this charge: workers in the special system for agricultural employees and in the special system for domestic employees, both inside the general regime, workers in the special regime for coal mining, and the special employment relationship of performers in the performing, audiovisual and musical arts together with those doing the technical or auxiliary work that activity needs, and it excepts contratos por sustitucion. It does not apply to training in alternance or apprenticeship contracts still running either. A short substitution contract therefore carries no charge.

## Section 4: Social security, employer contributions (2026)

### Contribution rates (Régimen General: employer share)

**Employer share of each rate (Orden PJC/297/2026)**

| Concept | Employer share | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296 |
| Contingencias comunes | 23.60% | "el 23,60 por ciento será a cargo de la empresa y el 4,70 por ciento, a cargo de" |
| Desempleo, permanent contract, and the fixed-term cases listed below | 5.5% | "del que el 5,5 por ciento será a cargo de la empresa y el 1,55 por ciento, a cargo" |
| Desempleo, other fixed-term contracts | 6.70% | "8,30 por ciento, del que el 6,70 por ciento será a cargo del empresario y el 1,60" |
| Fondo de Garantía Salarial (FOGASA) | 0.20% | "Fondo de Garantía Salarial: el 0,20 por ciento, a cargo de la empresa" |
| Formación profesional | 0.60% | "el 0,70 por ciento, del que el 0,60 por ciento será a cargo de la empresa y el 0,10" |
| Mecanismo de equidad intergeneracional | 0.75% | "del que el 0,75 por ciento será a cargo del empleador y el 0,15 por ciento, a cargo" |

The lower rate is not only for permanent contracts. The order applies it to permanent contracts including part time and fijo discontinuo, and also to training in alternance and apprenticeship contracts still running, the contract for obtaining professional practice, the relevo contract, substitution contracts, interinidad contracts still running, and any contract whatever its form with a worker with a recognised disability of thirty three per cent or more. A fixed-term substitution contract is on the lower rate, not the higher one.

The base for unemployment, the wage guarantee fund and vocational training is the accident and occupational disease base above, not the base for common contingencies.

**Accidents at work and occupational disease (AT and EP) have no single rate.** Article 4.b) of the order sends the reader to the tariff of premiums in additional provision sixty-one of the Ley General de la Seguridad Social, by activity, and says the resulting premiums fall on the employer alone. Where a worker's activity carries a reduced retirement age coefficient, the employer applies the highest rate in that tariff. Read the premium for the client's own activity code; do not quote a range.

**A worker who has reached pension age and stays on.** Article 152 of the Ley General de la Seguridad Social exempts both sides from contributing for common contingencies, unemployment, the wage guarantee fund and vocational training once the worker has reached the retirement age that applies to them. The exemption does not cover the temporary incapacity part of common contingencies, which is contributed at the rate in the table below. Accident and occupational disease contributions and the intergenerational equity mechanism are unaffected.

**Temporary incapacity rate for a worker exempt under article 152 (Social Security, bases and rates 2026)**

| Concept | Total rate | Employer and employee shares |
| --- | --- | --- |
| Source | all figures below | https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/CotizacionRecaudacionTrabajadores/36537 |
| Temporary incapacity from common contingencies, worker past pension age | 1.55% | employer 1.30%, employee 0.25% |

### Typical total employer cost (including AT and EP)

**No official page prints a combined employer percentage, so this Guide prints none.** The previous version of this Guide gave approximate total rates for an office worker, a construction worker and a retail employee. Those numbers were sums of the parts plus an assumed accident premium, and no allowed page carries any of them. They are removed. State the parts in the table above, add the accident premium read from the tariff for the client's activity, and let the payroll system produce the total. The employer's own contribution must in any case appear on the payslip, so the client's own document is the check.

### Solidarity surcharge: employer share (2026)

The employer's share of each solidarity band is in the table in Section 3, printed by the order as its own percentage. The law does say the two sides split each band in the same proportion as the common contingencies rate, but the order prints each side's percentage outright, so read them from the table rather than working the proportion out. The previous version of this Guide printed the proportion as a number of its own, which no official page carries. That number is removed.

## Section 5: Minimum wage and overtime

### Salario mínimo interprofesional (2026)

**Minimum wage, Real Decreto 126/2026, of 18 February**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2026-3815 |
| Where the wage is set by the day | EUR 40.70 | "queda fijado en 40,70 euros/día o 1 221 euros/mes" |
| Where the wage is set by the month | EUR 1,221 | "queda fijado en 40,70 euros/día o 1 221 euros/mes" |
| Floor in annual terms for the compensation and absorption test | EUR 17,094 | "sin que en ningún caso pueda considerarse una cuantía anual inferior a 17 094 euros" |
| Increase on the 2025 amounts | 3.1% | "un incremento del 3,1 por ciento respecto de las previstas en el Real Decreto 87/2025" |
| Fixed-term worker whose service to the same employer does not exceed one hundred and twenty days, per legal working day | EUR 57.82 | "sin que la cuantía del salario profesional pueda resultar inferior a 57,82 euros" |
| Domestic worker paid by the hour, external regime, all pay concepts included | EUR 9.55 | "el salario mínimo de dichas empleadas y empleados de hogar será de 9,55 euros por hora" |

Only pay in money counts towards the minimum wage, and pay in kind may never reduce the full cash amount. The monthly figure assumes the legal working day for the activity; a shorter day is paid pro rata. The decree takes effect for the period from 1 January to 31 December 2026. The figure for a worker on a short fixed-term contract already carries the proportional part of Sundays, public holidays and the two gratificaciones extraordinarias.

The previous version of this Guide also gave a prorated twelve-payment monthly figure and a monthly increase in euros. Neither is printed in the decree, so both are removed.

### Working hours and overtime

**Working time limits (Punto de Acceso General, working time, leave and holidays)**

| Rule | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://administracion.gob.es/pag_Home/Tu-espacio-europeo/derechos-obligaciones/ciudadanos/trabajo-jubilacion/condiciones-trabajo/jornada-permisos |
| Maximum effective working week, averaged over a year and fixed by collective agreement | 40 hours | "Máxima de 40 horas de trabajo efectivo (media semanal en un año)" |
| Maximum ordinary hours in a day | 9 hours | "Máximo de horas de trabajo ordinario al día: 9 horas" |
| Minimum rest between one day's work and the next | 12 hours | "Descanso entre jornada y jornada: mínimo 12 horas" |
| Break once six hours of continuous work are passed | 15 minutes | "debe hacerse un descanso de, como mínimo, 15 minutos" |
| Maximum overtime in a year | 80 hours | "Máximo 80 horas al año, sin contar aquellas que se realicen para prevenir o reparar" |
| Paid public holidays in a year | 14 | "Fiestas laborables: 14 al año" |

Article 35.1 of the Estatuto de los Trabajadores says overtime is either paid at an amount fixed by collective agreement or individual contract, which **may never be lower than the value of the ordinary hour**, or compensated with equivalent paid rest. With no agreement either way, it must be compensated with rest within the four months following. Hours compensated with rest inside those four months do not count against the annual cap. The previous version of this Guide gave typical collective agreement premiums and a night premium as percentages. No allowed page prints them, so they are removed: read the client's own convenio colectivo.

Overtime hours are recorded day by day and totalled over the pay period, and a copy of that summary goes to the worker with the payslip.

**Additional contribution on overtime (Orden PJC/297/2026)**

| What | Total rate | Employer and employee shares |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296 |
| Overtime caused by force majeure | 14.00% | employer 12.00%, employee 2.00% |
| All other overtime | 28.30% | employer 23.60%, employee 4.70% |

## Section 6: Mandatory benefits

### Pagas extraordinarias (extra payments)

Article 31 of the Estatuto de los Trabajadores gives every worker **two** gratificaciones extraordinarias a year. One falls at Christmas; the collective agreement, or an agreement with the workers' representatives, fixes the month of the other. The amount of both, and whether they are prorated across the twelve monthly payments instead of paid as lump sums, is fixed by the collective agreement alone, not by an agreement with the workers' representatives.

For contributions the choice makes no difference. Article 147.1 of the Ley General de la Seguridad Social spreads any payment that falls due at more than monthly intervals across the twelve months of the year, whether or not the employer pays it in a lump sum. The previous version of this Guide said a lump-sum paga extra gets a separate contribution calculation. It does not: it is prorated either way. For withholding, the paga extra is part of the year's total pay used to set the rate in Section 2.

### Vacaciones (annual leave)

Paid annual leave may not be shorter than **thirty calendar days**, and it may not be replaced by money (article 38 of the Estatuto de los Trabajadores). The dates are agreed between employer and worker. The previous version of this Guide converted the thirty calendar days into an approximate number of working days. That conversion is on no official page and is removed; the statute counts calendar days.

Where holiday is accrued and not taken and is paid on the ending of the employment relationship, article 147.1 of the Ley General de la Seguridad Social requires a **complementary contribution** covering the days of that holiday, even where they run into the next month or a new job has started. That is the row most often missed on a finiquito.

The number of paid public holidays is in the working time table in Section 5.

### Incapacidad temporal (sick leave)

**Percentage of the regulatory base (Social Security, temporary incapacity benefit)**

| Case | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/PrestacionesPensionesTrabajadores/10952/28362/28365 |
| Common illness or non-work accident, day 4 to day 20 inclusive | 60% | "60% desde el día 4 hasta el 20 inclusive" |
| Common illness or non-work accident, from day 21 | 75% | "75% desde el día 21 en adelante" |
| Accident at work or occupational disease, from the day the right arises | 75% | "75% desde el día en que se produzca" |
| Donation of organs or tissue for transplant, from the first day of the sick leave | 100% | "100% de la base reguladora desde el primer día de la baja" |

Who pays is set by article 173 of the Ley General de la Seguridad Social. For a common illness or a non-work accident nothing is paid for the first three days, the benefit starts on the fourth, and **from day four to day fifteen inclusive it is at the employer's cost**. For a work accident or an occupational disease the benefit starts the day after the sick note and the employer pays the whole wage for the day of the note itself. Article 174 puts one maximum on the benefit: **five hundred and forty-five calendar days** from the medical sick note. The previous version of this Guide described that as three hundred and sixty-five days plus a further one hundred and eighty; it is one period in the statute, not two.

Many collective agreements improve these percentages. Read the convenio before quoting the statutory figures to a client.

### Maternidad (maternity leave)

**The right is no longer two separate leaves and it is no longer sixteen weeks.** Article 48.4 of the Estatuto de los Trabajadores, as amended by Real Decreto-ley 9/2025 of 29 July, suspends the contract of the biological mother and of the other parent for **nineteen weeks** each on a birth. Where there is a single parent, the period is **thirty-two weeks**. It is distributed as six uninterrupted weeks immediately after the birth, which are compulsory and full time; eleven weeks, twenty-two for a single parent, taken in weekly periods until the child is twelve months old, which the biological mother may start up to four weeks before the expected date; and two weeks, four for a single parent, taken until the child is eight. The right is individual and cannot be transferred to the other parent. Fifteen days' notice to the employer is required.

Where the newborn is hospitalised for more than seven days after a premature birth or for a clinical condition, the period is extended by as many days as the hospitalisation lasts, up to thirteen extra weeks.

**A birth before 31 July 2025 is not simply on the old rules.** The single transitional provision of Real Decreto-ley 9/2025 applies the added two weeks, four for a single parent, taken until the child is eight, to events from 2 August 2024 onwards, and says they may be applied for from 1 January 2026 with no fresh recognition of the right. The rest of the increase runs from 31 July 2025. An employer will therefore see requests this year for two weeks arising from a 2024 or 2025 birth.

Article 48.5 gives the same nineteen weeks, and the same thirty-two for a single parent, on adoption, guardianship for adoption and fostering, running from the judicial decision or administrative decision.

**Benefit rate for birth and care of a child (article 179 Ley General de la Seguridad Social)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724 |
| Subsidy for nacimiento y cuidado de menor, as a share of the regulatory base | 100% | "un subsidio equivalente al 100 por ciento de la base reguladora correspondiente" |
| Subsidy for shared care of a nursing infant, as a share of the regulatory base for temporary incapacity, in proportion to the cut in hours | 100% | "un subsidio equivalente al 100 por ciento de la base reguladora establecida para la prestación de incapacidad temporal" |

The regulatory base is in general the base for common contingencies of the month immediately before the month prior to the event, divided by the days that contribution covers; where the worker joined the employer in the month before the event, or in the month of the event itself, the base is taken from a later month instead. Where pay is monthly and the worker was registered for the whole calendar month, that base is divided by thirty. The worker must be registered, or treated as registered, at the start of each rest period.

### Paternidad (paternity leave)

Spanish law no longer uses the word paternidad for this. The other parent takes the same right described under maternidad above: nineteen weeks, of which the first six are compulsory, full time and immediately after the birth. Anyone quoting sixteen weeks is quoting the law as it stood before 31 July 2025.

### Severance (indemnización por despido)

The statute prints these day counts in words, and no allowed page prints them as digits, so this Guide states them in words.

- **Unfair dismissal (despido improcedente), article 56.** Where a dismissal is declared unfair, the employer may choose, within five days of being notified of the judgment, between taking the worker back and paying an indemnity equal to **thirty-three days' salary per year of service**, months counted pro rata, up to a maximum of **twenty-four monthly payments**. Taking the indemnity ends the contract.
- **Contracts signed before 12 February 2012 are not on that rule alone.** Transitional provision eleven of the Estatuto calculates the indemnity at **forty-five days' salary per year of service for the service before that date** and **thirty-three days for the service after it**, months pro rata either side. The total may not exceed **seven hundred and twenty days' salary**, unless the pre 2012 part on its own already gives more, in which case that larger figure is the ceiling, and in no case above **forty-two monthly payments**. Ask the hire date before quoting any severance number.
- **Objective dismissal (despido objetivo), article 53.** The employer must put at the worker's disposal, at the same time as the written notice, an indemnity of **twenty days per year of service**, months pro rata, up to **twelve monthly payments**, and give **fifteen days' notice**.
- **End of a fixed-term contract, article 49.1.c.** Except for training contracts and a fixed-term substitution contract, the worker is entitled to the proportional part of **twelve days' salary per year of service**.
- **Death, retirement or incapacity of the employer, article 49.1.g.** One month's salary.

Statutory dismissal indemnities are outside the contribution base under article 147.2.c) of the Ley General de la Seguridad Social, in the amount the Estatuto makes compulsory. An amount agreed above that is not.

**FOGASA.** The Fondo de Garantía Salarial pays unpaid wages and indemnities when the employer is insolvent (article 33 of the Estatuto de los Trabajadores). It is funded by the employer contribution in Section 4. What it pays is capped by a daily pay module equal to twice the daily minimum wage including the proportional part of the extra payments.

**Limits on what the wage guarantee fund pays, for a cause arising in this tax year (Ministerio de Trabajo y Economía Social)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.mites.gob.es/fogasa/faqs.html |
| Daily pay module, twice the daily minimum wage with the extra payments prorated | EUR 94.78 | "Duplo S.M.I. con prorrata de pagas extraordinarias: 94,78 EUROS" |
| Ceiling on unpaid wages, being that module for one hundred and twenty days | EUR 11,373.60 | "Límite Salarios (120 días): 11.373,60 EUROS" |
| Ceiling on indemnities | EUR 34,594.70 | "Límite Indemnizaciones: 34.594,70 EUROS" |

Unpaid wages are paid for at most one hundred and twenty days at that module. Indemnities are paid for at most one year's pay, nine monthly payments in the article 41.3 case, and for the articles 50 and 56 cases the fund computes the indemnity at thirty days per year of service whatever the judgment says.

### Finiquito (final settlement)

Article 49.2 of the Estatuto de los Trabajadores: when the contract ends, the employer must send with the notice of termination, or with the notice period, **a proposed settlement document of the amounts owed**. The worker may ask for a workers' representative to be present at the signing of the finiquito receipt, and the receipt records whether one was present or whether the worker did not use the right. If the employer prevents that presence, the worker may note it on the receipt.

A finiquito is a payslip, not a separate document type: it runs through the same devengos and deducciones structure as Section 7. The parts that most often go missing are the proportional pagas extraordinarias, the accrued and untaken holiday with its complementary contribution, and, for a fixed-term contract, the twelve days' salary per year of service.

## Section 7: Payslip requirements

Article 29.1 of the Estatuto de los Trabajadores requires the salary to be documented by handing the worker **an individual receipt evidencing payment**. The receipt follows the model approved by the Ministry, which is the annex to the Orden of 27 December 1994, unless a collective agreement or, failing that, an agreement with the workers' representatives sets another model **containing the different payments to the worker and the deductions that legally apply, with due clarity and separation**. Pay periods may not exceed one month.

Orden ESS/2098/2014 rewrote that annex for one reason: until then the payslip showed only the contribution base and the worker's rate, not the employer's contribution. Article 142.2 of the Ley General de la Seguridad Social now requires the employer to inform the worker on the payment document of **the total Social Security contribution, showing the employer's part and the worker's part separately**. A payslip that shows only the worker's deductions does not comply.

### Mandatory payslip fields

The annex is published as an image in the official gazette, so its field names could not be read as text from the BOE page used for this refresh. The structure below is the legacy content of this Guide, kept as reference. Check it against the official model before relying on it, and note that modifications that are purely formal, or that add information for the worker, are treated as complying, provided no concept in the model is removed and no name is changed.

| Section | Fields |
| --- | --- |
| Header | Employer: name, CIF, address, código de cuenta de cotización (CCC), activity code |
| Employee | Name, NIF or NIE, número de afiliación a la Seguridad Social, contribution group, professional category, start date |
| Period | Month and year, days covered |
| Devengos, percepciones salariales | Salario base, complementos salariales, horas extraordinarias, horas complementarias, gratificaciones extraordinarias, salario en especie |
| Devengos, percepciones no salariales | Indemnizaciones o suplidos, prestaciones e indemnizaciones de la Seguridad Social, indemnizaciones por traslados, suspensiones o despidos, other non-salary payments |
| Deducciones | Worker's Social Security contributions, at the rates in Section 3, on the base shown |
|  | IRPF withholding, as an amount and as the percentage applied, Section 2 |
|  | Advances, the value of goods received in kind, other lawful deductions |
| Totals | Total devengado, total a deducir, líquido total a percibir |
| Employer contribution | Base de cotización por contingencias comunes, base de cotización por contingencias profesionales including overtime, and the employer's contribution by concept, Section 4 |
| Footer | Date, employer signature or electronic equivalent, worker signature |

The payer must also tell the worker, when it pays, the withholding made and the percentage applied (article 108.4 of the IRPF regulation).

### Delivery

- The receipt refers to natural months. Where an employer pays for shorter periods, those payments are documented as advances on account of the definitive settlement, which is made in the monthly receipt.
- The worker signs the receipt on being handed the duplicate and paid. The signature evidences receipt of the amounts, not agreement with them.
- Where payment is by bank transfer, the employer hands over the duplicate without asking for a signature, and the bank's proof of payment takes its place.
- **Payslips are archived and kept, together with the Social Security contribution documents, for a minimum period of five years.** The previous version of this Guide said four. Article 3 of the Orden of 27 December 1994 says five.

## Section 8: Filing obligations

### Monthly

Social Security is settled through the Sistema RED, the electronic data transmission system, using the Sistema de Liquidación Directa. SILTRA is the TGSS application an authorised user runs to exchange the contribution, affiliation and benefit files. The employer sends the variable data, the TGSS calculates the liquidation and returns the Recibo de Liquidación de Cotizaciones (RLC) and the Relación Nominal de Trabajadores (RNT), which replaced the old TC1 and TC2.

| Obligation | Rule | Source |
| --- | --- | --- |
| Transmit the liquidation, self-assessment system | Up to the last calendar day of the payment period, whether or not the contributions are actually paid in it (article 18.1) | https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579 |
| Ask the TGSS to calculate the liquidation and send the data, direct settlement system | Up to the penultimate calendar day of the payment period (article 18.2) | https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579 |
| Pay the contributions | Within the month following the month they accrue (article 56) | https://www.boe.es/buscar/act.php?id=BOE-A-2004-11836 |

**Surcharges for paying Social Security late (article 30 Ley General de la Seguridad Social)**

| Case | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724 |
| Filing duties met, paid within the first calendar month after the deadline | 10% | "Recargo del 10 por ciento de la deuda, si se abonasen las cuotas debidas dentro del primer mes" |
| Filing duties met, paid from the second calendar month | 20% | "Recargo del 20 por ciento de la deuda, si se abonasen las cuotas debidas a partir del segundo mes" |
| Filing duties not met, paid before the deadline in the demand | 20% | "Recargo del 20 por ciento de la deuda, si se abonasen las cuotas debidas antes de la terminación" |
| Filing duties not met, paid after that deadline | 35% | "Recargo del 35 por ciento" |

Withholding is settled separately, on modelo 111, through the Agencia Tributaria. Monthly filing is the exception, not the rule: see the next heading.

### Quarterly (small employers), and when an employer must go monthly

**The trigger is not headcount.** The previous version of this Guide said employers with fewer than six employees file quarterly. Quarterly is the default for everyone. The Agencia Tributaria page puts monthly filing on those whose volume of operations in the previous year exceeded the figure below, and says that is one case among others. Article 108.1 of the IRPF regulation names the others: a withholder in either of the two cases in article 71.3 of the VAT regulation, and a public administration, the Social Security included, whose last approved annual budget exceeded six million euros.

**Modelo 111 and modelo 190 deadlines (Agencia Tributaria, obligations as a withholder)**

| Obligation | Rule | Note |
| --- | --- | --- |
| Source | all figures below | https://sede.agenciatributaria.gob.es/Sede/irpf/retenciones-ingresos-cuenta-pagos-fraccionados/retenciones-ingresos-cuenta/obligaciones-retenedor.html |
| Modelo 111, quarterly, the default | First 20 calendar days of April, July, October and January, for the previous quarter, unless the payment is direct debited | "en los 20 primeros días naturales de abril, julio, octubre y enero" |
| Modelo 111, monthly, the most common of several cases | Where the volume of operations in the immediately preceding year is above EUR 6,010,121.04, in the first 20 calendar days of the month, for the previous month | "cuando el volumen de tus operaciones en el año inmediato anterior es mayor de 6.010.121,04 €" |
| Nil returns | Filed on the same deadlines and the same forms, where income subject to withholding is paid but no withholding is due on the amount | "Deberás presentar declaraciones negativas, en los plazos anteriores y con los mismos modelos" |
| Deadline falling on a non-working day | The period ends on the next working day | "Si el vencimiento de los plazos de presentación coincide con un día inhábil" |
| Modelo 190, annual summary | Between 1 and 31 January of the year after the one the annual return covers | "es entre el 1 de enero y el 31 de enero del año siguiente" |
| Certificado de retenciones | Issued to each payee and made available before the income tax filing period opens | "Deberás ponerlos a su disposición antes del inicio de la declaración de IRPF" |

Anyone who filed modelo 111 must file modelo 190. Article 108.2 of the IRPF regulation sets the annual declaration in the first twenty calendar days of January, and gives the 1 to 31 January window where the declaration is filed on machine readable media or through the tax administration's own print modules, which is how modelo 190 is filed in practice. The Agencia Tributaria page for the current campaign states "del 1 de enero al 2 de febrero de 2026" for the summary of 2025 pay, because the ordinary closing date fell on a non-working day. Where a technical problem stops an internet filing inside the regulatory period, filing is allowed in the four calendar days after it ends. Check the campaign page for the year being filed rather than assuming 31 January.

### Annual

| Obligation | Detail |
| --- | --- |
| Modelo 190 | The annual summary of withholding and payments on account, listing each payee by name and tax number, with the income, the withholding, the reductions applied and the family circumstances declared. Deadline in the table above |
| Certificado de retenciones | One per employee, available before the income tax filing period opens. It is what the employee's own return is built from |
| Certificado de empresa | Sent to the authorities through the Sistema RED when a contract ends, so the worker can claim unemployment benefit. No page read for this refresh gives its deadline, so this Guide states none. The previous version said ten days |

### Employee obligations

The employee files their own income tax return. The employer's duty ends with the certificate.

**Thresholds below which an employee need not file (article 96 Ley 35/2006)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Employment income from one payer, general limit | EUR 22,000 | "Rendimientos íntegros del trabajo, con el límite de 22.000 euros anuales" |
| Employment income with two or more payers, where the second and later payers together pass the next row | EUR 15,876 | "El límite a que se refiere la letra a) del apartado 2 anterior será de 15.876 euros" |
| Amount the second and later payers must exceed for that lower limit to apply | EUR 1,500 | "no supera en su conjunto la cantidad de 1.500 euros anuales" |

The filing window each year is on the Agencia Tributaria campaign page, not in this Guide, and not in `es-income-tax`, which is written for the self employed.

## Section 9: Common payroll patterns

### Typical bank statement descriptions (salary credits)

| Pattern | Classification |
| --- | --- |
| NOMINA, SALARIO, HABERES | Net salary payment |
| PAGA EXTRA, PAGA EXTRAORDINARIA | Extra payment, Section 6 |
| LIQUIDACION, FINIQUITO | Final settlement on termination, Section 6 |
| INDEMNIZACION DESPIDO | Severance payment, Section 6 |
| PRESTACION INSS, INCAPACIDAD TEMPORAL | Sickness or birth benefit, often paid by the employer on the authority's behalf |
| DESEMPLEO SEPE | Unemployment benefit, not payroll |

### Typical employer debit patterns

| Pattern | Classification |
| --- | --- |
| TGSS COTIZACIONES, SEG SOCIAL | Social Security contribution payment, Section 8 |
| AEAT modelo 111, HACIENDA RETENCIONES | IRPF withholding remittance, Section 8 |
| NOMINAS TRANSFERENCIA | Salary disbursement to employees |
| FOGASA | Wage guarantee fund contribution, Section 4 |
| MUTUA and a name | Mutua collaborating with Social Security, accident and occupational disease cover |

## Section 10: Interaction with other Guides

| Scenario | Guide to use |
| --- | --- |
| Employee payroll, withholding and contributions | **This Guide** |
| Self-employed income tax | `es-income-tax` |
| Self-employed contributions (RETA), bands, rates and regularisation | `es-social-contributions` |
| Self-employed registration and obligations | `es-autonomous-worker` |
| The withholding return itself | `es-modelo-111` |
| IVA (Spanish VAT) | `es-vat-return` |
| Payroll entries in the books, and what to keep | `spain-bookkeeping` |
| Invoicing and its reporting duties | `spain-einvoice` |
| Personal income tax deductions | `es-irpf-deductions` |

`es-income-tax` is written for the self employed. An employee's own annual return is under the same IRPF law, but this Guide does not walk through it; use the certificado de retenciones and the Agencia Tributaria campaign page instead.

### Key handoff points

- **Payroll to bookkeeping.** Gross wages and the employer's Social Security are expenses. The employee's IRPF is a liability until the modelo 111 payment, and both parties' Social Security contributions are liabilities until payment to the TGSS. Pagas extraordinarias are accrued monthly. The account codes used by Spanish charts of accounts are not reproduced here.
- **Payroll to income tax.** The certificado de retenciones feeds the employee's own return. The employer sets a personalised rate under Section 2; it does not apply a tax scale.
- **Payroll to Social Security.** The RLC and the RNT must reconcile with the payroll totals. The Sistema RED is the channel for affiliation as well as contributions.
- **Payroll to the self-employed Guides.** A company director or working member registered in RETA is not on this Guide's payroll rules for contributions. Their base is set by the bands in `es-social-contributions`, subject to a floor equal to the group 7 minimum in Section 3.

## The method, step by step

1. **Register the employer and the worker before work starts.** Get a código de cuenta de cotización, choose the mutua for accident cover, and register the worker with the TGSS through the [Sistema RED](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724), whose authorised users are covered by additional provision thirty-four of the Ley General de la Seguridad Social.
2. **Fix the contribution group and the contract type.** The group sets the minimum base in Section 3 and the contract type sets the unemployment rate in Sections 3 and 4. Both come from article 3 and article 4 of [Orden PJC/297/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296).
3. **Work out the withholding rate once for the year.** Follow articles 82 to 86 of the [IRPF regulation](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820) in the order given in Section 2, or use the Agencia Tributaria calculation service in Sources. Check the result against the no-withholding table in Section 2 before telling anyone their rate is zero.
4. **Build the contribution bases.** Apply article 147 of the [Ley General de la Seguridad Social](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724): total monthly remuneration, payments due at more than monthly intervals spread over twelve months, then the group minimum and the ceiling in Section 3. Build the professional contingencies base separately, with overtime.
5. **Produce the payslip.** Use the model in the annex to the [Orden of 27 December 1994](https://www.boe.es/buscar/act.php?id=BOE-A-1995-912), or the model in the convenio. It must show the employer's contribution as well as the worker's, and the withholding percentage applied.
6. **File and pay Social Security.** Send the liquidation through the Sistema RED inside the period in [Real Decreto 2064/1995](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579) and pay within the month following accrual under [Real Decreto 1415/2004](https://www.boe.es/buscar/act.php?id=BOE-A-2004-11836). Late payment brings the surcharges in Section 8.
7. **File and pay the withholding.** Modelo 111 on the deadlines on the [Agencia Tributaria page for withholders](https://sede.agenciatributaria.gob.es/Sede/irpf/retenciones-ingresos-cuenta-pagos-fraccionados/retenciones-ingresos-cuenta/obligaciones-retenedor.html), quarterly unless the turnover test in Section 8 puts the employer on monthly filing.
8. **Close the year.** File modelo 190 and give each employee the certificado de retenciones before the income tax filing period opens, per the same page.
9. **On termination, build the finiquito.** Send the proposed settlement document with the notice, under article 49.2 of the [Estatuto de los Trabajadores](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430), and include the proportional pagas extraordinarias and the accrued untaken holiday with its complementary contribution.

## Ask the client first

- **Which convenio colectivo applies?** It can raise the wage, the number and size of the pagas extraordinarias, the overtime premium and the sick pay above every statutory floor in this Guide.
- **Permanent or fixed-term contract, and how long?** It changes the unemployment rate on both sides, whether the one-off charge on contracts under thirty days applies, and whether the two per cent withholding floor bites.
- **What is the worker's family situation, and have they told you about children, a disability, an ascendant or a mortgage on their main home?** Every one of them moves the withholding rate, and the employer may only act on what the worker has notified.
- **What contribution group and what activity code?** The group sets the minimum base; the activity sets the accident and occupational disease premium, which has no general rate.
- **Is any part of the monthly pay above the contribution ceiling?** If so the solidarity contribution applies to the excess, on both sides.
- **Are the pagas extraordinarias paid as lump sums or prorated?** It changes the payslip, though not the contribution base.
- **Is the worker a company director or a working member of the company?** If so they may belong in the self-employed regime instead, and this Guide's contribution rules do not apply to them.

## When to refuse or refer

- Any question that needs a figure from a convenio colectivo. This Guide carries statutory floors only.
- The accident and occupational disease premium for a specific activity. It comes from the tariff in additional provision sixty-one of the Ley General de la Seguridad Social, by activity code.
- Any request for a combined employer percentage, a combined employee percentage, or a total cost of employment as one rate. No official page prints one.
- Contribution reductions, bonificaciones and exemptions for particular hires. They change several times a year and none is in this Guide.
- Payroll in Álava, Bizkaia, Gipuzkoa or Navarra. Those territories run their own tax administrations and their own withholding rules. Social Security is common; income tax withholding is not.
- Posted workers, and anyone contributing in two member states. That is EU social security coordination.
- Dismissal advice. This Guide gives the statutory indemnity formulas so a payslip can be built, not whether a dismissal is lawful.
- Any payroll computation presented as final. Send it to an asesor fiscal, a gestor administrativo or a graduado social for sign-off.

## Prohibitions

- **Never present the withholding scale as the income tax scale.** The 19, 24, 30, 37, 45 and 47 per cent figures are the reference scale used inside the withholding calculation. Spain's income tax is a state half plus a community half, and neither is this table.
- **Never work out a withholding rate by hand from a monthly salary.** Follow articles 82 to 86, or use the Agencia Tributaria calculation service.
- **Never say a minimum-wage worker is exempt from withholding.** The annual minimum wage is above the "otras situaciones" threshold with no children.
- **Never add the contribution shares together and call the sum an official rate.** The order prints each share; it prints no total for either side.
- **Never quote a single accident and occupational disease rate.** It is a tariff by activity.
- **Never omit the pagas extraordinarias.** Two a year are the statutory minimum, and they are prorated into the contribution base whether or not they are prorated in pay.
- **Never treat a lump-sum paga extra as contributed for separately.** Article 147.1 prorates it over twelve months either way.
- **Never leave the employer's contribution off the payslip.** Article 142.2 of the Ley General de la Seguridad Social requires it.
- **Never keep payslips for less than five years.** Article 3 of the Orden of 27 December 1994.
- **Never assume modelo 111 is monthly.** Quarterly is the default. Monthly filing follows the previous year's volume of operations in the most common case, but that is one trigger among several: see the list in the filing section.
- **Never miss the contribution payment period.** It is the month following accrual, and the surcharges in Section 8 start immediately.
- **Never state sixteen weeks for birth leave.** It has been nineteen since 31 July 2025, and thirty-two for a single parent, and two of those weeks reach back to births from 2 August 2024.
- **Never present a payroll computation as definitive.** Direct the client to a qualified professional for sign-off.

## Sources

- [Orden PJC/297/2026, contribution bases and rates for 2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296)
- [Real Decreto 126/2026, minimum wage](https://www.boe.es/buscar/act.php?id=BOE-A-2026-3815)
- [Estatuto de los Trabajadores](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430)
- [Ley General de la Seguridad Social](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724)
- [Ley 35/2006, IRPF](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764)
- [Real Decreto 439/2007, IRPF regulation](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820)
- [Orden of 27 December 1994, individual salary receipt](https://www.boe.es/buscar/act.php?id=BOE-A-1995-912)
- [Orden ESS/2098/2014, amending the salary receipt annex](https://www.boe.es/buscar/doc.php?id=BOE-A-2014-11637)
- [Real Decreto 2064/1995, contribution and settlement](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579)
- [Real Decreto 1415/2004, Social Security collection](https://www.boe.es/buscar/act.php?id=BOE-A-2004-11836)
- [Social Security, bases and rates of contribution](https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/CotizacionRecaudacionTrabajadores/36537)
- [Social Security, temporary incapacity benefit](https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/PrestacionesPensionesTrabajadores/10952/28362/28365)
- [Fondo de Garantía Salarial, what it covers and its limits](https://www.mites.gob.es/fogasa/faqs.html)
- [Agencia Tributaria, obligations as a withholder](https://sede.agenciatributaria.gob.es/Sede/irpf/retenciones-ingresos-cuenta-pagos-fraccionados/retenciones-ingresos-cuenta/obligaciones-retenedor.html)
- [Agencia Tributaria, modelo 190 filing periods](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-190-decla_____moniales-imputaciones-rentas-anual_/plazos-presentacion.html)
- [Punto de Acceso General, working time, leave and holidays](https://administracion.gob.es/pag_Home/Tu-espacio-europeo/derechos-obligaciones/ciudadanos/trabajo-jubilacion/condiciones-trabajo/jornada-permisos)
- [Punto de Acceso General, ending a contract, resignations and dismissals](https://administracion.gob.es/pag_Home/Tu-espacio-europeo/derechos-obligaciones/ciudadanos/trabajo-jubilacion/condiciones-trabajo/finalizacion-contrato.html)

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal, gestor administrativo, or graduado social in Spain) before implementation.

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
