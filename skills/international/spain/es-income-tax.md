---
name: es-income-tax
description: >
  Use this skill whenever asked about Spanish personal income tax (IRPF -- Impuesto sobre la Renta de las Personas Fisicas) for self-employed individuals (autonomos). Trigger on phrases like "how much tax do I pay in Spain", "IRPF", "Modelo 100", "Modelo 130", "pago fraccionado", "estimacion directa", "retencion", "autonomo tax", "rendimientos de actividades economicas", "gastos deducibles", "amortizacion", "minimo personal", "cuota autonomica", or any question about filing or computing income tax for a self-employed or freelance client in Spain. Covers IRPF progressive rates, Modelo 100 structure, estimacion directa normal vs simplificada, deductible expenses, depreciation, quarterly payments (Modelo 130), withholding (retenciones), regional surcharges, personal and family allowances, and interaction with IVA and Social Security. ALWAYS read this skill before touching any Spanish income tax work.
version: 2.0
jurisdiction: ES
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Spain Income Tax (IRPF) -- Self-Employed (Autonomo) Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Spain (Estado Espanol) |
| Tax | IRPF (Impuesto sobre la Renta de las Personas Fisicas) |
| Currency | EUR only |
| Tax year | Calendar year (ano natural) |
| Primary legislation | Ley 35/2006 del IRPF (LIRPF) |
| Supporting legislation | Real Decreto 439/2007 (RIRPF); Ley 58/2003 (Ley General Tributaria) |
| Tax authority | Agencia Estatal de Administracion Tributaria (AEAT) |
| Filing portal | Sede Electronica AEAT (sede.agenciatributaria.gob.es) |
| Filing deadline | 30 June of the following year (Renta campaign April-June) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a qualified asesor fiscal |
| Skill version | 2.0 |

### IRPF Tax Brackets -- State Portion (Cuota Estatal) 2025 [T1]

| Taxable Income (EUR) | State Rate | Regional Rate (General) | Combined Rate |
|---|---|---|---|
| 0 -- 12,450 | 9.50% | 9.50% | 19.00% |
| 12,451 -- 20,200 | 12.00% | 12.00% | 24.00% |
| 20,201 -- 35,200 | 15.00% | 15.00% | 30.00% |
| 35,201 -- 60,000 | 18.50% | 18.50% | 37.00% |
| 60,001 -- 300,000 | 22.50% | 22.50% | 45.00% |
| 300,001+ | 24.50% | 22.50%-24.50% | 47.00%-49.00% |

**Regional rates vary by Comunidad Autonoma.** The table above shows the general (common territory) rates. Cataluna, Andalucia, Comunidad Valenciana, etc. may have different regional brackets. The state portion is fixed; only the regional portion varies.

### Savings Income Rates (Rentas del Ahorro) 2025 [T1]

| Savings Income (EUR) | Rate |
|---|---|
| 0 -- 6,000 | 19% |
| 6,001 -- 50,000 | 21% |
| 50,001 -- 200,000 | 23% |
| 200,001 -- 300,000 | 27% |
| 300,001+ | 28% |

### Key Allowances [T1]

| Item | Amount (EUR) |
|---|---|
| Minimo personal (personal minimum) | 5,550 |
| Minimo por descendientes (1st child) | 2,400 |
| Minimo por descendientes (2nd child) | 2,700 |
| Minimo por descendientes (3rd child) | 4,000 |
| Minimo por descendientes (4th+ child) | 4,500 |
| Minimo por ascendientes (65+ living with taxpayer) | 1,150 |
| Reduccion rendimientos del trabajo (employment reduction) | Up to 6,498 |
| Gastos deducibles autonomo simplificada (5% difficulty-of-justification) | 5% of net income, max EUR 2,000 |

### Quarterly Payments (Modelo 130) [T1]

| Item | Value |
|---|---|
| Rate | 20% of net profit (cumulative year-to-date minus prior payments) |
| Deadlines | 20 April, 20 July, 20 October, 30 January |
| Alternative (Modelo 131) | For estimacion objetiva (modulos) -- out of scope |

### Retenciones (Withholding on Professional Invoices) [T1]

| Scenario | Rate |
|---|---|
| Standard professional retencion | 15% |
| First 3 years of activity (new autonomo) | 7% |
| Applicability | Only professional activities (Seccion 2 IAE), NOT business/commercial (Seccion 1) |

### Conservative Defaults [T1]

| Ambiguity | Default |
|---|---|
| Unknown Comunidad Autonoma | General (common territory) rates |
| Unknown estimation regime | Estimacion directa simplificada |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown whether professional or business activity | Professional (Seccion 2) |
| Unknown retencion rate | 15% (standard) |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year, confirmation of Comunidad Autonoma of fiscal residence, and type of activity (professional vs business/commercial).

**Recommended** -- all facturas emitidas (outgoing invoices), facturas recibidas (purchase invoices), Modelo 130 filings for the year, Social Security contribution receipts.

**Ideal** -- complete libro de ingresos y gastos, asset register, prior year Modelo 100, all retenciones certificates (certificados de retenciones).

### Refusal Catalogue

**R-ES-1 -- Estimacion objetiva (modulos).** "This skill covers estimacion directa only. Estimacion objetiva uses activity-based modules, not actual income/expenses. Out of scope."

**R-ES-2 -- Non-resident (IRNR).** "Non-residents file Impuesto sobre la Renta de No Residentes. Different rules and forms. Out of scope."

**R-ES-3 -- Sociedades (corporate tax).** "Companies file Impuesto de Sociedades. This skill covers IRPF for natural persons only."

**R-ES-4 -- Comunidades forales (Navarra, Pais Vasco).** "The foral territories have their own tax systems and rates. This skill covers common territory (territorio comun) only."

**R-ES-5 -- Complex capital gains (ganancias patrimoniales).** "Real estate disposals, share sales, and other complex capital gains require specialised computation. Escalate."

---

## Section 3 -- Transaction Pattern Library

### 3.1 Income Patterns (Credits on Bank Statement)

| Pattern | Tax Line | Treatment | Notes |
|---|---|---|---|
| FACTURA EMITIDA, COBRO FACTURA, [client name] PAGO | Rendimientos de actividades economicas (ingresos) | Business income | Net of IVA if IVA-registered |
| RETENCION, RETENCION IRPF | Reduce gross by retencion amount | Withholding | 15% (or 7% first 3 years) withheld at source. Must reconcile with certificado de retenciones. |
| STRIPE PAYOUT, PAYPAL PAYOUT | Ingresos | Business income | Match to underlying invoices |
| NOMINA, SALARIO, SUELDO | Rendimientos del trabajo | NOT self-employment | Employment income -- separate category |
| INTERESES, RENDIMIENTOS CUENTA | Rentas del ahorro | NOT self-employment | Savings income -- separate base |
| DIVIDENDO | Rentas del ahorro | NOT self-employment | Savings -- separate base |
| ALQUILER RECIBIDO, RENTA COBRADA | Rendimientos de capital inmobiliario | NOT self-employment | Rental income -- separate |
| DEVOLUCION HACIENDA, DEVOLUCION AEAT | EXCLUDE | Not income | Tax refund |
| SUBVENCION, AYUDA | Check | May be taxable | Government subsidies are generally taxable |

### 3.2 Expense Patterns (Debits on Bank Statement)

| Pattern | Tax Line | Tier | Treatment |
|---|---|---|---|
| ALQUILER OFICINA, RENTA LOCAL | Arrendamientos y canones | T1 | Fully deductible if dedicated business premises |
| SUMINISTROS, LUZ, GAS, AGUA, ELECTRICIDAD | Suministros | T2 | If home office: 30% of proportional share (area-based). If business premises: fully deductible. |
| TELEFONO, MOVISTAR, VODAFONE, ORANGE | Suministros | T2 | Business portion only -- default 0% if mixed |
| INTERNET, FIBRA | Suministros | T2 | Business portion only |
| GASOLINA, COMBUSTIBLE, REPSOL, CEPSA, BP | Otros gastos (vehiculo) | T2 | Max 50% deductible for IVA. For IRPF: business portion only with logbook. |
| DIETAS, COMIDA, RESTAURANTE (business travel) | Otros gastos deducibles | T1 | Deductible if business travel: max EUR 26.67/day domestic, EUR 48.08/day international. Must be on a business trip away from usual workplace. |
| RESTAURANTE, COMIDA (client entertainment) | NOT deductible | T1 | Client entertainment: NOT deductible for IRPF |
| SEGURO AUTONOMO, MUTUALIDAD | Gastos de personal (seguridad social) | T1 | Social Security (RETA): fully deductible as business expense |
| CUOTA AUTONOMOS, SEGURIDAD SOCIAL | Gastos de personal | T1 | Monthly RETA contribution: fully deductible |
| ASESORIA, GESTORIA, ASESOR FISCAL | Servicios profesionales independientes | T1 | Fully deductible |
| ABOGADO, NOTARIO | Servicios profesionales | T1 | Deductible if business-related |
| MATERIAL OFICINA, PAPELERIA | Otros gastos | T1 | Fully deductible |
| SOFTWARE, SUSCRIPCION, LICENCIA | Otros gastos | T1 | Fully deductible if business use |
| PUBLICIDAD, MARKETING, GOOGLE ADS | Publicidad y relaciones publicas | T1 | Fully deductible |
| FORMACION, CURSO, MASTER | Otros gastos | T1 | Fully deductible if related to activity |
| SEGURO RESPONSABILIDAD, SEGURO PROFESIONAL | Primas de seguros | T1 | Fully deductible |
| SEGURO HOGAR, SEGURO COCHE (personal) | NOT deductible / T2 | T2 | Personal insurance: not deductible. Car: business portion only. |
| COMISION BANCO, COMISION TPV | Gastos financieros | T1 | Fully deductible for business account |
| STRIPE FEE, PAYPAL FEE | Gastos financieros | T1 | Transaction fees: fully deductible |
| HACIENDA, AEAT, IRPF, MODELO 130 | EXCLUDE | Not deductible | Income tax payments are not deductible expenses |
| IVA LIQUIDACION, IVA PAGO | EXCLUDE from IRPF | T1 | IVA payments are separate; net figures on IRPF if registered |
| HIPOTECA, PRESTAMO | EXCLUDE | Not deductible | Loan principal |
| INTERESES PRESTAMO (business) | Gastos financieros | T1 | Interest on business loan: deductible |

### 3.3 SaaS Subscriptions

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, SLACK, ZOOM, META | Otros gastos -- fully deductible | EU/non-EU reverse charge for IVA is separate |
| NOTION, GITHUB, FIGMA, CANVA, AWS, OPENAI | Otros gastos -- fully deductible | Non-EU reverse charge for IVA |

### 3.4 Internal Transfers and Exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| TRASPASO, TRANSFERENCIA PROPIA | EXCLUDE | Internal movement |
| PRESTAMO, AMORTIZACION CAPITAL | EXCLUDE | Loan principal |
| RETIRADA EFECTIVO, CAJERO | T2 -- ask | Default exclude |
| DONACION, DONATIVO | Deduccion en cuota (not gasto) | Donations: deduccion in tax computation, not a business expense |

---

## Section 4 -- Worked Examples

### Example 1 -- Standard Autonomo (IT Consultant)

**Input:** Gross invoiced EUR 55,000 (all with 15% retencion and 21% IVA). Expenses: office rent EUR 6,000, Social Security (RETA) EUR 4,200, accountant EUR 1,200, software EUR 800, travel EUR 2,000.

**Computation:**
- Ingresos: EUR 55,000 (net of IVA; retenciones are prepayments of IRPF, NOT a reduction in income)
- Gastos deducibles: 6,000 + 4,200 + 1,200 + 800 + 2,000 = EUR 14,200
- Rendimiento neto previo: 55,000 - 14,200 = EUR 40,800
- Estimacion directa simplificada: 5% reduccion = EUR 2,040 (max EUR 2,000)
- Rendimiento neto reducido: 40,800 - 2,000 = EUR 38,800
- Retenciones already withheld: 55,000 x 15% = EUR 8,250 (credit against final IRPF)

### Example 2 -- Home Office (Suministros)

**Input:** Autonomo works from home. Apartment 80 sqm, dedicated office 12 sqm (15%). Annual utilities: electricity EUR 1,200, gas EUR 600, water EUR 300, internet EUR 480.

**Computation:**
- Area proportion: 12/80 = 15%
- Deductible proportion of supplies: 15% x 30% = 4.5% (the 30% rule for home office supplies)
- Electricity: 1,200 x 4.5% = EUR 54
- Gas: 600 x 4.5% = EUR 27
- Water: 300 x 4.5% = EUR 13.50
- Internet: 480 x 4.5% = EUR 21.60 (but if internet is 100% business, higher proportion may apply with documentation)
- Total home office supplies deduction: EUR 116.10
- [T2] Flag: the 30% applied to the proportional area is the statutory cap for supplies since 2018 reform.

### Example 3 -- Retencion Reconciliation

**Input:** Client received EUR 8,250 in retenciones certificates from clients. Modelo 130 quarterly payments totalled EUR 4,000. Final IRPF liability is EUR 10,500.

**Computation:**
- Total prepaid: 8,250 (retenciones) + 4,000 (Modelo 130) = EUR 12,250
- Final IRPF: EUR 10,500
- Result: EUR 1,750 refund (devolucion)

### Example 4 -- Dietas (Travel Meals)

**Input:** Autonomo travels to client site in another city. Lunch EUR 35, dinner EUR 28.

**Classification:**
- Daily maximum for domestic dietas: EUR 26.67/meal (with overnight stay) or EUR 26.67 total (without overnight).
- With overnight stay: full-day allowance EUR 53.34. Both meals within limit.
- Without overnight stay: the combined EUR 63 exceeds EUR 26.67 day limit. Only EUR 26.67 deductible.
- [T2] Flag: confirm whether overnight stay applies.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Rendimientos de Actividades Economicas [T1]

**Legislation:** LIRPF Arts. 27-32

All business/professional income. Estimacion directa simplificada is default if turnover under EUR 600,000 and taxpayer has not elected normal.

### 5.2 Gastos Deducibles [T1]

**Legislation:** LIRPF Art. 28; RIRPF Arts. 28-30

Expenses must be linked to the economic activity and properly documented (factura). The "correlacion de ingresos y gastos" principle applies.

### 5.3 Amortizacion (Depreciation) [T1]

**Legislation:** LIRPF Art. 28; Simplified depreciation table

| Asset | Max Annual Rate | Max Period (years) |
|---|---|---|
| Buildings | 3% | 68 |
| Plant and machinery | 12% | 18 |
| Tools and utensils | 30% | 8 |
| Furniture | 10% | 20 |
| Computer hardware | 26% | 10 |
| Computer software | 33% | 6 |
| Motor vehicles | 16% | 14 |
| Transport elements | 10% | 20 |

Under estimacion directa simplificada, use the simplified table (tabla simplificada). Under normal, use the full official table.

### 5.4 Reduccion por Estimacion Directa Simplificada [T1]

5% of rendimiento neto previo, capped at EUR 2,000/year. Covers "gastos de dificil justificacion" (difficult-to-justify expenses). Applied automatically under simplificada regime.

### 5.5 Modelo 130 Computation [T1]

Each quarter: 20% x (cumulative net income year-to-date) - prior Modelo 130 payments - retenciones received year-to-date. If result is negative, no payment due (cannot generate refund via Modelo 130 -- refund comes through Modelo 100).

### 5.6 Filing Deadlines [T1]

| Filing | Deadline |
|---|---|
| Modelo 130 Q1 | 1-20 April |
| Modelo 130 Q2 | 1-20 July |
| Modelo 130 Q3 | 1-20 October |
| Modelo 130 Q4 | 1-30 January |
| Modelo 100 (annual IRPF) | April-June (exact dates published by AEAT each year) |
| Modelo 303 (IVA) | Same quarterly deadlines as Modelo 130 |

### 5.7 Penalties [T1]

| Offence | Penalty |
|---|---|
| Late filing without AEAT request | 1% surcharge per month late (up to 12 months), then 15% + interest |
| Late filing after AEAT request | 50%-150% of unpaid tax (depending on severity) |
| Late payment | 5% (first month), 10% (3 months), 15% (6 months), 20% (12+ months) + interest |
| Interest rate (interes de demora) | ~3.75% annually (varies by year) |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office (Suministros) [T2]

Since 2018 reform: deductible proportion = (office area / total area) x 30% of supply costs (electricity, gas, water, internet). The 30% factor is the statutory cap -- no negotiation.

**Flag for reviewer:** Confirm area measurements and that workspace is genuinely dedicated.

### 6.2 Vehicle Expenses [T2]

For IRPF: business-use proportion only, supported by records. For IVA: maximum 50% input tax recovery on vehicle costs (presumption is 50% private use). If 100% business use can be proven, 100% for both IRPF and IVA.

**Flag for reviewer:** Confirm business-use percentage and documentation.

### 6.3 Estimacion Directa Normal vs Simplificada [T2]

| Feature | Simplificada | Normal |
|---|---|---|
| Turnover limit | Under EUR 600,000 | No limit |
| 5% gastos dificil justificacion | YES (max EUR 2,000) | NO |
| Depreciation table | Simplified | Full official |
| Provisiones deducibles | NO | YES |
| Complexity | Lower | Higher |

Most small autonomos benefit from simplificada. Flag for reviewer if turnover approaches EUR 600,000 or if provisions are material.

### 6.4 Minimo Personal y Familiar [T2]

Personal and family minimums reduce the cuota integra, not the base imponible. They create a zero-rate band effect. Flag for reviewer to confirm family situation and applicable minimums.

---

## Section 7 -- Excel Working Paper Template

```
IRPF WORKING PAPER -- Tax Year 2025

A. INGRESOS (INCOME)
  A1. Rendimientos actividades economicas          ___________
  A2. Other business income                        ___________
  A3. Total ingresos                               ___________

B. GASTOS DEDUCIBLES (EXPENSES)
  B1. Consumos de explotacion                      ___________
  B2. Sueldos y salarios                           ___________
  B3. Seguridad Social (RETA)                      ___________
  B4. Otros gastos de personal                     ___________
  B5. Arrendamientos y canones                     ___________
  B6. Suministros (utilities, home office)         ___________
  B7. Servicios profesionales                      ___________
  B8. Primas de seguros                            ___________
  B9. Gastos financieros                           ___________
  B10. Amortizaciones                              ___________
  B11. Publicidad                                  ___________
  B12. Otros gastos deducibles                     ___________
  B13. Total gastos                                ___________

C. RENDIMIENTO NETO PREVIO (A3 - B13)             ___________
D. REDUCCION 5% (max EUR 2,000)                   ___________
E. RENDIMIENTO NETO REDUCIDO (C - D)              ___________

F. PREPAYMENTS
  F1. Retenciones                                  ___________
  F2. Modelo 130 payments                          ___________
  F3. Total prepaid                                ___________

REVIEWER FLAGS:
  [ ] Comunidad autonoma confirmed?
  [ ] Estimation regime confirmed?
  [ ] Home office area ratio verified?
  [ ] Vehicle business use documented?
  [ ] Retenciones certificates reconciled?
```

---

## Section 8 -- Bank Statement Reading Guide

### Spanish Bank Statement Formats

| Bank | Format | Key Fields |
|---|---|---|
| CaixaBank, BBVA, Santander | CSV, PDF | Fecha, Concepto, Importe, Saldo |
| Sabadell, Bankinter | CSV, PDF | Fecha Valor, Descripcion, Cargo/Abono |
| N26, Revolut | CSV | Date, Counterparty, Amount |
| ING Direct | CSV | Fecha, Movimiento, Importe |

### Key Spanish Banking Terms

| Spanish Term | English | Classification Hint |
|---|---|---|
| Ingreso | Credit (incoming) | Potential income |
| Cargo | Debit (outgoing) | Potential expense |
| Transferencia | Bank transfer | Check direction |
| Recibo / Domiciliacion | Direct debit | Regular expense |
| Bizum | Mobile payment | Could be income or expense |
| Reintegro | Cash withdrawal | Ask what it was for |
| Comisiones | Bank charges | Gastos financieros |
| Nomina | Salary payment | Employment income |

---

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- SPAIN IRPF
1. Comunidad autonoma of fiscal residence?
2. Type of activity: professional (Seccion 2 IAE) or business (Seccion 1)?
3. Estimation regime: directa simplificada or normal?
4. Are you in your first 3 years of activity? (affects retencion rate)
5. Home office: do you have a dedicated workspace? Area ratio?
6. Vehicle: what percentage is business use?
7. Do you have all certificados de retenciones from clients?
8. Marital status and dependents?
9. RETA contribution amount per month?
10. Prior year Modelo 100 available?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| Self-employment income | LIRPF Arts. 27-32 |
| Deductible expenses | LIRPF Art. 28; RIRPF Arts. 28-30 |
| Depreciation | LIRPF Art. 28; Simplified table |
| Retenciones | RIRPF Arts. 95, 101 |
| Modelo 130 | RIRPF Art. 110 |
| Personal/family minimums | LIRPF Arts. 56-61 |
| Tax brackets | LIRPF Art. 63 (state); autonomic laws (regional) |
| Savings income | LIRPF Art. 66 |
| Home office supplies | LIRPF Art. 30.2.5.b (as amended 2018) |
| Filing/penalties | Ley 58/2003 (LGT) |

---

## PROHIBITIONS

- NEVER compute IRPF without knowing the Comunidad Autonoma (affects regional rates)
- NEVER deduct client entertainment expenses
- NEVER deduct IRPF payments (Modelo 130, retenciones) as business expenses -- they are prepayments of tax
- NEVER apply estimacion objetiva rules to a directa taxpayer
- NEVER deduct home office supplies beyond the (area % x 30%) formula
- NEVER allow vehicle expenses at 100% without documented proof of exclusive business use
- NEVER forget the 5% reduccion under simplificada (it is automatic, max EUR 2,000)
- NEVER confuse retenciones (withholding) with a reduction in income -- gross income is the full invoice amount before retencion
- NEVER apply foral territory rates to common territory taxpayers
- NEVER present tax calculations as definitive -- always label as estimated

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
