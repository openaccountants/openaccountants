---
name: es-corporate-tax
description: Use this skill whenever asked about Spanish corporate income tax (Impuesto sobre Sociedades, IS), Modelo 200, Modelo 202 (pagos fraccionados), corporate tax rates in Spain, SL tax obligations, company formation tax, deducciones empresariales, bases imponibles negativas (BINs), reserva de capitalizacion, reserva de nivelacion, or foral corporate tax. Trigger on phrases like "Impuesto de Sociedades", "Modelo 200", "Modelo 202", "IS Spain", "corporate tax Spain", "tipo gravamen sociedades", "SL taxes", "nueva creacion", "empresa reducida dimension", "microempresa fiscal", "BINs", "compensacion perdidas sociedad", "pago fraccionado empresa", "ZEC Canarias", "bonificacion Ceuta Melilla sociedades", "I+D deduccion sociedades", "donativos sociedad", "resultado contable", or any question about computing or filing corporate income tax in Spain. ALWAYS read this skill before touching any Spanish corporate tax work.
version: 1.0
jurisdiction: ES
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ES Corporate Tax

## Spain Corporate Income Tax (Impuesto sobre Sociedades) Skill v1.0

> **Based on work by [Nambu89 (Impuestify)](https://github.com/Nambu89/Impuestify)** and **[Pau March (larenta)](https://github.com/paumrch/larenta)**, licensed under MIT. Adapted for the OpenAccountants format.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Spain (Estado Español) |
| Tax | Impuesto sobre Sociedades (IS) |
| Currency | EUR only |
| Fiscal year | Generally calendar year (can differ) |
| Primary legislation | Ley 27/2014 (LIS); Ley 7/2024 (reform) |
| Supporting legislation | RDL 4/2024 (microempresa); Art. 25-26 LIS (reserves/BINs) |
| Tax authority | AEAT (common territory); Haciendas Forales (Basque/Navarra) |
| Filing form | Modelo 200 (annual) |
| Quarterly payments | Modelo 202 (pagos fraccionados) |
| Filing deadline | 25 days after 6 months from fiscal year-end (July 25 for calendar year) |
| Modelo 202 deadlines | 1-20 April, 1-20 October, 1-20 December |

## Section 2 -- Tax Rates (Tipos de Gravamen) 2025

### Common Territory (Territorio Común) -- Ley 7/2024

**Common Territory Rates**  _(Ley 7/2024)_

| Entity Type | INCN (Facturación) | Rate | Notes |
| --- | --- | --- | --- |
| Microempresa | < EUR 1,000,000 | 2025: 21% (first EUR 50,000) + 22% (rest); 2026: 19% + 21%; 2027 onwards: 17% + 20% | Ley 7/2024 Disp. Final 8ª / LIS DT 44ª |
| ERD (Empresa Reducida Dimensión) | EUR 1M - 10M | 24% | Transitional: drops 1pp/year to 20% by 2029 |
| General | ≥ EUR 10,000,000 | 25% | Standard rate |
| Nueva creación | Any (first 2 years with BI > 0) | 15% | First 2 fiscal years with positive base imponible |

### ERD Transitional Calendar (Ley 7/2024)

**ERD Transitional Calendar**  _(Ley 7/2024)_

| Fiscal Year | ERD Rate |
| --- | --- |
| 2025 | 24% |
| 2026 | 23% |
| 2027 | 22% |
| 2028 | 21% |
| 2029+ | 20% |

### Foral Territories

**Foral Territories Rates**

| Territory | General Rate | Microempresa | Nueva Creación |
| --- | --- | --- | --- |
| Álava (NF 37/2013) | 24% | 20%/24% (EUR 50k tramo) | 19%/24% |
| Bizkaia (NF 11/2013) | 24% | 20%/24% (EUR 50k tramo) | 19%/24% |
| Gipuzkoa (NF 1/2025) | 19% | 15%/17% (EUR 50k tramo) | 15%/19% |
| Navarra (LF 26/2016) | 28% | 23%/28% (EUR 50k tramo) | 15%/28% |

### Special Regimes

**Special Regimes Rates**

| Regime | Rate | Applicable |
| --- | --- | --- |
| ZEC Canarias | 4% (up to employment-based ceiling) | Entities in Zona Especial Canaria |
| Ceuta/Melilla | 25% with 50% bonificación on qualifying income | Income generated in Ceuta/Melilla |
| Cooperativas fiscalmente protegidas | 20% | Ley 20/1990 |
| Cooperativas especialmente protegidas | 20% + 50% bonificación cuota | Art. 34.2 Ley 20/1990 |

## Section 3 -- Liquidation Pipeline (Modelo 200)

The IS computation follows this pipeline:

```
1. Resultado contable (accounting profit)
   + Ajustes positivos (non-deductible expenses, amortization differences)
   - Ajustes negativos (exempt income, timing differences)
   - Reserva de capitalización (Art. 25 LIS)
   = Base imponible previa
   - Reserva de nivelación (Art. 105 LIS, ERD only)
   - Compensación BINs (Art. 26 LIS)
   - RIC Canarias (if applicable)
   = Base imponible (floor: EUR 0)
   × Tipo de gravamen (rate table above)
   = Cuota íntegra
   - Deducciones (I+D, IT, donativos, empleo, cine...)
   - Bonificaciones (Ceuta/Melilla, cooperativas)
   = Cuota líquida (with tributación mínima floor if applicable)
   - Retenciones e ingresos a cuenta
   - Pagos fraccionados (Modelo 202)
   = Resultado liquidación (a ingresar / a devolver)
```

## Section 4 -- Key Computations

### 4.1 Reserva de Capitalización (Art. 25 LIS)

**Reserva de Capitalización table**  _(Art. 25 LIS)_

| Fiscal Year | Reduction % | Limit (% of base previa) |
| --- | --- | --- |
| Pre-2025 | 10% of equity increase | 10% |
| 2025 (Ley 7/2024) | 20% base (up to 30% with workforce growth) | 20% |

- **2025 scale by workforce growth** — 0% workforce increase: 20% reduction; 2%+ workforce increase: 23% reduction; 5%+ workforce increase: 26.5% reduction; 8%+ workforce increase: 30% reduction  _(Art. 25 LIS)_

### 4.2 Compensación de Bases Imponibles Negativas (BINs) -- Art. 26 LIS

**BIN Compensation Limit table**  _(Art. 26 LIS)_

| INCN (Annual Revenue) | BIN Compensation Limit |
| --- | --- |
| < EUR 20M | 100% (with EUR 1M free floor) |
| EUR 20M - 60M | 70% of base imponible previa |
| ≥ EUR 60M | 50% of base imponible previa |

- **BINs expiry** — BINs never expire (no time limit since 2015 reform).  _(Art. 26 LIS)_

### 4.3 Reserva de Nivelación (Art. 105 LIS) -- ERD Only

- **Reserva de Nivelación** — Only for companies with INCN < EUR 10M: Reduces base imponible by up to 10% (max EUR 1,000,000); must be added back within 5 years if not offset by future losses; effectively allows 'advance' loss compensation.  _(Art. 105 LIS)_

### 4.4 Deducciones en Cuota

**Deducciones en Cuota table**

| Deduction | Rate | Limit (% of cuota) | Reference |
| --- | --- | --- | --- |
| I+D (Investigación y Desarrollo) | 25% of expenditure | 25% of cuota íntegra | Art. 35.1 LIS |
| I+D (exceso sobre media 2 años) | 42% of excess | Included in 25% limit | Art. 35.1.b LIS |
| I+D personal investigador | +17% of researcher costs | Included | Art. 35.1.b LIS |
| I+D inmovilizado afecto | +8% of dedicated assets | Included | Art. 35.1.b LIS |
| IT (Innovación Tecnológica) | 12% of expenditure | 25% of cuota íntegra | Art. 35.2 LIS |
| Donativos mecenazgo | 40% (sociedades) | 10% of base imponible | Art. 20 Ley 49/2002 |
| Empleo discapacitados 33-65% | EUR 9,000/employee | No limit | Art. 38 LIS |
| Empleo discapacitados ≥65% | EUR 12,000/employee | No limit | Art. 38 LIS |
| Producción cinematográfica española | 30%/25% (first EUR 1.5M/rest) | EUR 20M | Art. 36.1 LIS |
| Producción cinematográfica extranjera | 30% | EUR 20M (EUR 40M CSI) | Art. 36.2 LIS |

### 4.5 Bonificación Ceuta y Melilla (Art. 33.6 LIS)

- **Bonificación Ceuta y Melilla** — 50% bonificación on the cuota íntegra proportional to income generated in Ceuta/Melilla. Proportion = rentas Ceuta-Melilla / resultado contable total. Combined with 25% rate = effective ~12.5% on Ceuta/Melilla income.  _(Art. 33.6 LIS)_

### 4.6 Tributación Mínima (Art. 30 bis LIS)

**Tributación Mínima table**  _(Art. 30 bis LIS)_

| Situation | Minimum Rate (on base imponible) |
| --- | --- |
| General | 15% |
| Nueva creación (first 2 years BI+) | 10% |
| Banking/hydrocarbon entities | 18% |

- **Applicability and floor mechanism** — Applies to entities with INCN ≥ EUR 20M or in consolidated group. If cuota líquida (after deductions) < minimum, it is raised to the minimum.  _(Art. 30 bis LIS)_

## Section 5 -- Modelo 202: Pagos Fraccionados

### Two Modalities

**Two Modalities table**

| Modality | Calculation | When Used |
| --- | --- | --- |
| Art. 40.2 | 18% × (cuota íntegra - deducciones - bonificaciones - retenciones) del último ejercicio | Default for most companies |
| Art. 40.3 | 17% × base imponible del período (24% if INCN > EUR 10M) | Mandatory if INCN > EUR 6M; optional otherwise |

### Calendar

**Calendar table**

| Period | Deadline |
| --- | --- |
| 1P (Jan-Mar) | 1-20 April |
| 2P (Jan-Sep) | 1-20 October |
| 3P (Jan-Nov) | 1-20 December |

### Pago Fraccionado Mínimo (DA 14ª LIS)

- **Pago Fraccionado Mínimo** — For entities with INCN ≥ EUR 10M in modality Art. 40.3: Minimum payment: 23% of (resultado contable positivo + ajustes positivos) for the period. Banking/hydrocarbon: 25%. If calculated payment < minimum, minimum applies.  _(DA 14ª LIS)_

## Section 6 -- Non-Deductible Expenses (Gastos No Deducibles)

**Non-Deductible Expenses table**

| Expense | Art. LIS | Treatment |
| --- | --- | --- |
| Resultado contable del propio IS | Art. 15.b | Ajuste positivo |
| Multas y sanciones | Art. 15.c | Never deductible |
| Donativos y liberalidades | Art. 15.e | Generally not deductible (exceptions for promotion) |
| Retribución fondos propios | Art. 15.a | Dividends are not expense |
| Pérdidas por deterioro de participaciones | Art. 15.k | Not deductible (since 2013) |
| Gastos financieros > 30% EBITDA or EUR 1M | Art. 16 | Excess is non-deductible (carry forward) |
| Atenciones a clientes > EUR 1/1000 INCN | Art. 15.e | Excess is non-deductible, max EUR 1% of INCN |

## Section 7 -- ZEC Canarias (Zona Especial Canaria)

**ZEC Canarias table**  _(Art. 43 Ley 19/1994)_

| Feature | Value |
| --- | --- |
| Rate | 4% on base imponible up to ceiling |
| Ceiling by employees | 5 employees: EUR 1.8M; 6-10: EUR 2.7M; each +5: +EUR 1.8M |
| Minimum employees | 5 (3 in remote areas) |
| Excess above ceiling | 25% (general rate) |
| Eligible activities | Industrial, commercial, services (with exclusions) |
| Combining with RIC | Yes -- RIC further reduces base imponible |

## Section 8 -- Worked Example: Standard SL

**Input:** SL Consultora Digital, Madrid. Calendar year 2025. INCN EUR 500,000. Resultado contable EUR 80,000. Gastos no deducibles EUR 3,000. Incremento fondos propios EUR 20,000. BINs pendientes EUR 15,000. No I+D. 1 employee with 33% disability.

**Computation:**

```
1. Resultado contable:                        EUR 80,000
2. + Ajustes positivos (gastos no deducibles): EUR 3,000
3. - Ajustes negativos:                        EUR 0
4. - Reserva capitalización (20% × 20,000):   EUR 4,000
   = Base imponible previa:                    EUR 79,000
5. - Compensación BINs (100%, free floor 1M):  EUR 15,000
   = Base imponible:                           EUR 64,000
6. Tipo gravamen: Microempresa (INCN < 1M)
   - First EUR 50,000 × 17% =                 EUR 8,500
   - Remaining EUR 14,000 × 20% =             EUR 2,800
   = Cuota íntegra:                            EUR 11,300
7. - Deducción empleo discapacidad (1 × 9,000): EUR 9,000
   = Cuota líquida:                            EUR 2,300
8. - Retenciones:                              EUR 0
   - Pagos fraccionados:                       EUR 0
   = Resultado liquidación:                    EUR 2,300 (a ingresar)

Tipo efectivo: 2,300 / 80,000 = 2.88%
```

## Section 9 -- Filing Obligations

**Filing Obligations table**

| Modelo | Who Must File | Deadline |
| --- | --- | --- |
| 200 | All entities subject to IS | 25 July (calendar year) |
| 202 | Entities with cuota líquida > 0 in prior year OR INCN > EUR 6M | April/October/December |
| 220 | Consolidated groups | 25 July |
| 232 | Related-party transactions > EUR 250K | November |

### Exempt from filing Modelo 200:

- Entities fully exempt (Art. 9.1 LIS): State, CCAA, local entities
- Partially exempt entities with income exclusively from exempt sources, no withholdings, and no non-exempt income

## Section 10 -- Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown territory | Common territory (Madrid) |
| Unknown INCN | General rate (25%) |
| Unknown entity type | SL (standard) |
| Unknown fiscal year | 2025 |
| Unknown BINs | EUR 0 (no compensation) |
| Amortización fiscal unknown | Same as contable (no adjustment) |
| Unknown if nueva creación | NOT nueva creación (higher rate) |
| ERD vs general unknown | General (higher rate) |

## PROHIBITIONS

- NEVER apply microempresa rates to entities with INCN ≥ EUR 1,000,000
- NEVER apply nueva creación rate beyond the first 2 fiscal years with positive base imponible
- NEVER compensate BINs beyond the percentage limit for the entity's INCN bracket
- NEVER exceed the 25% cuota íntegra limit for I+D/IT/donations combined
- NEVER forget tributación mínima for entities with INCN ≥ EUR 20M or consolidated groups
- NEVER apply ZEC 4% rate without verifying the employment ceiling
- NEVER deduct multas, sanciones, or retribución de fondos propios
- NEVER apply the Ley 7/2024 microempresa rates (17%/20%) to fiscal years before 2025
- NEVER apply common territory IS rates to entities fiscally domiciled in foral territories
- NEVER confuse IRPF (personal) with IS (corporate) -- completely different regimes

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
