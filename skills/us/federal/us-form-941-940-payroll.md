---
name: us-form-941-940-payroll
description: Run 2026 US federal employer payroll tax compliance for businesses with W-2 employees. Form 941 (quarterly) line by line, Form 940 (annual FUTA) with Schedule A and the final 2026 California credit reduction of 1.5%, Forms W-2 and W-3 with the new 2026 box 12 codes TP, TT and TA and box 14b, the monthly or semiweekly deposit schedule under the lookback rule, the USD 100,000 next-day rule, Additional Medicare Tax withholding above USD 200,000, supplemental wage withholding at 22% and 37% over USD 1 million, the 2026 Form W-4 and the failure-to-deposit penalties. 2026 figures from IRS Pub. 15 (2026), including the Social Security wage base of USD 184,500, 6.2% and 1.45% each side, and FUTA at 6.0% on the first USD 7,000 with up to 5.4% state credit (0.6% net). Trigger on "Form 941", "Form 940", "FUTA", "payroll tax deposit", "semiweekly depositor", "lookback period", "W-2", "W-3", "Additional Medicare withholding", "Schedule B", "credit reduction state". Federal only.
version: "3.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# US federal employer payroll: Forms 941, 940, W-2 and W-3, tax year 2026

> **Source-cited draft.** Built from IRS Pub. 15 (2026), Pub. 15-T (2026), Form 941 (Rev. March 2026) and its instructions, the 2025 Instructions for Form 940 and Schedule A (Form 940), the 2026 General Instructions for Forms W-2 and W-3, the 2026 Form W-4, the 2026 Instructions for Form 8027, the IRS Voluntary Classification Settlement Program page and the U.S. Department of Labor's final 2026 FUTA credit reductions, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before any return is filed or deposit made.

**Answer first.** For 2026, Social Security tax is 6.2% from the employee and 6.2% from the employer on wages up to **USD 184,500** per employee per employer; Medicare tax is 1.45% each side with no cap; the employer withholds a further 0.9% Additional Medicare Tax from an employee's wages above **USD 200,000** in the calendar year (no employer match). FUTA is 6.0% on the first **USD 7,000** of each employee's wages, less a state credit of up to 5.4%, so 0.6% net, except in California, a credit reduction state for 2026 at 1.5% (2.1% net). A Form 941 filer is a monthly depositor for 2026 if its Form 941 line 12 totals for 1 July 2024 to 30 June 2025 were USD 50,000 or less, and a semiweekly depositor if more. A liability of USD 100,000 or more on any day is deposited the next business day. 2026 Forms W-2 go to employees and to the SSA by **1 February 2027**.

## Scope and who this is for

In scope: a US business (sole proprietor, partnership, LLC or corporation) with one or more common-law employees paid wages in 2026, for its federal employment taxes:

- Form 941, Employer's Quarterly Federal Tax Return: federal income tax withheld, Social Security and Medicare tax (both halves), Additional Medicare Tax withheld, current-quarter adjustments, and Schedule B for semiweekly depositors.
- Form 941-X corrections (outline only).
- Deposit schedule: the lookback rule, monthly or semiweekly, the USD 100,000 next-day rule, the USD 2,500 payment-with-return exception, electronic deposit.
- Form 940, Employer's Annual Federal Unemployment (FUTA) Tax Return, and Schedule A (Form 940) for credit reduction states.
- Forms W-2, W-3, W-2c and W-3c: the three wage boxes, box 12 codes including the 2026 codes, box 14a and 14b.
- Form W-4 (2026) administration and supplemental wage withholding.
- The failure-to-deposit, failure-to-file, failure-to-pay and trust fund recovery penalties.
- Routing only: Forms 944, 943 and 945, Form 8027, worker classification.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| State income tax withholding, state unemployment (SUTA) returns and rates, state disability and paid leave, local payroll taxes | `us-state-payroll-matrix` |
| New-hire reporting | `us-state-new-hire-reporting-matrix` |
| Independent contractors, Form 1099-NEC, the W-9, backup withholding and its rate | `us-1099-nec-issuance` |
| Worker classification analysis (common-law test) beyond the outline here | `us-1099-nec-issuance` |
| Wages paid to the owner's own children | `us-hiring-your-children-and-accountable-plans` |
| The owner's own self-employment tax (no Form 941 for a sole proprietor's own earnings) | `us-schedule-c-and-se-computation` |
| S corporation owner-employee salary level | `us-s-corp-election-decision` |
| The qualified small business payroll tax credit for research (election amount, Form 6765) | `us-r-and-d-section-174-and-41` |
| The employee's deductions for qualified tips and qualified overtime (amounts and phase-outs) | `us-federal-income-tax-return-1040` |
| Trust fund recovery penalty defence, collections, penalty appeals | `us-irs-collections-and-controversy` |
| Household employees (Schedule H), U.S. territories, nonresident alien withholding (chapter 3), Forms 1094-C and 1095-C, Form 5500, garnishments | Refer |

## Ask the client first

1. **Form 941 line 12 for each quarter from 1 July 2024 to 30 June 2025, as originally filed** (not as later corrected), and whether the business filed Form 944 in 2024 or 2025. This sets the 2026 deposit schedule.
2. **Did any single day's accumulated liability reach USD 100,000** in 2025 or 2026? That makes the employer semiweekly for the rest of that year and the next.
3. **Payroll register by pay date** (not by period worked): gross wages, tips reported, supplemental payments, federal income tax withheld, and each pre-tax deduction by type (401(k), Roth, section 125 health, dependent care, HSA).
4. **Is there a written section 125 cafeteria plan document?** Without one, the pre-tax health and HSA deductions are not excluded.
5. **Year-to-date wages per employee**, including any wages paid by a predecessor employer that sold the business to the client during 2026, and any change of payroll provider during the year.
6. **States where each employee works** and whether state unemployment tax was paid in full and on time. Any employee working in California?
7. **Tipped employees** (and their Treasury Tipped Occupation Code), employees paid FLSA overtime, and any employer contributions to a Trump account from 4 July 2026.
8. **Group-term life insurance over USD 50,000**, company cars, fringe benefits, third-party sick pay.
9. **Current Forms W-4** for every employee, including any claiming exemption, and the date each was received.
10. **EFTPS enrolment** and the deposit confirmations for every 2026 deposit.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Social Security tax rate, employee, and again employer | 6.2% | [IRS Pub. 15 (2026), What's New](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Social Security wage base, per employee per employer | USD 184,500 | [IRS Pub. 15 (2026), What's New](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Medicare tax rate, employee, and again employer; no wage base | 1.45% | [IRS Pub. 15 (2026), What's New](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Form 941 line 5a and 5b multiplier (both halves of Social Security) | 0.124 | [Form 941 (Rev. March 2026)](https://www.irs.gov/pub/irs-pdf/f941.pdf) |
| Form 941 line 5c multiplier (both halves of Medicare) | 0.029 | [Form 941 (Rev. March 2026)](https://www.irs.gov/pub/irs-pdf/f941.pdf) |
| Additional Medicare Tax withholding, employee only, line 5d multiplier | 0.009 (0.9%) | [Form 941 (Rev. March 2026)](https://www.irs.gov/pub/irs-pdf/f941.pdf) |
| Additional Medicare Tax: employer withholds on wages in excess of | USD 200,000 in the calendar year | [Instructions for Form 941 (Rev. March 2026), line 5d](https://www.irs.gov/pub/irs-pdf/i941.pdf) |
| Additional Medicare Tax owed by the employee, married filing jointly, above | USD 250,000 | [26 U.S.C. 1401(b)(2)(A)(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1401.htm) |
| Additional Medicare Tax owed by the employee, married filing separately, above | USD 125,000 | [IRS Additional Medicare Tax questions and answers](https://www.irs.gov/businesses/small-businesses-self-employed/questions-and-answers-for-the-additional-medicare-tax) |
| Supplemental wage withholding, optional flat rate | 22% | [IRS Pub. 15 (2026), What's New and section 7](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Supplemental wage withholding, mandatory on supplemental wages above USD 1 million in the year | 37% | [IRS Pub. 15 (2026), section 7](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| FUTA tax rate | 6.0% | [IRS Pub. 15 (2026), section 14](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| FUTA wage base, per employee | USD 7,000 | [IRS Pub. 15 (2026), section 14](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Maximum credit for state unemployment tax | 5.4% | [IRS Pub. 15 (2026), section 14](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| FUTA rate after the maximum credit | 0.6% | [IRS Pub. 15 (2026), section 14](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| FUTA credit reduction, California, 2026 (final) | 1.5% (0.015) | [U.S. DOL, Final 2026 FUTA Credit Reductions](https://oui.doleta.gov/unemploy/docs/final_credit_states_2026.xlsx) |
| FUTA credit reduction, U.S. Virgin Islands, 2026 (final; advances repaid) | 0 | [U.S. DOL, Final 2026 FUTA Credit Reductions](https://oui.doleta.gov/unemploy/docs/final_credit_states_2026.xlsx) |
| FUTA deposit required when the quarter's liability (with carry-forward) is over | USD 500 | [IRS Pub. 15 (2026), section 14](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| FUTA general test: wages in any calendar quarter of 2025 or 2026 of | USD 1,500 or more | [IRS Pub. 15 (2026), section 14](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| FUTA general test, alternative: an employee on some part of a day in | 20 or more different weeks of 2025 or of 2026 | [IRS Pub. 15 (2026), section 14](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Lookback period for 2026 deposits, Form 941 filer | 1 July 2024 to 30 June 2025 | [IRS Pub. 15 (2026), section 11, Table 1](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Monthly depositor if lookback taxes were | USD 50,000 or less (semiweekly if more) | [IRS Pub. 15 (2026), section 11](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Next-day deposit rule: accumulated liability on any day of | USD 100,000 or more | [IRS Pub. 15 (2026), section 11](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Payment with Form 941 allowed if line 12 for the current or prior quarter is less than | USD 2,500 | [IRS Pub. 15 (2026), section 11](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Form 944 for employers expecting a year's employment taxes of | USD 1,000 or less (IRS written notice required) | [IRS Pub. 15 (2026), Reminders](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Tips reported in a month of this amount or more are subject to withholding and FICA | USD 20 | [IRS Pub. 15 (2026), What's New and section 6](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Form W-2 needed even with no tax withheld once wages reach (new for wages paid after 2025) | USD 2,000 | [General Instructions for Forms W-2 and W-3 (2026), What's New](https://www.irs.gov/pub/irs-pdf/iw2w3.pdf) |
| Electronic filing of Forms W-2 required if the employer files in total at least | 10 information returns | [General Instructions for Forms W-2 and W-3 (2026)](https://www.irs.gov/pub/irs-pdf/iw2w3.pdf) |
| Employer contribution to an employee's Trump account, excluded, from 4 July 2026, up to | USD 2,500 a year (box 12 code TA) | [General Instructions for Forms W-2 and W-3 (2026), What's New](https://www.irs.gov/pub/irs-pdf/iw2w3.pdf) |
| Form W-4 (2026) Step 3: per qualifying child under 17 | USD 2,200 | [Form W-4 (2026)](https://www.irs.gov/pub/irs-pdf/fw4.pdf) |
| Form W-4 (2026) Step 3: per other dependent | USD 500 | [Form W-4 (2026)](https://www.irs.gov/pub/irs-pdf/fw4.pdf) |
| Household workers: FICA applies to cash wages in 2026 of (routing only) | USD 3,000 or more | [IRS Pub. 15 (2026), What's New](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Election workers: FICA applies to pay in 2026 of (routing only) | USD 2,500 or more | [IRS Pub. 15 (2026), What's New](https://www.irs.gov/pub/irs-pdf/p15.pdf) |

The Social Security and Medicare rates, the 0.9% and its USD 200,000 withholding trigger, the 22% and 37% supplemental rates and all the FUTA figures are unchanged from 2025. The wage base rose from USD 176,100 (2025) to USD 184,500. The 22%, 37% and the 24% backup rate are now permanent because Public Law 119-21 (the One Big Beautiful Bill Act) made the 2017 individual rates permanent (Pub. 15 (2026), What's New).

### Step 1: decide the 2026 deposit schedule (the lookback rule)

1. **Lookback period.** For a Form 941 filer, 2026 deposits are set by the four quarters from 1 July 2024 to 30 June 2025. A 2026 Form 941 filer that filed Form 944 in 2024 or 2025 uses calendar year 2024. A Form 943, 944 or 945 filer uses the second preceding calendar year (2024). Source: [Pub. 15 (2026), section 11, Table 1](https://www.irs.gov/pub/irs-pdf/p15.pdf).
2. **Add Form 941 line 12 for the four quarters as originally reported.** Adjustments on Form 941-X do not change the lookback amount (Pub. 15's own example: USD 45,000 originally reported, later corrected upward by USD 10,000, is still a monthly depositor).
3. **USD 50,000 or less: monthly.** Deposit the taxes for wages paid in a month by the 15th of the next month.
4. **More than USD 50,000: semiweekly.** Taxes for paydays on Wednesday, Thursday or Friday are due the following Wednesday; for Saturday, Sunday, Monday or Tuesday, the following Friday. Attach Schedule B (Form 941) to every Form 941. If a semiweekly period spans two quarters, make two deposits (Pub. 15's example: a Wednesday 30 September 2026 payday and a Friday 2 October 2026 payday need separate deposits, both due Wednesday 7 October 2026).
5. **New employers** are monthly in their first calendar year (Form 941) or first two years (Forms 943, 944, 945), because lookback quarters before the business started count as zero, subject to the next-day rule.
6. **Liability arises when wages are paid** (pay date, cash basis), not when they are earned or accrued.
7. **Next-day rule.** If accumulated taxes reach USD 100,000 on any day in a deposit period, deposit by the next business day. The test is made before nonrefundable credits. Accumulation stops at the end of each deposit period and starts again the day after a next-day deposit. A monthly depositor that hits USD 100,000 becomes semiweekly from the next day for the rest of 2026 and all of 2027. The USD 100,000 counts all of federal income tax withheld plus both halves of Social Security and Medicare.
8. **Business days.** A deposit due on a Saturday, Sunday or legal holiday moves to the next business day. A semiweekly depositor always has at least 3 business days after the end of the semiweekly period. A statewide holiday does not delay a deposit.
9. **USD 2,500 exception.** If Form 941 line 12 for the current quarter or the prior quarter is less than USD 2,500 and no next-day obligation arose this quarter, the tax may be paid with a timely filed return. If unsure the quarter will stay under USD 2,500, deposit on schedule. A monthly depositor may also pay a shortfall with the return under the accuracy of deposits rule.
10. **How to deposit.** All deposits are by electronic funds transfer (EFTPS or a same-day wire through the bank). Through EFTPS a deposit must be submitted by 8:00 p.m. Eastern time the day before it is due. Keep the EFT acknowledgement numbers. Source: [Pub. 15 (2026), section 11](https://www.irs.gov/pub/irs-pdf/p15.pdf).

### Step 2: compute each pay date's liability

For each employee and each pay date:

1. **Federal income tax withholding** from the employee's Form W-4 and the Pub. 15-T (2026) tables (percentage method or wage bracket method). The 2026 tables reflect Public Law 119-21. A pre-2020 Form W-4 still on file stays valid. With no Form W-4, withhold as Single or Married filing separately with no entries in Steps 2 to 4. A replacement Form W-4 takes effect no later than the first payroll period ending on or after the 30th day after it is received. Source: [Pub. 15-T (2026)](https://www.irs.gov/pub/irs-pdf/p15t.pdf); [Pub. 15 (2026), section 9](https://www.irs.gov/pub/irs-pdf/p15.pdf).
2. **Supplemental wages** (bonuses, commissions, severance, back pay, awards; overtime and tips may be treated as regular or supplemental). If paid separately and income tax was withheld from regular wages, the employer may use 22% flat. Once supplemental wages to one employee in 2026 pass USD 1 million (all businesses under common control counted), the excess is withheld at 37% regardless of the Form W-4. Source: [Pub. 15 (2026), section 7](https://www.irs.gov/pub/irs-pdf/p15.pdf).
3. **Social Security:** 6.2% of wages up to the employee's cumulative USD 184,500 for this employer. Stop at the pay date that crosses it; withhold only on the part that brings the total to USD 184,500.
4. **Medicare:** 1.45% of all Medicare wages.
5. **Additional Medicare Tax:** start in the pay period in which this employer's wages to the employee pass USD 200,000; withhold 0.9% on the excess and on all later wages that year. Filing status and other jobs are ignored. There is no employer share.
6. **Employer share:** 6.2% (to the wage base) and 1.45%, the same base as the employee's.
7. **Pay-date liability** = income tax withheld + employee and employer Social Security + employee and employer Medicare + Additional Medicare withheld. This is what the deposit schedule and the USD 100,000 test use.

What is in and out of each wage base:

| Item | Box 1 (income tax) | Box 3 (Social Security) | Box 5 (Medicare) | FUTA |
| --- | --- | --- | --- | --- |
| Traditional 401(k), 403(b), governmental 457(b) elective deferral | Out | In | In | In |
| Roth 401(k), 403(b) or 457(b) deferral | In | In | In | In |
| Section 125 health premium (written plan) | Out | Out | Out | Out |
| Dependent care assistance under section 125 (within the limit; box 10) | Out | Out | Out | Out |
| HSA contribution through a section 125 salary reduction | Out | Out | Out | Out |
| Employer HSA contribution reasonably believed excludable | Out | Out | Out | Out |
| Employee's own after-tax HSA contribution (deducted on Form 8889) | In | In | In | In |
| Group-term life insurance, cost of the first USD 50,000 | Out | Out | Out | Out |
| Group-term life insurance cost above USD 50,000 (box 12 code C) | In | In | In | Out |
| Adoption assistance (within the limit; box 12 code T) | Out | In | In | Not covered here: check Pub. 15-B |
| Qualified transportation fringe (within the limit) | Out | Out | Out | Out |
| Qualified tips (code TP) and qualified overtime premium (code TT) | In | In | In | In |
| Nonqualified deferred compensation (section 3121(v)(2)) | When paid | When vested | When vested | When vested |

Sources: [Pub. 15 (2026), sections 5 and 15](https://www.irs.gov/pub/irs-pdf/p15.pdf); [General Instructions for Forms W-2 and W-3 (2026)](https://www.irs.gov/pub/irs-pdf/iw2w3.pdf). Tips and overtime stay fully subject to income tax withholding and to both halves of FICA; the employee's deduction for them is taken on Form 1040, and the employee may reduce withholding through Form W-4 (2026) Step 4(b).

### Step 3: Form 941, line by line (Rev. March 2026)

The March 2026 revision is used for all four quarters of 2026 unless the IRS revises it again.

| Line | What goes there |
| --- | --- |
| 1 | Employees paid for the pay period including 12 March (Q1), 12 June (Q2), 12 September (Q3) or 12 December (Q4). A snapshot, not a total |
| 2 | Wages, tips and other compensation (income tax wages, box 1 basis) |
| 3 | Federal income tax withheld |
| 4 | Check only if no wages are subject to Social Security or Medicare tax |
| 5a | Taxable Social Security wages (column 1) x 0.124 (column 2), capped per employee at USD 184,500 for the year |
| 5b | Taxable Social Security tips x 0.124 |
| 5c | Taxable Medicare wages and tips x 0.029, no cap |
| 5d | Wages and tips subject to Additional Medicare Tax withholding (column 1: the wages above USD 200,000) x 0.009. Once wages pass USD 200,000, include all reported tips even if the 0.9% could not be withheld |
| 5e | Total of column 2 on lines 5a to 5d |
| 5f | Section 3121(q) Notice and Demand tax on unreported tips (only after an IRS notice) |
| 6 | Lines 3 + 5e + 5f |
| 7 | Fractions of cents adjustment |
| 8 | Sick pay adjustment (third-party sick pay) |
| 9 | Tips and group-term life insurance adjustments: the employee share of Social Security and Medicare on uncollected tips and on group-term life for former employees, entered as a negative |
| 10 | Lines 6 to 9 combined |
| 11 | Qualified small business payroll tax credit for research (attach Form 8974). Used first against the employer share of Social Security tax up to USD 250,000 per quarter, then the employer share of Medicare tax; any rest carries to the next quarter. The election amount is in `us-r-and-d-section-174-and-41` |
| 12 | Line 10 minus line 11: total taxes. This is the lookback figure |
| 13 | Deposits for the quarter, including an overpayment applied from the prior quarter |
| 14 | Balance due (line 12 more than line 13); pay electronically |
| 15 | Overpayment: apply to the next return, or refund (now paid by direct deposit) |
| 16 | Under USD 2,500 (current or prior quarter) and no next-day obligation: check the first box. Monthly depositor: enter the liability for each month. Semiweekly depositor: check the third box and attach Schedule B |

Part 3 marks a closed business or a seasonal employer; Part 4 names a third-party designee; Part 5 is the signature. Third-party aggregate filers (section 3504 agents, CPEOs) now complete the Aggregate Return Filers Only section and Schedule R; that is outside this skill. Source: [Form 941 (Rev. March 2026)](https://www.irs.gov/pub/irs-pdf/f941.pdf); [Instructions for Form 941 (Rev. March 2026)](https://www.irs.gov/pub/irs-pdf/i941.pdf). The 2026 form has no lines for the COVID-19 sick and family leave credits; those are claimed on Form 941-X.

**Schedule B (Form 941)** reports the tax liability for each day wages were paid (the liability date, not the deposit date), month by month. Its total must equal line 12. The IRS compares it with EFTPS deposit dates to assess deposit penalties.

**Form 941-X** is filed separately, never attached to the next Form 941. Two routes: the adjusted return process (interest-free for an underreported amount if filed by the due date of the return for the quarter in which the error was found), or the claim for refund process, which for overcollected employee tax needs each employee's written consent or proof of repayment to the employee. Typical causes: a bonus never run through payroll, a worker reclassified from contractor to employee, the wage base crossed earlier than the system tracked, a missed fringe benefit (also needs a Form W-2c).

### Step 4: Form 940 and FUTA

1. **Who owes FUTA (general test):** USD 1,500 or more of wages in any calendar quarter of 2025 or 2026, or at least one employee on some part of a day in 20 or more different weeks of 2025 or of 2026. Household employers (USD 1,000 in a quarter) report on Schedule H, not here. Farm employers: USD 20,000 cash wages in a quarter, or 10 or more farmworkers in 20 or more weeks. Only the employer pays FUTA. Source: [Pub. 15 (2026), section 14](https://www.irs.gov/pub/irs-pdf/p15.pdf).
2. **FUTA wages:** the first USD 7,000 paid to each employee in 2026. A successor employer that acquired the business may count the predecessor's wages toward the USD 7,000.
3. **Tax:** 6.0% of FUTA wages, less the credit for state unemployment tax of up to 5.4%. Full credit needs state tax paid in full, on time and on the same wages. Where a state's base excludes wages that FUTA taxes (for example some corporate officer wages), more than 0.6% is owed on those wages.
4. **Credit reduction (Schedule A, Form 940).** For 2026 the Department of Labor's final list (updated 10 November 2026) names only California, at 1.5%: California had an outstanding advance on every 1 January from 2021 to 2026, did not repay before 10 November 2026, and was granted a waiver of the further benefit cost rate add-on. The U.S. Virgin Islands repaid its advances before 10 November 2026, so has no 2026 reduction. FUTA wages paid in California cost 0.6% + 1.5% = 2.1%, which is USD 147 per employee at the USD 7,000 base. Source: [DOL final 2026 credit reductions](https://oui.doleta.gov/unemploy/docs/final_credit_states_2026.xlsx).
5. **Quarterly deposits.** Each quarter, multiply that quarter's FUTA wages by 0.6%. If the total with any amount carried forward is over USD 500, deposit by the last day of the month after the quarter: 30 April, 31 July, 31 October (2 November 2026, as 31 October is a Saturday) and 31 January (1 February 2027). If USD 500 or less, carry it forward. A fourth-quarter amount of USD 500 or less may be paid with Form 940. **The credit reduction is a fourth-quarter liability:** it is included with the fourth-quarter deposit (it may be deposited earlier but is not due earlier). Source: [Pub. 15 (2026), section 14, Table 4](https://www.irs.gov/pub/irs-pdf/p15.pdf).
6. **Multi-state employers** file one Form 940 with Schedule A. The USD 7,000 is one cap per employee per employer across states; Schedule A follows the wages that were subject to each state's unemployment tax law (Instructions for Form 940, line 1b and line 2).
7. **Corrections:** there is no Form 940-X; file a Form 940 marked "Amended" (it can be e-filed).

### Step 5: Forms W-2 and W-3 (2026)

1. **Who gets a W-2:** every employee from whom income tax, Social Security or Medicare tax was withheld (or would have been, but for an exemption claim). New for wages paid after 2025: an employee with no tax withheld needs a W-2 once wages reach USD 2,000 (was USD 600), indexed after 2026.
2. **Box 1, 3 and 5** follow the table in Step 2. Box 3 is never more than USD 184,500. Box 4 is the employee's 6.2% only; box 6 is the employee's 1.45% plus any Additional Medicare Tax withheld.
3. **Box 12 codes.** A, B (uncollected tax on tips); C (group-term life over USD 50,000); D, E, F, G, H, S (elective deferrals: 401(k), 403(b), SARSEP, 457(b), 501(c)(18)(D), SIMPLE); AA, BB, EE (Roth 401(k), 403(b), 457(b)); J (nontaxable sick pay); K (golden parachute excise); L (substantiated business expense reimbursements); M, N (uncollected tax on group-term life for former employees); P (excludable moving reimbursements, now only for active-duty Armed Forces members moving on orders, and from 2026 also intelligence community employees and appointees moving on a change in assignment); Q (nontaxable combat pay); R (Archer MSA); T (adoption benefits); V (nonstatutory stock option income); W (employer HSA contributions, including section 125 salary reductions); Y, Z (section 409A); DD (cost of employer health coverage); FF (QSEHRA); GG, HH (section 83(i)); II (Medicaid waiver payments). **New for 2026:** TA (employer contributions to a Trump account under a section 128 programme), TP (total cash tips reported to the employer), TT (total qualified overtime compensation: only the premium part, such as the "half" of time-and-a-half, paid under FLSA section 7). Paper and online-created forms hold four box 12 amounts per W-2; an uploaded electronic file can hold every code. Source: [General Instructions for Forms W-2 and W-3 (2026)](https://www.irs.gov/pub/irs-pdf/iw2w3.pdf).
4. **Box 14** is split for 2026: box 14a "Other" (what box 14 used to hold: state disability withholding, union dues, after-tax health premiums, vehicle fringe details) and box 14b, the Treasury Tipped Occupation Code(s), required when code TP is used. The 2025 transition relief of Notice 2025-62 covered tax year 2025 only.
5. **Boxes 15 to 20** carry state and local wages and tax; add rows (or a second W-2) for more states. State rules are in `us-state-payroll-matrix`.
6. **Due date:** 2026 Forms W-2 to employees, and Forms W-2 and W-3 to the SSA (paper or electronic), by **1 February 2027**. One 30-day extension for the SSA filing may be requested on Form 8809, and it is not automatic.
7. **Electronic filing:** required if the employer files at least 10 information returns in total (Forms W-2, 1099 and others counted together); a waiver may be requested on Form 8508 at least 45 days before the due date. A W-2c corrects on the same medium as the original. Business Services Online builds the W-3 automatically for e-filed W-2s.
8. **Penalties for Forms W-2 due after 31 December 2026:** USD 60 per form if correctly filed within 30 days of the due date, USD 130 if by 1 August, USD 340 after that or not at all, with annual maximums (lower for small businesses). Source: [General Instructions for Forms W-2 and W-3 (2026), Penalties](https://www.irs.gov/pub/irs-pdf/iw2w3.pdf).
9. **Form W-2c and W-3c** correct an issued W-2 (wrong SSN or name, wrong amounts, missed fringe benefit, misallocated state wages). If FICA changes, file Form 941-X for the quarter; if FUTA changes, an amended Form 940.

**Reconcile the year before filing.** The SSA compares the W-3 with the four Forms 941 and sends a discrepancy notice when they differ.

| W-3 box | Should equal, from the four Forms 941 |
| --- | --- |
| 1 | Sum of line 2 |
| 2 | Sum of line 3 |
| 3 (plus box 7 tips) | Sum of line 5a column 1 (plus 5b column 1) |
| 4 | Half of the sum of line 5a column 2 (plus 5b), the employee share |
| 5 | Sum of line 5c column 1 |
| 6 | Half of the sum of line 5c column 2, plus the sum of line 5d column 2 |

Common causes of a difference: a 31 December payroll with a January check date (wages belong to the pay-date year), third-party sick pay, group-term life for former employees (line 9 adjustment), section 3121(v)(2) deferred compensation counted for FICA in the vesting year.

### Step 6: Form W-4 (2026)

- Five steps: (1) personal information and filing status; (2) multiple jobs or a working spouse; (3) dependents: USD 2,200 per qualifying child under 17 and USD 500 per other dependent; (4) other income (4a), deductions (4b, whose worksheet now includes estimated qualified tips, qualified overtime and car loan interest) and extra withholding (4c); (5) signature. Source: [Form W-4 (2026)](https://www.irs.gov/pub/irs-pdf/fw4.pdf).
- Exemption from withholding is now a checkbox below Step 4(c) (previously written in). It is valid only if the employee had no income tax liability last year and expects none this year, and it lasts one year: a 2026 exemption needs a new Form W-4 by 16 February 2027. Forms W-4 claiming exemption for the previous year expire on 16 February; then withhold as Single or Married filing separately with no adjustments, and do not refund tax withheld while no exemption was in place. Source: [Pub. 15 (2026), Calendar](https://www.irs.gov/pub/irs-pdf/p15.pdf).
- Do not accept a fixed dollar or percentage instruction instead of a Form W-4; an employee may only add extra withholding in Step 4(c).

### Step 7: penalties

Failure to deposit (section 6656), measured in calendar days from the due date:

| Late | Penalty on the amount | Source |
| --- | --- | --- |
| 1 to 5 days | 2% | [Pub. 15 (2026), section 11](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| 6 to 15 days | 5% | [Pub. 15 (2026), section 11](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| 16 or more days, or paid directly to the IRS or with the return instead of deposited (outside the exceptions) | 10% | [Pub. 15 (2026), section 11](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Still unpaid more than 10 days after the first IRS notice, or the day notice and demand for immediate payment is received, whichever is earlier | 15% | [Pub. 15 (2026), section 11](https://www.irs.gov/pub/irs-pdf/p15.pdf) |

The penalty is figured deposit by deposit, not on the quarter's net shortfall, so one quarter can carry a 10% and a 2% penalty on different deposits; a late deposit is generally applied to the most recent liability first. Penalties do not apply with reasonable cause and no willful neglect. The IRS may also waive the penalty for an inadvertent failure in the first quarter a deposit was required, or the first deposit after the deposit frequency changed, if the return was timely and the employer meets the section 7430 net worth and size limits (businesses: net worth up to USD 7 million and up to 500 employees; individuals: net worth up to USD 2 million).

Other penalties:

- **Late Form 941 or 940:** 5% of the unpaid tax per month or part month, up to 25%. **Late payment:** 0.5% per month, up to 25%. When both apply in a month, the filing penalty is reduced by the payment penalty.
- **Trust fund recovery penalty (section 6672):** 100% of the unpaid income tax withheld and employee Social Security and Medicare, assessable personally against every person responsible for collecting, accounting for or paying it who acted willfully: officers, signatories, sometimes bookkeepers. Defence and appeals: `us-irs-collections-and-controversy`.
- **First-time abatement** may relieve the failure-to-deposit, failure-to-file and failure-to-pay penalties for an employer with a clean three-year history; request it after the notice.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Lookback taxes exactly USD 50,000 | Monthly depositor (the test is "more than USD 50,000" for semiweekly) |
| Form 941-X filed in 2026 for a lookback quarter | Ignored for the lookback; the original line 12 counts |
| First year of business, Form 941 filer | Monthly, unless the USD 100,000 next-day rule is hit |
| Monthly depositor accumulates USD 100,000 on a day | Deposit next business day; semiweekly from the next day for the rest of 2026 and all of 2027 |
| Liability of USD 95,000 on Tuesday and USD 10,000 on Wednesday (semiweekly) | Two deposit periods: no next-day deposit; USD 95,000 by Friday, USD 10,000 by the next Wednesday |
| Employee works for two unrelated employers | Each employer withholds 6.2% up to USD 184,500; the employee claims the excess on Form 1040; employers get no refund of their share |
| Related employers with a common paymaster (section 3121(s)) | One wage base for the group if the common paymaster rules are met |
| Business bought mid-year (successor employer) | Successor may count the predecessor's wages toward USD 184,500 and USD 7,000; new Forms W-4 unless the alternative procedure in Rev. Proc. 2004-53 is used |
| Employee's wages pass USD 200,000 with this employer | Withhold 0.9% from that pay period; no employer share; the employee reconciles on Form 8959 |
| Married employee, joint income under USD 250,000, but over USD 200,000 at one job | Employer still withholds; the employee recovers it through Form 8959 |
| Two jobs of USD 150,000 each, single | Neither employer withholds the 0.9%; the employee owes 0.9% on USD 100,000 on Form 8959 |
| HSA or health premiums deducted pre-tax with no written section 125 plan | Not excluded: include in boxes 1, 3 and 5 and correct with Forms W-2c and 941-X |
| Group-term life over USD 50,000, active employee | Imputed cost in boxes 1, 3, 5 and code C; FICA must be withheld; income tax withholding optional; not FUTA wages |
| Group-term life over USD 50,000, former employee | Employee share of FICA uncollected: codes M and N; negative adjustment on Form 941 line 9 |
| Large food or beverage establishment (more than 10 employees on a typical business day in the prior year, tipping customary) | Form 8027; if reported tips are under 8% of gross receipts, allocate the difference (W-2 box 8); no withholding on allocated tips |
| IRS section 3121(q) notice for unreported tips | Employer share on Form 941 line 5f |
| Back pay or a correction paid later | Wages of the period and year paid, not earned; Form 941-X only to correct an amount already reported |
| Total quarterly liability under USD 2,500 | May pay with the return, if the prior or current quarter test is met and no next-day obligation arose |
| Employer filing Form 944 (notified by the IRS) | Annual return due 31 January; to switch between Forms 944 and 941, contact the IRS in the first calendar quarter |
| Farm workers | Form 943; FICA applies to a worker paid USD 150 or more in cash, or if total farm wages are USD 2,500 or more |
| Nonpayroll withholding (pensions, gambling, backup withholding) | Form 945, deposited separately from Form 941 taxes |
| Worker classification in doubt | Common-law test under section 3121(d); section 530 relief or the Voluntary Classification Settlement Program (Form 8952: pay 10% of the employment tax for the most recent year at the reduced section 3509(a) rates). Analysis in `us-1099-nec-issuance` |

## Worked cases

**Case 1, a decision: monthly or semiweekly depositor for 2026?** Harbor Supply LLC files Form 941. As originally filed, line 12 was USD 11,800 for Q3 2024, USD 12,600 for Q4 2024, USD 13,100 for Q1 2025 and USD 13,400 for Q2 2025. In January 2026 its bookkeeper filed a Form 941-X reducing Q4 2024 by USD 1,500, and proposes to treat the company as a monthly depositor because the corrected total is USD 49,400.

The lookback total uses the amounts originally reported: USD 50,900, which is more than USD 50,000, so Harbor Supply is a **semiweekly depositor for all of 2026** and must attach Schedule B to each Form 941. The Form 941-X does not change this (Pub. 15 (2026), section 11, "Adjustments and the lookback rule"). On Friday 6 March 2026 it pays wages of USD 21,000 (all under the wage bases) and withholds USD 2,730 of income tax. FICA on both sides is USD 21,000 x 15.3% = USD 3,213, so the pay-date liability is USD 5,943, due by **Wednesday 11 March 2026**. Under the bookkeeper's monthly reading it would have gone in on 15 April 2026, 35 days late: a 10% failure-to-deposit penalty of USD 594.30 on this one deposit. Recommend: semiweekly schedule, Schedule B, and set the payroll system to deposit on the Wednesday and Friday cycle.

```oa-check
name: Lookback rule, monthly or semiweekly for 2026, and one Friday deposit
inputs:
  q3_2024: 11800
  q4_2024: 12600
  q1_2025: 13100
  q2_2025: 13400
  form_941x_change: -1500
  wages: 21000
  income_tax_withheld: 2730
steps:
  - lookback_total: q3_2024 + q4_2024 + q1_2025 + q2_2025
  - corrected_total_not_used: lookback_total + form_941x_change
  - semiweekly: clamp(ceil((lookback_total - 50000) / 1000000), 0, 1)
  - fica_both_halves: wages * 0.153
  - deposit: income_tax_withheld + fica_both_halves
  - penalty_if_paid_monthly: deposit * 0.10
expected:
  lookback_total: 50900.00
  corrected_total_not_used: 49400.00
  semiweekly: 1
  fica_both_halves: 3213.00
  deposit: 5943.00
  penalty_if_paid_monthly: 594.30
```

**Case 2, an executive crossing the wage base and the Additional Medicare trigger.** Northwind Analytics Inc. pays its CEO USD 25,000 on the last day of each month in 2026 (USD 300,000 for the year, no pre-tax deductions).

- **Social Security:** cumulative wages are USD 175,000 after July. August's USD 25,000 is taxed only on USD 9,500 (to reach USD 184,500): employee tax USD 589 that month, then nothing for September to December. Box 3 is USD 184,500 and box 4 is USD 11,439.
- **Additional Medicare:** cumulative wages reach exactly USD 200,000 at the end of August (not "in excess of"). From the September payroll, 0.9% is withheld on every dollar: USD 225 a month, USD 900 for the year on USD 100,000.
- **Box 5** is USD 300,000; **box 6** is USD 4,350 (1.45%) + USD 900 = USD 5,250.
- **Q3 Form 941, this employee only:** line 5a column 1 USD 34,500 (July 25,000 + August 9,500) x 0.124 = USD 4,278; line 5c column 1 USD 75,000 x 0.029 = USD 2,175; line 5d column 1 USD 25,000 x 0.009 = USD 225.

Common errors: box 3 at USD 300,000 (no cap), or at USD 200,000 (confusing the wage base with the Additional Medicare trigger), or using the 2025 base of USD 176,100.

```oa-check
name: Wage base crossover and Additional Medicare withholding, USD 300,000 salary (2026)
inputs:
  annual_wages: 300000
  wages_through_july: 175000
  wage_base: 184500
  addl_trigger: 200000
  q3_medicare_wages: 75000
  september_wages: 25000
steps:
  - august_ss_wages: wage_base - wages_through_july
  - august_employee_ss: august_ss_wages * 0.062
  - box_3: min(annual_wages, wage_base)
  - box_4: box_3 * 0.062
  - additional_medicare: max(annual_wages - addl_trigger, 0) * 0.009
  - box_6: annual_wages * 0.0145 + additional_medicare
  - q3_line_5a_wages: 25000 + august_ss_wages
  - q3_line_5a_tax: q3_line_5a_wages * 0.124
  - q3_line_5c_tax: q3_medicare_wages * 0.029
  - q3_line_5d_tax: september_wages * 0.009
expected:
  august_ss_wages: 9500.00
  august_employee_ss: 589.00
  box_3: 184500.00
  box_4: 11439.00
  additional_medicare: 900.00
  box_6: 5250.00
  q3_line_5a_wages: 34500.00
  q3_line_5a_tax: 4278.00
  q3_line_5c_tax: 2175.00
  q3_line_5d_tax: 225.00
```

**Case 3, FUTA in California, the 2026 credit reduction state.** Pacific Grove Cafe LLC pays wages only in California and pays its state unemployment tax in full and on time. Its 12 employees each earn more than USD 7,000 in 2026, half of the FUTA wages in Q1 and half in Q2.

FUTA wages: 12 x USD 7,000 = USD 84,000. Gross FUTA at 6.0% is USD 5,040; the 5.4% credit is USD 4,536; net at 0.6% is USD 504. Schedule A: USD 84,000 x 0.015 = USD 1,260 of credit reduction. Total 2026 FUTA: USD 1,764, which is USD 147 per employee. Deposits: Q1 USD 252 (USD 500 or less, carry forward); Q2 cumulative USD 504 (over USD 500), deposit by **31 July 2026**; Q3 nil; the USD 1,260 credit reduction is a fourth-quarter liability, over USD 500, so it is deposited by **1 February 2027** (31 January 2027 is a Sunday). Form 940 with Schedule A is due 1 February 2027, or 10 February 2027 if every FUTA deposit was made on time.

```oa-check
name: Form 940 with the 2026 California credit reduction, 12 employees
inputs:
  employees: 12
  futa_base: 7000
  ca_reduction: 0.015
steps:
  - futa_wages: employees * futa_base
  - gross_futa: futa_wages * 0.06
  - state_credit: futa_wages * 0.054
  - net_futa: gross_futa - state_credit
  - credit_reduction: futa_wages * ca_reduction
  - total_futa: net_futa + credit_reduction
  - per_employee: total_futa / employees
  - q1_liability: futa_wages / 2 * 0.006
expected:
  futa_wages: 84000.00
  gross_futa: 5040.00
  state_credit: 4536.00
  net_futa: 504.00
  credit_reduction: 1260.00
  total_futa: 1764.00
  per_employee: 147.00
  q1_liability: 252.00
```

**Case 4, a small employer's Q2 2026 Form 941.** Acme Coffee Roasters LLC (three employees, monthly depositor) paid Q2 2026 gross wages of USD 46,200, with USD 2,200 of traditional 401(k) deferrals, USD 2,000 of section 125 health premiums under a written plan, and USD 5,960 of income tax withheld. Nobody is near the wage base. Line 2: USD 46,200 - 2,200 - 2,000 = USD 42,000. Lines 5a and 5c column 1: USD 46,200 - 2,000 = USD 44,200 (the 401(k) stays in FICA wages). Line 5a column 2: USD 5,480.80; line 5c column 2: USD 1,281.80; line 5e: USD 6,762.60; lines 6, 10 and 12: USD 12,722.60. Deposits: April wages by 15 May 2026, May by 15 June 2026, June by 15 July 2026. Form 941 due 31 July 2026, or 10 August 2026 if every deposit was on time.

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-PR-STATE | State withholding, SUTA, state disability or paid leave, local taxes | Use `us-state-payroll-matrix` |
| R-PR-AGG | Section 3504 agent, CPEO or PEO filing an aggregate Form 941 or 940 (Schedule R) | Refer |
| R-PR-TERR | Employer in a U.S. territory (Forms 941-SS or 944-SS, territorial W-2s) | Refer |
| R-PR-NRA | Nonresident alien employees (chapter 3 withholding, Forms 1042 and 8233), totalization agreements | Refer |
| R-PR-HH | Household employer | Refer: Schedule H (Form 1040) and Pub. 926 |
| R-PR-TFRP | IRS has proposed a trust fund recovery penalty (Letter 1153) or is collecting unpaid payroll tax | Refer: `us-irs-collections-and-controversy` |
| R-PR-CLASS | Disputed worker classification with past-year exposure, section 530 or VCSP | Refer after a first read in `us-1099-nec-issuance` |
| R-PR-NQDC | Section 409A failures, section 3121(v)(2) special timing for deferred compensation | Refer |
| R-PR-RAIL | Railroad employers (RRTA, Form CT-1), clergy, church employees, government employers (section 218 agreements) | Refer |
| R-PR-OLDSICK | COVID-19 era sick and family leave credit claims | Refer: Form 941-X only |
| R-PR-ACA | Employer mandate reporting (Forms 1094-C and 1095-C), Form 5500 | Refer |

## Filing and payment

| What | 2026 due date |
| --- | --- |
| Form 941, Q1 | 30 April 2026 (11 May 2026 if all deposits on time; 10 May is a Sunday) |
| Form 941, Q2 | 31 July 2026 (10 August 2026 if all deposits on time) |
| Form 941, Q3 | 2 November 2026 (31 October is a Saturday; 10 November 2026 if all deposits on time) |
| Form 941, Q4 | 1 February 2027 (31 January is a Sunday; 10 February 2027 if all deposits on time) |
| Monthly depositor | 15th of the following month |
| Semiweekly depositor | Wednesday after a Wednesday to Friday payday; Friday after a Saturday to Tuesday payday |
| FUTA deposits | 30 April 2026, 31 July 2026, 2 November 2026, 1 February 2027 (each only if over USD 500) |
| Form 940 for 2026 | 1 February 2027 (10 February 2027 if all FUTA deposits on time) |
| Forms W-2 to employees, and W-2 and W-3 to the SSA | 1 February 2027 |
| Forms 944, 943, 945 for 2026 | 1 February 2027 |

The 941 dates are the last day of the month after the quarter, moved to the next business day when it falls on a weekend or legal holiday (Instructions for Form 941, When To File; Pub. 15 (2026), Calendar). Form 941 and Form 940 are filed electronically through an authorised provider or on paper to the address in the instructions; balances are paid electronically. Every deposit goes through EFTPS or a same-day wire.

## Completion checklist

- Deposit schedule set from the original line 12 amounts for 1 July 2024 to 30 June 2025, and no USD 100,000 day missed.
- Every deposit matched to a pay date and an EFTPS acknowledgement; Schedule B total equals line 12 for semiweekly depositors.
- Box 3 at most USD 184,500 per employee per employer, including any predecessor wages and any mid-year provider change.
- 0.9% Additional Medicare withheld from the pay period wages passed USD 200,000; line 5d column 1 shows the wages, not the tax.
- Every difference between boxes 1, 3 and 5 explained by a deduction type, and a written section 125 plan exists for each pre-tax health or HSA deduction.
- Codes TP and TT, and box 14b, filled for every tipped or FLSA-overtime employee; code TA for Trump account contributions.
- Four Forms 941 reconciled to the W-3 before filing.
- Schedule A attached and the California 1.5% included in the fourth-quarter FUTA deposit where wages were paid in California.
- Forms W-2 e-filed if the employer files 10 or more information returns in total.
- Current Form W-4 for every employee; 2026 exemption claims renewed by 16 February 2027.
- Any late deposit identified, with the reasonable-cause facts documented.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IRS Pub. 15 (2026), Employer's Tax Guide. Read for What's New (6.2%, $184,500, 1.45%, 22% and 37% over $1 million, $3,000 household, $2,500 election workers, tips and overtime, moving expenses, Trump accounts), Calendar (16 February W-4 expiry), sections 5 to 9 (supplemental wages, W-4), section 11 (Table 1 lookback, $50,000, semiweekly table, $100,000 rule, $2,500 payment with return, 8:00 p.m. EFTPS cutoff, deposit penalty tiers, section 7430 limits, trust fund recovery penalty), section 12 (filing and payment penalties) and section 14 (FUTA 6.0%, $7,000, 5.4%, 0.6%, $1,500 and 20-week tests, $500 deposits, Table 4, credit reduction in the fourth quarter) and section 15 (wage treatment chart). | https://www.irs.gov/pub/irs-pdf/p15.pdf | 2026-11-13 |
| IRS Pub. 15-T (2026), Federal Income Tax Withholding Methods. Read for What's New (2026 tables updated for Public Law 119-21, 2026 Form W-4 exemption checkbox, tips and overtime). | https://www.irs.gov/pub/irs-pdf/p15t.pdf | 2026-11-13 |
| Form 941 (Rev. March 2026). Read for lines 1 to 16 and the 0.124, 0.029 and 0.009 multipliers. | https://www.irs.gov/pub/irs-pdf/f941.pdf | 2026-11-13 |
| Instructions for Form 941 (Rev. March 2026). Read for What's New (aggregate filers, direct deposit refunds), When To File, line 5d ($200,000 withholding trigger) and line 11 (research credit against employer Social Security up to $250,000 per quarter, then Medicare). | https://www.irs.gov/pub/irs-pdf/i941.pdf | 2026-11-13 |
| Instructions for Form 940 (2025). Read for the return structure, Schedule A mechanics and the amended-return route; the 2026 edition is not yet published. | https://www.irs.gov/pub/irs-pdf/i940.pdf | 2026-11-13 |
| Schedule A (Form 940) 2025. Read for the credit reduction computation and the 2025 rates (California 0.012, U.S. Virgin Islands 0.045), used only to check what changed. | https://www.irs.gov/pub/irs-pdf/f940sa.pdf | 2026-11-13 |
| U.S. Department of Labor, Final 2026 FUTA Credit Reductions (updated 10 November 2026), linked from the FUTA Credit Reductions page. Read for California 1.5% with the benefit cost rate add-on waived, and the U.S. Virgin Islands at zero after repayment. | https://oui.doleta.gov/unemploy/docs/final_credit_states_2026.xlsx | 2026-11-13 |
| U.S. Department of Labor, FUTA Credit Reductions page. Read for the 10 November repayment rule and the 0.6% plus reduction formula. | https://oui.doleta.gov/unemploy/futa_credit.asp | 2026-11-13 |
| General Instructions for Forms W-2 and W-3 (2026). Read for What's New ($2,000 wage reporting threshold, box 14a and 14b, codes TP, TT and TA, $2,500 Trump account contribution), the 1 February 2027 due date, e-filing at 10 returns, Form 8508, box 12 codes and the $60, $130 and $340 penalties. | https://www.irs.gov/pub/irs-pdf/iw2w3.pdf | 2026-11-13 |
| Form W-4 (2026). Read for Step 3 ($2,200 and $500), the Step 4(b) worksheet and the exemption checkbox with renewal by 16 February 2027. | https://www.irs.gov/pub/irs-pdf/fw4.pdf | 2026-11-13 |
| Instructions for Form 8027 (2026). Read for the 8% tip allocation rule. | https://www.irs.gov/pub/irs-pdf/i8027.pdf | 2026-11-13 |
| IRS Voluntary Classification Settlement Program page. Read for the 10% payment at section 3509(a) reduced rates. | https://www.irs.gov/businesses/small-businesses-self-employed/voluntary-classification-settlement-program | 2026-11-13 |
| 26 U.S.C. 1401 (govinfo). Read for the $250,000 joint Additional Medicare threshold (library figure). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1401.htm | 2026-11-13 |
| IRS Additional Medicare Tax questions and answers. Read for the $125,000 married filing separately threshold (library figure). | https://www.irs.gov/businesses/small-businesses-self-employed/questions-and-answers-for-the-additional-medicare-tax | 2026-11-13 |

Not yet confirmed: the 2026 Form 940, its instructions and the 2026 Schedule A were not yet published when read, so Form 940 line numbers are not quoted and the 2026 credit reduction comes from the Department of Labor's final list; the IRS has not yet printed the 2026 Schedule A rate. The adoption assistance FUTA treatment was not checked against Pub. 15-B (2026). The first-time abatement criteria are stated from IRS practice, not from a 2026 page read today.
