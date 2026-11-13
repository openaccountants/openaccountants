---
name: wi-payroll
description: Wisconsin employer payroll withholding, unemployment insurance and reporting workflow for tax year 2026.
jurisdiction: US-WI
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
category: payroll
type: computation
version: "0.2"
---

# Wisconsin employer payroll, withholding and unemployment insurance, 2026

> **General reference only.** Built from official Wisconsin sources read November 13, 2026; not approved by an accountant. Circular 230 section 10.37: use verified facts, state assumptions and unresolved matters, and obtain professional review before a payroll filing or tax position.

## Scope

Wisconsin (US-WI) private employers: state income-tax withholding under chapter 71, WT-4/WT-4A/W-220 certificates, WT-6 deposits, WT-7 annual reconciliation, state UI under chapter 108, DWD registration, wage base, new/experienced rates and quarterly reporting. These are separate accounts with separate wage definitions. This skill preserves the prior draft's reciprocity, classification, wage-law and named-case topics while correcting unsupported rules.

The DOR January 2026 W-166 publication still prescribes withholding methods effective for periods beginning on or after January 1, 2022. Its formula is the published payroll method, not the final 2026 individual income-tax schedule. Some annual examples in that publication relate to 2025 wages filed in the **2025-2026 filing cycle**; the ordinary recurring deadlines below are separately stated. DWD's site relocated November 10, 2026; the current UI URLs were opened in an ordinary browser where direct retrieval failed. No CAPTCHA, proxy or access bypass was used.

Federal wages, withholding, FICA, FUTA and federal information returns belong in `us-form-941-940-payroll`; do not copy their rates or bases here. Wisconsin individual return brackets/standard deductions belong in `wi-income-tax`. Corporate franchise/income tax and sales tax belong in `wi-corporate-tax` and `wisconsin-sales-tax`. Public-sector/tribal/reimbursable payroll and complex multistate sourcing require their specific rules; their coverage boundary is stated below.

## Ask the client first

- What legal entity, FEIN, DOR withholding number, DWD UI account, first employment date and assigned filing frequencies/rate notices apply?
- Where does each employee actually work, where are they domiciled, and are there moves, reciprocal declarations, military or transport-worker exceptions?
- What signed WT-4/WT-4A/W-220 forms, effective dates, marital status, exemptions and extra withholding are in force?
- What is the pay frequency, current taxable pay, supplemental pay, benefits and each employee's year-to-date UI wages?
- Is the employer commercial, construction, farm, domestic, nonprofit, governmental or a successor, and what taxable payroll determines its UI size category?
- Are any workers classified as contractors or officers, and are there closures, missing returns, notices, wage disputes or prior-period corrections?

## The method, step by step

### 1. Determine withholding coverage and register

Read both employee and employer conditions. An employer engaged/licensed/transacting business in Wisconsin or organized under Wisconsin law generally withholds on Wisconsin residents' wages wherever services are performed and nonresidents' wages for services performed in Wisconsin. The current https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx lists exceptions for reciprocal-state residents, certain interstate carriers, retirement payments, qualifying military spouses/servicemembers and nonreciprocal nonresidents whose expected Wisconsin earnings are less than $2,000 annually. The latter is a withholding exception, not a universal no-return or no-UI rule. [DOR https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx questions 1-3](https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx).

Register a required or voluntary withholding account through My Tax Account (MTA), business tax registration, or BTR-101. The initial $20 BTR registration covers two years, followed by a $10 renewal every two years. DOR assigns a 15-digit withholding number, distinct from the FEIN. Each corporate subsidiary with employees and its own FEIN needs its own Wisconsin number; divisions of the same corporation share one. Wisconsin does not permit a common paymaster for separate corporations. [W-166 pp.6-7](https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf).

DOR assigns frequency using the registration information; it is not automatically quarterly for every new employer. Keep the actual notice and effective period. More frequent payments are allowed with at least one return per required period; less frequent filing needs permission. A reactivation with unchanged ownership can use the prior number; a change of entity may require a new account. Closing withholding does not close UI or other tax accounts. [W-166 pp.6-7](https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf).

### 2. Obtain and apply the correct employee certificate

Every newly hired employee supplies Wisconsin Form WT-4; a federal W-4 does not replace it. Retain the form and use its Wisconsin status, exemptions and extra amount, subject to any DOR instruction. If WT-4 is missing, obtain the certificate or confirm the applicable DOR default before a final payroll run; the old draft's single/zero default has not been independently located in the sections read. Do not transfer a pre-2020 federal allowance count or the individual return's exemption amount into the payroll formula. [W-166 pp.5,7](https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf).

| Certificate / condition | Required action | Official source |
|---|---|---|
| WT-4 claims more than 10 exemptions | Send a copy to DOR at quarter end; no copy required if the worker no longer works for the employer at quarter end | https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf |
| WT-4 claims complete exemption and earns over $200 weekly | Same quarter-end submission rule, not the prior draft's universal 20-day certificate deadline | https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf |
| Complete exemption from withholding | Prior-year no liability and current-year no liability expected; renew WT-4 annually by April 30 or use zero exemptions thereafter | https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx ; https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf |
| WT-4A reduced-withholding agreement | Use the employee's properly completed agreement, subject to DOR revocation; do not invent allowances | https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf |
| New hire or rehire, employer with FEIN | Report to Wisconsin New Hire Program within 20 days | https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf |
| W-220 reciprocity declaration | Written verification for eligible IL/IN/KY/MI compensation; remains effective while the employee remains subject to reciprocity | https://www.revenue.wi.gov/DOR%20Publications/pb121.pdf ; https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx |

WT-4A is a different route from complete exemption. The 2026 employee worksheet reconciles estimated Wisconsin tax and credits, subtracts prior withholding/estimates and expected spouse withholding, and divides the balance by remaining pay periods. It requires filing a copy with DOR within ten days; the calendar-year 2026 agreement expires April 30, 2027. Its actual 2026 deduction/bracket figures belong to `wi-income-tax`, not the regular W-166 withholding method. The old draft confused exemption renewal with annual W-220 expiration. [2026 WT-4A worksheet](https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf).

### 3. Compute ordinary state withholding using W-166

Select either the current wage-bracket table for the actual pay period/status/exemptions or the approved alternate method. Another method needs prior DOR permission. Do not use final-return tax brackets as a substitute and do not subtract an ordinary income-return standard deduction from every employee's pay. The approved alternate method annualizes current taxable wages, deducts its own allowance formula, deducts $400 per WT-4 exemption, taxes the annual net wage and divides by pay periods. [W-166 pp.25-27](https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf).

Let G = taxable wages for the period times annual pay periods; E = the certificate's number of withholding exemptions. The deduction D below is specific to payroll. N = max(G minus D minus 400 times E, 0). After dividing annual tax by annual pay periods, add any valid requested additional withholding. Keep the wage definition and current certificate in the workpaper. [W-166 p.26](https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf).

| W-166 alternate-method input / annual wage condition | Payroll figure / rule | Official source |
|---|---|---|
| Single, G < $17,780 | D = $6,702 | https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf |
| Single, $17,780 <= G < $73,630 | D = $6,702 minus 12% of (G minus $17,780) | https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf |
| Single, G >= $73,630 | D = $0 | https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf |
| Married, G < $25,727 | D = $9,461 | https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf |
| Married, $25,727 <= G < $73,032 | D = $9,461 minus 20% of (G minus $25,727) | https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf |
| Married, G >= $73,032 | D = $0 | https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf |
| Each WT-4 withholding exemption | $400 in the alternate annual net-wage computation | https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf |
| N <= $12,760 | Annual tax = 3.54% of N | https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf |
| $12,760 < N <= $25,520 | Annual tax = $451.70 + 4.65% of excess over $12,760 | https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf |
| $25,520 < N <= $280,950 | Annual tax = $1,045.04 + 5.30% of excess over $25,520 | https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf |
| N > $280,950 | Annual tax = $14,582.83 + 7.65% of excess over $280,950 | https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf |

Use the printed base amounts at band changes; the small base rounding in the published schedule should not be silently replaced by a newly compounded schedule. For no fixed payroll period, W-166 p.25 prescribes daily/miscellaneous treatment and a special short-week declaration rule; do not assume 52 pay periods for every commission. The ordinary formula above does not independently audit every wage-table cell or settle unusual status/certificate situations. [W-166 pp.25-27](https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf).

Supplemental pay paid with regular wages may be aggregated as one regular-period payment. Pay between regular periods may be added to the current or last preceding regular payment in the same calendar year. Alternatively, the following approved flat percentages depend on estimated annual gross salary and apply only to supplemental pay. The former version's universal 7.65% bonus rate was wrong. [W-166 p.25](https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf).

| Estimated annual gross salary for supplemental method | Flat percentage on supplemental payment | Official source |
|---|---|---|
| At least $0, less than $12,760 | 3.54% | https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf |
| At least $12,760, less than $25,520 | 4.65% | https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf |
| At least $25,520, less than $280,950 | 5.30% | https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf |
| $280,950 or more | 7.65% | https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf |

### 4. Deposit and reconcile through DOR

Frequency is based on remittances in the twelve months ending October 31, reviewed annually by the end of November; changes normally start January 1, with different-year-end notices aligned to the fiscal year. Use the assigned frequency until notified, rather than deriving it solely from gross payroll. [November 2026 frequency page](https://www.revenue.wi.gov/Pages/Businesses/Filing-Frequency-Changes.aspx).

| Annual withholding remittances / assigned status | Ordinary filing/payment cadence | Official source |
|---|---|---|
| $20,001 or more | Semi-monthly WT-6; pay dates 1st-15th due month end, pay dates 16th-end due next month's 15th | https://www.revenue.wi.gov/Pages/Businesses/Filing-Frequency-Changes.aspx ; https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx |
| $2,401-$20,000 | Monthly WT-6; last day of following month | https://www.revenue.wi.gov/Pages/Businesses/Filing-Frequency-Changes.aspx ; https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx |
| $301-$2,400 | Quarterly WT-6; last day of month after quarter | https://www.revenue.wi.gov/Pages/Businesses/Filing-Frequency-Changes.aspx ; https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx |
| $300 or less | Annual WT-7; do not file WT-6 | https://www.revenue.wi.gov/Pages/Businesses/Filing-Frequency-Changes.aspx ; https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx |
| WT-7 and wage/information returns with Wisconsin withholding | January 31 following calendar year; next business day for weekend/legal holiday | https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx |
| Withholding account closed before December 31 | WT-7 within 30 days of account cease date | https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx |
| MTA ACH debit | Initiate by 4 p.m. Central Standard Time on due date | https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx |

Quarterly/monthly/semi-monthly accounts must electronically file WT-6 even for zero withholding. Options include MTA, approved software, Telefile, ACH credit and file transmission. The old $300 e-file gate and forecast end of paper acceptance are not the governing rule. Annual filers report through WT-7. Retain a return receipt and separately verify payment settlement; a debit request is not proof the bank paid. [DOR https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx questions 4-5](https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx).

In MTA, select the withholding account and correct period, report tax actually withheld during the period, submit the deposit report and arrange the matching payment. Before filing WT-7, reconcile the year by payment date and account, including all original/corrected WT-6 periods, W-2s and applicable information returns. W-166 warns that WT-7 is rejected where required WT-6s are missing or annual tax exceeds reported deposits; a deposit may be pending with a future payment date. Do not force the annual figure to match a wrong deposit. Correct the underlying period. [W-166 p.5 and DOR https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx](https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf).

File WT-7 through MTA, approved software, Telefile or file transmission. File wage data separately using an accepted DOR channel; ten or more W-2s must be electronic, and ten or more of an information-return type triggers its electronic rule. The current https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx describes MTA, Wisconsin specifications, third-party XML and IRIS/FIRE transition; do not assume an SSA filing automatically satisfies Wisconsin. Do not send federal/state transmittal forms with mailed W-2s. DOR advises electronic filing for a confirmation number. [DOR https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx questions 7-10](https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx).

An extension of up to one month for WT-6/WT-7 and supporting filings may be granted for good cause if requested by the original due date; it does not extend employee wage-statement delivery. The old statement that WT-7 has no extension was wrong. When closing, report the actual last withholding date and file the short-period annual reconciliation; do not stop filing merely because payroll is zero. Keep tax records through the applicable limitation period, usually four years from the return due date or filing date, whichever is later. [DOR https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx questions 6,12-13](https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx).

### 5. Resolve income-tax reciprocity separately from UI

Wisconsin has employee-compensation reciprocity with Illinois, Indiana, Kentucky and Michigan. Obtain W-220 written verification before treating compensation as exempt. Publication 121 says this remains effective while the person is subject to reciprocity; it does not expire automatically December 31. Revalidate the facts if the employee moves or circumstances change. Complete withholding exemption on WT-4 has its own annual renewal rule and is not the same declaration. [DOR https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx](https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx); [Publication 121 pp.3-5, 2025-2026 filing cycle](https://www.revenue.wi.gov/DOR%20Publications/pb121.pdf).

Reciprocity covers defined employee compensation, not self-employment profit, rental/business income or all dual-resident situations. A reciprocal-state resident with only reciprocal compensation may have no Wisconsin return obligation; Form 1NPR is needed to recover Wisconsin tax actually withheld. A Wisconsin resident reports reciprocal-state wages to Wisconsin. Home-state withholding and its forms/rates require that state's owner skill and registration rules; merely hiring a resident does not establish a complete other-state registration conclusion. [Publication 121 pp.3-5](https://www.revenue.wi.gov/DOR%20Publications/pb121.pdf).

For Minnesota, do not invent reciprocity. W-166 p.9 instead gives a special withholding arrangement: Wisconsin withholding is not required on Minnesota-earned wages of a Wisconsin domiciliary when those wages are subject to Minnesota withholding and would also be subject to Wisconsin withholding. The individual may still need Wisconsin estimated payments and return reconciliation. This arrangement is not an exemption of the wages from Wisconsin income tax. [W-166 p.9](https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf).

An employee actually working at an out-of-state home is not automatically performing services in Wisconsin merely because the customer or assigned office is there. Document actual work days, domicile and applicable exception. Income-tax reciprocity does not decide the UI state, workers' compensation, new-hire reporting or sales nexus. UI localization requires its own analysis; the old remote-work/product-delivery shortcut is withdrawn. [DOR https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx question 1](https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx); [DWD handbook employment exclusions](https://dwd.wisconsin.gov/ui201/t2201).

### 6. Establish UI coverage and register with DWD

The following liability conditions are from current UCB-201-P Part 1, opened in a normal browser. Coverage is generally retroactive to January 1 of the year a liability condition is first met; acquiring covered business activity starts coverage at acquisition. Keep records even before the threshold is met so liability can be determined. [DWD coverage](https://dwd.wisconsin.gov/ui201/t1201).

| Employer / trigger | UI liability condition | Official source |
|---|---|---|
| Commercial | $1,500 wages in any quarter, or one or more individuals for part of a day in 20 or more weeks in any calendar year; part-time and nonconsecutive weeks count | https://dwd.wisconsin.gov/ui201/t1201 |
| Agricultural | $20,000 cash agricultural wages in a quarter, or ten or more workers in agricultural labor for part of a day in 20 or more weeks | https://dwd.wisconsin.gov/ui201/t1201 |
| Domestic | $1,000 cash wages for domestic service in a quarter | https://dwd.wisconsin.gov/ui201/t1201 |
| 501(c)(3) nonprofit | Four or more individuals on a day in 20 or more weeks; other nonprofits use commercial conditions | https://dwd.wisconsin.gov/ui201/t1201 |
| Government | Mandatory coverage; financing/benefit rules require separate review | https://dwd.wisconsin.gov/ui201/t1201 |
| General additional triggers | Wisconsin wages with FUTA liability for the year, acquiring part/all of a covered business, or approved voluntary coverage | https://dwd.wisconsin.gov/ui201/t1201 |

Use DWD Employer Unemployment Resources, new UI account/new employer registration, rather than the DOR withholding account. Supply the entity, FEIN, employment/ownership/acquisition facts and retain DWD's liability determination, account number and rate notice. Do not register a qualified settlement fund as the employer; settlement wages are allocated to the actual employer. The employer page also links tax/wage filing, payments, account changes and the new-hire program. [DWD Part 1](https://dwd.wisconsin.gov/ui201/t1201); [employer services](https://dwd.wisconsin.gov/ui/employer).

Government, certain nonprofit and tribal employers may elect reimbursement financing rather than ordinary contributions, while still filing quarterly wage/tax reports. Their benefit-charge reimbursement and assurance requirements are outside the ordinary rate calculation here. Do not apply a new commercial employer rate to a reimbursement account. [DWD Part 1 C](https://dwd.wisconsin.gov/ui201/t1201).

### 7. Compute 2026 UI using the proper wage base and rate notice

UI is employer financed. Report all covered wages; tax only the first $14,000 per employee per calendar year. A zero-rate employer still files tax and wage reports. DWD's 2026 page confirms Schedule D and includes separate basic and solvency components. Total rate is basic plus solvency; the old assertion that solvency is universally zero is incorrect. [DWD 2026 schedule](https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026); [handbook introduction and Part 4](https://dwd.wisconsin.gov/ui201/t4201).

| UI 2026 item / category | Value | Official source |
|---|---|---|
| Annual employee taxable wage base | $14,000 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| Employer size | Under $500,000 taxable payroll versus $500,000 or more; equality belongs to large category | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 ; https://dwd.wisconsin.gov/ui201/t4201 |
| New employer, nonconstruction, small / large | 3.05% / 3.25% total | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| New construction employer, small / large | 2.50% / 2.70% total, replacing 2025's 2.90% / 3.10% | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| New-employer rating period | First three calendar years, not a fixed number of quarters | https://dwd.wisconsin.gov/ui201/t4201 |
| Experienced Schedule D total-rate range | Small 0%-12%; large 0.05%-12%, subject to actual notice and special rules | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |

For an experienced employer, use the actual UCT-100B notice and year. Reserve percentage is the account balance at June 30, including taxes paid through July 31 and benefit payments through June 30, divided by the fiscal-year taxable payroll ending June 30. Basic contributions credit the individual reserve; solvency contributions go to the shared balancing account. Special rate-change and seasonal provisions may affect the actual notice. The following is the full ordinary 2026 total-rate schedule, preserving the former rate-table topic with corrected boundaries. [DWD schedule](https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026); [Part 4 D](https://dwd.wisconsin.gov/ui201/t4201).

| Reserve percentage | Small total % | Large total % | Official source |
|---|---|---|---|
| 15% or more | 0.00 | 0.05 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| 10% to under 15% | 0.12 | 0.15 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| 9.5% to under 10% | 0.27 | 0.30 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| 9% to under 9.5% | 0.37 | 0.40 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| 8.5% to under 9% | 0.65 | 0.70 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| 8% to under 8.5% | 0.80 | 0.90 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| 7.5% to under 8% | 0.90 | 1.05 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| 7% to under 7.5% | 1.10 | 1.25 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| 6.5% to under 7% | 1.35 | 1.55 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| 6% to under 6.5% | 1.70 | 1.90 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| 5.5% to under 6% | 2.10 | 2.30 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| 5% to under 5.5% | 2.50 | 2.70 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| 4.5% to under 5% | 2.90 | 3.10 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| 4% to under 4.5% | 3.30 | 3.45 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| 3.5% to under 4% | 3.75 | 3.90 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| 0% to under 3.5% | 4.30 | 4.45 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| Overdrawn by less than 1% | 6.40 | 6.40 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| Overdrawn by 1% to under 2% | 6.90 | 6.90 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| Overdrawn by 2% to under 3% | 7.40 | 7.40 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| Overdrawn by 3% to under 4% | 7.90 | 7.90 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| Overdrawn by 4% to under 5% | 8.50 | 8.50 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| Overdrawn by 5% to under 6% | 9.05 | 9.05 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| Overdrawn by 6% to under 7% | 9.75 | 9.75 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| Overdrawn by 7% to under 8% | 10.55 | 10.55 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| Overdrawn by 8% to under 9% | 11.30 | 11.30 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |
| Overdrawn by 9% or more | 12.00 | 12.00 | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 |

Determine covered UI wages independently from withholding or federal income-tax wages. Part 3 includes salaries, commissions, bonuses, vacation/dismissal pay, accounted-for tips and certain benefits/payments in kind. Wages are reported when paid or constructively paid. Employee salary reductions to a 401(k) remain UI wages, while qualifying cafeteria-plan deductions and employer contributions have their own rules. Do not use federal W-2 box 1 as the UI base without reconciliation. [DWD wage definitions](https://dwd.wisconsin.gov/ui201/t3201).

For each employee and quarter, compute max(min(covered annual wages after this payment, $14,000) minus covered annual wages already taxed, 0), bounded by the current payment. Sum employee taxable wages and multiply by the assigned total rate. Retain total wages, excess wages and taxable wages separately. Successor/predecessor transfers and interstate wage-base credits require their specific rules before changing the running base. Never assume a nonresident's reciprocal wages are exempt from UI. [DWD Part 4 A-D](https://dwd.wisconsin.gov/ui201/t4201).

### 8. File UI tax and wage reports and make payment

Report on a calendar-quarter basis even for zero payroll. Ordinary due dates are April 30, July 31, October 31 and January 31; a weekend/state or federal holiday moves the due date to the next eligible day. DWD's employer page currently identifies fourth-quarter 2026 reports as due February 1, 2027. UI accounts with 25 or more employees file tax reports online and remain subject to electronic filing thereafter; employer agents file electronically regardless of client size. The cited handbook states a $25 paper-filing penalty for a required electronic report. [DWD Part 4 A-C](https://dwd.wisconsin.gov/ui201/t4201); [employer resources](https://dwd.wisconsin.gov/ui/employer).

In Employer Unemployment Resources choose File Tax and Wage Reports, the correct UI account/year/quarter, enter employee wage detail, reconcile total/excess/taxable wages and verify the assigned rate before submission. The online system can calculate wage-base exclusions. Retain both tax and wage report acknowledgements; an incomplete wage report is not cured by paying tax. The exact current UCT-101/UCT-7823 paper-form IDs from the earlier draft have not been tied out to the redesigned portal, so use its named tax/wage functions rather than inventing fields. [DWD Part 4 B](https://dwd.wisconsin.gov/ui201/t4201).

Pay through the account's EFT debit or another listed payment option and keep a separate payment receipt. ACH credit must be initiated at least one business day before the due date and identify the UI account in the bank's addenda; do not initiate a zero-dollar payment. The handbook distinguishes the state UI account from the FEIN used for federal wage/tax matching. Federal Form 940 and its credit calculation remain in `us-form-941-940-payroll`. [DWD Part 4 H-I](https://dwd.wisconsin.gov/ui201/t4201).

The first-quarter deferral is elective, not an automatic extension: liability must be at least $1,000, no prior quarter amounts may remain outstanding at April 30, the report and at least 40% must be received by the first due date, then 30%,20%,10% of first-quarter liability accompany timely full subsequent-quarter payments. Elect electronically between February 15 and April 30 each year and file all quarters electronically. A later default can generate interest retroactive to April 30, and deferral may affect next year's experience rate. [DWD Part 4 A](https://dwd.wisconsin.gov/ui201/t4201).

For corrections, Part 4 identifies UCT-7842-E Contribution Adjustment Report or a written quarterly breakdown, and the rate for the year underpaid. A voluntary contribution to lower a rate is different from tax payment or correction: compare cost with actual rate savings, observe the mid-October-November 30 window, and recognize the payment is irrevocable. UI closure needs its own notification/account determination; reimbursement accounts remain open for possible benefit charges. [DWD Part 4 E,F,K](https://dwd.wisconsin.gov/ui201/t4201).

### 9. Apply the actual UI contractor test and keep regimes separate

**AUDIT FLASH POINT**. For private-sector employers other than nonprofit, trucking or logging employers, DWD requires freedom from direction/control in contract and fact **and at least six of the current nine conditions**. Freedom from control is a separate gate; a worker cannot compensate for failing it by scoring more factors. Trucking/logging/government/nonprofit relationships have a different independently-established-business test. [DWD Part 2 A](https://dwd.wisconsin.gov/ui201/t2201).

| Current private-sector UI condition | Evidence to collect | Official source |
|---|---|---|
| Holds out to public as in business | Advertising, public client offers | https://dwd.wisconsin.gov/ui201/t2201 |
| Own office or chosen location and own equipment/materials | Workspace choice, ownership and access records | https://dwd.wisconsin.gov/ui201/t2201 |
| Multiple contracts with one or more employing units | Actual contracts for specific services | https://dwd.wisconsin.gov/ui201/t2201 |
| Incurs main service expenses | Unreimbursed cost records | https://dwd.wisconsin.gov/ui201/t2201 |
| Redoes unsatisfactory work without extra pay or monetary penalty | Enforceable contract and actual practice | https://dwd.wisconsin.gov/ui201/t2201 |
| Services do not directly relate to retaining entity's activities | Nature of both businesses, not merely separate legal names | https://dwd.wisconsin.gov/ui201/t2201 |
| May profit or lose under contracts | Pricing, costs and business risk | https://dwd.wisconsin.gov/ui201/t2201 |
| Recurring business liabilities/obligations | Continuing software, insurance, rent, debt | https://dwd.wisconsin.gov/ui201/t2201 |
| Not economically dependent on particular employing unit | Receipts mix and capacity to continue without that customer | https://dwd.wisconsin.gov/ui201/t2201 |

The former draft's per-job/commission-only factor and receipts-versus-expenses success factor are not the current sixth and ninth factors. Current DWD text places those concepts in its historical pre-2011 list. Do not count the same old factors as though the present test were unchanged. Document uncertainty rather than marking every box YES from a freelancer label. [DWD Part 2 A](https://dwd.wisconsin.gov/ui201/t2201).

DOR generally follows IRS classification guidance for income-tax withholding, while DWD applies its own UI test. A federal contractor conclusion is not proof of a Wisconsin UI exclusion. Workers' compensation has a separate test and scope; no automatic contractor conclusion follows there. DOR's current https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx identifies a $25,000 per-violation fine for specified willful construction withholding misclassification, rather than a generic UI fine for every contractor. DWD Part 2 instead describes construction UI false-information penalties of $500 per misclassified employee capped at $7,500 and coercion penalties of $1,000 per person capped at $10,000, plus possible criminal consequences. [DOR classification https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx question 15](https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx); [DWD Part 2 A](https://dwd.wisconsin.gov/ui201/t2201).

### 10. Other payroll obligations retained as separate checks

Report new hires/rehired employees within twenty days under W-166 p.9. Do not assume WT-4 retention, an ordinary DOR withholding filing or a federal W-4 submission satisfies the Wisconsin New Hire Program. Employer name/FEIN and employee identity/hire data should be checked against the current program specification before transmission; do not publish employee details in workpapers shared for pack review. [W-166 p.9](https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf).

Workers' compensation coverage, state wage/tipped-wage floors, final-pay timing, pay-stub contents, benefit policies and paid leave remain distinct compliance checks. They are not determined by the WT-4, UI rate, reciprocal declaration or tax return. The earlier Milwaukee ordinance narrative, accrual/caps, litigation citations and local-stacking examples have not been established from primary authority and are withdrawn from usable guidance; no payroll accrual or deduction should be set up from that text. The complete unresolved topics/figures are retained under Sources for independent checking rather than silently treated as settled law.

## Boundary and exception table

| Scenario | Required distinction |
|---|---|
| Wisconsin resident working elsewhere | Resident withholding baseline, hardship/specific Minnesota arrangement and other-state rules; do not assume reciprocity. |
| IL/IN/KY/MI employee working in Wisconsin | W-220 may exempt employee compensation; UI and WC remain separate. |
| Farm/domestic/501(c)(3) employer | Apply its own UI coverage threshold and withholding exclusions, not generic commercial rules. |
| Corporate officer or family employee | Some statutory/elective UI exclusions exist; do not assume ownership alone excludes wages. DWD Part 2 C requires an approved officer election. |
| Reimbursement financing account | Quarterly reporting continues; ordinary percentage contributions are not its funding mechanism. |
| Taxable payroll exactly $500,000 | Large UI rate category. |
| Final-year closure | DOR WT-7 due within 30 days when account closes before December 31; UI closure is separate. |
| Wage reimbursement, prior-year bonus repayment or multistate W-2 correction | Use applicable correction instructions; the old blanket W-2c/WT-7 cash-basis assertions were not verified. |

## Worked cases

### Case A: Bratwurst & Sons, Sarah and James

The invented Madison manufacturer formed in 2024 has eight employees and $420,000 total annual payroll. It is still in its first three UI calendar years in 2026 and is nonconstruction. Taxable payroll cannot exceed its $420,000 gross payroll, so the small-employer new rate applies. Sarah earns $52,000 annually, single with one WT-4 exemption, paid biweekly; assume ordinary taxable wages and no extra withholding. James earns $28,000. The corrected W-166 formula gives Sarah $88.07 per pay period; the old return-bracket method was invalid. UI reaches $427 for each, $854 for the two together.

```oa-check
name: Wisconsin Sarah withholding and two employee UI
inputs:
  salary: 52000
  periods: 26
  exemptions: 1
  james_salary: 28000
  ui_base: 14000
  new_rate: 0.0305
steps:
  - deduction: 6702 - 0.12 * (salary - 17780)
  - annual_net_wage: max(salary - deduction - 400 * exemptions, 0)
  - annual_tax: 1045.04 + 0.053 * (annual_net_wage - 25520)
  - withholding: annual_tax / periods
  - sarah_ui: min(salary, ui_base) * new_rate
  - james_ui: min(james_salary, ui_base) * new_rate
  - total_two_ui: sarah_ui + james_ui
expected:
  deduction: 2595.6
  annual_net_wage: 49004.4
  annual_tax: 2289.71
  withholding: 88.07
  sarah_ui: 427
  james_ui: 427
  total_two_ui: 854
```

If the same invented employer has $12,000 annual withholding remittances, it falls in the monthly frequency-review band, not the old >$5,000 semi-monthly band. The actual DOR assignment controls until changed. WT-7 covers the calendar year's wages; its recurring January 31 deadline moves for weekends/holidays. Do not put a 2025-wage filing date on a 2026 reconciliation.

### Case B: Cheese & Cracker Co. and David, reciprocity/UI split

The invented Kenosha employer's Illinois-domiciled employee David earns $75,000 working entirely in Wisconsin. His qualifying W-220 is on file, no dual-residence exception applies and his only Wisconsin income is reciprocal wages. Wisconsin income withholding is zero while reciprocity remains valid; the declaration does not expire annually. Determine Illinois withholding using that state's skill. Assume DWD has assigned a valid 2026 experienced total rate of 1.35% and his services are covered in Wisconsin. His UI contribution base reaches $14,000 and employer tax is $189. Income reciprocity does not produce zero UI.

```oa-check
name: Wisconsin David reciprocity and UI decision
inputs:
  wages: 75000
  reciprocity_fraction: 1
  ui_rate: 0.0135
steps:
  - wi_wages_requiring_withholding: wages * (1 - reciprocity_fraction)
  - taxable_ui: min(wages, 14000)
  - ui_due: taxable_ui * ui_rate
expected:
  wi_wages_requiring_withholding: 0
  taxable_ui: 14000
  ui_due: 189
```

If David moves to Wisconsin, reevaluate the declaration on the actual move date and begin required Wisconsin withholding. A refund of wrongly withheld Wisconsin income tax follows the applicable state process; do not invent a home-state rate, W-2 box pattern or universal employer-refund prohibition. UI localization and workers' compensation remain separate factual determinations.

### Case C: Lakefront Web Design and Maya, current factors

The invented Lakefront Web Design LLC engages Maya for ten logos at $4,800 each. She chooses a home studio, owns equipment, advertises publicly, has five other clients, bears service expenses, must redo unsatisfactory work without extra pay, and pays ongoing business costs. On the stated facts, the worker appears free from control, but verify actual practice. Graphic design directly relates to the retaining web-design business, so do not mark the unrelated-services factor YES. Profit/loss risk and absence of economic dependence require their own evidence; five other clients alone does not establish their revenue weight.

Suppose the reviewer documents freedom from control and six supported current factors: public business, chosen location/equipment, multiple contracts, main expenses, uncompensated rework and recurring liabilities. The six-factor gate is met even though the other three are not established. If the revised facts instead require fixed hours, employer software and direct supervision, failure of freedom from control defeats the exclusion irrespective of the factor count. This illustrates the decision, not a binding agency determination or a federal/WC conclusion.

```oa-check
name: Wisconsin Maya current UI gate
inputs:
  logos: 10
  fee_per_logo: 4800
  supported_factors: 6
  free_from_control: 1
  revised_free_from_control: 0
steps:
  - receipts: logos * fee_per_logo
  - exclusion_gate_met: free_from_control * min(floor(supported_factors / 6), 1)
  - revised_gate_met: revised_free_from_control * min(floor(supported_factors / 6), 1)
expected:
  receipts: 48000
  exclusion_gate_met: 1
  revised_gate_met: 0
```

## When to refuse or refer

Refer disputed classification, agency audits, coercion, intentional underwithholding, penalties/abatement, cross-border localization, successor wage histories, public/tribal/reimbursement financing, fringe-benefit exclusions, officer elections, out-of-state carrier/military/disaster exceptions and benefit-policy disputes. Do not treat a W-220, federal 1099 or incorporation document as a complete conclusion across all payroll regimes. Missing actual pay data/certificates/rate notices prevent final payroll computation. No contact with an accountant is implied by this skill; the user must arrange professional sign-off through the normal engagement.

## Filing and payment

Maintain separate calendars for DOR WT-6/WT-7 and DWD quarterly tax/wage reports. Report actual withholding, reconcile year-end wage statements and file required zero returns; then separately check payment settlement. Never put UI payments in a withholding deposit or reduce an employee's taxable income by employer UI. For 2026 wages the recurring January 31 annual/quarter-four deadlines fall on a Sunday, so the ordinary next-business-day rule gives February 1, 2027, absent a special extension. [DOR https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx](https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx); [DWD Part 4](https://dwd.wisconsin.gov/ui201/t4201).

| DOR withholding delinquency item / condition | Published consequence | Official source |
|---|---|---|
| Delinquent withholding deposits/payments | 1.5% interest per month; during a granted extension, 1% monthly | https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx |
| Willful neglect, not reasonable cause, late withholding report/deposit | $50 late fee, or $150 for specified corporation/insurance filers | https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx |
| Willful neglect, incorrect/incomplete report or failure to withhold/deposit/pay | 25% of amount not reported or withheld, subject to statutory conditions | https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx |
| Incorrect/late wage statement | $10 per violation under cited conditions | https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx |

The prior draft's automatic 5%-monthly deposit penalty, 1%-monthly ordinary delinquency interest and generic 50% fraud penalty are not substituted for the current source. DOR's https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx additionally describes intentional failure liability, construction-specific misclassification fines and possible criminal consequences; refer the notice and facts. Current UI late-report penalties/interest must be confirmed from their own DWD/statutory sources, not copied from withholding or an old asserted 0.75% compound rate.

## Completion checklist

- Tie each payroll run to residence/workplace evidence, current certificates, employer identity and account notices.
- Use the approved W-166 method, correct annualization and $400 withholding exemption; retain a period-level recomputation.
- Separate supplemental wages, income-tax exemptions, UI coverage and wage-base exclusions.
- Use taxable payroll for the UI size boundary and the actual year's assigned total rate including solvency.
- Reconcile DOR deposit periods to WT-7 and W-2/1099 submissions, and UI tax report to employee wage detail.
- Check filing and bank acknowledgements, zero periods, closures and corrections separately.
- Identify unconfirmed wage-law/classification issues and provide a source-linked brief for qualified review.

## Sources

| Official source / section read | URL | Read on |
|---|---|---|
| DOR W-166, January 2026, pp.5-10 and 25-27. Read for registration, certificates/quarter-end submission, new hires, Minnesota arrangement, approved payroll deduction/exemption and supplemental/alternate formulas. Wage-table cells outside these sections were not exhaustively audited. | https://www.revenue.wi.gov/DOR%20Publications/pb166.pdf | 2026-11-13 |
| DOR General Withholding Tax Questions, questions 1-15, April 2026 law statement. Read for coverage/exceptions, electronic/zero filing, WT-6/WT-7 dates, extension, wage statements, closure, records, penalties and classification. | https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx | 2026-11-13 |
| DOR Annual Filing Frequency Scan, November 2026 law statement. Read for actual withholding remittance bands, review period and effective notices. | https://www.revenue.wi.gov/Pages/Businesses/Filing-Frequency-Changes.aspx | 2026-11-13 |
| DOR 2026 WT-4A worksheet, both pages. Read for reduced-withholding agreement procedure, ten-day copy, estimate reconciliation and April 30, 2027 expiration. | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf | 2026-11-13 |
| DOR Publication 121, January 2026, pp.3-5, 2025-2026 filing cycle. Read for compensation scope, dual-residence exceptions, W-220 continuing effect and refund/return distinction. | https://www.revenue.wi.gov/DOR%20Publications/pb121.pdf | 2026-11-13 |
| DWD 2026 Tax Rate Schedule, complete current table, normal browser. Read for Schedule D, all 26 reserve bands, size boundary, basic/solvency totals and both construction/nonconstruction new-employer columns. | https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026 | 2026-11-13 |
| DWD UCB-201-P Part 1 A-C, normal browser. Read for coverage, retroactivity, sector thresholds, registration and reimbursement boundary. | https://dwd.wisconsin.gov/ui201/t1201 | 2026-11-13 |
| DWD UCB-201-P Part 2 A-D, normal browser. Read for current versus historical contractor factors, special-industry tests, construction penalties and statutory/elective exclusions. | https://dwd.wisconsin.gov/ui201/t2201 | 2026-11-13 |
| DWD UCB-201-P Part 3 A-B, normal browser. Read for paid/constructively paid UI wages, cafeteria/retirement/fringe distinctions and casual labor. | https://dwd.wisconsin.gov/ui201/t3201 | 2026-11-13 |
| DWD UCB-201-P Part 4 A-K. Read for reporting, wage base, due dates, electronic requirements, rate calculation, deferral, corrections, payments and closure. | https://dwd.wisconsin.gov/ui201/t4201 | 2026-11-13 |
| DWD Employer Unemployment Resources, normal browser. Read for live new-account/tax-wage filing links, separate UI services and February 1, 2027 quarter-four deadline. | https://dwd.wisconsin.gov/ui/employer | 2026-11-13 |

Not yet confirmed: default status when no initial WT-4 is supplied; complete final 2026 wage-statement specifications and corrected W-2/bonus-repayment procedures; all W-166 wage-table cells and unusual certificate statuses; detailed current UI interstate localization, same-employer/predecessor wage-base credit, transfer/rate-change restrictions and paper UCT-101/UCT-7823 identifiers; UI late-report fee (old $50 minimum), late-payment interest (old 0.75% compound) and all criminal/audit limitation rules; WC coverage/exemptions and separate contractor test (old three-worker/$500/any-construction-worker and officer/family assertions not carried forward); final wages, benefit-forfeiture and pay-stub enforcement (old double damages/$100 figures not confirmed); new-hire data specification and old $25/$500 penalties; state/tipped minimum wages and local preemption (old $7.25/$2.33 figures not confirmed here); the old purported Milwaukee 2024 ordinance/2025 start, 80-hour coverage, one-hour-per-30 accrual, 40/72-hour caps, 40-hour carryover, three-year records, $1,000 penalties, court/AB41 chronology and municipal stacking claims. Those Milwaukee assertions have no established primary-source basis in this pass and must not drive accruals, deductions or advice. Federal rates, other-state withholding figures, federal classification and federal payroll corrections remain in their owner skills.
