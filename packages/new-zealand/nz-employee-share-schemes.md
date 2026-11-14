---
name: nz-employee-share-schemes
description: >
  Use this skill for New Zealand employee share schemes (ESS) run through payroll from 1 April 2026: when an ESS benefit arises and its value, the taxing date, 2026 deferred shares, withholding PAYE and student loans on ESS income, employer funding of the tax, filing and payment dates, and the conditions for an exempt employee share scheme (purchase, value and participation limits, financing, hardship, restrictions and exit, employer deductions and annual disclosure, IR1211 and IR1212). Trigger on ESS, employee share scheme, share options, exempt ESS, IR1211, IR1212. PAYE generally is in nz-employer-payroll.
version: 1.0
jurisdiction: NZ
tax_year: 2026
last_updated: 2026-11-14
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# New Zealand employee share schemes through payroll, and exempt schemes (2026-27)

Figures are for tax year 2026, meaning payroll paid from 1 April 2026 to 31 March 2027 (the New Zealand 2026-27 tax year, which Inland Revenue calls the 2027 income year). All amounts are New Zealand dollars. Written by Ryan Duguid on his fork (ryanduguid/openaccountants, rules checked 12 and 13 November 2026) and imported on 14 November 2026. It has not been reviewed by an accountant.

## Scope and who this is for

This skill covers the payroll side of employee share schemes for a New Zealand employer in the 2026-27 tax year: establishing the benefit, its value and date, withholding and funding, filing and payment, and whether a scheme is an exempt ESS.

- **Companions:** PAYE codes and payday filing are in `nz-employer-payroll`; the employee's annual IR3 is in `nz-income-tax-ir3`.
- **Does not cover:** difficult valuations, replacement schemes, legacy approvals and historic transitions, scheme receipt failures and cross-border employees.

## Ask the client first

- Is the arrangement an employee share scheme at all, and is it an exempt ESS (with its initial notification filed)?
- What was granted, when, at what price, and what is the share value at the taxing date?
- Is the employee on a main or secondary code, and do they have a student loan?
- Has the employer elected to withhold PAYE on the benefit, and who funds the tax?
- Were any shares cancelled, sold back or bought under a loan?

## The method, step by step

1. **Establish the benefit first:** is there an ESS, and is it exempt?
2. **If exempt, test every condition** (purchase, value and participation, financing, hardship, restrictions and exit).
3. **If not exempt, value the benefit** at the taxing date.
4. **Withhold or report:** apply the withholding election, student loan rules and any employer funding.
5. **File and pay** on the dates set out below, and file the annual disclosure.

### Rates, bands and thresholds

Key figures for payroll paid from 1 April 2026 to 31 March 2027. The detail and conditions are in the sections below.

| Item | Figure | Condition | Source |
| --- | --- | --- | --- |
| Exempt ESS, market value of shares bought in a year | No more than $7,500 | Offers made on or after 1 April 2025; earlier offers $5,000 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/ |
| Exempt ESS, market value less employee spending in a year | No more than $3,000 | Offers made on or after 1 April 2025; earlier offers $2,000 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/ |
| Exempt ESS, required minimum spend | No more than $1,000 in a year | Limits the required minimum only | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/ |
| Exempt ESS, service requirement | No more than 3 years of full-time work | Or an accumulated equivalent | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/ |
| Exempt ESS, excluded holding | 10% or more of issued capital, with associated persons | Exactly 10% is excluded | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32494/ |


### Employee share schemes: establish the benefit first

These selected rules concern an established employee under a contract of service, with an ordinary New Zealand payroll code. Obtain the scheme and offer terms, employment connection, beneficiary and associate details, issue/transfer/vesting/cancellation dates, market values, consideration, any withholding election and the written funding agreement. An incentive labelled a share scheme is not enough. Section CE 7 requires an arrangement with a purpose or effect of issuing or transferring shares, connected to employment or service, and has exclusions for exempt ESS and the specified market-value arrangements. IS25/06 does not establish an independent contractor's or non-executive director's treatment. Section RD 7(1B), effective 21 February 2026, excludes its specified contractors and other statutory non-employees from extra pay. Resolve classification before applying this employee method. [S74](https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/employee-share-schemes/deducting-tax-on-ess-benefits), [S75](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-06.pdf?modified=20250331012659), [S78](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512798/), [S82](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519952/)

A scheme that always pays cash and never has a purpose or effect of issuing or transferring shares is ordinarily a phantom scheme with an ordinary cash bonus. A mixed cash/share award does not make its cash entitlement an ESS benefit automatically. For genuine cash settlement, establish that the payment is consideration for transfer or cancellation of shares or related rights and gives rise to a CE 2 benefit. Otherwise check the ordinary bonus rules, including ACC and KiwiSaver, separately. [IS25/06, paragraphs 5-13 and 38-48](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-06.pdf?modified=20250331012659)

### Exempt ESS: establish the scheme before excluding payroll

An amount derived from an exempt ESS is exempt income under CW 26B. CW 26C has 2 routes: a scheme with the Commissioner's approval under former DC 12 before its 2018 repeal, or the modern notified arrangement described below. A legacy approval, an IRD receipt or meeting the dollar limits alone does not establish every applicable condition. Keep the approval or notification, complete scheme terms, offer dates, employee/associate evidence, valuations, payments and annual returns. Actual legacy approvals and their continuing effect require separate review. [S100](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32342/), [S101](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/)

For the modern route, the Commissioner must have been notified under TAA 63B(1), the arrangement must meet CW 26C(2)-(9) and the Commissioner must have **received all forms due** under TAA 63B(2) and (3). Check receipt as well as submission. These provisions do not, by themselves, settle the timing or retrospective effect of a missed form or a later cure; obtain a specific determination before treating a non-compliant scheme as exempt or reclassifying earlier payroll. [S101](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/), [S106](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS32667/)

#### Purchase, value and participation conditions

For offers made **on or after 1 April 2025**, the increased limits apply for the **2025-26 and later income years**. A later purchase under an earlier offer does not establish that these limits apply. Section 27 of 2025 No 9 increased the share-value limit from $5,000 to **$7,500** and the discount limit from $2,000 to **$3,000**; earlier offers and other historical transitions need their own check. [S107, sections 2(34) and 27](https://www.legislation.govt.nz/act/public/2025/9/en/latest/)

| Condition | Required scheme provision or established input |
|---|---|
| Meaning of share | For CW 26C, CW 26F defines share, for a company whose shares are made available under an exempt ESS, as a **fully paid ordinary share** that **ranks equally with, and has the same designation as, an existing ordinary voting share** in the company. A partly paid share is not a share for CW 26C. Establish the offered shares' terms and designation. [S112](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32498/) |
| Price and annual amounts | Shares must be available for no more than market value at purchase/subscription. Shares purchased/subscribed for by the employee or a trustee for them have market value of no more than **$7,500 in a year**. That market value less the employee's spending on the shares is no more than **$3,000 in a year**. Aggregate the relevant purchases, rather than testing each grant in isolation. [S101, subsection (2)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/) |
| Meaning of year | YA 1 defines year as a **12-month period**. Establish the relevant period for the arrangement and its purchases; do not assume a fresh allowance on 1 April merely because the separate annual return uses a tax year. [S98](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520575/), [S101](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/) |
| Market value | CW 26DB imports YA 1 market value (a)/(b): a quoted share/option ordinarily uses the middle market quotation for the same terms, subject to the fair-reflection qualification; an unquoted one uses the arm's-length willing-purchaser amount, with a commercially acceptable, fair and reasonable valuation method. Appropriate income, cash-flow or asset methods may be relevant. CW 26DB also permits the **5-day volume weighted average price**, another Commissioner-accepted method or a comparable method for quoted shares/options. This guide does not establish an actual valuation or recognised-exchange status. [S98](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520575/), [S103](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS328941/) |
| Employee and ownership | CW 26D requires employment by the company. It excludes a non-employed director, a company/other body and a person who, with any associated person, holds **10% or more** of issued capital. Exactly 10% is excluded. Establish association and the relevant holdings; an employee's own holding below 10% is insufficient evidence. [S102](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32494/) |
| Equal participation | A full-time permanent employee receiving an offer must be eligible on an equal basis with **90% or more of other full-time permanent employees whose offers are not subject to foreign security disclosure rules**. If the arrangement applies to part-time employees or seasonal workers, apply the same statutory test separately to that class. Establish the actual comparison pool, foreign-disclosure qualification and equal terms, rather than using an unqualified whole-workforce percentage. [S101, subsection (3)(a)-(c)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/) |
| Minimum spending/service | A required minimum spend must be no more than **$1,000 in a year**; this limits the required minimum, not an employee's voluntary spending. Any service requirement must be no more than **3 years** of full-time work, or an accumulated equivalent for other employees. [S101, subsection (3)(d)-(e)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/) |
| Trust dividends | If a trust holds shares for an employee, the trustee must pay dividends directly to the employee and the dividends must be treated as derived by that employee. For CW 26C, CW 26G defines trustee as a group of persons appointed to administer an exempt ESS of a company that employs an employee, and to hold shares under that scheme on trust for the employee during any period of restriction described in CW 26C(7). Exemption of the scheme benefit does not establish exemption of dividends. [S101, subsection (3B)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/), [S113](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32500/) |

#### Financing, hardship, restrictions and exit

Where the employee must buy shares for **more than nominal consideration**, the arrangement must make a loan for their cost available or permit regular instalments at intervals of a month or less. Any purchase loan must be free of interest **and other charges**. Loans/regular instalments have terms of **36-60 months**. Loan repayments must be monthly or more frequent, with early repayment in full or part at the employee's discretion. For unpaid or parental leave lasting **more than a month**, regular instalments are suspended whilst on leave and the loan term is extended as appropriate; the direct-instalment alternative is also subject to that suspension provision. Keep this statutory extension qualification when testing the ordinary 60-month limit. [S101, subsection (4)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/)

If continued participation causes or may cause serious hardship, the arrangement must provide, **with the employee's agreement**, for payment terms to be varied or withdrawal with a **market-value** buyback on the withdrawal day, subject to repayment of the outstanding loan. Ordinary withdrawal instead requires **1 month's notice** and buyback at the **lesser of market value on that day and the employee's cost**, again subject to the outstanding loan. Do not use the hardship price merely because an employee wants to leave. [S101, subsections (5)-(6)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/)

For shares acquired below market value, the restriction period prohibits disposal except a takeover or similar share reorganisation. Its length is the **shorter** of (a) **3 years from acquisition or the loan repayment period, whichever is longer**, and (b) the period until employment ends with the employer, or the same-group employer following a transfer. A group transfer alone is not the stated employment-end event. For market-value acquisitions, the restriction is **no longer than** the shorter of that statutory period and an arrangement restriction ending on or after all loan repayment obligations cease. Preserve that separate market-value branch rather than imposing the discounted-share period on every purchase. [S101, subsection (7)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/)

At restriction end, a subsection (8) scheme may provide transfer if needed or, at the employee's choice, buyback at the lesser of cost and then market value. If the scheme does not use that option, subsection (8B) requires that choice for a current employee but requires the lesser-value buyback for someone no longer employed. Subsection (9) overrides both where employment ends through **death, accident, sickness, redundancy or retirement at normal retiring age**: transfer to the former employee/estate as appropriate or, if the employee chooses, the lesser-value buyback. Do not presume every resignation receives that protected-exit treatment. [S101](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/)

CW 26E defines normal retiring age as no less than **60**, with a **55** minimum for its specified female employee whose pre-**1 April 1978** employment contract entitles her to earlier retirement. It also allows an earlier age the Commissioner considers reasonable for the employment/business/occupation. Require the relevant contractual or Commissioner basis; an employee's chosen retirement date alone does not establish it. [S104](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32496/)

#### Employer deductions and separate annual disclosure

DV 28 denies a party to an exempt ESS a deduction for related expenditure/loss, **except to the extent incurred in establishing or managing the scheme**. That exception removes this particular denial; it does not, by itself, establish positive deduction entitlement under all other rules. Keep acquisition/funding costs separate from evidenced establishment/management costs. [S105](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS33459/), [S99](https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/exempt-employee-share-schemes)

Notify Inland Revenue using **IR1211**. The October 2026 blank form requests the registered company name, company IRD number and a signed declaration that the arrangement meets CW 26C(2)-(9). The current IRD process sends that form to its published exempt-ESS address. TAA 63B(1) does not state a fixed 20-day initial deadline; do not import the separate deferred-share deadline. [S106](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS32667/), [S108](https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/exempt-employee-share-schemes/report-exempt-ess), [S110](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1200---ir1299/ir1211/ir1211.pdf?modified=20261022002436)

For each tax year, provide the prescribed annual return **on or before 31 May following that tax year's end**. The October 2026 **IR1212** records the company, period start/end, **total value of shares granted, total employee contributions and number of employee recipients**. Reconcile those aggregates to individual scheme records and retain receipt evidence. The form's aggregate fields do not replace each employee's value/discount eligibility tests. IRD excludes exempt ESS benefits from ordinary employment information; use this separate disclosure process once exemption is established. An annual form submitted but not received is not sufficient evidence of the statutory receipt condition. [S101](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/), [S106](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS32667/), [S109](https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/exempt-employee-share-schemes/report-employee-shares-under-exempt-ess), [S111](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1200---ir1299/ir1212/ir1212.pdf?modified=20261022002438), [S85](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/employee-share-scheme-benefits)

### ESS value, taxing date and 2026 deferred shares

Determine the share scheme taxing date under CE 7B from the actual scheme conditions. It is ordinarily the earlier of qualifying beneficial ownership without the stated material risks/protections, or cancellation/transfer to a person outside the specified association. Subsection (2) ignores specified rights, including certain market-value transfer rights and immaterial risks. A vesting label or an ordinary disposal restriction alone does not establish the date. [S80](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS92763/)

Under CE 2, calculate **share value − consideration paid + consideration received − previous income** using the statutory definitions. If transfer/cancellation triggers the taxing date, do not add a market value as share value to the consideration received. Consideration can be paid or payable; replacement-scheme consideration and historic previous income have specific limits. A positive amount is a benefit; a negative amount is dealt with as a deduction under CE 2(3), not automatically negative payroll or a refund. Valuation evidence, historic transitions, replacement schemes and foreign-service allocation require their own actual-case checks. [S79](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512781/)

For shares issued or transferred on or after **1 April 2026**, EA 4B can defer the taxing date to a qualifying liquidity event. The issuing company must be unlisted and outside a group containing a listed company. Designate qualifying shares **at issue or transfer** and notify **both** the Commissioner and the beneficiary within **20 days**, or by a later date allowed by the Commissioner. An unlisted-company description or a late internal designation does not establish eligibility. [S81](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS1593301/), [S91](https://www.legislation.govt.nz/act/public/2026/8/en/latest/)

The liquidity date is generally the earliest relevant listing, sale/transfer to a person outside the specified association, or cancellation, including company cessation. If that event occurs during a restriction preventing disposal, use the restriction's end date. EA 4B(4)(c) excludes specified share-only exchanges into another qualifying unlisted company. Keep evidence for those conditions and exceptions rather than using every sale or group reorganisation as a trigger. The March 2026 IRD summary is shorter than the enacted conditions; it predates assent and is not an exhaustive eligibility test. [S81](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS1593301/), [S83](https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/employee-share-schemes/ess-rules/tax-on-employee-deferred-shares), [S91](https://www.legislation.govt.nz/act/public/2026/8/en/latest/)

### Withholding, student loans and funding

| Established payment or benefit | Selected employee payroll treatment |
|---|---|
| Genuine cash-settled CE 2 ESS benefit | Withhold income tax using the applicable extra-pay method; deduct student loan where required. The employer cannot elect out of mandatory cash withholding. No ACC earners' levy or KiwiSaver deductions/employer contributions on the ESS benefit itself. |
| Share-settled benefit | The employer can ordinarily choose whether to withhold. An offer or scheme term requiring withholding creates an irrevocable RD 7B obligation for that benefit/employee and replacement benefits. A valid election requires calculation, payment and timely employment-information disclosure. If withholding applies, use extra-pay income tax and any required student-loan deduction, with no ACC or KiwiSaver on the benefit itself. |
| Share-settled benefit with no withholding | Report where required; the employee deals with income tax through their annual return and provisional tax if applicable. No withholding does not mean tax-free income. |
| Separate employer payment to fund tax or student loan on a share benefit | This is separate extra pay, outside CE 2's ESS benefit value. Establish its income-tax, ACC, student-loan and KiwiSaver treatment independently; the ESS exemptions do not extend to it. |

Sources: [S74](https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/employee-share-schemes/deducting-tax-on-ess-benefits), [IS25/06, paragraphs 5-13 and 103-125](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-06.pdf?modified=20250331012659), [S77](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM7269557/), [S82](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519952/), [IS25/07, paragraphs 35-71](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-07.pdf?modified=20250331012754), [S88](https://www.legislation.govt.nz/act/public/2011/62/en/latest/). The 2025 interpretation statements' illustrative rates are not the 2026-27 rate tables.

Apply the selected extra-pay income-tax method above to the established ESS benefit using the **excluding-ACC** rate. For student loans, first establish the notified SL/TTC code or other required notice and any special deduction certificate. The ordinary primary-pay threshold is available only once in the pay period; secondary SL extra pay has no threshold. Use the complete-dollar and cent rules in the student-loan method above, rather than a universal percentage of every benefit. [S2](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S22](https://www.ird.govt.nz/calculate-lump-sum-paye), [S24](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments/calculate-paye-for-a-lump-sum-payment-end-of-employment), [S84](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments), [S88](https://www.legislation.govt.nz/act/public/2011/62/en/latest/)

Document who funds each deduction. An employee-funded tax payment, agreed sale of their shares or agreed deduction from net salary does not itself give the employee an additional employer-funded benefit. An employer-funded payment does. For the latter, first calculate the income tax and any student-loan amount on the ESS benefit that the employer agreed to fund, then gross up that **additional payment**, not the share value. IS25/07 gives **gross additional payment = net funding required ÷ (1 − combined funded deduction rates)**. Include only deductions the employer funds, at their actual applicable rates and bases. Recheck the extra-pay band, ACC cap, loan threshold/certificate, KiwiSaver base/rate and statutory rounding after grossing up; a single flat divisor is insufficient if any boundary changes. Establish compulsory employer contributions and ESCT separately. An agreement to fund income tax alone does not fund the employee's student loan or KiwiSaver automatically. [IS25/07, paragraphs 47-67](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-07.pdf?modified=20250331012754)

These rules do not authorise a wage deduction or share sale without the required agreement. For child-support or competing notices on an ESS benefit, obtain Inland Revenue's direction; do not extend the ordinary protected-earnings example automatically. [S74](https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/employee-share-schemes/deducting-tax-on-ess-benefits), [IS25/06, paragraph 19](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-06.pdf?modified=20250331012659)

### ESS income, filing and payment dates

Where CE 2(7)'s employment-information condition applies, CE 2(8)-(9) places income recognition on the **ESS deferral date, 20 days after the share scheme taxing date**. For qualifying employee deferred shares, first substitute the EA 4B liquidity date. A former employee's share benefit without withholding has the stated reporting exclusion and is ordinarily recognised on the taxing date, without this reporting-based deferral. [S79](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512781/), [S80](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS92763/), [S85](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/employee-share-scheme-benefits), [S86](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS191845/)

Report the ESS benefit in its **employee share scheme earnings** field, also in the **earnings not liable for ACC earners' levy** field. Use the current tax code, not the retired ESS code. Show PAYE and student loan deducted. Keep an employer's separate tax-funding payment in **gross earnings**, outside the ESS field, with its own levy treatment. Do not treat the ESS reporting value as additional cash wages. [S76](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-07.pdf?modified=20250331012754), [S85](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/employee-share-scheme-benefits)

TAA 23K permits payday reporting using the ESS deferral date or the specified twice-monthly method: deferral dates on the 1st-15th use the 15th; later dates use month end. File within **2 working days** electronically or **10 working days** under allowed paper filing from the applicable reporting day. Exempt ESS benefits are excluded from this reporting regime; establish exemption separately. Former-employee share benefits without withholding are excluded, but withheld benefits must be reported. A cash payment to a former employee is not automatically covered by the share-only operational exception. [S85](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/employee-share-scheme-benefits), [S86](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS191845/)

Filing and paying remain distinct. RD 6(3) supplies the deemed payment date for the elected non-cash benefit; RD 7B links the election to timely disclosure and RD 4 payment. For cash, RA 5(2) requires withholding when payment is made. Do not use an EI reporting concession as blanket authority to delay cash withholding or remittance. A separate funding payment uses its own actual payment facts; IS25/07's same-reporting-date example assumes aligned processing, rather than creating a universal ESS timing rule for the extra cash. Apply the established monthly/twice-monthly remittance schedule in Section 5 and reconcile the streams. Unusual differences between cancellation, cash payment, deferral and funding dates need a specific Inland Revenue/qualified review before processing. [S76](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-07.pdf?modified=20250331012754), [S77](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM7269557/), [S87](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519950/), [S89](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519944/), [S90](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519735/)


## Worked cases

These fictional cases assume the stated code, eligibility, contribution base and notices have already been established. They check the arithmetic of the selected rules, not an actual person's liability. Tolerance is zero, so a cent error fails.

**Case 1: a positive share-settled benefit.** Assume an established CE 2 benefit with market value $24,000, consideration paid $6,000, no consideration received or historic previous income, valid withholding and a derived 33% extra-pay rate. The benefit is $18,000 and income-tax withholding is $5,940, with no ACC or KiwiSaver on that benefit. This does not verify the market valuation or taxing date. [S74](https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/employee-share-schemes/deducting-tax-on-ess-benefits), [S79](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512781/)

```oa-check
name: nz-2026-ess-share-value
tolerance: 0.001
inputs:
  share_value: 24000
  consideration_paid: 6000
  consideration_received: 0
  previous_income: 0
steps:
  benefit: share_value - consideration_paid + consideration_received - previous_income
  income_tax: benefit * 0.33
expected:
  benefit: 18000
  income_tax: 5940
```

**Case 2: cancellation uses consideration received.** Assume cancellation triggers the taxing date, $15,000 is paid for the rights and $2,000 was paid for them, with no previous income. Share value in this formula is zero; do not add another $15,000 market value. At an established 33% extra-pay rate the $13,000 benefit has $4,290 income tax. [S75](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-06.pdf?modified=20250331012659), [S79](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512781/)

```oa-check
name: nz-2026-ess-cancellation-value
tolerance: 0.001
inputs:
  share_value: 0
  consideration_paid: 2000
  consideration_received: 15000
  previous_income: 0
steps:
  benefit: share_value - consideration_paid + consideration_received - previous_income
  income_tax: benefit * 0.33
expected:
  benefit: 13000
  income_tax: 4290
```

**Case 3: a negative formula is preserved for review.** Assume the statutory formula has share value $1,000, consideration paid $2,000 and no other items. The result is negative $1,000, within CE 2(3)'s deduction rule. This arithmetic does not authorise a negative employment-information payment, offset or payroll refund. [S79](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512781/)

```oa-check
name: nz-2026-ess-negative-formula
tolerance: 0.001
inputs:
  share_value: 1000
  consideration_paid: 2000
  consideration_received: 0
  previous_income: 0
steps:
  formula_result: share_value - consideration_paid + consideration_received - previous_income
expected:
  formula_result: -1000
```

**Case 4: genuine cash settlement with the loan threshold already used.** Assume a $5,000 genuine cash-settled benefit, ordinary 30% extra-pay income-tax rate, required SL deductions and no remaining primary threshold or special certificate. Income tax is $1,500, student loan $600 and net cash $2,900. No ACC, employee KiwiSaver or employer KiwiSaver applies to this benefit. The classification is an input, not established by the calculation. [S74](https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/employee-share-schemes/deducting-tax-on-ess-benefits), [S75](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-06.pdf?modified=20250331012659), [S84](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments), [S88](https://www.legislation.govt.nz/act/public/2011/62/en/latest/)

```oa-check
name: nz-2026-ess-cash-with-loan
tolerance: 0.001
inputs:
  benefit: 5000
steps:
  income_tax: benefit * 0.30
  student_loan: floor(benefit) * 0.12
  net_cash: benefit - income_tax - student_loan
expected:
  income_tax: 1500
  student_loan: 600
  net_cash: 2900
```

**Case 5: employee-funded withholding creates no employer bonus.** Assume the same $5,000 value is provided in shares, with valid withholding, a 30% rate and SL on the full amount. The employee agrees to fund the $1,500 tax and $600 loan deduction from their own resources. Required funding is $2,100; it is not an additional employer-funded gross payment. No share sale, wage deduction or sufficient cash balance is proved here. [S74](https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/employee-share-schemes/deducting-tax-on-ess-benefits), [S76](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-07.pdf?modified=20250331012754), [S77](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM7269557/)

```oa-check
name: nz-2026-ess-employee-funded-withholding
tolerance: 0.001
inputs:
  benefit: 5000
steps:
  income_tax: benefit * 0.30
  student_loan: floor(benefit) * 0.12
  employee_funding: income_tax + student_loan
expected:
  income_tax: 1500
  student_loan: 600
  employee_funding: 2100
```

**Case 6: primary student loan uses only the remaining threshold.** Assume a weekly M SL employee, ordinary pay $300, $464 threshold, no other extra pay or certificate and a $1,000 genuine cash ESS benefit in that pay period. Ordinary four-week pay of $1,200 gives annualised base $15,600, so the extra-pay income-tax rate is 17.5%. Only $164 of threshold remains for the ESS benefit. Income tax is $175, loan $100.32 and net benefit cash $724.68. The regular pay itself has no standard loan deduction. [S2](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S24](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments/calculate-paye-for-a-lump-sum-payment-end-of-employment), [S74](https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/employee-share-schemes/deducting-tax-on-ess-benefits), [S84](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments), [S88](https://www.legislation.govt.nz/act/public/2011/62/en/latest/)

```oa-check
name: nz-2026-ess-main-loan-remaining-threshold
tolerance: 0.001
inputs:
  regular_pay: 300
  weekly_threshold: 464
  benefit: 1000
steps:
  remaining_threshold: max(0, weekly_threshold - regular_pay)
  loan_base: floor(max(0, benefit - remaining_threshold))
  student_loan: loan_base * 0.12
  income_tax: benefit * 0.175
  net_cash: benefit - income_tax - student_loan
expected:
  remaining_threshold: 164
  loan_base: 836
  student_loan: 100.32
  income_tax: 175
  net_cash: 724.68
```

**Case 7: secondary student loan has no threshold.** Assume an S SL employee with derived extra-pay income-tax rate 17.5%, a $1,000 genuine cash ESS benefit and no special certificate. Withhold $175 income tax and $120 loan, leaving $705. Do not subtract the primary weekly threshold from this secondary payment. [S2](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S24](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments/calculate-paye-for-a-lump-sum-payment-end-of-employment), [S74](https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/employee-share-schemes/deducting-tax-on-ess-benefits), [S84](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments), [S88](https://www.legislation.govt.nz/act/public/2011/62/en/latest/)

```oa-check
name: nz-2026-ess-secondary-loan-no-threshold
tolerance: 0.001
inputs:
  benefit: 1000
steps:
  income_tax: benefit * 0.175
  student_loan: floor(benefit) * 0.12
  net_cash: benefit - income_tax - student_loan
expected:
  income_tax: 175
  student_loan: 120
  net_cash: 705
```

**Case 8: the funding payment attracts ACC.** Assume a $4,550 share benefit, valid withholding and an employer agreement to fund its tax and the tax/ACC on the additional payment. Annualised base is $60,000, so the benefit plus the $2,000 funding gross stays in the 30% band and below the ACC cap. There is no SL, KiwiSaver membership or employer contribution obligation. The ESS tax is $1,365. Grossing that funding amount up for 30% tax and 1.75% ACC gives $2,000, including $600 tax and $35 ACC, leaving $1,365 to fund the ESS tax. The benefit remains $4,550 in the ESS field; the $2,000 is separate gross earnings. [S2](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S24](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments/calculate-paye-for-a-lump-sum-payment-end-of-employment), [S74](https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/employee-share-schemes/deducting-tax-on-ess-benefits), [S76](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-07.pdf?modified=20250331012754), [S85](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/employee-share-scheme-benefits)

```oa-check
name: nz-2026-ess-funded-tax-acc-separate
tolerance: 0.001
inputs:
  benefit: 4550
  annualised_base: 60000
steps:
  ess_tax: benefit * 0.30
  funding_gross: ess_tax / (1 - 0.30 - 0.0175)
  funding_tax: funding_gross * 0.30
  funding_acc: funding_gross * 0.0175
  funding_net: funding_gross - funding_tax - funding_acc
  rate_comparison_total: annualised_base + benefit + funding_gross
expected:
  ess_tax: 1365
  funding_gross: 2000
  funding_tax: 600
  funding_acc: 35
  funding_net: 1365
  rate_comparison_total: 66550
```

**Case 9: funding income tax, loan and employee KiwiSaver.** Assume a $9,800 share benefit and valid withholding, annualised base $160,000, ordinary 33% income-tax rate, required 12% SL with the primary threshold already used and a valid 6% employee KiwiSaver instruction. The employer funds both benefit deductions and all applicable deductions on the additional payment. The $9,000 additional gross keeps the combined rate comparison at $178,800, within 33%; ACC is zero because the established annualised base already exceeds $156,641. ESS tax $3,234 plus loan $1,176 needs $4,410 funding. The additional gross has $2,970 tax, $1,080 loan and $540 employee KiwiSaver, leaving $4,410. A separately established 3.5% compulsory employer contribution on that additional gross is $315 before its own ESCT; none is due on the ESS benefit. [S2](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S24](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments/calculate-paye-for-a-lump-sum-payment-end-of-employment), [S74](https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/employee-share-schemes/deducting-tax-on-ess-benefits), [S76](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-07.pdf?modified=20250331012754), [S88](https://www.legislation.govt.nz/act/public/2011/62/en/latest/)

```oa-check
name: nz-2026-ess-all-deductions-funded
tolerance: 0.001
inputs:
  benefit: 9800
  annualised_base: 160000
  employee_kiwisaver_rate: 0.06
  employer_rate: 0.035
steps:
  ess_tax: benefit * 0.33
  ess_loan: floor(benefit) * 0.12
  net_funding: ess_tax + ess_loan
  funding_gross: net_funding / (1 - 0.33 - 0.12 - employee_kiwisaver_rate)
  funding_tax: funding_gross * 0.33
  funding_loan: floor(funding_gross) * 0.12
  employee_kiwisaver: funding_gross * employee_kiwisaver_rate
  funding_net: funding_gross - funding_tax - funding_loan - employee_kiwisaver
  employer_gross: funding_gross * employer_rate
  rate_comparison_total: annualised_base + benefit + funding_gross
expected:
  ess_tax: 3234
  ess_loan: 1176
  net_funding: 4410
  funding_gross: 9000
  funding_tax: 2970
  funding_loan: 1080
  employee_kiwisaver: 540
  funding_net: 4410
  employer_gross: 315
  rate_comparison_total: 178800
```

**Case 10: tax-only funding above the ACC cap.** Assume annualised base $200,000, an established $6,100 share benefit, valid withholding and an employer agreement to fund all income tax. There is no SL or KiwiSaver obligation and no ACC on the additional payment at this established base. The 39% benefit tax is $2,379; a separate gross payment of $3,900 has $1,521 tax and leaves $2,379. The gross-up applies to the funding payment, not to $6,100 of share value. [S2](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S24](https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments/calculate-paye-for-a-lump-sum-payment-end-of-employment), [S74](https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/employee-share-schemes/deducting-tax-on-ess-benefits), [S76](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-07.pdf?modified=20250331012754)

```oa-check
name: nz-2026-ess-tax-only-above-acc-cap
tolerance: 0.001
inputs:
  benefit: 6100
steps:
  ess_tax: benefit * 0.39
  funding_gross: ess_tax / (1 - 0.39)
  funding_tax: funding_gross * 0.39
  funding_net: funding_gross - funding_tax
expected:
  ess_tax: 2379
  funding_gross: 3900
  funding_tax: 1521
  funding_net: 2379
```

**Case 11: modern exempt ESS at both amount limits.** Assume a qualifying post-1 April 2025 offer in the current income year, an established relevant 12-month cap period, market value of $7,500 and voluntary employee spending of $4,500 across all purchases in that period. The discount is $3,000, with no headroom in either limit. A qualifying interest/charge-free $4,500 loan over 36 monthly payments is $125 a month before any statutory leave suspension, assuming equal payments; CW 26C(4)(d) requires regular instalments of a month or less, not equal ones. Assume every other scheme and receipt condition is satisfied; these amounts alone do not prove exemption. [S101](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/), [S107](https://www.legislation.govt.nz/act/public/2025/9/en/latest/)

```oa-check
name: nz-2026-exempt-ess-exact-limits
tolerance: 0
inputs:
  market_value: 7500
  employee_cost: 4500
  value_limit: 7500
  discount_limit: 3000
  loan_months: 36
steps:
  discount: market_value - employee_cost
  value_headroom: value_limit - market_value
  discount_headroom: discount_limit - discount
  monthly_payment: employee_cost / loan_months
expected:
  discount: 3000
  value_headroom: 0
  discount_headroom: 0
  monthly_payment: 125
```

**Case 12: share-value limit exceeded by a cent.** Under the same modern offer/period assumptions, total share value is $7,500.01 and employee cost is $4,500.01. The $3,000 discount meets its limit, but share value exceeds its separate limit by $0.01. Do not accept the arrangement on the discount test alone. The tax consequences of failed exemption require separate review. [S101](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/), [S107](https://www.legislation.govt.nz/act/public/2025/9/en/latest/)

```oa-check
name: nz-2026-exempt-ess-value-excess
tolerance: 0
inputs:
  market_value: 7500.01
  employee_cost: 4500.01
  value_limit: 7500
steps:
  discount: market_value - employee_cost
  value_excess: market_value - value_limit
expected:
  discount: 3000
  value_excess: 0.01
```

**Case 13: discount limit exceeded by a cent.** Under the same modern offer/period assumptions, total share value is $7,500 and employee cost is $4,499.99. Value meets its limit, but the $3,000.01 discount exceeds its separate limit by $0.01. Do not treat the value test as sufficient. [S101](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/), [S107](https://www.legislation.govt.nz/act/public/2025/9/en/latest/)

```oa-check
name: nz-2026-exempt-ess-discount-excess
tolerance: 0
inputs:
  market_value: 7500
  employee_cost: 4499.99
  discount_limit: 3000
steps:
  discount: market_value - employee_cost
  discount_excess: discount - discount_limit
expected:
  discount: 3000.01
  discount_excess: 0.01
```

**Case 14: associated holdings reach the exclusion.** Assume the employee holds 8% and a separately established associated person holds 2% of issued capital, without overlap. The combined holding is exactly 10%, so CW 26D excludes this person. This calculation does not establish association or ownership facts. [S102](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32494/)

```oa-check
name: nz-2026-exempt-ess-associated-holding
tolerance: 0
inputs:
  employee_percent: 8
  associate_percent: 2
  exclusion_percent: 10
steps:
  combined_percent: employee_percent + associate_percent
  margin_to_exclusion: exclusion_percent - combined_percent
expected:
  combined_percent: 10
  margin_to_exclusion: 0
```

**Case 15: statutory equal-participation pool.** For a particular full-time permanent offeree, assume the legally established pool of other full-time permanent employees is 110, of whom 10 have offers subject to foreign security disclosure rules. Of the remaining 100, 90 are eligible on an equal basis. That is exactly 90%. This conditional pool calculation does not prove the scheme-wide test for every offeree or the separate part-time/seasonal tests. [S101](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/)

```oa-check
name: nz-2026-exempt-ess-other-employee-pool
tolerance: 0
inputs:
  other_employees: 110
  foreign_disclosure: 10
  equal_eligible: 90
steps:
  comparison_pool: other_employees - foreign_disclosure
  eligible_percent: equal_eligible / comparison_pool * 100
expected:
  comparison_pool: 100
  eligible_percent: 90
```

**Case 16: discounted shares and actual group employment end.** Assume discounted shares, a 48-month loan repayment period and actual employment ending 24 months after acquisition, including any same-group employment following transfer. The restriction is the shorter of 48 months (the longer of 36 and 48) and 24 months, hence 24 months. The applicable exit/transfer/buyback rule still needs separate application. [S101, subsections (7)-(9)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/)

```oa-check
name: nz-2026-exempt-ess-employment-end-restriction
tolerance: 0
inputs:
  three_year_months: 36
  loan_period_months: 48
  employment_end_months: 24
steps:
  longer_period: max(three_year_months, loan_period_months)
  restriction_months: min(longer_period, employment_end_months)
expected:
  longer_period: 48
  restriction_months: 24
```

**Case 17: early repayment does not remove the 3-year limb.** Assume discounted shares, a 36-month loan paid off voluntarily after 12 months, continuing qualifying employment until month 60 and no other exception. Even using the actual 12-month repayment period, the longer-of test retains 36 months; restriction ends at month 36 on these facts. This does not determine the effect of leave extensions or different loan terms. [S101](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/)

```oa-check
name: nz-2026-exempt-ess-early-repayment
tolerance: 0
inputs:
  three_year_months: 36
  actual_repayment_months: 12
  employment_end_months: 60
steps:
  longer_period: max(three_year_months, actual_repayment_months)
  restriction_months: min(longer_period, employment_end_months)
expected:
  longer_period: 36
  restriction_months: 36
```

**Case 18: ordinary and qualifying hardship withdrawal prices.** Assume employee cost of $4,500, withdrawal-day market value of $6,000 and a $1,000 outstanding loan. An ordinary withdrawal with the required notice gives a $4,500 buyback and $3,500 after loan repayment. A separately established serious-hardship withdrawal with the employee agreement required by subsection (5) gives a $6,000 buyback and $5,000 after repayment. These are alternative established cases, not an employee election to claim the higher price without hardship. [S101](https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/)

```oa-check
name: nz-2026-exempt-ess-withdrawal-prices
tolerance: 0
inputs:
  employee_cost: 4500
  market_value: 6000
  loan_balance: 1000
steps:
  ordinary_price: min(employee_cost, market_value)
  ordinary_after_loan: ordinary_price - loan_balance
  hardship_price: market_value
  hardship_after_loan: hardship_price - loan_balance
expected:
  ordinary_price: 4500
  ordinary_after_loan: 3500
  hardship_price: 6000
  hardship_after_loan: 5000
```

**Case 19: annual exempt scheme aggregates.** Assume 3 distinct employee recipients in the established tax-year reporting period, shares granted with total values of $7,500, $5,000 and $3,000, and respective employee contributions of $4,500, $3,000 and $1,000. IR1212 reports $15,500 share value, $8,500 contributions and 3 recipients. The $7,000 aggregate difference is a reconciliation amount, not a per-person discount allowance or an ordinary EI amount. Assume all individual eligibility and other scheme conditions have been independently established. [S106](https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS32667/), [S111](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1200---ir1299/ir1212/ir1212.pdf?modified=20261022002438)

```oa-check
name: nz-2026-exempt-ess-annual-aggregates
tolerance: 0
inputs:
  shares_a: 7500
  shares_b: 5000
  shares_c: 3000
  contributions_a: 4500
  contributions_b: 3000
  contributions_c: 1000
  distinct_recipients: 3
steps:
  shares_total: shares_a + shares_b + shares_c
  contributions_total: contributions_a + contributions_b + contributions_c
  aggregate_difference: shares_total - contributions_total
  recipient_count: distinct_recipients
expected:
  shares_total: 15500
  contributions_total: 8500
  aggregate_difference: 7000
  recipient_count: 3
```

## When to refuse or refer

Refer: actual scheme eligibility where receipt fails, legacy approvals and historic transitions, difficult valuations, replacement schemes, and classification beyond the selected employee methods.

## Sources

| Source | URL | Read on | What was read |
| --- | --- | --- | --- |
| IRD ESS withholding, updated 28 October 2026 | https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/employee-share-schemes/deducting-tax-on-ess-benefits | 2026-11-13 | Read for Employee share schemes: establish the benefit first, Withholding, student loans and funding, Worked cases (read by Ryan Duguid) |
| IS25/06, 31 March 2025; selected paragraphs, employee scope | https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-06.pdf?modified=20250331012659 | 2026-11-13 | Read for Employee share schemes: establish the benefit first, Withholding, student loans and funding, Worked cases (read by Ryan Duguid) |
| Income Tax Act CE7, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512798/ | 2026-11-13 | Read for Employee share schemes: establish the benefit first (read by Ryan Duguid) |
| Income Tax Act RD7, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519952/ | 2026-11-13 | Read for Employee share schemes: establish the benefit first, Withholding, student loans and funding (read by Ryan Duguid) |
| Income Tax Act CW26B, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32342/ | 2026-11-13 | Read for Exempt ESS: establish the scheme before excluding payroll (read by Ryan Duguid) |
| Income Tax Act CW26C, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/ | 2026-11-13 | Read for Exempt ESS: establish the scheme before excluding payroll, Worked cases (read by Ryan Duguid) |
| Tax Administration Act63B, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS32667/ | 2026-11-13 | Read for Exempt ESS: establish the scheme before excluding payroll, Worked cases (read by Ryan Duguid) |
| 2025 No9 sections2(34) and27, offer-date application of exempt ESS limits | https://www.legislation.govt.nz/act/public/2025/9/en/latest/ | 2026-11-13 | Read for Exempt ESS: establish the scheme before excluding payroll, Worked cases (read by Ryan Duguid) |
| Income Tax Act CW26F, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32498/ | 2026-11-13 | Read for Exempt ESS: establish the scheme before excluding payroll (read by Ryan Duguid) |
| Income Tax Act YA 1 selected worker, market value and year definitions, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520575/ | 2026-11-13 | Read for Exempt ESS: establish the scheme before excluding payroll (read by Ryan Duguid) |
| Income Tax Act CW26DB, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS328941/ | 2026-11-13 | Read for Exempt ESS: establish the scheme before excluding payroll (read by Ryan Duguid) |
| Income Tax Act CW26D, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32494/ | 2026-11-13 | Read for Exempt ESS: establish the scheme before excluding payroll, Worked cases (read by Ryan Duguid) |
| Income Tax Act CW26G, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32500/ | 2026-11-13 | Read for Exempt ESS: establish the scheme before excluding payroll (read by Ryan Duguid) |
| Income Tax Act CW26E, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32496/ | 2026-11-13 | Read for Exempt ESS: establish the scheme before excluding payroll (read by Ryan Duguid) |
| Income Tax Act DV28, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS33459/ | 2026-11-13 | Read for Exempt ESS: establish the scheme before excluding payroll (read by Ryan Duguid) |
| IRD exempt employee share schemes, updated 13 November 2026; statutory qualifications apply | https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/exempt-employee-share-schemes | 2026-11-13 | Read for Exempt ESS: establish the scheme before excluding payroll (read by Ryan Duguid) |
| IRD initial exempt ESS notification, updated 22 October 2026 | https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/exempt-employee-share-schemes/report-exempt-ess | 2026-11-13 | Read for Exempt ESS: establish the scheme before excluding payroll (read by Ryan Duguid) |
| IR1211 initial exempt ESS notification, October 2026, page1 | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1200---ir1299/ir1211/ir1211.pdf?modified=20261022002436 | 2026-11-13 | Read for Exempt ESS: establish the scheme before excluding payroll (read by Ryan Duguid) |
| IRD annual exempt ESS reporting, updated 22 October 2026 | https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/exempt-employee-share-schemes/report-employee-shares-under-exempt-ess | 2026-11-13 | Read for Exempt ESS: establish the scheme before excluding payroll (read by Ryan Duguid) |
| IR1212 annual exempt ESS return, October 2026, page1 | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1200---ir1299/ir1212/ir1212.pdf?modified=20261022002438 | 2026-11-13 | Read for Exempt ESS: establish the scheme before excluding payroll, Worked cases (read by Ryan Duguid) |
| IRD ESS employment information, updated 28 October 2026 | https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/employee-share-scheme-benefits | 2026-11-13 | Read for Exempt ESS: establish the scheme before excluding payroll, ESS income, filing and payment dates, Worked cases (read by Ryan Duguid) |
| Income Tax Act CE7B, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS92763/ | 2026-11-13 | Read for ESS value, taxing date and 2026 deferred shares, ESS income, filing and payment dates (read by Ryan Duguid) |
| Income Tax Act CE2, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512781/ | 2026-11-13 | Read for ESS value, taxing date and 2026 deferred shares, ESS income, filing and payment dates, Worked cases (read by Ryan Duguid) |
| Income Tax Act EA4B, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS1593301/ | 2026-11-13 | Read for ESS value, taxing date and 2026 deferred shares (read by Ryan Duguid) |
| 2026 No8 sections2,10,51,114; selected commencement and application | https://www.legislation.govt.nz/act/public/2026/8/en/latest/ | 2026-11-13 | Read for ESS value, taxing date and 2026 deferred shares (read by Ryan Duguid) |
| IRD employee deferred shares, updated 16 March 2026; qualify by enacted law | https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/employee-share-schemes/ess-rules/tax-on-employee-deferred-shares | 2026-11-13 | Read for ESS value, taxing date and 2026 deferred shares (read by Ryan Duguid) |
| Income Tax Act RD7B, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM7269557/ | 2026-11-13 | Read for Withholding, student loans and funding, ESS income, filing and payment dates, Worked cases (read by Ryan Duguid) |
| IS25/07, 31 March 2025; selected funding/reporting paragraphs | https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-07.pdf?modified=20250331012754 | 2026-11-13 | Read for Withholding, student loans and funding, ESS income, filing and payment dates, Worked cases (read by Ryan Duguid) |
| Student Loan Scheme Act2011 s4 and ss36-37, copy 1 April 2026 | https://www.legislation.govt.nz/act/public/2011/62/en/latest/ | 2026-11-13 | Read for Withholding, student loans and funding, Worked cases (read by Ryan Duguid) |
| 2026-27 payroll specification, selected sections | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 | 2026-11-14 | Read for Withholding, student loans and funding, Worked cases; reopened on 2026-11-14 for the annual PAYE formula, earners' levy, student-loan threshold, NSW rate and ESCT table (2026-27 specification dated 24 March 2026, version 1.0) |
| Non-termination lump-sum PAYE, updated 18 May 2026 | https://www.ird.govt.nz/calculate-lump-sum-paye | 2026-11-13 | Read for Withholding, student loans and funding (read by Ryan Duguid) |
| End-of-employment lump-sum PAYE, updated 20 April 2026 | https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments/calculate-paye-for-a-lump-sum-payment-end-of-employment | 2026-11-13 | Read for Withholding, student loans and funding, Worked cases (read by Ryan Duguid) |
| IRD lump sum payments, updated 27 January 2026 | https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments | 2026-11-13 | Read for Withholding, student loans and funding, Worked cases (read by Ryan Duguid) |
| Tax Administration Act23K, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS191845/ | 2026-11-13 | Read for ESS income, filing and payment dates (read by Ryan Duguid) |
| Income Tax Act RD6, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519950/ | 2026-11-13 | Read for ESS income, filing and payment dates (read by Ryan Duguid) |
| Income Tax Act RD4, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519944/ | 2026-11-13 | Read for ESS income, filing and payment dates (read by Ryan Duguid) |
| Income Tax Act RA5, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519735/ | 2026-11-13 | Read for ESS income, filing and payment dates (read by Ryan Duguid) |

Not yet confirmed: the rows below were read by Ryan Duguid on 12 and 13 November 2026, and only the spot-checked figures listed in the PR were reopened on 14 November 2026. Inherited sources checked 12 November 2026; selected ESS sources checked 13 November 2026. Selected District Court Act sections use the current copy dated 17 February 2026; Tax Administration Act section 157 uses the current copy dated 1 October 2026. SPS 21/01 is dated 12 April 2021 and remains linked by IRD's arrears page updated 16 April 2026. Extra-pay and deduction examples are recalculated from the stated rules; known inconsistent printed examples and boundary wording are recorded in the verification log. The technical specification is dated 24 March 2026, version 1.0, and expressly covers 1 April 2026 to 31 March 2027. IR335's cover says September 2026. KS4's cover says April 2026. Selected KiwiSaver Act provisions use the current copy dated 1 April 2026. The verification log records the selected native/image page scope, the surviving legacy default and conflicting sample-letter/example wording. The selected correction regulations use the 30 March 2026 consolidation. Selected TAA record, assessment and penalty provisions use the 1 October 2026 copy. Its full-Act page flags unincorporated amendments; the selected amendment-impact check is recorded in the verification log. SPS19/04 is dated 30 May 2019. Current statutory wording controls the affected-employee penalty base and inclusive $100 exemption. These checks do not claim full PDF or statute review. Employer ACC Work and Working Safer levy invoices are not calculated.
