---
name: to-income-tax
description: "Determine Tonga individual residence/source and compute ordinary annual employment-income tax using the current Ministry table for 2026 work. Reconcile certificates and refunds; route business/final-tax income separately and hold unresolved benefit, periodic-PAYE, treaty or live-form applications."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/to-income-tax"
  jurisdiction: "TO"
  tax_year: "2026"
  last_updated: "2026-11-16"
---

# Tonga Individual Income Tax v0.1

**General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Use for Tonga individual residence/source intake and ordinary annual employment-income tax during 2026, including the fiscal year ending 30 June 2026. The actual fiscal period, source and exemptions determine what enters the bands; the editing year does not turn a fiscal year into a calendar year. Current published bands are not described as a newly enacted 2026 schedule.

The resident gross-income rule includes worldwide non-exempt income; a non-resident includes only Tongan-source income. An individual physically working in Tonga can have taxable Tongan employment income even if paid offshore. Foreign-source employment taxed abroad has a specific exemption below. Separate/final non-resident payment taxes, companies and NRBF contributions use their own analysis, not a universal employee band calculation.

| Item | Amount / rule and complete conditions | Official source |
|---|---|---|
| Ordinary annual individual bands | TOP 0-12,000:0%; over 12,000 up to 30,000:10%; over 30,000 up to 50,000:15%; over 50,000 up to 70,000:20%; over 70,000:25%, marginal on each slice. Current Ministry schedule effective 1 July 2021. | [New Tax Rate -1st July 2021; ITA s 5](https://www.revenue.gov.to/paye) |
| Employee tax base | Gross employment income includes salary/wage, bonuses, allowances and benefits; no employment-expense deduction. Apply statutory exclusions/exemptions before the bands. | [ss 13,15-26; MORC Individual Employee](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2007/2007-0010/IncomeTaxAct_3.pdf) |
| Residence | Home in Tonga at any time, or 183 days aggregate in any 12-month period beginning/ending in the fiscal year, or Tonga government employee posted abroad; part-year arrival/departure rules apply. | [s 4(3)-(5)](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2007/2007-0010/IncomeTaxAct_3.pdf) |
| Individual fiscal year | 12 months ending 30 June; identify the actual fiscal period before annual calculation, not a calendar-year assumption. | [s 2 fiscal year](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2007/2007-0010/IncomeTaxAct_3.pdf) |
| Monthly PAYE | Employer withholds under prescribed method; Form 7 monthly list/return and remittance within 28 days after month end. No blanket 15th-day rule. | [Forms; ITA ss 76,82; MORC due-date table](https://www.revenue.gov.to/paye) |
| Employee certificate | Form 4 within 14 days after the employer financial year under Ministry guidance; shows annual gross pay and withheld tax. Annual withholding statement itself uses the statutory 30 June fiscal period. | [Withholding Tax Certificate; ITA s 86(1)](https://www.revenue.gov.to/paye) |
| Annual PAYE reconciliation | Form 8 plus each employee Form 4; within 2 months after 30 June under s 86, ordinarily 31 August; actual extension/next-business-day rules apply. | [s 86; MORC PAYE/Tax Due Dates](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2007/2007-0010/IncomeTaxAct_3.pdf) |
| Ordinary individual business return | Form 10; within 4 months after 30 June, ordinarily 31 October, subject to s 69 exemptions, actual notice and valid extension. Ordinary tax payment due with return. | [ss 68-69,72; MORC due-date table](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2007/2007-0010/IncomeTaxAct_3.pdf) |

## Ask the client first

Obtain the fiscal year, all homes and arrival/departure dates across adjacent years and rolling 12-month periods; government overseas posting and where duties were exercised; every employer and all cash/non-cash remuneration, termination/retirement amounts and reimbursement evidence; foreign-source employment and foreign tax/withholding proof; Forms 4, actual PAYE deductions and other income/withholding; any business, turnover, professional activity, CT registration and election notices. Obtain exemption evidence before removing any receipt.

## The method, step by step

### Establish residence, source and exempt receipts

Apply the three alternative residence tests in [s 4(3)](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2007/2007-0010/IncomeTaxAct_3.pdf). The 183 days can be consecutive or aggregated and the test can span the fiscal boundary. Home and government-posting tests are independent of day count. If resident now but not in the preceding fiscal year, residence begins with the first day present in Tonga; if resident now but not in the following fiscal year, it ends with the last day present, under ss 4(4)-(5). Obtain adjacent-year facts instead of declaring residence from the current year's count alone.

For residents, start with worldwide non-exempt income under s 11; for non-residents, Tongan-source only. Section 60(1) sources employment to duties exercised in Tonga wherever paid, or pay by/on behalf of the Tonga government wherever duties occur. Do not treat being below 183 days as an employment-tax exemption.

Under s 61, foreign-source employment received by a resident individual is exempt if foreign income tax was paid; foreign income tax withheld by the individual’s employer counts as paid. Identify duties/source first and retain foreign tax evidence. Taxable foreign-source income may instead involve s 62. Hold that credit calculation until a separate working paper establishes foreign tax paid, net taxable foreign income, average pre-credit Tonga rate, separate business/other classes, payment within the statutory 2-year limit and unused-credit restrictions; do not both exempt the same income and claim a credit for it. This employment-only example does not compute that credit.

Test actual statutory exemptions before calculating. Sections 15-24 address the King's income, specified diplomatic/international/statutory bodies, qualifying assistance agreements, certified non-profit non-business income, specified pensions, approved-fund retirement/death/migration/medical gratuities, resident-company dividends to resident members, approved retirement-fund receipts/employer contributions, scholarships subject to the associate exception and maintenance. The published 2020 amendment proposes s20A Legislative Assembly retirement-fund payout conditions, but the commencement condition is unresolved; this exemption is held under Not yet confirmed and is not an operative calculation instruction. These are conditional categories, not a blanket exemption for every pension, non-profit wage, scholarship or foreign project; obtain the actual instrument/approved status and refer an uncertain claim.

### Build gross taxable employment income

Under s 13 include salary/wages, leave/overtime pay, bonuses, commissions, fees, gratuities, taxable allowances, payments for entering/changing employment or restrictive covenants, termination payments, relevant pensions and valued non-cash benefits. Employer, associate, arranged third-party, past and prospective-employer payments can all count. A duty allowance solely spent performing duties and reimbursement of expenditure incurred on the employer's behalf in performing duties are excluded under s 13(1)(c)-(d); ordinary personal living costs relabelled as an allowance are not.

Value benefits using the actual First Schedule/current applicable ruling before annualizing. Do not deduct employment expenses or employee NRBF contributions from the tax base merely because they reduce cash pay: s 26(1)(b) and s 76(2) preserve the gross-base/withholding distinction. Approved employer retirement-fund contributions have their own s 22(2) employee-income exemption; confirm approved status. The examples below are cash pay with no unresolved benefit valuation.

### Apply marginal bands and reconcile withholding

Use the current Ministry bands above to the established annual base. Each rate applies only to its slice; the tax-free band is not a separate deduction taken again. Sum the slices, identify actual withholding that is creditable rather than final, and reconcile the annual tax to Forms 4 and Ministry records. Employment-only income from which PAYE was withheld can fall within s 69's return exemption, with finality under s 90; do not demand a Form 10 business return from every employee. Other income, an incorrect deduction, a notice or a repayment claim requires its actual filing route.

MORC identifies Form 9 for an employee excess-withholding refund, accompanied by the employee Form 4; short withholding can produce an assessment/demand and applicable charges. Keep claimed and approved refunds separate. For payroll-period deductions use the prescribed current PAYE worksheet/method linked on the official PAYE page, not the annual figure divided arbitrarily when pay is irregular or the period/rounding differs. Live worksheet mechanics are outside these annual cases.

### Separate an individual business from employee and company tax

The old pack mentioned simplified small-business tax without defining its population. ITA s 8 applies to a non-company business conducted solely in Tonga, not CT-taxable, with annual gross turnover below TOP 100,000; professional services are excluded and associates' turnover may be considered. There is a written approved election into normal profit tax and a 3-year restriction (3 in words on the page) before applying to return to small-business tax. This is not a right to compare two figures and switch on the return without approval.

Section 8/Third Schedule distinguish annual periods for turnover TOP 50,000 or less from quarterly 2%-of-turnover periods above that amount within the eligibility limit. MORC's sole-trader/professional/existing-election guidance and Forms 12-15 must be read with the Act, especially exactly TOP 50,000, which the website prose leaves between “less than” and “more than”. No company or CT-registered business uses this concession. Retain this route as an explicit intake/referral rather than apply the employee bands to gross business sales or claim every small business owes company tax. Complete business deductions, returns and election administration require the actual facts and approved forms.

## Boundary and exception table

| Fact | Required treatment |
|---|---|
| Fewer than 183 days in current fiscal year | Still test home, government posting, rolling 12-month and adjacent-year rules; no automatic non-resident/exempt conclusion. |
| Foreign salary | Determine actual source and foreign tax paid before s 61 exemption or s 62 credit. |
| Allowance/reimbursement/benefit | Establish statutory inclusion, performance-of-duties evidence and actual benefit valuation; no deduction by payment label. |
| Only employment/PAYE or final-tax income | Apply s 69/s 90 to the actual income mix; do not assume every person needs an annual business return. |
| Individual business or professional practice | Establish s 8 eligibility/election or normal profit-tax method; this annual employment calculation is not a complete business return. |
| Non-resident investment/technical/independent-service receipt | Route [corporate/withholding](to-corporate-income-tax.md) for classification; do not apply employee bands blindly. |

## Worked cases

Amounts are hypothetical TOP inputs and derived outputs. These are annual ordinary-income computations, with no unresolved benefits, part-year proration, treaty, loss or separate/final tax. They do not establish monthly withholding rounding.

### Ordinary employment: tax and refund reconciliation

Annual gross taxable employment income is TOP 50,000. Tax is TOP 1,800 on the next TOP 18,000 after the tax-free band plus TOP 3,000 on the next TOP 20,000, totalling TOP 4,800. Proved withholding is TOP 5,000, so the arithmetic excess is TOP 200. A refund still needs the actual Form 9/Form 4 application and approval.

```oa-check
name: Annual employment bands and excess-withholding reconciliation
inputs:
  taxable_employment: 50000
  withholding: 5000
steps:
  band_10: clamp(taxable_employment - 12000, 0, 18000) * 0.10
  band_15: clamp(taxable_employment - 30000, 0, 20000) * 0.15
  band_20: clamp(taxable_employment - 50000, 0, 20000) * 0.20
  band_25: max(taxable_employment - 70000, 0) * 0.25
  annual_tax: band_10 + band_15 + band_20 + band_25
  excess_withholding: withholding - annual_tax
expected:
  annual_tax: 4800
  excess_withholding: 200
```

### Foreign employment exemption changes the base

A full-year resident has TOP 60,000 of taxable Tonga employment and TOP 20,000 of genuinely foreign-source employment with proved foreign income tax paid. Section 61 excludes the foreign employment, so Tonga tax on the remaining TOP 60,000 is TOP 6,800. If that otherwise ordinary foreign employment had no qualifying foreign tax paid and no other relief, the TOP 80,000 base would yield TOP 11,300. The difference is TOP 4,500. This is a statutory eligibility comparison, not an election or a tax-credit claim on exempt income.

```oa-check
name: Foreign-source employment with versus without proved foreign tax paid
inputs:
  tonga_employment: 60000
  foreign_employment: 20000
steps:
  exempt_case_base: tonga_employment
  taxable_case_base: tonga_employment + foreign_employment
  tax_with_exemption: clamp(exempt_case_base - 12000, 0, 18000) * 0.10 + clamp(exempt_case_base - 30000, 0, 20000) * 0.15 + clamp(exempt_case_base - 50000, 0, 20000) * 0.20 + max(exempt_case_base - 70000, 0) * 0.25
  tax_without_exemption: clamp(taxable_case_base - 12000, 0, 18000) * 0.10 + clamp(taxable_case_base - 30000, 0, 20000) * 0.15 + clamp(taxable_case_base - 50000, 0, 20000) * 0.20 + max(taxable_case_base - 70000, 0) * 0.25
  difference: tax_without_exemption - tax_with_exemption
expected:
  tax_with_exemption: 6800
  tax_without_exemption: 11300
  difference: 4500
```

## When to refuse or refer

Hold calculation when rolling/adjacent-year residence, income source, foreign tax proof, benefit value or exemption conditions are missing. Refer complex business/special-industry, PE/treaty and disputed assessment positions. Do not choose a deduction, small-business election or employee filing obligation merely to reproduce an old approximate answer.

## Filing and payment

Monthly Form 7 is the employer's job. Obtain the employee Form 4 within the stated certificate period and reconcile gross pay and tax. Employer Form 8 plus all Forms 4 is ordinarily due 31 August for the 30 June withholding year; an individual's business Form 10 ordinarily by 31 October after 30 June. These are separate filings. The old 30 April company deadline belongs to the company skill only when its actual year end supports it.

Apply the next-business-day rule for a Saturday, Sunday or Tonga public holiday. Request a filing extension before the due date under RSAA 2021 s 11, show reasonable cause and keep the written decision. It can be granted only once, ordinarily for no more than 30 consecutive days unless exceptional circumstances justify longer; it does not extend tax payment. Use the current approved form and authorized submission/payment method, TOP amounts, actual TIN and correct period. Retain acceptance, certificate, assessment/refund decision and official payment receipt. Unverified portal/box mapping must remain open.

## Completion checklist

Confirm fiscal period, residence/source, exemption evidence, gross taxable pay, current marginal table, credit/finality/refund classification, actual form route and due date. Preserve all source documents and leave unresolved business or payroll/social applications explicitly pending. This research draft is not accountant approval.

## Sources

| Source and actual reading scope | Official URL | Read on |
|---|---|---|
| Income Tax Act, Cap.11.05, 2020 consolidation: Read for s 2 definitions, ss 3-14,15-26,37-38,60-63,68-69,72,76-86,89-91 and Third Schedule; full relevant employment/residence/exemption neighbors | https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2007/2007-0010/IncomeTaxAct_3.pdf | 2026-11-15 |
| Income Tax (Amendment) Act 2020: Read for all published ss 1-14 including conditional commencement, new 20A and procedure amendments; commencement not established | https://ago.gov.to/cms/images/LEGISLATION/AMENDING/2021/2021-0036/IncomeTaxAmendmentAct2020.pdf | 2026-11-15 |
| MORC PAYE: Read for complete current-rate, monthly return, certificate and annual-reconciliation instructions | https://www.revenue.gov.to/paye | 2026-11-16 |
| MORC Individual Employee: Read for complete current/old rate distinction, gross base/no deductions, certificate/refund/short-payment instructions | https://www.revenue.gov.to/individual-employee | 2026-11-15 |
| MORC Non Residents and Visitors: Read for complete individual residence, part-year, source and non-resident obligations | https://www.revenue.gov.to/non-residents-and-visitors | 2026-11-15 |
| MORC Small Business Tax: Read for complete eligibility, turnover rates, forms, periods and record instructions; exact 50,000 boundary resolved against s 8 | https://www.revenue.gov.to/small-business-tax | 2026-11-15 |
| MORC Tax Due Dates and Extensions: Read for complete monthly/annual and extension/weekend table | https://www.revenue.gov.to/Tax-Due-Dates-and-Extensions | 2026-11-16 |
| Revenue Services Administration Act 2021: Read for ss 9-13,33 and 1 commencement; filing extension versus payment distinction | https://www.revenue.gov.to/sites/default/files/inline-files/RevenueServicesAdministrationAct2021_1_4.pdf | 2026-11-15 |
| Revenue Services Administration Regulations 2021: Read for regs 14-18 and 24-26: TOP, payment receipt, quarter-linked interest formula and weekends | https://www.revenue.gov.to/sites/default/files/inline-files/RevenueServicesAdministrationRegulations2021_FINAL_Eng_0.pdf | 2026-11-15 |

Not yet confirmed: The published Income Tax Amendment Act 2020 and Consumption Tax Amendment Act 2020 make commencement conditional on the Revenue Services Administration Act 2020, whereas the recovered administration Act is named 2021. No official provision resolving that identity/commencement condition has been recovered; do not infer it from an index or passage history. The amendment-dependent s20A Legislative Assembly payout exemption is held; do not apply it or assume an opposite default without the operative instrument. The full post-2021 Income Tax rate Order has not been recovered; the current MORC table expressly effective 1 July 2021 is the primary published rate source used here, read 16 November 2026. No new 2026 thresholds are invented. Exact live eTax/form box mapping, complex benefit valuation/rulings, individual special-industry computations, treaty-specific outcomes and the administration of changed small-business classifications/elections require current supporting documents. The old monthly PAYE 15th-day and universal 30 April return claims are not current defaults. Administrative penalty amounts are withheld pending current RSAA 2021 Part 14 commencement; late-interest amount also requires the actual quarter-specific official lending-rate input. NRBF payroll deductions are not assumed income-tax deductions. The small-business paragraph supplies eligibility and routing, not a complete sole-trader filing opinion.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-16. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `to-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/to-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
