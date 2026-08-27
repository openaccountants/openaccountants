---
name: spain-tax-optimization
description: Use this skill whenever asked about reducing tax in Spain, tax planning, saving tax, optimizing tax, allowances, deductions the client might be missing, or any question about legal strategies to minimize income tax liability for self-employed individuals (autónomos) in Spain. Trigger on phrases like "reduce tax", "tax planning", "save tax", "optimize", "allowances", "deductions I'm missing", "pagar menos impuestos", "optimización fiscal", "ahorrar en impuestos", "deducciones IRPF", "autónomo fiscal". ALWAYS read this skill before advising on any Spanish tax optimization strategy.
version: 1.0
jurisdiction: ES
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spain Tax Optimization

## Spain Tax Optimization -- Self-Employed (Autónomo) Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Spain (Reino de España) |
| Key optimization legislation | Ley 35/2006 del IRPF (Ley del IRPF); Real Decreto 439/2007 (RIRPF); Ley 37/1992 del IVA; Ley 58/2003, General Tributaria (LGT); Real Decreto Legislativo 8/2015 (LGSS -- social security); Ley de Presupuestos Generales del Estado 2026 |
| Tax authority attitude to planning | The Agencia Estatal de Administración Tributaria (AEAT) accepts legitimate planning (economía de opción). Spain has a general anti-avoidance rule under Art. 15 LGT (conflicto en la aplicación de la norma tributaria): arrangements that are unusual or improper and whose principal purpose is to obtain a tax advantage can be disregarded. Additionally, Art. 16 LGT covers simulación (sham transactions). |
| Currency | EUR |
| Tax year | Calendar year (1 Jan -- 31 Dec) |
| Filing deadline | 30 June of the following year (Renta campaign typically April-June) |

### IRPF Rates 2026 (State Scale)

**IRPF Rates 2026 (State Scale)**

| Taxable income (EUR) | State rate | Typical combined rate (state + autonomic) |
| --- | --- | --- |
| 0 -- 12,450 | 9.5% | ~19% |
| 12,451 -- 20,200 | 12% | ~24% |
| 20,201 -- 35,200 | 15% | ~30% |
| 35,201 -- 60,000 | 18.5% | ~37% |
| 60,001 -- 300,000 | 22.5% | ~45% |
| 300,001+ | 24.5% | ~47-54% (varies by CCAA) |

Autonomous community (CCAA) rates vary. Madrid has the lowest combined rates; Cataluña, Valencia, and Extremadura among the highest.

## Section 2 -- Income Splitting & Structuring

### Autónomo vs Sociedad Limitada (SL)

**Autónomo vs Sociedad Limitada (SL) table**  _(Ley 27/2014 del Impuesto sobre Sociedades; Ley del IRPF Art. 25-26)_

| Factor | Autónomo (Persona Física) | Sociedad Limitada (SL) |
| --- | --- | --- |
| Top marginal rate | 47-54% (IRPF + CCAA) | 25% Impuesto sobre Sociedades (IS); 23% for first EUR 50,000 if turnover < EUR 1m |
| Extraction | N/A | Salary (deductible, taxed as income) + dividends (19-28% withholding) |
| When to incorporate | When net profits consistently exceed ~EUR 40,000-50,000 | Requires notarial deed, compliance costs, annual accounts |

- **Legislation** — Ley 27/2014 del Impuesto sobre Sociedades; Ley del IRPF Art. 25-26  _(Ley 27/2014 del Impuesto sobre Sociedades; Ley del IRPF Art. 25-26)_

### Régimen de Estimación Directa

**Régimen de Estimación Directa table**

| Method | Detail |
| --- | --- |
| Estimación Directa Normal (EDN) | Full accounting, actual expenses, for turnover > EUR 600,000 |
| Estimación Directa Simplificada (EDS) | Actual expenses + 5% provisión de gastos de difícil justificación (max EUR 2,000/year). For turnover ≤ EUR 600,000. |
| Estimación Objetiva (módulos) | Fixed tax based on objective indicators (square meters, employees, vehicles). Limited activities. Being phased out for many sectors. |

Most autónomos use EDS. The automatic 5% provisión (up to EUR 2,000) is often forgotten -- it applies even if you cannot justify specific expenses.

### Ley Beckham (Régimen de Impatriados)

**Ley Beckham table**  _(IRPF Art. 93)_

| Feature | Detail | Legislation |
| --- | --- | --- |
| Flat rate | 24% on Spanish-source employment income up to EUR 600,000; 47% above | IRPF Art. 93 |
| Eligibility | Must not have been Spanish tax resident in prior 5 of 10 years | IRPF Art. 93 |
| Duration | 6 years (year of arrival + 5) |  |
| Restrictions | Cannot mix with standard IRPF deductions; not available for autónomos (employment income only) |  |

## Section 3 -- Deductions Most People Miss

### Gastos Deducibles para Autónomos (IRPF Art. 28-30)

**Gastos Deducibles para Autónomos table**  _(IRPF Art. 28-30)_

| Deduction | Legislation | Notes |
| --- | --- | --- |
| Cuota de autónomos (RETA) | IRPF Art. 28; LGSS | Fully deductible social security contributions. EUR 200-530/month depending on income bracket (2026 progressive system). |
| Provisión gastos difícil justificación | IRPF Art. 30.2.4ª | 5% of rendimientos netos, max EUR 2,000/year. Automatic in EDS -- no receipts needed. |
| Suministros del hogar (home utilities) | IRPF Art. 30.2.5ª.c) | 30% of the proportional share of home costs (electricity, water, gas, internet) attributable to the workspace. Calculation: (workspace m² ÷ total m²) × 30% × annual cost. |
| Gastos de manutención (meals while traveling) | IRPF Art. 30.2.5ª.a) | EUR 26.67/day (Spain) / EUR 48.08/day (abroad) for meals. Must be on business travel, paid electronically, and at commercial establishment. |
| Seguro de salud (private health insurance) | IRPF Art. 30.2.5ª.d) | Up to EUR 500/person/year (EUR 1,500 if disabled) for autónomo + spouse + children under 25. Not a deduction but an exempt benefit reducing taxable income. |
| Vehículo (IVA deductible 50%) | Ley IVA Art. 95.3.2ª | 50% IVA on vehicle costs is deductible by default (100% if exclusively business use is proven). IRPF deduction more restrictive. |
| Formación profesional | IRPF Art. 28 | Courses, certifications, conferences related to the activity. |
| Cuotas colegiales | IRPF Art. 28 | Professional body membership fees (Colegio de Abogados, Colegio de Economistas, etc.). |
| Amortización | IRPF Art. 29 | Depreciation of business assets per the simplified table. |
| Gastos de difícil justificación | RIRPF Art. 30 | The 5% provision is effectively a "buffer" for small, hard-to-document expenses. |
| Reparaciones y conservación | IRPF Art. 28 | Repairs and maintenance on business assets. |
| Primas de seguro | IRPF Art. 28 | Professional liability, commercial premises insurance, vehicle insurance (business portion). |

## Section 4 -- Capital Allowances Optimization

**Legislation:** IRPF Art. 29; RIRPF Art. 4 + simplified depreciation table

### Simplified Depreciation Table (Estimación Directa Simplificada)

**Simplified Depreciation Table**

| Asset category | Maximum annual rate | Maximum years |
| --- | --- | --- |
| Buildings (commercial) | 3% | 68 |
| Plant, machinery, tools | 12% | 18 |
| Furniture | 10% | 20 |
| IT equipment (hardware/software) | 26% | 10 |
| Vehicles | 16% | 14 |
| Other assets | 10% | 20 |

### Libertad de Amortización (Free Depreciation)

- **Free depreciation for low-value assets** — Available for assets of reduced value: items under EUR 300 can be freely depreciated (immediately expensed) up to EUR 25,000/year total.  _(IS Art. 12.3 (for companies); IRPF applies similar principles for small businesses.)_

### Timing Strategy

Purchase IT equipment (26% rate) in January to maximize the first-year deduction (full 26%). A December purchase gives only 1/12th of the annual rate.

## Section 5 -- Loss Utilization

- **Legislation** — IRPF Art. 48-49  _(IRPF Art. 48-49)_

**Loss Utilization table**  _(IRPF Art. 48-49)_

| Relief | Detail |
| --- | --- |
| Offset against general base | Losses from economic activities (rendimientos de actividades económicas) can offset other income in the general base (employment, rental) in the same year. |
| Carry-forward | Unused losses carry forward for 4 years against future income of the same category. |
| No carry-back | Spain does not allow loss carry-back for IRPF. |
| Base del ahorro offset | Capital losses can only offset capital gains (base del ahorro). If capital losses exceed gains, up to 25% of the excess can offset positive general income. |
| Compensación between bases | Negative rendimientos del capital mobiliario can offset up to 25% of positive ganancias patrimoniales, and vice versa. |

### Strategy

In the start-up phase, maximize deductible expenses to create losses. These offset any employment or rental income in the same year, then carry forward for 4 years. Plan to use them before they expire.

## Section 6 -- Timing Strategies

**Timing Strategies table**

| Strategy | Detail |
| --- | --- |
| Defer invoicing | Under estimación directa, income is recognized on accrual basis. However, cash flow timing affects IVA obligations. For módulos, timing of invoices is irrelevant. |
| Accelerate expenses | Prepay insurance premiums, professional subscriptions, training before 31 December. |
| Plan de pensiones contributions | Maximize contributions before 31 December. Reduces base imponible general directly. |
| Ganancias/pérdidas patrimoniales timing | Realize capital losses before year-end to offset capital gains. Defer gains to next year if possible. Beware the 2-month anti-wash rule (no repurchase of same/similar securities within 2 months). |
| Retenciones management | Autónomos apply 15% IRPF withholding on invoices to professionals/companies (7% in first 3 years). Ensure correct rate to avoid overpaying during the year. |
| Matrimonial tax choice | Married couples can file jointly (declaración conjunta) or separately. Compare both: joint filing benefits when one spouse has no/low income (EUR 3,400 additional mínimo personal). |
| Módulos exit timing | If leaving módulos for estimación directa, time the switch at the start of the year. Mid-year switches can create complications. |

## Section 7 -- VAT Optimization (IVA)

- **Legislation** — Ley 37/1992 del IVA  _(Ley 37/1992 del IVA)_

**VAT Optimization table**  _(Ley 37/1992 del IVA)_

| Strategy | Detail |
| --- | --- |
| Régimen General vs Simplificado | General: quarterly returns (Modelo 303). Simplificado: available for módulos activities, fixed quota. |
| Recargo de Equivalencia | For retail traders buying from wholesalers: no IVA returns needed, wholesaler charges RE surcharge. Simplifies compliance but eliminates input IVA recovery. |
| Criterio de Caja (cash basis IVA) | Pay output IVA only when collected from clients (not when invoiced). Available if turnover ≤ EUR 2m. Must opt in. |
| IVA deducible on vehicles | 50% of IVA on vehicle purchase/lease is deductible by default. 100% if exclusive business use is proven (difficult -- requires documentation). |
| Pro rata for mixed activities | If performing both IVA-taxable and IVA-exempt activities, optimize the pro rata calculation to maximize input IVA recovery. |
| Modelo 390 (annual summary) | Review the annual summary to ensure no input IVA has been missed. |

## Section 8 -- Social Security Optimization

- **Legislation** — LGSS (Real Decreto Legislativo 8/2015); RD-Ley 13/2022 (progressive RETA system)  _(LGSS (Real Decreto Legislativo 8/2015); RD-Ley 13/2022 (progressive RETA system))_

### Progressive Cuota de Autónomos (from 2023, phased through 2025)

From 2025/2026, autónomo contributions are based on real net income brackets:

**Progressive Cuota de Autónomos table**

| Net monthly income (EUR) | Approximate monthly cuota (2025) |
| --- | --- |
| ≤ 670 | ~EUR 200 |
| 671 -- 900 | ~EUR 220 |
| 901 -- 1,166.70 | ~EUR 260 |
| 1,166.71 -- 1,300 | ~EUR 290 |
| 1,300 -- 1,500 | ~EUR 350 |
| 1,500 -- 1,700 | ~EUR 370 |
| 1,700 -- 1,850 | ~EUR 390 |
| 1,850 -- 2,030 | ~EUR 400 |
| > 4,050 | ~EUR 530 |

### Optimization Strategies

**Optimization Strategies table**

| Strategy | Detail |
| --- | --- |
| Tarifa plana (flat rate) | New autónomos: EUR 80/month for first 12 months (extendable to 24 months if income remains below minimum wage). |
| Income bracket management | The progressive system means lower reported income = lower cuota. But this reduces future pension. |
| Regularización anual | RETA contributions are regularized annually based on actual income reported in IRPF. Overpayments are refunded, underpayments are billed. |
| Cese de actividad (unemployment) | Autónomos contribute to the cese de actividad fund. This provides unemployment-like benefits for 2-12 months. Ensure it is correctly configured. |
| Pluriactividad (dual activity) | If simultaneously employed (régimen general) and autónomo (RETA), you may be entitled to a refund of excess contributions if combined bases exceed the contribution ceiling. Apply via Modelo 190. |

## Section 9 -- Investment & Retirement

### Planes de Pensiones -- IRPF Art. 51-52

**Planes de Pensiones table**  _(IRPF Art. 51-52)_

| Feature | Detail |
| --- | --- |
| Individual plan limit | EUR 1,500/year (reduces base imponible general) |
| Employer plan (plan de empleo) | Additional EUR 8,500/year from employer contributions |
| Autónomo simplified plan (PPES) | Additional EUR 4,250/year for autónomos who set up a simplified occupational plan |
| Combined autónomo limit | EUR 1,500 (individual) + EUR 4,250 (PPES) = **EUR 5,750/year** |
| Tax saving | At 37% marginal rate: EUR 5,750 × 37% = EUR 2,128/year |
| Exit taxation | Taxed as rendimientos del trabajo (employment income) at progressive rates on withdrawal |
| 2-year window rule | Contributions from > 2 years ago can be withdrawn as capital with 40% exemption (pre-2007 contributions only). |

### Inversión en Empresas de Nueva Creación -- IRPF Art. 68.1

**Inversión en Empresas de Nueva Creación table**  _(IRPF Art. 68.1)_

| Feature | Detail |
| --- | --- |
| Deducción | 50% of investment in new companies (startups) up to EUR 100,000 |
| Requirements | Company < 3 years old; participation ≤ 25%; held for 3-12 years |
| Maximum deducción | EUR 50,000/year |

### Base del Ahorro (Savings Tax)

**Base del Ahorro table**

| Gains/income (EUR) | Rate |
| --- | --- |
| 0 -- 6,000 | 19% |
| 6,001 -- 50,000 | 21% |
| 50,001 -- 200,000 | 23% |
| 200,001 -- 300,000 | 27% |
| 300,001+ | 28% |

**Strategy:** Time realization of capital gains across tax years to stay in lower brackets. Use the EUR 6,000 @ 19% band each year.

## Section 10 -- Red Lines

**Red Lines table**

| Risk | Detail |
| --- | --- |
| Conflicto en la aplicación de la norma (Art. 15 LGT) | Unusual or improper arrangements principally aimed at tax advantage can be recharacterized. No penalty, but unpaid tax + interest. |
| Simulación (Art. 16 LGT) | Sham transactions: penalty of 50-100% of avoided tax + interest. |
| Economía sumergida | Undeclared income is criminal if > EUR 120,000/year (Art. 305 Código Penal). Prison sentences of 1-5 years. |
| Factura falsa | Issuing or using false invoices: criminal under Art. 310 CP (1-5 years) and Art. 305 CP. |
| Anti-wash rule | Cannot deduct capital losses if the same or substantially similar securities are repurchased within 2 months (Ley IRPF Art. 33.5.f). |
| Tarifa plana abuse | Re-registering as a new autónomo to re-claim the tarifa plana after a short cessation period. AEAT monitors gaps < 2-3 years. |
| Vinculación (related party transactions) | Transactions between autónomo and own SL (or family SL) must be at arm's length. Art. 18 Ley IS. |
| CCAA deduction eligibility | Autonomous community deductions require actual residence in that community. Moving solely for tax benefits (particularly to Madrid) is scrutinized if not genuine. |

## Section 11 -- Annual Tax Planning Calendar

**Annual Tax Planning Calendar table**

| Month | Action |
| --- | --- |
| January | Review prior year's income and expenses. Apply for tarifa plana if new autónomo. File Modelo 303 (Q4 IVA) + Modelo 130 (Q4 IRPF pago fraccionado). |
| February | Gather facturas, bank statements, cuotas autónomos records. |
| March | File Modelo 347 (annual third-party transactions > EUR 3,005.06). Review plan de pensiones capacity. |
| April | **Renta campaign opens** (~first week). File Modelo 303 + Modelo 130 for Q1. Compare declaración conjunta vs individual if married. |
| May | Complete Renta filing. Verify AEAT borrador: add missing deductions (gastos actividad, plan pensiones, deducciones autonómicas). |
| June | **30 June** -- Renta filing deadline. File annual IVA summary (Modelo 390) if not already filed in January. |
| July | File Modelo 303 + Modelo 130 for Q2. Mid-year income review. |
| August | Plan H2 purchases: equipment, training, professional development. |
| September | Review IVA position: input IVA missed? Pro rata optimization? |
| October | File Modelo 303 + Modelo 130 for Q3. Estimate full-year income. Consider reducing pago fraccionado if income dropping. |
| November | Maximize plan de pensiones contributions (EUR 1,500 + EUR 4,250 PPES). Realize capital losses to offset gains. |
| December | Defer invoicing if income timing is beneficial. Prepay deductible expenses. Make charitable donations. Purchase assets for amortización. File Modelo 390 (annual IVA). |

## Section 12 -- Cash Impact Examples

### Example 1 -- Plan de Pensiones (Autónomo, Net Income EUR 45,000)

**Example 1 table**

| Contribution (individual + PPES) | EUR 5,750 |
| --- | --- |
| Tax saving at 37% marginal rate | **EUR 2,128/year** |

### Example 2 -- Provisión de Gastos de Difícil Justificación (EDS)

**Example 2 table**

| Net rendimientos before provisión | EUR 40,000 |
| --- | --- |
| 5% provisión (max EUR 2,000) | EUR 2,000 |
| Tax saving at 37% | **EUR 740/year** |

### Example 3 -- Suministros del Hogar (15m² office in 90m² home)

**Example 3 table**

| Annual home costs (electricity + water + gas + internet) | EUR 3,600 |
| --- | --- |
| Workspace proportion (15/90) | 16.67% |
| Deductible (30% of proportion) | EUR 3,600 × 16.67% × 30% = EUR 180 |
| Tax saving at 37% | **EUR 67/year** |

### Example 4 -- Gastos de Manutención (100 Travel Days/Year)

**Example 4 table**

| Deductible meals | 100 × EUR 26.67 = EUR 2,667 |
| --- | --- |
| Tax saving at 37% | **EUR 987/year** |

### Example 5 -- Seguro de Salud (Family of 4)

**Example 5 table**

| Premium (4 × EUR 500) | EUR 2,000 |
| --- | --- |
| Tax saving at 37% | **EUR 740/year** |

### Example 6 -- Tarifa Plana (First 12 Months)

**Example 6 table**

| Standard cuota (income ~EUR 1,300/month) | ~EUR 290/month |
| --- | --- |
| Tarifa plana | EUR 80/month |
| **Annual saving** | **EUR 2,520** |

### Example 7 -- Startup Investment (EUR 20,000 in Nueva Creación)

**Example 7 table**

| Deducción (50%) | **EUR 10,000** |
| --- | --- |
| Direct tax reduction (off cuota íntegra) | **EUR 10,000** |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
