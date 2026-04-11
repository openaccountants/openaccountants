---
name: uk-student-loan-repayment
description: >
  Use this skill whenever asked about UK Student Loan repayment for self-employed individuals. Trigger on phrases like "student loan repayment", "Plan 1", "Plan 2", "Plan 4", "Plan 5", "postgraduate loan", "student loan self-employed", "student loan Self Assessment", "SLC repayment", or any question about student loan obligations for a self-employed client. Also trigger when preparing an SA100 Self Assessment return where student loan repayment is relevant. This skill covers Plan 1, Plan 2, Plan 4, Plan 5, and Postgraduate Loan thresholds and rates, self-employed calculation via Self Assessment, multiple plan interaction, overseas earnings rules, write-off periods, and edge cases. ALWAYS read this skill before touching any UK student loan repayment work.
version: 1.0
jurisdiction: GB
tax_year: 2025-26
category: international
depends_on:
  - income-tax-workflow-base
---

# UK Student Loan Repayment -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | United Kingdom |
| Jurisdiction Code | GB |
| Primary Legislation | Education (Student Loans) Act 1998; Education (Repayment of Student Loans) Regulations 2009 |
| Supporting Legislation | Teaching and Higher Education Act 1998; Higher Education (Fee Limits and Student Support) (England) Regulations |
| Administering Body | Student Loans Company (SLC); collected by HMRC via Self Assessment |
| Rate Publisher | SLC / HMRC (publishes annual thresholds) |
| Contributor | Open Accountants |
| Validated By | Pending -- requires sign-off by a UK-qualified practitioner |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year Coverage | 2025-26 |
| Confidence Coverage | Tier 1: threshold lookup, rate calculation, Self Assessment computation. Tier 2: multiple plan interaction, overseas income assessment, early repayment decisions. Tier 3: loan cancellation disputes, SLC administrative errors, disability-related queries. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified practitioner must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any student loan repayment figure, you MUST know:

1. **Which plan type(s)?** [T1] -- Plan 1, Plan 2, Plan 4, Plan 5, Postgraduate Loan, or a combination?
2. **Tax year** [T1] -- thresholds change annually.
3. **Total taxable income** [T1] -- not just self-employment profits; includes employment income, unearned income above £2,000, and other taxable sources.
4. **Has PAYE already deducted student loan repayments?** [T1] -- employment income may have had repayments deducted at source.
5. **Is the client living outside the UK?** [T2] -- overseas income assessment applies.
6. **When did the client take out their loan?** [T2] -- determines plan type if client is unsure.

**If plan type is unknown, advise client to check with SLC or log in at repaymentplan.studentloanrepayment.co.uk. Do not guess the plan type.**

---

## Step 1: Determine Plan Type [T1]

**Legislation:** Education (Repayment of Student Loans) Regulations 2009

| Plan | Who | When Loan Taken |
|------|-----|-----------------|
| Plan 1 | English/Welsh students (pre-2012), NI students (all years) | Before 1 September 2012 (England/Wales) or any time (Northern Ireland) |
| Plan 2 | English/Welsh students (post-2012) | On or after 1 September 2012 |
| Plan 4 | Scottish students | All Scottish student loans (replaced Plan 1 for Scotland from April 2021) |
| Plan 5 | English students (post-2023) | On or after 1 August 2023 (undergraduate and Advanced Learner Loans) |
| Postgraduate Loan | Postgraduate Master's or Doctoral students (England/Wales) | From 2016-17 onward |

**A client can be on multiple plans simultaneously** (e.g., Plan 2 undergraduate + Postgraduate Loan).

---

## Step 2: Thresholds and Rates (2025-26) [T1]

**Source:** HMRC Student and Postgraduate Loan deduction tables 2025-26; SLC annual threshold confirmation

| Plan | Annual Threshold | Monthly Equivalent | Weekly Equivalent | Rate |
|------|-----------------|-------------------|-------------------|------|
| Plan 1 | £26,065 | £2,172 | £501 | 9% |
| Plan 2 | £28,470 | £2,372 | £547 | 9% |
| Plan 4 | £32,745 | £2,728 | £629 | 9% |
| Plan 5 | £25,000 | £2,083 | £480 | 9% |
| Postgraduate Loan | £21,000 | £1,750 | £403 | 6% |

### Key Notes on Thresholds

- **Plan 5 threshold** is fixed at £25,000 until April 2027, then rises annually with RPI.
- **Plan 2 threshold** increases to £29,385 from April 2026, then frozen until April 2030.
- **Postgraduate Loan threshold** has remained at £21,000 since inception.
- Plan 5 repayments begin from April 2026 at the earliest (even if the student left their course early).

---

## Step 3: Self-Employed Calculation via Self Assessment [T1]

**Legislation:** Education (Repayment of Student Loans) Regulations 2009, Reg 49-51

### What Income Counts?

For Self Assessment purposes, "income" for student loan repayment includes:

| Income Type | Included? |
|-------------|-----------|
| Self-employment profits (SA103) | Yes |
| Employment income (SA100) | Yes (but PAYE deductions may already apply) |
| Savings income | Yes, if total unearned income exceeds £2,000 |
| Dividend income | Yes, if total unearned income exceeds £2,000 |
| Rental income | Yes, if total unearned income exceeds £2,000 |
| Pension income | Yes |
| Capital gains | No |

### Formula (Single Plan)

```
Repayment = (total_relevant_income - threshold) x rate
```

If the result is negative, repayment = £0.

### PAYE Offset

If the client is also employed and student loan repayments have been deducted via PAYE, the Self Assessment calculation works as follows:

```
Total repayment due = (total_relevant_income - threshold) x rate
Less: PAYE deductions already made
= Balance due via Self Assessment
```

**If PAYE deductions exceed the total amount due, the client may be entitled to a refund from SLC (not HMRC).**

---

## Step 4: Multiple Plan Interaction [T2]

**A client on more than one plan repays on EACH plan separately, using each plan's own threshold.**

### Rules for Multiple Plans

| Combination | How It Works |
|------------|-------------|
| Plan 1 + Postgraduate Loan | 9% above £26,065 (Plan 1) AND 6% above £21,000 (PGL). Both apply simultaneously. |
| Plan 2 + Postgraduate Loan | 9% above £28,470 (Plan 2) AND 6% above £21,000 (PGL). Both apply simultaneously. |
| Plan 4 + Postgraduate Loan | 9% above £32,745 (Plan 4) AND 6% above £21,000 (PGL). Both apply simultaneously. |
| Plan 1 then Plan 2 (sequential) | Plan 1 is repaid first. Once Plan 1 is cleared, Plan 2 repayments begin. HMRC/SLC coordinate this. |

**Maximum combined rate: 9% + 6% = 15% of income above the lower threshold (where both thresholds are exceeded).**

**[T2] flag for reviewer when client has multiple plans. Confirm plan types with SLC before computing.**

---

## Step 5: Overseas Earnings [T2]

**Legislation:** Education (Repayment of Student Loans) Regulations 2009

| Requirement | Detail |
|-------------|--------|
| Notification | Must inform SLC if leaving the UK for 3+ months |
| Assessment | SLC conducts overseas income assessment based on country of residence |
| Thresholds | SLC applies country-specific thresholds (may be higher or lower than UK thresholds) |
| Currency | Income converted to GBP by SLC |
| Repayment method | Direct to SLC (not via HMRC Self Assessment) |
| Non-compliance | SLC can apply a fixed monthly repayment if income evidence is not provided |

**[T2] flag for reviewer whenever client has overseas earnings. Country-specific thresholds are set by SLC and vary significantly. Do not use UK thresholds for overseas borrowers.**

---

## Step 6: Write-Off Periods [T1]

**Legislation:** Education (Repayment of Student Loans) Regulations 2009

| Plan | Write-Off Rule |
|------|---------------|
| Plan 1 (loan before 1 Sep 2006) | Written off at age 65 |
| Plan 1 (loan on/after 1 Sep 2006) | Written off 25 years after first due repayment date |
| Plan 2 | Written off 30 years after first due repayment date |
| Plan 4 | Written off 30 years after first due repayment date (or age 65 for older borrowers) |
| Plan 5 | Written off 40 years after first due repayment date |
| Postgraduate Loan | Written off 30 years after first due repayment date |

**Write-off also occurs on death or permanent disability (confirmed by SLC).**

---

## Step 7: Payment Schedule for Self-Employed [T1]

Student loan repayments via Self Assessment follow the same payment schedule as income tax:

| Payment | Due Date |
|---------|----------|
| First payment on account | 31 January during tax year |
| Second payment on account | 31 July after tax year end |
| Balancing payment | 31 January following tax year end |

**Payments on account for student loans are calculated at 50% of the prior year's student loan repayment via Self Assessment.**

**Example for 2025-26 tax year:**
- 31 January 2026: First payment on account
- 31 July 2026: Second payment on account
- 31 January 2027: Balancing payment

---

## Step 8: Key Rules [T1]

1. **Student loan repayment is not a tax.** It is a separate obligation collected alongside tax through Self Assessment.
2. **Student loan repayments are NOT tax-deductible.** They cannot be deducted from trading profits or claimed as a business expense.
3. **Interest accrues on the outstanding loan balance** at rates set by SLC (linked to RPI and/or prevailing market rates depending on plan type). Interest is not the concern of the Self Assessment computation -- it is managed by SLC.
4. **Voluntary overpayments** can be made directly to SLC at any time to reduce the balance faster.
5. **If the client believes they have overpaid**, they must claim a refund from SLC, not from HMRC.
6. **The £2,000 unearned income rule**: unearned income (savings, dividends, rent) only counts toward the repayment calculation if total unearned income exceeds £2,000 per year.

---

## Step 9: Edge Case Registry

### EC1 -- Client unsure of plan type [T1]
**Situation:** Client does not know whether they are on Plan 1, 2, 4, or 5.
**Resolution:** Direct client to check with SLC online or call SLC directly. Do NOT guess based on graduation year alone -- Plan 4 was introduced retrospectively for Scottish borrowers. If preparing SA return, the plan type box must be completed accurately.

### EC2 -- Client on Plan 2 and Postgraduate Loan simultaneously [T1]
**Situation:** Client has both an undergraduate Plan 2 loan and a Postgraduate Loan. Total income £40,000.
**Resolution:** Plan 2 repayment = (£40,000 - £28,470) x 9% = £1,037.70. PGL repayment = (£40,000 - £21,000) x 6% = £1,140.00. Total student loan repayment via SA = £2,177.70 (less any PAYE deductions already made).

### EC3 -- Income below all thresholds [T1]
**Situation:** Client's total relevant income is £20,000. On Plan 2.
**Resolution:** £20,000 < £28,470 threshold. No repayment due. Enter zero on SA return for student loan section.

### EC4 -- Self-employed with employment income where PAYE already deducted [T1]
**Situation:** Client earns £30,000 from employment (Plan 1 PAYE deductions made) and £15,000 from self-employment. Total income £45,000.
**Resolution:** Total repayment = (£45,000 - £26,065) x 9% = £1,704.15. PAYE already deducted = (£30,000 - £26,065) x 9% = £354.15. Balance via SA = £1,704.15 - £354.15 = £1,350.00.

### EC5 -- Client moved overseas mid-year [T2]
**Situation:** Client was UK-resident for 6 months, then moved abroad.
**Resolution:** UK Self Assessment covers the UK-resident period. SLC overseas income assessment covers the overseas period. [T2] flag -- reviewer must confirm split-year treatment and ensure SLC has been notified.

### EC6 -- Client approaching write-off date [T2]
**Situation:** Client is on Plan 1 (post-2006) and is 2 years from the 25-year write-off.
**Resolution:** Advise client NOT to make voluntary overpayments if the remaining balance will be written off. [T2] flag -- reviewer should confirm exact write-off date with SLC and advise accordingly.

### EC7 -- Client has fully repaid but HMRC still showing liability [T1]
**Situation:** Client's loan was fully repaid during the year but Self Assessment is calculating a repayment.
**Resolution:** Client must obtain confirmation of full repayment from SLC and inform HMRC. SA return should reflect the correct position -- if the loan was repaid partway through the year, only income up to the repayment date counts. Contact SLC for a settlement figure.

### EC8 -- Plan 5 first year of repayment (2025-26) [T1]
**Situation:** Client started a Plan 5 course in September 2023 and left in June 2025. First repayment due April 2026.
**Resolution:** Plan 5 repayments cannot begin before April 2026 regardless of when the student left their course. For tax year 2025-26 (ending 5 April 2026), no Plan 5 repayment is due through Self Assessment. First SA repayment will appear in 2026-27.

---

## Step 10: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified practitioner must confirm before advising client.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified practitioner or SLC directly. Document gap.
```

---

## Step 11: Test Suite

### Test 1 -- Plan 2, self-employed only, standard income
**Input:** Tax year 2025-26. Plan 2. Self-employed only. Total relevant income £35,000.
**Expected output:** Repayment = (£35,000 - £28,470) x 9% = £587.70.

### Test 2 -- Plan 1, self-employed only, high income
**Input:** Tax year 2025-26. Plan 1. Self-employed only. Total relevant income £60,000.
**Expected output:** Repayment = (£60,000 - £26,065) x 9% = £3,054.15.

### Test 3 -- Plan 4 (Scotland), self-employed only
**Input:** Tax year 2025-26. Plan 4. Self-employed only. Total relevant income £40,000.
**Expected output:** Repayment = (£40,000 - £32,745) x 9% = £652.95.

### Test 4 -- Plan 5, income above threshold
**Input:** Tax year 2025-26. Plan 5. Self-employed only. Total relevant income £30,000.
**Expected output:** Repayment = (£30,000 - £25,000) x 9% = £450.00. NOTE: Plan 5 repayments do not begin until April 2026. For 2025-26 SA, this repayment would only apply if HMRC confirms Plan 5 collections began in-year.

### Test 5 -- Postgraduate Loan only
**Input:** Tax year 2025-26. Postgraduate Loan only. Self-employed. Total relevant income £28,000.
**Expected output:** Repayment = (£28,000 - £21,000) x 6% = £420.00.

### Test 6 -- Plan 2 + Postgraduate Loan (dual plan)
**Input:** Tax year 2025-26. Plan 2 + Postgraduate Loan. Self-employed. Total relevant income £45,000.
**Expected output:** Plan 2 = (£45,000 - £28,470) x 9% = £1,487.70. PGL = (£45,000 - £21,000) x 6% = £1,440.00. Total = £2,927.70.

### Test 7 -- Income below threshold
**Input:** Tax year 2025-26. Plan 2. Self-employed. Total relevant income £25,000.
**Expected output:** £25,000 < £28,470 threshold. Repayment = £0.

### Test 8 -- Mixed employment and self-employment with PAYE offset
**Input:** Tax year 2025-26. Plan 1. Employment income £28,000 (PAYE student loan deductions made). Self-employment profits £12,000. Total relevant income £40,000.
**Expected output:** Total repayment = (£40,000 - £26,065) x 9% = £1,254.15. PAYE already deducted = (£28,000 - £26,065) x 9% = £174.15. Balance via SA = £1,254.15 - £174.15 = £1,080.00.

---

## PROHIBITIONS

- NEVER guess the client's plan type -- always confirm with the client or direct them to SLC
- NEVER include capital gains in the student loan repayment income calculation
- NEVER treat student loan repayments as a tax-deductible expense
- NEVER apply UK thresholds to overseas borrowers -- SLC sets country-specific thresholds
- NEVER advise a client to make voluntary overpayments without checking proximity to write-off date
- NEVER combine Plan 1/2/4/5 thresholds -- each plan has its own separate threshold and calculation
- NEVER assume PAYE deductions have been made -- always verify with the client's payslips or P60
- NEVER present student loan figures without noting that SLC (not HMRC) manages the loan balance and interest
- NEVER compute Plan 5 repayments for tax years before 2026-27 without confirming SLC's collection start date
- NEVER include unearned income in the calculation if total unearned income is £2,000 or less

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
