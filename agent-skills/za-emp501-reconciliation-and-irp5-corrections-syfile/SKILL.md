---
name: za-emp501-reconciliation-and-irp5-corrections-syfile
description: "A filing how-to for South African employers and their tax practitioners on the EMP501 employer reconciliation for the 2027 year of assessment (1 March 2026 to 28 February 2027), covering the interim period (21 September to 31 October 2026, for March to August 2026) and the annual period, issuing and correcting IRP5 and IT3(a) certificates on e@syFile Employer or eFiling, the EMP601 cancellation and EMP701 adjustment, mandatory income tax reference numbers, the UIF remuneration ceiling that drives the UIF values, and the 80 and 20 percent travel allowance inclusion."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/za-emp501-reconciliation-and-irp5-corrections-syfile"
  jurisdiction: "ZA"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# EMP501 reconciliation and IRP5 corrections on e@syFile in South Africa

The employer reconciliation is the process in which an employer submits an Employer Reconciliation Declaration (EMP501), issues Employee Tax Certificates (IRP5/IT3(a)) and, where certificates must be cancelled, a Tax Certificate Cancellation Declaration (EMP601). SARS states that three things must agree for a successful submission: the monthly EMP201s submitted (PAYE, SDL, UIF and ETI where applicable), the payments made (excluding penalty and interest payments), and the PAYE, SDL and UIF values on the IRP5/IT3(a)s generated. Figures and dates are for the 2027 year of assessment (2026/27) unless a row says otherwise.

## Scope

For employers registered with SARS for employees' tax who must reconcile EMP201 declarations, payments and IRP5/IT3(a) certificates, and for the practitioners who file for them through e@syFile Employer or eFiling. Manually completed, posted payroll returns are no longer accepted, and submissions on disc at a branch are no longer available. An employer with at most five IRP5/IT3(a)s may be helped at a SARS branch by appointment.

Not covered: individual taxpayers querying an IRP5 on their own ITR12; UIF declarations made to the Unemployment Insurance Fund or the Department of Employment and Labour (the UI-19); PAYE computation (see `za-payroll-paye-uif-sdl`).

## Ask the client first

1. Is this the interim reconciliation (March to August 2026) or the annual one (March 2026 to February 2027)?
2. Does every employee on the certificate file have a valid income tax reference number?
3. How many IRP5/IT3(a)s are there (50 or fewer may use eFiling; at most five may be captured at a branch by appointment)?
4. Is the travel allowance fixed or reimbursive, and is the employer satisfied the vehicle is used at least 80% for business?
5. Do any employees earn above the UIF ceiling, or work fewer than 24 hours a month for the employer?
6. Are you correcting certificates for the current period, or for a prior period, and has SARS already audited or assessed it (EMP217)?

## The method, step by step

### Rates, bands and thresholds

| Item | Figure or date | Source |
| --- | --- | --- |
| Interim reconciliation submission period, 2026 | 21 September 2026 to 31 October 2026, for 1 March 2026 to 31 August 2026 | https://www.sars.gov.za/types-of-tax/pay-as-you-earn/ |
| Annual reconciliation submission period for the year ended 28 February 2026 | 1 April 2026 to 31 May 2026 | https://www.sars.gov.za/latest-news/employer-annual-reconciliation-emp501-1-april-31-may-2026/ |
| Interim period covers | 1 March to 31 August (six months) | https://www.sars.gov.za/types-of-tax/pay-as-you-earn/reconciliations/ |
| Annual period covers | 1 March to 28 or 29 February | same |
| Records to keep | five years | same |
| eFiling may be used by employers with | 50 IRP5/IT3(a)s or fewer | same |
| Branch-capture exception | a maximum of five IRP5/IT3(a)s, by appointment | same |
| UIF remuneration ceiling from 1 June 2021 | R17,712 a month (R212,544 a year) | https://www.sars.gov.za/types-of-tax/unemployment-insurance-fund/ |
| UIF contribution | 1% employee plus 1% employer, 2% in total | same |
| Maximum monthly employee UIF deduction | R177.12 | same |
| UIF exclusion | employee working fewer than 24 hours a month for the employer | same |
| Fixed travel allowance subject to employees' tax | 80% | https://www.sars.gov.za/faq/faq-how-are-travel-expenses-for-which-i-was-reimbursed-treated-for-paye-purposes/ |
| Fixed travel allowance where business use is more than 80% | 20% | same |
| Skills development levy | 1% of total remuneration; employers paying less than R500,000 a year are exempt | https://www.sars.gov.za/budget-tax-guide-2026-online-version-for-printing/ |

### Step 1: confirm registration

Any employer registered with SARS for employees' tax also registers to pay UIF contributions; registration for all tax types can be done once through the client information system. Employers who need not register for employees' tax register at the UI Commissioner's office instead.

### Step 2: declare and pay monthly on the EMP201

The EMP201 declares the total payment, with allocations for PAYE, SDL, UIF and ETI where applicable. A unique payment reference number is pre-populated to link the payment to the declaration.

### Step 3: get every employee's income tax reference number

Valid income tax reference numbers are mandatory. From the 2026 reconciliation period SARS does not accept EMP501 submissions without the required numbers, and missing or invalid numbers stop certificates from being captured. Register employees through the ITREG or BundleReg process on eFiling or e@syFile, use the Tax Reference Number Enquiry Service, or visit a branch by appointment.

### Step 4: generate or import certificates

Generate or import the IRP5/IT3(a) certificates into e@syFile Employer (or capture them on eFiling for 50 or fewer), and capture any extra manual certificates. e@syFile uses all the certificates to calculate the certificate totals for the EMP501. Use the codes guide for the year: PAYE-AE-06-G06 for 2027 (Revision 14, effective 18 September 2026). Source code 4590 has been removed (BRS 2026 release, 2 April 2026).

### Step 5: enter monthly liabilities, payments and ETI

Enter the monthly liabilities, payments (excluding penalties and interest) and ETI. Where the prepopulated PAYE, UIF and SDL values differ from the certificates, amend them to the correct amounts.

### Step 6: balance and submit

The EMP501 must agree with the EMP201s for the period, the payments made and the certificate values. Submit within the period in the table. After submitting, check the submission status and the PAYE Dashboard to confirm the reconciliation was processed.

### Step 7: correct certificates

- **Current period:** cancel a wrong certificate with an EMP601 (from the 2026 interim season the Reconciliation Status Dashboard Action tab can generate an EMP601) and issue a correct one with the reconciliation.
- **A previously submitted reconciliation:** adjust it with a Reconciliation Declaration Adjustment (EMP701).
- The screen-by-screen procedure is in EMP-GEN-02-G01, A Guide to the Employer Reconciliation Process.

### Step 8: re-submit after a SARS audit

Where SARS audits the EMP501 and amends the PAYE liability, the employer must re-submit the EMP501 in line with the audit result on the assessment (EMP217).

### Step 9: issue the certificates

Issue IRP5/IT3(a)s to employees accurately and on time. SARS states that late certificates, or incomplete or incorrect reconciliation information, are non-compliance and may lead to penalties and enforcement.

### Source code 4582

The 2027 codes guide lists code 4582 in its sub-code rationalisation table as "applicable from the 2017 year of assessment", with 4583, 4585 and 4586 (from 2017), 4584 (from 2020), 4587 (from 2021), and 4588 and 4589 (from 2026). The SARS pages read for this skill do not restate the full description of 4582 or which codes feed it; read PAYE-AE-06-G06 for 2027 before advising on it.

## Boundary and exception table

| Situation | What to do |
| --- | --- |
| Employee without an income tax number | Register them first; the EMP501 will not be accepted without it |
| EMP201 values differ from the certificates | Amend the prepopulated figures to the correct amounts before submitting |
| Wrong certificate, current period | EMP601 cancellation and a new certificate |
| Wrong reconciliation already submitted | EMP701 adjustment |
| SARS audited and amended the liability | Re-submit per the EMP217 |
| Employee earns above R17,712 a month | UIF on the ceiling only: R177.12 employee plus R177.12 employer |
| Employee works under 24 hours a month | No UIF contribution |
| 51 or more certificates | Use e@syFile Employer, not eFiling |
| 5 or fewer certificates and no software | Branch capture by appointment |

## Worked cases

### Case 1: UIF on the certificates for an employee above the ceiling

An employee earns R25,000 a month for all twelve months of 2026/27. UIF is worked on the ceiling of R17,712.

- Employee UIF 1% x R17,712 = R177.12 a month; employer the same.
- Total UIF a month R354.24; for the year R4,250.88, which is what the certificates, the EMP201s and the payments must show between them.

```oa-check
name: UIF for 12 months on remuneration above the ceiling, 2026/27
inputs:
  monthly_remuneration: 25000
  ceiling: 17712
  rate_each: 0.01
  months: 12
steps:
  - base: min(monthly_remuneration, ceiling)
  - employee_month: base * rate_each
  - total_month: employee_month * 2
  - total_year: total_month * months
expected:
  employee_month: 177.12
  total_month: 354.24
  total_year: 4250.88
```

## When to refuse or refer

- UI-19 completion and pro rata rules: lodged with the Unemployment Insurance Fund; not on the SARS pages read. Refer to the Department of Employment and Labour.
- The full description of code 4582 and its feeder codes: read PAYE-AE-06-G06 for 2027 first.
- The employee's own travel deduction on assessment (see `za-travel-allowance-tables`).
- Quantifying penalties and interest for a late or wrong reconciliation: the SARS pages read say penalties may follow but give no amounts.
- ETI calculations, ETI validation failures and ETI refunds.
- Directives, IRP3(a) applications and foreign employment income certificates (see `za-foreign-employment-exemption`).

## Filing and payment

- **Channel:** e@syFile Employer, or eFiling for 50 IRP5/IT3(a)s or fewer; a branch by appointment for five or fewer.
- **Interim 2026:** 21 September to 31 October 2026, for 1 March to 31 August 2026.
- **Annual:** the year ended 28 February 2026 was due 1 April to 31 May 2026. The window for the year ending 28 February 2027 is published by SARS in its notice for the season and the Government Gazette; it was not yet published on the pages read.
- Payments are made monthly with the EMP201; the reconciliation itself carries no payment, but differences found must be paid with the correct EMP201 allocation.

## Completion checklist

- [ ] Every employee has a valid income tax reference number.
- [ ] Certificates generated on the 2027 codes guide (PAYE-AE-06-G06 Revision 14).
- [ ] EMP201 values, payments and certificate totals agree for PAYE, SDL, UIF and ETI.
- [ ] UIF worked on the R17,712 ceiling; under-24-hour employees excluded.
- [ ] Travel allowances at 80% (or 20% where justified).
- [ ] EMP601 or EMP701 used for corrections; EMP217 followed if audited.
- [ ] Submission status and PAYE Dashboard checked after submitting.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| SARS, Pay-As-You-Earn page: read for the 2026 interim season (21 September to 31 October 2026, 1 March to 31 August 2026), mandatory income tax numbers, the EMP601 dashboard option, the 2027 codes guide and the removal of source code 4590 | https://www.sars.gov.za/types-of-tax/pay-as-you-earn/ | 2026-11-14 |
| SARS news, Employer Annual Reconciliation (EMP501): 1 April to 31 May 2026: read for the annual season dates for the year ended 28 February 2026 | https://www.sars.gov.za/latest-news/employer-annual-reconciliation-emp501-1-april-31-may-2026/ | 2026-11-14 |
| SARS, Reconciliations page: read for the three items that must agree, interim and annual periods, five-year record keeping, the eFiling limit of 50 certificates, the branch exception of five, EMP601, EMP701 and EMP217 | https://www.sars.gov.za/types-of-tax/pay-as-you-earn/reconciliations/ | 2026-11-14 |
| SARS, Unemployment Insurance Fund page: read for the R17,712 monthly ceiling, R177.12 maximum, 1% plus 1% contribution and the 24-hour exclusion | https://www.sars.gov.za/types-of-tax/unemployment-insurance-fund/ | 2026-11-14 |
| SARS FAQ, travel expenses reimbursed and PAYE: read for the 80% and 20% fixed travel allowance inclusion | https://www.sars.gov.za/faq/faq-how-are-travel-expenses-for-which-i-was-reimbursed-treated-for-paye-purposes/ | 2026-11-14 |
| SARS, PAYE-AE-06-G06 Guide for Codes Applicable to Employees Tax Certificates 2027, Revision 14, effective 18 September 2026: read for the sub-code rationalisation table (4582 to 4589) | https://www.sars.gov.za/wp-content/uploads/Ops/Guides/PAYE-AE-06-G06-Guide-for-Codes-Applicable-to-Employees-Tax-Certificates-2027-External-Guide.pdf | 2026-11-14 |
| SARS, Budget Tax Guide 2026: read for the 1% skills development levy and the R500,000 exemption | https://www.sars.gov.za/budget-tax-guide-2026-online-version-for-printing/ | 2026-11-14 |

Not yet confirmed: the annual reconciliation window for the year ending 28 February 2027 (not yet published on the SARS pages read on 14 November 2026). The description of source code 4582 and its feeder codes.

Drafted by OpenAccountants. Not yet reviewed or approved by a named accountant.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `za-emp501-reconciliation-and-irp5-corrections-syfile` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/za-emp501-reconciliation-and-irp5-corrections-syfile. If neither is available, confirm every figure against the official source pages cited above before relying on it.
