---
name: ca-fed-instalments
description: >
  Canadian federal quarterly instalment requirements for self-employed individuals. Covers the $3,000 net tax owing threshold, three calculation methods (no-calculation, prior-year, current-year), instalment due dates (Mar 15, Jun 15, Sep 15, Dec 15), instalment interest and penalties, and interaction with provincial instalments.
version: 1.0
jurisdiction: CA-FED
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Canada Federal Quarterly Instalments v1.0

## What this file is

**Obligation category:** ET (Estimated Tax)
**Functional role:** Computation
**Status:** Complete

This file provides the detailed computation logic for quarterly income tax instalments payable by self-employed Canadian individuals under ITA s 156.

**Tax year coverage.** This skill targets **tax year 2025** (calendar year January 1 to December 31, 2025).

**The reviewer is the customer of this output.** This skill assumes a credentialed reviewer reviews and signs the return. The skill produces working papers and a brief, not a return.

---

## Section 1 — Scope statement

This skill covers:

- **Forms:** No formal form — payments made to CRA by instalment due dates; may receive instalment reminder (INNS1 or INNS2)
- **Entity types:** Self-employed individuals, sole proprietors, and individuals with significant income not subject to source deductions
- Three instalment calculation methods
- Interest and penalty rules
- Interaction with provincial instalment obligations

This skill does NOT cover:

- Corporate instalment requirements (ITA s 157)
- GST/HST instalments (see `ca-fed-gst-hst.md`)
- Trust instalment requirements
- Non-resident instalment obligations

---

## Section 2 — Filing requirements

### 2.1 Who must pay by instalments

An individual must pay income tax by quarterly instalments if their "net tax owing" exceeds $3,000 in both:
- The current year (2025), AND
- Either of the two preceding years (2024 or 2023).

Source: ITA s 156(1).

**Net tax owing** = total federal and provincial tax payable minus amounts withheld at source (T4 withholdings, Part XIII withholdings, etc.) and refundable credits.

For Quebec residents: the federal threshold is $1,800 (since provincial tax is administered by Revenu Quebec separately). Source: ITA s 156.1(1).

### 2.2 Instalment due dates

| Instalment | Due date | Source |
|------------|----------|--------|
| Q1 | March 15, 2025 | ITA s 156(1)(a) |
| Q2 | June 15, 2025 | ITA s 156(1)(b) |
| Q3 | September 15, 2025 | ITA s 156(1)(c) |
| Q4 | December 15, 2025 | ITA s 156(1)(d) |

If the due date falls on a Saturday, Sunday, or public holiday, the payment is due on the next business day. Source: Interpretation Act s 26.

### 2.3 CRA instalment reminders

The CRA sends instalment reminders (form INNS1 for the no-calculation method, INNS2 for prior-year or current-year methods) in February and August. These are suggestions, not assessments. The taxpayer may choose any of the three calculation methods.

---

## Section 3 — Rates and thresholds

| Item | 2025 Value | Source |
|------|------------|--------|
| Instalment threshold (most provinces) | $3,000 net tax owing | ITA s 156(1) |
| Instalment threshold (Quebec residents, federal portion) | $1,800 net tax owing | ITA s 156.1(1) |
| Instalment interest rate (Q1 2025) | Prescribed rate + 2% (updated quarterly by CRA) | ITA s 161(2), Reg 4301 |
| Instalment penalty threshold | Instalment interest > $1,000 | ITA s 163.1 |
| Instalment penalty rate | 50% of (instalment interest charged minus the greater of $1,000 or 25% of instalment interest that would be charged if no payments were made) | ITA s 163.1 |

---

## Section 4 — Computation rules

### 4.1 Three calculation methods

CRA allows taxpayers to choose any of three methods. The taxpayer should choose whichever results in the lowest instalment payments (to maximize cash flow) while avoiding interest charges.

#### Method 1 — No-calculation method (CRA suggested amounts)

**Step 1.** Use the amounts on the CRA instalment reminder (INNS1):
- Q1 and Q2: each = 1/4 of the net tax owing from two years prior (2023)
- Q3 and Q4: each = (net tax owing from one year prior (2024) minus Q1+Q2 amounts) / 2

This is the CRA's default suggestion and guarantees no instalment interest if followed exactly.

#### Method 2 — Prior-year method

**Step 1.** Calculate total net tax owing from the prior year (2024).

**Step 2.** Each quarterly instalment = prior year net tax owing / 4.

```
Q1 = Q2 = Q3 = Q4 = (2024 net tax owing) / 4
```

This method results in no instalment interest if the prior year is used correctly.

#### Method 3 — Current-year method

**Step 1.** Estimate the current year (2025) net tax owing.

**Step 2.** Each quarterly instalment = estimated 2025 net tax owing / 4.

```
Q1 = Q2 = Q3 = Q4 = (2025 estimated net tax owing) / 4
```

This method may result in instalment interest if the estimate is too low. No interest is charged if payments equal or exceed the amounts calculated under Method 1 or Method 2.

### 4.2 Determining net tax owing

**Step 1.** Calculate total federal tax payable:
- Tax on taxable income (using 2025 federal brackets)
- Add: net federal surtax (if applicable — currently none)
- Add: Additional tax on RRSP over-contributions, OAS clawback, etc.

**Step 2.** Calculate total provincial tax payable (for non-Quebec residents; combined on T1).

**Step 3.** Subtract:
- Tax withheld at source (from T4s, T4As, T4RSPs, etc.)
- Refundable tax credits (GST/HST credit, Canada Workers Benefit, etc.)
- CPP/EI overpayments
- Other credits applied at source

**Step 4.** Net tax owing = Step 1 + Step 2 - Step 3. If > $3,000, instalments are required.

### 4.3 Worked example

| Item | 2023 | 2024 | 2025 (est.) |
|------|------|------|-------------|
| Federal tax | $18,000 | $20,000 | $22,000 |
| Provincial tax | $9,000 | $10,000 | $11,000 |
| Tax withheld at source | ($2,000) | ($2,000) | ($2,000) |
| Net tax owing | $25,000 | $28,000 | $31,000 |

**Method 1 (no-calculation):**
- Q1, Q2: $25,000/4 = $6,250 each
- Q3, Q4: ($28,000 - $12,500) / 2 = $7,750 each
- Total: $28,000

**Method 2 (prior-year):**
- Each quarter: $28,000/4 = $7,000
- Total: $28,000

**Method 3 (current-year):**
- Each quarter: $31,000/4 = $7,750
- Total: $31,000

In this example, Method 1 and Method 2 both total $28,000 and guarantee no interest. Method 3 results in higher payments but matches the expected liability.

---

## Section 5 — Edge cases and special rules

### 5.1 First year of self-employment

If the taxpayer had less than $3,000 net tax owing in both 2023 and 2024 (e.g., because they were employed with full source deductions), no instalments are required in 2025 even if 2025 net tax owing is expected to be substantial. However, a large balance will be due on April 30, 2026.

**Recommendation:** Flag to the reviewer. The client should voluntarily set aside estimated tax or make voluntary instalment payments to avoid a large lump sum.

### 5.2 Deceased taxpayer

If the taxpayer dies during the year, the legal representative must pay any outstanding instalments up to the date of death. Any remaining tax is due on the balance-due date or 6 months after death, whichever is later. Source: ITA s 159.

### 5.3 Farming and fishing income

Individuals whose chief source of income is farming or fishing may pay a single annual instalment by December 31 (instead of four quarterly payments). The instalment equals 2/3 of the estimated net tax for the current year or 2/3 of the prior year's net tax. Source: ITA s 155.

### 5.4 Provincial instalment considerations

- For non-Quebec residents: federal and provincial tax are combined on the T1, so instalments cover both.
- For Quebec residents: federal instalments cover federal tax only (threshold $1,800). Revenu Quebec administers separate provincial instalments (threshold $1,800 of Quebec tax).

### 5.5 Instalment interest calculation

Interest is charged on the difference between the amount that should have been paid (under the method that produces the least interest) and the amount actually paid, for each quarter, from the due date to the earlier of:
- The date the payment is made, or
- April 30 of the following year (balance-due date).

The interest rate is the CRA prescribed rate + 2%, compounded daily. Source: ITA s 161(2), (4.01).

**Offset:** If the taxpayer overpays one quarter, the overpayment can offset underpayments in other quarters (contra interest).

### 5.6 Instalment penalty

A penalty applies if instalment interest exceeds $1,000. The penalty is calculated as:

```
Penalty = 50% x (instalment interest - max($1,000, 25% of interest if no payments made))
```

Source: ITA s 163.1.

### 5.7 Voluntary payments

Taxpayers who are not required to pay instalments may still make voluntary payments. This does not trigger the instalment system, and no penalty applies.

---

## Section 6 — Self-checks

Before delivering output, verify:

- [ ] Net tax owing threshold ($3,000 or $1,800 for Quebec) checked for current and two prior years
- [ ] Correct calculation method identified (no-calculation, prior-year, or current-year)
- [ ] All four quarterly due dates are correct (Mar 15, Jun 15, Sep 15, Dec 15)
- [ ] Net tax owing correctly calculated (total tax minus withholdings minus refundable credits)
- [ ] Farming/fishing exception checked if applicable
- [ ] Provincial instalment treatment correct (combined for non-QC, separate for QC)
- [ ] Instalment interest exposure quantified if underpayment is likely
- [ ] First-year-of-self-employment exception noted if applicable
- [ ] Rates and thresholds match the 2025 tax year
- [ ] Output format matches the base skill spec

---

## Section 7 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
