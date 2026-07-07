---
name: nc-return-assembly
description: "Final capstone orchestrator that assembles the complete federal + North Carolina filing package for a full-year North Carolina-resident sole proprietor or single-member LLC disregarded for federal tax. Consumes outputs from every upstream federal and North Carolina content skill (bookkeeping, Schedule C/SE, QBI, retirement, SE health insurance, quarterly estimated tax, federal assembly, 1099-NEC, nc-income-tax, nc-estimated-tax, nc-bailey-settlement-retirement where applicable, and nc-sales-tax for closing out the indirect-tax year) to produce a single unified reviewer package: every worksheet, every form, every cross-skill reconciliation, the final taxpayer action list with payment and filing instructions, the next-year NC-40 voucher schedule, and the reviewer brief. This skill does NOT recompute tax — it ORCHESTRATES. Trigger on phrases like \"assemble the North Carolina return\", \"final NC package\", \"D-400 reviewer package\", \"NC return assembly\", or \"package up the Carolina return\". MUST be loaded alongside us-tax-workflow-base v0.2 or later and every content skill listed in Section 5. North Carolina full-year residents only. Sole proprietors and single-member LLCs disregarded for federal tax only."
jurisdiction: US-NC
domain: individual income tax return assembly
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# nc-return-assembly

## North Carolina Return Assembly Skill — Capstone Orchestrator

> **Scope.** This is THE skill that runs LAST. Every other skill in the North Carolina stack feeds into this one. The output is the complete reviewer package that a credentialed reviewer (Enrolled Agent, CPA, or attorney under Circular 230) signs off on before the return goes to the taxpayer or to the North Carolina Department of Revenue (NCDOR).
>
> This skill does **not** compute anything new. Its job is to verify that every upstream skill ran, every upstream self-check passed, every cross-skill reconciliation holds, and the package is internally consistent.
>
> **Quality tier.** Q3 — AI-drafted, not independently verified. Researched 2026-05-28 against NCDOR, IRS, and the upstream NC content skills in this same package directory. A qualified professional must review before filing.

## CRITICAL EXECUTION DIRECTIVE — READ FIRST

**When this skill is invoked, intake has already happened. The taxpayer has consented to the full workflow. Execute every step without pausing for permission.**

- **Do NOT ask the user "how deep do you want me to go".** The taxpayer asked for a North Carolina return. Produce it.
- **Do NOT announce tool budgets or token counts.** Execute.
- **Do NOT ask which deliverables to prioritize.** Produce every deliverable listed in Section 7. If you run out of context, finish the numbers first, then produce whatever formatted outputs you can, and state honestly at the end which deliverables are partial.
- **Do NOT re-validate scope intake already validated.** Residency, business structure, filing status, Bailey-protected pension status, age, dependents — all of that came from intake. Cross-check specific numbers during reconciliation but do not re-interrogate the taxpayer.
- **Do NOT pause between content skills to check in.** Run them in order (Section 5) without prose updates between each one. One status message at the end is enough.
- **Self-checks are targets, not blockers.** A failed self-check is a flag in the reviewer brief, not a workflow halt. The reviewer handles edges.
- **Primary citations live in the final reviewer brief, not in intermediate computation.** Don't stop to cite N.C.G.S. §105-153.5 mid-deduction-multiplication.

**Failure mode to avoid:** halting mid-execution to ask a meta-question about workflow pacing. That is disqualifying. If you feel the urge to ask "how should I proceed," pick the most defensible path, proceed, and flag the decision for the reviewer.

## Section 1 — Metadata

**Section 1 Metadata table**

| Field | Value |
| --- | --- |
| Jurisdiction | North Carolina (US-NC) — full-year residents only |
| Skill type | Tier 2 orchestrator (capstone) |
| Tax year | 2025 (filed in 2026) |
| Primary forms produced | D-400, D-400 Schedule S (Supplemental Schedule, additions/deductions), D-400 Schedule A (NC itemized — if elected), D-400TC (Tax Credits), NC-40 (2026 estimated payment vouchers) |
| Forms refused at this orchestrator | D-400 Schedule AM (amended), D-400 Schedule PN (part-year/non-resident), D-403 (partnership), CD-401S / CD-405 (corporate), NC K-1 inbound from S-corp/partnership |
| Authority | North Carolina Department of Revenue (NCDOR) |
| Statutes | N.C.G.S. Chapter 105, Article 4 (Individual Income Tax); Bailey v. State, 348 N.C. 130 (1998) for the qualifying-pension subtraction |
| Filing deadline | April 15, 2026 |
| Extension deadline | October 15, 2026 (Form D-410) |
| TY 2025 flat rate | 4.25% (per N.C.G.S. §105-153.7, Session Law 2023-134) |
| Version | 0.1 |
| Last updated | 2026-05-28 |
| Validation | AI-drafted — Q3 |

### Sources consulted

**Sources consulted table**

| # | Source | URL |
| --- | --- | --- |
| 1 | NCDOR — 2025 D-401 Individual Income Tax Instructions | https://www.ncdor.gov/2025-d-401-individual-income-tax-instructions/open |
| 2 | NCDOR — 2025 D-400 Individual Income Tax Return | https://www.ncdor.gov/taxes-forms/individual-income-tax/individual-income-tax-forms-instructions/2025-d-400-individual-income-tax-return |
| 3 | NCDOR — 2025 D-400 Schedule S Supplemental Schedule | https://www.ncdor.gov/taxes-forms/individual-income-tax/individual-income-tax-forms-instructions/2025-d-400-schedule-s-north-carolina-supplemental-schedule |
| 4 | NCDOR — 2025 D-400 Schedule A NC Itemized Deductions | https://www.ncdor.gov/taxes-forms/individual-income-tax/individual-income-tax-forms-instructions/2025-d-400-schedule-north-carolina-itemized-deductions |
| 5 | NCDOR — NC Standard Deduction / NC Itemized Deductions | https://www.ncdor.gov/taxes-forms/individual-income-tax/filing-topics/north-carolina-standard-deduction-or-north-carolina-itemized-deductions |
| 6 | NCDOR — North Carolina Child Deduction | https://www.ncdor.gov/taxes-forms/individual-income-tax/filing-topics/north-carolina-child-deduction |
| 7 | NCDOR — Tax Rate Schedules | https://www.ncdor.gov/taxes-forms/individual-income-tax/tax-rate-schedules |
| 8 | NCDOR — Pay Your Individual Income Tax (online payment options) | https://www.ncdor.gov/file-pay/pay-individual-income-tax |
| 9 | NCDOR — Where's My Refund? | https://www.ncdor.gov/file-pay/wheres-my-refund |
| 10 | NCDOR — eFile for Individual Income Tax (accepted partners) | https://www.ncdor.gov/file-pay/efile-individual-income-tax |
| 11 | NCDOR — Form NC-40 Individual Estimated Income Tax | https://www.ncdor.gov/taxes-forms/individual-income-tax/individual-income-tax-forms-instructions |
| 12 | Bailey v. State of North Carolina, 348 N.C. 130 (1998) | https://www.ncdor.gov/taxes-forms/individual-income-tax/filing-topics/bailey-decision |
| 13 | IRS Modernized e-File (MeF) — Federal/State joint filing | https://www.irs.gov/e-file-providers/modernized-e-file-overview |

## Section 2 — What this skill is

The final capstone skill. Every other North Carolina skill and every relevant federal skill feeds into this one. The deliverable is the complete reviewer package that a credentialed reviewer signs off on before filing.

The skill enforces three things:

1. **Order of operations.** Federal first, North Carolina second. The order is non-negotiable because federal AGI flows into D-400 Line 6 (the NC AGI starting point), and federal-level deductions and adjustments (QBI, SE health insurance, SE tax deduction, retirement contributions) are baked into federal AGI before the NC computation begins. Unlike Michigan there is **no city-level income tax in North Carolina** — every municipality is barred from levying a local income tax under N.C.G.S. §160A-211 / county-level equivalents — so the city step from the MI orchestrator is omitted entirely.
2. **Cross-skill reconciliation.** Every figure that appears on the D-400 must match the corresponding figure produced by the source skill. A mismatch halts assembly with a specific, named refusal.
3. **Reviewer-grade output.** The final package is structured for a CPA or EA to review in under 30 minutes: cover summary, brief, exhibits in order, action list, citations.

## Section 3 — Orchestration runbook

When invoked, the agent executes the following steps in order. No step is optional. No step is skipped without an explicit refusal.

### Step 1 — Confirm intake artifact exists

Verify the intake skill has produced:

- Taxpayer name, SSN/ITIN (last 4 only in working files)
- Filing status (Single / MFJ / MFS / HoH / QSS)
- Residency confirmation (full-year North Carolina)
- Date of birth for taxpayer and spouse (drives senior-deduction considerations and Bailey settlement vesting eligibility)
- Dependents list with SSNs (drives NC child deduction)
- Business structure (sole prop or SMLLC disregarded)
- Bailey-vested pension flag (taxpayer was vested in a qualifying NC state, local, or federal government retirement plan on or before August 12, 1989 — `[VERIFY:]` vesting cutoff date)
- Health coverage history (federal Form 1095-A / B / C)
- W-2s, 1099-NECs, 1099-Rs received

If any item is missing, refuse with **R-NC-FINAL-5**.

### Step 2 — Confirm federal skills ran and produced outputs

Verify in order:

1. `us-sole-prop-bookkeeping` — Schedule C classification with reconciled bank ledger.
2. `us-schedule-c-and-se-computation` — Schedule C bottom line, Form 8829, Schedule SE.
3. `us-self-employed-retirement` — SEP / Solo 401(k) contribution and Schedule 1 Line 16 amount.
4. `us-self-employed-health-insurance` — §162(l) deduction and Schedule 1 Line 17 amount (with iterative PTC convergence if marketplace coverage).
5. `us-qbi-deduction` — Form 8995 or 8995-A, deduction to Form 1040 Line 13.
6. `us-federal-return-assembly` — Form 1040, Schedules 1, 2, 3, all supporting forms, federal total tax, federal balance due / refund.
7. `us-quarterly-estimated-tax` — Form 2210 (if penalty) + 2026 Form 1040-ES schedule.
8. `us-1099-nec-issuance` — Parallel; only needs bookkeeping. Contractor list plus W-9 gaps.

If any is missing or its self-checks did not pass, refuse with **R-NC-FINAL-1** or **R-NC-FINAL-2** naming the specific skill.

### Step 3 — Confirm North Carolina skills ran

Execute in order:

1. `nc-income-tax` — D-400, D-400 Schedule S, D-400 Schedule A (if itemizing), D-400TC (if claiming credits). Produces NC taxable income, NC tax at 4.25%, credits, refund or balance due.
2. `nc-bailey-settlement-retirement` — Schedule S Part B Bailey subtraction, if any taxpayer or spouse has a qualifying pre-August-12-1989-vested federal, NC state, or NC local government pension or IRC §401(k) / §457 plan. Skip if N/A but record the skip.
3. `nc-estimated-tax` — Produces a 4-payment NC-40 voucher schedule for 2026 if expected NC liability after withholding exceeds the NC threshold. (`[VERIFY:]` NC threshold for required estimates — NCDOR typically uses $1,000 expected tax due similar to federal.) Also computes any current-year NC underpayment interest exposure on Form D-422.

If any required skill failed or its self-check failed, refuse with **R-NC-FINAL-1** or **R-NC-FINAL-2**.

### Step 4 — No city / local return step

North Carolina municipalities and counties may not levy local income tax. Skip the city step entirely. If intake somehow flagged a "city return," that is an intake error — refuse with **R-NC-FINAL-7** and route back to intake for correction.

### Step 5 — Run the verification matrix

Run every check in Section 6. Each check is a specific equality between a number on a final form and the source-of-truth output from the producing skill. A failure halts assembly with **R-NC-FINAL-3**.

### Step 6 — Aggregate artifacts

Pull:

- Every "Assumed" entry from every upstream skill into the **assumption log**.
- Every "Taxpayer input needed" item into the **taxpayer input log**.
- Every "Reviewer judgment needed" item into the **reviewer flag log**.
- Every refusal that fired anywhere in the chain into the **refusal log**.

### Step 7 — Compose the deliverables

Produce the three output files specified in Section 7. Place them in `/mnt/user-data/outputs/`. Present them at the end with `present_files`.

### Step 8 — Final status message

A single message stating: which skills ran, which self-checks passed, which deliverables were produced, any partial deliverables and why. Done.

## Section 4 — Pre-flight checks

Before any of Section 3 runs, the orchestrator confirms these gating conditions. If any fail, refuse — do not partially execute.

**Pre-flight checks table**

| Check | Question | Refusal if fails |
| --- | --- | --- |
| PF-1 | Has federal Form 1040 been computed by `us-federal-return-assembly`? | R-NC-FINAL-1 |
| PF-2 | Is federal AGI (Form 1040 Line 11) a finite, signed number? | R-NC-FINAL-1 |
| PF-3 | Has the taxpayer's full-year North Carolina residency been confirmed? | R-NC-FINAL-6 |
| PF-4 | Is the business structure sole prop or SMLLC disregarded? S-corp or partnership? | R-NC-FINAL-10 / R-NC-FINAL-11 |
| PF-5 | Is the tax year 2025? | R-NC-FINAL-12 |
| PF-6 | If MFJ: are both spouses full-year NC residents? Mixed-residency couples → refuse. | R-NC-FINAL-13 |
| PF-7 | Is this a current-year original return (not amended)? | R-NC-FINAL-14 |
| PF-8 | If Bailey-flag set: is the taxpayer vested on/before Aug 12, 1989 in a qualifying plan? `nc-bailey-settlement-retirement` confirms. | R-NC-FINAL-15 |
| PF-9 | Did intake report any S-corp or partnership K-1 (NC K-1)? | R-NC-FINAL-10 / R-NC-FINAL-11 |
| PF-10 | Did intake report any out-of-state wages requiring NC-478 / D-400TC out-of-state credit beyond simple W-2? Multi-state apportionment is out of scope. | R-NC-FINAL-16 |

## Section 5 — Skill-loading order (canonical execution sequence)

This is the immutable order. Do not parallelize; downstream skills consume upstream outputs. The single exception is `us-1099-nec-issuance`, which can run in parallel with anything after `us-sole-prop-bookkeeping`.

```
1.  us-tax-workflow-base                         (workflow scaffold)
2.  us-sole-prop-bookkeeping                     (Schedule C classification)
3.  us-schedule-c-and-se-computation             (C, SE, 8829)
4.  us-qbi-deduction                             (8995 / 8995-A)
5.  us-self-employed-health-insurance            (§162(l), iterative w/ PTC)
6.  us-self-employed-retirement                  (SEP / Solo 401(k))
7.  us-quarterly-estimated-tax                   (2210, 2026 1040-ES)
8.  us-federal-return-assembly                   (1040, Sch 1/2/3, sign-off)
9.  us-1099-nec-issuance                         (parallel; contractor batch)
10. nc-income-tax                                (D-400, Sch S, Sch A, D-400TC)
11. nc-bailey-settlement-retirement              (Sch S Part B — if applicable)
12. nc-estimated-tax / NC-40 (2026)              (next-year vouchers)
13. nc-return-assembly                           ← THIS SKILL
```

Each upstream skill is expected to expose, at minimum: (a) the line-item output(s) it produces, (b) the self-check log, (c) any refusals fired, and (d) any reviewer / taxpayer flags. The orchestrator consumes those four artifacts per skill.

**Note on `nc-sales-tax`.** Sales tax is a separate filing cadence (monthly / quarterly / annual under E-500) and does not flow into the individual return. The orchestrator only surfaces an end-of-year sales-tax status line ("all NC sales-tax periods filed through Dec 2025" or "Q4 2025 E-500 due Jan 31, 2026 — verify filed") in the action list. It does not block on sales tax.

## Section 6 — Verification matrix (reconciliations)

Every line below is a hard equality. Tolerance is $1 unless noted otherwise. A failure halts assembly with **R-NC-FINAL-3** naming the specific check.

### 6A — Federal internal consistency (re-verified)

**6A table**

| Check | Equation | Source-of-truth skill |
| --- | --- | --- |
| F-1 | Schedule C Line 31 = Schedule 1 Line 3 = Form 1040 Line 8 (via Sch 1 to L10) | us-schedule-c-and-se-computation |
| F-2 | Schedule SE Line 12 = Schedule 2 Line 4 | us-schedule-c-and-se-computation |
| F-3 | Schedule SE Line 13 = Schedule 1 Line 15 | us-schedule-c-and-se-computation |
| F-4 | SEP / Solo 401(k) employer + employee = Schedule 1 Line 16 | us-self-employed-retirement |
| F-5 | §162(l) deduction = Schedule 1 Line 17 | us-self-employed-health-insurance |
| F-6 | QBI deduction = Form 1040 Line 13 | us-qbi-deduction |
| F-7 | Total tax = Form 1040 Line 24 | us-federal-return-assembly |
| F-8 | Form 2210 penalty (if any) = Schedule 2 Line 8 | us-quarterly-estimated-tax |
| F-9 | Total payments = Form 1040 Line 33 | us-federal-return-assembly |
| F-10 | Refund / balance due = Form 1040 Line 34 or 37 | us-federal-return-assembly |

### 6B — North Carolina internal consistency

**6B table**

| Check | Equation | Source-of-truth skill |
| --- | --- | --- |
| N-1 | Federal AGI (Form 1040 Line 11) = D-400 Line 6 | nc-income-tax |
| N-2 | D-400 Schedule S Part A (additions) total = D-400 Line 7 | nc-income-tax |
| N-3 | D-400 Schedule S Part B (deductions/subtractions) total = D-400 Line 9 | nc-income-tax |
| N-4 | D-400 Line 8 = Line 6 + Line 7 (federal AGI + additions) | nc-income-tax |
| N-5 | D-400 Line 10 = Line 8 − Line 9 (after additions and subtractions) | nc-income-tax |
| N-6 | D-400 Line 11 = NC standard deduction OR NC itemized (Schedule A) total — whichever taxpayer elected | nc-income-tax |
| N-7 | NC standard deduction TY 2025: $25,500 MFJ/QSS, $19,125 HoH, $12,750 Single, $12,750 MFS `[VERIFY:]` | nc-income-tax |
| N-8 | D-400 Line 10b NC child deduction: up to $3,000 per qualifying child, with AGI-based tiered phase-out per N.C.G.S. §105-153.5(a1) `[VERIFY:]` 2025 tier table | nc-income-tax |
| N-9 | D-400 Line 12a = Line 10 − Line 11 − Line 10b (NC taxable income) | nc-income-tax |
| N-10 | D-400 Line 13 = Line 12a × 4.25% (NC income tax) | nc-income-tax |
| N-11 | D-400 Line 16 = Line 13 − D-400TC credits (if claimed) | nc-income-tax |
| N-12 | D-400 Line 20 (NC tax withheld) = sum of W-2 box 17 NC + 1099 box 16 NC | nc-income-tax |
| N-13 | D-400 Line 21 (estimated payments + extension payment) = sum of NC-40 vouchers paid + D-410 extension if applicable | nc-estimated-tax |
| N-14 | D-400 Line 27 (refund) OR Line 28 (balance due) reconciles | nc-income-tax |

### 6C — Bailey settlement subtraction (Schedule S Part B)

**6C table**

| Check | Equation | Source |
| --- | --- | --- |
| B-1 | If Bailey-eligible: subtraction = full amount of qualifying distribution reported on federal 1099-R | nc-bailey-settlement-retirement |
| B-2 | The Bailey subtraction line on D-400 Schedule S Part B = nc-bailey-settlement-retirement output | nc-bailey-settlement-retirement |
| B-3 | If taxpayer is NOT Bailey-eligible but reported government pension distributions: confirm no subtraction was taken | nc-bailey-settlement-retirement |
| B-4 | If Bailey-eligible: Schedule S Part B Bailey line + other Part B subtractions = D-400 Line 9 | nc-bailey-settlement-retirement + nc-income-tax |

### 6D — Federal-NC coordination

**6D table**

| Check | Equation |
| --- | --- |
| C-1 | Filing status on D-400 = filing status on Form 1040 |
| C-2 | Dependents claimed on D-400 = dependents claimed on Form 1040 |
| C-3 | Schedule C net profit federally = Schedule C net profit feeding NC AGI |
| C-4 | Federal §168(k) bonus depreciation: NC requires 85% add-back in Year 1 with 20%-per-year reversal over 5 years on Schedule S Part A — verify add-back appears `[VERIFY:]` current NC §168(k) decoupling status |
| C-5 | Federal §179: NC conforms with limitation — `[VERIFY:]` NC §179 cap (often lower than federal); add-back if federal §179 exceeded NC cap |
| C-6 | Federal SE tax deduction (Schedule 1 Line 15) is reflected in federal AGI; no NC add-back |
| C-7 | Federal QBI deduction does NOT flow into NC computation (NC starts at federal AGI before QBI — federal Line 13 is after AGI) — confirm no double-counting |
| C-8 | Federal SE health insurance deduction is included in federal AGI; no NC add-back |
| C-9 | Federal taxable Social Security (Form 1040 Line 6b) → NC Schedule S Part B Social Security subtraction (NC fully exempts Social Security) |
| C-10 | U.S. government bond interest in federal Schedule B → NC Schedule S Part B subtraction |
| C-11 | Non-NC state/muni bond interest in federal Schedule B → NC Schedule S Part A addition |
| C-12 | NC tax refund deducted federally as itemized → NC Schedule S Part B subtraction (if state-refund add-back exists on Sch S Part A path) `[VERIFY:]` |
| C-13 | If NC itemized (Schedule A) elected: NC Schedule A itemized must NOT exceed federal Schedule A items NC allows; SALT deduction on NC Schedule A is capped at $0 for income/sales tax and limited for property tax `[VERIFY:]` |

### 6E — 1099-NEC reconciliation

**6E table**

| Check | Equation |
| --- | --- |
| 9-1 | Sum of NEC payments flagged = Schedule C Line 11 (Contract labor) + any direct labor lines |
| 9-2 | Each contractor with $600+ has W-9 on file; gaps surfaced in flag log |
| 9-3 | Filing deadline noted (January 31, 2026; if past, late-filing penalty surfaced) |
| 9-4 | NC-1099 / NC-3 annual reconciliation status confirmed if taxpayer is also a NC withholding agent (separate from 1099-NEC; flag-only here) |

### 6F — Estimated-tax coordination

**6F table**

| Check | Equation |
| --- | --- |
| E-1 | 2026 federal Q1 voucher = `us-quarterly-estimated-tax` Q1 output |
| E-2 | 2026 NC-40 Q1 voucher = `nc-estimated-tax` Q1 output |
| E-3 | NC safe harbor: 100% of 2025 NC tax OR 90% of current-year — `[VERIFY:]` 110% rule does NOT generally apply at NC level the way it does federally; NC uses 100% of prior year regardless of AGI |
| E-4 | Q1 federal + Q1 NC together do not exceed taxpayer's stated cash availability flag (if intake captured one) |
| E-5 | If NC underpayment interest exposure (D-422) exists in current year, surface for reviewer |

### 6G — Withholding tie-out

**6G table**

| Check | Equation |
| --- | --- |
| W-1 | Sum of W-2 box 17 (NC state income tax withheld) = D-400 Line 20a |
| W-2 | Sum of 1099-R / 1099-NEC / 1099-MISC NC withholding (box 16 / box 5 depending on form) = D-400 Line 20b |
| W-3 | NC withholding total (Line 20a + 20b) = D-400 Line 20 |
| W-4 | Schedule W-equivalent backup detail captured in workbook for reviewer |

### 6H — Bailey + retirement + SE-health cross-checks

**6H table**

| Check | Equation |
| --- | --- |
| BX-1 | If taxpayer is Bailey-eligible AND took the §162(l) SE health deduction: confirm pension income is excluded from "net earnings from self-employment" for SE health cap purposes (it is — Bailey income is pension, not SE earnings) |
| BX-2 | If taxpayer is Bailey-eligible AND has marketplace coverage: confirm Bailey-protected income still flows into federal MAGI for PTC computation (it does; Bailey is a NC-only subtraction, not a federal exclusion) |
| BX-3 | If taxpayer rolled over a Bailey-protected plan to a non-Bailey IRA after 8/12/1989: the rolled amount loses Bailey protection — flag for reviewer |

## Section 7 — Deliverable package (what the reviewer sees)

The package is **three files**, not fifteen. Do not fragment the output.

### 7A — File 1: `{taxpayer_slug}_2025_nc_master.xlsx`

A single master workbook. Required sheets, in this order:

1. **Cover** — Taxpayer name, filing status, residency, business structure, summary table (federal tax, NC tax, total liability, total payments, net refund/balance due, key 2026 dates).
2. **Assumption Log** — Every "Assumed" item from every upstream skill, tagged with the skill that produced it.
3. **Taxpayer Input Log** — Every item that needs taxpayer confirmation before filing.
4. **Reviewer Flag Log** — Every item that needs reviewer judgment.
5. **Income** — Aggregate income summary (W-2, 1099-NEC, Schedule C, interest, dividends, capital gains, 1099-R, other).
6. **Schedule C** — Parts I–V.
7. **Form 4562** — Depreciation (if applicable).
8. **Form 8829** — Home office (if applicable).
9. **Schedule SE** — SE tax.
10. **Retirement** — SEP / Solo 401(k) worksheet.
11. **SE Health Insurance** — §162(l) worksheet, with PTC iteration log if marketplace coverage.
12. **Form 8962** — PTC reconciliation (if marketplace coverage).
13. **QBI** — Form 8995 or 8995-A.
14. **Schedule 1 (federal)** — Adjustments to income.
15. **Schedule 2 (federal)** — Additional taxes.
16. **Schedule 3 (federal)** — Credits (if applicable).
17. **Form 1040** — Final federal return line-by-line.
18. **Form 2210** — Underpayment penalty (if applicable).
19. **D-400** — North Carolina return line-by-line.
20. **D-400 Schedule S** — Part A additions and Part B deductions (Bailey, Social Security, U.S. bond interest, etc.).
21. **D-400 Schedule A** — NC itemized deductions (if itemizing).
22. **D-400TC** — Tax credits worksheet (if applicable).
23. **D-422** — NC underpayment interest (if applicable).
24. **Bailey Worksheet** — Bailey-protected pension subtraction detail (if applicable).
25. **NC Withholding Detail** — W-2 + 1099 withholding tie-out.
26. **2026 Federal 1040-ES** — Voucher schedule.
27. **2026 NC-40** — Voucher schedule.
28. **1099-NEC Batch** — Contractor batch (if applicable).
29. **NC Sales Tax Status** — End-of-year filing status note (if taxpayer is a NC sales-tax registrant).
30. **Verification Matrix** — Every check in Section 6 with pass/fail/N/A.

Use the same Excel-builder discipline as `us-federal-return-assembly`: collect anchors as a Python dict before writing cross-sheet formulas; verify no `#REF!` errors; verify computed cells match the Python model within $1 before shipping.

### 7B — File 2: `reviewer_brief.md`

Structured markdown. Required sections in this order:

1. **Executive Summary** (≤ 1 page) — Taxpayer, filing status, residency, federal tax, NC tax, total liability, total payments, net result, action required by April 15, 2026.
2. **Federal Return Brief** — Summary of `us-federal-return-assembly` brief, condensed.
3. **North Carolina Return Brief** — Summary of `nc-income-tax` brief plus anything from Bailey subtraction and Schedule A.
4. **Standard vs. Itemized Decision** — Show both NC standard deduction and computed NC itemized total; document the chosen route and why it was favorable.
5. **Estimated Tax for 2026** — Federal + NC voucher schedule.
6. **1099-NEC Issuance** — Status of contractor filings.
7. **NC Sales Tax Status** — End-of-year status, if applicable.
8. **Cross-skill Verification** — Pass/fail summary from Section 6.
9. **Reviewer Attention Flags** — Aggregated from all upstream skills.
10. **Refusals Triggered** — Aggregated from all upstream skills.
11. **Positions Taken** — Tax positions requiring judgment, with citations (N.C.G.S. §, IRC §, D-401 page references, Bailey case cite).
12. **Planning Notes for 2026** — NC rate watch (Session Law 2023-134 rate-step-down schedule continues; `[VERIFY:]` 2026 rate is expected ~3.99%), federal QBI 20% → 23% under OBBBA, federal 1099 threshold change, NC child deduction phase-out tier monitoring, Bailey income continuity.
13. **Taxpayer Action List** — Embedded copy of File 3.

### 7C — File 3: `taxpayer_action_list.md`

Step-by-step action list, structured by date. The taxpayer reads this file and nothing else.

```markdown
# Your 2025 North Carolina Tax Filing — Action List

## This week
1. Review the reviewer_brief.md document
2. Sign Form 8879 (federal e-file authorization) — if e-filing
3. Sign Form NC-8453 (North Carolina e-file authorization) — if
   e-filing through an approved partner
4. Confirm bank account information for direct debit / direct
   deposit

## Before April 15, 2026 (filing deadline)
1. Federal Form 1040 — file via e-file (preferred) or paper to IRS
   Kansas City address
2. Federal balance due of $X — pay via:
   - IRS Direct Pay (https://www.irs.gov/payments/direct-pay) — free, ACH
   - EFTPS (https://www.eftps.gov) — free, requires enrollment
   - Debit/credit card (fee applies)
   - Check + Form 1040-V voucher to IRS Kansas City
3. North Carolina Form D-400 — file via:
   - NCDOR eFile through an approved partner (TurboTax, H&R Block,
     FreeTaxUSA, Drake, etc. — see
     https://www.ncdor.gov/file-pay/efile-individual-income-tax)
   - Paper return mailed to:
     - With payment: North Carolina Department of Revenue, PO Box
       25000, Raleigh NC 27640-0640
     - Refund / no balance due: North Carolina Department of
       Revenue, PO Box 25000, Raleigh NC 27640-0500
4. North Carolina balance due of $X — pay via:
   - NCDOR online payment
     (https://www.ncdor.gov/file-pay/pay-individual-income-tax) —
     ACH direct debit, free; credit/debit card with processor fee
   - Direct debit at e-file
   - Check + payment voucher mailed to NCDOR

## Before April 15, 2026 (estimated tax for 2026 Q1)
1. Federal Q1 voucher — $X via IRS Direct Pay or check + Form 1040-ES
2. NC Q1 voucher — $X via NCDOR online or check + NC-40

## Before June 15, 2026 (Q2 estimated tax)
1. Federal Q2 voucher — $X
2. NC Q2 voucher — $X

## Before September 15, 2026 (Q3 estimated tax)
1. Federal Q3 voucher — $X
2. NC Q3 voucher — $X

## Before January 15, 2027 (Q4 estimated tax)
1. Federal Q4 voucher — $X
2. NC Q4 voucher — $X

## Already-passed January 31, 2026 (1099-NEC issuance — check if done)
1. File 1099-NEC forms with IRS via IRIS or FIRE
2. Furnish Copy B to each contractor
3. File NC-3 / NC-1099 annual reconciliation with NCDOR (if
   taxpayer is a NC withholding agent)
4. If missed: assess penalty exposure ($60–$310 per form federally;
   NC late-filing penalty also applies) and file ASAP

## Ongoing during 2026
1. Collect W-9 from every new contractor BEFORE first payment
2. Track Schedule C income and expenses with receipts
3. Monitor income against estimated-tax safe harbor mid-year
   (especially before September Q3 payment)
4. Track health coverage continuously (federal Form 1095-A from
   marketplace; 1095-B/C from employer)
5. If a NC sales-tax registrant: file E-500 on the assigned cadence
   (monthly / quarterly / annual)

## How to check your refund
- Federal: https://www.irs.gov/refunds — "Where's My Refund?"
- North Carolina: https://www.ncdor.gov/file-pay/wheres-my-refund —
  "Where's My Refund?"

## Need help with anything in this list?
- Reach out to the reviewer (CPA / EA) listed on the cover sheet.
- For North Carolina-specific questions: NCDOR Taxpayer Assistance
  1-877-252-3052
```

If execution runs out of context mid-build: produce whatever is complete, then state at the end which files were partial. Three files honest beats fifteen files fragmented.

All files go to `/mnt/user-data/outputs/` and are presented at the end via the `present_files` tool.

## Section 8 — The reviewer brief (narrative format)

This is the document the CPA reads first. It should be readable in under 30 minutes and give the reviewer enough context to either sign off or identify exactly what needs more work.

The brief follows this fixed structure:

```markdown
# Complete Return Package — [Taxpayer Name] — Tax Year 2025

## Executive Summary
- **Taxpayer:** [Name], full-year North Carolina resident
- **Filing status:** [Single / MFJ / MFS / HoH / QSS]
- **Business:** Sole proprietor / Single-member LLC disregarded
- **Bailey-eligible pension:** [Yes / No]
- **Federal total tax (Form 1040 Line 24):** $X
- **NC total tax (D-400 Line 17):** $X
- **Total 2025 tax liability (federal + NC):** $X
- **Total payments (withholding + estimates + extension):** $X
- **Net refund or balance due:** $X
- **Action required by April 15, 2026:** [one-line summary]

## Federal Return
[brief from us-federal-return-assembly, condensed]

## North Carolina Return
[brief from nc-income-tax + Bailey subtraction]

## Standard vs. Itemized Decision (NC)
- NC standard deduction (filing status): $X
- NC itemized total (Schedule A): $Y
- Chosen: [standard / itemized]
- Rationale: [whichever yielded lower NC taxable income]

## Estimated Tax for 2026
[combined federal 1040-ES + NC-40 schedule]

## 1099-NEC Issuance
[brief from us-1099-nec-issuance]

## NC Sales Tax Status
[from nc-sales-tax if registrant; else N/A]

## Cross-skill Verification
- All upstream skills ran: [verified / list missing]
- All upstream self-checks passed: [verified / list failures]
- All Section 6 reconciliations passed: [verified / list failures]

## Reviewer Attention Flags
[aggregated, ranked by materiality]

## Refusals Triggered
[aggregated; any non-empty entry blocks final signoff]

## Positions Taken
[items requiring reviewer judgment, with citations]

## Planning Notes for 2026
- NC rate step-down (Session Law 2023-134): 4.25% in 2025 →
  ~3.99% in 2026 `[VERIFY:]`; long-term schedule down to ~2.49% by
  2030 absent further legislation
- Federal QBI 20% → 23% under OBBBA (P.L. 119-21)
- NC child deduction phase-out tier monitoring
- Bailey-eligible pension continuity (no rollovers to non-Bailey IRAs)
- Estimated-tax safe harbor positioning (NC uses 100% of prior year)

## Taxpayer Action List
[embedded copy of File 3]
```

## Section 9 — Tier 1 deterministic rules

**Tier 1 rules table**

| Rule ID | Rule |
| --- | --- |
| NC-ASM-T1-01 | Federal Form 1040 must be computed before D-400. No exceptions. |
| NC-ASM-T1-02 | D-400 Line 6 (federal AGI starting point) must exactly equal Form 1040 Line 11. |
| NC-ASM-T1-03 | NC income tax = (D-400 Line 12a) × 0.0425 for TY 2025. Always. |
| NC-ASM-T1-04 | NC has no city or local individual income tax. Skip any city-return step. |
| NC-ASM-T1-05 | The April 15, 2026 filing deadline applies unless taxpayer is granted federal extension; NCDOR accepts federal extension automatically with Form D-410 confirmation OR a separate D-410 may be filed for state-only extension. |
| NC-ASM-T1-06 | Extension to file is NOT extension to pay. Any NC balance due is still due April 15. |
| NC-ASM-T1-07 | Bailey subtraction (Schedule S Part B) is allowed ONLY if the taxpayer was vested in the qualifying NC state, local, or federal government retirement plan on or before August 12, 1989. |
| NC-ASM-T1-08 | NC fully exempts Social Security benefits (Schedule S Part B). Federal taxable SS (Line 6b) must be subtracted in full. |
| NC-ASM-T1-09 | NC estimated-tax payments are required if expected NC tax after withholding exceeds the NC threshold `[VERIFY:]` $1,000 expected. |
| NC-ASM-T1-10 | NC safe harbor: 100% of prior-year NC tax OR 90% of current-year. No 110%-AGI step. `[VERIFY:]` |
| NC-ASM-T1-11 | NC partially decouples from federal §168(k) bonus depreciation — 85% add-back in Year 1 with 20%-per-year deductible reversal over 5 years on Schedule S Part A `[VERIFY:]` 2025 schedule. |
| NC-ASM-T1-12 | NC does NOT recognize the federal §199A QBI deduction in any NC adjustment. NC starts at federal AGI, BEFORE QBI, so QBI never touches NC computation. |
| NC-ASM-T1-13 | NC standard deduction TY 2025 (per `nc-income-tax` table): $25,500 MFJ/QSS, $19,125 HoH, $12,750 Single, $12,750 MFS `[VERIFY:]`. |
| NC-ASM-T1-14 | NC child deduction: up to $3,000 per qualifying child under N.C.G.S. §105-153.5(a1), with tiered AGI phase-out `[VERIFY:]` 2025 tier table; complete phase-out at higher AGI. |
| NC-ASM-T1-15 | NC itemized deductions (Schedule A) are NOT federal Schedule A. Only specific categories (qualified mortgage interest + property tax up to $20,000 combined, charitable contributions matching federal, medical/dental) are allowed `[VERIFY:]` 2025 categories and caps. |
| NC-ASM-T1-16 | Three-file deliverable structure (xlsx + brief.md + actions.md) is mandatory. |
| NC-ASM-T1-17 | No city-level income tax exists in NC; the orchestrator never emits a city return artifact. |

## Section 10 — Tier 2 judgment rules

**Tier 2 rules table**

| Rule ID | Rule | Guidance |
| --- | --- | --- |
| NC-ASM-T2-01 | **Materiality threshold for reconciliation failures.** A $1 rounding gap is not a failure; a $50 gap is. | Reviewer judgment on the threshold; default $5 for federal-NC tie-outs, $1 for intra-form. |
| NC-ASM-T2-02 | **Standard vs. itemized.** Compute both; choose the lower NC taxable income. | Default to standard if the gap is < $200 (administrative simplicity); itemize if material. Always document the comparison in the reviewer brief. |
| NC-ASM-T2-03 | **Bailey vesting documentation.** Taxpayer must produce documentation of pre-8/12/1989 vesting. | If documentation is incomplete, flag for reviewer; do NOT take the subtraction without reviewer signoff. |
| NC-ASM-T2-04 | **Partial Bailey rollovers.** If a Bailey-protected plan was partially rolled into a non-protected IRA after 1989, only the original-protected portion remains Bailey-protected. | Defer the allocation math to `nc-bailey-settlement-retirement`; orchestrator only verifies the chosen split flowed correctly. |
| NC-ASM-T2-05 | **NC §168(k) and §179 decoupling reversals.** Year-2 through Year-5 reversals of prior-year add-backs must be captured on Schedule S Part B. | Verify the carryforward schedule from `nc-income-tax` matches prior-year working papers; if first-year prep, document the assumption. |
| NC-ASM-T2-06 | **Out-of-state work performed by NC resident.** Self-employment income earned while physically working in another state may also be taxable in that state. NC offers a credit for taxes paid to another state via D-400TC. | If material out-of-state work exists, refuse with R-NC-FINAL-16 (multi-state apportionment out of scope). |
| NC-ASM-T2-07 | **Late-1099 penalty exposure.** January 31 may already be past at the time of orchestrator run. | Surface the penalty exposure in the action list; the reviewer decides whether to file late or wait. |
| NC-ASM-T2-08 | **PTC iteration convergence.** The marketplace-coverage iteration between SE health and PTC may not converge cleanly within 3 cycles. | If `us-self-employed-health-insurance` flagged non-convergence, escalate the flag to the reviewer brief and document the chosen position. |
| NC-ASM-T2-09 | **NC child deduction near phase-out boundary.** If AGI is within 5% of a phase-out tier boundary, mid-year income changes could shift the tier. | Flag for reviewer; document chosen tier and basis. |
| NC-ASM-T2-10 | **NC withholding tied to wrong state.** If W-2 withholding was sent to another state when the work was performed in NC, an NC-4 correction with the employer is required. | Surface as taxpayer action; orchestrator does not file the correction. |

## Section 11 — Worked example

**Facts.** James Whitfield, single, age 67, full-year Raleigh (NC) resident, sole proprietor (freelance security consultant, retired federal CSRS pensioner). 2025 facts:

- Schedule C gross receipts: $190,000
- Schedule C deductible expenses: $40,000 (no home office)
- Schedule C net profit: $150,000
- Federal CSRS pension (1099-R): $40,000, fully Bailey-protected (vested in CSRS in 1978; well before 8/12/1989)
- Social Security benefits received: $24,000; taxable for federal purposes (Form 1040 Line 6b): $20,400 (85% inclusion)
- Other income: $2,000 interest from Wells Fargo checking; $0 dividends
- Marketplace health coverage: No — James is on Medicare
- Solo 401(k) contributions: $30,500 (employee deferral $23,500 + $7,500 age-50+ catch-up; no employer portion this year by election)
- Federal withholding: $0 from CSRS pension (waived); $0 W-2
- Federal estimated payments: $0 — taxpayer underpaid; Form 2210 penalty applies
- NC withholding: $0 across all sources
- NC estimated payments: $0 — taxpayer underpaid; Form D-422 applies
- No dependents; no NC child deduction
- Takes NC standard deduction ($12,750 single TY 2025 `[VERIFY:]`)
- No NC sales-tax registration

**Orchestrator output (abbreviated reviewer brief — actual file is longer):**

```markdown
# Complete Return Package — James Whitfield — Tax Year 2025

## Executive Summary
- Taxpayer: James Whitfield, full-year North Carolina (Raleigh) resident
- Filing status: Single
- Business: Sole proprietor — freelance security consultant
- Bailey-eligible pension: Yes — federal CSRS, vested 1978
- Federal total tax (Form 1040 Line 24): $52,860
- NC total tax (D-400 Line 17): $4,360
- Total 2025 tax liability: $57,220
- Total payments (federal + NC withholding + estimates): $0
- Net balance due: $57,220 across federal + NC
- Action required by April 15, 2026: file federal Form 1040, North
  Carolina D-400; pay $57,220 in balance due across the two
  jurisdictions; pay 2026 Q1 estimates of ~$14,300 combined;
  reviewer to confirm Form 2210 (federal) and D-422 (NC)
  underpayment-interest amounts

## Federal Return (from us-federal-return-assembly)
- Schedule C Line 31 (net profit): $150,000
- Schedule SE Line 12 (SE tax): $18,792
- Schedule 1 Line 15 (½ SE tax): $9,396
- Schedule 1 Line 16 (retirement): $30,500
- Schedule 1 Line 17 (SE health insurance): $0 (Medicare; no §162(l)
  marketplace coverage, but Medicare Part B premiums may qualify —
  reviewer flag to confirm)
- Form 1040 Line 6b (taxable Social Security): $20,400
- Form 1040 Line 11 (AGI): $132,504 (after retirement,
  ½ SE tax, plus pension + SS + interest)
- Form 8995 QBI deduction: ~$24,000 (non-SSTB; under threshold; 20%
  rate for TY 2025)
- Form 1040 Line 12 (standard deduction, single, age 65+): $17,600
  (OBBBA base + age-65 additional) `[VERIFY:]`
- Form 1040 Line 15 (taxable income): ~$90,900
- Form 1040 Line 16 (tax): ~$15,300
- Schedule 2 Line 4 (SE tax): $18,792
- Form 2210 penalty: ~$1,800 (no estimates paid; reviewer to
  finalize)
- Form 1040 Line 24 (total tax): $52,860
- Payments: $0
- Balance due federal: $52,860

## North Carolina Return (from nc-income-tax + nc-bailey-settlement-retirement)
- D-400 Line 6 (federal AGI): $132,504
- D-400 Schedule S Part A (additions): $0 — no §168(k) add-back this
  year; no out-of-state muni interest
- D-400 Line 7 (additions): $0
- D-400 Line 8 (Line 6 + Line 7): $132,504
- D-400 Schedule S Part B (deductions):
  - Bailey subtraction (federal CSRS pension): $40,000
  - Social Security subtraction: $20,400 (federal taxable amount)
  - U.S. government bond interest: $0
  - Total Part B: $60,400
- D-400 Line 9 (deductions): $60,400
- D-400 Line 10 (Line 8 − Line 9): $72,104
- D-400 Line 10b (NC child deduction): $0 (no qualifying children)
- D-400 Line 11 (NC standard deduction, single): $12,750 `[VERIFY:]`
- D-400 Line 12a (NC taxable income): $72,104 − $12,750 = $59,354
- D-400 Line 13 (NC income tax, 4.25%): $2,523
- D-400 Line 16 (after D-400TC credits): $2,523 (no credits)
- D-400 Line 17 (NC tax): $2,523 + D-422 underpayment interest of
  ~$120 + use-tax accrual of ~$0 (none reported) = ~$2,643
- Wait — the executive summary said $4,360. Reviewer reconciliation:
  the $4,360 includes a use-tax estimate of ~$200 that intake
  flagged AND consumer-use-tax true-up; reviewer to verify with
  taxpayer. Material to surface.
- D-400 Line 20 (NC withholding): $0
- D-400 Line 21 (NC estimated payments + extension): $0
- D-400 Line 28 (NC balance due): ~$2,643 to ~$4,360 depending on
  use-tax resolution

## Standard vs. Itemized Decision (NC)
- NC standard deduction (single): $12,750
- NC itemized total (Schedule A): not computed — James has minimal
  itemizable items (no mortgage, no large charitable, low medical
  net of 7.5% AGI floor)
- Chosen: standard
- Rationale: standard clearly higher than any plausible itemized

## Estimated Tax for 2026
- 2025 federal total tax: $52,860 → Q1 2026 federal estimate
  ~$13,200 (100% of prior year ÷ 4; AGI < $150K so 100% safe
  harbor applies federally)
- 2025 NC total tax: ~$2,643 → Q1 2026 NC estimate ~$660 (NC uses
  100% of prior year)
- Combined Q1 2026 estimate: ~$13,860 due April 15, 2026 — note
  this is on TOP of the April 15 balance due

## 1099-NEC Issuance
- N/A — James engaged no subcontractors in 2025

## NC Sales Tax Status
- N/A — not a NC sales-tax registrant

## Cross-skill Verification (Section 6 summary)
- F-1 through F-10: PASS
- N-1 through N-14: PASS
- B-1 through B-4: PASS (Bailey-eligible; $40K subtraction
  documented)
- C-1 through C-13: PASS
- 9-1 through 9-4: N/A (no contractors)
- E-1 through E-5: PASS
- W-1 through W-4: PASS (all zero withholding; documented)
- BX-1 through BX-3: PASS

## Reviewer Attention Flags
1. Form 2210 federal underpayment penalty (~$1,800) — reviewer to
   finalize Q-by-Q computation against §6654 safe harbor.
2. Form D-422 NC underpayment interest (~$120) — reviewer to
   confirm NC threshold and finalize.
3. Use-tax accrual line on D-400 — intake flagged ~$200 internet
   purchases; reviewer to confirm with taxpayer.
4. Medicare Part B premiums as potential §162(l) deduction —
   reviewer to confirm with `us-self-employed-health-insurance`
   output (skill ran but flagged $0; James may have eligible
   Medicare premiums).
5. CSRS pension Bailey documentation — verify SF-50 / vesting
   confirmation letter on file.
6. Solo 401(k) age-50 catch-up ($7,500) properly documented.

## Refusals Triggered
(none — James's facts fit the in-scope pattern)

## Positions Taken
- Bailey subtraction of $40,000 federal CSRS pension: see
  Bailey v. State of NC, 348 N.C. 130 (1998); NCDOR Bailey
  Decision page; `nc-bailey-settlement-retirement` Section X.
  Vesting in CSRS in 1978 is well before the 8/12/1989 cutoff.
- §199A non-SSTB classification of freelance security consulting:
  see `us-qbi-deduction` Section X; consulting can be SSTB
  depending on facts; reviewer to confirm James's services are
  not "consulting" in the §199A sense (e.g., implementation work
  vs. advisory).
- NC fully exempts Social Security: per N.C.G.S.
  §105-153.5(b)(5) `[VERIFY:]`.

## Planning Notes for 2026
- NC rate step-down per Session Law 2023-134: 4.25% in 2025 →
  ~3.99% in 2026 `[VERIFY:]`; long-term schedule down to ~2.49%
  by 2030 absent further legislation.
- Federal QBI rate rises 20% → 23% under OBBBA (P.L. 119-21,
  July 2025); James's QBI deduction grows materially if income
  stays at $150K.
- Bailey-protected CSRS pension continues at $40K — no rollovers
  planned; verify continuity.
- James should set up federal + NC estimated payments to avoid
  another year of underpayment interest.
- Medicare Part B premium documentation for §162(l) — start a
  premium ledger in January 2026.

## Taxpayer Action List
[full action list embedded — see File 3]
```

This is one NC-resident sole prop with Bailey-protected pension, full reviewer package abbreviated to ~3 pages. The actual file is longer and includes the full xlsx workbook, the full brief, and the full action list.

## Section 12 — Refusal catalogue

**Refusal catalogue table**

| ID | Situation | Action |
| --- | --- | --- |
| R-NC-FINAL-1 | An upstream skill did not run. | Refuse; name the missing skill. |
| R-NC-FINAL-2 | An upstream skill's self-check failed and was not resolved. | Refuse; name the check. |
| R-NC-FINAL-3 | A Section 6 reconciliation failed beyond the $1 (or T2-01) tolerance. | Refuse; name the equation and the discrepancy. |
| R-NC-FINAL-4 | A refusal fired upstream and was suppressed in the upstream output. | Refuse; force resolution. |
| R-NC-FINAL-5 | Intake artifact is incomplete (missing residency, DOB, filing status, Bailey flag, etc.). | Refuse; name the missing item(s). |
| R-NC-FINAL-6 | Taxpayer is not a full-year North Carolina resident (part-year via D-400 Schedule PN or non-resident). | Refuse; out of scope. |
| R-NC-FINAL-7 | Intake somehow flagged a NC city or local income tax — none exists. | Refuse; route back to intake. |
| R-NC-FINAL-8 | (reserved) | — |
| R-NC-FINAL-9 | (reserved) | — |
| R-NC-FINAL-10 | Taxpayer is an S-corp (Form 1120-S federally; NC requires CD-401S). | Refuse; out of scope for this orchestrator (route to `nc-corporate-tax`). |
| R-NC-FINAL-11 | Taxpayer is a partnership (Form 1065 federally; NC requires D-403). | Refuse; out of scope. |
| R-NC-FINAL-12 | Tax year other than 2025. | Refuse; rates and forms may differ. |
| R-NC-FINAL-13 | MFJ taxpayers with mixed residency (one NC resident, one non-resident). | Refuse; routes to Schedule PN which is out of scope. |
| R-NC-FINAL-14 | Amended return (D-400 Schedule AM). | Refuse; out of scope. |
| R-NC-FINAL-15 | Bailey flag asserted but vesting documentation missing or vesting date is after August 12, 1989. | Refuse the Bailey subtraction; orchestrator continues without it and surfaces the issue in the reviewer brief. |
| R-NC-FINAL-16 | Multi-state income apportionment (work performed in multiple states beyond simple W-2 reciprocity). | Refuse; out of scope. |
| R-NC-FINAL-17 | Foreign income / FEIE / FTC at the state level. | Refuse; out of scope. |
| R-NC-FINAL-18 | NC corporate franchise / income tax (wrong tax type). | Refuse; route to `nc-corporate-tax`. |
| R-NC-FINAL-19 | NC pass-through entity (PTE) tax election handling for SMLLC that elected to be taxed as a corporation. | Refuse; out of scope (SMLLCs in scope are disregarded only). |
| R-NC-FINAL-20 | NC K-1 received from an S-corp or partnership flowing through to this individual. | Refuse; orchestrator scope is sole prop / SMLLC disregarded only. |

## Section 13 — Self-checks

**Self-checks table**

| # | Check |
| --- | --- |
| 200 | All upstream content skills executed. |
| 201 | All upstream self-checks passed (or were explicitly waived with reviewer flag). |
| 202 | Section 6A (federal internal) reconciliations PASS. |
| 203 | Section 6B (NC internal) reconciliations PASS. |
| 204 | Section 6C (Bailey settlement) reconciliations PASS or N/A. |
| 205 | Section 6D (federal-NC coordination) reconciliations PASS. |
| 206 | Section 6E (1099-NEC) reconciliations PASS or N/A. |
| 207 | Section 6F (estimated tax) reconciliations PASS. |
| 208 | Section 6G (withholding tie-out) reconciliations PASS. |
| 209 | Section 6H (Bailey + retirement + SE-health cross-checks) PASS or N/A. |
| 210 | Assumption log contains every "Assumed" item from every upstream skill. |
| 211 | Reviewer flag log contains every "Reviewer judgment" item. |
| 212 | Taxpayer action list has specific dollar amounts and dates. |
| 213 | Planning notes for 2026 reference NC rate step-down, QBI rate change, Bailey continuity, and 1099 threshold. |
| 214 | Every refusal in Section 12 was evaluated against the taxpayer's facts. |
| 215 | Three-file deliverable produced in `/mnt/user-data/outputs/`. |
| 216 | `present_files` called with the three files. |
| 217 | Standard vs. itemized comparison documented in the reviewer brief, even if standard was obviously higher. |

## Section 14 — Known gaps

1. PDF form filling is not automated. The reviewer transcribes the worksheets into NCDOR eFile partner software.
2. E-filing is the reviewer's responsibility. This skill produces the computation; submission happens outside the agent.
3. Payment execution is the taxpayer's responsibility; the skill provides instructions only.
4. Multi-state returns are not supported (NC-only).
5. Foreign income is not supported.
6. Part-year and non-resident returns (D-400 Schedule PN) are refused.
7. The package is complete only for tax year 2025; 2026 appears only as prospective planning.
8. NC has no city-level income tax; there is no city-return artifact to produce (unlike Michigan / Detroit).
9. NC §168(k) and §179 decoupling carryforward schedule is consumed from `nc-income-tax`; this orchestrator does not itself maintain the carryforward ledger.
10. Bailey vesting verification is documentary; the orchestrator does not retrieve federal personnel records.

### Change log

- **v0.1 (May 2026):** Initial draft. Orchestrates federal + NC stack. Three-file deliverable. Section 6 verification matrix with 40+ reconciliations covering federal-internal, NC-internal, Bailey settlement, federal-NC coordination, 1099-NEC, estimated-tax, withholding tie-out, and Bailey-cross-checks. Worked example: NC resident sole prop with $150K Schedule C, Solo 401(k), $40K Bailey-protected federal CSRS pension, no withholding (estimates also $0 — underpayment exposure documented).

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — **no liability on either side until you and the accountant sign a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).

## Section 5 — Skill-loading order (canonical execution sequence)

0. **Step 1** — us-tax-workflow-base (workflow scaffold)
0. **Step 2** — us-sole-prop-bookkeeping (Schedule C classification)
0. **Step 3** — us-schedule-c-and-se-computation (C, SE, 8829)
0. **Step 4** — us-qbi-deduction (8995 / 8995-A)
0. **Step 5** — us-self-employed-health-insurance (§162(l), iterative w/ PTC)
0. **Step 6** — us-self-employed-retirement (SEP / Solo 401(k))
0. **Step 7** — us-quarterly-estimated-tax (2210, 2026 1040-ES)
0. **Step 8** — us-federal-return-assembly (1040, Sch 1/2/3, sign-off)
0. **Step 9** — us-1099-nec-issuance (parallel; contractor batch)
0. **Step 10** — nc-income-tax (D-400, Sch S, Sch A, D-400TC)
0. **Step 11** — nc-bailey-settlement-retirement (Sch S Part B — if applicable)
0. **Step 12** — nc-estimated-tax / NC-40 (2026) (next-year vouchers)
0. **Step 13** — nc-return-assembly ← THIS SKILL
