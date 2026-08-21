---
name: mi-payroll
description: Tier 2 Michigan content skill for employer payroll compliance covering tax year 2025. Includes the 4.25% flat PIT, MI 165 quarterly withholding, MI SUTA wage base $9,500 with rates 0.06-10.30%, the 24 Michigan cities imposing local income tax (Detroit 2.4% resident/1.2% non-resident, Grand Rapids 1.5%/0.75%, plus Lansing/Saginaw/Highland Park/Hamtramck/Battle Creek/Flint/etc.), Detroit Form D-1040 employer withholding, and the Paid Medical Leave Act covering employers with 50+ employees.
jurisdiction: US-MI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MI Payroll

## Michigan Payroll — Tier 2 Content Skill (Tax Year 2025)

## 1. Scope and prerequisites

### 1.1 What this skill covers

This skill handles **employer payroll compliance in the State of Michigan** for the 2025 tax year, including:

- Michigan Personal Income Tax (PIT) withholding at the statewide 4.25% flat rate
- Form MI-W4 (Employee's Michigan Withholding Exemption Certificate)
- Quarterly and accelerated withholding remittance (Forms 5080/5081, formerly MI-165/MI-501 series)
- Michigan Unemployment Insurance (SUTA/UIA) under the Michigan Employment Security Act (MCL 421.1 et seq.)
- Form UIA 1028 quarterly contribution and wage reports
- The 24 Michigan cities imposing local income tax under the Uniform City Income Tax Ordinance (MCL 141.501 et seq.) — Detroit and Grand Rapids in depth, the rest as a routed-out summary
- Employer city-tax withholding for Detroit (Form 5321/DW-3 family) and Grand Rapids (Form GR-W3)
- The Paid Medical Leave Act, MCL 408.961 et seq. (50+ employees)
- Worker classification under Michigan's economic reality test and the ABC test where it applies
- W-2 and 1099 filing with the Department of Treasury, including the Form 5081 annual reconciliation

### 1.2 What this skill does NOT cover

- **Federal payroll** (Forms 941, 940, W-2 federal, FUTA, FICA) — defer to `us-federal-payroll`
- **Multi-state apportionment of withholding for telecommuting employees** outside Michigan — defer to `us-multistate-payroll`
- **Workers' compensation** under the Michigan Workers' Disability Compensation Act — separate workflow
- **Michigan Earned Sick Time Act (ESTA)** — see Section 8.4; ESTA replaced the Paid Medical Leave Act effective 21 February 2025 but a subsequent legislative compromise (HB 4001/HB 4002, signed 21 February 2025) materially amended it. Read Section 8 carefully — this is the most volatile area of Michigan payroll law in 2025
- **Detroit business taxes** other than employer withholding (corporate income tax, utility users tax)
- **School district income taxes** — Michigan does not impose these (unlike Ohio); do not confuse with city taxes
- **Public Act 4 of 2023 retirement income exemption** at the individual level — that's a personal return item, not a payroll item, though it does interact with pension withholding which is in scope for retirees only

### 1.3 Required upstream skills

This skill MUST be loaded alongside:
- `us-tax-workflow-base` v0.2 or later (workflow architecture)
- `us-federal-payroll` (federal payroll provides the wage base from which Michigan withholding is computed)

### 1.4 Conservative defaults

- **Default to withholding** — Default to withholding rather than not withholding (under-withholding triggers MCL 205.27a interest and penalty; over-withholding is refunded on the employee's MI-1040)  _(MCL 205.27a)_
- **Default to city residency at higher resident rate** — Default to city residency at the higher resident rate if the employer cannot evidence the employee's address with a current Form MI-W4 and a city-specific certificate (e.g., Detroit DW-4)
- **Default to employee classification** — Default to employee classification under the Michigan economic reality test unless a written contractor agreement, 1099 history, and at least 3 of the 20 IRS factors clearly point to contractor — this is a Michigan UIA audit hot spot
- **Default to PMLA/ESTA coverage** — Default to PMLA/ESTA coverage if the employee count straddles the threshold over the look-back period

## 2. Michigan PIT — the 4.25% flat rate

### 2.1 Statutory rate

- **Michigan PIT flat rate, tax year 2025** — 4.25% (0.0425)  _(MCL 206.51)_
- **History and trigger mechanism** — MCL 206.51(1)(c) contains a rate-reduction trigger tied to General Fund growth. The trigger activated in tax year 2023 reducing the rate to 4.05%. The Michigan Supreme Court in *Mothering Justice v. Attorney General* and the related Attorney General Opinion No. 7321 (March 2024) confirmed the reduction was a one-year reduction, not permanent. The rate reverted to 4.25% for tax year 2024 and remains 4.25% for tax year 2025. Employers who continued withholding at 4.05% in 2024 produced under-withheld W-2s and the employees owed balances on their MI-1040 returns. Verify your client's payroll software updated to 4.25% effective 1 January 2024 — this is a common reviewer finding for 2024 and 2025 returns.  _(MCL 206.51(1)(c); Mothering Justice v. Attorney General; AG Opinion No. 7321 (March 2024))_

The same trigger could activate again for a future year if General Fund revenue grows above the threshold, but the formula compares against a high 2021 baseline so reactivation is unlikely in the near term. Use 4.25% for any 2025 or 2026 projection unless the Treasury issues Revenue Administrative Bulletin (RAB) confirming otherwise.

### 2.2 Supplemental wages

- **Supplemental wage withholding** — Michigan does not publish a separate supplemental wage rate. Bonuses, commissions, severance, accumulated leave payouts, and other supplemental wages are withheld at the same 4.25% flat rate, applied to the gross supplemental amount. There is no 'aggregate vs. flat' election as exists federally — the math is just 4.25% × gross supplemental wages.

### 2.3 Personal exemption allowance

- **2025 Michigan personal exemption per allowance** — $5,800  _(MCL 206.30)_

**Per-pay-period exemption amount, 2025**

| Pay frequency | Annual exemption per allowance | Per-period |
| --- | --- | --- |
| Weekly (52) | $5,800 | $111.54 |
| Biweekly (26) | $5,800 | $223.08 |
| Semimonthly (24) | $5,800 | $241.67 |
| Monthly (12) | $5,800 | $483.33 |
| Quarterly (4) | $5,800 | $1,450.00 |
| Annual (1) | $5,800 | $5,800.00 |

Employees may claim exemptions for themselves, their spouse, and dependents, plus additional exemptions for age 65+, blindness, deafness, hemiplegia/paraplegia/quadriplegia, and totally and permanently disabled status (MI-W4 lines 6a–6e).

### 2.4 Withholding formula

- **Per-pay-period withholding calculation** — 1. Take gross taxable wages (federal-conformity definition with Michigan modifications; pre-tax 401(k) and §125 cafeteria are excluded, same as federal) 2. Subtract the per-period exemption: (allowances × $5,800) ÷ pay periods per year 3. Subtract any additional withholding amount the employee entered on MI-W4 line 8 (NOT subtracted — added to the calculated tax; see the form) 4. Multiply by 4.25% 5. Round to the nearest cent

There is no Michigan equivalent of the federal wage-bracket method's standard deduction inside withholding — the exemption mechanism handles it.

### 2.5 Compensation NOT subject to Michigan withholding

- **Wages paid to nonresident for services outside Michigan** — Not subject to Michigan withholding  _(MCL 206.703)_
- **Active-duty military pay of MI residents under PCS orders outside Michigan** — Not subject to Michigan withholding  _(Servicemembers Civil Relief Act; MCL 206.30(1)(g))_
- **Tribal-member income on tribal trust land** — Not subject to Michigan withholding for enrolled members of federally recognized Michigan tribes (compact-by-compact; check the specific tribal compact)
- **Renaissance Zone wages** — Exempt only for the resident portion where the employee resides and works in a designated zone — confirm zone status with the local treasurer  _(MCL 125.2689)_

### 2.6 Pension and retirement withholding

Michigan moved to substantial pension exemption under Public Act 4 of 2023. For payroll skill purposes, retiree pension withholding is handled on Form MI-W4P; the payer (not employer) withholds. This is out of scope for active-employee payroll but you may encounter it for a client running their own pension plan.

## 3. Form MI-W4 (Employee's Withholding Exemption Certificate)

### 3.1 When required

- **MI-W4 filing requirement** — Every employee MUST file MI-W4 with the employer on or before the first day of work. Federal Form W-4 does NOT substitute. The employer must keep MI-W4 on file and provide a copy to Treasury upon request.  _(MCL 206.351(3))_
- **Failure-to-file by employee** — If the employee does not file, the employer withholds as if zero exemptions were claimed and the employee is treated as a Michigan resident. This is the most punitive treatment — push clients to require MI-W4 with the I-9 at hire.
- **Updated certificates** — The employee should file a new MI-W4 within 10 days of any change reducing allowances (e.g., divorce, dependent leaving the household). Increases (new dependent, marriage) may be filed at any time and take effect the next pay period.

### 3.2 Key fields

- **MI-W4 Line 5** — Full home address; the city/township determines local withholding obligations under Section 7
- **MI-W4 Line 6** — Personal and dependency exemptions (max 1 self + 1 spouse + each dependent; do NOT double-claim with the other spouse if both work)
- **MI-W4 Line 7** — Claim of complete exemption from withholding; requires the employee to certify they had no Michigan tax liability last year AND expect none this year. Treat with skepticism; if claimed, watch for year-end W-2 reconciliation issues
- **MI-W4 Line 8** — Additional dollar amount per pay period to withhold over the formula amount
- **MI-W4 Section 2** — Residency in a Renaissance Zone (rare, but flag if checked)

### 3.3 Sending MI-W4 to Treasury

- **MI-W4 submission to Treasury requirement** — The employer must send a copy of MI-W4 to Treasury within 10 business days if the employee claims more than 10 exemptions OR claims exempt and is expected to earn more than $200 per week.  _(MCL 206.351(4))_

Send to:

Michigan Department of Treasury
Tax Technical Section
P.O. Box 30477
Lansing MI 48909

### 3.4 City withholding certificates — separate forms

- **City withholding certificates** — MI-W4 does NOT cover city tax. Each city-tax city issues its own employee certificate: - Detroit: Form DW-4 (City of Detroit Employee's Withholding Certificate) - Grand Rapids: Form GRW-4 - Other cities: each has its own; commonly modeled on Detroit DW-4 A nonresident commuter working in Detroit must complete DW-4 listing the percentage of time worked inside Detroit (the predominant place of employment / Detroit-day-count). The employer must keep this on file. Audit flash point — see Section 7.7.

## 4. Withholding remittance — Form 5080 (replaces MI-165/MI-501)

### 4.1 Form 5080 — the unified monthly/quarterly return

- **Form 5080 background** — Michigan retired the legacy MI-165 (quarterly) and MI-501 (monthly) forms in 2015 and consolidated them into Form 5080 — Sales, Use and Withholding Taxes Monthly/Quarterly Return. Despite the name change, payroll preparers still colloquially say 'MI-165' — be aware your client may use the old terminology. Form 5080 is filed electronically via Michigan Treasury Online (MTO) at mto.treasury.michigan.gov. Paper filing is allowed but strongly discouraged.

### 4.2 Filing frequency determination

**Filing frequency threshold ladder**

| Annual tax liability (W/H + sales + use combined) | Filing frequency | Form |
| --- | --- | --- |
| ≤ $750 | Annual (Form 5081 only) | 5081 |
| $751 – $3,600 | Quarterly | 5080 quarterly |
| $3,601 – $720,000 | Monthly | 5080 monthly |
| > $720,000 | Monthly with EFT-accelerated payments | 5080 + EFT |

- **Accelerated EFT threshold** — Accelerated EFT (the historical 'MI-501' trigger): an employer whose annual withholding alone exceeded $480,000 in the look-back year (so roughly $40k/month) must pay via EFT on the same accelerated schedule as federal semi-weekly depositors. The employer still files Form 5080 monthly to reconcile; the EFT payments hit on the 20th of each month and a true-up. For most freelancer/small-business clients, quarterly Form 5080 is the typical posture.

### 4.3 Due dates

**Form 5080/5081 due dates**

| Period | Form 5080 due date |
| --- | --- |
| January (monthly) | 20 February |
| Q1 (Jan-Mar) | 20 April |
| Q2 (Apr-Jun) | 20 July |
| Q3 (Jul-Sep) | 20 October |
| Q4 (Oct-Dec) | 20 January |
| Annual (Form 5081) | **28 February** of the year after the tax year (reconciliation of 5080s + W-2 transmittal) |

### 4.4 Form 5081 — the annual reconciliation

- **Form 5081 contents** — Form 5081 — Sales, Use and Withholding Taxes Annual Return consolidates the year: - Lines 1-12 reconcile withholding remitted across all 5080s - The form is filed with W-2 transmittal data (employee SSN, name, MI wages, MI tax withheld) - The W-2 / 1099 filings (Section 9) attach to 5081 Due 28 February 2026 for tax year 2025. There is no extension.

### 4.5 Late filing — interest and penalty

- **Penalty for late filing** — 5% of tax due for the first two months past due, plus an additional 5% per month up to a maximum of 25%  _(MCL 205.24)_
- **Interest on late payment** — Prime rate + 1% (Treasury publishes semi-annually; for 2025 it has been roughly 9.47% annualized depending on the period)  _(MCL 205.24)_

Aggregate late-payment exposure on a missed quarter can easily reach 30-35% of the unpaid tax within a year. Treat the 5080 due dates as hard.

### 4.6 Adjusting prior periods

- **Correcting prior-period errors** — A prior-period error is corrected by amending the relevant 5080 (file a new 5080 marked 'Amended Return') or, if the error is small and within the same tax year, by adjusting the next period's 5080 with an explanatory schedule. The annual 5081 is the failsafe — any year-end reconciliation discrepancy gets cleaned up there.

## 5. Michigan SUTA / UIA

### 5.1 Statutory framework

- **UIA administration** — Michigan's unemployment insurance program is administered by the Unemployment Insurance Agency (UIA) under the Michigan Employment Security Act. Employer contributions fund the Trust Fund from which benefits are paid.  _(MCL 421.1 et seq.)_

### 5.2 Wage base and rates for 2025

**2025 SUTA wage base and rates**

| Item | 2025 value |
| --- | --- |
| Taxable wage base per employee per year | **$9,500** |
| New-employer rate (most industries) | **2.7%** |
| New-employer rate, construction (NAICS 23) | **6.0%** (the industry-average construction rate; UIA recomputes annually) |
| Minimum experience-rated total rate | **0.06%** |
| Maximum experience-rated total rate | **10.30%** |

- **Total rate components** — The total rate is the sum of: - CBC — Chargeable Benefits Component (experience-based, 0%–6.3%) - AC — Account Building Component (0%–2.7%; helps build the employer's reserve) - NBC — Non-Chargeable Benefits Component (0%–1.0%; covers benefits not chargeable to a specific account) - Solvency tax — applies in years the Trust Fund is below the solvency threshold (currently NOT in effect for 2025; verify on Form UIA 1771) Form UIA 1771 (Tax Rate Determination) issued each December tells the employer its rate for the following calendar year.

### 5.3 Employer registration

- **UIA registration trigger events** — Register at Michigan Web Account Manager (MiWAM) at miwam.unemployment.state.mi.us. Trigger events: - Paying wages of $1,000 or more in any calendar quarter (general), OR - Acquiring all or part of an existing Michigan business that was an employer, OR - Being subject to FUTA (federal), OR - Employing agricultural labor — $20,000 in any quarter or 10+ employees on any day in 20 weeks, OR - Employing domestic labor — $1,000 in any quarter Upon registration the employer receives a UIA Account Number (7 digits) and a Treasury Withholding Account Number (separate; same legal entity, different agencies).

### 5.4 Reporting and payment — Form UIA 1028

**Form UIA 1028 quarterly due dates**

| Quarter | Due date |
| --- | --- |
| Q1 | 25 April |
| Q2 | 25 July |
| Q3 | 25 October |
| Q4 | 25 January |

- **1028 wage reporting and contribution calc** — Note the 25th-of-month-following-quarter-end due date — this is 5 days later than Form 5080's 20th-of-month. Easy to mix up. The 1028 reports each employee's gross wages for the quarter, capped at the $9,500 wage base cumulative for the year. The contribution = (wages up to the cap) × the assigned rate. Payment is due with the 1028.

### 5.5 Penalty and interest

- **Late filing of UIA 1028** — $25 per missing report
- **Late payment penalty/interest** — 1% per month interest plus a 10% penalty  _(MCL 421.15(a))_

Misclassification: see Section 9

### 5.6 SUTA dumping — MCL 421.22b

- **SUTA dumping prohibition and penalties** — Michigan adopted the federal SUTA Dumping Prevention Act in MCL 421.22b. Transferring payroll between commonly-controlled entities to obtain a lower experience rate triggers mandatory rate-transfer rules and civil penalties of up to $5,000 plus a maximum 10.30% rate for two years. If a client asks about 'moving employees to a new entity to reset the rate,' refuse and explain the statute.  _(MCL 421.22b)_

### 5.7 FUTA credit

- **FUTA credit reduction status** — Michigan is a fully-compliant state for FUTA purposes (no §3302 credit reduction in recent years). Employers paying Michigan SUTA timely get the full 5.4% FUTA credit, reducing effective FUTA to 0.6% on the first $7,000 of federal wages. Verify Treasury Department FUTA credit-reduction list each year.

## 6. City income taxes — overview of the 24 cities

### 6.1 The Uniform City Income Tax Ordinance (UCITO)

- **UCITO maximum rate caps** — Under MCL 141.501 et seq. (the Uniform City Income Tax Ordinance, 'UCITO'), a city may adopt a local income tax by ordinance, subject to voter approval. The statute fixes the maximum rates that any city may charge: - 1.0% resident / 0.5% nonresident for most cities - A higher cap of 2.0% / 1.0% for cities with population over 600,000 (functionally, only Detroit qualifies; Detroit is then further authorized by Public Act 56 of 2011 to go to 2.4% / 1.2%)  _(MCL 141.501 et seq.; Public Act 56 of 2011)_

### 6.2 The 24 cities with active income tax (as of 2025)

**24 Michigan cities with active income tax**

| # | City | Resident rate | Nonresident rate | Filing entity |
| --- | --- | --- | --- | --- |
| 1 | **Detroit** | **2.4%** | **1.2%** | City of Detroit (Income Tax Administration is run by Michigan Treasury since 2015) |
| 2 | **Grand Rapids** | **1.5%** | **0.75%** | City of Grand Rapids Income Tax Department |
| 3 | Saginaw | 1.5% | 0.75% | City of Saginaw |
| 4 | Highland Park | 2.0% | 1.0% | City of Highland Park |
| 5 | Lansing | 1.0% | 0.5% | City of Lansing |
| 6 | Flint | 1.0% | 0.5% | City of Flint |
| 7 | Pontiac | 1.0% | 0.5% | City of Pontiac (administered by Treasury) |
| 8 | Jackson | 1.0% | 0.5% | City of Jackson |
| 9 | Battle Creek | 1.0% | 0.5% | City of Battle Creek |
| 10 | Lapeer | 1.0% | 0.5% | City of Lapeer |
| 11 | Albion | 1.0% | 0.5% | City of Albion |
| 12 | Big Rapids | 1.0% | 0.5% | City of Big Rapids |
| 13 | Hudson | 1.0% | 0.5% | City of Hudson |
| 14 | Ionia | 1.0% | 0.5% | City of Ionia |
| 15 | Muskegon | 1.0% | 0.5% | City of Muskegon |
| 16 | Muskegon Heights | 1.0% | 0.5% | City of Muskegon Heights |
| 17 | Hamtramck | 1.0% | 0.5% | City of Hamtramck (administered by Treasury) |
| 18 | Walker | 1.0% | 0.5% | City of Walker |
| 19 | Springfield | 1.0% | 0.5% | City of Springfield |
| 20 | Portland | 1.0% | 0.5% | City of Portland |
| 21 | Grayling | 1.0% | 0.5% | City of Grayling |
| 22 | Port Huron | 1.0% | 0.5% | City of Port Huron |
| 23 | East Lansing | 1.0% | 0.5% | City of East Lansing (added 2019) |
| 24 | Benton Harbor | 1.0% | 0.5% | City of Benton Harbor |

The Treasury maintains the authoritative list on its City Tax page. Highland Park is sometimes reported as inactive — Treasury has confirmed it remains active for 2025. Confirm any non-Detroit/non-Grand Rapids filing on the Treasury site before relying.

### 6.3 The base structure (uniform across all 24 cities under UCITO)

- **UCITO base structure rules** — Every UCITO city uses the same statutory framework: - Residents: taxed on ALL income from all sources (wages, self-employment, pass-through, interest, dividends, capital gains where applicable) - Nonresidents: taxed ONLY on income earned within the city — wages for services performed in the city, business income from in-city activity, rents from in-city property - Allocation/apportionment: nonresident wage earners apportion using the 'day-count' method — (days worked in city ÷ total work days) × wages. Sick days, vacation days, holidays at the home location reduce the in-city numerator - Personal exemption: each city sets its own. Detroit is $600/exemption; Grand Rapids is $600; most 1.0% cities are $600-$750. The exemption operates the same way as the state MI-W4 exemption — reduce annualized wages before applying the rate - Treaties with the state: city income tax is deductible on Michigan MI-1040 Schedule 1 (i.e., it reduces state taxable income)

### 6.4 Cities administered by Treasury

- **Treasury-administered cities** — Effective with Detroit's 2015 transition, Treasury operates collections for: - Detroit (since 2015) - Pontiac (since 2017) - Hamtramck (since 2020) - Highland Park (since 2020) These cities use Treasury's MTO portal for employer withholding remittance — much cleaner than the self-administered cities. The other 20 cities each run their own systems with separate logins and (often) paper-heavy processes.

## 7. Detroit and Grand Rapids — employer withholding deep dive

### 7.1 Detroit — Form 5321 / W/H 941 monthly + W/H 5321 reconciliation

- **Detroit resident/nonresident rates** — Detroit resident: 2.4% on all wages; Detroit nonresident working in Detroit: 1.2% on Detroit-source wages
- **Employer withholding obligation trigger** — An employer is required to withhold Detroit income tax if it has employees who either (a) live in Detroit (regardless of where work is performed), OR (b) perform services within the City of Detroit, even if they live elsewhere. Note (a) — Detroit reaches Detroit-resident telecommuters working entirely outside Detroit. The employer must withhold the resident rate (2.4%) for the resident employee, even on days worked from a Birmingham home office, because residency drives the entire wage base.
- **Detroit forms (post-2015 Treasury-administered regime)** — - Form 5321 — City of Detroit Income Tax Withholding Monthly/Quarterly Return (parallel to state Form 5080) - Form DW-3 / Form 5323 — Annual Reconciliation (parallel to state 5081) - Form DW-4 — Employee's Detroit withholding certificate (kept on file; not transmitted) Both 5321 and 5323 are filed via Treasury's MTO portal alongside state withholding — the same login.
- **Detroit due dates** — Due dates mirror state Form 5080: monthly returns due the 20th, annual reconciliation due 28 February.

### 7.2 Grand Rapids — Form GRW-3 + GR-501

- **Grand Rapids rates and exemption** — Rates: 1.5% resident / 0.75% nonresident. Personal exemption: $600 per allowance.

Grand Rapids is NOT administered by Treasury. The City of Grand Rapids Income Tax Department runs it directly.

Employer forms:
- Form GR-501 — monthly withholding payment voucher (legacy paper; e-file via grcity.us preferred)
- Form GRW-3 — Annual Reconciliation of Income Tax Withheld
- Form GRW-4 — Employee Withholding Certificate
- Form GRW-5 — Resident Working in Another GR-Tax City (credit certificate — see Section 7.4)

Due dates:
- Monthly: end of the following month (NOTE — this is different from state 5080's 20th)
- Annual GRW-3: last day of February (2026 deadline: 28 February 2026 — Saturday-Sunday rule may push to following Monday)

### 7.3 The DW-4 / GRW-4 day-count mechanism

- **Detroit day-count withholding formula** — Detroit wages subject to W/H = Gross wages × (Detroit work days / Total work days) Detroit withholding = Detroit wages × 1.2%

Update the percentage at least annually. Many employers leave 100% Detroit on the DW-4 forever and over-withhold — the employee then claims a refund on Form D-1040(NR). Over-withholding is not punitive but generates client friction.

Days worked in Detroit count:
- Any day where the employee physically performed work in Detroit, even partially (a 1-hour client meeting in Detroit = 1 Detroit day)
- Training, conferences, depositions inside the City limits

Days NOT counted as Detroit days:
- Pure commute time (in transit through Detroit to a non-Detroit worksite)
- Sick / vacation / holiday days, regardless of where taken
- Days the employee was outside Detroit, including telecommuting from a non-Detroit home

### 7.4 Reciprocity / credit between city-tax cities

- **Detroit resident working in Grand Rapids example** — If a Detroit resident works in Grand Rapids, the employee owes: Detroit 2.4% (residence) on all wages; Grand Rapids 0.75% (nonresident) on GR-day wages. The Detroit ordinance allows a credit for tax paid to another Michigan city, but capped at the Detroit nonresident rate of 1.2%. So in this example: GR withholds 0.75% on GR-source wages; Detroit allows a credit up to 1.2% (so the full 0.75% is creditable); Detroit still collects 2.4% − 0.75% = 1.65% on those GR-source wages, plus 2.4% on non-GR wages. Employers typically handle this by withholding BOTH the work-city nonresident tax AND the residence-city tax (net of credit). The employee reconciles on their D-1040 and GR-1040.

### 7.5 Quick rate table for the major cities (employer's view)

**Quick rate table for major cities**

| City | Resident WH rate | Nonresident WH rate | Annual employer form |
| --- | --- | --- | --- |
| Detroit | 2.4% | 1.2% | Form 5323 (DW-3) |
| Highland Park | 2.0% | 1.0% | HP-W3 |
| Grand Rapids | 1.5% | 0.75% | Form GRW-3 |
| Saginaw | 1.5% | 0.75% | Form SW-3 |
| Lansing | 1.0% | 0.5% | Form L-W3 |
| Flint | 1.0% | 0.5% | Form F-W3 |
| Battle Creek | 1.0% | 0.5% | BC-W3 |
| Hamtramck | 1.0% | 0.5% | Treasury-administered |
| Pontiac | 1.0% | 0.5% | Treasury-administered |
| (other 1.0% cities) | 1.0% | 0.5% | City-specific |

### 7.6 Employer registration with cities

- **City employer registration process** — For Detroit, Pontiac, Hamtramck, Highland Park — registration is built into the state Form 518 (Registration for Michigan Taxes). Check the appropriate city boxes during state setup. For Grand Rapids and the other self-administered cities — separate registration with the city income tax department. Grand Rapids requires Form GR-SS-4 (City of Grand Rapids Application for Employer Identification Number).

### 7.7 AUDIT FLASH POINT — missed nonresident city withholding for commuters

Highest-frequency Michigan payroll audit finding. Employers based outside Detroit/Grand Rapids who have just a few employees who commute into the city routinely fail to register and withhold the nonresident tax. The cities cross-reference state W-2 transmittal data (Form 5081 + W-2 box 20 locality data) against their own city employer registrations. A Birmingham-based employer with one employee living in Detroit and one driving to a Detroit jobsite three days a week is exposed.

Triggers an audit when:
- W-2 box 5 (Medicare wages) > total of all city withholdings shown
- Employee files D-1040(NR) claiming Detroit-source income with no employer DW-3 on record
- Cross-reference with state UIA data showing work locations

Mitigation:
- Run a residency / work-location audit annually using employee MI-W4 addresses and project/jobsite location lists
- Register with the relevant city the first time any employee triggers the obligation
- Document zero-Detroit-days for telecommuters in writing each year

## 8. Paid leave — PMLA versus ESTA (the 2025 reset)

This is the most volatile area of Michigan employer law in 2025. Read carefully.

### 8.1 The history

- **PMLA/ESTA legislative history** — 2018: Michigan voters' ballot initiative for sick leave qualifies. The legislature, before the election, adopts the initiative ('adopt-and-amend') and then in lame duck immediately amends it down to the Paid Medical Leave Act (PMLA), effective 29 March 2019. PMLA covers employers with 50+ employees and grants up to 40 hours/year of paid medical leave. 31 July 2024: Michigan Supreme Court rules in Mothering Justice v. Attorney General that the adopt-and-amend tactic was unconstitutional. The Court orders the original ballot initiative — now the Earned Sick Time Act (ESTA) — to take effect 21 February 2025, automatically replacing PMLA. ESTA as enacted: covers ALL employers (no 50-employee floor) — small employers (≤10 employees) accrue up to 40 hours/year; large employers (11+) accrue up to 72 hours/year. Accrual at 1 hour per 30 worked. Rehire reinstatement. Strict notice and recordkeeping. 21 February 2025: Same day ESTA takes effect, the Legislature passes and the Governor signs HB 4002 (Public Act 7 of 2025) materially amending ESTA. The amendments: - Restore a smaller-employer carve-out (1-10 employees) at 40 hours of paid + extended 30-hour grace period for some setups - Confirm 11+ employees at 72 hours/year - Adjust accrual rules, notice requirements, and clarify enforcement - Extend the small-employer effective date to 1 October 2025 (so 21 Feb 2025–30 Sep 2025 is a partial implementation window for small employers)  _(Mothering Justice v. Attorney General; HB 4002 (Public Act 7 of 2025))_

### 8.2 What applies in 2025

- **ESTA rules for employers with 11+ employees (effective 21 February 2025)** — Up to 72 hours of earned sick time per benefit year (employer's choice of calendar year, fiscal year, or anniversary year). Accrual at 1 hour per 30 hours worked (or front-load 72 hours). Covered uses: employee's own illness; family member's illness; domestic violence/sexual assault recovery; closure of workplace or child's school due to public health emergency. Family member is broadly defined — spouse, child, parent, sibling, grandparent, grandchild, in-laws, plus any individual whose close association is the equivalent of a family relationship. Paid at the same hourly rate the employee normally earns. Carryover: unused hours roll forward (no cap on carryover beyond the 72-hour annual use cap). Notice: written notice to employees within 30 days of hire OR by 1 March 2025 for existing employees. Recordkeeping: 3 years of accrual and use records — UIA-enforced.
- **ESTA rules for employers with 1-10 employees (effective 1 October 2025)** — Up to 40 hours of earned sick time per benefit year (after a 1-year exemption window). Same accrual rate.

### 8.3 Employer count — how to count

- **ESTA employee count methodology** — Count includes: - Full-time, part-time, and temporary employees - Employees on leave (count for staffing purposes) - Do NOT count contractors classified under Section 9 The count is by calendar week, and the threshold is met if the employer employed the threshold count for at least 20 weeks in the current or preceding calendar year.

### 8.4 AUDIT FLASH POINT — coverage threshold straddling

Many Michigan employers run between 8 and 14 employees seasonally. They MUST track the 20-week look-back carefully — if they cross 11 employees for 20 weeks in 2024, they are an '11+' employer for ALL of 2025, including the 21 February 2025 effective date and 72-hour entitlement. Misclassification as a small employer carries:
- Back-pay of unprovided sick hours
- $1,000-per-employee civil fine under ESTA
- UIA / LEO referral

Document the count weekly. Snapshot the headcount each Friday and store the screenshot.

### 8.5 Interaction with PMLA

- **PMLA to ESTA carryover treatment** — PMLA is repealed by operation of ESTA's effective date. Any PMLA balances at 20 February 2025 should be carried forward and credited against the ESTA 72-hour pool — Treasury / LEO guidance from March 2025 confirms this carryover treatment.  _(Treasury / LEO guidance, March 2025)_

### 8.6 What payroll software needs to track

- Hours-worked accrual (1 per 30 worked, capped at 72 or 40)
- Hours-used decrement
- Hours-carried forward at year end
- Reason code for each use (for the 3-year audit record)
- Wage at time of use (for the 'regular rate' payment)

## 9. Worker classification — economic reality + ABC

### 9.1 Three different tests in Michigan

**Classification tests by context**

| Context | Test |
| --- | --- |
| State income tax withholding | **IRS 20-factor / common-law** (Michigan conforms to federal characterization) |
| Unemployment insurance (UIA) | **Michigan economic reality test** (MCL 421.42 + case law) — broader than common-law, results in MORE employees |
| Wage and hour (minimum wage, ESTA, overtime under Workforce Opportunity Wage Act) | **20-factor**, but LEO leans toward the **ABC test** for certain industries |
| Workers' compensation | **Economic reality** plus statutory presumption |

### 9.2 The Michigan economic reality test

- **Economic reality test factors** — Per Kidder v. Miller-Davis Co., 455 Mich 25 (1997) and progeny, the UIA applies a non-exclusive multi-factor test: 1. Control — does the principal control the manner and means of work? 2. Investment — does the worker invest in their own equipment / business? 3. Opportunity for profit or loss depending on managerial skill 4. Special skill required for the work 5. Permanency of the relationship 6. Integral nature — is the work an integral part of the principal's business? No single factor controls. The UIA weighs the totality — and in close cases, presumes employee status.  _(Kidder v. Miller-Davis Co., 455 Mich 25 (1997))_

### 9.3 The ABC test — where it applies

- **ABC test in construction industry** — Michigan does NOT have a statewide ABC test for general worker classification. However, construction and certain other industries operate under stricter statutory presumptions per the Improved Workforce Opportunity Wage Act and Treasury revenue administrative bulletins. For the construction industry, a worker is presumed an employee unless: (A) Free from the principal's direction and control as a matter of fact, AND (B) Performing work outside the usual course of the principal's business, AND (C) Engaged in an independently established trade. This three-part test mirrors California's AB5/Dynamex ABC. For freelance software developers, ABC does NOT formally apply — but a UIA auditor will reach the same conclusion via the economic reality test if the developer works exclusively for one principal with no other clients.  _(Improved Workforce Opportunity Wage Act)_

### 9.4 The contractor's 1099 default — and why it is dangerous

- **1099 does not establish contractor status** — Issuing a 1099 does not establish contractor status under Michigan law. The 1099 is downstream of classification, not the cause of it. Reviewer should question: - 'Does the worker have other clients?' - 'Does the worker provide their own laptop, phone, software licenses?' - 'Does the worker set their own hours and methods?' - 'Is the work outside the principal's normal business?' (a freelance dev working on the principal's product is INSIDE the principal's normal business) If the answers tilt employee, the right outcome is to convert to W-2, register for UIA and withholding, and remediate.

### 9.5 Reclassification exposure

- **Retroactive reclassification consequences** — When UIA reclassifies a contractor as an employee retroactively: - Back UIA contributions for the entire look-back period (up to 6 years) - Interest and penalties under Section 5.5 - Possible criminal referral for willful misclassification under MCL 421.54a (rare but on the books) - Treasury reclassification follows automatically — back state withholding owed, plus interest and penalty - City tax reclassification follows automatically — back city withholding (Detroit will pursue this aggressively)  _(MCL 421.13; MCL 421.54a)_

A 5-developer freelance shop reclassified retroactively at the UIA experience-rate maximum 10.30% × $9,500 × 5 × 6 years = ~$29,355 of back UIA alone, before interest and Treasury.

## 10. W-2, 1099, and annual reporting

### 10.1 W-2 filing with Michigan

- **W-2 filing methods and due date** — Employers file W-2s with Michigan Treasury alongside Form 5081 (Section 4.4). Filing methods: - Electronic via MTO — required if filing 250 or more W-2s (the federal threshold synced) - EFW2 format — same format as federal SSA; Michigan accepts the federal file with the RS state record - Paper W-2 + 5081 — allowed for under 250, but discouraged Due 28 February 2026 for tax year 2025.

### 10.2 1099 filing with Michigan

- **1099 filing triggers and methods** — Michigan requires 1099 filing for: - 1099-NEC (nonemployee compensation) — if Michigan tax was withheld OR if the recipient is a Michigan resident, OR if the payer is a Michigan business with $600+ paid to the recipient - 1099-MISC — same triggers as 1099-NEC plus the rent/royalty reporting categories - 1099-R (retirement distributions) — if Michigan tax was withheld - W-2G (gambling winnings) — if Michigan tax was withheld Filing method: bundled with the federal Combined Federal/State Filing (CF/SF) program if the 1099 is filed via IRS FIRE — Michigan automatically receives the data. If filing via IRIS, Michigan participates as well. If withholding occurred on the 1099, file via MTO with Form 5081. Due 31 January 2026 for 1099-NEC (same as federal); 28 February 2026 for other 1099s.

### 10.3 Detroit W-2 transmittal

- **Detroit W-2 transmittal requirements** — Detroit accepts W-2 data through Treasury's MTO via Form 5323 (Detroit annual reconciliation). Local-tax box 19/20 data on the W-2 must show 'DETROIT' with the correct withholding amount. Grand Rapids and the other self-administered cities require the W-2 to be transmitted directly to the city, usually with their own annual reconciliation form (GRW-3 etc.).

## 11. Worked examples

### 11.1 Example A — Detroit employer with a non-Detroit-resident commuter

Acme Software LLC is headquartered at 1500 Woodward Avenue, Detroit (inside city limits). It employs Sarah, who lives in Royal Oak (outside Detroit). Sarah works 4 days/week at the Detroit office and 1 day/week from her Royal Oak home. Sarah's gross annual wages: $104,000 (biweekly: $4,000). She files MI-W4 claiming 1 exemption. She files DW-4 documenting 80% Detroit work-day percentage.

Gross: $4,000
Less exemption: $5,800 / 26 = $223.08
Taxable: $3,776.92
Michigan tax: $3,776.92 × 4.25% = $160.52 per pay period
Annual MI withholding: $160.52 × 26 = $4,173.52
Total annual MI tax due (rough): ($104,000 − $5,800) × 4.25% = $4,173.50 ✓ (matches)

Detroit wages: $4,000 × 80% = $3,200
Less Detroit exemption: $600 / 26 = $23.08
Detroit taxable: $3,176.92
Detroit nonresident rate: 1.2%
Detroit tax per period: $3,176.92 × 1.2% = $38.12
Annual Detroit withholding: $38.12 × 26 = $991.20

$9,500 wage base hit by end of February (paychecks 1 and 2 fully attributable + part of pay 3)
Assuming new-employer 2.7%: $9,500 × 2.7% = $256.50 UIA contribution for Sarah for 2025
Acme paid this entirely in Q1; Q2-Q4 UIA contribution for Sarah = $0
Reported on Form UIA 1028 each quarter (showing wages, even after cap)

If Acme is a quarterly filer, Q1 2025 Form 5080 (due 20 April 2025) reports:
- State withholding: $160.52 × 6 paychecks = $963.12 (assuming 6 biweekly periods in Q1)
- Detroit withholding (Section 5 of Form 5080 reports city W/H): $38.12 × 6 = $228.72

No Royal Oak tax — Royal Oak is not a UCITO city.

### 11.2 Example B — Multi-city employer (Detroit + Grand Rapids)

RegionalCo has its main office in Lansing and a satellite in Grand Rapids. It employs:
- John — lives in Detroit, works at the Lansing office 5 days/week
- Maya — lives in Cascade Township (suburb of GR, outside GR city limits), works at the Grand Rapids office 3 days/week and the Lansing office 2 days/week
- Carlos — lives in Lansing, works at the Lansing office 5 days/week

All three earn $60,000/year. Annual exemptions claimed = 1 each.

- **State withholding — same for all three** — ($60,000 − $5,800) × 4.25% = $2,303.50/year each  _(none)_

**City withholding**  _(none)_

| Employee | Residence | Work | Lansing W/H | GR W/H | Detroit W/H |
| --- | --- | --- | --- | --- | --- |
| John | Detroit | Lansing 100% | $60k × 0.5% nonres = $300 (Lansing nonresident on Lansing wages) | none | $60k × 2.4% resident = $1,440. **Credit for Lansing tax paid**, capped at Detroit nonresident equivalent rate (1.2%). Credit = min($300, $60k × 1.2%) = $300. Net Detroit W/H = $1,440 − $300 = **$1,140** |
| Maya | Cascade (non-city) | GR 60%, Lansing 40% | $60k × 40% × 0.5% nonres = $120 | $60k × 60% × 0.75% nonres = $270 | none |
| Carlos | Lansing | Lansing 100% | $60k × 1.0% resident = $600 | none | none |

Must register and file Form 5080 for Detroit (for John's resident withholding)
Must register and file Lansing withholding (for John, Maya, Carlos)
Must register and file Grand Rapids withholding (for Maya)
Lansing, GR are self-administered — separate filings each month/quarter to those cities
Detroit is via Treasury MTO alongside Form 5080
Three city employer accounts + state account = four monthly/quarterly returns plus four annual reconciliations

This is a common reviewer trap. Many bookkeepers handle only the state and assume the cities will sort themselves out at the employee level. They will not — the employer is jointly liable.

### 11.3 Example C — Contractor misclassification

SmallApp LLC (4 employees, all in Detroit) engages "Pat" as a 1099 developer. Pat works exclusively for SmallApp, on SmallApp's product, using SmallApp's MacBook, with Slack hours of 9-5 Eastern, for $90,000/year. Pat works from home in Hamtramck. SmallApp issues a 1099-NEC at year-end.

Control: SmallApp sets the project, the hours, the tools — strong employee
Investment: SmallApp provides the laptop — employee
Profit/loss: Pat has no real upside or downside — employee
Special skill: developer — neutral
Permanency: full-time, year-round — strong employee
Integral: developing SmallApp's product is the business — strong employee

Conclusion: employee. A UIA audit triggered by Pat filing for unemployment after termination would reclassify with high confidence.

UIA contributions: $9,500 × new-employer 2.7% × 3 years = $769.50, plus 10% penalty and ~9.47% interest ≈ ~$1,100
State withholding: ($90,000 − $5,800) × 4.25% × 3 years = $10,735.50 (employer is liable absent proof Pat paid on his MI-1040)
Detroit nonresident withholding (if SmallApp office is in Detroit, Pat is a Hamtramck resident commuting in): Detroit nonresident at 1.2% on $90k × 3 yrs = $3,240 (assume 100% Detroit-day) — credit for Hamtramck residency rules
Hamtramck resident withholding 1.0% on $90k × 3 = $2,700 — credit/coordination with Detroit
Penalties and interest, multiplied
Plus federal (out of scope here): 941 back-taxes, FUTA, 940

Total Michigan exposure: easily $20,000+ over three years for ONE misclassified worker. The 1099 was the wrong answer — push the client to convert Pat to W-2, register for Detroit and Hamtramck withholding, and file amended UIA 1028s for the look-back period.

## 12. Self-checks (reviewer must run before signoff)

1. MI rate verified at 4.25% — payroll software did not stick at 4.05%? Pull a sample W-2 and verify box 17 ÷ box 16 ≈ 4.25%.
2. Form 5080 filed for each quarter/month? Cross-check MTO portal "Returns Filed" against the calendar.
3. Form 5081 filed by 28 February? With matching W-2 data?
4. UIA Form 1028 filed for each quarter by the 25th of the month after quarter-end?
5. UIA wage base correct at $9,500 — software did not still hold a prior-year cap?
6. MI-W4 on file for every active employee? Including new hires within 10 days of start?
7. DW-4 / GRW-4 / city certificates on file for every employee with a city-tax obligation?
8. City employer registration completed in each city where any employee lives or works? This is the audit flash point in Section 7.7.
9. ESTA accrual records exist for each employee — start date, hours worked, hours accrued, hours used, balance carried forward?
10. Headcount determination for ESTA — 11+ employer test applied with 20-week look-back?
11. W-2 box 19/20 populated correctly for every employee with city withholding? Box 18 (local wages) ≤ box 16 (state wages)?
12. 1099-NEC issued for every contractor paid ≥ $600, transmitted via CF/SF or directly with Treasury?
13. Contractor classifications reviewed under economic reality test — at least one factor analysis on file for each 1099 worker?
14. Federal-state reconciliation — W-2 box 1 (federal wages) versus box 16 (Michigan wages) reconciled with documented differences (e.g., pre-tax 401(k) is identical, but Michigan retirement subtraction is on MI-1040, not on W-2)?

## 13. Refusals (this skill will not produce)

- **R-MI-1** — Combined-group or unitary business income tax positions. Refer to corporate-tax specialist.  _(R-MI-1)_
- **R-MI-2** — Detroit Renaissance Zone certifications. Coordinate with the Detroit Economic Growth Corporation.  _(R-MI-2)_
- **R-MI-3** — Workers' compensation premium calculations. Refer to a licensed insurance professional.  _(R-MI-3)_
- **R-MI-4** — Custom ABC test analysis for industries with statutory presumptions other than construction without LEO consultation.  _(R-MI-4)_
- **R-MI-5** — Retroactive UIA contribution reduction or experience-rate appeals — these require LEO Form UIA 1771 protest within 30 days and are not a payroll-prep task.  _(R-MI-5)_
- **R-MI-6** — ESTA / PMLA litigation defense. Pre-existing litigation requires Michigan-licensed employment counsel.  _(R-MI-6)_
- **R-MI-7** — Multi-state apportionment for a Michigan-resident remote worker performing services in another state. Defer to us-multistate-payroll.  _(R-MI-7)_
- **R-MI-8** — Pension administrator obligations under Form MI-W4P. Pension administration is a regulated activity.  _(R-MI-8)_

## 14. Sources and citations

### Statutes

- **Income Tax Act of 1967** — PIT rate, exemptions  _(MCL 206.51 et seq.)_
- **Withholding provisions** — Withholding provisions  _(MCL 206.351)_
- **Uniform City Income Tax Ordinance** — Uniform City Income Tax Ordinance  _(MCL 141.501 et seq.)_
- **Michigan Employment Security Act** — UIA  _(MCL 421.1 et seq.)_
- **SUTA Dumping Prevention** — SUTA Dumping Prevention  _(MCL 421.22b)_
- **Earned Sick Time Act** — as amended by Public Act 7 of 2025  _(MCL 408.961a et seq.)_
- **Paid Medical Leave Act** — repealed by ESTA effective 21 February 2025, but historical for pre-2025 compliance  _(MCL 408.961-408.973)_
- **Improved Workforce Opportunity Wage Act** — Improved Workforce Opportunity Wage Act  _(MCL 408.931 et seq.)_

### Case law

- **Mothering Justice v. Attorney General** — adopt-and-amend unconstitutional  _(___ Mich ___ (31 July 2024))_
- **Kidder v. Miller-Davis Co.** — economic reality test framework  _(455 Mich 25 (1997))_

### Treasury guidance

- **Revenue Administrative Bulletin (RAB) 2024-3** — Income tax rate determination  _(RAB 2024-3)_
- **Treasury City Tax page** — list of administering cities and rates  _(Treasury "City Tax" page (state of Michigan website))_
- **Form instructions** — Form 5080, Form 5081, Form 5321, Form 5323 instructions (annual updates)  _(Form 5080, Form 5081, Form 5321, Form 5323 instructions)_
- **Form UIA 1028 instructions** — annual updates  _(Form UIA 1028 instructions)_

### Federal interactions

- **IRC §3402** — withholding — Michigan conforms to federal taxable-wage definition  _(IRC §3402)_
- **IRC §3303** — FUTA state credit — Michigan is a fully-compliant state for 2025  _(IRC §3303)_

### Verification reminder

Tax rates, wage bases, and thresholds are subject to legislative change and annual indexing. Verify the following at the start of each engagement:
- MI PIT rate (Treasury RAB or MCL 206.51 trigger calc)
- UIA wage base ($9,500 for 2025 — verify via UIA Form 1771)
- City rates and personal exemptions on each city's website
- ESTA accrual rules in case of further legislative amendment

## End of mi-payroll skill v0.1 — pending review.

End of mi-payroll skill v0.1 — pending review.

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
