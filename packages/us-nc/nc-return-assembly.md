---
name: nc-return-assembly
description: Runs last. Assembles and checks the complete federal and North Carolina package for tax year 2026 for a full-year North Carolina resident sole proprietor or single-member LLC owner disregarded for federal tax. Sets the order in which the federal skills and the NC skills (nc-income-tax, nc-bailey-settlement-retirement, nc-estimated-tax) run, the pre-flight checks, the federal-to-D-400 tie-outs (federal AGI to line 6, Schedule S totals to lines 7 and 9, the tax on line 15, withholding and estimates to lines 20 and 21), the status lines for NC sales tax and payroll, the refusal codes, the reviewer deliverables and the taxpayer's dated action list. It computes no tax itself and restates no rate; every figure comes from the skill that owns it. Trigger on "assemble my North Carolina return", "NC return package", "D-400 review package", "final NC return check".
version: "2.0"
jurisdiction: US-NC
tax_year: 2026
last_updated: 2026-11-14
category: orchestrator
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: router
---

# North Carolina return assembly, tax year 2026

> **Source-cited draft.** Built from G.S. 105-155 and the NCDOR 2025 D-401 instructions, read on 2026-11-14, and from the sibling NC and federal skills named below, which own every rate, deduction and threshold. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** This skill computes nothing new. It runs the federal skills first, then `nc-income-tax`, `nc-bailey-settlement-retirement` and `nc-estimated-tax`, then checks that every D-400 figure ties back to its source, and hands the reviewer one package. The rate on line 15, the standard deduction, the child deduction, the depreciation add-backs, the itemized caps, the estimated tax test and the due date all come from the owning skill, listed below; none is typed in here. North Carolina has no city or county income tax, so there is no local return.

## Scope

In scope: one full-year North Carolina resident (or a married couple filing jointly, both full-year residents), sole proprietor or single-member LLC disregarded for federal tax, with wages, investment and retirement income, for tax year 2026, original return.

Out of scope: part-year residents and nonresidents (Schedule PN), amended returns, S corporations, partnerships and taxed pass-through entities, multistate apportionment, foreign income at the state level, and corporate income and franchise tax (see "When to refuse or refer").

How to run it: intake and the content skills have already collected the facts. Use them and ask the client again only where something is missing or contradicts itself. Do not ask how deep to go, which deliverables to prioritize, or pause between skills to check in: run them in order and send one status message at the end. A failed self-check is a flag in the reviewer brief, not a reason to stop, unless a refusal code below applies. Citations go in the reviewer brief, not in intermediate working.

## Ask the client first

Intake normally has these; confirm only what is missing:

1. North Carolina residence for all of 2026, for the taxpayer and any spouse.
2. Filing status, dates of birth, and dependents with SSNs and whether each qualified for the federal child tax credit.
3. Business structure, and every asset placed in service in 2026 with the federal bonus and section 179 amounts; prior NC returns showing bonus and section 179 add-backs (2021 to 2025).
4. Any government or uniformed services pension claimed under Bailey, with the plan and service history.
5. NC withholding on every W-2 and 1099, and every 2026 NC-40 payment with its date (and any 2025 refund applied).
6. Whether the business holds a sales tax certificate or has employees.

## The method, step by step

### Who owns each figure

This skill uses figures; it does not hold them. Take each from the owning skill's output for this client.

- `nc-income-tax`: the rate on line 15, the standard deduction by filing status, the child deduction bands, the Schedule S additions and deductions (including the bonus depreciation and section 179 add-backs and limits), the NC itemized deductions and their cap, credits, consumer use tax on line 18, the due date and the extension rule.
- `nc-bailey-settlement-retirement`: the Bailey vesting test and the Schedule S Part B retirement lines.
- `nc-estimated-tax`: the estimated tax requirement, the required annual payment, the NC-40 dates and the D-422 interest.
- `nc-sales-tax`: sales and use tax rates and Form E-500 filing.
- `nc-payroll`: NC withholding tables, NC-5 and NC-3 filing, and unemployment insurance.
- The federal skills in Step 3: federal AGI, Schedule C, self-employment tax, QBI and the 1099-NEC threshold.

### Step 1: pre-flight checks

| Check | Question | Refusal if it fails |
| --- | --- | --- |
| PF-1 | Has Form 1040 been computed by `us-federal-return-assembly`? | R-NC-FINAL-1 |
| PF-2 | Is federal AGI (Form 1040 line 11) a definite number, sign included? | R-NC-FINAL-1 |
| PF-3 | Full-year NC residence confirmed for the taxpayer (and spouse if joint)? | R-NC-FINAL-6, R-NC-FINAL-13 |
| PF-4 | Business is a sole proprietorship or disregarded single-member LLC? | R-NC-FINAL-10, -11 |
| PF-5 | Tax year is 2026? | R-NC-FINAL-12 |
| PF-6 | Original return, not amended? | R-NC-FINAL-14 |
| PF-7 | If a Bailey pension is claimed, is vesting on August 12, 1989 documented? | R-NC-FINAL-15 |
| PF-8 | Any NC K-1 from an S corporation or partnership? | R-NC-FINAL-20 |
| PF-9 | Income taxed by another state beyond a simple single-state W-2? | R-NC-FINAL-16 |

### Step 2: intake items that must exist

Name and last four digits of the SSN or ITIN; filing status; NC residence for all of 2026; dates of birth; dependents with SSNs and whether each qualified for the federal child tax credit; business structure; a Bailey flag with the plan and service history; W-2s, 1099-NECs, 1099-Rs and 1099-Ks; prior NC returns showing bonus and section 179 add-backs (2021 to 2025); 2026 NC-40 payments with dates. Missing items: R-NC-FINAL-5.

### Step 3: run the skills in this order

```
1.  us-sole-prop-bookkeeping              (Schedule C classification)
2.  us-schedule-c-and-se-computation      (Schedule C, Form 8829, Schedule SE)
3.  us-section-179-and-bonus-depreciation (federal depreciation figures)
4.  us-qbi-deduction                      (Form 8995 or 8995-A)
5.  us-self-employed-health-insurance     (section 162(l))
6.  us-self-employed-retirement           (SEP or solo 401(k))
7.  us-quarterly-estimated-tax            (Form 2210, 2027 Form 1040-ES)
8.  us-federal-return-assembly            (Form 1040 and schedules)
9.  us-1099-nec-issuance                  (in parallel after step 1)
10. nc-income-tax                         (D-400, Schedule S, Schedule A, D-400TC)
11. nc-bailey-settlement-retirement       (Schedule S Part B lines 20 and 21, if any)
12. nc-estimated-tax                      (D-422 for 2026; NC-40 plan for 2027)
13. nc-return-assembly                    (this skill)
```

Each skill hands over its line outputs, self-check log, refusals and flags. `nc-sales-tax` does not flow into the D-400 (Form E-500 is filed on its own cycle); show only a status line, plus any consumer use tax on D-400 line 18. `nc-payroll` applies only if the client has employees or withholds on contractors; show the NC-3 status.

### Step 4: verification matrix

Every row is an equality with a $1 tolerance. A failure is R-NC-FINAL-3. D-400 line numbers are the 2025 form's (the 2026 form is published in January 2027).

**Federal (re-checked)**

| Check | Equation | Owner |
| --- | --- | --- |
| F-1 | Schedule C line 31 = Schedule 1 line 3 | `us-schedule-c-and-se-computation` |
| F-2 | Schedule SE line 12 = Schedule 2 line 4; Schedule SE line 13 = Schedule 1 line 15 | `us-schedule-c-and-se-computation` |
| F-3 | Retirement and health insurance deductions = Schedule 1 lines 16 and 17 | `us-self-employed-retirement`, `us-self-employed-health-insurance` |
| F-4 | QBI deduction = Form 1040 line 13 | `us-qbi-deduction` |
| F-5 | Total tax, payments and refund or balance due agree with Form 1040 | `us-federal-return-assembly` |

**North Carolina**

| Check | Equation | Owner |
| --- | --- | --- |
| N-1 | Federal AGI (Form 1040 line 11) = D-400 line 6 | `nc-income-tax` |
| N-2 | Schedule S Part A total = D-400 line 7 | `nc-income-tax` |
| N-3 | Schedule S Part B total (2025 line 41) = D-400 line 9 | `nc-income-tax` |
| N-4 | D-400 line 10b = qualifying children times the per-child amount for the federal AGI band in `nc-income-tax` | `nc-income-tax` |
| N-5 | D-400 line 11 = the NC standard deduction for the filing status, or the Schedule A total, whichever is elected (the larger unless a reason is recorded) | `nc-income-tax` |
| N-6 | D-400 line 14 = line 6 + line 7 minus lines 9, 10b and 11 (full-year resident) | `nc-income-tax` |
| N-7 | D-400 line 15 = line 14 times the 2026 rate in `nc-income-tax` | `nc-income-tax` |
| N-8 | D-400 line 16 = D-400TC total, if credits claimed | `nc-income-tax` |
| N-9 | Lines 20a and 20b = NC withholding on W-2 box 17 and on 1099s (each statement attached) | `nc-income-tax` |
| N-10 | Line 21a = 2026 NC-40 payments plus any 2025 refund applied | `nc-estimated-tax` |
| N-11 | Line 26e = D-422 interest, or zero with the reason given by `nc-estimated-tax` | `nc-estimated-tax` |

**Federal to NC coordination**

| Check | Equation | Owner |
| --- | --- | --- |
| C-1 | Filing status and dependents agree on Form 1040 and D-400 | `nc-income-tax` |
| C-2 | Federal bonus depreciation (section 168(k)): the add-back on Schedule S Part A line 3 as computed by `nc-income-tax`; prior-year recoveries deducted | `nc-income-tax` |
| C-3 | Federal section 179 above the NC limits: the add-back on Part A line 4 as computed by `nc-income-tax` | `nc-income-tax` |
| C-4 | Self-employment tax deduction and self-employed health insurance: already in federal AGI, no NC entry | `nc-income-tax` |
| C-5 | QBI deduction: not in AGI, so not in NC; no double count | `nc-income-tax` |
| C-6 | Taxable Social Security (Form 1040 line 6b) = Schedule S Part B line 19 | `nc-income-tax` |
| C-7 | US obligation interest = Part B line 18; other states' bond interest = Part A line 1 | `nc-income-tax` |
| C-8 | NC itemized: only charity, mortgage interest plus property tax within the cap in `nc-income-tax`, medical, and gambling losses; no state income or sales tax | `nc-income-tax` |

**Bailey and retirement**

| Check | Equation | Owner |
| --- | --- | --- |
| B-1 | Schedule S line 20 = vested Bailey benefits in federal AGI, each with a 1099-R and service proof | `nc-bailey-settlement-retirement` |
| B-2 | Line 21 = uniformed services pay (20 years or medical retirement) not on line 20 | `nc-bailey-settlement-retirement` |
| B-3 | Government pension without August 12, 1989 vesting: no line 20 amount | `nc-bailey-settlement-retirement` |
| B-4 | Bailey money rolled into a non-Bailey IRA: withdrawals taxable, flagged | `nc-bailey-settlement-retirement` |

**1099-NEC, withholding agent, sales tax**

| Check | Equation | Owner |
| --- | --- | --- |
| 9-1 | NEC payments in the contractor batch agree with Schedule C contract labor | `us-1099-nec-issuance` |
| 9-2 | If the client withholds NC tax (employees or contractor withholding), NC-3 status is confirmed | `nc-payroll` |
| S-1 | Sales tax: every E-500 due while the certificate is open is filed; only consumer use tax reaches D-400 line 18 | `nc-sales-tax` |

### Step 5: deliverables

1. **Master workbook**: cover summary; assumption, taxpayer input and reviewer flag logs; federal sheets (Schedule C, 4562, 8829, SE, retirement, health insurance, 8962 if any, QBI, Schedules 1 to 3, Form 1040, Form 2210); NC sheets (D-400, Schedule S, Schedule A if itemizing, D-400TC, D-422, Bailey worksheet, NC withholding detail); 2027 Form 1040-ES and NC-40 plans; 1099-NEC batch; NC sales tax status; the verification matrix with pass, fail or not applicable. Build cross-sheet formulas from named anchors and check there are no reference errors.
2. **Reviewer brief**: executive summary; federal brief; NC brief; standard against itemized decision with both totals; 2027 estimated tax; 1099-NEC status; sales tax status; verification results; flags; refusals fired; positions taken with citations; planning notes (whether the revenue trigger in G.S. 105-153.7 has changed the 2027 rate, as reported by `nc-income-tax`).
3. **Taxpayer action list**, by date, with each date taken from the owning skill:
   - Now: review the brief; sign federal Form 8879 and the NC e-file authorization.
   - By the D-400 due date in `nc-income-tax`: file Form 1040 and D-400; pay any balance (NCDOR online, or check with Form D-400V). A federal extension extends the D-400 filing date automatically only if the "Federal Extension" circle is filled in; otherwise file Form D-410. Neither extends the time to pay.
   - 2027 estimated tax: the NC-40 installments and the test for whether they are needed, from `nc-estimated-tax`.
   - January 2027 (already due when most packages are built): 1099-NECs to contractors (`us-1099-nec-issuance`); NC-3 if the client withholds NC tax (`nc-payroll`).
   - Through the year: W-9 before first payment to a contractor; keep Schedule C records; check income against the estimated tax plan before September.

If context runs short, finish the numbers first, then the brief, and say which files are partial.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| No children | N-4 is zero; say so |
| Itemizing chosen though the standard deduction is larger | Allowed only with a recorded reason (for example a spouse filing separately itemizes); flag it |
| 2026 assets with federal bonus or section 179 | C-2 and C-3 must show add-backs; nil add-backs are a hold |
| Earlier years' bonus add-backs | Prior-year recoveries must appear as Schedule S deductions; ask for the 2021 to 2025 returns if missing |
| Bailey claimed | B-1 to B-4; without vesting proof the line 20 amount is dropped (R-NC-FINAL-15) |
| Sales tax certificate open, no sales | Status line; nil E-500 still due under `nc-sales-tax` |
| No employees and no NC withholding on contractors | Skip `nc-payroll`; say so |

### Defaults when a fact is missing

| Missing fact | Default |
| --- | --- |
| Prior NC add-back history | No prior-year recovery deduction; flag it |
| NC-40 payment dates | Use NCDOR account records; flag any difference (N-10) |
| A withholding statement | Claim no withholding for it until attached (N-9) |
| Child tax credit eligibility | No child deduction for that child; flag it |

### Red flags

| Flag | Why |
| --- | --- |
| D-400 line 6 differs from Form 1040 line 11 | The NC return was built from a superseded federal draft |
| Schedule S empty with 2026 assets | Depreciation add-backs missed |
| State income tax in NC itemized deductions | Not allowed (C-8) |
| Line 26e zero with a balance due and no reason | `nc-estimated-tax` did not run |

## Worked cases

**Case 1, tie out the assembled D-400.** A single sole proprietor who itemizes. From the skills: federal AGI $90,000 (Form 1040 line 11 and D-400 line 6), Schedule S additions $17,000 (bonus add-back), Schedule S deductions $1,000 (US interest), no child deduction, NC itemized deductions $21,000, all from `nc-income-tax`, which reports line 14 of $85,000 and line 15 of $3,391.50. This skill recomputes line 14 from the parts: $90,000 + $17,000 - $1,000 - $0 - $21,000 = $85,000, so N-6 ties with no difference. NC withholding $0; 2026 NC-40 payments $3,000. Balance due on line 27 before interest: **$391.50**. N-11 then checks line 26e against the D-422 result from `nc-estimated-tax`.

```oa-check
name: NC 2026 assembly, N-6 tie-out and balance due
inputs:
  line6: 90000
  line7: 17000
  line9: 1000
  line10b: 0
  line11: 21000
  line14_reported: 85000
  line15_reported: 3391.50
  withholding: 0
  estimates: 3000
steps:
  - line14_recomputed: line6 + line7 - line9 - line10b - line11
  - n6_difference: abs(line14_recomputed - line14_reported)
  - balance_due: line15_reported - withholding - estimates
expected:
  line14_recomputed: 85000
  n6_difference: 0
  balance_due: 391.50
```

**Case 2, a decision: release or hold the package (check N-9).** The client has a W-2 with $2,400 of NC withholding in box 17 and a 1099-NEC with $300 of NC withholding. The D-400 shows $2,400 on lines 20a and 20b together. The statements total $2,700, so the return is $300 short, $299 beyond the $1 tolerance: hold and send it back to `nc-income-tax` with the missing 1099 attached. Once lines 20a and 20b carry $2,700 the difference is nil and the package is released.

```oa-check
name: NC 2026 assembly, withholding tie-out, hold against release
inputs:
  w2_box17: 2400
  form_1099_nc_withholding: 300
  lines_20_in_package: 2400
  lines_20_after_fix: 2700
  tolerance: 1
steps:
  - statements_total: w2_box17 + form_1099_nc_withholding
  - shortfall_before: statements_total - lines_20_in_package
  - excess_over_tolerance: max(0, shortfall_before - tolerance)
  - shortfall_after_fix: statements_total - lines_20_after_fix
expected:
  statements_total: 2700
  shortfall_before: 300
  excess_over_tolerance: 299
  shortfall_after_fix: 0
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-NC-FINAL-1 | An upstream skill did not run | Refuse; name the skill |
| R-NC-FINAL-2 | An upstream self-check failed and was not resolved | Refuse; name the check |
| R-NC-FINAL-3 | A verification row failed beyond $1 | Refuse; name the equation and the difference |
| R-NC-FINAL-4 | An upstream refusal was suppressed | Refuse; resolve it first |
| R-NC-FINAL-5 | Intake is incomplete | Refuse; name the missing items |
| R-NC-FINAL-6 | Not a full-year NC resident (Schedule PN) | Refuse; out of scope |
| R-NC-FINAL-7 | Intake flagged a NC city or county income tax | Refuse; none exists, route back to intake |
| R-NC-FINAL-10 | The business is an S corporation (CD-401S) | Refuse; use `nc-corporate-tax` |
| R-NC-FINAL-11 | The business is a partnership (D-403) | Refuse; use `nc-corporate-tax` |
| R-NC-FINAL-12 | Tax year other than 2026 | Refuse; rates and forms differ by year |
| R-NC-FINAL-13 | Joint filers with one spouse not a full-year resident | Refuse; Schedule PN |
| R-NC-FINAL-14 | Amended return (Schedule AM) | Refuse |
| R-NC-FINAL-15 | Bailey claimed without vesting proof, or vesting after August 12, 1989 | Drop the line 20 amount, continue, flag it |
| R-NC-FINAL-16 | Income taxed by several states or apportionment | Refuse |
| R-NC-FINAL-17 | Foreign income, foreign tax credit at state level | Refuse |
| R-NC-FINAL-18 | Corporate income or franchise tax asked here | Route to `nc-corporate-tax` |
| R-NC-FINAL-19 | Single-member LLC taxed as a corporation, or a taxed pass-through entity election | Refuse; route to `nc-corporate-tax` |
| R-NC-FINAL-20 | NC K-1 from an S corporation or partnership | Refuse |

## Filing and payment

| Return | When and how |
| --- | --- |
| Federal Form 1040 | As in `us-federal-return-assembly` |
| D-400 with Schedule S, Schedule A, D-400TC and D-422 as needed | Due date as in `nc-income-tax` (a calendar-year return is due on or before April 15 under G.S. 105-155(a)); e-file, or mail: refund returns to NC Department of Revenue, PO Box R, Raleigh, NC 27634-0001; returns with a payment, with Form D-400V, to NC Department of Revenue, PO Box 25000, Raleigh, NC 27640-0640 |
| Extension | Automatic if the federal extension was granted and the "Federal Extension" circle on the D-400 is filled in; otherwise Form D-410 by the due date. It does not extend the time to pay |
| 2027 NC-40 installments | As in `nc-estimated-tax` |
| E-500, NC-5, NC-3 | Their own cycle, under `nc-sales-tax` and `nc-payroll` |

The reviewer files, not the agent. Payment is the client's act.

## Completion checklist

- Every skill in Step 3 ran, or its absence is explained in the brief.
- Pre-flight checks PF-1 to PF-9 passed.
- Every verification row (F, N, C, B, 9, S) passed within $1, or the refusal is recorded.
- No rate, deduction or threshold was typed into the package; each came from its owning skill.
- Depreciation add-backs present for every 2026 asset with federal bonus or section 179, and prior-year recoveries deducted.
- Standard against itemized compared, both totals in the brief.
- Withholding statements attached for every amount on lines 20a and 20b.
- 2027 NC-40 plan included; sales tax and payroll status lines included.
- Taxpayer action list dated from the owning skills.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| G.S. 105-155. Read for the rule that a calendar-year return "is due on or before the fifteenth day of April". | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-155.html | 2026-11-14 |
| NCDOR 2025 D-401 instructions. Read for the D-400 and Schedule S line numbers (lines 6, 7, 9, 10b, 11, 14, 15, 16, 18, 20a, 26e; Schedule S lines 20, 21 and 41), the Federal Extension circle and Form D-410, Form D-400V and the two mailing addresses. | https://www.ncdor.gov/2025-d-401-individual-income-tax-instructions/open | 2026-11-14 |

Not yet confirmed: the 2026 D-400 and Schedule S line numbers (published January 2027), so the 2025 lines are used; the name of the NC e-file authorization form for 2026; whether the 2026 D-401 keeps the same mailing addresses.
