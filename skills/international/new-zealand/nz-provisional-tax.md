---
name: nz-provisional-tax
description: >
  Use this skill whenever asked about New Zealand provisional tax for self-employed individuals. Trigger on phrases like "provisional tax", "RIT", "residual income tax", "standard uplift", "estimation method", "AIM", "use of money interest", "UOMI", "provisional tax instalment", or any question about provisional tax obligations for sole traders in New Zealand. Covers the $5,000 RIT threshold, standard uplift (105%), estimation method, AIM method, instalment dates, and UOMI. ALWAYS read this skill before touching any NZ provisional tax work.
version: 2.0
jurisdiction: NZ
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# NZ Provisional Tax -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | New Zealand |
| Tax | Provisional income tax |
| Primary legislation | Income Tax Act 2007 (ITA 2007), Part RC |
| Supporting legislation | Tax Administration Act 1994 (TAA 1994), ss 120A-120Q (UOMI) |
| Authority | Inland Revenue (IR / Te Tari Taake) |
| Portal | myIR (myir.ird.govt.nz) |
| Currency | NZD only |
| Threshold | RIT (residual income tax) must exceed $5,000 to trigger obligation |
| Default method | Standard uplift: prior year RIT x 105%, divided by 3 instalments |
| Alternative methods | Estimation method, AIM (Accounting Income Method) |
| Standard balance date | 31 March |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by NZ Chartered Accountant (CA) |
| Validation date | Pending |

**Standard instalment schedule (31 March balance date):**

| Instalment | Due date | Amount |
|---|---|---|
| 1st | 28 August | 1/3 of (RIT x 105%) |
| 2nd | 15 January | 1/3 of (RIT x 105%) |
| 3rd | 7 May | 1/3 of (RIT x 105%) |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Method unclear | Use standard uplift (no UOMI risk if paid on time) |
| RIT threshold borderline | If exactly $5,000, no provisional tax (must EXCEED $5,000) |
| Balance date non-standard | Verify instalment dates in IR's provisional tax calendar |
| Tax agent EOT | May change to 2 instalments -- confirm |
| First year of SE income | No provisional tax obligation |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- prior year residual income tax (RIT) figure and chosen method (standard uplift, estimation, or AIM).

**Recommended** -- balance date, tax agent status (EOT), GST registration status, current year income trend.

**Ideal** -- complete prior year tax return, IR assessment, myIR statement, current year P&L if estimating.

**Refusal policy if minimum is missing -- HARD STOP.** Without the prior year RIT, the standard uplift cannot be computed. If estimating, current year projections are needed.

### Refusal catalogue

**R-NZ-PT-1 -- Pooling arrangements.** Trigger: client uses provisional tax pooling. Message: "Tax pooling arrangements have specific rules outside this skill."

**R-NZ-PT-2 -- Multi-entity structures.** Trigger: complex multi-entity group. Message: "Multi-entity provisional tax allocation is outside this skill."

**R-NZ-PT-3 -- Non-resident provisional tax.** Trigger: non-resident client. Message: "Non-resident provisional tax is outside this skill."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as a provisional tax payment.

### 3.1 Inland Revenue provisional tax debits

| Pattern | Treatment | Notes |
|---|---|---|
| IRD, INLAND REVENUE, IR PAYMENT | Provisional tax payment | Match with Aug/Jan/May timing |
| PROVISIONAL TAX, PROV TAX | Provisional tax payment | Explicit description |
| MYIR PAYMENT | Provisional tax payment | Online payment via myIR |
| TERMINAL TAX | NOT provisional tax | Year-end balance -- flag separately |

### 3.2 Timing-based identification

| Debit date range | Likely instalment | Confidence |
|---|---|---|
| 20 August -- 5 September | 1st instalment (28 Aug) | High if IR payee |
| 8 January -- 20 January | 2nd instalment (15 Jan) | High |
| 1 May -- 14 May | 3rd instalment (7 May) | High |
| January -- February (following year) | Terminal tax | Flag separately |

### 3.3 Related but NOT provisional tax

| Pattern | Treatment | Notes |
|---|---|---|
| GST, GOODS AND SERVICES TAX | EXCLUDE | GST payment |
| ACC LEVY | EXCLUDE | Accident Compensation levy |
| STUDENT LOAN | EXCLUDE | Student loan repayment |
| KIWISAVER | EXCLUDE | Retirement savings |
| CHILD SUPPORT, IR CHILD | EXCLUDE | Child support via IR |
| PENALTIES AND INTEREST IR | EXCLUDE | Penalty/interest charge |
| TERMINAL TAX | Flag separately | Year-end balance, not provisional |

### 3.4 Tax agent EOT identification

If the client uses a tax agent with extension of time, instalment dates shift. Common pattern: 28 October + 7 May (two instalments of 50% each).

---

## Section 4 -- Worked examples

### Example 1 -- Standard uplift, three instalments

**Input:** Prior year RIT = $15,000. Standard uplift. 31 March balance date.

| Instalment | Due date | Amount |
|---|---|---|
| 1st | 28 August | $5,250 |
| 2nd | 15 January | $5,250 |
| 3rd | 7 May | $5,250 |
| **Total** | | **$15,750** |

(Calculation: $15,000 x 105% = $15,750. Each instalment = $15,750 / 3 = $5,250.)

### Example 2 -- Below threshold

**Input:** Prior year RIT = $4,800.

**Output:** RIT does not exceed $5,000. No provisional tax required. Client pays terminal tax only.

### Example 3 -- Estimation method

**Input:** Prior year RIT = $25,000. Estimated current year RIT = $12,000.

**Output:** Standard uplift would require $26,250. Estimation method: pay $12,000 / 3 = $4,000 per instalment. Warning: if actual RIT > $12,000, UOMI applies from instalment dates.

### Example 4 -- Tax agent EOT (two instalments)

**Input:** Prior year RIT = $50,000. Tax agent with EOT.

| Instalment | Due date | Amount |
|---|---|---|
| 1st | 28 October | $26,250 |
| 2nd | 7 May | $26,250 |

(Calculation: $50,000 x 105% = $52,500. Two instalments of $26,250.)

### Example 5 -- Bank statement classification

**Input line:** `28.08.2025 ; IRD PROVISIONAL TAX ; DEBIT ; -5,250.00 ; NZD`

**Classification:** Provisional tax, 1st instalment 2025/26. Tax payment -- not a deductible expense.

---

## Section 5 -- Computation rules

### 5.1 RIT threshold

```
RIT = income_tax_assessed - PAYE_credits - RWT_credits - other_withholding
if RIT > 5,000: provisional tax required
if RIT <= 5,000: no provisional tax (terminal tax only)
```

First-year exemption: no provisional tax in the first year of earning income giving rise to RIT.

### 5.2 Standard uplift method

```
provisional_tax = prior_year_RIT x 105%
each_instalment = provisional_tax / number_of_instalments (3 standard, 2 with EOT)
```

Safe harbour: if each instalment is paid on time and in full, NO UOMI is charged even if actual RIT is much higher.

### 5.3 Estimation method

```
provisional_tax = estimated_current_year_RIT
each_instalment = provisional_tax / number_of_instalments
```

Risk: UOMI charged from each instalment date if estimate < actual RIT. Client can re-estimate at any instalment date.

### 5.4 AIM method

Tax calculated each period based on actual accounting income via AIM-capable software (Xero, MYOB). Aligned with GST return periods. No UOMI exposure if correct and on time. Requires gross income < $5,000,000.

### 5.5 Terminal tax

```
terminal_tax = actual_RIT - provisional_tax_paid
```

Due 7 February (without EOT) or 7 April (with EOT).

---

## Section 6 -- Penalties and interest

### 6.1 Use of Money Interest (UOMI)

| Rate type | Rate (verify annually) |
|---|---|
| Underpayment rate | ~10.91% (2025) |
| Overpayment rate | ~3.41% (2025) |

### 6.2 UOMI exposure by method

| Method | UOMI exposure |
|---|---|
| Standard uplift (paid on time) | None -- safe harbour |
| Estimation | UOMI from each instalment date if estimate < actual |
| AIM (correct and on time) | None |

### 6.3 Late payment penalties

| Offence | Penalty |
|---|---|
| Late payment | 1% initial + 4% if still unpaid after 7 days |
| Late IR3 filing | $250 (may increase) |
| Shortfall from deliberate understatement | 20-150% |

---

## Section 7 -- Method selection guidance

| Situation | Recommended method | Rationale |
|---|---|---|
| Income stable or growing | Standard uplift | Safe harbour, no UOMI risk |
| Income dropping significantly | Estimation | Lower cash outflow, but UOMI risk |
| Irregular/seasonal income | AIM | Pay as you earn, no UOMI |
| First year of business | No provisional tax | Exempt; voluntary payments accepted |

Flag estimation method for reviewer whenever recommended.

---

## Section 8 -- Edge cases

**EC1 -- First year of self-employment.** No provisional tax obligation. Terminal tax due 7 February following year-end. May voluntarily pay to avoid large lump sum.

**EC2 -- Income drops significantly.** Standard uplift = $31,500 but expected RIT = $10,000. Use estimation method ($10,000/3 per instalment). UOMI risk if actual exceeds estimate.

**EC3 -- Mixed PAYE and self-employment.** RIT = total tax minus PAYE credits. If RIT > $5,000, provisional tax on RIT amount.

**EC4 -- Non-standard balance date.** Instalment dates shift. 30 September balance date: instalments 28 February, 15 July, 7 November.

**EC5 -- RIT exactly $5,000.** No provisional tax. Must EXCEED $5,000.

**EC6 -- Voluntary payments.** First-year freelancer may make voluntary payments. UOMI overpayment interest may apply.

**EC7 -- 3rd instalment after year-end.** The 7 May instalment falls AFTER the 31 March year-end. This is correct by design.

---

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] RIT threshold ($5,000) confirmed -- must exceed, not equal
- [ ] Method selected (standard uplift, estimation, AIM)
- [ ] Uplift factor is 105%
- [ ] Correct number of instalments (3 standard, 2 with EOT)
- [ ] All instalment dates correct for the balance date
- [ ] UOMI exposure noted for estimation method
- [ ] Safe harbour benefit noted for standard uplift
- [ ] First-year exemption checked
- [ ] Terminal tax due date included
- [ ] Output labelled as estimated until NZ CA confirms

---

## Section 10 -- Test suite

### Test 1 -- Standard uplift
**Input:** Prior year RIT = $15,000. 31 March balance date.
**Expected:** $15,750 total. 3 x $5,250. Dates: 28 Aug, 15 Jan, 7 May.

### Test 2 -- Below threshold
**Input:** Prior year RIT = $4,800.
**Expected:** No provisional tax.

### Test 3 -- Estimation method
**Input:** Prior year RIT = $25,000. Estimated current = $12,000.
**Expected:** $4,000 per instalment. UOMI warning.

### Test 4 -- Tax agent EOT
**Input:** Prior year RIT = $50,000.
**Expected:** $52,500 total. 2 x $26,250. Dates: 28 Oct, 7 May.

### Test 5 -- First year
**Input:** New freelancer, no prior RIT.
**Expected:** No provisional tax. Terminal tax by 7 Feb.

### Test 6 -- RIT exactly $5,000
**Input:** Prior year RIT = $5,000.
**Expected:** No provisional tax (must exceed $5,000).

### Test 7 -- Mixed PAYE and SE
**Input:** PAYE salary $60,000. SE $20,000. RIT = $6,000.
**Expected:** Provisional tax on $6,000 RIT. Uplift: $6,300 / 3 = $2,100.

---

## Prohibitions

- NEVER require provisional tax when prior year RIT is $5,000 or less
- NEVER apply UOMI to standard uplift payments made on time and in full
- NEVER recommend estimation method without flagging UOMI risk
- NEVER use an uplift factor other than 105%
- NEVER confuse RIT with total income tax -- RIT is after deducting PAYE and other credits
- NEVER apply provisional tax in the first year of earning SE income (unless voluntary)
- NEVER ignore the 3rd instalment date falling after year-end
- NEVER present calculations as definitive -- direct to IR or NZ CA

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a New Zealand Chartered Accountant or equivalent licensed practitioner) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
