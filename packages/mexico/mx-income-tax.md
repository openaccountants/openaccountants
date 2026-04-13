---
name: mx-income-tax
description: >
  Use this skill whenever asked about Mexican individual income tax (ISR) for self-employed individuals (personas físicas con actividades empresariales y profesionales). Trigger on phrases like "how much tax do I pay in Mexico", "ISR", "Declaración Anual", "pagos provisionales", "actividades profesionales", "honorarios", "RESICO", "deducciones personales", "deducciones autorizadas", "retenciones", "RFC", "income tax return Mexico", "SAT", "CFDI honorarios", "comprobante fiscal", or any question about filing or computing income tax for a self-employed or freelance client in Mexico. This skill covers the Declaración Anual PF (Personas Físicas), pagos provisionales (monthly estimated payments), progressive ISR brackets, deducciones autorizadas and personales, retenciones on professional CFDI, and the RESICO regime. ALWAYS read this skill before touching any Mexican income tax work.
version: 2.0
---

# Mexican Income Tax — Persona Física Actividades Profesionales (ISR) v2.0

## Section 1 — Quick Reference

### ISR Annual Brackets 2025 (Personas Físicas — Régimen General)

| Lower Limit (MXN) | Upper Limit (MXN) | Fixed Fee | Rate on Excess |
|---|---|---|---|
| 0.01 | 8,952.49 | 0 | 1.92% |
| 8,952.50 | 75,984.55 | 171.88 | 6.40% |
| 75,984.56 | 133,536.07 | 4,461.94 | 10.88% |
| 133,536.08 | 155,229.80 | 10,723.55 | 16.00% |
| 155,229.81 | 185,852.57 | 14,194.54 | 17.92% |
| 185,852.58 | 374,837.88 | 19,682.13 | 21.36% |
| 374,837.89 | 590,795.99 | 60,049.40 | 23.52% |
| 590,796.00 | 1,127,926.84 | 110,842.74 | 30.00% |
| 1,127,926.85 | 1,503,902.46 | 271,981.99 | 32.00% |
| 1,503,902.47 | 4,511,707.37 | 392,294.17 | 34.00% |
| Over 4,511,707.38 | — | 1,414,947.85 | 35.00% |

**Formula:** ISR = Fixed Fee + (Gross Income − Lower Limit) × Rate

**Note:** Annual table is published by SAT each year. Monthly pagos provisionales use the monthly equivalent table. Always verify current-year SAT tables.

### RESICO (Régimen Simplificado de Confianza) — Alternative

Professionals with annual gross income ≤ MXN 3,500,000 may use RESICO:

| Annual Income (MXN) | RESICO Rate |
|---|---|
| Up to 300,000 | 1.00% |
| 300,001 – 600,000 | 1.10% |
| 600,001 – 1,000,000 | 1.50% |
| 1,000,001 – 2,500,000 | 2.00% |
| 2,500,001 – 3,500,000 | 2.50% |

**RESICO key features:**
- Rate applied to gross income (no expense deductions)
- Monthly provisional = monthly gross × rate
- No annual Declaración Anual for purely RESICO income (informativa only)
- Cannot combine RESICO with Régimen General in same year for same activity

### Retenciones (Withholding by Clients)

| Client Type | Withholding on Honorarios CFDI |
|---|---|
| Moral (corporation) | 10% ISR + 2/3 of applicable IVA (10.667% of invoice amount) |
| Física (individual) with business activity | Same obligations as Moral |
| Persona Física consumer | No withholding obligation |

Retenciones are credited against the annual ISR balance.

**ISR retenido:** Client withholds 10% on the pre-IVA amount (honorarios brutos). The 10% is an advance payment, not the final rate.

### IVA on Professional Services

Standard IVA rate: **16%**. Not included in ISR computation — IVA is collected and remitted separately. Strip IVA from all income and expense figures for ISR purposes.

### IMSS / ISSSTE Social Security

Personas físicas with actividades profesionales (autónomas) pay IMSS voluntarily (seguro voluntario) or have no mandatory IMSS obligation (unless registered as patron). Mandatory regime applies when they have employees.

Voluntary IMSS contributions: deductible in Declaración Anual as deducciones personales.

### Conservative Defaults

| Situation | Default Assumption |
|---|---|
| RESICO vs. Régimen General unclear | Flag — regime determines entire calculation approach |
| IVA included in income figures | Strip 16% IVA before ISR computation |
| Retention rate unclear (PJ client) | Apply 10% ISR retention as default |
| Deducción autorizada without CFDI | Reject — no CFDI = not deductible under SAT rules |
| Pago provisional amount unknown | Estimate using monthly bracket table; flag for actual |
| Foreign client income (no RFC) | Treat as taxable; no retention from foreign payer; pagos provisionales required |

### Red Flag Thresholds

| Flag | Threshold |
|---|---|
| Gross income > MXN 3,500,000 | RESICO not available — Régimen General mandatory |
| No CFDI emitted for services | SAT audit risk — CFDI de honorarios required for every PJ client |
| No pagos provisionales | Multa and recargos — verify monthly obligations met |
| Cash income without CFDI | Non-deductible for client; high SAT scrutiny for taxpayer |
| Single client > 80% of income | Régimen de asalariados may apply — verify |

---

## Section 2 — Required Inputs + Refusal Catalogue

### Required Inputs

Before computing Mexican ISR, collect:

1. **Total gross income** (ingresos cobrados) — all amounts received, ex-IVA, for the fiscal year
2. **CFDI de honorarios emitidos** — all CFDIs issued to clients (SAT portal or accounting system)
3. **Retenciones comprobantes** — withholding certificates from PJ clients (10% ISR)
4. **Pagos provisionales made** — monthly ISR payments (línea de captura / recibos from SAT)
5. **Deducciones autorizadas** — documented expenses with CFDI de proveedores
6. **Deducciones personales** — medical, dental, hospital, education, mortgage, IMSS voluntary (with CFDI/facturas)
7. **Bank statements** — 12 months of the fiscal year
8. **RFC** — client's Registro Federal de Contribuyentes
9. **Declaración anual prior year** (if available) — to verify prior pagos provisionales and carryforward losses
10. **RESICO status** — confirm if enrolled in RESICO or Régimen de Actividades Empresariales y Profesionales

### Refusal Catalogue

| Code | Situation | Action |
|---|---|---|
| R-MX-1 | Client in RESICO but claims deducciones autorizadas | Stop — RESICO does not allow expense deductions; apply gross income × rate only |
| R-MX-2 | No CFDI for claimed expense > MXN 2,000 | Reject expense — SAT requires CFDI for all deductible expenses; cash payments > MXN 2,000 not deductible |
| R-MX-3 | Income from employment (asalariado) mixed with professional | Flag — empleos simultáneos con honorarios require careful coordination; employer withholds IRPF; consolidated return required |
| R-MX-4 | Foreign-source income without RFC from payer | Treat as taxable; no retention was made; pago provisional required for each month |
| R-MX-5 | Client claiming RIF (Régimen de Incorporación Fiscal) | RIF was abolished January 2022 — now RESICO; stop if client still references RIF |

---

## Section 3 — Transaction Pattern Library

### Income Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| I-01 | `TRANSFERENCIA DE [client]` / `SPEI DE [client]` | Gross income (ex-IVA) | SPEI (Mexican interbank transfer) from client |
| I-02 | `CoDi COBRO [client]` / `CODI PAGO RECIBIDO` | Gross income (ex-IVA) | CoDi (Cobro Digital) QR/NFC payment from client |
| I-03 | `MERCADO PAGO RETIRO` / `MERCADOPAGO DEPOSITO` | Gross income — gross-up | Mercado Pago payout; fee deductible with CFDI |
| I-04 | `STRIPE PAYMENTS MEXICO` / `STRIPE PAYOUT MXN` | Gross income — gross-up | Stripe Mexico payout; require CFDI Stripe Mexico |
| I-05 | `PAYPAL RETIRO` / `PAYPAL TRANSFER` | Gross income — foreign-source or domestic | PayPal payout; classify by payer country; IVA implications |
| I-06 | `DEPOSITO [client]` / `ABONO [client]` | Gross income (ex-IVA) | Generic bank deposit from client |
| I-07 | `RETENCION ISR 10%` (annotation on CFDI) | Tax credit — not income reduction | Withholding by PJ client; gross up received amount |
| I-08 | `DEVOLUCION SAT` / `SALDO A FAVOR ISR` | NOT income — ISR refund | SAT devolution is not income |
| I-09 | `DEPOSITO IVA RETENIDO` (from client) | IVA retention — NOT ISR income | IVA 2/3 retained by PJ is separate from ISR computation |
| I-10 | `ARRENDAMIENTO RECIBIDO` | Rental income — Capítulo III | Separate from Capítulo II professional income |

### Expense Patterns (Deducciones Autorizadas — require CFDI)

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| E-01 | `RENTA OFICINA` / `ARRENDAMIENTO OFICINA` | Rent — deductible (professional use) | Require CFDI arrendamiento from landlord |
| E-02 | `CFE ENERGIA ELECTRICA` / `CFE PAGO` | Utilities — deductible (professional proportion) | CFE = Comisión Federal de Electricidad; require CFDI |
| E-03 | `TELMEX` / `IZZI` / `TOTALPLAY` / `MEGACABLE` | Internet/phone — deductible (professional %) | Require CFDI; document business percentage |
| E-04 | `TELCEL` / `AT&T MEXICO` / `MOVISTAR MEXICO` | Mobile — deductible (professional %) | Require CFDI factura |
| E-05 | `ADOBE` / `MICROSOFT 365` / `GOOGLE WORKSPACE` | Software — deductible | Require CFDI or foreign CFDI equivalent |
| E-06 | `CONTADOR` / `DESPACHO CONTABLE` / `CPA` | Accounting fees — deductible | Require CFDI servicios profesionales |
| E-07 | `AEROMEXICO` / `VOLARIS` / `VIVAAEROBUS` | Air travel — deductible (business) | Require CFDI or factura; business purpose needed |
| E-08 | `HOTEL` / `RESERVACION HOTEL` / `AIRBNB` | Accommodation — deductible (business travel) | Require CFDI; 50% deductible cap for meals (see E-09) |
| E-09 | `RESTAURANTE` / `ALIMENTOS` | Meals — 8.5% deductible cap (Art. 28 LISR) | Limited deduction for consumos en restaurantes: 8.5% of amount |
| E-10 | `COMBUSTIBLE` / `GASOLINA` / `PEMEX` / `OXXO GAS` | Fuel — deductible (vehicle proportion) | Require CFDI; electronic payment only (cash fuel NOT deductible) |
| E-11 | `SEGURO VEHICULO EMPRESARIAL` | Vehicle insurance — deductible (proportion) | Business use proportion |
| E-12 | `PAGO PROVISIONAL ISR SAT` / `LINEA DE CAPTURA` | Pago provisional — NOT deductible | ISR advance payment; not an expense |
| E-13 | `PAGO IVA SAT` | IVA payment — NOT deductible | Separate tax |
| E-14 | `IMSS VOLUNTARIO` | Voluntary IMSS — deducción personal (not autorizada) | Goes in Declaración Anual deducc. personales, not Cap. II |
| E-15 | `CAPACITACION` / `CURSOS` / `DIPLOMADO` | Training — deductible | Require CFDI; professional development |
| E-16 | `PAPELERIA` / `MATERIAL OFICINA` | Office supplies — deductible | Require CFDI; small amounts deductible with CFDI |
| E-17 | `COMISION BANCARIA` / `CUOTA ANUAL TARJETA` | Bank commissions — deductible | Require bank CFDI; professional account fees |

### Deducciones Personales (in Declaración Anual — not Cap. II expenses)

| # | Type | Cap |
|---|---|---|
| DP-01 | Gastos médicos, dentales, hospitalarios | No cap (require CFDI) |
| DP-02 | Primas de seguros de gastos médicos | No cap (require CFDI) |
| DP-03 | Gastos funerarios | Up to 1 UMA × 12 = ~MXN 38,220 |
| DP-04 | Donativos (donations to authorized entities) | Up to 7% of prior-year income |
| DP-05 | Crédito hipotecario interest | Up to 1,500,000 UDIs |
| DP-06 | Colegiaturas (education) | Capped by level: e.g., preparatoria MXN 14,200 |
| DP-07 | Aportaciones voluntarias AFORE | Up to 10% of income, max 5 UMA annual |

Total deducciones personales cap: 15% of gross income OR 5 UMA anual (MXN ~159,200), whichever is lower.

---

## Section 4 — Worked Examples

### Example 1 — BBVA México (CDMX, Marketing Consultant — Régimen General)

**Bank:** BBVA Bancomer CoDi/SPEI statement
**Client:** Andrés Torres, marketing consultant, CDMX, Régimen de Actividades Profesionales

```
Fecha;Concepto;Cargo;Abono;Saldo
05/01/2025;SPEI DE EMPRESA ALPHA SA DE CV;;87500.00;
15/01/2025;COMISION BANCARIA;150.00;;
10/02/2025;SPEI DE MARKETING CORP SA;;57500.00;
28/02/2025;TELMEX PAGO;850.00;;
15/03/2025;STRIPE PAYMENTS MEXICO;;34800.00;
01/04/2025;ADOBE CREATIVE CLOUD MEXICO;1250.00;;
20/04/2025;SPEI DE BETA CONSULTORES SC;;69000.00;
15/06/2025;PAGO PROVISIONAL ISR SAT;12500.00;;
10/07/2025;DESPACHO CONTABLE GOMEZ;4640.00;;
10/10/2025;AEROMEXICO MONTERREY;3480.00;;
```

**Step 1 — Income (ex-IVA)**

| Narration | Pattern | Received | IVA (if incl.) | Ex-IVA Gross |
|---|---|---|---|---|
| SPEI DE EMPRESA ALPHA | I-01 | MXN 87,500 | ÷ 1.16 if incl. | MXN 75,431 |
| SPEI DE MARKETING CORP | I-01 | MXN 57,500 | | MXN 49,569 |
| STRIPE PAYMENTS MX | I-04 | MXN 34,800 | gross-up | ~MXN 35,900 |
| SPEI DE BETA CONSULTORES | I-01 | MXN 69,000 | | MXN 59,483 |

Note: If amounts received are already net of IVA that Andrés already remitted to SAT, the ex-IVA gross = CFDI subtotal. Confirm with CFDI records. For simplicity, assume SPEI amounts are already net received after clients withheld 10% ISR.

Gross income from CFDIs (annualised): MXN 520,000
IRSR retenido 10% by PJ clients: MXN 52,000

**Step 2 — Deducciones Autorizadas**

| Concept | Amount | Deductible |
|---|---|---|
| TELMEX (80% business) | MXN 10,200/yr × 80% = MXN 8,160 | MXN 8,160 |
| ADOBE | MXN 15,000/yr | MXN 15,000 |
| DESPACHO CONTABLE | MXN 55,680/yr | MXN 55,680 |
| AEROMEXICO (business trip) | MXN 3,480 | MXN 3,480 |
| COMISION BANCARIA | MXN 1,800/yr | MXN 1,800 |
| STRIPE FEES | ~MXN 1,100 | MXN 1,100 |
| PAGO PROVISIONAL ISR | MXN 12,500 | MXN 0 |
| **Total deducciones** | | **MXN 85,220** |

**Step 3 — Taxable Income (Base ISR)**

```
Gross income:         MXN 520,000
Less deducciones:     MXN  85,220
Taxable income:       MXN 434,780
```

**Step 4 — ISR**

```
Bracket: MXN 374,837.89 – MXN 590,795.99
Fixed fee:         MXN 60,049.40
(434,780 − 374,837.89) × 23.52% = MXN 59,942.11 × 23.52% = MXN 14,098.58
ISR gross:         MXN 74,147.98

Less retenciones:  MXN 52,000
Less pagos provisionales: MXN 12,500 × months
ISR balance:       MXN 74,147.98 − MXN 52,000 − MXN [provisional total]
```

---

### Example 2 — Santander México (Guadalajara, Developer — RESICO)

**Bank:** Santander Cuenta Digital
**Client:** Sofía Ramírez, software developer, Guadalajara, enrolled in RESICO

Gross income (all CFDI invoiced): MXN 480,000 (ex-IVA)
RESICO bracket: MXN 300,001–600,000 → 1.10%

Annual ISR RESICO: MXN 480,000 × 1.10% = **MXN 5,280**

Key points:
- No deducciones autorizadas allowed under RESICO
- Monthly pago provisional: (monthly income) × 1.10% via SAT portal
- No Declaración Anual required (informativa only)
- IVA still applies separately (collect 16%, remit to SAT)

---

### Example 3 — Banamex / Citibanamex (Monterrey, Architect)

**Bank:** Banamex statement
**Client:** Ricardo Vega, architect, Monterrey, Régimen General

Complex deductions:
- Studio rent (commercial): MXN 84,000/yr → require CFDI arrendamiento
- AutoCAD / BIM software: MXN 18,000 → CFDI
- Subcontractor (structural engineer): MXN 120,000 → require CFDI honorarios

Gross income: MXN 800,000
Total deductions: MXN 300,000 (including subcontractor)
Taxable: MXN 500,000

ISR: MXN 60,049.40 + (MXN 500,000 − MXN 374,837.89) × 23.52%
= MXN 60,049.40 + MXN 125,162.11 × 23.52%
= MXN 60,049.40 + MXN 29,438.13 = **MXN 89,487.53**

Flag: Subcontractor paid MXN 120,000 — did Ricardo issue CFDI to subcontractor? If subcontractor has RFC and Andrés is acting as client, no issue. But if Ricardo paid as employer, IMSS and payroll taxes may apply.

---

### Example 4 — HSBC México (CDMX, Consultant with Foreign Clients)

**Bank:** HSBC Advance statement
**Client:** Laura Pérez, management consultant, CDMX, 40% of income from US clients (USD)

US client income: USD 24,000 → at SAT exchange rate (~MXN 17.50) = MXN 420,000
Note: No ISR retention made by US client. Laura must pay pagos provisionales on this income each month.

Domestic PJ income: MXN 280,000 (with 10% retention = MXN 28,000 withheld)

Total gross: MXN 700,000
Deducciones: MXN 95,000
Taxable: MXN 605,000

ISR: MXN 110,842.74 + (MXN 605,000 − MXN 590,796) × 30% = MXN 110,842.74 + MXN 4,261.20 = **MXN 115,103.94**

Foreign tax credit: If US withholding tax was paid, may credit against Mexican ISR (Art. 5 LISR). Flag for treaty review.

---

### Example 5 — Banorte (Puebla, Physician)

**Bank:** Banorte statement
**Client:** Dr. Martín Cruz, physician, Puebla, hospital PJ fees + private patients (PF)

Hospital PJ (CFDI emitidos): MXN 360,000; 10% ISR retenido = MXN 36,000
Private patients (PF — no retention): MXN 120,000 — pagos provisionales required

Total gross: MXN 480,000
Deductions: consulting room rent MXN 36,000, medical equipment depreciation MXN 24,000, professional insurance MXN 8,400, accounting MXN 18,000 = MXN 86,400

Taxable: MXN 480,000 − MXN 86,400 = MXN 393,600

ISR: MXN 60,049.40 + (MXN 393,600 − MXN 374,837.89) × 23.52%
= MXN 60,049.40 + MXN 18,762.11 × 23.52% = MXN 60,049.40 + MXN 4,413.85 = **MXN 64,463.25**

Deducciones personales: gastos médicos propios MXN 12,000 + colegiaturas hijo MXN 8,900 = MXN 20,900 (reduces ISR ~ MXN 4,000 at marginal rate).

---

### Example 6 — Nu México / Hey Banco (CDMX, Freelance Designer)

**Bank:** Nu México statement (digital bank)
**Client:** Valentina Cruz, graphic designer, CDMX, multiple small PF clients + one PJ

Nu México narrations:
- `Transferencia recibida de [client name]` — PF clients
- `SPEI recibido de EMPRESA X SA DE CV` — PJ client

PF income (no retention): MXN 90,000 — pagos provisionales required monthly
PJ income (10% retention): MXN 60,000; retention = MXN 6,000

Total gross: MXN 150,000
RESICO check: MXN 150,000 < MXN 3,500,000 → RESICO available
RESICO rate at MXN 150,000: 1.00%
RESICO ISR: MXN 150,000 × 1.00% = **MXN 1,500**

vs. Régimen General:
Deductions ~MXN 20,000; taxable MXN 130,000
ISR (bracket MXN 133,536.08 at 16%): MXN 10,723.55 + (130,000 − 133,536 → below bracket; use MXN 75,984.56–133,536.07 at 10.88%): MXN 4,461.94 + (MXN 130,000 − MXN 75,984.56) × 10.88% = MXN 4,461.94 + MXN 5,872.61 = MXN 10,334.55 − retención MXN 6,000 = MXN 4,334.55

RESICO (MXN 1,500) significantly better → recommend RESICO (client must be formally enrolled).

---

## Section 5 — Tier 1 Rules (Apply Directly)

**T1-MX-1 — Always strip IVA before ISR computation**
Mexican professional services carry 16% IVA. All income and expense figures for ISR purposes must be ex-IVA (subtotal on CFDI). IVA is collected and remitted separately. Never include IVA in ISR base calculations.

**T1-MX-2 — No CFDI = no deduction**
Under LISR, deductible expenses require a valid CFDI (Comprobante Fiscal Digital por Internet) from the supplier with the taxpayer's RFC. Cash payments > MXN 2,000 are explicitly non-deductible. Reject any expense claim without a CFDI.

**T1-MX-3 — RESICO prohibits expense deductions**
RESICO applies a flat rate to gross income without any deductions. Never apply deducciones autorizadas to a RESICO taxpayer. The two regimes are mutually exclusive for the same activity in the same year.

**T1-MX-4 — 10% ISR retenido is a credit, not income reduction**
Clients withholding 10% ISR on honorarios CFDI do not reduce the taxpayer's gross income — they reduce the final tax balance payable. Always gross up received amounts by the 10% retention to compute the income figure, then credit the retention against annual ISR.

**T1-MX-5 — Meals deduction: 8.5% cap**
Restaurant consumption (consumos en restaurantes) deductible at only 8.5% of the CFDI amount (Art. 28 LISR). Apply 8.5% to all restaurant narrations where a CFDI exists. Never apply 100% to meals.

**T1-MX-6 — Fuel: electronic payment mandatory**
Gasoline and diesel expenses are only deductible when paid electronically (CFDI with electronic payment method). Cash fuel purchases are explicitly disallowed. Apply zero deduction to any fuel expense that appears to be a cash purchase.

**T1-MX-7 — Pagos provisionales are not deductible**
Monthly ISR advance payments made to SAT (línea de captura / complemento de pago) are not deductible expenses. They are credits against the annual tax balance.

---

## Section 6 — Tier 2 Catalogue (Reviewer Judgement Required)

| Code | Situation | Escalation Reason | Suggested Treatment |
|---|---|---|---|
| T2-MX-1 | RESICO vs. Régimen General comparison | Regime choice has major tax impact; cannot be changed mid-year | Present both calculations; advise formal enrollment at SAT for following year |
| T2-MX-2 | Foreign income without retention | No ISR withheld by foreign payer; pago provisional required each month on that income | Compute pagos provisionales on foreign income; flag FX conversion (SAT rates) |
| T2-MX-3 | Subcontractor payments (honorarios a terceros) | If paying a freelancer > MXN 2,000, client must issue CFDI and subcontractor is obligated to emit CFDI | Flag — verify CFDI chain; both CFDIs must exist for the deduction |
| T2-MX-4 | Rental income (arrendamiento) alongside professional | Capítulo III income; different pago provisional regime and deductions | Flag — separate the two income streams in Declaración Anual |
| T2-MX-5 | Vehicle expenses (deducción de automóvil) | Cars deductible up to MXN 175,000 purchase value; annual depreciation 25%; strict fuel rules | Flag — vehicle deduction calculations require SAT-compliant depreciation schedule |
| T2-MX-6 | Prior-year tax losses (pérdidas fiscales) | Losses can offset income for up to 10 years with inflation adjustment | Flag — review prior-year declaraciones for carryforward losses |

---

## Section 7 — Excel Working Paper Template

```
MEXICAN ISR WORKING PAPER (PERSONA FÍSICA — ACTIVIDADES PROFESIONALES)
Taxpayer: _______________  RFC: _______________  FY: 2025

SECTION A — INCOME (INGRESOS COBRADOS, EX-IVA)
                                        MXN
Domestic PJ clients (CFDI issued):    ___________
Domestic PF clients (pagos provisionales): ________
Foreign income (converted at SAT rate): ___________
Platform payouts (grossed up, ex-IVA): ___________
TOTAL GROSS INCOME                     ___________

SECTION B — DEDUCCIONES AUTORIZADAS (LISR Art. 105)
(Only for Régimen General — NOT for RESICO)
Office rent (CFDI required):           ___________
Utilities (business proportion, CFDI): ___________
Phone/internet (%, CFDI):              ___________
Software subscriptions (CFDI):         ___________
Accounting/legal fees (CFDI):          ___________
Air travel (CFDI, business purpose):   ___________
Accommodation (CFDI):                  ___________
Restaurant meals (8.5% of CFDI):       ___________
Fuel (electronic payment only, CFDI):  ___________
Vehicle depreciation (to MXN 175k cap):___________
Training/CPD (CFDI):                   ___________
Office supplies (CFDI):                ___________
Bank commissions (CFDI):               ___________
Subcontractor payments (CFDI):         ___________
TOTAL DEDUCCIONES                      ___________

SECTION C — ISR BASE
Gross income − Deducciones             ___________

SECTION D — ISR CALCULATION (Régimen General)
ISR at bracket rates:                  ___________
RESICO check (if applicable):          ___________

SECTION E — TAX CREDITS
ISR retenido (10% by PJ clients):      (___________)
Pagos provisionales paid:              (___________)
ISR BALANCE DUE / (REFUND)             ___________

SECTION F — DEDUCCIONES PERSONALES (Declaración Anual)
Medical/dental/hospital (CFDI):        ___________
Medical insurance (CFDI):              ___________
Education/colegiaturas (CFDI):         ___________
Other personales:                      ___________
Cap check (15% of gross or 5 UMA):     ___________

SECTION G — REVIEWER FLAGS
[ ] IVA stripped from all income/expense figures?
[ ] CFDI verified for every deducción autorizada?
[ ] Cash fuel purchases excluded (non-deductible)?
[ ] Restaurant meals limited to 8.5%?
[ ] RESICO vs. Régimen General comparison done?
[ ] Retenciones certificates collected from all PJ clients?
[ ] Pagos provisionales reconciled vs. SAT account?
[ ] Foreign income converted at SAT publication rate?
[ ] CFDI de honorarios emitidos match total income?
```

---

## Section 8 — Bank Statement Reading Guide

### BBVA México
- Export: CSV/Excel via "Mis Finanzas" → "Descargar movimientos"
- Columns: `Fecha;Concepto;Cargo;Abono;Saldo`
- Amount format: no thousands separator, period decimal (varies) or comma depending on locale
- Date: DD/MM/YYYY
- SPEI credits: `SPEI DE [RFC/name] [reference]`; CoDi: `CoDi COBRO`

### Santander México
- Export: CSV/PDF from Santander Online
- Columns: `Fecha;Descripción;Monto;Saldo`
- Positive Monto = credit; negative = debit (or separate columns)
- SPEI narrations: `TRANSF SPEI DE [name]`

### Banamex (Citibanamex)
- Export: PDF or XLS from Banca en Línea
- Columns: `Fecha;Descripción;Retiros;Depósitos;Saldo`
- Deposits = credits; Retiros = debits

### Banorte
- Export: CSV/Excel from Banorte En Línea
- Standard format: `Fecha;Movimiento;Cargo;Abono;Saldo`

### HSBC México
- Export: CSV from HSBC Personal Banking portal
- Columns: `Fecha;Descripción;Débitos;Créditos;Saldo`

### Nu México (Nubank México)
- Export: CSV from Nu app ("Movimientos" → export)
- Simple format: `Fecha,Descripción,Valor`
- Positive = credit; negative = debit; period decimal

### Hey Banco / Clip / Konfio (digital banks)
- Export varies; typically CSV with `Fecha;Concepto;Monto;Tipo` (CARGO/ABONO)

### CFDI Cross-Reference
Always cross-reference bank statement credits with CFDI de ingresos in SAT portal:
- SAT Portal: cfdiv4.sat.gob.mx → "Factura Electrónica" → "Consultar CFDI emitidos"
- Confirm total CFDI subtotals (ex-IVA) = bank statement gross receipts
- Gaps may indicate income received outside CFDI obligations

---

## Section 9 — Onboarding Fallback

**RESICO vs. Régimen General:**
> "Before I compute your ISR, I need to confirm which regime you are in: RESICO (Régimen Simplificado de Confianza) or Régimen de Actividades Empresariales y Profesionales (Régimen General). RESICO applies a flat rate to gross income (no expense deductions), while Régimen General allows deductions but uses higher rates. If your annual income is below MXN 3,500,000, both may be available. Check your RFC status on the SAT portal to confirm your current enrollment."

**Missing CFDI:**
> "To deduct any expense under Mexican tax law, a valid CFDI (Comprobante Fiscal Digital por Internet) is mandatory. For each expense you want to deduct, please provide the CFDI PDF or XML. Without a CFDI, the expense cannot be included regardless of the bank statement entry. Cash payments above MXN 2,000 are specifically excluded by LISR."

**No pagos provisionales:**
> "Personas físicas with actividades profesionales must make monthly advance ISR payments (pagos provisionales) by the 17th of each following month. Do you have confirmation of payments made on your SAT account? If payments were missed, we need to calculate the recargos (interest) and multas that apply. You can check your SAT account at satid.sat.gob.mx."

**Foreign income:**
> "I see payments from foreign clients. These amounts must be: (1) converted to MXN at the SAT-published exchange rate for the date of each receipt, and (2) included in monthly pagos provisionales since the foreign payer does not withhold Mexican ISR. Do you have bank records showing the MXN equivalent received, or can you provide the dates and foreign currency amounts?"

---

## Section 10 — Reference Material

### Key Legislation
- **LISR (Ley del Impuesto Sobre la Renta)** — Mexican income tax law; Capítulo II (actividades empresariales y profesionales), Capítulo IX (RESICO)
- **LISR Art. 28** — non-deductible expenses (meals cap, fuel rules, etc.)
- **LISR Art. 105** — deductible expenses for professionals
- **Resolución Miscelánea Fiscal 2025** — annual SAT administrative rules

### Filing Deadlines 2025 (FY 2024)
| Deadline | Event |
|---|---|
| Day 17 of each month | Pago provisional ISR for prior month |
| Day 17 of each month | IVA monthly payment |
| 30 April 2025 | Declaración Anual PF 2024 (Régimen General) |
| 30 April 2025 | SAT provides pre-filled proposal in portal |
| Automatic (RESICO) | No Declaración Anual required; informativa if applicable |

### Useful References
- SAT Portal: sat.gob.mx
- Mi Portal SAT: portalsat.plataforma.sat.gob.mx
- CFDI validation: verificacfdi.facturaelectronica.sat.gob.mx
- Exchange rates (SAT): sat.gob.mx/consultas/18038/consulta-de-tipo-de-cambio
- RESICO enrollment: sat.gob.mx → "Trámites" → "RFC y obligaciones"
