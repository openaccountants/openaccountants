---
name: cl-income-tax
description: >
  Use this skill whenever asked about Chilean income tax for self-employed individuals (trabajadores independientes / trabajadores a honorarios). Trigger on phrases like "Impuesto Global Complementario", "Operación Renta", "boleta de honorarios", "trabajador independiente", "PPM", "retención honorarios", "gastos presuntos", "segunda categoría", "Formulario 22", "SII", "RUT Chile", "cotizaciones previsionales", "APV", or any question about filing or computing income tax for a self-employed or independent worker in Chile. This skill covers Impuesto Global Complementario (progressive 0-40%), honorarios withholding, PPM credits, gastos efectivos vs presuntos, cotizaciones previsionales, and SII filing. ALWAYS read this skill before touching any Chilean income tax work.
version: 2.0
---

# Chilean Income Tax — Trabajador Independiente / Honorarios (IGC) v2.0

## Section 1 — Quick Reference

### Impuesto Global Complementario (IGC) — Tax Year 2025 (Año Tributario 2025)

The IGC uses UTA (Unidad Tributaria Anual) as the reference unit. The December 2024 UTA was approximately CLP 807,528. Always verify at www.sii.cl.

| Taxable Income (UTA) | Approx CLP (at UTA 807,528) | Rate | Amount to Deduct (UTA) |
|---|---|---|---|
| 0 -- 13.5 UTA | 0 -- 10,901,628 | Exempt (0%) | -- |
| 13.5 -- 30 UTA | 10,901,629 -- 24,225,840 | 4% | 0.54 UTA |
| 30 -- 50 UTA | 24,225,841 -- 40,376,400 | 8% | 1.74 UTA |
| 50 -- 70 UTA | 40,376,401 -- 56,526,960 | 13.5% | 4.49 UTA |
| 70 -- 90 UTA | 56,526,961 -- 72,677,520 | 23% | 11.14 UTA |
| 90 -- 120 UTA | 72,677,521 -- 96,903,360 | 30.4% | 17.80 UTA |
| 120 -- 310 UTA | 96,903,361 -- 250,333,680 | 35% | 23.26 UTA |
| 310+ UTA | 250,333,681+ | 40% | 38.76 UTA |

Formula: IGC = (Taxable Income in UTA x Rate) - Amount to Deduct in UTA, then convert to CLP

WARNING: UTA values change monthly. Always use the December UTA of the tax year at www.sii.cl.

### Honorarios Withholding Rate Phase-In

| Year | Withholding Rate |
|---|---|
| 2024 | 13.75% |
| 2025 | 14.5% |
| 2026 | 15.25% |
| 2027 | 16% |
| 2028+ | 17% |

### Gastos Presuntos (Deemed Expenses)

| Rule | Detail |
|---|---|
| Rate | 30% of gross honorarios |
| Annual cap | 15 UTA (~CLP 12,112,920 at UTA 807,528) |
| Documentation | No receipts required |

### Gastos Efectivos (Actual Expenses)

| Rule | Detail |
|---|---|
| Rate | Actual documented expenses |
| Cap | No cap — must pass "necessary for income production" test |
| Documentation | Full receipts, facturas, boletas required |

### Cotizaciones Previsionales (Mandatory Social Security)

| Contribution | Approximate Rate | Base |
|---|---|---|
| AFP (pension) | ~11.5-12.5% (incl. commission) | 80% of gross honorarios |
| Salud (Fonasa 7% or Isapre) | 7% minimum | 80% of gross honorarios |
| SIS (disability/survivors) | ~1.85% | 80% of gross honorarios |
| ATEP (work accident) | ~0.93% | 80% of gross honorarios |

### Computation Structure

| Step | Description |
|---|---|
| A | Honorarios brutos (gross boleta income) |
| B | Less: Cotizaciones previsionales obligatorias |
| C | Less: Gastos (presuntos 30% capped at 15 UTA, or efectivos) |
| D | Renta neta (A minus B minus C) |
| E | Add: Other income (employment, rental, dividends, interest) |
| F | Renta neta global |
| G | Less: APV Régimen A deduction (if applicable) |
| H | Base imponible IGC |
| I | Apply IGC progressive table |
| J | Less: PPM credit (withholdings on boletas) |
| K | Less: Other credits (education, donations) |
| L | Tax due / (refund) |

### Conservative Defaults

| Situation | Default Assumption |
|---|---|
| Gastos presuntos vs efectivos unclear | STOP — choice fundamentally changes computation |
| UTA value uncertain | Verify December UTA at www.sii.cl |
| Withholding rate unknown | Use 14.5% for 2025 boletas |
| Gastos efectivos without documentation | Reject — only documented expenses qualify |
| APV regime (A vs B) unclear | Do NOT apply deduction — flag for reviewer |
| Cotizaciones not provided | Estimate at standard rates on 80% gross; flag |

### Red Flag Thresholds

| Flag | Threshold |
|---|---|
| Gastos presuntos hit 15 UTA cap | Compare with gastos efectivos |
| No Formulario 29 payments (self-withholding) | If boletas issued to individuals, self-withholding required |
| No cotizaciones paid | Verify — mandatory under Ley 21.133 |
| Single client > 80% of income | Employment relationship risk |
| UTA applied from wrong month | Always use December UTA |

---

## Section 2 — Required Inputs + Refusal Catalogue

### Required Inputs

Before computing Chilean IGC, collect:

1. **Type of independent work** — trabajador a honorarios, empresario individual, sociedad
2. **Gross annual honorarios** — total bruto from boletas issued
3. **Expense method** — gastos efectivos or gastos presuntos
4. **Cotizaciones previsionales paid** — AFP, salud, SIS, ATEP
5. **PPM withheld** — withholding on boletas during the year
6. **Other income sources** — employment, rental, dividends, interest
7. **APV contributions** — Ahorro Previsional Voluntario (Régimen A or B)
8. **RUT** — tax identification number
9. **Bank statements** — 12 months of the fiscal year
10. **Prior-year Formulario 22** — for carryforward verification

### Refusal Catalogue

| Code | Situation | Action |
|---|---|---|
| R-CL-1 | Expense method unknown | Stop — gastos presuntos vs efectivos fundamentally changes computation |
| R-CL-2 | Gastos efectivos claimed without documentation | Reject — SII requires facturas/boletas for all deductible expenses |
| R-CL-3 | Client references RIF regime | Stop — RIF does not exist in Chile; clarify regime |
| R-CL-4 | Mixed employment + honorarios without breakdown | Flag — both incomes aggregate in IGC; need separate figures |
| R-CL-5 | Foreign-source income with treaty implications | Escalate — Chile has extensive treaty network; requires analysis |

---

## Section 3 — Transaction Pattern Library

### 3.1 Income Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| I-01 | `TRANSFERENCIA DE [client]` / `TRF TEF [client]` | Gross income — honorarios | Standard TEF (inter-bank transfer) from client |
| I-02 | `ABONO TRANSFERENCIA [client]` | Gross income — honorarios | Generic bank credit from client |
| I-03 | `MERCADOPAGO RETIRO` / `MERCADOPAGO DEPOSITO` | Gross income — gross-up | Mercado Pago settlement; fee deductible |
| I-04 | `STRIPE PAYOUT CLP` / `STRIPE PAYMENTS` | Gross income — gross-up | Stripe payout; classify by payer country |
| I-05 | `PAYPAL RETIRO` / `PAYPAL TRANSFERENCIA` | Gross income — foreign source if from abroad | PayPal withdrawal; flag FX conversion |
| I-06 | `WEBPAY ABONO` / `TRANSBANK ABONO` | Gross income — gross-up | Transbank/Webpay card payment settlement |
| I-07 | `BOLETA HONORARIOS [number]` | Gross income (cross-ref with SII) | If narration references boleta number |
| I-08 | `DEVOLUCIÓN SII` / `REINTEGRO RENTA` | NOT income — tax refund | Operación Renta refund |
| I-09 | `INTERESES DEPÓSITO` / `RENDIMIENTO FONDO` | Financial income | Interest/fund returns; separate treatment |
| I-10 | `ARRIENDOS COBRADOS` | Rental income | Separate IGC category |

### 3.2 Expense Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| E-01 | `ARRIENDO OFICINA` / `ARRENDAMIENTO COMERCIAL` | Rent — deductible (gastos efectivos) | Require factura/boleta |
| E-02 | `ENEL CHILE` / `CGE` / `SAESA` / `CHILQUINTA` | Electricity — deductible (business proportion) | Require boleta/factura |
| E-03 | `ENTEL` / `MOVISTAR CHILE` / `CLARO CHILE` / `WOM` | Phone/internet — deductible (business %) | Require boleta/factura |
| E-04 | `VTR` / `GTD` / `TELSUR` | Internet/TV — deductible (business %) | Require factura |
| E-05 | `ADOBE` / `MICROSOFT 365` / `GOOGLE WORKSPACE` | Software — deductible | Professional tools |
| E-06 | `CONTADOR` / `ESTUDIO CONTABLE` / `AUDITOR` | Accounting fees — deductible | Require boleta de honorarios |
| E-07 | `LATAM AIRLINES` / `SKY AIRLINE` / `JETSMART` | Air travel — deductible (business purpose) | Document purpose |
| E-08 | `HOTEL` / `BOOKING.COM` / `AIRBNB` | Accommodation — deductible (business travel) | Business purpose required |
| E-09 | `AFP [name]` / `COTIZACIÓN AFP` | Pension contribution — deductible | Mandatory cotización previsional |
| E-10 | `FONASA` / `ISAPRE [name]` / `COTIZACIÓN SALUD` | Health contribution — deductible | Mandatory cotización |
| E-11 | `PPM SII` / `FORMULARIO 29` / `PAGO PROVISIONAL` | Tax prepayment — NOT deductible | Credit against annual IGC |
| E-12 | `IMPUESTO RENTA` / `PAGO F22` | Annual tax payment — NOT deductible | Tax payment |
| E-13 | `COMBUSTIBLE` / `COPEC` / `SHELL` / `PETROBRAS` | Fuel — deductible (business proportion) | Document business use |
| E-14 | `INSUMOS OFICINA` / `LIBRERÍA` | Office supplies — deductible | Require boleta |
| E-15 | `CAPACITACIÓN` / `CURSO` / `DIPLOMADO` | Training — deductible | Professional development |
| E-16 | `COMISIÓN BANCARIA` / `MANTENCIÓN CUENTA` | Bank fees — deductible | Business account fees |
| E-17 | `APV [fund name]` / `AHORRO PREVISIONAL` | Voluntary pension — Régimen A or B | Régimen A: deductible; B: not deductible but 15% state bonus |

### 3.3 Bank Fees and Financial (Exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BANCOESTADO | EXCLUDE for bank charges | Financial service |
| BCI, BANCO DE CRÉDITO | EXCLUDE for bank charges | Financial service |
| SANTANDER CHILE | EXCLUDE for bank charges | Financial service |
| BANCO DE CHILE, BCHILE | EXCLUDE for bank charges | Financial service |
| SCOTIABANK CHILE | EXCLUDE for bank charges | Financial service |
| MACH, TENPO, FINTUAL | EXCLUDE for fintech fees | Check for separate taxable items |
| INTERESES CRÉDITO, DIVIDENDO HIPOTECARIO | EXCLUDE | Loan interest — not IGC deductible for self-employment |

### 3.4 Government and Statutory (Exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| SII, SERVICIO IMPUESTOS INTERNOS | EXCLUDE | Tax authority payment |
| TESORERÍA GENERAL | EXCLUDE | Treasury payment |
| MUNICIPALIDAD, PATENTE MUNICIPAL | EXCLUDE | Municipal licence (separate from IGC) |

### 3.5 Internal Transfers and Exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| TRASPASO ENTRE CUENTAS | EXCLUDE | Internal movement |
| GIRO ATM, RETIRO EFECTIVO | TIER 2 — ask | Default exclude; ask purpose |
| CRÉDITO HIPOTECARIO | EXCLUDE | Mortgage payment, out of scope |

---

## Section 4 — Worked Examples

### Example 1 — BancoEstado (Santiago, IT Consultant — Gastos Presuntos)

**Bank:** BancoEstado statement
**Client:** Pablo Muñoz, IT consultant, Santiago, trabajador a honorarios

```
Fecha;Descripción;Cargo;Abono;Saldo
05/01/2025;TRANSFERENCIA DE EMPRESA ALPHA SPA;;2.500.000;
15/01/2025;COMISIÓN MANTENCIÓN;3.500;;
10/02/2025;TRANSFERENCIA DE BETA TECH SPA;;1.800.000;
28/02/2025;COTIZACIÓN AFP HABITAT;185.000;;
15/03/2025;STRIPE PAYOUT CLP;;980.000;
31/03/2025;PPM FORMULARIO 29;145.000;;
20/04/2025;TRANSFERENCIA DE GAMMA LTDA;;3.200.000;
10/07/2025;ESTUDIO CONTABLE SILVA;250.000;;
```

**Step 1 — Income Classification**

All transfers from clients = gross honorarios. Annualised gross: CLP 25,000,000 (example).
Withholding at 14.5%: CLP 3,625,000 withheld by corporate clients (PPM credit).

**Step 2 — Gastos Presuntos**

30% x CLP 25,000,000 = CLP 7,500,000. Cap = 15 UTA = CLP 12,112,920. Under cap — apply CLP 7,500,000.

**Step 3 — Cotizaciones**

Approx CLP 2,500,000 deducted from withholding for AFP + salud + SIS.

**Step 4 — IGC Computation**

```
Gross honorarios:        CLP 25,000,000
Less cotizaciones:       CLP  2,500,000
Less gastos presuntos:   CLP  7,500,000
Renta neta:              CLP 15,000,000
```

At UTA 807,528: CLP 15,000,000 = ~18.6 UTA
IGC: first 13.5 UTA exempt. 13.5-18.6 UTA at 4%.
Tax = (18.6 - 13.5) x 4% x 807,528 = 5.1 x 0.04 x 807,528 = ~CLP 164,736

PPM credit: CLP 3,625,000 - cotizaciones = ~CLP 1,125,000 remaining as PPM.
Result: CLP 164,736 - CLP 1,125,000 = **refund ~CLP 960,264**

### Example 2 — BCI (Valparaíso, Architect — Gastos Efectivos)

**Bank:** BCI statement
**Client:** Sofía Araya, architect, Valparaíso, high expenses

Gross honorarios: CLP 45,000,000
Gastos efectivos (documented): studio rent CLP 7,200,000, software CLP 2,400,000, subcontractors CLP 8,000,000, travel CLP 1,800,000 = CLP 19,400,000

Compare: gastos presuntos = 30% x 45M = CLP 13,500,000 (capped at 15 UTA = CLP 12,112,920).
Gastos efectivos (CLP 19,400,000) > presuntos cap (CLP 12,112,920) — **use efectivos**.

Renta neta: CLP 45,000,000 - cotizaciones - CLP 19,400,000 = ~CLP 21,100,000
IGC at higher brackets. PPM and cotizaciones as credits.

### Example 3 — Santander Chile (Santiago, Low-Income Refund)

**Bank:** Santander Chile
**Client:** Camila Rojas, translator, low income

Gross: CLP 8,000,000. Withholding 14.5% = CLP 1,160,000.
After cotizaciones and gastos presuntos: renta neta below 13.5 UTA.
IGC = CLP 0. Full PPM (after cotizaciones) refunded.

### Example 4 — Banco de Chile (Concepción, Mixed Employment + Honorarios)

**Bank:** Banco de Chile
**Client:** Andrés Soto, engineer, employed + freelance

Employment income: CLP 20,000,000 (employer withholds PAYE).
Honorarios: CLP 15,000,000 (gastos presuntos).

Both aggregate in IGC. PPM from honorarios + PAYE from employment = total credits.
Flag: mixed income requires careful coordination; verify employment tax withholding.

### Example 5 — Banco BICE (Santiago, Gastos Presuntos Cap Hit)

**Bank:** Banco BICE
**Client:** Roberto Díaz, consultant, high-income

Gross honorarios: CLP 60,000,000.
Gastos presuntos: 30% x 60M = CLP 18,000,000. Cap = 15 UTA = CLP 12,112,920.
Deduction = CLP 12,112,920 (capped). Compare with gastos efectivos — if actual expenses exceed CLP 12M, switch to efectivos.

### Example 6 — Mach / Tenpo (Santiago, Digital Creator)

**Bank:** Mach (BCI digital wallet) / Tenpo
**Client:** Valentina Pérez, digital creator, receives via Stripe and Transbank

Digital bank narrations: `Transferencia recibida`, `Abono TEF`
Stripe: gross-up required for fee deduction.
Total gross: CLP 18,000,000.

At ~22.3 UTA: IGC bracket 13.5-30 UTA at 4%.
PPM credit likely covers entire tax. Probable refund.

---

## Section 5 — Tier 1 Rules (Apply Directly)

**T1-CL-1 — Gastos presuntos capped at 15 UTA**
The 30% deemed expense deduction cannot exceed 15 UTA regardless of how high the gross income is. Always check the cap. Use the December UTA of the tax year.

**T1-CL-2 — Withholding rate is 14.5% for 2025**
Boletas de honorarios issued in 2025 attract a 14.5% withholding. This covers both PPM (income tax advance) and cotizaciones previsionales. Do not use rates from other years.

**T1-CL-3 — PPM is a credit, not income reduction**
The withholding on boletas (after cotizaciones are deducted) is a credit against the annual IGC. It does not reduce gross income. Excess PPM is refunded during Operación Renta.

**T1-CL-4 — Cotizaciones previsionales are mandatory**
Under Ley 21.133, trabajadores a honorarios must contribute to AFP, salud, SIS, and ATEP. Cotizaciones are deducted from the boleta withholding before PPM is calculated. They are deductible from gross income for IGC purposes.

**T1-CL-5 — December UTA only for IGC computation**
The IGC table uses the December UTA of the tax year. Never use January or any other month's UTA. Verify at www.sii.cl.

**T1-CL-6 — Tax payments are not deductible**
PPM payments (Formulario 29) and annual tax payments (Formulario 22 balance) are credits against tax, not deductible expenses.

---

## Section 6 — Tier 2 Catalogue (Reviewer Judgement Required)

| Code | Situation | Escalation Reason | Suggested Treatment |
|---|---|---|---|
| T2-CL-1 | Gastos efectivos with partial documentation | Only documented expenses qualify; undocumented must be removed | Flag — SII audit risk; reviewer must confirm documentation |
| T2-CL-2 | APV Régimen A vs Régimen B choice | Optimal regime depends on marginal IGC rate | Present both options; flag for reviewer |
| T2-CL-3 | Mixed employment and honorarios | Both incomes aggregate in IGC; PPM and PAYE are separate credits | Flag — confirm aggregation and credit coordination |
| T2-CL-4 | Cotizaciones opt-out claim | Workers may opt out only if covered by other source (employment) | Verify eligibility under Ley 21.133 phase-in |
| T2-CL-5 | Foreign-source income | Chilean residents taxed on worldwide income after 3 years | Escalate — treaty analysis may apply |
| T2-CL-6 | Capital gains from investments | Separate IGC treatment under art. 17 No. 8 | Flag — different rates and exemptions apply |

---

## Section 7 — Excel Working Paper Template

```
CHILEAN IGC WORKING PAPER (TRABAJADOR INDEPENDIENTE / HONORARIOS)
Taxpayer: _______________  RUT: _______________  FY: 2025 (Año Tributario 2025)

SECTION A — INCOME (HONORARIOS BRUTOS)
                                        CLP
Boletas de honorarios issued:          ___________
Platform payouts (grossed up):         ___________
Other Categoria B income:              ___________
TOTAL GROSS HONORARIOS                 ___________

SECTION B — COTIZACIONES PREVISIONALES
AFP pension:                           ___________
Salud (Fonasa/Isapre):                ___________
SIS + ATEP:                            ___________
TOTAL COTIZACIONES                     ___________

SECTION C — GASTOS
[ ] Gastos Presuntos: 30% x gross = ___________ (cap 15 UTA = ___________)
[ ] Gastos Efectivos:
  Office rent:                         ___________
  Utilities (business %):              ___________
  Phone/internet:                      ___________
  Software:                            ___________
  Accounting:                          ___________
  Travel:                              ___________
  Subcontractors:                      ___________
  Other documented:                    ___________
  TOTAL GASTOS EFECTIVOS:              ___________
Gastos applied (higher of presuntos or efectivos): ___________

SECTION D — RENTA NETA
Gross - cotizaciones - gastos          ___________

SECTION E — OTHER INCOME
Employment (if any):                   ___________
Rental:                                ___________
Financial:                             ___________
RENTA NETA GLOBAL                      ___________

SECTION F — APV DEDUCTION
Régimen A deduction (if applicable):   ___________
BASE IMPONIBLE IGC                     ___________

SECTION G — IGC COMPUTATION
UTA value (December of tax year):      ___________
Tax per IGC table:                     ___________

SECTION H — CREDITS
PPM withheld (from boletas):           (___________)
PAYE (if employed):                    (___________)
Education / donation credits:          (___________)
IGC BALANCE DUE / (REFUND)            ___________

SECTION I — REVIEWER FLAGS
[ ] Expense method confirmed (presuntos vs efectivos)?
[ ] Gastos presuntos cap checked (15 UTA)?
[ ] December UTA verified at www.sii.cl?
[ ] Withholding rate 14.5% confirmed for 2025?
[ ] Cotizaciones verified against receipts?
[ ] APV regime confirmed (A or B)?
[ ] Boletas electrónicas cross-checked with SII portal?
[ ] Mixed income properly aggregated (if applicable)?
```

---

## Section 8 — Bank Statement Reading Guide

### BancoEstado
- Export: CSV/PDF from BancoEstado Online
- Columns: `Fecha;Descripción;Cargo;Abono;Saldo`
- Amount format: period thousands, comma decimal (e.g., `2.500.000`)
- Date: DD/MM/YYYY
- Credits: `TRANSFERENCIA DE [sender]`, `ABONO TEF [sender]`

### BCI (Banco de Crédito e Inversiones)
- Export: CSV from BCI En Línea
- Columns: `Fecha;Detalle;Cargo;Abono;Saldo`
- Standard Chilean format

### Santander Chile
- Export: CSV/PDF from Santander Online
- Columns: `Fecha;Descripción;Monto;Saldo`
- Positive = credit; negative = debit

### Banco de Chile
- Export: CSV/Excel from Mi Banco en Línea
- Columns: `Fecha;Descripción;Cargo;Abono;Saldo`
- TEF transfers: `TRANSFERENCIA RECIBIDA [sender]`

### Scotiabank Chile
- Export: CSV from Scotiabank Online
- Standard format; `Fecha;Movimiento;Cargo;Abono;Saldo`

### Banco BICE
- Export: PDF/CSV from BICE Online
- Standard Chilean bank format

### Mach / Tenpo / Fintual (Digital)
- Export: CSV/PDF from app
- Simple format; credit/debit in columns or single column (positive/negative)
- Mach (BCI): `Transferencia recibida de [name]`
- Tenpo: `Abono por transferencia`

### Transbank / Webpay Settlements
- Appear in primary bank statement as `TRANSBANK ABONO` or `WEBPAY LIQUIDACIÓN`
- Gross-up required — Transbank deducts commission before settlement
- Cross-reference with Transbank merchant portal for gross amounts

### Key Chilean Banking Notes
- All amounts in CLP (Chilean pesos); period as thousands separator
- TEF (Transferencia Electrónica de Fondos) is the standard inter-bank system
- CuentaRUT (BancoEstado universal account) narrations may differ from full banking narrations

---

## Section 9 — Onboarding Fallback

**Expense method choice:**
> "Before I compute your IGC, I need to know whether you want to use gastos presuntos (deemed 30% deduction, no receipts needed, capped at 15 UTA) or gastos efectivos (actual documented expenses, no cap but requires full receipts). If your actual expenses exceed the presuntos cap (~CLP 12 million), gastos efectivos may save you tax. Which method would you like to use?"

**Cotizaciones verification:**
> "Trabajadores a honorarios are required to make social security contributions (AFP, salud, SIS, ATEP) under Ley 21.133. These are deducted from your boleta withholding. Do you have records of cotizaciones paid? You can check at www.previred.com or your AFP's website."

**PPM reconciliation:**
> "The boleta withholding (14.5% in 2025) covers both cotizaciones and PPM (income tax advance). After cotizaciones are deducted, the remaining amount is your PPM credit against the annual IGC. Do you have your Formulario 29 payment receipts for months where you self-withheld? I need to reconcile total PPM for the year."

**APV regime:**
> "I see you may have voluntary pension contributions (APV). APV Régimen A deducts the contribution from taxable income now (taxed later on withdrawal). Régimen B gives no deduction now but provides a 15% state bonus. The optimal choice depends on your marginal IGC rate. Can you confirm which regime your APV is under?"

---

## Section 10 — Reference Material

### Key Legislation
- **Decreto Ley 824** — Ley sobre Impuesto a la Renta
- **Ley 21.133** — Cotizaciones previsionales obligatorias para trabajadores independientes
- **Código Tributario** — filing deadlines, penalties
- **Circular SII 67/2025** — annual guidance

### Filing Deadlines 2025 (Año Tributario 2025)

| Deadline | Event |
|---|---|
| April 1-30, 2025 | Operación Renta (Formulario 22) |
| 12th of each month | Formulario 29 (monthly self-withholding, if applicable) |
| March 2025 | Declaraciones juradas (informational returns) |
| 30-60 days after filing | Refund payment by SII |

### Penalties

| Offence | Penalty |
|---|---|
| Late filing of F22 | 10% of tax due + 2% per month (up to 30%) |
| Late payment | Interest at 1.5% per month |
| Failure to issue boleta | 50-500% of the boleta amount |
| Incorrect return | 5-20% of tax difference |
| Tax evasion | 50-300% of evaded tax + criminal prosecution |

### Record Keeping
- Minimum retention: 6 years from the tax year
- Boletas electrónicas maintained on SII portal
- All supporting documents (facturas, boletas, contracts, bank statements)

### Useful References
- SII Portal: www.sii.cl
- Operación Renta: www.sii.cl/renta
- Previred (cotizaciones): www.previred.com
- UTA values: www.sii.cl/valores_702/utm_uta_702.html
