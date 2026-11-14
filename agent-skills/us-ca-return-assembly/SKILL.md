---
name: us-ca-return-assembly
description: "Final assembly of the 2026 federal and California return package for a full-year California resident sole proprietor or single-member LLC owner. Runs the skills in dependency order (bookkeeping, Schedule C and SE, retirement, health insurance, QBI, federal assembly, federal estimates, 1099-NEC, California Form 540, Form 568, California estimates, form FTB 3853), then checks that each figure lands where the next form expects it, that federal and California agree where they must and differ only where California law says so, and produces three files for a credentialed reviewer (master workbook, reviewer brief, taxpayer action list). Trigger after us-ca-freelance-intake on \"assemble the return\", \"finish my federal and California return\", \"reviewer package\", \"complete return package California\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-ca-return-assembly"
  jurisdiction: "US-CA"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Federal and California return assembly for a California freelancer, tax year 2026

> **Source-cited draft.** Built from the 2025 Form 540 and its booklet, the 2026 Form 540-ES instructions and the FTB extension page, read on 2026-11-13, and from the skills it routes to. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** This skill computes nothing new. It runs the federal and California skills in the order below, checks that every figure carries to the right line, records every refusal and judgment call, and hands a credentialed reviewer (enrolled agent, CPA or attorney) three files: a master workbook, a reviewer brief and a taxpayer action list. If an upstream skill did not run or a check fails, it says which one and carries on to the end rather than stopping to ask how to proceed.

## Scope and who this is for

A full-year California resident, sole proprietor or single-member LLC disregarded for federal tax, tax year 2026 (or 2025 on extension, with that year's figures), filing Form 1040, Form 540 and, for an LLC, Form 568. Out of scope: multi-state returns, foreign income, partnerships and corporations, e-filing itself (the reviewer files), and paying (the taxpayer pays).

## The method, step by step

### How it runs

- Use what intake (`us-ca-freelance-intake`) collected. Ask the user again only where something is missing or contradicts itself; do not re-interrogate filing status, residency or entity.
- Do not ask how deep to go, which deliverables to prioritize, or announce a tool budget. Produce the package.
- Run the skills in order without status messages between them; one status line at the end.
- A failed self-check is a flag in the reviewer brief, not a stop.
- Cite sources once, in the reviewer brief, not in the middle of each computation.
- State once, in the final output, that a credentialed reviewer must sign off before filing.
- If context runs short, finish the numbers, positions and flags first, then state which files are missing or partial.

### Order of the skills

| Step | Skill | Needs |
| --- | --- | --- |
| 1 | `us-sole-prop-bookkeeping` | Intake package |
| 2 | `us-schedule-c-and-se-computation` | Step 1 |
| 3 | `us-self-employed-retirement` | Step 2 |
| 4 | `us-self-employed-health-insurance` | Step 2 |
| 5 | `us-qbi-deduction` | Steps 2 to 4 |
| 6 | `us-federal-return-assembly` | Steps 2 to 5 |
| 7 | `us-quarterly-estimated-tax` | Federal total tax from step 6 |
| 8 | `us-1099-nec-issuance` | Step 1 (can run beside 2 to 7) |
| 9 | `ca-540-individual-return` (figures from `ca-income-tax`) | Federal AGI from step 6 |
| 10 | `ca-smllc-form-568` and `ca-llc-fee-and-tax` | LLC only; beside step 9 |
| 11 | `ca-estimated-tax-540es` | California total tax from step 9 |
| 12 | `ca-form-3853-coverage` | Coverage by month from intake; beside step 9 |
| 13 | This skill | Steps 1 to 12 |

### Checks that figures carry

**Federal.** Schedule C net profit to Schedule 1 and Form 1040; Schedule SE tax to Schedule 2; half of SE tax, SE retirement and SE health insurance to Schedule 1 adjustments; QBI deduction below AGI; total tax; Form 2210 penalty; total payments. Line numbers come from `us-federal-return-assembly` for the 2026 forms.

**California** (2025 Form 540 line numbers until the 2026 form is published):

| From | To |
| --- | --- |
| Federal AGI | Form 540 line 13 |
| Schedule CA (540) Part I line 27 column B and column C | Lines 14 and 16 |
| Bonus depreciation and section 179 differences (FTB 3885A) | Schedule CA Section B line 3 |
| HSA deduction and employer HSA | Schedule CA Section C line 13 column B; line 1h column C |
| QBI deduction | Nothing: it is below federal AGI |
| California AGI | Line 17 |
| Tax | Line 31; exemption credits line 32 |
| Behavioral Health Services Tax | Line 62 (taxable income over $1,000,000) |
| Use tax | Line 91 (never blank) |
| FTB 3853 penalty or full-year coverage box | Line 92 |
| FTB 5805 penalty | Line 113 |
| Form 568 balance | Separate from Form 540 |

**Federal and California together.** Same filing status and dependents (RDP exceptions documented); standard or itemized may differ but the choice is documented; the Schedule C profit used federally is the start of Schedule CA; California depreciation recomputed where bonus or section 179 differs; 1099-NEC payees match contract labor on Schedule C and W-9 gaps are listed with the January 31, 2027 due date.

### The three output files

1. **`<taxpayer>_2026_master.xlsx`**: one workbook with every worksheet and form (cover, income, Schedule C, Form 4562, Form 8829, Schedule SE, retirement, SE health, Form 8962, Form 8995 or 8995-A, Schedules 1 and 2, Form 1040, Form 2210, Form 540, Schedule CA (540), FTB 5805, Form 568, FTB 3853, 1099-NEC batch, 2027 estimates). Build the cross-sheet anchors first, check there is no #REF!, and check each computed value against the model within $1.
2. **`reviewer_brief.md`**: taxpayer summary; each computation (Schedule C, SE tax, retirement, SE health, QBI, federal tax, California tax, Form 568); federal and California reconciliation; reviewer attention flags; refusals triggered; positions taken; self-check results; sources.
3. **`taxpayer_action_list.md`**: what the taxpayer must do, with dates and amounts: corrective actions now (late 1099s, DE 542), before April 15, 2027 (sign, pay, first 2027 estimates), and the year ahead.

Do not fragment the package into more files.

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-FINAL-1 | An upstream skill did not run | Name it; produce the rest and mark the gap |
| R-FINAL-2 | An upstream self-check failed | Name the check; flag in the brief |
| R-FINAL-3 | A carry-forward check fails | Name both figures and the difference |
| R-FINAL-4 | An upstream refusal was not surfaced | Surface it and force a decision in the brief |
| R-FINAL-5 | Intake is incomplete | List the missing items |
| Out of scope | Part-year residence, another state's income, foreign income, partnership or corporation | Refer (`ca-residency-leaving-california`, `us-multi-state-residency-and-allocation`) |

## Worked cases

### Case 1: the carry-forward check catches a missing Schedule CA entry

Federal AGI is $142,000. The federal return took $18,000 of bonus depreciation; California allows $2,400 of depreciation on the same asset, so Schedule CA column C should carry an addition of $15,600. The client's $4,300 federal HSA deduction is not allowed in California: it goes on Schedule CA Section C line 13, column B, which takes it back out of the adjustments and so raises California AGI by $4,300. The draft Form 540 shows line 17 of $142,000. Expected California AGI is $142,000 plus $15,600 plus $4,300 = $161,900, so the check fails by $19,900 (R-FINAL-3).

```oa-check
name: CA assembly check, California AGI carry-forward
inputs:
  federal_agi: 142000
  federal_depreciation: 18000
  ca_depreciation: 2400
  hsa_deduction: 4300
  draft_line_17: 142000
steps:
  - depreciation_addition: federal_depreciation - ca_depreciation
  - expected_line_17: federal_agi + depreciation_addition + hsa_deduction
  - difference: expected_line_17 - draft_line_17
expected:
  depreciation_addition: 15600
  expected_line_17: 161900
  difference: 19900
```

### Case 2: the action list dates for 2027 estimates (decision on the fourth installment)

California 2026 tax is $10,000 and the 2027 required annual payment is set at $10,000 by `ca-estimated-tax-540es`. The action list shows $3,000 by April 15, 2027, $4,000 by June 15, 2027, nothing in September and $3,000 by January 15, 2028. If the client will file the 2027 return and pay in full by January 31, 2028, the fourth installment can be skipped, so the action list carries the choice: pay $3,000 in January, or file and pay the balance by January 31.

```oa-check
name: CA assembly action list, 2027 installments from a 10,000 required payment
inputs:
  required: 10000
steps:
  - april: required * 0.3
  - june: required * 0.4
  - september: required * 0
  - january: required * 0.3
  - total: april + june + september + january
expected:
  april: 3000
  june: 4000
  september: 0
  january: 3000
  total: 10000
```

### Self-checks for the brief

- All upstream skills ran; all their self-checks passed or are flagged.
- Federal and California carry-forward checks pass.
- Federal and California coordination checks pass.
- 1099-NEC and DE 542 reconciliation done.
- Taxpayer action list complete, with dates, amounts and payment methods.
- Planning notes cover the 2027 changes the upstream skills flagged.
- Every refusal catalogue was tested against the facts, and every flag is in the brief.

## Filing and payment

| Item | Date | Source |
| --- | --- | --- |
| Federal and California 2026 returns | April 15, 2027 | `us-federal-return-assembly`; [2025 Form 540 booklet](https://www.ftb.ca.gov/forms/2025/2025-540-booklet.pdf) |
| California automatic extension to file (not to pay) | October 15, 2027 | [FTB extension to file](https://www.ftb.ca.gov/file/when-to-file/extension-to-file.html) |
| 2027 California estimates | 30% April 15, 40% June 15, none September, 30% January 15, 2028 | `ca-estimated-tax-540es`; [2026 Form 540-ES instructions](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.pdf) |
| Form 1099-NEC for 2026 payments | January 31, 2027 | `us-1099-nec-issuance` |

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 2025 Form 540. Read for lines 13 to 17, 31, 32, 62, 91, 92 and 113. | https://www.ftb.ca.gov/forms/2025/2025-540.pdf | 2026-11-13 |
| 2025 California 540 Personal Income Tax Booklet. Read for the due date and line instructions. | https://www.ftb.ca.gov/forms/2025/2025-540-booklet.pdf | 2026-11-13 |
| 2026 Instructions for Form 540-ES. Read for the installment shares and the January 31 early-filing rule. | https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.pdf | 2026-11-13 |
| FTB extension to file. Read for the automatic six-month extension. | https://www.ftb.ca.gov/file/when-to-file/extension-to-file.html | 2026-11-13 |

Not yet confirmed: the 2026 Form 540 and Schedule CA (540) line numbers (2025 forms used); the 2027 Form 540-ES (the 2026 pattern of 30/40/0/30 is assumed to continue for 2027 installments in Case 2).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-ca-return-assembly` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-ca-return-assembly. If neither is available, confirm every figure against the official source pages cited above before relying on it.
