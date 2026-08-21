---
name: ky-payroll
description: Tier 2 Kentucky content skill for employer payroll compliance covering tax year 2025. Includes the 4.0% flat PIT phasing down to 3.5% in 2026, K-1 quarterly withholding, K-3 annual reconciliation, KY SUI wage base $11,400 with rates 0.225-9.0%, the 200+ city and county occupational license tax system collected by work-location (Louisville 2.2%, Lexington 2.25%), school district wage tax (0.5-0.75% in some districts), reciprocal agreements with OH/IN/IL/MI/VA/WV exempting non-resident employees from KY withholding, and Form OL-3 occupational license return.
jurisdiction: US-KY
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# KY Payroll

## Kentucky Payroll Compliance — Tier 2 Content Skill

## 1. Scope

This skill provides the Kentucky-specific employer payroll content layer for tax year 2025. It is loaded together with the federal payroll baseline (federal income tax withholding, FICA, FUTA, Form 941, Form W-2) and produces the additional Kentucky state and local withholding, unemployment insurance, and occupational license obligations that a Kentucky employer must satisfy.

In scope:
- Kentucky personal income tax (PIT) withholding at the 4.0% flat 2025 rate, including the statutory phase-down to 3.5% for tax year 2026.
- Form K-4 (Kentucky employee withholding allowance certificate) intake and recordkeeping.
- Form K-1 (Kentucky employer quarterly withholding return) preparation and remittance.
- Form K-3 (Kentucky annual reconciliation of income tax withheld) preparation and reconciliation against Forms W-2.
- Kentucky State Unemployment Insurance (SUI) administered by the Kentucky Office of Unemployment Insurance — wage base $11,400, experience-rated employer contribution rates 0.225% to 9.0%, new-employer rate 2.7%, Schedule A trigger.
- The Kentucky local occupational license tax system: ~200 cities, counties, and other taxing districts that impose a tax on wages earned within their jurisdictional boundaries.
- Occupational license withholding determined by employee work location (where the work is physically performed), distinguishing it from Pennsylvania Act 32 which is driven by the higher of work-location or residence-location rates.
- Major locality detail: Louisville/Jefferson County Metro (2.2% resident / 1.45% non-resident effective combined), Lexington-Fayette Urban County Government (2.25%), Northern Kentucky cities (Covington, Newport, Florence), and the county-level occupational license model.
- Form OL-3 (occupational license fee return) — the consolidated quarterly and annual employer return used by most Kentucky localities, in particular Louisville Metro Revenue Commission and Lexington-Fayette LFUCG.
- Kentucky school district occupational license / utility tax on wages — additional 0.5% to 0.75% imposed by certain county school districts on top of the city/county occupational tax stack.
- Reciprocal income tax agreements with Ohio, Indiana, Illinois, Michigan, Virginia, and West Virginia, including the operational mechanics of Form 42A809 (Certificate of Non-Residence) and the absence of any reciprocity for local occupational taxes.
- Worker classification under the standard IRS three-factor common-law test as adopted by the Kentucky Department of Revenue, including the Kentucky-specific construction industry presumption under KRS 341.123.
- Final pay rules under KRS 337.055.

Out of scope (defer to companion skills):
- Federal income tax withholding, FICA, FUTA, Form 941, Form 944, Form 940, Form W-2, Form W-3, Form 1099-NEC — defer to the federal payroll skill.
- Kentucky business entity income tax (LLET, corporate income tax) — defer to ky-business-income-tax.
- Kentucky sales and use tax — defer to ky-sales-tax.
- Multi-state apportionment for employees who physically work in more than one state in the same pay period beyond the simple reciprocal-state commuter pattern — defer to multistate-payroll-allocation.
- Workers' compensation insurance premium administration — handled by carrier, not by this skill.
- Garnishments, child support orders, and income execution under KRS 425.501 et seq. — out of scope.

This skill assumes the employer is a Kentucky-domiciled or Kentucky-registered employer with at least one employee whose Kentucky tax obligations need to be administered, and that the reviewer is a CPA, EA, or attorney credentialed to sign off on the deliverable.

## 2. Conservative Defaults

- **Unconfirmed residence default** — If the residence of an employee cannot be confirmed, assume the employee is a Kentucky resident and withhold full Kentucky PIT at 4.0%. Do not apply a reciprocal-state exemption without a signed Form 42A809 on file.  _(Section 2)_
- **Unconfirmed work location default** — If the work location of an employee cannot be confirmed, assume the work is performed at the employer's registered Kentucky business address for purposes of local occupational tax withholding.  _(Section 2)_
- **Locality tax presumption** — If a city or county locality has any imposed occupational tax and the work location falls within the locality boundaries, withhold local occupational tax. Do not assume a 'small employer' or 'low wage' exemption unless the locality's ordinance is on file showing such an exemption.  _(Section 2)_
- **School district stacking default** — If a school district imposes an occupational license tax and the employee's work location is within the district boundaries, stack the school district tax on top of the city and county tax. Do not net or offset stacks unless a specific reciprocity ordinance exists between the localities.  _(Section 2)_
- **Worker classification default** — If a worker's classification as employee vs independent contractor is ambiguous, default to employee classification. Kentucky construction-industry workers receive an additional employee presumption under KRS 341.123 that the reviewer must rebut affirmatively.  _(KRS 341.123)_
- **SUI rate uncertainty default** — For Kentucky SUI rate uncertainty (e.g., the employer has not yet received the annual rate notice), use the most recent prior-year rate plus a conservative 0.10% buffer; do not use the new-employer 2.7% rate unless the employer is genuinely within its first three calendar years of liability.  _(Section 2)_

## 3. Kentucky Personal Income Tax (PIT) — 4.0% Flat Rate

### 3.1 Rate history and 2026 phase-down

- **Flat tax origin** — Kentucky moved from a graduated income tax to a flat tax effective January 1, 2023 under House Bill 8 (2022 Regular Session). The flat rate has been ratcheted down by 0.5 percentage points per year when statutory revenue triggers under KRS 141.020(2)(d) are satisfied.  _(KRS 141.020(2)(d); HB 8 (2022))_
- **Tax year 2023 rate** — 4.5%  _(KRS 141.020)_
- **Tax year 2024 rate** — 4.0%  _(KRS 141.020)_
- **Tax year 2025 rate** — 4.0% (no reduction triggered for 2025 — the FY2024 General Fund condition for an additional reduction was not satisfied at the cutoff for the 2025 rate determination)  _(KRS 141.020)_
- **Tax year 2026 rate** — 3.5% (House Bill 1, 2025 Regular Session, enacted February 6, 2025, set the 2026 rate at 3.5% on a one-time legislative basis rather than relying on the automatic trigger)  _(HB 1 (2025))_
- **2026 rate effective date for payroll** — For payroll computations dated on or after January 1, 2026, the withholding rate becomes 3.5% and employers must update payroll software accordingly. Employers should not pre-emptively use the 2026 rate for 2025 payrolls.  _(HB 1 (2025))_

AUDIT FLASH POINT — RATE TIMING. A common audit finding is the use of the wrong year's flat rate at year-end / new-year crossover, particularly for late-December bonus runs that are paid in early January. The constructive-receipt rule under KRS 141.310(2) controls — the rate applicable is the rate in effect when the wages are paid, not when they are earned. A December 26 bonus accrued for 2025 work and paid January 2, 2026 is withheld at 3.5%, not 4.0%.

### 3.2 Supplemental wages

- **Supplemental wages withholding rate** — Kentucky withholds on supplemental wages (bonuses, commissions, retroactive pay, severance) at the same 4.0% flat rate for 2025. There is no separate 'supplemental' rate as exists for some other states. Whether the employer aggregates supplemental wages with regular wages or treats them separately, the rate applied is the same flat rate.  _(Section 3.2)_

### 3.3 Standard deduction in withholding tables

- **2025 annual standard deduction** — $3,270  _(KRS 141.081; 103 KAR 18:070)_
- **Withholding computation steps** — 1. Annualize gross wages. 2. Subtract the 2025 annual standard deduction of $3,270. 3. Apply the 4.0% flat rate. 4. De-annualize to the pay period.  _(103 KAR 18:070)_
- **2026 projected standard deduction** — $3,370 (projected under KRS 141.081(2)(a)'s annual cost-of-living adjustment; confirm against the Department of Revenue's published 2026 withholding instructions before processing the first 2026 pay run)  _(KRS 141.081(2)(a))_

### 3.4 Form K-4 (Employee Withholding Allowance Certificate)

- **Form K-4** — Kentucky's Form K-4 is required for every Kentucky employee. The current revision (Form K-4, revised December 2022) was simplified to align with the flat-tax structure and now allows employees to claim: exemption from withholding (full exemption) — only if the employee had no Kentucky income tax liability in the prior year and reasonably expects none for the current year, expiring February 15 of the following year, consistent with the federal Form W-4 exemption mechanic; additional withholding (a flat dollar amount per pay period); reciprocal-state exemption — a non-resident employee from Ohio, Indiana, Illinois, Michigan, Virginia, or West Virginia who works in Kentucky but lives in the reciprocal state must file Form 42A809 (Certificate of Non-Residence) with the Kentucky employer to claim exemption from Kentucky PIT withholding. See Section 9.  _(Form K-4 (rev. Dec 2022))_
- **K-4 retention and default** — Form K-4 is retained in the employer's records and is not filed with the Kentucky Department of Revenue unless requested. If the employee fails to provide a K-4, the employer withholds as if the employee were a Kentucky resident with no additional withholding claimed.  _(Section 3.4)_

## 4. Form K-1 — Employer Quarterly Withholding Return

### 4.1 Filing frequency

- **Twice-monthly (semi-monthly remittance) threshold** — average monthly liability $50,000 or more  _(103 KAR 18:150)_
- **Monthly threshold** — average monthly liability of $400 to less than $50,000  _(103 KAR 18:150)_
- **Quarterly threshold** — average monthly liability under $400  _(103 KAR 18:150)_
- **Annual threshold** — very small employers with total annual liability under $400  _(103 KAR 18:150)_
- **K-1 terminology** — The 'K-1' terminology is sometimes loosely used to cover all three filing-frequency variants. Strictly: Form K-1 is the return — filed by every employer regardless of frequency, used to report total Kentucky withholding for the period. Form K-1E is the electronic-filing variant filed via the Kentucky Online Gateway (KOG) / WRAPS (Withholding Return and Payment System). Semi-monthly and monthly remitters still file a quarterly Form K-1 return that reconciles the period's remittances against the wages paid.  _(Section 4.1)_

### 4.2 Due dates

- **Quarterly return due dates** — Quarterly returns are due by the last day of the month following the close of the calendar quarter (April 30, July 31, October 31, January 31).  _(Section 4.2)_
- **Monthly remittance due date** — Monthly remittances are due by the 15th of the following month.  _(Section 4.2)_
- **Semi-monthly remittance due date** — Semi-monthly remittances are due by the 3rd banking day after the close of the semi-monthly period (1st-15th and 16th-end).  _(Section 4.2)_
- **Annual return due date** — Annual returns are due January 31 of the following year.  _(Section 4.2)_

### 4.3 Payment method

- **Mandatory EFT threshold** — For employers with average monthly withholding of $1,000 or more, electronic payment via EFT is mandatory.  _(KRS 131.155)_
- **WRAPS portal and paper checks** — The Kentucky Department of Revenue uses the WRAPS portal for both return filing and remittance. Paper check payments are accepted for under-$1,000-per-month employers but are increasingly being phased out in favor of mandatory electronic filing as of the Department's 2024 guidance updates.  _(Section 4.3)_

### 4.4 Penalties

- **Late filing penalty** — 2% of the tax due per month or fraction thereof, capped at 20%, with a minimum penalty of $10 per return.  _(KRS 131.180(2))_
- **Late payment penalty** — 2% per month, also capped at 20%, with a $10 minimum.  _(KRS 131.180(2))_
- **Stacking of penalties** — The two penalties stack — late filing AND late payment results in up to 40% combined penalty.  _(KRS 131.180(2))_
- **2025 interest rate on deficiencies** — 8% annual for 2025, set annually by the Commissioner  _(KRS 131.183)_

## 5. Form K-3 — Annual Reconciliation

- **K-3 filing deadline and purpose** — Form K-3 is the Kentucky employer annual reconciliation of income tax withheld. It is filed by January 31 of the year following the tax year, together with copies of Forms W-2 (or W-2C) for every Kentucky-source employee.  _(Section 5)_
- **Mechanics — W-2 Box 16 reconciliation** — Total Kentucky wages from all W-2 Box 16 amounts must reconcile to total Kentucky wages reported on the four quarterly Form K-1s.  _(Section 5)_
- **Mechanics — W-2 Box 17 reconciliation** — Total Kentucky income tax withheld from all W-2 Box 17 amounts must reconcile to total Kentucky withholding paid in across the year.  _(Section 5)_
- **W-2 electronic filing threshold** — electronic filing is required for employers with 26 or more W-2s, via the WRAPS portal or the KOG bulk-upload interface. Below 26, paper filing is permitted but discouraged.  _(Section 5)_
- **Reconciling differences** — A reconciling difference must be either corrected on Form K-1X (amended quarterly return) for the affected quarter, or shown on Form K-3 with a brief explanation. Persistent imbalances often trigger a desk audit.  _(Section 5)_

AUDIT FLASH POINT — K-3 RECONCILIATION. The most common Form K-3 audit issue is a mismatch caused by mid-year payroll provider changes where the predecessor and successor providers each filed K-1 returns for portions of the year but neither was assigned the year-end K-3 responsibility. The employer remains responsible. The reviewer should confirm that a single K-3 covers all Kentucky wages paid in the calendar year regardless of how many payroll service providers were used.

## 6. Kentucky State Unemployment Insurance (SUI)

Kentucky SUI is administered by the Kentucky Office of Unemployment Insurance within the Education and Labor Cabinet.

### 6.1 Wage base and rate

- **2025 taxable wage base** — $11,400 per employee per calendar year (set annually; the 2024 wage base was $11,400 and the 2025 base remained $11,400 because the trust fund triggers for an automatic increase were not satisfied for calendar 2025)  _(KRS 341.030; KRS 341.270)_
- **2025 employer contribution rate range** — 0.225% to 9.0% (Schedule A — most favorable schedule, applicable for 2025 because the trust fund balance ratio was above the Schedule A floor on the September 30, 2024 measurement date)  _(KRS 341.270)_
- **2025 new-employer rate** — 2.7% for non-construction; the construction-industry new-employer rate is the maximum schedule rate (9.0% in 2025)  _(KRS 341.270(4))_
- **2025 service capacity surcharge** — 0.075% (statutory administrative assessment)  _(KRS 341.243)_

### 6.2 Rate determination

- **UI-3 determination process** — Each year by January 1, the Office of Unemployment Insurance issues Form UI-3 (Determination of Contribution Rate). The rate is computed as the employer's reserve ratio multiplied by the applicable Schedule A factor table. Employers in the third year of liability or later receive an experience rating; before that, the new-employer rate applies.  _(Section 6.2)_

### 6.3 Filing and payment

- **UI-3 due date** — Quarterly Form UI-3 (employer's wage and tax report) is due by the last day of the month following the quarter end.  _(Section 6.3)_
- **Electronic filing mandate** — Filing is mandatory electronic via the Kentucky Employer Tax Account (KETA) system at uiconnect.ky.gov.  _(Section 6.3)_
- **SUI penalties and interest** — Penalties: $15 per worker not reported plus 10% of tax owed for late filing; interest at 1.5% per month on unpaid tax.  _(Section 6.3)_

### 6.4 Voluntary contributions

- **Voluntary contribution mechanics** — Kentucky permits a voluntary contribution to buy down the reserve ratio within 30 days of the rate-notice date. The reviewer should compute whether a voluntary contribution that moves the employer down one experience-rate row produces a positive ROI for the upcoming year — generally yes if the rate would drop more than 0.3 percentage points on a $1M+ wage base.  _(KRS 341.270(7))_

## 7. Kentucky Local Occupational License Tax — The "Act 32-ish but Different" System

This is the most error-prone area of Kentucky payroll. Approximately 200 Kentucky cities, counties, urban-county governments, and school districts impose a 'license fee' or 'occupational license tax' on wages earned within their boundaries, authorized by KRS 67.083 (counties), KRS 91A.080 (cities), and KRS 160.605 (school districts).

### 7.1 Work-location, not residence

- **Work-location basis distinguished from PA Act 32** — Unlike Pennsylvania Act 32 — which requires comparing the work-location resident rate against the work-location non-resident rate and remitting at the higher — Kentucky's local occupational tax is purely work-location based. The employee's residence is irrelevant for withholding purposes (residence may matter for crediting purposes when the resident locality offers a credit for tax paid to another locality, but that is an employee-level reconciliation issue, not a withholding issue).  _(Section 7.1)_
- **Lexington-to-Louisville commuter example** — A Lexington resident who commutes daily to a Louisville office has Louisville Metro occupational tax withheld, not Lexington tax. The Lexington-Fayette LFUCG does not 'claw back' the tax via withholding — if Lexington offers a resident credit for occupational taxes paid to other Kentucky jurisdictions, the employee claims it on the Lexington individual return (Form 220-221), not through payroll.  _(Section 7.1)_
- **Distinction from PA Act 32** — PA Act 32 requires the employer to know both the work-location PSD code and the resident PSD code and to withhold at the higher of the two rates. Kentucky requires only the work-location. This is simpler in concept but is often missed by payroll providers that assume cross-state symmetry.  _(Section 7.1)_

### 7.2 Major localities and 2025 rates

**Major localities and 2025 rates**  _(Form OL-3; Form 220-221-A/Q)_

| Locality | Type | 2025 Rate | Cap (wage base ceiling) | Return |
| --- | --- | --- | --- | --- |
| Louisville Metro / Jefferson County | Consolidated metro | 1.45% (occupational) + 0.75% (school board) on resident; 1.45% on non-resident | No cap on occupational; school portion subject to Jefferson County Public Schools wage cap | Form OL-3 (Metro Revenue Commission) |
| Lexington-Fayette Urban County Government | Urban-county | 2.25% | First $148,000 of wages per employee per year (2025 cap) | Form 220-221-A (Annual), 220-221-Q (Quarterly) |
| Covington | City | 2.45% | $160,200 (Social Security wage base alignment) | Form OL-3 |
| Newport | City | 2.45% | No cap | Form OL-3 |
| Florence | City | 2.00% | $160,200 | Form OL-3 |
| Bowling Green | City | 1.85% | No cap | Form OL-3 |
| Owensboro | City | 1.78% | No cap | Form OL-3 |
| Boone County | County | 0.80% | $80,100 (2025) | Form OL-3 |
| Kenton County | County | 0.7097% | Tiered cap | Form OL-3 |
| Campbell County | County | 1.05% | No cap | Form OL-3 |
| Daviess County | County | 0.35% | No cap | Form OL-3 |

- **Rate verification caveat** — Rates and caps shown above are 2025 published rates. Locality rate ordinances change frequently; verify the rate against the locality's current published ordinance before the first payroll of each year.  _(Section 7.2)_

### 7.3 Form OL-3

- **Form OL-3 functions** — Form OL-3 is the consolidated occupational license fee return used by Louisville Metro Revenue Commission and adopted by most other Kentucky localities (with minor revisions to form numbering). It has two functions: 1. Employer withholding — Form OL-3E (employer withholding) is filed quarterly. The employer reports total wages paid to employees working within the locality, total tax withheld, and remits accordingly. 2. Business net profits — Form OL-3 (annual business return) is filed by businesses with gross receipts or net profits earned within the locality. This is a business-entity tax, not a payroll tax, but the same form is used.  _(Section 7.3)_
- **OL-3 due dates** — Quarterly OL-3E due dates: April 30, July 31, October 31, January 31. Annual OL-3 reconciliation: April 15 (or 105 days after fiscal year end).  _(Section 7.3)_

### 7.4 Northern Kentucky overlap — the multi-locality stack

- **Covington/Kenton stacking example** — Northern Kentucky (Boone, Kenton, Campbell counties and the cities of Covington, Newport, Florence, Erlanger, etc.) presents the most complex stacking. An employee working at a Covington office pays: Covington city occupational tax (2.45%); Kenton County occupational tax (0.7097%) — if the city-county overlap rules permit. Kenton County exempts wages already taxed by an incorporated city within the county from county tax under the Kenton ordinance.  _(Section 7.4)_
- **Default stacking presumption** — The rule: read each locality's ordinance for its overlap treatment. The default presumption is stacking (city + county) unless the county ordinance expressly carves out city-taxed wages. Kenton, Campbell, and Boone counties each have different overlap rules. Always confirm against the ordinance.  _(Section 7.4)_

AUDIT FLASH POINT — MULTI-LOCALITY STACKING. Failure to apply correct overlap treatment in Northern Kentucky is the #1 local-occupational audit finding. The county may issue a deficiency for un-withheld county tax even where the employer assumed the city tax superseded. Document the overlap rule applied per locality, citing the ordinance section.

### 7.5 School district occupational tax

- **School district occupational tax range** — ranging from 0.5% to 0.75% on wages earned within district boundaries  _(KRS 160.605)_
- **Jefferson County Public Schools rate** — 0.75% — collected as part of the Louisville Metro consolidated return  _(KRS 160.605)_
- **Fayette County Public Schools rate** — 0.50% — collected separately from the Lexington-Fayette urban-county return  _(KRS 160.605)_
- **Boone County Schools rate** — 0.50% — collected separately  _(KRS 160.605)_
- **Stacking of school district tax** — The school district tax stacks on top of the city and county taxes. It is not reciprocal with the city/county taxes. An employee working in Louisville pays 1.45% Metro + 0.75% JCPS = 2.20% combined. An employee in Lexington pays 2.25% LFUCG + 0.50% FCPS = 2.75% combined.  _(Section 7.5)_

AUDIT FLASH POINT — SCHOOL DISTRICT STACKING FORGOTTEN. Payroll providers that handle 'Kentucky local' tax often configure only the city/county rate and omit the school district stack. The employer is liable for the un-withheld school district tax plus penalties. The reviewer should explicitly verify school district tax setup for every employee work location in Jefferson County, Fayette County, Boone County, Kenton County, and any other county where the school district has imposed the tax. Maintain a school-district-tax map by ZIP-of-work and cross-reference annually.

### 7.6 Working from home — telecommuter rule

- **Telecommuter relief expiration and current rule** — Pandemic-era telecommuter relief expired June 30, 2021. From July 1, 2021 onward, the work location for occupational tax purposes is the location where the employee physically performs the work. An employee who lives in Indianapolis but works remotely for a Louisville-based employer has no Louisville Metro occupational tax exposure for the remote-work days, because the work is not physically performed in Louisville.  _(Section 7.6)_
- **New locality obligation from telecommuting** — This rule cuts both ways: a Kentucky-employed worker who has chosen to telecommute from a county or city that imposes occupational tax now creates a new withholding obligation in that locality. The employer must register, withhold, and remit even if the employer has no physical presence in the locality. This is the Kentucky parallel to the 'convenience of the employer' debates in NY/CT/MA — Kentucky resolves it by following physical performance, not convenience.  _(Section 7.6)_

## 8. Reciprocal Income Tax Agreements

Kentucky has reciprocal personal income tax agreements with six states:
- Ohio — KY-OH reciprocity (1972 agreement, codified at KRS 141.070 and Ohio Rev. Code §5747.05(A)(2))
- Indiana — KY-IN reciprocity
- Illinois — KY-IL reciprocity
- Michigan — KY-MI reciprocity
- Virginia — KY-VA reciprocity (limited; see below)
- West Virginia — KY-WV reciprocity

### 8.1 Operational mechanics

- **Reciprocal state resident working in Kentucky** — A resident of a reciprocal state who works in Kentucky: 1. Files Form 42A809 (Certificate of Non-Residence and Reciprocity Affidavit) with the Kentucky employer. 2. Kentucky employer withholds the home state's income tax instead of Kentucky PIT — but only if the employer is registered as a withholding agent in the home state. If not registered, the employer must register or the employee must make estimated payments at home. 3. The non-resident files an income tax return only in their home state for the wages.  _(Form 42A809)_
- **Kentucky resident working in a reciprocal state** — A Kentucky resident who works in a reciprocal state: 1. Files the equivalent reciprocity affidavit with the out-of-state employer (e.g., Ohio's IT-4NR for a KY resident working in OH). 2. The Ohio employer withholds Kentucky PIT instead of Ohio PIT. 3. The Kentucky resident files only the Kentucky return (Form 740) for the wages.  _(Section 8.1)_

### 8.2 Reciprocity does NOT cover local occupational taxes

- **Reciprocity scope limitation** — This is the most important nuance. The reciprocal agreements cover only the state-level personal income tax. Local occupational taxes are NOT reciprocal.  _(Section 8.2)_
- **Cincinnati resident working in Louisville example** — A Cincinnati, Ohio resident working in Louisville pays no Kentucky PIT (reciprocity), but DOES pay Louisville Metro occupational tax of 1.45% plus JCPS 0.75% on the Louisville wages.  _(Section 8.2)_
- **Louisville resident working in Cincinnati example** — A Louisville resident working in Cincinnati pays no Ohio PIT (reciprocity), but DOES pay Cincinnati city tax of 1.8% (Cincinnati municipal income tax) on the Cincinnati wages. The Louisville Metro tax does not apply to Cincinnati-source wages because Metro tax is work-location based.  _(Section 8.2)_

AUDIT FLASH POINT — RECIPROCAL-STATE LOCAL WITHHOLDING. Reciprocity confuses employers and payroll providers into thinking all Kentucky tax falls away for the reciprocal-state employee. It does not. The employer must continue withholding Louisville Metro / Lexington-Fayette / etc. for the cross-border commuter. Document the reciprocity treatment per employee with the state PIT exempted but the local tax preserved.

### 8.3 Virginia limitation

- **KY-VA reciprocity narrower scope** — The KY-VA reciprocity is narrower than the others — it applies only to 'wage and salary' income, and only where the Virginia resident has no Kentucky-source income other than wages. A Virginia resident with a Kentucky rental property or Kentucky-source business income loses reciprocity entirely. The employer should confirm the employee has signed Form 42A809 with the Virginia-only exception acknowledged.  _(Section 8.3)_

### 8.4 Local credit mechanics

- **Local resident credit for occupational tax paid elsewhere** — Some Kentucky local jurisdictions offer a credit to their own residents for occupational tax paid to another locality (Kentucky or out-of-state). Louisville Metro, for example, offers a partial credit under the Louisville Metro Code to residents who pay occupational tax to another Kentucky city or county. The credit is claimed on the resident's individual occupational return (where the locality requires individual filing) — not by adjustment of withholding. Lexington-Fayette has a similar provision for its residents.  _(Louisville Metro Code of Ordinances Ch. 110)_
- **Employee vs employer responsibility** — This is an employee compliance issue rather than an employer payroll obligation. The employer simply withholds at the work-location rate; the employee claims the credit in their home locality's return.  _(Section 8.4)_

## 9. Worker Classification

Kentucky generally adopts the IRS common-law test (behavioral control, financial control, type of relationship) for employee vs. independent contractor classification, with one important Kentucky-specific overlay.

### 9.1 Construction industry presumption

- **Construction industry presumptive employee status** — Under KRS 341.123 (added in 2010 amid the federal misclassification crackdown), workers in the construction industry in Kentucky are presumptively employees for purposes of: Kentucky unemployment insurance, Kentucky workers' compensation, Kentucky wage and hour law.  _(KRS 341.123)_
- **Construction industry definition** — The construction industry is broadly defined to include any person engaged in the construction, alteration, demolition, repair, or improvement of real property — including subcontractors, drywallers, electricians, plumbers, roofers, painters, and general laborers.  _(KRS 341.123)_
- **Rebuttal test (a)(b)(c)** — To rebut the presumption, the hiring party must establish that the worker: (a) is free from direction and control over the work performed, both under the contract and in fact; (b) operates an independently established trade, occupation, profession, or business; AND (c) has filed all required federal and state tax returns (including Form 1099-NEC) for the prior two years as a self-employed person.  _(KRS 341.123)_
- **Practical gatekeeper prong (c)** — The (c) prong is the practical gatekeeper. A general contractor cannot treat a drywall subcontractor as a 1099 contractor unless the subcontractor has been filing Schedule C returns for the prior two years. New construction workers default to employee classification.  _(Section 9.1)_

### 9.2 Non-construction industries

- **Standard IRS test applies; no KY safe harbor** — For non-construction work, the standard IRS three-factor test applies. There is no Kentucky safe harbor analogous to California's ABC test or Massachusetts' three-prong test. The Department of Revenue accepts a federal Form SS-8 determination as persuasive but not binding.  _(Section 9.2)_

## 10. Final Pay

- **Final wage payment timing** — Under KRS 337.055, when an employee is terminated (voluntarily or involuntarily), final wages — including accrued vacation if the employer has a policy of paying out accrued vacation — must be paid: By the next regular payday, OR Within 14 days of the date of termination, whichever is later.  _(KRS 337.055)_
- **Liquidated damages for untimely final pay** — Failure to pay final wages timely exposes the employer to liquidated damages equal to the wages owed, plus attorney fees and costs.  _(KRS 337.385)_
- **Final pay withholding and reporting** — Final pay must include any earned occupational license tax withholding and Kentucky PIT withholding, and the final pay is reported on the next quarterly Form K-1 and OL-3E.  _(Section 10)_

## 11. Worked Examples

### Example A — Louisville employer with multi-resident workforce

Acme Manufacturing LLC operates a plant at 2200 Industrial Parkway, Louisville, KY 40213 (Jefferson County, City of Louisville, Jefferson County Public Schools district). Acme has three full-time employees on a $1,500/week gross wage: Sarah, lives in Shelbyville, KY (Shelby County) — commutes to Louisville. Mike, lives in Jeffersonville, IN — commutes from Indiana to Louisville. Tony, lives in New Albany, IN, but telecommutes from home four days per week, on-site at Louisville one day per week.

**Withholding for Sarah (KY resident commuter)**

| Tax | Rate | Wages | Per pay |
| --- | --- | --- | --- |
| Kentucky PIT | 4.0% (annualized w/ $3,270 std ded) | $1,500 | ~$57.49 |
| Louisville Metro occupational | 1.45% | $1,500 | $21.75 |
| Jefferson County Public Schools | 0.75% | $1,500 | $11.25 |
| **Total KY/local** |  |  | **$90.49** |

Shelby County does not impose an occupational tax. Sarah's residence is irrelevant for Louisville/JCPS withholding (work-location rule). Sarah will file her Kentucky Form 740 and claim all Kentucky PIT withheld.

- **Mike reciprocity treatment** — Mike files Form 42A809 with Acme claiming Indiana residency under the KY-IN reciprocal agreement. Acme withholds Indiana state income tax (currently 3.0% for 2025) and the applicable Indiana county adjusted gross income tax for Mike's Indiana county of residence (Clark County, IN — 2.0% for 2025), instead of Kentucky PIT.  _(Form 42A809; KY-IN reciprocal agreement)_

**Withholding for Mike (IN resident commuter, full-time in Louisville)**

| Tax | Rate | Wages | Per pay |
| --- | --- | --- | --- |
| Indiana state PIT | 3.0% | $1,500 | $45.00 |
| Indiana Clark County tax | 2.0% | $1,500 | $30.00 |
| Louisville Metro occupational | 1.45% | $1,500 | $21.75 |
| Jefferson County Public Schools | 0.75% | $1,500 | $11.25 |
| **Total cross-border + local** |  |  | **$108.00** |

The reciprocity exempts the state PIT, but the local occupational and school district taxes are not subject to reciprocity. Acme must be registered as an Indiana withholding agent or assist Mike in registering for individual estimated payments.

Withholding for Tony (IN resident, 1 day onsite, 4 days remote from IN): This is the most error-prone case. Of Tony's $1,500 weekly wage: $300 (1/5) is for work physically performed in Louisville. $1,200 (4/5) is for work physically performed in New Albany, Indiana.

- **Tony's Indiana state PIT treatment** — For Indiana state PIT: All $1,500 is Indiana resident wages — Acme withholds Indiana state and county tax on the full $1,500 (Mike's situation, scaled).
- **Tony's Kentucky PIT treatment** — For Kentucky PIT: Reciprocity covers what would otherwise be Kentucky PIT on the $300 Louisville-source portion; with Form 42A809 on file, no Kentucky PIT is withheld at all.
- **Tony's Louisville Metro/JCPS calculation** — For Louisville Metro and JCPS: Only the $300 work-performed-in-Louisville portion is subject. Per pay = $300 × (1.45% + 0.75%) = $6.60.
- **Floyd County Indiana local tax** — Indiana does not have a Floyd County (New Albany) local tax equivalent that applies to the remote-work day in lieu of Louisville Metro — but Floyd County, IN, does have its own county income tax (1.5% for 2025) that applies because Tony is a Floyd County resident. The 1.5% Floyd County rate is built into the Indiana county tax withholding.

The reviewer must confirm Indiana state and county registration is in place for the full $1,500 and that Louisville/JCPS are correctly withheld on only the $300 on-site portion. The employer cannot withhold Louisville Metro on the full $1,500 — that would over-withhold the four telecommute days and create a refund claim on Tony's individual Louisville Metro return.

### Example B — Kentucky resident commuting to Ohio (KY-OH reciprocity)

Beth lives in Covington, KY (Kenton County), and commutes daily to a Cincinnati, OH employer. Beth's gross weekly wage is $2,000. Beth has filed Form IT-4NR (Ohio's reciprocity affidavit) with her Cincinnati employer.

**Cincinnati employer's withholding for Beth**

| Tax | Rate | Wages | Per pay |
| --- | --- | --- | --- |
| Ohio state PIT | EXEMPT under reciprocity | $2,000 | $0 |
| Kentucky PIT | 4.0% (annualized w/ $3,270 std ded) | $2,000 | ~$77.49 |
| Cincinnati municipal income tax | 1.8% | $2,000 | $36.00 |

- **Critical points for Beth's withholding** — Ohio reciprocity zeroes the Ohio state PIT only. Cincinnati municipal tax is NOT covered by the state reciprocity agreement and is fully withheld. The Cincinnati employer withholds Kentucky PIT (not Ohio) because the employer is presumably registered with the Kentucky Department of Revenue as a withholding agent. If not, Beth must register for Kentucky estimated payments via Form 740-ES. Covington, KY (where Beth lives) imposes a 2.45% occupational tax — BUT only on wages earned for work performed in Covington. Beth's work is in Cincinnati, not Covington, so no Covington tax applies. Kenton County does not impose an occupational tax on wages earned outside Kenton County. Beth's only Kentucky income tax filing obligations are the Kentucky Form 740 (full credit for the $77.49/week withheld) and any potential Covington individual return showing a zero work-in-Covington tax base.

AUDIT FLASH POINT — RECIPROCAL-STATE FILINGS. If Beth's Cincinnati employer fails to register as a Kentucky withholding agent and continues to withhold Ohio state PIT despite the IT-4NR on file, Beth faces a double-tax situation that is resolved only by: (1) Filing an Ohio non-resident return (Form IT-1040 with IT-NRC) claiming a refund of all withheld Ohio tax; AND (2) Filing a Kentucky Form 740 reporting the full wages and paying the Kentucky PIT due (no credit for Ohio tax paid because the OH tax should have been zero in the first place). This is operationally messy and creates ~$4,000+ cash-flow issues for the employee until the Ohio refund processes. The reviewer should always confirm with the cross-border employer that they are properly registered in the employee's home state before assuming clean reciprocity.

### Example C — School district stacking with Lexington employer

Carla works at a Lexington, KY office at 250 W Main St, Lexington, KY 40507 (Fayette County, Lexington-Fayette Urban County Government, Fayette County Public Schools district). Carla earns a $200,000 annual salary, paid bi-weekly at $7,692.31 per pay period. Carla is a Kentucky resident (Lexington).

**Per-pay-period withholding (regular pay periods, first half of year before LFUCG cap is reached)**

| Tax | Rate | Wages | Per pay |
| --- | --- | --- | --- |
| Kentucky PIT | 4.0% (annualized w/ $3,270 std ded) | $7,692.31 | ~$302.65 |
| LFUCG occupational | 2.25% | $7,692.31 | $173.08 |
| Fayette County Public Schools | 0.50% | $7,692.31 | $38.46 |
| **Total KY/local** |  |  | **$514.19** |

- **LFUCG wage cap mechanics** — Lexington-Fayette caps the 2.25% occupational tax at the first $148,000 of wages per employee per year (2025 cap, set annually by LFUCG ordinance, indexed to Social Security wage base movements but historically lagged by 1 year). Carla will hit the $148,000 LFUCG cap in pay period 20 (week 40, late September). After that, no further LFUCG occupational tax is withheld for the remainder of 2025.
- **FCPS and KY PIT cap treatment** — The Fayette County Public Schools 0.50% has no annual wage cap — it continues to apply on all wages through year-end. The 4.0% Kentucky PIT has no wage cap (uncapped, like the federal Medicare tax).

Kentucky PIT: $200,000 × 4.0%, less the standard-deduction benefit annualized: roughly $7,869.20. LFUCG occupational: $148,000 × 2.25% = $3,330.00 (cap reached around pay 20; no further withholding). FCPS school district: $200,000 × 0.50% = $1,000.00.

AUDIT FLASH POINT — LFUCG CAP TRACKING. Payroll software must be configured to track the LFUCG occupational cap on a per-employee, per-year basis. Failure to stop withholding at $148,000 results in over-withholding that the employee must reclaim on the LFUCG individual return (Form 220-221) — slow and irritating. The reviewer should validate the cap setting at year-start and at any mid-year compensation adjustment that crosses the cap threshold.

AUDIT FLASH POINT — SCHOOL DISTRICT NOT CAPPED. Conversely, payroll software that also caps FCPS at $148,000 (mistakenly treating it as part of the LFUCG cap) under-withholds the school district tax. The school district has no cap and is a separately administered tax with its own remittance schedule. Verify the FCPS configuration is independent of the LFUCG configuration.

## 12. Reviewer Self-Checks

Before signing off on a Kentucky payroll period or year-end deliverable, the reviewer should confirm:
1. KY PIT rate applied is 4.0% for 2025 pay dates; switch to 3.5% for any pay date on or after January 1, 2026 (constructive-receipt rule).
2. K-4 on file for every Kentucky-source employee; Form 42A809 on file for every reciprocal-state non-resident.
3. Form K-1 filing frequency matches the average-monthly-liability bracket; rolling re-determination performed annually.
4. Form K-3 annual reconciliation reconciles to the sum of Forms K-1 and to the sum of W-2 Box 16/17.
5. KY SUI rate applied matches the UI-3 rate notice; new-employer 2.7% used only if within first three years of liability; voluntary contribution opportunity evaluated.
6. Local occupational tax configured for every work location based on physical performance, not residence.
7. School district tax stack confirmed for Jefferson County (JCPS 0.75%), Fayette County (FCPS 0.50%), Boone County, Kenton County, and any other district imposing the tax for the work location.
8. LFUCG / Covington / Florence / other locality wage caps configured per-employee per-year.
9. Multi-locality overlap (Northern Kentucky stack) confirmed against current ordinance language.
10. Telecommuter work-location apportionment performed for any remote/hybrid employee whose work is not physically performed at the registered office address.
11. Reciprocal-state non-resident employees withheld at the home state's rate (with state registration confirmed) but still subject to Kentucky local occupational tax.
12. Construction-industry presumption rebuttal documented for any 1099 contractor in construction.
13. Final pay calculations include all Kentucky and local withholding; final pay date within KRS 337.055 window.

## 13. Refusals

- **R-KY-1** — The employer is not registered with the Kentucky Department of Revenue for withholding (no KY Withholding Account Number on file). Withholding cannot be remitted without registration; advise the employer to register via WRAPS first.  _(Section 13)_
- **R-KY-2** — The employer is not registered with the Kentucky Office of Unemployment Insurance (no UI Account Number on file). SUI cannot be reported without registration.  _(Section 13)_
- **R-KY-3** — An employee's work location is in a Kentucky locality where the employer is not registered for occupational tax withholding. Direct the employer to register with the locality (Louisville Metro Revenue Commission, LFUCG Division of Revenue, etc.) before processing the next pay period.  _(Section 13)_
- **R-KY-4** — An employee claims reciprocal-state exemption but Form 42A809 is not on file. Require the form before honoring the exemption.  _(Section 13)_
- **R-KY-5** — A construction-industry worker is being treated as a 1099 contractor without two years of prior Schedule C filings on record. Default to employee classification and escalate.  _(Section 13)_
- **R-KY-6** — Multi-state apportionment is required for an employee working in more than one state in the same pay period beyond a simple reciprocal-state commute pattern. Defer to the multistate-payroll-allocation skill.  _(Section 13)_
- **R-KY-7** — The employer is operating in a Kentucky locality whose 2025 occupational tax ordinance has not been confirmed against the current published rate. Confirm the rate against the locality's website before processing.  _(Section 13)_
- **R-KY-8** — Pandemic-era telecommuter relief is being claimed for a work period after June 30, 2021. The relief has expired; refuse.  _(Section 13)_
- **R-KY-9** — A Virginia resident with non-wage Kentucky-source income is claiming KY-VA reciprocity. The reciprocity is wage-only; escalate.  _(Section 13)_
- **R-KY-10** — Year-crossover pay dates where the 4.0% vs 3.5% rate question is unclear. Apply the rate in effect on the payment date and document.  _(Section 13)_

## 14. Citation Reference

Primary statutory and regulatory citations used in this skill:
- KRS 141.020 — Kentucky income tax rates; flat-rate phase-down triggers.
- KRS 141.070 — Reciprocity authority.
- KRS 141.081 — Kentucky standard deduction.
- KRS 141.310 — Withholding from wages; constructive receipt rule.
- KRS 131.155 — EFT requirement for tax remittances.
- KRS 131.180 — Penalty provisions.
- KRS 131.183 — Interest rate on tax deficiencies.
- KRS 67.083 — County occupational license tax authorization.
- KRS 91A.080 — City occupational license fee authorization.
- KRS 160.605 — School district occupational license tax authorization.
- KRS 337.055 — Final pay timing.
- KRS 337.385 — Liquidated damages for unpaid wages.
- KRS 341.030 — SUI taxable wage base.
- KRS 341.123 — Construction industry employee presumption.
- KRS 341.243 — Service capacity surcharge.
- KRS 341.270 — SUI experience rating; rate schedules; voluntary contributions.
- KRS 425.501 — Wage garnishments (out of scope, listed for completeness).
- 103 KAR 18:070 — Kentucky withholding tables regulation.
- 103 KAR 18:150 — Filing frequency thresholds.
- HB 8 (2022) — Original flat-tax legislation.
- HB 1 (2025) — 2026 rate set at 3.5%.
- Ohio Rev. Code §5747.05(A)(2) — Ohio side of KY-OH reciprocity.
- Louisville Metro Code of Ordinances Ch. 110 — Louisville Metro occupational license fee.
- LFUCG Code of Ordinances Ch. 13 — Lexington-Fayette occupational license tax.

Form references:
- K-1 / K-1E (employer quarterly withholding return)
- K-3 (annual reconciliation)
- K-4 (employee withholding allowance certificate)
- 42A809 (certificate of non-residence)
- UI-3 (employer quarterly wage and tax report)
- OL-3 / OL-3E (occupational license return — employer withholding variant)
- 220-221-Q / 220-221-A (Lexington-Fayette quarterly / annual)
- IT-4NR (Ohio reciprocity affidavit)

## 15. Version Log

v0.1 (2025-11-15): Initial draft covering 2025 rates, K-1/K-3, SUI, occupational license tax system, school district stacking, reciprocity. Pending reviewer verification.

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
