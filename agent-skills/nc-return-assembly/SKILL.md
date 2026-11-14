---
name: nc-return-assembly
description: "Runs last. Assembles and checks the complete federal and North Carolina package for tax year 2026 for a full-year North Carolina resident sole proprietor or single-member LLC owner disregarded for federal tax. Sets the order in which the federal skills and the NC skills (nc-income-tax, nc-bailey-settlement-retirement, nc-estimated-tax) run, the pre-flight checks, the federal-to-D-400 tie-outs (federal AGI to line 6, Schedule S totals to lines 7 and 9, line 15 at 3.99%, withholding and estimates to lines 20 and 21), the refusal codes, the reviewer deliverables and the taxpayer's dated action list (D-400 due April 15, 2027; 2027 NC-40 installments). Trigger on \"assemble my North Carolina return\", \"NC return package\", \"D-400 review package\", \"final NC return check\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nc-return-assembly"
  jurisdiction: "US-NC"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# North Carolina return assembly, tax year 2026

> **Source-cited draft.** Built from G.S. 105-153.5, 105-153.7, 105-155 and 105-163.15 and the NCDOR 2025 D-401 instructions, read on 2026-11-13, and from the sibling NC and federal skills named below. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** This skill computes nothing new. It runs the federal skills first, then `nc-income-tax`, `nc-bailey-settlement-retirement` and `nc-estimated-tax`, then checks that every D-400 figure ties back to its source, and hands the reviewer one package. For 2026 the D-400 tax is NC taxable income × **3.99%** ([G.S. 105-153.7](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.7.html)); the return is due **April 15, 2027** ([G.S. 105-155](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-155.html)). North Carolina has no city or county income tax, so there is no local return.

## The method, step by step

### Work rules

Intake and the content skills have already collected the facts. Use them and ask the client again only where something is missing or contradicts itself. Do not ask how deep to go, which deliverables to prioritize, or pause between skills to check in: run them in order and send one status message at the end. A failed self-check is a flag in the reviewer brief, not a reason to stop, unless a refusal code below applies. Citations go in the reviewer brief, not in intermediate working.

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
1.  us-tax-workflow-base                  (workflow scaffold)
2.  us-sole-prop-bookkeeping              (Schedule C classification)
3.  us-schedule-c-and-se-computation      (Schedule C, Form 8829, Schedule SE)
4.  us-section-179-and-bonus-depreciation (federal depreciation figures)
5.  us-qbi-deduction                      (Form 8995 or 8995-A)
6.  us-self-employed-health-insurance     (section 162(l))
7.  us-self-employed-retirement           (SEP or solo 401(k))
8.  us-quarterly-estimated-tax            (Form 2210, 2027 Form 1040-ES)
9.  us-federal-return-assembly            (Form 1040 and schedules)
10. us-1099-nec-issuance                  (in parallel after step 2)
11. nc-income-tax                         (D-400, Schedule S, Schedule A, D-400TC)
12. nc-bailey-settlement-retirement       (Schedule S Part B lines 19 to 21, if any)
13. nc-estimated-tax                      (D-422 for 2026; NC-40 plan for 2027)
14. nc-return-assembly                    (this skill)
```

Each skill hands over its line outputs, self-check log, refusals and flags. `nc-sales-tax` does not flow into the D-400 (Form E-500 is filed on its own cycle); show only a status line, plus any consumer use tax on D-400 line 18. `nc-payroll` applies only if the client has employees; show the NC-3 status.

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
| N-4 | D-400 line 10b = qualifying children × the per-child amount for the federal AGI band | `nc-income-tax` |
| N-5 | D-400 line 11 = NC standard deduction ($12,750 / $25,500 / $19,125) or Schedule A total, whichever is larger and elected | `nc-income-tax` |
| N-6 | D-400 line 14 = line 6 + line 7 minus lines 9, 10b and 11 (full-year resident) | `nc-income-tax` |
| N-7 | D-400 line 15 = line 14 × 3.99% | `nc-income-tax` |
| N-8 | D-400 line 16 = D-400TC total, if credits claimed | `nc-income-tax` |
| N-9 | Lines 20a and 20b = NC withholding on W-2 box 17 and on 1099s (each statement attached) | `nc-income-tax` |
| N-10 | Line 21a = 2026 NC-40 payments plus any 2025 refund applied | `nc-estimated-tax` |
| N-11 | Line 26e = D-422 interest, or zero with the reason (under $1,000, no 2025 liability, or paid by January 31) | `nc-estimated-tax` |

**Federal to NC coordination**

| Check | Equation |
| --- | --- |
| C-1 | Filing status and dependents agree on Form 1040 and D-400 |
| C-2 | Federal bonus depreciation (section 168(k)): 85% added on Schedule S Part A line 3; prior-year 20% recoveries deducted |
| C-3 | Federal section 179 above the NC $25,000 / $200,000 limits: 85% of the excess added on Part A line 4 |
| C-4 | Self-employment tax deduction and self-employed health insurance: already in federal AGI, no NC entry |
| C-5 | QBI deduction: not in AGI, so not in NC; no double count |
| C-6 | Taxable Social Security (Form 1040 line 6b) = Schedule S Part B line 19 |
| C-7 | US obligation interest = Part B line 18; other states' bond interest = Part A line 1 |
| C-8 | NC itemized: only charity, mortgage interest plus property tax up to $20,000, medical, and gambling losses; no state income or sales tax |

**Bailey and retirement**

| Check | Equation |
| --- | --- |
| B-1 | Line 20 = vested Bailey benefits in federal AGI, each with a 1099-R and service proof |
| B-2 | Line 21 = uniformed services pay (20 years or medical retirement) not on line 20 |
| B-3 | Government pension without August 12, 1989 vesting: no line 20 amount |
| B-4 | Bailey money rolled into a non-Bailey IRA: withdrawals taxable, flagged |

**1099-NEC and withholding agent status**

| Check | Equation |
| --- | --- |
| 9-1 | NEC payments in the contractor batch agree with Schedule C contract labor |
| 9-2 | If the client withholds NC tax (employees or 4% contractor withholding), NC-3 status by January 31, 2027 is confirmed |

### Step 5: deliverables

1. **Master workbook**: cover summary; assumption, taxpayer input and reviewer flag logs; federal sheets (Schedule C, 4562, 8829, SE, retirement, health insurance, 8962 if any, QBI, Schedules 1 to 3, Form 1040, Form 2210); NC sheets (D-400, Schedule S, Schedule A if itemizing, D-400TC, D-422, Bailey worksheet, NC withholding detail); 2027 Form 1040-ES and NC-40 plans; 1099-NEC batch; NC sales tax status; the verification matrix with pass, fail or not applicable. Build cross-sheet formulas from named anchors and check there are no reference errors.
2. **Reviewer brief**: executive summary; federal brief; NC brief; standard against itemized decision with both totals; 2027 estimated tax; 1099-NEC status; sales tax status; verification results; flags; refusals fired; positions taken with citations; planning notes (watch whether the FY 2025-2026 revenue trigger cut the 2027 rate to 3.49%, G.S. 105-153.7(a1)).
3. **Taxpayer action list**, by date:
   - Now: review the brief; sign federal Form 8879 and the NC e-file authorization.
   - By **April 15, 2027**: file Form 1040 and D-400; pay any balance (NCDOR online, or check with D-400V to NCDOR, PO Box 25000, Raleigh, NC 27640-0640). A federal extension extends the D-400 filing date automatically if the "Federal Extension" circle is filled in, but not the time to pay.
   - 2027 estimated tax: NC-40 by April 15, June 15 and September 15, 2027 and January 15, 2028, if the 2027 tax after withholding will be $1,000 or more ([G.S. 105-163.15](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.15.html)).
   - By January 31, 2027 (already due when most packages are built): 1099-NECs to contractors; NC-3 if the client withholds NC tax.
   - Through the year: W-9 before first payment to a contractor; keep Schedule C records; check income against the estimated tax plan before September.

If context runs short, finish the numbers first, then the brief, and say which files are partial.

## Worked case

A single sole proprietor's assembled D-400: federal AGI $90,000, Schedule S additions $17,000 (bonus add-back), deductions $1,000 (US interest), standard deduction $12,750, no children. Line 14 $93,250; line 15 $3,720.68. NC withholding $0; 2026 NC-40 payments of $3,000. Balance due on line 27 before interest: **$720.68**. Check N-11: the D-422 test uses the required annual payment from `nc-estimated-tax` (here 90% of $3,720.68 = $3,348.61, if lower than the 2025 tax), and $3,000 paid in four equal parts is short of it, so interest is computed and entered on line 26e.

```oa-check
name: NC 2026 assembled D-400 balance due
inputs:
  fagi: 90000
  additions: 17000
  deductions: 1000
  std: 12750
  rate: 0.0399
  withholding: 0
  estimates: 3000
steps:
  - line14: fagi + additions - deductions - std
  - line15: round(line14 * rate, 2)
  - balance_due: line15 - withholding - estimates
  - rap_current_year: round(line15 * 0.90, 2)
expected:
  line14: 93250
  line15: 3720.68
  balance_due: 720.68
  rap_current_year: 3348.61
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
| R-NC-FINAL-12 | Tax year other than 2026 | Refuse; rates and forms differ (2025 was 4.25%) |
| R-NC-FINAL-13 | Joint filers with one spouse not a full-year resident | Refuse; Schedule PN |
| R-NC-FINAL-14 | Amended return (Schedule AM) | Refuse |
| R-NC-FINAL-15 | Bailey claimed without vesting proof, or vesting after August 12, 1989 | Drop the line 20 amount, continue, flag it |
| R-NC-FINAL-16 | Income taxed by several states or apportionment | Refuse |
| R-NC-FINAL-17 | Foreign income, foreign tax credit at state level | Refuse |
| R-NC-FINAL-18 | Corporate income or franchise tax asked here | Route to `nc-corporate-tax` |
| R-NC-FINAL-19 | Single-member LLC taxed as a corporation, or a taxed pass-through entity election | Refuse; route to `nc-corporate-tax` |
| R-NC-FINAL-20 | NC K-1 from an S corporation or partnership | Refuse |

## Sources

| Source | URL | Read for | Read on |
| --- | --- | --- | --- |
| G.S. 105-153.7 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.7.html | Read for the 3.99% 2026 rate and the 2027 trigger | 2026-11-13 |
| G.S. 105-153.5 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html | Read for the standard deduction, child deduction and Schedule S items checked | 2026-11-13 |
| G.S. 105-155 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-155.html | Read for the April 15 due date | 2026-11-13 |
| G.S. 105-163.15 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.15.html | Read for estimated tax dates and the $1,000 test | 2026-11-13 |
| NCDOR 2025 D-401 instructions | https://www.ncdor.gov/2025-d-401-individual-income-tax-instructions/open | Read for D-400 and Schedule S line numbers, extension and payment address | 2026-11-13 |

Not yet confirmed: the 2026 D-400 and Schedule S line numbers (published January 2027); the NC e-file authorization form name for 2026 (v0.1 named Form NC-8453, not checked); the refund mailing address (v0.1 gave PO Box 25000, Raleigh NC 27640-0500, not checked).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nc-return-assembly` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nc-return-assembly. If neither is available, confirm every figure against the official source pages cited above before relying on it.
