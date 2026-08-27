---
name: nz-provisional-tax
description: Use this skill whenever asked about New Zealand provisional tax for individuals, companies, contractors, sole traders, and small businesses. Trigger on phrases like "provisional tax", "RIT", "residual income tax", "standard option", "standard uplift", "estimation method", "AIM", "ratio option", "use of money interest", "UOMI", "provisional tax instalment", or any question about provisional tax obligations in New Zealand. Covers the $5,000 RIT threshold, standard option 105%/110% uplift rules, estimation, AIM, ratio-option routing, March balance-date instalments, 6-monthly GST two-instalment cases, and current UOMI rate handling. ALWAYS read this skill before touching any NZ provisional tax work.
version: 2.0
jurisdiction: NZ
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NZ Provisional Tax

## Section 1 -- Quick reference

**Quick reference field table**  _(https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option)_

| Field | Value |
| --- | --- |
| Country | New Zealand |
| Tax | Provisional income tax |
| Primary legislation | Income Tax Act 2007 (ITA 2007), Part RC |
| Supporting legislation | Tax Administration Act 1994 (TAA 1994), ss 120A-120Q (UOMI) |
| Authority | Inland Revenue (IR / Te Tari Taake) |
| Portal | myIR (myir.ird.govt.nz) |
| Currency | NZD only |
| Threshold | RIT (residual income tax) must exceed $5,000 to trigger obligation |
| Default method | Standard option: previous-year RIT + 5% (105%) if filed by the instalment; otherwise two-years-ago RIT + 10% (110%) until recalculated |
| Alternative methods | Estimation method, AIM (Accounting Income Method), and ratio option where available |
| Standard balance date | 31 March |
| Standard dates | 28 August, 15 January, and 7 May for standard/estimation; next working day if a date falls on a weekend or public holiday |
| 6-monthly GST dates | Usually two instalments for a 31 March balance date: 28 October and 7 May |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by NZ Chartered Accountant (CA) |
| Validation date | July 2026 source refresh |

**Standard instalment schedule (31 March balance date)**  _(https://www.ird.govt.nz/income-tax/provisional-tax/paying-your-provisional-tax/payment-dates-for-provisional-tax)_

| Instalment | Due date | Amount |
| --- | --- | --- |
| 1st | 28 August | 1/3 of standard-option amount (105% or 110%, as applicable) |
| 2nd | 15 January | 1/3 of standard-option amount (105% or 110%, as applicable) |
| 3rd | 7 May | 1/3 of standard-option amount (105% or 110%, as applicable) |
| 6-monthly GST / qualifying two-instalment case | 28 October and 7 May | 1/2 of standard-option amount each |

**Conservative defaults**  _(https://www.ird.govt.nz/income-tax/provisional-tax/paying-your-provisional-tax/payment-dates-for-provisional-tax)_

| Ambiguity | Default |
| --- | --- |
| Method unclear | Use standard option and check 105% vs 110%, GST filing frequency, and UOMI exposure |
| RIT threshold borderline | If exactly $5,000, no provisional tax (must EXCEED $5,000) |
| Balance date non-standard | Use IR's due-date calculator / provisional tax calendar; dates differ for non-31 March balance dates |
| Tax agent EOT / 6-monthly GST | May change to two instalments (commonly 28 October and 7 May) -- confirm in myIR or the IR calendar |
| First year with no prior RIT | No compulsory provisional tax from prior-year RIT; voluntary payments may be sensible for cash flow |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Minimum viable** — previous-year RIT, whether that return has been filed by the instalment date, any two-years-ago RIT fallback, balance date, GST filing frequency, and chosen method (standard option, estimation, AIM, or ratio).  _(https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option)_
- **Recommended** — balance date, tax agent status (EOT), GST registration status, current year income trend.
- **Ideal** — complete prior year tax return, IR assessment, myIR statement, current year P&L if estimating.
- **Refusal policy if minimum is missing** — HARD STOP. Without prior-year RIT and filing-status timing, the standard option cannot be computed. If the previous-year return is not filed by the relevant instalment, two-years-ago RIT may be needed for the 110% fallback. If estimating, current-year projections are needed.  _(https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option)_

### Refusal catalogue

- **R-NZ-PT-1 -- Pooling arrangements** — Trigger: client uses provisional tax pooling. Message: "Tax pooling arrangements have specific rules outside this skill."  _(R-NZ-PT-1)_
- **R-NZ-PT-2 -- Multi-entity structures** — Trigger: complex multi-entity group. Message: "Multi-entity provisional tax allocation is outside this skill."  _(R-NZ-PT-2)_
- **R-NZ-PT-3 -- Non-resident provisional tax** — Trigger: non-resident client. Message: "Non-resident provisional tax is outside this skill."  _(R-NZ-PT-3)_

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as a provisional tax payment.

### 3.1 Inland Revenue provisional tax debits

**Inland Revenue provisional tax debits**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IRD, INLAND REVENUE, IR PAYMENT | Provisional tax payment | Match with Aug/Jan/May timing |
| PROVISIONAL TAX, PROV TAX | Provisional tax payment | Explicit description |
| MYIR PAYMENT | Provisional tax payment | Online payment via myIR |
| TERMINAL TAX | NOT provisional tax | Year-end balance -- flag separately |

### 3.2 Timing-based identification

**Timing-based identification**

| Debit date range | Likely instalment | Confidence |
| --- | --- | --- |
| 20 August -- 5 September | 1st instalment (28 Aug) | High if IR payee |
| 8 January -- 20 January | 2nd instalment (15 Jan) | High |
| 1 May -- 14 May | 3rd instalment (7 May) | High |
| January -- February (following year) | Terminal tax | Flag separately |

### 3.3 Related but NOT provisional tax

**Related but NOT provisional tax**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GST, GOODS AND SERVICES TAX | EXCLUDE | GST payment |
| ACC LEVY | EXCLUDE | Accident Compensation levy |
| STUDENT LOAN | EXCLUDE | Student loan repayment |
| KIWISAVER | EXCLUDE | Retirement savings |
| CHILD SUPPORT, IR CHILD | EXCLUDE | Child support via IR |
| PENALTIES AND INTEREST IR | EXCLUDE | Penalty/interest charge |
| TERMINAL TAX | Flag separately | Year-end balance, not provisional |

### 3.4 Tax agent EOT identification

- **Tax agent EOT identification** — If the client uses a tax agent with extension of time, or is registered for GST and files 6-monthly, instalment dates can shift. Common two-instalment pattern for a 31 March balance date: 28 October and 7 May, each 50% of the standard-option amount. Confirm in myIR or IR's provisional tax calendar.  _(https://www.ird.govt.nz/income-tax/provisional-tax/paying-your-provisional-tax/payment-dates-for-provisional-tax)_

## Section 4 -- Worked examples

### Example 1 -- Standard uplift, three instalments

**Example 1 instalment table**

| Instalment | Due date | Amount |
| --- | --- | --- |
| 1st | 28 August | $5,250 |
| 2nd | 15 January | $5,250 |
| 3rd | 7 May | $5,250 |
| **Total** |  | **$15,750** |

**Input:** Prior year RIT = $15,000. Standard uplift. 31 March balance date.

(Calculation: $15,000 x 105% = $15,750. Each instalment = $15,750 / 3 = $5,250.)

### Example 2 -- Below threshold

**Input:** Prior year RIT = $4,800.

**Output:** RIT does not exceed $5,000. No provisional tax required. Client pays terminal tax only.

### Example 3 -- Estimation method

**Input:** Prior year RIT = $25,000. Estimated current year RIT = $12,000.

**Output:** Standard option at 105% would require $26,250 if the previous-year return was filed by the instalment date. Estimation method: pay $12,000 / 3 = $4,000 per instalment. Warning: if actual RIT > $12,000, UOMI applies from instalment dates.

### Example 4 -- Tax agent EOT (two instalments)

**Example 4 instalment table**

| Instalment | Due date | Amount |
| --- | --- | --- |
| 1st | 28 October | $26,250 |
| 2nd | 7 May | $26,250 |

**Input:** Prior year RIT = $50,000. Tax agent with EOT.

(Calculation: $50,000 x 105% = $52,500. Two instalments of $26,250.)

### Example 5 -- Bank statement classification

**Input line:** `28.08.2025 ; IRD PROVISIONAL TAX ; DEBIT ; -5,250.00 ; NZD`

**Classification:** Provisional tax, 1st instalment 2025/26. Tax payment -- not a deductible expense.

## Section 5 -- Computation rules

### 5.1 RIT threshold

- **RIT threshold formula** — RIT = income_tax_assessed - PAYE_credits - RWT_credits - other_withholding if RIT > 5,000: provisional tax required if RIT <= 5,000: no provisional tax (terminal tax only)
- **First-year exemption** — no provisional tax in the first year of earning income giving rise to RIT.

### 5.2 Standard uplift method

- **Standard option formula** — provisional_tax = prior_year_RIT x 105% each_instalment = provisional_tax / number_of_instalments (3 standard, 2 with EOT)  _(https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option)_
- **Safe harbour** — if standard-option instalments are paid on time and in full, UOMI exposure is reduced. Do not state there is blanket immunity: late or short payments can attract interest, and if actual RIT is $60,000 or more, UOMI can apply from the day after the final instalment on the difference between actual RIT and provisional tax paid.  _(https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments)_

### 5.3 Estimation method

- **Estimation method formula** — provisional_tax = estimated_current_year_RIT each_instalment = provisional_tax / number_of_instalments
- **Risk** — UOMI is calculated by comparing provisional tax paid with actual RIT. Under estimation, underpayments can be charged from each instalment date; the client can re-estimate at an instalment date.  _(https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments)_

### 5.4 AIM method

- **AIM method** — Tax calculated each period based on actual accounting income via AIM-capable software. AIM aligns with GST return periods; no UOMI is charged or paid if AIM statements and payments are correct and on time. Requires gross income under $5,000,000.  _(https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option)_

### 5.5 Terminal tax

- **Terminal tax formula** — terminal_tax = actual_RIT - provisional_tax_paid
- **Terminal tax due date** — Due 7 February (without EOT) or 7 April (with EOT).

## Section 6 -- Penalties and interest

### 6.1 Use of Money Interest (UOMI)

**UOMI rate table**  _(https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments)_

| Effective from | IR charges on underpayments | IR pays on overpayments |
| --- | --- | --- |
| 16 January 2026 | 8.97% | 2.25% |
| 8 May 2025 | 9.89% | 3.27% |
| 16 January 2025 | 10.88% | 4.30% |

### 6.2 UOMI exposure by method

**UOMI exposure by method**  _(https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments)_

| Method | UOMI exposure |
| --- | --- |
| Standard option, actual RIT under $60,000, required instalments paid full/on time | Generally no UOMI before terminal-tax timing |
| Standard option, actual RIT $60,000 or more | UOMI can apply from the day after the final instalment on the difference between actual RIT and provisional tax paid |
| Estimation | UOMI can apply from each instalment date if the estimate is too low |
| AIM (correct and on time) | No UOMI charged or paid |
| Ratio option (paid on time) | No UOMI charged or paid on provisional tax |

### 6.3 Late payment penalties

**Late payment penalties**

| Offence | Penalty |
| --- | --- |
| Late payment | 1% initial + 4% if still unpaid after 7 days |
| Late IR3 filing | $250 (may increase) |
| Shortfall from deliberate understatement | 20-150% |

## Section 7 -- Method selection guidance

**Method selection guidance table**  _(https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option)_

| Situation | Recommended method | Rationale |
| --- | --- | --- |
| Income stable or growing | Standard option | Predictable uplift; check 105% vs 110%, the $60,000 RIT rule, and due-date timing |
| Income dropping significantly | Estimation | Lower cash outflow, but UOMI and shortfall-penalty risk if too low |
| Irregular/seasonal income | AIM or ratio option | Pay closer to actual trading pattern; confirm eligibility and software/GST setup |
| First year of business | No compulsory provisional tax from prior-year RIT | Voluntary payments accepted; plan for terminal tax cash flow |

Flag estimation method for reviewer whenever recommended.

## Section 8 -- Edge cases

No provisional tax obligation. Terminal tax due 7 February following year-end. May voluntarily pay to avoid large lump sum.

Standard option at 105% = $31,500 but expected RIT = $10,000. Use estimation method ($10,000/3 per instalment). UOMI risk if actual exceeds estimate.

RIT = total tax minus PAYE credits. If RIT > $5,000, provisional tax on RIT amount.

Instalment dates shift. 30 September balance date: instalments 28 February, 15 July, 7 November.

No provisional tax. Must EXCEED $5,000.

First-year freelancer may make voluntary payments. UOMI overpayment interest may apply.

The 7 May instalment falls AFTER the 31 March year-end. This is correct by design.

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] RIT threshold ($5,000) confirmed -- must exceed, not equal
- [ ] Method selected (standard uplift, estimation, AIM)
- [ ] Uplift factor is 105% or 110% as applicable
- [ ] Correct number of instalments (3 standard, 2 with EOT)
- [ ] All instalment dates correct for the balance date
- [ ] UOMI exposure noted for estimation method
- [ ] Safe harbour benefit noted for standard uplift
- [ ] First-year exemption checked
- [ ] Terminal tax due date included
- [ ] Output labelled as estimated until NZ CA confirms

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

## Section 10 -- Test suite

## Prohibitions

- NEVER require provisional tax when prior year RIT is $5,000 or less
- NEVER state that standard-option payments eliminate all UOMI without checking late/short payments, terminal-tax timing, and the $60,000 actual RIT rule
- NEVER recommend estimation method without flagging UOMI risk
- NEVER apply 105% blindly when filing status requires the 110% two-years-ago RIT fallback
- NEVER confuse RIT with total income tax -- RIT is after deducting PAYE and other credits
- NEVER apply provisional tax in the first year of earning SE income (unless voluntary)
- NEVER ignore the 3rd instalment date falling after year-end
- NEVER present calculations as definitive -- direct to IR or NZ CA

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a New Zealand Chartered Accountant or equivalent licensed practitioner) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
