---
name: azerbaijan-social-contributions
description: 'Use this skill for 2026 Azerbaijan compulsory social, medical and unemployment contribution working papers. It covers employee and employer schedules, private non-oil employer classification, the social band above AZN 8000, the medical band at AZN 2500, ordinary entrepreneur floors and ceilings, civil-contract providers, professional and fixed social categories, payment dates and quarterly reporting. Trigger on Azerbaijan social contributions, DSMF, SSPF, medical insurance, unemployment insurance, entrepreneur social tax and payroll deductions. Use the payroll skill for income tax and net pay. Technology-park elections and foreign-worker exclusions require eligibility evidence. Subsidy claims and informal-worker medical assessments are outside implemented scope. Checked against the law (tier 2); no accountant has signed it off.'
version: 0.2
jurisdiction: AZ
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Azerbaijan Social, Medical and Unemployment Contributions v0.2

> **Checked against the law.** Tax year 2026. Figures independently re-checked against the official sources on 31 October 2026. General reference for working papers; a qualified professional must review the facts and filing position. No accountant has signed this skill off.

## Who this applies to

Employers, employees, entrepreneurs and the non-employment categories expressly covered by the Social Insurance, Unemployment Insurance and Medical Insurance laws. These are separate charges with different bases. Income-tax residence or an income-tax exemption does not establish exemption from contributions. This skill calculates ordinary payroll, ordinary entrepreneurs, civil-contract service providers and statutory professional categories. Pension/benefit entitlement is outside scope.

Classify the employer under [Cabinet Decision 56, paragraphs 2.1–2.2](https://www.taxes.gov.az/az/post/321), not the employee's job title. SOCAR group and specified PSA/pipeline contractors/operators are oil/gas employers. An existing subcontractor crosses the criterion if prior-year receipts from the specified parties exceed 50% of total receipts; the new-subcontractor cumulative test can remove preferential status from the following month for the rest of the year. The non-state definition excludes public entities, budget-funded bodies and entities at least 51% directly or indirectly state-owned. Retain customer, turnover and ownership evidence.

## Rates, bands and thresholds

Use AZN and the monthly statutory base for each charge. All social and unemployment rates below are uncapped unless a specific statutory rule says otherwise.

| Item | Monthly calculation | Tax year | Official source |
|---|---|---|---|
| Standard social insurance | Employee 3%; employer 22% | 2026 | [Social Insurance Law art. 14.3](https://frameworks.e-qanun.az/3/f_3813.html) |
| Private non-oil social, income up to 200 | Employee 3%; employer 22% | 2026 | [Social Insurance Law art. 14.4](https://frameworks.e-qanun.az/3/f_3813.html) |
| Private non-oil social, over 200 through 8,000 | Employee 6 + 10% of excess over 200; employer 44 + 15% of excess over 200 | 2026 | [Social Insurance Law art. 14.4](https://frameworks.e-qanun.az/3/f_3813.html) |
| Private non-oil social, over 8,000 | Employee 786 + 10% of excess over 8,000; employer 1,214 + 11% of excess over 8,000 | 2026 | [Social Insurance Law art. 14.4](https://frameworks.e-qanun.az/3/f_3813.html) |
| Unemployment | Employee 0.5%; employer 0.5% of their statutory wage bases | 2026 | [Unemployment Insurance Law art. 9](https://frameworks.e-qanun.az/36/f_36310.html) |
| Standard medical, each side separately | 2% up to 8,000 plus 0.5% above | 2026 | [Medical Insurance Law art. 15-10.1.2](https://frameworks.e-qanun.az/0/f_80.html) |
| Private non-oil medical, each side separately | 2% up to 2,500 plus 0.5% above | From 1 Jan 2026 | [Medical Insurance Law art. 15-10.1.2-1](https://frameworks.e-qanun.az/0/f_80.html) |

| Non-employment item | Calculation | Tax year | Official source |
|---|---|---|---|
| Ordinary entrepreneur social | 2% of gross income, minimum 15% and maximum 100% of monthly minimum wage | 2026 | [Social Insurance Law art. 14.5.1](https://frameworks.e-qanun.az/3/f_3813.html) |
| Non-entrepreneur civil-contract provider | Withhold 25% of income as social insurance | 2026 | [Social Insurance Law art. 14.5.2](https://frameworks.e-qanun.az/3/f_3813.html) |
| Author remuneration social | Withhold 15% | 2026 | [Social Insurance Law art. 14.5.4](https://frameworks.e-qanun.az/3/f_3813.html) |
| Bar members and independent mediators social | 15% of income less expenses | 2026 | [Social Insurance Law art. 14.5.5](https://frameworks.e-qanun.az/3/f_3813.html) |
| Private notary / private enforcement officer social | 25% of 10 / 5 times minimum monthly wage | 2026 | [Social Insurance Law arts. 14.5.3–14.5.3-1](https://frameworks.e-qanun.az/3/f_3813.html) |
| Registered self-insured individual's medical | 4% of minimum monthly wage | 2026 | [Medical Insurance Law arts. 15-2.2.2, 15-10.1.3](https://frameworks.e-qanun.az/0/f_80.html) |
| Civil-contract provider's medical | 2% of income through 8,000 plus 1% above | 2026 | [Medical Insurance Law arts. 15-2.2.3, 15-10.1.4](https://frameworks.e-qanun.az/0/f_80.html) |
| Minimum monthly wage used in these calculations | 400; ordinary entrepreneur social floor 60/ceiling 400; registered individual's medical 16 | 2026 | [Ministry 2026 social indicators](https://sosial.gov.az/az/faydali/sosial-odenisler); statutory percentages above |

## The base

For payroll, determine gross salary, taxable benefits, bonuses and each statutory exclusion independently. Social Insurance Law art. 15 covers all remuneration/income except its listed exclusions. It excludes genuine business-expense reimbursements, specified statutory termination payments, compulsory and qualifying insurance payments, non-employment/non-business passive income and other listed items. Cash salary is not the only base. A PIT allowance of 200 does not reduce social or medical wage bases. Unemployment uses the employer wage fund and employee wages under art. 9. Medical uses the statutory employee remuneration under art. 15-10.

For a private non-oil employee with social base B, calculate employee social as 3% of min(B,200) + 10% of max(B−200,0). Employer social is 22% of min(B,200) + 15% of min(max(B−200,0),7,800) + 11% of max(B−8,000,0). This reproduces all three 2026 statutory rows. For standard employers use 3%/22%. Medical is calculated separately for each side: 2% of min(M,2,500) + 0.5% of max(M−2,500,0) for private non-oil employees, or the same formula with 8,000 for standard employees. Unemployment is 0.5% on each side's base. Employer charges are additional employer expense; only employee charges reduce net pay. Use azerbaijan-payroll for PIT and the final net-pay reconciliation.

An ordinary entrepreneur computes monthly social as min(minimum wage, max(15% of minimum wage, 2% of gross income)). Expenses do not reduce this base. Add the separate 4%-of-minimum-wage medical payment while within art. 15-2.2.2, except a properly recorded suspension. A civil-contract provider who is not an individual entrepreneur instead has 25% social withheld by the payer, plus medical under the separate civil-contract schedule; do not apply the entrepreneur floor/ceiling to that provider. Do not add employee/employer unemployment insurance to entrepreneurial receipts without an employment relationship. An entrepreneur employing staff has both own-person and employer obligations.

The fixed social categories in art. 14.5.1-1 differ from ordinary entrepreneurs. Solo event performers and individual photo/audio/video services use 8% of minimum wage; listed solo trades/domestic services, hairdressers, tailors and veterinary practice use 5%; domestic passenger transport with the identifying certificate uses 6%. Multiply those non-farming amounts by 2 in Baku, 1.5 in Absheron/Sumgayit/Ganja and 1 elsewhere (art. 14.5.1-2). Farming-family/qualifying land-user contributions instead use the statutory per-person agricultural area bands: up to 5 hectares 5%, over 5 through 10 hectares 7.5%, above 10 hectares 12.5% of minimum wage, subject to the age/disability/other-covered-work exceptions in art. 14.5.1-1.3. The farming category does not receive those geographic multipliers. Verify the activity and receipt/certificate before selecting a fixed category.

Social Insurance Law art. 14.8 permits eligible technology-park activity employees, excluding foreigners/stateless persons, to elect social contributions on four times minimum wage instead of actual covered employment income, applying the relevant art. 14.3/14.4 rates. This runs from 1 January 2023 through 31 December 2032. Written annual election is due by 15 January; mid-year entitlement and new hires follow the distinct rules in that article. Do not substitute the elected social base for the medical, unemployment or PIT base. Amendments under Law 476-VIIQD taking effect on 1 January 2027 are not 2026 rules.

## Deadlines and filing

Calculate social and unemployment monthly and pay with wages/other covered income, no later than the next month's 15th ([Social Law art. 14.6](https://frameworks.e-qanun.az/3/f_3813.html); [Unemployment Law art. 10.3](https://frameworks.e-qanun.az/36/f_36310.html)). Medical payroll and self-insured/civil-contract payments are also monthly, by the next month's 15th ([Medical Law art. 15-11.3–15-11.5](https://frameworks.e-qanun.az/0/f_80.html)). Ordinary contributions are paid without cash as required by Social Law art. 14.6. Obtain the required combined fixed-tax/social/medical receipt or passenger identifying certificate before operating in the fixed categories (Social Law art. 14.6-1; Medical Law art. 15-11.4).

File the unified wage-withholding return quarterly by the next month's 20th. Social Law art. 10, Unemployment Law art. 6.2.11 and Medical Law art. 15-11.3 establish the contribution reporting cycle. A suspension, liquidation or cessation triggers the applicable report within 30 days, without extending the ordinary reporting deadline. Submit through the State Tax Service's electronic system and reconcile each component separately. Tax registration and insured-person registration remain required under the respective statutes; a tax number alone does not evidence all personnel records.

## Penalties and interest

The tax administration procedures apply through Social Law art. 9-1.1, Unemployment Law art. 7 and Medical Law art. 15-24.1. Under [Tax Code art. 57.1](https://e-qanun.az/frameworks/46/f_46948.html), failure without grounds to submit a required return for a period with taxable or exempt operations or tax objects attracts AZN 40. Under [Tax Code art. 58.1](https://e-qanun.az/frameworks/46/f_46948.html), an understated or evaded tax amount attracts a 50% financial sanction, excluding additional tax assessed by a desk audit; the horizontal-monitoring case in art. 58.1-1 uses 25%. Under [Tax Code art. 59.1–59.2](https://e-qanun.az/frameworks/46/f_46948.html), late tax or advance payments bear 0.1% per overdue day, for at most one year. For additional tax identified by field audit or horizontal monitoring, interest starts on the assessment date under art. 59.2. Apply the facts and procedural exceptions before assessing a sanction.

Do not transfer the additional-insurance-charge rule for informal workers in Medical Law art. 15-11.10–15-11.11 to normal wage contributions. Its category and commencement are distinct.

## Cross-border points

Social Law art. 12 includes foreigners/stateless persons receiving Azerbaijan-source remuneration, with specified PSA and technology-park exclusions. The technology-park foreign-worker exclusion runs from 1 January 2023 for ten years and requires the exact activity/employer/contractor chain in art. 12. Income-tax treaty relief does not by itself remove social, unemployment or medical charges. Medical Law art. 15-2 defines covered persons and exceptions for foreign nationals; test the employment/registered/civil-contract category rather than presuming all foreigners exempt. Obtain the employment facts and any applicable social-security agreement before departing from domestic contributions.

Social Law art. 14-1 subsidises eligible paid contributions for specified liberated-territory and Nakhchivan activities. For non-state employers resident in the liberated territories (art. 14-1.1, with the listed sector exclusions), the state reimburses this share of the employer social insurance paid under arts. 14.3–14.4: 100% to 31 December 2025, 80% from 1 January 2026 to 31 December 2028, 60% in 2029–2030 and 40% in 2031–2032; entrepreneurs' own art. 14.5.1 and fixed art. 14.5.1-1 contributions there are reimbursed in full. For qualifying non-state Nakhchivan producers (excluding oil and gas), the employer share is 100% in 2026–2028, 80% in 2029–2031, 60% in 2032–2033 and 40% in 2034–2035 (art. 14-1.1-1). This is not a general private-sector subsidy: the old version of this skill applied the liberated-territory schedule to every private employer, which the law does not support. A subsidy is a subsequent reimbursement under the statutory process, not permission to omit payroll assessment or payment. Claim calculations are outside this ordinary contribution computation.

## Two worked examples that recompute

### Private non-oil employee, monthly gross 1,000

Assume all gross pay is in all three bases. Employee social is 86, medical 20 and unemployment 5, totalling 111. Employer social is 164, medical 20 and unemployment 5, totalling 189. PIT is separate.

```oa-check
name: AZ private non-oil contributions 1000 in 2026
inputs:
  gross: 1000
steps:
  - employee_social: min(gross,200)*0.03 + max(gross-200,0)*0.10
  - employer_social: min(gross,200)*0.22 + min(max(gross-200,0),7800)*0.15 + max(gross-8000,0)*0.11
  - medical_each: min(gross,2500)*0.02 + max(gross-2500,0)*0.005
  - unemployment_each: gross*0.005
  - employee_total: employee_social+medical_each+unemployment_each
  - employer_total: employer_social+medical_each+unemployment_each
expected:
  employee_social: 86
  employer_social: 164
  employee_total: 111
  employer_total: 189
```

### Entrepreneur at the floor

Assume an active ordinary entrepreneur has only 1,000 monthly gross receipts and minimum wage is 400. Two percent of receipts is 20, below the social floor of 60. Social is 60 and medical is 16, totalling 76. The lower profit after expenses does not change the social floor.

```oa-check
name: AZ entrepreneur floor 2026
inputs:
  receipts: 1000
  minimum_wage: 400
steps:
  - social: min(minimum_wage,max(minimum_wage*0.15,receipts*0.02))
  - medical: minimum_wage*0.04
  - total: social+medical
expected:
  social: 60
  medical: 16
  total: 76
```

## Ask the client first

- Is this employment, registered entrepreneurship, civil-contract work, author remuneration or a statutory profession/fixed activity?
- What evidence supports sector classification, ownership and oil/gas customer turnover?
- What payments/benefits and statutory exclusions enter each contribution base?
- Are there foreign workers, a PSA, technology-park documents or an annual election?
- What are monthly receipts, minimum-wage periods, location, farmland area and suspension dates?
- What contribution payments, payroll reports or subsidy claims already exist?

## Sources

| Source and provisions read | Official URL | Read on |
|---|---|---|
| Social Insurance Law, arts. 9-1–15 | https://frameworks.e-qanun.az/3/f_3813.html | 2026-10-31 |
| Medical Insurance Law, arts. 15-2, 15-10–15-11, 15-24 | https://frameworks.e-qanun.az/0/f_80.html | 2026-10-31 |
| Unemployment Insurance Law, arts. 3, 6–10 | https://frameworks.e-qanun.az/36/f_36310.html | 2026-10-31 |
| Tax Code, arts. 57–59 | https://e-qanun.az/frameworks/46/f_46948.html | 2026-10-31 |
| Cabinet Decision 56, employer-sector criteria | https://www.taxes.gov.az/az/post/321 | 2026-10-31 |
| Ministry, 2026 social indicators | https://sosial.gov.az/az/faydali/sosial-odenisler | 2026-10-31 |

Not yet confirmed: Informal-worker medical-category commencement and implementing amount; the claim procedure for territorial contribution subsidies (art. 14-1.2 leaves it to an implementing body); a social-insurance exemption for foreign diplomatic staff (stated by the old version of this skill from a secondary source; Social Law art. 12 names only the PSA and technology-park exclusions). These are excluded from computations, not assumed zero.

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
