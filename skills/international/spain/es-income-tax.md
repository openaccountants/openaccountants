---
name: es-income-tax
description: >
  Use this skill whenever asked about Spanish personal income tax (IRPF -- Impuesto sobre la Renta de las Personas Fisicas) for self-employed individuals (autonomos). Trigger on phrases like "how much tax do I pay in Spain", "IRPF", "Modelo 100", "Modelo 130", "pago fraccionado", "estimacion directa", "retencion", "autonomo tax", "rendimientos de actividades economicas", "gastos deducibles", "amortizacion", "minimo personal", "cuota autonomica", or any question about filing or computing income tax for a self-employed or freelance client in Spain. Also trigger when preparing or reviewing a Modelo 100 return, computing deductible expenses, advising on quarterly payments (pagos fraccionados), or explaining withholding (retenciones) on professional invoices. This skill covers IRPF progressive rates, Modelo 100 structure, estimacion directa normal vs simplificada, deductible expenses, depreciation (amortizacion), quarterly payments (Modelo 130), withholding (retenciones), regional surcharges (cuota autonomica), personal and family allowances (minimo personal y familiar), deducciones, penalties, and interaction with IVA and Social Security. ALWAYS read this skill before touching any Spanish income tax work.
version: 1.0
jurisdiction: ES
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Spain Income Tax (IRPF) -- Self-Employed (Autonomo) Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Spain (Estado Espanol) |
| Jurisdiction Code | ES |
| Primary Legislation | Ley 35/2006 del Impuesto sobre la Renta de las Personas Fisicas (LIRPF) |
| Supporting Legislation | Real Decreto 439/2007 (RIRPF -- Reglamento); Ley 58/2003 (Ley General Tributaria); Orden de 27 de marzo de 1998 (Tabla de Amortizacion Simplificada) |
| Tax Authority | Agencia Estatal de Administracion Tributaria (AEAT) |
| Filing Portal | Sede Electronica de la Agencia Tributaria (sede.agenciatributaria.gob.es) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a qualified asesor fiscal or economista colegiado in Spain |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate table application, Modelo 100 structure, Modelo 130 calculation, retencion rates, minimo personal amounts, amortizacion tables, filing deadlines. Tier 2: mixed-use expense apportionment, home office deduction, vehicle business %, estimacion directa normal vs simplificada choice, regional surcharge variations. Tier 3: non-resident income, Beckham Law (regimen especial), regime de modulos (estimacion objetiva), complex capital gains, multi-regional activity. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified asesor fiscal must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any IRPF figure, you MUST know:

1. **Comunidad autonoma of fiscal residence** [T1] -- determines the regional (autonomica) portion of the tax. STOP if unknown.
2. **Type of economic activity** [T1] -- professional (seccion 2 IAE) or business/commercial (seccion 1 IAE). Determines retencion obligations.
3. **Estimation regime** [T1] -- estimacion directa normal or simplificada. Default is simplificada unless turnover exceeds EUR 600,000 or the taxpayer has voluntarily elected normal.
4. **Gross income from self-employment** [T1] -- total invoiced/received in the tax year.
5. **Business expenses** [T1/T2] -- nature and amount of each expense (T2 for mixed-use items).
6. **Capital assets acquired in the year** [T1] -- type, cost, date first used in business.
7. **Retenciones soportadas** [T1] -- total IRPF withheld by clients on professional invoices during the year.
8. **Pagos fraccionados (Modelo 130)** [T1] -- total quarterly payments made during the year.
9. **Marital/family status** [T1] -- for minimo personal y familiar calculation (age, dependants, disability).
10. **Other income** [T1] -- employment income (rendimientos del trabajo), rental, capital gains, dividends, interest.
11. **Cotizaciones a la Seguridad Social (RETA)** [T1] -- Social Security contributions paid as autonomo.
12. **Years registered as autonomo** [T1] -- determines retencion rate (7% first 3 years vs 15% standard).

**If comunidad autonoma is unknown, STOP. Do not apply regional rates. Fiscal residence is mandatory.**

---

## Step 1: Determine IRPF Progressive Rate Table [T1]

**Legislation:** LIRPF Art. 63 (escala estatal), Art. 74 (escala autonomica)

The IRPF is split into two components: the cuota estatal (state portion) and the cuota autonomica (regional portion). The combined general rates below reflect the standard state + common regional scale. Regional variations exist -- see Step 10.

### Combined General Scale (Base Liquidable General) -- 2025

| Base Liquidable (EUR) | Marginal Rate | Cumulative Tax at Top of Band |
|----------------------|---------------|-------------------------------|
| 0 -- 12,450 | 19% | EUR 2,365.50 |
| 12,451 -- 20,200 | 24% | EUR 4,225.50 |
| 20,201 -- 35,200 | 30% | EUR 8,725.50 |
| 35,201 -- 60,000 | 37% | EUR 17,901.50 |
| 60,001 -- 300,000 | 45% | EUR 125,901.50 |
| 300,001+ | 47% | -- |

### State Portion Only (Escala Estatal)

| Base Liquidable (EUR) | Marginal Rate |
|----------------------|---------------|
| 0 -- 12,450 | 9.50% |
| 12,451 -- 20,200 | 12.00% |
| 20,201 -- 35,200 | 15.00% |
| 35,201 -- 60,000 | 18.50% |
| 60,001 -- 300,000 | 22.50% |
| 300,001+ | 24.50% |

### Savings Income Scale (Base Liquidable del Ahorro) -- 2025

| Base Liquidable (EUR) | Marginal Rate |
|----------------------|---------------|
| 0 -- 6,000 | 19% |
| 6,001 -- 50,000 | 21% |
| 50,001 -- 200,000 | 23% |
| 200,001 -- 300,000 | 27% |
| 300,001+ | 28% |

**Note:** Self-employment income (rendimientos de actividades economicas) is taxed under the general scale, NOT the savings scale. The savings scale applies to dividends, interest, and capital gains only.

**Spain does NOT have a zero-rate band. The minimum exempt amount (minimo personal y familiar) achieves a similar effect -- see Step 6.**

---

## Step 2: Modelo 100 -- Annual Return Structure [T1]

**Legislation:** LIRPF; RIRPF; Modelo 100 form guidance (AEAT)

The Modelo 100 is the annual IRPF self-assessment return. Key sections for autonomos:

| Section | Description | How to Populate |
|---------|-------------|-----------------|
| Rendimientos del trabajo | Employment income (if any) | Gross salary minus deductible expenses (Seguridad Social, etc.) |
| Rendimientos de actividades economicas | Self-employment income | Net profit from business activity -- see Step 3 |
| Rendimientos del capital mobiliario | Investment income | Dividends, interest, royalties |
| Rendimientos del capital inmobiliario | Rental income | Net rental income after deductible expenses |
| Ganancias y perdidas patrimoniales | Capital gains/losses | Sale of assets, property, investments |
| Base imponible general | General taxable base | Sum of general income types |
| Base imponible del ahorro | Savings taxable base | Investment/savings income |
| Reducciones de la base imponible | Reductions | Pension contributions, joint filing reduction, etc. |
| Minimo personal y familiar | Personal/family allowance | See Step 6 |
| Cuota integra | Gross tax liability | Rate table applied to base liquidable |
| Deducciones | Tax credits/deductions | See Step 11 |
| Cuota liquida | Net tax liability | Cuota integra minus deducciones |
| Retenciones y pagos a cuenta | Withholdings and payments on account | Retenciones + Modelo 130 payments |
| Cuota diferencial | Tax due / refund | Cuota liquida minus retenciones and pagos a cuenta |

---

## Step 3: Rendimientos de Actividades Economicas [T1]

**Legislation:** LIRPF Arts. 27-32; RIRPF Arts. 28-39

### Estimacion Directa Simplificada vs Normal [T1/T2]

| Feature | Simplificada | Normal |
|---------|-------------|--------|
| Eligibility | Turnover under EUR 600,000 in prior year | All taxpayers; mandatory if turnover >= EUR 600,000 |
| Default | YES -- applies automatically unless excluded or taxpayer elects normal | Must be elected or triggered by turnover |
| Accounting | Libro de ventas e ingresos + Libro de compras y gastos | Full accounting per Codigo de Comercio (double-entry) |
| Depreciation | Simplified depreciation table (Orden 27/03/1998) | Corporate Income Tax tables (more detailed) |
| Provisions | NOT deductible individually | Deductible if properly justified |
| Hard-to-justify expenses | 5% of net income (max EUR 2,000/year) | NOT available |
| Complexity | Lower | Higher |

### Net Income Computation -- Estimacion Directa Simplificada [T1]

```
  Gross income (ingresos computables)
- Deductible expenses (gastos deducibles) -- see Step 4
- Depreciation (amortizacion) -- see Step 5
= Rendimiento neto previo

- Reduccion por gastos de dificil justificacion (5% of rendimiento neto previo, max EUR 2,000)
= Rendimiento neto reducido de la actividad
```

### Net Income Computation -- Estimacion Directa Normal [T1]

```
  Gross income (ingresos computables)
- Deductible expenses (gastos deducibles) -- see Step 4
- Depreciation (amortizacion) -- see Step 5
- Provisions (provisiones deducibles)
= Rendimiento neto de la actividad
```

**The 5% hard-to-justify expense deduction (gastos de dificil justificacion) is ONLY available in simplificada. Do NOT apply it under normal.**

---

## Step 4: Gastos Deducibles -- Deductible Expenses [T1/T2]

**Legislation:** LIRPF Art. 28; RIRPF Art. 30; Ley 27/2014 del Impuesto sobre Sociedades (LIS) by reference

### The Correlation Principle [T1]

An expense is deductible only if it is directly linked to the economic activity, properly documented with a valid invoice (factura), and recorded in the required books. Expenses must correlate with income generation.

### Deductible Expenses

| Expense | Tier | Treatment |
|---------|------|-----------|
| Cotizaciones Seguridad Social (RETA) | T1 | Fully deductible -- both as expense of the activity and as reduccion |
| Office rent (local afecto a la actividad) | T1 | Fully deductible if exclusively for business |
| Professional insurance (seguro de responsabilidad civil) | T1 | Fully deductible |
| Gestor/asesor fiscal fees | T1 | Fully deductible |
| Legal fees (business-related) | T1 | Fully deductible |
| Office supplies / stationery | T1 | Fully deductible |
| Software subscriptions (SaaS, cloud tools) | T1 | Fully deductible if business-only |
| Marketing / advertising | T1 | Fully deductible |
| Bank charges (business account) | T1 | Fully deductible |
| Training / courses related to activity | T1 | Fully deductible |
| Professional association fees (colegio profesional) | T1 | Fully deductible |
| Travel (transport, accommodation for business) | T1 | Fully deductible if wholly business purpose |
| Per-diem meals during travel | T1 | Up to EUR 26.67/day within Spain; EUR 48.08/day abroad. Must be in a restaurant, paid by card or electronic means |
| Health insurance (seguro medico privado) | T1 | Deductible up to EUR 500/year per insured person (taxpayer + spouse + children under 25 living in household). EUR 1,500 if disabled. |
| Phone / mobile | T2 | Business use portion only -- client must justify percentage |
| Vehicle expenses (fuel, insurance, maintenance) | T2 | Generally NOT deductible unless vehicle is exclusively for business (transport, delivery, taxi, etc.). Partial deduction is contentious -- see vehicle rules below |
| Home office supplies (suministros) | T2 | 30% of the proportional share based on m2 dedicated to business vs total m2. See home office rules |
| Entertaining / meals with clients | T2 | Deductible up to 1% of net turnover. Must be properly documented. Flag for reviewer |

### NOT Deductible [T1]

| Expense | Reason |
|---------|--------|
| Personal living expenses | Not linked to economic activity |
| Fines and penalties (multas y sanciones) | Public policy -- LIRPF Art. 14 |
| IRPF itself | Tax on income is not deductible against income |
| Donations | Not a business expense (may qualify for deduccion -- see Step 11) |
| Capital expenditure | Goes through amortizacion, not gastos |
| Personal vehicle costs (unapportioned) | Contentious -- see vehicle rules |
| Gifts to clients exceeding limits | Only deductible if properly documented and within customs |

### Home Office Rules (Suministros) [T2]

**Legislation:** LIRPF Art. 30.2.5.c (introduced by Ley 6/2017 de Reformas Urgentes del Trabajo Autonomo)

- Calculate the proportion of the home dedicated to business: m2 used for business / total m2
- Apply 30% of that proportion to: electricity, water, gas, internet, telephone
- Example: Home = 100 m2, office = 15 m2. Proportion = 15%. Electricity bill EUR 1,200/year. Deductible = EUR 1,200 x 15% x 30% = EUR 54
- The space does NOT need to be exclusively dedicated, but the proportion must be reasonable and documented
- Must have registered the home address (or partial use) with AEAT via Modelo 036/037
- [T2] Flag for reviewer: confirm m2 declaration, that Modelo 036/037 reflects partial business use

### Vehicle Rules [T2]

**Legislation:** LIRPF Art. 22; LIS Art. 15 by reference; AEAT administrative doctrine

- Vehicles are generally NOT deductible for IRPF unless used EXCLUSIVELY in the activity
- Activities where full deduction is accepted: commercial agents, taxi drivers, delivery services, driving instructors, transport businesses
- For all other autonomos, AEAT's administrative position is that personal vehicles used partially for business are NOT deductible for IRPF (unlike IVA, where 50% input VAT is commonly accepted)
- This is a frequent source of disputes. [T2] Flag for reviewer: confirm whether client's activity qualifies for vehicle deduction
- If deductible: depreciation, fuel, insurance, maintenance -- all at 100% if exclusive business use

**CRITICAL: The IVA 50% vehicle rule does NOT automatically apply to IRPF. They are separate taxes with separate rules. A vehicle may be 50% deductible for IVA but 0% for IRPF.**

---

## Step 5: Amortizacion -- Depreciation [T1]

**Legislation:** LIRPF Art. 30; Orden de 27 de marzo de 1998 (simplified table); LIS Art. 12 (normal table)

### Simplified Depreciation Table (Estimacion Directa Simplificada) [T1]

| Asset Group | Maximum Annual Rate | Maximum Useful Life (Years) |
|------------|--------------------|-----------------------------|
| Commercial buildings (edificios) | 3% | 68 |
| Industrial buildings (naves) | 3% | 68 |
| Furniture and fittings (mobiliario) | 10% | 20 |
| Office equipment (equipos y enseres) | 10% | 20 |
| Computer hardware (equipos informaticos) | 26% | 10 |
| Computer software (aplicaciones informaticas) | 26% | 10 |
| Motor vehicles (vehiculos) | 16% | 14 |
| Tools and utensils (utiles y herramientas) | 30% | 8 |
| Machinery (maquinaria) | 12% | 18 |
| Other tangible assets (otros) | 10% | 20 |

### Rules [T1]

- Depreciation is calculated using the **straight-line method** (metodo lineal) on cost price
- Depreciation starts from the date the asset is **put into use** in the business
- If acquired partway through the year, depreciation is prorated (days or months in use / total days or months in year)
- The taxpayer may choose any rate between the minimum (cost / maximum useful life years) and maximum annual rate
- Assets below approximately EUR 300 are commonly expensed directly, though AEAT does not set a formal low-value threshold for IRPF -- [T2] flag if material
- Residual value is typically assumed to be zero for tax purposes

### Example [T1]

Laptop purchased for EUR 1,200, put into use 1 July 2025:
- Maximum rate: 26%
- Annual depreciation: EUR 1,200 x 26% = EUR 312
- Prorated (184 days / 365 days): EUR 312 x 0.504 = EUR 157.25 for 2025

---

## Step 6: Minimo Personal y Familiar [T1]

**Legislation:** LIRPF Arts. 57-61

The minimo personal y familiar is NOT a deduction from income. It is the amount of income exempt from taxation, applied as a reduction from the cuota integra (gross tax) by computing tax on the minimo amount at the same progressive rates and subtracting it.

### Personal Allowance (Minimo del Contribuyente) [T1]

| Taxpayer Age | Annual Amount (EUR) |
|-------------|---------------------|
| Under 65 | 5,550 |
| 65 or over | 6,700 (5,550 + 1,150) |
| 75 or over | 8,100 (5,550 + 1,150 + 1,400) |

### Descendant Allowance (Minimo por Descendientes) [T1]

Applies for children under 25 (or any age if disabled) living with the taxpayer and with income under EUR 8,000/year (excluding exempt income) and who have not filed their own return with income over EUR 1,800.

| Descendant | Annual Amount (EUR) |
|-----------|---------------------|
| 1st child | 2,400 |
| 2nd child | 2,700 |
| 3rd child | 4,000 |
| 4th and subsequent | 4,500 |
| Additional: child under 3 years old | +2,800 |

### Ascendant Allowance (Minimo por Ascendientes) [T1]

Applies for parents/grandparents over 65 living with the taxpayer with income under EUR 8,000/year.

| Ascendant Age | Annual Amount (EUR) |
|-------------|---------------------|
| Over 65 | 1,150 |
| Over 75 | 2,550 (1,150 + 1,400) |

### Disability Allowance (Minimo por Discapacidad) [T1]

| Degree of Disability | Additional Amount (EUR) |
|---------------------|------------------------|
| 33% to 64% | 3,000 |
| 65% or more | 9,000 |
| Assistance required (65%+ with mobility) | +3,000 |

### How It Works Mechanically [T1]

```
1. Compute cuota integra (gross tax) on the base liquidable general using the progressive rate table
2. Compute "tax on the minimo" by applying the same progressive rate table to the total minimo personal y familiar amount
3. Cuota integra reducida = cuota integra - tax on the minimo
```

This means the minimo saves tax at the taxpayer's lowest marginal rate (19% on the first EUR 5,550 = EUR 1,054.50 for a standard taxpayer under 65).

---

## Step 7: Reduccion por Rendimientos del Trabajo [T1]

**Legislation:** LIRPF Art. 20

This reduction applies ONLY to employment income (rendimientos del trabajo), NOT to self-employment income.

| Net Employment Income (EUR) | Reduction (EUR) |
|---------------------------|-----------------|
| Up to 14,047.50 | 6,498 |
| 14,047.50 -- 19,747.50 | 6,498 - 1.14 x (income - 14,047.50) |
| Over 19,747.50 | 0 |

**If the autonomo has NO employment income, this step is skipped entirely. Do NOT apply this reduction to rendimientos de actividades economicas.**

---

## Step 8: Pagos Fraccionados -- Modelo 130 [T1]

**Legislation:** LIRPF Art. 109; RIRPF Arts. 109-112

### Who Must File [T1]

All autonomos in estimacion directa (normal or simplificada) conducting economic activities MUST file Modelo 130 quarterly, UNLESS at least 70% of their prior year professional income (actividades profesionales, seccion 2 IAE) was subject to retencion (withholding).

If the 70% exception applies, the professional is exempt from Modelo 130 but MUST still file Modelo 100 annually.

### Computation (Estimacion Directa) [T1]

```
  Cumulative net income (ingresos - gastos) from 1 January to end of quarter
x 20%
- Cumulative pagos fraccionados already paid in prior quarters of the same year
- Cumulative retenciones soportadas from 1 January to end of quarter
= Amount to pay (if positive) or zero (negative result = EUR 0, no refund mid-year)
```

### Filing Deadlines [T1]

| Quarter | Period Covered | Filing Deadline |
|---------|---------------|-----------------|
| Q1 (1T) | 1 Jan -- 31 Mar | 1--20 April |
| Q2 (2T) | 1 Apr -- 30 Jun | 1--20 July |
| Q3 (3T) | 1 Jul -- 30 Sep | 1--20 October |
| Q4 (4T) | 1 Oct -- 31 Dec | 1--30 January (following year) |

**The Modelo 130 is CUMULATIVE. Each quarter reports from 1 January through the end of the quarter, not just the quarter itself. Prior quarter payments are subtracted to arrive at the incremental amount due.**

### Example [T1]

Q1: Net income EUR 8,000. Retenciones EUR 400. Pago = (8,000 x 20%) - 0 - 400 = EUR 1,200.
Q2: Cumulative net income EUR 18,000. Cumulative retenciones EUR 900. Pago = (18,000 x 20%) - 1,200 - 900 = EUR 1,500.

---

## Step 9: Retenciones -- Withholding on Professional Invoices [T1]

**Legislation:** LIRPF Art. 99; RIRPF Arts. 95, 101

### Who Must Apply Retenciones [T1]

Professionals (actividades profesionales, seccion 2 IAE) must apply IRPF withholding on invoices issued to:
- Companies (sociedades)
- Other autonomos or professionals
- Any entity obligated to withhold

Retenciones are NOT applied on invoices to private individuals (particulares) or foreign clients without a permanent establishment in Spain.

Business activities (actividades empresariales, seccion 1 IAE -- e.g., retail, hospitality, construction) generally do NOT apply retenciones on their sales invoices.

### Rates [T1]

| Situation | Retencion Rate |
|----------|---------------|
| Standard professional | 15% |
| New professional (year of registration + 2 following calendar years) | 7% |
| Certain agricultural/livestock activities | 2% |
| Certain forestry activities | 2% |
| Business activities in estimacion objetiva (modulos) | 1% |

### Requirements for 7% Reduced Rate [T1]

- The autonomo must be newly registered (alta) for the first time or not have been registered in the prior calendar year
- Applies during the year of registration and the two following calendar years
- Must notify the client in writing that the reduced rate applies
- [T2] If the autonomo previously exercised a different professional activity, confirm eligibility with AEAT criteria

### Interaction with Modelo 130 [T1]

Retenciones reduce the Modelo 130 quarterly payment (subtracted in the computation). They also reduce the final Modelo 100 annual liability. The autonomo receives credit for all retenciones withheld during the year, as reported by clients via Modelo 190.

---

## Step 10: Cuota Autonomica -- Regional Surcharge [T2]

**Legislation:** LIRPF Art. 74; individual Comunidad Autonoma legislation

### How It Works [T1]

The IRPF is split approximately 50/50 between the state and the comunidad autonoma. The state scale is fixed nationwide. Each comunidad autonoma sets its own regional scale, which may differ from the common scale shown in Step 1.

### Common Regional Scale (Tarifa Autonomica Comun) [T1]

Most comunidades apply rates close to the common scale, but some have higher or lower rates. The combined rates in Step 1 reflect the common scale.

### Notable Regional Variations [T2]

| Comunidad Autonoma | Notable Difference |
|--------------------|--------------------|
| Madrid | Lower top marginal rates -- generally the lowest regional rates in Spain |
| Cataluna | Higher top marginal rates -- combined top rate can exceed 50% |
| Andalucia | Moderate -- broadly aligned with common scale |
| Comunidad Valenciana | Higher rates in upper brackets |
| Pais Vasco / Navarra | SEPARATE tax systems (regimen foral) -- entirely different rules. [T3] Escalate. |

**[T3] CRITICAL: The Basque Country (Pais Vasco -- Alava, Guipuzcoa, Vizcaya) and Navarra have their own fiscal regimes (regimen foral). This skill does NOT cover those territories. Any client fiscally resident in Pais Vasco or Navarra must be escalated immediately.**

---

## Step 11: Deducciones -- Tax Credits and Deductions [T1/T2]

**Legislation:** LIRPF Arts. 68-69; individual Comunidad Autonoma legislation

### State-Level Deducciones [T1]

| Deduccion | Amount / Rate | Notes |
|----------|--------------|-------|
| Inversion en vivienda habitual (primary residence mortgage) | 15% of amounts paid, max base EUR 9,040/year | ONLY for mortgages taken out BEFORE 1 Jan 2013. Transitional regime. |
| Donativos (donations) to qualifying entities | 80% on first EUR 250; 40% on excess (45% if recurring 3+ years) | Must be to entities under Ley 49/2002 |
| Deduccion por maternidad | EUR 1,200/year per child under 3 | Working mothers only. Can be advanced monthly (EUR 100/month) |
| Deduccion por familia numerosa | EUR 1,200 -- 2,400/year | Depends on category (general vs especial) |
| Planes de pensiones (pension contributions) | Reduces base imponible (not cuota) | Max EUR 1,500/year (or EUR 8,500 including employer contributions) |

### Regional Deducciones [T2]

Each comunidad autonoma offers its own deducciones (e.g., rent deductions, birth/adoption credits, education expenses). These vary significantly.

- [T2] Flag for reviewer: always check the specific comunidad autonoma's deducciones applicable to the client's situation

---

## Step 12: Interaction with IVA [T1]

**Legislation:** Ley 37/1992 del IVA; LIRPF

| Scenario | IRPF Treatment |
|----------|---------------|
| IVA collected on sales (IVA repercutido) | NOT income -- it is a liability to AEAT. Exclude from ingresos. |
| Input IVA recovered (IVA deducible) | NOT an expense -- it is reclaimable. Exclude from gastos. |
| Input IVA NOT deductible (e.g., under regime de recargo de equivalencia or exempt activities) | IS an expense -- adds to the cost. Include in gastos. |
| Autonomo in recargo de equivalencia | All IVA paid on purchases is a cost. Full gross amount is the expense. |
| IVA on mixed-use items (e.g., vehicle 50% IVA deduction) | The non-deductible IVA portion is an IRPF expense. The deductible IVA portion is NOT. |

**Key rule:** For autonomos on the general IVA regime, only non-deductible IVA appears in the IRPF computation. Reclaimable IVA is a balance sheet/IVA-only item.**

---

## Step 13: Filing Deadlines [T1]

**Legislation:** LIRPF; RIRPF; Orden HAC anual

| Filing / Payment | Deadline |
|-----------------|----------|
| Modelo 100 (annual IRPF return) | April -- June of following year (typically opens early April, closes 30 June). If result is to pay and direct debit is chosen, deadline is usually 25 June. |
| Modelo 130 Q1 | 1--20 April |
| Modelo 130 Q2 | 1--20 July |
| Modelo 130 Q3 | 1--20 October |
| Modelo 130 Q4 | 1--30 January (following year) |
| Modelo 303 (IVA quarterly) | Same deadlines as Modelo 130 |
| Modelo 390 (IVA annual summary) | 1--30 January (following year) |

**Note:** If the deadline falls on a weekend or public holiday, it extends to the next business day.

---

## Step 14: Penalties [T1]

**Legislation:** Ley 58/2003 (Ley General Tributaria), Arts. 191-206

### Late Filing (Declaracion Extemporanea Voluntaria -- without AEAT request) [T1]

| Delay | Surcharge (Recargo) | Interest |
|-------|---------------------|----------|
| Up to 3 months | 5% of amount due | No interest |
| 3--6 months | 10% of amount due | No interest |
| 6--12 months | 15% of amount due | No interest |
| Over 12 months | 20% of amount due | + late payment interest from month 12 |

### Late Filing (After AEAT Notification -- Requerimiento) [T1]

| Severity | Sanction |
|----------|----------|
| Leve (minor -- up to EUR 3,000 unpaid or no concealment) | 50% of amount due |
| Grave (serious -- EUR 3,000+ or concealment methods used) | 50--100% of amount due |
| Muy grave (very serious -- fraudulent means) | 100--150% of amount due |

### Late Payment Interest (Interes de Demora) [T1]

The annual late payment interest rate is set each year in the Ley de Presupuestos Generales del Estado. For 2025: approximately 4.0625%.

**WARNING:** Penalties for AEAT-initiated adjustments are severe (50--150%). Voluntary regularization (declaracion complementaria) before AEAT acts is always preferable -- the maximum surcharge is 20% with no sanction.**

---

## Step 15: Record Keeping [T1]

**Legislation:** RIRPF Art. 68; Codigo de Comercio

| Requirement | Detail |
|-------------|--------|
| Minimum retention period | 4 years from the end of the filing deadline (prescription period under LGT Art. 66). In practice, 5--6 years recommended. |
| Required books (simplificada) | Libro de ventas e ingresos; Libro de compras y gastos; Libro de bienes de inversion |
| Required books (normal) | Full double-entry accounting per Codigo de Comercio + Plan General de Contabilidad |
| Invoice requirements | Must comply with Real Decreto 1619/2012 (Reglamento de Facturacion): NIF, name, date, description, base imponible, IVA, total |
| Format | Paper or digital (AEAT accepts digital; Verifactu/SII requirements may apply) |

---

## Step 16: Edge Case Registry

### EC1 -- IVA collected included in IRPF income [T1]
**Situation:** Autonomo invoices EUR 1,210 (EUR 1,000 + EUR 210 IVA 21%). Client reports EUR 1,210 as gross income for IRPF.
**Resolution:** Ingresos must show EUR 1,000 only. The EUR 210 IVA repercutido is a liability to AEAT, not income. Correct before filing.

### EC2 -- New autonomo applies 15% retencion instead of 7% [T1]
**Situation:** Autonomo registered in October 2025 applies 15% retencion on invoices to clients.
**Resolution:** The 7% reduced rate applies during 2025, 2026, and 2027 (year of registration + 2 following years). Client should notify recipients in writing and correct future invoices. For already-issued invoices, the excess retencion will be credited on the Modelo 100 annual return.

### EC3 -- Vehicle deduction claimed by consultant [T2]
**Situation:** IT consultant claims 50% of vehicle costs (fuel, insurance, depreciation) as gastos deducibles.
**Resolution:** For IRPF, vehicle expenses are generally NOT deductible unless the vehicle is used EXCLUSIVELY for the activity. AEAT's position for consultants is that a personal vehicle used partially for business is not deductible. The IVA 50% deduction does NOT carry over to IRPF. [T2] Flag for reviewer to confirm activity type and AEAT criteria.

### EC4 -- Gastos de dificil justificacion applied under estimacion directa normal [T1]
**Situation:** Autonomo on estimacion directa normal applies the 5% hard-to-justify expense deduction.
**Resolution:** INCORRECT. The 5% deduction (max EUR 2,000) is ONLY available under estimacion directa simplificada. Remove from computation.

### EC5 -- Modelo 130 not filed because all income has retenciones [T1/T2]
**Situation:** Professional autonomo (seccion 2 IAE) has 100% of income subject to 15% retencion. Does not file Modelo 130.
**Resolution:** CORRECT -- if at least 70% of prior year income from professional activities was subject to retencion, Modelo 130 is not required. [T2] Verify prior year percentage if this is the first year claiming the exemption.

### EC6 -- Home office deduction without Modelo 036/037 declaration [T2]
**Situation:** Autonomo deducts home office suministros but has not declared partial business use of home on Modelo 036/037.
**Resolution:** The deduction requires that the home (or portion) is declared as afecto parcialmente to the activity via Modelo 036/037. Without this declaration, AEAT may reject the deduction on inspection. [T2] Flag for reviewer: advise client to update Modelo 036/037 before claiming.

### EC7 -- Pais Vasco / Navarra resident [T3]
**Situation:** Client says they live in Bilbao (Vizcaya) and asks about IRPF.
**Resolution:** ESCALATE IMMEDIATELY. Pais Vasco and Navarra have entirely separate tax systems (regimen foral) administered by their own tax authorities (Hacienda Foral). This skill does not cover them. Refer to a local asesor fiscal.

### EC8 -- Autonomo with both professional and business activities [T2]
**Situation:** Autonomo is registered for both a professional activity (seccion 2 IAE -- e.g., consulting) and a business activity (seccion 1 IAE -- e.g., e-commerce). Different retencion rules apply.
**Resolution:** Professional invoices require retencion (15% or 7%). Business activity sales do NOT require retencion. Income from both activities is combined in rendimientos de actividades economicas on Modelo 100 but retencion treatment differs. [T2] Flag for reviewer to confirm correct IAE classification and retencion treatment per activity.

### EC9 -- Vivienda habitual deduction claimed for post-2013 mortgage [T1]
**Situation:** Autonomo purchased home in 2020 and claims the 15% housing deduction.
**Resolution:** INCORRECT. The deduccion por inversion en vivienda habitual was abolished for mortgages taken out on or after 1 January 2013. Only taxpayers with pre-2013 mortgages who claimed the deduction before 2013 retain the transitional right. Remove from return.

### EC10 -- Modelo 130 shows negative result [T1]
**Situation:** Q3 cumulative computation: (net income x 20%) - prior payments - retenciones = negative amount.
**Resolution:** The Modelo 130 payment is EUR 0 (zero). Negative results are NOT refunded mid-year. The credit carries forward within the same year's cumulative calculation. Any excess is recovered via the annual Modelo 100.

### EC11 -- Health insurance deduction exceeds EUR 500 per person [T1]
**Situation:** Autonomo pays EUR 900/year for private health insurance and deducts the full amount.
**Resolution:** INCORRECT. The deduction for private health insurance is capped at EUR 500/year per insured person (taxpayer, spouse, children under 25 in household). For a single autonomo, max deduction = EUR 500. The EUR 400 excess is not deductible. Cap is EUR 1,500/person if disabled.

---

## Step 17: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified asesor fiscal must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified asesor fiscal. Document gap.
```

---

## Step 18: Test Suite

### Test 1 -- Standard autonomo, simplificada, mid-range income
**Input:** Single, under 65, no dependants. Comunidad de Madrid (common scale). Estimacion directa simplificada. Gross income EUR 50,000. Deductible gastos EUR 12,000. Amortizacion EUR 500. RETA paid EUR 4,000 (included in gastos). Retenciones soportadas EUR 5,700. Modelo 130 payments EUR 2,500.
**Expected computation:**
- Rendimiento neto previo = 50,000 - 12,000 - 500 = EUR 37,500
- Gastos de dificil justificacion = 37,500 x 5% = EUR 1,875 (under EUR 2,000 cap)
- Rendimiento neto = 37,500 - 1,875 = EUR 35,625
- Base imponible general = EUR 35,625 (no other income)
- Cuota integra = 2,365.50 + 1,860 + 4,627.50 + 157.25 = EUR 9,010.25
- Tax on minimo (EUR 5,550 x 19%) = EUR 1,054.50
- Cuota integra reducida = 9,010.25 - 1,054.50 = EUR 7,955.75
- Cuota liquida = EUR 7,955.75 (no deducciones)
- Retenciones + pagos a cuenta = 5,700 + 2,500 = EUR 8,200
- Cuota diferencial = 7,955.75 - 8,200 = EUR -244.25 (REFUND of EUR 244.25)

### Test 2 -- New autonomo with 7% retencion, first year
**Input:** Single, under 65, no dependants. Andalucia (common scale). Estimacion directa simplificada. First year as autonomo (registered March 2025). Gross income EUR 25,000. Gastos EUR 6,000. Amortizacion EUR 312. RETA EUR 3,600 (in gastos). All income from professional invoices with 7% retencion = EUR 1,750.
**Expected computation:**
- Rendimiento neto previo = 25,000 - 6,000 - 312 = EUR 18,688
- Gastos dificil justificacion = 18,688 x 5% = EUR 934.40
- Rendimiento neto = 18,688 - 934.40 = EUR 17,753.60
- Cuota integra = 2,365.50 + (17,753.60 - 12,450) x 24% = 2,365.50 + 1,272.86 = EUR 3,638.36
- Tax on minimo = EUR 1,054.50
- Cuota integra reducida = 3,638.36 - 1,054.50 = EUR 2,583.86
- Retenciones = EUR 1,750. No Modelo 130 (assuming >70% had retencion).
- Cuota diferencial = 2,583.86 - 1,750 = EUR 833.86 due

### Test 3 -- High-income autonomo, top bracket
**Input:** Single, under 65, 1 child (age 5). Madrid (common scale assumed). Estimacion directa simplificada. Gross income EUR 150,000. Gastos EUR 30,000. Amortizacion EUR 2,000. RETA EUR 5,000 (in gastos). Retenciones EUR 17,700. Modelo 130 payments EUR 8,000.
**Expected computation:**
- Rendimiento neto previo = 150,000 - 30,000 - 2,000 = EUR 118,000
- Gastos dificil justificacion = 118,000 x 5% = EUR 5,900 -- CAPPED at EUR 2,000
- Rendimiento neto = 118,000 - 2,000 = EUR 116,000
- Cuota integra = 2,365.50 + 1,860 + 4,500 + 9,176 + (116,000 - 60,000) x 45% = 17,901.50 + 25,200 = EUR 43,101.50
- Minimo = 5,550 (personal) + 2,400 (1st child) = EUR 7,950. Tax on minimo = 7,950 x 19% = EUR 1,510.50
- Cuota integra reducida = 43,101.50 - 1,510.50 = EUR 41,591
- Retenciones + pagos = 17,700 + 8,000 = EUR 25,700
- Cuota diferencial = 41,591 - 25,700 = EUR 15,891 due

### Test 4 -- Modelo 130 quarterly computation
**Input:** Autonomo in estimacion directa simplificada. Professional activity. Q1 cumulative net income EUR 10,000. Retenciones Q1 EUR 1,500.
**Expected computation:**
- Pago fraccionado Q1 = (10,000 x 20%) - 0 (prior payments) - 1,500 = EUR 500

Q2 cumulative net income EUR 22,000. Cumulative retenciones EUR 3,300.
- Pago fraccionado Q2 = (22,000 x 20%) - 500 (Q1 payment) - 3,300 = EUR 600

### Test 5 -- Home office suministros deduction
**Input:** Home total area 90 m2. Declared business area 10 m2. Annual electricity EUR 1,440. Annual internet EUR 600.
**Expected computation:**
- Proportion = 10/90 = 11.11%
- Electricity deductible = 1,440 x 11.11% x 30% = EUR 47.99
- Internet deductible = 600 x 11.11% x 30% = EUR 20.00
- Total suministros deduction = EUR 67.99

### Test 6 -- Health insurance cap
**Input:** Autonomo pays EUR 1,800/year for family health insurance covering self, spouse, and 1 child under 25. All three live in the household.
**Expected computation:**
- Max per person = EUR 500
- 3 persons x EUR 500 = EUR 1,500 cap
- Deductible amount = EUR 1,500 (EUR 300 excess is NOT deductible)

### Test 7 -- Capital item incorrectly expensed
**Input:** Autonomo on simplificada buys office furniture for EUR 3,000 and includes it fully in gastos deducibles.
**Expected computation:**
- INCORRECT. EUR 3,000 furniture must go through amortizacion.
- Annual depreciation at maximum rate: EUR 3,000 x 10% = EUR 300/year.
- Remove EUR 3,000 from gastos. Add EUR 300 to amortizacion (or prorated if acquired partway through year).

### Test 8 -- IVA incorrectly excluded from IRPF expense
**Input:** Autonomo purchases supplies for EUR 605 (EUR 500 + EUR 105 IVA 21%). The autonomo is on the general IVA regime and deducts the IVA on their Modelo 303. They claim EUR 605 as an IRPF expense.
**Expected computation:**
- INCORRECT. Since the autonomo recovers the EUR 105 IVA via Modelo 303, the IRPF deductible expense is EUR 500 only (net of recoverable IVA). Remove EUR 105 from gastos.

---

## PROHIBITIONS

- NEVER apply the combined rate table without confirming the comunidad autonoma of fiscal residence
- NEVER apply the gastos de dificil justificacion (5%, max EUR 2,000) under estimacion directa normal -- it is ONLY for simplificada
- NEVER apply the reduccion por rendimientos del trabajo to self-employment income -- it is ONLY for employment income
- NEVER include IVA repercutido (collected) as income for IRPF
- NEVER deduct recoverable IVA soportado as an IRPF expense
- NEVER allow vehicle expenses for IRPF without confirming exclusive business use (the IVA 50% rule does NOT apply to IRPF)
- NEVER allow the vivienda habitual deduction for mortgages taken out on or after 1 January 2013
- NEVER advise on Pais Vasco or Navarra fiscal matters -- escalate immediately (regimen foral)
- NEVER issue a Modelo 130 refund mid-year -- negative results are EUR 0, credit recoverable only via Modelo 100
- NEVER exceed health insurance deduction caps (EUR 500/person, EUR 1,500 if disabled)
- NEVER allow capital expenditure as a direct gastos deducible -- it must go through amortizacion
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their asesor fiscal for confirmation
- NEVER allow fines, penalties (multas, sanciones), or IRPF itself as deductible expenses

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal, economista colegiado, or equivalent licensed practitioner in Spain) before filing or acting upon.

This skill does NOT cover the regimen foral (Pais Vasco, Navarra), estimacion objetiva (modulos), non-resident taxation, or the Beckham Law (regimen especial para trabajadores desplazados).

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
