---
name: us-tx-return-assembly
description: "Final assembly of the 2026 federal return and Texas compliance package for a Texas-resident sole proprietor or single-member LLC disregarded for federal tax. Runs the federal skills in order, then the Texas franchise tax (Public Information Report, or a report above the $2,650,000 no tax due threshold), Texas sales tax where taxable items are sold, and Texas Workforce Commission unemployment tax where there are employees. Reconciles Schedule C with Texas total revenue (Schedule C line 3 is Item 1 for an LLC), checks the Texas filings are current, and produces the reviewer brief and the client's dated action list. Texas has no individual income tax and no state estimated tax. Trigger after us-tx-freelance-intake, or on \"assemble my Texas return package\", \"Texas freelancer return\", \"Texas LLC filing package\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-tx-return-assembly"
  jurisdiction: "US-TX"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Texas freelancer return assembly, tax year 2026

> **Source-cited draft.** The Texas figures are from the Texas Comptroller's franchise tax page and 2026 instructions (Form 05-915), Tax Code Chapter 171 and Article 8 of the Texas Constitution; the one federal figure stated here is from Public Law 119-21 (via the federal figures library). All read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For a full-year Texas resident there is no state income tax return and no state estimated tax. The package is: the 2026 Form 1040 with Schedules C, SE, 1 and 2 (due 15 April 2027); for an LLC, the Texas Public Information Report (Form 05-102) due 17 May 2027 (15 May is a Saturday), plus a franchise tax report only if annualized revenue is over **$2,650,000**; Texas sales tax returns if a permit is held; and TWC quarterly reports if there are employees. A sole proprietor with no LLC files nothing for franchise tax.

## Scope

In scope: one Texas-resident individual, full year 2026, sole proprietor or single-member LLC disregarded for federal tax, after `us-tx-freelance-intake` has confirmed scope. Out of scope: anything refused there, and the cases in "When to refuse or refer" below.

How to run it: use the facts intake captured and ask again only where something is missing or contradicts itself. Produce the full package without asking how deep to go, without pausing between skills, and without re-checking scope intake already settled. A failed self-check is flagged for the reviewer, not a reason to stop.

## Ask the client first

Intake has asked these; confirm only if missing:

1. Is there an LLC, and is every past Public Information Report filed?
2. Total 2026 revenue of the LLC, its formation date, and any revenue outside Schedule C (interest, gains) belonging to the LLC.
3. Is a Texas sales tax permit open, and are all its returns filed?
4. Were there employees in 2026, and is the TWC account current?
5. Federal estimated tax paid for 2026, with dates.

## The method, step by step

### Rates, bands and thresholds

| Item | Figure | Source |
| --- | --- | --- |
| Texas individual income tax | None (prohibited) | [Texas Constitution, Article 8, Section 24-a](https://statutes.capitol.texas.gov/Docs/CN/htm/CN.8.htm) |
| Franchise tax no tax due threshold, 2026 and 2027 reports | USD 2,650,000 annualized total revenue | [Texas Comptroller, franchise tax](https://comptroller.texas.gov/taxes/franchise/) |
| Texas estimated tax | None required | [Form 05-915 (2026), Estimated Tax](https://comptroller.texas.gov/forms/05-915.pdf) |
| Federal SALT deduction cap, taxable years beginning in 2026 (half if married filing separately; reduced above a MAGI threshold) | USD 40,400 | [Public Law 119-21, section 70120](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |

Every other figure has its home in the skill that runs it.

### Execution order

1. `us-sole-prop-bookkeeping`: classify transactions to Schedule C lines.
2. `us-schedule-c-and-se-computation`: Schedule C net profit, home office, Schedule SE.
3. `us-self-employed-retirement`, then `us-self-employed-health-insurance`.
4. `us-qbi-deduction`.
5. `us-federal-income-tax-return-1040` (or `us-federal-return-assembly`): the Form 1040.
6. `us-quarterly-estimated-tax`: 2026 underpayment check and 2027 vouchers.
7. `us-1099-nec-issuance`: 1099-NECs to contractors paid in 2026.
8. `tx-franchise-tax`: for an LLC only.
9. The Texas sales tax skill named in this folder's README: if a permit is open or taxable items are sold.
10. `tx-payroll`, with `us-form-941-940-payroll`: if there were employees.
11. This skill: reconcile and assemble.

### Federal consistency checks

Schedule C line 31 to Schedule 1 line 3; Schedule SE tax to Schedule 2 line 4; the deductible half to Schedule 1 line 15; retirement to Schedule 1 line 16; self-employed health insurance to Schedule 1 line 17; QBI to Form 1040 line 13; estimated payments to the payments section, matched to IRS records. Line numbers follow the federal skills; if a 2026 form moved a line, the federal skill governs.

### Texas franchise tax checks (LLC only)

1. Total revenue for Texas = Schedule C **line 3** (gross receipts less returns and allowances) as Item 1, plus LLC income outside it (Schedule C line 6 to the extent not included, and the LLC's share of Schedule D, Form 4797 and Schedule E items) less the 171.1011 exclusions (Form 05-915, Items 1 to 9). Explain every difference from Schedule C line 1.
2. Annualize if the LLC existed for less than the full period, then compare with USD 2,650,000.
3. At or below: prepare Form 05-102 (entity name, taxpayer number, principal office, officers, managers or members, registered agent matching the Secretary of State record). Above: run `tx-franchise-tax` and attach its E-Z or Long Form working.
4. Confirm the entity's status is active and that no earlier PIR is missing; a missing one is a red flag (forfeiture and personal liability).
5. Any franchise tax paid is a business expense on Schedule C, not a personal state tax.

### Texas sales tax and payroll checks

Sales tax collected per the books matches the returns, the returns match the Comptroller payments, no period is unfiled while the permit is open, and filing frequency matches the Comptroller's assignment (all under the sales tax skill). TWC: four quarterly reports filed, taxable wages capped at USD 9,000 per employee, rate from the 2026 notice (`tx-payroll`).

### Federal itemized deduction note

There is no Texas income tax to deduct. A client who itemizes may deduct state and local general sales taxes instead (actual receipts or the IRS optional tables), together with property taxes, within the SALT cap of USD 40,400 for 2026 (USD 20,200 married filing separately), which is reduced for MAGI above the threshold in `us-federal-income-tax-return-1040`. Compare with the standard deduction there.

### Package

1. Executive summary: filing status, income, federal tax, Texas franchise tax status, sales tax and payroll status, refund or balance due.
2. Form 1040 working with Schedules C, SE, 1, 2 and 3, Form 8995 or 8995-A, Form 2210 if needed.
3. 2027 estimated tax schedule (`us-quarterly-estimated-tax`).
4. Texas franchise tax sheet: total revenue build, annualization, threshold result, PIR data or the report working.
5. Texas sales tax summary and TWC summary, if they apply.
6. 1099-NEC batch.
7. Reviewer brief: positions with citations, the Schedule C to Texas revenue reconciliation, flags, and planning notes (revenue against USD 2,650,000; S corporation election in `us-s-corp-election-decision`, which also changes the franchise tax compensation figure).
8. Client action list with dates.

Files: `[client]_2026_master.xlsx`, `reviewer_brief.md`, `client_action_list.md`.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Sole proprietor, no LLC | Skip `tx-franchise-tax` entirely |
| LLC at or below USD 2,650,000 annualized | PIR only, by 17 May 2027 |
| LLC above USD 2,650,000 annualized | `tx-franchise-tax`; refer the computation to a reviewer if cost of goods sold or apportionment is in question |
| Sales tax permit open, no taxable sales | Zero returns still due; note closing the permit |
| Employees | TWC quarterly reports; federal payroll |
| Earlier PIR missing | Flag first: file it before anything else |

## Worked cases

**Case 1, reconciling Schedule C with Texas total revenue.** A Texas single-member LLC reports 2026 Schedule C line 1 gross receipts of USD 410,000, line 2 returns of USD 10,000 (so line 3 is USD 400,000) and line 6 other income of USD 2,500. Texas total revenue = USD 400,000 + USD 2,500 = USD 402,500, with no exclusions. It is USD 2,247,500 under the USD 2,650,000 threshold, so the 2027 filing is Form 05-102 only, by 17 May 2027, and no franchise tax is owed.

```oa-check
name: Schedule C to Texas total revenue, PIR-only result (2027 report)
inputs:
  line_1: 410000
  line_2: 10000
  line_6: 2500
  threshold: 2650000
steps:
  - line_3: line_1 - line_2
  - texas_total_revenue: line_3 + line_6
  - headroom: threshold - texas_total_revenue
expected:
  line_3: 400000.00
  texas_total_revenue: 402500.00
  headroom: 2247500.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-TX-AS-UPSTREAM | An upstream skill did not run | Name it and run it; do not assemble around a gap |
| R-TX-AS-MARGIN | LLC above USD 2,650,000 with cost of goods sold, compensation or apportionment questions | Refer the franchise tax working to a reviewer |
| R-TX-AS-APPORT | Customers outside Texas in volume and services performed in several states | Refer: apportionment and other states' taxes |
| R-TX-AS-SALESAUDIT | Sales tax audit or dispute with the Comptroller | Refer |
| R-TX-AS-COMBINED | The LLC is in a combined group with related entities | Refer |
| R-TX-AS-FORFEIT | The LLC's right to transact business is forfeited | Refer: reinstatement first |

## Filing and payment

| When | Action |
| --- | --- |
| By 15 April 2027 | File Form 1040; pay any balance (IRS Direct Pay or EFTPS); first 2027 estimate per `us-quarterly-estimated-tax` |
| By 17 May 2027 | LLC only: Form 05-102 on Comptroller Webfile (and the franchise tax report and payment if above the threshold). An extension to 15 November is available under `tx-franchise-tax` |
| Quarterly, if a sales tax permit is open | Sales tax returns per the assigned frequency (sales tax skill) |
| 30 April, 31 July, 31 October, 31 January | TWC reports and payments if there are employees (`tx-payroll`) |
| Ongoing | W-9 before paying contractors; keep receipts; watch revenue against USD 2,650,000; keep the registered agent current |

## Completion checklist

- Every upstream skill ran, or its absence is flagged.
- Federal flow-through lines agree.
- Texas total revenue reconciled to Schedule C line 3 and other LLC income; annualized if needed; compared with USD 2,650,000.
- PIR or report prepared for an LLC; none for a sole proprietor.
- All past PIRs, sales tax returns and TWC reports confirmed filed.
- No state estimated tax or state income tax payment on the action list.
- SALT note made only if the client itemizes.
- Action list dated, with 17 May 2027 for the PIR.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Texas Constitution Article 8. Read for Section 24-a. | https://statutes.capitol.texas.gov/Docs/CN/htm/CN.8.htm | 2026-11-13 |
| Texas Comptroller, Franchise Tax page. Read for the $2,650,000 threshold and the 15 May due date with the next-business-day rule. | https://comptroller.texas.gov/taxes/franchise/ | 2026-11-13 |
| Form 05-915, 2026 Franchise Tax Report Information and Instructions. Read for Items 1 to 9 for a single member LLC filing as a sole proprietorship (Schedule C line 3, line 6, Schedule D, Form 4797, Schedule E), annualized total revenue and no estimated tax. | https://comptroller.texas.gov/forms/05-915.pdf | 2026-11-13 |
| Public Law 119-21 (One Big Beautiful Bill Act), section 70120, via library/us/federal/figures.json (us.obbba.salt.cap-2026). Read for "in the case of any taxable year beginning in calendar year 2026, $40,400". | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |

Not yet confirmed: the 2027 franchise tax forms are not yet published; 2026 federal form line numbers are as given in the federal skills this one routes to.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-tx-return-assembly` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-tx-return-assembly. If neither is available, confirm every figure against the official source pages cited above before relying on it.
