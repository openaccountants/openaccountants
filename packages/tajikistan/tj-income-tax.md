---
name: tj-income-tax
description: "Compute 2026 Tajikistan resident main-job and other individual income tax; distinguish non-resident employment, personal deductions, social tax and annual filing. Produces a review working paper, with special regimes and live return fields held for confirmation."
jurisdiction: TJ
tax_year: 2026
last_updated: 2026-11-15
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
category: international
type: computation
version: 0.1
---

# Tajikistan personal income tax v0.1

> **General reference only.** This skill prepares a working paper for review by a qualified Tajikistan professional. Confirm the facts, source version and filing procedure before filing, paying or taking a tax position.

**Built from the law. Not yet approved.** Tax year 2026; checked on 2026-11-15.


## Scope

Use for an individual under the ordinary income-tax rules. Residents have worldwide-income exposure; non-residents have Tajik-source exposure. An entrepreneur within a special regime needs that regime checked before this computation. [Tax Code arts. 180-182](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).

The employment rates below replace the old 8% / 13% bands and the old 25% non-resident estimate. They are distinct categories, not progressive wage bands. [Art. 183](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).


## Ask the client first

- Tax year, citizenship, day-by-day presence, arrival/departure history, permanent residence and any foreign residence certificate.
- Main or additional job, employer category, days employed in the month, and evidence of any enhanced personal deduction.
- Cash wages, benefits in kind, other income, foreign income and amounts already withheld.
- Employee social tax actually withheld, exemption evidence and whether income falls under a special regime.
- Foreign accounts, annual-return triggers, cashless-expense claims and the current official return supplied by the filer.


## The method, step by step


### Establish residence and source

The presence test is more than 182 days in any 12-month period beginning or ending in the current calendar year. First-year and departure-year rules can restrict the resident part of the year. Citizenship, state service abroad and certain citizenship/permanent-residence applications are additional residence grounds; foreign diplomatic/consular, international-organisation and foreign-state-service exceptions need separate review. Do not decide residence from days alone. [Art. 14(2)-(6)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).


### Select the category before calculating

| Item and conditions | 2026 rate or amount | Official provision |
|---|---|---|
| Resident individual, main employment | 12% on taxable main-job income after permitted deductions | [Art. 183(1)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) |
| Non-resident individual, Tajik-source employment | 20%; do not apply the resident personal allowance | [Art. 183(2), 191(1)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) |
| Individual income outside those employment categories, unless a specific rule or special regime controls | 15%, without art. 191 deductions except employee social tax | [Art. 183(3)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) |
| Calculation indicator | TJS 78 from 1 January 2026 | [Budget Law art. 24(1)](https://sadoimardum.tj/1296-onuni-umurii-toikiston-dar-borai-bueti-davlatii-umurii-toikiston-baroi-soli-2026-2203.html) |
| Ordinary resident main-job monthly personal deduction | 2 indicators (in words on the page); TJS 156 derived as 2 × 78. No deduction if employed for fewer than 16 calendar days in the month (in words on the page); only the main job receives it | [Art. 191(1), (4)-(5)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) and [Budget Law art. 24(1)](https://sadoimardum.tj/1296-onuni-umurii-toikiston-dar-borai-bueti-davlatii-umurii-toikiston-baroi-soli-2026-2203.html) |
| Enhanced resident main-job monthly personal deduction | 10 indicators for the specifically listed qualifying groups; TJS 780 derived as 10 × 78. Use the larger eligible deduction, with evidence, rather than adding deductions | [Art. 191(2)-(3)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) and [Budget Law art. 24(1)](https://sadoimardum.tj/1296-onuni-umurii-toikiston-dar-borai-bueti-davlatii-umurii-toikiston-baroi-soli-2026-2203.html) |

For the enhanced deduction, art. 191(2) lists the specified national/Soviet heroes, war participants and equivalent persons, Group II disabled persons, and specified persons affected by or involved in nuclear accidents. Check the exact statutory category and documents; do not extend it to everyone receiving a pension. [Art. 191(2)-(3)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).


### Build the base and compute

Start with taxable wages and benefits in cash, tangible or intangible form under art. 186. Identify an actual art. 189 exemption before excluding an item. State and insurance pensions and qualifying state benefits are exempt; the existence of an exempt pension does not exempt new employment wages. [Arts. 186, 189(1)(4)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).

Deduct the employee social tax withheld under art. 332(2), rather than assuming the old universal employee rate. Load [tj-payroll-social](tj-payroll-social.md) for the employer category and social-tax base. At the main job, also subtract the eligible personal deduction; apply the category rate to the remaining taxable amount. Keep the base at zero if deductions exceed taxable wages. [Arts. 183, 191(1)-(6)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).

Other individual taxable income requires its own income/source and deduction analysis under arts. 180-192. Do not turn the ordinary employment computation into a self-employed special-regime return. A claim for qualifying documented domestic cashless expenditure under art. 191(8) is an annual-return issue; confirm its implementing procedure before claiming it. [Arts. 180, 191(8), 241(4)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).


### Filing and payment handoff

Employment withholding has a calendar-month period. The employer files the unified income/social-tax declaration by the 15th of the following month. The payment rule also requires withholding payment when bank funds are obtained for wages; a following-month filing deadline is not permission to delay that payment. [Arts. 236(5)-(6), 240(1), 241(1)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf). For Code filing/payment deadlines, day periods are calendar days unless working days are specified; if the final day is a holiday or non-working day, the deadline moves to the following working day. [Art. 4(6)-(7)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).

The annual return is due by 1 April after the reporting year for persons within art. 241(4), including residents with income not taxed at a Tajik payment source, residents receiving foreign income, the stated foreign-account trigger, and non-residents with taxable Tajik income not withheld at source. A salary-only person is not automatically an annual filer. Individual income-tax payment under art. 243(1) is due by the 15th after the calendar month in which income was received; the old blanket 10 April final-payment instruction is not the individual rule. [Arts. 241(4), 243(1)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).

Prepare a schedule showing income category, source, exempt items and evidence, employee social tax, personal deduction, taxable amount, tax and withholding credits. Reconcile it to the employer certificate or annual return. Obtain the current official form and its fields through the Tax Committee [personal cabinet](https://www.andoz.tj/) or the competent local office; retain the submission receipt and payment reconciliation. Live form fields have not been read for this skill, so this is a computation handoff rather than authority to submit.


## Worked cases


### Ordinary main job: personal deduction applies

Illustrative resident, ordinary private-sector main job, employed throughout the month: taxable gross TJS 5,000; employee social tax TJS 100 under the payroll skill. The personal deduction is 2 × 78 = TJS 156. Taxable base is 5,000 − 100 − 156 = TJS 4,744; tax is TJS 569.28; net pay is TJS 4,330.72. Inputs assume no other exemption or deduction.

```oa-check
name: Resident main-job monthly computation
inputs:
  gross: 5000
  employee_social: 100
  indicator: 78
steps:
  personal_deduction: 2 * indicator
  taxable: max(0, gross - employee_social - personal_deduction)
  tax: taxable * 0.12
  net: gross - employee_social - tax
expected:
  personal_deduction: 156
  taxable: 4744
  tax: 569.28
  net: 4330.72
```


### Main job or additional job changes the answer

Illustrative resident receives TJS 2,000, with TJS 40 employee social tax. If this is the qualifying main job with enough days, the base is TJS 1,804 and tax TJS 216.48. If it is additional employment under art. 183(3), no personal deduction applies: base TJS 1,960, tax TJS 294. The category difference is TJS 77.52; do not let the employee choose the main-job treatment for both jobs.

```oa-check
name: Main versus additional employment
inputs:
  gross: 2000
  employee_social: 40
  indicator: 78
steps:
  main_base: max(0, gross - employee_social - 2 * indicator)
  main_tax: main_base * 0.12
  additional_base: gross - employee_social
  additional_tax: additional_base * 0.15
  difference: additional_tax - main_tax
expected:
  main_base: 1804
  main_tax: 216.48
  additional_base: 1960
  additional_tax: 294
  difference: 77.52
```


## When to refuse or refer

Refer residence conflicts, treaties, special entrepreneurial regimes, disputed benefit valuation, unusual exemption claims and an unverified enhanced/cashless deduction. Do not compute from net pay alone or invent a lower wage band. Stop the filing handoff until the current official declaration and any foreign-tax-credit evidence have been matched.


## Sources

| Official source | Read for | Date read |
|---|---|---|
| [Tax Committee, current consolidated Tax Code](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) | Read for arts. 4(6)-(7), 14, 180-183, 186, 189(1)(4), 190-192, 236(4)-(6), 240-243; rate and period distinctions. | 2026-11-15 |
| [Parliamentary publication, 2026 State Budget Law](https://sadoimardum.tj/1296-onuni-umurii-toikiston-dar-borai-bueti-davlatii-umurii-toikiston-baroi-soli-2026-2203.html) | Read for art. 24(1), 2026 calculation indicator. | 2026-11-15 |

Not yet confirmed: Live declaration fields and the cashless-expense implementing procedure; the client-specific foreign-account trigger, treaty/foreign-credit computation and special-regime return; detailed non-wage exemption calculations. The earlier 8% low-wage band, 13% resident rate, 25% non-resident rate and TJS 75 allowance are superseded, not alternative 2026 instructions.
