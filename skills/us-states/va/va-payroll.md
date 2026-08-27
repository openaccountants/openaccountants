---
name: va-payroll
description: Tier 2 Virginia content skill for employer payroll compliance covering tax year 2025. Includes the VA PIT brackets up to 5.75%, VA-4 state W-4, VA-15 quarterly and VA-5 monthly withholding returns, VA-16 wage report annual reconciliation, VA SUI wage base $8,000 (among lowest in US) with rates 0.10-6.20%, reciprocal agreements with DC/KY/MD/PA/WV exempting non-resident employees, workers' compensation mandatory for 3+ employees, and the absence of state-level paid sick leave (with city-level mandates in Alexandria).
jurisdiction: US-VA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# VA Payroll

## 1. Scope

This skill covers Virginia-specific employer payroll compliance for tax year 2025. It is a **Tier 2 content skill** that MUST be loaded alongside `us-tax-workflow-base v0.2` or later, plus the federal payroll workflow skill (federal income tax withholding, FICA, FUTA, Forms 941/940/W-2/W-3).

**In scope:**
- Virginia personal income tax (VA PIT) withholding from wages paid to Virginia residents and non-residents performing services in Virginia
- VA-4 (Employee's Virginia Income Tax Withholding Exemption Certificate)
- VA-5 (Monthly) and VA-15 (Quarterly) withholding returns — and the Semi-Weekly accelerated regime
- VA-6 / VA-16 annual reconciliation and wage report
- Virginia State Unemployment Insurance (SUI) administered by the Virginia Employment Commission (VEC)
- Reciprocal agreements with DC, KY, MD, PA, WV
- Worker classification (federal common-law test plus Virginia Construction Industry Misclassification statute)
- Workers' compensation triggering threshold (3+ employees)
- Paid sick leave (state-level absence and Alexandria municipal mandate)
- Domestic worker treatment
- Final pay timing under Virginia Code §40.1-29
- Federal contractor multistate wage allocation

**Out of scope (refer-out):**
- Virginia corporate income tax — see `va-corporate-tax-and-bpol`
- BPOL (Business, Professional and Occupational License tax) — see `va-corporate-tax-and-bpol`
- Sales and use tax — see `va-sales-tax`
- Virginia individual income tax return (Form 760) — see `va-income-tax`
- Federal income tax withholding mechanics (Form W-4, IRS Pub 15-T) — defer to federal skill
- Federal unemployment (FUTA Form 940) — defer to federal skill
- Multi-state nexus determination beyond reciprocal-state mechanics

**Assumed reviewer:** Every output of this skill is assumed to be reviewed and signed off by a credentialed practitioner — a Virginia-licensed CPA, Enrolled Agent, or attorney admitted in Virginia — before any return is filed with the Virginia Department of Taxation or the Virginia Employment Commission. The skill produces a reviewer-oriented work product, not a self-filing return.

## 2. Virginia Personal Income Tax — Withholding Brackets

Virginia imposes a graduated personal income tax with four brackets. The brackets have not been indexed for inflation in many years and remain at the statutory levels set in Va. Code §58.1-320.

### 2.1 2025 Virginia PIT brackets (single, married filing jointly, married filing separately — Virginia does NOT have separate bracket schedules; the same brackets apply to all filing statuses)

**2025 Virginia PIT brackets**  _(Va. Code §58.1-320)_

| Taxable income (annual) | Marginal rate | Tax on bracket |
| --- | --- | --- |
| $0 – $3,000 | 2.00% | up to $60 |
| $3,001 – $5,000 | 3.00% | $60 + 3% over $3,000 |
| $5,001 – $17,000 | 5.00% | $120 + 5% over $5,000 |
| Over $17,000 | 5.75% | $720 + 5.75% over $17,000 |

The top marginal rate of **5.75%** kicks in at just $17,000 of Virginia taxable income — one of the lowest top-bracket thresholds in the country. In practice this means almost every full-time employee in Virginia hits the 5.75% bracket on incremental wages.

### 2.2 Standard deduction and personal exemption (2025)

- **Married filing separately** — $8,500
- **Married filing jointly** — $17,000
- **Personal exemption — each dependent** — $930
- **Age 65+ or blind additional exemption** — $800 USD  _(2.2 Standard deduction and personal exemption (2025))_

These reduce taxable wages for withholding-table purposes and feed the VA-4 allowance computation.

### 2.3 Supplemental withholding rate

- **Supplemental withholding rate** — 5.75% (flat rate for bonuses, commissions, other supplemental wage payments)  _(Va. Dept. of Taxation Pub. VA-15A withholding tables, §2.3)_
- **Practical convention for bonuses** — For bonuses processed in a separate payroll run, withhold a flat 5.75% on the bonus amount in addition to whatever the regular wage withholding produces. For bonuses aggregated with regular wages on a single check, run the combined amount through the regular wage-bracket method.  _(Va. Dept. of Taxation Pub. VA-15A withholding tables, §2.3)_

### 2.4 Computing Virginia withholding from gross wages

- **Standard withholding computation method** — Step 1: Convert wage payment to annualized basis (multiply by pay periods per year) Step 2: Subtract VA-4 personal exemption allowance × $930 Step 3: Subtract standard deduction (annualized: $8,500 single / $17,000 MFJ — but VA-4 line for additional standard deduction is rare in practice; default is $8,500 unless the employee claims MFJ via VA-4 line 3) Step 4: Apply graduated bracket table from §2.1 to remaining amount Step 5: Divide annualized tax by pay periods per year = withholding per pay period Step 6: Add any additional flat dollar amount the employee elected on VA-4 line 4  _(Va. Dept. of Taxation Withholding Tables, percentage method)_

**Worked example (employee earns $80,000 annually, semi-monthly, single, 1 exemption, no additional withholding):**
- Annualized wages: $80,000
- Less personal exemption: $80,000 − $930 = $79,070
- Less standard deduction (single): $79,070 − $8,500 = $70,570 Virginia taxable wages
- Tax: $720 + 5.75% × ($70,570 − $17,000) = $720 + $3,080.28 = **$3,800.28/year**
- Per semi-monthly pay period (24 periods): **$158.35**

### 3.1 What it is

- **Form VA-4** — Form VA-4 is Virginia's state W-4. Every employee subject to Virginia withholding must complete a VA-4 at hire and whenever exemption status changes. There is no federal-cross-walk; Virginia does NOT accept the federal Form W-4 as a substitute.  _(Va. Dept. of Taxation Reg. §23 VAC 10-140-281)_

### 3.2 Key VA-4 fields

- **Line 1(a)** – Number of personal exemptions (typically 1 for self; +1 for spouse if MFJ and spouse has no income; +1 per dependent)
- **Line 1(b)** – Additional age 65+ / blind exemptions
- **Line 2** – Subtotal exemptions
- **Line 3** – Additional standard deduction box if MFJ (signals withholding table to use $17,000 SD instead of $8,500)
- **Line 4** – Additional flat dollar amount to withhold per pay period
- **Line 5** – Exempt status (employee certifies (i) no Virginia tax liability prior year AND (ii) anticipates none in current year) — must be re-filed by Feb 15 each year, parallel to the federal exempt re-certification deadline

### 3.3 Reciprocal-state exemption: Form VA-4 vs Form VA-4-NR vs Form VA-4 with reciprocal certification

- **Reciprocal-state exemption filing** — If an employee is a resident of DC, KY, MD, PA, or WV who commutes into Virginia to work and is exempt under the reciprocal agreement (see §7), the employee files Form VA-4 with line 5 "exempt" and writes their state of residency in the certification box — OR the employer may use Form VA-4 with the reciprocal-state certification block completed. Some practitioners use Form VA-4-NR (Non-Resident); both are accepted. Without a properly-completed reciprocal certification, the employer MUST withhold Virginia tax from the non-resident commuter's wages. This is AUDIT FLASH POINT #1 below.  _(3.3 Reciprocal-state exemption: Form VA-4 vs Form VA-4-NR vs Form VA-4 with reciprocal certification)_

### 3.4 Retention

- **VA-4 retention period** — Employers retain VA-4s for four years after the last date the form was in effect, parallel to federal W-4 retention. They are not filed with the Department; they are produced on audit request.  _(3.4 Retention)_

### 3.5 New-hire reporting

- **New-hire reporting deadline** — 20 days days (of hire, to the Virginia New Hire Reporting Center)  _(Va. Code §63.2-1946)_

## 4. VA-5 (Monthly) and VA-15 (Quarterly) Withholding Returns

Virginia assigns employers to a withholding-deposit frequency based on average monthly Virginia withholding liability, redetermined annually each November for the following calendar year:

### 4.1 Frequency tiers

**Frequency tiers**  _(4.1 Frequency tiers)_

| Frequency | Threshold (avg monthly VA withholding) | Return form | Deposit due date |
| --- | --- | --- | --- |
| **Quarterly** | Less than $100/month | **VA-15** (quarterly) | Last day of month following quarter |
| **Monthly** | $100 – $999.99/month | **VA-5** (monthly) | 25th of month following |
| **Semi-Weekly** | $1,000+/month | VA-15 (return) + EFT deposits | Wed/Fri depending on payday (parallel to federal Pub. 15) |

> Note: Virginia's nomenclature inverts the federal pattern — VA-15 is the **quarterly OR semi-weekly summary return**, while VA-5 is the **monthly return**. Do not confuse VA-15 with the IRS Form 945 or Form 941; the numbering similarity is coincidental.

### 4.2 VA-5 (Monthly) mechanics

- **VA-5 monthly mechanics** — - Filed for any month in which the employer was assigned monthly status - Due by the 25th of the following month (e.g., January VA-5 due February 25) - Reports total Virginia tax withheld for the month - No wage-detail data — that flows to VA-6/VA-16 annual reconciliation - Filed electronically via iReg / Business iFile at www.tax.virginia.gov — paper filing is permitted only with prior waiver - Payment via ACH debit, ACH credit, or eForms credit card (with convenience fee)  _(4.2 VA-5 (Monthly) mechanics)_

### 4.3 VA-15 (Quarterly) mechanics

- **VA-15 quarterly due dates** — - Filed quarterly by employers under the $100/month threshold - Quarterly return due: - Q1 (Jan–Mar): April 30 - Q2 (Apr–Jun): July 31 - Q3 (Jul–Sep): October 31 - Q4 (Oct–Dec): January 31 (of following year) - Same electronic filing channel as VA-5  _(4.3 VA-15 (Quarterly) mechanics)_

### 4.4 Semi-weekly deposit regime

- **Semi-weekly deposit schedule** — Employers with avg monthly Virginia withholding ≥ $1,000 must deposit on the federal semi-weekly schedule: - Wages paid Wed/Thu/Fri → deposit due following Wednesday - Wages paid Sat/Sun/Mon/Tue → deposit due following Friday Semi-weekly depositors still file VA-15 at quarter end as a summary return, with separate Schedule VA-15-W listing each semi-weekly deposit. This is a frequent point of confusion — semi-weekly depositors are NOT exempt from filing a quarterly return; they file VA-15 with the deposit detail.  _(4.4 Semi-weekly deposit regime)_

### 4.5 Penalties and interest

- **Late filing penalty** — 6% per month or fraction (max 30%) of tax due on the return  _(Va. Code §58.1-635(A))_
- **Late payment penalty** — same 6%/month penalty stacks with late-filing penalty if both apply  _(Va. Code §58.1-635(A))_
- **Underpayment (semi-weekly) penalty** — separate 6% penalty on each underdeposited installment  _(4.5 Penalties and interest)_
- **Interest rate** — 8% annualized for most of 2025 (federal underpayment rate, accruing from the original due date)  _(4.5 Penalties and interest)_
- **Negligence penalty** — 25% (where evidence of intent)  _(Va. Code §58.1-308)_
- **Fraud penalty** — 100% (plus criminal exposure)  _(4.5 Penalties and interest)_

### 4.6 Zero returns

- **Zero return requirement** — A monthly or quarterly employer with NO Virginia withholding liability for the period must still file a "zero" VA-5 or VA-15. Failure to file a zero return triggers the $25/quarter administrative penalty plus the 6%/month penalty on $0 (which evaluates to the $25 minimum).  _(4.6 Zero returns)_

### 5.1 Form VA-6 (Annual Withholding Reconciliation)

- **VA-6 annual reconciliation contents and due date** — VA-6 is the annual reconciliation form. It is filed by all Virginia withholding employers and reports: - Total Virginia wages paid during the year - Total Virginia tax withheld - Total deposits/payments made during the year (sum of VA-5s or VA-15s) - Difference (balance due or refund) - Count of W-2 statements being transmitted Due date: January 31 of the following year.  _(5.1 Form VA-6 (Annual Withholding Reconciliation))_

### 5.2 Form VA-16 (Employer's Annual Wage Report)

- **VA-16 wage-detail transmittal** — VA-16 is the wage-detail transmittal — Virginia's equivalent of the federal Form W-3 / W-2 transmittal, but filed with the Department of Taxation rather than the SSA. It is the magnetic-media/electronic vehicle that carries the employee-level W-2 wage data to Virginia. - Due: January 31 with the VA-6 - Filed electronically (paper VA-16 is no longer accepted for employers with 10+ W-2s; the de facto rule is that virtually all employers e-file) - Format: EFW2 format (same as SSA), with Virginia-specific RS records carrying the state wage and tax data - Filed via Web Upload at www.tax.virginia.gov  _(5.2 Form VA-16 (Employer's Annual Wage Report))_

> AUDIT FLASH POINT #3 — VA-16 vs federal W-3: Filing only the federal W-3 with the SSA does NOT satisfy VA-16. Virginia obtains W-2 data from the Department of Taxation submission, not from SSA. Practitioners who assume "the SSA forwards it" find that Virginia's matching program flags the employer for non-filing of VA-16 and assesses penalties even where the federal W-3 was timely filed. Always confirm a Virginia Web Upload confirmation number for VA-16.

### 5.3 Penalties for VA-6/VA-16 default

- **VA-6/VA-16 default penalties** — - Late filing: $30/W-2 (up to $1,500/year) - Failure to file: $200 administrative penalty + the $30/W-2 stacking - Discrepancy between VA-5/VA-15 deposits and VA-6 totals: triggers correspondence audit and the 6%/month penalty on any unpaid balance  _(5.3 Penalties for VA-6/VA-16 default)_

### 5.4 Corrected returns

- **Corrected returns process** — Use Form VA-6-W (Amended Annual Reconciliation) for corrections to the VA-6. For wage-detail corrections, refile the corrected EFW2 file via Web Upload with the "amended" indicator. Always file the federal W-2c with SSA first, then Virginia, to keep the reconciliation in sync.  _(5.4 Corrected returns)_

### 6.1 Administering agency

- **VEC administration** — Virginia Employment Commission (VEC), separate from the Department of Taxation. Registration on the VEC website (www.vec.virginia.gov) yields a 10-digit VEC account number, distinct from the Department of Taxation's 15-digit withholding account number.  _(6.1 Administering agency)_

### 6.2 Coverage threshold

- **SUI coverage attachment** — Paid $1,500 or more in wages in a calendar quarter OR Employed one or more workers for any portion of a day in 20 or more different weeks in a calendar year  _(Va. Code §60.2-210)_

These mirror FUTA coverage tests, so any FUTA-liable employer is also VA SUI-liable.

### 6.3 Wage base

- **Virginia SUI wage base** — $8,000 USD per employee per calendar year (2025)  _(6.3 Wage base)_

This is among the lowest SUI wage bases in the country (only Mississippi, Tennessee, Louisiana, Arizona, and California cluster near this level). The wage base has not been increased since 2009. This is important for the cost picture — Virginia SUI tax tops out at roughly $496/employee/year ($8,000 × 6.20% max rate).

### 6.4 Rate range and new-employer rate

- **Experience-rated employer rate range** — 0.10% to 6.20% (2025 rate schedule, including the 0.10% pool charge and the 0.20% Fund Building rate where applicable)  _(6.4 Rate range and new-employer rate)_
- **New employer rate** — 2.50% (standard new-employer rate, first three computation periods)  _(Va. Code §60.2-516)_
- **Construction industry new-employer rate** — typically 6.20% (separate higher new-employer rate reflecting higher historical claims experience)  _(6.4 Rate range and new-employer rate)_

### 6.5 Quarterly reporting — Form VEC FC-20 / FC-21

- **FC-20 and FC-21 reporting** — - FC-20 — Quarterly Tax Report (totals: gross wages, taxable wages, tax due, contribution rate) - FC-21 — Quarterly Payroll Report (employee-by-employee SSN, name, gross wages) Both filed together quarterly: - Q1: due April 30 - Q2: due July 31 - Q3: due October 31 - Q4: due January 31 of following year Filed via the VEC Business iFile portal. Employers with 100+ employees must e-file (in practice, virtually all employers e-file).  _(6.5 Quarterly reporting — Form VEC FC-20 / FC-21)_

### 6.6 SUI penalties

- **SUI penalty schedule** — - Late filing FC-20: $100 minimum OR $30 plus 10% of tax due, whichever is greater - Late payment FC-20: 1.5%/month interest plus penalty stacking - Failure to file FC-21 (payroll report): independent $25/quarter penalty plus impairs the employer's experience rating computation - Misclassification (worker reported as 1099 when in fact employee under VEC's audit): back contributions + interest + 25% penalty + civil penalty up to $5,000 per misclassified worker under the Construction Industry Misclassification Act  _(6.6 SUI penalties)_

### 6.7 SUTA dumping

- **SUTA Dumping Prevention** — Virginia adopted the federal SUTA Dumping Prevention Act provisions. Acquiring an employer's experience rating through a sham transaction triggers reassignment to the highest rate plus penalties.  _(Va. Code §60.2-536.1)_

### 7.1 The reciprocal-state rule

- **Reciprocal jurisdictions** — Virginia has reciprocal income-tax agreements with five jurisdictions: DC (District of Columbia), KY (Kentucky), MD (Maryland), PA (Pennsylvania), WV (West Virginia). Under each agreement, a resident of one of these jurisdictions who works in Virginia is exempt from Virginia withholding — and conversely, a Virginia resident who works in any of these five jurisdictions is exempt from that jurisdiction's withholding. The employee pays income tax only to the state of residence.  _(7.1 The reciprocal-state rule)_

### 7.2 Operational mechanics

- **Reciprocal operational steps** — For an out-of-state resident commuting into Virginia: 1. Employee completes Form VA-4 marking "exempt" and indicating state of residency in the reciprocal certification block (or files Form VA-4-NR) 2. Employer stops withholding Virginia tax — withholds only the resident state's tax instead 3. Employer must register as a withholding employer in the employee's resident state (e.g., a Virginia employer with a Maryland-resident employee must register with Maryland Comptroller and withhold Maryland tax) 4. The Virginia VA-6/VA-16 will report zero Virginia wages for that employee 5. The resident state's W-2 box 15/16/17 reports the wages and withholding for the resident state For a Virginia resident commuting into a reciprocal state: 1. Employee files the foreign state's equivalent form (e.g., MW 507 for Maryland, IT-4NR for Kentucky) with the foreign employer claiming reciprocal exemption 2. Foreign employer withholds Virginia tax instead, registering with Virginia Department of Taxation 3. Virginia resident files VA Form 760 reporting wages and claiming Virginia withholding  _(7.2 Operational mechanics)_

### 7.3 Key edge cases

- **Reciprocity covers wages only** — Self-employment income, gambling winnings, lottery winnings, rental income, partnership income, and S-corporation income earned in Virginia by a non-resident are NOT covered by reciprocity. The non-resident must still file Form 763 (VA non-resident return).  _(7.3 Key edge cases)_
- **Local jurisdiction tax not covered** — Reciprocity covers state income tax. Some reciprocal jurisdictions (notably Kentucky and Pennsylvania) have local occupational license taxes that are NOT covered. A Virginia resident working in Louisville, KY still owes Louisville occupational tax even though they don't owe Kentucky state tax.  _(7.3 Key edge cases)_
- **DC no non-resident income tax** — DC technically cannot impose income tax on non-residents of DC under the federal Home Rule Act. So a Virginia resident working in DC owes Virginia tax (which the DC employer must withhold via Virginia withholding registration), and a DC resident working in Virginia owes DC tax via Virginia employer registration with DC. The "reciprocal" framing exists administratively to harmonize this.  _(D.C. Code §47-1806.04)_
- **MD reciprocal mechanics** — Maryland imposes a county tax in addition to state tax. A Maryland resident working in Virginia owes Maryland state + county tax via the Virginia employer's Maryland withholding registration. The Virginia employer must apply the correct county-of-residence tax rate for each MD-resident employee, not a single state rate.  _(7.3 Key edge cases)_

### 7.4 Failure to apply reciprocity correctly — AUDIT FLASH POINT

> AUDIT FLASH POINT #1 — Missed reciprocal-state employee classifications. This is the single most common Virginia payroll audit finding for employers in Northern Virginia (Arlington, Alexandria, Fairfax County). Symptoms:
>
> - Virginia withholding being applied to a Maryland or DC resident commuter
> - VA-4 on file with no reciprocal certification, often because employee unaware
> - Employer has not registered as a withholding agent in the employee's resident state
>
> Consequences: the affected employee files VA Form 763 (non-resident) claiming a refund of all Virginia withholding (Department of Taxation must refund), while simultaneously owing unpaid resident-state tax with penalties. The employer faces resident-state penalties for failure to register and withhold, plus potential class-action exposure for incorrectly withholding from multiple employees.
>
> Required correction:
> 1. Confirm each non-Virginia-resident employee's resident state from VA-4, I-9, and HR records
> 2. Where the employee is a resident of DC/KY/MD/PA/WV: collect a properly-completed VA-4 with reciprocal certification (line 5 exempt + residency state)
> 3. Register with the resident state's withholding authority
> 4. Stop VA withholding prospectively
> 5. For prior-year errors: issue corrected W-2 (W-2c) reducing Virginia wages and Virginia withholding to zero, increasing resident-state wages and withholding
> 6. File Form VA-6-W amended reconciliation
> 7. Coordinate with the employee on filing VA-763 refund claim

### 8.1 Federal common-law test

- **Federal common-law test adoption** — Virginia adopts the federal IRS common-law employee test (right-to-control, financial control, type-of-relationship) for income tax withholding purposes. Workers who would be employees under IRS Form SS-8 analysis are employees for VA-4/VA-5/VA-15 purposes.  _(8.1 Federal common-law test)_

### 8.2 VEC-specific test for unemployment

- **ABC test for SUI purposes** — For SUI purposes, VEC applies the ABC test — the worker is an employee for VEC purposes UNLESS the hiring entity proves all three of: - (A) The worker is free from control or direction - (B) The service is outside the usual course of the hiring entity's business - (C) The worker is customarily engaged in an independently established trade The ABC test is stricter than the federal common-law test. A worker may be a legitimate 1099 contractor for federal income tax purposes but an employee for VEC purposes. Classification mismatches are common.  _(Va. Code §60.2-212)_

### 8.3 Virginia Construction Industry Misclassification

- **Statutory presumption of employee status** — Va. Code §40.1-28.7:7 (effective July 1, 2020, amended 2024) creates a statutory presumption of employee status for any individual providing services to a construction-industry employer. The employer rebuts the presumption only by satisfying a multi-factor list including: - Written contract specifying independent contractor status - The worker has their own business license, EIN, and insurance - The worker advertises services to the general public - The worker has the right to hire and fire helpers - The worker furnishes their own tools costing $1,000+  _(Va. Code §40.1-28.7:7)_
- **Penalties for misclassification in construction** — - 1st offense: civil penalty up to $1,000 per misclassified worker - 2nd offense: civil penalty up to $5,000 per worker - 3rd+ offense: civil penalty up to $10,000 per worker + debarment from public contracts for up to one year - Plus back SUI contributions, back withholding, back workers' comp premiums, all with interest This statute is administered by the Department of Labor and Industry (DOLI) jointly with VEC and the Department of Taxation. Cross-referral between agencies is automatic once any one agency opens a misclassification case.  _(Va. Code §40.1-28.7:7)_

### 8.4 General-business misclassification

- **General industry misclassification penalty** — Va. Code §58.1-1900 (added 2020) applies parallel penalties to misclassification in any industry, though without the rebuttable presumption of construction. Civil penalty up to $1,000/worker first offense.  _(Va. Code §58.1-1900)_

### 9.1 Mandatory coverage threshold

- **Workers' compensation insurance mandatory threshold** — 3 or more employees  _(O.C.G.A. §34-9-1 et seq.)_
- **3-employee count inclusions** — The 3-employee count includes: - Working owners and officers (unless the officer formally opts out via Form 61A) - Part-time and temporary workers - Family-member employees (with limited exception for sole-proprietor spouse/minor children)  _(Va. Code §65.2-101 et seq.)_

### 9.2 Construction industry — lower threshold

- **Construction industry WC threshold** — 1 or more subcontractors  _(Va. Code §65.2-302)_

### 9.3 Coverage mechanism

- **WC coverage options** — - Commercial workers' comp insurance policy from an admitted Virginia carrier, OR - Approval as a self-insured employer by the Virginia Workers' Compensation Commission (high bar — typically $20M+ net worth requirement)  _(9.3 Coverage mechanism)_

### 9.4 Penalties for non-coverage

- **Non-coverage penalties** — - Civil penalty up to $250/day of non-coverage - Stop-work order — Commission may shut down the business until coverage is in place - Personal liability of owners/officers for the full value of any work-related injury during the uncovered period - Loss of access to Virginia courts as a defense to tort claims  _(Va. Code §65.2-805)_

### 9.5 Domestic worker exception

- **Domestic servant WC exclusion** — Va. Code §65.2-101 excludes "domestic servants" employed in a private home from mandatory coverage UNLESS the employer voluntarily elects coverage. See §11 for domestic worker treatment generally.  _(Va. Code §65.2-101)_

### 10.1 No state mandate

- **No statewide paid sick leave law** — Virginia has no statewide paid sick leave law as of 2025. Multiple legislative attempts (most recently HB 1389 in the 2023 session) have failed.  _(10.1 No state mandate)_

### 10.2 Limited paid-leave provisions in state law

- **Home health workers paid sick leave** — up to 40 hours/year (for home health workers employed by Medicaid waiver providers)  _(Va. Code §40.1-33.6)_

State employees: separate civil service rules under DHRM Policy 4.55.

### 10.3 Municipal mandates

- **City of Alexandria PSL mandate** — employers with 5+ employees to provide up to 40 hours/year of paid sick leave (accrued at 1 hour per 30 hours worked) (effective for hours worked within Alexandria city limits)  _(Alexandria City Code §11-12-1 et seq.)_

The City of Arlington has considered but not enacted a local mandate.

For an employer with workers physically performing services in Alexandria, the city ordinance applies regardless of where the employer is headquartered.

### 10.4 Federal contractor PSL

- **Federal contractor PSL under E.O. 13706** — Federal contractors with covered contracts remain subject to Executive Order 13706 (paid sick leave for federal contractors — 7 days/year accrued). This is independent of Virginia state law and applies in Virginia to contracts within E.O. 13706's scope.  _(Executive Order 13706)_

### 11.1 Federal threshold

- **Household employer federal thresholds** — $2,800 or more in cash wages in 2025 (FICA threshold) to any single domestic worker, OR $1,000+ in any calendar quarter (FUTA threshold) to all domestic workers combined  _(11.1 Federal threshold)_

### 11.2 Virginia withholding for domestic workers

- **VA withholding for domestic workers** — Virginia treats household employers under the same withholding framework as other employers. If a domestic worker requests Virginia withholding by filing a VA-4, the employer must register for a withholding account and remit quarterly. Many household employers handle Virginia tax instead through the worker's own estimated payments (Form 760ES), with the worker electing not to file VA-4 — this is acceptable if the worker is otherwise current on estimated payments.  _(11.2 Virginia withholding for domestic workers)_

### 11.3 VEC coverage for domestic workers

- **VEC coverage for domestic workers** — VEC coverage attaches at the federal Schedule H threshold ($1,000+/quarter). The household becomes a VEC-registered employer and files FC-20/FC-21 quarterly. This is often overlooked — many household employers handling federal Schedule H fail to register with VEC.  _(11.3 VEC coverage for domestic workers)_

### 11.4 Domestic workers and workers' comp

- **Domestic workers WC exclusion** — Domestic workers are excluded from the Workers' Compensation Act UNLESS the employer voluntarily elects coverage. Many household insurance riders effectively provide voluntary coverage; verify policy language.  _(Va. Code §65.2-101)_

### 11.5 Virginia Domestic Workers' Bill of Rights

- **Domestic Workers' Bill of Rights protections** — Va. Code §40.1-28.7:9 (effective July 1, 2021) extends to domestic workers: - Minimum wage protections (full Virginia minimum wage, currently $12.41/hour for 2025) - Overtime protections at 1.5× regular rate for 40+ hours/week (live-out workers; live-in workers have separate rules) - Anti-discrimination protections This is a labor-law overlay, not a tax statute, but it affects gross-wage computation for VA-4/VA-5/VA-15 purposes.  _(Va. Code §40.1-28.7:9)_

## 12. Final Pay

- **Final pay timing requirement** — Virginia Code §40.1-29 requires final wages to be paid: - By the next regular payday after termination (whether voluntary or involuntary) - In the usual manner the employee was paid There is no separate Virginia statute requiring same-day or next-day payment of final wages (contrast with California). Accrued unused vacation/PTO is paid out only if the employer's policy or contract so provides — Virginia has no statutory PTO-payout mandate. Practical implication for payroll skill output: when computing final-period withholding for a terminated employee, use the regular wage-bracket method; do NOT use the supplemental rate unless the final check includes severance, vacation cash-out, or bonus components.  _(Va. Code §40.1-29)_

## 13. BPOL — Refer-Out

- **BPOL out of scope** — The Business, Professional and Occupational License tax (BPOL) is a locality-level gross-receipts tax imposed by Virginia cities, counties, and towns. While BPOL is sometimes confused with payroll (because some localities historically used a payroll-based proxy), it is a gross-receipts tax on the business itself, not a payroll tax. BPOL is out of scope for this skill. Refer all BPOL questions to `va-corporate-tax-and-bpol` for: - BPOL rate schedules by locality - Gross-receipts apportionment - Wholesaler vs retailer vs service vs financial-services classifications - Filing thresholds and due dates  _(Va. Code §58.1-3700 et seq.)_

### 14.1 Example A — VA-resident DC commuter (reciprocal)

**Facts:**
- Employer: Smith Federal Contracting LLC, headquartered in Arlington, VA
- Employee: Sarah Hernandez, resident of Reston, VA (Fairfax County)
- Sarah commutes to DC daily and performs all services in the District
- Annual salary: $95,000, paid bi-weekly (26 periods)
- Sarah is single, claims 1 personal exemption

**Analysis:**
- Sarah is a Virginia resident performing services in DC
- Under the VA-DC reciprocal arrangement, DC does not impose income tax on non-residents of DC
- Sarah owes Virginia income tax on the full $95,000
- The employer must register as a Virginia withholding employer (already done since HQ is in Virginia) and withhold Virginia tax even though the work is performed in DC
- DC withholding: NONE (DC cannot tax non-residents)
- Federal withholding: per Form W-4

**Virginia withholding computation:**
- Annualized wages: $95,000
- Less personal exemption (1 × $930): $94,070
- Less standard deduction ($8,500): $85,570 VA taxable
- Tax: $720 + 5.75% × ($85,570 − $17,000) = $720 + $3,942.78 = $4,662.78/year
- Per bi-weekly pay (26 periods): **$179.34**

**W-2 reporting:**
- Box 15: VA, with Virginia employer account number
- Box 16: $95,000 (Virginia state wages)
- Box 17: $4,662.78 (Virginia state income tax)
- DC fields: blank (no DC tax)

**Notes:**
- No VEC SUI complexity in this example since Sarah's services in DC are "localized" in DC for SUI purposes BUT the employer-employee relationship is administered out of Virginia. Under Va. Code §60.2-212 the localization-of-services test would actually push SUI coverage to DC for this employee. In practice, federal contractors with field staff working in DC commonly register with both VEC and DC's Department of Employment Services and report the wages to whichever jurisdiction's coverage analysis applies. This is the kind of multistate allocation that flows into example C.
- Sarah files VA Form 760 reporting all wages and claiming the $4,662.78 withholding credit.

### 14.2 Example B — VA federal contractor with Maryland-resident employee

**Facts:**
- Employer: Patriot Defense Systems Inc., HQ in McLean, VA
- Employee: Marcus Johnson, resident of Bethesda, MD (Montgomery County)
- Marcus performs all services in Virginia at the McLean office
- Annual salary: $140,000, paid semi-monthly (24 periods)

**Analysis:**
- Marcus is a Maryland resident performing services in Virginia
- Under the VA-MD reciprocal agreement, Marcus is exempt from Virginia withholding
- The employer must:
  1. Collect a VA-4 from Marcus with the reciprocal certification block completed (residency state: MD)
  2. Register with the Maryland Comptroller as an out-of-state withholding employer (Form CRA — Combined Registration Application)
  3. Withhold Maryland state tax PLUS Montgomery County local tax (Maryland uses a county-of-residence local tax that varies by county)
  4. Remit Maryland withholding quarterly via Maryland's bFile system
  5. Issue W-2 reporting MD wages and MD withholding only — Virginia boxes 15/16/17 are BLANK
  6. File MD Form MW-508 annual reconciliation (Maryland's equivalent of VA-6) by January 31

**Maryland withholding rates applicable for 2025 (Montgomery County resident):**
- State: graduated 2% to 5.75% (Maryland's top bracket starts at $250,000 single)
- Montgomery County local: 3.20% flat (2025 Montgomery County rate)
- Combined effective rate at $140,000 income ≈ 7.95% — significantly higher than the Virginia 5.75% rate

**Virginia treatment:**
- No Virginia withholding
- VA-6/VA-16 reports $0 Virginia wages for Marcus
- VEC SUI coverage: Marcus performs services in Virginia, so VEC coverage applies. Wages are reported on FC-20/FC-21 up to the $8,000 wage base (Virginia SUI is independent of the income-tax reciprocal agreement)
- Workers' comp: Virginia coverage applies (Marcus works in Virginia)

**AUDIT FLASH POINT illustration:**
If Patriot Defense had failed to collect the reciprocal-certified VA-4 and continued withholding Virginia tax from Marcus's wages, the consequences:
- Marcus would file VA Form 763 (non-resident return) claiming refund of ~$8,050 (5.75% × ~$140K Virginia tax incorrectly withheld)
- Marcus would owe Maryland approximately $11,130 in unpaid tax + interest + penalty
- Patriot Defense would face Maryland Comptroller penalties for failure to register and withhold (~10% of unpaid tax + interest)
- Patriot Defense would NOT face a Virginia penalty (over-withholding is not a Virginia violation) but would face administrative burden of issuing W-2c and amending VA-6

### 14.3 Example C — Multistate employer with VA residents working across multiple jurisdictions

**Facts:**
- Employer: Acme Federal Services LLC, headquartered in Arlington, VA, with a federal prime contract under GSA Schedule
- Employee: David Park, Virginia resident living in Falls Church
- David's services in 2025:
  - 60% of work time at the Arlington office (Virginia)
  - 25% on-site at a federal facility in Bethesda, MD
  - 10% on-site at a federal facility in Washington, DC
  - 5% on-site at a federal facility in Richmond, VA
- Annual salary: $175,000, paid bi-weekly

**Analysis — wage allocation:**
The employer must allocate David's wages by physical location of services because (i) David's resident state is Virginia, (ii) some non-resident states might assert tax jurisdiction, and (iii) reciprocal agreements may eliminate some non-resident tax exposure.

**Per-jurisdiction analysis:**

**Per-jurisdiction wage allocation table**  _(14.3 Example C — Multistate employer with VA residents working across multiple jurisdictions)_

| Jurisdiction | % of services | Wages allocated | Resident-state reciprocity covers? | Withholding required? |
| --- | --- | --- | --- | --- |
| Virginia (Arlington + Richmond) | 65% | $113,750 | N/A — Virginia is resident state | VA withholding YES |
| Maryland (Bethesda) | 25% | $43,750 | Yes — VA-MD reciprocal applies; David exempt from MD | VA withholding (continues since David is VA resident); NO MD withholding |
| DC (Washington) | 10% | $17,500 | Yes — DC cannot tax non-residents under Home Rule Act | VA withholding (continues); NO DC withholding |

**Total Virginia wages for W-2 Box 16: $175,000** (all wages flow to Virginia because David is a Virginia resident AND each non-resident jurisdiction is either reciprocal or unable to tax non-residents).

**Virginia withholding computation (David single, 1 exemption):**
- Annualized: $175,000
- Less exemption: $174,070
- Less SD: $165,570
- Tax: $720 + 5.75% × ($165,570 − $17,000) = $720 + $8,542.78 = $9,262.78/year
- Per bi-weekly (26 periods): **$356.26**

**VEC SUI allocation — AUDIT FLASH POINT:**

> AUDIT FLASH POINT #2 — Federal contractor multistate wage allocation for SUI. Under the multistate "localization of services" framework in Va. Code §60.2-212 (which mirrors federal UCFE rules), VEC coverage for a single employee is generally determined by:
>
> 1. Localization test: services in one state only OR incidental services elsewhere → coverage in that one state
> 2. Base of operations: if services in multiple states, coverage where employee's base of operations is located
> 3. Place of direction or control: if no base of operations, where the employer's direction comes from
> 4. Residence: if none of the above, employee's state of residence
>
> Applied to David:
> - Services in 4 locations across 3 states — fails localization
> - David's base of operations: Arlington, VA (the office where he reports for assignments and stores his work materials) — coverage attaches in Virginia
> - David's full wages report on VA FC-20/FC-21 (up to the $8,000 wage base)
> - The employer should NOT report any wages to Maryland UI or DC ESA for David
>
> The audit flashpoint: federal contractors often inadvertently report David's Bethesda-site wages to Maryland UI because the Maryland federal facility provides a worksite. This produces double-reporting (both Maryland UI and Virginia VEC), creates a Maryland UI account that triggers Maryland audit notices, and produces a reciprocal disagreement that VEC and Maryland will eventually resolve in Virginia's favor — but only after fact-finding and penalty exposure for inconsistent state reporting.
>
> Required practice: confirm and document the employee's base-of-operations location for every employee working at federal facilities outside their resident state. Report all SUI wages to the base-of-operations state.

**Workers' compensation:**
- Virginia workers' comp coverage applies because David's base of operations is Virginia
- The employer should confirm with its WC carrier that the policy covers Maryland and DC work-sites under the "extraterritorial" endorsement — most Virginia WC policies include this for incidental out-of-state work, but a 35% non-Virginia work pattern may trigger the carrier's threshold for requiring a multistate endorsement

**Federal contractor PSL (Executive Order 13706):**
- David's contract is GSA Schedule (federal) — covered by E.O. 13706
- Employer must accrue 1 hour PSL per 30 hours worked, up to 56 hours/year (7 days)
- This is independent of Virginia state law (no state mandate) and Alexandria municipal law (not applicable since David works in Arlington, not Alexandria)

## 15. Skill Self-Check Checklist

Before producing a reviewer-facing Virginia payroll work product, confirm:

- [ ] Each non-Virginia-resident employee has a properly-completed VA-4 (with reciprocal certification where applicable)
- [ ] For reciprocal-state employees: employer is registered as a withholding agent in the employee's resident state
- [ ] VA-5 / VA-15 frequency assignment matches the current Department of Taxation determination letter (re-verify each November)
- [ ] Semi-weekly depositors have a separate file of Schedule VA-15-W deposit detail
- [ ] VA-6 reconciles to the sum of VA-5/VA-15 deposits within $1
- [ ] VA-16 wage report Web Upload confirmation number is on file
- [ ] FC-20 quarterly wages reconcile to W-2 Box 16 Virginia wages within the $8,000 wage-base cap
- [ ] FC-21 employee detail matches W-2 employee-level data
- [ ] Workers' comp policy is in force and the employee count has not crossed the 3-employee threshold without coverage
- [ ] Construction-industry employer: each 1099 worker has a documented Va. Code §40.1-28.7:7 rebuttal file
- [ ] Federal contractor multistate worker: base-of-operations is documented and SUI is reported only to the base-of-operations state
- [ ] Alexandria-worksite employees: PSL accrual tracked
- [ ] Final-pay-period workers: payment scheduled for next regular payday

## 16. Citations and Authority

**Statutes:**
- Va. Code §58.1-320 — graduated income tax rates
- Va. Code §58.1-460 et seq. — employer withholding
- Va. Code §58.1-635 — late filing/payment penalties
- Va. Code §60.2-210 — SUI coverage
- Va. Code §60.2-212 — multistate services / ABC test
- Va. Code §60.2-516 — new-employer rate
- Va. Code §40.1-29 — final pay
- Va. Code §40.1-28.7:7 — construction industry misclassification
- Va. Code §40.1-28.7:9 — domestic workers
- Va. Code §65.2-101 et seq. — workers' compensation
- Va. Code §63.2-1946 — new hire reporting

**Regulations:**
- 23 VAC 10-140 — withholding regulations
- 16 VAC 5-32 — VEC regulations

**Department publications:**
- Virginia Withholding Tax Guide (Pub. VA-15A, 2025 edition)
- VEC Employer Handbook (2025)
- Virginia Department of Taxation Tax Bulletin 25-1 (2025 rate notice)

**Federal cross-reference:**
- IRC §3401 et seq. — federal withholding
- IRC §3306 — FUTA
- IRS Pub 15 / Pub 15-T — federal withholding tables
- Executive Order 13706 — federal contractor PSL

**Reciprocal agreement references:**
- DC: D.C. Code §47-1806.04 (Home Rule Act non-resident tax bar)
- KY: KRS §141.070
- MD: Md. Tax-Gen §10-806
- PA: 72 Pa. Cons. Stat. §7359
- WV: W. Va. Code §11-21-71b

## 17. Refusal Catalogue (Virginia-specific additions to base R-US refusals)

- **R-VA-1** — Will not produce a Virginia payroll return without confirmation that the federal payroll skill has produced the federal withholding figures the Virginia return relies upon for reconciliation.  _(17. Refusal Catalogue (Virginia-specific additions to base R-US refusals))_
- **R-VA-2** — Will not compute Virginia withholding for an employee whose VA-4 is missing or stale (>4 years without re-execution by an employee claiming exempt). The reviewer must collect a current VA-4.  _(17. Refusal Catalogue (Virginia-specific additions to base R-US refusals))_
- **R-VA-3** — Will not classify a construction-industry worker as a 1099 independent contractor without a documented Va. Code §40.1-28.7:7 multi-factor rebuttal file. Default classification is employee.  _(17. Refusal Catalogue (Virginia-specific additions to base R-US refusals))_
- **R-VA-4** — Will not allocate multistate wages for SUI without a documented base-of-operations determination.  _(17. Refusal Catalogue (Virginia-specific additions to base R-US refusals))_
- **R-VA-5** — Will not produce a Virginia payroll work product for a household domestic employer paying below the federal Schedule H threshold ($2,800 FICA / $1,000-quarter FUTA) unless the household has voluntarily elected coverage — refer the user to the federal Schedule H skill.  _(17. Refusal Catalogue (Virginia-specific additions to base R-US refusals))_
- **R-VA-6** — Will not provide BPOL guidance — refer-out to `va-corporate-tax-and-bpol`.  _(17. Refusal Catalogue (Virginia-specific additions to base R-US refusals))_
- **R-VA-7** — Will not produce a Virginia individual income tax return (Form 760) — refer-out to `va-income-tax`.  _(17. Refusal Catalogue (Virginia-specific additions to base R-US refusals))_

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
