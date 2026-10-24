---
name: au-return-assembly
description: Final orchestrator skill that assembles the complete Australian filing package for Australian-resident sole traders. Consumes outputs from all Australian content skills (australia-gst for BAS, au-individual-return for ITR, au-super-guarantee for voluntary contributions, au-medicare-levy for levy and surcharge, au-payg-instalments for instalment schedule) to produce a single unified reviewer package containing every worksheet, every form, every brief section, all cross-skill reconciliations, and the final action list with payment instructions, filing instructions, and next-year planning. This is the capstone skill that runs last and produces the final deliverable. MUST be loaded alongside all Australian content skills listed above. Australian full-year residents only. Sole traders only.
version: 0.5
jurisdiction: AU
tax_year: 2025
last_updated: 2026-10-21
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Return Assembly

## AU Return Assembly

## AU Return Assembly

## Australia Return Assembly Skill v0.5

Australia Return Assembly Skill v0.5

## CRITICAL EXECUTION DIRECTIVE -- READ FIRST

**When this skill is invoked, you have already passed through intake. The user has consented to the full workflow. Execute all steps without pausing for permission.**

Specifically:

- **Do NOT ask the user "how deep do you want me to go"** or "do you want the full package" or any variant. The user asked for their tax returns. They want their tax returns. Produce them.
- **Do NOT announce how many tokens or tool calls this will take.** Execute.
- **Do NOT ask which deliverables to prioritise.** Produce all deliverables listed in Section 4. If you run out of context mid-execution, finish the computation work first (numbers, positions, flags) then produce whatever formatted outputs you can, and at the very end state clearly which deliverables were not produced and why.
- **Do NOT re-validate scope that intake already validated.** If `au-freelance-intake` produced an intake package, trust it. You can cross-check specific numbers during reconciliation but do not re-interrogate the user about residency, business structure, or anything else intake already captured.
- **Do NOT pause between content skills to check in.** Run them in dependency order (Section 2) without prose status updates between each one. A single status message at the end is fine.
- **Completion gate:** Resolve failed calculation checks, unsupported years and omitted taxable items before issuing a final taxable-income, refund or payable figure. Continue unaffected working papers and label the package incomplete while those matters remain open.
- **Primary source citations go in the final reviewer brief, not in intermediate computation steps.**

**The user has already been told (by the intake skill) that the final package requires registered tax agent signoff before lodging. State it once in the final output and move on.**

**Failure mode to avoid:** The skill halts mid-execution and asks the user a meta-question about workflow pacing. If you feel the urge to ask "how should I proceed," the correct action is to pick the most defensible path and proceed, flagging the decision in the reviewer brief so the reviewer can challenge it.

## What this file is

The final capstone skill for Australian sole trader returns. Every Australian content skill feeds into this one. The output is the complete reviewer package that a registered tax agent can review, sign off on, and deliver to the client along with lodgement instructions.

This skill coordinates execution of the content skills, verifies cross-skill consistency, and assembles the final deliverable.

## Section 1 -- Scope

- **Scope of package** — Produces the complete Australian filing package for: Full-year Australian residents; Sole traders; Tax year 2025-26 (1 July 2025 - 30 June 2026); Lodging BAS (if GST registered), individual tax return (ITR), super reconciliation, Medicare levy calculation, PAYG instalment schedule (Full-year Australian residents; Sole traders; Tax year 2025-26)  _(Section 1 -- Scope)_

## Required year

- **Required year** — This assembly supports 2025–26. Match the intake year and every upstream output before computing. Keep later-year planning separate. The former 2024–25 MLS base thresholds were $97,000/$194,000; those historical figures must not be substituted for the 2025–26 thresholds.  _([ATO MLS income and rates](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy-surcharge/medicare-levy-surcharge-income-thresholds-and-rates))_

## Section 2 -- Execution order and dependency chain

1. **Run australia-gst first:** Prepare or verify the 2025–26 BAS and reconcile its sales to the income-tax ledger. Output the completed labels, GST position, accounting basis and reconciling items. Require supported calculations for the requested year.
2. **Run au-individual-return second:** Prepare the 2025–26 ITR and business schedule from the reconciled ledger. Deduct only the GST credits to which the taxpayer is entitled when determining deductible expenses. Hold final totals until the super reconciliation and all required schedules are complete.
3. **Run au-super-guarantee third:** Use its explicit 2025–26 reconciliation branch and $30,000 standard cap plus eligible carry-forward amounts. Reconcile fund receipts and valid acknowledged notices. Feed personal deductions back into the ITR before calculating Medicare, HELP and final tax.
4. **Run au-medicare-levy fourth:** Use the completed 2025–26 ITR, spouse/dependent details and cover evidence. Calculate the levy, reductions, exemptions and surcharge using their separate income measures. Require supported calculations for the requested year.
5. **Run au-payg-instalments-2 fifth:** Reconcile the 2025–26 instalment credit against the ATO account and notices. Show any 2026–27 forecast separately; the actual notice determines the method, rate, amount and dates.

- **Upstream failure handling:** Require every calculation output to identify 2025–26, its inputs, evidence and unresolved items. An unsupported year, unavailable module or unvalidated amount blocks final totals. Do not substitute an unverified calculation; prepare only the unaffected working papers until the missing amount is resolved.

0. **Run australia-gst first** — Prepare or verify the 2025–26 BAS and reconcile its sales to the income-tax ledger. Output the completed labels, GST position, accounting basis and reconciling items. Require supported calculations for the requested year.
0. **Run au-individual-return second** — Prepare the 2025–26 ITR and business schedule from the reconciled ledger. Deduct only the GST credits to which the taxpayer is entitled when determining deductible expenses. Hold final totals until the super reconciliation and all required schedules are complete.
0. **Run au-super-guarantee third** — Use its explicit 2025–26 reconciliation branch and $30,000 standard cap plus eligible carry-forward amounts. Reconcile fund receipts and valid acknowledged notices. Feed personal deductions back into the ITR before calculating Medicare, HELP and final tax.
0. **Run au-medicare-levy fourth** — Use the completed 2025–26 ITR, spouse/dependent details and cover evidence. Calculate the levy, reductions, exemptions and surcharge using their separate income measures. Require supported calculations for the requested year.
0. **Run au-payg-instalments-2 fifth** — Reconcile the 2025–26 instalment credit against the ATO account and notices. Show any 2026–27 forecast separately; the actual notice determines the method, rate, amount and dates.

### Cross-check 1: Reconcile BAS sales to assessable business income

- **BAS-to-income reconciliation bridge** — Start with annual BAS sales on their stated GST basis. Bridge to the income-tax ledger through GST removal, GST-free and input-taxed sales, cash/accrual timing, capital receipts, excluded deposits and other tax adjustments. Reconcile the adjusted result, not an assumed equality between G1 and ITR income. Check 1A against actual taxable supplies and GST adjustments rather than 10% of all income. Explain each reconciling item and resolve unexplained differences. Example: $10,000 of qualifying GST-free business income can be assessable income with no output GST. A loan deposit is not sales merely because it is a bank credit.  _([ATO completing the GST labels](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/goods-and-services-tax-gst))_

### Cross-check 2: Super contributions within the concessional cap

- **If excess** — Test the applicable cap including eligible carry-forward amounts. Include excess concessional contributions in assessable income with the relevant 15% offset; consider release and non-concessional-cap effects. The excess concessional contributions charge does not apply to contributions made from 1 July 2021. Division 293 income is income for surcharge purposes excluding reportable super contributions, plus applicable low-tax contributions. Include the relevant reportable fringe benefits and net investment losses; apply statutory exclusions, including assessable FHSS released amounts. Tax is 15% of the lesser of low-tax contributions and the positive excess over $250,000. Exclude excess concessional contributions from low-tax contributions.  _([ITAA 1997 ss 293-20 and 293-25](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/293-20))_

**Cross-check 2 table**  _(Cross-check 2 table)_

| Super Input | Source | Rule |
| --- | --- | --- |
| Employer contributions (if also employed) | PAYG summary / income statement | Counted toward cap |
| Salary sacrifice (if any) | PAYG summary | Counted toward cap |
| Personal deductible contributions | Super fund statement + s290-170 notice | Counted toward cap |
| Total concessional | Sum of above | Compare with $30,000 plus eligible carry-forward amounts |

### Cross-check 3: Medicare levy surcharge only if no PHI and income above threshold

- **If MLS applies** — Calculate and include in tax liability. Flag for reviewer with income calculation breakdown.  _(Cross-check 3)_

**Cross-check 3 table**  _([ATO MLS income and rates](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy-surcharge/medicare-levy-surcharge-income-thresholds-and-rates))_

| MLS Input | Source | Rule |
| --- | --- | --- |
| Income for MLS purposes | ITR taxable income + reportable fringe benefits + total net investment loss + reportable super | Combined figure |
| PHI status | Insurer statement | If adequate hospital cover for full year, no MLS |
| MLS thresholds (2025–26) | Single: $101,000; family: $202,000 | Add $1,500 for each dependent child after the first; apply individual liability and coverage rules. [ATO MLS income and rates](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy-surcharge/medicare-levy-surcharge-income-thresholds-and-rates) |
| MLS rates | Tier 1: 1%; Tier 2: 1.25%; Tier 3: 1.5% | Select the tier using income for surcharge purposes, then apply it to each person’s statutory surcharge base and uncovered days. [ATO MLS income and rates](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy-surcharge/medicare-levy-surcharge-income-thresholds-and-rates) |

### Cross-check 4: PAYG instalments credit against final tax

- **If mismatch** — Common cause is varied instalments (taxpayer requested variation), or first year with no prior instalment history.  _(Cross-check 4)_

**Cross-check 4 table**  _(Cross-check 4: PAYG instalments credit against final tax)_

| PAYG Input | Source | Rule |
| --- | --- | --- |
| Instalments paid during 2025-26 | ATO income-tax account and issued instalment notices, reconciled to payments, variations and credits | Credit against final tax |
| Tax withheld by employer (if any) | PAYG summary | Additional credit |
| Final tax liability | ITR computation | Total tax - credits = balance due or refund |

### Cross-check 5: Instant asset write-off consistency

- **If inconsistency** — An asset claimed as instant write-off but costing above the threshold (on the correct GST basis) must be moved to depreciation schedule. Flag for reviewer.  _(Cross-check 5)_

**Cross-check 5 table**  _(Cross-check 5: Instant asset write-off consistency)_

| System | Threshold (2025-26) | Treatment |
| --- | --- | --- |
| GST-registered | Asset cost ex-GST < $20,000 | Immediate deduction; GST credit claimed separately |
| Non-GST-registered | Asset cost inc-GST < $20,000 | Immediate deduction on gross cost |
| At or above threshold | Apply the relevant small business pool or other depreciation rules | ITR depreciation schedule |

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
# Complete Return Package: [Client Name] -- Tax Year 2025-26

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
- 2026-27 PAYG instalment amount: $X

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
- Written-down values carried forward to 2026-27

## Super Contributions
[Content from au-super-guarantee output]
- Personal deductible contributions (s290-170 notice required)
- Employer contributions (if also employed)
- Total concessional: $X of the year's concessional cap ($30,000 for 2025–26 plus eligible carry-forward amounts)
- Excess concessional: $X / nil
- Non-concessional contributions: $X
- Division 293 check: statutory surcharge income excluding reportable super, plus applicable low-tax contributions; apply exclusions and the $250,000 threshold.
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
[Content from au-payg-instalments-2 output]
- 2025-26 instalments paid: $X (credit against final tax)
- 2025-26 instalment rate used: X%
- 2026-27 instalment income for each actual reporting period: $X
- 2026-27 notified method and amount/rate (from ATO notice): $X / X%
- 2026-27 quarterly instalment amounts:
  - Q1 (Jul-Sep): due 28 Oct 2026
  - Q2 (Oct-Dec): due 1 Mar 2027
  - Q3 (Jan-Mar): due 28 Apr 2027
  - Q4 (Apr-Jun): due 28 Jul 2027

## Cross-skill Reconciliation
- BAS-to-income reconciliation bridge: [pass/fail with reconciling items]
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
- e.g., "Home office deduction claimed at 70c/hr for X hours -- Practical Compliance Guideline PCG 2023/1"
- e.g., "Motor vehicle cents-per-km at 88c/km (2025–26) for X km -- s 28-25 ITAA 1997"
- e.g., "MacBook Pro instant asset write-off -- ITAA 1997 Div 328, $20,000 threshold" (temporary full expensing ENDED 30 June 2023 -- never cite it for a current year)
- e.g., "Personal super contribution deduction -- s290-150 ITAA 1997, s290-170 notice lodged"

## Planning Notes for 2026-27
- PAYG instalment schedule (quarterly amounts and dates)
- Super contribution strategy (remaining cap, carry-forward unused cap from prior years)
- GST registration threshold monitoring (if approaching $75K)
- Depreciation schedule continuing into 2026-27 (WDV schedule)
- PHI rebate tier based on projected income
- Any legislative changes affecting 2026-27 (budget measures, rate changes)

## Client Action List

### Immediate (before 2 November 2026 -- ITR lodgement deadline for self-lodgers):
1. Review this return package with your registered tax agent
2. Lodge ITR via myTax or through tax agent (tax agent clients have extended deadline)
3. Pay balance due of $X to ATO (or receive refund of $X)
4. Lodge any outstanding BAS quarters

### Note on lodgement deadlines:
- Self-lodgers: 2 November 2026
- Tax agent lodgement: extended deadlines apply (use the client’s applicable 2026–27 lodgement programme)

### Quarterly obligations for 2026-27:
- BAS Q1 (Jul-Sep): lodge and pay by 28 October 2026
- BAS Q2 (Oct-Dec): lodge and pay by 1 March 2027
- BAS Q3 (Jan-Mar): lodge and pay by 28 April 2027
- BAS Q4 (Apr-Jun): lodge and pay by 28 July 2027

### Super obligations:
- If you have employees: reconcile 2025–26 quarterly SG separately; use au-super-guarantee for the payday rules applying from 1 July 2026.
- Personal deductible contributions: lodge s290-170 notice with super fund BEFORE lodging ITR
- Monitor the concessional cap for the income year being assembled ($30,000 for 2025–26 plus eligible carry-forward amounts) across all contribution sources

### Ongoing:
1. Issue tax invoices for all sales (if GST registered)
2. Retain all records for 5 years from lodgement date
3. Maintain motor vehicle logbook if claiming logbook method
4. Track home office hours if claiming fixed rate method
5. Monitor turnover for GST registration threshold ($75K)
6. Review PAYG instalment rate -- vary if income changes significantly
``` (AU10)

## Section 5 -- Refusals

- **R-AU-1** — Upstream skill did not run. Name the specific skill. Note: this is a warning, not a hard stop. Continue with available data and flag the gap.  _(Section 5 -- Refusals)_
- **R-AU-2** — Upstream self-check failed. Name the specific check and note it in the reviewer brief. Continue.  _(Section 5 -- Refusals)_
- **R-AU-3** — Cross-skill reconciliation failed. Name the specific reconciliation and describe the discrepancy. Flag for reviewer but continue.  _(Section 5 -- Refusals)_
- **R-AU-4** — Intake incomplete. Specific missing intake items prevent computation. List what is missing and ask the user for the specific data point.  _(Section 5 -- Refusals)_
- **R-AU-5: Missing schedule** — If rental, CGT, foreign income or another required schedule is outside scope, record it and obtain a reviewer-completed schedule. Continue unaffected working papers, but withhold final taxable-income, tax, refund and payable figures until all required amounts are included.  _(Section 5 -- Refusals)_

## Section 6 -- Self-checks

### Pre-lodgement check register

Include a check register in the reviewer brief, separate from the issue list. Record every AU1-AU12
check and each applicable income source or schedule identified at intake, including one that could
not be performed. A blank cell, missing document or absent upstream output is not a passed check.

| Check and scope | Coverage | Evidence / method / date | Result and amount affected | Missing input / next action / owner |
| --- | --- | --- | --- | --- |
| AU reference, income source or required schedule | Performed / not performed / not applicable | Exact file or upstream output, year, reconciliation or recalculation performed | Supported / exception / unresolved; use unknown where an amount is not established | Evidence needed and reviewer responsible |

- **Performed** requires an identified procedure and actual evidence. State any sample boundary.
  A tool call that failed, a supplied checklist tick or a general statement that the books reconcile
  does not establish completion of the underlying check.
- **Not performed** includes inaccessible reports, missing upstream outputs and checks outside the
  available workflow. State the limitation and what would complete the check. Continue unaffected
  working papers subject to the existing completion gate.
- **Not applicable** requires a reason tied to the taxpayer's established facts. An unanswered
  intake question does not establish that an income source or schedule is absent.
- Keep coverage separate from findings and their disposition. A performed check can produce an
  unresolved exception; a low priority issue can still affect a mandatory amount. Risk scores,
  materiality screens and the absence of detected anomalies are review aids, never lodgement
  clearance or evidence of income completeness.
- Reconcile the intake inventory of income sources to the included schedules, ledger, prior-year
  return and relevant third-party statements. Use each source only for the coverage it provides.
  Do not assert that all taxable income is included when the necessary records were not supplied.
- Aggregate unresolved items, unavailable checks and reviewer decisions in the final brief. Claims
  such as 'recalculated', 'verified' or 'complete' must match the work actually performed. The
  reviewer determines readiness; no automated rating grants authority to lodge.

This register applies the existing completion gate: failed calculation checks, unsupported years,
unexplained reconciliation differences and missing taxable items or required schedules block final
taxable-income, tax, refund and payable figures. It does not replace a registered tax agent's review.

**Fabricated acceptance cases:**

1. Intake identifies a rental property, but no rental schedule was supplied. Record 'not performed',
   request the reviewer-completed schedule and withhold final totals, even if all other checks pass
   and the issue screen labels the case 'low risk'. Deliver the unaffected working papers as incomplete.
2. PAYG credits have been copied from a ledger without ATO statements. Record the copied amount as
   unverified and the reconciliation as 'not performed'. Do not say 'credits confirmed' or treat an
   empty exception list as evidence that the return is ready to lodge.

- **Check AU1 -- All upstream skills executed** — australia-gst, au-individual-return, au-super-guarantee, au-medicare-levy all produced output. au-payg-instalments produced output or was computed from ITR figures.  _(Section 6 -- Self-checks)_
- **Check AU2** — The BAS-to-income bridge explains GST treatment, timing, capital and other adjustments; any unexplained difference blocks final totals.  _(Section 6 -- Self-checks)_
- **Check AU3 -- Super within concessional cap** — Total concessional contributions do not exceed $30,000 (or cap plus carry-forward unused amounts).  _(Section 6 -- Self-checks)_
- **Check AU4 -- Medicare levy surcharge correctly assessed** — MLS applied only if no adequate PHI and income above threshold; MLS not applied if PHI held for full year.  _(Section 6 -- Self-checks)_
- **Check AU5 -- PAYG instalments correctly credited** — Total instalments paid during 2025-26 credited against final tax liability.  _(Section 6 -- Self-checks)_
- **Check AU6 -- GST treatment correct for registered traders** — Business income reported ex-GST; input tax credits excluded from deductible expenses; GST credits claimed on BAS.  _(Section 6 -- Self-checks)_
- **Check AU7** — Unregistered traders use the appropriate GST-inclusive income and deductible expenses; separately check PAYG instalments and withholding activity statements.  _(Section 6 -- Self-checks)_
- **Check AU8 -- Instant asset write-off threshold correct** — Assets under $20,000 (on correct GST basis) claimed as immediate deduction; assets above threshold depreciated.  _(Section 6 -- Self-checks)_
- **Check AU9 -- Personal super deduction s290-170 notice flagged** — Reviewer brief notes that the taxpayer must lodge a notice of intent to claim with the super fund before the ITR is lodged.  _(Section 6 -- Self-checks)_
- **Check AU10 -- Tax rate table correct for residency** — Resident tax rates applied (including tax-free threshold of $18,200).  _(Section 6 -- Self-checks)_
- **Check AU11 -- HELP compulsory repayment calculated from repayment income** — Repayment income = taxable income + net investment loss + reportable fringe benefits + reportable super. Correct rate applied from HELP repayment thresholds.  _(Section 6 -- Self-checks; AU11)_
- **Check AU12 -- Filing calendar is complete** — All deadlines for BAS, ITR, super, and PAYG instalments are listed with specific dates and amounts.  _(Section 6 -- Self-checks; AU12)_

## Section 7 -- Output files

- **Output file 1: master workbook** — `[client_slug]_2025-26_australia_master.xlsx` -- Single master workbook containing every worksheet and form. Sheets include: Cover, BAS Summary (quarterly), ITR (label-by-label), Depreciation Schedule, Expense Detail, Super Reconciliation, Medicare Levy, PAYG Instalments, Cross-Check Summary. Use live formulas where possible -- e.g., ITR business income references the reconciled income-tax ledger and BAS-to-income bridge; Medicare levy references ITR taxable income; PAYG credit references BAS instalment totals. Verify no `#REF!` errors. Verify computed values match the computation model within $1 before shipping.  _(Section 7 -- Output files)_
- **Output file 2: reviewer brief** — `reviewer_brief.md` -- Single markdown file covering all sections from Section 4 above: executive summary, BAS, ITR, super, Medicare, PAYG, cross-skill reconciliation, flags, positions, planning notes.  _(Section 7 -- Output files)_
- **Output file 3: client action list** — `client_action_list.md` -- Single markdown file with step-by-step actions: immediate lodgements and payments, quarterly calendar for 2026-27, ongoing compliance reminders.  _(Section 7 -- Output files)_

## Section 7 -- Output files

**If execution runs out of context mid-build:** produce whatever is complete, then state at the end which of the three files were not produced or are partial.

**All files are placed in `/mnt/user-data/outputs/` and presented to the user via the `present_files` tool at the end.**

## Section 8 -- Cross-skill references

**Inputs:**
- `au-freelance-intake` -- structured intake package (JSON)
- `australia-gst` -- BAS box values and GST output
- `au-individual-return` -- ITR label values and computation output
- `au-super-guarantee` -- Super reconciliation output
- `au-medicare-levy` -- Medicare levy and surcharge output
- `au-payg-instalments` -- Instalment schedule (or fallback computation)

**Outputs:** The final reviewer package. No downstream skill.

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
10. The package is complete only for the 2025-26 tax year; 2026-27 appears only as prospective planning.

### Change log

**v0.1 (April 2026):** Initial draft. Modelled on mt-return-assembly v0.1 adapted for Australian jurisdiction with five content skills (BAS, ITR, super, Medicare, PAYG).

## End of skill

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

> Contributed by Ryan Duguid.

> Contributed by Ryan Duguid.

> Contributed by Ryan Duguid.

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
