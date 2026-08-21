---
name: ca-payroll
description: Tier 2 California content skill for employer payroll compliance covering tax year 2025. Includes the 13.3% top PIT bracket with 1% mental health surtax over $1M, SDI 1.2% with no wage cap (SB 951), Form DE 9/DE 9C quarterly returns, the CalSavers retirement mandate for 1+ employees, AB5 / ABC test contractor classification, DE 542 reporting for $600+ contractors, supplemental wage withholding at 10.23%, ETT 0.1% on first $7,000, and SUI with $7,000 base and 1.5-6.2% experience-rated range. Covers federal payroll interactions and CA labor-code wage statement requirements.
jurisdiction: US-CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# CA Payroll

## 1. Scope

This skill covers California employer payroll compliance for the 2025 tax year, including:

- California Personal Income Tax (PIT) withholding administered by the Employment Development Department (EDD)
- State Disability Insurance (SDI) and Paid Family Leave (PFL) — bundled, employee-paid
- State Unemployment Insurance (SUI) — employer-paid, experience-rated
- Employment Training Tax (ETT) — employer-paid, on first $7,000
- Form DE 9 (Quarterly Contribution Return and Report of Wages) and Form DE 9C (Quarterly Contribution Return and Report of Wages — Continuation)
- Form DE 4 (Employee's Withholding Allowance Certificate) — California's W-4 equivalent
- DE 88 deposit coupons and e-Services for Business deposit cadence
- CalSavers retirement mandate (Government Code §100000 et seq.)
- AB5 / ABC test for independent contractor classification (Labor Code §2775 et seq., Dynamex Operations West, Inc. v. Superior Court, 4 Cal.5th 903 (2018))
- DE 542 (Report of Independent Contractor) for $600+ payments
- California wage-statement requirements (Labor Code §226)
- Final pay rules and waiting-time penalty (Labor Code §201-203)
- Workers' compensation overview
- Local tax overlays for San Francisco (Gross Receipts Tax, Payroll Expense Tax) and Los Angeles City Business Tax — referred out

**Out of scope (refuse or refer out):**

- Federal employment tax filing (Forms 941, 940, 943, 944, W-2/W-3 transmittal) — see `us-federal-payroll` (separate skill) or refer to credentialed payroll provider
- Multi-state nexus apportionment of payroll (employee working partly in another state) — refer to credentialed payroll professional
- Public-sector / governmental employer payroll (special rates, special funds)
- Agricultural employers under the Agricultural Labor Relations Act (separate rules)
- Tipped employee minimum-wage interaction with federal FLSA tip credit (CA does NOT allow a tip credit — refer-out for FLSA-CA interaction beyond the basic note in §13)
- Cannabis employer payroll (special licensure interaction)
- Garnishment and child-support withholding administration beyond noting the obligation exists
- ERISA-governed retirement plan administration (different from the CalSavers mandate, which is non-ERISA)
- H-1B / J-1 visa and totalization-agreement payroll edge cases
- Stock option §83(b) elections and §409A deferred compensation (refer to equity comp specialist)

**Prerequisites:** This skill MUST be loaded alongside `us-tax-workflow-base` v0.2 or later. It assumes a human reviewer credentialed under Circular 230 (EA, CPA, or attorney) or a CA-licensed payroll professional / SHRM-certified HR practitioner reviews and signs off every output before it reaches the employer or the EDD.

## 2. The Four California Employer Payroll Taxes (Quick Map)

**The Four California Employer Payroll Taxes (Quick Map)**  _(https://edd.ca.gov/en/payroll_taxes/rates_and_withholding/)_

| Tax | Who Pays | 2025 Rate | 2025 Wage Base | Notes |
| --- | --- | --- | --- | --- |
| **PIT (Personal Income Tax)** | Employee (withheld) | Per DE 4 / DE 44 tables; supplemental flat 10.23% for bonuses and stock options, 6.6% for other supplemental wages; top marginal 13.3% incl. MHST | No cap on wages subject; bracket-based | Mental Health Services Tax 1% over $1,000,000 |
| **SDI / PFL** | Employee (withheld) | 1.2% | **NO WAGE CAP** (SB 951 removed cap effective 2024 and continuing 2025) | Includes Paid Family Leave |
| **SUI (UI)** | Employer | New employer 3.4% for first 2-3 years; experience-rated 1.5%-6.2% thereafter | $7,000 per employee per year | UI Trust Fund; CA fund is currently in deficit and FUTA credit-reduction state in 2024 (carryover risk for 2025) |
| **ETT (Employment Training Tax)** | Employer | 0.1% (positive-reserve employers only; negative-reserve employers are exempt) | $7,000 per employee per year | Funds workforce training |

In addition, the employer must also withhold and remit federal taxes (FIT, FICA Social Security 6.2% to $176,100 in 2025, Medicare 1.45% + 0.9% additional, FUTA 6.0% with 5.4% credit on first $7,000) and observe federal Form 941 / 940 / W-2 obligations. Those are covered in `us-federal-payroll` (separate skill); this skill stays in the California lane.

**Key 2025 mnemonic:** "PIT and SDI come out of the employee's pocket; SUI and ETT come out of the employer's pocket." The two employer taxes share the same $7,000 wage base. SDI lost its cap in 2024 and remains uncapped in 2025.

### 3.1 Authority and Method

- **PIT withholding authority** — PIT withholding is governed by California Revenue and Taxation Code §18661 et seq. and Unemployment Insurance Code §13020. The EDD publishes the withholding method in Publication DE 44 (California Employer's Guide) and the bracket-and-table schedules in DE 44 Appendix.  _(R&TC §18661 et seq.; Unemployment Insurance Code §13020; DE 44)_
- **Withholding methods** — 1. Method A — Wage Bracket Tables (per DE 44). Suitable for most pay periods. 2. Method B — Exact Calculation Method (per DE 44). Required when wages exceed the top wage-bracket entry. Most payroll software uses Method B. 3. Supplemental wage withholding: 10.23% for bonuses and stock options; 6.6% for other supplemental wages (commissions, overtime paid separately, sales awards, severance, vacation pay), unless aggregated with regular wages under DE 44.  _([DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44-25.pdf))_

### 3.2 2025 California PIT Brackets

The 2025 California marginal brackets (single filer; MFJ doubles most thresholds; head of household intermediate) used for withholding tabulation:

**2025 California PIT Brackets (Single Filer)**

| Single Bracket (Taxable Income) | Marginal Rate |
| --- | --- |
| $0 — $11,079 | 1.0% |
| $11,080 — $26,264 | 2.0% |
| $26,265 — $41,452 | 4.0% |
| $41,453 — $57,542 | 6.0% |
| $57,543 — $72,724 | 8.0% |
| $72,725 — $371,479 | 9.3% |
| $371,480 — $445,771 | 10.3% |
| $445,772 — $742,953 | 11.3% |
| $742,954 — $1,000,000 | 12.3% |
| Over $1,000,000 | 12.3% + 1.0% MHST = **13.3%** |

- **Mental Health Services Tax (MHST)** — The Mental Health Services Tax (MHST) under R&TC §17043 applies a flat 1% surtax on taxable income exceeding $1 million. Withholding tables build this into the top wage brackets, but for executive compensation and equity events the supplemental withholding mechanic generally undercollects, leaving the employee with a Form 540 balance due. AUDIT FLASH POINT — see §3.5.  _(R&TC §17043)_

Bracket figures above reflect FTB inflation indexing publicly available as of the skill's last_updated date. If your client engagement falls in a window where the FTB has released updated indexed brackets and the EDD has issued a revised DE 44 Appendix, refresh and disclose the figures used.

### 3.3 Form DE 4 — Employee Withholding Allowance Certificate

- **Form DE 4** — Form DE 4 is California's analogue to federal Form W-4. It is REQUIRED in addition to (not instead of) the federal W-4 when: the employee claims a different number of California allowances than federal allowances; the employee is exempt from California withholding but not federal (or vice versa); the employee wants additional CA withholding withheld; the employee is a nonresident performing services in California (special rules; refer-out for nonresident apportionment).
- **Default when no DE 4 on file / retention / FTB copy requirement** — If no DE 4 is on file, the employer defaults to the filing status and allowances on the federal W-4 (with adjustments per DE 44 Section B). A common error is treating the post-2020 federal W-4 (which eliminated personal allowances) as zero CA allowances — the EDD instructs employers to use the DE 4 filing-status and allowance structure independently, so a DE 4 is now effectively required for any employee who wants accurate CA withholding. The DE 4 is retained by the employer (not submitted to EDD) but must be available on request. If withholding allowances exceed 10, the employer should send a copy of the DE 4 to the Franchise Tax Board within 20 days under R&TC §18664.  _(R&TC §18664; DE 44 Section B)_

### 3.4 Supplemental Wage Withholding — 10.23%

- **Supplemental wage withholding rates 2025** — Use 10.23% for bonuses and stock options; use 6.6% for other supplemental wages such as commissions, separately paid overtime, sales awards, severance, and vacation pay. If supplemental wages are paid with regular wages, DE 44 permits aggregate withholding under Method A/B.  _([DE 44 (current)](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44-25.pdf))_
- **Supplemental wages definition** — Supplemental wages are wages paid in addition to regular wages and include bonuses, commissions, overtime when paid separately, severance, accumulated PTO payouts, retroactive pay, and most equity compensation events (RSU vesting, NQSO exercise spread, ESPP disqualifying disposition).

EDD DE 44 for 2025 still distinguishes supplemental wage categories: bonuses and stock options use 10.23%; other supplemental wages (commissions, overtime paid separately, sales awards, severance, and vacation pay) use 6.6%. Confirm against the current DE 44 before filing because EDD updates the guide annually.

- **Concurrent vs separate supplemental payments** — For supplemental wages paid concurrently with regular wages, the employer may aggregate the supplemental wages with the regular paycheck and compute total withholding under Method A/B. If using the flat-rate method for a separate supplemental payment, apply the DE 44 category rate: 10.23% for bonuses and stock options; 6.6% for other supplemental wages such as commissions, separately paid overtime, sales awards, severance, and vacation pay.  _(https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44-25.pdf)_

### 3.5 AUDIT FLASH POINT — Equity Compensation Undercollection at the Top Marginal Rate

The 10.23% supplemental rate is materially below the 13.3% top marginal rate (12.3% + 1% MHST). High-income employees with significant RSU vesting, NQSO exercise, or large bonuses systematically end the year with insufficient withholding and owe a substantial Form 540 balance plus possibly a Form 5805 underpayment penalty.

**Red flags during payroll review:**
- Tech employees with annual gross compensation > $360,659 (10.3% bracket and up) receiving large RSU vests at 10.23% supplemental
- Executives with cash bonuses > $1,000,000 (MHST kicks in at 13.3% effective) withheld at 10.23%
- Annual W-2 Box 1 wages comparable to Box 16 (state wages) but CA withholding < 10.5% of Box 16 — likely under-withholding indicator

**Mitigation:**
- Employee files DE 4 requesting additional flat-dollar withholding per pay period
- Employer offers a "supplemental withholding election" allowing employees to elect a higher voluntary withholding on supplemental wages (some payroll platforms support this)
- Employee makes a Q4 estimated payment on Form 540-ES — refer to `ca-540-es-estimated-tax` skill for safe-harbor analysis

This is one of the most common findings in California tax-return preparation and a legitimate audit/inquiry point with EDD when the FTB cross-matches W-2 Box 17 to Form 540 line 71.

### 3.6 Wages Subject to California Withholding

- **CA wage differences from federal Box 1** — California wages generally mirror federal Box 1 wages but with three notable differences: 1. HSA contributions — California does not conform to the federal exclusion. Employer and employee HSA contributions are taxable for CA PIT, SDI, SUI, and ETT and must be added back. CA wages = federal wages + HSA contributions. 2. Same-sex spouse health benefits — fully conformed since federal recognition, no longer an adjustment. 3. Domestic partner health benefits — California conforms to non-taxation for registered domestic partners; federal still taxes the imputed value. This makes CA wages LOWER than federal wages. 4. §125 cafeteria plan elections — generally conformed; no adjustment.

Verify the CA wage base independently — payroll software occasionally misses the HSA add-back, leading to under-withholding and an underreporting of SDI.

### 4.1 SDI — Cap Removal Under SB 951

- **SB 951 cap removal** — Senate Bill 951 (Chapter 878, Statutes of 2022) eliminated the SDI taxable wage cap effective January 1, 2024, and the cap remains removed for 2025.  _(SB 951 (Chapter 878, Statutes of 2022))_
- **2025 SDI mechanics** — Rate: 1.2% of gross wages; Wage cap: None (uncapped); Paid by: Employee only (employer withholds and remits); Remitted on: Form DE 9 / DE 9C, alongside PIT; Reported on: Form W-2 Box 14 ("CA SDI") percent  _(https://edd.ca.gov/en/payroll_taxes/rates_and_withholding/)_

Prior to 2024, SDI had a wage cap ($153,164 in 2023 at a 0.9% rate, capping employee SDI at ~$1,378/year). With the cap removed and the 2025 rate at 1.2%, a Silicon Valley executive earning $5 million pays $60,000 in SDI for 2025 (vs ~$1,378 under pre-2024 rules). This is a 40× increase for top earners and is the largest CA payroll cost shift in a generation.

### 4.2 PFL — Bundled Into SDI

- **PFL bundled into SDI** — Paid Family Leave is administratively bundled into SDI. The same 1.2% withholding funds both the SDI benefit (own disability, including pregnancy) and the PFL benefit (bonding with new child, caring for seriously ill family member, qualifying military exigency).  _(https://edd.ca.gov/en/payroll_taxes/rates_and_withholding/)_
- **2025 PFL benefit** — Up to 8 weeks of partial wage replacement, capped at approximately $1,681 per week maximum (the benefit cap is set as a function of statewide average weekly wage; 60-70% wage replacement subject to the cap). SB 951 also increased the wage-replacement percentage for lower-wage workers up to 90% effective 2025.  _(SB 951)_

The employer's payroll obligation is identical for SDI and PFL — there is no separate withholding. Employees apply for benefits directly through EDD; the employer's role at claim time is verifying employment and reporting the last day worked.

### 4.3 AUDIT FLASH POINT — SDI Removed-Cap Mid-Year Reconciliation

For payroll systems that were not properly reconfigured when the cap was removed, the typical failure mode is:

- Payroll software continued to apply the 2023 cap ($153,164) or some other stale cap into 2024 and 2025
- High earners were under-withheld for SDI
- The employer's DE 9/DE 9C for Q1-Q4 2024 understated SDI liability
- Form W-2 Box 14 reports an SDI figure smaller than 1.2% of Box 16 CA wages

**Reconciliation procedure:**
1. Pull Box 14 (CA SDI) and Box 16 (CA wages) from all 2024 and 2025 W-2s
2. Compute expected SDI = 1.2% × Box 16
3. Difference > $5 per employee is a flag
4. Employer must issue corrected W-2c, file amended DE 9X (DE 9 amended return), and collect the under-withheld SDI from the employee per Labor Code §221 (employer cannot absorb the SDI — it is the employee's tax)
5. EDD interest applies on the underpayment

This was the most common payroll-software error in 2024 and continues to surface in 2025 prior-period audits.

### 4.4 Voluntary Plan Alternative

- **Voluntary Plan (VP)** — Employers may opt out of state SDI and offer a Voluntary Plan (VP) approved by EDD under Unemployment Insurance Code §3251 et seq. The VP must provide benefits at least as generous as state SDI, must be approved by majority employee vote, and is subject to ongoing EDD oversight. Adoption is rare among SMBs because of administrative burden; large employers and certain industries use VPs.  _(Unemployment Insurance Code §3251 et seq.)_

### 5.1 Mechanics

- **SUI mechanics 2025** — SUI is paid entirely by the employer (no employee withholding) and is experience-rated based on the employer's history of unemployment-benefit charges. **2025 SUI structure:** - Wage base: $7,000 per employee per calendar year - New employer rate: 3.4% for the first 2-3 calendar years (transferred to experience-rated schedule thereafter) - Experience-rated range: 1.5% (best rating) to 6.2% (worst rating) in 2025 - Schedule: EDD publishes annual contribution rate schedules; the F+ schedule has been in effect because the UI trust fund is in deficit - Maximum SUI per employee per year (new employer): $7,000 × 3.4% = $238 - Maximum SUI per employee per year (worst experience rating): $7,000 × 6.2% = $434
- **Notice of Contribution Rate** — The employer receives a Notice of Contribution Rate (Form DE 2088) from EDD each December showing the rate for the following calendar year. Adjustments to the rate must be appealed within 60 days.  _(Form DE 2088)_

### 5.2 FUTA Credit Reduction Interaction

- **FUTA credit reduction** — When the UI trust fund borrows from the federal government and fails to repay within statutory windows, California becomes a FUTA credit-reduction state. For 2023 and 2024 California was a credit-reduction state, and the trajectory suggests this may continue for 2025 (verify against the IRS / Department of Labor announcement in November 2025 for 2025 Form 940). When CA is a credit-reduction state, the federal FUTA effective rate increases above the normal 0.6% by 0.3% per year of credit reduction. This is a federal cost increase (Form 940) but is a direct consequence of California UI policy and should be flagged to the employer during budgeting.

### 5.3 Voluntary UI Contribution

- **Voluntary UI contribution buy-down** — Under Unemployment Insurance Code §976.5, an employer may make a voluntary contribution by March 31 to "buy down" the experience rating for the next year. This is only beneficial when (a) the employer's experience rating is high and (b) the projected wages multiplied by the rate reduction exceed the voluntary contribution. Worth modeling for medium-sized employers (50+ employees) with deteriorating experience ratings.  _(Unemployment Insurance Code §976.5)_

## 6. Employment Training Tax (ETT)

- **ETT rate and structure** — Rate: 0.1% on the first $7,000 of wages per employee. Max per employee per year: $7. Applies only to employers with a positive reserve account balance (i.e., the employer has paid more in SUI than has been charged in benefits). Negative-reserve employers are exempt from ETT. Purpose: Funds the Employment Training Panel (ETP) which subsidizes worker training programs. percent

ETT is reported on the same Form DE 9 as SUI and PIT. New employers are positive-reserve by default and so pay ETT in their first years.

### 7.1 Form DE 9 — Quarterly Contribution Return and Report of Wages

- **DE 9 contents** — Form DE 9 is the summary quarterly return. It reports: Total subject wages, PIT wages, UI taxable wages, and SDI taxable wages; UI contributions due (employer); ETT due (employer); SDI withheld (employee); PIT withheld (employee); Total contributions and withholdings due; Payments already made via DE 88 deposits; Balance due or overpayment.

### 7.2 Form DE 9C — Quarterly Contribution Return and Report of Wages (Continuation)

- **DE 9C contents** — Form DE 9C is the detail schedule that accompanies DE 9. It reports for each employee: SSN, full legal name; Total subject wages paid in the quarter; PIT wages; PIT withheld; Pay period weeks (for SDI benefit-eligibility tracking).

The DE 9C is the EDD's primary cross-match source — the FTB uses it to verify Form 540 wage reporting and the EDD uses it to determine unemployment benefit eligibility. Errors on DE 9C are surfaced years later when an employee files an unemployment claim, so accuracy matters.

### 7.3 Due Dates

**DE 9 / DE 9C Due Dates**

| Quarter | Period | Due Date |
| --- | --- | --- |
| Q1 | Jan-Mar | April 30 |
| Q2 | Apr-Jun | July 31 |
| Q3 | Jul-Sep | October 31 |
| Q4 | Oct-Dec | January 31 of following year |

- **Weekend/holiday rule** — When the due date falls on a weekend or California state holiday, the next business day applies.

### 7.4 Filing Method

- **e-Services for Business filing** — DE 9 and DE 9C must be filed electronically via e-Services for Business (EDD's online portal) for any employer required to file. Paper filings are accepted only with prior EDD waiver (rare).

### 7.5 Q4 DE 9 as Annual Reconciliation

- **Annual reconciliation** — The Q4 DE 9 doubles as the annual reconciliation — it must reconcile annual subject wages, PIT withheld, SDI withheld, UI taxable, etc., to the figures that will appear on Form W-2 Box 16 (state wages) and Box 17 (state withholding). Any discrepancy between cumulative DE 9C and W-2 totals is the most common EDD desk-audit trigger.

## 8. Deposit Cadence — DE 88 / E-Services

PIT withholding and SDI must be deposited on a cadence that matches the employer's federal deposit schedule and CA-specific PIT thresholds.

**California PIT deposit thresholds (2025):**

**California PIT deposit thresholds (2025)**

| If PIT withheld in pay period is... | Deposit schedule |
| --- | --- |
| < $500 in a quarter | Deposit with quarterly DE 9 (no separate DE 88 needed) |
| ≥ $500 in a quarter but federal schedule is monthly | Monthly deposit, due 15th of following month |
| Federal "next-day" deposit ($100,000+ in a single day) | Next business day |
| Federal semi-weekly | Semi-weekly (Wed-Fri payday → following Wednesday; Sat-Tue payday → following Friday) |

- **DE 88 mechanics and SUI/ETT cadence** — The CA deposit is made via DE 88 coupon (electronic only — paper DE 88 was sunset) through e-Services for Business. SUI and ETT are deposited with the quarterly DE 9 — not on the monthly/semi-weekly cadence. This often confuses payroll staff who expect SUI to follow federal FUTA cadence.

### 8.1 Penalties for Late Deposits

- **CA deposit penalties** — CA deposit penalties under R&TC §19170 et seq.: 15% of underpayment if not deposited timely (harsher than the federal 2%-15% graduated schedule); plus interest at the FTB rate (3-5% annualized, adjusted semi-annually); plus the 10% / 25% / 50% penalties for negligent or fraudulent failure under R&TC §19133. CA penalties are materially harsher than federal penalties; do not assume timely federal deposits satisfy CA.  _(R&TC §19170 et seq.; R&TC §19133)_

### 9.1 Statutory Authority

- **CalSavers statutory authority** — CalSavers is governed by California Government Code §100000 et seq. and is administered by the CalSavers Retirement Savings Board. It is a Roth IRA-based payroll-deduction program for employees of employers that do not offer a qualified employer-sponsored retirement plan.  _(Government Code §100000 et seq.)_

### 9.2 Mandate — 1+ Employee Threshold

- **CalSavers 1+ employee mandate** — Effective December 31, 2025, every California employer with one (1) or more employees that does NOT offer a qualified retirement plan (401(k), 403(b), SEP-IRA, SIMPLE IRA, etc.) must register with CalSavers and facilitate payroll deductions for employees who do not opt out.  _(SB 1126 (Chapter 681, Statutes of 2022))_

**CalSavers Phased Thresholds (now superseded)**

| Phase | Employees | Original Deadline |
| --- | --- | --- |
| Phase 1 | 100+ | June 30, 2020 |
| Phase 2 | 50+ | June 30, 2021 |
| Phase 3 | 5+ | June 30, 2022 |
| Phase 4 (SB 1126, 2022) | 1+ | December 31, 2025 |

- **SB 1126 expansion and exemptions** — SB 1126 (Chapter 681, Statutes of 2022) expanded the mandate to all employers with at least one employee, effective December 31, 2025. Self-employed individuals without employees and sole proprietors who are the only person on payroll are exempt from the mandate but may still enroll voluntarily.  _(SB 1126 (Chapter 681, Statutes of 2022))_

### 9.3 Employer Obligations

- **Employer obligations under CalSavers** — 1. Register with CalSavers within the deadline (existing employer with 1-4 employees must register by Dec 31, 2025) 2. Submit employee census (name, DOB, SSN, contact info) within 30 days of hire 3. Facilitate payroll deductions at the default 5% rate (auto-escalating 1% per year to 8% max) unless the employee opts out or selects a different rate 4. Remit contributions to CalSavers via the portal each pay period 5. Do NOT make matching contributions (CalSavers is employee-only by design; employer matches are prohibited because that would convert it into an ERISA plan, which CalSavers is structured to avoid) 6. Do NOT provide investment advice (the employer's role is strictly clerical)

### 9.4 AUDIT FLASH POINT — CalSavers Mandate Enforcement

- **CalSavers penalties** — CalSavers enforces compliance through the Franchise Tax Board, with penalties under Government Code §100033: $250 per eligible employee if non-compliant 90+ days after notice; Additional $500 per eligible employee if non-compliant 180+ days after notice; Total potential penalty: $750 per employee.  _(Government Code §100033)_

For a 5-employee shop that ignores the mandate, exposure is $3,750. For a 50-employee shop, $37,500. Enforcement letters began arriving in 2023 and have accelerated. The mandate is not optional and there is no de minimis exception below the 1+ threshold.

**Compliance check during engagement:**
1. Confirm whether employer offers a qualified plan (401(k), SEP, SIMPLE, defined benefit, etc.). If yes, file the CalSavers "Exemption" attestation in the portal.
2. If no qualified plan, confirm CalSavers registration and active facilitation.
3. Review payroll register for the CalSavers deduction line.
4. If neither plan nor CalSavers, the employer is non-compliant. Recommend immediate registration to mitigate penalty exposure.

### 10.1 Statutory Authority

- **AB5 statutory authority** — Labor Code §2775 et seq., enacted by Assembly Bill 5 (Chapter 296, Statutes of 2019) and amended by AB 2257 (Chapter 38, Statutes of 2020), codified the ABC test from the California Supreme Court's decision in Dynamex Operations West, Inc. v. Superior Court, 4 Cal.5th 903 (2018).  _(Labor Code §2775 et seq.; AB 5 (Chapter 296, Statutes of 2019); AB 2257 (Chapter 38, Statutes of 2020); Dynamex Operations West, Inc. v. Superior Court, 4 Cal.5th 903 (2018))_

### 10.2 The ABC Test

- **ABC test prongs** — A worker is presumed to be an employee unless the hiring entity proves ALL THREE of the following: (A) The worker is free from the control and direction of the hiring entity in connection with the performance of the work, both under the contract and in fact; (B) The worker performs work that is outside the usual course of the hiring entity's business; (C) The worker is customarily engaged in an independently established trade, occupation, or business of the same nature as the work performed. If ANY prong fails, the worker is an employee for purposes of the Labor Code, Unemployment Insurance Code, and the wage orders.

The bar is materially higher than the federal common-law (Borello) test and substantially harder to satisfy than the IRS 20-factor test. A worker who is a federal 1099 contractor under federal common-law analysis can still fail the ABC test in California and be reclassified as an employee.

### 10.3 Statutory Exemptions

- **AB5 / AB 2257 exemptions reverting to Borello test** — AB 5 / AB 2257 carve out specific occupations and business-to-business relationships that revert to the older Borello test (a multi-factor common-law analysis) rather than the ABC test. Major exemptions include: Licensed professionals: physicians, dentists, lawyers, architects, engineers, accountants (CPAs), private investigators, securities broker-dealers, investment advisers; Direct sales salespersons; Commercial fisherman; Real estate licensees, repossession agents; Construction subcontractors (with specific business-license and contract requirements); Referral agencies for licensed services (graphic design, photography, tutoring, etc., subject to detailed compliance criteria); Business-to-business contractors meeting all 12 criteria in §2776 (separate business location, separate business license, advertising, etc.); Freelance writers, photographers, content contributors meeting specific submission-count and contract conditions; Single-engagement contractors meeting §2778 criteria.  _(Labor Code §2776; Labor Code §2778)_

Practical impact on freelance software developers: Software development engagements are NOT among the statutory exemptions. A freelance software developer who works exclusively for one client over many months and whose work product is the client's core product (e.g., building the client's primary SaaS application) likely fails prong (B) and is an employee under the ABC test. A freelance developer building a marketing website for a non-tech company likely passes prong (B). The B2B exemption under §2776 may apply if all 12 criteria are met (S-corp or LLC structure, separate business license, separate workspace, multiple clients, etc.).

### 10.4 AUDIT FLASH POINT — AB5 Misclassification Disputes

- **Misclassification consequences** — Misclassification is the single highest-stakes California payroll exposure. Consequences: EDD reclassification of contractor payments as employee wages → back SUI, ETT, SDI, and PIT withholding for up to 3 years (sometimes longer with fraud allegations); Unpaid wages claims under Labor Code §1194 (minimum wage), §510 (overtime), §226.7 (meal/rest breaks), §226 (wage-statement violations) — recoverable for 3 years (4 with UCL claim); PAGA penalties under Labor Code §2698 et seq. — $100 per pay period per aggrieved employee, then $200 for subsequent violations, with 75% to LWDA and 25% to the employees, and a private right of action; Workers' comp gap — the misclassified worker who is injured can claim against the employer despite no policy, exposing the employer to direct liability under Labor Code §3700; Federal exposure — IRS §530 relief is unavailable if the misclassification is willful; Form SS-8 determination can also reclassify federally.  _(Labor Code §1194; §510; §226.7; §226; §2698 et seq.; §3700)_
- **Risk-management protocol** — 1. Document the ABC analysis in writing for every 1099 contractor before engagement 2. Confirm the contractor has a separate business license, EIN, separate workspace, and other indicia of an independently established business 3. Use a written contract that recites the ABC factors and the contractor's independent-business status 4. Require the contractor to provide proof of business insurance, workers' comp coverage (if they have employees), and a current business license 5. If any prong is doubtful, treat the worker as an employee — the cost of reclassification dwarfs the cost of withholding

## 11. DE 542 — Independent Contractor Reporting

- **DE 542 reporting requirement** — Under Unemployment Insurance Code §1088.8, an employer (referred to in the statute as a "service-recipient") must report any independent contractor to whom payments of $600 or more in a calendar year are made.  _(Unemployment Insurance Code §1088.8)_

### 11.1 Mechanics

- **DE 542 mechanics** — Form: DE 542 (Report of Independent Contractor(s)). Threshold: $600 in cumulative payments in a calendar year, OR a contract with a value of $600 or more (whichever occurs first). Due: Within 20 days of EITHER the contract being executed OR the $600 cumulative payment threshold being reached. Information required: Service-recipient's name, address, FEIN, and CA employer account number; service-provider's name, SSN or FEIN, address; contract amount; contract start date; whether the contract is ongoing. Filing method: Electronically via e-Services for Business; paper DE 542 still accepted via mail or fax.

### 11.2 Purpose

- **DE 542 purpose and penalties** — DE 542 reporting feeds the California New Hire Reporting system, which the EDD shares with state agencies for child-support enforcement (Family Code §17506.5). It is NOT a tax document — the contractor pays their own taxes on Schedule C — but failure to file exposes the employer to penalties of $24 per failure, or $490 per failure for collusion to defeat child-support orders (Unemployment Insurance Code §1088.8(c)).  _(Family Code §17506.5; Unemployment Insurance Code §1088.8(c))_

### 11.3 Interaction with Federal 1099-NEC

- **DE 542 vs federal 1099-NEC** — DE 542 is a California-only report, separate from federal Form 1099-NEC. Both are required for contractor payments of $600 or more (or $2,000 starting in 2026 per OBBBA — note federal threshold change but California has not conformed; CA DE 542 remains at $600). See `us-1099-nec-issuance` for federal mechanics.

## 12. Wage Statement Requirements — Labor Code §226

- **Nine required itemized wage statement items** — California has the most prescriptive itemized-pay-stub requirement in the United States. Labor Code §226(a) requires the employer to provide an itemized wage statement EITHER as a detachable part of the paycheck or as a separate document, containing nine specific items: 1. Gross wages earned 2. Total hours worked (for non-exempt employees only) 3. The number of piece-rate units earned and the applicable piece rate (if paid on piece rate) 4. All deductions (in detail, not aggregated) 5. Net wages earned 6. The inclusive dates of the period for which the employee is paid 7. The name of the employee and the last four digits of the SSN or an employee ID number 8. The name and address of the legal entity that is the employer 9. All applicable hourly rates in effect during the pay period and the corresponding number of hours worked at each rate Additional itemization items required for piece-rate workers under §226.2, and for non-exempt salaried employees (regular rate of pay calculation for sick pay and overtime).  _(Labor Code §226(a); §226.2)_

### 12.1 §226(e) Penalties

- **§226(e) penalty structure** — Failure to provide a compliant wage statement exposes the employer to: Actual damages or, if greater, a penalty of $50 for the initial violation per employee and $100 per subsequent violation per employee, per pay period, up to an aggregate of $4,000 per employee; Costs and attorney's fees to a prevailing employee under §226(h); PAGA penalties under Labor Code §2699 ($100 / $200 per pay period per aggrieved employee, plus a 25% / 75% split with LWDA).  _(Labor Code §226(e); §226(h); §2699)_

Common §226 failures:
- Missing the last four digits of the SSN (or using full SSN — equally a violation)
- Missing the legal entity name (e.g., showing the DBA but not the LLC)
- Aggregating deductions instead of itemizing
- Missing the pay-period dates
- Missing the regular rate of pay for non-exempt employees

The legal name on the wage statement must exactly match the legal name on the IRS EIN registration and the CA Secretary of State filing. A DBA-only wage statement is a §226 violation per Cicairos v. Summit Logistics, Inc., 133 Cal.App.4th 949 (2005) and its progeny.

### 13.1 Timing of Final Wages

- **Final wage timing rules** — Labor Code §201-203 governs the timing of final wages: Involuntary termination (fired or laid off): Final wages, including all accrued unused vacation/PTO, are due IMMEDIATELY at the time of discharge (§201); Voluntary resignation with at least 72 hours' notice: Final wages due on the last day worked (§202); Voluntary resignation without 72 hours' notice: Final wages due within 72 hours of resignation (§202).  _(Labor Code §201; §202; §203)_

"Immediately" means at the moment of discharge — the employer must have the final paycheck (with all earned wages plus accrued PTO) ready to hand the employee when delivering the termination news. For practical scheduling, payroll teams often run a manual off-cycle check the day before.

### 13.2 PTO and Vacation Payout

- **PTO vesting and payout rules** — California is a "use-it-or-don't-lose-it" state per Suastez v. Plastic Dress-Up Co., 31 Cal.3d 774 (1982). Accrued vacation/PTO is vested wages and must be paid out at the final rate of pay at termination. Cap on accrual is permitted (per Boothby v. Atlas Mechanical, Inc., 6 Cal.App.4th 1595 (1992)) but forfeiture of accrued PTO is not.  _(Suastez v. Plastic Dress-Up Co., 31 Cal.3d 774 (1982); Boothby v. Atlas Mechanical, Inc., 6 Cal.App.4th 1595 (1992))_
- **Sick leave payout treatment** — Sick leave under the Healthy Workplaces, Healthy Families Act of 2014 (Labor Code §245 et seq.) is NOT required to be paid out at termination, but if the employer maintains a combined PTO policy (vacation + sick in one bucket), the entire bucket is treated as vested and must be paid out.  _(Labor Code §245 et seq.)_

### 13.3 AUDIT FLASH POINT — Waiting-Time Penalty Under §203

- **Waiting-time penalty structure** — If the employer willfully fails to pay final wages on time, Labor Code §203 imposes a waiting-time penalty equal to one day of wages at the employee's regular rate for each day the wages remain unpaid, up to a maximum of 30 days. **Critical features:** - The penalty runs at the employee's full daily rate, not the unpaid balance. An employee earning $1,000/day with $50 of unpaid wages owed still triggers up to $30,000 in waiting-time penalties. - "Willful" is broadly construed under Mamika v. Barca, 68 Cal.App.4th 487 (1998) — even a good-faith mistake can be deemed willful if there was no genuine legal dispute about the obligation to pay. - Penalty is recoverable for up to 3 years under §203(b); the worker need not file a labor commissioner claim within 30 days. - Section 203 penalties are NOT wages for tax purposes — they are penalties, reported on Form 1099-MISC Box 3 (Other Income), not Form W-2.  _(Labor Code §203; §203(b); Mamika v. Barca, 68 Cal.App.4th 487 (1998))_
- **Mitigation** — Process final paychecks for terminations BEFORE delivering the termination news. Confirm all PTO, commissions, bonuses earned (per Labor Code §200 definition of wages and Schachter v. Citigroup, Inc., 47 Cal.4th 610 (2009) on vested but unpaid bonuses), and any expense reimbursements (§2802) are included. Use direct deposit only if the employee has previously consented per Labor Code §213(d) — otherwise the final check must be a physical paycheck.  _(Labor Code §200; Schachter v. Citigroup, Inc., 47 Cal.4th 610 (2009); Labor Code §2802; §213(d))_

### 13.4 Tipped Workers Note (Brief)

- **No tip credit in California** — California does NOT permit a tip credit under Labor Code §351. Tipped employees must be paid at least the full state minimum wage (or higher local minimum) plus tips. Tips are not wages for minimum-wage purposes but ARE wages for PIT/SDI withholding when reported (Form 4070 / Form 4137 federal mechanic; California conforms via DE 44 instructions). See worked example §15.2 for a retail-tip walkthrough.  _(Labor Code §351)_

### 14.1 Workers' Compensation — Mandatory

- **Workers' comp mandatory coverage** — Labor Code §3700 makes workers' compensation insurance mandatory for every California employer of at least one employee. Coverage is via: A private workers' comp carrier (rates set by class code per the Workers' Compensation Insurance Rating Bureau (WCIRB)); State Compensation Insurance Fund (SCIF) — the insurer of last resort; Self-insurance (only for very large employers with regulatory approval).  _(Labor Code §3700)_
- **Penalties for failure to carry workers' comp** — Failure to carry workers' comp is a misdemeanor under §3700.5 with criminal penalties up to $10,000 and one year imprisonment, plus a $1,500 administrative penalty per employee per day uninsured, plus direct liability for any injured worker's benefits and damages.  _(Labor Code §3700.5)_

Class-code rates vary enormously: a clerical employee (class 8810) might be 0.30% of payroll, a roofer (class 5552) might be 25%+ of payroll. WCIRB publishes the pure-premium rates; carriers apply experience modifications and underwriting discounts on top.

**Practical:** Verify the employer has an active workers' comp policy that covers all California employees, including remote employees working from home (California has expansive workers' comp coverage for telecommuting injuries).

### 14.2 Local Taxes — San Francisco

- **San Francisco local taxes** — San Francisco imposes separate local business taxes that overlay state payroll obligations. The principal taxes are: Gross Receipts Tax (GRT) — Business and Tax Regulations Code Article 12-A-1; rates by industry sector, ranging roughly 0.075% to 1.0%+; applies to businesses with SF nexus and SF-attributable gross receipts above thresholds; Homelessness Gross Receipts Tax — Article 28; surcharge on certain large businesses; Commercial Rents Tax — Article 21; Payroll Expense Tax — historically 0.38%; has been substantially phased out and replaced by GRT but residual obligations remain for certain large employers. SF payroll filing: Annual Business Registration Renewal and Statement of Information; quarterly estimated tax payments for businesses above thresholds; annual Business Tax Return (formerly Form P-2).  _(Business and Tax Regulations Code Article 12-A-1; Article 28; Article 21)_

This skill REFERS OUT to SF Office of the Treasurer & Tax Collector and a credentialed SF tax practitioner for SF-specific compliance. The interactions between SF GRT, SF Payroll Expense Tax (residual), and state payroll are complex and beyond the Tier 2 scope.

### 14.3 Local Taxes — Los Angeles

- **LA City Business Tax** — LA City imposes a Business Tax (Los Angeles Municipal Code §21.00 et seq.) on businesses with LA city operations. Rates vary by classification and are filed annually with the Office of Finance. Many small businesses qualify for the LA small-business exemption (gross receipts under $100,000) but must still file a Statement of Information to claim it.  _(Los Angeles Municipal Code §21.00 et seq.)_

This skill REFERS OUT to LA Office of Finance and a credentialed LA tax practitioner. LA does not impose a separate payroll tax; the business tax is gross-receipts-based.

### 14.4 Other Local Payroll Surcharges

A handful of California cities have unique payroll surcharges:

- San Jose — Business tax; rate by employee count
- Oakland — Business license tax
- Berkeley — Business license tax with a payroll-based tier
- San Diego — Business tax certificate; nominal

Confirm the employer's city and check the city's business-license ordinance. Most are nominal but should not be ignored.

## 15. Worked Examples

### 15.1 Worked Example — SMB with 5 Employees (Tech Consulting, Non-Tipped)

**Facts:** Acme Consulting LLC (single-member LLC owned by founder, no S-corp election), based in Mountain View, CA. Five W-2 employees as of January 1, 2025:

**Acme Consulting employees table**

| Employee | Annual Salary | Filing Status | DE 4 Allowances |
| --- | --- | --- | --- |
| Ada (CEO) | $250,000 | MFJ | 2 |
| Ben (Senior Dev) | $180,000 | Single | 1 |
| Carol (Dev) | $120,000 | HOH | 2 |
| Dan (Designer) | $90,000 | Single | 1 |
| Eve (Office Mgr) | $60,000 | MFJ | 3 |

No bonuses, no equity. Acme offers a Solo 401(k) for the founder only — does NOT cover the W-2 employees. The W-2 employees have no employer-sponsored retirement plan.

**California payroll tax computation for Q1 2025 (Jan-Mar)**  _(https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44-25.pdf)_

| Employee | Q1 Wages | PIT Withheld (est. Method B) | SDI 1.2% | SUI (3.4% × min($7,000, Q1 wages)) | ETT 0.1% on same |
| --- | --- | --- | --- | --- | --- |
| Ada | $62,500 | ~$5,200 | $750.00 | $238 (cap hit) | $7 |
| Ben | $45,000 | ~$3,400 | $540.00 | $238 (cap hit) | $7 |
| Carol | $30,000 | ~$1,800 | $360.00 | $238 (cap hit) | $7 |
| Dan | $22,500 | ~$1,400 | $270.00 | $238 (cap hit) | $7 |
| Eve | $15,000 | ~$700 | $180.00 | $238 (cap hit) | $7 |
| **Total Q1** | $175,000 | $12,500 | $2,100 | $1,190 | $35 |

(PIT amounts are approximate Method B estimates for illustration; actual amounts depend on pay-period bracketing.)

- **Q1 DE 9 total liability to EDD** — $12,500 (PIT) + $2,100 (SDI, employee) + $1,190 (SUI, employer) + $35 (ETT, employer) = $15,825  _(https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44-25.pdf)_

**Deposit cadence:** Q1 PIT withholding is $12,500, which is materially above the $500 quarterly threshold. Acme's federal deposit schedule (assumed monthly based on prior-year aggregate < $50,000) translates to monthly CA deposits on the 15th of the following month:
- Jan PIT + SDI ≈ $4,870: deposit by Feb 15
- Feb PIT + SDI ≈ $4,870: deposit by Mar 15
- Mar PIT + SDI ≈ $4,870: deposit by Apr 15

SUI ($1,190) and ETT ($35) are remitted with the DE 9 by April 30 (not deposited monthly).

**CalSavers compliance:** Acme does NOT offer a qualified plan to its W-2 employees (the Solo 401(k) covers only the owner, who is not a W-2 employee here). Acme is therefore subject to the **CalSavers mandate**. Acme must register with CalSavers by December 31, 2025 (the 1+ employee deadline), submit the employee census, and facilitate payroll deductions at the default 5% rate. **AUDIT FLASH POINT** — failure exposes Acme to $750 × 5 = $3,750 in penalties.

**Workers' comp:** Acme must carry a workers' comp policy covering all five employees. Class code 8810 (clerical) and 8742 (outside sales / tech consulting at client sites) are likely applicable, with rates ~$0.30-$0.50 per $100 of payroll. Annual premium estimate on $700,000 annualized payroll: $2,100 - $3,500.

**Annual reconciliation (Form W-2 Box 16/17):** Each employee receives a Form W-2 in January 2026 showing CA wages in Box 16 and CA PIT withheld in Box 17. Box 14 shows SDI withheld. Acme files Form W-2 with the SSA by January 31, 2026 (federal) and the Q4 DE 9 by January 31, 2026 (CA) — the two filings must reconcile.

### 15.2 Worked Example — Retail with Tipped Employees

**Facts:** Bella's Bistro LLC, full-service restaurant in Sacramento, CA. Ten W-2 employees: 4 servers (tipped), 2 line cooks (non-tipped), 1 dishwasher (non-tipped), 2 bartenders (tipped), 1 manager (salaried exempt). The 2025 California minimum wage is $16.50/hour (statewide); Sacramento has no separate higher minimum wage (the city minimum aligns with state). Tipped employees are paid the full minimum wage in cash by the employer plus tips (no tip credit per Labor Code §351).

- **Server tip mechanics** — Cash tips: Reported by the employee to the employer on Form 4070 (federal) or its equivalent by the 10th of the following month. Tips are subject to PIT, SDI, federal income tax, and FICA. Credit-card tips: Pooled by the restaurant and distributed to servers (and tip-pool participants per Labor Code §351; managers and owners cannot share in a mandatory tip pool). Reported via payroll. Service charges (mandatory gratuities of 18%+ on large parties): NOT tips — they are wages to the employee, subject to the employer's full payroll tax responsibility and minimum-wage compliance.  _(Labor Code §351)_

**Worked Q1 2025 illustration — Server Sarah:**

- Hourly rate: $16.50/hour
- Hours worked: 480 hours (Q1)
- Direct wages: $7,920
- Cash tips reported: $5,000
- Credit-card tips distributed: $4,000
- Total wages subject to CA PIT and SDI: $7,920 + $5,000 + $4,000 = **$16,920**

CA payroll on Sarah's Q1:
- PIT withheld (Method B, approximated, single, 1 allowance, quarterly): ~$340
- SDI 1.2% × $16,920 = $203.04 (employee)
- SUI 3.4% × min($7,000, $16,920) = $238 (employer, capped at $7,000 wage base)
- ETT 0.1% × $7,000 = $7 (employer)

- **Tips count toward SUI wage base** — Critical: Sarah's reported tips count toward the SUI wage base. Bella's SUI cost is therefore the maximum $238 for Sarah in Q1, even though her direct wages alone would not have hit the $7,000 cap until late Q2. This is a common reporting error — payroll software sometimes excludes tips from the SUI base, understating Bella's SUI liability for the lower-tipped employees.
- **Wage statement under §226 requirements** — Sarah's pay stub must itemize: Gross direct wages; Tips paid through payroll (credit-card pool); Cash tips reported (informational; usually shown as a memo line); All deductions (PIT, SDI, federal income tax, FICA Social Security, FICA Medicare, any union dues, etc.); Net pay; Hours worked; Pay period dates; Sarah's name and last 4 of SSN; Bella's Bistro LLC's full legal name and address; Hourly rate ($16.50). Failure to itemize any single item is a §226 violation per pay period, exposing Bella's to $50/$100 per pay period per employee.  _(Labor Code §226)_
- **Service Charges Note** — If Bella's adds an automatic 20% service charge on parties of 6+, that 20% is NOT a tip — it's revenue to the restaurant, and any portion distributed to staff is straight wages. Wage statement must show it as a separate wage line.

### 15.3 Worked Example — Tech Company with Equity Grants (Founder + Engineering Hires)

**Facts:** Crescent Robotics Inc. (Delaware C-corp, registered to do business in California, sole headquarters in San Francisco). Founder Frank earns $250,000 W-2 salary; 8 engineering employees earn $200,000-$400,000 base; all employees receive Restricted Stock Unit (RSU) grants vesting quarterly. In Q1 2025:

- Frank vests $400,000 in RSUs (cliff-vest from a 2021 grant); FMV $400,000
- Eight engineers collectively vest $2,800,000 in RSUs
- Base salaries totaling $625,000 paid in Q1

- **California PIT withholding on RSU vests** — RSU vesting events generate W-2 ordinary income equal to the FMV of the shares at vest, less any amount paid by the employee (typically zero for RSUs). This income is supplemental wages for California withholding purposes — subject to the 10.23% flat supplemental rate unless aggregated with the regular paycheck.  _(https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44-25.pdf)_

For Frank's $400,000 vest:
- CA PIT supplemental withholding at 10.23%: **$40,920**
- SDI 1.2% × $400,000: **$4,800** (no wage cap — full vest is SDI-taxable)
- Federal supplemental withholding at 22% (first $1M of supplemental in a calendar year): **$88,000**
- Federal Medicare 1.45% + Additional Medicare 0.9% (Frank's YTD > $200,000): **$9,400**
- Federal Social Security 6.2% — likely already capped from prior wages or this vest; if not, up to $176,100 base × 6.2% = up to $10,918

**Frank's CA tax exposure at his 13.3% top marginal rate:**
- True CA tax on the vest at the top bracket: $400,000 × 13.3% = $53,200 (assuming Frank's total income exceeds $1M, triggering MHST)
- CA PIT withheld at 10.23% supplemental: $40,920
- **Under-withholding: $12,280 on this single vest**

Across the year, if Frank has four such quarterly vests, the under-withholding compounds to ~$49,000 owed at year-end on Form 540. **AUDIT FLASH POINT** (§3.5 referenced) — Frank should file a DE 4 requesting additional fixed-dollar withholding per pay period, or make estimated payments via Form 540-ES (see `ca-540-es-estimated-tax`).

**Aggregate Q1 CA payroll cost to Crescent**  _(https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44-25.pdf)_

| Component | Amount |
| --- | --- |
| PIT withholding on base salaries (9 employees, mixed brackets) | ~$70,000 |
| PIT withholding on RSU vests ($3.2M × 10.23%) | $327,360 |
| SDI on all wages ($625K base + $3.2M vest = $3.825M × 1.2%) | $45,900 |
| SUI on first $7,000 per employee × 9 employees × 3.4% (assuming experience-rated; if new employer use 3.4%) | $2,142 |
| ETT 0.1% × $7,000 × 9 employees | $63 |
| **Total Q1 CA EDD remittance** | **$445,465** |

The bulk is PIT withholding; SDI is the second-largest line item due to the uncapped wage base — about $46K of SDI for a 9-person engineering team is a material expense category that did not exist before SB 951's cap removal.

- **Wage statement §226 for RSU vests** — Each RSU vest event creates wages that must appear on the wage statement for the pay period in which the vest is settled. If Crescent uses a payroll integration with the equity-management platform (e.g., Carta), the vest amount and supplemental withholding lines must flow through to the pay stub. Otherwise, an off-cycle stub must be issued. Failure exposes Crescent to §226(e) penalties per vest event per employee.  _(§226(e))_
- **§83(b) elections, ESPP disqualifying dispositions, NQSO exercises** — All follow similar mechanics — supplemental withholding at 10.23% CA + 22% federal (or 37% on supplemental wages above $1M YTD federal). Refer to equity-comp specialist for §409A and §83(b) interactions.  _(https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44-25.pdf)_
- **CalSavers exemption for Crescent** — Crescent offers a 401(k) plan to all employees with company match — Crescent is therefore EXEMPT from the CalSavers mandate but must still file the CalSavers exemption attestation in the portal (one-time, then maintained).

## 16. Cross-Skill Coordination

This skill outputs feed into:

- `us-federal-payroll` (separate skill, if loaded) — for Form 941, 940, W-2 federal mechanics
- `ca-540-individual-return` — Form 540 line 71 (CA withholding) is sourced from W-2 Box 17, which this skill governs at issuance
- `ca-540-es-estimated-tax` — employees with under-withheld supplemental wages (§3.5 flash point) feed into Q4 estimated-payment planning
- `us-s-corp-election-decision` — founders modeling S-corp election need accurate CA payroll cost estimates (SUI, ETT, SDI on the salary leg, CalSavers if no qualified plan) for the break-even analysis
- `ca-llc-fee-and-tax` — LLC owners who pay themselves as W-2 employees of their own S-corp run this skill; LLC owners who take guaranteed payments / draws do NOT (those are not wages and not subject to EDD payroll taxes)
- `us-1099-nec-issuance` — paired with §11 (DE 542) for any contractor payments

When called from `us-ca-return-assembly`, this skill produces the prior-year W-2 totals that flow into Form 540 line 71 and Schedule CA (540).

## 17. Conservative Defaults — Quick Reference

**Conservative Defaults — Quick Reference**  _(https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44-25.pdf)_

| Ambiguity | Conservative Default |
| --- | --- |
| Worker is contractor vs employee under ABC test | **Employee** unless all three prongs clearly pass |
| Tip amount disputed by employee | Use employee's reported figure (Form 4070 / payroll declaration) |
| SDI cap question | **No cap** (since 2024) |
| Supplemental withholding rate uncertainty | **Use DE 44 category rate**: 10.23% for bonuses/stock options; 6.6% for other supplemental wages |
| CalSavers exemption claim where qualified plan coverage is fuzzy | Register with CalSavers; the exemption attestation requires affirmative qualified-plan status |
| Final-pay timing question | Same day for involuntary; same day or within 72 hours for voluntary |
| Wage-statement item missing | Reissue corrected statement and document the correction |
| Workers' comp coverage gap (e.g., remote employee in another state) | Confirm CA policy covers remote work; if remote employee is in another state, that state's WC may apply (refer-out) |
| AB5 exemption claim under §2776 B2B | All 12 criteria must demonstrably be met; partial satisfaction = ABC test applies |
| FUTA credit-reduction state status | Assume California IS a credit-reduction state for 2025 (verify in Nov 2025 IRS announcement) |

When facts are ambiguous, apply the conservative default and disclose:

## 18. Provenance and Citations

**Statutory:**
- California Unemployment Insurance Code §13020 et seq. (PIT withholding mechanism)
- California Unemployment Insurance Code §976.5 (voluntary UI contribution)
- California Unemployment Insurance Code §1088.8 (DE 542 contractor reporting)
- California Unemployment Insurance Code §3251 et seq. (Voluntary SDI Plans)
- California Revenue and Taxation Code §17043 (Mental Health Services Tax 1% surtax over $1M)
- California Revenue and Taxation Code §18661, §18664 (PIT withholding administration)
- California Revenue and Taxation Code §19170 (deposit penalties)
- California Labor Code §201-203 (final pay and waiting-time penalty)
- California Labor Code §226 (itemized wage statements)
- California Labor Code §351 (no tip credit)
- California Labor Code §2698 et seq. (PAGA)
- California Labor Code §2775 et seq. (ABC test; AB5 / AB 2257 codification)
- California Labor Code §3700 et seq. (workers' compensation mandatory coverage)
- California Government Code §100000 et seq. (CalSavers)
- Senate Bill 951 (Chapter 878, Statutes of 2022) — SDI cap removal
- Senate Bill 1126 (Chapter 681, Statutes of 2022) — CalSavers 1+ employee expansion
- Assembly Bill 5 (Chapter 296, Statutes of 2019) — ABC test codification
- Assembly Bill 2257 (Chapter 38, Statutes of 2020) — ABC test exemption refinement

**Case law:**
- Dynamex Operations West, Inc. v. Superior Court, 4 Cal.5th 903 (2018) — ABC test
- Suastez v. Plastic Dress-Up Co., 31 Cal.3d 774 (1982) — vacation pay as vested wages
- Boothby v. Atlas Mechanical, Inc., 6 Cal.App.4th 1595 (1992) — vacation accrual caps permitted
- Schachter v. Citigroup, Inc., 47 Cal.4th 610 (2009) — vested but unpaid bonuses are wages
- Mamika v. Barca, 68 Cal.App.4th 487 (1998) — §203 willfulness standard
- Cicairos v. Summit Logistics, Inc., 133 Cal.App.4th 949 (2005) — legal entity name on wage statement
- S.G. Borello & Sons, Inc. v. Dept. of Industrial Relations, 48 Cal.3d 341 (1989) — pre-ABC common-law factors (still applies to statutory exemptions)

**Administrative guidance:**
- EDD Publication DE 44 (California Employer's Guide) — annual update; the primary practitioner reference
- EDD Publication DE 8829 (Household Employer's Guide) — domestic worker variant
- EDD Information Sheet DE 231 series (specific topics; classification, supplemental wages, voluntary plans)
- EDD Form DE 4 instructions
- EDD Form DE 9 / DE 9C instructions
- EDD Form DE 542 instructions
- Form DE 2088 (annual employer rate notice)
- CalSavers Employer Handbook (CalSavers Retirement Savings Board)
- FTB Publication 1006 (California Tax Forms and Related Federal Forms) — withholding cross-reference

**Federal interactions (referenced, not authoritative within this skill):**
- IRS Publication 15 (Circular E) — federal employment tax basics
- IRS Form 941, 940, W-2/W-3 instructions
- IRS §6041, §3406 (information reporting and backup withholding)
- US Department of Labor FUTA credit-reduction state announcement (annual, November)

**Last updated:** 2025-11-15. Confirm against current EDD DE 44 and FTB indexed bracket announcements at engagement time. Bracket inflation indexing is performed annually by FTB; SUI / ETT rates are reset annually via Form DE 2088.

## 19. Circular 230 Disclosure and Reviewer Responsibility

This skill is a content reference for credentialed payroll and tax professionals. It is NOT tax advice to the taxpayer. Under Treasury Department Circular 230 §10.33 and §10.37, any written advice based on this skill's output must be reviewed by a credentialed reviewer (Enrolled Agent, CPA, or attorney) — or for purely state-payroll matters, a CPP (Certified Payroll Professional) or experienced payroll practitioner with California-specific competence — before delivery to the client or filing with the EDD, FTB, or any other authority.

The skill is reviewer-oriented and assumes downstream reconciliation and self-checks per `us-tax-workflow-base`. Misapplication risk is high in three areas:

1. **AB5 classification** — the ABC test is unforgiving and litigation is active. When in doubt, treat as an employee.
2. **SDI uncapped wage base** — payroll system configuration drift continues to produce errors in 2025 prior-period audits.
3. **CalSavers mandate** — the December 31, 2025 1+ employee deadline arrives during the engagement window for many small businesses; non-registration is a $750/employee penalty.

A taxpayer or employer relying on this skill without credentialed review proceeds at their own risk. The skill is current as of November 15, 2025 and is subject to change with new EDD publications, FTB rate adjustments, court decisions affecting AB5, and statutory amendments.

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
