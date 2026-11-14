---
name: us-household-employment-schedule-h
description: Work out a US household employer's 2026 federal employment taxes for a nanny, housekeeper, caregiver or other household employee, the USD 3,000 cash wage threshold for social security and Medicare, the USD 1,000 calendar quarter test for FUTA, the family-member exceptions, Schedule H (Form 1040), the EIN, and the Form W-2 and W-3 due 1 February 2027. Figures from IRS Pub. 926 (2026). Trigger on "nanny tax", "household employee", "Schedule H", "pay my housekeeper", "caregiver taxes", "babysitter W-2". Federal only.
version: "1.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
category: payroll
type: computation
---

# US household employment taxes and Schedule H, tax year 2026

> **Source-cited draft.** Built from IRS Pub. 926 (2026), Household Employer's Tax Guide, Schedule H (Form 1040) and IRS Pub. 15 (2026), read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

## Scope and who this is for

In scope: an individual who pays someone to do household work in or around their home in 2026 (a nanny, babysitter, housekeeper, cleaner, cook, driver, caretaker, health aide, private nurse, gardener) and needs to know whether they owe social security, Medicare and federal unemployment (FUTA) tax, how to report it on Schedule H with their Form 1040, and what Forms W-2 to give.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Whether the worker is an employee at all (an agency, a self-employed cleaner with many clients) | `us-worker-classification-w2-vs-1099` |
| Business employees and Forms 941 and 940 | `us-form-941-940-payroll` |
| State unemployment, state withholding and workers' compensation | `us-state-payroll-matrix` and the state's payroll skill |
| The child and dependent care credit on wages paid to the nanny | `us-federal-income-tax-return-1040` |
| Paying the tax during the year through estimated tax | `us-quarterly-estimated-tax` |

## Ask the client first

1. **Who is the worker and who controls the work?** Does the client decide what is done and how? Did an agency hire, pay and control the worker? (If the agency controls the work, the agency is the employer.)
2. **Relationship:** is the worker the client's spouse, child under 21, parent, or under 18 at any time in 2026 (and is household work their principal occupation)?
3. **Cash wages paid in 2026**, by calendar quarter, and in 2025 by quarter (for the FUTA test). Include cash, checks and transfers; meals and lodging at the home for the client's convenience are not counted.
4. **Did the client withhold** the employee's 7.65% share, or agree to withhold federal income tax at the worker's request (Form W-4)?
5. **State unemployment contributions:** has the client registered and paid the state fund, and on time (by 15 April 2027)? Which state?
6. **EIN:** does the client already have an employer identification number? Does the client own a business with its own payroll?
7. **Worker's details:** legal name and social security number as on the card (Form W-2 needs them), and the Form I-9 kept on file.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Cash wages to one household employee that trigger social security and Medicare | USD 3,000 | [IRS Pub. 926 (2026), Table 1](https://www.irs.gov/pub/irs-pdf/p926.pdf) |
| Social security tax rate, employee and employer each | 6.2% | [IRS Pub. 15 (2026)](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Medicare tax rate, employee and employer each | 1.45% | [IRS Pub. 15 (2026)](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Combined social security and Medicare on cash wages | 15.3% | [IRS Pub. 926 (2026), Table 1](https://www.irs.gov/pub/irs-pdf/p926.pdf) |
| Social security wage base | USD 184,500 | [IRS Pub. 15 (2026)](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Additional Medicare Tax withholding, employee only, on wages above | USD 200,000 | [IRS Pub. 926 (2026), Table 1 note](https://www.irs.gov/pub/irs-pdf/p926.pdf) |
| FUTA test: total cash wages to household employees in any calendar quarter of 2025 or 2026 | USD 1,000 | [IRS Pub. 926 (2026), Table 1](https://www.irs.gov/pub/irs-pdf/p926.pdf) |
| FUTA tax rate | 6.0% | [IRS Pub. 926 (2026), FUTA Tax](https://www.irs.gov/pub/irs-pdf/p926.pdf) |
| Maximum credit against FUTA for state contributions | 5.4% | [IRS Pub. 926 (2026), FUTA Tax](https://www.irs.gov/pub/irs-pdf/p926.pdf) |
| Net FUTA rate with the full credit | 0.6% | [IRS Pub. 926 (2026), FUTA Tax](https://www.irs.gov/pub/irs-pdf/p926.pdf) |
| FUTA wage limit per employee | USD 7,000 | [IRS Pub. 926 (2026), FUTA wages](https://www.irs.gov/pub/irs-pdf/p926.pdf) |
| Credit if state contributions are paid after 15 April 2027 | limited to 90% | [IRS Pub. 926 (2026), FUTA Tax](https://www.irs.gov/pub/irs-pdf/p926.pdf) |
| Forms W-2 and W-3 for 2026 due | 1 February 2027 | [IRS Pub. 926 (2026), Table 2](https://www.irs.gov/pub/irs-pdf/p926.pdf) |
| Schedule H with the 2026 return due | 15 April 2027 | [IRS Pub. 926 (2026), Table 2](https://www.irs.gov/pub/irs-pdf/p926.pdf) |

The USD 3,000 threshold is set each year by the Social Security Administration; always take it from the current Pub. 926. The USD 1,000 FUTA test and the USD 7,000 limit are fixed.

### Step 1: is there a household employee?

1. The worker is an employee if the client can control not only what work is done but how it is done. Full or part time, hourly or by the job, found through an agency list: none of that changes it. If an agency provides the worker and controls the work, the worker is the agency's employee. A self-employed worker who offers the service to the public, brings their own tools and controls how the job is done is not. Source: [IRS Pub. 926 (2026)](https://www.irs.gov/pub/irs-pdf/p926.pdf). Doubtful cases: `us-worker-classification-w2-vs-1099`.

### Step 2: social security and Medicare (the USD 3,000 test, per employee)

2. Add the **cash wages** paid in 2026 to each household employee. Leave out wages to the client's spouse, child under 21, parent (unless the Pub. 926 exception for a parent caring for the client's young or disabled child applies), and an employee under 18 at any time in 2026 unless household work is their principal occupation (a student is not).
3. If one employee's cash wages are USD 3,000 or more, all of that employee's cash wages are social security and Medicare wages (social security only up to USD 184,500). Below USD 3,000: none of them are.
4. Tax = wages x 15.3%: the employer's 7.65% plus the employee's 7.65%. The client should withhold the employee's share if they expect to reach USD 3,000; if they pay it themselves instead, the amount they pay is extra wages for income tax (Form W-2 box 1) but not for social security and Medicare. Withhold the 0.9% Additional Medicare Tax only above USD 200,000 of wages to that employee.

### Step 3: FUTA (the USD 1,000 quarter test, all household employees together)

5. If total cash wages to all household employees (again leaving out spouse, child under 21 and parent; the under-18 exception does not apply here) were USD 1,000 or more in any calendar quarter of 2025 or 2026, FUTA applies for 2026.
6. FUTA wages are the first USD 7,000 of 2026 cash wages per employee. FUTA = FUTA wages x 6.0%, less the credit of up to 5.4% for state unemployment contributions paid on time: 0.6% net. The credit is lower in a credit reduction state (see the Schedule H instructions) and if state contributions are paid late. FUTA is never withheld from the employee.

### Step 4: federal income tax withholding

7. Not required. Withhold only if the employee asks (Form W-4) and the client agrees, using Pub. 15-T.

### Step 5: forms and payment

8. **EIN:** needed for Schedule H and Form W-2 (Form SS-4 or online). A social security number cannot be used instead.
9. **Form W-2:** give Copies B, C and 2 to each employee and send Copy A with Form W-3 to the SSA by 1 February 2027, if the employee's social security and Medicare wages were USD 3,000 or more or any federal income tax was withheld.
10. **Schedule H (Form 1040):** file with the 2026 Form 1040 by 15 April 2027; the total goes to Schedule 2 and is paid with the income tax. If the client does not otherwise file a return, Schedule H is filed by itself.
11. **Pay during the year** to avoid an estimated tax penalty: extra withholding from the client's own job (new Form W-4) or Form 1040-ES payments (15 April, 15 June, 15 September 2026, 15 January 2027).
12. **Business owner option:** a client with a business payroll may instead include the household taxes on the business's Forms 941 (or 944) and 940. Source: [IRS Pub. 926 (2026)](https://www.irs.gov/pub/irs-pdf/p926.pdf).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Cash wages to one employee under USD 3,000 | No social security or Medicare; FUTA may still apply under the quarter test |
| Two employees, one at USD 3,000 or more | The USD 3,000 test is per employee: only that one has social security and Medicare wages |
| Worker is the client's child under 21 | No social security, Medicare or FUTA; wages are still taxable income to the child |
| Worker is the client's parent | No FUTA; social security and Medicare only under the Pub. 926 exception (caring for a child under 18 or a disabled child, with the client widowed, divorced or married to someone unable to care for the child) |
| Teenage babysitter, under 18, a student | Not counted for social security and Medicare; counted for FUTA |
| Agency controls the worker and pays them | Agency is the employer: no Schedule H |
| Meals and lodging at the home for the client's convenience | Not wages |
| Employer pays the employee's share instead of withholding | Not social security and Medicare wages; it is income tax wages on Form W-2 |
| Withheld, but wages end up below USD 3,000 | Repay the employee the amount withheld |
| Client lives in a credit reduction state | FUTA credit is lower: use the Schedule H instructions |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Wages by quarter | Assume the FUTA test is met if annual wages are USD 1,000 or more; ask |
| Whether state unemployment was paid on time | Assume not paid; compute FUTA at 6.0% until shown, then reduce |
| Whether the client withheld the employee share | Assume not withheld: the client owes both halves |
| Worker's age or relationship | Treat as an unrelated adult |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Paid in cash with no records | Employer still owes the tax, plus interest and penalties |
| Worker insists on being a "contractor" | Classification follows control, not the label |
| No EIN and no state registration | Schedule H and Form W-2 cannot be filed correctly |
| Back years unpaid | Schedule H can be filed with an amended return for each year: refer |
| Large Schedule H balance and no estimated payments | Estimated tax penalty |

## Worked cases

**Case 1, a full-time nanny.** A married couple pays a nanny USD 500 a week for 52 weeks of 2026: USD 26,000 in cash wages, at least USD 6,500 in every quarter. They withhold her 7.65% share and pay their state unemployment fund on time; the state is not a credit reduction state.

Social security and Medicare: USD 26,000 x 15.3% = USD 3,978, of which USD 1,989 was withheld from the nanny and USD 1,989 is the couple's share. FUTA: the USD 1,000 quarter test is met; FUTA wages USD 7,000 x 0.6% = USD 42. Schedule H total: USD 4,020, paid with their Form 1040. The couple's own cost on top of wages is USD 1,989 + USD 42 = USD 2,031. They give the nanny a Form W-2 by 1 February 2027.

```oa-check
name: Full-time nanny, Schedule H (2026)
inputs:
  cash_wages: 26000
  fica_threshold: 3000
  futa_wage_limit: 7000
  net_futa_rate: 0.006
steps:
  - fica_wages: cash_wages * min(floor(cash_wages / fica_threshold), 1)
  - employee_share: fica_wages * 0.0765
  - employer_share: fica_wages * 0.0765
  - fica_total: fica_wages * 0.153
  - futa: min(cash_wages, futa_wage_limit) * net_futa_rate
  - schedule_h_total: fica_total + futa
  - employer_cost: employer_share + futa
expected:
  employee_share: 1989.00
  employer_share: 1989.00
  fica_total: 3978.00
  futa: 42.00
  schedule_h_total: 4020.00
  employer_cost: 2031.00
```

**Case 2, a cleaner under the USD 3,000 line.** A single client pays a house cleaner USD 2,900 in 2026, of which USD 1,200 in April to June. The cleaner is an unrelated adult employee.

Social security and Medicare: USD 2,900 is under USD 3,000, so none is due and no Form W-2 is needed (no income tax withheld). FUTA: USD 1,200 in one quarter meets the USD 1,000 test, so FUTA is due on USD 2,900 x 0.6% = USD 17.40, on Schedule H. If the client had paid USD 3,000 or more, USD 3,000 x 15.3% = USD 459 more would be due at the threshold.

```oa-check
name: Cleaner below the social security threshold, FUTA only (2026)
inputs:
  cash_wages: 2900
  max_quarter_wages: 1200
  fica_threshold: 3000
  futa_quarter_test: 1000
  futa_wage_limit: 7000
  net_futa_rate: 0.006
steps:
  - fica_wages: cash_wages * min(floor(cash_wages / fica_threshold), 1)
  - fica_total: fica_wages * 0.153
  - futa_wages: min(cash_wages, futa_wage_limit) * min(floor(max_quarter_wages / futa_quarter_test), 1)
  - futa: futa_wages * net_futa_rate
  - fica_at_threshold: fica_threshold * 0.153
expected:
  fica_total: 0.00
  futa: 17.40
  fica_at_threshold: 459.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-HH-BACK | Unpaid household employment taxes for earlier years | Refer: amended returns with Schedule H for each year, penalties and interest |
| R-HH-CLASS | Real doubt whether the worker is an employee or self-employed | Use `us-worker-classification-w2-vs-1099`; refer if a Form SS-8 is needed |
| R-HH-FARM | Farm workers or household work on a farm operated for profit | Refer: Form 943 rules |
| R-HH-PR | Employer in Puerto Rico or a US territory, or a worker covered abroad | Refer |
| R-HH-STATE | State unemployment registration and state withholding | Use the state's payroll skill |

## Filing and payment

Schedule H with the 2026 Form 1040, due **15 April 2027** (paid then, or during 2026 through withholding or estimated tax). Forms W-2 and W-3 to the SSA and the employee by **1 February 2027**. State unemployment contributions paid by **15 April 2027** to keep the full FUTA credit.

## Completion checklist

- Employee status confirmed (control test) and family-member exceptions applied.
- USD 3,000 test applied per employee; USD 1,000 quarter test applied to all household employees for 2025 and 2026.
- Employee share withheld, or the employer-paid share added to Form W-2 box 1 only.
- FUTA on the first USD 7,000 per employee, with the state credit only if state contributions were paid on time.
- EIN obtained; Form W-2 and W-3 filed by 1 February 2027.
- Schedule H attached to Form 1040; estimated tax or withholding adjusted.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IRS Pub. 926 (2026), Household Employer's Tax Guide. Read for What's New (USD 3,000 for 2026, 6.2%, 1.45%, USD 184,500), Table 1 (USD 3,000, 15.3%, USD 1,000 quarter test, 6%, USD 7,000), Table 2 (1 February 2027 and 15 April 2027), FUTA credit (5.4%, 0.6%, 90%), wages not counted, and the business-employer option. | https://www.irs.gov/pub/irs-pdf/p926.pdf | 2026-11-13 |
| IRS Pub. 15 (2026). Read for the 6.2% and 1.45% rates and the USD 184,500 wage base. | https://www.irs.gov/pub/irs-pdf/p15.pdf | 2026-11-13 |
| Schedule H (Form 1040). Read for the parts of the form (social security and Medicare, FUTA). | https://www.irs.gov/pub/irs-pdf/f1040sh.pdf | 2026-11-13 |

Not yet confirmed: the 2026 Schedule H and its 2026 instructions were not yet published when read (the posted versions are for 2025), so Schedule H line numbers are not quoted and the 2026 credit reduction states are not listed.
