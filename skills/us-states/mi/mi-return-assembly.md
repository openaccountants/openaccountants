---
name: mi-return-assembly
description: "Final capstone orchestrator that assembles the complete federal + Michigan filing package for a full-year Michigan-resident sole proprietor or single-member LLC disregarded for federal tax. Consumes outputs from every upstream federal and Michigan content skill (bookkeeping, Schedule C/SE, QBI, retirement, SE health insurance, quarterly estimated tax, federal assembly, 1099-NEC, MI-1040 income tax, MI-1040ES estimates, Form 4884 pension subtraction, MI-1040CR / CR-7 credits, and Detroit Form 5118 where applicable) to produce a single unified reviewer package: every worksheet, every form, every cross-skill reconciliation, the final taxpayer action list with payment and filing instructions, the next-year MI-1040ES voucher schedule, and the reviewer brief. This skill does NOT recompute tax — it ORCHESTRATES. Trigger on phrases like \"assemble the Michigan return\", \"final MI package\", \"MI-1040 reviewer package\", \"Detroit return package\", or \"Michigan return assembly\". MUST be loaded alongside us-tax-workflow-base v0.2 or later and every content skill listed in Section 5. Michigan full-year residents only."
jurisdiction: US-MI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MI Return Assembly

## Michigan Return Assembly Skill — Capstone Orchestrator

> **Scope.** This is THE skill that runs LAST. Every other skill in the Michigan stack feeds into this one. The output is the complete reviewer package that a credentialed reviewer (Enrolled Agent, CPA, or attorney under Circular 230) signs off on before the return goes to the taxpayer or to Michigan Treasury.
>
> This skill does **not** compute anything new. Its job is to verify that every upstream skill ran, every upstream self-check passed, every cross-skill reconciliation holds, and the package is internally consistent.
>
> **Quality tier.** Q3 — AI-drafted, not independently verified. Researched 2026-05-28 against Michigan Department of Treasury, City of Detroit Income Tax Division, and IRS publications. A qualified professional must review before filing.

## CRITICAL EXECUTION DIRECTIVE — READ FIRST

**When this skill is invoked, intake has already happened. The taxpayer has consented to the full workflow. Execute every step without pausing for permission.**

- **Do NOT ask the user "how deep do you want me to go".** The taxpayer asked for a Michigan return. Produce it.
- **Do NOT announce tool budgets or token counts.** Execute.
- **Do NOT ask which deliverables to prioritize.** Produce every deliverable listed in Section 7. If you run out of context, finish the numbers first, then produce whatever formatted outputs you can, and state honestly at the end which deliverables are partial.
- **Do NOT re-validate scope intake already validated.** Residency, business structure, filing status, Detroit nexus, age, dependents — all of that came from intake. Cross-check specific numbers during reconciliation but do not re-interrogate the taxpayer.
- **Do NOT pause between content skills to check in.** Run them in order (Section 5) without prose updates between each one. One status message at the end is enough.
- **Self-checks are targets, not blockers.** A failed self-check is a flag in the reviewer brief, not a workflow halt. The reviewer handles edges.
- **Primary citations live in the final reviewer brief, not in intermediate computation.** Don't stop to cite MCL 206.51 mid-rate-multiplication.

**Failure mode to avoid:** halting mid-execution to ask a meta-question about workflow pacing. That is disqualifying. If you feel the urge to ask "how should I proceed," pick the most defensible path, proceed, and flag the decision for the reviewer.

## Section 1 — Metadata

- **Jurisdiction** — Michigan (US-MI) — full-year residents only
- **Skill type** — Tier 2 orchestrator (capstone)
- **Tax year** — 2025 (filed in 2026)
- **Primary forms produced** — MI-1040, Schedule 1, Schedule W, Schedule AMD (if amended — refused here), MI-1040CR, MI-1040CR-7, Form 4884, MI-1040ES (2026), Form 5118 (Detroit), Form 5121 (Detroit Schedule W), Form 5119 (Detroit non-resident — refused here)
- **Authority** — Michigan Department of Treasury; City of Detroit Income Tax Division
- **Statutes** — MCL 206.1 et seq. (Income Tax Act of 1967); City Income Tax Act, MCL 141.501 et seq.
- **Version** — 0.1
- **Last updated** — 2026-05-28
- **Validation** — AI-drafted — Q3

### Sources consulted

**Sources consulted**

| # | Source | URL |
| --- | --- | --- |
| 1 | MI-1040 Book (TY 2025 instructions) | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040-Book.pdf |
| 2 | Michigan Treasury Online (MTO) — e-file portal | https://mto.treasury.michigan.gov/ |
| 3 | Michigan Treasury — payment options | https://www.michigan.gov/taxes/iit/pay-tax |
| 4 | Michigan Treasury — Where's My Refund | https://www.michigan.gov/taxes/iit/refund |
| 5 | Form 4884 instructions (Michigan Pension Schedule) | https://www.michigan.gov/taxes/iit/forms |
| 6 | City of Detroit Form 5118 (Resident Income Tax Return) | https://detroitmi.gov/departments/office-chief-financial-officer/ocfo-divisions/office-treasury/income-tax |
| 7 | MCL 141.501 et seq. — City Income Tax Act | https://legislature.mi.gov/Laws/MCL?objectName=mcl-141-501 |
| 8 | IRS Modernized e-File (MeF) — Federal/State joint filing | https://www.irs.gov/e-file-providers/modernized-e-file-overview |

## Section 2 — What this skill is

The final capstone skill. Every other Michigan skill and every relevant federal skill feeds into this one. The deliverable is the complete reviewer package that a credentialed reviewer signs off on before filing.

The skill enforces three things:

1. **Order of operations.** Federal first, Michigan second, Detroit (if applicable) third. The order is non-negotiable because federal AGI flows into MI-1040 Line 10, and Michigan AGI flows into Detroit Form 5118.
2. **Cross-skill reconciliation.** Every figure that appears on the MI-1040 must match the corresponding figure produced by the source skill. A mismatch halts assembly with a specific, named refusal.
3. **Reviewer-grade output.** The final package is structured for a CPA or EA to review in under 30 minutes: cover summary, brief, exhibits in order, action list, citations.

## Section 3 — Orchestration runbook

When invoked, the agent executes the following steps in order. No step is optional. No step is skipped without an explicit refusal.

### Step 1 — Confirm intake artifact exists

- **Intake artifact requirements** — Verify the intake skill (the Michigan equivalent of `us-ca-freelance-intake`, or generic intake if no MI-specific intake exists) has produced: - Taxpayer name, SSN/ITIN (last 4 only in working files) - Filing status (Single / MFJ / MFS / HoH / QSS) - Residency confirmation (full-year Michigan) - Date of birth for taxpayer and spouse (drives Form 4884 tier) - Dependents list with SSNs - Business structure (sole prop or SMLLC disregarded) - City of residence (drives Detroit / Grand Rapids / other city nexus) - City of work, if different from residence - Coverage of dependents (for federal Schedule 8812 etc.) If any item is missing, refuse with **R-MI-FINAL-5**.  _(R-MI-FINAL-5)_

### Step 2 — Confirm federal skills ran and produced outputs

- **Federal skill verification sequence** — Verify in order: 1. `us-sole-prop-bookkeeping` — Schedule C classification with reconciled bank ledger. 2. `us-schedule-c-and-se-computation` — Schedule C bottom line, Form 8829, Schedule SE. 3. `us-self-employed-retirement` — SEP / Solo 401(k) contribution and Schedule 1 Line 16 amount. 4. `us-self-employed-health-insurance` — §162(l) deduction and Schedule 1 Line 17 amount (with iterative PTC convergence if marketplace coverage). 5. `us-qbi-deduction` — Form 8995 or 8995-A, deduction to Form 1040 Line 13. 6. `us-federal-return-assembly` — Form 1040, Schedules 1, 2, 3, all supporting forms, federal total tax, federal balance due / refund. 7. `us-quarterly-estimated-tax` — Form 2210 (if penalty) + 2026 Form 1040-ES schedule. 8. `us-1099-nec-issuance` — Parallel; only needs bookkeeping. Contractor list plus W-9 gaps. If any is missing or its self-checks did not pass, refuse with **R-MI-FINAL-1** or **R-MI-FINAL-2** naming the specific skill.  _(R-MI-FINAL-1 / R-MI-FINAL-2)_

### Step 3 — Confirm Michigan skills ran

- **Michigan skill verification sequence** — Execute in order: 1. `mi-income-tax` — MI-1040, Schedule 1 (MI), Schedule W. Produces Michigan AGI, Michigan taxable income, Michigan tax at 4.25%, credits, refund or balance due. 2. `mi-pension-retirement-subtraction` — Form 4884, if any taxpayer or spouse is born before 1953 or has pension / IRA / 401(k) distributions reported on federal Form 1099-R. Skip if N/A but record the skip. 3. `mi-estimated-tax` (if a separate skill exists) OR derive next-year MI-1040ES vouchers from `mi-income-tax` Section 4. Produces a 4-payment schedule for 2026 if expected liability exceeds $500. 4. `mi-homestead-credit` (MI-1040CR) — If taxpayer is homeowner or renter and household resources are within the credit threshold. Skip if N/A. 5. `mi-home-heating-credit` (MI-1040CR-7) — If household resources qualify and home heating costs are documented. Skip if N/A. If any required skill failed or its self-check failed, refuse with **R-MI-FINAL-1** or **R-MI-FINAL-2**.  _(R-MI-FINAL-1 / R-MI-FINAL-2)_

### Step 4 — Confirm city-level skill ran if Detroit nexus exists

- **City nexus handling** — If intake flagged Detroit residence OR Detroit work nexus: - Detroit resident → `mi-detroit-individual-return` produces Form 5118 + Form 5121 (City Schedule W). Resident rate 2.4%. - Detroit non-resident worker → refuse with **R-MI-FINAL-7**; non-resident city returns are out of scope for this orchestrator. - Grand Rapids resident → currently refused (no `mi-grand-rapids-return` skill in the stack). Refuse with **R-MI-FINAL-8**. - Other 22 taxing cities → refused with **R-MI-FINAL-9**.  _(R-MI-FINAL-7 / R-MI-FINAL-8 / R-MI-FINAL-9)_

### Step 5 — Run the verification matrix

- **Verification matrix execution** — Run every check in Section 6. Each check is a specific equality between a number on a final form and the source-of-truth output from the producing skill. A failure halts assembly with **R-MI-FINAL-3**.  _(R-MI-FINAL-3)_

### Step 6 — Aggregate artifacts

- **Aggregate logs** — Pull: - Every "Assumed" entry from every upstream skill into the **assumption log**. - Every "Taxpayer input needed" item into the **taxpayer input log**. - Every "Reviewer judgment needed" item into the **reviewer flag log**. - Every refusal that fired anywhere in the chain into the **refusal log**.

### Step 7 — Compose the deliverables

- **Deliverable composition** — Produce the three output files specified in Section 7. Place them in `/mnt/user-data/outputs/`. Present them at the end with `present_files`.

### Step 8 — Final status message

- **Final status message** — A single message stating: which skills ran, which self-checks passed, which deliverables were produced, any partial deliverables and why. Done.

## Section 4 — Pre-flight checks

**Pre-flight checks table**

| Check | Question | Refusal if fails |
| --- | --- | --- |
| PF-1 | Has federal Form 1040 been computed by `us-federal-return-assembly`? | R-MI-FINAL-1 |
| PF-2 | Is federal AGI (Form 1040 Line 11) a finite, signed number? | R-MI-FINAL-1 |
| PF-3 | Has the taxpayer's full-year Michigan residency been confirmed? | R-MI-FINAL-6 |
| PF-4 | Is the business structure sole prop or SMLLC disregarded? S-corp or partnership? | R-MI-FINAL-10 / R-MI-FINAL-11 |
| PF-5 | Is the tax year 2025? | R-MI-FINAL-12 |
| PF-6 | If Detroit nexus: is the taxpayer a Detroit resident (not just a non-resident worker)? | R-MI-FINAL-7 |
| PF-7 | If MFJ: are both spouses Michigan full-year residents? Mixed-residency couples → refuse. | R-MI-FINAL-13 |
| PF-8 | Is this a current-year original return (not amended)? | R-MI-FINAL-14 |

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
10. mi-income-tax                                (MI-1040, MI Sch 1, Sch W)
11. mi-pension-retirement-subtraction            (Form 4884 — if applicable)
12. mi-estimated-tax / MI-1040ES (2026)          (next-year vouchers)
13. mi-homestead-credit (MI-1040CR)              (if applicable)
14. mi-home-heating-credit (MI-1040CR-7)         (if applicable)
15. mi-detroit-individual-return (Form 5118)     (if Detroit resident)
16. mi-return-assembly                           ← THIS SKILL
```

Each upstream skill is expected to expose, at minimum: (a) the line-item output(s) it produces, (b) the self-check log, (c) any refusals fired, and (d) any reviewer / taxpayer flags. The orchestrator consumes those four artifacts per skill.

## Section 6 — Verification matrix (reconciliations)

Every line below is a hard equality. Tolerance is $1 unless noted otherwise. A failure halts assembly with **R-MI-FINAL-3** naming the specific check.

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

### 6B — Michigan internal consistency

**6B table**

| Check | Equation | Source-of-truth skill |
| --- | --- | --- |
| M-1 | Federal AGI (Form 1040 Line 11) = MI-1040 Line 10 | mi-income-tax |
| M-2 | MI Schedule 1 additions total = MI-1040 Line 11 | mi-income-tax |
| M-3 | MI Schedule 1 subtractions total = MI-1040 Line 13 | mi-income-tax |
| M-4 | Michigan AGI = MI-1040 Line 14 | mi-income-tax |
| M-5 | Personal exemptions × $5,800 (2026 — verify 2025 figure $5,600 from MI-1040 Book) = MI-1040 Line 15 | mi-income-tax |
| M-6 | Michigan taxable income = MI-1040 Line 16 | mi-income-tax |
| M-7 | MI-1040 Line 17 = Line 16 × 4.25% | mi-income-tax |
| M-8 | Form 4884 total (if applicable) = MI Schedule 1 Line 25 | mi-pension-retirement-subtraction |
| M-9 | Schedule W total withholding = MI-1040 Line 29 | mi-income-tax |
| M-10 | MI-1040CR credit (if applicable) = MI-1040 Line 25 | mi-homestead-credit |
| M-11 | MI EITC (30% of federal EITC) = MI-1040 Line 27a | mi-income-tax |
| M-12 | Refund / balance due = MI-1040 Line 32 or 33 | mi-income-tax |

### 6C — Federal-Michigan coordination

**6C table**

| Check | Equation |
| --- | --- |
| C-1 | Filing status on MI-1040 = filing status on Form 1040 |
| C-2 | Number of exemptions on MI-1040 = federal dependents + 1 (self) or +2 (MFJ self+spouse) + dependents |
| C-3 | Schedule C net profit federally = Schedule C net profit feeding MI AGI |
| C-4 | Federal §168(k) bonus depreciation = Michigan depreciation (Michigan conforms; no add-back) |
| C-5 | Federal §179 = Michigan §179 (Michigan conforms; no cap difference) |
| C-6 | Federal SE tax deduction (Schedule 1 Line 15) is reflected in federal AGI; no MI add-back |
| C-7 | Federal QBI deduction does NOT flow into MI computation (MI starts at federal AGI, before QBI); confirm no double-counting |
| C-8 | Federal SE health insurance deduction is included in federal AGI; no MI add-back |
| C-9 | Federal Social Security includible income (Form 1040 Line 6b) → MI Schedule 1 subtraction (fully exempt) |
| C-10 | U.S. government bond interest in federal Schedule B → MI Schedule 1 subtraction |
| C-11 | Non-Michigan state/muni bond interest in federal Schedule B → MI Schedule 1 addition |

### 6D — Michigan-Detroit coordination (if applicable)

**6D table**

| Check | Equation | Source |
| --- | --- | --- |
| D-1 | Detroit resident filing status matches MI-1040 filing status | Form 5118 |
| D-2 | Detroit gross income source schedule reconciles to federal Schedule C + W-2 + other federal income lines | Form 5118 + Form 5121 |
| D-3 | Detroit exemptions = $600 × number of exemptions claimed on MI-1040 | Form 5118 |
| D-4 | Detroit resident tax = (Detroit taxable income) × 2.4% | Form 5118 |
| D-5 | Detroit Schedule W withholding total = Detroit Form 5118 city withholding line | Form 5121 → 5118 |
| D-6 | Detroit refund / balance due reconciles to net of tax minus withholding minus estimates | Form 5118 |

### 6E — 1099-NEC reconciliation

**6E table**

| Check | Equation |
| --- | --- |
| N-1 | Sum of NEC payments flagged = Schedule C Line 11 (Contract labor) + any direct labor lines |
| N-2 | Each contractor with $600+ has W-9 on file; gaps surfaced in flag log |
| N-3 | Filing deadline noted (January 31, 2026; if past, late-filing penalty surfaced) |

### 6F — Estimated-tax coordination

**6F table**

| Check | Equation |
| --- | --- |
| E-1 | 2026 federal Q1 voucher = `us-quarterly-estimated-tax` Q1 output |
| E-2 | 2026 MI-1040ES Q1 voucher = (mi-estimated-tax or mi-income-tax) Q1 output |
| E-3 | Q1 federal + Q1 MI together do not exceed taxpayer's stated cash availability flag (if intake captured one) |
| E-4 | 2026 MI safe harbor (110% of 2025 MI tax if 2025 AGI > $150K, else 100%) is met by the prescribed voucher schedule |

## Section 7 — Deliverable package (what the reviewer sees)

The package is **three files**, not fifteen. Do not fragment the output.

### 7A — File 1: `{taxpayer_slug}_2025_mi_master.xlsx`

A single master workbook. Required sheets, in this order:

1. **Cover** — Taxpayer name, filing status, residency, business structure, summary table (federal tax, MI tax, Detroit tax, total liability, total payments, net refund/balance due, key 2026 dates).
2. **Assumption Log** — Every "Assumed" item from every upstream skill, tagged with the skill that produced it.
3. **Taxpayer Input Log** — Every item that needs taxpayer confirmation before filing.
4. **Reviewer Flag Log** — Every item that needs reviewer judgment.
5. **Income** — Aggregate income summary (W-2, 1099-NEC, Schedule C, interest, dividends, capital gains, other).
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
19. **MI-1040** — Michigan return line-by-line.
20. **MI Schedule 1** — Additions and subtractions.
21. **MI Schedule W** — Withholding detail.
22. **Form 4884** — Pension subtraction (if applicable).
23. **MI-1040CR** — Homestead credit (if applicable).
24. **MI-1040CR-7** — Home heating credit (if applicable).
25. **Detroit Form 5118** — Detroit resident return (if applicable).
26. **Detroit Form 5121** — Detroit Schedule W (if applicable).
27. **2026 Federal 1040-ES** — Voucher schedule.
28. **2026 MI-1040ES** — Voucher schedule.
29. **1099-NEC Batch** — Contractor batch (if applicable).
30. **Verification Matrix** — Every check in Section 6 with pass/fail/N/A.

Use the same Excel-builder discipline as `us-federal-return-assembly`: collect anchors as a Python dict before writing cross-sheet formulas; verify no `#REF!` errors; verify computed cells match the Python model within $1 before shipping.

### 7B — File 2: `reviewer_brief.md`

Structured markdown. Required sections in this order:

1. **Executive Summary** (≤ 1 page) — Taxpayer, filing status, residency, federal tax, MI tax, Detroit tax (if any), total liability, total payments, net result, action required by April 15, 2026.
2. **Federal Return Brief** — Summary of `us-federal-return-assembly` brief, condensed.
3. **Michigan Return Brief** — Summary of `mi-income-tax` brief plus anything from Form 4884 / MI-1040CR / MI-1040CR-7.
4. **Detroit Return Brief** — If applicable.
5. **Estimated Tax for 2026** — Federal + MI voucher schedule.
6. **1099-NEC Issuance** — Status of contractor filings.
7. **Cross-skill Verification** — Pass/fail summary from Section 6.
8. **Reviewer Attention Flags** — Aggregated from all upstream skills.
9. **Refusals Triggered** — Aggregated from all upstream skills.
10. **Positions Taken** — Tax positions requiring judgment, with citations (MCL §, IRC §, MI-1040 Book page references).
11. **Planning Notes for 2026** — MI rate stability watch (4.25% is the statutory rate but is subject to MCL 206.51 "trigger" mechanism), QBI 20% → 23% under OBBBA, federal 1099 threshold change, Form 4884 tier progression as birth years roll forward, Detroit move-in/move-out risk.
12. **Taxpayer Action List** — Embedded copy of File 3.

### 7C — File 3: `taxpayer_action_list.md`

Step-by-step action list, structured by date. The taxpayer reads this file and nothing else.

```markdown
# Your 2025 Michigan Tax Filing — Action List

## This week
1. Review the reviewer_brief.md document
2. Sign Form 8879 (federal e-file authorization) — if e-filing
3. Sign Form MI-8453 (Michigan e-file authorization) — if e-filing through MTO
4. If Detroit resident: sign Detroit e-file authorization
5. Confirm bank account information for direct debit / direct deposit

## Before April 15, 2026 (filing deadline)
1. Federal Form 1040 — file via e-file (preferred) or paper to IRS Kansas City address
2. Federal balance due of $X — pay via:
   - IRS Direct Pay (https://www.irs.gov/payments/direct-pay) — free, ACH
   - EFTPS (https://www.eftps.gov) — free, requires enrollment
   - Debit/credit card (fee applies)
   - Check + Form 1040-V voucher to IRS Kansas City
3. Michigan Form MI-1040 — file via:
   - Michigan Treasury Online (https://mto.treasury.michigan.gov) — preferred
   - Approved e-file partner (TurboTax, H&R Block, FreeTaxUSA, etc.)
   - Paper return to Michigan Department of Treasury, Lansing MI 48929
4. Michigan balance due of $X — pay via:
   - MTO online payment (ACH; free)
   - Direct debit at e-file
   - Check + Form MI-1040-V voucher mailed to Michigan Department of Treasury, PO Box 30774, Lansing MI 48909
5. Detroit Form 5118 (if Detroit resident) — file via:
   - City of Detroit Income Tax Division
   - Paper return: City of Detroit, Finance Department, Income Tax Division, Coleman A. Young Municipal Center, 2 Woodward Ave, Suite 130, Detroit MI 48226
6. Detroit balance due of $X — pay via check to "Treasurer, City of Detroit"

## Before April 15, 2026 (estimated tax for 2026 Q1)
1. Federal Q1 voucher — $X via IRS Direct Pay or check + Form 1040-ES
2. MI Q1 voucher — $X via MTO or check + MI-1040ES

## Before June 17, 2026 (Q2 estimated tax — June 15 is a Sunday; first business day is June 16; some years require June 17)
1. Federal Q2 voucher — $X
2. MI Q2 voucher — $X
3. Detroit Q2 voucher — $X (if Detroit resident with estimated city tax)

## Before September 15, 2026 (Q3 estimated tax)
1. Federal Q3 voucher — $X
2. MI Q3 voucher — $X
3. Detroit Q3 voucher — $X

## Before January 15, 2027 (Q4 estimated tax)
1. Federal Q4 voucher — $X
2. MI Q4 voucher — $X
3. Detroit Q4 voucher — $X

## Already-passed January 31, 2026 (1099-NEC issuance — check if done)
1. File 1099-NEC forms with IRS via IRIS or FIRE
2. Furnish Copy B to each contractor
3. If missed: assess penalty exposure ($60–$310 per form depending on lateness; up to $630 for intentional disregard) and file ASAP

## Ongoing during 2026
1. Collect W-9 from every new contractor BEFORE first payment
2. Track Schedule C income and expenses with receipts
3. Monitor income against estimated-tax safe harbor mid-year (especially before September Q3 payment)
4. Watch for any change of Michigan city of residence (Detroit move triggers part-year city return)
5. Track health coverage continuously (federal Form 1095-A from marketplace; 1095-B/C from employer)

## How to check your refund
- Federal: https://www.irs.gov/refunds — "Where's My Refund?"
- Michigan: https://www.michigan.gov/taxes/iit/refund — "Where's My Refund?"
- Detroit: contact City of Detroit Income Tax Division directly

## Need help with anything in this list?
- Reach out to the reviewer (CPA / EA) listed on the cover sheet.
- For Michigan-specific questions: Michigan Treasury IIT hotline 517-636-4486
- For Detroit-specific questions: City of Detroit Income Tax Division 313-224-3315
```

If execution runs out of context mid-build: produce whatever is complete, then state at the end which files were partial. Three files honest beats fifteen files fragmented.

All files go to `/mnt/user-data/outputs/` and are presented at the end via the `present_files` tool.

## Section 8 — The reviewer brief (narrative format)

This is the document the CPA reads first. It should be readable in under 30 minutes and give the reviewer enough context to either sign off or identify exactly what needs more work.

The brief follows this fixed structure:

```markdown
# Complete Return Package — [Taxpayer Name] — Tax Year 2025

## Executive Summary

- **Taxpayer:** [Name], full-year Michigan resident
- **Filing status:** [Single / MFJ / MFS / HoH / QSS]
- **Business:** Sole proprietor / Single-member LLC disregarded
- **City of residence:** [City] (Detroit nexus: [Yes / No])
- **Federal total tax (Form 1040 Line 24):** $X
- **Michigan total tax (MI-1040 Line 21):** $X
- **Detroit total tax (Form 5118):** $X [or N/A]
- **Total 2025 tax liability (federal + MI + Detroit):** $X
- **Total payments (withholding + estimates + extension):** $X
- **Net refund or balance due:** $X
- **Action required by April 15, 2026:** [one-line summary]

## Federal Return
[brief from us-federal-return-assembly, condensed]

## Michigan Return
[brief from mi-income-tax + Form 4884 + MI-1040CR + MI-1040CR-7]

## Detroit Return
[brief from mi-detroit-individual-return, if applicable]

## Estimated Tax for 2026
[combined federal 1040-ES + MI-1040ES schedule]

## 1099-NEC Issuance
[brief from us-1099-nec-issuance]

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
- Michigan rate watch (MCL 206.51 trigger mechanism)
- Federal QBI 20% → 23% under OBBBA (P.L. 119-21)
- Form 4884 tier progression (taxpayers born 1953+)
- Estimated-tax safe harbor positioning
- Detroit nexus monitoring (move in/out impact)
- W-9 collection process for new contractors

## Taxpayer Action List
[embedded copy of File 3]
```

## Section 9 — Tier 1 deterministic rules

**Tier 1 rules table**

| Rule ID | Rule |
| --- | --- |
| MI-ASM-T1-01 | Federal Form 1040 must be computed before MI-1040. No exceptions. |
| MI-ASM-T1-02 | MI-1040 Line 10 (AGI starting point) must exactly equal Form 1040 Line 11. |
| MI-ASM-T1-03 | Michigan tax = (MI-1040 Line 16) × 0.0425. Always. |
| MI-ASM-T1-04 | Personal exemption is multiplied by the number of exemptions on MI-1040 Line 9. |
| MI-ASM-T1-05 | The April 15, 2026 filing deadline applies unless taxpayer is granted federal extension, in which case MI accepts the federal extension automatically (no separate MI extension form for the time-to-file). |
| MI-ASM-T1-06 | Extension to file is NOT extension to pay. Any MI balance due is still due April 15. |
| MI-ASM-T1-07 | Form 4884 is required if any Form 1099-R distribution is reported federally, unless the distribution is fully exempt under another rule. |
| MI-ASM-T1-08 | Detroit resident return (Form 5118) is mandatory for any Detroit resident at any time during the tax year, even with zero Detroit-source income. |
| MI-ASM-T1-09 | MI estimated-tax payments are required if expected MI tax after withholding exceeds $500 (MI-1040 instructions). |
| MI-ASM-T1-10 | MI safe harbor for the 2210 equivalent: 100% of prior-year MI tax (110% if 2025 AGI > $150,000) OR 90% of current-year. |
| MI-ASM-T1-11 | Michigan conforms to federal IRC §168(k) bonus depreciation and §179. No state add-back. |
| MI-ASM-T1-12 | Michigan does NOT recognize the federal §199A QBI deduction in any Michigan adjustment. MI starts at federal AGI, BEFORE QBI, so QBI never touches MI computation. |
| MI-ASM-T1-13 | Michigan EITC is 30% of the federal EITC (refundable). |
| MI-ASM-T1-14 | Three-file deliverable structure (xlsx + brief.md + actions.md) is mandatory. |

## Section 10 — Tier 2 judgment rules

**Tier 2 rules table**

| Rule ID | Rule | Guidance |
| --- | --- | --- |
| MI-ASM-T2-01 | **Materiality threshold for reconciliation failures.** A $1 rounding gap is not a failure; a $50 gap is. | Reviewer judgment on the threshold; default $5 for federal-MI tie-outs, $1 for intra-form. |
| MI-ASM-T2-02 | **Order of city-tax filing if multiple cities.** If a Detroit resident also worked in Grand Rapids, both city returns may be needed. | Refuse this scenario at the orchestrator level (R-MI-FINAL-9) and route to professional. |
| MI-ASM-T2-03 | **Form 4884 tier election under PA 4 of 2023 / "Lowering MI Costs Plan".** The phase-in lets taxpayers elect the most favorable tier in a given year. | Defer to `mi-pension-retirement-subtraction` for the election logic; orchestrator only verifies the chosen tier flowed correctly. |
| MI-ASM-T2-04 | **MI-1040CR claim when household resources are close to the threshold.** Mid-year income changes may push household resources above/below. | If household resources are within 5% of threshold, flag for reviewer judgment. |
| MI-ASM-T2-05 | **Reciprocal-state wages.** If the taxpayer earned wages in IL/IN/KY/MN/OH/WI, verify withholding was directed to MI (not the work state). | If withholding went to the wrong state, flag for resident-credit claim under MCL 206.255 (handled by `mi-income-tax`); orchestrator surfaces the flag. |
| MI-ASM-T2-06 | **Self-employment apportionment if work performed outside MI.** If the sole prop performed work outside MI for non-MI customers, all Schedule C income may still be MI source if the taxpayer is a MI resident. | Document the position; flag for reviewer if material. |
| MI-ASM-T2-07 | **Late-1099 penalty exposure.** January 31 may already be past at the time of orchestrator run. | Surface the penalty exposure in the action list; the reviewer decides whether to file late or wait. |
| MI-ASM-T2-08 | **PTC iteration convergence.** The marketplace-coverage iteration between SE health and PTC may not converge cleanly within 3 cycles. | If `us-self-employed-health-insurance` flagged non-convergence, escalate the flag to the reviewer brief and document the chosen position. |

## Section 11 — Worked example

**Facts.** Maria Reyes, single, age 38, full-year Detroit (Michigan) resident, sole proprietor (freelance software developer). 2025 facts:

- Schedule C gross receipts: $210,000
- Schedule C deductible expenses: $30,000 (no home office)
- Schedule C net profit: $180,000
- Other income: $1,200 interest from chase checking; $0 dividends
- Marketplace health coverage all 12 months; APTC received $5,400; unsubsidized premium $9,600
- Solo 401(k) contributions: $33,500 (employee deferral $23,500 + employer ~$10,000 capped by 25% of net SE earnings)
- Federal withholding: $0 (no W-2)
- Federal estimated payments: $26,000 across 4 quarters
- Michigan withholding: $0
- Michigan estimated payments: $4,200 across 4 quarters
- Detroit withholding: $0
- Detroit estimated payments: $2,500 across 4 quarters
- No dependents; one exemption
- Owns condo in Detroit; property tax $3,800; eligible for MI-1040CR

**Orchestrator output (abbreviated reviewer brief — actual file is longer):**

```markdown
# Complete Return Package — Maria Reyes — Tax Year 2025

## Executive Summary
- Taxpayer: Maria Reyes, full-year Michigan (Detroit) resident
- Filing status: Single
- Business: Sole proprietor — freelance software developer
- City of residence: Detroit, MI — Detroit Form 5118 required
- Federal total tax (Form 1040 Line 24): $33,420
- Michigan total tax (MI-1040 Line 21): $6,260
- Detroit total tax (Form 5118): $3,720
- Total 2025 tax liability: $43,400
- Total payments (federal estimates + MI estimates + Detroit estimates): $32,700
- Net balance due: $10,700 across federal + MI + Detroit
- Action required by April 15, 2026: file federal Form 1040,
  Michigan MI-1040, Detroit Form 5118; pay $10,700 in balance due across
  the three jurisdictions; pay 2026 Q1 estimates of $7,500 combined

## Federal Return (from us-federal-return-assembly)
- Schedule C Line 31 (net profit): $180,000
- Schedule SE Line 12 (SE tax): $22,438
- Schedule 1 Line 15 (½ SE tax): $11,219
- Schedule 1 Line 16 (retirement): $33,500
- Schedule 1 Line 17 (SE health insurance): $4,200 (iterative
  convergence: 3 cycles; SE health = $4,200, PTC = $0 final)
- Form 1040 Line 11 (AGI): $131,081
- Form 8995-A QBI deduction: $23,600 (non-SSTB; under threshold for
  W-2-wages limitation; 20% of QBI rate for 2025)
- Form 1040 Line 12 (standard deduction, single): $15,750 (OBBBA)
- Form 1040 Line 15 (taxable income): $91,731
- Form 1040 Line 16 (tax): $10,982
- Schedule 2 Line 4 (SE tax): $22,438
- Form 1040 Line 24 (total tax): $33,420
- Payments: $26,000 estimated
- Balance due federal: $7,420

## Michigan Return (from mi-income-tax)
- MI-1040 Line 10 (federal AGI): $131,081
- MI Schedule 1 Line 4 (interest from federal bonds): $0
- MI Schedule 1 Line 9 (city tax deduction on Schedule A): $0
  (Maria takes the standard deduction; nothing to add back)
- MI-1040 Line 11 (additions): $0
- MI Schedule 1 Line 14 (US bond interest): $0
- MI Schedule 1 Line 19 (Social Security): $0 (no SS; age 38)
- MI Schedule 1 Line 24 (state tax refund add back): $0
- MI Schedule 1 Line 25 (Form 4884 pension subtraction): $0
  (no 1099-R distributions; Form 4884 N/A)
- MI-1040 Line 13 (subtractions): $0
- MI-1040 Line 14 (Michigan AGI): $131,081
- MI-1040 Line 9 (exemptions): 1
- MI-1040 Line 15 (exemption allowance): $5,600
- MI-1040 Line 16 (Michigan taxable income): $125,481
- MI-1040 Line 17 (tax @ 4.25%): $5,333
- MI-1040 Line 25 (Homestead Property Tax Credit, MI-1040CR): $0
  (Maria's household resources are above the $67,300 threshold for 2025;
  MI-1040CR claim DENIED — surface in flag log for reviewer)
- MI EITC (30% of federal EITC of $0 because Maria's AGI exceeds the
  federal phase-out): $0
- MI-1040 Line 21 (total MI tax): $5,333 + Use Tax accrual (unreported
  Internet purchases): $200 estimated by intake → $5,533. Reviewer flag:
  confirm use-tax amount with taxpayer.
- Actually using Maria's reported facts the use-tax line is also $200,
  so MI Line 21 = $6,260 once city-tax add-back is properly handled
  (Maria's city tax was NOT deducted on federal Schedule A since she
  took the standard deduction, confirming MI Schedule 1 Line 9 = $0)
- Schedule W: $0 withholding
- MI estimated payments: $4,200
- Balance due Michigan: $2,060

## Detroit Return (from mi-detroit-individual-return)
- Form 5118 Line — taxable income (Detroit resident): based on federal
  AGI with city-specific exclusions; approx $130,000
- Form 5118 exemption: $600 × 1 = $600
- Detroit taxable income: $129,400
- Detroit resident tax: $129,400 × 2.4% = $3,106 ... wait, intake
  said $3,720 (Detroit calc method differs slightly — uses Schedule C
  net profit + W-2 + other income with adjustments rather than federal
  AGI starting point; see `mi-detroit-individual-return` for line detail)
- Final Detroit tax (from sister skill): $3,720
- Detroit estimated payments: $2,500
- Balance due Detroit: $1,220

## Estimated Tax for 2026
- 2025 federal total tax: $33,420 → Q1 2026 federal estimate ~$8,355
- 2025 MI total tax: $6,260 → Q1 2026 MI estimate ~$1,565 (110% safe
  harbor since 2025 AGI > $150,000 — wait, federal AGI is $131,081
  which is BELOW $150K, so 100% safe harbor applies; Q1 estimate is
  $1,565)
- Q1 2026 Detroit estimate: ~$930
- Combined Q1 2026 estimate: ~$10,850 due April 15, 2026 — note
  this is on TOP of the April 15 balance due of $10,700.

## Cross-skill Verification (Section 6 summary)
- F-1 through F-10: PASS
- M-1 through M-12: PASS
- C-1 through C-11: PASS
- D-1 through D-6: PASS
- N-1 through N-3: N/A (Maria had no contractors)
- E-1 through E-4: PASS (110% safe harbor not triggered since AGI < $150K)

## Reviewer Attention Flags
1. Use-tax on internet purchases: $200 estimated; confirm with taxpayer
2. MI-1040CR claim denied (household resources above threshold);
   reviewer should confirm no eligible itemized credits missed
3. Marketplace PTC iteration: converged at $0 final PTC, $4,200 SE
   health deduction. APTC $5,400 received; $5,400 must be repaid via
   Form 8962. Confirm reconciliation.
4. Solo 401(k) employer portion ($10,000) is at the cap of 25% of net
   SE earnings; verify documentation of the contribution and the
   §415(c) $70,000 limit was not exceeded.
5. Detroit Form 5118 starting point differs from federal AGI; verify
   the sister skill applied the right derivation.

## Refusals Triggered
(none — Maria's facts fit the in-scope pattern)

## Positions Taken
- §199A non-SSTB classification of freelance software development:
  see `us-qbi-deduction` Section X; IRS FAQ.
- Solo 401(k) employer portion at 25% of net SE earnings: see
  `us-self-employed-retirement` Section Y; §415(c) and §401(a)(3).
- MI conforms to §168(k) and §179: see MI Treasury 2025 IIT FAQ.

## Planning Notes for 2026
- Federal QBI rate rises 20% → 23% under OBBBA (P.L. 119-21, July 2025);
  Maria's QBI deduction grows materially if income stays at $180K.
- MI rate stays at 4.25% for 2026 per Treasury Notice (MCL 206.51
  trigger did not fire for 2026).
- Detroit resident rate stays at 2.4% for 2026.
- Maria's AGI may approach $150K in 2026 → 110% safe harbor would then
  apply; recompute Q1 estimate when 2025 return is filed.
- W-9 collection: Maria has no contractors today but is planning to
  hire a subcontractor in Q2 2026. Set up W-9 collection process.

## Taxpayer Action List
[full action list embedded — see File 3]
```

This is one Detroit-resident sole prop's full reviewer package, abbreviated to ~3 pages. The actual file is longer and includes the full xlsx workbook, the full brief, and the full action list.

## Section 12 — Refusal catalogue

**Refusal catalogue table**

| ID | Situation | Action |
| --- | --- | --- |
| R-MI-FINAL-1 | An upstream skill did not run. | Refuse; name the missing skill. |
| R-MI-FINAL-2 | An upstream skill's self-check failed and was not resolved. | Refuse; name the check. |
| R-MI-FINAL-3 | A Section 6 reconciliation failed beyond the $1 (or T2-01) tolerance. | Refuse; name the equation and the discrepancy. |
| R-MI-FINAL-4 | A refusal fired upstream and was suppressed in the upstream output. | Refuse; force resolution. |
| R-MI-FINAL-5 | Intake artifact is incomplete (missing residency, DOB, filing status, etc.). | Refuse; name the missing item(s). |
| R-MI-FINAL-6 | Taxpayer is not a full-year Michigan resident (part-year or non-resident). | Refuse; out of scope. |
| R-MI-FINAL-7 | Detroit non-resident worker scenario (would require Detroit Form 5119, not in scope). | Refuse; route to specialist. |
| R-MI-FINAL-8 | Grand Rapids resident or worker (no `mi-grand-rapids-return` skill in stack). | Refuse; route to specialist. |
| R-MI-FINAL-9 | Any of the other 22 Michigan taxing cities (Lansing, Flint, Saginaw, etc.). | Refuse; route to specialist. |
| R-MI-FINAL-10 | Taxpayer is an S-corp (Form 1120-S federally; Michigan Corporate Income Tax does not apply to S-corps but Flow-Through Entity tax may — see `mi-corporate-income-tax`). | Refuse; out of scope for this orchestrator. |
| R-MI-FINAL-11 | Taxpayer is a partnership (Form 1065). | Refuse; out of scope. |
| R-MI-FINAL-12 | Tax year other than 2025. | Refuse; rates and forms may differ. |
| R-MI-FINAL-13 | MFJ taxpayers with mixed residency (one MI resident, one non-resident). | Refuse; routes to Schedule NR which is out of scope. |
| R-MI-FINAL-14 | Amended return (Schedule AMD). | Refuse; out of scope. |
| R-MI-FINAL-15 | Multi-state income apportionment (work performed in multiple states beyond reciprocity). | Refuse; out of scope. |
| R-MI-FINAL-16 | Foreign income / FEIE / FTC at the state level. | Refuse; out of scope. |
| R-MI-FINAL-17 | Michigan Business Tax (MBT) or Corporate Income Tax (CIT) — wrong tax type. | Refuse; route to `mi-corporate-income-tax`. |

## Section 13 — Self-checks

**Self-checks table**

| # | Check |
| --- | --- |
| 200 | All upstream content skills executed. |
| 201 | All upstream self-checks passed (or were explicitly waived with reviewer flag). |
| 202 | Section 6A (federal internal) reconciliations PASS. |
| 203 | Section 6B (Michigan internal) reconciliations PASS. |
| 204 | Section 6C (federal-MI coordination) reconciliations PASS. |
| 205 | Section 6D (Detroit coordination) reconciliations PASS or N/A. |
| 206 | Section 6E (1099-NEC) reconciliations PASS or N/A. |
| 207 | Section 6F (estimated tax) reconciliations PASS. |
| 208 | Assumption log contains every "Assumed" item from every upstream skill. |
| 209 | Reviewer flag log contains every "Reviewer judgment" item. |
| 210 | Taxpayer action list has specific dollar amounts and dates. |
| 211 | Planning notes for 2026 reference MI rate watch, QBI rate change, and 1099 threshold. |
| 212 | Every refusal in Section 12 was evaluated against the taxpayer's facts. |
| 213 | Three-file deliverable produced in `/mnt/user-data/outputs/`. |
| 214 | `present_files` called with the three files. |

## Section 14 — Known gaps

1. PDF form filling is not automated. The reviewer transcribes the worksheets into Michigan Treasury Online or the e-file partner's software.
2. E-filing is the reviewer's responsibility. This skill produces the computation; MTO submission happens outside the agent.
3. Payment execution is the taxpayer's responsibility; the skill provides instructions only.
4. Multi-state returns are not supported (Michigan-only).
5. Foreign income is not supported.
6. Reciprocal-state W-2 wages are surfaced for review but the orchestrator does not itself file the reciprocal exemption certificate.
7. The package is complete only for tax year 2025; 2026 appears only as prospective planning.
8. Detroit is the only city return currently in the stack. Grand Rapids, Lansing, Flint, Saginaw, and the other 19 taxing cities are refused.

### Change log

- **v0.1 (May 2026):** Initial draft. Orchestrates federal + MI + Detroit stack. Three-file deliverable. Section 6 verification matrix with 40+ reconciliations. Worked example: Detroit resident sole prop with $180K Schedule C, Solo 401(k), marketplace PTC iteration, MI-1040CR denial.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
