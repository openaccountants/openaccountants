---
name: qc-employer-contributions
description: >
  Calculate and reconcile ordinary Quebec employer contributions for 2026:
  QPP, QPIP, HSF, CNESST, labour standards and WSDRF. Prepare a working paper
  with separate employee deductions and employer costs, RL-1 reporting and
  explicit referrals for special coverage, sector exemptions and cessation.
version: 1.3
jurisdiction: CA
category: payroll
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Quebec employer contributions v1.3

## Scope

Prepare a CAD working paper for Quebec employer contributions on remuneration paid in 2026. This guide does not file a return or make a payment. It is **Built from the law** and **Not yet approved**. Use [canada-payroll](../canada-payroll.md) for federal income tax, EI, T4 and ROE work. This guide does not calculate Quebec income tax withholding.

## Ask the client first

Obtain employee-level pay dates, pay frequency, cash and non-cash remuneration, year-to-date deductions, province of employment, age and coverage/election records. Obtain the employer accounts, assigned remittance frequency, actual payments, associated-employer payroll, CNESST rate notice and training records. Do not infer eligibility or an exemption from missing records.

## The method, step by step

### 1. Establish coverage and separate the bases

Determine the province of employment before selecting QPP or CPP; do not infer it from the employee's home address. [Province instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/set-up-new-employee/determine-province-employment.html)

Keep separate columns for QPP pensionable wages, QPIP eligible wages, HSF subject remuneration, labour standards remuneration, WSDRF payroll and CNESST insurable wages. Establish each base from its own rules; matching totals in a cash-only example do not establish matching treatment of benefits or excluded employment.

### 2. Select the 2026 rates and caps

These are annual ceilings for fully covered employees. They do not determine a deduction from a single pay run.

| Item | 2026 value | Official source |
|---|---|---|
| QPP maximum pensionable earnings | CAD 74,600 | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2027/employers-principal-changes-for-2026-1/ |
| QPP annual basic exemption | CAD 3,500 | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2027/employers-principal-changes-for-2026-1/ |
| QPP first-tier rate, employee and employer each | 6.30% | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2027/employers-principal-changes-for-2026-1/ |
| QPP first-tier annual maximum, each | CAD 4,479.30 | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2027/employers-principal-changes-for-2026-1/ |
| QPP2 upper earnings limit | CAD 85,000 | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2027/employers-principal-changes-for-2026-1/ |
| QPP2 rate, employee and employer each | 4% on pensionable wages above CAD 74,600 up to CAD 85,000 | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2027/employers-principal-changes-for-2026-1/ |
| QPP2 annual maximum, each | CAD 416 | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2027/employers-principal-changes-for-2026-1/ |
| QPIP eligible remuneration ceiling | CAD 103,000 | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2027/employers-principal-changes-for-2026-1/ |
| QPIP employee rate and maximum | 0.430%; CAD 442.90 | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2027/employers-principal-changes-for-2026-1/ |
| QPIP employer rate and maximum per employee | 0.602%; CAD 620.06 | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2027/employers-principal-changes-for-2026-1/ |
| Labour standards employer contribution | 0.06%; maximum subject remuneration CAD 103,000 per employee | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/contribution-related-to-labour-standards/ |
| CNESST annual-basis maximum insurable wages | CAD 103,000 per worker; use the employer's assigned rate | https://www.cnesst.gouv.qc.ca/sites/default/files/documents/periodic-payment-calculation-2026.pdf |
| WSDRF participation threshold | Subject payroll over CAD 2,000,000; 1% eligible-training requirement | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/contribution-to-the-workforce-skills-development-and-recognition-fund/ |

### 3. Calculate QPP

For an ordinary full-year eligible employee with one employer, no exemptions and annual pensionable wages E, use these annual reasonableness checks:

`first_qpp = round(max(0, min(E, 74600) - 3500) * 0.063, 2)`

`qpp2 = round(max(0, min(E, 85000) - 74600) * 0.04, 2)`

The employer matches each component. For actual pay-period deductions, use the current-year employer calculation instructions; do not deduct an annual example result from one pay. [Qpp instructions](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/qpp-contributions/maximum-pensionable-earnings-and-contribution-rate/) [Summary instructions](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rlz-1-s-g-v/guide-to-filing-the-rl-1-summary-summary-of-source-deductions-and-employer-contributions/)

On RL-1, B.A contains employee base plus first additional QPP contributions; B.B contains employee second additional contributions. Box G is pensionable wages, subject to the slip guide's rules. [Slip instructions](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rl-1-g-v/guide-to-filing-the-rl-1-slip-employment-and-other-income/)

For age-related coverage, retirement pensions, RR-50-V elections, pension cancellation, election revocation, disability, excepted employment, partial-year or irregular pay: Check this point with one of our partner accountants.

### 4. Calculate QPIP

Apply the employee and employer rates separately to eligible wages up to the QPIP ceiling. For the cash-only annual examples below, the base is eligible wages without the QPP basic exemption. For payroll calculations use WebRAS, TP-1015.TA-V or TP-1015.F-V. [Qpip instructions](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/qpip-premiums/qpip-premiums-what-you-need-to-know/)

RL-1 H contains employee QPIP premiums withheld; I contains eligible wages, capped at CAD 103,000 for 2026. For non-cash benefits or other remuneration adjustments: Check this point with one of our partner accountants. [Slip instructions](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rl-1-g-v/guide-to-filing-the-rl-1-slip-employment-and-other-income/)

### 5. Calculate HSF with two payroll populations

For an ordinary continuing employer, rate-setting payroll includes worldwide remuneration paid by the employer and employers associated with it on December 31. Apply the resulting rate to this employer's remuneration subject to HSF, after the applicable exclusions. [Total instructions](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/employer-contribution-to-the-health-services-fund/total-payroll/) [Subject instructions](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/employer-contribution-to-the-health-services-fund/remuneration-subject-to-the-contribution/)

For an ordinary private service employer outside the primary/manufacturing and public sectors, with no applicable exemption and rate-setting payroll of CAD 1,000,000 or less, the 2026 HSF rate is 1.65%. [Rates instructions](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2027/employers-principal-changes-for-2026-1/)

For higher payroll and intermediate-rate precision, primary/manufacturing or public-sector status, agriculture/forestry/fishing/sawmill/pulp exemptions, credits, early business cessation or amended HSF reconciliation: Check this point with one of our partner accountants.

### 6. Keep CNESST and labour standards separate

For CNESST periodic payments, determine insurable wages after the guide's exclusions and per-worker annual surplus. Multiply those wages by the latest applicable periodic payment rate supplied by CNESST for the year, then divide by 100. The rate in the examples is hypothetical. Periodic payments go to Revenu Quebec; an assessment balance goes to CNESST by the date on its statement. [Cnesst instructions](https://www.cnesst.gouv.qc.ca/sites/default/files/documents/periodic-payment-calculation-2026.pdf)

Return the 2026 Statement of Wages before March 15, 2027 in the ordinary continuing-employer case. For the last worker's permanent departure, final periodic payment and earlier Statement of Wages deadlines: Check this point with one of our partner accountants. For weekly-basis eligibility, multiple units, personal/volunteer coverage or retrospective rating: Check this point with one of our partner accountants. [Cnesst instructions](https://www.cnesst.gouv.qc.ca/sites/default/files/documents/periodic-payment-calculation-2026.pdf)

For an employer subject to the separate labour standards contribution, calculate eligible remuneration and the contribution on LE-39.0.2-V. Transfer its line 34 base to RL-1 summary line 61 and its line 36 contribution to line 63; line 64 records the payment not already made. Pay by the last day of February of the following year using the summary remittance route. For religious/charitable bodies, Canada Labour Code employers, international organizations or another claimed exemption: Check this point with one of our partner accountants. [Labour instructions](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/contribution-related-to-labour-standards/) [Summary instructions](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rlz-1-s-g-v/guide-to-filing-the-rl-1-summary-summary-of-source-deductions-and-employer-contributions/)

### 7. Determine the WSDRF shortfall

Use the business-wide WSDRF subject payroll across establishments. Payroll of CAD 2,000,000 or less does not meet the participation threshold. Above it, the requirement is 1% of subject payroll; pay the positive difference after eligible training expenditures. For assistance adjustments, carryforwards, first above-threshold-year expenditure, training-cost substantiation or a training initiative quality certificate: Check this point with one of our partner accountants. [Training instructions](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/contribution-to-the-workforce-skills-development-and-recognition-fund/)

For multiple establishments with employer accounts, file an RL-1 summary for each account, but put all business-wide WSDRF data on lines 71-75 of only one summary and leave those lines blank on the others. [Summary instructions](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rlz-1-s-g-v/guide-to-filing-the-rl-1-summary-summary-of-source-deductions-and-employer-contributions/)

### 8. Produce the working paper

Show employee deductions and employer costs separately. Reconcile employee wages to payroll, component bases to evidence, calculated contributions to year-to-date amounts and each liability to actual remittances. Do not treat employee deductions as employer cost. Keep CNESST out of the RL-1 summary remittance. [Summary instructions](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rlz-1-s-g-v/guide-to-filing-the-rl-1-summary-summary-of-source-deductions-and-employer-contributions/)

## Boundary and exception table

| Situation | Action |
|---|---|
| Self-employment, mixed CPP/QPP or personal QPIP return calculations and deductions | Check this point with one of our partner accountants. |
| Disputed worker status, remote or multi-province work, foreign/non-resident payroll, Indigenous exemptions or social-security agreements | Check this point with one of our partner accountants. |
| Employer succession, amalgamation or subsidiary wind-up | Check this point with one of our partner accountants. |
| Pay equity or health-and-safety prevention procedures | Check this point with one of our partner accountants. |

## Worked cases

### Case 1: one employee, CAD 55,000 in 2026

An ordinary private service employer has one full-year employee, no associated employers, no exemptions and CAD 55,000 of cash wages subject to each contribution. The employee is eligible for full-year QPP. The hypothetical CNESST notice assigns CAD 0.18 per CAD 100 of insurable wages; **this is an example input, not a published sector rate**. No WSDRF threshold is met. Use the annual check only, not a pay-period withholding instruction.

```oa-check
name: Quebec employer annual contribution check, one employee, 2026
inputs:
  wages: 55000
  cnesst_dollars_per_100: 0.18
steps:
  - qpp_first_each: round(max(0, min(wages, 74600) - 3500) * 0.063, 2)
  - qpp_second_each: round(max(0, min(wages, 85000) - 74600) * 0.04, 2)
  - qpip_employee: round(min(wages, 103000) * 0.00430, 2)
  - qpip_employer: round(min(wages, 103000) * 0.00602, 2)
  - hsf: round(wages * 0.0165, 2)
  - labour_standards: round(min(wages, 103000) * 0.0006, 2)
  - cnesst: round(min(wages, 103000) / 100 * cnesst_dollars_per_100, 2)
  - employee_quebec_contributions: qpp_first_each + qpp_second_each + qpip_employee
  - employer_quebec_contributions: qpp_first_each + qpp_second_each + qpip_employer + hsf + labour_standards + cnesst
expected:
  qpp_first_each: 3244.50
  qpp_second_each: 0
  qpip_employee: 236.50
  qpip_employer: 331.10
  hsf: 907.50
  labour_standards: 33.00
  cnesst: 99.00
  employee_quebec_contributions: 3481.00
  employer_quebec_contributions: 4615.10
```

The employer subtotal excludes federal EI, wages, income tax deductions and any benefits/other costs. It is not a take-home-pay result.

### Case 2: the nine-person employer reconciles to CAD 885,000

Six employees earn CAD 95,000, two earn CAD 130,000 and one earns CAD 55,000. All are full-year eligible employees of the same ordinary service employer, without associated employers or exemptions. All pay is subject to the listed contributions. Use the same hypothetical CNESST notice rate as case 1. Actual wages are CAD 885,000; do not replace the total by CAD 800,000 while keeping the employee list unchanged.

```oa-check
name: Quebec nine-person annual payroll reconciliation, 2026
inputs:
  standard_count: 6
  standard_wage: 95000
  senior_count: 2
  senior_wage: 130000
  manager_wage: 55000
  cnesst_dollars_per_100: 0.18
steps:
  - payroll: standard_count * standard_wage + senior_count * senior_wage + manager_wage
  - qpp_first_each_total: (standard_count + senior_count) * 4479.30 + (manager_wage - 3500) * 0.063
  - qpp_second_each_total: (standard_count + senior_count) * 416
  - capped_qpip_wages: standard_count * min(standard_wage, 103000) + senior_count * min(senior_wage, 103000) + manager_wage
  - qpip_employer: round(capped_qpip_wages * 0.00602, 2)
  - hsf: round(payroll * 0.0165, 2)
  - labour_standards: round(capped_qpip_wages * 0.0006, 2)
  - cnesst: round(capped_qpip_wages / 100 * cnesst_dollars_per_100, 2)
  - employer_quebec_contributions: qpp_first_each_total + qpp_second_each_total + qpip_employer + hsf + labour_standards + cnesst
expected:
  payroll: 885000
  qpp_first_each_total: 39078.90
  qpp_second_each_total: 3328.00
  capped_qpip_wages: 831000
  qpip_employer: 5002.62
  hsf: 14602.50
  labour_standards: 498.60
  cnesst: 1495.80
  employer_quebec_contributions: 64006.42
```

Although the capped wage totals happen to match in this cash-only example, QPIP, labour standards and CNESST bases must be tested independently in real payroll. CNESST does not cap all eight higher-paid employees at the maximum: the six CAD 95,000 employees remain below it. WSDRF is zero under the threshold.

## When to refuse or refer

If evidence does not establish coverage, contribution bases or the assigned CNESST rate, calculate only supported components and identify the missing fact. Do not turn an unknown fact into a higher stated liability. For any unresolved payroll position: Check this point with one of our partner accountants.

## Filing and payment

Use the remittance frequency assigned by Revenu Quebec. Do not change it before receiving the Notice of Change in Filing Frequency of Returns. For annual, quarterly, monthly, twice-monthly or weekly eligibility and due-date changes: Check this point with one of our partner accountants. [Frequency instructions](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/remitting-source-deductions-and-employer-contributions/frequency-of-remittances/)

For an ordinary continuing employer, file RL-1 slips and the RL-1 summary and distribute employee slips by the last day of February of the following year, applying the authority's due-date calendar. More than five RL-1 slips must be filed online. Deliver employee paper copies; for email consent or secure electronic distribution conditions: Check this point with one of our partner accountants. [Slip instructions](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rl-1-g-v/guide-to-filing-the-rl-1-slip-employment-and-other-income/)

File a summary for each employer account. Use My Account to file online or the prescribed paper summary for the filing year; online slip filing alone does not file the summary. Retain filing and payment confirmations. [Summary instructions](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rlz-1-s-g-v/guide-to-filing-the-rl-1-summary-summary-of-source-deductions-and-employer-contributions/)

For permanently stopping payroll, business cessation, a responsible person's death, late remittances, late slips/summary, insufficient CNESST instalments, late Statement of Wages or interest: Check this point with one of our partner accountants.

## Completion checklist

- Evidence supports the year, coverage, separate bases, rates and actual pay-period method.
- Both case inputs and the employer's own payroll reconcile; no hypothetical rate is used as a real notice.
- Employee deductions and employer costs are separate; filing, employee delivery and payment confirmations are retained.
- Unresolved cases use the partner-accountant referral above.

## Sources

Retained 2026 authority passages were read on 2026-11-23 and their applicability checked on 2026-11-26. The 2026 principal-changes page moved: its explicit 2026 successor was read on 2026-11-26. Labour standards and WSDRF guidance was also read on 2026-11-26. The other rows reuse the saved substantive reads, not a claim of a new whole-source review. CNESST evidence is digital text. These instructions do not claim a separate reading of every consolidated Act.

| Authority and portion | Official source | Read date |
|---|---|---|
| 2026 QPP/QPIP tables and ordinary HSF rate | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2027/employers-principal-changes-for-2026-1/ | 2026-11-26 |
| Annual QPP limits and calculation instructions | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/qpp-contributions/maximum-pensionable-earnings-and-contribution-rate/ | 2026-11-23 |
| Premium calculation tools | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/qpip-premiums/qpip-premiums-what-you-need-to-know/ | 2026-11-23 |
| Worldwide rate-setting payroll | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/employer-contribution-to-the-health-services-fund/total-payroll/ | 2026-11-23 |
| Subject remuneration and exclusions | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/employer-contribution-to-the-health-services-fund/remuneration-subject-to-the-contribution/ | 2026-11-23 |
| Rate, cap, form and payment | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/contribution-related-to-labour-standards/ | 2026-11-26 |
| Participation and shortfall | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/contribution-to-the-workforce-skills-development-and-recognition-fund/ | 2026-11-26 |
| Sections 4.2-4.4, 5.4, 5.9-5.11 | https://www.revenuquebec.ca/en/online-services/forms-and-publications/rl-1-g-v/guide-to-filing-the-rl-1-slip-employment-and-other-income/ | 2026-11-23 |
| Sections 3.3.1, 4.3, 5.4-5.7 and 6.1 | https://www.revenuquebec.ca/en/online-services/forms-and-publications/rlz-1-s-g-v/guide-to-filing-the-rl-1-summary-summary-of-source-deductions-and-employer-contributions/ | 2026-11-23 |
| Notice before changing frequency | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/remitting-source-deductions-and-employer-contributions/frequency-of-remittances/ | 2026-11-23 |
| 2026 guide: annual surplus, periodic rate/calculation, assessment | https://www.cnesst.gouv.qc.ca/sites/default/files/documents/periodic-payment-calculation-2026.pdf | 2026-11-23 |
| Province-of-employment determination | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/set-up-new-employee/determine-province-employment.html | 2026-11-23 |

Not yet confirmed: specialist cases listed above are referred and are not calculation instructions. Check this point with one of our partner accountants.
