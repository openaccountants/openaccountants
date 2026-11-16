---
name: fj-payroll-social
description: Compute 2026 Fiji employment income tax with the current resident and non-resident bands and cumulative primary-employment PAYE formula. Reconcile statutory FNPF totals by wage month, employee coverage and filing records. Keep the unresolved post-August employee-recovery split separate from the confirmed total. Do not stack obsolete SRT or ECAL on income or finalise uncertain deductions, wages or benefit valuations.
jurisdiction: FJ
category: payroll
tax_year: 2026
last_updated: 2026-11-16
version: 0.2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Fiji payroll and social contributions v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Compute ordinary Fiji employment-income tax for 2026 and reconcile employer withholding, covered FNPF contributions and net-pay records. The currency is FJD and the ordinary tax year is the calendar year. Primary and secondary employment, tax residence, taxable employment income and FNPF coverage are separate determinations. This file preserves the high-earner, non-resident, minimum-wage, bank-classification, remittance and employer-cost topics; unsupported old rules are corrected or held, not silently treated as zero.

The old payroll added separate Social Responsibility Tax (SRT) and ECAL on income to obsolete capped income-tax bands. That is wrong for 2026. The current individual table incorporates higher income-tax bands; do not add those former levies. [Income Tax Act amendment 2023 ss. 2-3, 8-12](https://www.frcs.org.fj/wp-content/uploads/2023/07/Act-5-Income-Tax-Budget-Amendment.pdf); [LN 55-56 of 2023](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf); [FRCS current PAYE notice](https://frcs.org.fj/public-notice/customer-service-new-pay-as-you-earn-paye-structure/).

A second unresolved issue affects post-August FNPF deductions. The enacted total contribution reduction is clear, but the old statutory employee-recovery fraction was not amended by the same Act. The agency's stated split is reported as a conflict below, outside the usable deduction rates. Do not finalise a payslip or employer-cost split on that unresolved branch.

### Quick reference

| Item | Rule and conditions | Official source |
|---|---|---|
| Tax year | Calendar year, subject to the Act's separate substituted-year provisions; do not use a fiscal-budget year as the ordinary employee tax year | [Income Tax Act s. 2](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf) |
| Resident annual nil band | First FJD 30,000 of chargeable income; only for a resident, with chargeable-income and period facts established | [LN 55 of 2023 Schedule para. 1](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf) |
| Resident annual income tax | Marginal bands reach 39%; the old 20% cap is not current | [LN 55 of 2023 Schedule para. 1](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf) |
| Non-resident annual income tax | No resident nil band; 20% in the initial bands, then higher marginal bands, not flat on all income | [LN 55 of 2023 Schedule para. 1](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf) |
| Primary-employment withholding | Cumulative Regulation 6 formula with actual normal pay, earlier pay, tax withheld, period counts and bonus/director/overtime facts | [LN 56 of 2023 reg. 3](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf) |
| PAYE payment | End of the calendar month following the month in which tax was required to be withheld, not a general fifteenth-day rule | [Income Tax Act ss. 116-118](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf) |
| PAYE finality/no-return | Conditional; concurrent employments defeat the cited salary-only exception, and other income still needs its own return analysis | [Income Tax Act ss. 105, 125](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf) |
| FNPF total before August | 18% of covered total wages for the month, before the temporary 2026 override; apply statutory rounding and exemption tests | [Act 13 of 2014 s. 2](https://www.parliament.gov.fj/wp-content/uploads/2017/03/ACT-No-13-FNPF-Budget-Amendment.pdf?ver=1794354122); [Act 13 of 2023 s. 5](https://www.parliament.gov.fj/wp-content/uploads/2023/07/Act-13-Fiji-National-Provident-Fund-Budget-Amendment.pdf?ver=1794354122) |
| FNPF employee recovery before August | Derived: 8% of the same wage base from the statutory recovery fraction applied to the ordinary total, with the Act's rounding rule | [Act 13 of 2014 s. 3; Act ss. 37, 39](https://www.parliament.gov.fj/wp-content/uploads/2017/03/ACT-No-13-FNPF-Budget-Amendment.pdf?ver=1794354122) |
| FNPF employer cost before August | Derived: 10% of the same covered wage base, being the ordinary total less employee recovery, subject to rounding | [Act 13 of 2014 ss. 2-3](https://www.parliament.gov.fj/wp-content/uploads/2017/03/ACT-No-13-FNPF-Budget-Amendment.pdf?ver=1794354122) |
| FNPF total from August | 16% of covered total wages for the month from 1 August 2026 to 31 July 2027, rounded to the nearest cent | [Act 21 of 2026 ss. 1-2, new s. 37(4A)](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-21-Fiji-National-Provident-Fund-Budget-Amendment-Act-2026.pdf?ver=1794354122) |
| FNPF remittance statement | No later than the first 14 days of the following month under the amended statement provision; separate from payment | [Act 11 of 2024 ss. 1, 4](https://frcs.org.fj/files/2024/08/Act-11-Fiji-National-Provident-Fund-Budget-Amendment-Act-2024.pdf) |
| FNPF payment | No later than the last day of the following month; not automatically its last working day | [Decree 77 of 2012 s. 8, amending s. 37(1)](https://myfnpf.com.fj/wp-content/uploads/2019/09/FNPF_AMENDMENT_DECREENo__77.pdf) |
| FNPF late-payment penalty | 10% of the outstanding balance for each month contributions remain unpaid, effective 1 January 2025; apply to the actual outstanding balance, not gross wages | [Act 11 of 2024 ss. 1, 5](https://frcs.org.fj/files/2024/08/Act-11-Fiji-National-Provident-Fund-Budget-Amendment-Act-2024.pdf) |

## Ask the client first

Read the case records and existing payroll before asking for facts. Minimum inputs for a real withholding calculation are tax year, pay date and wage period, pay frequency and actual number of periods, residency, primary/secondary tax-code declaration or special certificate, normal gross pay, all earlier normal pay and withholding for the year, bonuses/overtime/directors' remuneration, other one-off payments, and any FRCS direction. Annual income alone does not establish each pay-period deduction.

For contributions obtain citizenship and residency separately, age, FNPF membership/status, employer registration and member number, wage components and month payable, any actual exemption/admission, voluntary-contribution direction and Board confirmation, and statutory rate-period facts. TIN, employment start/end dates, contract, sector/occupation, hours, leave, payslip history and bank evidence are also needed. Non-cash benefits, redundancy and final pay have separate rules and must not be valued from the bank statement.

Do not assume monthly frequency, a primary code, a below-threshold income, FNPF-mandatory status from age alone, or ordinary wages excluding allowances. If no voluntary direction is evidenced, do not invent one. A missing business-use or benefit valuation remains an open item; it is not a legal exemption. Check the applicable sector instrument before declaring compliance with a national minimum wage.

## The method, step by step

### 1. Separate tax residence, employment classification and the bases

Use the Income Tax Act's resident-individual definition and the actual travel/home facts. Section 6 has separate arrival-year and departure-year residence branches; do not grant a full-year treatment blindly from one current address. A non-resident has different rates and no resident nil band. Citizenship or FNPF membership does not decide income-tax residence. Confirm employment rather than contractor income before using PAYE; particular FNPF deeming provisions can cover persons not described as employees in an ordinary payroll export. [Income Tax Act ss. 2, 6, 15, 111](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf); [FNPF Act s. 4](https://www.rbf.gov.fj/wp-content/uploads/2020/03/Fiji-National-Provident-Fund-Decree-No.-52-of-2011.pdf).

Build taxable employment income from the actual remuneration and statutory inclusions/exemptions. Distinguish gross pay, chargeable income, net bank salary, reimbursed costs, employee deductions and employer contributions. Do not automatically reduce taxable employment pay by employee FNPF contributions or subtract employee tax withheld from the employer's gross wage expense. The withholding obligation is not reduced because another deduction is due. [Income Tax Act ss. 15, 22-23, 111](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf).

Termination, redundancy, leave-on-termination, fringe benefits and other non-cash benefits remain separate work. Preserve their records and potential liabilities and refer the exact valuation/timing questions rather than assuming every payment is regular salary. Income at a high band is not itself evidence of a separate SRT or ECAL charge.

### 2. Apply the current annual income-tax table

The following rates came into force for individuals from 1 January 2024 and are the continuing table confirmed by the current FRCS PAYE notice. Read annual chargeable income C against the band; tax is the base plus the marginal rate on C above that band's lower limit. The table is an annual tax function T(C), not permission to ignore cumulative withholding. [LN 55 of 2023 ss. 1, 3(a)](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf); [FRCS notice](https://frcs.org.fj/public-notice/customer-service-new-pay-as-you-earn-paye-structure/).

| Annual chargeable-income band, FJD | Resident income-tax rate and amount | Non-resident income-tax rate and amount | Official source |
|---|---|---|---|
| Up to 30,000 | Nil | 20% of C | [LN 55 Schedule para. 1](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf) |
| Above 30,000 up to 50,000 | 18% × (C - 30,000) | 6,000 plus 20% × (C - 30,000) | [LN 55 Schedule para. 1](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf) |
| Above 50,000 up to 270,000 | 3,600 plus 20% × (C - 50,000) | 10,000 plus 20% × (C - 50,000) | [LN 55 Schedule para. 1](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf) |
| Above 270,000 up to 300,000 | 47,600 plus 33% × (C - 270,000) | 54,000 plus 33% × (C - 270,000) | [LN 55 Schedule para. 1](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf) |
| Above 300,000 up to 350,000 | 57,500 plus 34% × (C - 300,000) | 63,900 plus 34% × (C - 300,000) | [LN 55 Schedule para. 1](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf) |
| Above 350,000 up to 400,000 | 74,500 plus 35% × (C - 350,000) | 80,900 plus 35% × (C - 350,000) | [LN 55 Schedule para. 1](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf) |
| Above 400,000 up to 450,000 | 92,000 plus 36% × (C - 400,000) | 98,400 plus 36% × (C - 400,000) | [LN 55 Schedule para. 1](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf) |
| Above 450,000 up to 500,000 | 110,000 plus 37% × (C - 450,000) | 116,400 plus 37% × (C - 450,000) | [LN 55 Schedule para. 1](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf) |
| Above 500,000 up to 1,000,000 | 128,500 plus 38% × (C - 500,000) | 134,900 plus 38% × (C - 500,000) | [LN 55 Schedule para. 1](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf) |
| Above 1,000,000 | 318,500 plus 39% × (C - 1,000,000) | 324,900 plus 39% × (C - 1,000,000) | [LN 55 Schedule para. 1](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf) |

In each expression, the rate multiplies **the excess over the named lower limit**, not C followed by a separate subtraction of the lower limit. For example T(320,000) for a resident is 57,500 + 0.34 × (320,000 - 300,000). The nil band is not a separate deduction applied again to those base amounts.

**SRT and ECAL history:** keep historical SRT/ECAL columns only to reconcile an earlier year's payroll. No separate SRT or ECAL-on-income calculation is added to the 2026 table. The 2023 Act removes SRT provisions and the ECAL income provision; LN 56 replaces the withholding formula and deletes obsolete rules. The FRCS notice explicitly provides the new template excluding both. A historical arrears/assessment line must retain its actual tax year rather than being recoded automatically to zero. [Act 5 of 2023 ss. 1-3, 8-12](https://www.frcs.org.fj/wp-content/uploads/2023/07/Act-5-Income-Tax-Budget-Amendment.pdf); [LN 56 regs. 2-5](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf); [FRCS PAYE notice](https://frcs.org.fj/public-notice/customer-service-new-pay-as-you-earn-paye-structure/).

### 3. Compute primary-employment PAYE cumulatively

Obtain a valid P tax-code declaration. The amended Regulation 6 formula is:

```text
T(C) = annual income tax using the applicable resident/non-resident table
A1 = T(C1)
C1 = D × (F - G + 1) + E
C2 = C1 + H
PAYE to withhold = max((A1 / F × G) - B1 + T(C2) - T(C1), 0)
```

D is the current period's normal basic gross pay. E is normal pay in earlier periods in the tax year. F is the number of payment periods in the tax year. G is completed periods including the current period. B1 is income tax withheld to date. H is total directors' remuneration and bonus/overtime paid to date, including the current period. If the pay period is the same as the previous period, use the previous period's C1 as directed by the regulation. Keep one-off and normal pay distinguishable; the regulation's special/uncertain-payment branches still apply. [LN 56 of 2023 reg. 3, amended reg. 6(2)](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf).

The old annual-tax/divisor shortcut only reproduces this result for the stated stable-pay facts with no bonus and the matching withholding history. Do not use it for a mid-year starter/leaver, variable pay, arrears, repeated pay-period run, director's payment or bonus without the required history. PAYE cannot be negative under this formula. For uncertain withholding, the Regulations provide for written clarification from FRCS; do not invent a new tax-code rate. [Income Tax (Withholding Tax) Regulations reg. 6(3)-(6)](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf).

Employees must give their tax-code declaration within 5 working days of starting or the permitted later time. A person can use a P declaration with only one concurrent employer; secondary employment uses an S declaration and its actual applicable S-code rate or Special Tax Rate Certificate. Do not feed secondary pay into a separate resident-threshold computation. Missing declarations and disputed codes require the actual prescribed/FRCS treatment, not an assumed P code. [Withholding Regulations regs. 5, 7-8](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf).

### 4. Establish FNPF coverage and covered wages

The original Act defines wages broadly as money payable under the employment contract before deductions, and excludes genuine employment reimbursements. It also expands employee/employer definitions to specified manual-labour, apprenticeship, commission/success-fee and vessel/aircraft arrangements. Certain service-remuneration dividends can be deemed wages. Do not automatically exclude allowances, overtime, bonuses or every commission, or classify every contractor solely from the PAYE label. [FNPF Act s. 4(1)-(6)](https://www.rbf.gov.fj/wp-content/uploads/2020/03/Fiji-National-Provident-Fund-Decree-No.-52-of-2011.pdf).

The base Act's exempt-employee definition includes an employee under age 15, specified outworkers/detained persons, wages below the prescribed monthly amount, certain diplomatic personnel, and a person employed in Fiji who is not a citizen unless admitted with the employer's agreement under section 36(2). It also permits a specific Board exemption for qualifying overseas employment arrangements; an overseas pension alone is not the declaration. The 2014 Regulations prescribe the low-wage amount as FJD 28 per month. Do not extrapolate this to an unverified contribution floor or ceiling. [FNPF Act ss. 4, 35-36](https://www.rbf.gov.fj/wp-content/uploads/2020/03/Fiji-National-Provident-Fund-Decree-No.-52-of-2011.pdf); [2014 Regulations reg. 3](https://myfnpf.com.fj/wp-content/uploads/2019/09/FNPF_Regulations_2014.pdf).

The current agency page asks employers to register new employees aged 15 or over who are not already members. Read that together with the statutory exceptions, citizenship/admission and the actual employee record. A tax non-resident may be a citizen or admitted member; a foreign employee's immigration status is not a tax-residence test. Obtain the operative exemption or admission before calculating a foreign employee's deduction. The whole current consolidated membership/amendment chain and any particular Board decision have not been certified by this scoped read; uncertain coverage stays held. [FNPF employer guidance](https://myfnpf.com.fj/employers/); [FNPF Act ss. 4, 36](https://www.rbf.gov.fj/wp-content/uploads/2020/03/Fiji-National-Provident-Fund-Decree-No.-52-of-2011.pdf).

Registration, continued membership and retirement withdrawals are not identical. The 2025 Act changes the readmission wording to two further occasions from September 2025. Do not stop contributions automatically at a presumed retirement age without the actual membership and employment facts. Voluntary contributions require the actual direction and Board procedure, not an invented employee election. [Act 23 of 2025](https://www.parliament.gov.fj/wp-content/uploads/2025/08/Act-23-Fiji-National-Provident-Fund-Amendment-Act-2025.pdf); [Act s. 38 as amended in 2012](https://myfnpf.com.fj/wp-content/uploads/2019/09/FNPF_AMENDMENT_DECREENo__77.pdf); [2014 Regulations reg. 19](https://myfnpf.com.fj/wp-content/uploads/2019/09/FNPF_Regulations_2014.pdf).

### 5. Use the wage month's contribution rule and preserve the recovery conflict

Before August 2026 the ordinary total is the amended section 37 rate, with the temporary pandemic Division 3A deleted from January 2024. The Act's ordinary contribution and employee-recovery provisions use upward cent rounding. Record exact wage-month totals and round at the statutory step; the employer's own cost is the total less the lawful employee recovery, plus any separately authorised employer addition. [Act 13 of 2014 ss. 2-3](https://www.parliament.gov.fj/wp-content/uploads/2017/03/ACT-No-13-FNPF-Budget-Amendment.pdf?ver=1794354122); [Act 13 of 2023 s. 5](https://www.parliament.gov.fj/wp-content/uploads/2023/07/Act-13-Fiji-National-Provident-Fund-Budget-Amendment.pdf?ver=1794354122); [base Act ss. 37-39](https://www.rbf.gov.fj/wp-content/uploads/2020/03/Fiji-National-Provident-Fund-Decree-No.-52-of-2011.pdf).

From August the enacted temporary override sets the total at 16% of covered wages, rounded to the nearest cent. It is a defined temporary period, not a permanent whole-2026 rate or a confirmed post-July-2027 rule. Split a calendar-year reconciliation by actual wage month; do not apply the old employer cost percentage to the full year. [Act 21 of 2026](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-21-Fiji-National-Provident-Fund-Budget-Amendment-Act-2026.pdf?ver=1794354122).

**Unresolved employee-recovery conflict, not usable as a payslip instruction:** the FNPF employer page states employee 8% and employer 8% during the temporary period. The read section 39 amendment instead permits recovery of “8/18 or 44.4% (whichever is the greater)” of mandated contributions. Applying that unchanged fraction to the new total does not yield the agency's employee percentage. Act 21 changes the total provision but does not expressly amend section 39. No later operative recovery amendment was found in this read. Preserve both actual sources and obtain the applicable current legal instrument before finalising the employee deduction or employer-cost split. Do not choose a new recovery fraction, silently call the agency split enacted, or assume a voluntary top-up authorises the difference. [Act 13 of 2014 s. 3](https://www.parliament.gov.fj/wp-content/uploads/2017/03/ACT-No-13-FNPF-Budget-Amendment.pdf?ver=1794354122); [Act 21 of 2026 s. 2](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-21-Fiji-National-Provident-Fund-Budget-Amendment-Act-2026.pdf?ver=1794354122); [FNPF agency statement](https://myfnpf.com.fj/employers/).

A total contribution can be calculated separately where coverage and wages are established, but it does not establish a final employee net salary. The examples below therefore retain confirmed annual tax and pre-August contribution illustrations and expressly hold unsupported full-year/post-August splits.

### 6. Register, report, remit and reconcile

Register the employer for PAYE within 30 days of commencing the trade, business, profession or vocation under Regulation 4, and obtain the employee's TIN/declaration and actual FRCS obligation. Withhold when the payment is applied, credited, paid or otherwise made available under the statutory timing rule. Remit by the end of the following calendar month. A failure to withhold/pay can make the payer personally liable; it is not excused by an employee's net-pay agreement. [Income Tax Act ss. 111, 116-118; Withholding Regulations reg. 4](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf).

Use the current FRCS TPOS PAYE template, with normal pay, one-offs, withholding-to-date and the correct employee code. The published new template excludes SRT and ECAL. Do not invent TPOS box numbers or assume every taxpayer has the same report frequency. Section 121 excludes employment-income final withholding from its general monthly-summary rule, while Regulation 17 has its own prescribed reporting branches. Check the actual employer's current electronic obligation before declaring filing complete; the payment deadline is a separate rule. [Income Tax Act s. 121, Withholding Regulations reg. 17](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf); [FRCS notice](https://frcs.org.fj/public-notice/customer-service-new-pay-as-you-earn-paye-structure/).

Give the employee the prescribed Tax Withholding Certificate. Regulation 18(1) provides the last day of February following the year for its issue, with special deceased/departing-person branches. LN 56 deletes the old subregulation requiring the payer's duplicate annual copy; do not resurrect that filing from historical text. Keep gross employment pay, each deduction, tax-code declarations, acknowledgements and payment references. [Income Tax Act s. 120, Withholding Regulations regs. 10-12, 16, 18, 20-22](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf); [LN 56 regs. 4-5](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf).

FNPF registration on engagement requires the prescribed return within 4 weeks under Regulation 7(2), rather than assuming a vague later payroll anniversary. Record employer/member numbers and actual exemptions. Submit the following month's remittance statement within its first 14 days and pay by its last day. An approved schedule produces an invoice in the agency workflow; match the invoice and bank remittance to the correct wage month and never mistake a pending schedule for payment. Keep the statement deadline separate from the payment date. [FNPF Act s. 35 and 2014 Regulations regs. 7-10, 18, 23](https://myfnpf.com.fj/wp-content/uploads/2019/09/FNPF_Regulations_2014.pdf); [2012 payment amendment s. 8](https://myfnpf.com.fj/wp-content/uploads/2019/09/FNPF_AMENDMENT_DECREENo__77.pdf); [2024 statement amendment s. 4](https://frcs.org.fj/files/2024/08/Act-11-Fiji-National-Provident-Fund-Budget-Amendment-Act-2024.pdf); [agency payment workflow](https://myfnpf.com.fj/employers/).

Retain FNPF employee/wage/deduction/payment records and remittance documents for 7 years after the transaction. The regulation also requires changes in employer details to be notified within 3 months and cessation of an employee within 1 month. Payroll/tax records must support ascertainment of liability under the tax law; do not discard them because the annual salary was below a tax band. [FNPF Regulations regs. 17, 23](https://myfnpf.com.fj/wp-content/uploads/2019/09/FNPF_Regulations_2014.pdf); [Tax Administration Act s. 34 and 2026 amendment s. 4](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-13-Tax-Administration-Budget-Amendment-Act-2026.pdf?ver=1794354122).

### 7. Finality, penalties, wages and corporate-tax boundaries

PAYE finality under section 125 and the section 105 no-return exception are conditional. Concurrent employments during any part of the year prevent the stated salary-only treatment. Other business, rental or investment income must be tested separately; a salary bank description does not certify no annual return. Nor does finality mean the employer can ignore correct cumulative withholding or certificates. [Income Tax Act ss. 105, 125](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf).

The enacted FNPF late-payment penalty is confirmed in the quick reference. Determine the outstanding contribution balance and months and keep assessment/waiver and payment evidence. Other FRCS filing/payment penalties and interest are not calculated here because their exact applicable current branches and facts have not been read sufficiently. Preserve the notice and dates; do not treat this limitation as a nil penalty or copy the old unsupported figures. [Act 11 of 2024 s. 5](https://frcs.org.fj/files/2024/08/Act-11-Fiji-National-Provident-Fund-Budget-Amendment-Act-2024.pdf).

**Minimum wages remain a separate legal check.** The Government's 2024-2025 Budget address announced FJD 4.50 from August 2024 and FJD 5.00 from April 2025, with sector changes and a construction-foreman illustration of FJD 7.54. The actual current 2026 wage regulation and occupation-specific conditions were not read here. These announcements are retained as historical context, not certified current minimum-wage guidance. Obtain the operative national/sector instrument and employment facts before approving wage compliance. The raw hourly-pay case below is arithmetic on supplied inputs. [Government address, National Minimum Wage section](https://www.fiji.gov.fj/2024-2025-national-budget-address/).

**Corporate income tax is context, not an employee deduction.** LN 55 supplies the ordinary company rate and the distinct listed-company transitional branch, including its listing-period condition. Do not apply a concession to every employer or offset company income tax against PAYE/FNPF. Route a company-income-tax calculation and any deduction for additional employer contributions to `fj-corporate-income-tax`, with the actual tax year, company class and statutory conditions. The agency's advertised additional-contribution incentive is not confirmed by this payroll read. [LN 55 regs. 2-3](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf); [Income Tax Act s. 23](https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf).

### 8. Reconcile bank patterns and deliver the working paper

| Original pattern | Evidence and classification control |
|---|---|
| SALARY, PAY, WAGES, NET PAY | Reconcile net bank salary to gross payslip, PAYE, lawful employee contribution and other authorised deductions; do not reconstruct gross by assuming old levy percentages. |
| FORTNIGHT PAY, MONTHLY SALARY | Confirm frequency, period number and year-to-date normal pay/withholding before the cumulative calculation. |
| BACK PAY, ARREARS | Identify the period and payment type and rerun the actual cumulative formula or obtain the required special treatment. |
| FNPF REFUND, FNPF ADJUSTMENT | Match fund statement and cause; do not classify every fund refund as ordinary salary or as automatically non-taxable. |
| FRCS, PAYE, TAX REMITTANCE, TPOS | Match the actual tax-year liability and remittance; old-year SRT/ECAL may need historical reconciliation but are not fresh 2026 deductions. |
| FNPF, FNPF CONTRIBUTION, FNPF EMPLOYER | Split employee withholding, employer cost, voluntary additions and penalties only after the wage-month and recovery basis is established. |
| NET WAGES, PAYROLL RUN, SALARY DISBURSEMENT | Reconcile the sum of employee net pays to actual payments and outstanding payroll liabilities. |
| FNPF VOLUNTARY | Obtain the actual written direction/approval or employer policy and Board procedure; do not infer an election from narration. |
| INTERNAL TRANSFER, OWN ACCOUNT | Match both sides of the same owner's transfer before excluding it. |
| LOAN, ADVANCE REPAYMENT | Separate principal, deduction and remuneration; an advance may still be salary or a benefit under its actual facts. |
| EXPENSE REIMBURSEMENT | Reconcile receipts and the contract; genuine employment reimbursements are excluded from FNPF wages by its definition, but a cash allowance is not proved to be one. |

These patterns are review cues, not statutory exemptions. Preserve unsupported amounts in an open-items schedule. Do not turn a blank fact into zero income or a legally deductible contribution.

Retain the original working-paper purpose and columns A-O, correcting the obsolete calculations:

| Column | Required content |
|---|---|
| A-C | Employee name, TIN, FNPF member number and confirmed employer |
| D-E | Tax residence, P/S code/certificate, wage month, pay date, frequency and current period number |
| F | Gross pay, split normal pay, bonus/overtime/director remuneration, other one-offs and separately established FNPF wages |
| G-H | E, F, G, H, B1 inputs to the cumulative formula; projected annual chargeable income and annual tax function |
| I-J | Historical SRT/ECAL reconciliation only where an earlier tax period actually requires it; no separate 2026 levy added |
| K | Current-period PAYE from the cumulative/special-code rule, not annual tax plus obsolete levies divided blindly |
| L-M | Lawful employee FNPF recovery and other authorised deductions; net pay, held if the applicable recovery branch is unresolved |
| N-O | Statutory total FNPF, employer's supported own cost/additions and total employer cost; no invented post-August split |

Add source-document IDs, prior-period totals, rounding, exemption/direction evidence, returns, due dates, notices, amounts paid, acknowledgements and held questions. Reconcile PAYE withheld to FRCS paid plus outstanding liability; total FNPF to paid plus outstanding by wage month; and net pay to employee bank disbursements. Do not book employee withholding as an additional employer salary cost or deduct the same liability twice.

Terminology remains: FRCS is the revenue authority; FNPF the provident fund; PAYE employment-income withholding; TPOS the FRCS portal; TIN the tax ID; WRO a sector wage instrument; SRT/ECAL historical levy names. “Ordinary wages” in an old export is not a substitute for the Act's total-wages definition. Consult the labour authority's current instrument rather than relying on an old ministry abbreviation.

## Worked cases

All six original raw case inputs remain. Annual chargeable income equals gross only where expressly assumed below. The annual tax function is not itself proof of a particular period's PAYE. Contribution illustrations on a pre-August wage base are expressly additional scenario facts, not an assumption that all annual wages were paid before August. No unsupported post-August employee-recovery split is used.

### Case 1: resident annual gross ordinary wages 20,000

**Original input:** Resident, annual gross ordinary wages FJD 20,000.

Assume full-year resident ordinary taxable employment income, no excluded benefit or other chargeable amount. Annual income tax is zero. For the separate stated scenario in which a confirmed covered wage amount of 20,000 is payable wholly before August, ordinary employee recovery is 1,600, employer cost 2,000 and pay after those employee deductions 18,400. That contribution scenario cannot be reused as a full calendar-year contribution schedule without the actual wage months. [LN 55 Schedule para. 1](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf); [Act 13 of 2014 ss. 2-3](https://www.parliament.gov.fj/wp-content/uploads/2017/03/ACT-No-13-FNPF-Budget-Amendment.pdf?ver=1794354122).

```oa-check
name: Fiji resident original 20000 with separate pre-August wage scenario
inputs:
  annual_chargeable: 20000
  covered_pre_august_wages: 20000
steps:
  - annual_income_tax: max(annual_chargeable - 30000, 0) * 0.18
  - employee_recovery: covered_pre_august_wages * 0.08
  - employer_own_cost: covered_pre_august_wages * 0.10
  - pay_after_tax_and_recovery: annual_chargeable - annual_income_tax - employee_recovery
expected:
  annual_income_tax: 0
  employee_recovery: 1600
  employer_own_cost: 2000
  pay_after_tax_and_recovery: 18400
```

### Case 2: resident annual gross 45,000, monthly pay

**Original input:** Resident, annual gross FJD 45,000. Monthly pay.

Assume stable primary normal pay of 3,750 each month, no bonuses/other income/benefits and matching actual history. At the first January period, D=3,750, E=0, F=12, G=1, H=0 and B1=0. C1 is 45,000, annual income tax 2,700 and first-period PAYE 225. On confirmed covered January wages the employee recovery is 300 and own employer contribution cost 375; net January pay is 3,225 and employer payroll cost 4,125. These employee/employer splits are not authorised for August by this calculation. [LN 56 reg. 3 and LN 55 Schedule](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf); [Act 13 of 2014](https://www.parliament.gov.fj/wp-content/uploads/2017/03/ACT-No-13-FNPF-Budget-Amendment.pdf?ver=1794354122).

```oa-check
name: Fiji resident primary January cumulative PAYE
inputs:
  D: 3750
  E: 0
  F: 12
  G: 1
  H: 0
  B1: 0
steps:
  - C1: D * (F - G + 1) + E
  - C2: C1 + H
  - T_C1: max(min(C1,50000)-30000,0) * 0.18 + max(C1-50000,0) * 0.20
  - T_C2: max(min(C2,50000)-30000,0) * 0.18 + max(C2-50000,0) * 0.20
  - PAYE: max(T_C1 / F * G - B1 + T_C2 - T_C1,0)
  - employee_recovery: D * 0.08
  - employer_own_cost: D * 0.10
  - net_pay: D - PAYE - employee_recovery
  - employer_payroll_cost: D + employer_own_cost
expected:
  C1: 45000
  T_C1: 2700
  PAYE: 225
  employee_recovery: 300
  employer_own_cost: 375
  net_pay: 3225
  employer_payroll_cost: 4125
```

### Case 3: resident annual gross 80,000

**Original input:** Resident, annual gross FJD 80,000.

Assume chargeable employment income equals that annual gross. Annual income tax is 3,600 + 20% × 30,000 = 9,600. No separate SRT or ECAL is added. A separately confirmed covered pre-August wage base of the same amount would yield employee recovery of 6,400 and employer cost 8,000; those are a deliberately stated pre-August scenario, not confirmed whole-year contributions from the raw annual input. Actual full-year net and cost need actual wage-month and recovery facts. [LN 55](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf); [Act 13 of 2014](https://www.parliament.gov.fj/wp-content/uploads/2017/03/ACT-No-13-FNPF-Budget-Amendment.pdf?ver=1794354122).

```oa-check
name: Fiji resident original annual 80000 tax function
inputs:
  annual_chargeable: 80000
steps:
  - lower_band_tax: 3600
  - upper_band_tax: (annual_chargeable - 50000) * 0.20
  - income_tax: lower_band_tax + upper_band_tax
expected:
  income_tax: 9600
```

### Case 4: resident annual chargeable income 320,000

**Original input:** Resident, annual chargeable income FJD 320,000.

Annual income tax is 57,500 + 34% × 20,000 = 64,300. The old separate tax/SRT/ECAL stack and resulting net figure were wrong. Chargeable income alone does not establish gross wages, FNPF covered wages or the months payable, so no final contribution, net pay or employer cost is calculated from this input. Do not silently set chargeable income equal to a contribution base. [LN 55 Schedule para. 1](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf).

```oa-check
name: Fiji resident original annual 320000 without obsolete levies
inputs:
  annual_chargeable: 320000
steps:
  - income_tax: 57500 + (annual_chargeable - 300000) * 0.34
expected:
  income_tax: 64300
```

### Case 5: non-resident annual gross 60,000

**Original input:** Non-resident, annual gross FJD 60,000. No resident tax-free threshold.

Assume the gross is chargeable employment income. Annual income tax is 12,000 under the non-resident table at this level, not a claim that all non-resident incomes are taxed at a flat rate. FNPF coverage was not supplied: do not subtract the old assumed employee contribution, present the old net pay as confirmed, or assume foreign citizenship from tax non-residence. Obtain membership/admission/exemption and wage-month facts first. [LN 55 Schedule para. 1](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf); [FNPF Act ss. 4, 36](https://www.rbf.gov.fj/wp-content/uploads/2020/03/Fiji-National-Provident-Fund-Decree-No.-52-of-2011.pdf).

```oa-check
name: Fiji nonresident original annual 60000
inputs:
  annual_chargeable: 60000
steps:
  - first_band: 30000 * 0.20
  - second_band: (50000 - 30000) * 0.20
  - third_band: (annual_chargeable - 50000) * 0.20
  - income_tax: first_band + second_band + third_band
expected:
  income_tax: 12000
```

### Case 6: hourly-pay input 5.00 × 40 × 52

**Original input:** Resident, FJD 5.00/hr × 40 hrs × 52 weeks = FJD 10,400/yr.

Annual pay from those supplied inputs is 10,400 and, assuming it is all chargeable employment income, annual income tax is zero. This does not certify the legal wage rate, sector, paid leave or overtime entitlement. For the additional scenario of a covered January week's wages of 200, the ordinary employee recovery is 16, own employer contribution cost 20 and net after tax/recovery 184. Do not apply that employer percentage blindly through August or treat a weekly illustration as the final monthly contribution schedule. [LN 55](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf); [Act 13 of 2014](https://www.parliament.gov.fj/wp-content/uploads/2017/03/ACT-No-13-FNPF-Budget-Amendment.pdf?ver=1794354122). The wage-announcement versus current-instrument boundary is in step 7.

```oa-check
name: Fiji original hourly input and January covered weekly scenario
inputs:
  hourly_pay: 5
  weekly_hours: 40
  weeks: 52
steps:
  - weekly_gross: hourly_pay * weekly_hours
  - annual_gross: weekly_gross * weeks
  - annual_income_tax: max(annual_gross-30000,0) * 0.18
  - january_employee_recovery: weekly_gross * 0.08
  - january_employer_own_cost: weekly_gross * 0.10
  - january_week_net: weekly_gross - january_employee_recovery
expected:
  annual_gross: 10400
  annual_income_tax: 0
  january_employee_recovery: 16
  january_employer_own_cost: 20
  january_week_net: 184
```

### Additional control: confirmed temporary total without inventing a split

On confirmed covered wages of 3,750 payable in August 2026, total FNPF is 600. This proves neither the disputed employee recovery nor the final employer-cost/net-pay split. The total uses the enacted nearest-cent rule. [Act 21 of 2026](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-21-Fiji-National-Provident-Fund-Budget-Amendment-Act-2026.pdf?ver=1794354122).

```oa-check
name: Fiji August statutory total only
inputs:
  covered_august_wages: 3750
steps:
  - total_contribution: round(covered_august_wages * 0.16,2)
expected:
  total_contribution: 600
```

### Retained regression controls

The six original annual-input cases remain above. The original additional controls are corrected as follows:

- Contribution composition: the ordinary pre-August total and recovery are reconciled separately from the enacted temporary total; no unsupported post-August employee/employer split is declared passed.
- Former high-earner levy boundary: at resident chargeable income 270,000 annual income tax is 47,600, and no separate current SRT/ECAL is added. A further marginal amount enters the next current income-tax band.
- Bracket continuity: resident annual tax at 50,000 is 3,600; at 270,000 is 47,600; at 300,000 is 57,500; at 1,000,000 is 318,500. The old last two tax totals were wrong. Test the adjacent band formulas, not a capped table plus historic levies. [LN 55 Schedule para. 1](https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf).

## When to refuse or refer

Preserve the original refusal IDs, with the legal corrections:

- **R-FJ-1: residence unknown.** Stop band selection; the resident nil band is not granted to a non-resident. Do not replace the missing fact with a flat rate on all non-resident income.
- **R-FJ-2: high-earner thresholds.** Refer an unresolved high-income/pay-package computation for review, but use the current integrated income-tax bands. The old SRT/ECAL stacking method is retired.
- **R-FJ-3: ECAL provenance.** Do not add historic ECAL to a current payroll. Separate an actual historic liability/arrears year from the 2026 withholding method and investigate it under its own law.
- **R-FJ-4: penalty figures.** The enacted FNPF balance-based penalty is confirmed; hold a disputed balance, month, waiver or FRCS penalty branch until its source and notice are read. Do not invent a penalty or represent an unconfirmed one as zero.
- **R-FJ-5: termination/final pay/redundancy.** These calculations remain outside the ordinary-pay method. Obtain the actual entitlements, tax rules and facts and refer the special computation.
- **R-FJ-6: fringe benefits/non-cash remuneration.** These valuations and employer fringe-benefits tax are separate work; do not guess from the net salary.

Also stop finalisation for unknown FNPF coverage/base, a disputed post-August recovery split, missing cumulative history/code, a special FRCS direction, voluntary-contribution authority, uncertain sector wages or unsupported corporate incentive. Keep exact amounts and alternative scenarios in the review brief.

The original prohibitions remain as corrected controls: no resident threshold for a non-resident; no obsolete income-tax cap; no current SRT/ECAL stacking; no invented contribution cap/floor; no automatic ordinary-wage definition; no omitted supported employer cost; no unconditional PAYE-final/no-return claim; no unsupported penalties; no wage compliance from an unverified sector rate; and no final payroll claim from a bank-only estimate. Calculations remain subject to review of the actual facts and return, not a new accountant-approval claim.

## Sources

These are actual scoped reads on the dates below, not statuses inferred from a successful download. The source texts contain historical versions; use operative amendments and the stated commencement dates. A current-year label does not certify unread wage instruments, benefit tables or a client's records. No person or approval is added.

| Source and actual scope read | Official URL | Read date |
|---|---|---|
| Read for Income Tax Act consolidation: ss. 2, 6 resident/tax-year definitions and part-year branches; employment/base and fund provisions ss. 15, 22-23; ss. 105, 111, 116-125; Withholding Regulations regs. 4-8, 10-13, 16-22 with neighbouring text; historical formula distinguished | https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf | 2026-11-16 |
| Read for Act 5 of 2023: complete amendment; commencement, deletion of SRT and ECAL income provision and old employment levy provisions | https://www.frcs.org.fj/wp-content/uploads/2023/07/Act-5-Income-Tax-Budget-Amendment.pdf | 2026-11-16 |
| Read for LN 55 and LN 56 of 2023: complete notices, both individual tables, company transition, current cumulative formula and deleted certificate/levy rules | https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf | 2026-11-16 |
| Read for LN 35-37 of 2025: complete Gazette bundle; confirms no individual-band replacement in LN 36, electronic-fiscal-device threshold and employment-incentive extensions distinguished from payroll rates | https://frcs.org.fj/wp-content/uploads/2025/08/EFD-Regs.pdf | 2026-11-16 |
| Read for FRCS new PAYE structure notice: resident/non-resident tables, new formula/template instructions excluding SRT/ECAL | https://frcs.org.fj/public-notice/customer-service-new-pay-as-you-earn-paye-structure/ | 2026-11-16 |
| Read for FNPF original Act: full s. 4 definitions/deeming/exemptions, ss. 34-40 and neighbours; old total/split/payment text not treated as current without amendments | https://www.rbf.gov.fj/wp-content/uploads/2020/03/Fiji-National-Provident-Fund-Decree-No.-52-of-2011.pdf | 2026-11-16 |
| Read for Decree 77 of 2012: commencement and full ss. 7-10, membership/readmission, payment-date change, deletion of old split subsection and voluntary direction procedure, with neighbours | https://myfnpf.com.fj/wp-content/uploads/2019/09/FNPF_AMENDMENT_DECREENo__77.pdf | 2026-11-16 |
| Read for FNPF Regulations 2014: definitions; regs. 3, 7-11, 17-19, 23-24 with neighbours, prescribed amounts/registration/records/directions and reporting evidence | https://myfnpf.com.fj/wp-content/uploads/2019/09/FNPF_Regulations_2014.pdf | 2026-11-16 |
| Read for Act 13 of 2014: complete enacted Act; ordinary total and employee-recovery fraction, commencement | https://www.parliament.gov.fj/wp-content/uploads/2017/03/ACT-No-13-FNPF-Budget-Amendment.pdf?ver=1794354122 | 2026-11-16 |
| Read for Act 13 of 2023: complete enacted Act; offshore provisions and deletion of temporary Division 3A from January 2024 | https://www.parliament.gov.fj/wp-content/uploads/2023/07/Act-13-Fiji-National-Provident-Fund-Budget-Amendment.pdf?ver=1794354122 | 2026-11-16 |
| Read for Act 11 of 2024: complete enacted Act; statement timing, late-payment penalty, membership and withdrawal amendments, separate commencement dates | https://frcs.org.fj/files/2024/08/Act-11-Fiji-National-Provident-Fund-Budget-Amendment-Act-2024.pdf | 2026-11-16 |
| Read for Act 23 of 2025: complete enacted Act and readmission wording/commencement | https://www.parliament.gov.fj/wp-content/uploads/2025/08/Act-23-Fiji-National-Provident-Fund-Amendment-Act-2025.pdf | 2026-11-16 |
| Read for Act 21 of 2026: complete enacted Act; temporary total-contribution override, nearest-cent rule and dates; no express amendment to recovery provision | https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-21-Fiji-National-Provident-Fund-Budget-Amendment-Act-2026.pdf?ver=1794354122 | 2026-11-16 |
| Read for FNPF current employers page: employee registration, temporary total and agency-stated split, approved-schedule/invoice/payment workflow and voluntary-incentive claim, with the legal limits above | https://myfnpf.com.fj/employers/ | 2026-11-16 |
| Read for Government 2024-2025 Budget address, National Minimum Wage section: announcement dates and national/sector examples, read through official web text; not the current enacted wage instrument | https://www.fiji.gov.fj/2024-2025-national-budget-address/ | 2026-11-16 |
| Read for Tax Administration Act 2026 amendment: ss. 1, 4 and neighbouring provisions; record sufficiency and commencement, not a payroll-penalty table | https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-13-Tax-Administration-Budget-Amendment-Act-2026.pdf?ver=1794354122 | 2026-11-16 |

Not yet confirmed: The operative post-August FNPF employee-recovery instrument resolving the agency split versus amended section 39; complete current membership/exemption amendments and any specific Board decision; a current 2026 wage/sector instrument; special benefit/final-pay valuations; FRCS taxpayer-specific electronic report fields/frequency and directions; exact applicable FRCS penalty/interest branches; additional employer-contribution tax incentive. These are held, not assumed absent or approved.

Version 0.2 corrects the capped tax bands, obsolete SRT/ECAL, simplistic annualisation and unqualified finality, remittance dates and whole-year contribution claims. All six original raw case inputs, six refusal IDs, supplier/payment patterns, workbook purposes, onboarding questions and extra regression topics remain, with unsupported derived net/cost amounts withheld or scoped to explicit facts. The single notice replaces repeated boilerplate.
