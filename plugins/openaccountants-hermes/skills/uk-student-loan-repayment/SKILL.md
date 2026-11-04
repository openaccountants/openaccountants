---
name: uk-student-loan-repayment
description: "Use this skill whenever asked about UK Student Loan repayment for self-employed individuals. Trigger on phrases like \"student loan repayment\", \"Plan 1\", \"Plan 2\", \"Plan 4\", \"Plan 5\", \"Plan 5 student loan\", \"Postgraduate loan repayment\", \"postgraduate loan\", \"April 2026 student loan threshold\", \"student loan self-employed\", \"student loan Self Assessment\", \"SLC repayment\", \"student loan deduction\", or any question about student loan obligations for a self-employed client. Also trigger when classifying bank statement transactions showing SLC repayments via SA, PAYE student loan deductions, or direct SLC payments. This skill covers Plan 1-5 and Postgraduate Loan thresholds across three tax years (2024-25, 2025-26, 2026-27), self-employed SA calculation, multiple plan interaction, bank statement classification patterns, overseas earnings, write-off periods, and edge cases. ALWAYS read this skill before touching any UK student loan repayment work."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/uk-student-loan-repayment"
  jurisdiction: "GB"
  tax_year: "2026"
  last_updated: "2026-10-23"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# UK Student Loan Repayment

## UK Student Loan Repayment -- Self-Employed Skill v2.2

## Rates and thresholds

> Source-cited draft: not reviewed by an accountant.

### Student loan repayment, tax year 2026/27 (6 April 2026 to 5 April 2027)

Source: [Rates and thresholds for employers 2026 to 2027](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) and [Repaying your student loan: what you pay](https://www.gov.uk/repaying-your-student-loan/what-you-pay), read on 2026-10-23.

- **Plan 1, 2026/27:** £26,900 a year, 9% above it
- **Plan 2, 2026/27:** £29,385 a year, 9% above it
- **Plan 4, 2026/27:** £33,795 a year, 9% above it
- **Plan 5, 2026/27:** £25,000 a year, 9% above it
- **Postgraduate Loan, 2026/27:** £21,000 a year, 6% above it
- **Tax-deductible?** No. Repayments are not a business expense.
- **Capital gains included?** No.
- **Unearned income included?** Only if total unearned income is over £2,000.

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | United Kingdom |
| Primary Legislation | Education (Student Loans) Act 1998; Education (Student Loans) (Repayment) Regulations 2009 (SI 2009/470) |
| Administering Body | Student Loans Company (SLC); collected by HMRC via Self Assessment |
| Tax Years Covered | 2024-25, 2025-26, 2026-27 |
| Currency | GBP only |
| Payment method | Via Self Assessment, with the balancing payment due 31 January after the tax year. Not part of payments on account |
| Not tax-deductible | Student loan repayments are NOT business expenses |
| Contributor | Open Accountants |
| Review status | Source-cited draft: not reviewed by an accountant. |

### 1.1 Three-year threshold table -- all plans

**Three-year threshold table**

| Plan | Rate | 2024-25 Threshold | 2025-26 Threshold | 2026-27 Threshold |
| --- | --- | --- | --- | --- |
| Plan 1 | 9% | £24,990 | £26,065 | £26,900 |
| Plan 2 | 9% | £27,295 | £28,470 | £29,385 |
| Plan 4 | 9% | £31,395 | £32,745 | £33,795 |
| Plan 5 | 9% | £25,000 | £25,000 (frozen by SLC) | £25,000 |
| Postgraduate Loan | 6% | £21,000 | £21,000 | £21,000 |

**2026-27 thresholds:** published by HMRC in [Rates and thresholds for employers 2026 to 2027](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) and by SLC in [Repaying your student loan: what you pay](https://www.gov.uk/repaying-your-student-loan/what-you-pay), both read on 2026-10-23. Plan 5 and the Postgraduate Loan stay at £25,000 and £21,000. Thresholds change on 6 April each year: check the next year's figures before using them.

- **Plan 1 eligibility** — Student Finance England or Wales courses started before 1 September 2012; all Student Finance Northern Ireland borrowers (undergraduate and postgraduate).
- **Plan 2 eligibility** — Student Finance England courses started 1 September 2012 to 31 July 2023; Student Finance Wales undergraduate or PGCE courses started on or after 1 September 2012.
- **Plan 4 eligibility** — all Student Awards Agency Scotland borrowers, undergraduate or postgraduate.
- **Plan 5 eligibility** — Student Finance England undergraduate or PGCE courses started on or after 1 August 2023 (collections began April 2026).
- **Postgraduate Loan (PGL) eligibility** — England/Wales master's and doctoral loans.

Plan eligibility source: [Which repayment plan you're on](https://www.gov.uk/repaying-your-student-loan/which-repayment-plan-you-are-on), read on 2026-10-23.

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown plan type | STOP -- do not guess; direct client to SLC |
| Unknown total income | Ask -- threshold comparison requires total relevant income |
| Unknown PAYE deductions | Ask -- PAYE offset affects SA balance |
| Unknown unearned income | Ask if total unearned > £2,000 (below £2,000 = excluded) |
| Unknown overseas status | Flag for reviewer -- SLC applies country-specific thresholds |
| 2027-28 threshold unknown | Flag "verify when HMRC announces" |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- plan type(s), tax year, and total taxable income (all sources).

**Recommended** -- P60 or payslips showing PAYE student loan deductions, bank statements showing SA payments, SLC online account balance.

**Ideal** -- complete SA100 return data, SLC repayment schedule, confirmation of plan type from SLC.

### Refusal catalogue

- **R-UK-SL-1 -- Plan type unknown** — Trigger: client does not know plan type. Message: "Do not guess the plan type. Direct the client to check at repaymentplan.studentloanrepayment.co.uk or call SLC directly."
- **R-UK-SL-2 -- Overseas borrower** — Trigger: client lives outside the UK for 3+ months. Message: "SLC conducts an overseas income assessment with country-specific thresholds. Do not use UK thresholds. Escalate to SLC directly."
- **R-UK-SL-3 -- Loan cancellation or SLC error** — Trigger: client disputes loan balance or believes SLC has made an error. Message: "Loan balance disputes and administrative errors must be resolved directly with SLC. Out of scope."
- **R-UK-SL-4 -- Next year's thresholds not yet published** — Trigger: a 2027-28 or later computation requires a specific threshold that HMRC has not yet announced. Message: "Thresholds are published annually by HMRC and may not yet be confirmed. Flag for reviewer and verify before finalising any computation."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to student loan repayments.

### 3.1 Student loan repayments via Self Assessment

**SA payment patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| HMRC SELF ASSESSMENT | EXCLUDE -- combined SA payment | Student loan repayment is embedded in the SA payment alongside income tax and NIC; cannot isolate from bank statement |
| HMRC, HM REVENUE & CUSTOMS | EXCLUDE -- SA payment | Same -- student loan component included |
| SA PAYMENT, SA BALANCING | EXCLUDE -- SA payment | Same |

### 3.2 Direct SLC payments (voluntary overpayments or overseas)

**Direct SLC payment patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SLC, STUDENT LOANS COMPANY | EXCLUDE -- student loan repayment | Direct payment to SLC (voluntary overpayment or overseas repayment) |
| STUDENT LOAN, STUDENT LOANS | EXCLUDE -- student loan | Generic reference |
| ERUDIO STUDENT LOANS | EXCLUDE -- legacy loan | Pre-1998 mortgage-style loans (now managed by Erudio) |

### 3.3 PAYE deductions (visible on payslips, not bank statement)

**PAYE deduction pattern**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, WAGES (incoming credit) | Not a student loan payment | Student loan deduction already made at source by employer -- net salary shown on bank statement is post-deduction |

### 3.4 SLC refunds

**SLC refund pattern**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SLC REFUND, STUDENT LOANS REFUND | EXCLUDE -- refund of overpayment | SLC refunds overpaid amounts directly |

## Section 4 -- Worked examples

Six bank statement classifications for a hypothetical UK self-employed graphic designer with a Plan 2 loan and Postgraduate Loan.

### Example 1 -- SA balancing payment (includes student loan)

**Input line:**
`31.01.2027 ; HMRC SELF ASSESSMENT ; DEBIT ; BALANCING PAYMENT ; -5,800.00 ; GBP`

**Reasoning:**
Matches "HMRC SELF ASSESSMENT" (pattern 3.1). This is the 31 January balancing payment. Includes income tax + Class 4 NIC + student loan repayment combined. Cannot isolate student loan component from bank statement. Need SA302 for breakdown.

**Classification:** EXCLUDE -- combined SA payment. Request SA302 for student loan component.

### Example 2 -- Voluntary overpayment direct to SLC

**Input line:**
`15.05.2026 ; STUDENT LOANS COMPANY ; DEBIT ; VOLUNTARY OVERPAYMENT ; -500.00 ; GBP`

**Reasoning:**
Matches "STUDENT LOANS COMPANY" (pattern 3.2). This is a voluntary overpayment made directly to SLC. Not deductible. Not part of SA. Reduce outstanding loan balance.

**Classification:** EXCLUDE -- voluntary student loan overpayment. Not tax-deductible.

### Example 3 -- Employment salary (PAYE deduction already made)

**Input line:**
`28.02.2026 ; DESIGN AGENCY LTD ; CREDIT ; FEB SALARY ; +2,400.00 ; GBP`

**Reasoning:**
Employment income. If the client is on Plan 2, the employer has already deducted student loan repayments from gross salary before paying the net amount. The £2,400 is post-deduction. This is NOT a student loan payment visible on the bank statement.

**Classification:** NOT a student loan payment. PAYE deduction already made at source.

### Example 4 -- SLC refund

**Input line:**
`20.06.2026 ; SLC REFUND ; CREDIT ; OVERPAYMENT REFUND ; +320.00 ; GBP`

**Reasoning:**
Matches "SLC REFUND" (pattern 3.4). Client overpaid and SLC is refunding. Not taxable income. Not a student loan payment.

**Classification:** EXCLUDE -- refund from SLC. Not taxable.

### Example 5 -- Payment on account (no student loan in it)

**Input line:**
`31.07.2026 ; HMRC ; DEBIT ; 2ND PAYMENT ON ACCOUNT ; -2,900.00 ; GBP`

**Reasoning:**
Matches "HMRC" (pattern 3.1). Second payment on account. Covers income tax and Class 4 NIC only. Student loan repayments are not part of payments on account: they are paid with the balancing payment on 31 January ([payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account)).

**Classification:** EXCLUDE -- SA payment on account. No student loan component. Look for the student loan in the 31 January payment and confirm it from the SA302.

### Example 6 -- Erudio legacy loan payment

**Input line:**
`01.04.2026 ; ERUDIO STUDENT LOANS ; DEBIT ; MONTHLY REPAYMENT ; -180.00 ; GBP`

**Reasoning:**
Matches "ERUDIO STUDENT LOANS" (pattern 3.2). This is a pre-1998 mortgage-style student loan managed by Erudio. Separate from the income-contingent plans. Monthly fixed repayments.

**Classification:** EXCLUDE -- legacy student loan repayment. Not tax-deductible.

## Section 4A -- Three-year worked example: Plan 2 + PGL SA filer

Hypothetical: a self-employed UK consultant with both a Plan 2 undergraduate loan and a Postgraduate Loan. Trading profits are the only relevant income (no employment, no unearned income above £2,000). Demonstrates how the SA deduction shifts as thresholds rise.

Assume trading profits of **£42,000** in each of the three years (held constant to isolate the threshold effect).

### Year 1 -- 2024-25

**Year 1 calculation table**

| Component | Threshold | Income above | Rate | Repayment |
| --- | --- | --- | --- | --- |
| Plan 2 | £27,295 | £14,705 | 9% | £1,323.45 |
| PGL | £21,000 | £21,000 | 6% | £1,260.00 |
| **Total via SA** |  |  |  | **£2,583.45** |

### Year 2 -- 2025-26

**Year 2 calculation table**

| Component | Threshold | Income above | Rate | Repayment |
| --- | --- | --- | --- | --- |
| Plan 2 | £28,470 | £13,530 | 9% | £1,217.70 |
| PGL | £21,000 | £21,000 | 6% | £1,260.00 |
| **Total via SA** |  |  |  | **£2,477.70** |

Change from 2024-25: **down £105.75** (Plan 2 threshold rose by £1,175 -> £1,175 x 9% = £105.75 less on Plan 2; PGL threshold unchanged).

### Year 3 -- 2026-27

Plan 2 threshold: **£29,385**. PGL threshold: **£21,000** (unchanged).

| Component | Threshold | Income above | Rate | Repayment |
| --- | --- | --- | --- | --- |
| Plan 2 | £29,385 | £12,615 | 9% | £1,135.35 |
| PGL | £21,000 | £21,000 | 6% | £1,260.00 |
| **Total via SA** |  |  |  | **£2,395.35** |

Change from 2025-26: **down £82.35** (Plan 2 threshold rose by £915 -> £915 x 9% = £82.35 less on Plan 2; PGL threshold unchanged).

**Key takeaway:** With constant profits of £42,000, the SA deduction shifts modestly year-on-year as Plan 2 thresholds rise. The PGL component is currently insensitive to threshold movement because PGL is frozen.

## Section 5 -- Tier 1 rules

### Rule 1 -- Single plan formula

- **Single plan formula** — Repayment = (total_relevant_income - threshold) x rate If result is negative, repayment = £0.

### Rule 2 -- What income counts

**Income counting table**

| Income Type | Included? |
| --- | --- |
| Self-employment profits (SA103) | Yes |
| Employment income (SA100) | Yes (but PAYE deductions offset) |
| Savings income | Yes, if total unearned > £2,000 |
| Dividend income | Yes, if total unearned > £2,000 |
| Rental income | Yes, if total unearned > £2,000 |
| Pension income | Yes |
| Capital gains | No |

### Rule 3 -- PAYE offset

- **PAYE offset formula** — Total repayment due = (total_relevant_income - threshold) x rate Less: PAYE deductions already made = Balance due via Self Assessment If PAYE exceeds total due, client claims refund from SLC (not HMRC).

### Rule 4 -- Multiple plans

- **Multiple plans general rule** — Plans 1, 2, 4 and 5 together give one 9% repayment above the lowest of their thresholds, not one charge per plan (Education (Student Loans) (Repayment) Regulations 2009, reg 29(5A); [GOV.UK: repaying your student loan](https://www.gov.uk/repaying-your-student-loan/print)). A Postgraduate Loan is a separate 6% charge above its own threshold, paid at the same time (reg 29(3A)).

**Combination table**

| Combination (2025-26 figures) | Calculation |
| --- | --- |
| Plan 2 + Postgraduate Loan | 9% above £28,470 AND 6% above £21,000 |
| Plan 1 + Postgraduate Loan | 9% above £26,065 AND 6% above £21,000 |
| Plan 1 + Plan 2 | One 9% charge above £26,065 (the lower threshold). SLC splits it between the loans |

- **Maximum combined rate** — 15% (9% + 6%) where the income is above both the undergraduate plan threshold and the Postgraduate Loan threshold.

### Rule 5 -- NOT tax-deductible

- **Not tax-deductible** — Student loan repayments are NOT business expenses. Cannot be deducted from trading profits.

### Rule 6 -- Payment schedule (via Self Assessment)

- **Payment schedule** — The whole student loan repayment for the year is due with the balancing payment on 31 January after the tax year. It is not included in payments on account, so it never goes into the 31 January or 31 July POA ([payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account): the balancing payment "will also include anything you owe for capital gains or student loans"). See uk-payments-on-account.

### Rule 7 -- Write-off periods

**Write-off periods table**

| Plan | Write-Off |
| --- | --- |
| Plan 1 (pre-Sep 2006) | Age 65 |
| Plan 1 (post-Sep 2006) | 25 years after first repayment |
| Plan 2 | 30 years |
| Plan 4 | 30 years (or age 65 for older borrowers) |
| Plan 5 | 40 years |
| Postgraduate Loan | 30 years |

### Rule 8 -- Plan 5 timing

- **Plan 5 timing** — Plan 5 collections began April 2026. For 2024-25 SA, no Plan 5 repayment is due. For 2025-26 SA, no Plan 5 repayment is due either (collections only begin in tax year 2026-27). From 2026-27 onwards, Plan 5 repayments apply at 9% above the published threshold.

### Rule 9 -- Unearned income rule

- **Unearned income rule** — Total unearned income (savings + dividends + rent) only counts if it exceeds £2,000/year.

### Rule 10 -- Threshold publication timing

- **Threshold publication timing** — HMRC publishes student loan thresholds annually, typically in the months preceding the start of the tax year (April). When a threshold for an upcoming year is not yet announced, flag for reviewer rather than estimating.

## Section 6 -- Tier 2 catalogue

### T2-1 -- Multiple plan interaction

- **T2-1** — Trigger: Client has more than one plan type simultaneously. Action: Confirm plan types with SLC before computing. Undergraduate plans (1, 2, 4, 5) share one 9% charge above the lowest threshold; a Postgraduate Loan adds 6% above its own threshold.

### T2-2 -- Overseas earnings

- **T2-2** — Trigger: Client lives outside UK for 3+ months. Action: SLC applies country-specific thresholds. Do not use UK thresholds. Escalate.

### T2-3 -- Approaching write-off date

- **T2-3** — Trigger: Client is within 2 years of write-off. Action: Advise against voluntary overpayments. Flag for reviewer to confirm exact write-off date with SLC.

### T2-4 -- Mid-year overseas move

- **T2-4** — Trigger: Client was UK-resident part of the year, then moved abroad. Action: UK SA covers UK-resident period; SLC overseas assessment covers the rest. Flag for reviewer.

### T2-5 -- Early repayment decision

- **T2-5** — Trigger: Client asks whether to make voluntary overpayments. Action: Flag for reviewer. Consider interest rates, write-off proximity, and opportunity cost.

### T2-6 -- Next year's threshold not yet published

- **T2-6** — Trigger: Computation requires a 2027-28 or later threshold that HMRC has not announced. Action: Use the latest published figure as a placeholder, clearly label "PROVISIONAL -- threshold pending HMRC announcement", and flag for reviewer to revisit once HMRC publishes.

## Section 7 -- Excel working paper template

```
UK STUDENT LOAN REPAYMENT -- WORKING PAPER
Client: [name]
Tax Year: [2024-25 / 2025-26 / 2026-27]
Prepared: [date]

INPUT DATA
  Plan type(s):                    [Plan 1/2/4/5/PGL]
  Total relevant income:           GBP [____]
  Employment income:               GBP [____]
  Self-employment profits:         GBP [____]
  Unearned income (if > £2,000):   GBP [____]
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

## Section 8 -- Bank statement reading guide

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
- Not visible on bank statement -- deducted from gross salary before net payment
- Visible on payslips and P60 only

**Key identification tips:**
1. For self-employed, student loan is almost always embedded in SA payments
2. The SA302 is the only reliable source for the student loan component
3. Direct SLC payments are voluntary overpayments
4. SLC refunds appear as credits from SLC

## Section 9 -- Onboarding fallback

If the client provides only a bank statement:

1. **Identify HMRC SA payments** -- these contain the student loan component (if any)
2. **Look for direct SLC payments** -- these are voluntary overpayments
3. **Flag:** "Student loan repayments for self-employed are collected through Self Assessment and combined with income tax and NIC in a single HMRC payment. The bank statement cannot isolate the student loan component. Please provide the SA302 tax calculation and confirm the plan type with SLC."

## Section 10 -- Reference material

### Thresholds and rates -- three-year view

**Thresholds and rates -- three-year view**

| Plan | Rate | 2024-25 | 2025-26 | 2026-27 |
| --- | --- | --- | --- | --- |
| Plan 1 | 9% | £24,990 | £26,065 | £26,900 |
| Plan 2 | 9% | £27,295 | £28,470 | £29,385 |
| Plan 4 | 9% | £31,395 | £32,745 | £33,795 |
| Plan 5 | 9% | £25,000 | £25,000 (frozen) | £25,000 |
| Postgraduate Loan | 6% | £21,000 | £21,000 | £21,000 |

### Test suite (2025-26 figures unless stated)

**Test 1:** Plan 2, self-employed, income £35,000. -> (£35,000 - £28,470) x 9% = £587.70.

**Test 2:** Plan 1, self-employed, income £60,000. -> (£60,000 - £26,065) x 9% = £3,054.15.

**Test 3:** Plan 4, self-employed, income £40,000. -> (£40,000 - £32,745) x 9% = £652.95.

**Test 4:** Plan 5 (2026-27), income £30,000. -> (£30,000 - £25,000) x 9% = £450.00.

**Test 5:** PGL only, income £28,000. -> (£28,000 - £21,000) x 6% = £420.00.

**Test 6:** Plan 2 + PGL, income £45,000 (2025-26). -> Plan 2 = £1,487.70, PGL = £1,440.00. Total = £2,927.70.

**Test 7:** Plan 2, income £25,000. -> Below threshold. Repayment = £0.

**Test 8:** Plan 1, employed £28,000 (PAYE deductions made) + self-employed £12,000. Total £40,000 (2025-26). -> Total = £1,254.15. Less PAYE £174.15. Balance via SA = £1,080.00.

**Test 9 (3-year sensitivity):** Plan 2 + PGL, profits £42,000 each year.
- 2024-25: Plan 2 £1,323.45 + PGL £1,260.00 = £2,583.45.
- 2025-26: Plan 2 £1,217.70 + PGL £1,260.00 = £2,477.70.
- 2026-27: Plan 2 £1,135.35 + PGL £1,260.00 = £2,395.35.

### Prohibitions

- NEVER guess the client's plan type
- NEVER include capital gains in the repayment income calculation
- NEVER treat student loan repayments as tax-deductible
- NEVER apply UK thresholds to overseas borrowers
- NEVER advise voluntary overpayments without checking write-off proximity
- NEVER charge 9% twice for two undergraduate plans -- one 9% charge applies above the lowest threshold; only a Postgraduate Loan adds a second (6%) charge
- NEVER assume PAYE deductions have been made -- verify with payslips or P60
- NEVER present figures without noting that SLC manages the loan balance and interest
- NEVER finalise a year's figures without confirming HMRC has published that year's thresholds
- NEVER include unearned income if total unearned is £2,000 or less

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `uk-student-loan-repayment` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/uk-student-loan-repayment. If neither is available, confirm every figure against the official source pages cited above before relying on it.
