---
name: it-estimated-tax
description: >
  Use this skill whenever asked about Italian estimated income tax advance payments (acconti IRPEF) for self-employed individuals, freelancers, or professionisti. Trigger on phrases like "acconti IRPEF", "acconto imposta", "estimated tax Italy", "Italian advance tax", "primo acconto", "secondo acconto", "historical method", "forecast method", "metodo storico", "metodo previsionale", "F24 payment", or any question about advance income tax obligations under the TUIR. Covers the two-instalment schedule (40% by Jun 30, 60% by Nov 30), historical vs forecast computation methods, the EUR 257.52 threshold, penalties for shortfall, and F24 payment procedures. ALWAYS read this skill before touching any estimated tax work for Italy.
version: 2.0
jurisdiction: IT
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Italy Estimated Tax (Acconti IRPEF) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Italy |
| Tax | Income tax advance payments (acconti IRPEF / imposta sostitutiva) |
| Primary legislation | D.P.R. 917/1986 (TUIR); D.L. 444/1997 Art. 1; D.P.R. 435/2001 Art. 17 |
| Supporting legislation | D.Lgs. 241/1997 (F24); D.Lgs. 472/1997 (penalties); D.Lgs. 462/1997 |
| Authority | Agenzia delle Entrate |
| Portal | Agenzia delle Entrate online |
| Currency | EUR only |
| Payment schedule | Two instalments: 40% by 30 June + 60% by 30 November (if > EUR 257.52); single instalment by 30 Nov if <= EUR 257.52 |
| Computation basis | 100% of prior year IRPEF (rigo RN34) -- historical method |
| Minimum threshold | EUR 51.65 triggers obligation; EUR 257.52 determines single vs two instalments |
| F24 codes | 4033 (primo acconto IRPEF), 4034 (secondo acconto IRPEF), 1840/1841 (forfettario) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by Italian commercialista |
| Validation date | Pending |

**Instalment schedule summary:**

| Condition | Schedule |
|---|---|
| Acconto > EUR 257.52 | 40% by 30 June + 60% by 30 November |
| Acconto <= EUR 257.52 but > EUR 51.65 | 100% by 30 November |
| Acconto <= EUR 51.65 | No advance payment required |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Historical vs forecast method | Use historical method (no penalty risk) |
| Regime unclear (ordinario vs forfettario) | Confirm before computing -- different codici tributo |
| Primo acconto deferral | 0.40% maggiorazione applies for 30-day deferral to 30 July |
| Addizionali regionali/comunali | Flag for reviewer -- separate advance obligations may apply |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- prior year IRPEF liability from Modello Redditi PF (rigo RN34 "Differenza") OR prior year imposta sostitutiva for regime forfettario.

**Recommended** -- tax regime confirmation (ordinario vs forfettario), current year estimated income (if forecast method considered), ritenute d'acconto received.

**Ideal** -- complete prior year Modello Redditi PF, F24 payment history, Cassetto Fiscale data.

**Refusal policy if minimum is missing -- HARD STOP for historical method.** Without rigo RN34, the historical method cannot be computed. If the client wants to use the forecast method, current year projections are needed -- flag for commercialista.

### Refusal catalogue

**R-IT-ET-1 -- Cross-border income.** Trigger: client has foreign-source income affecting DTAA credit timing. Message: "Cross-border income interactions with Italian acconti are outside this skill."

**R-IT-ET-2 -- Non-resident advance payments.** Trigger: non-resident client. Message: "Non-resident advance tax obligations have different rules."

**R-IT-ET-3 -- Addizionali computation.** Trigger: client asks for detailed addizionale regionale/comunale advance computation. Message: "Addizionali advances are separate obligations with municipality-specific rates. Consult a commercialista."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as an IRPEF advance payment.

### 3.1 F24 IRPEF advance debits

| Pattern | Treatment | Notes |
|---|---|---|
| F24, MODELLO F24, PAGAMENTO F24 | IRPEF acconto | Match with June/November timing and codice tributo |
| AGENZIA ENTRATE, AG ENTRATE | IRPEF acconto | Revenue agency payment |
| ACCONTO IRPEF, PRIMO ACCONTO, SECONDO ACCONTO | IRPEF acconto | Explicit description |
| CODICE 4033 | Primo acconto IRPEF | Specific codice tributo |
| CODICE 4034 | Secondo acconto IRPEF | Specific codice tributo |
| CODICE 1840 | Primo acconto forfettario | Imposta sostitutiva |
| CODICE 1841 | Secondo acconto forfettario | Imposta sostitutiva |

### 3.2 Timing-based identification

| Debit date range | Likely payment | Confidence |
|---|---|---|
| 25 June -- 5 July | Primo acconto (40%) | High if F24 reference |
| 25 July -- 5 August | Primo acconto with maggiorazione (deferred) | High -- check for 0.40% surcharge |
| 25 November -- 5 December | Secondo acconto (60%) | High |

### 3.3 Related but NOT IRPEF acconti

| Pattern | Treatment | Notes |
|---|---|---|
| IVA, CODICE 6099, LIQUIDAZIONE IVA | EXCLUDE | VAT payment |
| INPS, CONTRIBUTI PREVIDENZIALI | EXCLUDE | Social security contribution |
| CODICE 1001, RITENUTE LAVORO | EXCLUDE | Employee withholding payment |
| IMU, TASI, TARI | EXCLUDE | Property/municipal taxes |
| SALDO IRPEF, CODICE 4001 | Flag for reviewer | Year-end balance, not advance |
| RAVVEDIMENTO | Flag for reviewer | Voluntary regularisation payment |
| ADDIZIONALE REGIONALE, ADDIZIONALE COMUNALE | EXCLUDE | Separate from IRPEF acconti |

---

## Section 4 -- Worked examples

### Example 1 -- Standard two-instalment (historical method)

**Input:** Prior year IRPEF (rigo RN34) = EUR 5,000.

| Instalment | Due date | Percentage | Amount |
|---|---|---|---|
| Primo acconto | 30 June 2025 | 40% | EUR 2,000 |
| Secondo acconto | 30 November 2025 | 60% | EUR 3,000 |
| **Total** | | **100%** | **EUR 5,000** |

### Example 2 -- Single instalment (below EUR 257.52)

**Input:** Prior year IRPEF (rigo RN34) = EUR 200.

**Output:** EUR 200 > EUR 51.65, so acconti are due. EUR 200 <= EUR 257.52, so single instalment: EUR 200 by 30 November.

### Example 3 -- Below minimum threshold

**Input:** Prior year IRPEF (rigo RN34) = EUR 40.

**Output:** EUR 40 <= EUR 51.65. No advance payment required.

### Example 4 -- Regime forfettario

**Input:** Prior year imposta sostitutiva (5% new activity rate) = EUR 1,500.

| Instalment | Due date | Codice tributo | Amount |
|---|---|---|---|
| Primo acconto | 30 June 2025 | 1840 | EUR 600 |
| Secondo acconto | 30 November 2025 | 1841 | EUR 900 |

### Example 5 -- Primo acconto deferral

**Input:** Client cannot pay by 30 June. Defers to 30 July.

**Computation:** 0.40% maggiorazione on EUR 2,000 = EUR 8.00. Total payment by 30 July: EUR 2,008.00.

### Example 6 -- Bank statement classification

**Input line:** `30.06.2025 ; F24 TELEMATICO AGENZIA ENTRATE ; DEBIT ; COD 4033 ANNO 2025 ; -2,000.00 ; EUR`

**Classification:** Primo acconto IRPEF for 2025. Tax payment -- not a deductible business expense.

---

## Section 5 -- Computation rules

### 5.1 Historical method (metodo storico) -- default

```
acconto_base = prior_year_IRPEF (rigo RN34)
total_acconto = acconto_base x 100%
if total_acconto > 257.52:
    primo_acconto = total_acconto x 40%
    secondo_acconto = total_acconto x 60%
elif total_acconto > 51.65:
    single_instalment = total_acconto (due 30 November)
else:
    no_acconti_due
```

### 5.2 Forecast method (metodo previsionale) -- flag for reviewer

```
estimated_current_IRPEF = tax_on_estimated_income - detrazioni - ritenute
total_acconto = estimated_current_IRPEF x 100%
```

Risk: if forecast underestimates actual IRPEF, 30% penalty on the shortfall applies. Always flag for commercialista.

### 5.3 Regime forfettario

Same 40%/60% split, same deadlines. Use codici tributo 1840/1841. Base = prior year imposta sostitutiva, NOT IRPEF. Same EUR 257.52 / EUR 51.65 thresholds.

### 5.4 Maggiorazione for deferral

Primo acconto can be deferred by 30 days (to 30 July) with a 0.40% surcharge. Beyond 30 July: ravvedimento operoso applies.

---

## Section 6 -- Penalties and interest

### 6.1 Sanzione for insufficient/omitted acconti

| Violation | Base penalty |
|---|---|
| Omitted advance payment | 30% of unpaid amount |
| Insufficient advance payment | 30% of shortfall |

### 6.2 Ravvedimento operoso (voluntary regularisation)

| Timing | Reduced penalty |
|---|---|
| Within 14 days | 0.1% per day (max 1.4%) |
| Within 30 days | 1.5% |
| Within 90 days | 1.67% |
| Within annual return deadline | 3.75% |
| Within 2 years | 4.29% |
| Beyond 2 years | 5% |

Plus interest at the legal rate (2.5% per annum for 2025, subject to MEF decree).

### 6.3 Ravvedimento formula

```
amount_due = unpaid_tax + (unpaid_tax x reduced_penalty%) + interest
interest = unpaid_tax x (legal_rate / 365) x days_late
```

---

## Section 7 -- F24 payment procedure

### 7.1 Codici tributo

| Code | Description |
|---|---|
| 4033 | IRPEF -- Primo acconto |
| 4034 | IRPEF -- Secondo acconto |
| 1840 | Imposta sostitutiva forfettario -- Primo acconto |
| 1841 | Imposta sostitutiva forfettario -- Secondo acconto |

### 7.2 Filing steps

1. Access Agenzia delle Entrate portal or use intermediario abilitato
2. Complete Sezione Erario of F24 with codice tributo, anno di riferimento (2025), importo
3. Submit electronically (F24 telematico) -- mandatory for amounts > EUR 1,000 or with compensazioni
4. Retain the ricevuta telematica

### 7.3 Compensazione (offsetting)

Tax credits can be offset against acconti via F24. Horizontal compensation for credits > EUR 5,000 requires visto di conformita.

---

## Section 8 -- Edge cases

**EC1 -- First year of activity.** No prior year return. No acconti due under historical method. Tax settled entirely with the 2025 return in 2026.

**EC2 -- Switching from forfettario to ordinario.** No IRPEF acconti due (prior year was imposta sostitutiva). May still owe imposta sostitutiva acconti if switch happens after primo acconto deadline. Flag for commercialista.

**EC3 -- Acconto exactly EUR 257.52.** Single instalment by 30 November. Two-instalment split applies only when acconto EXCEEDS EUR 257.52.

**EC4 -- Deferral with maggiorazione.** Cannot pay by 30 June: defer to 30 July with 0.40% surcharge. Beyond 30 July: ravvedimento operoso.

**EC5 -- Forecast method underestimation.** If forecast method used and actual IRPEF exceeds the forecast, 30% penalty on the shortfall applies (reducible via ravvedimento).

---

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] Prior year IRPEF (rigo RN34) or imposta sostitutiva confirmed
- [ ] Correct threshold applied (EUR 51.65 / EUR 257.52)
- [ ] Method identified (historical vs forecast) with flag for forecast
- [ ] Correct codici tributo (4033/4034 for IRPEF, 1840/1841 for forfettario)
- [ ] Ravvedimento rates current for the applicable period
- [ ] Regime forfettario vs ordinario correctly distinguished
- [ ] Maggiorazione noted if deferral is relevant
- [ ] Compensazione visto threshold checked
- [ ] Due dates confirmed with weekend/holiday adjustments
- [ ] Output labelled as estimated until commercialista confirms

---

## Section 10 -- Test suite

### Test 1 -- Standard two-instalment
**Input:** Prior year IRPEF (RN34) = EUR 5,000.
**Expected:** Primo acconto = EUR 2,000 (30 Jun). Secondo acconto = EUR 3,000 (30 Nov). Total = EUR 5,000.

### Test 2 -- Single instalment
**Input:** Prior year IRPEF = EUR 200.
**Expected:** Single instalment EUR 200 by 30 November.

### Test 3 -- Below minimum
**Input:** Prior year IRPEF = EUR 40.
**Expected:** No acconti due.

### Test 4 -- Forfettario
**Input:** Prior year imposta sostitutiva = EUR 1,500.
**Expected:** Primo = EUR 600 (code 1840). Secondo = EUR 900 (code 1841).

### Test 5 -- Deferral with maggiorazione
**Input:** Primo acconto EUR 2,000 deferred to 30 July.
**Expected:** Maggiorazione = EUR 8.00. Total = EUR 2,008.00.

### Test 6 -- First year
**Input:** First year of activity. No prior return.
**Expected:** No acconti due under historical method.

### Test 7 -- Ravvedimento (30-day late)
**Input:** Secondo acconto EUR 3,000 paid 25 days late.
**Expected:** Penalty = 1.5% x EUR 3,000 = EUR 45. Plus interest at legal rate.

---

## Prohibitions

- NEVER compute acconti without confirming the prior year IRPEF liability (rigo RN34)
- NEVER use forecast method without flagging for commercialista and warning about 30% penalty
- NEVER confuse IRPEF acconti (4033/4034) with imposta sostitutiva acconti (1840/1841)
- NEVER ignore the EUR 257.52 threshold for single vs two-instalment determination
- NEVER forget the 0.40% maggiorazione when deferring primo acconto to July
- NEVER present acconto amounts as definitive -- advise confirmation with commercialista

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a commercialista or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
