---
name: mt-estimated-tax
description: >
  Use this skill whenever asked about Malta provisional tax (estimated tax) for self-employed or self-occupied individuals. Trigger on phrases like "provisional tax Malta", "estimated tax", "PT instalments", "how much provisional tax do I pay", "20% 30% 50%", "April instalment", "August instalment", "December instalment", "TA24 overpayment", "refund of provisional tax", "Chapter 372", "ITA provisional tax", or any question about Malta's advance income tax payment obligations. Covers the three-instalment schedule (20/30/50), basis of computation (prior year assessment), first-year rules, minimum provisional tax, penalties for late payment, and interaction with the TA24 final assessment. ALWAYS read this skill before touching any Malta provisional tax work.
version: 2.0
jurisdiction: MT
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Malta Provisional Tax (PT) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Malta (Republic of Malta) |
| Tax | Income tax provisional payments (Provisional Tax / PT) |
| Primary legislation | Income Tax Management Act, Chapter 372, Art. 44 et seq.; Provisional Tax Rules (S.L. 372.04) |
| Supporting legislation | Income Tax Act, Chapter 123, Art. 14 (deductions); Art. 50 (penalties) |
| Authority | Commissioner for Revenue (CFR), Malta |
| Portal | https://cfr.gov.mt (CFR Online Services) |
| Currency | EUR only |
| Payment schedule | Three instalments: 20% by 30 April, 30% by 31 August, 50% by 21 December |
| Computation basis | 100% of prior year assessed tax liability (from most recent TA24) |
| Minimum threshold | CFR-determined administrative minimum for new businesses with no prior assessment |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a Malta-warranted CPA |
| Validation date | Pending |

**Instalment schedule summary:**

| Instalment | Percentage | Due date |
|---|---|---|
| 1st | 20% | 30 April |
| 2nd | 30% | 31 August |
| 3rd | 50% | 21 December |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| No prior year TA24 available | STOP -- request latest TA24 assessment or CFR PT notice |
| First year, no penultimate year | Flag for reviewer -- minimum PT per CFR applies |
| Income expected to drop | Pay per notice -- do NOT reduce without CFR approval |
| Rental income in prior year tax | Exclude rental income taxed at 15% final WHT from PT basis |
| Overpayment treatment | Credit against next year (not automatic refund) |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- the prior year TA24 assessed tax liability (the net tax payable after credits) OR the CFR-issued PT notice (Vorauszahlungsbescheid equivalent). One of these is mandatory.

**Recommended** -- current year of assessment, any PAYE or withholding tax deducted at source in the current year, the client's TIN.

**Ideal** -- full TA24 from the prior year, any CFR PT notice received, bank statements showing prior PT payments, any correspondence about PT reductions.

**Refusal policy if minimum is missing -- HARD STOP.** Without the prior year TA24 tax liability or a CFR PT notice, provisional tax cannot be computed. Do not estimate from income figures.

### Refusal catalogue

**R-MT-PT-1 -- Group companies or partnership PT.** Trigger: client asks about PT for a company or partnership. Message: "This skill covers provisional tax for self-employed individuals only. Company and partnership PT obligations have different rules. Please consult a warranted accountant."

**R-MT-PT-2 -- Non-resident PT obligations.** Trigger: client is non-resident or asks about PT for non-residents. Message: "Non-resident provisional tax obligations are outside the scope of this skill. Please consult a warranted accountant."

**R-MT-PT-3 -- PT penalty disputes.** Trigger: client asks about disputing PT penalties or CFR enforcement. Message: "Penalty disputes require legal analysis. Please escalate to a warranted accountant or tax advocate."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as a provisional tax payment. Do not second-guess.

### 3.1 CFR provisional tax debits

| Pattern | Treatment | Notes |
|---|---|---|
| CFR, COMMISSIONER FOR REVENUE | PT payment | Match with April/August/December timing to identify which instalment |
| INLAND REVENUE MALTA | PT payment | Legacy name, same authority |
| PROVISIONAL TAX, PROV TAX, PT PAYMENT | PT payment | Explicit description |
| TAX INSTALMENT, TAX INST | PT payment | Generic instalment label |

### 3.2 Timing-based identification

| Debit date range | Likely instalment | Confidence |
|---|---|---|
| 15 April -- 10 May | 1st instalment (20%) | High if payee is CFR |
| 15 August -- 15 September | 2nd instalment (30%) | High if payee is CFR |
| 1 December -- 31 December | 3rd instalment (50%) | High if payee is CFR |
| Any other date to CFR | Late payment or adjustment | Flag for reviewer |

### 3.3 Related but NOT provisional tax

| Pattern | Treatment | Notes |
|---|---|---|
| VAT DEPARTMENT, VAT PAYMENT | EXCLUDE from PT | VAT payment, separate obligation |
| SSC, SOCIAL SECURITY, CESOP | EXCLUDE from PT | Social security contribution |
| FSS, FINAL SETTLEMENT | EXCLUDE from PT | PAYE final settlement system |
| PENALTY, INTEREST CFR | EXCLUDE from PT | Late payment charge, not PT principal |

### 3.4 Bank transfer references

| Reference pattern | Treatment | Notes |
|---|---|---|
| PT followed by year (e.g., PT2025) | PT payment for that year | Common bank transfer reference format |
| YA followed by year | PT payment for that year of assessment | Alternative reference format |
| INSTALMENT 1, INSTALMENT 2, INSTALMENT 3 | PT payment, specific instalment | Self-identified |

---

## Section 4 -- Worked examples

### Example 1 -- Standard three-instalment computation

**Input:** Prior year TA24 tax liability = EUR 9,000.

**Computation:**

| Instalment | Percentage | Amount | Due date |
|---|---|---|---|
| 1st | 20% | EUR 1,800 | 30 April 2025 |
| 2nd | 30% | EUR 2,700 | 31 August 2025 |
| 3rd | 50% | EUR 4,500 | 21 December 2025 |
| **Total** | **100%** | **EUR 9,000** | |

### Example 2 -- Reconciliation with final assessment (underpayment)

**Input:** Total PT paid = EUR 8,000. Final TA24 tax liability = EUR 11,500.

**Output:** Balance due = EUR 11,500 - EUR 8,000 = EUR 3,500. Due with TA24 filing by 30 June following the year of assessment.

### Example 3 -- Reconciliation with final assessment (overpayment)

**Input:** Total PT paid = EUR 10,000. Final TA24 tax liability = EUR 7,200.

**Output:** Overpayment = EUR 2,800. Client may request refund (written application to CFR, 6-12 months processing) or accept credit against next year's PT.

### Example 4 -- Rental income excluded from PT basis

**Input:** Prior year TA24: EUR 3,000 tax on self-employment income + EUR 1,500 tax on rental income (15% final WHT). Total tax = EUR 4,500.

**Computation:** PT based on EUR 3,000 only (rental income at 15% final WHT excluded).

| Instalment | Amount |
|---|---|
| 1st (20%) | EUR 600 |
| 2nd (30%) | EUR 900 |
| 3rd (50%) | EUR 1,500 |

### Example 5 -- Late payment penalty

**Input:** 1st instalment of EUR 1,800 due 30 April. Paid 15 July (2.5 months late).

**Computation:** Interest = EUR 1,800 x 0.75% x 3 months (rounded up) = EUR 40.50. Additional 10% penalty may apply at CFR discretion.

### Example 6 -- Bank statement classification

**Input line:** `30.04.2025 ; CFR ONLINE PAYMENT ; DEBIT ; PT2025 INST 1 ; -1,800.00 ; EUR`

**Classification:** Provisional tax payment, 1st instalment for YA 2025. Not a deductible expense for VAT or income tax purposes -- this is a tax payment, not a business cost.

---

## Section 5 -- Computation rules

### 5.1 Standard computation (prior-year basis)

The computation basis is always the prior year assessed tax liability from the most recent TA24, after credits, minus any tax deducted at source.

```
prior_year_tax = TA24_assessed_tax - tax_credits - WHT_at_source
PT_instalment_1 = prior_year_tax x 20%
PT_instalment_2 = prior_year_tax x 30%
PT_instalment_3 = prior_year_tax x 50%
total_PT = prior_year_tax x 100%
```

Do NOT divide by three equally. The split is always 20/30/50.

### 5.2 Year-end reconciliation

```
balance_due = final_tax_liability - total_PT_paid - WHT_at_source
if balance_due > 0: additional payment required with TA24 (by 30 June)
if balance_due < 0: overpayment -- refund or credit
```

### 5.3 Special rules for first year and new businesses

For the first year of self-employment with no prior TA24: PT is based on the penultimate year's tax. If no penultimate year assessment exists, the CFR sets a minimum PT amount administratively. Flag for reviewer.

### 5.4 Excluded income

Income subject to final withholding tax (e.g., 15% on rental income, 15% on certain interest) is NOT included in the PT computation base. PT applies only to income subject to progressive rates.

---

## Section 6 -- Penalties and interest

### 6.1 Late payment interest

| Element | Rate |
|---|---|
| Interest rate | 0.75% per month (9% per annum) |
| Runs from | Due date of each instalment |
| Maximum | No statutory cap -- accrues until paid |
| Additional penalty | CFR may impose 10% on amounts outstanding after final due date |

### 6.2 Interest computation

```
interest = unpaid_amount x 0.75% x months_overdue
```

Interest accrues per instalment independently. A missed April instalment accrues 8+ months of interest by December.

---

## Section 7 -- Adjustments and reductions

If the taxpayer expects current year income to be significantly lower than the prior year, they may apply in writing to CFR to reduce PT instalments. The application must include evidence (reduced contracts, cessation of activity) and should be submitted before the relevant instalment due date.

Risk: if actual tax exceeds the reduced PT, interest and penalties apply on the shortfall.

Flag for reviewer before advising any PT reduction.

---

## Section 8 -- Edge cases

**EC1 -- No prior year TA24 assessment available.** Client has been self-employed for 3 years but never filed a TA24. CFR may issue estimated assessments. PT should be based on the latest CFR-issued assessment. If none exists, CFR minimum applies. Flag for reviewer -- client must regularise filing history urgently.

**EC2 -- Prior year resulted in zero tax.** Tax liability = EUR 0. PT = EUR 0. No instalments required. However, if current year income is expected to exceed the personal allowance, voluntary PT payments are prudent.

**EC3 -- Mid-year switch from employment to self-employment.** First year of self-employment. Penultimate-year rule applies. PAYE covers the employment portion. PT applies only to the self-employment income. Flag for reviewer.

**EC4 -- Rental income at 15% final WHT.** Rental income taxed at 15% final WHT is excluded from the PT computation. PT applies only to income subject to progressive rates.

**EC5 -- Overpayment carried forward but client wants refund.** Client must submit written request to CFR. Processing time 6-12 months. Flag for reviewer for cash flow advice.

**EC6 -- Client ceases self-employment mid-year.** Apply to CFR to cancel remaining PT instalments. Final TA24 reconciles actual liability.

**EC7 -- CFR PT notice differs from client calculation.** The CFR notice prevails unless the client appeals. Pay the CFR-stated amount and query separately. Paying less triggers penalties on the shortfall.

**EC8 -- Foreign source income with DTR.** PT is based on the NET tax from the prior TA24, which already factors in double taxation relief. Flag for reviewer to confirm DTR availability in the current year.

**EC9 -- Late filing of prior year TA24.** Use the latest available assessed year as the basis. File the overdue TA24 urgently. CFR may issue revised PT notices once processed.

---

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] Prior year TA24 tax liability confirmed (or CFR PT notice obtained)
- [ ] 20/30/50 split applied (NOT equal thirds)
- [ ] Rental income at final WHT excluded from PT basis
- [ ] All three instalment due dates stated (30 Apr, 31 Aug, 21 Dec)
- [ ] Year-end reconciliation formula presented
- [ ] First-year / new business rule checked
- [ ] Any adjustment request flagged for reviewer
- [ ] Overpayment treatment explained (credit vs refund)
- [ ] Penalty rates stated if relevant
- [ ] Output labelled as estimated until CFR notice confirmed

---

## Section 10 -- Test suite

### Test 1 -- Standard three-instalment computation
**Input:** Prior year TA24 tax liability = EUR 9,000.
**Expected:** 1st = EUR 1,800 (30 Apr). 2nd = EUR 2,700 (31 Aug). 3rd = EUR 4,500 (21 Dec). Total = EUR 9,000.

### Test 2 -- Zero prior year tax
**Input:** Prior year TA24 tax liability = EUR 0.
**Expected:** PT = EUR 0. No instalments due. Flag: advise voluntary payments if current year income expected to exceed threshold.

### Test 3 -- Underpayment reconciliation
**Input:** Total PT paid = EUR 8,000. Final TA24 = EUR 11,500.
**Expected:** Balance due = EUR 3,500. Due with TA24 filing by 30 June.

### Test 4 -- Overpayment reconciliation
**Input:** Total PT paid = EUR 10,000. Final TA24 = EUR 7,200.
**Expected:** Overpayment = EUR 2,800. Client may request refund or credit.

### Test 5 -- Late payment penalty
**Input:** 1st instalment EUR 1,800 due 30 April. Paid 15 July (approx. 3 months late).
**Expected:** Interest = EUR 1,800 x 0.75% x 3 = EUR 40.50. Additional 10% penalty may apply.

### Test 6 -- First year, no prior assessment
**Input:** First year of self-employment. No prior TA24.
**Expected:** Flag for reviewer. Minimum PT per CFR administrative determination. Request CFR notice.

### Test 7 -- Rental income excluded
**Input:** Prior year: EUR 3,000 tax on SE income + EUR 1,500 on rental (15% WHT). Total = EUR 4,500.
**Expected:** PT on EUR 3,000 only. 1st = EUR 600, 2nd = EUR 900, 3rd = EUR 1,500.

---

## Prohibitions

- NEVER compute PT without the prior year TA24 tax liability or a CFR PT notice
- NEVER use current year estimated income as the basis -- PT is always prior year
- NEVER advise skipping PT payments because income is expected to drop -- must apply to CFR
- NEVER divide by three equally -- the split is always 20/30/50
- NEVER include income subject to final WHT (rental at 15%) in the PT basis
- NEVER present PT figures as definitive without a CFR notice -- label as estimated
- NEVER advise on PT penalty disputes without escalating to a warranted accountant
- NEVER assume overpayment is automatically refunded -- client must apply or accept credit

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
