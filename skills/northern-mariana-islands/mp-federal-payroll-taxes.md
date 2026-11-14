---
name: mp-federal-payroll-taxes
description: How the federal payroll taxes apply in Northern Mariana Islands in 2026. Covers why social security (OASDI), Medicare and Additional Medicare Tax reach Northern Mariana Islands wages, who pays them, how they are reported (Form 941 to the IRS, Form W-2CM to the SSA and the CNMI Division of Revenue and Taxation (Finance.gov.mp)), whether FUTA applies, the government-service and immigration exceptions that differ by territory, and the mistakes to refuse. Rates and the 2026 wage base are in us-form-941-940-payroll. Trigger on "Northern Mariana Islands FICA", "Northern Mariana Islands social security tax", "Northern Mariana Islands Medicare tax", "Northern Mariana Islands Additional Medicare", "Northern Mariana Islands FUTA".
version: "1.0"
jurisdiction: MP
category: payroll
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: situation-rules
depends_on:
  - us-form-941-940-payroll
---

# Northern Mariana Islands: federal payroll taxes (social security, Medicare, Additional Medicare), 2026

> **Source-cited draft.** Folded from Ryan Duguid's Northern Mariana Islands reference files (mp-oasdi-annual-wage-base-reference, mp-medicare-ordinary-share-reference, mp-additional-medicare-annual-reference and mp-additional-medicare-employer-payment-reference); brought to the 2026 standard by Claude. Built from IRC sections 3101, 3102, 3111 and 3121, IRS Publication 15 (2026) and the Covenant (48 USC 1801). No accountant has reviewed it.

**Answer first.** Federal social security and Medicare (FICA) apply to wages for services in Northern Mariana Islands exactly as in the 50 states: the employer withholds the employee share, pays its own matching share, and reports both on **Form 941** to the IRS. The 2026 rates, the OASDI wage base and the Additional Medicare threshold are in `us-form-941-940-payroll` and are not restated here. What is specific to Northern Mariana Islands: not named in IRC 3121(e). Covenant s601(c) reads Code references to Guam as also referring to the Northern Mariana Islands (unless distinctly expressed otherwise or manifestly incompatible); federal income tax is **not** withheld (the territorial income tax is); FUTA **does not apply**; wages are reported on **Form W-2CM**.

## Scope

In scope: an ordinary private employer with employees working in Northern Mariana Islands, wages paid in calendar 2026: whether FICA reaches the wages, who pays, where it is reported, FUTA, and the territory-specific exceptions.

Out of scope, and where it goes:

| Topic | Skill |
|---|---|
| FICA rates, OASDI wage base, Additional Medicare threshold, Form 941 lines and deposit schedules | `us-form-941-940-payroll` |
| Territorial income tax withholding on wages | the Northern Mariana Islands payroll or income tax skill |
| Self-employment tax of Northern Mariana Islands residents | the Northern Mariana Islands income tax or self-employment skill |
| Employee or contractor | `us-worker-classification-w2-vs-1099` |

## Ask the client first

1. **Where each employee works**, and their citizenship, residence and immigration status.
2. **Who the legal employer is**: private, US federal agency, or the territorial government (and its retirement system).
3. **All wages paid in calendar 2026** by this employer, with noncash pay, tips and corrections.
4. **Other employers, predecessor or successor wages, common paymaster** and any totalization agreement.
5. **Forms 941 and deposits made so far**, and the wage statements filed.

## The method, step by step

### Rates, bands and thresholds

| Item | Rule or figure, 2026 | Source |
|---|---|---|
| Territorial link for FICA | Not named in IRC 3121(e). Covenant s601(c) reads Code references to Guam as also referring to the Northern Mariana Islands (unless distinctly expressed otherwise or manifestly incompatible); Covenant s606(b) applies the US social security tax and benefit laws as they apply to Guam, from 1 January 1987 (the calendar year after trusteeship ended on 3 November 1986, as amended by Public Law 98-213 s9) | [48 USC 1801, Covenant](https://uscode.house.gov/us/usc/119-124/t48/s1801/) |
| Social security and Medicare (FICA) | Apply to wages for services in Northern Mariana Islands as in the 50 states; rates, OASDI wage base and Additional Medicare threshold for 2026 are in `us-form-941-940-payroll` | [IRS Publication 15 (2026)](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Federal income tax withholding | Does not apply to Northern Mariana Islands employers unless the employee is subject to US income tax withholding; the territorial income tax is withheld instead | same |
| FUTA (federal unemployment tax) | Does not apply to employers in Northern Mariana Islands | [IRS Publication 15 (2026), section 14](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Wage statement | Form W-2CM, with Form W-3SS (instructions from the CNMI tax department); Copy A to the SSA, Copy 1 to the CNMI Division of Revenue and Taxation (Finance.gov.mp) | [IRS Publication 15 (2026), Certain Information Returns](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Government service | CNMI government service needs its own 3121(b)(7) branch through the Covenant and the retirement-system facts; do not borrow Guam's or American Samoa's treatment. Medicare for government service follows 3121(u) separately. | [IRC section 3121(b)(7) and (u)](https://uscode.house.gov/us/usc/119-124/t26/s3121/) |
| Residents of the Philippines working in the CNMI | Social security and Medicare must be withheld unless the worker holds H-2 status and meets 3121(b)(18) as read through the Covenant, or another section 15 exception applies; CW status is not H-2 | [IRS Publication 15 (2026), Residents of the Philippines working in the CNMI](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Federal employers in the CNMI | Withhold CNMI income tax (not federal income tax) under the 5 U.S.C. 5517 agreement of December 2006 | same |

### Steps

1. Confirm the service is in Northern Mariana Islands and the worker is an employee of this employer.
2. Test the special-service branches first (government service, immigration exceptions, family, student and the rest of 3121(b)); hold anything not resolved.
3. For ordinary covered wages, apply the 2026 FICA rates and the OASDI wage base from `us-form-941-940-payroll`: aggregate each employee's pay with this employer for the calendar year, apply the OASDI base once, apply Medicare to all wages, and withhold Additional Medicare only on wages over the threshold from the payment that crosses it.
4. Report on Form 941 (quarterly) and deposit under the schedules in `us-form-941-940-payroll`; no Form 940 is due for Northern Mariana Islands wages.
5. After the year, give each employee Form W-2CM, file Copy A with the SSA and Copy 1 with the CNMI Division of Revenue and Taxation (Finance.gov.mp).

## Boundary and exception table

| Situation | Treatment |
|---|---|
| The CNMI is said to be named in 3121(e), without the Covenant chain. | Refuse the shortcut. Cite Covenant ss601(c) and 606(b), with the intent qualification. |
| The 1976 "upon termination" wording, 3 November 1986 or 4 November 1986 is used as the social security start date. | Use 1 January 1987: Public Law 98-213 s9 changed s606(b) to 1 January of the following calendar year, subject to an earlier agreed date. |
| Philippine residence, CW status or the pre-2015 relief in Announcement 2012-43 is offered as a 2026 FICA exemption. | Refuse. CW is not H-2, the pre-2015 relief is historical, and nothing is inferred nil without the 3121(b)(18) conditions. |
| Territorial income tax adoption or territorial taxable income is offered as the FICA authority or base. | Hold. FICA is federal and its wage base is covered remuneration; the territorial income tax is a separate law and a separate skill. |
| Government, student, household, agricultural, fishing, family, nonresident-alien or other special service is present. | Hold the applicable 3121(b) branch, retirement-system and immigration facts; an OASDI exception does not settle Medicare (3121(u)). |
| Medicare or all FICA is capped at the OASDI wage base, or the OASDI total is used as the employment cost. | Refuse: the 3121(a)(1) ceiling applies only to OASDI (3101(a), 3111(a)); Medicare has no base limit. |
| Additional Medicare is matched by the employer, inferred nil below a threshold, or the employee asks to stop withholding at the joint-return threshold. | Refuse: the employer withholds 0.9% only on wages it pays over USD 200,000 in the calendar year, regardless of filing status; there is no employer match and no election. |
| Two components of one employee's pay are each capped separately. | Aggregate per employee, per employer, per calendar year, then apply the OASDI base once. |
| Other employers, predecessor or successor wages, common paymaster or a totalization agreement is present. | Hold the aggregation, successor and coverage rules; no exhausted cap or credit is inferred. |
| Noncash pay, tips, corrections, deferred compensation or an uncertain year of payment is present. | Hold 3121(c), valuation, the actual or constructive payment date (26 CFR 31.3121(a)-2) and lawful allocation. |

## Worked cases

The figures used below are the 2026 federal figures from `us-form-941-940-payroll` (OASDI 6.2% each up to USD 184,500; Medicare 1.45% each, no limit; Additional Medicare 0.9% withheld on wages over USD 200,000). Results are exact reference figures (derived), not rounded withholding.

**Case A: one employee, USD 150,000 plus USD 50,000 bonus, private employer in Northern Mariana Islands.** Aggregate to USD 200,000, cap OASDI once, Medicare on all; no Additional Medicare because wages do not exceed USD 200,000.

```oa-check
name: Northern Mariana Islands 2026 FICA, USD 200,000 aggregated wages
inputs:
  salary: 150000
  bonus: 50000
  oasdi_base: 184500
  oasdi_rate: 0.062
  medicare_rate: 0.0145
  addl_threshold: 200000
steps:
  - wages: salary + bonus
  - oasdi_each: min(wages, oasdi_base) * oasdi_rate
  - medicare_each: wages * medicare_rate
  - addl_wages: max(0, wages - addl_threshold)
expected:
  wages: 200000
  oasdi_each: 11439
  medicare_each: 2900
  addl_wages: 0
```

**Case B: the payment that crosses USD 200,000.** Wages paid to date by this employer are USD 195,000 and the next payment is USD 10,000. Additional Medicare is withheld on the USD 5,000 above the threshold in that payment (Ryan's position P06); there is no employer match, whatever the employee's filing status.

```oa-check
name: Northern Mariana Islands 2026 Additional Medicare, USD 195,000 to date plus USD 10,000
inputs:
  paid_to_date: 195000
  payment: 10000
  threshold: 200000
  addl_rate: 0.009
steps:
  - excess: max(0, paid_to_date + payment - max(paid_to_date, threshold))
  - addl_withheld: excess * addl_rate
  - employer_match: 0
expected:
  excess: 5000
  addl_withheld: 45
  employer_match: 0
```

Result: USD 45 withheld from that payment (derived). The employee's annual Additional Medicare liability (USD 200,000, USD 250,000 joint or USD 125,000 married filing separately) is settled on the employee's return and is not an employer test.

## When to refuse or refer

| Code | Trigger | Output |
|---|---|---|
| R-MP-FICA-SOURCE | The applicable law, coverage, covered wages, year or required history is unresolved | "I cannot complete this Northern Mariana Islands FICA request because the applicable law, covered remuneration or required facts have not been established. Obtain the missing evidence and have a qualified reviewer resolve it before calculation, withholding or filing." |
| R-MP-FICA-SCOPE | A filing-ready payroll, another programme or a government or special-service result is asked for | "This skill sets out how federal payroll taxes apply in Northern Mariana Islands. Complete payroll, territorial income tax withholding, prescribed outputs and professional review are not established here." |
| R-MP-FICA-RUNTIME | Verified recalculation or output tools are not available | "The required verified contribution calculation and output tools are unavailable. I cannot substitute chat arithmetic, static values or an incomplete file for the required financial outputs." |
| R-MP-FICA-AMBIGUITY | More than 10 grouped factual questions remain after reusing the evidence | "More than 10 grouped factual questions remain unresolved. Obtain the missing records with the reviewer before continuing." |

Refer territorial income tax withholding to the Northern Mariana Islands pack and anything about rates, deposits or Form 941 lines to `us-form-941-940-payroll`.

## Filing and payment

Form 941 each quarter to the IRS, deposits through EFTPS under the schedules in `us-form-941-940-payroll`; Form W-2CM to employees and Copy A to the SSA (SSA.gov/employer) by the due date in the General Instructions for Forms W-2 and W-3, Copy 1 with the transmittal to the CNMI Division of Revenue and Taxation (Finance.gov.mp).

## Completion checklist

- The service location, employer and employee status are established and evidenced.
- Each special-service branch in the boundary table is cleared or held.
- OASDI base applied once per employee and employer; Medicare on all wages; Additional Medicare only on wages over the threshold, from the crossing payment.
- Territorial income tax handled in the territory's skill, not here.
- Form 941, wage statements and Copy 1 accounted for.
- Nothing missing is treated as nil; holds are listed for the reviewer.

## Sources

| Source | URL | Read on |
|---|---|---|
| IRS Publication 15 (2026). Read for the territories' use of Pub. 15, the W-2AS, W-2CM, W-2GU, W-2VI and 499R-2/W-2PR forms and W-3SS, federal income tax withholding not applying to territorial employers, FUTA in section 14, the CNMI passages, and the 2026 FICA figures. | https://www.irs.gov/pub/irs-pdf/p15.pdf | 2026-11-14 |
| IRC section 3121 (House, through Public Law 119-124). Read for (a)(1), (b)(7)(B) and (D), (b)(18), (e)(1) and (e)(2) including the Puerto Rico citizen sentence, and (u). | https://uscode.house.gov/us/usc/119-124/t26/s3121/ | 2026-11-14 |
| IRC section 3101 (same edition). Read for (b)(2): 0.9 percent of wages over $250,000 (joint return), half that for married filing separately, $200,000 in any other case. | https://uscode.house.gov/us/usc/119-124/t26/s3101/ | 2026-11-14 |
| 48 USC 1801, Covenant (reproduced). Read for ss601(c), 606(b), 1003 and Proclamations 4534 and 5564. | https://uscode.house.gov/us/usc/119-124/t48/s1801/ | 2026-10-25 |
| Public Law 98-213 (97 Stat. 1459), s9. Read for the amended s606(b) start date (1 January of the following calendar year). | https://www.govinfo.gov/content/pkg/STATUTE-97/pdf/STATUTE-97-Pg1459.pdf | 2026-10-25 |
| IRS Announcement 2012-43, 2012-51 I.R.B. Read for the 3121(b)(18) H-2 exception in the CNMI and the pre-2015 relief. | https://www.irs.gov/irb/2012-51_IRB | 2026-10-25 |

Not yet confirmed: amendments after Public Law 119-124; Northern Mariana Islands government retirement-system coverage; any Northern Mariana Islands new hire registry or employer contribution of its own; whether the CNMI Division of Revenue and Taxation (Finance.gov.mp) sets its own Copy 1 deadline.
