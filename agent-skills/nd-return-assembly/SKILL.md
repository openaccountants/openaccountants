---
name: nd-return-assembly
description: "Final capstone orchestrator that assembles the complete federal and North Dakota filing package for tax year 2026 for a full-year North Dakota resident sole proprietor or single-member LLC disregarded for federal tax. Consumes the outputs of every upstream federal and North Dakota skill (bookkeeping, Schedule C and SE, QBI, retirement, self-employed health insurance, quarterly estimated tax, federal return assembly, 1099-NEC, nd-income-tax, nd-estimated-tax, nd-payroll, nd-corporate-tax routing checks and nd-sales-tax status) and produces one reviewer package with every worksheet, every cross-skill reconciliation, the taxpayer action list with filing and payment steps, the 2027 ND-1ES schedule and the reviewer brief. It does not recompute tax; it orchestrates and links every figure to the skill that owns it. Trigger on assemble the North Dakota return, final ND package, ND-1 reviewer package, ND return assembly, package up the Dakota return. Load alongside us-tax-workflow-base and ever"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nd-return-assembly"
  jurisdiction: "US-ND"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# North Dakota return assembly, tax year 2026 (capstone orchestrator)

> **Source-cited draft.** Built from the 2025 North Dakota individual income tax booklet (the 2025-2026 filing cycle, the latest published), the 2026 Form ND-1ES, the 2025 Schedule ND-1UT, the Tax Commissioner's individual income tax and credit pages and N.D.C.C. chapter 57-38, read on 2026-11-14. No accountant has reviewed it. A qualified professional (Enrolled Agent, CPA or attorney under Circular 230) must review the package before filing.

**Answer first.** This skill runs last. Federal first, North Dakota second: the 2026 Form ND-1 starts from federal taxable income (Form 1040, line 15), entered even when negative, so every federal deduction, including the standard or itemized deduction and the QBI deduction, is already in the starting figure. North Dakota then adds and subtracts its own adjustments, applies the 2026 rate schedules owned by `nd-income-tax`, subtracts credits, withholding and estimates, and adds any Schedule ND-1UT interest. The orchestrator checks that every upstream skill ran, that every figure on the ND-1 equals the figure its owning skill produced, and then writes three files: a master workbook, a reviewer brief and a taxpayer action list. The 2026 Form ND-1 is due by the regular due date, generally 15 April 2027. No figure is restated here; each is linked to the skill that owns it.

## Scope and who this is for

In scope: tax year 2026 (returns filed in 2027) for a full-year North Dakota resident, single or married filing jointly with both spouses full-year residents, who is a sole proprietor or owns a single-member LLC disregarded for federal tax, possibly with W-2 wages (including Minnesota or Montana wages under reciprocity), interest, dividends, retirement income, Social Security, military retirement, farm income with averaging, Renaissance Zone income, or enrolled-member reservation income.

Primary North Dakota outputs: Form ND-1, Schedule ND-1SA (statutory adjustments), Schedule ND-1TC (credits), Schedule ND-1CR (credit for income tax paid to another state), Schedule ND-1FA (farm income averaging) if used, Schedule ND-1UT (underpayment of estimated tax) if needed, and the 2027 Form ND-1ES schedule.

Refused at this orchestrator: Schedule ND-1NR (nonresident or part-year), amended returns, fiduciary returns (Form 38), corporations (Form 40), partnerships (Form 58), S corporations (Form 60), and incoming North Dakota Schedule K-1s from pass-through entities.

Who owns what:

| Topic | Skill |
| --- | --- |
| 2026 rate schedules, additions, subtractions, credits, Schedule ND-1SA and ND-1TC detail | `nd-income-tax` |
| 2026 estimated tax tests, Schedule ND-1UT interest, the 2027 ND-1ES schedule | `nd-estimated-tax` |
| Nonresident sourcing, reciprocity, military residence, credit for tax paid to another state | `nd-cross-border-tax` |
| Employer withholding and reconciliation (if the taxpayer is also an employer) | `nd-payroll` |
| Sales and use tax status | `nd-sales-tax` |
| Corporate and pass-through routing | `nd-corporate-tax` |
| The federal return, Form 1040 line 15 and every federal figure | `us-federal-return-assembly` and the federal skills it loads |
| 1099-NEC thresholds and deadlines | `us-1099-nec-issuance` |

## Ask the client first

Intake and the content skills have already collected the facts. Use what they captured; ask again only where something is missing or contradicts itself. Before assembly, confirm that intake holds:

1. **Identity and status:** taxpayer name, SSN or ITIN (last four digits only in working files), filing status (single, married filing jointly, married filing separately, head of household, qualifying surviving spouse), dates of birth (they drive the federal additional standard deduction already inside line 15), dependents with SSNs.
2. **Residence:** full-year North Dakota residence for the taxpayer and, if joint, the spouse; days spent outside North Dakota; whether the person is in the armed forces.
3. **Business structure:** sole proprietor or single-member LLC disregarded federally; no S corporation, partnership or incoming North Dakota Schedule K-1.
4. **Cross-border wages:** any W-2 wages from Minnesota or Montana employers and whether Minnesota Form MW-R or Montana Form MT-R was given to the employer; any wages from other states.
5. **Flags:** oil and gas royalty or mineral income; enrolled tribal member with reservation income; Renaissance Zone project; military retirement or military pay; Social Security; farm income and a federal Schedule J election.
6. **Documents:** Forms W-2, 1099-NEC, 1099-R, SSA-1099, 1095-A, B or C; 2026 North Dakota estimated payment records; the 2025 Form ND-1 (for line 25 and any overpayment applied to 2026).

If any item is missing, refuse with R-ND-FINAL-5 and name the item.

### How this workflow runs

- Do not ask the user "how deep do you want me to go". The taxpayer asked for a North Dakota return. Produce it.
- Do not announce tool budgets or token counts. Execute.
- Do not ask which deliverables to prioritize. Produce all three files. If context runs short, finish the numbers first, then produce what formatted output you can, and say at the end which deliverables are partial.
- Do not re-validate scope intake already validated (residence, business structure, filing status, reciprocity, oil and gas, tribal, Renaissance Zone, age, dependents). Cross-check specific numbers during reconciliation; do not re-interrogate the taxpayer.
- Do not pause between content skills to check in. Run them in the loading order without prose updates between them. One status message at the end is enough.
- Self-checks are targets, not blockers. A failed self-check is a flag in the reviewer brief, not a halt. The reviewer handles edges.
- Primary citations go in the reviewer brief, not in intermediate computation.

Failure mode to avoid: halting mid-run to ask a meta-question about pacing. If you feel the urge to ask "how should I proceed", pick the most defensible path, proceed, and flag the decision for the reviewer.

## The method, step by step

### Rates, bands and thresholds

None are stated here. The 2026 rate schedules and every North Dakota adjustment and credit figure belong to `nd-income-tax`; estimated tax thresholds and the interest rate belong to `nd-estimated-tax`; every federal figure belongs to the federal skills. The orchestrator compares figures; it does not hold them.

### Step 1: pre-flight checks

| Check | Question | Refusal if it fails |
| --- | --- | --- |
| PF-1 | Has `us-federal-return-assembly` computed Form 1040? | R-ND-FINAL-1 |
| PF-2 | Is federal taxable income (Form 1040, line 15) available as a finite number? If the federal computation is below zero, the federal form shows 0, but Form ND-1, line 1b takes the negative number with a minus sign ([2025 booklet, line 1b](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf)). Flag it. | R-ND-FINAL-1 |
| PF-3 | Is full-year North Dakota residence confirmed, including the statutory 7-month rule and armed forces residence (`nd-cross-border-tax`)? | R-ND-FINAL-6 |
| PF-4 | Is the business a sole proprietorship or disregarded single-member LLC? | R-ND-FINAL-10 / R-ND-FINAL-11 |
| PF-5 | Is the tax year 2026? | R-ND-FINAL-12 |
| PF-6 | If married filing jointly, are both spouses full-year residents? (If either was a nonresident for any part of the year, Schedule ND-1NR is required.) | R-ND-FINAL-13 |
| PF-7 | Is this an original return, not an amended one? | R-ND-FINAL-14 |
| PF-8 | Any incoming Schedule K-1 from an S corporation or partnership? | R-ND-FINAL-20 |
| PF-9 | Wages earned outside North Dakota, Minnesota or Montana? | R-ND-FINAL-16 |
| PF-10 | Oil, gas or mineral royalty income? Income tax treatment is in scope; extraction and production tax filings are not. | Flag only; R-ND-FINAL-21 for the excise filings |
| PF-11 | Farm income with a federal Schedule J election? | In scope: confirm `nd-income-tax` produced Schedule ND-1FA |
| PF-12 | Renaissance Zone income? | In scope: confirm the subtraction on Schedule ND-1SA |
| PF-13 | Enrolled tribal member with income earned on the reservation? | In scope: confirm the subtraction with enrollment evidence |

### Step 2: confirm the federal skills ran

In this order, each with its outputs and self-check log: `us-sole-prop-bookkeeping` (Schedule C classification), `us-schedule-c-and-se-computation` (Schedule C, Form 8829, Schedule SE), `us-self-employed-retirement` (SEP or solo 401(k), Schedule 1), `us-self-employed-health-insurance` (section 162(l), iterated with any premium tax credit), `us-qbi-deduction` (Form 8995 or 8995-A, Form 1040 line 13; it lowers North Dakota tax because North Dakota starts after it), `us-federal-return-assembly` (Form 1040 and schedules; line 15 is the single most important handoff), `us-quarterly-estimated-tax` (Form 2210 and the 2027 Form 1040-ES schedule), and `us-1099-nec-issuance` (contractor list and W-9 gaps; may run in parallel after bookkeeping). If any is missing or its self-checks failed, refuse with R-ND-FINAL-1 or R-ND-FINAL-2 naming the skill.

### Step 3: confirm the North Dakota skills ran

1. `nd-income-tax`: Form ND-1 with Schedule ND-1SA, ND-1TC, ND-1CR and ND-1FA as needed; North Dakota taxable income, tax under the 2026 schedule, credits, refund or balance due.
2. `nd-estimated-tax`: Schedule ND-1UT interest for any short 2026 installment, and the 2027 ND-1ES schedule if the 2026 net tax liability makes estimates required.
3. `nd-payroll`: flag only. If the taxpayer is also a North Dakota employer, record the status of the withholding returns and annual reconciliation. It does not block the individual return.
4. `nd-corporate-tax`: routing check only. Any corporate, partnership or S corporation fact refuses with R-ND-FINAL-10, R-ND-FINAL-11 or R-ND-FINAL-18.

Any missing skill or failed self-check refuses with R-ND-FINAL-1 or R-ND-FINAL-2.

### Step 4: no city or county return step

The North Dakota individual booklet sets out no city or county income tax return, so this workflow has no local return step. If intake flagged a "city return", treat it as an intake error: refuse with R-ND-FINAL-7 and route back to intake. (The credit on Schedule ND-1CR covers income tax paid to another state or a local jurisdiction in that state; that is a different point, handled in Step 5.)

### Step 5: reciprocity and other-state wages

For a North Dakota resident with Minnesota or Montana wages: North Dakota has reciprocity agreements with both states, so compensation for services is taxable only by the state of residence ([2025 booklet, "Reciprocity"](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf)). Confirm the employer had Minnesota Form MW-R or Montana Form MT-R, so no Minnesota or Montana tax was withheld. If it was withheld, the taxpayer must file in that state to get it back: refuse that filing with R-ND-FINAL-22 and continue the North Dakota return. No Schedule ND-1CR credit is claimed for reciprocity wages, because no tax was due to the other state. Wages from any other state may need that state's nonresident return and a Schedule ND-1CR credit (`nd-cross-border-tax`); simple single-state cases proceed, multi-state apportionment refuses with R-ND-FINAL-16.

### Step 6: run the verification matrix

Run every check below. Each is an equality between a figure on a final form and the output of the skill that produced it. Tolerance is USD 1 unless noted; a failure halts assembly with R-ND-FINAL-3 naming the check.

Form line numbers below are those on the 2025 forms (the 2025-2026 filing cycle). Confirm each against the 2026 Form ND-1, its schedules and the 2026 Form 1040 when published.

#### 6A: federal internal consistency (re-verified)

| Check | Equation | Owning skill |
| --- | --- | --- |
| F-1 | Schedule C line 31 = Schedule 1 line 3, carried to Form 1040 | `us-schedule-c-and-se-computation` |
| F-2 | Schedule SE line 12 = Schedule 2 line 4 | `us-schedule-c-and-se-computation` |
| F-3 | Schedule SE line 13 = Schedule 1 line 15 | `us-schedule-c-and-se-computation` |
| F-4 | SEP or solo 401(k) employer plus employee amounts = Schedule 1 line 16 | `us-self-employed-retirement` |
| F-5 | Section 162(l) deduction = Schedule 1 line 17 | `us-self-employed-health-insurance` |
| F-6 | QBI deduction = Form 1040 line 13 | `us-qbi-deduction` |
| F-7 | Form 1040 line 11 (AGI) = line 9 less line 10 | `us-federal-return-assembly` |
| F-8 | Form 1040 line 14 = line 12 plus line 13 | `us-federal-return-assembly` |
| F-9 | Form 1040 line 15 = line 11 less line 14 (the North Dakota handoff) | `us-federal-return-assembly` |
| F-10 | Total tax = Form 1040 line 24 | `us-federal-return-assembly` |
| F-11 | Form 2210 penalty, if any, = Schedule 2 amount | `us-quarterly-estimated-tax` |
| F-12 | Total payments = Form 1040 line 33 | `us-federal-return-assembly` |
| F-13 | Refund or balance due = Form 1040 line 34 or 37 | `us-federal-return-assembly` |

#### 6B: North Dakota internal consistency

| Check | Equation | Owning skill |
| --- | --- | --- |
| N-1 | Form ND-1, line 1b = Form 1040 line 15 (federal taxable income, not federal AGI), negative if the federal computation was below zero | `nd-income-tax` |
| N-2 | Additions on lines 2 to 3 = the additions `nd-income-tax` produced | `nd-income-tax` |
| N-3 | Subtractions on lines 5 to 16 (line 16 = Schedule ND-1SA total) = the subtractions `nd-income-tax` produced | `nd-income-tax` |
| N-4 | North Dakota taxable income = line 1b plus additions less subtractions | `nd-income-tax` |
| N-5 | Line 20 tax = the 2026 schedule for the filing status applied to North Dakota taxable income, as computed by `nd-income-tax` (recompute; do not take a stored figure) | `nd-income-tax` |
| N-6 | If Schedule ND-1FA is used, its tax replaces the schedule tax on line 20 and is documented | `nd-income-tax` |
| N-7 | Line 21 = Schedule ND-1CR; credit no more than the lesser of tax actually paid to the other state and the North Dakota tax on that income ([credit page](https://www.tax.nd.gov/credit-income-tax-paid-another-state-or-local-jurisdiction)) | `nd-cross-border-tax` |
| N-8 | Line 22 marriage penalty credit only on a joint return meeting the booklet's conditions | `nd-income-tax` |
| N-9 | Line 23 = Schedule ND-1TC total | `nd-income-tax` |
| N-10 | Line 25 net tax liability = tax less credits (withholding and estimates are not subtracted) | `nd-income-tax` |
| N-11 | Line 26 withholding = North Dakota amounts on Forms W-2, 1099 and North Dakota Schedules K-1; no extraction or production tax withheld from royalties | `nd-income-tax` |
| N-12 | Line 27 = 2026 Form ND-1ES payments plus any Form ND-1EXT payment plus any 2025 overpayment left on deposit | `nd-estimated-tax` |
| N-13 | Overpayment (line 29) or tax due (line 33) = net tax liability less total payments | `nd-income-tax` |
| N-14 | Line 37 = Schedule ND-1UT line 17 interest, included in the balance due or deducted from the refund | `nd-estimated-tax` |
| N-15 | Line 30 overpayment applied to 2027 matches the 2027 ND-1ES first-installment credit | `nd-estimated-tax` |

#### 6C: federal and North Dakota coordination

| Check | Equation |
| --- | --- |
| C-1 | Filing status on Form ND-1 = filing status on Form 1040 |
| C-2 | Dependents flow from the federal return; North Dakota has no separate dependent deduction in the Form ND-1 lines read, so nothing is added on Schedule ND-1TC for them |
| C-3 | Schedule C net profit is inside the federal taxable income on line 1b |
| C-4 | Bonus depreciation and section 179: no North Dakota addition unless `nd-income-tax` names one; verify no stray addition |
| C-5 | The deductible half of self-employment tax and the section 162(l) deduction are inside federal AGI; no North Dakota addition |
| C-6 | The federal QBI deduction is already inside line 1b; verify no second deduction on Schedule ND-1SA |
| C-7 | The federal standard or itemized deduction (including any age 65 addition) is already inside line 1b; North Dakota takes no second deduction |
| C-8 | Taxable Social Security from Form 1040 line 6b is subtracted on Form ND-1, line 15; Railroad Retirement Board Tier 1 equivalents go on line 8 instead ([2025 booklet](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf)) |
| C-9 | Interest on US obligations in Schedule B is subtracted on line 5 |
| C-10 | Interest on other states' municipal bonds: an addition only if `nd-income-tax` produced one |
| C-11 | Taxable military retirement from Form 1040 line 5b is subtracted on line 14, only the military portion; military pay included in federal taxable income goes on line 11 |
| C-12 | Renaissance Zone income: federal reporting unchanged; subtraction through Schedule ND-1SA (line 16) only with the zone project documentation |
| C-13 | Enrolled-member reservation income: federal reporting unchanged; subtraction on line 7 only with enrollment evidence and on-reservation sourcing |
| C-14 | Net long-term capital gain exclusion on line 6 and qualified dividend exclusion on line 13 match the `nd-income-tax` worksheets |

#### 6D: Minnesota and Montana reciprocity

| Check | Equation |
| --- | --- |
| R-1 | Minnesota wages: Minnesota Form MW-R on file with the employer; no Minnesota withholding; wages taxed only in North Dakota |
| R-2 | Montana wages: Montana Form MT-R on file; no Montana withholding; wages taxed only in North Dakota |
| R-3 | Minnesota or Montana tax withheld in error: R-ND-FINAL-22 (the other state's refund return is a separate job) |
| R-4 | No Schedule ND-1CR credit for reciprocity wages |
| R-5 | Wages from a third state: Schedule ND-1CR may apply, limited as in N-7 |

#### 6E: 1099-NEC reconciliation

| Check | Equation |
| --- | --- |
| 9-1 | Contractor payments flagged for 1099-NEC = Schedule C contract labor plus any other labor lines |
| 9-2 | Every contractor over the federal threshold in `us-1099-nec-issuance` has a W-9; gaps go to the flag log |
| 9-3 | The federal filing deadline from `us-1099-nec-issuance` is noted; if it has passed, the late-filing exposure is surfaced |
| 9-4 | If the taxpayer is also a North Dakota withholding agent, the annual reconciliation status from `nd-payroll` is recorded (flag only) |

#### 6F: estimated tax

| Check | Equation |
| --- | --- |
| E-1 | 2027 federal first voucher = `us-quarterly-estimated-tax` output |
| E-2 | 2027 ND-1ES first voucher = `nd-estimated-tax` output (no voucher if the 2026 net tax liability is below the threshold in `nd-estimated-tax`) |
| E-3 | The North Dakota prior-year test is 100% of the prior-year net tax liability with no high-income step-up ([2026 Form ND-1ES, line 12](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf)); the federal and state required payments may differ |
| E-4 | First federal plus first North Dakota voucher fits the cash availability intake recorded, if any |
| E-5 | Any 2026 Schedule ND-1UT interest is surfaced for the reviewer |
| E-6 | 2026 North Dakota estimated payments actually made (Tax Commissioner payment confirmations or cancelled checks) = line 27 |

#### 6G: withholding tie-out

| Check | Equation |
| --- | --- |
| W-1 | Sum of Form W-2 North Dakota income tax withheld = the W-2 part of line 26 |
| W-2 | Sum of Form 1099 and North Dakota Schedule K-1 North Dakota withholding = the rest of line 26 |
| W-3 | Total North Dakota withholding = line 26 |
| W-4 | Backup detail captured in the workbook |
| W-5 | Reciprocity wages: the employer withheld North Dakota tax (not Minnesota or Montana); otherwise see R-3 |

#### 6H: special-population cross-checks

| Check | Equation |
| --- | --- |
| S-1 | Military retirement subtraction: Form 1099-R consistent with military retirement; service documentation on file; a copy of Form 1099-R included |
| S-2 | Renaissance Zone subtraction: zone project documentation on file; income tied to the qualifying activity |
| S-3 | Enrolled-member subtraction: enrollment evidence on file; income earned on the reservation, not merely by an enrolled member off it |
| S-4 | Farm averaging: federal Schedule J used; Schedule ND-1FA tax computed and included |
| S-5 | Oil and gas royalties: only the income tax treatment is in scope; extraction and production taxes withheld are not income tax withholding and are not on line 26 |

### Step 7: aggregate the logs

Pull every "Assumed" item from every upstream skill into the assumption log; every "Taxpayer input needed" item into the taxpayer input log; every "Reviewer judgment needed" item into the reviewer flag log; every refusal that fired anywhere into the refusal log.

### Step 8: compose the three deliverables

The package is three files, not fifteen. Do not fragment the output. Place them in `/mnt/user-data/outputs/` and present them at the end with `present_files`.

**File 1: `{taxpayer_slug}_2026_nd_master.xlsx`.** One workbook, sheets in this order:

1. Cover: taxpayer, filing status, residence, business structure, reciprocity flag, oil and gas flag, summary (federal tax, North Dakota tax, total liability, total payments, net refund or balance due, key 2027 dates).
2. Assumption log. 3. Taxpayer input log. 4. Reviewer flag log.
5. Income summary (W-2, 1099-NEC, Schedule C, interest, dividends, capital gains, 1099-R, other).
6. Schedule C. 7. Form 4562 (if any). 8. Form 8829 (if any). 9. Schedule SE.
10. Retirement worksheet. 11. Self-employed health insurance worksheet with any premium tax credit iteration log. 12. Form 8962 (if marketplace coverage).
13. QBI (Form 8995 or 8995-A). 14. Schedule 1. 15. Schedule 2. 16. Schedule 3 (if any).
17. Form 1040 line by line, with line 15 highlighted as the North Dakota handoff. 18. Form 2210 (if any).
19. Form ND-1 line by line. 20. Schedule ND-1SA. 21. Schedule ND-1TC (if any). 22. Schedule ND-1CR (if any). 23. Schedule ND-1FA (if any). 24. Schedule ND-1UT (if any).
25. Reciprocity wage tracker (if any). 26. Military retirement and military pay detail (if any). 27. Renaissance Zone detail (if any). 28. Reservation income detail (if any).
29. North Dakota withholding detail. 30. 2027 federal Form 1040-ES schedule. 31. 2027 Form ND-1ES schedule (if required).
32. 1099-NEC batch (if any). 33. North Dakota sales tax status (if a registrant). 34. Verification matrix: every Step 6 check with pass, fail or not applicable.

Use the same workbook discipline as `us-federal-return-assembly`: collect anchors as a Python dict before writing cross-sheet formulas; verify no `#REF!` errors; verify computed cells match the Python model within USD 1 before shipping.

**File 2: `reviewer_brief.md`.** Readable in under 30 minutes. Sections in this order:

```markdown
# Complete Return Package -- [Taxpayer Name] -- Tax Year 2026

## Executive Summary
- Taxpayer: [Name], full-year North Dakota resident
- Filing status: [Single / MFJ / MFS / HoH / QSS]
- Business: sole proprietor / single-member LLC disregarded
- Minnesota or Montana reciprocity in play: [Yes / No]
- Special populations: [military retirement / military pay / Renaissance Zone /
  reservation income / farm averaging / none]
- Federal total tax (Form 1040 line 24): $X
- Federal taxable income (Form 1040 line 15, the North Dakota starting point): $X
- North Dakota net tax liability (Form ND-1 net tax liability line): $X
- Total payments (withholding, estimates, extension payments): $X
- Net refund or balance due: $X
- Action required by the 2027 due date: [one line]

## Federal Return
[condensed brief from us-federal-return-assembly; emphasise line 15]

## North Dakota Return
[brief from nd-income-tax, with each addition and subtraction line]

## Rate Schedule Audit
- North Dakota taxable income: $X
- Filing-status schedule applied (from nd-income-tax, 2026): [name]
- Band reached: [0% / 1.95% / 2.50%]
- Line 20 tax: $X (recomputed, matches nd-income-tax: yes / no)

## Reciprocity
[form on file with each employer, source state, North Dakota treatment; or N/A]

## Estimated Tax for 2027
[federal Form 1040-ES and Form ND-1ES schedules side by side]

## 1099-NEC Issuance
[from us-1099-nec-issuance]

## North Dakota Sales Tax Status
[from nd-sales-tax if a registrant; else N/A]

## Cross-skill Verification
- All upstream skills ran: [verified / list missing]
- All upstream self-checks passed: [verified / list failures]
- All Step 6 reconciliations passed: [verified / list failures]

## Reviewer Attention Flags
[aggregated, ranked by materiality]

## Refusals Triggered
[aggregated; any entry blocks final sign-off]

## Positions Taken
[items needing reviewer judgment, with citations to N.D.C.C., the IRC and booklet pages]

## Planning Notes for 2027
[rate schedule changes from the Legislative Assembly; federal changes that flow
through line 15; zone end dates; military continuity; estimated-tax positioning]

## Taxpayer Action List
[embedded copy of File 3]
```

**File 3: `taxpayer_action_list.md`.** Step by step, by date. The taxpayer reads this file and nothing else.

```markdown
# Your 2026 North Dakota Tax Filing -- Action List

## This week
1. Read the reviewer brief.
2. Sign the federal e-file authorization (Form 8879) if e-filing.
3. Sign the North Dakota return or its e-file authorization (both spouses on a joint return).
4. Confirm bank details for direct debit or direct deposit.

## By the 2026 return due date (generally 15 April 2027)
1. File federal Form 1040 (e-file preferred).
2. Pay the federal balance due of $X (methods in us-federal-return-assembly).
3. File North Dakota Form ND-1: e-file with the federal return through the
   Federal/State e-file program, or mail the paper return with a complete copy of
   the federal return to Office of State Tax Commissioner, P.O. Box 5621,
   Bismarck, ND 58506-5621.
4. Pay the North Dakota balance due of $X: online at tax.nd.gov ("Make A Payment"),
   or by check payable to "ND State Tax Commissioner" with the last four digits of
   your SSN and "2026 Form ND-1" on it, with Form ND-1PRV (paper return) or
   Form ND-1V (e-filed return).

## 2027 estimated tax (if required)
1. 15 April 2027: federal first voucher $X; North Dakota first voucher $X.
2. 15 June 2027: federal $X; North Dakota $X.
3. 15 September 2027: federal $X; North Dakota $X.
4. 15 January 2028: federal $X; North Dakota $X.

## Contractor forms (check if done)
1. File 1099-NEC forms and furnish copies by the date in us-1099-nec-issuance.
2. If you are also a North Dakota employer, file the annual withholding
   reconciliation (see nd-payroll).

## During the year
1. Collect a W-9 from every new contractor before the first payment.
2. Keep Schedule C income and expense records with receipts.
3. Check income against the estimated-tax tests mid-year.
4. Keep health coverage records (Forms 1095-A, B, C).
5. If a sales tax registrant, file on your assigned schedule (see nd-sales-tax).
6. If you work for a Minnesota or Montana employer, give them a new
   Form MW-R or Form MT-R as that state requires.

## Checking your refund
- Federal: "Where's My Refund?" at irs.gov.
- North Dakota: "Where's My Refund?" at tax.nd.gov.

## Questions
- Your reviewer (CPA or EA) named on the cover sheet.
- North Dakota Office of State Tax Commissioner, individual income tax: 701-328-1247.
```

### Step 9: final status message

One message: which skills ran, which self-checks passed, which deliverables were produced, any partial deliverables and why. Done.

### Deterministic rules

| Rule | Rule text | Source |
| --- | --- | --- |
| ND-ASM-T1-01 | The federal return is completed before Form ND-1; information from it is needed for the North Dakota return. | [2025 booklet, "Federal income tax return"](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf) |
| ND-ASM-T1-02 | Form ND-1, line 1b = Form 1040 line 15 (federal taxable income, not AGI), entered as a negative number if the federal computation is below zero. | same, line 1b |
| ND-ASM-T1-03 | Full-year residents compute line 20 from the 2026 tax table or rate schedule in `nd-income-tax`; anyone who was a nonresident for any part of the year needs Schedule ND-1NR (refused here). | same, line 20 |
| ND-ASM-T1-04 | No city or county income tax return step. | Step 4 |
| ND-ASM-T1-05 | The return is due by the regular due date, generally 15 April 2027; a date on a Saturday, Sunday or holiday moves to the next day that is not one. | [2026 Form ND-1ES](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf); 2025 booklet, "When and where to file" |
| ND-ASM-T1-06 | A federal extension is recognized for North Dakota with no separate form; fill in the "Extension" circle. Without a federal extension, Form 101 must be postmarked by the due date and needs good cause. | 2025 booklet, "Extension of time to file" |
| ND-ASM-T1-07 | An extension to file is not an extension to pay: interest at 12% per year runs from the original due date to the earlier of filing or the extended due date; prepay with Form ND-1EXT (and then file Form ND-1, not ND-EZ). | 2025 booklet, "Extension interest" and "Prepayment of tax due" |
| ND-ASM-T1-08 | Taxable Social Security (Form 1040 line 6b) is subtracted on line 15. | 2025 booklet, line 15 |
| ND-ASM-T1-09 | Taxable military retirement (Form 1040 line 5b) is subtracted on line 14; military pay on line 11. | 2025 booklet, lines 11 and 14 |
| ND-ASM-T1-10 | 2027 estimated tax follows the four tests and the 90% or 100% required payment in `nd-estimated-tax`; there is no 110% step-up. | [2026 Form ND-1ES](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf) |
| ND-ASM-T1-11 | North Dakota takes no second standard or itemized deduction and no second QBI deduction; both are inside line 1b. | 2025 booklet, line 1b |
| ND-ASM-T1-12 | Reciprocity wages of a North Dakota resident are taxed only in North Dakota; no Schedule ND-1CR credit for them. | 2025 booklet, "Reciprocity" |
| ND-ASM-T1-13 | The Schedule ND-1CR credit is the lesser of tax actually paid to the other state and the North Dakota tax on the income it taxed. | [credit page](https://www.tax.nd.gov/credit-income-tax-paid-another-state-or-local-jurisdiction) |
| ND-ASM-T1-14 | North Dakota extraction or production taxes withheld from royalties are not income tax withholding: never on line 26. | 2025 booklet, line 26 |
| ND-ASM-T1-15 | A paper return carries a complete copy of the federal return (Form 1040 and all schedules, not depreciation workpapers). | 2025 booklet, "Federal income tax return" |
| ND-ASM-T1-16 | Use Form ND-1, not ND-EZ, if there are any additions, subtractions or credits, any nonresidence, any amount applied from the prior year, any extension payment, or Schedule ND-1UT interest. | 2025 booklet, "Which form to use" and line 37 |
| ND-ASM-T1-17 | Three files (workbook, brief, action list) are mandatory. | Step 8 |
| ND-ASM-T1-18 | Oil and gas extraction tax filings are not produced; royalty income tax treatment is handled through line 1b. | Step 1, PF-10 |

### Judgement rules

| Rule | Situation | Guidance |
| --- | --- | --- |
| ND-ASM-T2-01 | Materiality of a reconciliation gap | A USD 1 rounding gap is not a failure; USD 50 is. Default USD 5 for federal and North Dakota tie-outs, USD 1 within a form; the reviewer may set another threshold. North Dakota allows amounts to be rounded to the nearest dollar ([N.D.C.C. 57-38-75](https://ndlegis.gov/cencode/t57c38.pdf)). |
| ND-ASM-T2-02 | Taxable income just above the top of the 0% band in `nd-income-tax` | Note in planning whether a deductible expense or retirement contribution would keep it in the 0% band. |
| ND-ASM-T2-03 | Renaissance Zone documentation incomplete | Flag; do not take the subtraction without reviewer sign-off. |
| ND-ASM-T2-04 | Reservation income sourcing | `nd-income-tax` decides on-reservation status; the orchestrator checks the enrollment evidence is on file. |
| ND-ASM-T2-05 | Military retirement scope | Only military retirement qualifies on line 14 (plus the dual-status technician retirement the booklet names); disability pay and VA benefits are generally already excluded federally. Check the Form 1099-R payer and code. |
| ND-ASM-T2-06 | Minnesota or Montana certificate missing or stale | R-ND-FINAL-22; route the other state's refund return to a multistate preparer. |
| ND-ASM-T2-07 | Self-employment work physically done in another state | It may be taxable there and may earn a Schedule ND-1CR credit; material out-of-state work refuses with R-ND-FINAL-16. |
| ND-ASM-T2-08 | The 1099-NEC deadline may have passed when the orchestrator runs | Surface the exposure in the action list; the reviewer decides. |
| ND-ASM-T2-09 | Premium tax credit iteration did not converge | Escalate the flag from `us-self-employed-health-insurance` to the brief and document the position chosen. |
| ND-ASM-T2-10 | Farm income averaging | Confirm the federal Schedule J election came first and that averaging lowers the combined federal and North Dakota tax. |
| ND-ASM-T2-11 | Negative federal taxable income or an NOL | Enter the negative figure on line 1b; verify the North Dakota carryforward documentation in `nd-income-tax`; flag for the reviewer. |
| ND-ASM-T2-12 | Oil and gas royalties | Royalties are ordinary income inside line 1b; severance taxes paid at the well are not a credit on Form ND-1. Document the royalty source; avoid double counting. |
| ND-ASM-T2-13 | A federal return change later | An amended North Dakota return is due within 90 days of the amended federal return or of the final IRS determination ([2025 booklet, "Change to federal return"](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf)); record it in the planning notes. |

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Minnesota or Montana resident (not a North Dakota resident) with North Dakota wages | Not this orchestrator: `nd-cross-border-tax` (reciprocity refund return, item F). |
| Nonresident North Dakota spouse on a joint return | Schedule ND-1NR: refuse (R-ND-FINAL-13). |
| Statutory 7-month rule: a nonresident with a North Dakota home and more than the booklet's day count in North Dakota | Treated as a full-year resident; confirm with `nd-cross-border-tax` before running. |
| Taxpayer also an employer | Individual return continues; payroll filings flagged from `nd-payroll`. |
| Sales tax registrant | Status line only from `nd-sales-tax`; does not block. |
| Late filing or late payment | Penalties and interest under N.D.C.C. 57-38-45: see Filing and payment. Line 34 may carry them, or the Commissioner will notify. |
| Overpayment to apply to 2027 | Line 30; the election cannot be changed after filing ([2025 booklet, line 30](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf)). |
| Voluntary contributions from the refund or with a balance due | Lines 31 and 35, at least USD 1.00 to a fund; record the taxpayer's choice. |
| Direct deposit to a foreign financial institution | Not allowed; a paper check is issued (2025 booklet, line 32). |

## Worked cases

**Kari Halvorson, single, Fargo, tax year 2026.** Full-year resident sole proprietor, no special populations, no additions or subtractions. Upstream outputs: `us-federal-return-assembly` gives Form 1040 line 15 of USD 90,604; `nd-income-tax` gives North Dakota tax on line 20 of USD 800.07 under the 2026 single schedule; no credits. North Dakota withholding USD 360 (a small W-2 job); 2026 ND-1ES payments USD 400 (USD 200 on 15 April and 15 June 2026). Her 2025 net tax liability was USD 780.

Assembly: N-1 line 1b = 90,604; N-4 North Dakota taxable income = 90,604; N-5 recomputed tax = 800.07, matches; N-10 net tax liability = 800.07; payments = 360 + 400 = 760; tax due = USD 40.07. Schedule ND-1UT is not needed: her 2025 net tax liability was below the USD 1,000 floor in `nd-estimated-tax`, so no 2026 estimates were required. For 2027, the 2026 net tax liability of USD 800.07 is also below that floor, so no 2027 ND-1ES schedule is produced. The action list tells her to pay USD 40.07 (or USD 40 if rounded to whole dollars under N.D.C.C. 57-38-75) by the 2027 due date at tax.nd.gov.

```oa-check
name: ND-1 2026 assembly tie-out, single resident with withholding and estimates
inputs:
  federal_taxable_income: 90604
  nd_additions: 0
  nd_subtractions: 0
  nd_tax_from_nd_income_tax: 800.07
  credits: 0
  nd_withholding: 360
  nd_estimates: 400
  prior_year_net_tax_liability: 780
  estimate_floor_from_nd_estimated_tax: 1000
steps:
  - nd_taxable_income: federal_taxable_income + nd_additions - nd_subtractions
  - net_tax_liability: nd_tax_from_nd_income_tax - credits
  - total_payments: nd_withholding + nd_estimates
  - tax_due: net_tax_liability - total_payments
  - prior_year_gap_to_floor: estimate_floor_from_nd_estimated_tax - prior_year_net_tax_liability
  - current_year_gap_to_floor: estimate_floor_from_nd_estimated_tax - net_tax_liability
expected:
  nd_taxable_income: 90604
  net_tax_liability: 800.07
  total_payments: 760
  tax_due: 40.07
  prior_year_gap_to_floor: 220
  current_year_gap_to_floor: 199.93
```

Both gaps are positive, so the liability is under the floor in both years and no Schedule ND-1UT or 2027 ND-1ES is needed.

## When to refuse or refer

| ID | Situation | Action |
| --- | --- | --- |
| R-ND-FINAL-1 | An upstream skill did not run. | Refuse; name the missing skill. |
| R-ND-FINAL-2 | An upstream self-check failed and was not resolved. | Refuse; name the check. |
| R-ND-FINAL-3 | A Step 6 reconciliation failed beyond the USD 1 (or T2-01) tolerance. | Refuse; name the equation and the gap. |
| R-ND-FINAL-4 | A refusal fired upstream and was suppressed in its output. | Refuse; force resolution. |
| R-ND-FINAL-5 | Intake is incomplete (residence, dates of birth, filing status, reciprocity flag, oil and gas flag and so on). | Refuse; name the missing items. |
| R-ND-FINAL-6 | Not a full-year North Dakota resident. | Refuse; out of scope (`nd-cross-border-tax`). |
| R-ND-FINAL-7 | Intake flagged a North Dakota city or county income tax return. | Refuse; route back to intake. |
| R-ND-FINAL-8, 9, 15 | Reserved. | None. |
| R-ND-FINAL-10 | S corporation (Form 1120-S federally; North Dakota Form 60). | Refuse; route to `nd-corporate-tax`. |
| R-ND-FINAL-11 | Partnership (Form 1065 federally; North Dakota Form 58). | Refuse; out of scope. |
| R-ND-FINAL-12 | A tax year other than 2026. | Refuse; schedules and forms differ. |
| R-ND-FINAL-13 | Joint filers with mixed residence. | Refuse; Schedule ND-1NR is out of scope. |
| R-ND-FINAL-14 | Amended return. | Refuse; out of scope. |
| R-ND-FINAL-16 | Multi-state apportionment beyond simple Minnesota or Montana reciprocity wages. | Refuse; out of scope. |
| R-ND-FINAL-17 | Foreign income, the foreign earned income exclusion or foreign tax credit at state level. | Refuse; out of scope. |
| R-ND-FINAL-18 | North Dakota corporate or pass-through tax (wrong tax type). | Refuse; route to `nd-corporate-tax`. |
| R-ND-FINAL-19 | A single-member LLC that elected to be taxed as a corporation, or any entity-level election. | Refuse; only disregarded LLCs are in scope. |
| R-ND-FINAL-20 | Incoming North Dakota Schedule K-1 from an S corporation or partnership. | Refuse; out of scope. |
| R-ND-FINAL-21 | Oil and gas extraction or production tax, or coal severance tax, filings. | Refuse; out of scope. Royalty income tax proceeds through line 1b. |
| R-ND-FINAL-22 | Minnesota or Montana tax withheld in error despite reciprocity. | Refuse the other state's refund filing; continue the North Dakota return and flag the recovery as separate work. |
| R-ND-FINAL-23 | Part-year residence with a move to or from another state. | Refuse; Schedule ND-1NR is out of scope. |

## Filing and payment

- **Due date:** the 2026 Form ND-1 is due by the regular due date, generally 15 April 2027 ([2026 Form ND-1ES](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf)). Fiscal-year filers: the 15th day of the 4th month after year end ([2025 booklet](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf)).
- **E-file:** North Dakota participates in the IRS Federal/State e-file program, so both returns can be filed together ([Tax Commissioner individual income tax page](https://www.tax.nd.gov/individual-income-tax)). A payment can be scheduled when e-filing (2025 booklet).
- **Paper:** mail to Office of State Tax Commissioner, P.O. Box 5621, Bismarck, ND 58506-5621, with a complete copy of the federal return (2025 booklet, "When and where to file").
- **Pay:** online at tax.nd.gov ("Make A Payment") by electronic check or card; or by check or money order payable to "ND State Tax Commissioner", with the last four digits of the SSN and the form name and year on it, using Form ND-1PRV with a paper return or Form ND-1V with an e-filed return; the check must be on a US or Canadian bank in US dollars (2025 booklet, line 36).
- **Late payment and late filing** ([N.D.C.C. 57-38-45](https://ndlegis.gov/cencode/t57c38.pdf); 2025 booklet, "Penalty and interest"): unpaid tax on a timely return, 5% or USD 5, whichever is greater; late return with tax due, 5% (or USD 5) for the first month plus 5% for each further month or part, up to 25%; interest 1% per month or part, except the month the tax was due; the Commissioner may waive for good cause.
- **Refund status:** "Where's My Refund?" on tax.nd.gov; the Tax Commissioner states about 30 days for refund processing ([individual income tax page](https://www.tax.nd.gov/individual-income-tax)).
- **Refund claims on an amended return:** generally within three years after filing the original return (2025 booklet, "Changing your return").
- **Help:** 701-328-1247 ([2026 Form ND-1ES, page 3](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf)).

## Completion checklist

| # | Check |
| --- | --- |
| 200 | All upstream content skills ran. |
| 201 | All upstream self-checks passed, or were waived with a reviewer flag. |
| 202 | 6A federal internal reconciliations pass. |
| 203 | 6B North Dakota internal reconciliations pass. |
| 204 | 6C federal and North Dakota coordination passes. |
| 205 | 6D reciprocity passes or is not applicable. |
| 206 | 6E 1099-NEC passes or is not applicable. |
| 207 | 6F estimated tax passes. |
| 208 | 6G withholding tie-out passes. |
| 209 | 6H special populations pass or are not applicable. |
| 210 | The assumption log holds every "Assumed" item from every upstream skill. |
| 211 | The reviewer flag log holds every "Reviewer judgment" item. |
| 212 | The action list has specific dollar amounts and dates. |
| 213 | Planning notes cover rate schedule changes, federal changes flowing through line 15, military, zone and reservation continuity where they apply, and contractor form thresholds from `us-1099-nec-issuance`. |
| 214 | Every refusal in the table was tested against the facts. |
| 215 | Three files produced in `/mnt/user-data/outputs/`. |
| 216 | `present_files` called with the three files. |
| 217 | The rate schedule audit in the brief names the band and the schedule from `nd-income-tax`. |
| 218 | Form ND-1, line 1b equals Form 1040 line 15 (not line 11), sign included. |

Known gaps: PDF form filling is not automated (the reviewer transcribes the worksheets into tax software or the paper form); e-filing and payment are done outside the agent; multi-state returns, foreign income, part-year and nonresident returns are not supported; oil and gas extraction and coal severance filings are not produced; Renaissance Zone, reservation and military subtractions are computed by `nd-income-tax` and only their documentation is checked here; the reciprocity check assumes the employer correctly withheld North Dakota tax when the other state's certificate was on file.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 2025 individual income tax booklet, 2025-2026 filing cycle. Read for "Which form to use", reciprocity, residence and the 7-month rule, when and where to file, extensions, extension interest and prepayment, penalty and interest, federal return copy, amended returns, and Form ND-1 lines 1b, 2, 5 to 16, 20 to 23, 26, 27, 30 to 37. | https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf | 2026-11-14 |
| 2026 Form ND-1ES. Read for the 2026 return due date ("generally, April 15, 2027"), the 100% prior-year test, payment instructions and the help line. | https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf | 2026-11-14 |
| 2025 Schedule ND-1UT, 2025-2026 filing cycle. Read for the line 1 and line 3 links to Form ND-1 lines 25 and 26 and the line 17 transfer to line 37. | https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28704-schedule-nd-1ut-2025.pdf | 2026-11-14 |
| Tax Commissioner individual income tax page. Read for filing requirements, Federal/State e-file, paper filing, amendment within 90 days, extensions and refund processing time. | https://www.tax.nd.gov/individual-income-tax | 2026-11-14 |
| Tax Commissioner page, credit for income tax paid to another state or local jurisdiction. Read for qualifications, the lesser-of amount and Schedule ND-1CR. | https://www.tax.nd.gov/credit-income-tax-paid-another-state-or-local-jurisdiction | 2026-11-14 |
| N.D.C.C. chapter 57-38. Read for sections 57-38-45 (penalties, interest, waiver) and 57-38-75 (rounding to whole dollars). | https://ndlegis.gov/cencode/t57c38.pdf | 2026-11-14 |

Not yet confirmed: the 2026 Form ND-1, schedules and instructions (not yet published; every line number here is from the 2025 forms, 2025-2026 filing cycle); the Form ND-1 line number for North Dakota taxable income, which the 2025 booklet gives as both line 18 and line 19 in different places; the 2026 Form 1040 line numbers in the federal checks; a statutory source for the absence of any city or county individual income tax; North Dakota treatment of bonus depreciation, section 179 and other states' municipal bond interest beyond what `nd-income-tax` states; the federal and North Dakota extended due dates for tax year 2026.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nd-return-assembly` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nd-return-assembly. If neither is available, confirm every figure against the official source pages cited above before relying on it.
