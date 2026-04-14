---
name: ar-income-tax
description: >
  Use this skill whenever asked about Argentine income tax (Impuesto a las Ganancias) for self-employed individuals (autónomos / profesionales independientes). Trigger on phrases like "Ganancias", "impuesto a las ganancias", "autónomo Argentina", "monotributo vs responsable inscripto", "cuarta categoría", "deducciones personales", "ganancia no imponible", "bienes personales", "DDJJ Ganancias", "ARCA", "AFIP", "CUIT", "income tax Argentina", "anticipos ganancias", or any question about filing or computing income tax for a self-employed client in Argentina. This skill covers progressive rates (5-35%), personal deductions (ganancia no imponible, cargas de familia, deducción especial), Bienes Personales interaction, advance payments (anticipos), percepciones as credits, and ARCA filing. ALWAYS read this skill before touching any Argentine income tax work.
version: 2.0
---

# Argentine Income Tax — Autónomo / Profesional Independiente (Ganancias) v2.0

## Section 1 — Quick Reference

### Progressive Tax Scale — First Semester 2025 (Illustrative)

WARNING: Argentina adjusts these thresholds semi-annually (January and July) by the IPC (Consumer Price Index). You MUST verify the current semester's thresholds with ARCA before applying. The amounts below are for the first semester 2025 only.

| Ganancia Neta Imponible Acumulada (ARS) | Rate | Cumulative Fixed Amount |
|---|---|---|
| 0 -- 1,750,026 | 5% | -- |
| 1,750,027 -- 3,500,053 | 9% | 87,501 |
| 3,500,054 -- 5,250,079 | 12% | 245,004 |
| 5,250,080 -- 7,000,106 | 15% | 455,007 |
| 7,000,107 -- 10,500,159 | 19% | 717,511 |
| 10,500,160 -- 14,000,211 | 23% | 1,382,521 |
| 14,000,212 -- 21,000,317 | 27% | 2,187,033 |
| 21,000,318 -- 28,000,423 | 31% | 4,077,062 |
| 28,000,424+ | 35% | 6,247,095 |

Formula: Tax = Cumulative Fixed Amount + (Ganancia Neta Imponible - Lower Limit) x Rate

### Personal Deductions (Deducciones Personales) — First Semester 2025 (Illustrative)

| Deduction | Annual Amount (ARS, approx) | Notes |
|---|---|---|
| Ganancia no imponible (GNI) | ~3,916,268 | Minimum non-taxable income |
| Deducción especial — autónomos | GNI x 2.5 = ~9,790,671 | For autónomos under art. 53 |
| Deducción especial — empleados | GNI x 3.8 = ~14,881,819 | NOT for autónomos |
| Cónyuge | ~3,688,339 | Spouse with income below GNI |
| Hijo/a menor de 18 | ~1,860,043 per child | Per child under 18 |
| Hijo/a con discapacidad | ~3,720,086 per child | No age limit |

### General Deductions (Deducciones Generales, art. 85)

| Deduction | Limit |
|---|---|
| Aportes jubilatorios (retirement) | Actual amount paid |
| Obra social / prepaga (health) | 5% of ganancia neta |
| Seguros de vida / retiro | Annual cap (adjusted semi-annually) |
| Servicio doméstico | Up to GNI amount |
| Alquiler vivienda habitual | 40% of rent, capped at GNI |
| Donaciones (to exempt entities) | 5% of ganancia neta |

### Computation Structure

| Step | Description |
|---|---|
| A | Ganancia bruta (gross income from all categories) |
| B | Less: Gastos deducibles (allowable business expenses, art. 83-87) |
| C | Ganancia neta (A minus B) |
| D | Less: Deducciones generales (art. 85) |
| E | Less: Deducciones personales (art. 30 — GNI + deducción especial + cargas de familia) |
| F | Ganancia neta imponible (C minus D minus E) |
| G | Apply progressive scale to F |
| H | Less: Anticipos paid |
| I | Less: Retenciones sufridas |
| J | Less: Percepciones (e.g., on foreign currency purchases) |
| K | Tax due / (refund) |

### Conservative Defaults

| Situation | Default Assumption |
|---|---|
| Autónomo vs empleado unclear | STOP — multiplier differs (2.5x vs 3.8x) |
| Semi-annual thresholds uncertain | Verify with ARCA — never use stale thresholds |
| Undocumented expenses | NOT deductible + 35% punitive tax (art. 38) |
| Spouse claimed but income uncertain | Do NOT claim unless confirmed below GNI |
| Percepciones from USD purchases | Include as credit against final DDJJ |
| Monotributo vs Responsable Inscripto | STOP — entirely different regime |
| Bienes Personales threshold | Flag — always check alongside Ganancias |

### Red Flag Thresholds

| Flag | Threshold |
|---|---|
| No aportes jubilatorios claimed | Verify — mandatory for autónomos |
| Gastos sin factura detected | Non-deductible + 35% punitive tax |
| Single client > 80% of income | Employment relationship risk |
| Large percepciones claimed as credit | Verify certificates from ARCA account |
| Bienes Personales threshold may be exceeded | Flag for concurrent filing |

---

## Section 2 — Required Inputs + Refusal Catalogue

### Required Inputs

Before computing Argentine Ganancias, collect:

1. **Tax category** — 4ta categoría autónomo (art. 53) or relación de dependencia
2. **Marital / family status** — for cargas de familia deductions
3. **Gross annual income from self-employment** — total honorarios / ingresos brutos
4. **Business expenses** — documented with facturas electrónicas
5. **Retirement contributions (jubilación autónomos)** — mandatory contributions paid
6. **Obra social and prepaga contributions** — health insurance paid
7. **Other income sources** — employment, rental (1ra cat.), financial (2da cat.)
8. **Bienes Personales status** — assets above threshold
9. **CUIT** — tax identification number
10. **Bank statements** — 12 months (calendar year)
11. **Percepciones suffered** — from foreign currency purchases, imports
12. **Anticipos paid** — advance payments from prior DDJJ

### Refusal Catalogue

| Code | Situation | Action |
|---|---|---|
| R-AR-1 | Client is Monotributo | Stop — Monotributo is a separate simplified regime; use ar-monotributo skill |
| R-AR-2 | Tax category unknown (autónomo vs empleado) | Stop — deducción especial multiplier differs; category is mandatory |
| R-AR-3 | Gastos sin factura (undocumented expenses) claimed | Reject + flag 35% punitive tax under art. 38 |
| R-AR-4 | Foreign-source income with treaty implications | Escalate — worldwide income applies but foreign tax credits need treaty analysis |
| R-AR-5 | Trust taxation or corporate reorganisation | Escalate — outside scope |
| R-AR-6 | No CUIT provided | Stop — cannot determine filing schedule |

---

## Section 3 — Transaction Pattern Library

### 3.1 Income Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| I-01 | `TRANSFERENCIA DE [client]` / `TRF CR [client]` | Gross income — Ganancias 4ta cat. | Standard inter-bank transfer from client |
| I-02 | `ACREDITACIÓN CVU [client]` / `CVU CRÉDITO` | Gross income — Ganancias 4ta cat. | CVU (fintech wallet) credit from client |
| I-03 | `MERCADOPAGO COBRO` / `MP COBRO [client]` | Gross income — gross-up | Mercado Pago settlement; fee deductible with factura |
| I-04 | `DEBIN RECIBIDO [client]` | Gross income — Ganancias 4ta cat. | DEBIN (instant debit request) payment received |
| I-05 | `PAYPAL RETIRO` / `PAYPAL TRANSFER` | Gross income — foreign source | PayPal withdrawal; convert at ARCA exchange rate |
| I-06 | `STRIPE PAYOUT` / `STRIPE AR` | Gross income — foreign source | Stripe payout; classify by payer country |
| I-07 | `RAPIPAGO COBRO` / `PAGO FÁCIL COBRO` | Gross income — Ganancias 4ta cat. | Cash collection network receipt |
| I-08 | `DEVOLUCIÓN GANANCIAS ARCA` / `REINTEGRO ARCA` | NOT income — tax refund | Refund of overpaid tax |
| I-09 | `INTERESES PLAZO FIJO` / `RENDIMIENTO FCI` | 2da categoría — financial income | Interest/fund returns; separate treatment |
| I-10 | `DIVIDENDOS [company]` | Renta exenta or gravada | Dividends; verify current treatment |
| I-11 | `ALQUILER COBRADO` / `RENTA INMUEBLE` | 1ra categoría — rental income | Separate category; aggregates in Ganancias |

### 3.2 Expense Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| E-01 | `ALQUILER OFICINA` / `LOCACIÓN COMERCIAL` | Rent — fully deductible | Require factura electrónica |
| E-02 | `EDESUR` / `EDENOR` / `EPEC` / `EPE` | Utilities — deductible (business proportion) | Electricity; require factura |
| E-03 | `METROGAS` / `NATURGY` / `CAMUZZI` | Gas — deductible (business proportion) | Require factura |
| E-04 | `PERSONAL` / `CLARO` / `MOVISTAR` / `TELECOM` | Phone/internet — deductible (business %) | Require factura |
| E-05 | `ADOBE` / `MICROSOFT 365` / `GOOGLE WORKSPACE` | Software — fully deductible | Professional tools |
| E-06 | `CONTADOR` / `ESTUDIO CONTABLE` / `HONORARIOS CPN` | Accounting fees — fully deductible | Require factura |
| E-07 | `AEROLÍNEAS ARGENTINAS` / `FLYBONDI` / `JETSMART` | Air travel — deductible (business purpose) | Document purpose |
| E-08 | `HOTEL` / `BOOKING.COM` / `AIRBNB` | Accommodation — deductible (business travel) | Business purpose required |
| E-09 | `MONOTRIBUTO APORTES` / `JUBILACIÓN AUTÓNOMOS` | Retirement contributions — deducción general | Fully deductible |
| E-10 | `OBRA SOCIAL` / `PREPAGA` / `OSDE` / `SWISS MEDICAL` | Health insurance — deducción general (5% cap) | Cap at 5% of ganancia neta |
| E-11 | `SEGURO PROFESIONAL` / `RC PROFESIONAL` | Professional insurance — fully deductible | |
| E-12 | `COLEGIO PROFESIONAL` / `CPACF` / `MATRÍCULA` | Professional body fees — fully deductible | |
| E-13 | `PAGO GANANCIAS ARCA` / `VEP GANANCIAS` | Tax payment — NOT deductible | Credit against liability |
| E-14 | `ANTICIPO GANANCIAS` / `VEP ANTICIPO` | Advance payment — NOT deductible | Credit against annual DDJJ |
| E-15 | `PERCEPCIÓN RG 4815` / `PERC. DÓLAR` / `IMP. PAÍS` | Percepción — NOT deductible | Credit against Ganancias DDJJ |
| E-16 | `MARKETING` / `PUBLICIDAD` / `GOOGLE ADS` | Marketing — fully deductible | Require factura or foreign invoice |
| E-17 | `PAPELERÍA` / `INSUMOS OFICINA` | Office supplies — fully deductible | Require factura |
| E-18 | `SERVICIO DOMÉSTICO` | Domestic staff — deducción general | Capped at GNI amount |
| E-19 | `ALQUILER VIVIENDA` / `INQUILINO` | Housing rent (personal) — deducción general | 40% of rent, capped at GNI |

### 3.3 Bank Fees and Financial (Exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BANCO NACIÓN, BNA | EXCLUDE for bank charges/fees | Financial service |
| BANCO GALICIA, GALICIA | EXCLUDE for bank charges/fees | Financial service |
| SANTANDER ARGENTINA | EXCLUDE for bank charges/fees | Financial service |
| BBVA ARGENTINA | EXCLUDE for bank charges/fees | Financial service |
| MACRO, BANCO MACRO | EXCLUDE for bank charges/fees | Financial service |
| BRUBANK, UALA, NARANJA X | EXCLUDE for fintech fees | Check for separate taxable subscription |
| COMISIÓN BANCARIA, MANTENIMIENTO CTA | EXCLUDE | Bank maintenance fee |
| INTERESES, INTERÉS PRÉSTAMO | EXCLUDE | Interest on loan — out of scope |

### 3.4 Government and Statutory (Exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| ARCA, AFIP | EXCLUDE | Tax payment |
| ANSES | EXCLUDE | Social security system payment |
| RENTAS [province] | EXCLUDE | Provincial tax (Ingresos Brutos — separate) |
| ARBA, AGIP, DGIP | EXCLUDE | Provincial revenue agency payment |
| MUNICIPALIDAD | EXCLUDE | Municipal fee/tax |

### 3.5 Internal Transfers and Exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| TRANSFERENCIA PROPIA, CUENTA PROPIA | EXCLUDE | Internal movement |
| EXTRACCIÓN ATM, RETIRO EFECTIVO | TIER 2 — ask | Default exclude; ask purpose |
| PRÉSTAMO PERSONAL | EXCLUDE | Loan principal, out of scope |
| CUOTA PRÉSTAMO | EXCLUDE | Loan repayment, out of scope |

---

## Section 4 — Worked Examples

### Example 1 — Banco Nación (Buenos Aires, IT Consultant)

**Bank:** Banco de la Nación Argentina statement
**Client:** Martín López, IT consultant, Buenos Aires, Responsable Inscripto

```
Fecha;Concepto;Débito;Crédito;Saldo
05/01/2025;TRANSFERENCIA CR EMPRESA TECH SA;;1.200.000;
15/01/2025;COMISIÓN BANCARIA;1.500;;
10/02/2025;TRANSFERENCIA CR STARTUP DIGITAL SRL;;850.000;
28/02/2025;VEP JUBILACIÓN AUTÓNOMOS;180.000;;
15/03/2025;PAYPAL RETIRO;;420.000;
31/03/2025;ANTICIPO GANANCIAS VEP;250.000;;
20/04/2025;MERCADOPAGO COBRO;;380.000;
05/06/2025;TRANSFERENCIA CR GAMMA CONSULTING SA;;1.500.000;
10/07/2025;ESTUDIO CONTABLE PÉREZ;120.000;;
10/10/2025;AEROLÍNEAS ARGENTINAS;95.000;;
```

**Step 1 — Income Classification**

| Narration | Pattern | Amount (ARS) | Notes |
|---|---|---|---|
| EMPRESA TECH SA | I-01 | 1,200,000 | Domestic PJ — check retención |
| STARTUP DIGITAL SRL | I-01 | 850,000 | Domestic PJ — check retención |
| PAYPAL RETIRO | I-05 | 420,000 | Foreign source — convert at ARCA rate |
| MERCADOPAGO COBRO | I-03 | 380,000 | Gross up for MP fees |
| GAMMA CONSULTING SA | I-01 | 1,500,000 | Domestic PJ — check retención |

Total gross annualised: ARS 28,000,000 (example)

**Step 2 — Deductible Expenses**

Accounting: ARS 1,440,000; jubilación: ARS 2,160,000; travel: ARS 1,140,000; software: ARS 480,000; bank fees excluded.

**Step 3 — Computation**

```
Ganancia bruta:              ARS 28,000,000
Less gastos deducibles:      ARS  5,220,000
Ganancia neta:               ARS 22,780,000
Less deducciones generales:  ARS  2,160,000 (jubilación)
Less deducciones personales:
  GNI:                       ARS  3,916,268
  Deducción especial (2.5x): ARS  9,790,671
  Total personal:            ARS 13,706,939
Ganancia neta imponible:     ARS  6,913,061
Tax (apply scale):           ~ARS 1,012,000
Less anticipos + retenciones + percepciones
```

### Example 2 — Banco Galicia (Córdoba, Architect)

**Bank:** Banco Galicia statement
**Client:** Lucía Fernández, architect, Córdoba, married with 2 children

Gross income: ARS 35,000,000
Expenses: ARS 8,000,000 (staff, office rent, software, materials)
Jubilación: ARS 2,400,000
Obra social: ARS 600,000 (check 5% cap)

Personal deductions: GNI + DE (2.5x) + cónyuge + 2 hijos = ARS 13,706,939 + ARS 3,688,339 + ARS 3,720,086 = ARS 21,115,364

Ganancia neta imponible: ARS 35,000,000 - 8,000,000 - 3,000,000 - 21,115,364 = ARS 2,884,636

Tax: bracket 1,750,027–3,500,053 at 9% = ARS 87,501 + (2,884,636 - 1,750,027) x 9% = ARS 87,501 + ARS 102,115 = ARS 189,616

Flag: Verify spouse income is below GNI. Verify Bienes Personales.

### Example 3 — Santander Argentina (CABA, Digital Creator with Percepciones)

**Bank:** Santander Argentina
**Client:** Diego Ruiz, digital creator, receives foreign payments, large percepciones from USD purchases

Gross income: ARS 18,000,000 (mix of domestic and foreign)
Percepciones from USD purchases: ARS 3,500,000 (RG 4815 + adelanto Ganancias)

After deductions and personal allowances, tax per scale: ARS 1,200,000
Less percepciones: ARS 3,500,000
Result: Saldo a favor (credit balance) ARS 2,300,000

Flag: Percepciones exceed computed tax. Client has saldo a favor. Verify all percepción certificates.

### Example 4 — Brubank (CABA, Freelance Developer, Low Income)

**Bank:** Brubank (digital bank)
**Client:** Ana García, freelance developer, single, no dependants

Gross income: ARS 15,000,000
Expenses: ARS 4,000,000
Jubilación: ARS 1,800,000

After GNI + DE (2.5x) = ARS 13,706,939:
Ganancia neta imponible: ARS 15,000,000 - 4,000,000 - 1,800,000 - 13,706,939 = max(0, -4,506,939) = ARS 0

Tax: ARS 0. Personal deductions fully shelter the income.

### Example 5 — Banco Macro (Tucumán, Physician with Gastos sin Factura)

**Bank:** Banco Macro
**Client:** Dr. Carlos Méndez, physician, Tucumán

Issue: Client claims ARS 2,000,000 in expenses without facturas.

Resolution: NOT deductible under art. 83. Additionally, art. 38 imposes 35% punitive tax on undocumented expenses = ARS 700,000 additional tax. Remove from deductions and flag.

### Example 6 — BBVA Argentina (Mendoza, Consultant with Mixed Income)

**Bank:** BBVA Argentina
**Client:** Patricia Vega, consultant, Mendoza, also earns rental income

Self-employment: ARS 22,000,000
Rental income (1ra categoría): ARS 6,000,000
Total ganancia bruta: ARS 28,000,000

All income categories aggregate. Apply expenses per category. Apply GNI + DE + cargas to combined ganancia neta. Flag: Bienes Personales likely triggered by real property.

---

## Section 5 — Tier 1 Rules (Apply Directly)

**T1-AR-1 — Autónomos use the 2.5x multiplier, NEVER 3.8x**
The deducción especial multiplier of 3.8x is exclusively for empleados en relación de dependencia. Autónomos use 2.5x the ganancia no imponible. Apply without escalating.

**T1-AR-2 — Undocumented expenses trigger 35% punitive tax**
Gastos sin factura are not only non-deductible but subject to an additional 35% tax on the gross undocumented amount under art. 38 of Ley 20.628. Always flag and compute the 35% penalty.

**T1-AR-3 — Percepciones are credits, not deductions**
Percepciones suffered (e.g., RG 4815 on foreign currency purchases, import percepciones) are credits against the annual DDJJ Ganancias. They reduce the final tax balance payable. If percepciones exceed tax, a saldo a favor results.

**T1-AR-4 — Anticipos are credits, not deductions**
Advance payments (anticipos) paid bimonthly are credits against the final DDJJ. They are NOT deductible expenses.

**T1-AR-5 — Cargas de familia: dependent must earn below GNI**
The cónyuge and hijo deductions only apply if the dependent's own income is below the ganancia no imponible. Verify before applying.

**T1-AR-6 — Semi-annual threshold adjustment is mandatory**
Argentina adjusts tax scale thresholds and personal deduction amounts every 6 months by IPC. Each semester's income must use that semester's applicable thresholds. Never use a full-year table from a single semester.

**T1-AR-7 — Bienes Personales must be considered alongside Ganancias**
Bienes Personales is a separate wealth tax (progressive 0.5% to 1.75%) filed on the same schedule as Ganancias. Always flag when a client's asset base may exceed the threshold.

---

## Section 6 — Tier 2 Catalogue (Reviewer Judgement Required)

| Code | Situation | Escalation Reason | Suggested Treatment |
|---|---|---|---|
| T2-AR-1 | Monotributo vs Responsable Inscripto decision | Entire regime differs; depends on turnover, expenses, and client position | Flag for Contador Público; do not compute under wrong regime |
| T2-AR-2 | Home office expense proportion | Requires documented dedicated space and proportion calculation | Flag — proportional deduction; reviewer must confirm methodology |
| T2-AR-3 | Motor vehicle business use percentage | Limited deduction under art. 88; acquisition and running costs capped | Flag — vehicle business-use percentage must be documented |
| T2-AR-4 | Semi-annual threshold application | Each semester may have different amounts; annual DDJJ aggregates both | Flag — confirm correct semester thresholds applied |
| T2-AR-5 | Bienes Personales interaction | Assets above threshold trigger wealth tax; filed alongside Ganancias | Flag — verify asset base and threshold; separate computation |
| T2-AR-6 | Foreign-source income for Argentine resident | Worldwide income subject to Ganancias; foreign tax credits may apply | Escalate — treaty analysis required |

---

## Section 7 — Excel Working Paper Template

```
ARGENTINE GANANCIAS WORKING PAPER (AUTÓNOMO / PROFESIONAL INDEPENDIENTE)
Taxpayer: _______________  CUIT: _______________  FY: 2025 (Calendar Year)

SECTION A — INCOME (GANANCIA BRUTA)
                                        ARS
4ta categoría (honorarios/servicios):  ___________
1ra categoría (rental, if any):        ___________
2da categoría (financial, if any):     ___________
Foreign-source income (converted):     ___________
TOTAL GANANCIA BRUTA                   ___________

SECTION B — GASTOS DEDUCIBLES (Art. 83-87)
Office rent:                           ___________
Utilities (business %):                ___________
Phone/internet (business %):           ___________
Software:                              ___________
Accounting/legal fees:                 ___________
Travel (business purpose):             ___________
Marketing/advertising:                 ___________
Staff salaries + cargas sociales:      ___________
Office supplies:                       ___________
Professional insurance:                ___________
Professional body fees:                ___________
TOTAL GASTOS DEDUCIBLES                ___________

SECTION C — GANANCIA NETA
Ganancia bruta - gastos deducibles     ___________

SECTION D — DEDUCCIONES GENERALES (Art. 85)
Aportes jubilatorios:                  ___________
Obra social / prepaga (5% cap):        ___________
Seguros de vida:                       ___________
Servicio doméstico (GNI cap):          ___________
Alquiler vivienda (40%, GNI cap):      ___________
Donaciones (5% cap):                   ___________
TOTAL DEDUCCIONES GENERALES            ___________

SECTION E — DEDUCCIONES PERSONALES (Art. 30)
Ganancia no imponible (GNI):           ___________
Deducción especial (2.5x GNI):        ___________
Cónyuge:                               ___________
Hijos (x ___):                         ___________
TOTAL DEDUCCIONES PERSONALES           ___________

SECTION F — GANANCIA NETA IMPONIBLE
C - D - E (min 0):                     ___________

SECTION G — IMPUESTO DETERMINADO
Tax per progressive scale:             ___________

SECTION H — CREDITS
Anticipos paid:                        (___________)
Retenciones sufridas:                  (___________)
Percepciones (RG 4815, etc.):          (___________)
TAX DUE / (SALDO A FAVOR)             ___________

SECTION I — REVIEWER FLAGS
[ ] Tax category confirmed (autónomo, not empleado or Monotributo)?
[ ] Semi-annual thresholds verified with ARCA?
[ ] All expenses documented with facturas electrónicas?
[ ] No gastos sin factura included (35% penalty check)?
[ ] Cargas de familia — dependant income below GNI confirmed?
[ ] Percepciones certificates verified?
[ ] Bienes Personales obligation assessed?
[ ] Foreign income converted at ARCA official rate?
```

---

## Section 8 — Bank Statement Reading Guide

### Banco de la Nación Argentina (BNA)
- Export: PDF or CSV from Home Banking BNA
- Columns: `Fecha;Concepto;Débito;Crédito;Saldo`
- Amount format: period thousands separator, comma decimal (e.g., `1.200.000,00`)
- Date: DD/MM/YYYY
- Credit narrations: `TRANSFERENCIA CR [sender]`, `ACREDITACIÓN [sender]`

### Banco Galicia
- Export: CSV/Excel from Online Banking Galicia
- Columns: `Fecha;Descripción;Débito;Crédito;Saldo`
- Standard Argentine format; positive credit, negative debit
- SPEI/CVU narrations: `TRF CVU [sender]`, `TRANSFERENCIA [sender]`

### Santander Argentina
- Export: CSV/PDF from Santander Online
- Columns: `Fecha;Concepto;Importe;Saldo`
- Positive = credit; negative = debit

### BBVA Argentina (ex-Francés)
- Export: CSV/PDF from BBVA Net
- Columns: `Fecha;Detalle;Débito;Crédito;Saldo`
- Narrations: `TRF RECIBIDA DE [sender]`

### Banco Macro
- Export: CSV from Macro Online
- Standard format; `Fecha;Movimiento;Débito;Crédito;Saldo`

### Brubank / Ualá / Naranja X (Digital Banks)
- Export: CSV or PDF from app
- Simple format; credit/debit in single column (positive/negative) or separate columns
- CVU transfers: `Transferencia recibida de [sender]`
- Mercado Pago: `MP COBRO [amount]`

### Mercado Pago
- Not a bank statement per se; settlements appear in the primary bank statement
- Look for: `MERCADOPAGO`, `MP COBRO`, `LIQUIDACIÓN MP`
- Gross-up required for fee deduction

### Key Argentine Banking Notes
- All amounts in ARS (Argentine pesos); period as thousands separator, comma as decimal
- CVU (Clave Virtual Uniforme) is the Argentine instant payment identifier for fintech wallets
- CBU (Clave Bancaria Uniforme) for traditional bank transfers
- Both CVU and CBU transfers appear as credits with sender identification

---

## Section 9 — Onboarding Fallback

**Tax category confirmation:**
> "Before I can compute your Ganancias, I need to confirm your tax category. Are you registered as an autónomo (Responsable Inscripto) or are you in Monotributo? If Monotributo, you pay a fixed monthly fee (DAS) and do not file a Ganancias return on this income — a different skill applies. If you are a Responsable Inscripto autónomo, this skill applies. Please check your status at www.arca.gob.ar with your Clave Fiscal."

**Missing facturas:**
> "Argentine tax law requires all deductible expenses to be supported by facturas electrónicas. Expenses without facturas are not only non-deductible but trigger a 35% punitive tax under art. 38 of Ley 20.628. Please ensure all claimed expenses have corresponding facturas. You can verify your received facturas at www.arca.gob.ar → 'Mis Comprobantes'."

**Percepciones verification:**
> "I see you may have percepciones from foreign currency purchases or imports (RG 4815 / Impuesto PAÍS). These are credits against your Ganancias DDJJ. To claim them, I need the percepción certificates. You can download them from your ARCA account under 'Mis Retenciones' or check your bank statements for percepción line items."

**Bienes Personales reminder:**
> "As part of your annual tax filing, I also need to assess whether you have a Bienes Personales (wealth tax) obligation. This tax applies to worldwide assets exceeding a threshold updated annually by ARCA. Do you own real estate, vehicles, investments, or bank deposits that in aggregate might exceed the threshold? Bienes Personales is filed on the same schedule as Ganancias."

---

## Section 10 — Reference Material

### Key Legislation
- **Ley 20.628** — Impuesto a las Ganancias (texto ordenado)
- **Ley 27.743** — Paquete Fiscal 2024 (modified rates and thresholds)
- **Ley 23.966** — Impuesto sobre los Bienes Personales
- **Ley 11.683** — Procedimiento Tributario (penalties, interest)
- **Decreto Reglamentario** — implementing regulations

### Filing Calendar

| Deadline | Event |
|---|---|
| June (by last CUIT digit) | DDJJ Ganancias annual return |
| June (same schedule) | DDJJ Bienes Personales |
| Bimonthly from June | Anticipos (5 instalments, 20% each of prior year tax) |

### Penalties

| Offence | Penalty |
|---|---|
| Late filing (omisión) | 1% per month of unpaid tax (up to 100%) |
| Material omission (art. 45) | 100% of omitted tax |
| Tax fraud (art. 46) | 200-1000% of evaded tax + criminal |
| Undocumented expenses (art. 38) | 35% additional tax on gross amount |
| Late payment interest | ARCA resolutiva rate (~4-6% monthly) |

### Useful References
- ARCA Portal: www.arca.gob.ar
- Clave Fiscal: servicioscf.arca.gob.ar
- IPC updates: www.indec.gob.ar
- Bienes Personales thresholds: check ARCA RG annually


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
