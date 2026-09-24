---
name: es-rental-income
description: Use this skill whenever asked about Spanish rental income taxation. Trigger on phrases like "rental income Spain", "alquiler IRPF", "rendimientos del capital inmobiliario", "rental deductions Spain", "60% reduction rental Spain", "non-resident rental Spain", "IBI deduction", "Modelo 100 rental", "vivienda turística", "imputación de rentas inmobiliarias", "valor catastral", "amortización inmueble", or any question about declaring rental income in Spain. This skill covers IRPF rental computation, deductible expenses, the 60% reduction for residential rental, non-resident flat rate, tourist rental, and imputed income for vacant properties. ALWAYS read this skill before touching any Spanish rental income work.
version: "1.0"
jurisdiction: ES
tax_year: 2026
last_updated: 2026-09-23
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spanish rental income in IRPF, for residents and non-residents

Letting property in Spain is taxed as rendimientos del capital inmobiliario under articles 22 to 24 of Ley 35/2006, unless the letting amounts to an economic activity under article 27.2. A second home that is neither let nor the owner's main home produces imputed income under article 85. Figures are for tax year 2026. Two of the pages cited below carry a different date on their face, and each is named where it is used: the Agencia Tributaria practical income tax manual is the manual for 2025 (the return filed in 2026), and the Agencia Tributaria page on value added tax for tourist lets was last updated in 2023. The statute pages on boe.es are the consolidated texts in force in 2026.

One thing to read before anything else: the reduction on letting a home is no longer a single 60 per cent. Ley 12/2023 replaced it with five different cases, each with its own condition, and left older contracts on the old rule. A percentage quoted without its condition is worse than no answer. Section 2.5 sets out all five.

## Section 1: Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Spain (Reino de España) |
| Tax | IRPF (Impuesto sobre la Renta de las Personas Físicas), rental income |
| Currency | EUR only |
| Tax year | 1 January to 31 December 2026 |
| Primary legislation | Ley 35/2006, de 28 de noviembre, del IRPF; Real Decreto 439/2007 (Reglamento) |
| Supporting legislation | Ley 29/1994 de Arrendamientos Urbanos; articles 22 to 24 of Ley 35/2006 (rendimientos del capital inmobiliario); Real Decreto Legislativo 5/2004 (non-residents) |
| Tax authority | Agencia Estatal de Administración Tributaria (AEAT) |
| Filing portal | Renta Web (sede.agenciatributaria.gob.es) |
| Resident filing deadline | For the 2025 return, 8 April to 30 June 2026. The dates for the 2026 return are not yet published on an allowed page. |
| Non-resident rental filing | Modelo 210. See section 2.7 for the 2026 deadlines, which changed. |
| Guide version | 2.0 |

### IRPF General Tax Rates: the escala general, state half only

Rental income goes into the general taxable base and is taxed at the escala general, not at the savings rates. The scale below is the STATE half of that tax only. Article 74 of Ley 35/2006 leaves the other half to each autonomous community, and each community approves its own scale. No page on an allowed host publishes the seventeen community scales, so this Guide cannot state a total marginal rate for Spain. A rate quoted as "the Spanish rate" is a rate for a region nobody named.

**IRPF General Tax Rates: state half of the escala general**

| Band of the general taxable base | State rate | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Up to EUR 12,450 | 9.5% | Article 63.1, escala general del impuesto |
| EUR 12,450 to EUR 20,200 | 12% | State half only |
| EUR 20,200 to EUR 35,200 | 15% | State half only |
| EUR 35,200 to EUR 60,000 | 18.5% | State half only |
| EUR 60,000 to EUR 300,000 | 22.5% | State half only |
| Over EUR 300,000 | 24.5% | State half only |

The table often printed as "the Spanish income tax brackets", running 19, 24, 30, 37, 45 and 47, is the payroll withholding scale in article 101.1 of Ley 35/2006. It is not the income tax scale and it is not the rate a landlord bears.

### Key Features

**Key Features**

| Feature | Detail |
| --- | --- |
| Rental income classification | Rendimientos del capital inmobiliario (article 22 of Ley 35/2006) |
| When it becomes an economic activity | Only where at least one person is employed under an employment contract and full time, or where services proper to the hotel trade are supplied. See section 2.0. |
| Reduction on letting a home | Five cases with different percentages and different conditions. See section 2.5. |
| Non-resident rate, outside the EU and EEA | Charged on gross income, no expenses. See section 2.7. |
| Non-resident rate, EU and EEA with exchange of information | Charged on net income, expenses allowed. See section 2.7. |
| Imputed income on a home neither let nor lived in | A percentage of the cadastral value. Two rates, and the official sources disagree for 2026. See section 2.8. |
| Depreciation (amortización) | A percentage of the greater of acquisition cost or cadastral value of the construction, land excluded. See section 2.4. |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether the home is the tenant's permanent home | Do NOT apply any reduction under article 23.2 |
| Contract date unknown | Do NOT choose between the old rule and the new ladder. Get the contract date. |
| Unknown whether the property is in a stressed residential market area | Use the general case, not the enhanced percentages |
| Unknown cadastral value split between land and construction | Do not compute depreciation. Obtain the property tax receipt (recibo del Impuesto sobre Bienes Inmuebles). |
| Unknown whether resident or non-resident | Assume resident and verify |
| Unknown autonomous community | Use the state scale only. State that the community half is missing. |
| Unknown whether the cadastral value was revised, and when | Use the general imputation rate, not the reduced one |

## Section 2: Classification Rules

### 2.0 Is the letting an economic activity?

This question comes first, because it changes everything downstream: the income category, the expense rules, the withholding, the reduction, and for a non-resident whether there is a permanent establishment.

Article 27.2 of Ley 35/2006 states the test in one sentence: letting property is carried on as an economic activity "únicamente cuando para la ordenación de esta se utilice, al menos, una persona empleada con contrato laboral y a jornada completa". So the test is an employed person, under a contract that labour law treats as an employment contract, and full time. There is no "local" or premises requirement in the current wording; that requirement was removed with effect from 1 January 2015. The number of properties does not enter the test, and neither does the amount of rent.

The Agencia Tributaria adds two points on the same page. First, the requirement is not met by management work the owner does himself. Second, letting is also an economic activity where the owner does not merely put the property at the tenant's disposal but supplies services proper to the hotel trade (restaurant, cleaning during the stay, laundry and the like).

If the letting is an economic activity, this Guide stops being the right one: the income is rendimientos de actividades económicas, computed under articles 27 to 32, and the reductions in article 23.2 do not apply.

Sources for this section: the statute at https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 and the Agencia Tributaria manual page at https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/rendimientos-capital-inmobiliario/concepto-rendimientos-capital-inmobiliario.html

### 2.1 Rental Income (Rendimientos del Capital Inmobiliario)

Article 22.2 of Ley 35/2006 says the gross income is everything the tenant must pay on every count, including amounts for goods let with the property, and excluding value added tax or the Canary Islands general indirect tax.

**Rental Income (Rendimientos del Capital Inmobiliario)**

| Income Type | Treatment |
| --- | --- |
| Monthly rent received | Full amount assessable (rendimiento íntegro) |
| Tenant payment of owner expenses, for example the property tax | Assessable income where it is the landlord's own obligation |
| Value added tax charged on the rent | Excluded from the gross income (article 22.2) |
| Security deposit retained for damages | Assessable when retained |
| Key money or premium paid by tenant | Assessable |
| Goods let together with the property (furniture, garage) | Assessable as part of the same gross income |
| Sub-letting: what the sub-lessor receives | Rendimientos del capital mobiliario, a different category (article 25.4.c) |
| Sub-letting: the owner's share of the sub-let price | Rendimientos del capital inmobiliario, but with NO reduction under article 23.2 |
| Letting a business as a going concern | Rendimientos del capital mobiliario, not covered by this Guide |
| Letting a bare business premises only | Rendimientos del capital inmobiliario, no reduction |
| Compensation received by the landlord because the tenant ends the lease early | Rendimientos del capital inmobiliario, assessable in the year received |

The sub-letting and going-concern points are on the Agencia Tributaria page at https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/rendimientos-capital-inmobiliario/concepto-rendimientos-capital-inmobiliario.html

### 2.2 Deductible Expenses (Gastos Deducibles): Art. 23 LIRPF

Article 23.1 of Ley 35/2006 and article 13 of Real Decreto 439/2007 list the deductible expenses. The rule is "all expenses necessary to obtain the income", followed by a non-exhaustive list.

**Deductible Expenses (Gastos Deducibles)**

| Expense | Deductible? | Notes |
| --- | --- | --- |
| Mortgage interest (intereses del préstamo) and other finance costs | Yes | Interest on capital invested in acquiring or improving the property. Capped with repairs: see section 2.6. |
| Property tax (Impuesto sobre Bienes Inmuebles) | Yes | Non-state taxes and surcharges that fall on the income or on the property, provided they are not penalties |
| Comunidad de propietarios (community fees) | Yes | Amounts owed to third parties for services |
| Insurance premiums | Yes | Civil liability, fire, theft, breakage of glass and the like, on the property producing the income |
| Repairs and maintenance (reparación y conservación) | Yes | Painting, rendering, repair of installations, and replacement of items such as heating, lift or security doors. Capped with interest: see section 2.6. |
| Legal costs and costs of formalising the letting | Yes | Costs of drawing up the lease and of legal defence relating to the property or the income |
| Property management, caretaking, security (administración, portería, vigilancia) | Yes | Amounts owed to third parties for personal services |
| Utilities and supplies paid by the landlord | Yes | Article 13.g), cantidades destinadas a servicios o suministros |
| Amortización (depreciation) of the building | Yes | See section 2.4 |
| Amortización of furniture and fittings let with the home | Yes | See section 2.4 |
| Doubtful debts (saldos de dudoso cobro) | Yes | Where the debtor is in insolvency proceedings, OR more than six months have run between the first collection attempt and the end of the tax period and the credit has not been renewed |
| Municipal waste charge (tasa de basuras) | Yes | A non-state charge falling on the property |

Two corrections worth naming, because both were in the earlier version of this Guide. A doubtful debt does NOT require that legal action has been started: the second test in article 13.e) is six months from the first collection attempt with no renewal of credit. And where a doubtful debt deducted in one year is later paid, article 13.e) requires it to be brought in as income in the year of payment.

Source for this section: https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820

### 2.3 Non-Deductible / Capital Expenses

**Non-Deductible / Capital Expenses**

| Expense | Treatment |
| --- | --- |
| Improvements (mejoras) | NOT deductible. Article 13.a) excludes amounts spent on enlargement or improvement. They add to the acquisition cost. |
| Enlargement or extension (ampliación) | NOT deductible, capital |
| Purchase of furniture | Not deducted at once. Depreciated: see section 2.4. |
| Repayment of mortgage principal | NOT deductible. Only the interest is. |
| Compensation paid by the landlord for early termination of the lease | Treated as an improvement, not an expense |
| The land component of the property | Never depreciated |

### 2.4 Amortización (Depreciation)

Depreciation is deductible where it answers to the real depreciation of the asset. Article 14 of Real Decreto 439/2007 sets the tests, and the Agencia Tributaria manual states the percentages.

**Amortización: maximum rates**

| Item | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/gastos-deducibles/cantidades-destinadas-amortizacion.html |
| Building, per year, on the greater of acquisition cost paid or cadastral value, land excluded | 3% | "no excedan del resultado de aplicar el porcentaje del 3 por 100 sobre el mayor de los siguientes valores" |
| The statute says the same in one sentence, and names both values and the land exclusion: https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 | 3% | "si no excede del resultado de aplicar el 3 por ciento sobre el mayor de los siguientes valores: el coste de adquisición satisfecho o el valor catastral, sin incluir el valor del suelo" |
| Furniture and fittings let with the home (instalaciones, mobiliario y enseres) | 10% | Simplified depreciation table: "para Instalaciones, mobiliario y enseres es el 10 por 100" |
| Minimum depreciation that reduces the acquisition cost on a later sale | 1% | The owner may deduct a percentage between the minimum and the maximum in this table |

- **Land and construction split** Where the value of the land is not known, article 14.2.a) of Real Decreto 439/2007 says it is worked out by apportioning the acquisition cost paid between the cadastral values of the land and of the construction for each year. The property tax receipt shows the two cadastral values separately. Apply the building rate in the table above to the construction part only. See https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820
- **Method** Take the construction share from the property tax receipt, apply that share to the acquisition cost paid, compare the result with the cadastral value of the construction, take the greater, and apply the building rate in the table above. Earlier versions of this Guide carried a worked example with invented amounts. It has been replaced by the Agencia Tributaria's own example below.

**Worked example published by the Agencia Tributaria: a home inherited and then let**

| Step | Amount | Source text |
| --- | --- | --- |
| Source | all figures below | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/gastos-deducibles/cantidades-destinadas-amortizacion.html |
| Value of the home for inheritance tax | EUR 100,000 | "cuyo valor atribuido en la liquidación del Impuesto sobre Sucesiones y Donaciones (ISD) ... fue de 100.000 euros" |
| Costs and taxes of the acquisition | EUR 2,000 | "Los gastos y tributos inherentes a la adquisición (notaria, registro, ISD) ascienden a 2.000 euros" |
| Cadastral value of the home | EUR 80,000 | "El valor catastral del inmueble heredado: 80.000 euros" |
| Share of the total value that is land | 20% | "El porcentaje que representa el valor del suelo respecto al valor total del inmueble es del 20 por 100" |
| Acquisition cost paid, land excluded | EUR 81,600 | "Coste de adquisición satisfecho: 80% s/(100.000 + 2.000) = 81.600" |
| Cadastral value, land excluded | EUR 64,000 | "Valor catastral excluido el valor del suelo: (80% s/ 80.000) = 64.000" |
| Maximum yearly depreciation, being the building rate on the greater of the two above | EUR 2,448 | "el importe de la amortización anual máxima deducible será el 3% s/81.600 euros = 2.448 euros" |
| Cap on the depreciation accumulated over the whole ownership | EUR 81,600 | "El contribuyente podrá amortizar el inmueble hasta que el importe de la amortización acumulada alcance el valor de adquisición del inmueble ... esto es, 80% x (100.000 + 2.000) = 81.600 euros" |

- **The minimum bites later** The rate in the table above is a maximum. The Agencia Tributaria page also records that the owner may deduct a lower figure, but when the property is later sold the amount deducted as depreciation must reduce the acquisition cost used to compute the capital gain.
- **There is a lifetime cap as well as a yearly one** Accumulated depreciation may not exceed the acquisition value of the building that produces the income, land excluded, whatever the yearly maximum allows. The Agencia Tributaria states it as "El límite de la amortización acumulada será el valor de adquisición del inmueble generador de los rendimientos", and the Tribunal Económico-Administrativo Central fixed it on 18 December 2025 (claim 00/00653/2025) as applying "con independencia del límite anual previsto en el artículo 14 del Reglamento". For a property bought for money the value is the one in article 35 of Ley 35/2006; for one inherited or given, the value in article 36. See https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/gastos-deducibles/cantidades-destinadas-amortizacion.html
- **Only while let** Depreciation, like the other expenses, belongs to the days the property was let. See section 6.1.

### 2.5 The reduction on letting a home (Reducción por arrendamiento de vivienda)

This is the trap in Spanish rental tax, and it has two layers: WHICH ladder applies (that depends on the contract date), and then WHICH rung (that depends on the facts at the moment the contract was signed).

First, the ladder. Article 23.2 of Ley 35/2006 as rewritten by the disposición final segunda of Ley 12/2023 applies to home lettings whose contract was signed from the entry into force of that law. Disposición transitoria trigésima octava of the same law leaves earlier contracts on article 23.2 "en su redacción vigente a 31 de diciembre de 2021". The Agencia Tributaria puts the dividing line at 26 May 2023 and states the percentage for the earlier contracts.

**Which ladder: by contract date**

| Contract date | Reduction | Note |
| --- | --- | --- |
| Source | all figures below | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/reducciones-rendimiento-neto/arrendamiento-inmuebles-destinados-vivienda/cuadro-reducciones-arrendamiento.html |
| Contracts signed before 26 May 2023 | 60% | "Contratos anteriores a 26 de mayo de 2023 60 por 100 En general. Redacción vigente a 31-12-2021" |
| Contracts signed on or after 26 May 2023, general case | 50% | "50 por 100 Para el resto de arrendamientos" |

So the plain answer to "is it still 60 per cent in Spain?" is: yes, but only for a contract signed before 26 May 2023, and only for as long as that contract runs. This page is in the Agencia Tributaria manual for 2025 and is headed "aplicables en 2025"; the wording it reproduces is the wording of the statute in force for 2026.

Second, the rungs, for contracts signed on or after that date. The enhanced percentages replace the general one only where their conditions are met at the moment the contract is signed, and they apply only while those conditions continue to be met.

**Reductions on the positive net income from letting a home: article 23.2 and article 23.3**

| Case | Reduction | Condition, in the statute's own terms |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| New contract in a stressed residential market area with the rent cut | 90% | A new contract by the same landlord on a home in a "zona de mercado residencial tensionado" where the initial rent is cut by more than the percentage in the row below against the last rent of the previous contract on the same home, after applying that contract's annual uprating clause |
| The rent cut that the row above requires | 5% | "la renta inicial se hubiera rebajado en más de un 5 por ciento" |
| Young tenant in a stressed residential market area, first letting | 70% | Where the 90 per cent case is not met: the landlord lets the home for the first time, the home is in a stressed residential market area, and the tenant is aged between 18 and 35. With several tenants, the reduction applies only to the share of net income belonging to the tenants who qualify. |
| Public body or qualifying non-profit tenant | 70% | Where the 90 per cent case is not met: the tenant is a public administration or a non-profit within title II of Ley 49/2002 and the home goes to social letting below the state housing plan rent, to housing people in economic vulnerability under Ley 19/2021, or to a public housing programme that caps the rent |
| Recently refurbished home | 60% | Where neither the 90 per cent case nor either 70 per cent case is met: the home has undergone a rehabilitación within article 41.1 of the Reglamento, finished in the two years before the date the lease was signed |
| Any other case | 50% | "En un 50 por ciento, en cualquier otro caso." |
| Net income with a generation period over two years, or notoriously irregular, taxed in one year | 30% | Article 23.3, applied after the reduction above |
| Cap on the net income to which the row above applies | EUR 300,000 | "no podrá superar el importe de 300.000 euros anuales" |

What a reduction in the table above is, and is not:

- It applies only to POSITIVE net income. A loss is not reduced.
- It applies only to net income the taxpayer computed in a self-assessment filed BEFORE a data verification, limited review or inspection covering that income was started. Article 23.2 says so in terms.
- It never applies to the part of positive net income coming from income left out, or expenses wrongly deducted, and then regularised in such a procedure, even where the taxpayer declared or accepted the point during it.
- It never applies to a lease that breaches article 17.6 of the Ley de Arrendamientos Urbanos.
- "Rehabilitación" is not ordinary refurbishment. Article 41.1 of Real Decreto 439/2007 defines it as works subsidised under the state housing rehabilitation scheme, or works whose main object is reconstruction through work on structures, facades or roofs and similar, where the global cost exceeds the share in the table below of the acquisition price (if bought in the two years before the works started) or otherwise of the market value at that moment, land excluded. See https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820

**Rehabilitación: the cost test in article 41.1 of the Reglamento**

| Test | Value | Source text |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Share of the acquisition price, or of the market value where the home was not bought in the two years before the works began, that the global cost of the works must exceed, land excluded | 25% | "siempre que el coste global de las operaciones de rehabilitación exceda del 25 por ciento del precio de adquisición si se hubiese efectuado ésta durante los dos años inmediatamente anteriores al inicio de las obras de rehabilitación o, en otro caso, del valor de mercado que tuviera la vivienda en el momento de dicho inicio" |

- The stressed residential market areas are those in the resolution approved by the ministry responsible for housing, not a list in the tax statute.
- No reduction applies to a seasonal let, summer or otherwise: article 3 of the Ley de Arrendamientos Urbanos puts a seasonal let outside letting for use as a home.
- Letting to a legal person: as a general rule no reduction, because the property is not then destined to be a home with exclusive use by a named individual in the contract, and none either where the home is let to a company for generic use by its employees. The reduction DOES apply where it is proved that the home goes to named individuals, that is where from the outset the contract records the exclusive use of the home by a determined natural person (criterion of the Tribunal Económico-Administrativo Central of 8 September 2016). See https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/reducciones-rendimiento-neto/arrendamiento-inmuebles-destinados-vivienda.html
- No reduction applies to a tourist let, because it does not meet a permanent need for a home but a temporary one. Same page.

### 2.6 Interest Expense Limitation

- **Interest and repairs are capped together, per property** Article 23.1.a).1.º of Ley 35/2006 and article 13.a) of Real Decreto 439/2007 cap interest, other finance costs, and repair and maintenance costs TOGETHER at the gross income obtained from that property or right. They cannot create a loss by themselves. See https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764
- **The excess carries forward four years, not five** The excess is deductible "en los cuatro años siguientes", and in each of those years the same cap applies, per property: the total for these same items may not exceed that year's gross income from that property. The earlier version of this Guide said five years. See https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820
- **Other expenses are not capped this way** The property tax, community fees, insurance, management, supplies and depreciation are not inside this cap, so they can produce a negative net income.

### 2.7 Non-Resident Rental Income

A non-resident landlord with no permanent establishment in Spain is taxed under Real Decreto Legislativo 5/2004, separately for each accrual, and files modelo 210.

**Non-resident rates on Spanish rental income and imputed income**

| Who | Rate | Base |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527 |
| General rate, article 25.1.a) | 24% | Gross income, no expenses deducted |
| Resident of another EU member state, or of an EEA state with effective exchange of tax information, article 25.1.a) | 19% | Net income. Only these taxpayers may deduct expenses, under article 24.6. |

The Agencia Tributaria states which countries fall in the lower row: residents of the EU, Iceland, Norway and, with effect from 11 July 2021, Liechtenstein. An individual in that group may deduct the expenses provided in the IRPF law, provided the taxpayer shows they relate directly to the income obtained in Spain and have a direct and inseparable economic link with the activity carried on in Spain. See https://sede.agenciatributaria.gob.es/Sede/no-residentes/irnr-sin-establecimiento-permanente/cuestiones-especificas-sobre-tributacion-inmuebles/rendimientos-inmuebles-arrendados.html

Deadlines on modelo 210 changed in 2026, by Orden HAC/623/2026, of 12 June. The Agencia Tributaria note at https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-renta-no-residentes/modelo-210-irnr______a-no-residentes-permanente_/nota-modificaciones-plazos-presentacion-modelo-210.html sets out:

- Rental income accruing in April to September 2026 and declared without grouping keeps its old deadline: the first twenty calendar days of July and of October 2026, as the case may be.
- Rental income accruing in the last calendar quarter of 2026 and declared without grouping, where the return has tax to pay: the first twenty calendar days of April 2027.
- Rental income of the whole of 2026 declared grouped, where the return has tax to pay: the first twenty calendar days of April 2027. Grouping for rental income has been ANNUAL, not quarterly, for accruals from 2024. The note states this window for autoliquidaciones "con resultado a ingresar"; a nil or refund return follows the ordinary modelo 210 rules, which this Guide does not cover.
- Imputed income for 2026: 1 April to 31 December 2027. Imputed income for 2025 keeps 1 January to 31 December 2026.
- Direct debit for rental income runs 1 to 15 April of the year after accrual; for imputed income, 1 April to 23 December.
- Returns filed from 1 January 2027 use the new form content, including a new annex breaking down the deductible expenses of a let property, and new boxes for the number of days and the ownership share.

Also on modelo 210: where the non-resident has at least one person employed in Spain under an employment contract and full time for the ordering of the letting activity, the Agencia Tributaria says the activity may be understood to be a business carried on through a permanent establishment, and taxed under the permanent establishment rules instead.

### 2.8 Imputación de Rentas Inmobiliarias (Imputed Income)

- **Conditions for imputed income** Article 85 of Ley 35/2006 applies to urban property, and to rural property with buildings not indispensable to farming, forestry or livestock, where the property is NOT used in an economic activity and does NOT generate capital income, excluding the main home and undeveloped land. In plain terms: a second home that is neither let nor used in a business.
- **Nothing is deducted** The Agencia Tributaria states that no expense of any kind may be deducted from the imputed amount.
- **Owned in shares** Where several people own the property, each is treated as obtaining the income in proportion to their share. Where there is a right of enjoyment over the property, the holder of that right computes what the owner would have computed.
- **No imputation at all** Where the property is under construction, or cannot be used for planning reasons, no income is estimated.

**Imputed income: the statute in force for 2026**

| Case | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| General case, on the cadastral value | 2% | "la cantidad que resulte de aplicar el 2 por ciento al valor catastral", apportioned to the days in the tax period |
| Municipalities where the cadastral values were revised, modified or set in a general collective valuation that took effect in the tax period or in the ten preceding tax periods | 1.1% | Article 85.1, second paragraph |
| No cadastral value at the accrual date, or none notified to the owner: the rate that applies | 1.1% | "Si a la fecha de devengo del impuesto el inmueble careciera de valor catastral o éste no hubiera sido notificado al titular, el porcentaje será del 1,1 por ciento" |
| In that case the rate is applied to this share of the greater of the value checked by the administration for other taxes and the acquisition price | 50% | "se aplicará sobre el 50 por ciento del mayor de los siguientes valores" |

**Imputed income: what the Agencia Tributaria page says**

| Case | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://sede.agenciatributaria.gob.es/Sede/vivienda-otros-inmuebles/imputacion-rentas-inmobiliarias/calculo-renta-imputada.html |
| General case, on the cadastral value in the property tax receipt | 2% | "Con carácter general se aplicará el 2% sobre el valor catastral del inmueble que figure en el recibo del IBI" |
| Tax periods 2023, 2024 and 2025, where the cadastral values were revised, modified or set in a general collective valuation that took effect from 1 January 2012 | 1.1% | "El 1,1% en los siguientes supuestos" |

**The two official sources do not agree, and neither covers 2026 cleanly.** The statute in article 85 gives the reduced rate where the revision took effect in the tax period or in the ten preceding tax periods. The Agencia Tributaria page gives the reduced rate where the revision took effect from 1 January 2012, but says that rule applies to 2023, 2024 and 2025 only. Behind that page sits disposición adicional quincuagésima quinta of Ley 35/2006, which is still headed "durante el período impositivo 2023": attempts to extend it to 2025 and beyond, by Real Decreto-ley 16/2025 and Real Decreto-ley 2/2026, were each left without effect when the Congress of Deputies repealed those decrees. Do not place a client on one reading. Compute both, state the difference, and get the date the cadastral value was revised from the property tax receipt or the cadastre.

## Section 3: Transaction Pattern Library

### 3.1 Income Patterns

**Income Patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ALQUILER, RENTA MENSUAL, INQUILINO [name] | Rental income | Monthly rent receipt |
| IDEALISTA PAYMENTS, SPOTAHOME | Rental income | Platform letting, may be a tourist let |
| AIRBNB PAYOUT, BOOKING.COM PAYOUT | Tourist letting income | No reduction under article 23.2. Licensing rules differ by community. |
| FIANZA RETENIDA (retained deposit) | Income when retained | Assessable in the year of retention |
| INDEMNIZACIÓN DESISTIMIENTO, TRASPASO (received by landlord) | Rendimiento del capital inmobiliario | Income. Compensation the landlord PAYS to end the lease is an improvement instead: see section 2.3. |

### 3.2 Expense Patterns

**Expense Patterns**

| Pattern | Category | Treatment |
| --- | --- | --- |
| IBI, IMPUESTO BIENES INMUEBLES, AYUNTAMIENTO [city] | Property tax | Deductible |
| COMUNIDAD DE PROPIETARIOS, ADMINISTRADOR FINCAS | Community fees | Deductible |
| SEGURO HOGAR, MAPFRE, ZURICH, MUTUA | Insurance | Deductible |
| HIPOTECA INTERESES, [BANK] INTERESES | Mortgage interest | Deductible, inside the cap in section 2.6 |
| FONTANERO, ELECTRICISTA, REPARACIÓN | Repairs | Deductible if repair and not improvement, inside the cap in section 2.6 |
| ADMINISTRACIÓN FINCA, GESTIÓN ALQUILER | Management fees | Deductible |
| TASA BASURAS, RESIDUOS | Waste charge | Deductible |
| NOTARÍA, ABOGADO (tenancy) | Legal and formalisation costs | Deductible |
| SUMINISTROS, LUZ, AGUA, GAS (paid by landlord) | Supplies | Deductible |

### 3.3 Capital / Non-Deductible Patterns

**Capital / Non-Deductible Patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| REFORMA, REHABILITACIÓN, AMPLIACIÓN | Capital (improvement) | Adds to cost base. A rehabilitación may instead open the reduction in section 2.5: check article 41.1 of the Reglamento. |
| COCINA NUEVA, BAÑO NUEVO (full replacement) | Capital | Not a repair |
| HIPOTECA PRINCIPAL, AMORTIZACIÓN PRÉSTAMO | Not deductible | Principal repayment |
| MOBILIARIO, ELECTRODOMÉSTICOS | Not deducted at once | Depreciated: see section 2.4 |

## Section 4: Computation Method

### Step 1: Gross Rental Income (Rendimiento Íntegro)

- **Gross rental income** Everything the tenant must pay on every count for the year, including amounts for goods let with the property, and excluding value added tax (article 22.2 of Ley 35/2006). See https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764

### Step 2: Deductible Expenses (Gastos Deducibles)

- **Deductible expenses** Add up the expenses in section 2.2 for the days the property was let, including depreciation at the rates in section 2.4, and apply the interest-and-repairs cap in section 2.6.

### Step 3: Net Rental Income (Rendimiento Neto)

- **Net rental income** Gross income less deductible expenses, computed property by property.

### Step 4: Apply the reduction on letting a home, if applicable

- **Which reduction** Decide the ladder from the contract date, then the rung from the facts at signature, using the two tables in section 2.5. Apply it to POSITIVE net income only, and only if the return is filed before a verification, limited review or inspection of that income has started.

### Step 5: Report on Modelo 100

- **Report on Modelo 100** Declare the reduced net income in the rendimientos del capital inmobiliario section of the return, property by property. It forms part of the general taxable base, taxed at the escala general in section 1, not at the savings rates. For the 2025 return the filing window was 8 April to 30 June 2026: see https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c01-campana-declaracion-renta/confirmacion-borrador-presentacion-declaraciones/plazo-forma-presentacion.html

## Section 4A: Withholding on rent

A business or professional tenant of urban property must withhold from the rent it pays. A private individual renting a home for himself does not.

**Withholding on rent: rate and the Ceuta and Melilla credit**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Withholding on rent from letting or sub-letting urban property, article 101.8 | 19% | "subarrendamiento de bienes inmuebles urbanos, cualquiera que sea su calificación, será del 19 por ciento" |
| Credit for income obtained in Ceuta or Melilla, article 68.4 | 60% | "se deducirán el 60 por ciento de la parte de la suma de las cuotas íntegras" |

**When there is NO withholding, and the Ceuta and Melilla cut**

| Case | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Rents paid by one tenant to one landlord that do not exceed this amount in a year: no withholding, article 75.3.g).2.º | EUR 900 | "Cuando las rentas satisfechas por el arrendatario a un mismo arrendador no superen los 900 euros anuales" |
| Property in Ceuta or Melilla within article 68.4: the withholding percentage on rent in the table above is cut by this much | 60% | "Este porcentaje se reducirá en el 60 por ciento cuando el inmueble urbano esté situado en Ceuta o Melilla" |

This cut belongs to the rent withholding paragraph. Article 101 of Ley 35/2006 grants the Ceuta and Melilla cut paragraph by paragraph, so it may not be carried across to any other withholding percentage without reading that paragraph.

The other two cases with no withholding, in article 75.3.g) of Real Decreto 439/2007, carry no figure:

1. Letting of a home by a company for its employees (article 75.3.g).1.º).
2. Where the landlord's activity is classified in one of the headings of group 861 of section one of the tariffs of the Impuesto sobre Actividades Económicas, or in another heading permitting the letting or sub-letting of urban property, and applying to the cadastral value of the properties let the rules for working out the quota in those headings would not have produced a nil quota. The landlord must prove this to the tenant (article 75.3.g).3.º).

The rate in the table above is applied to everything paid to the landlord, value added tax excluded. The tenant declares it on modelo 115: see https://sede.agenciatributaria.gob.es/Sede/irpf/retenciones-ingresos-cuenta-pagos-fraccionados/retenciones-ingresos-cuenta/modelo-115.html

## Section 5: Tourist Rental (Vivienda de Uso Turístico)

A tourist let is a letting for a use other than as a home, because its main purpose is not to meet a permanent need for a home.

**Tourist Rental (Vivienda de Uso Turístico)**

| Item | Detail |
| --- | --- |
| Reduction under article 23.2 | NOT available. A tourist let meets a temporary need, not a permanent need for a home. |
| Income category, no hotel services and no full-time employee | Rendimientos del capital inmobiliario |
| Income category, with services proper to the hotel trade | Rendimientos de actividades económicas |
| Income category, with at least one full-time employee under an employment contract | Rendimientos de actividades económicas |
| What counts as hotel services | Permanent and continuous reception and customer attention in a space for the purpose; periodic cleaning of the property and the accommodation; periodic change of bed and bath linen; other services such as laundry, luggage custody, press, bookings; sometimes food and restaurant services |
| What does NOT count as hotel services | Cleaning at entry and exit of each tenant's contracted period; change of linen at entry and exit; cleaning of the common areas of the building and the estate; technical assistance and maintenance for repairs to plumbing, electrics, glass, blinds, locks and appliances |
| Comunidad rules | Each region has its own licensing requirements (licencia turística). Those rules are not on an allowed host and are not stated here. |
| Platform reporting | Modelo 179 is NOT in force for 2024 onwards. The duty moved to the platform operators' reporting rules, with modelo 040 for registration and modelo 238 for the information itself. |
| Landlord's own return | The income still goes on the resident return, or on modelo 210 for a non-resident |

Sources for the table above: https://sede.agenciatributaria.gob.es/Sede/vivienda-otros-inmuebles/tributacion-arrendador-viviendas-otros-inmuebles/tributacion-alquiler-apartamentos-turisticos.html and https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/reducciones-rendimiento-neto/arrendamiento-inmuebles-destinados-vivienda.html

**Value added tax on a tourist let**

| Case | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://sede.agenciatributaria.gob.es/Sede/vivienda-otros-inmuebles/tributacion-arrendador-viviendas-otros-inmuebles/tributacion-alquiler-apartamentos-turisticos/impuesto-sobre-valor-anadido.html |
| Tourist accommodation let WITH services proper to the hotel trade | 10% | "deberá tributar al tipo reducido del 10 por 100 como un establecimiento hotelero" |

Where the landlord does NOT supply services proper to the hotel trade, the Agencia Tributaria page above says the letting is exempt from value added tax and instead falls under the transfer tax (Impuesto sobre Transmisiones Patrimoniales), whose tariff each autonomous community sets. That page was last updated in 2023 and it relies on rulings of the Dirección General de Tributos. The exemption itself is article 20.Uno.23.º of Ley 37/1992, whose exception e´) removes the exemption for furnished flats or homes where the landlord undertakes to supply any of the complementary services proper to the hotel trade: see https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740

## Section 6: Edge Cases

### 6.1 Partially Rented Year

- **Partially rented year** Interest and other finance costs, insurance, community fees, the property tax, supplies and the rest belong to the number of days of the year the property was let. For the days it was not let, imputed income under section 2.8 applies, computed in proportion to those days. See https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/gastos-deducibles/cantidades-destinadas-amortizacion.html
- **Successive or simultaneous uses** Where a property is let for part of the year and at the owner's disposal for the rest, the letting part is rendimiento del capital inmobiliario and the rest is imputed income. The same split applies where only part of the property is let.
- **Waiting for a tenant is not the same as let** A property that is not let but is intended to be let (an inmueble en expectativa de alquiler) produces imputed income for that period, and no expense of that period is deductible, because no rental income arises in it. The Agencia Tributaria states it as "Las rentas procedentes de bienes inmuebles, que no se encuentran arrendados ni subarrendados, pero que están destinados a serlo (inmuebles en expectativa de alquiler), tributan como rentas imputadas y no cabe deducir gastos correspondientes a ese periodo", following the Tribunal Supremo judgment 270/2021 of 25 February. See https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/rendimientos-capital-inmobiliario/concepto-rendimientos-capital-inmobiliario.html

### 6.2 Below-Market Rent (e.g., to family)

- **The statutory rule is about relatives, not about market rent** Article 24 of Ley 35/2006 says that where the tenant or sub-tenant is the taxpayer's spouse or a relative, including relatives by affinity, up to and including the third degree, the total net income may not be lower than the amount the rules of article 85 would give. That is the imputed income figure in section 2.8, not a market rent. The Agencia Tributaria applies it as a comparison made last: the reduced net income for that property is the greater of the net income after any reduction in section 2.5, and the minimum computable because of the kinship. See https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764
- **What this Guide does not say** There is no general rule on an allowed page that the Agencia Tributaria imputes a market rent whenever rent is below market to an unrelated tenant. An earlier version of this Guide said so; it has been removed. Separate rules on estimated income and related-party transactions exist and are outside this Guide.

### 6.3 Co-Ownership (Proindiviso)

- **Co-ownership** Each co-owner reports the share of income and expenses matching their share of ownership, and article 85.2 applies the same rule to imputed income.

### 6.4 Rental at a Loss

- **Rental at a loss** A negative net rental income is part of the general tax base and can be set against other general income under the offsetting rules. The reductions in section 2.5 do NOT apply to a loss: they apply only to positive net income. The Agencia Tributaria worked example makes the same point.
- **What cannot create the loss** Interest, other finance costs and repairs cannot by themselves make the net income negative, because of the cap in section 2.6. A loss must come from the other expenses.

### 6.5 Non-Resident with Multiple Properties

- **Non-resident with multiple properties** A non-resident taxed without a permanent establishment is taxed separately for each accrual. Imputed income on an unlet property is also declared on modelo 210. Since accruals from 2024, rental income may be grouped ANNUALLY rather than quarterly, and the 2026 deadlines are in section 2.7.

## The method, step by step

1. Decide whether the letting is an economic activity. Apply the test in article 27.2 of Ley 35/2006 (at least one person employed under an employment contract and full time) and the hotel-services test on the Agencia Tributaria page at https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/rendimientos-capital-inmobiliario/concepto-rendimientos-capital-inmobiliario.html If either is met, stop: this is business income, not capital inmobiliario.
2. Decide whether the owner is resident or non-resident. A non-resident without a permanent establishment is taxed under Real Decreto Legislativo 5/2004 on modelo 210, at the rates in section 2.7: https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527
3. Compute the gross income under article 22.2 of Ley 35/2006, value added tax excluded: https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764
4. Deduct the expenses in article 13 and depreciation under article 14 of Real Decreto 439/2007, apportioned to the days let, and apply the interest-and-repairs cap: https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820
5. Get the contract date. Before 26 May 2023, the old single reduction applies. On or after that date, work down the ladder in section 2.5 and prove the condition for the rung you pick: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/reducciones-rendimiento-neto/arrendamiento-inmuebles-destinados-vivienda.html
6. For any part of the year the property was not let, add imputed income under article 85 of Ley 35/2006, and record which of the two readings in section 2.8 you used and why: https://sede.agenciatributaria.gob.es/Sede/vivienda-otros-inmuebles/imputacion-rentas-inmobiliarias/calculo-renta-imputada.html
7. Check withholding. If the tenant is a business or professional, the rate in section 4A applies unless one of the three cases in article 75.3.g) of Real Decreto 439/2007 is met. The tenant files modelo 115: https://sede.agenciatributaria.gob.es/Sede/irpf/retenciones-ingresos-cuenta-pagos-fraccionados/retenciones-ingresos-cuenta/modelo-115.html
8. File. A resident declares on modelo 100 in the Renta campaign; a non-resident on modelo 210 within the deadlines in section 2.7: https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-renta-no-residentes/modelo-210-irnr______a-no-residentes-permanente_/nota-modificaciones-plazos-presentacion-modelo-210.html

## Ask the client first

- On what date was each lease signed? Before 26 May 2023, or on or after it? This decides which reduction ladder applies, and it is the single most common error in Spanish rental tax.
- Is the home the tenant's permanent home, or is the let seasonal, tourist or to a company? Only a permanent home let opens the reductions in section 2.5.
- Is the home in a stressed residential market area, and if so, is this a new contract with the rent cut, a first letting to a tenant aged between 18 and 35, or a let to a public body or qualifying non-profit? Each opens a different rung.
- Do you employ anyone full time under an employment contract to run the lettings, or supply hotel-type services? Either answer moves the income out of this Guide.
- Which autonomous community are you resident in? The community half of the tax and any community rental deduction are not on an allowed page for all communities, so they must be looked up separately.
- Do you have the property tax receipt showing the cadastral value split between land and construction, and the date the cadastral value was last revised? Without both, depreciation and imputed income cannot be computed.
- Is the tenant a business or a professional, and how much rent do they pay you in the year? That decides withholding and the exemption in section 4A.

## When to refuse or refer

- The letting is an economic activity under article 27.2 of Ley 35/2006, or hotel-type services are supplied. Refer to business income and, for a non-resident, to the permanent establishment rules.
- A total marginal rate for Spain is asked for. The community half of the escala general is not on an allowed host for every community. Give the state half and say the community half is missing.
- An autonomous community rental deduction is asked for, whether for the landlord or for the tenant. These are community law and are not on an allowed page for all communities. Refuse to generalise.
- The imputation rate for 2026 has to be certain. The statute and the Agencia Tributaria page do not agree, and neither covers 2026 cleanly. Give both and refer.
- Tourist licensing, registration of tourist homes, or municipal restrictions. These are regional and municipal rules, not on an allowed host.
- A treaty question, a Beckham regime question, or the capital gain on selling the property. Each is a separate Guide.
- Sub-letting from the sub-lessor's side: that is rendimientos del capital mobiliario, not covered here.
- Ceuta and Melilla beyond the two figures in section 4A. The wider Ceuta and Melilla regime is not covered here.
- A property in the Basque Country or Navarra. Those territories have their own income tax laws, which are not on the hosts used here.

## Sources

- https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764
- https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820
- https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527
- https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740
- https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/rendimientos-capital-inmobiliario/concepto-rendimientos-capital-inmobiliario.html
- https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/gastos-deducibles/cantidades-destinadas-amortizacion.html
- https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/reducciones-rendimiento-neto/arrendamiento-inmuebles-destinados-vivienda.html
- https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c04-rendimientos-capital-inmobiliario/reducciones-rendimiento-neto/arrendamiento-inmuebles-destinados-vivienda/cuadro-reducciones-arrendamiento.html
- https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c01-campana-declaracion-renta/confirmacion-borrador-presentacion-declaraciones/plazo-forma-presentacion.html
- https://sede.agenciatributaria.gob.es/Sede/vivienda-otros-inmuebles/imputacion-rentas-inmobiliarias/calculo-renta-imputada.html
- https://sede.agenciatributaria.gob.es/Sede/no-residentes/irnr-sin-establecimiento-permanente/cuestiones-especificas-sobre-tributacion-inmuebles/rendimientos-inmuebles-arrendados.html
- https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-renta-no-residentes/modelo-210-irnr______a-no-residentes-permanente_/nota-modificaciones-plazos-presentacion-modelo-210.html
- https://sede.agenciatributaria.gob.es/Sede/irpf/retenciones-ingresos-cuenta-pagos-fraccionados/retenciones-ingresos-cuenta/modelo-115.html
- https://sede.agenciatributaria.gob.es/Sede/vivienda-otros-inmuebles/tributacion-arrendador-viviendas-otros-inmuebles/tributacion-alquiler-apartamentos-turisticos.html
- https://sede.agenciatributaria.gob.es/Sede/vivienda-otros-inmuebles/tributacion-arrendador-viviendas-otros-inmuebles/tributacion-alquiler-apartamentos-turisticos/impuesto-sobre-valor-anadido.html

## Section 7: Prohibitions

- **Prohibitions** NEVER quote a reduction percentage without the condition and the contract date that go with it; NEVER apply a reduction under article 23.2 to a tourist or seasonal let; NEVER apply a reduction under article 23.2 to a negative net income; NEVER apply a reduction under article 23.2 where the income was not in a self-assessment filed before a verification, limited review or inspection of that income began; NEVER let a non-resident outside the EU and EEA deduct expenses; NEVER depreciate the land component; NEVER exceed the building depreciation rate in section 2.4; NEVER deduct mortgage principal; NEVER let interest and repairs together exceed that property's gross income for the year; NEVER ignore imputed income for the days a non-main home was not let; NEVER state a total Spanish marginal rate without naming the autonomous community; NEVER present the imputation rate for 2026 as settled; NEVER present tax calculations as definitive, always label them as estimated.

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal, gestor administrativo, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
