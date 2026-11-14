---
name: us-hsa-form-8889
description: >
  Compute 2026 health savings account limits, the deduction, and taxable
  distributions under section 223 and Form 8889. Covers who is an eligible
  individual, the self-only and family contribution limits, the high deductible
  health plan thresholds, the age-55 catch-up, the last-month rule and its
  testing period, employer contributions, qualified distributions, the 20 percent
  additional tax, and the 6 percent tax on excess contributions. Includes the
  2026 rules for telehealth, bronze and catastrophic Marketplace plans, and
  direct primary care arrangements. Trigger on HSA, Form 8889, health savings
  account, HDHP, catch-up contribution. Federal only, tax year 2026.
version: "1.0"
jurisdiction: US
category: federal
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Health savings accounts and Form 8889, tax year 2026

> **Source-cited draft.** Built from Rev. Proc. 2025-19, 26 U.S.C. 223 (United States Code, 2024 edition), 26 U.S.C. 219(f)(3), 26 U.S.C. 4973, 42 U.S.C. 1395c, and Public Law 119-21 sections 71306, 71307 and 71308, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026 an eligible individual may contribute up to USD 4,400 for self-only high deductible health plan coverage or USD 8,750 for family coverage, plus USD 1,000 if the individual is age 55 or older by year end. The plan's deductible must be at least USD 1,700 (self-only) or USD 3,400 (family), and out-of-pocket costs cannot exceed USD 8,500 or USD 17,000, unless a Marketplace bronze or catastrophic plan is treated as a high deductible health plan under the 2026 rule below. A distribution not used for qualified medical expenses is included in income and, unless an exception applies, is also subject to 20 percent additional tax. Employer contributions that are excluded from income are not deducted again.

## Scope and who this is for

In scope: a 2026 health savings account of an individual eligible under section 223, the deduction, employer contributions, and distributions, including the results that Form 8889 reports.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Deducting Marketplace or other premiums as self-employed health insurance | `us-self-employed-health-insurance` |
| Premium tax credit on a Marketplace plan | `us-premium-tax-credit-8962` |
| Where the HSA deduction sits on Form 1040 | `us-form-1040-individual-return` |

## Ask the client first

1. **Coverage on the first day of each month:** self-only high deductible health plan, family coverage, or neither, and whether a Marketplace bronze or catastrophic plan is the coverage.
2. **Other coverage** in any month (Medicare, a general-purpose health flexible spending arrangement, or a spouse's plan that is not a high deductible health plan).
3. **Age at year end**, and whether a spouse also has a health savings account or family coverage.
4. **Contributions:** amounts the individual paid, amounts the employer contributed and excluded, and Archer MSA or IRA-to-HSA funding. Contributions for 2026 may be made up to the unextended due date of the 2026 return.
5. **Distributions** and whether each one paid qualified medical expenses. Date of birth if the 20 percent tax might be off because of age, disability, or death.
6. **Last-month rule:** if coverage started late in 2026, whether the individual will stay eligible through 31 December 2027.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Contribution limit, self-only coverage | USD 4,400 | [Rev. Proc. 2025-19, section 2.01](https://www.irs.gov/pub/irs-drop/rp-25-19.pdf) |
| Contribution limit, family coverage | USD 8,750 | same |
| High deductible health plan, minimum annual deductible | USD 1,700 self-only; USD 3,400 family | same |
| High deductible health plan, maximum out-of-pocket | USD 8,500 self-only; USD 17,000 family | same |
| Additional contribution if age 55 or older before year end | USD 1,000 | [26 U.S.C. 223(b)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec223.htm) |
| Additional tax on a taxable distribution | 20 percent | [26 U.S.C. 223(f)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec223.htm) |
| Additional tax if the last-month rule is failed | 10 percent of the income included | same |
| Tax on excess contributions still in the account | 6 percent | [26 U.S.C. 4973](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleD-chap43-sec4973.htm) |
| Direct primary care fee that still leaves the person eligible, per month | USD 150; twice that if the arrangement covers more than one person | [Public Law 119-21, section 71308](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Rollover into another health savings account | within 60 days, and not more than once in a 1-year period | [26 U.S.C. 223(f)(5)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec223.htm) |

The USD 1,000 catch-up is the statutory amount for 2009 and years after. It is not an inflation-adjusted figure in Rev. Proc. 2025-19. Out-of-pocket costs for the high deductible health plan test are deductibles, co-payments, and other amounts, but not premiums.

The direct primary care dollar cap is not adjusted for inflation for a taxable year beginning in 2026. The inflation adjustment for that cap starts with taxable years beginning after 2026. Source: [Public Law 119-21, section 71308(c)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).

### Who is eligible, month by month

An individual is eligible for a month if, on the first day, they are covered by a high deductible health plan and are not covered by another plan that pays benefits the high deductible plan covers. Disregarded coverage includes permitted insurance, accidents, disability, dental, vision, long-term care, and a limited health flexible spending arrangement carryover. A person claimed as someone else's dependent cannot deduct a contribution. Source: [26 U.S.C. 223(b)(6) and (c)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec223.htm).

For months beginning after 31 December 2025, an individual-market bronze or catastrophic plan bought through an Exchange is a high deductible health plan even if its deductible or out-of-pocket maximum would not otherwise meet the dollar tests. The contribution limit is still the self-only or family limit above, based on the coverage. Source: [Public Law 119-21, section 71307](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).

For plan years beginning after 31 December 2024, a plan does not fail to be a high deductible health plan because it has no deductible for telehealth and other remote care, and that telehealth coverage is disregarded. Source: [Public Law 119-21, section 71306](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).

For months beginning after 31 December 2025, a direct primary care service arrangement is not a health plan that blocks eligibility if the only compensation is a fixed periodic fee at or under the monthly cap in the table, and the care is primary care within the limits in section 71308. Fees for that arrangement can be qualified medical expenses. Source: [Public Law 119-21, section 71308](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).

The monthly limit is zero for the first month the individual is entitled to Medicare (title XVIII of the Social Security Act) and every later month. The hospital-insurance program in that title covers individuals who are age 65 or over (and certain others). Source: [26 U.S.C. 223(b)(7)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec223.htm); [42 U.S.C. 1395c](https://www.govinfo.gov/content/pkg/USCODE-2023-title42/html/USCODE-2023-title42-chap7-subchapXVIII-partA-sec1395c.htm).

### The contribution limit and the deduction

1. For each eligible month, the monthly limit is one-twelfth of USD 4,400 (self-only on the first day of the month) or USD 8,750 (family coverage on the first day). Add the months.
2. If the individual is an eligible individual on the first day of December, they may instead be treated as eligible for every month of the year under the December coverage. That is the last-month rule. If they are not eligible for any month in the testing period (December of the contribution year through 31 December of the next year), the contributions that the rule allowed, and that the months of actual eligibility would not have allowed, are included in income for the year of the first failed month, and the tax increases by 10 percent of that inclusion. Death or disability during the testing period turns the extra tax off. Source: [26 U.S.C. 223(b)(8)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec223.htm).
3. Add USD 1,000 if the individual is age 55 or older before the end of the year. Each spouse who is 55 or older has their own USD 1,000. It is not split.
4. If either spouse has family coverage, both are treated as having family coverage (the plan with the lower deductible, if the plans differ). The family limit, before either catch-up, is split equally unless the spouses agree on a different split. Source: [26 U.S.C. 223(b)(5)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec223.htm).
5. Reduce the limit, not below zero, by Archer MSA contributions, by employer health savings account contributions excluded under section 106(d), and by IRA funding rolled to the account under section 408(d)(9). The excluded employer amount is not also deducted. Source: [26 U.S.C. 223(b)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec223.htm).
6. A contribution made by the unextended due date of the return, and designated for that year, is treated as made on the last day of that year. Extensions do not move this date. Source: [26 U.S.C. 223(d)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec223.htm), applying [26 U.S.C. 219(f)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec219.htm).

The deduction is the amount paid in cash to the account, limited as above. It is an adjustment to income, not an itemized deduction.

### Distributions

A distribution used for qualified medical expenses of the beneficiary, spouse, or dependent is not included in income. Qualified medical expenses are medical care under section 213(d) that insurance did not pay, including menstrual care products. Health insurance premiums are not qualified medical expenses, except continuation coverage required by federal law, a qualified long-term care contract, a health plan while the individual receives unemployment compensation, and, after the individual has reached the age in section 1811 of the Social Security Act, health insurance other than a Medicare supplement. Source: [26 U.S.C. 223(d)(2) and (f)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec223.htm).

Any other distribution is included in income. The tax increases by 20 percent of the included amount, unless the distribution is after the beneficiary becomes disabled (section 72(m)(7)), dies, or reaches the age in section 1811 (age 65 for the hospital-insurance program). An amount included in income is still included after that age. Only the 20 percent is off. Source: [26 U.S.C. 223(f)(2) and (f)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec223.htm).

Do not also deduct the same expense on Schedule A. A rollover to another health savings account within 60 days is not included, and the once-a-year limit applies. A transfer to a spouse or former spouse under a divorce or separation instrument is not taxable.

Section 4973 imposes a tax of 6 percent of excess contributions to a health savings account, determined as of the close of the taxable year, and not more than 6 percent of the account's value at that close. An excess contribution (other than a rollover) is one that is neither excluded under section 106(d) nor deductible under section 223. A withdrawal of the excess, plus the earnings on it, by the due date of the return including extensions, keeps section 223(f)(2) from including the excess itself. The earnings are income in the year received. Source: [26 U.S.C. 4973](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleD-chap43-sec4973.htm); [26 U.S.C. 223(f)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec223.htm).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Covered by a non-high-deductible plan on the first day of the month | That month's limit is zero, unless the other plan is disregarded coverage |
| Entitled to Medicare | Limit is zero from that month on. Later distributions are still allowed. The 20 percent tax is off once the section 1811 age is reached |
| Claimed as a dependent | No deduction |
| Spouses and family coverage | One family limit, split equally unless they agree otherwise. Each spouse age 55 or older adds their own USD 1,000 |
| Last-month rule, then coverage ends in the testing period | The extra contribution is income in the year of the first failed month, plus 10 percent, unless the cause is death or disability |
| Bronze or catastrophic Marketplace plan, months after 31 December 2025 | Treated as a high deductible health plan. Contribution limit is still USD 4,400 or USD 8,750 |
| Distribution after age 65 for non-medical costs | Included in income. No 20 percent additional tax |

## Worked cases

**Case 1. Self-only coverage all year, age 56, employer contribution.** The individual is eligible every month of 2026 with self-only coverage and is 56 at year end. The employer contributes USD 1,000, excluded from income under section 106(d). The individual contributes USD 4,400 in cash. No Archer MSA and no IRA funding.

The limit is USD 4,400 plus USD 1,000 = USD 5,400. The excluded employer USD 1,000 reduces that limit for the deduction. The deduction is USD 4,400. Total contributions of USD 5,400 equal the limit, so there is no excess.

```oa-check
name: Self-only HSA with employer contribution and catch-up (2026)
inputs:
  self_only: 4400
  catch_up: 1000
  employer: 1000
  paid_by_individual: 4400
steps:
  - limit: self_only + catch_up
  - deduction_cap: limit - employer
  - deduction: min(paid_by_individual, deduction_cap)
  - excess: paid_by_individual + employer - limit
expected:
  limit: 5400.00
  deduction_cap: 4400.00
  deduction: 4400.00
  excess: 0.00
```

**Case 2, a decision: last-month rule or six months only.** The individual is under 55 and has self-only coverage on the first day of each month from July through December 2026 only (6 months), including 1 December. No employer contribution.

Without the last-month rule the limit is 6/12 of USD 4,400 = USD 2,200. With the rule, December coverage supports a USD 4,400 contribution. The extra USD 2,200 is allowed only if the individual stays eligible through 31 December 2027.

If they contribute USD 4,400 and then fail the testing period, that extra USD 2,200 is included in income for the year of the first failed month, and the tax increases by 10 percent, which is USD 220. Death or disability is the exception. Contribute USD 2,200 if coverage through 2027 is uncertain. Contribute USD 4,400 only if they expect to stay eligible for the whole testing period. The income-tax value of deducting the extra USD 2,200 depends on the bracket in `us-form-1040-individual-return`. The USD 220 is the additional tax on top of that inclusion.

```oa-check
name: Last-month rule against six months of self-only coverage (2026)
inputs:
  annual_limit: 4400
  eligible_months: 6
steps:
  - prorated: annual_limit * eligible_months / 12
  - extra: annual_limit - prorated
  - additional_tax_if_failed: extra * 0.10
expected:
  prorated: 2200.00
  extra: 2200.00
  additional_tax_if_failed: 220.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-HSA-MEDICARE | Medicare entitlement starts mid-year | Stop the limit at the month before entitlement. Do not use the last-month rule for a December in which they are entitled to Medicare |
| R-HSA-SPOUSE | Both spouses have family coverage or both are 55 or older | Split the family limit and give each spouse their own catch-up. Do not double the USD 8,750 |
| R-HSA-EXCESS | Contributions already above the limit | Compute the excess and the earnings. See the note under Sources before telling the client the 6 percent tax is waived |
| R-HSA-FSA | General-purpose health flexible spending arrangement | That coverage usually blocks eligibility. Refer if the arrangement is a limited-purpose or post-deductible design |

## Filing and payment

Contributions designated for 2026 may be made through the unextended due date of the 2026 return. Form 8889 reports the deduction, taxable distributions, and the 20 percent additional tax. The deduction is the section 223 adjustment on Form 1040. Taxable distributions are included in income. The 6 percent tax on an excess that remains is reported with the other additional taxes. The 2026 form's line numbers were not published as a final form when this skill was written. The due date of the return is in `us-form-1040-individual-return`.

## Completion checklist

- Each month tested on the first day, including Medicare and other coverage.
- Self-only USD 4,400 or family USD 8,750, plus USD 1,000 for each person age 55 or older.
- Employer amount excluded under section 106(d) subtracted, and not deducted again.
- Last-month rule used only if December eligibility is real, with the testing period flagged through 31 December 2027.
- Distributions split between qualified medical expenses and taxable amounts, with the 20 percent tax off only for disability, death, or the section 1811 age.
- Spouses did not each take the full family limit.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Rev. Proc. 2025-19, section 2.01. Read for the 2026 limits: self-only contribution USD 4,400, family contribution USD 8,750, deductible not less than USD 1,700 or USD 3,400, out-of-pocket not over USD 8,500 or USD 17,000. | https://www.irs.gov/pub/irs-drop/rp-25-19.pdf | 2026-11-13 |
| 26 U.S.C. 223 (United States Code, 2024 edition). Read for eligibility, the USD 1,000 catch-up for 2009 and after, the married split, the dependent bar, the Medicare cutoff, the last-month rule and 10 percent charge, qualified medical expenses, the 20 percent additional tax, the 60-day rollover, and the rule that applies section 219(f)(3). This edition predates Public Law 119-21. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec223.htm | 2026-11-13 |
| 26 U.S.C. 219(f)(3) (United States Code, 2024 edition). Read for contributions by the unextended filing deadline treated as made on the last day of the prior year. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec219.htm | 2026-11-13 |
| 26 U.S.C. 4973 (United States Code, 2024 edition). Read for the 6 percent tax on excess contributions to a health savings account, capped at 6 percent of the account value, both measured at the close of the taxable year. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleD-chap43-sec4973.htm | 2026-11-13 |
| Public Law 119-21. Read for section 71306 (telehealth safe harbor, plan years beginning after 31 December 2024), section 71307 (bronze and catastrophic plans, months beginning after 31 December 2025), and section 71308 (direct primary care, USD 150 and twice that amount, months beginning after 31 December 2025, inflation adjustment only after 2026). | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| 42 U.S.C. 1395c (United States Code, 2023 edition), which is section 1811 of the Social Security Act. Read for the hospital-insurance program covering individuals who are age 65 or over. | https://www.govinfo.gov/content/pkg/USCODE-2023-title42/html/USCODE-2023-title42-chap7-subchapXVIII-partA-sec1395c.htm | 2026-11-13 |

Not yet confirmed: the final 2026 Form 8889 and its line numbers. Whether a withdrawal of an excess contribution that meets section 223(f)(3) also removes that excess from the section 4973 tax of 6 percent. The 2026 instructions that would tie those two sections together were not published as a final Publication 969 when this was written. The W-2 box and code an employer uses to report its contribution were not read.
