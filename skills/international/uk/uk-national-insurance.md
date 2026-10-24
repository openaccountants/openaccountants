---
name: uk-national-insurance
description: "UK National Insurance contributions for tax year 2026/27 (6 April 2026 to 5 April 2027). Covers Class 1 employee contributions (8% from the GBP 12,570 primary threshold to the GBP 50,270 upper earnings limit, 2% above), employer contributions (15% above the GBP 5,000 secondary threshold), the 0% employer rate for under-21s, apprentices under 25 and veterans, the GBP 10,500 Employment Allowance, Class 1A and 1B at 15%, directors' annual earnings period, Class 2 (no longer a liability, voluntary GBP 3.65 a week below the GBP 7,105 small profits threshold), Class 4 (6% and 2%), Class 3 (GBP 18.40 a week), RTI payment dates, penalties and interest. Trigger on: employer NIC, employee NI, Class 1, Class 1A, Class 2, Class 3, Class 4, Employment Allowance, director NIC, voluntary NI. Out of scope: PAYE income tax and statutory pay (uk-payroll), trading profit computation (uk-self-employment-sa103), cross-border residence (uk-statutory-residence-test)."
version: 3.1
jurisdiction: GB
tax_year: 2026
tax_year_notes: "2026-27"
last_updated: 2026-10-24
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK National Insurance contributions (2026/27)

> **Source-cited draft.** Built from the Social Security Contributions and Benefits Act 1992 (SSCBA), the Social Security (Contributions) Regulations 2001 (SI 2001/1004), HMRC's National Insurance Manual and HMRC pages on GOV.UK, all read on 2026-10-24. No accountant has reviewed it. Do not file from it without review by a qualified UK professional.

Figures are for the 2026/27 tax year, 6 April 2026 to 5 April 2027. Use this skill with `uk-payroll` (PAYE income tax, RTI, statutory pay) and `uk-self-employment-sa103` (computing the trading profit that Class 4 is charged on). Their NIC figures match this skill.

## Who this applies to

- **Employees and office holders (Class 1 primary).** Anyone in an employed earner's employment aged 16 or over, up to State Pension age. Company directors are office holders and pay Class 1 like employees ([NIM12001](https://www.gov.uk/hmrc-internal-manuals/national-insurance-manual/nim12001)). Category letter C (over State Pension age) pays nil employee Class 1 ([employer rates 2026/27](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).
- **Employers (Class 1 secondary, Class 1A, Class 1B).** Every secondary contributor paying earnings above the secondary threshold. The employer still pays 15% for an employee over State Pension age ([employer rates 2026/27](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)).
- **Self-employed (Class 2 and Class 4).** Sole traders and partners with trading profits. Class 2 is no longer a charge: SSCBA s.11(2), which made it payable, was omitted from 6 April 2024 by the National Insurance Contributions (Reduction in Rates) Act 2023, s.3 ([SSCBA s.11](https://www.legislation.gov.uk/ukpga/1992/4/section/11)). Class 4 is due on profits above GBP 12,570 ([SSCBA s.15](https://www.legislation.gov.uk/ukpga/1992/4/section/15)).
- **Out of Class 4:** a person over State Pension age at the start of the tax year, and a person not resident in the UK for income tax in that year (SSCR 2001 reg.91, [link](https://www.legislation.gov.uk/uksi/2001/1004/regulation/91)).
- **Voluntary (Class 2 and Class 3).** People with gaps in their National Insurance record who want the year to count for the State Pension ([voluntary rates](https://www.gov.uk/voluntary-national-insurance-contributions/rates)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Lower earnings limit (LEL) | GBP 129 a week (GBP 559 a month, GBP 6,708 a year) | 2026/27 | SSCR 2001 reg.10(a), [link](https://www.legislation.gov.uk/uksi/2001/1004/regulation/10); [HMRC employer rates](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) |
| Primary threshold (PT) | GBP 242 a week (GBP 1,048 a month, GBP 12,570 a year) | 2026/27 | SSCR 2001 reg.10(c), [link](https://www.legislation.gov.uk/uksi/2001/1004/regulation/10); [HMRC employer rates](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) |
| Secondary threshold (ST) | GBP 96 a week (GBP 417 a month, GBP 5,000 a year), unchanged since 6 April 2025 | 2026/27 | SSCR 2001 reg.10(d), [link](https://www.legislation.gov.uk/uksi/2001/1004/regulation/10); [HMRC employer rates](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) |
| Upper earnings limit (UEL) | GBP 967 a week (GBP 4,189 a month, GBP 50,270 a year) | 2026/27 | SSCR 2001 reg.10(b), [link](https://www.legislation.gov.uk/uksi/2001/1004/regulation/10); [HMRC employer rates](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) |
| Upper secondary threshold, under 21 and apprentice under 25 | GBP 967 a week (GBP 50,270 a year) | 2026/27 | SSCR 2001 reg.10(e) and (f), [link](https://www.legislation.gov.uk/uksi/2001/1004/regulation/10) |
| Veterans upper secondary threshold | GBP 967 a week (GBP 4,189 a month, GBP 50,270 a year) | 2026/27 | National Insurance Contributions Act 2022 (NICA 2022) s.8(2), [link](https://www.legislation.gov.uk/ukpga/2022/9/section/8) |
| Freeport and Investment Zone upper secondary threshold | GBP 481 a week (GBP 2,083 a month, GBP 25,000 a year) | 2026/27 | NICA 2022 s.8(1), [link](https://www.legislation.gov.uk/ukpga/2022/9/section/8); [HMRC employer rates](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) |
| Employee Class 1, main rate (PT to UEL) | 8% | 2026/27 | SSCBA s.8(2)(a), [link](https://www.legislation.gov.uk/ukpga/1992/4/section/8) |
| Employee Class 1, additional rate (above UEL) | 2% | 2026/27 | SSCBA s.8(2)(b), [link](https://www.legislation.gov.uk/ukpga/1992/4/section/8) |
| Employee Class 1, married women and widows reduced rate (letter B), PT to UEL | 1.85% (2% above UEL) | 2026/27 | [HMRC employer rates](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) |
| Employee Class 1, deferment letters (J, Z), PT to UEL | 2% (2% above UEL) | 2026/27 | [HMRC employer rates](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) |
| Employer Class 1 (secondary percentage), above ST, no upper limit | 15% | 2026/27 | SSCBA s.9(2), [link](https://www.legislation.gov.uk/ukpga/1992/4/section/9) |
| Employer rate for under-21s (letters M, Z) up to the upper secondary threshold | 0% | 2026/27 | SSCBA s.9A(3), [link](https://www.legislation.gov.uk/ukpga/1992/4/section/9A) |
| Employer rate for apprentices under 25 (letter H) up to the upper secondary threshold | 0% | 2026/27 | SSCBA s.9B, [link](https://www.legislation.gov.uk/ukpga/1992/4/section/9B) |
| Employer rate for veterans in their first year of civilian employment (letter V) up to the veterans threshold | 0% (relief runs to 2027/28) | 2026/27 | NICA 2022 s.6 and s.7, [link](https://www.legislation.gov.uk/ukpga/2022/9/section/6); tax years extended by SI 2026/231 reg.6, [link](https://www.legislation.gov.uk/uksi/2026/231/made) |
| Employment Allowance, per employer per tax year | GBP 10,500, or the employer's secondary Class 1 liability if less | 2026/27 | National Insurance Contributions Act 2014 (NICA 2014) s.1(2), [link](https://www.legislation.gov.uk/ukpga/2014/7/section/1); [HMRC employer rates](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) |
| Class 1A on benefits in kind | 15% (equal to the secondary percentage) | 2026/27 | SSCBA s.10(5), [link](https://www.legislation.gov.uk/ukpga/1992/4/section/10); [HMRC employer rates](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) |
| Class 1A on termination awards over GBP 30,000 and sporting testimonials over GBP 100,000 | 15% on the excess | 2026/27 | SSCBA s.10(1A) and (4A), [link](https://www.legislation.gov.uk/ukpga/1992/4/section/10); [HMRC employer rates](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027) |
| Class 1B on a PAYE Settlement Agreement | 15% (equal to the secondary percentage) | 2026/27 | SSCBA s.10A(6), [link](https://www.legislation.gov.uk/ukpga/1992/4/section/10A) |
| Small profits threshold (Class 2) | GBP 7,105 a year | 2026/27 | SSCBA s.11(4)(b), [link](https://www.legislation.gov.uk/ukpga/1992/4/section/11) |
| Voluntary Class 2 | GBP 3.65 a week | 2026/27 | SSCBA s.11(6), [link](https://www.legislation.gov.uk/ukpga/1992/4/section/11) |
| Special Class 2: share fishermen / volunteer development workers | GBP 4.30 / GBP 6.45 a week | 2026/27 | [HMRC rates and allowances NIC](https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions) |
| Class 3 voluntary | GBP 18.40 a week | 2026/27 | SSCBA s.13(1), [link](https://www.legislation.gov.uk/ukpga/1992/4/section/13) |
| Class 4 lower and upper profits limits | GBP 12,570 and GBP 50,270 | 2026/27 | SSCBA s.15(3), [link](https://www.legislation.gov.uk/ukpga/1992/4/section/15) |
| Class 4 main rate (LPL to UPL) | 6% | 2026/27 | SSCBA s.15(3ZA)(a), [link](https://www.legislation.gov.uk/ukpga/1992/4/section/15) |
| Class 4 additional rate (above UPL) | 2% | 2026/27 | SSCBA s.15(3ZA)(b), [link](https://www.legislation.gov.uk/ukpga/1992/4/section/15) |
| 2025/26 figures (for 2025/26 returns and voluntary payments due by 31 January 2027) | LEL GBP 125 a week; small profits threshold GBP 6,845; voluntary Class 2 GBP 3.50 a week; Class 3 GBP 17.75 a week; all other Class 1 and Class 4 figures as 2026/27 | 2025/26 | SI 2026/231 regs.3 to 5 (the amounts they replaced), [link](https://www.legislation.gov.uk/uksi/2026/231/made); [HMRC rates and allowances NIC](https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions) |
| Deferment (2 or more jobs): reduced rate in the deferred jobs | 2% on earnings from GBP 242 to GBP 967 a week | 2026/27 | [Defer National Insurance](https://www.gov.uk/defer-national-insurance) |
| Late payment interest (base rate plus 4% from 6 April 2025) | 7.75% a year from 9 January 2026 | current on 2026-10-24 | [HMRC interest rates](https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates) |

The statute fixes the weekly figures (SSCR 2001 reg.10 as amended for 2026/27 by SI 2026/231 reg.5; the GBP 242, GBP 96 and GBP 967 figures were already in place). The monthly and annual equivalents are HMRC's published figures for payroll, except the Freeport and veterans thresholds, whose monthly and annual figures are in NICA 2022 s.8 itself.

## The taxable base

**Class 1 earnings.** Class 1 is charged on earnings paid in each earnings period, usually the pay period (weekly, monthly). Employee NIC is 0% from the LEL to the PT (the earnings still build the NI record), then 8% to the UEL and 2% above. Employer NIC is 15% of everything above the ST, with no cap ([SSCBA s.8](https://www.legislation.gov.uk/ukpga/1992/4/section/8); [s.9](https://www.legislation.gov.uk/ukpga/1992/4/section/9)). HMRC tests the thresholds per job, so each employment is worked out on its own pay.

**Employer reliefs by category letter.**
- Under 21 (M, or Z with deferment) and apprentice under 25 (H): employer pays 0% up to GBP 967 a week, 15% above. The employer is still treated as liable even though the amount is nil ([SSCBA s.9A(6)](https://www.legislation.gov.uk/ukpga/1992/4/section/9A); [s.9B(3)](https://www.legislation.gov.uk/ukpga/1992/4/section/9B)). The upper secondary threshold stops applying once the employee turns 21 ([NIM01297](https://www.gov.uk/hmrc-internal-manuals/national-insurance-manual/nim01297)).
- Veteran (V): 0% up to GBP 967 a week. Conditions: the employee served at least one day in the regular forces, the job is civilian, and the earnings are paid within one year from the first day of the first civilian employment since leaving the forces. The employer elects for the relief. It applies for tax years up to 2027/28 ([NICA 2022 s.6 and s.7](https://www.legislation.gov.uk/ukpga/2022/9/section/7); [SI 2026/231 reg.6](https://www.legislation.gov.uk/uksi/2026/231/made)).
- Freeport and Investment Zone special tax site letters (F, I, L, S, N, E, D, K): 0% up to GBP 481 a week ([NICA 2022 s.1 and s.8(1)](https://www.legislation.gov.uk/ukpga/2022/9/section/1)). Employees who work in a Freeport or Investment Zone but not on a special tax site do not use these letters. Refer these claims.
- Letter X: employees who pay no National Insurance, for example because they are under 16 ([category letters](https://www.gov.uk/national-insurance-rates-letters/category-letters)).

**Two or more jobs: deferment.** Each job is tested on its own. A person with 2 jobs earning GBP 967 or more a week in one and GBP 242 or more in the other (or, with more than 2 jobs, GBP 1,209 or more a week from 2 of them and GBP 242 or more in the others) can apply to defer. The deferred jobs then pay 2% between GBP 242 and GBP 967 a week (letters J and Z), and HMRC collects any shortfall after the year. Apply on form CA72A; for 2026/27 HMRC must receive it by 14 February 2027. The self-employed cannot defer Class 4 ([defer National Insurance](https://www.gov.uk/defer-national-insurance)).

**Directors: annual earnings period.** A person who is a director at the start of the tax year has the whole year as the earnings period. A director appointed during the year has a pro-rata period from the week of appointment (SSCR 2001 reg.8(2) and (3), [link](https://www.legislation.gov.uk/uksi/2001/1004/regulation/8); [NIM12001](https://www.gov.uk/hmrc-internal-manuals/national-insurance-manual/nim12001)). HMRC accepts two methods ([directors](https://www.gov.uk/employee-directors)):
- standard ("AN" on the FPS): at each payment, work out NIC on cumulative pay for the year, less NIC already paid;
- alternative ("AL"): per-period NIC during the year, then an annual recalculation with any shortfall taken from the last payment.
Dividends are not earnings for Class 1. A director who leaves but stays as an employee stays on the annual basis for the rest of that tax year.

**Employment Allowance.** Up to GBP 10,500 a year, set against employer Class 1 each payroll run until used. It cannot exceed the employer Class 1 liability ([Employment Allowance](https://www.gov.uk/claim-employment-allowance)). Eligible: businesses and public bodies doing less than half their work in the public sector, charities, and people employing a care or support worker. Excluded: a company where every payment of earnings in the year goes to one employee who is a director when paid (NICA 2014 s.2(4A)); liabilities on earnings of workers under the IR35 service-company rules (s.2(4)); domestic workers other than care and support workers (s.2(3) and (3A)) ([NICA 2014 s.2](https://www.legislation.gov.uk/ukpga/2014/7/section/2)). One claim per group of connected companies and one payroll only. The former GBP 100,000 liability test no longer applies from April 2025 ([eligibility](https://www.gov.uk/claim-employment-allowance/eligibility)).

**Class 1A and 1B.** Class 1A is 15% of taxable benefits in kind not already charged to Class 1, and of the part of a termination award above GBP 30,000 where Class 1 has not been paid on it ([SSCBA s.10](https://www.legislation.gov.uk/ukpga/1992/4/section/10); [pay Class 1A](https://www.gov.uk/pay-class-1a-national-insurance)). Class 1B is 15% of the items in a PAYE Settlement Agreement plus the tax the employer pays on them ([SSCBA s.10A(2) and (3)](https://www.legislation.gov.uk/ukpga/1992/4/section/10A)). Employees never pay 1A or 1B.

**Class 4 profits.** Class 4 is charged on the profits of all UK trades, professions and vocations, computed as for income tax (SSCBA s.15 and Sch.2, [link](https://www.legislation.gov.uk/ukpga/1992/4/section/15)). Formula: 6% x (lower of profit and 50,270, minus 12,570, if positive) + 2% x (profit minus 50,270, if positive). The profit figure itself comes from `uk-self-employment-sa103`. The trader's own Class 2 and Class 4 are not deductible in computing trading profits; an employer's secondary Class 1, Class 1A and Class 1B are ([ITTOIA 2005 s.53](https://www.legislation.gov.uk/ukpga/2005/5/section/53)).

**Class 2.** With profits of GBP 7,105 or more, Class 2 is treated as paid for each week of self-employment, so the year counts for benefits at no cost. Below that, nothing is due, but the person may pay GBP 3.65 a week ([SSCBA s.11(5A), (5B) and (6)](https://www.legislation.gov.uk/ukpga/1992/4/section/11); [self-employed rates](https://www.gov.uk/self-employed-national-insurance-rates)). Some self-employed people never have Class 2 treated as paid but may pay it voluntarily: examiners, moderators, invigilators and people who set exam questions; landlords eligible to pay Class 2; ministers of religion without a salary or stipend; and people making investments, not as a business and without a fee or commission ([voluntary NI](https://www.gov.uk/voluntary-national-insurance-contributions)). Examiners, moderators and invigilators pay Class 4 as "Special Class 4" by arrangement with the National Insurance office, not through Self Assessment ([self-employed rates](https://www.gov.uk/self-employed-national-insurance-rates)).

**Class 3.** GBP 18.40 a week, for anyone with a gap who cannot use Class 2. Class 2 for the previous tax year and Class 3 for the previous 2 tax years are paid at the original rates; earlier years at the 2026/27 rate ([voluntary rates](https://www.gov.uk/voluntary-national-insurance-contributions/rates)). A married woman or widow paying the reduced rate cannot pay voluntary contributions ([voluntary NI](https://www.gov.uk/voluntary-national-insurance-contributions)).

**Credits and the State Pension.** Check credits before advising a voluntary payment. Class 1 credits (for example on Jobseeker's Allowance, Employment and Support Allowance or Carer's Allowance) count for the State Pension and some other benefits; Class 3 credits (for example on Universal Credit, or Child Benefit for a child under 12) count for the State Pension only ([NI credits](https://www.gov.uk/national-insurance-credits)). The full new State Pension is GBP 241.30 a week; it needs 35 qualifying years, and at least 10 are needed for any State Pension ([new State Pension](https://www.gov.uk/new-state-pension)).

## Deadlines and filing

| What | Deadline | Source |
|---|---|---|
| Report Class 1 on the Full Payment Submission (RTI) | On or before each payday | [Reporting to HMRC: FPS](https://www.gov.uk/running-payroll/reporting-to-hmrc) |
| Pay PAYE and Class 1 (and Class 1A on termination awards) | 22nd of the next tax month (monthly) or 22nd after the quarter end (quarterly); 19th if paying by cheque | [Pay employers' PAYE](https://www.gov.uk/pay-paye-tax) |
| Claim the Employment Allowance | On an EPS, each tax year | [Employment Allowance](https://www.gov.uk/claim-employment-allowance) |
| P11D(b) for 2026/27 benefits (Class 1A) | 6 July 2027 | [benefits deadlines](https://www.gov.uk/employer-reporting-expenses-benefits/deadlines) |
| Pay Class 1A on 2026/27 benefits | 22 July 2027 (19 July by cheque) | [pay Class 1A](https://www.gov.uk/pay-class-1a-national-insurance) |
| Apply for a PSA covering 2026/27 | 5 July 2027 | [PSA deadlines](https://www.gov.uk/paye-settlement-agreements/deadlines-and-payment) |
| Pay Class 1B for 2026/27 | 22 October 2027 (19 October by post) | [PSA deadlines](https://www.gov.uk/paye-settlement-agreements/deadlines-and-payment) |
| Class 4 and voluntary Class 2 for 2025/26 | With the Self Assessment balancing payment, 31 January 2027 (online return the same date) | [SA deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines) |
| Class 4 for 2026/27 | Payments on account 31 January and 31 July 2027; balance 31 January 2028 | [SA deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines) |
| Voluntary Class 2 or 3 for 2026/27 | Up to 5 April 2033 (6-year window) | [voluntary deadlines](https://www.gov.uk/voluntary-national-insurance-contributions/deadlines) |

Class 3 by Direct Debit in 2026/27 is GBP 73.60 in 4-week months and GBP 92.00 in 5-week months ([HMRC rates and allowances NIC](https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions)).

## Penalties and interest

**Late RTI filing (FPS).** Monthly penalty by employer size: 1 to 9 employees GBP 100; 10 to 49 GBP 200; 50 to 249 GBP 300; 250 or more GBP 400. No penalty for the first failure in a tax year, for an FPS late but with payments within 3 days of payday, or for a new employer's first FPS within 30 days ([late reporting](https://www.gov.uk/guidance/what-happens-if-you-dont-report-payroll-information-on-time)).

**Late PAYE and Class 1 payment.** The first late payment in a tax year is not a default. Then 1% of the late amount for 1 to 3 defaults, 2% for 4 to 6, 3% for 7 to 9 and 4% for 10 or more. Still unpaid after 6 months: a further 5%; after 12 months: another 5% ([PAYE late payment penalties](https://www.gov.uk/guidance/what-happens-if-you-dont-pay-paye-and-national-insurance-on-time)).

**Class 1A and 1B.** 5% if not paid within 30 days of the due date, another 5% at 6 months and another 5% at 12 months. A late P11D(b) costs GBP 100 per 50 employees for each month or part month ([PAYE late payment penalties](https://www.gov.uk/guidance/what-happens-if-you-dont-pay-paye-and-national-insurance-on-time); [benefits deadlines](https://www.gov.uk/employer-reporting-expenses-benefits/deadlines)).

**Class 4 through Self Assessment.** Outside Making Tax Digital (and for 2025/26 returns): 5% of the unpaid tax at 30 days, 6 months and 12 months; late filing GBP 100, then GBP 10 a day after 3 months (up to GBP 900), then the greater of 5% or GBP 300 at 6 and 12 months ([SA penalties](https://www.gov.uk/self-assessment-tax-returns/penalties)). A person in Making Tax Digital for Income Tax from 2026/27 is under the new regime for that year. Late payment of the balancing payment: nothing if paid within 15 days; 3% of the tax owed at day 15 if paid on days 16 to 30; 3% at day 15 plus 3% at day 30, plus 10% a year on the balance charged daily from day 31 for up to 2 years, if later. In the first year under the new regime there is no penalty for the first 30 days. Payments on account carry no late payment penalty. Late filing earns a penalty point; at 4 points the penalty is GBP 200, and GBP 200 for each further missed deadline ([MTD penalties](https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax)).

**Interest.** Late payment interest runs daily from the due date at Bank of England base rate plus 4%: 7.75% from 9 January 2026 on the page read on 2026-10-24 ([HMRC interest rates](https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates)). A penalty paid within 30 days of the notice carries no interest.

## Cross-border points

- **Non-residents and Class 4.** A person not resident in the UK for income tax in the year owes no Class 4 (SSCR 2001 reg.91, [link](https://www.legislation.gov.uk/uksi/2001/1004/regulation/91)). Residence comes from `uk-statutory-residence-test`.
- **Working in a country with a social security agreement.** The worker may stay in UK National Insurance and needs a certificate of coverage to avoid paying in the other country ([NI if you go abroad](https://www.gov.uk/national-insurance-if-you-go-abroad)).
- **Working in a country with no agreement.** UK Class 1 continues for the first 52 weeks if the work abroad is temporary, the employer has a UK place of business, the employee is ordinarily resident in the UK and lived in the UK just before going ([NI if you go abroad](https://www.gov.uk/national-insurance-if-you-go-abroad)).
- **Voluntary contributions from abroad.** A person abroad with a certificate of coverage may pay voluntary Class 2 if profits are below GBP 7,105. Without one, Class 2 cannot be paid for time abroad from 6 April 2026 ([Class 2 abroad](https://www.gov.uk/pay-class-2-national-insurance/if-you-work-or-live-abroad)).
- **Class 3 for time abroad from 6 April 2026.** Allowed only for a person who previously lived in the UK for 10 years in a row or has 10 years of qualifying contributions in total (3 years under the old rules for 2025/26 and earlier, and for some applications made by 5 April 2026) ([voluntary NI abroad](https://www.gov.uk/voluntary-national-insurance-contributions/if-you-live-or-work-abroad)).
- **Refer** inbound workers, multi-state workers and any certificate of coverage question.

## Worked examples

**Example 1: employee on GBP 60,000, letter A, paid evenly through 2026/27.** Pay is the same each month, so the annual figure equals the sum of the months. Employee NIC: 8% on GBP 50,270 less GBP 12,570, which is GBP 37,700, giving GBP 3,016.00. Then 2% on GBP 9,730 above the UEL, giving GBP 194.60. Total employee NIC is GBP 3,210.60. Employer NIC: 15% on GBP 60,000 less GBP 5,000, which is GBP 55,000, giving GBP 8,250.00. With no Employment Allowance, the employer pays that in full.

```oa-check
name: Employee GBP 60,000, letter A, 2026/27
inputs:
  pay: 60000
steps:
  - ee_main: (min(pay, 50270) - 12570) * 0.08
  - ee_upper: max(pay - 50270, 0) * 0.02
  - employee_nic: ee_main + ee_upper
  - employer_nic: (pay - 5000) * 0.15
expected:
  ee_main: 3016.00
  ee_upper: 194.60
  employee_nic: 3210.60
  employer_nic: 8250.00
```

**Example 2: director with a March bonus, plus a small sole trade.** A company has two employees: its sole director and a full-time administrator, so the sole-director exclusion does not bar the Employment Allowance. The director was a director on 6 April 2026, so the earnings period is the whole year. Salary is GBP 12,570, paid as GBP 1,047.50 a month, and a GBP 20,000 bonus is paid in March 2027. Annual earnings are GBP 32,570. Employee NIC on the annual basis is 8% of GBP 20,000, which is GBP 1,600.00. Employer NIC is 15% of GBP 27,570, which is GBP 4,135.50 before the Employment Allowance. The edge case: if the bonus month were worked as an ordinary monthly period, the employee would pay 8% only up to the monthly UEL of GBP 4,189 and 2% above it, so GBP 588.45, and nothing in the other 11 months. The annual earnings period stops that saving of GBP 1,011.55. The director also has a sole trade with profit of GBP 8,000. That is below the GBP 12,570 lower profits limit, so Class 4 is nil. It is above the GBP 7,105 small profits threshold, so Class 2 is treated as paid at no cost.

```oa-check
name: Director annual earnings period with bonus, plus side trade, 2026/27
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

## Ask the client first

1. **Status and date of birth.** Employee, director, employer, self-employed, or several at once; and the person's age (under 21, under 25 apprentice, State Pension age).
2. **Pay per period and category letter**, or for a director the date of appointment and every payment of salary and bonus in the year.
3. **For an employer:** number of employees, whether the only director is the only employee, group companies, public-sector share of work, and any IR35 or domestic workers. These decide the Employment Allowance.
4. **Benefits in kind, termination payments over GBP 30,000, or a PAYE Settlement Agreement.** These bring Class 1A or 1B.
5. **Trading profit for 2026/27 from all trades, and UK residence for the year.** These decide Class 4 and Class 2.
6. **Gaps in the NI record and any time abroad.** Get the NI record and State Pension forecast before advising on voluntary Class 2 or 3.

## Sources

| Source | URL | Read on |
|---|---|---|
| SSCBA 1992 s.8 (primary Class 1 rates) | https://www.legislation.gov.uk/ukpga/1992/4/section/8 | 2026-10-24 |
| SSCBA 1992 s.9 (secondary percentage 15%) | https://www.legislation.gov.uk/ukpga/1992/4/section/9 | 2026-10-24 |
| SSCBA 1992 s.9A (under-21 age-related secondary percentage) | https://www.legislation.gov.uk/ukpga/1992/4/section/9A | 2026-10-24 |
| SSCBA 1992 s.9B (apprentices under 25) | https://www.legislation.gov.uk/ukpga/1992/4/section/9B | 2026-10-24 |
| SSCBA 1992 s.10 (Class 1A) | https://www.legislation.gov.uk/ukpga/1992/4/section/10 | 2026-10-24 |
| SSCBA 1992 s.10A (Class 1B) | https://www.legislation.gov.uk/ukpga/1992/4/section/10A | 2026-10-24 |
| SSCBA 1992 s.11 (Class 2, small profits threshold, voluntary rate) | https://www.legislation.gov.uk/ukpga/1992/4/section/11 | 2026-10-24 |
| SSCBA 1992 s.13 (Class 3) | https://www.legislation.gov.uk/ukpga/1992/4/section/13 | 2026-10-24 |
| SSCBA 1992 s.15 (Class 4) | https://www.legislation.gov.uk/ukpga/1992/4/section/15 | 2026-10-24 |
| Social Security (Contributions) Regulations 2001 reg.8 (directors' earnings periods) | https://www.legislation.gov.uk/uksi/2001/1004/regulation/8 | 2026-10-24 |
| Social Security (Contributions) Regulations 2001 reg.10 (limits and thresholds) | https://www.legislation.gov.uk/uksi/2001/1004/regulation/10 | 2026-10-24 |
| Social Security (Contributions) Regulations 2001 reg.91 (Class 4 exceptions) | https://www.legislation.gov.uk/uksi/2001/1004/regulation/91 | 2026-10-24 |
| Social Security (Contributions) (Rates, Limits and Thresholds Amendments, National Insurance Funds Payments and Extension of Veteran's Relief) Regulations 2026 (SI 2026/231) regs.3 to 6 | https://www.legislation.gov.uk/uksi/2026/231/made | 2026-10-24 |
| National Insurance Contributions Act 2022 s.1 (Freeport and Investment Zone relief) | https://www.legislation.gov.uk/ukpga/2022/9/section/1 | 2026-10-24 |
| National Insurance Contributions Act 2022 s.6 and s.7 (veterans relief and conditions) | https://www.legislation.gov.uk/ukpga/2022/9/section/6 | 2026-10-24 |
| National Insurance Contributions Act 2022 s.8 (upper secondary thresholds for special tax sites and veterans) | https://www.legislation.gov.uk/ukpga/2022/9/section/8 | 2026-10-24 |
| National Insurance Contributions Act 2014 s.1 (Employment Allowance amount) | https://www.legislation.gov.uk/ukpga/2014/7/section/1 | 2026-10-24 |
| National Insurance Contributions Act 2014 s.2 (excluded liabilities and excluded companies) | https://www.legislation.gov.uk/ukpga/2014/7/section/2 | 2026-10-24 |
| Income Tax (Trading and Other Income) Act 2005 s.53 (NIC not deductible) | https://www.legislation.gov.uk/ukpga/2005/5/section/53 | 2026-10-24 |
| HMRC NIM12001 (directors: introduction) | https://www.gov.uk/hmrc-internal-manuals/national-insurance-manual/nim12001 | 2026-10-24 |
| HMRC NIM01297 (upper secondary threshold, under 21) | https://www.gov.uk/hmrc-internal-manuals/national-insurance-manual/nim01297 | 2026-10-24 |
| HMRC, Rates and thresholds for employers 2026 to 2027 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 | 2026-10-24 |
| HMRC, Rates and allowances: National Insurance contributions | https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions | 2026-10-24 |
| GOV.UK, Self-employed National Insurance rates | https://www.gov.uk/self-employed-national-insurance-rates | 2026-10-24 |
| GOV.UK, Voluntary National Insurance: rates | https://www.gov.uk/voluntary-national-insurance-contributions/rates | 2026-10-24 |
| GOV.UK, Voluntary National Insurance: who can pay | https://www.gov.uk/voluntary-national-insurance-contributions | 2026-10-24 |
| GOV.UK, Voluntary National Insurance: if you live or work abroad | https://www.gov.uk/voluntary-national-insurance-contributions/if-you-live-or-work-abroad | 2026-10-24 |
| GOV.UK, Defer National Insurance | https://www.gov.uk/defer-national-insurance | 2026-10-24 |
| GOV.UK, National Insurance credits | https://www.gov.uk/national-insurance-credits | 2026-10-24 |
| GOV.UK, The new State Pension | https://www.gov.uk/new-state-pension | 2026-10-24 |
| GOV.UK, Voluntary National Insurance: deadlines | https://www.gov.uk/voluntary-national-insurance-contributions/deadlines | 2026-10-24 |
| GOV.UK, NI category letters | https://www.gov.uk/national-insurance-rates-letters/category-letters | 2026-10-24 |
| GOV.UK, Employment Allowance and eligibility | https://www.gov.uk/claim-employment-allowance/eligibility | 2026-10-24 |
| GOV.UK, NIC for company directors | https://www.gov.uk/employee-directors | 2026-10-24 |
| GOV.UK, Reporting to HMRC: FPS | https://www.gov.uk/running-payroll/reporting-to-hmrc | 2026-10-24 |
| GOV.UK, Pay employers' PAYE | https://www.gov.uk/pay-paye-tax | 2026-10-24 |
| GOV.UK, Pay Class 1A | https://www.gov.uk/pay-class-1a-national-insurance | 2026-10-24 |
| GOV.UK, Expenses and benefits deadlines | https://www.gov.uk/employer-reporting-expenses-benefits/deadlines | 2026-10-24 |
| GOV.UK, PSA deadlines and payment | https://www.gov.uk/paye-settlement-agreements/deadlines-and-payment | 2026-10-24 |
| HMRC, Late reporting penalties (RTI) | https://www.gov.uk/guidance/what-happens-if-you-dont-report-payroll-information-on-time | 2026-10-24 |
| HMRC, Late payment penalties for PAYE and NIC | https://www.gov.uk/guidance/what-happens-if-you-dont-pay-paye-and-national-insurance-on-time | 2026-10-24 |
| GOV.UK, Self Assessment deadlines and penalties | https://www.gov.uk/self-assessment-tax-returns/penalties | 2026-10-24 |
| HMRC, Penalties for Making Tax Digital for Income Tax | https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax | 2026-10-24 |
| HMRC, Interest rates for late and early payments | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | 2026-10-24 |
| GOV.UK, National Insurance if you go abroad | https://www.gov.uk/national-insurance-if-you-go-abroad | 2026-10-24 |
| GOV.UK, Pay voluntary Class 2 if you work or live abroad | https://www.gov.uk/pay-class-2-national-insurance/if-you-work-or-live-abroad | 2026-10-24 |

Not yet confirmed: whether an under-21 employee paid at the 0% age-related rate makes a second "payment of earnings" for the single-director Employment Allowance exclusion (NICA 2014 s.2(4A)); the PAYE payment rule in SSCR 2001 Sch.4 (GOV.UK page used); the statutory basis of the MTD for Income Tax late payment penalty rates (GOV.UK page used).

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
