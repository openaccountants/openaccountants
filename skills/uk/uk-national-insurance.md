---
name: uk-national-insurance
description: "Compute UK National Insurance for 2026/27: ordinary employee and employer Class 1, directors, self-employed Classes 2 and 4, voluntary contributions and payment deadlines. Includes dated historical cases and explicit referrals for special categories, relief eligibility, credits and cross-border work."
version: 3.3
jurisdiction: GB
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - social-contributions-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# UK National Insurance contributions (2026/27)

Use the earnings period and category letter before calculating NIC. Equal monthly pay does not make annual thresholds interchangeable with monthly thresholds. Figures below are for 6 April 2026 to 5 April 2027 unless expressly dated otherwise ([HMRC rates](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).

## Who this applies to

Ordinary UK employees, employers, company directors and self-employed earners. Use `uk-self-employment-sa103` for trading-profit computation and `uk-payroll` for the wider payroll process. Confirm employment status, age, earnings period, category and territorial coverage before using a formula.

Employee Class 1 normally stops at State Pension age; employer Class 1 can continue ([SSCBA s.6](https://www.legislation.gov.uk/ukpga/1992/4/section/6/data.xml)). **Out of Class 4: a person over State Pension age at the start of the tax year, and a person not resident in the UK for income tax in that year** ([SSCR reg.91](https://www.legislation.gov.uk/uksi/2001/1004/regulation/91/data.xml)). Reaching State Pension age during a year normally stops Class 4 only from the following 6 April ([HMRC](https://www.gov.uk/national-insurance)). Do not infer residence or pension age from the amount of profit.

For employment status, under-age workers, unusual categories or exemptions: **Check this point with one of our partner accountants.**

## Rates, bands and thresholds

These Class 1 thresholds are earnings-period figures. Use the weekly or monthly column for that period; the annual column applies where the annual earnings-period rules actually apply.

| Class 1 threshold | Weekly | Monthly | Annual | Source |
|---|---|---|---|---|
| Lower earnings limit (LEL) | GBP 129 | GBP 559 | GBP 6,708 | [HMRC 2026/27](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) |
| Primary threshold (PT) | GBP 242 | GBP 1,048 | GBP 12,570 | [HMRC 2026/27](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) |
| Secondary threshold (ST) | GBP 96 | GBP 417 | GBP 5,000 | [HMRC 2026/27](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) |
| Upper earnings limit (UEL); under-21 upper secondary threshold | GBP 967 | GBP 4,189 | GBP 50,270 | [HMRC 2026/27](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) |

| Item and conditions | Rate or amount | Year | Source |
|---|---|---|---|
| Employee Class 1, confirmed category A: earnings above PT through UEL; excess above UEL | 8%; 2% respectively | 2026/27 | [SSCBA s.8](https://www.legislation.gov.uk/ukpga/1992/4/section/8/data.xml); [HMRC](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) |
| Employer Class 1, ordinary category A: earnings above ST, no upper cap | 15% | 2026/27 | [SSCBA s.9](https://www.legislation.gov.uk/ukpga/1992/4/section/9/data.xml) |
| Under-21 employee, category M: employer rate up to upper secondary threshold; above it | 0%; 15% respectively | 2026/27 | [SSCBA s.9A](https://www.legislation.gov.uk/ukpga/1992/4/section/9A/data.xml); [HMRC](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) |
| Employment Allowance, eligible employer only; capped at eligible employer Class 1 liability | Up to GBP 10,500 | 2026/27 | [HMRC allowance](https://www.gov.uk/claim-employment-allowance) |
| Class 1A on liable expenses/benefits or liable termination/testimonial amounts; classification referred below | 15% | 2026/27 | [HMRC](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) |
| Class 1B under an agreed PAYE Settlement Agreement (PSA); computation referred below | 15% | 2026/27 | [HMRC](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) |
| Ordinary self-employed Class 2: small profits threshold (SPT); optional weekly rate below it | GBP 7,105; GBP 3.65 | 2026/27 | [SSCBA s.11](https://www.legislation.gov.uk/ukpga/1992/4/section/11/data.xml); [HMRC](https://www.gov.uk/self-employed-national-insurance-rates) |
| Class 4, liable profits above lower limit through upper limit; excess above upper limit | GBP 12,570; GBP 50,270; 6%; 2% respectively | 2026/27 | [SSCBA s.15](https://www.legislation.gov.uk/ukpga/1992/4/section/15/data.xml) |
| Voluntary Class 3, eligibility must be established | GBP 18.40 a week | 2026/27 | [HMRC voluntary rates](https://www.gov.uk/voluntary-national-insurance-contributions/rates) |
| 2025/26 figures (for 2025/26 returns and voluntary payments due by 31 January 2027) | LEL GBP 125 a week; small profits threshold GBP 6,845; voluntary Class 2 GBP 3.50 a week; Class 3 GBP 17.75 a week | 2025/26 | [HMRC NIC rates](https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions) |
| Historical employer Class 1 above ST; Employment Allowance if eligible | 13.8% above GBP 9,100 annually (GBP 175 weekly, GBP 758 monthly); allowance up to GBP 5,000 | 2024/25 only | [HMRC 2024/25](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025) |
| Historical ordinary Class 2 SPT and voluntary weekly rate; Class 3 weekly rate | GBP 6,725; GBP 3.45; GBP 17.45 respectively | 2024/25 only | [HMRC NIC rates](https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions) |
| Historical Class 4 lower/upper limits and rates | GBP 12,570; GBP 50,270; 6%; 2% respectively | 2024/25 and 2025/26 | [HMRC NIC rates](https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions) |

The 31 January date in the dated row describes ordinary Self Assessment payment timing, not the final deadline for every voluntary contribution. See the separate voluntary window below. Historical figures are not current-year defaults.

## The base

**Class 1.** For a confirmed ordinary category A employee below State Pension age, compute each earnings period: employee NIC = 8% × max(min(NIC earnings, UEL) − PT, 0) + 2% × max(NIC earnings − UEL, 0); employer NIC = 15% × max(NIC earnings − ST, 0). Regular monthly pay normally has a monthly earnings period ([SSCR reg.3](https://www.legislation.gov.uk/uksi/2001/1004/regulation/3/data.xml); [SSCBA ss.8–9](https://www.legislation.gov.uk/ukpga/1992/4/section/8/data.xml)). Under the exact-percentage method, calculate employee and employer NIC separately and round each to the nearest penny, disregarding a halfpenny or less ([SSCR reg.12](https://www.legislation.gov.uk/uksi/2001/1004/regulation/12/data.xml)). The LEL-to-PT band can protect the record without employee NIC; it is not a guarantee of a whole qualifying year ([HMRC overview](https://www.gov.uk/national-insurance)).

For category M, the under-21 employer relief ends at the applicable upper secondary threshold; ordinary employee rates still apply. Recheck age/category when it changes ([SSCBA s.9A](https://www.legislation.gov.uk/ukpga/1992/4/section/9A/data.xml); [HMRC rates](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)). For reduced-rate married women/widows (B, E, I), deferment (D, J, L, Z), pension-age categories (C, K, S), apprentices under 25 (H), veterans (V), Freeport/Investment Zone letters (F, I, L, S, N, E, D, K), X, relief duration/elections, special-site and apprenticeship evidence: **Check this point with one of our partner accountants.** Do not select a relief from age, location or a category letter alone.

**Multiple jobs.** Separate employment is normally assessed separately, subject to statutory exceptions. For aggregation across the same/associated employers, annual maximums, refunds, deferment, CA72A and its application deadline: **Check this point with one of our partner accountants.** ([SSCBA s.6(5)](https://www.legislation.gov.uk/ukpga/1992/4/section/6/data.xml)).

**Directors.** A director in office at the beginning of the tax year has an annual earnings period even if they cease being a director during it. Appointment during the year uses the number of weeks from the appointment week to year end; confirm appointment dates before using thresholds ([SSCR reg.8(2)–(3)](https://www.legislation.gov.uk/uksi/2001/1004/regulation/8/data.xml)). Under the standard method, use cumulative annual salary/bonus and deduct NIC already paid; the FPS method code is AN. Under the alternative method, calculate per period during the year and recalculate at year end, deducting any further employee NIC from the last payment; code AL. Use payroll software. A departing director who remains employed stays on the annual basis for that year ([HMRC directors](https://www.gov.uk/employee-directors)). For category changes, part-year or former-director payments, dividend classification and alternative-method eligibility: **Check this point with one of our partner accountants.**

**Employment Allowance.** Only after eligibility is established, deduct the lesser of the available allowance and eligible employer Class 1 liability. A company whose sole director is its only employee liable for secondary Class 1 cannot claim ([HMRC eligibility](https://www.gov.uk/claim-employment-allowance/eligibility)). The statute's excluded-company test concerns all payments of earnings in relation to which the company is the secondary contributor, made to the same employed earner who is a director whenever paid ([NICA 2014 s.2(4A)](https://www.legislation.gov.uk/ukpga/2014/7/section/2/data.xml)). Merely having an administrator does not prove eligibility. For public-sector work/charities, care workers and domestic staff, IR35, connected companies/payrolls, business transfers, avoidance, nil-rated second employees, EPS claims, annual renewal, backclaims and set-off/refunds: **Check this point with one of our partner accountants.**

**Classes 1A/1B.** The rate alone does not establish a charge. For taxable-benefit and payrolling/P11D(b) treatment, termination awards including the former GBP 30,000 example threshold, sporting testimonials including the former GBP 100,000 threshold, Class 1 overlap, PSA item eligibility, tax gross-up and the Class 1B base: **Check this point with one of our partner accountants.** Do not apply those thresholds to all termination or testimonial payments.

**Class 4.** Start with the year's liable profits, computed under SSCBA s.15 and Schedule 2, from all relevant trades/professions/vocations; exclude wholly overseas trades from this ordinary formula. Class 4 = 6% × max(min(profit, 50,270) − 12,570, 0) + 2% × max(profit − 50,270, 0). No Class 4 arises at or below the lower limit. Confirm adjustments, losses and exemptions before treating accounting profit as liable profit ([SSCBA s.15](https://www.legislation.gov.uk/ukpga/1992/4/section/15/data.xml)). For basis-period reform, transition profits, loss relief, partnership status, combined employment/self-employment annual limits and special exemptions: **Check this point with one of our partner accountants.**

**Class 2.** In ordinary self-employment within s.11, relevant profits at or above the SPT give contributions treated as paid for each week in that employment; below the SPT payment is optional. The ordinary rule excludes weeks before the week of attaining 16 and after the week of attaining pensionable age. Do not convert part-year self-employment into a whole qualifying year automatically ([SSCBA s.11(5A)–(7)](https://www.legislation.gov.uk/ukpga/1992/4/section/11/data.xml)). For examiners, moderators, invigilators/question setters (including Special Class 4 payment), landlords, ministers without salary/stipend, non-business investors without commission, mariners, share fishermen and volunteer development workers: **Check this point with one of our partner accountants.**

**Deductibility and records.** The trader's own Class 2/Class 4 contributions are not deductible in computing trading profit. ITTOIA s.53's prohibition does not apply to employer secondary Class 1, Class 1A or Class 1B; this is not itself permission to deduct every payment regardless of other rules ([ITTOIA s.53](https://www.legislation.gov.uk/ukpga/2005/5/section/53/data.xml)). Reconcile HMRC payments/refunds to payroll, the Self Assessment statement and tax computation; never classify a bank transaction solely from its reference, date or approximate amount. Preserve an audit trail of inputs, period, category, calculation and evidence.

**Voluntary contributions, credits and pension.** First obtain the NI record and pension forecast; do not promise that paying increases the pension ([HMRC voluntary overview](https://www.gov.uk/voluntary-national-insurance-contributions)). Class 2 for the previous tax year and Class 3 for the previous two years use those years' original rates; earlier years normally use the current rate ([HMRC voluntary rates](https://www.gov.uk/voluntary-national-insurance-contributions/rates)). For voluntary eligibility/reduced-rate exclusions, available weeks, monthly Direct Debits, payment references, registration, record-update times or disputed records: **Check this point with one of our partner accountants.** For credits (Class 1 versus Class 3; JSA, ESA, Maternity Allowance, Carer's Allowance/Scottish Carer Support Payment, statutory sick/parental pay, Universal Credit, Child Benefit, foster/kinship carers and family childcare), application/transfer rules, reconsideration, qualifying years, pre-2016/contracted-out records and the pension amount: **Check this point with one of our partner accountants.**

## Deadlines and filing

| What | Ordinary timing | Source |
|---|---|---|
| FPS for payroll pay and deductions | On or before payday; late-reporting exceptions require checking | [HMRC FPS](https://www.gov.uk/running-payroll/reporting-to-hmrc) |
| Monthly PAYE/Class 1 payment | 22nd of next tax month; postal cheque must reach HMRC by 19th | [HMRC PAYE](https://www.gov.uk/pay-paye-tax) |
| Quarterly PAYE/Class 1, only where quarterly payment applies | 22nd after quarter end; postal cheque by 19th | [HMRC PAYE](https://www.gov.uk/pay-paye-tax) |
| Report 2026/27 benefits/Class 1A, including P11D(b) where required | 6 July 2027 | [HMRC benefits deadlines](https://www.gov.uk/employer-reporting-expenses-benefits/deadlines) |
| Pay 2026/27 Class 1A on benefits | 22 July 2027; 19 July by cheque | [HMRC benefits deadlines](https://www.gov.uk/employer-reporting-expenses-benefits/deadlines) |
| Apply for PSA first covering 2026/27 | 5 July 2027; permitted items depend on application timing | [HMRC PSA](https://www.gov.uk/paye-settlement-agreements/deadlines-and-payment) |
| Pay 2026/27 PSA tax/Class 1B | 22 October 2027; 19 October by post | [HMRC PSA](https://www.gov.uk/paye-settlement-agreements/deadlines-and-payment) |

For Self Assessment filing, Class 4/voluntary Class 2 collection, balancing payments and payments on account (including exceptions and reductions), late notices, quarterly-payment eligibility, EPS and submission/payment references: **Check this point with one of our partner accountants.** The dated 2025/26 row is not a complete filing instruction.

The ordinary voluntary contribution window is six years, with a 5 April deadline: 2025/26 gaps until 5 April 2032; 2026/27 gaps until 5 April 2033 (derived from the same window). Eligibility and exceptional deadlines still need checking ([HMRC voluntary deadlines](https://www.gov.uk/voluntary-national-insurance-contributions/deadlines)). For the correct payment route or an exception: **Check this point with one of our partner accountants.**

## Penalties and interest

For FPS late filing, PAYE/Class 1 late payment, P11D(b), Class 1A/1B, Self Assessment and Making Tax Digital penalty regimes, commencement, grace periods, reasonable excuse, appeals and interest on penalties: **Check this point with one of our partner accountants.** Do not reuse a penalty percentage from another regime or tax year.

Ordinary HMRC late-payment interest was 7.75% from 9 January through 23 November 2026 and is 8.00% from 24 November 2026. Split a calculation where the rate changes; actual chargeability and day count need checking ([HMRC interest](https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates)). **Check this point with one of our partner accountants.**

## Cross-border points

The domestic Class 4 residence exception is stated above. For residence determination, inbound/outbound or multi-state workers, social security agreements, certificates of coverage, non-agreement temporary postings and the former 52-week rule, Class 2 abroad, and Class 3 abroad including post-April-2026 eligibility and transitional applications: **Check this point with one of our partner accountants.** No overseas contribution entitlement follows from a UK profit figure alone.

## Two worked examples that recompute

All amounts are GBP. Unless a case expressly says otherwise, assume ordinary UK coverage, confirmed category A, age within employee contribution liability throughout, no aggregation or special relief, the exact-percentage method and no Employment Allowance. For self-employment, assume the stated figure is total liable UK trading profit after adjustments, ordinary Class 2 eligibility, and no age/residence exemption. These are explicit case assumptions, not facts to infer for a real person. Rates: [2026/27 employer](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027), [historical NIC](https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions), [voluntary](https://www.gov.uk/voluntary-national-insurance-contributions/rates).

**Example 1 / historical Case C2: GBP 60,000 employee, paid GBP 5,000 each month in 2026/27.** Monthly employee NIC is (4,189 − 1,048) × 8% + (5,000 − 4,189) × 2% = 251.28 + 16.22 = 267.50; annual total 3,210.00. Monthly employer NIC is (5,000 − 417) × 15% = 687.45; annual total 8,249.40. The former annual-threshold results 3,210.60 and 8,250.00 are not the totals for these monthly facts.

```oa-check
name: Employee GBP 60000 monthly category A 2026/27
inputs:
  pay: 60000
steps:
  - monthly_pay: pay / 12
  - ee_main: (4189 - 1048) * 0.08
  - ee_upper: (monthly_pay - 4189) * 0.02
  - monthly_employee_nic: ee_main + ee_upper
  - employee_nic: monthly_employee_nic * 12
  - monthly_employer_nic: (monthly_pay - 417) * 0.15
  - employer_nic: monthly_employer_nic * 12
expected:
  monthly_pay: 5000
  ee_main: 251.28
  ee_upper: 16.22
  monthly_employee_nic: 267.50
  employee_nic: 3210.00
  monthly_employer_nic: 687.45
  employer_nic: 8249.40
```

**Example 2: director with March bonus and small sole trade, 2026/27.** Original facts: sole director plus full-time administrator; director in office on 6 April 2026, salary 12,570 paid as 1,047.50 a month, bonus 20,000 in March 2027, sole-trade profit 8,000. Assume director remains category A and within relevant age/UK coverage throughout; no other liable profits. Annual earnings 32,570 give employee NIC 1,600.00 and employer NIC 4,135.50 before any allowance. Administrator pay/secondary liability and other allowance facts are unknown: no allowance entitlement or net employer bill is concluded. **Check this point with one of our partner accountants.**

For comparison only, an ordinary monthly employee on that same salary/bonus would pay 588.45 in March and nil in the other months, a difference of 1,011.55; that is not a director's permitted saving. Class 4 on the sole trade is nil. Class 2 is treated as paid for eligible weeks; 8,000 profit alone does not prove a complete qualifying year.

```oa-check
name: Director annual earnings period with bonus plus side trade 2026/27
inputs:
  salary: 12570
  bonus: 20000
  trade_profit: 8000
steps:
  - annual_pay: salary + bonus
  - director_ee_nic: (min(annual_pay, 50270) - 12570) * 0.08
  - director_er_nic: (annual_pay - 5000) * 0.15
  - march_pay: salary / 12 + bonus
  - march_only_ee_nic: (4189 - 1048) * 0.08 + (march_pay - 4189) * 0.02
  - saving_blocked: director_ee_nic - march_only_ee_nic
  - class4: max(min(trade_profit, 50270) - 12570, 0) * 0.06
expected:
  annual_pay: 32570
  director_ee_nic: 1600.00
  director_er_nic: 4135.50
  march_only_ee_nic: 588.45
  saving_blocked: 1011.55
  class4: 0
```

### Earlier cases, with their original years and inputs

Use the assumptions above and the dated rates. Voluntary totals assume exactly 52 eligible weeks, an effective choice to pay and confirmation that payment is permitted/useful; they do not promise a pension increase. Unknown eligibility or a different payment schedule requires recalculation or referral.

- **C1, 2026/27 employee salary 35,000 spread evenly:** explicitly assume monthly payments of 2,916.67 for eleven months and 2,916.63 in the last. Employee NIC rounds to 149.49 each month, total 1,793.88; employer NIC rounds to 374.95 for eleven months and 374.94 in the last, total 4,499.39. Annual-threshold amounts 1,794.40/4,500.00 do not apply to that schedule.
- **C3 / old Test 1, profit 30,000 in 2026/27 / 2025/26; old Test 8, profit 30,000 in 2024/25:** Class 4 = (30,000 − 12,570) × 6% = 1,045.80 in each stated year. Ordinary Class 2 is treated as paid for eligible weeks under that year's SPT; no contribution payment is required for those weeks.
- **C4 / old Test 2, profit 80,000 in 2026/27 / 2025/26:** Class 4 = 37,700 × 6% + 29,730 × 2% = 2,262.00 + 594.60 = 2,856.60 in each year.
- **C5, 2026/27 profit 6,000:** Class 4 nil; ordinary Class 2 is not treated as paid from these profits. At 52 eligible weeks, optional Class 2 = 3.65 × 52 = 189.80; Class 3 arithmetic = 18.40 × 52 = 956.80 only if eligible for that class. Check credits/forecast before choosing.
- **C6, 2026/27 four employees each on 30,000, eligible for full unused allowance:** assume 2,500 paid monthly each, all category A. Employer NIC = 312.45 × 12 × 4 = 14,997.60; less 10,500 = 4,497.60. Variation: one employee is category M and aged at least 16 but under 21 throughout; that employee's employer NIC is nil. The other three cost 11,248.20; net 748.20. Annual salary totals cannot replace pay periods.
- **C7, 2026/27 sole director as only employee, salary 12,570:** assume director at year start and throughout, category A. Employee NIC nil; employer NIC = (12,570 − 5,000) × 15% = 1,135.50. No Employment Allowance on these stipulated sole-employee facts.
- **C8, sole trader reaching State Pension age on 10 October 2026, also employed:** age timing alone does not exempt 2026/27 Class 4; the age exemption starts 6 April 2027. Employee Class 1 normally stops at State Pension age; employer liability can continue. Profit, pay and category must be established before giving amounts.
- **C9, 2025/26 profit 6,500, ordinary return/payment date 31 January 2027:** below that year's SPT 6,845. Optional ordinary Class 2 for 52 eligible weeks = 3.50 × 52 = 182.00, if paid while the original-rate rule applies. Class 4 nil. Filing/payment exceptions are referred above.
- **Old Test 3, 2025/26 profit 10,000:** Class 4 nil; above SPT 6,845 so ordinary Class 2 treated as paid for eligible weeks.
- **Old Tests 4 and 5, 2025/26 profit 5,000 and loss −3,000, respectively:** Class 4 nil in each. For an eligible ordinary voluntary payer choosing 52 weeks at the original rate, Class 2 = 3.50 × 52 = 182.00 in each case.
- **Old Test 6, 2025/26 salary 45,000 plus trade profit 20,000:** stand-alone Class 4 formula gives (20,000 − 12,570) × 6% = 445.80 before any combined-contributions adjustment. Salary alone does not determine actual Class 1 or the annual maximum; no final combined NIC total is stated. **Check this point with one of our partner accountants.**
- **Old Test 7, 2025/26 age 69, profit 40,000:** explicitly assume already over State Pension age at the start of that tax year and throughout it; Class 4 nil. The age is not a substitute for checking the actual date and exemption.
- **Old employer Tests 9–11, salary 35,000, allowance-ineligible:** explicitly assume a genuine annual earnings period (regular annual pay under reg.3), ordinary category A and full-year coverage. For 2024/25: (35,000 − 9,100) × 13.8% = 3,574.20. For 2025/26 and 2026/27: (35,000 − 5,000) × 15% = 4,500.00. Increase = 925.80, approximately 25.9%. These conditional annual-period results are not monthly payroll totals; C1 shows the monthly case.
- **Old employer Test 12, 2025/26 two employees each on 25,000, allowance-eligible:** explicitly assume genuine annual earnings periods, category A and full unused allowance 10,500. Gross employer NIC = 2 × (25,000 − 5,000) × 15% = 6,000; allowance restricted to 6,000; net nil.
- **Earlier HMRC weekly case, 2026/27 category A pay 1,000:** employee NIC = (967 − 242) × 8% + (1,000 − 967) × 2% = 58.00 + 0.66 = 58.66 ([HMRC example](https://www.gov.uk/national-insurance-rates-letters)).

## Ask the client first

Obtain the year, employment/self-employment/director status, date of birth and pension age; pay dates and NIC earnings per period; category and any category changes; appointment/cessation dates; all jobs and trading profits/adjustments; residence and overseas work; benefits/termination/PSA facts; employer relief and allowance evidence, other staff and their secondary liability, connected payrolls/entities; and the NI record, credits and pension forecast. Stop a computation whose material inputs are missing. Retain source documents and a reconciliation of payments to the relevant liability rather than a guessed bank-reference classification.

## Sources

| Source and what was read | URL | Read date |
|---|---|---|
| SSCBA s.6: primary/secondary liability, pension age and separate employments | https://www.legislation.gov.uk/ukpga/1992/4/section/6/data.xml | 2026-11-26 |
| SSCBA s.8: employee main/additional bands and percentages | https://www.legislation.gov.uk/ukpga/1992/4/section/8/data.xml | 2026-11-26 |
| SSCBA s.9: employer percentage and threshold | https://www.legislation.gov.uk/ukpga/1992/4/section/9/data.xml | 2026-11-26 |
| SSCBA s.9A: under-21 relief and upper limit | https://www.legislation.gov.uk/ukpga/1992/4/section/9A/data.xml | 2026-11-26 |
| SSCBA s.11: relevant profits, eligible weeks, age and voluntary payment | https://www.legislation.gov.uk/ukpga/1992/4/section/11/data.xml | 2026-11-26 |
| SSCBA s.15: liable profits, limits and rates | https://www.legislation.gov.uk/ukpga/1992/4/section/15/data.xml | 2026-11-26 |
| SSCR regs.3, 8, 12, 91: earnings periods, directors, rounding and Class 4 exemptions | https://www.legislation.gov.uk/uksi/2001/1004/regulation/3/data.xml ; https://www.legislation.gov.uk/uksi/2001/1004/regulation/8/data.xml ; https://www.legislation.gov.uk/uksi/2001/1004/regulation/12/data.xml ; https://www.legislation.gov.uk/uksi/2001/1004/regulation/91/data.xml | 2026-11-26 |
| NICA 2014 s.2: excluded companies and liabilities | https://www.legislation.gov.uk/ukpga/2014/7/section/2/data.xml | 2026-11-26 |
| ITTOIA s.53: own NIC deduction prohibition and employer exception | https://www.legislation.gov.uk/ukpga/2005/5/section/53/data.xml | 2026-11-26 |
| HMRC employer rates: periods, thresholds, categories and Class 1A/1B rates | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 | 2026-11-26 |
| HMRC 2024/25: employer threshold, rate and allowance | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025 | 2026-11-26 |
| HMRC NIC tables: dated Classes 2, 3 and 4 | https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions | 2026-11-26 |
| HMRC self-employed rates: ordinary Class 2/4 conditions; completed SA103 proof reused | https://www.gov.uk/self-employed-national-insurance-rates | 2026-11-26 |
| HMRC directors: methods, FPS codes, leaving office | https://www.gov.uk/employee-directors | 2026-11-26 |
| HMRC Employment Allowance: amount and sole-director eligibility | https://www.gov.uk/claim-employment-allowance ; https://www.gov.uk/claim-employment-allowance/eligibility | 2026-11-26 |
| HMRC NI overview: age timing and contribution record | https://www.gov.uk/national-insurance | 2026-11-26 |
| HMRC voluntary rates/window and pension caution | https://www.gov.uk/voluntary-national-insurance-contributions/rates ; https://www.gov.uk/voluntary-national-insurance-contributions/deadlines ; https://www.gov.uk/voluntary-national-insurance-contributions | 2026-11-26 |
| HMRC FPS, PAYE, benefits and PSA deadlines | https://www.gov.uk/running-payroll/reporting-to-hmrc ; https://www.gov.uk/pay-paye-tax ; https://www.gov.uk/employer-reporting-expenses-benefits/deadlines ; https://www.gov.uk/paye-settlement-agreements/deadlines-and-payment | 2026-11-26 |
| HMRC weekly employee example | https://www.gov.uk/national-insurance-rates-letters | 2026-11-26 |
| HMRC late-payment interest; completed UK bookkeeping exact read reused, applicability confirmed 26 November | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | 2026-11-22 |

Not yet confirmed: special category/relief eligibility, complex allowance cases, Classes 1A/1B classification, credits/pension entitlement, overseas voluntary coverage, collection exceptions and penalty regimes are explicit partner-accountant referrals above, not usable instructions. No inference is made from an illustrative calculation to a real person's eligibility.
