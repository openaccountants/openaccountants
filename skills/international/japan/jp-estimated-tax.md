---
name: jp-estimated-tax
description: >
  Use this skill whenever asked about Japanese estimated tax prepayments (yotei nozei / 予定納税) for self-employed individuals, freelancers, or sole proprietors. Trigger on phrases like "予定納税", "yotei nozei", "estimated tax Japan", "Japanese advance tax", "予定納税基準額", "reduction application", "予定納税額の減額申請", or any question about advance income tax obligations under the Income Tax Act (所得税法). Covers the two-instalment schedule (July and November), the JPY 150,000 threshold, reduction applications, penalties for non-payment, and payment procedures. ALWAYS read this skill before touching any estimated tax work for Japan.
version: 2.0
jurisdiction: JP
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Japan Estimated Tax (予定納税 / Yotei Nozei) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Japan |
| Tax | Estimated income tax prepayments (予定納税 / yotei nozei) |
| Primary legislation | Income Tax Act (所得税法), Arts. 104-108, 111 |
| Supporting legislation | National Tax General Act (国税通則法), Arts. 60-63 |
| Authority | National Tax Agency (国税庁 / NTA) |
| Portal | e-Tax (etax.nta.go.jp) |
| Currency | JPY only |
| Payment schedule | Two instalments: 1/3 by July 31, 1/3 by November 30; final 1/3 with return (Feb-Mar) |
| Computation basis | 予定納税基準額 (baseline amount) from prior year final return |
| Minimum threshold | JPY 150,000 baseline amount |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by Japanese zeirishi (税理士) |
| Validation date | Pending |

**Instalment schedule summary:**

| Instalment | Due date | Amount |
|---|---|---|
| 1st (第1期) | 1-31 July | 1/3 of baseline |
| 2nd (第2期) | 1-30 November | 1/3 of baseline |
| Final (確定申告) | 16 Feb - 15 Mar (next year) | Actual tax minus yotei nozei paid |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Baseline amount unknown | Request prior year final return -- do not estimate |
| Capital gains in prior year | Verify exclusion from baseline (should be excluded) |
| Income dropping | File reduction application (減額申請) before reducing payments |
| Blue return status | Does not affect yotei nozei schedule |
| Disaster circumstances | Flag for zeirishi -- special provisions may apply |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- the 予定納税基準額 (baseline amount) from the prior year final return (確定申告).

**Recommended** -- nature of income, withholding tax (源泉徴収) credits, blue return (青色申告) status, current year income trend.

**Ideal** -- complete prior year 確定申告, NTA notification of yotei nozei amounts, bank statements showing prior payments.

**Refusal policy if minimum is missing -- HARD STOP.** Without the baseline amount, yotei nozei cannot be computed.

### Refusal catalogue

**R-JP-ET-1 -- Cross-border income.** Trigger: client has foreign-source income with treaty credits. Message: "Cross-border income and treaty credit timing for yotei nozei are outside this skill."

**R-JP-ET-2 -- Non-resident estimated tax.** Trigger: non-resident client. Message: "Non-resident estimated tax is outside this skill."

**R-JP-ET-3 -- Corporate estimated tax.** Trigger: client asks about corporate prepayments. Message: "Corporate estimated tax has different rules. This skill covers individuals only."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as a yotei nozei payment.

### 3.1 NTA income tax debits

| Pattern | Treatment | Notes |
|---|---|---|
| 税務署 (zeimusho / tax office) | Yotei nozei payment | Match with July/November timing |
| 予定納税, 予定 | Yotei nozei payment | Explicit description |
| 所得税 (shotokuzei / income tax) | Yotei nozei payment | Match with timing -- could also be final payment |
| 申告所得税 | Yotei nozei payment | "Declared income tax" |
| 振替納税 (furikae nozei) | Yotei nozei payment | Direct debit for tax (debit typically ~1 month after due date) |

### 3.2 Timing-based identification

| Debit date range | Likely payment | Confidence |
|---|---|---|
| 1 July -- 10 August | 1st instalment (第1期) | High if payee is tax office |
| Late July -- early August | 1st instalment via 振替納税 (direct debit) | Debit date is later than due date |
| 1 November -- 10 December | 2nd instalment (第2期) | High |
| Late December | 2nd instalment via 振替納税 | Debit date is later |
| 16 February -- 15 March | Final return payment (not yotei nozei) | Flag separately |

### 3.3 Related but NOT yotei nozei

| Pattern | Treatment | Notes |
|---|---|---|
| 消費税 (shouhizei) | EXCLUDE | Consumption tax payment |
| 住民税 (juuminzei) | EXCLUDE | Resident tax (municipal) |
| 国民健康保険 (kokumin kenko hoken) | EXCLUDE | National health insurance |
| 国民年金 (kokumin nenkin) | EXCLUDE | National pension |
| 加算税 (kasanzei) | EXCLUDE | Penalty surcharge |
| 延滞税 (entaizei) | EXCLUDE | Delinquent tax interest |
| 還付金 (kanpukin) | Flag for reviewer | Tax refund |

### 3.4 Payment method references

| Reference pattern | Treatment | Notes |
|---|---|---|
| e-Tax + 所得税 + 予定 | Yotei nozei via e-Tax | Electronic payment |
| 納付書 (nofusho) | Yotei nozei via payment slip | Bank counter payment |
| クレジットカード + 国税 | Yotei nozei via credit card | Via NTA credit card site |
| Pay-easy + 国税 | Yotei nozei via Pay-easy | Electronic banking |

---

## Section 4 -- Worked examples

### Example 1 -- Standard two-instalment computation

**Input:** Baseline amount (予定納税基準額) = JPY 600,000.

| Instalment | Period | Amount |
|---|---|---|
| 1st (第1期) | July 2025 | JPY 200,000 |
| 2nd (第2期) | November 2025 | JPY 200,000 |
| Final return | Feb-Mar 2026 | Actual tax - JPY 400,000 |

### Example 2 -- Below threshold

**Input:** Baseline amount = JPY 120,000.

**Output:** Below JPY 150,000 threshold. No yotei nozei required.

### Example 3 -- Delinquent tax computation

**Input:** 1st instalment JPY 200,000 due 31 July. Paid 15 October (76 days late).

**Computation:**
- First 60 days: JPY 200,000 x 2.4% x 60/365 = JPY 789
- Remaining 16 days: JPY 200,000 x 8.7% x 16/365 = JPY 762
- Total delinquent tax = JPY 1,551

### Example 4 -- Bank statement classification

**Input line:** `2025/07/31 ; 振替納税 所得税予定1期 ; 出金 ; -200,000 ; JPY`

**Classification:** Yotei nozei, 1st instalment for 2025. Tax payment -- not a deductible business expense.

---

## Section 5 -- Computation rules

### 5.1 Baseline amount (予定納税基準額)

The baseline is computed from the prior year's final return: income tax on recurring income sources minus withholding credits on those sources.

```
baseline = prior_year_tax_on_recurring_income - withholding_on_recurring_income
if baseline >= 150,000: yotei_nozei required
else: no yotei_nozei
```

Excluded from baseline: capital gains from asset sales, retirement income, timber income, one-off income.

### 5.2 Instalment amounts

```
each_instalment = baseline / 3
```

Each instalment is exactly 1/3 of the baseline (not 1/2).

### 5.3 Final return reconciliation

```
actual_tax = income_tax + special_reconstruction_tax (復興特別所得税)
total_yotei_paid = 1st + 2nd instalments
if actual_tax > total_yotei_paid: balance due with final return
if actual_tax < total_yotei_paid: refund via final return
```

---

## Section 6 -- Penalties and interest

### 6.1 Delinquent tax (延滞税 / entaizei)

| Period | Rate (2025) |
|---|---|
| First 2 months from due date | 2.4% per annum (特例基準割合, reviewed annually) |
| After 2 months | 8.7% per annum (standard rate) |

### 6.2 No penalty surcharge (加算税)

Yotei nozei is not subject to penalty surcharges (加算税) because it is a prepayment, not a return-based assessment. Only delinquent tax (延滞税) applies.

---

## Section 7 -- Reduction application (減額申請)

### 7.1 When to apply

| Trigger | Action |
|---|---|
| Current year income significantly lower | File 予定納税額の減額申請書 |
| Business closed or suspended | File reduction application |
| Disaster or extraordinary circumstances | File reduction application |
| New dependents or increased deductions | File reduction application |

### 7.2 Application deadlines

| Instalment | Deadline |
|---|---|
| 1st instalment reduction | By 15 July |
| 2nd instalment reduction | By 15 November |

### 7.3 Process

1. Complete 予定納税額の減額申請書
2. Attach estimated income statement through 30 June (for 1st) or 31 October (for 2nd)
3. Submit to jurisdictional tax office (所轄税務署)
4. Tax office reviews and approves or denies

If the NTA determines the estimate was unreasonably low, penalties may apply.

---

## Section 8 -- Edge cases

**EC1 -- First year of business.** No prior year return. No yotei nozei obligation. Tax settled entirely through final return.

**EC2 -- Capital gain in prior year inflated baseline.** Capital gains from asset sales are excluded from baseline by definition. If incorrectly included, contact tax office for correction.

**EC3 -- Income dropped significantly.** File 減額申請 by 15 July (1st) or 15 November (2nd). Flag for zeirishi.

**EC4 -- Disaster relief.** Special deferral or reduction provisions under the Disaster Tax Relief Act (災害減免法). Flag for zeirishi.

**EC5 -- 振替納税 (direct debit) timing.** Actual debit date is typically about 1 month after official due date. No delinquent tax for the gap between the official due date and the debit date.

---

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] 予定納税基準額 confirmed from prior year return
- [ ] JPY 150,000 threshold checked
- [ ] Instalments correctly calculated as 1/3 each (not 1/2)
- [ ] Capital gains, retirement, one-off income excluded from baseline
- [ ] Reduction application deadlines identified if applicable
- [ ] Delinquent tax rates current for the applicable year
- [ ] Payment method appropriate for the amount (convenience store cap JPY 300,000)
- [ ] 振替納税 timing noted if applicable
- [ ] Special reconstruction tax included in final reconciliation
- [ ] Output labelled as estimated until zeirishi confirms

---

## Section 10 -- Test suite

### Test 1 -- Standard computation
**Input:** Baseline = JPY 600,000.
**Expected:** 1st = JPY 200,000 (Jul). 2nd = JPY 200,000 (Nov). Final = actual - JPY 400,000.

### Test 2 -- Below threshold
**Input:** Baseline = JPY 120,000.
**Expected:** No yotei nozei required.

### Test 3 -- Delinquent tax (76 days late)
**Input:** JPY 200,000 paid 76 days late.
**Expected:** First 60 days at 2.4%, remaining 16 days at 8.7%. Total approx. JPY 1,551.

### Test 4 -- First year
**Input:** New freelancer, no prior return.
**Expected:** No yotei nozei. Tax paid with final return.

### Test 5 -- Reduction application
**Input:** Baseline JPY 600,000. Client expects 50% income drop.
**Expected:** Flag for zeirishi. File 減額申請 by 15 July or 15 November.

### Test 6 -- Refund on final return
**Input:** Yotei nozei paid JPY 400,000. Actual tax JPY 300,000.
**Expected:** Refund JPY 100,000 claimed on final return.

---

## Prohibitions

- NEVER compute yotei nozei without confirming the 予定納税基準額
- NEVER include capital gains, retirement, or one-off income in the baseline
- NEVER forget that each instalment is 1/3 (not 1/2) of the baseline
- NEVER advise filing a reduction application without flagging for zeirishi review
- NEVER apply penalty surcharge (加算税) to yotei nozei -- only delinquent tax (延滞税) applies
- NEVER present amounts as definitive -- advise confirmation with zeirishi

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a zeirishi or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
