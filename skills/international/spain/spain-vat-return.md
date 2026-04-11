---
name: spain-vat-return
description: Use this skill whenever asked to prepare, review, or create a Spanish VAT return (Modelo 303 / IVA autoliquidacion) for any client. Trigger on phrases like "prepare VAT return", "do the Spanish VAT", "fill in Modelo 303", "IVA", "Modelo 390", or any request involving Spanish VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Spanish VAT classification rules, Modelo 303 casilla (box) mappings, Modelo 390 annual summary structure, deductibility rules, reverse charge treatment (inversion del sujeto pasivo), recargo de equivalencia, SII real-time reporting, prorrata de deduccion, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any VAT-related work for Spain.
status: verified
version: 2.1-verified
---

# Spain VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Spain (Peninsula + Balearic Islands) |
| Jurisdiction Code | ES |
| Primary Legislation | Ley 37/1992, de 28 de diciembre, del Impuesto sobre el Valor Anadido (LIVA) |
| Regulations | Real Decreto 1624/1992, de 29 de diciembre (RIVA -- Reglamento del IVA) |
| SII Regulation | Real Decreto 596/2016 (Suministro Inmediato de Informacion) |
| Tax Authority | Agencia Estatal de Administracion Tributaria (AEAT) |
| Filing Portal | Sede Electronica AEAT (sede.agenciatributaria.gob.es) |
| Authentication | Certificado electronico, DNI electronico, or Cl@ve PIN |
| Contributor | DRAFT -- awaiting practitioner validation |
| Validated By | Deep research verification, April 2026 |
| Validation Date | 2026-04-10 |
| Skill Version | 2.1-verified |
| Territorial Exclusions | Canary Islands (IGIC, not IVA), Ceuta (IPSI), Melilla (IPSI) |
| Confidence Coverage | Tier 1: casilla assignment, reverse charge, deductibility blocks, derived calculations, recargo de equivalencia, SII obligation triggers. Tier 2: prorrata de deduccion, sector-specific regimes, regimen simplificado modules. Tier 3: complex group structures, IGIC/IPSI Canary Islands/Ceuta/Melilla, RECC cash-basis regime, regimen especial de bienes usados. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. An Asesor Fiscal (licensed tax advisor) must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to Asesor Fiscal and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and NIF** [T1] -- NIF (Numero de Identificacion Fiscal) for individuals; CIF for companies (now unified as NIF). NIF-IVA format: ES + letter + 8 digits (e.g., ESB12345678) or ES + 8 digits + letter (e.g., ES12345678A). LIVA Art. 164.Uno.1.
2. **Legal form** [T1] -- Persona fisica (individual/autonomo), Sociedad Limitada (SL), Sociedad Anonima (SA), Comunidad de Bienes (CB), etc. Impacts regime eligibility.
3. **VAT regime** [T1] -- Regimen general (standard), regimen simplificado (simplified modules), recargo de equivalencia (surcharge for retailers), regimen especial de criterio de caja (RECC -- cash basis), or exempt (Art. 20 LIVA). LIVA Art. 148-163 (recargo), Art. 122-123 (simplificado).
4. **Filing frequency** [T1] -- Quarterly (standard for most businesses) or monthly (mandatory for large companies with turnover > EUR 6,010,121.04, REDEME registrants, or SII-obliged entities). RIVA Art. 30.
5. **Industry/sector** [T2] -- Impacts prorrata and special regimes (construction, agriculture, used goods, travel agencies).
6. **Does the business make exempt supplies (Art. 20 LIVA)?** [T2] -- If yes, prorrata de deduccion required (Art. 102-106 LIVA). Examples: medical services, education, insurance, financial services.
7. **Is the client in recargo de equivalencia?** [T1] -- Applies to retailers who are personas fisicas selling goods without transformation. LIVA Art. 148-163.
8. **IVA credit carried forward from prior period** [T1] -- Casilla 67 (cuotas a compensar de periodos anteriores).
9. **Is the client in SII (Suministro Inmediato de Informacion)?** [T1] -- Mandatory for monthly filers; near-real-time invoice reporting within 4 calendar days. RD 596/2016.
10. **Is the client registered in REDEME?** [T1] -- Registro de Devolucion Mensual: voluntary monthly filing with monthly refund rights. RIVA Art. 30.
11. **Does the client perform operations with Canary Islands, Ceuta, or Melilla?** [T3] -- These territories use IGIC/IPSI, not IVA. Escalate.

For exempt clients [T1]: confirm activity falls under LIVA Art. 20 (exempt without right of deduction) or LIVA Art. 21-25 (exempt with right of deduction -- exports, intra-EU supplies).

**If items 1-4 are unknown, STOP. Do not classify any transactions until confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]

| Category | Treatment | Legal Basis |
|----------|-----------|-------------|
| Sale of goods/services (entregas de bienes / prestaciones de servicios) | IVA repercutido (output IVA) | LIVA Art. 4, Art. 5 (entregas), Art. 11 (prestaciones) |
| Purchase of goods/services | IVA soportado (input IVA) | LIVA Art. 92-94 |
| Salaries / nominas | OUT OF SCOPE | Not a supply |
| Social Security (Seguridad Social) | OUT OF SCOPE | Not a supply |
| IRPF withholdings | OUT OF SCOPE | Income tax, not IVA |
| Loan repayments | OUT OF SCOPE | Not a supply |
| Dividends | OUT OF SCOPE | Not a supply |
| Bank charges | EXEMPT without deduction right | LIVA Art. 20.Uno.18 |

**Legislation:** LIVA Art. 4 (taxable transactions -- hecho imponible).

### 1b. Determine Counterparty Location [T1]

| Territory | IVA Treatment | Notes |
|-----------|---------------|-------|
| Spain -- Peninsula + Balearic Islands | Standard IVA applies | TAI (Territorio de Aplicacion del Impuesto) per LIVA Art. 3 |
| Canary Islands | IGIC applies, NOT IVA | Impuesto General Indirecto Canario. Escalate [T3]. LIVA Art. 3.Dos |
| Ceuta | IPSI applies, NOT IVA | Impuesto sobre la Produccion, los Servicios y la Importacion. Escalate [T3]. LIVA Art. 3.Dos |
| Melilla | IPSI applies, NOT IVA | Same as Ceuta. Escalate [T3]. LIVA Art. 3.Dos |
| EU Member States | Intra-Community regime | LIVA Art. 13-16 (acquisitions), Art. 25 (exempt supplies) |
| Non-EU / Third territories | Import/export regime | LIVA Art. 17-19 (imports), Art. 21-22 (export exemptions) |

**Critical:** Canary Islands, Ceuta, and Melilla are Spanish sovereign territory but are NOT within the TAI (Territorio de Aplicacion del Impuesto). Supplies to/from these territories are treated similarly to exports/imports, not domestic transactions. LIVA Art. 3.Dos.

### 1c. Determine VAT Rate [T1]

**Legislation:** LIVA Art. 90 (general rate), Art. 91 (reduced and super-reduced rates).

#### 21% -- Tipo General (Standard Rate) -- LIVA Art. 90

Default rate for all supplies of goods and services not specifically listed in Art. 91.

| Supply Category | Examples | Legal Basis |
|----------------|----------|-------------|
| Professional services | Legal, consulting, accounting, architecture | LIVA Art. 90 (default) |
| Electronics and technology | Computers, phones, software licences | LIVA Art. 90 |
| Clothing and footwear | All apparel not specifically reduced | LIVA Art. 90 |
| Furniture and household goods | Office furniture, appliances | LIVA Art. 90 |
| Telecommunications | Phone plans, internet services | LIVA Art. 90 |
| Alcoholic beverages | Wine, beer, spirits | LIVA Art. 90 |
| Tobacco | All tobacco products | LIVA Art. 90 |
| Cosmetics and perfumery | Non-medical personal care | LIVA Art. 90 |
| Jewellery and luxury goods | Precious metals, gems (non-trade) | LIVA Art. 90 |
| Vehicles and accessories | Cars, motorbikes, parts | LIVA Art. 90 |

#### 10% -- Tipo Reducido (Reduced Rate) -- LIVA Art. 91.Uno

| Supply Category | Examples | Legal Basis |
|----------------|----------|-------------|
| Food products (general) | Meat, fish, eggs, vegetables, fruit (not super-reduced) | LIVA Art. 91.Uno.1.1 |
| Water | All water supplies for human consumption | LIVA Art. 91.Uno.1.4 |
| Passenger transport | Bus, train, taxi, air (domestic) | LIVA Art. 91.Uno.2.1 |
| Hotel and accommodation | Hotels, hostels, camping (not long-term rental) | LIVA Art. 91.Uno.2.2 |
| Restaurant and catering | Eating/drinking on premises, takeaway | LIVA Art. 91.Uno.2.3 |
| Live cultural events | Theatre, cinema, concerts, exhibitions | LIVA Art. 91.Uno.2.6 |
| Housing -- new construction | First delivery of new residential property | LIVA Art. 91.Uno.1.7 |
| Renovation of private dwellings | Works on housing > 2 years old (conditions apply) | LIVA Art. 91.Uno.2.10 |
| Agricultural inputs | Seeds, fertilisers, animal feed (not super-reduced) | LIVA Art. 91.Uno.1.3 |
| Medical devices and equipment | Glasses, contact lenses, hearing aids (not super-reduced) | LIVA Art. 91.Uno.1.6 |
| Funeral services | Coffins, burial, cremation | LIVA Art. 91.Uno.2.4 |
| Cleaning of public roads | Street cleaning, waste collection | LIVA Art. 91.Uno.2.9 |

#### 4% -- Tipo Superreducido (Super-Reduced Rate) -- LIVA Art. 91.Dos

| Supply Category | Examples | Legal Basis |
|----------------|----------|-------------|
| Bread and bread-making flour | All varieties of bread, base flour | LIVA Art. 91.Dos.1.1 |
| Milk | Natural, certified, pasteurised, concentrated, skimmed, sterilised | LIVA Art. 91.Dos.1.1 |
| Cheese and eggs | All varieties | LIVA Art. 91.Dos.1.1 |
| Fruit and vegetables | Fresh, natural, chilled (unprocessed) | LIVA Art. 91.Dos.1.1 |
| Cereals and tubers | Natural, unprocessed (potatoes, rice, etc.) | LIVA Art. 91.Dos.1.1 |
| Olive oil | All varieties of olive oil (virgin, extra-virgin, refined). Permanent super-reduced rate from 1 January 2025. | LIVA Art. 91.Dos.1.1 |
| Books and newspapers | Physical and electronic books, periodicals, newspapers | LIVA Art. 91.Dos.1.2 |
| Medicines for human use | Prescription and OTC (for human consumption) | LIVA Art. 91.Dos.1.3 |
| Vehicles for disabled persons | Wheelchairs, adapted vehicles for persons with disability | LIVA Art. 91.Dos.1.4 |
| Social housing (VPO) | Vivienda de proteccion oficial (state-subsidised housing) | LIVA Art. 91.Dos.1.6 |
| Prostheses and implants | Medical prostheses, dental implants | LIVA Art. 91.Dos.1.5 |
| Feminine hygiene products | Sanitary towels, tampons (since 2023 reform) | LIVA Art. 91.Dos.1.1 bis |

#### 0% -- Temporary Zero Rate

Temporary 0% rates were applied to specific basic food items during 2023-2024 under Royal Decree-Law 20/2022 and extensions. These expired as follows: basic staples (bread, milk, cheese, eggs, fruit, vegetables, cereals) returned to 4% from 1 January 2025; olive oil moved permanently to 4% super-reduced from 1 January 2025; seed oils and pasta returned to 10% from 1 January 2025. **As of 2025, no 0% food VAT rates remain in force.** Casillas 150-152 on Modelo 303 (introduced in 2023 for 0% rate operations) should be zero for periods from 1 January 2025 onward unless new temporary measures are enacted. **Always verify current status with AEAT guidance for the filing period.** [T2]

### 1d. Determine Expense Category [T1]

| Category | Definition | Legal Basis |
|----------|-----------|-------------|
| Bienes de inversion (capital assets) -- movable | Movable goods with acquisition cost > EUR 3,005.06 and useful life > 1 year | LIVA Art. 108.Uno |
| Bienes de inversion (capital assets) -- immovable | All immovable property (buildings, land) regardless of value | LIVA Art. 108.Dos |
| Stock / mercancias | Goods acquired for resale without transformation | LIVA Art. 92 |
| Bienes corrientes (current goods) | Raw materials, consumables used in production | LIVA Art. 92 |
| Servicios / gastos generales | Overhead: rent, utilities, professional fees, subscriptions | LIVA Art. 92 |

---

## Step 2: VAT Return Form Structure -- Modelo 303 [T1]

### Overview

| Field | Detail |
|-------|--------|
| Form | Modelo 303 -- Impuesto sobre el Valor Anadido, Autoliquidacion |
| Frequency | Quarterly (1T, 2T, 3T, 4T) or monthly (01-12) |
| Filing method | Sede Electronica AEAT (electronic only for most entities) |
| Legal basis | LIVA Art. 164; RIVA Art. 71 |

**Legislation:** LIVA Art. 164 (filing obligations); RIVA Art. 71 (form and deadlines).

### Section I: Identificacion (Identification)

| Casilla | Spanish Name | English Translation | Content |
|---------|-------------|---------------------|---------|
| -- | NIF | Numero de Identificacion Fiscal | Entity tax ID |
| -- | Razon social / Apellidos y nombre | Company name / Surname and first name | Legal name |
| -- | Ejercicio / Periodo | Tax year / Period | e.g., 2026 / 1T |
| -- | Tipo de declaracion | Type of return | Ordinaria, complementaria, sustitutiva |

### Section II: Liquidacion -- IVA Devengado (Output IVA)

#### Regimen General (Standard Regime)

| Casilla | Spanish Name | English Translation | Content | Derived? |
|---------|-------------|---------------------|---------|----------|
| 01 | Base imponible al 4% | Taxable base at 4% | Total net value of supplies at super-reduced rate | No -- from records |
| 02 | Tipo % | Rate % | Always 4 | Fixed |
| 03 | Cuota | Tax amount | = Casilla 01 x 0.04 | Yes -- derived |
| 04 | Base imponible al 10% | Taxable base at 10% | Total net value of supplies at reduced rate | No -- from records |
| 05 | Tipo % | Rate % | Always 10 | Fixed |
| 06 | Cuota | Tax amount | = Casilla 04 x 0.10 | Yes -- derived |
| 07 | Base imponible al 21% | Taxable base at 21% | Total net value of supplies at standard rate | No -- from records |
| 08 | Tipo % | Rate % | Always 21 | Fixed |
| 09 | Cuota | Tax amount | = Casilla 07 x 0.21 | Yes -- derived |

#### Operaciones al 0% (Zero-Rate Operations) -- Casillas added in 2023

| Casilla | Spanish Name | English Translation | Content | Derived? |
|---------|-------------|---------------------|---------|----------|
| 150 | Base imponible al 0% | Taxable base at 0% | Total net value of supplies at temporary 0% rate | No -- from records |
| 151 | Tipo % | Rate % | Always 0 | Fixed |
| 152 | Cuota | Tax amount | = 0 | Yes -- derived |

**Note:** Casillas 150-152 were introduced for the temporary 0% food VAT rates (2023-2024). From 1 January 2025, no 0% food rates remain in force; these casillas should be zero unless new temporary measures are enacted. Casillas 153-155 (5% rate, used for energy during 2022-2023) also exist on the form but are not currently in active use for standard filers.

#### Adquisiciones Intracomunitarias (Intra-Community Acquisitions)

| Casilla | Spanish Name | English Translation | Content | Derived? |
|---------|-------------|---------------------|---------|----------|
| 10 | Base imponible -- adquisiciones intracomunitarias de bienes | Taxable base -- intra-EU goods acquisitions | Net value of goods acquired from EU suppliers | No -- from records |
| 11 | Cuota | Tax amount | Self-assessed IVA on EU goods at applicable rate | Yes -- derived |

#### Otras operaciones con inversion del sujeto pasivo (Other Reverse Charge Operations)

| Casilla | Spanish Name | English Translation | Content | Derived? |
|---------|-------------|---------------------|---------|----------|
| 12 | Base imponible -- otras operaciones con ISP | Taxable base -- other reverse charge operations | Net value of services/goods received under reverse charge (Art. 84.Uno.2 LIVA): EU services, non-EU services, construction subcontracting, scrap, certain real estate | No -- from records |
| 13 | Cuota | Tax amount | Self-assessed IVA on reverse charge operations at applicable rate | Yes -- derived |

#### Recargo de Equivalencia (Equivalence Surcharge) -- Output Side

| Casilla | Spanish Name | English Translation | Content | Derived? |
|---------|-------------|---------------------|---------|----------|
| 14 | Base imponible RE al 0.5% | RE base at 0.5% | Base for super-reduced rate surcharge | No |
| 15 | Cuota RE 0.5% | RE tax 0.5% | = Casilla 14 x 0.005 | Yes |
| 16 | Base imponible RE al 1.4% | RE base at 1.4% | Base for reduced rate surcharge | No |
| 17 | Cuota RE 1.4% | RE tax 1.4% | = Casilla 16 x 0.014 | Yes |
| 18 | Base imponible RE al 5.2% | RE base at 5.2% | Base for standard rate surcharge | No |
| 19 | Cuota RE 5.2% | RE tax 5.2% | = Casilla 18 x 0.052 | Yes |

#### Modificaciones y Otros

| Casilla | Spanish Name | English Translation | Content | Derived? |
|---------|-------------|---------------------|---------|----------|
| 22 | Base imponible RE al 1.75% | RE base at 1.75% | Base for tobacco surcharge | No |
| 23 | Cuota RE 1.75% | RE tax 1.75% | = Casilla 22 x 0.0175 | Yes |
| 24 | Modificacion de bases y cuotas -- base | Adjustment to bases and tax (base) | Credit notes, corrections, bad debt relief (Art. 80 LIVA). Positive or negative. | No |
| 25 | Modificacion de bases y cuotas -- cuota | Adjustment to bases and tax (tax amount) | Corresponding tax adjustment | No |

#### Total IVA Devengado

| Casilla | Spanish Name | English Translation | Calculation |
|---------|-------------|---------------------|-------------|
| 27 | Total cuota devengada | Total output IVA due | = 03 + 06 + 09 + 11 + 13 + 15 + 17 + 19 + 23 + 25 |

### Section III: IVA Deducible (Input IVA)

#### Operaciones Interiores (Domestic Purchases)

| Casilla | Spanish Name | English Translation | Content | Derived? |
|---------|-------------|---------------------|---------|----------|
| 28 | Base -- operaciones interiores corrientes | Base -- domestic current operations | Net value of domestic purchases (goods and services, not capital) | No |
| 29 | Cuota -- operaciones interiores corrientes | Tax -- domestic current operations | Deductible input IVA on domestic purchases | No |
| 30 | Base -- bienes de inversion interiores | Base -- domestic capital assets | Net value of domestic capital asset purchases | No |
| 31 | Cuota -- bienes de inversion interiores | Tax -- domestic capital assets | Deductible input IVA on domestic capital assets | No |

#### Importaciones (Imports from Non-EU -- Goods through Customs)

| Casilla | Spanish Name | English Translation | Content | Derived? |
|---------|-------------|---------------------|---------|----------|
| 32 | Base -- importaciones corrientes | Base -- imports current operations | Net value of imports of goods (customs value + duties). Only goods that pass through customs with DUA. | No |
| 33 | Cuota -- importaciones corrientes | Tax -- imports current operations | IVA paid at customs or deferred (DUA document) | No |
| 34 | Base -- importaciones bienes de inversion | Base -- imports capital assets | Net value of imported capital assets (goods through customs) | No |
| 35 | Cuota -- importaciones bienes de inversion | Tax -- imports capital assets | IVA on imported capital assets | No |

#### Adquisiciones Intracomunitarias (Intra-EU Purchases -- Input Side)

| Casilla | Spanish Name | English Translation | Content | Derived? |
|---------|-------------|---------------------|---------|----------|
| 36 | Base -- adquisiciones intracomunitarias corrientes | Base -- intra-EU current goods and services | Net value of intra-EU purchases of goods and services (not capital) | No |
| 37 | Cuota -- adquisiciones intracomunitarias corrientes | Tax -- intra-EU current goods and services | Self-assessed input IVA on EU acquisitions | No |
| 38 | Base -- bienes de inversion intracomunitarios | Base -- intra-EU capital assets | Net value of intra-EU capital asset acquisitions | No |
| 39 | Cuota -- bienes de inversion intracomunitarios | Tax -- intra-EU capital assets | Self-assessed input IVA on EU capital assets | No |

**Note on non-EU B2B services:** Services received from non-EU suppliers under reverse charge (Art. 84.Uno.2.a LIVA) are reported on the input side in casillas 28/29 (domestic current operations) or 30/31 (if capital), NOT in casillas 32-35 (which are exclusively for goods imported through customs). The output side for such services goes in casillas 12/13.

#### Regularizaciones (Adjustments)

| Casilla | Spanish Name | English Translation | Content | Derived? |
|---------|-------------|---------------------|---------|----------|
| 40 | Rectificacion de deducciones | Correction of deductions | Adjustments for prior period errors, Art. 114 LIVA | No |
| 41 | Regularizacion bienes de inversion | Capital goods regularisation | Annual adjustment of capital goods deductions over 5 years (movable) or 10 years (immovable). LIVA Art. 107-110 | No |
| 42 | Regularizacion por prorrata definitiva | Definitive pro-rata regularisation | Adjustment when provisional prorrata differs from definitive. Only in Q4/December. LIVA Art. 105 | No |

#### Total IVA Deducible

| Casilla | Spanish Name | English Translation | Calculation |
|---------|-------------|---------------------|-------------|
| 45 | Total a deducir | Total deductible input IVA | = 29 + 31 + 33 + 35 + 37 + 39 + 40 + 41 + 42 (casilla numbers unchanged; order: domestic + imports + intra-EU + adjustments) |

### Section IV: Resultado (Result)

| Casilla | Spanish Name | English Translation | Calculation |
|---------|-------------|---------------------|-------------|
| 46 | Diferencia | Difference | = Casilla 27 - Casilla 45 |
| 47-58 | (Reserved for complementary declarations) | -- | -- |
| 59 | Resultado regimen simplificado | Simplified regime result | Only for regimen simplificado filers |
| 60 | Suma de resultados | Sum of results | = Casilla 46 + Casilla 59 (if applicable) |
| 61 | Porcentaje atribuible a la Administracion del Estado | % attributable to State | 100% for most filers; adjusted for Pais Vasco/Navarra |
| 62 | Atribuible a la Administracion del Estado | Amount attributable to State | = Casilla 60 x Casilla 61 / 100 |
| 63 | Cuotas a compensar de periodos anteriores aplicadas | Prior period credits applied | Credits from Casilla 67 of prior period |
| 64 | Resultado de la autoliquidacion | Self-assessment result | = Casilla 62 - Casilla 63 |
| 65 | A deducir: resultado de la declaracion anterior | Deduct: prior return result | Only for complementary returns |
| 66 | Resultado de la liquidacion | Settlement result | = Casilla 64 - Casilla 65 |
| 67 | Cuotas a compensar de periodos anteriores | Credits to carry forward from prior periods | Accumulated negative balances not yet offset |
| 71 | Resultado ingreso/devolucion | Final result: payment / refund | Final amount payable (positive) or refundable (negative, only in last period or REDEME) |

### Section V: Sin Actividad

| Casilla | Spanish Name | English Translation | Content |
|---------|-------------|---------------------|---------|
| 69 | Sin actividad | No activity | Tick if no economic activity in the period. Return still filed. LIVA Art. 164. |

### Section VI: Datos Adicionales (Q4 / December Only)

| Casilla | Spanish Name | English Translation | Content |
|---------|-------------|---------------------|---------|
| 80-99 | Various annual summary data | Annual regularisation data | Total annual turnover, exempt operations, prorrata adjustments, sector-specific data. Only completed in Q4 (quarterly filers) or December (monthly filers). |

---

## Step 2b: Modelo 390 -- Annual Summary (Declaracion-Resumen Anual) [T1]

### Overview

| Field | Detail |
|-------|--------|
| Form | Modelo 390 -- Declaracion-Resumen Anual del IVA |
| Frequency | Annual (covers full calendar year) |
| Deadline | 1-30 January of following year |
| Filing method | Sede Electronica AEAT |
| Legal basis | RIVA Art. 71.4; LIVA Art. 164.Uno.6 |
| Exemption from filing | SII-obliged entities are EXEMPT from filing Modelo 390 (since 2017) |

**Legislation:** RIVA Art. 71.4 (annual summary obligation); RD 596/2016 (SII exemption from Modelo 390).

### Key Sections of Modelo 390

| Section | Content |
|---------|---------|
| 1. Identificacion | NIF, entity name, tax year |
| 2. Devengo | Output IVA -- mirrors Modelo 303 totals for the full year |
| 3. IVA deducible | Input IVA -- mirrors Modelo 303 totals for the full year |
| 4. Resultado liquidacion anual | Annual result (should equal sum of Modelo 303 results) |
| 5. Volumen de operaciones | Total turnover (Art. 121 LIVA) including: domestic taxable, intra-EU, exports, exempt |
| 6. Operaciones especificas | Intra-EU acquisitions, imports, reverse charge received, non-subject operations |
| 7. Prorrata | Provisional and definitive prorrata percentages; sector differentiation if applicable |
| 8. Actividades con regimen de deduccion diferenciado | Sectored activities (prorrata especial) |
| 9. Datos estadisticos | Statistical data on the nature of supplies by rate and type |

### Modelo 390 Cross-Checks

- Sum of all Modelo 303 Casilla 27 values across periods must equal Modelo 390 total output IVA [T1]
- Sum of all Modelo 303 Casilla 45 values across periods must equal Modelo 390 total input IVA [T1]
- Annual prorrata definitiva in Modelo 390 must match the Q4/December regularisation in Casilla 42 [T1]

---

## Step 3: Transaction Classification Matrix [T1]

### Lookup Table: Sales (IVA Devengado / Output)

| Transaction Type | Counterparty Location | Rate | Casilla (Base) | Casilla (Tax) | Legal Basis |
|-----------------|-----------------------|------|----------------|---------------|-------------|
| Domestic sale -- standard | Spain (TAI) | 21% | 07 | 09 | LIVA Art. 90 |
| Domestic sale -- reduced | Spain (TAI) | 10% | 04 | 06 | LIVA Art. 91.Uno |
| Domestic sale -- super-reduced | Spain (TAI) | 4% | 01 | 03 | LIVA Art. 91.Dos |
| Intra-EU B2B supply of goods | EU | Exempt (0%) | Not on 303 | -- | LIVA Art. 25; report on Modelo 349 |
| Intra-EU B2B supply of services | EU | Not subject | Not on 303 | -- | LIVA Art. 69-70; report on Modelo 349 |
| Export of goods (non-EU) | Non-EU | Exempt with deduction right | Not on 303 | -- | LIVA Art. 21 |
| Export of services (non-EU B2B) | Non-EU | Not subject | Not on 303 | -- | LIVA Art. 69.Uno |
| Supply to Canary Islands | Canary Islands | Exempt/not subject | Not on 303 | -- | LIVA Art. 21.2; treated like export [T3] |
| Supply with recargo de equivalencia | Spain (TAI) | 21%+5.2% | 07+18 | 09+19 | LIVA Art. 148-163 |
| Credit note issued | Spain (TAI) | Negative | 24 | 25 | LIVA Art. 80 |

### Lookup Table: Purchases (IVA Deducible / Input)

| Transaction Type | Counterparty Location | Category | Casilla (Base) | Casilla (Tax) | Legal Basis |
|-----------------|-----------------------|----------|----------------|---------------|-------------|
| Domestic purchase -- current | Spain (TAI) | Overhead/stock | 28 | 29 | LIVA Art. 92 |
| Domestic purchase -- capital asset | Spain (TAI) | Capital (> EUR 3,005.06) | 30 | 31 | LIVA Art. 108 |
| EU goods acquisition -- current | EU | Overhead/stock | 36 | 37 | LIVA Art. 13 |
| EU goods acquisition -- capital | EU | Capital | 38 | 39 | LIVA Art. 13, 108 |
| EU services received (B2B) | EU | Overhead | 36 | 37 | LIVA Art. 69-70 |
| Non-EU import of goods -- current | Non-EU | Overhead/stock | 32 | 33 | LIVA Art. 17-19 |
| Non-EU import of goods -- capital | Non-EU | Capital | 34 | 35 | LIVA Art. 17-19, 108 |
| Non-EU services received (B2B) | Non-EU | Overhead | 28 | 29 | LIVA Art. 69-70, 84.Uno.2.a (reverse charge; input reported as domestic) |
| Reverse charge received (construction, scrap, etc.) | Spain (TAI) | Any | 28 or 30 | 29 or 31 | LIVA Art. 84.Uno.2 |
| Capital goods regularisation | -- | -- | -- | 41 | LIVA Art. 107-110 |
| Prorrata definitiva regularisation | -- | -- | -- | 42 | LIVA Art. 105 |

### Lookup Table: Reverse Charge -- Output Side (Self-Assessment)

When reverse charge applies, the recipient ALSO records output IVA:

| Transaction Type | Output Casilla (Base) | Output Casilla (Tax) | Input Casilla (Base) | Input Casilla (Tax) |
|-----------------|----------------------|---------------------|---------------------|---------------------|
| EU goods acquisition | 10 | 11 | 36 or 38 | 37 or 39 |
| EU/non-EU services, construction RC, scrap, etc. | 12 | 13 | 28 or 30 | 29 or 31 |

---

## Step 4: Reverse Charge -- Inversion del Sujeto Pasivo [T1]

**Legislation:** LIVA Art. 84.Uno.2.

### When Reverse Charge Applies

The RECIPIENT becomes the sujeto pasivo (taxable person) in the following cases:

| Situation | Specific Provision | Conditions |
|-----------|-------------------|------------|
| Services from EU/non-EU businesses (B2B) | LIVA Art. 84.Uno.2.a | Supplier not established in TAI; recipient is empresario/profesional |
| Intra-Community acquisition of goods | LIVA Art. 13 | Goods shipped from another EU state to TAI; supplier charges 0% |
| Construction services (subcontracting) | LIVA Art. 84.Uno.2.f | Ejecuciones de obra (construction works) including renovation, demolition, when recipient is main contractor or developer (promotor) |
| Waste and scrap materials (chatarra) | LIVA Art. 84.Uno.2.b | Sale of industrial waste, scrap metal, residual materials |
| Gold (not for jewellery) | LIVA Art. 84.Uno.2.c | Investment gold and semi-finished gold products |
| Mobile phones, tablets, laptops, game consoles | LIVA Art. 84.Uno.2.g | Only when total invoice value > EUR 5,000 (anti-fraud) |
| Gas and electricity by non-established traders | LIVA Art. 84.Uno.2.d | Supplier not established in TAI |
| Emissions trading (derechos de emision) | LIVA Art. 84.Uno.2.e | CO2 emissions allowances |
| Real estate -- certain supplies | LIVA Art. 84.Uno.2.e | Renunciation of exemption on second or subsequent supplies of immovable property (Art. 20.Dos LIVA) |
| Silver, platinum, and tin | LIVA Art. 84.Uno.2.b | Raw materials |

### Reverse Charge Mechanics

1. Supplier invoices WITHOUT IVA, noting "Inversion del sujeto pasivo -- Art. 84.Uno.2 LIVA" [T1]
2. Recipient reports net amount in output casillas (10/11 for EU goods; 12/13 for all other RC) [T1]
3. Recipient self-assesses IVA at applicable rate (21% standard, or reduced if applicable) [T1]
4. Recipient claims input IVA in corresponding deductible casillas (28/29 or 30/31 for domestic RC and non-EU services; 36/37 or 38/39 for EU acquisitions; 32/33 or 34/35 for imported goods through customs) [T1]
5. Net effect: ZERO for fully taxable businesses [T1]

### Reverse Charge Exceptions [T1]

| Situation | Treatment | Legal Basis |
|-----------|-----------|-------------|
| Out-of-scope payments (wages, loans, dividends) | NEVER reverse charge | Not a supply |
| Local consumption abroad (hotel, restaurant, taxi in another EU country) | NOT reverse charge; foreign VAT paid at source, irrecoverable | LIVA Art. 70 |
| Canary Islands / Ceuta / Melilla supplies | IGIC/IPSI applies, NOT IVA | LIVA Art. 3.Dos [T3] |
| EU supplier charged their local VAT > 0% | NOT reverse charge in Spain; expense includes foreign VAT | Supplier error if B2B; may need correction |
| B2C services from non-established supplier | Supplier may still be sujeto pasivo in some cases | LIVA Art. 84.Uno.1 [T2] |

---

## Step 5: Blocked Input Tax (IVA No Deducible) [T1]

**Legislation:** LIVA Art. 95-96.

### Fully Blocked Categories

| Category | Spanish Term | Rule | Legal Basis |
|----------|-------------|------|-------------|
| Entertainment and client hospitality | Atenciones a clientes | 100% BLOCKED -- no deduction regardless of business purpose | LIVA Art. 96.Uno.5 |
| Gifts to clients or third parties | Obsequios | 100% BLOCKED -- includes Christmas hampers, gift baskets, promotional gifts | LIVA Art. 96.Uno.5 |
| Food, drink, tobacco (hospitality) | Alimentacion, bebidas, tabaco | 100% BLOCKED when provided as entertainment | LIVA Art. 96.Uno.5 |
| Jewellery, gems, precious metals | Joyas, alhajas, piedras preciosas | 100% BLOCKED unless trade stock for resale | LIVA Art. 96.Uno.4 |
| Recreational goods and services | Espectaculos, servicios recreativos | 100% BLOCKED unless directly related to taxable activity (e.g., event organiser) | LIVA Art. 96.Uno.3 |
| Travel and accommodation (employee personal benefit) | Viajes, hosteleria | 100% BLOCKED unless directly and exclusively linked to taxable output | LIVA Art. 96.Uno.3 |

### Partially Deductible Categories

| Category | Spanish Term | Rule | Legal Basis |
|----------|-------------|------|-------------|
| Passenger vehicles (turismos) | Vehiculos turismos, ciclomotores, motocicletas | 50% presumed business use -- deduct 50% of IVA. 100% deductible ONLY if taxpayer proves exclusive business use (e.g., delivery vehicles, taxis, commercial reps with no personal use) | LIVA Art. 95.Tres.2 |
| Vehicle running costs | Combustible, reparaciones, peajes | Same % as vehicle itself (50% presumed unless 100% proven) | LIVA Art. 95.Tres.2 |
| Mixed-use assets | Bienes de uso mixto | Deductible in proportion to business use. Burden of proof on taxpayer. | LIVA Art. 95.Tres |

### Fuel-Specific Rules [T1]

| Fuel Use | Deductibility | Legal Basis |
|----------|--------------|-------------|
| Fuel for 50%-presumed vehicle | 50% deductible | LIVA Art. 95.Tres.2 |
| Fuel for 100%-proven business vehicle | 100% deductible | LIVA Art. 95.Tres.2 |
| Fuel for blocked vehicle (personal) | 0% deductible | LIVA Art. 95.Uno |
| Fuel for non-vehicle use (machinery, generators) | 100% deductible if used in taxable activity | LIVA Art. 94 |

### Vehicles Eligible for 100% Deduction (Exceptions to 50% Rule) [T1]

| Vehicle Type | Justification | Legal Basis |
|-------------|---------------|-------------|
| Vehicles used in driving instruction | Autoescuelas | LIVA Art. 95.Tres.2.a |
| Vehicles used by commercial agents | Agentes comerciales (exclusively for travel) | LIVA Art. 95.Tres.2.b |
| Vehicles for passenger transport (taxi, VTC) | Transporte de viajeros | LIVA Art. 95.Tres.2.c |
| Vehicles used in car rental business | Alquiler de vehiculos | LIVA Art. 95.Tres.2.d |
| Delivery and goods transport vehicles | Furgonetas, camiones | LIVA Art. 95.Tres.2 (not turismos) |

---

## Step 6: Registration and Special Regimes [T1]

### Registration Obligation

**There is NO turnover threshold for VAT registration in Spain.** [T1]

Any person or entity carrying out economic activity (actividad economica / actividad empresarial o profesional) in the TAI must register for IVA and file returns, regardless of turnover. LIVA Art. 164.Uno.

| Registration Detail | Rule | Legal Basis |
|--------------------|------|-------------|
| Registration trigger | All economic activity in TAI | LIVA Art. 164.Uno |
| No threshold | No minimum turnover required | LIVA Art. 164 (no exemption threshold exists) |
| Registration form | Modelo 036 (censal) or Modelo 037 (simplified censal) | RIVA Art. 9-11 |
| NIF-IVA format | ES + letter + 8 digits (e.g., ESB12345678) or ES + 8 digits + letter (e.g., ES12345678A) | RIVA Art. 25 |
| VIES registration | Required for intra-EU operations via Modelo 036 | RIVA Art. 25 |
| De-registration | Modelo 036 within 1 month of cessation | RIVA Art. 11 |

### Regimen General (Standard Regime) [T1]

Default regime for all taxable persons. Full right of deduction subject to Art. 95-96 restrictions. Quarterly or monthly filing of Modelo 303. LIVA Art. 92-114.

### Regimen Simplificado (Simplified Regime) [T1/T2]

| Field | Detail | Legal Basis |
|-------|--------|-------------|
| Who | Personas fisicas (individuals) and entidades en regimen de atribucion de rentas (partnerships) | LIVA Art. 122 |
| Condition | Must also be in estimacion objetiva (modules) for IRPF | LIVA Art. 122.Dos |
| How it works | IVA due calculated by fixed indices/modules based on activity type, not actual invoices | LIVA Art. 123 |
| Input IVA | Deduction limited to cuotas soportadas supported by invoices for certain categories (capital assets, imports, intra-EU acquisitions) plus a fixed % for general expenses | LIVA Art. 123.Uno.C |
| Filing | Modelo 303 quarterly: first 3 quarters are fixed instalments; Q4 is final annual calculation | RIVA Art. 40 |
| Exclusion threshold | Annual turnover > EUR 250,000 (goods) or EUR 250,000 (services) | LIVA Art. 122.Dos.2 |
| Incompatibility | Cannot be combined with regimen general for the same activity | LIVA Art. 122.Dos |

**Flag as [T2]:** Module-based calculations require specific activity coefficients from AEAT published orders. Asesor Fiscal must determine the correct modules.

### Regimen de Recargo de Equivalencia (Equivalence Surcharge for Retailers) [T1]

**Legislation:** LIVA Art. 148-163.

| Field | Detail | Legal Basis |
|-------|--------|-------------|
| Who | Personas fisicas (individuals) who are comerciantes minoristas (retailers) selling goods acquired without transformation | LIVA Art. 148 |
| Definition of minorista | > 80% of sales in prior year were to end consumers (not empresarios) | LIVA Art. 149 |
| How it works | Supplier charges IVA + surcharge on the invoice. Retailer does NOT file Modelo 303. | LIVA Art. 154-156 |
| No input IVA recovery | Retailer cannot deduct any input IVA | LIVA Art. 154.Dos |
| No IVA books | Retailer is NOT required to keep libro registro de IVA | LIVA Art. 157 |

#### Surcharge Rates [T1]

| IVA Rate | Surcharge Rate (Recargo) | Combined Rate | Legal Basis |
|----------|------------------------|---------------|-------------|
| 21% | 5.2% | 26.2% | LIVA Art. 161.1 |
| 10% | 1.4% | 11.4% | LIVA Art. 161.2 |
| 4% | 0.5% | 4.5% | LIVA Art. 161.3 |
| 0% | 0% | 0% | LIVA Art. 161 |
| Tobacco | 1.75% | varies | LIVA Art. 161.5 |

#### Casillas for Recargo (Supplier/Wholesaler Reporting) [T1]

| IVA Rate | Recargo Rate | Casilla (Base) | Casilla (Rate) | Casilla (Tax) |
|----------|-------------|----------------|----------------|---------------|
| 4% | 0.5% | 14 | -- | 15 |
| 10% | 1.4% | 16 | -- | 17 |
| 21% | 5.2% | 18 | -- | 19 |
| Tobacco | 1.75% | 22 | -- | 23 |

**Critical:** [T2] If retailer also provides services or transforms goods, regimen general applies to those activities. Mixed activity requires Asesor Fiscal confirmation.

### NIF-IVA Format Reference [T1]

| Entity Type | Format | Example |
|------------|--------|---------|
| Sociedad (company) | ES + letter + 8 digits | ESB12345678 |
| Persona fisica (individual) | ES + 8 digits + letter | ES12345678A |
| Non-resident entity | ES + N + 7 digits + letter | ESN1234567A |
| Foreign entity with Spanish establishment | ES + W + 7 digits + letter | ESW1234567A |

---

## Step 7: Filing Deadlines [T1]

**Legislation:** RIVA Art. 71-72; LIVA Art. 167.

### Modelo 303 -- Quarterly Filers

| Period | Quarter | Filing Window | Legal Basis |
|--------|---------|--------------|-------------|
| 1T (Jan-Mar) | Q1 | 1-20 April | RIVA Art. 71.4 |
| 2T (Apr-Jun) | Q2 | 1-20 July | RIVA Art. 71.4 |
| 3T (Jul-Sep) | Q3 | 1-20 October | RIVA Art. 71.4 |
| 4T (Oct-Dec) | Q4 | 1-30 January (following year) | RIVA Art. 71.4 |

**Note:** Q4 has an extended deadline (30 January) to allow for annual regularisation.

### Modelo 303 -- Monthly Filers (SII / REDEME / Large Companies)

| Period | Filing Deadline | Legal Basis |
|--------|----------------|-------------|
| January - November | 1st to 30th of following month (e.g., January filed by 28 February; note: for months with fewer than 30 days, the last calendar day applies) | RIVA Art. 71.4 |
| December | 1-30 January (following year) | RIVA Art. 71.4 |

### Monthly Filing Triggers [T1]

| Trigger | Threshold | Legal Basis |
|---------|-----------|-------------|
| Large company (gran empresa) | Turnover > EUR 6,010,121.04 in prior year | RIVA Art. 71.3 |
| REDEME (Registro de Devolucion Mensual) | Voluntary registration; enables monthly refunds | RIVA Art. 30 |
| SII (Suministro Inmediato de Informacion) | Mandatory for all monthly filers | RD 596/2016 |
| Grupo de IVA (VAT group) | All group members | LIVA Art. 163 quinquies |

### Other Returns

| Return | Period | Deadline | Who Must File | Legal Basis |
|--------|--------|----------|---------------|-------------|
| Modelo 390 (annual summary) | Annual | 1-30 January | All filers EXCEPT SII-obliged entities | RIVA Art. 71.4 |
| Modelo 349 (EU recapitulative) | Quarterly or monthly | Same as Modelo 303 | Entities with intra-EU transactions | RIVA Art. 78-81 |
| Modelo 347 (annual third-party > EUR 3,005.06) | Annual | 1-28 February | All entities with qualifying transactions | RIVA Art. 31-35 |
| SII reporting (replaced Modelo 340) | Real-time (4 calendar days, excluding Saturdays, Sundays, and national holidays) | Within 4 calendar days of invoice issuance (sales) or accounting date (purchases) | SII-obliged entities | RD 596/2016; RIVA Art. 69 bis |

### Late Filing Penalties (Recargos por Declaracion Extemporanea) [T1]

**Legislation:** Ley General Tributaria (LGT) Art. 27.

| Delay | Recargo (Surcharge) | Interest | Legal Basis |
|-------|---------------------|----------|-------------|
| 1 complete month late | 1% | None | LGT Art. 27.2 (as amended by Ley 11/2021) |
| 2 complete months late | 2% | None | LGT Art. 27.2 |
| 3 complete months late | 3% | None | LGT Art. 27.2 |
| 4 complete months late | 4% | None | LGT Art. 27.2 |
| 5 complete months late | 5% | None | LGT Art. 27.2 |
| 6 complete months late | 6% | None | LGT Art. 27.2 |
| 7 complete months late | 7% | None | LGT Art. 27.2 |
| 8 complete months late | 8% | None | LGT Art. 27.2 |
| 9 complete months late | 9% | None | LGT Art. 27.2 |
| 10 complete months late | 10% | None | LGT Art. 27.2 |
| 11 complete months late | 11% | None | LGT Art. 27.2 |
| 12 complete months late | 12% | None | LGT Art. 27.2 |
| > 12 months late | 15% | + intereses de demora from month 13 | LGT Art. 27.2 |
| AEAT-initiated (requerimiento) | 50-150% sanction | + intereses de demora | LGT Art. 191-195 |

**Note:** Under Ley 11/2021 reform, the surcharge is 1% plus 1% for each additional complete month of delay (up to 12 months). Surcharges may be reduced by 25% if paid within the voluntary period (LGT Art. 27.5).

---

## Step 8: SII -- Suministro Inmediato de Informacion [T1]

**Legislation:** RD 596/2016; RIVA Art. 69 bis.

### Overview

| Field | Detail |
|-------|--------|
| What | Real-time electronic reporting of invoice details to AEAT |
| Who must use SII | All entities filing monthly Modelo 303: large companies (> EUR 6,010,121.04), REDEME registrants, VAT groups (grupo de IVA) |
| Voluntary | Any entity may opt in voluntarily via Modelo 036 |
| Reporting deadline | Within 4 calendar days of invoice date (issuance for sales; accounting date for purchases). Saturdays, Sundays, and national holidays are excluded from the count. |
| Books reported | Libro registro de facturas expedidas, libro registro de facturas recibidas, libro registro de bienes de inversion, libro registro de operaciones intracomunitarias |

### SII Reporting Requirements [T1]

| Book | Spanish Name | Content | Deadline |
|------|-------------|---------|----------|
| Sales invoices | Libro registro de facturas expedidas | Invoice number, date, counterparty NIF, base, rate, tax, type of operation | 4 calendar days from invoice date (excl. Sat/Sun/national holidays) |
| Purchase invoices | Libro registro de facturas recibidas | Invoice number, date, supplier NIF, base, rate, deductible tax | 4 calendar days from accounting date (excl. Sat/Sun/national holidays) |
| Capital goods | Libro registro de bienes de inversion | Asset details, acquisition date, amounts, prorrata adjustments | Annual |
| Intra-EU operations | Libro registro de operaciones intracomunitarias | Details of all intra-EU acquisitions and supplies | 4 calendar days (excl. Sat/Sun/national holidays) |

### SII Benefits and Implications [T1]

| Benefit | Detail |
|---------|--------|
| No Modelo 390 required | SII entities are exempt from filing the annual summary | RD 596/2016 |
| No Modelo 347 required | SII entities are exempt from the annual third-party declaration | RD 596/2016 |
| Extended Modelo 303 deadline | Monthly filers on SII have until last day of following month (not 20th) | RIVA Art. 71.4 |
| Monthly refund eligibility | SII entities can obtain monthly refunds | RIVA Art. 30 |
| Reduced inspection risk | Real-time data reduces likelihood of discrepancies | Administrative practice |
| Verifactu (future) | From 2027, businesses NOT in SII will be required to use Verifactu-compliant invoicing software (RD-Ley 15/2025 delayed: corporates from 1 Jan 2027; others from 1 Jul 2027). SII-obliged entities are exempt from Verifactu. | Ley 11/2021 Art. 29.2.j; RD 1007/2023; RD-Ley 15/2025 |

---

## Step 9: Prorrata de Deduccion (Proportional Deduction) [T2]

**Legislation:** LIVA Art. 102-106; RIVA Art. 28.

### When Prorrata Applies

When a taxpayer makes BOTH taxable supplies (with right of deduction) AND exempt supplies (without right of deduction), input IVA can only be partially deducted.

### Prorrata General (General Pro-Rata) [T2]

**Formula:**

```
% deduccion = [(Taxable turnover + Exempt-with-deduction-right turnover) / Total turnover] x 100
```

| Rule | Detail | Legal Basis |
|------|--------|-------------|
| Rounding | Always round UP to next whole integer | LIVA Art. 104.Dos |
| Threshold | If prorrata >= 99%, treat as 100% (full deduction) | LIVA Art. 104.Dos.2 |
| Provisional | Apply provisional prorrata (from prior year) during Q1-Q3 | LIVA Art. 105.Uno |
| Definitive | Calculate definitive prorrata in Q4 and regularise | LIVA Art. 105.Dos |
| Regularisation | Adjustment in Casilla 42 of Q4 Modelo 303 | LIVA Art. 105 |

### Prorrata Especial (Special Pro-Rata / Sector Differentiation) [T2]

**Legislation:** LIVA Art. 106.

When a taxpayer has clearly differentiated sectors of activity (sectores diferenciados), each sector applies its own prorrata:

| Rule | Detail | Legal Basis |
|------|--------|-------------|
| When required | Mandatory if prorrata general would distort deduction by > 10% in any sector | LIVA Art. 103.Dos |
| Optional | Taxpayer may voluntarily elect prorrata especial | LIVA Art. 103.Dos |
| How it works | Each sector calculates its own deduction % | LIVA Art. 106 |
| Common costs | Allocated using prorrata general to common costs not attributable to any single sector | LIVA Art. 106.Dos |

**Flag for reviewer [T2]:** Prorrata calculation must be confirmed by Asesor Fiscal. Both provisional and definitive rates require professional judgement.

---

## Step 10: Key Thresholds [T1]

| Threshold | Value | Legal Basis |
|-----------|-------|-------------|
| Capital goods -- movable (bienes de inversion) | > EUR 3,005.06 acquisition cost | LIVA Art. 108.Uno |
| Capital goods -- immovable | Always capital regardless of value | LIVA Art. 108.Dos |
| Capital goods regularisation period -- movable | 5 years | LIVA Art. 107.Uno |
| Capital goods regularisation period -- immovable | 10 years | LIVA Art. 107.Uno |
| Monthly filing trigger (gran empresa) | Turnover > EUR 6,010,121.04 in prior year | RIVA Art. 71.3 |
| SII mandatory | All monthly filers | RD 596/2016 |
| Vehicle business use presumption | 50% (rebuttable) | LIVA Art. 95.Tres.2 |
| Prorrata rounding | >= 99% = treat as 100% | LIVA Art. 104.Dos.2 |
| Recargo de equivalencia eligibility | Personas fisicas, > 80% sales to end consumers, goods sold without transformation | LIVA Art. 148-149 |
| Anti-fraud reverse charge (electronics) | Invoice > EUR 5,000 | LIVA Art. 84.Uno.2.g |
| Modelo 347 reporting threshold | > EUR 3,005.06 annual transactions with single counterparty | RIVA Art. 33 |
| Regimen simplificado exclusion | Annual turnover > EUR 250,000 | LIVA Art. 122.Dos.2 |

---

## PROHIBITIONS [T1]

1. NEVER let AI guess casilla numbers -- they are 100% deterministic from facts. LIVA Art. 164.
2. NEVER apply Canary Islands, Ceuta, or Melilla rules in this skill -- IGIC and IPSI are entirely separate tax regimes. LIVA Art. 3.Dos. Escalate as [T3].
3. NEVER allow recargo de equivalencia clients to file Modelo 303 or claim input IVA. LIVA Art. 154.Dos.
4. NEVER apply reverse charge to out-of-scope categories (wages, loans, dividends, bank charges). Not a supply under LIVA Art. 4.
5. NEVER apply reverse charge to local consumption services abroad (hotel, restaurant, taxi in another EU country). LIVA Art. 70.
6. NEVER classify vehicles at 100% business use without documented evidence proving exclusive business use -- default is always 50%. LIVA Art. 95.Tres.2.
7. NEVER allow entertainment or gift deductions -- blocked under LIVA Art. 96.Uno.5 with no exceptions.
8. NEVER confuse zero-rated (exempt with right of deduction -- exports, intra-EU supplies) with exempt without right of deduction (Art. 20 LIVA). The former allows input IVA recovery; the latter does not.
9. NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude.
10. NEVER file Modelo 390 for SII-obliged entities -- they are exempt from this obligation. RD 596/2016.
11. NEVER apply regimen simplificado to Sociedades (companies) -- only available to personas fisicas and entidades en regimen de atribucion de rentas. LIVA Art. 122.
12. NEVER allow a recargo de equivalencia retailer to deduct input IVA on intra-EU acquisitions -- the supplier must charge the surcharge or the retailer must self-assess it. LIVA Art. 157.
13. NEVER accept an invoice without the notation "Inversion del sujeto pasivo" as a valid reverse charge invoice -- RIVA Art. 6.1.k requires this notation.

---

## Step 11: Edge Case Registry

### EC1 -- EU hotel / restaurant / taxi booked abroad [T1]

**Situation:** Client pays hotel in France. Invoice shows French TVA.
**Resolution:** NOT reverse charge. Foreign VAT paid at source. No Modelo 303 entry. Irrecoverable foreign VAT embedded in expense. The service is consumed locally abroad.
**Legislation:** LIVA Art. 70.Uno.1 (place of supply for immovable property-related services); Art. 70.Uno.5 (restaurant and catering services localised where performed).

### EC2 -- SaaS subscription from US provider [T1]

**Situation:** US company charges EUR 100/month for cloud software, no IVA on invoice.
**Resolution:** Reverse charge applies. Output: Casilla 12 = EUR 100 (base), Casilla 13 = EUR 21 (21%). Input: Casilla 28 = EUR 100, Casilla 29 = EUR 21 (if fully taxable business; non-EU services go to domestic input casillas, not import casillas). Net = zero.
**Legislation:** LIVA Art. 84.Uno.2.a; Art. 69.Uno (place of supply for B2B services).

### EC3 -- Construction subcontracting (inversion del sujeto pasivo) [T1]

**Situation:** Subcontractor provides construction works (ejecucion de obra) to a main contractor (contratista principal). Both are registered in Spain.
**Resolution:** Reverse charge under Art. 84.Uno.2.f LIVA. Subcontractor invoices WITHOUT IVA, noting "Inversion del sujeto pasivo." Main contractor self-assesses: Output Casilla 12/13, Input Casilla 28/29 (or 30/31 if capital). Applies to: construction, renovation, demolition, urbanisation works where recipient is a developer or contractor who will in turn supply the works to a third party.
**Legislation:** LIVA Art. 84.Uno.2.f; RIVA Art. 6.1.k.

### EC4 -- Company car (vehiculo turismo) [T2]

**Situation:** Client purchases car for EUR 25,000 + EUR 5,250 IVA (21%).
**Resolution:** Presumed 50% business use. Input IVA deductible = EUR 2,625 (50%). Casilla 28 = EUR 12,500, Casilla 29 = EUR 2,625. If client can prove exclusive business use (e.g., vehicle is a commercial van, taxi, driving school car), 100% deductible. Flag for reviewer: request evidence of exclusive business use before allowing 100%.
**Legislation:** LIVA Art. 95.Tres.2.

### EC5 -- Client gifts and entertainment [T1]

**Situation:** Client gives Christmas gift baskets (cestas de Navidad) worth EUR 500 + EUR 105 IVA to clients.
**Resolution:** IVA NOT deductible. Entertainment and gifts to clients are BLOCKED under Art. 96.Uno.5 LIVA. No exceptions. Casilla 29 = EUR 0 for this item. The expense is recognised for income tax purposes (with limitations under Impuesto sobre Sociedades) but IVA is irrecoverable.
**Legislation:** LIVA Art. 96.Uno.5.

### EC6 -- Intra-Community supply of goods (entrega intracomunitaria) [T1]

**Situation:** Client sells goods to German business (B2B), ships goods from Spain to Germany.
**Resolution:** Exempt with right of deduction. No output IVA on Modelo 303. Report in Modelo 349 (recapitulative statement). Conditions: (i) buyer must be registered for VAT in another EU state; (ii) goods must physically leave Spain; (iii) client must have buyer's NIF-IVA and verify via VIES.
**Legislation:** LIVA Art. 25; RIVA Art. 13.

### EC7 -- Credit notes (facturas rectificativas) [T1]

**Situation:** Client receives credit note from supplier correcting a prior invoice.
**Resolution:** Reduce the original casilla entries by the credit note amount. Use Casillas 24/25 for modifications to output IVA bases/tax. For input IVA, reduce the relevant input casilla (28/29, 32/33, etc.). Report net figures. A factura rectificativa must reference the original invoice and comply with RIVA Art. 15.
**Legislation:** LIVA Art. 80 (modification of bases); RIVA Art. 15 (rectification invoices).

### EC8 -- Canary Islands transaction [T3]

**Situation:** Client sells goods to customer in Canary Islands.
**Resolution:** ESCALATE. IGIC (Impuesto General Indirecto Canario) applies, not IVA. The supply is treated similarly to an export from the TAI. For IVA purposes, the supply is exempt with right of deduction under LIVA Art. 21.2. However, the Canary Islands customer may owe IGIC on importation. Do NOT attempt to calculate IGIC -- different regime entirely.
**Legislation:** LIVA Art. 3.Dos; Art. 21.2.

### EC9 -- RECC (Regimen Especial del Criterio de Caja) [T2]

**Situation:** Client is registered under the cash-basis IVA regime.
**Resolution:** Under RECC, output IVA (IVA devengado) is not due until payment is received from the customer, rather than at invoice date. Input IVA (IVA soportado) is not deductible until payment is made to the supplier. Both the RECC taxpayer and their trading partners are affected (the customer of a RECC supplier cannot deduct input IVA until they pay). RECC invoices must be annotated "Regimen especial del criterio de caja." Cash basis applies up to 31 December of the year following the invoice date (longstop date). Flag for reviewer: timing of all deductions changes.
**Legislation:** LIVA Art. 163 decies-163 sexdecies; RIVA Art. 61 decies-61 sexdecies.

### EC10 -- SII real-time reporting obligation [T1]

**Situation:** Client is a large company (turnover > EUR 6,010,121.04) and is obliged to use SII.
**Resolution:** Client must report all invoices electronically to AEAT within 4 calendar days (excluding Saturdays, Sundays, and national holidays) of issuance (sales) or accounting date (purchases). Files monthly Modelo 303 (not quarterly). Exempt from Modelo 390 and Modelo 347. SII data must include: invoice type (F1, F2, etc.), operation key (01-15), counterparty NIF, base, rate, and tax amount.
**Legislation:** RD 596/2016; RIVA Art. 69 bis.

### EC11 -- Operaciones triangulares (triangular operations / EU simplification) [T2]

**Situation:** Spanish company (A) buys goods from French company (B), but the goods are shipped directly from France to a German customer (C). A never takes physical possession in Spain.
**Resolution:** This is an operacion triangular (ABC transaction) under the EU simplification. Company A is the intermediary. The intra-EU acquisition by A is deemed to take place in Germany (where goods arrive). Company A invoices C without IVA, noting "Operacion triangular -- Art. 141 Directiva 2006/112/CE." C self-assesses IVA in Germany. A reports the triangulation in Modelo 349 using the specific operation key "T." Flag for Asesor Fiscal to confirm the chain qualifies.
**Legislation:** LIVA Art. 26 (triangular simplification); Directive 2006/112/EC Art. 141.

### EC12 -- Regimen especial de bienes usados (second-hand goods margin scheme) [T2]

**Situation:** Client is a dealer in second-hand goods (coches de segunda mano, antiguedades, objetos de arte).
**Resolution:** Under the margin scheme, IVA is charged only on the profit margin (difference between selling price and purchase price), not on the full selling price. The dealer cannot deduct input IVA on goods purchased for resale under this regime. Invoices must NOT show IVA separately. The margin scheme cannot be applied if the goods were acquired with a right of deduction. Flag for Asesor Fiscal: verify each transaction qualifies.
**Legislation:** LIVA Art. 135-139; RIVA Art. 50-51.

### EC13 -- Prorrata de deduccion -- mixed taxable and exempt [T2]

**Situation:** Client is a medical practice (exempt under Art. 20.Uno.3 LIVA) that also provides taxable cosmetic surgery services.
**Resolution:** The practice makes both exempt supplies (no deduction right) and taxable supplies (deduction right). Prorrata de deduccion applies. Calculate provisional prorrata at start of year based on prior year's ratio. Apply to all input IVA. Regularise in Q4 with definitive prorrata. If prorrata >= 99%, treat as 100%. If sectors are clearly differentiated, prorrata especial may be mandatory (Art. 103.Dos LIVA).
**Legislation:** LIVA Art. 102-106.

### EC14 -- Bad debt relief (modificacion de base por creditos incobrables) [T1]

**Situation:** Client issued invoice over 6 months ago and customer has not paid.
**Resolution:** After 6 months from accrual (1 year for large companies), if the debt has been claimed judicially or through notarial requirement, the base can be modified downward. Output IVA previously reported is recovered. Report in Casillas 24/25. Must issue factura rectificativa and notify AEAT. Customer must adjust their input IVA deduction.
**Legislation:** LIVA Art. 80.Cuatro; RIVA Art. 24.

### EC15 -- Fuel card / fleet card purchases [T1]

**Situation:** Client uses a fuel card (e.g., Repsol, Cepsa) for business vehicles.
**Resolution:** Fuel for vehicles with 50% presumed business use: 50% of IVA deductible. Fuel for 100%-proven business vehicles (vans, trucks, taxis): 100% deductible. The fuel card statement must include valid factura data (NIF, base, IVA) per RIVA Art. 6. Simplified invoices (tickets) are NOT sufficient for deduction. Ensure the fuel card provider issues proper facturas.
**Legislation:** LIVA Art. 95.Tres.2; RIVA Art. 6.

### EC16 -- Intra-EU acquisition of goods by recargo de equivalencia retailer [T1]

**Situation:** Retailer in recargo de equivalencia regime acquires goods from an EU supplier.
**Resolution:** The retailer must self-assess both the IVA AND the recargo de equivalencia on the intra-EU acquisition, since the EU supplier cannot charge Spanish recargo. The retailer must file a special Modelo 309 for these acquisitions. This is an exception to the general rule that recargo retailers do not file returns.
**Legislation:** LIVA Art. 157; RIVA Art. 17.

---

## Step 12: Comparison with Malta

| Feature | Spain (IVA) | Malta (VAT) |
|---------|------------|-------------|
| **Primary legislation** | Ley 37/1992 (LIVA) | VAT Act Cap. 406 |
| **Standard rate** | 21% (LIVA Art. 90) | 18% (Cap. 406, 1st Schedule) |
| **Reduced rates** | 10% and 4% (LIVA Art. 91) | 7%, 5%, 12% (Cap. 406, 5th Schedule) |
| **Registration threshold** | None -- all economic activity triggers registration (LIVA Art. 164) | EUR 35,000 for Article 11 small enterprise exemption; Article 10 voluntary/mandatory |
| **Return form** | Modelo 303 (quarterly/monthly) + Modelo 390 (annual) | VAT3 (quarterly) or Article 11 declaration (annual) |
| **Filing portal** | Sede Electronica AEAT | CFR Online (cfr.gov.mt) |
| **Quarterly deadline** | 20th of month after quarter (Q4 = 30 January) | 21st of month after quarter (e-filing); 14th (paper) |
| **Capital goods threshold** | > EUR 3,005.06 movable; all immovable (LIVA Art. 108) | >= EUR 1,160 gross (Cap. 406, Art. 24) |
| **Motor vehicle deduction** | 50% presumed (LIVA Art. 95.Tres.2) | Fully blocked (10th Schedule Item 3(1)(a)(iv-v)) |
| **Entertainment deduction** | Fully blocked (LIVA Art. 96.Uno.5) | Fully blocked (10th Schedule Item 3(1)(b)) |
| **Reverse charge** | Art. 84.Uno.2 LIVA -- extensive list including construction, scrap, electronics > EUR 5,000 | Art. 19-20 Cap. 406 -- EU/non-EU acquisitions |
| **Real-time reporting** | SII mandatory for monthly filers (RD 596/2016) | No equivalent |
| **Surcharge regime** | Recargo de equivalencia for retailers (LIVA Art. 148-163) | No equivalent |
| **Simplified regime** | Regimen simplificado for small traders (LIVA Art. 122-123) | Article 11 small enterprise exemption |
| **Territorial exclusions** | Canary Islands (IGIC), Ceuta/Melilla (IPSI) (LIVA Art. 3.Dos) | None |
| **Prorrata** | Prorrata general and especial (LIVA Art. 102-106) | Partial exemption (Art. 22(4)) |
| **Cash basis option** | RECC (LIVA Art. 163 decies) | Not available |
| **Annual summary** | Modelo 390 (except SII entities) | No separate annual summary |
| **EU recapitulative** | Modelo 349 | Included in VAT3 |
| **Late filing penalty** | Graduated surcharges 1%-15% + interest (LGT Art. 27) | Administrative penalties per CFR |
| **NIF-IVA format** | ES + letter + 8 digits or ES + 8 digits + letter | MT + 8 digits |

### Key Differences for Practitioners

1. **No registration threshold in Spain** vs Malta's EUR 35,000 Article 11 exemption. In Spain, even the smallest autonomo must register and file. LIVA Art. 164.
2. **Spain allows 50% vehicle deduction** (LIVA Art. 95.Tres.2) vs Malta's full block (10th Schedule). This is a significant planning difference.
3. **Spain has SII real-time reporting** (RD 596/2016) with no Malta equivalent. Spanish large companies must report invoices within 4 days.
4. **Recargo de equivalencia** (LIVA Art. 148-163) has no Malta counterpart. Retailers in Spain may be in a fundamentally different regime.
5. **Territorial complexity** -- Spain has three distinct indirect tax zones (IVA/IGIC/IPSI) within its sovereign territory. Malta has a single unified system.
6. **Modelo 390 annual summary** is required in Spain (unless SII). Malta has no separate annual reconciliation form.

---

## Step 13: Test Suite

### Test 1 -- Standard domestic purchase, 21% IVA [T1]

**Input:** Spanish supplier, office supplies, gross EUR 242, IVA EUR 42 (21%), net EUR 200. Regimen general client.
**Expected output:** Casilla 28 = EUR 200 (base), Casilla 29 = EUR 42 (input IVA deductible).
**Legislation:** LIVA Art. 92; Art. 94.

### Test 2 -- US software subscription, reverse charge [T1]

**Input:** US provider (no EU establishment), EUR 100/month, no IVA on invoice. Regimen general client.
**Expected output:** Output: Casilla 12 = EUR 100, Casilla 13 = EUR 21 (21%). Input: Casilla 28 = EUR 100, Casilla 29 = EUR 21 (non-EU services under reverse charge go to domestic input casillas). Net IVA effect = zero.
**Legislation:** LIVA Art. 84.Uno.2.a; Art. 69.Uno.

### Test 3 -- Intra-Community goods acquisition [T1]

**Input:** German supplier ships goods to Spain, EUR 5,000, no IVA on invoice. Regimen general client.
**Expected output:** Output: Casilla 10 = EUR 5,000, Casilla 11 = EUR 1,050 (21%). Input: Casilla 36 = EUR 5,000, Casilla 37 = EUR 1,050 (intra-EU acquisitions). Net = zero.
**Legislation:** LIVA Art. 13; Art. 26.

### Test 4 -- EU B2B sale of goods [T1]

**Input:** Client sells goods to French business EUR 3,000, ships Spain to France. French buyer has valid NIF-IVA verified on VIES.
**Expected output:** No output IVA on Modelo 303. Exempt with right of deduction. Report EUR 3,000 on Modelo 349.
**Legislation:** LIVA Art. 25.

### Test 5 -- Company car, 50% presumed [T2]

**Input:** Client purchases passenger car EUR 25,000 + EUR 5,250 IVA (21%). No proof of exclusive business use.
**Expected output:** Casilla 28 = EUR 12,500, Casilla 29 = EUR 2,625 (50% deductible). Flag for reviewer.
**Legislation:** LIVA Art. 95.Tres.2.

### Test 6 -- Entertainment dinner, blocked [T1]

**Input:** Client entertainment dinner with clients EUR 330 including IVA EUR 30 (10% restaurant rate). Net EUR 300.
**Expected output:** Casilla 29 = EUR 0 for this item. IVA BLOCKED under Art. 96.Uno.5 LIVA. No deduction regardless of business purpose.
**Legislation:** LIVA Art. 96.Uno.5.

### Test 7 -- EU hotel, local consumption [T1]

**Input:** Client pays hotel in Italy EUR 400 including Italian IVA.
**Expected output:** No Modelo 303 entry. Foreign IVA irrecoverable. Service consumed locally abroad.
**Legislation:** LIVA Art. 70.Uno.1.

### Test 8 -- Recargo de equivalencia purchase by retailer [T1]

**Input:** Retailer (persona fisica in recargo regime) buys goods from Spanish wholesaler: EUR 1,000 net + EUR 210 IVA (21%) + EUR 52 recargo (5.2%). Wholesaler invoices all three amounts.
**Expected output:** NO Modelo 303 entry by the retailer. The retailer does not file. The wholesaler reports the recargo in Casillas 18 (base EUR 1,000) and 19 (tax EUR 52) on their own Modelo 303.
**Legislation:** LIVA Art. 154-156; Art. 161.

### Test 9 -- Construction subcontracting reverse charge [T1]

**Input:** Subcontractor invoices main contractor EUR 50,000 for construction works. Invoice states "Inversion del sujeto pasivo -- Art. 84.Uno.2.f LIVA." No IVA charged.
**Expected output (for main contractor):** Output: Casilla 12 = EUR 50,000, Casilla 13 = EUR 10,500 (21%). Input: Casilla 28 = EUR 50,000, Casilla 29 = EUR 10,500. Net = zero (if fully taxable).
**Legislation:** LIVA Art. 84.Uno.2.f.

### Test 10 -- Capital goods purchase (domestic) [T1]

**Input:** Client purchases industrial machinery for EUR 15,000 + EUR 3,150 IVA (21%). Cost > EUR 3,005.06 and useful life > 1 year.
**Expected output:** Casilla 30 = EUR 15,000 (capital assets base), Casilla 31 = EUR 3,150 (capital assets IVA). Subject to 5-year regularisation period.
**Legislation:** LIVA Art. 108.Uno; Art. 107.

### Test 11 -- Sale at reduced rate (restaurant) [T1]

**Input:** Client operates a restaurant. Total sales for quarter: EUR 50,000 net.
**Expected output:** Casilla 04 = EUR 50,000, Casilla 05 = 10, Casilla 06 = EUR 5,000.
**Legislation:** LIVA Art. 91.Uno.2.3.

### Test 12 -- Scrap metal purchase (chatarra) -- reverse charge [T1]

**Input:** Client (recycling company) purchases scrap metal from Spanish supplier for EUR 8,000. Supplier invoices without IVA, noting reverse charge.
**Expected output:** Output: Casilla 12 = EUR 8,000, Casilla 13 = EUR 1,680 (21%). Input: Casilla 28 = EUR 8,000, Casilla 29 = EUR 1,680. Net = zero.
**Legislation:** LIVA Art. 84.Uno.2.b.

### Test 13 -- Fuel for company car (50% rule) [T1]

**Input:** Client purchases fuel EUR 100 + EUR 21 IVA (21%) for passenger car with 50% presumed business use.
**Expected output:** Casilla 28 = EUR 50, Casilla 29 = EUR 10.50 (50% deductible). Same proportion as the vehicle.
**Legislation:** LIVA Art. 95.Tres.2.

---

## Step 14: Out of Scope -- Direct Tax [T3]

This skill does not compute income tax. The following is reference only. Escalate to Asesor Fiscal.

- **IRPF (Impuesto sobre la Renta de las Personas Fisicas):** Progressive rates 19%-47%. For autonomos filing quarterly: Modelo 130 (estimacion directa) or Modelo 131 (estimacion objetiva/modulos).
- **Impuesto sobre Sociedades (Corporate Tax):** 25% standard; 23% for entities with net turnover < EUR 1,000,000 in prior year. Filed annually via Modelo 200.
- **Seguridad Social autonomos:** Separate obligation based on real income (since 2023 reform). Not related to IVA.
- **IAE (Impuesto sobre Actividades Economicas):** Exempt if turnover < EUR 1,000,000. Municipal tax.
- **IBI, ITP/AJD:** Property-related taxes. Separate regimes.

---

## Step 15: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Asesor Fiscal must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to Asesor Fiscal. Document gap.
```

---

## Contribution Notes

Adapted from the Malta VAT Return Skill template. All legislation, casilla numbers, thresholds, and blocked categories are specific to Spain (Peninsula + Balearic Islands). Canary Islands (IGIC), Ceuta, and Melilla (IPSI) are excluded from this skill entirely.

**A skill may not be published without sign-off from an Asesor Fiscal in Spain.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
