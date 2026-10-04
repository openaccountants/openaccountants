---
name: ca-payroll
description: Tier 2 California content skill for employer payroll compliance covering tax year 2025. Includes the 13.3% top PIT bracket with 1% mental health surtax over $1M, SDI 1.2% with no wage cap (SB 951), Form DE 9/DE 9C quarterly returns, the CalSavers retirement mandate for 1+ employees, AB5 / ABC test contractor classification, DE 542 reporting for $600+ contractors, supplemental wage withholding at 10.23%, ETT 0.1% on first $7,000, and SUI with $7,000 base and 1.5-6.2% experience-rated range. Covers federal payroll interactions and CA labor-code wage statement requirements.
jurisdiction: US-CA
tax_year: 2026
last_updated: 2026-10-03
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# California payroll for employers: PIT withholding, SDI, UI, ETT, filings and final pay

Figures are for tax year 2026. This Guide covers the four California payroll taxes an employer handles through the Employment Development Department (EDD): California Personal Income Tax (PIT) withholding, State Disability Insurance (SDI), Unemployment Insurance (UI) and the Employment Training Tax (ETT). It also covers the quarterly and annual filings, deposits, new hire and contractor reports, and the final pay rules enforced by the Labor Commissioner. Every rate below comes from an EDD or Department of Industrial Relations page. California income tax brackets for the annual return are set by the Franchise Tax Board; confirm them on ftb.ca.gov, because this Guide does not reproduce them.

## 1. Scope

This Guide covers California employer payroll for 2026:

- PIT withholding from wages, using the 2026 EDD withholding schedules (Method A and Method B) and the flat rates for supplemental wages.
- SDI, withheld from the employee. Paid Family Leave (PFL) is part of SDI, not a separate deduction.
- UI, paid by the employer on the first part of each employee's wages, at a rate set each year.
- ETT, paid by the employer on the same wage base as UI, by employers with a positive UI reserve account balance and employers subject to section 977(c) of the California Unemployment Insurance Code.
- The Quarterly Contribution Return and Report of Wages (DE 9) and its continuation (DE 9C), payroll tax deposits (DE 88), the e-file and e-pay mandate, and the Notice of Contribution Rates (DE 2088).
- The Employee's Withholding Allowance Certificate (DE 4).
- New hire reporting (DE 34) and independent contractor reporting (DE 542).
- Worker classification under the ABC test, as EDD applies it.
- Final pay timing and the waiting time penalty, vacation payout, tips and the minimum wage, from the Labor Commissioner's pages.

**Out of scope (refuse or refer out):**

- Federal employment tax filing (Forms 941, 940, 943, 944, W-2 and W-3). Use `us-form-941-940-payroll`, which a named accountant maintains, or refer to a payroll professional.
- Other states' payroll rules, and an employee who works partly in another state. Use `us-state-payroll-matrix` for the state-by-state map; refer multistate apportionment to a payroll professional.
- Public-sector and governmental employer payroll.
- Agricultural employers and household employers (EDD publishes a separate household employer guide).
- Garnishment and child-support withholding beyond noting that the obligation exists.
- ERISA retirement plan administration and the CalSavers program (see section 9).
- Visa, totalization-agreement and other cross-border payroll cases.
- Stock option and restricted stock planning, section 83(b) elections and section 409A deferred compensation. Use `us-equity-compensation-restricted-stock-units-and` for the federal side.
- San Francisco, Los Angeles and other city business taxes (see section 14).

**Prerequisites:** Load this Guide with `us-tax-workflow-base`. A credentialed reviewer (Enrolled Agent, CPA or attorney) or an experienced California payroll practitioner reviews every output before it reaches the employer or EDD.

## 2. The Four California Employer Payroll Taxes (Quick Map)

EDD's DE 44 (California Employer's Guide 2026) sets out who pays each tax and on which wages. Rates for 2026 come from EDD's rates page in the first table below.

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding |
| UI rate for a new employer, for two to three years | 3.4% | "New employers are assigned a 3.4 percent UI rate for two to three years." |
| UI rate range in 2026 (Schedule F+) | 1.5% to 6.2% | "The UI rate schedule for 2026 is Schedule F+. This is Schedule F, plus a 15 percent emergency surcharge, rounded to the nearest tenth. Schedule F+ provides for UI contribution rates from 1.5 percent to 6.2 percent." |
| UI taxable wage limit, per employee, per calendar year | USD 7,000 | "The taxable wage limit is $7,000 per employee, per calendar year." |
| ETT rate for 2026 | 0.1% | "The ETT rate for 2026 is 0.1 percent." |
| ETT taxable wage limit, per employee, per calendar year | USD 7,000 | "The ETT taxable wage limit is $7,000 per employee, per calendar year." |
| SDI withholding rate for 2026 | 1.3% | "The SDI withholding rate for 2026 is 1.3 percent." |
| SDI taxable wage limit | none | "Effective January 1, 2024, all wages are subject to SDI contributions." |

| Tax | Who pays | Wages taxed |
| --- | --- | --- |
| PIT withholding | Employee (employer withholds) | No limit; withheld under the employee's DE 4 and the EDD schedules |
| SDI (includes PFL) | Employee (employer withholds) | No limit |
| UI | Employer | First part of each employee's wages each calendar year, up to the UI limit in the table above |
| ETT | Employer with a positive UI reserve balance, or subject to section 977(c) | Same limit as UI |

The maximum per employee, per calendar year, printed in DE 44:

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf |
| Maximum UI per employee, at the highest UI rate | USD 434 | "Maximum Tax $434 per employee," (the UI maximum, worked at the highest UI rate on the wage limit) |
| Maximum ETT per employee | USD 7 | "($7,000 x .001)" (the ETT maximum, worked at the wage limit) |
| SDI rate as printed in DE 44 | 1.3% | "1.3 percent (.013)" (SDI column of the State Payroll Taxes table; the PDF columns interleave) |
| Flat PIT rate on bonuses and stock options paid separately | 10.23% | "Bonuses and stock options 10.23 percent (.1023)" |
| Flat PIT rate on other supplemental wages paid separately | 6.6% | "severance, and 6.6 percent (.066) vacation pay" |
| PIT accumulated below this amount: quarterly deposit | USD 350 | "Less than $350 Any payday Quarterly" |
| PIT from USD 350 to this amount (federal next-day or semi-weekly depositor): monthly deposit | USD 400 | "$350 to $400 Any payday 15th of the following month" |
| Penalty on late payroll tax payments | 15% | "A penalty of 15 percent plus interest will be charged on late payroll tax payments." |
| Paper DE 9 (or other tax return) penalty | USD 50 | "Tax Return: $50 per return" |
| Paper DE 9C penalty | USD 20 | "Wage Report: $20 per wage item" |
| Fine on conviction for failing to withhold and send payroll taxes | USD 1,000 | "the person or employer can be fined up to $1,000 or sentenced to jail for up to one year" |
| DE 542 reporting threshold for a contractor | USD 600 | "within 20 calendar days of either paying an independent contractor $600 or more for services performed or entering into a contract for $600 or more, whichever is earlier" |
| Wages paid in a calendar quarter above which a commercial employer registers (DE 1) within 15 calendar days | USD 100 | "Within 15 calendar days after paying more than $100" (DE 1 row of 2026 Forms and Due Dates; the PDF columns interleave) |
| Paper payroll tax deposit (DE 88) penalty | 15% | "Payroll Tax Deposit: 15% of amount due" |

Federal taxes run alongside these. Federal income tax withholding, social security, Medicare, Form 941 and Form 940 belong to `us-form-941-940-payroll`. This Guide states no federal rates.

What employers get wrong most often:

- SDI has no wage ceiling. Since 1 January 2024 every dollar of wages is subject to SDI, so a payroll system that still stops SDI at an old cap under-withholds from high earners (section 4.3).
- The SDI rate changes every year. It is the 2026 rate in the first table, not last year's rate.
- UI and ETT stop at the wage limit, per employee, per calendar year. A new calendar year starts the count again.
- ETT is not paid by every employer. It applies to employers with a positive UI reserve account balance and employers subject to section 977(c). The DE 2088 shows the employer's rate.
- A bonus paid with regular wages must be added to the regular wages and withheld under the schedules. The flat bonus rate applies only to a payment made separately.

## 3. California PIT Withholding

### 3.1 Authority and Method

- **Two methods.** EDD publishes two methods for PIT withholding: Method A (Wage Bracket Table Method) and Method B (Exact Calculation Method). EDD limits Method A to wages or salaries under one million dollars, so use Method B above that. Both are on EDD's rates page and in DE 44. [2026 Method B](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/26methb.pdf)
- **The Method B steps.** Step 1: if gross wages are at or below the low income exemption amount, withhold nothing. Step 2: subtract the estimated deduction amount for any additional allowances claimed on a DE 4. Step 3: subtract the standard deduction. Step 4: apply the tax rate table for the payroll period and marital status. Step 5: subtract the exemption allowance credit for the regular allowances claimed. [2026 Method B](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/26methb.pdf)
- **Married employees with working spouses.** EDD recommends using the single filing status, or an additional flat amount of withholding, to avoid under-withholding. [2026 Method B](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/26methb.pdf)

### 3.2 2026 California Withholding Schedules (Method B)

The figures below are EDD's 2026 withholding schedule amounts, not the Franchise Tax Board's income tax brackets. Do not use them to compute an employee's annual tax. For the annual return, confirm the brackets on ftb.ca.gov.

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://edd.ca.gov/siteassets/files/pdf_pub_ctr/26methb.pdf |
| Low income exemption, monthly, single | USD 1,575 | Table 1, Monthly row: "Monthly $1,575 $1,575 $3,149 $3,149" |
| Low income exemption, monthly, married with 2 or more allowances or head of household | USD 3,149 | Table 1, same row |
| Standard deduction, monthly, single | USD 476 | Table 3, Monthly row: "Monthly $476 $476 $951 $951" |
| Standard deduction, monthly, married with 2 or more allowances or head of household | USD 951 | Table 3, same row |
| Exemption allowance credit, monthly, 1 allowance | USD 14.03 | Table 4, row for 1 allowance, Monthly column: "$14.03" |
| Monthly single (Table 20): taxable income not over USD 924 | 1.100% | "$924 1.100%" |
| Over USD 924, not over USD 2,188 | 2.200% of the excess over USD 924, plus USD 10.16 | "$924 $2,188 2.200% $924 $10.16" |
| Over USD 2,188, not over USD 3,454 | 4.400% of the excess over USD 2,188, plus USD 37.97 | "$2,188 $3,454 4.400% $2,188 $37.97" |
| Over USD 3,454, not over USD 4,796 | 6.600% of the excess over USD 3,454, plus USD 93.67 | "$3,454 $4,796 6.600% $3,454 $93.67" |
| Over USD 4,796, not over USD 6,060 | 8.800% of the excess over USD 4,796, plus USD 182.24 | "$4,796 $6,060 8.800% $4,796 $182.24" |
| Over USD 6,060, not over USD 30,956 | 10.230% of the excess over USD 6,060, plus USD 293.47 | "$6,060 $30,956 10.230% $6,060 $293.47" |
| Over USD 30,956, not over USD 37,148 | 11.330% of the excess over USD 30,956, plus USD 2,840.33 | "$30,956 $37,148 11.330% $30,956 $2,840.33" |
| Over USD 37,148, not over USD 61,912 | 12.430% of the excess over USD 37,148, plus USD 3,541.88 | "$37,148 $61,912 12.430% $37,148 $3,541.88" |
| Over USD 61,912, not over USD 83,334 | 13.530% of the excess over USD 61,912, plus USD 6,620.05 | "$61,912 $83,334 13.530% $61,912 $6,620.05" |
| Over USD 83,334 | 14.630% of the excess over USD 83,334, plus USD 9,518.45 | "14.630% $83,334 $9,518.45" |
| Annual single (Table 5): top band, taxable income over USD 1,000,000 | 14.630% | "N/A 14.630% $1,000,000" (the PDF prints two tables side by side) |

Other payroll periods (weekly, biweekly, semi-monthly, quarterly, annual, daily) and the married and head of household tables are in the same PDF. Use the table for the actual payroll period.

### 3.3 Form DE 4: Employee's Withholding Allowance Certificate

- **Both forms are needed.** A new hire, and an existing employee who changes withholding, must complete and sign both the federal Form W-4 and the DE 4. Since 2020 the federal W-4 has no allowances, so it cannot drive California withholding. [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding)
- **No DE 4 on file.** If an employee does not give the employer a properly completed DE 4, the employer must withhold "as if the employee were single and claiming zero withholding allowances". The live version of this Guide said to fall back to the federal W-4; that is wrong for anyone hired or changing withholding since 2020. [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding)
- **Old W-4s.** An employee who gave a Form W-4 before 2020 and has no change does not have to submit a new form; keep using the earlier form. [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding)
- **Copies to the Franchise Tax Board.** Any rule on sending a DE 4 with many allowances to the Franchise Tax Board is a Franchise Tax Board rule; confirm it on ftb.ca.gov.

### 3.4 Supplemental Wage Withholding (flat rates in the DE 44 table)

- **What counts.** Supplemental wages include, but are not limited to, bonuses, overtime pay, sales awards, commissions, stock options, vacation pay, and dismissal or severance pay. The stock option rate applies only to stock options that are wages subject to PIT withholding. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
- **Paid at the same time as regular wages.** The employer is "required to treat the sum of the payments as regular wages" and withholds under the schedules for the regular payroll period. The flat rates are not available. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
- **Paid separately.** The employer may choose either option. Option 1: compute withholding on the supplemental payment plus the current regular wages under the schedules, then subtract the PIT already withheld from the regular wages. Option 2: withhold a flat rate "without allowing for any withholding allowances": the bonus and stock option rate, or the other supplemental wages rate (DE 44: "such as overtime pay, commissions, sales awards, severance, and vacation pay"), both in the DE 44 table in section 2. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
- **Stock options.** Whether an option is wages subject to PIT withholding depends on the type of option; EDD's Information Sheet DE 231SK explains statutory and nonstatutory options. [DE 231SK](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de231sk.pdf)

### 3.5 AUDIT FLASH POINT: Under-withholding on Large Bonuses and Equity

The flat bonus rate is a withholding rate, not the employee's tax. EDD's own annual Method B table withholds at its top band rate on taxable income over USD 1,000,000 (table in section 3.2), which is well above the flat bonus rate. A high earner paid a large bonus or equity income at the flat rate can therefore end the year owing California tax on the annual return.

**Red flags during payroll review:**
- Large bonuses or equity income paid separately and withheld only at the flat bonus rate.
- Executives whose annual wages reach the top band of the annual Method B table.

**Mitigation:**
- The employee asks for additional withholding on the DE 4 (DE 44 describes additional PIT withholding requests).
- The employer uses Option 1 (aggregate method) for a separately paid bonus instead of the flat rate.
- The employee makes California estimated payments; see `ca-estimated-tax-540es`. DE 44 warns that quarterly estimates paid by an employee to the Franchise Tax Board instead of proper withholding "may result in an assessment to the employer". [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)

### 3.6 Wages Subject to California Withholding

- **Box 16 usually matches Box 1, but not always.** DE 44 says the California PIT wages on Form W-2 Box 16 are generally the same as federal Box 1 wages, but may differ because of federal and California differences in the definition of employee and of wages. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
- **HSA contributions.** EDD's Types of Payments table treats contributions to a Health Savings Account (HSA) as "Subject" to UI and ETT, SDI and PIT withholding, and "Reportable" as PIT wages, whether or not they are made under a section 125 cafeteria plan. California payroll that excludes HSA contributions the way federal payroll does understates California wages. The information sheet is revision 1 of June 2016; it is the current version on EDD's forms page. [DE 231TP](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de231tp.pdf)
- **Other differences.** For any other payment type (fringe benefits, lodging, life insurance, tuition programs), look up the row in DE 231TP before setting up the pay code. The live version of this Guide stated a rule for registered domestic partner health benefits; no allowed page confirms it, so it is removed.

## 4. State Disability Insurance (SDI)

### 4.1 SDI: No Wage Ceiling Since 2024

- **No cap.** "Effective January 1, 2024, Senate Bill 951 removed the taxable wage limit and maximum withholdings for each employee subject to State Disability Insurance (SDI) contributions." This continues in 2026: the 2026 rate in the first table in section 2 applies to all wages. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
- **Who pays.** SDI is withheld from the employee. The employer does not pay it from its own funds. It is reported with PIT on the DE 9 and DE 9C. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
- **Form W-2.** Enter "The abbreviation CASDI or SDI withheld" in Box 14 (Other). An employer with an approved Voluntary Plan enters VPDI and the amount withheld instead. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
- **The rate changes yearly.** EDD's history table shows the recent SDI rates and the last wage cap:

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de3395.pdf |
| SDI rate 2025 (no wage limit) | 1.2% | "2025 7,000 None1 3.4 6.2 0.1 1.2" |
| SDI rate 2024 (no wage limit) | 1.1% | "2024 7,000 None1 3.4 6.2 0.1 1.1" |
| SDI rate 2023 | 0.9% | "2023 7,000 153,164 3.4 6.2 0.1 0.9" |
| SDI taxable wage limit 2023 (the last year with a cap) | USD 153,164 | same row |

### 4.2 PFL: Part of SDI

- **One deduction.** "Paid Family Leave (PFL) is a component of the SDI program." There is no separate PFL withholding. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
- **Benefits.** PFL and disability benefit amounts are claim-side rules administered by EDD and are not covered here. The live version of this Guide stated a weekly benefit maximum and replacement percentages for 2025; those are removed because no 2026 page was read for them.

### 4.3 AUDIT FLASH POINT: SDI Cap Still Switched On in Payroll Software

Payroll systems that were not reconfigured when the cap was removed keep stopping SDI at an old cap. The usual result:

- High earners are under-withheld for SDI.
- The DE 9 and DE 9C understate SDI withheld.
- Form W-2 Box 14 shows less SDI than the year's rate times California SDI wages.

**Reconciliation procedure:**
1. For each year from 2024, take each employee's SDI wages and SDI withheld.
2. Expected SDI equals SDI wages times that year's rate (2024 and 2025 in the history table above, 2026 in section 2). This is arithmetic only, per year, per employee.
3. Investigate any shortfall.
4. Correct prior quarters with the DE 9ADJ (Quarterly Contribution and Wage Adjustment Form) or through e-Services for Business, and issue corrected Forms W-2 (W-2c). DE 44 explains when and how to correct a DE 9 and DE 9C. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
5. Recovering the shortfall from the employee is an employment law question; refer it to employment counsel.

### 4.4 Voluntary Plan Alternative

- **Voluntary Plan (VP).** An employer may apply to EDD for approval of a Voluntary Plan that pays DI and PFL benefits in place of SDI. A VP "must provide all the benefits of SDI, at least one benefit that is better than SDI, and it cannot cost employees more than SDI". The employer must post a security deposit with EDD. Once approved, the employer stops sending SDI withholdings to EDD for the covered employees. The live version of this Guide said a VP needs a majority employee vote; DE 44 does not say so, and that statement is removed. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)

## 5. Unemployment Insurance (UI)

### 5.1 Mechanics

- **Employer only.** UI is paid by the employer; nothing is withheld from the employee. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
- **New employer.** A new employer pays the new employer rate in the first table in section 2 for two to three years. Which it is depends on when the employer meets the criteria in section 982(b) of the California Unemployment Insurance Code. After that the rate is experience rated within the Schedule F+ range. [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding)
- **Buying a business.** A buyer of an established business may keep the previous owner's UI rate, or apply for a transfer of the reserve account on the DE 4453. [DE 231Z](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de231z.pdf)
- **SUTA dumping.** An employer subject to section 977(c) pays the highest rate provided by law plus an additional 2 percent; refer these cases out. [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding)
- **How experience rating works.** EDD's Information Sheet DE 231Z explains reserve account balances and the rate schedules. [DE 231Z](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de231z.pdf)

**Notice of Contribution Rates (DE 2088).** Each December EDD mails the DE 2088 with the employer's rates for the coming year. DE 44 says the employer "may protest any item on the DE 2088 except Employment Training Tax, which is specifically set by law", within 60 days of the issued date on the notice. EDD's rates page says "except SDI and ETT, which are specifically set by law", and DE 231Z says "except the ETT and SDI rates". [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding) Do not treat the SDI rate as protestable. An extension of up to 60 days may be granted for good cause if it is requested before the protest deadline. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)

### 5.2 FUTA Credit Reduction Interaction

California has an outstanding federal loan, so California employers lose part of the federal unemployment (FUTA) credit. EDD's page prints the position for wages paid in 2025:

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://edd.ca.gov/en/payroll_taxes/federal-unemployment-tax-act |
| Normal federal credit toward the regular federal rate | 5.4% toward 6.0% | "federal law provides employers with a 5.4 percent tax credit toward the 6.0 percent regular tax" |
| Credit reduction for the 2025 tax year | 1.2% | "this credit will be reduced by 1.2 percent to a 4.2 percent credit for the 2025 tax year" |
| Credit left for the 2025 tax year | 4.2% | same sentence |
| Extra federal cost per employee for 2025 | USD 84 | "California employers will pay an extra $84 per employee for the 2025 tax year" |

The 2026 reduction is fixed by the federal government after the year ends; EDD's page only says the credit is expected to be reduced "by an additional 0.3 percent each year" until the loan is repaid. Do not state a 2026 figure until the IRS publishes it. Form 940 is in `us-form-941-940-payroll`. EDD and the IRS also compare Form 940 with DE 9 lines C and D2 each year; an out-of-balance condition can produce an assessment. [EDD FUTA page](https://edd.ca.gov/en/payroll_taxes/federal-unemployment-tax-act)

### 5.3 Voluntary UI Contribution

The live version of this Guide described a voluntary contribution to buy down the UI rate, with a March deadline. No page read for this rewrite states the deadline or the conditions, so the rule is not repeated here. Ask EDD or check DE 231Z before advising on it. [DE 231Z](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de231z.pdf)

## 6. Employment Training Tax (ETT)

- **Rate and base.** ETT is charged at the 2026 ETT rate in the first table in section 2, on the same per-employee wage limit as UI. The DE 44 maximum per employee is in the second table. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
- **Who pays.** ETT is set by statute and applies to UI taxable wages of employers with positive UI reserve account balances and of employers subject to section 977(c) of the California Unemployment Insurance Code (DE 44, State Payroll Taxes table). An employer with a negative reserve balance that is not subject to section 977(c) does not pay it. The DE 2088 shows whether ETT applies. DE 44 states: "All tax-rated employers, including new employers, are subject to the ETT." It also states: "Employers do not pay the ETT while their accounts have a negative reserve balance, but they must pay a higher rate of Unemployment Insurance (UI) tax." The DE 2088 shows the ETT rate assigned. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
- **Reporting.** ETT is reported on the DE 9 with UI, SDI and PIT. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)

## 7. Quarterly and Annual Filings

### 7.1 Form DE 9: Quarterly Contribution Return and Report of Wages

- **DE 9 contents.** The DE 9 "reconciles tax and withholding amounts with deposits for the quarter". It carries Total Subject Wages on line C and UI Taxable Wages on line D2, the lines EDD and the IRS compare with Form 940. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)

### 7.2 Form DE 9C: Quarterly Contribution Return and Report of Wages (Continuation)

- **DE 9C contents.** The DE 9C "reports total subject wages and Personal Income Tax (PIT) wages paid and PIT withheld for each employee for the quarter". [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)

### 7.3 Due Dates

The DE 9 and DE 9C have a due date and a later delinquency date. A return is late only if it is not filed by the delinquency date. For 2026:

| Quarter | Due | Delinquent if not filed by |
| --- | --- | --- |
| 1st (January, February, March) | April 1, 2026 | April 30, 2026 |
| 2nd (April, May, June) | July 1, 2026 | July 31, 2026 |
| 3rd (July, August, September) | October 1, 2026 | November 2, 2026 |
| 4th (October, November, December) | January 1, 2027 | February 1, 2027 |

Source: [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf), table "Report Quarter Due Delinquent if Not Filed By". The live version of this Guide gave the third quarter as October 31 and the fourth quarter as January 31; for 2026 those dates fall on weekends, and EDD prints November 2, 2026 and February 1, 2027.

- **Weekend and holiday rule.** "If the Delinquent if Not Filed By date falls on a Saturday, Sunday, or legal holiday, the Delinquent if Not Filed By date is extended to the next business day." [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)

### 7.4 Filing Method

- **E-file and e-pay mandate.** "All employers are required to electronically submit their employment tax returns, wage reports, and payroll tax deposits to EDD." A paper DE 9 and a paper DE 9C each carry a penalty (amounts in the DE 44 table in section 2), and a paper deposit carries its own penalty (row in the DE 44 table in section 2). An employer may request a waiver for lack of automation, severe economic hardship, a current federal exemption or another good cause; waivers cannot be filed retroactively. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)

### 7.5 Q4 DE 9 and the Annual Reconciliation

- **Reconcile to Form W-2.** The year's DE 9C totals for each employee must agree with Form W-2 Box 16 (California PIT wages), Box 17 (California PIT withheld) and Box 14 (SDI withheld). EDD also compares DE 9 lines C and D2 with the federal Form 940 (section 5.2). [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
- **Late reports.** If returns are filed late or payments are not made on time, EDD sends a Statement of Account (DE 2176), and an unpaid balance can lead to a state tax lien that becomes public record. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)

## 8. Deposit Cadence: DE 88 and e-Services

SDI and PIT deposits follow the employer's federal deposit schedule and the amount of PIT accumulated. UI and ETT are not deposited on this schedule; they are paid quarterly. The thresholds are in the DE 44 table in section 2.

| Federal deposit schedule | PIT accumulated | California PIT and SDI deposit due |
| --- | --- | --- |
| Next-day | Less than the quarterly threshold (USD 350) | Quarterly |
| Next-day | USD 350 to USD 400 | 15th of the following month |
| Next-day | More than USD 400 | Next business day |
| Semi-weekly | Less than USD 350 | Quarterly |
| Semi-weekly | USD 350 to USD 400 | 15th of the following month |
| Semi-weekly | More than USD 400 (payday Wednesday, Thursday or Friday) | Following Wednesday |
| Semi-weekly | More than USD 400 (payday Saturday, Sunday, Monday or Tuesday) | Following Friday |
| Monthly | Less than USD 350 | Quarterly |
| Monthly | USD 350 or more | 15th of the following month |
| Quarterly or annually | Less than USD 350 | Quarterly |
| Quarterly or annually | USD 350 or more | 15th of the following month |

Source: [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf), table "California Deposit Requirements". The live version of this Guide used a higher quarterly threshold that EDD does not print; the DE 44 thresholds are USD 350 and USD 400.

- **Notes to the table.** If a due date falls on a Saturday, Sunday or legal holiday it moves to the next business day. Electronic deposits must settle in the state's bank account on or before the third business day after the payroll date. An employer not on any federal schedule still deposits SDI and PIT quarterly or more often under this table. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
- **UI and ETT.** These are paid by quarter; for 2026 a quarter's UI and ETT payment is delinquent if not paid by April 30, July 31, November 2 (2026) and February 1 (2027). [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)

### 8.1 Penalties for Late Deposits

- **Late payment.** A penalty of 15% plus interest is charged on late payroll tax payments (rate in the DE 44 table in section 2). The interest rate is reset every six months. For electronic payments, timeliness is judged by the settlement date. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
- **Failure to withhold and send.** Failing to withhold payroll taxes and send them to EDD, "even by mistake, can result in a misdemeanor charge", with a fine and jail term on conviction (fine in the DE 44 table in section 2). [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
- **Removed.** The live version of this Guide cited Revenue and Taxation Code percentage penalties for negligence and fraud and a Franchise Tax Board interest range. Those are not on any EDD page read for this rewrite; confirm any Franchise Tax Board penalty on ftb.ca.gov.

## 9. CalSavers

### 9.1 Statutory Authority

CalSavers is the state retirement savings program for employers that do not offer a retirement plan. Its official pages (on treasurer.ca.gov) refused our reader with a 403 response for this rewrite, so this Guide states no CalSavers deadline, employee threshold, contribution rate or penalty.

### 9.2 Mandate: Employee Threshold

Not covered (see 9.1). The live version of this Guide stated an employee threshold, a deadline and phase dates; they are removed until an official page can be read.

### 9.3 Employer Obligations

Not covered (see 9.1). Confirm registration, exemption and payroll deduction duties with the CalSavers program directly.

### 9.4 AUDIT FLASH POINT: CalSavers Mandate Enforcement

Not covered (see 9.1). The live version of this Guide stated penalties per employee; they are removed. Ask the employer whether it offers a qualified retirement plan, and if not, refer the CalSavers question.

## 10. Worker Classification (ABC Test)

### 10.1 Statutory Authority

- **Who is an employee.** An employee includes any worker who is an employee under the ABC test or the Borello test, and any worker whose services are specifically covered by law, such as a corporate officer. Day labor, part-time help, casual labor, temporary help and probationary work are not excluded from employment. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)

### 10.2 The ABC Test

- **All three, or an employee.** A person providing labor or services for pay is an employee, not an independent contractor, unless the hiring entity shows that ALL THREE are satisfied: (A) the person is free from the control and direction of the hiring entity in performing the work, both under the contract and in fact; (B) the person performs work that is outside the usual course of the hiring entity's business; (C) the person is customarily engaged in an independently established trade, occupation or business of the same nature as the work performed. If any one fails, the worker is an employee. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)

### 10.3 Statutory Exemptions

- **Borello instead of ABC.** In specific situations the Borello multi-factor test is used instead of the ABC test. EDD points to Information Sheet DE 231 and the state Employment Status Portal for the exceptions. The live version of this Guide listed occupations and a business-to-business test with a count of criteria; no page read for this rewrite prints that list, so it is removed. Test each exception against DE 231 before relying on it. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)

### 10.4 AUDIT FLASH POINT: Misclassification

- **Exposure.** An employer that classified employees as independent contractors "could be liable for back taxes, penalties, and interest". [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
- **No federal safe harbor.** "California does not provide relief under the Safe Harbor provisions of the Internal Revenue Code." A worker treated as a contractor under federal section 530 relief can still be an employee for California payroll. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
- **Wage-and-hour claims.** Unpaid wage, overtime, wage statement and Private Attorneys General Act claims follow a misclassification. The live version of this Guide stated penalty amounts and limitation periods for them; those are removed. Refer to employment counsel.
- **Protocol.** Document the ABC analysis in writing before engaging a contractor. If any prong is doubtful, treat the worker as an employee.

## 11. DE 542: Independent Contractor Reporting

- **Reporting duty.** A business that pays an independent contractor must report the contractor to EDD on the Report of Independent Contractor(s) (DE 542) within 20 calendar days of paying the contractor the threshold amount or more, or entering into a contract for that amount or more, whichever is earlier. The threshold is in the DE 44 table in section 2. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)

### 11.1 Mechanics

- **How.** File online through e-Services for Business. DE 44 sends employers to page 58 of the guide and to the DE 542 for the data required. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)

### 11.2 Purpose

- **Purpose and penalties.** The information helps locate parents who are delinquent in child support. It is not a tax return.

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de542faq.pdf |
| Penalty for each failure to report on time | USD 24 | "The EDD may assess a penalty of $24 for each failure to comply within the required time frames." |
| Penalty where the failure results from conspiracy between the business and the contractor | USD 490 | "a penalty of $490 may be assessed for the failure to report IC information if the failure is the result of conspiracy" |

### 11.3 Interaction with Federal 1099-NEC

- **Separate reports.** The DE 542 is a California report and does not replace federal Form 1099-NEC. The 2026 DE 44 still prints the DE 542 threshold in section 2, whatever the federal threshold is. For the federal form, use `us-1099-nec-issuance`. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)

### 11.4 New Hire Reporting (DE 34)

- **Who and when.** Report every newly hired employee on the Report of New Employee(s) (DE 34) within 20 calendar days of the employee's start-of-work date. This includes employees rehired after a separation of at least 60 consecutive days and employees returning from a furlough, separation, leave of absence without pay or termination. Employees kept on after buying a business count as new hires. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
- For other states' new hire rules, use `us-state-new-hire-reporting-matrix`.

## 12. Wage Statement Requirements: Labor Code Section 226

- **Every payday.** Under Labor Code Section 226(a), semimonthly or every time wages are paid, whether by check, in cash or otherwise, the employee must receive a detachable part of the check or a separate writing showing the required information. Only the last four digits of the social security number, or an employee identification number other than a social security number, may be shown. [DIR paydays FAQ](https://www.dir.ca.gov/dlse/FAQ_Paydays.htm)
- **Overtime corrections.** Overtime hours recorded as a correction on the next regular pay period's statement, with the dates of the pay period being corrected, comply with Section 226(a) on total hours worked. [DIR paydays FAQ](https://www.dir.ca.gov/dlse/FAQ_Paydays.htm)

### 12.1 Section 226(e) Penalties

The live version of this Guide stated per-pay-period penalty amounts and an aggregate cap under Section 226(e), and Private Attorneys General Act amounts. The statute site (leginfo.legislature.ca.gov) did not answer for this rewrite and no Labor Commissioner page read prints those amounts, so they are removed. Refer wage statement penalty questions to employment counsel.

## 13. Final Pay

### 13.1 Timing of Final Wages

- **Discharge or layoff.** An employee who is discharged must be paid all wages, including accrued vacation, immediately at the time of termination (Labor Code Sections 201 and 227.3). [DIR paydays FAQ](https://www.dir.ca.gov/dlse/FAQ_Paydays.htm)
- **Quit with at least 72 hours' notice.** An employee without a written contract for a definite period who gives at least 72 hours' prior notice and quits on the day given must be paid all wages, including accrued vacation, at the time of quitting (Section 202). [DIR paydays FAQ](https://www.dir.ca.gov/dlse/FAQ_Paydays.htm)
- **Quit without 72 hours' notice.** The same employee who quits without 72 hours' prior notice must be paid all wages, including accrued vacation, within 72 hours of quitting. The employee may ask for the final payment to be mailed. [DIR paydays FAQ](https://www.dir.ca.gov/dlse/FAQ_Paydays.htm)
- **Special industries.** Seasonal layoffs in curing, canning or drying perishable fruit, fish or vegetables (72 hours), motion picture production, for an employee whose unusual or uncertain terms of employment require special computation (next regular payday), oil drilling (24 hours, excluding weekends and holidays) and some hiring-hall venue workers under a collective bargaining agreement have their own deadlines. [DIR paydays FAQ](https://www.dir.ca.gov/dlse/FAQ_Paydays.htm)
- **Direct deposit.** Final wages may be paid by direct deposit only if the employee has voluntarily authorized it and the employer complies with Labor Code Section 213(d). [DIR paydays FAQ](https://www.dir.ca.gov/dlse/FAQ_Paydays.htm)

### 13.2 PTO and Vacation Payout

- **Vacation is wages.** Vacation pay accrues as it is earned and cannot be forfeited, even on termination, whatever the reason (Suastez v. Plastic Dress Up). An employer may place a reasonable cap that stops further accrual (Boothby v. Atlas Mechanical). Unless a collective bargaining agreement provides otherwise, all earned and unused vacation is paid at termination at the employee's final rate of pay (Labor Code Section 227.3). [DIR vacation FAQ](https://www.dir.ca.gov/dlse/FAQ_Vacation.htm)
- **Sick leave.** The live version of this Guide stated a rule on paying out sick leave and combined PTO banks; no page read for this rewrite covers it, so it is removed. Check the Labor Commissioner's paid sick leave FAQ before advising.

### 13.3 AUDIT FLASH POINT: Waiting Time Penalty Under Section 203

- **When it applies.** The penalty applies when an employer willfully fails to pay any wages due under Sections 201, 201.5, 202 or 202.5 to an employee who quits or is discharged. Willful does not require intent or blame; it means the employer knows what it is doing. A good faith dispute that any wages are due prevents the penalty. [DIR waiting time FAQ](https://www.dir.ca.gov/dlse/FAQ_WaitingTimePenalty.htm)
- **How much.** The penalty is the employee's daily rate of pay times the number of days the wages are unpaid, up to a maximum of 30 days. The 30 days are calendar days, including weekends and holidays. [DIR waiting time FAQ](https://www.dir.ca.gov/dlse/FAQ_WaitingTimePenalty.htm)
- **What counts as wages.** Unpaid accrued vacation counts. Business expense reimbursements are not wages, so paying them late does not trigger the waiting time penalty. The live version of this Guide told employers to include expense reimbursements to avoid the penalty; that is wrong for Section 203, though reimbursements are still owed. [DIR waiting time FAQ](https://www.dir.ca.gov/dlse/FAQ_WaitingTimePenalty.htm)
- **Removed.** The live version of this Guide said the penalty is reported on Form 1099-MISC and stated a limitation period; no page read for this rewrite supports either, so both are removed.
- **Mitigation.** Prepare the final check, including accrued vacation, before the termination meeting.

### 13.4 Tips and the Minimum Wage

- **No tip credit.** It is illegal for employers to make deductions from gratuities, or to use gratuities "as direct or indirect credits against an employee's wages". Tipped employees receive at least the full minimum wage plus their tips. Tips belong to the employee. A tip paid by credit card must reach the employee no later than the next regular payday after the patron authorized the payment (Labor Code Section 351). [DIR tips FAQ](https://www.dir.ca.gov/dlse/FAQ_TipsAndGratuities.htm)
- **Tips as wages for payroll tax.** Cash tips the employee receives while working and includes in a written statement to the employer are subject to UI and ETT, SDI and PIT withholding, and reportable as PIT wages, if they total USD 20 or more in a month. Noncash tips are not subject. [DE 231TP](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de231tp.pdf)

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.dir.ca.gov/dlse/faq_minimumwage.htm |
| State minimum wage from January 1, 2026, all employers | USD 16.90 per hour | "Effective January 1, 2026, the minimum wage is $16.90 per hour for all employers, not otherwise covered by a higher minimum wage specific to an industry or a locality." |

A higher minimum wage applies to fast food and health care workers and in many cities. Check the local ordinance for the work location.

## 14. Other Employer Obligations

### 14.1 Workers' Compensation: Mandatory

- **Required by law.** "If you have any employees, you are required by law to have workers' compensation insurance. Failure to do so is a crime and may result in penalties and closure of your business." [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
- The live version of this Guide stated criminal and per-employee penalty amounts and class code premium rates; they are removed because no page read for this rewrite prints them. Refer premium questions to the insurer and the Division of Workers' Compensation.

### 14.2 Local Taxes: San Francisco

San Francisco business taxes are administered by the city, outside EDD. No allowed host covers them, so this Guide states no rates or thresholds. Refer to the San Francisco Office of the Treasurer and Tax Collector.

### 14.3 Local Taxes: Los Angeles

The Los Angeles City business tax is administered by the city's Office of Finance. No allowed host covers it, so this Guide states no rates or exemptions. Refer out.

### 14.4 Other Local Payroll Surcharges

Some cities (for example San Jose, Oakland, Berkeley, San Diego) levy business taxes or license taxes. Confirm the employer's city and read the city ordinance; this Guide does not cover them.

## 15. Worked Examples

All three examples are hypothetical. The people and amounts are invented; the rates are the 2026 rates in the tables above. Arithmetic is shown so it can be checked.

### 15.1 Worked Example: Monthly Salaried Employee, Gross to Net

**Facts (hypothetical):** Ana is single, claims 1 allowance on her DE 4 and no estimated deduction allowances, and is paid monthly. Her gross pay for January 2026 is USD 6,000.00. Her employer is a new employer and its DE 2088 shows ETT applies. [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding)

California PIT withholding, Method B, monthly, single:

1. Gross USD 6,000.00 is more than the low income exemption of USD 1,575, so PIT is withheld. [2026 Method B](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/26methb.pdf)
2. No estimated deduction allowances, so nothing is subtracted at step 2. [2026 Method B](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/26methb.pdf)
3. Taxable income: USD 6,000.00 minus the standard deduction USD 476 = USD 5,524.00. [2026 Method B](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/26methb.pdf)
4. Taxable income of USD 5,524.00 is over USD 4,796 and not over USD 6,060: 8.800% of (USD 5,524.00 minus USD 4,796) plus USD 182.24 = USD 246.30. [2026 Method B](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/26methb.pdf)
5. Minus the exemption allowance credit for 1 allowance, USD 14.03: PIT withheld = USD 232.27. [2026 Method B](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/26methb.pdf)

Other deductions from Ana's pay:

6. SDI: USD 6,000.00 times 1.3% = USD 78.00. No ceiling applies. [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding)
7. Federal social security, Medicare and federal income tax withholding: compute them under `us-form-941-940-payroll`.
8. Pay after California deductions only: USD 6,000.00 minus USD 232.27 and USD 78.00 = USD 5,689.73. [2026 Method B](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/26methb.pdf)

Employer cost on top of gross pay (California only):

9. UI in January: USD 6,000.00 times 3.4% = USD 204.00. [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding)
10. ETT in January: USD 6,000.00 times 0.1% = USD 6.00. [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding)
11. In February only USD 1,000.00 of UI wage base is left (USD 7,000 minus USD 6,000.00), so UI is USD 34.00 and ETT is USD 1.00. From March, no UI or ETT is due on Ana's wages for the rest of 2026. Her year's UI is USD 238.00 and ETT USD 7.00, which matches the ETT maximum in DE 44. [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding)

Filing: PIT and SDI go on the DE 88 under the deposit schedule in section 8; UI and ETT are paid by quarter; all four are reported on the first quarter DE 9 and DE 9C, delinquent if not filed by April 30, 2026. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)

### 15.2 Worked Example: Tipped Server, First Quarter

**Facts (hypothetical):** Ben is a server in a city with no local minimum wage above the state rate. He works 480 hours in the first quarter of 2026 at the state minimum wage of USD 16.90 per hour. He reports USD 9,000.00 of cash tips in written monthly statements, more than USD 20 in each month. The employer is a new employer and its DE 2088 shows ETT applies. [DIR minimum wage FAQ](https://www.dir.ca.gov/dlse/faq_minimumwage.htm)

1. Hourly pay: 480 hours times USD 16.90 = USD 8,112.00. No tip credit may be taken. [DIR minimum wage FAQ](https://www.dir.ca.gov/dlse/faq_minimumwage.htm)
2. Reported cash tips of USD 9,000.00 are subject to UI, ETT, SDI and PIT withholding. Subject wages: USD 8,112.00 plus USD 9,000.00 = USD 17,112.00. [DE 231TP](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de231tp.pdf)
3. SDI: USD 17,112.00 times 1.3% = USD 222.46. [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding)
4. UI: only the first USD 7,000 of the year's wages is taxed, so UI is USD 7,000 times 3.4% = USD 238.00, all in the first quarter. [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding)
5. ETT: USD 7,000 times 0.1% = USD 7.00. [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding)
6. PIT: withhold under the schedules for Ben's actual payroll period and DE 4. The employer can only withhold from wages it controls; tips reported in cash increase the wages on which PIT is figured. [2026 Method B](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/26methb.pdf)

Payroll software that leaves reported tips out of the UI base understates UI for employees whose hourly pay alone would not reach the limit in the quarter.

### 15.3 Worked Example: Bonus Paid Separately

**Facts (hypothetical):** Ana (example 15.1) receives a USD 10,000.00 bonus in a separate payment in March 2026, not with her regular wages. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)

1. Option 2, flat rate: PIT = USD 10,000.00 times 10.23% = USD 1,023.00, without allowing for withholding allowances. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
2. SDI: USD 10,000.00 times 1.3% = USD 130.00. [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding)
3. UI and ETT: none, because Ana's 2026 wages already passed the UI and ETT wage limit in February. [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding)
4. If the same bonus were paid in the same check as her March salary, the flat rate could not be used: the employer adds it to the regular wages and withholds under the monthly schedule. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)

For restricted stock units and other equity paid through payroll, the federal side is in `us-equity-compensation-restricted-stock-units-and`; the California treatment of options is in DE 231SK.

## 16. Cross-Guide Coordination

- `us-form-941-940-payroll`: federal Forms 941 and 940, federal income tax withholding, social security and Medicare deposits (a named accountant maintains it; this Guide links to it and stops).
- `us-state-payroll-matrix`: other states' payroll taxes (link only).
- `us-state-new-hire-reporting-matrix`: new hire reporting in other states.
- `ca-540-individual-return`: the employee's California return, where Form W-2 Box 17 withholding is claimed.
- `ca-estimated-tax-540es`: employees under-withheld on supplemental wages (section 3.5).
- `us-s-corp-election-decision`: owners modelling salary through an S corporation need the California employer cost (UI, ETT) and employee SDI.
- `ca-llc-fee-and-tax`: LLC owners who are not employees are not on this payroll.
- `us-1099-nec-issuance`: the federal contractor form that sits beside the DE 542.
- `us-equity-compensation-restricted-stock-units-and`: federal equity compensation.
- `us-ca-return-assembly`: the California return package for sole proprietors.

## 17. Conservative Defaults: Quick Reference

| Ambiguity | Conservative default |
| --- | --- |
| Contractor or employee under the ABC test | Employee unless all three prongs clearly pass |
| No DE 4 on file | Withhold as single with zero allowances |
| SDI cap question | No cap since 2024 |
| Bonus paid with regular wages | Aggregate with regular wages; the flat rate is not available |
| Bonus paid separately | Option 1 (aggregate) for high earners; Option 2 flat rate only where under-withholding is not a concern |
| Whether ETT applies | New employers are subject to ETT (DE 44); read the DE 2088 for the rate |
| DE 9 date | File by the due date; the delinquency date is the last timely day |
| Final pay on discharge | Pay all wages and accrued vacation at the termination meeting |
| Disputed tips | Use the employee's written tip statement |
| CalSavers, city taxes, wage statement penalties | Refer out (not covered) |

When facts are ambiguous, apply the conservative default and disclose it.

## The method, step by step

1. A commercial employer registers with EDD on the DE 1 within 15 calendar days after paying more than the registration amount in the DE 44 table in section 2 in wages during any calendar quarter (other employers: DE 44 page 6). All returns and deposits then go through e-Services for Business under the e-file and e-pay mandate. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
2. Get a signed Form W-4 and DE 4 from each new employee; with no valid DE 4, withhold as single with zero allowances. [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding)
3. Report each new hire on the DE 34 within 20 calendar days of the start-of-work date, and each contractor on the DE 542 within 20 calendar days of reaching the threshold. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
4. Classify each worker under the ABC test, or the Borello test where an exception applies. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
5. Set up pay codes: check each payment type (HSA contributions, tips, lodging, fringe benefits) against DE 231TP. [DE 231TP](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de231tp.pdf)
6. Each payday, withhold PIT under the 2026 Method A or Method B schedules for the payroll period, or the flat supplemental rate for a separately paid bonus. [2026 Method B](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/26methb.pdf)
7. Withhold SDI at the 2026 rate on all wages, with no ceiling. [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding)
8. Compute UI and ETT at the rates on the employer's DE 2088, on each employee's wages up to the per-employee limit for the calendar year. [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding)
9. Deposit PIT and SDI on the DE 88 under the schedule in section 8. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
10. File the DE 9 and DE 9C each quarter by the delinquency date, and pay UI and ETT. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
11. After year end, reconcile the DE 9C totals to Form W-2 Boxes 14, 16 and 17, and the DE 9 to Form 940. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
12. On termination, pay final wages on the Labor Code timetable. [DIR paydays FAQ](https://www.dir.ca.gov/dlse/FAQ_Paydays.htm)
13. Each December, read the new DE 2088 and protest within 60 days of its issued date if it is wrong. [DE 44](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)

## Ask the client first

- Is the business a new employer with EDD, and what UI and ETT rates does its latest DE 2088 show?
- Which federal deposit schedule is it on (next-day, semi-weekly, monthly, quarterly or annual)? This sets the California PIT and SDI deposit dates.
- Does every employee have a signed DE 4 on file, and is anyone paid supplemental wages separately from regular pay?
- Has the payroll system ever applied an SDI wage cap since 1 January 2024?
- Does anyone work for the business as an independent contractor, and has each been tested under the ABC test and reported on the DE 542?
- Does anyone work outside California, or live outside California while working here?

## When to refuse or refer

- Multistate employees, reciprocal coverage elections and nonresident withholding: refer to a payroll professional; see `us-state-payroll-matrix`.
- Federal payroll returns and federal income tax withholding: `us-form-941-940-payroll`.
- Misclassification disputes, Private Attorneys General Act claims, wage statement penalties and waiting time claims already filed: refer to employment counsel.
- CalSavers questions: refer (no official page could be read for this Guide).
- City business taxes (San Francisco, Los Angeles and others): refer to the city or a local practitioner.
- Voluntary Plan applications, reserve account transfers and section 977(c) cases: refer to EDD or a payroll specialist.
- Annual California income tax brackets and Franchise Tax Board penalties: confirm on ftb.ca.gov; this Guide does not state them.

## Sources

- [EDD: Contribution Rates, Withholding Schedules, and Meals and Lodging Values](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding)
- [EDD: California Employer's Guide 2026 (DE 44)](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf)
- [EDD: California Withholding Schedules for 2026, Method B](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/26methb.pdf)
- [EDD: Tax Rates, Wage Limits, and Value of Meals and Lodging (DE 3395)](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de3395.pdf)
- [EDD: Federal Unemployment Tax Act](https://edd.ca.gov/en/payroll_taxes/federal-unemployment-tax-act)
- [EDD: Information Sheet, Types of Payments (DE 231TP)](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de231tp.pdf)
- [EDD: Information Sheet, Stock Options (DE 231SK)](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de231sk.pdf)
- [EDD: Information Sheet, California System of Experience Rating (DE 231Z)](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de231z.pdf)
- [EDD: Independent Contractor Reporting FAQ (DE 542 FAQ)](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de542faq.pdf)
- [Labor Commissioner: Paydays, Pay Periods, and the Final Payment of Wages FAQ](https://www.dir.ca.gov/dlse/FAQ_Paydays.htm)
- [Labor Commissioner: Waiting Time Penalty FAQ](https://www.dir.ca.gov/dlse/FAQ_WaitingTimePenalty.htm)
- [Labor Commissioner: Minimum Wage FAQ](https://www.dir.ca.gov/dlse/faq_minimumwage.htm)
- [Labor Commissioner: Vacation FAQ](https://www.dir.ca.gov/dlse/FAQ_Vacation.htm)
- [Labor Commissioner: Tips and Gratuities FAQ](https://www.dir.ca.gov/dlse/FAQ_TipsAndGratuities.htm)

## 18. Provenance and Citations

Rates, wage limits, schedules, due dates and penalties above are taken from the EDD and Labor Commissioner pages listed in Sources, read on 3 October 2026. The 2026 DE 44 is revision 52. The Franchise Tax Board site (ftb.ca.gov) and the statute site (leginfo.legislature.ca.gov) could not be read for this rewrite; nothing here relies on them, and any figure only they print is labelled "confirm on ftb.ca.gov" or removed.

## 19. Circular 230 Disclosure and Reviewer Responsibility

This Guide is a content reference for credentialed payroll and tax professionals. It is NOT tax advice to the taxpayer. Under Treasury Department Circular 230 §10.33 and §10.37, any written advice based on this Guide's output must be reviewed by a credentialed reviewer (Enrolled Agent, CPA, or attorney), or for purely state-payroll matters an experienced payroll practitioner with California-specific competence, before delivery to the client or filing with EDD, the Franchise Tax Board, or any other authority.

Misapplication risk is high in three areas:

1. **ABC test classification.** When in doubt, treat the worker as an employee.
2. **SDI with no wage ceiling.** Payroll configuration drift continues to produce errors in prior-period reviews.
3. **Supplemental wages.** The flat rate applies only to separate payments and does not match the employee's tax.

A taxpayer or employer relying on this Guide without credentialed review proceeds at their own risk.

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
