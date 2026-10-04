---
name: uk-national-insurance
description: Use this skill whenever asked about UK National Insurance Contributions (NIC) for self-employed individuals or employers. Trigger on phrases like "how much NIC do I pay", "Class 2 contributions", "Class 4 NIC", "Class 1 employer NIC", "Employer NIC 15%", "Secondary Threshold £5,000", "Employment Allowance £10,500", "April 2026 NIC", "Class 2 abolished", "national insurance self-employed", "NIC calculation", "state pension qualifying years", "NIC deferment", "voluntary Class 2", "HMRC NIC payment", or any question about UK NIC obligations. Also trigger when classifying bank statement transactions showing HMRC NIC debits, Self Assessment NIC payments, or Class 2 direct debits. This skill covers Class 1 (employee and employer), Class 2 (voluntary post-April 2024), Class 4 (profit-based), thresholds, payment schedule, bank statement pattern classification, Employment Allowance, interaction with employment Class 1, deferment, state pension entitlement, and edge cases across three tax years (2024-25, 2025-26, 2026-27). ALWAYS read this skill before touching any UK NIC-related work.
version: 3.0
jurisdiction: GB
tax_year: 2026
last_updated: 2026-09-26
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK National Insurance contributions: Classes 1, 1A, 1B, 2, 3 and 4 (2026/27, with 2025/26 notes)

Figures are for the 2026/27 tax year, which runs from 6 April 2026 to 5 April 2027, unless a line says otherwise. HMRC's own summaries are [Rates and thresholds for employers 2026 to 2027](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) and [Rates and allowances: National Insurance contributions](https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions). A dated section near the end covers 2025/26, the year whose Self Assessment returns and voluntary Class 2 payments are due by 31 January 2027.

## Scope and who this is for

Use this Guide to work out, explain or check UK National Insurance contributions (NIC) for:

- employees and employers (Class 1), including thresholds, category letters and company directors;
- employers' Class 1A (benefits and termination awards) and Class 1B (PAYE Settlement Agreements);
- the self-employed: Class 2, which is no longer compulsory, and Class 4 on profits;
- voluntary contributions (Class 2 and Class 3) to fill gaps in a National Insurance record, and the deadlines;
- the Employment Allowance;
- National Insurance credits, and how contributions build qualifying years for the State Pension.

It does not cover:

- the full payroll process (PAYE income tax, RTI, statutory pay): see the UK payroll Guide;
- people working across borders, certificates of coverage and social security agreements (refer: see "When to refuse or refer");
- mariners, share fishermen, volunteer development workers, Freeport and Investment Zone relief claims (refer);
- the Apprenticeship Levy and income tax on Self Assessment, except where they sit next to NIC on the same bill.

## Ask the client first

- **Which tax year?** Employer NIC changed on 6 April 2025: 13.8% above £9,100 in 2024/25, then 15% above £5,000 from 2025/26. The Class 2 voluntary rate, the Small Profits Threshold, the LEL and the Class 3 rate change most years. ([rates and allowances](https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions))
- **Employed, self-employed, both, or an employer?** Each is a different class. An employee with self-employed income can owe Class 1 and Class 4 in the same year.
- **Date of birth and State Pension age.** Employee Class 1 stops at State Pension age. Class 4 stops only from the next 6 April after it.
- **For an employee: pay per pay period, pay frequency and category letter.** Class 1 works per pay period, not on annual pay (except for directors).
- **Is the worker a company director?** Directors use an annual earnings period.
- **For an employer:** is it a company whose sole director is its only employee liable for employer Class 1? Is it part of a group of connected companies or charities? Does it do half or more of its work in the public sector? These decide the Employment Allowance.
- **Any benefits in kind, termination payments over £30,000, or a PAYE Settlement Agreement?** These bring Class 1A or Class 1B. ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027))
- **For the self-employed: net profit for the tax year** from all trades together, and whether the person is an examiner, landlord, minister of religion or investor (special Class 2 and Class 4 rules).
- **Is there a gap in the National Insurance record?** Get the online record or State Pension forecast before recommending voluntary contributions, and check first whether credits are available.
- **Has the person lived or worked outside the UK, or do they have more than one job?** Both change the answer (refer, or consider deferment).

## The method, step by step

1. **Fix the tax year and the person's status** (employee, director, employer, self-employed, not working). Use the rates for that year only.
2. **Employee Class 1 (primary).** For each pay period, apply the employee's category letter to earnings in each band. With letter A: nothing up to the Primary Threshold (PT), 8% from the PT to the Upper Earnings Limit (UEL), and 2% above the UEL. Earnings from the Lower Earnings Limit (LEL) up to the PT are charged at 0% but still count towards the contribution record ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).
3. **Employer Class 1 (secondary).** Charge 15% on earnings above the Secondary Threshold (ST) of £5,000 a year (£96 a week, £417 a month). Letters for under-21s, apprentices under 25, veterans, Freeports and Investment Zones give a 0% rate up to a higher threshold (see the tables below). ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027))
4. **Directors.** Work out a director's Class 1 on an annual earnings period, using the standard method or the alternative method (see "Directors").
5. **Employment Allowance.** If the employer is eligible, set up to £10,500 a year against employer Class 1 only, until it is used up or the year ends. ([Employment Allowance](https://www.gov.uk/claim-employment-allowance))
6. **Class 1A and 1B.** Add 15% Class 1A on taxable benefits (paid after the year end) and on termination awards over £30,000 (paid through payroll). Add 15% Class 1B on the items and tax in a PAYE Settlement Agreement. ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027))
7. **Self-employed Class 4.** Take the taxable trading profit for the tax year, adding all trades together. Charge 6% on profit over £12,570 up to £50,270, and 2% above £50,270 ([self-employed rates](https://www.gov.uk/self-employed-national-insurance-rates)). It is collected through Self Assessment with income tax.
8. **Self-employed Class 2.** If profit is £7,105 or more, Class 2 is treated as paid and nothing is due. If profit is below £7,105, nothing is due, but the person may choose to pay voluntary Class 2 at £3.65 a week to protect their record. ([self-employed rates](https://www.gov.uk/self-employed-national-insurance-rates))
9. **Gaps and voluntary contributions.** Check the record, then credits. Then choose Class 2 (if the person was self-employed in that period and eligible) or Class 3 (£18.40 a week), and check the 6-year deadline. ([voluntary rates](https://www.gov.uk/voluntary-national-insurance-contributions/rates))
10. **Check the special cases** in the boundary table, then record the result and the sources used.

## Figures for 2026/27

### Class 1 thresholds (6 April 2026 to 5 April 2027)

| Threshold ([source](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)) | Weekly | Monthly | Yearly |
| --- | --- | --- | --- |
| Lower earnings limit (LEL) | £129 | £559 | £6,708 |
| Primary threshold (PT), employee NIC starts | £242 | £1,048 | £12,570 |
| Secondary threshold (ST), employer NIC starts | £96 | £417 | £5,000 |
| Freeport and Investment Zone upper secondary threshold | £481 | £2,083 | £25,000 |
| Upper secondary threshold (under 21), apprentice (under 25) and veterans upper secondary thresholds | £967 | £4,189 | £50,270 |
| Upper earnings limit (UEL) | £967 | £4,189 | £50,270 |

- The ST of £5,000 a year is the same as in 2025/26. The PT and UEL are unchanged. The LEL went up from £125 a week in 2025/26 to £129 a week ([rates and allowances](https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions)).
- An employee earning from £129 to £242 a week from one job does not usually pay NIC but may still qualify for benefits and the State Pension. An employee earning less than £129 a week from one job can choose to pay voluntary Class 3 contributions to cover gaps in their National Insurance record ([NI classes](https://www.gov.uk/national-insurance/national-insurance-classes)).
- HMRC states the thresholds "from one job", so each employment is tested on its own pay. Where earnings from different jobs might have to be added together (for example, jobs with the same or associated employers), refer.

### Employee (primary) Class 1 rates by category letter (2026/27)

| Letter ([source](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)) | LEL up to and including PT | Above PT up to and including UEL | Above UEL |
| --- | --- | --- | --- |
| A, F, H, M, N, V | 0% | 8% | 2% |
| B, E, I (married women and widows reduced rate) | 0% | 1.85% | 2% |
| D, J, L, Z (deferment) | 0% | 2% | 2% |
| C, K, S (over State Pension age) | nil | nil | nil |

HMRC's own example for letter A: on £1,000 in a week, the employee pays nothing on the first £242, 8% (£58) on earnings from £242.01 to £967, and 2% (£0.66) on the rest, so £58.66 for the week ([NI rates and categories](https://www.gov.uk/national-insurance-rates-letters)).

### Employer (secondary) Class 1 rates by category letter (2026/27)

| Letter ([source](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)) | Above ST up to LEL | LEL up to Freeport/Investment Zone upper threshold | From there up to UEL, or to the under-21, apprentice or veterans upper threshold | Above UEL, or above those upper thresholds |
| --- | --- | --- | --- | --- |
| A, B, C, J | 15% | 15% | 15% | 15% |
| D, E, F, I, K, L, N, S (Freeport and Investment Zone special tax sites) | 0% | 0% | 15% | 15% |
| H (apprentice under 25), M (under 21), V (veteran), Z (under 21, deferment) | 0% | 0% | 0% | 15% |

- **In practice:** for letters M, H, V and Z, the employer pays 0% on earnings up to £50,270 a year (£967 a week) and 15% above. For the Freeport and Investment Zone letters, the 0% band runs up to £25,000 a year (£481 a week). ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027))
- **Over State Pension age (letter C):** the employee pays no Class 1, but the employer still pays 15% above the ST. ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027))

### Category letters (who gets which)

From HMRC's list ([category letters](https://www.gov.uk/national-insurance-rates-letters/category-letters)):

- **A**: all employees apart from those in groups B, C, H, J, M, V and Z.
- **B**: married women and widows with a certificate of election for the reduced rate.
- **C**: employees over State Pension age.
- **H**: apprentices under 25.
- **J**: employees who can defer NIC because they already pay it in another job.
- **M**: employees under 21.
- **V**: employees in their first job since leaving the armed forces (veterans).
- **Z**: employees under 21 who can defer NIC because they already pay it in another job.
- **F, I, L, S**: eligible employees working in a special tax site within a Freeport (F generally; I reduced-rate married women and widows; L deferment; S over State Pension age).
- **N, E, D, K**: the same four groups in a special tax site within an Investment Zone.
- **X**: employees who do not have to pay NIC, for example because they are under 16.

Employees who work in a Freeport or Investment Zone but not within a special tax site do not use the Freeport or Investment Zone letters.

### Directors

- Directors are employees for NIC. They pay NIC on annual pay from salary and bonuses over £12,570, worked out on annual earnings rather than on each pay period. Dividends are not earnings for NIC ([NIC for company directors](https://www.gov.uk/employee-directors)).
- **Standard annual earnings period method** (common for directors paid irregularly): at each payment, work out NIC on total pay for the tax year so far, including bonuses, and take off the employee NIC already paid.
- **Alternative method** (common for directors paid regularly): work out NIC on each period's pay, then at the year end recalculate on the annual basis and deduct any shortfall from the last payment.
- Put "AN" (standard) or "AL" (alternative) in the director's NIC calculation method field on the FPS, and fill in the week of appointment.
- The company pays employer NIC on a director's salary even if the director runs the payroll and is the only employee.
- If a director leaves but stays on as an employee, use the annual basis for the whole of that tax year, and switch to per-period rules from the next tax year.
- A director may be due a refund if their category letter changes during the year, for example on reaching State Pension age.

### Class 1A and Class 1B (employers only, 2026/27)

- **Class 1A on expenses and benefits:** 15%. It is reported on form P11D(b) and paid after the end of the tax year ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)). This applies even where benefits are payrolled: a P11D(b) is still needed ([reporting and paying](https://www.gov.uk/employer-reporting-expenses-benefits/reporting-and-paying)).
- **Class 1A on termination awards:** 15% on the part of a termination award over £30,000, and on sporting testimonial payments by independent committees over £100,000. It is paid through payroll during the year ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)). It is due only where Class 1 has not already been paid on the award ([pay Class 1A](https://www.gov.uk/pay-class-1a-national-insurance)).
- **Class 1B:** 15% for 2026/27, paid by an employer that has a PAYE Settlement Agreement (PSA). A PSA is one annual payment covering the tax and NIC on minor, irregular or impracticable expenses and benefits ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)). Items in the PSA do not go on P11Ds and do not carry Class 1A: Class 1B is paid instead ([PSA overview](https://www.gov.uk/paye-settlement-agreements)).
- Employees never pay Class 1A or 1B ([NI classes](https://www.gov.uk/national-insurance/national-insurance-classes)).

### Employment Allowance (2026/27)

- **Amount:** up to £10,500 a tax year, set against the employer's Class 1 NIC only. It reduces employer NIC each payroll run until the £10,500 is used or the year ends. An employer with a lower liability can still claim, but gets no refund of the difference ([Employment Allowance](https://www.gov.uk/claim-employment-allowance); [when to claim](https://www.gov.uk/claim-employment-allowance/when-to-claim)).
- **Who can claim:** businesses and public bodies that do less than half their work in the public sector, charities (including community amateur sports clubs), and people who employ a care or support worker ([eligibility](https://www.gov.uk/claim-employment-allowance/eligibility)).
- **No £100,000 cap:** from April 2025, employers with more than £100,000 of Class 1 liabilities can claim. The old test that prior-year employer NIC had to be under £100,000 no longer applies. ([eligibility](https://www.gov.uk/claim-employment-allowance/eligibility))
- **Exclusions:**
  - a company whose only director is also the only employee liable for employer Class 1 NIC;
  - employees within the IR35 off-payroll working rules;
  - people employed for personal, household or domestic work (such as a nanny or gardener), unless they are a care or support worker.
- **Groups and payrolls:** in a group of connected companies or charities, only one can claim. An employer with more than one payroll can claim against one payroll only.
- **Timing:** claim each tax year. The claim is made on an EPS, once each tax year ([EPS](https://www.gov.uk/running-payroll/reporting-to-hmrc-eps)). A late claim can be set against other tax owed, or refunded after the year end. Claims can go back 4 tax years, to 2021/22 ([when to claim](https://www.gov.uk/claim-employment-allowance/when-to-claim)).

### Self-employed: Class 2 and Class 4 (2026/27)

| Item ([source](https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions)) | 2026/27 | 2025/26 |
| --- | --- | --- |
| Small Profits Threshold (SPT), per year | £7,105 | £6,845 |
| Voluntary Class 2 rate, per week | £3.65 | £3.50 |
| Class 4 Lower Profits Limit (LPL) | £12,570 | £12,570 |
| Class 4 Upper Profits Limit (UPL) | £50,270 | £50,270 |
| Class 4 main rate (LPL to UPL) | 6% | 6% |
| Class 4 additional rate (above UPL) | 2% | 2% |
| Special Class 2 rate, share fishermen, per week | £4.30 | £4.15 |
| Special Class 2 rate, volunteer development workers, per week | £6.45 | £6.25 |

**Class 2: no longer a compulsory charge.**

- The compulsory Class 2 charge was removed with effect from 6 April 2024: subsection 11(2) of the Social Security Contributions and Benefits Act 1992 was omitted by the National Insurance Contributions (Reduction in Rates) Act 2023. Section 11 now sets the SPT at £7,105. A person with profits of, or exceeding, that threshold is treated as having actually paid Class 2 for each week of self-employment, for benefit purposes. Someone with lower profits may pay £3.65 a week ([SSCBA 1992 s.11](https://www.legislation.gov.uk/ukpga/1992/4/section/11)). No Class 2 is paid or treated as paid for weeks after the week the person reaches pensionable age.
- In plain terms: if profits are £7,105 or more, Class 2 is treated as paid, which protects the NI record at no cost. ([self-employed rates](https://www.gov.uk/self-employed-national-insurance-rates))
- If profits are less than £7,105, nothing is due, but the person can choose to pay voluntary Class 2 at £3.65 a week ([self-employed rates](https://www.gov.uk/self-employed-national-insurance-rates)).
- Note the wording: the SPT test is "£7,105 or more", while Class 4 starts only on profits "more than £12,570". ([self-employed rates](https://www.gov.uk/self-employed-national-insurance-rates))
- Some self-employed people never have Class 2 treated as paid, but may pay voluntarily: examiners, moderators, invigilators and people who set exam questions; landlords who are eligible to pay Class 2; ministers of religion without a salary or stipend; and people who make investments for themselves or others, not as a business and without a fee or commission ([voluntary NI](https://www.gov.uk/voluntary-national-insurance-contributions)).
- Voluntary Class 2 is usually paid through the Self Assessment return. A person who does not file Self Assessment registers with HMRC, which sends a payment request between September and the end of October each year ([pay voluntary Class 2](https://www.gov.uk/pay-class-2-national-insurance)).

**Class 4.**

- Class 4 is due on profits of the tax year, computed as for income tax, from all trades, professions or vocations carried on in the UK. The statutory rates and limits are in section 15 of the Social Security Contributions and Benefits Act 1992: 6% between £12,570 and £50,270 and 2% above ([SSCBA 1992 s.15](https://www.legislation.gov.uk/ukpga/1992/4/section/15)).
- Formula: Class 4 = 6% x (lower of profit and £50,270, minus £12,570, if positive) + 2% x (profit minus £50,270, if positive). Profits of £12,570 or less give no Class 4. ([SSCBA 1992 s.15](https://www.legislation.gov.uk/ukpga/1992/4/section/15))
- **Not a trading expense.** In working out a trade's profits, no deduction is allowed for NIC paid by any person under Part 1 of the SSCBA 1992, so the trader's own Class 2 and Class 4 are not deductible. The ban does not apply to an employer's contributions (secondary Class 1, Class 1A and Class 1B), which are deductible ([ITTOIA 2005 s.53](https://www.legislation.gov.uk/ukpga/2005/5/section/53)).
- Class 4 is paid through Self Assessment, together with income tax, including in payments on account ([payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account)).
- Examiners, moderators, invigilators and people who set exam questions cannot pay Class 4 through Self Assessment. They pay "Special Class 4" by arrangement with the National Insurance office ([self-employed rates](https://www.gov.uk/self-employed-national-insurance-rates)).
- Class 4 stops from 6 April (the start of the tax year) after the person reaches State Pension age ([NI introduction](https://www.gov.uk/national-insurance)).

### Voluntary contributions: Class 2 and Class 3 (2026/27)

- **Rates for 2026/27:** Class 2 is £3.65 a week and Class 3 is £18.40 a week ([voluntary rates](https://www.gov.uk/voluntary-national-insurance-contributions/rates)). Over 52 weeks that is £189.80 for Class 2 and £956.80 for Class 3.
- **Which class:**
  - Class 2 is for periods of self-employment: profits under the SPT, or the special jobs listed above.
  - Class 3 is for everyone else with a gap, for example people who were not working, earned below the LEL, or were not eligible for credits ([NI classes](https://www.gov.uk/national-insurance/national-insurance-classes)).
- **Class 3 by Direct Debit, 2026/27:** HMRC collects £73.60 in 4-week months and £92.00 in 5-week months ([rates and allowances](https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions)).
- **Which year's rate applies:**
  - Class 2 for the previous tax year and Class 3 for the previous 2 tax years are paid at the original rate for those years.
  - For any earlier year, the rate for 2026/27 applies ([voluntary rates](https://www.gov.uk/voluntary-national-insurance-contributions/rates)).
- **Deadline:** voluntary contributions can be paid only for the past 6 years. The deadline for each year is 5 April. For example, gaps in 2025/26 can be filled until 5 April 2032 ([deadlines](https://www.gov.uk/voluntary-national-insurance-contributions/deadlines)).
- **Who cannot pay:**
  - people with no gaps, unless they get Class 3 credits and are eligible to pay Class 2;
  - married women and widows paying the reduced rate;
  - anyone past the deadline for the period with the gap ([voluntary NI](https://www.gov.uk/voluntary-national-insurance-contributions)).
- **Check before paying.** Voluntary contributions do not always increase the State Pension, for example for people who were contracted out. Below State Pension age, check the State Pension forecast or contact the Future Pension Centre first. At or over State Pension age, contact the Pension Service.
- **Abroad:**
  - A person living abroad with a certificate of coverage may pay voluntary Class 2 if their self-employed profits are below £7,105. ([Class 2 abroad](https://www.gov.uk/pay-class-2-national-insurance/if-you-work-or-live-abroad))
  - Without a certificate of coverage, Class 2 cannot be paid for time abroad from 6 April 2026 onwards, though earlier periods abroad can still be paid for ([Class 2 abroad](https://www.gov.uk/pay-class-2-national-insurance/if-you-work-or-live-abroad)).
  - Refer all cases involving time abroad.

### National Insurance credits

Credits fill gaps without payment. Check them before recommending voluntary contributions ([NI credits](https://www.gov.uk/national-insurance-credits); [eligibility](https://www.gov.uk/national-insurance-credits/eligibility)).

- **Class 1 credits** count towards the State Pension and some other benefits. **Class 3 credits** count towards the State Pension only.
- **Automatic Class 1 credits:**
  - Jobseeker's Allowance (if not in education or working 16 hours or more a week);
  - Employment and Support Allowance;
  - Maternity Allowance;
  - Carer's Allowance, or Carer Support Payment in Scotland.
- **Class 1 credits on application**, by writing to HMRC, where earnings are too low for a qualifying year while on:
  - Statutory Sick Pay; or
  - Statutory Maternity, Adoption, Shared Parental, Neonatal Care or Parental Bereavement Pay.
- **Automatic Class 3 credits:**
  - Universal Credit;
  - being registered for Child Benefit for a child under 12, even if the Child Benefit is not received.
- **Class 3 credits on application:**
  - foster carers and kinship carers in Scotland;
  - people caring for one or more sick or disabled people for at least 20 hours a week who are not on Carer's Allowance;
  - grandparents and other eligible family members caring for a child under 12 (Specified Adult Childcare credits).
- Married women paying the reduced rate cannot usually get credits.

### State Pension and qualifying years

- The full rate of the new State Pension is £241.30 a week. It usually needs 35 qualifying years for someone whose record started after April 2016 ([what you'll get](https://www.gov.uk/new-state-pension/what-youll-get)).
- A person usually needs at least 10 qualifying years to get any State Pension ([voluntary NI](https://www.gov.uk/voluntary-national-insurance-contributions)).
- People who were contracted out before 2016 usually need more than 35 years for the full rate.

## Boundaries and exceptions

| Situation | Treatment | Source |
| --- | --- | --- |
| Self-employed profit exactly £7,105 | Class 2 treated as paid (the test is "£7,105 or more") | [self-employed rates](https://www.gov.uk/self-employed-national-insurance-rates) |
| Self-employed profit exactly £12,570 | No Class 4 (it is due only on profits "more than £12,570") | [self-employed rates](https://www.gov.uk/self-employed-national-insurance-rates) |
| Profit between £7,105 and £12,570 | Nothing to pay; Class 2 treated as paid, so the year still counts | [NI classes](https://www.gov.uk/national-insurance/national-insurance-classes) |
| Loss or profit below £7,105 | Nothing due; voluntary Class 2 is optional | [self-employed rates](https://www.gov.uk/self-employed-national-insurance-rates) |
| Employee reaches State Pension age | Employee Class 1 stops (letter C); employer still pays 15% above the ST | [NI introduction](https://www.gov.uk/national-insurance); [rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) |
| Self-employed person reaches State Pension age | Class 4 continues for the rest of that tax year and stops from the next 6 April | [NI introduction](https://www.gov.uk/national-insurance) |
| Employee under 21 (M) or apprentice under 25 (H) | Employee pays as letter A; employer pays 0% up to £50,270 a year | [rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) |
| Veteran in first civilian job (V) | Employer pays 0% up to £50,270 a year | [category letters](https://www.gov.uk/national-insurance-rates-letters/category-letters) |
| Married woman or widow with a reduced-rate certificate (B) | 1.85% from PT to UEL, 2% above; cannot pay voluntary contributions or usually get credits | [rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027); [NI credits eligibility](https://www.gov.uk/national-insurance-credits/eligibility) |
| Employed and self-employed in the same year | Class 1 through payroll and Class 4 through Self Assessment; HMRC works out the combined amount after the return | [how much you pay](https://www.gov.uk/national-insurance/how-much-you-pay) |
| Two or more jobs (deferment) | May defer: with 2 jobs, needs £967 or more a week from one job and £242 or more a week in the second; with more than 2 jobs, £1,209 or more a week from 2 of them and £242 or more in the others. Deferred jobs pay 2% between £242 and £967 a week. Apply on form CA72A; for 2026/27 HMRC must receive it by 14 February 2027 | [defer NI](https://www.gov.uk/defer-national-insurance) |
| Self-employed person asks to defer Class 4 | HMRC's deferment page says the self-employed cannot defer Class 4 but may claim a refund for past years. HMRC's rates table still lists an "Additional Class 4 rate when deferring" of 2%, so the two HMRC pages differ; refer | [defer NI](https://www.gov.uk/defer-national-insurance); [rates and allowances](https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions) |
| Company whose only employee is its sole director | Employer NIC still due on salary above £5,000; no Employment Allowance | [directors](https://www.gov.uk/employee-directors); [EA eligibility](https://www.gov.uk/claim-employment-allowance/eligibility) |
| Termination award | First £30,000 free of Class 1A; 15% Class 1A on the excess through payroll, unless Class 1 already applied | [pay Class 1A](https://www.gov.uk/pay-class-1a-national-insurance) |
| Examiner, moderator, invigilator | Class 2 never treated as paid; Class 4 is paid as Special Class 4, not through Self Assessment | [self-employed rates](https://www.gov.uk/self-employed-national-insurance-rates) |
| Minister of religion with no salary or stipend | No NIC to pay; may pay voluntary contributions | [self-employed rates](https://www.gov.uk/self-employed-national-insurance-rates) |

## Worked cases

### Rates used in the cases ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027); [self-employed rates](https://www.gov.uk/self-employed-national-insurance-rates); [voluntary rates](https://www.gov.uk/voluntary-national-insurance-contributions/rates); [Employment Allowance](https://www.gov.uk/claim-employment-allowance))

All cases use 2026/27 rates, category letter A unless stated, and pay spread evenly across the year so annual figures match the sum of the pay periods.

**Case 1: employee on £35,000.**
- Employee NIC: £35,000 minus £12,570 = £22,430. At 8%, that is £1,794.40.
- Employer NIC: £35,000 minus £5,000 = £30,000. At 15%, that is £4,500.00.

**Case 2: employee on £60,000.**
- Employee NIC, main band: £50,270 minus £12,570 = £37,700. At 8%, that is £3,016.00.
- Employee NIC, above the UEL: £60,000 minus £50,270 = £9,730. At 2%, that is £194.60.
- Total employee NIC: £3,210.60.
- Employer NIC: £60,000 minus £5,000 = £55,000. At 15%, that is £8,250.00.

**Case 3: sole trader, profit £30,000.**
- Class 4: £30,000 minus £12,570 = £17,430. At 6%, that is £1,045.80.
- Class 2 is treated as paid because profit is £7,105 or more, so nothing is paid for Class 2 and the year still counts.

**Case 4: sole trader, profit £80,000.**
- Class 4 main band: £37,700 at 6% = £2,262.00.
- Class 4 above the UPL: £80,000 minus £50,270 = £29,730. At 2%, that is £594.60.
- Total Class 4: £2,856.60.

**Case 5: sole trader, profit £6,000, wants the year to count.**
- No Class 4, and Class 2 is not treated as paid because £6,000 is below £7,105.
- Voluntary Class 2 for 52 weeks: £3.65 x 52 = £189.80, usually paid through the 2026/27 Self Assessment return.
- The alternative, Class 3, would cost £18.40 x 52 = £956.80. Check credits first, for example from Universal Credit or Child Benefit for a child under 12.

**Case 6: employer with 4 employees, each on £30,000, claiming the Employment Allowance.**
- Employer NIC per employee: £30,000 minus £5,000 = £25,000. At 15%, that is £3,750.00.
- For 4 employees: £15,000.00.
- Less the Employment Allowance of £10,500: £4,500.00 payable.
- If one of the 4 is under 21 (letter M), that employee's employer NIC is 0%. The other 3 cost £11,250.00, which leaves £750.00 after the allowance.

**Case 7: company whose sole director is its only employee, salary £12,570.**
- Employee NIC: nil, because pay does not exceed the PT.
- Employer NIC: £12,570 minus £5,000 = £7,570. At 15%, that is £1,135.50.
- No Employment Allowance, because the only director is the only employee liable for employer Class 1.
- The director's NIC is worked out on the annual earnings period, and the FPS shows AN or AL.

**Case 8: sole trader reaching State Pension age on 10 October 2026.**
- Class 4 is still due on the full 2026/27 profits.
- It stops from 6 April 2027.
- If the same person also had a job, employee Class 1 would stop from reaching State Pension age, and the employer would continue paying 15%. ([NI introduction](https://www.gov.uk/national-insurance))

## When to refuse or refer

Refer to a qualified UK adviser, or to HMRC, when:

- the person lives or works outside the UK, has a certificate of coverage question, or comes from a country with a social security agreement;
- the person is a mariner, deep-sea fisherman, share fisherman or volunteer development worker (special rates and rules) ([category letters](https://www.gov.uk/national-insurance-rates-letters/category-letters));
- an employer wants Freeport or Investment Zone relief, or wants to check whether an employee works inside a special tax site;
- someone with several jobs wants to defer, or has overpaid across jobs and wants a refund;
- employment status is unclear (employee or self-employed), including off-payroll (IR35) work;
- a group of connected companies or charities must decide which one claims the Employment Allowance;
- someone is deciding whether to pay voluntary contributions for past years. Get the NI record and State Pension forecast first; voluntary contributions do not always increase the State Pension;
- the NI record looks wrong, or a credits decision is disputed (mandatory reconsideration) ([NI credits](https://www.gov.uk/national-insurance-credits)).

Refuse to give a figure when the tax year, status or profit or pay is unknown. Do not guess them. Do not tell a self-employed person that Class 2 is compulsory. Do not tell someone with profits below £7,105 that the year counts automatically. ([self-employed rates](https://www.gov.uk/self-employed-national-insurance-rates))

## Filing and payment

**Employers (Class 1, 1A, 1B).**
- Employee and employer Class 1 is reported on the FPS and paid with PAYE. Payment is due by the 22nd of the next tax month, or by the 22nd after the end of the quarter for employers who pay quarterly. A cheque by post must arrive by the 19th ([pay PAYE](https://www.gov.uk/pay-paye-tax)).
- **Class 1A on benefits:** report on the P11D(b) by 6 July after the tax year, and pay by 22 July (19 July by cheque). A late P11D(b) costs £100 per 50 employees for each month or part month ([deadlines](https://www.gov.uk/employer-reporting-expenses-benefits/deadlines)).
- **Class 1B under a PSA:** apply for the PSA by 5 July after the first tax year it covers. Pay by 22 October after the tax year (19 October by post) ([PSA deadlines](https://www.gov.uk/paye-settlement-agreements/deadlines-and-payment)).

**Self-employed (Class 4 and voluntary Class 2 through Self Assessment).**
- Class 4 is paid with income tax through Self Assessment.
- **Payments on account:** two instalments, each half of last year's bill, due on 31 January and 31 July. They are not needed if last year's bill was less than £1,000, or if more than 80% of the tax was paid at source. The balancing payment is due on 31 January after the tax year ([payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account)).
- **For 2025/26:** the online return and payment are due by 11:59pm on 31 January 2027. Paper returns were due by 31 October 2026 ([deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines)).
- A person who missed paying voluntary Class 2 through Self Assessment must contact the National Insurance helpline for a reference ([pay voluntary Class 2](https://www.gov.uk/pay-class-2-national-insurance)).
- Self Assessment payments to HMRC combine income tax, Class 4, any voluntary Class 2 and sometimes student loan repayments. A bank statement cannot separate them: use the tax calculation (SA302) or the Self Assessment statement ([understand your bill](https://www.gov.uk/understand-self-assessment-bill/payments-on-account)).

**Voluntary Class 2 outside Self Assessment, and Class 3.**
- Register with HMRC. HMRC sends a Class 2 payment request between September and the end of October with an 18-digit reference.
- Allow up to 8 weeks for a payment to show on the NI record ([pay voluntary Class 2](https://www.gov.uk/pay-class-2-national-insurance)).
- Class 3 can be paid online through the Check your State Pension forecast service, by regular payments or by bank transfer. The record updates within 5 working days through the forecast service, or up to 8 weeks otherwise ([pay Class 3](https://www.gov.uk/pay-voluntary-class-3-national-insurance)).

## 2025/26: the year just ended (dated section) ([rates and allowances](https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions))

For 2025/26 (6 April 2025 to 5 April 2026), whose returns and payments are due now ([rates and allowances](https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions); [2025/26 employer rates](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026)):

- LEL £125 a week (£542 a month). PT £242, ST £96 and UEL £967 a week, the same as 2026/27.
- Employee rates 8% and 2%. Employer rate 15%. Class 1A and 1B at 15%. Employment Allowance £10,500.
- SPT £6,845. Voluntary Class 2 £3.50 a week, so £182.00 for 52 weeks. Class 3 £17.75 a week.
- Class 4 is 6% on profits between £12,570 and £50,270 and 2% above, the same as 2026/27.
- **Paying voluntary Class 2 for 2025/26:** it is the previous tax year, so it is paid at the original £3.50 rate, normally through the 2025/26 return due by 31 January 2027.
- **Voluntary Class 3 for 2025/26 and 2024/25:** paid at the original rates for those years (£17.75 and £17.45 a week). The deadline for 2025/26 is 5 April 2032.
- **Employer year-end for 2025/26:** the P11D(b) was due by 6 July 2026 and Class 1A by 22 July 2026. Class 1B under a 2025/26 PSA is due by 22 October 2026.
- **Worked check, 2025/26:** a sole trader with profit of £6,500 is below the £6,845 SPT, so Class 2 is not treated as paid. Voluntary Class 2 of £3.50 x 52 = £182.00 makes the year count. With profit of £30,000, Class 4 is £1,045.80, the same as in 2026/27.
- **For reference, 2024/25:** the employer rate was 13.8% above a £9,100 ST (£175 a week), and the Employment Allowance was £5,000 ([2024/25 employer rates](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025)).

## Completion checklist

### Figures to check against ([rates and thresholds](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027); [self-employed rates](https://www.gov.uk/self-employed-national-insurance-rates))

- [ ] Tax year confirmed, and only that year's rates used.
- [ ] Status confirmed: employee, director, employer, self-employed, or more than one.
- [ ] For employees: category letter checked against HMRC's list, including M, H, V and Z for the 0% employer band.
- [ ] Class 1 worked per pay period, or on the annual earnings period for directors (AN or AL on the FPS).
- [ ] Employer NIC at 15% above £5,000 a year (£96 a week, £417 a month).
- [ ] Employment Allowance eligibility checked: sole director rule, connected group, public-sector work, excluded workers, and one payroll only. No £100,000 test applied.
- [ ] Class 1A and 1B identified and deadlines noted (6 July, 22 July, 22 October).
- [ ] Class 4 on total trading profit: 6% from £12,570 to £50,270, 2% above.
- [ ] Class 2 treated as paid if profit is £7,105 or more. Voluntary Class 2 at £3.65 offered only where it helps.
- [ ] State Pension age timing applied: Class 1 stops at State Pension age; Class 4 stops from the next 6 April.
- [ ] Credits checked before any voluntary payment. NI record and forecast obtained. 6-year deadline (5 April) and original-rate rules applied.
- [ ] Abroad, deferment, special occupations and group Employment Allowance cases referred.
- [ ] Sources recorded for every figure used.

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
