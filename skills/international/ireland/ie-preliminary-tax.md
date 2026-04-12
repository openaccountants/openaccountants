---
name: ie-preliminary-tax
description: >
  Use this skill whenever asked about Irish Preliminary Tax for self-employed individuals. Trigger on phrases like "preliminary tax Ireland", "Form 11", "self-assessed tax Ireland", "October 31 deadline", "ROS filing", "100% rule preliminary tax", "90% rule Ireland", or any question about estimated tax payment obligations for a self-employed client in Ireland. Covers the 100%/90% prior-year/current-year rules, payment deadlines, and surcharges. ALWAYS read this skill before touching any Ireland preliminary tax work.
version: 2.0
jurisdiction: IE
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Ireland Preliminary Tax -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Ireland |
| Tax | Preliminary income tax (income tax + USC + PRSI Class S) |
| Primary legislation | TCA 1997, Part 41A (Self-Assessment), ss. 952-959 |
| Supporting legislation | TCA 1997, s.1080 (interest), s.1084 (surcharges); Finance Acts |
| Authority | Revenue Commissioners (Revenue) |
| Portal | ROS (Revenue Online Service) |
| Currency | EUR only |
| Payment schedule | Annual lump sum: 31 October (paper) or ~14 November (ROS) |
| Safe harbours | 100% of prior year liability OR 90% of current year liability |
| De minimis | Prior year liability <= EUR 200: no preliminary tax required |
| Components | Income tax + USC + PRSI (Class S at 4%) |
| CGT | Separate payment dates (15 Dec / 31 Jan) -- NOT part of preliminary tax |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires validation by Irish Chartered Accountant or CTA |
| Validation date | Pending |

**Key dates (tax year 2025):**

| Event | Paper deadline | ROS deadline |
|---|---|---|
| Pay 2025 preliminary tax | 31 Oct 2025 | ~14 Nov 2025 |
| File 2024 Form 11 | 31 Oct 2025 | ~14 Nov 2025 |
| Pay 2024 balance of tax | 31 Oct 2025 | ~14 Nov 2025 |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Rule selection unclear | Use 100% of prior year (safe, no estimation needed) |
| Filing method unclear | Confirm paper vs ROS (2-week difference in deadline) |
| CGT included in preliminary | EXCLUDE -- separate dates |
| First year of self-assessment | Must use 90% rule (no prior year available) |
| Prior year liability unknown | STOP -- the 100% rule requires prior year figure |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- prior year final tax liability (income tax + USC + PRSI) for the 100% rule, OR current year estimated income for the 90% rule.

**Recommended** -- filing method (paper vs ROS), PAYE credits from employment, CGT obligations (separate), current year income expectations.

**Ideal** -- complete prior year Form 11, Revenue assessment, current year P&L projection, PAYE certificates.

**Refusal policy if minimum is missing -- HARD STOP for 100% rule.** Without prior year liability, the 100% rule cannot be computed. For 90% rule, current year estimates needed.

### Refusal catalogue

**R-IE-PT-1 -- Trust/corporate preliminary tax.** Trigger: client asks about corporate or trust preliminary tax. Message: "This skill covers self-employed individuals only."

**R-IE-PT-2 -- CGT computation.** Trigger: client asks about CGT preliminary tax computation. Message: "CGT has separate payment dates (15 December / 31 January) and is NOT part of the 31 October preliminary tax payment. CGT computation is outside this skill."

**R-IE-PT-3 -- Non-resident self-assessment.** Trigger: non-resident client. Message: "Non-resident self-assessment is outside this skill."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as a preliminary tax payment.

### 3.1 Revenue preliminary tax debits

| Pattern | Treatment | Notes |
|---|---|---|
| REVENUE, REVENUE COMMISSIONERS | Preliminary tax payment | Match with October/November timing |
| ROS PAYMENT, ROS DEBIT | Preliminary tax payment | ROS online payment |
| PRELIMINARY TAX, PRELIM TAX | Preliminary tax payment | Explicit description |
| FORM 11, SELF ASSESSMENT | Preliminary tax or balance payment | Distinguish by timing |
| INCOME TAX REVENUE | Preliminary tax payment | Generic description |

### 3.2 Timing-based identification

| Debit date range | Likely payment | Confidence |
|---|---|---|
| 15 October -- 5 November | Preliminary tax (paper deadline 31 Oct) | High if Revenue payee |
| 1 November -- 20 November | Preliminary tax (ROS deadline ~14 Nov) | High |
| Same date: large single debit | Combined: balance of prior year + current year preliminary | Flag for reviewer to split |

### 3.3 Related but NOT preliminary tax

| Pattern | Treatment | Notes |
|---|---|---|
| CGT, CAPITAL GAINS TAX | EXCLUDE | Separate obligation, separate dates |
| PAYE, EMPLOYER PAYE | EXCLUDE | Employer PAYE payment |
| VAT, VAT3 RETURN | EXCLUDE | VAT payment |
| PRSI EMPLOYER | EXCLUDE | Employer PRSI |
| LOCAL PROPERTY TAX, LPT | EXCLUDE | Property tax |
| USC DIRECT | EXCLUDE | USC coded through employment |
| SURCHARGE, INTEREST REVENUE | EXCLUDE | Penalty/interest |

### 3.4 Direct debit identification

If the client pays preliminary tax by direct debit instalments (105% of pre-prior-year rule), monthly debits to Revenue throughout the year are direct debit preliminary tax payments. Flag for reviewer.

---

## Section 4 -- Worked examples

### Example 1 -- Standard 100% rule

**Input:** Prior year final liability = EUR 15,000 (income tax EUR 9,000 + USC EUR 3,500 + PRSI EUR 2,500).

**Output:** Preliminary tax = EUR 15,000. Due 31 Oct (paper) or ~14 Nov (ROS).

### Example 2 -- 90% rule, income drop

**Input:** Prior year liability = EUR 30,000. Current year estimated liability = EUR 10,000.

**Output:** 90% rule: EUR 10,000 x 90% = EUR 9,000. Saves EUR 21,000 vs 100% rule. Risk: if actual > estimate, interest applies on shortfall.

### Example 3 -- First year of self-employment

**Input:** First year, no prior year self-assessed liability. Estimated income EUR 60,000. Estimated tax: IT EUR 11,000 + USC EUR 2,400 + PRSI EUR 2,400 = EUR 15,800.

**Output:** 90% rule (only option). Preliminary = EUR 15,800 x 90% = EUR 14,220.

### Example 4 -- De minimis

**Input:** Prior year liability = EUR 120.

**Output:** Below EUR 200 de minimis. No preliminary tax required. Still must file Form 11.

### Example 5 -- CGT separate payment

**Input:** Income preliminary EUR 12,000 (due 31 Oct). CGT on June disposal = EUR 8,250.

**Output:** Income preliminary: EUR 12,000 due 31 Oct. CGT: EUR 8,250 due 15 Dec. Two separate payments.

### Example 6 -- Bank statement classification

**Input line:** `31.10.2025 ; REVENUE COMMISSIONERS ROS ; DEBIT ; PRELIMINARY TAX 2025 ; -15,000.00 ; EUR`

**Classification:** Preliminary tax for 2025. Tax payment -- not a deductible expense.

---

## Section 5 -- Computation rules

### 5.1 Two safe harbour rules

| Rule | Amount | When |
|---|---|---|
| 100% of prior year | 100% of prior year final liability | Safe default -- no estimation needed |
| 90% of current year | 90% of current year estimated liability | If current year significantly lower |

Taxpayer meets obligation if they pay at least ONE of these amounts.

### 5.2 What constitutes "tax liability"

Preliminary tax = income tax + USC + PRSI (Class S at 4%). PRSI minimum = EUR 500 if income > EUR 5,000.

### 5.3 Computation steps

```
prior_year_liability = income_tax + USC + PRSI
option_A = prior_year_liability x 100%
option_B = estimated_current_year_liability x 90%
preliminary_tax = min(option_A, option_B) (or simply pay option_A for safety)
net_due = preliminary_tax - PAYE_credits - withholding_tax
```

### 5.4 105% of pre-prior-year (direct debit)

For clients on direct debit: 105% of the pre-prior-year liability, spread in equal monthly instalments. This is a third safe harbour.

### 5.5 First year rule

First year of self-assessment: 100% rule is unavailable (no prior year). Must use 90% of estimated current year.

---

## Section 6 -- Penalties and interest

### 6.1 Interest on late/insufficient payment

| Element | Rate |
|---|---|
| Daily rate | 0.0219% per day |
| Approximate annual rate | ~8% per annum |
| Runs from | Due date to actual payment date |

### 6.2 Surcharge for late return filing

| Delay | Surcharge |
|---|---|
| Within 2 months of deadline | 5% of tax due (max EUR 12,695) |
| More than 2 months late | 10% of tax due (max EUR 63,485) |

The surcharge applies to the RETURN, not the payment. Even if payment is on time, a late return triggers the surcharge.

---

## Section 7 -- PRSI Class S

| Parameter | Value |
|---|---|
| Rate | 4% |
| Minimum annual contribution | EUR 500 (even if 4% < EUR 500) |
| Applied to | All self-employment income, no upper limit |
| Exemption | Income below EUR 5,000 |

PRSI is included in the preliminary tax payment and collected through self-assessment.

---

## Section 8 -- Edge cases

**EC1 -- Prior year liability under EUR 200.** De minimis: no preliminary tax. Must still file Form 11.

**EC2 -- Income dropped significantly.** Use 90% rule. Risk: interest if estimate too low.

**EC3 -- First year of self-employment.** No prior year liability. Must estimate and pay 90%.

**EC4 -- ROS vs paper deadline confusion.** Paper: strictly 31 October. ROS: ~14 November (exact date published annually). Extension ONLY for ROS filers who both file AND pay through ROS.

**EC5 -- Capital gain in August.** CGT = gain x 33%. Due 15 December. Separate from 31 Oct preliminary.

**EC6 -- PAYE employee with rental income.** Preliminary tax on rental income (Case V). 100% rule on prior year Case V liability. PAYE credits offset income tax.

**EC7 -- Direct debit (105% rule).** Monthly spread of 105% of pre-prior-year. Flag for reviewer.

**EC8 -- Surcharge on late return.** Payment on time but return 6 weeks late: 5% surcharge applies. Surcharge triggered by return, not payment.

---

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] Safe harbour rule selected (100% prior / 90% current / 105% pre-prior DD)
- [ ] All three components included (income tax + USC + PRSI)
- [ ] PRSI minimum EUR 500 checked if income > EUR 5,000
- [ ] CGT excluded from 31 October payment
- [ ] Correct deadline used (paper 31 Oct vs ROS ~14 Nov)
- [ ] De minimis EUR 200 threshold checked
- [ ] First-year rule applied if no prior year
- [ ] Surcharge risk noted for late filing
- [ ] Interest rate quoted (0.0219%/day)
- [ ] Output labelled as estimated until Irish CA or CTA confirms

---

## Section 10 -- Test suite

### Test 1 -- Standard 100% rule
**Input:** Prior year liability EUR 15,000.
**Expected:** Preliminary = EUR 15,000. Due 31 Oct or ~14 Nov (ROS).

### Test 2 -- 90% rule
**Input:** Prior year EUR 30,000. Estimated current = EUR 10,000.
**Expected:** 90% x EUR 10,000 = EUR 9,000. Interest risk flagged.

### Test 3 -- First year
**Input:** First year. Estimated liability EUR 15,800.
**Expected:** 90% = EUR 14,220.

### Test 4 -- De minimis
**Input:** Prior year liability EUR 120.
**Expected:** No preliminary tax. Must still file Form 11.

### Test 5 -- CGT separate
**Input:** Income preliminary EUR 12,000. CGT EUR 8,250.
**Expected:** EUR 12,000 due 31 Oct. EUR 8,250 due 15 Dec.

### Test 6 -- Surcharge
**Input:** Tax EUR 20,000. Return filed 6 weeks late.
**Expected:** 5% surcharge = EUR 1,000.

### Test 7 -- PAYE + self-employment
**Input:** PAYE salary EUR 50,000. SE income EUR 25,000. Prior year SE component EUR 8,000.
**Expected:** Preliminary = EUR 8,000 (100% of prior year SE portion).

---

## Prohibitions

- NEVER tell a client the 100% rule requires estimating current year -- it does NOT
- NEVER confuse paper deadline (31 Oct) with ROS deadline (~mid-Nov)
- NEVER include CGT in the 31 October payment -- separate dates
- NEVER forget USC and PRSI when computing "tax liability"
- NEVER ignore the surcharge for late filing -- applies even if payment is on time
- NEVER apply the 105% rule without confirming direct debit arrangement
- NEVER tell a first-year self-employed person to use the 100% rule -- must use 90%
- NEVER ignore the EUR 200 de minimis threshold
- NEVER present preliminary tax as final -- balance settled with Form 11

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
