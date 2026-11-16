---
name: kg-payroll-social
description: "Kyrgyzstan 2026 ordinary payroll: employer tariff selection, employee deductions, social contribution floors and cap, PIT withholding, reporting and remittance."
jurisdiction: KG
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
tax_year: 2026
last_updated: 2026-11-15
version: 0.1
type: computation
category: international
---

# Kyrgyzstan payroll and social contributions (2026)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Select the employer and employee category before multiplying salary. Ordinary business employers generally use the reduced tariff; the higher employer tariff remains for listed excluded sectors.

## Who this applies to

Ordinary domestic payroll for employers and hired workers under Tariffs Act No8 arts2 and2-2. Permanent/temporary workers, including foreign nationals and stateless persons, are covered subject to treaty exceptions. Garment/textile production, agricultural cooperatives, individual-entrepreneur worker categories, HTP and other specialist schedules require their own classification; do not apply the ordinary examples to them.

## Rates, bands and thresholds

| Item | Amount and conditions | Official source |
|---|---|---|
| Ordinary business/non-profit employer | 2.25% under art2-2(1)(a): Pension Fund 1%, mandatory medical insurance 1%, workers' health improvement 0.25%; floor/cap apply | https://cbd.minjust.gov.kg/4-1330/edition/latest/ru |
| Ordinary employee | 10% under arts2(2)(a),2-2(2)(a): Pension Fund 8%, State Accumulative Pension Fund 2%; the special art11-1(a) category instead allocates 10% to Pension Fund | https://cbd.minjust.gov.kg/4-1330/edition/latest/ru |
| Ordinary combined contribution | 12.25%, derived as 2.25% + 10% when both use actual salary and neither a floor nor cap changes the amount | https://cbd.minjust.gov.kg/4-1330/edition/latest/ru |
| Listed excluded-sector employer | 17.25% under art2(1)(a): Pension Fund 15%, mandatory medical insurance 2%, workers' health improvement 0.25%; excluded sectors below | https://cbd.minjust.gov.kg/4-1330/edition/latest/ru |
| Higher-tariff combined contribution | 27.25%, derived as 17.25% + 10% for an ordinary worker before floor/cap adjustments; not the universal business rate | https://cbd.minjust.gov.kg/4-1330/edition/latest/ru |
| Disabled employee categories | Groups I/II and group III hearing disability: employer 1.25% under art2-2 or 15.25% under art2; employee 2% Pension Fund, subject to the statutory war-disability exception | https://cbd.minjust.gov.kg/4-1330/edition/latest/ru |
| Working pensioner | Employee 8% Pension Fund; pensioners employed by a homeowners' association use 2% under art2-2(2)(b) | https://cbd.minjust.gov.kg/4-1330/edition/latest/ru |
| Ordinary-business employer floor | Employer contribution at least the amount based on 100% of the published district/city average wage, art13(3)(b); employee withholding remains on actual pay, subject to cap | https://cbd.minjust.gov.kg/4-1330/edition/latest/ru |
| Art2 employer floor | Employer contribution at least the amount based on 60% of the published district/city average wage, art13(3)(a); statutory exceptions below | https://cbd.minjust.gov.kg/4-1330/edition/latest/ru |
| Combined monthly cap | Art13(4): contribution for one insured person cannot exceed the amount calculated from 20 times the previous year's national average monthly wage, using the applicable category tariffs; this is not the district/city floor | https://cbd.minjust.gov.kg/4-1330/edition/latest/ru; current method: https://cbd.minjust.gov.kg/230020107/edition/latest/ru |
| Ordinary PIT | 10% of the statutory salary tax base, Tax Code art197(1); special rates, deductions and average-wage rules below | https://cbd.minjust.gov.kg/112340/edition/latest/ru |

Art2-2(3) excludes budget-funded organisations; nationally significant mining/subsoil developers; electricity/heat/gas supply; alcohol/tobacco/fuel production/import subject to the licensed refining exception; mobile operators; internet providers; commercial banks and specified financial/credit institutions. Those categories use art2 rather than the ordinary-business employer rate. Check the exact licensed activity rather than classifying a whole industry by name alone.

## The base

1. Identify the correct employer and worker tariff. Contributions generally apply to all relevant accrued payments at each job separately; Tariffs Act art13(1)-(2) covers multiple workplaces/categories. Check the statutory earnings exclusions and special category before treating every payment as contributory.
2. For ordinary full-month art2-2 payroll, employer base is actual accrued pay plus any positive shortfall to the applicable district/city average. For art2, use the corresponding floor percentage. The employee contribution uses actual accrued pay. Art13(3) excludes designated junior support staff and the specified budget/state, state educational, social-insurance-funded, rural-producer and homeowners' association employers from the floor. Instruction729 paras5-10 govern additional wage fund, incomplete days and part-time calculations; do not apply a full-month floor to a partial month without adjustment.
3. Apply the combined cap in art13(4) and Instruction729 para7 using the current national average. The instruction's printed historical wage example is not the current-year wage figure. High-pay cap allocation needs the current reporting method before finalising either party's deduction.
4. Compute PIT separately under Tax Code arts187,194,197,200. Ordinary documented personal deduction is 6.5 calculation indicators per month, with 1 indicator per qualifying dependant; an indicator is KGS 100 under Resolution1115-III. Eligible employee state social contributions are deductible except those on PIT-exempt income. Standard deductions at the employer generally need employment lasting at least 15 days that month; shorter employment/concurrent jobs permit only the social contribution deduction.
5. Where the PIT average-wage floor applies, tax on the actual calculated base is withheld from the worker and tax on the shortfall is paid by the employer from its own funds, cumulatively for actual months worked. Art187 exceptions and proportional-time rules differ from the social-insurance floor. Do not use one floor calculation for both taxes. Missing relief documents mean withholding without relief until the permitted correction.
6. Reconcile net pay, employer contributions and employer-funded PIT separately. Employer contributions are additional employer cost, not an employee deduction.

Special PIT categories include the 5% employee groups in art197(2), garment/textile and qualifying platform rules. The linked [personal income tax skill](kg-income-tax.md) sets their boundaries and annual deduction claims. Garment/textile social tariffs use the separate art2-1 schedule, not this ordinary salary method. Refer any unclassified specialist payroll before computing.

## Deadlines and filing

| Obligation | Due and condition | Official source |
|---|---|---|
| PIT tax-agent payment and report | Not later than 20 of the following month under Tax Code arts202-203, for the relevant paid/received income | https://cbd.minjust.gov.kg/112340/edition/latest/ru |
| Ordinary employer/employee social contributions | Monthly, not later than 20 of the month after accrual, Social Insurance Act art24(1); special final-results remuneration has art24(3) timing | https://cbd.minjust.gov.kg/627/edition/latest/ru |
| Social contribution report | Monthly electronic report not later than 20 of the following month, Instruction729 paras18-19; next working day if the last day is non-working | https://cbd.minjust.gov.kg/230020107/edition/latest/ru |

Use the prescribed electronic PIT/social report through the tax authority system. Check TIN/insured-person identification, reporting month, actual wage fund, additional wage fund, worker category, amounts and days under Instruction729 paras19,22-1. Reconcile each insured person with payroll and payment records; submit corrections with supporting documents under para20. Keep the filed report, submission evidence, person-level reconciliation and payment evidence. Current live form identifier, box layout and payment account/reference are not verified here. Do not substitute the old approximate remittance window. Tax Code art18 governs PIT non-working deadlines.

## Penalties and interest

Social Insurance Act art26 charges late-contribution interest at 0.09% per day, capped at 100% of principal debt, with the stated budget-financing and force-majeure exceptions; concealed/understated wages have a separate sanction. Tax Code art82 applies ordinary tax interest separately, with its own exceptions. Tax Code art163 addresses late reports/declarations; do not apply an obsolete pre-2021 reporting penalty to a current report.

## Cross-border points

Tariffs Act art14 applies citizen tariffs to foreign/stateless employees unless an effective treaty provides otherwise. Foreign civil-contract recipients and entrepreneurs can have self-payment obligations rather than ordinary payroll. Confirm employment classification and treaty/social-security coverage; a foreign passport alone does not remove contributions. PIT source/residence/permit rules remain separate from social coverage.

## Two worked examples that recompute

Illustrative KGS inputs. Assume a full eligible ordinary-rate month, no dependants, no pensioner/disability/special status, and pay below the contribution cap. The average-wage amount in a case is hypothetical, not a published district statistic.

An ordinary business pays KGS 50000, above all applicable floors. Employee contributions are KGS 5000 and employer contributions KGS 1125. With a KGS 650 personal deduction, PIT is KGS 4435 and net salary KGS 40565. Employer total cost is KGS 51125.

```oa-check
name: Ordinary business payroll above both floors
inputs:
  salary: 50000
  indicator: 100
steps:
  - employee_social: salary * 0.10
  - employer_social: salary * 0.0225
  - pit_base: salary - employee_social - 6.5 * indicator
  - pit: pit_base * 0.10
  - net_salary: salary - employee_social - pit
  - employer_cost: salary + employer_social
expected:
  employee_social: 5000
  employer_social: 1125
  pit: 4435
  net_salary: 40565
  employer_cost: 51125
```

For a full month below both applicable ordinary-business floors, suppose salary is KGS 15000 and the hypothetical district average is KGS 20000. Employer social contributions use KGS 20000; employee contributions use actual pay. Actual PIT base after deductions is KGS 12850: the worker pays KGS 1285 and the employer funds KGS 715 of PIT. Assume this is the first actual month, all floor conditions apply, no exceptions and no cap.

```oa-check
name: Employer funds social floor and PIT shortfall
inputs:
  salary: 15000
  district_average: 20000
  indicator: 100
steps:
  - employee_social: salary * 0.10
  - employer_social: max(salary, district_average) * 0.0225
  - actual_pit_base: salary - employee_social - 6.5 * indicator
  - employee_pit: actual_pit_base * 0.10
  - employer_funded_pit: max(0, district_average - actual_pit_base) * 0.10
  - net_salary: salary - employee_social - employee_pit
  - employer_cost: salary + employer_social + employer_funded_pit
expected:
  employee_social: 1500
  employer_social: 450
  actual_pit_base: 12850
  employee_pit: 1285
  employer_funded_pit: 715
  net_salary: 12215
  employer_cost: 16165
```

## Ask the client first

- Employer legal form, exact activity/licence and any specialist regime.
- Worker status, pension/disability category, nationality and treaty coverage.
- Employment dates, concurrent jobs, hours/days and district/city.
- Accrued and paid salary, benefits, contribution exclusions and relief documents.
- Applicable published district and national averages, prior cumulative months and cap position.
- Prior reports, insured-person identifiers and payments/corrections.

## Sources

| Source and scope actually read | URL | Read on |
|---|---|---|
| Tariffs Act No8, consolidated through 22 July 2026. Read for arts1,2,2-1,2-2,13,14,14-1: categories, rates, floors, cap and foreign employees | https://cbd.minjust.gov.kg/4-1330/edition/latest/ru | 2026-11-15 |
| Social Insurance Act No20, current consolidated text. Read for arts24-26: payment timing, control, arrears and interest | https://cbd.minjust.gov.kg/627/edition/latest/ru | 2026-11-15 |
| Instruction under Cabinet Resolution729, consolidated through 21 July 2026. Read for paras2,5-10,18-28,52,70,75-76: wage fund, cap, current reporting, payment and historical distinctions | https://cbd.minjust.gov.kg/230020107/edition/latest/ru | 2026-11-15 |
| Tax Code No3. Read for arts18,53,82,100,163,185-188,194-203: salary tax, floors, deductions, agent obligations and liability | https://cbd.minjust.gov.kg/112340/edition/latest/ru | 2026-11-15 |
| Resolution1115-III. Read for KGS100 calculation indicator | https://cbd.minjust.gov.kg/51948/edition/latest/ru | 2026-11-15 |

Not yet confirmed: actual current-year district/city and national average-wage amounts; current live report identifier/fields, payment references and high-pay cap allocation in the filing system; specialist HTP, agricultural, garment/textile and entrepreneur computations. The seed universal higher employer rate and no-cap statement are replaced by the current category rules and art13(4).
