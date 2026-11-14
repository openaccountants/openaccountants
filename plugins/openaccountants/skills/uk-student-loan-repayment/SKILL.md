---
name: uk-student-loan-repayment
description: "Use this skill whenever asked about UK Student Loan repayment for self-employed individuals. Trigger on phrases like \"student loan repayment\", \"Plan 1\", \"Plan 2\", \"Plan 4\", \"Plan 5\", \"Plan 5 student loan\", \"Postgraduate loan repayment\", \"postgraduate loan\", \"April 2026 student loan threshold\", \"student loan self-employed\", \"student loan Self Assessment\", \"SLC repayment\", \"student loan deduction\", or any question about student loan obligations for a self-employed client. Also trigger when classifying bank statement transactions showing SLC repayments via SA, PAYE student loan deductions, or direct SLC payments. This skill covers Plan 1-5 and Postgraduate Loan thresholds across three tax years (2024-25, 2025-26, 2026-27), self-employed SA calculation, multiple plan interaction, bank statement classification patterns, overseas earnings, write-off periods, and edge cases. ALWAYS read this skill before touching any UK student loan repayment work."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/uk-student-loan-repayment"
  jurisdiction: "GB"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# UK Student Loan Repayment

UK Student Loan Repayment for the self-employed, tax year 2026/27 (6 April 2026 to 5 April 2027), with the 2024/25 and 2025/26 figures for earlier returns. Every threshold below was read on the official page on 14 November 2026.

## Scope

**Read this whole skill before computing or classifying anything.**

This skill computes the student loan repayment a self-employed borrower makes through Self Assessment, offsets PAYE deductions, handles more than one plan, and classifies student loan items on a bank statement. It does not cover loan balances, interest, disputes with the Student Loans Company, or the overseas income assessment (refer, see When to refuse or refer).

### Quick reference

- **Country:** United Kingdom
- **Primary Legislation:** Education (Student Loans) Act 1998; Education (Student Loans) (Repayment) Regulations 2009 (SI 2009/470)
- **Administering Body:** Student Loans Company (SLC); collected by HMRC via Self Assessment
- **Tax Years Covered:** 2024-25, 2025-26, 2026-27
- **Currency:** GBP only
- **Payment method:** Via Self Assessment, with the balancing payment due 31 January after the tax year. Not part of payments on account
- **Not tax-deductible:** Student loan repayments are NOT business expenses
- **Contributor:** Open Accountants
- **Review status:** Source-cited draft: not reviewed by an accountant.

### Student loan repayment, tax year 2026/27, at a glance

- **Plan 1, 2026/27:** GBP 26,900 a year, 9% above it
- **Plan 2, 2026/27:** GBP 29,385 a year, 9% above it
- **Plan 4, 2026/27:** GBP 33,795 a year, 9% above it
- **Plan 5, 2026/27:** GBP 25,000 a year, 9% above it
- **Postgraduate Loan, 2026/27:** GBP 21,000 a year, 6% above it
- **Tax-deductible?** No. Repayments are not a business expense.
- **Capital gains included?** No.
- **Unearned income included?** Only if total unearned income is over GBP 2,000.

## Ask the client first

### Required inputs

**Minimum viable**: plan type(s), tax year, and total taxable income (all sources).

**Recommended**: P60 or payslips showing PAYE student loan deductions, bank statements showing SA payments, SLC online account balance.

**Ideal**: complete SA100 return data, SLC repayment schedule, confirmation of plan type from SLC.

### Conservative defaults

| Ambiguity | Default |
| --- | --- |
| Unknown plan type | STOP: do not guess; direct client to SLC |
| Unknown total income | Ask: threshold comparison requires total relevant income |
| Unknown PAYE deductions | Ask: PAYE offset affects SA balance |
| Unknown unearned income | Ask if total unearned > GBP 2,000 (GBP 2,000 or below = excluded) |
| Unknown overseas status | Flag for reviewer: SLC applies country-specific thresholds |
| 2027-28 threshold unknown | Flag "verify when HMRC announces" |

### Onboarding fallback (bank statement only)

If the client provides only a bank statement:

1. **Identify HMRC SA payments**: these contain the student loan component (if any).
2. **Look for direct SLC payments**: these are voluntary overpayments.
3. **Flag:** "Student loan repayments for self-employed are collected through Self Assessment and combined with income tax and NIC in a single HMRC payment. The bank statement cannot isolate the student loan component. Please provide the SA302 tax calculation and confirm the plan type with SLC."

## The method, step by step

1. **Confirm the plan type(s)** with the client or SLC (eligibility below). Never guess.
2. **Pick the tax year's thresholds** from the rates table. If the year's threshold is not yet published, stop and flag (Rule 10).
3. **Work out total relevant income** (Rule 2): all income for income tax, with unearned income only if it exceeds GBP 2,000, and no capital gains.
4. **Apply the formula** (Rule 1) for one plan, or the multiple-plans rule (Rule 4).
5. **Deduct PAYE student loan deductions** already made (Rule 3).
6. **Put the balance on the 31 January balancing payment**, not the payments on account (Rule 6).
7. **Check write-off proximity** before any advice on voluntary overpayments (Rule 7, T2-3).

### Rates, bands and thresholds

| Plan and year | Repayment threshold and rate | Applies | Official source |
| --- | --- | --- | --- |
| Plan 1, 2026/27 | GBP 26,900 a year, 9% | Income over the threshold | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Plan 2, 2026/27 | GBP 29,385 a year, 9% | Income over the threshold | same |
| Plan 4, 2026/27 | GBP 33,795 a year, 9% | Income over the threshold | same |
| Plan 5, 2026/27 | GBP 25,000 a year, 9% | Income over the threshold; collections from April 2026 | same |
| Postgraduate Loan, 2026/27 | GBP 21,000 a year, 6% | Income over the threshold | same |
| Plan 1, 2025/26 | GBP 26,065 a year, 9% | 2025/26 returns | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026 |
| Plan 2, 2025/26 | GBP 28,470 a year, 9% | 2025/26 returns | same |
| Plan 4, 2025/26 | GBP 32,745 a year, 9% | 2025/26 returns | same |
| Postgraduate Loan, 2025/26 | GBP 21,000 a year, 6% | 2025/26 returns | same |
| Plan 1, 2024/25 | GBP 24,990 a year, 9% | 2024/25 returns | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025 |
| Plan 2, 2024/25 | GBP 27,295 a year, 9% | 2024/25 returns | same |
| Plan 4, 2024/25 | GBP 31,395 a year, 9% | 2024/25 returns | same |
| Postgraduate Loan, 2024/25 | GBP 21,000 a year, 6% | 2024/25 returns | same |
| Rates, all plans 2026/27 | 9% over the threshold on Plan 1, 2, 4 or 5; 6% over the threshold on a Postgraduate Loan | Borrower's yearly income | https://www.gov.uk/repaying-your-student-loan/what-you-pay |
| Unearned income | Excluded unless it exceeds GBP 2,000 for the year | Total income for repayment | https://www.legislation.gov.uk/uksi/2009/470/regulation/29 |
| Combination of plan 1, 2, 4 or 5 loans | The threshold of the loan with the lowest threshold applies | SI 2009/470 reg 29(5A) | same |

Plan 5 has no 2024/25 or 2025/26 row: collections began in 2026/27, so no Plan 5 repayment is due for those years (Rule 8). Thresholds change on 6 April each year: check the next year's figures before using them.

### Which plan the client is on

- **Plan 1 eligibility**: Student Finance England or Wales courses started before 1 September 2012; all Student Finance Northern Ireland borrowers (undergraduate and postgraduate).
- **Plan 2 eligibility**: Student Finance England courses started 1 September 2012 to 31 July 2023; Student Finance Wales undergraduate or PGCE courses started on or after 1 September 2012.
- **Plan 4 eligibility**: all Student Awards Agency Scotland borrowers, undergraduate or postgraduate.
- **Plan 5 eligibility**: Student Finance England undergraduate or PGCE courses started on or after 1 August 2023 (collections began April 2026).
- **Postgraduate Loan (PGL) eligibility**: England/Wales master's and doctoral loans.

Plan eligibility source: [Which repayment plan you're on](https://www.gov.uk/repaying-your-student-loan/which-repayment-plan-you-are-on), read on 2026-11-14.

### Rule 1: single plan formula

Repayment = (total_relevant_income - threshold) x rate. If the result is negative, repayment = GBP 0.

### Rule 2: what income counts

| Income Type | Included? |
| --- | --- |
| Self-employment profits (SA103) | Yes |
| Employment income (SA100) | Yes (but PAYE deductions offset) |
| Savings income | Yes, if total unearned > GBP 2,000 |
| Dividend income | Yes, if total unearned > GBP 2,000 |
| Rental income | Yes, if total unearned > GBP 2,000 |
| Pension income | Yes |
| Capital gains | No |

### Rule 3: PAYE offset

Total repayment due = (total_relevant_income - threshold) x rate. Less: PAYE deductions already made. = Balance due via Self Assessment. If PAYE exceeds total due, the client claims a refund from SLC (not HMRC).

### Rule 4: multiple plans

Plans 1, 2, 4 and 5 together give one 9% repayment above the lowest of their thresholds, not one charge per plan (Education (Student Loans) (Repayment) Regulations 2009, reg 29(5A); [GOV.UK: repaying your student loan](https://www.gov.uk/repaying-your-student-loan/print)). A Postgraduate Loan is a separate 6% charge above its own threshold, paid at the same time (reg 29(3A)).

| Combination (2025-26 figures) | Calculation | Source |
| --- | --- | --- |
| Plan 2 + Postgraduate Loan | 9% above GBP 28,470 AND 6% above GBP 21,000 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026 |
| Plan 1 + Postgraduate Loan | 9% above GBP 26,065 AND 6% above GBP 21,000 | same |
| Plan 1 + Plan 2 | One 9% charge above GBP 26,065 (the lower threshold). SLC splits it between the loans | same |

**Maximum combined rate**: 15% (9% + 6%) where the income is above both the undergraduate plan threshold and the Postgraduate Loan threshold.

### Rule 5: not tax-deductible

Student loan repayments are NOT business expenses. They cannot be deducted from trading profits.

### Rule 6: payment schedule (via Self Assessment)

The whole student loan repayment for the year is due with the balancing payment on 31 January after the tax year. It is not included in payments on account, so it never goes into the 31 January or 31 July POA ([payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account): the balancing payment "will also include anything you owe for capital gains or student loans"). See uk-payments-on-account.

### Rule 7: write-off periods

| Plan | Write-off | Source |
| --- | --- | --- |
| Plan 1 (first loan paid before 1 September 2006) | Age 65 | https://www.gov.uk/repaying-your-student-loan/print |
| Plan 1 (first loan paid on or after 1 September 2006) | 25 years after the April first due to repay | same |
| Plan 2 | 30 years after the April first due to repay | same |
| Plan 4 (first loan paid on or after 1 August 2007) | 30 years after the April first due to repay | same |
| Plan 4 (first loan paid before 1 August 2007) | Age 65 or 30 years, whichever comes first | same |
| Plan 5 | 40 years after the April first due to repay | same |
| Postgraduate Loan (England or Wales) | 30 years after the April first due to repay | same |

### Rule 8: Plan 5 timing

Plan 5 collections began April 2026. For 2024-25 SA, no Plan 5 repayment is due. For 2025-26 SA, no Plan 5 repayment is due either (collections only begin in tax year 2026-27). From 2026-27 onwards, Plan 5 repayments apply at 9% above the published threshold.

### Rule 9: unearned income rule

Total unearned income (savings + dividends + rent) only counts if it exceeds GBP 2,000 a year (SI 2009/470 reg 29).

### Rule 10: threshold publication timing

HMRC publishes student loan thresholds annually, typically in the months preceding the start of the tax year (April). When a threshold for an upcoming year is not yet announced, flag for reviewer rather than estimating.

## Boundary and exception table

### Tier 2 catalogue

| Code | Trigger | Action |
| --- | --- | --- |
| T2-1 Multiple plan interaction | Client has more than one plan type simultaneously | Confirm plan types with SLC before computing. Undergraduate plans (1, 2, 4, 5) share one 9% charge above the lowest threshold; a Postgraduate Loan adds 6% above its own threshold |
| T2-2 Overseas earnings | Client lives outside the UK for more than 3 months | SLC applies country-specific thresholds. Do not use UK thresholds. Escalate |
| T2-3 Approaching write-off date | Client is within 2 years of write-off | Advise against voluntary overpayments. Flag for reviewer to confirm exact write-off date with SLC |
| T2-4 Mid-year overseas move | Client was UK-resident part of the year, then moved abroad | UK SA covers the UK-resident period; SLC overseas assessment covers the rest. Flag for reviewer |
| T2-5 Early repayment decision | Client asks whether to make voluntary overpayments | Flag for reviewer. Consider interest rates, write-off proximity, and opportunity cost |
| T2-6 Next year's threshold not yet published | Computation requires a 2027-28 or later threshold that HMRC has not announced | Use the latest published figure as a placeholder, clearly label "PROVISIONAL: threshold pending HMRC announcement", and flag for reviewer to revisit once HMRC publishes |

### Payment pattern library (bank statements)

This is the deterministic pre-classifier for bank statement transactions related to student loan repayments.

**Student loan repayments via Self Assessment**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| HMRC SELF ASSESSMENT | EXCLUDE: combined SA payment | Student loan repayment is embedded in the SA payment alongside income tax and NIC; cannot isolate from bank statement |
| HMRC, HM REVENUE & CUSTOMS | EXCLUDE: SA payment | Same: student loan component included |
| SA PAYMENT, SA BALANCING | EXCLUDE: SA payment | Same |

**Direct SLC payments (voluntary overpayments or overseas)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SLC, STUDENT LOANS COMPANY | EXCLUDE: student loan repayment | Direct payment to SLC (voluntary overpayment or overseas repayment) |
| STUDENT LOAN, STUDENT LOANS | EXCLUDE: student loan | Generic reference |
| ERUDIO STUDENT LOANS | EXCLUDE: legacy loan | Pre-1998 mortgage-style loans (now managed by Erudio) |

**PAYE deductions (visible on payslips, not bank statement)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, WAGES (incoming credit) | Not a student loan payment | Student loan deduction already made at source by employer: net salary shown on bank statement is post-deduction |

**SLC refunds**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SLC REFUND, STUDENT LOANS REFUND | EXCLUDE: refund of overpayment | SLC refunds overpaid amounts directly |

### How student loan payments appear on UK bank statements

**Via Self Assessment (most common for self-employed):**
- Combined with income tax and NIC in a single HMRC debit
- Cannot identify student loan component from bank statement alone
- Need SA302 tax calculation for breakdown
- Timing: 31 Jan (with the balancing payment); never in the 31 Jul payment on account

**Direct to SLC (voluntary overpayments):**
- Description: "STUDENT LOANS COMPANY", "SLC"
- Any timing (client-initiated)
- Clearly identifiable as student loan specific

**PAYE deductions (employed clients with additional self-employment):**
- Not visible on bank statement: deducted from gross salary before net payment
- Visible on payslips and P60 only

**Key identification tips:**
1. For self-employed, student loan is almost always embedded in SA payments
2. The SA302 is the only reliable source for the student loan component
3. Direct SLC payments are voluntary overpayments
4. SLC refunds appear as credits from SLC

## Worked cases

All amounts are illustrations, not client data.

### Checked examples

```oa-check
name: Plan 2 and Postgraduate Loan, income GBP 42,000 (2024/25)
inputs:
  income: 42000
  plan2: 27295
  pgl: 21000
steps:
  - p2: pct(income - plan2, 9)
  - pg: pct(income - pgl, 6)
  - total: p2 + pg
expected:
  p2: 1323.45
  pg: 1260
  total: 2583.45
```

```oa-check
name: Plan 2 and Postgraduate Loan, income GBP 42,000 (2026/27)
inputs:
  income: 42000
  plan2: 29385
  pgl: 21000
steps:
  - p2: pct(income - plan2, 9)
  - pg: pct(income - pgl, 6)
  - total: p2 + pg
expected:
  p2: 1135.35
  pg: 1260
  total: 2395.35
```

### Three-year worked example: Plan 2 + PGL SA filer

Hypothetical: a self-employed UK consultant with both a Plan 2 undergraduate loan and a Postgraduate Loan. Trading profits are the only relevant income (no employment, no unearned income above GBP 2,000). Demonstrates how the SA deduction shifts as thresholds rise. Assume trading profits of **GBP 42,000** in each of the three years (held constant to isolate the threshold effect).

**Year 1: 2024-25**

| Component | Threshold | Income above | Rate | Repayment | Source |
| --- | --- | --- | --- | --- | --- |
| Plan 2 | GBP 27,295 | GBP 14,705 | 9% | GBP 1,323.45 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025 |
| PGL | GBP 21,000 | GBP 21,000 | 6% | GBP 1,260.00 | same |
| **Total via SA** |  |  |  | **GBP 2,583.45** | same |

**Year 2: 2025-26**

| Component | Threshold | Income above | Rate | Repayment | Source |
| --- | --- | --- | --- | --- | --- |
| Plan 2 | GBP 28,470 | GBP 13,530 | 9% | GBP 1,217.70 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026 |
| PGL | GBP 21,000 | GBP 21,000 | 6% | GBP 1,260.00 | same |
| **Total via SA** |  |  |  | **GBP 2,477.70** | same |

Change from 2024-25: **down GBP 105.75** (Plan 2 threshold rose by GBP 1,175; GBP 1,175 x 9% = GBP 105.75 less on Plan 2; PGL threshold unchanged).

**Year 3: 2026-27**

| Component | Threshold | Income above | Rate | Repayment | Source |
| --- | --- | --- | --- | --- | --- |
| Plan 2 | GBP 29,385 | GBP 12,615 | 9% | GBP 1,135.35 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| PGL | GBP 21,000 | GBP 21,000 | 6% | GBP 1,260.00 | same |
| **Total via SA** |  |  |  | **GBP 2,395.35** | same |

Change from 2025-26: **down GBP 82.35** (Plan 2 threshold rose by GBP 915; GBP 915 x 9% = GBP 82.35 less on Plan 2; PGL threshold unchanged).

**Key takeaway:** With constant profits of GBP 42,000, the SA deduction shifts modestly year-on-year as Plan 2 thresholds rise. The PGL component is currently insensitive to threshold movement because PGL is frozen.

### Bank statement classifications

Six bank statement classifications for a hypothetical UK self-employed graphic designer with a Plan 2 loan and Postgraduate Loan.

**Example 1: SA balancing payment (includes student loan).** Input line: `31.01.2027 ; HMRC SELF ASSESSMENT ; DEBIT ; BALANCING PAYMENT ; -5,800.00 ; GBP`. Reasoning: matches "HMRC SELF ASSESSMENT". This is the 31 January balancing payment. Includes income tax + Class 4 NIC + student loan repayment combined. Cannot isolate student loan component from bank statement. Need SA302 for breakdown. Classification: EXCLUDE, combined SA payment. Request SA302 for student loan component.

**Example 2: voluntary overpayment direct to SLC.** Input line: `15.05.2026 ; STUDENT LOANS COMPANY ; DEBIT ; VOLUNTARY OVERPAYMENT ; -500.00 ; GBP`. Reasoning: matches "STUDENT LOANS COMPANY". This is a voluntary overpayment made directly to SLC. Not deductible. Not part of SA. Reduces outstanding loan balance. Classification: EXCLUDE, voluntary student loan overpayment. Not tax-deductible.

**Example 3: employment salary (PAYE deduction already made).** Input line: `28.02.2026 ; DESIGN AGENCY LTD ; CREDIT ; FEB SALARY ; +2,400.00 ; GBP`. Reasoning: employment income. If the client is on Plan 2, the employer has already deducted student loan repayments from gross salary before paying the net amount. The GBP 2,400 is post-deduction. This is NOT a student loan payment visible on the bank statement. Classification: NOT a student loan payment. PAYE deduction already made at source.

**Example 4: SLC refund.** Input line: `20.06.2026 ; SLC REFUND ; CREDIT ; OVERPAYMENT REFUND ; +320.00 ; GBP`. Reasoning: matches "SLC REFUND". Client overpaid and SLC is refunding. Not taxable income. Not a student loan payment. Classification: EXCLUDE, refund from SLC. Not taxable.

**Example 5: payment on account (no student loan in it).** Input line: `31.07.2026 ; HMRC ; DEBIT ; 2ND PAYMENT ON ACCOUNT ; -2,900.00 ; GBP`. Reasoning: matches "HMRC". Second payment on account. Covers income tax and Class 4 NIC only. Student loan repayments are not part of payments on account: they are paid with the balancing payment on 31 January ([payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account)). Classification: EXCLUDE, SA payment on account. No student loan component. Look for the student loan in the 31 January payment and confirm it from the SA302.

**Example 6: Erudio legacy loan payment.** Input line: `01.04.2026 ; ERUDIO STUDENT LOANS ; DEBIT ; MONTHLY REPAYMENT ; -180.00 ; GBP`. Reasoning: matches "ERUDIO STUDENT LOANS". This is a pre-1998 mortgage-style student loan managed by Erudio. Separate from the income-contingent plans. Monthly fixed repayments. Classification: EXCLUDE, legacy student loan repayment. Not tax-deductible.

### Test suite (2025-26 figures unless stated)

- **Test 1:** Plan 2, self-employed, income GBP 35,000. (GBP 35,000 - GBP 28,470) x 9% = GBP 587.70.
- **Test 2:** Plan 1, self-employed, income GBP 60,000. (GBP 60,000 - GBP 26,065) x 9% = GBP 3,054.15.
- **Test 3:** Plan 4, self-employed, income GBP 40,000. (GBP 40,000 - GBP 32,745) x 9% = GBP 652.95.
- **Test 4:** Plan 5 (2026-27), income GBP 30,000. (GBP 30,000 - GBP 25,000) x 9% = GBP 450.00.
- **Test 5:** PGL only, income GBP 28,000. (GBP 28,000 - GBP 21,000) x 6% = GBP 420.00.
- **Test 6:** Plan 2 + PGL, income GBP 45,000 (2025-26). Plan 2 = GBP 1,487.70, PGL = GBP 1,440.00. Total = GBP 2,927.70.
- **Test 7:** Plan 2, income GBP 25,000. Below threshold. Repayment = GBP 0.
- **Test 8:** Plan 1, employed GBP 28,000 (PAYE deductions made) + self-employed GBP 12,000. Total GBP 40,000 (2025-26). Total = GBP 1,254.15. Less PAYE GBP 174.15. Balance via SA = GBP 1,080.00.
- **Test 9 (3-year sensitivity):** Plan 2 + PGL, profits GBP 42,000 each year. 2024-25: Plan 2 GBP 1,323.45 + PGL GBP 1,260.00 = GBP 2,583.45. 2025-26: Plan 2 GBP 1,217.70 + PGL GBP 1,260.00 = GBP 2,477.70. 2026-27: Plan 2 GBP 1,135.35 + PGL GBP 1,260.00 = GBP 2,395.35.

## When to refuse or refer

### Refusal catalogue

- **R-UK-SL-1: plan type unknown.** Trigger: client does not know plan type. Message: "Do not guess the plan type. Direct the client to check at repaymentplan.studentloanrepayment.co.uk or call SLC directly."
- **R-UK-SL-2: overseas borrower.** Trigger: client lives outside the UK for 3+ months. Message: "SLC conducts an overseas income assessment with country-specific thresholds. Do not use UK thresholds. Escalate to SLC directly."
- **R-UK-SL-3: loan cancellation or SLC error.** Trigger: client disputes loan balance or believes SLC has made an error. Message: "Loan balance disputes and administrative errors must be resolved directly with SLC. Out of scope."
- **R-UK-SL-4: next year's thresholds not yet published.** Trigger: a 2027-28 or later computation requires a specific threshold that HMRC has not yet announced. Message: "Thresholds are published annually by HMRC and may not yet be confirmed. Flag for reviewer and verify before finalising any computation."

### Prohibitions

- NEVER guess the client's plan type
- NEVER include capital gains in the repayment income calculation
- NEVER treat student loan repayments as tax-deductible
- NEVER apply UK thresholds to overseas borrowers
- NEVER advise voluntary overpayments without checking write-off proximity
- NEVER charge 9% twice for two undergraduate plans: one 9% charge applies above the lowest threshold; only a Postgraduate Loan adds a second (6%) charge
- NEVER assume PAYE deductions have been made: verify with payslips or P60
- NEVER present figures without noting that SLC manages the loan balance and interest
- NEVER finalise a year's figures without confirming HMRC has published that year's thresholds
- NEVER include unearned income if total unearned is GBP 2,000 or less

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Filing and payment

- The repayment is computed on the SA100 return and paid with the **balancing payment on 31 January** after the tax year. It is never in a payment on account.
- PAYE deductions already made are set against it; an overpayment is refunded by SLC, not HMRC.
- The SA302 tax calculation shows the student loan line; it is the evidence for the amount.

### Working paper template

```
UK STUDENT LOAN REPAYMENT: WORKING PAPER
Client: [name]
Tax Year: [2024-25 / 2025-26 / 2026-27]
Prepared: [date]

INPUT DATA
  Plan type(s):                    [Plan 1/2/4/5/PGL]
  Total relevant income:           GBP [____]
  Employment income:               GBP [____]
  Self-employment profits:         GBP [____]
  Unearned income (if > GBP 2,000): GBP [____]
  PAYE student loan deductions:    GBP [____]

PLAN [X] CALCULATION
  Threshold:                       GBP [____]   (flag if the year's threshold is not yet published)
  Income above threshold:          GBP [____]
  Rate:                            [9% / 6%]
  Gross repayment:                 GBP [____]
  Less PAYE deductions:            GBP [____]
  Net repayment via SA:            GBP [____]

[REPEAT FOR ADDITIONAL PLANS]

TOTAL STUDENT LOAN VIA SA:         GBP [____]

PAYMENT SCHEDULE
  Balancing payment (31 Jan):      GBP [____]   (student loan is not in POAs)

REVIEWER FLAGS
  [List any Tier 2 flags, including threshold confirmation for any unpublished year]
```

## Completion checklist

- [ ] Plan type(s) confirmed with the client or SLC.
- [ ] Thresholds taken from the right tax year's row, and that year is published.
- [ ] Total relevant income built; unearned income included only above GBP 2,000; no capital gains.
- [ ] One 9% charge for undergraduate plans above the lowest threshold; 6% Postgraduate Loan added separately.
- [ ] PAYE deductions checked against payslips or P60 and offset.
- [ ] Balance placed on the 31 January balancing payment, not the POAs.
- [ ] Overseas, write-off and voluntary overpayment flags raised where they apply.
- [ ] Not deducted as a business expense.

## Sources

| Source | What was read | URL | Read on |
|---|---|---|---|
| HMRC, Rates and thresholds for employers 2026 to 2027 | Read for the Plan 1, 2, 4 and 5 and Postgraduate Loan thresholds and the 9% and 6% deduction rates for 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 | 2026-11-14 |
| HMRC, Rates and thresholds for employers 2025 to 2026 | Read for the Plan 1, 2 and 4 and Postgraduate Loan thresholds for 2025/26 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026 | 2026-11-14 |
| HMRC, Rates and thresholds for employers 2024 to 2025 | Read for the Plan 1, 2 and 4 and Postgraduate Loan thresholds for 2024/25 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025 | 2026-11-14 |
| GOV.UK, Repaying your student loan: what you pay | Read for the 2026/27 thresholds table and the 9% and 6% rates | https://www.gov.uk/repaying-your-student-loan/what-you-pay | 2026-11-14 |
| GOV.UK, Repaying your student loan (print version) | Read for the lowest-threshold rule, the 3-month overseas rule and the write-off periods | https://www.gov.uk/repaying-your-student-loan/print | 2026-11-14 |
| GOV.UK, Which repayment plan you're on | Read for the plan eligibility dates and the Northern Ireland and Scotland plans | https://www.gov.uk/repaying-your-student-loan/which-repayment-plan-you-are-on | 2026-11-14 |
| GOV.UK, Payments on account | Read for student loans paid with the balancing payment | https://www.gov.uk/understand-self-assessment-bill/payments-on-account | 2026-11-14 |
| Education (Student Loans) (Repayment) Regulations 2009, reg 29 | Read for the GBP 2,000 unearned income rule, reg 29(3A) and the lowest-threshold rule in reg 29(5A) | https://www.legislation.gov.uk/uksi/2009/470/regulation/29 | 2026-11-14 |

Not yet confirmed: the 2027/28 thresholds (not yet published by HMRC; flag per Rule 10).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `uk-student-loan-repayment` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/uk-student-loan-repayment. If neither is available, confirm every figure against the official source pages cited above before relying on it.
