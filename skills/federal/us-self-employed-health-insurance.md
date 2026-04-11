---
name: us-self-employed-health-insurance
description: Tier 2 content skill for computing the self-employed health insurance deduction under IRC §162(l) for US sole proprietors and single-member LLCs disregarded for federal tax purposes. Covers tax year 2025 rules including the 100% deduction for medical, dental, vision, and qualified long-term care premiums, the age-based long-term care premium limits, the net SE earnings limitation, the employer-sponsored plan eligibility bar, the Medicare premium eligibility rules (Parts A voluntary, B, D, Medigap), COBRA continuation premiums, ACA Marketplace interaction with the Premium Tax Credit, the month-by-month coverage calculation, and the Schedule 1 Line 17 reporting position. Consumes Schedule C net profit and SE tax from us-schedule-c-and-se-computation. Feeds QBI computation in us-qbi-deduction. MUST be loaded alongside us-tax-workflow-base v0.1 or later. Federal only. No state tax.
version: 0.2
---

# US Self-Employed Health Insurance Skill v0.2

## What this file is, and what it is not

**This file is a content skill that loads on top of `us-tax-workflow-base` v0.1.** It computes the self-employed health insurance deduction under IRC §162(l) for sole proprietors and single-member LLCs for tax year 2025. It does not classify transactions (that is `us-sole-prop-bookkeeping`), compute Schedule C net profit or SE tax (that is `us-schedule-c-and-se-computation`), or compute the QBI deduction (that is `us-qbi-deduction`, which consumes this skill's output).

**Where this skill fits in the pipeline:**

```
Bank statement / source data
        ↓
us-sole-prop-bookkeeping (classifies every transaction into a Schedule C line)
        ↓
us-schedule-c-and-se-computation (aggregates, computes net profit, computes SE tax)
        ↓
us-self-employed-health-insurance (THIS SKILL — computes SE health insurance deduction)
  + us-self-employed-retirement (companion — computes retirement contribution deduction)
        ↓
us-qbi-deduction (QBI deduction, adjusted for SE health insurance and retirement)
        ↓
us-quarterly-estimated-tax (safe harbor for following year)
```

**Tax year coverage.** This skill is current for **tax year 2025** as of its currency date (April 2026). The §162(l) rules are largely unchanged from prior years. The age-based long-term care premium limits are from Rev. Proc. 2024-40.

**The reviewer is the customer of this output.** The skill produces a SE health insurance deduction worksheet and a brief that the reviewing EA or CPA can audit and sign off on.

---

## Section 1 — Scope statement

This skill covers, for tax year 2025:

- **The §162(l) deduction** — 100% of eligible health insurance premiums for self-employed individuals
- **Eligible premium types** — medical, dental, vision, qualified long-term care (with age-based limits)
- **Medicare premiums** — Parts A (voluntary only), B, D, Medigap supplemental
- **COBRA continuation premiums** — eligibility under §162(l)
- **The net SE earnings limitation** — deduction cannot exceed net SE earnings from the business
- **The employer-sponsored plan eligibility bar** — month-by-month determination
- **ACA Marketplace interaction** — §162(l) vs. Premium Tax Credit (PTC), cannot double-dip
- **Self-only vs. family coverage** — allocating premiums when coverage includes family members
- **Month-by-month coverage calculation** — when coverage type, eligibility, or premiums change mid-year
- **The reporting position** — Schedule 1, Line 17 (adjustment to income, NOT on Schedule C)
- **Long-term care premium limits** — age-based caps under §213(d)(10)

This skill does NOT cover:

- The Premium Tax Credit (PTC) computation on Form 8962 — flagged for reviewer
- Health Savings Account (HSA) contributions and deductions — separate skill
- Marketplace enrollment or qualification — out of scope
- COBRA administration — out of scope
- Long-term care policy qualification under §7702B — flagged for reviewer
- Medical expense deduction on Schedule A (§213(a) — the 7.5% AGI floor itemized deduction) — separate from §162(l)
- State health insurance mandates or credits (e.g., California §3853) — out of scope for this federal skill

---

## Section 2 — Year coverage and currency

**Tax year covered:** 2025 (returns due April 15, 2026, or October 15, 2026 with extension).

**Currency date:** April 2026.

**Legislation reflected:**
- Internal Revenue Code §162(l) as in force for tax year 2025
- IRC §213(d)(10) — long-term care premium limits (inflation-adjusted)
- Affordable Care Act provisions as in force for 2025 (§36B Premium Tax Credit)
- Rev. Proc. 2024-40 — 2025 inflation adjustments (long-term care premium limits)
- IRS Publication 535 (2025) — Business expenses (SE health insurance chapter)
- Form 1040 Schedule 1 Instructions (2025) — Line 17
- IRS Publication 974 (2025) — Premium Tax Credit

**Currency limitations:**
- OBBBA (P.L. 119-21) did NOT change §162(l) or the self-employed health insurance deduction mechanics. The rules are unchanged from prior years.
- The Inflation Reduction Act (IRA 2022) extended enhanced ACA Premium Tax Credits through 2025. Verify whether these were further extended beyond 2025 for future-year skills.

---

## Section 3 — Year-specific figures table for tax year 2025

### Long-term care premium limits (age-based, §213(d)(10))

| Age at end of tax year | Maximum eligible LTC premium (2025) | Primary source |
|---|---|---|
| 40 or under | $480 | Rev. Proc. 2024-40; IRC §213(d)(10) |
| 41-50 | $900 | Rev. Proc. 2024-40 |
| 51-60 | $1,790 | Rev. Proc. 2024-40 |
| 61-70 | $4,770 | Rev. Proc. 2024-40 |
| Over 70 | $5,960 | Rev. Proc. 2024-40 |

### Other figures

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| §162(l) deduction percentage | 100% of eligible premiums | IRC §162(l)(1)(A) |
| Net SE earnings limitation | Deduction ≤ net SE earnings from the trade or business | IRC §162(l)(2)(A) |
| Schedule 1 reporting line | Line 17 | Form 1040 Schedule 1 Instructions (2025) |
| ACA enhanced PTC availability | Yes (through 2025, per Inflation Reduction Act) | §36B as amended by IRA 2022 |

---

## Section 4 — Primary source library

### Statute (Internal Revenue Code, Title 26 USC)

- **IRC §162(l)** — Special rules for health insurance costs of self-employed individuals
- **IRC §162(l)(1)(A)** — Allowance of deduction: 100% of amounts paid for insurance for the taxpayer, spouse, and dependents
- **IRC §162(l)(2)(A)** — Limitation: deduction cannot exceed taxpayer's earned income from the trade or business for which the insurance plan is established
- **IRC §162(l)(2)(B)** — Coordination with employer-sponsored plans: no deduction for any month the taxpayer is eligible for employer-subsidized health coverage
- **IRC §162(l)(4)** — S corporation shareholders: 2%+ shareholders treated as self-employed for this purpose (out of scope)
- **IRC §162(l)(5)** — Long-term care insurance included, subject to §213(d)(10) limits
- **IRC §213(d)(1)** — Definition of medical care (for eligible premium types)
- **IRC §213(d)(10)** — Limitation on long-term care premiums treated as medical care (age-based table)
- **IRC §36B** — Premium Tax Credit (refundable, for Marketplace coverage)
- **IRC §7702B** — Treatment of qualified long-term care insurance

### Treasury Regulations

- **Treas. Reg. §1.162(l)-1** — (reserved; limited regulatory guidance — rely on statute and IRS publications)

### IRS Guidance and Publications

- **Rev. Proc. 2024-40** — 2025 inflation adjustments (LTC premium limits)
- **IRS Publication 535 (2025)** — Business Expenses, Chapter 6 (Insurance)
- **IRS Publication 974 (2025)** — Premium Tax Credit
- **Form 7206** — Self-Employed Health Insurance Deduction (introduced 2023, used for 2025)
- **Form 7206 Instructions (2025)** — Computation of SE health insurance deduction
- **Form 8962** — Premium Tax Credit (PTC)

---

## Section 5 — Eligibility rules

### Who qualifies for the §162(l) deduction

The deduction is available to:

1. **Sole proprietors** who report business income on Schedule C
2. **Single-member LLC owners** (disregarded entity — Schedule C filer)
3. **Partners** in a partnership (out of scope for this skill)
4. **S corporation 2%+ shareholders** (out of scope for this skill)

The taxpayer must have **net self-employment earnings** from the business for which the health insurance plan is established. The business must be the source of the insurance — the health insurance must be established under the business (or in the taxpayer's name as a self-employed individual).

### The employer-sponsored plan eligibility bar

Under IRC §162(l)(2)(B), the §162(l) deduction is NOT available for any month in which the taxpayer was **eligible to participate** in a subsidized health plan maintained by:

- The taxpayer's own employer (if the taxpayer also has W-2 employment)
- The taxpayer's spouse's employer
- The taxpayer's parent's employer (if the taxpayer is under age 27)

**"Eligible to participate" means eligible, not actually enrolled.** If the taxpayer's spouse works for an employer that offers family health coverage and the taxpayer is eligible for that coverage, the taxpayer CANNOT take the §162(l) deduction — even if the taxpayer declined the employer coverage and purchased individual insurance instead.

**Month-by-month test.** Eligibility is tested each month. If the spouse started a new job in July 2025 that offers health coverage with a 60-day waiting period, the taxpayer is ineligible for §162(l) starting the month the employer coverage becomes available (approximately September 2025), not the month the spouse started.

### What "subsidized" means

The employer plan must be subsidized — meaning the employer pays at least some portion of the premium. An employer plan where the employee pays 100% of the cost (no employer contribution) does NOT bar the §162(l) deduction. However, this is rare; most employer plans are at least partially subsidized.

---

## Section 6 — Eligible premium types

### Medical, dental, and vision insurance

All premiums for medical, dental, and vision insurance qualify for the §162(l) deduction. This includes:

- Individual health insurance purchased through the ACA Marketplace (Healthcare.gov or state exchange)
- Individual health insurance purchased off-exchange (directly from an insurer)
- Dental insurance premiums
- Vision insurance premiums
- Short-term health insurance premiums (qualify as medical care under §213(d))

### Qualified long-term care insurance

Long-term care insurance premiums are eligible but subject to the age-based limits under §213(d)(10). Only the portion of premiums up to the age-based limit is treated as medical care for §162(l) purposes.

**Example:** A 55-year-old sole prop pays $3,000/year in long-term care premiums. The 2025 limit for age 51-60 is $1,790. Only $1,790 qualifies for the §162(l) deduction.

### Medicare premiums

The following Medicare premiums qualify for the §162(l) deduction:

| Medicare component | Eligible? | Notes |
|---|---|---|
| Part A (hospital) — voluntary premiums | YES | Only if the taxpayer pays voluntary Part A premiums (most people get Part A premium-free) |
| Part A — premium-free | N/A | No premium paid, nothing to deduct |
| Part B (medical) | YES | The standard monthly premium ($185.00/month for 2025 at standard, higher with IRMAA) |
| Part B — IRMAA surcharge | YES | The income-related monthly adjustment amount is a premium and qualifies |
| Part D (prescription drug) | YES | Monthly premium for the Part D plan chosen |
| Part D — IRMAA surcharge | YES | Same as Part B IRMAA |
| Medigap (Medicare Supplement) | YES | Premiums for Plans A through N |
| Medicare Advantage (Part C) | YES | Premiums for Medicare Advantage plans (many have $0 premium) |

**Key point:** A sole prop who is on Medicare can deduct all Medicare premiums (B, D, Medigap) under §162(l) as long as they are not eligible for employer-sponsored coverage for those months and have net SE earnings.

### COBRA continuation premiums

COBRA premiums paid by the self-employed individual qualify for §162(l). COBRA is typically expensive (102% of the full group rate), making this deduction particularly valuable during transition periods.

### Premiums that do NOT qualify

- Workers' compensation insurance (this is a business expense on Schedule C, not §162(l))
- Disability insurance (not medical insurance under §213(d))
- Life insurance premiums
- Premiums for policies that pay a fixed daily amount for hospitalization (indemnity plans) — these may not qualify as medical care
- Premiums paid with pre-tax dollars from an employer plan (already excluded from income)

---

## Section 7 — The net SE earnings limitation

### The rule

Under IRC §162(l)(2)(A), the §162(l) deduction cannot exceed the taxpayer's **earned income** derived from the trade or business with respect to which the health insurance plan is established.

For sole props: earned income = net SE earnings = Schedule C net profit (Line 31). The deduction is capped at Schedule C net profit.

### What counts as "the trade or business"

The health insurance must be established in connection with the taxpayer's trade or business. For a sole prop with one Schedule C, this is straightforward. For a sole prop with multiple Schedule Cs, the insurance must be associated with a specific business, and the net SE earnings limitation applies to THAT business's profit.

**Conservative default:** If a sole prop has multiple Schedule Cs and the insurance is not clearly tied to one business, apply the limitation against the lowest-profit business (conservative). Flag for reviewer.

### Interaction with the SE tax deduction

The §162(l) deduction does NOT reduce net SE earnings for purposes of this limitation. The limitation is based on Schedule C net profit, not on net SE earnings after the SE tax deduction. This prevents a circular trap.

### When net SE earnings are insufficient

If the §162(l) deduction exceeds net SE earnings, the deduction is limited to net SE earnings. The excess premiums are NOT carried forward (unlike home office expenses). They are simply lost as a §162(l) deduction.

However, the excess premiums may be deductible as a medical expense on Schedule A (subject to the 7.5% AGI floor) if the taxpayer itemizes. The skill flags this alternative but does not compute the Schedule A medical expense deduction.

---

## Section 8 — The ACA Premium Tax Credit interaction

### The core conflict

For ACA Marketplace coverage, the taxpayer may be eligible for both:
1. The §162(l) self-employed health insurance deduction, AND
2. The §36B Premium Tax Credit (PTC)

**You cannot double-dip.** For any given dollar of premium, the taxpayer can claim EITHER the §162(l) deduction OR the PTC, but not both. The IRS enforces this through the iterative computation on Form 7206 and Form 8962.

### How the interaction works

The §162(l) deduction reduces AGI. Lower AGI can increase PTC eligibility (since PTC is based on household income as a percentage of the Federal Poverty Level). But if PTC increases, the net premium (premium minus PTC) decreases, which reduces the §162(l) deduction. This creates a circular computation.

**The IRS solution:** An iterative calculation described in IRS Publication 974, Chapter 9 ("Self-Employed Individuals"). The taxpayer must:

1. Estimate the §162(l) deduction and PTC simultaneously
2. Iterate until the figures converge
3. Report the final amounts on Form 7206 (SE health insurance deduction) and Form 8962 (PTC)

### Practical approach for the skill

The skill uses the IRS-prescribed iterative method:

```
Step 1: Compute provisional AGI WITHOUT the §162(l) deduction
Step 2: Compute the PTC based on provisional AGI
Step 3: Compute the §162(l) deduction = total premium − PTC (from Step 2)
Step 4: Compute revised AGI = provisional AGI − §162(l) deduction (from Step 3)
Step 5: Recompute PTC based on revised AGI (from Step 4)
Step 6: Recompute §162(l) deduction = total premium − PTC (from Step 5)
Step 7: Repeat Steps 4-6 until AGI, PTC, and §162(l) deduction converge (stabilize within $1)
```

**Conservative default:** If the iterative computation is complex or the inputs are incomplete, the skill defaults to §162(l) deduction ONLY (no PTC) and flags for reviewer to determine if PTC is more favorable.

### When PTC is better than §162(l)

PTC is a refundable credit (reduces tax dollar-for-dollar, and can result in a refund). §162(l) is a deduction (reduces taxable income, value depends on marginal tax rate). For lower-income self-employed individuals, PTC may be worth more than §162(l). The skill flags this comparison for reviewer when the taxpayer's marginal rate is below 22%.

### Advance PTC reconciliation

If the taxpayer received advance PTC payments (APTC) through the Marketplace, Form 8962 must be filed to reconcile. The §162(l) deduction affects this reconciliation. If the taxpayer took too much APTC (based on lower projected income), they may owe money back. The skill flags APTC reconciliation but does not compute it.

---

## Section 9 — Month-by-month computation

### When month-by-month is required

The deduction must be computed month-by-month when:

1. Coverage type changed mid-year (e.g., switched from individual to family plan)
2. Premium amount changed mid-year
3. Employer-plan eligibility changed mid-year (e.g., spouse got a new job with coverage)
4. The taxpayer started or stopped self-employment mid-year
5. PTC amounts varied by month

### The computation

For each month, determine:
- Was the taxpayer self-employed?
- Was the taxpayer eligible for an employer-sponsored plan?
- What was the premium paid?
- What PTC was received (if any)?

Sum the eligible months to get the annual deduction.

**Form 7206 handles this.** Form 7206 (Self-Employed Health Insurance Deduction), introduced for tax year 2023, structures the month-by-month computation. The skill produces the Form 7206 worksheet.

### Coverage for the taxpayer, spouse, and dependents

The §162(l) deduction covers premiums for:
- The taxpayer
- The taxpayer's spouse
- The taxpayer's dependents (children under 27 at end of tax year, regardless of dependency status for §162(l) purposes per §162(l)(1)(D))

**The "child under 27" rule:** For §162(l) purposes only, a child of the taxpayer who has not attained age 27 as of the end of the tax year is treated as a dependent, even if the child is not actually a dependent for other tax purposes (e.g., the child has their own income and files their own return). This is broader than the general dependency rules.

---

## Section 10 — Reporting position

### Where the deduction appears

The §162(l) deduction is reported on **Schedule 1 (Form 1040), Line 17** — "Self-employed health insurance deduction."

This is an **adjustment to gross income** (above-the-line deduction). It reduces AGI.

### Where the deduction does NOT appear

- **NOT on Schedule C.** Health insurance premiums for the self-employed individual are not a business expense on Schedule C. They are a personal deduction that happens to be available because of self-employment status. (Premiums for employees' health insurance ARE on Schedule C Line 14, but that is a different deduction.)
- **NOT on Schedule A.** The §162(l) deduction is separate from the itemized medical expense deduction. Premiums deducted under §162(l) cannot also be deducted on Schedule A.

### Form 7206

Starting with tax year 2023, the IRS requires Form 7206 to compute the self-employed health insurance deduction. The form walks through:
- Line 1: Premiums paid for medical and dental insurance
- Lines 2-11: Month-by-month eligibility (employer plan test)
- Lines 12-17: Long-term care premiums (age-based limit)
- Lines 18-20: Net SE earnings limitation
- Line 21: Total SE health insurance deduction → flows to Schedule 1, Line 17

---

## Section 11 — Interaction with QBI

The §162(l) deduction reduces QBI. Under IRC §199A(c)(1), QBI is net income from the qualified trade or business, reduced by deductions attributable to that trade or business. The SE health insurance deduction is attributable to the trade or business under §62(a)(1).

```
QBI = Schedule C net profit
    − Deductible half of SE tax
    − SE health insurance deduction (THIS SKILL's output)
    − Retirement contributions
```

This means a larger SE health insurance deduction reduces QBI, which reduces the QBI deduction (20% of QBI). The net effect is still favorable — the §162(l) deduction saves more tax than the reduced QBI deduction costs.

---

## Section 12 — Conservative defaults table

| Ambiguity | Conservative default |
|---|---|
| Whether taxpayer is eligible for employer-sponsored plan | Assume eligible (no §162(l) deduction); ask for clarification |
| Whether spouse's employer offers coverage | Assume yes (bars §162(l)); ask for clarification |
| Premium amount not documented | $0 deduction; ask for Form 1095-A/B/C or premium statements |
| Whether insurance is medical vs. disability or other | Assume non-qualifying unless premium statement confirms medical/dental/vision/LTC |
| Long-term care premium exceeds age-based limit | Cap at the age-based limit; deduct only the eligible portion |
| PTC vs. §162(l) choice unclear | Default to §162(l) only (more common for self-employed); flag PTC alternative for reviewer |
| APTC received but amount unknown | Flag for reviewer — Form 8962 reconciliation required |
| Coverage months unclear (mid-year change) | Deduct only for months with documented coverage and confirmed eligibility |
| Multiple Schedule Cs — which business supports the insurance? | Attribute to the business with the highest net profit (maximizes the net SE earnings limitation); flag for reviewer |
| Medicare premium amounts not stated | Use standard Part B premium ($185.00/month for 2025); flag if IRMAA may apply |

---

## Section 13 — Topical refusal catalogue

**R-SEHI-PTC — Premium Tax Credit computation.**
Trigger: The taxpayer asks for the full PTC computation on Form 8962.
Output: "The Premium Tax Credit computation requires household income as a percentage of the Federal Poverty Level, benchmark silver plan premiums, and APTC reconciliation. This skill handles the §162(l) deduction side of the interaction but does not fully compute Form 8962. Please consult a CPA or Enrolled Agent for PTC optimization."

**R-SEHI-HSA — Health Savings Account.**
Trigger: The taxpayer asks about HSA contributions or deductions.
Output: "HSA contributions for self-employed individuals are deductible on Schedule 1 Line 13 (separate from the §162(l) deduction on Line 17). HSA rules (§223) including HDHP requirements, contribution limits, and the last-month rule are outside the scope of this skill. The 2025 HSA contribution limits are $4,300 (self-only) and $8,550 (family). Please consult a CPA or financial advisor."

**R-SEHI-SCHEDULE-A — Medical expense deduction on Schedule A.**
Trigger: The taxpayer's §162(l) deduction is limited by net SE earnings, and the excess premiums could be deductible on Schedule A.
Output: "Premiums not deductible under §162(l) may be deductible as medical expenses on Schedule A, subject to the 7.5% AGI floor. This skill does not compute Schedule A medical expenses. Please consult a CPA or Enrolled Agent."

**R-SEHI-COBRA-ADMIN — COBRA eligibility and administration.**
Trigger: Questions about COBRA election periods, qualifying events, or administrative requirements.
Output: "COBRA administration (qualifying events, election periods, notification requirements) is an employment law question, not a tax computation. The skill confirms that COBRA premiums paid by the self-employed individual qualify for §162(l) if other eligibility requirements are met. For COBRA administration, consult an employment attorney or benefits administrator."

**R-SEHI-LTC-QUALIFIED — Whether a long-term care policy qualifies under §7702B.**
Trigger: The taxpayer has a long-term care policy and wants to confirm it is a qualified policy.
Output: "Whether a long-term care policy is a qualified long-term care insurance contract under §7702B depends on the policy terms (it must not pay for expenses reimbursable by Medicare, must be guaranteed renewable, etc.). This skill assumes the policy is qualified if the insurer represents it as such. For policy qualification, consult the insurer or an insurance professional."

---

## Section 14 — Reviewer attention thresholds

| Threshold | Trigger | Rationale |
|---|---|---|
| §162(l) deduction > $20,000 | Always flag | Large deduction; verify premium documentation |
| §162(l) deduction limited by net SE earnings | Always flag | Taxpayer losing part of the deduction; consider Schedule A alternative |
| PTC interaction present | Always flag | Iterative computation required; verify Form 8962 reconciliation |
| APTC received | Always flag | Reconciliation on Form 8962 may result in tax owed |
| Employer eligibility bar invoked for some months | Always flag | Month-by-month computation needed; verify eligibility dates |
| Long-term care premiums claimed | Always flag | Age-based limit applies; verify policy is qualified under §7702B |
| Medicare premiums claimed | Always flag | Verify Part B amount, IRMAA status, and voluntary Part A status |
| Spouse's employer offers coverage | Always flag | This bars §162(l) for months of eligibility |
| Coverage includes child approaching age 27 | Always flag | Age 27 rule is tested at end of tax year — verify child's age |

---

## Section 15 — Worked examples

### Example 1 — Basic SE health insurance deduction

**Taxpayer:** Maria Hernandez, single, age 34, freelance UX designer, Schedule C net profit $62,644. Individual health insurance purchased off-exchange: $700/month = $8,400/year. No employer plan eligibility. No PTC.

```
Annual premium:           $8,400
Employer plan test:       Not eligible for any employer plan (all 12 months)
Net SE earnings limit:    $62,644 (Schedule C net profit)
§162(l) deduction:        $8,400 (within limit)

Reported on: Schedule 1, Line 17 = $8,400
Form 7206: completed, 12 months eligible
```

### Example 2 — Deduction limited by net SE earnings

**Taxpayer:** Alex Rivera, single, age 28, freelance graphic designer, Schedule C net profit $12,000. ACA Marketplace plan: $450/month = $5,400/year. No PTC claimed.

```
Annual premium:           $5,400
Net SE earnings limit:    $12,000
§162(l) deduction:        $5,400 (within limit)

If Schedule C net profit were only $4,000:
  §162(l) deduction:      $4,000 (limited by net SE earnings)
  Excess $1,400:          Not deductible under §162(l)
                          May be deductible on Schedule A if itemizing (7.5% AGI floor)
```

### Example 3 — Mid-year employer plan eligibility

**Taxpayer:** Sarah Kim, MFJ, age 45, freelance financial advisor. Spouse started W-2 job on July 1, 2025 with employer-sponsored family health plan (coverage effective August 1, 2025).

```
January-July (7 months):  Not eligible for employer plan → §162(l) eligible
August-December (5 months): Eligible for spouse's employer plan → §162(l) BARRED

Individual plan premium: $900/month
Eligible months: 7
§162(l) deduction: 7 × $900 = $6,300

August-December premiums ($4,500): NOT deductible under §162(l)
  (Sarah may want to drop individual plan and enroll in spouse's employer plan)
```

### Example 4 — Medicare premiums

**Taxpayer:** Robert Garcia, single, age 68, freelance consultant, Schedule C net profit $95,000. Medicare Part B: $185.00/month. Medigap Plan F: $220/month. Part D: $35/month. No employer plan eligibility.

```
Part B:     12 × $185.00 = $2,220
Medigap:    12 × $220.00 = $2,640
Part D:     12 × $35.00  = $420
                          -------
Total:                     $5,280

Net SE earnings limit: $95,000
§162(l) deduction: $5,280

Reported on: Schedule 1, Line 17 = $5,280
```

### Example 5 — Long-term care with age-based limit

**Taxpayer:** Lisa Park, MFJ, age 61, Schedule C net profit $180,000. Medical insurance: $12,000/year. Long-term care premium: $6,000/year.

```
Medical insurance:     $12,000 (fully eligible)
LTC premium paid:      $6,000
LTC age-based limit:   $4,770 (age 61-70)
LTC eligible:          $4,770

Total §162(l) deduction: $12,000 + $4,770 = $16,770
Excess LTC ($1,230):     Not deductible under §162(l); may qualify on Schedule A
```

---

## Section 16 — Edge cases

1. **Net SE earnings are zero or negative.** No §162(l) deduction. Premiums may be deductible on Schedule A as medical expenses (7.5% AGI floor). The taxpayer gets no above-the-line benefit.

2. **Taxpayer has both SE income and W-2 income with employer health plan.** The employer plan eligibility bars §162(l) for months the taxpayer is eligible. If the taxpayer is eligible for the employer plan all year, §162(l) = $0, even if the taxpayer did not enroll.

3. **COBRA premiums after leaving W-2 employment.** COBRA premiums qualify for §162(l) IF the taxpayer is now self-employed and not eligible for another employer plan. The months on COBRA count as eligible months for §162(l).

4. **ACA Marketplace with APTC, switching to §162(l) mid-year.** If the taxpayer received APTC for part of the year and wants to claim §162(l) for the rest, the iterative computation applies to the §162(l) months, and Form 8962 reconciliation applies to the APTC months. Flag for reviewer.

5. **Spouse is self-employed too.** Each spouse can take their own §162(l) deduction from their own Schedule C net profit for premiums on their own coverage. If both are covered under a single family policy, the premiums must be allocated between them. Allocation method: proportional to each spouse's coverage cost, or equally if costs cannot be separated.

6. **Child turns 27 during the tax year.** For §162(l), the child is treated as a dependent if they have not attained age 27 as of the END of the tax year (December 31, 2025). If the child turns 27 on or before December 31, 2025, their coverage premiums do not qualify for the full year. If the child turns 27 after December 31 (i.e., in 2026), their 2025 premiums qualify for all 12 months.

7. **Part-year self-employment.** If the taxpayer was self-employed only for part of the year, the net SE earnings limitation applies to actual net SE earnings (not annualized). Only months of self-employment with simultaneous health insurance qualify.

8. **Insurance purchased in spouse's name.** The policy does not have to be in the sole proprietor's name. Insurance purchased in the spouse's name qualifies for §162(l) if it covers the self-employed taxpayer and the business effectively establishes or pays for the coverage.

9. **Health insurance premiums paid through the business bank account vs. personal.** The source of payment does not matter for §162(l) eligibility — the deduction is the same whether paid from a business or personal account. However, the premiums should NOT be deducted on Schedule C (they are Schedule 1 Line 17 items).

10. **Taxpayer eligible for employer plan but the plan is not subsidized.** If the employer plan requires the employee to pay 100% of the premium (employer contributes $0), the employer plan eligibility bar does NOT apply. The taxpayer can claim §162(l). This is uncommon but possible.

---

## Section 17 — Test suite

### Test 1 — Full year, straightforward
**Input:** Schedule C net profit $80,000; individual health insurance $600/month ($7,200/year); no employer plan eligibility; no PTC.
**Expected:** §162(l) deduction = $7,200. Schedule 1 Line 17 = $7,200.

### Test 2 — Limited by net SE earnings
**Input:** Schedule C net profit $5,000; individual health insurance $500/month ($6,000/year); no employer plan eligibility.
**Expected:** §162(l) deduction = $5,000 (limited by net SE earnings). Excess $1,000 not deductible under §162(l); flag Schedule A alternative.

### Test 3 — Mid-year employer plan bar
**Input:** Schedule C net profit $60,000; health insurance $800/month; eligible for spouse's employer plan July-December (6 months).
**Expected:** Eligible months = January-June (6 months). §162(l) deduction = 6 × $800 = $4,800.

### Test 4 — Medicare premiums
**Input:** Schedule C net profit $50,000; Medicare Part B $185/month; Medigap $150/month; Part D $40/month; no employer plan.
**Expected:** Total premiums = 12 × ($185 + $150 + $40) = $4,500. §162(l) deduction = $4,500.

### Test 5 — Long-term care with age limit
**Input:** Schedule C net profit $100,000; medical insurance $10,000/year; LTC premium $5,000/year; age 55; no employer plan.
**Expected:** LTC limit (age 51-60) = $1,790. Eligible LTC = $1,790. Total §162(l) = $10,000 + $1,790 = $11,790.

### Test 6 — Net SE earnings = $0
**Input:** Schedule C net profit $0 (break-even year); health insurance $500/month ($6,000/year).
**Expected:** §162(l) deduction = $0 (limited by net SE earnings). Entire $6,000 not deductible under §162(l). Flag Schedule A.

### Test 7 — Family coverage with child under 27
**Input:** Schedule C net profit $120,000; family health insurance (self + spouse + 25-year-old child) $1,800/month ($21,600/year); no employer plan.
**Expected:** Child is under 27 at end of year → qualifies. §162(l) deduction = $21,600 (within net SE earnings limit).

---

## Section 18 — PROHIBITIONS

1. **NEVER deduct SE health insurance premiums on Schedule C.** The deduction is on Schedule 1, Line 17. Putting it on Schedule C would double-count it (once as a business expense, once as an above-the-line deduction) and would incorrectly reduce net SE earnings for SE tax purposes.

2. **NEVER allow the §162(l) deduction for any month the taxpayer was eligible for an employer-sponsored plan.** Eligible means eligible, not enrolled. This includes the spouse's employer plan.

3. **NEVER allow both §162(l) and PTC on the same dollar of premium.** The deduction and the credit are coordinated — the §162(l) deduction applies only to the net premium after PTC.

4. **NEVER exceed the net SE earnings limitation.** The §162(l) deduction cannot exceed Schedule C net profit from the business with respect to which the plan is established. Excess premiums are lost as §162(l) deductions.

5. **NEVER deduct long-term care premiums in excess of the age-based limit.** Only the portion up to the §213(d)(10) limit qualifies for §162(l).

6. **NEVER carry forward excess §162(l) deductions.** Unlike the home office deduction, there is no carryforward for §162(l). Excess premiums are lost for §162(l) purposes (though they may be deductible on Schedule A).

7. **NEVER treat disability insurance premiums as eligible for §162(l).** Disability insurance is not medical care under §213(d).

8. **NEVER ignore the month-by-month computation when eligibility changed mid-year.** A full-year computation when the taxpayer was only eligible for part of the year will overstate the deduction.

9. **NEVER treat the §162(l) deduction as reducing net SE earnings for SE tax purposes.** The SE health insurance deduction is an income tax adjustment, not a SE tax adjustment. Schedule SE uses Schedule C net profit, not AGI.

10. **NEVER skip Form 7206.** Starting with tax year 2023, Form 7206 is required to compute and report the §162(l) deduction. The deduction flows from Form 7206 to Schedule 1 Line 17.

---

## Section 19 — Cross-skill references

| Upstream skill | Data consumed |
|---|---|
| `us-schedule-c-and-se-computation` | Schedule C net profit (Line 31), for net SE earnings limitation |

| Downstream skill | Data provided |
|---|---|
| `us-qbi-deduction` | SE health insurance deduction amount (reduces QBI) |
| `us-quarterly-estimated-tax` | SE health insurance deduction (reduces estimated tax liability) |
| `us-federal-return-assembly` | SE health insurance deduction for Schedule 1 Line 17 |
| `us-ca-return-assembly` | SE health insurance deduction for federal return portion |

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
