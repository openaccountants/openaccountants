---
name: in-payroll
description: Indiana Payroll Skill
jurisdiction: US-IN
domain: state-tax
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# in-payroll

## 1. Scope

This skill covers Indiana (US-IN) employer payroll tax obligations for tax
year 2025. It is designed for small employers (1-50 employees) with an
Indiana nexus through either: (a) Indiana-resident employees, (b) Indiana
work locations, or (c) employees performing services in Indiana on a
non-incidental basis.

**In scope:**

- Indiana personal income tax (PIT) withholding at the 3.15% flat rate
  (2025), including the multi-year statutory phase-down to 2.9% by 2027
- Indiana supplemental wage withholding (bonuses, commissions, severance,
  retroactive wage adjustments) at 3.15% for 2025
- Form WH-4 (Indiana Employee's Withholding Exemption and County Status
  Certificate)
- Form WH-1 (Indiana Withholding Tax Voucher) – periodic remittance
- Form WH-3 (Annual Withholding Reconciliation) and the W-2 transmittal
- Indiana unemployment insurance (SUTA) under the Department of Workforce
  Development (DWD): $9,500 taxable wage base, experience-rated employer
  rates from 0.50% to 7.40%, new employer rate of 2.5%
- County tax (Local Option Income Tax / LOIT) for all 92 counties,
  including the binding January 1 residence rule that locks the county
  rate for the full tax year
- Reciprocal income tax agreements with Ohio (OH), Kentucky (KY), Michigan
  (MI), Pennsylvania (PA), and Wisconsin (WI)
- Worker classification under Indiana's ABC test (administered by DWD for
  unemployment purposes) and the right-to-control test (administered by
  the Department of Revenue for income tax withholding)
- Final wage payment timing (next regular payday)
- Wage payment frequency and pay stub disclosures
- Direct deposit and pay card rules
- New hire reporting

**Out of scope:**

- Federal income tax withholding (see `us-federal/federal-payroll.md`)
- FICA, FUTA, and federal W-2 mechanics
- Indiana corporate income tax (covered in `us-in/in-corporate-tax.md`)
- Indiana sales and use tax (covered in `us-in/in-sales-tax.md`)
- Indiana property tax
- Workers' compensation premium computation (Indiana Workers'
  Compensation Board – referenced only in passing)
- Multi-state nexus determination beyond the five reciprocal states
- Equity compensation (RSUs, ISOs, ESPPs) – only basic sourcing rules
  noted
- Garnishments beyond a high-level summary

**Authority and source documents:**

- Indiana Code Title 6 (Taxation), Article 3 (Adjusted Gross Income Tax)
- Indiana Code Title 6, Article 3.6 (Local Income Taxes) – the modern
  successor to the older CAGIT/COIT/CEDIT structure
- Indiana Code Title 22, Article 4 (Unemployment Compensation System)
- Indiana Code Title 22, Article 2 (Wages, Hours, and Benefits)
- Indiana Department of Revenue (DOR) Departmental Notice #1 (effective
  for 2025), which publishes the 92-county tax rate schedule used by
  employers to compute county withholding
- DOR Information Bulletin #32 (county tax withholding) and #33
  (reciprocal agreements)
- DWD Employer Handbook (2025 edition)

## 2. Indiana Personal Income Tax (PIT) Withholding – 3.15% Flat Rate

- **Flat rate structure** — Indiana imposes a flat-rate state adjusted gross income tax. There is no progressive bracket structure and no separate tax computation for supplemental wages versus regular wages – the same flat rate applies to both.  _(IC 6-3-2-1(b))_

### 2.1 The 2025 rate and statutory phase-down

**Indiana PIT rate schedule under IC 6-3-2-1(b)**  _(IC 6-3-2-1(b), as last amended by HEA 1001-2023 and HEA 1427-2023)_

| Tax year | Indiana PIT rate |
| --- | --- |
| 2023 | 3.15% |
| 2024 | 3.05% |
| 2025 | **3.15%** (see note below) |
| 2026 | 3.00% |
| 2027 | **2.90%** (statutory floor) |

**Note on the 2025 rate.** The legislative phase-down originally placed
the 2025 rate at 3.00%. HEA 1001-2023 contained revenue-based triggers
that could accelerate or delay the cuts. For purposes of this skill the
rate used for 2025 employer withholding is **3.15%**, matching the rate
published in DOR Departmental Notice #1 for the 2025 calendar year and
the rate that Indiana employers were instructed to use for January 1
2025 forward. A reviewer signing off on a 2025 return must confirm the
rate against the Departmental Notice in effect for the relevant pay
period before filing.

- **Wages for withholding purposes** — The Indiana PIT rate is applied to federal adjusted gross income modified by Indiana add-backs and subtractions. For withholding purposes, the rate is applied to "wages" as defined under IC 6-3-4-8(b), which adopts the federal definition under IRC §3401 with Indiana modifications.  _(IC 6-3-1-3.5; IC 6-3-4-8(b); IRC §3401)_

### 2.2 Supplemental wages

- **Supplemental wage withholding rate** — Indiana does not have a separate supplemental withholding rate. Bonuses, commissions, severance, retroactive wage adjustments, and similar non-regular wage payments are withheld at the same 3.15% flat state rate for 2025, plus the employee's applicable county rate.

This differs sharply from the federal supplemental wage flat rate of 22% under IRS Pub 15. Practitioners migrating from a federal-only mindset sometimes apply 22% to Indiana supplemental wages – this is incorrect and overwithholds by roughly 7x.

### 2.3 Withholding mechanics

- **Per-pay-period withholding computation** — 1. Take the employee's gross taxable wages. 2. Subtract the per-pay-period value of the employee's WH-4 exemptions. Each personal exemption is $1,000/year prorated by pay periods; each dependent exemption is $1,500/year for the first dependent (a 2023 increase). Additional dependent exemptions of $1,500 also apply. 3. Multiply the remainder by 3.15% (state) and the applicable county rate to obtain the per-period state and county withholding. 4. Round to the nearest cent.  _(IC 6-3-1-3.5(a))_
- **No standard deduction / additional withholding line** — There is no Indiana standard deduction in the withholding formula, and no separate "additional withholding" line – instead, employees who want additional state or county withholding write the dollar amount per pay period directly on the WH-4 (Lines 7 and 8 respectively).

### 2.4 Employees claiming exempt status

- **Conditions for exempt status** — An employee may claim exempt from Indiana income tax withholding only if: the employee had no Indiana income tax liability in the prior year AND expects none in the current year, OR the employee is a resident of a reciprocal state (OH, KY, MI, PA, WI) and has filed the appropriate exemption documentation, OR the employee qualifies under the Servicemembers Civil Relief Act or the Military Spouses Residency Relief Act.  _(IC 6-3-4-8 and WH-4 instructions)_
- **Annual renewal and liability** — Exempt-status WH-4 filings must be re-executed annually by February 15 in the same manner as federal Form W-4. An employee who claims exempt incorrectly is personally liable for the under-withheld tax; the employer is not liable provided the WH-4 is on file in good faith.

## 3. Form WH-1 – Periodic Withholding Remittance

### 3.1 Filing frequency

**WH-1 filing frequency by average monthly withholding**

| Avg. monthly withholding | Filing frequency | Voucher / due date |
| --- | --- | --- |
| Less than $83.33 | **Annual** | January 31 |
| $83.33 – $999.99 | **Monthly** | 30th of the following month |
| $1,000.00 – $7,083.33 | **Monthly with EFT** | 30th of the following month |
| Above $7,083.33 (i.e. >$85,000/year) | **Early filer** (semi-monthly EFT) | 20th of the same month (1st-15th) and 5th of following month (16th-end) |

These thresholds correspond to roughly $1,000/year, $12,000/year, and $85,000/year in total withholding respectively.

> **Important.** The thresholds for "monthly with EFT" and "early filer" are administrative determinations made by DOR and may shift year-to-year. A reviewer should confirm the current threshold against the WH-1 instructions before re-classifying an employer.

### 3.2 Mandatory electronic filing

- **INTIME mandatory e-filing** — All Indiana withholding tax must be filed electronically through INTIME (Indiana Taxpayer Information Management Engine) effective January 1 2022. Paper WH-1 vouchers are no longer accepted from active employers.  _(DOR notice in 2021)_

### 3.3 Late filing and late payment penalties

- **Late filing penalty** — The greater of $5 or 10% of the unpaid tax.  _(IC 6-8.1-10-2.1)_
- **Late payment penalty** — 10% of the unpaid tax.  _(IC 6-8.1-10-2.1)_
- **Interest rate on unpaid withholding (2025)** — approximately 7% per annum (compare against current DOR notice)  _(IC 6-8.1-10-1)_
- **Fraudulent non-remittance penalty and responsible person liability** — 100% penalty for fraudulent withholding non-remittance, and personal liability under responsible person liability extending to officers and individuals with control over withheld funds.  _(IC 6-8.1-10-4; IC 6-2.5-9-3)_

### 3.4 Zero-liability periods

- **Zero WH-1 filing requirement** — A registered employer must still file a WH-1 for each period in its assigned frequency, even if no tax was withheld. Filing a "zero" WH-1 through INTIME satisfies this requirement. Failing to file zero returns generates automatic non-filer notices and may trigger a billing for an estimated assessment.

## 4. Form WH-3 – Annual Withholding Reconciliation

### 4.1 What WH-3 does

- **Purpose of WH-3** — WH-3 reconciles total tax withheld during the calendar year (per all WH-1 filings) against the sum of state and county income tax shown on the employer's W-2s. It is the Indiana analogue of federal Form W-3 and the IRS reconciliation that occurs on the employer's 941 series.

### 4.2 Due date

- **WH-3 due date** — WH-3 is due January 31 following the close of the calendar year. All W-2s, W-2Gs, and 1099-Rs showing Indiana withholding must be filed electronically with the WH-3 through INTIME. The same January 31 deadline applies to copies furnished to employees.

### 4.3 Late filing and late W-2 penalties

- **Late W-2 filing penalty** — $10 per W-2 filed late (capped at $25,000 per employer per year).  _(IC 6-8.1-10-6)_
- **WH-3 non-filing treatment** — Failure to file WH-3 is treated as a non-filing of an information return, with the same penalty structure. Persistent non-filing can lead DOR to revoke the employer's withholding registration, which prevents lawful Indiana payroll operations.

### 4.4 Reconciliation discrepancies

- **WH-3 mismatch resolution** — When the WH-3 totals differ from the WH-1 totals reported during the year, DOR will issue a "WH-3 mismatch" letter. The employer must: provide an amended WH-1 (Form WH-1U) for any period that was underreported, with payment of the difference plus penalty and interest, OR claim a refund or credit against future periods for any overreported period via INTIME.

Mismatches commonly arise from:

1. Treating a bonus payment as nontaxable for Indiana when it is in fact taxable.
2. Failing to update an employee's county-tax classification when they moved across a county line on or before January 1.
3. Misclassifying a reciprocal-state employee mid-year and missing the required true-up.

## 5. County Tax – Local Option Income Tax (LOIT)

### 5.1 All 92 counties impose a county tax

- **Universal county levy and rate range** — Indiana is the only state where every county levies a local income tax (the few counties that had no LOIT historically have all adopted one by 2017). Rates for 2025 range from approximately 0.50% to 2.864%, with most counties falling between 1.00% and 2.25%.
- **LOIT consolidation** — The county-tax structure was consolidated under IC 6-3.6 (effective 2017), replacing the older CAGIT / COIT / CEDIT three-tax structure with a single LOIT framework administered uniformly through Indiana payroll withholding.  _(IC 6-3.6)_

### 5.2 Selected county rates for 2025

**Selected county rates for 2025**  _(DOR Departmental Notice #1)_

| County | County name (FIPS) | 2025 rate |
| --- | --- | --- |
| Marion | Indianapolis | 2.02% |
| Lake | Gary / Crown Point | 1.50% |
| Allen | Fort Wayne | 1.59% |
| Hamilton | Carmel / Fishers | 1.10% |
| St. Joseph | South Bend | 1.75% |
| Vanderburgh | Evansville | 1.20% |
| Tippecanoe | Lafayette / Purdue | 1.10% |
| Monroe | Bloomington / IU | 2.035% |
| Porter | Valparaiso | 0.50% |
| Vigo | Terre Haute | 2.00% |
| Madison | Anderson | 2.25% |
| Delaware | Muncie | 1.50% |
| Pulaski | (highest in 2025) | **3.38%** in some prior years, ~2.864% in others — confirm |

> **Reviewer note.** The "highest county" in Indiana changes year to year as smaller counties enact emergency rate hikes. Pulaski and Cass have historically been near the top. Always reconfirm by pulling the current Departmental Notice #1.

### 5.3 The January 1 residence rule – AUDIT FLASH POINT

- **January 1 county residence locks rate for full year** — Under IC 6-3.6-8-1, the county rate that applies to an employee for the entire calendar year is the rate in effect in the county where the employee was a resident on January 1 of that year. The rate does NOT change mid-year if the employee moves to another Indiana county. The rate does NOT follow the employee. If an employee moves on January 2, the January 1 county's rate still applies for all 12 months.  _(IC 6-3.6-8-1)_
- **Non-resident on January 1 rule** — If the employee was not an Indiana resident on January 1, the employer instead uses the rate of the county in which the employee's principal place of employment was located on January 1. If the employee was not employed by the current employer on January 1, the employer determines the principal place of employment as of the first day of employment, and that county rate applies for the remainder of the calendar year.  _(IC 6-3.6-8-1)_

Practical sequence each year:

1. On or before January 1, require every employee to file an updated WH-4 stating their county of residence and county of principal employment as of January 1.
2. Use the residence county rate (Box A on WH-4). If the employee was not an Indiana resident on January 1, use the principal-place-of-employment county rate (Box B on WH-4) instead.
3. Lock that rate in payroll for the remainder of the year.
4. Re-run the determination on January 1 of the next year.

Failure to capture an accurate January 1 status is the single most common Indiana payroll audit finding. Employers often default new hires to the rate of their work-location county rather than the employee's residence county – this is wrong for an Indiana resident and overrides their statutory rate.

### 5.4 County withholding mechanics

- **Total Indiana withholding rate formula** — County tax is withheld in addition to the 3.15% state rate and is remitted on the same WH-1 voucher in a separate column / line. County tax is reported on the W-2 in Box 19 (Local income tax) with Box 20 (Locality name) showing the Indiana county name and FIPS code prefix (e.g. "MARION-IN" for Marion County). Total rate = 3.15% (state) + county rate (residence on Jan 1) For a Marion County resident in 2025: 3.15% + 2.02% = 5.17% total Indiana income tax withholding

## 6. Form WH-4 – Employee's Withholding Exemption and County Status Certificate

### 6.1 What WH-4 does

- **Purpose of WH-4** — WH-4 is the Indiana state analogue of federal Form W-4 with one critical addition: it also establishes the employee's county tax status under IC 6-3.6. An employer cannot lawfully compute Indiana withholding without a WH-4 on file.  _(IC 6-3.6)_

### 6.2 When WH-4 must be filed

- **Filing triggers for WH-4** — - At hire (before the first wage payment). - On or before January 1 each year if the employee's residence or county of principal employment has changed. - On or before any pay period after a change in personal exemptions (marriage, birth of a dependent, etc.). - When claiming exempt status (must be renewed annually by February 15).
- **Default withholding if no WH-4 on file** — If no WH-4 is on file, the employer must withhold state income tax at 3.15% with zero exemptions and county tax at the county rate applicable to the employee's work location (because the employer cannot determine the residence county without the WH-4).

### 6.3 Key fields

- Line 1: Personal exemption ($1,000/year claim per exemption).
- Line 2: Additional exemptions for the employee's spouse if not employed.
- Line 3: Dependent exemption ($1,500/year per dependent; first dependent claims an extra $1,500 if the employee is unmarried head of household).
- Line 4: County of residence on January 1.
- Line 5: County of principal employment on January 1 (only used if the employee is NOT an Indiana resident on January 1).
- Line 6: Additional Indiana state tax to withhold per pay period.
- Line 7: Additional county tax to withhold per pay period.
- Line 8: Exempt status declaration (reciprocal state, military spouse, zero-liability prior year).

### 6.4 Record retention

- **WH-4 retention period** — The employer must retain WH-4 forms for at least 3 years after the employee's last day of employment. DOR can request WH-4 forms during any payroll audit, and missing WH-4s create a default presumption that the employer should have withheld at the maximum applicable rate.  _(IC 6-8.1-5-4)_

## 7. Reciprocal Agreements with Surrounding States

### 7.1 The five reciprocal states

- **Indiana's reciprocal states** — Indiana has reciprocal income tax agreements with: Ohio (OH), Kentucky (KY), Michigan (MI), Pennsylvania (PA), and Wisconsin (WI). Under these agreements, wages earned by a resident of one state while working in the other state are taxable only by the state of residence, not by the state where the work is performed. The reciprocal agreement covers W-2 wages only — it does NOT cover self-employment income, lottery winnings, rental income, or investment income.

> Indiana does NOT have a reciprocal agreement with Illinois. A Chicago-area commuter who lives in Indiana and works in Illinois pays Illinois income tax to Illinois on the wages and then claims a credit for taxes paid to another state on their Indiana IT-40.

### 7.2 Practical effect for Indiana employers

- **Indiana employer hiring reciprocal-state resident** — 1. The employee files Indiana Form WH-47 (Certificate of Residence in Reciprocal State) with the employer. 2. The Indiana employer does NOT withhold Indiana state income tax. 3. The Indiana employer DOES still withhold Indiana county tax based on the county where the employee works (because Indiana county tax is not covered by the reciprocal agreement, and the employee is not an Indiana resident on January 1). 4. The Indiana employer should register with and withhold the home state income tax (e.g. Ohio Form IT-4 for an Ohio resident), subject to the home state's own employer rules.
- **Out-of-state employer hiring Indiana resident** — 1. The employee files the home-state equivalent reciprocity form (e.g. Ohio IT-4NR, Kentucky 42A809, Michigan MI-W4). 2. The out-of-state employer does NOT withhold the other state's income tax. 3. The out-of-state employer SHOULD withhold Indiana state and county tax based on the Indiana residence, subject to the employer's Indiana nexus.  _(IC 6-3-2-2(a))_

### 7.3 AUDIT FLASH POINT — Missed reciprocal classifications

- **Consequences of missed reciprocal classification** — A missed reciprocal classification creates double withholding that the employee must unwind through two refund claims, and the employer remains exposed to a tax-collected-but-not-properly-allocated finding. The DOR audit team specifically looks for: (a) Indiana employers withholding Indiana state tax on employees who filed a WH-47 (over-withheld and over-remitted to Indiana); (b) Indiana employers NOT withholding Indiana county tax on reciprocal-state employees (under-withheld and short-remitted to Indiana); (c) Indiana employers failing to register for and remit Ohio / Kentucky / Michigan / Pennsylvania / Wisconsin withholding when they have a reciprocal-state employee. All three patterns are commonly flagged in a DOR payroll audit and all three create assessment exposure.

### 7.4 Local taxes are not covered

- **Reciprocal agreements do not cover local taxes** — A critical limitation: reciprocal agreements between states do NOT extend to local taxes. - An Indiana resident working in Louisville, Kentucky still owes the Louisville Metro Occupational License Tax. - An Indiana resident working in a Pennsylvania municipality still owes the local Earned Income Tax (EIT) and Local Services Tax (LST) under PA Act 32. - An Indiana resident working in Detroit still owes the Detroit city income tax (currently 2.4% for residents, 1.2% for non-residents). Conversely, an Ohio resident working in Indianapolis still owes the Marion County tax at 2.02% even though Indiana state income tax is not withheld.

## 8. Indiana Unemployment Insurance (SUTA)

### 8.1 Wage base and rate structure

- **Taxable wage base** — $9,500 per employee per year (one of the lowest in the country – has not changed since the 1980s)  _(IC 22-4-4-2)_
- **Experience rating range** — 0.50% (lowest experience rating) to 7.40% (highest experience rating, sometimes called the "delinquent" or "max" rate for employers with adverse experience)
- **New employer rate** — 2.5% for non-construction employers, and a higher industry-specific rate for construction (typically the industry average for construction NAICS codes, which has run around 2.5%-3.5% depending on the year)
- **Reserve-ratio experience rating method** — The experience rating is determined by Indiana DWD using the reserve-ratio method, which compares contributions paid in minus benefits charged out, divided by average annual taxable payroll over three years.  _(IC 22-4-11)_

### 8.2 Registration

- **SUTA liability trigger** — An Indiana employer becomes liable for SUTA contributions when it: pays $1 or more of wages in any calendar quarter, AND has at least one employee (which the ABC test analysis is used to determine), AND is not otherwise exempt.  _(IC 22-4-8)_
- **Registration process** — Registration is done through Uplink Employer Self Service (ESS) at www.in.gov/dwd. A SUTA account number is issued; this is distinct from the DOR withholding account number.

### 8.3 Quarterly UC-1/UC-5 filing

- **UC-1 and UC-5 reporting requirements** — SUTA contributions are reported on the UC-1 Wage and Employment Report (showing each employee, their gross wages for the quarter, and the taxable wages up to the $9,500 cap) and remitted with the UC-5 Contribution Report. Due dates: April 30 (Q1), July 31 (Q2), October 31 (Q3), January 31 (Q4). Filing is electronic only via Uplink ESS for any employer with 25 or more employees. Smaller employers may still file on paper but most use Uplink.

### 8.4 Voluntary contributions

- **Voluntary contribution mechanism** — An employer with adverse experience may make a voluntary contribution by the early March deadline each year to reduce its SUTA rate for the upcoming year. The breakeven analysis: if the voluntary contribution cost is less than the projected first-year SUTA savings on next year's taxable payroll, the contribution makes sense.  _(IC 22-4-11.5)_

### 8.5 SUTA dumping prohibition

- **SUTA dumping enforcement** — Indiana enforces the federal SUTA Dumping Prevention Act and its own state-level transfer-of-experience rules. Common SUTA-dumping patterns that trigger criminal investigation by DWD: - Setting up a new LLC each year to obtain the new-employer rate. - Transferring employees to a related entity with a lower experience rate without transferring the experience history. - Acquiring a company solely to "absorb" its lower rate. Penalties include the maximum 7.40% rate for the current and two succeeding years, plus civil penalty of up to 2% of taxable wages.  _(IC 22-4-11.5-7)_

## 9. Worker Classification – The ABC Test

### 9.1 Indiana's three-part ABC test for unemployment purposes

- **ABC test elements** — Under IC 22-4-8-1, an individual performing services for wages is presumed to be an employee for unemployment compensation purposes unless ALL THREE of the following are established by the putative employer: - A. Behavioral / control test. The individual is free from control or direction in the performance of the service, both under the contract of service and in fact. - B. Business test. The service is performed outside the usual course of the business for which the service is performed, OR is performed outside all of the places of business of the enterprise for which the service is performed. - C. Customarily engaged test. The individual is customarily engaged in an independently established trade, occupation, profession, or business of the same nature as that involved in the service performed. This is the same "ABC test" used (with variations) by Massachusetts, New Jersey, and California (in the Dynamex / AB 5 form). All three prongs must be satisfied for the worker to be a contractor; failure of any one prong means the worker is an employee for SUTA purposes.  _(IC 22-4-8-1)_

### 9.2 Right-to-control test for income tax withholding

- **Right-to-control test applicability** — For DOR income tax withholding purposes, Indiana follows the federal common-law right-to-control test (IRS 20-factor test, later consolidated into behavioral, financial, and relationship-of-the-parties categories). This is a more employer-friendly test than the ABC test.  _(IRS Rev. Rul. 87-41)_

> **Practical consequence.** A worker may pass the right-to-control test (and so receive a 1099-NEC for federal income tax purposes) but fail the ABC test (and so be reclassified as an employee for SUTA purposes). Indiana DWD will assess back unemployment contributions, penalty, and interest on the "shadow employees" even though the DOR and IRS treated the worker as a contractor.

This dual-test divergence is the single most expensive classification trap in Indiana payroll.

### 9.3 Penalties for misclassification

- **Misclassification penalty structure** — - DWD back contributions for up to 3 prior years. - Penalty of 1.5x the unpaid contribution. - Interest at 1% per month. - Workers' Compensation Board separately can pursue uninsured exposure. - DOR can pursue unwithheld income tax. - Possible criminal liability for knowing misclassification.  _(IC 22-4-29-1; IC 22-4-11-2(c); IC 22-3-2; IC 6-3-4-8; IC 22-4-29; IC 6-8.1-10-5)_

## 10. Wage Payment, Final Pay, and Other Workplace Rules

### 10.1 Pay frequency

- **Minimum pay frequency requirements** — Wages must be paid at least semi-monthly or biweekly. Salaried exempt employees may be paid monthly. Wages must be paid within 10 business days of the end of the pay period to which they relate.  _(IC 22-2-5-1)_

### 10.2 Final pay – next regular payday

- **Final wage payment timing** — An employee who leaves employment voluntarily or involuntarily must be paid all wages due by the next regular payday on which the wages would otherwise have been paid. Indiana does NOT require immediate payment at termination (unlike California or Colorado). However: the employer cannot delay payment to "investigate" alleged misconduct, theft, or property return beyond the next regular payday absent court order. If an employee requests written final pay information, the employer must comply.  _(IC 22-2-9-2)_
- **Vacation/PTO payout at termination** — Vacation / PTO payout at termination is governed by the employer's written policy. Indiana courts (e.g. Naugle v. Beech Grove City Schools, 864 N.E.2d 1058 (Ind. 2007)) treat accrued vacation as wages if the employer's policy promises payout.  _(Naugle v. Beech Grove City Schools, 864 N.E.2d 1058 (Ind. 2007))_

### 10.3 Wage Payment Statute claims

- **Liquidated damages for late wage payment** — A non-fault late wage payment is subject to liquidated damages of 10% per day up to a maximum of 200% of the unpaid wages, plus attorney fees. This is a powerful private right of action and the most common Indiana wage-and-hour lawsuit pattern.  _(IC 22-2-5-2)_

### 10.4 Pay stub disclosures

- **Required pay statement contents** — Each pay statement (paper or electronic) must show: hours worked; wages paid for the pay period; a listing of deductions made. There is no statutory requirement to itemize state vs. county tax separately on the pay stub, but virtually all payroll software does so to support the WH-3 reconciliation.  _(IC 22-2-2-8)_

### 10.5 Direct deposit and pay cards

- **Direct deposit and pay card requirements** — Direct deposit can be required by the employer in Indiana provided that the employee may select the financial institution. Pay cards are permitted but the employee must be able to make at least one no-fee withdrawal per pay period.  _(IC 22-2-5-1.1)_

### 10.6 Paid sick leave – NO state mandate

- **No state or local paid sick leave mandate** — Indiana has no state-mandated paid sick leave and no state-mandated paid family leave. Indiana also does not impose any local paid-sick-leave requirements on private employers (and indeed has a state preemption statute that bars municipalities from enacting their own paid-sick-leave mandates).  _(IC 22-2-16)_

This contrasts sharply with neighboring Illinois (which has the Illinois Paid Leave for All Workers Act effective January 1 2024, at 40 hours/year).

### 10.7 New hire reporting

- **New hire reporting deadline** — All Indiana employers must report new hires (and re-hires after a 60-day separation) to the Indiana New Hire Reporting Center within 20 days of the hire date. Reporting is done online at www.in-newhire.com or by submitting an FCR-style file.  _(IC 22-4-32)_

## 11. Worked Examples

### 11.1 Example 1 — IN-IL Chicago commuter (no reciprocity)

**Facts.** Alex Patel is a software engineer who lives in Schererville, Lake County, Indiana (resident on January 1 2025). Alex commutes daily to a Chicago, Illinois office of NorthShore Capital LLC, an Illinois employer with no Indiana nexus and no Indiana payroll tax registration. Alex's 2025 gross wages are $120,000, paid semi-monthly ($5,000 per pay period, 24 periods).

**Analysis.**

1. **Indiana–Illinois reciprocity.** There is no Indiana–Illinois reciprocal agreement. (Indiana's reciprocal partners are OH, KY, MI, PA, WI only.) Therefore Illinois imposes its state income tax on the wages Alex earns while physically working in Illinois.
2. **Illinois withholding.** NorthShore Capital withholds Illinois income tax at the Illinois 4.95% flat rate on the wages earned while Alex is physically in Illinois. Approximate Illinois withholding: $120,000 × 4.95% = $5,940.
3. **Indiana withholding.** Because NorthShore Capital has no Indiana nexus, it is NOT required to register with DOR and withhold Indiana state and county tax. Alex must instead make Indiana estimated tax payments (Form IT-40ES) for 2025.
4. **Indiana state tax.** $120,000 × 3.15% = $3,780 before exemptions and the credit for taxes paid to other states.
5. **Indiana county tax.** Alex is a Lake County resident on January 1, so the Lake County rate of 1.50% applies. $120,000 × 1.50% = $1,800.
6. **Credit for taxes paid to another state.** Alex's Indiana IT-40 will claim a credit (Schedule 6, Credit for Local Taxes Paid Outside Indiana, and credit for taxes paid to other states on IT-40 Schedule 6) for the Illinois tax. The credit is capped at the Indiana state tax that would have applied to the same income. Effectively, Alex's Indiana state tax of $3,780 is wiped out by the Illinois credit, but the Lake County tax of $1,800 still owes because Illinois state tax credit does not offset Indiana county tax.
7. **Net Indiana payment.** Alex makes quarterly estimated payments totaling approximately $1,800 for the year to cover the Lake County tax. If Alex does not, the Indiana underpayment penalty under IC 6-3-4-4.1 applies.

**Reviewer notes.** This pattern catches many cross-border employees by surprise. Practitioners should flag for any Indiana-resident / Illinois-employer client (a) Indiana quarterly estimated payments are required because the IL employer cannot/will not withhold Indiana tax, and (b) the county tax obligation remains in full because the credit for taxes paid to another state offsets only the Indiana state tax component.

### 11.2 Example 2 — IN-only employer with Marion County resident

**Facts.** Indy Mechanical Services Inc. is a small HVAC contractor based in Indianapolis, Marion County. It has 8 employees, all of whom are Marion County residents on January 1 2025. Gross monthly payroll is $40,000. The company's prior-year DWD experience rating is 2.10%.

**Analysis.**

1. **WH-4.** Each employee files a WH-4 listing Marion County as their residence on January 1.
2. **State withholding.** $40,000 × 3.15% = $1,260 per month.
3. **County withholding.** $40,000 × 2.02% (Marion County 2025 rate) = $808 per month.
4. **Total Indiana income tax withholding.** $2,068 per month.
5. **WH-1 filing frequency.** Total annual withholding is roughly $2,068 × 12 = $24,816. This is above the $1,000/year threshold (monthly filer) and below the $85,000/year threshold (early filer / semi-monthly). So Indy Mechanical files monthly WH-1 vouchers via INTIME, due the 30th of the following month.
6. **WH-3 reconciliation.** Due January 31 2026 with eight W-2s uploaded through INTIME. Box 17 of each W-2 shows the Indiana state tax withheld. Box 19 shows the Marion County tax withheld with locality name "MARION-IN".
7. **SUTA.** Wage base $9,500 per employee × 8 employees = $76,000 taxable wages. Rate 2.10%. Annual SUTA contribution: $76,000 × 2.10% = $1,596. Quarterly UC-1/UC-5 reports are due 4/30, 7/31, 10/31, and 1/31.
8. **New hire reporting.** Each new hire reported within 20 days.

**Reviewer notes.** Even with a single county and a single state, the employer must run the WH-1 monthly, the UC-1/UC-5 quarterly, and the WH-3 annually. Missing any periodic filing triggers the 10% penalty plus interest plus possible non-filer notice escalation.

### 11.3 Example 3 — Reciprocal Ohio resident hired by Indiana employer

**Facts.** RiverBend Pharma LLC is a small biotech company in Lawrenceburg, Dearborn County, Indiana. It hires Sandra Lee, who lives in Cincinnati, Hamilton County, Ohio, and commutes to Lawrenceburg daily. Sandra's salary is $80,000.

**Analysis.**

1. **Reciprocity.** Indiana and Ohio have a reciprocal agreement. Sandra files Indiana Form WH-47 with RiverBend.
2. **Indiana state income tax withholding.** RiverBend does NOT withhold the 3.15% Indiana state income tax on Sandra's wages.
3. **Indiana county tax withholding.** Reciprocity does NOT extend to county tax. Sandra is not an Indiana resident on January 1, so under IC 6-3.6-8-1 the rate is determined by the county of principal employment on January 1 — Dearborn County. Dearborn County's 2025 rate is approximately 1.20% (confirm against Departmental Notice #1). RiverBend withholds $80,000 × 1.20% = $960 per year for Dearborn County tax.
4. **Ohio state income tax withholding.** RiverBend should register as an Ohio employer (Ohio IT 1) and withhold Ohio state tax under the Ohio progressive brackets. Sandra files Ohio Form IT-4 with RiverBend.
5. **Ohio local taxes.** Sandra does not work in any Ohio municipality (she works in Indiana), but her Cincinnati city income tax obligation may still attach as a "residence tax" if Cincinnati imposes a residence tax on the wages — under most Ohio city rules, residence tax applies and is offset by a credit for tax paid to the work municipality. Indiana does not impose a "work municipality" tax in the Ohio sense, so Sandra likely owes Cincinnati residence tax with no offsetting credit. RiverBend is not generally required to withhold Cincinnati city tax (the employee handles it through Cincinnati estimated payments or year-end filing). Coordinate with Ohio counsel.
6. **WH-4 and WH-47.** Both forms must be retained for 3+ years.
7. **WH-1 and WH-3.** RiverBend reports Sandra's Dearborn county withholding on the WH-1 and WH-3 even though it reports zero Indiana state tax for her.

**Reviewer notes.** This is the highest-risk pattern in Indiana payroll. A common error is to withhold neither Ohio income tax nor Indiana county tax for Sandra, on the (mistaken) view that the reciprocal agreement zeroed out all state-level obligations. Both amounts are owed; the employer is exposed to under-withholding for both Ohio and Indiana county.

### 11.4 Example 4 — Contractor misclassification (ABC test)

**Facts.** Hoosier Cleaning Co. operates janitorial services across Marion County. It engages 12 "independent contractor" cleaners on 1099-NEC. Each cleaner: (a) is given a route and a schedule by Hoosier; (b) wears Hoosier-branded shirts that Hoosier provides; (c) cleans only Hoosier client sites; (d) is paid hourly through Bill Pay; (e) does not have their own business name, insurance, or other clients.

**ABC test application.**

- Prong A (control). Hoosier sets routes, schedules, and methods. Fails. The cleaners are not free from direction and control.
- Prong B (course of business). Cleaning IS the usual course of Hoosier's business. Fails.
- Prong C (customarily engaged). None of the cleaners has their own cleaning business, brand, license, or other clients. Fails.

All three prongs fail. For DWD purposes, the cleaners are employees, not contractors.

**Consequences.**

- DWD back-assesses SUTA contributions for the past 3 years at Hoosier's experience rate plus 1.5x penalty plus 1%/month interest.
- DOR back-assesses unwithheld Indiana state tax and Marion County tax under IC 6-3-4-8 (3.15% + 2.02% = 5.17% applied to gross payments).
- Workers' Compensation Board may pursue Hoosier under IC 22-3-2 for uninsured exposure plus penalty.
- Federal exposure: IRS Section 530 relief is not available because Hoosier did not file Forms 1099-NEC consistently across all cleaners (some were paid more than the $600 threshold without 1099 issuance, per facts).

**Reviewer notes.** Conversion to W-2 going forward is the only defensible path. Some firms attempt a quiet conversion without voluntarily disclosing past misclassification — this is risky because DWD audit cycles increasingly cross-reference DOR 1099 data and the former contractors are common unemployment-claim filers themselves. The Indiana Voluntary Classification Settlement Program (analogous to the IRS VCSP) can be used for prospective conversion with limited look-back, but the program terms change periodically — confirm current parameters with DOR before filing.

### 11.5 Example 5 — January 1 county move (audit flash point)

**Facts.** Maya Cortez was a resident of Hamilton County (Carmel) on January 1 2025. On March 1 2025 she moves to Marion County (Indianapolis). Her employer, ChartLogic Software LLC, updates her WH-4 in March and switches her county tax withholding from Hamilton (1.10%) to Marion (2.02%) effective with the next pay period.

**Analysis.**

- The employer's action is INCORRECT. Under IC 6-3.6-8-1, Maya's county tax rate for the entire 2025 calendar year is locked at the Hamilton County rate of 1.10%, because she was a Hamilton County resident on January 1 2025. The fact that she moved on March 1 is irrelevant for 2025 withholding.
- Correct action. Withhold 1.10% for all 12 months of 2025. On January 1 2026, Maya files a new WH-4 stating Marion County as her residence as of January 1 2026, and from January 1 2026 forward the employer withholds at the Marion County rate (2.02% in 2025, whatever the 2026 rate proves to be — likely the same in 2026 unless the council adopts a change).
- Audit exposure. ChartLogic over-withheld for Maya from March through December 2025. The excess ($X × (2.02% - 1.10%) for those months) must be either (a) refunded to Maya in a corrective paycheck and recovered from DOR through a WH-1U adjustment, or (b) claimed by Maya on her IT-40.

> **AUDIT FLASH POINT — Always re-train payroll on the rule: the January 1 rate locks for the full year. Never change county withholding mid-year due to an Indiana-to-Indiana move. The ONLY mid-year change is when an employee moves OUT of Indiana entirely (then they become subject to no Indiana county tax going forward, but they remain liable for the full year's county tax via the IT-40 on the wages earned during the period they were an Indiana resident).**

## 12. Reviewer Checklist

Before signing off on an Indiana payroll year-end, confirm:

- [ ] Each employee has a WH-4 on file for the current year with correct January 1 residence county.
- [ ] State tax withheld matches 3.15% × taxable wages (or the current-year Departmental Notice #1 rate).
- [ ] County tax withheld for each employee matches the published 2025 rate for their January 1 residence county.
- [ ] No mid-year county rate changes were applied for Indiana-to-Indiana moves.
- [ ] All employees from reciprocal states (OH, KY, MI, PA, WI) have a WH-47 on file and Indiana state tax is NOT withheld for them.
- [ ] All reciprocal-state employees nevertheless have Indiana county tax withheld at the appropriate rate.
- [ ] WH-1 filing frequency matches DOR's most recent classification letter, with no missed periods (including zero-liability periods).
- [ ] WH-3 reconciliation matches the sum of WH-1 amounts and the sum of W-2 amounts.
- [ ] UC-1/UC-5 quarterly reports are filed and SUTA contributions are paid on time.
- [ ] All workers paid on 1099-NEC have been tested under the ABC test, not merely the right-to-control test.
- [ ] New-hire reporting has been filed within 20 days for every hire and rehire.
- [ ] Final-pay checks were issued by the next regular payday for every termination during the year.
- [ ] Pay-stub disclosures (hours, wages, deductions) are present on every pay statement.
- [ ] No paid-sick-leave accrual is being tracked under any local ordinance (Indiana state preemption applies).

## 13. Citations and Cross-References

- IC 6-3 (Adjusted Gross Income Tax)
- IC 6-3.6 (Local Income Taxes, replacing CAGIT/COIT/CEDIT)
- IC 6-8.1-10 (Penalties and Interest)
- IC 22-2-2 (Minimum Wage / Pay Statements)
- IC 22-2-5 (Wage Payment)
- IC 22-2-9 (Wage Payment Upon Separation)
- IC 22-2-16 (Paid Sick Leave State Preemption)
- IC 22-4 (Unemployment Compensation System)
- IC 22-4-8-1 (ABC Test)
- HEA 1001-2023 / HEA 1427-2023 (PIT rate phase-down)
- DOR Departmental Notice #1 (annual rate schedule)
- DOR Information Bulletin #32 (county tax withholding)
- DOR Information Bulletin #33 (reciprocal agreements)
- DWD Employer Handbook (2025 edition)
- IRS Rev. Rul. 87-41 (right-to-control test, referenced via DOR practice)
- Naugle v. Beech Grove City Schools, 864 N.E.2d 1058 (Ind. 2007) (vacation as wages)

**Related skills in this repository:**

- `us-federal/federal-payroll.md` — federal layer (W-4, 941, 940, FICA, FUTA)
- `us-in/in-individual-income-tax.md` — IT-40 individual return, including the credit for taxes paid to other states
- `us-in/in-corporate-tax.md` — IN corporate adjusted gross income tax
- `us-il/il-payroll.md` — Illinois payroll (for the IN-IL commuter fact pattern in Example 1)
- `us-oh/oh-payroll.md` — Ohio payroll (for reciprocal pattern)
- `us-ky/ky-payroll.md` — Kentucky payroll (for reciprocal pattern)
- `us-mi/mi-payroll.md` — Michigan payroll (for reciprocal pattern)
- `_cross-border/us-reciprocal-state-agreements.md` — consolidated reference

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).
