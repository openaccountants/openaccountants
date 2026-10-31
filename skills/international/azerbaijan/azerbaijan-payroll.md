---
name: azerbaijan-payroll
description: 'Use this skill for 2026 Azerbaijan payroll withholding, gross-to-net salary and employer-cost working papers. It covers employer sector classification, standard and private non-oil income-tax schedules, the primary-workplace exemption, personal deductions, social, medical and unemployment deductions, multiple workplaces, monthly payments and quarterly unified reporting. Trigger on Azerbaijan payroll, salary tax, net pay, employer cost, PIT withholding, AZN salary and unified payroll declaration. Use the social-contributions skill for detailed insurance bases, non-employment categories and special elections. Foreign-worker and special-regime cases need their supporting documents. Checked against the law (tier 2); no accountant has signed it off.'
version: 0.2
jurisdiction: AZ
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Azerbaijan Payroll Withholding and Net Pay v0.2

> **Checked against the law.** Tax year 2026. Figures independently re-checked against the official sources on 31 October 2026. General reference for working papers; a qualified professional must review the facts and filing position. No accountant has signed this skill off.

## Who this applies to

Azerbaijan employers and other wage tax agents paying individuals employment income under [Tax Code art. 98, 150.1.1–150.1.2](https://e-qanun.az/frameworks/46/f_46948.html). Run each workplace separately; the sector of the employer and the primary workplace determine the applicable schedule and personal relief. Do not default an unknown employer to the private non-oil regime. Resolve classification first.

Classify the employer under [Cabinet Decision 56, paragraphs 2.1–2.2](https://www.taxes.gov.az/az/post/321), not the employee's job title. SOCAR group and specified PSA/pipeline contractors/operators are oil/gas employers. An existing subcontractor crosses the criterion if prior-year receipts from the specified parties exceed 50% of total receipts; the new-subcontractor cumulative test can remove preferential status from the following month for the rest of the year. The non-state definition excludes public entities, budget-funded bodies and entities at least 51% directly or indirectly state-owned. Retain customer, turnover and ownership evidence.

This skill calculates ordinary gross-to-net pay and employer cost. A registered entrepreneur's profits and an unregistered civil-contract provider's fee are not salaries merely because the payer processes them in a payroll system. The individual and social-contributions skills cover those categories. PSA, free-economic-zone and other special statutory employment regimes require their actual governing documents. Pension, sickness and other benefit entitlements are outside this skill.

## Rates, bands and thresholds

| PIT item | Amount | Tax year / period | Official source |
|---|---|---|---|
| Standard taxable monthly employment income | 14% through 2,500; 350 + 25% above 2,500 | 2026 | [Tax Code art. 101.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Private non-oil taxable monthly income | 3% through 2,500; 75 + 10% over 2,500 through 8,000; 625 + 14% above 8,000 | 1 Jan–31 Dec 2026 | [Tax Code art. 101.1-1.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Later private non-oil lower band | 5% in 2027; 7% from 2028; upper-band base constants also change | 1 Jan 2027 / 1 Jan 2028 | [Tax Code art. 101.1-1.2–101.1-1.3](https://e-qanun.az/frameworks/46/f_46948.html) |
| Primary-workplace general exemption | 200 if monthly income at most 2,500; annual 2,400 if annual income at most 30,000 | 2026 | [Tax Code art. 102.1.6](https://e-qanun.az/frameworks/46/f_46948.html) |
| Martyr-status family monthly deduction | 800 for specified parents, widow(er)s and children | 2026 | [Tax Code art. 102.1-1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Specified hero/veteran/war-disability and related categories | 400 monthly deduction | 2026; new mine-clearer family category from 5 May 2026 | [Tax Code art. 102.2](https://e-qanun.az/frameworks/46/f_46948.html), Law 396-VIIQD commencement annotation |
| Specified disability/caregiver category | 200 monthly deduction | 2026 | [Tax Code art. 102.3](https://e-qanun.az/frameworks/46/f_46948.html) |
| Specified other service/family/displaced-person categories | 100 monthly deduction | 2026 | [Tax Code art. 102.4](https://e-qanun.az/frameworks/46/f_46948.html) |
| At least 3 qualifying dependants | 50 monthly deduction for one spouse; statutory exclusions apply | 2026 | [Tax Code art. 102.5–102.6](https://e-qanun.az/frameworks/46/f_46948.html) |
| Eligible off-park technology-park specialists | 5% of monthly employment income | 1 Jan 2026–31 Dec 2032 | [Tax Code art. 101.7.2](https://e-qanun.az/frameworks/46/f_46948.html) |

| Item | Monthly calculation | Tax year | Official source |
|---|---|---|---|
| Standard social insurance | Employee 3%; employer 22% | 2026 | [Social Insurance Law art. 14.3](https://frameworks.e-qanun.az/3/f_3813.html) |
| Private non-oil social, income up to 200 | Employee 3%; employer 22% | 2026 | [Social Insurance Law art. 14.4](https://frameworks.e-qanun.az/3/f_3813.html) |
| Private non-oil social, over 200 through 8,000 | Employee 6 + 10% of excess over 200; employer 44 + 15% of excess over 200 | 2026 | [Social Insurance Law art. 14.4](https://frameworks.e-qanun.az/3/f_3813.html) |
| Private non-oil social, over 8,000 | Employee 786 + 10% of excess over 8,000; employer 1,214 + 11% of excess over 8,000 | 2026 | [Social Insurance Law art. 14.4](https://frameworks.e-qanun.az/3/f_3813.html) |
| Unemployment | Employee 0.5%; employer 0.5% of their statutory wage bases | 2026 | [Unemployment Insurance Law art. 9](https://frameworks.e-qanun.az/36/f_36310.html) |
| Standard medical, each side separately | 2% up to 8,000 plus 0.5% above | 2026 | [Medical Insurance Law art. 15-10.1.2](https://frameworks.e-qanun.az/0/f_80.html) |
| Private non-oil medical, each side separately | 2% up to 2,500 plus 0.5% above | From 1 Jan 2026 | [Medical Insurance Law art. 15-10.1.2-1](https://frameworks.e-qanun.az/0/f_80.html) |
| Minimum monthly wage | 400 | 2026 | [Ministry of Labour and Social Protection, 2026 social indicators](https://sosial.gov.az/az/faydali/sosial-odenisler) |

## The base

Collect salary, bonuses and employment benefits under art. 98, including former or future employment payments. Value non-cash benefits as that article directs: market value of employer-provided goods/services, the prescribed loan-interest advantage and forgiven employee debt are examples. Genuine business expense reimbursements are excluded under art. 98.3. Do not treat every payment described as compensation as exempt.

Determine statutory exempt amounts under art. 102, then apply any documented primary-workplace deductions. The art. 102.1.6 threshold tests monthly employment income before its 200 exemption; the exemption is unavailable once that income exceeds 2,500. It applies under the 2026 private non-oil schedule as well as the standard schedule. Compute tax on the remaining non-negative taxable base. For the private non-oil schedule, use 3% × min(T,2,500) + 10% × min(max(T−2,500,0),5,500) + 14% × max(T−8,000,0). The constants 75 and 625 are cumulative band tax, not extra taxes added to a full 3%/10% calculation.

Under art. 102.7, a person entitled to multiple deductions in arts. 102.1-1, 102.2, 102.3 and 102.4 receives only the largest of those. The general primary-workplace exemption and the qualifying-dependant deduction are separate statutory tests. Art. 102.5 excludes dependants receiving the specified pensions/stipends/unemployment benefit except children, and those fully maintained by the state (art. 102.6). Keep age, full-time education and household evidence. Apply relief only at the primary workplace and obtain the prescribed proof. Art. 102.8 allows recalculation from the employment contract's effective date where eligible status existed but proof was supplied later. The mine-clearer family category in art. 102.2.9 starts on 5 May 2026; do not backdate that new entitlement into January–April.

Recognise the actual employee status when applying art. 102.2: the 400 category includes specified national heroes, war-disabled persons, statutory veterans, specified survivor families, decorated wartime workers and specified radiation-illness categories. The 200 category in art. 102.3 covers the stated disability percentages/disabled children and specified co-resident carers. The 100 category in art. 102.4 includes specified deceased servicemen/public-servant relatives, persons sent to the stated combat regions and qualifying displaced persons subject to the permanent-resettlement exclusion. These descriptions do not replace the documentary category in the cited article.

Separately calculate social, medical and unemployment charges using their own bases. Do not deduct employee contributions from the PIT base merely because they reduce take-home pay. Use the social-contributions skill for exclusions and non-employment schedules. Net cash pay is gross cash pay minus employee PIT, employee contributions and evidenced other deductions; employer contributions are additional employer cost. Reconcile benefits that increase taxable remuneration without increasing cash paid, rather than reporting them as cash salary.

For multiple workplaces, calculate PIT separately at each workplace under art. 101.1-2; only the primary workplace applies art. 102 relief. An ordinary employed director uses the employment rules on actual employment remuneration. Payments to a director in another legal capacity must be classified under arts. 98–101 and 150 before applying a rate. A tax invoice does not settle worker status.

## Deadlines and filing

Calculate monthly PIT on employment income and remit it no later than the following month's 20th ([Tax Code art. 150.3.1](https://e-qanun.az/frameworks/46/f_46948.html)). This is distinct from contributions: social, medical and unemployment charges are paid with the relevant remuneration and no later than the following month's 15th under Social Law art. 14.6, Medical Law art. 15-11.3 and Unemployment Law art. 10.3.

Submit the unified wage-withholding return, Muzdlu işlə əlaqədar ödəmə mənbəyində tutulmalar üzrə vahid bəyannamə (hesabat), quarterly by the following month's 20th ([Tax Code art. 150.3.3](https://e-qanun.az/frameworks/46/f_46948.html); Social Law art. 10; Medical Law art. 15-11.3; Unemployment Law art. 6.2.11). For example, the ordinary fourth-quarter 2026 due date is 20 January 2027. File through the State Tax Service Internet Tax Office. Correct the affected reporting data where the source facts or relief changes. Art. 71.4 requires at least five years' record retention.

Before work begins, complete the legally required employment contract and electronic personnel procedure. The [State Tax Service's 2026 wage booklet](https://www.taxes.gov.az/uploads/2026/buklet/1_16.pdf), page 1, directs employer and employee confirmation in the labour information system. Contract registration, monthly tax payment and quarterly reporting are separate obligations.

## Penalties and interest

Under [Tax Code art. 57.1](https://e-qanun.az/frameworks/46/f_46948.html), failure without grounds to submit a required return for a period with taxable or exempt operations or tax objects attracts AZN 40. Under [Tax Code art. 58.1](https://e-qanun.az/frameworks/46/f_46948.html), an understated or evaded tax amount attracts a 50% financial sanction, excluding additional tax assessed by a desk audit; the horizontal-monitoring case in art. 58.1-1 uses 25%. Under [Tax Code art. 59.1–59.2](https://e-qanun.az/frameworks/46/f_46948.html), late tax or advance payments bear 0.1% per overdue day, for at most one year. For additional tax identified by field audit or horizontal monitoring, interest starts on the assessment date under art. 59.2. Apply the facts and procedural exceptions before assessing a sanction.

Employers resident in the liberated territories, and qualifying Nakhchivan producers, can have part of the employer social insurance they paid reimbursed by the state under Social Insurance Law art. 14-1 (80% for liberated-territory employers in 2026). It is a reimbursement after payment, not a reduction of the payroll charge; see azerbaijan-social-contributions for the schedule.

Under [Tax Code art. 150.2](https://e-qanun.az/frameworks/46/f_46948.html), the payer is responsible for tax not withheld or remitted, plus the relevant sanctions and interest. Under art. 58.10, using workers before the employment contract takes legal effect in the specified income-concealment circumstances attracts 2,000 per person for the first occurrence in the calendar year, 4,000 for the second and 6,000 for the third or later occurrence. Establish the conduct; do not apply this tax sanction indiscriminately to every personnel error.

## Cross-border points

Foreign employees are not automatically exempt from payroll tax or contributions. Art. 102.1.2's employment exemption for a non-resident requires payment by/on behalf of a non-resident employer and no Azerbaijan PE payment or connection. Apply the actual treaty and domestic facts together. Technology-park/PSA contribution exclusions are distinct from PIT relief. Foreign payroll, home-country social payments or fewer than 183 days in Azerbaijan do not alone determine Azerbaijan withholding. Use the cross-border skill for residence, source and treaty procedure.

## Two worked examples that recompute

### Private non-oil primary job, gross 1,000

Assume all pay is ordinary cash remuneration and there are no special reliefs. PIT is (1,000−200) × 3% = 24. Employee social is 86, medical 20 and unemployment 5; net pay is 865. Employer contributions are 189, giving employer cost 1,189. The 200 PIT exemption does not reduce contributions.

```oa-check
name: AZ private payroll 1000 primary workplace 2026
inputs:
  gross: 1000
steps:
  - pit: max(0,gross-200)*0.03
  - employee_social: 6+(gross-200)*0.10
  - employee_medical: gross*0.02
  - employee_unemployment: gross*0.005
  - net: gross-pit-employee_social-employee_medical-employee_unemployment
  - employer_social: 44+(gross-200)*0.15
  - employer_cost: gross+employer_social+gross*0.02+gross*0.005
expected:
  pit: 24
  net: 865
  employer_cost: 1189
```

### Private non-oil salary above both upper thresholds

At gross 10,000, no general 200 exemption applies. PIT is 625 + 14% × 2,000 = 905. Employee social is 986; medical is 87.50 using the 2,500 threshold; unemployment is 50. Net pay is 7,971.50. Employer social is 1,434 using 11% above 8,000; total employer cost is 11,571.50.

```oa-check
name: AZ private payroll upper bands 2026
inputs:
  gross: 10000
steps:
  - pit: 625+(gross-8000)*0.14
  - employee_social: 786+(gross-8000)*0.10
  - medical_each: 2500*0.02+(gross-2500)*0.005
  - unemployment_each: gross*0.005
  - net: gross-pit-employee_social-medical_each-unemployment_each
  - employer_social: 1214+(gross-8000)*0.11
  - employer_cost: gross+employer_social+medical_each+unemployment_each
expected:
  pit: 905
  employee_social: 986
  medical_each: 87.5
  net: 7971.5
  employer_social: 1434
  employer_cost: 11571.5
```

## Ask the client first

- What confirms employer sector, state ownership and oil/gas customer turnover?
- Which workplace is primary, and what are gross salary, benefits and reimbursement documents?
- What statutory personal-relief status, dependants and proof dates apply?
- Is the recipient an employee, director in another capacity, entrepreneur or civil contractor?
- Are there foreign workdays, non-resident employer/PE facts or special-regime documents?
- What was already paid/reported and did a contract, sector or status change during the year?

## Sources

| Source and provisions read | Official URL | Read on |
|---|---|---|
| Tax Code, arts. 57–59, 71, 98, 101–102, 150; Law 396-VIIQD commencement annotation | https://e-qanun.az/frameworks/46/f_46948.html | 2026-10-31 |
| Social Insurance Law, arts. 9-1–15 (including art. 14-1) | https://frameworks.e-qanun.az/3/f_3813.html | 2026-10-31 |
| Medical Insurance Law, arts. 15-2, 15-10–15-11, 15-24 | https://frameworks.e-qanun.az/0/f_80.html | 2026-10-31 |
| Unemployment Insurance Law, arts. 6–10 | https://frameworks.e-qanun.az/36/f_36310.html | 2026-10-31 |
| Ministry of Labour and Social Protection, 2026 social indicators (minimum monthly wage) | https://sosial.gov.az/az/faydali/sosial-odenisler | 2026-10-31 |
| Cabinet Decision 56, paragraphs 2.1–2.2 | https://www.taxes.gov.az/az/post/321 | 2026-10-31 |
| STS 2026 wage booklet, contract procedure page 1 | https://www.taxes.gov.az/uploads/2026/buklet/1_16.pdf | 2026-10-31 |

Not yet confirmed: which month's schedule applies to pay for December 2025 that is paid in January 2026 (art. 150.3.1 taxes the calculated monthly income; no explicit transition rule was found); whether monthly thresholds are pro-rated for a mid-month joiner or leaver (no pro-rating rule was found in arts. 101–102). Treatment of non-employment corporate-office/director fees outside an employment contract has not been fully resolved; do not calculate them as ordinary salaries by default.

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
