---
name: us-form-941-940-payroll
description: Tier 2 US federal content skill for employer payroll tax compliance — Forms 941 (quarterly), 940 (annual FUTA), W-2 (employee), W-3 (SSA transmittal). Covers tax year 2025 including the $176,100 Social Security wage base, the 0.9% Additional Medicare withholding threshold, monthly vs semiweekly vs next-day deposit schedules under IRC §6302, the $7,000 FUTA wage base and 5.4% state UI credit (0.6% effective in non-credit-reduction states), W-2 Box 1/3/5 reconciliation traps with §125, HSA, retirement, and the 10+ W-2 electronic-filing mandate from the 2024 IRS final regs.
jurisdiction: US
category: federal-tax
tier: 2
verified_by: pending
last_updated: 2026-07-06
version: 0.1
---

# US Federal Payroll Tax — Forms 941, 940, W-2, W-3 (Tax Year 2025)

## 1. Scope

This skill covers US federal employer payroll tax compliance for tax year 2025 for businesses that have one or more W-2 employees. It is the companion to `us-1099-nec-issuance` (which handles independent contractor reporting) and `us-schedule-c-and-se-computation` (which handles the owner's own SE tax when the owner is a sole proprietor or single-member LLC disregarded for federal tax).

In scope:

- Form 941 (Employer's Quarterly Federal Tax Return) — federal income tax withholding, employer + employee Social Security tax, employer + employee Medicare tax, and the 0.9% Additional Medicare Tax employer withholding obligation
- Form 940 (Employer's Annual Federal Unemployment (FUTA) Tax Return) — including Schedule A multi-state credit reduction computation
- Form W-2 (Wage and Tax Statement) — preparation for each employee, the Box 1 vs Box 3 vs Box 5 reconciliation, Box 12 codes, and Box 14 free-text use
- Form W-3 (Transmittal of Wage and Tax Statements) — the paper transmittal to SSA
- Form W-4 (2020-and-later redesigned employee withholding certificate)
- Deposit schedule determination — the lookback rule, monthly vs semiweekly, the $100,000 next-day deposit rule, EFTPS mechanics
- Form 944 (annual return for very small employers), Form 943 (agricultural employers), Form 945 (nonpayroll income tax withholding) — referenced for scope routing
- Form 8027 (tip reporting for large food and beverage establishments) — referenced
- IRC §6656 deposit penalty tiers (2%, 5%, 10%, 15%)
- The IRS final regulations under T.D. 9972 (published Feb. 23, 2023; applicable to returns required to be filed on or after Jan. 1, 2024) reducing the electronic-filing threshold from 250 to 10 information returns
- Worker classification at a high level (refers to `us-1099-nec-issuance` for the §3121(d) common-law control test and the DOL economic-realities test under the 2024 Worker Classification rule at 29 C.F.R. Part 795)

Out of scope (refusal-eligible):

- State income tax withholding (covered separately by state-specific skills such as `ca-540-individual-return`'s payroll-adjacent state filings)
- State unemployment insurance (SUI) returns — covered by state skills; the federal skill computes only the FUTA portion and the credit for state UI taxes paid
- Local payroll taxes (city, county, school district)
- Multi-employer pension plan reporting
- Form 5500 series (employee benefit plan returns)
- Affordable Care Act employer mandate forms 1094-C and 1095-C
- Garnishments, child support withholding orders, and other non-tax payroll deductions
- Non-US employees (resident aliens are in scope; nonresident aliens, Form 1042, Form 8233 chapter 3 withholding are out of scope)
- Statutory employees (limited touch — see §11)
- Household employees on Schedule H (Form 1040) — out of scope; the employer is the household, not a business
- Family employee exemptions under §3121(b)(3) (parent employing child under 18, etc.) — referenced only

This skill assumes a credentialed reviewer (CPA, EA, or attorney) will review all output before any return is signed or any deposit is made on the taxpayer's behalf.

---

## 2. Form 941 — Employer's Quarterly Federal Tax Return

### 2.1 Purpose

Form 941 reports the wages paid to W-2 employees during the calendar quarter and the federal employment taxes attributable to those wages. The form is filed by virtually every employer that pays wages subject to federal income tax withholding or Social Security and Medicare tax, except those qualifying for Form 944 (very small annual filers), Form 943 (farm employers), or Form 944-SS / 941-SS (US territories — out of scope).

The form has four functional sections:

1. Identification and totals (Part 1) — wages, tips, federal income tax withheld, FICA (Social Security + Medicare) wages and tax, and the Additional Medicare withholding
2. Deposit schedule (Part 2) — confirms monthly or semiweekly depositor status and reports the schedule of liabilities (Schedule B for semiweekly)
3. Business closure / seasonal indicator (Part 3)
4. Third-party designee and signature (Parts 4-5)

### 2.2 Line-by-line walkthrough (2025 form)

The IRS publishes Form 941 with quarter-specific revision dates but the line numbering is stable for 2025. The principal lines:

- Line 1 — Number of employees who received wages, tips, or other compensation for the pay period including March 12 (Q1), June 12 (Q2), September 12 (Q3), or December 12 (Q4). This is a snapshot count, not a quarter total.
- Line 2 — Total wages, tips, and other compensation (Box 1 federal income tax wages — federal income tax wages, not FICA wages)
- Line 3 — Federal income tax withheld from those wages, tips, and other compensation
- Line 4 — Checkbox if no wages, tips, and other compensation are subject to Social Security or Medicare tax (rare — used by certain religious organizations and certain agricultural employers filing 943 instead)
- Line 5a — Taxable Social Security wages × 0.124 (combined 6.2% employee + 6.2% employer). Column 1 is the wages, Column 2 is the tax. The wages reported here are capped per employee per calendar year at the Social Security wage base ($176,100 for 2025).
- Line 5a(i) — Qualified sick leave wages × 0.062 (legacy FFCRA — should be zero for 2025; FFCRA credits expired 9/30/2021)
- Line 5a(ii) — Qualified family leave wages × 0.062 (legacy FFCRA — should be zero for 2025)
- Line 5b — Taxable Social Security tips × 0.124
- Line 5c — Taxable Medicare wages and tips × 0.029 (combined 1.45% employee + 1.45% employer). No wage cap.
- Line 5d — Taxable wages and tips subject to Additional Medicare Tax withholding × 0.009. This is the employer's withholding obligation only — the employer must withhold an additional 0.9% on each individual employee's wages in excess of $200,000 paid by that employer during the calendar year, regardless of the employee's filing status or other employers. The actual liability for Additional Medicare Tax is reconciled on the employee's Form 8959 attached to Form 1040.
- Line 5e — Total Social Security and Medicare tax (sum of 5a Col 2 + 5a(i) Col 2 + 5a(ii) Col 2 + 5b Col 2 + 5c Col 2 + 5d Col 2)
- Line 5f — Section 3121(q) Notice and Demand for tax on unreported tips (rare; used only when the IRS has issued a §3121(q) notice)
- Line 6 — Total taxes before adjustments = Line 3 + Line 5e + Line 5f
- Line 7 — Current quarter's adjustment for fractions of cents (small rounding plug, typically a few cents)
- Line 8 — Current quarter's adjustment for sick pay (third-party sick pay shifts; see Pub 15-A)
- Line 9 — Current quarter's adjustments for tips and group-term life insurance (the GTL > $50k employer FICA paid on behalf of former employees, etc.)
- Line 10 — Total taxes after adjustments
- Line 11a — Qualified small business payroll tax credit for increasing research activities (Form 8974). For 2025, the maximum credit is $500,000 per year ($250,000 against Social Security tax under the original IRC §41(h) limit and an additional $250,000 against Medicare tax under the Inflation Reduction Act of 2022 increase, applicable to tax years beginning after 12/31/2022). Form 8974 must be attached.
- Line 11b — Reserved for future use (formerly used for ERC and FFCRA — should be blank in 2025)
- Line 11c — Reserved
- Line 11d — Reserved
- Line 11e — Reserved
- Line 11f — Reserved
- Line 11g — Total nonrefundable credits
- Line 12 — Total taxes after adjustments and nonrefundable credits = Line 10 minus Line 11g
- Line 13a — Total deposits for the quarter, including overpayments from prior quarters applied
- Line 13b through 13f — Reserved for future use
- Line 13g — Total deposits and refundable credits
- Line 14 — Balance due = Line 12 minus Line 13g, if positive
- Line 15 — Overpayment = Line 13g minus Line 12, if positive; check box to apply to next return or request refund
- Line 16 — Tax liability for the quarter. If Line 12 is less than $2,500, no deposit schedule required — pay with return. If $2,500 or more and a monthly depositor, enter monthly liabilities directly on Line 16. If $2,500 or more and a semiweekly depositor, check the box on Line 16 indicating semiweekly and attach Schedule B (Form 941).

### 2.3 Filing due dates

Form 941 is due the last day of the month following the end of the quarter:

| Quarter | Period covered | Due date | Extended due date if all deposits timely |
|---|---|---|---|
| Q1 | Jan 1 – Mar 31 | April 30 | May 10 |
| Q2 | Apr 1 – Jun 30 | July 31 | August 10 |
| Q3 | Jul 1 – Sep 30 | October 31 | November 10 |
| Q4 | Oct 1 – Dec 31 | January 31 (of next year) | February 10 |

The 10-day extension under IRC §6071(b) and Treas. Reg. §31.6071(a)-1(a)(1) is available only if all required deposits for the quarter were made in full and on time.

If the due date falls on a Saturday, Sunday, or legal holiday, the return is timely if filed by the next business day under IRC §7503.

### 2.4 Form 941-X (Adjusted Employer's Quarterly Federal Tax Return or Claim for Refund)

Used to correct errors on a previously filed Form 941. Two paths:

1. **Adjusted return process** (interest-free under §6205) — used to correct administrative errors (wrong wages, wrong tax) that resulted in either an underpayment or overpayment, when the period of limitation on assessment has not expired and the employer is correcting a §3402 income tax withholding or §3121 FICA error. The interest-free adjustment must be reported on Form 941-X by the due date of the return for the return period in which the error is ASCERTAINED (Treas. Reg. §31.6205-1(b)(2)), not a flat April 15 deadline.
2. **Claim for refund process** under §6402 — used when the employer is claiming a refund of overcollected employee tax. Requires written consent from each affected employee (or evidence the employer reimbursed the employee) per Treas. Reg. §31.6402(a)-2.

Common 941-X scenarios:

- Discovery of a bonus that was never run through payroll
- Misclassification correction (treated as 1099, should have been W-2)
- Mid-year discovery that an employee crossed the $176,100 Social Security wage base earlier than the payroll system tracked
- Retroactive wage adjustments (settlements, back pay)
- Reclassification of a fringe benefit (e.g., personal use of company car that was missed during the year — also corrected via W-2c if W-2 was already issued)

Form 941-X is filed separately, not attached to the next Form 941.

### 2.5 Form 944 (annual variant for very small employers)

Form 944 is an annual employment tax return that replaces Form 941 for employers whose total annual employment tax liability is $1,000 or less. **Eligibility is by IRS notification only** — the employer cannot self-elect. The IRS sends a written notice (typically in early in the year) informing the employer that they are eligible to file Form 944 for that year.

Employers who want to file 944 can request the change by April 1 of the year by calling the IRS or writing to the appropriate IRS office. Employers who want to switch from 944 to 941 must request the change in writing by April 1.

Form 944 is due January 31 of the following year (February 10 with the 10-day extension if all deposits were timely).

### 2.6 Form 943 (agricultural employers)

Form 943 (Employer's Annual Federal Tax Return for Agricultural Employees) is filed by employers who paid wages to one or more farmworkers if the wages were subject to FICA or federal income tax withholding. The two tests for FICA on farm wages are:

1. **$150 test** — cash wages of $150 or more in the calendar year to any one farmworker, or
2. **$2,500 test** — total cash and noncash wages of $2,500 or more paid to all farmworkers in the year

If either is met, all cash wages paid to the farmworker are subject to FICA. Form 943 is annual; due January 31 (February 10 extension).

### 2.7 Form 945 (annual return of withheld federal income tax — nonpayroll)

Form 945 reports federal income tax withheld from **nonpayroll** payments. Common items:

- Pensions, annuities, and IRA distributions (1099-R)
- Military retirement
- Gambling winnings (W-2G)
- Indian gaming profits paid to tribal members
- Backup withholding under §3406 at 24% for 2025 (the fourth-lowest §1(c) rate; the TCJA rate structure was made permanent by OBBBA §70101)
- Voluntary withholding on unemployment compensation, Social Security benefits, and certain federal payments

Form 945 is annual, due January 31 (February 10 extension). Federal income tax withheld from W-2 wages is NOT reported on Form 945 — that goes on Form 941.

---

## 3. Wage Bases and Rates — 2025

### 3.1 Social Security (OASDI)

- **Combined rate**: 12.4% (6.2% employee + 6.2% employer)
- **Wage base for 2025**: **$176,100** per employee, per calendar year
- Source: Social Security Administration Fact Sheet released October 10, 2024 announcing the 2025 cost-of-living adjustment. The $176,100 base reflects the SSA's calculation under §230 of the Social Security Act using the national average wage index.
- Self-employed equivalent on Schedule SE: 12.4% on the same $176,100 base, computed against 92.35% of net SE earnings.
- The wage base is **per employer's EIN**. If an employee works for two unrelated employers in the same year, each employer is independently obligated to withhold 6.2% up to $176,100 of wages it paid. The employee then receives a credit for the excess on Form 1040, Schedule 3, Line 11 ("Excess Social Security and tier 1 RRTA tax withheld"). The employers do NOT get a refund of their portion — the excess refund is to the employee only.
- For a **single employer with multiple EINs** (e.g., common paymaster arrangement under §3121(s) or successor employer rule), there is one combined base if the requirements are met.
- Successor employer rule under §3121(a)(1) and Rev. Proc. 2004-53: when an employer acquires substantially all the property of another employer mid-year, the successor may credit the predecessor's payments toward the wage base.

### 3.2 Medicare (Hospital Insurance)

- **Combined rate**: 2.9% (1.45% employee + 1.45% employer)
- **Wage base**: None — uncapped
- Applies to all wages and self-employment earnings

### 3.3 Additional Medicare Tax (§3101(b)(2))

- **Rate**: 0.9% (employee only)
- **Employer withholding threshold**: $200,000 of wages paid by that employer to a single employee during the calendar year. The employer is required to withhold an additional 0.9% from wages in excess of $200,000, **regardless of the employee's filing status, other income, or wages from other employers**. The employer does NOT match this 0.9%.
- **Employee filing threshold**: The actual Additional Medicare Tax liability is assessed against the employee's combined wages and SE earnings using filing-status thresholds:
  - Married filing jointly: $250,000
  - Married filing separately: $125,000
  - Single, head of household, qualifying widow(er): $200,000
- The employee reconciles the difference between what was withheld by the employer (based on the $200,000 per-employer threshold) and what is actually owed (based on filing-status threshold against combined income) on **Form 8959** filed with Form 1040.

This creates two common reconciliation scenarios:

1. **Married filing jointly with one earner at $250,000** — employer withholds 0.9% on wages above $200,000 = $450 withheld. Filing-status threshold is $250,000, so no Additional Medicare Tax owed. The $450 is credited as withheld federal tax via Form 8959 → Schedule 2 → 1040.
2. **Single earner with two jobs, $150,000 each** — neither employer withholds Additional Medicare (each is below $200,000). Total wages $300,000 against single threshold $200,000 = $100,000 × 0.9% = $900 owed. Computed on Form 8959 and added to total tax.

### 3.4 FUTA (Federal Unemployment Tax Act)

- **Statutory rate**: 6.0%
- **Wage base**: First $7,000 of wages per employee per calendar year
- **State credit**: Up to 5.4% credit for state unemployment insurance taxes paid timely → effective federal rate **0.6%** in non-credit-reduction states
- Maximum FUTA per employee in a non-credit-reduction state: $7,000 × 0.6% = **$42.00 per year**
- Employee does NOT pay FUTA — employer only

### 3.5 Federal Income Tax Withholding

- No flat rate — computed under Pub 15-T using the percentage method or wage bracket method against the employee's Form W-4
- 2020-and-later W-4 uses dollar amounts; pre-2020 W-4 uses allowances (still valid if on file)
- 2025 brackets for income tax withholding mirror the 2025 individual tax brackets (10%, 12%, 22%, 24%, 32%, 35%, 37%) under §1, adjusted for inflation per Rev. Proc. 2024-40

### 3.6 2025 reference table

| Tax | Employee rate | Employer rate | Wage base 2025 | Max per employee per year |
|---|---|---|---|---|
| Social Security | 6.2% | 6.2% | $176,100 | $10,918.20 each side |
| Medicare | 1.45% | 1.45% | None | No cap |
| Additional Medicare | 0.9% | 0% | $200,000 (employer withholding trigger) | Variable |
| FUTA | 0% | 6.0% gross / 0.6% net | $7,000 | $42.00 (net) |
| Federal income tax | Variable | 0% | None | Variable |

---

## 4. Deposit Schedule — The Lookback Rule

The deposit schedule is determined annually based on the employer's **lookback period** total tax liability under §6302 and Treas. Reg. §31.6302-1.

### 4.1 Lookback period definition

The lookback period for Form 941 filers is the 12-month period ending the previous June 30. For deposit obligations during calendar year 2025, the lookback period is **July 1, 2023 through June 30, 2024**.

For Form 944 (annual) filers who are required or eligible to file 944, the lookback period is the second preceding calendar year (so 2023 for deposits made in 2025).

For Form 943 (agricultural), the lookback period is the second preceding calendar year.

### 4.2 Monthly vs Semiweekly classification

| Lookback period total Form 941 liabilities (Lines 12 of all four quarters) | Depositor status for 2025 |
|---|---|
| ≤ $50,000 | Monthly depositor |
| > $50,000 | Semiweekly depositor |

**Monthly depositor**: Deposit the entire month's accumulated employment tax by the **15th of the following month**. Example: April 2025 payroll taxes are deposited by May 15, 2025.

**Semiweekly depositor**: Deposit on a Wednesday or Friday following payday, based on the day of the week the wages were paid:

| Payday falls on | Deposit due by |
|---|---|
| Wednesday, Thursday, or Friday | Following Wednesday |
| Saturday, Sunday, Monday, or Tuesday | Following Friday |

The semiweekly schedule gives the employer at least 3 banking days from payday to deposit. If a banking holiday intervenes, the deposit due date is extended.

### 4.3 The $100,000 Next-Day Deposit Rule

If accumulated unpaid employment tax liability reaches **$100,000 or more on any single day**, the employer must deposit by the **next business day**, regardless of whether the employer is a monthly or semiweekly depositor.

Once the $100,000 next-day rule is triggered, a monthly depositor **immediately becomes a semiweekly depositor for the remainder of the current calendar year and for the entire following calendar year**. This is sometimes called the "promotion" to semiweekly.

The $100,000 amount is the accumulated employment tax — federal income tax withheld plus employee and employer FICA — not just one component.

### 4.4 The de minimis $2,500 quarter rule

The tax may be paid with the return (no deposit required) if Line 12 for the CURRENT quarter is less than $2,500, OR Line 12 for the PRIOR quarter was less than $2,500 (a disjunctive test, not conjunctive). This is a quarter-by-quarter rule, not the annual lookback test.

### 4.5 EFTPS — Electronic Federal Tax Payment System

All federal tax deposits must be made electronically via EFTPS (Electronic Federal Tax Payment System), 26 C.F.R. §31.6302-1(h). The mandatory electronic deposit rule applies to substantially all employers; the legacy Form 8109 paper deposit coupon was retired effective December 31, 2010.

Mechanics:

- Enrollment: at eftps.gov, takes 5-7 business days to receive the PIN by mail
- Deposit must be initiated by 8:00 PM ET on the day before the deposit due date
- Payments can be scheduled up to 365 days in advance
- Confirmation number (EFT Acknowledgment Number) is the audit trail
- Same-day wire option is available for emergency deposits via the Federal Tax Same-Day Payment Worksheet — must be initiated by the employer's financial institution and there is typically a wire fee

### 4.6 Schedule B (Form 941) — Report of Tax Liability for Semiweekly Depositors

Required attachment for semiweekly depositors and for any employer that became a semiweekly depositor mid-quarter under the $100,000 next-day rule.

Schedule B reports the daily tax liability for each of the three months in the quarter. It does NOT report deposits — it reports liabilities (when wages were paid, the day the liability arose). The IRS uses Schedule B to determine deposit timeliness, comparing reported liabilities against EFTPS deposit dates.

---

## 5. Form 940 — Federal Unemployment (FUTA) Tax

### 5.1 Purpose

Form 940 computes the annual FUTA tax. FUTA funds the federal portion of state unemployment insurance administration and a federal account that lends to states whose UI trust funds become insolvent. FUTA is paid by the employer only — no employee withholding.

### 5.2 Coverage tests

An employer must file Form 940 if either:

1. **$1,500 test** — paid wages of $1,500 or more in any calendar quarter of the current or preceding calendar year, OR
2. **One-employee-20-weeks test** — had at least one employee for some part of a day in any 20 different weeks of the current or preceding calendar year

Separate tests apply for household employers (paid $1,000+ cash wages in any quarter; reported on Schedule H of Form 1040, not Form 940) and agricultural employers ($20,000 cash wages in any quarter OR 10+ employees for 20+ weeks; reported on Form 940 but with different thresholds).

### 5.3 Computation

- Gross FUTA: 6.0% × first $7,000 of each employee's wages
- State UI credit: up to 5.4% if state UI taxes were paid timely (generally by the federal Form 940 due date) and the state is **not a credit reduction state**
- Net FUTA in non-credit-reduction states: **0.6%** × first $7,000 per employee = **$42.00 per employee per year maximum**

### 5.4 Credit Reduction States — Schedule A

States that have borrowed from the federal unemployment trust fund (Title XII advances) and have not repaid by November 10 of the second consecutive year are subject to a FUTA credit reduction. The reduction starts at 0.3% for the first year of delinquency and increases by 0.3% each subsequent year (with limited "BCR add-on" provisions).

**2024 credit reduction states (for Form 940 filed by January 31, 2025)** — finalized by DOL:

- California (CA): 0.9% reduction → effective FUTA rate 1.5% (0.6% + 0.9%) on first $7,000 = $105 per employee
- New York (NY): 0.9% reduction → effective FUTA rate 1.5%
- US Virgin Islands (VI): 4.2% reduction → effective FUTA rate 4.8%
- Connecticut (CT): finalized — reduction status varied; verify final 2024 status against DOL November 2024 announcement

**For 2025 (Form 940 filed by January 31, 2026)** — the DOL announces final credit reduction states each November. As of the November 2025 DOL determination, the credit reduction status of each state must be verified against the official DOL Credit Reduction State announcement at oui.doleta.gov/unemploy/futa_credit.asp. The reviewer must check the current-year list before finalizing Form 940 Schedule A.

If the employer paid wages in any credit reduction state, **Schedule A (Form 940) is required**, listing each state with FUTA-taxable wages and the applicable credit reduction.

### 5.5 Filing due date

Form 940 is due **January 31** of the year following the tax year (so January 31, 2026 for tax year 2025), with an extension to **February 10** if all FUTA deposits were made on time.

### 5.6 Deposit schedule

FUTA is deposited quarterly when accumulated liability exceeds $500:

- If FUTA liability at the end of a quarter is **more than $500**, deposit by the last day of the month following the quarter (April 30, July 31, October 31, January 31)
- If $500 or less, carry forward to the next quarter
- If Q4 carryforward + Q4 accrual is $500 or less, pay with Form 940 by January 31
- Deposits via EFTPS only

### 5.7 Special situations

- **Multi-state employer** — files one Form 940 with Schedule A reporting each state's wages and applicable credit reductions
- **Successor employer** — may credit predecessor's wage payments toward the $7,000 per-employee FUTA base under §3306(b)(1) (and the corresponding FICA successor rule under §3121(a)(1)); note §3306(c)(8) is the exclusion for §501(c)(3) service, unrelated to the wage-base credit
- **Employee in two states for same employer** — wages are aggregated per employee per employer; the $7,000 base is one annual cap. The state of payment for credit reduction purposes is generally the state where the employee primarily performs services.
- **Group-term life insurance imputed income** — FUTA-taxable in most cases (see §3306(b))
- **§125 cafeteria plan elections, qualified retirement plan elective deferrals, HSA** — generally not FUTA-taxable (parallel to FICA treatment with some nuances; see Pub 15 Section 15 for the wage classification chart)

---

## 6. Form W-2 — Wage and Tax Statement

### 6.1 Purpose and due dates

Form W-2 reports the wages paid to and taxes withheld from each employee during the calendar year. One W-2 is required for each employee who was paid wages from which income, Social Security, or Medicare tax was withheld, or would have been withheld if the employee had not claimed exemption.

**Due dates** (accelerated by the PATH Act of 2015):

- To employees: by **January 31** of the year following the tax year
- To SSA (paper or electronic): by **January 31** — both copies share the same date as a result of PATH Act §201

The accelerated SSA due date enables the IRS to match W-2 wage data against individual tax returns claiming refunds in real-time, reducing identity-theft refund fraud.

### 6.2 The 10+ electronic filing mandate

Under **T.D. 9972** (final regulations published February 23, 2023, effective for information returns required to be filed on or after January 1, 2024), the electronic filing threshold for most information returns dropped from 250 to **10 in the aggregate** across most return types.

For W-2 purposes specifically:

- An employer required to file 10 or more information returns of any type (W-2, 1099-NEC, 1099-MISC, 1098, etc., counted in aggregate) must file all W-2s electronically with SSA via the SSA Business Services Online (BSO) portal
- Paper W-2 filing is permitted only if total information returns are 9 or fewer
- Penalty under §6721 for paper filing when electronic was required is the standard information return penalty per return

### 6.3 Boxes 1, 3, 5 — The Three Wages

The most common W-2 preparation error is the assumption that Box 1, Box 3, and Box 5 wages should be equal. They very often are not. Understanding the three wages is the single most important payroll-skill concept.

| Box | Wages reported | Federal tax base |
|---|---|---|
| 1 | Wages, tips, other compensation | Federal income tax (Form 1040 Line 1a) |
| 3 | Social Security wages | OASDI tax (capped at $176,100 for 2025) |
| 5 | Medicare wages and tips | HI tax (uncapped) |

**Differences from Box 1 → Box 3 / Box 5** (common):

| Item | Box 1 | Box 3 (SS) | Box 5 (Medicare) |
|---|---|---|---|
| 401(k) elective deferral (traditional) | Excluded | Included | Included |
| 403(b) elective deferral | Excluded | Included | Included |
| 457(b) elective deferral (governmental) | Excluded | Included | Included |
| Roth 401(k) elective deferral | Included | Included | Included |
| §125 cafeteria plan health premium | Excluded | Excluded | Excluded |
| §125 cafeteria plan dependent care FSA | Excluded (reported Box 10) | Excluded | Excluded |
| HSA contribution via §125 cafeteria plan (payroll deduction) | Excluded | Excluded | Excluded |
| HSA contribution outside §125 (rare for W-2) | Included | Included | Included |
| Group-term life insurance ≤ $50,000 | Excluded | Excluded | Excluded |
| Group-term life insurance > $50,000 (imputed income on excess) | Included | Included | Included |
| Adoption assistance under §137 (up to limit) | Excluded (reported Box 12 T) | Included | Included |
| Qualified transportation fringe under §132(f) (up to limit) | Excluded | Excluded | Excluded |
| Non-qualified deferred comp (§409A) | Depends — generally excluded when deferred, included when paid | Subject to special timing under §3121(v)(2) — included when vested | Included when vested |

**Differences from Box 3 only (capped at SS wage base)**:

- Box 3 is capped at $176,100 for 2025
- If employee earns $250,000 with no pre-tax 401(k), then Box 3 = $176,100 (capped), Box 5 = $250,000 (uncapped)

### 6.4 Box 12 codes — The Single-Letter Reference

| Code | Description |
|---|---|
| A | Uncollected SS or RRTA tax on tips |
| B | Uncollected Medicare tax on tips |
| C | Taxable cost of group-term life insurance over $50,000 (also in Boxes 1, 3, 5) |
| D | Elective deferrals to §401(k) (traditional) |
| E | Elective deferrals to §403(b) |
| F | Elective deferrals to §408(k)(6) SARSEP |
| G | Elective deferrals to §457(b) deferred comp plan |
| H | Elective deferrals to §501(c)(18)(D) plan |
| J | Nontaxable sick pay |
| K | 20% excise tax on excess golden parachute payments |
| L | Substantiated employee business expense reimbursements |
| M | Uncollected SS or RRTA tax on taxable cost of GTL > $50k (former employees only) |
| N | Uncollected Medicare tax on taxable cost of GTL > $50k (former employees only) |
| P | Excludable moving expense reimbursements paid to active-duty military |
| Q | Nontaxable combat pay |
| R | Employer contributions to Archer MSA |
| S | Employee salary reduction contributions under §408(p) SIMPLE |
| T | Adoption benefits |
| V | Income from exercise of nonstatutory stock options (also in Boxes 1, 3, 5) |
| W | Employer + employee contributions to HSA (sum of both, when made via §125 cafeteria plan) |
| Y | Deferrals under §409A NQDC plan (informational) |
| Z | Income under §409A on NQDC plan (also in Box 1) |
| AA | Designated Roth contributions to §401(k) plan |
| BB | Designated Roth contributions to §403(b) plan |
| CC | (Reserved — formerly HIRE Act 2010) |
| DD | Cost of employer-sponsored health coverage (informational, ACA reporting) |
| EE | Designated Roth contributions to §457(b) governmental plan |
| FF | Permitted benefits under qualified small employer health reimbursement arrangement (QSEHRA) |
| GG | Income from qualified equity grants under §83(i) |
| HH | Aggregate deferrals under §83(i) — current year |
| II | Reserved |

Multiple Box 12 entries are entered in Box 12a, 12b, 12c, 12d (up to four on the W-2 itself; additional codes require a second W-2 for that employee).

### 6.5 Box 14 — Free-text "Other"

Box 14 is the catch-all for items the employer wants to report that don't have a specific box. Common Box 14 entries:

- State Disability Insurance (SDI) withholding — e.g., CA SDI, NJ SDI, NY SDI
- Union dues
- Charitable contributions via payroll
- Educational assistance under §127 (over the $5,250 limit, the excess goes in Box 1; the excluded portion may be informational in Box 14)
- After-tax health insurance premiums
- Auto fringe benefit details
- 414(h) pickup contributions (governmental employers)

### 6.6 Boxes 15-20 — State and Local

| Box | Content |
|---|---|
| 15 | State, employer's state ID number |
| 16 | State wages, tips, etc. |
| 17 | State income tax |
| 18 | Local wages, tips, etc. |
| 19 | Local income tax |
| 20 | Locality name |

If the employee worked in multiple states, multiple rows are reported on the same W-2 (or a second W-2 if more than the form accommodates).

### 6.7 Form W-2c (Corrected Wage and Tax Statement)

Used to correct an already-issued W-2. Common scenarios:

- Wrong Social Security number or name
- Wrong wages or withheld tax amount
- Missed bonus or fringe benefit
- Misallocated state wages

W-2c must be furnished to the employee and to SSA. If the correction also affects FICA, a corresponding Form 941-X may be needed for the affected quarter. If the correction affects FUTA, a corresponding amended Form 940 (no separate "940-X" form — the employer files an amended Form 940 marked "Amended").

The W-3c (Transmittal of Corrected Wage and Tax Statements) accompanies paper W-2c filings to SSA.

---

## 7. Form W-3 — Transmittal of Wage and Tax Statements

The W-3 summarizes the totals from all W-2s filed by the employer. It is required only with paper Copy A W-2 filing. Electronic W-2 filing via SSA BSO does not require a separate W-3 — the totals are computed automatically by the system.

W-3 boxes mirror W-2 boxes 1-19 but as employer-wide totals. Reconciliation to Form 941:

| W-3 box | Should equal sum of four Form 941s, line: |
|---|---|
| Box 1 (wages) | Line 2 (sum of quarters) |
| Box 2 (FIT withheld) | Line 3 (sum of quarters) |
| Box 3 (SS wages) | Line 5a Column 1 (sum of quarters) |
| Box 4 (SS tax) | (Line 5a Col 2 / 2 — employee half only) |
| Box 5 (Medicare wages) | Line 5c Column 1 (sum of quarters) |
| Box 6 (Medicare tax) | (Line 5c Col 2 / 2 + Line 5d Col 2 — employee Medicare + employee Additional Medicare) |

**Reconciliation tip**: SSA matches W-3 totals against the four 941s and sends a "CAWR" (Combined Annual Wage Reporting) discrepancy notice if they disagree. Common reconciliation differences:

- Third-party sick pay — adjusted on 941 Line 8 but appears in W-2 wages
- Group-term life > $50k — fully on W-2 but may have been handled via Schedule B liability rather than Line 2
- Q4 wage payments made on 12/31 but deposited in January — timing
- §3121(v)(2) NQDC FICA timing — wages on Box 3/5 in vesting year, Box 1 in payment year

---

## 8. Form W-4 — Employee's Withholding Certificate (2020+ Redesign)

The Form W-4 was substantively redesigned for 2020 in response to the Tax Cuts and Jobs Act of 2017. The 2020-and-later W-4 has five steps and **no longer uses withholding allowances**.

**Steps**:

1. Step 1 — Personal information and filing status (Single/MFJ/HoH)
2. Step 2 — Multiple jobs or spouse works (three options: online estimator, multiple jobs worksheet, or check the box if only two jobs and they earn roughly equal amounts)
3. Step 3 — Dependents (multiply qualifying children under 17 by $2,000, other dependents by $500)
4. Step 4 — Other adjustments (a) other income (b) deductions in excess of standard deduction (c) extra withholding per pay period
5. Step 5 — Signature

Employees with W-4s filed before 2020 ("pre-2020 W-4") are NOT required to submit a new W-4. The employer continues to compute withholding using the legacy allowances method per Pub 15-T's pre-2020 W-4 tables.

**Default if no W-4 on file**: under Treas. Reg. §31.3402(f)(2)-1(a), if an employee does not furnish a W-4, the employer withholds as if the employee had checked the Single/MFS box on Step 1(c) with no other adjustments — i.e., the highest standard withholding tier.

**Exempt from withholding**: An employee may claim "Exempt" on Form W-4 only if (a) had no federal income tax liability the prior year AND (b) expects to have none the current year. The "Exempt" claim must be renewed annually by February 15. If not renewed, the employer reverts to withholding as Single with no adjustments.

**Withholding adjustments mid-year**: An employee may submit a new W-4 at any time. The employer must put the new W-4 into effect no later than the first payroll period ending on or after the 30th day from receipt (Treas. Reg. §31.3402(f)(3)-1(b)).

---

## 9. Worker Classification — High-Level

The classification of a worker as an employee (W-2) or independent contractor (1099-NEC) determines whether the payroll tax framework in this skill applies at all. The classification is a question of fact under federal common law as codified in §3121(d)(2) and refined by the IRS three-factor test (Rev. Rul. 87-41 with the 20-factor test, modernized to the three-category framework):

1. **Behavioral control** — Does the firm direct and control how the work is done (instructions, training, evaluation systems)?
2. **Financial control** — Does the worker have a significant investment, opportunity for profit/loss, ability to make services available to others, and an unreimbursed business expense risk?
3. **Relationship type** — Written contracts, employee-type benefits (insurance, pension, vacation), permanency of relationship, services as a key activity of the business

**DOL 2024 Worker Classification Rule** (29 C.F.R. Part 795, effective March 11, 2024) — applies for FLSA (wage-and-hour) purposes, not directly for FICA/FUTA, but is persuasive. The rule uses a six-factor "economic realities" test:

1. Opportunity for profit or loss depending on managerial skill
2. Investments by the worker and the potential employer
3. Degree of permanence of the work relationship
4. Nature and degree of control
5. Extent to which the work performed is integral to the potential employer's business
6. Skill and initiative

For payroll tax purposes the IRS common-law test under §3121(d) controls. However, the DOL rule is a useful corroborating analysis, and a worker classified as an employee under the FLSA economic-realities test almost certainly will be classified as an employee for FICA purposes.

**Section 530 relief** (Revenue Act of 1978, P.L. 95-600 §530, never codified in IRC): An employer may avoid retroactive payroll tax liability for misclassification if:

1. The employer had a reasonable basis (judicial precedent, IRS ruling, prior IRS audit on the same issue, or long-standing industry practice)
2. The employer consistently treated the worker (and similar workers) as independent contractors
3. The employer filed all required information returns (Form 1099-NEC) on a basis consistent with treating the worker as an independent contractor

**Voluntary Classification Settlement Program (VCSP)**: Allows an employer to reclassify workers as employees going forward with reduced past-period liability (about 10% of one year's employment tax). Application via Form 8952.

**Refer out**: For independent contractor reporting (1099-NEC), see `us-1099-nec-issuance`. That skill covers the §6041A $600 threshold (rising to $2,000 for 2026 under OBBBA), the §6109 W-9 collection requirement, and the §3406 backup withholding mechanics.

---

## 10. §6656 Failure-to-Deposit Penalty

If the employer fails to deposit employment taxes on time, the penalty under IRC §6656(b)(1) is calculated as a percentage of the underpaid deposit:

| Days late | Penalty rate |
|---|---|
| 1-5 calendar days late | 2% |
| 6-15 calendar days late | 5% |
| 16+ days late, but before the date of IRS notice and demand | 10% |
| Not paid within 10 days after IRS notice and demand | 15% |

The penalty applies to **each deposit**, not to the cumulative shortfall. So an employer who is 16 days late on the first deposit of the quarter and 3 days late on the second deposit owes 10% on the first underpayment and 2% on the second.

Additional consequences:

- **§6651 failure-to-file penalty** — 5% per month, max 25%, if Form 941 itself is filed late
- **§6651 failure-to-pay penalty** — 0.5% per month, max 25%, if the tax shown on the return is not paid by the due date
- **§6672 Trust Fund Recovery Penalty (TFRP)** — 100% of the employee-portion of withheld tax (federal income tax withheld + employee FICA) assessed personally against any "responsible person" who willfully failed to collect, account for, or pay over. This is a personal liability that survives bankruptcy. Common targets: corporate officers, payroll service signatories, anyone with check-signing authority.

**Reasonable cause exception** — the failure-to-deposit penalty carries its own reasonable-cause standard in §6656(a) ('unless it is shown that such failure is due to reasonable cause and not willful neglect'); §6724(a) is the parallel standard for information-return penalties. The penalty may be abated if the employer shows reasonable cause and not willful neglect. Documentation matters: documented banking error, EFTPS outage with same-day re-attempt, payroll service failure with employer due diligence.

**First-Time Abatement (FTA)** — administrative relief under IRM 20.1.1.3.6.1 for employers with a clean compliance history (no penalties in the prior three tax years). One-time relief per taxpayer.

---

## 11. Common Errors and Reconciliation Traps

### 11.1 Social Security wage base mistakes

**Mid-year crossing the $176,100 base** — payroll software should automatically stop the 6.2% Social Security withholding once an employee's YTD wages reach $176,100. Common failure modes:

- Mid-year payroll system change (provider switch) loses the YTD tracker
- Multiple EINs under common ownership not aggregated when they should be (or, conversely, aggregated when they shouldn't)
- Bonus or commission paid through a separate "off-cycle" run that misses the YTD check
- Negative wage adjustments (refund of overpaid wages) that the system doesn't apply to the YTD base

**Multiple jobs at same EIN** — if an employee works for two divisions of the same employer with one EIN, there is one combined wage base. If the divisions have separate EINs and are unrelated, the employee will have excess SS withheld and reclaims it on Schedule 3 Line 11.

### 11.2 HSA, §125, and Box 1/3/5 misalignment

This is the single most common W-2 error in small-business payroll. The rules:

- **HSA contribution via §125 cafeteria plan (payroll deduction with §125 election)** — excluded from Boxes 1, 3, AND 5 (and FUTA)
- **HSA contribution NOT via §125 cafeteria plan** (e.g., employee writes a personal check, claims the deduction on Form 1040 Schedule 1) — Box 1 is unaffected by payroll; if the employer makes a contribution outside §125, the employer contribution is generally taxable wages

The key practical question: was the HSA contribution funded through pre-tax payroll deduction under a written §125 cafeteria plan? If yes → exclude from all three boxes. If no → include in all three.

Many small employers set up "HSA payroll deduction" without a written §125 plan document and incorrectly exclude from Boxes 1, 3, 5. The IRS position (Notice 2002-3 and Pub 969) is clear: no written §125 plan = no §125 exclusion.

### 11.3 Tipped employees — Form 8027 and §3121(q)

Restaurants and other large food/beverage establishments must file **Form 8027** (Employer's Annual Information Return of Tip Income and Allocated Tips) if they:

1. Operate a large food or beverage establishment (more than 10 employees on a typical business day in the prior calendar year), AND
2. Tipping by customers is customary

Form 8027 reports gross receipts, charged tips, and allocated tips. If reported tip income is less than 8% of gross receipts, the employer must allocate the shortfall among directly tipped employees (Box 8 on the W-2).

The **employer FICA on unreported tips** — if the IRS later assesses additional tip income on a §3121(q) Notice and Demand, the employer owes the employer share of FICA on the unreported tips. The notice is reported on Form 941 Line 5f. The employee owes their share separately.

### 11.4 Group-term life insurance over $50,000

§79 excludes the cost of the first $50,000 of employer-provided group-term life insurance from wages. The cost of coverage above $50,000 is imputed income calculated using the IRS Uniform Premium Table I. The imputed amount is:

- Box 1 wages — included
- Box 3 SS wages — included
- Box 5 Medicare wages — included
- Box 12 Code C — reported separately
- Federal income tax withholding — optional (not required); the employer may but is not required to withhold
- FICA — required to withhold employee Social Security and Medicare on the imputed amount

For **former employees** (e.g., retirees still receiving employer-provided life insurance), the employer cannot withhold FICA from a paycheck because there is no paycheck. The uncollected FICA goes in Box 12 Code M (SS) and Code N (Medicare). The former employee pays the uncollected FICA on Form 1040.

### 11.5 Retroactive wage adjustments

If the employer discovers in Q3 that an employee was underpaid in Q1, the corrective wage payment is generally treated as a wage of the period in which it is paid (Q3 deposit and Q3 941). Form 941-X is used only when correcting a previously reported amount, not when paying additional wages discovered late.

For W-2 purposes, the wages are reported in the year paid. If Q1 wages discovered and paid in Q3 of the same year — included in that year's W-2. If discovered and paid the next year — included in next year's W-2.

### 11.6 Common 941 reconciliation errors

- Line 2 (federal income tax wages) does not equal the sum of all W-2 Box 1 amounts because of timing differences (e.g., 12/31 payroll with check date 1/2)
- Line 5a Col 1 (SS wages) > Line 5c Col 1 (Medicare wages) — impossible. Medicare is uncapped, SS is capped. Inverted ratio is always an error.
- Line 5d (Additional Medicare wages × 0.009) reports the WAGES subject to Additional Medicare, not the tax — read the column header carefully
- Schedule B liabilities don't reconcile to Line 12 — typically caused by entering a deposit date instead of the liability date, or by transposing months

### 11.7 §125 cafeteria plan written-plan requirement

A §125 cafeteria plan must have a **written plan document** to be effective. Many small employers offer "pre-tax health insurance" via payroll deduction without a written §125 plan. The IRS may recharacterize the deductions as after-tax, making the withheld premiums taxable wages. This is a high-frequency examination issue. The plan document need not be complex but must exist in writing and be available for IRS inspection.

---

## 12. Worked Examples

### 12.1 Example 1 — Small employer with 3 W-2 employees, quarterly 941

**Facts**: Acme Coffee Roasters LLC (SMLLC taxed as an S-corp — owner is a separate employee/shareholder; for this skill we treat all three as W-2 employees and ignore S-corp specifics). Quarter ending June 30, 2025 (Q2). Three employees:

| Employee | Q2 gross wages | 401(k) pre-tax | §125 health premium | Federal income tax withheld |
|---|---|---|---|---|
| Alice (owner-employee) | $25,000 | $1,500 | $1,200 | $4,200 |
| Bob (shift lead) | $14,000 | $700 | $800 | $1,400 |
| Carla (barista) | $7,200 | $0 | $0 | $360 |
| **Totals** | **$46,200** | **$2,200** | **$2,000** | **$5,960** |

**Computations**:

- Box 1 federal income tax wages (Line 2): $46,200 − $2,200 (401(k)) − $2,000 (§125) = **$42,000**
- Box 3 / Line 5a Col 1 SS wages: $46,200 − $2,000 (§125 only; 401(k) is NOT excluded from SS) = **$44,200**
- Box 5 / Line 5c Col 1 Medicare wages: $44,200 (same as SS, none crossed $176,100) = **$44,200**

**Form 941 Q2**:

| Line | Item | Amount |
|---|---|---|
| 1 | Employees on June 12 payroll | 3 |
| 2 | Wages, tips, and other compensation | $42,000 |
| 3 | Federal income tax withheld | $5,960 |
| 5a Col 1 | SS wages | $44,200 |
| 5a Col 2 | SS tax (× 0.124) | $5,480.80 |
| 5c Col 1 | Medicare wages | $44,200 |
| 5c Col 2 | Medicare tax (× 0.029) | $1,281.80 |
| 5d Col 1 | Additional Medicare wages (none > $200k) | $0 |
| 5d Col 2 | Additional Medicare tax | $0 |
| 5e | Total FICA | $6,762.60 |
| 6 | Total before adjustments (3 + 5e) | $12,722.60 |
| 7 | Fractions of cents adjustment | $0 |
| 10 | Total after adjustments | $12,722.60 |
| 12 | Total taxes after credits | $12,722.60 |

**Deposit schedule**: 2025 lookback period is 7/1/2023 – 6/30/2024. If Acme's total Form 941 liability over that period was under $50,000 → monthly depositor. Each month's accumulated tax is due by the 15th of the following month. Q2 monthly liabilities (assumed approximately equal): roughly $4,240 per month, all under $100,000 → next-day rule not triggered.

| Liability month | Deposit due |
|---|---|
| April 2025 | May 15, 2025 |
| May 2025 | June 16, 2025 (15th is Sunday) |
| June 2025 | July 15, 2025 |

**Form 941 Q2 due**: July 31, 2025 (or August 11, 2025 — Aug 10 is Sunday — if all deposits timely).

### 12.2 Example 2 — Mid-size employer crossing $176,100 wage base mid-year for one executive

**Facts**: TechCo Inc. has 8 employees in 2025. Carol (CEO) earns $300,000/year, paid as $25,000/month (no commissions, no bonus). All other employees earn under $176,100. We focus on the wage-base crossover for Carol.

**Carol's monthly wages** = $25,000.

| Month | Cumulative gross wages | SS wages in this month | SS wages cumulative | SS withheld this month |
|---|---|---|---|---|
| January | $25,000 | $25,000 | $25,000 | $1,550.00 |
| February | $50,000 | $25,000 | $50,000 | $1,550.00 |
| March | $75,000 | $25,000 | $75,000 | $1,550.00 |
| April | $100,000 | $25,000 | $100,000 | $1,550.00 |
| May | $125,000 | $25,000 | $125,000 | $1,550.00 |
| June | $150,000 | $25,000 | $150,000 | $1,550.00 |
| July | $175,000 | $25,000 | $175,000 | $1,550.00 |
| August | $200,000 | **$1,100** (only $176,100 − $175,000) | $176,100 | $68.20 |
| September | $225,000 | $0 | $176,100 | $0 |
| October | $250,000 | $0 | $176,100 | $0 |
| November | $275,000 | $0 | $176,100 | $0 |
| December | $300,000 | $0 | $176,100 | $0 |

**SS wages for the year**: $176,100 (capped). Total employee SS withheld: $176,100 × 6.2% = $10,918.20.

**Medicare and Additional Medicare**:

| Month | Cumulative wages | Medicare wages this month | Additional Medicare 0.9% withheld? |
|---|---|---|---|
| Jan-Aug | up to $200,000 | $25,000/month | No (cumulative wages threshold not crossed) |
| August (end) | $200,000 | (No Add'l Medicare yet — threshold is "in excess of $200,000") |
| September | $225,000 | $25,000 | Yes — $25,000 × 0.9% = $225 (because YTD wages now exceed $200,000; the employer withholds 0.9% on the portion of wages in the pay period that causes total to exceed $200,000 and on all wages thereafter in the calendar year) |
| Oct, Nov, Dec | $25,000/month | Yes — $225/month |

**Total Additional Medicare withheld in 2025 by employer**: $100,000 × 0.9% = $900 (on wages from $200,001 to $300,000).

**Form 941 Q3 reporting for Carol** (other employees omitted for clarity):

- Line 5a Col 1 (SS wages): July = $25,000; August = $1,100; September = $0 → Q3 SS wages = **$26,100**
- Line 5c Col 1 (Medicare wages): Q3 = $25,000 × 3 = **$75,000**
- Line 5d Col 1 (Additional Medicare wages subject to 0.9%): September only = **$25,000**
- Line 5d Col 2 (Additional Medicare tax): $25,000 × 0.009 = **$225**

**W-2 for Carol**:

- Box 1: $300,000 (assuming no pre-tax 401(k) or §125)
- Box 3: **$176,100** (capped at the wage base)
- Box 4: $176,100 × 6.2% = $10,918.20
- Box 5: **$300,000** (uncapped Medicare)
- Box 6: $300,000 × 1.45% = $4,350 PLUS $100,000 × 0.9% = $900 = **$5,250** total

**Common error**: Reporting Box 3 as $300,000 (forgetting the cap) or as $200,000 (confusing the Additional Medicare threshold with the SS wage base). Always Box 3 = lesser of (FICA wages, $176,100); Box 5 = full FICA wages with no cap.

### 12.3 Example 3 — Employer in California (credit reduction state) computing FUTA

**Facts**: BeachCo LLC pays wages in California only. 2025 calendar year. 12 employees. Total taxable wages per employee (first $7,000 each):

| Employees | First $7,000 each | Total FUTA-taxable wages |
|---|---|---|
| 12 employees who each earned > $7,000 | $7,000 × 12 | $84,000 |

**Computation assuming CA is a credit reduction state for 2024 at 0.9% (final 2024 status finalized November 2024)**:

- Gross FUTA: $84,000 × 6.0% = $5,040.00
- State UI credit: maximum 5.4% × $84,000 = $4,536.00, **less** the credit reduction adjustment
- Credit reduction (0.9%): $84,000 × 0.9% = $756.00 — this is the additional FUTA owed
- Effective FUTA: ($84,000 × 0.6%) + ($84,000 × 0.9%) = $504 + $756 = **$1,260.00**
- Per employee: $1,260 / 12 = $105.00

**Form 940 reporting**:

- Part 2 Line 7 (Total FUTA wages): $84,000
- Part 2 Line 8: Credit reduction states → "Yes" → attach Schedule A
- **Schedule A (Form 940)**: Check the CA box; enter $84,000 in the CA row; credit reduction rate 0.009; credit reduction amount $756
- Total FUTA tax (Line 12 of Form 940): $84,000 × 0.006 = $504 (base) plus $756 (Schedule A credit reduction) = **$1,260.00**

**FUTA deposit schedule**: Total annual FUTA liability $1,260 > $500 — quarterly deposits required when accumulated liability exceeds $500 within the quarter.

Assuming relatively even payroll across the year and the wage base concentration in Q1-Q2:

- Q1 (Jan-Mar): about $42,000 of FUTA-taxable wages → $42,000 × 0.6% = $252 (no credit reduction is added until year-end) — accrued $252 < $500 → carry forward
- Q2 (Apr-Jun): about $42,000 FUTA-taxable wages → $252 — cumulative through Q2 = $504 > $500 → **deposit by July 31** → $504
- Q3, Q4: zero FUTA-taxable wages (all employees over $7,000) → no additional deposit until year-end
- Year-end: credit reduction of $756 added at filing → **paid with Form 940 by January 31, 2026**

(The credit reduction $756 is paid with the return rather than via quarterly deposit, because the credit reduction adjustment is computed on Schedule A at year-end. The IRS instructions for Form 940 confirm this treatment — see line 16 instructions, "if Line 9 or 10 applies"… effectively, the additional credit-reduction FUTA tax is owed at the time of filing.)

**Form 940 due date**: January 31, 2026 (or February 10, 2026 if all deposits including the $504 Q2 deposit were timely).

**Worked-example note for the reviewer**: The 2025 credit reduction status of CA must be confirmed against the DOL November 2025 announcement before finalizing. If CA repaid its Title XII loans during 2025, the credit reduction may not apply.

### 12.4 Example 4 — Reconciliation of all four 941s to the W-3 (brief)

**Facts**: Same TechCo Inc. as Example 2, full year, 8 employees. The full year totals across the four 941s should match the W-3:

| Item | Sum of four 941s | W-3 totals |
|---|---|---|
| Total wages (Line 2) | $1,800,000 (illustrative) | Box 1 = $1,800,000 |
| Federal income tax withheld (Line 3) | $360,000 | Box 2 = $360,000 |
| SS wages (Line 5a Col 1) | $1,408,800 (Carol capped at $176,100; her actual wages are $567,300, so the 7 others total $1,232,700, each ≤ the $176,100 wage base) | Box 3 = $1,408,800 |
| SS tax (Line 5a Col 2) | $174,691.20 (12.4% × $1,408,800) | Box 4 = $87,345.60 (employee half only) |
| Medicare wages (Line 5c Col 1) | $1,800,000 (uncapped) | Box 5 = $1,800,000 |
| Medicare tax (Line 5c Col 2 + 5d Col 2) | Regular Medicare 2.9% × $1,800,000 = **$52,200**; Additional Medicare 0.9% × $367,300 (only Carol's wages over $200,000) = **$3,305.70**; total $55,505.70 | Box 6 = employee regular half $26,100 (1.45% × $1,800,000) + Additional Medicare $3,305.70 = **$29,405.70** |

**Note on Box 4 / Box 6 vs 941**: Box 4 and Box 6 on W-2/W-3 are the EMPLOYEE half only. Form 941 Line 5a Col 2 (SS) and Line 5c Col 2 (regular Medicare) report the COMBINED employer + employee, so halve them for the W-2 boxes; Line 5d Col 2 (Additional Medicare) is 100% employee, so it is added to Box 6 in full, not halved. Additional Medicare applies only to the portion of an individual employee's wages above $200,000 — here only Carol crosses that threshold.

If W-3 totals don't match the four 941s, the SSA sends a CAWR discrepancy notice. The employer typically has 45 days to respond with reconciliation.

---

## 13. Self-Checks Before Reviewer Sign-Off

Before delivering Form 941, Form 940, or W-2/W-3 outputs:

1. **Wage base cap check** — Confirm Box 3 SS wages ≤ $176,100 per employee for 2025. Cumulative across the year, including any predecessor-employer credit if applicable.
2. **Box 1 vs Box 3/5 reconciliation** — Identify and document every difference between Box 1, Box 3, and Box 5 for each employee. Common drivers: 401(k), Roth 401(k), §125, HSA, GTL > $50k. Each driver should be either reported in Box 12 (codes D, AA, W, C) or be implicit (§125).
3. **§125 written-plan check** — If the employer excluded health premiums, dental, vision, or HSA contributions from any Box, confirm a written §125 cafeteria plan document exists.
4. **Additional Medicare 0.9%** — For each employee with YTD wages > $200,000, confirm the employer withheld 0.9% on the portion exceeding $200,000 and reported on Line 5d.
5. **Quarterly 941 sum = W-3** — Reconcile sum of four 941s to W-3 totals; document any differences (typical: Q4 12/31 payroll check-dated 1/2 of next year, third-party sick pay).
6. **Deposit schedule** — Identify the lookback period (7/1 of two years prior through 6/30 of prior year) and the monthly vs semiweekly classification. Confirm next-day rule was not triggered.
7. **Schedule B (if semiweekly)** — Each daily liability matches the corresponding EFTPS deposit within the allowed days.
8. **Form 940 Schedule A** — If any wages were paid in a credit reduction state, Schedule A is attached and the credit reduction is applied.
9. **2024 credit reduction states** — For Form 940 filed in January 2025 for tax year 2024, confirm against DOL November 2024 announcement (CA 0.9%, NY 0.9%, VI 4.2%, others as applicable).
10. **2025 credit reduction states** — For Form 940 to be filed January 2026 for tax year 2025, confirm against DOL November 2025 announcement before finalizing.
11. **W-2 due January 31** — Both employee copies and SSA filing.
12. **10+ information return e-file mandate** — If the employer has 10+ information returns in aggregate (W-2, 1099-NEC, 1099-MISC, etc.), confirm electronic filing via SSA BSO and IRS IRIS/FIRE.
13. **EFTPS enrollment** — Confirm employer is enrolled and has the PIN; no paper Form 8109 attempted.
14. **§6656 deposit penalty exposure** — Identify any late deposits and document reasonable-cause facts.
15. **Worker classification** — For any disputed 1099 contractor, document the §3121(d) common-law factors and §530 relief eligibility.
16. **W-4 on file** — Each employee has a current W-4; "Exempt" claims renewed annually by February 15.
17. **Form 944 eligibility** — If the IRS notified the employer of 944 eligibility and the employer is filing 941, document the conversion request (or vice versa).

---

## 14. Cross-References

- `us-1099-nec-issuance` — for independent contractor reporting, the §6041A threshold (2026 increase to $2,000 per OBBBA), §3406 backup withholding, and the W-9 collection requirement
- `us-schedule-c-and-se-computation` — for self-employed owner SE tax (no 941 obligation for the sole proprietor's own earnings)
- `us-quarterly-estimated-tax` — for individual Form 1040-ES safe-harbor estimated tax (separate from Form 941 deposits)
- `us-tax-workflow-base` — for the workflow runbook, intake form, and global refusal catalogue
- `us-federal-return-assembly` — when the employer is a sole proprietor and the payroll output feeds into the Schedule C deduction for "wages" (Line 26)

---

## 15. Provenance

This skill is based on the following primary sources, all current as of November 15, 2025:

**Statutory**:

- IRC §3101 (FICA employee tax), §3111 (FICA employer tax), §3121 (FICA wages and definitions), §3301-3311 (FUTA), §3401 (income tax withholding wages), §3402 (income tax withholding), §3406 (backup withholding), §6011 (return filing), §6051 (W-2 furnishing), §6071 (timely filing), §6109 (TIN), §6302 (deposit rules), §6656 (failure-to-deposit penalty), §6672 (TFRP), §6721/§6722 (information return penalties)
- Social Security Act §230 (wage base computation)
- One Big Beautiful Bill Act of 2025 (P.L. 119-21, July 4, 2025) — for the 2026 1099-NEC threshold change to $2,000 (referenced via `us-1099-nec-issuance`)
- Inflation Reduction Act of 2022 (P.L. 117-169) — for the §41(h) qualified small business payroll tax credit Medicare-portion increase to $250,000

**Regulatory**:

- Treas. Reg. §31.3402(f) (W-4 administration)
- Treas. Reg. §31.6302-1 (deposit schedule, EFTPS mandate)
- Treas. Reg. §31.6071(a)-1 (10-day timely-deposit extension)
- Treas. Reg. §31.6402(a)-2 (overcollected tax refund)
- Treas. Reg. §31.6051-1 (W-2 furnishing)
- T.D. 9972 (final regulations on electronic filing of information returns, effective for returns required to be filed on or after January 1, 2024, reducing the threshold from 250 to 10 aggregate returns)
- 29 C.F.R. Part 795 (DOL Worker Classification rule, effective March 11, 2024) — referenced

**IRS Publications and Forms**:

- Pub 15 (Circular E), Employer's Tax Guide, 2025 edition
- Pub 15-A, Employer's Supplemental Tax Guide, 2025 edition
- Pub 15-B, Employer's Tax Guide to Fringe Benefits, 2025 edition
- Pub 15-T, Federal Income Tax Withholding Methods, 2025 edition
- Pub 51 (Circular A), Agricultural Employer's Tax Guide, 2025 edition (for §6 Form 943)
- Pub 80 (Circular SS), for US Territory employers (not in scope, listed for completeness)
- Pub 926, Household Employer's Tax Guide (not in scope, listed for completeness)
- Pub 969, Health Savings Accounts and Other Tax-Favored Health Plans
- Form 941 (2025 quarterly revisions) and instructions
- Form 940 (2024 — filed January 2025) and 2025 (filed January 2026) instructions
- Schedule A (Form 940) — Multi-State Employer and Credit Reduction Information
- Schedule B (Form 941) — Report of Tax Liability for Semiweekly Schedule Depositors
- Schedule R (Form 941) — Allocation Schedule for Aggregate Form 941 Filers (PEO/CPEO)
- Form W-2 and General Instructions for Forms W-2 and W-3 (2025)
- Form W-3 and W-3c
- Form W-2c
- Form W-4 (2025 revision)
- Form 8959 (Additional Medicare Tax)
- Form 8027 (Tip income)
- Form 8974 (Qualified Small Business Payroll Tax Credit)

**Administrative**:

- Rev. Rul. 87-41 (20-factor worker classification test) — superseded for analytical structure but the underlying common-law factors remain authoritative under §3121(d)(2)
- Rev. Proc. 2024-40 (2025 inflation adjustments for income tax brackets, applied to Pub 15-T withholding tables)
- Notice 2002-3 (cafeteria plan written-plan requirement)
- IRM 20.1.1 (Penalty Handbook) — for First-Time Abatement and reasonable-cause procedures
- DOL Credit Reduction State announcements at oui.doleta.gov/unemploy/futa_credit.asp (November 2024 for tax year 2024 Form 940; November 2025 for tax year 2025 Form 940)
- SSA Fact Sheet on 2025 Social Security Changes (October 10, 2024) — for the $176,100 wage base
- IRS news release IR-2024-273 and Rev. Proc. 2024-40 for 2025 figures

**Verification status**: The $176,100 wage base, the 0.6%/1.5% effective FUTA rates, the credit reduction state list (CA, NY, VI, CT for 2024), and the 0.9% Additional Medicare employer withholding threshold of $200,000 are all verified against the cited primary sources as of November 15, 2025. The 2025 final credit reduction state list (for Form 940 to be filed January 2026) must be re-verified against the DOL November 2025 announcement before any 2025 Form 940 is finalized. The 2026 backup withholding rate, 2026 SS wage base, and 2026 OBBBA-driven 1099-NEC threshold are referenced as scope notes; this skill does not produce 2026 returns.

**Reviewer**: pending. This skill has not yet been reviewed by a Circular 230-credentialed practitioner. No Form 941, Form 940, W-2, or W-3 output should be filed without independent review and signature by a CPA, EA, or attorney licensed to practice before the IRS.

---

<!-- openaccountants-cta-block -->

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://www.openaccountants.com/network).

<!-- openaccountants-mcp-cta -->

## The accountant-verified version lives in the connector

This file is the open, **research-grade draft**. The **accountant-verified**
version of this skill is **not published to GitHub** — it is delivered free
through the OpenAccountants MCP connector, where your AI agent loads the
verified rules together with the name of the accountant who signed them off.

**→ Install the free connector:** <https://www.openaccountants.com/connect>
**MCP endpoint:** `https://www.openaccountants.com/api/mcp`

## Changelog
- **2026-07-06** — Worked-example arithmetic pass (completes the §12.4 item flagged 2026-07-05). Example 4 reconciliation: corrected the Medicare figures — regular Medicare is 2.9% × $1,800,000 = $52,200 (was $53,100), and Additional Medicare is 0.9% only on the portion of an individual's wages above $200,000 (here only Carol, whose $567,300 gives 0.9% × $367,300 = $3,305.70, not a flat $900); Box 6 employee Medicare is $26,100 + $3,305.70 = $29,405.70 (was $27,900). Made Carol's $567,300 wages explicit so the reconciliation is followable. The HSA/§125 FICA-exclusion table remains flagged for a separate pass.
- **2026-07-05** — Payroll corrections (Fable review, verified against IRS i940/i941 + 2025 SS/FUTA figures): T.D. 9972 dated Feb 2023 (not "2024 IRS final regs"); the $2,500 de-minimis deposit test is disjunctive (current OR prior quarter); backup-withholding drafting residue cleaned to a flat 24% for 2025 (§3406; TCJA rates made permanent by OBBBA §70101); FUTA successor wage-base credit cited to §3306(b)(1) not §3306(c)(8); Form 941-X interest-free-adjustment timing tied to when the error is ascertained; reasonable-cause standard split between §6656(a) (deposits) and §6724(a) (info returns). FLAGGED: §12.4 Example 4 reconciliation arithmetic and the HSA/§125 FICA-exclusion table need a follow-up pass.
