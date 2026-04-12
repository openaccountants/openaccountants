---
name: es-estimated-tax
description: >
  Use this skill whenever asked about Spanish estimated income tax payments (pagos fraccionados) for self-employed individuals (autonomos). Trigger on phrases like "Modelo 130", "pagos fraccionados", "estimated tax Spain", "IRPF quarterly", "Spanish advance tax", "autonomo tax payments", "estimacion directa", "Modelo 131", or any question about quarterly income tax prepayment obligations under the IRPF. Covers the quarterly filing schedule (Apr 20, Jul 20, Oct 20, Jan 30), the 20% cumulative computation method, the 70% withholding exemption, penalties for late filing, and payment procedures. ALWAYS read this skill before touching any estimated tax work for Spain.
version: 2.0
jurisdiction: ES
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Spain Estimated Tax (Pagos Fraccionados -- Modelo 130) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Spain |
| Tax | Quarterly IRPF advance payments (pagos fraccionados) |
| Primary legislation | Ley 35/2006 del IRPF, Art. 99.7-99.8; Real Decreto 439/2007 (RIRPF), Arts. 109-112 |
| Supporting legislation | Ley 58/2003 General Tributaria (LGT), Arts. 191-195; Orden EHA/672/2007 |
| Authority | Agencia Estatal de Administracion Tributaria (AEAT) |
| Portal | sede.agenciatributaria.gob.es |
| Currency | EUR only |
| Form | Modelo 130 (estimacion directa); Modelo 131 (estimacion objetiva / modulos) |
| Filing schedule | Quarterly: 1-20 April, 1-20 July, 1-20 October, 1-30 January |
| Computation | 20% of cumulative YTD net income minus retenciones minus prior payments |
| 70% exemption | Profesionales exempt if >= 70% of prior year income had retenciones |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by Spanish asesor fiscal |
| Validation date | Pending |

**Filing schedule summary:**

| Quarter | Period | Deadline |
|---|---|---|
| Q1 (1T) | Jan -- Mar | 1-20 April |
| Q2 (2T) | Apr -- Jun | 1-20 July |
| Q3 (3T) | Jul -- Sep | 1-20 October |
| Q4 (4T) | Oct -- Dec | 1-30 January (next year) |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Modelo 130 vs 131 uncertain | Confirm estimation method -- do not assume |
| 70% exemption status unclear | File Modelo 130 (safer -- exemption must be proven) |
| Cumulative vs quarterly confusion | ALWAYS cumulative YTD -- never quarterly in isolation |
| Low-income deduction eligibility | Check prior year net income against EUR 12,000 threshold |
| New autonomo rate reduction | Flag for reviewer -- confirm eligibility with asesor fiscal |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- cumulative income and expenses YTD, retenciones received YTD, prior quarter Modelo 130 payments made this year.

**Recommended** -- prior year net income (for low-income deduction), prior year retenciones percentage (for 70% exemption test), estimation method confirmation.

**Ideal** -- complete quarterly accounting, all CFDI/invoices, Modelo 130 copies from prior quarters, prior year Renta declaration.

**Refusal policy if minimum is missing -- SOFT WARN.** If YTD figures are unavailable, the 20% computation cannot proceed. Request at minimum a summary of income and expenses.

### Refusal catalogue

**R-ES-ET-1 -- Estimacion objetiva (modulos).** Trigger: client uses modulos. Message: "Clients under estimacion objetiva file Modelo 131, not Modelo 130. The computation uses fixed percentages of modulo amounts. This skill covers Modelo 130 (estimacion directa) only."

**R-ES-ET-2 -- Cross-border income.** Trigger: client has EU/EFTA treaty interactions or is non-resident autonomo. Message: "Cross-border IRPF obligations are outside this skill."

**R-ES-ET-3 -- Empresarial claiming 70% exemption.** Trigger: an empresario (not profesional) claims the withholding exemption. Message: "The 70% exemption applies only to profesionales, not empresarios."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as a Modelo 130 payment.

### 3.1 AEAT quarterly payment debits

| Pattern | Treatment | Notes |
|---|---|---|
| AEAT, AGENCIA TRIBUTARIA | Modelo 130 payment | Match with Apr/Jul/Oct/Jan timing |
| HACIENDA, MINISTERIO DE HACIENDA | Modelo 130 payment | Government payee |
| MODELO 130 | Modelo 130 payment | Explicit form reference |
| PAGO FRACCIONADO, IRPF TRIMESTRAL | Modelo 130 payment | Explicit description |
| DOMICILIACION AEAT | Modelo 130 payment | Direct debit by AEAT |

### 3.2 Timing-based identification

| Debit date range | Likely quarter | Confidence |
|---|---|---|
| 1 April -- 25 April | Q1 (1T) filing | High if payee is AEAT |
| 1 July -- 25 July | Q2 (2T) filing | High |
| 1 October -- 25 October | Q3 (3T) filing | High |
| 1 January -- 5 February | Q4 (4T) filing | High (30 Jan deadline) |

### 3.3 Related but NOT Modelo 130 payments

| Pattern | Treatment | Notes |
|---|---|---|
| IVA, MODELO 303 | EXCLUDE | VAT quarterly payment |
| MODELO 111 | EXCLUDE | Retenciones payment (employer obligation) |
| MODELO 131 | EXCLUDE | Modulos payment (different form) |
| SEGURIDAD SOCIAL, RETA, AUTONOMO CUOTA | EXCLUDE | Social security contribution |
| RENTA, DECLARACION ANUAL | EXCLUDE | Annual return balance payment |
| RECARGO, SANCION | EXCLUDE | Surcharge or penalty |

### 3.4 NRC and payment references

| Reference pattern | Treatment | Notes |
|---|---|---|
| NRC followed by digits | AEAT payment confirmed | Numero de Referencia Completo from bank |
| CSV followed by alphanumeric | Filing receipt reference | Codigo Seguro de Verificacion |
| 130-1T, 130-2T, 130-3T, 130-4T | Modelo 130, specific quarter | Self-identified |

---

## Section 4 -- Worked examples

### Example 1 -- Q2 filing (cumulative Jan-Jun)

**Input:**

| Item | Amount |
|---|---|
| Cumulative income (Jan-Jun) | EUR 30,000 |
| Cumulative expenses (Jan-Jun) | EUR 10,000 |
| Retenciones received YTD | EUR 500 |
| Q1 Modelo 130 payment | EUR 1,500 |

**Computation:**
- Cumulative net income = EUR 30,000 - EUR 10,000 = EUR 20,000
- 20% of net income = EUR 4,000
- Minus retenciones = EUR 4,000 - EUR 500 = EUR 3,500
- Minus Q1 payment = EUR 3,500 - EUR 1,500 = EUR 2,000
- Q2 payment due = EUR 2,000

### Example 2 -- 70% exemption applies

**Input:** Architect with 80% of prior year income subject to retenciones from legal entities.

**Output:** Exempt from Modelo 130 filing. Retenciones serve as advance payments.

### Example 3 -- Negative cumulative result

**Input:** Client has losses YTD. Cumulative net income = negative EUR 3,000.

**Output:** Payment = EUR 0 for the quarter. The loss carries forward in the cumulative computation for subsequent quarters.

### Example 4 -- Low-income deduction

**Input:** Prior year net income = EUR 8,500. Q1 cumulative net income = EUR 5,000.

**Computation:** Prior year below EUR 9,000: quarterly deduction = EUR 100. Payment = (EUR 5,000 x 20%) - EUR 100 = EUR 900.

### Example 5 -- Bank statement classification

**Input line:** `18.04.2025 ; DOMICILIACION AEAT MODELO 130 ; DEBIT ; 1T 2025 ; -1,200.00 ; EUR`

**Classification:** Modelo 130 payment, Q1 (1T) 2025. Income tax advance -- not a deductible business expense.

---

## Section 5 -- Computation rules

### 5.1 The 20% cumulative method

```
cumulative_net_income = total_income_YTD - total_expenses_YTD
gross_payment = cumulative_net_income x 20%
minus_retenciones = withholdings_received_YTD
minus_prior_payments = sum of Modelo 130 payments already made this year
payment_this_quarter = gross_payment - retenciones - prior_payments
if payment_this_quarter < 0: payment = 0 (carries forward)
```

### 5.2 Low-income deduction

| Prior year net income | Quarterly deduction |
|---|---|
| <= EUR 9,000 | EUR 100 |
| EUR 9,000.01 -- EUR 10,000 | EUR 75 |
| EUR 10,000.01 -- EUR 11,000 | EUR 50 |
| EUR 11,000.01 -- EUR 12,000 | EUR 25 |
| > EUR 12,000 | EUR 0 |

### 5.3 Modelo 130 form key lines

| Line | Description |
|---|---|
| 01 | Cumulative net income (ingresos - gastos) |
| 02 | 20% of line 01 |
| 03 | Cumulative retenciones e ingresos a cuenta |
| 04 | Sum of prior quarterly payments |
| 05 | Low-income deduction |
| 07 | Result: line 02 - line 03 - line 04 - line 05 |

### 5.4 The 70% withholding exemption

A profesional (not empresario) is exempt from Modelo 130 if at least 70% of their prior year income was subject to retenciones at source.

### 5.5 New autonomo reduction

In the first year and the following year, new autonomos under estimacion directa may be eligible for a reduced rate. Flag for asesor fiscal to confirm eligibility.

---

## Section 6 -- Penalties and interest

### 6.1 Voluntary late filing surcharges

| Delay | Surcharge (recargo) | Interest |
|---|---|---|
| Within 1 month | 1% | None |
| 1-2 months | 2% | None |
| 2-3 months | 3% | None |
| 3-6 months | 5% | None |
| 6-12 months | 10% | None |
| > 12 months | 15% | + late interest from month 12 |

### 6.2 Late filing after AEAT request

| Severity | Penalty |
|---|---|
| Minor | 50% of unpaid amount |
| Serious | 50-100% |
| Very serious (fraud) | 100-150% |

### 6.3 Late payment interest (interes de demora)

Set annually by the Ley de Presupuestos. 2025 rate: approximately 4.0625% (confirm in annual budget law).

---

## Section 7 -- Filing and payment procedure

### 7.1 Filing methods

| Method | Details |
|---|---|
| Sede Electronica AEAT | Online with certificado digital or Cl@ve |
| PDF Modelo 130 | Download, complete, submit via bank |
| Tax advisor (asesor fiscal) | Files on behalf via AEAT platform |

### 7.2 Payment methods

| Method | Details |
|---|---|
| Domiciliacion bancaria | Direct debit -- set up 5 days before deadline |
| NRC | Pay at bank first, file with NRC code |
| Adeudo en cuenta | Charge to bank account at filing |

Retain the justificante de presentacion with CSV.

---

## Section 8 -- Edge cases

**EC1 -- Negative cumulative result.** Losses YTD: payment = EUR 0. Loss carries forward within cumulative computation for subsequent quarters in the same year.

**EC2 -- Professional exempt from Modelo 130.** Architect with 80% retenciones from prior year. Exempt -- retenciones serve as advance payments.

**EC3 -- Activity started mid-year.** Registered as autonomo in May. First Modelo 130 due Q2 (by 20 July). Covers period from start date only.

**EC4 -- Modelo 131 vs 130 confusion.** Client under estimacion objetiva files Modelo 131, not 130. Different computation method.

**EC5 -- Q4 has longer filing window.** 30 days (1-30 January) vs 20 days for other quarters.

**EC6 -- New autonomo rate reduction.** First year of activity: possible reduced rate between 5% and 20%. Flag for asesor fiscal confirmation.

---

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] Correct modelo identified (130 vs 131)
- [ ] 70% withholding exemption checked for profesionales
- [ ] Cumulative method applied (not quarterly isolated)
- [ ] Prior quarter payments subtracted
- [ ] Low-income deduction applied if eligible
- [ ] Filing deadline correct (20th vs 30th for Q4)
- [ ] New autonomo rate reduction checked
- [ ] Retenciones correctly subtracted
- [ ] Form line references accurate
- [ ] Output labelled as estimated until asesor fiscal confirms

---

## Section 10 -- Test suite

### Test 1 -- Q2 standard computation
**Input:** Cumulative income EUR 30,000. Expenses EUR 10,000. Retenciones EUR 500. Q1 payment EUR 1,500.
**Expected:** Net income EUR 20,000. 20% = EUR 4,000. Minus EUR 500 = EUR 3,500. Minus EUR 1,500 = EUR 2,000.

### Test 2 -- 70% exemption
**Input:** Profesional, 80% of prior year income had retenciones.
**Expected:** Exempt from Modelo 130.

### Test 3 -- Negative result
**Input:** Cumulative net income = negative EUR 3,000.
**Expected:** Payment = EUR 0. Loss carries forward.

### Test 4 -- Low-income deduction
**Input:** Prior year net income EUR 8,500. Q1 net income EUR 5,000.
**Expected:** Deduction EUR 100. Payment = (EUR 5,000 x 20%) - EUR 100 = EUR 900.

### Test 5 -- Activity started mid-year
**Input:** Registered May 2025. Q2 cumulative income (May-Jun) EUR 6,000. Expenses EUR 2,000.
**Expected:** Net EUR 4,000. Payment = EUR 4,000 x 20% = EUR 800. Due by 20 July.

### Test 6 -- Q4 longer deadline
**Input:** Q4 filing for 2025.
**Expected:** Deadline is 30 January 2026 (not 20 January).

---

## Prohibitions

- NEVER compute Modelo 130 using a quarterly (non-cumulative) method -- ALWAYS cumulative YTD
- NEVER forget to subtract prior quarter payments from the cumulative result
- NEVER apply the 70% withholding exemption to empresarios -- only profesionales
- NEVER file Modelo 130 for a client under estimacion objetiva -- they use Modelo 131
- NEVER ignore the low-income deduction for eligible clients
- NEVER present payment amounts as definitive -- advise confirmation with asesor fiscal
- NEVER confuse Q4 deadline (30 Jan) with other quarters (20th)

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
