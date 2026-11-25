---
name: ca-fed-instalments
description: Use this skill whenever asked about Canadian federal quarterly instalment requirements for self-employed individuals. Trigger on phrases like "CRA instalments", "quarterly tax Canada", "instalment reminder", "INNS1", "INNS2", "net tax owing", "$3,000 threshold", "instalment interest", or any question about quarterly income tax prepayments for Canadian individuals. Covers the $3,000 net-tax-owing threshold, three calculation methods (no-calculation, prior-year, current-year), instalment due dates (Mar 15, Jun 15, Sep 15, Dec 15), instalment interest and penalties, and interaction with provincial instalments. ALWAYS read this skill before touching any Canada estimated tax work.
version: 2.1
jurisdiction: CA
tax_year: 2025
tax_year_notes: This corrects the existing 2025 instalment workpaper using its completed 21 November 2026 audit; 2023 and 2024 remain the prior-year example inputs. It remains a historical calendar-year workpaper and does not claim current-year or cross-year coverage.
last_updated: 2026-11-25
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Nathan Wiebe"
reviewed_on: 2026-11-03
tier: 1
domain: income-tax
---

# CA Fed Instalments

## Canada Federal Quarterly Instalments -- Self-Employed Skill v2.1

This is a **2025 instalment workpaper**. Keep eligibility net tax owing separate from the full payment base, and bind the actual reminder, return/worksheet inputs, province and farming/fishing status. **HOLD** means the affected result must not be finalized until the stated condition or input is established; it does not mean no instalments or zero tax.

## Rates and thresholds

Reviewed against the cited tax authorities by **Nathan Wiebe** on 2026-06-21.
The historical review attribution above is retained; it does not approve this proposed correction. Unresolved conditions and inputs are explicitly held below.

### Fed Instalments

- **Net tax owing threshold** — Ordinary individual: > $3,000 current AND either of two prior years; use $1,800 for Quebec and the separate farming/fishing test below. [ITA 156.1(1)-(2)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html)
- **Quebec federal threshold** — $1,800  _(ITA s.156.1(1); CRA — Instalments — canada.ca)_
- **Q1** — March 15  _(ITA s.156(1))_
- **Q2** — June 15  _(ITA s.156(1))_
- **Q3** — September 15  _(ITA s.156(1))_
- **Q4** — December 15  _(ITA s.156(1))_
- **No-calculation (CRA suggested)** — Pay the actual reminder amounts: first-half quarters use one-quarter of the second-prior-year payment base; second-half quarters reconcile to the prior-year payment base. Include applicable CPP/EI amounts, not NTO alone. [ITA 156](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.html); [2025 CRA chart](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/instalment-chart-fill-25e.pdf)
- **Prior-year method** — Each ordinary quarter uses the full prior-year instalment payment base, including applicable CPP/EI payable after the NTO eligibility test; it is not NTO alone divided by four. [2025 CRA chart](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/instalment-chart-fill-25e.pdf); [Official source](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/options-calculate.html)
- **Current-year method** — Each ordinary quarter uses the full estimated current-year payment base, including applicable CPP/EI payable after the NTO eligibility test. Underestimation can cause interest. [2025 CRA chart](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/instalment-chart-fill-25e.pdf); [Official source](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/options-calculate.html)
- **Interest conditions** — Pay the actual no-calculation reminder amounts in full and on time. Prior/current-year options also avoid interest when correctly calculated amounts are paid in full by their due dates; inadequate estimates can attract interest. Do not call a method unconditionally safe without its amount and timing conditions. ITA 161(4.01) uses the least total amount under the statutory alternatives, including the Minister's notices, for instalment interest and penalty purposes. [ITA 161(4.01)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-161.html); [CRA options](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/options-calculate.html)
- **Interest formula** — Overdue-taxes prescribed rate (base rate + 4 percentage points), compounded daily  _(ITA s.161(2); CRA — Prescribed interest rates — canada.ca)_
- **Penalty trigger** — Instalment interest > $1,000  _(ITA s.163.1)_
- **Penalty formula** — max(0, instalment interest − max($1,000, 25% × interest if no payments)) ÷ 2. Do not halve the result twice. [ITA 163.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-163.1.html); [Official source](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/interest-penalty-charges.html)
- **Farming/fishing** — Where the statutory farming/fishing regime applies, the ordinary threshold must be exceeded in the current year **and both** prior years. The statutory annual payment, due December 31, uses two-thirds of the estimated tax payable under Part I for the current year or the prescribed instalment base for the preceding year. **HOLD:** establish chief-source status, full base and applicable year inputs; the CRA 2025 chart prints 66% while ITA 155 says two-thirds, so the chart/statute difference must be reconciled before finalizing a payment. [ITA 155](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-155.html); [ITA 156.1(2)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html)
- **Quebec residents** — Federal threshold $1,800; provincial administered by Revenu Quebec  _(ITA s.156.1; Revenu Québec)_
- **Due date on weekend** — Next business day  _(Interpretation Act s.26; CRA guidance)_

## Section 1 -- Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Canada (federal) |
| Tax | Quarterly income tax instalments |
| Primary legislation | Income Tax Act (ITA), [s 156](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.html) (ordinary instalments); [s 156.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html) (thresholds, NTO definition and exceptions); [s 155](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-155.html) (farming/fishing regime) |
| Supporting legislation | ITA s 161(2) (interest); s 163.1 (penalty); Interpretation Act s 26 (due date rules) |
| Authority | Canada Revenue Agency (CRA) |
| Portal | My Account (cra-arc.gc.ca) |
| Currency | CAD only |
| Threshold | Net tax owing > $3,000 in current year AND either of two preceding years ($1,800 for Quebec residents, federal portion) |
| Payment schedule | Quarterly: March 15, June 15, September 15, December 15 |
| Three methods | No-calculation (CRA suggested), prior-year, current-year |
| Contributor | Open Accountants Community |
| Validated by | Verified by Nathan Wiebe on 2026-06-21 |
| Validation date | Verified by Nathan Wiebe on 2026-06-21 |

**Instalment schedule summary**

| Instalment | Due date |
| --- | --- |
| Q1 | March 15 |
| Q2 | June 15 |
| Q3 | September 15 |
| Q4 | December 15 |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Method selection | Bind the actual reminder or full selected payment base and pay on time; prior/current-year estimates must be adequate. No unconditional method guarantee. |
| Quebec resident | Federal threshold $1,800 (provincial administered separately by Revenu Quebec) |
| Farming/fishing income | Single annual instalment by December 31 may apply |
| First year of SE | May not meet two-year threshold -- check both prior years |
| Due date on weekend | Next business day |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Minimum viable** — net tax owing for the current year and two preceding years (to confirm threshold), CRA instalment reminder (INNS1 or INNS2) if available.
- **Recommended** — T1 returns for prior two years, expected current year income and tax, province of residence.
- **Ideal** — complete three-year T1 history, CRA My Account statement, farming/fishing income status.
- **Refusal policy if minimum is missing** — **HOLD** the required-payment conclusion without the necessary threshold history, full payment base or applicable reminder. Explain the missing input; do not substitute zero or conclude no obligation.

### Refusal catalogue

- **R-CA-FI-1 -- Corporate instalments** — Trigger: client asks about corporate instalment requirements. Message: "Corporate instalments under ITA s 157 have different rules. This skill covers individuals only."  _(ITA s 157)_
- **R-CA-FI-2 -- GST/HST instalments** — Trigger: client asks about GST/HST instalments. Message: "GST/HST instalments are a separate obligation. See ca-fed-gst-hst."
- **R-CA-FI-3 -- Trust instalment requirements** — Trigger: trust client. Message: "Trust instalments are outside this skill."

## Section 3 -- Payment pattern library

These are candidate bank-matching patterns, not legal due dates or proof that a debit is an income-tax instalment. **HOLD:** confirm payee, account/year, reminder and reconciliation evidence before classification. Keep the original timing windows as workflow heuristics, not statutory tests.

### 3.1 CRA instalment debits

**CRA instalment debits**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CRA, CANADA REVENUE AGENCY | Instalment payment | Match with Mar/Jun/Sep/Dec timing |
| CRA INSTALMENT, CRA INST | Instalment payment | Explicit description |
| RECEIVER GENERAL, REC GEN CANADA | Instalment payment | Federal government payee |
| CRA PRE-AUTHORIZED DEBIT | Instalment payment | Automatic payment |
| MY PAYMENT CRA | Instalment payment | Online payment via My Account |

### 3.2 Timing-based identification

**Timing-based identification**

| Debit date range | Likely instalment | Confidence |
| --- | --- | --- |
| 10 March -- 20 March | Q1 (Mar 15) | High if CRA payee |
| 10 June -- 20 June | Q2 (Jun 15) | High |
| 10 September -- 20 September | Q3 (Sep 15) | High |
| 10 December -- 20 December | Q4 (Dec 15) | High |
| April -- May | Balance owing from prior year return | Flag separately |

### 3.3 Related but NOT income tax instalments

**Related but NOT income tax instalments**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CRA GST, GST/HST | EXCLUDE | GST/HST payment |
| CRA CPP, CPP PAYMENT | EXCLUDE | CPP contribution (if separate) |
| CRA CHILD BENEFIT, CCB | EXCLUDE (credit) | Canada Child Benefit receipt |
| REVENU QUEBEC, MRQ | EXCLUDE | Provincial instalment (Quebec) |
| CRA PENALTY, CRA INTEREST | EXCLUDE | Penalty/interest charge |
| CRA REFUND | Flag for reviewer | Tax refund |

### 3.4 Payment references

**Payment references**

| Reference pattern | Treatment | Notes |
| --- | --- | --- |
| SIN + INST or INSTALMENT | CRA instalment | Standard reference format |
| Tax year + Q1/Q2/Q3/Q4 | CRA instalment, specific quarter | Self-identified |

## Section 4 -- Worked examples

### Example 1 -- No-calculation method

**No-calculation method table**

| Instalment | Due date | Amount | Basis |
| --- | --- | --- | --- |
| Q1 | 15 Mar | $6,250 | 1/4 of 2023 ($25,000) |
| Q2 | 15 Jun | $6,250 | 1/4 of 2023 ($25,000) |
| Q3 | 15 Sep | $7,750 | ($28,000 - $12,500) / 2 |
| Q4 | 15 Dec | $7,750 | ($28,000 - $12,500) / 2 |
| **Total** |  | **$28,000** |  |

2023 net tax owing = $25,000. 2024 net tax owing = $28,000. These original inputs are retained. The table is conditional arithmetic assuming applicable CPP/EI additions are zero and the reminder/payment bases equal those NTO amounts. **HOLD:** the inputs alone do not establish those assumptions or an actual required payment. Dates are nominal; apply weekend/holiday relief separately.

### Example 2 -- Prior-year method

**Input:** 2024 net tax owing = $28,000.

**Output:** If applicable CPP/EI additions are zero, each quarter is $28,000 / 4 = $7,000; total $28,000. **HOLD:** bind those additions and payment timing before finalizing. For comparison, $4,000 of applicable CPP/EI payable makes the full base $32,000 and each quarter **$8,000**, not $7,000. Correctly calculated prior-year payments made in full on time can avoid interest.

### Example 3 -- Below threshold

**Input:** 2024 net tax owing = $2,500. 2023 net tax owing = $2,800.

**Output:** For an ordinary non-Quebec individual, both preceding years are below $3,000, so no 2025 instalments are required. Balance due April 30, 2026. **HOLD for Quebec:** recompute the prior-year amounts on the Quebec-specific federal NTO definition and bind current-year NTO; the ordinary non-Quebec figures do not establish its threshold history.

### Example 4 -- Farming/fishing exception

**Input:** Chief source of income is farming. Expected 2025 net tax = $18,000.

**Output:** $18,000 × 2/3 = $12,000 is arithmetic only. **HOLD:** neither the prior-year eligibility history nor the full current/prior-year payment bases and applicable CPP/EI additions are supplied. Do not conclude that exactly $12,000 is required. Resolve the 66% chart/two-thirds statute discrepancy described above before finalizing.

### Example 5 -- Bank statement classification

**Input line:** `15.03.2025 ; CRA INSTALMENT PAYMENT ; DEBIT ; -7,000.00 ; CAD`

**Candidate classification:** Federal income tax instalment, Q1 2025; a tax payment is not a deductible expense. **HOLD:** confirm payee, tax account/year and reconciliation evidence before booking. The synthetic debit date is not proof of the adjusted statutory due date.

## Section 5 -- Computation rules

### 5.1 Threshold test

- **Threshold test** — Instalments required if net tax owing > $3,000 in BOTH: - Current year (2025), AND - Either of two preceding years (2024 or 2023) Quebec residents: federal threshold is $1,800.

This is the ordinary individual test. For the statutory farming/fishing regime, NTO must exceed the applicable threshold in **all three years**. First self-employment year alone is not an exemption. [ITA 156.1(1)-(2)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html)

### 5.2 Net tax owing

- **Net tax owing** — Use the actual 2025 chart's specific payable/credit lines, including applicable social-benefit repayments. Do not subtract generic refundable credits or CPP/EI overpayments through the old shortcut. Keep ordinary non-Quebec combined tax separate from Quebec's federal calculation. **HOLD:** no threshold result from an unbound shortcut or missing chart inputs. [ITA 156.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html); [2025 CRA chart](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/instalment-chart-fill-25e.pdf)

### 5.3 Three calculation methods

**Method 1 -- No-calculation (CRA suggested):**
- Q1, Q2: 1/4 of the full second-prior-year (2023) payment base.
- Q3, Q4: (full prior-year (2024) payment base - Q1 - Q2) / 2.
- Use the actual reminder and applicable CPP/EI additions; NTO alone is not the full base. [ITA 156](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.html); [2025 CRA chart](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/instalment-chart-fill-25e.pdf)

**Method 2 -- Prior-year:**
- Each ordinary quarter = the **full 2024 instalment payment base** / 4, including applicable CPP/EI payable after the tax-only threshold test. [Official source](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/instalment-chart-fill-25e.pdf)

**Method 3 -- Current-year:**
- Each ordinary quarter = the **full estimated 2025 instalment payment base** / 4, including applicable CPP/EI payable after the tax-only threshold test. [Official source](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/instalment-chart-fill-25e.pdf)
- Interest risk if estimate too low

Method 1 requires the actual reminder amounts paid in full on time. Methods 2 and 3 also depend on correctly calculated, adequate amounts and timely payment. Do not certify an estimate as interest-free before those conditions are established. ITA 161(4.01)(a)-(d) includes current tax, prior instalment base, the statutory two-year method and amounts in the Minister's notices; its least-total calculation applies for interest/penalty purposes. [ITA 161(4.01)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-161.html); [CRA options](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/options-calculate.html)

### 5.4 Instalment interest

- **Instalment interest** — Interest on shortfall = overdue-taxes prescribed rate (base rate + 4 percentage points), compounded daily, from due date to payment date or April 30 balance-due date. Overpayment in one quarter offsets underpayment in another (contra interest).

### 5.5 Instalment penalty

- **Instalment penalty** — If instalment interest exceeds $1,000, calculate max(0, I − max(1000, 0.25 × I_if_none)) / 2. With I = $2,500 and I_if_none = $3,200, the penalty is **$750**, not $375. [Official source](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/interest-penalty-charges.html); [ITA 163.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-163.1.html)

## Section 6 -- Penalties and interest

### 6.1 Instalment interest

- **Instalment interest rate** — Use the published overdue-debt rate. Regulation 4301(a) uses the prescribed base plus **4 percentage points**, not the separate refund uplift; do not add four points again to an already-published overdue rate. The applicable rate can change by quarter and interest compounds daily. [ITR 4301(a)](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-4301.html); [Official source](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/interest-penalty-charges.html)

### 6.2 Instalment penalty

- **Instalment penalty formula** — Only if interest exceeds $1,000: max(0, I − max(1000, 0.25 × I_if_none)) / 2. The statutory 50% is this single division by two, not an additional halving. [ITA 163.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-163.1.html)

### 6.3 Late filing

- **Late filing** — Ordinary 2025 balance is due **30 April 2026**; the ordinary self-employed filing deadline is **15 June 2026**, not a later payment deadline. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html) Ordinary first-failure late-filing penalty with unpaid tax is 5% plus 1% per full month, up to 12 months; the repeated-failure regime is separate. [ITA 162](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html)

## Section 7 -- Provincial considerations

- **Provincial considerations** — For non-Quebec residents: federal and provincial tax are combined on T1, so instalments cover both. For Quebec residents: federal instalments cover federal tax only (threshold $1,800). Revenu Quebec administers separate provincial instalments (threshold $1,800 of Quebec tax).

## Section 8 -- Edge cases

For an ordinary non-Quebec individual, if NTO does not exceed $3,000 in both 2023 and 2024, no 2025 instalments are required even if 2025 will be substantial. Apply the $1,800 threshold for Quebec, and the separate all-three-year farming/fishing test. Flag the remaining balance for cash planning.

No instalment is required on or after the date of death. **HOLD:** settle any earlier liability and use the actual final-return/payment rules for the death date; the six-month wording is not a universal extension for every prior-year return or balance. [ITA 156.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html); [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/life-events/doing-taxes-someone-died/prepare-returns/filing-deadlines.html)

For the statutory farming/fishing regime, use the annual December 31 rule and full payment base, not net tax alone. Eligibility history, applicable CPP/EI and the chart/statute fraction discrepancy remain required checks.

Federal threshold $1,800. Provincial instalments administered by Revenu Quebec separately.

Taxpayers below threshold may make voluntary payments. No penalty for not paying.

Moves to next business day (Interpretation Act s 26).

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] Net tax owing threshold ($3,000 or $1,800 QC) checked for current and two prior years
- [ ] Correct calculation method identified
- [ ] All four due dates correct (Mar 15, Jun 15, Sep 15, Dec 15)
- [ ] NTO bound to the specific 2025 chart lines; no generic refundable-credit/CPP-overpayment shortcut
- [ ] Full payment base includes applicable CPP/EI payable after the eligibility test
- [ ] Farming/fishing exception checked
- [ ] Provincial treatment correct (combined for non-QC, separate for QC)
- [ ] Interest exposure quantified if underpayment likely
- [ ] First-year exception noted if applicable
- [ ] Weekend/holiday adjustments applied
- [ ] Output labelled as estimated until Canadian CPA confirms

## Section 10 -- Test suite

### Test 1 -- No-calculation method

**Input:** 2023 NTO = $25,000. 2024 NTO = $28,000.
**Expected:** Conditional arithmetic with zero applicable CPP/EI additions and matching reminder bases: Q1, Q2 = $6,250 each; Q3, Q4 = $7,750 each; total = $28,000. Otherwise HOLD actual required amounts.

### Test 2 -- Prior-year method

**Input:** 2024 NTO = $28,000.
**Expected:** With zero applicable CPP/EI additions: each quarter = $7,000, total $28,000. With $4,000 of additions: each quarter = $8,000, total $32,000. HOLD until additions are established.

### Test 3 -- Below threshold

**Input:** 2024 NTO = $2,500. 2023 NTO = $2,800.
**Expected:** No ordinary non-Quebec instalments required. For Quebec, HOLD until prior-year amounts are recomputed using the Quebec-specific federal NTO definition and current-year NTO is supplied.

### Test 4 -- Farming exception

**Input:** Farmer. Expected NTO = $18,000.
**Expected:** Arithmetic-only $12,000 at the statutory two-thirds fraction; HOLD required payment pending chief-source eligibility, all three threshold years, full payment bases and resolution of the CRA chart/statute discrepancy.

### Test 5 -- First year of SE

**Input:** 2023 NTO = $500. 2024 NTO = $800. Expected 2025 NTO = $25,000.
**Expected:** No instalments (prior years below $3,000). Flag: large balance due April 30, 2026.

### Test 6 -- Quebec resident

**Input:** Quebec resident. Federal NTO = $2,000.
**Expected:** Current federal threshold $1,800 exceeded, but HOLD the obligation conclusion until the necessary prior-year history is supplied. Provincial obligations are separately administered by Revenu Quebec.

These checks recompute illustrations only. They do not establish missing eligibility, reminder, payment-base or timing inputs.

```oa-check
name: Original 2023 and 2024 bases, zero CPP/EI additions assumed
inputs:
  second_prior: 25000
  prior: 28000
steps:
  q1: second_prior / 4
  q2: q1
  q3: (prior - q1 - q2) / 2
  q4: q3
  total: q1 + q2 + q3 + q4
expected:
  q1: 6250
  q2: 6250
  q3: 7750
  q4: 7750
  total: 28000
```

```oa-check
name: Prior-year base omission counterexample
inputs:
  nto: 28000
  cpp_ei: 4000
steps:
  tax_only_quarter: nto / 4
  full_base: nto + cpp_ei
  full_quarter: full_base / 4
expected:
  tax_only_quarter: 7000
  full_base: 32000
  full_quarter: 8000
```

```oa-check
name: Farming arithmetic only, actual obligation held
inputs:
  amount: 18000
steps:
  two_thirds: amount * 2 / 3
expected:
  two_thirds: 12000
```

```oa-check
name: Instalment penalty uses one halving
inputs:
  interest: 2500
  interest_if_none: 3200
steps:
  floor: max(1000, interest_if_none * 0.25)
  penalty: max(0, interest - floor) / 2
expected:
  floor: 1000
  penalty: 750
```

## Sources

Completed reads below are from 21 November 2026 and reused for this unchanged 2025 baseline. The 25 November options/interest follow-up resolves the contradictory interest guarantees; those current pages present 2026, so their year labels do not replace the historical 2025 worksheet or original example years. A source receipt is limited to the stated operative scope, not a certification of the whole skill.

| Primary source | Completed read scope | Read date |
| --- | --- | --- |
| [ITA 156.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html) | Subsections (1)-(4): NTO definition, ordinary/farming threshold tests and death exception | 2026-11-21 |
| [ITA 156](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.html) | Subsection (1): quarterly dates, fractions and year/base structure | 2026-11-21 |
| [CRA payment due dates](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html) and [Interpretation Act 26](https://laws-lois.justice.gc.ca/eng/acts/I-21/section-26.html) | Nominal dates and weekend/holiday handling; synthetic bank dates are not statutory verification | 2026-11-21 |
| [CRA 2025 instalment chart](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/instalment-chart-fill-25e.pdf) | Both pages: specific NTO payable/credit lines, applicable CPP/EI additions after eligibility; chart's 66% differs from statutory two-thirds | 2026-11-21 |
| [ITR 4301](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-4301.html) | Paragraphs (a)-(b): debt base-plus-four versus refund base-plus-two; do not uplift a published overdue rate twice | 2026-11-21 |
| [CRA interest and penalty](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/interest-penalty-charges.html) | Interest/credit mechanics and complete penalty example; follow-up on the stated charging conditions and least-interest option, not a no-calculation safe-harbour statement | 2026-11-21; bounded follow-up 2026-11-25 |
| [ITA 163.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-163.1.html) | Complete operative penalty section: one 50% calculation, not two halvings | 2026-11-21 |
| [ITA 155](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-155.html) | Complete operative section: farming/fishing annual rule, two-thirds fraction, current estimated tax and prior prescribed instalment base | 2026-11-21; bounded follow-up 2026-11-25 |
| [CRA individual dates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html) | Explicit 2025 return/payment dates in 2026; filing and payment distinguished | 2026-11-21 |
| [ITA 162](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html) | Subsections (1)-(2): ordinary and repeated-failure late-filing conditions | 2026-11-21 |
| [CRA deceased filing/payment deadlines](https://www.canada.ca/en/revenue-agency/services/tax/individuals/life-events/doing-taxes-someone-died/prepare-returns/filing-deadlines.html) | Final-return, prior-year and self-employed distinctions; actual death-date result remains held | 2026-11-21 |
| [Revenu Québec instalments](https://www.revenuquebec.ca/en/citizens/income-tax-return/paying-a-balance-due-or-receiving-a-refund/instalment-payments/making-instalment-payments/) | Provincial threshold, reminder and farmer paragraphs; separate administration | 2026-11-21 |
| [CRA calculation options](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/options-calculate.html) | No-calculation reminder description and prior/current-year amount/timing conditions; no-calculation interest protection rests on ITA 161(4.01), not this page; current 2026 inputs not substituted into this 2025 workpaper | 2026-11-21; bounded follow-up 2026-11-25 |
| [ITA 161](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-161.html) | Subsections (2), (4) and (4.01), including complete (a)-(d) and closing limitation: instalment interest and least-amount statutory alternatives/notices; no complete personal interest computation certified | 2026-11-25 |

**Not yet confirmed:** individual obligation/payment amount without the full applicable history, chart base or reminder; farming/fishing chief-source and three-year conditions in the original example; the chart/statute fraction discrepancy; actual death-date final/prior-year deadlines; Quebec's missing prior-year example inputs; payment timing and sufficient estimates for interest protection; and bank-debit classification without reconciliation evidence. These holds prevent final use of the affected result, not discussion of the scoped rule or illustration.

## Prohibitions

- NEVER require instalments without checking the two-year threshold history
- NEVER confuse the three calculation methods -- each has different basis
- NEVER give an unconditional interest guarantee for any method; bind its actual amount and due-date conditions
- NEVER combine Quebec provincial tax into federal instalments
- NEVER ignore the farming/fishing single-instalment exception
- NEVER forget that self-employed filers have June 15 filing deadline but April 30 interest start
- NEVER present amounts as definitive -- advise confirmation with Canadian CPA

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
