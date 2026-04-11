---
name: uk-return-assembly
description: Final orchestrator skill that assembles the complete UK filing package for UK-resident sole traders. Consumes outputs from all UK content skills (uk-vat-return for VAT100, uk-self-employment-sa103 for trading income, uk-income-tax-sa100 for personal tax, uk-national-insurance for Class 2+4 NIC, uk-student-loan-repayment for student loan, uk-payments-on-account for payments on account) to produce a single unified reviewer package containing every worksheet, every form, every brief section, all cross-skill reconciliations, and the final action list with payment instructions, filing instructions, and next-year planning. This is the capstone skill that runs last and produces the final deliverable. MUST be loaded alongside all UK content skills listed above. UK full-year residents only. Sole traders only.
version: 0.1
---

# UK Return Assembly Skill v0.1

## CRITICAL EXECUTION DIRECTIVE -- READ FIRST

**When this skill is invoked, you have already passed through intake. The user has consented to the full workflow. Execute all steps without pausing for permission.**

Specifically:

- **Do NOT ask the user "how deep do you want me to go"** or "do you want the full package" or any variant. The user asked for their tax returns. They want their tax returns. Produce them.
- **Do NOT announce how many tokens or tool calls this will take.** Execute.
- **Do NOT ask which deliverables to prioritise.** Produce all deliverables listed in Section 4. If you run out of context mid-execution, finish the computation work first (numbers, positions, flags) then produce whatever formatted outputs you can, and at the very end state clearly which deliverables were not produced and why.
- **Do NOT re-validate scope that intake already validated.** If `uk-freelance-intake` produced an intake package, trust it. You can cross-check specific numbers during reconciliation but do not re-interrogate the user about residency, business structure, or anything else intake already captured.
- **Do NOT pause between content skills to check in.** Run them in dependency order (Section 2) without prose status updates between each one. A single status message at the end is fine.
- **Self-checks are targets, not blockers.** If a self-check fails, note it in the reviewer brief's open flags section and continue. Do NOT halt the entire workflow because one self-check had an ambiguous answer.
- **Primary source citations go in the final reviewer brief, not in intermediate computation steps.**

**The user has already been told (by the intake skill) that the final package requires chartered accountant signoff before filing. State it once in the final output and move on.**

**Failure mode to avoid:** The skill halts mid-execution and asks the user a meta-question about workflow pacing. If you feel the urge to ask "how should I proceed," the correct action is to pick the most defensible path and proceed, flagging the decision in the reviewer brief so the reviewer can challenge it.

---

## What this file is

The final capstone skill for UK sole trader returns. Every UK content skill feeds into this one. The output is the complete reviewer package that a chartered accountant can review, sign off on, and deliver to the client along with filing instructions.

This skill coordinates execution of the content skills, verifies cross-skill consistency, and assembles the final deliverable.

---

## Section 1 -- Scope

Produces the complete UK filing package for:
- Full-year UK residents
- Sole traders (self-employed individuals)
- Tax year 2025/26 (6 April 2025 to 5 April 2026)
- Filing SA100 with SA103 (self-employment), VAT100 (if VAT registered), Class 2+4 NIC, student loan repayment (if applicable), payments on account for 2026/27

---

## Section 2 -- Execution order and dependency chain

The skill enforces the following execution order:

1. **`uk-vat-return`** -- VAT100 return (if VAT registered)
   - Runs first because VAT turnover figures feed into the SA103
   - For standard registration: prepare outstanding quarterly VAT100; verify prior quarters
   - For Flat Rate Scheme: apply FRS percentage to gross turnover (including VAT)
   - For unregistered: skip. Verify turnover stays under GBP 90,000 rolling 12-month threshold.
   - Output: VAT100 box values, input VAT recovered (standard) or FRS saving, turnover (ex-VAT)

2. **`uk-self-employment-sa103`** -- SA103 self-employment pages (trading income)
   - Depends on VAT output: turnover on SA103 must be ex-VAT for VAT-registered traders
   - Covers: turnover (Box 15/16), allowable expenses (Boxes 17-30), net profit (Box 31), capital allowances (Box 34), adjustments
   - Cash basis vs accruals: affects timing of income and expense recognition
   - Output: SA103 box values, net profit for tax computation, capital allowances schedule

3. **`uk-income-tax-sa100`** -- SA100 main return (personal tax computation)
   - Depends on SA103: net self-employment profit enters the SA100 as self-employment income
   - Depends on P60: employment income and PAYE tax deducted
   - Covers: total income, personal allowance (GBP 12,570, tapered above GBP 100,000), tax computation at applicable rates (rUK or Scottish), marriage allowance
   - Output: total income, taxable income, income tax liability, tax already paid (PAYE + POA), balancing payment/refund

4. **`uk-national-insurance`** -- Class 2 + Class 4 NIC
   - Depends on SA103: net self-employment profit feeds Class 4 NIC computation
   - Class 2: flat rate GBP 3.45/week (GBP 179.40/year) if profits above Small Profits Threshold (GBP 6,725) -- voluntary below threshold
   - Class 4: 6% on profits between GBP 12,570 and GBP 50,270; 2% above GBP 50,270
   - Output: Class 2 amount, Class 4 amount, total NIC due via Self Assessment

5. **`uk-student-loan-repayment`** -- Student loan repayment via Self Assessment (if applicable)
   - Depends on SA100: total income determines repayment amount
   - Plan 1: 9% above GBP 22,015; Plan 2: 9% above GBP 27,295; Plan 4: 9% above GBP 27,660; Plan 5: 9% above GBP 25,000; Postgraduate: 6% above GBP 21,000
   - Deduct repayments already made via PAYE
   - **Status check:** uk-student-loan-repayment may be a Q4 stub. If the stub has substantive content, use it. If placeholder, compute using the thresholds above and flag in the reviewer brief.
   - Output: total repayment due, amount via PAYE, amount via SA

6. **`uk-payments-on-account`** -- Payments on account for 2026/27
   - Depends on SA100: payments on account are based on current year's SA liability
   - **Status check:** uk-payments-on-account is currently a Q4 stub. If the stub has substantive content, use it. If placeholder, compute: each POA = 50% of current year SA liability (income tax + Class 4 NIC, excluding PAYE, Class 2, student loan, capital gains tax). Due 31 January 2027 (1st POA) and 31 July 2027 (2nd POA). Flag in the reviewer brief.
   - If SA liability < GBP 1,000, or > 80% was collected at source (PAYE), no POA required.
   - Output: two POA amounts and dates for 2026/27

If any upstream content skill fails to produce validated output, the assembly skill notes the failure in the reviewer brief and continues with available data rather than halting entirely.

---

## Section 3 -- Cross-skill reconciliation

### Cross-check 1: SA103 net profit = SA100 self-employment income

| SA103 Output | SA100 Input | Rule |
|-------------|-----------|------|
| SA103 Box 31 (net profit) or Box 32 (net loss) | SA100 self-employment income field | Must match exactly |
| SA103 turnover (Box 15/16) | Must be ex-VAT (if VAT registered) | VAT collected is not turnover on SA103 |

**If mismatch:** Flag for reviewer. Common causes: timing difference between VAT period and tax year (VAT quarters don't align with 6 Apr-5 Apr), adjustments for private use.

### Cross-check 2: SA103 net profit feeds Class 4 NIC computation

| NIC Input | Source | Rule |
|-----------|--------|------|
| Net self-employment profit | SA103 Box 31 | Class 4 base = net profit |
| Class 4: 6% on GBP 12,570-50,270 | SA103 net profit | Lower profits limit = GBP 12,570, upper profits limit = GBP 50,270 |
| Class 4: 2% above GBP 50,270 | SA103 net profit | No cap |

**If mismatch:** Verify SA103 net profit figure. If multiple self-employments, combine profits for NIC purposes.

### Cross-check 3: Payments on account = 50% of prior year SA balance

| POA Input | Source | Rule |
|----------|--------|------|
| Prior year total SA liability | Prior year SA302 | Relevant amount = income tax + Class 4 NIC via SA |
| Less: PAYE tax deducted | P60 / prior year SA302 | PAYE deducted from the relevant amount |
| Less: Class 2 NIC | Excluded from POA computation | Class 2 does not count toward POA |
| Less: student loan | Excluded from POA computation | Student loan does not count toward POA |
| Each POA = 50% of (relevant amount - PAYE) | | If result < GBP 1,000 total, no POA required |

**If mismatch:** Common cause is first year of self-employment (no POA due), or claim to reduce POA (SA303).

### Cross-check 4: VAT turnover consistency with SA103

| VAT Output | SA103 Input | Rule |
|-----------|-----------|------|
| VAT100 Box 6 (total sales ex-VAT) | SA103 Box 15/16 (turnover) | Should broadly match, adjusted for VAT period vs tax year timing |
| FRS: gross turnover x FRS% = VAT payable | SA103 turnover = gross ex-VAT (not FRS adjusted) | SA103 uses actual turnover, not FRS calculation |

**If mismatch:** VAT periods (quarters ending Mar/Jun/Sep/Dec) don't perfectly align with the tax year (6 Apr-5 Apr). Small timing differences are expected. Large differences need investigation.

### Cross-check 5: Student loan computation consistent with total income

| Student Loan Input | Source | Rule |
|-------------------|--------|------|
| Total income from SA100 | SA100 total income field | Repayment based on total income minus threshold |
| Repayments via PAYE | P60 student loan deductions | Deducted from total repayment due |
| Net repayment via SA | Total - PAYE deductions | Cannot be negative (no refund of SL via SA) |

**If no student loan:** This cross-check does not apply. Skip.

---

## Section 4 -- Final reviewer package contents

### Documents

1. **Executive summary** -- one-page overview: filing status, income, tax liability, VAT position, NIC, student loan, payments on account, balancing payment/refund
2. **VAT100 worksheet** (if VAT registered) -- box-by-box with formulas
3. **SA103 worksheet** -- self-employment pages Box 15 through Box 52 with formulas and supporting schedules
4. **SA100 computation** -- total income, personal allowance, taxable income, tax at applicable rates, NIC, student loan, less PAYE/POA, balancing payment
5. **Capital allowances schedule** -- asset register with cost, date, AIA/WDA, annual allowance, WDV
6. **NIC computation** -- Class 2 + Class 4 breakdown
7. **Student loan computation** (if applicable) -- plan, threshold, repayment due, PAYE offset
8. **Payments on account schedule** -- 2026/27 two-instalment calculation
9. **Cross-skill reconciliation summary** -- all five cross-checks with pass/fail and notes
10. **Reviewer brief** -- comprehensive narrative with positions, citations, flags, self-check results
11. **Client action list** -- what the client needs to do, with dates and amounts

### Reviewer brief contents

```markdown
# Complete Return Package: [Client Name] -- Tax Year 2025/26

## Executive Summary
- Filing status: [Single / Married / Civil partner]
- Residence: UK (full-year)
- Scottish taxpayer: [Yes / No]
- Business: Sole trader
- VAT status: Standard / Flat Rate Scheme / Unregistered
- Accounting basis: Cash / Accruals
- VAT position (Q4 or annual): GBP X due / GBP X refund
- SA103 net profit (Box 31): GBP X
- SA100 total income: GBP X
- Personal allowance: GBP X
- Income tax liability: GBP X
- Class 2 NIC: GBP X
- Class 4 NIC: GBP X
- Student loan repayment via SA: GBP X
- Total SA liability: GBP X
- Tax already paid (PAYE + POA): GBP X
- Balancing payment / refund: GBP X
- 2026/27 payments on account: GBP X each (x2)

## VAT Return
[Content from uk-vat-return output]
- Registration type and period
- Output VAT summary (standard rated, zero rated, exempt, outside scope)
- Input VAT summary (reclaimable, blocked)
- FRS computation (if applicable)
- Box-by-box summary
- VAT due / refund

## Self-Employment (SA103)
[Content from uk-self-employment-sa103 output]
- Box 15/16: Turnover breakdown by client
- Box 17-30: Allowable expenses schedule
- Box 31: Net profit
- Box 34: Capital allowances (AIA, WDA, balancing charges)
- Cash basis adjustments (if applicable)
- Simplified expenses used (if applicable)

## Income Tax (SA100)
[Content from uk-income-tax-sa100 output]
- Self-employment income (from SA103)
- Employment income (from P60, if any)
- Other income (interest, dividends, rental)
- Total income
- Personal allowance (GBP 12,570, tapered if income > GBP 100,000)
- Taxable income
- Tax at rUK or Scottish rates
- Marriage allowance (if applicable)
- Tax already deducted (PAYE)
- Net tax liability

## National Insurance
[Content from uk-national-insurance output]
- Class 2: GBP 3.45/week, GBP 179.40/year (if profits > GBP 6,725)
- Class 4: 6% on GBP 12,570-50,270 = GBP X
- Class 4: 2% above GBP 50,270 = GBP X
- Total NIC via Self Assessment: GBP X
- Class 1 already paid via PAYE (informational): GBP X

## Student Loan (if applicable)
[Content from uk-student-loan-repayment output, or computed if stub]
- Plan type: [Plan 1/2/4/5/Postgraduate]
- Repayment threshold: GBP X
- Total repayment due: GBP X
- Less: repaid via PAYE: GBP X
- Net repayment via SA: GBP X

## Payments on Account (2026/27)
[Content from uk-payments-on-account output, or computed if stub]
- Based on 2025/26 SA liability (income tax + Class 4 NIC, less PAYE)
- 1st POA: 31 January 2027 -- GBP X (50%)
- 2nd POA: 31 July 2027 -- GBP X (50%)
- POA not required if total SA liability < GBP 1,000 or > 80% deducted at source

## Cross-skill Reconciliation
- SA103 net profit vs SA100 self-employment income: [pass/fail]
- SA103 net profit vs Class 4 NIC base: [pass/fail]
- POA vs prior year SA liability: [pass/fail]
- VAT turnover vs SA103 turnover: [pass/fail]
- Student loan vs total income: [pass/fail] (or N/A)

## Reviewer Attention Flags
[Aggregated from all upstream skills]
- T2 items requiring chartered accountant confirmation
- Mixed-use expense percentages (vehicle, phone, broadband)
- Use of home claim (simplified or actual)
- Capital allowances: AIA vs WDA vs small pools
- Cash basis appropriateness (turnover under GBP 150,000?)
- Simplified expenses elections
- Scottish taxpayer determination
- Personal allowance taper (if total income approaches GBP 100,000)
- Marriage allowance eligibility
- VAT registration threshold monitoring (approaching GBP 90,000)
- Student loan plan type confirmation
- CIS deductions (if Construction Industry Scheme applies)

## Positions Taken
[List with legislation citations]
- e.g., "Use of home simplified rate GBP 26/month (101+ hours) -- ITTOIA 2005 s94H"
- e.g., "Motor vehicle simplified expenses 45p/mile x 8,000 miles = GBP 3,600 -- ITTOIA 2005 s94D"
- e.g., "MacBook Pro GBP 1,800 claimed under AIA -- CAA 2001 s51A"
- e.g., "Cash basis elected -- ITTOIA 2005 s25A, turnover under GBP 150,000"
- e.g., "Class 2 NIC GBP 179.40 -- SSCBA 1992 s11(2)"
- e.g., "Class 4 NIC 6%/2% -- SSCBA 1992 s15"
- e.g., "Student loan Plan 2 repayment 9% above GBP 27,295 -- Education (Student Loans) (Repayment) Regulations 2009"

## Planning Notes for 2026/27
- Payments on account schedule (two instalments with amounts and dates)
- VAT threshold monitoring (if approaching GBP 90,000)
- Capital allowances pool WDV carried forward
- Cash basis threshold monitoring (if approaching GBP 150,000)
- Any legislative changes affecting 2026/27 (NIC rate changes, threshold changes)
- Class 2 NIC voluntary payment consideration (if below Small Profits Threshold)

## Client Action List

### Immediate (before 31 January 2027 -- SA filing and payment deadline):
1. Review this return package with your chartered accountant
2. File SA100 + SA103 online via HMRC Self Assessment portal
3. Pay balancing payment of GBP X to HMRC
4. Pay 1st payment on account 2026/27 of GBP X (same deadline)
5. File outstanding Q4 VAT return (if applicable)

### Before 31 July 2027:
1. Pay 2nd payment on account 2026/27 of GBP X

### VAT filing calendar (if VAT registered -- quarterly):
- Q1 2026/27 (Apr-Jun): file and pay by [date -- 1 month 7 days after quarter end]
- Q2 2026/27 (Jul-Sep): file and pay by [date]
- Q3 2026/27 (Oct-Dec): file and pay by [date]
- Q4 2026/27 (Jan-Mar): file and pay by [date]

### If claim to reduce POA (SA303):
- If you expect 2026/27 income to be materially lower, you can apply to reduce POA via form SA303. Discuss with your accountant -- penalties apply if you reduce too much.

### Ongoing:
1. Issue VAT-compliant invoices for all sales (if VAT registered)
2. Retain all receipts and records (5 years from 31 January following the tax year)
3. Maintain mileage log if claiming simplified vehicle expenses
4. Track capital assets for capital allowances pool
5. Monitor turnover for VAT registration threshold (GBP 90,000 rolling 12 months)
6. File VAT returns quarterly via Making Tax Digital (MTD)
7. Prepare for MTD for Income Tax Self Assessment (ITSA) -- mandatory from April 2026 for businesses with turnover > GBP 50,000
```

---

## Section 5 -- Refusals

**R-UK-1 -- Upstream skill did not run.** Name the specific skill. Note: this is a warning, not a hard stop. Continue with available data and flag the gap.

**R-UK-2 -- Upstream self-check failed.** Name the specific check and note it in the reviewer brief. Continue.

**R-UK-3 -- Cross-skill reconciliation failed.** Name the specific reconciliation and describe the discrepancy. Flag for reviewer but continue.

**R-UK-4 -- Intake incomplete.** Specific missing intake items prevent computation. List what is missing and ask the user for the specific data point.

**R-UK-5 -- Out-of-scope item discovered during assembly.** E.g., rental income requiring SA105, capital gains requiring SA108, foreign income requiring SA106. Flag and exclude from computation.

---

## Section 6 -- Self-checks

**Check UK1 -- All upstream skills executed.** uk-vat-return (if VAT registered), uk-self-employment-sa103, uk-income-tax-sa100, uk-national-insurance all produced output. uk-student-loan-repayment produced output or was computed or was skipped (no loan). uk-payments-on-account produced output or was computed from SA liability.

**Check UK2 -- SA103 net profit matches SA100 self-employment income.** Exact match required.

**Check UK3 -- SA103 net profit feeds Class 4 NIC.** Class 4 computed on correct profit figure.

**Check UK4 -- Payments on account correctly computed.** Each POA = 50% of (income tax + Class 4 NIC - PAYE). Exclusions: Class 2, student loan, CGT.

**Check UK5 -- VAT treatment correct for registered traders.** Output VAT excluded from SA103 turnover; reclaimable input VAT excluded from SA103 expenses.

**Check UK6 -- VAT treatment correct for unregistered traders.** No VAT separation needed; gross amounts used throughout.

**Check UK7 -- Capital allowances correctly applied.** AIA on qualifying items (GBP 1,000,000 limit); WDA at 18% main pool / 6% special rate; small pools written off if WDV < GBP 1,000.

**Check UK8 -- Personal allowance correctly applied.** GBP 12,570 standard; tapered by GBP 1 for every GBP 2 above GBP 100,000; zero above GBP 125,140.

**Check UK9 -- Correct tax rate table applied.** Scottish rates if Scottish taxpayer; rUK rates otherwise.

**Check UK10 -- Filing calendar is complete.** All deadlines for VAT, SA, NIC, and POA are listed with specific dates and amounts.

**Check UK11 -- Class 2 NIC correctly determined.** Due if profits > Small Profits Threshold (GBP 6,725). Voluntary if below.

**Check UK12 -- Reviewer brief contains legislation citations.** Every position taken references the specific Act and section.

**Check UK13 -- Student loan plan type confirmed and correct threshold applied.** Plan 1/2/4/5/Postgraduate each have different thresholds.

**Check UK14 -- Cash basis vs accruals consistently applied.** If cash basis elected, no accruals adjustments appear in SA103. If accruals, debtors/creditors adjustments are present.

---

## Section 7 -- Output files

The final output is **three files**:

1. **`[client_slug]_2025-26_uk_master.xlsx`** -- Single master workbook containing every worksheet and form. Sheets include: Cover, VAT100 (quarterly, if applicable), SA103 (self-employment), SA100 (tax computation), Capital Allowances, Expense Detail, NIC Computation, Student Loan (if applicable), Payments on Account 2026/27, Cross-Check Summary. Use live formulas where possible -- e.g., SA100 self-employment income references the SA103 net profit cell; Class 4 NIC references the SA103 sheet; POA references the SA100 liability. Verify no `#REF!` errors. Verify computed values match the computation model within GBP 1 before shipping.

2. **`reviewer_brief.md`** -- Single markdown file covering all sections from Section 4 above: executive summary, VAT, SA103, SA100, NIC, student loan, POA, cross-skill reconciliation, flags, positions, planning notes.

3. **`client_action_list.md`** -- Single markdown file with step-by-step actions: immediate filings and payments, POA schedule, quarterly VAT calendar for 2026/27, ongoing compliance reminders.

**If execution runs out of context mid-build:** produce whatever is complete, then state at the end which of the three files were not produced or are partial.

**All files are placed in `/mnt/user-data/outputs/` and presented to the user via the `present_files` tool at the end.**

---

## Section 8 -- Cross-skill references

**Inputs:**
- `uk-freelance-intake` -- structured intake package (JSON)
- `uk-vat-return` -- VAT100 box values and classification output (if VAT registered)
- `uk-self-employment-sa103` -- SA103 box values and computation output
- `uk-income-tax-sa100` -- SA100 computation output
- `uk-national-insurance` -- Class 2 + Class 4 NIC output
- `uk-student-loan-repayment` -- Student loan computation output (or fallback, or N/A)
- `uk-payments-on-account` -- POA schedule (or fallback computation)

**Outputs:** The final reviewer package. No downstream skill.

---

## Section 9 -- Known gaps

1. PDF form filling is not automated. The reviewer uses the worksheets to file online via HMRC Self Assessment portal.
2. E-filing is handled by the reviewer via HMRC portal, not by this skill.
3. Payment execution is the client's responsibility; the skill only provides instructions and amounts.
4. SA102 (employment supplement) is partially supported -- employment income from P60 is included in SA100, but detailed SA102 boxes (benefits in kind, expenses) are not fully automated. Flag for chartered accountant.
5. Multi-year capital allowances tracking assumes the prior year pool balance is provided. If not, only current-year acquisitions are depreciated.
6. uk-student-loan-repayment is a Q4 stub. Until fleshed out, student loan is computed using the thresholds in Section 2 step 5. Deterministic per the Education (Student Loans) (Repayment) Regulations 2009.
7. uk-payments-on-account is a Q4 stub. Until fleshed out, POA is computed as 50% of SA liability. Deterministic per TMA 1970 s59A.
8. Foreign source income is out of scope (no SA106 / DTA relief).
9. Rental income (SA105) is out of scope.
10. Capital gains (SA108) are out of scope.
11. High Income Child Benefit Charge is not automatically computed -- flagged if income exceeds GBP 60,000.
12. The package is complete only for the 2025/26 tax year; 2026/27 appears only as prospective planning.
13. Making Tax Digital for ITSA (mandatory from April 2026 for turnover > GBP 50,000) may change quarterly reporting requirements -- flagged in planning notes.

### Change log
- **v0.1 (April 2026):** Initial draft. Modelled on mt-return-assembly v0.1 adapted for UK jurisdiction with six content skills (VAT100, SA103, SA100, NIC, student loan, payments on account).

## End of skill


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a chartered accountant, ACCA member, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
