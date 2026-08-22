---
name: es-autonomous-worker
description: Use this skill whenever asked about Spanish self-employed (autónomo) tax and social security obligations beyond IRPF computation. Trigger on phrases like "autonomo", "autónomo", "cuota de autonomos", "cuota seguridad social autonomo", "RETA", "tarifa plana", "alta autonomo", "baja autonomo", "cotizacion por ingresos reales", "obligaciones fiscales autonomo", "modelos autonomo", "Modelo 303", "Modelo 130", "Modelo 390", "Modelo 349", "calendario fiscal autonomo", "pluriactividad", "autonomo societario", "facturacion autonomo", "estimacion directa", "libro registro", "IGIC autonomo", "IPSI autonomo", "autonomo Canarias", "autonomo Ceuta Melilla", "cuanto paga un autonomo", or any question about the complete fiscal and social security picture for a self-employed worker in Spain. ALWAYS read this skill before advising on autónomo setup, ongoing obligations, or take-home pay calculations.
version: 1.0
jurisdiction: ES
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - es-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ES Autonomous Worker

## Spain Autónomo (Self-Employed Worker) Complete Obligations Skill v1.0

> **Based on work by [Nambu89 (Impuestify)](https://github.com/Nambu89/Impuestify)** and **[Pau March (larenta)](https://github.com/paumrch/larenta)**, licensed under MIT. Adapted for the OpenAccountants format.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Spain (Estado Español) |
| Subject | Trabajador Autónomo (Self-Employed Worker / Sole Trader) |
| Currency | EUR only |
| Legal framework | Ley 20/2007 (Estatuto del Trabajo Autónomo); RDL 13/2022 (cotización por ingresos reales) |
| Social Security regime | RETA (Régimen Especial de Trabajadores Autónomos) |
| Tax regime | IRPF (estimación directa simplificada by default) |
| Tax authority | AEAT (tax) + Tesorería General de la Seguridad Social (TGSS) (social security) |
| Key filing forms | Modelo 036/037 (census), Modelo 130 (quarterly IRPF), Modelo 303 (quarterly IVA), Modelo 100 (annual IRPF) |

## Section 2 -- Cuota de Autónomos 2025: Cotización por Ingresos Reales

Since January 2023, self-employed workers pay Social Security (cuota de autónomos) based on actual income (rendimientos netos). The system has 15 brackets deployed gradually until 2032.

### The 15 Contribution Brackets (Tramos) -- 2025

**The 15 Contribution Brackets (Tramos) -- 2025**

| Tramo | Net Monthly Income (EUR) | Minimum Contribution (EUR/month) |
| --- | --- | --- |
| 1 | ≤ 670 | 200 |
| 2 | 670.01 - 900 | 250 |
| 3 | 900.01 - 1,166.70 | 267 |
| 4 | 1,166.71 - 1,300 | 291 |
| 5 | 1,300.01 - 1,500 | 294 |
| 6 | 1,500.01 - 1,700 | 294 |
| 7 | 1,700.01 - 1,850 | 310 |
| 8 | 1,850.01 - 2,030 | 315 |
| 9 | 2,030.01 - 2,330 | 320 |
| 10 | 2,330.01 - 2,760 | 330 |
| 11 | 2,760.01 - 3,190 | 350 |
| 12 | 3,190.01 - 3,620 | 370 |
| 13 | 3,620.01 - 4,050 | 390 |
| 14 | 4,050.01 - 6,000 | 400 |
| 15 | > 6,000 | 530 |

- **Contribution rate** — 31.4% of chosen base de cotización (the contribution amounts above are the minimums -- workers can choose higher bases within their bracket for better future pensions)

### How to Calculate Net Monthly Income (Rendimiento Neto)

- **Net monthly income calculation** — 1. Annual gross income (ingresos brutos) 2. MINUS deductible expenses (gastos deducibles) 3. MINUS 7% generic deduction (3% for autónomos societarios) 4. DIVIDE by 12 = Monthly net income (rendimiento neto mensual) (For autónomos persona física in estimación directa)

### Key Rules

- **6 changes per year** — You can change your contribution base up to 6 times annually to match income fluctuations
- **Annual regularization** — After year-end, TGSS compares actual income vs. chosen base. Overpayments are refunded; underpayments are collected (second half of following year)
- **Autónomos societarios minimum** — EUR 1,000/month base → EUR 314/month minimum contribution

## Section 3 -- Tarifa Plana (Flat Rate for New Autónomos)

### Standard Tarifa Plana (DA 52ª LGSS, RDL 13/2022)

**Standard Tarifa Plana (DA 52ª LGSS, RDL 13/2022)**  _(DA 52ª LGSS, RDL 13/2022)_

| Period | Monthly Contribution |
| --- | --- |
| Months 1-12 | EUR 80 |
| Months 13-24 (if income < SMI) | Reduced rate (tramo-dependent) |

### Requirements

- **Not registered as autónomo previously** — Not registered as autónomo in the previous 2 years
- **No prior tarifa plana benefit** — Not previously benefited from tarifa plana in the previous 3 years
- **No outstanding debts** — No outstanding debts with Seguridad Social or Hacienda
- **Not autónomo societario** — NOT autónomo societario (company administrators excluded)
- **Must apply at registration** — Must apply at the moment of registration (alta)

### Extended Tarifa Plana (24 months at EUR 80)

- **Availability** — Available for: Workers with disability ≥ 33%; Victims of gender violence; Victims of terrorism

### Important Notes

- **Automatic request** — Request is automatic when registering (mark the box in Modelo TA.0521)
- **No retroactive request** — Cannot be requested retroactively
- **Compatible with pluriactividad** — Compatible with pluriactividad (working as both employed and self-employed)
- **After tarifa plana ends** — After tarifa plana ends, the normal bracket system applies

## Section 4 -- Complete Fiscal Calendar for Autónomos

### Quarterly Obligations

**Quarterly Obligations**

| Quarter | Period | Deadline | Models to File |
| --- | --- | --- | --- |
| Q1 | Jan-Mar | 1-20 April | 130 (IRPF) + 303 (IVA) |
| Q2 | Apr-Jun | 1-20 July | 130 + 303 |
| Q3 | Jul-Sep | 1-20 October | 130 + 303 |
| Q4 | Oct-Dec | 1-30 January | 130 + 303 |

### Annual Obligations

**Annual Obligations**

| Model | Description | Deadline |
| --- | --- | --- |
| 100 | Declaración de la Renta (IRPF annual) | April-June (campaign dates vary) |
| 390 | Annual IVA summary | 1-30 January |
| 347 | Operations with third parties > EUR 3,005.06 | February |
| 349 | Intra-EU operations (if applicable) | Monthly or quarterly |

### Additional Models (if applicable)

**Additional Models (if applicable)**

| Model | Who | When |
| --- | --- | --- |
| 111 | If you have employees (retenciones nóminas) | Quarterly |
| 115 | If you rent premises (retenciones alquileres) | Quarterly |
| 131 | Instead of 130, if in estimación objetiva (módulos) | Quarterly |
| 720 | Assets abroad > EUR 50,000 | March |

## Section 5 -- Indirect Tax by Territory

### IVA (Common Territory + Baleares)

**IVA (Common Territory + Baleares)**

| Item | Value |
| --- | --- |
| General rate | 21% |
| Reduced rate | 10% (food, transport, hotels) |
| Super-reduced rate | 4% (bread, milk, medicines, books) |
| Filed via | Modelo 303 (quarterly) + Modelo 390 (annual summary) |

### IGIC (Canarias)

**IGIC (Canarias)**

| Item | Value |
| --- | --- |
| General rate | 7% |
| Reduced | 3% |
| Zero rate | 0% (certain essential goods) |
| Incrementado | 9.5%, 15% |
| Filed via | Modelo 420 (quarterly) to Hacienda Canaria |

### IPSI (Ceuta and Melilla)

**IPSI (Ceuta and Melilla)**

| Item | Value |
| --- | --- |
| General rate (services) | 4% |
| Other rates | 0.5% - 10% depending on goods/services |
| Filed via | Local IPSI models to Ciudad Autónoma |

## Section 6 -- Net Take-Home Calculation (Sueldo Neto Autónomo)

### Monthly Calculation Formula

- **Monthly calculation formula** — Facturación bruta (without IVA) + IVA/IGIC/IPSI repercutido (charged to client) = Total factura (amount on invoice) - Retención IRPF (15% or 7% withheld by client, if applicable) = Cobro efectivo (cash received) - Cuota autónomos (Social Security) - Gastos deducibles = Neto mensual aproximado IVA/IGIC/IPSI a pagar Hacienda = repercutido - soportado (on purchases)

### Annual Calculation Formula

- **Annual calculation formula** — Facturación bruta anual - Gastos deducibles anuales - Cuota autónomos anual - 5% gastos difícil justificación (max EUR 2,000, if simplificada) = Base imponible IRPF IRPF anual = Apply progressive brackets to base imponible Neto anual = Facturación bruta - IRPF - Cuota SS - Gastos

### Worked Example: IT Freelancer, Madrid, EUR 3,000/month billing

Monthly:
  Facturación bruta:            EUR 3,000
  + IVA 21%:                    EUR 630
  = Total factura:              EUR 3,630
  - Retención IRPF 15%:        EUR 450
  = Cobro efectivo:             EUR 3,180
  - Cuota autónomos (Tramo 9): EUR 320
  - Gastos deducibles:          EUR 200
  = Neto mensual estimado:      EUR 2,660

Annual:
  Facturación bruta:            EUR 36,000
  - Gastos deducibles:          EUR 2,400
  - Cuota autónomos:            EUR 3,840
  - Gastos difícil justificación: EUR 1,488 (5% × 29,760, < 2,000)
  = Base imponible:             EUR 28,272
  IRPF estimado (escala 2025):  ~EUR 5,600
  Neto anual:                   EUR 36,000 - 5,600 - 3,840 - 2,400 = EUR 24,160
  Neto mensual real:            EUR 2,013
  % neto sobre facturación:     ~67%

**Note:** The monthly "neto" from cash flow differs from the annual real neto because retenciones are prepayments that may result in refund or additional payment at year-end.

## Section 7 -- Territorial Regime Classification

**Territorial Regime Classification**

| Fiscal Residence | IRPF Scale | Indirect Tax | SS Bonification |
| --- | --- | --- | --- |
| Common territory (15 CCAA) | State + Regional (50/50) | IVA 21% | None |
| Canarias | State + Regional | IGIC 7% | None |
| Ceuta | State + Regional, 60% deduction cuota | IPSI 4% | 50% cuota SS (certain sectors) |
| Melilla | State + Regional, 60% deduction cuota | IPSI 4% | 50% cuota SS (certain sectors) |
| País Vasco (Álava/Bizkaia/Gipuzkoa) | Foral (own scale, 23%-49%) | IVA 21% | None |
| Navarra | Foral (own scale, 13%-52.8%) | IVA 21% | None |

### Ceuta/Melilla Sectors with 50% SS Bonification

- **Eligible sectors** — Agriculture, fishing, aquaculture; Industry (except energy and water); Commerce, tourism, hospitality; Other services (excluding air transport, building construction, financial/real estate activities)

## Section 8 -- Types of Autónomo

### 8.1 Autónomo Persona Física (Standard)

- **Autónomo Persona Física** — Most common: freelancer or sole trader; Filed as individual IRPF taxpayer; Can choose estimación directa simplificada (default) or normal; Retención 15% (7% first 3 years) on professional invoices (Sección 2 IAE only)

### 8.2 Autónomo Societario

- **Autónomo Societario** — Administrators/partners with ≥33% ownership who perform management; Must register in RETA; Minimum base: EUR 1,000/month (cuota mínima EUR 314/month); Cannot access tarifa plana; Deduction for generic expenses: 3% (not 7%); Their income comes as nómina from the company (rendimientos del trabajo), NOT business income

### 8.3 Autónomo Colaborador (Family Member)

- **Autónomo Colaborador** — Spouse or family member (up to 2nd degree) working regularly in the business; Minimum base: SMI (EUR 1,000/month in 2025); Bonificación: 50% during first 18 months, 25% next 6 months; Does NOT file their own Modelo 130/303 -- works under the main autónomo's business

### 8.4 Autónomo Económicamente Dependiente (TRADE)

- **TRADE** — Derives ≥75% of income from a single client; Must formalize the relationship with a written contract; Specific protections under Estatuto del Trabajo Autónomo; Tax obligations are the same as standard autónomo

## Section 9 -- Registration Process (Alta de Autónomo)

### Steps

- **Step 1: Alta en Hacienda** — Alta en Hacienda (Modelo 036 or 037): Register for tax obligations, select IAE epígrafe, choose estimation regime
- **Step 2: Alta en RETA** — Alta en RETA (Modelo TA.0521): Register with Social Security within 60 days before starting activity (or same day)
- **Step 3: Licencia de actividad** — Licencia de actividad (if applicable): Some activities require local permits
- **Step 4: Libro registro** — Libro registro: Start maintaining income and expense records from day one

### Key Decisions at Registration

**Key Decisions at Registration**

| Decision | Options | Default |
| --- | --- | --- |
| Estimation regime | Directa simplificada / Directa normal / Objetiva (módulos) | Simplificada |
| IAE epígrafe | Section 1 (business) or Section 2 (professional) | Determines if retención applies |
| IVA regime | General / Simplified / Recargo equivalencia | General |
| Tarifa plana | Apply or not | Apply if eligible |
| Contribution base | Minimum of bracket or higher | Minimum |

## Section 10 -- Deductible Expenses for Autónomos

### Fully Deductible (with proper invoice)

**Fully Deductible (with proper invoice)**

| Expense | Notes |
| --- | --- |
| Cuota autónomos (RETA) | Monthly SS contribution |
| Office rent (local de negocio) | Fully deductible with factura |
| Professional services (gestoría, abogado) | Fully deductible |
| Software and subscriptions | Business use |
| Advertising and marketing | Fully deductible |
| Professional training | Related to activity |
| Professional insurance | Liability, etc. |
| Bank fees (business account) | Fully deductible |
| Payment processor fees (Stripe, PayPal) | Fully deductible |
| Depreciation (amortización) | Per simplified table |
| Business travel (transport) | Documented trips |
| Travel meals (dietas) | Max EUR 26.67/day domestic, EUR 48.08/day international |

### Partially Deductible (Special Rules)

**Partially Deductible (Special Rules)**

| Expense | Rule | Reference |
| --- | --- | --- |
| Home office supplies (luz, gas, agua) | (office area / total area) × 30% of supply costs | LIRPF Art. 30.2.5.b |
| Vehicle expenses | Business portion only (default: 50% IVA, IRPF needs logbook) | Art. 95 LIVA |
| Mobile phone | Business portion only (default 0% if not documented) |  |
| Meals not during travel | NOT deductible | Client entertainment excluded |
| Personal insurance | NOT deductible |  |
| IRPF payments (Modelo 130) | NOT deductible (prepayment of tax, not expense) |  |

### Gastos de Difícil Justificación (Simplificada only)

- **Gastos de difícil justificación** — 5% of rendimiento neto previo, maximum EUR 2,000/year; Automatic reduction under estimación directa simplificada; Covers expenses that are difficult to document but clearly business-related

## Section 11 -- Obligación de Declarar (Filing Obligation)

Not all autónomos are obligated to file the annual Renta if their income is very low:

## Section 11 -- Obligación de Declarar (Filing Obligation)

**Obligación de Declarar thresholds**

| Situation | Limit |
| --- | --- |
| Single payer, employment income only | EUR 22,000 |
| Multiple payers (2nd+ pays > EUR 1,500) | EUR 15,876 |
| Capital income | > EUR 1,600 |
| Real estate income | > EUR 1,000 |
| Any business/professional income | Always obligated to file |

## Section 11 -- Obligación de Declarar (Filing Obligation)

- **Always obligated to file** — Autónomos are ALWAYS obligated to file Modelo 100 regardless of income level (Art. 96 LIRPF exception for rendimientos de actividades económicas)  _(Art. 96 LIRPF)_

## Section 12 -- Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown estimation regime | Directa simplificada |
| Unknown cuota autónomos | Calculate from bracket table using 60% of billing as proxy for net income |
| Unknown tarifa plana eligibility | Not eligible (apply standard brackets) |
| Unknown if new autónomo | NOT new (15% retención, not 7%) |
| Unknown Sección IAE | Sección 2 (professional -- retención applies) |
| Unknown business-use % | 0% for mixed-use items |
| Unknown territory | Common territory with IVA 21% |
| Unknown activity start date | Do not apply tarifa plana |

## PROHIBITIONS

- **Prohibition 1** — NEVER tell someone they can avoid paying cuota de autónomos if they are actively self-employed
- **Prohibition 2** — NEVER apply tarifa plana to autónomos societarios
- **Prohibition 3** — NEVER deduct client entertainment meals from IRPF
- **Prohibition 4** — NEVER apply the 7% generic deduction to autónomos persona física (it's 7% for them, 3% for societarios -- don't mix these up)
- **Prohibition 5** — NEVER confuse retenciones (tax prepayments) with expenses -- they are NOT deductible business expenses
- **Prohibition 6** — NEVER apply IVA to an autónomo in Canarias (they use IGIC) or Ceuta/Melilla (IPSI)
- **Prohibition 7** — NEVER forget that Modelo 130 is cumulative year-to-date (not just the quarter's income)
- **Prohibition 8** — NEVER apply the EUR 80 tarifa plana beyond month 12 without verifying income < SMI
- **Prohibition 9** — NEVER present cuota estimates as exact -- actual regularization happens the following year
- **Prohibition 10** — NEVER advise on baja (deregistration) without noting that this affects future tarifa plana eligibility

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

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
