---
name: to-payroll-social
description: "Reconcile Tonga 2026 PAYE, employee NRBF deductions and employer contributions using distinct earnings bases and confirmed minimum rates. Use for ordinary covered-adult payroll; disputed Fund age eligibility, remittance timing and atypical review-date calculations remain held."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/to-payroll-social"
  jurisdiction: "TO"
  tax_year: "2026"
  last_updated: "2026-11-22"
---

# Tonga Payroll and Retirement Contributions v0.2

**General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Prepare a Tonga 2026 PAYE and retirement-fund payroll reconciliation. Income tax and the National Retirement Benefits Fund (NRBF) use different legal bases, payment records and compliance calendars. Current minimum contribution rates are confirmed below; eligibility for disputed age groups, atypical review-date pay and the conflicting Fund remittance instructions remain explicitly unresolved.

Use the [individual income-tax skill](to-income-tax.md) for residence, employment-income inclusion/exemptions and current marginal tax bands. Do not copy a different band schedule into this skill or reduce the tax base automatically by a retirement deduction. This skill is not a blanket opinion that PAYE and NRBF exhaust every employment obligation.

| Item | Amount / rule and complete conditions | Official source |
|---|---|---|
| Member minimum contribution | 5% of each complete pa’anga of insurable earnings; confirm actual covered member/base and any additional voluntary amount. | [s 20 and Second Schedule](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2016/2016-0442/NationalRetirementBenefitsFundAct_3.pdf) |
| Employer minimum contribution | 7.5% of each complete pa’anga of insurable earnings after the first 5 years of implementation (5 in words on the page); employee and employer amounts stay separate. | [Second Schedule; current NRBF member accounts](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2016/2016-0442/NationalRetirementBenefitsFundAct_3.pdf) |
| Combined minimum | 12.5% derived as 5% +7.5% on the same proved eligible base; not all deducted from employee pay. | [Second Schedule; s 21](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2016/2016-0442/NationalRetirementBenefitsFundAct_3.pdf) |
| Fund earnings versus PAYE gross | Statutory earnings include remuneration, bonuses, commissions and allowances, but exclude overtime, gratuity, retrenchment/redundancy/termination, retirement benefits, sickness/maternity/work-injury payments, travel allowance/concession and employment-expense reimbursements. Verify the actual item. | [s 2 earnings definition](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2016/2016-0442/NationalRetirementBenefitsFundAct_3.pdf) |
| Review-date base | Regulations refer to annual salary applicable at 1 July review date; current Guide uses annual earnings at that review date. Do not substitute every item of current PAYE gross or invent a cap/floor. | [regs 2,4-5; current Guide panel 9](https://nrbf.to/download/resources/governance/3.%20NationalRetirementBenefitsScheme%28Administration%29Regulations2012.pdf) |
| PAYE monthly return/payment | Form 7 and PAYE within 28 days after month end; use current prescribed withholding method from the individual-tax owner. | [ss 76,82; MORC PAYE and due-date table](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2007/2007-0010/IncomeTaxAct_3.pdf) |
| Tax certificates/reconciliation | Form 4 within 14 days after the 30 June employment fiscal year ends, ordinarily 14 July, or within 7 days after employment ends during the year. Form 8 plus each Form 4 is due within 2 months after 30 June, ordinarily 31 August. | [Form 4 and certificate deadlines](https://www.revenue.gov.to/sites/default/files/inline-files/form4%20-%20annual%20tax%20witholding_1.pdf); [Income Tax Regulations reg 16](https://ago.gov.to/cms/images/LEGISLATION/SUBORDINATE/2608/2608-0004/IncomeTaxRegulations_2.pdf#page=17); [PAYE reconciliation](https://www.revenue.gov.to/paye) |
| Fund payer and recovery | Employer remits both parts; its own part cannot be deducted from employee wages. Employee deductions relate to the relevant pay period; failure-to-deduct and arrears have different statutory recovery rules. | [ss 20-23](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2016/2016-0442/NationalRetirementBenefitsFundAct_3.pdf) |

## Ask the client first

Obtain employer and employee TIN/NRBF registrations and identifiers; ages, employment contracts, employment dates, leave/termination and any complying-scheme/exemption evidence; salary/earnings at the July review date and all regular/variable cash/non-cash pay; the actual approved contribution base/schedule, voluntary elections and deductions; fiscal and payroll periods, current PAYE worksheet and Forms 4/7/8; prior returns, payment receipts, arrears and Fund/Ministry notices. Obtain residence/source facts before using employee tax bands.

## The method, step by step

### Establish Fund coverage and register the right population

Under NRBF Act s 19 an employer with at least 1 covered employee (1 in words on the page) and those employees are liable, subject to the Act and an actual exemption. Register using the Fund's employer/employee forms and supporting identity, business-licence/incorporation documents required by regs 12-18; obtain the membership/reference records. A lack of registration does not erase contribution liability from the date of insurable employment (s 23). For subcontract arrangements s 19(4) preserves principal-employer fallback liability if the responsible contractor defaults; obtain the actual contract rather than assume the invoice transfers all liability.

Apply First Schedule/s 57 exemptions to the actual facts: domestic employees/outworkers, casual workers, members of complying schemes, persons detained in prison/mental hospital, non-Tongan persons with Tonga diplomatic privileges, and the specified non-Tongan worker who supplies Board-satisfactory proof of actually contributing to a statutory national superannuation scheme abroad providing equivalent/better benefits than this Act. Casual-worker status requires all s 2 conditions: no ongoing expectation of permanent employment, no fixed hours, irregular working days and payment at the end of each work period; a casual label alone is insufficient. A private foreign policy or a foreign passport alone is not that proof. Obtain the actual certificate/decision for a complying-scheme or discretionary exemption. A general exemption assertion is not evidence.

The Act defines retirement age as 60, or an older age up to 70 which the employer notifies to the Fund for its employees. The current website/Guide membership age statement differs from the Act. Hold affected age-boundary classifications for the governing instrument; do not mark a 15-17-year-old exempt merely because the public page begins at 18. The worked cases use an already-confirmed adult covered member, so do not decide those disputed categories.

### Reconcile the two earnings bases

Prepare a pay-item schedule showing cash/non-cash employment income for PAYE and the separate NRBF statutory earnings treatment. Use Income Tax Act s 13 and actual benefit valuations/exemptions for tax. Use NRBF s 2 exclusions beside the contribution base. In particular, overtime can enter taxable employment pay while being excluded from Fund earnings; the word “gross” on a public summary does not override the statutory exclusions.

Apply the actual July review-date salary/earnings rule and contribution schedule; record both the annual basis and the amount allocated to the pay period. The Second Schedule rates are minimums after the initial implementation period. The older regulation's first-period employer 5% wording expressly refers to the Act's Schedule; the current Act's later-period 7.5% minimum and Fund guidance control that rate. Keep elected voluntary amounts separately. Do not invent a cap/floor, annual salary reset rule or rounding method for an atypical case.

Compute PAYE on its tax base using the prescribed period worksheet, then employee NRBF and authorized voluntary/other deductions for cash net pay. The employer bears its own contribution as an additional employer cost. Section 21 prohibits recovering that part from the employee. A missed employee deduction is not automatically recoverable in a later pay packet: read the s 21 failure-to-deduct rule against s 23's distinct arrears recovery/financial-hardship arrangement and obtain a Fund determination before recovering disputed arrears. Under reg 11 contributions are not payable during leave without pay; under reg 10 they cease with service. Under regs 19-20, notify the Fund within 1 month (1 in words on the page) after the employer ceases to be an employer or the registered employee ceases service, as applicable.

### File and reconcile PAYE separately

Complete Form 7 with every employee's gross wage details for the month and PAYE, including a nil withholding position where applicable. The employer withholds and remits under the current tax method; another payroll deduction does not reduce the employer's PAYE duty (ITA s 76(2)). Match the total employee ledger to the return and payment receipt. The old 15th-day tax deadline is replaced by the confirmed monthly rule above.

Issue each Form 4 with gross pay and tax deducted. The annual Form 4 uses the employment fiscal year ending 30 June, including for an employer with a different company balance date. File Form 8 with copies of all employee Forms 4 and reconcile to every monthly return and payment. The Ministry lists 31 August for the annual reconciliation. Refer any live form or period ambiguity before submission.

### Pay Fund contributions without inventing a grace period

Employer payment covers both employer and employee contributions and must carry the completed prescribed contribution schedule/forms (regs 7-9). Match employee/base/rate and month to the Fund receipt and member accounts; investigate rejected or unallocated payments. Use the Fund's actual official authorized channel and schedule; no account number or private credential is supplied here.

The sources disagree about when payment is due: the Act's monthly/end-of-employment language, the 2012 regulation's 10-working-day instruction (10 in words on the page) and the current Guide's 28-working-day instruction are not interchangeable. Record the conflict and obtain the governing current determination before advising a deadline or computing arrears; do not wait for the most permissive wording. The Act s 29 also uses 28 days following the month as a surcharge trigger, which does not by itself prove a working-day payment extension. Do not use the tax PAYE deadline as the Fund deadline.

## Boundary and exception table

| Situation | Treatment |
|---|---|
| Overtime, benefit, reimbursement or other atypical item | Resolve both tax and Fund classifications; one gross-pay number cannot settle both. |
| Foreign worker or other pension scheme | Obtain the precise First Schedule/Board qualifying proof or exemption certificate. |
| Employee outside the undisputed adult covered population | Resolve the statute/guidance age or retirement determination before classifying. |
| Late contributions or prior missed employee deduction | Reconcile actual due instrument, payments, recovery and hardship rules; no automatic employee recovery or surcharge bill. |
| Additional payroll tax/labour charge alleged | Obtain the actual law; the old “no separate general payroll tax” sentence is not an established current exemption. |

## Worked cases

Hypothetical TOP annual cash-pay examples for a confirmed covered adult with no exemption, voluntary amounts, other deductions or benefits. Salary is constant and its documented Fund earnings basis is the stated regular salary at the July review date; all bases are whole pa'anga. These do not establish monthly worksheet rounding or resolve disputed coverage/payment dates. Income-tax bands come from the linked [individual-tax owner](to-income-tax.md); Fund rates and exclusions from the sources above. Outputs are derived.

### Regular salary: employee deduction is not employer cost

Annual gross taxable salary and proved Fund earnings are TOP 24,000. Annual tax is TOP 1,200. Employee minimum Fund contribution is TOP 1,200 and employer minimum TOP 1,800. Cash net pay is TOP 21,600; total minimum Fund payment TOP 3,000; employer cost TOP 25,800. Deducting the entire Fund total from salary would wrongly shift the employer part to the employee.

```oa-check
name: Regular salary separates employee cash and employer contribution
inputs:
  annual_salary: 24000
steps:
  annual_paye: clamp(annual_salary - 12000, 0, 18000) * 0.10
  employee_fund: annual_salary * 0.05
  employer_fund: annual_salary * 0.075
  fund_remittance: employee_fund + employer_fund
  cash_net: annual_salary - annual_paye - employee_fund
  employer_cost: annual_salary + employer_fund
expected:
  annual_paye: 1200
  employee_fund: 1200
  employer_fund: 1800
  fund_remittance: 3000
  cash_net: 21600
  employer_cost: 25800
```

### Overtime: different Fund and PAYE bases

Regular annual salary is TOP 48,000 and overtime TOP 6,000. All TOP 54,000 is ordinary taxable cash employment income; the documented Fund base is TOP 48,000 because s 2 excludes overtime. Annual tax is TOP 5,600, employee Fund TOP 2,400 and employer Fund TOP 3,600. Cash net is TOP 46,000 and employer cost TOP 57,600. Treating overtime as Fund earnings would overstate the combined minimum contribution by TOP 750; taking the employee Fund contribution off taxable pay would also use the wrong PAYE base.

```oa-check
name: Overtime included for PAYE but excluded from Fund earnings
inputs:
  regular_salary: 48000
  overtime: 6000
steps:
  taxable_pay: regular_salary + overtime
  annual_paye: clamp(taxable_pay - 12000, 0, 18000) * 0.10 + clamp(taxable_pay - 30000, 0, 20000) * 0.15 + clamp(taxable_pay - 50000, 0, 20000) * 0.20 + max(taxable_pay - 70000, 0) * 0.25
  employee_fund: regular_salary * 0.05
  employer_fund: regular_salary * 0.075
  cash_net: taxable_pay - annual_paye - employee_fund
  employer_cost: taxable_pay + employer_fund
  wrong_combined_fund: taxable_pay * 0.125
  correct_combined_fund: employee_fund + employer_fund
  overstatement: wrong_combined_fund - correct_combined_fund
expected:
  annual_paye: 5600
  employee_fund: 2400
  employer_fund: 3600
  cash_net: 46000
  employer_cost: 57600
  overstatement: 750
```

## When to refuse or refer

Hold final payroll if residence, taxable benefit value, covered status, Fund base or period method is unresolved. Refer disputed age/exemption, arrears recovery, remittance timing and actual surcharge/penalty positions. Do not impose all contributions on employee pay or compute PAYE after deducting NRBF merely to match an old spreadsheet.

## Filing and payment

Keep PAYE returns, annual certificates/reconciliation and Fund schedules/payment records separate. Apply tax next-business-day rules to tax deadlines only. Check actual official accounts for accepted returns and allocated payments, retain receipts and reconcile employee/year-to-date totals. The unresolved Fund timing conflict remains an open item, not a successful filing.

## Completion checklist

Check registrations, employee classification, dual pay-item bases, current tax method, minimum/voluntary contribution splits, net pay, employer cost, actual accepted submissions and allocated receipts. Leave disputes and other labour/tax requirements open. No professional accountant approval is claimed.

## Sources

| Source and actual reading scope | Official URL | Read on |
|---|---|---|
| National Retirement Benefits Fund Act, Cap.8.08, 2020 consolidation: Read for s 2 earnings/employee definitions, ss 19-25,29,57,59,62 and First/Second Schedules, including exemptions and adjacent contribution provisions | https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2016/2016-0442/NationalRetirementBenefitsFundAct_3.pdf | 2026-11-15 |
| NRBF Administration Regulations 2012: Read for regs 1-21: review date, salary, contributions, payment, leave/cessation, registration and complying-scheme conditions | https://nrbf.to/download/resources/governance/3.%20NationalRetirementBenefitsScheme%28Administration%29Regulations2012.pdf | 2026-11-16 |
| NRBF Information Guide, revised 2025 and currently published: Read for complete two physical-page pamphlet, all numbered panels; rate/base/payment/age passages compared with law | https://nrbf.to/download/resources/pampflet/InformationGuide_Pamphlet_Eng%20revised%202025.pdf | 2026-11-16 |
| Current NRBF member information: Read for complete current member/voluntary/employer account and membership information | https://nrbf.to/ | 2026-11-16 |
| Income Tax Act, Cap.11.05, 2020 consolidation: Read for ss 13,22,26,76,82-86 and 89-90; no employee retirement deduction inferred | https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2007/2007-0010/IncomeTaxAct_3.pdf | 2026-11-15 |
| MORC PAYE: Read for complete withholding, Form 7, Form 4 and Form 8 procedure | https://www.revenue.gov.to/paye | 2026-11-16 |
| Income Tax Regulations reg 16(2)–(4) and MORC Form 4: Read for the certificate fiscal year and annual and cessation deadlines | [Regulation](https://ago.gov.to/cms/images/LEGISLATION/SUBORDINATE/2608/2608-0004/IncomeTaxRegulations_2.pdf#page=17), [Form 4](https://www.revenue.gov.to/sites/default/files/inline-files/form4%20-%20annual%20tax%20witholding_1.pdf) | 2026-11-22 |
| MORC Tax Due Dates and Extensions: Read for complete monthly/annual dates and weekend rule | https://www.revenue.gov.to/Tax-Due-Dates-and-Extensions | 2026-11-16 |
| Revenue Services Administration Regulations 2021: Read for regs 14-18 and 24-26, including payment receipts and weekends | https://www.revenue.gov.to/sites/default/files/inline-files/RevenueServicesAdministrationRegulations2021_FINAL_Eng_0.pdf | 2026-11-15 |

Not yet confirmed: NRBF eligibility/payment conflicts are unresolved for affected applications. The Act defines employee from age 15 up to the applicable retirement age, while current Fund guidance describes 18-70; do not exclude a 15-17-year-old from liability or certify an older-worker outcome from the website alone. The Act s 20(4) says end of month/last employment day, Administration Regulations 2012 reg 7 says 10 working days after month end, while the current 2025 Guide says 28 working days; no universal remittance/grace-period conclusion or automated late charge is authorized pending the current governing instrument. Confirm any later Board/Minister determination, salary-change/review-date application, cap/floor or rounding implementation and the actual contribution schedule before processing atypical pay. The old 5% employer/10% combined default is historical first-five-years material, not the current minimum. The old no-separate-payroll-tax assertion has not been established by an exhaustive current-law search. The old 15th-day PAYE and 31 March annual reconciliation dates are superseded by the confirmed tax filing rules. Exact periodic PAYE worksheet rounding, live portal/box mapping and any other employment/labour charge remain open. These examples are annual ordinary cash-pay reconciliations for a confirmed adult NRBF member with a documented insurable base, not a complete monthly payroll return.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-22. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `to-payroll-social` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/to-payroll-social. If neither is available, confirm every figure against the official source pages cited above before relying on it.
