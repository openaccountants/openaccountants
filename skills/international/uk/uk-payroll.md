---
name: uk-payroll
description: Use this skill whenever asked about UK payroll, PAYE, National Insurance contributions, employer obligations, RTI submissions, statutory payments, or payslip requirements. Trigger on phrases like "PAYE", "National Insurance", "NIC", "Class 1 NI", "employer NI", "employee NI", "RTI", "FPS", "EPS", "real time information", "P45", "P60", "P11D", "statutory sick pay", "SSP", "statutory maternity pay", "SMP", "national minimum wage", "national living wage", "payslip", "tax code", "student loan deduction", "workplace pension", "auto-enrolment", "HMRC payroll", or any question about running payroll in the United Kingdom. ALWAYS read this skill before processing any UK payroll work.
version: 1.0
jurisdiction: GB
tax_year: 2026
last_updated: 2026-09-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK employer payroll: PAYE, RTI, National Insurance, statutory pay, minimum wage and year-end (2026/27, with 2025/26 notes)

Figures are for the 2026/27 tax year, which runs from 6 April 2026 to 5 April 2027, unless a line says otherwise. HMRC's own summary is [Rates and thresholds for employers 2026 to 2027](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027). The National Minimum Wage and National Living Wage change on 1 April each year, not 6 April ([NMW rates](https://www.gov.uk/national-minimum-wage-rates)). A dated section near the end covers 2025/26, the year whose P60s, P11Ds and Class 1A are already due.

## Scope and who this is for

- **Covers:** employers running payroll for employees in England, Wales, Scotland and Northern Ireland under PAYE:
  - registering a PAYE scheme and reporting in real time (RTI): the Full Payment Submission (FPS) and the Employer Payment Summary (EPS);
  - tax codes, starter information and the 2026/27 PAYE bands, including Scotland and Wales;
  - Class 1 employee and employer National Insurance (NIC), category letters and directors;
  - the Employment Allowance;
  - the National Minimum Wage and National Living Wage;
  - Statutory Sick Pay (SSP), Statutory Maternity Pay (SMP), Statutory Paternity Pay (SPP) and recovery of statutory pay;
  - automatic enrolment thresholds and minimum contributions;
  - student loan and postgraduate loan deductions;
  - paying HMRC (monthly or quarterly), year-end (P60, P11D, P11D(b), Class 1A) and penalties;
  - the payrolling of benefits in kind that HMRC has announced from April 2027.
- **Does not cover:**
  - the employee's own Self Assessment return (see the Guide **uk-income-tax-sa100**);
  - payroll bookkeeping entries (see the Guide **uk-bookkeeping**);
  - National Insurance beyond employer payroll (see the Guide **uk-national-insurance**);
  - VAT, including any VAT effect of benefits provided to staff (see the Guide **uk-vat-return**);
  - employment status (employee or self-employed), IR35 and off-payroll working;
  - the Construction Industry Scheme, PAYE Settlement Agreements in detail, and termination payments beyond the Class 1A threshold;
  - Freeport and Investment Zone eligibility (only the category letters are shown);
  - employment law beyond the payroll minimums listed here (contracts, dismissal, family leave rights).
- **Payroll software does the arithmetic.** HMRC expects employers to use payroll software, which works out tax and NIC from the code and category letter ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)). This Guide explains what the software should be doing, so that you can check it and spot the cases where it cannot know the answer.

## Ask the client first

- Is the business registered as an employer with HMRC, and does it have its employer PAYE reference? When is the first payday? Registration must happen before the first payday and not more than 2 months before it ([register as an employer](https://www.gov.uk/register-employer)).
- Is the company's only paid worker a single director? This matters for the Employment Allowance.
- For each new starter: do they have a P45? If not, which starter checklist statement (A, B or C) did they tick? Do they have a student loan (which plan) or a postgraduate loan?
- Where does each employee live? Scottish and Welsh taxpayers have S and C tax code prefixes.
- For each employee: date of birth (under 21, State Pension age), apprentice status and age, and whether they are an armed forces veteran or work at a Freeport or Investment Zone site. These set the NIC category letter.
- Pay frequency (weekly, fortnightly, four-weekly, monthly) and the regular payday.
- Does anyone earn less than the National Minimum Wage for their age once accommodation charges are counted?
- Is anyone off sick, on maternity, paternity, adoption, shared parental, bereavement or neonatal care leave, or due to start it?
- What was total Class 1 NIC (employee and employer) in the last complete tax year? This sets the 92% or 109% recovery rate ([recover statutory pay](https://www.gov.uk/recover-statutory-payments)).
- Does the employer usually pay HMRC less than £1,500 a month? If so, it may be able to pay quarterly ([running payroll](https://www.gov.uk/running-payroll)).
- Which benefits in kind are provided (cars, vans, fuel, medical insurance, loans, accommodation)? Are any already payrolled?
- Is the business part of a group of connected companies or charities? Only one company in a group can claim the Employment Allowance.
- Has the workplace pension been set up? Are any workers aged 22 or over earning £10,000 or more a year not yet enrolled ([joining a workplace pension](https://www.gov.uk/workplace-pensions/joining-a-workplace-pension))?

## The method, step by step

1. **Register as an employer before the first payday.** You must register even if the only employee is yourself, for example as the only director of a limited company. You cannot register more than 2 months before you start paying people. If you have to pay someone before the PAYE reference arrives, run payroll, store the FPS and send it late ([register as an employer](https://www.gov.uk/register-employer)). HMRC will close the scheme of a new employer that does not send a report or pay HMRC within 120 days ([running payroll](https://www.gov.uk/running-payroll)).
2. **Decide who goes through PAYE.** You usually have to operate PAYE on employees who earn £129 or more a week (£559 a month or £6,708 a year). Once you already run a PAYE scheme, you must still record and report the pay of an employee below that level ([new employee](https://www.gov.uk/new-employee/print); [running payroll](https://www.gov.uk/running-payroll)). An employee paid only once gets code 0T on a week 1/month 1 basis, "IO" in the pay frequency field, and no P45.
3. **Set up each starter.** From the P45, take the leaving date, pay and tax to date, the tax code and the student loan status. Keep this information for the current year and the 3 following tax years. If there is no P45, or the employee left the last job before 6 April 2025 (HMRC's current page text; for 2026/27 read this as before 6 April of the current tax year), ask for the starter checklist ([new employee](https://www.gov.uk/new-employee/print)). Apply the code for the statement ticked ([starter checklist](https://assets.publishing.service.gov.uk/media/6331a05f8fa8f51d29278ebc/Starter_checklist.pdf)):
   - **Statement A** (first job since 6 April, and no Jobseeker's Allowance, Employment and Support Allowance or Incapacity Benefit since then): the current personal allowance code, 1257L, cumulative.
   - **Statement B** (had another job since 6 April but has no P45, or has received one of those benefits): 1257L on a week 1/month 1 basis.
   - **Statement C** (has another job, or receives a State, workplace or private pension): code BR.
   - Add the S or C prefix for a Scottish or Welsh taxpayer when HMRC tells you. Report the new starter on the FPS on or before the first payday ([work out the tax code](https://www.gov.uk/new-employee-tax-code)).
4. **Apply the tax code HMRC sends.** Use the latest-dated P9(T) or online coding notice. For employees with no new code, carry the 2025/26 code into 2026/27 but do **not** carry over any week 1 or month 1 marking ([P9X 2026](https://assets.publishing.service.gov.uk/media/6996e9b3b33a4db7ff889e08/P9X_2026_Tax_codes_to_use_from_6_April_2026.pdf)). Payments after a P45 has been issued use 0T (S0T, C0T) on a non-cumulative basis.
5. **Set the NIC category letter** from the employee's age, apprentice status, veteran status and workplace (see the NIC tables below). Directors use an annual earnings period (see step 10).
6. **Run each payday.** Work out gross pay, PAYE, employee NIC, employer NIC, student and postgraduate loan deductions, pension contributions and any statutory pay. Give each employee a payslip on or before payday ([payslips](https://www.gov.uk/payslips)). Send the FPS **on or before** payday ([running payroll](https://www.gov.uk/running-payroll)).
7. **Check the minimum wage** for each worker's age and apprentice status, using the rate in force for the pay reference period (see the rates below).
8. **Send an EPS by the 19th of the following tax month** if you are reclaiming statutory pay, claiming the Employment Allowance (once a tax year), reclaiming CIS deductions as a limited company, or paying the Apprenticeship Levy. Send an EPS instead of an FPS if you paid nobody in a tax month ([EPS](https://www.gov.uk/running-payroll/reporting-to-hmrc-eps)).
9. **Pay HMRC** by the 22nd of the next tax month if paying electronically, or so that a cheque arrives by the 19th. If HMRC has agreed to quarterly payment, pay by the 22nd after the quarter ends ([pay PAYE](https://www.gov.uk/pay-paye-tax)).
10. **Directors.** Work out a director's NIC on an annual earnings period, using the standard (cumulative) method or the alternative method. Under the alternative method, NIC is worked out on each period's pay and trued up on the last payment of the year. Enter "AN" or "AL" in the director's NIC method field on the FPS ([NIC for company directors](https://www.gov.uk/employee-directors)).
11. **Automatic enrolment.** Enrol eligible jobholders (aged 22 to State Pension age, earning at least £10,000 a year, ordinarily working in the UK) and pay at least the minimum contributions on qualifying earnings ([joining a workplace pension](https://www.gov.uk/workplace-pensions/joining-a-workplace-pension)).
12. **Year-end.** Send the final FPS of the year on or before the last payday. Give P60s by 31 May. Report expenses and benefits (P11D and P11D(b)) by 6 July, and pay Class 1A NIC by 22 July, or 19 July by cheque ([annual reporting](https://www.gov.uk/payroll-annual-reporting); [benefits deadlines](https://www.gov.uk/employer-reporting-expenses-benefits/deadlines)).
   - **The order matters.** An FPS sent after payday without a valid late-reporting reason can bring a penalty. A missing EPS lets HMRC estimate a "specified charge", and an EPS sent after the 19th means the reduction is not applied to that month's bill.

## Figures for 2026/27

### PAYE income tax (from 6 April 2026)

The personal allowance is £12,570 a year, which is £242 a week or £1,048 a month. The emergency codes are 1257L W1, 1257L M1 and 1257L X ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).

| Band (above the PAYE threshold), England and Northern Ireland, and Wales ([source](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)) | Rate |
| --- | --- |
| Up to £37,700 | 20% |
| £37,701 to £125,140 | 40% |
| Above £125,140 | 45% |

| Band (above the PAYE threshold), Scotland ([source](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)) | Rate |
| --- | --- |
| Starter: up to £3,967 | 19% |
| Basic: £3,968 to £16,956 | 20% |
| Intermediate: £16,957 to £31,092 | 21% |
| Higher: £31,093 to £62,430 | 42% |
| Advanced: £62,431 to £125,140 | 45% |
| Top: above £125,140 | 48% |

- **Personal allowance taper.** The allowance falls by £1 for every £2 of adjusted net income above £100,000, and is zero at £125,140 or above ([Income Tax rates](https://www.gov.uk/income-tax-rates/income-over-100000)). HMRC reflects this in the code it issues. Do not change a code yourself.
- **Tax code letters** ([what your tax code means](https://www.gov.uk/tax-codes/what-your-tax-code-means)):
  - L: standard allowance.
  - M and N: Marriage Allowance received or transferred.
  - BR, D0 and D1: all pay at the basic, higher or additional rate.
  - 0T: no allowance.
  - NT: no tax.
  - K: untaxed income exceeds the allowance, so the code adds to taxable pay.
  - S or C prefix: Scottish or Welsh rates. SD0 to SD3 are the Scottish intermediate, higher, advanced and top rates.
- **Emergency basis.** A code ending W1, M1 or X, or shown as NONCUM, is worked out on that period's pay alone, not on the cumulative basis ([emergency tax codes](https://www.gov.uk/tax-codes/emergency-tax-codes)).

### Class 1 National Insurance thresholds (2026/27)

| Threshold ([source](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)) | Weekly | Monthly | Yearly |
| --- | --- | --- | --- |
| Lower earnings limit (LEL) | £129 | £559 | £6,708 |
| Primary threshold (PT) | £242 | £1,048 | £12,570 |
| Secondary threshold (ST) | £96 | £417 | £5,000 |
| Freeport and Investment Zone upper secondary threshold | £481 | £2,083 | £25,000 |
| Upper secondary threshold (under 21), apprentice (under 25) and veterans | £967 | £4,189 | £50,270 |
| Upper earnings limit (UEL) | £967 | £4,189 | £50,270 |

- Earnings from the LEL up to the PT carry 0% employee NIC, but they protect the employee's contribution record ([source](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).

### Employee (primary) Class 1 rates (2026/27)

| Category letter ([source](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)) | LEL to PT | PT to UEL | Above UEL |
| --- | --- | --- | --- |
| A (standard), F (Freeport), H (apprentice under 25), M (under 21), N (Investment Zone), V (veteran) | 0% | 8% | 2% |
| B, E, I (married women and widows reduced rate) | 0% | 1.85% | 2% |
| J, L, D, Z (deferment) | 0% | 2% | 2% |
| C (over State Pension age), K and S (state pensioner) | nil | nil | nil |

### Employer (secondary) Class 1 rates (2026/27)

- **The employer rate is 15%** on earnings above the secondary threshold of £5,000 a year (£96 a week), with **no upper limit** ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)). The same 15% rate and £5,000 threshold have applied since 6 April 2025 ([2025/26 rates](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026)).
- **Reliefs by category letter** ([source](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)):
  - **M (under 21), H (apprentice under 25), V (veteran), Z (under 21, deferment):** 0% up to £967 a week (£50,270 a year), then 15% above ([source](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).
  - **F, I, L, S (Freeport) and N, D, E, K (Investment Zone):** 0% up to £481 a week (£25,000 a year), then 15% above ([source](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).
  - **A, B, C, J:** 15% on everything above the secondary threshold. Category C (over State Pension age) still attracts employer NIC ([source](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).
- **Directors.** The company pays employer NIC on a director's salary even when the director runs the payroll and is the only employee ([NIC for company directors](https://www.gov.uk/employee-directors)).

### Class 1A and Class 1B (2026/27)

- **Class 1A on expenses and benefits** is 15%, reported and paid after the end of the tax year ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).
- **Class 1A on termination awards** is 15% on the amount over £30,000. It is paid through payroll during the year, and only where Class 1 has not already been paid on the award ([pay Class 1A](https://www.gov.uk/pay-class-1a-national-insurance)).
- **Class 1B** on a PAYE Settlement Agreement is 15% ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).

### Employment Allowance (2026/27)

- **Amount.** Eligible employers can reduce their employer Class 1 NIC by up to £10,500 in the tax year. The reduction applies each payroll run until the £10,500 is used or the year ends. It cannot exceed the employer Class 1 liability ([Employment Allowance](https://www.gov.uk/claim-employment-allowance)).
- **Who can claim** ([eligibility](https://www.gov.uk/claim-employment-allowance/eligibility)):
  - a business or public body that does less than half its work in the public sector;
  - a charity, including a community amateur sports club;
  - someone who employs a care or support worker.
- **The £100,000 cap is gone.** From April 2025, employers with more than £100,000 of Class 1 NIC liabilities can claim ([eligibility](https://www.gov.uk/claim-employment-allowance/eligibility)).
- **Who cannot claim:**
  - a company whose only director is the only employee liable for employer Class 1 NIC;
  - for employees within the IR35 off-payroll rules;
  - for domestic staff such as a nanny or gardener (a care or support worker is the exception).
- **Groups and more than one payroll.** Only one company in a group of connected companies or charities can claim, and only against one payroll.
- **How to claim.** Claim on the EPS, once each tax year ([EPS](https://www.gov.uk/running-payroll/reporting-to-hmrc-eps)).

### National Minimum Wage and National Living Wage (from 1 April 2026)

| Category ([source](https://www.gov.uk/national-minimum-wage-rates)) | From 1 April 2026 | 1 April 2025 to 31 March 2026 |
| --- | --- | --- |
| Aged 21 and over (National Living Wage) | £12.71 | £12.21 |
| Aged 18 to 20 | £10.85 | £10 |
| Under 18 (above school leaving age) | £8 | £7.55 |
| Apprentice (under 19, or 19 or over in the first year) | £8 | £7.55 |

- **Apprentices** aged 19 or over who have completed the first year of the apprenticeship get the rate for their age. For example, a 21-year-old after the first year gets £12.71 ([NMW rates](https://www.gov.uk/national-minimum-wage-rates)).
- **Accommodation offset** from April 2026: £11.10 a day or £77.70 a week (2025: £10.66 a day or £74.62 a week). Accommodation is the only benefit in kind that counts towards minimum wage pay. A charge above the offset reduces pay for minimum wage purposes. Free accommodation adds the offset to pay ([accommodation](https://www.gov.uk/national-minimum-wage-accommodation)).
- **Overtime.** There is no statutory overtime premium. Overtime pay is set by the contract, but average pay for the pay reference period must still meet the minimum wage.

### Statutory payments (2026/27)

| Payment ([source](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)) | Weekly rate |
| --- | --- |
| SSP | £123.25 or 80% of average weekly earnings, whichever is lower |
| SMP, first 6 weeks | 90% of average weekly earnings |
| SMP, remaining 33 weeks (39 weeks in total) | £194.32 or 90% of average weekly earnings, whichever is lower |
| SPP, SAP after 6 weeks, ShPP, SPBP, SNCP | £194.32 or 90% of average weekly earnings, whichever is lower |

- **SMP rate date.** The SMP rate applies from 5 April 2026. The other rates apply from 6 April 2026 ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).

**Statutory Sick Pay from 6 April 2026** ([transition guidance](https://www.gov.uk/guidance/sickness-absences-that-start-before-and-end-on-or-after-6-april-2026)):

- **Changes from 6 April 2026:**
  - SSP is available to all eligible employees regardless of their earnings, because the lower earnings limit test has gone;
  - it is payable from the first full day of sickness absence, because the 3 waiting days have gone;
  - it is paid at 80% of average weekly earnings or £123.25, whichever is lower ([source](https://www.gov.uk/guidance/sickness-absences-that-start-before-and-end-on-or-after-6-april-2026)).
- **Qualifying.** The employee must be sick for at least one full working day. A day on which they worked a minute or more does not count. SSP is paid for up to 28 weeks, on the employee's normal qualifying days, through payroll with tax and NIC deducted ([SSP entitlement](https://www.gov.uk/employers-sick-pay/entitlement)).
- **Daily rate.** Divide the weekly rate by the number of qualifying days in the week. At the flat rate for 5 qualifying days that is £24.65 a day ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).
- **Linked periods.** Absences of at least one full working day that are 8 weeks or less apart link. A continuous series of linked periods lasting more than 3 years ends eligibility ([SSP eligibility](https://www.gov.uk/employers-sick-pay/eligibility-and-form-ssp1)).
- **Exclusions.** No SSP for an employee who:
  - has had the 28-week maximum;
  - is getting SMP or Maternity Allowance;
  - is off with a pregnancy-related illness in the 4 weeks before the expected week of birth;
  - was in custody or on strike on the first day;
  - has had Employment and Support Allowance within 12 weeks of starting or returning to work;
  - is working outside the EU where you are not liable for their NIC.
- **Form SSP1.** Give SSP1 within 7 days if an employee does not qualify, and within 7 days if SSP ends unexpectedly. Where SSP is expected to end before the sickness does, give it by the start of the 23rd week ([SSP eligibility](https://www.gov.uk/employers-sick-pay/eligibility-and-form-ssp1)).
- **Transition cases** ([transition guidance](https://www.gov.uk/guidance/sickness-absences-that-start-before-and-end-on-or-after-6-april-2026)):
  - **Previously below the LEL.** An employee who was not entitled because they earned below the LEL can become entitled from 6 April 2026 if the absence started on or after 22 September 2025. The same applies if it started before 21 September 2025 but they returned to work for periods between 22 September 2025 and 5 April 2026. They are not entitled if the absence started on or before 21 September 2025 and ran unbroken to 5 April 2026, until they have been back at work for at least 8 weeks.
  - **Waiting days.** Waiting days being served on 6 April 2026 fall away. No SSP is paid for waiting days before 6 April 2026.
  - **Already on SSP with AWE of £125 to £154.05 a week.** An employee already receiving SSP before 6 April 2026, with AWE in that range, keeps the flat rate until they return to work or SSP ends ([source](https://www.gov.uk/guidance/sickness-absences-that-start-before-and-end-on-or-after-6-april-2026)).
- **No recovery.** SSP cannot be recovered from HMRC ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).

**SMP and SPP conditions:**

- **SMP.** The employee must be on the payroll in the qualifying week (the 15th week before the expected week of childbirth) and have 26 weeks' continuous employment up to any day in that week. They must earn at least the LEL on average in the 8-week relevant period, give the correct notice, and give proof of pregnancy (usually MATB1) within 21 days of the SMP start date. You do not have to pay SMP if you have no proof of the due date 13 weeks after the SMP start date ([SMP eligibility](https://www.gov.uk/employers-maternity-pay-leave/eligibility-and-proof-of-pregnancy)).
  - **Check the earnings figure.** That page still shows "at least £125 a week", the 2025/26 LEL. The 2026/27 LEL is £129 ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)). Use the SMP calculator, which applies the correct year.
- **SPP.** SPP is 1 or 2 weeks at £194.32 or 90% of AWE, whichever is lower. The employee must be on the payroll, earn at least £129 a week (gross) in the 8-week relevant period, and have been continuously employed for at least 26 weeks up to any day in the qualifying week. They must also give the correct notice, be taking time off to look after the child or their partner, and be responsible for the child's upbringing. Paternity leave (unpaid) is available from the first day of employment ([SPP eligibility](https://www.gov.uk/employers-paternity-pay-leave/eligibility); [SPP entitlement](https://www.gov.uk/employers-paternity-pay-leave)).

**Recovering statutory pay** ([recover statutory payments](https://www.gov.uk/recover-statutory-payments)):

- **What is recoverable.** Reclaim 92% of SMP, SPP, SAP, ShPP, SPBP and SNCP ([source](https://www.gov.uk/recover-statutory-payments)).
- **Small Employers' Relief.** Reclaim 109% instead if total Class 1 NIC (employee and employer, ignoring reductions such as the Employment Allowance) was £45,000 or less in the last complete tax year before the relevant qualifying, matching or relevant week ([source](https://www.gov.uk/recover-statutory-payments)).
- **How.** Claim through the EPS. Even if you pay more than the statutory amount, you can reclaim only the percentage of the statutory amount.

### Automatic enrolment (2026/27)

| Threshold ([TPR earnings thresholds](https://www.thepensionsregulator.gov.uk/en/employers/new-employers/im-an-employer-who-has-to-provide-a-pension/declare-your-compliance/ongoing-duties-for-employers/earnings-thresholds)) | Annual | Week | 4 weeks | Month |
| --- | --- | --- | --- | --- |
| Lower level of qualifying earnings | £6,240 | £120 | £480 | £520 |
| Earnings trigger for automatic enrolment | £10,000 | £192 | £768 | £833 |
| Upper level of qualifying earnings | £50,270 | £967 | £3,867 | £4,189 |

- **2026/27 thresholds are unchanged from 2025/26** ([TPR earnings thresholds](https://www.thepensionsregulator.gov.uk/en/employers/new-employers/im-an-employer-who-has-to-provide-a-pension/declare-your-compliance/ongoing-duties-for-employers/earnings-thresholds)).
- **Who must be enrolled.** Workers aged between 22 and State Pension age, earning at least £10,000 a year and usually working in the UK ([joining a workplace pension](https://www.gov.uk/workplace-pensions/joining-a-workplace-pension)). The employer may postpone enrolment by up to 3 months, but must tell the worker in writing.
- **Minimum contributions** on qualifying earnings: employer 3%, employee 5%, total 8% ([what you pay](https://www.gov.uk/workplace-pensions/what-you-your-employer-and-the-government-pay)). The employer may pay more, and the worker can then pay less, provided the total minimum is met.
- **Qualifying earnings** include salary, bonuses, commission, overtime and statutory sick, maternity, paternity, adoption, shared parental, bereavement and neonatal care pay.
- **Workers who opt in.** For a worker earning £520 a month, £120 a week or £480 over 4 weeks, or less, who joins voluntarily, the employer does not have to contribute ([source](https://www.gov.uk/workplace-pensions/what-you-your-employer-and-the-government-pay)).

### Student loan and postgraduate loan deductions (2026/27)

| Plan ([source](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)) | Yearly threshold | Monthly | Weekly | Rate |
| --- | --- | --- | --- | --- |
| Plan 1 | £26,900 | £2,241.66 | £517.30 | 9% |
| Plan 2 | £29,385 | £2,448.75 | £565.09 | 9% |
| Plan 4 (Scotland) | £33,795 | £2,816.25 | £649.90 | 9% |
| Plan 5 | £25,000 | £2,083.33 | £480.76 | 9% |
| Postgraduate loan | £21,000 | £1,750 | £403.84 | 6% |

- **Rules for deductions** ([new employee](https://www.gov.uk/new-employee/print)):
  - Deduct only one student loan plan at a time, but a postgraduate loan can run alongside it.
  - If the employee does not know the plan, use Plan 5 until an SL1 start notice arrives.
  - If they have more than one plan and you do not know which is in repayment, use the plan with the lowest threshold.
  - Do not stop deductions because the employee asks. Stop only on an SL2 or PGL2 from HMRC.

### Apprenticeship Levy (2026/27)

- **Who pays.** Employers, together with connected companies, whose annual pay bill is more than £3 million pay the levy at 0.5% of the pay bill. An annual allowance of £15,000 reduces the levy. HMRC's page describes the allowance for employers not connected to another company or charity, so check how a connected group allocates it. The levy is paid monthly through the EPS and the PAYE bill ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027); [EPS](https://www.gov.uk/running-payroll/reporting-to-hmrc-eps)).

### Payrolling benefits in kind: announced for April 2027 (not yet in force)

This is announced policy, not yet final law. The secondary legislation that sets the detailed scope is due at Budget 2026 ([HMRC policy paper, updated 23 July 2026](https://www.gov.uk/government/publications/changes-to-reporting-of-benefits-in-kind-from-april-2027/mandatory-reporting-of-benefits-in-kind-in-real-time-information-rti-from-april-2027)).

- **Phase 1, from 6 April 2027.** Most employers providing medical benefit, company cars, vans, and car and van fuel will have to report them through payroll software. They will have to calculate Income Tax and Class 1A NIC in real time, and will no longer report these on a P11D after the year end.
- **Phase 2, from 6 April 2028.** Most remaining benefits will follow. Employer-provided loans and accommodation stay on the existing year-end route for now ([phased introduction](https://www.gov.uk/guidance/draft-guidance-and-legislation-to-aid-preparation-for-reporting-benefits-in-kind-in-real-time/the-phased-introduction-of-mandatory-payrolling-for-benefits-in-kind)).
- **Penalty easement.** The policy paper provides for penalties not to be charged for non-deliberate inaccuracies for a limited period of one year.
- **What to do now.**
  - Check that the payroll software will support the new FPS fields.
  - Decide whether to payroll other benefits voluntarily. Registration to payroll is voluntary today, and HMRC has not yet published the final phase 1 guidance ("to align with Autumn Budget 2026").
  - Recheck both pages after the Budget.

### Payslips and working-time minimums (still current)

- **Payslips.** Give a payslip on or before payday, on paper or electronically. It must show pay before and after deductions, and the amount of each variable deduction (such as tax and NIC). Where pay varies with time worked, it must show the hours worked. Fixed deductions can be explained on the payslip or in a separate written statement given before the first payslip and updated every year ([payslips](https://www.gov.uk/payslips)).
- **Holiday.** Most workers on a 5-day week are entitled to at least 28 days' paid leave a year, which is 5.6 weeks. Bank holidays can count towards it. For part-time workers it is pro rata: 3 days a week gives 16.8 days ([holiday entitlement](https://www.gov.uk/holiday-entitlement-rights)).
- **Rolled-up holiday pay.** This applies in Great Britain to irregular-hours workers and part-year workers, for leave years beginning on or after 1st April 2024 ([WTR reg 15B](https://www.legislation.gov.uk/uksi/1998/1833/regulation/15B)).
  - Holiday pay may be paid as a 12.07% uplift to the worker's pay for work done ([WTR reg 16A](https://www.legislation.gov.uk/uksi/1998/1833/regulation/16A)).
  - The uplift must be paid at the same time as that pay.
  - Any itemised payslip must show the holiday pay paid for the period ([WTR reg 16A](https://www.legislation.gov.uk/uksi/1998/1833/regulation/16A)).
  - Northern Ireland has its own regulations. Check them there.
- **Working time.** The limit is 48 hours a week on average, normally averaged over 17 weeks, unless the worker opts out in writing. Under-18s cannot work more than 8 hours a day or 40 hours a week ([maximum weekly hours](https://www.gov.uk/maximum-weekly-working-hours)).

## Boundaries and exceptions

| Situation | Rule | Source |
| --- | --- | --- |
| Employee earns under £129 a week | PAYE usually not required, but an existing scheme must still record and report their pay | [new employee](https://www.gov.uk/new-employee/print); [running payroll](https://www.gov.uk/running-payroll) |
| Earnings exactly at a threshold | Employee NIC is 8% on earnings **above** the PT up to **and including** the UEL. Employer NIC is 15% on earnings **above** the ST | [rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) |
| Employee turns 21 | Category M stops. Employer NIC of 15% then applies above £96 a week, not £967 | [rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) |
| Employee reaches State Pension age | Employee NIC stops (category C), but employer NIC of 15% continues. A director may be due a refund when the letter changes | [NIC for company directors](https://www.gov.uk/employee-directors) |
| Only employee is a sole director | No Employment Allowance, but employer NIC is still due on salary above £5,000 | [eligibility](https://www.gov.uk/claim-employment-allowance/eligibility) |
| Employer NIC above £100,000 | Employment Allowance can still be claimed (from April 2025) | [eligibility](https://www.gov.uk/claim-employment-allowance/eligibility) |
| Starter with no P45, second job | Statement B uses 1257L on a week 1/month 1 basis. Statement C uses BR | [starter checklist](https://assets.publishing.service.gov.uk/media/6331a05f8fa8f51d29278ebc/Starter_checklist.pdf) |
| Payday falls on a weekend or bank holiday | The FPS may go on the next banking day, with late reporting reason code G | [FPS after payday](https://www.gov.uk/running-payroll/fps-after-payday) |
| New starter with no P45 paid under £96 a week, or employed for under a week | The FPS may be sent within 7 days of paying | [FPS after payday](https://www.gov.uk/running-payroll/fps-after-payday) |
| No employees paid in a tax month | Send an EPS by the 19th, not an FPS. A period of inactivity of 1 to 12 months can be flagged in advance | [EPS](https://www.gov.uk/running-payroll/reporting-to-hmrc-eps) |
| Average PAYE bill under £1,500 a month | Quarterly payment possible if HMRC agrees. Pay by 22 July, 22 October, 22 January and 22 April | [running payroll](https://www.gov.uk/running-payroll); [pay PAYE](https://www.gov.uk/pay-paye-tax) |
| All of an employee's benefits payrolled | No P11D for that employee, but a P11D(b) is still needed for Class 1A | [reporting and paying](https://www.gov.uk/employer-reporting-expenses-benefits/reporting-and-paying) |
| Termination award over £30,000 | Class 1A at 15% on the excess, paid through PAYE during the year | [pay Class 1A](https://www.gov.uk/pay-class-1a-national-insurance) |
| SSP absence started before 6 April 2026 | Follow HMRC's transition rules (see above) | [transition guidance](https://www.gov.uk/guidance/sickness-absences-that-start-before-and-end-on-or-after-6-april-2026) |

## Worked cases

These are straight-line checks of what the software should produce. Real software applies HMRC's tables and rounding rules, so pennies can differ.

**Case 1: monthly employee in England, 2026/27.** Salary £3,500 a month, tax code 1257L (cumulative), category A, Plan 2 student loan, auto-enrolled on qualifying earnings. Thresholds are from [rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) and [TPR earnings thresholds](https://www.thepensionsregulator.gov.uk/en/employers/new-employers/im-an-employer-who-has-to-provide-a-pension/declare-your-compliance/ongoing-duties-for-employers/earnings-thresholds).

- PAYE: annual pay £42,000, less £12,570 = £29,430, all within the £37,700 basic rate band. At 20% that is £5,886 a year, or £490.50 a month ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).
- Employee NIC: (£3,500 − £1,048) × 8% = £196.16 ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).
- Employer NIC: (£3,500 − £417) × 15% = £462.45 ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).
- Plan 2 loan: (£3,500 − £2,448.75) × 9% = £94.61 before the software's rounding ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).
- Pension on qualifying earnings above £520 a month (the band ends at £4,189): employee 5% of £2,980 = £149.00; employer 3% = £89.40 ([what you pay](https://www.gov.uk/workplace-pensions/what-you-your-employer-and-the-government-pay)).

**Case 2: Employment Allowance.** A trading company has 4 employees, each paid £30,000 a year, category A. Employer NIC per employee is (£30,000 − £5,000) × 15% = £3,750, so £15,000 in total. The company claims the Employment Allowance on its EPS. The first £10,500 is offset, leaving £4,500 of employer NIC for the year ([Employment Allowance](https://www.gov.uk/claim-employment-allowance); [rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).

- **Variation 1:** if the only employee were a sole director, no allowance could be claimed ([eligibility](https://www.gov.uk/claim-employment-allowance/eligibility)).
- **Variation 2:** if one of the four were 19 years old (category M), no employer NIC would be due on that employee's £30,000, because it is below £50,270. Total employer NIC would be £11,250. The allowance would leave £750 to pay ([source](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).

**Case 3: SSP from day one.** An employee works 5 qualifying days a week with average weekly earnings of £140, and is off sick for 3 qualifying days in June 2026. 80% of £140 is £112, which is lower than £123.25, so the weekly rate is £112. The daily rate is £112 ÷ 5 = £22.40. SSP for the 3 days is £67.20, paid from the first day ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027); [transition guidance](https://www.gov.uk/guidance/sickness-absences-that-start-before-and-end-on-or-after-6-april-2026)). Under the rules before 6 April 2026, 3 waiting days meant nothing was paid for a 3-day absence. None of this SSP is recoverable.

**Case 4: recovering SMP.** An employer pays £2,000 of SMP in a tax month ([source](https://www.gov.uk/recover-statutory-payments)).

- Its Class 1 NIC in the last complete tax year before the qualifying week was more than £45,000, so it reclaims 92%, which is £1,840 ([source](https://www.gov.uk/recover-statutory-payments)).
- If that NIC was £45,000 or less, it reclaims 109%, which is £2,180 ([source](https://www.gov.uk/recover-statutory-payments)).
- Claim on the EPS by the 19th of the following tax month ([recover statutory payments](https://www.gov.uk/recover-statutory-payments); [EPS](https://www.gov.uk/running-payroll/reporting-to-hmrc-eps)).

**Case 5: benefits and Class 1A for 2026/27.** A company car benefit of £6,000 is not payrolled ([source](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).

- File a P11D for the employee and a P11D(b) by 6 July 2027.
- Pay Class 1A of £6,000 × 15% = £900 by 22 July 2027 (19 July by cheque) ([benefits deadlines](https://www.gov.uk/employer-reporting-expenses-benefits/deadlines); [rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).
- For 2027/28, cars fall within phase 1 of mandatory payrolling as announced (see above).

**Case 6: late FPS.** An employer with 12 employees sends an FPS late in a month without a valid reason. It is not the first failure of the tax year, and the payments were not within 3 days of payday. The penalty for 10 to 49 employees is £200 for that month. Paying within 30 days of the notice avoids interest ([late filing penalties](https://www.gov.uk/guidance/what-happens-if-you-dont-report-payroll-information-on-time)).

## When to refuse or refer

- **Employment status.** Refer if the question is whether a worker is an employee, self-employed, or inside IR35. Getting it wrong brings extra tax, NIC, interest and a penalty ([new employee](https://www.gov.uk/new-employee/print)).
- **Foreign and cross-border cases.** Refer employees seconded from abroad, UK employees working overseas, and cases where the employer pays foreign tax for the employee. These need specialist treatment of PAYE and NIC.
- **Freeport and Investment Zone relief.** Refer the question of whether the site and employee conditions are met. This Guide shows only the rates.
- **Complex non-cash pay.** Refer share options, and PAYE Settlement Agreements beyond the basic Class 1B rate. HMRC tells employers to contact it for complex situations such as exercising share options ([FPS after payday](https://www.gov.uk/running-payroll/fps-after-payday)).
- **Unsettled benefits payrolling detail.** Do not state the final phase 1 rules for April 2027 as settled law until the secondary legislation at Budget 2026 and HMRC's final guidance are published.
- **Old or contested SSP and SMP disputes, and employee appeals.** An employee who disputes an SSP decision can appeal to HMRC. Refer rather than decide.
- **Penalty appeals and time-to-pay arrangements.** Refer where the amounts are significant or the reasonable-excuse grounds are arguable.
- **Refuse** to advise paying below the National Minimum Wage, or deducting pension or loan amounts the employee has not been told about.

## Filing and payment

| What | When | Source |
| --- | --- | --- |
| Register as an employer | Before the first payday, and no more than 2 months before it | [register as an employer](https://www.gov.uk/register-employer) |
| FPS | On or before each payday | [running payroll](https://www.gov.uk/running-payroll) |
| EPS (reclaims, Employment Allowance, levy, nil month) | By the 19th of the following tax month (tax months start on the 6th) | [EPS](https://www.gov.uk/running-payroll/reporting-to-hmrc-eps) |
| Pay PAYE and NIC monthly | By the 22nd of the next tax month electronically; the 19th if by cheque through the post | [pay PAYE](https://www.gov.uk/pay-paye-tax) |
| Pay quarterly (average under £1,500 a month, agreed with HMRC) | By the 22nd after the quarter ends, for example 22 July for 6 April to 5 July | [pay PAYE](https://www.gov.uk/pay-paye-tax); [running payroll](https://www.gov.uk/running-payroll) |
| Final FPS of the year | On or before the last payday | [annual reporting](https://www.gov.uk/payroll-annual-reporting) |
| P60 to employees | By 31 May | [annual reporting](https://www.gov.uk/payroll-annual-reporting) |
| P11D, P11D(b) and copies to employees | By 6 July | [benefits deadlines](https://www.gov.uk/employer-reporting-expenses-benefits/deadlines) |
| Class 1A payment | By 22 July (19 July by cheque) | [benefits deadlines](https://www.gov.uk/employer-reporting-expenses-benefits/deadlines) |
| PAYE Settlement Agreement tax and Class 1B | By 22 October (19 October by cheque) | [benefits deadlines](https://www.gov.uk/employer-reporting-expenses-benefits/deadlines) |

- **P11D and P11D(b) filing.** Employers with fewer than 500 employees file through PAYE Online. Employers with more than 500 must use payroll software. Paper is accepted only from employers who have stopped trading ([reporting and paying](https://www.gov.uk/employer-reporting-expenses-benefits/reporting-and-paying)).
- **Corrections.** Correct a P11D(b) by showing the **total** Class 1A due, not the difference.
- **Records.** Keep starter information for the current year and the 3 following tax years ([new employee](https://www.gov.uk/new-employee/print)).

### Penalties

- **Late or missing FPS or EPS** ([late filing penalties](https://www.gov.uk/guidance/what-happens-if-you-dont-report-payroll-information-on-time)). The penalty is monthly and set by the number of employees:
  - 1 to 9 employees: £100 ([source](https://www.gov.uk/guidance/what-happens-if-you-dont-report-payroll-information-on-time));
  - 10 to 49: £200 ([source](https://www.gov.uk/guidance/what-happens-if-you-dont-report-payroll-information-on-time));
  - 50 to 249: £300 ([source](https://www.gov.uk/guidance/what-happens-if-you-dont-report-payroll-information-on-time));
  - 250 or more: £400 ([source](https://www.gov.uk/guidance/what-happens-if-you-dont-report-payroll-information-on-time)).
- **When there is no penalty:**
  - all payments on the late FPS were within 3 days of payday (regular late filers may still be penalised);
  - a new employer sent its first FPS within 30 days of paying an employee;
  - it is the first failure in the tax year (this does not apply to annual schemes).
- **Specified charges.** HMRC may raise an estimated specified charge where no FPS or EPS arrives. Only sending the missing return replaces it.
- **Paying the penalty.** HMRC issues notices quarterly. Pay within 30 days of the notice to avoid interest. Appeal through PAYE for Employers ("Appeal a penalty").
- **Late payment of monthly or quarterly PAYE** ([late payment penalties](https://www.gov.uk/guidance/what-happens-if-you-dont-pay-paye-and-national-insurance-on-time)). The first late payment in a tax year is not a default. After that, the penalty is set by the number of defaults in the year:
  - 1 to 3 defaults: 1% ([source](https://www.gov.uk/guidance/what-happens-if-you-dont-pay-paye-and-national-insurance-on-time));
  - 4 to 6: 2% ([source](https://www.gov.uk/guidance/what-happens-if-you-dont-pay-paye-and-national-insurance-on-time));
  - 7 to 9: 3% ([source](https://www.gov.uk/guidance/what-happens-if-you-dont-pay-paye-and-national-insurance-on-time));
  - 10 or more: 4% ([source](https://www.gov.uk/guidance/what-happens-if-you-dont-pay-paye-and-national-insurance-on-time)).
- **Payments still unpaid later.** A further 5% applies if a payment is still unpaid after 6 months, and another 5% after 12 months. These apply even if only one payment in the year is late. Interest runs daily ([source](https://www.gov.uk/guidance/what-happens-if-you-dont-pay-paye-and-national-insurance-on-time)).
- **Class 1A, Class 1B and HMRC determinations.** A 5% penalty applies if the amount is not paid within 30 days of the due date. Further 5% penalties apply at 6 and 12 months ([source](https://www.gov.uk/guidance/what-happens-if-you-dont-pay-paye-and-national-insurance-on-time)).
- **Late P11D(b).** The penalty is £100 per 50 employees for each month or part month late ([benefits deadlines](https://www.gov.uk/employer-reporting-expenses-benefits/deadlines)).
- **Inaccurate returns.** Careless or deliberate errors bring inaccuracy penalties. There is no penalty where reasonable care was taken ([late filing penalties](https://www.gov.uk/guidance/what-happens-if-you-dont-report-payroll-information-on-time)).

## 2025/26: the year just ended (dated section)

The 2025/26 tax year ran from 6 April 2025 to 5 April 2026 ([2025/26 rates](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026)). Its year-end deadlines have passed: P60 by 31 May 2026, P11D and P11D(b) by 6 July 2026, and Class 1A by 22 July 2026. Late items now attract the penalties above. Use these figures when correcting 2025/26 through an Earlier Year Update, or checking arrears:

| 2025/26 item ([source](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026)) | Figure |
| --- | --- |
| LEL | £125 a week, £542 a month, £6,500 a year |
| PT, ST, UEL | Same as 2026/27 (£242, £96, £967 a week) |
| Employer NIC rate and Class 1A | 15% |
| Employment Allowance | £10,500 |
| SMP and SPP flat rate | £187.18 or 90% of AWE if lower |
| SSP weekly rate | £118.75 (with 3 waiting days and the LEL test) |
| Small Employers' Relief recovery | 108.5% (92% otherwise) |
| Student loan thresholds, Plans 1, 2 and 4 | £26,065; £28,470; £32,745 (postgraduate £21,000) |

- **Minimum wage.** From 1 April 2025 to 31 March 2026 the rates were £12.21 (21 and over), £10 (18 to 20) and £7.55 (under 18 and apprentices) ([NMW rates](https://www.gov.uk/national-minimum-wage-rates)).

## Completion checklist

- [ ] PAYE scheme registered before the first payday. The employer PAYE reference is on file ([register as an employer](https://www.gov.uk/register-employer)).
- [ ] Each starter has a P45 or a starter checklist, the correct statement code (A, B or C), and a loan plan recorded.
- [ ] Tax codes updated from the P9X and any P9(T) notices, with no week 1/month 1 markings carried into 2026/27.
- [ ] Category letters checked for under-21s, apprentices under 25, veterans, Freeport and Investment Zone staff, and people over State Pension age.
- [ ] Directors flagged with AN or AL on the FPS.
- [ ] Every FPS sent on or before payday. Every EPS sent by the 19th. Payment made by the 22nd (the 19th by cheque).
- [ ] Employment Allowance eligibility checked and claimed once on the EPS.
- [ ] Minimum wage met for each worker's age band from 1 April 2026.
- [ ] SSP paid from the first full day of sickness, with SSP1 issued where needed. SMP and SPP conditions and evidence are on file. Reclaims made at 92% or 109% ([source](https://www.gov.uk/recover-statutory-payments)).
- [ ] Automatic enrolment done for eligible jobholders, with contributions at least 3% employer and 8% total on qualifying earnings ([source](https://www.gov.uk/workplace-pensions/what-you-your-employer-and-the-government-pay)).
- [ ] P60s issued by 31 May. P11D and P11D(b) filed by 6 July. Class 1A paid by 22 July.
- [ ] Payroll software checked for the April 2027 payrolling of cars, vans, fuel and medical benefit. HMRC's final guidance to be rechecked after Budget 2026.

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
