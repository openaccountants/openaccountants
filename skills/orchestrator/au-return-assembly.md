---
name: au-return-assembly
description: Final orchestrator skill that assembles the complete Australian filing package for Australian-resident sole traders. Consumes outputs from all Australian content skills (australia-gst for BAS, au-individual-return for ITR, au-super-guarantee for voluntary contributions, au-medicare-levy for levy and surcharge, au-payg-instalments for instalment schedule) to produce a single unified reviewer package containing every worksheet, every form, every brief section, all cross-skill reconciliations, and the final action list with payment instructions, filing instructions, and next-year planning. This is the capstone skill that runs last and produces the final deliverable. MUST be loaded alongside all Australian content skills listed above. Australian full-year residents only. Sole traders only.
version: 0.1
---

# Australia Return Assembly Skill v0.1

## CRITICAL EXECUTION DIRECTIVE -- READ FIRST

**When this skill is invoked, you have already passed through intake. The user has consented to the full workflow. Execute all steps without pausing for permission.**

Specifically:

- **Do NOT ask the user "how deep do you want me to go"** or "do you want the full package" or any variant. The user asked for their tax returns. They want their tax returns. Produce them.
- **Do NOT announce how many tokens or tool calls this will take.** Execute.
- **Do NOT ask which deliverables to prioritise.** Produce all deliverables listed in Section 4. If you run out of context mid-execution, finish the computation work first (numbers, positions, flags) then produce whatever formatted outputs you can, and at the very end state clearly which deliverables were not produced and why.
- **Do NOT re-validate scope that intake already validated.** If `au-freelance-intake` produced an intake package, trust it. You can cross-check specific numbers during reconciliation but do not re-interrogate the user about residency, business structure, or anything else intake already captured.
- **Do NOT pause between content skills to check in.** Run them in dependency order (Section 2) without prose status updates between each one. A single status message at the end is fine.
- **Self-checks are targets, not blockers.** If a self-check fails, note it in the reviewer brief's open flags section and continue. Do NOT halt the entire workflow because one self-check had an ambiguous answer.
- **Primary source citations go in the final reviewer brief, not in intermediate computation steps.**

**The user has already been told (by the intake skill) that the final package requires registered tax agent signoff before lodging. State it once in the final output and move on.**

**Failure mode to avoid:** The skill halts mid-execution and asks the user a meta-question about workflow pacing. If you feel the urge to ask "how should I proceed," the correct action is to pick the most defensible path and proceed, flagging the decision in the reviewer brief so the reviewer can challenge it.

---

## What this file is

The final capstone skill for Australian sole trader returns. Every Australian content skill feeds into this one. The output is the complete reviewer package that a registered tax agent can review, sign off on, and deliver to the client along with lodgement instructions.

This skill coordinates execution of the content skills, verifies cross-skill consistency, and assembles the final deliverable.

---

## Section 1 -- Scope

Produces the complete Australian filing package for:
- Full-year Australian residents
- Sole traders
- Tax year 2024-25 (1 July 2024 - 30 June 2025)
- Lodging BAS (if GST registered), individual tax return (ITR), super reconciliation, Medicare levy calculation, PAYG instalment schedule

---

## Section 2 -- Execution order and dependency chain

The skill enforces the following execution order:

1. **`australia-gst`** -- BAS return (quarterly, if GST registered)
   - Runs first because GST turnover figures feed into the ITR
   - For GST-registered: prepare any outstanding quarterly BAS; verify previously lodged quarters
   - Output: BAS box values (1A GST on sales, 1B GST on purchases), net GST position, turnover (ex-GST)
   - **Status check:** australia-gst is currently a Q2 skill. If it has substantive computation content, use it. If it is still a placeholder, compute BAS figures from the intake package data and flag in the reviewer brief that the dedicated skill was not available.

2. **`au-individual-return`** -- Individual tax return (ITR)
   - Depends on BAS output: business income must use ex-GST turnover for GST-registered traders
   - Depends on BAS output: GST credits are excluded from deductible expenses (net amounts only)
   - Output: ITR label values, taxable income, tax on taxable income, tax offsets, tax liability
   - **Status check:** au-individual-return is currently a Q2 skill. If it has substantive computation content, use it. If it is still a placeholder, compute ITR figures from the intake package data and flag in the reviewer brief that the dedicated skill was not available.

3. **`au-super-guarantee`** -- Voluntary super contributions reconciliation
   - Depends on ITR: personal deductible contributions reduce taxable income
   - Verifies contributions are within the $30,000 concessional cap
   - Output: contribution amounts, cap utilisation, any excess contributions
   - **Status check:** au-super-guarantee is currently a Q2 skill. If it has substantive computation content, use it. If it is still a placeholder, compute super figures from the intake package data and flag in the reviewer brief that the dedicated skill was not available.

4. **`au-medicare-levy`** -- Medicare levy and surcharge
   - Depends on ITR: levy is 2% of taxable income; surcharge applies if no PHI and income above threshold
   - Checks PHI status from intake package
   - Output: Medicare levy amount, surcharge amount (if applicable), PHI rebate adjustment
   - **Status check:** au-medicare-levy is currently a Q2 skill. If it has substantive computation content, use it. If it is still a placeholder, compute Medicare figures from the intake package data and flag in the reviewer brief that the dedicated skill was not available.

5. **`au-payg-instalments`** -- PAYG instalment schedule (next year)
   - Depends on ITR: instalment income and rate for 2025-26 based on 2024-25 return
   - Reconciles instalments paid during 2024-25 against final tax liability
   - Output: instalment credit for current year, next-year instalment schedule
   - **Status check:** au-payg-instalments is currently a Q4 stub. If the stub has substantive computation content, use it. If it is still a placeholder, compute PAYG instalment figures using the ATO's instalment rate method and flag in the reviewer brief that the dedicated skill was not available.

If any upstream content skill fails to produce validated output, the assembly skill notes the failure in the reviewer brief and continues with available data rather than halting entirely.

---

## Section 3 -- Cross-skill reconciliation

### Cross-check 1: BAS G1 taxable sales = ITR business income (ex-GST)

| BAS Output | ITR Input | Rule |
|-----------|-----------|------|
| BAS 1A total GST on sales (annual) | Implied from ITR business income x 10% | Must reconcile |
| BAS G1 total sales (ex-GST, annual sum) | ITR business income label | Must match within $1 |
| Non-GST registered: gross receipts | ITR business income label | Direct match (no GST separation) |

**If mismatch:** Flag for reviewer. Common causes: timing differences (cash vs accrual), private sales included in bank deposits, GST-free supplies, input-taxed supplies.

### Cross-check 2: Super contributions within concessional cap ($30,000)

| Super Input | Source | Rule |
|------------|--------|------|
| Employer contributions (if also employed) | PAYG summary / income statement | Counted toward cap |
| Salary sacrifice (if any) | PAYG summary | Counted toward cap |
| Personal deductible contributions | Super fund statement + s290-170 notice | Counted toward cap |
| Total concessional | Sum of above | Must not exceed $30,000 |

**If excess:** Flag for reviewer. Excess concessional contributions are included in assessable income and taxed at marginal rate (plus excess concessional contributions charge). Division 293 tax applies if income + super > $250,000.

### Cross-check 3: Medicare levy surcharge only if no PHI and income above threshold

| MLS Input | Source | Rule |
|----------|--------|------|
| Income for MLS purposes | ITR taxable income + reportable fringe benefits + total net investment loss + reportable super | Combined figure |
| PHI status | Insurer statement | If adequate hospital cover for full year, no MLS |
| MLS thresholds (2024-25) | Single: $93,000; Family: $186,000 | Below threshold = no MLS regardless of PHI |
| MLS rates | Tier 1: 1%; Tier 2: 1.25%; Tier 3: 1.5% | Applied to taxable income |

**If MLS applies:** Calculate and include in tax liability. Flag for reviewer with income calculation breakdown.

### Cross-check 4: PAYG instalments credit against final tax

| PAYG Input | Source | Rule |
|-----------|--------|------|
| Instalments paid during 2024-25 | BAS PAYG instalment labels (T7/T8) or ATO records | Credit against final tax |
| Tax withheld by employer (if any) | PAYG summary | Additional credit |
| Final tax liability | ITR computation | Total tax - credits = balance due or refund |

**If mismatch:** Common cause is varied instalments (taxpayer requested variation), or first year with no prior instalment history.

### Cross-check 5: Instant asset write-off consistency

| System | Threshold (2024-25) | Treatment |
|--------|---------------------|-----------|
| GST-registered | Asset cost ex-GST < $20,000 | Immediate deduction; GST credit claimed separately |
| Non-GST-registered | Asset cost inc-GST < $20,000 | Immediate deduction on gross cost |
| Above threshold | Depreciate using effective life | ITR depreciation schedule |

**If inconsistency:** An asset claimed as instant write-off but costing above the threshold (on the correct GST basis) must be moved to depreciation schedule. Flag for reviewer.

---

## Section 4 -- Final reviewer package contents

### Documents

1. **Executive summary** -- one-page overview: filing status, business income, taxable income, tax liability, Medicare levy, super position, PAYG credits, refund/balance due
2. **BAS worksheet** -- quarterly box-by-box with formulas (GST on sales, GST on purchases, PAYG instalments)
3. **ITR worksheet** -- label-by-label with formulas and supporting schedules (business income, deductions, taxable income, tax rates, offsets)
4. **Depreciation schedule** -- asset register with cost, date, effective life, method, annual deduction, written-down value
5. **Super reconciliation** -- concessional cap tracking, contribution breakdown, excess check
6. **Medicare levy worksheet** -- levy calculation, MLS assessment, PHI rebate adjustment
7. **PAYG instalment reconciliation** -- instalments paid vs final tax, next-year schedule
8. **Cross-skill reconciliation summary** -- all five cross-checks with pass/fail and notes
9. **Reviewer brief** -- comprehensive narrative with positions, citations, flags, self-check results
10. **Client action list** -- what the client needs to do, with dates and amounts

### Reviewer brief contents

```markdown
# Complete Return Package: [Client Name] -- Tax Year 2024-25

## Executive Summary
- Filing status: [Single / Married / etc.]
- Residence: Australia (full-year), [State]
- Business: Sole trader, ABN [number]
- GST registration: Yes / No
- Business income (ex-GST): $X
- Total deductions: $X
- Taxable income: $X
- Tax on taxable income: $X
- Medicare levy: $X
- Medicare levy surcharge: $X / nil
- Tax offsets: $X
- PAYG instalments credit: $X
- PAYG withholding credit: $X
- Balance due / refund: $X
- HELP compulsory repayment: $X / nil
- 2025-26 PAYG instalment amount: $X

## BAS / GST Return
[Content from australia-gst output]
- Registration status and reporting period
- GST on sales (1A) -- quarterly and annual
- GST on purchases (1B) -- quarterly and annual
- Net GST position per quarter
- Any outstanding BAS quarters
- PAYG instalment amounts per BAS

## Individual Tax Return (ITR)
[Content from au-individual-return output]
- Business income (ex-GST)
- Total business deductions schedule
- Net business income
- Other income (interest, dividends, etc.)
- Total income
- Total deductions (including personal deductible super)
- Taxable income
- Tax on taxable income (rate table applied)
- Tax offsets (low income, LMITO if applicable, PHI rebate)
- Medicare levy
- HELP compulsory repayment
- Total tax liability
- Less: PAYG instalments paid
- Less: PAYG withholding
- Balance due / refund

## Depreciation Schedule
- Asset register with cost, purchase date, effective life, method (prime cost / diminishing value)
- Instant asset write-off items (under $20K threshold)
- Continuing depreciation from prior years
- Written-down values carried forward to 2025-26

## Super Contributions
[Content from au-super-guarantee output]
- Personal deductible contributions (s290-170 notice required)
- Employer contributions (if also employed)
- Total concessional: $X of $30,000 cap
- Excess concessional: $X / nil
- Non-concessional contributions: $X
- Division 293 check: income + super vs $250,000 threshold
- Total super balance (for carry-forward cap calculation)

## Medicare Levy and Surcharge
[Content from au-medicare-levy output]
- Medicare levy: 2% of taxable income = $X
- Medicare levy reduction (if low income): $X / nil
- Income for MLS purposes: $X
- PHI status: adequate hospital cover / no cover
- MLS rate: X% / nil
- MLS amount: $X / nil
- PHI rebate tier and adjustment: $X / nil

## PAYG Instalments
[Content from au-payg-instalments output]
- 2024-25 instalments paid: $X (credit against final tax)
- 2024-25 instalment rate used: X%
- 2025-26 instalment income (from 2024-25 return): $X
- 2025-26 instalment rate (from NOA): X%
- 2025-26 quarterly instalment amounts:
  - Q1 (Jul-Sep): due 28 Oct 2025
  - Q2 (Oct-Dec): due 28 Feb 2026
  - Q3 (Jan-Mar): due 28 Apr 2026
  - Q4 (Apr-Jun): due 28 Jul 2026

## Cross-skill Reconciliation
- BAS G1 vs ITR business income: [pass/fail]
- Super within concessional cap: [pass/fail]
- MLS correctly assessed: [pass/fail]
- PAYG credits reconciled: [pass/fail]
- Instant asset write-off thresholds correct: [pass/fail]

## Reviewer Attention Flags
[Aggregated from all upstream skills]
- T2 items requiring registered tax agent confirmation
- Mixed-use expense percentages (motor vehicle, phone, internet)
- Home office deduction (method and hours/area)
- Instant asset write-off eligibility
- Super cap proximity
- PHI rebate tier boundary
- HELP repayment income threshold
- Any income approaching tax bracket boundaries
- Any turnover approaching $75K GST registration threshold (if not registered)

## Positions Taken
[List with legislation citations]
- e.g., "Home office deduction claimed at 67c/hr for X hours -- Practical Compliance Guideline PCG 2023/1"
- e.g., "Motor vehicle cents-per-km at 85c/km for X km -- s28-25 ITAA 1997, TD 2024/3"
- e.g., "MacBook Pro instant asset write-off -- s328-180 ITAA 1997, Temporary Full Expensing extended"
- e.g., "Personal super contribution deduction -- s290-150 ITAA 1997, s290-170 notice lodged"

## Planning Notes for 2025-26
- PAYG instalment schedule (quarterly amounts and dates)
- Super contribution strategy (remaining cap, carry-forward unused cap from prior years)
- GST registration threshold monitoring (if approaching $75K)
- Depreciation schedule continuing into 2025-26 (WDV schedule)
- PHI rebate tier based on projected income
- Any legislative changes affecting 2025-26 (budget measures, rate changes)

## Client Action List

### Immediate (before 31 October 2025 -- ITR lodgement deadline for self-lodgers):
1. Review this return package with your registered tax agent
2. Lodge ITR via myTax or through tax agent (tax agent clients have extended deadline)
3. Pay balance due of $X to ATO (or receive refund of $X)
4. Lodge any outstanding BAS quarters

### Note on lodgement deadlines:
- Self-lodgers: 31 October 2025
- Tax agent lodgement: extended deadlines apply (typically March-May 2026 depending on category)

### Quarterly obligations for 2025-26:
- BAS Q1 (Jul-Sep): lodge and pay by 28 October 2025
- BAS Q2 (Oct-Dec): lodge and pay by 28 February 2026
- BAS Q3 (Jan-Mar): lodge and pay by 28 April 2026
- BAS Q4 (Apr-Jun): lodge and pay by 28 July 2026

### Super obligations:
- If you have employees: SG due quarterly (28 days after quarter end)
- Personal deductible contributions: lodge s290-170 notice with super fund BEFORE lodging ITR
- Monitor concessional cap ($30,000) across all contribution sources

### Ongoing:
1. Issue tax invoices for all sales (if GST registered)
2. Retain all records for 5 years from lodgement date
3. Maintain motor vehicle logbook if claiming logbook method
4. Track home office hours if claiming fixed rate method
5. Monitor turnover for GST registration threshold ($75K)
6. Review PAYG instalment rate -- vary if income changes significantly
```

---

## Section 5 -- Refusals

**R-AU-1 -- Upstream skill did not run.** Name the specific skill. Note: this is a warning, not a hard stop. Continue with available data and flag the gap.

**R-AU-2 -- Upstream self-check failed.** Name the specific check and note it in the reviewer brief. Continue.

**R-AU-3 -- Cross-skill reconciliation failed.** Name the specific reconciliation and describe the discrepancy. Flag for reviewer but continue.

**R-AU-4 -- Intake incomplete.** Specific missing intake items prevent computation. List what is missing and ask the user for the specific data point.

**R-AU-5 -- Out-of-scope item discovered during assembly.** E.g., rental income requiring rental schedule, capital gains requiring CGT schedule, foreign income requiring FITO. Flag and exclude from computation.

---

## Section 6 -- Self-checks

**Check AU1 -- All upstream skills executed.** australia-gst, au-individual-return, au-super-guarantee, au-medicare-levy all produced output. au-payg-instalments produced output or was computed from ITR figures.

**Check AU2 -- BAS G1 matches ITR business income.** Within $1 tolerance.

**Check AU3 -- Super within concessional cap.** Total concessional contributions do not exceed $30,000 (or cap plus carry-forward unused amounts).

**Check AU4 -- Medicare levy surcharge correctly assessed.** MLS applied only if no adequate PHI and income above threshold; MLS not applied if PHI held for full year.

**Check AU5 -- PAYG instalments correctly credited.** Total instalments paid during 2024-25 credited against final tax liability.

**Check AU6 -- GST treatment correct for registered traders.** Business income reported ex-GST; input tax credits excluded from deductible expenses; GST credits claimed on BAS.

**Check AU7 -- GST treatment correct for unregistered traders.** Business income reported gross; all expenses reported gross (GST-inclusive); no BAS required.

**Check AU8 -- Instant asset write-off threshold correct.** Assets under $20,000 (on correct GST basis) claimed as immediate deduction; assets above threshold depreciated.

**Check AU9 -- Personal super deduction has s290-170 notice requirement flagged.** Reviewer brief notes that the taxpayer must lodge a notice of intent to claim with the super fund before the ITR is lodged.

**Check AU10 -- Tax rate table correct for residency.** Resident tax rates applied (including tax-free threshold of $18,200).

**Check AU11 -- HELP compulsory repayment calculated from repayment income.** Repayment income = taxable income + net investment loss + reportable fringe benefits + reportable super. Correct rate applied from HELP repayment thresholds.

**Check AU12 -- Filing calendar is complete.** All deadlines for BAS, ITR, super, and PAYG instalments are listed with specific dates and amounts.

---

## Section 7 -- Output files

The final output is **three files**:

1. **`[client_slug]_2024-25_australia_master.xlsx`** -- Single master workbook containing every worksheet and form. Sheets include: Cover, BAS Summary (quarterly), ITR (label-by-label), Depreciation Schedule, Expense Detail, Super Reconciliation, Medicare Levy, PAYG Instalments, Cross-Check Summary. Use live formulas where possible -- e.g., ITR business income references the BAS turnover cell; Medicare levy references ITR taxable income; PAYG credit references BAS instalment totals. Verify no `#REF!` errors. Verify computed values match the computation model within $1 before shipping.

2. **`reviewer_brief.md`** -- Single markdown file covering all sections from Section 4 above: executive summary, BAS, ITR, super, Medicare, PAYG, cross-skill reconciliation, flags, positions, planning notes.

3. **`client_action_list.md`** -- Single markdown file with step-by-step actions: immediate lodgements and payments, quarterly calendar for 2025-26, ongoing compliance reminders.

**If execution runs out of context mid-build:** produce whatever is complete, then state at the end which of the three files were not produced or are partial.

**All files are placed in `/mnt/user-data/outputs/` and presented to the user via the `present_files` tool at the end.**

---

## Section 8 -- Cross-skill references

**Inputs:**
- `au-freelance-intake` -- structured intake package (JSON)
- `australia-gst` -- BAS box values and GST output
- `au-individual-return` -- ITR label values and computation output
- `au-super-guarantee` -- Super reconciliation output
- `au-medicare-levy` -- Medicare levy and surcharge output
- `au-payg-instalments` -- Instalment schedule (or fallback computation)

**Outputs:** The final reviewer package. No downstream skill.

---

## Section 9 -- Known gaps

1. PDF form filling is not automated. The reviewer uses the worksheets to lodge via myTax or tax agent portal.
2. E-lodgement is handled by the reviewer via myTax or tax agent software, not by this skill.
3. Payment execution is the client's responsibility; the skill only provides instructions and amounts.
4. Rental income schedule is not supported -- if rental income exists, the skill flags it but the rental schedule must be completed separately by the reviewer.
5. Capital gains tax (CGT) schedule is not supported -- if capital gains exist, the skill flags it but the CGT schedule must be completed separately.
6. Foreign income and foreign income tax offset (FITO) are out of scope.
7. Multi-year depreciation tracking assumes the prior year schedule is provided. If not, only current-year acquisitions are depreciated.
8. au-payg-instalments is a Q4 stub. Until it is fleshed out, PAYG instalments are computed using the ATO's instalment rate method from the NOA. This is a redundancy, not a gap -- the rules are deterministic.
9. Several upstream content skills (australia-gst, au-individual-return, au-super-guarantee, au-medicare-levy) are Q2 skills. If any are still stubs, the assembly skill computes the figures directly and flags the gap.
10. The package is complete only for the 2024-25 tax year; 2025-26 appears only as prospective planning.

### Change log
- **v0.1 (April 2026):** Initial draft. Modelled on mt-return-assembly v0.1 adapted for Australian jurisdiction with five content skills (BAS, ITR, super, Medicare, PAYG).

## End of skill


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
