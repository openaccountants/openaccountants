---
name: it-estimated-tax
description: >
  Use this skill whenever asked about Italian estimated income tax advance payments (acconti IRPEF) for self-employed individuals, freelancers, or professionisti. Trigger on phrases like "acconti IRPEF", "acconto imposta", "estimated tax Italy", "Italian advance tax", "primo acconto", "secondo acconto", "historical method", "forecast method", "metodo storico", "metodo previsionale", "F24 payment", or any question about advance income tax obligations under the TUIR. This skill covers the two-instalment schedule (40% by Jun 30, 60% by Nov 30), historical vs forecast computation methods, the EUR 257.52 threshold, penalties for shortfall, and F24 payment procedures. ALWAYS read this skill before touching any estimated tax work for Italy.
version: 1.0
jurisdiction: IT
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Italy Estimated Tax (Acconti IRPEF) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Italy |
| Jurisdiction Code | IT |
| Primary Legislation | D.P.R. 917/1986 (TUIR), Art. 2 (tax residence); D.L. 444/1997 Art. 1 (advance payment obligation); D.P.R. 435/2001 Art. 17 (payment deadlines) |
| Supporting Legislation | D.Lgs. 241/1997 (F24 payment system); D.Lgs. 472/1997 (penalties); D.Lgs. 462/1997 (assessment notices) |
| Tax Authority | Agenzia delle Entrate |
| Rate Publisher | Ministero dell'Economia e delle Finanze (MEF) |
| Contributor | Open Accountants community |
| Validated By | Pending -- requires sign-off by Italian commercialista |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: instalment schedule, historical method, EUR 257.52 threshold, F24 procedure. Tier 2: forecast method risk, regime forfettario interaction, addizionali regionali/comunali advances. Tier 3: cross-border income, DTAA credit timing, non-resident advance payments. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Commercialista must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any acconto, you MUST know:

1. **Prior year IRPEF liability from Modello Redditi PF (rigo RN34 "Differenza")** [T1] -- base for historical method
2. **Tax regime** [T1] -- regime ordinario, regime forfettario (flat tax 15%/5%), or regime dei minimi
3. **Current year estimated income** [T2] -- needed if using forecast method (metodo previsionale)
4. **Withholdings (ritenute d'acconto) received** [T1] -- reduces IRPEF liability
5. **Any tax credits (detrazioni/deduzioni) expected?** [T1] -- affects net tax
6. **Addizionale regionale and comunale IRPEF** [T2] -- separate advance payment obligations may apply
7. **Is this the first year of activity?** [T1] -- no prior year base means no acconti due under historical method

**If the prior year IRPEF liability (rigo RN34) is zero or a credit, no acconti are due under the historical method.**

---

## Step 1: Determine Advance Payment Obligation [T1]

**Legislation:** D.L. 444/1997, Art. 1

### Who Must Pay Acconti

| Category | Acconti Required? |
|----------|-------------------|
| Self-employed with prior year IRPEF > EUR 51.65 | YES |
| Freelancer/professionista with prior year IRPEF > EUR 51.65 | YES |
| Regime forfettario with prior year imposta sostitutiva > EUR 51.65 | YES (advance on substitute tax, not IRPEF) |
| First year of activity, no prior year return | NO (under historical method) |
| Prior year IRPEF = zero or credit | NO |

### Threshold for Advance Payment [T1]

| Threshold | Amount |
|-----------|--------|
| Minimum to trigger any advance payment | EUR 51.65 (rigo RN34 > EUR 51.65) |
| Single instalment vs two instalments | EUR 257.52 |

---

## Step 2: Instalment Schedule [T1]

**Legislation:** D.P.R. 435/2001, Art. 17

### Advance Payment = 100% of Prior Year IRPEF (Historical Method)

| Condition | Number of Instalments | Schedule |
|-----------|----------------------|----------|
| Acconto <= EUR 257.52 | 1 instalment | 100% by 30 November |
| Acconto > EUR 257.52 | 2 instalments | 40% by 30 June + 60% by 30 November |

### Due Dates

| Instalment | Due Date | Percentage of Total Acconto |
|------------|----------|---------------------------|
| Primo acconto (1st) | 30 June | 40% |
| Secondo acconto (2nd) | 30 November | 60% |

**The primo acconto can be deferred by 30 days (to 30 July) with a 0.40% surcharge (maggiorazione).**

**If 30 June or 30 November falls on a weekend/holiday, the due date shifts to the next business day.**

### Example: Prior Year IRPEF = EUR 5,000

| Instalment | Due Date | Computation | Amount |
|------------|----------|-------------|--------|
| Primo acconto | 30 Jun 2025 | EUR 5,000 x 40% | EUR 2,000 |
| Secondo acconto | 30 Nov 2025 | EUR 5,000 x 60% | EUR 3,000 |
| **Total acconti** | | | **EUR 5,000** |

---

## Step 3: Computation Methods [T1/T2]

### Method 1: Historical Method (Metodo Storico) [T1]

```
acconto_base = prior_year_IRPEF (rigo RN34 of Modello Redditi PF)
total_acconto = acconto_base x 100%
primo_acconto = total_acconto x 40%  (if total > EUR 257.52)
secondo_acconto = total_acconto x 60%
```

**This is the default and safest method. No risk of penalties for underpayment.**

### Method 2: Forecast Method (Metodo Previsionale) [T2]

```
estimated_current_year_IRPEF = tax_on_estimated_income - detrazioni - ritenute
total_acconto = estimated_current_year_IRPEF x 100%
primo_acconto = total_acconto x 40%
secondo_acconto = total_acconto x 60%
```

**WARNING:** If the forecast underestimates actual IRPEF, the taxpayer faces penalties for insufficient advance payment. **[T2] flag -- commercialista must confirm the forecast is reasonable.**

### When to Use Forecast Method

| Trigger | Rationale |
|---------|-----------|
| Significant drop in income expected | Reduces cash outflow during the year |
| Prior year had one-off income (capital gain, inheritance) | Avoids overpaying acconti |
| Client stopping activity mid-year | Reduces unnecessary prepayment |

---

## Step 4: Penalties for Insufficient Payment [T1]

**Legislation:** D.Lgs. 472/1997, Art. 13; D.Lgs. 471/1997, Art. 1

### Sanzione for Omitted or Insufficient Acconti

| Violation | Base Penalty |
|-----------|-------------|
| Omitted advance payment | 30% of unpaid amount |
| Insufficient advance payment | 30% of the shortfall |

### Ravvedimento Operoso (Voluntary Regularisation) [T1]

| Timing of Regularisation | Reduced Penalty |
|--------------------------|----------------|
| Within 14 days of due date | 0.1% per day (max 1.4%) |
| Within 30 days of due date | 1.5% |
| Within 90 days of due date | 1.67% |
| Within the annual return deadline | 3.75% |
| Within 2 years | 4.29% |
| Beyond 2 years | 5% |

**Interest is also due at the legal rate (currently 2.5% per annum for 2025, subject to annual MEF decree).**

### Ravvedimento Formula

```
regularisation_amount = unpaid_tax + (unpaid_tax x reduced_penalty%) + interest
interest = unpaid_tax x (legal_rate / 365) x days_late
```

---

## Step 5: F24 Payment Procedure [T1]

**Legislation:** D.Lgs. 241/1997

### Codici Tributo (Tax Codes)

| Code | Description |
|------|-------------|
| 4033 | IRPEF -- Primo acconto |
| 4034 | IRPEF -- Secondo acconto |
| 1840 | Imposta sostitutiva regime forfettario -- Primo acconto |
| 1841 | Imposta sostitutiva regime forfettario -- Secondo acconto |

### Filing the F24

| Step | Action |
|------|--------|
| 1 | Access Agenzia delle Entrate online portal or use intermediario abilitato |
| 2 | Complete Sezione Erario of F24 with codice tributo, anno di riferimento (2025), and importo |
| 3 | Submit electronically (F24 telematico) -- mandatory for amounts exceeding EUR 1,000 or with compensazioni |
| 4 | Retain the ricevuta telematica as proof of payment |

### Compensazione (Offsetting) [T2]

Tax credits (e.g., credito IRPEF from prior year) can be offset against acconti via the F24. Horizontal compensation (across different taxes) requires a visto di conformita for credits exceeding EUR 5,000.

---

## Step 6: Regime Forfettario Interaction [T1]

**Legislation:** L. 190/2014, Art. 1, commi 54-89 (as amended)

| Item | Regime Forfettario Rule |
|------|------------------------|
| Tax | Imposta sostitutiva (15%, or 5% for first 5 years of new activity) |
| Advance payment | Same 40%/60% split, same deadlines |
| Codici tributo | 1840 (primo acconto), 1841 (secondo acconto) |
| Historical method base | Prior year imposta sostitutiva, NOT IRPEF |
| Threshold | Same EUR 257.52 / EUR 51.65 thresholds |

---

## Step 7: Edge Cases

### EC1 -- First year of activity [T1]
**Situation:** Client started freelance activity in 2025, no prior year return.
**Resolution:** No acconti due in 2025 under the historical method. Client pays saldo (balance) with the 2025 return in 2026.

### EC2 -- Switching from forfettario to ordinario [T2]
**Situation:** Client was in regime forfettario in 2024, moves to ordinario in 2025.
**Resolution:** No IRPEF acconti due (prior year was imposta sostitutiva, not IRPEF). May still owe imposta sostitutiva acconti if the switch happens after the primo acconto deadline. [T2] flag -- confirm with commercialista.

### EC3 -- Acconto exactly EUR 257.52 [T1]
**Situation:** Prior year IRPEF is exactly EUR 257.52.
**Resolution:** Single instalment of EUR 257.52 due by 30 November. The two-instalment split applies only when the acconto EXCEEDS EUR 257.52.

### EC4 -- Deferral of primo acconto with maggiorazione [T1]
**Situation:** Client cannot pay by 30 June.
**Resolution:** May defer to 30 July with a 0.40% surcharge on the deferred amount. Beyond 30 July, ravvedimento operoso applies.

---

## Self-Checks

Before delivering output, verify:

- [ ] Prior year IRPEF (rigo RN34) confirmed
- [ ] Correct threshold applied (EUR 51.65 / EUR 257.52)
- [ ] Method identified (historical vs forecast) with T2 flag for forecast
- [ ] Correct codici tributo used (4033/4034 for IRPEF, 1840/1841 for forfettario)
- [ ] Ravvedimento rates current for the applicable period
- [ ] Regime forfettario vs ordinario correctly distinguished

---

## PROHIBITIONS

- NEVER compute acconti without confirming the prior year IRPEF liability (rigo RN34)
- NEVER use forecast method without flagging as [T2] and warning about penalty risk
- NEVER confuse IRPEF acconti (4033/4034) with imposta sostitutiva acconti (1840/1841)
- NEVER ignore the EUR 257.52 threshold for single vs two-instalment determination
- NEVER forget the 0.40% maggiorazione when deferring the primo acconto to July
- NEVER present acconto amounts as definitive -- advise client to confirm with their commercialista

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a commercialista or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
