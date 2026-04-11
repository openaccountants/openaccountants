---
name: us-quarterly-estimated-tax
description: Tier 2 content skill for computing quarterly estimated federal income tax payments for US sole proprietors and single-member LLCs disregarded for federal tax. Covers tax year 2025 Form 1040-ES requirements including the 100%/110% prior-year safe harbor under IRC §6654(d)(1)(B)/(C), the 90% current-year alternative under §6654(d)(1)(A), the annualized income installment method under §6654(d)(2) and Form 2210 Schedule AI, the underpayment penalty computation under §6654 and Form 2210, the quarterly due dates under §6654(c), the interaction between withholding and estimated payments under §6654(b), and the waiver provisions under §6654(e). Consumes net profit from us-schedule-c-and-se-computation and tax positions from us-form-1040-self-employed-positions. Defers state estimated tax to state-specific skills. MUST be loaded alongside us-tax-workflow-base v0.1+. Federal only.
version: 0.2
---

# US Quarterly Estimated Tax Skill v0.2

## What this file is, and what it is not

**This file is a content skill that loads on top of `us-tax-workflow-base` v0.1.** It provides the rules for computing quarterly estimated federal income tax payments using Form 1040-ES for tax year 2025. It does not provide workflow architecture — that comes from the base. It does not classify transactions, compute Schedule C net profit, or compute QBI — those are upstream content skills.

**Where this skill fits in the pipeline:**

```
us-sole-prop-bookkeeping (classifies transactions)
        |
us-schedule-c-and-se-computation (net profit, SE tax)
        |
us-form-1040-self-employed-positions (QBI, retirement, SE health insurance)
        |
us-quarterly-estimated-tax (THIS SKILL — estimated payments for current/following year)
```

This skill is the final step in the federal pipeline. It takes the total federal tax liability (income tax + SE tax - credits - above-the-line deductions) and determines what quarterly estimated payments are required, whether the safe harbor is met, and whether an underpayment penalty applies.

**Tax year coverage.** This skill is current for **tax year 2025** as of its currency date (April 2026). It reflects the One Big Beautiful Bill Act (Public Law 119-21, signed July 4, 2025) and post-OBBBA guidance available as of the currency date.

**The reviewer is the customer of this output.** Per the base, this skill assumes a credentialed reviewer (Enrolled Agent, CPA, or attorney under Circular 230) reviews and signs the return. The skill produces working papers and a brief, not a return.

---

## Section 1 — Scope statement

This skill covers federal estimated tax payments for tax year 2025 for taxpayers who are:

- US sole proprietors filing Schedule C, OR
- Single-member LLCs treated as disregarded entities for federal income tax purposes

For the following kinds of work:

- Determining whether estimated tax payments are required under IRC §6654
- Computing the required annual payment using the prior-year safe harbor or current-year method
- Allocating the required annual payment across the four quarterly installments
- Applying the annualized income installment method (Form 2210 Schedule AI) for taxpayers with uneven income
- Computing the underpayment penalty on Form 2210 when payments fall short
- Determining whether withholding from other sources (W-2, 1099-R, etc.) eliminates or reduces the estimated tax obligation
- Producing quarterly payment vouchers (Form 1040-ES) with correct amounts and due dates
- Evaluating whether a penalty waiver applies under §6654(e)

This skill does NOT cover:

- Computation of the underlying tax liability — handled by upstream skills
- State estimated tax payments — handled by state-specific skills (e.g., `ca-estimated-tax-540es`)
- Corporate estimated tax (Form 1120-W) — out of scope
- Trust/estate estimated tax (Form 1041-ES) — out of scope
- Estimated tax for nonresident aliens (Form 1040-ES NR) — out of scope

---

## Section 2 — Year coverage and currency

**Tax year covered:** 2025 (returns due April 15, 2026, or October 15, 2026 with extension; estimated tax payments for TY2025 due April 15, June 16, September 15, 2025, and January 15, 2026).

**Currency date:** April 2026.

**Legislation reflected:**
- Internal Revenue Code as in force for tax year 2025
- One Big Beautiful Bill Act (OBBBA), Public Law 119-21, signed July 4, 2025
- Tax Cuts and Jobs Act of 2017 provisions still in force in 2025
- IRS Form 1040-ES Instructions for tax year 2025
- IRS Form 2210 and Instructions for tax year 2025
- Rev. Proc. 2024-40 (2025 inflation adjustments, where not superseded by OBBBA)

**Currency limitations:**
- The IRS underpayment interest rate is set quarterly by the IRS based on the federal short-term rate plus 3 percentage points (IRC §6621(a)(2)). The rates used in this skill reflect published rates through Q1 2026. Rates for subsequent quarters should be verified against IRS announcements.

---

## Section 3 — Year-specific figures table for tax year 2025

All dollar thresholds, rates, percentages, and indexed figures the skill relies on, in one place.

### Estimated tax thresholds and safe harbors

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| Minimum tax liability to trigger estimated tax requirement | $1,000 | IRC §6654(e)(1) |
| Prior-year safe harbor (AGI ≤ $150K; ≤ $75K MFS) | 100% of prior year tax | IRC §6654(d)(1)(B) |
| Prior-year safe harbor (AGI > $150K; > $75K MFS) | 110% of prior year tax | IRC §6654(d)(1)(C) |
| Current-year safe harbor | 90% of current year tax | IRC §6654(d)(1)(A) |
| Required annual payment | Lesser of current-year 90% or applicable prior-year percentage | IRC §6654(d)(1) |

### Quarterly due dates for TY2025 estimated payments

| Installment | Due date | Income period covered |
|---|---|---|
| 1st installment | April 15, 2025 | Jan 1 - Mar 31, 2025 |
| 2nd installment | June 16, 2025 * | Apr 1 - May 31, 2025 |
| 3rd installment | September 15, 2025 | Jun 1 - Aug 31, 2025 |
| 4th installment | January 15, 2026 | Sep 1 - Dec 31, 2025 |

\* June 15 falls on a Sunday in 2025; the due date shifts to the next business day, June 16.

**Note:** If the return is filed and all tax is paid by January 31, 2026, the 4th installment is not required. IRC §6654(h)(2).

### Underpayment penalty rates (IRS interest rates for individual underpayments)

| Quarter | Rate | Primary source |
|---|---|---|
| Q1 2025 (Jan-Mar) | 7% | Rev. Rul. 2024-23 |
| Q2 2025 (Apr-Jun) | 7% | Rev. Rul. 2025-2 |
| Q3 2025 (Jul-Sep) | 7% | Rev. Rul. 2025-10 |
| Q4 2025 (Oct-Dec) | 7% | Rev. Rul. 2025-18 |
| Q1 2026 (Jan-Mar) | 7% | Rev. Rul. 2025-25 |

**Note:** The underpayment penalty rate under §6654 equals the federal short-term rate (AFR) plus 3 percentage points, compounded daily. The rates above are illustrative based on published rates through early 2026. The reviewer must verify the applicable rate for each quarter from the IRS's published Revenue Rulings, as the rate changes quarterly.

### Related figures from upstream skills (for context)

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| Social Security wage base | $176,100 | SSA annual announcement |
| SE tax rate (OASDI + Medicare) | 15.3% (12.4% + 2.9%) | IRC §1401(a), (b) |
| Additional Medicare Tax threshold (single) | $200,000 | IRC §3101(b)(2)(C) |
| Additional Medicare Tax rate | 0.9% | IRC §3101(b)(2) / §1401(b)(2) |
| Net Investment Income Tax rate | 3.8% | IRC §1411(a)(1) |
| NIIT threshold (single) | $200,000 | IRC §1411(b) |
| NIIT threshold (MFJ) | $250,000 | IRC §1411(b) |

---

## Section 4 — Primary source library

### Statute (Internal Revenue Code, Title 26 USC)

- **IRC §6654** — Failure by individual to pay estimated income tax (the master section)
- **IRC §6654(a)** — Addition to the tax (the penalty is technically an "addition to tax," not a penalty)
- **IRC §6654(b)** — Amount of underpayment; role of withholding
- **IRC §6654(c)** — Required installment amounts (25% of required annual payment each quarter)
- **IRC §6654(d)(1)** — Required annual payment: lesser of 90% current year or 100%/110% prior year
- **IRC §6654(d)(1)(C)** — 110% prior-year threshold for high-income taxpayers (AGI > $150K)
- **IRC §6654(d)(2)** — Annualized income installment method
- **IRC §6654(e)(1)** — Exception: no penalty if tax liability < $1,000 after credits and withholding
- **IRC §6654(e)(2)** — Exception: no penalty if withholding covers 100% of prior-year tax
- **IRC §6654(e)(3)** — Waiver for casualty, disaster, or other unusual circumstances; waiver for newly retired or disabled taxpayers
- **IRC §6654(h)** — Special rule: filing by January 31 eliminates 4th installment requirement
- **IRC §6654(l)** — Application to self-employment tax
- **IRC §6621(a)(2)** — Underpayment rate (federal short-term rate + 3 percentage points)
- **IRC §6622** — Interest compounded daily
- **IRC §1401** — Self-employment tax rates
- **IRC §1402** — Net earnings from self-employment
- **IRC §3402** — Income tax collected at source (withholding)

### IRS Forms and Instructions

- **Form 1040-ES (2025)** — Estimated Tax for Individuals, including the Estimated Tax Worksheet
- **Form 2210 (2025)** — Underpayment of Estimated Tax by Individuals, Estates, and Trusts
- **Form 2210, Schedule AI (2025)** — Annualized Income Installment Method
- **Form 1040-ES Instructions (2025)** — Step-by-step estimated tax worksheet
- **Form 2210 Instructions (2025)** — Penalty computation, waiver rules

### IRS Publications

- **Pub 505 (2025)** — Tax Withholding and Estimated Tax

### Revenue Rulings (underpayment interest rates)

- **Rev. Rul. 2024-23** — Q1 2025 interest rate
- Subsequent quarterly Revenue Rulings setting §6621 rates through the filing period

---

## Section 5 — Determining whether estimated tax is required

### The $1,000 threshold test

Under IRC §6654(e)(1), no estimated tax penalty applies if the taxpayer expects to owe less than **$1,000** in tax after subtracting withholding and refundable credits. This is the first gate.

**Computation:**

```
Expected total tax (income tax + SE tax + Additional Medicare Tax + NIIT)
  MINUS  Tax withholding (W-2, 1099, voluntary withholding on SS benefits, etc.)
  MINUS  Refundable credits (Earned Income Credit, Child Tax Credit refundable portion, etc.)
  = Net tax due

IF net tax due < $1,000 → No estimated payments required.
```

### The withholding safe harbor

Under IRC §6654(e)(2), no estimated tax penalty applies if withholding from all sources (not just wages) equals or exceeds 100% of the prior year's total tax liability (110% if AGI > $150K, or > $75K if MFS).

**Key point for sole proprietors:** Most sole proprietors have minimal or no withholding, making this safe harbor inapplicable. However, taxpayers with a spouse who has W-2 income can increase withholding on the spouse's W-2 (via Form W-4) to cover the self-employment tax liability. This is a legitimate and common strategy.

### When estimated payments ARE required

Estimated tax payments are required when ALL of the following are true:

1. The taxpayer expects to owe $1,000 or more after withholding and credits
2. The taxpayer's withholding does not meet the prior-year safe harbor (100% or 110%)
3. The taxpayer is not otherwise exempt (e.g., prior year was a full 12-month year with zero tax liability — IRC §6654(e)(2) second sentence)

---

## Section 6 — Computing the required annual payment

### Two methods — taxpayer uses the LESSER amount

Under IRC §6654(d)(1), the required annual payment is the **lesser of:**

**Method A — Current-year method:**
90% of the tax shown on the current year return (TY2025)

**Method B — Prior-year method:**
100% of the tax shown on the prior year return (TY2024) — OR 110% if the prior year AGI exceeded $150,000 ($75,000 if MFS)

### Prior-year safe harbor rules in detail

| Prior year AGI | Safe harbor percentage | IRC cite |
|---|---|---|
| AGI ≤ $150,000 (≤ $75,000 MFS) | 100% of prior year tax | §6654(d)(1)(B) |
| AGI > $150,000 (> $75,000 MFS) | 110% of prior year tax | §6654(d)(1)(C) |

**Requirements for using the prior-year safe harbor:**
- The prior year must have been a 12-month tax year
- The taxpayer must have filed a return for the prior year (or a return was filed for them)
- The prior year return must show a tax liability (if prior year tax was zero, the required annual payment under Method B is zero — meaning no estimated payments are required under this method)

### The prior-year-tax-was-zero rule

If the taxpayer filed a prior-year return showing zero tax liability and the prior year was a full 12-month year, no estimated tax penalty can apply for the current year under the prior-year safe harbor, regardless of how much tax is owed in the current year. IRC §6654(e)(2). This is a powerful planning tool for a taxpayer's first profitable year.

### Required annual payment worksheet

```
Line 1.  Current year expected tax (income tax + SE tax + AMT + NIIT + Additional Medicare Tax)
Line 2.  Current year credits (nonrefundable)
Line 3.  Line 1 minus Line 2
Line 4.  Current year other taxes (if any)
Line 5.  Line 3 plus Line 4 = Total current year expected tax
Line 6.  Current year withholding (all sources)
Line 7.  Line 5 minus Line 6 = Net expected tax due
         IF Line 7 < $1,000 → STOP. No estimated payments required.
Line 8.  90% of Line 5 (current year method)
Line 9.  Prior year tax from TY2024 return
Line 10. Prior year AGI from TY2024 return
         IF Line 10 > $150,000 ($75,000 MFS): Line 11 = Line 9 x 110%
         ELSE: Line 11 = Line 9 x 100%
Line 12. Required annual payment = LESSER of Line 8 or Line 11
Line 13. Line 12 minus Line 6 (withholding) = Net estimated payments required
Line 14. Each quarterly payment = Line 13 / 4
```

---

## Section 7 — Quarterly installment allocation

### Standard method: equal installments

Under §6654(c), the required installment for each quarter is **25%** of the required annual payment. The four payments are due on the dates listed in Section 3.

### Annualized income installment method (Form 2210 Schedule AI)

For taxpayers whose income is not earned evenly throughout the year (common for freelancers with seasonal work, large one-time payments, or ramp-up periods), the annualized income installment method under IRC §6654(d)(2) may reduce or eliminate underpayment penalties for earlier quarters.

**How it works:**

The method annualizes the taxpayer's income for each cumulative period:

| Period | Months | Annualization factor |
|---|---|---|
| Period 1 | Jan 1 - Mar 31 | 4 |
| Period 2 | Jan 1 - May 31 | 2.4 |
| Period 3 | Jan 1 - Aug 31 | 1.5 |
| Period 4 | Jan 1 - Dec 31 | 1 |

**For each period:**
1. Compute actual income (Schedule C net profit + other income) for the cumulative months
2. Multiply by the annualization factor to get annualized income
3. Compute annualized tax on that income
4. The required installment is 25% of annualized tax (cumulative), minus payments already made

**When to use it:**
- Freelancer earns most income in Q3/Q4 and would face penalties under the standard method for Q1/Q2 underpayment
- Taxpayer received a large one-time payment that skews annual income
- New business started mid-year

**Important:** The annualized method is elected on Form 2210 and requires completing Schedule AI. The taxpayer must use the method for all four quarters — they cannot use it selectively for only the quarters where it helps.

---

## Section 8 — Underpayment penalty computation (Form 2210)

### What the "penalty" actually is

The estimated tax penalty under §6654 is technically an "addition to tax," not a penalty. It is computed as interest on the underpayment amount for the period of underpayment. The rate is the federal short-term rate plus 3 percentage points (§6621(a)(2)), compounded daily (§6622).

### Computation steps

For each installment period:

```
Step 1. Required installment amount (25% of required annual payment, or annualized amount)
Step 2. Amount paid by the due date (estimated payments + allocable withholding)
Step 3. Underpayment = Step 1 minus Step 2 (if positive)
Step 4. Period of underpayment:
        - Starts: installment due date
        - Ends: EARLIER of (a) actual payment date, or (b) April 15 of following year
Step 5. Penalty = Underpayment x daily rate x number of days in the period
```

### Withholding allocation

Under §6654(b)(2), withholding is treated as paid ratably throughout the year unless the taxpayer elects to use actual withholding dates by filing Form 2210 with box A checked. For most sole proprietors (whose withholding, if any, comes from a spouse's W-2 throughout the year), the ratable allocation is favorable.

### Penalty waiver provisions

The IRS may waive the penalty under IRC §6654(e)(3) in two cases:

1. **Casualty, disaster, or other unusual circumstances** where imposition of the penalty would be against equity and good conscience
2. **Retirement or disability** — the taxpayer retired (after reaching age 62) or became disabled in the current or prior tax year, and the underpayment was due to reasonable cause and not willful neglect

Waiver is requested on Form 2210 by checking box B (Part II) and attaching an explanation.

### When the IRS computes the penalty for you

If the taxpayer does not file Form 2210, the IRS will compute the penalty and send a bill. In many cases, taxpayers choose to let the IRS compute the penalty because:
- It is often small
- The IRS computation may be more favorable if withholding timing is beneficial
- It avoids the complexity of Form 2210

However, filing Form 2210 is **required** if the taxpayer uses the annualized income installment method, requests a waiver, or wants to use actual withholding dates.

---

## Section 9 — Special situations

### Withholding strategy for married couples

When one spouse is self-employed and the other has W-2 income, a common and fully legitimate strategy is to increase the W-2 spouse's withholding to cover both spouses' tax liability. This eliminates the need for estimated payments entirely if withholding meets the safe harbor.

**How to implement:** File a new Form W-4 with the W-2 employer, increasing the "Extra withholding" amount on Step 4(c) by the quarterly estimated tax amount times the number of remaining pay periods.

**Advantage:** Withholding is treated as paid ratably throughout the year (§6654(b)(2)), even if the W-4 change happens mid-year. This is a planning advantage over estimated payments, which must be timely per quarter.

### First year of self-employment

If the taxpayer had zero tax liability in the prior year (e.g., the prior year was the taxpayer's first year, or they had significant losses), the prior-year safe harbor requires zero estimated payments. The current-year method (90%) still applies as an alternative ceiling, but the taxpayer need only pay the lesser of the two methods — which is zero.

### Mid-year income changes

If the taxpayer's income changes significantly mid-year (e.g., loss of a major client, new contract), the annualized income installment method (Section 7) is the primary tool for adjusting installments without penalty. The taxpayer may also simply adjust future estimated payments up or down, but the safe harbor is computed on the full-year required annual payment, not quarter-by-quarter.

### Fiscal year taxpayers

This skill covers calendar year taxpayers only (virtually all sole proprietors). Fiscal year filers have different installment due dates under §6654(c)(2) and should consult IRS Publication 505 or a tax professional.

---

## Section 10 — Conservative defaults table

| Situation | Conservative default | Rationale |
|---|---|---|
| Prior-year AGI unknown | Assume > $150K; use 110% safe harbor | Avoids underpayment if AGI turns out to be high |
| Underpayment rate uncertain for future quarter | Use most recently published rate | Rates rarely drop dramatically; small variance |
| Taxpayer has both W-2 withholding and SE income | Do not assume W-2 covers SE; compute explicitly | Avoids surprise underpayment |
| Taxpayer is unsure whether to use annualized method | Default to equal installments; flag annualized option for reviewer | Annualized method requires Schedule AI and increases complexity |
| Mid-year estimate of SE income uncertain | Use year-to-date income, annualize, and add 10% buffer | Conservative cushion against Q4 surge |
| Prior year return not yet filed | Use last filed return; flag for reviewer | Cannot compute safe harbor without prior year data |

---

## Section 11 — PROHIBITIONS

The skill MUST NOT:

1. **File estimated payments or generate payment instructions** — the skill computes amounts; payment execution is the taxpayer's responsibility
2. **Recommend underpaying estimated tax as a "strategy"** — underpayment triggers statutory penalties; the skill never advises intentional underpayment
3. **Compute state estimated tax** — state rules differ materially (different safe harbors, different installment schedules); defer to state-specific skills
4. **Override the reviewer's judgment on method selection** — the choice between equal installments and annualized method, or between prior-year and current-year safe harbor, is the reviewer's call
5. **Guarantee that a particular safe harbor eliminates all penalties** — the skill surfaces the rules but cannot predict final tax liability mid-year
6. **Advise on estimated tax for entities other than sole proprietors / disregarded SMLLCs** — partnerships, S-corps, C-corps, and trusts have different estimated tax regimes
7. **Compute the Additional Medicare Tax or NIIT in isolation** — these are computed by upstream skills; this skill uses their outputs
8. **Apply penalty waiver without reviewer approval** — waiver under §6654(e)(3) is discretionary with the IRS and fact-intensive

---

## Section 12 — Edge cases

**Edge Case 1 — Prior year was a short tax year.**
If the taxpayer's prior year return covered fewer than 12 months (e.g., first-year return for a taxpayer who changed tax years), the prior-year safe harbor does not apply. Only the current-year 90% method is available. IRC §6654(d)(1)(B)(ii). Flag for reviewer.

**Edge Case 2 — Prior year tax was zero but AGI was high.**
If the prior year return showed zero tax liability (due to credits, NOLs, or other items) but high AGI, the required annual payment under the prior-year method is $0, even though the 110% threshold would technically apply. The zero-tax rule dominates. §6654(e)(2).

**Edge Case 3 — Taxpayer dies mid-year.**
Estimated tax payments are required only through the quarter in which the taxpayer dies. The estate takes over for subsequent periods. The decedent's final return Form 2210 should reflect only the installments through the date of death. Treas. Reg. §1.6654-2(d).

**Edge Case 4 — Large Q4 income for freelancer.**
A freelancer earns $20K in Q1-Q3 combined but lands a $180K project payment in Q4. Under equal installments, Q1-Q3 payments based on prior-year safe harbor would be adequate. Under the current-year method, the annualized method on Schedule AI would show low required installments for Q1-Q3 and a large Q4 installment. The prior-year safe harbor is typically the better choice here if available.

**Edge Case 5 — Taxpayer switches from W-2 to self-employment mid-year.**
The taxpayer had W-2 withholding through June, then became self-employed. Withholding from the W-2 period is treated as paid ratably across all four quarters (unless Form 2210 box A is checked). This ratable treatment may cover early installments. The annualized method can reduce required installments for Q1/Q2 when self-employment income only existed in Q3/Q4.

**Edge Case 6 — Estimated payments exceed actual tax liability.**
Overpayments are applied to the following year's estimated tax or refunded, at the taxpayer's election (Form 1040, line 36). The skill should note the overpayment and flag the election choice for the reviewer.

**Edge Case 7 — Taxpayer makes unequal estimated payments.**
The safe harbor analysis compares total payments to total required, but underpayment penalties are computed per-quarter. A taxpayer who pays $0 in Q1 and makes up the shortfall in Q2 still owes a penalty for Q1's underpayment period (Q1 due date through Q2 payment date). The skill must compute penalties quarter-by-quarter, not just on the annual shortfall.

**Edge Case 8 — Disaster area relief extends the due date.**
IRS disaster relief announcements (e.g., for hurricanes, wildfires) often postpone estimated tax due dates for affected taxpayers. The skill should check whether any IRS disaster relief notice applies to the taxpayer's area and adjust due dates accordingly. Flag for reviewer verification.

**Edge Case 9 — Farmer or fisherman exception.**
Taxpayers who earn at least 2/3 of their gross income from farming or fishing may file only one estimated payment (by January 15) or file their return by March 1 and pay in full to avoid penalties entirely. IRC §6654(i). This skill flags the exception but does not adjudicate farming/fishing income classification.

**Edge Case 10 — Net Investment Income Tax creates an unexpected estimated tax requirement.**
A sole proprietor who also has significant investment income (rental, capital gains, passive income) above the NIIT threshold ($200K single, $250K MFJ) must include the 3.8% NIIT in estimated tax calculations. The NIIT is not part of SE tax but is part of total tax liability.

---

## Section 13 — Test suite

### Test 1 — Basic prior-year safe harbor (standard)

**Input:** Sole proprietor, single filer, TY2024 AGI = $95,000, TY2024 total tax = $18,000. Expected TY2025 total tax = $22,000. No withholding.
**Expected output:**
- Prior-year safe harbor: 100% of $18,000 = $18,000
- Current-year method: 90% of $22,000 = $19,800
- Required annual payment: lesser = $18,000
- Quarterly payment: $18,000 / 4 = $4,500 per quarter
- Due dates: Apr 15, Jun 16, Sep 15, 2025; Jan 15, 2026

### Test 2 — High-income prior-year safe harbor (110%)

**Input:** Sole proprietor, MFJ, TY2024 AGI = $210,000, TY2024 total tax = $42,000. Expected TY2025 total tax = $55,000. No withholding.
**Expected output:**
- Prior-year safe harbor: 110% of $42,000 = $46,200 (AGI > $150K)
- Current-year method: 90% of $55,000 = $49,500
- Required annual payment: lesser = $46,200
- Quarterly payment: $46,200 / 4 = $11,550 per quarter

### Test 3 — Withholding eliminates estimated tax requirement

**Input:** Sole proprietor, MFJ. Spouse has W-2 withholding of $25,000/year. TY2024 total tax = $20,000. TY2024 AGI = $120,000. Expected TY2025 total tax = $28,000.
**Expected output:**
- Prior-year safe harbor: 100% of $20,000 = $20,000
- Spouse's withholding ($25,000) exceeds prior-year safe harbor ($20,000)
- No estimated payments required
- Result: withholding covers the safe harbor entirely

### Test 4 — Annualized income installment method

**Input:** Sole proprietor, single filer. No prior year return (first year of business). Income: Q1 = $5,000, Q2 = $8,000, Q3 = $12,000, Q4 = $75,000. Total SE income = $100,000. Expected total tax = $25,000. No withholding.
**Expected output:**
- Prior-year safe harbor: $0 (no prior year return / zero prior year tax)
- Required annual payment: lesser of 90% x $25,000 = $22,500 or $0 = **$0**
- No estimated payments required under prior-year method
- However, if prior-year method unavailable (no return filed): current-year 90% applies
- Flag for reviewer: first-year taxpayer, confirm prior year filing status
- If annualized method elected: Q1 installment = 25% x (tax on $5,000 x 4) = modest amount; Q4 installment absorbs remainder

### Test 5 — Underpayment penalty computation

**Input:** Sole proprietor, single filer. Required annual payment = $20,000 ($5,000/quarter). Actual payments: Q1 = $3,000, Q2 = $5,000, Q3 = $5,000, Q4 = $5,000. Total paid = $18,000. Underpayment rate = 7%.
**Expected output:**
- Q1 underpayment: $5,000 - $3,000 = $2,000
- Q1 penalty period: Apr 15, 2025 through Apr 15, 2026 (or actual payment date if earlier)
- Assuming the $2,000 shortfall is not made up until filing: penalty = $2,000 x 7% x (365/365) = approximately $140
- Q2-Q4: no underpayment (payments met required installments)
- Total Form 2210 penalty: approximately $140
- Note: excess Q2-Q4 payments do not retroactively cure Q1 underpayment for penalty purposes

### Test 6 — Under $1,000 threshold eliminates requirement

**Input:** Sole proprietor, single filer. Expected TY2025 total tax = $5,200. W-2 withholding from part-time job = $4,500. Net expected tax due = $700.
**Expected output:**
- Net tax due ($700) < $1,000 threshold
- No estimated payments required under §6654(e)(1)
- No penalty regardless of whether estimated payments are made

---

## Section 14 — Cross-skill references

**Inputs from upstream skills:**

- **From `us-schedule-c-and-se-computation`:** Schedule C net profit (Line 31), SE tax (Schedule SE), deductible half of SE tax
- **From `us-form-1040-self-employed-positions`:** QBI deduction amount, SE health insurance deduction, retirement contribution deduction, total 1040 tax liability after all above-the-line deductions and credits

**Outputs to downstream skills:**

- This skill is the terminal skill in the federal pipeline. Its output is the quarterly payment schedule and any Form 2210 penalty computation for the reviewer's brief.

**State interaction:**

- State estimated tax skills (e.g., `ca-estimated-tax-540es`) operate independently but may reference the federal estimated tax computation as a starting point. This skill includes a pointer to state skills but does not compute state amounts.

---

## Section 15 — Reference material

### Validation status

This file is v0.2 of `us-quarterly-estimated-tax`, drafted in April 2026. Year-specific figures are verified against IRC §6654, IRS Form 1040-ES (2025) Instructions, IRS Form 2210 (2025) Instructions, and IRS Publication 505 (2025).

### Known gaps

1. The underpayment interest rates are set quarterly and may change. The rates in Section 3 reflect published rates through early 2026. The reviewer must verify rates from the applicable IRS Revenue Rulings.
2. The skill does not handle AMT estimated tax for taxpayers subject to the alternative minimum tax. AMT increases total tax liability and therefore increases the estimated tax requirement, but AMT computation is out of scope.
3. Disaster area relief due date extensions are flagged but not tracked automatically. The reviewer must check IRS disaster relief announcements for the taxpayer's geographic area.
4. The interaction between estimated tax and the premium tax credit (Form 8962) is not addressed. Taxpayers receiving advance premium tax credits may have an unexpected tax liability at filing if income exceeds estimates.

### Change log

- **v0.1 (April 2026):** Stub.
- **v0.2 (April 2026):** Full skill. Tax year 2025. Built on `us-tax-workflow-base` v0.1.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
