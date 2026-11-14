---
name: in-income-tax
description: "Indiana individual income tax in 2026 for residents and sole traders. Covers state and county tax boundaries, return selection, the 2026-only tips/overtime/vehicle-interest deductions and computation from reconciled taxable income. Final annual forms and detailed credit computations remain explicit gaps."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/in-income-tax"
  jurisdiction: "US-IN"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Indiana individual income tax v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick reference:** 2026 state individual rate 2.95%, with separate county income tax. IT-40 is for full-year residents; IT-40PNR handles part-year/nonresidents. Final annual 2026 forms were not confirmed. Built from the law; Not yet approved.

## Who this applies to

Indiana residents, including sole traders and pass-through owners, and nonresidents with Indiana-source income. Full-year residents generally file when gross income exceeds their exemptions; a refund return may still be useful below that threshold. A temporary absence does not automatically end Indiana legal residence. See [DOR individual overview](https://www.in.gov/dor/i-am-a/individual/individual-income-tax-overview/).

## Rates, bands and thresholds

| Item | Amount / condition | Official source |
|---|---|---|
| State individual AGI tax | 2.95% in 2026, on the reconciled Indiana taxable base | [Departmental Notice 1, page 2; IC 6-3-2-1](https://www.in.gov/dor/files/dn01.pdf) |
| Local income tax | Separate county tax; residence/principal-work county fixed as of January 1 | [Bulletin 32; IC 6-3.6](https://www.in.gov/dor/files/reference/ib32.pdf) |
| New tips/overtime/vehicle-interest deductions | State enactment applies only to tax year 2026; eligibility and state/local allocation must be checked separately | [Bulletin 128; IC 6-3-2-31 through 33](https://www.in.gov/dor/files/reference/ib128.pdf) |
| Annual individual deadline | April 15 after year-end; next business day for weekend/holiday | [Individual filing overview](https://www.in.gov/dor/i-am-a/individual/individual-income-tax-overview/) |

Do not use payroll withholding constants as the annual exemption calculation. County annual-return computation must use the tax year's CT-40/CT-40PNR, not simply the October payroll table. Load `in-payroll` for employer withholding.

## The base

Complete federal income in `us-federal-income-tax-return-1040`, and business income in `us-schedule-c-and-se-computation` where applicable. Federal figures have one home and are not repeated here. Reconcile federal income to Indiana add-backs, deductions and exemptions before applying the state rate; retain each adjustment's evidence. The [DOR forms catalogue](https://www.in.gov/dor/tax-forms/individual/current/) identifies Schedule 1 add-backs, Schedule 2 deductions, Schedule 3 exemptions, Schedule 5 credits and Schedule 6 offset credits, plus county schedules. Its available annual forms are labelled 2025; their line numbers are not presented as 2026 fields.

Under [Bulletin 128](https://www.in.gov/dor/files/reference/ib128.pdf), the 2026 qualified-tip deduction starts from the **allowable federal deduction**. Where exemptions exclude part of the tips, multiply it by qualified tips subject to the relevant Indiana state/local tax divided by qualified tips in federal AGI. Apply state and local ratios separately; no double deduction for tips already exempt. Overtime and vehicle-interest rules require their own allocation; they are not assumed identical to tips. Federal eligibility, caps and phaseouts remain with the federal owner skill.

| Boundary | Action | Source |
|---|---|---|
| Full-year Indiana legal resident | IT-40 | [DOR overview](https://www.in.gov/dor/i-am-a/individual/individual-income-tax-overview/) |
| Part-year or nonresident with Indiana income | IT-40PNR; determine income allocation before tax | [DOR overview](https://www.in.gov/dor/i-am-a/individual/individual-income-tax-overview/) |
| Full-year KY/MI/OH/PA/WI resident with Indiana wage-type income only | Consider IT-40RNR; other income can require IT-40PNR | [DOR overview](https://www.in.gov/dor/i-am-a/individual/individual-income-tax-overview/) |
| Resident with another state's income tax | Reconcile credits and state/local limits; do not erase county tax automatically | [Bulletin 32](https://www.in.gov/dor/files/reference/ib32.pdf) |

## Deadlines and filing

Select the return by residency, then attach required schedules and wage/income evidence. Use the tax year's authorized e-filing software or official paper forms; do not change a prior form's year manually. Make payments through [INTIME](https://intime.dor.in.gov/) with the right period/type and save acceptance and payment records separately. The [DOR current-form instructions](https://www.in.gov/dor/tax-forms/individual/current/) require Schedule 3, Schedule 7 and CT-40 with a resident IT-40, and other schedules when entries exist; final 2026 packet/line confirmation remains pending.

## Penalties and interest

Do not treat a filing extension as permission to leave tax unpaid. Numeric extension tests, penalties, annual interest and individual estimated-payment safe harbours were not verified for this skill and must be confirmed before calculating arrears or installments.

## Cross-border points

State wage reciprocity does not remove county tax. [Bulletin 32](https://www.in.gov/dor/files/reference/ib32.pdf) fixes residence/work county at January 1 and distinguishes residents' whole-income base from a nonresident's principal-county income. International, multistate business and complete nonresident allocation work require separate analysis.

## Two worked examples that recompute

**State component only.** Invented 2026 taxpayer has $40,000 of fully reconciled Indiana taxable income after all applicable adjustments/exemptions. The state component before credits is $1,180. County tax, credits and payments remain separate.

```oa-check
name: Indiana state component 2026
inputs:
  taxable_income: 40000
steps:
  state_tax: taxable_income * 0.0295
expected:
  state_tax: 1180
```

**Tip allocation boundary.** Invented eligible nonresident has an allowable federal tip deduction of $10,000, total qualified tips in federal AGI of $20,000, and only $15,000 subject to Indiana state tax after exemptions. The Indiana deduction is $7,500, not the full $10,000. At the state rate that reduces this component by $221.25 instead of $295; the $73.75 difference follows the legal allocation. Local tax needs its own ratio. Source: [Bulletin 128](https://www.in.gov/dor/files/reference/ib128.pdf).

```oa-check
name: Indiana 2026 qualified-tip allocation
inputs:
  allowable_federal_deduction: 10000
  total_qualified_tips: 20000
  state_taxable_tips: 15000
steps:
  state_deduction: allowable_federal_deduction * state_taxable_tips / total_qualified_tips
  state_reduction: state_deduction * 0.0295
  incorrect_reduction: allowable_federal_deduction * 0.0295
  difference: incorrect_reduction - state_reduction
expected:
  state_deduction: 7500
  state_reduction: 221.25
  incorrect_reduction: 295
  difference: 73.75
```

## Ask the client first

- What year, federal filing status, residence/domicile dates and return type apply?
- What were January 1 residence and principal-work counties?
- What federal income, Indiana sources, modifications and exemptions are documented?
- Are tips/overtime/vehicle-interest deductions, reciprocity or other exclusions involved?
- What other-state/local taxes, credits, withholding and estimates require reconciliation?

## Sources

| Source | URL | Read for | Read for on |
|---|---|---|---|
| DOR individual overview | https://www.in.gov/dor/i-am-a/individual/individual-income-tax-overview/ | Read for residence, filing test, return choice and general annual deadline | 2026-11-13 |
| DOR Notice 1, October 2026 | https://www.in.gov/dor/files/dn01.pdf | Read for the expressly stated 2026 individual AGI tax rate; withholding amounts not used as annual exemptions | 2026-11-13 |
| DOR individual forms catalogue | https://www.in.gov/dor/tax-forms/individual/current/ | Read for annual 2025 form labels, schedule purposes and required attachments; no annual 2026 form confirmed | 2026-11-13 |
| Bulletin 128, June 2026; IC 6-3-2-31 through 33 | https://www.in.gov/dor/files/reference/ib128.pdf | Read for pages 1-3 for 2026-only enactment, tip eligibility/proration, state/local differences and no double deduction | 2026-11-13 |
| Bulletin 32; IC 6-3.6 | https://www.in.gov/dor/files/reference/ib32.pdf | Read for pages 1-3 for county identity, resident/nonresident bases and reciprocity boundary | 2026-11-13 |

Not yet confirmed: final annual 2026 return/schedule lines, full add-backs/deductions/exemptions, complete county computation and credits, overtime/vehicle-interest allocation details, full IT-40PNR allocation, individual estimates, extension tests and penalty/interest schedules. The form-download host returned 403 for the available 2025 IT-40; no unread form has been treated as checked. No 2025 exemption amount is guessed forward into 2026.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `in-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/in-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
