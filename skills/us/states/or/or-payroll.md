---
name: or-payroll
description: "Oregon 2026 employer payroll: approved income withholding formulas, UI coverage and wage base, STT, TriMet/LTD, Paid Leave, WBF, combined registration/reporting and recomputing cases."
jurisdiction: US-OR
category: payroll
domain: tax
tax_year: 2026
tier: 2
type: computation
version: "0.3"
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Oregon payroll, 2026

> **General reference only.** This skill provides working papers and a filing brief, not accountant approval. Apply cited law to verified facts, identify assumptions and unresolved issues, and obtain qualified professional review before filing or acting. Circular 230 section 10.37 requires reasonable factual and legal analysis.

## Scope

Oregon (US-OR) employer payroll for wages paid in 2026: income tax withholding, employer UI, employee statewide transit tax, employer TriMet/LTD, Paid Leave Oregon contributions, Workers' Benefit Fund assessment, registration, reporting and employment-law boundaries. This skill is not an individual Form OR-40 tax calculator. Use `or-income-tax` for the owner's tax and individual deductions, `or-corporate-tax` for corporate excise/income tax and `or-cat` for commercial activity tax.

Federal payroll rates, wage bases, credits and deposit classification belong to `us-form-941-940-payroll`. Federal contractor classification belongs to `us-worker-classification-w2-vs-1099`. Do not import either as a substitute for Oregon coverage/classification. The ordinary employer scenarios below exclude equivalent Paid Leave plans, reimbursement employers and special exemptions unless expressly stated.

## Ask the client first

- Where does each employee reside and actually work, including homeworking, travel, out-of-state work and transit district addresses?
- What entity, owners/officers, worker duties, control, business evidence and program-specific exemptions apply?
- What OR-W-4 status/allowances, exemption dates, pay frequency, taxable wages and actual federal income tax withholding apply?
- What Oregon BIN, UI account/rate notice, current-employer year-to-date wages and predecessor/successor facts exist?
- What nationwide average headcount, Paid Leave plan/grant status, subject wages and WBF hours/coverage apply?
- What payroll dates, federal deposit schedule, prior reports/payments, hires/terminations and agency notices need reconciliation?

## The method, step by step

### 1. Register and separate coverage by program

Register the employer through Oregon combined employer registration and obtain the Business Identification Number before reporting; an FEIN alone is not the Oregon BIN. Add/change transit obligations when actual work locations change. Keep DOR withholding/transit, OED UI/Paid Leave and DCBS WBF account responsibilities distinct even though Form OQ combines reporting. Frances Online supports combined payroll reporting; Revenue Online supports DOR accounts/payments and OR-WR. A payment confirmation is not a filed quarterly report. [2026 combined payroll pp.4-9](https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf); [transit publication p.1](https://www.oregon.gov/dor/forms/FormsPubs/transit-payroll-taxes_211-503.pdf).

Ordinary UI coverage is generally triggered by at least $1,000 wages in a calendar quarter **or** one or more workers in each of 18 weeks in a calendar year. Agricultural coverage generally uses at least $20,000 cash wages in a quarter or ten or more workers in each of twenty weeks. Domestic coverage generally uses $1,000 cash wages in a quarter in the current or preceding year; domestic employers can use annual OA/132 or quarterly OQ/132. Apply actual exemptions, officer elections and reimbursement rules before taxing everyone alike. LLC members/partners and genuine independent contractors are not automatically UI employees. [OED payroll FAQ, subject/domestic/agricultural employers](https://www.oregon.gov/employ/Businesses/Pages/Frequently-Asked-Questions.aspx).

These are Oregon coverage thresholds, not federal FUTA rules. General, domestic, agricultural, nonprofit, governmental, tribal, public and special-industry employers must be classified before choosing a tax/reimbursement account. Federal/railroad/maritime exclusions, tribal elections and owner/officer rules require specific authority; they are referral gates, not blanket exemptions inferred from an entity label. [OED FAQ](https://www.oregon.gov/employ/Businesses/Pages/Frequently-Asked-Questions.aspx); [Paid Leave coverage](https://paidleave.oregon.gov/resources/common-questions.html).

### 2. Obtain the actual Oregon certificate

Use Form OR-W-4 for Oregon status, allowances, additional withholding and exemption. A valid pre-2020 federal W-4 used for Oregon may continue until a new Oregon certificate/change is needed. A later federal W-4 does not supply Oregon allowances. If there is no withholding statement or exemption certificate, withhold **8%**, rather than assuming single with zero allowances. A qualifying no-liability exemption requires both prior-year no tax liability and current-year expected no liability. [2026 formula pp.1-3,8](https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf).

Exempt certificates expire February 15 following the election year. Obtain the renewed certificate before February 15; absent renewal/statement, apply the 8% rule. A late valid exemption affects future wages; do not refund withholding from the gap merely because a new certificate arrives. Preserve certificate dates and changes. Extra withholding is applied as directed on OR-W-4. An income-tax exemption does not itself exempt STT, UI, Paid Leave or WBF. [Formula pp.2-3](https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf); [STT coverage](https://www.oregon.gov/dor/programs/businesses/pages/statewide-transit-tax.aspx).

Resident/out-of-state and nonresident/Oregon-service withholding require actual source facts. The 2026 combined booklet permits a nonresident withholding exception when annual Oregon earnings are below the applicable Oregon standard deduction; use the current individual amounts owned by `or-income-tax`, not a payroll formula allowance. Nonresident employees below that amount may request withholding because of other Oregon income. There is no blanket Oregon reciprocity certificate inferred here. Military/spouses, tribal and other statutory exemptions need their specific authority. [Combined payroll p.4](https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf).

### 3. Compute withholding from the approved 2026 formula

Determine Oregon taxable pay after applicable exclusions, annualize at the correct number of pay periods, and subtract the allowed actual **federal income tax withholding**, not FICA or federal tax liability. Apply the formula's payroll standard deduction and federal-withholding cap/phase-out, then its status/allowance table. Floor a negative result at zero, deannualize and add any per-pay extra withholding. Monthly, twice-monthly, biweekly, weekly and daily use the source's 12/24/26/52/260 annualization factors. Whole-dollar withholding rounding is optional for the percentage method. [2026 formulas pp.4-8](https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf).

The payroll deduction/allowance are inputs to withholding, not deductions/credits copied onto OR-40. Use the approved wage tables or approved software if implementing the full formula. A self-designed formula requires DOR approval. The source's explanatory page retains older $8,500/$256 text and an inconsistent $21,165/$1,798 example. Its explicit 2026 tables and internally recomputing calculation use $8,750/$263, $21,090 base and about $1,789 annual withholding in that example. Do not copy the stale arithmetic. [Formula pp.5-8](https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf).

| Item / condition | Rate, amount or threshold | Official source |
|---|---|---|
| No statement/certificate; expired exemption without renewal | 8% Oregon withholding until valid certificate treatment applies | https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf |
| Supplemental wages paid at a different time from regular payday | Optional 8% flat withholding; do not apply to every regular wage | https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf |
| Payroll standard deduction, formula only | Single/HOH fewer than 3 allowances: $2,910; single at least 3 allowances or married: $5,820 | https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf |
| Payroll allowance amount, formula only | $263 per allowed annual allowance; single wages >$100,000 or married wages >$200,000 force zero allowances | https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf |
| Federal withholding annual cap, single status | Below $125,000 wages: $8,750; $125,000-<130,000: $7,000; $130,000-<135,000: $5,250; $135,000-<140,000: $3,500; $140,000-<145,000: $1,750; at least $145,000: zero | https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf |
| Federal withholding annual cap, married status | Below $250,000 wages: $8,750; $250,000-<260,000: $7,000; $260,000-<270,000: $5,250; $270,000-<280,000: $3,500; $280,000-<290,000: $1,750; at least $290,000: zero | https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf |

Select the cap using **wages and certificate status**, not base wages or return AGI. A single claimant with at least three allowances uses the married deduction/formula but still the single federal-withholding phase-out. A married claimant electing higher single withholding uses the single phase-out/allowance limit. [Formula pp.7-8](https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf).

Let G be annualized Oregon taxable wages, F actual annualized federal income tax withheld limited by the applicable cap, A allowed allowances, and B = G - F - payroll deduction. The annual formulas below are copied as calculation structure, not a final individual tax chart. Clamp final withholding at zero.

| Item / condition | Rate, amount or threshold | Official source |
|---|---|---|
| G below $50,000, single fewer than 3 allowances; B $0-4,550 | 263 + 4.75% x B - 263 x A | https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf |
| Same; B >$4,550 through $11,400 | 479 + 6.75% x (B - 4,550) - 263 x A | https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf |
| Same; B >$11,400 through $50,000 | 941 + 8.75% x (B - 11,400) - 263 x A | https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf |
| G below $50,000, single at least 3 allowances or married; B $0-9,100 | 263 + 4.75% x B - 263 x A | https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf |
| Same; B >$9,100 through $22,800 | 695 + 6.75% x (B - 9,100) - 263 x A | https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf |
| Same; B >$22,800 through $50,000 | 1,620 + 8.75% x (B - 22,800) - 263 x A | https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf |
| G at least $50,000, single fewer than 3 allowances; B through $125,000 | 678 + 8.75% x (B - 11,400) - 263 x A | https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf |
| Same; B above $125,000 | 10,618 + 9.9% x (B - 125,000) - 263 x A | https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf |
| G at least $50,000, single at least 3 allowances or married; B through $250,000 | 1,357 + 8.75% x (B - 22,800) - 263 x A | https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf |
| Same; B above $250,000 | 21,237 + 9.9% x (B - 250,000) - 263 x A | https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf |

The official table labels overlap at exactly $50,000 gross wages and gives minimum base ranges for the upper table. Use an approved table/calculator/software for that boundary or unusual additional deductions rather than arbitrarily extending a formula. Regular wages and separately timed supplemental wages require the correct method. Pretax insurance/retirement deductions affect Oregon taxable wages as the source directs; different payroll programs can have different wage definitions. [Formulas pp.6-8](https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf); [Paid Leave subject wages](https://paidleave.oregon.gov/resources/common-questions.html).

### 4. UI: use the 2026 notice and this employer's annual base

| Item / condition | Rate, amount or threshold | Official source |
|---|---|---|
| 2026 UI annual taxable wage base per worker | $56,700 | https://www.oregon.gov/employ/Businesses/Pages/Current-Tax-Rate.aspx |
| 2026 UI schedule and ordinary experience range | Schedule 3; 0.9%-5.4%, use assigned employer notice | https://www.oregon.gov/employ/Businesses/Pages/Current-Tax-Rate.aspx |
| 2026 UI new-employer rate | 2.4% | https://www.oregon.gov/employ/Businesses/Pages/Current-Tax-Rate.aspx |
| 2026 special payroll tax offset, all four quarters | 0.135% of UI taxable wages, separately reported; not an additional tax or deduction from total UI due | https://www.oregon.gov/employ/Businesses/Pages/Current-Tax-Rate.aspx |
| 2026 Paid Leave subject wage limit | $184,500 per employee for Oregon contributions, as published by Oregon | https://www.oregon.gov/employ/Businesses/Pages/Current-Tax-Rate.aspx |
| 2026 Paid Leave combined contribution | 1% of subject wages; employee 60% of contribution, employer 40% when subject | https://paidleave.oregon.gov/resources/common-questions.html |
| Paid Leave employer-share gate | At least 25 employees on average, counting workers in and outside Oregon; smaller employers generally no employer share unless assistance-grant rule applies | https://paidleave.oregon.gov/resources/common-questions.html |
| 2026 STT | one-tenth of 1 percent (.001) of subject employee wages, no annual wage cap; employee-paid | https://www.oregon.gov/dor/programs/businesses/pages/statewide-transit-tax.aspx |
| 2026 TriMet employer payroll tax | 0.8237% of covered wages for services in district; employer-paid | https://www.oregon.gov/dor/forms/FormsPubs/transit-payroll-taxes_211-503.pdf |
| 2026 LTD employer payroll tax | 0.80% of covered wages for services in district; employer-paid | https://www.oregon.gov/dor/forms/FormsPubs/transit-payroll-taxes_211-503.pdf |
| 2026 WBF combined assessment | 1.8 cents per subject hour; employer at least half, employee no more than half | https://wcd.oregon.gov/laws/Documents/New_rules/070%20WBF%20-%20January%201%2C%202026/70-25054-rule-notice-and-rules.pdf |

Report all UI subject wages, excess over the annual base and taxable wages separately. Current-quarter taxable wages are max(0, min(current subject wages, annual base minus prior **same employer** taxable/subject wages used toward that base)). Use the actual rate notice, not the range or an old example rate. Do not label Oregon's wage base the highest nationally; that comparison is unnecessary and unverified. [OED rates](https://www.oregon.gov/employ/Businesses/Pages/Current-Tax-Rate.aspx); [OQ instructions pp.14-15](https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf).

A worker's unrelated prior employer wages do not automatically reduce this employer's UI base. Acquisitions, common paymasters and successors need their specific wage-transfer/account rules, not the ordinary unrelated-employer calculation. Keep successor facts for agency review and do not manipulate entities to obtain a lower rate. Oregon does not permit combined payroll reporting through a federal section 3504 common pay agent; that is a separate issue from a legally established wage-base transfer. The special payroll offset is entered separately on OQ box 25 and **must not be added to or subtracted from** UI due/total payment boxes. [Combined payroll pp.14-16](https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf); [OED FAQ](https://www.oregon.gov/employ/Businesses/Pages/Frequently-Asked-Questions.aspx).

### 5. STT and district employer taxes are different taxes

Continue STT at 0.1% for 2026 under DOR's current referendum update. It applies to Oregon resident wages wherever earned and nonresident wages for Oregon services, subject to exclusions, even when little or no personal income tax is withheld. It does not apply to self-employment income. An out-of-state employer paying an Oregon resident for services entirely outside Oregon may not be required to withhold; courtesy withholding and the employee's separate OR-STI obligation must be tested. Do not convert resident liability into an unlimited employer jurisdiction claim. [STT page](https://www.oregon.gov/dor/programs/businesses/pages/statewide-transit-tax.aspx); [2025 individual instructions, STT section](https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf).

For periods from 2023, ordinary employers report STT quarterly on Form OQ in Frances Online or approved paper reporting. Annual/older-period channels differ. Annual reconciliation is required; a zero income-tax withholding return does not prove zero STT. STT is employee-paid and the employer remits it. Employer failure to withhold can create liability and penalties; the STT page describes a $250-per-employee failure-to-withhold penalty capped at $25,000 per period. [STT reporting/penalties](https://www.oregon.gov/dor/programs/businesses/pages/statewide-transit-tax.aspx).

TriMet and Lane Transit payroll taxes apply to employer payroll for actual services inside district boundaries, including homeworking and traveling representatives, with the publication's exclusions. Neither is a separate employee TriMet deduction. Zip codes are screening aids, not complete boundary maps. Verify each address and allocate services before applying the employer rate; an entire metropolitan/county label is insufficient. [Transit publication pp.1-2](https://www.oregon.gov/dor/forms/FormsPubs/transit-payroll-taxes_211-503.pdf).

The publication exempts federal credit unions, public school districts, specified nonprofit/tax-exempt institutions except hospitals, specified insurers and domestic service. Certain local governmental/public districts exempt from LTD remain subject to TriMet. Check the exact category rather than assuming every nonprofit/public payroll is exempt from both. Boring, Canby, Sandy, Wilsonville, Molalla and Damascus have different historical deletion dates; current location and work dates matter. The old Cherriots levy and employee TriMet levy were not established by these official sources and are not usable charges. [Transit publication](https://www.oregon.gov/dor/forms/FormsPubs/transit-payroll-taxes_211-503.pdf).

Net self-employment district taxes are separate from employer payroll tax and from STT. Do not apply employer rates and wage definitions automatically to a sole proprietor's profit or treat owner draws as wages. Federal self-employment numerical rules remain in `us-schedule-c-and-se-computation`. Local SHS/PFA and any district self-employment filing need separate sourced work; they are not discharged by OQ. [Transit publication p.2](https://www.oregon.gov/dor/forms/FormsPubs/transit-payroll-taxes_211-503.pdf).

### 6. Paid Leave and WBF

Count average full-time and part-time employees in and outside Oregon for the Paid Leave employer-share gate, excluding temporary replacements for eligible employees on leave as the FAQ directs. Small employers still collect/remit employees' contributions and provide applicable job protection. At exactly 25 employees the ordinary employer share applies. A qualifying assistance grant can change a small employer's contribution obligation. Approved equivalent plans, elective self-employed/tribal coverage and employees working wholly outside Oregon need separate treatment. [Paid Leave employer FAQ](https://paidleave.oregon.gov/resources/common-questions.html).

The 1% combined contribution is 0.6% employee and 0.4% employer when the employer share is due, subject to the Oregon-published annual base. This is not 0.6% combined or 0.2% employee. Employers may voluntarily pay the employee share. Reconcile program-specific subject wages instead of treating every federal/UI wage exclusion alike. General leave entitlement, pregnancy-related additional leave, eligibility, notice and benefits are not inferred from contribution amounts. The FAQ describes general benefits up to twelve weeks, possible additional pregnancy-related time and job protection after ninety consecutive days, subject to its conditions. [Paid Leave FAQ](https://paidleave.oregon.gov/resources/common-questions.html).

For WBF, establish subject-worker coverage and assessment hours, then apply the 2026 combined cents-per-hour rate. It is not a percentage of wages and it is not workers' compensation insurance premium. Employers pay at least half and can pay all; employee deductions cannot exceed half. Use the rule/booklet for fractional hours, salaried workers, overtime and time not worked; do not treat a hypothetical 2,080-hour year as a statutory default. The rule permits a reasonable/contract method or its specified flat-hours method when actual hours are not tracked: 40 hours weekly or 173.33 monthly, with appropriate weekly/biweekly/monthly/semi-monthly application. Employee amounts are rounded each pay period to the nearest cent, with half cents rounded up; OQ total hours are rounded down to a whole hour and the reported assessment down to cents. Reconcile payroll deductions with the reporting calculation instead of assuming annual multiplication always equals the sum of rounded deductions. Report the source-prescribed whole hours and round total assessment down to cents as instructed. [2026 WBF rule](https://wcd.oregon.gov/laws/Documents/New_rules/070%20WBF%20-%20January%201%2C%202026/70-25054-rule-notice-and-rules.pdf); [WBF page](https://www.oregon.gov/dcbs/wbf/pages/index.aspx); [OQ WBF boxes](https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf).

### 7. Classification and final pay

ORS 670.600 is not the generic ABC test stated previously. For its listed tax/UI/workers' compensation/licensing chapters, establish freedom from direction/control over means and manner; an independently established business subject to the farm exception; required chapter 671/701 licenses; and responsibility for other necessary licenses/certificates. The independent-business test generally requires **three of five**: separate business premises (qualifying home space can count); risk of loss; services for two or more persons in twelve months **or** regular qualifying marketing; significant investment; and authority to hire/fire assistants. Each statutory subcondition matters. Entity formation alone does not establish independence. [ORS 670.600(2)-(5)](https://www.oregonlegislature.gov/bills_laws/ors/ors670.html).

A worker does not become a contractor merely by issuing invoices, having an LLC or working remotely. Different statutes can use different tests, including wage/hour law and federal employment tax. Refer classification where control/licensing or business-factor evidence is incomplete; document the facts rather than reducing every test to “outside usual course.” [ORS 670.600-605](https://www.oregonlegislature.gov/bills_laws/ors/ors670.html); federal owner `us-worker-classification-w2-vs-1099`.

Under the ordinary final-pay rule, discharge or mutual termination requires payment by the end of the next business day. A quit with at least 48 hours' notice, excluding weekends/holidays, normally requires the final day, or next business day if that day is a weekend/holiday. Less notice normally means within five business days or the next regular payday, whichever is earlier. Seasonal farm work, fair employment and collective agreements can have specific exceptions. Willful failure can trigger penalty wages; do not assume every late dollar automatically receives the maximum. [BOLI Paychecks, ORS 652.140 and penalty discussion](https://www.oregon.gov/boli/workers/Pages/paychecks.aspx).

## Boundary and exception table

| Facts | Action |
|---|---|
| No OR-W-4 / expired exemption without renewal | Apply sourced 8% rule, not assumed single-zero formula. |
| Wages exactly at a withholding table boundary | Use approved Oregon table/calculator; do not invent a tie rule. |
| Nonresident below ordinary withholding threshold | Test exception using individual deduction; STT and UI remain separate. |
| Unrelated prior employer | No automatic UI base credit; successor facts are different. |
| Remote worker in Portland/Eugene | Actual address/services determine district tax, not employer headquarters. |
| Self-employed draw | Not employee STT; analyze separate district/self-employed and elective leave rules. |
| Fewer than 25 workers | Employee Paid Leave collection ordinarily continues; check grants/plan. |
| “Contractor” with company registration only | Apply actual Oregon statutory factors and separate federal/wage-law tests. |
| Government, nonprofit, tribal, domestic, farm or special industry | Resolve each program's separate coverage/reporting before calculating. |

## Worked cases

### Case A: Acme Software LLC, J. Smith, Portland

Retain the former scenario's Oregon-resident employee living and working in Portland, Multnomah County, $120,000 annual wage, no bonuses and 2,080 actual subject hours. Assume all services are in TriMet, UI new-employer rate 2.4%, wages are subject to all listed programs, no prior wages at this employer and at least 25 average employees with no equivalent plan. Employer Oregon costs are UI $1,360.80, TriMet $988.44, Paid Leave $480 and WBF half $18.72: $2,847.96. Employee amounts other than income/federal withholding are STT $120, Paid Leave $720 and WBF $18.72: $858.72. The former employee TriMet charge is removed. Actual income withholding needs OR-W-4 and federal withholding, not salary alone.

```oa-check
name: Oregon Acme J Smith 2026 payroll
inputs:
  wages: 120000
  hours: 2080
steps:
  - ui: min(wages, 56700) * 0.024
  - trimet: floor(wages * 0.008237 * 100) / 100
  - leave_er: min(wages, 184500) * 0.004
  - leave_ee: min(wages, 184500) * 0.006
  - wbf_each: hours * 0.009
  - stt: wages * 0.001
  - employer_total: ui + trimet + leave_er + wbf_each
  - employee_other: stt + leave_ee + wbf_each
expected:
  ui: 1360.8
  trimet: 988.44
  employer_total: 2847.96
  employee_other: 858.72
```

### Case B: Willamette Designs Inc., M. Garcia, Eugene

Retain the Oregon-resident employee, $75,000 annual wages, 2,080 actual subject hours and thirty nationwide employees. Assume all services are in LTD, the actual 2026 notice assigns 1.8% UI, and ordinary Paid Leave coverage applies. Employer amounts: UI $1,020.60, LTD $600, Paid Leave $300 and WBF $18.72, totaling $1,939.32. Employee other amounts: STT $75, Paid Leave $450 and WBF $18.72, totaling $543.72. The 1.8% is a documented case assumption, not a new-employer rate.

```oa-check
name: Oregon Willamette M Garcia 2026 payroll
inputs:
  wages: 75000
  hours: 2080
  notice_ui_rate: 0.018
steps:
  - ui: min(wages, 56700) * notice_ui_rate
  - ltd: floor(wages * 0.008 * 100) / 100
  - leave_er: min(wages, 184500) * 0.004
  - leave_ee: min(wages, 184500) * 0.006
  - wbf_each: hours * 0.009
  - stt: wages * 0.001
  - employer_total: ui + ltd + leave_er + wbf_each
  - employee_other: stt + leave_ee + wbf_each
expected:
  ui: 1020.6
  ltd: 600
  employer_total: 1939.32
  employee_other: 543.72
```

### Case C: TechCorp Inc., K. Nguyen, Bend remote worker

Retain the Austin-headquartered employer, $150,000 annual wages, 2,080 actual subject hours and two hundred employees. Assume all work is physically in Bend, Deschutes County, no services in either district, ordinary UI new-employer rate and Paid Leave coverage. Oregon UI is $1,360.80, employer leave $600 and WBF $18.72, totaling $1,979.52. Employee other amounts total $1,068.72. The employer's Texas headquarters does not remove Oregon obligations for an employee physically working in Oregon; no TriMet/LTD is charged on these facts.

```oa-check
name: Oregon TechCorp K Nguyen location decision
inputs:
  wages: 150000
  hours: 2080
  district_wages: 0
steps:
  - ui: min(wages, 56700) * 0.024
  - district_tax: district_wages * 0.008237
  - leave_er: min(wages, 184500) * 0.004
  - leave_ee: min(wages, 184500) * 0.006
  - wbf_each: hours * 0.009
  - employer_total: ui + district_tax + leave_er + wbf_each
  - employee_other: wages * 0.001 + leave_ee + wbf_each
expected:
  district_tax: 0
  employer_total: 1979.52
  employee_other: 1068.72
```

### Case D: Acme, D. Park changes employers April 1

Retain annual salary $200,000 and $50,000 earned January-March at an unrelated former employer. Assume no successor/common-paymaster relationship and $150,000 April-December wages paid by Acme. Acme has its own full $56,700 UI base, yielding $1,360.80 at 2.4%. Subtracting former-employer wages would incorrectly produce only $160.80. At a level monthly $200,000/12 salary, Acme reaches its base during July, not mid-June. Same-employer prior wages or a proven successor rule would require a different workpaper.

```oa-check
name: Oregon D Park unrelated employer UI decision
inputs:
  new_employer_wages: 150000
  prior_unrelated_wages: 50000
  annual_salary: 200000
steps:
  - ui_correct: min(new_employer_wages, 56700) * 0.024
  - incorrect_base: max(56700 - prior_unrelated_wages, 0)
  - ui_incorrect: incorrect_base * 0.024
  - difference: ui_correct - ui_incorrect
  - months_to_base: ceil(56700 / (annual_salary / 12))
expected:
  ui_correct: 1360.8
  ui_incorrect: 160.8
  difference: 1200
  months_to_base: 4
```

### Case E: compute the published formula, not the stale example

An invented single employee with zero allowances has $25,000 annual taxable wages and $1,000 actual annual federal income tax withholding. Base is $21,090. The 2026 lower-gross-wage formula gives $1,788.875 annual withholding, or $149.0729167 monthly before optional rounding. If no certificate existed, the separately applicable 8% rule would instead withhold $2,000 annually. These are alternatives determined by certificate facts, not elective least-tax methods.

```oa-check
name: Oregon 2026 withholding certificate decision
inputs:
  wages: 25000
  federal_withheld: 1000
  allowances: 0
steps:
  - base: wages - min(federal_withheld, 8750) - 2910
  - annual_formula: max(941 + (base - 11400) * 0.0875 - 263 * allowances, 0)
  - monthly: annual_formula / 12
  - no_certificate: wages * 0.08
expected:
  base: 21090
  annual_formula: 1788.875
  monthly: 149.0729166667
  no_certificate: 2000
```

## When to refuse or refer

Refer incomplete work-location records, withholding certificate/annualization edge cases, conflicting classifications, successors/common paymasters, stock compensation, noncash benefits, multistate UI localization, tribal/public/nonprofit/agricultural coverage, equivalent Paid Leave plans and disputed final pay. Minimum wages, sick time, workers' compensation premiums, new-hire deadlines and local income taxes need their own current official authority before adding figures. Do not treat a combined return as proof of federal or wage-law compliance.

## Filing and payment

Income withholding deposits follow the federal deposit cadence as adopted by Oregon, including EFT when federal EFTPS use is mandatory; the federal classification thresholds are owned by `us-form-941-940-payroll`. New employers ordinarily deposit monthly until a lookback exists. A quarterly return date does not postpone an earlier deposit. Agricultural/household reporting has separate annual options; follow the actual account registration. [Formula pp.3-4](https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf).

For 2026 ordinary quarters, OQ/132 due dates are April 30, July 31, November 2, 2026 and February 1, 2027 (October 31 and January 31 move from weekends). File OQ while registered even with zero payroll; use the correct no-payroll option and numeric zero fields, not blanks. Do not submit employee detail/Schedule B unnecessarily for a no-payroll report. Frances Online is the combined reporting channel; approved paper forms remain available under the booklet's rules. [2026 combined payroll pp.3-9](https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf); [OED rates/report dates](https://www.oregon.gov/employ/Businesses/Pages/Current-Tax-Rate.aspx).

| 2026 reporting field | Reconciliation | Official source |
|---|---|---|
| OQ withholding column, boxes 1a-4a | Subject wages, withholding, prepaid amounts, net due | https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf |
| STT column, boxes 1b-4b | STT subject wages, tax, prepayments and due | https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf |
| TriMet boxes 5a-9a / LTD boxes 5b-9b | District wages x rate; tax rounded down to cents; subtract program prepayments | https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf |
| UI column, boxes 13a-22a | Subject wages less annual-base excess = taxable wages; box 19a tax, 20a prepaid, 21a penalty/interest, 22a due | https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf |
| Paid Leave column, boxes 13b-24 | Subject/excess/taxable wages; boxes 17/18 shares, 19b total, 20b prepaid, 21b penalty/interest, 22b due; boxes 23/24 out-of-state and replacement workers | https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf |
| Box 25, special payroll tax offset | UI taxable wages x quarter offset; informational allocation, not added/subtracted from UI total or combined payment | https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf |
| WBF boxes 27-31 | Assessment hours, rate, total assessment rounded down, prepaid and net due | https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf |
| Form 132 | Employee-level UI/Paid Leave subject wages and hours; reconcile to OQ | https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf |
| Oregon Schedule B | Withholding liability detail, not employee UI wage detail | https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf |
| Form OR-WR | Annual withholding/STT reconciliation, electronically through Revenue Online | https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf |

Do not use fabricated “Schedule TM/LTD/STT” fields. Reconcile OQ, employee Form 132 and withholding Schedule B as separate records. Retain accepted reports and each agency/payment allocation. Amend the affected OQ, Schedule B and/or Form 132 for the original period and reconcile credits/payments rather than applying an unexplained next-quarter net change. W-2/information returns have their own iWire submission and deadlines; a federal submission or OR-WR alone does not establish Oregon information-return compliance. [Combined payroll pp.8-9,14-17](https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf).

UI, Paid Leave, withholding/transit and WBF have different delinquency provisions. The 2026 booklet states UI interest of 1.5% per month or fraction and separate reporting penalties; do not apply a DOR annual income-tax interest rate to UI. Transit publication gives 5% unpaid tax, additional 20% for OQ over one month late, additional 25% after an unmet demand and 100% after three consecutive nonfiling years, subject to exact conditions. The UI reporting calculation in the booklet uses $11 per employee after the stated ten-day reporting trigger, minimum $100 and maximum $2,800; a no-employee report can have up to $100. Paid Leave has its separately identified reporting penalty and 1.5% monthly/fraction interest on unpaid contributions. Do not compound interest on prior interest or penalties under those instructions. Complete all-program penalty/fraud and relief calculations require dated notices and the program's own rules. [Combined payroll pp.11-13](https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf); [transit p.1](https://www.oregon.gov/dor/forms/FormsPubs/transit-payroll-taxes_211-503.pdf).

The 2026 combined booklet requires WBF payroll records for at least four years and other payroll records for at least six years after required reports are filed. Preserve records longer where an audit, correction or other rule requires. [Combined payroll p.7](https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf).

## Completion checklist

- Establish BIN, each program's coverage and actual services/location.
- Preserve OR-W-4 and compute 2026 approved withholding rather than return tax.
- Use the current UI notice and this employer's annual wage accumulation.
- Separate STT employee tax, district employer tax, leave shares and hourly WBF.
- Reconcile quarterly totals, employee detail, liability schedule, payments and annual reporting.
- Record final-pay/worker-classification referrals and unresolved deadlines or special regimes.

## Sources

| Official source / section read | URL | Read on |
|---|---|---|
| DOR 2026 Withholding Tax Formulas, all eight pages, revised December 31, 2025. Read for certificate default/expiry, approved annual formulas, caps, payroll deduction/allowance, deposits and negative-result treatment. | https://www.oregon.gov/dor/forms/FormsPubs/withholding-tax-formulas_206-436_2026.pdf | 2026-11-13 |
| DOR 2026 Combined Payroll Tax Report, pp.3-9,11-17. Read for current wages/rates, account channels, zero returns, OQ/132/Schedule B fields, special offset, rounding and program distinctions. | https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf | 2026-11-13 |
| OED Current Tax Rate, 2026 column and report calendar. Read for Schedule 3, range, new rate, base, offset and Oregon Paid Leave limit. | https://www.oregon.gov/employ/Businesses/Pages/Current-Tax-Rate.aspx | 2026-11-13 |
| OED Payroll Tax Frequently Asked Questions, employer/employee/domestic/agricultural sections. Read for coverage triggers and annual/quarterly domestic reporting. | https://www.oregon.gov/employ/Businesses/Pages/Frequently-Asked-Questions.aspx | 2026-11-13 |
| DOR Statewide Transit Tax, current rate/referendum and reporting sections. Read for 0.1% continuation, wage coverage, self-employment exclusion and failure-to-withhold penalty. | https://www.oregon.gov/dor/programs/businesses/pages/statewide-transit-tax.aspx | 2026-11-13 |
| DOR transit payroll publication, both pages, revised November 18, 2025. Read for 2026 TriMet/LTD employer rates, district work, exemptions, deleted areas and penalties. | https://www.oregon.gov/dor/forms/FormsPubs/transit-payroll-taxes_211-503.pdf | 2026-11-13 |
| Paid Leave Oregon common questions, employer/contribution/coverage sections. Read for 1% 2026 rate, 60/40 split, average headcount, small employer/grant/equivalent-plan boundaries and benefits routing. | https://paidleave.oregon.gov/resources/common-questions.html | 2026-11-13 |
| DCBS Workers Benefit Fund current page. Read for 2026 combined hourly assessment and OQ channel. | https://www.oregon.gov/dcbs/wbf/pages/index.aspx | 2026-11-13 |
| DCBS 2026 WBF rule notice and OAR 436-070, effective January 1, 2026. Read for combined assessment, employer/employee allocation and subject hours. | https://wcd.oregon.gov/laws/Documents/New_rules/070%20WBF%20-%20January%201%2C%202026/70-25054-rule-notice-and-rules.pdf | 2026-11-13 |
| ORS 670.600-605. Read for control, three-of-five independent business factors, licenses, farm exception and entity-formation limitation. | https://www.oregonlegislature.gov/bills_laws/ors/ors670.html | 2026-11-13 |
| BOLI Paychecks, final paycheck and penalty sections. Read for ordinary discharge/quit deadlines and special exceptions. | https://www.oregon.gov/boli/workers/Pages/paychecks.aspx | 2026-11-13 |
| DOR 2025 OR-40 instructions, STT individual section; 2025-2026 filing cycle. Read for separate individual transit reporting boundary. | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf | 2026-11-13 |

Not yet confirmed: exact $50,000 withholding table tie and unusual below-minimum base treatment; special stock/benefit and agricultural/household withholding cases; complete nonresident/military/tribal exemptions and multistate UI localization; current successor/common-paymaster wage transfers; government/nonprofit reimbursement and officer elections; equivalent Paid Leave plans, grants and complete benefit calculations; special WBF hour/coverage exceptions beyond the sourced flat-hours and rounding rules; exact 2026 iWire upload specifications, corrections, annual due-date relief and new-hire deadlines; local SHS/PFA and self-employment district calculations; minimum wage/sick-time/premium schedules and full all-program penalties/relief. The former employee TriMet charge, Cherriots rate, generic ABC description, “highest UI base” comparison and single-zero missing-certificate default are withdrawn as unsupported or incorrect.
