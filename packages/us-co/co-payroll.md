---
name: co-payroll
description: Tier 2 Colorado content skill for employer payroll compliance covering tax year 2025. Includes the 4.4% flat PIT phasing from 4.55%, DR 1098 state withholding form, DR 1094 annual reconciliation, CO SUTA wage base $24,800 with rates 0.50-10.39%, the FAMLI Paid Family and Medical Leave program effective January 2024 (0.9% total payroll tax split between employer and employee for 10+ employees), Healthy Families and Workplaces Act 48-hour paid sick leave, Equal Pay for Equal Work Act salary range disclosure requirements, and ABC contractor classification.
jurisdiction: US-CO
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# CO Payroll

## Colorado Payroll Compliance Skill (Tax Year 2025)

## 1. Scope

- **Tier 2 dependency requirement** — MUST be loaded alongside `us-tax-workflow-base` v0.2 or later.  _(Skill scope statement)_

This skill governs employer payroll obligations in the State of Colorado for tax year 2025. It is a Tier 2 content skill and MUST be loaded alongside `us-tax-workflow-base` v0.2 or later. It covers:

- Colorado Personal Income Tax (PIT) withholding at the 4.4% flat rate (Colorado Revised Statutes §39-22-104), including the supplemental withholding rate and the 2025 step-down from the historical 4.55% rate.
- The DR 1098 Colorado Employee Withholding Certificate (state analog of the federal Form W-4) and the optional use of the federal Form W-4 for Colorado purposes.
- The DR 1094 Annual Reconciliation of Income Tax Withheld and the DR 1093 Annual Transmittal of State W-2s (commonly described as the "combined" annual filing in informal usage).
- Colorado State Unemployment Tax Act (SUTA) liability administered by the Colorado Division of Unemployment Insurance (CDLE-UI), including the 2025 taxable wage base of $24,800, the experience-rated employer schedule (0.50% to 10.39%), the 1.70% new-employer rate for non-construction employers, and the support surcharge components.
- The Colorado Family and Medical Leave Insurance program ("FAMLI"), in effect for benefits since January 1, 2024 and continuing in 2025, with 0.9% total payroll premium, employer/employee split rules, the 10-employee threshold, the $176,100 wage cap (Social Security wage base for 2025), and the 12-week leave entitlement.
- The Healthy Families and Workplaces Act (HFWA): 48 hours of accrued paid sick leave per year plus the Public Health Emergency (PHE) supplemental leave entitlement.
- The Equal Pay for Equal Work Act (EPEWA), Senate Bill 19-085 as amended by Senate Bill 23-105 (the "Ensure Equal Pay for Equal Work" amendments), including the salary range disclosure obligation and the new post-selection notice obligation effective January 1, 2024.
- Worker classification under Colorado's modified ABC test (C.R.S. §8-70-115(1)(b)) for unemployment-insurance purposes.
- Final pay timing rules under the Colorado Wage Act, C.R.S. §8-4-109.
- Construction industry compliance overlays: separate SUTA rate schedule, HB 19-1267 wage-theft criminal exposure, and the construction-employee retainage rules.

Out of scope:
- Federal income tax withholding, FICA, FUTA — see `us-federal-payroll` and `us-payroll-fundamentals`.
- Local occupational privilege taxes ("OPT" or "head taxes") imposed by Denver, Aurora, Glendale, Greenwood Village, and Sheridan — see `co-local-opt`. This skill mentions them only at the integration points.
- Workers' compensation insurance under C.R.S. §8-40-101 et seq.
- ERISA-governed retirement plans, except where the Colorado SecureSavings state mandate intersects with payroll. SecureSavings registration enforcement is addressed in `co-securesavings`.

## 2. Colorado Personal Income Tax Withholding

### 2.1 Statutory rate

- **Colorado PIT withholding rate 2025** — 4.40% percent (flat rate for tax year 2025)  _(C.R.S. §39-22-104(1.7))_
- **Historical PIT rate 2020-2021** — 4.55% percent (tax years 2020 through 2021)  _(C.R.S. §39-22-104(1.7))_
- **PIT rate 2022 and forward** — 4.40% percent (tax years 2022 and forward, per TABOR refund mechanism and Proposition 121 (approved November 2022))  _(C.R.S. §39-22-627; Proposition 121)_
- **Colorado PIT withholding rate 2025** — 4.40% percent (flat rate for tax year 2025)  _(C.R.S. §39-22-104(1.7))_
- **TABOR further reduction check** — Colorado may, contingent on TABOR refund triggers under C.R.S. §39-22-627(3)(a), step the rate down further for a given tax year. For tax year 2025 no such temporary further reduction was triggered as of the last_updated date of this skill. Reviewers MUST confirm against CDOR's current-year Income 70 publication if filing after the legislative session.  _(C.R.S. §39-22-627(3)(a))_

### 2.2 DR 1098: Colorado Employee Withholding Certificate

- **DR 1098** — Colorado's state-equivalent of the federal Form W-4. Since tax year 2022 CDOR has accepted a DR 1098 in lieu of using the federal Form W-4 for Colorado withholding purposes.  _(CDOR DR 1098)_
- **Employer options for withholding form** — Employers MAY use either: (a) The federal Form W-4 alone, with Colorado-specific allowances inferred under the DR 1098 Worksheet, OR (b) The DR 1098 itself, completed by the employee, OR (c) Both, with the DR 1098 governing for Colorado purposes if the employee chooses a different number of withholding allowances or additional Colorado withholding amount than the federal W-4 implies.  _(DR 1098 Worksheet)_

The DR 1098 collects:
- Filing status (single; married filing jointly; married filing separately; head of household).
- Annual gross wages estimate (used by the worksheet).
- Number of dependent children under age 17 and other dependents.
- Other Colorado-specific income (interest, dividends, side income).
- Other Colorado adjustments (Colorado-source deductions).
- Other Colorado tax credits the employee expects to claim.
- An "Additional Colorado Withholding" line (analogous to W-4 step 4(c)).
- Optional exemption claim if the employee expects zero Colorado tax liability (analogous to the prior W-4 exemption claim, which the federal form no longer supports directly).

- **DR 1098 retention and expiration** — Employers retain the DR 1098 with payroll records and apply it to all wage payments beginning with the first payroll on or after receipt. The DR 1098 does NOT expire annually — it remains in effect until superseded by a new one. Employees who claim exempt MUST refile by February 15 of each subsequent year, mirroring federal W-4 exempt-claim mechanics.  _(CDOR DR 1098 instructions)_

AUDIT FLASH POINT — DR 1098 NEGLECT: Employers commonly default new hires to "Single, zero allowances" using the federal W-4 only and never offer the DR 1098. The CDOR position is that a properly completed federal W-4 is sufficient absent an employee request, but the employer's exposure on over-withholding refund claims and on EPEWA recordkeeping audits is materially lower when DR 1098s are retained in the employee file. Workpapers MUST document which form is in use.

### 2.3 Withholding deposit cadence

- **Quarterly filer threshold** — under $7,000 USD annual aggregate withholding liability (Deposit by the last day of the month following each calendar quarter (April 30, July 31, October 31, January 31))  _(CDOR withholding deposit rules)_
- **Monthly filer threshold** — between $7,000 and $50,000 USD annual aggregate withholding liability (Deposit by the 15th day of the following month)  _(CDOR withholding deposit rules)_
- **Weekly filer threshold** — $50,000 or more USD annual aggregate withholding liability (Deposit within three business days of the wage payment date that triggered the weekly threshold)  _(CDOR withholding deposit rules)_
- **Seasonal filer** — Businesses with regular off-season months can apply for seasonal status; deposits only during active months.  _(CDOR withholding deposit rules)_
- **Electronic filing requirement** — All deposits and returns are submitted electronically through Revenue Online unless CDOR has granted a paper-filing waiver. The remittance form attached to each deposit is the DR 1094 in its periodic role (see §2.4).  _(Revenue Online filing requirement)_

### 2.4 DR 1094 (Annual Reconciliation) and DR 1093 (Transmittal)

- **DR 1094** — Colorado W-2 Wage Withholding Tax Return. This is BOTH (a) the periodic payment voucher accompanying each deposit, AND (b) the annual reconciliation form. The annual reconciliation reports total Colorado wages paid, total Colorado tax withheld per period, and any reconciliation adjustments. It is due January 31 of the year following the wage year.  _(CDOR DR 1094)_
- **DR 1093** — Annual Transmittal of State W-2s. This accompanies the paper or electronic submission of Colorado W-2s (the Colorado copy of federal Form W-2). It is also due January 31.  _(CDOR DR 1093)_

In practice CDOR's Revenue Online accepts a combined annual filing that satisfies both DR 1094 and DR 1093 in a single workflow. Practitioners informally call this the "combined annual filing," which is the usage adopted by the description in the frontmatter of this skill.

- **Penalty for failure to file annual reconciliation** — $50 minimum penalty plus the higher of $5 per W-2 unreconciled or 5% of unreported withholding per month (capped at 12 months).  _(CDOR penalty rules)_
- **Penalty for failure to deposit timely** — 5% penalty plus 0.5% per month, plus interest at the CDOR statutory rate (subject to annual TABOR-adjusted rate publication; reviewers verify current rate).  _(CDOR penalty rules)_

## 3. Colorado State Unemployment Insurance (SUTA)

### 3.1 Coverage and registration

- **Employer subject-to-UI tests** — An employer becomes subject to Colorado UI when ANY of the following tests is met: - Pays $1,500 or more in wages in any calendar quarter in the current or preceding calendar year (general employer test); OR - Employs at least one worker in any portion of a day in 20 different calendar weeks in the current or preceding year (general employer test, alternative branch); OR - Pays $1,000 or more in domestic-service wages in any calendar quarter (domestic employer test); OR - Pays $20,000 or more in agricultural wages in any calendar quarter (agricultural employer test).  _(C.R.S. §8-70-101 et seq.)_
- **Registration process** — A subject employer registers via My UI Employer+ (the CDLE-UI portal). Construction industry employers register on a separate workflow that asserts construction status — this matters for the rate schedule (see §3.4).  _(CDLE-UI My UI Employer+ portal)_

### 3.2 Taxable wage base for 2025

- **Colorado SUTA taxable wage base 2025** — $24,800 USD per employee per calendar year  _(C.R.S. §8-76-102.5)_
- **Colorado SUTA taxable wage base 2024** — $23,800 USD per employee per calendar year  _(C.R.S. §8-76-102.5)_

### 3.3 Premium rate schedule

- **2025 experience-rated SUTA premium rate range** — 0.50% to 10.39% percent (applied to the first $24,800 of each employee's wages, determined by reserve ratio and UI Trust Fund solvency tier; published December 2024)  _(2025 CDLE rate notices)_
- **Non-construction new-employer rate** — 1.70% percent (first 3 years)  _(2025 CDLE rate notices)_
- **Construction new-employer rate** — published annually on a separate schedule that materially exceeds 1.70% (commonly in the 3-5% range; reviewer to confirm against the 2025 rate notice) percent (first 3 years)  _(2025 CDLE rate notice (reviewer to confirm))_
- **Support Surcharge 2025** — 0.22% percent (subject to annual adjustment; reviewer to confirm against current CDLE-UI rate notice)  _(C.R.S. §8-77-106)_
- **Bond Assessment 2025** — Not assessed for 2025 because the bond issued during the COVID Trust Fund solvency crisis was retired in 2023. Reviewers verify against the current rate notice before assuming zero.  _(SB 20-207)_
- **Combined effective rate for new non-construction employer 2025** — 1.70% premium + 0.22% surcharge = 1.92%, applied to the $24,800 wage base, producing a per-employee maximum cost of approximately $476.16 per year  _(Skill computed example)_

### 3.4 Construction industry overlay

- **Construction employer separate experience pool** — Colorado treats construction employers as a separate experience pool under C.R.S. §8-76-102.5(5). The construction new-employer rate is substantially higher than the 1.70% non-construction rate because the construction pool has historically had higher claim incidence. Employers registering should self-identify on the My UI Employer+ portal with the appropriate NAICS code in the 23xxxx range; misclassification of industry sector to obtain the lower non-construction rate is fraud under C.R.S. §8-81-101.  _(C.R.S. §8-76-102.5(5); C.R.S. §8-81-101)_

### 3.5 Quarterly reporting

- **UI Premium and Wage Report due dates** — The Colorado UI Premium Report and Wage Report are due: Q1 — April 30; Q2 — July 31; Q3 — October 31; Q4 — January 31.  _(CDLE-UI filing schedule)_
- **Electronic filing and report contents** — Filing is electronic-only through MyUI Employer+. The wage report itemizes each employee's gross wages for the quarter; the premium report computes the SUTA owed using the employer's published rate and the up-to-the-wage-base portion of each employee's wages.  _(CDLE-UI MyUI Employer+)_

## 4. Colorado FAMLI (Family and Medical Leave Insurance)

### 4.1 Program overview

- **FAMLI program history** — Colorado's Paid Family and Medical Leave Insurance program ("FAMLI") was created by Proposition 118 (November 2020), codified at C.R.S. §8-13.3-501 et seq. Premium collection began January 1, 2023. Benefit payments to employees on qualifying leave began January 1, 2024 and continue in 2025. The program is administered by the CDLE Division of Family and Medical Leave Insurance ("CDLE-FAMLI").  _(C.R.S. §8-13.3-501 et seq.; Proposition 118)_
- **FAMLI qualifying leave reasons** — FAMLI provides up to 12 weeks of paid leave per benefit year for: - Bonding with a new child (birth, adoption, foster placement); - Caring for a family member with a serious health condition; - The employee's own serious health condition; - Qualifying military exigency; - Safe leave for survivors of domestic violence, stalking, sexual assault, or abuse.  _(C.R.S. §8-13.3-501 et seq.)_
- **FAMLI base leave entitlement** — 12 weeks weeks per benefit year  _(C.R.S. §8-13.3-501 et seq.)_
- **FAMLI pregnancy/childbirth complications additional leave** — An additional 4 weeks (16 weeks total) is available for pregnancy or childbirth complications. weeks  _(C.R.S. §8-13.3-501 et seq.)_
- **FAMLI weekly benefit calculation** — The weekly benefit is wage-replacement on a progressive schedule: 90% of the portion of the employee's average weekly wage at or below 50% of the state AWW, plus 50% of the portion above.  _(CDLE-FAMLI benefit schedule)_
- **2025 FAMLI maximum weekly benefit** — $1,324.21 USD (90% of the 2025 Colorado average weekly wage published by CDLE)  _(CDLE-FAMLI 2025 benefit publication)_

### 4.2 Premium: 0.9% total, employer/employee split

- **Total FAMLI premium** — 0.9% percent of wages (applied to the same wage cap as the Social Security wage base)  _(C.R.S. §8-13.3-501 et seq.)_
- **2025 FAMLI wage cap** — $176,100 USD  _(2025 Social Security wage base)_
- **Default premium split** — The default statutory split is 0.45% employee + 0.45% employer, with the employer required to deposit the full 0.9% to CDLE-FAMLI quarterly.  _(CDLE-FAMLI premium rules)_
- **Sub-10 employer waiver** — Employers with fewer than 10 employees are NOT required to pay the employer 0.45% share. They MUST still withhold and remit the employee's 0.45% share. The employer share is waived but the employee share is not.  _(CDLE-FAMLI premium rules)_
- **10+ employer obligation** — Employers with 10 or more employees owe the full 0.9% (0.45% employer + 0.45% employee withheld). The employer may voluntarily absorb the employee's share if it chooses (a common election among Colorado employers competing for talent).  _(CDLE-FAMLI premium rules)_
- **10-employee count methodology** — The 10-employee count uses the national employee count, not the Colorado-only headcount, and uses a rolling 20-week look-back analogous to the federal FMLA 50-employee test. An employer that is 10+ for any 20 weeks (consecutive or not) in the calendar year is treated as a 10+ employer for the next premium year. Local-government employers have unique opt-out rights under C.R.S. §8-13.3-522.  _(C.R.S. §8-13.3-522)_

AUDIT FLASH POINT — 10-EMPLOYEE THRESHOLD MISCOUNT:

The single most common FAMLI compliance error is for an employer with 8-12 employees to assume they are exempt from the employer share because they "feel small." The actual rules:

1. The count is total employees nationally, including part-time and seasonal workers, NOT FTE-adjusted and NOT Colorado-only.
2. Owners, partners, and members of an LLC are NOT counted as employees unless they receive W-2 wages.
3. The look-back is the prior calendar year's average headcount across 20 weeks, not a point-in-time count.
4. Even employers under 10 MUST register, withhold the employee share, and file quarterly reports — only the EMPLOYER share is waived.
5. Crossing the 10-employee threshold mid-year does not retroactively make the employer responsible for the employer share for prior quarters of that year; the obligation activates the following premium year (the following January 1).

Workpapers MUST document the 20-week headcount computation and retain the underlying payroll register snapshots that support the count. A CDLE-FAMLI audit will request these directly.

### 4.3 Quarterly premium remittance

- **FAMLI quarterly remittance due dates** — FAMLI premiums are remitted quarterly through My FAMLI+ Employer: Q1 — April 30; Q2 — July 31; Q3 — October 31; Q4 — January 31.  _(CDLE-FAMLI My FAMLI+ Employer)_
- **Filing method by headcount** — Filing is electronic-only above 10 employees. Below 10 employees, paper filing is technically available but discouraged.  _(CDLE-FAMLI filing rules)_
- **Quarterly filing wage reporting and cap** — The quarterly filing reports each employee's FAMLI-subject wages (gross wages up to $176,100 year-to-date per employee) and computes the 0.9% premium (or 0.45% for employers under 10). Wages above the $176,100 cap for an employee year-to-date are excluded.  _(CDLE-FAMLI filing rules)_

### 4.4 Private plan substitution

- **Private plan substitution rules** — An employer may apply to CDLE-FAMLI for approval to substitute a private paid-leave plan that meets or exceeds FAMLI benefits and costs no more to the employee than the FAMLI program. Approval is on a one-year basis renewable annually; private-plan employers are exempt from the 0.9% premium but pay a separate administrative fee to CDLE-FAMLI. This skill does not deep-dive private plan administration — refer to `co-famli-private-plan` (planned).  _(CDLE-FAMLI private plan program)_

### 4.5 Job protection

- **FAMLI job protection eligibility** — An employee who has been employed by the same employer for at least 180 days at the time of leave commencement is entitled to job protection (restoration to the same or equivalent position) on return from FAMLI leave. This overlays but does not displace federal FMLA — for employees eligible under both, the leaves run concurrently and the more protective rule prevails.  _(CDLE-FAMLI job protection rules)_

## 5. Healthy Families and Workplaces Act (HFWA)

### 5.1 48-hour annual accrual

- **HFWA applicability** — The Colorado Healthy Families and Workplaces Act (SB 20-205), C.R.S. §8-13.3-401 et seq., requires every Colorado employer regardless of size to provide paid sick leave.  _(C.R.S. §8-13.3-401 et seq.; SB 20-205)_
- **Sick leave accrual rate** — 1 hour per 30 hours worked hours  _(C.R.S. §8-13.3-401 et seq.)_
- **Maximum mandatory accrual** — 48 hours per year hours  _(C.R.S. §8-13.3-401 et seq.)_
- **Maximum carryover** — 48 hours hours  _(C.R.S. §8-13.3-401 et seq.)_
- **New hire usage and pay rate** — New hires may use accrued leave immediately (no 90-day wait). Sick leave is paid at the employee's regular rate.  _(C.R.S. §8-13.3-401 et seq.)_

Eligible uses:
- Employee's mental or physical illness, injury, or health condition.
- Diagnosis, care, or treatment of same.
- Preventive care.
- Care for a covered family member.
- Safe leave (domestic abuse, sexual assault, stalking).
- School/childcare closure due to weather or public health.
- Bereavement.

### 5.2 Public Health Emergency (PHE) supplemental leave

- **PHE supplemental leave amounts** — When a federal, state, or local public health emergency is declared, the HFWA requires employers to provide additional supplemental paid leave on top of the 48 hours: Up to 80 hours for full-time employees (40+ hours/week). For part-time employees, the greater of (a) hours typically worked in a 14-day period, or (b) hours actually worked over the prior 14 days, capped at 80 hours.  _(HFWA PHE provisions)_
- **PHE leave duration and refresh** — The PHE leave is available throughout the duration of the declared emergency and for four weeks after its expiration. PHE leave is a one-time pool per emergency, but it refreshes when a new unrelated emergency is declared.  _(HFWA PHE provisions)_

As of the last_updated date of this skill there is no active statewide PHE in Colorado. Reviewers MUST confirm against CDLE publications before excluding PHE supplemental leave from a payroll configuration.

### 5.3 Notice, posting, and recordkeeping

- **HFWA notice, posting, recordkeeping requirements** — Employers must: - Provide written notice to each employee at hire describing HFWA rights (the CDLE-INFO 6B model notice satisfies this). - Post the CDLE workplace poster (HFWA section) in each workplace and on any electronic platform employees regularly access. - Maintain HFWA records (accrual, use, balance) for two years — not three, the general Colorado payroll record retention period.  _(CDLE-INFO 6B)_

## 6. Equal Pay for Equal Work Act (EPEWA)

### 6.1 Statutory framework

- **EPEWA statutory framework** — The Colorado Equal Pay for Equal Work Act, C.R.S. §8-5-101 et seq., was enacted by SB 19-085 effective January 1, 2021, and substantially expanded by SB 23-105 ("Ensure Equal Pay for Equal Work") effective January 1, 2024. Both provisions are in force for 2025.  _(C.R.S. §8-5-101 et seq.; SB 19-085; SB 23-105)_

### 6.2 Salary range disclosure

- **Job posting disclosure obligations** — Every job posting for a position that could be performed in Colorado (remote postings included if a Colorado-based employee could fill the role) MUST include: (a) The hourly or salary compensation range that the employer in good faith believes it will pay for the position. A range is permitted but must be a "good faith" range, not an arbitrary $0-$1,000,000 placeholder. (b) A general description of all benefits and other compensation offered (health insurance summary level, retirement, equity summary, bonus structure, paid time off). (c) The application deadline (or a statement that applications will be accepted on a rolling basis).  _(C.R.S. §8-5-101 et seq.)_
- **Scope of disclosure applicability** — This disclosure obligation applies to: - All external postings. - All internal postings (with limited exceptions where the position is a "career progression" rather than a "job opportunity" — CDLE INFO 9 sets the test). - Postings made by third-party recruiters and job boards on the employer's behalf.  _(CDLE INFO 9)_

### 6.3 Post-selection notice (new under SB 23-105)

- **Post-selection notice requirement** — Within 30 days after a successful candidate begins work in a posted position, the employer MUST notify employees who, at the employer's discretion, have a "career progression" interest in that position, of: - The name of the successful candidate; - Their former job title (if internal); - Their new job title; - Information on how employees may demonstrate interest in similar future opportunities.  _(SB 23-105)_

This requirement is widely under-implemented and is the leading EPEWA enforcement target as of 2025.

### 6.4 Pay-history prohibition

- **Pay-history prohibition rules** — Employers MAY NOT: - Ask applicants about wage-rate history. - Rely on prior wage history to set offered compensation. - Discriminate or retaliate against an applicant who declines to disclose prior wage history.  _(C.R.S. §8-5-101 et seq.)_

### 6.5 Penalties

- **EPEWA penalty amounts** — $500 to $10,000 per violation (per posting, per failure-to-notice). Multiple postings of the same position can be aggregated as one violation at the Director's discretion. Civil action by aggrieved employees is also available for pay-equity violations.  _(C.R.S. §8-5-203)_

AUDIT FLASH POINT — EPEWA POSTING NEGLECT:

The EPEWA salary-disclosure regime is enforced primarily by employee and union complaints, not proactive audit. CDLE has assessed five-figure aggregate penalties against multistate employers whose "job posting on LinkedIn for a remote role open to Colorado" omitted the salary range. Common failure modes:

1. Treating remote roles as out-of-scope because no specific Colorado office is designated — wrong. If the role COULD be filled by a Colorado-based employee, the disclosure applies.
2. Listing only "DOE" (depending on experience) instead of a range.
3. Listing a $0 to $X range with X arbitrarily high.
4. Posting the job range in the original posting but omitting it from the LinkedIn/Indeed amplifications.
5. Forgetting the post-selection notice obligation entirely.

Workpapers for an EPEWA risk assessment MUST review (a) a random sample of 2025 postings, (b) the post-selection notice log, (c) the internal-vs-external posting classification policy, and (d) the job-board syndication process for range carry-through.

## 7. Worker Classification — Colorado ABC Test

### 7.1 The ABC test under C.R.S. §8-70-115

- **ABC test three prongs** — For Colorado unemployment-insurance purposes, a worker is presumed to be an employee unless the putative employer can establish ALL THREE of the following ("ABC test"): A. The worker is free from control and direction in the performance of the service, both under the contract and in fact; AND B. The service is performed outside the usual course of business of the person for whom the service is performed, OR is performed outside of all the places of business of the enterprise for which the service is performed; AND C. The worker is customarily engaged in an independent trade, occupation, profession, or business related to the service performed. Failure on any prong means the worker is an employee for SUTA, FAMLI, and HFWA purposes.  _(C.R.S. §8-70-115)_

### 7.2 The nine-factor safe harbor under §8-70-115(1)(c)

- **Nine-factor documentary safe harbor** — C.R.S. §8-70-115(1)(c) provides a documentary safe harbor: a written contract that includes at least nine specified provisions (e.g., the worker is not insurance-covered by the principal; pay is by the job not by time; the worker provides own tools; etc.) creates a rebuttable presumption of contractor status. However, the actual conduct of the relationship can override the contract language. The safe harbor is heavily contested in audits.  _(C.R.S. §8-70-115(1)(c))_

### 7.3 ABC vs federal common-law test

- **ABC test vs federal common-law test** — Colorado's ABC test is STRICTER than the federal IRS common-law test used for federal employment-tax purposes. A worker can be a contractor for IRS purposes (1099-NEC) and an employee for Colorado SUTA / FAMLI / HFWA purposes simultaneously. This is a common source of error in multistate practices: a worker properly classified as a 1099 federally may still trigger Colorado employer liability.  _(C.R.S. §8-70-115)_

AUDIT FLASH POINT — ABC IN COLORADO:

The Colorado ABC test is one of the strictest in the United States and substantially stricter than the federal common-law test. Common failure modes:

1. Treating long-tenured "contractors" who work only for the principal as bona fide independent contractors — fails Prong C (not customarily engaged in an independent trade).
2. Treating a contractor who performs the same core services as the company's regular employees as a contractor — fails Prong B (within the usual course of business).
3. Relying on a contract with the nine §8-70-115(1)(c) clauses without conforming actual practice to the clauses.
4. Aggregating 1099 spend that exceeds the W-2 payroll base — a strong CDLE-UI audit trigger.
5. Reclassifying employees as contractors to avoid FAMLI premium collection — separate violation under FAMLI rules and triggers C.R.S. §8-13.3-516 retaliation exposure.

Workpapers for any Colorado contractor classification MUST walk through ALL THREE prongs, not just rely on the contract template.

## 8. Final Pay and Wage Act

- **Discharge/involuntary termination final pay timing** — All wages and compensation earned and unpaid at separation are due immediately. If the employer's accounting unit is not available (e.g., after-hours discharge), wages are due within six hours of the start of the accounting unit's next regular workday, OR within 24 hours if accounting is offsite.  _(C.R.S. §8-4-109)_
- **Voluntary resignation final pay timing** — Wages are due on the next regular payday.  _(C.R.S. §8-4-109)_
- **PTO/vacation treatment at termination** — Earned and accrued vacation pay is treated as wages under C.R.S. §8-4-101(14)(a)(III) following Nieto v. Clark's Market (2021). It cannot be forfeited at termination, even under a "use it or lose it" policy, to the extent earned. PTO and vacation that has been earned but not used IS payable at separation; "front-loaded but unearned" leave can be subject to forfeiture rules in the employee handbook so long as those rules are clear and consistent.  _(C.R.S. §8-4-101(14)(a)(III); Nieto v. Clark's Market (2021))_
- **HFWA sick leave at separation** — NOT payable at separation, unless the employer voluntarily commits to pay it in the handbook.  _(C.R.S. §8-4-109)_
- **Penalty for non-payment of final wages** — A demand letter from the employee triggers a 14-day cure period. After 14 days, the employee may recover the unpaid wages PLUS a statutory penalty equal to the greater of (a) two times the unpaid amount, or (b) $1,000. Willful nonpayment doubles this to three times or $3,000.  _(C.R.S. §8-4-109)_

## 9. Construction Industry Compliance Overlay

- **Construction industry heightened obligations** — Construction industry employers in Colorado are subject to several heightened payroll obligations: - Separate SUTA rate pool (see §3.4). - HB 19-1267: criminal wage-theft exposure — failure to pay wages with intent or reckless disregard is a Class 6 felony if the amount exceeds $2,000. - Mechanic's lien retainage rules under C.R.S. §38-22-101 and prompt-payment statutes under C.R.S. §24-91-103 (public works) — these are not payroll but they affect when payroll cash is available. - The Workers' Compensation Cost Containment Certificate (CCC) is broadly required in construction to maintain insurance rate stability.  _(HB 19-1267; C.R.S. §38-22-101; C.R.S. §24-91-103)_

This skill does NOT cover prevailing wage under Davis-Bacon or Colorado HB 21-1264 (Colorado prevailing wage on certain public projects) — see `co-prevailing-wage`.

## 10. Worked Examples

### Example 1 — Colorado 5-employee creative agency (sub-10 FAMLI)

Facts:
- Single-member LLC operating as an S-corp in Denver, CO.
- 5 employees on W-2 (including the owner-employee at $80,000 salary).
- 4 other employees at average $55,000 each.
- Total Colorado W-2 wages 2025: $80,000 + (4 × $55,000) = $300,000.
- Owner-employee on FAMLI applies because owner takes W-2.

Step 1 — Colorado PIT withholding:
- Aggregate Colorado withholding for 2025 (assuming no other state income, single filer for owner, married joint for others): approximately 4.40% × $300,000 = $13,200, less applicable DR 1098 worksheet adjustments (~$1,500 in standard adjustments).
- Net annual Colorado withholding ≈ $11,700.
- Filing cadence: $11,700 is in the $7,000-$50,000 range, so monthly filing of DR 1094 deposits, due the 15th of the following month.
- Annual DR 1094 reconciliation due January 31, 2026.
- DR 1093 W-2 transmittal due January 31, 2026.

Step 2 — Colorado SUTA:
- All 5 employees exceed the $24,800 wage base.
- Taxable wages: 5 × $24,800 = $124,000.
- New-employer non-construction rate: 1.70%.
- Support surcharge: 0.22%.
- Combined: 1.92%.
- Annual SUTA: 1.92% × $124,000 = $2,380.80.
- Filed quarterly through MyUI Employer+.

Step 3 — FAMLI (sub-10 employer):
- 5 < 10 employees → employer share WAIVED.
- Employee share: 0.45% × $300,000 = $1,350 withheld from employees and remitted to CDLE-FAMLI.
- All employees under the $176,100 cap, so full wages subject.
- Quarterly remittance via My FAMLI+ Employer.
- Note: even though the employer share is waived, the employer MUST register and file quarterly returns. Skipping registration is a $50 per quarter penalty plus the unremitted employee share.

Step 4 — HFWA:
- All 5 employees accrue 1 hour per 30 hours worked.
- A full-time employee (40 hr/wk × 50 wk) accrues 66.67 hours, capped at the 48-hour annual maximum.
- Carryover into 2026: up to 48 hours per employee.

Step 5 — EPEWA:
- Any 2025 job postings must include salary range, benefits summary, application deadline.
- Post-selection notice within 30 days of each hire.

Aggregate Colorado payroll-tax burden for this employer:
- SUTA $2,380.80
- FAMLI employer share $0 (sub-10 exception)
- FAMLI employee share withheld $1,350 (employee-borne, not employer cost)
- Colorado withholding $11,700 (employee-borne)
- Total EMPLOYER cost: $2,380.80

### Example 2 — Colorado 50-employee tech company (full FAMLI)

Facts:
- Delaware C-corp with Colorado nexus, 50 W-2 employees in CO.
- Average salary $120,000. Total CO W-2 wages = $6,000,000.
- No employees over $176,100 (FAMLI cap), no employees over $24,800 wage base for SUTA (all are).
- Established employer with 2024 SUTA rate of 1.10%.

Step 1 — Colorado PIT withholding:
- Approx. 4.40% × $6,000,000 = $264,000, less DR 1098 worksheet adjustments (~$30,000) = ~$234,000 net.
- Filing cadence: > $50,000 → weekly filing, deposit within 3 business days of each payroll.
- Annual DR 1094 reconciliation due January 31, 2026.

Step 2 — Colorado SUTA:
- Taxable wages: 50 × $24,800 = $1,240,000.
- Premium rate: 1.10% (experience-rated).
- Support surcharge: 0.22%.
- Combined: 1.32%.
- Annual SUTA: 1.32% × $1,240,000 = $16,368.

Step 3 — FAMLI (10+ employer):
- Full 0.9% applies.
- All employees below $176,100 cap, so full $6,000,000 in subject wages.
- Total FAMLI premium: 0.9% × $6,000,000 = $54,000.
- Split: $27,000 employer share + $27,000 employee share withheld from employee paychecks.
- Many tech employers in Colorado voluntarily absorb the employee share; if absorbed, total employer cost is $54,000.
- If standard split: employer cost $27,000.

Step 4 — HFWA:
- Same 1-hour-per-30-hours accrual, 48-hour cap.
- For a 40 hr/wk employee, the cap binds.
- No active PHE in 2025 as of skill date.

Step 5 — EPEWA exposure:
- High-volume hiring → high posting volume → highest EPEWA exposure of these examples.
- Post-selection notice obligation is the most-missed item.
- Recommend a posting-compliance checklist in the ATS workflow.

Aggregate Colorado employer payroll-tax burden:
- SUTA $16,368
- FAMLI employer share $27,000 (or $54,000 if absorbing employee share)
- Total EMPLOYER cost: $43,368 (standard split) or $70,368 (full absorb).

### Example 3 — Multistate employer (CO + TX + remote)

Facts:
- Texas-headquartered LLC taxed as S-corp.
- 20 employees total: 12 in TX, 5 in CO, 3 remote (one in WY, two in NM).
- Q: Which Colorado obligations apply?

Analysis:

Colorado PIT withholding:
- Withhold Colorado PIT only on the 5 CO-resident employees' Colorado-source wages. The 3 remote-state employees do NOT have Colorado withholding unless they perform services in Colorado.
- File DR 1094 quarterly or monthly based on the CO portion alone.

Colorado SUTA:
- Liable for SUTA on the 5 CO employees' wages up to $24,800 each. The TX and remote employees are not Colorado SUTA wages.
- Register with CDLE-UI as a "foreign employer with Colorado operations."

Colorado FAMLI:
- HEADCOUNT TEST IS NATIONAL: 20 employees total ≥ 10, so the employer is a 10+ employer for FAMLI purposes.
- Premium applies only to CO employees' wages (FAMLI is a Colorado tax on Colorado work).
- 0.9% on 5 CO employees: employer 0.45% + employee 0.45%.
- This is the single most common multistate mistake — a CO employer with only 5 CO employees but 20 total is NOT a sub-10 employer for FAMLI purposes.

Colorado HFWA:
- Applies to all 5 CO employees.
- Does NOT apply to TX, WY, NM employees (state law-only).

EPEWA:
- Any job posting open to remote Colorado candidates MUST include CO salary disclosure even if HQ is in TX.
- This is the highest-risk multistate item.

ABC test:
- The 3 remote employees (WY, NM) are governed by their own state's ABC or common-law test. The 5 CO employees are governed by the strict Colorado ABC test.

Aggregate Colorado employer payroll-tax burden (CO portion only):
- Colorado PIT withholding: employee-borne, ~$22,000 routed to CDOR.
- SUTA: 1.92% × (5 × $24,800) = $2,380.80.
- FAMLI employer share: 0.45% × CO wages. Assuming $120k average × 5 = $600,000 CO wages, all below the cap → 0.45% × $600,000 = $2,700.
- Total CO-specific EMPLOYER cost: ~$5,080.80, plus EPEWA compliance overhead.

### Example 4 — Sub-10 employer crossing the threshold mid-year

Facts:
- Boulder-based startup begins 2025 with 8 employees.
- Hires aggressively and reaches 12 employees by August 2025.
- Q: When does the 10+ FAMLI employer share liability begin?

Analysis:
- The FAMLI 10-employee threshold uses a 20-week look-back over the prior calendar year for the current year's classification.
- Because the startup averaged 8 employees in 2024 (prior year), it is a sub-10 employer for ALL of 2025, regardless of the August jump.
- However, for 2026 classification: count the 2025 average over 20 weeks. If the startup is at 10+ for any 20 weeks in 2025 (almost certainly true given the August jump), it is a 10+ employer for 2026 and owes the employer 0.45% beginning January 1, 2026.
- Workpaper MUST document the 2025 20-week count to support the 2026 classification.

Aggregate 2025 employer FAMLI cost: $0 employer share, employee share still withheld throughout.

## 11. Filing Calendar Summary

**Filing Calendar Summary**  _(placeholder)_

:n placeholder

## 12. Self-Checks Before Sign-Off

Before producing reviewer output that incorporates this skill's content, verify:

1. The 4.40% PIT rate is correct for the tax year in scope, and the TABOR-trigger temporary further reduction has not been activated.
2. The SUTA wage base $24,800 and rate schedule 0.50%-10.39% are current; confirm against the latest CDLE-UI rate notice.
3. The FAMLI 10-employee threshold has been computed using national headcount and the 20-week look-back, with the underlying payroll register snapshots retained.
4. EPEWA job posting compliance has been reviewed for any 2025 postings, including remote postings open to Colorado.
5. ABC test analysis for any 1099 contractors with Colorado nexus has walked through ALL THREE prongs, not just relied on contract language.
6. Final pay timing is correct for the separation type (discharge vs resignation).
7. The construction-industry overlay has been considered if the employer's NAICS is in the 23xxxx range.
8. Local OPT (Denver, Aurora, Glendale, Greenwood Village, Sheridan) has been considered for employees working in those jurisdictions — out of scope of this skill but in scope of the workflow.

## 13. Refusal Catalogue (Colorado Payroll Specific)

- **R-CO-PAY-1** — Do not advise reclassifying employees as contractors solely to avoid FAMLI premium — violates C.R.S. §8-13.3-516 anti-retaliation provision.  _(C.R.S. §8-13.3-516)_
- **R-CO-PAY-2** — Do not advise omitting salary range from a Colorado-visible job posting — EPEWA $500-$10,000 per-violation exposure.  _(C.R.S. §8-5-203)_
- **R-CO-PAY-3** — Do not advise "front-loading and clawing back" vacation to defeat Nieto v. Clark's Market — Colorado Wage Act forbids forfeiture of earned vacation.  _(Nieto v. Clark's Market)_
- **R-CO-PAY-4** — Do not advise withholding Colorado tax from a non-resident remote employee who performs no services in Colorado; this creates an over-withholding compliance posture for the employee.  _(Skill refusal catalogue)_
- **R-CO-PAY-5** — Do not advise treating the FAMLI threshold as Colorado-only headcount — it is national.  _(Skill refusal catalogue)_

## 14. Citation Discipline

- **Citation requirements** — Citations in workpapers produced from this skill MUST identify: - C.R.S. section number for substantive statutory rules. - CDOR DR-number for forms and the relevant Income tax publication (Income 70 for withholding; FYI Income 11 for Colorado source income). - CDLE INFO number for HFWA (INFO 6B), EPEWA (INFO 9), and FAMLI (INFO 17 series) interpretive guidance. - The case name and citation for Nieto v. Clark's Market, 488 P.3d 1140 (Colo. 2021) when discussing vacation forfeiture. When citing a 2025 rate, identify the source publication date and the URL or document reference. Reviewers must verify rates against the live CDOR/CDLE publications before sign-off because Colorado revenue rates change with TABOR triggers and the SUTA schedule publishes annually.  _(Nieto v. Clark's Market, 488 P.3d 1140 (Colo. 2021))_

## 15. Skill Slot Contract

- **Slot satisfaction and dependencies** — This skill SATISFIES the `state-payroll` slot for jurisdiction US-CO in the us-tax-workflow-base v0.2 workflow. It DEPENDS ON: - `us-tax-workflow-base` v0.2 or later (workflow architecture). - `us-payroll-fundamentals` (federal payroll baseline; planned). It is COMPLEMENTED BY (load alongside for full Colorado payroll): - `co-income-tax` (employee/owner-side Colorado PIT — already in the package). - `co-local-opt` (Denver/Aurora/Glendale/Greenwood Village/Sheridan occupational privilege taxes; planned). - `co-securesavings` (state retirement registration mandate; planned). - `co-prevailing-wage` (HB 21-1264 prevailing wage; planned). End of co-payroll v0.1.

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
