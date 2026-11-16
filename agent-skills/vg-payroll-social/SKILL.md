---
name: vg-payroll-social
description: "British Virgin Islands employment contributions for 2026. Covers Social Security Board contributions (4% employee and 4.5% employer for private employers, 8.5% self-employed, civil servant and voluntary rates), the 2026 maximum insurable earnings of USD 53,400 and the 2027 figure, National Health Insurance at 3.75% plus 3.75% on up to twice the Social Security ceiling, due dates, the late penalty (10% or 5%: the Board's two pages differ), refunds for people with more than one employer, and where payroll tax is filed (eTax at efiling.gov.vg). Payroll tax rates are not confirmed in this version. Trigger phrases include BVI social security, BVI NHI, insurable earnings BVI, BVI payroll tax filing."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/vg-payroll-social"
  jurisdiction: "VG"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# British Virgin Islands payroll and social contributions v1.1
> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Employer, employee and self-employed contributions in the British Virgin Islands (the Virgin Islands) for calendar 2026: Social Security Board (SSB) contributions and National Health Insurance (NHI) contributions, both collected by the Social Security Board. Amounts are US dollars.

Payroll tax is the territory's main tax on remuneration, collected by the Inland Revenue Department (IRD), which also collects stamp duty, property tax and other levies ([IRD](https://gov.vg/inland-revenue-department)). Since 2 November 2026 payroll tax declarations are filed, and all IRD tax types paid, on the eTax portal at efiling.gov.vg ([Ministry of Finance notice, 6 Nov 2026](https://gov.vg/sites/default/files/2026-11/ministry_of_finance_launches_enhanced_etax_portal_and_online_tax_payments.pdf)). **The payroll tax rates, classes and exemption are not confirmed in this version** (the Payroll Taxes Act could not be opened on an official site; see Not yet confirmed). Do not compute payroll tax from this skill.

The territory has no income tax; see [bvi-tax](bvi-tax.md).

## Ask the client first

1. Is the worker employed by a private employer, a civil servant, self-employed or a voluntary contributor?
2. Gross insurable earnings for the pay period, and the pay frequency (weekly, fortnightly, semi-monthly, monthly).
3. Does the employee work for more than one employer in the year?
4. When will the contributions be paid (on or before the 14th of the following month)?
5. For payroll tax: the employer's payroll, turnover and headcount, which decide its class (rates to be confirmed with the IRD).

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| SSB, private employer employee share | 4% of insurable earnings | [SSB contributions](https://www.vissb.vg/contributions/) |
| SSB, private employer share | 4.5% of insurable earnings (8.5% total) | same |
| SSB, civil servants | 3.5% employee plus 4% Government (7.5% total); civil servants are not covered for sickness benefit | same |
| SSB, self-employed | 8.5% of insurable earnings | same |
| SSB, voluntary contributor | 7% of earnings established by the Board; covers age, invalidity, funeral and survivors benefits only | same |
| SSB maximum insurable earnings 2026 | USD 53,400 a year (period maxima computed: 53,400 / 12 = 4,450.00 a month, / 24 = 2,225.00 semi-monthly, / 26 = 2,053.85 fortnightly, / 52 = 1,026.92 weekly, matching the bulletin's schedule) | [SSB 2026 maximum insurable earnings](https://www.vissb.vg/wp-content/uploads/2026/09/2026-SSB-Maximum-Earnings.pdf) |
| SSB maximum contributions 2026 at the private rate | USD 2,136.00 employee and 2,403.00 employer a year (178.00 and 200.25 a month), computed: 4% and 4.5% of the ceiling, matching the bulletin's schedule | same |
| SSB maximum insurable earnings from 1 January 2027 | USD 55,536 a year; contribution rates unchanged | [SSB notice, 2027 earnings](https://www.vissb.vg/increase-in-maximum-insurable-earnings-effective-1st-january-2027/) |
| NHI maximum insurable earnings 2026 | USD 106,800 a year (from 1 January 2027, USD 111,072) | same |
| NHI, employee | 3.75% of insurable income | [NHI brochure](https://vinhi.vg/wp-content/nhi/NHI-Brochure.pdf) |
| NHI, employer | 3.75% of insurable income (7.5% total) | same |
| NHI, self-employed | 7.5% of stated income | same |
| NHI ceiling rule | Twice the upper wage limit for Social Security contributions | same |
| Due date | On or by the 14th of the month after the month the contributions are due | [SSB contributions](https://www.vissb.vg/contributions/) |
| Late payment, contributions page | Payments made on or after the 15th incur a 10% penalty | same |
| Late payment, 2026 bulletin | Payments made on or after the 15th incur a 5% penalty; the Board's own pages disagree, so confirm the rate with the Board before quoting either | [SSB 2026 bulletin](https://www.vissb.vg/wp-content/uploads/2026/09/2026-SSB-Maximum-Earnings.pdf) |

### Steps

1. **Classify the contributor** (private employee, civil servant, self-employed, voluntary).
2. **Cap the earnings.** SSB on earnings up to the pay-period maximum (USD 4,450.00 a month in 2026); NHI on earnings up to twice the SSB ceiling (USD 106,800 a year in 2026).
3. **SSB:** employee 4% and employer 4.5% of capped earnings (private sector).
4. **NHI:** employee 3.75% and employer 3.75% of NHI-capped earnings. The employer deducts the employee shares from wages.
5. **Remit** both on the employer remittance form by the 14th of the following month.
6. **More than one employer:** each employer deducts and pays on its own earnings; if the combined contributions exceed the maximum payable, the Board refunds the excess to the employee ([SSB contributions](https://www.vissb.vg/contributions/)).
7. **Payroll tax:** file the declaration and pay on eTax (efiling.gov.vg); employers can key employees or import CSV files and correct past periods online.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Employee earning above USD 53,400 in 2026 | SSB stops at the ceiling; NHI continues to USD 106,800 (computed: twice the SSB ceiling, per the NHI brochure) | [SSB 2026 bulletin](https://www.vissb.vg/wp-content/uploads/2026/09/2026-SSB-Maximum-Earnings.pdf); [NHI brochure](https://vinhi.vg/wp-content/nhi/NHI-Brochure.pdf) |
| Civil servant | Lower SSB rates; no sickness benefit cover | [SSB contributions](https://www.vissb.vg/contributions/) |
| Two employers | Each deducts in full; refund of the excess over the maximum from the Board | same |
| Paid on the 15th or later | 10% penalty per the contributions page, 5% per the 2026 bulletin; confirm with the Board | same; [SSB 2026 bulletin](https://www.vissb.vg/wp-content/uploads/2026/09/2026-SSB-Maximum-Earnings.pdf) |
| 2027 payroll | Use USD 55,536 (SSB) and 111,072 (NHI) from 1 January 2027 | [SSB notice](https://www.vissb.vg/increase-in-maximum-insurable-earnings-effective-1st-january-2027/) |

## Worked cases

### Case 1: private employee earning USD 60,000 in 2026

SSB is capped at 53,400: employee 2,136, employer 2,403. NHI is below its 106,800 cap: 2,250 each side. Total employer cost on top of salary 4,653; total deducted from the employee 4,386.

```oa-check
name: BVI SSB and NHI on USD 60,000, 2026
inputs:
  salary: 60000
  ssb_cap: 53400
  nhi_cap: 106800
steps:
  - ssb_employee: min(salary, ssb_cap) * 0.04
  - ssb_employer: min(salary, ssb_cap) * 0.045
  - nhi_each: min(salary, nhi_cap) * 0.0375
  - employer_cost: ssb_employer + nhi_each
  - employee_deduction: ssb_employee + nhi_each
expected:
  ssb_employee: 2136
  ssb_employer: 2403
  nhi_each: 2250
  employer_cost: 4653
  employee_deduction: 4386
```

### Case 2 (decision): two jobs, claim the refund or not

An employee earns USD 40,000 from one employer and 30,000 from another in 2026. Each employer deducts 4%: 1,600 and 1,200, total 2,800. The 2026 maximum employee contribution is 2,136, so the employee should claim a refund of 664 from the Board. Paying a month's contributions on the 15th instead of the 14th would add a penalty: on a USD 5,000 monthly salary at the private SSB rate (8.5% of the 4,450 cap, 378.25) that is 37.83 at the contributions page's 10%, or 18.91 at the 2026 bulletin's 5% (both derived). Confirm which rate the Board applies.

```oa-check
name: BVI SSB two employers refund and late penalty, 2026
inputs:
  job_a: 40000
  job_b: 30000
  ssb_cap: 53400
  monthly_cap: 4450
steps:
  - deducted: job_a * 0.04 + job_b * 0.04
  - maximum: ssb_cap * 0.04
  - refund: max(0, deducted - maximum)
  - month_contribution: monthly_cap * 0.085
  - late_penalty: month_contribution * 0.10
  - late_penalty_bulletin: month_contribution * 0.05
expected:
  deducted: 2800
  maximum: 2136
  refund: 664
  month_contribution: 378.25
  late_penalty: 37.825
  late_penalty_bulletin: 18.9125
```

## When to refuse or refer

- Payroll tax amounts (employer class, rates, exemption): not confirmed here; ask the IRD (bvitaxes@gov.vg, (284) 468-2155) or a local adviser before computing.
- Which late penalty applies (10% on the contributions page, 5% in the 2026 bulletin), whether it also applies to NHI contributions, and any interest: confirm with the Board.
- Benefit entitlement questions (pensions, sickness, unemployment): out of scope.

## Filing and payment

1. SSB and NHI: complete Employer Remittance Form I (or Form II) or the Self-Employed Remittance Form and pay the Board by the 14th of the following month; queries to the contributions department, (284) 852-7844 per the SSB 2026 bulletin ([SSB contributions](https://www.vissb.vg/contributions/)).
2. Payroll tax: sign in or register at efiling.gov.vg, file the payroll tax declaration and pay by card through the payment gateway; inquiries bvitaxes@gov.vg or (284) 468-2155 ([Ministry of Finance notice](https://gov.vg/sites/default/files/2026-11/ministry_of_finance_launches_enhanced_etax_portal_and_online_tax_payments.pdf)).

## Completion checklist

- Contributor type set; pay-period ceilings applied.
- SSB at 4% and 4.5%; NHI at 3.75% and 3.75%.
- Paid by the 14th; refund claimed for multiple employers where due.
- Payroll tax filed on eTax with rates confirmed from the IRD.

## Sources

| Source | URL | Read on |
|---|---|---|
| Social Security Board, contributions page (read via Firecrawl; direct fetch refused): read for the rates by contributor type, the 14th due date, the 10% penalty and the multiple-employer refund | https://www.vissb.vg/contributions/ | 2026-11-14 |
| Social Security Board, 2026 maximum insurable earnings bulletin (PDF): read for the 2026 ceiling by pay period, the maximum contributions, the 14th due date and the 5% late penalty | https://www.vissb.vg/wp-content/uploads/2026/09/2026-SSB-Maximum-Earnings.pdf | 2026-11-14 |
| Social Security Board, notice of 2027 maximum insurable earnings: read for the 2026 to 2027 SSB and NHI ceilings | https://www.vissb.vg/increase-in-maximum-insurable-earnings-effective-1st-january-2027/ | 2026-11-14 |
| National Health Insurance brochure (PDF): read for the 3.75% shares, the self-employed 7.5% and the twice-the-ceiling rule (its 2016 monthly example figures are not used) | https://vinhi.vg/wp-content/nhi/NHI-Brochure.pdf | 2026-11-14 |
| Inland Revenue Department page: read for the taxes the IRD collects and its contacts | https://gov.vg/inland-revenue-department | 2026-11-14 |
| Ministry of Finance notice of 6 November 2026 (PDF): read for the eTax portal launch on 2 November 2026 | https://gov.vg/sites/default/files/2026-11/ministry_of_finance_launches_enhanced_etax_portal_and_online_tax_payments.pdf | 2026-11-14 |

Not yet confirmed: payroll tax rates and classes (the old file had 8% employee, 2% Class 1 and 6% Class 2 employer, Class 1 limits of 7 employees, USD 150,000 payroll and USD 300,000 turnover, and a USD 10,000 employee exemption); the payroll tax due date (the old files gave both the 15th and the 21st of the following month) and the late filing and payment penalties (old file: USD 50 a day, 1.5% a month); the self-employed payroll tax rule; none of these could be read on an official page (the Payroll Taxes Act was not reachable on laws.gov.vg, and the Inland Revenue "Guide to Payroll Tax" PDF at bvi.gov.vg, which Ryan Duguid's fork cites for 10% and 14% class totals, the USD 10,000 exemption from 1 January 2007, a 21-day monthly deadline and a 30 April annual return, returned 404 on 14 November 2026). Indirect evidence only: the FSC's 2024 audited accounts record payroll tax of 6% of salaries for the Commission as employer, and the Financial Investigation Agency's 2024 accounts are reported to show a 14% liability of which 8 points are recoverable from employees. The old SSB rate "4.5% each, 9% total" in bvi-tax was wrong: the Board shows 4% employee and 4.5% employer.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `vg-payroll-social` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/vg-payroll-social. If neither is available, confirm every figure against the official source pages cited above before relying on it.
