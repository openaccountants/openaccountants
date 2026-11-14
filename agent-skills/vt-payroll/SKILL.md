---
name: vt-payroll
description: "Compute and administer Vermont employer wage withholding and UI for 2026, with W-4VT, current percentage tables, USD 15,400 UI wage base, new-employer rates, registrations and returns. Includes mandatory Child Care Contribution and distinguishes its employee deduction. Trigger on Vermont payroll, withholding, e-Services, unemployment and WHT-436."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/vt-payroll"
  jurisdiction: "US-VT"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Vermont payroll withholding and unemployment insurance, tax year 2026

> **Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant. General reference for AI-assisted working papers. A qualified professional must review the established facts and filing result. Circular 230 section 10.37: consider relevant facts and circumstances; do not assume missing facts or rely on audit risk.

**Answer first.** Use the 2026 Vermont withholding table for the actual pay frequency and W-4VT allowances. UI has its own annual USD 15,400 employee wage base and notice-assigned rate. The separate Child Care Contribution (CCC) applies to covered wages without that UI cap. [2026 tables](https://tax.vermont.gov/sites/tax/files/documents/GB-1210-2026.pdf); [UI base](https://labor.vermont.gov/unemployment-insurance/ui-employers/quarterly-reporting-taxable-wage-information); [CCC](https://tax.vermont.gov/business/child-care-contribution).

## Scope

Vermont employer withholding and unemployment insurance, plus the linked CCC required on covered payroll. Federal figures belong to `us-form-941-940-payroll`. Self-employed CCC and annual individual tax belong to `vt-income-tax`; do not use employee withholding allowances as annual-return deductions.

## Ask the client first

1. Entity, FEIN, state accounts, first Vermont employment and acquisition history.
2. Employee residence, work locations/days/hours and date remote work began.
3. W-4VT marital category, allowance count, requested extra withholding and actual payroll period.
4. Covered wages/benefits, year-to-date UI wages and supplemental/deferred payments.
5. UI rate notices and effective periods; foreign-construction classification if applicable.
6. Assigned deposit frequency, prior returns/payments and CCC employee-share election.

## The method, step by step

### Rates, bands and thresholds

| Item and condition | Amount, 2026 | Official source |
| --- | --- | --- |
| Weekly withholding allowance | USD 103.85 per allowance; subtract count times amount before weekly table | [2026 tables p.7](https://tax.vermont.gov/sites/tax/files/documents/GB-1210-2026.pdf) |
| Single weekly adjusted-wage bands | Up to 75:0;75-1,051:3.35% excess 75;1,051-2,438:32.70+6.6% excess 1,051;2,438-5,004:124.24+7.6% excess 2,438;above 5,004:319.25+8.75% excess 5,004 | [2026 percentage tables](https://tax.vermont.gov/sites/tax/files/documents/GB-1210-2026.pdf) |
| Married weekly adjusted-wage bands | Up to 226:0;226-1,855:3.35% excess 226;1,855-4,164:54.57+6.6% excess 1,855;4,164-6,227:206.96+7.6% excess 4,164;above 6,227:363.75+8.75% excess 6,227 | [2026 percentage tables](https://tax.vermont.gov/sites/tax/files/documents/GB-1210-2026.pdf) |
| Other payroll-period allowance amounts | Biweekly 207.69;semimonthly 225;monthly 450;quarterly 1,350;annual 5,400;daily 20.77; pair with corresponding official period table | [2026 tables](https://tax.vermont.gov/sites/tax/files/documents/GB-1210-2026.pdf) |
| UI taxable wage base, calendar 2026 | USD 15,400 per employee, up from 14,800 in 2025 | [UI reporting](https://labor.vermont.gov/unemployment-insurance/ui-employers/quarterly-reporting-taxable-wage-information) |
| General new employer, effective July 1,2026 | 1%; use earlier-period notice for Jan-June | [UI rate page](https://labor.vermont.gov/unemployment-insurance/ui-employers/unemployment-tax-rates) |
| Foreign construction new employers, effective July 1,2026 | NAICS 236:1.9%;237:4.0%;238:2.7%; other classification uses notice | [UI rate page](https://labor.vermont.gov/unemployment-insurance/ui-employers/unemployment-tax-rates) |
| CCC on covered wages | 0.44%; employee deduction optional up to 0.11%, leaving employer at least 0.33% (derived: 0.44% less 0.11%) | [CCC rules](https://tax.vermont.gov/business/child-care-contribution) |
| UI liability general screen | USD 1,500 wages in any quarter or one/more workers in 20 different weeks, current/prior year; special coverage/successor rules also apply | [UI coverage](https://labor.vermont.gov/employer-responsibility-unemployment-coverage) |

1. Register a withholding account in myVTax or BR-400. Separately determine UI liability and register through Department of Labor employer e-Services. Covered employers electronically report quarterly wages/contributions; successor, nonprofit, domestic and agricultural coverage differs from the general screen.
2. Request W-4VT. Determine Vermont taxable wages, marital table, allowance count and pay frequency. Subtract that period's allowance amount times count, apply the correct table and add requested Vermont extra withholding. Federal fallback is permitted by read instructions but may underwithhold; a current W-4VT supplies the state facts. For nonperiodic payments the 2026 instructions permit an estimate of 30% of federal withholding; nonqualified deferred compensation instead uses 6% of the deferred payment plus its associated income.
3. Nonresident employees working partly in Vermont: compute tax on full pay and multiply by Vermont hours/total hours. Vermont residents' full-pay withholding is reduced by tax withheld in the state where services were performed. Out-of-state employers' remote-work withholding rule begins after 30 days at a Vermont location; this does not mean the employee's underlying first 30 days' income is tax-exempt.
4. Compute UI separately per employee: taxable current wages = smaller of current covered wages or annual base less prior-year-to-date wages, not below zero. Multiply by the rate notice effective for the quarter. Do not assume the July 2026 new-employer rate applies to the first half or to foreign construction.
5. Compute CCC on covered wages at 0.44%; decide whether the employer absorbs it all or deducts at most 0.11% from employees. A voluntary courtesy withholding on wages physically outside Vermont that do not require Vermont withholding does not itself create CCC coverage. Report/remit with withholding on WHT-436. Self-employed CCC has its own individual-return route, not the employee UI base.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| UI base exhausted | Continue total-wage reporting but cap additional UI taxable wages |
| Foreign construction corporation | Use effective industry rate/notice, not general new-employer rate |
| Resident/nonresident work split | Apply the appropriate withholding localization rule; UI localization is a separate analysis |
| Nonprofit/domestic/agriculture/successor | Obtain coverage/rate determination; ordinary rate assumption may fail |
| Health-care contribution or special benefits | Separate eligibility and rate review; not assumed included in UI/CCC |

## Worked cases

**Case 1.** An invented employee earns USD 1,800 weekly, married with two W-4VT allowances and no extra withholding. Allowances are 207.70, adjusted wages 1,592.30. The married weekly first positive band yields(1,592.30-226)x 3.35%=USD 45.77. This uses the official period table, not annual-return tax bands.

```oa-check
name: Vermont2026 married weekly withholding
inputs:
  wages: 1800
  allowances: 2
steps:
  - allowance_deduction: allowances * 103.85
  - adjusted_wages: wages - allowance_deduction
  - withholding: max(adjusted_wages - 226, 0) * 0.0335
expected:
  allowance_deduction: 207.70
  adjusted_wages: 1592.30
  withholding: 45.77
```

**Case 2, employer CCC decision.** An invented employer with a verified 1% UI notice pays USD 5,000 covered wages after USD 14,000 prior-year-to-date wages. UI taxable wages are 1,400, so UI is 14. CCC is 22 on the full 5,000. Absorbing CCC costs 22; maximum employee deduction is 5.50, leaving employer 16.50. The election changes who funds CCC, not the 22 remitted. Year-to-date UI exhaustion does not cap CCC.

```oa-check
name: Vermont UI cap and CCC employee-share decision
inputs:
  wages: 5000
  prior_ui_wages: 14000
steps:
  - ui_taxable: min(wages, max(15400 - prior_ui_wages, 0))
  - ui_tax: ui_taxable * 0.01
  - ccc_total: wages * 0.0044
  - employee_max: wages * 0.0011
  - employer_if_split: ccc_total - employee_max
expected:
  ui_taxable: 1400
  ui_tax: 14
  ccc_total: 22
  employee_max: 5.50
  employer_if_split: 16.50
```

## When to refuse or refer

Refer disputed worker status, multistate UI localization, successor rate transfer, reimbursable employers, health-care contribution, unusual benefits and missing rate notices. Do not use a general withholding residency rule as a UI coverage determination.

## Filing and payment

Withholding frequency is assigned by the Department, generally matching federal frequency. Quarterly payers settle with WHT-436. Monthly payers pay by the 25 th following month, except January by February 23; the third month is settled on the quarterly return. Semiweekly: Wednesday-Friday pay dates deposit the following Wednesday; all other pay dates the following Friday. All employers file WHT-436 quarterly, ordinarily the 25 th following quarter. WHT-434 annual reconciliation and wage statements are due January 31, subject to business-day adjustments. The Department's published 2026 calendar gives January 25,2027 for Q 42026 WHT-436 and February 1,2027 for the annual reconciliation.

File directly with Vermont; the federal combined program does not substitute. Electronic filing is required with 10 ormore W 2/1099 s, semiweekly payments, payroll-service filing or prior-year withholding above USD 100,000, subject to stated extraordinary-circumstance relief. Reconcile state income tax, CCC, W 2/1099 totals and deposits, submit, save acceptance and verify payment posted to the proper account/period.

UI reports/payments use e-Services, due April 30,July 31,October 31 and January 31 after their respective quarters, moved to the next business day for weekends. UI reporting is electronic. The reporting page states delinquent interest 1.5% monthly/18% annually; verify any assessed penalties separately. Income-tax interest from another agency is not the UI rate.

Under [3202](https://legislature.vermont.gov/statutes/section/32/103/03202), late filing can attract 5% monthly/part up to 25% and a USD 50 minimum after 60 days, subject to reasonable-cause provisions. Applicable withholding/CCC late-payment and current interest require their own statutory-period calculation.

## Completion checklist

- Separate employer accounts and coverage/rate notices retained.
- Correct 2026 pay-period table/W-4VT used.
- UI cap and CCC coverage/share kept separate.
- Deposits, quarterly/annual returns and wage statements reconciled.
- Electronic acceptance and payment posting saved for both agencies.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 2026 withholding instructions/tables. Read for pay-period allowances, percentage tables, resident/nonresident rules, special payments, registration and annual wage reporting. | https://tax.vermont.gov/sites/tax/files/documents/GB-1210-2026.pdf | 2026-11-13 |
| Department withholding page. Read for deposit schedules, WHT-436/WHT-434, electronic requirements and 2026 calendar. | https://tax.vermont.gov/business/withholding | 2026-11-13 |
| Department CCC page. Read for covered wages,0.44% total and optional 0.11% employee share. | https://tax.vermont.gov/business/child-care-contribution | 2026-11-13 |
| Labor UI rate page. Read for July 2026 new/foreign-construction rates and experience notices. | https://labor.vermont.gov/unemployment-insurance/ui-employers/unemployment-tax-rates | 2026-11-13 |
| Labor UI reporting page. Read for 2026 wage base, quarterly electronic deadlines and UIinterest. | https://labor.vermont.gov/unemployment-insurance/ui-employers/quarterly-reporting-taxable-wage-information | 2026-11-13 |
| Labor UI employer coverage. Read for general and special-employer coverage screens. | https://labor.vermont.gov/employer-responsibility-unemployment-coverage | 2026-11-13 |
| Labor modernization resources. Read for employer e-Services registration/reporting route. | https://labor.vermont.gov/unemployment-insurance-modernization-employer-resources | 2026-11-13 |
| 32 V.S.A. 3202. Read for late filing and applicable tax-specific penalties. | https://legislature.vermont.gov/statutes/section/32/103/03202 | 2026-11-13 |

Not yet confirmed: January-June 2026 new-employer/foreign-construction rates and experience schedule must come from effective rate notices; no first-half rate is inferred from the July page. Special health-care contribution applicability/rate, UI penalty schedule, interstate localization, successor transfers and reimbursable coverage require separate confirmation.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `vt-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/vt-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
