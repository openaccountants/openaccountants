---
name: us-social-contributions
description: >
  Compute ordinary United States federal Social Security and Medicare contributions
  for 2026 employees, employers and self-employed individuals. Covers FICA and
  SECA wage-base coordination, Additional Medicare Tax, multiple employers,
  FUTA, employment-tax deposits and returns, and totalization checks. Use for
  US social contributions, FICA, OASDI, Medicare payroll tax, Schedule SE,
  or wages plus self-employment income. Does not compute business profit,
  income-tax withholding, state unemployment tax or special occupational exemptions.
jurisdiction: US
category: federal
domain: tax
type: computation
tax_year: 2026
tax_year_notes: "2026 contributions; separate 2025 wage-base note"
tier: 2
last_updated: 2026-11-13
version: 0.1
depends_on: [us-tax-workflow-base]
---

# US federal social contributions v0.1

**General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick answer.** For 2026, ordinary covered wages bear Social Security at 6.2% each for employee and employer up to USD 184,500, and Medicare at 1.45% each without a wage ceiling. The employer also withholds 0.9% Additional Medicare above USD 200,000 paid to that employee; the individual's final threshold depends on filing status. Ordinary self-employment earnings use the 92.35% adjustment and the remaining personal Social Security base after wages. FUTA is employer-only and has a separate base and credit. [Publication 15, sections 9 and 14](https://www.irs.gov/publications/p15), [2026 Schedule SE](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf).

**Required inputs.** Tax year; worker and employer classification; covered wages and tips by person and employer; year-to-date payroll; W-2 Social Security and Medicare wages; net profit from every self-employment activity; spouse's Medicare wages/earnings for a joint return; filing status; state unemployment payments; deposit lookback; and any overseas work and certificate of coverage.

## Who this applies to

Use this guide to coordinate ordinary employee, employer and self-employed federal contributions. Establish covered employment and taxable compensation before applying a rate. Employees pay through withholding; employers remit both regular FICA shares and any Additional Medicare withholding; self-employed individuals calculate SECA on Schedule SE. Retirement age or receiving Social Security does not itself exempt self-employment earnings. [Publication 15, sections 2 and 9](https://www.irs.gov/publications/p15); [Schedule SE instructions, Who Must File](https://www.irs.gov/instructions/i1040sse).

Use `us-schedule-c-and-se-computation` to establish business profit and `us-form-941-940-payroll` for the complete payroll-return workflow. Check each companion's tax year before using its figures. This guide adds the contribution calculation and coordination across employment and self-employment; it does not prepare all income-tax withholding or business deductions.

Household, agricultural, church, ministerial, student, family, government and railroad work can have different coverage, thresholds, forms or exclusions. Do not assume that either the ordinary rules or an exemption applies from the occupation alone. Resolve those facts using the relevant service/payment category in [Publication 15, sections 3, 9, 14 and 15](https://www.irs.gov/publications/p15) and the [Schedule SE instructions](https://www.irs.gov/instructions/i1040sse) before computing. State unemployment and workers' compensation are outside this federal calculation.

**Circular 230 disclosure.** This reference does not constitute written advice for an identified taxpayer. Advice based on it must use reasonable factual and legal assumptions, consider all relevant facts, relate the law to those facts, and must not rely on the possibility that a return will not be audited. [31 CFR 10.37](https://www.ecfr.gov/current/title-31/subtitle-A/part-10/subpart-B/section-10.37).

## Rates, bands and thresholds

All amounts are USD. These are 2026 rules unless the row explicitly says 2025.

| Item and conditions | Rate or amount | Official authority and wording |
|---|---|---|
| Social Security, employee and employer each, covered wages | 6.2% each; annual base 184,500 | [Publication 15, section 9](https://www.irs.gov/publications/p15): "6.2% each"; "wage base limit is $184,500" |
| Prior-year comparison only: 2025 Social Security base | 176,100 | [SSA contribution and benefit base table](https://www.ssa.gov/oact/cola/cbb.html): "2025 176,100"; do not substitute the live page's 2027 amount for 2026 |
| Medicare, employee and employer each | 1.45% each, no wage ceiling | [Publication 15, section 9](https://www.irs.gov/publications/p15): "1.45% each"; "There is no wage base limit for Medicare tax" |
| Ordinary SE net-earnings adjustment, positive combined profit | 92.35% | [2026 Schedule SE, line 4a](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf): "multiply line 3 by 92.35% (0.9235)" |
| Ordinary Schedule SE filing threshold | Net earnings of 400 or more; special church/optional-method rules separate | [Schedule SE instructions, Who Must File](https://www.irs.gov/instructions/i1040sse): "$400 or more" |
| SE Social Security component | 12.4% of net earnings, limited by unused personal 184,500 base after covered wages | [2026 Schedule SE, lines 7-10](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf): "Multiply the smaller of line 6 or line 9 by 12.4%" |
| SE Medicare component | 2.9% of covered net earnings, no ceiling | [2026 Schedule SE, line 11](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf): "Multiply line 6 by 2.9% (0.029)" |
| Deductible part of ordinary SE tax, income-tax adjustment | 50%; Additional Medicare excluded | [2026 Schedule SE, line 13](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf): "Multiply line 12 by 50% (0.50)" |
| Additional Medicare rate, individual only | 0.9%; no employer matching tax | [IRS Additional Medicare questions and answers](https://www.irs.gov/businesses/small-businesses-self-employed/questions-and-answers-for-the-additional-medicare-tax): "0.9 percent" |
| Employer Additional Medicare withholding trigger | Wages it pays that employee above 200,000, regardless of filing status or spouse | [Publication 15, section 9](https://www.irs.gov/publications/p15): "in excess of $200,000 in a calendar year" |
| Final Additional Medicare threshold, married filing jointly | 250,000 combined Medicare wages and SE income | [IRS Additional Medicare questions and answers, threshold table](https://www.irs.gov/businesses/small-businesses-self-employed/questions-and-answers-for-the-additional-medicare-tax): "Married filing jointly $250,000" |
| Final Additional Medicare threshold, married filing separately | 125,000 | [IRS Additional Medicare questions and answers, threshold table](https://www.irs.gov/businesses/small-businesses-self-employed/questions-and-answers-for-the-additional-medicare-tax): "Married filing separate $125,000" |
| Final Additional Medicare threshold, other statuses | 200,000, including single, head of household and qualifying surviving spouse | [IRS Additional Medicare questions and answers, threshold table](https://www.irs.gov/businesses/small-businesses-self-employed/questions-and-answers-for-the-additional-medicare-tax): "Single $200,000" |
| FUTA, covered employers, employer-only | 6.0% on first 7,000 per employee annually | [Publication 15, section 14](https://www.irs.gov/publications/p15): "FUTA tax rate is 6.0%"; "first $7,000" |
| FUTA credit and conditional effective rate | Credit up to 5.4%; 0.6% only if full credit conditions met | [Publication 15, section 14](https://www.irs.gov/publications/p15): "maximum 5.4% credit"; "tax rate after credit is 0.6%" |
| California, 2026 FUTA credit reduction | 1.5% reduction; effective federal rate 2.1% when otherwise eligible for the full state credit | [DOL final 2026 credit reduction workbook](https://oui.doleta.gov/unemploy/docs/final_credit_states_2026.xlsx), California row, H13 = 0.015; 2.1% is 0.6% + 1.5% |
| US Virgin Islands, 2026 FUTA credit reduction | 0%; timely repayment removed the reduction | [DOL final 2026 credit reduction workbook](https://oui.doleta.gov/unemploy/docs/final_credit_states_2026.xlsx), USVI row, H14 = 0; November 10 update |

## The base

### Employee and employer FICA

Start with covered remuneration, including taxable benefits and tips, rather than assuming W-2 box 1 equals the Social Security or Medicare base. Accountable-plan reimbursements meeting the conditions are excluded; nonaccountable amounts are wages. Income-tax deductions for qualified tips or overtime do not remove otherwise covered wages from FICA. [Publication 15, sections 5, 6 and 9](https://www.irs.gov/publications/p15).

For each payroll, ordinary Social Security taxable wages are the smaller of current covered Social Security wages and the positive remainder of the annual base after that employer's prior covered wages. Multiply by 6.2% for each side. Multiply all covered current Medicare wages by 1.45% for each side. Compute the Additional Medicare withholding increment as 0.9% times:

`max(0, prior Medicare wages + current Medicare wages - 200000) - max(0, prior Medicare wages - 200000)`.

Withhold that increment from the employee; there is no corresponding employer share. Thresholds restart each calendar year. A successor employer may count predecessor wages only when the legal successor conditions apply. Ordinary unrelated employers do not share a payroll wage cap. [Publication 15, section 9](https://www.irs.gov/publications/p15).

### Self-employment and wage coordination

1. Establish each individual's total SE profit or loss from all included activities, including the applicable partnership amounts. Aggregate business gains and losses before computing the ordinary net-earnings adjustment; prepare a separate Schedule SE for each spouse.
2. For positive ordinary combined profit `P`, compute `N = P * 0.9235`. The ordinary filing test is whether net earnings reach 400, not whether profit or the projected balance due reaches that figure. Special church wages and optional methods require their own instructions.
3. Compute the remaining personal Social Security base `B = max(0, 184500 - covered Social Security wages and tips)`. Schedule SE line 8 also accounts for the specified unreported tips, Form 8919 wages and railroad retirement tier 1 amounts; use the actual line 8 instructions where present.
4. Compute Social Security SE tax `min(N, B) * 0.124` and Medicare SE tax `N * 0.029`. Their sum is Schedule SE line 12, flowing to Schedule 2 line 4 on the published 2026 Schedule SE.
5. Half of that ordinary SE tax is the deductible part on Schedule SE line 13, flowing to Schedule 1 line 15. Do not include Additional Medicare Tax in that deduction. Check the final annual destination schedules before filing.

[2026 Schedule SE, lines 3-13](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf); [Schedule SE instructions, More Than One Business and Joint Returns](https://www.irs.gov/instructions/i1040sse).

**AUDIT FLASH POINT**: A partner's status and services can determine whether distributive share or guaranteed payments are SE income. A limited-partner or LLC label alone does not resolve eligibility for the limited-partner exception. Establish the facts and applicable law before setting the input; do not use this calculation to decide a disputed classification. [Schedule SE instructions, Partnership Income or Loss](https://www.irs.gov/instructions/i1040sse).

### Additional Medicare on the individual's return

For ordinary Medicare-covered wages `W`, nonnegative covered SE income `N`, and the filing-status threshold `T`, calculate:

- Wage component: `max(0, W - T) * 0.009`.
- Remaining threshold for SE income: `max(0, T - W)`.
- SE component: `max(0, N - max(0, T - W)) * 0.009`.

For a joint return, include both spouses' wages and SE income for this tax; keep their ordinary Social Security bases separate. A self-employment loss does not reduce wages subject to Additional Medicare Tax. RRTA compensation uses a separate calculation and is not combined with ordinary Medicare wages/SE income. File Form 8959 when tax is due or Additional Medicare Tax was withheld, including when reconciliation produces a refund. [IRS Additional Medicare questions and answers, liability and Form 8959](https://www.irs.gov/businesses/small-businesses-self-employed/questions-and-answers-for-the-additional-medicare-tax).

### Multiple employers, errors and FUTA

| Situation | Treatment | Official source |
|---|---|---|
| Two unrelated employers each correctly withhold Social Security but combined wages exceed the annual base | Claim excess employee Social Security withholding as a credit on the individual's income-tax return; calculate separately for each spouse. Employers generally do not recover their proper matching shares through that employee credit | [IRS Topic 608](https://www.irs.gov/taxtopics/tc608) |
| One employer alone overwithholds Social Security | Seek employer correction. If not corrected, follow Form 843 refund procedures; do not treat it as the multiple-employer credit | [IRS Topic 608](https://www.irs.gov/taxtopics/tc608) |
| Each employer pays below its Additional Medicare withholding trigger but joint/spousal or combined income exceeds the final threshold | Reconcile Form 8959; cover the balance through estimated payments or additional income-tax withholding requested on Form W-4 | [IRS Additional Medicare questions and answers](https://www.irs.gov/businesses/small-businesses-self-employed/questions-and-answers-for-the-additional-medicare-tax) |
| Employee claims an income-tax withholding exemption | It does not by itself exempt covered wages from Social Security or Medicare | [Publication 15, section 9](https://www.irs.gov/publications/p15) |

For ordinary nonfarm/nonhousehold employment, FUTA coverage in 2026 is triggered by wages of at least USD 1,500 in any quarter of 2025 or 2026, or at least one employee for some part of a day in at least 20 different weeks in either year. Separate tests and statutory exclusions apply to other employment. Compute each employee's FUTA base independently of FICA; sum the first USD 7,000 of FUTA-covered annual wages. [Publication 15, section 14, Who must pay and Figuring FUTA tax](https://www.irs.gov/publications/p15).

The 0.6% FUTA rate is conditional: state unemployment contributions must be paid in full, on time, on all wages also subject to FUTA, and the state must not be a credit reduction state. A state exemption, late state payment or credit reduction can increase federal liability. Never withhold FUTA from employees. [Publication 15, section 14](https://www.irs.gov/publications/p15).

For 2026, the Department of Labor's final determination gives California a 1.5% credit reduction after approval of its BCR waiver. The US Virgin Islands repaid its advances before November 10 and has no 2026 reduction. Thus California's effective federal rate is 2.1% on the FUTA base when the other full-credit conditions are met; do not apply that rate to all states. Use the final annual Form 940/Schedule A to report the reduction. [DOL final 2026 credit reduction workbook](https://oui.doleta.gov/unemploy/docs/final_credit_states_2026.xlsx).

## Deadlines and filing

### Employer workflow

Obtain the EIN and employee identity/payroll records, classify coverage, calculate liabilities by pay date, and establish the deposit schedule before payroll starts. Deposits and tax returns are separate duties. Use electronic federal tax deposits through an IRS-supported payment method, selecting the correct EIN, form, period and amount. Verify current scheduling cutoffs before authorizing payment and retain the confirmation and bank settlement. [Publication 15, sections 1, 4 and 11](https://www.irs.gov/publications/p15).

| Requirement | Rule and conditions | Official authority |
|---|---|---|
| Ordinary 2026 Form 941 deposit lookback | July 1, 2024 through June 30, 2025; total reported liability at most 50,000 means monthly, above 50,000 means semiweekly. New-employer and Form 944/943 rules differ | [Publication 15, section 11, Lookback period](https://www.irs.gov/publications/p15) |
| Monthly deposits | By the 15th of the next month for that month's wage payments, subject to business-day rules | [Publication 15, section 11, Monthly Deposit Schedule](https://www.irs.gov/publications/p15) |
| Semiweekly deposits | Wednesday-Friday wage payments: following Wednesday; Saturday-Tuesday: following Friday; apply the legal-holiday/business-day rules | [Publication 15, section 11, Semiweekly Deposit Schedule](https://www.irs.gov/publications/p15) |
| Large accumulated liability | 100,000 or more accumulated on any day in a deposit period: next business day deposit. A monthly depositor becomes semiweekly the following day for the rest of that year and the following year | [Publication 15, section 11, $100,000 Next-Day Deposit Rule](https://www.irs.gov/publications/p15) |
| Form 941 filing | Last day of the month after the quarter: April 30, July 31, October 31, January 31; next business day for weekend/legal holiday. If all taxes timely deposited, file by the 10th day of the second month after the quarter | [2026 Form 941 instructions, When Must You File](https://www.irs.gov/instructions/i941) |
| FUTA deposits | Calculate quarterly; carry 500 or less forward. If accumulated liability exceeds 500, deposit by the last day of the next month. Fourth-quarter balance of 500 or less can be paid with Form 940. Weekend/holiday rule applies | [Publication 15, section 14, Depositing FUTA tax](https://www.irs.gov/publications/p15) |
| Annual FUTA return | Form 940, generally January 31 following the wage year, or February 10 if all FUTA tax deposited when due; adjust for weekends/legal holidays and check the annual instructions | [Form 940 instructions, When Must You File](https://www.irs.gov/instructions/i940) |

Do not accumulate the next-day test across separate deposit periods. Use liability before nonrefundable credits for that test. Check the small-liability payment-with-return exception and deposit-shortfall rules in Publication 15 before relying on them; payroll frequency does not set the deposit schedule. Keep FUTA deposits separate from Form 941 taxes. [Publication 15, section 11](https://www.irs.gov/publications/p15).

On the March 2026 Form 941 instructions, lines 5a and 5b cover Social Security wages and tips at the combined 12.4%, line 5c Medicare at 2.9%, and line 5d Additional Medicare wages at 0.9%; line 5e totals those taxes. Reconcile payroll rounding through the permitted fractions-of-cents adjustment on line 7. Report liabilities by pay date in the proper monthly record or Schedule B; do not use deposit dates. Submit through supported e-file software/provider or the instructed paper address, retain the accepted acknowledgement or mailing evidence, and reconcile deposits, Form 941 and annual W-2/W-3 totals. [2026 Form 941 instructions, lines 5a-5e, 7 and 16](https://www.irs.gov/instructions/i941).

### Individual workflow

File Schedule SE with the individual return; attach Form 8959 when required. The ordinary calendar-year 2026 income-tax return is due April 15, 2027 under [26 USC 6072(a)](https://uscode.house.gov/us/usc/119-124/t26/s6072/). Check any taxpayer-specific disaster, overseas or other relief. An extension to file does not extend payment. [IRS When to file](https://www.irs.gov/filing/individuals/when-to-file).

For ordinary calendar-year 2026 estimated payments, the installment dates are April 15, June 15 and September 15, 2026, and January 15, 2027. Use the full Form 1040-ES worksheet to decide whether estimates are required and calculate safe-harbor or annualized amounts; the Schedule SE USD 400 filing test is not an estimated-payment trigger. Additional income-tax withholding from wages can cover the projected SE/Additional Medicare balance. [2026 Form 1040-ES, General Rule and When To Pay Estimated Tax](https://www.irs.gov/pub/irs-pdf/f1040es.pdf); [IRS Estimated taxes](https://www.irs.gov/businesses/small-businesses-self-employed/estimated-taxes).

## Penalties and interest

| Failure or exposure | Rule | Official authority |
|---|---|---|
| Required deposit 1-5 days late | 2% of the underdeposit | [Publication 15, section 11, Deposit Penalties](https://www.irs.gov/publications/p15) |
| Required deposit 6-15 days late | 5% | [Publication 15, section 11, Deposit Penalties](https://www.irs.gov/publications/p15) |
| Required deposit at least 16 days late, before the higher notice trigger | 10% | [Publication 15, section 11, Deposit Penalties](https://www.irs.gov/publications/p15) |
| Paid directly to IRS rather than deposited when deposit required | Generally 10% | [Publication 15, section 11, Deposit Penalties](https://www.irs.gov/publications/p15) |
| Remains unpaid more than 10 days after first IRS notice, or on notice and demand for immediate payment, whichever earlier | 15% | [Publication 15, section 11, Deposit Penalties](https://www.irs.gov/publications/p15) |
| Trust fund recovery penalty | 100% of unpaid trust fund taxes, potentially assessed against a responsible person who willfully fails to collect/pay; includes employee FICA and withheld income tax, not the employer matching share | [IRS TFRP explanation](https://www.irs.gov/businesses/small-businesses-self-employed/employment-taxes-and-the-trust-fund-recovery-penalty-tfrp) |

These deposit rates are graduated alternatives for the deposit failure, not percentages to add together. Failure-to-file, failure-to-pay and individual estimated-tax penalties are distinct exposures. Interest can continue until payment and rates change quarterly; retrieve the applicable period's rate instead of treating today's rate as permanent. Evaluate available reasonable-cause or administrative relief against the facts; it is not automatic. [Publication 15, sections 11-12](https://www.irs.gov/publications/p15); [IRS Interest](https://www.irs.gov/payments/interest); [2026 Form 1040-ES](https://www.irs.gov/pub/irs-pdf/f1040es.pdf).

## Cross-border points

FICA depends on covered employment, place of services, employer and applicable exclusions; nonresident status or an income-tax treaty does not by itself establish an exemption. Examine the applicable nonresident employment and international social security agreement rules before removing wages. [Publication 15, section 9](https://www.irs.gov/publications/p15).

US citizens and residents ordinarily remain subject to SE tax on covered self-employment abroad. The foreign earned income exclusion does not reduce SE net earnings. A foreign employer's employee is not automatically self-employed merely because the employer is foreign. Nonresident aliens generally do not pay SE tax unless an applicable social security agreement assigns coverage to the United States. [Schedule SE instructions, US Citizens or Resident Aliens Living Outside the United States and Nonresident Alien](https://www.irs.gov/instructions/i1040sse).

Totalization agreements can assign coverage to one system and prevent dual contributions. Check the current SSA agreement list and the specific agreement's worker/assignment rules, then obtain the certificate of coverage from the covering country. Employers retain the certificate supporting employee exemption; a self-employed person claiming foreign coverage attaches the foreign certificate to the US return as instructed. Follow the current Schedule SE instructions for the Schedule 2 exemption entry rather than simply omitting an unexplained tax. [SSA agreements overview, Certificates of coverage](https://www.ssa.gov/international/agreements_overview.html); [Schedule SE instructions, Effect of international social security agreements](https://www.irs.gov/instructions/i1040sse).

## Two worked examples that recompute

### Example 1: employee and employer, plus conditional FUTA

A single employee has USD 80,000 of covered 2026 wages from one ordinary employer and no other earnings. Employee Social Security is 4,960 and Medicare is 1,160, totaling 6,120. The employer matches 6,120. No Additional Medicare is due. Assume all FUTA coverage and full state-credit conditions are met, including no state credit reduction: FUTA is 7,000 x 0.6% = 42, employer-only. Thus employer contributions here total 6,162 and both parties' contributions total 12,282, excluding state taxes. Rates and conditions: [Publication 15, sections 9 and 14](https://www.irs.gov/publications/p15).

```oa-check
name: 2026 employee and employer contributions with full FUTA credit
inputs:
  wages: 80000
  annual_base: 184500
  ss_rate: 0.062
  med_rate: 0.0145
  additional_rate: 0.009
  single_threshold: 200000
  futa_base: 7000
  net_futa_rate: 0.006
steps:
  - employee_ss: min(wages, annual_base) * ss_rate
  - employee_med: wages * med_rate
  - employee_regular: employee_ss + employee_med
  - employer_regular: employee_ss + employee_med
  - additional: max(0, wages - single_threshold) * additional_rate
  - futa: min(wages, futa_base) * net_futa_rate
  - employer_total: employer_regular + futa
  - combined_total: employee_regular + employer_total + additional
expected:
  employee_ss: 4960
  employee_med: 1160
  employee_regular: 6120
  employer_regular: 6120
  additional: 0
  futa: 42
  employer_total: 6162
  combined_total: 12282
```

### Example 2: wages and self-employment, partial remaining base

A single taxpayer has USD 170,000 Social Security and Medicare wages from one employer and USD 100,000 ordinary net SE profit. No other income, special methods or exemptions apply. Adjusted SE earnings are 92,350. Remaining Social Security base is 14,500, giving SE Social Security of 1,798 and SE Medicare of 2,678.15. Ordinary SE tax is 4,476.15 and its half deduction, rounded to cents for this illustration, is 2,238.08. The remaining Additional Medicare threshold is 30,000, so the SE component is (92,350 - 30,000) x 0.9% = 561.15. The employer withheld no Additional Medicare because its wages did not exceed 200,000; the individual must still reconcile and fund the 561.15. Return software may use permitted whole-dollar rounding. [2026 Schedule SE](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf); [IRS Additional Medicare questions and answers](https://www.irs.gov/businesses/small-businesses-self-employed/questions-and-answers-for-the-additional-medicare-tax).

```oa-check
name: 2026 wages plus self-employment with remaining Social Security base
inputs:
  ss_wages: 170000
  med_wages: 170000
  profit: 100000
  annual_base: 184500
  net_factor: 0.9235
  se_ss_rate: 0.124
  se_med_rate: 0.029
  threshold: 200000
  additional_rate: 0.009
steps:
  - net_se: profit * net_factor
  - remaining_ss: max(0, annual_base - ss_wages)
  - se_ss: min(net_se, remaining_ss) * se_ss_rate
  - se_med: net_se * se_med_rate
  - se_tax: se_ss + se_med
  - deduction: round(se_tax * 0.5, 2)
  - additional_wages: max(0, med_wages - threshold) * additional_rate
  - remaining_additional_threshold: max(0, threshold - med_wages)
  - additional_se: max(0, net_se - remaining_additional_threshold) * additional_rate
  - additional_total: additional_wages + additional_se
expected:
  net_se: 92350
  remaining_ss: 14500
  se_ss: 1798
  se_med: 2678.15
  se_tax: 4476.15
  deduction: 2238.08
  remaining_additional_threshold: 30000
  additional_total: 561.15
```

## Ask the client first

- Which tax year, filing status, spouse and residency facts apply?
- What covered wages/tips did each employer pay each person, including predecessor wages, taxable benefits, corrections, unreported tips or Form 8919 amounts?
- What is the established net profit/loss from every business and partnership, and does any classification or optional SE method need specialist review?
- Are there household, agricultural, church, student, family, government or railroad services requiring different coverage?
- Which state unemployment systems apply, were all required contributions paid on time, and what is the final tax-year FUTA credit reduction status?
- What deposit lookback, pay dates, deposits, notices, estimates and withholding are documented? What foreign work and coverage certificates exist?

## Sources

These official sources were opened and the stated sections read on the dates below; the DOL workbook evidence was supplied by the coordinating agent. Source verification is not accountant approval; this version remains tier 2, not yet approved.

| Source | Read date | Sections actually read and use |
|---|---|---|
| [IRS Publication 15 (2026)](https://www.irs.gov/publications/p15) | 2026-11-13 | Read for sections 5-6 compensation/tips; 9 Social Security, Medicare and foreign coverage; 11 deposit schedules, next-day rule and penalties; 12 filing; 14 FUTA coverage, credit, deposits; section 15 service/payment scope |
| [SSA contribution and benefit base](https://www.ssa.gov/oact/cola/cbb.html) | 2026-11-13 | Read for annual table's 2025 and 2026 rows; Medicare no-ceiling discussion; live 2027 figure kept separate |
| [2026 Schedule SE](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf) | 2026-11-13 | Read for lines 3-13: net earnings, wage coordination, component taxes and deduction |
| [Schedule SE instructions (2026)](https://www.irs.gov/instructions/i1040sse) | 2026-11-13 | Read for Who Must File; multiple businesses; joint returns; partnership income; foreign residence and totalization |
| [IRS Additional Medicare questions and answers](https://www.irs.gov/businesses/small-businesses-self-employed/questions-and-answers-for-the-additional-medicare-tax) | 2026-11-13 | Read for rate/status table, employer threshold, wages plus SE examples, losses, RRTA separation and Form 8959 |
| [Form 941 instructions (March 2026)](https://www.irs.gov/instructions/i941) | 2026-11-13 | Read for filing/deposits, lines 5a-5e, 7 and liability schedule on line 16 |
| [Form 940 instructions (2025)](https://www.irs.gov/instructions/i940) | 2026-11-13 | Read for general annual filing rule and e-filing; not used for 2026 state credit-reduction determinations |
| [DOL final 2026 credit reduction workbook](https://oui.doleta.gov/unemploy/docs/final_credit_states_2026.xlsx) | 2026-11-13 | Coordinating agent read for November 10 update, California BCR waiver and 1.5% reduction, USVI repayment and zero reduction; cells H13-H14 |
| [IRS Topic 608](https://www.irs.gov/taxtopics/tc608) | 2026-11-13 | Read for excess employee Social Security: multiple-employer credit versus single-employer refund |
| [SSA agreements overview](https://www.ssa.gov/international/agreements_overview.html) | 2026-11-13 | Read for coverage assignment and certificates for employees/self-employed persons |
| [IRS TFRP](https://www.irs.gov/businesses/small-businesses-self-employed/employment-taxes-and-the-trust-fund-recovery-penalty-tfrp) | 2026-11-13 | Read for responsible person, willfulness and trust fund amount |
| [IRS Interest](https://www.irs.gov/payments/interest) | 2026-11-13 | Read for accrual and quarterly rate changes |
| [2026 Form 1040-ES](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) | 2026-11-13 | Read for General Rule and installment payment dates |
| [IRS Estimated taxes](https://www.irs.gov/businesses/small-businesses-self-employed/estimated-taxes) | 2026-11-13 | Read for SE tax in estimates and additional wage withholding |
| [26 USC 6072(a), US House](https://uscode.house.gov/us/usc/119-124/t26/s6072/) | 2026-11-13 | Read for calendar-year individual return due date |
| [IRS When to file](https://www.irs.gov/filing/individuals/when-to-file) | 2026-11-13 | Read for extension does not extend payment; taxpayer-specific relief |
| [31 CFR 10.37](https://www.ecfr.gov/current/title-31/subtitle-A/part-10/subpart-B/section-10.37) | 2026-11-13 | Read for written-advice factual and legal standards |

Not yet confirmed: final 2026 Form 940/Schedule A line mappings are not supplied here; verify the final annual form before filing. The 2026 state credit reductions above come from the DOL determination. Special occupational coverage, optional SE methods and taxpayer-specific foreign certificates/relief require the stated separate checks; this guide does not assert an exemption.
