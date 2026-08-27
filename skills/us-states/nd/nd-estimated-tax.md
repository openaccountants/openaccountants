---
name: nd-estimated-tax
description: Use this skill whenever asked about North Dakota individual quarterly estimated income tax for self-employed individuals, sole proprietors, single-member LLC owners, S-corp shareholders, or W-2 earners with insufficient withholding. Trigger on phrases like "ND-1ES", "North Dakota estimated tax", "ND quarterly payments", "ND-1UT", "underpayment penalty North Dakota", "ND safe harbor". Covers tax year 2025 Form ND-1ES vouchers, Schedule ND-1UT underpayment computation, and coordination with federal Form 1040-ES.
jurisdiction: US-ND
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ND Estimated Tax

## North Dakota Individual Quarterly Estimated Income Tax Skill

**Scope.** This skill covers North Dakota individual quarterly estimated income tax payments (Form ND-1ES) and the underpayment-of-estimated-tax interest computation (Schedule ND-1UT) for full-year ND residents who are sole proprietors, single-member LLC owners, S-corp shareholders, or W-2 employees with insufficient withholding. Tax year 2025 (payments due April 15, 2025 through January 15, 2026; reconciled on the Form ND-1 filed by April 15, 2026).

**Quality tier.** Q3 — AI-drafted, not independently verified. All outputs must be reviewed by a qualified tax professional before filing or payment.

## Section 1: Metadata

- **Tax type** — Individual income tax — quarterly estimated payments
- **Jurisdiction** — North Dakota (US-ND)
- **Tax year** — 2025 (TY 2025 quarterly payments and TY 2026 Q1)
- **Primary form** — Form ND-1ES (Estimated Income Tax — Individuals)
- **Reconciliation form** — Form ND-1 (Individual Income Tax Return)
- **Underpayment form** — Schedule ND-1UT (Underpayment of Estimated Individual Income Tax)
- **Federal counterpart** — Form 1040-ES
- **Tax authority** — North Dakota Office of State Tax Commissioner
- **Payment portal** — North Dakota Taxpayer Access Point (ND TAP)
- **Statute** — N.D.C.C. §57-38-62  _(N.D.C.C. §57-38-62)_
- **Regulation** — N.D. Admin Code 81-03-04-01 through 81-03-04-02  _(N.D. Admin Code 81-03-04-01 through 81-03-04-02)_
- **Underpayment interest rate** — 12% per annum [VERIFY: confirm against current Tax Commissioner publication for TY 2025]
- **Threshold** — Net tax liability expected to exceed $1,000 [VERIFY]

**Metadata table**

| Field | Value |
| --- | --- |
| Tax type | Individual income tax — quarterly estimated payments |
| Jurisdiction | North Dakota (US-ND) |
| Tax year | 2025 (TY 2025 quarterly payments and TY 2026 Q1) |
| Primary form | Form ND-1ES (Estimated Income Tax — Individuals) |
| Reconciliation form | Form ND-1 (Individual Income Tax Return) |
| Underpayment form | Schedule ND-1UT (Underpayment of Estimated Individual Income Tax) |
| Federal counterpart | Form 1040-ES |
| Tax authority | North Dakota Office of State Tax Commissioner |
| Payment portal | North Dakota Taxpayer Access Point (ND TAP) |
| Statute | N.D.C.C. §57-38-62 |
| Regulation | N.D. Admin Code 81-03-04-01 through 81-03-04-02 |
| Underpayment interest rate | 12% per annum [VERIFY: confirm against current Tax Commissioner publication for TY 2025] |
| Threshold | Net tax liability expected to exceed $1,000 [VERIFY] |

**Sources:**
- N.D.C.C. §57-38-62 (estimated tax statute): https://ndlegis.gov/cencode/t57c38.html
- N.D. Admin Code 81-03-04-02: https://www.law.cornell.edu/regulations/north-dakota/N-D-A-C-81-03-04-02
- Form ND-1ES (TY 2025): https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2024-iit/28709-form-nd-1es-2025.pdf
- Schedule ND-1UT (TY 2025): https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28704-schedule-nd-1ut-2025.pdf
- 2025 Individual Income Tax Booklet: https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf

## Section 2: Quick reference

### Threshold

**Threshold**

| Item | Value |
| --- | --- |
| ND net tax liability threshold | **More than $1,000** [VERIFY] |
| Federal trigger (required by §57-38-62) | Taxpayer must also be required to pay federal estimated tax |

### Safe harbor (lower of)

**Safe harbor (lower of)**

| Test | Amount |
| --- | --- |
| (a) Current-year test | **90%** of TY 2025 ND net tax liability |
| (b) Prior-year test | **100%** of TY 2024 ND net tax liability |
| (c) Qualified farmer / fisherman | 66⅔% of current-year liability |

> **Note on the 110% high-income variant.** Unlike federal Form 2210 — which requires 110% of the prior year for taxpayers with prior-year AGI over $150,000 — North Dakota's statute and Schedule ND-1UT use a **flat 100% prior-year** test with no high-income step-up. [VERIFY against the 2025 Schedule ND-1UT instructions before relying on this for high-AGI clients.]

### Four installment due dates (TY 2025 calendar-year filer)

**Four installment due dates (TY 2025 calendar-year filer)**

| Installment | Due date | Percentage of annual required payment |
| --- | --- | --- |
| Q1 | April 15, 2025 | 25% |
| Q2 | June 15, 2025 | 25% |
| Q3 | September 15, 2025 | 25% |
| Q4 | January 15, 2026 | 25% |

Same calendar as federal Form 1040-ES.

### Underpayment interest rate

**Underpayment interest rate**

| Period | Rate |
| --- | --- |
| TY 2025 | **12% per annum**, simple interest, computed from each installment due date to the earlier of the date paid or the original Form ND-1 due date (April 15, 2026) [VERIFY: confirm rate in 2025 Schedule ND-1UT instructions] |

### Payment methods

**Payment methods**

| Method | Notes |
| --- | --- |
| ND Taxpayer Access Point (TAP) | https://apps.nd.gov/tax/tap — ACH debit, credit card |
| Paper check + Form ND-1ES voucher | Make check payable to "ND State Tax Commissioner" |
| Direct debit via TAP scheduled payments | Schedule all four installments in advance |
| Credit / debit card via TAP | Third-party convenience fees apply |

No electronic-payment mandate currently published for individual estimated tax at any threshold. [VERIFY]

## Section 3: Threshold determination — when must you make estimated payments

Per N.D.C.C. §57-38-62 and the Form ND-1ES instructions, a North Dakota individual taxpayer **must** make estimated payments if **both** of the following are true for the tax year:

1. The taxpayer is required to pay federal estimated income tax (i.e., the federal safe-harbor rules of IRC §6654 would otherwise impose a federal underpayment penalty); **and**
2. The taxpayer's expected **ND net tax liability** for the year exceeds **$1,000** [VERIFY].

**ND net tax liability** = ND income tax (Form ND-1, Line 22 area) **less** allowable credits and **less** ND income tax withheld (W-2 Box 17 and 1099 ND-source withholding).

### Practical decision tree

- **Decision tree** — If withholding + credits ≥ 100% of prior-year ND tax → no estimates required (safe-harbor met by withholding alone). If expected ND liability ≤ $1,000 after withholding → no estimates required (de minimis). If neither of the above → estimates required; compute safe harbor in Section 4.  _(Form ND-1ES instructions)_

### Statutory de minimis exception (N.D. Admin Code 81-03-04-02(3)(d))

- **De minimis interest waiver** — Interest is waived where current-year tax liability exceeds withholding by less than $500, even if estimates were technically required. This is a penalty-relief rule, not a filing exemption — the taxpayer should still make estimated payments where prudent.  _(N.D. Admin Code 81-03-04-02(3)(d))_

## Section 4: Safe-harbor calculation

The taxpayer's **required annual payment** is the **lesser of**:

- **(a) Current-year safe harbor:** 90% of the ND net tax liability shown on the current-year Form ND-1; or
- **(b) Prior-year safe harbor:** 100% of the ND net tax liability shown on the prior-year Form ND-1.

The prior-year test is unavailable if:
- The prior-year return was not filed; or
- The prior-year return covered fewer than 12 months; or
- The taxpayer had no ND tax liability in the prior year (in which case current year is the only test).

### Worked safe-harbor calc

A taxpayer's TY 2024 ND tax was $4,000. They expect TY 2025 ND tax of $6,800.

- 90% × $6,800 = $6,120 (current-year)
- 100% × $4,000 = $4,000 (prior-year) ← **lesser**

Required annual payment = **$4,000**.

If TY 2025 withholding will be $1,200, the four installments must collectively total at least $4,000 − $1,200 = **$2,800**, i.e., **$700 per quarter** under the regular installment method.

### Joint vs. separate prior year

- **MFS to MFJ combination** — If the taxpayer was MFS in the prior year and is MFJ in the current year, the prior-year tests for both spouses are summed to determine the joint prior-year safe harbor.  _(N.D. Admin Code 81-03-04-02)_

## Section 5: Regular installment method — the four equal payments

Once the required annual payment is fixed, the **regular installment method** allocates **25% to each quarter**:

**Regular installment method table**

| Q | Cumulative required by due date | Marginal Q payment |
| --- | --- | --- |
| Q1 | 25% × annual | 25% |
| Q2 | 50% × annual | 25% |
| Q3 | 75% × annual | 25% |
| Q4 | 100% × annual | 25% |

- **Withholding deemed paid evenly** — ND withholding is deemed paid evenly across the four quarters unless the taxpayer elects to treat it as paid when actually withheld (rare and disadvantageous). The taxpayer satisfies each quarterly threshold by the sum of (a) ¼ of expected withholding plus (b) the ND-1ES voucher payment for that quarter.  _(Schedule ND-1UT)_

## Section 6: Annualized income installment method

Where income is **lumpy or back-loaded** (e.g., a freelancer who closes a major contract in Q3, or an S-corp shareholder receiving a December distribution), the regular ¼-each-quarter method overstates Q1/Q2 requirements. The **annualized income installment method** lets the taxpayer match installment size to actual cumulative income.

ND follows the federal Schedule AI approach by reference: if the taxpayer utilizes the annualized income installment method for federal purposes, the ND underpayment interest is waived to the corresponding extent (N.D. Admin Code 81-03-04-02(3)(c)).

### Annualization factors (calendar-year)

**Annualization factors (calendar-year)**

| Installment | Period ending | Months | Annualization factor | Installment % |
| --- | --- | --- | --- | --- |
| Q1 | March 31 | 3 | × 4 | 22.5% (90% / 4) |
| Q2 | May 31 | 5 | × 2.4 | 45% cumulative |
| Q3 | August 31 | 8 | × 1.5 | 67.5% cumulative |
| Q4 | December 31 | 12 | × 1 | 90% cumulative |

The taxpayer must complete the annualized worksheet (federal Schedule AI is the template; ND does not publish a standalone state annualization schedule — the federal schedule is attached or reproduced in support of Schedule ND-1UT columns).

### Worked example — Q3 income spike

A freelance software developer in Fargo expects $140,000 of ND-taxable income for TY 2025, but the income arrives as follows:

**Cumulative income table**

| Period through | Cumulative ND taxable income | Annualized | Tax at ND rates (single) |
| --- | --- | --- | --- |
| Mar 31 | $12,000 | $48,000 | $0 (within 0% bracket) |
| May 31 | $24,000 | $57,600 | $178 |
| Aug 31 | $60,000 | $90,000 | $810 |
| Dec 31 | $140,000 | $140,000 | $1,786 |

**Annualized required installment amounts table**

| Q | Cumulative required (rounded) | Marginal Q payment |
| --- | --- | --- |
| Q1 | 22.5% × $0 = $0 | $0 |
| Q2 | 45% × $178 = $80 | $80 |
| Q3 | 67.5% × $810 = $547 | $467 |
| Q4 | 90% × $1,786 = $1,607 | $1,060 |

Versus the regular method (¼ × $1,607 = ~$402 per quarter), the annualized method shifts ~$800 of payment from Q1/Q2 into Q3/Q4 while still avoiding underpayment interest.

Attach a reproduction of the federal annualization worksheet to Schedule ND-1UT when filing Form ND-1.

## Section 7: Form ND-1ES voucher mechanics

Form ND-1ES is a **single-page voucher** (one per installment). The taxpayer prepares one voucher per quarter when paying by check.

### Voucher fields

**Voucher fields table**

| Field | Source |
| --- | --- |
| Tax year | "2025" (or the year the installment relates to) |
| Installment number | 1, 2, 3, or 4 |
| Name, SSN, spouse SSN if joint | From last filed Form ND-1 |
| Mailing address | Current address |
| Amount paid | The quarterly installment |

### Mailing address

> Office of State Tax Commissioner
> PO Box 5622
> Bismarck, ND 58506-5622

[VERIFY: confirm address from current 2025 ND-1ES voucher]

### TAP electronic payment

For TAP payments, no paper voucher is required — the electronic posting through TAP serves as the voucher. The taxpayer logs into https://apps.nd.gov/tax/tap and selects "Make a Payment" → "Individual Income Tax" → "Estimated Payment."

### Recordkeeping

The taxpayer should retain confirmation numbers (TAP) or cancelled checks for each installment to support Form ND-1 Line 27 (Estimated payments) when filing the annual return.

## Section 8: Underpayment interest — Schedule ND-1UT

If any installment is underpaid (paid late or paid in a smaller amount than the required installment), the taxpayer owes underpayment interest computed on Schedule ND-1UT (SFN 28704). The Schedule attaches to Form ND-1.

### Computation outline (simplified)

- **Underpayment interest computation** — For each of the four installments: 1. Compute the required installment (¼ of the required annual payment, OR the annualized installment if Schedule AI is used). 2. Compute payments applied to that installment: ¼ of withholding + ND-1ES payments made by or before the installment due date. 3. Underpayment = (1) − (2), if positive. 4. Days outstanding = from installment due date to the earlier of (a) the date the underpayment is paid (via a later ND-1ES voucher or April-15 balance due) or (b) April 15, 2026. 5. Interest = Underpayment × 12% × (Days / 365). The sum of the four interest computations flows to Form ND-1 as additional amount due.  _(Schedule ND-1UT)_

### Statutory waivers (N.D. Admin Code 81-03-04-02(3))

**Statutory waivers table**  _(N.D. Admin Code 81-03-04-02(3))_

| Subsection | Waiver |
| --- | --- |
| (3)(a) | Qualified farmer who files federal return by March 1 and pays federal in full by that date |
| (3)(b) | Qualified farmer making one combined federal+state installment by January 15 |
| (3)(c) | Taxpayer using the federal annualized income installment method (state interest waived in proportion) |
| (3)(d) | De minimis — current-year liability exceeds withholding by less than $500 |

### Reasonable-cause waiver

The Tax Commissioner may waive interest under general reasonable-cause authority (illness, casualty, disaster, or other circumstance preventing timely payment). The taxpayer requests waiver in a signed statement attached to Form ND-1. [VERIFY: confirm administrative process in the current ND-1 booklet.]

## Section 9: Payment methods

### ND Taxpayer Access Point (TAP)

- URL: https://apps.nd.gov/tax/tap
- Login required (one-time enrollment for new users)
- Payment types: ACH debit (free), credit/debit card (third-party convenience fee, ~2.5%)
- Confirmation: emailed receipt with confirmation number
- Scheduling: all four installments can be scheduled in advance from a single TAP session — recommended for steady-income clients

### Paper check + Form ND-1ES voucher

- Make payable to "ND State Tax Commissioner"
- Write SSN and "2025 ND-1ES" on the memo line
- Mail with the printed voucher to the Bismarck PO Box [VERIFY current address]
- USPS postmark date controls timeliness

### Direct debit via TAP scheduled payments

- Same as TAP but the taxpayer sets the debit dates in advance for all four quarters
- Useful for clients who want set-and-forget compliance

### No electronic mandate

ND does not currently impose an electronic-payment mandate on individual estimated tax at any threshold [VERIFY against current Tax Commissioner guidance], though TAP is strongly recommended.

## Section 10: Coordination with federal Form 1040-ES

The ND quarterly calendar aligns exactly with the federal Form 1040-ES calendar:

**Coordination table**

| Installment | Federal 1040-ES | ND-1ES |
| --- | --- | --- |
| Q1 | April 15, 2025 | April 15, 2025 |
| Q2 | June 15, 2025 | June 15, 2025 |
| Q3 | September 15, 2025 | September 15, 2025 |
| Q4 | January 15, 2026 | January 15, 2026 |

### Practical workflow

1. Compute the federal required annual payment on Form 1040-ES worksheet (90% current / 100% or 110% prior depending on prior-year AGI). 2. Compute the ND required annual payment using the state safe-harbor tests (90% / flat 100% — no 110% step-up). 3. Schedule both federal (IRS Direct Pay or EFTPS) and state (ND TAP) payments for the same four dates. 4. If the federal taxpayer uses the annualized income installment method on federal Schedule AI, propagate the annualization to Schedule ND-1UT to preserve the state interest waiver under N.D. Admin Code 81-03-04-02(3)(c).

### Independence of safe harbors

- **Independence of federal and ND safe harbors** — The federal and ND safe harbors are independent — meeting the federal safe harbor does not satisfy the ND safe harbor. A taxpayer who is paid up federally via withholding alone may still owe ND estimates if their ND-1 line 27 prior-year amount is low (e.g., due to W-2 withholding being primarily federal with little ND-source withholding).  _(N.D. Admin Code 81-03-04-02)_

## Section 11: Tier 1 rules — deterministic

**Tier 1 rules table**

| Rule ID | Rule | Source |
| --- | --- | --- |
| NDES-T1-01 | Estimated tax required if expected ND net tax liability > $1,000 AND federal estimated tax is also required | N.D.C.C. §57-38-62; Form ND-1ES instructions |
| NDES-T1-02 | Safe harbor = lesser of (a) 90% current year OR (b) 100% prior year | N.D. Admin Code 81-03-04-02 |
| NDES-T1-03 | No 110% high-income variant — flat 100% prior-year test [VERIFY] | N.D. Admin Code 81-03-04-02 |
| NDES-T1-04 | Four equal installments due April 15, June 15, September 15, January 15 | Form ND-1ES |
| NDES-T1-05 | Underpayment interest rate = 12% per annum simple [VERIFY for TY 2025] | Schedule ND-1UT instructions |
| NDES-T1-06 | Withholding deemed paid evenly unless taxpayer elects otherwise | Schedule ND-1UT |
| NDES-T1-07 | De minimis waiver if current-year tax exceeds withholding by < $500 | N.D. Admin Code 81-03-04-02(3)(d) |
| NDES-T1-08 | Qualified farmer (>⅔ gross from farming) — single Jan 15 installment OR March 1 file + pay | N.D. Admin Code 81-03-04-02(3)(a),(b) |
| NDES-T1-09 | Annualized installment method per federal Schedule AI waives state interest in proportion | N.D. Admin Code 81-03-04-02(3)(c) |
| NDES-T1-10 | Prior-year safe harbor unavailable if prior return not filed or < 12 months | N.D. Admin Code 81-03-04-02 |

## Section 12: Tier 2 rules — requires judgment

**Tier 2 rules table**

| Rule ID | Situation | Guidance |
| --- | --- | --- |
| NDES-T2-01 | **Q3 / Q4 income spike** (S-corp distribution, contract close) | Consider annualized installment method; preserve federal Schedule AI for state interest waiver |
| NDES-T2-02 | **Mid-year ND move-in** | Part-year residents fall outside this skill (see Refusal R-NDES-04); coordinate with Schedule ND-1NR |
| NDES-T2-03 | **Spousal status change** (MFS to MFJ between years) | Combine both spouses' prior-year ND liabilities for the joint 100% test |
| NDES-T2-04 | **High W-2 withholding shortfall** | If W-2 withholding alone satisfies 100% prior-year, no estimates required; verify ND-source withholding (Box 17), not federal |
| NDES-T2-05 | **Newly self-employed (first year)** | No prior-year ND-1 → only 90% current-year test available; build cushion into Q1 |
| NDES-T2-06 | **Year-end Roth conversion or capital gain** | Annualize installment method may eliminate Q1/Q2 underpayment for a Q4 event |
| NDES-T2-07 | **K-1 income from out-of-state PTE** | Coordinate with ND credit for taxes paid to other states (Schedule ND-1CR) before sizing estimates |
| NDES-T2-08 | **Reasonable-cause waiver** | Illness, casualty, disaster — attach signed statement to Form ND-1; outcome at Commissioner's discretion |

## Section 13: Worked examples

### Example 1 — Steady-income ND freelancer ($120,000 expected)

**Facts.** Single, full-year ND resident, Bismarck. Freelance software developer. TY 2024 ND tax was $1,420. Expects TY 2025 net Schedule C income of $120,000, federal taxable income of $97,500 after standard deduction and QBI. No W-2 withholding. No prior-year safe harbor issues.

**ND tax computation table**

| Bracket | Amount | Rate | Tax |
| --- | --- | --- | --- |
| $0 – $48,475 | $48,475 | 0% | $0 |
| $48,475 – $97,500 | $49,025 | 1.95% | $956 |
| **TY 2025 ND tax** |  |  | **$956** |

**Safe harbor:**

- 90% × $956 (current) = $860
- 100% × $1,420 (prior) = $1,420
- **Lesser = $860**

But $860 < $1,000 threshold and prior-year exceeded $1,000? Prior year was $1,420. **Threshold is on the expected current-year liability ($956)** — at $956 the taxpayer is **not required** to make estimates (below $1,000) [VERIFY that threshold tests expected current-year ND tax rather than prior-year].

However, prudent practice is to pay anyway to avoid surprises. If the taxpayer elects to pay:

**Elective installment schedule**

| Installment | Date | Amount |
| --- | --- | --- |
| Q1 | April 15, 2025 | $215 |
| Q2 | June 15, 2025 | $215 |
| Q3 | September 15, 2025 | $215 |
| Q4 | January 15, 2026 | $215 |
| **Total** |  | **$860** |

Pay via ND TAP scheduled debits.

### Example 2 — Self-employed with Q3 income spike (annualized method)

**Facts.** Single, ND resident, Fargo. Software consultant. TY 2024 ND tax was $3,200. Expects TY 2025 federal taxable income of $185,000 from a Q3 contract close. Income flow:

**Income flow table**

| Cumulative through | FTI |
| --- | --- |
| Mar 31 | $20,000 |
| May 31 | $35,000 |
| Aug 31 | $145,000 |
| Dec 31 | $185,000 |

**TY 2025 ND tax table**

| Bracket | Tax |
| --- | --- |
| $48,475 – $185,000 → $136,525 × 1.95% = $2,662 |  |
| **TY 2025 ND tax** | **$2,662** |

**Safe harbor:**

- 90% × $2,662 = $2,396
- 100% × $3,200 = $3,200
- **Lesser = $2,396** (required annual payment)

**Regular installment method:** $2,396 / 4 = **$599 per quarter** — would require $599 by April 15 even though only $20k of income has materialized.

**Annualized installment method (using federal Schedule AI):**

Annualized tax at each cutoff:

**Annualized tax at each cutoff table**

| Period | Cumulative FTI | × Factor | Annualized FTI | ND tax | × 90% × Cum % | Required cum |
| --- | --- | --- | --- | --- | --- | --- |
| Q1 | $20,000 | 4 | $80,000 | $615 | × 22.5% | $138 |
| Q2 | $35,000 | 2.4 | $84,000 | $693 | × 45% | $312 |
| Q3 | $145,000 | 1.5 | $217,500 | (top bracket) ~$3,725 | × 67.5% | $2,514 |
| Q4 | $185,000 | 1 | $185,000 | $2,662 | × 90% | $2,396 |

**Marginal installments under annualized method table**

| Q | Required cum | Marginal |
| --- | --- | --- |
| Q1 | $138 | $138 |
| Q2 | $312 | $174 |
| Q3 | $2,514 | $2,202 |
| Q4 | $2,396 (capped) | $0 [VERIFY: cap mechanics in 2025 Schedule ND-1UT] |

The annualization defers ~$2,000 of Q1/Q2 payment exposure into Q3, matching income timing. Attach federal Schedule AI to Schedule ND-1UT.

### Example 3 — High-income earner with W-2 withholding shortfall

**Facts.** MFJ, both spouses ND residents. Primary spouse W-2 wages $280,000 with ND withholding of $4,800. Secondary spouse Schedule C net profit $60,000. TY 2024 ND tax was $5,900. Expects TY 2025 federal taxable income of $305,000, ND tax of $6,775.

**Safe harbor:**

- 90% × $6,775 (current) = $6,098
- 100% × $5,900 (prior) = $5,900
- **Lesser = $5,900**

> Note: federal would apply 110% × $5,900 = $6,490 because prior-year AGI > $150,000. **ND does NOT apply the 110% step-up** [VERIFY] — the state safe harbor remains a flat $5,900.

**Coverage check.** Withholding $4,800 satisfies $4,800 of the $5,900 requirement. Remaining gap: **$1,100**.

**Quarterly installments:** $1,100 / 4 = **$275 per quarter** via ND-1ES.

**Quarterly installments table**

| Installment | Date | Amount |
| --- | --- | --- |
| Q1 | April 15, 2025 | $275 |
| Q2 | June 15, 2025 | $275 |
| Q3 | September 15, 2025 | $275 |
| Q4 | January 15, 2026 | $275 |

Federal Form 1040-ES installments will be larger because the 110% federal prior-year test produces a higher required annual payment. The state and federal calendars are aligned; the amounts differ.

## Section 14: Refusal catalogue

- **R-NDES-01** — Estate or trust estimated tax  _("ND fiduciary estimated payments (Form 38-ES) are not covered by this skill — fiduciary rules differ from individual rules under N.D.C.C. Chapter 57-38.")_
- **R-NDES-02** — Pass-through entity (PTE) estimated tax  _("ND PTE estimated payments (Form 60-ES partnership / 58-ES S-corp) are not covered — PTE tax election rules require a separate skill.")_
- **R-NDES-03** — Corporate estimated tax (Form 40-ES)  _("Corporate estimated tax (Form 40-ES, Form 40-UT for corporate underpayment) is not covered — this skill is individual only.")_
- **R-NDES-04** — Part-year resident or nonresident  _("Part-year and nonresident estimated tax involves Schedule ND-1NR allocation; outside this skill. See nd-income-tax.md scope notes.")_
- **R-NDES-05** — Farm-income averaging interaction  _("Detailed farm-income averaging and the qualified-farmer safe harbor under N.D. Admin Code 81-03-04-02(3)(a)–(b) require specialist review.")_
- **R-NDES-06** — Pre-TY 2024 or prior-year amended estimates  _("This skill covers TY 2025 only. Older or amended quarterly computations require historical rate tables outside scope.")_
- **R-NDES-07** — Reasonable-cause waiver drafting  _("We will not draft the signed reasonable-cause statement — taxpayer or their representative must compose, sign, and submit.")_

## Section 15: Form mapping

**Form mapping table**

| Output | Form / Line | Notes |
| --- | --- | --- |
| Each quarterly payment | Form ND-1ES voucher (one per installment) or TAP electronic | Paper voucher only required when paying by check |
| Annual reconciliation | Form ND-1, Line 27 (Estimated payments) [VERIFY current 2025 line number] | Sum of four quarterly ND-1ES payments |
| Withholding reconciliation | Form ND-1, Line 26 (ND income tax withheld) | W-2 Box 17 + ND-source 1099 withholding |
| Underpayment interest | Schedule ND-1UT, flows to Form ND-1 balance due line | Attach Schedule ND-1UT to ND-1 |
| Annualized-method support | Federal Schedule AI attached to Schedule ND-1UT | ND does not publish standalone state annualization schedule |
| Federal coordination | Form 1040-ES (federal) | Same April/June/September/January 15 calendar |
| Federal annualized | Federal Form 2210, Schedule AI | Drives ND interest waiver per Admin Code 81-03-04-02(3)(c) |

## Section 16: Sources and provenance

### Statutes and regulations

- **N.D.C.C. §57-38-62** — Estimated tax statute (individual) https://ndlegis.gov/cencode/t57c38.html
- **N.D. Admin Code 81-03-04-01** — Estimated tax — general https://ndlegis.gov/prod/acdata/pdf/81-03-04.pdf
- **N.D. Admin Code 81-03-04-02** — Payments of estimated taxes by individuals, estates, and trusts https://www.law.cornell.edu/regulations/north-dakota/N-D-A-C-81-03-04-02

### Forms (TY 2025)

- **Form ND-1ES** — Estimated Income Tax — Individuals https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2024-iit/28709-form-nd-1es-2025.pdf
- **Schedule ND-1UT** — Underpayment of Estimated Individual Income Tax (SFN 28704) https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28704-schedule-nd-1ut-2025.pdf
- **2025 Individual Income Tax Booklet** https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf

### Payment portal

- **ND Taxpayer Access Point (TAP)** — https://apps.nd.gov/tax/tap

### Federal counterparts

- **IRC §6654** — Failure by individual to pay estimated income tax
- **Form 1040-ES** — Estimated Tax for Individuals
- **Form 2210, Schedule AI** — Annualized Income Installment Method

### Verification markers in this draft

The following items are tagged **[VERIFY]** and must be confirmed against the current 2025 ND Tax Commissioner publications before reliance:

1. The $1,000 threshold on current-year expected liability (vs. prior-year)
2. Absence of a 110% high-income variant on the prior-year safe harbor
3. The 12% per-annum underpayment interest rate for TY 2025
4. The Bismarck mailing PO Box on the 2025 ND-1ES voucher
5. Current 2025 Form ND-1 line numbers (27 estimated, 26 withholding)
6. The annualized installment cap mechanic on Schedule ND-1UT
7. Reasonable-cause waiver administrative process
8. Absence of an electronic-payment mandate for individual estimated tax
9. TY 2025 PIT bracket schedule interaction with safe harbor (HB 1158 phase-down)

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
