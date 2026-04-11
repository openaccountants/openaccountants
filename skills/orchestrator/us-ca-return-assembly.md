---
name: us-ca-return-assembly
description: Final orchestrator skill that assembles the complete federal and California filing package for California resident sole proprietors and single-member LLCs disregarded for federal tax. Consumes outputs from all federal content skills (bookkeeping, Schedule C/SE, QBI, retirement, SE health insurance, quarterly estimated tax, federal assembly, 1099-NEC) and all California content skills (540 individual return, 540-ES estimated tax, 568 SMLLC where applicable, 3853 coverage) to produce a single unified reviewer package containing every worksheet, every form, every brief section, all cross-skill reconciliations, and the final taxpayer action list with payment instructions, filing instructions, and 2026 planning. This is the capstone skill that runs last and produces the final deliverable. MUST be loaded alongside us-tax-workflow-base v0.2 or later and all content skills listed above. California residents only.
version: 0.2
---

# US+CA Return Assembly Skill v0.2

## CRITICAL EXECUTION DIRECTIVE — READ FIRST

**When this skill is invoked, you have already passed through intake. The user has consented to the full workflow. Execute all steps without pausing for permission.**

Specifically:

- **Do NOT ask the user "how deep do you want me to go"** or "do you want the full package" or any variant. The user asked for a tax return. They want the tax return. Produce it.
- **Do NOT announce how many tokens or tool calls this will take.** The user does not care about your tool budget. Execute.
- **Do NOT ask which deliverables to prioritize.** Produce all deliverables listed in Section 8. If you run out of context mid-execution, finish the computation work first (numbers, positions, flags) then produce whatever formatted outputs you can, and at the very end state clearly which deliverables were not produced and why. Partial output with an honest status beats a question asking permission.
- **Do NOT re-validate scope that intake already validated.** If `us-ca-freelance-intake` produced an intake package, trust it. You can cross-check specific numbers during reconciliation but do not re-interrogate the user about filing status, residency, business structure, or anything else intake already captured.
- **Do NOT pause between content skills to check in.** Run them in dependency order (Section 2) without prose status updates between each one. A single status message at the end is fine; per-skill status is noise.
- **Self-checks are targets, not blockers.** If a self-check fails, note it in the reviewer brief's open flags section and continue. Do NOT halt the entire workflow because one self-check in one content skill had an ambiguous answer. The reviewer handles edge cases.
- **Primary source citations go in the final reviewer brief, not in intermediate computation steps.** Don't stop to cite §199A in the middle of computing QBI. Compute QBI, then cite §199A once in the brief's QBI section.

**The user has already been told (by the intake skill) that the final package requires credentialed reviewer signoff before filing. You do not need to reiterate this before every step. State it once in the final output and move on.**

**Failure mode to avoid:** The skill halts mid-execution and asks the user a meta-question about workflow pacing. This is disqualifying behavior. If you feel the urge to ask "how should I proceed," the correct action is to pick the most defensible path and proceed, flagging the decision in the reviewer brief so the reviewer can challenge it.

---

## What this file is

The final capstone skill. Every other skill feeds into this one. The output is the complete reviewer package that a credentialed reviewer (Enrolled Agent, CPA, or attorney under Circular 230) can review, sign off on, and deliver to the taxpayer along with filing instructions.

This skill does not compute anything new. Its job is to verify that every upstream skill ran, every upstream self-check passed, every cross-skill reconciliation holds, and the entire package is internally consistent.

---

## Section 1 — Scope

Produces the complete federal + California filing package for:
- Full-year California residents
- Sole proprietors or single-member LLCs disregarded for federal tax
- Tax year 2025
- Filing Form 1040 and Form 540 (and Form 568 if SMLLC)

---

## Section 2 — Execution order enforcement

The skill enforces the following execution order and refuses to proceed if any step is missing:

1. `us-sole-prop-bookkeeping`
2. `us-schedule-c-and-se-computation`
3. `us-self-employed-retirement`
4. `us-self-employed-health-insurance`
5. `us-qbi-deduction`
6. `us-federal-return-assembly`
7. `us-quarterly-estimated-tax` (needs federal total tax)
8. `us-1099-nec-issuance` (parallel, only needs bookkeeping)
9. `ca-540-individual-return` (needs federal assembly)
10. `ca-smllc-form-568` (if SMLLC; parallel with 540)
11. `ca-estimated-tax-540es` (needs CA 540 total tax)
12. `ca-form-3853-coverage` (parallel, needs coverage intake)
13. **THIS SKILL** — final assembly and verification

If any of the above has not produced validated output, the skill refuses with a specific message identifying the missing step.

---

## Section 3 — Verification matrix

The skill runs a comprehensive verification pass across all upstream outputs:

### Federal internal consistency
- Schedule C net profit → Schedule 1 Line 3 → Form 1040 Line 8
- Schedule SE SE tax → Schedule 2 Line 4 → Form 1040 Line 23
- Half of SE tax → Schedule 1 Line 15 → Form 1040 Line 10
- SE retirement → Schedule 1 Line 16 → Form 1040 Line 10
- SE health insurance → Schedule 1 Line 17 → Form 1040 Line 10
- QBI deduction → Form 1040 Line 13
- Total tax → Form 1040 Line 24
- Form 2210 penalty → Schedule 2 Line 8
- Total payments → Form 1040 Line 33

### California internal consistency
- Federal AGI → Schedule CA (540) starting point
- QBI add-back → Schedule CA (540) additions
- HSA add-back if applicable → Schedule CA (540) additions
- Bonus depreciation add-back → Schedule CA (540) additions
- §179 cap difference → Schedule CA (540) additions
- California AGI → Form 540 Line 17
- California tax → Form 540 Line 31
- MHST → Form 540 Line 62 if applicable
- Form 5805 penalty → Form 540 Line 113
- Form 3853 penalty → Form 540 Line 92
- Form 568 balance (if SMLLC) → separate from Form 540

### Federal-California coordination
- Filing status consistent (MFJ federal + MFJ California)
- Dependents consistent
- Deduction election (standard vs itemized) may differ but must be documented
- Schedule C net profit used federally and on California Schedule CA match
- Depreciation recomputed for California if bonus or §179 differences exist

### 1099 issuance reconciliation
- Payments flagged for 1099-NEC match Schedule C Line 11 (Contract Labor) and related lines
- W-9 collection gaps identified
- Filing deadline noted (January 31, 2026)

---

## Section 4 — Final reviewer package contents

### Documents
1. **Executive summary** — one-page overview: filing status, income, federal tax, state tax, total liability, refund/balance due
2. **Federal Form 1040 worksheet** — line-by-line with formulas
3. **Schedule 1** — adjustments to income
4. **Schedule 2** — additional taxes
5. **Schedule 3** — credits and payments (if applicable)
6. **Schedule C** — sole prop P&L
7. **Schedule SE** — SE tax
8. **Form 8995 or 8995-A** — QBI
9. **Form 7206** — SE health insurance worksheet
10. **Form 8962** — PTC reconciliation (if marketplace coverage)
11. **Form 2210** — underpayment penalty (if applicable)
12. **Form 4562** — depreciation (if applicable)
13. **Form 8829** — home office actual method (if applicable)
14. **Form 1040-ES** — 2026 prospective payment schedule
15. **California Form 540** — state return worksheet
16. **California Schedule CA (540)** — state adjustments
17. **California Form 5805** — state underpayment penalty (if applicable)
18. **California Form 3853** — individual mandate (if applicable)
19. **California Form 540-ES** — 2026 state prospective payment schedule
20. **California Form 568** — SMLLC return (if applicable)
21. **Form 3522** — $800 LLC tax voucher (if applicable)
22. **Form 3536** — LLC fee estimation voucher (if applicable)
23. **1099-NEC batch** — contractor information returns (if applicable)
24. **Reviewer brief** — comprehensive narrative with positions, citations, flags, self-check results
25. **Taxpayer action list** — what the taxpayer needs to do, with dates and amounts

### Reviewer brief contents

```markdown
# Complete Return Package: [Taxpayer Name] — Tax Year 2025

## Executive Summary
- Filing status: [X]
- Residence: California (full-year)
- Business: Sole proprietor / Single-member LLC disregarded
- Federal total tax: $X
- California total tax: $X
- Total 2025 tax liability: $X
- Total payments (federal + CA): $X
- Net refund or balance due: $X
- Action required by April 15, 2026: [summary]

## Federal Return
[Content from us-federal-return-assembly brief]

## California Return
[Content from ca-540-individual-return brief]

## California SMLLC (if applicable)
[Content from ca-smllc-form-568 brief]

## Individual Mandate
[Content from ca-form-3853-coverage brief]

## Estimated Tax
[Content from us-quarterly-estimated-tax brief]
[Content from ca-estimated-tax-540es brief]

## 1099 Issuance
[Content from us-1099-nec-issuance brief]

## Cross-skill verification
- All upstream skills ran: [verified]
- All upstream self-checks passed: [verified]
- All cross-form reconciliations passed: [verified]
- Specific checks: [list]

## Reviewer attention flags
[Aggregated from all upstream skills]

## Refusals triggered
[Any refusals from any skill in the chain]

## Positions taken
[Aggregated list with citations]

## Planning notes for 2026
- Federal estimated tax schedule
- California estimated tax schedule
- S-corp election consideration (if applicable)
- 2026 rate changes (QBI 20% → 23%, 1099 threshold $600 → $2,000)
- Expanded PTC expiration after 2025
- Retirement contribution planning
- W-9 collection for contractors
- Other

## Taxpayer action list

### Before April 15, 2026:
1. Review and sign this return package
2. Sign Form 8879 (e-file authorization) — if e-filing
3. Pay federal balance due of $X via EFTPS, Direct Pay, or check
4. Pay California balance due of $X via FTB Web Pay or check
5. File Form 568 and pay $800 LLC tax + $X LLC fee (if applicable)
6. Pay 2026 Q1 federal estimated tax of $X
7. Pay 2026 Q1 California estimated tax of $X (30% installment)

### Before January 31, 2026 (ALREADY PASSED — check if done):
1. File 1099-NEC forms with IRS (IRIS or FIRE)
2. Furnish Copy B to contractors
3. If missed, assess penalty exposure and file ASAP

### Before June 15, 2026:
1. Pay 2026 Q2 federal estimated tax of $X
2. Pay 2026 Q2 California estimated tax of $X (40% installment)
3. Pay 2026 Form 3536 LLC fee estimate of $X (if applicable)

### Before September 15, 2026:
1. Pay 2026 Q3 federal estimated tax of $X
2. California Q3 is $0 under 30/40/0/30 rule — no payment needed

### Before January 15, 2027:
1. Pay 2026 Q4 federal estimated tax of $X
2. Pay 2026 Q4 California estimated tax of $X (30% installment)

### Ongoing:
1. Collect W-9 from new contractors before paying them
2. Track business expenses with receipts
3. Monitor income to adjust Solo 401(k) contribution
4. Watch for mid-year health coverage changes
```

---

## Section 5 — Refusals

**R-FINAL-1 — Upstream skill did not run.** Name the specific skill.

**R-FINAL-2 — Upstream self-check failed.** Name the specific check.

**R-FINAL-3 — Cross-skill reconciliation failed.** Name the specific reconciliation and describe the discrepancy.

**R-FINAL-4 — Refusal hidden upstream.** A refusal from an upstream skill was not surfaced in its output. Name the refusal and force resolution.

**R-FINAL-5 — Taxpayer intake incomplete.** Specific missing intake items prevent final assembly.

---

## Section 6 — Self-checks

**Check 130 — All upstream skills executed.**
**Check 131 — All upstream self-checks passed.**
**Check 132 — Federal internal consistency verified.**
**Check 133 — California internal consistency verified.**
**Check 134 — Federal-California coordination verified.**
**Check 135 — 1099-NEC reconciliation verified.**
**Check 136 — Taxpayer action list is complete with dates and amounts.**
**Check 137 — Planning notes include 2026 changes (QBI rate, 1099 threshold, PTC expiration).**
**Check 138 — Every refusal in the catalogue was evaluated against taxpayer facts.**
**Check 139 — Every reviewer attention flag is surfaced.**
**Check 140 — Payment instructions are specific (amount, method, due date).**

---

## Section 7 — Output files

The final output is **three files** (not eleven — do not fragment the package):

1. **`[taxpayer_slug]_2025_master.xlsx`** — Single master workbook containing every worksheet and form. Sheets include: Cover, Income, Schedule C (Parts I-V), Form 4562, Form 8829, Schedule SE, Retirement, SE Health, Form 8962, Form 8995-A (or 8995), Schedule 1, Form 1040, Form 2210, Form 540, Schedule CA (540), Form 5805, Form 568, Schedule IW, Form 3853, 1099-NEC batch, 2026 Est Tax. Use the Excel builder pattern specified in `us-federal-return-assembly` — collect anchors as a Python dict before writing cross-sheet formulas, verify no `#REF!` errors, verify computed values match the Python model within $1 before shipping.

2. **`reviewer_brief.md`** — Single markdown file covering all sections: taxpayer summary, Schedule C summary, SE tax, retirement, SE health insurance, QBI, federal tax computation, California tax computation, Form 568 (if SMLLC), cross-jurisdiction reconciliation, open flags for reviewer, self-check results, primary source citations, position statements for anything requiring reviewer judgment.

3. **`taxpayer_action_list.md`** — Single markdown file with step-by-step actions for the taxpayer: this week (corrective actions, late 1099 filings), before reviewer finishes, by April 15 (signing, payments, estimates), and year-ahead planning items.

**If execution runs out of context mid-build:** produce whatever is complete, then state at the end which of the three files were not produced or are partial. Three files with honest status beats eleven files partially built.

**All files are placed in `/mnt/user-data/outputs/` and presented to the user via the `present_files` tool at the end.**

---

## Section 8 — Cross-skill references

Inputs: every other skill in the product.

Outputs: the final reviewer package. No downstream skill.

---

## Section 9 — Known gaps

1. PDF form filling is not automated. The reviewer uses the worksheets to fill official IRS/FTB forms in their tax software.
2. E-filing is handled by the reviewer, not by this skill.
3. Payment execution is the taxpayer's responsibility; the skill only provides instructions.
4. Multi-state returns not supported (California only).
5. Foreign income not supported.
6. The package is complete only for the 2025 tax year; 2026 appears only as prospective planning.

### Change log
- **v0.1 (April 2026):** Initial draft.

## End of skill


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
