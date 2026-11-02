---
name: kosovo-payroll
description: >
  Calculate the Kosovo wage-tax and pension components for 2026 employers and employees. Covers primary and secondary employers, current monthly income-tax bands, deduction of employee pension before withholding, voluntary pension limits, benefits in kind, documented travel and commuting exclusions, the two minimum-wage periods, employee notification, WM and CM filing, withholding certificates, and current procedural penalties. Distinguishes tax residence from pension coverage and routes foreign employment and other income to the relevant review. Use for gross-to-net pay, salary withholding, secondary employment, EDI payroll, pension deductions, and payroll reconciliation. Final health-inclusive payroll remains partial pending the new healthcare law's operative phase and collection instruments.
version: 0.2
jurisdiction: XK
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants skill License v1.0 (content)
---

# Kosovo payroll v0.2

Tax year **2026**. Checked against the law on **30 October 2026** (tier 2); no
licensed accountant has signed it off.

## Who this applies to

Employers paying Kosovo-taxable wages must withhold PIT when wages are paid.
PIT Law 05/L-028 art. 38 includes specified professional, management, service-
contract, performance and dependent-agent payments to non-business individuals.
Do not decide tax treatment from the invoice label alone. Establish the worker's
actual status, taxable source and principal-employer designation
([05/L-028 arts. 2–4, 37–38](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf)).

Residents are taxed on Kosovo and foreign-source income; non-residents on
Kosovo-source income. Residence includes principal residence in Kosovo or
physical presence for 183 days in any twelve-month period, not simply more
than half a calendar year (05/L-028 art. 2(1.18)). Business income, investment
income and foreign tax credits are reconciled in the income-tax and cross-
border skills. Pension coverage has a separate residence/temporary-stay test.

## Rates, bands and thresholds

All amounts are EUR. PIT bands apply to **taxable wage after the employee's
allowable pension contribution**, not automatically to gross cash pay.

| Item | Amount or rule | Period | Official authority |
|---|---|---|---|
| Primary-employer monthly taxable wage, first band | Up to EUR 250 inclusive: 0% | 2026 | [05/L-028 art. 6, replaced by 08/L-142 art. 5](https://gzk.rks-gov.net/ActDetail.aspx?ActID=96360&langid=2); [TAK monthly table](https://www.atk-ks.org/en/portfolio/informata-te-pergjithshme-per-tatimet-ne-kosove/) |
| Primary-employer second band | Above EUR 250 to EUR 450 inclusive: 8% of excess over EUR 250 | 2026 | [Amended art. 6](https://gzk.rks-gov.net/ActDetail.aspx?ActID=96360&langid=2); [TAK monthly table](https://www.atk-ks.org/en/portfolio/informata-te-pergjithshme-per-tatimet-ne-kosove/) |
| Primary-employer top band | Above EUR 450: EUR 16 plus 10% of excess over EUR 450 | 2026 | [Amended art. 6](https://gzk.rks-gov.net/ActDetail.aspx?ActID=96360&langid=2); [TAK monthly table](https://www.atk-ks.org/en/portfolio/informata-te-pergjithshme-per-tatimet-ne-kosove/) |
| Secondary-employer withholding | 10% of taxable wage after employee pension deduction | 2026 | [05/L-028 art. 38(3)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf); [AI 01/2016 art. 37(3)–(4)](https://gzk.rks-gov.net/ActDocumentDetail.aspx?ActID=12233) |
| Employee and employer mandatory pension | 5% each, subject to separate coverage/base rules | 2026 | [04/L-101 art. 6](https://bqk-kos.org/wp-content/uploads/2024/11/Law-on-Pension-Funds.pdf?lang=en) |
| Voluntary pension top-up | Additional maximum 10 percentage points each, total maximum 15% each | 2026 | [04/L-101 art. 6(2)(c)](https://bqk-kos.org/wp-content/uploads/2024/11/Law-on-Pension-Funds.pdf?lang=en); [AI art. 37(4.3)–(4.4)](https://gzk.rks-gov.net/ActDocumentDetail.aspx?ActID=12233) |
| Benefit-in-kind monthly threshold | EUR 65; include only the excess under this rule | 2026 | [AI 01/2016 art. 14(1)](https://gzk.rks-gov.net/ActDocumentDetail.aspx?ActID=12233) |
| Minimum full-time wage / regular hourly wage | EUR 425 monthly / EUR 2.50 hourly | 1 January–30 June 2026 | [Decision 10/273 para. 1.1](https://kryeministri.rks-gov.net/wp-content/uploads/2025/10/Vendimet-e-mbledhjes-se-273-te-te-Qeverise.pdf) |
| Minimum full-time wage / regular hourly wage | EUR 500 monthly / EUR 3 hourly | From 1 July 2026 | [Decision 10/273 para. 1.2](https://kryeministri.rks-gov.net/wp-content/uploads/2025/10/Vendimet-e-mbledhjes-se-273-te-te-Qeverise.pdf) |
| Standard health wage shares in new law | 3.5% employee and 3.5% employer; operative phase remains unconfirmed | Subject to 2026 transition | [10/L-028 arts. 22(1), 35(2)](https://gzk.rks-gov.net/ActDetail.aspx?ActID=119938&langid=1) |

The annual PIT equivalents are 0% through EUR 3,000; 8% on the next EUR
2,400; then EUR 192 plus 10% above EUR 5,400. Do not reuse the superseded
4% band in the unamended 2015 PDF (08/L-142 art. 5). The current bands apply
from 23 August 2024, when 08/L-142 was published and entered into force
(art. 7); a correction to an earlier pay period uses the schedule then in force.

## The base

Build gross taxable employment income from salary, bonuses, cash allowances,
personal expenses paid by the employer, debt forgiveness and other wage items
under PIT art. 9(1). The specific monthly benefit-in-kind rule includes only the
amount exceeding EUR 65: an ordinary benefit of EUR 90 adds EUR 25, not EUR 90
(AI art. 14(1)). This is not an exemption for a cash bonus, and does not replace
the pension law's market-value rule for wages paid substantially in kind.

Separate statutory exclusions before calculating PIT. Article 9(2) excludes
qualifying documented business travel and work-accident indemnities, employer-
provided meals and transport in kind, and specified commuting reimbursements.
AI art. 14(2) requires written business-trip authority, business purpose and
claims. It limits domestic lodging to EUR 50 daily; domestic meals to EUR 15
daily or EUR 25 for overnight trips; own-vehicle domestic travel to EUR 0.16/km.
Foreign travel requires the relevant official limits and evidence, rather than
those domestic amounts. Article 9(2.4)–(2.6) gives distinct commuting conditions;
do not treat every cash travel allowance as exempt
([PIT art. 9](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf); [AI art. 14](https://gzk.rks-gov.net/ActDocumentDetail.aspx?ActID=12233)).

Deduct the employee's allowable pension from the taxable wage before applying
**either** principal-employer bands or secondary-employer 10%. Do not deduct the
employer's pension from the employee's wage. Primary and secondary employers
each apply the contribution rules to their own payments. The employer's own
contribution is its expense under the pension law
([AI art. 37(2)–(4.7)](https://gzk.rks-gov.net/ActDocumentDetail.aspx?ActID=12233); [04/L-101 art. 37 as replaced by 05/L-116 art. 10](https://bqk-kos.org/wp-content/uploads/2024/11/Law-05-L116-on-Amending-and-Supplementing-The-Law-on-Pension-Funds-Of-Ko.pdf)).

The employer's monthly EDI payroll list records the employee's principal-
employer selection under AI 03/2016 art. 6, replacing the former AI art. 7(3)
procedure. Obtain that designation; do not default every employer to principal
or tax all second-job gross cash before pension
([AI 03/2016 art. 6](https://gzk.rks-gov.net/ActDocumentDetail.aspx?ActID=12507)).

For a nonnegative monthly taxable wage `T`, principal-employer PIT is
`0.08 * max(0, min(T, 450) - 250) + 0.10 * max(0, T - 450)`.
Use the actual payroll period and paid amounts. Reconcile corrections and
prior withholding to avoid withholding the same wage twice (PIT art. 38(2)).

**2026 health-law change.** Law 10/L-028 was published on 15 May 2026;
art. 37 provides entry into force fifteen days after publication. Article 36
repeals Law 04/L-249, its amendment and derived by-laws. The old description of
04/L-249 as the current dormant law is therefore obsolete.

Article 22(1) sets a standard wage contribution of 7%, split 3.5% employee and
3.5% employer. Article 35(2) allows different rates during the first five years
of operation, with phase contributions approved through the government and
Assembly process. Article 22(2), (13) and (21) requires collection procedures.
A statutory standard rate alone does not establish the operative collection
period, phased rate or filing process. Obtain those instruments before adding
a health deduction. This skill supplies pension and wage-tax components and
leaves final health-inclusive payroll open; it does not certify either a zero
health liability or automatic collection at the standard rate
([10/L-028 arts. 21–22, 35–37](https://gzk.rks-gov.net/ActDetail.aspx?ActID=119938&langid=1)).

## Deadlines and filing

| Obligation | Deadline and route | Official authority |
|---|---|---|
| Notify employment contract | One day before work begins, in TAK's prescribed form | [08/L-257 art. 43(5)](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf) |
| Wage withholding statement and payment | By the 15th following each calendar month, WM through TAK EDI | [PIT art. 38(5)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf); [TAK forms timetable](https://www.atk-ks.org/en/portfolio/informata-te-pergjithshme-per-tatimet-ne-kosove/) |
| Pension declaration and payment | Monthly CM, by the 15th following the month; employee list before payment | [04/L-101 art. 6(3), (10)](https://bqk-kos.org/wp-content/uploads/2024/11/Law-on-Pension-Funds.pdf?lang=en); [TAK WM/CM timetable](https://www.atk-ks.org/en/portfolio/informata-te-pergjithshme-per-tatimet-ne-kosove/) |
| Employee withholding certificate | By 1 March of the following year; for 2026, 1 March 2027 | [PIT art. 38(6)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) |
| Annual individual return, where required | By 31 March of the following year; for 2026, 31 March 2027 | [PIT art. 48](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) |

Keep employee IDs, principal-employer designation, cash/benefit schedules,
pension elections, withholding certificates and payment receipts. Reconcile
WM, CM, payroll totals, bank payments and Trust allocations. A transfer to TAK
is not proof of which tax, period or worker it cleared.

PIT art. 48(2.1) exempts taxpayers receiving only wages from the annual-return
requirement; art. 48(3) permits an election to file. Do not invent a mandatory
annual return for every two-employer worker or a separate employer annual
reconciliation deadline from the employee-certificate rule. Additional income
or a refund/credit claim changes the annual reconciliation.

## Penalties and interest

Use Law 08/L-257, not the repealed Law 03/L-222's penalty schedule.

| Failure | Current statutory consequence | Official authority |
|---|---|---|
| Missing mandatory return that results in a tax liability | EUR 50 per return for a business natural person; EUR 150 for a legal entity; EUR 20 for a non-business natural person | [08/L-257 art. 99](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf) |
| Understatement or excess refund/credit | 15% of the difference if it is at most 10% of correct tax; 25% if it exceeds 10% | [08/L-257 art. 100(1)](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf) |
| Failure to withhold and pay over wage tax | 25% of the unpaid difference | [08/L-257 art. 103(1)](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf) |
| Failure to withhold or pay pension contributions | 25% of the unpaid contribution difference | [08/L-257 art. 103(2)](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf) |
| Failure to notify TAK of an employee as required | EUR 500 per undeclared worker | [08/L-257 art. 102(3)](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf) |

Late-payment interest runs for each month or part-month, for at most ten years.
The Minister sets the rate at least annually and TAK publishes it. Under a
compliant instalment agreement interest stops from the following month; default
reinstates it. The rate must be higher than commercial bank lending rates in
Kosovo (art. 24(3)). Apply the published rate for the liability period, not an old
presentation or the rate for commercial debts ([08/L-257 art. 24](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf)).
These fines
have distinct statutory triggers; do not automatically add every row to every
correction.

## Cross-border points

A resident's foreign wages belong in the worldwide-income review; a non-
resident's Kosovo-source wages require source and treaty analysis. Confirm the
actual work location, employer, payment bearer, days and treaty period. The
183-day residence rule is not a universal treaty wage exemption. Do not exempt
remote work merely because the payer is foreign
([PIT arts. 2–4, 38, 47–48](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf)).

For pension, apply the separate prohibition for foreign employees with
temporary stay in 04/L-101 art. 6(14), alongside resident coverage under
art. 6(13). Obtain any applicable social-security agreement evidence. The
health law's own insured categories and phase rules require separate testing.
Use [xk-cross-border](xk-cross-border.md) for business-payment withholding and
PE rules; a nonresident service invoice is not automatically employee wages.

## Two worked examples that recompute

Both examples compute **PIT and mandatory pension components only**. Their
cash remainder and employer cost exclude any health component and other
contractual deductions; they are not a health-inclusive final payslip.

### 1. Principal employer, EUR 600 cash wage

Assume an ordinary resident employee below pension age, one principal employer,
no benefits or voluntary pension. Employee pension is EUR 30, leaving taxable
wage EUR 570. PIT is EUR 16 plus 10% of EUR 120, or EUR 28. Cash remaining
after these two deductions is EUR 542. Employer wage plus pension is EUR 630.

```oa-check
name: Kosovo primary-employer wage PIT after employee pension 2026
inputs:
  gross_cash: 600
steps:
  - employee_pension: gross_cash * 0.05
  - employer_pension: gross_cash * 0.05
  - taxable_wage: gross_cash - employee_pension
  - lower_band: max(0, min(taxable_wage, 450) - 250) * 0.08
  - upper_band: max(0, taxable_wage - 450) * 0.10
  - wage_pit: lower_band + upper_band
  - cash_after_pit_and_pension: gross_cash - employee_pension - wage_pit
  - wage_plus_employer_pension: gross_cash + employer_pension
expected:
  employee_pension: 30
  employer_pension: 30
  taxable_wage: 570
  wage_pit: 28
  cash_after_pit_and_pension: 542
  wage_plus_employer_pension: 630
```

### 2. Secondary employer, part-time EUR 400 wage

Assume the same pension coverage, documented secondary-employer status,
part-time hours consistent with the hourly minimum, and no benefits/top-up.
Employee pension EUR 20 reduces taxable wage to EUR 380. Secondary PIT is
EUR 38, leaving EUR 342 after those deductions. Employer wage plus pension
is EUR 420. There is no second principal-employer tax-free band and no
full-time EUR 500 contribution floor imposed on this part-time example.

```oa-check
name: Kosovo secondary-employer PIT on pension-adjusted wage 2026
inputs:
  gross_cash: 400
steps:
  - employee_pension: gross_cash * 0.05
  - employer_pension: gross_cash * 0.05
  - taxable_wage: gross_cash - employee_pension
  - wage_pit: taxable_wage * 0.10
  - cash_after_pit_and_pension: gross_cash - employee_pension - wage_pit
  - wage_plus_employer_pension: gross_cash + employer_pension
expected:
  employee_pension: 20
  employer_pension: 20
  taxable_wage: 380
  wage_pit: 38
  cash_after_pit_and_pension: 342
  wage_plus_employer_pension: 420
```

## Ask the client first

1. Where did the person work, what are their residence/stay status and age, and does an agreement or coverage certificate apply?
2. Which employer is designated principal in the EDI payroll list, and what other paid employments or income exist?
3. Which pay period, hours, gross/net contract, bonuses, cash allowances and benefits apply?
4. What pension election and health implementation instrument apply to that period?
5. What travel/commuting evidence and actual business purpose support each claimed exclusion?
6. Which wage/pension returns, certificates, payments and prior-period corrections need reconciliation?


## Sources

| Official source and provisions read | URL | Read on |
|---|---|---|
| Personal Income Tax Law 05/L-028 arts. 2–9, 37–38, 47–48; read with 2024 amendment | https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf | 2026-10-30 |
| 08/L-142 art. 5, replacement PIT art. 6 | https://gzk.rks-gov.net/ActDetail.aspx?ActID=96360&langid=2 | 2026-10-30 |
| PIT AI 01/2016 arts. 7, 14, 37; read with 03/2016 amendment | https://gzk.rks-gov.net/ActDocumentDetail.aspx?ActID=12233 | 2026-10-30 |
| AI 03/2016 art. 6, replacement principal-employer reporting procedure | https://gzk.rks-gov.net/ActDocumentDetail.aspx?ActID=12507 | 2026-10-30 |
| Pension Funds Law 04/L-101 arts. 1 and 6 | https://bqk-kos.org/wp-content/uploads/2024/11/Law-on-Pension-Funds.pdf?lang=en | 2026-10-30 |
| Pension amendment 05/L-116 art. 10, tax treatment | https://bqk-kos.org/wp-content/uploads/2024/11/Law-05-L116-on-Amending-and-Supplementing-The-Law-on-Pension-Funds-Of-Ko.pdf | 2026-10-30 |
| Decision 10/273 para. 1, both 2026 wage periods | https://kryeministri.rks-gov.net/wp-content/uploads/2025/10/Vendimet-e-mbledhjes-se-273-te-te-Qeverise.pdf | 2026-10-30 |
| Tax-procedure Law 08/L-257 arts. 24, 43(5), 99–103 | https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf | 2026-10-30 |
| TAK current monthly wage bands, forms and filing timetable; read in ordinary browser | https://www.atk-ks.org/en/portfolio/informata-te-pergjithshme-per-tatimet-ne-kosove/ | 2026-10-30 |
| Compulsory Healthcare Insurance Law 10/L-028 arts. 21–22 and 35–37; actual Gazette PDF downloaded through its public form | https://gzk.rks-gov.net/ActDetail.aspx?ActID=119938&langid=1 | 2026-10-30 |
| Official health fund copy of 10/L-028; full normalised text matches the Gazette download | https://fssh.rks-gov.net/wp-content/uploads/2026/05/LIGJI-PER-SIGURIMIN-E-DETYRUESHEM-TE-KUJDESIT-SHENDETESOR-2.pdf | 2026-10-30 |

Not yet confirmed: operative 2026 health-insurance phase, contribution rates, collection commencement and filing instruments; numeric 2026 tax late-interest rate; foreign-travel limit instruments for an actual destination and date. PR remains partial for a complete health-inclusive payroll result.

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
