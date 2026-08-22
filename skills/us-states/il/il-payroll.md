---
name: il-payroll
description: Tier 2 Illinois content skill for employer payroll compliance covering tax year 2025. Includes the 4.95% flat PIT, supplemental 4.95%, IL-941 quarterly withholding, IL UI wage base $13,590 with rates 0.85-8.65%, the Secure Choice Savings Program auto-enroll mandate for 5+ employees (5% default deferral if no qualified retirement plan offered), Chicago Fair Workweek Ordinance predictive scheduling for 10+ employees in covered industries, Cook County paid sick leave, and the One Day Rest in Seven Act.
jurisdiction: US-IL
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: A licensed accountant (name withheld at their request)
review_status: current
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# IL Payroll

## Illinois Payroll Compliance — Tax Year 2025

This skill covers employer payroll obligations under Illinois law for tax year 2025. It complements `us-federal-payroll` (federal withholding, FICA, FUTA, Form 941, W-2) and assumes the federal layer has already been resolved. Illinois imposes a flat personal income tax, a separate unemployment insurance system administered by IDES, a state-mandated retirement program (Secure Choice), and a layered set of labor standards including the One Day Rest in Seven Act and, in Chicago and Cook County, predictive scheduling and paid sick leave ordinances. The reviewer must hold an Illinois-relevant credential (CPA, EA with state experience, or licensed payroll specialist) and sign off before any return or filing is submitted.

The reviewer-oriented output for this skill is a payroll memo identifying every Illinois-specific obligation triggered by the employer's headcount, location, industry, and worker classification, with the dollar amounts and filing deadlines for each obligation in the 2025 plan year.

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **a licensed accountant** on 2026-06-03.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### IL Payroll

- **IL PIT flat rate** — 4.95% on all wages  _(35 ILCS 5/201; Booklet IL-700-T.)_
- **Personal exemption (payroll)** — $2,850 for 2025 (the 2025 IL-700-T withholding allowance reflects $2,850; $2,775 was 2024)  _(IDOR FY2025-16; 2025 Booklet IL-700-T.)_
- **Supplemental wage rate** — IL withholds 4.95% on all wages, including supplemental pay (no separate supplemental rate)  _(Booklet IL-700-T; 86 Ill. Admin. Code 100.7110.)_
- **Annual (≤ $1,000 prior year)** — IL has no 'annual' withholding payment schedule. Illinois has only two payment schedules - monthly and semi-weekly. IL-941 is filed quarterly. ($1,000 is not an IL withholding deposit threshold.)  _(IDOR Pub-131; 2025 IL-941 instr.)_
- **Quarterly ($1,001–$12,000)** — No 'quarterly' payment schedule exists. Employers whose look-back withholding was <= $12,000 are MONTHLY payers (Form IL-501 by the 15th of the following month) and file IL-941 quarterly.  _(IDOR Pub-131; 2025 IL-941 instr.)_
- **Monthly (> $12,000)** — Threshold reversed: monthly applies when look-back withholding is <= $12,000 (not > $12,000). Monthly payers remit by the 15th of the following month (that due date is correct).  _(IDOR Pub-131; 2025 IL-941 instr.)_
- **Semi-weekly (> $12,000 + $50K+/qtr)** — The semi-weekly schedule is triggered solely by look-back withholding > $12,000; there is no '$50,000/quarter' condition (that is a federal rule). The Wed/Fri remittance mechanics shown are correct.  _(IDOR Pub-131; 2025 IL-941 instr.)_
- **IL-941 due date** — IL-941 is due the LAST DAY of the month following the quarter: April 30, July 31, October 31, January 31.  _(2025 IL-941 instr.)_
- **W-2 e-file deadline** — W-2/W-2c/W-2G must be e-filed to IL by January 31 (waiver via IL-900-EW)  _(2025 IL-941 instr.; IDOR Pub-110.)_
- **1099 e-file deadline** — IL requires required 1099 types to be filed electronically; March 31 aligns with the federal e-file date for most 1099s, but Form 1099-NEC is due January 31.  _(IDOR Pub-110.)_
- **UI taxable wage base** — 2025 IL UI taxable wage base = $13,916 ($13,590 was 2024; 2026 = $14,250)  _(IDES 2025 EA-50 / Historical Rate Chart.)_
- **UI min rate** — 2025 minimum UI rate = 0.750% (0.85% was 2024)  _(IDES 2025 Historical Rate Chart.)_
- **UI max rate** — 2025 maximum UI rate = 7.850% (8.65% was 2024)  _(IDES 2025 Historical Rate Chart.)_
- **New employer — non-construction** — 2025 standard new-employer rate = 3.65% (3.95% was 2024); 3.75% for NAICS sectors 56/99  _(IDES 2025 Historical Rate Chart; Bloomberg Tax 12/2024.)_
- **New employer — construction** — No 2025 construction-specific new-employer rate of 6.45%; the standard 3.65% applies (2025 chart shows construction at the standard rate).  _(IDES 2025 Historical Rate Chart.)_
- **Fund Building Rate** — 2025 Fund Building Rate = 0.550%  _(IDES 2025 Historical Rate Chart.)_
- **State Experience Factor** — 2025 State Experience Factor = 114% (109% is not a recent IL figure; 2024 = 126%, 2023 = 127%)  _(IDES 2025 Historical Rate Chart.)_
- **Trigger** — Coverage applies to Illinois employers with at least 5 employees, in business 2+ years, with no qualified retirement plan. IDOR measures the count by averaging, across all four quarters of the tax year, the number of employees showing non-zero Illinois tax withheld on Schedule P (filed with Form IL-941), not a literal "5+ in every quarter" test.  _(820 ILCS 80/; IDOR Q&A 924; IDOR Informational Bulletin FY2023-09.)_
- **Default deferral** — 5% auto-enroll default (auto-escalates 1%/yr to a 10% cap)  _(820 ILCS 80/; program rules.)_
- **Penalty — Year 1** — $250 per employee, first year of noncompliance  _(820 ILCS 80/85.)_
- **Penalty — Year 2+** — $500 per employee, each subsequent year  _(820 ILCS 80/85.)_
- **PLAWA (statewide paid leave)** — Up to 40 hours paid leave per 12-month period (1 hr per 40 worked)  _(820 ILCS 192/; IDOL.)_
- **Chicago paid leave + sick** — Chicago = 40 hrs paid leave + 40 hrs paid sick = 80 hrs combined (separate banks)  _(Chicago Paid Leave & Paid Sick and Safe Leave Ordinance.)_
- **Pay frequency** — IWPCA requires at least semi-monthly pay (executive/admin/professional may be monthly)  _(820 ILCS 115/3.)_
- **Final pay** — Final compensation due no later than the next regularly scheduled payday  _(820 ILCS 115/5.)_
- **Meal break** — ODRISA: 20-minute meal period for shifts of 7.5+ continuous hours, no later than 5 hours in  _(820 ILCS 140/3.)_
- **Worker classification test** — IL UI uses the ABC test - all three prongs (A, B, C) must be met for independent-contractor status  _(820 ILCS 405/212.)_

## 1. Scope

### 1.1 In scope

- Illinois personal income tax withholding (IL PIT) at the 4.95% flat rate under 35 ILCS 5/201(b) and the supplemental wage withholding under 86 Ill. Adm. Code 100.7110.
- IL-941 Illinois Withholding Income Tax Return (quarterly), the IL-941-X amended return, and the IL-W-3 annual reconciliation.
- IL-W-4 Employee's Illinois Withholding Allowance Certificate, including the basic allowance and the additional allowance for age 65+ and blindness.
- Illinois Unemployment Insurance (IL UI) administered by the Illinois Department of Employment Security (IDES) under the Unemployment Insurance Act, 820 ILCS 405/, including the 2025 taxable wage base of $13,590 and the 2025 contribution rate schedule of 0.85% to 8.65%.
- Illinois Secure Choice Savings Program Act (820 ILCS 80/) covering employer mandate triggers, auto-enrollment mechanics, the 5% default deferral, the penalty schedule under 820 ILCS 80/85, and exemption pathways.
- Chicago Fair Workweek Ordinance (Municipal Code of Chicago § 1-25) for predictive scheduling in covered industries (building services, healthcare, hotels, manufacturing, restaurants, retail, warehouse services) with 100+ employees globally and 50+ Chicago-covered employees.
- Cook County Earned Sick Leave Ordinance and the interaction with the Illinois Paid Leave for All Workers Act (820 ILCS 192/), effective January 1, 2024 statewide.
- Worker classification under the Illinois Employee Classification Act (820 ILCS 185/) for construction and the ABC test in the Unemployment Insurance Act § 212.
- Illinois Wage Payment and Collection Act (820 ILCS 115/) for final pay timing and frequency-of-pay rules.
- One Day Rest in Seven Act (820 ILCS 140/) as amended effective January 1, 2023.

### 1.2 Out of scope

- Federal income tax withholding, FICA, FUTA, Form 941, Form 940, W-2, W-3 — see `us-federal-payroll`.
- Illinois corporate income tax (1.5% personal property replacement tax for partnerships and S-corps; 7% plus 2.5% PPRT for C-corps) — see `il-corporate-income-tax`.
- Workers' compensation insurance under the Illinois Workers' Compensation Act — separate insurance product, not payroll tax.
- Multi-state nexus determination for income tax withholding apportionment beyond Illinois/Indiana reciprocity issues — see `_cross-border/multi-state-payroll-nexus`.
- City of Chicago Personal Property Lease Transaction Tax, Amusement Tax, and other Chicago non-payroll taxes.
- Public sector employers (state agencies, school districts, municipalities) which have separate retirement and benefit rules.
- Agricultural employers — IL UI has a different wage base trigger; consult IDES Pub. 197 directly.
- Domestic household employers — different IL UI threshold ($1,000/quarter); see federal Schedule H first.

## 2. Illinois Personal Income Tax Withholding

### 2.1 Flat rate

- **IL flat individual income tax rate** — 4.95%  _(35 ILCS 5/201(b)(5.4))_

Illinois imposes a flat 4.95% individual income tax under 35 ILCS 5/201(b)(5.4). The rate has been unchanged since July 1, 2017 when SB 9 restored it from the 3.75% rate that prevailed January 1, 2015 to June 30, 2017. The "Fair Tax" graduated-rate constitutional amendment was rejected by voters in November 2020, so the flat rate remains in force for 2025.

Withholding is required on:

- Wages paid for services performed in Illinois.
- Wages paid to Illinois residents for services performed anywhere (subject to the credit for taxes paid to other states on the resident's IL-1040, which does not affect employer withholding).
- Gambling and lottery winnings of $1,000 or more (different rules — see IL Pub. 130).
- Non-employee compensation in certain circumstances (1099-MISC, 1099-NEC) — IL does not generally require withholding on independent contractor payments unless backup withholding applies federally.

### 2.2 Computing withholding — Booklet IL-700-T

- **Percentage method formula** — 1. Determine gross wages for the pay period. 2. Subtract the allowance amount: $2,775 per allowance per year (the basic personal exemption under 35 ILCS 5/204(b) for 2025), prorated by pay period: - Weekly: $2,775 / 52 = $53.37 per allowance - Bi-weekly: $2,775 / 26 = $106.73 per allowance - Semi-monthly: $2,775 / 24 = $115.63 per allowance - Monthly: $2,775 / 12 = $231.25 per allowance 3. Multiply the result by 4.95%. 4. Round to the nearest cent.  _(35 ILCS 5/204(b))_

The Illinois Department of Revenue publishes Booklet IL-700-T (Illinois Withholding Tax Tables) annually. The 2025 edition retains the wage-bracket and percentage methods used since 2017.

> AUDIT FLASH POINT — The Illinois personal exemption amount is indexed annually under PA 102-0700 (2021). The 2025 amount of $2,775 differs from the 2024 amount of $2,775 (no change) and the 2023 amount of $2,425. Using a prior-year exemption causes systematic under-withholding. Verify the current amount against IL Booklet IL-700-T before locking payroll software for the year.

### 2.3 Supplemental wages

- **Supplemental wage withholding methods** — Under 86 Ill. Adm. Code 100.7110, supplemental wages (bonuses, commissions, severance, stock option exercise, retroactive pay) are withheld at the flat 4.95% rate. There is no separate higher rate as in some federal contexts. The employer has two options: - **Aggregate method**: Add the supplemental payment to the regular wages and apply the regular withholding formula. - **Flat-rate method**: Withhold 4.95% on the supplemental payment without regard to allowances. The flat-rate method is administratively simpler and is the dominant practice. Either method satisfies the withholding obligation; the difference is reconciled on the employee's IL-1040 at year-end.  _(86 Ill. Adm. Code 100.7110)_

### 2.4 IL-W-4

Form IL-W-4 (Employee's Illinois Withholding Allowance Certificate) is required from every Illinois employee. The 2025 form has not changed structurally since the 2018 revision following PA 100-0023.

Allowances claimable:

- **Basic allowance**: 1 if the employee cannot be claimed as a dependent on someone else's return.
- **Spouse allowance**: 1 if the spouse cannot be claimed as a dependent on someone else's return and the spouse is not separately employed (or has filed IL-W-4 claiming zero allowances at the other job).
- **Dependent allowances**: 1 per dependent claimed on the employee's federal return.
- **Age 65+**: 1 additional allowance for the employee and 1 for the spouse if applicable.
- **Legally blind**: 1 additional allowance for the employee and 1 for the spouse if applicable.

The IL-W-4 also provides for additional dollar withholding per pay period and for claiming exempt status (if the employee had no IL tax liability in the prior year and expects none in the current year — narrow grounds, typically applicable only to students and very-low-income employees).

If the employer has not received a completed IL-W-4, the employer must withhold as if the employee claimed zero allowances (treating the employee as single with no dependents).

### 2.5 Reciprocity — Iowa, Kentucky, Michigan, Wisconsin

Illinois has reciprocal income tax agreements with Iowa, Kentucky, Michigan, and Wisconsin. Under these agreements, an employee who is a resident of one of those four states but works in Illinois pays income tax only to their state of residence, not to Illinois.

To activate reciprocity, the employee files Form IL-W-5-NR (Employee's Statement of Nonresidence in Illinois) with the Illinois employer. The employer then ceases Illinois withholding and must (depending on the resident state) withhold for the employee's home state, which usually requires the employer to register for withholding in that state.

> AUDIT FLASH POINT — Illinois has NO reciprocity agreement with Indiana. An IL employer with an IN-resident employee working in IL must withhold IL tax. The IN resident then claims a credit for IL tax paid on their IN return. This is a frequent error for employers near the Indiana border (e.g., Calumet City, Lansing, Beecher, Joliet area, Kankakee).

### 2.6 IL-941 quarterly return

- **IL-941 filing requirement** — IL-941 (Illinois Withholding Income Tax Return) is filed quarterly by all Illinois withholding employers regardless of payment frequency.  _(86 Ill. Adm. Code 100.7300)_

**IL-941 due dates by quarter**  _(86 Ill. Adm. Code 100.7300)_

| Quarter | Period | Due Date |
| --- | --- | --- |
| Q1 2025 | January 1 – March 31 | April 30, 2025 |
| Q2 2025 | April 1 – June 30 | July 31, 2025 |
| Q3 2025 | July 1 – September 30 | October 31, 2025 |
| Q4 2025 | October 1 – December 31 | February 2, 2026 (January 31 is a Saturday) |

IL-941 must be filed electronically via MyTax Illinois under 86 Ill. Adm. Code 100.7300. Paper filing is generally not permitted except for waiver-approved hardship filers.

### 2.7 Withholding payment frequency

**Withholding deposit schedule by threshold**

| Schedule | Threshold | Deposit Timing |
| --- | --- | --- |
| **Annual** | $1,000 or less withheld in prior calendar year | With IL-941 for Q4 (Feb 2026) |
| **Quarterly** | More than $1,000 but $12,000 or less in lookback period | With each IL-941 |
| **Monthly** | More than $12,000 in lookback period | 15th of month following payday |
| **Semi-weekly** | More than $12,000 in lookback period AND $50,000+ in a single quarter, OR $100,000+ accumulated in any quarter | Wednesday for Wed-Fri paydays; Friday for Sat-Tue paydays |

- **Lookback period definition** — The lookback period is the 12-month period ending June 30 of the preceding calendar year (so for 2025, the lookback is July 1, 2023 to June 30, 2024). Semi-weekly depositors with a single accumulated liability of $100,000 or more in a quarter must deposit the next banking day under the federal-style "one-day rule," which Illinois has incorporated by reference.

### 2.8 IL-W-3 annual reconciliation

- **IL-W-3 reconciliation process** — The IL-W-3 (Annual Withholding Income Tax Return Reconciliation) is reconciled on the Q4 IL-941 (there is no separate IL-W-3 form for 2025 — the reconciliation is built into the fourth-quarter return and the W-2 transmittal). Employers must: 1. File the Q4 IL-941 by February 2, 2026. 2. Electronically file W-2 copies with IL via MyTax Illinois by January 31, 2026. 3. Electronically file 1099 copies with IL via MyTax Illinois by March 31, 2026 (only those with IL withholding or IL income). The W-2 totals must reconcile to the sum of the four IL-941s for the year. A mismatch generates a notice from IL DOR Compliance Division and triggers a desk audit.

## 3. Illinois Unemployment Insurance (IL UI)

### 3.1 IDES administration and SUTA framework

- **UI subjectivity threshold** — IL UI is administered by the Illinois Department of Employment Security (IDES) under the Unemployment Insurance Act, 820 ILCS 405/. Every employer that pays $1,500 or more in wages in any calendar quarter or that employs at least one worker in 20 different weeks in a calendar year becomes subject to UI tax (820 ILCS 405/205).  _(820 ILCS 405/205)_

### 3.2 2025 wage base and rates

**2025 IL UI wage base and rate table**

| Item | 2025 Value |
| --- | --- |
| Taxable wage base per employee | $13,590 |
| Minimum contribution rate (positive-balance employers) | 0.85% |
| Maximum contribution rate (negative-balance employers) | 8.65% |
| New employer rate (non-construction) | 3.95% |
| New employer rate (construction) | 6.45% |
| Fund Building Rate (component included in the above) | 0.55% |
| State Experience Factor | 109% |

- **New employer rate duration** — These are set by IDES and published annually. The 2024 wage base was $13,590 (unchanged for 2025). Rates apply to the first $13,590 of each employee's calendar-year wages. The new employer rate applies for the first three calendar years of liability or until the employer accumulates sufficient experience to be experience-rated, whichever is later.

### 3.3 Quarterly contribution and wage report

**UI-3/40 due dates by quarter**

| Quarter | Due Date |
| --- | --- |
| Q1 2025 | April 30, 2025 |
| Q2 2025 | July 31, 2025 |
| Q3 2025 | October 31, 2025 |
| Q4 2025 | January 31, 2026 |

- **e-file threshold** — Employers file Form UI-3/40 (Employer's Contribution and Wage Report) quarterly through MyTax Illinois. Employers with 25+ employees in any quarter of the prior calendar year must file electronically.

### 3.4 Successor employer

- **Successor experience rate transfer** — When a business is acquired (asset purchase or stock purchase that constitutes a complete or partial transfer of the trade or business), the successor may take the predecessor's experience rate under 820 ILCS 405/1507. This is generally favorable when the predecessor's rate is below the new-employer rate (3.95%) and unfavorable when above. The transfer is mandatory in certain cases (substantial common ownership) and elective in others (arm's-length purchase) — see IDES Form UI-1S.  _(820 ILCS 405/1507)_

### 3.5 SUTA dumping

- **SUTA dumping penalty** — IDES enforces the federal SUTA Dumping Prevention Act of 2004 (P.L. 108-295) through 820 ILCS 405/1507.1. Knowing transfers of business with the principal purpose of obtaining a lower contribution rate are subject to the maximum rate plus a penalty of 2.0% of the wage base for each year involved.  _(820 ILCS 405/1507.1)_

### 3.6 Voluntary contributions

- **Voluntary contribution mechanics** — An employer may make a voluntary contribution under 820 ILCS 405/1500 to buy down its experience rate. The contribution must be made within 30 days of receiving the annual rate notice (typically mailed in late November or early December for the following calendar year). Voluntary contributions are most often economic when the rate would fall by at least one bracket relative to the cost.  _(820 ILCS 405/1500)_

## 4. Illinois Secure Choice Savings Program

### 4.1 Statutory framework

- **Secure Choice statutory framework** — The Illinois Secure Choice Savings Program Act (820 ILCS 80/) was enacted in 2015, amended by PA 101-0026 in 2019 and PA 102-0179 in 2021. It establishes a state-facilitated payroll-deduction Roth IRA program administered by the Illinois Treasurer's Office. The implementation timeline rolled out from late 2018 to 2023, with the final wave (employers with 5–15 employees) coming online November 1, 2023.  _(820 ILCS 80/)_

### 4.2 Employer mandate

- **Employer mandate triggers** — An employer must register with Secure Choice if all of the following apply: 1. The employer has had **5 or more Illinois employees** in every quarter of the preceding calendar year (under 820 ILCS 80/5, "employer" definition). 2. The employer has been in business for at least **2 years**. 3. The employer does **not offer a qualified retirement plan** in the preceding 2 years (qualified plans include 401(k), 403(b), 408(k) SEP-IRA, 408(p) SIMPLE IRA, 457(b), payroll-deduction IRA under § 7701, and certain defined benefit plans under § 401(a)). Employees who are not Illinois residents and do not work in Illinois are excluded from the headcount. > AUDIT FLASH POINT — The 5-employee threshold was lowered from 25 by PA 102-0179 effective November 1, 2022, with phased compliance dates by employer size. Many small Illinois employers (5–15 employees) are unaware they became subject November 1, 2023. The Illinois Treasurer publishes employer registration notices via the Illinois Secretary of State business registration data; non-registered employers receive enforcement letters with escalating penalties. Verify Secure Choice registration status (or a documented exemption) for every Illinois employer with 5+ employees at the start of any engagement.  _(820 ILCS 80/5)_

### 4.3 Auto-enrollment mechanics

- **Auto-enrollment process** — Once registered, the employer must: 1. Provide each eligible employee with an information packet from Secure Choice within 30 days of hire (or within 30 days of registration for existing employees at first onboarding). 2. Give the employee 30 days to opt out, change the contribution rate, or change the investment allocation. 3. If the employee does not opt out, automatically enroll the employee at the **default 5% deferral rate** of pre-tax wages (the deduction itself is post-tax because Secure Choice is a Roth IRA, but the 5% is computed on gross wages). 4. Remit contributions to the Secure Choice trustee (currently Vestwell) via payroll deduction within 7 business days of each payroll. 5. Provide a default investment in the Target Retirement Date Fund matching the employee's nearest retirement year (age 65 default). The default contribution rate auto-escalates by 1% per year up to a cap of 10%, unless the employee opts out of escalation.

### 4.4 Employer responsibilities and prohibited activities

- **Facilitator-only obligations** — The employer is a **facilitator only**. The employer: - Must NOT contribute to employee accounts (no employer match). - Must NOT serve as a fiduciary or provide investment advice. - Must NOT endorse the program or recommend participation. - Must NOT offer Secure Choice as a substitute for required workplace policies (e.g., final pay, posted wage notices). - Must withhold employee elections and remit timely. - Must maintain employee election records for 6 years. Failure to facilitate does not give the employee a private right of action against the employer.

### 4.5 Penalties

**Secure Choice penalty table**  _(820 ILCS 80/85)_

| Violation | Penalty |
| --- | --- |
| Failure to enroll an employee (first year) | $250 per employee |
| Failure to enroll an employee (each subsequent year) | $500 per employee |

Under 820 ILCS 80/85, the Department of Revenue assesses penalties for non-compliance. The penalty assessment runs cumulatively, so a 10-employee employer that fails to register and remains non-compliant for three years faces $250 + $500 + $500 = $1,250 per employee × 10 = $12,500.

> AUDIT FLASH POINT — Secure Choice penalty assessments are issued by IL DOR and processed through MyTax Illinois. They are not waivable for "reasonable cause" in the same way IRS penalties are; the Treasurer's office and DOR have taken the position that the statute is mandatory. The only relief pathway is to demonstrate that the employer was exempt (qualified plan offered, fewer than 5 employees in every quarter, less than 2 years in business). Maintain documentation of the qualified plan adoption date and the IRS determination letter or prototype adoption document.

### 4.6 Exemption registration

- **Exemption registration process** — Employers that offer a qualified plan or otherwise do not meet the criteria must affirmatively register their exemption through the Illinois Secure Choice employer portal (employer.ilsecurechoice.com). Filing the exemption clears the employer from the enforcement workflow. Re-confirmation is required annually.

## 5. Chicago Fair Workweek Ordinance

### 5.1 Coverage trigger

- **Fair Workweek coverage trigger and covered industries** — The Chicago Fair Workweek Ordinance (Municipal Code of Chicago § 1-25) took effect July 1, 2020 (delayed from July 1, 2020 due to COVID, fully enforced from January 1, 2021). It applies to employers with: - **100 or more employees globally** (250+ for nonprofits), AND - **50 or more employees who perform work in Chicago in covered industries**. Covered industries: 1. Building services 2. Healthcare 3. Hotels 4. Manufacturing 5. Restaurants (250+ employees and 30+ Chicago locations for restaurant trigger) 6. Retail 7. Warehouse services  _(MCC § 1-25)_

### 5.2 Predictive scheduling requirements

- **Predictive scheduling and predictability pay rules** — For covered employees earning $30.99/hour or less or $61,149.35/year or less (2025 amounts indexed annually), the employer must: 1. **Provide a good-faith estimate of work schedule** at time of hire — typical days per week, hours per week, expected start/end times. 2. **Post schedule 14 days in advance** (the ordinance increased the advance notice from 10 days to 14 days effective July 1, 2022). 3. **Pay predictability pay** for changes to the posted schedule: - **1 hour of pay at the regular rate** for changes that add or subtract hours within 14 days but with at least 24 hours' notice. - **No-fault pay equal to 50% of lost hours** if a shift is cancelled or hours are subtracted with less than 24 hours' notice. - **1 hour additional pay** for added shifts with less than 14 days' notice. 4. **Right to decline** previously unscheduled hours added with less than 14 days' notice without retaliation. 5. **Right to rest** — employees may decline a shift that begins less than 10 hours after the end of the previous shift; if accepted, the hours are paid at 1.25× the regular rate.  _(MCC § 1-25)_

### 5.3 Recordkeeping and posting

- **Recordkeeping requirements** — Employers must: - Post the Fair Workweek notice (issued by the Chicago Department of Business Affairs and Consumer Protection, BACP) in the workplace. - Maintain schedule records, predictability pay records, and good-faith estimates for **3 years**. - Provide records to employees upon written request within 21 days.

### 5.4 Penalties

**Fair Workweek penalty table**

| Violation | Penalty |
| --- | --- |
| First violation | $300–$500 per violation per employee per day |
| Subsequent violations | Up to $500 per violation per employee per day |
| Private right of action | Yes, after exhausting BACP administrative remedies; double damages plus attorney's fees available |

> AUDIT FLASH POINT — Fair Workweek violations are commonly under-detected because employees often do not know their predictability-pay rights. BACP enforcement actions have accelerated since 2023, and the City has signaled the restaurant industry as a 2025 enforcement priority. Even an employer "near" the threshold (e.g., 95 employees globally) should be advised to implement the ordinance proactively because crossing the threshold mid-year does not provide a grace period. Class actions and PAGA-style aggregations are increasing.

### 5.5 Carve-outs

- **Ordinance exclusions** — The ordinance does not apply to: - Employees covered by a collective bargaining agreement that explicitly waives the Fair Workweek provisions (and the waiver must be specific, not general). - Employees of city, state, or federal government. - Independent contractors properly classified under the ABC test (see Section 7).

## 6. Cook County Paid Sick Leave and Illinois Paid Leave for All Workers Act

### 6.1 Illinois Paid Leave for All Workers Act (statewide)

- **PLAWA statewide requirements** — Effective January 1, 2024, the Paid Leave for All Workers Act (820 ILCS 192/) requires nearly every Illinois employer to provide **40 hours of paid leave per 12-month period** that employees may use for any reason without justification. For 2025 this continues unchanged. Key features: - Accrual: 1 hour per 40 hours worked, OR front-loaded 40 hours at the start of the 12-month period. - Carry-over: Accrued hours must carry over (up to the 40-hour annual usage cap), unless the employer front-loads. - Use: Employees may begin using leave 90 days after employment starts. - No payout at termination required (unlike the Illinois Vacation Pay rule under 820 ILCS 115/5). - Cook County and Chicago have separate, more generous ordinances that preempt PLAWA within their boundaries.  _(820 ILCS 192/)_

### 6.2 Cook County Earned Sick Leave Ordinance

- **Cook County sick leave accrual and use rules** — The Cook County Paid Sick Leave Ordinance (Cook County Code § 42-2) applies to all employers with at least one employee working in unincorporated Cook County or in a Cook County municipality that has NOT opted out. Many Cook County municipalities did opt out in 2017-2018, but the trend has reversed since the 2024 statewide PLAWA mandate, and several municipalities have re-opted in. Accrual and use rules largely mirror Chicago's ordinance: - 1 hour earned per 40 hours worked. - Cap: 40 hours per 12-month period (60 hours under Chicago's ordinance — see § 6.3). - Use within 80 hours rolling, must be allowed for self, family member, domestic violence, public health emergency.  _(Cook County Code § 42-2)_

### 6.3 Chicago Paid Leave and Paid Sick Leave Ordinance

- **Chicago combined paid leave rules** — Effective July 1, 2024 (delayed from December 31, 2023 by the Chicago City Council), the Chicago ordinance now provides: - **40 hours of paid sick leave** per year (uses similar to Cook County). - **40 hours of paid leave for any reason** per year (similar to PLAWA). - Together, 80 hours of paid leave per year for Chicago employees. Payout at termination is required for the paid-leave-for-any-reason portion (40 hours) for employers with 51+ employees. The paid sick leave portion is not paid out. > AUDIT FLASH POINT — The Chicago ordinance is the most generous in Illinois. Employers with mixed Chicago / non-Chicago Illinois employees must track location of work weekly and apply the correct ordinance. The "majority of work performed in Chicago" test does not apply — it is per-hour. A Cook County employee who occasionally works in Chicago accrues at the Chicago rate for those hours.  _(MCC § 1-24)_

## 7. Worker Classification

### 7.1 Illinois UI Act ABC test

- **ABC test prongs** — Under 820 ILCS 405/212, a worker is presumed to be an employee for unemployment insurance purposes unless the employer proves ALL THREE prongs: - **(A)** The individual is free from control and direction over the performance of the work, both under contract and in fact. - **(B)** The work is performed either outside the usual course of business of the employer OR outside all of the employer's places of business. - **(C)** The individual is engaged in an independently established trade, occupation, profession, or business. The Illinois ABC test is among the strictest in the country. IDES applies it aggressively in audits.  _(820 ILCS 405/212)_

### 7.2 Illinois Employee Classification Act (construction)

- **Construction classification standard and penalties** — Under 820 ILCS 185/, the construction industry has an even stricter classification standard. A construction worker is conclusively presumed an employee unless the employer can prove the worker is a separate business entity meeting 12 enumerated factors (sole proprietor with own license, separate office, multiple clients, performs services for the public, files taxes as a business, etc.). The 12-factor test for sole proprietors operating as bona fide independent businesses is in 820 ILCS 185/10(c). Penalties for misclassification under the Employee Classification Act: - $1,500 per violation per day per worker for the first audit. - $2,500 per violation per day per worker for subsequent audits within 5 years. - Personal liability for corporate officers who knowingly misclassify. - Debarment from public contracts for 5 years for willful violators. > AUDIT FLASH POINT — The Illinois Department of Labor and IDES coordinate cross-referrals on classification audits. A worker who files for unemployment after being terminated as a "contractor" often triggers an IDES audit that propagates to IL DOR (withholding) and IDOL (Construction Act). Three agencies, three penalty regimes, one bad classification. Maintain contemporaneous 1099 vs W-2 analysis files for every contractor, refreshed at least annually.  _(820 ILCS 185/; 820 ILCS 185/10(c))_

### 7.3 Withholding for non-residents working in Illinois temporarily

- **No de minimis rule** — Illinois does not have a "30-day" or "60-day" de minimis non-resident withholding rule. Withholding is required from the first day a non-resident (non-reciprocity-state) employee works in Illinois unless the IL-W-5-NR is on file (and only IA, KY, MI, WI residents may file IL-W-5-NR).

## 8. Final Pay and Other Wage Standards

### 8.1 Final pay timing

- **Final pay and vacation payout rules** — Under the Illinois Wage Payment and Collection Act (820 ILCS 115/5), final compensation must be paid: - **By the next regularly scheduled payday** following separation, regardless of whether the separation is voluntary or involuntary. - Earned but unused **vacation must be paid out** at the final rate of pay (820 ILCS 115/5 — Illinois treats earned vacation as wages). - PLAWA paid leave does NOT have to be paid out. - Chicago paid leave (40 hours of paid-leave-for-any-reason) MUST be paid out by employers with 51+ employees. A discharged employee may demand final compensation be paid sooner, but the employer has until the next payday to comply without penalty.  _(820 ILCS 115/5)_

### 8.2 Frequency of pay

- **Pay frequency rules** — Under 820 ILCS 115/3, wages must be paid: - At least **semi-monthly** for most employees. - **Monthly** for executive, administrative, and professional employees under FLSA exemptions, and for outside salespersons. - Within **13 days** after the end of the pay period (semi-monthly) or 21 days (monthly).  _(820 ILCS 115/3)_

### 8.3 One Day Rest in Seven Act

- **ODRISA rest, meal break, exemption, and penalty rules** — Under 820 ILCS 140/, as amended by PA 102-0828 effective January 1, 2023, every employer must provide every employee: - **At least 24 consecutive hours of rest in every consecutive 7-day period** (not every calendar week). - A **20-minute meal break** for every 7.5-hour work period, with an additional 20-minute break for every 4.5 hours worked beyond 7.5. - Written notice of these rights via a poster (IDOL provides the template). Exemptions: agricultural workers, certain healthcare workers under collective bargaining, employees in a "supervisory capacity," part-time employees working less than 20 hours/week (limited). Voluntary waivers of the rest day are permitted only if the employer petitions IDOL for permission and shows undue hardship. Penalties under PA 102-0828: - $250–$500 per offense per employee (employers with fewer than 25 employees). - $250–$500 per offense per employee plus a $100–$250 additional damages payable to the employee (employers with 25+ employees).  _(820 ILCS 140/; PA 102-0828)_

### 8.4 Construction industry drug testing

- **Substance abuse prevention program requirements** — Under 820 ILCS 265/ (Substance Abuse Prevention on Public Works Projects Act), contractors on Illinois public works projects must implement a substance abuse prevention program meeting minimum standards. This is not a payroll tax but a labor compliance obligation that affects: - Pre-employment drug testing requirements. - Random testing protocols (10% of workforce annually minimum). - Reasonable suspicion testing and post-accident testing. - The interaction with the Illinois Cannabis Regulation and Tax Act (410 ILCS 705/) — cannabis use off-duty is generally lawful but may still disqualify a worker from federally regulated construction roles.  _(820 ILCS 265/)_

### 8.5 Other notable payroll-adjacent obligations

- **Additional wage and pay statutes** — - **Wage Theft Enforcement Act** (820 ILCS 115/14) — willful refusal to pay wages is a Class A misdemeanor; repeat offenses are Class 4 felonies. - **Illinois Equal Pay Act** (820 ILCS 112/) — wage discrimination prohibitions; PA 101-0656 added pay data reporting for employers with 100+ employees (EEO-1 alignment). - **Illinois Pay Transparency Law** (effective January 1, 2025 under PA 103-0539) — employers with 15+ employees must include pay scale and benefits in job postings.  _(820 ILCS 115/14; 820 ILCS 112/; PA 103-0539)_

## 9. Worked Examples

### Example 1 — Illinois employer with 10 employees, Secure Choice trigger

**Facts**: Greenbridge Marketing LLC is a Chicago-based marketing firm with 10 Illinois W-2 employees, in business since 2019, with no retirement plan. The owner is unaware of the Secure Choice mandate. The firm's 2025 gross payroll is $850,000.

**Analysis**:

1. **Secure Choice mandate**: Greenbridge has 5+ employees in every quarter of 2024, has been in business more than 2 years, and offers no qualified plan. Greenbridge is required to register and facilitate Secure Choice for all 10 employees.

2. **Registration deadline**: The compliance date for 5–15 employee employers was November 1, 2023. Greenbridge is currently two full years out of compliance.

3. **Penalty exposure**: Year 1 (2024): $250 × 10 = $2,500. Year 2 (2025, ongoing): $500 × 10 = $5,000. Total potential penalty: **$7,500** if assessed retroactively.

4. **Remediation plan**:
   - Register immediately at employer.ilsecurechoice.com.
   - Provide information packets to all 10 employees within 30 days of registration.
   - Begin payroll deductions at the 5% default rate (employee opt-out window: 30 days).
   - Document the late compliance and request penalty abatement (limited success expected; the statute provides no "reasonable cause" exception, but the Treasurer's office has shown some flexibility for employers who self-remediate before a notice of assessment is issued).

5. **Alternative**: If Greenbridge prefers, it may adopt a SEP-IRA, SIMPLE IRA, 401(k), or other qualified plan and register the exemption. A SEP-IRA can be adopted as late as the extended return due date for 2025 with no plan document filing fee. The owner-employees often prefer a qualified plan because it permits employer contributions and higher individual deferrals.

6. **IL withholding**: Independent of Secure Choice, Greenbridge is withholding IL PIT at 4.95% on all 10 employees and filing IL-941 quarterly with the Q4 IL-W-3 reconciliation built into the Q4 return.

7. **IL UI**: 10 employees × $13,590 wage base = $135,900 total taxable wages. At the new-employer rate of 3.95% (assuming Greenbridge has not yet earned an experience rating because it had no employees pre-2022), 2025 UI tax = $5,368. By 2026 Greenbridge will have an experience rating and the rate may drop to as low as 0.85% if no UI claims were filed.

### Example 2 — Multi-state employer with Illinois/Indiana border employees

**Facts**: Lakeshore Logistics Inc. operates a warehouse in Hammond, Indiana, just east of the Illinois border. The company has 60 employees: 35 work at the Indiana warehouse (15 are Illinois residents, 20 are Indiana residents), and 25 work at a satellite distribution center in Calumet City, Illinois (10 are Illinois residents, 15 are Indiana residents).

**Analysis**:

1. **No IL/IN reciprocity**: Illinois has reciprocity agreements with Iowa, Kentucky, Michigan, and Wisconsin only. Indiana is NOT a reciprocity state. This means:
   - Illinois residents who work in Indiana: Indiana withholds IN tax; the IL resident claims a credit for IN tax paid on the IL-1040. Lakeshore must withhold IN tax (3.05% state + applicable Indiana county tax based on the employee's Indiana county of principal employment, or county of residence if no IN county of employment).
   - Indiana residents who work in Illinois: Illinois withholds IL tax at 4.95%. The IN resident claims a credit for IL tax paid on the IN-40, capped at the IN tax rate (3.05% + county).

2. **Withholding registration**: Lakeshore needs to be registered for both IL withholding (with IL DOR) and IN withholding (with IN DOR). It must file IL-941 quarterly and IN WH-1 monthly (Indiana defaults to monthly).

3. **IL UI**: The 25 employees physically working at the Calumet City facility are reported to IDES for unemployment, regardless of state of residence (UI is based on physical location of work). $13,590 × 25 = $339,750 taxable IL wages. At the new-employer rate (3.95% if first year) = $13,420 IL UI.

4. **IN UI**: The 35 employees working at the Hammond facility are reported to Indiana DWD for unemployment. (Indiana 2025 wage base: $9,500.)

5. **Localization rules for UI**: When an employee works in both states (e.g., a driver), the "localization of services" test under § 3304(a)(4) of the federal SUTA framework determines which state's UI covers the employee. Lakeshore should adopt a written policy assigning each multi-state-working employee to a primary state based on (1) where most work is performed, (2) base of operations, (3) place of direction and control, (4) residence — applied in order.

6. **Secure Choice**: The 25 Calumet City employees count toward the 5-employee threshold (they are Illinois employees because they work in Illinois, regardless of residence). The 35 Hammond employees do not count (Indiana employer-employee relationship). Lakeshore is well over the threshold based on Calumet City alone, so it must register for Secure Choice (or offer a qualified plan and register the exemption).

7. **Chicago Fair Workweek**: Calumet City is NOT in Chicago, so the Chicago ordinance does not apply. Cook County paid sick leave DOES apply because Calumet City is in Cook County (and has not opted out of the Cook County ordinance for the period in question — confirm current municipal status at the Cook County Clerk's office).

8. **IL Paid Leave for All Workers Act**: Applies to all 25 Calumet City employees (40 hours/year, accrual or front-load). Does not apply to the 35 Hammond employees (Indiana law governs).

9. **One Day Rest in Seven Act**: Applies to all 25 Calumet City employees, including the 15 Indiana residents who work in IL.

10. **Net IL payroll tax burden for 2025** (Calumet City facility only, illustrative):
    - IL PIT withheld on 25 employees: depends on wages, but at $50,000 average gross and $2,775 personal exemption, withholding ≈ 4.95% × ($50,000 – $2,775) = $2,338 per employee × 25 = **$58,440 IL PIT remitted via IL-941**.
    - IL UI: **$13,420** as computed above (year 1; will adjust).
    - Total IL employer-side cost: $13,420 UI plus Secure Choice administrative facilitation (no employer cost).

### Example 3 — Contractor misclassification challenge under the ABC test

**Facts**: Northshore Construction Co. is a residential remodeling contractor in Evanston. It engages 12 carpenters as 1099 contractors. Each carpenter (1) signed a contract stating they are independent contractors, (2) provides their own hand tools but uses Northshore's lumber, scaffolding, and power tools on each job, (3) is told which jobsite to report to and what work to do that day by the Northshore project manager, (4) works exclusively for Northshore in the current and prior calendar year, and (5) is paid an hourly rate of $35 with no benefits. One carpenter, Mr. Diaz, is terminated and files for unemployment. IDES initiates an audit.

**Analysis**:

1. **UI Act § 212 ABC test applied**:

   - **Prong A — Free from control and direction**: FAIL. The carpenters are told which jobsite, what work, and what hours. Northshore's project manager supervises daily. Northshore controls both the result and the means.

   - **Prong B — Outside usual course of business OR outside all places of business**: FAIL. Carpentry IS the usual course of business of a residential remodeling contractor. The work is performed at customer jobsites which are Northshore's places of business by extension under Illinois case law (Carpetland U.S.A. v. IDES, 776 N.E.2d 166 (Ill. 2002)).

   - **Prong C — Independently established trade**: FAIL. The carpenters work exclusively for Northshore with no other clients, no separate business name, no own customers, no business cards, no commercial general liability insurance, and no separate workers' compensation policy.

2. **Conclusion**: All 12 carpenters are employees for UI purposes. IDES will reclassify retroactively and assess UI contributions on all wages paid.

3. **Cascading consequences**:

   - **UI back contributions** (Northshore's potential exposure): If average annual wages per carpenter are $70,000 over 2023, 2024, 2025 (3 years × 12 carpenters × $13,590 wage base × ~3.95% new-employer rate or higher experience rate after Diaz's claim is paid) — approximately $19,330 in UI back-contributions, plus interest at 1.5% per month and penalties under 820 ILCS 405/2206 of up to 25% of unpaid contributions.

   - **IL PIT withholding back-assessment**: IL DOR is cross-referred. 12 carpenters × $70,000 average × 3 years × 4.95% = $124,740 in IL PIT that should have been withheld. The employer is jointly and severally liable under 35 ILCS 5/704A. Penalty under 35 ILCS 735/3 of 15% of the underwithheld amount, plus interest.

   - **Employee Classification Act (construction) penalty**: 820 ILCS 185/40 — $1,500 per day per worker × ~750 working days × 12 workers = potentially **$13.5 million theoretical maximum**, though IDOL typically settles for a fraction. Personal liability attaches to corporate officers.

   - **Federal liability**: Backup withholding, FICA back-assessment, FUTA, IRS § 3509 reduced rates if there's no intentional disregard (the lack of 1099 filing in some years may eliminate the § 3509 relief).

   - **Workers' compensation**: Northshore likely did not carry comp on the reclassified workers, exposing it to liability for past injuries plus penalties under 820 ILCS 305/4.

   - **Wage Payment Act**: If any unpaid overtime owed under FLSA exists, it is now actionable under 820 ILCS 115/14 (Class A misdemeanor for willful nonpayment).

4. **Remediation**: There is no clean retroactive fix once the audit has started. Northshore should:
   - Engage Illinois employment counsel immediately.
   - Consider IRS Voluntary Classification Settlement Program (VCSP) for federal exposure (cannot use if under audit at any level).
   - Reclassify going forward to W-2.
   - Adopt a workers' comp policy.
   - Register for Secure Choice (with 12+ employees, mandate clearly triggered).
   - Begin IL UI quarterly filings; switch to IL-941 reporting; consider voluntary disclosure to IDES under 820 ILCS 405/2207 for limited penalty relief.

5. **Reviewer note**: Document the ABC analysis contemporaneously for every contractor engagement going forward. The cost of getting this wrong in Illinois is among the highest in the country because of the layered Construction Act penalty regime stacked on top of UI and PIT assessments.

## 10. Quick Reference Table — 2025 Illinois Payroll

**Quick reference table**

| Item | 2025 Value | Citation |
| --- | --- | --- |
| IL PIT flat rate | 4.95% | 35 ILCS 5/201(b)(5.4) |
| Personal exemption | $2,775 | 35 ILCS 5/204(b); IL Pub. 130 |
| Supplemental wage rate | 4.95% | 86 Ill. Adm. Code 100.7110 |
| IL UI wage base | $13,590 | IDES Rate Determination 2025 |
| IL UI minimum rate | 0.85% | IDES |
| IL UI maximum rate | 8.65% | IDES |
| New employer rate (non-construction) | 3.95% | IDES |
| New employer rate (construction) | 6.45% | IDES |
| Secure Choice trigger | 5+ IL employees, 2+ years in business, no qualified plan | 820 ILCS 80/30 |
| Secure Choice default deferral | 5% | 820 ILCS 80/55 |
| Secure Choice penalty | $250/employee Y1, $500/employee Y2+ | 820 ILCS 80/85 |
| Chicago Fair Workweek trigger | 100+ global, 50+ Chicago, covered industry | MCC § 1-25-040 |
| Fair Workweek covered worker cap | $30.99/hr or $61,149.35/yr | BACP 2025 update |
| Cook County paid sick leave accrual | 1 hr per 40 worked | Cook County Code § 42-2 |
| PLAWA (statewide) | 40 hrs paid leave/year | 820 ILCS 192/15 |
| Chicago paid leave + sick (combined) | 80 hrs/year | MCC § 1-24 |
| Final pay deadline | Next regular payday | 820 ILCS 115/5 |
| One Day Rest in Seven | 24 consec hrs per 7-day period | 820 ILCS 140/2 |
| Meal break | 20 min per 7.5 hrs | 820 ILCS 140/3 |
| ABC test | All 3 prongs required | 820 ILCS 405/212 |
| Construction misclassification penalty | $1,500/day/worker first; $2,500 subsequent | 820 ILCS 185/40 |
| IL-941 due date | 30 days after quarter-end | 86 Ill. Adm. Code 100.7300 |
| W-2 e-file with IL | January 31 | IL DOR |
| 1099 e-file with IL | March 31 | IL DOR |
| Pay frequency | Semi-monthly minimum | 820 ILCS 115/3 |

## 11. Provenance and Citations

### Statutory authority

- 35 ILCS 5/ — Illinois Income Tax Act (4.95% flat rate, withholding rules)
- 820 ILCS 80/ — Illinois Secure Choice Savings Program Act (PA 99-0008 as amended by PA 101-0026 and PA 102-0179)
- 820 ILCS 115/ — Illinois Wage Payment and Collection Act
- 820 ILCS 140/ — One Day Rest in Seven Act (as amended by PA 102-0828)
- 820 ILCS 185/ — Employee Classification Act (construction)
- 820 ILCS 192/ — Paid Leave for All Workers Act (effective January 1, 2024)
- 820 ILCS 405/ — Unemployment Insurance Act, including § 212 (ABC test) and § 1507 (successor liability)
- 820 ILCS 265/ — Substance Abuse Prevention on Public Works Projects Act
- 820 ILCS 305/ — Workers' Compensation Act

### Administrative rules

- 86 Ill. Adm. Code 100.7110 — Supplemental wage withholding
- 86 Ill. Adm. Code 100.7300 — Withholding return filing
- 56 Ill. Adm. Code 2760 — IDES contribution rate determination

### Municipal ordinances

- Municipal Code of Chicago § 1-24 — Chicago Paid Leave and Paid Sick Leave Ordinance (as amended effective July 1, 2024)
- Municipal Code of Chicago § 1-25 — Chicago Fair Workweek Ordinance (as amended effective July 1, 2022)
- Cook County Code § 42-2 — Cook County Earned Sick Leave Ordinance

### Agency publications

- IL DOR Booklet IL-700-T (2025) — Illinois Withholding Tax Tables
- IL DOR Publication 130 (2025) — Who is Required to Withhold Illinois Income Tax
- IL DOR Publication 131 (2025) — Withholding Income Tax Payment and Filing Requirements
- IDES Rate Determination 2025 — Annual rate schedule notice
- Illinois Treasurer's Office, Secure Choice Employer Handbook (2024 edition)
- City of Chicago BACP, Fair Workweek Ordinance Rules and Regulations (2024 update)
- Cook County Commission on Human Rights, Earned Sick Leave Interpretive and Procedural Rules (2024)
- IL DOL, One Day Rest in Seven Act Guidance (revised 2023 following PA 102-0828)

### Case law

- Carpetland U.S.A., Inc. v. IDES, 776 N.E.2d 166 (Ill. 2002) — leading case interpreting the ABC test
- AFM Messenger Service v. IDES, 763 N.E.2d 272 (Ill. 2001) — Prong B "usual course of business" interpretation
- People ex rel. Dep't of Labor v. MCC Home Health Care, 339 Ill. App. 3d 10 (1st Dist. 2003) — joint employer doctrine

### Recent legislative changes affecting 2025

- PA 103-0539 (effective January 1, 2025) — Illinois Pay Transparency requirements for employers with 15+ employees
- PA 103-0201 (2023) — Domestic workers expressly covered under PLAWA
- PA 102-0828 (effective January 1, 2023) — One Day Rest in Seven Act amendments increasing penalties and expanding meal break rules
- PA 102-0179 (2021, fully effective November 1, 2023) — Secure Choice expansion to 5-employee threshold

### Verification status

This skill is marked `verified_by: pending`. Before publication, the reviewer must:

1. Confirm the 2025 IL PIT personal exemption amount of $2,775 against the published IL-700-T booklet.
2. Confirm the 2025 IDES rate schedule (0.85% – 8.65%, wage base $13,590) against the IDES public rate determination.
3. Confirm the current Cook County opt-out status for any municipality where the client has employees.
4. Confirm the current Secure Choice employer registration data via the Treasurer's portal.
5. Sign off as an Illinois-credentialed reviewer (CPA, EA with Illinois practice, or licensed payroll specialist).

End of skill.

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
