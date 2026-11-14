---
name: in-payroll
description: "Indiana employer payroll in 2026: state and county withholding, WH-4/WH-47, WH-1/WH-3 filing, unemployment premiums and wage base, registration, electronic wage reports, classification and voluntary-payment decisions. Preserves legacy case topics while withdrawing unsupported labor-law and penalty claims."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/in-payroll"
  jurisdiction: "US-IN"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Indiana payroll withholding and unemployment v 1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick reference:** 2026 state withholding rate 2.95%; county identity is determined on January 1, but a published county rate can change during the year. UI is employer-paid on the first $9,500 annually; typical new-employer rate 2.5%, subject to the notice and special categories. Built from the law; Not yet approved.

## Who this applies to

Indiana employers withholding state/county income tax and employers with covered unemployment employment. Use `us-form-941-940-payroll` for federal payroll; no federal rates or wage bases are repeated. Use `in-income-tax` for annual personal returns.

Do not infer coverage from a contractor label. [DWD employee classification](https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/employer-qualifications-and-special-circumstances/employee-classification) requires the applicable control, outside-usual-business and independent-business conditions, including its commission-sales alternative. A 1099/contract alone does not decide it. The old alternative allowing any work outside the employer's premises is withdrawn. For registration, use [DWD's coverage questionnaire and ESS process](https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/employer-qualifications-and-special-circumstances/); the old universal $1 trigger is not used.

## Rates, bands and thresholds

| Item | 2026 amount and condition | Official source |
|---|---|---|
| State withholding | 2.95%; ordinary periodic taxable pay after the permitted WH-4 deductions | [DN 1 p.2; IC 6-3-2-1](https://www.in.gov/dor/files/dn01.pdf) |
| Nonperiodic/bonus pay | Compute without exemptions; apply state and applicable county rates | [DN 1 pp.1-2](https://www.in.gov/dor/files/dn01.pdf) |
| Personal exemption constant | $1,000 annually per qualifying WH-4 line 5 exemption; use the frequency table | [DN 1 p.2](https://www.in.gov/dor/files/dn01.pdf) |
| Additional dependent constants | $1,500 per qualifying line 6 dependent and separate qualifying line 7 first-time dependent exemption; adopted-child line 8 constant $3,000 | [DN 1 p.2](https://www.in.gov/dor/files/dn01.pdf) |
| UI annual taxable wage base | $9,500 per employee; employer-paid | [DWD rate computation; IC 22-4](https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/rate-computation/) |
| Typical new-employer UI rate | 2.50%; use the assigned notice; special construction, government and successor treatment differs | [DWD new-employer rates](https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/rate-computation/new-employer-premium-rate) |
| UI experience range, good standing | 0.50%-7.40%; maximum delinquent rate shown separately at 9.40% | [DWD rate computation](https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/rate-computation/) |
| UI quarterly report | April 30, July 31, October 31, January 31 for the preceding quarter; use current calendar/notice for nonbusiness-day adjustments | [DWD due dates](https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/wage-reporting-need-to-know/quarterly-report-due-dates) |
| WH-1 cycle | Annual at monthly average $83.33 or less; otherwise monthly through $1,000; early monthly above $1,000, subject to DOR's assignment | [DOR business FAQ](https://www.in.gov/dor/i-am-a/business-corp/business-faq/) |
| WH-1 monthly / early monthly deadline | 30 /20 days after month-end respectively; not the same as the 30th/20th calendar date in every case | [DOR business FAQ](https://www.in.gov/dor/i-am-a/business-corp/business-faq/) |
| WH-3 reconciliation | January 31 after year-end; calendar adjustments must be checked | [DOR withholding](https://www.in.gov/dor/i-am-a/business-corp/withholding/) |
| Voluntary UI rate buy-down offer | Eligible employers have 30 days from the merit-rate notice; pay the full offer using the correct ESS option | [DWD voluntary payments](https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/rate-computation/voluntary-payments) |

### Selected county withholding rates, effective October 1, 2026

The old selected-county topics are retained. This is the October notice, not a substitute for earlier-period notices or the annual CT-40 computation.

| County | State county code | Rate | Official source |
|---|---|---|---|
| Marion | 49 | 2.02% | [DN 1 p.5](https://www.in.gov/dor/files/dn01.pdf) |
| Lake | 45 | 1.50% | [DN 1 p.5](https://www.in.gov/dor/files/dn01.pdf) |
| Allen | 02 | 1.59% | [DN 1 p.5](https://www.in.gov/dor/files/dn01.pdf) |
| Hamilton | 29 | 1.10% | [DN 1 p.5](https://www.in.gov/dor/files/dn01.pdf) |
| St. Joseph | 71 | 1.75% | [DN 1 p.5](https://www.in.gov/dor/files/dn01.pdf) |
| Vanderburgh | 82 | 1.25% | [DN 1 p.5](https://www.in.gov/dor/files/dn01.pdf) |
| Tippecanoe | 79 | 1.28% | [DN 1 p.5](https://www.in.gov/dor/files/dn01.pdf) |
| Monroe | 53 | 2.14% | [DN 1 p.5](https://www.in.gov/dor/files/dn01.pdf) |
| Porter | 64 | 0.50% | [DN 1 p.5](https://www.in.gov/dor/files/dn01.pdf) |
| Vigo | 84 | 2.00% | [DN 1 p.5](https://www.in.gov/dor/files/dn01.pdf) |
| Madison | 48 | 2.25% | [DN 1 p.5](https://www.in.gov/dor/files/dn01.pdf) |
| Delaware | 18 | 1.50% | [DN 1 p.5](https://www.in.gov/dor/files/dn01.pdf) |
| Pulaski | 66 | 2.85% | [DN 1 p.5](https://www.in.gov/dor/files/dn01.pdf) |
| Dearborn | 15 | 1.40% | [DN 1 p.5](https://www.in.gov/dor/files/dn01.pdf) |

The state county code is not a FIPS code. The [notice](https://www.in.gov/dor/files/dn01.pdf) expressly applies rates to withholding periods beginning on/after October 1 and flags a changed Boone rate. January 1 determines **which county**; it does not freeze that county's percentage forever.

## The base

**Withholding method.** Collect WH-4 and its January 1 residence/work facts. For regular pay, subtract the published frequency constants for valid exemptions from taxable wages, floor at zero, then multiply by the state rate and applicable county rate. Nonperiodic pay uses no exemptions. DN 1 states Indiana does not adopt the federal no-withholding allowance under IRC 3402(n); the old generic prior/current-year-zero-liability exemption and February 15 renewal are not relied on. Source: [DN 1, pages 1-3](https://www.in.gov/dor/files/dn01.pdf). Final WH-4 extra-withholding field mapping remains pending because the form download did not open.

**County identity.** [Bulletin 32](https://www.in.gov/dor/files/reference/ib32.pdf), IC 6-3.6, fixes residence and principal-work county at January 1. A later move does not itself change the county liable for that year, including a move outside Indiana. A new WH-4 records changes for the following year. Nonresidents' principal-county income differs from residents' base. State reciprocity does not remove county tax.

**UI wages.** Track gross covered wages and remaining annual taxable wages per employee; apply the assigned rate to wages remaining below the cap. Wages above the cap still belong in the report. [DWD](https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/rate-computation/) states the employer pays premiums without employee deductions. Its delinquent-rate cost illustration is arithmetically inconsistent: $9,500 x 9.40% is **$893**, not its printed $902.50. Use the rate and wage base, not that printed product.

**Rate assignment.** [DWD new-employer guidance](https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/rate-computation/new-employer-premium-rate) gives typical 2.5%, government 1.6% unless reimbursing, and successor/predecessor rules. It lists construction separately; confirm the actual industry assignment. Merit eligibility requires both the stated consecutive-registration and wage-reporting lookback tests; a gap can restore new-employer treatment. Do not label 7.4% the universal delinquent ceiling.

**Worker classification.** [DWD's classification page](https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/employer-qualifications-and-special-circumstances/employee-classification) requires all three ordinary conditions: freedom from control in contract and fact; service outside the usual course of the recipient's business; and an independently established trade, occupation, profession or business. The old alternative of merely working outside the enterprise's premises is withdrawn. The page also provides a separate commission-only sales-agent route with its own conditions. A tax form or contract alone does not decide classification; do not substitute another agency's test.

## Deadlines and filing

1. **Register DOR withholding through INBiz.** Obtain the business's own account/EIN and use its assigned tax types. Create an INTIME logon with TID and LetterID or request the welcome letter. [DOR withholding](https://www.in.gov/dor/i-am-a/business-corp/withholding/) explains the account and periodic/annual returns.
2. **File WH-1 in INTIME for the correct period.** Reconcile state and county amounts to payroll, submit the return, schedule payment and retain both confirmations. Active periods need a return even with no tax. Follow the assigned annual/monthly/early-monthly cycle; the old semi-monthly $85,000 scheme is replaced. Annual WH-1 deadline conflicts in DOR materials remain below; obtain the issued account due date.
3. **File WH-3 and supporting wage statements.** Reconcile all WH-1 returns to state/county totals on wage statements and correct period errors. More than 25 withholding statements triggers mandatory electronic WH-3/statement filing under the DOR page; do not infer that every smaller employer is forbidden paper without checking the current rule. Retain the processing acknowledgment; an upload alone is not final acceptance. [DOR withholding](https://www.in.gov/dor/i-am-a/business-corp/withholding/) supplies electronic and bulk filing routes; use the current specifications before a bulk submission.
4. **Register UI separately in Uplink ESS.** The [DWD employer qualifications page](https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/employer-qualifications-and-special-circumstances/) identifies employer qualifications and account setup; DOR's account is not the SUTA account. File/report wages until DWD confirms closure or inactivation.
5. **Submit UI wages electronically.** Choose quarter/year. Up to 50 workers may use Manual Entry/Add Employee/Save and Close; more than 50 require File Upload. Submit Report, certify and select I Confirm. Use Nothing to Report for an active zero-wage quarter. See [DWD filing steps](https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/wage-reporting-need-to-know/submitting-quarterly-wage-reports). Separate electronic payment is required; receipt, not postmark, controls payment timing under [DWD due dates](https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/wage-reporting-need-to-know/quarterly-report-due-dates). Reports require electronic filing unless a waiver is approved, regardless of the old 25-worker claim. Do not reuse the old reversed UC-1/UC-5 descriptions.
6. **Report hires/rehire events.** [DWD's state directory instructions](https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/unemployer-insurance-employer-guide/new-hire-reporting) require electronic reporting within 20 days and describe job-title, occupation and starting-compensation fields. Follow that official page's designated reporting portal.

## Penalties and interest

Current withholding/UI penalty schedules, interest and personal-liability standards were not fully checked. The old approximate interest, three-year lookback, 1.5-times penalty, 100% fraud figure and SUTA-dumping penalties are not usable computations. Classify a late return, late payment, inadequate wage record and worker-classification issue separately before obtaining the applicable current assessment rule. [DWD classification](https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/employer-qualifications-and-special-circumstances/employee-classification) confirms additional contributions/interest/penalties can arise, without validating those old figures.

## Cross-border points

Residents of KY/MI/OH/PA/WI with qualifying Indiana wage-type income can claim state reciprocity; Illinois is not on that list. County liability is separate. The [DOR individual overview](https://www.in.gov/dor/i-am-a/individual/individual-income-tax-overview/) identifies reciprocal/nonresident return types, while [Bulletin 32](https://www.in.gov/dor/files/reference/ib32.pdf) preserves local liability. Under [Bulletin 33](https://secure.in.gov/dor/files/ib33.pdf), a qualifying worker files WH-47 with the employer to claim state reciprocity. Indiana encourages home-state withholding; that does not itself establish another state's legal registration duty. The bulletin separately preserves county withholding based on January 1 principal work. DN 1 also has a conditional 30-day nonresident relief rule and excluded occupations; inspect all conditions before withholding is stopped.

## Two worked examples that recompute

The existing fictional case names and businesses are preserved. Figures below are invented inputs with verified state values; none is a real person's record.

**Case 1: Alex Patel / NorthShore Capital LLC, IN-IL commuter.** Retain the $120,000 compensation and Lake County January 1 facts. On an assumed fully reconciled state base of $120,000, the 2026 state component before credits is $3,540. At the selected Lake withholding rate, the gross county illustration is $1,800. These are separate components. The old Illinois rate, automatic credit wipe-out, employer-no-nexus conclusion and required $1,800 estimate recommendation are withdrawn pending actual sourcing/credit/employer analysis.

```oa-check
name: Indiana Alex Patel separate state and county components
inputs:
  reconciled_state_base: 120000
  illustrated_county_base: 120000
steps:
  state_before_credits: reconciled_state_base * 0.0295
  county_illustration: illustrated_county_base * 0.015
expected:
  state_before_credits: 3540
  county_illustration: 1800
```

**Case 2: Indy Mechanical Services Inc., Marion payroll and UI.** Retain 8 employees, $40,000 monthly taxable payroll and an assumed actually assigned 2.10% UI rate. Assuming the $40,000 is after valid withholding deductions, state withholding is $1,180 and county $808, total $1,988. If all 8 have reached the annual UI base, total annual taxable wages are $76,000 and premiums $1,596. The assumed notice, not the typical new-employer rate, decides the UI computation.

```oa-check
name: Indiana Indy Mechanical payroll and annual UI
inputs:
  monthly_taxable_pay: 40000
  employees: 8
  assigned_ui_rate: 0.021
steps:
  state: monthly_taxable_pay * 0.0295
  county: monthly_taxable_pay * 0.0202
  total_withholding: state + county
  annual_ui: employees * 9500 * assigned_ui_rate
expected:
  state: 1180
  county: 808
  total_withholding: 1988
  annual_ui: 1596
```

**Case 3: Sandra Lee / RiverBend Pharma LLC, reciprocal Ohio resident.** Retain $80,000 wages and a qualifying January 1 Dearborn principal-work county. Assume state reciprocity is properly established and no other exclusion applies. State tax is zero on the reciprocal wages, but at the October Dearborn rate the gross annualized county illustration is $1,120, not the old $960. Actual periodic deductions and earlier-year notice rates must be applied; this is not an annual-return result. Ohio/Cincinnati taxes are routed to their own skills without figures.

```oa-check
name: Indiana Sandra Lee reciprocity does not remove county tax
inputs:
  illustrated_taxable_wages: 80000
steps:
  state_on_reciprocal_wages: illustrated_taxable_wages * 0
  county_illustration: illustrated_taxable_wages * 0.014
expected:
  state_on_reciprocal_wages: 0
  county_illustration: 1120
```

**Case 4: Hoosier Cleaning Co., contractor classification.** Retain 12 cleaners given routes/schedules/shirts, working solely for its clients and paid hourly without independent businesses. Under the cited DWD classification conditions, neither a contract nor a 1099 alone establishes independence. The old numerical penalty/lookback, federal relief and alleged Indiana settlement-program outcomes are unconfirmed; do not compute them from these facts.

**Case 5: Maya Cortez / ChartLogic Software LLC, county move.** Retain Hamilton residence on January 1 and a March move to Marion. The move alone does not replace Hamilton with Marion for that year. For invented $50,000 remaining taxable pay at the selected notice rates, Hamilton withholding is $550 versus $1,010 using Marion, a $460 overstatement. A published change to Hamilton's rate would still need implementation; identity and rate are different facts.

```oa-check
name: Indiana Maya Cortez county identity versus rate
inputs:
  remaining_taxable_pay: 50000
steps:
  hamilton: remaining_taxable_pay * 0.011
  incorrect_marion: remaining_taxable_pay * 0.0202
  difference: incorrect_marion - hamilton
expected:
  hamilton: 550
  incorrect_marion: 1010
  difference: 460
```

**Case 6: voluntary-payment decision.** Invented eligible employer has an official offer costing $500 to reduce the assigned rate from 3% to 2% on expected taxable payroll $100,000. Premium saving $1,000 less the offer yields $500 benefit. If only $20,000 taxable payroll is expected, premium saving $200 yields a $300 loss. Use the actual notice and full offer; DWD says submitted voluntary payments are nonrefundable and an insufficient offer payment does not obtain the reduction.

```oa-check
name: Indiana voluntary UI payment decision both ways
inputs:
  larger_payroll: 100000
  smaller_payroll: 20000
  old_assigned_rate: 0.03
  offered_rate: 0.02
  offer_cost: 500
steps:
  larger_net_benefit: larger_payroll * (old_assigned_rate - offered_rate) - offer_cost
  smaller_net_benefit: smaller_payroll * (old_assigned_rate - offered_rate) - offer_cost
expected:
  larger_net_benefit: 500
  smaller_net_benefit: -300
```

## Ask the client first

- What work/residence locations and January 1 counties apply, with actual days worked?
- What year/pay dates, wage types, WH-4 exemptions and reciprocity documents apply?
- What DOR cycle, UI coverage/rate notice, entity/industry and successor status exist?
- What gross wages and remaining annual UI wage bases are documented per worker?
- What filings, payments, corrections, voluntary offers and overdue periods exist?
- Are classification, military/nonresident relief or employment-law issues involved?

## Sources

| Source | URL | Read for | Read for on |
|---|---|---|---|
| DOR DN 1, effective October 1, 2026 | https://www.in.gov/dor/files/dn01.pdf | Read for all 5 pages for state rate, exemption constants, nonperiodic pay, county-period changes, conditional nonresident relief and selected county codes/rates | 2026-11-13 |
| DOR Bulletin 32; IC 6-3.6 | https://www.in.gov/dor/files/reference/ib32.pdf | Read for pages 1-3 for January 1 identity, moves, state/local distinction and resident/nonresident bases | 2026-11-13 |
| DOR Bulletin 33 | https://secure.in.gov/dor/files/ib33.pdf | Read for both pages for reciprocal wage types, WH-47 submission, local-tax boundary and home-state encouragement | 2026-11-13 |
| DOR business FAQ | https://www.in.gov/dor/i-am-a/business-corp/business-faq/ | Read for withholding cycle table and assignment letter process; annual due-date wording conflicts with other DOR material | 2026-11-13 |
| DOR July 2026 business handbook | https://www.in.gov/dor/files/new-small-business-handbook.pdf | Read for printed pages 19-21 for WH-4, WH-1/WH-3, electronic filing and cycle table; annual Jan 30 differs from calendar | 2026-11-13 |
| DOR withholding | https://www.in.gov/dor/i-am-a/business-corp/withholding/ | Read for registration, account access, zero returns, WH-3 and processing acknowledgment | 2026-11-13 |
| DOR individual overview | https://www.in.gov/dor/i-am-a/individual/individual-income-tax-overview/ | Read for reciprocal-state list and appropriate annual return types | 2026-11-13 |
| DWD rate computation | https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/rate-computation/ | Read for base, ordinary/delinquent rates and employer-paid condition; recomputed incorrect printed maximum product | 2026-11-13 |
| DWD new-employer rates | https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/rate-computation/new-employer-premium-rate | Read for typical/special rates and consecutive-registration/wage-reporting lookback requirements | 2026-11-13 |
| DWD employer qualifications | https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/employer-qualifications-and-special-circumstances/ | Read for pre-registration questionnaire, ESS, zero returns and account closure | 2026-11-13 |
| DWD employee classification | https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/employer-qualifications-and-special-circumstances/employee-classification | Read for all contractor conditions, commission-sales alternative and distinction from other systems | 2026-11-13 |
| DWD quarterly due dates | https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/wage-reporting-need-to-know/quarterly-report-due-dates | Read for quarterly deadlines, all-employer electronic reporting/payment and receipt timing | 2026-11-13 |
| DWD report submission | https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/wage-reporting-need-to-know/submitting-quarterly-wage-reports | Read for manual/file thresholds, form fields, certification and nothing-to-report route | 2026-11-13 |
| DWD voluntary payments | https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/rate-computation/voluntary-payments | Read for eligibility, 30-day notice window, full-offer/ESS rules and nonrefundability | 2026-11-13 |
| DWD new hires | https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/unemployer-insurance-employer-guide/new-hire-reporting | Read 20-day electronic reporting and additional job/compensation fields | 2026-11-13 |

Not yet confirmed: annual WH-1 deadline conflict (DOR July 2026 handbook says Jan 30; calendar lists Jan 31); exact WH-4 extra-withholding fields, no-form defaults, retention and WH-47 retention/field requirements beyond the established certificate requirement; UI initial liability/coverage thresholds and the old universal $1-of-wages trigger; new-hire 60-day rehire definition; WH-1 U adjustment/refund workflow and exact W-2 locality-format claims; universal county adoption/history and highest-rate rankings; earlier 2026 county notices; complete short-stay/military/equity treatment and out-of-state employer/credit rules; current DOR classification test and numerical penalty/interest/responsible-person/SUTA-dumping rules; historical misclassification relief/settlement-program claims. Legacy employment-law topics remain unconfirmed: pay-frequency and 10-day rules, final pay, PTO and Naugle v. Beech Grove City Schools, liquidated damages, pay statements, direct deposit/pay cards, paid-sick/family-leave preemption, garnishments and workers compensation. No unsourced federal or other-state figures are retained. An ordinary WH-4 download returned 403. Verify calendar adjustments and actual notices before filing.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `in-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/in-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
