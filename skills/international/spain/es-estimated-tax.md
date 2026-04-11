---
name: es-estimated-tax
description: >
  Use this skill whenever asked about Spanish estimated income tax payments (pagos fraccionados) for self-employed individuals (autonomos). Trigger on phrases like "Modelo 130", "pagos fraccionados", "estimated tax Spain", "IRPF quarterly", "Spanish advance tax", "autonomo tax payments", "estimacion directa", "Modelo 131", or any question about quarterly income tax prepayment obligations under the IRPF. This skill covers the quarterly payment schedule (Apr 20, Jul 20, Oct 20, Jan 30), the 20% cumulative computation method, the 70% withholding exemption, penalties for late filing, and payment procedures. ALWAYS read this skill before touching any estimated tax work for Spain.
version: 1.0
jurisdiction: ES
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Spain Estimated Tax (Pagos Fraccionados -- Modelo 130) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Spain |
| Jurisdiction Code | ES |
| Primary Legislation | Ley 35/2006 del IRPF, Art. 99.7-99.8 (obligation to make fractional payments); Real Decreto 439/2007 (RIRPF), Arts. 109-112 (computation and filing) |
| Supporting Legislation | Ley 58/2003 General Tributaria (LGT), Arts. 191-195 (penalties); Orden EHA/672/2007 (Modelo 130/131 forms) |
| Tax Authority | Agencia Estatal de Administracion Tributaria (AEAT) |
| Rate Publisher | AEAT / Ministerio de Hacienda |
| Contributor | Open Accountants community |
| Validated By | Pending -- requires sign-off by Spanish asesor fiscal |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: filing schedule, 20% computation, 70% withholding exemption, filing procedure. Tier 2: estimacion directa simplificada vs normal interaction, Modelo 131 (modulos), loss carryforward within the year. Tier 3: cross-border income, EU/EFTA treaty interactions, non-resident autonomos. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Asesor fiscal must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any pago fraccionado, you MUST know:

1. **Tax estimation method** [T1] -- estimacion directa normal, estimacion directa simplificada, or estimacion objetiva (modulos)
2. **Nature of activity** [T1] -- empresarial (business) or profesional (professional)
3. **Cumulative income and expenses year-to-date** [T1] -- needed for the 20% computation
4. **Withholdings (retenciones) received on invoices** [T1] -- determines 70% exemption eligibility
5. **Prior quarter payments already made** [T1] -- subtracted in cumulative calculation
6. **Any reduccion por inicio de actividad?** [T2] -- rate reduction in first 2 years for new autonomos
7. **Low-income deduction eligibility** [T1] -- prior year net income below EUR 12,000

**If the client uses estimacion objetiva (modulos), they file Modelo 131 instead of Modelo 130. This skill focuses on Modelo 130 (estimacion directa).**

---

## Step 1: Determine Filing Obligation [T1]

**Legislation:** Ley 35/2006, Art. 99.7; RIRPF Art. 109

### Who Must File Modelo 130

| Category | Modelo 130 Required? |
|----------|---------------------|
| Autonomo with economic activity under estimacion directa | YES |
| Professional (e.g., abogado, arquitecto) with >= 70% income subject to retenciones | NO (exempt) |
| Professional with < 70% income subject to retenciones | YES |
| Autonomo under estimacion objetiva (modulos) | NO -- files Modelo 131 instead |
| Employee with no economic activity | NO |

### The 70% Withholding Exemption [T1]

**A professional (not empresario) is exempt from Modelo 130 if at least 70% of their income from the prior year was subject to retenciones (withholding at source).** This is because the withholdings already serve as advance payments.

---

## Step 2: Payment Schedule [T1]

**Legislation:** RIRPF Art. 112

### Due Dates

| Quarter | Period Covered | Filing Deadline |
|---------|---------------|----------------|
| Q1 (1T) | 1 Jan -- 31 Mar | 1-20 April |
| Q2 (2T) | 1 Apr -- 30 Jun | 1-20 July |
| Q3 (3T) | 1 Jul -- 30 Sep | 1-20 October |
| Q4 (4T) | 1 Oct -- 31 Dec | 1-30 January (next year) |

**If the deadline falls on a Saturday, Sunday, or holiday, it moves to the next business day.**

**Q4 has a longer filing window (30 days vs 20 days) because it coincides with the start of the Renta campaign.**

---

## Step 3: Computation Method -- 20% Cumulative [T1]

**Legislation:** RIRPF Art. 110

### Formula

```
cumulative_net_income = total_income_YTD - total_expenses_YTD
gross_payment = cumulative_net_income x 20%
minus_retenciones = withholdings_received_YTD
minus_prior_payments = sum of Modelo 130 payments already made this year
payment_this_quarter = gross_payment - retenciones - prior_payments
if payment_this_quarter < 0:
    payment = 0  # negative result = no payment, amount carries forward
```

### Low-Income Deduction [T1]

If the prior year's net income (rendimientos netos) was less than EUR 12,000:

| Prior Year Net Income | Quarterly Deduction |
|----------------------|-------------------|
| <= EUR 9,000 | EUR 100 per quarter |
| EUR 9,000.01 -- EUR 10,000 | EUR 75 per quarter |
| EUR 10,000.01 -- EUR 11,000 | EUR 50 per quarter |
| EUR 11,000.01 -- EUR 12,000 | EUR 25 per quarter |
| > EUR 12,000 | EUR 0 |

### Example: Q2 Filing (Cumulative Jan-Jun)

| Item | Amount |
|------|--------|
| Cumulative income (Jan-Jun) | EUR 30,000 |
| Cumulative expenses (Jan-Jun) | EUR 10,000 |
| Cumulative net income | EUR 20,000 |
| 20% of net income | EUR 4,000 |
| Retenciones received YTD | EUR 500 |
| Q1 Modelo 130 payment made | EUR 1,500 |
| Q2 payment due | EUR 4,000 - EUR 500 - EUR 1,500 = EUR 2,000 |

---

## Step 4: Modelo 130 Form Structure [T1]

### Key Lines

| Line | Description |
|------|-------------|
| 01 | Cumulative net income (ingresos - gastos) |
| 02 | 20% of line 01 |
| 03 | Cumulative retenciones e ingresos a cuenta |
| 04 | Sum of prior quarterly payments |
| 05 | Low-income deduction (if applicable) |
| 07 | Result: line 02 - line 03 - line 04 - line 05 |

**If line 07 is negative, enter zero. The negative amount reduces future quarters.**

---

## Step 5: Penalties for Late Filing and Non-Payment [T1]

**Legislation:** LGT Arts. 191-195, Art. 27

### Late Filing Without AEAT Request (Voluntary)

| Delay | Surcharge (Recargo) | Interest |
|-------|---------------------|----------|
| Within 1 month | 1% | None |
| 1-2 months | 2% | None |
| 2-3 months | 3% | None |
| 3-6 months | 5% | None |
| 6-12 months | 10% | None |
| > 12 months | 15% | + late interest from month 12 |

### Late Filing After AEAT Request

| Severity | Penalty |
|----------|---------|
| Minor (no economic harm) | 50% of unpaid amount |
| Serious (concealment involved) | 50-100% |
| Very serious (fraudulent means) | 100-150% |

### Late Payment Interest (Interes de Demora)

The current rate is set annually by the Ley de Presupuestos Generales del Estado. For 2025: **4.0625%** (to be confirmed in the annual budget law).

---

## Step 6: Payment Procedure [T1]

### Filing Methods

| Method | Details |
|--------|---------|
| Sede Electronica AEAT | Online filing at sede.agenciatributaria.gob.es with certificado digital or Cl@ve |
| Modelo 130 PDF | Download, complete, and submit via bank (entidades colaboradoras) |
| Tax advisor (asesor fiscal) | Files on behalf of client via AEAT online platform |

### Payment Methods

| Method | Details |
|--------|---------|
| Domiciliacion bancaria | Direct debit -- must be set up 5 days before deadline |
| NRC (Numero de Referencia Completo) | Pay at bank first, then file with NRC code |
| Adeudo en cuenta | Charge to bank account at time of filing |

**Always retain the filing receipt (justificante de presentacion) with the CSV (Codigo Seguro de Verificacion).**

---

## Step 7: New Autonomo Reduction [T2]

**Legislation:** RIRPF Art. 110.3.b

In the first year of activity and the following year, new autonomos under estimacion directa may apply a reduced rate of between 5% and 20% depending on the applicable regime and conditions. This is subject to verification by the asesor fiscal.

**[T2] flag -- confirm eligibility with asesor fiscal before applying reduced rate.**

---

## Step 8: Edge Cases

### EC1 -- Negative cumulative result [T1]
**Situation:** Client has losses YTD, cumulative net income is negative.
**Resolution:** Payment = EUR 0 for the quarter. The loss carries forward within the cumulative computation for subsequent quarters in the same year.

### EC2 -- Professional exempt from Modelo 130 [T1]
**Situation:** Architect with 80% of income from entities that withhold retenciones.
**Resolution:** Exempt from Modelo 130 filing. Retenciones serve as advance payments.

### EC3 -- Activity started mid-year [T1]
**Situation:** Client registered as autonomo in May 2025.
**Resolution:** First Modelo 130 due in Q2 (by 20 July). Computation covers only the period from the start date. No Q1 filing required.

### EC4 -- Modelo 131 vs 130 confusion [T1]
**Situation:** Client asks about Modelo 130 but is under estimacion objetiva (modulos).
**Resolution:** Redirect to Modelo 131. Computation under modulos uses a fixed percentage of the modulo amount, not the 20% cumulative method.

---

## Self-Checks

Before delivering output, verify:

- [ ] Correct modelo identified (130 vs 131)
- [ ] 70% withholding exemption checked for professionals
- [ ] Cumulative method applied (not quarterly isolated)
- [ ] Prior quarter payments subtracted
- [ ] Low-income deduction applied if eligible
- [ ] Filing deadline correct (20th vs 30th for Q4)

---

## PROHIBITIONS

- NEVER compute Modelo 130 using a quarterly (non-cumulative) method -- it is ALWAYS cumulative YTD
- NEVER forget to subtract prior quarter payments from the cumulative result
- NEVER apply the 70% withholding exemption to empresarios -- it applies only to profesionales
- NEVER file Modelo 130 for a client under estimacion objetiva (modulos) -- they use Modelo 131
- NEVER ignore the low-income deduction for eligible clients
- NEVER present payment amounts as definitive -- advise client to confirm with their asesor fiscal

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
