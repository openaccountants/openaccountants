---
name: uk-payroll
description: "UK employer payroll for the 2026/27 tax year (6 April 2026 to 5 April 2027), with dated 2025/26 notes. Covers registering a PAYE scheme, tax codes and starter checklists, PAYE bands for England, Northern Ireland, Wales and Scotland, Class 1 NIC as payroll applies it, the Employment Allowance, student and postgraduate loan deductions, National Minimum Wage and National Living Wage from 1 April 2026, Statutory Sick Pay after the April 2026 reform, SMP and SPP and their recovery, automatic enrolment thresholds, the Apprenticeship Levy, benefits in kind and mandatory payrolling from April 2027, RTI (FPS and EPS), paying HMRC by the 22nd, year-end and penalties. Trigger on 'PAYE', 'RTI', 'FPS', 'EPS', 'tax code', 'P45', 'P60', 'P11D', 'SSP', 'SMP', 'minimum wage', 'auto-enrolment', 'payroll UK'. Out of scope: NIC detail (uk-national-insurance), the employee's own return (uk-income-tax-sa100), Scottish status (uk-scottish-income-tax), bookkeeping (uk-bookkeeping)."
version: 1.2
jurisdiction: GB
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK employer payroll: PAYE, RTI, statutory pay, minimum wage and year-end (2026/27, with 2025/26 notes)

Figures are for the 2026/27 tax year, 6 April 2026 to 5 April 2027, unless a line says otherwise. The minimum wage changes on 1 April each year, not 6 April. HMRC expects employers to use payroll software, which does the arithmetic from the tax code and NIC category letter. This skill says what the software should be doing, so you can check it and spot the cases it cannot know.

## Who this applies to

- **Covers** employers running PAYE for employees in England, Wales, Scotland and Northern Ireland. The legal base is the PAYE regulations made under ITEPA 2003 s 684 (the Income Tax (Pay As You Earn) Regulations 2003, SI 2003/2682).
- **Register before the first payday**, and not more than 2 months before it. This applies even if the only employee is you, for example as sole director of a company. If you must pay someone before the PAYE reference arrives, run payroll, keep the FPS and send it late. HMRC closes a new scheme that sends no report and makes no payment within 120 days.
- **Who goes through PAYE.** You must operate PAYE on employees who earn at least the lower earnings limit, £129 a week (£559 a month, £6,708 a year). Once a scheme exists you must still record and report the pay of an employee below that level. An employee paid only once gets code 0T on a week 1/month 1 basis, "IO" in the pay frequency field, and no P45.
- **Out of scope here:**
  - National Insurance rules beyond what payroll applies: see **uk-national-insurance** (category letters, directors, Class 1A and 1B detail, reliefs);
  - the employee's own Self Assessment: **uk-income-tax-sa100**; Scottish taxpayer status: **uk-scottish-income-tax**;
  - student loans repaid through Self Assessment: **uk-student-loan-repayment**;
  - payroll journals: **uk-bookkeeping**; VAT on staff benefits: **uk-vat-return**;
  - employment status, IR35 and off-payroll working, the Construction Industry Scheme, PAYE Settlement Agreements in detail, share schemes, termination payments beyond the Class 1A threshold, Freeport and Investment Zone eligibility (only the category letters are named), and employment law beyond the payslip and working-time minimums below.
- **Refer, do not decide:** whether a worker is employed or self-employed or inside IR35; employees seconded from abroad, UK employees working overseas, and tax-equalised staff; Freeport and Investment Zone site conditions; share options and complex non-cash pay (HMRC tells employers to contact it); SSP or SMP disputes and employee appeals to HMRC; penalty appeals and time to pay where the sums or the excuse are significant. **Refuse** to help pay below the minimum wage or to make deductions the employee has not been told about.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Personal allowance (code 1257L) | £12,570 a year, £1,048 a month, £242 a week | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Emergency codes | 1257L W1, 1257L M1, 1257L X | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| PAYE, England, NI and Wales | 20% to £37,700; 40% £37,701 to £125,140; 45% above | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| PAYE, Scotland (bands above the allowance) | 19% to £3,967; 20% to £16,956; 21% to £31,092; 42% to £62,430; 45% to £125,140; 48% above | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Allowance taper | £1 lost per £2 of adjusted net income above £100,000; nil at £125,140. HMRC puts it in the code; do not change a code yourself | 2026/27 | https://www.gov.uk/income-tax-rates/income-over-100000 |
| NIC lower earnings limit | £129 a week, £559 a month, £6,708 a year | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| NIC primary threshold / UEL | £242 / £967 a week (£1,048 / £4,189 a month; £12,570 / £50,270 a year) | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| NIC secondary threshold | £96 a week, £417 a month, £5,000 a year | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Employee Class 1 (category A) | 8% PT to UEL, 2% above | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Employer Class 1 | 15% above the ST, no upper limit; 0% to £50,270 for under-21s (M, Z), apprentices under 25 (H) and veterans (V); 0% to £25,000 at Freeport and Investment Zone sites | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Class 1A (benefits; termination awards over £30,000) and Class 1B (PSA) | 15% | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Employment Allowance | Up to £10,500 off employer Class 1 | 2026/27 | https://www.gov.uk/claim-employment-allowance |
| National Living Wage (21 and over) | £12.71 an hour | from 1 April 2026 | https://www.legislation.gov.uk/uksi/2026/357/made |
| NMW 18 to 20 | £10.85 an hour | from 1 April 2026 | https://www.legislation.gov.uk/uksi/2026/357/made |
| NMW under 18, and apprentice rate | £8.00 an hour | from 1 April 2026 | https://www.legislation.gov.uk/uksi/2026/357/made |
| Accommodation offset | £11.10 a day (£77.70 a week) | from 1 April 2026 | https://www.legislation.gov.uk/uksi/2026/357/made |
| SSP | £123.25 a week or 80% of average weekly earnings, whichever is lower; from day one; no LEL test | from 6 April 2026 | https://www.gov.uk/guidance/sickness-absences-that-start-before-and-end-on-or-after-6-april-2026 |
| SMP | 90% of AWE for 6 weeks, then £194.32 or 90% of AWE if lower for 33 weeks | from 5 April 2026 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| SPP, SAP after 6 weeks, ShPP, SPBP, SNCP | £194.32 or 90% of AWE if lower | from 6 April 2026 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Statutory pay recovery | 92%; 109% with Small Employers' Relief (Class 1 NIC £45,000 or less in the last complete tax year); SSP not recoverable | 2026/27 | https://www.gov.uk/recover-statutory-payments |
| Student loan thresholds (9%) | Plan 1 £26,900; Plan 2 £29,385; Plan 4 £33,795; Plan 5 £25,000 a year | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Student loan monthly thresholds | Plan 1 £2,241.66; Plan 2 £2,448.75; Plan 4 £2,816.25; Plan 5 £2,083.33; PGL £1,750 | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Postgraduate loan | 6% above £21,000 | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Auto-enrolment trigger | £10,000 a year (£833 a month, £192 a week, £768 per 4 weeks) | 2026/27 | https://www.thepensionsregulator.gov.uk/en/employers/new-employers/im-an-employer-who-has-to-provide-a-pension/declare-your-compliance/ongoing-duties-for-employers/earnings-thresholds |
| Qualifying earnings band | £6,240 to £50,270 a year (£520 to £4,189 a month; £120 to £967 a week; £480 to £3,867 per 4 weeks) | 2026/27 | https://www.thepensionsregulator.gov.uk/en/employers/new-employers/im-an-employer-who-has-to-provide-a-pension/declare-your-compliance/ongoing-duties-for-employers/earnings-thresholds |
| Minimum pension contributions | Employer 3%, total 8% of qualifying earnings | 2026/27 | https://www.gov.uk/workplace-pensions/what-you-your-employer-and-the-government-pay |
| Apprenticeship Levy | 0.5% of pay bill over £3 million, less a £15,000 allowance | 2026/27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Quarterly payment limit | Average monthly payment under £1,500 | 2026/27 | https://www.gov.uk/running-payroll |

## The taxable base

**Tax codes.**
- Apply the latest P9(T) or online coding notice. For employees with no new code, carry the 2025/26 code into 2026/27 but drop any week 1 or month 1 marking ([P9X 2026](https://assets.publishing.service.gov.uk/media/6996e9b3b33a4db7ff889e08/P9X_2026_Tax_codes_to_use_from_6_April_2026.pdf)). Pay after a P45 has been issued uses 0T (S0T, C0T) non-cumulative.
- Letters: L standard allowance; M and N Marriage Allowance received or transferred; BR, D0 and D1 all pay at basic, higher or additional rate; 0T no allowance; NT no tax; K untaxed income exceeds the allowance, so the code adds to taxable pay. S or C prefix means Scottish or Welsh rates; SD0 to SD3 are the Scottish intermediate, higher, advanced and top rates. W1, M1, X or NONCUM means non-cumulative ([what your tax code means](https://www.gov.uk/tax-codes/what-your-tax-code-means); [emergency codes](https://www.gov.uk/tax-codes/emergency-tax-codes)).

**Starters.** From the P45 take the leaving date, pay and tax to date, the code and the student loan status. Keep starter information for the current year and the 3 following tax years. With no P45, use the starter checklist ([new employee](https://www.gov.uk/new-employee/print); [starter checklist](https://assets.publishing.service.gov.uk/media/6331a05f8fa8f51d29278ebc/Starter_checklist.pdf)):
- Statement A (first job since 6 April, no JSA, ESA or Incapacity Benefit since then): 1257L cumulative.
- Statement B (another job since 6 April but no P45, or one of those benefits): 1257L week 1/month 1.
- Statement C (another job or a pension): BR.
- Add the S or C prefix when HMRC says so. Report the starter on the FPS on or before the first payday.

**National Insurance.** Employee NIC is 8% on earnings above the PT up to and including the UEL; employer NIC is 15% on earnings above the ST. Earnings from the LEL to the PT carry 0% but protect the contribution record. Category C (over State Pension age) stops employee NIC, but employer NIC continues. When a worker turns 21, category M stops and employer NIC starts above £96 a week. Directors use an annual earnings period (AN or AL on the FPS), and the company pays employer NIC on a director's salary even when the director is the only employee. All of this, including the married women's reduced rate, deferment letters and the Freeport and Investment Zone letters, is set out in **uk-national-insurance**; this skill does not repeat it.

**Employment Allowance.** Up to £10,500 a year, set against employer Class 1 each run until used. It cannot exceed the liability. The £100,000 cap went in April 2025. It is claimed once a year on the EPS. No claim for: a company whose only director is the only employee paid above the ST; workers inside the off-payroll rules; domestic staff other than care or support workers. Only one company in a connected group, and one payroll, can claim. A body doing more than half its work in the public sector cannot claim; charities and community amateur sports clubs can ([eligibility](https://www.gov.uk/claim-employment-allowance/eligibility)).

**Student and postgraduate loans.** Deduct 9% above the plan threshold (6% for the postgraduate loan). Only one plan at a time, but a postgraduate loan runs alongside it. Unknown plan: use Plan 5 until an SL1 arrives. More than one plan and unsure which: use the lowest threshold. Stop only on an SL2 or PGL2 from HMRC, never because the employee asks ([new employee](https://www.gov.uk/new-employee/print)). Self Assessment repayments are in **uk-student-loan-repayment**.

**Minimum wage.** The rates are set by the National Minimum Wage Regulations 2015 as amended by the National Minimum Wage (Amendment) Regulations 2026 (SI 2026/357), from 1 April 2026. Apprentices aged 19 or over who have finished the first year get the rate for their age. Accommodation is the only benefit that counts towards minimum wage pay: free accommodation adds the offset to pay; a charge above the offset reduces pay ([accommodation](https://www.gov.uk/national-minimum-wage-accommodation)). There is no statutory overtime premium, but average pay for the pay reference period must meet the minimum.

**Statutory Sick Pay from 6 April 2026** ([transition guidance](https://www.gov.uk/guidance/sickness-absences-that-start-before-and-end-on-or-after-6-april-2026)):
- No lower earnings limit test and no waiting days. SSP is the lower of £123.25 a week and 80% of AWE, paid from the first full day of sickness for up to 28 weeks on qualifying days, through payroll with tax and NIC. A day on which the employee worked a minute or more does not count.
- Daily rate is the weekly rate divided by qualifying days in the week (£24.65 at the flat rate over 5 days).
- Absences of at least one full working day 8 weeks or less apart link. A run of linked periods over 3 years ends eligibility ([SSP eligibility](https://www.gov.uk/employers-sick-pay/eligibility-and-form-ssp1)).
- No SSP for an employee who has had 28 weeks, gets SMP or Maternity Allowance, has a pregnancy-related illness in the 4 weeks before the expected week of birth, was in custody or on strike on the first day, had ESA within 12 weeks of starting or returning, or works outside the EU where you are not liable for their NIC.
- Form SSP1 within 7 days if the employee does not qualify or SSP ends unexpectedly; by the start of the 23rd week if SSP will end before the sickness does.
- Transition: an employee below the old LEL can become entitled from 6 April 2026 if the absence began on or after 22 September 2025, or began before 21 September 2025 with returns to work between 22 September 2025 and 5 April 2026. An unbroken absence from on or before 21 September 2025 to 5 April 2026 gives no entitlement until 8 weeks back at work. Waiting days being served on 6 April 2026 fall away, and none before that date are paid. Someone already on SSP with AWE of £125 to £154.05 keeps the flat rate until they return or SSP ends.

**SMP and SPP.**
- SMP: on payroll in the qualifying week (15th week before the expected week of childbirth), 26 weeks' continuous employment up to any day in that week, average earnings at least the LEL in the 8-week relevant period, correct notice, and proof of pregnancy (usually MATB1) within 21 days of the SMP start. No SMP is due without proof of the due date 13 weeks after the start ([SMP eligibility](https://www.gov.uk/employers-maternity-pay-leave/eligibility-and-proof-of-pregnancy)). That page still shows £125, the 2025/26 LEL; for 2026/27 the LEL is £129.
- SPP: 1 or 2 weeks at the SPP rate. On payroll, at least £129 a week gross in the relevant period, 26 weeks' continuous employment to the qualifying week, correct notice, responsible for the child. Unpaid paternity leave is a day-one right ([SPP eligibility](https://www.gov.uk/employers-paternity-pay-leave/eligibility)).
- Recovery is on the EPS at 92% or 109% of the statutory amount only, even if you pay more. Small Employers' Relief looks at Class 1 NIC (employee and employer, before the Employment Allowance) in the last complete tax year before the qualifying week. On £2,000 of SMP that is £1,840 at 92% or £2,180 at 109%.

**Automatic enrolment.** Enrol workers aged 22 to State Pension age, earning at least £10,000 and usually working in the UK. Postponement up to 3 months is allowed with written notice. Contributions are on qualifying earnings, which include salary, bonus, commission, overtime and statutory pay. The employer can pay more and the worker less, as long as the 8% total is met. A worker earning at or below the lower level who opts in gets no compulsory employer contribution ([joining](https://www.gov.uk/workplace-pensions/joining-a-workplace-pension)). The 2026/27 thresholds are unchanged from 2025/26.

**Apprenticeship Levy.** Employers, with connected companies, whose pay bill is over £3 million pay 0.5%, less the £15,000 allowance, monthly through the EPS and the PAYE bill. HMRC's page describes the allowance for unconnected employers, so check how a group allocates it.

**Benefits in kind.** Benefits not payrolled go on a P11D, with Class 1A at 15% on the P11D(b). An employee whose benefits are all payrolled needs no P11D, but the P11D(b) is still due ([reporting and paying](https://www.gov.uk/employer-reporting-expenses-benefits/reporting-and-paying)). Example: a £6,000 car benefit not payrolled for 2026/27 means a P11D and P11D(b) by 6 July 2027 and £900 Class 1A by 22 July 2027. Payrolling is voluntary in 2026/27.

**Mandatory payrolling of benefits (announced, not yet final law).** From 6 April 2027 most employers providing medical benefit, cars, vans and car and van fuel must report them in payroll and calculate Income Tax and Class 1A in real time, with no P11D for them. From 6 April 2028 most other benefits follow; loans and accommodation stay on the year-end route for now. A one-year easement on penalties for non-deliberate inaccuracies is planned. The detailed regulations were due at Budget 2026 ([policy paper, updated 23 July 2026](https://www.gov.uk/government/publications/changes-to-reporting-of-benefits-in-kind-from-april-2027/mandatory-reporting-of-benefits-in-kind-in-real-time-information-rti-from-april-2027); [phased introduction](https://www.gov.uk/guidance/draft-guidance-and-legislation-to-aid-preparation-for-reporting-benefits-in-kind-in-real-time/the-phased-introduction-of-mandatory-payrolling-for-benefits-in-kind)). Check the software supports the new FPS fields.

**Payslips and working time.**
- Payslip on or before payday, paper or electronic, showing pay before and after deductions, each variable deduction, and hours where pay varies with time. Fixed deductions can be in a separate annual statement ([payslips](https://www.gov.uk/payslips)).
- Holiday: at least 5.6 weeks (28 days on a 5-day week), bank holidays can count, pro rata for part-time (3 days a week gives 16.8 days) ([holiday entitlement](https://www.gov.uk/holiday-entitlement-rights)).
- Rolled-up holiday pay in Great Britain for irregular-hours and part-year workers, leave years from 1 April 2024: a 12.07% uplift paid with the pay for work done and shown on the payslip ([WTR reg 15B](https://www.legislation.gov.uk/uksi/1998/1833/regulation/15B); [reg 16A](https://www.legislation.gov.uk/uksi/1998/1833/regulation/16A)). Northern Ireland has its own regulations.
- Working time: 48 hours a week on average, normally over 17 weeks, unless the worker opts out in writing. Under-18s: 8 hours a day, 40 a week ([maximum weekly hours](https://www.gov.uk/maximum-weekly-working-hours)).

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Register as employer | Before first payday, not more than 2 months before | https://www.gov.uk/register-employer |
| FPS | On or before each payment (PAYE Regs 2003 reg 67B) | https://www.legislation.gov.uk/uksi/2003/2682/regulation/67B |
| EPS (reclaims, Employment Allowance, levy, CIS reclaim by a company, nil month) | By the 19th of the following tax month | https://www.gov.uk/running-payroll/reporting-to-hmrc-eps |
| Pay PAYE and NIC monthly | Within 17 days after the tax month ends (the 22nd) electronically; 14 days (the 19th) otherwise (reg 69) | https://www.legislation.gov.uk/uksi/2003/2682/regulation/69 |
| Pay quarterly (agreed with HMRC) | 22 July, 22 October, 22 January, 22 April | https://www.gov.uk/pay-paye-tax |
| Final FPS of the year | On or before the last payday | https://www.gov.uk/payroll-annual-reporting |
| P60 | By 31 May | https://www.gov.uk/payroll-annual-reporting |
| P11D, P11D(b) and employee copies | By 6 July | https://www.gov.uk/employer-reporting-expenses-benefits/deadlines |
| Class 1A | By 22 July (19 July by cheque) | https://www.gov.uk/employer-reporting-expenses-benefits/deadlines |
| PSA tax and Class 1B | By 22 October (19 October by cheque) | https://www.gov.uk/employer-reporting-expenses-benefits/deadlines |

- Tax months run from the 6th to the 5th.
- A payday on a weekend or bank holiday: the FPS may go on the next banking day with late reporting reason G. A starter with no P45 paid under £96 a week, or employed under a week: FPS within 7 days of paying ([FPS after payday](https://www.gov.uk/running-payroll/fps-after-payday)).
- No one paid in a tax month: send an EPS by the 19th instead of an FPS. Inactivity of 1 to 12 months can be flagged in advance.
- A missing EPS lets HMRC estimate a specified charge; an EPS after the 19th means the reduction is not applied to that month's bill.
- P11D filing: fewer than 500 employees through PAYE Online; 500 or more through software; paper only from employers who stopped trading. Correct a P11D(b) by showing the total Class 1A due, not the difference.
- 2025/26 year-end: P60s by 31 May 2026, P11D and P11D(b) by 6 July 2026, Class 1A by 22 July 2026 have passed. Correct 2025/26 through an Earlier Year Update using the 2025/26 figures: LEL £125 a week (£542 a month, £6,500 a year); PT, ST and UEL as 2026/27; employer and Class 1A rate 15%; Employment Allowance £10,500; SMP and SPP flat rate £187.18; SSP £118.75 with 3 waiting days and the LEL test; Small Employers' Relief 108.5%; student loan thresholds Plan 1 £26,065, Plan 2 £28,470, Plan 4 £32,745, postgraduate £21,000; minimum wage from 1 April 2025 £12.21, £10.00 and £7.55 ([2025/26 rates](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026); SI 2026/357).

## Penalties and interest

- **Late or missing FPS or EPS** (Finance Act 2009 Sch 55; [late filing](https://www.gov.uk/guidance/what-happens-if-you-dont-report-payroll-information-on-time)): monthly, by employee count: 1 to 9 £100; 10 to 49 £200; 50 to 249 £300; 250 or more £400. No penalty if all payments on the late FPS were within 3 days of payday (regular late filers excepted), for a new employer whose first FPS is within 30 days of paying, or for the first failure in the tax year (not for annual schemes). Notices are quarterly; pay within 30 days to avoid interest. A specified charge is replaced only by sending the missing return, not by later year-to-date figures.
- **Late PAYE payment** (Finance Act 2009 Sch 56; [late payment](https://www.gov.uk/guidance/what-happens-if-you-dont-pay-paye-and-national-insurance-on-time)): the first late payment in a year is not a default. Then 1% for 1 to 3 defaults, 2% for 4 to 6, 3% for 7 to 9, 4% for 10 or more, on the amount late. A further 5% if still unpaid after 6 months and 5% more after 12 months, even for a single late payment. Interest runs daily.
- **Class 1A, Class 1B and HMRC determinations**: 5% if unpaid 30 days after the due date, and further 5% at 6 and 12 months.
- **Late P11D(b)**: £100 per 50 employees for each month or part month.
- **Inaccurate returns**: careless or deliberate errors bring inaccuracy penalties; none where reasonable care was taken.
- **Minimum wage arrears**: underpaid workers must be paid back; HMRC enforces. The penalty figures are not restated here (see Not yet confirmed).

## Cross-border points

- PAYE applies to employees working in the UK, including those of a non-UK employer with a UK presence. Seconded inbound staff, UK staff working abroad and tax-equalised employees need specialist treatment of PAYE and NIC: refer.
- NIC for workers moving in or out of the UK (certificates of coverage, the EU and treaty rules) is in **uk-national-insurance**; residence is in **uk-statutory-residence-test**.
- SSP is not payable to an employee working outside the EU where the employer is not liable for their NIC.
- Auto-enrolment applies to workers who usually work in the UK.

## Worked examples

**Example 1: monthly employee in England.** Salary £3,500 a month, code 1257L cumulative, category A, Plan 2 student loan, auto-enrolled on qualifying earnings. Annual pay £42,000 less £12,570 gives £29,430, all in the 20% band, so PAYE is £490.50 a month. Employee NIC is (3,500 minus 1,048) at 8% = £196.16. Employer NIC is (3,500 minus 417) at 15% = £462.45. The Plan 2 deduction is (3,500 minus 2,448.75) at 9% = £94.61 before the software's rounding. Pension is on £2,980 (3,500 minus 520): employee 5% £149.00, employer 3% £89.40. These are straight-line checks; real software uses HMRC tables, so pennies can differ.

```oa-check
name: Monthly employee, England, 2026/27, Plan 2, auto-enrolled
inputs:
  monthly_pay: 3500
steps:
  - annual_taxable: monthly_pay * 12 - 12570
  - paye_month: annual_taxable * 0.20 / 12
  - ee_nic: (monthly_pay - 1048) * 0.08
  - er_nic: (monthly_pay - 417) * 0.15
  - plan2: round((monthly_pay - 2448.75) * 0.09, 2)
  - qualifying: min(monthly_pay, 4189) - 520
  - pension_ee: qualifying * 0.05
  - pension_er: qualifying * 0.03
expected:
  paye_month: 490.50
  ee_nic: 196.16
  er_nic: 462.45
  plan2: 94.61
  pension_ee: 149.00
  pension_er: 89.40
```

**Example 2: Employment Allowance with an under-21.** A trading company has 4 employees each on £30,000 a year. If all are category A, employer NIC is (30,000 minus 5,000) at 15% = £3,750 each, £15,000 in total, and the Employment Allowance leaves £4,500. Here one employee is 19 (category M), so no employer NIC is due on that pay, which is below £50,270. Employer NIC is £11,250 and the allowance leaves £750. If the only employee were a sole director, no allowance could be claimed.

```oa-check
name: Employment Allowance, 4 staff on 30,000, one aged 19
inputs:
  salary: 30000
  staff_a: 3
steps:
  - per_head: (salary - 5000) * 0.15
  - all_a_net: per_head * 4 - 10500
  - er_total: per_head * staff_a
  - net_after_ea: max(er_total - 10500, 0)
expected:
  per_head: 3750.00
  all_a_net: 4500.00
  er_total: 11250.00
  net_after_ea: 750.00
```

## Ask the client first

- Is the employer registered with HMRC, and when is the first payday?
- For each employee: P45 or starter checklist statement, student or postgraduate loan plan, where they live (Scotland or Wales), date of birth, apprentice or veteran status, and pay frequency.
- Is the only paid worker a single director, and is the company in a connected group? This decides the Employment Allowance.
- What was total Class 1 NIC in the last complete tax year? This sets 92% or 109% recovery. Is the monthly PAYE bill under £1,500?
- Is anyone off sick or on family leave, or due to be?
- Which benefits in kind are provided, and are any payrolled? Is the pension scheme in place for every eligible worker?

## Sources

| Source | URL | Read on |
|---|---|---|
| ITEPA 2003 s 684 (PAYE regulations) | https://www.legislation.gov.uk/ukpga/2003/1/section/684 | 2026-10-26 |
| Income Tax (PAYE) Regulations 2003, reg 67B | https://www.legislation.gov.uk/uksi/2003/2682/regulation/67B | 2026-10-26 |
| Income Tax (PAYE) Regulations 2003, reg 69 | https://www.legislation.gov.uk/uksi/2003/2682/regulation/69 | 2026-10-26 |
| National Minimum Wage (Amendment) Regulations 2026, SI 2026/357 | https://www.legislation.gov.uk/uksi/2026/357/made | 2026-10-26 |
| Finance Act 2009 Sch 55 and Sch 56 | https://www.legislation.gov.uk/ukpga/2009/10/schedule/55 | 2026-10-24 |
| Working Time Regulations 1998 regs 15B, 16A | https://www.legislation.gov.uk/uksi/1998/1833/regulation/16A | 2026-10-24 |
| HMRC, rates and thresholds for employers 2026 to 2027 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 | 2026-10-24 |
| HMRC, rates and thresholds for employers 2025 to 2026 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026 | 2026-10-24 |
| HMRC, SSP absences around 6 April 2026 | https://www.gov.uk/guidance/sickness-absences-that-start-before-and-end-on-or-after-6-april-2026 | 2026-10-24 |
| HMRC, late payroll reports | https://www.gov.uk/guidance/what-happens-if-you-dont-report-payroll-information-on-time | 2026-10-24 |
| HMRC, late PAYE payments | https://www.gov.uk/guidance/what-happens-if-you-dont-pay-paye-and-national-insurance-on-time | 2026-10-24 |
| HMRC, pay PAYE | https://www.gov.uk/pay-paye-tax | 2026-10-24 |
| HMRC, running payroll and EPS | https://www.gov.uk/running-payroll/reporting-to-hmrc-eps | 2026-10-24 |
| HMRC, expenses and benefits deadlines | https://www.gov.uk/employer-reporting-expenses-benefits/deadlines | 2026-10-24 |
| HMRC, Employment Allowance | https://www.gov.uk/claim-employment-allowance/eligibility | 2026-10-24 |
| HMRC, recover statutory payments | https://www.gov.uk/recover-statutory-payments | 2026-10-24 |
| HMRC, mandatory payrolling of benefits from April 2027 | https://www.gov.uk/government/publications/changes-to-reporting-of-benefits-in-kind-from-april-2027/mandatory-reporting-of-benefits-in-kind-in-real-time-information-rti-from-april-2027 | 2026-10-24 |
| The Pensions Regulator, earnings thresholds | https://www.thepensionsregulator.gov.uk/en/employers/new-employers/im-an-employer-who-has-to-provide-a-pension/declare-your-compliance/ongoing-duties-for-employers/earnings-thresholds | 2026-10-24 |
| gov.uk, workplace pension contributions | https://www.gov.uk/workplace-pensions/what-you-your-employer-and-the-government-pay | 2026-10-24 |

Not yet confirmed: the final regulations and HMRC guidance for mandatory payrolling of benefits from 6 April 2027 (due at Budget 2026); the legislation.gov.uk text of the April 2026 SSP reform (figures here are from HMRC guidance); minimum wage underpayment penalty figures; how the £15,000 Apprenticeship Levy allowance is shared in a connected group; the legislation text of the 2026/27 student loan thresholds (HMRC rates page used).

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
