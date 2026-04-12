---
name: co-income-tax
description: >
  Use this skill whenever asked about Colombian income tax for self-employed individuals (trabajadores independientes / personas naturales). Trigger on phrases like "declaración de renta", "renta personas naturales", "Formulario 210", "cédula general", "UVT", "retención en la fuente", "renta presuntiva", "DIAN", "NIT Colombia", "deducciones Colombia", "rentas exentas", "income tax Colombia", or any question about filing or computing income tax for a self-employed or independent worker in Colombia. This skill covers cédula general progressive rates (0-39%), UVT-based thresholds, the 40%/5,040 UVT cap on exemptions and deductions, renta presuntiva, retención en la fuente, social security for independents, and DIAN filing. ALWAYS read this skill before touching any Colombian income tax work.
version: 2.0
---

# Colombian Income Tax — Trabajador Independiente / Persona Natural (Renta) v2.0

## Section 1 — Quick Reference

### UVT (Unidad de Valor Tributario)

| Year | UVT Value (COP) |
|---|---|
| 2024 | COP 47,065 |
| 2025 | COP 49,799 |

All thresholds, brackets, and limits are expressed in UVT. For income earned in 2025 (declared in 2026): use UVT 2025.

### Progressive Tax Table — Cédula General (ET art. 241)

| Taxable Income (UVT) | Rate | Computation |
|---|---|---|
| 0 -- 1,090 | 0% | 0 |
| >1,090 -- 1,700 | 19% | (Base - 1,090) x 19% |
| >1,700 -- 4,100 | 28% | (Base - 1,700) x 28% + 115.9 UVT |
| >4,100 -- 8,670 | 33% | (Base - 4,100) x 33% + 788 UVT |
| >8,670 -- 18,970 | 35% | (Base - 8,670) x 35% + 2,296.1 UVT |
| >18,970 -- 31,000 | 37% | (Base - 18,970) x 37% + 5,901.1 UVT |
| >31,000 | 39% | (Base - 31,000) x 39% + 10,352.2 UVT |

Non-residents: flat 35% on Colombia-source income. No deductions.

### Filing Thresholds (2025 for 2024 income, UVT 2024 = COP 47,065)

A natural person must file if ANY of these apply:

| Condition | Threshold |
|---|---|
| Gross income | >= 1,400 UVT (COP 65,891,000) |
| Gross patrimonio (assets) | >= 4,500 UVT (COP 211,793,000) |
| Credit card purchases | >= 1,400 UVT |
| Total purchases/consumption | >= 1,400 UVT |
| Bank account deposits | >= 1,400 UVT |

### Computation Structure

| Step | Description |
|---|---|
| A | Ingresos brutos (gross income) |
| B | Less: Ingresos no constitutivos de renta (e.g., mandatory pension contributions) |
| C | Ingresos netos (A minus B) |
| D | Less: Costos y gastos procedentes (allowable costs/expenses) |
| E | Renta líquida (C minus D) |
| F | Less: Rentas exentas (25% general, capped at 2,880 UVT/year + AFC/FVP) |
| G | Less: Deducciones (dependientes, interest, health, GMF) |
| H | Total F + G capped at 40% of C or 5,040 UVT, whichever is lower |
| I | Renta líquida gravable (E minus capped F+G) |
| J | Compare with renta presuntiva (0% for 2023+) |
| K | Apply art. 241 progressive table |
| L | Less: Retención en la fuente |
| M | Less: Anticipos paid |
| N | Tax due / (refund) |

### Rentas Exentas and Deducciones

| Item | Limit |
|---|---|
| 25% general worker exemption | 2,880 UVT/year (240 UVT/month) |
| Voluntary pension (AFC, FVP) | 30% of gross or 3,800 UVT/year |
| Dependientes | 10% of gross, max 384 UVT/year |
| Mortgage interest | 1,200 UVT/year |
| Medicina prepagada | 192 UVT/year |
| GMF (4x1000, 50%) | 50% of GMF paid |

**CRITICAL: Total rentas exentas + deducciones cannot exceed 40% of ingresos netos OR 5,040 UVT, whichever is lower.**

### Social Security for Independent Workers

| Contribution | Rate | Base |
|---|---|---|
| Pensión | 16% | IBC = 40% of gross monthly income |
| Salud | 12.5% | IBC = 40% of gross monthly income |
| ARL | 0.522% minimum | Risk-based |

IBC cannot be below 1 SMLMV or above 25 SMLMV. Pension contributions are ingresos no constitutivos de renta.

### Conservative Defaults

| Situation | Default Assumption |
|---|---|
| Residency unknown | STOP — non-residents pay flat 35% |
| UVT year unclear | Use UVT for the income year (2025 = COP 49,799) |
| Cost/expense without factura electrónica | Reject — DIAN requires electronic invoice |
| 40% cap not checked | Always check — most common error |
| Renta presuntiva rate uncertain | 0% for 2023+ (verify for future reform) |
| Retención certificates missing | Do NOT credit without certificates |
| IBC below SMLMV | Use SMLMV as minimum base |

### Red Flag Thresholds

| Flag | Threshold |
|---|---|
| Total exemptions + deductions > 40% | Must cap — verify computation |
| No retención certificates from clients | Cannot credit without certificates |
| IBC below SMLMV | Verify — minimum base applies |
| Single client > 80% of income | Employment requalification risk |
| No PILA payments | Verify social security compliance |

---

## Section 2 — Required Inputs + Refusal Catalogue

### Required Inputs

1. **Residency status** — resident (183+ days) vs non-resident
2. **Type of income** — cédula general (work, capital, non-labour) vs pension vs dividends
3. **Gross annual income** — total ingresos brutos
4. **Costs and expenses** — documented with factura electrónica
5. **Retención en la fuente certificates** — from each payer
6. **Dependants** — qualifying children, spouse, parents
7. **Social security contributions (PILA)** — pensión, salud, ARL
8. **NIT / cédula number** — for filing schedule
9. **Patrimonio bruto** — for filing threshold analysis
10. **Bank statements** — 12 months
11. **Prior-year return** — for anticipo verification

### Refusal Catalogue

| Code | Situation | Action |
|---|---|---|
| R-CO-1 | Non-resident | Stop — flat 35% applies; this skill covers residents only |
| R-CO-2 | Residency unknown | Stop — determines entire tax treatment |
| R-CO-3 | Retención certificates missing for claimed credit | Do not credit without certificates |
| R-CO-4 | Expense without factura electrónica | Reject — DIAN mandatory requirement |
| R-CO-5 | 40% cap exceeded without reduction | Error — must reduce exemptions + deductions to cap |
| R-CO-6 | Transfer pricing or CFC situation | Escalate — outside scope |

---

## Section 3 — Transaction Pattern Library

### 3.1 Income Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| I-01 | `TRANSFERENCIA DE [client]` / `ABONO ACH [client]` | Gross income — cédula general | Standard ACH transfer from client |
| I-02 | `NEQUI RECIBIDO [client]` / `NEQUI COBRO` | Gross income — cédula general | Nequi (Colombian digital wallet) receipt |
| I-03 | `DAVIPLATA RECIBIDO [client]` | Gross income — cédula general | Daviplata receipt |
| I-04 | `PSE RECIBIDO [client]` | Gross income — cédula general | PSE (payment button) collection |
| I-05 | `MERCADOPAGO RETIRO` / `MERCADOPAGO DEPOSITO` | Gross income — gross-up | Mercado Pago settlement |
| I-06 | `STRIPE PAYOUT` / `STRIPE PAYMENTS` | Gross income — gross-up or foreign | Stripe payout; classify by payer country |
| I-07 | `PAYPAL RETIRO` | Gross income — foreign source if from abroad | PayPal; flag for FX conversion |
| I-08 | `RAPPI PAY COBRO` | Gross income — cédula general | Rappi Pay collection |
| I-09 | `DEVOLUCIÓN DIAN` / `SALDO A FAVOR DIAN` | NOT income — tax refund | Refund of overpaid tax |
| I-10 | `INTERESES CDT` / `RENDIMIENTO FONDO` | Capital income — cédula general | Interest/fund returns |
| I-11 | `ARRIENDO COBRADO` / `CANON ARRENDAMIENTO` | Non-labour income — cédula general | Rental income |
| I-12 | `DIVIDENDOS [company]` | Dividend income — separate cédula | Different tax treatment |

### 3.2 Expense Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| E-01 | `ARRIENDO OFICINA` / `CANON ARRIENDO COMERCIAL` | Rent — deductible (costo/gasto) | Require factura electrónica |
| E-02 | `EPM` / `CODENSA` / `ELECTRICARIBE` / `CELSIA` | Electricity — deductible (business proportion) | Require factura |
| E-03 | `GAS NATURAL` / `VANTI` | Gas — deductible (business proportion) | Require factura |
| E-04 | `CLARO COLOMBIA` / `MOVISTAR COLOMBIA` / `TIGO` / `WOM` | Phone/internet — deductible (business %) | Require factura |
| E-05 | `ETB` / `UNE` | Internet/telecom — deductible (business %) | Require factura |
| E-06 | `ADOBE` / `MICROSOFT 365` / `GOOGLE WORKSPACE` | Software — deductible | Professional tools |
| E-07 | `CONTADOR` / `FIRMA CONTABLE` / `HONORARIOS CPC` | Accounting fees — deductible | Require factura |
| E-08 | `AVIANCA` / `LATAM` / `VIVA AIR` / `WINGO` | Air travel — deductible (business purpose) | Document purpose; require factura |
| E-09 | `HOTEL` / `BOOKING.COM` / `AIRBNB` | Accommodation — deductible (business travel) | Require factura |
| E-10 | `PILA PENSIÓN` / `PORVENIR` / `PROTECCIÓN` / `COLPENSIONES` | Pension contribution — ingreso no constitutivo | Reduces ingresos netos before tax |
| E-11 | `PILA SALUD` / `EPS [name]` / `NUEVA EPS` / `SURA` | Health contribution — ingreso no constitutivo | Part of social security |
| E-12 | `MEDICINA PREPAGADA` / `COLSANITAS` / `COOMEVA` | Private health — deducción (192 UVT/year cap) | Personal deduction |
| E-13 | `RETENCIÓN EN LA FUENTE` (annotation) | Tax credit — not expense | Credit against annual renta |
| E-14 | `PAGO RENTA DIAN` / `RECIBO OFICIAL` | Tax payment — NOT deductible | Payment of tax liability |
| E-15 | `GMF 4X1000` / `GRAVAMEN FINANCIERO` | 50% deductible | 50% of GMF paid is a deduction |
| E-16 | `COMBUSTIBLE` / `TERPEL` / `PRIMAX` / `BIOMAX` | Fuel — deductible (business proportion) | Require factura |
| E-17 | `PAPELERÍA` / `PANAMERICANA` | Office supplies — deductible | Require factura |
| E-18 | `CAPACITACIÓN` / `CURSO` / `DIPLOMADO` | Training — deductible | Professional development |
| E-19 | `CRÉDITO HIPOTECARIO INTERESES` | Mortgage interest — deducción (1,200 UVT/year cap) | Personal deduction |

### 3.3 Bank Fees and Financial (Exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BANCOLOMBIA | EXCLUDE for bank charges | Financial service |
| DAVIVIENDA | EXCLUDE for bank charges | Financial service |
| BANCO DE BOGOTÁ | EXCLUDE for bank charges | Financial service |
| BBVA COLOMBIA | EXCLUDE for bank charges | Financial service |
| BANCO DE OCCIDENTE | EXCLUDE for bank charges | Financial service |
| NEQUI (fees), DAVIPLATA (fees) | EXCLUDE | Fintech service fees |
| COMISIÓN BANCARIA, CUOTA MANEJO | EXCLUDE | Bank maintenance fee |
| INTERESES CRÉDITO | EXCLUDE | Loan interest (unless mortgage — see E-19) |

### 3.4 Government and Statutory (Exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| DIAN | EXCLUDE | Tax authority payment |
| SECRETARÍA DE HACIENDA | EXCLUDE | Municipal/departmental tax |
| ICA (Industria y Comercio) | EXCLUDE | Municipal tax (separate from renta) |
| CÁMARA DE COMERCIO | EXCLUDE | Chamber of commerce fees |

### 3.5 Internal Transfers and Exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| TRANSFERENCIA ENTRE CUENTAS | EXCLUDE | Internal movement |
| RETIRO ATM | TIER 2 — ask | Default exclude; ask purpose |
| CRÉDITO PERSONAL / LIBRANZA | EXCLUDE | Loan proceeds, out of scope |
| CUOTA CRÉDITO | EXCLUDE | Loan repayment, out of scope |

---

## Section 4 — Worked Examples

### Example 1 — Bancolombia (Medellín, IT Consultant)

**Bank:** Bancolombia statement
**Client:** Juan Carlos Restrepo, IT consultant, Medellín, resident

```
Fecha;Descripción;Débito;Crédito;Saldo
05/01/2025;ACH DE EMPRESA TECH SAS;;12.000.000;
15/01/2025;CUOTA MANEJO;25.000;;
10/02/2025;ACH DE STARTUP DIGITAL SAS;;8.500.000;
28/02/2025;PILA PENSIÓN PORVENIR;960.000;;
28/02/2025;PILA SALUD NUEVA EPS;750.000;;
15/03/2025;STRIPE PAYOUT COP;;4.200.000;
01/04/2025;GMF 4X1000;48.000;;
20/04/2025;ACH DE GAMMA CONSULTING SAS;;15.000.000;
10/07/2025;HONORARIOS CONTADOR;1.800.000;;
10/10/2025;AVIANCA VUELO BOGOTÁ;850.000;;
```

**Step 1 — Income Classification**

Annualised gross: COP 150,000,000 (example).
Retención en la fuente (11%): COP 16,500,000 withheld by corporate clients.

**Step 2 — Computation**

```
Ingresos brutos:                    COP 150,000,000
Less pension (ingreso no const.):   COP  11,520,000
Ingresos netos:                     COP 138,480,000
Less costos y gastos:               COP  30,000,000
Renta líquida:                      COP 108,480,000
Less 25% general exemption:         COP  27,120,000 (check cap 2,880 UVT)
  2,880 UVT x 49,799 = COP 143,421,120 — under cap
Check 40% cap: 27,120,000 / 138,480,000 = 19.6% — under 40%
Renta líquida gravable:             COP  81,360,000
In UVT: 81,360,000 / 49,799 = ~1,634 UVT
Tax: (1,634 - 1,090) x 19% x 49,799 = 544 x 19% x 49,799 = ~COP 5,147,890
Less retención: COP 16,500,000
Result: refund ~COP 11,352,110
```

### Example 2 — Davivienda (Bogotá, Architect with 40% Cap)

**Bank:** Davivienda statement
**Client:** María Fernández, architect, Bogotá

Gross: COP 200,000,000. Pension: COP 12,800,000.
Ingresos netos: COP 187,200,000. Costs: COP 40,000,000.
Renta líquida: COP 147,200,000.

Claimed exemptions + deductions:
- 25% general: COP 36,800,000
- AFC voluntary pension: COP 30,000,000
- Dependientes: COP 20,000,000
- Mortgage interest: COP 10,000,000
- Total: COP 96,800,000

40% of ingresos netos = COP 74,880,000.
5,040 UVT = COP 250,986,960.
Cap at COP 74,880,000 (lower). Must reduce from COP 96,800,000 to COP 74,880,000.

### Example 3 — Banco de Bogotá (Cali, Low-Income Refund)

**Bank:** Banco de Bogotá
**Client:** Andrés López, freelance designer, Cali

Gross: COP 60,000,000. After deductions: below 1,090 UVT.
Tax = COP 0. Retención refunded. Check filing threshold — COP 60M below 1,400 UVT threshold but may still file voluntarily for refund.

### Example 4 — BBVA Colombia (Bogotá, Foreign Client Income)

**Bank:** BBVA Colombia
**Client:** Laura Gutiérrez, management consultant, 40% income from US clients

Foreign income: no retención by foreign payer. All income subject to Colombian renta.
Must include in cédula general. No foreign tax credit unless treaty applies. Flag.

### Example 5 — Nequi / Daviplata (Barranquilla, Micro-Freelancer)

**Bank:** Nequi (Bancolombia digital)
**Client:** Carlos Herrera, freelance graphic designer, small Nequi payments

Nequi narrations: `Nequi recibido de [client]`.
Many small consumer payments = no retención.
Gross: COP 40,000,000. Below filing threshold (1,400 UVT = COP 65,891,000).
Not required to file — but may file voluntarily if retención was suffered for refund.

### Example 6 — Banco de Occidente (Bucaramanga, GMF Deduction Missed)

**Bank:** Banco de Occidente
**Client:** Patricia Vargas, consultant

GMF (4x1000) paid: COP 2,400,000 during the year.
50% deductible: COP 1,200,000. Often overlooked — include in deducciones. Reduces tax at marginal rate.

---

## Section 5 — Tier 1 Rules (Apply Directly)

**T1-CO-1 — The 40% / 5,040 UVT cap is mandatory**
Total rentas exentas plus deducciones cannot exceed 40% of ingresos netos or 5,040 UVT per year, whichever is lower. Always check this cap. Reduce proportionally if exceeded.

**T1-CO-2 — Pension contributions are ingresos no constitutivos de renta**
Mandatory pension contributions by the independent worker are excluded from gross income BEFORE arriving at ingresos netos. They are NOT a deduction — they reduce the income base at an earlier stage.

**T1-CO-3 — Retención is a credit, not income reduction**
The retención en la fuente (11% or 10%) withheld by clients is a credit against the annual tax balance. It does not reduce gross income. Always gross-up to the pre-retención amount.

**T1-CO-4 — No factura electrónica = no deduction**
DIAN requires factura electrónica for all deductible costs and expenses. Reject any expense claim without a valid factura.

**T1-CO-5 — IBC minimum is 1 SMLMV**
The ingreso base de cotización for social security cannot be below 1 SMLMV. If 40% of gross monthly income is below SMLMV, pay contributions on SMLMV.

**T1-CO-6 — GMF is 50% deductible**
The 4x1000 financial transaction tax (Gravamen a los Movimientos Financieros) is 50% deductible. Often overlooked. Include in deducciones.

**T1-CO-7 — Renta presuntiva is 0% for 2023+**
For tax year 2023 onwards, renta presuntiva is effectively 0%. No comparison needed. Verify for future reform.

---

## Section 6 — Tier 2 Catalogue (Reviewer Judgement Required)

| Code | Situation | Escalation Reason | Suggested Treatment |
|---|---|---|---|
| T2-CO-1 | 40% cap optimisation | Multiple ways to allocate the cap between exemptions and deductions | Flag — reviewer should optimise allocation |
| T2-CO-2 | Dependant definition unclear | ET art. 387 definition of economic dependence | Verify dependant status with supporting documentation |
| T2-CO-3 | Multiple income cédulas (work + rental + dividends) | Different cédulas have different rules | Flag — separate and aggregate correctly |
| T2-CO-4 | Foreign-source income | Colombian residents taxed on worldwide income | Escalate — treaty analysis if foreign tax paid |
| T2-CO-5 | AFC / FVP voluntary pension contributions | Complex interaction with 40% cap | Flag — confirm amounts and cap interaction |
| T2-CO-6 | First-year filer anticipo calculation | 25% first year, 50% second, 75% third+ | Flag — verify year number for anticipo rate |

---

## Section 7 — Excel Working Paper Template

```
COLOMBIAN RENTA WORKING PAPER (PERSONA NATURAL — TRABAJADOR INDEPENDIENTE)
Taxpayer: _______________  NIT/Cédula: _______________  FY: 2025

SECTION A — INGRESOS BRUTOS
                                        COP
Independent work (cédula general):     ___________
Capital income:                        ___________
Non-labour income (rental, etc.):      ___________
Foreign-source income:                 ___________
TOTAL INGRESOS BRUTOS                 ___________

SECTION B — INGRESOS NO CONSTITUTIVOS DE RENTA
Mandatory pension (worker portion):    ___________
Other non-constitutive:                ___________
TOTAL INGRESOS NETOS                  ___________

SECTION C — COSTOS Y GASTOS
Office rent (factura):                 ___________
Utilities (business %, factura):       ___________
Phone/internet (factura):              ___________
Software (factura):                    ___________
Accounting/legal (factura):            ___________
Travel (factura):                      ___________
Other documented (factura):            ___________
TOTAL COSTOS Y GASTOS                 ___________

SECTION D — RENTA LÍQUIDA
Ingresos netos - costos y gastos      ___________

SECTION E — RENTAS EXENTAS + DEDUCCIONES
25% general worker exemption:          ___________  (cap: 2,880 UVT)
AFC/FVP voluntary pension:            ___________  (cap: 3,800 UVT)
Dependientes (10%, max 384 UVT):      ___________
Mortgage interest (max 1,200 UVT):    ___________
Medicina prepagada (max 192 UVT):     ___________
GMF 50%:                               ___________
TOTAL EXEMPTIONS + DEDUCTIONS          ___________
40% cap check (40% of ingresos netos):___________
5,040 UVT cap:                         ___________
APPLIED AMOUNT (lower of caps):       ___________

SECTION F — RENTA LÍQUIDA GRAVABLE
Renta líquida - applied exemptions    ___________
In UVT (÷ UVT value):                ___________

SECTION G — TAX COMPUTATION
Tax per art. 241 table (in UVT):      ___________
Tax in COP:                            ___________

SECTION H — CREDITS
Retención en la fuente:                (___________)
Anticipos paid:                        (___________)
TAX DUE / (REFUND)                    ___________

SECTION I — ANTICIPO FOR NEXT YEAR
Year number: ___  Rate: ___%
Anticipo calculation:                  ___________

SECTION J — REVIEWER FLAGS
[ ] Residency confirmed (183+ days)?
[ ] Correct UVT year applied?
[ ] 40%/5,040 UVT cap checked?
[ ] All costs/expenses have factura electrónica?
[ ] Retención certificates collected from all payers?
[ ] IBC minimum (SMLMV) verified for social security?
[ ] GMF 50% deduction included?
[ ] Pension treated as ingreso no constitutivo (not deduction)?
[ ] Filing threshold checked?
[ ] Anticipo calculated correctly (year number)?
```

---

## Section 8 — Bank Statement Reading Guide

### Bancolombia
- Export: CSV/Excel from Sucursal Virtual Personas
- Columns: `Fecha;Descripción;Débito;Crédito;Saldo`
- Amount format: period thousands, comma decimal (e.g., `12.000.000,00`)
- Date: DD/MM/YYYY
- Credits: `ACH DE [sender]`, `TRANSFERENCIA RECIBIDA`

### Davivienda
- Export: CSV/PDF from Davivienda Virtual
- Columns: `Fecha;Concepto;Débito;Crédito;Saldo`
- Standard Colombian format

### Banco de Bogotá
- Export: CSV from Banca Virtual
- Columns: `Fecha;Descripción;Valor;Saldo`
- Positive = credit; negative = debit

### BBVA Colombia
- Export: CSV/PDF from BBVA Net
- Columns: `Fecha;Detalle;Débito;Crédito;Saldo`
- ACH narrations: `ACH RECIBIDA [sender]`

### Banco de Occidente
- Export: CSV from Occidente Virtual
- Standard format

### Nequi (Bancolombia Digital)
- Export: CSV/PDF from Nequi app
- Simple format: `Fecha;Descripción;Valor`
- Positive = credit; negative = debit
- Narrations: `Nequi recibido de [name]`, `Transferencia recibida`

### Daviplata (Davivienda Digital)
- Export: PDF from Daviplata app
- Simple format; narrations include `Daviplata recibido de [name]`

### PSE (Pagos Seguros en Línea)
- Not a bank — PSE payments appear in primary bank statement as `PSE [payer]`
- Used for electronic payments; appear as credits when collecting

### Key Colombian Banking Notes
- All amounts in COP (Colombian pesos); period as thousands separator, comma as decimal
- ACH (Cámara de Compensación) is the standard inter-bank transfer system
- Nequi and Daviplata are the dominant digital wallets; receipts appear in the linked bank account

---

## Section 9 — Onboarding Fallback

**Residency confirmation:**
> "Before computing your Colombian renta, I need to confirm your tax residency. Are you a Colombian resident (present 183 or more days in the calendar year or prior year)? Residents are taxed on worldwide income using progressive rates. Non-residents pay a flat 35% on Colombia-source income with no deductions. Please confirm your residency status."

**Missing retención certificates:**
> "To credit retención en la fuente against your annual tax, I need the certificados de retención from each client who withheld taxes. Companies are legally required to issue these. You can also check información exógena on the DIAN portal. Without certificates, the withholding credit cannot be claimed."

**Social security verification:**
> "Independent workers in Colombia must pay pensión (16%), salud (12.5%), and ARL through PILA on a base of 40% of gross monthly income (minimum 1 SMLMV). Do you have records of PILA payments? The pension portion is deducted as ingreso no constitutivo de renta — it reduces your tax base."

**40% cap explanation:**
> "Colombian tax law caps the total of rentas exentas and deducciones at 40% of your ingresos netos or 5,040 UVT, whichever is lower. This means your 25% worker exemption, voluntary pension, dependant deduction, mortgage interest, and other deductions combined cannot exceed this limit. I need to optimise how these are applied."

---

## Section 10 — Reference Material

### Key Legislation
- **Estatuto Tributario (ET)** — arts. 5-364 (Libro I)
- **Ley 2277 de 2022** — Reforma Tributaria
- **Ley 2010 de 2019** — prior reform
- **Decreto 1625 de 2016** — DUR Tributario
- **Ley 100 de 1993** — Social security
- **Decreto 1273 de 2018** — Independent worker contributions

### Filing Calendar

| Deadline | Event |
|---|---|
| August -- October (by NIT last 2 digits) | Declaración de Renta (Formulario 210) |
| Monthly | Retención en la fuente (if agente de retención) |
| Monthly | PILA social security contributions |

### Penalties

| Offence | Penalty |
|---|---|
| Late filing (extemporaneidad) | 5% of tax per month of delay (max 100%) |
| Late payment interest | Tasa de usura (~30-35% annual) |
| Inexactitud (inaccuracy) | 100% of tax difference (50% if corrected early) |
| No filing after emplazamiento | 20% of patrimonio líquido or 160% of tax |

### Useful References
- DIAN Portal: www.dian.gov.co
- Servicios en Línea: muisca.dian.gov.co
- UVT values: DIAN resolution annual
- PILA: www.aportesenlinea.com / www.miplanilla.com
- SMLMV 2025: verify with Ministerio de Trabajo
