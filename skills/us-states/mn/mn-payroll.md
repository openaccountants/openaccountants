---
name: mn-payroll
description: Minnesota Payroll Compliance Skill (Tax Year 2025)
jurisdiction: US-MN
domain: state-tax
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# mn-payroll

## 1. Scope

This skill covers Minnesota state-level payroll tax and labor-law compliance for employers with one or more workers performing services in Minnesota during tax year 2025, with forward-looking guidance for the 2026 transition to the Minnesota Paid Leave program. It is designed to be loaded alongside `us-federal-payroll` (FICA, FUTA, federal withholding, Form 941, Form 940, W-2/W-3 federal copy) and any sibling state skills where the employer operates in more than one jurisdiction.

In scope:

- Minnesota Personal Income Tax (PIT) withholding under Minnesota Statutes Chapter 290, including the 2025 graduated bracket schedule and the supplemental withholding rate.
- Form W-4MN, the Minnesota Employee Withholding Allowance/Exemption Certificate, including the conditions under which an employer must require it instead of, or in addition to, federal Form W-4.
- Minnesota Department of Revenue (DOR) withholding deposit and return mechanics (Form MW-1 deposits, Form MWR information return, year-end W-2/W-3 reconciliation by January 31).
- Minnesota Unemployment Insurance (UI) under Minnesota Statutes Chapter 268, administered by the Department of Employment and Economic Development (DEED), including the 2025 taxable wage base of $43,000, experience-rated and new-employer rate schedules, and the quarterly UI wage detail/tax return.
- Minnesota Earned Sick and Safe Time (ESST) under Minnesota Statutes §181.9445–§181.9448 (effective January 1, 2024, with the 2024 expansion bringing it to a statewide mandate covering virtually all private employers).
- Minnesota Paid Leave under Minnesota Statutes Chapter 268B (enacted by 2023 Laws Ch. 59, amended by 2024 Laws Ch. 127): a state-administered paid family and medical leave program funded by a payroll premium, with employer reporting beginning in 2024 and benefit payments and premium collection beginning **January 1, 2026**. This is the single largest 2026 transition item for Minnesota employers.
- Wage Theft Prevention Act (WTPA) under Minnesota Statutes §181.032 and §181.101, including the written wage notice required at hire and on any material change.
- Worker classification (employee vs. independent contractor) under Minnesota's 9-factor common-law/economic-realities test as administered by DEED for UI purposes, the parallel test for state withholding, and the heightened construction-industry standard under Minnesota Statutes §181.723.
- Construction-industry-specific compliance: the Independent Contractor Exemption Certificate (ICEC) regime, the registration requirements for construction contractors, and the role of the Minnesota Department of Labor and Industry (DLI). Older practitioner shorthand sometimes references this as "Carlson certification" after the 2012 reforms; the operative regime today is the DLI ICEC / construction contractor registration framework under §181.723 and §326B.
- Final pay timing under Minnesota Statutes §181.13 and §181.14 (separation by employer vs. voluntary resignation), and the closely related rules on commissions and accrued PTO.

Out of scope (handled by other skills or expressly excluded):

- Federal income tax withholding, FICA, FUTA, ACA reporting → see `us-federal-payroll`.
- Minnesota corporate income tax (M4) and pass-through entity tax → see `us-mn-business-tax`.
- Minnesota sales and use tax → see `us-mn-sales-tax`.
- Local-level employment ordinances (e.g., Minneapolis and Saint Paul earned sick and safe time ordinances, Minneapolis minimum wage ordinance, Saint Paul minimum wage ordinance, the Minneapolis Wage Theft Prevention Ordinance). These local rules layer on top of the state ESST and WTPA and are addressed in the companion local-ordinance addendum (`us-mn-local-ordinances`), not here.
- Workers' compensation insurance procurement (mandatory in Minnesota; handled by `us-mn-workers-comp`).
- Multi-state apportionment of wages where the employee performs services in more than one state — refer to Minnesota Revenue Notice 03-12 and the reciprocity discussion below, and consult a credentialed multi-state payroll specialist.
- Public-sector and tribal employer carve-outs.

Reviewer assumption: every output of this skill is reviewed and signed off by a credentialed Minnesota payroll professional (CPA, EA, CPP, or licensed Minnesota attorney) before any filing is submitted or any notice is delivered to an employee. The skill produces draft work product, not final filings.

## 2. Minnesota Personal Income Tax — Withholding Brackets and Supplemental Rate (2025)

### 2.1 Brackets

**Minnesota 2025 PIT withholding brackets**  _(Minnesota Statutes §290.06, subd. 2d)_

| Bracket | Rate |
| --- | --- |
| 1 | 5.35% |
| 2 | 6.80% |
| 3 | 7.85% |
| 4 | 9.85% |

- **Bracket 1 rate** — 5.35%
- **Bracket 2 rate** — 6.80%
- **Bracket 3 rate** — 7.85%
- **Bracket 4 rate** — 9.85%
- **Rate stability** — The 5.35% floor and the 9.85% ceiling have been stable since 2014. The exact 2025 dollar thresholds at which each marginal rate begins differ by filing status (Single, Married Filing Jointly, Married Filing Separately, Head of Household) and are published annually in the Minnesota Income Tax Withholding Instruction Booklet and Tax Tables (the 'Minnesota Withholding Tax Tables') issued by the Minnesota DOR in December. The booklet provides both percentage-method tables and wage-bracket tables; employers may use either method consistently for a given employee.
- **Practical withholding inputs** — For practical withholding computation in 2025, the relevant inputs are: Annualized wages (gross pay × number of pay periods per year); W-4MN allowances (Minnesota allowances, which may differ from federal W-4 entries; see §4 below); Filing status as elected on W-4MN.
- **Percentage method calculation skeleton** — 1. Annualize the gross wage for the pay period. 2. Subtract the Minnesota allowance value × number of allowances claimed on W-4MN. The per-allowance value is published annually in the withholding booklet; for 2025 it tracks the federal personal exemption baseline as adjusted under §290.0671 / §290.06. 3. Apply the bracket table for the elected filing status to get annual Minnesota tax. 4. Divide by the number of pay periods to get the per-period withholding amount.  _(§290.0671 / §290.06)_
- **W-4 vs W-4MN divergence risk** — Step (2) is where Minnesota diverges sharply from the federal 'post-TCJA' Form W-4, which eliminated allowances. Minnesota retained allowances on W-4MN precisely because the state withholding tables remained allowance-based. **An employer that simply mirrors the federal W-4 onto Minnesota withholding will systematically under-withhold or over-withhold and will likely fail a DOR audit on the W-4MN requirement.** See §4.

### 2.2 Supplemental withholding rate

- **Minnesota supplemental withholding rate (2025)** — 6.25%  _(§290.92, subd. 2a)_
- **Supplemental wages** — Bonuses, commissions, severance, retroactive pay increases, accumulated sick pay, certain taxable fringe benefits, and any payment that is 'not a payment of regular wages' within the meaning of §290.92, subd. 2a.  _(§290.92, subd. 2a)_
- **Availability of supplemental rate** — The supplemental rate is available in lieu of the aggregate method only when the supplemental wages are paid separately from regular wages, or when they are paid together with regular wages but separately identified on the payroll record. If supplemental wages are commingled with regular wages without separate identification, the employer must use the aggregate method (combine the supplemental amount with the regular wage for that period and compute withholding on the total using the regular tables).

Practical note for software developers and other professional freelancers transitioning to W-2 employment (a common OpenAccountants client scenario): year-end bonuses paid in December are the single most common 6.25% supplemental withholding event. If the bonus pushes the employee's total compensation into the 9.85% top marginal bracket, the 6.25% flat rate will under-withhold materially and the employee will owe with their Form M1. Reviewers should confirm whether the employee has elected additional withholding on W-4MN Line 2 to compensate.

### 2.3 Reciprocity

- **North Dakota reciprocity** — Minnesota has a longstanding income tax reciprocity agreement with North Dakota.  _(Minnesota Statutes §290.081)_
- **Wisconsin reciprocity terminated** — It also formerly had reciprocity with Wisconsin, which was terminated in 2009 and has not been reinstated as of 2025; Wisconsin residents working in Minnesota are subject to Minnesota withholding (with a Wisconsin credit for taxes paid to Minnesota).
- **Form MWR mechanics** — Under the North Dakota reciprocity agreement, a North Dakota resident who works in Minnesota and files Form MWR ('Reciprocity Exemption/Affidavit of Residency') with the Minnesota employer may have Minnesota withholding waived. The employer must retain Form MWR and submit a copy to the DOR annually. The Michigan and other neighboring-state reciprocity rumors that circulate in payroll forums are not currently in effect for Minnesota.

### 2.4 Forms M1 / M1W reconciliation

- **M1/M1W reconciliation** — Although the employer is not the M1 filer, the employee's year-end Form M1 (Minnesota Individual Income Tax Return) reconciles to the W-2 box 17 amount via Schedule M1W. If the employer's W-2 reporting and the DOR's withholding records diverge, the employee's M1 will be rejected or held for review. Year-end W-2/W-3 reconciliation discipline (see §3.4) matters not only for the employer but for every employee's individual return.

## 3. Minnesota Withholding — Deposit and Return Mechanics

### 3.1 Registration

- **Employer registration requirement** — Every employer paying wages for services performed in Minnesota must register with the Minnesota DOR for a Minnesota Tax ID number before the first wage payment. Registration is via the DOR e-Services portal (www.revenue.state.mn.us). The DOR will assign: A 7-digit Minnesota Tax ID for income tax withholding; A separate UI account number issued by DEED (see §5). The same Minnesota Tax ID is used for sales tax, MinnesotaCare tax, and other DOR-administered taxes; the system uses the account-type suffix to distinguish.

### 3.2 Deposit frequency

- **Monthly depositor threshold** — $1,500 USD (prior calendar year Minnesota withholding exceeded this amount)
- **Monthly depositor due date** — Deposits are due by the 15th day of the month following the month in which wages were paid. (Note: the deposit due date is the 15th of the following month, not the federal semiweekly schedule.)
- **Quarterly depositor threshold** — $1,500 or less USD (prior-year Minnesota withholding)
- **Quarterly depositor due dates** — Deposits are due by the last day of the month following the close of the calendar quarter (April 30, July 31, October 31, January 31).
- **Accelerated schedule notice** — In addition, the DOR may notify a high-liability employer that it must follow a more frequent schedule (semi-weekly or accelerated payment) where Minnesota mirrors the federal accelerated rules. These are uncommon outside very large employers and are not addressed in detail here; if a notice is received, escalate to the reviewer.
- **No annual deposit category** — There is no 'annual' Minnesota withholding deposit category for active employers.
- **Electronic deposit mechanism** — All deposits are made electronically through e-Services using Form MW-1 (an online return; there is no longer a separate paper coupon in routine use). ACH debit and ACH credit are both supported.

### 3.3 Quarterly return — Form MWR

- **Form MWR filing requirement** — Notwithstanding the deposit schedule, every Minnesota withholding registrant must file Form MWR ('Reconciliation of Withholding') information returns on a schedule prescribed by the DOR. In practice, the operative filing is the quarterly withholding return filed through e-Services, which reconciles wages paid and tax withheld for the quarter against deposits made. The quarterly return is due by the last day of the month following the quarter (the same date as the quarterly deposit, when applicable).
- **Nil-quarter return requirement** — A nil-quarter return is required even if no wages were paid, as long as the account is open. Failure to file the nil return is a common audit trigger.

### 3.4 Annual W-2/W-3 reconciliation — due January 31

- **Annual reconciliation deadline** — Minnesota requires employers to submit Forms W-2 (employee copy data) and the state W-3M reconciliation through e-Services by January 31 following the close of the calendar year. This is the same accelerated deadline that applies federally under the PATH Act for W-2 transmittal to SSA, and the deadlines have been aligned since 2017.
- **Late filing exposure** — Late filing exposes the employer to: A statutory late-filing penalty under Minnesota Statutes §289A.60. Interest on any underpayment from the original due date. Potential disallowance of the employer's wage deduction on its own income tax return, in extreme cases of non-filing.  _(Minnesota Statutes §289A.60)_
- **Information return e-filing threshold** — The annual reconciliation also captures any 1099-NEC, 1099-MISC, and 1099-R that report Minnesota withholding. For employers issuing fewer than 10 information returns total (W-2 + 1099 combined) paper filing is permitted; otherwise e-filing is mandatory.

### 3.5 Audit flash point — MWR vs. W-2/W-3 reconciliation

> **AUDIT FLASH POINT — withholding reconciliation drift.** The single most common Minnesota withholding audit finding is a mismatch between (a) the sum of Minnesota withholding reported on the four quarterly MWR returns, (b) the total Minnesota withholding reported on the year-end W-3M reconciliation, and (c) the total Minnesota withholding reported in box 17 across all W-2s. These three numbers must tie to the penny. Pre-filing, the reviewer should run a three-way reconciliation worksheet and clear any variance before submitting the W-3M. A variance of even $1 will generate an automated DOR notice and a credit-hold on the account.

## 4. Form W-4MN — Minnesota Employee Withholding Allowance/Exemption Certificate

### 4.1 Why W-4MN exists separately from federal W-4

- **Non-conformity rationale** — When the federal Tax Cuts and Jobs Act eliminated personal exemptions and the IRS redesigned Form W-4 in 2020 to remove the allowance concept, Minnesota chose not to conform. Minnesota's income tax base under Chapter 290 continues to incorporate a state-level personal exemption mechanism, and the state withholding tables remain calibrated to a per-allowance dollar value. The result is that a federal W-4 completed under the post-2020 design does not provide the data the Minnesota withholding tables require.  _(Chapter 290)_
- **W-4MN contents** — Form W-4MN is the Minnesota-specific certificate. It collects: Filing status (Single / Married / Married but withhold at higher Single rate); Number of Minnesota allowances claimed; Additional Minnesota withholding amount per pay period (Line 2); Exemption claims (Line 7) where the employee qualifies (e.g., reciprocity, military spouse, or expectation of no Minnesota tax liability).

### 4.2 When the employer MUST require a W-4MN

- **Situations requiring W-4MN** — An employer must obtain Form W-4MN from an employee in any of the following situations (Minnesota Statutes §290.92, subd. 5; Revenue Notice 04-02 and successors): 1. The employee claims fewer Minnesota allowances than federal allowances on the federal W-4 (legacy pre-2020 forms). 2. The employee claims more than 10 Minnesota allowances. 3. The employee claims to be exempt from Minnesota withholding but is not exempt from federal withholding. 4. The employee requests additional Minnesota withholding. 5. The employee claims an exemption from Minnesota withholding based on residency in a reciprocity state (currently only North Dakota; see Form MWR rather than W-4MN for the reciprocity affidavit). 6. The employee uses the redesigned post-2020 federal Form W-4 (which has no allowance line) — in this case the employer must obtain a W-4MN in order to apply the Minnesota allowance-based tables. As a practical matter, this means every new hire from 2020 forward should be given a W-4MN at onboarding.  _(Minnesota Statutes §290.92, subd. 5; Revenue Notice 04-02)_
- **Default rule if no valid W-4MN** — If the employer does not have a valid W-4MN on file for an employee in any of these scenarios, the default rule is to withhold at Single with zero allowances — the most conservative (highest withholding) treatment. This default protects the employer from the DOR's preferred audit position but will routinely over-withhold for married employees with dependents.

### 4.3 Submission to DOR

- **DOR submission requirement** — Most W-4MNs stay in the employee personnel file. However, the employer must submit a copy to the DOR within 30 days when: The employee claims more than 10 Minnesota allowances. The employee claims exempt from Minnesota withholding and earns more than $200 per week. Submission is via e-Services upload. Failure to submit a copy when required is a separate violation from any under-withholding that may result.

### 4.4 Annual refresh

- **Exemption claim expiration** — W-4MN exemption claims (Line 7) expire on February 15 of the following year. An exempt employee who does not provide a fresh W-4MN by February 15 must be withheld at Single / zero allowances beginning with the first pay period after February 15. This mirrors the federal exempt-W-4 expiration rule and is one of the most commonly missed payroll calendar items.

## 5. Minnesota Unemployment Insurance (UI)

### 5.1 Coverage and registration

- **Subject employer coverage** — Minnesota's UI program is administered by DEED under Minnesota Statutes Chapter 268. Coverage is broad: virtually all employers paying $1,500 or more in wages in any calendar quarter, or employing one or more workers in 20 or more weeks in a calendar year, are 'subject employers.' Agricultural and domestic-service employers have higher thresholds. Nonprofit 501(c)(3) employers are covered but may elect a reimbursement basis instead of contribution.  _(Minnesota Statutes Chapter 268)_
- **Registration process** — Registration is mandatory and is completed through the DEED Unemployment Insurance employer portal (www.uimn.org). The employer receives a UI account number, separate from the DOR Minnesota Tax ID, and an initial rate assignment.

### 5.2 Taxable wage base — $43,000 for 2025

- **Minnesota UI taxable wage base (2025)** — $43,000 USD (per employee)  _(Minnesota Statutes §268.035, subd. 23)_
- **Wage base ranking and indexing** — This is one of the highest UI wage bases in the United States — only Washington, Oregon, Idaho, Hawaii, and a handful of others routinely exceed it. The wage base is indexed annually to 60% of the state average weekly wage under Minnesota Statutes §268.035, subd. 23.  _(Minnesota Statutes §268.035, subd. 23)_

Practical consequence: an employee earning $80,000 produces roughly $43,000 × employer rate of UI exposure; the marginal cost of an additional $1 of wages above $43,000 is zero for UI purposes. For comparison, an employer in a $7,000-wage-base state (the federal FUTA base, also the SUTA base in several southern states) exhausts its UI wage base in the first 2–3 months of the year. In Minnesota, UI cost continues to accrue through roughly mid-year for a typical full-time salaried hire.

### 5.3 Experience rates and new-employer rates

- **Experience-rated employer rate range (2025)** — approximately 0.10% to 9.0% % of taxable wages
- **Rate schedule publication** — The exact minimum and maximum, and the schedule used to translate each employer's reserve ratio (or, for some experience definitions, benefit ratio) into a rate, is published annually by DEED in the year-end rate notice mailed/posted in December.
- **Construction industry new-employer rate (2025)** — approximately 9.0% % of taxable wages (the maximum on the schedule)
- **Non-construction new-employer rate (2025)** — approximately 1.0% % of taxable wages (schedule minimum or near it; DEED may assign higher based on NAICS-code risk classification)

These ranges are wider than most states. A new construction-industry employer in Minnesota will pay UI at roughly $43,000 × 9.0% = $3,870 per employee per year in UI for the first three years of operation (the standard new-employer period before experience rating begins). A new non-construction employer at 1.0% pays $430 per employee per year. The difference — nearly $3,500 per employee per year — is one of the largest single drivers of the 'should I classify this worker as my employee, the GC's employee, or an independent contractor?' question in §9.

- **Additional rate components** — In addition to the experience-rated portion, each employer pays: A base tax component, set annually. An Additional Assessment if the UI trust fund balance falls below a statutory target (Minnesota Statutes §268.051, subd. 2). The Additional Assessment was 14% in some recent years; for 2025 the DEED schedule should be consulted. A Federal Loan Interest Assessment if applicable (not applicable in 2025 as the Minnesota UI trust fund is in positive balance). A Workforce Development Fee (0.10% in recent years) under Minnesota Statutes §116L.20.  _(Minnesota Statutes §268.051, subd. 2; Minnesota Statutes §116L.20)_
- **Modeling assumption for combined rate** — The 'rate' the employer sees on the December notice is the combined rate of all these components. For modeling purposes, assume an effective rate at the published experience-rate ceiling plus 0.10% for the workforce development fee.

### 5.4 Quarterly UI return and wage detail

**UI quarterly return due dates**

| Quarter | Wages paid | Return due |
| --- | --- | --- |
| Q1 | Jan–Mar | April 30 |
| Q2 | Apr–Jun | July 31 |
| Q3 | Jul–Sep | October 31 |
| Q4 | Oct–Dec | January 31 |

- **Wage detail report content** — Both the return (gross wages, taxable wages, contribution due) and the wage detail report (employee-by-employee SSN, name, total wages, hours worked) are submitted together. Hours worked is a required field in Minnesota, distinguishing it from many states; it is used by DEED to compute UI benefit eligibility for terminated employees.
- **Late filing penalty** — Late filing penalty: $25 minimum, escalating with delay. Interest on unpaid contributions accrues at the statutory rate.  _(Minnesota Statutes §268.058)_

### 5.5 Common UI audit triggers

- **Audit trigger list** — Misclassification of workers as 1099 contractors when they should be W-2 (§9 below). Failure to include all taxable fringe benefits in UI wages (the UI wage definition under §268.035, subd. 29 is slightly broader than the federal Form 941 wage definition for some non-cash items). Failure to report newly hired employees within 20 days through the Minnesota New Hire Reporting Center, which is a separate but related obligation. 'Successor' issues — if a buyer acquires substantially all of the assets of an existing Minnesota employer, the UI experience rate generally transfers to the buyer under §268.051, subd. 4. Buyers in M&A diligence frequently miss this and inherit a 9.0% rate.  _(§268.035, subd. 29; §268.051, subd. 4)_

## 6. Earned Sick and Safe Time (ESST) — Statewide, effective January 1, 2024

### 6.1 Statutory framework

- **ESST statutory basis** — Minnesota Statutes §181.9445 through §181.9448 establish a statewide Earned Sick and Safe Time mandate, enacted by 2023 Laws Ch. 53, Article 12, and refined by clarifying amendments in 2024 Laws Ch. 110. Effective January 1, 2024, virtually every private-sector employer in Minnesota with one or more employees performing work in the state must provide accrued paid sick and safe time. There is no small-employer carve-out at the state level (Minneapolis and Saint Paul had pre-existing ordinances; the state law now provides a floor that covers the rest of the state and supplements the local ordinances).  _(Minnesota Statutes §181.9445–§181.9448; 2023 Laws Ch. 53, Article 12; 2024 Laws Ch. 110)_

This is one of the most operationally disruptive Minnesota employment law changes in the past decade for employers that previously offered no sick leave or only unlimited-PTO arrangements.

### 6.2 Accrual

- **ESST accrual rate** — 1 hour of ESST for every 30 hours worked
- **ESST accrual cap** — 48 hours per year hours
- **ESST accrued-and-unused balance cap** — 80 hours total hours
- **Carryover rule** — Accrued, unused ESST carries over from year to year up to the 80-hour cap. The employer cannot extinguish accrued ESST at year-end except in narrow circumstances (e.g., front-loading; see below).
- **Eligibility and waiting period** — An employee accrues from the first hour worked. There is no waiting period or probationary period for accrual itself, although the employer may impose a 90-day waiting period before the accrued ESST is usable.
- **Front-loading alternative** — Alternative compliance method — front-loading: an employer may instead provide 48 hours of ESST at the start of each year, available immediately. Under the front-loading method, the employer is not required to carry over unused hours into the following year (a meaningful administrative simplification). Front-loaded ESST must still be paid out under §6.5 below.

### 6.3 Permitted uses

- **Permitted uses list** — ESST may be used for: 1. The employee's mental or physical illness, injury, medical condition, or preventive care. 2. Care of a family member with any of the above. 3. Absence due to domestic abuse, sexual assault, or stalking affecting the employee or a family member (the 'safe time' component). 4. Closure of the employee's workplace or the employee's child's school/place of care due to weather or public emergency. 5. The employee's inability to work due to a determination by a health authority that the employee or a family member's presence in the community would jeopardize others' health (the 'communicable disease' provision, which generalizes the COVID-era school-closure issues).
- **Family member definition** — 'Family member' is defined broadly and includes — beyond spouse, child, and parent — siblings, grandparents, grandchildren, in-laws, and 'any other individual related by blood or whose close association with the employee is the equivalent of a family relationship.' This is broader than the federal FMLA definition.

### 6.4 Notice requirements

- **Three notices required** — Three discrete notices apply: 1. Workplace poster / written notice at hire: by the start of employment, the employer must provide each employee a written notice (in English and in the employee's primary language if not English) explaining ESST rights, the accrual rate, the permitted uses, and the anti-retaliation provisions. A model notice is published by DLI. 2. Earnings statement disclosure: each pay statement must include the number of ESST hours accrued and unused, and the number of ESST hours used in the pay period. This is enforced through the Wage Theft Prevention Act earnings-statement provisions (§8). 3. Notice of use: an employee using ESST must give 'as much advance notice as practicable' if the need is foreseeable, but the employer cannot require more than 7 days' notice and cannot require notice at all for unforeseeable uses.

### 6.5 Pay-out and rate

- **ESST pay rate** — ESST is paid at the employee's regular rate of pay for the hours of ESST used. The regular rate computation follows the federal Fair Labor Standards Act (FLSA) regular-rate methodology — for nonexempt employees who routinely receive nondiscretionary bonuses, shift differentials, or commission, this is not a trivial calculation.
- **No separation payout requirement** — ESST is not required to be paid out at separation, except where the employer's general PTO policy commingles ESST with vacation/PTO and treats the commingled balance as paid out under §181.13 (or under the employer's own policy or CBA).  _(§181.13)_

### 6.6 Recordkeeping

- **ESST recordkeeping retention** — Employers must retain records of ESST accrual, use, and balance for three years for each employee, available for DLI inspection. Records must include, at minimum: hours worked each pay period, ESST hours accrued each pay period, ESST hours used each pay period, and the running balance.

> **AUDIT FLASH POINT — ESST tracking from day one.** The most common ESST violation found in DLI investigations is not refusal to grant leave; it is failure to track accrual at all, particularly by employers that previously had unlimited-PTO or 'salaried-no-tracking' policies. These employers must retrofit a tracking system. Even a 'we give everyone unlimited PTO' policy does not satisfy §181.9447 unless the employer can demonstrate that the policy meets or exceeds every element of the statutory minimum (accrual rate, permitted uses, family member definition, carryover, pay statement disclosure, recordkeeping). In practice this means: track ESST as a separate bucket even if the employer provides PTO that exceeds the statutory minimum. Failure to do so is per se non-compliance with the pay-stub disclosure rule and is the easiest violation for DLI to prove.

### 6.7 Anti-retaliation

- **Anti-retaliation and remedies** — §181.9447 prohibits retaliation against an employee for requesting or using ESST. Remedies include reinstatement, back pay, statutory damages of up to the value of the ESST denied, and attorneys' fees. Pattern-or-practice violations can trigger DLI administrative penalties up to $10,000 per violation.  _(§181.9447)_

### 6.8 Interaction with local ordinances

- **State vs local ordinance interaction** — The Minneapolis and Saint Paul ESST ordinances pre-date the state law. Where the state law is more generous to the employee (e.g., uses, family-member definition), the state law applies; where the local ordinance is more generous (e.g., faster accrual, more covered uses), the local ordinance applies. Employers in those two cities must comply with the stricter element-by-element, which in practice means tracking under the local ordinance and adding the state-law elements on top. The local-ordinance addendum covers this.

## 7. Minnesota Paid Leave (Chapter 268B) — Effective January 1, 2026 (DEEP DIVE)

### 7.1 What it is

- **Minnesota Paid Leave description** — Minnesota Paid Leave is a state-administered paid family and medical leave insurance program, modeled on the Washington, Oregon, Colorado, and Connecticut programs. It is funded by a payroll premium split between employer and employee, and it pays partial wage-replacement benefits to covered workers taking leave for the qualifying reasons (own serious health condition, family member's serious health condition, bonding with a new child, qualifying military exigency, or safety leave related to domestic violence/sexual assault/stalking).
- **Statutory basis and administrator** — Statutory basis: Minnesota Statutes Chapter 268B, enacted by 2023 Laws Ch. 59, Article 11, with implementation amendments in 2024 Laws Ch. 127. Administrator: Minnesota Department of Employment and Economic Development (DEED), through the new Family and Medical Benefits Insurance Division.  _(Minnesota Statutes Chapter 268B; 2023 Laws Ch. 59, Article 11; 2024 Laws Ch. 127)_
- **Effective dates** — Effective date for benefits and premium collection: January 1, 2026. Effective date for employer wage reporting: October 31, 2024 (Q3 2024 wage detail). This is critical: employers have already been reporting wages to Paid Leave through the existing UI wage detail submission since late 2024. The 2026 transition is the addition of premium collection on top of wage reporting, plus the activation of the benefit side.

### 7.2 Premium rate and split

- **2026 Paid Leave premium rate** — 0.88% of taxable wages  _(Minnesota Statutes §268B.14)_
- **Employer share** — 0.44% (mandatory)  _(Minnesota Statutes §268B.14)_
- **Employee share** — 0.44% (employer may, but is not required to, withhold from the employee's wages; employer may also elect to cover the employee share as a benefit)  _(Minnesota Statutes §268B.14)_

This is the operative statutory split as of the 2024 amendments. (Earlier 2023 commentary using a 0.7% split of 0.35% / 0.35% reflected the original 2023 Act before the 2024 amendments adjusted the rate to fund the actuarial projection; the 2026 startup rate is the 0.88% / 0.44% / 0.44% schedule. Confirm against the DEED rate notice published in late 2025.)

- **Statutory combined premium cap** — 1.2% % combined (currently; Commissioner of DEED may set premium rate each year up to this cap based on actuarial soundness)

### 7.3 Taxable wage base

- **Paid Leave taxable wage base (2025 SS wage base)** — $176,100 USD (for 2025; the 2026 figure will be published by SSA in October 2025; Paid Leave premium applies to wages up to the Social Security wage base)
- **Wage base comparison to UI** — This is materially higher than the UI wage base of $43,000 — meaning Paid Leave premium continues to accrue on the same wages long after UI has capped out.

For an employee earning $176,100 or more in 2026, the maximum annual Paid Leave premium is approximately: Employer: $176,100 × 0.44% ≈ $774.84. Employee: $176,100 × 0.44% ≈ $774.84. Combined: ≈ $1,549.68 per high-earner per year. For a $60,000 employee: Employer: $264; Employee: $264; Combined: $528.

### 7.4 Small-employer relief

- **Small-employer reduced premium eligibility and benefit** — Employers with 30 or fewer employees averaged across the prior year, and with average wages below 150% of the state average wage, qualify for a reduced employer-share premium under §268B.14, subd. 5. The reduction is approximately 50% of the standard employer share, plus access to grants for hiring temporary replacement workers when an employee goes on leave. The employee share is not reduced.  _(§268B.14, subd. 5)_

### 7.5 Private plan option

- **Private plan approval and requirements** — An employer may apply to DEED for approval of an equivalent private plan in lieu of the state program (§268B.10). The private plan must provide benefits equal to or greater than the state program in every dimension (eligibility, duration, wage replacement, job protection). Approved private plans are exempted from the state premium but must pay a per-employee administrative assessment to DEED.  _(§268B.10)_

For most small and mid-sized employers, the state program is operationally simpler than building a compliant private plan and securing approval. The private plan option is mainly relevant to large employers that already have a generous short-term disability and parental leave package and want to integrate.

### 7.6 Benefits employees will receive

- **Benefit caps and wage replacement structure** — Up to 12 weeks of medical leave for the employee's own serious health condition in a benefit year. Up to 12 weeks of family leave for bonding, family care, qualifying exigency, or safety leave. Combined cap of 20 weeks of medical + family leave in a single benefit year. Wage replacement on a progressive formula: 90% of the portion of the employee's average weekly wage up to 50% of the state average weekly wage, plus 66% of the next tier, plus 55% of wages above that, subject to a weekly maximum cap (the cap will be set annually by DEED; for benefit year 2026 the cap is approximately the state average weekly wage). Minimum benefit: not less than $100 per week (or the employee's average weekly wage, if lower).
- **Job protection and health insurance continuation** — Job protection: the employee is entitled to reinstatement to the same or an equivalent position upon return, subject to certain exceptions (the position-elimination defense, key-employee carve-out). Job protection runs in parallel with FMLA where applicable, and runs as a state-law right independent of FMLA where FMLA does not apply (e.g., for employers under 50 employees, where FMLA is not triggered). Health insurance continuation: the employer must continue group health insurance during Paid Leave on the same basis as if the employee were actively at work.

### 7.7 Interaction with FMLA, ESST, short-term disability, and PTO

- **Interaction rules** — FMLA: runs concurrently with Paid Leave for the same qualifying reason. The employer must notice FMLA designation as it normally would. ESST: ESST is a separate accrued benefit and is not consumed by Paid Leave. An employee may use ESST in lieu of unpaid time during the Paid Leave waiting period (if any), or to top up Paid Leave benefits to 100% of regular wages. Short-term disability: an STD policy may coordinate with Paid Leave to provide top-up. The STD carrier will need to integrate; employers should expect 2025 plan-year STD renewals to address this. PTO / vacation: the employer cannot require the employee to use accrued PTO before or during Paid Leave, but the employee may elect to use PTO to supplement Paid Leave wage replacement up to 100% of regular wages. Workers' compensation: not concurrent. An employee receiving workers' comp wage replacement is not eligible for Paid Leave benefits for the same period.

### 7.8 What employers need to prepare for NOW (2025 readiness checklist)

- **2025 readiness checklist** — 1. Payroll system update: confirm the payroll vendor (Gusto, ADP, Paychex, Rippling, Justworks, or in-house) has the Minnesota Paid Leave premium configured as a 2026 deduction code. The combined rate of 0.88% and the SSN-base wage cap must be implementable. Confirm whether the system supports the employer-pays-employee-share election or requires it as a wage advance. 2. Employee communication: by December 1, 2025, employers should issue a written notice to all Minnesota employees explaining the new payroll deduction, the program, the qualifying reasons, and how to file a claim. DEED is publishing a model notice; do not draft from scratch. 3. Posting: the DEED workplace poster for Paid Leave must be posted by January 1, 2026 alongside the existing required posters (FLSA, FMLA, OSHA, MN Wage Disclosure, etc.). 4. Handbook update: the employee handbook should be updated to reflect Paid Leave eligibility, the interaction with PTO, the interaction with FMLA, the interaction with ESST, and the procedure for requesting leave through the DEED portal (employees file claims directly with DEED, not the employer; the employer is asked to verify employment). 5. Leave administration workflow: designate the internal person or vendor responsible for responding to DEED employment verification requests within the statutory 5-business-day window. Late responses can result in the benefit being approved without the employer's input, and the employer being later assessed for any overpayment. 6. Multi-state coordination: for employers with employees who work partly in Minnesota and partly out of state, confirm with the reviewer which employees are 'Minnesota employees' for Paid Leave purposes. The §268B test is based on where services are localized (the same multi-factor test used for UI), with overlap for cross-border workers between Minnesota and Wisconsin/North Dakota/South Dakota/Iowa. 7. Budget impact: model the 2026 employer-share cost. For a 10-employee company averaging $75,000 salaries, the employer-side incremental payroll cost is approximately $75,000 × 10 × 0.44% = $3,300 per year, plus the same again on the employee side if the employer elects to absorb it. For a 100-employee company at the same salary, $33,000 per year. 8. Private-plan decision: if the employer is considering a private plan, the application must be filed with DEED well in advance of January 1, 2026; approval is not automatic and may take several months. Decide by mid-2025. 9. Reasonable-accommodation interaction: train HR on the interaction between Paid Leave and ADA reasonable accommodation. Paid Leave is a wage-replacement program, not an accommodation; an extended leave beyond the 12/20-week caps may still be required as a reasonable accommodation under the ADA. 10. Reconcile UI wage detail: since 2024 Q3, the UI wage detail report has captured the data that DEED will use for Paid Leave premium computation. Confirm that 2024-2025 UI wage detail has been filed accurately and on time — gaps in the UI wage detail will surface as gaps in the Paid Leave premium base in 2026, and remediation later is materially harder than fixing now.

> **AUDIT FLASH POINT — 2026 Paid Leave setup deadlines.** The Minnesota Paid Leave program goes live January 1, 2026 with both premium collection AND benefit eligibility on day one. Employers that have not (a) configured their payroll system, (b) posted the DEED notice, (c) issued the employee written notice by December 1, 2025, (d) updated the handbook, and (e) confirmed accurate 2024–2025 UI wage detail history will face compounding problems in Q1 2026: employees will file claims that the employer is unprepared to verify within 5 business days; payroll deductions will be late or incorrect; and DEED will impose late-filing penalties under §268B.14, subd. 9 (up to $250 per employee for late or inaccurate reporting). The September–December 2025 implementation window is the single most important Minnesota payroll project in 2025.

### 7.9 Premium remittance mechanics

**Paid Leave premium remittance due dates (2026)**

| Quarter | Due |
| --- | --- |
| Q1 (Jan–Mar 2026) | April 30, 2026 |
| Q2 (Apr–Jun 2026) | July 31, 2026 |
| Q3 (Jul–Sep 2026) | October 31, 2026 |
| Q4 (Oct–Dec 2026) | January 31, 2027 |

- **Combined filing mechanics** — From Q1 2026 forward, Paid Leave premium remittance will be quarterly, on the same schedule and through the same DEED portal as UI contributions. The wage detail report is shared with UI (no duplicate filing). Premium is remitted as a single combined employer-plus-employee amount; the split is internal to the employer's books.

## 8. Wage Theft Prevention Act (WTPA)

### 8.1 Statutory framework

- **WTPA statutory basis and felony threshold** — Minnesota's Wage Theft Prevention Act, enacted by 2019 Laws Ch. 50 and codified primarily at Minnesota Statutes §181.032 (earnings statements), §181.101 (final wages), §181.13 (separation), and §609.52 (criminal wage theft), is one of the strictest wage-theft laws in the United States. It elevates willful failure to pay wages to a felony-level criminal offense when the unpaid amount exceeds $1,000 (the threshold tracks the theft statute).  _(2019 Laws Ch. 50; §181.032; §181.101; §181.13; §609.52)_

### 8.2 Notice at hire

- **Written notice content requirements** — Under §181.032, at the start of employment, the employer must provide each employee a written notice containing, at minimum: 1. The employee's rate(s) of pay and basis (hourly, salary, commission, piece rate). 2. Allowances claimed by the employer toward minimum wage (tip credit, meal/lodging). 3. Paid vacation, sick time, or PTO accrual rate and terms (including ESST under §6). 4. The employee's employment status — exempt or nonexempt from FLSA overtime. 5. The number of days in the pay period and the regularly scheduled payday. 6. The legal name of the employer and any operating name (DBA). 7. The physical address of the employer's main office or principal place of business, and a mailing address if different. 8. The employer's telephone number. 9. A list of deductions that may be made from the employee's pay.  _(§181.032)_
- **Signature and multilingual model notice** — The notice must be signed and dated by the employee, and the employee must be provided a copy. A model notice (in English, Spanish, Hmong, Somali, and other common languages) is published by DLI.
- **Material changes notice requirement** — Material changes: any change to any of the above elements (e.g., a pay raise, a change in pay frequency, a new deduction, a promotion that changes exempt status) must be reflected in a written notice provided to the employee before the effective date of the change. This is the most commonly missed element of the WTPA; many employers provide notice at hire but fail to issue update notices.

### 8.3 Earnings statement requirements

- **Pay statement required elements** — Each pay statement (paystub) must include: Name of employee. Hours worked (for nonexempt employees). Rate(s) of pay and total pay. Deductions, itemized. Net pay. Allowances claimed for permitted credits (e.g., meals, lodging). Pay period dates. Employer's legal name, contact information, and the date the wages are paid. The amount of ESST accrued and used in the pay period, and the balance available (added by the 2024 ESST amendments).

### 8.4 Final wages

- **Discharge final pay timing** — Under §181.13, when an employee is discharged by the employer, all earned wages are due within 24 hours of the employee's demand. If no demand is made, wages are due at the next regular payday but no later than 20 days after termination.  _(§181.13)_
- **Voluntary quit final pay timing** — Under §181.14, when an employee voluntarily quits, wages are due at the next regular payday, but no later than 20 calendar days after the date of resignation.  _(§181.14)_
- **Safer practical rule for routine separations** — Practically, the safer rule for routine separations is: pay all earned wages by the next regular payday following the separation. This satisfies both §181.13 and §181.14 in the absence of an immediate demand following discharge. (Note: this answers the user's prompt requirement that final pay is 'by next regular payday.')  _(§181.13; §181.14)_
- **Earned wages for final-pay purposes and PTO payout** — Earned wages for final-pay purposes include accrued commissions, accrued bonuses that have become non-discretionary by their terms, and any accrued PTO that the employer's policy treats as a paid-out benefit. Whether accrued unused PTO must be paid out at separation depends on the employer's written policy: Minnesota does not statutorily require PTO payout, but a policy that grants the right vests the obligation and the employer cannot retroactively rescind.
- **ESST separation payout cross-reference** — ESST, as noted in §6.5, is not statutorily required to be paid out at separation (unless commingled with general PTO).

### 8.5 Penalties

- **Civil penalties** — Civil: an employee may recover unpaid wages, an equal amount as liquidated damages, attorney's fees, and costs. The DLI may also assess administrative penalties.
- **Criminal penalties** — Criminal: under §609.52 (the theft statute, as amended by 2019 Laws Ch. 50), willful failure to pay wages exceeding $1,000 is treated as theft of the corresponding amount. Penalties scale to the amount: at $1,000–$5,000, gross misdemeanor; above $5,000, felony with potential imprisonment.  _(§609.52; 2019 Laws Ch. 50)_
- **Per-pay-stub penalty** — Per-pay-stub penalty: failure to provide a compliant earnings statement is a separate violation per pay period per employee, with a statutory penalty of up to $50 per occurrence.

## 9. Worker Classification — Employee vs. Independent Contractor

### 9.1 The two regimes

- **General nine-factor test description** — General nine-factor test — applicable to most industries; used by DEED for UI coverage and by the DOR for state withholding. This test draws from the federal common-law 'right to control' test and the IRS 20-factor framework, distilled by DEED into nine practical factors.
- **Construction-industry test description** — Construction-industry test — applicable specifically to building construction and improvement work under Minnesota Statutes §181.723. This is materially stricter than the general test; in the construction context, the default presumption is 'employee,' and the employer must satisfy a multi-prong showing to support contractor classification. See §10.  _(Minnesota Statutes §181.723)_

### 9.2 The general nine-factor test (UI / withholding)

- **Nine factors list** — DEED applies these nine factors in determining whether services are performed by an employee or an independent contractor: 1. Right to control the means and manner of performance — the most heavily weighted factor. If the hiring party controls how the work is done (not just the result), the worker is an employee. 2. Mode of payment — hourly/weekly/monthly suggests employee; per-project or per-deliverable suggests contractor. 3. Furnishing of materials and tools — if the hiring party supplies tools, suggests employee. 4. Control over premises where work is performed — work on the hiring party's site under its supervision suggests employee. 5. Right of discharge — if the hiring party can fire the worker at will without breach-of-contract liability, suggests employee. 6. Engagement in an independently established trade or business — does the worker hold themselves out to the public, advertise, carry insurance, serve multiple clients? If yes, contractor. 7. Realization of profit or loss — does the worker have entrepreneurial risk (could lose money on the engagement)? If yes, contractor. 8. Investment in facilities — significant investment in the worker's own tools, vehicles, equipment, or workspace suggests contractor. 9. Permanency of the relationship — open-ended ongoing engagement suggests employee; finite project with a defined end suggests contractor.
- **Totality of circumstances and burden of proof** — No single factor is dispositive; DEED weighs the totality. The hiring party bears the burden of supporting a contractor classification once challenged. Auditors look at facts on the ground, not the label in the contract — a '1099 Independent Contractor Agreement' is not evidence of contractor status by itself.

### 9.3 Consequences of misclassification

- **Misclassification consequences list** — If a worker is reclassified by DEED as an employee: Retroactive UI contributions for up to 4 years of audit lookback, at the employer's experience rate (or new-employer rate if no history), plus interest and penalties. Retroactive Minnesota income tax withholding liability for the same period (§290.92 imposes joint liability on the employer for tax that should have been withheld). Joint liability for federal FICA and federal income tax withholding (the IRS will follow once DEED has reclassified; DEED routinely shares findings). Penalty under §181.722 for 'willful misrepresentation' of employment status, up to $5,000 per misrepresentation. For construction, treble damages under §181.723 (see §10). ESST and Paid Leave backfill obligations (the worker, having been reclassified to employee, was due ESST accrual and Paid Leave premium contributions for the entire reclassification period). Workers' compensation insurance liability for any work-related injury during the misclassification period that was not covered.  _(§290.92; §181.722; §181.723)_

### 9.4 ABC test? No — Minnesota uses the nine-factor test, not ABC

- **No ABC test in Minnesota** — Some practitioners assume Minnesota uses the ABC test (used by California, Massachusetts, New Jersey, and others). It does not, for general UI purposes. Pending legislation has been introduced in several recent sessions to adopt an ABC test, but as of 2025 has not passed. The nine-factor test remains operative.

> **AUDIT FLASH POINT — construction-industry classification.** Construction is the single highest-audit-risk industry for worker classification in Minnesota. DEED runs targeted construction-industry audits with multiple state agencies (DLI, DOR, Department of Commerce) jointly. The economic incentive to misclassify is large (a 9.0% construction UI rate × $43,000 wage base = $3,870 per worker per year in UI alone, plus workers' comp avoidance, plus the Paid Leave premium starting 2026). The penalty exposure is correspondingly large. Any construction-industry engagement of an individual or a sole-proprietor LLC should be assumed misclassified by default until the ICEC and §10 analysis is completed and documented. See §10.

## 10. Construction Industry — Special Compliance Regime

### 10.1 Overview

- **Construction industry definition and regime elements** — Minnesota Statutes §181.723 establishes a specialized worker classification and licensing regime for the construction industry — defined as building construction or improvement, including residential, commercial, and infrastructure work. The regime imposes: 1. A heightened classification test, requiring the worker to satisfy all of a multi-element test to be treated as an independent contractor (rather than a totality-of-the-circumstances weighing under §9 above). 2. A registration requirement for individuals working as independent contractors in construction. 3. The historical Independent Contractor Exemption Certificate (ICEC) regime, administered by the Department of Labor and Industry (DLI).  _(Minnesota Statutes §181.723)_

(Older practitioner shorthand sometimes calls this the "Carlson certification" framework after the policy debates of the early 2010s. The operative current framework is the DLI ICEC regime and the construction-contractor registration under §326B and §181.723, as amended in 2024.)

### 10.2 The multi-element test for contractor status (§181.723, subd. 4)

- **Multi-element test elements a-i** — To support independent-contractor classification in construction, the hiring party must be able to demonstrate that the worker: a. Maintains a separate business with their own office, equipment, materials, and other facilities. b. Holds (or has applied for) a federal employer identification number (EIN), unless the worker is a sole proprietor without employees who has not been required to obtain one. c. Operates under a written contract that specifies the services to be performed, the rate of pay, and the duration. d. Submits invoices for work completed. e. Is responsible for satisfactory completion of work and may be liable for failure to complete the work. f. Realizes a profit or loss under the contract. g. Has continuing or recurring business liabilities or obligations (e.g., business insurance, rent on a business premises, advertising). h. The success or failure of the business depends on the relationship of business receipts to business expenditures. i. Has established the business with the intent of profit independent of any single hiring party.  _(Minnesota Statutes §181.723, subd. 4)_
- **DLI registration requirement plus all-elements requirement** — Plus, importantly: the worker must be registered with the DLI as an independent contractor (or hold an active ICEC if the legacy ICEC regime applies to the engagement). All elements must be satisfied. This is materially stricter than the nine-factor weighing in §9.2.  _(Minnesota Statutes §181.723, subd. 4)_

### 10.3 Registration with DLI

- **DLI annual registration requirements** — Individuals working as independent contractors in construction must register with the DLI annually. The registration: - Identifies the individual by name, address, EIN, and the type of construction work performed. - Costs a nominal annual fee. - Is publicly searchable by hiring parties, so a general contractor can verify a sub's registration before engagement. The hiring party should retain a copy of the registration in the project file at the time of engagement, and refresh annually.  _(Minnesota DLI, construction-industry independent-contractor registration portal)_

### 10.4 Penalties for misclassification in construction

- **Penalties under §181.723 subd. 8** — §181.723, subd. 8 imposes: - A penalty of up to $5,000 per individual misclassified. - Treble damages to the misclassified individual for unpaid wages, overtime, and benefits. - Joint and several liability of officers, directors, and managing agents who knowingly permitted the misclassification. - Possible debarment from public construction contracts. In addition, DLI and DEED routinely coordinate on construction-industry investigations, so a finding by one agency typically produces parallel findings by the other.  _(Minnesota Statutes §181.723, subd. 8)_

### 10.5 Prevailing wage and apprenticeship overlay

- **Overlay rules for public construction projects** — Where the construction work is on a public project, additional rules apply: - Minnesota Prevailing Wage Act (§177.41 et seq.). - Federal Davis-Bacon Act (40 U.S.C. §3141 et seq.) for federally funded projects. - Apprenticeship registration with the DLI Apprenticeship Division for apprentice classifications. These are outside the scope of this skill but should trigger a referral to a credentialed prevailing-wage specialist on any public project.  _(Minnesota Prevailing Wage Act §177.41 et seq.; Federal Davis-Bacon Act 40 U.S.C. §3141 et seq.)_

### 10.6 Workers' compensation in construction

- **Workers' comp mandatory coverage and construction risk** — Workers' compensation insurance is mandatory for all Minnesota employers with at least one employee (Minnesota Statutes §176.181), with no employer-size carve-out. Construction-industry workers' comp rates are among the highest in the state by class code, often exceeding 10% of payroll for high-risk classes (roofing, framing, excavation). Misclassification "savings" from avoiding workers' comp are precisely the kind of artifact that triggers a §181.723 enforcement action.  _(Minnesota Statutes §176.181)_

> AUDIT FLASH POINT — construction multi-agency enforcement. A construction-industry employer in Minnesota faces parallel enforcement risk from DEED (UI), DOR (withholding), DLI (§181.723, prevailing wage, workers' comp), and the Attorney General (criminal wage theft). These agencies share information. A single misclassified worker can trigger findings across all four agencies. The compliance posture for any construction engagement of a non-W-2 worker should be: (1) §181.723 multi-element test documented in writing, (2) DLI registration verified and copy on file, (3) written contract per §181.723(c), (4) invoices in file, (5) the worker's separate-business indicia (EIN, business insurance, business address) verified. Anything less is a misclassification risk.

## 11. Worked Examples

### Example 1 — Small non-construction employer (5 employees, 2025 full year)

Facts: ACME Software Studio LLC, a Minneapolis-based small software development shop, has 5 W-2 employees throughout 2025. Annual salaries: $120,000, $95,000, $85,000, $70,000, $55,000. The owner (also a W-2 employee at $120,000) is exempt. Two engineers receive year-end bonuses of $10,000 each in December 2025. ACME has been registered with DEED and DOR since 2020 and is on a 1.4% UI experience rate. The DOR has classified ACME as a monthly withholding depositor.

MN PIT withholding (regular payroll, illustrative for the $95,000 employee, single, 2 W-4MN allowances): - Annualized wages: $95,000. - Subtract 2 × Minnesota per-allowance value (~$5,050 in 2025 per DOR booklet): –$10,100. - Taxable wage base for MN: $84,900. - Apply 2025 single brackets (5.35% / 6.80% / 7.85% / 9.85%) — the bulk of $84,900 falls in the 6.80% bracket with a portion at 7.85%. - Approximate annual Minnesota tax: ~$5,200. - Per pay period (biweekly, 26 periods): ~$200 per check.

Supplemental withholding on December bonuses: - Each engineer: $10,000 × 6.25% = $625 Minnesota withholding on the supplemental payment, paid separately from the regular December check.

UI: - 2025 wage base: $43,000 per employee. - Five employees × $43,000 = $215,000 total taxable wages (each exhausted by mid-year on a >$43k salary; the $55,000 employee also exhausts). - UI rate: 1.4% experience + 0.10% Workforce Development Fee = 1.5%. - Total 2025 UI: $215,000 × 1.5% = $3,225.

Deposit cadence: - Monthly Minnesota withholding deposits via Form MW-1 in e-Services, due the 15th of the following month. - Quarterly Minnesota withholding return (MWR) and quarterly UI wage detail, due the last day of the month following each quarter.

ESST: - Five employees × ~2,080 hours each = 10,400 hours. - At 1 hour per 30 hours worked = ~347 hours of ESST accrual per year aggregate, capped at 48 hours per employee per year (240 hours aggregate). - All five employees are well over the 48-hour cap; ACME's actual exposure is 5 × 48 = 240 hours per year of ESST. At an average $40/hour blended rate, the cost ceiling if all ESST is used is $9,600.

WTPA: - Notice at hire for each employee, plus update notice issued when the December bonus is announced (bonuses are a change in pay terms; the safer practice is to document via written notice).

2026 Paid Leave readiness (action in 2025): - Configure payroll for 0.44% employer + 0.44% employee starting January 1, 2026. - Estimated 2026 cost: ($120k + $95k + $85k + $70k + $55k) = $425k × 0.44% employer share = $1,870 employer Paid Leave premium for 2026, plus the same on the employee side. - Issue employee notice by December 1, 2025; update handbook; post DEED poster; designate leave administrator.

### Example 2 — Construction-industry single-trade contractor (3 W-2 employees + 1 questionable subcontractor)

Facts: NorthPoint Roofing LLC, a new Minneapolis-area roofing company, started operations January 2025. The owner is a single-member LLC owner taxed on Schedule C (and not a W-2 employee of the LLC). NorthPoint hires three crew members as W-2 employees at $60,000 each, and engages a fourth individual ("Sam") as a "1099 contractor" at the same effective rate. Sam works on NorthPoint's jobs only, uses NorthPoint's ladders and safety harnesses, is dispatched by NorthPoint's owner each morning, and submits a weekly invoice for hours worked × $30/hour. Sam has not registered with DLI as an independent contractor.

Analysis under §181.723: - (a) Separate business with own equipment? No — Sam uses NorthPoint's tools. - (c) Written contract specifying services, rate, duration? Not adequately — only a verbal arrangement plus invoices. - (e) Responsible for satisfactory completion, with liability for failure? No — Sam is paid hourly regardless of outcome. - (f) Realizes profit or loss? No — Sam's compensation is hourly, no entrepreneurial risk. - (g) Continuing business liabilities (insurance, advertising, etc.)? No. - DLI registration as an independent contractor? No.

Conclusion: Sam fails the §181.723 multi-element test on at least six elements. Sam is misclassified. He should be a W-2 employee.

Exposure if challenged: - UI: NorthPoint is new in 2025, construction industry, on the ~9.0% new-employer rate. Sam's 2025 wages of ~$60,000 produce taxable wages of $43,000 × 9.0% = $3,870 unpaid UI contributions, plus penalties and interest. - Minnesota withholding: $60,000 × roughly 6% average effective rate = ~$3,600 unpaid state withholding, plus joint liability if Sam does not pay his own M1. - §181.723 civil penalty: up to $5,000. - Treble damages for unpaid overtime if Sam worked >40 hours in any week without being paid 1.5× — the employer's potential exposure here is multiples of the underpaid overtime. - Workers' comp: if Sam was injured during the period, NorthPoint is the responsible employer with no policy in place — uninsured-employer exposure is the full medical and indemnity cost. - Federal: parallel federal exposure for FICA, FUTA, and federal income tax withholding under §3509 / §530. - 2026 forward: NorthPoint would also owe Paid Leave premium back to January 1, 2026 if the misclassification continues.

Remediation: reclassify Sam as a W-2 employee effective immediately. File an amended UI wage detail. Provide Sam with the WTPA written notice. Add him to the ESST tracker. Confirm workers' comp coverage. Issue a Form W-2 at year-end. Consult counsel about Section 530 safe harbor for federal exposure (state has no parallel safe harbor under §181.723).

### Example 3 — Mid-size employer entering 2026 Paid Leave

Facts: GoodSoft Inc., a 35-employee Minneapolis software product company with $4M annual payroll (average salary $114k), runs payroll through Gusto. The company offers unlimited PTO and has never tracked accrued sick time. The CFO realizes in October 2025 that the company has compliance work to do for both ESST and the 2026 Paid Leave rollout.

ESST gap analysis (effective retroactively to 2024): - Unlimited PTO does not satisfy §181.9447 without explicit ESST tracking. Pay-stub disclosure of accrued/used ESST is required; GoodSoft has not been doing this. - The fix: configure Gusto to track ESST as a separate bucket beginning the next pay period, with front-loaded 48 hours per employee per year going forward. Issue an updated WTPA notice and an ESST policy in the handbook. - 2024–2025 retroactive exposure: difficult to quantify but likely limited because no employees appear to have been denied leave; the violation is recordkeeping, not denial. DLI penalty exposure for pure recordkeeping violations is typically remediable with a documented corrective action plan.

2026 Paid Leave premium budget: - Taxable wages capped at SSN base (~$176k 2025; 2026 base TBD). With most of the 35 employees earning above the SSN cap is unlikely; assume average $114k × 35 = $3,990,000 total premium base (all wages well under the SSN cap). - Employer share: $3,990,000 × 0.44% = $17,556 in 2026 employer Paid Leave premium. - Employee share: $17,556 (if employer withholds; otherwise add to employer cost if employer absorbs). - Quarterly remittance through DEED portal, starting April 30, 2026 (Q1 2026).

2025 Q4 readiness checklist: - October 2025: configure Gusto for Paid Leave deduction code; confirm Gusto's 2026 release supports MN Paid Leave. - November 2025: draft employee notice (DEED model); update handbook; identify designated leave administrator (HR director). - December 1, 2025: distribute employee notice in writing and electronically. - December 31, 2025: post DEED workplace notice; confirm payroll system tax-table update has loaded for Jan 1. - January 1, 2026: deductions begin on the first pay date of the year; leave claims may be filed by employees beginning that day.

Multi-state: GoodSoft has 3 remote employees outside Minnesota (1 in WI, 1 in ND, 1 in TX). Apply the §268B localization test for each; in this fact pattern, the WI and TX employees are not Minnesota employees for Paid Leave, the ND employee may be (depending on whether services are localized in MN vs. ND — likely not). Document the determination in the payroll file.

## 12. Practitioner Quick Reference

**Practitioner Quick Reference table**  _(Section 12. Practitioner Quick Reference)_

| Item | 2025 | 2026 transition |
| --- | --- | --- |
| MN PIT brackets | 5.35% / 6.80% / 7.85% / 9.85% | Indexed; rates unchanged |
| MN supplemental rate | 6.25% | Unchanged barring legislation |
| MN UI wage base | $43,000 | Indexed annually (~$44,000 expected) |
| UI experience rate range | 0.10% – 9.0% | Indexed |
| UI new-employer (non-construction) | ~1.0% | Indexed |
| UI new-employer (construction) | ~9.0% | Indexed |
| Withholding deposit thresholds | Monthly >$1,500/yr prior; else quarterly | Unchanged |
| W-2/W-3M filing deadline | January 31 | Unchanged |
| ESST accrual | 1 hr per 30 hrs worked | Unchanged |
| ESST annual cap | 48 hrs/year, 80 hrs balance | Unchanged |
| MN Paid Leave premium | Not yet collected | **0.88% combined, 0.44% / 0.44% split, effective Jan 1, 2026** |
| MN Paid Leave wage base | n/a | ~SSN base (~$176k+) |
| WTPA notice | Required at hire and on material change | Unchanged |
| Final wages — discharged | Within 24 hrs of demand; else next payday (≤20 days) | Unchanged |
| Final wages — voluntary quit | Next regular payday (≤20 days) | Unchanged |
| Construction classification | §181.723 multi-element + DLI registration | Unchanged |

## 13. Self-Checks (run before delivering output)

1. Did the engagement involve construction work? If yes, did the analysis run through §10 in addition to §9? 2. Was a W-4MN obtained for every Minnesota employee, including any employee who completed only a post-2020 federal W-4? 3. Does the year-end W-3M total tie to the sum of the four MWR returns AND to the sum of W-2 box 17? 4. Did UI wage detail correctly include all employees with hours worked, with no nil-quarter return missed? 5. Is the employer tracking ESST as a separate bucket, with accrual and balance on every pay stub? 6. Has the 2026 Paid Leave readiness checklist been worked through item-by-item, with December 1, 2025 employee notice and January 1, 2026 system-readiness milestones flagged? 7. Has the WTPA notice been issued at hire and refreshed on every material change for the period under review? 8. For any 1099 contractor, has the §9 nine-factor (general) or §10 multi-element (construction) test been documented in writing? 9. Were final wages for any separated employees paid by the next regular payday following separation, with shorter timing applied where a discharged employee demanded earlier payment? 10. Has the reviewer (credentialed Minnesota payroll professional) signed off in writing before any filing is submitted?

## 14. Citations

- Minnesota Statutes Chapter 290 (income tax). - Minnesota Statutes Chapter 268 (unemployment insurance). - Minnesota Statutes Chapter 268B (paid leave), as enacted by 2023 Laws Ch. 59 and amended by 2024 Laws Ch. 127. - Minnesota Statutes §181.032 (earnings statements; WTPA). - Minnesota Statutes §181.101 (final wages; WTPA). - Minnesota Statutes §181.13, §181.14 (separation pay timing). - Minnesota Statutes §181.722, §181.723 (worker misclassification; construction industry). - Minnesota Statutes §181.9445 – §181.9448 (Earned Sick and Safe Time). - Minnesota Statutes §326B (construction-industry licensing and DLI authority). - Minnesota Statutes §177.41 et seq. (Minnesota Prevailing Wage Act). - Minnesota DOR, Minnesota Income Tax Withholding Instruction Booklet and Tax Tables (annual; 2025 edition). - Minnesota DEED, UI Employer Handbook (2025). - Minnesota DEED, Family and Medical Benefits Insurance Division publications (2024–2025 readiness materials). - Minnesota DLI, ESST employer guidance (2024, updated 2025). - Minnesota DLI, construction-industry independent-contractor registration portal.

## 12. Practitioner Quick Reference

- **MN PIT brackets** — 5.35% / 6.80% / 7.85% / 9.85%  _(Indexed; rates unchanged)_
- **MN supplemental rate** — 6.25%  _(Unchanged barring legislation)_
- **MN UI wage base** — $43,000  _(Indexed annually (~$44,000 expected))_
- **UI experience rate range** — 0.10% – 9.0%  _(Indexed)_
- **UI new-employer (non-construction)** — ~1.0%  _(Indexed)_
- **UI new-employer (construction)** — ~9.0%  _(Indexed)_
- **Withholding deposit thresholds** — Monthly >$1,500/yr prior; else quarterly  _(Unchanged)_
- **W-2/W-3M filing deadline** — January 31  _(Unchanged)_
- **ESST accrual** — 1 hr per 30 hrs worked  _(Unchanged)_
- **ESST annual cap** — 48 hrs/year, 80 hrs balance  _(Unchanged)_
- **MN Paid Leave premium** — Not yet collected  _(**0.88% combined, 0.44% / 0.44% split, effective Jan 1, 2026**)_
- **MN Paid Leave wage base** — n/a  _(~SSN base (~$176k+))_
- **WTPA notice** — Required at hire and on material change  _(Unchanged)_
- **Final wages — discharged** — Within 24 hrs of demand; else next payday (≤20 days)  _(Unchanged)_
- **Final wages — voluntary quit** — Next regular payday (≤20 days)  _(Unchanged)_
- **Construction classification** — §181.723 multi-element + DLI registration  _(Unchanged)_
