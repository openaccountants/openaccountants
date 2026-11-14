---
name: ng-pension-nhf-social-contributions
description: "Nigerian employer social contributions for 2026: the Contributory Pension Scheme (10% employer and 8% employee of monthly emoluments; private-sector threshold 15 employees in the Act, 3 in PenCom guidance), the National Housing Fund (2.5% of basic salary), the Employees' Compensation Scheme contribution to NSITF (1% of monthly payroll), and the Industrial Training Fund levy (1% of annual payroll). Also covers how these contributions interact with personal income tax under the Nigeria Tax Act 2025 (in force 1 January 2026), which treats pension, NHF and NHIS contributions as eligible deductions and taxes individuals from 0% to 25%. Covers coverage, exemptions, foreign employees, remittance deadlines, Group Life cover and penalties. Trigger on: Nigeria pension contribution, PenCom 8% 10%, RSA remittance, NHF 2.5%, NSITF 1%, ITF levy, Nigerian payroll deductions 2026. Out of scope: PAYE administration (ng-payroll), NHIS rates, state pension laws."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ng-pension-nhf-social-contributions"
  jurisdiction: "NG"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Nigerian social contributions: pension, NHF, NSITF and ITF (2026)

Nigeria has no single social security tax. An employer with staff deals with four separate schemes, each under its own law and agency:

- **Contributory Pension Scheme (CPS).** Under the Pension Reform Act 2014 (PRA; Act No. 4 of 2014), run by the National Pension Commission (PenCom). Contributions go to each employee's Retirement Savings Account (RSA) with a Pension Fund Administrator.
- **National Housing Fund (NHF).** Under the National Housing Fund Act, Cap. N45. Contributions are paid to the Federal Mortgage Bank of Nigeria (FMBN).
- **Employees' Compensation Scheme.** Under the Employees' Compensation Act 2010, run by the Nigeria Social Insurance Trust Fund (NSITF).
- **Industrial Training Fund (ITF) training contribution.** Under the Industrial Training Fund Act.

**Tax year.** Calendar year 2026. From 1 January 2026 (the commencement date printed in the gazette), personal income tax is charged under the Nigeria Tax Act 2025 ("NTA"; Act No. 7 of 2025, Official Gazette No. 117, 26 June 2025). That Act replaced the Personal Income Tax Act. The NTA treats pension, NHF and National Health Insurance Scheme contributions as eligible deductions (s30). This skill gives that interaction; PAYE administration itself is in ng-payroll.

## Who this applies to

- **Pension (CPS).** It applies to employment in the public service of the Federation, the FCT, the States and the Local Governments, and in the private sector (PRA s2(1)).
  - **Private-sector threshold: the official texts disagree.** The Act as published by PenCom applies the scheme to employees of an organisation "in which there are 15 or more employees" (PRA s2(2)). PenCom's own FAQ says private organisations with **3 or more** employees are covered (PenCom FAQ 2020, Q16) and requires every employer with at least 3 employees to obtain an employer code. The statute text is followed here (rule: the statute wins), so the scheme is mandatory at 15 or more employees. For an employer with 3 to 14 staff, confirm PenCom's current position before advising; PenCom treats such employers as covered.
  - **Fewer than 3 employees, and the self-employed:** may join voluntarily under PenCom guidelines (PRA s2(3)); PenCom calls this the Micro Pension Plan.
  - **Exempt (PRA s5(1)):** the persons mentioned in section 291 of the 1999 Constitution (PenCom FAQ Q18 names judicial officers), including the armed forces and the intelligence and secret services of the Federation; and an employee entitled to benefits under a pension scheme existing before 25 June 2004 (the commencement of the Pension Reform Act 2004) who at that date had 3 years or less to retire.
  - **Foreigners working in Nigeria:** not required by law to participate (PenCom FAQ 2020, Q19).

- **NHF.** Every Nigerian worker earning NGN 3 000 or more a year, in the public and private sectors (NHF Act s4(a)). The employer deducts the contribution (s9). The self-employed contribute directly (s10).
- **NSITF.** Every registered employer pays an employer-funded contribution on its monthly payroll (NSITF; Employees' Compensation Act 2010).
- **ITF.** Employers pay a statutory training contribution on their annual payroll (ITF Revenue department page). The size threshold for liability was not confirmed from an official source for this version.

Not covered here, refer to a specialist: NHIS/NHIA contribution rates, state pension laws, the details of the Micro Pension Plan, Group Life claims, ITF reimbursement claims, and NSITF benefit claims.

## Rates, bands and thresholds

| Item | Amount | Source |
|---|---|---|
| Pension, employer | at least 10% of monthly emoluments | [PRA s4(1)(a)](https://www.pencom.gov.ng/wp-content/uploads/2018/01/PRA_2014.pdf) |
| Pension, employee | at least 8% of monthly emoluments | [PRA s4(1)(b)](https://www.pencom.gov.ng/wp-content/uploads/2018/01/PRA_2014.pdf) |
| Employer bearing the whole contribution | at least 20% of monthly emoluments | [PRA s4(4)(b)](https://www.pencom.gov.ng/wp-content/uploads/2018/01/PRA_2014.pdf) |
| Monthly emoluments for pension | as defined in the contract, but at least basic salary + housing + transport allowances; if pay is not split, the salary payable | [PRA s120 ("monthly emoluments"); PenCom FAQ 2020, service-delivery Q5](https://www.pencom.gov.ng/wp-content/uploads/2018/01/PRA_2014.pdf) |
| Pension coverage threshold, private sector | 15 or more employees in the Act; PenCom applies 3 or more (see above) | [PRA s2(2); PenCom FAQ 2020, Q16](https://www.pencom.gov.ng/wp-content/uploads/2018/01/PRA_2014.pdf) |
| Voluntary additional pension contributions | allowed while total contributions and other deductions do not exceed one-third of monthly emoluments | [PenCom FAQ 2020, Q7](https://pencom.gov.ng/wp-content/uploads/2020/06/FREQUENTLY-ASK-QUESTION-2020-ENGLISH-MAIN-VISUAL.pdf) |
| Group Life Insurance | at least 3 times the employee's annual total emolument (basic + all allowances for a year); premium paid no later than the start of cover | [PRA s4(5); PenCom FAQ 2020, Q28–29](https://www.pencom.gov.ng/wp-content/uploads/2018/01/PRA_2014.pdf) |
| NHF | 2.5% of basic monthly salary, for workers earning NGN 3 000+ a year | [NHF Act ss4(a), 9(1)](https://fmbn.gov.ng/backend/storage/uploads/37UNgpzsyASabzhQCnHuyzFtIpnsfmW2ODvAmQSG.pdf) |
| NSITF employee compensation contribution | 1% of total monthly payroll, employer only | [NSITF services page](https://nsitf.gov.ng/services/) |
| ITF training contribution | 1% of annual payroll, employer only (50% reimbursable for qualifying training) | [ITF Revenue department page](https://itf.gov.ng/departments/revenue.html) |
| Individual tax bands (2026) | first NGN 800 000 at 0%; next 2 200 000 at 15%; next 9 000 000 at 18%; next 13 000 000 at 21%; next 25 000 000 at 23%; above 50 000 000 at 25% (an individual earning the national Minimum Wage is outside s58) | [NTA s58 and Fourth Schedule](https://nass.gov.ng/documents/download/11249) |
| Eligible deductions for individuals | NHF, NHIS and PRA contributions; mortgage interest on an owner-occupied home; life assurance/deferred annuity premiums; rent relief of 20% of annual rent, up to NGN 500 000 | [NTA s30(2)(a)](https://nass.gov.ng/documents/download/11249) |

## The taxable base

- **Pension.** 18% minimum in total on monthly emoluments: 10% from the employer and 8% from the employee (PRA s4(1)). The rates may be raised by agreement, with notice to PenCom (s4(2)). The floor for emoluments is basic salary + housing + transport (PRA s120). For casual or contract staff whose pay is not split, use the whole salary (PenCom FAQ). Contributions are tax-deductible expenses for the employer and the employee (PRA s10(1)); income on voluntary contributions is taxed if withdrawn within 5 years (s10(4)). In the employee's income tax, the employee's own contributions are an eligible deduction (NTA s30(2)(a)(iii)).
- **NHF.** 2.5% of **basic** monthly salary only. Allowances are excluded (NHF Act s4(a)). The employee's NHF contribution is an eligible deduction (NTA s30(2)(a)(i)).
- **NSITF.** 1% of the employer's **total** monthly payroll, meaning all emoluments (NSITF). There is no employee share.
- **ITF.** 1% of **annual** payroll. "Payroll" in the ITF Act includes basic pay, allowances and other entitlements, but that definition was not read from an official page for this version. There is no employee share.
- **Income tax effect.** Chargeable income is total income less the eligible deductions (NTA s30(1)). The Fourth Schedule bands then apply. Deductions must be claimed in writing in the form the tax authority prescribes (s31).

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| Remit pension contributions (employer + employee) to the Pension Fund Custodian named by the employee's PFA | not later than 7 working days from the day the employee is paid | PRA s11(3)(b) |
| Obtain a PenCom employer code | PenCom requires it of employers with at least 3 employees (through any Pension Fund Administrator) | PenCom FAQ 2020, registration Q8 |
| Remit NHF deductions to FMBN | within one month of making the deduction | NHF Act s9(2) |
| NSITF monthly contribution | monthly, through ecsonline.nsitf.gov.ng | NSITF services page |
| ITF contribution | annually; the exact due date not confirmed for this version | ITF Revenue department page |

## Penalties and interest

- **Pension not deducted or remitted on time:** the employer pays the overdue contributions plus a penalty set by PenCom (PRA s11(6)). The penalty is at least 2% of the total contribution that remains unpaid **for each month or part of a month** the default continues, and is recoverable as a debt owed to the employee's RSA (PRA s11(7)).
- **NHF:** an employer that fails to deduct NHF, or deducts and fails to remit, commits an offence (NHF Act s20):
  - a body corporate: a fine of NGN 50 000;
  - the staff member authorised to deduct or pay: a fine of NGN 20 000, imprisonment for five years, or both;
  - a self-employed defaulter: a fine of NGN 5 000, imprisonment for one year, or both.

  A conviction does not remove the duty to pay the money deducted to FMBN (s20(5)).
  
  FMBN notes the Act is being amended.
- **NSITF and ITF penalties** were not read from an official source for this version.

## Cross-border points

- Foreign employees working in Nigeria are not required to join the CPS (PenCom FAQ 2020, Q19). They may join voluntarily.
- NHF applies to "Nigerian workers" (NHF Act s4(a)). Whether it applies to foreign nationals on a Nigerian payroll was not confirmed.
- Whether an employee's employment income is Nigerian depends on residence and on where the duties are performed (NTA s13). See ng-non-resident-cross-border.

## Worked examples

### Example 1: employee on NGN 600 000 a month, employer with 40 staff

Amaka is a resident employee. Her monthly pay is basic NGN 400 000, housing NGN 150 000 and transport NGN 50 000. Her employer has 40 staff, so it is in the CPS on either reading of the threshold. It is assumed to be liable to ITF. She claims no deductions other than her pension and NHF.

- **Pension:** emoluments are 600 000.
  - Employee 8% = **48 000**.
  - Employer 10% = **60 000**.
  - Total 108 000, remitted within 7 working days of payday.
- **NHF:** 2.5% x basic 400 000 = **10 000**. The allowances are excluded.
- **NSITF** (her share of the employer's 1% of payroll): 1% x 600 000 = 6 000 a month.
- **ITF** (if liable): 1% x 7 200 000 a year = 72 000 a year.
- **Income tax for 2026:**
  - Annual pay 7 200 000.
  - Less eligible deductions: pension 576 000 + NHF 120 000 = 696 000.
  - Chargeable income 6 504 000.
  - Tax: 0% on 800 000; 15% x 2 200 000 = 330 000; 18% x 3 504 000 = 630 720.
  - Total **960 720 a year**, or 80 060 a month.

```oa-check
name: Nigeria employee NGN 600 000/month (basic 400 000), 2026
inputs:
  basic: 400000
  housing: 150000
  transport: 50000
steps:
  - emoluments: basic + housing + transport
  - pension_employee: emoluments * 0.08
  - pension_employer: emoluments * 0.10
  - nhf: basic * 0.025
  - nsitf: emoluments * 0.01
  - itf_annual: emoluments * 12 * 0.01
  - annual_pay: emoluments * 12
  - eligible_deductions: (pension_employee + nhf) * 12
  - chargeable: annual_pay - eligible_deductions
  - band15: max(0, min(chargeable, 3000000) - 800000) * 0.15
  - band18: max(0, min(chargeable, 12000000) - 3000000) * 0.18
  - annual_tax: band15 + band18
  - monthly_tax: annual_tax / 12
expected:
  emoluments: 600000.00
  pension_employee: 48000.00
  pension_employer: 60000.00
  nhf: 10000.00
  nsitf: 6000.00
  itf_annual: 72000.00
  annual_pay: 7200000.00
  eligible_deductions: 696000.00
  chargeable: 6504000.00
  band15: 330000.00
  band18: 630720.00
  annual_tax: 960720.00
  monthly_tax: 80060.00
```

### Example 2: a two-person business (below the pension threshold)

Kola Designs has 2 employees. Each is paid basic NGN 150 000 plus allowances of NGN 50 000 a month.

- **Pension:** not mandatory. The business is below the Act's 15-employee threshold (PRA s2(2)) and also below PenCom's 3-employee line; with fewer than 3 employees the staff may join voluntarily (s2(3)). Mandatory contributions are **0**.
- **NHF still applies:** 2.5% x 150 000 = 3 750 per employee, **7 500** a month in total, remitted to FMBN within one month.
- **NSITF:** 1% x total monthly payroll of 400 000 = **4 000** a month.
- **The edge:** PenCom treats an employer with a third employee as covered, while the Act's text sets the line at 15 employees. If the pension applies, at these pay levels it is 10% + 8% of 200 000 = 36 000 a month per employee. Confirm PenCom's position before telling a 3-to-14-employee business it is outside the scheme.

```oa-check
name: Nigeria two-employee business, pension threshold edge (2026)
inputs:
  employees: 2
  basic_each: 150000
  allowances_each: 50000
steps:
  - pension_mandatory: max(0, min(1, employees - 14))
  - pension_total: pension_mandatory * employees * (basic_each + allowances_each) * 0.18
  - nhf_total: employees * basic_each * 0.025
  - nsitf: employees * (basic_each + allowances_each) * 0.01
  - pension_per_head_if_covered: (basic_each + allowances_each) * 0.18
expected:
  pension_mandatory: 0.00
  pension_total: 0.00
  nhf_total: 7500.00
  nsitf: 4000.00
  pension_per_head_if_covered: 36000.00
```

## Ask the client first

1. How many employees, including casual and contract staff? At 15 or more the Act makes the pension mandatory; PenCom applies it from 3.
2. Each employee's split of basic salary, housing, transport and other allowances.
3. Whether any employee is a foreign national, or falls in an exempt public category.
4. Whether the employer has a PenCom employer code and is registered with FMBN, NSITF and ITF.
5. Pay dates, and when each contribution was actually remitted.
6. Any voluntary pension contributions, NHIS contributions, mortgage interest, life premiums or rent each employee wants claimed as eligible deductions.

## Sources

| Source | URL | Read on |
|---|---|---|
| Nigeria Tax Act 2025 (Act No. 7 of 2025), Official Gazette No. 117 of 26 June 2025 (commencement 1 January 2026; s13, s30, s31, s58, Fourth Schedule) | https://nass.gov.ng/documents/download/11249 | 2026-10-29 |
| Pension Reform Act 2014 (Act No. 4 of 2014), PenCom copy (ss2, 4, 5, 10, 11, 120); text headed "A Bill" with a blank commencement date | https://www.pencom.gov.ng/wp-content/uploads/2018/01/PRA_2014.pdf (linked from https://www.pencom.gov.ng/pra2014/) | 2026-10-29 |
| PenCom, Frequently Asked Questions on the Contributory Pension Scheme (read for 2020 edition) | https://pencom.gov.ng/wp-content/uploads/2020/06/FREQUENTLY-ASK-QUESTION-2020-ENGLISH-MAIN-VISUAL.pdf | 2026-10-29 |
| National Housing Fund Act, Cap. N45, FMBN copy (ss4, 9, 10, 20) | https://fmbn.gov.ng/backend/storage/uploads/37UNgpzsyASabzhQCnHuyzFtIpnsfmW2ODvAmQSG.pdf | 2026-10-29 |
| FMBN, NHF Scheme legal framework (read for Act being amended) | https://fmbn.gov.ng/products/nhf-scheme/legal-framework | 2026-10-29 |
| NSITF, Services (read for 1% of total monthly payroll) | https://nsitf.gov.ng/services/ | 2026-10-29 |
| Industrial Training Fund, Revenue, Inspectorate and Compliance Department (read for 1% of annual payroll) | https://itf.gov.ng/departments/revenue.html | 2026-10-29 |

Not yet confirmed:
- The private-sector pension threshold: PRA s2(2) in PenCom's published copy says 15 or more employees; PenCom's FAQ (Q16) says 3 or more. Whether the gazetted Act or a later amendment reads 3 was not confirmed (PenCom's copy is headed "A Bill" and leaves the commencement date blank).
- The ITF liability threshold (number of employees or turnover), the ITF due date and "payroll" definition, and ITF penalties.
- The NSITF penalty rates and payment due date.
- NHIS/NHIA contribution rates.
- Whether NHF applies to foreign nationals.
- The status of the pending NHF Act amendment.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ng-pension-nhf-social-contributions` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ng-pension-nhf-social-contributions. If neither is available, confirm every figure against the official source pages cited above before relying on it.
