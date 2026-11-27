---
name: uk-payroll
description: "UK employer payroll for 2026/27: PAYE, RTI FPS/EPS, tax codes, Class 1 NIC, Employment Allowance, student loans, minimum wage, statutory pay, workplace pensions and year-end. Includes original payroll cases and dated 2025/26 correction guidance; complex eligibility and future changes require an accountant."
version: 1.5
jurisdiction: GB
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - payroll-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# UK employer payroll (2026/27, with dated earlier-year cases)

Use this Guide for UK employer payroll for **6 April 2026 to 5 April 2027**. Use payroll software with the employee's actual tax code, NIC category, payment dates and pension arrangement. The examples are conditional checks, not permission to run payroll without those inputs ([HMRC rates](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).

## Who this applies to

Register before the first payday, no more than 2 months in advance. If you pay before the PAYE reference arrives, run payroll, store the FPS and submit it late when the reference arrives ([registration](https://www.gov.uk/register-employer)).

PAYE registration is **not decided by the NIC lower earnings limit**. HMRC lists payment of £96 or more a week, expenses or company benefits, a pension, another job, or receipt of Jobseeker's Allowance, Employment and Support Allowance or Incapacity Benefit as registration triggers. If operating PAYE, include everyone paid in the FPS, including people below £96 a week ([PAYE](https://www.gov.uk/paye-for-employers); [FPS](https://www.gov.uk/running-payroll/reporting-to-hmrc)). For unusual registration or scheme-closure circumstances: Check this point with one of our partner accountants.

Before each run, obtain the P45 or completed current starter checklist, HMRC coding notices, loan notices, date of birth, pay frequency, taxable/NIC-able earnings and pension scheme instructions. Use HMRC's current [new employee process](https://www.gov.uk/new-employee) rather than inferring a starter statement from a short description. For A/B/C statement selection, P9X carry-forward, missing P45s, post-leaving payments, one-off payments, emergency codes, S/C prefixes, K-code limits or retention requirements: Check this point with one of our partner accountants.

## Rates, bands and thresholds

The following are **HMRC's PAYE coding-table figures**, not a standalone personal Income Tax calculation. Apply the actual code and cumulative/non-cumulative basis in software. In particular, do not subtract a full allowance from high income and then apply these displayed upper endpoints; allowance withdrawal and coding affect the result. The employee's annual return belongs in **uk-income-tax-sa100**. Scottish codes, rates and taxpayer status: **uk-scottish-income-tax**; Check this point with one of our partner accountants.

| Item | Rate or amount | Period | Official source |
|---|---|---|---|
| Personal allowance (code 1257L) | £12,570 a year, £1,048 a month, £242 a week | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| PAYE, England, NI and Wales | 20% to £37,700; 40% £37,701 to £125,140; 45% above | 2026/27, subject to coding explanation above | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Allowance taper | £1 lost per £2 of adjusted net income above £100,000; nil at £125,140 | 2026/27 | https://www.gov.uk/income-tax-rates/income-over-100000 |
| NIC lower earnings limit | £129 a week, £559 a month, £6,708 a year | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| NIC primary threshold / UEL | £242 / £967 a week; £1,048 / £4,189 a month; £12,570 / £50,270 a year | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| NIC secondary threshold | £96 a week, £417 a month, £5,000 a year | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Employee Class 1 (category A) | 8% PT to UEL, 2% above | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Employer Class 1 (category A) | 15% above the secondary threshold, uncapped | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Employment Allowance | Up to £10,500 against eligible employer Class 1 liability; never more than that liability | 2026/27 | https://www.gov.uk/claim-employment-allowance |
| Student loan Plan 1 | 9% above £26,900 a year; £2,241.66 a month; £517.30 a week | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Student loan Plan 2 | 9% above £29,385 a year; £2,448.75 a month; £565.09 a week | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Student loan Plan 4 | 9% above £33,795 a year; £2,816.25 a month; £649.90 a week | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Student loan Plan 5 | 9% above £25,000 a year; £2,083.33 a month; £480.76 a week | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Postgraduate loan | 6% above £21,000 a year; £1,750 a month; £403.84 a week | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Minimum wage, age 21+ / age 18–20 / under 18 above compulsory school-leaving age | £12.71 / £10.85 / £8.00 an hour | Rates introduced 1 April 2026; apply from the first pay reference period beginning on or after that date | https://www.gov.uk/national-minimum-wage-rates |
| Apprentice minimum wage | £8.00 an hour only for qualifying apprentices under 19 or in their first year; otherwise the age rate | Same commencement rule | https://www.gov.uk/national-minimum-wage-rates |
| Qualifying earnings for pensions | £6,240–£50,270 a year; £520–£4,189 a month; £120–£967 a week; £480–£3,867 per 4 weeks | 2026/27 | https://www.thepensionsregulator.gov.uk/en/employers/new-employers/im-an-employer-who-has-to-provide-a-pension/declare-your-compliance/ongoing-duties-for-employers/earnings-thresholds |
| Pension contributions, ordinary qualifying-earnings money purchase basis | Employer minimum 3%, total minimum 8%; the employee portion includes applicable tax relief | 2026/27; scheme rules can require more | https://www.gov.uk/workplace-pensions/what-you-your-employer-and-the-government-pay |

## The taxable base

**NIC.** Ordinary regularly monthly paid employees use monthly thresholds, not annual thresholds divided into an annual liability. Calculate employee and employer contributions separately; under the exact-percentage method round to the nearest penny, disregarding a halfpenny or less ([SSC Regs 2001 regs 3 and 12](https://www.legislation.gov.uk/uksi/2001/1004/regulation/12)). Earnings between the LEL and PT protect the NIC record; do not promise a complete qualifying year from a single pay period. Directors and AN/AL methods, State Pension age, under-16s, deferment, reduced-rate letters, aggregation, apprentices under 25, veterans, Freeport/Investment Zone conditions and cross-border NIC: **uk-national-insurance**; Check this point with one of our partner accountants.

**Employment Allowance.** A company whose only director is its only employee liable for secondary Class 1 is excluded. The former prior-year £100,000 liability limit no longer applies from April 2025 ([eligibility](https://www.gov.uk/claim-employment-allowance/eligibility)). Staff count alone does not establish entitlement. For public-sector activity, connected companies/charities, multiple payrolls, domestic/care workers, off-payroll earnings, annual EPS claims, back-claims or set-off: Check this point with one of our partner accountants.

**Loans.** Use the gross earnings basis for secondary Class 1 and the correct earnings period. Disregard pence in the calculated repayment; a postgraduate deduction can run alongside the student loan ([reg 44](https://www.legislation.gov.uk/uksi/2009/470/regulation/44); [HMRC](https://www.gov.uk/guidance/special-rules-for-student-loans)). If the employee cannot identify their undergraduate plan after checking, HMRC permits Plan 5 pending SL1 only for Plan 1, 2 or 4 loans; do not turn an unknown postgraduate liability into Plan 5. Multiple undergraduate plans use the lowest recovery threshold pending SL1. Stop on SL2/PGL2 or HMRC's exceptional written instructions, including phone instructions subsequently confirmed in writing; not simply at the employee's request. For start dates, arrears, overpayments, court orders, off-payroll or Self Assessment loans: Check this point with one of our partner accountants.

**Minimum wage.** The rates are from SI 2026/357 and NMW Regs 2015 regs 4, 4A, 4B and 5. For worker eligibility, age or apprentice changes, accommodation offset, deductions, overtime, salaried/time/output/unmeasured work, pay reference periods or underpayment arrears and penalties: Check this point with one of our partner accountants. Do not infer compliance from gross salary alone.

**Statutory pay.** For the Great Britain SSP rate calculation, SSCBA 1992 s 157 sets the lower of £123.25 and 80% of normal weekly earnings; the daily rate divides by qualifying days in that week. SSP is not recoverable from HMRC ([s 157](https://www.legislation.gov.uk/ukpga/1992/4/section/157); [HMRC rates](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)). This is a rate rule after entitlement is established. For first-day entitlement, earnings tests, the 28-week maximum, linked absences, all exclusions, SSP1, Northern Ireland rules, disputes or the April 2026 transition (including absences starting by 21 September 2025 and protected pre-change earnings of £125–£154.05): Check this point with one of our partner accountants. Do not use the new formula to reduce a protected transitional payment.

For SMP, SPP, SAP, ShPP, SPBP and SNCP entitlement, notice/evidence, qualifying or matching weeks, relevant earnings periods, duration, statutory rates, day-one leave rights, adoption/neonatal/bereavement circumstances and Northern Ireland differences: Check this point with one of our partner accountants. A leave right does not by itself establish a pay right. For recovery classification other than the conditional SMP case below, advance funding or repayments: Check this point with one of our partner accountants.

**Pensions.** The table does not establish who must be enrolled. For the earnings trigger, age 22/State Pension age boundaries, ordinary UK working, opt-in/joining, postponement, re-enrolment, pensionable-pay definitions, contribution remittance and salary sacrifice: Check this point with one of our partner accountants. Confirm net pay versus relief at source before calculating PAYE or cash pension deductions ([scheme treatment](https://www.gov.uk/workplace-pensions/managing-your-pension)).

**Other payroll topics.** For Apprenticeship Levy liability, its pay bill and connected-group £15,000 allowance allocation; benefits/expenses classification, voluntary payrolling, P11D/P11D(b) corrections and filing channels; termination awards including the £30,000 boundary, sporting testimonials and Class 1/1A overlap; PAYE Settlement Agreements and Class 1B; or mandatory benefit payrolling in 2027/28 and 2028/29: Check this point with one of our partner accountants. These topics are retained as non-usable holds, not promised future rules. Do not apply ordinary benefits' July collection dates to termination awards.

## Deadlines and filing

| What | Ordinary deadline / action | Official source |
|---|---|---|
| FPS | On or before payday, including quarterly payers; report the usual payday when payment is early because of a bank holiday | https://www.gov.uk/running-payroll/reporting-to-hmrc |
| EPS for reductions | By the 19th of the following tax month; tax months start on the 6th | https://www.gov.uk/running-payroll/reporting-to-hmrc-eps |
| Nobody paid in a tax month | Send an EPS, not an FPS, by the 19th after that month | https://www.gov.uk/running-payroll/reporting-to-hmrc-eps |
| Monthly PAYE payment | By the 22nd of the next tax month; a postal cheque must reach HMRC by the 19th | https://www.gov.uk/pay-paye-tax |
| Quarterly PAYE payment | Only where applicable and arranged with HMRC; by the 22nd after the quarter, e.g. 22 July for 6 April–5 July | https://www.gov.uk/pay-paye-tax |
| Final FPS | On or before the last payday of the tax year | https://www.gov.uk/payroll-annual-reporting/send-your-final-payroll-report |
| P60 for employees working for you on 5 April | By 31 May after the tax year | https://www.gov.uk/payroll-annual-reporting/give-employees-p60-form |
| Required benefit reports and Class 1A total | By 6 July after the tax year; Class 1A on benefits paid by 22 July, or 19 July by cheque | https://www.gov.uk/employer-reporting-expenses-benefits/deadlines |
| PSA tax and Class 1B | By 22 October after the tax year, or 19 October by post | https://www.gov.uk/paye-settlement-agreements/deadlines-and-payment |

For quarterly eligibility (including the £1,500 average monthly payment test), FPS exceptions including weekend/bank-holiday and short/low-paid engagements, inactivity reporting, EPS late allocation, specified charges, missing-return replacement or other filing exceptions: Check this point with one of our partner accountants.

**Correcting 2025/26:** for wrong pay or deductions in an FPS for 6 April 2025–5 April 2026, submit another FPS with correct year-to-date figures, **not an Earlier Year Update** ([HMRC corrections](https://www.gov.uk/payroll-errors/correcting-your-fps-or-eps)). For NIC refunds/recovery from staff, changed employee details, payment-after-leaving fields, final-FPS or EPS corrections: Check this point with one of our partner accountants. Do not substitute 2026/27 rates for 2025/26. Earlier 2024/25 and 2025/26 tax/NIC/loan/wage/statutory-pay rate tables, accommodation offsets, old recovery percentages and the already-passed 2026 year-end dates require a period-specific check: Check this point with one of our partner accountants.

## Penalties and interest

The conditional late-FPS case below is not a general penalty calculation. For late/missing FPS or EPS, new-employer and first-failure easements, annual schemes, repeated lateness, specified charges, PAYE/Class 1A/Class 1B/PSA late payment, P11D(b), inaccuracy, minimum wage penalties, interest, appeals, reasonable excuse or time to pay: Check this point with one of our partner accountants. Do not quote a fixed current interest rate for a later payment period.

## Cross-border points

For employment status, IR35/off-payroll, CIS, inbound secondments, overseas duties, tax equalisation, non-UK employers, residence, tax treaties or certificates of coverage: Check this point with one of our partner accountants. Routes remain **uk-national-insurance**, **uk-statutory-residence-test**, **uk-income-tax-sa100**, **uk-student-loan-repayment**, **uk-bookkeeping**, **uk-corporation-tax** and **uk-vat-return**. Payroll journals, employer deductions and VAT on benefits are not determined by this Guide. Historical Pattern 2 (director AN/AL) and Pattern 3 (starter without P45) remain the explicit holds above; neither is silently discarded.

For payslips (gross/net, variable/fixed deductions, standing statements and hours), holiday entitlement including 5.6 weeks/28 days and the 3-day-week 16.8-day example, rolled-up holiday pay including the 12.07% method and leave-year commencement, working time including the 48-hour/17-week and under-18 and night-work limits, and Great Britain/Northern Ireland employment-law differences: Check this point with one of our partner accountants. Those former numerical rules are not usable calculations here. Do not assist underpayment of minimum wage or unauthorised deductions.

## Worked examples

**Example 1 / historical Case 1 and Pattern 1: monthly England employee.** Retain £3,500 monthly pay, 1257L cumulative, category A, Plan 2 and enrolment on qualifying earnings for 2026/27. Assume equal pay throughout the year, no earlier pay/tax discrepancy, no other adjustments, and a relief-at-source pension with 5% gross employee contribution and 3% employer contribution. The annual Income Tax check is (£42,000 − £12,570) × 20% = £5,886, averaging £490.50 monthly; actual cumulative PAYE uses software tables and pay-to-date. NIC is £196.16 employee and £462.45 employer monthly. Plan 2 is floor((£3,500 − £2,448.75) × 9%) = **£94**, not £94.61. Qualifying earnings £2,980 give £149 gross employee contribution (cash £119.20 plus £29.80 basic-rate relief) and £89.40 employer. A net-pay scheme changes the PAYE calculation ([rates](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027); [loan rounding](https://www.legislation.gov.uk/uksi/2009/470/regulation/44); [pensions](https://www.gov.uk/workplace-pensions/managing-your-pension)). The earlier **2025/26 Pattern 1**, with the same £3,500, code and pension inputs but no stated loan, has the same conditional annual tax check £5,886 and monthly average £490.50; its £595.50 result was arithmetic error. Its NIC and gross pension checks remain £196.16 / £462.45 and £149 / £89.40 on those stated assumptions; do not add a loan to that historical case.

```oa-check
name: Original monthly England case, 2026/27
inputs:
  monthly_pay: 3500
steps:
  - annual_taxable: monthly_pay * 12 - 12570
  - annual_tax: annual_taxable * 0.20
  - paye_average: annual_tax / 12
  - ee_nic: (monthly_pay - 1048) * 0.08
  - er_nic: (monthly_pay - 417) * 0.15
  - plan2: floor((monthly_pay - 2448.75) * 0.09)
  - qualifying: min(monthly_pay, 4189) - 520
  - pension_gross: qualifying * 0.05
  - pension_cash: pension_gross * 0.80
  - pension_relief: pension_gross - pension_cash
  - pension_er: qualifying * 0.03
expected:
  annual_tax: 5886
  paye_average: 490.50
  ee_nic: 196.16
  er_nic: 462.45
  plan2: 94
  pension_gross: 149
  pension_cash: 119.20
  pension_relief: 29.80
  pension_er: 89.40
```

**Example 2 / historical Case 2: four employees, £30,000 each.** Retain the trading company, four category A employees and the variation with one aged 19 (category M). Assume ordinary monthly £2,500 payments throughout 2026/27, no aggregated employments, unchanged categories, established EA eligibility and the full unused £10,500 allowance. Employer NIC is (£2,500 − £417) × 15% = £312.45 per person monthly; four staff give £14,997.60 annually, leaving £4,497.60. With one employee aged 19 throughout, that employee is below the £4,189 monthly upper secondary threshold; three category A staff give £11,248.20, leaving £748.20. The former £15,000/£4,500 and £11,250/£750 totals used annual thresholds and are not monthly-payroll results. A sole-director-only liable employee cannot claim EA ([NIC rates](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027); [eligibility](https://www.gov.uk/claim-employment-allowance/eligibility)).

```oa-check
name: Four original staff, monthly payroll, one aged 19
inputs:
  salary: 30000
  staff_a: 3
steps:
  - monthly: salary / 12
  - per_month: (monthly - 417) * 0.15
  - per_head: per_month * 12
  - all_a_total: per_head * 4
  - all_a_net: max(all_a_total - 10500, 0)
  - er_total: per_head * staff_a
  - net_after_ea: max(er_total - 10500, 0)
expected:
  per_month: 312.45
  per_head: 3749.40
  all_a_total: 14997.60
  all_a_net: 4497.60
  er_total: 11248.20
  net_after_ea: 748.20
```

**Example 3 / historical Case 3: SSP, June 2026.** Retain AWE £140, 5 qualifying days each week and 3 qualifying days sick in June 2026. Assume this is a new Great Britain absence, entitlement for all 3 days has been established, no prior linked entitlement is exhausted and no transitional protection applies. The weekly rate is min(£140 × 80%, £123.25) = £112; daily £22.40; total **£67.20**, not recoverable from HMRC ([s 157](https://www.legislation.gov.uk/ukpga/1992/4/section/157); [rates](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)). The historical comparison with a 3-day absence before 6 April 2026 cannot determine entitlement without linked-period and qualifying-day facts: Check this point with one of our partner accountants.

```oa-check
name: Original June 2026 SSP case, entitlement established
inputs:
  awe: 140
  days: 3
steps:
  - weekly: min(awe * 0.80, 123.25)
  - daily: weekly / 5
  - ssp: daily * days
expected:
  weekly: 112
  daily: 22.40
  ssp: 67.20
```

**Historical Case 4 / Pattern 4: £2,000 SMP recovery.** Assume £2,000 is valid Great Britain statutory SMP paid in a 2026/27 tax month, not an occupational top-up, and the employer made contribution payments in each of the 12 months of the qualifying tax year. Ordinary 92% recovery is £1,840. If total employee and employer Class 1 NIC, before Employment Allowance or other reductions, was £45,000 or less in the last complete tax year before the maternity qualifying week, Small Employers' Relief gives 109%, or £2,180. If contribution payments were made in fewer months or none, statutory annualisation or estimation can change the test; Check this point with one of our partner accountants. Claim through the EPS by the 19th of the following tax month for that month's reduction ([recovery](https://www.gov.uk/recover-statutory-payments); [recovery law](https://www.legislation.gov.uk/ukpga/1992/4/section/167), [small-employer test](https://www.legislation.gov.uk/uksi/1994/1882/regulation/2), [2026 amendment](https://www.legislation.gov.uk/uksi/2026/201/made); [EPS](https://www.gov.uk/running-payroll/reporting-to-hmrc-eps)).

```oa-check
name: Original 2000 statutory SMP recovery, 2026/27
inputs:
  smp: 2000
steps:
  - ordinary: smp * 0.92
  - small_employer: smp * 1.09
expected:
  ordinary: 1840
  small_employer: 2180
```

**Historical Case 5: £6,000 company car benefit, 2026/27, not payrolled.** Assume the £6,000 is an already-established taxable Class 1A benefit value, with required P11D/P11D(b) reporting and no exemption. At 15%, Class 1A is £900; report by 6 July 2027 and pay by 22 July 2027 (19 July by cheque). This does not calculate a car benefit from a car's cost, nor determine 2027/28 reporting ([rate](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027); [deadlines](https://www.gov.uk/employer-reporting-expenses-benefits/deadlines)).

```oa-check
name: Original established 6000 car benefit, 2026/27
inputs:
  benefit: 6000
steps:
  - class1a: benefit * 0.15
expected:
  class1a: 900
```

**Example 4 / historical Case 6: 12 employees, late FPS.** Retain 12 staff, a late FPS without valid reason, not the first failure, payments outside 3 days of payday. If HMRC establishes an ordinary chargeable monthly failure, the 10–49 employee band is £200. Also establish that the new-employer first-FPS-within-30-days easement does not apply. HMRC says payment within 30 days of getting the notice avoids interest. Assessment, appeal, annual-scheme status and any other defence remain a hold: Check this point with one of our partner accountants ([reg 67I](https://www.legislation.gov.uk/uksi/2003/2682/regulation/67I); [HMRC](https://www.gov.uk/guidance/what-happens-if-you-dont-report-payroll-information-on-time)).

## Ask the client first

Collect the registration/reference and first payday; P45/checklist, codes and loan notices; age/status and pay frequency; established statutory-pay entitlement; EA eligibility and relevant prior-year Class 1 totals; benefits and pension scheme basis. Reconcile these to payroll records before using any example.

## Sources

Read dates for the retained operative rules: **27 November 2026**; applicable completed UK NIC and Income Tax reads of **26 November 2026** reused for unchanged claims. The links beside each rule identify its authority. Additional operative legislation: [SSCBA ss 8–9A](https://www.legislation.gov.uk/ukpga/1992/4/section/8), [NIC earnings periods](https://www.legislation.gov.uk/uksi/2001/1004/regulation/3), [EA sole-director exclusion](https://www.legislation.gov.uk/ukpga/2014/7/section/2), [minimum wage amendment](https://www.legislation.gov.uk/uksi/2026/357/made), [pension qualifying earnings](https://www.legislation.gov.uk/ukpga/2008/30/section/13), [pension minimums](https://www.legislation.gov.uk/ukpga/2008/30/section/20), [FPS obligation](https://www.legislation.gov.uk/uksi/2003/2682/regulation/67B), [PAYE payment timing](https://www.legislation.gov.uk/uksi/2003/2682/regulation/69).

Not yet confirmed: None retained as usable instructions. The explicit partner-accountant holds above must be resolved before those topics can determine a payroll result.
