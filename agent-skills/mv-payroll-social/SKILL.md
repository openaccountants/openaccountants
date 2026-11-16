---
name: mv-payroll-social
description: "Source-cited draft: payroll & social contributions for Maldives (tax year 2026): rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mv-payroll-social"
  jurisdiction: "MV"
  tax_year: "2026"
  last_updated: "2026-11-16"
---

# Maldives payroll and pension contributions

## Scope

Compute ordinary Maldives employee withholding tax (EWT), employee net pay and Maldives Retirement Pension Scheme (MRPS) contributions for 2026. Determine pension eligibility and pensionable wage separately from taxable remuneration: the bases are not interchangeable. This Guide owns the pack's monthly payroll rates; [individual income tax](mv-income-tax.md) owns the annual personal-tax computation.

Employers administer MRPS for eligible local employees. Foreign employees and self-employed persons may participate voluntarily; voluntary participation does not make every foreign worker subject to the ordinary compulsory deduction. EWT may apply to local and foreign employees, directors, partners and other remuneration recipients under the Income Tax Act's definitions, even where MRPS participation differs. This is a tier 2 source-cited Guide without accountant approval.

## Ask the client first

1. Who is the legal employer, what are its TIN and pension registration details, and what month and functional currency are involved?
2. For each worker, obtain nationality, date of birth, start/end dates, employee/contractor status, MRPS participation and the signed employment contract's basic-salary and pension-deduction clauses.
3. What are basic salary, overtime, allowances, bonuses, benefits in kind, salary advances, permitted absence deductions and actual monthly payments? Obtain payslips and the salary ledger, including when each amount became payable and when it was actually paid.
4. Does the employee receive remuneration from another payer? Obtain the MIRA 916 election, any MIRA 917 determination and prior/cumulative remuneration and EWT.
5. Does the employer fund any part of the employee's pension share? Obtain the contribution statement, actual bank payments, corrections, previous returns and year-to-date controls.
6. Is the work subject to minimum-wage, tourism service-charge or another sector-specific employment obligation? Obtain the applicable classification and underlying records before finalizing payroll.

## The method, step by step

### 1. Determine the pension obligation and base [https://storage.googleapis.com/staging.mpao-1327.appspot.com/strapi/Regulation_on_Determining_Pensionable_Wage_en_3319ce47f8/Regulation_on_Determining_Pensionable_Wage_en_3319ce47f8.pdf](https://storage.googleapis.com/staging.mpao-1327.appspot.com/strapi/Regulation_on_Determining_Pensionable_Wage_en_3319ce47f8/Regulation_on_Determining_Pensionable_Wage_en_3319ce47f8.pdf)

| Rule and conditions | Amount or treatment | Period | Official source |
|---|---|---|---|
| Local employees within compulsory MRPS participation | Enroll from the first month after attaining age 16; contributions stop on attaining age 65 under the scheme rule | 2026; check birth and payroll dates | [MRPS Regulation section 4(b)-(c); Pension Act sections 12 and 14](https://storage.googleapis.com/staging.mpao-1327.appspot.com/strapi/Regulation_on_Maldives_Retirement_Pension_Scheme_en_bfc8708dae/Regulation_on_Maldives_Retirement_Pension_Scheme_en_bfc8708dae.pdf) |
| Employee's ordinary mandatory contribution | 7% of pensionable wage, normally contractually specified basic salary | Each month | [Pensionable Wage Regulation 2021/R-27 section 6](https://storage.googleapis.com/staging.mpao-1327.appspot.com/strapi/Regulation_on_Determining_Pensionable_Wage_en_3319ce47f8/Regulation_on_Determining_Pensionable_Wage_en_3319ce47f8.pdf) |
| Employer's ordinary mandatory contribution | At least 7% of the employee's pensionable wage | Each month | [Pensionable Wage Regulation section 6](https://storage.googleapis.com/staging.mpao-1327.appspot.com/strapi/Regulation_on_Determining_Pensionable_Wage_en_3319ce47f8/Regulation_on_Determining_Pensionable_Wage_en_3319ce47f8.pdf) |
| Employer pays the employee's share | May fund the total 14% itself; do not also deduct the funded amount from the employee | Contractual arrangement and actual contributions required | [Pension Act section 14(e)](https://storage.googleapis.com/prod-storage/strapi/Translation_of_Consolidated_Version_2_of_Pension_Actf_3d700e555b/Translation_of_Consolidated_Version_2_of_Pension_Actf_3d700e555b.pdf) |
| Contract omits the required basic-salary/pension wording, or no qualifying contract | Pensionable wage becomes total remuneration and/or allowances as prescribed; do not use a guessed lower basic salary | 2026 | [Pensionable Wage Regulation section 9](https://storage.googleapis.com/staging.mpao-1327.appspot.com/strapi/Regulation_on_Determining_Pensionable_Wage_en_3319ce47f8/Regulation_on_Determining_Pensionable_Wage_en_3319ce47f8.pdf) |
| Permitted pre-pension deductions from basic salary | Contractual lateness, unauthorized absence and unpaid days at start/end of employment under section 7(a); other deductions follow pension computation | 2026 | [Pensionable Wage Regulation section 7](https://storage.googleapis.com/staging.mpao-1327.appspot.com/strapi/Regulation_on_Determining_Pensionable_Wage_en_3319ce47f8/Regulation_on_Determining_Pensionable_Wage_en_3319ce47f8.pdf) |
| Foreign workers and self-employed participants | Voluntary participation; obtain the applicable enrollment and contribution rules rather than imposing the ordinary employee split by default | 2026 | [Pension Act sections 12(g), 14(c); current FAQ](https://storage.googleapis.com/prod-storage/strapi/Translation_of_Consolidated_Version_2_of_Pension_Actf_3d700e555b/Translation_of_Consolidated_Version_2_of_Pension_Actf_3d700e555b.pdf) |

Check the contract before applying the basic-salary rule. Section 8 requires the pension clause; section 9 supplies a wider fallback base if it is missing. The former statement that all regular allowances always enter pensionable pay was too broad, as was a universal exclusion of all allowances. Keep pensionable salary, excluded pay and permitted reductions visible in the payroll working paper. No ordinary employee contribution cap is assumed here; voluntary-contribution limits require their own confirmation.

### 2. Build remuneration subject to EWT [https://www.mira.gov.mv/Legislations/View/Incometaxact](https://www.mira.gov.mv/Legislations/View/Incometaxact)

Start with remuneration under Income Tax Act sections 3(a) and 79(u)/(bb): cash salary, wages, allowances and taxable benefits, not just the amount received in the bank. Apply the actual exemptions under section 12 and benefits valuation under Income Tax Regulation Chapter 4. A commercial director's fee or partner's remuneration can be EWT remuneration even where the recipient is not described as an employee in the payroll system.

Under section 54(c), deduct MRPS contributions made from that month's employee remuneration before applying EWT. Employer contributions are exempt under section 12(x); a pension share paid wholly by the employer is not also an employee cash deduction. Do not deduct the same contribution twice or deduct every bank payment bearing MPAO from remuneration without matching the month and participant.

Select the EWT month before aggregation. Under Income Tax Act section 80(b), the time of remuneration payment for EWT is the earlier of actual payment and the amount becoming payable, not automatically the bank-payment month. Section 80(c) and Income Tax Regulation section 36 apply where the nature of the payment prevents determining whether it is payable in the relevant period or its exact amount: if the adopted accounting standards require a provision, compute withholding from that provision and include it in the return for the month to which the provision relates. Any additional withholding required when the amount is ascertained belongs in that ascertainment month. Regulation section 36(e)-(f) specifically addresses non-resident-withholding adjustments/refunds; do not assume it authorizes an automatic EWT overpayment credit. [Act section 80(b)-(c)](https://www.mira.gov.mv/Legislations/View/Incometaxact); [Regulation section 36](https://www.mira.gov.mv/Legislations/View/Income-Tax-Regulation).

Aggregate remuneration falling in that EWT month for the same payer under section 54(d), after applying the paid/payable and uncertain-payment rules above. Ordinary monthly bands below apply to remuneration subject to EWT, after the permitted pension deduction. They are marginal bands, not a flat rate on all salary.

| Monthly taxable-remuneration slice | Rate | Period and condition | Official source |
|---|---|---|---|
| First MVR 60,000 | 0% | 2026 ordinary elected/single payer | [Income Tax Act section 54(a)-(b)](https://www.mira.gov.mv/Legislations/View/Incometaxact) |
| Above MVR 60,000 to MVR 100,000 | 5.5% | Same | [Income Tax Act section 54(a)-(b)](https://www.mira.gov.mv/Legislations/View/Incometaxact) |
| Above MVR 100,000 to MVR 150,000 | 8% | Same | [Income Tax Act section 54(a)-(b)](https://www.mira.gov.mv/Legislations/View/Incometaxact) |
| Above MVR 150,000 to MVR 200,000 | 12% | Same | [Income Tax Act section 54(a)-(b)](https://www.mira.gov.mv/Legislations/View/Incometaxact) |
| Above MVR 200,000 | 15% | Same | [Income Tax Act section 54(a)-(b)](https://www.mira.gov.mv/Legislations/View/Incometaxact) |

Sum each slice. Do not use the former third-party table with different rates and much lower bands. Annual liability and annual filing exemptions require the individual Guide; monthly EWT is not a separate final personal-tax charge in every case.

### 3. Check multiple payers and irregular pay [https://www.mira.gov.mv/Legislations/View/Income-Tax-Regulation](https://www.mira.gov.mv/Legislations/View/Income-Tax-Regulation)

Under Regulation section 41(e)-(m), the recipient elects the payer applying the tax-free band using MIRA 916, subject to MIRA's power to determine a payer or rates. Other relevant payers deduct 8% from their monthly taxable remuneration up to MVR 150,000 and use the higher respective bands on the excess. MIRA 917 requests a changed determination; retain the actual MIRA notice instead of selecting a convenient rate. An election or determination made on or before the 10th applies from that month; after the 10th it applies no later than the following month, subject to the detailed provisions. A second employer must not grant another full tax-free band.

For irregular pay, section 42(b) can exempt a month above the ordinary monthly tax-free level where regular taxable pay and estimated annual taxable remuneration remain within the prescribed limits. Once cumulative remuneration exceeds MVR 720,000, section 42(b-1) requires cumulative computation using its annual bands, less EWT already deducted. The rule has a separate cessation condition after consecutive higher-pay months, and short accounting periods are prorated. Use the actual year-to-date payroll, employer election and section 42 conditions; do not simply multiply the latest month's tax by the year.

### 4. Reconcile payroll, pensions and EWT

For each employee, record gross cash salary, taxable benefits, exempt benefits, pensionable wage, employee MRPS, employer MRPS, taxable remuneration after employee MRPS, ordinary/cumulative or notified EWT, other lawful deductions and net cash pay. Record actual-payment and payable dates and the resulting EWT month separately; any required provision needs its own period and reconciliation. Keep noncash benefits out of the cash-payment total while including them in taxable remuneration when required.

Reconcile employee and employer pension amounts to the accepted contribution statement and bank payment. Reconcile EWT to the information sheet, MIRA 601, tax-account receipt and payslip deduction. Employee EWT and employee pension are withheld liabilities; employer MRPS is an additional employer cost. Do not treat remitting a withheld amount as a second payroll expense. Corrections require the underlying month and original submission, not an unexplained deduction from the next employee's salary.

## Boundary and exception table

| Circumstance | Action |
|---|---|
| Contractor rather than contract of service | Analyze the actual relationship; business income/NWT may replace EWT. Do not decide from invoice wording alone. |
| Foreign employee | EWT and MRPS tests are separate; voluntary pension enrollment is not an EWT exemption. |
| Missing basic-salary/pension clause | Apply the Regulation section 9 fallback before calculating pension. |
| Employer funds both pension shares | Record employer expense and total remittance; deduct no funded share from employee net salary. |
| Bonus, arrears, multiple salary payments or more than one employer | Check sections 41-43 and prior/cumulative data; do not grant repeated free bands. |
| Benefits in kind or accommodation | Use the specific exemption and valuation rules; value and document the benefit rather than assuming all allowances are tax free. |
| Minimum wage, tourism service charge or another contribution claimed | Obtain the applicable current employment instrument; this Guide does not certify that MRPS is the only possible employment-related charge. |

## Worked cases

### Case 1: ordinary employee deduction

Assume an eligible local employee with MVR 80,000 basic salary, a compliant pension clause, no benefits or other pay, an ordinary single payer and no other deductions. Employee MRPS is MVR 5,600; employer MRPS is MVR 5,600; the total pension remittance is MVR 11,200. EWT taxable remuneration is MVR 74,400, giving EWT MVR 792. Net cash pay is MVR 73,608 and employer cost is MVR 85,600. [Pensionable Wage Regulation section 6](https://storage.googleapis.com/staging.mpao-1327.appspot.com/strapi/Regulation_on_Determining_Pensionable_Wage_en_3319ce47f8/Regulation_on_Determining_Pensionable_Wage_en_3319ce47f8.pdf); [Income Tax Act section 54](https://www.mira.gov.mv/Legislations/View/Incometaxact).

```oa-check
name: Ordinary payroll after employee MRPS
inputs:
  basic: 80000
steps:
  - employee_mrps: basic * 0.07
  - employer_mrps: basic * 0.07
  - taxable: basic - employee_mrps
  - ewt: (taxable - 60000) * 0.055
  - net: basic - employee_mrps - ewt
  - cost: basic + employer_mrps
expected:
  employee_mrps: 5600
  employer_mrps: 5600
  taxable: 74400
  ewt: 792
  net: 73608
  cost: 85600
```

### Case 2: employer funds both shares

For the same MVR 80,000 salary, suppose the employer elects and actually pays the full pension contribution without taking any pension amount from the employee. Employer pension cost is MVR 11,200. EWT taxable remuneration remains MVR 80,000 because no pension was contributed from employee remuneration; EWT is MVR 1,100 and net salary is MVR 78,900. Employer cost is MVR 91,200. This choice increases employer cost and employee cash pay relative to Case 1; it does not generate another deduction from the employee's salary. [Pension Act section 14(e)](https://storage.googleapis.com/prod-storage/strapi/Translation_of_Consolidated_Version_2_of_Pension_Actf_3d700e555b/Translation_of_Consolidated_Version_2_of_Pension_Actf_3d700e555b.pdf); [Income Tax Act sections 12(x), 54(c)](https://www.mira.gov.mv/Legislations/View/Incometaxact).

```oa-check
name: Employer funds full pension
inputs:
  salary: 80000
steps:
  - employer_pension: salary * 0.14
  - ewt: (salary - 60000) * 0.055
  - net: salary - ewt
  - cost: salary + employer_pension
expected:
  employer_pension: 11200
  ewt: 1100
  net: 78900
  cost: 91200
```

### Case 3: missing pension clause changes the base

Suppose a contract describes total monthly remuneration MVR 80,000 including allowances, without specifying basic salary and the required pension deduction. Do not replace that with an unsupported MVR 60,000 basic figure. Section 9 makes the actual MVR 80,000 total the fallback pensionable wage; ordinary employee/employer contributions are MVR 5,600 each, rather than MVR 4,200 each on the guessed base. [Pensionable Wage Regulation section 9](https://storage.googleapis.com/staging.mpao-1327.appspot.com/strapi/Regulation_on_Determining_Pensionable_Wage_en_3319ce47f8/Regulation_on_Determining_Pensionable_Wage_en_3319ce47f8.pdf).

```oa-check
name: Contract fallback pensionable wage
inputs:
  total_pay: 80000
  guessed_basic: 60000
steps:
  - correct_share: total_pay * 0.07
  - unsupported_share: guessed_basic * 0.07
  - difference: correct_share - unsupported_share
expected:
  correct_share: 5600
  unsupported_share: 4200
  difference: 1400
```

## When to refuse or refer

Stop a filing-ready payroll where identity/age, legal employer, worker status, pension contract or gross-to-net reconciliation is unresolved. Refer benefits valuation, cross-border employment, retrospective corrections, service-charge distribution, minimum-wage disputes and pension enforcement when the necessary instrument or facts are missing. Keep provisional calculations clearly marked and identify the exact missing fact; do not invent a salary cap, voluntary limit or exemption.

## Filing and payment

For pension, confirm employer registration and employee enrollment in [Koshaaru via the Pension Office](https://pension.gov.mv/en/client-services). The current service instructions require updated salary/employment records, monthly submission, payment and upload of the payment slip. Reconcile the accepted contribution statement to both shares, pay the generated invoice/reference, retain the slip and check that the remittance has been credited. MRPS Regulation section 8(b) requires the ordinary monthly contributions by the 15th of the following month. The payment clause was visually read on the official scanned English PDF, page 5; the three listed amendments do not amend section 8(b). Check any specific notified holiday adjustment before payment.

For EWT, apply Income Tax Regulation sections 3, 7 and 96. MIRA 118 supplies employee registration information. Registration can be triggered by estimated average monthly taxable remuneration at or above MVR 60,000 or actual amounts at or above that level in two consecutive months; when the employer has a recipient meeting the trigger, section 7(c) brings in the relevant recipients at MVR 30,000 average taxable remuneration.

The recipient's self-registration tests are separate. Under section 7(d)-(e), a person deriving remuneration from more than one payer, who has not been registered by any of those payers, must apply for registration when average monthly gross income during any 12-month period exceeds MVR 40,000. Under section 7(f), an individual not registered by any payer of remuneration must apply when average monthly gross income during the past 12-month period exceeds MVR 60,000. These are recipient gross-income tests, distinct from the employer's taxable-remuneration tests above and the business gross-revenue test in section 4(c)(3). Do not equate tax payable with registration. [Regulation section 7(d)-(f)](https://www.mira.gov.mv/Legislations/View/Income-Tax-Regulation).

File [MIRA 601 v24.1](https://www.mira.gov.mv/Files/GetFile/66e00067-b1d0-46e8-90f0-f77b05e87f4c) through MIRAconnect with the employee information sheet. Enter the payer TIN/name, MM/YYYY month and functional currency; use Part One for the standard computation and Part Two only for the section 42(b-1) cumulative rule. The form's standard band fields A-E feed F, its cumulative fields G-L feed M, and total EWT payable O combines the two computations. Include the employee counts and reconcile the information sheet to gross remuneration, employee MRPS and total withheld before the authorized declaration. Use the live form's labels; do not guess box numbers from scrambled PDF text.

Under Income Tax Act section 58, EWT return/payment are due by the 15th of the following month, using the EWT month selected under section 80(b)-(c) and Regulation section 36 above rather than automatically the later cash-payment month. Regulation section 96 requires the remaining monthly returns in that year after the first required return, including nil periods, unless MIRA grants the specified exemption; prior required months must be filed first. Regulation section 97 provides the MIRA 650 reconciliation return when MIRA determines it is required; retain the particular deadline notice.

Under Regulation sections 105-108, a payer with MVR functional currency prepares EWT in MVR and can pay in MVR or USD. A non-MVR functional currency requires USD presentation/payment under the current rules. Retain the prescribed conversion evidence. Payment is via MIRAconnect or MRTGS under section 103, separate from the pension remittance. Save the submission acknowledgement and tax payment receipt, then reconcile the tax account.

Tax late-filing/information penalties and daily late-payment fines follow [Tax Administration Act sections 65-67](https://www.mira.gov.mv/Legislations/View/tax-admin-act-consolidated); pension noncompliance follows the Pension Act and scheme regulation. Do not apply a tax-penalty formula to pension arrears or assert that a salary deduction satisfies the employer's duty to remit.

## Completion checklist

- Identity, nationality, age, status, contract and pension eligibility documented.
- Pension base and EWT base calculated separately, with funded shares and benefits identified.
- Employer election/notified rates and year-to-date/cumulative data checked.
- Payslips, payroll ledger, contribution statement, information sheet and bank totals agree.
- Separate pension and EWT submissions, acknowledgements and payments retained.
- Open employment-law or enforcement matters referred before sign-off.

## Sources

| Source and actual material read | Official URL | Read on |
|---|---|---|
| Pension Office current MRPS FAQ: participation, contribution rates, pensionable wage and registration disclosures opened in an ordinary browser | https://pension.gov.mv/en/faq/mrps | 2026-11-16 |
| Consolidated English unofficial Pension Act, version 2 updated 4 June 2026: sections 12-15, including voluntary foreign enrollment and employer-funded contributions | https://storage.googleapis.com/prod-storage/strapi/Translation_of_Consolidated_Version_2_of_Pension_Actf_3d700e555b/Translation_of_Consolidated_Version_2_of_Pension_Actf_3d700e555b.pdf | 2026-11-16 |
| Official English unofficial Pensionable Wage Regulation 2021/R-27: all four pages, especially sections 6-9 and contract fallback | https://storage.googleapis.com/staging.mpao-1327.appspot.com/strapi/Regulation_on_Determining_Pensionable_Wage_en_3319ce47f8/Regulation_on_Determining_Pensionable_Wage_en_3319ce47f8.pdf | 2026-11-16 |
| MRPS Regulation 2014/R-20: sections 4 and 8-11 on scanned pages 2 and 5, visually read; amendment instructions for 2016/R-90, 2018/R-132 and 2024/R-44 inspected for affected sections, without claiming a full translation | https://storage.googleapis.com/staging.mpao-1327.appspot.com/strapi/Regulation_on_Maldives_Retirement_Pension_Scheme_en_bfc8708dae/Regulation_on_Maldives_Retirement_Pension_Scheme_en_bfc8708dae.pdf | 2026-11-16 |
| Pension Office Client Services: Contribution Collection steps opened in browser; current legislation page used to identify the linked official PDFs | https://pension.gov.mv/en/client-services | 2026-11-16 |
| Income Tax Act consolidated 31 August 2026, authority-hosted English unofficial translation: sections 12(x), 19, 54, 57-59, 79 remuneration/employee definitions and 80(b)-(c) paid/payable timing and its uncertain-payment exception | https://www.mira.gov.mv/Legislations/View/Incometaxact | 2026-11-16 |
| Income Tax Regulation consolidated 20 August 2026: sections 3, 7 including recipient self-registration under 7(d)-(f), 31, 36 uncertain-payment provisions, 41-43, 96-97, 103 and 105-108 | https://www.mira.gov.mv/Legislations/View/Income-Tax-Regulation | 2026-11-16 |
| MIRA 601 v24.1, both pages: standard/cumulative computation, functional currency, employee counts and information-sheet requirement | https://www.mira.gov.mv/Files/GetFile/66e00067-b1d0-46e8-90f0-f77b05e87f4c | 2026-11-16 |
| MIRA filing page: required/nil months, portal, currency and payment | https://www.mira.gov.mv/Pages/View/ewtfile | 2026-11-16 |
| Tax Administration Act sections 65-67, current consolidated English unofficial translation | https://www.mira.gov.mv/Legislations/View/tax-admin-act-consolidated | 2026-11-16 |

The storage.googleapis.com PDFs are the exact download links displayed by the Pension Office's [current legislation page](https://pension.gov.mv/en/regulations), not unrelated third-party summaries. The Dhivehi laws prevail over the English unofficial translations.

Not yet confirmed: any notified MRPS holiday adjustment; current voluntary/self-employed contribution ceiling; any additional generally applicable social-security charge beyond the identified MRPS scheme; current minimum-wage category amounts and tourism service-charge requirements; live portal payment-reference screens and any individual MIRA 650 deadline notice. Do not rely on a former draft's unverified figures for these matters.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-16. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mv-payroll-social` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mv-payroll-social. If neither is available, confirm every figure against the official source pages cited above before relying on it.
