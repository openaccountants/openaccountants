---
name: nz-provisional-tax
description: Use this skill whenever asked about New Zealand provisional tax for self-employed individuals. Trigger on phrases like "provisional tax", "RIT", "residual income tax", "standard uplift", "estimation method", "AIM", "use of money interest", "UOMI", "provisional tax instalment", or any question about provisional tax obligations for sole traders in New Zealand. Covers the $5,000 RIT threshold, standard uplift (105%), estimation method, AIM method, instalment dates, and UOMI. ALWAYS read this skill before touching any NZ provisional tax work.
---

# NZ Provisional Tax -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | New Zealand |
| Jurisdiction Code | NZ |
| Primary Legislation | Income Tax Act 2007 (ITA 2007), Part RC |
| Supporting Legislation | Tax Administration Act 1994 (TAA 1994) |
| Tax Authority | Inland Revenue (IR / Te Tari Taake) |
| Filing Portal | myIR (myir.ird.govt.nz) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a New Zealand chartered accountant (CA) |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year | 2025 (1 April 2025 -- 31 March 2026) |
| Confidence Coverage | Tier 1: RIT threshold, standard uplift calculation, instalment dates. Tier 2: estimation method risk, AIM setup. Tier 3: pooling arrangements, complex multi-entity structures. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified professional must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any provisional tax figure, you MUST know:

1. **Residual income tax (RIT) from the prior year** [T1] -- determines whether provisional tax is required
2. **Whether this is the first year of self-employment** [T1] -- first-year taxpayers may be exempt
3. **Chosen method** [T1] -- standard uplift, estimation, or AIM
4. **Balance date** [T1] -- most sole traders use 31 March; non-standard balance dates change instalment dates
5. **Whether using a tax agent with an extension of time (EOT)** [T1] -- affects instalment count and dates
6. **GST registration status** [T1] -- affects payment frequency options and AIM eligibility

**If prior-year RIT is $5,000 or less, STOP. No provisional tax is required.**

---

## Step 1: RIT Threshold [T1]

**Legislation:** ITA 2007, s RC 3

| Rule | Detail |
|------|--------|
| Provisional tax required | When RIT for the prior year exceeds **$5,000** |
| RIT definition | Total income tax minus PAYE and other withholding credits |
| First-year exemption | No provisional tax in the first year of earning income that gives rise to RIT |

### RIT Calculation [T1]

RIT = Income tax assessed - Tax credits (PAYE, RWT, etc.)

If RIT <= $5,000: no provisional tax obligation. Client pays terminal tax only.

---

## Step 2: Standard Uplift Method [T1]

**Legislation:** ITA 2007, s RC 5(2)-(3)

### Calculation [T1]

| Step | Action |
|------|--------|
| 2.1 | Take prior year's RIT |
| 2.2 | Multiply by 105% (the standard uplift) |
| 2.3 | Divide by the number of instalments |

### Instalment Schedule -- Standard Balance Date (31 March) [T1]

| Instalment | Due Date | Amount |
|-----------|----------|--------|
| 1st | 28 August | 1/3 of (prior year RIT x 105%) |
| 2nd | 15 January | 1/3 of (prior year RIT x 105%) |
| 3rd | 7 May | 1/3 of (prior year RIT x 105%) |

**Note:** The 3rd instalment (7 May) falls AFTER the end of the tax year. This is by design.

### With Tax Agent EOT [T1]

If the client uses a tax agent with extension of time, the instalment dates and number may vary. Common pattern:

| Instalment | Due Date |
|-----------|----------|
| 1st | 28 October |
| 2nd | 7 May |

(Two instalments of 50% each of prior year RIT x 105%.)

---

## Step 3: Estimation Method [T2]

**Legislation:** ITA 2007, s RC 6

| Rule | Detail |
|------|--------|
| Who can use | Any provisional taxpayer |
| How it works | Client estimates current year's RIT and pays in instalments |
| Risk | If estimate is too low, UOMI applies from original due dates on the shortfall |
| Advantage | Useful when income is expected to drop significantly |

### Rules [T2]

- No penalty for underestimation, but UOMI is charged on the difference between estimated and actual RIT
- Client can re-estimate at any instalment date
- [T2] Flag for reviewer: estimation method carries interest risk. Only recommend if income is clearly declining.

---

## Step 4: AIM Method (Accounting Income Method) [T2]

**Legislation:** ITA 2007, s RC 7B

| Rule | Detail |
|------|--------|
| Eligibility | Gross income < $5,000,000; must use AIM-capable accounting software |
| How it works | Tax calculated each period based on actual accounting income |
| Frequency | Aligned with GST return periods (monthly, 2-monthly, or 6-monthly) |
| Advantage | No UOMI exposure; pay as you earn |
| Software | Xero, MYOB, and other approved software |

[T2] Flag for reviewer: AIM requires compatible software and correct configuration. Confirm software is AIM-enabled.

---

## Step 5: Use of Money Interest (UOMI) [T1]

**Legislation:** TAA 1994, s 120A-120Q

| Rate Type | Rate (verify annually) |
|-----------|----------------------|
| Underpayment rate | ~10.91% (2025 -- verify with IR) |
| Overpayment rate | ~3.41% (2025 -- verify with IR) |

### When UOMI Applies [T1]

| Method | UOMI Exposure |
|--------|---------------|
| Standard uplift | No UOMI if each instalment paid on time and in full (even if actual RIT is higher) |
| Estimation | UOMI from each instalment date if estimate < actual RIT |
| AIM | No UOMI if each AIM payment is correct and on time |

### Safe Harbour -- Standard Uplift [T1]

If the taxpayer uses the standard uplift method and pays each instalment on time, NO UOMI is charged even if the actual tax liability turns out to be much higher. This is a key advantage of the standard method.

---

## Step 6: Terminal Tax [T1]

**Legislation:** ITA 2007, s RC 14

| Item | Detail |
|------|--------|
| Terminal tax | The balance of income tax after provisional tax payments are credited |
| Due date | 7 February of the following year (for 31 March balance date, without EOT) |
| With EOT | 7 April of the following year |

Terminal tax = Actual RIT - Provisional tax paid

If provisional tax exceeds actual RIT, the overpayment is refunded or credited.

---

## Step 7: Penalties [T1]

**Legislation:** TAA 1994, Part 9

| Offence | Penalty |
|---------|---------|
| Late payment of provisional tax | Initial late payment penalty: 1% + 4% if still unpaid after 7 days |
| UOMI on underpayment | Underpayment interest rate (compounding daily) |
| Late filing of IR3 | $250 late filing penalty (may increase) |
| Shortfall penalties | If estimation method used with intent to understate: shortfall penalties (20-150%) |

---

## Step 8: Edge Case Registry

### EC1 -- First year of self-employment [T1]
**Situation:** Client starts freelancing in July 2025. No prior-year RIT.
**Resolution:** No provisional tax obligation in the first year. Client pays terminal tax in full by 7 February 2027 (or EOT date). May voluntarily pay provisional tax to avoid a large terminal tax bill.

### EC2 -- Income drops significantly [T2]
**Situation:** Prior-year RIT was $30,000 but client expects only $10,000 this year.
**Resolution:** Standard uplift would require $31,500 (105% x $30,000) in payments. Client may use estimation method to pay based on $10,000 expected RIT. [T2] Flag: if actual RIT exceeds estimate, UOMI applies. Recommend estimation only if decline is certain.

### EC3 -- Mixed PAYE and self-employment income [T1]
**Situation:** Client earns $60,000 PAYE salary and $20,000 freelance income. RIT = $6,000.
**Resolution:** RIT exceeds $5,000 threshold. Provisional tax required on the $6,000 RIT (not on total income). Standard uplift: $6,000 x 105% = $6,300 / 3 = $2,100 per instalment.

### EC4 -- Non-standard balance date [T1]
**Situation:** Client has a 30 September balance date.
**Resolution:** Instalment dates shift. For 30 September balance date: instalments fall on 28 February, 15 July, and 7 November. Verify exact dates in IR's provisional tax calendar.

### EC5 -- Prior year RIT exactly $5,000 [T1]
**Situation:** Client's prior-year RIT is exactly $5,000.
**Resolution:** Provisional tax is required when RIT EXCEEDS $5,000 (i.e., > $5,000). Exactly $5,000 means NO provisional tax obligation.

### EC6 -- Voluntary provisional tax payments [T1]
**Situation:** First-year freelancer wants to make voluntary payments to avoid a large terminal tax bill.
**Resolution:** Permitted. Voluntary payments reduce terminal tax. UOMI overpayment interest may apply to early voluntary payments. No penalties for not paying voluntary provisional tax.

---

## Step 9: Test Suite

### Test 1 -- Standard uplift, mid-range income
**Input:** Prior-year RIT = $15,000. Standard uplift method. 31 March balance date.
**Expected output:**
- Provisional tax = $15,000 x 105% = $15,750
- Instalment 1 (28 Aug): $5,250
- Instalment 2 (15 Jan): $5,250
- Instalment 3 (7 May): $5,250

### Test 2 -- Below threshold
**Input:** Prior-year RIT = $4,800.
**Expected output:** No provisional tax required. RIT does not exceed $5,000.

### Test 3 -- Estimation method
**Input:** Prior-year RIT = $25,000. Estimated current-year RIT = $12,000.
**Expected output:**
- Provisional tax = $12,000 (estimated)
- Instalment 1: $4,000
- Instalment 2: $4,000
- Instalment 3: $4,000
- Warning: if actual RIT > $12,000, UOMI applies from instalment dates.

### Test 4 -- High earner, tax agent EOT
**Input:** Prior-year RIT = $50,000. Tax agent with EOT. Two instalments.
**Expected output:**
- Provisional tax = $50,000 x 105% = $52,500
- Instalment 1 (28 Oct): $26,250
- Instalment 2 (7 May): $26,250

### Test 5 -- First year, no prior RIT
**Input:** New freelancer, no prior-year income tax.
**Expected output:** No provisional tax required in first year. Terminal tax payable by 7 February following year-end.

---

## PROHIBITIONS

- NEVER require provisional tax when prior-year RIT is $5,000 or less
- NEVER apply UOMI to standard uplift payments made on time and in full
- NEVER recommend estimation method without flagging UOMI risk
- NEVER use an uplift factor other than 105% for the standard method
- NEVER confuse RIT with total income tax -- RIT is after deducting PAYE and other credits
- NEVER apply provisional tax in the first year of earning self-employment income (unless voluntary)
- NEVER ignore the 3rd instalment date falling after year-end -- this is correct by design
- NEVER present calculations as definitive -- always label as estimated and direct client to IR or a qualified NZ chartered accountant

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a New Zealand Chartered Accountant or equivalent licensed practitioner) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
