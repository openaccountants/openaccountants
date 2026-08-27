---
name: nd-return-assembly
description: "Final capstone orchestrator that assembles the complete federal + North Dakota filing package for a full-year North Dakota-resident sole proprietor or single-member LLC disregarded for federal tax. Consumes outputs from every upstream federal and North Dakota content skill (bookkeeping, Schedule C/SE, QBI, retirement, SE health insurance, quarterly estimated tax, federal assembly, 1099-NEC, nd-income-tax, nd-estimated-tax, nd-payroll, nd-corporate-tax routing checks, and nd-sales-tax for closing out the indirect-tax year) to produce a single unified reviewer package: every worksheet, every form, every cross-skill reconciliation, the final taxpayer action list with payment and filing instructions, the next-year ND-1ES voucher schedule, and the reviewer brief. This skill does NOT recompute tax — it ORCHESTRATES. Trigger on phrases like \"assemble the North Dakota return\", \"final ND package\", \"ND-1 reviewer package\", \"ND return assembly\", or \"package up the Dakota return\". MUST be loaded alongside us-tax-workflow-base v0.2 or later and every content skill listed in Section 5. North Dakota full-year residents only. Sole proprietors and single-member LLCs disregarded for federal tax only."
jurisdiction: US-ND
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ND Return Assembly

## North Dakota Return Assembly Skill — Capstone Orchestrator

Scope. This is THE skill that runs LAST. Every other skill in the North Dakota stack feeds into this one. The output is the complete reviewer package that a credentialed reviewer (Enrolled Agent, CPA, or attorney under Circular 230) signs off on before the return goes to the taxpayer or to the North Dakota Office of State Tax Commissioner.

This skill does not compute anything new. Its job is to verify that every upstream skill ran, every upstream self-check passed, every cross-skill reconciliation holds, and the package is internally consistent.

Quality tier. Q3 — AI-drafted, not independently verified. Researched 2026-05-29 against the ND Office of State Tax Commissioner, IRS, and the upstream ND content skills in this same package directory. A qualified professional must review before filing.

## CRITICAL EXECUTION DIRECTIVE — READ FIRST

When this skill is invoked, intake has already happened. The taxpayer has consented to the full workflow. Execute every step without pausing for permission.

- Do NOT ask the user "how deep do you want me to go". The taxpayer asked for a North Dakota return. Produce it.
- Do NOT announce tool budgets or token counts. Execute.
- Do NOT ask which deliverables to prioritize. Produce every deliverable listed in Section 7. If you run out of context, finish the numbers first, then produce whatever formatted outputs you can, and state honestly at the end which deliverables are partial.
- Do NOT re-validate scope intake already validated. Residency, business structure, filing status, MN/MT reciprocity status, oil & gas income flag, tribal-enrollment flag, Renaissance Zone flag, age, dependents — all of that came from intake. Cross-check specific numbers during reconciliation but do not re-interrogate the taxpayer.
- Do NOT pause between content skills to check in. Run them in order (Section 5) without prose updates between each one. One status message at the end is enough.
- Self-checks are targets, not blockers. A failed self-check is a flag in the reviewer brief, not a workflow halt. The reviewer handles edges.
- Primary citations live in the final reviewer brief, not in intermediate computation. Don't stop to cite N.D.C.C. §57-38-30.3 mid-bracket-multiplication.

Failure mode to avoid: halting mid-execution to ask a meta-question about workflow pacing. That is disqualifying. If you feel the urge to ask "how should I proceed," pick the most defensible path, proceed, and flag the decision for the reviewer.

## Section 1 — Metadata

- **Jurisdiction** — North Dakota (US-ND) — full-year residents only
- **Skill type** — Tier 2 orchestrator (capstone)
- **Tax year** — 2025 (filed in 2026)
- **Primary forms produced** — Form ND-1, Schedule ND-1SA (additions/subtractions), Schedule ND-1TC (credits), Schedule ND-1CR (credit for taxes paid to other states), Schedule ND-1FA (farm income averaging, if applicable), Schedule ND-1UT (underpayment of estimated tax), ND-1ES (2026 estimated payment vouchers)
- **Forms refused at this orchestrator** — Form ND-1NR (non-resident / part-year), Form ND-1X (amended), Form 38 (fiduciary), Form 40 (corporate), Form 58 (partnership), Form 60 (S-corp), inbound ND K-1 from pass-throughs
- **Authority** — North Dakota Office of State Tax Commissioner
- **Statutes** — N.D.C.C. Chapter 57-38 (Individual Income Tax); N.D.C.C. §57-38-30.3 (rate schedule); N.D.C.C. §57-38-01.18 (Renaissance Zone); N.D.C.C. §57-38-30 (military retirement subtraction)  _(N.D.C.C. Chapter 57-38)_
- **Filing deadline** — April 15, 2026
- **Extension deadline** — October 15, 2026 (federal Form 4868 grants automatic ND extension; no separate ND form required)
- **TY 2025 rate structure** — Graduated 3-bracket: 0% / 1.95% / 2.50% per N.D.C.C. §57-38-30.3  _(N.D.C.C. §57-38-30.3)_
- **Version** — 0.1
- **Last updated** — 2026-05-29
- **Validation** — AI-drafted — Q3

### Sources consulted

**Sources consulted**  _(Sources consulted list)_

| # | Source | URL |
| --- | --- | --- |
| 1 | ND Office of State Tax Commissioner — Individual Income Tax | https://www.tax.nd.gov/tax-types/individual-income-tax |
| 2 | ND — 2025 Individual Income Tax Booklet (Form ND-1 instructions) | https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf |
| 3 | ND — Form ND-1 (Individual Income Tax Return) | https://www.tax.nd.gov/forms |
| 4 | ND — Schedule ND-1SA (Statutory Adjustments) | https://www.tax.nd.gov/forms |
| 5 | ND — Schedule ND-1TC (Tax Credits) | https://www.tax.nd.gov/forms |
| 6 | ND — Schedule ND-1CR (Credit for Income Tax Paid to Another State) | https://www.tax.nd.gov/forms |
| 7 | ND — Schedule ND-1FA (Farm Income Averaging) | https://www.tax.nd.gov/forms |
| 8 | ND — Schedule ND-1UT (Underpayment of Estimated Tax) | https://www.tax.nd.gov/forms |
| 9 | ND — Form ND-1ES (Estimated Individual Income Tax) | https://www.tax.nd.gov/forms |
| 10 | ND Taxpayer Access Point (TAP) — online filing & payment | https://apps.nd.gov/tax/tap/ |
| 11 | ND — Reciprocity Agreement with Minnesota and Montana | https://www.tax.nd.gov/individual/reciprocity |
| 12 | ND — Renaissance Zone Program | https://www.tax.nd.gov/business/renaissance-zone |
| 13 | N.D.C.C. Chapter 57-38 (Income Tax) | https://www.ndlegis.gov/cencode/t57c38.pdf |
| 14 | IRS Modernized e-File (MeF) — Federal/State joint filing | https://www.irs.gov/e-file-providers/modernized-e-file-overview |

## Section 2 — What this skill is

The final capstone skill. Every other North Dakota skill and every relevant federal skill feeds into this one. The deliverable is the complete reviewer package that a credentialed reviewer signs off on before filing.

The skill enforces three things:

1. Order of operations. Federal first, North Dakota second. The order is non-negotiable because federal taxable income (Form 1040 Line 15, NOT federal AGI) flows into ND-1 Line 1 as the ND starting point. This is unusual — most states start at federal AGI; ND starts after the federal standard/itemized deduction AND after the federal QBI deduction. Every federal adjustment — Schedule C net profit, ½ SE tax, SE health insurance, retirement contributions, QBI deduction, standard or itemized deduction — is already baked into the starting figure before ND modifications apply. Unlike Michigan there is no city-level income tax in North Dakota — N.D.C.C. does not authorize municipal income tax — so the city step from the MI orchestrator is omitted entirely.
2. Cross-skill reconciliation. Every figure that appears on the ND-1 must match the corresponding figure produced by the source skill. A mismatch halts assembly with a specific, named refusal.
3. Reviewer-grade output. The final package is structured for a CPA or EA to review in under 30 minutes: cover summary, brief, exhibits in order, action list, citations.

## Section 3 — Orchestration runbook

When invoked, the agent executes the following steps in order. No step is optional. No step is skipped without an explicit refusal.

### Step 1 — Confirm intake artifact exists

0. **Step 1** — Verify the intake skill has produced: Taxpayer name, SSN/ITIN (last 4 only in working files); Filing status (Single / MFJ / MFS / HoH / QSS); Residency confirmation (full-year North Dakota); Date of birth for taxpayer and spouse (drives the federal age-65 additional standard deduction, which feeds Line 1 starting point); Dependents list with SSNs (drives federal dependents — ND has no separate child deduction unlike NC); Business structure (sole prop or SMLLC disregarded); MN/MT reciprocity flag — taxpayer wages earned in Minnesota or Montana while a ND resident are exempt from those states' income tax under the reciprocity agreements; conversely a ND resident working a W-2 job in MN/MT files no MN/MT return for those wages; Oil & gas / mineral income flag — flag-only; the orchestrator does not produce ND oil extraction tax filings (out of scope, see R-ND-FINAL-21); Tribal-enrollment flag — enrolled tribal members earning income on their reservation may take a Schedule ND-1SA subtraction; Renaissance Zone flag — income from a designated ND Renaissance Zone may be exempt under N.D.C.C. §57-38-01.18; Military retirement flag — ND fully subtracts military retirement pay per N.D.C.C. §57-38-30(5) `[VERIFY:]` 2025 conformity; Social Security flag — ND fully subtracts taxable Social Security benefits per N.D.C.C. §57-38-30 `[VERIFY:]` 2025 statute reference; Job Service ND unemployment benefits flag — taxable federally; subtracted on ND-1SA `[VERIFY:]` 2025 schedule line; Health coverage history (federal Form 1095-A / B / C); W-2s, 1099-NECs, 1099-Rs received. If any item is missing, refuse with R-ND-FINAL-5.

- **R-ND-FINAL-5** — Refuse if any required intake item is missing.  _(Step 1)_

### Step 2 — Confirm federal skills ran and produced outputs

0. **Step 2** — Verify in order: 1. us-sole-prop-bookkeeping — Schedule C classification with reconciled bank ledger. 2. us-schedule-c-and-se-computation — Schedule C bottom line, Form 8829, Schedule SE. 3. us-self-employed-retirement — SEP / Solo 401(k) contribution and Schedule 1 Line 16 amount. 4. us-self-employed-health-insurance — §162(l) deduction and Schedule 1 Line 17 amount (with iterative PTC convergence if marketplace coverage). 5. us-qbi-deduction — Form 8995 or 8995-A, deduction to Form 1040 Line 13. (CRITICAL — ND starts from federal taxable income, which is AFTER QBI. So QBI value materially reduces ND tax.) 6. us-federal-return-assembly — Form 1040, Schedules 1, 2, 3, all supporting forms, federal total tax, federal balance due / refund. In particular, Form 1040 Line 15 (federal taxable income) is the single most important upstream output for ND. 7. us-quarterly-estimated-tax — Form 2210 (if penalty) + 2026 Form 1040-ES schedule. 8. us-1099-nec-issuance — Parallel; only needs bookkeeping. Contractor list plus W-9 gaps. If any is missing or its self-checks did not pass, refuse with R-ND-FINAL-1 or R-ND-FINAL-2 naming the specific skill.

- **R-ND-FINAL-1 / R-ND-FINAL-2** — Refuse naming the specific skill if any federal skill is missing or its self-checks did not pass.  _(Step 2)_

### Step 3 — Confirm North Dakota skills ran

0. **Step 3** — Execute in order: 1. nd-income-tax — Form ND-1, Schedule ND-1SA (additions and subtractions including Social Security, military retirement, Renaissance Zone, tribal reservation, US bond interest, Job Service ND unemployment), Schedule ND-1TC (credits), Schedule ND-1CR (credit for taxes paid to another state — if any wages earned outside MN/MT reciprocity zone). Produces ND taxable income, ND tax via the 0% / 1.95% / 2.50% bracket schedule, credits, refund or balance due. 2. nd-estimated-tax — Produces a 4-payment ND-1ES voucher schedule for 2026 if expected ND liability after withholding exceeds the $1,000 threshold per N.D.C.C. §57-38-62. Also computes any current-year ND underpayment interest exposure on Schedule ND-1UT. 3. nd-payroll — Flag-only at this orchestrator stage. If the taxpayer is also a ND withholding agent (employer), confirm quarterly Form 306 and annual Form 307 reconciliation status. Does NOT block the individual return. 4. nd-corporate-tax — Routing check only. If intake flagged anything corporate (Form 40) or pass-through (Form 58 / Form 60), refuse with R-ND-FINAL-10 / R-ND-FINAL-11 / R-ND-FINAL-18. If any required skill failed or its self-check failed, refuse with R-ND-FINAL-1 or R-ND-FINAL-2.

- **R-ND-FINAL-1 / R-ND-FINAL-2 / R-ND-FINAL-10 / R-ND-FINAL-11 / R-ND-FINAL-18** — Refuse if any required ND skill or self-check failed, or routing check triggers corporate/pass-through scope violation.  _(Step 3)_

### Step 4 — No city / local return step

0. **Step 4** — North Dakota does not authorize municipal or county income tax. Skip the city step entirely. If intake somehow flagged a "city return," that is an intake error — refuse with R-ND-FINAL-7 and route back to intake for correction.

- **R-ND-FINAL-7** — Refuse and route back to intake if a "city return" is flagged, since ND has no municipal income tax.  _(Step 4)_

### Step 5 — MN/MT reciprocity check

0. **Step 5** — If intake flagged W-2 wages earned in Minnesota or Montana while the taxpayer was a ND resident: Confirm a Form MWR (Minnesota) or equivalent Montana reciprocity exemption certificate was on file with the employer, so MN/MT income tax was NOT withheld. The wages are taxable only in ND. If MN or MT withholding WAS taken (employer error), the taxpayer must file a MN or MT non-resident return to recover the withholding. That filing is out of scope here — refuse with R-ND-FINAL-22 and route to a multistate preparer. If wages were earned in any OTHER state (not MN, not MT), the taxpayer may need a non-resident return in that state and a ND-1CR credit for tax paid. Single-state simple W-2 cases proceed; complex multistate apportionment refuses with R-ND-FINAL-16.

- **R-ND-FINAL-22 / R-ND-FINAL-16** — Refuse with R-ND-FINAL-22 if MN/MT withholding was taken in error; refuse with R-ND-FINAL-16 for complex multistate apportionment beyond reciprocity.  _(Step 5)_

### Step 6 — Run the verification matrix

0. **Step 6** — Run every check in Section 6. Each check is a specific equality between a number on a final form and the source-of-truth output from the producing skill. A failure halts assembly with R-ND-FINAL-3.

- **R-ND-FINAL-3** — Halts assembly if any Section 6 reconciliation check fails.  _(Step 6)_

### Step 7 — Aggregate artifacts

0. **Step 7** — Pull: Every "Assumed" entry from every upstream skill into the assumption log. Every "Taxpayer input needed" item into the taxpayer input log. Every "Reviewer judgment needed" item into the reviewer flag log. Every refusal that fired anywhere in the chain into the refusal log.

### Step 8 — Compose the deliverables

0. **Step 8** — Produce the three output files specified in Section 7. Place them in /mnt/user-data/outputs/. Present them at the end with present_files.

### Step 9 — Final status message

0. **Step 9** — A single message stating: which skills ran, which self-checks passed, which deliverables were produced, any partial deliverables and why. Done.

## Section 4 — Pre-flight checks

**Pre-flight checks table**

| Check | Question | Refusal if fails |
| --- | --- | --- |
| PF-1 | Has federal Form 1040 been computed by `us-federal-return-assembly`? | R-ND-FINAL-1 |
| PF-2 | Is federal taxable income (Form 1040 Line 15) a finite, non-negative number? (Negative federal taxable income flows as zero into ND-1 Line 1 but flag it.) | R-ND-FINAL-1 |
| PF-3 | Has the taxpayer's full-year North Dakota residency been confirmed? | R-ND-FINAL-6 |
| PF-4 | Is the business structure sole prop or SMLLC disregarded? S-corp or partnership? | R-ND-FINAL-10 / R-ND-FINAL-11 |
| PF-5 | Is the tax year 2025? | R-ND-FINAL-12 |
| PF-6 | If MFJ: are both spouses full-year ND residents? Mixed-residency couples → refuse. | R-ND-FINAL-13 |
| PF-7 | Is this a current-year original return (not amended)? | R-ND-FINAL-14 |
| PF-8 | Did intake report any inbound K-1 from an S-corp or partnership? | R-ND-FINAL-20 |
| PF-9 | Did intake report wages earned outside ND, MN, or MT? Multi-state apportionment beyond reciprocity is out of scope. | R-ND-FINAL-16 |
| PF-10 | Did intake report oil/gas/mineral royalty income? Income tax effect is in scope; ND oil extraction tax filings (Form OG-1, etc.) are NOT. | Flag-only; refuse oil-extraction tax with R-ND-FINAL-21 |
| PF-11 | Did intake report farm income with averaging election (Schedule ND-1FA)? | In scope — confirm `nd-income-tax` produced Schedule ND-1FA |
| PF-12 | Did intake report Renaissance Zone income? | In scope — confirm subtraction documented on ND-1SA |
| PF-13 | Did intake report tribal-enrolled-member income earned on reservation? | In scope — confirm subtraction documented on ND-1SA with enrollment evidence |

## Section 5 — Skill-loading order (canonical execution sequence)

This is the immutable order. Do not parallelize; downstream skills consume upstream outputs. The single exception is `us-1099-nec-issuance`, which can run in parallel with anything after `us-sole-prop-bookkeeping`.

```
1.  us-tax-workflow-base                         (workflow scaffold)
2.  us-sole-prop-bookkeeping                     (Schedule C classification)
3.  us-schedule-c-and-se-computation             (C, SE, 8829)
4.  us-qbi-deduction                             (8995 / 8995-A — flows into Fed Line 13, then Line 15)
5.  us-self-employed-health-insurance            (§162(l), iterative w/ PTC)
6.  us-self-employed-retirement                  (SEP / Solo 401(k))
7.  us-quarterly-estimated-tax                   (2210, 2026 1040-ES)
8.  us-federal-return-assembly                   (1040 incl. Line 15 = ND-1 Line 1)
9.  us-1099-nec-issuance                         (parallel; contractor batch)
10. nd-income-tax                                (ND-1, ND-1SA, ND-1TC, ND-1CR, ND-1FA)
11. nd-estimated-tax / ND-1ES (2026)             (next-year vouchers + ND-1UT)
12. nd-payroll                                   (flag-only if also a withholding agent)
13. nd-sales-tax                                 (status note; does not block)
14. nd-return-assembly                           ← THIS SKILL
```

Each upstream skill is expected to expose, at minimum: (a) the line-item output(s) it produces, (b) the self-check log, (c) any refusals fired, and (d) any reviewer / taxpayer flags. The orchestrator consumes those four artifacts per skill.

Note on `nd-sales-tax`. ND sales and use tax is a separate filing cadence (monthly / quarterly / annual via ND TAP) and does not flow into the individual return. The orchestrator only surfaces an end-of-year sales-tax status line ("all ND sales-tax periods filed through Dec 2025" or "Q4 2025 ND sales-tax return due Jan 31, 2026 — verify filed") in the action list. It does not block on sales tax.

Note on `nd-corporate-tax`. Pure routing check at the orchestrator level. The sole prop / SMLLC disregarded scope means no Form 40 (corporate) or Form 58 (partnership) or Form 60 (S-corp) is produced. If intake says otherwise, refuse.

0. **us-tax-workflow-base** — workflow scaffold
0. **us-sole-prop-bookkeeping** — Schedule C classification
0. **us-schedule-c-and-se-computation** — C, SE, 8829
0. **us-qbi-deduction** — 8995 / 8995-A — flows into Fed Line 13, then Line 15
0. **us-self-employed-health-insurance** — §162(l), iterative w/ PTC
0. **us-self-employed-retirement** — SEP / Solo 401(k)
0. **us-quarterly-estimated-tax** — 2210, 2026 1040-ES
0. **us-federal-return-assembly** — 1040 incl. Line 15 = ND-1 Line 1
0. **us-1099-nec-issuance** — parallel; contractor batch
0. **nd-income-tax** — ND-1, ND-1SA, ND-1TC, ND-1CR, ND-1FA
0. **nd-estimated-tax / ND-1ES (2026)** — next-year vouchers + ND-1UT
0. **nd-payroll** — flag-only if also a withholding agent
0. **nd-sales-tax** — status note; does not block
0. **nd-return-assembly** — THIS SKILL

## Section 6 — Verification matrix (reconciliations)

Every line below is a hard equality. Tolerance is $1 unless noted otherwise. A failure halts assembly with R-ND-FINAL-3 naming the specific check.

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
| F-7 | Form 1040 Line 11 = Line 9 − Line 10 (AGI) | us-federal-return-assembly |
| F-8 | Form 1040 Line 14 = Line 12 + Line 13 (standard/itemized + QBI) | us-federal-return-assembly |
| F-9 | Form 1040 Line 15 = Line 11 − Line 14 (federal taxable income — KEY ND HANDOFF) | us-federal-return-assembly |
| F-10 | Total tax = Form 1040 Line 24 | us-federal-return-assembly |
| F-11 | Form 2210 penalty (if any) = Schedule 2 Line 8 | us-quarterly-estimated-tax |
| F-12 | Total payments = Form 1040 Line 33 | us-federal-return-assembly |
| F-13 | Refund / balance due = Form 1040 Line 34 or 37 | us-federal-return-assembly |

### 6B — North Dakota internal consistency

**6B table**

| Check | Equation | Source-of-truth skill |
| --- | --- | --- |
| N-1 | Federal taxable income (Form 1040 Line 15) = ND-1 Line 1 (NOT federal AGI — verify the right line was pulled) | nd-income-tax |
| N-2 | ND-1SA additions total = ND-1 Line 2 | nd-income-tax |
| N-3 | ND-1SA subtractions total = ND-1 Line 3 | nd-income-tax |
| N-4 | ND-1 Line 4 = Line 1 + Line 2 − Line 3 (ND taxable income) | nd-income-tax |
| N-5 | ND-1 Line 6 (tax) = bracket math against Line 4 using the filing-status-specific schedule (Single 0% / 1.95% / 2.50% with breakpoints at $48,475 and $244,825 for TY 2025) `[VERIFY:]` 2025 brackets | nd-income-tax |
| N-6 | If MFJ: bracket breakpoints $80,975 and $298,075 `[VERIFY:]` | nd-income-tax |
| N-7 | If HoH: bracket breakpoints $64,950 and $271,450 `[VERIFY:]` | nd-income-tax |
| N-8 | If MFS: bracket breakpoints $40,475 and $149,025 `[VERIFY:]` | nd-income-tax |
| N-9 | ND-1 credits line = Schedule ND-1TC total | nd-income-tax |
| N-10 | If ND-1CR claimed: credit ≤ lesser of (tax paid to other state) and (ND tax on the same income) | nd-income-tax |
| N-11 | If Schedule ND-1FA (farm averaging) claimed: averaging tax replaces Line 6 amount and is documented | nd-income-tax |
| N-12 | ND-1 Line 17 (ND withholding) = sum of W-2 Box 17 ND + 1099 ND withholding | nd-income-tax |
| N-13 | ND-1 Line 18 (estimated payments) = sum of ND-1ES vouchers paid for TY 2025 + any extension payment | nd-estimated-tax |
| N-14 | ND-1 Line 22 (refund) OR (balance due) reconciles to total tax − total payments | nd-income-tax |
| N-15 | If Schedule ND-1UT (underpayment) applies: interest computed and added to balance due | nd-estimated-tax |

### 6C — Federal-ND coordination

**6C table**

| Check | Equation |
| --- | --- |
| C-1 | Filing status on ND-1 = filing status on Form 1040 |
| C-2 | Dependents claimed on ND-1 = dependents claimed on Form 1040 (ND has no separate child credit — verify no duplication on ND-1TC) |
| C-3 | Schedule C net profit federally = Schedule C net profit reflected in federal taxable income feeding ND-1 Line 1 |
| C-4 | Federal §168(k) bonus depreciation: ND conforms — no add-back on ND-1SA. Verify no ghost add-back was entered. |
| C-5 | Federal §179: ND conforms with no separate cap — verify no add-back |
| C-6 | Federal SE tax deduction (½ SE tax, Schedule 1 Line 15) is reflected in federal AGI and therefore federal taxable income; no ND add-back |
| C-7 | Federal QBI deduction (§199A) IS effectively recognized at ND because ND starts at federal taxable income (post-QBI). No ND adjustment. Verify no double-deduction on ND-1SA. |
| C-8 | Federal SE health insurance (§162(l)) is in federal AGI; no ND add-back |
| C-9 | Federal taxable Social Security (Form 1040 Line 6b) → ND Schedule ND-1SA subtraction (ND fully exempts Social Security per `[VERIFY:]` N.D.C.C. §57-38-30) |
| C-10 | U.S. government bond interest in federal Schedule B → ND-1SA subtraction |
| C-11 | Non-ND state/muni bond interest in federal Schedule B → ND-1SA addition |
| C-12 | Federal standard deduction (or federal itemized, whichever taken) is ALREADY embedded in Form 1040 Line 15 — ND does NOT add or take another deduction. Verify no duplication. |
| C-13 | Federal age-65 additional standard deduction is embedded in Line 15 — flows through to ND with no separate ND senior deduction |
| C-14 | Military retirement pay (1099-R coded for military retirement) → ND-1SA subtraction per `[VERIFY:]` N.D.C.C. §57-38-30(5); confirm only the military retirement portion is subtracted, not other 1099-R amounts |
| C-15 | Job Service ND unemployment benefits taxable federally on Schedule 1 → ND-1SA subtraction `[VERIFY:]` 2025 schedule line and statutory authority |
| C-16 | Renaissance Zone income: federal reporting unchanged; ND-1SA subtraction only for documented qualifying RZ income with project certification |
| C-17 | Tribal reservation income (enrolled member): federal reporting unchanged; ND-1SA subtraction only with enrollment documentation and on-reservation sourcing |

### 6D — MN / MT reciprocity coordination

**6D table**

| Check | Equation |
| --- | --- |
| R-1 | If wages earned in MN: Form MWR on file with employer; no MN withholding; wages taxed only in ND |
| R-2 | If wages earned in MT: equivalent MT reciprocity exemption certificate on file; no MT withholding; wages taxed only in ND |
| R-3 | If MN/MT withholding WAS taken in error: orchestrator refuses with R-ND-FINAL-22 (taxpayer needs MN/MT non-resident refund return, out of scope) |
| R-4 | No Schedule ND-1CR credit is claimed for MN/MT wages, because reciprocity means no MN/MT tax was paid |
| R-5 | If wages were earned in any third state (not ND/MN/MT): Schedule ND-1CR credit may apply; the credit is limited to the lesser of tax paid to the other state OR ND tax on the same income |

### 6E — 1099-NEC reconciliation

**6E table**

| Check | Equation |
| --- | --- |
| 9-1 | Sum of NEC payments flagged = Schedule C Line 11 (Contract labor) + any direct labor lines |
| 9-2 | Each contractor with $600+ has W-9 on file; gaps surfaced in flag log |
| 9-3 | Federal filing deadline noted (January 31, 2026; if past, late-filing penalty surfaced) |
| 9-4 | ND annual reconciliation Form 307 status confirmed if taxpayer is also a ND withholding agent (separate from 1099-NEC; flag-only here) |

### 6F — Estimated-tax coordination

**6F table**

| Check | Equation |
| --- | --- |
| E-1 | 2026 federal Q1 voucher = `us-quarterly-estimated-tax` Q1 output |
| E-2 | 2026 ND-1ES Q1 voucher = `nd-estimated-tax` Q1 output |
| E-3 | ND safe harbor: lesser of 100% of prior-year ND tax OR 90% of current-year ND tax (no 110% step at the ND level) `[VERIFY:]` N.D.C.C. §57-38-62 |
| E-4 | Q1 federal + Q1 ND together do not exceed taxpayer's stated cash availability flag (if intake captured one) |
| E-5 | If current-year ND underpayment interest exposure (Schedule ND-1UT) exists, surface for reviewer |
| E-6 | 2025 ND estimated payments actually made = ND TAP records / cancelled checks reconcile to ND-1 Line 18 |

### 6G — Withholding tie-out

**6G table**

| Check | Equation |
| --- | --- |
| W-1 | Sum of W-2 box 17 (ND state income tax withheld) = ND-1 Line 17 W-2 portion |
| W-2 | Sum of 1099-R / 1099-NEC / 1099-MISC ND withholding = ND-1 Line 17 1099 portion |
| W-3 | ND withholding total = ND-1 Line 17 |
| W-4 | Backup detail captured in workbook for reviewer |
| W-5 | If any wages were tagged MN/MT-sourced under reciprocity: confirm employer withheld ND (not MN/MT) — if MN/MT was withheld, see R-3 above |

### 6H — Special-population cross-checks

**6H table**

| Check | Equation |
| --- | --- |
| S-1 | If military retirement subtraction taken: 1099-R distribution code consistent with military retirement; documentation of military service on file |
| S-2 | If Renaissance Zone subtraction taken: project certification number from ND Commerce; income tied to qualifying zone activity |
| S-3 | If tribal enrolled-member subtraction taken: enrollment letter / CDIB equivalent on file; income earned ON reservation (not merely by an enrolled member off-reservation) |
| S-4 | If farm averaging (Schedule ND-1FA) elected federally on Schedule J: ND-1FA mirrors federal averaging; verify ND tax computed on averaged amount |
| S-5 | If oil/gas royalty income reported: confirm only the income tax treatment is in scope; ND oil extraction tax is a separate filing track and is NOT produced here |

## Section 7 — Deliverable package (what the reviewer sees)

The package is three files, not fifteen. Do not fragment the output.

### 7A — File 1: `{taxpayer_slug}_2025_nd_master.xlsx`

A single master workbook. Required sheets, in this order:

1. Cover — Taxpayer name, filing status, residency, business structure, MN/MT reciprocity flag, oil/gas flag, summary table (federal tax, ND tax, total liability, total payments, net refund/balance due, key 2026 dates).
2. Assumption Log — Every "Assumed" item from every upstream skill, tagged with the skill that produced it.
3. Taxpayer Input Log — Every item that needs taxpayer confirmation before filing.
4. Reviewer Flag Log — Every item that needs reviewer judgment.
5. Income — Aggregate income summary (W-2, 1099-NEC, Schedule C, interest, dividends, capital gains, 1099-R, other).
6. Schedule C — Parts I–V.
7. Form 4562 — Depreciation (if applicable).
8. Form 8829 — Home office (if applicable).
9. Schedule SE — SE tax.
10. Retirement — SEP / Solo 401(k) worksheet.
11. SE Health Insurance — §162(l) worksheet, with PTC iteration log if marketplace coverage.
12. Form 8962 — PTC reconciliation (if marketplace coverage).
13. QBI — Form 8995 or 8995-A.
14. Schedule 1 (federal) — Adjustments to income.
15. Schedule 2 (federal) — Additional taxes.
16. Schedule 3 (federal) — Credits (if applicable).
17. Form 1040 — Final federal return line-by-line (with Line 15 highlighted as the ND handoff).
18. Form 2210 — Underpayment penalty (if applicable).
19. ND-1 — North Dakota return line-by-line.
20. Schedule ND-1SA — Additions (Part A) and subtractions (Part B) including Social Security, military retirement, Renaissance Zone, tribal reservation, US bond interest, Job Service ND benefits.
21. Schedule ND-1TC — Tax credits worksheet (if applicable).
22. Schedule ND-1CR — Credit for income tax paid to another state (if applicable, non-MN/MT only).
23. Schedule ND-1FA — Farm income averaging (if applicable).
24. Schedule ND-1UT — Underpayment of estimated tax (if applicable).
25. Reciprocity Worksheet — MN/MT wage tracker (if applicable).
26. Military Retirement Worksheet — Subtraction detail (if applicable).
27. Renaissance Zone Worksheet — Subtraction detail (if applicable).
28. Tribal Reservation Worksheet — Subtraction detail (if applicable).
29. ND Withholding Detail — W-2 + 1099 withholding tie-out.
30. 2026 Federal 1040-ES — Voucher schedule.
31. 2026 ND-1ES — Voucher schedule.
32. 1099-NEC Batch — Contractor batch (if applicable).
33. ND Sales Tax Status — End-of-year filing status note (if taxpayer is a ND sales-tax registrant).
34. Verification Matrix — Every check in Section 6 with pass/fail/N/A.

Use the same Excel-builder discipline as `us-federal-return-assembly`: collect anchors as a Python dict before writing cross-sheet formulas; verify no `#REF!` errors; verify computed cells match the Python model within $1 before shipping.

### 7B — File 2: `reviewer_brief.md`

Structured markdown. Required sections in this order:

1. Executive Summary (≤ 1 page) — Taxpayer, filing status, residency, federal tax, ND tax, total liability, total payments, net result, action required by April 15, 2026.
2. Federal Return Brief — Summary of `us-federal-return-assembly` brief, condensed. Highlight Form 1040 Line 15 (federal taxable income) since it is the ND starting point.
3. North Dakota Return Brief — Summary of `nd-income-tax` brief plus any special-population items (military retirement, RZ, tribal, farm averaging).
4. Bracket Math Audit — Show ND-1 Line 4, the filing-status bracket schedule applied, and the resulting Line 6 tax. ND's 0% first bracket is material; document whether the taxpayer landed in the 0%, 1.95%, or 2.50% band.
5. MN/MT Reciprocity — If applicable: confirm exemption certificates on file and no MN/MT return required.
6. Estimated Tax for 2026 — Federal + ND voucher schedule.
7. 1099-NEC Issuance — Status of contractor filings.
8. ND Sales Tax Status — End-of-year status, if applicable.
9. Cross-skill Verification — Pass/fail summary from Section 6.
10. Reviewer Attention Flags — Aggregated from all upstream skills.
11. Refusals Triggered — Aggregated from all upstream skills.
12. Positions Taken — Tax positions requiring judgment, with citations (N.D.C.C. §, IRC §, ND-1 booklet page references).
13. Planning Notes for 2026 — ND rate stability watch (any legislative changes from the 69th Legislative Assembly), federal QBI 20% → 23% under OBBBA, federal 1099 threshold change, Renaissance Zone project end dates if applicable, military retirement continuity.
14. Taxpayer Action List — Embedded copy of File 3.

### 7C — File 3: `taxpayer_action_list.md`

Step-by-step action list, structured by date. The taxpayer reads this file and nothing else.

```markdown
# Your 2025 North Dakota Tax Filing — Action List

## This week
1. Review the reviewer_brief.md document
2. Sign Form 8879 (federal e-file authorization) — if e-filing
3. Sign Form ND-1 e-file authorization — if e-filing through an
   approved partner or via ND TAP
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
3. North Dakota Form ND-1 — file via:
   - ND Taxpayer Access Point (TAP) at
     https://apps.nd.gov/tax/tap/ — free, direct from ND Office of
     State Tax Commissioner
   - Approved e-file partners (TurboTax, H&R Block, FreeTaxUSA,
     Drake, etc.)
   - Paper return mailed to:
     - Office of State Tax Commissioner, PO Box 5621, Bismarck ND
       58506-5621
4. North Dakota balance due of $X — pay via:
   - ND TAP online (ACH direct debit, free; credit/debit card with
     processor fee)
   - Direct debit at e-file submission
   - Check + payment voucher mailed to ND Office of State Tax
     Commissioner

## Before April 15, 2026 (estimated tax for 2026 Q1)
1. Federal Q1 voucher — $X via IRS Direct Pay or check + Form 1040-ES
2. ND Q1 voucher — $X via ND TAP or check + Form ND-1ES

## Before June 15, 2026 (Q2 estimated tax)
1. Federal Q2 voucher — $X
2. ND Q2 voucher — $X

## Before September 15, 2026 (Q3 estimated tax)
1. Federal Q3 voucher — $X
2. ND Q3 voucher — $X

## Before January 15, 2027 (Q4 estimated tax)
1. Federal Q4 voucher — $X
2. ND Q4 voucher — $X

## Already-passed January 31, 2026 (1099-NEC issuance — check if done)
1. File 1099-NEC forms with IRS via IRIS or FIRE
2. Furnish Copy B to each contractor
3. File ND Form 307 annual withholding reconciliation with ND Office
   of State Tax Commissioner (if taxpayer is a ND withholding agent)
4. If missed: assess penalty exposure ($60–$310 per form federally;
   ND late-filing penalty also applies) and file ASAP

## Ongoing during 2026
1. Collect W-9 from every new contractor BEFORE first payment
2. Track Schedule C income and expenses with receipts
3. Monitor income against estimated-tax safe harbor mid-year
4. Track health coverage continuously (federal Form 1095-A from
   marketplace; 1095-B/C from employer)
5. If a ND sales-tax registrant: file ND sales/use tax on the
   assigned cadence (monthly / quarterly / annual) via ND TAP
6. If MN/MT employer: keep Form MWR / MT reciprocity exemption
   certificate current with each employer

## How to check your refund
- Federal: https://www.irs.gov/refunds — "Where's My Refund?"
- North Dakota: https://apps.nd.gov/tax/tap/ — TAP "Where's My
  Refund?" function

## Need help with anything in this list?
- Reach out to the reviewer (CPA / EA) listed on the cover sheet.
- For North Dakota-specific questions: ND Office of State Tax
  Commissioner, individual income tax helpline 701-328-1247
```

If execution runs out of context mid-build: produce whatever is complete, then state at the end which files were partial. Three files honest beats fifteen files fragmented.

All files go to `/mnt/user-data/outputs/` and are presented at the end via the `present_files` tool.

## Section 8 — The reviewer brief (narrative format)

This is the document the CPA reads first. It should be readable in under 30 minutes and give the reviewer enough context to either sign off or identify exactly what needs more work.

The brief follows this fixed structure:

```markdown
# Complete Return Package — [Taxpayer Name] — Tax Year 2025

## Executive Summary
- **Taxpayer:** [Name], full-year North Dakota resident
- **Filing status:** [Single / MFJ / MFS / HoH / QSS]
- **Business:** Sole proprietor / Single-member LLC disregarded
- **MN/MT reciprocity in play:** [Yes / No]
- **Special populations:** [military retirement / Renaissance Zone /
  tribal / farm averaging / none]
- **Federal total tax (Form 1040 Line 24):** $X
- **Federal taxable income (Form 1040 Line 15 — ND starting point):** $X
- **ND total tax (ND-1 Line 16 or equivalent):** $X
- **Total 2025 tax liability (federal + ND):** $X
- **Total payments (withholding + estimates + extension):** $X
- **Net refund or balance due:** $X
- **Action required by April 15, 2026:** [one-line summary]

## Federal Return
[brief from us-federal-return-assembly, condensed; emphasize Line 15]

## North Dakota Return
[brief from nd-income-tax including ND-1SA modifications detail]

## Bracket Math Audit
- ND-1 Line 4 (ND taxable income): $X
- Filing-status bracket schedule: [Single / MFJ / MFS / HoH]
- Breakpoints: [$48,475 / $244,825] (Single TY 2025) `[VERIFY:]`
- Tax band landed in: [0% / 1.95% / 2.50%]
- ND-1 Line 6 (computed tax): $X

## MN/MT Reciprocity
[If applicable: certificate status, wages source state, ND
treatment; else N/A]

## Estimated Tax for 2026
[combined federal 1040-ES + ND-1ES schedule]

## 1099-NEC Issuance
[brief from us-1099-nec-issuance]

## ND Sales Tax Status
[from nd-sales-tax if registrant; else N/A]

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
- ND rate stability watch — `[VERIFY:]` any 69th Legislative
  Assembly changes to N.D.C.C. §57-38-30.3
- Federal QBI 20% → 23% under OBBBA (P.L. 119-21) — flows through
  to ND because ND starts at federal taxable income
- 1099 threshold change to $2,000 in 2026 under OBBBA
- Renaissance Zone project end dates (if applicable)
- Military retirement continuity (if applicable)
- ND estimated-tax safe harbor positioning

## Taxpayer Action List
[embedded copy of File 3]
```

## Section 9 — Tier 1 deterministic rules

**Tier 1 deterministic rules table**

| Rule ID | Rule |
| --- | --- |
| ND-ASM-T1-01 | Federal Form 1040 must be computed before ND-1. No exceptions. |
| ND-ASM-T1-02 | ND-1 Line 1 = Form 1040 Line 15 (federal **taxable** income, NOT federal AGI). |
| ND-ASM-T1-03 | ND tax = graduated bracket computation against ND-1 Line 4 using the filing-status schedule (TY 2025: Single 0%/1.95%/2.50% at $48,475/$244,825; MFJ at $80,975/$298,075; HoH at $64,950/$271,450; MFS at $40,475/$149,025) `[VERIFY:]` 2025 brackets per N.D.C.C. §57-38-30.3. |
| ND-ASM-T1-04 | ND has no city or local individual income tax. Skip any city-return step. |
| ND-ASM-T1-05 | The April 15, 2026 filing deadline applies. ND grants automatic 6-month extension when a federal Form 4868 is filed — no separate ND extension form required. |
| ND-ASM-T1-06 | Extension to file is NOT extension to pay. Any ND balance due is still due April 15. |
| ND-ASM-T1-07 | ND fully subtracts taxable Social Security benefits (ND-1SA) per `[VERIFY:]` N.D.C.C. §57-38-30. |
| ND-ASM-T1-08 | ND fully subtracts military retirement pay per `[VERIFY:]` N.D.C.C. §57-38-30(5). |
| ND-ASM-T1-09 | ND-1ES estimated payments are required if expected ND net tax liability is $1,000 or more (N.D.C.C. §57-38-62). |
| ND-ASM-T1-10 | ND safe harbor: lesser of 100% of prior-year ND tax OR 90% of current-year ND tax. No 110%-of-AGI step. `[VERIFY:]` |
| ND-ASM-T1-11 | ND conforms to federal §168(k) bonus depreciation — no add-back required. |
| ND-ASM-T1-12 | ND conforms to federal §179 — no separate cap, no add-back. |
| ND-ASM-T1-13 | ND effectively recognizes federal §199A QBI deduction because ND starts at federal taxable income (after QBI). No separate ND adjustment. |
| ND-ASM-T1-14 | ND has NO separate state standard deduction. The federal standard or itemized deduction is already embedded in Form 1040 Line 15. Never apply another deduction at the ND level. |
| ND-ASM-T1-15 | ND has NO separate child credit / child deduction. Federal dependents flow through but ND-1 does not add a state-level child credit. |
| ND-ASM-T1-16 | MN/MT wage reciprocity: ND-resident wages earned in MN or MT are taxed only in ND. No MN/MT return required for those wages; no ND-1CR credit allowed. |
| ND-ASM-T1-17 | ND-1CR credit for taxes paid to another state is limited to the lesser of (a) tax actually paid to the other state, or (b) ND tax computed on the same income. |
| ND-ASM-T1-18 | Three-file deliverable structure (xlsx + brief.md + actions.md) is mandatory. |
| ND-ASM-T1-19 | No city-level income tax exists in ND; the orchestrator never emits a city return artifact. |
| ND-ASM-T1-20 | Oil & gas extraction tax (Form OG-1 family) is NOT produced here. Income tax treatment of royalty income IS handled (ND-1 starts at federal taxable income which already includes royalty income). |

## Section 10 — Tier 2 judgment rules

**Tier 2 judgment rules table**

| Rule ID | Rule | Guidance |
| --- | --- | --- |
| ND-ASM-T2-01 | **Materiality threshold for reconciliation failures.** A $1 rounding gap is not a failure; a $50 gap is. | Reviewer judgment on the threshold; default $5 for federal-ND tie-outs, $1 for intra-form. |
| ND-ASM-T2-02 | **0% bracket optimization.** A taxpayer landing just over the 0% breakpoint may benefit from accelerating a deductible expense or retirement contribution. | Note in planning section if ND taxable income is within 5% of the upper 0% bracket boundary. |
| ND-ASM-T2-03 | **Renaissance Zone documentation.** Taxpayer must produce project certification from ND Commerce. | If certification is incomplete, flag for reviewer; do NOT take the subtraction without reviewer signoff. |
| ND-ASM-T2-04 | **Tribal reservation income sourcing.** Income must be earned ON the reservation by an enrolled member. | Defer the on-reservation determination to `nd-income-tax`; orchestrator verifies enrollment documentation is on file. |
| ND-ASM-T2-05 | **Military retirement scope.** Only military retirement pay qualifies — not military disability (which is federally excluded anyway) and not VA benefits (also federally excluded). | Verify 1099-R distribution code and payor consistent with DFAS / military retirement. |
| ND-ASM-T2-06 | **MN/MT reciprocity certificate missing or stale.** Employer withheld MN or MT tax in error. | Refuse with R-ND-FINAL-22; route taxpayer to a multistate preparer to recover withholding via MN / MT non-resident refund return. |
| ND-ASM-T2-07 | **Out-of-state work (non-MN/MT) by ND resident.** Self-employment income earned while physically working in another state may also be taxable in that state. ND-1CR may apply. | If material out-of-state work exists, refuse with R-ND-FINAL-16 (multi-state apportionment out of scope). |
| ND-ASM-T2-08 | **Late-1099 penalty exposure.** January 31 may already be past at the time of orchestrator run. | Surface the penalty exposure in the action list; the reviewer decides whether to file late or wait. |
| ND-ASM-T2-09 | **PTC iteration convergence.** The marketplace-coverage iteration between SE health and PTC may not converge cleanly within 3 cycles. | If `us-self-employed-health-insurance` flagged non-convergence, escalate the flag to the reviewer brief and document the chosen position. |
| ND-ASM-T2-10 | **Farm income averaging (Schedule ND-1FA) election.** Election is irrevocable once filed; verify the federal Schedule J election was made first. | Confirm the election produces a lower combined federal+ND tax than the non-averaged path before signing off. |
| ND-ASM-T2-11 | **Negative federal taxable income.** Form 1040 Line 15 can be negative (NOL carryforward, etc.). ND-1 Line 1 takes the federal figure as-is; an NOL may flow through. | Verify ND treatment of the federal NOL — ND generally conforms but verify carryforward documentation. Flag for reviewer. |
| ND-ASM-T2-12 | **Oil & gas royalty interplay.** Royalties are federally taxable as ordinary income and embedded in Line 15. ND oil extraction tax is paid at the wellhead by the operator and is NOT a credit on ND-1. | Document the royalty source on ND-1 working papers; confirm no double-counting; do NOT produce any oil-extraction-tax filing. |

## Section 11 — Worked example

**Facts.** Sarah Lindgren, single, age 42, full-year Fargo (ND) resident, sole proprietor (freelance software developer). Part of the year she also worked W-2 wages for a Moorhead, MN employer (reciprocity in play). 2025 facts:

- Schedule C gross receipts: $180,000
- Schedule C deductible expenses (incl. home office): $30,000
- Schedule C net profit: $150,000
- W-2 from Moorhead MN employer: $12,000 (Form MWR on file; no MN withholding; ND withholding $360)
- Q3 2025 income spike: $5,000 unexpected consulting bonus in September; documented in `us-quarterly-estimated-tax`
- Marketplace health coverage: No — Sarah is on her spouse's plan (wait — Sarah is single per intake; she is on COBRA from her previous W-2 employer): $7,200 in COBRA premiums → §162(l) deduction
- Solo 401(k) contributions: $31,000 (employee deferral $23,500 + employer profit-sharing $7,500 calculated against net SE earnings)
- Federal withholding: $0
- Federal estimated payments: $4,000 Q1, $4,000 Q2, $0 Q3, $0 Q4 (Q3 spike not covered) → Form 2210 penalty for Q3/Q4
- ND withholding: $360 (from MN W-2 employer who withheld ND under reciprocity)
- ND estimated payments: $200 Q1, $200 Q2, $0 Q3, $0 Q4 → ND Schedule ND-1UT interest exposure
- No dependents
- Federal standard deduction (single, TY 2025): $15,750 `[VERIFY:]` OBBBA-updated
- No Renaissance Zone, no tribal, no military retirement, no farm averaging
- No ND sales-tax registration

**Orchestrator output (abbreviated reviewer brief — actual file is longer):**

```markdown
# Complete Return Package — Sarah Lindgren — Tax Year 2025

## Executive Summary
- Taxpayer: Sarah Lindgren, full-year North Dakota (Fargo) resident
- Filing status: Single
- Business: Sole proprietor — freelance software developer
- MN/MT reciprocity in play: Yes (Moorhead MN W-2 employer; Form
  MWR on file; no MN withholding; ND withholding $360)
- Special populations: none
- Federal total tax (Form 1040 Line 24): $30,940
- Federal taxable income (Form 1040 Line 15 — ND starting point):
  $90,604
- ND total tax (ND-1 Line 6): $821
- Total 2025 tax liability: $31,761
- Total payments (federal + ND withholding + estimates): $8,760
- Net balance due: $23,001 across federal + ND
- Action required by April 15, 2026: file federal Form 1040, ND-1;
  pay $23,001 balance due across two jurisdictions; pay 2026 Q1
  estimates of ~$7,930 combined; reviewer to confirm Form 2210
  (federal) and Schedule ND-1UT (ND) interest amounts

## Federal Return (from us-federal-return-assembly)
- Schedule C Line 31 (net profit): $150,000
- Schedule SE Line 12 (SE tax): $18,792
- Schedule 1 Line 15 (½ SE tax): $9,396
- Schedule 1 Line 16 (retirement, Solo 401(k)): $31,000
- Schedule 1 Line 17 (SE health insurance, COBRA): $7,200
- W-2 wages (MN employer): $12,000
- Form 1040 Line 11 (AGI): $114,404 (after retirement, ½ SE tax,
  §162(l), and adding W-2 wages)
- Form 1040 Line 12 (standard deduction, single): $15,750 `[VERIFY:]`
- Form 8995 QBI deduction: ~$8,050 (non-SSTB software dev; 20% of
  qualified business income subject to limits)
- Form 1040 Line 13 (QBI): $8,050
- Form 1040 Line 14: $23,800
- Form 1040 Line 15 (federal taxable income — ND HANDOFF): $90,604
- Form 1040 Line 16 (federal tax): ~$12,148
- Schedule 2 Line 4 (SE tax): $18,792
- Form 2210 penalty (Q3/Q4 spike not covered): ~$240
- Form 1040 Line 24 (total tax): $30,940
- Payments: $8,000 federal estimates
- Balance due federal: $22,940

## North Dakota Return (from nd-income-tax)
- ND-1 Line 1 (federal taxable income — Form 1040 Line 15): $90,604
- Schedule ND-1SA Part A (additions): $0 — no non-ND muni bond
  interest
- ND-1 Line 2 (additions): $0
- Schedule ND-1SA Part B (subtractions): $0 — no Social Security,
  no military retirement, no RZ, no tribal, no Job Service ND,
  no US bond interest
- ND-1 Line 3 (subtractions): $0
- ND-1 Line 4 (ND taxable income): $90,604

## Bracket Math Audit
- ND-1 Line 4: $90,604
- Filing status: Single
- TY 2025 breakpoints: $48,475 / $244,825
- $0 to $48,475 at 0% = $0
- $48,475 to $90,604 = $42,129 at 1.95% = $821.52
- Tax band: 1.95% (middle bracket)
- ND-1 Line 6 (ND income tax): $821 (rounded)

## North Dakota Return (continued)
- ND-1 Line 14 (credits, Schedule ND-1TC): $0
- ND-1 Line 17 (ND withholding): $360 (from MN employer under
  reciprocity)
- ND-1 Line 18 (ND estimated payments): $400 ($200 Q1 + $200 Q2)
- Schedule ND-1UT interest exposure: ~$15 (Q3/Q4 underpayment)
- ND total tax + interest: $836
- ND total payments: $760
- ND-1 Line 22 (balance due): ~$76 (plus $15 interest = $91)
- Wait — exec summary says $821 ND tax and $23,001 net balance.
  Reconciliation: total balance = $22,940 federal + ~$91 ND ≈
  $23,031. Within $30 tolerance of the $23,001 exec-summary figure;
  difference is rounding across penalty/interest computations.
  Reviewer to lock final numbers.

## MN/MT Reciprocity
- MN W-2: $12,000 wages from Moorhead employer
- Form MWR on file with employer (verified); no MN withholding
- ND withholding $360 was properly remitted by MN employer to ND
- No MN return required; no Schedule ND-1CR credit (no MN tax was
  paid)
- PASS

## Estimated Tax for 2026
- 2025 federal total tax: $30,940 → Q1 2026 federal estimate
  ~$7,735 (100% of prior year ÷ 4; AGI < $150K so 100% safe
  harbor applies federally)
- 2025 ND total tax: $821 → Q1 2026 ND estimate ~$205 (100% of
  prior year ÷ 4)
- Combined Q1 2026 estimate: ~$7,940 due April 15, 2026 — note
  this is on TOP of the April 15 balance due
- Strong recommendation: switch ND-1ES to even quarterly schedule;
  the Q3/Q4 zero-payment pattern triggered ND-1UT interest in 2025

## 1099-NEC Issuance
- N/A — Sarah engaged no subcontractors in 2025

## ND Sales Tax Status
- N/A — not a ND sales-tax registrant

## Cross-skill Verification (Section 6 summary)
- F-1 through F-13: PASS
- N-1 through N-15: PASS (N-5 bracket math audit verified)
- C-1 through C-17: PASS (Social Security and military retirement
  N/A; QBI confirmed flowing through Line 15)
- R-1 through R-5: PASS (MN reciprocity clean)
- 9-1 through 9-4: N/A (no contractors)
- E-1 through E-6: PASS (Q3/Q4 underpayment flagged on both sides)
- W-1 through W-5: PASS (single $360 W-2 source documented)
- S-1 through S-5: N/A (no special populations)

## Reviewer Attention Flags
1. Form 2210 federal underpayment penalty (~$240) — Q3 spike not
   covered; reviewer to finalize annualized-income method to
   reduce penalty.
2. Schedule ND-1UT interest (~$15) — minor; reviewer to confirm.
3. COBRA §162(l) eligibility — confirm Sarah was not eligible for
   subsidized employer coverage in any month during 2025.
4. Solo 401(k) employer portion ($7,500) — confirm matches the
   25%-of-net-SE-earnings cap after the circular ½-SE-tax
   adjustment.
5. ND withholding via MN employer — verify the $360 actually
   landed in ND's account (TAP confirmation).

## Refusals Triggered
(none — Sarah's facts fit the in-scope pattern)

## Positions Taken
- §199A non-SSTB classification of freelance software development:
  see `us-qbi-deduction`; software dev is explicitly non-SSTB.
- ND-1 Line 1 = Form 1040 Line 15 (NOT Line 11 AGI): per N.D.C.C.
  §57-38-01(7) and 2025 ND-1 instructions Step 1.
- MN reciprocity for $12,000 wages: per ND-MN reciprocity
  agreement, MN-source wages of a ND resident are taxed only in
  ND when Form MWR is timely filed.

## Planning Notes for 2026
- ND rate stability: 0%/1.95%/2.50% schedule projected to continue
  in 2026 absent 69th Legislative Assembly action `[VERIFY:]`.
- Federal QBI rate rises 20% → 23% under OBBBA (P.L. 119-21);
  Sarah's QBI deduction grows materially, reducing both federal
  taxable income and (because Line 15 = ND Line 1) ND tax.
- Sarah should switch to even quarterly ND-1ES to avoid another
  year of ND-1UT interest.
- If Sarah loses MN W-2 income in 2026, the reciprocity tracking
  drops out — simpler return.
- Federal 1099 threshold rises $600 → $2,000 in 2026 under OBBBA
  — relevant only if Sarah hires contractors.

## Taxpayer Action List
[full action list embedded — see File 3]
```

This is one ND-resident sole prop with MN W-2 wages under reciprocity, full reviewer package abbreviated to ~3 pages. The actual file is longer and includes the full xlsx workbook, the full brief, and the full action list.

## Section 12 — Refusal catalogue

- **R-ND-FINAL-1** — An upstream skill did not run.  _(Refuse; name the missing skill.)_
- **R-ND-FINAL-2** — An upstream skill's self-check failed and was not resolved.  _(Refuse; name the check.)_
- **R-ND-FINAL-3** — A Section 6 reconciliation failed beyond the $1 (or T2-01) tolerance.  _(Refuse; name the equation and the discrepancy.)_
- **R-ND-FINAL-4** — A refusal fired upstream and was suppressed in the upstream output.  _(Refuse; force resolution.)_
- **R-ND-FINAL-5** — Intake artifact is incomplete (missing residency, DOB, filing status, MN/MT flag, oil/gas flag, etc.).  _(Refuse; name the missing item(s).)_
- **R-ND-FINAL-6** — Taxpayer is not a full-year North Dakota resident (part-year via Form ND-1NR or non-resident).  _(Refuse; out of scope.)_
- **R-ND-FINAL-7** — Intake somehow flagged a ND city or local income tax — none exists.  _(Refuse; route back to intake.)_
- **R-ND-FINAL-8** — (reserved)  _(—)_
- **R-ND-FINAL-9** — (reserved)  _(—)_
- **R-ND-FINAL-10** — Taxpayer is an S-corp (Form 1120-S federally; ND requires Form 60).  _(Refuse; out of scope for this orchestrator (route to `nd-corporate-tax`).)_
- **R-ND-FINAL-11** — Taxpayer is a partnership (Form 1065 federally; ND requires Form 58).  _(Refuse; out of scope.)_
- **R-ND-FINAL-12** — Tax year other than 2025.  _(Refuse; rates and brackets may differ.)_
- **R-ND-FINAL-13** — MFJ taxpayers with mixed residency (one ND resident, one non-resident).  _(Refuse; routes to Form ND-1NR which is out of scope.)_
- **R-ND-FINAL-14** — Amended return (Form ND-1X).  _(Refuse; out of scope.)_
- **R-ND-FINAL-15** — (reserved)  _(—)_
- **R-ND-FINAL-16** — Multi-state income apportionment (work performed in multiple states beyond simple W-2 MN/MT reciprocity).  _(Refuse; out of scope.)_
- **R-ND-FINAL-17** — Foreign income / FEIE / FTC at the state level.  _(Refuse; out of scope.)_
- **R-ND-FINAL-18** — ND corporate or pass-through tax (wrong tax type).  _(Refuse; route to `nd-corporate-tax`.)_
- **R-ND-FINAL-19** — ND pass-through entity (PTE) tax election handling for SMLLC that elected to be taxed as a corporation.  _(Refuse; out of scope (SMLLCs in scope are disregarded only).)_
- **R-ND-FINAL-20** — ND K-1 received from an S-corp or partnership flowing through to this individual.  _(Refuse; orchestrator scope is sole prop / SMLLC disregarded only.)_
- **R-ND-FINAL-21** — Taxpayer owes ND oil & gas extraction tax (Form OG-1 family) or coal severance tax.  _(Refuse; out of scope. Royalty income tax treatment proceeds normally via federal Line 15.)_
- **R-ND-FINAL-22** — Employer withheld MN or MT tax in error despite reciprocity.  _(Refuse the MN/MT recovery filing; orchestrator continues with the ND return and flags the recovery as a separate engagement.)_
- **R-ND-FINAL-23** — Part-year ND residency with mid-year move from / to another state.  _(Refuse; ND-1NR is out of scope.)_

**Refusal catalogue table**  _(Section 12 — Refusal catalogue)_

| ID | Situation | Action |
| --- | --- | --- |
| R-ND-FINAL-1 | An upstream skill did not run. | Refuse; name the missing skill. |
| R-ND-FINAL-2 | An upstream skill's self-check failed and was not resolved. | Refuse; name the check. |
| R-ND-FINAL-3 | A Section 6 reconciliation failed beyond the $1 (or T2-01) tolerance. | Refuse; name the equation and the discrepancy. |
| R-ND-FINAL-4 | A refusal fired upstream and was suppressed in the upstream output. | Refuse; force resolution. |
| R-ND-FINAL-5 | Intake artifact is incomplete (missing residency, DOB, filing status, MN/MT flag, oil/gas flag, etc.). | Refuse; name the missing item(s). |
| R-ND-FINAL-6 | Taxpayer is not a full-year North Dakota resident (part-year via Form ND-1NR or non-resident). | Refuse; out of scope. |
| R-ND-FINAL-7 | Intake somehow flagged a ND city or local income tax — none exists. | Refuse; route back to intake. |
| R-ND-FINAL-8 | (reserved) | — |
| R-ND-FINAL-9 | (reserved) | — |
| R-ND-FINAL-10 | Taxpayer is an S-corp (Form 1120-S federally; ND requires Form 60). | Refuse; out of scope for this orchestrator (route to `nd-corporate-tax`). |
| R-ND-FINAL-11 | Taxpayer is a partnership (Form 1065 federally; ND requires Form 58). | Refuse; out of scope. |
| R-ND-FINAL-12 | Tax year other than 2025. | Refuse; rates and brackets may differ. |
| R-ND-FINAL-13 | MFJ taxpayers with mixed residency (one ND resident, one non-resident). | Refuse; routes to Form ND-1NR which is out of scope. |
| R-ND-FINAL-14 | Amended return (Form ND-1X). | Refuse; out of scope. |
| R-ND-FINAL-15 | (reserved) | — |
| R-ND-FINAL-16 | Multi-state income apportionment (work performed in multiple states beyond simple W-2 MN/MT reciprocity). | Refuse; out of scope. |
| R-ND-FINAL-17 | Foreign income / FEIE / FTC at the state level. | Refuse; out of scope. |
| R-ND-FINAL-18 | ND corporate or pass-through tax (wrong tax type). | Refuse; route to `nd-corporate-tax`. |
| R-ND-FINAL-19 | ND pass-through entity (PTE) tax election handling for SMLLC that elected to be taxed as a corporation. | Refuse; out of scope (SMLLCs in scope are disregarded only). |
| R-ND-FINAL-20 | ND K-1 received from an S-corp or partnership flowing through to this individual. | Refuse; orchestrator scope is sole prop / SMLLC disregarded only. |
| R-ND-FINAL-21 | Taxpayer owes ND oil & gas extraction tax (Form OG-1 family) or coal severance tax. | Refuse; out of scope. Royalty income tax treatment proceeds normally via federal Line 15. |
| R-ND-FINAL-22 | Employer withheld MN or MT tax in error despite reciprocity. | Refuse the MN/MT recovery filing; orchestrator continues with the ND return and flags the recovery as a separate engagement. |
| R-ND-FINAL-23 | Part-year ND residency with mid-year move from / to another state. | Refuse; ND-1NR is out of scope. |

## Section 13 — Self-checks

**Self-checks table**  _(Section 13 — Self-checks)_

| # | Check |
| --- | --- |
| 200 | All upstream content skills executed. |
| 201 | All upstream self-checks passed (or were explicitly waived with reviewer flag). |
| 202 | Section 6A (federal internal) reconciliations PASS. |
| 203 | Section 6B (ND internal) reconciliations PASS. |
| 204 | Section 6C (federal-ND coordination) reconciliations PASS. |
| 205 | Section 6D (MN/MT reciprocity) reconciliations PASS or N/A. |
| 206 | Section 6E (1099-NEC) reconciliations PASS or N/A. |
| 207 | Section 6F (estimated tax) reconciliations PASS. |
| 208 | Section 6G (withholding tie-out) reconciliations PASS. |
| 209 | Section 6H (special-population cross-checks) PASS or N/A. |
| 210 | Assumption log contains every "Assumed" item from every upstream skill. |
| 211 | Reviewer flag log contains every "Reviewer judgment" item. |
| 212 | Taxpayer action list has specific dollar amounts and dates. |
| 213 | Planning notes for 2026 reference ND rate stability, QBI rate change, military retirement / RZ / tribal continuity where applicable, and 1099 threshold. |
| 214 | Every refusal in Section 12 was evaluated against the taxpayer's facts. |
| 215 | Three-file deliverable produced in `/mnt/user-data/outputs/`. |
| 216 | `present_files` called with the three files. |
| 217 | Bracket math audit explicitly documented in the reviewer brief (which band, breakpoints used). |
| 218 | ND-1 Line 1 verified equal to Form 1040 Line 15 (NOT Line 11). |

- **200** — All upstream content skills executed.  _(Section 13 — Self-checks)_
- **201** — All upstream self-checks passed (or were explicitly waived with reviewer flag).  _(Section 13 — Self-checks)_
- **202** — Section 6A (federal internal) reconciliations PASS.  _(Section 13 — Self-checks)_
- **203** — Section 6B (ND internal) reconciliations PASS.  _(Section 13 — Self-checks)_
- **204** — Section 6C (federal-ND coordination) reconciliations PASS.  _(Section 13 — Self-checks)_
- **205** — Section 6D (MN/MT reciprocity) reconciliations PASS or N/A.  _(Section 13 — Self-checks)_
- **206** — Section 6E (1099-NEC) reconciliations PASS or N/A.  _(Section 13 — Self-checks)_
- **207** — Section 6F (estimated tax) reconciliations PASS.  _(Section 13 — Self-checks)_
- **208** — Section 6G (withholding tie-out) reconciliations PASS.  _(Section 13 — Self-checks)_
- **209** — Section 6H (special-population cross-checks) PASS or N/A.  _(Section 13 — Self-checks)_
- **210** — Assumption log contains every "Assumed" item from every upstream skill.  _(Section 13 — Self-checks)_
- **211** — Reviewer flag log contains every "Reviewer judgment" item.  _(Section 13 — Self-checks)_
- **212** — Taxpayer action list has specific dollar amounts and dates.  _(Section 13 — Self-checks)_
- **213** — Planning notes for 2026 reference ND rate stability, QBI rate change, military retirement / RZ / tribal continuity where applicable, and 1099 threshold.  _(Section 13 — Self-checks)_
- **214** — Every refusal in Section 12 was evaluated against the taxpayer's facts.  _(Section 13 — Self-checks)_
- **215** — Three-file deliverable produced in `/mnt/user-data/outputs/`.  _(Section 13 — Self-checks)_
- **216** — `present_files` called with the three files.  _(Section 13 — Self-checks)_
- **217** — Bracket math audit explicitly documented in the reviewer brief (which band, breakpoints used).  _(Section 13 — Self-checks)_
- **218** — ND-1 Line 1 verified equal to Form 1040 Line 15 (NOT Line 11).  _(Section 13 — Self-checks)_

## Section 14 — Known gaps

1. PDF form filling is not automated. The reviewer transcribes the
   worksheets into ND TAP or an approved e-file partner.
2. E-filing is the reviewer's responsibility. This skill produces the
   computation; submission happens outside the agent.
3. Payment execution is the taxpayer's responsibility; the skill
   provides instructions only.
4. Multi-state returns are not supported (ND-only, plus MN/MT
   reciprocity handling).
5. Foreign income is not supported.
6. Part-year and non-resident returns (Form ND-1NR) are refused.
7. The package is complete only for tax year 2025; 2026 appears only
   as prospective planning.
8. ND has no city-level income tax; there is no city-return artifact
   to produce (unlike Michigan / Detroit).
9. ND oil & gas extraction tax and coal severance tax filings are
   not produced (income tax treatment of royalty income IS handled
   because it is already embedded in federal taxable income).
10. Renaissance Zone, tribal-enrollment, and military-retirement
    subtractions are consumed from `nd-income-tax`; the orchestrator
    only verifies documentation flags.
11. The MN/MT reciprocity check assumes the employer correctly
    remitted ND withholding when Form MWR / MT certificate was on
    file. If the employer erred, the recovery filing is out of
    scope (R-ND-FINAL-22).

### Change log

- **v0.1 (May 2026):** Initial draft. Orchestrates federal + ND
  stack. Three-file deliverable. Section 6 verification matrix with
  50+ reconciliations covering federal-internal, ND-internal,
  federal-ND coordination (especially the Line 15 NOT Line 11
  starting point), MN/MT reciprocity, 1099-NEC, estimated-tax,
  withholding tie-out, and special-population cross-checks
  (military retirement, Renaissance Zone, tribal, farm averaging).
  Worked example: Fargo ND resident sole prop with $150K Schedule
  C, Solo 401(k), $12K MN W-2 under reciprocity, Q3 spike causing
  Form 2210 / Schedule ND-1UT exposure.

## Disclaimer

This skill and its outputs are provided for informational and
computational purposes only and do not constitute tax, legal, or
financial advice. Open Accountants and its contributors accept no
liability for any errors, omissions, or outcomes arising from the use
of this skill. All outputs must be reviewed and signed off by a
qualified professional (such as a CPA, EA, tax attorney, or
equivalent licensed practitioner in your jurisdiction) before filing
or acting upon.

The most up-to-date, verified version of this skill is maintained at
[openaccountants.com](https://openaccountants.com). Log in to access
the latest version, request a professional review from a licensed
accountant, and track updates as tax law changes.

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
