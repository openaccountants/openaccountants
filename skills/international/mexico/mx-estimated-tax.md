---
name: mx-estimated-tax
description: >
  Use this skill whenever asked about Mexican provisional income tax payments (pagos provisionales de ISR) for self-employed individuals and sole proprietors. Trigger on phrases like "pagos provisionales", "ISR provisional", "estimated tax Mexico", "coeficiente de utilidad", "SAT monthly payment", "declaracion provisional", "Mexican advance tax", "RESICO", or any question about monthly provisional income tax obligations under the Ley del ISR. Covers the monthly payment schedule, cumulative computation method, RESICO simplified rates, penalties for late payment, and SAT filing procedures. ALWAYS read this skill before touching any estimated tax work for Mexico.
version: 2.0
jurisdiction: MX
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Mexico Estimated Tax (Pagos Provisionales de ISR) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Mexico |
| Tax | Monthly provisional income tax payments (pagos provisionales de ISR) |
| Primary legislation | Ley del ISR (LISR), Arts. 106-108 (personas fisicas); Art. 14 (personas morales); Arts. 113-E to 113-J (RESICO) |
| Supporting legislation | Codigo Fiscal de la Federacion (CFF), Arts. 17-A (actualizacion), Art. 21 (recargos) |
| Authority | Servicio de Administracion Tributaria (SAT) |
| Portal | sat.gob.mx |
| Currency | MXN only |
| Payment schedule | Monthly -- by the 17th of the following month |
| Computation | Cumulative YTD for general regime; gross income x fixed rate for RESICO |
| RESICO income limit | MXN 3,500,000 annual |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by Mexican contador publico |
| Validation date | Pending |

**RESICO monthly rate table:**

| Monthly income (MXN) | Rate |
|---|---|
| Up to 25,000 | 1.00% |
| 25,000.01 -- 50,000 | 1.10% |
| 50,000.01 -- 83,333.33 | 1.50% |
| 83,333.34 -- 208,333.33 | 2.00% |
| 208,333.34 -- 3,500,000 | 2.50% |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Regime unclear | Confirm: general, RESICO, or persona moral before computing |
| Cumulative vs monthly isolated | ALWAYS cumulative YTD for general regime |
| Coefficient of utility uncertain | Verify against most recent annual return |
| RESICO threshold exceeded | Switch to general regime immediately |
| CFDI status of expenses | Only deduct with valid CFDI |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- tax regime, monthly/cumulative income and deductible expenses (with CFDI), prior payments made, retenciones received.

**Recommended** -- prior year annual return (for coefficient of utility for personas morales), loss carryforwards, PTU paid.

**Ideal** -- complete monthly accounting with CFDI, prior year Declaracion Anual, SAT portal access for pre-filled data.

**Refusal policy if minimum is missing -- SOFT WARN.** Without income and expense figures, the cumulative computation cannot proceed.

### Refusal catalogue

**R-MX-ET-1 -- Corporate estimated tax (personas morales general).** Trigger: client is a persona moral using coefficient of utility. Message: "Persona moral provisional payments use the coefficient of utility method, which is a Tier 2 computation requiring the prior year annual return. Flag for contador publico."

**R-MX-ET-2 -- Cross-border PE issues.** Trigger: client has establecimiento permanente questions. Message: "Permanent establishment issues are outside this skill."

**R-MX-ET-3 -- Treaty credit timing.** Trigger: cross-border income with treaty interactions. Message: "Treaty credit allocation in provisional payments is outside this skill."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as a provisional ISR payment.

### 3.1 SAT provisional payment debits

| Pattern | Treatment | Notes |
|---|---|---|
| SAT, SERVICIO DE ADMINISTRACION TRIBUTARIA | ISR provisional payment | Match with monthly timing |
| ISR PROVISIONAL, PAGO PROVISIONAL | ISR provisional payment | Explicit description |
| LINEA DE CAPTURA followed by digits | ISR provisional payment | SAT payment reference |
| DECLARACION PROVISIONAL | ISR provisional payment | Filing description |
| HACIENDA, SHCP | ISR provisional payment | Government payee |

### 3.2 Timing-based identification

| Debit date range | Income month covered | Confidence |
|---|---|---|
| 1st -- 20th of month | Prior month income | High if SAT/ISR reference |
| After 17th with surcharge | Late payment | Flag for reviewer |

### 3.3 Related but NOT ISR provisional payments

| Pattern | Treatment | Notes |
|---|---|---|
| IVA, IVA PROVISIONAL | EXCLUDE | VAT provisional payment |
| IMSS, CUOTA OBRERO PATRONAL | EXCLUDE | Social security |
| ISN, IMPUESTO SOBRE NOMINAS | EXCLUDE | Payroll tax |
| ISR RETENIDO, RETENCION ISR | EXCLUDE | Withholding payment (employer) |
| DECLARACION ANUAL | EXCLUDE | Annual return payment |
| RECARGOS, ACTUALIZACION | EXCLUDE | Surcharges/inflation adjustment |
| MULTA SAT | EXCLUDE | Fine |
| PTU | EXCLUDE | Profit sharing payment |

### 3.4 Payment references

| Reference pattern | Treatment | Notes |
|---|---|---|
| Linea de captura + period reference | ISR provisional for that period | Standard SAT format |
| RFC + ISR + month/year | ISR provisional | Self-identified |

---

## Section 4 -- Worked examples

### Example 1 -- General regime cumulative (Q2 month)

**Input:** Cumulative income (Jan-May) = MXN 250,000. Cumulative deductions = MXN 80,000. Retenciones YTD = MXN 5,000. Prior payments (Jan-Apr) = MXN 15,000.

**Computation:**
- Taxable base = MXN 250,000 - MXN 80,000 = MXN 170,000
- Apply cumulative progressive table: find bracket, compute ISR
- Subtract retenciones MXN 5,000
- Subtract prior payments MXN 15,000
- May payment = result

### Example 2 -- RESICO monthly

**Input:** Monthly income = MXN 40,000.

**Computation:** Rate for MXN 25,000.01-50,000 = 1.10%. Payment = MXN 40,000 x 1.10% = MXN 440.

### Example 3 -- Negative cumulative result

**Input:** Cumulative deductions exceed income YTD.

**Output:** No provisional payment due. Loss carries forward in cumulative computation.

### Example 4 -- Bank statement classification

**Input line:** `17.02.2025 ; SAT PAGO PROVISIONAL ISR ENE 2025 ; CARGO ; -3,500.00 ; MXN`

**Classification:** ISR provisional payment for January 2025. Tax payment -- not a deductible business expense.

---

## Section 5 -- Computation rules

### 5.1 General regime -- cumulative method

```
cumulative_income = total_income_YTD (with valid CFDI)
cumulative_deductions = total_deductible_expenses_YTD
cumulative_PTU = profit sharing paid
cumulative_losses = loss carryforwards applied
taxable_base = income - deductions - PTU - losses
provisional_ISR = apply_progressive_table(taxable_base)
payment = provisional_ISR - retenciones_YTD - prior_payments_YTD
if payment < 0: payment = 0
```

### 5.2 Progressive rate table (Art. 96 LISR, cumulative)

Ranges from 1.92% to 35%. Confirm against Annex 8 of the 2025 Resolucion Miscelanea Fiscal.

### 5.3 RESICO -- simplified

Applied to gross monthly income. No deductions. Fixed rates 1%-2.5%. Income limit MXN 3,500,000/year.

### 5.4 Persona moral -- coefficient of utility

```
coefficient = prior_year_fiscal_profit / prior_year_nominal_income
taxable_base = cumulative_income x coefficient
provisional_ISR = taxable_base x 30%
payment = provisional_ISR - retenciones - prior_payments
```

Flag for contador publico.

### 5.5 Filing deadline

The 17th of the month following the income month. Weekend/holiday: next business day.

---

## Section 6 -- Penalties and interest

### 6.1 Recargos and actualizacion

| Element | Rule |
|---|---|
| Actualizacion | Tax adjusted by INPC ratio (due month to payment month) |
| Recargos | Approx. 1.47%/month on updated amount |

### 6.2 Computation

```
updated_tax = unpaid_tax x (INPC_payment_month / INPC_due_month)
recargos = updated_tax x recargo_rate x months_late
total = updated_tax + recargos
```

### 6.3 Multas (fines)

| Violation | Fine range |
|---|---|
| Failure to file | MXN 1,810 -- MXN 22,400 per return |
| Filing errors | MXN 460 -- MXN 6,730 |

---

## Section 7 -- SAT filing procedure

1. Log into SAT portal with e.firma or contrasena
2. Select Declaraciones > Presenta tu declaracion provisional o definitiva
3. Select tax period and ISR provisional obligation
4. Enter income, deductions, prior payments
5. System calculates -- review and confirm
6. Generate linea de captura for payment
7. Pay via bank portal using linea de captura
8. Download and retain acuse de recibo

---

## Section 8 -- Edge cases

**EC1 -- First year, no coefficient (persona moral).** No prior year return for coefficient. SAT may estimate or zero provisionals in first year. Flag for contador publico.

**EC2 -- RESICO to general regime switch.** Exceeded MXN 3.5M threshold. Switch to cumulative progressive method from the month threshold was exceeded.

**EC3 -- Negative cumulative result.** No payment due. Loss carries forward in YTD computation.

**EC4 -- Retenciones exceed provisional ISR.** No payment due. Excess carries forward.

**EC5 -- Coefficient reduction request (Jul-Dec).** Personas morales may request lower coefficient for second half of year. Must file at least 1 month before first reduced payment.

---

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] Correct regime identified (general, RESICO, persona moral)
- [ ] Cumulative method applied for general regime (not monthly isolated)
- [ ] Prior payments and retenciones subtracted
- [ ] Progressive rate table current for 2025
- [ ] RESICO rates and MXN 3.5M threshold checked
- [ ] Filing deadline is 17th (not end of month)
- [ ] Only expenses with valid CFDI deducted
- [ ] Actualizacion included in late payment computation
- [ ] Loss carryforwards and PTU accounted for
- [ ] Output labelled as estimated until contador publico confirms

---

## Section 10 -- Test suite

### Test 1 -- RESICO monthly
**Input:** Monthly income MXN 40,000.
**Expected:** Rate 1.10%. Payment = MXN 440.

### Test 2 -- RESICO threshold exceeded
**Input:** Cumulative income hits MXN 3.6M.
**Expected:** Switch to general regime. Apply cumulative progressive method.

### Test 3 -- Negative cumulative result
**Input:** Cumulative deductions > income.
**Expected:** No payment due. Loss carries forward.

### Test 4 -- Retenciones exceed ISR
**Input:** Provisional ISR = MXN 5,000. Retenciones YTD = MXN 6,000.
**Expected:** No payment. Excess MXN 1,000 carries forward.

### Test 5 -- Late payment
**Input:** MXN 3,500 due 17 Feb. Paid 17 Apr. INPC ratio = 1.008. Recargo rate = 1.47%.
**Expected:** Updated tax = MXN 3,528. Recargos = MXN 3,528 x 1.47% x 2 = MXN 103.72.

### Test 6 -- First year persona moral
**Input:** New company, no prior annual return.
**Expected:** No coefficient available. Flag for contador publico.

---

## Prohibitions

- NEVER compute pagos provisionales using monthly isolated method for general regime -- ALWAYS cumulative YTD
- NEVER forget to subtract prior payments from the cumulative result
- NEVER apply RESICO rates to taxpayer exceeding MXN 3.5M annual income
- NEVER use coefficient of utility without verifying against most recent annual return
- NEVER ignore actualizacion when computing late payment charges
- NEVER deduct expenses without valid CFDI
- NEVER present amounts as definitive -- advise confirmation with contador publico

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a contador publico or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
