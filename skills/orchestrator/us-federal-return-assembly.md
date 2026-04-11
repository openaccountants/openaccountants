---
name: us-federal-return-assembly
description: Tier 2 orchestrator skill that assembles the complete federal income tax return package for US freelance software developers filing as sole proprietors or single-member LLCs disregarded for federal tax. Sequences the upstream content skills (bookkeeping, SE computation, retirement, SE health insurance, QBI, estimated tax) in dependency order, resolves circular computations between SE health insurance and retirement contributions, produces Form 1040 with all required schedules (Schedule 1, Schedule 2, Schedule 3, Schedule C, Schedule SE, Schedule D if needed, Form 8829, Form 4562, Form 8995 or 8995-A, Form 8962 if marketplace coverage, Form 2210 if penalty, Form 7206), performs cross-form reconciliation checks, and produces the final reviewer package. Does not itself compute tax amounts — delegates to upstream content skills. MUST be loaded alongside us-tax-workflow-base v0.2 or later and all content skills it orchestrates. Federal only.
version: 0.2
---

# US Federal Return Assembly Skill v0.2

## CRITICAL EXECUTION DIRECTIVE — READ FIRST

**When this skill is invoked, either directly or via `us-ca-return-assembly`, execute the full workflow without pausing for user permission.**

- **Do NOT ask "how deep should I go"** or "do you want the full package." The answer is always: full package, all deliverables, every step.
- **Do NOT announce your token budget.** Run the work.
- **Do NOT pause between content skills for status updates.** One consolidated status message at the end is fine. Per-skill status between each upstream skill is noise.
- **Self-checks are targets, not blockers.** If a check fails, flag it in the reviewer brief and continue. Do not halt the workflow for ambiguous edge cases — the reviewer handles those.
- **If you run out of context mid-execution,** finish the computation work (numbers, positions, flags) first, then produce whatever formatted deliverables you can, and state clearly at the end which were not produced. Partial output with an honest status beats a question asking permission.
- **Primary source citations belong in the final reviewer brief,** not in intermediate computation steps. Compute first, cite once at the end.

**Failure mode to avoid:** halting mid-execution to ask the user a meta-question about workflow pacing. If you feel the urge to ask "how should I proceed," pick the most defensible path and proceed, flagging the decision in the reviewer brief.

---

## What this file is

This is an **orchestrator** skill, not a content skill. It does not contain tax computation rules — those live in the content skills (`us-sole-prop-bookkeeping`, `us-schedule-c-and-se-computation`, `us-self-employed-retirement`, `us-self-employed-health-insurance`, `us-qbi-deduction`, `us-quarterly-estimated-tax`). This skill's job is to:

1. **Sequence** the content skills in dependency order
2. **Resolve** the circular computations (specifically the SE health insurance + retirement + QBI interaction)
3. **Assemble** the final Form 1040 and all supporting schedules
4. **Cross-check** that amounts flowing between forms tie out
5. **Produce** the reviewer package (Form 1040, schedules, Excel working paper, reviewer brief)

**Tax year:** 2025

**The reviewer is still the customer.** The orchestrator produces a package ready for a credentialed reviewer to review and sign. It does not file the return.

---

## Section 1 — Scope

Taxpayers covered: same as the upstream content skills. US sole proprietors and SMLLC disregarded for federal tax, filing Form 1040 for tax year 2025.

Out of scope: anything refused by the base or any content skill.

---

## Section 2 — The dependency graph

The content skills must be run in a specific order because of forward references and circular dependencies.

```
Bookkeeping (us-sole-prop-bookkeeping)
  └→ produces: classified transactions, Schedule C line totals, owner draws
     │
     ↓
SE Computation (us-schedule-c-and-se-computation)
  └→ consumes: bookkeeping output
  └→ produces: Schedule C Line 31, Schedule SE Line 12, Schedule 1 Line 15 (half SE tax)
     │
     ↓
Retirement (us-self-employed-retirement)
  └→ consumes: Schedule C Line 31, half of SE tax
  └→ produces: Schedule 1 Line 16 (retirement contribution deduction)
     │
     ↓
SE Health Insurance (us-self-employed-health-insurance)
  └→ consumes: Schedule C Line 31, half of SE tax, Schedule 1 Line 16
  └→ produces: Schedule 1 Line 17 (SE health insurance deduction)
     │
     ↓
QBI (us-qbi-deduction)
  └→ consumes: Schedule C Line 31, Schedule 1 Lines 15/16/17, taxable income before QBI
  └→ produces: QBI deduction (Form 1040 Line 13)
     │
     ↓
Federal Return Assembly (this skill)
  └→ assembles: Form 1040 with all schedules
  └→ cross-checks: amounts tie across forms
     │
     ↓
Estimated Tax (us-quarterly-estimated-tax)
  └→ consumes: Form 1040 Line 24 (total tax) from this year
  └→ produces: Form 2210 penalty (if any), 2026 installment plan
```

**The circular subproblem:** QBI depends on taxable income before QBI, which depends on all deductions including QBI itself if done naively. The IRS resolves this by defining "taxable income before QBI" as taxable income computed without the QBI deduction. So the order is:
1. Compute all other adjustments to income (Schedule 1 Lines 11-25)
2. Compute AGI (Form 1040 Line 11)
3. Compute taxable income before QBI (AGI minus standard/itemized deduction)
4. Apply QBI using that taxable income as the threshold test
5. Compute final taxable income (taxable income before QBI minus QBI deduction)

**The SE health insurance + PTC iterative problem:** Already handled inside the SE health insurance skill via Rev. Proc. 2014-41. The orchestrator does not re-solve it.

---

## Section 3 — Workflow steps

### Step 1: Trigger intake and profile the taxpayer

Run the base intake (Tier 1 refusal sweep plus Tier 2 structured questions). Confirm the taxpayer is in scope. Confirm the reviewer is identified.

### Step 2: Run bookkeeping skill

Produce classified Schedule C transactions and line totals. Verify the 10 bookkeeping self-checks pass.

### Step 3: Run SE computation skill

Produce Schedule C Line 31, Schedule SE, and Schedule 1 Line 15. Verify the 17 computation self-checks pass.

### Step 4: Run retirement skill

Produce Schedule 1 Line 16. Verify retirement self-checks pass.

### Step 5: Run SE health insurance skill (with PTC iteration if applicable)

Produce Schedule 1 Line 17. Verify self-checks pass. If PTC iteration did not converge, halt and escalate to reviewer.

### Step 6: Compute other Schedule 1 items

Other Schedule 1 lines that may be relevant:
- Line 11: Educator expenses (not usually applicable for freelance developers)
- Line 12: Certain business expenses of reservists, performing artists, fee-basis government officials (not applicable)
- Line 13: HSA deduction (if the taxpayer has an HSA-qualified HDHP)
- Line 14: Moving expenses for members of the Armed Forces (not applicable)
- Line 18: Penalty on early withdrawal of savings
- Line 19a: Alimony paid (divorce agreements before 1/1/2019 only)
- Line 20: IRA deduction (from retirement skill if taxpayer made a traditional IRA contribution)
- Line 21: Student loan interest deduction (subject to income phase-out)
- Line 22: Reserved
- Line 23: Archer MSA deduction
- Line 24a-24z: Various other adjustments
- Line 25: Total other adjustments

The orchestrator handles HSA, student loan interest, and other adjustments either itself (simple cases) or by refusing and flagging for the reviewer (complex cases). For v0.1, the orchestrator handles only the items flagged in the intake.

### Step 7: Compute AGI

AGI (Form 1040 Line 11) = Total income (Line 9) − Adjustments from Schedule 1 Line 26.

### Step 8: Compute taxable income before QBI

- Standard deduction for 2025:
  - Single: $15,000
  - MFJ / QSS: $30,000
  - HoH: $22,500
  - MFS: $15,000
- OR itemized deductions from Schedule A
- Taxable income before QBI = AGI − greater of standard or itemized

### Step 9: Run QBI skill

Using the taxable income before QBI as the threshold test input. Produces QBI deduction for Form 1040 Line 13. Verify QBI self-checks pass.

### Step 10: Compute final taxable income

Form 1040 Line 15 = Line 11 − Line 12 (standard/itemized) − Line 13 (QBI).

### Step 11: Compute tax

Apply the 2025 tax brackets from Rev. Proc. 2024-40 to the final taxable income. Include:
- Regular income tax (using tax tables for income under $100K or tax rate schedules above)
- Capital gains tax (if applicable, from Schedule D)
- Other taxes (Schedule 2 Line 3)

**2025 tax brackets (ordinary income):**

Single:
- 10% on income up to $11,925
- 12% on $11,925 to $48,475
- 22% on $48,475 to $103,350
- 24% on $103,350 to $197,300
- 32% on $197,300 to $250,525
- 35% on $250,525 to $626,350
- 37% over $626,350

MFJ:
- 10% on income up to $23,850
- 12% on $23,850 to $96,950
- 22% on $96,950 to $206,700
- 24% on $206,700 to $394,600
- 32% on $394,600 to $501,050
- 35% on $501,050 to $751,600
- 37% over $751,600

HoH:
- 10% on income up to $17,000
- 12% on $17,000 to $64,850
- 22% on $64,850 to $103,350
- 24% on $103,350 to $197,300
- 32% on $197,300 to $250,500
- 35% on $250,500 to $626,350
- 37% over $626,350

**Source:** Rev. Proc. 2024-40 §3.01.

### Step 12: Compute Schedule 2 (additional taxes)

Schedule 2 Line 4: SE tax from Schedule SE
Schedule 2 Line 2: Excess advance PTC repayment (from SE health insurance skill)
Schedule 2 Line 11: Additional Medicare Tax (Form 8959) if applicable
Schedule 2 Line 12: Net Investment Income Tax (Form 8960) if applicable
Schedule 2 Line 21: Total other taxes

**Additional Medicare Tax thresholds (2025):**
- Single / HoH: $200,000
- MFJ: $250,000
- MFS: $125,000

Tax = 0.9% × (wages + SE earnings − threshold)

**NIIT thresholds (2025):** Same as Additional Medicare Tax. Tax = 3.8% × (net investment income, capped at MAGI − threshold). Generally doesn't apply to pure freelance Schedule C income because Schedule C earnings are not "net investment income" — they're earned income. But if the taxpayer has meaningful investment income, NIIT may apply.

### Step 13: Compute Schedule 3 (credits and payments)

Schedule 3 Line 1: Foreign tax credit (refusal if material — refer to base)
Schedule 3 Line 2: Child and dependent care expenses credit
Schedule 3 Line 3: Education credits (Form 8863)
Schedule 3 Line 4: Retirement savings contributions credit (Saver's credit, subject to income limits)
Schedule 3 Line 6: Other nonrefundable credits
Schedule 3 Line 9: Net premium tax credit (from Form 8962 if net PTC is refundable)
Schedule 3 Line 10: Amount paid with extension request (Form 4868)
Schedule 3 Line 11: Excess social security and tier 1 RRTA tax withheld

### Step 14: Compute total tax and payments

- Form 1040 Line 22: Subtract Schedule 3 nonrefundable credits
- Form 1040 Line 23: Other taxes (from Schedule 2)
- Form 1040 Line 24: Total tax
- Form 1040 Line 25: Federal income tax withheld (from W-2s, 1099s)
- Form 1040 Line 26: 2024 estimated tax payments and amount applied from prior year
- Form 1040 Line 27: Earned income credit (generally not applicable for freelance developers above poverty line)
- Form 1040 Line 28: Additional child tax credit
- Form 1040 Line 29: Refundable American opportunity credit
- Form 1040 Line 31: Amount from Schedule 3 Line 15 (refundable credits)
- Form 1040 Line 33: Total payments

### Step 15: Compute refund or balance due

- If Line 33 > Line 24: Refund (Line 34)
- If Line 33 < Line 24: Balance due (Line 37)

### Step 16: Run estimated tax skill for Form 2210 and 2026 planning

Using the final total tax (Line 24), compute Form 2210 penalty if any installments were underpaid. Also compute 2026 quarterly installments for prospective planning.

### Step 17: Cross-form reconciliation checks

See Section 4.

### Step 18: Produce the reviewer package

See Section 5.

---

## Section 4 — Cross-form reconciliation checks

The orchestrator verifies that amounts match between forms before producing output. Any mismatch is a hard error that stops assembly.

**Check A: Schedule C Line 31 matches Schedule SE Line 2.** If they don't match, one of the skills has a bug.

**Check B: Schedule SE Line 13 (deductible half of SE tax) matches Schedule 1 Line 15.** Same as above.

**Check C: Form 8995/8995-A QBI deduction matches Form 1040 Line 13.** Same.

**Check D: Schedule 1 total (Line 26) equals sum of Lines 11-25.** Arithmetic check.

**Check E: Form 1040 Line 9 equals sum of Line 1a + Line 2b + Line 3b + Line 4b + Line 5b + Line 6b + Line 7 + Line 8 (from Schedule 1 Line 10).** Arithmetic.

**Check F: Form 1040 Line 11 (AGI) = Line 9 − Line 10.** Arithmetic.

**Check G: Form 1040 Line 15 (taxable income) = Line 11 − Line 12 − Line 13, but not less than zero.** Arithmetic.

**Check H: Form 1040 Line 24 (total tax) = Line 22 + Line 23.** Arithmetic.

**Check I: QBI used correct "taxable income before QBI."** The amount on Form 8995 Line 11 / Form 8995-A Line 34 should equal Form 1040 Line 11 minus Line 12 (standard or itemized deduction), before subtracting Line 13 (QBI).

**Check J: Form 8962 reconciliation matches Schedule 2 Line 2 (repayment) or Schedule 3 Line 9 (net PTC).** Marketplace coverage.

**Check K: If Form 2210 is filed, the penalty matches Form 1040 Line 38.**

**Check L: Schedule 2 Line 4 (SE tax) equals Schedule SE Line 12.**

**Check M: Total payments on Form 1040 Line 33 equals sum of Lines 25a-25c + 26 + 27 + 28 + 29 + 31.**

**Check N: Form 1040 Line 34 (refund) or Line 37 (amount you owe) = Line 33 − Line 24. Exactly one of these is positive.**

If any check fails, the orchestrator halts and escalates. The reviewer must be informed that assembly could not complete.

---

## Section 5 — Reviewer package output

The orchestrator produces these artifacts:

### Excel builder pattern (CRITICAL — read before building the workbook)

The Alex Chen test run revealed a failure mode: building the Excel workbook by inlining cell references (e.g., `='Sch C'!B45`) leads to row-reference collisions when content is added or reordered. The first-pass builder hit multiple bugs where formulas pointed at the wrong rows because the layout shifted as sheets were filled in. The second-pass fix required scrapping the first builder and starting over.

**The pattern that works:**

1. **Build a single Python dict of every anchor cell BEFORE writing any formula.** The dict maps human-readable keys to cell coordinates:
   ```python
   anchors = {
       'sch_c.line_31_net_profit': None,  # filled in when row is written
       'sch_se.line_12_se_tax': None,
       'sch_1.line_15_half_se_tax': None,
       'sch_1.line_16_retirement': None,
       'sch_1.line_17_se_health': None,
       'form_1040.line_11_agi': None,
       'form_1040.line_13_qbi': None,
       'form_1040.line_15_taxable_income': None,
       # ... every anchor the workbook will reference
   }
   ```

2. **Write sheets in dependency order** (Schedule C first, then SE, then Schedule 1, then QBI, then Form 1040). As you write each row, record the actual cell coordinate in the anchors dict:
   ```python
   row = 42
   ws['A' + str(row)] = 'Line 31 — Net profit'
   ws['B' + str(row)] = '=B27-B40'  # whatever the formula is
   anchors['sch_c.line_31_net_profit'] = f"'Sch C'!B{row}"
   ```

3. **Only use anchors when writing cross-sheet formulas:**
   ```python
   # GOOD
   ws['B15'] = f"={anchors['sch_c.line_31_net_profit']}"
   
   # BAD
   ws['B15'] = "='Sch C'!B45"  # will break if Sch C layout changes
   ```

4. **Assert every anchor is filled before writing cross-sheet formulas.** Run a check like:
   ```python
   missing = [k for k, v in anchors.items() if v is None]
   assert not missing, f"Missing anchors: {missing}"
   ```

5. **After building, run openpyxl's formula verification** by opening the file with `data_only=False`, iterating every formula cell, and confirming no `#REF!` or `#NAME?` errors.

6. **Verify computed values against the Python model.** The orchestrator has already computed every number in Python. Before shipping the workbook, open it with `data_only=True` (or use libreoffice headless recalc) and compare key cells (net profit, AGI, total tax, balance due) against the Python numbers. Mismatches greater than $1 are bugs — investigate and fix before shipping.

**Why this matters:** Excel workbooks that claim to be the authoritative computation but contain formula bugs are worse than no workbook. A reviewer who trusts the workbook and finds errors loses confidence in the entire package. Get the workbook right or don't ship it.

**If you run out of context mid-workbook build:** ship a simplified flat-value workbook (just the final numbers, no cross-sheet formulas) with a note in the reviewer brief that "the live-formula working paper was not completed due to execution constraints; numbers are final but not interactively recomputable." Flat values with an honest note beat broken formulas.

### Artifact 1: Excel working paper (`[taxpayer]_2025_federal_working_paper.xlsx`)

Sheets:
- **Summary** — Form 1040 line-by-line in spreadsheet form, with cell references to supporting sheets
- **Schedule C** — line by line, with references to transaction classifications
- **Schedule SE** — line by line
- **Schedule 1** — line by line
- **Schedule 2** — line by line
- **Schedule 3** — line by line (if used)
- **Form 8829** — home office (if claimed)
- **Form 4562** — depreciation (if claimed)
- **Form 8995 or 8995-A** — QBI
- **Form 8962** — PTC reconciliation (if marketplace coverage)
- **Form 2210** — underpayment penalty (if any)
- **Form 7206** — SE health insurance worksheet
- **Downstream items** — Schedule 1 Lines 15/16/17 used as inputs
- **Transactions** — the raw classified transaction list from bookkeeping

### Artifact 2: Reviewer brief (`[taxpayer]_2025_reviewer_brief.md`)

Sections:
1. **Taxpayer summary** — name, filing status, scope confirmation, refusals triggered (none if assembly completed)
2. **Schedule C summary** — gross receipts, major expense categories, net profit
3. **SE tax** — net SE earnings, SE tax, deductible half
4. **Retirement contributions** — plan type, amount, Schedule 1 Line 16
5. **SE health insurance** — coverage type, eligible months, PTC interaction if any, Schedule 1 Line 17
6. **QBI deduction** — SSTB determination, threshold test, form used, deduction amount
7. **Tax computation** — taxable income, regular tax, SE tax, other taxes, total tax
8. **Payments and refund/balance due**
9. **Form 2210 penalty** — if applicable
10. **2026 estimated tax plan** — recommended quarterly installments
11. **Open questions for reviewer** — any flags that need reviewer judgment
12. **Citations** — primary sources for every significant position

### Artifact 3: Form package (PDF or fillable PDFs)

For v0.1, the orchestrator produces a structured JSON representation of every form line, and flags that PDF rendering is a separate downstream step (handled by a future rendering module, not by this skill).

### Artifact 4: Form 1040-ES vouchers for 2026

Four quarterly vouchers with the recommended installment amounts, due dates, and payment instructions.

---

## Section 6 — Refusals specific to orchestration

**R-ASSY-1 — Cross-form reconciliation failure.** If any reconciliation check in Section 4 fails, halt assembly and produce a diagnostic report. "Assembly failed: Schedule C Line 31 does not match Schedule SE Line 2. Upstream skill output is inconsistent. Reviewer must investigate before proceeding."

**R-ASSY-2 — Upstream skill did not produce expected output.** If any content skill failed its self-checks, the orchestrator does not proceed. "Upstream skill [name] failed self-check [N]. Assembly cannot proceed until the upstream issue is resolved."

**R-ASSY-3 — Taxpayer has income or deduction types not handled by any content skill.** Examples: royalties, schedule E income, rental income, K-1 from a partnership, capital gains from crypto. Halt assembly and refuse.

**R-ASSY-4 — Total tax calculation produces negative or nonsensical result.** "Total tax computed as [value], which is not plausible. Assembly halted for reviewer investigation."

**R-ASSY-5 — Required information still missing after intake.** "The following information is still missing: [list]. Assembly halted."

---

## Section 7 — Self-checks

**Check 79 — All upstream content skills completed successfully.** Each content skill's self-checks passed and produced its expected output.

**Check 80 — All reconciliation checks (A through N) passed.**

**Check 81 — No refusals fired during assembly.**

**Check 82 — Working paper has all expected sheets.**

**Check 83 — Reviewer brief covers all required sections.**

**Check 84 — All tax amounts are rounded consistently (to whole dollars, per IRS convention).**

**Check 85 — Primary source citations present for every significant position.**

**Check 86 — Reviewer identified and reviewer attention flags are listed.**

**Check 87 — 2026 estimated tax vouchers produced if taxpayer has a 2026 obligation.**

**Check 88 — CA state skill handoff data prepared (if taxpayer is CA resident).** The federal return produces certain numbers that the CA return needs (federal AGI, QBI deduction amount for add-back, etc.). This skill prepares those as a handoff package.

---

## Section 8 — Handoff to state skills

If the taxpayer is a California resident, this skill produces a handoff package containing:

- Federal AGI (Form 1040 Line 11) → CA Schedule CA (540) Part I Line 11
- Federal QBI deduction → CA Schedule CA (540) add-back
- Federal §179 deduction and bonus depreciation → CA Schedule CA (540) add-back (California decouples)
- Federal Schedule C net profit → CA Schedule CA Part I
- Federal Schedule SE → CA does not have SE tax at state level, but AGI reconciliation needs this
- Federal Schedule 1 Line 17 (SE health insurance) → CA conforms; no adjustment
- Federal Schedule 1 Line 16 (retirement) → CA conforms; no adjustment
- Federal Form 8962 (PTC) → CA uses its own state subsidy computation if Covered California
- Federal estimated tax payments → flag for CA 540-ES comparison

This handoff is consumed by the `ca-540-individual-return` skill.

---

## Section 9 — Reference material

### Known gaps
1. **PDF rendering is not implemented.** The orchestrator produces JSON and Excel; PDF generation requires a separate rendering module.
2. **E-file submission is not handled.** The reviewer uses a separate e-file provider after review.
3. **Amended returns (Form 1040-X) are out of scope.** Only original returns.
4. **Estimated tax payment tracking across the year** (separate from the return itself) is not handled — the taxpayer must manually track and report what was paid when.
5. **The orchestrator assumes all upstream skills produce output in a consistent JSON-like schema.** Schema versioning is a v0.2 concern.

### Change log
- **v0.1 (April 2026):** Initial draft for freelance software developer product.

## End of US Federal Return Assembly Skill v0.1


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
