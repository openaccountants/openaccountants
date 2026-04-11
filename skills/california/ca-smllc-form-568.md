---
name: ca-smllc-form-568
description: Tier 2 California content skill for preparing California Form 568 (Limited Liability Company Return of Income) for single-member LLCs disregarded for federal tax purposes but treated as separate entities by California for the $800 annual franchise tax and the gross receipts-based LLC fee. Covers tax year 2025 including the $800 minimum franchise tax (R&TC section 17941), the tiered LLC fee schedule (R&TC section 17942), first-year exemption rules, Form 3522 (LLC Tax Voucher), Form 3536 (Estimated Fee), Schedule B balance sheet requirements, and penalty and interest computations. Defers individual income tax to ca-540-individual-return and estimated personal tax to ca-estimated-tax-540es. MUST be loaded alongside us-tax-workflow-base v0.1 or later. California SMLLCs only.
version: 0.2
---

# CA SMLLC Form 568 Skill v0.2

## What this file is, and what it is not

**This file is a content skill that loads on top of `us-tax-workflow-base` v0.1.** It provides the California Form 568 filing rules for single-member LLCs (SMLLCs) that are disregarded for federal income tax purposes but are treated as separate entities by California for the annual franchise tax and LLC fee. This skill does NOT compute the owner's personal California income tax (handled by `ca-540-individual-return`) or California estimated personal income tax payments (handled by `ca-estimated-tax-540es`).

**Tax year coverage.** This skill is current for **tax year 2025** as of its currency date (April 2026). It reflects California Revenue and Taxation Code sections 17941 and 17942 as in force for 2025.

**Key concept.** A single-member LLC is disregarded for federal tax (activity reported on Schedule C). But California treats the LLC as a separate entity subject to: (1) an $800 annual franchise tax, and (2) a gross receipts-based LLC fee if total income exceeds $250,000. The SMLLC must file Form 568 with the FTB.

---

## Section 1 -- Scope statement

This skill covers California Form 568 for tax year 2025 for entities that are:

- Single-member LLCs organized in California OR doing business in California
- Disregarded for federal income tax purposes (activity flows to owner's Schedule C)

For the following kinds of work:

- Determining the $800 annual franchise tax obligation
- Computing the LLC fee based on total California income
- Preparing Form 568 (LLC Return of Income)
- Preparing Form 3522 (LLC Tax Voucher) for the $800 payment
- Preparing Form 3536 (Estimated Fee for LLCs) for the LLC fee
- Determining first-year exemption eligibility
- Identifying Schedule B (Balance Sheet) requirements
- Computing penalties and interest for late filing or late payment

This skill does NOT cover:

- Multi-member LLCs (Form 568 for partnerships -- out of scope)
- LLCs taxed as corporations (Form 100 -- out of scope)
- The owner's personal California income tax -- handled by `ca-540-individual-return`
- California estimated personal income tax -- handled by `ca-estimated-tax-540es`
- Federal SMLLC treatment -- handled by federal skills

---

## Section 2 -- Year coverage and currency

**Tax year covered:** 2025 (Form 568 due March 15, 2026 for calendar-year filers, or the 15th day of the 3rd month after the close of the fiscal year; extended to September 15, 2026 with Form 7004).

**Currency date:** April 2026.

**Legislation reflected:**
- R&TC section 17941 -- $800 annual franchise tax
- R&TC section 17942 -- LLC fee schedule
- R&TC section 17948 -- first-year exemption
- R&TC section 19131 -- late filing penalty
- R&TC section 19132 -- late payment penalty
- AB 85 (2020) / AB 150 (2021) -- first-year exemption for LLCs (verify current status for 2025)
- FTB Form 568 Instructions (2025)
- FTB Form 3522 Instructions (2025)
- FTB Form 3536 Instructions (2025)

---

## Section 3 -- Year-specific figures table for tax year 2025

### Annual franchise tax

| Figure | Value | Source |
|---|---|---|
| Annual franchise tax (minimum) | $800 | R&TC section 17941(a) |
| Due date for $800 tax | April 15 of the tax year (i.e., April 15, 2025 for TY2025) | R&TC section 17941; FTB instructions |
| Payment method | Form 3522 (LLC Tax Voucher) or Web Pay | FTB |

**Critical timing note:** The $800 franchise tax for tax year 2025 is due on April 15, 2025 -- the BEGINNING of the tax year, not the end. This is a prepayment, not a year-end obligation. Form 3522 is used for this payment.

### LLC fee schedule (based on total income) (verify 2025)

| Total income from California sources | LLC fee |
|---|---|
| Less than $250,000 | $0 |
| $250,000 -- $499,999 | $900 |
| $500,000 -- $999,999 | $2,500 |
| $1,000,000 -- $4,999,999 | $6,000 |
| $5,000,000 and above | $11,790 |

**"Total income" definition:** Total income means gross income plus cost of goods sold. For an SMLLC, this is generally the total revenue of the business (not net profit). This is a critical distinction -- a business with $300,000 gross revenue and $280,000 expenses (net profit $20,000) still owes the $900 LLC fee because total income is $300,000.

### LLC fee payment timing

| Item | Due date | Form |
|---|---|---|
| Estimated LLC fee | June 15, 2025 (for calendar year) | Form 3536 |
| Final LLC fee (balance due) | March 15, 2026 (with Form 568) | Form 568 |

### First-year exemption (verify 2025)

| Figure | Value | Source |
|---|---|---|
| First-year $800 tax exemption | Available for LLCs formed on or after January 1, 2021, for their first taxable year | AB 85 (2020); R&TC section 17948 |
| First-year LLC fee exemption | The LLC fee is NOT exempt in the first year -- only the $800 franchise tax is exempt | R&TC section 17948; FTB guidance |
| Sunset of first-year exemption | The exemption was enacted for tax years beginning on or after January 1, 2021 and before January 1, 2024. (verify whether extended to 2025) | AB 85 / AB 150 |

**Critical verification:** The first-year $800 exemption was originally enacted for tax years 2021-2023 under AB 85. AB 150 (2021) may have extended it. Verify whether the exemption is still available for LLCs formed in 2025. If the exemption has expired, the $800 is due in the first year. **Flag for reviewer.**

### Penalties

| Penalty | Amount | Source |
|---|---|---|
| Late filing penalty | $18/month (per member, per month, up to 12 months). For SMLLC: $18/month x 1 member = $18/month, max $216. | R&TC section 19172 |
| Late payment penalty (franchise tax) | 5% + 0.5%/month (up to 25%) of unpaid tax | R&TC section 19132 |
| Late payment penalty (LLC fee) | 10% of unpaid fee | R&TC section 19132.5 |
| Underpayment of estimated fee penalty | Interest on underpayment from June 15 to payment date | R&TC section 19142 |
| Interest rate | Varies; set by FTB quarterly (verify 2025 rate) | R&TC section 19521 |

---

## Section 4 -- Primary source library

| Source | Use |
|---|---|
| R&TC section 17941 | $800 annual franchise tax for LLCs |
| R&TC section 17942 | LLC fee based on total income |
| R&TC section 17946 | Definition of "doing business" in California |
| R&TC section 17948 | First-year exemption from $800 tax |
| R&TC section 17941(b)(2) | $800 not deductible against LLC fee |
| FTB Form 568 Instructions (2025) | Line-by-line filing instructions |
| FTB Form 3522 (2025) | LLC Tax Voucher |
| FTB Form 3536 (2025) | Estimated Fee for LLCs |
| FTB Publication 3556 | LLC Filing Information |
| IRC section 301.7701-3 | Check-the-box: SMLLC as disregarded entity |

---

## Section 5 -- Form 568 preparation

### 5.1 -- Who must file

An SMLLC must file Form 568 if ANY of the following apply:
- The LLC is organized in California, OR
- The LLC is registered to do business in California, OR
- The LLC is "doing business" in California (R&TC section 17946):
  - Actively engaging in transactions for financial gain in CA, OR
  - Organized in CA, OR
  - Having CA-source income, OR
  - Exceeding the "doing business" thresholds: $735,019 property in CA, $735,019 payroll in CA, $735,019 CA sales, or 25% of total sales are CA sales (verify 2025 thresholds)

### 5.2 -- Key Form 568 components

| Component | Description |
|---|---|
| Side 1 | General information: LLC name, EIN/FEIN, SOS number, business activity codes |
| Side 2 | Income and deductions (mirrors Schedule C but for CA purposes) |
| Side 3 | Schedule B (Balance Sheet) -- required if total assets or total liabilities ≥ specified threshold (verify) |
| Side 4 | Schedule K (Members' Shares) -- for SMLLC, 100% to single member |
| Schedule IW | LLC Income Worksheet -- used to compute total income for the LLC fee |

### 5.3 -- Schedule IW (LLC fee computation)

The LLC fee is based on "total income" computed on Schedule IW:

1. Start with total income from all sources (gross receipts or sales, minus returns/allowances, plus other income).
2. For SMLLCs, this generally matches Schedule C gross income (Line 7 of Schedule C) plus any other income items.
3. Apply the fee schedule from Section 3.
4. **Total income is NOT net income.** Cost of goods sold is subtracted, but operating expenses are NOT.
5. If the LLC has income from both California and non-California sources, only California-source income is used for the fee (but see apportionment rules for multi-state LLCs).

### 5.4 -- $800 franchise tax treatment

- The $800 franchise tax is NOT deductible against the LLC fee (they are separate obligations).
- The $800 franchise tax IS deductible as a business expense on the owner's Schedule C (federal) and on the CA return.
- The $800 is due on the 15th day of the 4th month of the taxable year (April 15 for calendar year).
- If the LLC existed at any point during the year, the $800 is owed for that year (pro-ration is not available).

### 5.5 -- Cancellation / dissolution

- If the LLC was cancelled or dissolved during the year, Form 568 is still required for the short period.
- The $800 franchise tax is still owed for the year of cancellation.
- File the final Form 568, check the "final return" box, and include Form 3522 for the final year.
- To avoid the $800 for the FOLLOWING year, cancel before the end of the current year.

---

## Section 6 -- PROHIBITIONS

**P-568-1.** NEVER confuse the $800 franchise tax with the LLC fee. They are separate obligations under different R&TC sections (17941 and 17942). Both may be owed.

**P-568-2.** NEVER compute the LLC fee using net income. The fee is based on TOTAL income (gross receipts less cost of goods sold, NOT less operating expenses).

**P-568-3.** NEVER skip Form 568 because the LLC had no income. If the LLC existed and was organized in CA or doing business in CA, Form 568 and the $800 franchise tax are owed regardless of income.

**P-568-4.** NEVER assume the first-year $800 exemption is still in effect without verifying current law. The exemption was enacted for 2021-2023 and may have expired for 2025. Flag for reviewer.

**P-568-5.** NEVER file Form 568 using the individual owner's SSN as the primary identifier. The LLC should have its own EIN. If it does not, obtain one before filing.

**P-568-6.** NEVER report the LLC fee payment as due on April 15. The estimated LLC fee is due on June 15 (Form 3536). Only the $800 franchise tax is due April 15 (Form 3522).

**P-568-7.** NEVER advise the taxpayer that dissolving the LLC mid-year eliminates the $800 for that year. The $800 is owed for any year the LLC existed, even for one day.

**P-568-8.** NEVER double-count the $800 franchise tax and LLC fee as a single payment. They are paid on different forms (3522 and 3536/568) at different times.

---

## Section 7 -- Edge Cases

### EC-568-1 -- New LLC formed in 2025, first-year exemption expired

**Situation:** Sole proprietor forms a California SMLLC on February 1, 2025. The first-year $800 exemption has expired (was for 2021-2023 only).

**Resolution:**
- The $800 franchise tax is owed for 2025. Due April 15, 2025 (Form 3522).
- If the LLC has total income exceeding $250,000, the LLC fee is also owed.
- Form 568 is due March 15, 2026.
- **Flag for reviewer:** Confirm whether the first-year exemption was extended past 2023.

### EC-568-2 -- LLC with high gross revenue but low net profit

**Situation:** SMLLC has $600,000 in gross receipts, $550,000 in operating expenses. Net profit is $50,000.

**Resolution:**
- Total income for LLC fee purposes = $600,000 (gross receipts, not net profit). If no COGS, total income = $600,000.
- LLC fee = $2,500 (income in $500K-$999K bracket).
- The $2,500 fee is owed despite the business earning only $50,000 in net profit.
- Plus $800 franchise tax.
- Total California entity-level cost: $3,300.
- **Flag for reviewer:** If the LLC has COGS, subtract COGS from gross receipts for the Schedule IW computation. Operating expenses are NOT subtracted.

### EC-568-3 -- LLC cancelled mid-year

**Situation:** SMLLC cancels with the Secretary of State on June 30, 2025.

**Resolution:**
- File a final Form 568 for the short period January 1 -- June 30, 2025.
- $800 franchise tax is owed for 2025 (the year of cancellation).
- LLC fee is computed on total income for the short period.
- To avoid the $800 for 2026, the cancellation must be effective before December 31, 2025. In this case it is, so no 2026 $800 is owed.
- Check the "final return" box on Form 568.

### EC-568-4 -- Out-of-state LLC doing business in California

**Situation:** Delaware-organized SMLLC has California customers generating $400,000 in California-source income. The LLC is not registered in California.

**Resolution:**
- The LLC is "doing business" in California under R&TC section 17946 (CA-source income exceeds the threshold).
- Must register with the CA Secretary of State (if not already), file Form 568, pay $800 franchise tax, and pay the LLC fee based on CA-source total income.
- LLC fee: $900 (income $250K-$499K range).
- Failure to register and file subjects the LLC to penalties and back taxes.
- **Flag for reviewer:** Out-of-state LLCs "doing business" in CA face the same obligations as CA-organized LLCs.

### EC-568-5 -- Estimated fee underpayment

**Situation:** LLC estimated total income of $200,000 in June 2025 and did not file Form 3536 (no fee estimated since under $250K). Actual total income was $300,000.

**Resolution:**
- Actual LLC fee owed = $900 (income $250K-$499K).
- No Form 3536 was filed by June 15. The $900 is now due with Form 568 on March 15, 2026.
- Underpayment penalty: interest on $900 from June 15, 2025 to payment date.
- **Flag for reviewer:** Calculate interest at the FTB's quarterly rate.

### EC-568-6 -- SMLLC with both W-2 payroll and Schedule C income

**Situation:** SMLLC pays the owner a salary (improperly -- disregarded entities typically do not pay W-2 to the owner for federal purposes). LLC also has Schedule C income.

**Resolution:**
- For federal purposes, a disregarded SMLLC owned by an individual cannot pay the owner a W-2 salary. This may indicate a classification error.
- For California Form 568, report all LLC income and deductions.
- The LLC fee is based on total income regardless of how compensation is structured.
- **Flag for reviewer:** Investigate whether the entity should be classified differently (e.g., S-corp election was intended).

### EC-568-7 -- LLC fee threshold boundary

**Situation:** SMLLC has gross receipts of $249,500. After subtracting COGS of $0, total income is $249,500.

**Resolution:**
- Total income is below $250,000. LLC fee = $0.
- Only the $800 franchise tax is owed.
- If income had been $500 higher, the fee would jump to $900.
- **Flag for reviewer:** Verify total income computation. Income items that are easy to overlook (interest, other income) could push total income over the threshold.

### EC-568-8 -- Late-formed LLC (December formation)

**Situation:** Sole proprietor forms a California SMLLC on December 1, 2025.

**Resolution:**
- $800 franchise tax is owed for 2025, even though the LLC existed for only one month.
- The $800 was technically due April 15, 2025, but the LLC did not exist then. FTB guidance: pay by the 15th day of the 4th month after formation (April 1, 2026 -- verify).
- Form 568 is due for the short period December 1-31, 2025.
- $800 franchise tax is ALSO owed for 2026 (due April 15, 2026).
- **Flag for reviewer:** Two $800 payments due within months of each other. Advise client of the cost of late-year formation.

---

## Section 8 -- Test Suite

### Test 568-1 -- Basic SMLLC, income under $250K

**Input:** California SMLLC, calendar year, total income $180,000. No first-year exemption.
**Expected:** $800 franchise tax (Form 3522, due April 15, 2025). LLC fee = $0 (under $250K). Form 568 due March 15, 2026. Total CA entity-level cost: $800.

### Test 568-2 -- SMLLC with LLC fee in $500K-$999K bracket

**Input:** California SMLLC, total income (gross receipts less COGS) = $750,000. No first-year exemption.
**Expected:** $800 franchise tax. LLC fee = $2,500. Estimated fee of $2,500 due June 15, 2025 (Form 3536). Total CA entity-level cost: $3,300.

### Test 568-3 -- High-income SMLLC

**Input:** California SMLLC, total income = $6,000,000.
**Expected:** $800 franchise tax. LLC fee = $11,790. Estimated fee due June 15 (Form 3536). Total CA entity-level cost: $12,590.

### Test 568-4 -- First-year LLC (exemption expired)

**Input:** New California SMLLC formed March 15, 2025. Total income = $100,000. First-year exemption expired after 2023.
**Expected:** $800 franchise tax owed (no exemption). LLC fee = $0 (under $250K). Total: $800. Form 568 due March 15, 2026.

### Test 568-5 -- LLC fee vs. net profit mismatch

**Input:** SMLLC with gross receipts $400,000, COGS $50,000, operating expenses $320,000. Net profit = $30,000.
**Expected:** Total income for LLC fee = $400,000 - $50,000 = $350,000. LLC fee = $900 (income $250K-$499K). The $30,000 net profit is irrelevant for fee computation. Total entity-level: $800 + $900 = $1,700.

### Test 568-6 -- Mid-year cancellation

**Input:** SMLLC cancels June 30, 2025. Total income for short period = $100,000.
**Expected:** $800 franchise tax owed for 2025. LLC fee = $0 (under $250K). Final Form 568 for short period. No 2026 $800 owed (cancellation effective before Dec 31).

### Test 568-7 -- Late filing penalty

**Input:** SMLLC files Form 568 four months late (July 15, 2026 instead of March 15, 2026). $800 paid on time.
**Expected:** Late filing penalty: $18/month x 1 member x 4 months = $72. No late payment penalty (tax was paid on time).

---

## Section 9 -- Self-checks

**Check 220 -- Form 568 filed for every SMLLC.** If the taxpayer operates through a California SMLLC, verify Form 568 is prepared.

**Check 221 -- $800 franchise tax accounted for.** Verify Form 3522 payment of $800 is documented. Verify due date (April 15, 2025 for TY2025).

**Check 222 -- LLC fee computed from total income, not net income.** Verify Schedule IW uses gross receipts less COGS, NOT net profit.

**Check 223 -- LLC fee bracket is correct.** Cross-check total income against fee schedule. Verify no income items were omitted (interest, other income).

**Check 224 -- Form 3536 estimated fee filed if applicable.** If total income was expected to exceed $250,000, verify Form 3536 was filed by June 15.

**Check 225 -- First-year exemption verified.** If LLC was formed in 2025, verify whether the first-year exemption is still in effect.

**Check 226 -- $800 deducted on federal Schedule C.** The $800 franchise tax is a deductible business expense. Verify it appears on the federal return.

**Check 227 -- Late filing/payment penalties computed if applicable.** If Form 568 or payments were late, compute penalties per Section 3.

**Check 228 -- EIN used on Form 568.** Verify the LLC files with its own EIN, not the owner's SSN.

---

## Section 10 -- Cross-skill references

**Inputs from:**
- `us-sole-prop-bookkeeping` -- gross receipts, COGS, business income for Schedule IW
- `us-schedule-c-and-se-computation` -- Schedule C net profit (for context, not for fee computation)

**Outputs to:**
- `ca-540-individual-return` -- $800 and LLC fee as deductible expenses
- `us-ca-return-assembly` -- Form 568, Form 3522, Form 3536 for final package

---

## Section 11 -- Known gaps

1. Multi-member LLC Form 568 is not supported (this skill is SMLLC only).
2. LLCs taxed as S-corps or C-corps use different forms (Form 100S, Form 100).
3. The exact first-year exemption status for LLCs formed in 2025 requires verification.
4. Multi-state apportionment for LLCs with income from multiple states is not fully detailed.
5. FTB interest rates for underpayment penalties change quarterly and must be looked up at filing time.

### Change log
- **v0.1 (April 2026):** Stub.
- **v0.2 (April 2026):** Full content skill with $800 franchise tax, LLC fee schedule, Form 568 preparation, edge cases, and test suite.

## End of skill


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
