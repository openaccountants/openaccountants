---
name: us-tax-workflow-base
description: "US federal individual/self-employed return preparation method for 2026, with separately labelled 2025 filing-cycle notes. Confirm year/status/entity, reconcile receipts and source records, apply supported Schedule C/SE, vehicle/home-office/asset/information-return and estimated-tax rules, preserve unresolved facts, and hand off full return assembly and required professional review. Federal only; no state-tax or accountant approval of a new client return is implied."
version: 0.3
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-14
type: filing-howto
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# US federal workflow v0.3: 2026 individual and self-employed returns, with 2025 notes

Figures are for tax year 2026 unless a line says 2025. The 2026 amounts come from Rev. Proc. 2025-32 and from IRS pages updated for the One Big Beautiful Bill Act (P.L. 119-21). The ordinary 2025 extended filing deadline of October 15, 2026 has already passed as of this read date. Separate 2025 notes do not establish a still-open extension; check any actual disaster, overseas or other special relief. Published 2025 detailed explanations below are explicitly the latest 2025-2026 filing-cycle guidance read, not a claim that every 2026 instruction has been published.

This skill is the front door for a US federal Form 1040 with self-employment income. It sets the order of work, the facts to collect, how to sort income and expenses, the records that must exist, and when to stop and refer.

## Scope and who this is for

- **Covers:** US citizens and resident aliens who file Form 1040 and run a business as a sole proprietor, or through a single-member LLC that is disregarded for federal income tax. It also covers a married couple running a business as a qualified joint venture. This method follows the Schedule C trade/business path; rental and farming activities can need other schedules and are referred to the appropriate workflow.
- **Does not cover:** partnerships and multi-member LLCs, S and C corporations, estates and trusts, nonresident aliens, and employer payroll. State and local tax is also out of scope. Each state has its own rules, so check that state's own revenue department before giving a combined answer.
- **Companion Skills (use them instead of repeating their rules here):**
  - `us-federal-return-assembly`: the order of Schedule SE, retirement, self-employed health insurance, QBI, Schedules 1, 1-A and 2, and the Form 2210 penalty.
  - `us-1099-k-and-payment-processors`: Form 1099-K, payment apps, and reconciling Box 1a to Schedule C.
  - `us-capital-gains`: sales of shares, funds, digital assets held as investments, and a home.
  - `us-secure-2-and-retirement-updates`: plan limits and SEP, SIMPLE and solo 401(k) rules.
  - `us-tax-residency`: whether the person is a resident alien at all.
  - `us-irs-collections-and-controversy`: notices, audits, unpaid balances and penalties.
- **Who reads the output.** Where a preparer uses this skill, a person who can sign the return reviews every position before filing. Where a taxpayer uses it directly, it explains the method and says clearly what needs a professional.

## Ask the client first

Read the full existing taxpayer record, prior returns/elections, source documents and latest answers first. Ask only for genuine gaps, preserving current source/version and actual approval provenance; using a named method does not approve this new client return.

- Which actual tax year and filing status is being prepared? For 2025, distinguish an overdue return from an evidenced special relief period; the ordinary extension has expired. Keep each year's forms, tables, elections, payments and amended/prior-year issues separate.
- Marital status on December 31 of that year, whether a spouse died during the year, and whether anyone can claim the taxpayer as a dependent. Filing status follows marital status on the last day of the year. If a spouse died, also establish remarriage and the actual available joint/separate/considered-unmarried conditions ([Pub. 501](https://www.irs.gov/publications/p501)).
- Was the taxpayer a US citizen or resident alien for the whole year? If not, stop and use `us-tax-residency`.
- How is the business held: in the owner's own name, through an LLC, or co-owned with a spouse or anyone else? Has any Form 8832 or Form 2553 election ever been filed?
- What does the business do, since when, and in which years did it make a profit? Does the owner work in it regularly?
- Every income source: Forms 1099-NEC, 1099-MISC and 1099-K, cash, checks and payment-app receipts. Income is reportable whether or not a form arrived.
- Bank and card statements for every account the business used, including personal accounts that carried business payments.
- Vehicles: how many are used in the business, the date each was first used for business, business and total miles, and whether a mileage log exists.
- Home office: square footage used only and regularly for the business, and the total square footage of the home. Is that space the principal place of business, a place to meet clients or customers, or a separate structure? Is it used for storing inventory or for daycare ([Pub. 587](https://www.irs.gov/publications/p587))?
- Equipment bought during the year: cost per invoice or item, date placed in service, and whether an applicable financial statement (AFS) exists under the actual definition; an audit is not the only qualifying category.
- People paid for services: names, amounts paid in the year, how they were paid, and whether a Form W-9 was collected.
- Wages from any job, estimated tax payments already made, and the prior year's tax and adjusted gross income (AGI).
- Anything that may take the return outside this skill: employees, foreign accounts or income, digital assets, rental property, K-1s, open IRS notices, unfiled years.

## The method, step by step

1. **Fix the year and the filing status first.** Use marital status on the last day of the year. If a spouse died during the year, the taxpayer is considered married for the whole year. If more than one status is legally available, compare the supported results subject to eligibility, actual joint-return consent and applicable restrictions ([Pub. 501](https://www.irs.gov/publications/p501)). Never assume a status. A married person cannot file as single, so a default of "single" can produce an invalid return. Resolve it from the records or ask the missing fact; do not infer consent to a joint return merely from a lower tax result.
2. **Confirm residence.** This skill assumes a US citizen or resident alien for the full year. For a first or last year in the US, or a dual-status year, use `us-tax-residency` before anything else.
3. **Classify the entity** ([IRS: single-member LLCs](https://www.irs.gov/businesses/small-businesses-self-employed/single-member-limited-liability-companies)). A single-member LLC is disregarded for income tax unless it files Form 8832 and elects to be a corporation. For the trade/business activity within this method, use the appropriate owner Schedule C; rental/farming or another activity may use a different schedule and remains outside this narrow workflow. It is still a separate entity for employment tax and certain excise taxes. An LLC with at least two members is a partnership unless it elects corporate status. Stop and refer if the business is a partnership or a corporation.
4. **Test spouse-owned businesses** ([IRS: qualified joint venture](https://www.irs.gov/businesses/small-businesses-self-employed/election-for-married-couples-unincorporated-businesses)). A business co-owned by a married couple is generally a partnership. It can instead be a qualified joint venture, with each spouse filing a Schedule C, only if **all** of these hold: the only members are the married couple, they file a joint return, **both** spouses materially participate, and **both** elect. A business held through an LLC does not qualify. For a married couple's LLC in a community property state, check Rev. Proc. 2002-69 before choosing the treatment.
5. **Decide business or hobby.** An activity is a business if its primary purpose is income or profit and the owner is involved with continuity and regularity. A sporadic activity or a hobby is not a business ([Schedule C instructions](https://www.irs.gov/instructions/i1040sc)). There is a presumption of profit motive if gross income exceeds deductions in 3 or more of the 5 consecutive years ending with the current year. For horse breeding, training, showing or racing it is 2 of 7 years ([26 U.S.C. 183](https://uscode.house.gov/us/usc/119-120/t26/s183/)). Hobby income is still taxable. Ordinary hobby operating expenses do not become Schedule C loss deductions; current section 67(h) disallows miscellaneous itemized deductions after 2017. Section 183(b)(1) preserves otherwise allowable deductions subject to their own rules, so do not say every otherwise deductible item is lost. The profit presumption is rebuttable, and failing it is not proof of a hobby ([26 U.S.C. 67(h)](https://uscode.house.gov/us/usc/119-120/t26/s67/)).
6. **Reconcile gross receipts from all records, not forms or bank deposits alone.** Read every invoice, cash/card/processor report and bank account, actual accounting method and unpaid/non-cash items. Exclude supported duplicate transfers, genuine loans and owner capital without deleting the source record. Expense refunds/recoveries are not automatically excluded: reconcile them to purchase cost, prior deduction or taxable recovery as applicable; Schedule C line 6 includes business recoveries/refunds. No one item is counted both from a payment report and its settlement. Then tie the result to each Form 1099-NEC, 1099-MISC and 1099-K. Actual payment-card/qualifying third-party settlement transactions under section 6050W are reported through the payment-settlement regime, not duplicated as NEC; do not infer this solely from an app name ([Form 1099-MISC and 1099-NEC instructions](https://www.irs.gov/instructions/i1099mec)). For the reconciliation, use `us-1099-k-and-payment-processors`.
7. **Classify each expense.** Deduct it only if it is an ordinary and necessary cost of this business and not personal. Then apply the limits in "Figures for 2026" below: meals, gifts, vehicles, home office, and whether an asset is expensed or capitalized. Ordinary business entertainment is generally disallowed, subject to actual statutory exceptions; ordinary commuting is personal. Do not convert the general rule into a denial of every qualifying exception ([Pub. 463](https://www.irs.gov/publications/p463)).
8. **Check that the records exist.** Travel, gifts and cars need records of the amount, the date, the place and the business purpose. Keep adequate statutory substantiation and actual business purpose/relationship. Latest detailed Pub. 463 guidance read is the 2025-2026 filing cycle: generally documentary evidence for lodging and other expenses of $75 or more, with actual receipt-unavailable transportation and other stated exceptions; casualty-lost records may be reconstructed. Do not invent a deduction from likelihood, but do not equate a missing original receipt with no possible lawful supporting evidence. [Pub. 463](https://www.irs.gov/publications/p463), [26 USC 274(d)](https://uscode.house.gov/us/usc/119-120/t26/s274/).
9. **Work out the business's own filing duties to others.** Decide whether each person paid was a worker or an independent contractor (see the boundary table). Obtain the proper payee identity/TIN and required certification, checking actual Form W-9/other documentation and exemption rules. A missing TIN is unresolved evidence, not permission to fabricate one or withhold on every payment regardless of scope. Then decide which Forms 1099-NEC and 1099-MISC are due for the year the payments were made ([Form 1099-MISC and 1099-NEC instructions](https://www.irs.gov/instructions/i1099mec)).
10. **Test self-employment tax.** SE tax usually applies when net earnings from self-employment are $400 or more. Net earnings are generally 92.35% of net profit ([Topic 554](https://www.irs.gov/taxtopics/tc554)). Then use `us-federal-return-assembly` for Schedule SE, the retirement and health insurance deductions, and QBI, in that order.
11. **Test estimated tax for the coming year** (see the 2026 figures). A new or growing business often owes estimated tax for the first time.
12. **Record every open fact as an open fact.** Where a fact is missing, keep the supported alternatives and exact evidence needed; any provisional calculation is explicitly incomplete, not an invented fact or a compulsory greater-tax treatment. Do not file on a provisional treatment. Resolve it, or take the position the facts support and disclose it where needed.
13. **Review before filing.** The return may be signed only when every position has authority behind it. Under section 6694(a), assess the actual understatement, preparer knowledge, ordinary substantial-authority standard and properly disclosed reasonable-basis rule. Tax-shelter/reportable-transaction positions have a different standard, and reasonable cause/good faith is an express exception; disclosure is not permission to file a guess ([26 U.S.C. 6694](https://uscode.house.gov/us/usc/119-124/t26/s6694/)).

## Figures for 2026, with years ([Rev. Proc. 2025-32](https://www.irs.gov/irb/2025-45_IRB); [Pub. 505 (2026)](https://www.irs.gov/publications/p505); [IRS standard mileage rates](https://www.irs.gov/tax-professionals/standard-mileage-rates))

| Item | 2026 | 2025 | Condition that decides it |
| --- | --- | --- | --- |
| Business standard mileage rate | 72.5 cents a mile from January 1 to June 30; 76 cents a mile from July 1 to December 31 | 70 cents a mile | 2026 has two rates. Apply each to the miles driven in its own period ([IRS standard mileage rates](https://www.irs.gov/tax-professionals/standard-mileage-rates)) |
| Simplified home office | $5 a square foot, up to 300 square feet | Same | Part of the home used exclusively and regularly as the principal place of business or to meet clients, or a separate structure used for the business. Storage and daycare have their own rules ([IRS simplified option](https://www.irs.gov/businesses/small-businesses-self-employed/simplified-option-for-home-office-deduction); [Pub. 587](https://www.irs.gov/publications/p587)) |
| De minimis safe harbor, no applicable financial statement | $2,500 per invoice or item | Same | Annual election on a timely filed original return, and the amounts must be expensed on the books under a policy in place at the start of the year ([IRS tangible property regulations](https://www.irs.gov/businesses/small-businesses-self-employed/tangible-property-final-regulations)) |
| De minimis safe harbor, with an applicable financial statement | $5,000 per invoice or item | Same | Same election. The book policy must be in writing ([IRS tangible property regulations](https://www.irs.gov/businesses/small-businesses-self-employed/tangible-property-final-regulations)) |
| Section 179 expensing limit | $2,560,000 | $2,500,000 | Reduced dollar for dollar once §179 property placed in service in the year exceeds the phase-out amount ([Rev. Proc. 2025-32](https://www.irs.gov/irb/2025-45_IRB)) |
| Section 179 phase-out starts above | $4,090,000 | $4,000,000 | Same dated law change/inflation adjustment; other eligibility/limitations still apply [Rev. Proc. 2025-32 sections 2.10, 3 and 4.24](https://www.irs.gov/irb/2025-45_IRB) |
| Section 179 limit for a sport utility vehicle | $32,000 | Not supplied; obtain actual 2025 Form 4562 rule | Applies only to qualifying SUV cost under section 179, not all vehicle deductions [Rev. Proc. 2025-32 section .24](https://www.irs.gov/irb/2025-45_IRB) |
| Business meals | Ordinary qualifying meal limit 50%; actual exceptions apply | Same general rule in latest 2025-cycle guide | DOT qualifying away-from-home/duty meals can use 80%, not every meal of every transport worker [26 USC 274(n)(1) to (3)](https://uscode.house.gov/us/usc/119-120/t26/s274/) / [Pub. 463 2025](https://www.irs.gov/publications/p463) |
| Business gifts | Ordinary covered gifts $25 per individual per tax year | Same | Actual indirect-gift, spouse and statutory promotional/incidental-cost exceptions still matter [26 USC 274(b)](https://uscode.house.gov/us/usc/119-120/t26/s274/) / [Pub. 463 2025](https://www.irs.gov/publications/p463) |
| Documentary-evidence guidance, latest detailed 2025-2026 filing cycle read | Apply actual substantiation; no new 2026 regulatory revision certified here | Generally lodging and other expenses $75 or more, with actual exceptions | Receipt-unavailable transportation, accountable-plan/per-diem scope and casualty reconstruction must be assessed, not a blanket no-receipt denial [Pub. 463](https://www.irs.gov/publications/p463) / [26 USC 274(d)](https://uscode.house.gov/us/usc/119-120/t26/s274/) |
| Form 1099-NEC nonemployee compensation | $2,000 or more | $600 or more | The payment year decides. The $2,000 applies from 2026 and may be adjusted for inflation from 2027 ([2026 instructions](https://www.irs.gov/instructions/i1099mec); [2025 instructions](https://www.irs.gov/pub/irs-prior/i1099mec--2025.pdf)) |
| Form 1099-MISC gross proceeds paid to an attorney | $600 or more | $600 or more | Box 10. This one did not move to $2,000 ([2026 instructions](https://www.irs.gov/instructions/i1099mec)) |
| Backup withholding rate | 24% | 24% | Applies when a payee does not give a correct TIN, among other cases ([IRS backup withholding](https://www.irs.gov/businesses/small-businesses-self-employed/backup-withholding)) |
| Self-employment tax applies | Net earnings of $400 or more | Same | [Topic 554](https://www.irs.gov/taxtopics/tc554) |
| Share of net profit that counts as net earnings | 92.35% | Same | [Topic 554](https://www.irs.gov/taxtopics/tc554) |
| SE tax rates | 12.4% social security plus 2.9% Medicare | Same | Social security part only up to the wage base ([Topic 554](https://www.irs.gov/taxtopics/tc554)) |
| Social security wage base | $184,500 | $176,100 | Wages already taxed for social security use up part of the base ([Pub. 505 (2026)](https://www.irs.gov/publications/p505); [archived Schedule SE (2025)](https://www.irs.gov/pub/irs-prior/f1040sse--2025.pdf)) |
| Estimated tax needed if expected balance due is | At least $1,000 | Same | And withholding and credits fall short of the safe harbor. The prior-year test needs a 2025 return covering all 12 months ([Pub. 505 (2026)](https://www.irs.gov/publications/p505)) |
| Safe harbor | Smaller of 90% of 2026 tax or 100% of 2025 tax | Not repeated here | The 2025 return must cover 12 months. 110% instead of 100% if 2025 AGI was more than $150,000 ($75,000 if married filing separately for 2026), unless at least two-thirds of gross income is from farming or fishing ([Pub. 505 (2026)](https://www.irs.gov/publications/p505)) |

The QBI thresholds, the Additional Medicare Tax and the net investment income tax are in `us-federal-return-assembly` and `us-capital-gains`. They are not repeated here.

## Boundaries and exceptions ([Pub. 463](https://www.irs.gov/publications/p463); [IRS: employee or contractor](https://www.irs.gov/businesses/small-businesses-self-employed/independent-contractor-self-employed-or-employee))

| Rule | The condition that decides it | Source |
| --- | --- | --- |
| Standard mileage rate: first year | For a car the taxpayer owns, the standard rate must be chosen in the **first year** the car is available for business use. In later years, either method can be used. For a leased car, the standard rate must be used for the whole lease period. | [Pub. 463](https://www.irs.gov/publications/p463) |
| Standard mileage rate: not allowed | Not allowed if five or more cars are used **at the same time**, or if the car was depreciated under MACRS, by any method other than straight line, or under §179. Also not allowed if the special depreciation allowance (bonus depreciation) was claimed on the car, or, for a leased car, if actual car expenses were claimed after 1997. | [Pub. 463](https://www.irs.gov/publications/p463) |
| Commuting | Travel between home and a regular place of work is personal. Travel from home to a temporary work location outside the metropolitan area is deductible. If the taxpayer has one or more regular work locations away from home, trips between home and a temporary work location in the same business are deductible regardless of distance. If home is the principal place of business, trips between home and another work location in the same business are deductible, whether the work is temporary or permanent and regardless of distance. | [Pub. 463](https://www.irs.gov/publications/p463) |
| Home office | Only the part of the home used **exclusively** and **regularly** as (a) the principal place of business, or (b) a place where the taxpayer meets or deals with patients, clients or customers in the normal course of business; or (c) a separate structure not attached to the home, used in connection with the business. Storage of inventory or product samples, and daycare, have their own rules ([Pub. 587](https://www.irs.gov/publications/p587)). The simplified/regular method choice is made on the timely filed original return and cannot be switched for that same year; preserve prior regular-method carryovers separately rather than assuming they disappear when not claimable in a simplified year. The deduction cannot exceed the gross income from the business use of the home, less business expenses. Under the simplified method any excess is lost, and there is no depreciation and no later recapture. The method can be changed from year to year. An employee working from home gets no home office deduction. | [IRS simplified option](https://www.irs.gov/businesses/small-businesses-self-employed/simplified-option-for-home-office-deduction) |
| De minimis safe harbor | The amounts must also be expensed on the books under a consistent accounting procedure in place at the start of the tax year. With an applicable financial statement (AFS) the procedure must be written; without one it need not be. Attach a statement titled "Section 1.263(a)-1(f) de minimis safe harbor election" to the timely filed **original** return, including extensions, for each year it applies. An item costing more than the limit is outside this safe harbour but may still be currently deductible as qualifying repairs/materials or under other actual rules; excess cost does not automatically require capitalisation. | [IRS tangible property regulations](https://www.irs.gov/businesses/small-businesses-self-employed/tangible-property-final-regulations) |
| Entertainment and meals | Ordinary business entertainment is generally disallowed; test actual statutory exceptions. Separately purchased/separately invoiced food and drink still need actual qualifying meal facts before the ordinary fifty-percent limit; absence of a business purpose, presence or another required condition is not cured by a separate invoice. | [Pub. 463](https://www.irs.gov/publications/p463) |
| Worker or contractor | The test is the right to control what is done and how it is done, looking at behavioral control, financial control and the type of relationship. If it is still unclear, Form SS-8 can be filed. A worker who is an employee takes the business outside this skill. | [IRS: employee or contractor](https://www.irs.gov/businesses/small-businesses-self-employed/independent-contractor-self-employed-or-employee) |
| Form 1099-NEC due date | January 31 after the payment year, on paper or electronically. A due date on a weekend or legal holiday moves to the next business day. January 31, 2027 is a Sunday, so 2026 forms are due February 1, 2027. | [Form 1099-MISC and 1099-NEC instructions](https://www.irs.gov/instructions/i1099mec) |
| E-filing information returns | Required if the business files 10 or more information returns in total (all types counted together), for returns due on or after January 1, 2024. | [Form 1099-MISC and 1099-NEC instructions](https://www.irs.gov/instructions/i1099mec) |
| Single-member LLC with employees | Disregarded for income tax, but a separate entity for employment tax. Payroll is outside this skill. | [IRS: single-member LLCs](https://www.irs.gov/businesses/small-businesses-self-employed/single-member-limited-liability-companies) |
| Hobby presumption | Needs gross income above deductions in 3 or more of the 5 years ending with this year (2 of 7 for horses). Failing it is not proof of a hobby. It only removes the presumption. | [26 U.S.C. 183(d)](https://uscode.house.gov/us/usc/119-120/t26/s183/) |
| Records: how long | Generally 3 years after filing, with an early return treated as filed on the due date. For a refund claim filed later, 3 years from filing the original return or 2 years from paying the tax, whichever is later. 6 years if unreported income is more than 25% of the gross income shown. 7 years for a claim for a loss from worthless securities or a bad debt deduction. Indefinitely if no return or a fraudulent return was filed. Employment tax records: at least 4 years after the tax becomes due or is paid, whichever is later. Retain property/basis records through the limitation period for the disposal year and any longer non-tax requirement; do not destroy all asset records after the ordinary three-year period. | [IRS: how long to keep records](https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records) |

## Provisional treatments while a fact is missing ([Pub. 463](https://www.irs.gov/publications/p463); [26 U.S.C. 6694](https://uscode.house.gov/us/usc/119-124/t26/s6694/))

Use these only as working positions in the file. Each one must be flagged, turned into a question, and resolved before filing. They are not filing positions. The return must show the correct tax, not the highest one.

| Missing fact | Provisional treatment | What resolves it |
| --- | --- | --- |
| Filing status | None. Ask; do not assume "single". | Marital status on December 31 ([Pub. 501](https://www.irs.gov/publications/p501)) |
| Business-use share of a car | Final deduction held; show only supported actual alternatives | Actual business/total-use records and any lawful substantiation exception; do not guess zero as a factual answer |
| Substantiation for travel, gifts or a car | Final deduction held unless actual substantiation/exception is established | Amount/date/place/business purpose and relationship, or lawful corroboration/reconstruction; missing original receipt is not necessarily no evidence |
| Whether a deposit is income | Reconcile source and accounting method; retain unresolved alternatives | Invoice/cash/processor/bank and transfer/loan/capital/recovery evidence; do not automatically make every unexplained deposit income |
| Whether an activity is a business | Flag. Do not deduct losses until settled. | The facts in step 5 |
| Whether a de minimis election was made in a past year | Actual annual election remains unresolved | Read that filed return, attachment and any applicable relief; do not assert no election merely because it was not initially provided |
| Whether estimated tax was paid | Payment/credit is unresolved, not definitively unpaid | IRS transcript and actual confirmations, dates and correct tax-year allocation |
| Whether a payee gave a TIN | Obtain identity/documentation and test actual backup-withholding scope | Actual W-9/appropriate payee evidence and exemptions; no invented TIN or automatic tax on all payments |

## Worked cases

The amounts in these cases are made up for illustration. The rates, limits and thresholds come from the sources linked in each heading.

### Case 1: SE tax on a 2026 Schedule C profit ([Topic 554](https://www.irs.gov/taxtopics/tc554))

- A single freelancer has 2026 Schedule C net profit of $60,000 and no wages.
- Net earnings: $60,000 × 92.35% = $55,410. That is $400 or more, so SE tax applies.
- Social security part: $55,410 × 12.4% = $6,870.84. The wage base of $184,500 is not reached.
- Medicare part: $55,410 × 2.9% = $1,606.89.
- SE tax: $6,870.84 + $1,606.89 = $8,477.73. Half of it (about $4,239) is an adjustment to income. Finish the return in `us-federal-return-assembly`.

```oa-check
name: Ordinary 2026 self employment calculation below combined Social Security cap
inputs:
  schedule_c_profit: 60000
  ordinary_se_fraction: 0.9235
  social_security_base: 184500
  prior_social_security_wages: 0
  social_security_rate: 0.124
  medicare_rate: 0.029
steps:
  - net_se_earnings: schedule_c_profit * ordinary_se_fraction
  - remaining_social_base: max(social_security_base - prior_social_security_wages, 0)
  - social_security_tax: min(net_se_earnings, remaining_social_base) * social_security_rate
  - medicare_tax: net_se_earnings * medicare_rate
  - total_se_tax: social_security_tax + medicare_tax
  - deductible_half_before_form_rounding: total_se_tax / 2
expected:
  net_se_earnings: 55410
  social_security_tax: 6870.84
  medicare_tax: 1606.89
  total_se_tax: 8477.73
  deductible_half_before_form_rounding: 4238.865
```

### Case 2: 2026 mileage across the mid-year rate change ([IRS standard mileage rates](https://www.irs.gov/tax-professionals/standard-mileage-rates))

- One car, owned, used for business since 2024 with the standard rate chosen that year. There is a mileage log.
- Business miles January 1 to June 30: 6,000 at 72.5 cents = $4,350.
- Business miles July 1 to December 31: 4,000 at 76 cents = $3,040.
- Vehicle deduction: $4,350 + $3,040 = $7,390. Using a single rate for the whole year would be wrong.

```oa-check
name: 2026 business mileage uses two actual effective date periods
inputs:
  first_half_supported_miles: 6000
  second_half_supported_miles: 4000
  first_half_dollars_per_mile: 0.725
  second_half_dollars_per_mile: 0.76
steps:
  - first_half_deduction: first_half_supported_miles * first_half_dollars_per_mile
  - second_half_deduction: second_half_supported_miles * second_half_dollars_per_mile
  - total_deduction: first_half_deduction + second_half_deduction
expected:
  first_half_deduction: 4350
  second_half_deduction: 3040
  total_deduction: 7390
```

### Case 3: home office capped by the simplified method ([IRS simplified option](https://www.irs.gov/businesses/small-businesses-self-employed/simplified-option-for-home-office-deduction))

- A 400-square-foot room is used only and regularly for the business, and it is the principal place of business: the owner does the administrative and management work there and has no other fixed location for it ([Pub. 587](https://www.irs.gov/publications/p587)). Gross income from the business is well above its expenses.
- The simplified method counts at most 300 square feet: 300 × $5 = $1,500.
- If the regular method would give more, it may be used for this year instead. It requires actual expenses, and it may involve depreciation and later recapture for relevant owned property. The method choice is made on the timely filed original return and cannot be switched for that same year; depreciation/recapture applies only where actually relevant to the regular method and property facts.

### Case 4: which contractors get a Form 1099-NEC ([2026 instructions](https://www.irs.gov/instructions/i1099mec); [2025 instructions](https://www.irs.gov/pub/irs-prior/i1099mec--2025.pdf))

- In 2026 the business paid contractor A $1,800 and contractor B $2,000, both by ordinary bank transfer for qualifying business services. Assume US individual nonemployee payees, correct TINs, no applicable payee exemption or backup-withholding issue, and no section 6050W settlement transaction.
- A: $1,800 is under $2,000, so no Form 1099-NEC is required for 2026. The payment is still deductible if it is a business expense.
- B: $2,000 meets "$2,000 or more", so a Form 1099-NEC is due by February 1, 2027. The normal date is January 31, but January 31, 2027 is a Sunday.
- The same $1,800 paid in 2025 would have needed a Form 1099-NEC, because the 2025 threshold was $600 or more.
- For payment-card or qualifying third-party-network transactions actually reportable under section 6050W, apply the information-return exclusion from NEC/MISC. A payment app or ordinary electronic bank transfer alone does not prove that classification or that a processor actually filed.

### Case 5: 2026 estimated tax with the 110% rule ([Pub. 505 (2026)](https://www.irs.gov/publications/p505))

- 2025 AGI was $180,000 (more than $150,000) and 2025 tax was $30,000, on a 12-month return. The expected 2026 tax is $40,000, with no withholding.
- 90% of the 2026 tax: $40,000 × 90% = $36,000. 110% of the 2025 tax: $30,000 × 110% = $33,000.
- The required annual payment is the smaller amount, $33,000. Assuming ordinary equal-instalment facts, that is $8,250 each, due April 15, June 15 and September 15, 2026, and January 15, 2027. Uneven-income annualisation, actual withholding/credits and payment history are separate conditions.

### Case 6: gifts and meals ([Pub. 463](https://www.irs.gov/publications/p463))

- In 2026 the owner gives one client three gifts of $60 each, and pays $300 for business meals with clients.
- Gifts: the limit is $25 per person for the year, so $25 is deductible, not $180.
- Meals: $300 × 50% = $150 is deductible, if the records show the business purpose.

### Case 7: asset under the de minimis safe harbor ([IRS tangible property regulations](https://www.irs.gov/businesses/small-businesses-self-employed/tangible-property-final-regulations))

- A sole proprietor with no applicable financial statement buys a laptop on one invoice for $2,200, and a machine for $2,800.
- The business has expensed items under $2,500 on its books under a policy in place since January 1, 2026. With the election attached to the timely filed 2026 original return, the $2,200 laptop is deducted as an expense.
- The $2,800 machine is outside the $2,500 safe harbour. Test actual repair/material/current-deduction or capitalisation/section 179/depreciation rules; being over the safe-harbour amount does not alone mandate capitalisation.
- Without the election, both are tested under the normal capitalization rules.

### Case 8: hobby or business ([26 U.S.C. 183](https://uscode.house.gov/us/usc/119-120/t26/s183/); [Schedule C instructions](https://www.irs.gov/instructions/i1040sc))

- A photographer has made a profit in 2 of the last 5 years, including this one. The presumption needs 3 of 5, so it does not apply.
- That is not the end of the question. Look at the facts: a business plan, separate books, time spent, marketing, and changes made to become profitable. If these show a profit motive and regular work, it is a business on Schedule C.
- If it is a hobby, the income is reported as other income. Ordinary hobby operating expenses do not produce a Schedule C loss or an allowed miscellaneous itemized deduction after 2017. Otherwise-allowable section 183(b)(1) deductions need their own rules; do not make a blanket claim that every item is denied.

### Case 9: filing status when the data suggests "single" ([Pub. 501](https://www.irs.gov/publications/p501))

- The draft return used "single" because the status was unknown. The client was married on December 31.
- A married person cannot file as single. The choices are married filing jointly or married filing separately, or head of household only if the Pub. 501 tests for being considered unmarried are met.
- If the client's spouse had died during the year instead, the client is considered married for the whole year and may file jointly for that year if they did not remarry before year-end.

### Case 10: spouses who run a business together ([IRS: qualified joint venture](https://www.irs.gov/businesses/small-businesses-self-employed/election-for-married-couples-unincorporated-businesses))

- A married couple co-own a business in their own names, file jointly, and both materially participate. They both elect qualified joint venture treatment, so each spouse files a Schedule C and a Schedule SE for their share.
- The same business held through the couple's LLC does not qualify for the election. Outside a community property state it is a partnership: refer it. Inside one, check Rev. Proc. 2002-69 first.

## When to refuse or refer

- **Refer** partnerships, multi-member LLCs, S corporations and C corporations. Also refer a married couple's business that fails any qualified joint venture condition and is not covered by Rev. Proc. 2002-69.
- **Refer** a business with employees. Payroll (Forms 941, 940, W-2) is outside this skill, even when the business is a single-member LLC.
- **Refer** nonresident aliens and dual-status years to `us-tax-residency`.
- **Refer** foreign accounts or income. Assess a US person's financial interest or signature authority over foreign financial accounts, aggregate value over $10,000 at any time in the calendar year and actual filing exceptions before the FBAR conclusion ([FinCEN](https://www.fincen.gov/report-foreign-bank-and-financial-accounts)). Form 8938 may also be needed where the specified foreign financial asset thresholds are met; see `us-fbar-fatca-reporting`. Foreign income brings in the foreign tax credit and treaty rules.
- **Refer** digital asset activity. Apply the digital-asset question and transaction reporting on the actual tax-year Form 1040 ([IRS: digital assets](https://www.irs.gov/filing/digital-assets)). Use `us-capital-gains` for sales held as investments, and a professional for mining, staking or payment in digital assets.
- **Refer** rental real estate, K-1 income, and prior-year carryovers (net operating loss, capital loss, passive loss, charitable, §179 or home office carryovers). They need the prior-year return and their own rules.
- **Refer** open IRS notices, audits, balances due or unfiled years to `us-irs-collections-and-controversy`.
- **Refer** the sale of a home or of the business, or a death or divorce during the year. Use `us-capital-gains` for the gain rules, with professional review.
- **Refuse to state as settled:** any business-or-hobby conclusion that rests on missing facts, any worker classification where control is unclear, and any state tax result. Say what is uncertain and which official source settles it.

## Filing and payment ([IRS: when to file](https://www.irs.gov/filing/individuals/when-to-file); [IRS: extensions](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return); [Pub. 505 (2026)](https://www.irs.gov/publications/p505))

- **Return:** Form 1040 with Schedule C, and Schedule SE where net earnings are $400 or more ([Topic 554](https://www.irs.gov/taxtopics/tc554)). Calendar-year returns are due April 15 after the year ends. If that date falls on a weekend or legal holiday, it moves to the next business day. For 2026 returns, confirm the April 2027 date in the 2026 Form 1040 instructions once they are published.
- **Extension:** it gives until October 15 to **file**. It does not extend the time to **pay**. Tax unpaid after the April date draws interest and any late-payment penalty.
- **2026 estimated tax:** due April 15, June 15 and September 15, 2026, and January 15, 2027. Pub. 505 describes filing/paying the return by January 31 instead of the fourth instalment; because January 31, 2027 is Sunday, section 7503 moves the ordinary act deadline to February 1, 2027. This does not erase penalties for earlier missed instalments. [Pub. 505](https://www.irs.gov/publications/p505), [26 USC 7503](https://uscode.house.gov/us/usc/119-120/t26/s7503/).
- **Business information returns for 2026 payments:** Form 1099-NEC to the recipient and the IRS by February 1, 2027, because January 31, 2027 is a Sunday. Form 1099-MISC to the IRS by March 1, 2027 on paper (February 28, 2027 is a Sunday), or March 31, 2027 electronically. A due date on a weekend or legal holiday moves to the next business day. Check the 10-return e-file rule ([Form 1099-MISC and 1099-NEC instructions](https://www.irs.gov/instructions/i1099mec)).
- **Elections that ride on a timely filed original return:** the de minimis safe harbor election, the choice of home office method for the year, and the distinct standard-mileage first-year choice and its actual due-date/revocation rule. Do not assume every election has identical amended-return or relief rules; check the actual provision.

## 2025 returns: ordinary extended deadline October 15, 2026 has passed ([IRS: extensions](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return); [archived Schedule SE (2025)](https://www.irs.gov/pub/irs-prior/f1040sse--2025.pdf))

- Use the 2025 forms and the 2025 column of the figures table: 70 cents a mile for the whole of 2025 ([IRS standard mileage rates](https://www.irs.gov/tax-professionals/standard-mileage-rates)), and a social security wage base of $176,100 ([archived Schedule SE (2025)](https://www.irs.gov/pub/irs-prior/f1040sse--2025.pdf)).
- Section 179 for 2025 is $2,500,000, reduced above $4,000,000, as amended by P.L. 119-21 ([Rev. Proc. 2025-32 §3](https://www.irs.gov/irb/2025-45_IRB)). Older 2025 tables printed before the law changed are out of date.
- Forms 1099-NEC for 2025 payments used the $600 threshold and were ordinarily due February 2, 2026, because January 31 was Saturday ([2025 instructions](https://www.irs.gov/pub/irs-prior/i1099mec--2025.pdf)). If some were missed, file them now. Penalties for late information returns are handled in `us-irs-collections-and-controversy`.
- An extension to October 15, 2026 covered filing only. Tax was due by April 15, 2026, so interest runs from that date.
- The Pub. 463 rules on meals, gifts and receipts cited here are from the 2025 edition, which applies to 2025 returns ([Pub. 463](https://www.irs.gov/publications/p463)).

## Completion checklist

- The tax year, actual filing status and source edition are stated; do not call expired 2025 ordinary extension still open. In 2026, split business mileage at July 1 using supported dated miles.
- The filing status comes from marital status on December 31 and was not assumed.
- Residence is confirmed, or the case has gone to `us-tax-residency`.
- The entity is classified: sole proprietor, disregarded single-member LLC, or qualified joint venture, with every condition met. Nothing that is a partnership or corporation is on Schedule C.
- The business-or-hobby question is answered on facts ([26 U.S.C. 183](https://uscode.house.gov/us/usc/119-120/t26/s183/)).
- Gross receipts tie to bank deposits and to every Form 1099. Transfers, loans and capital are excluded, with the reason recorded.
- Each expense is business, ordinary and necessary. The meals, gifts, vehicle, home office and capitalization limits are applied ([Pub. 463](https://www.irs.gov/publications/p463)).
- Travel/gift/car substantiation and actual exceptions are established. Latest detailed 2025-cycle receipt guidance covers lodging/other expenses $75 or more, receipt-unavailable transport and lawful casualty reconstruction, not a universal original-receipt denial.
- Workers are classified. W-9s are on file. Forms 1099-NEC are issued at the right threshold for the payment year ($2,000 or more in 2026; $600 or more in 2025).
- SE tax is tested at $400 of net earnings, and the return has gone through `us-federal-return-assembly`.
- The 2026 estimated tax is set against the right safe harbor, including 110% where 2025 AGI was more than $150,000 ($75,000 MFS).
- Every provisional treatment is resolved or disclosed, and nothing is filed on a guess ([26 U.S.C. 6694](https://uscode.house.gov/us/usc/119-124/t26/s6694/)).
- Referral items are listed, and state tax is flagged as a separate check.

## Sources

| Source and what was actually read | Official URL | Read on |
|---|---|---|
| FinCEN FBAR. Read for US-person financial-interest/signature-authority aggregate calendar-year threshold; complete exception analysis is not supplied here | https://www.fincen.gov/report-foreign-bank-and-financial-accounts | 2026-11-14 |
| IRS backup withholding. Read for current rate, correct-TIN/underreporting/certification triggers and listed reportable payment classes; not every payee exemption | https://www.irs.gov/businesses/small-businesses-self-employed/backup-withholding | 2026-11-14 |
| IRS QJV election. Read for complete qualifying conditions, state-law entity exclusion/community-property referral and allocation/Schedule C/SE reporting | https://www.irs.gov/businesses/small-businesses-self-employed/election-for-married-couples-unincorporated-businesses | 2026-11-14 |
| IRS record retention. Read for ordinary/credit-refund/omission/bad-debt/fraud/nonfiling/employment periods, early-filed treatment and property/basis retention | https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records | 2026-11-14 |
| IRS worker classification. Read for actual common-law control/financial/relationship factors, no single-factor rule and SS-8 referral | https://www.irs.gov/businesses/small-businesses-self-employed/independent-contractor-self-employed-or-employee | 2026-11-14 |
| IRS simplified home office. Read for full operative method table, square-foot/rate/income limit, depreciation/recapture and current/prior-year carryover/choice distinctions | https://www.irs.gov/businesses/small-businesses-self-employed/simplified-option-for-home-office-deduction | 2026-11-14 |
| IRS SMLLC. Read for entity/election, activity-appropriate Schedule C/E/F and separate employment/excise treatment; not every special entity election | https://www.irs.gov/businesses/small-businesses-self-employed/single-member-limited-liability-companies | 2026-11-14 |
| IRS tangible-property FAQs. Read for safe-harbour amounts, actual AFS categories, start-of-year book policy/writing, annual timely-original-return election and over-ceiling does-not-mandate-capitalisation distinction | https://www.irs.gov/businesses/small-businesses-self-employed/tangible-property-final-regulations | 2026-11-14 |
| IRS digital assets. Read for opening property/reporting and actual-return-question workstream; not a completed mining/staking or broker calculation | https://www.irs.gov/filing/digital-assets | 2026-11-14 |
| IRS extensions. Read for ordinary application/file versus payment dates and existence of special overseas/military relief; not a particular taxpayer relief determination | https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return | 2026-11-14 |
| IRS when-to-file. Read for currently displayed 2025-cycle April 2026 calendar deadline, fiscal-year and weekend/holiday rule; not final 2026 Form 1040 instructions | https://www.irs.gov/filing/individuals/when-to-file | 2026-11-14 |
| IRS 2025 Schedule C instructions. Read for activity test/entity/information-return opening, gross receipts and line6 recoveries/refunds, expense/capitalisation and relevant home-office references; latest 2025-2026 filing-cycle source, not the whole instruction | https://www.irs.gov/instructions/i1040sc | 2026-11-14 |
| IRS information-return instructions served as revision December 2026. Read for actual 2026 threshold/e-file/date/settlement-payment sections and attorney fees/gross-proceeds distinction; revision label recorded as served on this read date | https://www.irs.gov/instructions/i1099mec | 2026-11-14 |
| IRS Pub.463, 2025 edition. Read for selected meals/gifts, standard-mileage eligibility/choice/actual-cost distinction, commuting and chapter5 adequate/documentary/corroborating/casualty evidence; latest 2025-2026 detailed guide, not every travel example | https://www.irs.gov/publications/p463 | 2026-11-14 |
| IRS Pub.501, 2025 edition. Read for marital last-day/death/remarriage and available filing-status discussion; no 2025 deduction/age threshold imported as 2026 | https://www.irs.gov/publications/p501 | 2026-11-14 |
| IRS Pub.505 2026. Read for general required-estimated-tax test, high-income/farming exceptions, annual-payment and payment-period dates, January-return alternative and Social Security base; not every withholding worksheet | https://www.irs.gov/publications/p505 | 2026-11-14 |
| IRS Pub.587 2025. Read for principal-place/exclusive/regular-use, separate-structure, storage and daycare sections referenced for actual eligibility; latest 2025-cycle guide | https://www.irs.gov/publications/p587 | 2026-11-14 |
| IRS mileage rates. Read for current July-to-December 2026, January-to-June 2026 and historical 2025 business rows; other uses not adopted | https://www.irs.gov/tax-professionals/standard-mileage-rates | 2026-11-14 |
| IRS Topic554. Read for ordinary earnings/threshold/rate, optional-method/church exception identification and half-SE deduction; not every specialist optional-method computation | https://www.irs.gov/taxtopics/tc554 | 2026-11-14 |
| Official US Code section183. Read for complete subsections a to d, otherwise-allowable deductions and rebuttable profit-presumption conditions; official text current through October2026 | https://uscode.house.gov/us/usc/119-120/t26/s183/ | 2026-11-14 |
| Official US Code section67. Read for subsection h permanent post-2017 miscellaneous deduction disallowance and relevant definition distinctions, not every trust/educator exception | https://uscode.house.gov/us/usc/119-120/t26/s67/ | 2026-11-14 |
| Official US Code section6694. Read for subsection a ordinary/disclosed/shelter/reportable standards and reasonable-cause/good-faith exception plus b willful/reckless distinction; not penalty collection proceedings | https://uscode.house.gov/us/usc/119-124/t26/s6694/ | 2026-11-14 |
| Official US Code section274. Read for b gift limit/promotional/spousal rules, d adequate/corroborating substantiation, n ordinary meals/actual exceptions and transport-duty percentage; not every employer meal or facility exception | https://uscode.house.gov/us/usc/119-120/t26/s274/ | 2026-11-14 |
| Official US Code section7503. Read for complete operative next-business-day, authorised extension and legal-holiday rule | https://uscode.house.gov/us/usc/119-120/t26/s7503/ | 2026-11-14 |
| IRS Rev.Proc.2025-32. Read for section2.10/section3 corrected 2025 expensing values and section4.24 2026 limits/phase-out/SUV; not every inflation figure | https://www.irs.gov/irb/2025-45_IRB | 2026-11-14 |
| IRS 2025 information-return PDF. Read for first-page filing/e-file/settlement distinction and 2025 service-reporting threshold sections; use actual historical year | https://www.irs.gov/pub/irs-prior/i1099mec--2025.pdf | 2026-11-14 |
| Archived 2025 Schedule SE. Read for header and ordinary Part I earnings/base/rates; the rolling current URL now serves 2026 and is not a 2025 citation | https://www.irs.gov/pub/irs-prior/f1040sse--2025.pdf | 2026-11-14 |
| Current 2026 Schedule SE. Read for actual header and ordinary Part I lines4a to13, combined base/earnings/rates and half-tax deduction; no completed client return claimed | https://www.irs.gov/pub/irs-pdf/f1040sse.pdf | 2026-11-14 |

Not yet confirmed: final 2026 Form1040/full-return assembly instructions and each actual taxpayer's filing/election eligibility, accounting method, substantiation, deductions/credits/carryovers and disaster/overseas/other special relief; current 2026 detailed Pub.463/Pub.501/Pub.587 revisions beyond the latest published 2025-2026 filing-cycle explanations read here, including every regulatory receipt exception; complete section179 property/income limitations and each amended/late election relief; full QJV community-property Rev.Proc.2002-69 analysis, reportable/shelter positions and specialist preparer issues; actual exempt-payee/settlement/backup-withholding conditions, FBAR exceptions, foreign forms, digital assets and all state/local outcomes. Published rates/limits explicitly verified above are retained, while these unresolved conditions are not supplied by a generic greater-tax default or a source link alone.
