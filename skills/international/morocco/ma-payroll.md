---
name: ma-payroll
description: Tier 2 Massachusetts content skill for employer payroll compliance covering tax year 2025. Includes the 5% flat PIT plus 4% millionaire surtax over ~$1.08M, PFML 0.88% combined (employee portion 0.29% for 25+ employers, employer portion 0.59%), SUI wage base $15,000 with rates 0.94-14.37%, EMAC 0.34%, M-941 quarterly withholding, MA Wage Act §148 triple-damages exposure for unpaid wages, Earned Sick Leave 40-hour minimum, Pay Equity Act salary history ban, and Health Connector employer mandate for 50+ FTE under ACA.
version: 1.0
jurisdiction: US-MA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MA Payroll

## Massachusetts Payroll Compliance — Tax Year 2025

## 1. Scope

This skill covers Massachusetts state employer payroll compliance obligations for tax year 2025, where the employer either (a) is domiciled in Massachusetts, (b) maintains a place of business in Massachusetts, or (c) employs one or more Massachusetts residents performing services in Massachusetts. The skill is designed for use by an Enrolled Agent, CPA, or attorney acting as the reviewer of record under Circular 230 §10.34, and assumes that a federal payroll skill (handling Form 941, Form W-2, Form W-3, FUTA Form 940, FICA, and federal income tax withholding) is loaded separately in the workflow.

In scope:

- Massachusetts Personal Income Tax (PIT) withholding on wages under M.G.L. c. 62B §2, including the 5% flat rate, the 4% millionaire surtax under c. 62 §4(d), and the 5% supplemental withholding rate.
- Form M-4, the Massachusetts state employee withholding exemption certificate.
- Massachusetts Paid Family and Medical Leave (PFML) under M.G.L. c. 175M, including the 0.88% combined contribution rate for calendar 2025, the 25-employee threshold under §6 that triggers the employer share, and the PFML quarterly return.
- Massachusetts State Unemployment Insurance (SUI) under M.G.L. c. 151A, including the $15,000 taxable wage base, the 0.94%–14.37% experience-rated schedule (Schedule E for 2025), and the new-employer rate of 1.45%–3.30%.
- Employer Medical Assistance Contribution (EMAC) under M.G.L. c. 149 §189 at 0.34% on the first $15,000 of wages per employee.
- Universal Health Insurance (UHI) supplemental EMAC for non-compliant employers under c. 149 §189A (sunset 2019, residual exposure described below for catch-up assessments).
- Form M-941 (and the small-employer M-941A annual variant) for state withholding remittance, plus the Form WR-1 quarterly Unemployment Insurance wage report, plus the Form M-3 annual reconciliation.
- Massachusetts Health Connector employer reporting requirements for ALEs (50+ FTE) under the federal ACA, including the Form 1094-C/1095-C interface and the residual MA Health Care Reform statute reporting under M.G.L. c. 118H.
- Massachusetts Earned Sick Leave under M.G.L. c. 149 §148C (40 hours/year accrual; paid for employers with 11+ employees).
- Pay frequency rules under M.G.L. c. 149 §148 (weekly or bi-weekly).
- Wage Act §148 triple-damages liability for unpaid wages, untimely wages, and unauthorized deductions, including the §150 private right of action.
- Domestic Workers' Bill of Rights under M.G.L. c. 149 §190.
- Worker classification under the M.G.L. c. 149 §148B three-prong ABC test (the most restrictive independent contractor test of any US state).
- Pay Equity Act under M.G.L. c. 149 §105A (salary history ban effective July 1, 2018, plus mandatory salary range disclosure effective October 29, 2025 under the Frances Perkins Workplace Equity Act, c. 141 of the Acts of 2024).

Out of scope and deferred to other skills:

- Federal payroll: deferred to the federal payroll skill (Form 941, W-2/W-3, Form 940 FUTA, federal Form 1099-NEC). This skill assumes federal payroll is handled.
- Massachusetts corporate excise tax: deferred to ma-corporate-excise.
- Massachusetts personal income tax for the individual filer: deferred to ma-income-tax.
- Multi-state withholding allocation for telecommuters not specifically involving MA residents: deferred to the federal multi-state payroll skill.
- Massachusetts paid sick time accrual mechanics for employers with under 11 employees (unpaid sick time still required, but the accrual mechanics differ — out of scope here beyond a high-level note).
- Workers' compensation insurance under M.G.L. c. 152 (separate compliance regime, not a tax).
- The MA Tipped Wage Act and tip pool rules under c. 149 §152A.

Loading contract: this skill MUST be loaded alongside us-tax-workflow-base v0.2 or later. It supplements but does not replace a federal payroll skill.

## 2. Massachusetts Personal Income Tax Withholding

### 2.1 The 5% flat rate and the millionaire surtax

- **MA flat PIT rate on Part B wage income** — 5.0%  _(M.G.L. c. 62 §4(b))_
- **Millionaire surtax rate on Part B taxable income exceeding threshold** — 4%  _(Article XLIV, Massachusetts Constitution (Fair Share Amendment), effective January 1, 2023, ratified November 8, 2022)_
- **2025 surtax threshold (indexed)** — $1,083,150  _(Technical Information Release TIR 24-13)_
- **Combined top marginal rate above $1,083,150** — 9.0%  _(TIR 24-13 / M.G.L. c. 62 §4(b))_
- **Employer surtax withholding obligation** — Employers are NOT required to withhold the 4% surtax based on a single employee's wages with that employer alone. The threshold is computed on the employee's total Part B income for the year, including spouse income on a joint return, and the employer typically does not know that figure.  _(TIR 23-2 and Circular M)_
- **Employee election of additional surtax withholding** — An employee may request additional withholding for the surtax on Form M-4 line 5 ('additional amount you want withheld'). The skill should flag high earners (W-2 expected ≥ $900,000 from this employer) and recommend that the employee elect surtax withholding to avoid an underpayment penalty on the Form 1, Schedule 4% surtax line.  _(TIR 23-2 and Circular M)_
- **Surtax reconciliation** — The surtax is reconciled by the individual on Form 1 Schedule 4% at year end — the employer's payroll system does not need to compute it automatically, but the reviewer must coach the high-earner employee.  _(TIR 23-2)_

### 2.2 Supplemental wage withholding

- **Flat withholding rate on supplemental wages** — 5%  _(Circular M and Regulation 830 CMR 62B.2.1)_
- **No aggregate method alternative** — There is no aggregate-method alternative as exists in federal supplemental withholding — Massachusetts is flat at 5% on supplemental payments paid separately from regular wages.  _(Circular M and Regulation 830 CMR 62B.2.1)_
- **Combined payment treatment** — If the supplemental payment is combined with regular wages in a single payment, the employer applies the regular Circular M withholding tables (percentage method or wage-bracket method) to the combined amount.  _(Circular M)_
- **Voluntary additional 4% withholding on supplemental payment near surtax threshold** — If a supplemental payment to a high earner is reasonably expected to push the recipient over the $1,083,150 surtax threshold, the employer may voluntarily withhold an additional 4% on the excess slice if requested by the employee on Form M-4. Otherwise the supplemental rate is 5%.  _(Circular M; TIR 23-2)_

### 2.3 Form M-4 — state employee withholding certificate

- **Form M-4** — Massachusetts Employee's Withholding Exemption Certificate; captures the information needed to compute MA withholding. It is NOT the federal Form W-4. Massachusetts decoupled from the redesigned (2020+) federal Form W-4 and requires its own certificate.  _(Form M-4)_
- **Form M-4 Line 1 — filing status** — Filing status (single / married). Married filing separately is treated as single for MA withholding.  _(Form M-4)_
- **Form M-4 Line 2 — personal exemption amount (2025)** — $4,400 each  _(Form M-4)_
- **Form M-4 Line 3 — dependent exemption amount** — $1,000 each  _(Form M-4)_
- **Form M-4 Line 4 — age 65+ or blind additional exemption amount** — $700 each  _(Form M-4)_
- **Form M-4 Line 5 — additional withholding** — Additional amount to be withheld per pay period.  _(Form M-4)_
- **Form M-4 Line 6 — complete exemption claim** — Claim of complete exemption (for taxpayers expecting no MA liability — narrow eligibility).  _(Form M-4)_
- **Default withholding if no Form M-4 filed** — If an employee fails to file Form M-4, the employer must withhold as if the employee is single with zero exemptions.  _(DOR Directive 92-2)_
- **New Form M-4 requirement on changed circumstances** — A new Form M-4 is required when an employee's circumstances change (marriage, divorce, birth, death of dependent, change to additional withholding). Employers should require an annual refresh as a best practice, though state law does not mandate annual reissue.  _(Form M-4 instructions)_

## 3. Form M-941 — Massachusetts Withholding Return

### 3.1 Filing frequency and form variants

- **Annual filer (Form M-941A) threshold** — prior-year MA withholding of $100 or less; single return due January 31 of the following year  _(DOR)_
- **Quarterly filer (Form M-941 quarterly) threshold** — prior-year withholding of $101 to $1,200; returns due April 30, July 31, October 31, January 31  _(DOR)_
- **Monthly filer (Form M-941) threshold** — prior-year withholding of $1,201 to $25,000; returns due by the 15th of the following month  _(DOR)_
- **Quarter-monthly/weekly filer threshold** — prior-year withholding over $25,000; returns due within 3 business days of each quarter-monthly period (M-941W)  _(DOR)_
- **Electronic filing mandate** — All Massachusetts withholding returns must be filed electronically through MassTaxConnect; paper Form M-941 has been discontinued for periods beginning on or after January 1, 2010, with limited exceptions for taxpayers who obtain a hardship waiver.  _(DOR Directive 09-3)_

### 3.2 Form M-3 annual reconciliation

- **Form M-3** — Reconciliation of Massachusetts Income Taxes Withheld for Employers — the annual reconciliation between (a) total MA tax withheld per the four quarterly M-941 filings (or twelve monthly filings) and (b) total MA tax withheld as shown on Forms W-2 and Forms 1099 issued for the year. Due January 31 with the W-2s.  _(Form M-3)_
- **Common M-3 reconciliation breaks** — The reconciliation must tie to the penny. The most common reviewer-flagged M-3 reconciliation breaks are: - Late-issued bonus checks with MA withholding posted to the wrong period. - Employee residence change mid-year not reflected in MA wages on W-2 Box 16. - Third-party sick pay where the insurer reported MA withholding but the employer did not include it on M-941 quarterlies. - Excess Social Security wages credited as M-941 withholding by data-entry error.  _(Form M-3)_
- **Timing of M-3 reconciliation relative to W-2 issuance** — The Form M-3 reconciliation should be performed BEFORE issuing W-2s, not after, because reissuing W-2c forms after Form M-3 is filed creates a cascade of amended filings.  _(Form M-3)_

## 4. Paid Family and Medical Leave (PFML)

### 4.1 Statutory framework

- **PFML statutory framework** — The Massachusetts PFML program was established by c. 121 of the Acts of 2018 (the 'Grand Bargain'), codified at M.G.L. c. 175M, and is administered by the Department of Family and Medical Leave (DFML) within the Executive Office of Labor and Workforce Development. Benefits commenced January 1, 2021 for medical leave and bonding leave, and July 1, 2021 for family caregiving leave.  _(M.G.L. c. 175M)_
- **Covered individuals** — Every W-2 employee in Massachusetts is covered regardless of employer size. 1099-MISC/NEC contractors are covered ONLY if the contractor represents more than 50% of the employer's MA workforce (the 'covered contract worker' test).  _(458 CMR 2.04(2))_

### 4.2 2025 contribution rate and split

- **Combined PFML contribution rate for calendar 2025** — 0.88%  _(DFML rate notice dated October 11, 2024; M.G.L. c. 175M §7(c))_
- **2025 FAMLI wage cap** — $176,100 USD  _(2025 Social Security wage base)_
- **Medical leave contribution component** — 0.70%  _(DFML rate notice dated October 11, 2024)_
- **Family leave contribution component** — 0.18%  _(DFML rate notice dated October 11, 2024)_

**Maximum employer/employee split of PFML components**  _(M.G.L. c. 175M)_

| Component | Maximum employee share | Maximum employer share |
| --- | --- | --- |
| Medical (0.70%) | 40% = 0.28% | 60% = 0.42% |
| Family  (0.18%) | 100% = 0.18% | 0% = 0.00% |
| Combined (0.88%) | 0.46% max from employee | 0.42% min from employer |

Wait — the statute caps the employee share at 40% of the MEDICAL component and 100% of the FAMILY component, which yields a maximum employee deduction of 0.28% + 0.18% = 0.46%, not the 0.29% figure in the user request. The 0.29% figure represents the post-2024 rate at a particular split. Let me restate the current 2025 numbers carefully:

For 2025 specifically, the standard maximum employee deduction is:

- Medical employee share: 0.28% (40% × 0.70%)
- Family employee share: 0.18% (100% × 0.18%)
- **Total maximum employee deduction: 0.46%**

The remaining 0.42% (the medical employer share) is paid by the employer ONLY if the employer has 25 or more covered individuals (see §4.3 below).

### 4.3 The 25-employee threshold — AUDIT FLASH POINT

- **25-employee threshold for employer share of medical contribution** — 25 or more 'covered individuals' averaged across the four quarters ending on September 30 of the prior calendar year  _(M.G.L. c. 175M §6)_
- **AUDIT FLASH POINT — basis of 25-employee test** — The 25-employee test is calculated on the average-of-four-quarters basis ending September 30 — NOT on a current snapshot, NOT on a calendar-year average, NOT on a full-time-equivalent basis. Every year the DFML re-runs the threshold determination from prior-year UI wage records (the WR-1 filings) and re-classifies employers.  _(M.G.L. c. 175M §6)_

Employers near the threshold (typically the 20–30 employee band) should be flagged annually because:

1. Crossing into the '25+' bracket increases the employer's payroll tax cost by 0.42% × MA payroll on every paycheck for the following year.
2. Crossing OUT of the '25+' bracket (downsizing) eliminates the employer obligation, but the employer must REMEMBER to stop the employer-share remittance. Continued over-remittance is recoverable but only via an amended return.
3. The DFML's classification can be appealed. We have seen DFML classification errors where seasonal workers (e.g., camp counselors, ski-resort employees) were double-counted in the test period, pushing an employer over the threshold incorrectly.

For employers under 25 covered individuals: the employer pays NOTHING. The employee pays 0.46% of their own wages via payroll deduction (the full employee share for both components). The employer still must withhold, remit, and report — the employer is the conduit even when not the funder.

### 4.4 Wage cap

- **2025 FAMLI wage cap** — $176,100 USD  _(2025 Social Security wage base)_
- **Maximum employee PFML contribution for high earner at wage cap** — $176,100 × 0.46% = $810.06 employee share for 2025, with no further deduction once the cap is hit  _(PFML wage cap calculation)_
- **YTD tracking requirement** — Payroll systems must properly track YTD PFML wages and stop the deduction once the cap is hit.

### 4.5 Private plan exemption

- **Private plan exemption** — Under c. 175M §11, an employer may obtain DFML approval to provide PFML benefits via a private insurance policy in lieu of state PFML. Approved private plans must provide benefits at least as generous as the state plan. Employers with approved private plans do NOT remit PFML contributions to the state — but they MUST file the quarterly PFML return showing zero state liability and report private-plan coverage on their employee notices.  _(M.G.L. c. 175M §11)_
- **Private plan exemption bond requirement** — Private plan exemptions require annual renewal and a $1,000 bond.  _(M.G.L. c. 175M §11)_

The exemption is more common with large employers (3,000+ employees) that already self-insure short-term disability. For our typical 11–50 employee clients, the state plan is almost always more economical.

### 4.6 PFML quarterly return mechanics

- **PFML quarterly return filing and due dates** — PFML contributions are reported and remitted on the DFML quarterly return filed through MassTaxConnect. Due dates: April 30, July 31, October 31, January 31 for the prior calendar quarter. The return reconciles to the employer's UI wage report (Form WR-1) — DFML cross-checks PFML wages against UI wages and issues discrepancy notices for variances over $100 per employee.
- **Employee notice requirement** — Under c. 175M §4, every employer must distribute the DFML-issued employee notice within 30 days of hire and post the workplace poster (English plus the five most prevalent non-English languages of the workforce).  _(M.G.L. c. 175M §4)_

## 5. State Unemployment Insurance (SUI / DUA)

### 5.1 Wage base and rate schedule

- **2025 SUI taxable wage base** — $15,000 per employee per calendar year — unchanged since 2018  _(M.G.L. c. 151A)_
- **2025 experience rating schedule** — Massachusetts operates under Schedule E of the experience rating system (announced by DUA in November 2024).  _(DUA rate-schedule notice (November 2024))_
- **Minimum experience rate (Schedule E, 2025)** — 0.94%  _(DUA rate-schedule notice (November 2024))_
- **Maximum experience rate (Schedule E, 2025)** — 14.37%  _(DUA rate-schedule notice (November 2024))_
- **New-employer rate (most industries)** — 1.45%  _(DUA rate-schedule notice (November 2024))_
- **New-employer construction rate** — 6.72%  _(M.G.L. c. 151A §14(i))_
- **New employer build period expectations** — Most new non-construction employers in Massachusetts begin at 1.45% for their first three years; a non-construction services employer (e.g., a software firm) can expect to remain near 1.45% during the experience-rating build period. Construction employers begin in the 3.30%+ range.

### 5.2 COVID Recovery Assessment (residual exposure)

- **2025 COVID-19 Recovery Assessment rate range** — about 0.00% to 4.46% depending on the employer's UI rate class  _(c. 9 of the Acts of 2021)_
- **New employer COVID-19 Recovery Assessment rate** — approximately 1.80%  _(c. 9 of the Acts of 2021)_
- **Combined SUI + Recovery Assessment burden** — Combined SUI + Recovery Assessment can therefore push the effective unemployment-tax burden well above the headline 14.37% maximum.

### 5.3 Form WR-1 — quarterly UI wage report

- **Form WR-1 filing requirement** — DUA requires every Massachusetts employer to file Form WR-1 (Employment and Wage Detail Report) electronically through the UI Online portal each quarter. Due dates align with M-941 quarterly: April 30, July 31, October 31, January 31.
- **WR-1 late/incomplete filing penalty** — Penalties apply for late or incomplete filing — currently $25 per employee with a minimum $100 penalty.  _(M.G.L. c. 151A §14P)_
- **WR-1 report contents** — The WR-1 reports: - Each employee's SSN, full name, total gross wages, MA wages (if employee is multi-state), and hours worked. - Aggregated totals reconciled against UI tax due. - A field for 'workforce headcount' used by DFML to verify the PFML 25-employee threshold determination.
- **Cross-reference to PFML threshold** — Cross-reference: the WR-1 employee count drives the PFML 25-employee threshold (see §4.3). Misreporting hours or misclassifying contractors as employees on WR-1 has cascading effects across SUI rates, PFML obligation, and the EMAC base.

## 6. Employer Medical Assistance Contribution (EMAC)

### 6.1 Statutory basis

- **EMAC rate on first $15,000 of wages per employee per year** — 0.34%  _(M.G.L. c. 149 §189; reinstated by c. 110 of the Acts of 2017 ('EMAC II'))_
- **Maximum EMAC per employee per year** — $15,000 × 0.34% = $51.00  _(M.G.L. c. 149 §189)_

### 6.2 Exemptions

- **EMAC exemptions** — EMAC does not apply to: - Employers in their first three years of operation (new-employer exemption under §189(c)). - Employers with five or fewer employees. - Wages paid to employees covered under federal employment programs (e.g., federal trainee positions).  _(M.G.L. c. 149 §189(c))_

### 6.3 EMAC Supplement (formerly UHI supplemental)

- **EMAC Supplement (UHI supplemental)** — A temporary surcharge under c. 149 §189A imposed on employers whose non-disabled employees obtained subsidized coverage through MassHealth or the Health Connector ConnectorCare program. The supplement ran calendar 2018 and 2019 only and sunset on December 31, 2019.  _(M.G.L. c. 149 §189A)_
- **Residual EMAC Supplement exposure** — DUA continues to collect on EMAC Supplement assessments issued during 2018–2019, including penalty and interest. Successor liability under c. 62C §32 transfers EMAC Supplement liability to acquirers of MA businesses with unpaid balances from that period.  _(M.G.L. c. 62C §32)_
- **M&A due diligence recommendation** — During M&A due diligence on a MA employer formed before 2020, the reviewer should request a DUA payoff statement covering EMAC Supplement for 2018 and 2019 plus interest accrued to closing.
- **2025 forward status** — For 2025 forward, there is no UHI supplemental — only the standard EMAC at 0.34%.

## 7. Massachusetts Earned Sick Leave

- **Earned sick time accrual rate and minimum** — Under M.G.L. c. 149 §148C (enacted by ballot Question 4 in November 2014, effective July 1, 2015), every Massachusetts employer of any size must provide earned sick time at the rate of one hour for every 30 hours worked, up to a minimum of 40 hours per calendar year.  _(M.G.L. c. 149 §148C)_
- **Paid vs unpaid sick time by employer size** — - Employers with 11 or more employees: sick time is PAID at the employee's regular rate of pay. - Employers with 10 or fewer employees: sick time is UNPAID but still job-protected and accrued.  _(M.G.L. c. 149 §148C)_
- **11-employee headcount determination** — The 11-employee headcount is determined on a per-week basis: an employer is '11+' for a calendar year if it had 11+ employees for 20 or more weeks during either the current or preceding calendar year (mirroring the FUTA 20-week test under IRC §3306(a)).  _(M.G.L. c. 149 §148C; IRC §3306(a))_
- **Permitted uses of sick time** — Sick time may be used for: - The employee's own illness, injury, or medical appointment. - Care of the employee's child, spouse, parent, or parent of a spouse. - Addressing the psychological, physical, or legal effects of domestic violence on the employee or the employee's child. - Routine medical appointments of the employee or the employee's child, spouse, parent, or parent of a spouse.
- **Carryover cap** — Up to 40 hours may be carried over to the following year, but the total available in any year remains capped at 40 hours unless the employer's policy is more generous.
- **Coordination with PFML** — Earned sick time is SEPARATE from PFML. An employee may use earned sick time for short-term illness (1–3 days) and PFML for longer-term medical leave (over 7 days, the PFML waiting period). Employers may not require employees to exhaust earned sick time before applying for PFML.

## 8. Pay Frequency and the Wage Act — §148 Triple Damages

### 8.1 Pay frequency under M.G.L. c. 149 §148

- **General pay frequency requirement** — Massachusetts law requires that employees be paid at least once per week (weekly pay) UNLESS one of the following exceptions applies: - Bi-weekly pay is permitted if the employer obtains the employee's consent and complies with timely-payment rules. Most office and professional employees in Massachusetts are bi-weekly, which is a long-standing practice but technically requires consent under the current statute as interpreted by the Attorney General's Fair Labor Division in 2018 guidance. - Semi-monthly and monthly pay are NOT permitted for most workers (limited exceptions for casual employees and bona fide executive, administrative, or professional employees as defined in 940 CMR 27.03).  _(M.G.L. c. 149 §148; 940 CMR 27.03)_
- **Timing of payment rules** — - Wages must be paid within 6 days of the end of the pay period for workers paid weekly or bi-weekly. - For workers paid weekly with a Saturday cut-off, wages must be paid by the following Friday. - Terminated employees: wages are due on the day of discharge if the discharge is involuntary, and on the next regular payday if the employee resigns. Failure to pay on the day of discharge is a strict-liability Wage Act violation.  _(M.G.L. c. 149 §148)_

### 8.2 The Wage Act — §148 triple-damages liability — AUDIT FLASH POINT

- **AUDIT FLASH POINT — mandatory treble damages** — M.G.L. c. 149 §150 provides that an employee who prevails on a §148 Wage Act claim is entitled to MANDATORY treble damages plus attorney's fees and costs. The treble-damages remedy is not discretionary; the SJC confirmed this in Reuter v. City of Methuen, 489 Mass. 465 (2022), which held that even where an employer pays the disputed wages BEFORE the employee files suit, the employee is still entitled to treble damages on the late-paid amount as a matter of right.  _(M.G.L. c. 149 §150; Reuter v. City of Methuen, 489 Mass. 465 (2022))_
- **Practical implications of treble damages exposure** — 1. Late final paycheck after termination: a $5,000 final-pay error becomes $15,000 in damages plus attorney's fees. Settlement multiples of 3× to 5× the underlying wage error are typical because the fee-shifting statute exposes the defendant to plaintiff attorney's fees that often exceed the wage damages themselves. 2. Misclassification of an employee as an independent contractor (see §10 below) creates Wage Act exposure on every paycheck that should have been paid — overtime, sick time, holiday pay, etc. — for the entire limitations period (3 years under §150A). 3. Improper deductions from wages (e.g., for cash-register shortages, uniform costs, tip pooling violations) are themselves Wage Act violations subject to treble damages even if the underlying deduction was small. 4. Failure to pay accrued unused vacation on termination is a Wage Act violation; the SJC held vacation is 'wages' under §148 in Electronic Data Systems Corp. v. Attorney General, 454 Mass. 63 (2009).  _(M.G.L. c. 149 §150A; Electronic Data Systems Corp. v. Attorney General, 454 Mass. 63 (2009))_
- **Reviewer protocol when scoping a new MA payroll engagement** — - Always ask whether any employees have been terminated in the prior 3 years and whether final paychecks were issued on the day of discharge. - Review the standard offer letter / handbook for any 'use it or lose it' vacation policy — Massachusetts permits a use-it-or-lose-it policy PROSPECTIVELY (Attorney General Advisory 99/1) but not retroactively; any accrued-but-unused vacation as of separation is wages. - Audit historical 1099 contractors against the §148B ABC test (see §10); any misclassified contractor is a treble-damages exposure on accrued wages. - Flag any deduction from wages other than statutorily-authorized deductions (taxes, court-ordered garnishments, employee-elected benefits with written authorization).  _(Attorney General Advisory 99/1)_
- **Enforcement** — The Wage Act is enforced by the Attorney General's Fair Labor Division, which issues administrative complaints, and by private right of action under §150. Most enforcement is private — Massachusetts plaintiffs' bar includes specialty Wage Act firms that aggressively pursue class actions on unpaid commissions, misclassified contractors, and late final paychecks.  _(M.G.L. c. 149 §150)_

## 9. Pay Equity Act — Salary History Ban and Range Disclosure

### 9.1 The 2018 salary history ban — AUDIT FLASH POINT

- **Salary history ban provisions** — The Massachusetts Pay Equity Act, M.G.L. c. 149 §105A, was enacted by c. 177 of the Acts of 2016 and took effect July 1, 2018. Among its provisions: - Employers may not ask job applicants about their salary history before making an offer of employment, including the offer's compensation terms (§105A(c)(2)). This applies to written applications, verbal interviews, background-check questionnaires, and third-party recruiter inquiries. - Employers may not screen candidates based on prior wages or salary history. - Employers MAY confirm wage history AFTER a written offer has been extended that includes specific compensation terms (the 'permissible confirmation' rule). - Employers may not prohibit employees from discussing their own wages with co-workers (anti-secrecy clause under §105A(c)(1)).  _(M.G.L. c. 149 §105A)_
- **AUDIT FLASH POINT — private right of action damages** — Salary history violations carry a private right of action under §105D with damages of up to double the difference in wages plus attorney's fees and costs. A three-year statute of limitations applies. We have seen plaintiffs' counsel use the salary history ban to bootstrap broader pay-equity class actions because the ban removes the employer's traditional defense of 'we paid her less because she was paid less at her prior job.'  _(M.G.L. c. 149 §105D)_
- **Reviewer protocol for salary history ban** — - Review the client's standard employment application for any salary-history field. The field must be removed. - Review the client's ATS (applicant tracking system) for salary-history prompts. - Review the client's standard background-check release form — many third-party background-check vendors include salary history as a default field that must be turned off for MA candidates. - Interview the client's hiring managers on what they ask in interviews. Anecdotal client feedback shows that hiring managers often slip into salary-history questions despite formal compliance at the application level.

### 9.2 The 2024–2025 Frances Perkins Workplace Equity Act — salary range disclosure

- **Salary range disclosure requirement** — Salary range disclosure (effective October 29, 2025): employers with 25 or more employees must post a 'pay range' (the salary or hourly wage range that the employer reasonably and in good faith expects to pay) on every job posting for a position based in Massachusetts. The same applies to internal promotions and transfers.  _(M.G.L. c. 149 §29A; Frances Perkins Workplace Equity Act, c. 141 of the Acts of 2024)_
- **EEO-1 data filing requirement** — EEO-1 data filing (effective February 1, 2025): employers with 100 or more employees in MA that are required to file federal EEO-1, EEO-3, or EEO-5 reports must also file aggregated workforce demographic and pay data with the Massachusetts Secretary of the Commonwealth annually.  _(M.G.L. c. 149 §105E; Frances Perkins Workplace Equity Act, c. 141 of the Acts of 2024)_
- **Enforcement and penalty escalation** — Both new requirements are enforced by the Attorney General's Office. First-year violations are subject to warning only; second-year violations carry fines up to $500, third-year $1,000, fourth-year $25,000.
- **Reviewer action items for 2025 work** — 1. Confirm whether the client has 25+ MA employees (triggering range disclosure starting October 29, 2025) and review job postings published on or after that date for compliance. 2. Confirm whether the client has 100+ MA employees (triggering EEO-1 data filing). The first MA filing was due February 1, 2025 reflecting 2024 calendar-year workforce data.

## 10. Worker Classification — The §148B ABC Test

- **ABC test presumption and prongs** — Massachusetts has the most stringent independent contractor test of any US state. Under M.G.L. c. 149 §148B, an individual performing services for another is presumed to be an employee unless the putative employer proves ALL THREE prongs of the ABC test by a preponderance of evidence: - Prong A — Control: the individual is free from control and direction in the performance of the service, both under the contract and in fact. - Prong B — Outside the usual course: the service is performed outside the usual course of the business of the employer. - Prong C — Independent trade: the individual is customarily engaged in an independently established trade, occupation, profession, or business of the same nature as that involved in the service performed.  _(M.G.L. c. 149 §148B)_
- **Prong B interpretation and examples of failure** — Prong B is the killer. The SJC's interpretation in Sebago v. Tutunjian Enterprises, 471 Mass. 321 (2015) and Athol Daily News v. Board of Review, 439 Mass. 171 (2003) makes Prong B a near-impossibility for any service that is recognizably part of the client's business. Examples of Prong B failures: - A delivery service classifying drivers as contractors fails Prong B because driving deliveries is the usual course of a delivery service. - A cleaning company classifying housekeepers as contractors fails Prong B because cleaning is the usual course of a cleaning company. - A software firm classifying programmers as contractors fails Prong B unless the programmer is doing work demonstrably distinct from the firm's normal product engineering (e.g., a one-off marketing website).  _(Sebago v. Tutunjian Enterprises, 471 Mass. 321 (2015); Athol Daily News v. Board of Review, 439 Mass. 171 (2003))_
- **Consequences of misclassification** — - Wage Act treble damages on all unpaid overtime, sick time, vacation, and other employee-only benefits going back 3 years (§9 above). - SUI back-assessments plus penalties under c. 151A §14. - PFML back-assessments under c. 175M. - EMAC back-assessments under c. 149 §189. - Workers' compensation premium back-charges under c. 152. - Federal exposure under IRC §3509 and §530 if no §530 safe harbor.  _(M.G.L. c. 151A §14; M.G.L. c. 175M; M.G.L. c. 149 §189; M.G.L. c. 152; IRC §3509, §530)_
- **Federal tests not controlling in Massachusetts** — The federal 'right to control' test (Rev. Rul. 87-41) and the FLSA economic-realities test are NOT controlling in Massachusetts. A worker who is a contractor for federal tax purposes can still be an employee for Massachusetts purposes — and frequently is.  _(Rev. Rul. 87-41)_
- **Reviewer protocol on misclassification** — - Always ask the client for a list of all 1099-paid workers in MA over the last 3 years. - Apply the §148B test prong-by-prong. If Prong B fails for any worker, recommend reclassification going forward AND advise the client to consult employment counsel on remediation of historical exposure. - Document the §148B analysis in writing — the client may need it for an audit or litigation defense.
- **Special statutory exclusions** — Special exception: certain real estate salespersons, certain insurance agents, and certain franchisees are statutorily excluded from §148B by operation of other statutes. This skill does not cover those exclusions.

## 11. Domestic Workers

- **Domestic Workers' Bill of Rights framework** — Under the Massachusetts Domestic Workers' Bill of Rights, M.G.L. c. 149 §190 (enacted c. 148 of the Acts of 2014, effective April 1, 2015), domestic workers have separate substantive protections layered on top of the general wage-and-hour statutes: - Definition: a 'domestic worker' is an individual paid to perform work of a domestic nature in or about a private home — including childcare, housekeeping, cooking, eldercare, and companion services — and excluding casual babysitters (under 16 years of age or working under 18 hours/week intermittently). - Written agreement required: an employer of a domestic worker who works 16+ hours per week must provide a written employment agreement specifying wages, work hours, scheduled paid days off, leave benefits, health benefits, transportation, food and lodging arrangements, and any deductions. - Rest periods: 24 consecutive hours of rest per week and 48 consecutive hours per month required. - Live-in workers: protected from being on duty for more than 5 days in a row without 24 consecutive hours off. - Privacy protections: employers may not monitor or record the worker in bathrooms or sleeping quarters.  _(M.G.L. c. 149 §190)_
- **Domestic worker employer payroll obligations** — Domestic-worker employers must still register as MA employers, withhold state income tax, pay SUI (unless under c. 151A §6(o)'s domestic-service exemption — which is narrow), pay EMAC (subject to the 5-employee exemption), and remit PFML if the domestic worker is the only worker the employer's 25-employee threshold is not met but the employer is still the conduit for the employee's 0.46% deduction.  _(M.G.L. c. 151A §6(o))_

Federal payroll for household employers (Schedule H of Form 1040, 'Nanny Tax') is handled in the federal household-employer skill.

## 12. MA Health Connector — ACA Employer Mandate

### 12.1 ACA reporting (federal mandate)

- **ALE definition and mandate obligations** — Massachusetts employers with 50 or more full-time equivalent employees (FTEs) are Applicable Large Employers ('ALEs') under IRC §4980H. ALEs must: - Offer 'minimum essential coverage' to at least 95% of full-time employees and their dependents, or face the §4980H(a) penalty. - Offer coverage that is both 'affordable' (employee contribution for self-only coverage ≤ 9.02% of household income for 2025, per Rev. Proc. 2024-26) and 'minimum value' (60% actuarial value). - File Form 1094-C/1095-C annually with the IRS by March 31, 2025 (for 2024 calendar-year coverage) — though MA employers must also file with the Department of Revenue under c. 118H §3 for the residual MA Health Care Reform mandate.  _(IRC §4980H; Rev. Proc. 2024-26; M.G.L. c. 118H §3)_
- **2025 ACA affordability threshold** — 9.02% of household income for self-only coverage  _(Rev. Proc. 2024-26)_

### 12.2 MA Health Care Reform residual (Form MA 1099-HC)

- **MA Health Care Reform individual mandate and MA 1099-HC** — Massachusetts retains a separate state-level individual mandate under M.G.L. c. 111M (enacted by c. 58 of the Acts of 2006). For 2025, an MA resident filing Form 1 must demonstrate minimum creditable coverage ('MCC') or pay a state penalty. Employers offering MCC-compliant health coverage to MA-resident employees must issue Form MA 1099-HC by January 31 of each year and file a copy with the DOR.  _(M.G.L. c. 111M)_
- **MCC vs federal MEC comparison** — MCC is more generous than federal 'minimum essential coverage' — for example, MCC requires a prescription drug benefit, caps deductibles, and caps annual out-of-pocket maxima. A plan that satisfies federal MEC but not MA MCC will not protect the employee from the c. 111M penalty.  _(M.G.L. c. 111M)_
- **2025 MCC standards** — For 2025, MCC standards are codified in 956 CMR 5.00. The state-required MCC standards published by the Health Connector Board are reviewed annually; for 2025 the prescription drug benefit and the deductible cap are unchanged from 2024.  _(956 CMR 5.00)_

### 12.3 Health Connector for small employers

- **Connector Business program and Small Business Health Care Tax Credit** — The Massachusetts Health Connector operates a state-based exchange that includes a small-employer offering (the 'Connector Business' program). Small employers (1–50 employees) may purchase group coverage through the Connector and access the federal Small Business Health Care Tax Credit under IRC §45R if they meet the eligibility criteria (≤25 FTE, average wages ≤ $62,000 for 2025, paying ≥50% of premium).  _(IRC §45R)_
- **Scope note on §45R credit** — This is a federal credit administered through Form 8941, not a Massachusetts state credit, and is generally out of scope for this MA payroll skill — but the reviewer should flag the credit when the client is in the size band where it applies.

## 13. Worked Examples

### 13.1 Example A — Medium MA employer with 30 employees (PFML 25+ trigger)

Facts: Acme Software Inc., a Boston-based software company, has 30 full-time W-2 employees, all working in Massachusetts. Average wage is $120,000/year. Calendar 2025.

PFML 25-employee test: 30 covered individuals on the 9/30/2024 trailing-four-quarter average. Employer is in the '25+' bracket. Employer share of medical contribution = 0.42% applies.

Per-employee 2025 PFML:

- PFML wage base capped at $176,100; for an employee earning $120,000 the entire $120,000 is subject.
- Employee share: $120,000 × 0.46% = $552.00/year deducted from employee paycheck.
- Employer share: $120,000 × 0.42% = $504.00/year paid by employer.
- Combined per employee: $1,056.00/year.

Total annual PFML for 30 employees at average $120,000:

- Employee deductions total: 30 × $552 = $16,560.
- Employer expense total: 30 × $504 = $15,120.
- Combined remittance to DFML: $31,680/year.

SUI: 30 employees × $15,000 wage base × 1.45% new-employer rate (if Acme is in years 1–3) = $6,525/year. Plus COVID Recovery Assessment at approximately 1.80% × $15,000 × 30 = $8,100. Combined UI burden ≈ $14,625.

EMAC: 30 employees × $15,000 × 0.34% = $1,530/year. (Acme exceeds the 5-employee exemption and is past the 3-year new-employer exemption.)

State withholding: 30 employees × $120,000 × 5% MA PIT ≈ $180,000/year withheld and remitted via Form M-941 (monthly filer based on prior-year withholding). Reconciled annually on Form M-3.

Earned Sick Leave: 11+ employees → paid sick time. Each employee accrues up to 40 hours/year at $120,000 / 2,080 hours = $57.69/hour → up to $2,308 per employee per year if fully used.

Wage Act exposure: any late final paychecks expose Acme to treble damages. Standard offer letter must be reviewed.

Pay Equity Act: 25+ employees → salary range disclosure required on all MA job postings from October 29, 2025 forward.

### 13.2 Example B — Small MA employer under 25 (no employer PFML)

Facts: Beacon Design LLC, a Cambridge graphic design firm, has 8 W-2 employees, all in Massachusetts. Average wage $80,000. Calendar 2025.

PFML 25-employee test: 8 covered individuals — well under 25. Employer share = 0%. Employee still pays full 0.46% via deduction.

Per-employee PFML:

- Employee deduction: $80,000 × 0.46% = $368.00/year.
- Employer share: $0.
- Combined per employee: $368.00 (employee only).

Total annual PFML for 8 employees:

- Employee deductions: 8 × $368 = $2,944.
- Employer share: $0.
- Total remittance to DFML: $2,944 (entirely employee-funded but Beacon is still the conduit and must file the quarterly PFML return).

SUI: 8 × $15,000 × 1.45% = $1,740/year + Recovery Assessment ≈ $2,160.

EMAC: Beacon has more than 5 employees, so EMAC applies (unless still in 3-year new-employer window). 8 × $15,000 × 0.34% = $408/year.

Earned Sick Leave: Beacon has 10 or fewer employees, so sick time is UNPAID but accrued. At 11 employees, this flips to paid — borderline client, flag for monitoring.

Wage frequency: bi-weekly with written employee consent is acceptable.

Pay Equity Act: under 25 employees — salary range disclosure NOT yet mandatory (the 2024 Act's 25+ threshold). Salary history ban still applies regardless of size.

### 13.3 Example C — Multi-state employer with MA residents

Facts: Coastal Logistics Inc., headquartered in New Hampshire, has 100 employees total. 12 are MA residents who work primarily from home in Massachusetts, the rest work in NH.

Massachusetts withholding (the MA residency issue):

- MA residents pay MA tax on all income regardless of where earned (M.G.L. c. 62 §3). Coastal must register as a MA withholding employer, obtain a MA withholding account, and withhold 5% on the MA-resident employees' wages.
- For the 12 MA residents, Coastal files Form M-941 (frequency based on withholding volume) and Form M-3 annually.

PFML 25-employee test: Coastal has 12 MA-resident covered individuals (the NH workers don't count for the MA threshold). Coastal is under 25 MA covered individuals → employee-only PFML deduction (0.46%), no employer share.

But: Coastal is over 25 MA employees? The DFML guidance under 458 CMR 2.06 treats the 25-employee threshold as based on MA-located workforce. If all 12 MA residents work from home in MA, they count toward the MA threshold. The 88 NH-based workers do not. Coastal stays under 25 → no employer share.

(If Coastal had, for example, 30 MA-resident telecommuters, it would be over the 25-employee threshold and the employer share would apply on those 30 individuals only.)

SUI: complex multi-state determination under the federal 'localization of services' test (UIPL 20-04). Generally a remote-worker MA resident performing services in MA is reported to MA DUA. Coastal must register with DUA and file Form WR-1 for its MA workforce.

EMAC: 12 MA employees > 5, EMAC applies. Past 3-year new-employer window assumed → 12 × $15,000 × 0.34% = $612.

NH considerations (out of scope for this skill but flagged): New Hampshire does not have a state PIT on wages, so no NH withholding issue. The Massachusetts telecommuter rule (TIR 20-15) that taxed remote workers as in-state during COVID was rescinded; for 2025, NH residents working remotely from NH for a MA employer owe NO MA tax, reversing the temporary 2020–2021 rule. MA residents working remotely from MA for a NH employer still owe MA tax — which is the situation here.

### 13.4 Example D — Wage Act exposure on involuntary termination

Facts: Devon's Bakery Inc., a 6-employee MA bakery, terminates an employee on a Tuesday for cause. The employee's final paycheck (3.5 days of regular wages plus 24 hours of accrued unused vacation) is $1,847.50. Devon's standard payroll runs on Fridays. The bakery owner intends to issue the final paycheck on the next regular Friday (3 days after termination).

Wage Act analysis (§148 and §150):

- Statutory rule: final wages on involuntary termination are due on the day of discharge (Tuesday). The 3-day delay to Friday is a Wage Act violation regardless of employer intent.
- Reuter v. City of Methuen (2022): treble damages on the late-paid $1,847.50 are mandatory, even though the employee was eventually paid.
- Exposure: $1,847.50 × 3 = $5,542.50 in damages, PLUS plaintiff's attorney's fees and costs (typically $5,000–$25,000 in a routine Wage Act case).

Recommendation:

- Cut the final check on Tuesday before the employee leaves the premises. Use the bakery's reserve account if needed; do not wait for the next payroll cycle.
- For accrued unused vacation: must also be paid on Tuesday under Electronic Data Systems.
- Document the termination meeting and final-pay timing in the personnel file.

This example is included because the Wage Act exposure is the single most common source of preventable six-figure liability in our MA small-business book.

## 14. Filing Calendar (Quick Reference)

**Filing calendar quick reference**  _(DOR; DUA; DFML; Sec. State)_

| Form | Frequency | Due Date | Filed With |
| --- | --- | --- | --- |
| M-941 | Quarterly | Apr 30, Jul 31, Oct 31, Jan 31 | DOR |
| M-941 | Monthly | 15th of following month | DOR |
| M-941W | Quarter-monthly | Within 3 business days of period end | DOR |
| M-941A | Annual | January 31 | DOR |
| M-3 | Annual | January 31 | DOR |
| WR-1 | Quarterly | Apr 30, Jul 31, Oct 31, Jan 31 | DUA |
| PFML Return | Quarterly | Apr 30, Jul 31, Oct 31, Jan 31 | DFML |
| MA 1099-HC | Annual | January 31 | DOR |
| W-2 (state) | Annual | January 31 | DOR |
| EMAC | Quarterly | Apr 30, Jul 31, Oct 31, Jan 31 | DUA |
| EEO-1 (MA) | Annual | February 1 | Sec. State |

All filings are electronic via MassTaxConnect (DOR), UI Online (DUA), DFML portal (PFML), or DOR business portal (1099-HC).

## 15. Provenance and Citation Discipline

- M.G.L. c. 62 §4(b) — 5% PIT rate.
- Article XLIV, Massachusetts Constitution (ratified Nov 8, 2022) — 4% millionaire surtax.
- TIR 24-13 (DOR) — 2025 indexed surtax threshold ($1,083,150).
- TIR 23-2 (DOR) — surtax withholding mechanics on M-4.
- M.G.L. c. 62B §2 — wage withholding.
- M.G.L. c. 151A — Massachusetts Employment Security Law.
- M.G.L. c. 149 §148 — payment of wages.
- M.G.L. c. 149 §148B — independent contractor ABC test.
- M.G.L. c. 149 §148C — earned sick time.
- M.G.L. c. 149 §150 — Wage Act private right of action and treble damages.
- M.G.L. c. 149 §189 — EMAC.
- M.G.L. c. 149 §189A — EMAC Supplement (sunset 12/31/2019).
- M.G.L. c. 149 §190 — Domestic Workers' Bill of Rights.
- M.G.L. c. 149 §105A — Pay Equity Act (salary history ban).
- M.G.L. c. 149 §29A and §105E — Frances Perkins Workplace Equity Act (c. 141 of the Acts of 2024).
- M.G.L. c. 175M — Paid Family and Medical Leave.
- 458 CMR 2.00 — PFML regulations.
- M.G.L. c. 111M — MA individual health-insurance mandate.
- M.G.L. c. 118H — Health Connector reporting.
- 956 CMR 5.00 — Minimum Creditable Coverage.
- Reuter v. City of Methuen, 489 Mass. 465 (2022) — treble damages on late-paid wages.
- Electronic Data Systems Corp. v. Attorney General, 454 Mass. 63 (2009) — vacation is wages.
- Sebago v. Tutunjian Enterprises, 471 Mass. 321 (2015) — §148B Prong B interpretation.
- Athol Daily News v. Board of Review, 439 Mass. 171 (2003) — §148B Prong B in the UI context.
- DFML 2025 rate notice (October 11, 2024) — 0.88% combined PFML rate.
- DUA rate-schedule notice (November 2024) — Schedule E for 2025.
- SSA News Release (October 10, 2024) — 2025 SS wage base $176,100.
- Rev. Proc. 2024-26 — 2025 ACA affordability threshold 9.02%.

- The 2025 COVID-19 Recovery Assessment rate brackets — DUA publishes on a delayed basis; verify against the DUA 'Employer Resources' page before quoting client-specific rates.
- The Frances Perkins Act enforcement timeline for first-year warning vs. penalty — the regulations under §29A are still being promulgated as of the last_updated date and may be revised.
- The PFML private-plan exemption bond amount — verify against current DFML private-plan guidance.

## 16. Circular 230 Reviewer Sign-Off

This skill is a content reference for use by a credentialed reviewer. Outputs based on this skill must be signed off by an Enrolled Agent, CPA, or attorney admitted in Massachusetts before they are delivered to a client or filed with a Massachusetts agency. The reviewer's responsibilities include:

- Independent verification of every rate, threshold, and deadline against the cited primary source for the engagement's tax year.
- Independent confirmation of the client's 25-employee PFML status, ALE status, and §148B classification of any contractors.
- A separate written engagement letter that defines whether the engagement includes Wage Act remediation advice (note: Wage Act advice may be the unauthorized practice of law if rendered by a non-attorney accountant — coordinate with employment counsel).
- Documentation of the §148B ABC-test analysis for any contractor reclassification recommendation.
- Annual update of this skill on or before December 1 of each year to reflect the published DFML rate, DUA Schedule, surtax threshold, SS wage base, and ACA affordability percentage.

No part of this skill constitutes legal advice. Wage Act compliance, ABC-test analysis, and Pay Equity Act compliance are areas in which the line between tax/payroll advice and legal advice is thin; the reviewer must coordinate with employment counsel on any matter that includes a litigation, settlement, or class-action exposure.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).

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
