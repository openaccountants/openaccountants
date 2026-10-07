---
name: ie-payroll
description: Use this skill whenever asked to compute, review, or advise on end-to-end Irish monthly or weekly payroll for employees — gross-to-net calculation, payslip generation, statutory deduction sequencing (pension, BIK, PAYE, USC, PRSI, LPT-at-source), real-time submission to Revenue (PSR / "payroll submission request"), and year-end Employee Detail Summary reconciliation under Revenue myAccount. Trigger on phrases like "Ireland payroll", "Irish payroll", "Irish payslip", "compute Irish payroll", "monthly payroll Ireland", "weekly payroll Ireland", "gross to net Ireland", "RPN", "Revenue Payroll Notification", "PSR submission", "Employee Detail Summary", "BrightPay", "Sage payroll Ireland", "Surf Accounts payroll", "Thesaurus payroll", "BIK Ireland", "company car BIK Ireland", or any request involving running monthly or weekly payroll for one or more employees in Ireland. This skill is the ORCHESTRATOR — it pulls PAYE bracket rules from `ie-paye`, USC bands from `ie-usc`, and PRSI Class A rates from `ie-prsi-class-s` (which also covers Class A for completeness), and sequences them into the correct computation order. ALWAYS read this skill before touching Irish payroll computation.
jurisdiction: IE
tax_year: 2026
last_updated: 2026-10-02
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ireland payroll: gross to net for employees

This Guide runs an ordinary Irish weekly, fortnightly or monthly payroll for employees: the order of deductions, Income Tax under the Revenue Payroll Notification (RPN), USC, PRSI Class A, benefit in kind, the payroll submission to Revenue on or before pay day, the monthly statement and payment, and the year end. Figures are for tax year 2026. PRSI changed during 2026: one set of rates applies up to 30 September 2026 and another from 1 October 2026, and every PRSI rate below names its period. This is a source-cited draft. No accountant has reviewed it yet.

Companion Guides: `ie-usc` (USC in depth), `ie-prsi-class-s` (PRSI for the self-employed), `ie-income-tax-form11` (proprietary directors and others who file Form 11).

## Section 1: Quick reference, the order of payroll components

| Step | Component | Effect | Official page |
| --- | --- | --- | --- |
| 1 | Gross pay: basic, overtime, commission, bonus, taxable cash allowances | Starting point | [What are gross pay and taxable pay](https://www.revenue.ie/en/employing-people/what-constitutes-pay/what-are-gross-and-taxable-pay/index.aspx) |
| 2 | Add notional pay (benefit in kind) | Part of gross pay for Income Tax, USC and PRSI | [USC for employers](https://www.revenue.ie/en/employing-people/paying-an-employee/usc/index.aspx), [SW14](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf) |
| 3 | Subtract employee contributions to a Revenue approved pension scheme, PRSA, RAC or PEPP deducted by the employer, an approved income continuance scheme, or a salary sacrifice arrangement | Gives taxable pay for Income Tax only | [What are gross pay and taxable pay](https://www.revenue.ie/en/employing-people/what-constitutes-pay/what-are-gross-and-taxable-pay/index.aspx) |
| 4 | Income Tax on taxable pay using the cut-off point and tax credits on the RPN | Standard rate to the cut-off point, higher rate above, less tax credits | [Rule for calculating tax](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/calculating-tax-rules.aspx) |
| 5 | USC on gross pay, NOT reduced by employee pension contributions, using the USC cut-off points on the RPN | Withheld from the employee | [Employee's pension contributions](https://www.revenue.ie/en/employing-people/what-constitutes-pay/employees-pension-payments/index.aspx) |
| 6 | PRSI on reckonable pay (gross pay plus notional pay), NOT reduced by employee pension contributions | Employee share withheld; employer share paid on top | [Employee's pension contributions](https://www.revenue.ie/en/employing-people/what-constitutes-pay/employees-pension-payments/index.aspx), [SW14](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf) |
| 7 | Local Property Tax (LPT) only where it is shown on the RPN | Spread equally over the year | [Deduction of LPT](https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/deduction-of-lpt.aspx) |
| 8 | Net pay = gross cash pay less pension, Income Tax, USC, employee PRSI, LPT and voluntary deductions | Notional pay is not cash, so tax on it comes out of cash pay | |
| 9 | Payroll submission to Revenue on or before the pay date | Every pay run | [Payroll submissions](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/payroll-submissions.aspx) |

- **The base differs by deduction.** Revenue says of employee pension contributions: "You should not deduct these contributions from your employee's gross pay when you are calculating the following: Universal Social Charge (USC) and Pay Related Social Insurance (PRSI)." So pension relief at source reduces the Income Tax base only. The USC page also says "There is no relief from USC for employee pension contributions." ([Employee's pension contributions](https://www.revenue.ie/en/employing-people/what-constitutes-pay/employees-pension-payments/index.aspx), [USC overview](https://www.revenue.ie/en/jobs-and-pensions/usc/index.aspx))
- **For private sector employees, PRSI is charged on pension contributions.** SW14 says "PRSI is fully chargeable on payments by private sector employees in respect of" superannuation contributions and PRSA contributions. Public sector pension deductions are outside this Guide. ([SW14](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf))
- **Salary sacrifice.** Revenue lists a salary sacrifice arrangement among the deductions that reduce taxable pay for Income Tax. The pages read for this Guide do not say how salary sacrifice affects USC or PRSI; do not assume it reduces them. ([What are gross pay and taxable pay](https://www.revenue.ie/en/employing-people/what-constitutes-pay/what-are-gross-and-taxable-pay/index.aspx))
- **Conservative default, uncertain pension deductibility.** If you cannot confirm a contribution is to a Revenue approved scheme, or it exceeds the limits below, do not deduct it for Income Tax. Over-deduction of tax can be refunded to the employee through Revenue; late payment by the employer costs interest at the rate in the payment table in Section 5.

### Income Tax rates, bands and credits for 2026

| Item | Figure | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx |
| Standard rate | 20% | "Single or widowed or surviving civil partner, without qualifying children €44,000 @ 20%, balance @ 40%" |
| Higher rate, on the balance above the band | 40% | Same row |
| Standard rate band, single, widowed or surviving civil partner without qualifying children | EUR 44,000 | Same row |
| Standard rate band, single, widowed or surviving civil partner qualifying for the Single Person Child Carer Credit | EUR 48,000 | "qualifying for Single Person Child Carer Credit €48,000 @ 20%" |
| Standard rate band, married or civil partners, one with income | EUR 53,000 | "(one spouse or civil partner with income) €53,000 @ 20%" |
| Maximum increase in the band where both spouses or civil partners have income | EUR 35,000 | "The increase in the rate band is capped at the lower of €35,000 or the income of the lower earner." |
| Single Person Tax Credit | EUR 2,000 | "Single Person 2,000 2,000 1,875" (2026 column first) |
| Married Person or Civil Partner Tax Credit | EUR 4,000 | "Married Person or Civil Partner 4,000 4,000 3,750" |
| Employee (PAYE) Tax Credit | EUR 2,000 | "Employee PAYE Tax Credit 2,000 2,000 1,875" |

The employer does not choose the band or the credits. The RPN gives each employee's yearly tax credits and cut-off point, and the employer divides them by 52 (weekly), 26 (fortnightly) or 12 (monthly) ([Cumulative basis](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/cumulative-basis.aspx)). Use the table above only to sense-check an RPN.

### USC for 2026

| Item | Figure | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx |
| First band | EUR 12,012 | "Standard rates and thresholds of USC for 2026 Threshold for 2026 Rate First €12,012 0.5%" |
| Rate on the first band | 0.5% | Same quote |
| Next band (a band width, not a cumulative threshold) | EUR 16,688 | "Threshold for 2026 Rate First €12,012 0.5% Next €16,688 2%" |
| Rate on that band | 2% | Same quote |
| Next band (band width) | EUR 41,344 | "Next €16,688 2% Next €41,344 3% Balance 8%" |
| Rate on that band | 3% | Same quote |
| Rate on the balance | 8% | Same quote |

| Item | Figure | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/jobs-and-pensions/usc/index.aspx |
| Exemption threshold, a cliff: income above it pays USC on all of it | EUR 13,000 | "If your total income exceeds €13,000, you pay USC on your full income." |

| Item | Figure | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/jobs-and-pensions/usc/reduced-rates.aspx |
| Income limit for reduced rates (income at or below it, AND aged 70 or older OR holding a full Medical Card) | EUR 60,000 | "Reduced rates of USC will apply if your income is €60,000 or less and: you are aged 70 or older or hold a full Medical Card" |
| Reduced rate on the first EUR 12,012 | 0.5% | "The reduced rates for 2026 are: 0.5% on the first €12,012 and 2% on the balance." |
| Reduced rate on the balance | 2% | Same quote |

The RPN tells the employer which USC rates and cut-off points to apply, including any exemption ([USC for employers](https://www.revenue.ie/en/employing-people/paying-an-employee/usc/index.aspx), [RPN](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/revenue-payroll-notification.aspx)). Follow the RPN; do not apply the exemption or the reduced rates yourself.

### Emergency basis figures for 2026

| Item | Figure | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/jobs-and-pensions/documents/emergency-rates.pdf |
| Weekly cut-off point, employee has given a PPSN, weeks 1 to 4 (nil from week 5) | EUR 846.16 | "Weeks 1 to 4 €846.16 €0.00 Week 5 onwards €0.00 €0.00" |
| Monthly cut-off point, employee has given a PPSN, month 1 only (nil from month 2) | EUR 3,666.67 | "Month 1 €3,666.67 €0.00 Month 2 onwards €0.00 €0.00" |
| Tax credit under the emergency basis, every case, with or without a PPSN | EUR 0.00 | "Where employee does not provide a Personal Public Service Number (PPSN) Week / Month / Etc Cut-Off Point Tax Credit All €0.00 €0.00" |
| Emergency USC rate, on all pay, no USC cut-off point | 8% | "Emergency Basis of USC Deduction 2026 Week / Month / Etc USC Cut-Off Point USC Rate All €0.00 8%" |

### PRSI Class A for 2026: two periods

| Item | Figure | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-a-rates/ |
| Class A applies where reckonable pay is this amount or more a week, from all employments | EUR 38 | "reckonable pay of €38 or more per week from all employments" |
| Top of weekly band A0 (employee nil, employer lower rate), both periods | EUR 352 | "€38 - €352 A0 All Nil 9.00" |
| Top of weekly band AX (PRSI Credit band), both periods | EUR 424 | "€352.01 - €424 (**) AX All 4.20 9.00" |
| Weekly pay above which the employer higher rate applies (subclass A1, on all of that week's pay), both periods | EUR 552 | "€424.01 - €552 AL All 4.20 9.00 More than €552 A1" |
| Employee rate, weekly pay above EUR 352, period 1 January to 30 September 2026 | 4.2% | "€352.01 - €424 (**) AX All 4.20 9.00" |
| Employee rate, weekly pay above EUR 352, period from 1 October 2026 | 4.35% | "€352.01 - €424 (**) AX All 4.35" |
| Employer lower rate, weekly pay EUR 38 to EUR 552, period 1 January to 30 September 2026 | 9% | "€38 - €352 A0 All Nil 9.00" |
| Employer higher rate, weekly pay above EUR 552, period 1 January to 30 September 2026 | 11.25% | "More than €552 A1 All 4.20 11.25" |
| Employer lower rate, weekly pay EUR 38 to EUR 552, period from 1 October 2026 | 9.15% | "€38 - €352 A0 All Nil 9.15" |
| Employer higher rate, weekly pay above EUR 552, period from 1 October 2026 | 11.40% | "More than €552 A1 All 4.35 11.40" |

| Item | Figure | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf |
| Maximum weekly PRSI Credit (subclass AX), both periods | EUR 12 | "At gross weekly earnings of €352.01 the maximum PRSI Credit of €12 per week applies." |
| Bottom of the PRSI Credit earnings range, weekly | EUR 352.01 | "employees earning between €352.01 and €424 a week" |
| Monthly pay band for subclass A1 (employer higher rate) | EUR 2,392 | "More than €1,104 More than €2,392" (weekly, fortnightly, monthly columns) |

- **Which period.** Pay in the period 1 January to 30 September 2026 uses the first set of rates; pay from 1 October 2026 uses the second. The pages print the two periods but do not say whether the pay date or the week worked decides the rate for a pay period that straddles 1 October 2026. Check the payroll software's handling, and ask the Department of Social Protection if in doubt.
- **The bands are cliffs, not slices.** The column "How much of weekly income" reads "All": once weekly pay is above EUR 552, the employer higher rate applies to the whole week's pay, not only the excess. SW14 also prints fortnightly and monthly equivalents of each band (for example the monthly A1 band in the table above). ([PRSI Class A rates](https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-a-rates/), [SW14](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf))
- **PRSI Credit.** It applies only in subclass AX. SW14 says the credit is reduced by one sixth of earnings in excess of EUR 352.01, and SW14's worked example deducts the reduced credit from the PRSI charge at the employee rate. Above EUR 424 a week there is no credit. ([SW14](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf))
- **Lump sums on leaving.** SW14 says lump sum payments on leaving (redundancy, gratuities, ex-gratia) "are not regarded as reckonable pay for PRSI purposes and should be recorded under Class M".

### Pension contributions: limits on tax relief

| Item | Figure | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/jobs-and-pensions/pension/relief/tax-relief-limits.aspx |
| Under 30 | 15% | "Age Percentage limit Under 30 15% 30-39 20% 40-49 25% 50-54 30% 55-59 35% 60 or over 40%" |
| 30 to 39 | 20% | Same quote |
| 40 to 49 | 25% | Same quote |
| 50 to 54 | 30% | Same quote |
| 55 to 59 | 35% | Same quote |
| 60 or over | 40% | Same quote |
| Earnings limit for relief, per year | EUR 115,000 | "The maximum amount of earnings taken into account for calculating tax relief is €115,000 per year." |

The percentage limit and the earnings limit work together: relief is on contributions up to the age percentage of earnings, with earnings counted up to the yearly limit. Total contributions include ordinary contributions, AVCs and special contributions ([Employee's pension contributions](https://www.revenue.ie/en/employing-people/what-constitutes-pay/employees-pension-payments/index.aspx)). Employer contributions are not counted when calculating the employee's earnings threshold ([Tax relief limits](https://www.revenue.ie/en/jobs-and-pensions/pension/relief/tax-relief-limits.aspx)).

### Company car benefit in kind for 2026

| Item | Figure | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/employing-people/benefit-in-kind-for-employers/private-use-company-cars/calculate-value-benefit.aspx |
| Reduction to Original Market Value for 2026, categories A1, A, B, C and D only (not category E) | EUR 10,000 | "For 2023, 2024, 2025 and 2026, a reduction of €10,000 can be applied to the Original Market Value of cars in categories A1, A, B, C and D." |
| The same reduction for 2027 (not 2026) | EUR 5,000 | "2027 - reduction of €5,000." |
| Category A1 (0g/km, new from 1 January 2026), business km 0 to 26,000 | 15% | "0 26,000 15% 22.5% 26.25% 30% 33.75% 37.5%" |
| Category A (more than 0 up to and including 59g/km), business km 0 to 26,000 | 22.5% | Same row |
| Category B (more than 59 up to and including 99g/km), business km 0 to 26,000 | 26.25% | Same row |
| Category C (more than 99 up to and including 139g/km), business km 0 to 26,000 | 30% | Same row |
| Category D (more than 139 up to and including 179g/km), business km 0 to 26,000 | 33.75% | Same row |
| Category E (more than 179g/km), business km 0 to 26,000 | 37.5% | Same row |
| Lower limit of the highest business mileage band (made permanent from 1 January 2026) | 48,001 km | "the lower limit in the highest mileage band is reduced by 4,000 km to 48,001 km." |
| Category A1, business km 48,001 and above | 6% | "48,001* And above 6% 9% 10.5% 12% 13.5% 15%" |

The cash equivalent for 2026 is the Original Market Value (list price before first registration, including VAT and VRT), less the reduction where the category qualifies, times the percentage for the car's CO2 category and the year's business kilometres. Revenue says the Original Market Value reduction "is in addition to the relief for electric vehicles"; that EV relief is not covered here. Any contribution the employee makes directly to the employer towards running costs reduces the cash equivalent. Review notional pay at least quarterly. The middle mileage bands are on the same page.

### Small Benefit Exemption

| Item | Figure | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/employing-people/benefit-in-kind-for-employers/valuation-of-benefits/small-benefit-exemption.aspx |
| Combined value of up to five non-cash benefits a year, from 1 January 2025 | EUR 1,500 | "These benefits must not be in cash and the combined value of the five benefits cannot exceed €1,500." |

This is a cliff for a single benefit: "If a single benefit exceeds €1,500 in value, the full value of that benefit is subject to tax." Only the first five benefits in a year can qualify, unused allowance is not carried over, and a voucher that can be redeemed in whole or in part for cash does not qualify. The employer must report the date paid and the value to Revenue. ([Small Benefit Exemption](https://www.revenue.ie/en/employing-people/benefit-in-kind-for-employers/valuation-of-benefits/small-benefit-exemption.aspx))

### National minimum wage from 1 January 2026

| Item | Figure | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.ie/en/department-of-enterprise-tourism-and-employment/publications/national-minimum-wage-increase-on-1-january-2025/ |
| Aged 20 and over, per hour | EUR 14.15 | "The national minimum hourly rate will become €14.15 on 1 January 2026." |
| Aged 19, per hour | EUR 12.74 | "Aged 19 €12.74" |
| Aged 18, per hour | EUR 11.32 | "Aged 18 €11.32" |
| Aged under 18, per hour | EUR 9.91 | "Aged under 18 €9.91" |

The page address says 2025 but the page prints the 1 January 2026 rates. Check gross pay for hours worked against these rates before running the payroll.

## Section 2: Required inputs and refusal catalogue

### 2.1 Inputs required to run a payroll

| Input | Source | Notes |
| --- | --- | --- |
| PPSN | Employee | Without a PPSN no RPN is available and the employer must tax all pay at the higher rate with no tax credits; even with a PPSN, the emergency basis gives no tax credits (emergency table in Section 1) ([Emergency basis](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/emergency-basis.aspx)) |
| RPN | Requested from Revenue through payroll software or ROS before each payroll | Gives tax credits, cut-off points for Income Tax and USC, pay, tax and USC from any earlier employment since 1 January (unless week 1 or month 1 basis), exemptions, and LPT ([RPN](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/revenue-payroll-notification.aspx)) |
| Start date and leaving date | HR | A new employee is registered by an RPN request with the correct start date; a leaver's date of leaving goes on the final payroll submission ([Commencing and ceasing employees](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/commencing-and-ceasing-employees.aspx)) |
| Gross pay breakdown | Contract, timesheets | Basic, overtime, commission, bonuses, allowances; hours for the minimum wage check |
| Benefit in kind details | HR, fleet | Company car Original Market Value, CO2 category and business kilometres; other benefits; small benefits given so far this year |
| Pension details | Scheme provider | Scheme type (approved occupational scheme, PRSA, RAC, PEPP), employee and employer contributions, employee's age |
| PRSI class | HR, SW14 | Class A for most private sector employees aged 16 to 66 (or under 70 without a State Pension (Contributory)) |
| LPT | RPN | Deduct only where it is shown on the RPN |
| Attachment orders and other deductions | Court or employee | Apply as the order or authority says |

### 2.2 Refusal catalogue: out of scope for this Guide

| Scenario | Action |
| --- | --- |
| Cross-border employees, or Irish employment exercised outside the State | Refer to an Irish payroll specialist; a PAYE exclusion order or other relief may apply |
| Posted workers from another EU state with an A1 certificate | Refer; PRSI depends on the certificate |
| Multiple employments with the same employee | Follow the RPN for each employment; refer if the RPNs look inconsistent |
| Share schemes and share-based remuneration | Refer; SW14 says employer PRSI is not chargeable on share-based remuneration but employee PRSI may be |
| Pension lump sums on retirement | Out of scope |
| Termination payments above the basic exemption (see the table below) | Refer; the increased exemption and SCSB are fact-specific |
| Proprietary directors | Refer to `ie-income-tax-form11`; their PRSI class may not be Class A |
| Public sector employees (PRSI Classes B, C, D or public sector Class A rules) | Out of scope |
| Classes H, J, K, M and Community Employment | Out of scope; see SW14 |
| Backdated pay covering more than one tax year | Refer |
| Insolvency and Redundancy Payments Scheme claims | Out of scope |

| Item | Figure | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/lump-sum-payments/basic-exemption.aspx |
| Basic exemption for a termination payment | EUR 10,160 | "The basic exemption is €10,160, plus €765 for each full year you were working for your employer." |
| Added for each full year of service | EUR 765 | Same quote |
| Lifetime limit where the basic exemption is used more than once (payments from different, unconnected employers) | EUR 200,000 | "you do not exceed a life-time limit of €200,000" |

A termination payment is tax free if it does not exceed the basic exemption; above it the increased exemption or SCSB may apply, which this Guide does not compute (refer). A career break does not count towards a full year's work.

## The method, step by step

1. **Get the latest RPN for each employee before running payroll.** Revenue: "Before running payroll, you must request the latest RPN for each employee." Payroll software retrieves it; without software, request it in ROS. Always use the latest RPN. If no RPN can be retrieved, operate the emergency basis ([RPN](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/revenue-payroll-notification.aspx)).
2. **Pick the tax basis the RPN shows.** Cumulative basis is the norm: tax due on total income from 1 January to date, less tax already deducted in the year ([Cumulative basis](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/cumulative-basis.aspx)). Week 1 or month 1 basis taxes each pay day on its own and never refunds unused credits within the period; use it only if the RPN instructs it ([Week 1 basis](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/week1-basis.aspx)). Emergency basis applies only where no RPN is available. If the employee has given a PPSN, tax at the standard rate up to the emergency cut-off point in the emergency table in Section 1 for weeks 1 to 4 of weekly pay, or month 1 of monthly pay, with no tax credits; from week 5 or month 2 the cut-off point is nil and all pay is taxed at the higher rate. If no PPSN, tax all pay at the higher rate with no tax credits from the first pay day. USC under the emergency basis is charged at the emergency USC rate in that table on all pay, with no USC cut-off point. Emergency weeks count from the start date even in weeks not worked ([Emergency basis](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/emergency-basis.aspx)).
3. **Build gross pay, including notional pay.** Gross pay is total pay before any deductions, including notional pay, share-based remuneration and pay before pension or salary sacrifice deductions ([What are gross pay and taxable pay](https://www.revenue.ie/en/employing-people/what-constitutes-pay/what-are-gross-and-taxable-pay/index.aspx)). Value a company car with the BIK table in Section 1; apply the Small Benefit Exemption only within its conditions. Notional pay is not cash, so the tax on it comes out of the cash pay.
4. **Work out taxable pay for Income Tax.** Subtract the employee's approved pension, PRSA, RAC or PEPP contributions deducted by the employer, approved income continuance contributions and salary sacrifice amounts ([What are gross pay and taxable pay](https://www.revenue.ie/en/employing-people/what-constitutes-pay/what-are-gross-and-taxable-pay/index.aspx)). Cap pension relief at the age percentage and earnings limit in the pension table ([Tax relief limits](https://www.revenue.ie/en/jobs-and-pensions/pension/relief/tax-relief-limits.aspx)).
5. **Calculate Income Tax.** Apply the standard rate up to the period cut-off point, the higher rate on the balance, add the two, and subtract the period tax credits ([Rule for calculating tax](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/calculating-tax-rules.aspx)). The rates are in the Income Tax table in Section 1.
6. **Calculate USC on gross pay, not on taxable pay.** Do not subtract employee pension contributions ([Employee's pension contributions](https://www.revenue.ie/en/employing-people/what-constitutes-pay/employees-pension-payments/index.aspx)). Apply the USC rates and cut-off points on the RPN, cumulatively where the RPN is cumulative ([USC for employers](https://www.revenue.ie/en/employing-people/paying-an-employee/usc/index.aspx)).
7. **Calculate PRSI on reckonable pay.** Reckonable pay is gross pay plus notional pay; employee pension contributions are not deducted. Pick the subclass from the week's pay (or the fortnightly or monthly band in SW14), and use the rates for the period, 1 January to 30 September 2026 or from 1 October 2026, from the PRSI tables in Section 1. In subclass AX, deduct the PRSI Credit ([PRSI Class A rates](https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-a-rates/), [SW14](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf)).
8. **Deduct LPT only if the RPN shows it.** Revenue: "LPT may be deducted at source from employees' wages where it is shown on the employee's Revenue Payroll Notification (RPN)." It is spread equally over the year. An employee's request alone is not enough ([Deduction of LPT](https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/deduction-of-lpt.aspx)).
9. **Net pay** = gross cash pay less employee pension, Income Tax, USC, employee PRSI, LPT and voluntary deductions.
10. **Report the payroll to Revenue on or before the pay date.** Revenue: "You must report the payroll information to Revenue on, or before, the day you make a payment to your employee." Each submission gives, per employee, the pay date, the pay, and the Income Tax, USC, PRSI and LPT deductions. The employer is responsible for compliance whether it uses software, a payroll company, an agency or ROS ([Payroll submissions](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/payroll-submissions.aspx)). For PRSI, report the class and the weeks in the period paid (one week for a weekly payroll, two for fortnightly), never a cumulative number of weeks ([PRSI for employers](https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/prsi.aspx)).
11. **Review the monthly statement and pay.** See Section 5 for the dates and the interest rate ([Paying tax to Revenue](https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/paying-tax-to-revenue.aspx)).
12. **Give the employee a payslip** stating the gross wages and the nature and amount of every deduction (Payment of Wages Act 1991, section 4; see Section 4).

## Ask the client first

- Is there a current RPN for every employee, and on what basis (cumulative, week 1 or month 1, emergency)? Has any employee no PPSN?
- What is each employee's pay frequency and pay date, and does any pay period straddle 1 October 2026?
- Is any employee outside ordinary private sector Class A (under 16, aged 66 or over, public sector, a proprietary director, Community Employment, a posted worker)?
- Which pension contributions are deducted, to what kind of scheme, and what is each employee's age and yearly earnings?
- What benefits are provided: company car (Original Market Value, CO2 category, business kilometres, any employee contribution), vouchers, other non-cash benefits, and how many small benefits so far this year?
- Is the employer a monthly, quarterly or annual remitter, and does it file and pay on ROS?

## When to refuse or refer

- Any case in the refusal catalogue in Section 2.2.
- No RPN can be obtained and the employee disputes emergency tax: run the emergency basis as Revenue requires and send the employee to myAccount; do not guess credits.
- A pay period straddles 1 October 2026 and the software does not show how it split the PRSI rates: refer before paying.
- The employer has paid the monthly liability late, or wants to correct a prior year: refer, since interest and correction rules apply.
- Termination payments, share awards, pension lump sums and any payment where you cannot tell whether it is pay: refer.
- Everything in this Guide is a source-cited draft. A qualified Irish payroll professional should review a payroll before any payslip, submission or payment.

## Section 3: Worked example (hypothetical)

A hypothetical monthly-paid employee: single, age 32, private sector Class A, cumulative RPN with the single person credit and the employee credit and the single standard rate band, same pay every month, no benefits, no LPT. The amounts below are hypothetical; the rates come from the tables in Section 1.

| Line | Amount | How it is worked out |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/cumulative-basis.aspx |
| Monthly gross salary (hypothetical) | EUR 5,000.00 | Assumption |
| Employee pension contribution to an approved scheme (hypothetical) | EUR 250.00 | Assumption; well inside the 20% limit for age 30 to 39 |
| Taxable pay for Income Tax | EUR 4,750.00 | Gross less pension |
| Monthly cut-off point | EUR 3,666.67 | EUR 44,000 divided by 12 |
| Monthly tax credits | EUR 333.33 | (EUR 2,000 plus EUR 2,000) divided by 12 |
| Income Tax for the month | EUR 833.33 | 20% of the cut-off point, plus 40% of taxable pay above it, less the monthly credits |
| USC for the month, on gross pay (pension not deducted) | EUR 111.07 | 0.5% of one twelfth of EUR 12,012, plus 2% of one twelfth of EUR 16,688, plus 3% of the rest of the EUR 5,000.00 |
| Employee PRSI, a month paid in the period to 30 September 2026 (monthly pay above the A1 band of EUR 2,392) | EUR 210.00 | 4.2% of EUR 5,000.00 |
| Employer PRSI, a month paid in the period to 30 September 2026 | EUR 562.50 | 11.25% of EUR 5,000.00 |
| Net pay, a month paid in the period to 30 September 2026 | EUR 3,595.60 | Gross less pension, Income Tax, USC and employee PRSI |
| Employee PRSI, a month paid in the period from 1 October 2026 | EUR 217.50 | 4.35% of EUR 5,000.00 |
| Employer PRSI, a month paid in the period from 1 October 2026 | EUR 570.00 | 11.40% of EUR 5,000.00 |
| Net pay, a month paid in the period from 1 October 2026 | EUR 3,588.10 | Gross less pension, Income Tax, USC and employee PRSI |

The live version of this Guide reduced the USC base by the pension contribution; that is wrong, and it understates USC. Real payroll software rounds at each step; small differences of a cent are expected.

## Section 4: Payslip components

The legal minimum comes from the Payment of Wages Act 1991, section 4. The enacted text says: "An employer shall give or cause to be given to an employee a statement in writing specifying clearly the gross amount of the wages payable to the employee and the nature and amount of any deduction therefrom" and requires the employer to treat the statement confidentially ([Payment of Wages Act 1991, section 4, enacted text](https://www.irishstatutebook.ie/eli/1991/act/25/section/4/enacted/en/html); [section 2, enacted text](https://www.irishstatutebook.ie/eli/1991/act/25/section/2/enacted/en/html)). Where wages are paid by credit transfer or another mode whereby an amount is credited to an account specified by the employee (section 2(1)(f) of the Act), the statement is given as soon as may be after the payment; where paid by any other mode, including cheque or cash, at the time of the payment, unless regulations under section 2(1)(h) set another time.

Recommended layout (good practice beyond the statutory minimum):

~~~
+-----------------------------------------------------------------+
|  EMPLOYER NAME                          PAYSLIP: MONTH YEAR     |
|  Address                                                        |
|  Employer registration number                                   |
+-----------------------------------------------------------------+
|  Employee name                    PPSN                          |
|  Tax basis (cumulative / week 1 / emergency)    PRSI class      |
|  Pay date                         Pay period                    |
|  PRSI weeks this period                                         |
+-----------------------------------------------------------------+
|  EARNINGS: basic, overtime, allowances, notional pay (BIK)      |
|  Gross pay                                                      |
+-----------------------------------------------------------------+
|  DEDUCTIONS: employee pension, Income Tax, USC, employee PRSI,  |
|  LPT (only if on the RPN), voluntary deductions                 |
+-----------------------------------------------------------------+
|  NET PAY                                                        |
+-----------------------------------------------------------------+
|  Employer contributions (information): pension, employer PRSI   |
|  Year-to-date totals: gross, Income Tax, USC, PRSI, pension     |
+-----------------------------------------------------------------+
~~~

## Section 5: Payroll submissions, statements and payment

### 5.1 What a payroll submission is

Since 1 January 2019 the employer reports each payroll to Revenue in real time, on or before the pay date ([Employer payroll obligations](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/index.aspx)). Pages on obligations before 1 January 2019 belong to the old regime.

### 5.2 Submission channels

| Channel | Use case |
| --- | --- |
| Direct payroll reporting from payroll software | Software sends payroll information to ROS automatically |
| ROS payroll file upload | Software generates a file and the employer uploads it to ROS |
| ROS "Submit payroll by online form" | Employers without payroll software |
| Customised stationery | Only employers excluded from mandatory electronic filing |

Source: [Payroll submissions](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/payroll-submissions.aspx). Common Irish payroll packages include BrightPay, Sage, Surf Accounts, Thesaurus and CollSoft; whatever the tool, the employer stays responsible.

### 5.3 What goes into a payroll submission, per employee

| Field | Source |
| --- | --- |
| Pay date | Pay run |
| Amount of pay (gross, notional pay, taxable pay) | Steps 3 and 4 |
| Income Tax, USC, PRSI and LPT deducted | Steps 5 to 8 |
| PRSI class and number of weeks in this pay period | RPN, HR |
| Employer PRSI | Step 7 |
| Start date for a new employee; date of leaving on the final submission | HR |
| Small benefits: date paid and value | Benefit records |

Sources: [Payroll submissions](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/payroll-submissions.aspx), [PRSI for employers](https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/prsi.aspx), [Commencing and ceasing employees](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/commencing-and-ceasing-employees.aspx).

### 5.4 Monthly statement and payment

| Item | Figure | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/paying-tax-to-revenue.aspx |
| Yearly Income Tax, PRSI and USC at or below which an employer may apply to pay quarterly | EUR 28,800 | "If the employer's total Income Tax, PRSI and USC payments for the year are €28,800 or less, they can apply to make their payments quarterly." |
| Interest on late payment of the employer's monthly liability (Income Tax, PRSI, USC and LPT deducted from employees), per day | 0.0274% | "The rate of interest is 0.0274% for every day the payment is late." |

- Revenue makes the monthly statement available by the 5th of the next month. The employer can accept it by the 14th; if not accepted by the 14th, it is deemed the monthly return on that day. Errors are fixed by amending the payroll submission, not the statement ([Paying tax to Revenue](https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/paying-tax-to-revenue.aspx), [Statements from Revenue](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/statements-from-revenue.aspx)).
- Payment: monthly remitters pay 14 days after the end of the month, or 23 days where the employer files and pays on ROS. Quarterly remitters still get a monthly statement and return but pay 14 days after the end of each quarter (23 days on ROS). Annual remitters pay 14 days after the end of the year (23 days on ROS) ([Returns and payment due dates](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/returns-and-payment-due-dates.aspx)).
- To pay quarterly, the employer must apply to the Collector-General, have been registered as an employer for at least 12 months, and have filed all returns and payments.
- Late payment: Revenue charges interest "from the 14th of the month" at the daily rate in the table above.
- The statement and payment cover Income Tax, PRSI, USC and LPT. Keep PRSI separate from Income Tax and USC in the books, because the Collector-General's Division passes PRSI to the Department of Social Protection ([PRSI for employers](https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/prsi.aspx)).

### 5.5 Corrections

If the statement is wrong, amend the payroll submission. Before the return due date a revised statement issues; after it, an amended return applies ([Statements from Revenue](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/statements-from-revenue.aspx)). Correct PRSI errors as soon as you find them, because errors can affect the employee's social welfare entitlements ([PRSI for employers](https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/prsi.aspx)).

### 5.6 Late payment and late reporting

Late payment of the monthly liability costs interest at the daily rate in the table in 5.4. The pages read for this Guide print no fixed penalty for a late payroll submission; refer any penalty question.

## Section 6: Year-end activities

There is no separate employer year-end return: the monthly returns built from payroll submissions are the record. The old P30, P35, P45 and P60 forms belong to the regime before 1 January 2019.

### 6.1 Employer year-end steps

| Step | Action | Deadline |
| --- | --- | --- |
| 1 | Reconcile payroll submissions to the payroll records and the general ledger | Before the December statement becomes the return |
| 2 | Make the final December payroll submission, including final notional pay | On or before the pay date |
| 3 | Review and accept or correct the December statement | 14 January |
| 4 | Pay the December liability (monthly remitter) | 14 January, or 23 January if filed and paid on ROS |

### 6.2 Employee year-end: the Employment Detail Summary

Revenue's name is the Employment Detail Summary (EDS), not "Employee Detail Summary". It "will contain income and deduction details from each of your employments or pensions for the relevant year" and is available in January in myAccount, under PAYE Services. If the employer submits a financial change later, a new EDS can be created and the latest one is the corrected version ([Employment Detail Summary](https://www.revenue.ie/en/jobs-and-pensions/end-of-year-process/employment-detail-summary.aspx)).

### 6.3 Leavers

Put the date of leaving on the final payroll submission when an employee leaves, starts a career break or dies in service. Delay can give the next employer a nil RPN and push the employee onto emergency tax ([Commencing and ceasing employees](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/commencing-and-ceasing-employees.aspx)). If the old employer does not cease the job, the employee can do it in myAccount ([When you leave your job](https://www.revenue.ie/en/jobs-and-pensions/changing-jobs/leave-your-job.aspx)).

### 6.4 Reconciliation checklist

| Check | Pass criterion |
| --- | --- |
| Statements paid equal Income Tax, USC, employee and employer PRSI and LPT on the payroll submissions | Match |
| Employee pension contributions on the submissions equal the provider's records | Match |
| Company car notional pay reviewed at least quarterly and the year's business kilometres band applied | Done |
| Small benefits: no more than five, combined value inside the limit, each reported | Done |
| Every leaver has a final submission with a date of leaving | Done |
| Employer PRSI switches between the lower and higher rate when weekly pay crosses EUR 552 | Done |
| PRSI rates switch from the period to 30 September 2026 to the period from 1 October 2026 | Done |
| USC calculated on gross pay, not reduced by employee pension contributions | Done |

## Section 7: Conservative defaults

| Situation | Conservative position |
| --- | --- |
| No RPN for a new starter | Emergency basis as Revenue describes it; never guess credits |
| Company car CO2 category unknown | Use category E (no Original Market Value reduction, highest percentages) until the CO2 figure is confirmed |
| Pension contribution above the age limit or earnings limit | Relief on the limit only; the excess goes through Income Tax |
| Pension contribution to a scheme not shown to be Revenue approved | No Income Tax relief until confirmed |
| PRSI class uncertain | Class A for a private sector employee aged 16 to 66; confirm anything else with SW14 |
| Pay period straddling 1 October 2026 | Refer before paying (see Section 1) |
| Employee asks for LPT deduction but it is not on the RPN | Do not deduct; the employee deals with LPT through Revenue |
| Mid-month joiner or leaver | Pay actual pay; start date or date of leaving on the payroll submission |
| Pay in a foreign currency | Convert to EUR and record the rate used; refer the rate choice |
| Bonus or backdated pay | Tax in the period paid under the cumulative basis; do not reopen earlier submissions without advice |
| Illness Benefit or other Department of Social Protection payments | Follow the RPN; refer |
| Attachment of earnings order | Apply as the order says and record the priority |

## Sources

| Source | Used for |
| --- | --- |
| [Revenue: tax rates, bands and reliefs](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx) | Income Tax rates, bands and credits |
| [Revenue: standard rates and thresholds of USC](https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx), [USC overview](https://www.revenue.ie/en/jobs-and-pensions/usc/index.aspx), [reduced rates of USC](https://www.revenue.ie/en/jobs-and-pensions/usc/reduced-rates.aspx) | USC |
| [Department of Social Protection: PRSI Class A rates](https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-a-rates/) | PRSI Class A, both 2026 periods |
| [SW14: the 2026 PRSI Contribution Rates and User Guide](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf) | PRSI Credit, bands, reckonable pay, pension contributions, lump sums |
| [Revenue: tax relief limits on pension contributions](https://www.revenue.ie/en/jobs-and-pensions/pension/relief/tax-relief-limits.aspx), [employee's pension contributions](https://www.revenue.ie/en/employing-people/what-constitutes-pay/employees-pension-payments/index.aspx), [gross pay and taxable pay](https://www.revenue.ie/en/employing-people/what-constitutes-pay/what-are-gross-and-taxable-pay/index.aspx) | Pension relief and the deduction bases |
| [Revenue: RPN](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/revenue-payroll-notification.aspx), [cumulative basis](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/cumulative-basis.aspx), [week 1 basis](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/week1-basis.aspx), [emergency basis](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/emergency-basis.aspx), [Emergency Basis of Tax and USC Deduction 2026 (PDF)](https://www.revenue.ie/en/jobs-and-pensions/documents/emergency-rates.pdf), [rule for calculating tax](https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/calculating-tax-rules.aspx) | Tax bases and calculation |
| [Revenue: payroll submissions](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/payroll-submissions.aspx), [commencing and ceasing employees](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/commencing-and-ceasing-employees.aspx), [statements](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/statements-from-revenue.aspx), [return and payment due dates](https://www.revenue.ie/en/employing-people/becoming-an-employer-and-ongoing-obligations/employer-obligations-from-01-01-2019/returns-and-payment-due-dates.aspx), [paying tax to Revenue](https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/paying-tax-to-revenue.aspx), [PRSI for employers](https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/prsi.aspx), [deduction of LPT](https://www.revenue.ie/en/employing-people/paying-your-employees-tax-to-revenue/deduction-of-lpt.aspx) | Reporting, statements, payment, LPT |
| [Revenue: company car BIK](https://www.revenue.ie/en/employing-people/benefit-in-kind-for-employers/private-use-company-cars/calculate-value-benefit.aspx), [Small Benefit Exemption](https://www.revenue.ie/en/employing-people/benefit-in-kind-for-employers/valuation-of-benefits/small-benefit-exemption.aspx), [USC for employers](https://www.revenue.ie/en/employing-people/paying-an-employee/usc/index.aspx) | Benefit in kind |
| [Revenue: basic exemption for termination payments](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/lump-sum-payments/basic-exemption.aspx) | Termination payments |
| [Revenue: Employment Detail Summary](https://www.revenue.ie/en/jobs-and-pensions/end-of-year-process/employment-detail-summary.aspx), [when you leave your job](https://www.revenue.ie/en/jobs-and-pensions/changing-jobs/leave-your-job.aspx) | Year end and leavers |
| [Department of Enterprise: national minimum wage from 1 January 2026](https://www.gov.ie/en/department-of-enterprise-tourism-and-employment/publications/national-minimum-wage-increase-on-1-january-2025/) | Minimum wage |
| [Payment of Wages Act 1991, section 4, enacted text](https://www.irishstatutebook.ie/eli/1991/act/25/section/4/enacted/en/html), [section 2, enacted text](https://www.irishstatutebook.ie/eli/1991/act/25/section/2/enacted/en/html) | Payslip |

## Footer disclaimer

*OpenAccountants: open-source accounting Guides for AI.*
*This is not tax advice. All outputs must be reviewed by a qualified Irish payroll professional or tax adviser before any payslip is issued, any payroll submission is made, or any payment is made.*

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
