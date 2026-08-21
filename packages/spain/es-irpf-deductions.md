---
name: es-irpf-deductions
description: Use this skill whenever asked about Spanish regional tax deductions (deducciones autonomicas), IRPF deductions by Comunidad Autonoma, or territory-specific tax benefits. Trigger on phrases like "deducciones autonomicas", "deduccion por vivienda", "deduccion por familia numerosa", "deduccion por nacimiento", "deduccion Madrid", "deduccion Cataluna", "deduccion Valencia", "deducciones por discapacidad", "deducciones por alquiler", "deducciones IRPF por comunidad", "casilla AEAT", "territory deductions Spain", "regional tax credits Spain", "Ceuta Melilla deduction", "foral deductions", "Pais Vasco IRPF", "Navarra IRPF", "deduccion por donativo", "deduccion por guarderia", "deduccion por maternidad autonomica", or any question about which IRPF deductions apply in a specific Spanish territory. ALWAYS read this skill before advising on territory-specific deductions.
version: 1.0
jurisdiction: ES
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - es-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ES Irpf Deductions

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Spain (Estado Español) |
| Tax | IRPF -- Deducciones Autonómicas (Cuota Autonómica) |
| Currency | EUR only |
| Tax year | Calendar year (año natural) |
| Legislation | LIRPF Art. 77; Each Comunidad Autónoma's own tax law |
| Authority | AEAT + Regional tax agencies (ATC, ATV, etc.) |
| Total known deductions | ~339 in common territory + additional in foral territories |
| Territories covered | 15 common territory CCAA + 4 foral (Álava, Bizkaia, Gipuzkoa, Navarra) + Ceuta + Melilla |
| Skill version | 1.0 |

## Section 2 -- How Regional Deductions Work

### The Dual Structure of Spanish IRPF

- **Dual structure of IRPF** — Spanish IRPF is split 50/50 between the State (cuota estatal) and the Autonomous Community (cuota autonómica). The state portion is fixed nationwide; the regional portion is where each CCAA can: 1. Modify the regional tax brackets (escala autonómica) 2. Create regional deductions (deducciones autonómicas) that reduce the cuota autonómica. Regional deductions apply AFTER computing the cuota íntegra autonómica. They reduce the tax owed to the regional government. They do NOT reduce the state portion.

### Key Principles

- **Key principles** — Deductions are claimed on Modelo 100 (annual IRPF return), in the autonomous community section. Each deduction has a specific AEAT casilla (box number). Most deductions have income limits (base imponible general + base imponible del ahorro). Joint filing (tributación conjunta) may double some limits. Deductions cannot generate a negative cuota autonómica (floor = 0).

## Section 3 -- Deductions by Territory: Common Territory (Territorio Común)

### 3.1 Andalucía (15 deductions)

**Andalucía deductions**

| Category | Deduction | Key Requirements |
| --- | --- | --- |
| Familia | Por nacimiento o adopción de hijos | Recent birth/adoption |
| Familia | Por adopción internacional | International adoption |
| Familia | Familia monoparental | Single parent with dependents |
| Discapacidad | Contribuyente con discapacidad | Taxpayer disability ≥33% |
| Discapacidad | Cónyuge con discapacidad | Spouse disability ≥33% |
| Vivienda | Inversión vivienda protegida / jóvenes | Protected housing or under 35 |
| Vivienda | Alquiler vivienda habitual | Habitual residence rental |
| Inversión | Adquisición acciones sociedades | Investment in new companies |
| Donaciones | Donativos con finalidad ecológica | Ecological donations |
| General | Deducción aplicable con carácter general | Income below threshold |
| Salud | Gastos defensa jurídica laboral | Employment legal costs |

### 3.2 Aragón (21 deductions)

**Aragón deductions**

| Category | Deduction | Key Requirements |
| --- | --- | --- |
| Familia | Nacimiento o adopción tercer hijo+ | 3rd or subsequent child |
| Educación | Libros de texto y material escolar | School-age children |
| Vivienda | Adquisición vivienda habitual víctimas terrorismo | Terrorism victims |
| Inversión | Acciones entidades segmento empresas en expansión | Listed growth companies |
| Inversión | Adquisición acciones/participaciones nuevas sociedades | New company investment |
| Donaciones | Donaciones ecológicas e I+D | R&D and ecological |
| Discapacidad | Gastos formación autonomía discapacitados | Disability training expenses |

### 3.3 Asturias (Principado de Asturias) (27 deductions)

**Asturias deductions**

| Category | Deduction | Key Requirements |
| --- | --- | --- |
| Familia | Adopción internacional | International adoption |
| Familia | Partos múltiples / adopción simultánea | Multiple births |
| Familia | Familias numerosas | Large families |
| Familia | Familias monoparentales | Single-parent families |
| Educación | Libros de texto y material escolar | School-age children |
| Educación | Gastos formación contribuyentes | Training expenses |
| Vivienda | Inversión vivienda habitual protegida | Protected housing |
| Vivienda | Arrendamiento vivienda habitual | Rent ≤ income limits |
| Territorial | Trabajadores cuenta propia zonas rurales | Self-employed in rural areas |
| Territorial | Gastos transporte público concejos despoblación | Public transport in depopulating areas |
| Trabajo | Traslado domicilio fiscal a Asturias | Relocating to Asturias |

### 3.4 Islas Baleares (Illes Balears) (25 deductions)

**Islas Baleares deductions**

| Category | Deduction | Key Requirements |
| --- | --- | --- |
| Familia | Gastos adquisición libros texto | School books |
| Familia | Gastos aprendizaje extraescolar idiomas | Language classes |
| Vivienda | Arrendamiento vivienda habitual jóvenes/discapacitados | Under 36 or disabled, rental |
| Donaciones | Donaciones investigación, desarrollo, innovación | R&D&I donations |
| Donaciones | Donaciones patrimonio histórico | Heritage preservation |
| Salud | Gastos ascendientes mayores 65 años | Elderly care expenses |

### 3.5 Canarias (27 deductions)

**Canarias deductions**

| Category | Deduction | Key Requirements |
| --- | --- | --- |
| Donaciones | Donaciones finalidad ecológica | Ecological donations |
| Donaciones | Donaciones rehabilitación patrimonio | Heritage rehabilitation |
| Educación | Gastos estudios educación superior | University/higher education |
| Territorial | Traslado residencia a otra isla | Inter-island relocation |
| Vivienda | Inversión vivienda habitual | Habitual residence acquisition |
| Familia | Nacimiento o adopción | Birth/adoption |
| Familia | Gastos guardería | Nursery expenses |

### 3.5 Canarias (27 deductions)

Note: Canarias also has specific indirect tax benefits (IGIC instead of IVA) and the RIC (Reserva para Inversiones en Canarias) which affects corporate tax. These are NOT IRPF deductions.

### 3.6 Cantabria (18 deductions)

**Cantabria deductions**

| Category | Deduction | Key Requirements |
| --- | --- | --- |
| Familia | Cuidado familiares dependientes | Dependent family care |
| Familia | Gastos guardería menores 3 años | Nursery for children under 3 |
| Vivienda | Arrendamiento vivienda habitual jóvenes | Rental for young people |
| Vivienda | Obras mejora vivienda | Home improvement works |
| Donaciones | Donativos fundaciones Cantabria | Donations to Cantabrian foundations |

### 3.7 Castilla y León (22 deductions)

**Castilla y León deductions**

| Category | Deduction | Key Requirements |
| --- | --- | --- |
| Familia | Nacimiento o adopción | Birth/adoption |
| Familia | Cuidado hijos menores | Childcare expenses |
| Familia | Familias numerosas | Large families |
| Actividad Económica | Fomento emprendimiento | Entrepreneurship promotion |
| Vivienda | Adquisición vivienda jóvenes zonas rurales | Young people buying in rural areas |
| Vivienda | Alquiler vivienda habitual jóvenes | Rental for young people |

### 3.8 Castilla-La Mancha (25 deductions)

**Castilla-La Mancha deductions**

| Category | Deduction | Key Requirements |
| --- | --- | --- |
| Familia | Nacimiento o adopción | Birth/adoption |
| Familia | Familia numerosa | Large family |
| Discapacidad | Contribuyentes con discapacidad | Disability ≥33% |
| Vivienda | Adquisición vivienda habitual jóvenes | Young people (<36) buying home |
| Vivienda | Arrendamiento vivienda habitual jóvenes | Young people renting |
| Donaciones | Donaciones finalidad medioambiental | Environmental donations |
| Educación | Gastos educativos | Educational expenses |

### 3.9 Cataluña (Catalunya) (10 deductions)

**Cataluña deductions**

| Category | Deduction | Key Requirements |
| --- | --- | --- |
| Familia | Nacimiento o adopción hijo | Birth/adoption |
| Donaciones | Donativos lengua catalana/occitana | Catalan/Occitan language promotion |
| Donaciones | Donativos investigación científica | Scientific research donations |
| Vivienda | Alquiler vivienda habitual | Habitual residence rental |
| Educación | Intereses préstamos máster/doctorado | Loan interest for postgraduate studies |

### 3.9 Cataluña (Catalunya) (10 deductions)

Note: Cataluña has fewer deductions but applies modified regional brackets that can result in a higher overall rate for high earners.

### 3.10 Comunidad Valenciana (44 deductions -- most of any CCAA)

**Comunidad Valenciana deductions**

| Category | Deduction | Key Requirements |
| --- | --- | --- |
| Familia | Nacimiento, adopción, acogimiento | Birth/adoption/foster care |
| Familia | Nacimiento o adopción múltiples | Multiple births |
| Familia | Hijos con discapacidad | Children with disabilities |
| Familia | Familia numerosa o monoparental | Large or single-parent family |
| Familia | Custodia guarderías | Nursery custody expenses |
| Familia | Conciliación trabajo-familia | Work-family balance |
| Vivienda | Arrendamiento vivienda habitual | Habitual residence rental |
| Vivienda | Adquisición vivienda habitual discapacitados | Home purchase by disabled |
| Vivienda | Primera adquisición vivienda jóvenes ≤35 | First home under 35 |
| Sostenibilidad | Instalaciones autoconsumo renovable | Renewable self-consumption |
| Movilidad | Adquisición vehículos nuevos | New vehicle purchase |
| Donaciones | Donativos medioambientales | Environmental donations |
| Donaciones | Donaciones patrimonio cultural valenciano | Valencian cultural heritage |
| Educación | Gastos educativos: libros, transporte, comedor | School expenses |

### 3.11 Extremadura (13 deductions)

**Extremadura deductions**

| Category | Deduction | Key Requirements |
| --- | --- | --- |
| Familia | Cuidado hijos menores 14 años | Childcare for children under 14 |
| Vivienda | Adquisición vivienda habitual jóvenes | Young people buying home |
| Vivienda | Alquiler vivienda habitual jóvenes | Young people renting |
| Trabajo | Trabajo dependiente | Dependent employment income |
| Donaciones | Donaciones entidades Extremadura | Regional donations |

### 3.12 Galicia (21 deductions)

**Galicia deductions**

| Category | Deduction | Key Requirements |
| --- | --- | --- |
| Familia | Nacimiento o adopción | Birth/adoption |
| Familia | Familia numerosa | Large family |
| Familia | Cuidado hijos menores | Childcare |
| Vivienda | Inversión vivienda habitual | Home purchase |
| Vivienda | Alquiler vivienda habitual | Rental |
| Educación | Gastos universitarios | University expenses |
| Discapacidad | Contribuyentes con discapacidad ≥33% | Disability |
| Donaciones | Donativos entidades gallegas | Galician donations |

### 3.13 La Rioja (23 deductions)

**La Rioja deductions**

| Category | Deduction | Key Requirements |
| --- | --- | --- |
| Familia | Nacimiento y adopción | Birth/adoption |
| Vivienda | Inversión vivienda habitual jóvenes | Young people buying |
| Vivienda | Alquiler vivienda habitual jóvenes | Young people renting |
| Movilidad | Adquisición bicicletas pedaleo no asistido | Non-electric bicycle purchase |
| Donaciones | Donativos culturales, medioambientales | Cultural/environmental donations |
| Educación | Gastos escolarización | School expenses |

### 3.14 Comunidad de Madrid (26 deductions)

**Madrid deductions**

| Category | Deduction | Key Requirements |
| --- | --- | --- |
| Familia | Nacimiento o adopción | EUR 600/child (EUR 600 additional if multiple) |
| Familia | Adopción internacional | EUR 600/child |
| Familia | Acogimiento familiar menores | EUR 600-900/minor |
| Familia | Acogimiento no remunerado mayores 65/discapacitados | EUR 900/person |
| Vivienda | Arrendamiento vivienda habitual | 30% rent, max EUR 1,000 (under 35) |
| Actividad Económica | Fomento autoempleo jóvenes <35 | EUR 1,000 for new self-employed under 35 |
| Territorial | Cambio residencia municipio despoblación | Relocation to depopulating area |
| Donaciones | Donativos fundaciones culturales | 15% of donations |
| Donaciones | Donativos medioambientales | 15% of donations |
| Educación | Gastos educativos (escolaridad, idiomas, vestuario) | EUR 400-900/child depending on stage |

### 3.14 Comunidad de Madrid (26 deductions)

Madrid typical income limits for housing deductions:
- Base imponible general + ahorro < EUR 25,620 (individual) / EUR 36,200 (joint)

### 3.15 Región de Murcia (22 deductions)

**Murcia deductions**

| Category | Deduction | Key Requirements |
| --- | --- | --- |
| Familia | Gastos guardería menores 3 años | Nursery for children under 3 |
| Vivienda | Inversión vivienda habitual jóvenes | Young people buying home |
| Vivienda | Arrendamiento vivienda habitual | Rental deduction |
| Sostenibilidad | Instalaciones recursos energéticos renovables | Renewable energy installations |
| Donaciones | Donativos medioambientales | Environmental donations |
| Discapacidad | Contribuyentes con discapacidad | Disability ≥33% |

## Section 4 -- Foral Territories

### 4.1 País Vasco (Álava, Bizkaia, Gipuzkoa)

- **País Vasco foral system** — The three Basque provinces have their OWN IRPF system entirely separate from the common territory. They set their own: Tax brackets (generally lower than common territory for low-to-mid incomes); Deductions (different catalogue); Minimum exemptions. Key differences from common territory: IRPF brackets: 7 progressive brackets from 23% to 49% (2025); Mínimo personal exento: EUR 5,472; No split state/regional -- single scale; Own deductions catalogue not covered by AEAT XSD. Regime classifier: If the taxpayer's fiscal residence is in País Vasco, use foral basque rules. Do NOT apply common territory deductions.

### 4.2 Navarra (Comunidad Foral de Navarra)

- **Navarra foral system** — Navarra has its own complete IRPF system: 11 progressive brackets from 13% to 52.8%; Mínimo personal: ~EUR 5,500; Own deductions set; Filed with Hacienda Foral de Navarra, NOT AEAT. Regime classifier: If fiscal residence is Navarra, use foral navarra rules exclusively.

### 4.3 Ceuta and Melilla

- **Ceuta and Melilla benefits** — Ceuta and Melilla are NOT autonomous communities but autonomous cities. They use the common territory IRPF scale but benefit from: 60% deduction on cuota íntegra (Art. 68.4 LIRPF) for income generated there; 50% bonificación on cuota autónomos for specific sectors (Agriculture, Industry, Commerce, Tourism). This effectively means total IRPF rates are ~40% of what common territory taxpayers pay.  _(Art. 68.4 LIRPF)_

## Section 5 -- Deduction Categories Explained

**Deduction categories**

| Category | Count | Description |
| --- | --- | --- |
| Familia | 74 | Birth, adoption, large families, childcare, single parents |
| Vivienda | 74 | Home purchase, rental, renovation, protected housing |
| General | 65 | Broad-application deductions, income-based |
| Donaciones | 39 | Ecological, cultural, scientific, heritage donations |
| Discapacidad | 27 | Taxpayer or family member disability ≥33% |
| Educación | 20 | School materials, tuition, university, training |
| Inversión | 18 | Startup investment, company shares |
| Salud | 9 | Healthcare, elderly care, legal costs |
| Sostenibilidad | 3 | Renewable energy, self-consumption installations |
| Territorial | 3 | Rural depopulation incentives, island relocation |
| Trabajo | 3 | Employment mobility, relocation |
| Movilidad | 2 | Vehicle/bicycle purchase |
| Actividad Económica | 2 | Self-employment, entrepreneurship |

## Section 6 -- How to Apply Regional Deductions (Computation)

### Step-by-Step Process

- **Step-by-step computation process** — 1. Identify the taxpayer's Comunidad Autónoma of fiscal residence (where they lived on 31 December of the tax year) 2. Compute the cuota íntegra autonómica using that CCAA's regional brackets 3. Apply mínimo personal y familiar at the regional rate to get cuota líquida autonómica 4. Sum all applicable regional deductions for which the taxpayer qualifies 5. Cap: Total deductions cannot exceed the cuota líquida autonómica (floor = 0) 6. Result: Cuota diferencial autonómica = cuota líquida autonómica - deducciones autonómicas

### Common Eligibility Requirements

- **Common eligibility requirements** — Most deductions require: Income limit: Base imponible general + base imponible del ahorro below a threshold (varies by CCAA, typically EUR 25,000-30,000 individual, EUR 36,000-50,000 joint); Residency: Fiscal residence in the CCAA during the full tax year; Documentation: Supporting invoices, certificates, or official documents; Non-duplication: Cannot apply overlapping state and regional deductions for the same expense.

## Section 7 -- Conservative Defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown Comunidad Autónoma | DO NOT apply any regional deductions; ask first |
| Income limit unknown | Assume limit is exceeded (conservative = no deduction) |
| Foral vs common territory unknown | Ask -- critical difference in entire tax computation |
| Joint vs individual filing unknown | Assume individual (lower deduction limits) |
| Child disability not documented | Do not apply disability deduction |
| Duration of residency in CCAA unknown | Ask -- partial-year residency affects eligibility |

## Section 8 -- Worked Example: Madrid Taxpayer

Input: María, 32, single, one child born 2025, rents apartment EUR 800/month. Base imponible EUR 22,000. Fiscal residence: Madrid.

Applicable Madrid deductions:
1. Por nacimiento de hijos: EUR 600
2. Arrendamiento vivienda habitual (under 35): 30% × EUR 9,600 annual rent = EUR 2,880, capped at EUR 1,000
3. Total deductions: EUR 600 + EUR 1,000 = EUR 1,600

Result: María's cuota autonómica is reduced by EUR 1,600.

## Section 9 -- Casilla Reference (AEAT Modelo 100)

Regional deductions are declared in casillas 0850-1200+ of the AEAT Modelo 100 form. Each CCAA has assigned casilla ranges. Key ranges:

## Section 9 -- Casilla Reference (AEAT Modelo 100)

**CCAA casilla ranges**

| CCAA | Casilla Range (approximate) |
| --- | --- |
| Andalucía | 0850-0870 |
| Aragón | 0871-0900 |
| Asturias | 0901-0930 |
| Baleares | 0931-0960 |
| Canarias | 0961-0990 |
| Cantabria | 0991-1010 |
| Castilla y León | 1011-1040 |
| Castilla-La Mancha | 1041-1070 |
| Cataluña | 1071-1090 |
| Comunidad Valenciana | 1091-1140 |
| Extremadura | 1141-1160 |
| Galicia | 1161-1185 |
| La Rioja | 1186-1210 |
| Madrid | 1211-1240 |
| Murcia | 1241-1270 |

## Section 10 -- Interaction with State Deductions

- **State/regional deduction interaction** — Some deductions exist at BOTH state and regional level: Maternidad (maternity): State deduction EUR 1,200/year + some CCAA add regional top-up; Familia numerosa: State deduction + some CCAA add extra; Donativos: State deduction (Ley 49/2002) + CCAA-specific donation deductions; Vivienda habitual pre-2013: State transitional deduction + CCAA may maintain their own. Rule: State and regional deductions for the SAME concept may coexist (they reduce different portions of the tax). However, the same expense cannot generate deductions at BOTH levels if the law explicitly prohibits it.  _(Ley 49/2002)_

## PROHIBITIONS

- NEVER apply regional deductions without confirming the Comunidad Autónoma of fiscal residence
- NEVER apply common territory deductions to a foral (País Vasco / Navarra) taxpayer
- NEVER exceed the cuota líquida autonómica (deductions cannot create a refund from the regional portion alone)
- NEVER assume income limits are met -- verify base imponible first
- NEVER confuse the 60% Ceuta/Melilla deduction (state-level, Art. 68.4) with regional deductions
- NEVER apply 2024 deduction amounts to 2025 filings without checking for updates (rates change annually)
- NEVER claim a deduction without proper documentation (facturas, certificates, padron)
- NEVER apply Madrid deductions to a taxpayer whose fiscal residence is in another CCAA

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The deduction catalogue changes annually. CCAA legislatures modify amounts, add new deductions, and remove others each fiscal year. Always verify against the current year's published BOE/BOJA/DOGC/DOGV/etc.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — no liability on either side until you and the accountant sign
a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
