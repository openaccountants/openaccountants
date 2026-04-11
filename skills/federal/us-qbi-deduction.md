---
name: us-qbi-deduction
description: Tier 2 content skill for computing the §199A Qualified Business Income deduction for US sole proprietors and single-member LLCs disregarded for federal tax purposes. Covers tax year 2025 under the One Big Beautiful Bill Act (P.L. 119-21, July 4 2025) which made §199A permanent at 20% for 2025 (rising to 23% for 2026+). Handles the QBI calculation from Schedule C net profit, the deductible SE tax and SE health insurance adjustments, the taxable income thresholds ($197,300 single / $394,600 MFJ), phase-in ranges for SSTB and W-2/UBIA limitations, the specified service trade or business (SSTB) classification, W-2 wage and UBIA of qualified property limitations, the interaction with retirement contributions, and Forms 8995 (simplified) and 8995-A (detailed). Consumes net profit from us-schedule-c-and-se-computation and SE health insurance / retirement from companion skills. MUST be loaded alongside us-tax-workflow-base v0.1 or later. Federal only. No state tax.
version: 0.2
---

# US QBI Deduction Skill v0.2

## What this file is, and what it is not

**This file is a content skill that loads on top of `us-tax-workflow-base` v0.1.** It computes the §199A Qualified Business Income (QBI) deduction for sole proprietors and single-member LLCs (disregarded entities) for tax year 2025. It does not classify transactions (that is `us-sole-prop-bookkeeping`), compute Schedule C net profit or SE tax (that is `us-schedule-c-and-se-computation`), or compute retirement contributions or SE health insurance (those are companion skills whose outputs feed into this one).

**Where this skill fits in the pipeline:**

```
Bank statement / source data
        ↓
us-sole-prop-bookkeeping (classifies every transaction into a Schedule C line)
        ↓
us-schedule-c-and-se-computation (aggregates, runs Form 8829, computes net profit, computes SE tax)
        ↓
us-self-employed-retirement + us-self-employed-health-insurance (retirement deduction, SE health insurance deduction)
        ↓
us-qbi-deduction (THIS SKILL — computes QBI and the §199A deduction)
        ↓
us-quarterly-estimated-tax (safe harbor for following year)
```

This skill is downstream of Schedule C computation AND of the retirement and SE health insurance skills. That ordering matters because QBI is reduced by retirement contributions and SE health insurance premiums, creating a circular dependency that must be resolved iteratively or algebraically.

**Tax year coverage.** This skill is current for **tax year 2025** as of its currency date (April 2026). It reflects the One Big Beautiful Bill Act (Public Law 119-21, signed July 4, 2025) which made §199A permanent and set the rate increase to 23% effective for tax years beginning after December 31, 2025. For tax year 2025, the rate remains 20%.

**The reviewer is the customer of this output.** The skill produces a QBI computation worksheet and a brief that the reviewing EA or CPA can audit and sign off on.

---

## Section 1 — Scope statement

This skill covers, for tax year 2025:

- **QBI computation** from Schedule C net profit, adjusted for the deductible half of SE tax, SE health insurance premiums, and retirement contributions
- **§199A deduction calculation** at the 20% rate (2025)
- **Taxable income threshold testing** — determining whether the simplified or detailed computation applies
- **Specified service trade or business (SSTB) classification** — determining whether the taxpayer's trade or business is an SSTB under §199A(d)(2) and Treas. Reg. §1.199A-5
- **W-2 wage limitation** — the greater-of test under §199A(b)(2): (a) 50% of W-2 wages, or (b) 25% of W-2 wages plus 2.5% of UBIA of qualified property
- **UBIA of qualified property limitation** — unadjusted basis immediately after acquisition of qualified property
- **Phase-in computation** for taxpayers with taxable income within the phase-in range above the threshold
- **Form 8995 (simplified)** — for taxpayers with taxable income at or below the threshold
- **Form 8995-A (detailed)** — for taxpayers with taxable income above the threshold, SSTBs, or multiple trades or businesses
- **The circular dependency** between QBI, retirement contributions, and SE health insurance
- **Taxable income limitation** — QBI deduction cannot exceed 20% of taxable income (excluding net capital gain)

This skill does NOT cover:

- QBI from sources other than Schedule C (partnerships on K-1, S corporations on K-1, REITs, PTPs) — out of scope
- Aggregation of multiple trades or businesses under Treas. Reg. §1.199A-4 — flagged for reviewer if multiple Schedule Cs exist
- Net operating loss interactions with QBI — flagged for reviewer
- QBI carryover of losses from prior years — flagged for reviewer
- Any state-level QBI deduction or addback — out of scope
- Computation of the deduction for cooperatives under §199A(g) — out of scope

---

## Section 2 — Year coverage and currency

**Tax year covered:** 2025 (returns due April 15, 2026, or October 15, 2026 with extension).

**Currency date:** April 2026.

**Legislation reflected:**
- Internal Revenue Code §199A as in force for tax year 2025
- One Big Beautiful Bill Act (OBBBA), Public Law 119-21, signed July 4, 2025 — made §199A permanent (it was set to expire after 2025 under TCJA) and enacted a rate increase to 23% for tax years beginning after December 31, 2025. For tax year 2025, the deduction rate remains 20%.
- Tax Cuts and Jobs Act of 2017 — original enactment of §199A
- Treasury Regulations §1.199A-1 through §1.199A-6 — final regulations (January 2019) and subsequent amendments
- Rev. Proc. 2024-40 — 2025 inflation adjustments for taxable income thresholds
- IRS Publication 535 (2025) — QBI deduction guidance (where available)
- Form 8995 and Form 8995-A Instructions for tax year 2025

**Currency limitations:**
- OBBBA made §199A permanent and enacted the 23% rate for 2026+. The 2025 rate is confirmed at 20%. No OBBBA provision changed the 2025 QBI mechanics (thresholds, SSTB rules, W-2 wage test, UBIA test).
- The phase-in range widths ($50,000 single / $100,000 MFJ) are statutory under §199A(e)(2)(B) and are NOT indexed for inflation.

---

## Section 3 — Year-specific figures table for tax year 2025

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| §199A QBI deduction rate | 20% | IRC §199A(a); OBBBA confirmed for 2025 |
| §199A QBI deduction rate (2026 onward) | 23% | OBBBA P.L. 119-21; IRC §199A as amended |
| Taxable income threshold (single / HoH / QSS) | $197,300 | Rev. Proc. 2024-40; IRC §199A(e)(2) |
| Taxable income threshold (MFJ) | $394,600 | Rev. Proc. 2024-40 |
| Taxable income threshold (MFS) | $197,300 | Rev. Proc. 2024-40 |
| Phase-in range (single / HoH / QSS) | $50,000 above threshold | IRC §199A(e)(2)(B)(i); statutory, not indexed |
| Phase-in range (MFJ) | $100,000 above threshold | IRC §199A(e)(2)(B)(ii); statutory, not indexed |
| Phase-in range top (single) | $247,300 | $197,300 + $50,000 |
| Phase-in range top (MFJ) | $494,600 | $394,600 + $100,000 |
| W-2 wage limitation — alternative 1 | 50% of W-2 wages | IRC §199A(b)(2)(B)(i) |
| W-2 wage limitation — alternative 2 | 25% of W-2 wages + 2.5% of UBIA | IRC §199A(b)(2)(B)(ii) |
| Taxable income cap on QBI deduction | 20% of taxable income (excl. net capital gain) | IRC §199A(a)(1)(B) |
| SE tax rate (for deductible-half computation) | 15.3% (12.4% OASDI + 2.9% Medicare) | IRC §1401 |
| Net SE earnings adjustment factor | 92.35% | IRC §1402(a)(12) |

---

## Section 4 — Primary source library

### Statute (Internal Revenue Code, Title 26 USC)

- **IRC §199A** — Qualified business income deduction (full section)
- **IRC §199A(a)** — Allowance of deduction: lesser of (A) combined QBI amount or (B) 20% of taxable income minus net capital gain
- **IRC §199A(b)** — Combined QBI amount: sum of deductible amounts for each qualified trade or business
- **IRC §199A(b)(2)** — W-2 wage / UBIA limitation (applies above the threshold)
- **IRC §199A(c)** — Definition of qualified business income
- **IRC §199A(c)(3)(B)** — Items excluded from QBI: capital gains/losses, dividends, interest not allocable to trade or business, commodities transactions, foreign currency gains/losses, certain annuity income
- **IRC §199A(c)(4)** — QBI does not include reasonable compensation paid to taxpayer by S corp or guaranteed payments from partnership
- **IRC §199A(d)** — Qualified trade or business definition, SSTB exclusion
- **IRC §199A(d)(2)** — Specified service trade or business defined
- **IRC §199A(d)(3)** — Exception for taxpayers below threshold
- **IRC §199A(e)(2)** — Taxable income threshold and phase-in range
- **IRC §199A(f)** — Special rules (netting of QBI from multiple businesses, carryover of losses)
- **IRC §164(f)** — Deductible half of SE tax
- **IRC §162(l)** — Self-employed health insurance deduction
- **IRC §1402(a)(12)** — 92.35% net SE earnings adjustment

### Treasury Regulations (26 CFR)

- **Treas. Reg. §1.199A-1** — Operational rules
- **Treas. Reg. §1.199A-2** — W-2 wages and UBIA of qualified property
- **Treas. Reg. §1.199A-3** — Qualified business income, qualified REIT dividends, qualified PTP income
- **Treas. Reg. §1.199A-4** — Aggregation of trades or businesses
- **Treas. Reg. §1.199A-5** — Specified service trades or businesses and the trade or business of performing services as an employee
- **Treas. Reg. §1.199A-6** — RPE-level reporting

### IRS Guidance and Forms

- **Rev. Proc. 2024-40** — 2025 inflation adjustments
- **Form 8995** — Qualified Business Income Deduction Simplified Computation
- **Form 8995-A** — Qualified Business Income Deduction (detailed, with Schedules A through D)
- **IRS Publication 535 (2025)** — Business expenses (QBI chapter)

---

## Section 5 — The QBI computation for sole proprietors

### Step 1 — Determine qualified business income (QBI)

For a sole proprietor or SMLLC, QBI starts with Schedule C net profit (Line 31) and is adjusted downward:

```
QBI = Schedule C net profit (Line 31)
    − Deductible half of SE tax (Schedule 1, Line 15)
    − SE health insurance deduction (Schedule 1, Line 17)
    − Deductible retirement contributions (Schedule 1, Line 16 — SEP, SIMPLE, Solo 401(k))
```

**Why these adjustments?** Under IRC §199A(c)(1), QBI is the net amount of qualified items of income, gain, deduction, and loss with respect to the qualified trade or business. The deductible half of SE tax, the SE health insurance deduction, and the retirement contribution deduction are all deductions attributable to the trade or business under §62(a)(1), so they reduce QBI.

**What is NOT subtracted from QBI:**
- The standard deduction or itemized deductions (these are not attributable to the trade or business)
- The QBI deduction itself (that would be circular — the statute explicitly excludes it)
- Estimated tax payments (these are not deductions)
- State income taxes (not deductible on Schedule C and not attributable under §199A)

### Step 2 — Determine taxable income BEFORE the QBI deduction

Taxable income for QBI threshold purposes = AGI minus the greater of the standard deduction or itemized deductions, computed WITHOUT the QBI deduction itself.

This figure determines:
1. Whether the taxpayer is below, within, or above the phase-in range
2. The overall cap on the QBI deduction (20% of taxable income excluding net capital gain)

### Step 3 — Apply the threshold test

**Below the threshold** (taxable income ≤ $197,300 single / $394,600 MFJ):
- The QBI deduction is simply 20% of QBI, subject to the taxable income cap
- SSTB classification does NOT matter (the SSTB exclusion is phased in above the threshold)
- W-2 wage and UBIA limitations do NOT apply
- Use **Form 8995** (simplified computation)

**Above the threshold but within the phase-in range** ($197,300 < TI ≤ $247,300 single / $394,600 < TI ≤ $494,600 MFJ):
- W-2 wage / UBIA limitations are phased in
- SSTB exclusion is phased in (QBI, W-2 wages, and UBIA are reduced by the applicable percentage)
- Use **Form 8995-A** (detailed computation)
- The phase-in percentage = (taxable income − threshold) / phase-in range width

**Above the phase-in range** (taxable income > $247,300 single / $494,600 MFJ):
- W-2 wage / UBIA limitations apply in full
- SSTB businesses get ZERO QBI deduction
- Use **Form 8995-A** (detailed computation)

### Step 4 — W-2 wage and UBIA limitation (when applicable)

For taxpayers above the threshold, the QBI deduction for each qualified trade or business cannot exceed the GREATER of:

**(a)** 50% of W-2 wages paid by that trade or business, OR

**(b)** 25% of W-2 wages paid by that trade or business PLUS 2.5% of the unadjusted basis immediately after acquisition (UBIA) of qualified property held by the business

**For most sole props without employees:** W-2 wages = $0 (the sole proprietor's own draw is NOT W-2 wages). This means:
- Alternative (a) = $0
- Alternative (b) = 2.5% of UBIA of qualified property

If the sole prop has no depreciable property still within its ADS recovery period, UBIA = $0, and BOTH alternatives = $0. This means the QBI deduction is limited to $0 for taxpayers fully above the phase-in range.

**This is the critical cliff for high-income sole props without employees.** If taxable income exceeds the phase-in range top and the business has no W-2 wages and no qualifying property, the QBI deduction is $0. This is a major reason high-income sole props consider S corporation election (to create W-2 wages via reasonable compensation).

### Step 5 — UBIA of qualified property

UBIA = the unadjusted basis of tangible depreciable property held at the close of the tax year, that is:
- Used in the production of QBI, AND
- Still within its depreciable period (the longer of the MACRS recovery period or 10 years from the placed-in-service date)

"Unadjusted" means the original cost basis without reduction for depreciation. The property must still be in use at year-end.

**Example:** A MacBook Pro purchased for $3,499 in 2025, placed in service immediately, with a 5-year MACRS recovery period. UBIA = $3,499 for tax years 2025 through 2034 (10-year lookback). Even if 100% bonus depreciation was taken in year 1, the UBIA remains $3,499 for QBI purposes.

### Step 6 — Specified service trade or business (SSTB) rules

Under IRC §199A(d)(2) and Treas. Reg. §1.199A-5, an SSTB is a trade or business involving the performance of services in the fields of:

- Health
- Law
- Accounting
- Actuarial science
- Performing arts
- Consulting (defined narrowly — see below)
- Athletics
- Financial services
- Brokerage services
- Any trade or business where the principal asset is the reputation or skill of one or more of its employees or owners (narrowed by regulation to mean income from endorsements, licensing of name/likeness/image, and appearance fees)
- Engineering and architecture were EXCLUDED from the SSTB list by statute (§199A(d)(2) flush language)

**Key SSTB determinations for sole props in the target demographic:**

| Activity | SSTB? | Authority |
|---|---|---|
| Software development | NO | Treas. Reg. §1.199A-5(b)(2)(vii) — not consulting |
| Web development | NO | Same reasoning as software development |
| UX/UI design | NO | Design is not a listed field |
| Graphic design | NO | Design is not a listed field |
| Data science / analytics | NO | Not a listed field; not consulting under the narrow reg definition |
| IT consulting (advisory only, no deliverable) | MAYBE | Treas. Reg. §1.199A-5(b)(2)(vii) — "consulting" means providing advice and counsel, not delivering a work product. If the engagement produces a deliverable (code, report, system), it is NOT consulting for SSTB purposes |
| Marketing consulting | MAYBE | Same analysis — depends on whether the taxpayer provides advice vs. deliverables |
| Financial planning / advisory | YES | Financial services under §199A(d)(2) |
| Legal services | YES | Law under §199A(d)(2) |
| Medical / dental practice | YES | Health under §199A(d)(2) |
| Accounting / bookkeeping services | YES | Accounting under §199A(d)(2) |
| Real estate agent | NO | Not a listed field |

**The "consulting" trap:** The regulations define consulting narrowly as "the provision of advice and counsel to clients to assist the client in achieving goals and solving problems." Treas. Reg. §1.199A-5(b)(2)(vii). Importantly, performing services in the field of consulting does NOT include "the performance of services other than advice and counsel, such as sales or the provision of training courses." If a "consultant" actually delivers code, designs, systems, analyses, or other work product, the business is NOT consulting for SSTB purposes.

### Step 7 — Compute the deduction

**Below the threshold (simplified — Form 8995):**

```
QBI deduction = lesser of:
  (A) 20% × QBI
  (B) 20% × (taxable income − net capital gain)
```

**Within the phase-in range (detailed — Form 8995-A):**

The computation requires:
1. Calculate the "reduction amount" for the W-2/UBIA limitation
2. Calculate the "applicable percentage" for SSTB reduction (if SSTB)
3. Apply phase-in percentage to transition from unlimited to limited

Phase-in percentage = (taxable income − threshold) / ($50,000 single or $100,000 MFJ)

For non-SSTB businesses:
- Tentative QBI deduction = 20% × QBI
- W-2/UBIA limited amount = greater of 50% × W-2 wages or 25% × W-2 wages + 2.5% × UBIA
- Reduction amount = (tentative QBI deduction − W-2/UBIA limited amount) × phase-in percentage
- QBI deduction = tentative QBI deduction − reduction amount

For SSTB businesses:
- Applicable percentage = 1 − phase-in percentage
- Adjusted QBI = QBI × applicable percentage
- Adjusted W-2 wages = W-2 wages × applicable percentage
- Adjusted UBIA = UBIA × applicable percentage
- Then apply the non-SSTB formula above using the adjusted figures

**Above the phase-in range (detailed — Form 8995-A):**

For non-SSTB:
- QBI deduction = lesser of 20% × QBI or W-2/UBIA limited amount

For SSTB:
- QBI deduction = $0

### Step 8 — Apply the taxable income cap

The final QBI deduction cannot exceed 20% of taxable income (excluding net capital gain). This cap always applies regardless of threshold position.

### Step 9 — The circular dependency with retirement contributions

The computation of QBI depends on retirement contributions (which reduce QBI), but some retirement contribution limits depend on net SE earnings which are independent of QBI. However, the QBI deduction affects taxable income, which affects the threshold test, which can change the QBI deduction. For most sole props below the threshold, this circularity is irrelevant — the 20% rate applies regardless. For those near the threshold, the skill must iterate:

1. Compute retirement contributions and SE health insurance first (these depend on net SE earnings, not QBI)
2. Compute QBI = Schedule C net profit − deductible half of SE tax − SE health insurance − retirement contributions
3. Compute the QBI deduction
4. Compute taxable income including the QBI deduction
5. Verify the threshold position — if it changed from step 3's assumption, recompute

In practice, for most sole props, a single pass is sufficient because retirement and SE health insurance are fixed once net SE earnings are known.

---

## Section 6 — Form 8995 (simplified computation)

Form 8995 is used when:
- Taxable income is at or below $197,300 (single) / $394,600 (MFJ)
- The taxpayer has only one trade or business (or does not need aggregation)
- No SSTB considerations apply (below threshold, SSTB status is irrelevant)

**Form 8995 line-by-line:**

- **Line 1:** Trade, business, or aggregation name and TIN (sole prop = SSN)
- **Line 2:** Qualified business income (QBI) — from the computation in Section 5
- **Line 3:** Total QBI — sum of all lines 2 (typically just one for single-Schedule-C filers)
- **Line 4:** QBI component — if line 3 is positive, multiply by 20%. If negative, enter $0 (loss is carried forward)
- **Line 5:** Qualified REIT dividends and PTP income — $0 for most sole props
- **Line 6:** REIT/PTP component — 20% of line 5
- **Line 7:** Total QBI deduction before income limitation — line 4 + line 6
- **Line 8:** Taxable income before QBI deduction
- **Line 9:** Net capital gain — enter as positive number
- **Line 10:** Line 8 minus line 9
- **Line 11:** Income limitation — 20% of line 10
- **Line 12:** QBI deduction — smaller of line 7 or line 11
- **Line 13:** Total QBI loss carryforward — if line 3 is negative, carry to next year
- **Line 14:** Total REIT/PTP loss carryforward

---

## Section 7 — Form 8995-A (detailed computation)

Form 8995-A is used when:
- Taxable income exceeds the threshold ($197,300 single / $394,600 MFJ)
- The taxpayer has an SSTB (regardless of income — though below threshold, Form 8995 may still be used)
- Multiple trades or businesses require separate computation
- Aggregation election under Treas. Reg. §1.199A-4

Form 8995-A is substantially more complex. The skill produces the computation worksheet but defers the actual form preparation to the reviewer. Key additional schedules:

- **Schedule A** — SSTB determination for each trade or business
- **Schedule B** — Aggregation of business operations
- **Schedule C** — Loss netting and carryforward
- **Schedule D** — Special rules for patrons of agricultural and horticultural cooperatives

For a single-Schedule-C sole prop above the threshold with a non-SSTB business, the key computation on Form 8995-A is:

1. Report QBI, W-2 wages, and UBIA for the business
2. Compute the W-2/UBIA limitation
3. Apply the phase-in if within the range
4. Apply the taxable income cap

---

## Section 8 — QBI loss carryover rules

Under IRC §199A(c)(2), if QBI from a qualified trade or business is negative (a loss), the loss:

1. Is NOT deductible as part of the QBI deduction in the loss year
2. Is carried forward to the next tax year
3. Reduces QBI from the SAME trade or business in the next year (and subsequent years until absorbed)
4. Is treated as a loss from a separate trade or business in the carryforward year

For sole props with a single business: a Schedule C loss year produces zero QBI deduction, and the loss carries forward to reduce QBI in the next profitable year. The carryforward is tracked on Form 8995 line 13 or Form 8995-A Schedule C.

---

## Section 9 — Conservative defaults table

| Ambiguity | Conservative default |
|---|---|
| SSTB status unclear | Assume SSTB (reduces or eliminates deduction above threshold); flag for reviewer |
| Taxable income near the threshold (within $5,000) | Compute both ways (below-threshold simplified and above-threshold detailed); present both to reviewer |
| W-2 wages unclear (did the business have common-law employees?) | Assume $0 W-2 wages (conservative above threshold); ask for clarification |
| UBIA of qualified property not documented | Assume $0 UBIA (conservative above threshold); ask for Form 4562 or asset list |
| Prior-year QBI loss carryover amount not provided | Assume $0 carryover; flag for reviewer to check prior-year Form 8995/8995-A |
| Retirement contributions not yet computed | Compute retirement first, then QBI; do not skip the QBI adjustment |
| SE health insurance deduction not yet computed | Compute SE health insurance first, then QBI; do not skip the QBI adjustment |
| Multiple Schedule Cs | Compute QBI separately for each; do NOT net positive and negative QBI across businesses without applying §199A(c)(2) loss rules |
| Taxpayer has both SE income and W-2 wages from another employer | W-2 wages from another employer are NOT the taxpayer's qualified trade or business's W-2 wages for the §199A(b)(2) limitation |

---

## Section 10 — Topical refusal catalogue

Refusals on top of the global catalogue in `us-tax-workflow-base` Section 6 and the upstream skills' catalogues.

**R-QBI-MULTI — Multiple trades or businesses requiring aggregation.**
Trigger: The taxpayer has multiple Schedule Cs or K-1s with QBI, and the question of aggregation under Treas. Reg. §1.199A-4 arises.
Output: "Aggregation of multiple trades or businesses for QBI purposes under Treas. Reg. §1.199A-4 requires analysis of common ownership, shared facilities, shared employees, and interdependence. This skill computes QBI for a single Schedule C. For multi-business aggregation, please consult a CPA or Enrolled Agent."

**R-QBI-K1 — QBI from partnerships or S corporations.**
Trigger: The taxpayer has QBI flowing from a Form K-1 (partnership or S corporation).
Output: "QBI from partnerships and S corporations flows through Form K-1 and requires coordination with the entity-level W-2 wage and UBIA reporting. This skill handles sole proprietor QBI only. For K-1 QBI, please consult a CPA or Enrolled Agent."

**R-QBI-REIT — REIT dividends or PTP income.**
Trigger: The taxpayer has qualified REIT dividends or qualified PTP income eligible for the §199A deduction.
Output: "Qualified REIT dividends and publicly traded partnership (PTP) income have a separate 20% deduction under §199A(a)(1)(B) with different rules than trade-or-business QBI. This skill does not compute the REIT/PTP component. Please consult a CPA or Enrolled Agent."

**R-QBI-NOL — Net operating loss interaction.**
Trigger: The taxpayer has an NOL carryforward that affects taxable income, which in turn affects the QBI threshold test.
Output: "NOL carryforwards reduce taxable income, which can change the QBI threshold position and the taxable income cap on the QBI deduction. NOL-QBI interaction requires careful ordering. Please consult a CPA or Enrolled Agent."

**R-QBI-SSTB-MIXED — Mixed SSTB and non-SSTB activities.**
Trigger: The taxpayer's business has both SSTB and non-SSTB components (e.g., a CPA who also sells software products).
Output: "When a business has both SSTB and non-SSTB activities, the de minimis rule under Treas. Reg. §1.199A-5(c)(1) may apply: if gross receipts from the SSTB activity are less than 10% of total gross receipts (or 5% if total gross receipts exceed $25 million), the entire business may be treated as non-SSTB. This requires detailed revenue analysis. Please consult a CPA or Enrolled Agent."

---

## Section 11 — Reviewer attention thresholds

| Threshold | Trigger | Rationale |
|---|---|---|
| Taxable income within $10,000 of threshold | Always flag | Small changes in income could shift QBI computation dramatically |
| Taxable income above phase-in range top + sole prop has no W-2 wages | Always flag | QBI deduction is likely $0; S-corp election discussion warranted |
| QBI deduction > $15,000 | Always flag | Material deduction; verify all adjustments |
| SSTB classification is ambiguous | Always flag | Wrong classification can eliminate deduction above threshold |
| Business has both consulting and deliverable-based work | Always flag | "Consulting" SSTB classification depends on facts and circumstances |
| Prior-year QBI loss carryover applied | Always flag | Verify against prior-year Form 8995/8995-A |
| QBI is negative (loss year) | Always flag | Carryforward must be tracked |
| Retirement contribution was not subtracted from QBI | Always flag | Overstates QBI and the deduction |
| Taxpayer has multiple businesses | Always flag | Aggregation and loss netting rules apply |

---

## Section 12 — Worked examples

### Example 1 — Below threshold, non-SSTB sole prop (simplified — Form 8995)

**Taxpayer:** Maria Hernandez, single, freelance UX designer (NOT SSTB), Austin TX.

**Inputs from upstream skills:**
- Schedule C net profit (Line 31): $62,644
- Deductible half of SE tax: $4,427
- SE health insurance deduction: $8,400
- Solo 401(k) employee deferral: $23,500
- Employer contribution: $7,264

**QBI computation:**
```
Schedule C net profit:                $62,644
Less: deductible half of SE tax:     ($4,427)
Less: SE health insurance:           ($8,400)
Less: retirement contributions:      ($30,764)  [$23,500 + $7,264]
                                     --------
QBI:                                  $19,053
```

**QBI deduction:** 20% × $19,053 = **$3,811**

**Taxable income check:** $62,644 AGI − $4,427 SE tax − $8,400 SE health − $30,764 retirement − $15,000 standard deduction (2025) = ~$4,053 taxable income. Well below $197,300 threshold. QBI deduction limited to lesser of $3,811 or 20% × $4,053 = $811.

**Result: QBI deduction = $811** (limited by taxable income cap).

**Form:** 8995 (simplified).

### Example 2 — Below threshold, higher income, non-SSTB

**Taxpayer:** James Chen, single, freelance software developer (NOT SSTB), San Francisco.

**Inputs:**
- Schedule C net profit: $150,000
- Deductible half of SE tax: $10,597
- SE health insurance: $9,600
- SEP-IRA contribution: $26,081
- Standard deduction: $15,000

**QBI computation:**
```
Schedule C net profit:                $150,000
Less: deductible half of SE tax:     ($10,597)
Less: SE health insurance:            ($9,600)
Less: SEP-IRA contribution:          ($26,081)
                                     --------
QBI:                                  $103,722
```

**QBI deduction (tentative):** 20% × $103,722 = $20,744

**Taxable income:** $150,000 − $10,597 − $9,600 − $26,081 − $15,000 = $88,722. Below $197,300.

**Taxable income cap:** 20% × $88,722 = $17,744

**Result: QBI deduction = $17,744** (limited by taxable income cap).

### Example 3 — Above threshold, SSTB, within phase-in

**Taxpayer:** Sarah Kim, MFJ, freelance financial advisor (SSTB — financial services).

**Inputs:**
- Schedule C net profit: $380,000
- Deductible half of SE tax: $23,886
- SE health insurance: $14,400
- Solo 401(k) total contributions: $58,000
- Spouse W-2 income: $120,000
- Combined taxable income (before QBI): $425,000

**Analysis:** $425,000 is above $394,600 MFJ threshold but within the $494,600 phase-in top.

Phase-in percentage = ($425,000 − $394,600) / $100,000 = 30.4%

Applicable percentage for SSTB = 1 − 30.4% = 69.6%

Adjusted QBI = ($380,000 − $23,886 − $14,400 − $58,000) × 69.6% = $283,714 × 69.6% = $197,465

Tentative QBI deduction = 20% × $197,465 = $39,493

W-2 wages (adjusted) = $0 × 69.6% = $0

W-2/UBIA limited = $0 (no employees, minimal property)

Reduction amount phases in the W-2/UBIA limit. Because the W-2/UBIA limit is $0, the QBI deduction is reduced proportionally.

**Result:** The QBI deduction is significantly reduced and approaches $0 as the phase-in percentage increases. Flag for reviewer — S-corp election discussion warranted.

---

## Section 13 — Edge cases

1. **QBI is negative.** Schedule C loss or large retirement contributions create negative QBI. Deduction = $0; loss carries forward. Track on Form 8995 line 13 or Form 8995-A Schedule C.

2. **Taxable income is negative.** QBI deduction = $0 (cannot create or increase a loss). The QBI itself still carries forward if negative.

3. **Sole prop has employees (has W-2 wages).** W-2 wages paid to employees count for the §199A(b)(2) limitation, but the sole prop's own draw does NOT. This is unusual for freelancers but possible. Verify with Form 941/944 filings.

4. **Software developer who also provides "consulting."** If the same Schedule C includes both development (deliverable-based, NOT SSTB) and advisory consulting (advice-only, potentially SSTB), the de minimis rule under Treas. Reg. §1.199A-5(c)(1) applies: if SSTB revenue < 10% of total, the entire business is non-SSTB. If ≥ 10%, the skill cannot resolve — flag for reviewer.

5. **Taxpayer exactly at the threshold.** At $197,300 (single) exactly, the simplified computation applies. The phase-in begins at $197,301. Use Form 8995.

6. **Mid-year change in business activity.** If the business changed character mid-year (e.g., from consulting to software product sales), QBI is not split — it is all from the same Schedule C trade or business for the full year. SSTB status is determined based on the overall character for the full year.

7. **Property fully depreciated but within 10-year UBIA window.** UBIA uses the LONGER of the ADS recovery period or 10 years from placed-in-service. A laptop with a 5-year MACRS recovery period has a 5-year ADS life, but the 10-year rule applies, so UBIA persists for 10 years even though the asset is fully depreciated.

8. **Married filing separately.** The threshold is halved to $197,300 (same as single), and the phase-in range is halved to $25,000. This is a trap for high-income couples filing separately.

9. **Roth IRA contributions do NOT reduce QBI.** Only deductible retirement contributions (SEP, Solo 401(k) pre-tax deferrals, SIMPLE, traditional IRA) reduce QBI. Roth contributions are after-tax and do not affect QBI.

10. **Community property states.** In community property states (CA, TX, etc.), a sole prop's Schedule C income may be split between spouses for tax purposes. Each spouse reports their share, and QBI follows the income allocation. The skill flags this if the filing status is MFJ and the state is a community property state, but does not perform the split — that is a personal return issue.

---

## Section 14 — Test suite

### Test 1 — Basic below-threshold computation
**Input:** Schedule C net profit $80,000; deductible half of SE tax $5,652; SE health insurance $6,000; SEP-IRA $13,470; single; standard deduction $15,000; no capital gains.
**Expected:** QBI = $80,000 − $5,652 − $6,000 − $13,470 = $54,878. Tentative QBI deduction = 20% × $54,878 = $10,976. Taxable income = $80,000 − $5,652 − $6,000 − $13,470 − $15,000 = $39,878. TI cap = 20% × $39,878 = $7,976. **QBI deduction = $7,976** (TI-limited). Form 8995.

### Test 2 — Loss year
**Input:** Schedule C net loss ($15,000); deductible half of SE tax $0 (no profit); single.
**Expected:** QBI = ($15,000). QBI deduction = $0. QBI loss carryforward = ($15,000) to next year. Form 8995 line 13.

### Test 3 — Above threshold, non-SSTB, no W-2 wages, no UBIA
**Input:** Schedule C net profit $300,000; deductible half of SE tax $20,405; SE health insurance $12,000; Solo 401(k) $55,000; single; taxable income (before QBI) $210,000.
**Expected:** $210,000 > $197,300. Phase-in % = ($210,000 − $197,300) / $50,000 = 25.4%. QBI = $300,000 − $20,405 − $12,000 − $55,000 = $212,595. Tentative = 20% × $212,595 = $42,519. W-2/UBIA limit = $0. Reduction = ($42,519 − $0) × 25.4% = $10,800. QBI deduction = $42,519 − $10,800 = $31,719. TI cap = 20% × $210,000 = $42,000. **QBI deduction = $31,719**. Form 8995-A.

### Test 4 — SSTB fully above phase-in range
**Input:** Schedule C net profit $350,000 (accounting firm); single; taxable income (before QBI) $260,000.
**Expected:** $260,000 > $247,300 (phase-in top). SSTB = accounting (yes). **QBI deduction = $0**. Form 8995-A.

### Test 5 — Below threshold, SSTB irrelevant
**Input:** Schedule C net profit $100,000 (legal consulting — SSTB); deductible half SE tax $7,065; SE health insurance $7,200; Solo 401(k) $30,000; single; taxable income (before QBI) $45,000.
**Expected:** $45,000 < $197,300. SSTB status irrelevant below threshold. QBI = $100,000 − $7,065 − $7,200 − $30,000 = $55,735. Tentative = 20% × $55,735 = $11,147. TI cap = 20% × $45,000 = $9,000. **QBI deduction = $9,000** (TI-limited). Form 8995.

### Test 6 — Taxable income cap binds
**Input:** Schedule C net profit $50,000; no retirement; no SE health insurance; deductible half SE tax $3,532; single; itemizes with $30,000 deductions (mortgage interest + SALT + charitable).
**Expected:** QBI = $50,000 − $3,532 = $46,468. Tentative = 20% × $46,468 = $9,294. Taxable income = $50,000 − $3,532 − $30,000 = $16,468. TI cap = 20% × $16,468 = $3,294. **QBI deduction = $3,294** (TI-limited). Form 8995.

---

## Section 15 — PROHIBITIONS

1. **NEVER compute the QBI deduction without first subtracting deductible half of SE tax, SE health insurance, and retirement contributions from Schedule C net profit.** Skipping any of these adjustments overstates QBI and the deduction.

2. **NEVER apply the 23% rate for tax year 2025.** The 23% rate takes effect for tax years beginning after December 31, 2025. For 2025, the rate is 20%.

3. **NEVER tell a taxpayer their SSTB status does not matter without checking their taxable income.** SSTB status is irrelevant below the threshold but critical above it.

4. **NEVER treat the sole proprietor's own draw or self-employment income as W-2 wages for the §199A(b)(2) limitation.** Only wages paid to common-law employees count.

5. **NEVER assume UBIA is zero without asking.** A sole prop who purchased equipment, vehicles, or other depreciable property may have significant UBIA even if the property is fully depreciated (the 10-year lookback applies).

6. **NEVER net QBI losses across multiple businesses without applying the §199A(c)(2) ordering rules.** Losses from one business reduce QBI from other businesses proportionally — they do not simply offset dollar-for-dollar.

7. **NEVER apply the QBI deduction to reduce self-employment tax.** The QBI deduction reduces income tax only (it is below the AGI line). It does not affect Schedule SE.

8. **NEVER ignore the taxable income cap.** Even when 20% of QBI is large, the deduction cannot exceed 20% of taxable income excluding net capital gain.

9. **NEVER file Form 8995 when Form 8995-A is required.** If taxable income exceeds the threshold, Form 8995-A must be used.

10. **NEVER classify software development as an SSTB.** Software development is not consulting, not engineering (excluded from SSTB by statute), and not any other listed field. This is confirmed by Treas. Reg. §1.199A-5(b)(2)(vii).

---

## Section 16 — Cross-skill references

| Upstream skill | Data consumed |
|---|---|
| `us-sole-prop-bookkeeping` | Classified transactions for Schedule C |
| `us-schedule-c-and-se-computation` | Schedule C Line 31 (net profit), deductible half of SE tax |
| `us-self-employed-health-insurance` | SE health insurance deduction amount |
| `us-self-employed-retirement` | Retirement contribution deduction amount |

| Downstream skill | Data provided |
|---|---|
| `us-quarterly-estimated-tax` | QBI deduction amount (reduces estimated tax liability) |
| `us-federal-return-assembly` | QBI deduction for Form 1040 Line 13 |
| `us-federal-tx-return-assembly` | QBI deduction for Texas-resident federal return |
| `us-ca-return-assembly` | QBI deduction for CA-resident federal return |

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
