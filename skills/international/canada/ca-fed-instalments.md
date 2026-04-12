---
name: ca-fed-instalments
description: >
  Use this skill whenever asked about Canadian federal quarterly instalment requirements for self-employed individuals. Trigger on phrases like "CRA instalments", "quarterly tax Canada", "instalment reminder", "INNS1", "INNS2", "net tax owing", "$3,000 threshold", "instalment interest", or any question about quarterly income tax prepayments for Canadian individuals. Covers the $3,000 net-tax-owing threshold, three calculation methods (no-calculation, prior-year, current-year), instalment due dates (Mar 15, Jun 15, Sep 15, Dec 15), instalment interest and penalties, and interaction with provincial instalments. ALWAYS read this skill before touching any Canada estimated tax work.
version: 2.0
jurisdiction: CA-FED
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Canada Federal Quarterly Instalments -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Canada (federal) |
| Tax | Quarterly income tax instalments |
| Primary legislation | Income Tax Act (ITA), s 156 (instalment obligation); s 156.1 (Quebec residents) |
| Supporting legislation | ITA s 161(2) (interest); s 163.1 (penalty); Interpretation Act s 26 (due date rules) |
| Authority | Canada Revenue Agency (CRA) |
| Portal | My Account (cra-arc.gc.ca) |
| Currency | CAD only |
| Threshold | Net tax owing > $3,000 in current year AND either of two preceding years ($1,800 for Quebec residents, federal portion) |
| Payment schedule | Quarterly: March 15, June 15, September 15, December 15 |
| Three methods | No-calculation (CRA suggested), prior-year, current-year |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by Canadian CPA |
| Validation date | Pending |

**Instalment schedule summary:**

| Instalment | Due date |
|---|---|
| Q1 | March 15 |
| Q2 | June 15 |
| Q3 | September 15 |
| Q4 | December 15 |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Method selection | Use no-calculation (CRA suggested) or prior-year -- both guarantee no interest |
| Quebec resident | Federal threshold $1,800 (provincial administered separately by Revenu Quebec) |
| Farming/fishing income | Single annual instalment by December 31 may apply |
| First year of SE | May not meet two-year threshold -- check both prior years |
| Due date on weekend | Next business day |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- net tax owing for the current year and two preceding years (to confirm threshold), CRA instalment reminder (INNS1 or INNS2) if available.

**Recommended** -- T1 returns for prior two years, expected current year income and tax, province of residence.

**Ideal** -- complete three-year T1 history, CRA My Account statement, farming/fishing income status.

**Refusal policy if minimum is missing -- SOFT WARN.** Without two years of net tax owing history, the threshold test cannot be fully confirmed.

### Refusal catalogue

**R-CA-FI-1 -- Corporate instalments.** Trigger: client asks about corporate instalment requirements. Message: "Corporate instalments under ITA s 157 have different rules. This skill covers individuals only."

**R-CA-FI-2 -- GST/HST instalments.** Trigger: client asks about GST/HST instalments. Message: "GST/HST instalments are a separate obligation. See ca-fed-gst-hst."

**R-CA-FI-3 -- Trust instalment requirements.** Trigger: trust client. Message: "Trust instalments are outside this skill."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as a CRA instalment payment.

### 3.1 CRA instalment debits

| Pattern | Treatment | Notes |
|---|---|---|
| CRA, CANADA REVENUE AGENCY | Instalment payment | Match with Mar/Jun/Sep/Dec timing |
| CRA INSTALMENT, CRA INST | Instalment payment | Explicit description |
| RECEIVER GENERAL, REC GEN CANADA | Instalment payment | Federal government payee |
| CRA PRE-AUTHORIZED DEBIT | Instalment payment | Automatic payment |
| MY PAYMENT CRA | Instalment payment | Online payment via My Account |

### 3.2 Timing-based identification

| Debit date range | Likely instalment | Confidence |
|---|---|---|
| 10 March -- 20 March | Q1 (Mar 15) | High if CRA payee |
| 10 June -- 20 June | Q2 (Jun 15) | High |
| 10 September -- 20 September | Q3 (Sep 15) | High |
| 10 December -- 20 December | Q4 (Dec 15) | High |
| April -- May | Balance owing from prior year return | Flag separately |

### 3.3 Related but NOT income tax instalments

| Pattern | Treatment | Notes |
|---|---|---|
| CRA GST, GST/HST | EXCLUDE | GST/HST payment |
| CRA CPP, CPP PAYMENT | EXCLUDE | CPP contribution (if separate) |
| CRA CHILD BENEFIT, CCB | EXCLUDE (credit) | Canada Child Benefit receipt |
| REVENU QUEBEC, MRQ | EXCLUDE | Provincial instalment (Quebec) |
| CRA PENALTY, CRA INTEREST | EXCLUDE | Penalty/interest charge |
| CRA REFUND | Flag for reviewer | Tax refund |

### 3.4 Payment references

| Reference pattern | Treatment | Notes |
|---|---|---|
| SIN + INST or INSTALMENT | CRA instalment | Standard reference format |
| Tax year + Q1/Q2/Q3/Q4 | CRA instalment, specific quarter | Self-identified |

---

## Section 4 -- Worked examples

### Example 1 -- No-calculation method

**Input:** 2023 net tax owing = $25,000. 2024 net tax owing = $28,000.

| Instalment | Due date | Amount | Basis |
|---|---|---|---|
| Q1 | 15 Mar | $6,250 | 1/4 of 2023 ($25,000) |
| Q2 | 15 Jun | $6,250 | 1/4 of 2023 ($25,000) |
| Q3 | 15 Sep | $7,750 | ($28,000 - $12,500) / 2 |
| Q4 | 15 Dec | $7,750 | ($28,000 - $12,500) / 2 |
| **Total** | | **$28,000** | |

### Example 2 -- Prior-year method

**Input:** 2024 net tax owing = $28,000.

**Output:** Each quarter = $28,000 / 4 = $7,000. Total = $28,000. No interest guaranteed.

### Example 3 -- Below threshold

**Input:** 2024 net tax owing = $2,500. 2023 net tax owing = $2,800.

**Output:** Below $3,000 in both preceding years. No instalments required. Balance due April 30, 2026.

### Example 4 -- Farming/fishing exception

**Input:** Chief source of income is farming. Expected 2025 net tax = $18,000.

**Output:** Single annual instalment by December 31: 2/3 of $18,000 = $12,000. Or 2/3 of prior year.

### Example 5 -- Bank statement classification

**Input line:** `15.03.2025 ; CRA INSTALMENT PAYMENT ; DEBIT ; -7,000.00 ; CAD`

**Classification:** Federal income tax instalment, Q1 2025. Tax payment -- not a deductible expense.

---

## Section 5 -- Computation rules

### 5.1 Threshold test

Instalments required if net tax owing > $3,000 in BOTH:
- Current year (2025), AND
- Either of two preceding years (2024 or 2023)

Quebec residents: federal threshold is $1,800.

### 5.2 Net tax owing

```
net_tax_owing = total_federal_tax + total_provincial_tax
               - tax_withheld_at_source
               - refundable_credits
               - CPP/EI_overpayments
```

For non-Quebec residents: federal and provincial combined. For Quebec: federal only.

### 5.3 Three calculation methods

**Method 1 -- No-calculation (CRA suggested):**
- Q1, Q2: 1/4 of net tax owing from 2 years prior (2023)
- Q3, Q4: (net tax owing from 1 year prior (2024) - Q1 - Q2) / 2

**Method 2 -- Prior-year:**
- Each quarter = prior year (2024) net tax owing / 4

**Method 3 -- Current-year:**
- Each quarter = estimated 2025 net tax owing / 4
- Interest risk if estimate too low

Methods 1 and 2 guarantee no instalment interest. Method 3 carries risk.

### 5.4 Instalment interest

Interest on shortfall = CRA prescribed rate + 2%, compounded daily, from due date to payment date or April 30 balance-due date.

Overpayment in one quarter offsets underpayment in another (contra interest).

### 5.5 Instalment penalty

Applies if instalment interest exceeds $1,000:
```
penalty = 50% x (instalment_interest - max($1,000, 25% x interest_if_no_payments))
```

---

## Section 6 -- Penalties and interest

### 6.1 Instalment interest

Rate: CRA prescribed rate + 2% (updated quarterly). Compounded daily. Runs from instalment due date.

### 6.2 Instalment penalty

Only if interest exceeds $1,000. Penalty = 50% of excess over threshold.

### 6.3 Late filing

Balance-due date: April 30 (June 15 for self-employed filers, but interest runs from April 30). Late filing penalty: 5% + 1% per month (max 12 months).

---

## Section 7 -- Provincial considerations

For non-Quebec residents: federal and provincial tax are combined on T1, so instalments cover both.

For Quebec residents: federal instalments cover federal tax only (threshold $1,800). Revenu Quebec administers separate provincial instalments (threshold $1,800 of Quebec tax).

---

## Section 8 -- Edge cases

**EC1 -- First year of self-employment.** If net tax owing < $3,000 in both 2023 and 2024, no instalments required in 2025 even if 2025 will be substantial. Flag for reviewer -- client should set aside estimated tax.

**EC2 -- Deceased taxpayer.** Legal representative must pay outstanding instalments up to date of death. Remaining tax due on balance-due date or 6 months after death, whichever is later.

**EC3 -- Farming/fishing.** Single annual instalment by December 31 = 2/3 of estimated or prior year net tax.

**EC4 -- Quebec resident.** Federal threshold $1,800. Provincial instalments administered by Revenu Quebec separately.

**EC5 -- Voluntary payments.** Taxpayers below threshold may make voluntary payments. No penalty for not paying.

**EC6 -- Due date on weekend.** Moves to next business day (Interpretation Act s 26).

---

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] Net tax owing threshold ($3,000 or $1,800 QC) checked for current and two prior years
- [ ] Correct calculation method identified
- [ ] All four due dates correct (Mar 15, Jun 15, Sep 15, Dec 15)
- [ ] Net tax owing correctly calculated (total tax - withholdings - refundable credits)
- [ ] Farming/fishing exception checked
- [ ] Provincial treatment correct (combined for non-QC, separate for QC)
- [ ] Interest exposure quantified if underpayment likely
- [ ] First-year exception noted if applicable
- [ ] Weekend/holiday adjustments applied
- [ ] Output labelled as estimated until Canadian CPA confirms

---

## Section 10 -- Test suite

### Test 1 -- No-calculation method
**Input:** 2023 NTO = $25,000. 2024 NTO = $28,000.
**Expected:** Q1, Q2 = $6,250 each. Q3, Q4 = $7,750 each. Total = $28,000.

### Test 2 -- Prior-year method
**Input:** 2024 NTO = $28,000.
**Expected:** Each quarter = $7,000. Total = $28,000.

### Test 3 -- Below threshold
**Input:** 2024 NTO = $2,500. 2023 NTO = $2,800.
**Expected:** No instalments required.

### Test 4 -- Farming exception
**Input:** Farmer. Expected NTO = $18,000.
**Expected:** Single instalment Dec 31 = $12,000 (2/3).

### Test 5 -- First year of SE
**Input:** 2023 NTO = $500. 2024 NTO = $800. Expected 2025 NTO = $25,000.
**Expected:** No instalments (prior years below $3,000). Flag: large balance due April 30, 2026.

### Test 6 -- Quebec resident
**Input:** Quebec resident. Federal NTO = $2,000.
**Expected:** Federal threshold $1,800 exceeded. Federal instalments required. Provincial handled by Revenu Quebec.

---

## Prohibitions

- NEVER require instalments without checking the two-year threshold history
- NEVER confuse the three calculation methods -- each has different basis
- NEVER guarantee no interest for the current-year method -- only methods 1 and 2 are safe
- NEVER combine Quebec provincial tax into federal instalments
- NEVER ignore the farming/fishing single-instalment exception
- NEVER forget that self-employed filers have June 15 filing deadline but April 30 interest start
- NEVER present amounts as definitive -- advise confirmation with Canadian CPA

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
