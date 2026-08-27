---
name: az-payroll
description: Tier 2 Arizona content skill for employer payroll compliance covering tax year 2025. Includes the 2.5% flat PIT (phased down from 4.5% over 2022-2023), A-4 state W-4 expressed as percentage of federal withholding (0.5-3.5% options), A1-QRT quarterly withholding, A1-R annual reconciliation, AZ UI wage base $8,000 with rates 0.07-15.6%, Earned Paid Sick Time Proposition 206 mandate (1 hour per 30 hours worked statewide), and a 7-factor worker classification test.
jurisdiction: US-AZ
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AZ Payroll

## 1. Scope

This skill covers Arizona-specific employer payroll obligations for tax year 2025 for:

- Single-member LLCs, sole proprietors, partnerships, S-corporations, and C-corporations with employees performing services in Arizona
- Out-of-state employers with at least one Arizona-resident employee or with employees physically performing services in Arizona
- Employers electing voluntary withholding for Arizona-resident employees working entirely in another state

In scope:

- Arizona state personal income tax (PIT) withholding under Title 43, Chapter 4, Arizona Revised Statutes (A.R.S. §§ 43-401 et seq.)
- Form A-4 (Employee's Arizona Withholding Election)
- Form A1-QRT (Arizona Quarterly Withholding Tax Return)
- Form A1-R (Arizona Annual Withholding Reconciliation Return)
- Form A1-APR (Annual Payment Withholding Tax Return) — qualifying low-volume filers only
- Arizona Unemployment Insurance (AZ UI) under A.R.S. Title 23, Chapter 4 — wage base, rates, Form UC-018 (Unemployment Tax and Wage Report)
- Earned Paid Sick Time under the Fair Wages and Healthy Families Act (Proposition 206, 2016), codified at A.R.S. §§ 23-371 through 23-381
- Worker classification (employee vs independent contractor) under Arizona's 7-factor test in A.R.S. § 23-902(D) and § 23-1601
- Pre-tax cafeteria plan and 401(k) treatment for Arizona PIT and AZ UI purposes
- Final pay rules under A.R.S. § 23-353

Out of scope:

- Federal payroll obligations (Forms 941, 940, 944, W-2, W-3, FUTA) — defer to federal payroll skills
- Arizona Transaction Privilege Tax (TPT) — see `az-transaction-privilege-tax.md`
- Arizona individual income tax return preparation — see `az-income-tax.md`
- City of Phoenix, Tucson, Flagstaff, or Tempe minimum-wage local ordinances beyond Earned Paid Sick Time interaction
- Public-employer compliance (ASRS, PSPRS contributions)
- Workers' compensation insurance — Industrial Commission of Arizona requirements not addressed
- Multistate apportionment of compensation under reciprocal agreements (Arizona has none active for PIT in 2025)
- Tribal-land employment, federal contractor wage-determinations, and Service Contract Act requirements
- Equity compensation withholding (ISO, NSO, RSU, ESPP) — Arizona generally conforms to federal timing but reviewer must confirm

This skill MUST be loaded alongside `us-tax-workflow-base` v0.2 or later. Federal payroll content is assumed to be handled by a federal payroll skill.

## 2. Arizona Personal Income Tax — 2.5% Flat Rate

### 2.1 Statutory authority and rate history

- **Flat rate effective date** — For tax year 2023 and forward, Arizona moved to a single flat rate of 2.5% on Arizona taxable income for all filing statuses. Senate Bill 1828 (55th Legislature, 2nd Regular Session, 2021) enacted the phase-down originally scheduled over four years, but revenue triggers were met early and the flat 2.5% rate took full effect in tax year 2023.  _(A.R.S. § 43-1011)_

**Phase-down timeline**  _(A.R.S. § 43-1011)_

| Tax year | Top marginal rate | Structure |
| --- | --- | --- |
| 2021 and earlier | 4.50% | Four-bracket progressive |
| 2022 | 2.98% (top) / 2.55% (low) | Two-bracket transitional |
| 2023 | 2.50% | Flat rate |
| 2024 | 2.50% | Flat rate |
| 2025 | 2.50% | Flat rate (current) |

There is no separate withholding rate table to look up wages against. The flat structure simplifies employer withholding considerably compared to pre-2023 Arizona.

### 2.2 Supplemental wage withholding

- **Supplemental wage rate** — Arizona does not publish a separate supplemental wage withholding rate. For bonuses, commissions, severance, retroactive pay increases, accumulated vacation payouts, prizes, and other supplemental compensation paid to Arizona-source employees, the employer applies the employee's elected A-4 percentage to the supplemental payment, the same as for regular wages.

In practice many payroll systems will default the supplemental wage rate to 2.5% (the flat PIT rate) when the employee's A-4 election is silent or when an aggregate method would distort withholding. Where the employee's A-4 election is 0% (zero withholding), the employer withholds 0% on supplemental wages absent an alternative directive from the employee.

Reviewer note: confirm the payroll provider's configuration for supplemental wage handling. Gusto, ADP, Paychex, Rippling, and QuickBooks each handle Arizona supplemental wages slightly differently and the default may need to be adjusted.

### 2.3 Wages subject to Arizona withholding

- **Compensation subject to withholding** — A.R.S. § 43-401(A) requires Arizona income tax withholding from compensation paid to employees for services performed in Arizona. Compensation includes: Salary, wages, commissions, bonuses; Tips reported to the employer under IRC § 6053; Taxable fringe benefits (personal use of employer vehicle, group-term life insurance over $50,000); Sick pay paid by the employer; Third-party sick pay where the employer has accepted withholding responsibility; Severance pay; Deferred compensation when constructively received (and when not previously taxed as Arizona-source)  _(A.R.S. § 43-401(A))_
- **Compensation excluded from withholding** — Compensation excluded from Arizona withholding: Section 125 cafeteria plan elections (medical, dental, vision, dependent care FSA, HSA via cafeteria plan) — see §2.8 below; 401(k), 403(b), 457(b) traditional elective deferrals (not Roth) — Arizona conforms to federal treatment; Qualified transportation fringe (transit pass, qualified parking, vanpool) up to the federal monthly limit; Employer contributions to a qualified retirement plan; Workers' compensation benefits; Domestic-service wages paid in a private home (not subject to mandatory withholding but voluntary withholding permitted); Wages paid to a non-resident employee performing services entirely outside Arizona  _(A.R.S. § 43-401(A))_

### 2.4 Arizona-source wages — multistate employees

- **Allocation methods** — For an employee who performs services partly inside and partly outside Arizona, A.R.S. § 43-401 and Arizona Department of Revenue (ADOR) guidance require withholding on the Arizona-source portion. Arizona-source wages are generally determined by: 1. Workdays method (preferred): Arizona-source wages = total wages × (Arizona workdays / total workdays). A workday is any day on which the employee performs services for the employer, regardless of hours. 2. Time-tracking method: for highly mobile employees, an hours-based allocation is acceptable if tracked contemporaneously.  _(A.R.S. § 43-401)_
- **Arizona resident working entirely outside AZ** — For an Arizona resident performing services entirely in another state (e.g., resident commuter to California or remote worker temporarily in Nevada), Arizona does NOT mandate Arizona withholding, but the employee remains liable for Arizona PIT on worldwide income. The employer may offer voluntary Arizona withholding by employee request via Form A-4V (Voluntary Withholding Election for Arizona Resident Working Outside Arizona).

Arizona has no current reciprocal withholding agreements with neighboring states (California, Nevada, Utah, New Mexico, Colorado) for tax year 2025. Each multistate employee situation must be analyzed under both the work-state and resident-state rules.

## 3. Form A-4 — Employee's Arizona Withholding Election

### 3.1 The percentage method (Arizona's distinguishing feature)

- **AUDIT FLASH POINT — A-4 percentage method confusion** — Arizona's A-4 is fundamentally different from the federal Form W-4 and from most other states' withholding certificates. Arizona does NOT use a wage-bracket method, does NOT use a percentage method based on Arizona-only taxable wages, and does NOT use allowances. Instead, the employee elects a percentage of their federal taxable wages (after federal pre-tax deductions but before federal income tax) to be withheld for Arizona PIT. This is a frequent source of error. Out-of-state payroll administrators routinely: - Apply the A-4 percentage to Arizona gross wages instead of federal taxable wages - Treat the A-4 percentage as an allowance number rather than a rate - Default new hires to 2.7% (the pre-2023 default) instead of the current 2.0% default - Apply the percentage to wages after Arizona-specific subtractions The mechanically correct approach: take the employee's federal taxable wages for the pay period (Box 1 W-2 wages equivalent for the period, i.e., gross wages minus §125 cafeteria plan deductions minus traditional 401(k)/403(b)/457 elective deferrals minus other federal pre-tax items, but BEFORE federal income tax withholding is computed) and multiply by the A-4 elected percentage. The result is Arizona PIT withholding for that pay period.

### 3.2 Available A-4 percentage elections (2025)

**A-4 election options 2025**

| Election | Percentage of federal taxable wages |
| --- | --- |
| 0.5% | Minimum statutory election |
| 1.0% |  |
| 1.5% |  |
| 2.0% | **Default for employees who do not submit an A-4** |
| 2.5% | Matches the flat PIT rate |
| 3.0% |  |
| 3.5% | Maximum statutory election |
| Zero | Available only if the employee qualifies (see §3.4) |

The form was updated by ADOR in late 2022 to reflect the 2.5% flat tax. The 2022-and-earlier A-4 form with options ranging from 0.8% to 5.1% is obsolete. Employers using outdated forms should reissue current-year A-4s during the next open enrollment or annually as a refresh.

### 3.3 Default rate for missing A-4

- **Default 2.0% withholding** — A.R.S. § 43-401(G) and ADOR Form A-4 instructions provide that if a newly hired employee fails to submit an A-4 within their first pay period, the employer must withhold at the default percentage of 2.0% of the employee's federal taxable wages.  _(A.R.S. § 43-401(G))_

The employer does NOT use 2.5% as a default. The 2.0% default rate is a deliberate ADOR choice intended to give the employee room to adjust upward via Form A-4 if their actual liability exceeds the default.

The employee can submit an A-4 at any time; the new election is effective for the first pay period beginning on or after the employer's receipt of the form. Employers are not required to make the change retroactively to the start of the year.

### 3.4 Zero withholding election

- **Zero withholding qualification** — An employee may elect zero Arizona PIT withholding on Form A-4 only if the employee: 1. Had no Arizona income tax liability in the prior tax year, AND 2. Expects to have no Arizona income tax liability in the current tax year
- **Certification and revision requirement** — The employee certifies these conditions by checking the Zero Withholding box on the A-4 and signing under penalty of perjury. If the employee's circumstances change such that they will owe Arizona tax, the employee must submit a revised A-4 within ten days.

The employer accepts a Zero Withholding A-4 at face value and is not required to verify the employee's claim. The employer is, however, required to forward to ADOR any A-4 claiming Zero Withholding when requested by ADOR.

### 3.5 Voluntary Arizona withholding for AZ residents working out of state — Form A-4V

- **Voluntary withholding for AZ residents working out-of-state** — A.R.S. § 43-403 allows an Arizona resident performing services in another state to request voluntary Arizona withholding from the employer using Form A-4V. The employer is not required to honor the request, but if accepted, the employer remits the withheld amounts on Form A1-QRT the same as for mandatory withholding. This is increasingly common in 2025 for remote workers who have moved out of Arizona temporarily but remain Arizona residents.  _(A.R.S. § 43-403)_

### 3.6 A-4 retention

- **Retention period** — Employers must retain each employee's A-4 for at least four years after the last date the form is in effect, per ADOR Publication 701. ADOR may request submission of any A-4 at any time during the retention period.  _(ADOR Publication 701)_

### 3.7 Worked walkthrough — A-4 mechanics

Employee Sarah is a software developer at an Arizona LLC. Her bi-weekly gross wages are $4,000. She elects 0.5% on her A-4. Her pre-tax deductions per pay period are:

- §125 medical premium: $150
- §125 dependent care FSA: $200
- Traditional 401(k) elective deferral: $400

Sarah's federal taxable wages per pay period = $4,000 − $150 − $200 − $400 = $3,250.

Arizona PIT withholding = $3,250 × 0.5% = $16.25 per pay period.

If Sarah had not submitted an A-4, the default 2.0% would apply: $3,250 × 2.0% = $65.00 per pay period.

If Sarah's federal taxable wages had instead been computed wrong (e.g., the payroll administrator multiplied $4,000 × 0.5% = $20.00 against gross wages), the error is small per pay period but compounds across 26 pay periods to $97.50 of over-withholding annually. For higher earners with substantial pre-tax deductions, the error can run into the hundreds of dollars per year, and at the 3.5% election, well over a thousand dollars.

## 4. Form A1-QRT — Quarterly Withholding Tax Return

### 4.1 Who files A1-QRT

- **Filing requirement** — A.R.S. § 43-411 requires every employer with Arizona withholding obligations to file Form A1-QRT for each calendar quarter, even if no tax was withheld during the quarter (a zero return). Exception: employers qualifying as Annual filers (see §5.2) file Form A1-APR instead of quarterly A1-QRTs.  _(A.R.S. § 43-411)_

### 4.2 Quarterly due dates

**A1-QRT due dates**

| Quarter | Period covered | Due date |
| --- | --- | --- |
| Q1 | January 1 – March 31 | April 30 |
| Q2 | April 1 – June 30 | July 31 |
| Q3 | July 1 – September 30 | October 31 |
| Q4 | October 1 – December 31 | January 31 (next year) |

- **Weekend/holiday rule** — If the due date falls on a Saturday, Sunday, or Arizona legal holiday, the return is due the next business day.

### 4.3 Deposit frequencies — quarterly, monthly, or next-day

**Deposit frequency schedule**

| Average Q withholding | Deposit frequency |
| --- | --- |
| Less than $1,500 per quarter | Quarterly (pay with A1-QRT) |
| $1,500 – $50,000 per quarter | Monthly (15th of following month) |
| More than $50,000 per quarter | Semi-weekly under federal rules — Arizona generally aligns to federal Form 941 deposit schedule |
| Single tax liability of $500+ in a quarter | One-banking-day deposit (next business day) for any payday triggering $500+ in undeposited liability |

ADOR assigns each employer a deposit frequency based on the employer's average quarterly Arizona withholding liability. The frequency for the current calendar year is determined by the prior calendar year's lookback period (July 1 of two years prior through June 30 of the prior year).

Newly registered employers default to quarterly deposit frequency unless their first-quarter liability triggers a faster schedule.

ADOR sends a notice each November communicating the deposit frequency for the upcoming calendar year. Employers must self-monitor for accuracy.

### 4.4 Method of payment

- **Electronic payment threshold** — All deposits must be made electronically via AZTaxes.gov when annual Arizona withholding tax liability is $500 or more, per A.R.S. § 42-1129. Employers below that threshold may still file and pay electronically (and most do). Paper Form A1-QRT is technically permitted only for the very smallest employers.  _(A.R.S. § 42-1129)_

### 4.5 A1-QRT line structure

- **A1-QRT lines** — The A1-QRT collects: 1. Total Arizona wages paid this quarter; 2. Total Arizona PIT withheld this quarter; 3. Less: payments made during the quarter (monthly or weekly deposits); 4. Net tax due (or refund); 5. Penalty (if applicable); 6. Interest (if applicable); 7. Total balance due

Total Arizona wages on line 1 means wages subject to Arizona withholding, NOT gross wages. For an employee with $4,000 gross wages and $750 of §125 plus 401(k) pre-tax deductions, the Arizona-wages figure is $3,250 — the federal taxable wages base.

### 4.6 Penalty exposure

- **Late filing penalty** — 4.5% of the tax required to be shown on the return per month or fraction (max 25%)  _(A.R.S. § 42-1125)_
- **Late payment penalty** — 0.5% per month or fraction (max 10%)  _(A.R.S. § 42-1125)_
- **Failure to e-file penalty** — 5% of the tax shown, minimum $25  _(A.R.S. § 42-1125)_
- **Interest** — At the federal short-term rate plus 3%, compounded annually  _(A.R.S. § 42-1123)_

ADOR generally abates first-time penalties on reasonable-cause request, but the employer must affirmatively request abatement and provide documentation.

### 4.7 Amended A1-QRT

- **Amendment process** — To correct a previously filed A1-QRT, the employer files an amended A1-QRT for the same quarter, marking the Amended Return box at the top. The amended return reports CORRECTED totals (not net change). Any additional tax due is paid with the amended return; any overpayment can be applied to the next quarter's A1-QRT or requested as a refund.

## 5. Form A1-R — Annual Withholding Reconciliation

### 5.1 Purpose and due date

- **A1-R purpose and due date** — Form A1-R is the annual reconciliation between Arizona PIT withholding reported quarterly on A1-QRT and the Arizona PIT shown on the W-2 forms issued to employees. A1-R is due on or before January 31 following the close of the calendar year (no extension available; this matches the federal W-2 due date).
- **W-2 filing requirement** — Arizona requires W-2 Copy 1 (or electronic equivalent) to be submitted with the A1-R when Arizona PIT was withheld. The W-2 file must conform to SSA's EFW2 format with Arizona-specific RS records for state wages and tax.

### 5.2 A1-APR — Annual Payment Reconciliation (small employer election)

- **A1-APR eligibility and rules** — Employers with average quarterly Arizona PIT withholding of less than $1,500 AND who do not anticipate exceeding $1,500 in any quarter of the year may file Form A1-APR instead of quarterly A1-QRTs. A1-APR is due January 31, combines the four quarters into one annual return, and is filed with the employer's W-2s. The employer is still subject to Arizona deposit-frequency rules; A1-APR is a filing simplification, not a payment-timing change.

### 5.3 A1-WP — Payment Voucher

- **A1-WP** — When a monthly or semi-weekly depositor makes a deposit between A1-QRT filings, the deposit is accompanied by Form A1-WP (Payment Voucher) — though electronic depositors do not use a paper voucher. The A1-WP designates the quarter to which the deposit relates.

### 5.4 Mismatch resolution

- **Mismatch outcome** — If A1-R reveals a mismatch between cumulative A1-QRT remittances and W-2 totals, ADOR will assess additional tax (if W-2 totals exceed remittances) or issue a refund (if remittances exceed W-2 totals).

Common mismatch sources:

- Late-quarter bonus W-2s issued through year-end payroll runs without a corresponding A1-QRT update
- W-2c (corrected) wage corrections issued after January 31
- Year-end true-ups of taxable group-term life insurance over $50,000
- Reclassified independent contractors who become reclassified as employees after the quarter ended

Reviewer note: reconcile A1-QRT cumulative totals to projected W-2 totals BEFORE the December payroll run, and resolve variances with a corrected A1-QRT for Q4 if needed.

## 6. Arizona Unemployment Insurance (AZ UI)

### 6.1 Administration and authority

- **UI administration** — AZ UI is administered by the Arizona Department of Economic Security (DES) under A.R.S. Title 23, Chapter 4. The Unemployment Insurance Tax program registers employers, assigns tax rates, collects contributions on Form UC-018 (Unemployment Tax and Wage Report), and pays benefits to eligible separated workers.  _(A.R.S. Title 23, Chapter 4)_

### 6.2 Wage base — $8,000 (one of the lowest in the nation)

- **AZ UI taxable wage base 2025** — $8,000 per employee per year  _(A.R.S. § 23-622.01)_

This is among the lowest taxable wage bases in the United States — many states have wage bases of $14,000 to $50,000+. The $8,000 base means most Arizona employees become wage-base-exhausted (no further UI tax owed) within the first three to four months of the year.

There has been periodic legislative interest in raising the base (a 2023 bill proposed $12,000 by 2026 but did not pass) but for 2025 the base remains $8,000.

Wage base is per-employee, per-year, per-employer. If an employee changes employers mid-year, the new employer restarts the $8,000 base (subject to predecessor-successor rules for asset transfers under A.R.S. § 23-733).

### 6.3 Contribution rates for 2025

- **AZ UI rate range 2025** — minimum of 0.07% to a maximum of 15.6% of the taxable wage base  _(A.R.S. § 23-732)_

**Contribution rates by employer type 2025**  _(A.R.S. § 23-732)_

| Employer type | 2025 rate |
| --- | --- |
| Newly registered (no experience) | 2.00% for the first 2 calendar years (then experience rate) |
| Construction industry, newly registered | 5.40% for the first 2 calendar years |
| Minimum-rated experienced employer | 0.07% |
| Maximum-rated experienced employer | 15.60% |
| Average experienced rate | approximately 1.7% (2025) |

- **Experience rating computation** — Experience rating: the employer's rate is based on the ratio of UI benefit charges to the employer's experience-rating account to the employer's total taxable payroll, computed over the prior three completed fiscal years (July 1 – June 30 each).
- **Rate determination notice and protest** — DES sends a Determination of Unemployment Insurance Tax Rate (Form UB-006) each December for the upcoming calendar year. The employer has 15 days to protest the rate in writing under A.R.S. § 23-732(K).  _(A.R.S. § 23-732(K))_

### 6.4 UC-018 Quarterly Filing

- **UC-018 due date and contents** — Form UC-018 is due on the same schedule as A1-QRT — last day of the month following the quarter end. The UC-018 reports: Total wages paid this quarter (gross wages, before any deductions); Excess wages (amounts above the $8,000-per-employee cap); Taxable wages (total minus excess); Contributions owed (taxable wages × employer's UI rate); Job training tax (see §6.5); Total due
- **Electronic filing requirement** — Filing and payment are mandatory online via DES's Tax and Wage System (TWS) for all employers with 5 or more employees, and de facto required for everyone given the lack of paper-form support.

### 6.5 Job Training Tax

- **Job Training Tax rate and applicability** — Under A.R.S. § 23-769, Arizona imposes a 0.10% Job Training Tax on the same taxable wage base ($8,000) as the UI contribution, for employers with a positive experience-rating reserve account. New employers and employers with negative reserves do NOT pay the Job Training Tax. The tax appears on the UC-018 as a separate line and is remitted with the UI contribution.  _(A.R.S. § 23-769)_

### 6.6 Wages subject to AZ UI

- **UI wage treatment differences** — AZ UI taxable wages have a broader definition than Arizona PIT withholding wages. Notably: §125 cafeteria plan elections — EXCLUDED from AZ UI taxable wages (same as PIT); Traditional 401(k) elective deferrals — INCLUDED in AZ UI taxable wages (different from PIT — see §2.8 below). AZ UI follows FUTA (Form 940) treatment, not federal income tax treatment; §132 qualified transportation fringe — EXCLUDED from AZ UI to the federal monthly limit; HSA employer contributions — EXCLUDED from AZ UI; HSA employee pre-tax contributions via cafeteria plan — EXCLUDED from AZ UI; Group-term life insurance over $50,000 — INCLUDED in AZ UI (matches FUTA)

This divergence between PIT-withholding wages and UI wages is a common error source. A typical mid-career employee with $90,000 in gross wages, $5,000 of §125 cafeteria plan elections, and $10,000 of traditional 401(k) deferral has:

- Federal taxable wages: $90,000 − $5,000 − $10,000 = $75,000 (basis for PIT withholding)
- AZ UI taxable wages (first-year wages capped at $8,000): $90,000 − $5,000 = $85,000 gross subject to UI rules but capped at $8,000 (i.e., only the first $8,000 of UI-subject wages are taxable)
- Federal Social Security wages: $90,000 − $5,000 = $85,000 (then capped at FICA base)

### 6.7 New-employer registration

- **Registration timeline** — A new Arizona employer must register with DES within 20 days of the first payroll under A.R.S. § 23-722(B). Registration is online at the AZ Job Connection portal. DES issues an Arizona Employer Account Number (UI account number) within 7-10 business days. The same registration covers PIT withholding registration with ADOR if completed through the joint AZTaxes.gov portal.  _(A.R.S. § 23-722(B))_

### 6.8 Voluntary contributions

- **Voluntary contribution to lower UI rate** — A.R.S. § 23-731 permits an employer to make a voluntary contribution to its experience-rating reserve account on or before January 31 to lower its assigned UI tax rate for the year. This is sometimes economically rational for employers near a tier break — confirm that the voluntary contribution's cost is less than the contribution-rate savings on projected payroll.  _(A.R.S. § 23-731)_

## 7. Earned Paid Sick Time (Proposition 206)

### 7.1 Statutory framework

The Fair Wages and Healthy Families Act (Proposition 206), approved by Arizona voters in November 2016 and effective July 1, 2017, mandates earned paid sick time for nearly every employee in Arizona, regardless of employer size, industry, or full-time/part-time status. Compliance is enforced by the Industrial Commission of Arizona Labor Department.

Common compliance failures:
  - Employers exclude part-time, seasonal, or temporary workers (Proposition 206 covers them)
  - Employers fail to display the required workplace notice
  - Employers fail to provide the legally required information on each paystub (accrual rate, balance, used)
  - Employers attempt to substitute existing PTO without confirming the existing PTO meets ALL Proposition 206 requirements (accrual rate, carryover, usage rules, retaliation protections)
  - Employers retaliate against employees who use earned paid sick time

Proposition 206 penalties (A.R.S. § 23-364) include treble damages on unpaid sick time, $250 per violation per worker per day, attorney fees, and rescission of business licenses for willful repeat violations. The look-back period is 3 years.

### 7.2 Accrual rate

- **Accrual rate** — A.R.S. § 23-372(A) requires employers to provide earned paid sick time at a rate of at least 1 hour of paid sick time per 30 hours worked.  _(A.R.S. § 23-372(A))_

### 7.3 Annual usage cap

**Annual usage cap by employer size**

| Employer size (employees nationwide) | Annual usage / accrual cap |
| --- | --- |
| 15 or more employees | 40 hours per year |
| Fewer than 15 employees | 24 hours per year |

- **Cap applies to usage, doubles as accrual cap** — The cap is on USAGE per year, not on lifetime accrual. The annual cap also doubles as the annual accrual cap — i.e., an employee is not required to accrue beyond the cap during the year (though employers may permit it).

### 7.4 Carryover

- **Carryover and payout option** — Unused earned paid sick time carries over from one year to the next, subject to the annual usage cap remaining in effect. The employer may, in lieu of carryover, pay out unused balance at year-end at the employee's regular hourly rate (this is permissive, not required).

### 7.5 Front-loading

- **Front-loading option** — An employer may front-load the full annual entitlement (40 hours or 24 hours depending on size) at the start of the benefit year and avoid accrual tracking. Front-loaded sick time still must comply with all usage and carryover rules unless paid out.

### 7.6 Permitted uses

- **Permitted uses of sick time** — Earned paid sick time may be used for: Employee's own physical or mental illness, injury, health condition, diagnostic visit, or preventive care; Care for a family member with the same; Closure of the employee's place of business or child's school by public-official order due to public-health emergency; Absence necessary due to domestic violence, sexual violence, abuse, or stalking against the employee or family member
- **Family member** — "Family member" is defined broadly under A.R.S. § 23-371(8) to include child (regardless of age), parent, spouse or registered domestic partner, grandparent, grandchild, sibling, and any other individual whose close association with the employee is the equivalent of a family relationship.  _(A.R.S. § 23-371(8))_

### 7.7 Notice and recordkeeping

- **Employer notice/recordkeeping obligations** — Employers must: Provide written notice to employees of their Proposition 206 rights, on hire and via paystub/wage statement each pay period; Display the Industrial Commission's workplace poster (English and Spanish) in a conspicuous location; Track each employee's accrual, usage, and carryover for at least 4 years; On each wage statement: show the employee's available earned-paid-sick-time balance, the amount used in the pay period, and the pay paid for it

### 7.8 Existing PTO substitution

- **PTO substitution requirements** — An employer with an existing paid time off (PTO) policy may use that PTO to satisfy Proposition 206 IF the PTO policy: Provides accrual at a rate at least as generous as 1 per 30 hours; Allows use for all the same purposes (including domestic violence and public-health closure); Permits use in the same minimum increments; Allows the same carryover or annual payout; Includes the same retaliation and confidentiality protections

A single-bucket PTO that allows "any reason" generally satisfies Proposition 206 if accrual meets the threshold. A PTO that requires advance notice or doctor's notes more stringent than Proposition 206 allows does NOT satisfy.

## 8. Pre-Tax Cafeteria Plans and 401(k) Treatment

**Benefit treatment table**

| Benefit | Federal income tax | AZ PIT withholding | Federal FICA | AZ UI |
| --- | --- | --- | --- | --- |
| §125 cafeteria plan medical/dental/vision premium | Exempt | Exempt | Exempt | Exempt |
| §125 dependent care FSA | Exempt | Exempt | Exempt | Exempt |
| §125 health FSA | Exempt | Exempt | Exempt | Exempt |
| HSA pre-tax contribution via §125 | Exempt | Exempt | Exempt | Exempt |
| HSA post-tax employee contribution | Deductible by employee | Same | Taxable | Taxable |
| §132 qualified parking (≤ federal limit) | Exempt | Exempt | Exempt | Exempt |
| §132 transit/vanpool (≤ federal limit) | Exempt | Exempt | Exempt | Exempt |
| Traditional 401(k) elective deferral | Exempt | **Exempt** | Taxable | **Taxable** |
| Roth 401(k) elective deferral | Taxable | Taxable | Taxable | Taxable |
| Employer 401(k) match | Exempt (no W-2 inclusion) | Exempt | Exempt (no FICA) | Exempt |
| Group-term life ≤ $50,000 | Exempt | Exempt | Exempt | Exempt |
| Group-term life > $50,000 (imputed) | Taxable | Taxable | Taxable | Taxable |
| Adoption assistance (≤ §137 limit) | Exempt | Exempt | Taxable | Taxable |
| Educational assistance (≤ §127 $5,250) | Exempt | Exempt | Exempt | Exempt |
| Personal use of employer vehicle | Taxable | Taxable | Taxable | Taxable |

- **Key divergence note** — Arizona conforms to federal Internal Revenue Code treatment for pre-tax employee benefits, but with the divergence between PIT and UI noted above. The key divergence between PIT withholding and UI wages is the treatment of traditional 401(k): exempt from PIT withholding but included in UI wages (subject to the $8,000 cap).

## 9. Worker Classification — Arizona's 7-Factor Test

### 9.1 Why classification matters

- **Misclassification exposure** — Misclassification of employees as independent contractors exposes the employer to: Back AZ PIT withholding plus penalties under A.R.S. § 42-1125; Back AZ UI contributions plus penalties under A.R.S. § 23-738; Federal liability under IRC §§ 3101, 3111, 3402, 3403, 3509; Workers' compensation back-premiums and Industrial Commission penalties; Unpaid minimum wage and overtime exposure under the Arizona Minimum Wage Act and the FLSA; Unpaid earned paid sick time under Proposition 206; ERISA exposure if benefits should have been offered  _(A.R.S. § 42-1125; A.R.S. § 23-738)_
- **Arizona 7-factor test distinct from federal** — Arizona uses a 7-factor test under A.R.S. § 23-902(D) and § 23-1601 for state-employment-tax purposes, distinct from (but overlapping with) the federal common-law test used by the IRS.  _(A.R.S. § 23-902(D), § 23-1601)_

### 9.2 The 7 factors

- **7-factor test and DIBS presumption** — A worker is presumed to be an INDEPENDENT CONTRACTOR (not an employee) under Arizona law if the worker and the engaging business have signed a Declaration of Independent Business Status (DIBS) under A.R.S. § 23-1601, and the 7 factors are met: 1. No requirement to be at any specific business location — the worker is not restricted to operating from the engager's location and may work from the worker's own location or anywhere chosen; 2. Worker is free to provide same/similar services to others — including direct competitors of the engaging business; 3. Worker is free to accept or decline projects — without consequence to ongoing engagements; 4. Worker provides own tools and equipment — or, when tools must be standardized to industry practice, the worker is not required to use those specifically supplied by the engager; 5. Worker has authority to hire and fire assistants — and is responsible for compensating them; 6. Worker bears risk of profit and loss — the worker is not paid hourly without consideration of project outcome; 7. Worker is not provided with employee-style benefits or training — such as paid time off, health insurance, retirement contributions, or company-paid training programs  _(A.R.S. § 23-1601)_
- **DIBS presumption scope** — A signed DIBS plus genuine satisfaction of the 7 factors creates a rebuttable presumption of contractor status for Arizona purposes. The DIBS does NOT bind the IRS or other federal agencies.

### 9.3 Common misclassification patterns

The following arrangements typically FAIL the 7-factor test:

- Required to work specific hours at the engager's office
- Required to wear company uniform or branded apparel
- Paid hourly with no project deliverable
- Provided with company laptop, phone, and email address
- Restricted from working for competitors (covenant not to compete during engagement)
- Long engagement with one client (more than 12 months at full-time hours)
- Performance reviewed by engager's supervisor
- Trained in engager's specific methodology

The following arrangements typically SUPPORT contractor status:

- Project-based fee, not hourly
- Worker has multiple concurrent clients
- Worker has own business entity (LLC, S-corp), business license, business insurance
- Worker provides own laptop, software, tools
- Worker has own marketing presence
- Worker bills via invoice and the engager issues Form 1099-NEC
- Worker carries own workers' comp or general liability coverage

### 9.4 Behavioral-control checklist

Beyond the 7 factors, Arizona courts and DES auditors examine behavioral control. The more the engager dictates HOW the work is done (rather than just the result), the more likely the worker is an employee.

## 10. Final Pay Rules

### 10.1 Statutory rule

**Final wage deadlines**  _(A.R.S. § 23-353)_

| Situation | Final-pay deadline |
| --- | --- |
| Employer discharges employee | Within 7 working days OR by end of next regular pay period, whichever is sooner |
| Employee resigns voluntarily | Next regular payday |

- **Working days** — "Working days" excludes Saturdays, Sundays, and holidays observed by the employer.  _(A.R.S. § 23-353)_

### 10.2 What must be paid

- **Final pay components** — Final pay must include: All earned wages through the last day worked; All accrued, unused vacation IF the employer's written policy provides for payout at separation (Arizona does NOT mandate vacation payout in the absence of a policy); All accrued, unused earned paid sick time — Arizona does NOT mandate payout of unused sick time under Proposition 206; Any earned bonuses or commissions that are payable per the employer's compensation plan; Reimbursement of all approved business expenses outstanding

### 10.3 Penalties for late final pay

- **Treble damages** — A.R.S. § 23-355 imposes treble damages on unpaid final wages. The employer can be liable for 3× the unpaid amount, plus the employee's attorney fees. This is among the most severe wage-payment penalty regimes in the United States.  _(A.R.S. § 23-355)_

### 10.4 Form of payment

- **Final pay payment method** — Final pay may be paid by direct deposit IF the employee had previously authorized direct deposit and the employer can credit the account by the deadline. Otherwise, payment by paper check at the employee's last known address (or in-person pickup) is required.

## 11. Worked Examples

### 11.1 Example A — Arizona employer, all employees in Arizona

**Facts:**

- Desert Sun Software LLC, a Phoenix-based SMLLC disregarded for federal tax, with 8 full-time W-2 employees, all working in Arizona
- 2025 total Arizona payroll: $880,000
- All 8 employees have submitted A-4 forms electing 2.5%
- Average §125 cafeteria plan elections per employee: $4,800/year
- Average traditional 401(k) deferrals per employee: $8,000/year
- Desert Sun is in its third calendar year of business; DES assigned a 2025 UI rate of 1.40% based on experience rating; Job Training Tax 0.10% applies
- Desert Sun's average quarterly Arizona PIT withholding has been approximately $5,100, putting it on monthly deposit schedule

**Per-employee 2025 PIT withholding:**

- Average gross wages per employee: $110,000
- Federal taxable wages per employee: $110,000 − $4,800 (§125) − $8,000 (401(k)) = $97,200
- A-4 rate: 2.5%
- Annual AZ PIT withheld per employee: $97,200 × 2.5% = $2,430
- Total annual AZ PIT withholding: $2,430 × 8 = $19,440

**Per-employee 2025 UI:**

- UI taxable wages per employee (after §125 exclusion, before $8,000 cap): $110,000 − $4,800 = $105,200, then capped at $8,000
- Wage-base-exhausted per employee: $8,000
- UI contribution: $8,000 × 1.40% = $112.00 per employee
- Job Training Tax: $8,000 × 0.10% = $8.00 per employee
- Total per-employee UI burden: $120.00
- Total annual AZ UI + JTT: $120 × 8 = $960

**Filing calendar 2025:**

- A1-QRT Q1: due April 30, 2025
- A1-QRT Q2: due July 31, 2025
- A1-QRT Q3: due October 31, 2025
- A1-QRT Q4: due January 31, 2026
- UC-018 quarterly: same dates as A1-QRT
- A1-R + W-2 transmittal: due January 31, 2026
- Monthly PIT deposits: 15th of following month via AZTaxes.gov
- Federal W-2s and 941s: separate federal filings (not in scope)

**Proposition 206 sick time:**

- Desert Sun has 8 employees (under 15), so cap is 24 hours per year per employee
- Accrual: 1 hour per 30 hours worked = approximately 67 hours per year if fully accrued for 2,000-hour employee
- Cap is 24 hours per year regardless
- Year-end: unused balance carries over but is functionally capped at 24 hours of usage next year

**Final-pay scenario:**

If Desert Sun terminates an employee on Tuesday, the final paycheck (including any policy-required vacation payout) is due by the following Friday next week (7 working days) OR the next regular payday, whichever is sooner.

### 11.2 Example B — Multistate employer with Arizona residents

**Facts:**

- Cascadia Cloud Inc., a Delaware C-corp headquartered in Seattle, Washington, with 30 employees nationwide
- 4 employees are Arizona residents performing services entirely remotely from Arizona
- 2 additional employees are Washington residents who travel to Arizona for client engagements ~30 workdays per year
- Cascadia is not previously registered in Arizona

**Arizona employer registration:**

Cascadia must register with both ADOR (for PIT withholding) and DES (for UI) within 20 days of the first Arizona payroll. The 4 Arizona-resident employees performing services from Arizona create Arizona nexus for both PIT and UI.

**PIT withholding on Arizona residents working in Arizona:**

Full Arizona PIT withholding on the 4 Arizona residents under their A-4 elections. Cascadia must collect Form A-4 from each.

**PIT withholding on Washington residents traveling to Arizona:**

Under A.R.S. § 43-401, compensation for services PERFORMED in Arizona is subject to Arizona PIT withholding regardless of employee residency. For a Washington resident with 30 Arizona workdays out of 240 total workdays:

- Arizona-source wages = total wages × (30/240) = 12.5% of total wages
- Withhold Arizona PIT only on the 12.5% Arizona-source portion
- If the employee has not submitted an A-4, default 2.0% applies
- Practical approach: payroll system flags each pay period the employee was in Arizona and computes a pro-rata Arizona-source amount

**UI on Arizona-resident employees:**

The 4 Arizona-resident employees performing services in Arizona are clearly Arizona UI-covered. UC-018 reports them. New-employer UI rate is 2.00% for the first 2 calendar years.

**UI on Washington-resident employees traveling to Arizona:**

UI coverage for multistate workers follows the four-part localization-of-services test in A.R.S. § 23-615(B):

1. Service is "localized" in the state where it is performed entirely or only incidentally elsewhere; if so, UI is paid to that state.
2. If not localized in any state, UI is paid to the state where the employee's base of operations is.
3. If no base of operations, UI is paid to the state from which services are directed and controlled.
4. If none of the above, UI is paid to the state of residence.

For the Washington-resident traveling to Arizona occasionally, services are localized in Washington (the 30 Arizona workdays are incidental), so UI is paid to Washington. Cascadia does NOT report these employees on the AZ UC-018.

**Proposition 206 sick time:**

Cascadia has 30 employees nationwide, but Proposition 206's 15-employee cap test counts ALL employees regardless of location. Cascadia has 15+ employees, so the 40-hour annual cap applies. All 6 employees who perform any work in Arizona are entitled to earned paid sick time. The Washington residents accrue sick time for their Arizona workdays only.

### 11.3 Example C — Worker classification audit

**Facts:**

- Mesa Marketing LLC engaged Jordan as a "freelance graphic designer" for 11 months in 2024 and 2025
- Jordan worked 40 hours per week at Mesa's office
- Mesa provided a laptop, Adobe Creative Cloud subscription, and a corporate email
- Jordan was paid $35/hour weekly
- Mesa did not offer benefits and issued Jordan a 1099-NEC for 2024
- Jordan filed an Arizona unemployment claim in 2025 after the engagement ended
- DES audit triggered

**7-factor analysis**

| Factor | Mesa/Jordan facts | Pass/Fail |
| --- | --- | --- |
| 1. No required location | Required to work at Mesa office | FAIL |
| 2. Free to serve others | Mesa expected 40hr/wk; effectively exclusive | FAIL |
| 3. Free to accept/decline projects | All projects assigned, no decline | FAIL |
| 4. Own tools | Mesa-provided laptop and Adobe subscription | FAIL |
| 5. Authority to hire assistants | Not addressed; no assistants used | FAIL (no indication of authority) |
| 6. Risk of profit/loss | Hourly pay, no profit risk | FAIL |
| 7. No employee benefits/training | No benefits, but Mesa-provided onboarding training | MIXED |

No DIBS was ever signed. The 7-factor test fails on at least 6 factors. DES will reclassify Jordan as an employee.

**Consequences:**

- AZ UI back contributions on Jordan's $72,800 in 2025 wages (1,820 hours × $35) — but only the first $8,000 is taxable, so $8,000 × Mesa's UI rate × 2 years if also 2024
- AZ PIT back withholding: Mesa is liable for the AZ PIT that should have been withheld; Jordan ultimately owes the tax but Mesa is liable for failure to withhold and potentially for the tax itself if Jordan cannot be located or paid the tax already
- Penalties under A.R.S. §§ 23-738 (UI) and 42-1125 (PIT)
- Federal exposure: IRS reclassification under IRC § 3509 reduced rates if voluntary settlement or no fraud
- Proposition 206 sick time: Jordan was entitled to earned paid sick time; Mesa owes the back-pay equivalent, with treble-damages exposure
- Workers' compensation exposure: Mesa likely had no workers' comp covering Jordan; Industrial Commission penalty exposure

**Lesson:**

Issuing a 1099-NEC does not establish contractor status. The economic reality of the engagement controls. To support contractor status, Mesa should have:

- Signed a written contract including a DIBS
- Allowed Jordan to work from his own location
- Paid project-based fees, not hourly
- Required Jordan to provide his own equipment
- Permitted Jordan to take other clients

## 12. Compliance Checklist

For each Arizona employer engagement, the reviewer should verify:

- [ ] ADOR PIT withholding registration complete (TIN issued)
- [ ] DES UI registration complete (Arizona Employer Account Number issued)
- [ ] Current A-4 on file for every employee (updated for the 0.5-3.5% options post-2022)
- [ ] Default 2.0% applied to any employee without an A-4
- [ ] A1-QRT filed quarterly (or A1-APR annually if qualifying)
- [ ] Monthly or next-day deposits made on schedule
- [ ] UC-018 filed quarterly with correct experience rate
- [ ] A1-R + W-2 transmittal filed by January 31
- [ ] Proposition 206 sick time accrual at 1/30 ratio
- [ ] 15-or-fewer determination correct (counts all employees nationwide)
- [ ] Sick time balance, used, and accrual shown on every paystub
- [ ] Industrial Commission workplace poster displayed
- [ ] Every independent contractor has a signed DIBS and meets 7 factors, OR has been reclassified as employee
- [ ] Final pay procedure documented and tested against the 7-working-days / next-payday standard
- [ ] Payroll provider configured for supplemental wage handling consistent with A-4 elections
- [ ] AZ UI experience rating notice (Form UB-006) reviewed annually within 15-day protest window
- [ ] Job Training Tax 0.10% added for positive-reserve experienced employers
- [ ] §125, 401(k), and other pre-tax deductions correctly mapped to PIT-wages and UI-wages bases

## 13. References

- A.R.S. § 43-401 et seq. — Arizona income tax withholding
- A.R.S. § 43-1011 — Personal income tax rate (2.5% flat)
- A.R.S. Title 23, Chapter 4 — Arizona Employment Security Act (UI)
- A.R.S. § 23-622.01 — UI taxable wage base
- A.R.S. § 23-732 — UI contribution rates and experience rating
- A.R.S. § 23-769 — Job Training Tax
- A.R.S. §§ 23-371 to 23-381 — Earned Paid Sick Time (Fair Wages and Healthy Families Act)
- A.R.S. § 23-353 — Payment of wages on discharge or resignation
- A.R.S. § 23-355 — Treble damages for unpaid wages
- A.R.S. § 23-902(D), § 23-1601 — Worker classification and Declaration of Independent Business Status
- ADOR Form A-4 (2023 revision) — Employee's Arizona Withholding Election
- ADOR Form A1-QRT — Arizona Quarterly Withholding Tax Return
- ADOR Form A1-R — Arizona Annual Withholding Reconciliation Return
- ADOR Form A1-APR — Arizona Annual Payment Withholding Tax Return
- ADOR Publication 701 — Withholding Tax Tables and Instructions
- DES Form UC-018 — Unemployment Tax and Wage Report
- DES Form UB-006 — Determination of Unemployment Insurance Tax Rate
- Industrial Commission of Arizona — Fair Wages and Healthy Families Act guidance

## 14. Reviewer Sign-Off

This skill produces a draft Arizona payroll compliance analysis. A human reviewer credentialed under Circular 230 (CPA, EA, or attorney) and familiar with Arizona-specific employment-tax practice must sign off on every output. State-employment-tax positions are NOT within IRS Circular 230 directly but the credentialed reviewer should confirm Arizona-specific competence. Workers' compensation and wage-and-hour determinations may require Arizona-licensed counsel.

End of skill.

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
