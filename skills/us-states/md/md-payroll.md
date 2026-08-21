---
name: md-payroll
description: Tier 2 Maryland content skill for employer payroll compliance covering tax year 2025. Includes the MD PIT brackets up to 5.75% state plus county tax 2.25-3.20% (effective combined 4.25-8.95%), MW507 state W-4, MW-506 quarterly withholding, MD SUI wage base $8,500 with rates 0.30-7.50%, the 24-county + Baltimore City local tax structure (highest counties Howard/Montgomery/PG/Baltimore City at 3.20%), Maryland Healthy Working Families Act (Sick & Safe Leave 1 hour per 30 hours), reciprocal agreements with DC/PA/VA/WV exempting non-residents, and ABC contractor classification test.
jurisdiction: US-MD
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MD Payroll

## Maryland Payroll — Employer Compliance (Tax Year 2025)

## 1. Scope

This skill covers Maryland-specific payroll obligations for employers paying Maryland-resident employees or employing nonresidents who perform services in Maryland during tax year 2025. The skill addresses:

- Maryland personal income tax (PIT) withholding under Md. Code Ann., Tax-General §10-901 et seq.
- The stacked local income tax (county tax + Baltimore City) under Md. Code Ann., Tax-General §10-103 and §10-106
- Form MW507 (Employee's Maryland Withholding Exemption Certificate) and MW507M (military spouse)
- Form MW-506 (Employer's Return of Income Tax Withheld) and MW-508 (annual reconciliation)
- Maryland State Unemployment Insurance (SUI) under Md. Code Ann., Labor and Employment §8-101 et seq.
- The Maryland Healthy Working Families Act (Md. Code Ann., L&E §3-1301 et seq.)
- The Maryland Workplace Fraud Act ABC test for worker classification under Md. Code Ann., L&E §3-903
- Reciprocity agreements between Maryland and DC, PA, VA, and WV
- New hire reporting to the Maryland State Directory of New Hires
- Final pay rules under Md. Code Ann., L&E §3-505

OUT OF SCOPE: federal income tax withholding (see us-federal-payroll), federal FUTA, federal FICA, Maryland personal income tax filing for the employee (Form 502), Maryland corporate income tax, Maryland sales and use tax, Maryland Paid Family and Medical Leave Insurance (FAMLI) employer/employee premiums (deferred to a future revision when contributions commence under the current statutory schedule), and household employer special rules.

MUST be loaded alongside us-tax-workflow-base v0.2 or later. Maryland employers and Maryland-source wage income only.

## 2. Maryland State Personal Income Tax Brackets (2025)

Maryland imposes a graduated state income tax under Tax-General §10-105. The state brackets for tax year 2025 are:

### Single, Married Filing Separately, Dependent Filer

**Single, Married Filing Separately, Dependent Filer**  _(Tax-General §10-105)_

| Taxable income over | But not over | State rate |
| --- | --- | --- |
| $0 | $1,000 | 2.00% |
| $1,000 | $2,000 | 3.00% |
| $2,000 | $3,000 | 4.00% |
| $3,000 | $100,000 | 4.75% |
| $100,000 | $125,000 | 5.00% |
| $125,000 | $150,000 | 5.25% |
| $150,000 | $250,000 | 5.50% |
| $250,000 | — | 5.75% |

### Married Filing Jointly, Head of Household, Qualifying Surviving Spouse

**Married Filing Jointly, Head of Household, Qualifying Surviving Spouse**  _(Tax-General §10-105)_

| Taxable income over | But not over | State rate |
| --- | --- | --- |
| $0 | $1,000 | 2.00% |
| $1,000 | $2,000 | 3.00% |
| $2,000 | $3,000 | 4.00% |
| $3,000 | $150,000 | 4.75% |
| $150,000 | $175,000 | 5.00% |
| $175,000 | $225,000 | 5.25% |
| $225,000 | $300,000 | 5.50% |
| $300,000 | — | 5.75% |

## 2. Maryland State Personal Income Tax Brackets (2025)

- **Employer withholding tables** — For employer withholding the Comptroller publishes the 2025 Employer Withholding Tables (Publication "Maryland Employer Withholding Guide" with revision date January 2025). The tables embed both the state rate and the county rate so that an employer applies a single combined withholding rate based on the employee's county of residence as declared on the MW507.  _(Maryland Comptroller, Employer Withholding Guide (revision January 2025))_

## 3. County Tax Stacked on State (Local Income Tax)

Maryland is unusual among US states in that the "local" income tax is administered through the state withholding system and is mandatory in every jurisdiction. Every Maryland resident pays a local tax to one of 24 counties or to Baltimore City, in addition to the state tax. The rate is set annually by each county council and certified to the Comptroller. The local tax piggybacks on the same taxable income base used for the state tax.

### County / Baltimore City Tax Rates for 2025

**County / Baltimore City Tax Rates for 2025**  _(certified county rates 2025)_

| Jurisdiction | 2025 rate | Effective combined top rate (state 5.75% + local) |
| --- | --- | --- |
| Allegany County | 3.05% | 8.80% |
| Anne Arundel County | 2.81% (graduated; top rate) | 8.56% |
| Baltimore City | 3.20% | 8.95% |
| Baltimore County | 3.20% | 8.95% |
| Calvert County | 3.00% | 8.75% |
| Caroline County | 3.20% | 8.95% |
| Carroll County | 3.03% | 8.78% |
| Cecil County | 2.80% | 8.55% |
| Charles County | 3.03% | 8.78% |
| Dorchester County | 3.20% | 8.95% |
| Frederick County | 2.96% (graduated; top rate) | 8.71% |
| Garrett County | 2.65% | 8.40% |
| Harford County | 3.06% | 8.81% |
| Howard County | 3.20% | 8.95% |
| Kent County | 3.20% | 8.95% |
| Montgomery County | 3.20% | 8.95% |
| Prince George's County | 3.20% | 8.95% |
| Queen Anne's County | 3.20% | 8.95% |
| St. Mary's County | 3.10% | 8.85% |
| Somerset County | 3.20% | 8.95% |
| Talbot County | 2.40% | 8.15% |
| Washington County | 2.95% | 8.70% |
| Wicomico County | 3.20% | 8.95% |
| Worcester County | 2.25% | 8.00% |
| Nonresident rate (special) | 2.25% (statutory; in lieu of county tax for out-of-state residents working in MD) | 8.00% |

- **Lowest/highest county rates and graduated brackets** — The lowest county rate is Worcester at 2.25%; the highest county rates are 3.20% (Howard, Montgomery, Prince George's, Baltimore City, Baltimore County, Caroline, Dorchester, Kent, Queen Anne's, Somerset, Wicomico). Anne Arundel County and Frederick County adopted graduated local brackets; for withholding purposes the top marginal local rate is used unless the employee provides the lower-bracket certification on the MW507 worksheet.  _(MW507 worksheet)_

### Special Nonresident Tax

- **Special Nonresident Tax** — Under Tax-General §10-106.1, Maryland imposes a "Special Nonresident Tax" of 2.25% on Maryland-source income earned by nonresidents (i.e., individuals whose state of domicile is not Maryland). The 2.25% rate is in lieu of the local county tax that a Maryland resident would pay. It applies to wages earned by: - Pennsylvania residents earning wages in Maryland (but only if the PA resident is NOT covered by the MD-PA reciprocal agreement — see §7 below) - Virginia residents earning wages in Maryland (subject to MD-VA reciprocity) - West Virginia residents earning wages in Maryland (subject to MD-WV reciprocity) - DC residents earning wages in Maryland (subject to MD-DC reciprocity) - Residents of any other state (no reciprocity available)  _(Tax-General §10-106.1)_

> AUDIT FLASH POINT — missed local/county withholding. The single most common audit finding by the Comptroller of Maryland's Compliance Division is failure to withhold the county component. An employer who treats Maryland income tax as a flat 5.75% (state only) and ignores the 2.25–3.20% local stack is short by 39–56% of the actual liability. The Comptroller assesses the difference against the employer under Tax-General §13-704, plus interest at 11.5% per annum (2025 rate set by §13-604) plus a §13-701 penalty of up to 25%. Always verify that the withholding table used reflects the employee's certified county of residence on the MW507, not just "Maryland".

> AUDIT FLASH POINT — wrong county selected. Each employee must certify their county of residence on Line 4 of MW507. An employer that defaults all employees to the employer's county (e.g., Baltimore City because that is where the office sits) when employees actually live in lower-rate counties (e.g., Worcester at 2.25%) overcollects from the employee; the inverse undercollects. The MW507 county code is the controlling document — keep the signed original in the employee file for at least 4 years.

## 4. MW507 — Employee's Maryland Withholding Exemption Certificate

Form MW507 is the Maryland equivalent of the federal Form W-4. Every new hire must complete it on or before the first day of work. It captures:

- Line 1: number of personal exemptions claimed (default 1 per personal exemption — for 2025 the exemption value is $3,200 per exemption, phasing out for federal AGI over $100,000)
- Line 2: additional withholding amount per pay period
- Line 3: exempt from MD income tax due to MSRRA (military spouse) — use MW507M
- Line 4: county of residence (or "Baltimore City" — Baltimore City is NOT in Baltimore County and must be selected separately)
- Line 5: exempt from withholding because the employee meets the under-threshold criteria (no MD tax liability in prior year AND no MD tax liability expected in current year)
- Line 6: claim of total exemption because the employee is a nonresident of MD AND a resident of a reciprocal state (PA, VA, WV, DC) and has filed the appropriate documentation
- Line 7: claim of exemption as Pennsylvania resident under specific reciprocal agreement terms
- Line 8: claim of exemption as Virginia or West Virginia resident under reciprocity

The MW507 must be renewed every year if Line 3, Line 5, Line 6, Line 7, or Line 8 is checked (exemption claims expire annually). A continuing employee who simply changes their county of residence may submit a new MW507 mid-year and the employer must apply the new county rate beginning with the next pay period.

### MW507M — Military Spouses Residency Relief Act

- **MW507M requirements** — Form MW507M implements the federal Military Spouses Residency Relief Act (MSRRA) as amended by the Veterans Auto and Education Improvement Act of 2022. A military spouse who is physically present in Maryland solely because of a service member's military orders, and who is a domiciliary of a state other than Maryland, may elect to be exempt from MD income tax withholding by filing MW507M annually with proof of: - the service member's current orders - the spouse's out-of-state driver's license or voter registration (proof of non-MD domicile) - a copy of the service member's most recent LES The 2022 federal amendment allows the spouse to choose the service member's state of legal residence even if the spouse never lived there. The employer keeps MW507M on file; the employee files no Maryland return.  _(50 U.S.C. §4001 (Servicemembers Civil Relief Act — MSRRA basis))_

## 5. MW-506 — Employer's Quarterly Withholding Return

Employers report and remit withheld Maryland income tax on Form MW-506. The deposit/return frequency depends on the prior calendar year's withholding total under COMAR 03.04.01.04:

**Prior year MD withholding deposit frequency table**  _(COMAR 03.04.01.04)_

| Prior year MD withholding | Deposit frequency | Return due dates |
| --- | --- | --- |
| Less than $700 | Annual | January 31 of following year |
| $700 to $14,999.99 | Quarterly | April 30, July 31, October 31, January 31 |
| $15,000 to $49,999.99 | Monthly | 15th of following month |
| $50,000 or more | Accelerated (EFT, within 3 business days of payday for any payday with $700+ withheld) | per accelerated schedule |
| New employer (first year) | Quarterly default | quarterly |

- **Electronic filing and zero returns** — All MW-506 returns must be filed electronically via the Comptroller's bFile system unless the employer obtains a hardship waiver. Even if no tax was withheld in a period, a zero return must be filed.  _(COMAR 03.04.01.04)_
- **MW-508 annual reconciliation** — The annual reconciliation, Form MW-508, is due January 31 of the following year and must transmit W-2 copies for all employees who had MD wages or MD withholding. For 2025 wages the MW-508 is due January 31, 2026. Late MW-508 filing triggers a $100 penalty per W-2 not timely transmitted, capped at $50,000 per year under Tax-General §13-701.  _(Tax-General §13-701)_

> AUDIT FLASH POINT — frequency change not noticed. The Comptroller recalculates each employer's deposit frequency every November based on the trailing four-quarter look-back. The new frequency takes effect January 1. An employer that crosses the $15,000 threshold and continues to file quarterly into the next year accrues underpayment penalties even if all tax is ultimately paid. Always check the November notice from the Comptroller and update the payroll calendar before January 1.

## 6. Maryland SUI (State Unemployment Insurance)

Maryland Unemployment Insurance is administered by the Maryland Department of Labor, Division of Unemployment Insurance under L&E Title 8.

### 2025 Parameters

- **Taxable wage base** — $8,500 per employee per calendar year  _(Md. Code Ann., Labor and Employment Title 8)_
- **Standard contribution rate range** — 0.30% to 7.50%  _(Md. Code Ann., Labor and Employment Title 8)_
- **New employer rate** — 2.60% for the first three calendar years (or until the employer has a chargeable benefit history)  _(Md. Code Ann., Labor and Employment Title 8)_
- **Construction industry new employer rate** — 5.40% (statutorily set above standard new employer rate)  _(Md. Code Ann., Labor and Employment Title 8)_
- **Foreign contractor rate** — Foreign contractor rate (out-of-state employer with first MD operations): the maximum rate of 7.50% applies for the first three years unless an experience transfer is approved  _(Md. Code Ann., Labor and Employment Title 8)_
- **Work Sharing program** — Work Sharing program: available; affects experience rating  _(Md. Code Ann., Labor and Employment Title 8)_
- **2025 fund balance trigger** — Maryland operates on Table A through Table F; the table in effect for 2025 is Table C (mid-range) — confirm in the Comptroller of Labor's annual rate notice mailed each December  _(Maryland DOL DUI BEACON system, 2025 Contribution Rate Table C)_

### Reporting

Quarterly wage reports (Form DLLR/DUI 15) and contribution reports (Form DLLR/DUI 16) are due by the end of the month following the quarter:

**Quarterly wage report due dates**  _(Form DLLR/DUI 15/16)_

| Quarter | Wages reported | Due date |
| --- | --- | --- |
| Q1 | January–March | April 30 |
| Q2 | April–June | July 31 |
| Q3 | July–September | October 31 |
| Q4 | October–December | January 31 |

- **Registration thresholds** — All employers with 1+ employee in 20+ weeks of a calendar year, or who paid $1,500+ in any calendar quarter, must register and file. Domestic employers are subject to a $1,000-per-quarter test. Agricultural employers have the $20,000-per-quarter or 10-employees-in-20-weeks test.  _(Md. Code Ann., Labor and Employment Title 8)_
- **Electronic filing and penalties** — Electronic filing is mandatory through BEACON (the unified MD UI system that replaced the legacy MABS). Late filing penalty is $35 per report plus interest at 1.5% per month on unpaid contributions.  _(Maryland DOL DUI BEACON system)_

## 7. Reciprocal Agreements (DC, PA, VA, WV)

Maryland has bilateral wage-tax reciprocity with four neighboring jurisdictions. Under reciprocity an employee who is a resident of one state but works in the other pays income tax only to their state of residence; the employer of work withholds only for the employee's state of residence.

### MD–DC Reciprocity

- **MD-DC reciprocity terms** — Under the long-standing administrative agreement between MD and DC: - A Maryland resident working in DC pays only Maryland income tax. The DC employer should not withhold DC tax; the MD employee files a DC Form D-4A and the MD W-2 reflects MD withholding only. - A DC resident working in Maryland pays only DC income tax. The MD employer should withhold DC tax (not MD state tax and not MD county tax). The DC resident files MW507 Line 6 claiming exemption from MD tax. Note: DC does not have local/county tax, so MD residents working in DC owe only the MD state-plus-county stack to MD.

### MD–PA Reciprocity

- **MD-PA reciprocity terms** — The MD–PA agreement is the most nuanced of the four because PA's flat 3.07% state tax and the various PA local Earned Income Tax (EIT) rates (typically 1.0–3.9%) interact differently: - A PA resident working in MD: exempt from MD state income tax AND exempt from the MD 2.25% nonresident tax. The PA employee files MW507 Line 7. However, the MD employer is required by the agreement to withhold the PA local EIT (the resident's home municipality rate) and remit it to the PA tax collector that covers the employee's PA residence. This is the so-called "courtesy withholding" obligation under Act 32. - A MD resident working in PA: exempt from PA state tax; the PA employer should not withhold PA state tax. The MD resident files PA Form REV-419. The MD resident is still subject to PA local EIT in the PA work location, generally at the higher of the resident or non-resident rate, withheld by the PA employer.

### MD–VA Reciprocity

- **MD-VA reciprocity terms** — - A VA resident working in MD: exempt from MD state tax and MD 2.25% nonresident tax. File MW507 Line 8. Employer withholds VA tax instead. - A MD resident working in VA: exempt from VA state tax. File VA Form VA-4.

### MD–WV Reciprocity

- **MD-WV reciprocity terms** — Same structure as MD–VA. A WV resident working in MD files MW507 Line 8 and the employer withholds WV state tax. A MD resident working in WV files WV/IT-104R.

### Reciprocity Does Not Override Local Withholding for Residents

- **Residents remain liable for full MD stack** — Reciprocity only relieves the nonresident from the work-state's tax. A Maryland resident remains liable for the full MD state-plus-county stack on all wages regardless of where earned. An employer with a Maryland resident working remotely from PA must still withhold the MD state tax PLUS the MD county tax for the employee's MD county of residence.

> AUDIT FLASH POINT — multi-state employee, multi-county allocation. An employee who lives in Howard County (3.20%), works two days a week in the DC office, two days a week in the Tysons Corner VA office, and one day a week remotely from a Pennsylvania family cottage requires very careful sourcing. The full wages are subject to MD state 5.75% + Howard 3.20% (because the employee is an MD resident); none of those wages are sourced to DC, VA, or PA (because of MD's reciprocal agreements with each). However, if the employee establishes a tax home outside MD or changes residence mid-year, the analysis flips. Keep contemporaneous time-and-location records for any employee who routinely works from more than one state.

## 8. ABC Test for Worker Classification

- **ABC test scope** — The Maryland Workplace Fraud Act (Md. Code Ann., L&E §3-901 through §3-920) imposes an ABC test for classifying workers in the construction services and landscaping industries. For unemployment insurance purposes statewide (under L&E §8-205), Maryland applies a similar but broader ABC test that resembles California's AB-5 framework.  _(Md. Code Ann., L&E §3-901 through §3-920; L&E §8-205)_
- **Three-prong ABC test** — A worker is presumed to be an employee unless the putative employer can prove ALL THREE: - (A) the worker is free from control and direction of the hiring entity in connection with the performance of the work, both under the contract and in fact; - (B) the work is outside the usual course of the hiring entity's business OR the work is performed outside all of the hiring entity's places of business; AND - (C) the worker is customarily engaged in an independently established trade, occupation, profession, or business of the same nature as the work performed. Prongs A and C track the common-law right-to-control test and the IRS Section 530 safe harbor. Prong B is the strictest — it disqualifies most "core function" subcontractors. A software development firm that hires a "contractor" software developer to write code for the firm's product fails prong B because writing code IS the usual course of the firm's business. The worker is an employee under MD unemployment insurance rules regardless of contract language.  _(Md. Code Ann., L&E §3-901 through §3-920)_
- **Misclassification penalties** — Penalties under L&E §3-909 for knowing misclassification in construction services: $5,000 per misclassified worker for a first violation, $10,000 per worker for repeat violations, plus back taxes, plus restitution to the worker.  _(L&E §3-909)_

### Independent Contractor Affidavit (Construction)

- **Affidavit requirements** — For construction services only, the Workplace Fraud Act prescribes a specific written form — the Independent Contractor Affidavit — that the worker and employer must execute and that the employer must retain for 3 years (L&E §3-906). The affidavit does not by itself satisfy the ABC test; it is documentary evidence that the parties intended an independent contractor relationship but the substantive ABC test still controls.  _(L&E §3-906)_

> AUDIT FLASH POINT — ABC contractor misclassification. The Maryland DOL Joint Enforcement Task Force on Workplace Fraud cross-references 1099-NEC filings with UI wage records. A 1099-NEC issued by an MD employer to a worker who fails the ABC test triggers an audit with retroactive UI contributions, MD income tax withholding back-assessments (the employer is liable for the under-withheld tax under Tax-General §10-906), workers' compensation premiums, and the L&E §3-909 civil penalty. Never accept "they signed a contractor agreement" as a defense — the substantive ABC test is dispositive.

## 9. Maryland Healthy Working Families Act (Sick & Safe Leave)

- **Effective date and general requirement** — Effective February 11, 2018, the Maryland Healthy Working Families Act (L&E §3-1301 et seq.) requires employers to provide earned sick and safe leave.  _(Md. Code Ann., L&E §3-1301 et seq.)_

### Coverage and Accrual

- **Coverage, accrual, caps, carryover** — - All employers with 1+ employee must provide leave; the difference is whether the leave is PAID or UNPAID. - Employers with 15 or more employees (counted as the average number of monthly employees in the immediately preceding year, including FT, PT, and temp; out-of-state workers count) must provide PAID leave. - Employers with fewer than 15 employees must provide UNPAID leave. - Accrual rate: 1 hour of leave per 30 hours worked. - Annual accrual cap: 40 hours per year (employer may set cap at 40 hours; statute does not require more). - Annual usage cap: 64 hours per year. - Carryover: up to 40 unused hours roll over to the next year, unless the employer awards the full 40 hours at the beginning of the year (front-loading), in which case no carryover is required. - Total accrual cap: 64 hours.  _(Md. Code Ann., L&E §3-1301 et seq.)_

### Eligibility

- **Eligibility criteria** — - Employees regularly working 12+ hours per week. - Employee must be at a worksite physically located in Maryland (the law is location-of-work based, not employer-domicile based).  _(Md. Code Ann., L&E §3-1301 et seq.)_

### Permissible Uses

- **Permissible uses of leave** — - The employee's or family member's mental or physical illness, injury, or condition - Preventive medical care for the employee or a family member - Maternity or paternity leave - Absence due to domestic violence, sexual assault, or stalking against the employee or family member "Family member" is broadly defined to include spouse, child (biological, adopted, foster, step), parent, grandparent, grandchild, sibling, and the spouses of those relations.  _(Md. Code Ann., L&E §3-1301 et seq.)_

### Excluded Workers

- **Excluded worker categories** — - Employees who regularly work less than 12 hours per week - Independent contractors (genuine contractors that pass the ABC test) - Workers under 18 - Construction workers covered by a bona fide collective bargaining agreement that expressly waives the act - Certain seasonal/agricultural and as-needed health/human services workers  _(Md. Code Ann., L&E §3-1301 et seq.)_

### Documentation

- **Documentation requirements** — - An employer must provide written notice of the policy to employees. - Each pay statement must show the amount of sick and safe leave available. - Records of accrual and use must be kept for at least 3 years.  _(Md. Code Ann., L&E §3-1301 et seq.)_

### Final Pay and Sick Leave Payout

- **Sick leave payout at termination** — Maryland does NOT require payout of accrued unused sick and safe leave at termination, unlike vacation/PTO, which IS subject to payout under Md. Code Ann., L&E §3-505 if the employer's written policy treats vacation as wages.  _(Md. Code Ann., L&E §3-505)_

## 10. Final Pay Rules

- **Final pay timing and rules** — Md. Code Ann., L&E §3-505 requires that an employer pay all wages due to a separated employee "on or before the day on which the employee would have been paid the wages if the employment had not been terminated." In practice this is the next regular payday. - Voluntary quit: next regular payday. - Involuntary termination: next regular payday. - Accrued vacation/PTO: payable as wages IF the employer's written policy does not contain a forfeiture clause and IF the employer's practice treats it as earned wages. See Catapult Learning, LLC v. Comptroller (Md. App. 2011) for the leading case. - Accrued sick & safe leave: not payable on separation (statutory carve-out). Late payment of final wages can give rise to treble damages under L&E §3-507.2 if the failure to pay was not the result of a bona fide dispute.  _(Md. Code Ann., L&E §3-505, §3-507.2)_

## 11. New Hire Reporting

- **New hire reporting requirements** — Under Family Law §10-118 and Federal PRWORA, Maryland employers must report new hires (and rehires after a 60-day separation) to the Maryland State Directory of New Hires within 20 days of the hire date. - Reporting agency: Maryland State Directory of New Hires (administered by the Maryland Department of Human Services — DHS — Child Support Administration; historically referred to as DHR) - Information required: employee name, address, SSN, hire date, employer name, employer FEIN, employer address - Methods: online at MD-newhire.com, electronic file upload, magnetic media, or W-4 facsimile - Penalty: $20 per unreported new hire; $500 per conspiracy with employee to avoid reporting Multi-state employers may elect to report all new hires to a single state under 42 U.S.C. §653a — file the multistate election with the federal Office of Child Support Enforcement.  _(Family Law §10-118; 42 U.S.C. §653a)_

## 12. Worked Examples

### Example A — Baltimore City Employer, Single MD-Resident Employee

Facts: Acme Crab Cakes LLC operates a restaurant in Baltimore City. It hires Jamal, a single Maryland resident living in Baltimore City, in March 2025 at $52,000/year ($1,000/week gross). Jamal files MW507 claiming 1 personal exemption and Line 4 = "Baltimore City". No additional withholding on Line 2.

Computation per pay period ($1,000 gross):

1. Federal: handled by federal payroll skill — outside this scope.
2. Maryland state tax: using the 2025 Maryland Employer Withholding Tables for Baltimore City (combined state + local rate), the effective withholding rate at this income level is approximately 4.75% state + 3.20% local = 7.95% on each marginal dollar after the standard deduction and one personal exemption.
   - Annual exemption value 2025: $3,200 (one exemption, federal AGI below phaseout)
   - Annual standard deduction 2025 (15% of MD AGI, min $1,800, max $2,700 single): $2,700 cap
   - Annual MD AGI: $52,000
   - MD taxable income: $52,000 − $3,200 − $2,700 = $46,100
   - State tax on $46,100: $90 (on first $1,000 at 2%) + $30 + $40 + $2,043.25 (on $43,100 × 4.75%) = $2,203.25
   - Baltimore City tax on $46,100 × 3.20% = $1,475.20
   - Total annual MD state + local: $3,678.45
   - Per weekly pay period: ~$70.74
3. SUI: Acme's 2025 new-employer rate is 2.60%. Wage base $8,500 means SUI is owed only on the first $8,500 of Jamal's 2025 wages, i.e., $221.00 of SUI for Jamal's first 8.5 weeks; nothing further for the rest of 2025. Reported on DLLR/DUI 15/16 quarterly.
4. Sick & safe leave: Acme has 22 employees so it must provide PAID leave. Jamal accrues 1 hour per 30 hours worked. At 40 hours/week he accrues 40 × (1/30) = 1.333 hours per week, capped at 40 hours/year. The pay statement must show available hours.
5. New hire reporting: Acme submits Jamal's W-4-equivalent data to MD-newhire.com within 20 days of his start date.
6. MW-506: assume Acme is a new employer in 2025 — quarterly default. First MW-506 covering Q1 2025 is due April 30, 2025. Annual MW-508 + W-2s due January 31, 2026.

### Example B — Montgomery County Employer with Northern Virginia Commuters

Facts: BioWidget Inc., a biotech company headquartered in Bethesda (Montgomery County, MD), employs three workers:

- Priya: lives in Rockville, MD (Montgomery County). Salary $120,000.
- Sam: lives in Arlington, VA. Salary $110,000. Commutes to Bethesda 5 days/week.
- Kavita: lives in Fairfax, VA. Salary $130,000. Hybrid — 3 days in Bethesda, 2 days remote from her Fairfax home.

Treatment:

Priya — full MD state + Montgomery County tax. Effective top rate: 5.75% + 3.20% = 8.95% at the margin. Standard MW507 with Line 4 = "Montgomery County". Full state and county withholding on all wages.

Sam — VA resident commuting to MD. MD has full reciprocity with VA. Sam files MW507 Line 8 and BioWidget files a VA-4 to begin withholding Virginia state tax on Sam's wages. NO MD state tax, NO MD county tax, NO MD 2.25% nonresident tax. BioWidget registers as a VA employer for the limited purpose of remitting Sam's VA withholding via Virginia Form VA-5.

Kavita — same as Sam initially. However, the two days Kavita works remotely from VA are VA-sourced, and the three days in Bethesda are MD-sourced. Because of MD-VA reciprocity, the MD-sourced wages are STILL exempt from MD tax — the reciprocity covers all MD-source wages of a VA resident. BioWidget withholds 100% VA tax on Kavita's wages just as for Sam. Note: this is different from non-reciprocal multi-state scenarios where day-counting matters; with MD-VA reciprocity it is residency, not work-location-day-count, that controls.

If Kavita establishes residency in MD mid-year (e.g., moves to Bethesda in September), BioWidget must:
- Stop VA withholding effective the move date.
- Begin MD state + Montgomery County withholding effective the move date.
- File an updated MW507 from Kavita with Line 4 = "Montgomery County".
- Issue a 2025 W-2 with VA wages and tax for January–August, plus MD wages and tax for September–December (or, more practically, allocate based on the actual paydays after the move).

> AUDIT FLASH POINT — multi-county work-day allocations. The trap here is that MD-VA reciprocity makes day-counting irrelevant, but if Kavita instead lived in a non-reciprocal state (say, Delaware) and worked the same 3-MD/2-DE schedule, BioWidget would need to:
> (a) withhold MD state tax + 2.25% MD nonresident tax on the 3-MD-day portion (60% of wages), and
> (b) withhold Delaware tax on the full wages (because DE taxes residents on worldwide income), with a credit-side reconciliation on Kavita's DE return.
> Always confirm reciprocity status BEFORE setting up withholding; don't generalize from one employee to another.

### Example C — Construction Contractor "Independent Contractor" Reclassification

Facts: Charm City Builders LLC, an MD construction firm based in Towson (Baltimore County), pays Diego, a drywall installer, $4,500/month on a 1099-NEC. Diego works 40 hours/week exclusively for Charm City for 11 months in 2025. Charm City supplies the tools, sets the work schedule, supplies the materials, and Diego does not advertise his services or have other clients.

Workplace Fraud Act analysis:

- Prong A (free from control): FAILS. Charm City sets schedule, supplies tools, supervises.
- Prong B (outside usual course or outside places of business): FAILS. Drywall is in the usual course of Charm City's business; work is performed at Charm City's jobsites.
- Prong C (independently established trade): FAILS. No other clients, no advertising.

Diego fails all three prongs. He is an EMPLOYEE under MD law regardless of contract language or his preference.

Consequences for Charm City:

1. Retroactive MD income tax withholding liability under Tax-General §10-906 — Charm City is liable for the under-withheld tax. Assuming Diego is a Baltimore County resident, the rate is 5.75% + 3.20% = 8.95% (top of state bracket only applies above $100k of taxable income; in practice Diego's withholding at this wage level is closer to 4.75% + 3.20% = 7.95% on the marginal dollar).
2. Retroactive SUI contributions on Diego's wages up to the $8,500 wage base. At Charm City's construction-industry new-employer rate of 5.40%, the catch-up is $459 plus interest and 1.5%/month late fee.
3. Civil penalty under L&E §3-909 of $5,000 (first violation in construction).
4. Workers' compensation: separate exposure under Md. Code Ann., L&E Title 9 — Charm City should have been carrying WC coverage for Diego. The Workers' Compensation Commission can assess additional penalties.
5. Federal exposure: 1099-NEC issued in error triggers IRS Section 530 examination and potential FICA, FUTA, and federal income tax under-withholding assessment.
6. Diego's perspective: he can sue for unpaid overtime, sick & safe leave that should have accrued (Charm City has 15+ employees so PAID sick leave), unemployment benefits if separated, and treble damages under L&E §3-507.2 for any unpaid wages.

Remediation: Charm City should reclassify Diego as a W-2 employee going forward, issue corrected payroll records, file Form W-2c if a W-2 was issued for any prior period (none here — only 1099-NEC), file VCSP (Voluntary Classification Settlement Program) with the IRS, and self-disclose to the Comptroller of Maryland for a potentially reduced penalty. Consider whether other 1099-NEC workers in the same role need the same treatment.

> AUDIT FLASH POINT — ABC misclassification cascades. Misclassification of a single worker almost never stays isolated. The MD DOL audit team will demand a list of all 1099-NEC payments and apply the ABC test to each. Companies routinely settle MD payroll audits for 5–15× the cost of the original under-withholding because of the layered penalties (UI + income tax + workers' comp + civil penalty + interest).

## 13. Self-Checks Before Sign-Off

Before delivering a Maryland payroll computation or compliance memo to a reviewer, confirm each of the following:

1. Is the employer's MD Central Registration Number (CRN) and FEIN on file for both withholding and UI?
2. Has every employee submitted an MW507 with a county-of-residence entry on Line 4?
3. Are any MW507 lines 3/5/6/7/8 dated within the past 12 months (annual renewal)?
4. Has the Comptroller's November deposit-frequency notice been reviewed for the upcoming calendar year?
5. For employees in PA, VA, WV, or DC: has the corresponding state's withholding form been filed and is the MD-side withholding properly zeroed out?
6. For employees who moved counties or states mid-year: has the effective-date change been applied at the correct pay period?
7. For any 1099-NEC payments: has each been tested against the three-prong ABC test and documented?
8. Sick & safe leave: is the available balance shown on every pay statement and is the carryover correctly calculated?
9. For a new hire: has the report been transmitted to MD-newhire.com within 20 days?
10. Is the Q4 2025 MW-508 + W-2 reconciliation calendar set for January 31, 2026?

## 14. Citations

- Md. Code Ann., Tax-General §10-103 through §10-106.1 (state and county income tax structure)
- Md. Code Ann., Tax-General §10-901 through §10-913 (withholding)
- Md. Code Ann., Tax-General §13-604, §13-701, §13-704 (interest and penalties)
- COMAR 03.04.01.04 (withholding deposit frequency)
- Md. Code Ann., Labor and Employment Title 8 (Unemployment Insurance)
- Md. Code Ann., Labor and Employment §3-505, §3-507.2 (wage payment)
- Md. Code Ann., Labor and Employment §3-901 through §3-920 (Workplace Fraud Act, ABC test)
- Md. Code Ann., Labor and Employment §3-1301 through §3-1311 (Healthy Working Families Act)
- Md. Code Ann., Family Law §10-118 (new hire reporting)
- 42 U.S.C. §653a (federal new hire reporting framework)
- 50 U.S.C. §4001 (Servicemembers Civil Relief Act — MSRRA basis)
- Maryland Comptroller, Employer Withholding Guide (revision January 2025)
- Maryland DOL DUI BEACON system, 2025 Contribution Rate Table C

## 15. Refusals

- **Refusals list** — This skill will NOT: - Provide federal income tax, FICA, or FUTA computations (refer to us-federal-payroll). - Compute Maryland income tax for the EMPLOYEE's Form 502 (refer to a future md-individual-income-tax skill). - Cover Maryland Paid Family and Medical Leave Insurance (FAMLI) premiums until the contribution schedule is finalized in regulation. - Cover Maryland household employer special rules. - Cover multi-state UI Localization-of-Work analyses where the employee works in 3+ states (refer to a credentialed cross-border payroll specialist). - Substitute for credentialed reviewer sign-off under Circular 230 or under Maryland Board of Individual Tax Preparers oversight.  _(Skill scope definition)_

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
