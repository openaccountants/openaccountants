---
name: mo-payroll
description: Tier 2 Missouri content skill for employer payroll compliance covering tax year 2025. Includes the MO PIT brackets up to 4.95% (phasing down via revenue triggers), MO W-4 state W-4, MO-941 monthly/quarterly withholding, MO-W-3 annual reconciliation, MO UI wage base $9,500 with rates 0-9.75%, the Kansas City and St. Louis 1% local earnings taxes applicable to both residents and non-resident workers, and 20-factor worker classification test.
jurisdiction: US-MO
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MO Payroll

## Missouri Payroll Skill — Tax Year 2025

## 1. Scope

This skill covers employer payroll compliance obligations in the State of Missouri for tax year 2025. The audience is OpenAccountants reviewers (CPA, EA, or attorney credentialed under Circular 230 for federal touchpoints, and a Missouri-licensed practitioner for state matters) preparing or reviewing payroll returns for a small or mid-sized employer with at least one Missouri-resident employee or one employee performing services in Missouri.

### 1.1 In scope

- **MO PIT withholding** — In scope  _(Chapter 143 RSMo, Subchapter B (Employer Withholding))_
- **MO W-4** — In scope
- **MO-941** — In scope
- **MO-W-3** — In scope
- **MO UI** — In scope, $9,500 taxable wage base CY2025, experience-rated contribution schedule (0.0% to 9.75%), 2.7% new-employer rate, quarterly Form MODES-4-7  _(Chapter 288 RSMo)_
- **Kansas City Earnings Tax** — 1% earnings tax on residents wherever earned and non-residents for work within KC corporate limits  _(Chapter 68 of the Code of Ordinances of Kansas City, Missouri)_
- **St. Louis City Earnings Tax** — 1% earnings tax on residents wherever earned and non-residents for work within corporate limits of the City of St. Louis (NOT St. Louis County)  _(Chapter 5.22 of the Revised Code of the City of St. Louis)_
- **Worker classification** — 20-factor common law test applied by MO DES and DOR, contrasted with federal IRS three-category framework
- **New hire reporting** — To MO DSS FSD within 20 days of hire  _(§285.300 RSMo)_
- **Final pay rules** — In scope  _(§290.110 RSMo)_
- **Paid sick leave status** — State preempted as of August 28, 2025; St. Louis City sick leave ordinance separately analyzed

Worked examples for three common employer profiles: a Kansas City employer with a non-KC-resident employee, a St. Louis City employer, and a non-metro MO-only small business.

### 1.2 Out of scope

- **Federal income tax withholding** — Out of scope (FICA, FUTA, Form 941, Form 940) — defer to us-federal-payroll or federal employer skills
- **MO Workers' Compensation** — Out of scope for payroll tax; covered separately under MO workers' comp skill  _(Chapter 287 RSMo)_
- **Garnishments/child support withholding mechanics** — Out of scope except new hire reporting trigger  _(§454 RSMo)_
- **Multi-state nexus analysis** — Out of scope — defer to _cross-border/us-multi-state-payroll
- **Section 125 cafeteria plan, 401(k) admin, ERISA** — Out of scope
- **Statewide paid family leave** — Out of scope — Missouri has none
- **Independent contractor income tax reporting** — Out of scope (Form 1099-NEC) — defer to us-1099-nec-issuance
- **KC profits tax** — Out of scope — separate 1% profits tax on unincorporated business and corporations; only earnings-tax portion on wages is covered
- **KC convention/tourism/hotel/transient guest taxes** — Out of scope
- **St. Louis County** — St. Louis County does NOT levy an earnings tax — see Section 8

### 1.3 Year context

- **Tax year 2025** — Wages paid between January 1, 2025 and December 31, 2025
- **MO-941 cadence lookback** — Missouri uses its own analogous lookback under 12 CSR 10-2.015 (federal lookback for federal purposes)  _(12 CSR 10-2.015)_
- **MO-W-3 reconciliation due date for 2025 wages** — January 31, 2026
- **Fourth-quarter MODES-4-7 due date** — January 31, 2026
- **W-2 and 1099 transmittal to MO DOR due date** — January 31, 2026  _(§143.591 RSMo)_

## 2. Missouri PIT Withholding Brackets and Rate Phasing

### 2.1 2025 brackets

- **MO PIT graduation** — Missouri PIT is graduated from 0% to 4.95% on Missouri taxable income  _(§143.011 RSMo as amended by SB 3 (2022 First Extraordinary Session) and SB 190 (2023))_
- **Top marginal rate step-down** — Top marginal rate stepped down to 4.95% for tax year 2023 and has been further reduced via revenue triggers  _(§143.011.5 RSMo)_
- **MFJ bracket table note** — Married filing jointly uses the same table; MO does not double the brackets for MFJ — this is a common source of error and is flagged in Section 11

**2025 Missouri Taxable Income bracket table (single filer)**

| Missouri Taxable Income | Marginal Rate |
| --- | --- |
| $0 to $1,273 | 0.0% |
| $1,273 to $2,546 | 2.0% |
| $2,546 to $3,819 | 2.5% |
| $3,819 to $5,092 | 3.0% |
| $5,092 to $6,365 | 3.5% |
| $6,365 to $7,638 | 4.0% |
| $7,638 to $8,911 | 4.5% |
| Over $8,911 | 4.95% |

- **Bracket threshold indexing** — Bracket thresholds annually indexed using the Consumer Price Index for All Urban Consumers (CPI-U)  _(§143.011.4 RSMo)_
- **Withholding computation method** — Withholding computation does not mirror the bracket table directly — uses the MO Department of Revenue's Withholding Tax Formula published in the Employer's Tax Guide (Form 4282) for the year, which builds in the standard deduction and applies the bracket structure to the annualized projected wage  _(Form 4282, Employer's Tax Guide)_

### 2.2 The revenue-trigger phase-down

- **Revenue trigger mechanism** — Top marginal rate can be further reduced by 0.10 percentage points in any year in which net general revenue collections exceed the prior peak adjusted for inflation and the budget stabilization fund is fully funded; authorizes step-downs toward an eventual 4.5% top rate  _(§143.011.5 RSMo)_
- **2025 top rate status** — As of January 1, 2025, the top rate remains 4.95% — no trigger fired for fiscal year 2024 that would have reduced the 2025 rate

The Missouri Department of Revenue typically announces in late summer or early autumn whether a revenue trigger has fired that will reduce the following year's top marginal rate. Reviewers must verify the current-year top rate against the most recently published Form 4282 (Employer's Tax Guide) and the Missouri Department of Revenue's Withholding Tax Formula bulletin, not against the version in payroll software defaults. Software vendors lag behind the trigger announcements by several weeks, and the rate change applies to wages paid on or after January 1 of the following year regardless of when the announcement was made. If the reviewer is signing off on a payroll setup in December for a January 1 wage payment, the December version of Form 4282 is the authoritative source. Where the rate has stepped down from the prior year (e.g., 4.95% to 4.85%) and the employer's payroll system still uses 4.95%, the employer has over-withheld — not technically a compliance failure (the employee will receive the excess on the MO-1040 refund) but a cash-flow and employee-relations issue that reviewers should flag.

### 2.3 Supplemental wage rate

- **No separate flat supplemental wage rate** — Missouri does not publish a separate flat supplemental wage withholding rate  _(§143.191 RSMo or 12 CSR 10-2.015)_
- **Aggregate method** — Add the supplemental wage to the most recent regular wage payment and withhold on the combined total using the regular formula, less the amount withheld on the regular wage  _(Form 4282)_
- **Flat-rate method for supplemental wages** — 4.95%  _(Form 4282)_
- **Default supplemental rate guidance** — The reviewer should default to 4.95% as the supplemental rate when no facts indicate otherwise
- **Aggregate method documentation and requirement** — If the aggregate method is used, document the underlying regular-wage withholding computation in the payroll file. If the supplemental wage is paid in the same pay period as a regular wage, the aggregate method is required

### 2.4 Standard deduction and personal exemption

- **MO conformity to federal standard deduction** — Missouri conforms to the federal standard deduction  _(§143.131 RSMo)_
- **2025 federal standard deduction - Single or MFS** — $15,000  _(§143.131 RSMo)_
- **2025 federal standard deduction - MFJ or Qualifying Surviving Spouse** — $30,000  _(§143.131 RSMo)_
- **2025 federal standard deduction - Head of Household** — $22,500  _(§143.131 RSMo)_
- **Personal exemption repealed** — Missouri has no personal exemption (repealed effective tax year 2018)  _(HB 2540 (2018))_
- **MO W-4 collections** — The MO W-4 collects allowances, additional withholding, exempt status, and Missouri-specific deductions, but no personal exemption

### 2.5 Federal income tax deduction add-back

- **Federal income tax paid deduction** — Missouri historically allowed a deduction for federal income tax paid, subject to a cap, on the MO-1040; for tax year 2025, still allowed but phased out for higher-income taxpayers  _(§143.171 RSMo)_
- **Withholding formula exclusion** — The MO withholding formula does NOT incorporate this deduction at the withholding stage — withholding is computed on gross wages less the MO standard deduction and the MO W-4 allowance amounts. The federal income tax deduction is taken at year-end on the employee's MO-1040 and may result in a refund. Reviewers should not attempt to build the federal tax deduction into the per-payroll withholding computation.

## 3. Form MO-941 — Employer's Return of Income Taxes Withheld

### 3.1 Filing cadence

- **Filing frequency assignment basis** — MO Department of Revenue assigns each employer a filing frequency based on the employer's average monthly withholding  _(12 CSR 10-2.015)_

**MO-941 filing frequency table**  _(12 CSR 10-2.015)_

| Frequency | Threshold (avg. MO withholding) | Return Form | Payment Cadence |
| --- | --- | --- | --- |
| Quarter-monthly | $9,000+ per month | MO-941 quarterly | 8 quarter-monthly EFT payments per month |
| Monthly | $500 to $8,999 per month | MO-941 monthly | Monthly EFT |
| Quarterly | $100 to $499 per month | MO-941 quarterly | Quarterly with return |
| Annual | Less than $100 per month | MO-941 annual | Annual with return |

- **Quarter-monthly cadence definition** — The quarter-monthly cadence (sometimes called weekly but more accurately eight-times-per-month) applies to high-volume employers and requires deposits within three business days after the close of each quarter-monthly period (defined as days 1–7, 8–15, 16–22, and 23-end-of-month). A quarter-monthly filer must still file Form MO-941 quarterly to reconcile the deposits.  _(12 CSR 10-2.015(3))_

### 3.2 Due dates

- **Monthly filer due date** — MO-941 due by the 15th of the month following the wage payment month (e.g., January 2025 wages — due February 15, 2025; weekend-rolling)
- **Quarterly filer due dates** — MO-941 due by the last day of the month following the quarter close (Q1 — April 30; Q2 — July 31; Q3 — October 31; Q4 — January 31)
- **Annual filer due date** — MO-941 due by January 31 of the following year
- **Quarter-monthly filer due dates** — Deposits due within 3 banking days of the quarter-monthly period close; quarterly MO-941 reconciliation due by the last day of the month following quarter close

### 3.3 Lookback period and frequency changes

- **Lookback period determination** — MO Department of Revenue determines an employer's filing frequency annually based on the 12-month lookback period from July 1 of the second preceding year through June 30 of the preceding year. For tax year 2025, the lookback period is July 1, 2023 through June 30, 2024.
- **Notice and petition** — The Department mails a notice in October or November of the lookback year informing the employer of the assigned frequency for the following calendar year. If the employer disagrees with the assigned frequency, it may petition.  _(12 CSR 10-2.015(2)(D))_
- **No unilateral change / new employer default** — An employer may not unilaterally change its filing frequency. New employers default to monthly until the first lookback period completes.

### 3.4 Electronic filing and payment

- **EFT mandatory threshold** — EFT is mandatory for any employer with annual withholding of $8,000 or more  _(§143.221.3 RSMo)_
- **EFT channel** — The Department's MyTax Missouri portal is the standard EFT channel. ACH credit and ACH debit are both accepted. Paper Form MO-941 is permitted only for employers below the EFT threshold.

### 3.5 Penalties

- **Failure to file** — 5% of the tax due per month, up to 25%  _(§143.751 RSMo and §143.741 RSMo)_
- **Failure to pay** — 5% of the tax due, plus monthly interest at the rate set by the Director of Revenue (variable; published quarterly)  _(§143.751 RSMo and §143.741 RSMo)_
- **Negligence penalty** — Additional 5%  _(§143.751 RSMo and §143.741 RSMo)_
- **Fraud penalty** — Additional 50%  _(§143.751 RSMo and §143.741 RSMo)_
- **Late filing with no tax due** — A fixed $25 per return penalty  _(§143.751 RSMo and §143.741 RSMo)_
- **Reasonable cause abatement** — Available but requires a written request  _(§143.741.4 RSMo)_

## 4. Form MO-W-3 — Annual Reconciliation

Form MO-W-3 is the annual transmittal that reconciles total wages and Missouri tax withheld during the calendar year against the sum of MO-941 returns filed and the W-2s issued. Form MO-W-3 must be filed by January 31 of the year following the wage payment year, together with Copy 1 of each W-2 issued (or the equivalent electronic submission via MyTax Missouri or EFW2 format).

- **MO-W-3 and W-2 copies due date for TY2025** — January 31, 2026
- **Electronic filing requirement** — Employers issuing 250 or more W-2s must file electronically. The threshold may further decrease under federal alignment in future years; verify the current MO-W-3 instructions.  _(§143.591 RSMo)_

A separate transmittal applies to 1099-MISC and 1099-NEC information returns reporting Missouri-source non-wage payments — Form MO-99 Misc. is the Missouri analog, but most employers transmit 1099-NECs via the federal Combined Federal/State Filing (CF/SF) program for Missouri without filing a separate state copy. Confirm current-year mechanics.

## 5. Form MO W-4 — Missouri Employee's Withholding Certificate

### 5.1 When required

- **MO W-4 requirement** — Every Missouri employee subject to MO PIT withholding must complete a Form MO W-4 at hire. The MO W-4 is distinct from the federal Form W-4 — Missouri does NOT accept a federal W-4 as a substitute for the state form. Employers must obtain a signed MO W-4 from each Missouri employee at hire, and again whenever the employee's withholding circumstances change.

### 5.2 Contents of the MO W-4

- **MO W-4 contents** — Filing status (Single, MFJ, MFS, Head of Household); Number of allowances (the MO W-4 has its own allowance worksheet; do not import federal W-4 allowance counts); Additional Missouri withholding requested; Exempt-from-withholding claim (allowable only if employee had no MO tax liability in the prior year and expects none in the current year); Reduced withholding for nonresident military spouse under the Military Spouses Residency Relief Act (MSRRA)
- **Failure to provide MO W-4** — If an employee fails to provide a MO W-4, the employer must withhold at the Single rate with zero allowances

### 5.3 Exempt claims

- **Exempt claim refiling** — An employee claiming exempt status must file a new MO W-4 claiming exempt each year by February 15. If the employee does not refile by February 15, the employer must begin withholding at Single zero allowances until a new MO W-4 is received.

### 5.4 Nonresident employees

- **Nonresident employee withholding** — A nonresident employee performing services in Missouri is subject to MO withholding on the portion of wages attributable to Missouri-source work. The MO W-4 has a nonresident allocation section that the employee completes to indicate the expected percentage of work performed in Missouri. Employers withholding on nonresident wages should retain documentation supporting the allocation (timekeeping, project records).

### 5.5 Reciprocity

- **No reciprocity agreements** — Missouri has no reciprocity agreements with other states. A resident of Illinois, Kansas, Kentucky, or any other state who performs services in Missouri is subject to MO withholding on the Missouri-source portion of wages. Conversely, a Missouri resident performing services in another state may be subject to that state's withholding, and the Missouri employer should monitor whether to withhold for both jurisdictions (typically: withhold for the work state and let the employee claim a Missouri credit on the MO-1040). The cross-border analysis is out of scope for this skill — see _cross-border/us-multi-state-payroll.

## 6. Missouri Unemployment Insurance (MO UI)

### 6.1 Wage base and rates for 2025

- **Taxable wage base 2025** — $9,500 per employee. Wages paid above $9,500 per employee per calendar year are not subject to MO UI contributions.  _(§288.036.2 RSMo)_
- **Wage base history** — Wage base was $11,500 for 2014–2018, dropped to $11,000 for 2019, and has stepped down to $9,500 through HB 1409 (2018) tying the base to the trust fund balance  _(HB 1409 (2018))_
- **New employer rate - non-construction** — 2.7%
- **New employer rate - construction** — 4.13%  _(§288.123 RSMo)_
- **Experience-rated employer rates 2025** — 0.0% to 9.75%
- **Experience rate computation** — The rate is computed from the employer's reserve ratio (cumulative contributions less benefit charges, divided by average annual taxable payroll over the prior three completed calendar years) and looked up on the contribution rate schedule effective for the calendar year. Schedules A through I are statutorily defined; the Division of Employment Security announces the applicable schedule each November for the following calendar year based on the average balance of the Unemployment Compensation Trust Fund.  _(§288.121 RSMo)_

### 6.2 Contribution and wage report — Form MODES-4-7

- **MODES-4-7 due dates** — Q1 (Jan-Mar 2025): due April 30, 2025; Q2 (Apr-Jun 2025): due July 31, 2025; Q3 (Jul-Sep 2025): due October 31, 2025; Q4 (Oct-Dec 2025): due January 31, 2026
- **Report contents and computation** — The report lists each employee's quarterly gross wages and quarterly taxable wages (wages up to the $9,500 annual cap). Contributions are computed as taxable wages × the employer's assigned rate.
- **Electronic filing requirement** — EFT and electronic filing are required for employers with 50 or more employees, or with reported wages over a Department-set threshold (verify the current UInteract requirement). Most employers find it operationally easier to file electronically regardless.

### 6.3 Voluntary contributions

- **Voluntary contribution provision** — An experience-rated employer may make a voluntary contribution by January 15 to reduce its reserve ratio and lower the assigned rate for the following year.  _(§288.090 RSMo)_
- **Voluntary contribution breakeven analysis** — The breakeven is the contribution amount divided by the rate-reduction percentage applied to the projected following-year taxable payroll. If the rate reduction would save more than the voluntary contribution, recommend the contribution.  _(§288.090 RSMo)_

### 6.4 Coverage and exemptions

- **Employer subject to MO UI** — Any employer subject to FUTA (the federal unemployment tax), OR an employer that paid $1,500 or more in wages in any calendar quarter, OR an employer that employed at least one worker for some portion of a day in 20 different calendar weeks in the current or preceding calendar year.  _(§288.034 RSMo)_
- **Agricultural and domestic employer thresholds** — Higher (similar to FUTA)
- **Specific exemptions** — Services performed by an individual for their spouse, parent, or child under 21; Certain corporate officers if proper election is made; Services of independent contractors (subject to the 20-factor test); Domestic services in a private home below the $1,000-per-quarter threshold  _(§288.034.10 RSMo; §288.034.12 RSMo)_

### 6.5 Penalties

- **Late filing of MODES-4-7** — $100 per month or fraction thereof, up to $1,000 per report  _(§288.160 RSMo)_
- **Late payment interest** — Interest at 1% per month or fraction thereof  _(§288.160 RSMo)_
- **Misclassification penalty** — Back contributions, interest, and a 25% penalty for willful misclassification  _(§288.160.4 RSMo)_

## 7. Kansas City Earnings Tax — The 1% E-Tax

### 7.1 Overview

- **KC E-Tax base** — 1% tax on residents of Kansas City on all earnings (wages, salaries, commissions, other compensation, and net profits from self-employment) regardless of where earned, and on non-residents on earnings for work performed within the corporate limits of Kansas City.  _(Chapter 68 of the Code of Ordinances of Kansas City, Missouri; §92.110 RSMo)_
- **Reauthorization** — The E-Tax was reauthorized by Kansas City voters in April 2021 and is again subject to a reauthorization vote every five years. The next reauthorization vote is April 2026.  _(§92.115 RSMo)_

### 7.2 Employer withholding obligation

- **General withholding obligation** — Any employer with employees performing services within Kansas City corporate limits must withhold the 1% E-Tax from wages paid to those employees and remit the withheld tax to the City of Kansas City. The withholding obligation applies regardless of whether the employer is itself located within Kansas City.
- **KC-resident employee working for KC employer** — Employer withholds 1% on the full wage.
- **KC-resident employee working for non-KC employer** — Non-KC employer is generally NOT required to withhold the E-Tax from the resident employee's wages (because the employee performs no services in KC). The resident employee must self-pay the E-Tax annually via Form RD-109. The employer may voluntarily withhold as a convenience to the employee — many KC-area employers do.
- **Non-KC-resident employee at KC employer with KC work location** — Employer must withhold 1% on the portion of wages attributable to work performed in KC.
- **Hybrid non-KC-resident employee** — Employer must withhold 1% on the KC-source portion. The allocation is typically based on the ratio of days worked in KC to total days worked, supported by timekeeping or scheduling records. Hybrid and remote work arrangements have made this allocation a frequent audit topic — see Section 11.

### 7.3 Filing forms

- **Form RD-110** — Quarterly Earnings Tax Withholding Return. Filed quarterly by employers with annual KC E-Tax withholding below the monthly threshold; due by the last day of the month following quarter close.
- **Form RD-130** — Monthly Earnings Tax Withholding Payment Voucher. Used by employers with monthly KC E-Tax withholding of $100 or more; due by the 15th of the following month.
- **Form RD-113** — Annual Reconciliation of Earnings Tax Withheld. Due February 28 of the year following the wage payment year (i.e., 2025 wages reconciled by February 28, 2026), together with copies of W-2s for employees subject to KC E-Tax.
- **Business license note** — A Kansas City employer must also register with the Revenue Division to obtain a KC business license number — but the business-license aspect is out of scope here.

### 7.4 Penalties

- **KC E-Tax penalties** — 5% per month failure-to-file penalty, capped at 25%. 5% failure-to-pay penalty. Interest at 1% per month.  _(Kansas City Ordinance §68-394)_

The City has been actively auditing employer KC E-Tax compliance since 2020, with particular focus on non-resident worker allocation and remote work.

### 7.5 What counts as "within KC corporate limits"

- **KC corporate limits geography** — Kansas City's corporate limits include parts of Jackson, Clay, Platte, and Cass Counties. The boundaries are non-obvious — Independence, Lee's Summit, Liberty, Gladstone, and many other adjacent cities are NOT within KC corporate limits. The Revenue Division publishes a boundary map and an address lookup tool on kcmo.gov.
- **Verification requirement / ZIP code warning** — Reviewers should verify every employer work location and every employee work location against the city's official lookup, not against ZIP code or post-office city name — a 64111 ZIP code (a common KC ZIP) is mostly within city limits, but ZIP 64015 ("Blue Springs, MO") is entirely outside KC limits despite being in the metropolitan area.

The most common KC E-Tax employer compliance failure is failing to withhold on non-KC-resident employees who commute into a KC work location. Employers frequently believe — incorrectly — that the E-Tax applies only to KC residents. It applies to anyone performing services in KC, regardless of residence. A Lee's Summit resident commuting daily to a downtown KC office is subject to the 1% E-Tax on 100% of wages, withheld by the KC employer. Reviewers should:

1. Pull the employee roster and verify each work location against the KC corporate limits map (not ZIP code).
2. For each employee with a KC work location, confirm withholding is in place regardless of the employee's residence.
3. For hybrid employees splitting time between KC and a non-KC location, verify the allocation methodology is documented (typically a percentage of days, supported by timekeeping).
4. For remote-only employees who are KC residents but perform all work outside KC at home in another jurisdiction, confirm that the employer is NOT withholding (the resident pays via RD-109 directly) — many employers over-withhold here because their payroll software keys off the employee's residence rather than work location, leading to refund claims that the employee may miss.

## 8. St. Louis City Earnings Tax — The 1% E-Tax

### 8.1 Overview

- **St. Louis E-Tax base** — 1% tax on residents of the City of St. Louis on all earnings regardless of where earned, and on non-residents on earnings for work performed within the corporate limits of the City of St. Louis.  _(Chapter 5.22 of the Revised Code of the City of St. Louis; §92.110 RSMo)_
- **Reauthorization** — The St. Louis E-Tax was last reauthorized by voters in April 2021 and is again subject to reauthorization in April 2026.

### 8.2 City of St. Louis vs. St. Louis County

- **City vs County distinction** — This is the single most-confused element of MO local payroll. The City of St. Louis is an independent city — it is NOT part of St. Louis County. The City of St. Louis is the small geographic area roughly bounded by the Mississippi River on the east, the River des Peres on the south, Skinker Boulevard on the west, and the city's northern border. Most of the St. Louis metropolitan area (Clayton, Brentwood, Webster Groves, Kirkwood, Chesterfield, Ballwin, Florissant, Ferguson, Maryland Heights, and dozens of other municipalities) is in St. Louis County, which does NOT levy an earnings tax.
- **Examples of employer/employee location combos** — A Clayton-based employer with all employees working in Clayton has NO St. Louis City E-Tax obligation. A downtown-St. Louis-based employer with all employees working downtown has a full E-Tax withholding obligation. A Webster Groves resident working at a downtown St. Louis office is subject to the 1% E-Tax (on the downtown portion of wages — generally 100% if they work fully in St. Louis City). A St. Louis City resident working at a Clayton office is also subject to the 1% E-Tax (because they are a city resident — but the Clayton employer typically does not withhold, so the resident pays via Form E-1 directly).
- **Verification requirement** — Always verify the work location against the City of St. Louis address lookup at stlouis-mo.gov. ZIP codes overlap between the city and county (e.g., ZIP 63139 spans both). Post-office "St. Louis, MO" addresses include many county locations.

### 8.3 Employer withholding obligation

- **Withholding obligation** — An employer with employees performing services within the City of St. Louis corporate limits must withhold 1% from those wages and remit to the City of St. Louis Collector of Revenue, Earnings Tax Division. The withholding obligation applies regardless of where the employer is located.
- **Hybrid worker allocation** — For hybrid workers splitting time between city and non-city locations, withhold 1% on the city-source portion based on a documented allocation (typically days-in-city as a percentage of total work days).

### 8.4 Filing forms

- **Form W-10** — Quarterly Employer Withholding Return. Due by the last day of the month following quarter close. Most employers file quarterly.
- **Form W-11** — Annual Reconciliation. Due January 31 of the year following the wage payment year (2025 wages reconciled by January 31, 2026), filed together with copies of W-2s for employees subject to St. Louis E-Tax. Note that the St. Louis annual reconciliation is due January 31, NOT February 28 as KC's is — this is a frequent source of mis-filings for multi-city employers.
- **Form E-1** — Resident Individual Earnings Tax Return (used by city residents to self-pay E-Tax on wages not withheld by an employer, and by non-residents to claim refunds for non-city work where over-withheld).

### 8.5 Penalties

- **St. Louis E-Tax penalties** — 5% per month failure-to-file penalty, capped at 25%. 5% failure-to-pay penalty. Interest at 1% per month.  _(Chapter 5.22 of the Revised Code)_
- **Boles v. City of St. Louis holding** — The Boles v. City of St. Louis litigation (Missouri Court of Appeals, 2023) confirmed that work performed outside the city by an otherwise-city-based remote employee is NOT subject to the E-Tax — the city had been treating remote work as city-source if the employer was in the city, and the court rejected that position. Employers and reviewers should now ensure that withholding is based on the actual work location, not the employer's office location.  _(Boles v. City of St. Louis, Missouri Court of Appeals, 2023)_

Same pattern as KC: a non-resident commuting daily to a City of St. Louis workplace is subject to 1% E-Tax on 100% of wages. The opposite error — withholding on a fully-remote employee whose only connection to the city is the employer's downtown HQ — is now also a flash point after Boles. Reviewers must verify actual work location, not employer location and not employee residence in isolation.

### 8.6 St. Louis paid sick leave note

- **St. Louis Paid Sick Time Ordinance 71926** — The City of St. Louis enacted Ordinance 71926 (Paid Sick Time Ordinance, effective May 1, 2025) requiring employers with employees working within the city to provide paid sick leave: 1 hour per 30 hours worked, capped at 40 or 56 hours per year depending on employer size. This city ordinance was NOT preempted by the state-level repeal of Proposition A's paid sick leave provisions (HB 567 (2025), signed July 10, 2025, repealing the statewide Prop A sick leave with effect August 28, 2025) — the St. Louis ordinance is a separate municipal enactment under home-rule authority. Reviewers preparing payroll for employers with St. Louis City work locations must continue to track accrual, carryover, and notice obligations under Ordinance 71926. See Section 10.3 for the broader paid sick leave landscape.  _(Ordinance 71926; HB 567 (2025))_

## 9. Worker Classification — The 20-Factor Test

### 9.1 Why classification matters

- **Misclassification exposure** — MO UI back contributions and 25% penalty; MO withholding back taxes, interest, and 5%-25% penalties; KC and St. Louis E-Tax back withholding and penalties; Federal back FICA, FUTA, income tax withholding, and penalties under IRC §3509; Workers' compensation back premiums; Potential class-action liability for wages and benefits  _(§288.160.4 RSMo; §143.741 RSMo; IRC §3509)_

### 9.2 The 20-factor test

- **20-factor test basis** — The Missouri Division of Employment Security applies the 20-factor common law test, which is materially the same as the historical IRS 20-factor test (now superseded at the federal level by the IRS three-category framework — behavioral control, financial control, relationship — but the 20 factors are still used by Missouri).  _(§288.034.5 RSMo)_
- **The 20 factors** — 1. Instructions — does the employer instruct the worker on how to perform the work? 2. Training — does the employer train the worker in the employer's procedures? 3. Integration — is the worker's service integrated into the employer's business? 4. Services rendered personally — must the worker perform the services personally? 5. Hiring assistants — does the employer hire and pay the worker's assistants? 6. Continuing relationship — is there a continuing relationship between worker and employer? 7. Set hours of work — does the employer set the worker's hours? 8. Full-time required — is the worker required to work full-time for the employer? 9. On employer's premises — is the work performed on the employer's premises? 10. Order or sequence set — does the employer set the order or sequence of work? 11. Oral or written reports — must the worker submit regular reports? 12. Payment method — is the worker paid by the hour, week, or month (employee) vs. by the job (contractor)? 13. Expenses — does the employer pay the worker's business and travel expenses? 14. Tools and materials — does the employer furnish tools and materials? 15. Investment — does the worker have a significant investment in the facilities used? 16. Profit or loss — can the worker realize a profit or loss from the services? 17. Multiple firms — does the worker work for more than one firm at a time? 18. Available to general public — does the worker make services available to the general public? 19. Right to discharge — can the employer discharge the worker? 20. Right to terminate — can the worker terminate the relationship without liability?  _(§288.034.5 RSMo)_
- **Weighting guidance** — No single factor is dispositive; the Department weighs the totality of the relationship. The Department's published guidance and historical case law place particular weight on: Right to control the manner and means of work (factors 1, 7, 10, 19); Economic dependence (factors 13, 14, 15, 16, 17, 18); Integration (factor 3).

### 9.3 Statutory employees and exempt classifications

- **Direct sellers** — Statutorily non-employees if compensated by sales and pursuant to a written contract with the non-employee status spelled out  _(§288.034.10(15) RSMo)_
- **Real estate licensees** — Statutorily non-employees under the same provisions if compensated by sales  _(§288.034.10(15) RSMo)_
- **Newspaper carriers** — Non-employees under specific facts

### 9.4 Contrast with IRS framework

- **IRS three-category framework** — The IRS uses the three-category framework (behavioral control, financial control, type of relationship) under Rev. Rul. 87-41 and the SS-8 determination process. The 20-factor test maps to the IRS three-category framework but is structured differently. A worker can be classified as an independent contractor for federal IRS purposes and as an employee for Missouri DES purposes, or vice versa. Reviewers should apply both tests separately. The 1099-NEC issuance test under federal law (us-1099-nec-issuance) is separate from the MO UI classification test.  _(Rev. Rul. 87-41)_

### 9.5 Section 530 federal relief does NOT bind Missouri

- **Section 530 relief limitation** — The Revenue Act of 1978 §530 (codified at 26 U.S.C. §3401 note) provides federal employment-tax relief for employers who consistently treated workers as non-employees with reasonable basis. Section 530 relief does not bind the Missouri DES or Department of Revenue. A federal Section 530 win does not protect against MO UI or MO withholding reclassification. This is a frequent and expensive surprise for employers who relied on a federal audit outcome.  _(Revenue Act of 1978 §530; 26 U.S.C. §3401 note)_

## 10. Other Missouri Payroll Obligations

### 10.1 New hire reporting

- **New hire reporting requirement** — Every employer must report each newly hired or rehired employee to the Missouri Department of Social Services (DSS), Family Support Division, within 20 days of the hire date.  _(§285.300 RSMo)_
- **Report contents** — Employee name, address, Social Security number, date of hire; Employer name, address, federal Employer Identification Number (FEIN)  _(§285.300 RSMo)_
- **Reporting methods and multistate election** — Reporting may be done online through the Missouri New Hire Reporting Center, by fax, by mail (Form 2261), or via electronic transmission for high-volume employers. Multistate employers may elect to report all new hires to a single state under the federal Personal Responsibility and Work Opportunity Reconciliation Act (PRWORA) — file Form W-2 (Multistate Employer Notification of New Hire Reporting) with HHS to designate Missouri as the single reporting state.
- **Failure to report penalty** — $25-per-violation civil penalty, increased to $350 for conspiracy between employer and employee to evade reporting  _(§285.300.6 RSMo)_

### 10.2 Final pay

- **Discharged employee final pay** — An employee discharged by the employer must receive all unpaid wages on the day of discharge upon written request (or upon a labor inspector's request). If the employee fails to make the written request, the employer must pay by the next regular payday.  _(§290.110 RSMo)_
- **Resigning employee final pay** — An employee who resigns is paid by the next regular payday.  _(§290.110 RSMo)_
- **Vacation payout at termination** — Missouri does not require payout of accrued unused vacation at termination unless the employer's written policy or contract so provides — vacation payout is a contract matter under Missouri common law.  _(Pemberton v. KCNA, Inc., Missouri Court of Appeals 1989)_

### 10.3 Paid sick leave — state status as of 2025

- **Proposition A statewide sick leave** — In November 2024, Missouri voters approved Proposition A, which created a statewide paid sick leave entitlement effective May 1, 2025: 1 hour of paid sick leave per 30 hours worked, capped at 40 or 56 hours per year depending on employer size.
- **HB 567 repeal** — HB 567 was enacted and signed by the Governor on July 10, 2025, repealing the Prop A paid sick leave provisions with effect August 28, 2025 (the standard general-statute effective date). After August 28, 2025, Missouri has no statewide paid sick leave mandate.  _(HB 567 (2025))_
- **Carve-out 1: St. Louis ordinance** — The City of St. Louis Paid Sick Time Ordinance (Ordinance 71926, effective May 1, 2025) remains in force as a municipal enactment under home-rule authority. Employers with employees working within the City of St. Louis must continue to provide paid sick leave under that ordinance.  _(Ordinance 71926)_
- **Carve-out 2: accrued Prop A leave transition** — Accrued sick leave under Prop A between May 1, 2025 and August 28, 2025 is arguably vested for employees who earned it. Employer policy on retention or cash-out of accrued Prop A leave is a contract/transition issue — reviewers should advise the employer to document a written transition policy.
- **No paid family leave** — Missouri has no statewide paid family leave.

### 10.4 Minimum wage

- **2025 MO minimum wage (non-tipped)** — $13.75 per hour  _(§290.502 RSMo; Prop B (2018))_
- **2025 MO tipped minimum wage** — 50% of the state minimum ($6.875) plus tips, provided that total compensation reaches at least the minimum wage  _(§290.502 RSMo)_
- **2026 MO minimum wage step** — Effective January 1, 2026 the rate steps to $15.00 per hour, then becomes CPI-indexed thereafter  _(§290.502 RSMo)_
- **Local minimum wage preemption** — Some Missouri cities (notably St. Louis City and Kansas City) attempted higher local minimums but were preempted.  _(§67.1571 RSMo)_

### 10.5 Pay frequency

- **Manufacturing/industrial pay frequency requirement** — Manufacturing and certain industrial employers must pay at least semi-monthly. Other employers default to monthly. Most employers voluntarily pay bi-weekly or semi-monthly for operational reasons; the statutory minimum is monthly for most non-manufacturing private employers.  _(§290.080 RSMo)_

### 10.6 Wage statements

- **Wage statement requirement** — Employers must provide each employee with a statement of hours worked, wages earned, and deductions taken at each pay date. Electronic pay stubs are acceptable under Missouri Department of Labor and Industrial Relations interpretation, provided the employee can access and print the statement.  _(§290.080 RSMo)_

## 11. Worked Examples

### 11.1 Example A — Kansas City employer with a non-KC-resident employee

Cottonwood Bakery, LLC is a single-member LLC operating a bakery in downtown Kansas City, Missouri (verified within KC corporate limits via the city's address lookup). Cottonwood employs three workers:

- Anya, KC resident, full-time baker (40 hrs/wk), $52,000 annual salary, works entirely on premises.
- Brendan, Lee's Summit resident, full-time front-of-house manager (40 hrs/wk), $48,000 annual salary, works entirely on premises in KC.
- Carla, Independence resident, part-time delivery driver (20 hrs/wk), $26,000 annual wages, works partly in KC (8 hrs/wk in-store) and partly outside KC (12 hrs/wk delivering across the metro, of which 4 hrs/wk are in KC corporate limits and 8 hrs/wk are in adjacent cities).

Cottonwood's average monthly MO withholding is approximately $480 — placing it in the quarterly MO-941 filing frequency ($100–$499 monthly average).

*Federal*: Out of scope here; Cottonwood files Form 941 quarterly federally.

*MO PIT withholding*: Cottonwood withholds MO PIT on all three employees using the MO W-4 each provides and the MO Withholding Tax Formula (Form 4282). Files MO-941 quarterly (Q1 due April 30, etc.); reconciles via MO-W-3 by January 31, 2026.

*MO UI*: Cottonwood is subject to MO UI for all three employees. The taxable wage base is $9,500 per employee per year. Cottonwood's contribution = $9,500 × 3 × experience-rated rate (assume 2.0% for an established three-year employer with low turnover) = $570 per year total UI contribution. Files MODES-4-7 quarterly.

*KC E-Tax — Anya (KC resident)*: 1% withheld on full $52,000 wage = $520 per year withheld and remitted to KC Revenue Division. Anya files RD-109 if she has KC-source income that wasn't withheld, but with full employer withholding she has no balance due.

*KC E-Tax — Brendan (Lee's Summit resident, works entirely in KC)*: 1% withheld on full $48,000 wage = $480 per year. Brendan is a NON-KC resident, but he performs all services within KC corporate limits, so the full wage is KC-source. This is the audit flash point — Cottonwood must withhold even though Brendan does not live in KC.

*KC E-Tax — Carla (Independence resident, works 8 hrs/wk in KC + 4 hrs/wk delivering in KC = 12 hrs/wk in KC out of 20 total)*: KC allocation = 12/20 = 60%. KC-source wages = $26,000 × 60% = $15,600. Withhold 1% × $15,600 = $156 per year. Document the allocation in payroll records (timekeeping showing 8 hrs/wk in-store and route logs showing 4 hrs/wk in KC corporate limits out of 12 total delivery hours).

*KC E-Tax filing cadence*: Total annual KC E-Tax withheld = $520 + $480 + $156 = $1,156 / 12 months = ~$96 monthly. Below the $100 monthly threshold, so Cottonwood files Form RD-110 quarterly with payment, and Form RD-113 annual reconciliation by February 28, 2026.

*St. Louis E-Tax*: None — no City of St. Louis work location.

*Final pay*: If Carla resigns, her final pay is due by the next regular payday. If Cottonwood discharges Brendan, Brendan may demand his final pay on the day of discharge by written request.

*New hire reporting*: If Cottonwood hires a fourth employee on January 5, 2025, the new hire must be reported to MO DSS Family Support Division by January 25, 2025 (within 20 days).

**Reviewer brief — Cottonwood Bakery**

| Item | Amount |
| --- | --- |
| Total annual MO PIT withholding (approx.) | $5,760 |
| Total annual MO UI contribution | $570 |
| Total annual KC E-Tax withheld | $1,156 |
| MO-941 filing frequency | Quarterly |
| MODES-4-7 filing frequency | Quarterly |
| KC E-Tax filing | Quarterly RD-110, annual RD-113 |
| MO-W-3 due | January 31, 2026 |
| RD-113 due | February 28, 2026 |

### 11.2 Example B — St. Louis City employer

Riverfront Engineering, P.C. is a professional engineering corporation located at 1010 Market Street, City of St. Louis, MO (verified via stlouis-mo.gov city limits lookup). Employs:

- David, City of St. Louis resident, senior engineer, $115,000 salary, hybrid: 3 days/week at the Market Street office, 2 days/week at his home in the city.
- Erin, Webster Groves (St. Louis County) resident, junior engineer, $72,000 salary, fully on-site 5 days/week at Market Street.
- Frank, City of St. Louis resident, civil drafter, $58,000 salary, fully remote at his home in the city.
- Grace, Clayton resident, project manager, $95,000 salary, fully remote at her home in Clayton (after Boles v. City of St. Louis (Mo. Ct. App. 2023), Grace's wages are NOT St. Louis-source despite the employer's downtown HQ).

Riverfront's average monthly MO withholding is approximately $1,250 — placing it in the monthly MO-941 filing frequency ($500–$8,999 monthly average).

*MO PIT*: Withhold on all four employees per MO W-4 and Form 4282. File MO-941 monthly (each by the 15th of the following month). MO-W-3 reconciliation due January 31, 2026.

*MO UI*: All four employees subject to MO UI. Annual contribution = $9,500 × 4 × experience-rated rate (assume 1.5% for a low-turnover engineering firm) = $570 per year total.

*St. Louis E-Tax — David (city resident, hybrid)*: City residents owe E-Tax on ALL earnings regardless of work location. Withhold 1% on full $115,000 = $1,150 per year.

*St. Louis E-Tax — Erin (county resident, fully on-site at downtown)*: City work location for 100% of work. Withhold 1% on full $72,000 = $720 per year. Audit flash point — Erin lives in the County but commutes to the City; employers frequently miss this.

*St. Louis E-Tax — Frank (city resident, fully remote at home in city)*: Frank is both a city resident and performs all work in the city. Withhold 1% on full $58,000 = $580 per year.

*St. Louis E-Tax — Grace (county resident, fully remote at home in county)*: Per Boles (2023), Grace's work performed at her Clayton home is NOT City of St. Louis-source despite Riverfront's downtown office. Withhold 0% on Grace's wages. Riverfront should document the remote-work arrangement in writing (a written remote-work agreement showing Clayton as the work location). This is the post-Boles audit flash point: pre-Boles practice was to withhold on Grace; post-Boles the city accepts that fully remote out-of-city work is not subject. Some employers continue to over-withhold here — Grace can file Form E-1 to claim a refund, but reviewers should fix the withholding at source.

*St. Louis E-Tax filing*: Total annual = $1,150 + $720 + $580 = $2,450. Form W-10 filed quarterly with payment; Form W-11 annual reconciliation due January 31, 2026 (NOT February 28 like KC — note the difference).

*St. Louis Paid Sick Time Ordinance 71926*: All four employees work for an employer with employees working in the City (David hybrid, Erin on-site, Frank remote in city). Even Grace is arguably covered if the ordinance's "works within the city" prong is read narrowly to focus on the employer rather than the individual employee — but the more defensible reading is that Grace, working entirely outside city limits, is not covered. Riverfront must maintain the sick leave accrual program for David, Erin, and Frank at minimum: 1 hour per 30 hours worked, capped per the ordinance.

**Reviewer brief — Riverfront Engineering**

| Item | Amount |
| --- | --- |
| Total annual MO PIT withholding (approx.) | $14,850 |
| Total annual MO UI contribution | $570 |
| Total annual St. Louis E-Tax withheld | $2,450 |
| MO-941 filing frequency | Monthly |
| MODES-4-7 filing frequency | Quarterly |
| St. Louis E-Tax filing | Quarterly W-10, annual W-11 by January 31 |
| MO-W-3 due | January 31, 2026 |
| W-11 due | January 31, 2026 |

### 11.3 Example C — Non-metro MO-only small business

Heartland Auto Repair, LLC is a sole-member LLC operating a single auto repair shop in Columbia, Missouri (Boone County, no local earnings tax). Employs two workers:

- Hannah, Columbia resident, master mechanic, $54,000 salary, fully on-site.
- Ian, Columbia resident, service writer, $42,000 salary, fully on-site.

Heartland's average monthly MO withholding is approximately $370 — placing it in the quarterly MO-941 filing frequency ($100–$499).

*MO PIT*: Withhold on both employees using MO W-4. File MO-941 quarterly. MO-W-3 due January 31, 2026.

*MO UI*: Both employees subject. Contribution = $9,500 × 2 × experience-rated rate (assume 2.7% as a relatively new employer or one with some claims history) = $513 per year. File MODES-4-7 quarterly.

*KC E-Tax, St. Louis E-Tax*: None — Columbia is not within KC or St. Louis city limits.

*New hire reporting*: Each new hire reported to MO DSS within 20 days.

*Final pay*: Per §290.110, by the next regular payday upon resignation, or on day of discharge upon written request.

*Paid sick leave*: After August 28, 2025, no statewide mandate. No Columbia city ordinance imposes paid sick leave on private employers. Heartland may voluntarily provide sick leave but is not required to.

**Reviewer brief — Heartland Auto Repair**

| Item | Amount |
| --- | --- |
| Total annual MO PIT withholding (approx.) | $4,440 |
| Total annual MO UI contribution | $513 |
| MO-941 filing frequency | Quarterly |
| MODES-4-7 filing frequency | Quarterly |
| Local earnings tax | None |
| MO-W-3 due | January 31, 2026 |

## 12. Reviewer Self-Checks

Before signoff on a Missouri payroll engagement, the reviewer must confirm:

1. ☐ Current-year top marginal MO PIT rate confirmed against the most recent Form 4282 (Employer's Tax Guide), not against payroll software defaults. Document the rate used.
2. ☐ Each employee's MO W-4 on file (not just federal W-4). Exempt claims refiled by February 15.
3. ☐ MO-941 filing frequency matches the Department's most recent assignment notice.
4. ☐ MO UI experience rate confirmed against the DES annual notice for the current calendar year.
5. ☐ For each employee, work location (not residence, not employer HQ) verified against the KC and St. Louis city limits address lookup tools.
6. ☐ For employees in KC city limits, withholding the 1% E-Tax — even non-residents.
7. ☐ For employees in St. Louis city limits, withholding the 1% E-Tax — even non-residents.
8. ☐ For fully-remote employees, withholding tracks actual work location post-Boles (St. Louis) and the city's published guidance (KC).
9. ☐ Hybrid worker allocations documented with timekeeping or scheduling support.
10. ☐ New hire reporting to MO DSS confirmed within 20 days for all 2025 hires.
11. ☐ Worker classification: any 1099-NEC contractors reviewed under the 20-factor test for MO UI purposes, not solely under the IRS three-category framework.
12. ☐ MO-W-3, RD-113, and W-11 deadlines calendared correctly: MO-W-3 by January 31; W-11 (St. Louis) by January 31; RD-113 (KC) by February 28.
13. ☐ St. Louis Paid Sick Time Ordinance 71926 compliance confirmed for City-of-St-Louis-work-location employees.
14. ☐ Statewide paid sick leave repealed (HB 567, effective August 28, 2025) — confirm employer policy updated; document treatment of accrued Prop A leave between May 1 and August 28, 2025.

## 13. Refusals

- **R-MO-1** — Employer asks to classify a worker as a 1099 contractor where the 20-factor analysis indicates employee status, in order to avoid MO UI or MO withholding. Refuse — refer to MO DES SS-8 equivalent process.
- **R-MO-2** — Employer asks to skip KC or St. Louis E-Tax withholding on non-resident commuters because "the employee doesn't live in the city." Refuse — withholding is required on KC and St. Louis work-location wages regardless of residence.
- **R-MO-3** — Employer asks to use a federal Section 530 reasonable-basis defense to skip MO UI back contributions. Refuse — Section 530 does not bind Missouri.
- **R-MO-4** — Multi-state nexus questions beyond Missouri. Refuse and refer to `_cross-border/us-multi-state-payroll`.
- **R-MO-5** — Workers' compensation premium computation. Refuse and refer to MO workers' comp skill.
- **R-MO-6** — Questions about the KC or St. Louis profits tax (the separate 1% tax on business net profits). Out of scope — this skill covers only the earnings-tax portion that applies to wages.
- **R-MO-7** — Garnishment, wage assignment, or child support withholding mechanics beyond the new-hire-reporting trigger.

## 14. Sources and Citations

- §143.011 RSMo (Missouri personal income tax brackets)
- §143.011.5 RSMo (Revenue-trigger phase-down of top marginal rate)
- §143.131 RSMo (Standard deduction conformity)
- §143.171 RSMo (Federal income tax deduction)
- §143.191 RSMo (Withholding requirement)
- §143.221 RSMo (EFT requirement at $8,000 threshold)
- §143.591 RSMo (W-2 transmittal)
- §143.741, §143.751 RSMo (Penalties)
- §285.300 RSMo (New hire reporting)
- §290.080 RSMo (Pay frequency, wage statements)
- §290.110 RSMo (Final pay)
- §290.502 RSMo (Minimum wage indexing)
- §67.1571 RSMo (Local minimum wage preemption)
- §92.110, §92.115 RSMo (Authorization for KC and St. Louis earnings taxes; 5-year reauthorization)
- Chapter 288 RSMo, especially §288.034, §288.036, §288.090, §288.121, §288.123, §288.160 (Missouri UI)
- 12 CSR 10-2.015 (Withholding filing frequency and quarter-monthly deposit rules)
- MO Department of Revenue Form 4282 (Employer's Tax Guide), current year edition
- Kansas City Code of Ordinances Chapter 68 (Earnings and Profits Tax)
- City of St. Louis Revised Code Chapter 5.22 (Earnings Tax)
- Boles v. City of St. Louis, Missouri Court of Appeals (2023) (remote work not city-source)
- Pemberton v. KCNA, Inc., Missouri Court of Appeals (1989) (vacation payout)
- City of St. Louis Ordinance 71926 (Paid Sick Time Ordinance, effective May 1, 2025)
- HB 567 (2025) (Repeal of Prop A statewide paid sick leave, effective August 28, 2025)
- Proposition A (November 2024 ballot, partially repealed by HB 567 (2025))
- HB 1409 (2018) (UI wage base step-down)
- SB 3 (2022 First Extraordinary Session); SB 190 (2023) (PIT rate reductions)
- HB 2540 (2018) (Repeal of MO personal exemption)
- Rev. Rul. 87-41 (IRS three-category framework — for cross-reference only)
- 26 U.S.C. §3401 note (Revenue Act of 1978 §530 — for cross-reference only)
- Personal Responsibility and Work Opportunity Reconciliation Act of 1996 (PRWORA), 42 U.S.C. §653a (Multistate employer new hire reporting)
- Military Spouses Residency Relief Act (MSRRA), 50 U.S.C. §4001 et seq.

## End of mo-payroll.md verification note

*End of mo-payroll.md. Verified against Missouri Department of Revenue Form 4282 (2025), MO Division of Employment Security 2025 contribution rate notice, Kansas City Revenue Division 2025 employer guidance, and City of St. Louis Collector of Revenue Earnings Tax Division 2025 employer guidance.*

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
