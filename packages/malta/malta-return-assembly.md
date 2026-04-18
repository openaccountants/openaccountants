---
name: mt-return-assembly
description: Final orchestrator skill that assembles the complete Malta filing package for Malta-resident self-employed individuals and sole proprietors. Consumes outputs from all Malta content skills (malta-vat-return for Malta VAT, malta-income-tax for TA24, malta-ssc for Class 2 contributions, mt-estimated-tax for provisional tax) to produce a single unified reviewer package containing every worksheet, every form, every brief section, all cross-skill reconciliations, and the final action list with payment instructions, filing instructions, and next-year planning. This is the capstone skill that runs last and produces the final deliverable. MUST be loaded alongside all Malta content skills listed above. Malta full-year residents only. Self-employed individuals and sole proprietors only.
version: 0.1
---

# Malta Return Assembly Skill v0.1

## CRITICAL EXECUTION DIRECTIVE -- READ FIRST

**When this skill is invoked, you have already passed through intake. The user has consented to the full workflow. Execute all steps without pausing for permission.**

Specifically:

- **Do NOT ask the user "how deep do you want me to go"** or "do you want the full package" or any variant. The user asked for their tax returns. They want their tax returns. Produce them.
- **Do NOT announce how many tokens or tool calls this will take.** Execute.
- **Do NOT ask which deliverables to prioritise.** Produce all deliverables listed in Section 8. If you run out of context mid-execution, finish the computation work first (numbers, positions, flags) then produce whatever formatted outputs you can, and at the very end state clearly which deliverables were not produced and why.
- **Do NOT re-validate scope that intake already validated.** If `mt-freelance-intake` produced an intake package, trust it. You can cross-check specific numbers during reconciliation but do not re-interrogate the user about residency, business structure, or anything else intake already captured.
- **Do NOT pause between content skills to check in.** Run them in dependency order (Section 2) without prose status updates between each one. A single status message at the end is fine.
- **Self-checks are targets, not blockers.** If a self-check fails, note it in the reviewer brief's open flags section and continue. Do NOT halt the entire workflow because one self-check had an ambiguous answer.
- **Primary source citations go in the final reviewer brief, not in intermediate computation steps.**

**The user has already been told (by the intake skill) that the final package requires warranted accountant signoff before filing. State it once in the final output and move on.**

**Failure mode to avoid:** The skill halts mid-execution and asks the user a meta-question about workflow pacing. If you feel the urge to ask "how should I proceed," the correct action is to pick the most defensible path and proceed, flagging the decision in the reviewer brief so the reviewer can challenge it.

---

## What this file is

The final capstone skill for Malta self-employed returns. Every Malta content skill feeds into this one. The output is the complete reviewer package that a warranted accountant can review, sign off on, and deliver to the client along with filing instructions.

This skill coordinates execution of the content skills, verifies cross-skill consistency, and assembles the final deliverable.

---

## Section 1 -- Scope

Produces the complete Malta filing package for:
- Full-year Malta residents
- Self-employed individuals and sole proprietors (self-occupied)
- Tax year 2025
- Filing Malta VAT returns (Article 10 quarterly or Article 11 annual), TA24, Class 2 SSC reconciliation, provisional tax schedule

---

## Section 2 -- Execution order and dependency chain

The skill enforces the following execution order:

1. **`malta-vat-return`** -- Malta VAT return (quarterly for Article 10, annual declaration for Article 11)
   - Runs first because VAT turnover figures feed into the TA24
   - For Article 10: prepare Q4 2025 VAT return if not yet filed; verify Q1-Q3 figures
   - For Article 11: prepare annual declaration; verify turnover remains under EUR 35,000
   - Output: VAT return box values, input VAT recovered/blocked, turnover (ex-VAT)

2. **`malta-income-tax`** -- TA24 self-employed return (annual)
   - Depends on VAT output: gross income (Box 1) must use ex-VAT turnover for Article 10 clients
   - Depends on VAT output: blocked input VAT becomes a deductible expense in Box 2
   - Output: TA24 box values (Box 1 through Box 40), chargeable income, tax liability

3. **`malta-ssc`** -- Class 2 social security contributions (quarterly payments, annual reconciliation)
   - Depends on TA24: SSC paid enters Box 20 of the TA24
   - Depends on prior year TA24 net income: SSC amount is based on prior year, not current
   - Output: annual SSC amount, category (SA/SB/SC), payments made vs amount due, any shortfall

4. **`mt-estimated-tax`** -- Provisional tax schedule (2026 forward-looking)
   - Depends on TA24: provisional tax is based on the current year's final tax liability for next year
   - **Status check:** mt-estimated-tax is currently a Q4 stub. If the stub has substantive computation content, use it. If it is still a placeholder, compute provisional tax using the rules documented in malta-income-tax Step 5 (ITMA Chapter 372: 20%/30%/50% split) and flag in the reviewer brief that the dedicated skill was not available.
   - Output: three instalment amounts and dates for 2026

If any upstream content skill fails to produce validated output, the assembly skill notes the failure in the reviewer brief and continues with available data rather than halting entirely.

---

## Section 3 -- Cross-skill reconciliation

### Cross-check 1: VAT turnover matches TA24 gross income

| VAT Output | TA24 Input | Rule |
|-----------|-----------|------|
| VAT return total turnover (ex-VAT) | TA24 Box 1 (gross income) | Must match within EUR 1 |
| Article 10: sum of Box 1 + Box 2 (outputs) | TA24 Box 1 | Turnover is ex-VAT |
| Article 11: declared turnover | TA24 Box 1 | Turnover is gross (no VAT separation) |

**If mismatch:** Flag for reviewer. Common causes: timing differences (invoice vs payment basis), foreign income not subject to Malta VAT, exempt supplies, bad debt relief.

### Cross-check 2: SSC computation uses TA24 net income

| SSC Input | Source | Rule |
|-----------|--------|------|
| Prior year net self-employment income | Prior year TA24 Box 3 or Box 30 | SSC is always based on prior year |
| Current year SSC paid | DSS statements / bank statement | Enters current year TA24 Box 20 |

**If mismatch:** Verify the prior year figure. If prior year TA24 was not filed, SA minimum applies by default.

### Cross-check 3: Provisional tax based on prior-year TA24

| Provisional Tax Input | Source | Rule |
|----------------------|--------|------|
| Prior year final tax liability | Prior year TA24 Box 40 (or Box 35 minus credits) | 20%/30%/50% split |
| Payments made during 2025 | Bank statement / CFR receipts | Must reconcile to TA24 Box 36 |
| 2026 schedule | Current year TA24 final tax liability (Box 35 minus Box 37) | Drives next year's instalments |

**If mismatch:** Common cause is first year of self-employment (no provisional tax due) or prior year assessment differing from filed return.

### Cross-check 4: VAT input tax and income tax deductions consistency

| Item | VAT Treatment | Income Tax Treatment |
|------|--------------|---------------------|
| Reclaimable input VAT (Article 10) | Claimed in VAT return Boxes 34-38 | NOT a deduction in TA24 Box 2 (net amount only) |
| Blocked input VAT (Article 10) | Not claimed | IS a deduction in TA24 Box 2 (added to cost) |
| All VAT paid (Article 11) | No recovery | IS a deduction in TA24 Box 2 (gross amount is cost) |
| Capital goods VAT (Article 10, >= EUR 1,160) | Box 36 of VAT return | Capital allowance in TA24 Box 15 (on net cost) |

**If inconsistency:** An expense claimed net of VAT on the TA24 while also not claimed on the VAT return means the VAT is lost. Flag for reviewer.

### Cross-check 5: Capital items consistent across VAT and income tax

| System | Threshold | Treatment |
|--------|-----------|-----------|
| VAT Capital Goods Scheme | >= EUR 1,160 gross | VAT return Box 30 |
| Income Tax Capital Allowances | No threshold | TA24 Box 15, depreciated per 6th Schedule |

A EUR 500 printer: depreciated for income tax (25% x EUR 500 = EUR 125/year in Box 15) but does NOT go to VAT Box 30. These are separate systems and must be tracked independently.

---

## Section 4 -- Final reviewer package contents

### Documents

1. **Executive summary** -- one-page overview: filing status, income, tax liability, VAT position, SSC, provisional tax, refund/balance due
2. **VAT return worksheet** -- box-by-box with formulas (Q4 2025 or annual Article 11)
3. **TA24 worksheet** -- Box 1 through Box 40 with formulas and supporting schedules
4. **Capital allowances schedule** -- asset register with cost, date, rate, annual allowance, WDV
5. **SSC reconciliation** -- category determination, amount due, payments made, shortfall/overpayment
6. **Provisional tax schedule** -- 2026 three-instalment calculation
7. **Cross-skill reconciliation summary** -- all five cross-checks with pass/fail and notes
8. **Reviewer brief** -- comprehensive narrative with positions, citations, flags, self-check results
9. **Client action list** -- what the client needs to do, with dates and amounts

### Reviewer brief contents

```markdown
# Complete Return Package: [Client Name] -- Tax Year 2025

## Executive Summary
- Filing status: [Single / Married / Parent]
- Residence: Malta (full-year)
- Business: Self-employed / Self-occupied, sole proprietor
- VAT registration: Article 10 / Article 11
- VAT return position (Q4 or annual): EUR X due / EUR X credit
- TA24 total tax liability (Box 35): EUR X
- SSC Class 2 annual amount: EUR X
- Provisional tax paid (Box 36): EUR X
- Tax credits (Box 37): EUR X
- TA24 balance due / refund (Box 40): EUR X
- 2026 provisional tax total: EUR X

## VAT Return
[Content from malta-vat-return output]
- Registration type and period
- Output VAT summary
- Input VAT summary (reclaimable, blocked, capital goods)
- Reverse charge entries (EU/non-EU services)
- Box-by-box summary
- Excess credit position

## Income Tax Return (TA24)
[Content from malta-income-tax output]
- Box 1: Gross income breakdown by client
- Box 2: Allowable deductions schedule
- Box 3: Net profit
- Box 4: Other income (if any)
- Box 15: Capital allowances schedule
- Box 20: SSC deduction
- Box 30: Chargeable income
- Box 35: Tax liability (rate table applied)
- Box 36: Provisional tax paid
- Box 37: Tax credits
- Box 40: Balance due / refund

## Social Security Contributions
[Content from malta-ssc output]
- Birth year and cap category
- Prior year net income used
- Category: SA / SB / SC
- Annual amount due
- Quarterly payments made
- Shortfall or overpayment
- Deductibility confirmed (Box 20)

## Provisional Tax (2026)
[Content from mt-estimated-tax output, or computed from malta-income-tax Step 5 if stub]
- Based on 2025 final tax liability (Box 35 minus Box 37)
- 1st instalment: 20% -- due 30 April 2026
- 2nd instalment: 30% -- due 31 August 2026
- 3rd instalment: 50% -- due 21 December 2026
- If first year: no provisional tax was due in 2025; 2026 is the first year

## Cross-skill Reconciliation
- VAT turnover vs TA24 Box 1: [pass/fail]
- SSC base vs prior year TA24: [pass/fail]
- Provisional tax vs prior year liability: [pass/fail]
- VAT input tax vs TA24 deductions: [pass/fail]
- Capital items VAT vs income tax: [pass/fail]

## Reviewer Attention Flags
[Aggregated from all upstream skills]
- T2 items requiring warranted accountant confirmation
- Mixed-use expense percentages (motor vehicle, phone, internet)
- Home office deduction (if claimed)
- Capital item classification
- Any turnover approaching EUR 35,000 Article 11 threshold
- Any income approaching rate band boundaries
- TA22 vs TA24 decision (if employed + side income)

## Positions Taken
[List with legislation citations]
- e.g., "Home office deduction claimed at 15% of total floor area -- Article 14, ITA Cap. 123"
- e.g., "Motor vehicle business use at 70% -- client-stated, mileage log available -- Article 14, ITA Cap. 123"
- e.g., "MacBook Pro capitalised and depreciated at 25% p.a. -- 6th Schedule, ITA Cap. 123"

## Planning Notes for 2026
- Provisional tax schedule (three instalments with amounts and dates)
- SSC category projection based on 2025 net income
- VAT Article 11 threshold monitoring (if approaching EUR 35,000)
- Capital allowances continuing into 2026 (WDV schedule)
- Any legislative changes affecting 2026 (budget measures, rate changes)

## Client Action List

### Immediate (before 30 June 2026 -- TA24 filing deadline):
1. Review this return package with your warranted accountant
2. File TA24 via MTCA e-Services
3. Pay TA24 balance due of EUR X to CFR
4. File Q4 2025 Malta VAT return (if not yet filed) -- deadline was [date]

### Before 30 April 2026 (ALREADY PASSED if current date is after -- check):
1. Pay 2026 1st provisional tax instalment of EUR X (20%)
2. Pay Q1 2026 SSC instalment of EUR X

### Before 31 August 2026:
1. Pay 2026 2nd provisional tax instalment of EUR X (30%)
2. Pay Q3 2026 SSC instalment of EUR X

### Before 21 December 2026:
1. Pay 2026 3rd provisional tax instalment of EUR X (50%)
2. Pay Q4 2026 SSC instalment of EUR X

### VAT filing calendar (Article 10 quarterly):
- Q1 2026 (Jan-Mar): file by [Q1 deadline]
- Q2 2026 (Apr-Jun): file by [Q2 deadline]
- Q3 2026 (Jul-Sep): file by [Q3 deadline]
- Q4 2026 (Oct-Dec): file by [Q4 deadline]

### Ongoing:
1. Issue VAT-compliant invoices for all sales
2. Retain all purchase invoices and receipts (6-year retention)
3. Maintain mileage log if claiming motor vehicle expenses
4. Monitor turnover for VAT threshold (Article 11 clients)
5. Track capital assets in the asset register
```

---

## Section 5 -- Refusals

**R-MT-1 -- Upstream skill did not run.** Name the specific skill. Note: this is a warning, not a hard stop. Continue with available data and flag the gap.

**R-MT-2 -- Upstream self-check failed.** Name the specific check and note it in the reviewer brief. Continue.

**R-MT-3 -- Cross-skill reconciliation failed.** Name the specific reconciliation and describe the discrepancy. Flag for reviewer but continue.

**R-MT-4 -- Intake incomplete.** Specific missing intake items prevent computation. List what is missing and ask the user for the specific data point.

**R-MT-5 -- Out-of-scope item discovered during assembly.** E.g., rental income requiring supplementary forms, foreign source income, or partnership income. Flag and exclude from computation.

---

## Section 6 -- Self-checks

**Check MT1 -- All upstream skills executed.** malta-vat-return, malta-income-tax, malta-ssc all produced output. mt-estimated-tax produced output or was computed from malta-income-tax Step 5.

**Check MT2 -- VAT turnover matches TA24 Box 1.** Within EUR 1 tolerance.

**Check MT3 -- SSC uses correct prior-year base.** Prior year net income matches the figure used for SSC category determination.

**Check MT4 -- Provisional tax matches prior-year liability.** 20%+30%+50% = 100% of prior year final tax.

**Check MT5 -- Article 10 VAT treatment correct.** Output VAT excluded from income; reclaimable input VAT excluded from expenses; blocked VAT included in expenses.

**Check MT6 -- Article 11 VAT treatment correct.** No output VAT charged; all input VAT included in expenses (gross = cost).

**Check MT7 -- Capital items correctly split.** Items >= EUR 1,160 gross in VAT Box 30; all capital items in TA24 Box 15 at correct depreciation rates.

**Check MT8 -- SSC entered in TA24 Box 20.** Amount paid during 2025, not amount due.

**Check MT9 -- Rate table matches marital status.** Single/married/parent rate table correctly applied to Box 30 chargeable income.

**Check MT10 -- Filing calendar is complete.** All deadlines for VAT, TA24, SSC, and provisional tax are listed with specific dates and amounts.

**Check MT11 -- No form numbers in user-facing messages.** Internal notes can reference form numbers; user-facing messages use plain English where possible.

**Check MT12 -- Reviewer brief contains legislation citations.** Every position taken references the specific article of the relevant Act.

---

## Section 7 -- Output files

The final output is **three files**:

1. **`[client_slug]_2025_malta_master.xlsx`** -- Single master workbook containing every worksheet and form. Sheets include: Cover, VAT return (Q4 or Annual), TA24 (Box 1-40), Capital Allowances, Expense Detail, SSC Reconciliation, Provisional Tax 2026, Cross-Check Summary. Use live formulas where possible -- e.g., TA24 Box 1 references the VAT turnover cell; Box 20 references the SSC sheet total; Box 36 references the provisional tax paid. Verify no `#REF!` errors. Verify computed values match the Python/computation model within EUR 1 before shipping.

2. **`reviewer_brief.md`** -- Single markdown file covering all sections from Section 4 above: executive summary, VAT return, TA24, SSC, provisional tax, cross-skill reconciliation, flags, positions, planning notes.

3. **`client_action_list.md`** -- Single markdown file with step-by-step actions: immediate filings and payments, quarterly calendar for 2026, ongoing compliance reminders.

**If execution runs out of context mid-build:** produce whatever is complete, then state at the end which of the three files were not produced or are partial.

**All files are placed in `/mnt/user-data/outputs/` and presented to the user via the `present_files` tool at the end.**

---

## Section 8 -- Cross-skill references

**Inputs:**
- `mt-freelance-intake` -- structured intake package (JSON)
- `malta-vat-return` -- VAT return box values and classification output
- `malta-income-tax` -- TA24 box values and computation output
- `malta-ssc` -- Class 2 reconciliation output
- `mt-estimated-tax` -- Provisional tax schedule (or fallback computation)

**Outputs:** The final reviewer package. No downstream skill.

---

## Section 9 -- Known gaps

1. PDF form filling is not automated. The reviewer uses the worksheets to fill official CFR forms on MTCA e-Services.
2. E-filing is handled by the reviewer via MTCA portal, not by this skill.
3. Payment execution is the client's responsibility; the skill only provides instructions and amounts.
4. TA22 (part-time self-employment) assembly is not fully supported -- if TA22 applies, the skill flags it but the TA22 form is simpler (flat 10%) and may be completed manually by the reviewer.
5. Multi-year capital allowance tracking assumes the prior year schedule is provided. If not, only current-year acquisitions are depreciated.
6. mt-estimated-tax is a Q4 stub. Until it is fleshed out, provisional tax is computed using the rules in malta-income-tax Step 5. This is a redundancy, not a gap -- the rules are deterministic (ITMA Chapter 372).
7. Foreign source income is out of scope (no double taxation relief computation).
8. Rental income supplementary forms are out of scope.
9. The package is complete only for the 2025 tax year; 2026 appears only as prospective planning.

### Change log
- **v0.1 (April 2026):** Initial draft. Modelled on us-ca-return-assembly v0.2 adapted for Malta jurisdiction with four content skills (Malta VAT return, TA24, SSC, provisional tax).

## End of skill


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
