---
name: us-quarterly-estimated-tax
description: >
  Use this skill whenever asked about US federal quarterly estimated income tax payments for sole proprietors and single-member LLCs. Trigger on phrases like "1040-ES", "estimated tax", "quarterly tax", "safe harbor", "underpayment penalty", "Form 2210", "annualized income", or any question about federal estimated tax requirements. Covers the $1,000 threshold, 100%/110% prior-year safe harbor, 90% current-year method, quarterly due dates, annualized income instalment method, Form 2210 penalty computation, and withholding strategies. MUST be loaded alongside us-tax-workflow-base v0.1+. Federal only.
version: 2.0
jurisdiction: US-FED
tax_year: 2025
category: federal
depends_on:
  - us-tax-workflow-base
---

# US Quarterly Estimated Tax (Form 1040-ES) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | United States (federal) |
| Tax | Quarterly estimated income tax payments |
| Forms | 1040-ES (vouchers), 2210 (underpayment penalty), 2210 Schedule AI (annualized) |
| Primary legislation | IRC Section 6654 |
| Supporting legislation | IRC Sections 6621, 6622, 1401, 1402, 3402 |
| Authority | Internal Revenue Service (IRS) |
| Portal | IRS Direct Pay (irs.gov/payments) / EFTPS |
| Currency | USD only |
| Threshold | Net tax due >= $1,000 after withholding and credits |
| Safe harbours | 90% current year OR 100%/110% prior year |
| Payment schedule | Apr 15, Jun 16*, Sep 15, Jan 15 (*Jun 15 is Sunday in 2025) |
| Entity types | Sole proprietors, single-member LLCs (disregarded) |
| Companion skill | us-tax-workflow-base v0.1+ |
| Contributor | Open Accountants Community |
| Validated by | April 2026 |
| Validation date | April 2026 |

**Quarterly due dates (TY2025):**

| Instalment | Due date | Period |
|---|---|---|
| 1st | April 15, 2025 | Jan 1 -- Mar 31 |
| 2nd | June 16, 2025 | Apr 1 -- May 31 |
| 3rd | September 15, 2025 | Jun 1 -- Aug 31 |
| 4th | January 15, 2026 | Sep 1 -- Dec 31 |

**Safe harbour thresholds:**

| Prior year AGI | Safe harbour percentage |
|---|---|
| AGI <= $150,000 ($75,000 MFS) | 100% of prior year tax |
| AGI > $150,000 ($75,000 MFS) | 110% of prior year tax |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Prior year AGI unknown | Assume > $150K; use 110% |
| Underpayment rate uncertain | Use most recently published rate |
| W-2 withholding + SE income | Compute explicitly; do not assume W-2 covers SE |
| Annualized method considered | Default to equal instalments; flag for reviewer |
| Mid-year income uncertain | Annualize YTD + 10% buffer |
| Prior year return not filed | Use last filed return; flag |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- expected total federal tax (income tax + SE tax + NIIT + Additional Medicare Tax), prior year total tax and AGI, expected withholding from all sources.

**Recommended** -- prior year 1040 or transcript, current year Schedule C net profit estimate, W-2 withholding from spouse if MFJ.

**Ideal** -- complete prior year return, current year quarterly P&L, upstream skill outputs (Schedule C, SE tax, QBI).

**Refusal policy if minimum is missing -- SOFT WARN.** Without prior year data, safe harbour cannot be computed.

### Refusal catalogue

**R-US-ET-1 -- Corporate estimated tax (1120-W).** Trigger: corporation. Message: "Corporate estimated tax is outside this skill."

**R-US-ET-2 -- Trust/estate estimated tax (1041-ES).** Trigger: trust or estate. Message: "Trust/estate estimated tax is outside this skill."

**R-US-ET-3 -- State estimated tax.** Trigger: client asks about state payments. Message: "State estimated tax rules differ materially. Use the state-specific skill."

**R-US-ET-4 -- Nonresident alien (1040-ES NR).** Trigger: nonresident alien. Message: "Nonresident alien estimated tax is outside this skill."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as a federal estimated tax payment.

### 3.1 IRS estimated tax debits

| Pattern | Treatment | Notes |
|---|---|---|
| IRS, INTERNAL REVENUE SERVICE | Federal estimated payment | Match with Apr/Jun/Sep/Jan timing |
| EFTPS, ELECTRONIC FED TAX | Federal estimated payment | EFTPS payment |
| IRS DIRECT PAY | Federal estimated payment | IRS online payment |
| 1040-ES, 1040ES | Federal estimated payment | Explicit form reference |
| ESTIMATED TAX PAYMENT, EST TAX | Federal estimated payment | Explicit description |
| US TREASURY, TREASURY 310 | Federal estimated payment | Government payee |

### 3.2 Timing-based identification

| Debit date range | Likely instalment | Confidence |
|---|---|---|
| 10 April -- 20 April | 1st instalment (Apr 15) | High if IRS payee |
| 10 June -- 20 June | 2nd instalment (Jun 15/16) | High |
| 10 September -- 20 September | 3rd instalment (Sep 15) | High |
| 10 January -- 20 January | 4th instalment (Jan 15) | High |

### 3.3 Related but NOT federal estimated tax

| Pattern | Treatment | Notes |
|---|---|---|
| STATE TAX, NYS, CA FTB, IL DOR | EXCLUDE | State estimated tax |
| FICA, SOCIAL SECURITY | EXCLUDE | Employment tax (if separate) |
| IRS PENALTY, IRS INTEREST | EXCLUDE | Penalty/interest |
| IRS REFUND, TAX REFUND | Flag for reviewer | Refund |
| 1040 BALANCE, TAX DUE | Flag for reviewer | Annual return balance payment |

### 3.4 Withholding vs estimated payments

W-2 withholding appears as employer deductions on pay stubs, not as separate bank debits. Do not confuse employer withholding with estimated tax payments.

---

## Section 4 -- Worked examples

### Example 1 -- Basic prior-year safe harbour

**Input:** Single. TY2024 AGI = $95,000. TY2024 tax = $18,000. Expected TY2025 tax = $22,000. No withholding.

| Method | Amount |
|---|---|
| Prior year (100%) | $18,000 |
| Current year (90%) | $19,800 |
| Required (lesser) | $18,000 |
| Quarterly | $4,500 |

### Example 2 -- High-income 110% rule

**Input:** MFJ. TY2024 AGI = $210,000. TY2024 tax = $42,000. Expected TY2025 tax = $55,000.

| Method | Amount |
|---|---|
| Prior year (110%) | $46,200 |
| Current year (90%) | $49,500 |
| Required (lesser) | $46,200 |
| Quarterly | $11,550 |

### Example 3 -- Withholding eliminates requirement

**Input:** MFJ. Spouse W-2 withholding = $25,000. TY2024 tax = $20,000. AGI = $120,000.

**Output:** Withholding ($25,000) > 100% prior year ($20,000). No estimated payments required.

### Example 4 -- Under $1,000 threshold

**Input:** Expected TY2025 tax = $5,200. Part-time W-2 withholding = $4,500. Net = $700.

**Output:** Net tax due $700 < $1,000. No estimated payments required.

### Example 5 -- Bank statement classification

**Input line:** `04/15/2025 ; IRS DIRECT PAY EST TAX ; DEBIT ; -4,500.00 ; USD`

**Classification:** Federal estimated tax payment, 1st instalment TY2025. Tax payment -- not deductible on Schedule C.

---

## Section 5 -- Computation rules

### 5.1 The $1,000 threshold test

```
expected_tax = income_tax + SE_tax + Additional_Medicare + NIIT
net_tax_due = expected_tax - withholding - refundable_credits
if net_tax_due < 1,000: no estimated payments required
```

### 5.2 Required annual payment

Required = lesser of:
- **Method A (current year):** 90% of TY2025 tax
- **Method B (prior year):** 100% of TY2024 tax (110% if AGI > $150K / $75K MFS)

### 5.3 Prior year safe harbour requirements

- Prior year must be 12-month tax year
- Prior year return must be filed
- If prior year tax was zero: required annual payment under Method B = $0

### 5.4 Quarterly instalments

Each instalment = required annual payment / 4 (25% each).

### 5.5 Annualized income instalment method (Form 2210 Schedule AI)

| Period | Months | Annualization factor |
|---|---|---|
| Period 1 | Jan-Mar | 4 |
| Period 2 | Jan-May | 2.4 |
| Period 3 | Jan-Aug | 1.5 |
| Period 4 | Jan-Dec | 1 |

Required instalment = 25% of annualized tax, minus prior payments. Must be elected for all four quarters.

### 5.6 Withholding strategy (MFJ)

Increase W-2 spouse's withholding via Form W-4 Step 4(c). Withholding is treated as paid ratably throughout the year even if changed mid-year.

### 5.7 January 31 filing exception

If return filed and all tax paid by January 31, 2026: 4th instalment not required.

---

## Section 6 -- Penalties and interest

### 6.1 Underpayment penalty (Form 2210)

The "penalty" is interest on the underpayment. Rate = federal short-term rate + 3 percentage points, compounded daily.

### 6.2 Published rates (TY2025)

| Quarter | Rate |
|---|---|
| Q1 2025 | 7% |
| Q2 2025 | 7% |
| Q3 2025 | 7% |
| Q4 2025 | 7% |
| Q1 2026 | 7% |

(Verify against IRS Revenue Rulings.)

### 6.3 Per-quarter computation

```
for each quarter:
    required = 25% of required annual payment
    paid = estimated payments + allocable withholding
    underpayment = max(0, required - paid)
    period = instalment_due_date to earlier(payment_date, Apr 15 next year)
    penalty = underpayment x daily_rate x days_in_period
```

### 6.4 Waiver provisions

IRS may waive under IRC 6654(e)(3) for: casualty/disaster/unusual circumstances, retirement after age 62, or disability.

---

## Section 7 -- Special situations

### 7.1 Withholding strategy for married couples

Self-employed spouse + W-2 spouse: increase W-4 extra withholding to cover both. Withholding treated as ratable even if changed mid-year -- advantage over quarterly estimates.

### 7.2 First year of self-employment

If prior year tax was zero: required annual payment under prior-year method = $0. No estimated payments required under that method.

### 7.3 Mid-year income changes

Annualized method (Section 5.5) adjusts for uneven income. Alternatively, adjust future estimates up or down.

### 7.4 Farmer/fisherman exception

2/3 of income from farming/fishing: single instalment by January 15, or file by March 1 and pay in full.

---

## Section 8 -- Edge cases

**EC1 -- Prior year short tax year.** Prior year < 12 months: prior-year safe harbour unavailable. Only 90% current year.

**EC2 -- Prior year zero tax but high AGI.** Zero tax = $0 required annual payment under Method B. The zero-tax rule dominates.

**EC3 -- Taxpayer dies mid-year.** Estimated payments required only through quarter of death.

**EC4 -- Large Q4 income.** Prior-year safe harbour typically best. Annualized method shows low Q1-Q3 and large Q4.

**EC5 -- W-2 to self-employment mid-year.** W-2 withholding treated as ratable. Annualized method reduces Q1/Q2 required amounts.

**EC6 -- Overpayment.** Applied to next year or refunded (Form 1040 line 36).

**EC7 -- Unequal payments.** Penalties computed per-quarter. Q1 shortfall not cured by Q2 overpayment.

**EC8 -- Disaster area relief.** IRS may postpone due dates. Verify announcements.

**EC9 -- Farmer/fisherman.** Single January 15 payment or file by March 1.

**EC10 -- NIIT creates unexpected requirement.** Investment income above NIIT threshold ($200K single / $250K MFJ) adds 3.8% to total tax.

---

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] $1,000 threshold test applied
- [ ] Both safe harbour methods computed (prior year and current year)
- [ ] Correct prior-year percentage used (100% vs 110% based on AGI)
- [ ] All four quarterly due dates correct
- [ ] Withholding from all sources included
- [ ] SE tax + income tax + NIIT + Additional Medicare included in total tax
- [ ] Annualized method flagged if income is uneven
- [ ] First-year zero-prior-tax rule checked
- [ ] State estimated tax deferred to state skill
- [ ] Output labelled as estimated until reviewer confirms

---

## Section 10 -- Test suite

### Test 1 -- Basic prior-year safe harbour
**Input:** Single. TY2024 AGI $95K, tax $18K. TY2025 expected $22K. No withholding.
**Expected:** Required = $18,000 (100% prior). Quarterly = $4,500.

### Test 2 -- High-income 110%
**Input:** MFJ. TY2024 AGI $210K, tax $42K. TY2025 expected $55K.
**Expected:** Required = $46,200 (110% prior). Quarterly = $11,550.

### Test 3 -- Withholding covers safe harbour
**Input:** MFJ. Spouse withholding $25K. TY2024 tax $20K. AGI $120K.
**Expected:** No estimated payments required.

### Test 4 -- Below $1,000
**Input:** Expected tax $5,200. W-2 withholding $4,500.
**Expected:** Net $700 < $1,000. No payments required.

### Test 5 -- Underpayment penalty
**Input:** Required $5,000/quarter. Q1 paid $3,000. Q2-Q4 paid $5,000. Rate 7%.
**Expected:** Q1 underpayment $2,000. Penalty approx. $140 (full year).

### Test 6 -- First year, zero prior tax
**Input:** First year. No prior return.
**Expected:** Prior year method = $0. No payments required under that method.

### Test 7 -- Farmer exception
**Input:** 2/3+ farming income. Expected tax $25,000.
**Expected:** Single payment Jan 15 or file by Mar 1.

---

## Prohibitions

- NEVER file estimated payments or generate payment instructions -- compute amounts only
- NEVER recommend intentional underpayment as a strategy
- NEVER compute state estimated tax -- defer to state skills
- NEVER override reviewer's method selection
- NEVER guarantee a safe harbour eliminates all penalties mid-year
- NEVER advise on entities other than sole proprietors / disregarded SMLLCs
- NEVER apply penalty waiver without reviewer approval
- NEVER present amounts as definitive -- label as estimated

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
