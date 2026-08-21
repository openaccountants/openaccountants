---
name: es-rental-income
description: Use this skill whenever asked about Spanish rental income taxation. Trigger on phrases like "rental income Spain", "alquiler IRPF", "rendimientos del capital inmobiliario", "rental deductions Spain", "60% reduction rental Spain", "non-resident rental Spain", "IBI deduction", "Modelo 100 rental", "vivienda turística", "imputación de rentas inmobiliarias", "valor catastral", "amortización inmueble", or any question about declaring rental income in Spain. This skill covers IRPF rental computation, deductible expenses, the 60% reduction for residential rental, non-resident flat rate, tourist rental, and imputed income for vacant properties. ALWAYS read this skill before touching any Spanish rental income work.
version: "1.0"
jurisdiction: ES
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ES Rental Income

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Spain (Reino de España) |
| Tax | IRPF (Impuesto sobre la Renta de las Personas Físicas) -- Rental Income |
| Currency | EUR only |
| Tax year | 1 January -- 31 December 2025 |
| Primary legislation | Ley 35/2006, de 28 de noviembre, del IRPF; Real Decreto 439/2007 (Reglamento) |
| Supporting legislation | Ley 29/1994 de Arrendamientos Urbanos (LAU); LIRPF Art. 22-23 (rendimientos del capital inmobiliario); LIRNR (non-residents) |
| Tax authority | Agencia Estatal de Administración Tributaria (AEAT) |
| Filing portal | Renta Web (sede.agenciatributaria.gob.es) |
| Filing deadline | April -- June 2026 (Campaña de la Renta) |
| Non-resident rental filing | Modelo 210 (quarterly) |
| Skill version | 1.0 |

### IRPF General Tax Rates (2025) -- Escala general (state + regional average)

**IRPF General Tax Rates (2025) -- Escala general (state + regional average)**

| Taxable Income (EUR) | Marginal Rate (approx.) |
| --- | --- |
| 0 -- 12,450 | 19% |
| 12,451 -- 20,200 | 24% |
| 20,201 -- 35,200 | 30% |
| 35,201 -- 60,000 | 37% |
| 60,001 -- 300,000 | 45% |
| 300,001+ | 47% |

Note: Exact rates vary by Comunidad Autónoma (regional scale applies to ~50% of the tax).

### Key Features

**Key Features**

| Feature | Detail |
| --- | --- |
| Rental income classification | Rendimientos del capital inmobiliario (Art. 22 LIRPF) |
| 60% reduction (residential) | Net rental income reduced by 60% if rented as vivienda habitual (tenant's primary residence) |
| New 2024 Housing Law changes | Reduction of 50%/60%/70%/90% depending on conditions (Ley 12/2023, phasing in) |
| Non-resident rate (non-EU) | 24% on gross income (no deductions) |
| Non-resident rate (EU/EEA) | 19% on net income (deductions allowed) |
| Imputed income (vacant property) | 2% of valor catastral (1.1% if catastral value revised in prior 10 years) |
| Depreciation (amortización) | 3% of the greater of: acquisition cost or valor catastral of construction (excluding land) |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether vivienda habitual of tenant | Do NOT apply 60% reduction |
| Unknown valor catastral breakdown (land/construction) | Do not compute depreciation -- obtain recibo IBI |
| Unknown whether resident or non-resident | Assume resident (IRPF); verify |
| Unknown Comunidad Autónoma | Use state scale only (no regional adjustment) |

## Section 2 -- Classification Rules

### 2.1 Rental Income (Rendimientos del Capital Inmobiliario)

**Rental Income (Rendimientos del Capital Inmobiliario)**

| Income Type | Treatment |
| --- | --- |
| Monthly rent received | Full amount assessable (rendimiento íntegro) |
| Tenant payment of owner expenses (e.g., IBI) | Assessable income if landlord's obligation |
| Security deposit retained (for damages) | Assessable when retained |
| Key money / premium paid by tenant | Assessable |
| Sub-leasing income | Capital mobiliario (different category) unless property owned |

### 2.2 Deductible Expenses (Gastos Deducibles) -- Art. 23 LIRPF

**Deductible Expenses (Gastos Deducibles) -- Art. 23 LIRPF**  _(Art. 23 LIRPF)_

| Expense | Deductible? | Notes |
| --- | --- | --- |
| Mortgage interest (intereses del préstamo) | Yes | Limited to rental income (cannot create a loss from interest alone) |
| IBI (Impuesto sobre Bienes Inmuebles) | Yes | Annual property tax paid to municipality |
| Comunidad de propietarios (community fees) | Yes | Monthly/quarterly community charges |
| Insurance (seguro del hogar, RC) | Yes | Building insurance, liability |
| Repairs and maintenance (reparación y conservación) | Yes | Restoring to habitable condition; not improvements |
| Legal fees (abogado, procurador) | Yes | Related to tenancy |
| Property management (administración) | Yes | Agency fees |
| Utilities (paid by landlord) | Yes | If landlord bears cost |
| Amortización (depreciation) | Yes | 3% of construction cost (see below) |
| Service charges (portería, jardinería) | Yes | If landlord's obligation |
| Bad debts (saldos de dudoso cobro) | Yes | After 6 months unpaid + legal action initiated |
| Garbage tax (tasa de basuras) | Yes | Municipal waste charge |

### 2.3 Non-Deductible / Capital Expenses

**Non-Deductible / Capital Expenses**

| Expense | Treatment |
| --- | --- |
| Improvements (mejoras) | NOT deductible -- add to acquisition cost (increase cost base) |
| Enlargement / expansion | NOT deductible -- capital |
| Furniture purchase | Depreciated at 10% per year (not immediately deductible) |
| Principal repayment of mortgage | NOT deductible (only interest) |

### 2.4 Amortización (Depreciation)

- **Depreciation rate basis** — 3% per annum on the greater of: 1. Acquisition cost of construction (excluding land value), or 2. Valor catastral of construction component (from IBI receipt)
- **Land/construction split** — The recibo del IBI shows valor catastral del suelo (land) and valor catastral de la construcción (building) separately. Apply 3% to construction portion only.

Purchase price: €200,000
IBI shows: 40% land, 60% construction
Construction cost: €200,000 × 60% = €120,000
Annual depreciation: €120,000 × 3% = €3,600

### 2.5 The 60% Reduction (Reducción por arrendamiento de vivienda)

**The 60% Reduction (Reducción por arrendamiento de vivienda)**

| Condition | Reduction |
| --- | --- |
| Property rented as tenant's vivienda habitual (primary residence) | 60% of net positive rental income |
| Tourist / short-term rental | No reduction |
| Commercial / office rental | No reduction |
| Reduction base | Applied to positive net income ONLY (not losses) |

- **Ley 12/2023 (Housing Law) updated reductions** — 90% if rent reduced by 5%+ on new contract in zona tensionada; 70% if rented to young tenant (18-35) in zona tensionada, or social housing; 60% if substantial rehabilitation performed; 50% base reduction (replaces 60% for new contracts post-2024)  _(Ley 12/2023 (Housing Law), effective for new contracts from 2024)_

The traditional 60% reduction continues to apply to pre-existing contracts. For new contracts post-2024, the base reduction is 50% unless enhanced conditions are met.

### 2.6 Interest Expense Limitation

- **Interest expense limitation** — Interest on mortgage used to purchase/renovate the rental property is deductible, BUT: Interest + repair expenses CANNOT exceed rental income (they cannot generate a fiscal loss from these specific items). Excess interest/repair costs carry forward to subsequent years (5-year limit under Art. 23.1.a LIRPF)  _(Art. 23.1.a LIRPF)_

### 2.7 Non-Resident Rental Income

**Non-Resident Rental Income**

| Resident Status | Rate | Base |
| --- | --- | --- |
| Non-resident (non-EU/EEA) | 24% | Gross rental income (NO deductions allowed) |
| Non-resident (EU/EEA including Norway, Iceland) | 19% | Net income (deductions allowed, same as IRPF) |
| Filing form | Modelo 210 | Quarterly within 20 days of end of quarter |

### 2.8 Imputación de Rentas Inmobiliarias (Imputed Income)

- **Conditions for imputed income** — For properties that are: Owned by the taxpayer; NOT the taxpayer's primary residence (vivienda habitual); NOT rented out; NOT used for business
- **Imputed income formula** — Imputed income = valor catastral × 2% (or 1.1% if catastral value was revised in the last 10 years)

This is taxed at marginal rates as part of the general tax base. It applies to second homes, empty apartments, etc.

## Section 3 -- Transaction Pattern Library

### 3.1 Income Patterns

**Income Patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ALQUILER, RENTA MENSUAL, INQUILINO [name] | Rental income | Monthly rent receipt |
| IDEALISTA PAYMENTS, SPOTAHOME | Rental income | Platform rental (may be tourist) |
| AIRBNB PAYOUT, BOOKING.COM PAYOUT | Tourist rental income | No 60% reduction; different comunidad rules |
| FIANZA RETENIDA (retained deposit) | Income when retained | Assessable in year of retention |

### 3.2 Expense Patterns

**Expense Patterns**

| Pattern | Category | Treatment |
| --- | --- | --- |
| IBI, IMPUESTO BIENES INMUEBLES, AYUNTAMIENTO [city] | Property tax | Fully deductible |
| COMUNIDAD DE PROPIETARIOS, ADMINISTRADOR FINCAS | Community fees | Fully deductible |
| SEGURO HOGAR, MAPFRE, ZURICH, MUTUA | Insurance | Fully deductible |
| HIPOTECA INTERESES, [BANK] INTERESES | Mortgage interest | Deductible (subject to limit) |
| FONTANERO, ELECTRICISTA, REPARACIÓN | Repairs | Deductible (if repairs, not improvements) |
| ADMINISTRACIÓN FINCA, GESTIÓN ALQUILER | Management fees | Fully deductible |
| TASA BASURAS, RESIDUOS | Garbage tax | Fully deductible |
| NOTARÍA, ABOGADO (tenancy) | Legal fees | Deductible |

### 3.3 Capital / Non-Deductible Patterns

**Capital / Non-Deductible Patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| REFORMA, REHABILITACIÓN, AMPLIACIÓN | Capital (improvement) | Add to cost base |
| COCINA NUEVA, BAÑO NUEVO (full replacement) | Capital | Not a repair |
| HIPOTECA PRINCIPAL, AMORTIZACIÓN PRÉSTAMO | Not deductible | Principal repayment |

## Section 4 -- Computation Method

### Step 1: Gross Rental Income (Rendimiento Íntegro)

- **Gross rental income** — Total rent received/receivable for the year.

### Step 2: Deductible Expenses (Gastos Deducibles)

- **Deductible expenses** — Sum all allowable expenses including depreciation (3% of construction).

### Step 3: Net Rental Income (Rendimiento Neto)

- **Net rental income formula** — Gross income − deductible expenses.

### Step 4: Apply 60% Reduction (if applicable)

- **60% reduction application** — If vivienda habitual of tenant: Net × (1 − 60%) = reduced amount. E.g., Net income €10,000 → Reduced to €4,000 (only €4,000 taxed).

### Step 5: Report on Modelo 100

- **Report on Modelo 100** — Include in rendimientos del capital inmobiliario section. Taxed at marginal IRPF rates (general tax base, not savings base).

## Section 5 -- Tourist Rental (Vivienda de Uso Turístico)

**Tourist Rental (Vivienda de Uso Turístico)**

| Item | Detail |
| --- | --- |
| 60% reduction | NOT available for tourist rental |
| Comunidad rules | Each region has its own licensing requirements (licencia turística) |
| IVA/IGIC | No VAT if individual without additional hospitality services |
| With services (limpieza, recepción) | May be subject to IVA at 10% (actividad económica) |
| Declaration | Modelo 179 (platform reporting to AEAT) |
| Obligations | Tourist licence; municipal restrictions; Modelo 100 as rendimientos |

## Section 6 -- Edge Cases

### 6.1 Partially Rented Year

- **Partially rented year** — Expenses are apportioned between rented period and vacant period. Imputed income applies to the vacant period (if not available for rent).

### 6.2 Below-Market Rent (e.g., to family)

- **Below-market rent** — If rented below market value, AEAT may impute income at market rate. Minimum imputed income = imputed income that would apply if empty (valor catastral × 2%/1.1%).

### 6.3 Co-Ownership (Proindiviso)

- **Co-ownership** — Each co-owner reports their share of income and expenses proportional to ownership percentage.

### 6.4 Rental at a Loss

- **Rental at a loss** — Net rental losses are part of the general tax base and can offset other general income (employment, business). The 60% reduction does NOT apply to losses (only to positive net income).

### 6.5 Non-Resident with Multiple Properties

- **Non-resident with multiple properties** — Each property requires a separate Modelo 210 filing. Imputed income also requires Modelo 210 for vacant properties.

## Section 7 -- Prohibitions

- **Prohibitions** — NEVER apply the 60% reduction to tourist/short-term rental; NEVER apply the 60% reduction to a rental loss (only positive net income); NEVER allow non-EU non-residents to deduct expenses (24% on gross); NEVER depreciate the land component -- only construction value; NEVER exceed the 3% depreciation rate for the property itself; NEVER deduct mortgage principal as an expense; NEVER ignore imputación de rentas for vacant non-primary properties; NEVER present tax calculations as definitive -- always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal, gestor administrativo, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
