---
name: mx-estimated-tax
description: >
  Use this skill whenever asked about Mexican provisional income tax payments (pagos provisionales de ISR) for self-employed individuals and sole proprietors. Trigger on phrases like "pagos provisionales", "ISR provisional", "estimated tax Mexico", "coeficiente de utilidad", "coefficient of utility", "SAT monthly payment", "declaracion provisional", "Mexican advance tax", or any question about monthly provisional income tax obligations under the Ley del ISR. This skill covers the monthly payment schedule, cumulative computation method, coefficient of utility, reduction requests, penalties for late payment, and SAT filing procedures. ALWAYS read this skill before touching any estimated tax work for Mexico.
version: 1.0
jurisdiction: MX
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Mexico Estimated Tax (Pagos Provisionales de ISR) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Mexico |
| Jurisdiction Code | MX |
| Primary Legislation | Ley del Impuesto sobre la Renta (LISR), Art. 14 (pagos provisionales for personas morales); Arts. 106-108 (personas fisicas con actividades empresariales y profesionales); Art. 109 (Regimen Simplificado de Confianza / RESICO) |
| Supporting Legislation | Codigo Fiscal de la Federacion (CFF), Arts. 17-A (actualizacion), Art. 21 (recargos); Reglamento de la LISR, Art. 14 (reduction of provisional payments) |
| Tax Authority | Servicio de Administracion Tributaria (SAT) |
| Rate Publisher | SAT / Congreso de la Union (publishes rate tables in LISR) |
| Contributor | Open Accountants community |
| Validated By | Pending -- requires sign-off by Mexican contador publico |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: monthly schedule, cumulative computation for personas fisicas, progressive rate table, filing procedure. Tier 2: coefficient of utility for personas morales, reduction request (Jul-Dec), RESICO interaction. Tier 3: cross-border income, treaty credits, PE (establecimiento permanente) issues. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Contador publico must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any pago provisional, you MUST know:

1. **Tax regime** [T1] -- actividades empresariales y profesionales (general), RESICO (Regimen Simplificado de Confianza), or persona moral regimen general
2. **Monthly/cumulative income** [T1] -- gross income received for the period
3. **Deductible expenses** [T1] -- costs and expenses with valid CFDI (comprobante fiscal)
4. **Prior year annual return data** [T1] -- needed for coefficient of utility (personas morales)
5. **Withholdings (retenciones) received** [T1] -- reduces provisional payment
6. **Prior month provisional payments made** [T1] -- subtracted in cumulative method
7. **PTU (profit sharing) paid?** [T2] -- deductible in provisional payments
8. **Any loss carryforwards (perdidas fiscales)?** [T2] -- reduces taxable base

---

## Step 1: Determine Provisional Payment Obligation [T1]

**Legislation:** LISR Arts. 106-108 (personas fisicas); Art. 14 (personas morales)

### Who Must Make Pagos Provisionales

| Category | Provisional Payments Required? |
|----------|-------------------------------|
| Persona fisica -- actividades empresariales y profesionales | YES (monthly) |
| Persona fisica -- RESICO (income up to MXN 3.5M) | YES (monthly, simplified) |
| Persona moral -- regimen general | YES (monthly, using coefficient of utility) |
| Asalariado (employee) only | NO (employer withholds ISR) |

### Filing Deadline

**The 17th of the month following the period.** If the 17th falls on a non-business day, the deadline moves to the next business day.

| Income Month | Filing Deadline |
|-------------|----------------|
| January 2025 | 17 February 2025 |
| February 2025 | 17 March 2025 |
| ... | ... |
| December 2025 | 17 January 2026 |

---

## Step 2: Computation -- Personas Fisicas (Actividades Empresariales y Profesionales) [T1]

**Legislation:** LISR Art. 106

### Cumulative Method

```
cumulative_income = total_income_YTD (with valid CFDI)
cumulative_deductions = total_deductible_expenses_YTD
cumulative_PTU = profit sharing paid (if applicable)
cumulative_losses = loss carryforwards applied
taxable_base = cumulative_income - cumulative_deductions - cumulative_PTU - cumulative_losses
provisional_ISR = apply_progressive_rate_table(taxable_base)
minus_retenciones = withholdings_received_YTD
minus_prior_payments = sum of provisional payments already made this year
payment_due = provisional_ISR - retenciones - prior_payments
if payment_due < 0:
    payment = 0  # excess carries forward
```

### 2025 Monthly Progressive Rate Table (Art. 96 LISR, Annualized/Periodic)

The SAT publishes the applicable periodic tables (monthly, bimonthly, etc.) in Annex 8 of the Resolucion Miscelanea Fiscal. The monthly table applies cumulative income to monthly brackets and rates ranging from 1.92% to 35%.

| Lower Limit (MXN) | Upper Limit (MXN) | Fixed Quota (MXN) | Rate on Excess |
|-------------------|-------------------|-------------------|----------------|
| 0.01 | 8,952.49 | 0.00 | 1.92% |
| 8,952.50 | 75,984.55 | 171.88 | 6.40% |
| 75,984.56 | 133,536.07 | 4,461.94 | 10.88% |
| 133,536.08 | 155,229.80 | 10,723.55 | 16.00% |
| 155,229.81 | 185,852.57 | 14,194.54 | 17.92% |
| 185,852.58 | 374,837.88 | 19,682.13 | 21.36% |
| 374,837.89 | 590,795.99 | 60,049.40 | 23.52% |
| 590,796.00 | 1,127,926.84 | 110,842.74 | 30.00% |
| 1,127,926.85 | 1,503,902.46 | 271,981.99 | 32.00% |
| 1,503,902.47 | 4,511,707.37 | 392,294.17 | 34.00% |
| 4,511,707.38 | and above | 1,414,947.85 | 35.00% |

**Note:** Table is cumulative (applied to year-to-date taxable base). Confirm with Annex 8 of the 2025 RMF.

---

## Step 3: Computation -- Personas Morales (Coefficient of Utility) [T2]

**Legislation:** LISR Art. 14

### Coefficient of Utility (Coeficiente de Utilidad)

```
coefficient = prior_year_fiscal_profit / prior_year_nominal_income
provisional_taxable_base = current_month_cumulative_income x coefficient
minus_losses = fiscal loss carryforwards
minus_PTU = profit sharing paid
provisional_ISR = provisional_taxable_base x 30%  # corporate rate
minus_retenciones = withholdings
minus_prior_payments = prior provisional payments
payment_due = provisional_ISR - retenciones - prior_payments
```

### Reduction Request (Jul-Dec) [T2]

**Legislation:** LISR Art. 14, paragraph 7; RLISR Art. 14

From the second half of the fiscal year (July through December), taxpayers may request SAT authorization to apply a lower coefficient of utility if they estimate the year-end coefficient will be lower than the one currently used.

| Requirement | Detail |
|-------------|--------|
| When to file | At least 1 month before the first reduced payment |
| Form | Via SAT portal (solicitud de reduccion) |
| Documentation | Financial projections showing reduced profitability |
| Risk | If actual coefficient ends higher, recargos and actualizacion apply |

---

## Step 4: RESICO -- Simplified Regime [T1]

**Legislation:** LISR Art. 113-E to 113-J

### RESICO for Personas Fisicas

| Item | Rule |
|------|------|
| Income limit | Up to MXN 3,500,000 annual |
| Rate | Fixed rates from 1% to 2.5% based on monthly income |
| Method | Applied to gross income (no deductions) |
| Filing | Monthly via SAT portal |

### RESICO Monthly Rate Table

| Monthly Income (MXN) | Rate |
|----------------------|------|
| Up to 25,000.00 | 1.00% |
| 25,000.01 -- 50,000.00 | 1.10% |
| 50,000.01 -- 83,333.33 | 1.50% |
| 83,333.34 -- 208,333.33 | 2.00% |
| 208,333.34 -- 3,500,000.00 | 2.50% |

---

## Step 5: Penalties for Late Payment [T1]

**Legislation:** CFF Arts. 17-A, 21

### Recargos (Surcharges) and Actualizacion (Inflation Adjustment)

| Element | Rule |
|---------|------|
| Actualizacion | Unpaid tax is adjusted by the INPC (consumer price index) ratio from due month to payment month |
| Recargos | Currently approximately 1.47% per month on the updated amount (rate set by CFF Art. 21, adjusted periodically) |

### Computation

```
actualizacion_factor = INPC_payment_month / INPC_due_month
updated_tax = unpaid_tax x actualizacion_factor
recargos = updated_tax x recargo_rate x months_late
total_due = updated_tax + recargos
```

### Multas (Fines)

| Violation | Fine Range |
|-----------|-----------|
| Failure to file provisional return | MXN 1,810 -- MXN 22,400 per unfiled return |
| Filing with errors | MXN 460 -- MXN 6,730 |

---

## Step 6: Filing Procedure [T1]

### SAT Portal Filing

| Step | Action |
|------|--------|
| 1 | Log into SAT portal (sat.gob.mx) with e.firma or contrasena |
| 2 | Select "Declaraciones" > "Presenta tu declaracion provisional o definitiva de impuestos" |
| 3 | Select the tax period and obligation (ISR provisional) |
| 4 | Enter income, deductions, and prior payments |
| 5 | System calculates the tax -- review and confirm |
| 6 | Generate linea de captura for payment |
| 7 | Pay via bank portal using the linea de captura (valid for limited days) |
| 8 | Download and retain the acuse de recibo |

---

## Step 7: Edge Cases

### EC1 -- First year of operations, no coefficient [T2]
**Situation:** New persona moral has no prior year return for coefficient calculation.
**Resolution:** No coefficient available. The SAT may estimate or the taxpayer may use zero provisional payments in the first year. [T2] flag -- confirm approach with contador publico.

### EC2 -- RESICO to general regime switch [T1]
**Situation:** Client exceeded MXN 3.5M income threshold and must leave RESICO.
**Resolution:** Switch to actividades empresariales y profesionales regime. Begin using the cumulative progressive rate method from the month the threshold was exceeded.

### EC3 -- Negative cumulative result [T1]
**Situation:** Cumulative deductions exceed cumulative income YTD.
**Resolution:** No provisional payment due. The loss carries forward within the year's cumulative computation.

### EC4 -- Withholdings exceed provisional ISR [T1]
**Situation:** Client's retenciones already exceed the provisional ISR computed.
**Resolution:** No payment due. Excess retenciones carry forward in the cumulative computation.

---

## Self-Checks

Before delivering output, verify:

- [ ] Correct regime identified (general, RESICO, persona moral)
- [ ] Cumulative method applied (not monthly isolated)
- [ ] Prior payments and retenciones subtracted
- [ ] Progressive rate table current for 2025
- [ ] Coefficient of utility correctly computed (personas morales)
- [ ] Filing deadline is the 17th (not end of month)

---

## PROHIBITIONS

- NEVER compute pagos provisionales using a monthly isolated method -- ALWAYS use the cumulative YTD method (for general regime)
- NEVER forget to subtract prior provisional payments from the cumulative result
- NEVER apply the RESICO rate table to a taxpayer exceeding MXN 3.5M annual income
- NEVER use a coefficient of utility without verifying it against the most recent annual return
- NEVER ignore actualizacion when computing late payment charges
- NEVER present payment amounts as definitive -- advise client to confirm with their contador publico

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a contador publico or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
