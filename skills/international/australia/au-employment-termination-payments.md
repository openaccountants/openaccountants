---
name: au-employment-termination-payments
description: >
  Use this skill for any Australian employment termination question: employment
  termination payments (ETPs), genuine redundancy, the tax-free redundancy limit,
  the ETP cap and whole-of-income cap, unused annual and long service leave on
  termination, payment in lieu of notice, ETP codes and STP reporting, delayed
  termination payments and death benefit ETPs. Trigger on "ETP", "redundancy
  payment", "genuine redundancy tax-free", "lump sum D", "Schedule 11",
  "Schedule 7", "termination pay withholding", "golden handshake", "payment in
  lieu of notice", "preservation age ETP", "whole-of-income cap", "ETP code R",
  "ETP code O". Covers 2026-27 figures for employers, payroll staff and advisers.
version: 1.0
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27 income year (1 July 2026 to 30 June 2027)"
last_updated: 2026-09-27
review_status: pending_review
depends_on:
  - australia-payroll
  - au-super-guarantee
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Employment Termination Payments

## Australia Employment Termination Payments and Redundancy v1.0

> **General reference only.** This skill is general tax and accounting reference material for
> AI-assisted workflows. It has not been reviewed for any specific person's facts, documents,
> elections, deadlines, residency, filing status or local procedures. Do not rely on it to
> lodge, pay, amend or take a tax position without review by a qualified professional.

## Section 1 - Quick Reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Australia |
| Income year covered | 2026-27 (1 July 2026 to 30 June 2027) |
| ETP cap | $270,000, indexed annually |
| Whole-of-income cap | $180,000, not indexed, reduced by the employee's other taxable payments in the year |
| Genuine redundancy tax-free limit | $13,598 plus $6,801 for each completed year of service |
| Withholding on the taxable component within the cap | 32% under preservation age, 17% at or above preservation age |
| Withholding above the cap | 47% |
| Preservation age | 60 for anyone born after 30 June 1964 |
| Age-pension age | 67 for anyone born on or after 1 January 1957 |
| ETP timing rule | Paid within 12 months of termination, unless the ATO approves a later payment |
| Withholding tables | Schedule 11 for ETPs and Schedule 7 for unused leave, both applying from 1 July 2026 |
| Reporting | STP pay event with an ETP code, or an ETP payment summary within 14 days |
| Primary legislation | ITAA 1997 Divisions 82 and 83; TAA 1953 Schedule 1 sections 12-85 and 12-90 |
| Tax authority | Australian Taxation Office |
| Reviewed by | Pending. Australian CPA or CA review required |

## Section 2 - The calculation workflow

Work through these steps for every termination. Each component of the package gets its own
treatment, and the order matters because the code R part reduces the cap left for the code O part.

**Step 1. Split the package into components.**
Salary and wages owed, unused leave, the genuine redundancy or early retirement scheme amount,
the ETP components, and anything that is not an ETP at all (superannuation, foreign termination
payments, employee share scheme amounts, some restraint of trade payments). See Section 3.

**Step 2. Test whether the redundancy is genuine.**
The employer must have decided that the job no longer exists and dismissed the employee, who must
be under age-pension age on the day of dismissal. See Section 4.

**Step 3. Work out the tax-free limit.**
$13,598 plus $6,801 for each completed year of service in 2026-27. The genuine redundancy amount
up to the limit is tax-free, is reported at lump sum D and is not an ETP.

**Step 4. Treat any excess as an ETP.**
Identify a tax-free component (service before 1 July 1983 or an invalidity segment); the rest is
the taxable component. See Section 5.

**Step 5. Choose the cap.**
A code R payment uses the ETP cap only. A code O payment uses the smaller of the ETP cap and the
whole-of-income cap. See Section 6.

**Step 6. Withhold from the taxable component.**
32% or 17% up to the cap, depending on the employee's age at the end of the income year, and 47%
above it. See Section 7.

**Step 7. Withhold from unused leave under Schedule 7.**
The rate depends on the reason for termination and when the leave accrued. See Section 8.

**Step 8. Report each component in its own place.**
Each ETP carries a code, and a redundancy excess and a golden handshake from the same termination
are reported as two ETPs. See Section 9.

## Section 3 - What is and is not an ETP

**Payments in and out of the ETP**

| Included in the ETP | Not an ETP |
| --- | --- |
| Gratuity or golden handshake | Unused annual leave and long service leave (Schedule 7 applies) |
| Genuine redundancy or early retirement scheme amount above the tax-free limit | Genuine redundancy or early retirement scheme amount up to the tax-free limit |
| Severance pay and a non-genuine redundancy payment | Salary, wages, allowances, bonuses and incentives owed for work done or leave taken |
| Payment in lieu of notice | Superannuation benefits |
| Unused sick leave and unused rostered days off | Foreign termination payments |
| Compensation for loss of job, and for wrongful dismissal paid within 12 months | Certain restraint of trade payments |
| Payments for loss of future super | Certain personal injury compensation for the inability to be employed |
| Payments on termination because of ill health, other than personal injury compensation | Employee share scheme payments, advances and loans |
| Lump sums paid on the death of an employee | |

- **Definition** — An ETP is a lump sum paid in consequence of the termination of employment and received within 12 months of that termination, unless the ATO has determined otherwise. A payment from a super fund is never an ETP.  _([ITAA 1997 (Cth) s 82-130](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/82-130))_
- **The 12-month rule** — A payment made more than 12 months after termination is a delayed termination payment, not an ETP, unless the ATO approves ETP treatment. Withhold 32% from a delayed termination payment (47% from a resident and 45% from a foreign resident who has not quoted a TFN) and report it as gross payments. The exception is a genuine redundancy amount above the tax-free limit, which stays an ETP however late it is paid.  _([ATO, Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments))_
- **Life and death benefit ETPs** — A life benefit ETP is paid to the employee. A death benefit ETP is paid to a dependant, a non-dependant or the trustee of the estate because employment ended on death, and the withholding depends on who receives it. See Section 7.  _([ATO, Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments))_
- **Payments that are ETPs** — The ATO's lists of payments inside and outside an ETP are the starting point for Step 1, and compensation for wrongful dismissal counts only when paid within 12 months of the actual termination.  _([ATO, Payments that are ETPs](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/payments-that-are-etps))_

## Section 4 - Genuine redundancy and early retirement schemes

- **What makes a redundancy genuine** — The employer decides that the position no longer exists and dismisses the employee. Dismissal is the employer's decision to end the employment, so an employee who accepts a package offered to minimise disruption or to comply with a workplace agreement is still dismissed, and a redundancy stays genuine when the employer calls for expressions of interest before choosing whom to dismiss. TR 2009/2 adds that the parties must deal at arm's length, the payment must exceed what the employee would have received on voluntary resignation, and there must be no arrangement to re-employ the person.  _([ATO, Redundancy and early retirement](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/redundancy-and-early-retirement))_
- **Non-genuine redundancy** — A payment is not a genuine redundancy payment where the employee is dismissed on reaching normal retirement age, is at or above age-pension age on the day of dismissal, leaves voluntarily, has a contract that simply ends, or is dismissed for disciplinary or inefficiency reasons. An employee left with little choice but to resign, for example through a pay cut or an unsuitable alternative role, is generally a non-genuine redundancy. The whole payment is then an ETP coded O.  _([ATO, Redundancy and early retirement](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/redundancy-and-early-retirement))_

**Age-pension age**

| Date of birth | Age-pension age |
| --- | --- |
| Before 1 July 1952 | 65 |
| 1 July 1952 to 31 December 1953 | 65 and 6 months |
| 1 January 1954 to 30 June 1955 | 66 |
| 1 July 1955 to 31 December 1956 | 66 and 6 months |
| On or after 1 January 1957 | 67 |

- **The tax-free limit for 2026-27** — Base amount $13,598 plus $6,801 for each completed year of service. Part years do not count. The amount up to the limit is reported at lump sum D on the income statement, is not an ETP and has no withholding. Anything above the limit is an ETP coded R and subject only to the ETP cap.  _([ATO, Schedule 11, note 1](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments))_
- **Early retirement schemes** — A scheme needs ATO approval by class ruling before it starts, must be open to a broad class of employees and must form part of a reorganisation of the business, such as a closure, relocation or the introduction of new technology. Payments under an approved scheme use the same tax-free limit as a genuine redundancy.  _([ATO, Redundancy and early retirement](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/redundancy-and-early-retirement))_
- **Age limit since 2019** — Dismissals on or after 1 July 2019 use age-pension age rather than 65. An employer who withheld on the old basis can refund the excess and correct the STP report.  _([ATO, Redundancy and early retirement](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/redundancy-and-early-retirement))_
- **Ruling** — TR 2009/2 sets out the Commissioner's view on each condition, including dismissal, arm's length dealing and the exclusion of payments the employee would have received anyway.  _([TR 2009/2 Income tax: genuine redundancy payments](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20092/NAT/ATO/00001))_

## Section 5 - Tax-free and taxable components of an ETP

- **Tax-free component** — Only two things create a tax-free component: service before 1 July 1983 and an invalidity segment. Everything else is the taxable component. Do not withhold from the tax-free component, but report both.  _([ATO, Tax-free component of ETPs](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/tax-free-component-of-etps))_
- **Pre-1 July 1983 segment** — Subtract any invalidity segment from the ETP, then multiply the result by the days of employment before 1 July 1983 divided by the total days of employment the ETP relates to.  _([ATO, Tax-free component of ETPs](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/tax-free-component-of-etps))_
- **Invalidity segment** — Available only where employment ended because of ill health and two medical practitioners certify that the employee is unlikely ever to work again in a capacity for which they are reasonably qualified. The segment equals the ETP multiplied by the days to retirement divided by the sum of employment days and days to retirement, where retirement is generally the day the employee turns 65. A death benefit ETP cannot include an invalidity segment.  _([ATO, Tax-free component of ETPs](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/tax-free-component-of-etps))_

## Section 6 - Which cap applies

**ETP codes and caps**

| Code | Payment | Cap |
| --- | --- | --- |
| R | Early retirement scheme or genuine redundancy amount above the tax-free limit; invalidity; compensation for personal injury, unfair dismissal, harassment or discrimination | ETP cap only |
| O | Golden handshake, gratuity, non-genuine redundancy, severance pay, payment in lieu of notice, unused sick leave, unused rostered days off and any other life benefit ETP | Smaller of the ETP cap and the whole-of-income cap |
| S | A code R payment where a code R, code O or transitional payment for the same termination was made in an earlier income year | ETP cap only |
| P | A code O payment where a code R, code O or transitional payment for the same termination was made in an earlier income year | Smaller of the two caps |
| D | Death benefit paid to a dependant | ETP cap |
| N | Death benefit paid to a non-dependant | ETP cap |
| B | Death benefit paid to a non-dependant where a payment for the same termination was made in an earlier income year | ETP cap |
| T | Death benefit paid to the trustee of the deceased estate | No withholding |

- **ETP cap** — $270,000 for 2026-27, indexed annually. Every ETP for the same termination shares the one cap, so a later instalment gets only the balance.  _([ATO, Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments))_
- **Whole-of-income cap** — $180,000 and not indexed. Reduce it by all other taxable payments the employee received in the income year, including salary and wages and a lump sum of unused leave, but not the tax-free redundancy amount and not the ETP itself. Add up the other taxable payments, subtract them from $180,000, compare the result with the ETP cap or its remaining balance, and apply the smaller. If the two are equal, use the whole-of-income cap.  _([ATO, Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments))_
- **A package with both codes** — Deal with the code R part first, because it reduces the ETP cap available to the code O part. In the ATO's own example a $397 redundancy excess is withheld at 32%, and the $17,678 gratuity is then tested against a whole-of-income cap of $40,000 and an ETP cap balance of $269,603.  _([ATO, Schedule 11, example 4](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments))_
- **When other income is large** — An employee with $200,000 of other taxable income has a whole-of-income cap of nil, so a golden handshake is withheld at 47% in full while the redundancy excess still gets the ETP cap.  _([ATO, Redundancy and early retirement](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/redundancy-and-early-retirement))_
- **Detail pages** — The ATO's cap pages walk through which cap applies and how to work out the whole-of-income cap with more than one payment in the year.  _([ATO, Applying the ETP caps](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/applying-the-etp-caps))_

## Section 7 - Withholding rates under Schedule 11 (from 1 July 2026)

**Table A summary**

| Payment | Age at the end of the income year | Amount | Rate |
| --- | --- | --- | --- |
| Life benefit, code R | Under preservation age | Up to the ETP cap | 32% |
| Life benefit, code R | Preservation age or over | Up to the ETP cap | 17% |
| Life benefit, code R | Any | Above the ETP cap | 47% |
| Life benefit, code O | Under preservation age | Up to the smaller cap | 32% |
| Life benefit, code O | Preservation age or over | Up to the smaller cap | 17% |
| Life benefit, code O | Any | Above the smaller cap | 47% |
| Death benefit to a non-dependant | Any | Up to the ETP cap, then above it | 32%, then 47% |
| Death benefit to a dependant | Any | Up to the ETP cap, then above it | Nil, then 47% |
| Death benefit to the trustee of the estate | Any | All | Nil |

- **Preservation age** — Test the employee's age at the end of the income year in which the payment is made, not at termination. Preservation age is 60 for anyone born after 30 June 1964, and everyone born earlier has already reached it.  _([ATO, Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments))_
- **No TFN** — Withhold 47% from a resident and 45% from a foreign resident who has not quoted a TFN, ignoring cents. A TFN declaration stays effective for 12 months after the last payment.  _([ATO, Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments))_
- **Foreign residents** — Check the tax treaty first. If the ETP is assessable only in the other country, do not withhold. If it is assessable in Australia, use Table A less the 2% Medicare levy.  _([ATO, Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments))_
- **Rounding** — Round to the nearest dollar, with 50 cents rounding up.  _([ATO, Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments))_
- **Death benefit dependants** — A dependant includes a spouse, a child under 18, a person in an interdependency relationship and anyone who was a dependant of the deceased just before death. Nothing is withheld from a payment to the trustee of the estate.  _([ATO, Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments))_

## Section 8 - Unused leave on termination under Schedule 7 (from 1 July 2026)

**Withholding on unused annual leave, leave loading and long service leave**

| Leave | Reason for termination | Accrual period | Withholding | Reported at |
| --- | --- | --- | --- | --- |
| Annual leave and loading | Genuine redundancy, invalidity or early retirement scheme | Any | 32% | Lump sum A |
| Annual leave and loading | Any other reason | Before 18 August 1993 | 32% | Lump sum A |
| Annual leave and loading | Any other reason | On or after 18 August 1993 | Marginal rates | Salary and wages |
| Long service leave | Any reason | Before 16 August 1978 | 5% of the amount, taxed at marginal rates | Lump sum B |
| Long service leave | Any reason | 16 August 1978 to 17 August 1993 | 32% | Lump sum A |
| Long service leave | Genuine redundancy, invalidity or early retirement scheme | After 17 August 1993 | 32% | Lump sum A |
| Long service leave | Any other reason | After 17 August 1993 | Marginal rates | Salary and wages |

- **Marginal rate method** — For post-17 August 1993 leave on a normal termination, Schedule 7 spreads the lump sum across the year: divide the payment by the number of normal pay periods in 12 months, add the result to a normal pay, work out the withholding on the combined amount, subtract the normal withholding and multiply the difference by the number of pay periods.  _([ATO, Schedule 7](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment))_
- **Leave is never an ETP** — Unused annual leave and long service leave sit outside the ETP caps, but a lump sum of leave counts as a taxable payment when the whole-of-income cap is reduced.  _([ATO, Accrued leave](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/accrued-leave))_
- **No study loan withholding** — Do not withhold for study and training support loans from lump sum termination payments.  _([ATO, Weekly tax table](https://www.ato.gov.au/tax-rates-and-codes/tax-table-weekly))_
- **Super guarantee** — Superannuation guarantee is payable on ordinary time earnings. A payment in lieu of notice is ordinary time earnings; unused annual leave and long service leave paid on termination, and ETPs, are not. See `au-super-guarantee.md`.  _([SGR 2009/2](https://www.ato.gov.au/law/view/document?DocID=SGR/SGR20092/NAT/ATO/00001))_

## Section 9 - Reporting

- **STP** — Report each ETP in the pay event with its code, the tax-free and taxable components, the tax withheld and the payment date. An employer that is exempt from or deferred on STP gives the employee a PAYG payment summary for the ETP within 14 days.  _([ATO, Schedule 11](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments))_
- **One package, several records** — A redundancy excess (code R) and a payment in lieu of notice (code O) from the same termination are two ETPs with two records, while the tax-free redundancy amount goes to lump sum D and the leave to lump sum A or to gross payments.  _([ATO, Schedule 11, example 4](https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments))_
- **Working holiday makers** — Use Schedule 15, not Schedule 11 or Schedule 7, for every payment to a working holiday maker, including the taxable component of an ETP and unused leave. See `au-working-holiday-makers.md`.  _([ATO, Schedule 15](https://www.ato.gov.au/tax-rates-and-codes/schedule-15-tax-table-for-working-holiday-makers))_
- **Corrections** — Fix an STP error at the next pay event, or with an update event after finalisation. A payment summary already given to the employee cannot be changed; follow the ATO's amendment process instead.  _([ATO, Redundancy and early retirement](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/redundancy-and-early-retirement))_

## Section 10 - Worked example

**Worked example facts**

| Item | Detail |
| --- | --- |
| Employee | Ana, aged 45, preservation age 60, Australian resident, TFN quoted |
| Service | Started 3 September 2018, dismissed on 30 October 2026 because her role was abolished, so 8 completed years |
| Salary and wages from 1 July to 30 October 2026 | $34,000 |
| Redundancy payment | $80,000, more than she would receive on resignation, at arm's length, with no arrangement to re-employ her |
| Payment in lieu of notice | $9,000 |
| Unused annual leave | $6,000, all accrued after 17 August 1993 |

**Facts.** All figures are synthetic and fall in the 2026-27 income year.

**Step 1, genuine redundancy test.** Ana is under age-pension age, the job no longer exists and the
employer made the decision. The $80,000 is a genuine redundancy payment.

**Step 2, tax-free limit.**

```
Base amount                                      13,598
Service amount 6,801 x 8 completed years         54,408
Tax-free limit                                   68,006
Genuine redundancy payment                       80,000
Tax-free, reported at lump sum D                 68,006
Excess, an ETP coded R                           11,994
```

**Step 3, the ETP coded R.** There is no tax-free component. Only the ETP cap of $270,000 applies,
and Ana is under preservation age.

```
Taxable component                                11,994
Withholding at 32%                                3,838
```

**Step 4, the payment in lieu of notice, an ETP coded O.**

```
Other taxable payments (salary 34,000 plus leave 6,000)    40,000
Whole-of-income cap: 180,000 less 40,000                  140,000
ETP cap balance: 270,000 less 11,994                      258,006
Smaller cap                                               140,000
Taxable component                                           9,000
Withholding at 32%                                          2,880
```

**Step 5, unused annual leave.** The termination is a genuine redundancy, so Schedule 7 applies 32%
whatever the accrual date.

```
Unused annual leave                               6,000
Withholding at 32%                                1,920
Reported at lump sum A
```

**Step 6, super.** Superannuation guarantee at 12% applies to the $9,000 payment in lieu of notice
($1,080) and to the salary, but not to the redundancy payment, the ETP or the unused leave.

**Step 7, reporting.** The income statement shows lump sum D of $68,006 and lump sum A of $6,000.
Two ETP records follow: code R with a taxable component of $11,994 and tax of $3,838, and code O
with a taxable component of $9,000 and tax of $2,880. Total withholding on the package is $8,638.

**What changes with age.** If Ana were 62 at 30 June 2027, both ETPs would be withheld at 17%
($2,039 and $1,530) and the leave would stay at 32%. If she were 67 on the day of dismissal, the
redundancy would not be genuine, the whole $80,000 would be an ETP coded O, and the whole-of-income
cap would apply to all of it.

## Section 11 - Common errors

- Treating a resignation, the end of a fixed-term contract or a dismissal at age-pension age as a genuine redundancy.
- Counting part years of service in the tax-free limit.
- Applying the whole-of-income cap to a code R payment, or forgetting to reduce it by salary and unused leave already paid in the year.
- Testing preservation age at the termination date rather than at the end of the income year.
- Withholding from the tax-free component or from the lump sum D amount.
- Reporting a redundancy excess and a golden handshake under one ETP code.
- Using Schedule 11 for unused leave, or marginal rates for leave paid on a genuine redundancy.
- Withholding study loan amounts from a lump sum termination payment.
- Treating a payment made more than 12 months after termination as an ETP without ATO approval.
- Paying super guarantee on unused leave or an ETP, or omitting it from a payment in lieu of notice.

## Section 12 - Self-checks

- [ ] Every component of the package is classified before any rate is applied.
- [ ] The genuine redundancy conditions, including age-pension age on the dismissal date, are documented.
- [ ] Completed years of service are counted from the start date to the dismissal date.
- [ ] The whole-of-income cap has been reduced by all other taxable payments in the year.
- [ ] The ETP cap balance reflects earlier payments for the same termination.
- [ ] Preservation age is tested at 30 June of the payment year.
- [ ] Each ETP has its own code and record, and lump sums A, B and D sit on the income statement.
- [ ] Schedule 7 rates match the reason for termination and the accrual dates.
- [ ] Foreign resident and no-TFN adjustments have been considered.
- [ ] Super guarantee is paid on the payment in lieu of notice and not on the leave or the ETP.

## Section 13 - Sources

- Income Tax Assessment Act 1997, Division 82 (employment termination payments) and Division 83 (unused leave, genuine redundancy and early retirement scheme payments), https://www.ato.gov.au/law/view/document?docid=PAC/19970038/82-130
- Taxation Administration Act 1953, Schedule 1, sections 12-85 and 12-90 (withholding from ETPs and unused leave payments).
- ATO, Schedule 11 tax table for employment termination payments (from 1 July 2026), https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-11-tax-table-for-employment-termination-payments
- ATO, Schedule 7 tax table for unused leave payments on termination of employment (from 1 July 2026), https://www.ato.gov.au/tax-rates-and-codes/payg-withholding-schedule-7-tax-table-for-unused-leave-payments-on-termination-of-employment
- ATO, Taxation of termination payments, https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments
- ATO, Payments that are ETPs, https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/payments-that-are-etps
- ATO, Tax-free component of ETPs, https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/tax-free-component-of-etps
- ATO, Redundancy and early retirement, https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/redundancy-and-early-retirement
- ATO, Accrued leave, https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/accrued-leave
- ATO, Applying the ETP caps, https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/applying-the-etp-caps
- ATO, Working out the whole-of-income cap amount, https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/working-out-the-whole-of-income-cap-amount
- ATO, The 12-month rule, https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/when-a-worker-leaves-your-business/taxation-of-termination-payments/the-12-month-rule
- ATO, TR 2009/2 Income tax: genuine redundancy payments, https://www.ato.gov.au/law/view/document?DocID=TXR/TR20092/NAT/ATO/00001
- ATO, SGR 2009/2 Superannuation guarantee: meaning of the terms ordinary time earnings and salary or wages, https://www.ato.gov.au/law/view/document?DocID=SGR/SGR20092/NAT/ATO/00001
- ATO, Schedule 15 tax table for working holiday makers, https://www.ato.gov.au/tax-rates-and-codes/schedule-15-tax-table-for-working-holiday-makers

Sources were checked on 27 September 2026.

> **Working paper only, not a lodged return.** Have a qualified Australian CPA or CA review this before paying or reporting a termination package. Genuine redundancy status and early retirement scheme approval turn on the facts of the dismissal.

> Contributed by Ryan Duguid.

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
