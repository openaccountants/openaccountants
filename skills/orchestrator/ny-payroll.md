---
name: ny-payroll
description: Tier 2 New York content skill for employer payroll compliance covering tax year 2025. Includes the 10.9% PIT top rate, supplemental wage rate 11.7% (one of highest in US), the NYS-45 single quarterly combined return for withholding/UI/wage reporting, NYC resident withholding 3.078-3.876%, Yonkers resident +1.6135%, PFL 0.388% (max ~$354/year), DBL mandatory private insurance, MCTMT employer payroll tax in the 12-county MCTD (Zone 1 up to 0.60%, Zone 2 up to 0.34%), the convenience-of-the-employer rule preserving NY source for remote workers, and Wage Theft Prevention Act notice requirements.
jurisdiction: US-NY
domain: state-tax
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# ny-payroll

## New York Payroll Compliance — Tax Year 2025

> **Tier 2 content skill.** This skill MUST be loaded alongside `us-tax-workflow-base` v0.2 or later for workflow scaffolding. For self-employed sole proprietors, see `us-ny-freelance-intake` and `ny-estimated-tax`. This skill is specifically for **employer payroll** obligations in New York State, New York City, and Yonkers.

## 1. Scope

### 1.1 What this skill covers

- **Skill coverage list** — New York State personal income tax (PIT) withholding; Form NYS-45 consolidated quarterly return; NYC resident withholding (3.078%-3.876%); Yonkers resident withholding (+1.6135%) and Yonkers non-resident earner tax (+0.50%); DBL mandatory short-term disability insurance; PFL employee-funded insurance; MCTMT employer-paid payroll tax in 12-county MCTD; SUI contributions; IT-2104; convenience-of-the-employer rule under 20 NYCRR §132.18(a); WTPA notice/recordkeeping; worker classification ABC test; final pay rules under NY Labor Law §191; multi-state allocation  _(20 NYCRR §132.18(a); NY Labor Law §191)_

### 1.2 What this skill does NOT cover

Self-employment / sole proprietor quarterly estimates → see `ny-estimated-tax` and `us-quarterly-estimated-tax`. Personal income tax return preparation (IT-201, IT-203) → see `ny-income-tax`. NYC Unincorporated Business Tax (UBT) for self-employed → see `nyc-ubt`. Pass-Through Entity Tax (PTET) for S corps and partnerships → see `ny-pte-tax-ptet`. Corporate franchise tax (Article 9-A) → see `ny-corporate-franchise-article-9a`. LLC filing fee → see `ny-llc-filing-fee`. Detailed MCTMT computation → see `ny-mctmt`. This skill summarizes only the payroll-side employer obligation. Federal payroll tax computation (FICA, FUTA, federal withholding, Form 941, Form 940). Federal payroll is in scope for a separate federal payroll skill. Statutory non-employee benefits compliance beyond DBL/PFL (e.g., HSA, FSA, 401(k)) — touched on only insofar as they reduce taxable NY wages.

### 1.3 Federal scaffolding assumed

Federal Employer Identification Number (EIN) on file. Federal Form 941 (quarterly) and Form 940 (annual FUTA) compliance is happening separately. Each worker has been classified as either employee (W-2) or independent contractor (1099-NEC) based on federal common-law and the more stringent NY tests in §11. Workers' compensation coverage under NY WCL §10 is in place (separate from DBL/PFL).

## 2. New York PIT Withholding — Tax Year 2025

### 2.1 Statutory authority

- **Withholding duty** — NY Tax Law §671 imposes the duty on every employer who pays wages to a NY resident, or who pays wages to a non-resident for services performed in NY, to deduct and withhold NY state income tax. The withholding tables and methods are published in Publication NYS-50-T-NYS (NY State), NYS-50-T-NYC (NYC), and NYS-50-T-Y (Yonkers), effective for 2025.  _(NY Tax Law §671)_

### 2.2 NY State PIT brackets — 2025 (single filer / Form IT-2104)

**NY State PIT brackets — 2025 (single filer / Form IT-2104)**

| Taxable income | Marginal rate |
| --- | --- |
| Up to $8,500 | 4.0% |
| $8,501 to $11,700 | 4.5% |
| $11,701 to $13,900 | 5.25% |
| $13,901 to $80,650 | 5.50% |
| $80,651 to $215,400 | 6.00% |
| $215,401 to $1,077,550 | 6.85% |
| $1,077,551 to $5,000,000 | 9.65% |
| $5,000,001 to $25,000,000 | 10.30% |
| Over $25,000,000 | **10.90%** (millionaire's surtax — top rate) |

### 2.2 NY State PIT brackets — 2025 (single filer / Form IT-2104)

Married filing jointly and Head of Household brackets follow the same percentages with adjusted bracket widths (see NY IT-201-I). > **Important:** The top 10.90% rate applies only to taxable income above $25M. Most withholding for ordinary employees stops at 6.00% to 6.85% effective marginal. The supplemental rate of 11.70% is the practical "high" most payroll systems will encounter.

### 2.3 Supplemental wage withholding

- **NY State supplemental rate** — 11.70%
- **NYC supplemental rate** — 4.25%
- **Yonkers resident supplemental** — 1.95075%  _(Publication NYS-50-T-Y for 2025)_
- **Yonkers non-resident supplemental** — 0.50% (flat, on wages earned in Yonkers)

### 2.3 Supplemental wage withholding

NY's 11.70% supplemental rate is among the highest in the United States (only California's 10.23% on bonuses over $1M and Idaho's 5.8% baseline are commonly cited as benchmarks — NY effectively tops the supplemental scale at 11.70% for everyone receiving a separately identified bonus).

#### Two methods for supplemental wages

- **Aggregate and flat-rate methods** — Per Publication NYS-50, an employer may choose either: 1. Aggregate method: Add the supplemental payment to the most recent regular wage payment and compute withholding on the combined amount, then subtract what was already withheld. 2. Flat-rate method: Apply 11.70% to the supplemental payment if it is paid separately or separately identified on the pay stub. The flat-rate method requires that the employer has withheld income tax from the employee's regular wages within the current or preceding calendar year.  _(Publication NYS-50)_

### 2.4 Method of computation

- **Computation methods** — Two computation methods are permitted under 20 NYCRR §171: 1. Exact calculation method (formula-based) — used by all modern payroll software. Applies the bracket structure directly. 2. Wage bracket tables — published in NYS-50-T-NYS for manual computation. Suitable only for very small employers (typically <10 employees). For supplemental wages, the flat-rate method described in §2.3 above is the third option.  _(20 NYCRR §171)_

### 2.5 Pay frequency

- **Allowed pay frequencies** — NY allows: weekly, biweekly, semi-monthly, monthly, quarterly, semi-annual, annual, daily/miscellaneous. The annual bracket is converted to the appropriate per-period tax using the conversion factors in NYS-50-T-NYS Table I.  _(NYS-50-T-NYS Table I)_

### 2.6 Deposit frequency

**Deposit frequency by annual NY withholding liability**  _(NYS-45; NYS-1)_

| Annual NY withholding liability | Deposit frequency | Form |
| --- | --- | --- |
| Less than $700 in calendar year | Quarterly with NYS-45 | NYS-45 |
| $700 to $14,999.99 in lookback year | Within 5 business days after payroll | NYS-1 |
| $15,000+ in lookback year | Within 3 business days after payroll | NYS-1 |

### 2.6 Deposit frequency

- **Lookback period** — The lookback period is the four quarters ending on June 30 of the year before. For 2025, the lookback is July 1, 2023 through June 30, 2024.

### 2.6 Deposit frequency

- **Mandatory electronic deposit (PrompTax) threshold** — $100,000+ annual NY withholding

### 2.6 Deposit frequency

> **AUDIT FLASH POINT — Missed PFL/DBL coverage.** NY DTF and the Workers' Compensation Board cross-check NYS-45 wage reports against PFL/DBL insurance carrier records. Employers showing wage reports but no DBL or PFL policy on file are flagged for audit. Most commonly missed by very small (1-4 employee) employers who think they are exempt — they are not.

## 3. Form IT-2104 — NY State Employee's Withholding Allowance Certificate

### 3.1 Purpose

- **IT-2104 purpose** — IT-2104 is the NY-state-specific employee certificate used to determine the number of withholding allowances and any additional amount the employee wishes withheld. It is not the federal Form W-4. Both forms must be on file for any NY employee.

### 3.2 When to require IT-2104

- **When employer must require IT-2104** — The employer MUST require IT-2104 from: 1. Every new hire at the time of hire. 2. Any existing employee who: Changes residency between NY State, NYC, Yonkers, or out-of-state; Wants to change their allowances. 3. By February 1 each year, from any employee who claimed exemption from NY withholding in the prior year (claim must be renewed annually).

### 3.3 If IT-2104 is not received

- **Default withholding if no IT-2104** — If an employee does not provide a completed IT-2104, the employer MUST withhold as if the employee were single with zero allowances. This is the default fallback under 20 NYCRR §171.4(b).  _(20 NYCRR §171.4(b))_

### 3.4 IT-2104 variants

- **IT-2104 variants** — IT-2104: standard form (most employees). IT-2104-E: certificate of exemption (used by employees who expect no NY tax liability). IT-2104-MS: military spouse residency relief (federal Servicemembers Civil Relief Act). IT-2104-IND: certificate for Native Americans living and working on reservation. IT-2104-P: voluntary periodic pension payment withholding certificate. IT-2104.1: nonresident certificate for employees working in NY some days only (used to claim allocation, see §10).

### 3.5 High-allowance reporting

- **High-allowance DTF reporting requirement** — If an employee claims more than 14 allowances on IT-2104, the employer must send a copy of the form to the NY DTF within 90 days of receipt (under NY Tax Law §671(a-1)). This is a continuing compliance burden the federal W-4 abolished in 2020 but NY retained.  _(NY Tax Law §671(a-1))_

## 4. NYS-45 — Quarterly Combined Return

### 4.1 The single-return advantage

- **NYS-45 consolidation** — NYS-45 (Quarterly Combined Withholding, Wage Reporting, and Unemployment Insurance Return) consolidates three filings into one quarterly form: 1. State income tax withholding reconciliation (Part B). 2. Unemployment insurance contributions computation and payment (Part A). 3. Wage reporting for individual employees (Part C, with employee-level Form NYS-45-ATT or Part C of NYS-45 itself for ≤5 employees). This is unusual — most states require separate withholding and UI filings. NY's consolidation simplifies compliance but means a single late filing exposes the employer to multiple penalty regimes.

### 4.2 Due dates

**NYS-45 due dates by quarter**

| Quarter | Period covered | NYS-45 due date |
| --- | --- | --- |
| Q1 | Jan 1 - Mar 31 | April 30 |
| Q2 | Apr 1 - Jun 30 | July 31 |
| Q3 | Jul 1 - Sep 30 | October 31 |
| Q4 | Oct 1 - Dec 31 | January 31 (following year) |

### 4.2 Due dates

- **Weekend/holiday due date rule** — If the due date falls on a weekend or NY State holiday, the form is due the next business day.

### 4.3 Mandatory e-filing

- **Mandatory e-filing requirement** — All NYS-45 returns must be e-filed via the NY Online Services for Business portal. Paper filing is no longer accepted for any employer with internet access (effective tax years 2015+ under TSB-M-15(2)C).  _(TSB-M-15(2)C)_

### 4.4 Structure

- **NYS-45 parts structure** — Part A — Unemployment Insurance: Total wages, UI wages (subject to wage base), excess wages, UI contribution rate, contribution due. Also captures the Re-employment Service Fund (RSF) surcharge of 0.075% on the same UI wage base. Part B — NY State, NYC, Yonkers Income Tax Withholding: Total tax withheld this quarter for each of the three jurisdictions. Subtract deposits already made via NYS-1. Net result is the balance due (or overpayment). Part C — Quarterly Employee/Payee Wage Reporting: For each employee, gross wages and total NY state withholding YTD through the end of the quarter. Filed on NYS-45-ATT if more than 5 employees, or directly on NYS-45 Part C if 5 or fewer.

### 4.5 Annual reconciliation

- **Q4 annual reconciliation** — The fourth-quarter NYS-45 (due January 31) also functions as the annual reconciliation. Part C reports YTD wages and withholding for each employee, which must reconcile to the W-2 issued for that employee. NY DTF cross-references NYS-45 Q4 against W-2 Form NY-3 (state copy of W-2 transmitted through SSA filing or directly to NY DTF).

### 4.6 Penalties

- **NYS-45 penalties** — Late filing: 5% of unpaid tax per month (or fraction), max 25%, plus $50 minimum if zero balance. Late payment: 0.5% per month on unpaid tax, max 25%. Late wage reporting (Part C): $1 per employee per quarter not reported timely, with a minimum of $50 and a maximum of $10,000 per quarter (NY Labor Law §581(1)(e)). Failure to file UI return: greater of 5% of contributions due or $100 per quarter. Negligence/fraud: up to 50% of underpayment.  _(NY Labor Law §581(1)(e))_

## 5. NYC Resident Withholding

### 5.1 Statutory framework

- **NYC PIT statutory framework** — NY City imposes its own personal income tax on city residents under NYC Administrative Code §11-1701. The tax is administered by NY State DTF (not the city directly) and withheld via NYS-45 alongside state tax.  _(NYC Administrative Code §11-1701)_

### 5.2 Residency test

- **NYC resident definition for withholding** — NYC resident for withholding purposes means an employee who: Is domiciled in NYC, OR Maintains a permanent place of abode in NYC AND spends more than 183 days of the taxable year in NYC. The 183-day test is the "statutory resident" rule. Day counting includes any part of a day spent in NYC (the so-called "one-foot-in-NYC" rule, modified post-Gaied v. NY DTAC (2014) to require that the abode be reasonably used as a residence by the taxpayer, not just owned).  _(Gaied v. NY DTAC (2014))_

### 5.3 NYC PIT brackets — 2025

**NYC PIT brackets — 2025**  _(NYC Administrative Code §11-1701)_

| Taxable income | Marginal rate |
| --- | --- |
| Up to $12,000 | 3.078% |
| $12,001 to $25,000 | 3.762% |
| $25,001 to $50,000 | 3.819% |
| Over $50,000 | **3.876%** |

### 5.3 NYC PIT brackets — 2025

- **Combined effective rate note** — These rates are layered ON TOP OF the NY State rate. A NYC resident in the top NYC bracket who is also in the top NY State 6.85% ordinary bracket pays an effective marginal of 6.85% + 3.876% = 10.726% state-and-local on ordinary wage income before NY State surtaxes apply.

### 5.4 Employer obligation

- **Employer obligation to withhold NYC tax** — NYC tax must be withheld by: Any employer who pays wages to a NYC-resident employee (regardless of where the employer is located or where work is performed). This is a "follow-the-employee" rule based on residency. NYC tax is NOT withheld for non-residents working in NYC, because the NYC Commuter Tax was repealed in 1999 (Chapter 5 of the Laws of 1999). NYC has no non-resident wage tax.  _(Chapter 5 of the Laws of 1999)_

### 5.5 Tracking residency changes

- **Residency change withholding adjustment** — When a NYC resident moves out of NYC mid-year, or a non-resident moves into NYC, the employer must adjust withholding starting with the next regular pay period after the employee submits an updated IT-2104. The employee bears the burden of notifying the employer; the employer is not expected to discover residency changes independently.

### 5.5 Tracking residency changes

> **AUDIT FLASH POINT — NYC dual-residency challenges.** NY DTF aggressively pursues NYC residency cases. Employees who claim non-NYC residency while maintaining a NYC apartment, NYC family ties, or a NYC employer address are routinely audited under the statutory-resident 183-day test. Employers should obtain (and retain) the IT-2104 in effect for each pay period and not "split the difference" on residency in the absence of an employee declaration. Documentation in payroll files is the first line of defense in a residency audit.

## 6. Yonkers Withholding

### 6.1 Two distinct Yonkers taxes

- **Yonkers Resident Income Tax Surcharge** — 16.75% of the employee's NY State tax liability, which effectively translates to approximately 1.6135% on wages at the typical 6.85% NY State bracket. (The Yonkers surcharge is computed as a percentage of NY tax, not of wages, so the effective rate on wages varies with the NY bracket.)
- **Yonkers Non-Resident Earnings Tax** — 0.50% flat on wages earned by a non-resident for services performed within Yonkers  _(Yonkers Municipal Code §15-200)_

### 6.2 Withholding mechanics

- **Yonkers withholding mechanics** — Yonkers resident withholding: Withheld using the rate table in Publication NYS-50-T-Y. The employer applies the resident surcharge withholding tables to the same wage that the NY State tax was computed on. Yonkers non-resident earnings withholding: The employer must withhold 0.50% of wages allocated to Yonkers for any employee who performs services within the city of Yonkers. This requires day-counting allocation similar to the NY State non-resident rules.  _(Publication NYS-50-T-Y)_

### 6.3 Supplemental rates

- **Yonkers resident supplemental** — 1.95075%  _(Publication NYS-50-T-Y for 2025)_
- **Yonkers non-resident supplemental** — 0.50% (flat, on wages earned in Yonkers)

### 6.4 Form IT-2104 for Yonkers

- **Yonkers declaration and default rule** — Yonkers residency and Yonkers work allocation are declared by the employee on IT-2104 (state) — there is no separate Yonkers form. If the employee fails to declare Yonkers status, the employer must default to the most conservative position (typically resident if the employer knows the employee's home address is in Yonkers; otherwise non-resident with full Yonkers work allocation if work is performed in Yonkers).

## 7. Disability Benefits Law (DBL)

### 7.1 What DBL is — and is not

- **DBL definition** — DBL is NY's mandatory short-term disability insurance program under NY Workers' Compensation Law (WCL) Article 9. It covers employees who become disabled by non-work-related injury or illness (work-related is workers' comp under WCL Article 2). > Critical clarification: DBL is NOT a payroll tax. Unlike PFL (which is a state-run insurance program with mandatory employee payroll contribution), DBL is private insurance purchased by the employer from a NY-licensed carrier or the NY State Insurance Fund. The employer pays the premium; the employer may deduct a maximum of $0.60 per week per employee toward the premium.  _(NY WCL Article 9)_

### 7.2 Coverage requirement

- **DBL coverage requirement and exemptions** — An employer must provide DBL coverage if it has one or more employees for at least 30 days in any calendar year. The 30-day threshold can be cumulative across the year, not 30 consecutive days. Exemptions (rare): Sole proprietor with no employees. Partnership where only partners are involved. Religious organizations (limited). Federal government. Certain agricultural workers.

### 7.3 Employee contribution

- **Maximum weekly employee DBL contribution** — $0.60 per week  _(WCL §209(3))_
- **Maximum annual employee DBL contribution** — $0.60/week × 52 weeks = $31.20 maximum annual employee contribution to DBL  _(WCL §209(3))_

### 7.4 Benefit

- **DBL benefit amount and cap** — DBL provides 50% of the employee's average weekly wage, up to a maximum of $170/week, for up to 26 weeks during any 52-week period. This maximum has not been adjusted since 1989 and remains $170 in 2025.

### 7.5 Coordination with PFL

- **DBL/PFL coordination limit** — DBL covers the employee's own non-work-related disability. PFL (§8 below) covers leave to care for family. The two cannot be received simultaneously, but together they may not exceed 26 weeks of leave in any 52-week period. DBL claims and PFL claims are typically filed with the same private insurance carrier under a combined policy.

### 7.6 Reporting

- **DBL reporting obligations** — DBL is not reported on NYS-45. The carrier (or NY State Insurance Fund) handles regulatory reporting. The employer's only payroll-side obligation is: 1. Maintaining the policy in force. 2. Deducting up to $0.60/week from employee paychecks (optional; if deducted, must be shown on the pay stub). 3. Posting the DB-120 notice in the workplace.

### 7.6 Reporting

> **AUDIT FLASH POINT — Missed DBL coverage.** Small employers with 1-4 employees frequently fail to obtain DBL coverage believing it applies only to larger employers. The WCL §220 penalty for non-coverage is $500 per 10-day period of non-coverage, plus $250 per day for employees who would have been covered, plus full liability for any disability claim that would have been covered. Cross-checked against NYS-45 wage filings.

## 8. Paid Family Leave (PFL)

### 8.1 What PFL is

- **PFL definition** — PFL is NY's state-mandated paid family leave insurance program established under WCL Article 9, enacted in 2016 and phased in from 2018. It is funded entirely through employee payroll deductions — no employer contribution is required or permitted.  _(WCL Article 9)_

### 8.2 Coverage requirement

- **PFL coverage and eligibility** — PFL coverage is automatic when DBL coverage is required. The same employer who must provide DBL must provide PFL through the same carrier (typically as a rider on the DBL policy). Eligibility: an employee is eligible for PFL benefits after working for the employer for: Full-time (20+ hours/week): 26 consecutive weeks. Part-time (<20 hours/week): 175 days worked.

### 8.3 Employee contribution rate — 2025

- **2025 PFL employee contribution rate** — 0.388% of the employee's gross wages, capped at an annual maximum of $354.53 (based on the NY State Average Weekly Wage of $1,757.19 × 52 weeks × 0.388% = $354.53)  _(NY DFS September 2024 announcement)_

### 8.3 Employee contribution rate — 2025

- **Annual rate-setting process** — This is the rate set by NY DFS in the September 2024 announcement for the 2025 calendar year. The rate is reviewed and adjusted annually by the NY Department of Financial Services.

### 8.4 Withholding mechanics

- **PFL withholding mechanics** — The PFL contribution is: Deducted from the employee's gross wages each pay period. Computed on gross wages (no exclusions for pre-tax benefits except as specifically excluded by statute). Reported as a deduction on the pay stub. Remitted by the employer to the insurance carrier (NOT to NY DTF) on the carrier's billing cycle. The deduction must stop once the employee has contributed $354.53 in the calendar year — the employer cannot over-collect.

### 8.5 Benefit

- **PFL benefit duration and cap** — Duration: Up to 12 weeks per 52-week period. Benefit amount: 67% of the employee's average weekly wage, capped at 67% of the NY State Average Weekly Wage ($1,757.19 × 67% = $1,177.32/week maximum).

### 8.6 Reasons for leave

- **Qualifying PFL leave reasons** — Bonding with a newborn, adopted, or foster child (within 12 months). Caring for a family member with a serious health condition. Qualifying military exigency. (As of January 2023) Caring for an extended family member including siblings.

### 8.7 Tax treatment

- **PFL contribution and benefit tax treatment** — PFL employee contributions are deducted from after-tax wages (not pre-tax). They are subject to federal income tax, federal FICA, and NY income tax. PFL contributions are reported in Box 14 of Form W-2 as "NYPFL" (informational). PFL benefits received by the employee are taxable as wages for both federal and NY purposes and are reported on Form 1099-G or Form W-2 (depending on the carrier).

### 8.8 Reporting

- **PFL reporting obligation** — PFL is not reported on NYS-45. The carrier remits to the state. The employer's payroll obligation ends at the deduction and remittance to the carrier.

## 9. State Unemployment Insurance (SUI)

### 9.1 Statutory authority

- **SUI administration** — NY UI is administered by the Department of Labor under Labor Law Article 18. Employers register for an Employer Registration Number (which is the same as the NY withholding ID) and report wages quarterly on NYS-45 Part A.  _(Labor Law Article 18)_

### 9.2 Wage base — 2025

- **2025 NY UI taxable wage base** — $12,800 per employee per year  _(New York Department of Labor and 2025 NYS-50 guidance)_

### 9.2 Wage base — 2025

NY's wage base is among the lowest in the nation (compare: WA $72,800, OR $59,800, NJ $43,300 in 2025) — a key feature in multi-state employer cost comparisons. The wage base is indexed annually. The 2025 figure is $12,800, per New York Department of Labor and 2025 NYS-50 guidance.

### 9.3 Contribution rate

- **New employer UI rate 2025** — 4.10% (3.4% normal + 0.625% subsidiary + 0.075% Re-employment Service Fund). New employer status lasts for the first 4 quarters then experience rating begins.
- **Established employer rate range** — 2.10% to 9.90% total including RSF depending on the employer's reserve account balance and experience.
- **Re-employment Service Fund (RSF) surcharge** — 0.075% surcharge on top of the regular rate, applied to the same UI wage base. Not technically part of the UI rate but reported on NYS-45.

### 9.3 Contribution rate

- **Interest assessment surcharge status** — Applied separately when the state's UI Trust Fund has outstanding federal loans. As of 2025, NY has repaid its COVID-era federal advance, so no IAS applies for 2025.

### 9.4 New-employer transition to experience rating

- **Transition timing** — A new employer's account is rated effective the first January 1 after the employer has been liable for at least four full quarters and had wages reported in those quarters. The new-employer rate continues until the account is rated.

### 9.5 SUTA dumping prevention

- **SUTA dumping prevention rules** — NY follows the federal SUTA Dumping Prevention Act. Mandatory rate transfer rules apply when there is substantially common ownership, management, or control between two employers — the favorable experience rate of one cannot be "dumped" by closing one and opening another. Violation penalties: highest rate plus 2% for 4 years, plus criminal penalties.  _(federal SUTA Dumping Prevention Act)_

### 9.6 Voluntary contributions

- **Voluntary contribution window** — NY allows voluntary contributions to lower the assigned rate, but the timing window is narrow (30 days from receipt of rate notice). This is a planning lever rarely used outside very large employers.

### 9.7 FUTA credit interaction

- **FUTA credit interaction** — Employers paying NY UI on time and in full receive the standard 5.4% FUTA credit, reducing FUTA from 6.0% to 0.6% on the federal $7,000 wage base. NY has historically had FUTA credit reductions during recessions due to federal loans; for 2024 (paid in January 2025 with Form 940), NY has no FUTA credit reduction because the federal loan was repaid.

## 10. Convenience-of-the-Employer Rule

### 10.1 Why this matters

- **Convenience rule text and summary** — The "convenience of the employer" rule (often abbreviated convenience rule or COE rule) is one of the most aggressive sourcing rules in US state tax. It applies to wages paid by a NY-based employer to an employee who works outside NY. The rule, codified in 20 NYCRR §132.18(a), states: > Any allowance claimed for days worked outside New York State must be based upon the performance of services which, of necessity (as distinguished from convenience), obligate the employee to out-of-state duties in the service of his employer. Such duties are those which, by their very nature, cannot be performed at the employer's place of business. In plain English: a remote worker employed by a NY employer is treated as a NY-source employee unless the employer requires the work to be done out-of-state.  _(20 NYCRR §132.18(a))_

### 10.2 What "necessity" means

- **NY DTF interpretation of necessity** — The NY DTF has interpreted "necessity" narrowly. An employee working from a Florida apartment "for convenience" because she prefers the climate is still earning NY-source wages. The work has to of necessity be performed outside NY. NY DTF guidance under TSB-M-06(5)I and subsequent rulings has held: Working from a home office in another state because the employee prefers it: NY source. Working from a client site in another state because the client requires onsite presence: out-of-state source. Working from a second office of the employer in another state: out-of-state source (provided the second office is bona fide). COVID-era remote work: NY DTF held that COVID telework was generally for convenience unless the employer formally closed its NY office (TSB-M-21(1)I, March 2021).  _(TSB-M-06(5)I; TSB-M-21(1)I)_

### 10.3 The "bona fide employer office" exception

- **Bona fide employer office test** — If the employee works from a home office that qualifies as a bona fide employer office under the secondary factor test in TSB-M-06(5)I, then those days are sourced to the state where the home office is located. The test requires the home office to satisfy either: The primary factor (the home office contains or is near specialized facilities not available at the employer's office), OR At least 4 of 6 secondary factors and 3 of 10 "other factors" (including: employer reimburses home office expenses; employer-issued telephone; employer's name on entrance; employer requires meetings at the home office; etc.). In practice, almost no remote worker's home office satisfies this test. The result is that virtually all NY-employer remote workers in other states pay NY tax on 100% of their wages.  _(TSB-M-06(5)I)_

### 10.4 Practical employer consequences

- **Employer consequences for relocated employees** — If an employer in NY has an employee who has relocated to (e.g.) Florida or Texas: 1. The employer continues to withhold NY State PIT (and NYC tax if the employee is a NYC resident — though the residency would generally lapse). 2. The employee receives a W-2 with NY State wages = 100% of compensation. 3. The employee files a NY non-resident return (IT-203) to report NY-source wages. 4. The employee may be eligible for a resident state credit for taxes paid to NY, but only if the resident state recognizes the NY tax on those wages as taxes paid on the resident state's source — many do not for "convenience-source" wages.

### 10.5 Multistate double taxation risk

- **Double taxation risk and employer obligation** — Several states (CT, NJ, MA) have enacted "retaliatory" convenience rules or specific case law to push back on NY's rule. The result is that a NY-employer employee living in (e.g.) NJ may have both states claim full sourcing of the wages. The employee typically files NY non-resident, claims NJ resident credit, and litigates. Several major cases are ongoing in 2025 challenging the NY rule on Dormant Commerce Clause grounds. For payroll purposes, the employer's obligation is to withhold NY tax on the full wage. The employer is generally not required to withhold the resident state's tax unless the employer has a sufficient nexus with the resident state to be a registered withholding agent there. This is a fact-specific determination.

### 10.6 Form IT-2104.1 (nonresident allocation)

- **IT-2104.1 nonresident allocation form** — A nonresident employee who is in NY only some days and out-of-state other days can submit Form IT-2104.1 to estimate the percentage of days worked in NY. The employer then withholds NY tax only on that allocated portion. This form is for NY days vs. out-of-state days — NOT for convenience-rule cases. The convenience rule applies AFTER IT-2104.1 allocation by treating "convenience" out-of-state days as NY days.

### 10.6 Form IT-2104.1 (nonresident allocation)

> **AUDIT FLASH POINT — Convenience-of-employer audits.** NY DTF has dramatically increased convenience-rule audits post-pandemic. The DTF's data analytics flag NY-employer W-2s with employee addresses in low/no-tax states (FL, TX, TN, NH) for review. Penalties for misallocation include underpayment interest + 50% negligence penalty. Employer's documentation should include: written remote-work policy stating whether out-of-state work is permitted or required, employee declarations on IT-2104.1, contemporaneous records of any client-site work that genuinely requires out-of-state presence.

## 11. Wage Theft Prevention Act (WTPA)

### 11.1 Statutory authority

- **WTPA authority** — NY Labor Law §195 (as amended by the Wage Theft Prevention Act, Chapter 564 of the Laws of 2010, and subsequent amendments).  _(NY Labor Law §195)_

### 11.2 Required at hire

- **Hire notice contents** — Every NY employer must give every new employee, at the time of hire, a written notice containing: 1. The employee's rate(s) of pay (hourly, salary, commission, etc.) and basis of pay. 2. Overtime rate (if non-exempt under NY Labor Law). 3. Regular payday designated by the employer. 4. The employer's official name and any "doing business as" (DBA) names. 5. Physical address of the employer's main office and a mailing address (if different). 6. Employer's phone number. 7. Allowances claimed (tips, meals, lodging, if any).

### 11.3 Language requirements

- **Notice language requirements** — The notice must be provided in English AND in the employee's primary language, if NYS DOL has produced a template in that language. NYSDOL provides templates in English, Spanish, Chinese, Korean, Polish, Russian, Haitian Creole, and Bengali. If the primary language is not one of these, English alone is sufficient.

### 11.4 Employee signature

- **Signature and retention requirement** — The employee must sign the notice. The employer must keep the signed notice for six years after the date of hire (Labor Law §195(4)).  _(Labor Law §195(4))_

### 11.5 Required on each pay statement

- **Required pay stub contents** — Each pay stub (under Labor Law §195(3)) must contain: Pay period dates. Employee name. Employer name, address, phone. Gross wages. Deductions itemized. Net wages. For non-exempt: regular hours, overtime hours, rates of pay. For piece-rate or commission: applicable piece rate or commission terms.  _(Labor Law §195(3))_

### 11.6 Penalties

- **Failure to provide hire notice** — $50 per workday per employee, max $5,000 per employee  _(Labor Law §198(1-b))_
- **Failure to provide compliant pay stub** — $250 per workday per employee, max $5,000 per employee  _(Labor Law §198(1-d))_

### 11.6 Penalties

- **Willful or repeat violations and litigation exposure** — Willful or repeat violations: increased to up to 100% of wages, plus liquidated damages of 100% on top of the wage shortfall. Attorney's fees and costs are recoverable by the employee. WTPA is a private right of action — employees can sue directly, often as class actions. This is the largest source of NY wage-and-hour litigation exposure for small employers.

## 12. Worker Classification

### 12.1 Why classification matters

- **Consequences of misclassification** — A misclassified worker — labeled "independent contractor" but legally an employee — triggers retroactive liability for: All NY state PIT that should have been withheld. All FICA and FUTA that should have been paid (federal exposure). All NY UI contributions on the unreported wages. DBL and PFL coverage gaps. WTPA violations (no hire notice, no pay stub). Workers' compensation premium audit assessment. NYC commercial rent tax exposure if the "contractor" is treated as having used the employer's space. Penalties typically 50% of the tax due.

### 12.2 NY classification tests — multiple frameworks

NY uses different tests depending on the purpose:

#### (a) NY Common Law Test (for state PIT withholding)

- **NY common law test** — For income tax withholding purposes, NY follows the federal common-law test (the 20-factor test from Rev. Rul. 87-41 and the federal three-category test of behavioral control, financial control, and relationship). This is the same test used for federal employment tax classification.  _(Rev. Rul. 87-41)_

#### (b) ABC Test (for UI and certain wage-and-hour purposes)

- **ABC test for NY UI** — For NY UI purposes, NY uses an "ABC test" — modified from the classic Massachusetts ABC test. Under NY Labor Law §511 (definition of "employment"), a worker is presumed to be an employee unless the hiring entity proves ALL THREE: A: The worker is free from control and direction in the performance of the service. B: The service is performed outside the usual course of business of the employer or outside all the employer's places of business. C: The worker is customarily engaged in an independently established trade, occupation, profession, or business of the same nature as the service performed. This is a strict test — failure on any prong means employment status for UI purposes.  _(NY Labor Law §511)_

#### (c) Construction Industry Fair Play Act (Labor Law §861-c)

- **Construction industry presumption** — For construction work, an additional statutory presumption applies: a person performing construction services for a contractor is presumed an employee unless the contractor proves the worker satisfies a 12-factor independent contractor test under §861-c. This is the strictest classification regime in NY.  _(Labor Law §861-c)_

#### (d) Commercial Goods Transportation Fair Play Act

- **Commercial goods transportation presumption** — Similar statutory presumption for commercial goods transportation, under Labor Law §862-b.  _(Labor Law §862-b)_

### 12.3 Practical guidance

- **Most restrictive test guidance** — Because the tests can produce different results for different purposes, a "safe" classification of a worker as an independent contractor requires satisfying the most restrictive test applicable to the work — usually the ABC test. Software developers and other professional services freelancers typically pass the ABC test if they: Have multiple clients, not just one. Provide their own equipment. Set their own hours. Hold themselves out as an independent business (LLC, business cards, separate website, etc.). Are not integrated into the employer's regular operations.

### 12.4 Coordination with Form 1099-NEC

- **1099-NEC issuance threshold and NY conformity** — For workers properly classified as independent contractors (passing the relevant test), the employer issues Form 1099-NEC if total payments to the contractor are $600 or more in the calendar year (rising to $2,000 in 2026 under OBBBA — see `us-1099-nec-issuance`). NY does not have a separate state 1099-NEC equivalent — the federal Form 1099-NEC is the only required information return for NY purposes (NY participates in the federal Combined Federal/State Filing program for 1099s).

### 12.5 NY Freelance Isn't Free Act

- **Freelance Isn't Free Act requirements** — Effective August 28, 2024, NY's Freelance Isn't Free Act (Labor Law §191-d) requires: A written contract for any freelance work of $800 or more (single project or cumulative over 120 days). Payment to the freelancer within 30 days of completion (or as specified in the contract). Penalties: double damages, attorney's fees, $250 to $25,000 statutory penalties. This applies to independent contractor relationships, not employee relationships. NYC has a separate Freelance Isn't Free Act (NYC Admin Code §20-927) that has been in effect since 2017 with similar requirements.  _(Labor Law §191-d; NYC Admin Code §20-927)_

## 13. Final Pay Rules

### 13.1 Statutory authority

- **Final wage payment authority** — NY Labor Law §191(3): final wages must be paid to the discharged or resigning employee not later than the regular payday for the pay period during which the termination occurred.  _(NY Labor Law §191(3))_

### 13.2 Application

- **Final pay application scenarios** — Voluntary resignation: Final wages due on the next regular payday. Involuntary termination: Final wages due on the next regular payday. Death: Final wages may be paid to the surviving spouse, parent, child, or sibling (Labor Law §191(1)(b)(iii)) without going through estate administration if the amount is under $30,000.  _(Labor Law §191(1)(b)(iii))_

### 13.3 PTO/vacation payout

- **PTO payout policy enforcement** — NY does not require employers to pay out accrued unused vacation or PTO at termination — but if the employer's written policy or contract provides for it, NY DOL will enforce that policy under §198-c. Most employers have such policies; the written policy must be followed.  _(§198-c)_

### 13.4 Severance

- **Severance treatment** — Severance is not required under NY law. If offered, it is generally subject to standard wage withholding (FICA + federal + NY state + NYC if applicable). Severance paid in a separate check is supplemental wage subject to the 11.70% flat rate option.

### 13.5 Method of payment

- **Final pay payment methods** — Final pay must be by check, cash, direct deposit (if previously authorized), or payroll debit card (with employee consent and meeting §192 requirements). The employee may withdraw direct deposit authorization at termination and require a paper check.  _(§192)_

### 13.6 Last paycheck deductions

- **Prohibited final pay deductions** — Employers may NOT deduct from final pay for: Cash register shortages. Damaged or lost equipment. Customer non-payment. Uniforms (except as permitted under §193). Deductions are limited under §193 to those expressly authorized in writing by the employee and falling within statutory categories.  _(§193)_

## 14. MCTMT — Payroll-Side Summary

> **Refer to `ny-mctmt` for full computation rules and quarterly filing mechanics.** This section provides only the payroll-side summary an employer needs.

### 14.1 What MCTMT is

- **MCTMT definition** — The Metropolitan Commuter Transportation Mobility Tax (MCTMT) is an employer-paid payroll tax in the 12-county Metropolitan Commuter Transportation District (MCTD) under NY Tax Law Article 23. Employees do not pay MCTMT; it is entirely an employer obligation.  _(NY Tax Law Article 23)_

### 14.2 MCTD geography — Zones (2025)

- **MCTD zone geography** — The MCTD is divided into two zones effective for tax years 2024+ (Chapter 56 of the Laws of 2023): Zone 1: New York City — Bronx, Kings (Brooklyn), New York (Manhattan), Queens, Richmond (Staten Island) counties. Zone 2: Suburban — Rockland, Nassau, Suffolk, Orange, Putnam, Dutchess, Westchester counties.  _(Chapter 56 of the Laws of 2023)_

### 14.3 Rate structure — 2025

**Zone 1 (NYC) MCTMT rate structure**

| Quarterly payroll expense | Rate |
| --- | --- |
| ≤ $312,500 | 0% (under threshold) |
| $312,500.01 to $375,000 | 0.11% |
| $375,000.01 to $437,500 | 0.23% |
| Over $437,500 | **0.60%** (top Zone 1 rate, increased from 0.34% effective July 1, 2023) |

### 14.3 Rate structure — 2025

**Zone 2 (suburbs) MCTMT rate structure**

| Quarterly payroll expense | Rate |
| --- | --- |
| ≤ $312,500 | 0% |
| $312,500.01 to $375,000 | 0.11% |
| $375,000.01 to $437,500 | 0.23% |
| Over $437,500 | **0.34%** |

### 14.4 Payroll interaction

- **MCTMT filing forms** — MCTMT is a separate employer obligation, NOT withheld from employee wages. It is filed on: Form MTA-305 (employers, quarterly). Or via PrompTax for large employers. The employer's MCTMT obligation is in addition to all wages reported on NYS-45. There is no employee-side reporting.  _(Form MTA-305)_

### 14.5 Self-employed coordination

- **Self-employed MCTMT coordination** — Self-employed individuals working in the MCTD also have an MCTMT obligation (Form MTA-6), but that is annual not payroll-based — see `ny-mctmt` and `ny-estimated-tax`.  _(Form MTA-6)_

## 15. Multi-State Allocation — Worked Mechanics

### 15.1 Three patterns

- **Three multi-state allocation patterns** — 1. NYC-resident employee, NY-employer, all work in NYC. Simplest case. Withhold NY state + NYC + (if applicable) PFL. No allocation needed. 2. NY-resident employee, NY-employer, some work outside NY. Apply convenience-of-employer rule (§10). If "convenience" out-of-state, all NY-source. If "necessity," exclude out-of-state days. 3. Non-resident employee, NY-employer, some work in NY some out-of-state. Use Form IT-2104.1 to allocate. Apply convenience-of-employer rule to any out-of-state days that are for convenience (treat as NY days).

### 15.2 Day-counting

- **Day-counting rules** — A "day" worked in NY is any day on which the employee performs services in NY, regardless of duration. Partial days count as full days. Travel days are sourced to the location where work is performed, not departure or arrival point.

### 15.3 Allocation formula

- **Non-resident allocation formula** — NY-source wages = Total wages × (NY workdays / Total workdays). Where: "Total workdays" = total days actually worked in the year (excludes weekends, holidays, vacation, sick days, jury duty). "NY workdays" = days physically present in NY performing services PLUS any "convenience" out-of-state days.

### 15.4 Coordination with NJ and CT

- **NJ/CT coordination and reciprocity** — NJ and CT each operate their own withholding regimes for their residents. An employer who has a NJ or CT resident may be required to: Continue NY state withholding (per convenience rule). ALSO register and withhold for the resident state if the employer has nexus there. Most NY-based small employers without offices in NJ or CT do NOT have nexus in those states and therefore do NOT withhold for those states. The employee is responsible for filing the resident state return and claiming credits. NJ and NY have a reciprocity agreement for NJ residents working in NY only at the request of the NY employer — but in practice, NY's convenience rule overrides reciprocity, so NJ residents working remotely from NJ for a NY employer pay NY tax.

## 16. Worked Examples

### Example 1 — NYC resident with NY employer, all work in NYC

Maria, NYC resident (Manhattan). Employer: tech startup with office in Manhattan. 2025 annual salary: $150,000, paid biweekly ($5,769.23 per pay period). Single, claims 1 allowance on IT-2104. Single on federal W-4 with no adjustments. $200/month pre-tax 401(k) contribution. $150/month pre-tax health insurance. DBL/PFL coverage in place.

**Per-pay-period payroll computation**

| Item | Amount |
| --- | --- |
| Gross wages | $5,769.23 |
| Less: 401(k) pre-tax | ($92.31) (= $200 × 12/26) |
| Less: Health insurance pre-tax | ($69.23) |
| Federal taxable wages | $5,607.69 |
| FICA taxable wages | $5,676.92 (only 401k excluded for FICA; health is excluded for FICA too: $5,607.69) — corrected: $5,607.69 |
| NY taxable wages | $5,607.69 (NY conforms to federal pre-tax 401(k) and health) |
| Federal income tax (single, 2 deps simplified) | ~$880 |
| FICA (6.2% Social Security) | $347.68 |
| Medicare (1.45%) | $81.31 |
| NY state withholding (≈5.5% effective) | $292.21 |
| NYC withholding (≈3.876% top bracket) | $217.32 |
| PFL (0.388% of gross) | $22.38 |
| DBL (employer-paid; up to $0.60/wk; assume biweekly = $1.20) | $1.20 |
| 401(k) | $92.31 |
| Health insurance | $69.23 |
| **Net pay** | ~$3,765.59 |

File NYS-45 reporting Maria's wages, NY state withholding, NYC withholding. Pay UI on first $12,800 of wages (paid in Q1 of the year). Pay MCTMT at 0.60% (Zone 1, NYC) on the quarterly payroll if total quarterly payroll exceeds $437,500.

W-2 Box 1 (federal wages): ~$145,800. W-2 Box 16 (NY wages): ~$145,800. W-2 Box 18 (local wages, NYC): ~$145,800. W-2 Box 14 informational: "NYPFL $354.53" (capped at annual max), "NYSDI $31.20" (if employer deducted full $0.60/wk).

### Example 2 — NY-employer with Texas remote worker (convenience-of-employer rule)

James, Texas resident (Austin), working fully remote from his Austin home. Employer: hedge fund based in NYC (NY State employer). 2025 annual salary: $250,000, paid semi-monthly ($10,416.67 per pay period). Married filing jointly on IT-2104 (claims spouse + 2 kids). Pre-tax 401(k): 15% of gross. Health insurance: $400/month pre-tax. Employer has no Texas office. James works from home for convenience; no client-site requirement.

Convenience-of-employer rule applies. James's home in Austin is not a "bona fide employer office" — no specialized facilities, not the employer's choice of location. All work is for James's convenience. Result: 100% of James's $250,000 wages are NY-source.

**Per-pay-period**

| Item | Amount |
| --- | --- |
| Gross wages | $10,416.67 |
| Less: 401(k) (15%) | ($1,562.50) |
| Less: Health insurance | ($200.00) (semi-monthly portion of $400/mo) |
| NY taxable wages | $8,654.17 |
| NY state withholding (≈6.85% effective for high earner) | $592.81 |
| NYC withholding | **$0** (James is NOT a NYC resident) |
| Yonkers | **$0** (not a Yonkers resident, no Yonkers work) |
| PFL (0.388% of gross) | $40.42 (until $354.53 annual max hit) |
| Texas state withholding | $0 (TX has no PIT) |
| Federal + FICA | (standard) |

Withhold full NY state PIT on $250,000. Do NOT withhold NYC tax (non-resident). Pay MCTMT 0.60% on James's wages (NYC employer, so Zone 1 — NY DTF position is that MCTMT follows the employer's location for remote workers under the convenience rule by analogy). DBL: still required (NY employer with NY-source wages). PFL: still required (NY employer with employee on NY payroll). NJ/TX UI: NY employer with TX-resident remote worker may have triggered Texas UI nexus depending on facts. Texas UI assessment may apply for wages allocated to Texas under the federal "localization of work" test (which differs from NY's convenience rule and would generally find James's work localized in TX, creating dual UI exposure). Consult TX Workforce Commission.

James files NY Form IT-203 (nonresident return) reporting $250,000 NY-source wages. Texas: no PIT return. James pays full NY tax with no offsetting state credit (TX has no PIT, so no credit available). Net result: James pays NY tax as if he lived in NY but receives no benefit of NY residence.

### Example 2 — NY-employer with Texas remote worker (convenience-of-employer rule)

> **AUDIT FLASH POINT:** This is the textbook NY DTF audit profile. Employer should retain documentation that James's remote work is NOT employer-required, in case the employer later wishes to argue exception. In practice, employers default to NY withholding to avoid disputes.

### Example 3 — Multi-state hire mid-year (resident change)

Priya, hired May 1, 2025 by a NY tech employer based in Brooklyn. January-April 2025: lived in NJ, worked elsewhere (different employer). May 1, 2025: hired by NY employer, moved to NYC (Brooklyn). Salary: $180,000/year, biweekly. No pre-tax deductions for simplicity.

1. IT-2104: Required at hire. Priya completes as NYC resident effective May 1, claiming 2 allowances. 2. Federal W-4: Required. 3. WTPA notice: English version provided and signed; retained for 6 years. 4. DBL/PFL: Coverage already in place for employer; Priya covered from hire date for PFL waiting period purposes (eligibility begins after 26 weeks, but contributions start immediately). 5. New-hire reporting: Employer must report Priya to NY State Directory of New Hires within 20 days of hire date (Social Services Law §111-b(4)).

Gross wages: $180,000 / 26 = $6,923.08. Withhold NY state PIT. Withhold NYC PIT (resident). Withhold PFL 0.388% = $26.86.

Reports Priya's wages for May 1 - June 30. UI taxable wages: capped at $12,800 (Priya hits this in approximately first 2 months — wage base is exhausted very quickly at her salary level). NY state and NYC withholding reported.

Reports Priya's full May-Dec wages ($120,000). W-2 issued with Box 16 NY wages = $120,000, Box 18 NYC wages = $120,000. Priya files NY Form IT-201 (full-year NYC resident from May 1) — actually IT-203 as part-year resident from May 1 — reporting NY income only from May 1 onward. Pre-May income (NJ source) excluded. Box 14: "NYPFL $354.53" (Priya hit the cap), "NYSDI" if applicable.

Withholding NY tax on Priya's pre-May (other-employer) wages: not applicable (she had a different employer). Failing to update IT-2104 if Priya later moves to Yonkers: would cause under-withholding of Yonkers surcharge. Treating Priya as NJ resident for any portion of post-May payroll: incorrect; once she's a NYC resident, full NY+NYC withholding applies.

## 17. Audit Flash Point Summary

NY payroll has three audit profiles that account for the majority of DTF and DOL enforcement actions against small employers: 1. AUDIT FLASH POINT — Convenience-of-employer audits. Remote workers for NY employers in low/no-tax states. Trigger: W-2 with NY employer + employee address in FL/TX/TN/NH/SD/WY. Mitigation: document any employer-required out-of-state work; otherwise concede NY-source treatment. 2. AUDIT FLASH POINT — NYC dual-residency challenges. Employee claims non-NYC residence while maintaining NYC apartment. Trigger: W-2 with NYC employer address but employee address out-of-city + IT-203 (nonresident) filing. Mitigation: contemporaneous IT-2104 on file showing claimed residency; written domicile change documentation; day-counting records. 3. AUDIT FLASH POINT — Missed PFL/DBL coverage. Small employers (1-4 employees) without coverage. Trigger: NYS-45 wages reported but no DBL/PFL policy on file with NY Workers' Compensation Board. Mitigation: obtain coverage immediately upon first employee; verify carrier reports to WCB; retain policy declarations. Other secondary flash points: 4. WTPA pay-stub deficiency. Pay stubs missing required information (most commonly: not showing overtime hours/rates for non-exempt employees). Private right of action; class action exposure. 5. Misclassification of contractors as 1099 where ABC test fails. Triggers UI audit + retroactive employment tax assessment + DBL/PFL coverage gap penalties. 6. NYS-1 deposit late. Employers near the $700/$15,000 thresholds frequently miss deposit deadlines, triggering 0.5%/month penalties that compound quickly. 7. MCTMT skipped or wrong zone. Employer in NYC fails to file MTA-305; or files at Zone 2 rate (0.34%) when Zone 1 (0.60%) applies.

## 18. Provenance and Authority

### 18.1 Primary statutory authorities

- **Primary statutory authorities list** — NY Tax Law Article 22 (Personal Income Tax), particularly §§601 (rates), 671 (withholding duty), 685 (penalties). NY Tax Law Article 23 (MCTMT). NYC Administrative Code §11-1701 (NYC PIT). Yonkers Municipal Code §15-200 (Yonkers earnings tax). NY Labor Law Article 5 (§§190-199-a, wages); §195 (notice); §198 (penalties); §191 (frequency); §193 (deductions). NY Labor Law Article 18 (Unemployment Insurance), §§510 et seq. NY Workers' Compensation Law Article 9 (DBL/PFL). NY Codes, Rules and Regulations (20 NYCRR) Parts 132 (allocation), 171 (withholding), 173 (UI).

### 18.2 Administrative guidance

- **Administrative guidance list** — Publication NYS-50 (Employer's Guide to Unemployment Insurance, Wage Reporting, and Withholding Tax) — annually updated; 2025 edition. Publication NYS-50-T-NYS (NY State withholding tables and methods), effective January 1, 2025. Publication NYS-50-T-NYC (NYC withholding tables), effective January 1, 2025. Publication NYS-50-T-Y (Yonkers withholding tables), effective January 1, 2025. TSB-M-06(5)I — bona fide employer office secondary factor test. TSB-M-21(1)I — COVID-19 telework guidance. TSB-M-15(2)C — mandatory e-filing. DTF Form Instructions for IT-2104, IT-2104.1, NYS-45, NYS-1, MTA-305.

### 18.3 Federal scaffolding cross-references

- **Federal scaffolding cross-references list** — IRC §3401 (federal withholding) — followed by NY for FICA-exempt items. IRC §125 (cafeteria plans), §401(k) — NY conforms. Rev. Rul. 87-41 — 20-factor common-law test (followed for NY PIT withholding). Form W-2 Instructions (2025) — Box 14 reporting of NYPFL, NYSDI.

### 18.4 Key case law

- **Key case law list** — Gaied v. NY Tax Appeals Tribunal, 22 N.Y.3d 592 (2014) — statutory residency requires actual residential use of NY abode. Matter of Zelinsky v. NY Tax Appeals Tribunal, 1 N.Y.3d 85 (2003) — upheld convenience-of-employer rule. Hayes v. Comm'r of Tax. & Fin. (various) — IT-203 allocation challenges. In re Edelstein, NY DTA 2019 — work-from-home characterization, post-Zelinsky.

## 19. Circular 230 and Reviewer Sign-off

This skill produces payroll computation worksheets and compliance guidance for a credentialed reviewer (Enrolled Agent, CPA, or attorney admitted in NY) to review and approve before any output is delivered to the taxpayer or relied upon for filing.

### 19.1 Circular 230 disclosure

Output produced using this skill is not a covered opinion under Treasury Department Circular 230. It is technical assistance to a credentialed practitioner who is responsible for:

- Verifying the current-year rates against published DTF, NYC, Yonkers, and Labor Department announcements (rates change annually and mid-year corrections occur).
- Confirming taxpayer-specific facts including residency, work location, and worker classification.
- Signing the relevant returns and assuming professional responsibility.

### 19.2 Conservative defaults

When facts are ambiguous, this skill defaults to the more conservative position:

- Worker classification: presume employee unless ABC test demonstrably satisfied.
- Residency: presume NYC resident if any NYC ties + 183-day proximity.
- Convenience-of-employer: presume "convenience" (NY-source) unless documented employer requirement.
- Wage base: full inclusion unless statutory exemption is clearly established.

### 19.3 What this skill will refuse

- Withholding computations for tax years other than 2025 without explicit rate research.
- Worker classification opinions in industries explicitly carved out (construction, transportation) without referring to the statutory presumption tests.
- Multi-state nexus opinions for employers that may have triggered withholding obligations in states other than NY without state-specific research.
- Self-employment tax computations — these are out of scope (see `us-schedule-c-and-se-computation` and `ny-estimated-tax`).
- Personal income tax return preparation — out of scope (see `ny-income-tax`).

- **Withholding computations for other tax years** — Refuses withholding computations for tax years other than 2025 without explicit rate research.  _(19.3 What this skill will refuse)_
- **Worker classification opinions in carved-out industries** — Refuses worker classification opinions in industries explicitly carved out (construction, transportation) without referring to the statutory presumption tests.  _(19.3 What this skill will refuse)_
- **Multi-state nexus opinions** — Refuses multi-state nexus opinions for employers that may have triggered withholding obligations in states other than NY without state-specific research.  _(19.3 What this skill will refuse)_
- **Self-employment tax computations** — Out of scope — see `us-schedule-c-and-se-computation` and `ny-estimated-tax`.  _(19.3 What this skill will refuse)_
- **Personal income tax return preparation** — Out of scope — see `ny-income-tax`.  _(19.3 What this skill will refuse)_

### 19.4 What this skill produces

- Per-pay-period payroll computations showing all NY withholdings.
- Quarterly NYS-45 reconciliation worksheets.
- Annual W-2 reconciliation against NYS-45 Part C.
- Compliance checklists for IT-2104, WTPA, DBL/PFL coverage.
- Audit flash-point risk assessment for client.
- Reviewer brief summarizing positions taken and supporting authority.

### 19.5 Sign-off

- **Reviewer sign-off requirement** — Every output produced using this skill must be reviewed and signed off by a credentialed reviewer (EA, CPA, or NY-admitted attorney) before being filed or relied upon. The skill is a research and computation aid; it is not a substitute for professional judgment.  _(19.5 Sign-off)_

## 20. Coordination with Other OpenAccountants Skills

- **`us-tax-workflow-base`** (Tier 1) — REQUIRED scaffolding for this skill.
- **`ny-income-tax`** — for the employee-side IT-201 / IT-203 return that reconciles to W-2.
- **`ny-mctmt`** — for full MCTMT computation and Form MTA-305 mechanics.
- **`ny-estimated-tax`** — for the self-employed quarterly estimate (out-of-scope here).
- **`nyc-ubt`** — for NYC self-employed UBT (out of scope; employees only here).
- **`ny-pte-tax-ptet`** — for PTET election that may interact with shareholder/partner payroll.
- **`us-1099-nec-issuance`** — for federal 1099-NEC issuance to contractors (referenced in §12.4).
- **`us-s-corp-election-decision`** — if employer is a single-shareholder S corp, reasonable compensation analysis interacts with NY payroll.
- **`us-ny-return-assembly`** — final orchestrator that assembles the federal + NY package, of which W-2 outputs from this skill are a component.

---

*End of ny-payroll skill v0.1, last updated 2025-11-15. Pending verification by NY-credentialed reviewer.*

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).
