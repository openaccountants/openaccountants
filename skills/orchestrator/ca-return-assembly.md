---
name: ca-return-assembly
description: Final orchestrator skill that assembles the complete Canadian filing package for Canadian-resident sole proprietors. Consumes outputs from all Canadian content skills (canada-gst-hst for GST34, ca-fed-t2125 for business income, ca-fed-t1-return for federal return, ca-fed-cpp-ei for CPP/CPP2/EI, ca-fed-instalments for instalment schedule) to produce a single unified reviewer package containing every worksheet, every form, every brief section, all cross-skill reconciliations, and the final action list with payment instructions, filing instructions, and next-year planning. This is the capstone skill that runs last and produces the final deliverable. MUST be loaded alongside all Canadian content skills listed above. Canadian full-year residents only. Sole proprietors only (not incorporated).
version: 0.1
---

# Canada Return Assembly Skill v0.1

## CRITICAL EXECUTION DIRECTIVE -- READ FIRST

**When this skill is invoked, you have already passed through intake. The user has consented to the full workflow. Execute all steps without pausing for permission.**

Specifically:

- **Do NOT ask the user "how deep do you want me to go"** or "do you want the full package" or any variant. The user asked for their tax returns. They want their tax returns. Produce them.
- **Do NOT announce how many tokens or tool calls this will take.** Execute.
- **Do NOT ask which deliverables to prioritise.** Produce all deliverables listed in Section 4. If you run out of context mid-execution, finish the computation work first (numbers, positions, flags) then produce whatever formatted outputs you can, and at the very end state clearly which deliverables were not produced and why.
- **Do NOT re-validate scope that intake already validated.** If `ca-freelance-intake` produced an intake package, trust it. You can cross-check specific numbers during reconciliation but do not re-interrogate the user about residency, business structure, or anything else intake already captured.
- **Do NOT pause between content skills to check in.** Run them in dependency order (Section 2) without prose status updates between each one. A single status message at the end is fine.
- **Self-checks are targets, not blockers.** If a self-check fails, note it in the reviewer brief's open flags section and continue. Do NOT halt the entire workflow because one self-check had an ambiguous answer.
- **Primary source citations go in the final reviewer brief, not in intermediate computation steps.**

**The user has already been told (by the intake skill) that the final package requires CPA/professional signoff before filing. State it once in the final output and move on.**

**Failure mode to avoid:** The skill halts mid-execution and asks the user a meta-question about workflow pacing. If you feel the urge to ask "how should I proceed," the correct action is to pick the most defensible path and proceed, flagging the decision in the reviewer brief so the reviewer can challenge it.

---

## What this file is

The final capstone skill for Canadian sole proprietor returns. Every Canadian content skill feeds into this one. The output is the complete reviewer package that a CPA or licensed tax professional can review, sign off on, and deliver to the client along with filing instructions.

This skill coordinates execution of the content skills, verifies cross-skill consistency, and assembles the final deliverable.

---

## Section 1 -- Scope

Produces the complete Canadian filing package for:
- Full-year Canadian residents
- Sole proprietors (unincorporated)
- Tax year 2025 (calendar year, fiscal year end December 31)
- Filing GST34 (if registered), T2125, T1 federal return, CPP/CPP2/EI calculation, instalment schedule, provincial tax

---

## Section 2 -- Execution order and dependency chain

The skill enforces the following execution order:

1. **`canada-gst-hst`** -- GST/HST return (GST34)
   - Runs first because GST/HST revenue figures feed into the T2125
   - For registered filers: prepare annual or outstanding quarterly/monthly GST34
   - Output: line 101 revenue, line 105 GST/HST collected, line 108 ITCs, line 109 net tax
   - **Status check:** canada-gst-hst is currently a Q2 skill. If it has substantive computation content, use it. If it is still a placeholder, compute GST34 figures from the intake package data and flag in the reviewer brief that the dedicated skill was not available.

2. **`ca-fed-t2125`** -- Statement of Business or Professional Activities
   - Depends on GST34 output: gross business income must be reported net of GST/HST for registered filers
   - Computes business expenses, CCA/immediate expensing, home office (Part 7), motor vehicle (Part 8)
   - Output: T2125 line values -- gross revenue (line 8299), total expenses (line 9368), net income/loss (line 9946)
   - **Status check:** ca-fed-t2125 is currently a Q2 skill. If it has substantive computation content, use it. If it is still a placeholder, compute T2125 figures from the intake package data and flag in the reviewer brief that the dedicated skill was not available.

3. **`ca-fed-t1-return`** -- Federal T1 individual return
   - Depends on T2125: net business income flows to T1 line 13500 (gross self-employment income) and line 13700 (net self-employment income)
   - Incorporates employment income (T4), other income, RRSP deduction, total income, taxable income, federal tax
   - Output: T1 line values through line 43500 (total payable) and line 48500 (balance owing/refund)
   - **Status check:** ca-fed-t1-return is currently a Q2 skill. If it has substantive computation content, use it. If it is still a placeholder, compute T1 figures from the intake package data and flag in the reviewer brief that the dedicated skill was not available.

4. **`ca-fed-cpp-ei`** -- CPP, CPP2, and EI self-employed
   - Depends on T2125: CPP pensionable earnings = T2125 net income (line 9946) minus CPP basic exemption ($3,500)
   - Self-employed pay both employee and employer portions of CPP (2 x 5.95% = 11.90% for 2025, on pensionable earnings up to YMPE minus basic exemption)
   - CPP2: second ceiling earnings between YMPE and YAMPE (2 x 4% for 2025)
   - EI: optional for self-employed (special benefits only); if opted in, pay employee rate only
   - Half of CPP (employee portion) is deducted from net income on T1 line 22200; the other half (employer portion) is a non-refundable credit on Schedule 8
   - Output: total CPP owing, CPP2 owing, EI (if opted in), deduction amount, credit amount
   - **Status check:** ca-fed-cpp-ei is currently a Q2 skill. If it has substantive computation content, use it. If it is still a placeholder, compute CPP/EI figures from the intake package data and flag in the reviewer brief that the dedicated skill was not available.

5. **`ca-fed-instalments`** -- Instalment schedule for 2026
   - Depends on T1: instalment base = net tax owing minus amounts withheld at source
   - If net tax owing exceeds $3,000 ($1,800 for Quebec), CRA will require instalments for the following year
   - Two methods: no-calculation option (use CRA's instalment reminders from NOA) or prior-year / current-year calculation
   - Output: quarterly instalment amounts and due dates for 2026 (March 15, June 15, September 15, December 15)
   - **Status check:** ca-fed-instalments is currently a Q4 stub. If the stub has substantive computation content, use it. If it is still a placeholder, compute instalment figures using the prior-year method and flag in the reviewer brief that the dedicated skill was not available.

6. **Provincial return**
   - For all provinces except Quebec: provincial tax is calculated on the federal T1 (Form 428 for the province)
   - For Quebec: separate TP-1 provincial return is required -- flag as Q4 stub. If the user is in Quebec, compute federal figures only and flag that the TP-1 must be prepared separately.
   - Output: provincial tax payable, provincial credits, surtaxes (Ontario surtax if applicable)
   - **Status check:** Provincial returns are Q4 stubs. Compute provincial tax using the province's rate schedule and flag in the reviewer brief that the dedicated skill was not available.

If any upstream content skill fails to produce validated output, the assembly skill notes the failure in the reviewer brief and continues with available data rather than halting entirely.

---

## Section 3 -- Cross-skill reconciliation

### Cross-check 1: GST34 revenue = T2125 gross business income (net of GST/HST)

| GST34 Output | T2125 Input | Rule |
|-------------|-------------|------|
| Line 101 total revenue | T2125 line 8299 gross revenue | Must match within $1 |
| Revenue is reported ex-GST/HST on GST34 line 101 | T2125 gross revenue is also ex-GST/HST | Both should be the same figure |
| Non-registered: no GST34 | T2125 line 8299 = gross receipts (no GST separation) | Direct match |

**If mismatch:** Flag for reviewer. Common causes: timing differences (cash vs accrual), GST/HST-exempt supplies, zero-rated supplies, personal amounts mixed into business account.

### Cross-check 2: T2125 net income feeds CPP pensionable earnings

| CPP Input | Source | Rule |
|----------|--------|------|
| Pensionable self-employment earnings | T2125 line 9946 (net income) | Minus $3,500 basic exemption |
| If also employed | T4 Box 26 (CPP pensionable earnings) | Reduces self-employed CPP if combined exceeds YMPE |
| YMPE (2025) | $71,300 (estimated -- confirm when CRA publishes) | Maximum pensionable earnings |
| YAMPE (2025) | $81,200 (estimated -- confirm when CRA publishes) | CPP2 second ceiling |

**If mismatch:** Verify T2125 net income is the correct figure. If taxpayer has both employment and self-employment income, combined CPP pensionable earnings are capped at YMPE.

### Cross-check 3: CPP half deducted from net income, half as credit

| CPP Treatment | T1 Line | Rule |
|--------------|---------|------|
| Employee portion (half of self-employed CPP) | Line 22200 (deduction from net income) | Reduces net income before taxable income |
| Employer portion (other half) | Schedule 8, then line 31000 (non-refundable credit) | 15% federal credit |
| CPP2 employee portion | Line 22215 | Additional deduction |
| CPP2 employer portion | Schedule 8 | Additional credit |

**If inconsistency:** The total CPP self-employed = 2 x employee rate. Half goes to line 22200, half to Schedule 8. Verify the split is correct.

### Cross-check 4: Instalments credit against final balance owing

| Instalment Input | Source | Rule |
|-----------------|--------|------|
| Instalments paid during 2025 | Bank statement / CRA My Account | T1 line 47600 (tax paid by instalments) |
| Tax deducted at source (T4) | T4 Box 22 | T1 line 43700 |
| Total credits | Sum of above | Reduces balance owing |
| Balance owing / refund | Line 48500 | Net tax owing minus all credits |

**If mismatch:** Common cause is missed instalment payments, or instalment amounts that don't match CRA's records. Verify against CRA My Account instalment statement.

### Cross-check 5: Provincial tax consistency

| Provincial Item | Source | Rule |
|----------------|--------|------|
| Taxable income | T1 line 26000 | Same for federal and provincial (except QC) |
| Provincial rate schedule | Province established at intake | Applied to taxable income |
| Provincial credits | Province-specific | BPA, provincial surtax (ON), etc. |
| For Quebec | Separate TP-1 | Different taxable income calculation |

**If inconsistency:** Verify province was correctly established. If taxpayer moved provinces during the year, province on December 31 determines which provincial tax applies.

---

## Section 4 -- Final reviewer package contents

### Documents

1. **Executive summary** -- one-page overview: filing status, business income, taxable income, federal tax, provincial tax, CPP/EI, RRSP, instalments, balance due/refund
2. **GST34 worksheet** -- line-by-line with formulas (revenue, GST/HST collected, ITCs, net tax)
3. **T2125 worksheet** -- line-by-line with formulas (revenue, expenses, CCA, home office, vehicle, net income)
4. **T1 worksheet** -- line-by-line with formulas (total income, deductions, taxable income, federal tax, credits, balance)
5. **CCA schedule** -- Class, UCC opening, additions, immediate expensing, CCA claimed, UCC closing
6. **CPP/CPP2/EI worksheet** -- pensionable earnings, rates, amounts, deduction/credit split
7. **Provincial tax worksheet** -- rate schedule applied, credits, surtax, total provincial tax
8. **Instalment schedule** -- 2026 quarterly amounts and dates
9. **Cross-skill reconciliation summary** -- all five cross-checks with pass/fail and notes
10. **Reviewer brief** -- comprehensive narrative with positions, citations, flags, self-check results
11. **Client action list** -- what the client needs to do, with dates and amounts

### Reviewer brief contents

```markdown
# Complete Return Package: [Client Name] -- Tax Year 2025

## Executive Summary
- Filing status: [Single / Married / Common-law]
- Residence: Canada (full-year), [Province]
- Business: Sole proprietor, unincorporated
- GST/HST registration: Yes / No (rate: GST 5% / HST 13% / HST 15% / etc.)
- Gross business revenue (ex-GST/HST): $X
- T2125 net business income: $X
- Total income (line 15000): $X
- RRSP deduction: $X
- Net income (line 23600): $X
- Taxable income (line 26000): $X
- Federal tax: $X
- Provincial tax: $X
- CPP self-employed: $X (+ CPP2: $X)
- Total payable (line 43500): $X
- Tax deducted / instalments paid: $X
- Balance owing / refund (line 48500): $X
- 2026 instalment total: $X

## GST/HST Return (GST34)
[Content from canada-gst-hst output]
- Registration status and reporting period (annual / quarterly / monthly)
- Line 101: total revenue
- Line 105: GST/HST collected
- Line 108: input tax credits
- Line 109: net tax owing / refund
- Quick method election (if applicable)
- Any adjustments

## T2125 -- Statement of Business or Professional Activities
[Content from ca-fed-t2125 output]
- Line 8299: gross revenue
- Expense schedule by category (advertising, meals 50%, insurance, office, supplies, etc.)
- Line 9368: total expenses
- Part 7: home office calculation (if claimed)
- Part 8: motor vehicle expenses (if claimed)
- CCA schedule (Class, rate, UCC, additions, CCA, closing UCC)
- Immediate expensing (AIIP) items
- Line 9946: net income (or loss)

## T1 -- Federal Individual Return
[Content from ca-fed-t1-return output]
- Line 10100: employment income (T4)
- Line 13500: gross self-employment income
- Line 13700: net self-employment income
- Line 15000: total income
- Line 20800: RRSP deduction
- Line 21200: union/professional dues
- Line 22200: CPP deduction on self-employment earnings
- Line 22215: CPP2 deduction
- Line 23600: net income
- Line 25000: other payments deduction
- Line 26000: taxable income
- Federal tax calculation (rate schedule applied)
- Line 30000: basic personal amount ($16,129 for 2025 -- confirm)
- Line 31000: CPP contributions through employment + employer portion credit
- Other non-refundable credits
- Line 35000: total federal non-refundable credits
- Line 42000: net federal tax
- Line 42100: provincial tax (from Form 428)
- Line 43500: total payable
- Line 43700: tax deducted (T4 Box 22)
- Line 47600: tax paid by instalments
- Line 48200: total credits
- Line 48500: balance owing / refund

## CPP / CPP2 / EI
[Content from ca-fed-cpp-ei output]
- T2125 net income: $X
- Less basic exemption: $3,500
- Pensionable self-employment earnings: $X
- CPP rate (self-employed): 11.90% (2 x 5.95%)
- CPP payable: $X
- CPP from employment (T4 Box 16): $X -- reduces self-employed portion
- CPP2 earnings (between YMPE and YAMPE): $X
- CPP2 rate (self-employed): 8% (2 x 4%)
- CPP2 payable: $X
- EI: opted in / not opted in
- Split: half deduction (line 22200), half credit (Schedule 8)

## Provincial Tax -- [Province]
- Taxable income: $X (same as federal line 26000)
- Provincial rate schedule applied
- Provincial basic personal amount
- Provincial surtax (Ontario: if basic provincial tax > threshold)
- Provincial credits
- Total provincial tax: $X

## Instalment Schedule -- 2026
[Content from ca-fed-instalments output]
- 2025 net tax owing (instalment base): $X
- Threshold: $3,000 ($1,800 QC) -- instalments required? Yes / No
- Method: prior-year / current-year / no-calculation
- Quarterly amounts:
  - March 15, 2026: $X
  - June 15, 2026: $X
  - September 15, 2026: $X
  - December 15, 2026: $X
- Total: $X

## Cross-skill Reconciliation
- GST34 revenue vs T2125 gross income: [pass/fail]
- T2125 net income vs CPP pensionable earnings: [pass/fail]
- CPP deduction/credit split correct: [pass/fail]
- Instalments credited on T1: [pass/fail]
- Provincial tax on correct taxable income: [pass/fail]

## Reviewer Attention Flags
[Aggregated from all upstream skills]
- T2 items requiring CPA confirmation
- Mixed-use expense percentages (motor vehicle, phone, internet)
- Home office deduction (s18(12) conditions met?)
- CCA / immediate expensing elections
- RRSP contribution vs deduction limit
- Vehicle kilometre log adequacy
- Meals/entertainment 50% limitation applied correctly
- Quebec residents: TP-1 required separately (Q4 stub)
- Any revenue approaching $30K GST/HST registration threshold (if not registered)

## Positions Taken
[List with legislation citations]
- e.g., "Home office deduction claimed -- workspace is principal place of business per s18(12)(a) ITA"
- e.g., "Motor vehicle business use at X% -- based on full-year km log per s18(1)(r) ITA"
- e.g., "Dell laptop immediate expensing under AIIP -- s1104(2) ITR, CCPC/unincorporated limit"
- e.g., "Meals and entertainment at 50% -- s67.1(1) ITA"
- e.g., "RRSP deduction $X -- within limit per s146(5) ITA, s146(5.1) unused room"
- e.g., "CPP self-employed -- s10(1) CPP Act, both employee and employer portions"

## Planning Notes for 2026
- Instalment schedule (quarterly amounts and dates)
- RRSP contribution room generated by 2025 earned income (18% of line 23600, max $X)
- CCA/UCC schedule continuing into 2026
- GST/HST registration threshold monitoring (if approaching $30K)
- CPP/CPP2 rate changes for 2026 (if announced)
- Any legislative changes affecting 2026 (budget measures, rate changes)
- TFSA contribution room (not computed but noted for planning)

## Client Action List

### Immediate (before April 30, 2026 -- T1 balance owing payment deadline):
1. Review this return package with your CPA
2. Pay balance owing of $X to CRA by April 30, 2026 (even though filing deadline is June 15)
3. Pay any GST/HST balance owing

### Note on filing deadlines:
- Self-employed T1 filing deadline: June 15, 2026
- BUT: balance owing is due April 30, 2026 (interest accrues after this date)
- GST34 filing deadline: June 15, 2026 (if annual filer and self-employed)
- Quebec TP-1 (if applicable): June 15, 2026

### Instalment schedule for 2026:
- March 15, 2026: $X
- June 15, 2026: $X
- September 15, 2026: $X
- December 15, 2026: $X

### GST/HST filing calendar (if annual filer):
- 2026 GST34 due: June 15, 2027

### RRSP:
- 2026 RRSP contribution deadline: March 1, 2027
- Projected 2026 RRSP deduction limit: $X (from 2025 earned income)

### Ongoing:
1. Issue invoices with GST/HST for all sales (if registered)
2. Retain all records for 6 years from end of the tax year
3. Maintain motor vehicle kilometre log
4. Track home office hours/expenses if claiming
5. Monitor revenue for GST/HST $30K threshold (if not registered)
6. Review instalment amounts -- vary if income changes significantly
7. Lodge s290-170 equivalent: N/A for Canada (no separate notice required for RRSP -- just claim on return within limit)
```

---

## Section 5 -- Refusals

**R-CA-1 -- Upstream skill did not run.** Name the specific skill. Note: this is a warning, not a hard stop. Continue with available data and flag the gap.

**R-CA-2 -- Upstream self-check failed.** Name the specific check and note it in the reviewer brief. Continue.

**R-CA-3 -- Cross-skill reconciliation failed.** Name the specific reconciliation and describe the discrepancy. Flag for reviewer but continue.

**R-CA-4 -- Intake incomplete.** Specific missing intake items prevent computation. List what is missing and ask the user for the specific data point.

**R-CA-5 -- Out-of-scope item discovered during assembly.** E.g., rental income requiring Form T776, capital gains requiring Schedule 3, foreign income requiring Form T2209. Flag and exclude from computation.

**R-CA-6 -- Quebec resident.** TP-1 provincial return is required but is a Q4 stub. Federal return is computed; provincial return must be prepared separately by the reviewer.

---

## Section 6 -- Self-checks

**Check CA1 -- All upstream skills executed.** canada-gst-hst, ca-fed-t2125, ca-fed-t1-return, ca-fed-cpp-ei all produced output. ca-fed-instalments produced output or was computed from T1 figures. Provincial tax was computed or flagged as stub.

**Check CA2 -- GST34 revenue matches T2125 gross income.** Within $1 tolerance.

**Check CA3 -- T2125 net income feeds CPP correctly.** Pensionable earnings = T2125 line 9946 minus $3,500 basic exemption, capped at YMPE minus any employment pensionable earnings.

**Check CA4 -- CPP split correct.** Half (employee portion) deducted at line 22200; half (employer portion) credited via Schedule 8 at line 31000.

**Check CA5 -- Instalments correctly credited.** Total instalments paid during 2025 credited at T1 line 47600.

**Check CA6 -- GST/HST treatment correct for registered filers.** Business income reported net of GST/HST; ITCs excluded from deductible expenses; GST/HST collected remitted via GST34.

**Check CA7 -- GST/HST treatment correct for small suppliers.** Business income reported gross; all expenses reported gross; no GST34 required.

**Check CA8 -- CCA/immediate expensing correctly applied.** AIIP items fully expensed if elected; standard CCA items depreciated at correct class rates; half-year rule applied where required.

**Check CA9 -- RRSP deduction within limit.** Deduction claimed does not exceed lesser of (contribution amount, deduction limit from prior NOA).

**Check CA10 -- Meals and entertainment at 50%.** s67.1 limitation applied to all meals and entertainment expenses.

**Check CA11 -- Fiscal year end is December 31.** Sole proprietors must use December 31 year-end unless they were in business before 1995 and elected an alternative year-end.

**Check CA12 -- Filing calendar is complete.** All deadlines for GST34, T1, instalments, and RRSP are listed with specific dates and amounts.

**Check CA13 -- Provincial tax uses correct province.** Province on December 31 determines provincial tax; correct rate schedule applied.

---

## Section 7 -- Output files

The final output is **three files**:

1. **`[client_slug]_2025_canada_master.xlsx`** -- Single master workbook containing every worksheet and form. Sheets include: Cover, GST34 (line-by-line), T2125 (line-by-line), T1 Summary (line-by-line), CCA Schedule, Expense Detail, CPP/EI Calculation, Provincial Tax, Instalment Schedule, Cross-Check Summary. Use live formulas where possible -- e.g., T1 line 13700 references T2125 line 9946; CPP pensionable earnings reference T2125 net income; instalment amounts reference T1 net tax. Verify no `#REF!` errors. Verify computed values match the computation model within $1 before shipping.

2. **`reviewer_brief.md`** -- Single markdown file covering all sections from Section 4 above: executive summary, GST34, T2125, T1, CPP/EI, provincial tax, instalments, cross-skill reconciliation, flags, positions, planning notes.

3. **`client_action_list.md`** -- Single markdown file with step-by-step actions: immediate filings and payments, quarterly instalment calendar for 2026, ongoing compliance reminders.

**If execution runs out of context mid-build:** produce whatever is complete, then state at the end which of the three files were not produced or are partial.

**All files are placed in `/mnt/user-data/outputs/` and presented to the user via the `present_files` tool at the end.**

---

## Section 8 -- Cross-skill references

**Inputs:**
- `ca-freelance-intake` -- structured intake package (JSON)
- `canada-gst-hst` -- GST34 line values and classification output
- `ca-fed-t2125` -- T2125 line values and computation output
- `ca-fed-t1-return` -- T1 line values and computation output
- `ca-fed-cpp-ei` -- CPP/CPP2/EI calculation output
- `ca-fed-instalments` -- Instalment schedule (or fallback computation)
- Provincial return -- Form 428 or TP-1 (Quebec)

**Outputs:** The final reviewer package. No downstream skill.

---

## Section 9 -- Known gaps

1. PDF form filling is not automated. The reviewer uses the worksheets to file via NETFILE, EFILE, or paper.
2. E-filing is handled by the reviewer via certified tax software, not by this skill.
3. Payment execution is the client's responsibility; the skill only provides instructions and amounts.
4. Quebec TP-1 provincial return is a Q4 stub. Quebec residents get the federal package only; TP-1 must be prepared separately.
5. Rental income (T776) is not supported -- if rental income exists, the skill flags it but the T776 must be completed separately by the reviewer.
6. Capital gains (Schedule 3) are not supported -- if capital gains exist, the skill flags it but Schedule 3 must be completed separately.
7. Foreign income and foreign tax credit (T2209) are out of scope.
8. Multi-year CCA tracking assumes the prior year schedule is provided. If not, only current-year acquisitions are depreciated.
9. Several upstream content skills are Q2 skills. If any are still stubs, the assembly skill computes the figures directly and flags the gap.
10. ca-fed-instalments is a Q4 stub. Until it is fleshed out, instalments are computed using the prior-year method. This is a redundancy, not a gap -- the rules are deterministic.
11. Provincial returns for all provinces except Quebec are computed from the federal rate schedules. Dedicated provincial skills are Q4 stubs.
12. The package is complete only for the 2025 tax year; 2026 appears only as prospective planning.
13. EI self-employed opt-in is flagged but not deeply modelled -- if the taxpayer has opted in, the reviewer should verify special benefit eligibility.

### Change log
- **v0.1 (April 2026):** Initial draft. Modelled on mt-return-assembly v0.1 adapted for Canadian jurisdiction with five content skills plus provincial tax (GST34, T2125, T1, CPP/EI, instalments, provincial).

## End of skill


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
