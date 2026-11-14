---
name: global-home-office
description: Home office expense patterns and deduction rules across the top 10 jurisdictions for freelancers and self-employed individuals. Covers simplified and actual methods, rates, requirements, ceilings, and common mistakes.
version: 1.0
jurisdiction: GLOBAL
tax_year: 2026
last_updated: 2026-11-14
category: bookkeeping
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: cross-country-method
checked_on: 2026-11-14
---

# Home office and working from home deductions v1.0

This skill gives a shared method for claiming home office costs and works it through for the United States, the United Kingdom and Canada. Rules are checked on 2026-11-14 for 2026. The latest IRS Publication 587 edition is the 2025 publication, with its edition-specific forms and figures identified below. For any other country, it routes to that country's own Guide and does not state that country's rates. Written by the OpenAccountants team. Use the supplied facts and source-linked rules below; hold any missing eligibility evidence before computing.

## What this skill covers

- Who can claim: the employee versus the self-employed person, which is the first fork in all three worked countries.
- The use tests: exclusive use, regular use, principal place of business, and the meeting-clients alternative.
- The two kinds of method: a simplified or flat-rate amount, and an actual-cost method that apportions real household costs.
- Apportionment: by floor area, by rooms, and by hours where a space is shared.
- What never counts, and the income limits that stop a home office claim creating a loss.

It does not cover capital gains on the sale of a home with a business part, renting your home to your own company, or vehicle costs. For renting your home to your own US business for up to 14 days, see `us-augusta-rule-home-rental-to-your-business`.

## The method, step by step

1. **Decide employee or self-employed.** In all three worked countries the employee rules are narrower than the self-employed rules, and in the US an employee has no federal deduction at all (see the US section, [Public Law 119-21 section 70110](https://www.govinfo.gov/content/pkg/PLAW-119publ21/pdf/PLAW-119publ21.pdf)).
2. **Test the space.** Ask whether a specific area is used only for the work (exclusive use), whether it is used on a regular basis, and whether it is the principal place of business or a place where clients are met. The US tests are in [IRS Publication 587](https://www.irs.gov/publications/p587). Canada's self-employed tests are on the [CRA business-use-of-home page](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/business-use-home-expenses.html). The UK self-employed rules ask for a reasonable split rather than an exclusive-use test ([GOV.UK, expenses if you're self-employed](https://www.gov.uk/expenses-if-youre-self-employed)).
3. **List the method options for that country and that taxpayer.** A simplified amount (US per square foot, UK per month by hours) or actual costs apportioned. Canada has no flat-rate option for 2023 and later years ([CRA, what the changes are](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22900-other-employment-expenses/work-space-home-expenses/what-changes.html)).
4. **Apportion actual costs.** Workspace area divided by total home area, or business rooms divided by total rooms. Where the space is shared with private life, also apply the share of time it is used for work (Canada prints this hours step on its [employee work space page](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22900-other-employment-expenses/work-space-home-expenses/work-space-use.html) and its [self-employed page](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/business-use-home-expenses.html)).
5. **Apply the income limit.** In Canada, business-use-of-home costs cannot create/increase a business loss. In the US, the limitation applies to otherwise nondeductible home expenses after the specified deductions; independently deductible mortgage interest/taxes have their own rules, so do not cap every cost indiscriminately; the otherwise nondeductible home-cost excess carries forward under the actual-cost method, subject to its ordering and future-year limits ([IRS Publication 587](https://www.irs.gov/publications/p587); [CRA business-use-of-home page](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/business-use-home-expenses.html)).
6. **Strip out what never counts.** Private use, amounts the employer reimburses, mortgage capital, and anything already claimed elsewhere on the return.
7. **Report on the right form.** US: Form 8829 or the Simplified Method Worksheet with Schedule C ([IRS Publication 587](https://www.irs.gov/publications/p587)). UK: the self-employment pages of the Self Assessment return. Canada: Form T2125 Part 7 for the self-employed ([CRA business-use-of-home page](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/business-use-home-expenses.html)), Form T777 with a signed Form T2200 for employees ([CRA detailed method eligibility](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22900-other-employment-expenses/work-space-home-expenses/who-claim/detailed-method.html)).
8. **Keep the evidence.** A floor plan with areas, the bills, an hours log where a method depends on hours, and any employer form.

## United States

### Who can claim

Employees cannot deduct a home office on their federal return. The IRS page states that "taxpayers can no longer claim a deduction for use of a home office as an employee, as miscellaneous itemized deductions for employee business expenses were eliminated for tax years beginning after 2017, even if the simplified method is used" ([IRS simplified option page](https://www.irs.gov/businesses/small-businesses-self-employed/simplified-option-for-home-office-deduction)). The old suspension ran for 2018 through 2025. Public Law 119-21 of 4 July 2025 substituted "beginning after 2017" for "2018 through 2025" in the heading of § 67(h) and struck out ", and before January 1, 2026" from its text, for taxable years beginning after 31 December 2025, so it now reads: "no miscellaneous itemized deduction shall be allowed for any taxable year beginning after December 31, 2017" ([Public Law 119-21 section 70110](https://www.govinfo.gov/content/pkg/PLAW-119publ21/pdf/PLAW-119publ21.pdf)). The suspension therefore continues for 2026 with no end date. This skill does not cover state returns, some of which may differ.

The deduction is open to a self-employed person (Schedule C) whose space meets one of the use tests. Per [IRS Publication 587](https://www.irs.gov/publications/p587), you must use part of your home:
- exclusively and regularly as your principal place of business, including qualifying administration/management where no other fixed location hosts substantial such activity; or
- exclusively and regularly as a place where you meet or deal with patients, clients or customers in the normal course of business; or
- for a separate structure not attached to the home, in connection with the business; or
- on a regular basis for certain storage of inventory or product samples; or
- for rental use; or
- as a daycare facility.

Exclusive use means "a specific area of your home only for your trade or business". The only exceptions to exclusive use are qualifying storage of inventory/product samples (wholesale/retail business, the home is the only fixed business location, regular use and separately identifiable suitable storage) and qualifying daycare (including the relevant licensing/approval or application/exemption conditions) ([IRS Publication 587](https://www.irs.gov/publications/p587)). A dining table also used for meals fails the test.

### Simplified method

| Item | Value | Condition and official source |
| --- | --- | --- |
| Rate per square foot of home used for business | USD 5 | "Standard deduction of $5 per square foot of home used for business (maximum 300 square feet)"  https://www.irs.gov/businesses/small-businesses-self-employed/simplified-option-for-home-office-deduction |

- The area cap is 300 square feet. The rate in the table above times the allowable area gives the deduction, before the income limit.
- Under the simplified method there is "No home depreciation deduction or later recapture of depreciation for the years the simplified option is used", and eligible home-related itemized deductions (mortgage interest, real estate taxes) stay on Schedule A, subject to that schedule's own limits ([IRS simplified option page](https://www.irs.gov/businesses/small-businesses-self-employed/simplified-option-for-home-office-deduction)).
- The choice is made each tax year on a timely filed, original return, and "An election for a tax year, once made, is irrevocable". Switching between methods from one year to the next does not need the Commissioner's consent ([IRS Publication 587](https://www.irs.gov/publications/p587)).
- A carryover of disallowed actual expenses from an earlier year cannot be deducted in a year the simplified method is used. It keeps carrying over to the next year that actual expenses are used ([IRS Publication 587](https://www.irs.gov/publications/p587)).
- If the home was moved during the year, the simplified method can be used for only one home; any other home uses actual expenses ([IRS Publication 587](https://www.irs.gov/publications/p587)).
- The simplified deduction is limited to the gross income from the qualified business use of the home, reduced by business deductions unrelated to the use of the home ([IRS Publication 587](https://www.irs.gov/publications/p587)). The IRS comparison table says the amount in excess of this limit may not be carried over under the simplified option ([IRS simplified option page](https://www.irs.gov/businesses/small-businesses-self-employed/simplified-option-for-home-office-deduction)).

### Regular (actual expense) method

- The business percentage of the home (usually area used for business over total area) is applied to actual costs: mortgage interest, real estate taxes, rent, utilities, insurance, repairs and depreciation ([IRS Publication 587](https://www.irs.gov/publications/p587)).
- Schedule C filers "figure your deduction limit and carryover on Form 8829" ([IRS Publication 587](https://www.irs.gov/publications/p587)).
- Deduction limit: if gross income from the business use of the home is less than total business expenses, the otherwise nondeductible expenses (insurance, utilities, depreciation of the home, with depreciation taken last) are limited. The excess carries over to the next year ([IRS Publication 587](https://www.irs.gov/publications/p587)).
- Depreciation claimed on the business part of the home can be taxed when the home is sold. Refer that question to `us-capital-gains`.
- Publication 587 (2025) is the latest edition the IRS prints. Publication 587 explains the section 280A business-use tests. The full current section 280A statute could not be reopened today, so no claim of a fresh direct statutory read is made.

For the full Schedule C computation, see `us-schedule-c-and-se-computation`.

## United Kingdom

### Self-employed: simplified flat rate

| Item | Value | Condition and official source |
| --- | --- | --- |
| 25 to 50 hours of business use in the month | GBP 10 | "25 to 50 £10"  https://www.gov.uk/simpler-income-tax-simplified-expenses/working-from-home |
| 51 to 100 hours in the month | GBP 18 | "51 to 100 £18"  https://www.gov.uk/simpler-income-tax-simplified-expenses/working-from-home |
| 101 hours or more in the month | GBP 26 | "101 and more £26"  https://www.gov.uk/simpler-income-tax-simplified-expenses/working-from-home |

- The rate is per month, set by that month's hours. "You can only use simplified expenses if you work for 25 hours or more a month from home" ([GOV.UK simplified expenses, working from home](https://www.gov.uk/simpler-income-tax-simplified-expenses/working-from-home)). A month under 25 hours gives nothing under this method.
- "The flat rate does not include telephone or internet expenses. You can claim the business proportion of these bills by working out the actual costs" (same page). Phone and internet are claimed on top, at their business share.
- The flat rate needs no exclusive-use room. GOV.UK: "This means you do not have to work out the proportion of personal and business use for your home" (same page).

### Self-employed: actual costs

GOV.UK says a self-employed person working from home may claim a proportion of costs such as heating, electricity, Council Tax, mortgage interest or rent, and internet and telephone use, using "a reasonable method of dividing your costs, for example by the number of rooms you use for business or the amount of time you spend working from home" ([GOV.UK, expenses if you're self-employed](https://www.gov.uk/expenses-if-youre-self-employed)). Mortgage interest is listed; capital repayments are not. Choose either the flat rate or the actual split for the household running costs, not both.

For the wider self-employed return, see `uk-freelance-intake`.

### Employees: relief claimed by the employee

| Item | Value | Condition and official source |
| --- | --- | --- |
| Weekly amount an employee could claim relief on, earlier years | GBP 6 | "You can either claim tax relief on: £6 a week the exact amount you’ve spent"  https://www.gov.uk/tax-relief-for-employees/working-at-home |

- For the tax year 6 April 2026 to 5 April 2027 this relief is gone. GOV.UK states: "From the tax year 6 April 2026 to 5 April 2027, you will not be able to claim tax relief for working from home. You can still claim for the 4 previous tax years" ([GOV.UK, working from home relief](https://www.gov.uk/tax-relief-for-employees/working-at-home)).
- For those earlier years the employee had to work from home, not choose to. "You cannot claim tax relief if you choose to work from home", including where the contract lets you work from home some or all of the time, or the office exists but is sometimes full (same page). Costs used for both private and business use, such as rent or broadband, could not be claimed.

### Employees: payments from the employer

| Item | Value | Condition and official source |
| --- | --- | --- |
| Weekly limit, 2020 to 2021 onwards | GBP 6 | "2020 to 2021 onwards £6.00 (or £26 a month for employees paid monthly)"  https://www.gov.uk/expenses-and-benefits-homeworking/homeworking-expenses-and-benefits-that-are-exempt-from-tax |
| Monthly limit for employees paid monthly, 2020 to 2021 onwards | GBP 26 | "£26 a month for employees paid monthly"  https://www.gov.uk/expenses-and-benefits-homeworking/homeworking-expenses-and-benefits-that-are-exempt-from-tax |

- This is a separate rule from the employee's own claim above. An employer that covers additional household expenses does not report or pay tax if both apply: the employee is working at home as agreed with the employer and regularly works from home under those arrangements, AND the amount is not more than the employee's additional household expenses or not more than the weekly limit in the table above ([GOV.UK homeworking expenses exempt from tax](https://www.gov.uk/expenses-and-benefits-homeworking/homeworking-expenses-and-benefits-that-are-exempt-from-tax)). This page does not say the employer exemption ended in April 2026.
- Reimbursed broadband is exempt only if all apply: a connection was not already available, the employee needs it to work from home, and it is mainly used for business (same page).

## Canada

### The temporary flat rate has ended

| Item | Value | Condition and official source |
| --- | --- | --- |
| Temporary flat rate per day, 2020, 2021 and 2022 only | CAD 2 | "temporary flat rate of $2 for each day you worked from home in 2020, 2021, or 2022"  https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22900-other-employment-expenses/work-space-home-expenses/who-claim.html |

The CRA states: "Eligible employees who worked from home in 2023 or later tax years will be required to use the detailed method to claim home office expenses. The temporary flat rate method does not apply to the 2023 and later tax years" ([CRA, what the changes are](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22900-other-employment-expenses/work-space-home-expenses/what-changes.html)). For 2026 there is no flat rate.

### Employees: detailed method

| Item | Value | Condition and official source |
| --- | --- | --- |
| Share of time worked from the home work space | 50% | "You worked more than 50% of the time from the work space in your home for a period of at least 4 consecutive weeks in the year"  https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22900-other-employment-expenses/work-space-home-expenses/who-claim/detailed-method.html |

An employee must meet all of these ([CRA detailed method eligibility](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22900-other-employment-expenses/work-space-home-expenses/who-claim/detailed-method.html)):
- the employer required the employee to work from home (a written or verbal agreement is enough, and a voluntary formal telework arrangement counts as required); AND
- the employee was required to pay the work space expenses; AND
- either more than the share in the table above of the time worked from the home work space for at least 4 consecutive weeks, OR the space is used only to earn employment income and used regularly and continually for in-person meetings with clients, customers or others; AND
- the expenses are used directly in the work; AND
- the employee has a completed and signed Form T2200 from the employer.

Amounts the employer reimbursed or will reimburse cannot be claimed (same page).

Apportionment for employees: workspace area divided by home area. For a common (shared) area, multiply also by hours worked in the space over the 168 hours in a week; a designated room used only for work is not reduced for hours ([CRA, determine your work space use](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22900-other-employment-expenses/work-space-home-expenses/work-space-use.html)).

### Self-employed: business-use-of-home expenses

Per the [CRA business-use-of-home page](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/business-use-home-expenses.html):
- The workspace must be the principal place of business, OR be used only to earn business income AND used on a regular and ongoing basis to meet clients, customers or patients.
- Deductible: part of heating, home insurance, electricity, cleaning materials, property taxes, mortgage interest and capital cost allowance (CCA). Use a reasonable basis such as workspace area over total area. For a space also used for personal living, multiply by the business hours in the day over 24 hours. Reduce the claim if the business runs only part of the week or year.
- The claim "cannot be more than your net income from the business before you deduct these expenses". The amount not deducted carries forward to the next fiscal period, under the same rules.
- Claiming CCA on the home brings in the capital gain and recapture rules when the home is sold.
- The calculation goes on Form T2125, Part 7. For the full T2125 workflow, see `ca-fed-t2125`.

## Other countries: use the country Guide

This skill does not state rates for other countries. Use the country Guide:

| Country | Guide |
| --- | --- |
| Germany (Tagespauschale, Arbeitszimmer) | `germany-tax-optimization` |
| Australia (fixed rate or actual cost) | `au-sole-trader-schedule` |
| Malta | `malta-income-tax` |
| France | `fr-personal-income-tax` |
| Spain (suministros, IRPF deductions) | `es-irpf-deductions` |
| India | `india-income-tax` |
| Netherlands (werkruimte) | `nl-zzp-deductions` |
| Switzerland | `ch-federal-income-tax` |

If no country Guide covers home office costs, say so and refer the client to a local accountant.

## What never counts

- A space used for private life as well, under the US exclusive-use test (except storage and daycare as above).
- A US employee's home office, on the federal return, for 2026.
- A UK employee's own claim for working from home, for the tax year 6 April 2026 to 5 April 2027.
- The Canadian temporary flat rate, for 2023 and later years.
- Mortgage capital repayments. Interest is a potentially eligible actual-method cost for the relevant self-employed person; this does not make employee mortgage interest deductible or override country limits.
- Any cost the employer reimbursed (Canada says so expressly).
- The same cost claimed twice: once as home office and once as a separate business expense.

## Common mistakes

1. Claiming the US simplified rate for an employee. It is not available to employees, whichever method is chosen.
2. Using the UK GBP 6 a week employee relief for 2026 to 2027. It has ended for that year; earlier years may still be claimed.
3. Applying the Canadian temporary flat rate after 2022.
4. Leaving out the hours step for a shared space in Canada, or the area step in any country.
5. Ignoring Canada's no-loss limit or the US ordering/income limit for otherwise nondeductible home costs. Mortgage interest/taxes that are independently deductible require their separate rules.
6. Forgetting phone and internet are outside the UK flat rate and can be claimed at their business share.

## Ask the client first

- Are you an employee, self-employed, or both, and in which country do you file?
- Is the space used only for work, or also for private life, and what are its area and the home's total area?
- Is it your principal place of business, or do you meet clients there regularly in person?
- How many hours a month (UK) or a week (Canada) do you work in it?
- For employees: did your employer require you to work from home, do you have a signed Form T2200 (Canada), and does your employer reimburse any costs?
- Does the business have enough net income to absorb the claim, and is there a carryover from an earlier year?

## When to refuse or refer

- Any country other than the US, UK or Canada: route to the country Guide above and do not quote rates from this skill.
- US state returns, or a sale of a home on which home office depreciation or CCA was claimed: refer to an accountant.
- A UK room used exclusively for business where the client asks about Capital Gains Tax on the sale: refer.
- Mixed employee and self-employed use of the same space, or more than one business in the home: refer, as the apportionment is fact-specific.
- Australia: route to `au-sole-trader-schedule` only. This skill gives no Australian figures.

## Worked cases

### US simplified method with an income limit

Assume an eligible full-year sole proprietor, exclusive regular qualifying office of 350 square feet, a USD 5 rate and 300-square-foot cap from the linked IRS simplified-option source, and only USD 900 of home-use income after unrelated business deductions. The potential 1,500 is limited to 900; the 600 simplified excess is not carried forward. Eligibility is assumed only for this calculation, not inferred from the area.

```oa-check
name: US simplified home office, capped area and income
inputs:
  area: 350
  area_cap: 300
  rate: 5
  available_income: 900
steps:
  - usable_area: min(area, area_cap)
  - potential: usable_area * rate
  - deduction: min(potential, available_income)
  - simplified_excess_not_carried: potential - deduction
expected:
  usable_area: 300
  potential: 1500
  deduction: 900
  simplified_excess_not_carried: 600
```

### UK hours and separate business phone cost

An eligible sole trader has ten 40-hour months and two 60-hour months, plus an evidenced GBP 120 business share of telephone/internet. The published monthly flat rates give 136 household costs, with the separate business phone/internet amount giving 256 total on these facts. Do not add actual household utility costs again.

```oa-check
name: UK monthly homeworking bands and separate phone
inputs:
  lower_months: 10
  lower_rate: 10
  upper_months: 2
  upper_rate: 18
  business_phone_internet: 120
steps:
  - household_flat: lower_months * lower_rate + upper_months * upper_rate
  - total: household_flat + business_phone_internet
expected:
  household_flat: 136
  total: 256
```

### Canada shared workspace, no premature rounding

Assume an eligible employee has signed T2200, required unreimbursed costs ofCAD1,200 for the qualifying period, a shared area 12% of the finished home and 40 work hours of 168 weekly hours. Carry full precision through the area/time allocation and round the final cost: CAD 34.29. The CRA's printed illustration rounds its intermediate percentage to 2.8% and displays 33.60; that is an illustration of rounding, not a statutory flat deduction. Retain the actual allocation and documented rounding policy. Multiple workers must each allocate their own space/time; moves or changed workspaces require separate period calculations.

```oa-check
name: Canada employee shared area, exact hours allocation
inputs:
  eligible_costs: 1200
  area_share: 0.12
  work_hours: 40
  weekly_hours: 168
steps:
  - time_share: work_hours / weekly_hours
  - deductible: round(eligible_costs * area_share * time_share, 2)
expected:
  time_share: 0.2380952380952380952380952381
  deductible: 34.29
```

Deliver the eligibility decision, bills and supported allocation, method comparison, limitation/carryforward and proposed form amounts. Keep mortgage principal/private/reimbursed/duplicate amounts out. For read-only books, provide proposed postings or an import for human approval. Do not submit the return from this workpaper.

## Existing review requirement

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Sources

| Official source | Read on | Read scope |
|---|---|---|
| https://www.irs.gov/businesses/small-businesses-self-employed/simplified-option-for-home-office-deduction | 2026-11-14 | Read for current eligibility, USD 5/300-square-foot simplified option, income limit, no excess carryover, ScheduleA limits and annual method election. |
| https://www.irs.gov/publications/p587 | 2026-11-14 | Read for Publication 587(2025) qualifying uses/exceptions, principal place, actual-cost allocation and ordering, simplified choice, carryovers and multiple homes. This is the 2025 edition, not a published2026 form. |
| https://www.govinfo.gov/content/pkg/PLAW-119publ21/pdf/PLAW-119publ21.pdf | 2026-11-14 | Read for enacted section 70110 and effective date; permanent section 67 restriction and educator provision, effective after 31 December2025. |
| https://www.gov.uk/simpler-income-tax-simplified-expenses/working-from-home | 2026-11-14 | Read for monthly hours25-50/51-100/101+, rates10/18/26, minimum25hours and separate business phone/internet. |
| https://www.gov.uk/expenses-if-youre-self-employed | 2026-11-14 | Read for reasonable actual household-cost allocation, mortgage interest/rent and business/private split. |
| https://www.gov.uk/tax-relief-for-employees/working-at-home | 2026-11-14 | Read for explicit employee-own-claim termination for 6 April2026-5April2027 and earlier-year conditions. |
| https://www.gov.uk/expenses-and-benefits-homeworking/homeworking-expenses-and-benefits-that-are-exempt-from-tax | 2026-11-14 | Read for separate regular agreed homeworking/additional-cost reimbursement, GBP 6weekly/26monthly and broadband conditions. |
| https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22900-other-employment-expenses/work-space-home-expenses/what-changes.html | 2026-11-14 | Read for detailed-method requirement from 2023 and end of temporary employee flat rate. |
| https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22900-other-employment-expenses/work-space-home-expenses/who-claim.html | 2026-11-14 | Read for temporary flat-rate historical2020-2022-only scope and current detailed-method route. |
| https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22900-other-employment-expenses/work-space-home-expenses/who-claim/detailed-method.html | 2026-11-14 | Read for all current eligibility conditions and neighbouring2025 worked arrangements, employer requirement/telework, more-than 50%/4weeks or exclusive in-person alternative, reimbursement exclusion and signed T2200. |
| https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22900-other-employment-expenses/work-space-home-expenses/work-space-use.html | 2026-11-14 | Read for finished home area, designated/shared areas,40/168hours, multiple workers, workspace changes and moves; intermediate rounding in the printed example. |
| https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/business-use-home-expenses.html | 2026-11-14 | Read for principal-place/meeting tests, eligible costs, area/time, part-period reduction, CCA sale consequences, no-loss/carryforward and T2125 Part 7/line 9945. |

Not yet confirmed: IRS2026 Publication 587/Form 8829 and final2026 return line updates were not published/read in the sources used here; use the identified2025 edition for the structural method and verify the 2026 form before filing. The full current US section 280A text could not be reopened, so Cornell/private databases were removed as citations. No home-office rates for countries beyond the three worked countries are supplied.
