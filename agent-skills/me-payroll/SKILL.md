---
name: me-payroll
description: "Maine 2026 employer payroll: W-4ME annualized withholding with surcharge, 941ME deposit/return rules, UI wage cap, assigned rates, CSSF/UPAF and ME UC-1."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/me-payroll"
  jurisdiction: "US-ME"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Maine employer withholding and unemployment, 2026

> **Built from the law. Not yet approved.** Written by Codex; this version has not been reviewed by an accountant. General reference only. Under Circular 230 section 10.37, apply the cited authorities to the actual facts and obtain qualified professional review before filing or acting.

**Answer first:** Compute Maine wage withholding using the revised August 2026 booklet and W-4ME. UI uses each employee's first $12,000 of annual covered wages; the published new-employer total is 2.54%, including CSSF and UPAF. These are separate employer obligations. [2026 withholding booklet](https://www1.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_wh_tab_instr_August2026.pdf); [2026 UI rate array](https://www.maine.gov/unemployment/docs/2026/employers/uitaxrates2026.pdf); [2026 ME UC-1](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_Form_ME_UC1_fillable.pdf).

## Scope

Ordinary Maine employee wage withholding and contributory employer unemployment reporting. Federal wage taxes, FUTA, federal deposits and federal 941/940 belong to `us-form-941-940-payroll`; do not restate federal wage caps/rates here. Nonresident/military wage exceptions, special coverage, reimbursing entities and payroll obligations beyond withholding/UI require separate review.

## Ask the client first

1. Employer identity/accounts, Maine workers/work locations, employee versus contractor facts, successor/related-employer status and UI liability determination?
2. Pay period/frequency, Maine-taxable wages, W-4ME status/allowances, extra withholding and supplemental payments?
3. Each employee's calendar-year UI wages before this pay, exclusions and predecessor wage history?
4. Actual 2026 UI notice with base rate/CSSF/UPAF and contributory versus reimbursing status?
5. Withholding lookback, prior-year combined Maine tax liability, filing notices and payroll/quarterly payment records?

## The method, step by step

1. **Register and establish coverage.** Obtain MRS withholding and UI employer accounts; federal registration alone is insufficient. For ordinary UI, paying at least $1,500 in a quarter or employing someone in 20 weeks in the current/prior calendar year generally creates liability. Successor, controlled-group, agricultural, domestic and federal-liability routes differ. Localize multistate employment using work location, base of operations, direction/control and residence in that order. [MDOL liability terms](https://www.maine.gov/unemployment/liability/). Obtain the actual determination rather than assuming an exemption.
2. **Annualize Maine wage withholding.** Use W-4ME, not the federal W-4 deduction entry. Multiply pay by N=52 weekly, 26 biweekly, 24 semimonthly, 12 monthly or 260 daily/miscellaneous. Allowance amount A = claimed allowances x $5,300. Missing/invalid W-4ME requires the booklet's single/no-allowance default; verify any claimed exemption and extra withholding. [2026 booklet, W-4ME and percentage method](https://www1.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_wh_tab_instr_August2026.pdf).
3. **Calculate payroll deduction D.** For single, D=$12,850 through annual gross G=$102,250, zero at G at least $177,250, otherwise 12850 x (177250-G)/75000. For married, D=$28,550 through G=$204,550, zero at G at least $354,550, otherwise 28550 x (354550-G)/150000. Follow the booklet's four-decimal intermediate convention. Payroll D differs from the final-return deduction; do not substitute it. Annual taxable amount T=max(0,G-A-D). [percentage method steps 1-4](https://www1.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_wh_tab_instr_August2026.pdf).
4. **Apply payroll bands and surcharge.** Use the table below, then add 2% of T above $1 million single or $1.5 million married. Divide annual withholding by N and round to nearest dollar, adding any W-4ME additional withholding for the pay period. Separate supplemental wages can use 5%; otherwise follow aggregation rules. [steps 5-6 and supplemental wages](https://www1.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_wh_tab_instr_August2026.pdf).
5. **Compute UI separately.** For each covered employee, this-period taxable wages=max(0,min(current covered wages,12000-prior calendar-year taxable wages)). Employer contribution = taxable wages x assigned base rate, plus CSSF and UPAF on the same base when applicable. Report total wages, excess wages and taxable wages separately; never withhold employer UI from the employee. Do not add CSSF/UPAF twice when using the published combined rate. [2026 ME UC-1](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_Form_ME_UC1_fillable.pdf); [2026 array](https://www.maine.gov/unemployment/docs/2026/employers/uitaxrates2026.pdf).

## Rates, bands and thresholds

| Annualized taxable wages T | Single annual withholding | Married annual withholding | Authority |
| --- | --- | --- | --- |
| First band | Below $27,400: .058T | Below $54,850: .058T | [2026 authority](https://www1.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_wh_tab_instr_August2026.pdf) |
| Middle band | $27,400 to below $64,850: $1,589+.0675(T-27,400) | $54,850 to below $129,750: $3,181+.0675(T-54,850) | [2026 authority](https://www1.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_wh_tab_instr_August2026.pdf) |
| Top band | $64,850+: $4,117+.0715(T-64,850) | $129,750+: $8,237+.0715(T-129,750) | [2026 authority](https://www1.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_wh_tab_instr_August2026.pdf) |
| Surcharge | .02 x max(0,T-1,000,000) | .02 x max(0,T-1,500,000) | [2026 authority](https://www1.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_wh_tab_instr_August2026.pdf) |

[August 2026 booklet, percentage-method table and note 1](https://www1.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_wh_tab_instr_August2026.pdf).

| UI 2026 item | Published amount | Authority |
| --- | --- | --- |
| Annual taxable wage base | $12,000 per covered employee | [2026 authority](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_Form_ME_UC1_fillable.pdf) |
| New-employer base / CSSF / UPAF | 2.23% /0.14% /0.17% | [2026 authority](https://www.maine.gov/unemployment/docs/2026/employers/uitaxrates2026.pdf) |
| New-employer combined total | **2.54%** | [2026 authority](https://www.maine.gov/unemployment/docs/2026/employers/uitaxrates2026.pdf) |
| Experienced base range / combined range | 0% to 6.29% /0.31% to 6.60%; use assigned notice | [2026 authority](https://www.maine.gov/unemployment/docs/2026/employers/uitaxrates2026.pdf) |
| Direct-reimbursing employers | CSSF/UPAF do not apply on ME UC-1; do not use ordinary contribution method | [2026 authority](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_Form_ME_UC1_fillable.pdf) |

[2026 UI array](https://www.maine.gov/unemployment/docs/2026/employers/uitaxrates2026.pdf); [2026 ME UC-1 lines 2-9](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_Form_ME_UC1_fillable.pdf).

## Boundary table

| Fact | Treatment or stopping point |
| --- | --- |
| Nonresident or military spouse | Determine Maine wage sourcing/exemption under current withholding instructions; do not use residence alone or assume reciprocity. |
| Supplemental pay / pensions / backup | Different methods and statements apply; this ordinary wage computation does not prepare pension/backup withholding. |
| Successor / reimbursing / agricultural / domestic / nonprofit | Confirm liability, predecessor wage treatment and actual notice; do not assign ordinary new-employer rate automatically. |
| Other payroll obligations | This skill computes withholding/UI only; paid-leave, wage-hour, workers' compensation and other contributions are outside its computation. |

## Worked cases

### Weekly wage withholding

Single employee, $1,000 weekly, two valid W-4ME allowances, no extra withholding. G=$52,000, A=$10,600, D=$12,850 and T=$28,550. Annual withholding is $1,666.625; divided by 52 and rounded, withhold **$32**. This reproduces the official method without importing the final-return deduction.

```oa-check
name: ME weekly wage withholding 2026
inputs:
  pay: 1000
  periods: 52
  allowances: 2
steps:
  - gross: pay * periods
  - allowance: allowances * 5300
  - taxable: max(0, gross - allowance - 12850)
  - annual: 1589 + (taxable - 27400) * 0.0675
  - withhold: round(annual / periods)
expected:
  gross: 52000
  allowance: 10600
  taxable: 28550
  annual: 1666.625
  withhold: 32
```

### UI cap reached during the quarter

A contributory new employer has an employee with $11,000 prior annual taxable wages and $3,000 new covered wages. Only $1,000 remains taxable. Base contribution is $22.30, CSSF $1.40 and UPAF $1.70: total **$25.40**. $2,000 new wages are excess. Use this only if the actual notice assigns the published new-employer rates.

```oa-check
name: ME UI cap and assessments 2026
inputs:
  prior: 11000
  wages: 3000
steps:
  - taxable: max(0, min(wages, 12000 - prior))
  - excess: wages - taxable
  - base: taxable * 0.0223
  - cssf: taxable * 0.0014
  - upaf: taxable * 0.0017
  - total: base + cssf + upaf
expected:
  taxable: 1000
  excess: 2000
  base: 22.3
  cssf: 1.4
  upaf: 1.7
  total: 25.4
```

## When to refuse or refer

Refer uncertain worker status/localization, nonresident/military exemptions, successor/reimbursement arrangements, special supplemental or nonwage payments, missing UI notice and prior-period corrections. Do not invent an assigned UI rate or treat final-return personal deductions as payroll inputs.

## Filing and payment

**Withholding:** All registered filers submit quarterly 941ME electronically unless hardship waiver, including zero returns, by the last day of the following month. For 2026, lookback July 1, 2024 through June 30, 2025 withholding of at least $18,000 requires semiweekly deposits; lower amounts generally quarterly. Wednesday-Friday pay deposits are due next Wednesday; Saturday-Tuesday pay next Friday, subject to holiday rules. The actual assigned schedule governs. Prior-calendar-year combined Maine tax liability at least $10,000 requires electronic payments and continues in later years. [booklet sections 4-7](https://www1.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_wh_tab_instr_August2026.pdf).

Submit W-2/1099 data electronically by January 31 following the calendar year, with weekend/holiday relief; paper copies are not accepted. W-3ME was discontinued after 2023; do not invent an annual reconciliation requirement. Amend 941ME as instructed rather than using the discontinued 941A-ME. [booklet information reporting](https://www1.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_wh_tab_instr_August2026.pdf); [2026 employment form index](https://www.maine.gov/revenue/tax-return-forms/employment-tax-returns-2026).

**UI:** File quarterly wage/contribution report ME UC-1 and pay by April 30, July 31, October 31 and January 31, subject to applicable calendar relief. Reconcile employee wage detail and monthly headcounts for the pay period including the 12th. The quarterly UI report and 941ME are distinct obligations. Confirm the employer's current electronic submission route/notice rather than filing duplicate reports in different systems. [MDOL employer FAQ](https://www.maine.gov/unemployment/employersfaq/index.shtml); [2026 ME UC-1](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_Form_ME_UC1_fillable.pdf).

## Completion checklist

Confirm accounts and work-state coverage; retain W-4ME; annualize correctly using payroll deductions and surcharge; apply employee-level UI cap and actual total rate; reconcile wages/payments; file 941ME, wage report and annual information data on their respective schedules; retain confirmations.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| 2026 withholding tables/instructions, revised August; read for percentage steps and all bands, W-4ME/default, supplemental, lookback/deposit, filing and information-return sections. | https://www1.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_wh_tab_instr_August2026.pdf | 2026-11-13 |
| 2026 employment form index; read for 941ME/UC forms and discontinued W-3ME/941A notices. | https://www.maine.gov/revenue/tax-return-forms/employment-tax-returns-2026 | 2026-11-13 |
| MDOL 2026 UI array; read for new/experience base, CSSF, UPAF and combined rates. | https://www.maine.gov/unemployment/docs/2026/employers/uitaxrates2026.pdf | 2026-11-13 |
| 2026 ME UC-1; read for annual wage cap, excess wages, contribution components, reimbursing exception and headcount. | https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_Form_ME_UC1_fillable.pdf | 2026-11-13 |
| MDOL employer FAQ; read for quarterly due dates, wage base, successors and reimbursing coverage. | https://www.maine.gov/unemployment/employersfaq/index.shtml | 2026-11-13 |
| MDOL liability terms; read for ordinary thresholds, special coverage and ordered localization tests. | https://www.maine.gov/unemployment/liability/ | 2026-11-13 |

Not yet confirmed: employer-specific assigned UI total and special coverage/exemptions; current electronic UI submission assignment; exact 2027 weekend/holiday filing calendar and special nonwage/military cases. This is not a complete payroll-compliance pack beyond withholding/UI.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `me-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/me-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
