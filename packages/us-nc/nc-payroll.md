---
name: nc-payroll
description: Tier 2 North Carolina content skill for employer payroll compliance covering tax year 2025. Includes the 4.5% flat PIT phasing down toward 2.49% by 2030 contingent on revenue triggers, NC-4 state W-4, NC-5 monthly withholding voucher, NC-3 annual reconciliation, NC SUI wage base $32,600 with rates 0.06-5.76%, the absence of state-mandated paid leave or sick leave, and DHHS new-hire reporting within 20 days under PRWORA §453A.
jurisdiction: US-NC
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NC Payroll

## North Carolina Payroll Compliance Skill (Tax Year 2025)

## 1. Scope and Applicability

- **Scope** — This skill governs payroll tax compliance for employers operating in North Carolina (NC) for the 2025 tax year. It covers: North Carolina personal income tax (PIT) withholding under N.C. Gen. Stat. (NCGS) §105-163.1 through §105-163.24; Form NC-4 (Employee's Withholding Allowance Certificate) and NC-4EZ; Form NC-5 (Withholding Return) and NC-5P (Quarterly Withholding Payment Voucher) and NC-5Q (Quarterly Income Tax Withholding Return for semiweekly filers); Form NC-3 (Annual Withholding Reconciliation); NC State Unemployment Insurance (SUI) administered by the Division of Employment Security (DES) under NCGS Chapter 96; New-hire reporting to the NC Department of Health and Human Services (DHHS) under 42 U.S.C. §653A (PRWORA §453A) and NCGS §110-129.2; Worker classification under both the federal IRS 20-factor common-law test and NC-specific rules; Final pay timing under the NC Wage and Hour Act (NCGS Chapter 95, Article 2A).  _(NCGS §105-163.1 through §105-163.24)_

NOT in scope: Federal payroll (Form 941, FUTA, Form W-2 issuance to employees) — see federal payroll skill; Workers' compensation premium calculation; Local payroll taxes (NC has no county or municipal payroll/wage taxes); Multi-jurisdiction nexus analysis outside of the NC-specific apportionment rules in §6.

**Audience:** This skill is consumed by Claude when assisting a credentialed payroll specialist, CPA, or enrolled agent. All outputs must be reviewed by a human professional before filing.

## 2. North Carolina Personal Income Tax (PIT) Withholding

### 2.1 The 4.5% Flat Rate for 2025

- **2025 flat PIT rate** — 4.5% (flat on all taxable income, applies equally to wage withholding and supplemental wage rate)  _(NCGS §105-153.7(a), as amended by S.L. 2023-134 (the 2023 Appropriations Act) and S.L. 2024-1)_

**Effective dates of statutory rates**  _(S.L. 2023-134)_

| Tax Year | Statutory PIT Rate | Statutory Authority |
| --- | --- | --- |
| 2022 | 4.99% | NCGS §105-153.7 (pre-2022 amendment) |
| 2023 | 4.75% | S.L. 2021-180 |
| 2024 | 4.5% | S.L. 2021-180 |
| **2025** | **4.5%** | **S.L. 2023-134** |
| 2026 | 3.99% (scheduled) | S.L. 2023-134 |
| 2027 | 3.49% (contingent trigger) | S.L. 2023-134 §42.1(a) |
| 2028 | 2.99% (contingent trigger) | S.L. 2023-134 §42.1(a) |
| 2029 | 2.49% (contingent trigger) | S.L. 2023-134 §42.1(a) |
| 2030 | 2.49% (target floor if all triggers met) | S.L. 2023-134 |

### 2.2 AUDIT FLASH POINT: NC Phasing Rate Confusion Across 2025-2030

- **Contingent rate trigger mechanism** — The post-2026 rate reductions are NOT automatic. Under S.L. 2023-134 §42.1(a), the rate only drops from 3.99% to 3.49% (and lower) if General Fund net tax revenue for the prior fiscal year exceeds a statutory trigger amount.  _(S.L. 2023-134 §42.1(a))_

**Trigger amounts table**  _(S.L. 2023-134 §42.1(a))_

| Triggering FY | Trigger Amount | Rate That Applies If Triggered |
| --- | --- | --- |
| FY 2025-26 | $33.042 billion | 3.49% for TY 2027 |
| FY 2026-27 | $34.100 billion | 2.99% for TY 2028 |
| FY 2027-28 | $34.760 billion | 2.49% for TY 2029 |
| FY 2028-29 | $35.750 billion | 2.49% maintained for TY 2030 |

Common audit error: Payroll software vendors and small employers often pre-program rates assuming the triggers will be met. If a trigger is not met for a given fiscal year, the rate stays at the prior year's level and does not decrease further. When advising clients on 2026 and later withholding, always verify the actual statutory rate in effect via NCDOR Directive or Form NC-30 (Income Tax Withholding Tables and Instructions) for that tax year. Do not extrapolate.

For tax year 2025 only, the rate is firmly 4.5% and is not contingent.

### 2.3 Supplemental Wage Rate

- **Supplemental wage withholding rate 2025** — 4.5% (flat rate for bonuses, commissions, severance, equity vesting net of cover, retroactive pay; no aggregate method alternative)  _(NCDOR Form NC-30 (2025))_
- **Concurrent supplemental wages** — If supplemental wages are paid concurrently with regular wages and not separately identified, the combined amount is treated as a single regular wage payment subject to the standard withholding formula.  _(NCDOR Form NC-30 (2025))_

### 2.4 Standard Deduction in Withholding Tables

**NC standard deduction 2025**

| Filing Status | 2025 Standard Deduction |
| --- | --- |
| Single / Married Filing Separately | $12,750 |
| Head of Household | $19,125 |
| Married Filing Jointly / Qualifying Surviving Spouse | $25,500 |

- **Standard deduction indexing** — These amounts are reflected in the NC-30 percentage-method tables and the wage-bracket tables. The standard deduction is NOT indexed to inflation — it was set as a fixed-dollar amount by S.L. 2023-134.  _(S.L. 2023-134)_

### 2.5 No Personal Exemptions; Allowance Mechanism

- **Elimination of personal exemptions** — NC eliminated personal exemptions effective with the 2014 tax reform (S.L. 2013-316). For 2025, NC-4 still uses an "allowance" concept but those allowances now represent only: Estimated itemized deductions exceeding the standard deduction; Estimated tax credits (e.g., child credit); Adjustments for multiple jobs. There is no longer a one-allowance-per-dependent default. Employees who file NC-4 without completing the worksheet often over-withhold; advise clients accordingly.  _(S.L. 2013-316)_

## 3. Form NC-4: The Employee Withholding Certificate

### 3.1 Versions of NC-4

**Versions of NC-4 table**

| Form | Use Case |
| --- | --- |
| **NC-4** | Standard form. Full allowance worksheet for itemized deductions, credits, and multiple-job adjustments. |
| **NC-4EZ** | Simplified form. For employees claiming **zero allowances**, the standard deduction, and no additional credits or itemized deductions. Also used by **non-resident** workers who want flat withholding without an allowance computation. |
| **NC-4 NRA** | Nonresident alien employees. Mirrors the federal Form W-4 for NRAs and requires an additional withholding amount per pay period. |

### 3.2 When NC-4 Must Be Filed

- **NC-4 filing timing and default withholding** — An employee must file NC-4 (or NC-4EZ or NC-4 NRA, as applicable) on or before commencement of employment in NC. If no NC-4 is filed, the employer must withhold at single with zero allowances (the maximum withholding under NCGS §105-163.2(c)). An employee must file a new NC-4 within 10 days of any event reducing the number of allowances claimed (e.g., divorce, loss of dependent eligibility).  _(NCGS §105-163.2(c))_

### 3.3 Employer Submission of NC-4 to NCDOR

- **When NC-4 must be submitted to NCDOR** — Generally NC-4 is retained in the employer's payroll files and not submitted to NCDOR. However, the employer MUST submit the NC-4 to NCDOR if: The employee claims more than 10 allowances, OR The employee claims complete exemption from withholding AND earns more than $200 per week. Submissions go to NCDOR via written letter or electronic upload via the NCDOR e-Services Withholding Tax portal. NCDOR may issue a "lock-in" letter directing the employer to override the employee's NC-4.

### 3.4 NC-4EZ for Non-Resident Workers

- **Non-resident use of NC-4EZ and sourcing rule** — A NC employer with a non-resident employee (e.g., a remote worker who lives in Virginia but performs occasional in-NC work, or a Tennessee resident commuting to a NC worksite) may have the employee file NC-4EZ and check the non-resident box. This results in flat withholding on NC-sourced wages without any allowance reduction. Key non-resident rule: Wages are NC-sourced if the services are physically performed in NC. Residency of the employee is irrelevant for sourcing; only the location where the work is performed. See §6 below for multistate apportionment.  _(NCGS §105-153.3(13) and §105-163.1(13))_

## 4. Form NC-5 / NC-5P / NC-5Q: Withholding Returns and Payments

### 4.1 Filing Frequency Tiers

- **Filing frequency classification basis** — Under NCGS §105-163.6 and 17 NCAC 06C .0117, employers are classified into filing-frequency tiers based on average monthly withholding during a 12-month lookback period ending June 30.  _(NCGS §105-163.6 and 17 NCAC 06C .0117)_

**Filing frequency tiers table**  _(NCGS §105-163.6 and 17 NCAC 06C .0117)_

| Average Monthly Withholding | Filing Frequency | Form |
| --- | --- | --- |
| Less than $250 | **Quarterly** | NC-5 (filed quarterly) plus annual NC-3 |
| $250 to $1,999 | **Monthly** | NC-5 (filed monthly) plus annual NC-3 |
| $2,000 or more | **Semiweekly** | NC-5P (electronic payment per semiweekly schedule) plus quarterly NC-5Q plus annual NC-3 |

- **Annual reclassification and ratchet rule** — NCDOR reviews the classification each year and notifies employers of changes in writing. An employer that has been classified must continue at that frequency for the full calendar year regardless of mid-year payroll changes (one-way ratchet up, not down within year).

### 4.2 NC-5 Monthly Filers

- **NC-5 monthly due date** — Monthly filers must remit withholding tax and file Form NC-5 by the 15th day of the month following the month in which wages were paid. So January 2025 withholding is due February 15, 2025; March 2025 withholding is due April 15, 2025; and so on.
- **NC-5 report contents** — Form NC-5 reports: Total tax withheld for the period; Any prior period underpayment or overpayment; Penalty and interest for late filers.

### 4.3 NC-5P Semiweekly Schedule

- **Semiweekly deposit schedule** — Semiweekly depositors follow a schedule that mirrors the federal semiweekly deposit rules: Wages paid Wednesday, Thursday, Friday → deposit by following Wednesday; Wages paid Saturday, Sunday, Monday, Tuesday → deposit by following Friday. If the deposit is less than $500 in any one period, the deposit may be carried forward and combined with the next period's deposit; however, total liability for the quarter must still be reported on NC-5Q.

### 4.4 NC-5Q Quarterly Reconciliation (Semiweekly Filers Only)

- **NC-5Q due dates and reconciliation** — Semiweekly filers must file Form NC-5Q quarterly to reconcile total deposits made for the quarter with total withholding liability. NC-5Q is due: Q1: April 30; Q2: July 31; Q3: October 31; Q4: January 31. Underpayments are remitted with NC-5Q; overpayments are credited to the next quarter or refunded.

### 4.5 Quarterly Filers (Small Employers under $250/month)

- **Quarterly filer requirements** — Quarterly filers use Form NC-5 filed quarterly. Due dates align with NC-5Q (April 30, July 31, October 31, January 31). There is no separate NC-5P for quarterly filers — they simply file NC-5 by the quarterly due date and remit the tax with the return.

### 4.6 Electronic Filing Mandate

- **EFT mandate threshold** — Effective with payroll periods beginning after January 1, 2020 (per S.L. 2019-169 §3.5), an employer with average monthly withholding of $20,000 or more must remit by electronic funds transfer (EFT) through the NCDOR e-Services portal. Failure to remit electronically when required triggers a 5% penalty under NCGS §105-236(a)(1f). Most employers below the $20,000 threshold still file electronically because NCDOR strongly discourages paper filings.  _(S.L. 2019-169 §3.5; NCGS §105-236(a)(1f))_

### 4.7 Penalties and Interest

**Penalties and interest table**  _(NCGS §105-236)_

| Violation | Penalty | Authority |
| --- | --- | --- |
| Failure to file NC-5 / NC-5Q / NC-3 by due date | 5% per month, max 25% | NCGS §105-236(a)(3) |
| Failure to pay withheld tax by due date | 10% of unpaid tax | NCGS §105-236(a)(4) |
| Failure to remit by EFT when required | 5% of payment | NCGS §105-236(a)(1f) |
| Negligence or fraud | 25% to 50% | NCGS §105-236(a)(5)(b)–(c) |
| Underpayment interest | NCDOR-set rate, currently 8% APR (2025) | NCGS §105-241.21 |

- **Trust fund tax and responsible person liability** — Withholding tax is a trust fund tax under federal law (and effectively under NC practice). NC has a personal liability provision under NCGS §105-242.2 making responsible persons (corporate officers, certain employees with check-signing authority) personally liable for unremitted withholding. This survives bankruptcy and dissolution.  _(NCGS §105-242.2)_

## 5. Form NC-3: Annual Withholding Reconciliation

### 5.1 NC-3 Purpose and Due Date

- **NC-3 purpose and due date** — Form NC-3 (Annual Withholding Reconciliation) reconciles total NC withholding reported on NC-5 / NC-5P / NC-5Q during the year with the total NC withholding shown on Forms W-2, 1099-MISC, 1099-NEC, 1099-R, and NC-1099M issued to recipients. NC-3 is due by January 31 following the close of the calendar year. NC-3 for tax year 2025 is due January 31, 2026.

### 5.2 Electronic Filing Mandate for NC-3

- **Mandatory e-filing of NC-3 and information returns** — Under NCGS §105-163.7 (as amended by S.L. 2017-39), Form NC-3 and all associated W-2 and 1099 information returns must be filed electronically through the NCDOR e-Services portal. There is no paper option as of 2020. The $50-per-statement penalty under NCGS §105-236(a)(10) applies for each W-2 or 1099 not timely filed electronically.  _(NCGS §105-163.7 (as amended by S.L. 2017-39); NCGS §105-236(a)(10))_

### 5.3 Information Returns to Include with NC-3

- **Required information returns list** — W-2: for every employee with NC wages or NC withholding. W-2c: corrections issued during the year. 1099-NEC: for nonemployee compensation of $600 or more paid to a NC resident or for services performed in NC (NC sources). 1099-MISC: for rent, prizes, attorney fees, and other reportable payments. 1099-R: for retirement distributions with NC withholding. NC-1099M: NC-specific 1099 for compensation paid to a payee who claims an exemption from NC withholding (e.g., an ITIN holder providing W-9-equivalent attestation). NC-1099PS: NC-specific 1099 for non-wage compensation paid to nonresident contractors and ITIN holders subject to the 4% nonresident withholding requirement under NCGS §105-163.3.  _(NCGS §105-163.3)_

### 5.4 4% Nonresident Contractor Withholding

- **Nonresident contractor withholding rate** — 4% (applies when a NC-based payer pays a nonresident contractor or ITIN-holding contractor $1,500 or more in any calendar year for services performed in NC; remitted via NC-5/NC-5P; reported on NC-1099PS, not W-2)  _(NCGS §105-163.3)_

Common audit error: NC-based payers often miss this 4% withholding when paying out-of-state freelancers (e.g., a Charlotte SaaS company paying a Florida-resident design contractor for on-site work at the Charlotte office). The fact that the payee is a Form 1099-NEC contractor, not a W-2 employee, does NOT exempt the payment from NC-163.3 withholding.

## 6. AUDIT FLASH POINT: Multistate Employer Apportionment for NC Remote Workers

### 6.1 The Sourcing Rule

- **Physical presence sourcing rule** — NC follows a physical-presence-of-services sourcing rule under NCGS §105-153.4(c) for nonresidents and NCGS §105-130.4 for corporate-employer apportionment purposes. Wages are NC-sourced only to the extent services are physically performed within NC.  _(NCGS §105-153.4(c); NCGS §105-130.4)_

### 6.2 Common Multistate Scenarios

**Scenario A: NC-resident remote worker, out-of-state employer with no NC nexus.**
- The employer is not required to withhold NC tax because the employer has no NC payroll-tax nexus.
- The employee must make estimated NC payments on NC-40 or request additional NC withholding via NC-4.
- The employee's wages are 100% NC-taxable as NC-resident income, but no employer withholding occurs.

**Scenario B: NC-resident remote worker, employer with NC nexus.**
- Employer must withhold NC PIT on wages.
- If the employee occasionally travels to perform services in another state, that state's nonresident sourcing rule may apply. The "convenience of the employer" doctrine does NOT apply in NC (unlike NY, NE, PA, DE, AR).

**Scenario C: Non-NC resident, performs all services in NC.**
- Employer must withhold NC PIT on 100% of wages.
- Employee files Form D-400 as a nonresident at year-end and claims the resident-state credit.

**Scenario D: Non-NC resident, hybrid worker (3 days in NC, 2 days at home in VA).**
- Employer must apportion. Standard method: NC days / total work days for the pay period.
- If a hybrid worker works 60 days in NC and 100 total work days in the quarter, then 60% of the quarter's wages are NC-sourced.
- Document the day-count via a written reasonable methodology; NCDOR has accepted day-count, time-tracking-system reports, and Outlook calendar exports during audits.

**Scenario E: Traveling employee (sales rep, consultant) working in multiple states including NC.**
- Apportion by service-days-in-NC. Mileage, expense reports, and CRM check-ins are common evidence.
- If less than 30 service days per year and wages under the NC standard deduction prorated, NC withholding may be impractical; some employers obtain a written NCDOR authorization to waive.

### 6.3 Reciprocity

- **No reciprocity agreements** — NC has NO reciprocity agreements with any other state. Unlike Pennsylvania's reciprocity with NJ, DE, MD, OH, VA, IN, WV, NC does not waive withholding for residents of neighboring states (SC, VA, GA, TN) who perform services in NC. Always withhold NC tax on services physically performed in NC, regardless of the employee's resident state.

### 6.4 Documentation Best Practices

- **Documentation retention requirements** — Require all multistate employees to file an annual NC-4 declaring their estimated NC service days. Maintain timekeeping or location-tracking records sufficient to support apportionment. Retain records for at least 4 years from the latest filing date (NCGS §105-163.8 retention period; NCDOR audit lookback).  _(NCGS §105-163.8)_

## 7. NC State Unemployment Insurance (SUI)

### 7.1 Administering Agency

- **NC SUI administering agency** — NC SUI is administered by the Division of Employment Security (DES), a division of the NC Department of Commerce. Authority is NCGS Chapter 96 (Employment Security Law).  _(NCGS Chapter 96)_

### 7.2 Taxable Wage Base for 2025

- **2025 NC taxable wage base** — $32,600 USD per employee per calendar year

**Wage base history table**

| Year | NC SUI Wage Base |
| --- | --- |
| 2022 | $28,000 |
| 2023 | $29,600 |
| 2024 | $31,400 |
| **2025** | **$32,600** |
| 2026 | TBD (announced each November by DES) |

- **Wage base recalculation methodology** — The wage base is recalculated annually per NCGS §96-9.3 based on 50% of the average weekly wage in covered employment for the prior year. This is higher than the federal FUTA base of $7,000 (which has not changed since 1983) and meaningfully higher than many southeastern peers.  _(NCGS §96-9.3)_

Note: NC's wage base of $32,600 is significantly higher than SC ($14,000) and FL ($7,000), so multistate employers with NC operations should expect substantially higher per-employee NC SUI cost than FUTA cost alone would suggest.

### 7.3 Tax Rates for 2025

- **2025 experienced-rated employer contribution rate range** — 0.06% to 5.76% (of the first $32,600 in wages per employee)
- **New employer rate** — 1.0% (flat, first 2-3 years of NC operations)
- **Rate computation details** — Specific computations under NCGS §96-9.2(c): Each employer's rate is determined annually based on the employer's reserve ratio (cumulative contributions minus cumulative benefits charged, divided by average annual taxable payroll). The Trust Fund Solvency Surcharge under NCGS §96-9.7 is 0% for 2025 because the NC UI Trust Fund balance is well above the statutory solvency threshold (it was over $4 billion at the start of 2025). The annual rate notice (Form NCUI 104) is mailed in late November or December for the following year.  _(NCGS §96-9.2(c); NCGS §96-9.7)_

### 7.4 Workforce Investment Tax (Workforce Investment Surcharge)

- **Workforce investment allocation mechanism** — Under NCGS §96-9.4, 20% of an employer's regular SUI contribution is automatically diverted to the Workforce Investment Surcharge Account. This is NOT an additional tax on top of the SUI rate — it is a reallocation of a portion of the SUI contribution to fund workforce development.  _(NCGS §96-9.4)_
- **Workforce investment allocation example calculation** — For an employer paying the new-employer rate of 1.0% on $32,600 in wages = $326 per employee SUI contribution. Of that $326, 20% ($65.20) is allocated to workforce investment and 80% ($260.80) is credited to the employer's UI experience-rating reserve account. The employer's total cash outflow remains $326 per employee.  _(NCGS §96-9.4)_

Common audit error: Payroll software occasionally adds the workforce investment surcharge as a separate line item on top of the SUI rate, double-counting the tax. The correct treatment is a single SUI contribution at the rate on the NCUI 104 notice, with the 20% reallocation handled internally by DES.

### 7.5 SUI Reporting: NCUI 101

- **NCUI 101 filing due dates and content** — Form NCUI 101 (Employer's Quarterly Tax and Wage Report) is filed quarterly by all NC employers subject to NC SUI. Due dates: Q1: April 30; Q2: July 31; Q3: October 31; Q4: January 31. NCUI 101 reports: Total gross wages paid in the quarter; Excess wages (wages above the $32,600 base, not taxable for SUI); Taxable wages; Tax due (taxable wages × employer's NCUI 104 rate); Per-employee wage detail (name, SSN, gross wages). Electronic filing through DES's secure portal is mandatory for employers with 10 or more employees in any calendar quarter.

### 7.6 Coverage Threshold

- **NC SUI liability threshold** — An employer is liable for NC SUI under NCGS §96-1(b)(11) if it: Pays $1,500 or more in wages in any calendar quarter, OR Employs at least 1 person for some portion of a day in each of 20 different calendar weeks during the year. Once liable, the employer remains liable until DES grants termination, typically 2+ years of no NC employees.  _(NCGS §96-1(b)(11))_

### 7.7 SUTA Dumping

- **SUTA dumping enforcement** — NC enforces federal SUTA dumping rules under NCGS §96-9.2(g). Transferring payroll between commonly owned entities for the purpose of obtaining a lower SUI rate is a class 1 misdemeanor and triggers retroactive rate reassignment.  _(NCGS §96-9.2(g))_

## 8. Paid Family and Medical Leave: NOT Mandated in NC

- **No state-mandated PFML** — North Carolina does NOT have a state-mandated Paid Family and Medical Leave (PFML) program as of 2025. There is no payroll deduction, employer contribution, or program comparable to those in CA (CASDI/PFL), NY (PFL), NJ (FLI), MA, CT, WA, OR, CO, DE, MD, ME, or DC.

NC employers with employees in PFML states must: Withhold and remit the other state's PFML contribution if the work is performed in that state, OR For NC-resident employees temporarily working in a PFML state, apply that state's nexus rules (varies — CA generally exempts brief temporary work, MA looks at primary place of employment).

Voluntary benefits: A NC employer is free to offer paid family leave as a voluntary benefit. Many large NC employers (banks, tech firms, healthcare systems) do so. This is a private benefit and does not give rise to any NC payroll tax or filing obligation.

Federal FMLA still applies to NC employers with 50+ employees within 75 miles of a worksite. FMLA is unpaid and is a federal mandate, not a NC payroll tax.

## 9. Sick Leave: Not Mandated State-Wide

- **No statewide paid sick leave mandate** — NC has no state-wide paid sick leave mandate as of 2025. Unlike CA, NY, NJ, MA, OR, WA, CO, CT, RI, AZ, NM, MI, MN, IL, MD, NV, ME, VT, DC, and several others, NC has not enacted a paid-sick-leave statute.
- **Local preemption of sick leave ordinances** — Local preemption: NCGS §95-25.1A (added by S.L. 2017-4) preempts local governments from enacting paid-sick-leave or minimum-wage ordinances exceeding state law. Charlotte, Raleigh, Durham, Asheville, and other NC cities cannot legally impose a local paid-sick-leave requirement.  _(NCGS §95-25.1A (added by S.L. 2017-4))_

Implications for NC payroll: No accrual reporting on pay stubs; No state-mandated sick leave payout at termination (see §11); Federal FMLA, federal ADA, and federal Pregnant Workers Fairness Act still apply.

## 10. Worker Classification: IRS 20-Factor Plus NC-Specific Rules

### 10.1 The Federal Common-Law Test

- **IRS common-law 20-factor test categories** — NC follows the federal IRS common-law test under Rev. Rul. 87-41, organized into 20 factors grouped into three categories: 1. Behavioral control (instructions, training, evaluation systems); 2. Financial control (significant investment, opportunity for profit/loss, services available to the market, method of payment, expenses); 3. Type of relationship (written contracts, employee-type benefits, permanency, regular business activity). NC uses this test for income tax withholding determinations under NCGS §105-163.1(4)'s definition of "employee" by cross-reference to IRC §3401(c).  _(Rev. Rul. 87-41; NCGS §105-163.1(4); IRC §3401(c))_

### 10.2 NC SUI Test: ABC Test (Modified)

- **NC modified ABC test** — For NC SUI purposes under NCGS §96-1(b)(15), worker classification uses a modified ABC test: A worker is an employee for NC SUI unless ALL three of the following are met: A. The worker has been and will continue to be free from control or direction over the performance of the services. B. The service is either (i) outside the usual course of the business for which it is performed, OR (ii) performed outside all places of business of the enterprise for which it is performed. C. The worker is customarily engaged in an independently established trade, occupation, profession, or business.  _(NCGS §96-1(b)(15))_
- **NC ABC test stricter than federal** — NC's ABC test is meaningfully stricter than the federal common-law test. A worker can be a federal independent contractor but a NC SUI employee. This is most common where a NC employer engages a contractor who performs services in the usual course of the employer's business (e.g., a construction company engaging a "subcontractor" trim carpenter — likely an employee under NC ABC).

### 10.3 NC-Specific Industry Rules

- **Construction industry Employee Fair Classification Act** — Construction industry (NCGS §95-241 et seq.; "Employee Fair Classification Act," S.L. 2017-203): Effective December 31, 2017, NC's Employee Fair Classification Act established the Employee Classification Section within the NC Industrial Commission. It is empowered to: Investigate complaints of misclassification; Coordinate with NCDOR, DES, and NC DOL; Refer cases for civil penalties (up to $1,000 per misclassified employee per investigation); Bar misclassifying employers from state contracts for up to 5 years. Construction employers are the primary target. NC General Contractor licensees face license revocation risk for repeat misclassification.  _(NCGS §95-241 et seq.; S.L. 2017-203)_
- **Trucking/transportation classification** — Trucking/transportation: NC follows the federal "for-hire motor carrier" exception in certain limited cases, but only when the driver owns or leases the truck and bears operational expenses. Driver classification for NC SUI is fact-intensive and often litigated.
- **Real estate licensees exemption** — Real estate licensees: NCGS §96-1(b)(15)(d) provides a statutory exemption from SUI for real estate licensees who are paid by commission, work under a written contract, and would not be treated as employees for federal tax under IRC §3508(b). This mirrors the federal statutory non-employee category.  _(NCGS §96-1(b)(15)(d); IRC §3508(b))_
- **Direct sellers exemption** — Direct sellers: Mirrors the federal IRC §3508 exemption.  _(IRC §3508)_

### 10.4 Penalty for Misclassification

- **SUI misclassification audit consequences** — If a NC employer misclassifies an employee as a contractor and DES audits: Back SUI contributions for the lookback period (typically 4 quarters, can extend to 4 years for fraud); Penalty of up to 10% of unpaid contributions (NCGS §96-10(b)(2)); Interest at NCDOR rate (currently 8% APR); Personal liability for responsible officers under NCGS §96-10(g).  _(NCGS §96-10(b)(2); NCGS §96-10(g))_
- **PIT withholding misclassification liability** — For NCDOR PIT withholding misclassification, the employer is liable for the full amount of NC PIT that should have been withheld plus penalties under NCGS §105-236.  _(NCGS §105-236)_

### 10.5 Section 530 Federal Safe Harbor

- **Section 530 safe harbor does not extend to NC SUI** — If an employer has a reasonable basis under IRC §530 (Revenue Act of 1978) for treating a worker as a contractor for federal tax, that safe harbor applies for federal PIT withholding but does NOT extend to NC SUI. A federal Section 530 safe harbor does not bind DES; NC SUI ABC test is applied independently.  _(IRC §530 (Revenue Act of 1978))_

## 11. Final Pay and Wage Payment Rules

### 11.1 Final Pay Timing

- **Final pay timing rule** — Under the NC Wage and Hour Act, NCGS §95-25.7, an employer must pay all wages due to a separated employee by the next regular payday for the pay period in which the separation occurred. This applies whether the separation is voluntary (resignation), involuntary (termination, layoff), or by operation of law (death — pay to estate or to next of kin per the small-estates statute). No accelerated final pay requirement: NC, unlike CA (which requires immediate payment upon termination) and several others, does not require immediate payment. The next-regular-payday rule applies uniformly.  _(NCGS §95-25.7)_

### 11.2 Mailed Final Pay

- **Mailing final pay requirement** — If the separated employee requests payment by mail, the employer must mail the final pay by the regular payday. Holding the final paycheck for the employee to pick up in person is permissible only if the employee has not requested mailing.

### 11.3 Accrued PTO / Vacation Payout

- **PTO payout policy requirement** — Under NCGS §95-25.12, accrued vacation must be paid out at termination only if the employer's written policy or employment contract requires it. NC does not impose a default obligation to pay out PTO. If the employer's policy is silent, or expressly states "no payout at termination," there is no obligation.  _(NCGS §95-25.12)_

Practical compliance step: Maintain a written PTO policy in the employee handbook and have employees acknowledge receipt. Policies should clearly state whether unused vacation, sick leave, and floating holidays are paid out at termination.

### 11.4 Deductions from Final Pay

- **Permitted deductions from pay** — NCGS §95-25.8 limits deductions from any paycheck (including final pay) to: Deductions required by law (taxes, garnishments, child support); Deductions authorized in writing by the employee for the employee's benefit (401(k), health insurance, charitable contributions); Deductions for cash shortages, inventory shortages, or property damage only if authorized in writing AND only if employee has acknowledged liability and amount. Deducting from final pay for "unreturned company property" without a signed written authorization is a NC Wage and Hour Act violation. The proper remedy is a separate civil action, not a payroll deduction.  _(NCGS §95-25.8)_

### 11.5 Pay Stub Requirements

- **Pay stub itemization requirements** — Under NCGS §95-25.13, each paycheck must be accompanied by an itemized statement showing: Gross wages; Deductions; Net wages; Pay period dates. This may be furnished electronically with employee consent.  _(NCGS §95-25.13)_

## 12. New Hire Reporting to NC DHHS

### 12.1 Statutory Basis

- **New hire reporting statutory basis** — Federal PRWORA §453A (codified at 42 U.S.C. §653A) requires all states to maintain a new-hire directory. NC implements this through NCGS §110-129.2, requiring employers to report new hires to the NC New Hire Directory within 20 days of the date of hire. The NC Department of Health and Human Services (DHHS), Division of Child Support Services, administers the directory.  _(42 U.S.C. §653A (PRWORA §453A); NCGS §110-129.2)_

### 12.2 What to Report

- **Required new hire data elements** — For each newly hired or rehired employee: Employee's full name; Employee's address; Employee's Social Security Number; Date of hire (first day worked for pay); Employer's name; Employer's address; Employer's FEIN.

### 12.3 How to Report

- **New hire reporting channels** — NC New Hire Reporting Website: https://ncnewhires.com (electronic upload preferred). Mail: NC New Hire Directory, PO Box 90369, East Point, GA 30364-0369 (the directory is operated by a federal contractor). Fax: 1-866-257-7005. Multistate employers with employees in multiple states may elect to report all new hires to a single state under 42 U.S.C. §653A(b)(1)(B). The election must be filed with the federal Office of Child Support Enforcement (OCSE).  _(42 U.S.C. §653A(b)(1)(B))_

### 12.4 Rehires

- **Rehire reportability rule** — A rehire is reportable as a new hire if the employee has been separated for 60 consecutive days or more (federal standard adopted by NC). A rehire after a shorter break is not separately reportable.

### 12.5 Penalties

- **New hire reporting penalties** — Under NCGS §110-129.2(g): $25 per unreported new hire (first offense); $500 per unreported new hire if the failure is the result of a conspiracy between the employer and the employee (to avoid child support). In practice, NC DHHS rarely assesses these penalties on a first offense if the employer comes into compliance promptly.  _(NCGS §110-129.2(g))_

### 12.6 Independent Contractor Reporting (Optional)

- **Contractor reporting is optional** — NC does NOT mandate reporting of independent contractors to the New Hire Directory (unlike CA, which does). Employers may voluntarily report contractors and some choose to do so for child support enforcement cooperation, but it is not required.

## 13. Worked Examples

### 13.1 Example: Small NC Employer (5 employees, all in Raleigh)

**Facts:**
- "Triangle Bakery LLC" is a single-member LLC operating a small bakery in Raleigh.
- 5 W-2 employees: 1 manager, 2 bakers, 2 counter staff
- Total 2025 gross wages: $185,000
- Total 2025 NC withholding (estimated): $5,200
- Average monthly NC withholding: $5,200 / 12 = $433
- First year of operations: 2025
- All employees are NC residents working at the Raleigh location

**Filing classification:**
- Avg monthly withholding $433 → monthly filer (between $250 and $1,999)
- NC SUI: new employer rate of 1.0%

**Required filings table**

| Form | Frequency | Due Date | Annual |
| --- | --- | --- | --- |
| Federal Form 941 | Quarterly | Last day of month following quarter | — |
| NC-5 (state withholding) | Monthly | 15th of following month | — |
| NCUI 101 (SUI) | Quarterly | Last day of month following quarter | — |
| NC-3 + W-2s | Annual | January 31, 2026 | Yes |
| Federal Form 940 (FUTA) | Annual | January 31, 2026 | Yes |
| New hire reports (DHHS) | Within 20 days of each hire | — | — |

- **SUI calculation example** — Manager gross 2025 wages: $52,000. Wages above $32,600 base: $19,400 (excess; not SUI-taxable). Taxable wages: $32,600. NC SUI tax: $32,600 × 1.0% = $326. Of which workforce investment allocation: $326 × 20% = $65.20 (internal to DES; employer just remits $326 total). For all 5 employees, assuming all earn above $32,600 base: Total taxable SUI wages: $32,600 × 5 = $163,000. Total NC SUI for 2025: $163,000 × 1.0% = $1,630.
- **PIT withholding example calculation** — Biweekly gross: $2,000. Annualized: $52,000. 2025 standard deduction (single, NC-4 with zero allowances): $12,750. Annualized NC taxable wages: $52,000 − $12,750 = $39,250. Annual NC tax at 4.5%: $1,766.25. Per pay period (26 pay periods): $1,766.25 / 26 = $67.93 per pay period. (The NC-30 wage-bracket tables would produce a similar result, rounded to the nearest dollar.)

### 13.2 Example: Multistate Employer with NC Resident Remote Workers

**Facts:**
- "Cascade Software Inc." is a Washington-based S-corp with employees in WA, NC, VA, and TX.
- 2 NC-resident employees, both fully remote, working from home in Cary, NC and Asheville, NC
- One employee occasionally (3 days/quarter) travels to Cascade's Seattle HQ for company meetings
- Both NC employees earn $120,000/year
- Cascade has no physical office or property in NC, just the 2 remote employees

- **Nexus and withholding analysis** — **Does Cascade have NC payroll-tax nexus?** Yes. Having a NC-resident employee whose duties are performed in NC creates payroll-tax nexus under NCGS §105-163.1(13) (definition of "employer") regardless of the employer's lack of NC physical office. Cascade must register as a NC withholding agent and a NC SUI employer. **NC withholding:** - Both employees file NC-4 - Cascade withholds NC PIT at 4.5% effective rate on wages sourced to NC **Sourcing for the Cary employee:** 100% NC-sourced because all work is performed in NC. **Sourcing for the Asheville employee with 3 days/quarter in Seattle:** - Approximately 12 days/year in Seattle out of ~250 working days = 4.8% WA-sourced, 95.2% NC-sourced - NC withholding applies to 95.2% of wages - WA has no state income tax, so no WA withholding required (WA has Paid Family Medical Leave program; see WA payroll skill) - For practical administration, Cascade may either (a) withhold NC on 100% and let the employee claim a credit at year-end, or (b) reduce NC withholding proportionally with documented day-count records — both are acceptable to NCDOR if documented  _(NCGS §105-163.1(13))_
- **NC SUI and filing frequency calculation** — **NC SUI:** - Both employees are NC-resident remote workers performing services in NC - Cascade must register with DES, pay the 1.0% new-employer rate, on the first $32,600 of each employee's wages - NC SUI per employee: $32,600 × 1.0% = $326 - Total NC SUI: $652 - Plus quarterly NCUI 101 filings **Filing frequency:** - 2 employees × $120,000 × 4.5% / 95.2% NC-sourced for one ≈ $10,250 annual NC withholding - Avg monthly = $854 → monthly filer (NC-5) **Filings required:** - NC-5 monthly - NCUI 101 quarterly - NC-3 annual - New hire reports for both employees within 20 days of hire to NC DHHS (not to WA) **Multistate election for new-hire reporting:** Because Cascade has employees in multiple states, it may elect under 42 U.S.C. §653A(b)(1)(B) to report all new hires (including the WA, TX, VA employees) to NC DHHS. Whether this is administratively beneficial depends on Cascade's payroll vendor.  _(42 U.S.C. §653A(b)(1)(B))_

### 13.3 Example: Contractor Classification — NC Construction Subcontractor

**Facts:**
- "Mountain Homes Builders, Inc." is a NC general contractor based in Boone, NC, building custom homes.
- Mountain Homes engages "Joe Mason" to do all interior trim carpentry on its projects.
- Joe works exclusively for Mountain Homes for the past 18 months.
- Joe uses Mountain Homes-supplied materials but his own hand tools.
- Joe is paid by the job (flat fee per house) on Mountain Homes' standard 1099-NEC arrangement.
- Joe has no other clients, no business license, no website, no insurance under his own name.
- Joe sets his own daily hours but the job sites are dictated by Mountain Homes' project schedule.
- Mountain Homes treated Joe as a 1099 contractor in 2024 and reported $78,000 in payments on Form 1099-NEC.

**Federal IRS common-law analysis table**

| Factor | Indication |
| --- | --- |
| Behavioral control: Mountain Homes specifies which job sites and which homes | Employee |
| Behavioral control: Joe sets his daily hours within Mountain Homes' schedule | Mixed |
| Financial control: Joe has no significant investment beyond hand tools | Employee |
| Financial control: Joe has no opportunity for profit/loss beyond hourly efficiency | Employee |
| Financial control: Joe's services are not available to the market | Employee |
| Type of relationship: 18-month exclusive engagement | Employee |
| Type of relationship: No written contract characterizing as independent | Employee |
| Type of relationship: Trim carpentry is in the **usual course** of the GC business | Employee |

**Federal conclusion:** Joe is almost certainly an employee under the IRS common-law test. Mountain Homes has misclassification exposure for federal payroll taxes.

**NC SUI ABC test analysis:**

**A. Free from control or direction?** Mostly no — Mountain Homes specifies job sites and project schedules. Fails A.

**B. Outside usual course of business OR performed outside all places of business?** Trim carpentry is integral to building homes — the usual course of a GC's business. The work is performed AT Mountain Homes' job sites (its "places of business"). Fails B on both prongs.

**C. Customarily engaged in an independently established trade?** Joe has no other clients, no business license, no insurance under his name. Fails C.

**NC SUI conclusion:** Joe is unambiguously an employee under NC's ABC test.

- **Exposure calculation** — - Back SUI: 4 quarters × wages up to $32,600 × 1.0% new-employer rate (if Mountain Homes had not previously been classified as construction). If Mountain Homes already has an experience rating, the rate could be substantially higher. - $32,600 × 1.0% = $326 in back SUI per year for Joe alone. - 10% penalty: $32.60 - Interest at 8% APR - Back NC PIT withholding: 4.5% × $78,000 = $3,510 per year that should have been withheld - 10% penalty for failure to withhold: $351 - Interest at 8% APR - Back federal taxes: Mountain Homes is liable for the employer share of FICA (7.65%) on Joe's wages plus FUTA on the first $7,000. With reduced rates under IRC §3509, the employer FICA liability may be reduced if the 1099 was timely filed (which it was). Roughly $78,000 × 7.65% × 50% Section 3509 reduction ≈ $2,984 per year. - Employee Fair Classification Act exposure: Up to $1,000 per misclassified worker, plus potential debarment from state contracts for 5 years (severe consequence for a GC seeking state-funded projects). - Industrial Commission referral risk: The NC Industrial Commission may refer the case to NCDOR, DES, and NC DOL for coordinated enforcement.  _(IRC §3509)_

1. Reclassify Joe as a W-2 employee effective the next pay period.
2. Consult counsel about a voluntary disclosure to DES and NCDOR to limit penalties.
3. Consider participating in the IRS Voluntary Classification Settlement Program (VCSP) to limit federal back-tax exposure to 10% of one year's federal employment tax at reduced rates.
4. Review all other 1099 contractors on Mountain Homes' books for similar exposure — DES audits typically expand to cover all "contractors" on the payer's books.

## 14. Cross-References to Other Skills

- us-federal-return-assembly: Federal Form 941, Form 940 FUTA, and W-2 issuance
- us-1099-nec-issuance: Form 1099-NEC for nonemployee compensation; coordinates with NC-1099PS and NC-1099M for NC-source payments
- nc-income-tax: NC personal income tax for the employee or contractor's individual return (Form D-400)
- nc-corporate-tax: NC corporate franchise and income tax for the employer entity
- us-s-corp-election-decision: Reasonable salary analysis for S-corp shareholder-employees with NC payroll exposure
- us-sole-prop-bookkeeping: For NC sole proprietors hiring their first employee, the bookkeeping and Schedule C interactions

## 15. Reviewer Checklist

Before finalizing any NC payroll deliverable produced under this skill, the credentialed reviewer should verify:

- [ ] NC-4 (or NC-4EZ / NC-4 NRA) on file for every employee
- [ ] Filing frequency tier (quarterly / monthly / semiweekly) correctly determined from average monthly withholding
- [ ] NC-5 / NC-5P / NC-5Q deposits and returns timely filed
- [ ] NC SUI applied at correct 2025 rate (new-employer 1.0% or NCUI 104 experience rate)
- [ ] NC SUI wage base correctly capped at $32,600 per employee per year
- [ ] NCUI 101 quarterly filing complete with per-employee wage detail
- [ ] NC-3 reconciliation submitted by January 31 following the tax year, electronically
- [ ] All W-2s and applicable 1099s submitted electronically with NC-3
- [ ] 4% nonresident contractor withholding under NCGS §105-163.3 applied where applicable
- [ ] Multistate sourcing apportionment documented for hybrid/remote workers
- [ ] New-hire reports submitted to NC DHHS within 20 days of each hire/rehire (60-day rule for rehires)
- [ ] Worker-classification analysis under both federal common-law and NC ABC test for any 1099 engagement
- [ ] Final pay timing (next regular payday) and PTO payout (per written policy) compliant with NCGS §95-25.7 and §95-25.12
- [ ] All deductions from pay supported by written authorization under NCGS §95-25.8
- [ ] Pay stub itemization compliant with NCGS §95-25.13
- [ ] For 2026 and later, confirm actual NC PIT rate via NCDOR Form NC-30 — do NOT assume the scheduled phase-down has occurred without statutory confirmation of revenue triggers

## 16. Key Authorities and Citations

**Statutes:**
- NCGS Chapter 105, Subchapter V (Income Tax Withholding): §§105-163.1 to 105-163.24
- NCGS §105-153.7 (PIT rate; rate schedule under S.L. 2023-134)
- NCGS Chapter 96 (Employment Security Law): §§96-1 to 96-22
- NCGS §96-9.2 (Contribution rates)
- NCGS §96-9.3 (Wage base)
- NCGS §96-9.4 (Workforce investment allocation)
- NCGS Chapter 95, Article 2A (Wage and Hour Act): §§95-25.1 to 95-25.25
- NCGS §110-129.2 (New hire reporting)
- NCGS §95-241 et seq. (Employee Fair Classification Act, S.L. 2017-203)

**Session laws (recent):**
- S.L. 2023-134 (2023 Appropriations Act) — PIT rate phasedown
- S.L. 2024-1 — technical conforming amendments
- S.L. 2017-203 — Employee Fair Classification Act
- S.L. 2019-169 §3.5 — EFT mandate threshold
- S.L. 2017-4 — local preemption of minimum wage / paid sick leave
- S.L. 2017-39 — electronic filing of NC-3

**Administrative authorities:**
- NCDOR Form NC-30, Income Tax Withholding Tables and Instructions, 2025 Edition
- NCDOR Directive PD-23-1 (post-2023 rate phase-down implementation)
- 17 NCAC 06C (Withholding rules)
- DES Form NCUI 104 (Annual rate notice)
- DES Form NCUI 101 (Quarterly tax and wage report)

**Federal:**
- 42 U.S.C. §653A (PRWORA new hire reporting)
- IRC §3401(c) (definition of employee)
- IRC §3508 (statutory non-employees)
- IRC §3509 (reduced employment tax for misclassification)
- IRS Rev. Rul. 87-41 (20-factor common-law test)
- Section 530 of the Revenue Act of 1978 (federal safe harbor)

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
