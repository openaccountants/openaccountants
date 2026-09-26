---
name: us-tax-workflow-base
description: Tier 1 workflow base for US federal income tax skills serving sole proprietors and single-member LLCs disregarded for federal tax. Contains the workflow runbook, conservative defaults principle, structured intake form, reviewer-oriented output spec, self-checks, global refusal catalogue, citation discipline, and content skill slot contract. Workflow architecture only — no tax content, no rates, no thresholds, no form line references, no year-specific figures. MUST be loaded alongside at least one content skill (e.g., us-sole-prop-bookkeeping, us-schedule-c-and-se-computation, us-form-1040-self-employed-positions, us-quarterly-estimated-tax) that provides actual federal tax rules and current-year figures. Assumes a human reviewer credentialed under Circular 230 (Enrolled Agent, CPA, or attorney) reviews and signs off on every output before it reaches the taxpayer or the IRS. Federal-only in scope. State income tax skills may load it for workflow scaffolding but the base does not address state tax.
version: 0.2
jurisdiction: US
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US federal workflow for individual and self-employed returns: 2026 method, with 2025 return notes

Figures are for tax year 2026 unless a line says 2025. The 2026 amounts come from Rev. Proc. 2025-32 and from IRS pages updated for the One Big Beautiful Bill Act (P.L. 119-21). A dated section covers 2025 returns, which are due by October 15, 2026 if the taxpayer got an extension.

This Guide is the front door for a US federal Form 1040 with self-employment income. It sets the order of work, the facts to collect, how to sort income and expenses, the records that must exist, and when to stop and refer.

## Scope and who this is for

- **Covers:** US citizens and resident aliens who file Form 1040 and run a business as a sole proprietor, or through a single-member LLC that is disregarded for federal income tax. It also covers a married couple running a business as a qualified joint venture. The business is reported on Schedule C.
- **Does not cover:** partnerships and multi-member LLCs, S and C corporations, estates and trusts, nonresident aliens, and employer payroll. State and local tax is also out of scope. Each state has its own rules, so check that state's own revenue department before giving a combined answer.
- **Companion Guides (use them instead of repeating their rules here):**
  - `us-federal-return-assembly`: the order of Schedule SE, retirement, self-employed health insurance, QBI, Schedules 1, 1-A and 2, and the Form 2210 penalty.
  - `us-1099-k-and-payment-processors`: Form 1099-K, payment apps, and reconciling Box 1a to Schedule C.
  - `us-capital-gains`: sales of shares, funds, digital assets held as investments, and a home.
  - `us-secure-2-and-retirement-updates`: plan limits and SEP, SIMPLE and solo 401(k) rules.
  - `us-tax-residency`: whether the person is a resident alien at all.
  - `us-irs-collections-and-controversy`: notices, audits, unpaid balances and penalties.
- **Who reads the output.** Where a preparer uses this Guide, a person who can sign the return reviews every position before filing. Where a taxpayer uses it directly, it explains the method and says clearly what needs a professional.

## Ask the client first

- Which tax year is this: 2025 (now only on extension) or 2026? Every figure below depends on the year.
- Marital status on December 31 of that year, whether a spouse died during the year, and whether anyone can claim the taxpayer as a dependent. Filing status follows marital status on the last day of the year. If a spouse died during the year, the taxpayer is considered married for the whole year ([Pub. 501](https://www.irs.gov/publications/p501)).
- Was the taxpayer a US citizen or resident alien for the whole year? If not, stop and use `us-tax-residency`.
- How is the business held: in the owner's own name, through an LLC, or co-owned with a spouse or anyone else? Has any Form 8832 or Form 2553 election ever been filed?
- What does the business do, since when, and in which years did it make a profit? Does the owner work in it regularly?
- Every income source: Forms 1099-NEC, 1099-MISC and 1099-K, cash, checks and payment-app receipts. Income is reportable whether or not a form arrived.
- Bank and card statements for every account the business used, including personal accounts that carried business payments.
- Vehicles: how many are used in the business, the date each was first used for business, business and total miles, and whether a mileage log exists.
- Home office: square footage used only and regularly for the business, and the total square footage of the home. Is that space the principal place of business, a place to meet clients or customers, or a separate structure? Is it used for storing inventory or for daycare ([Pub. 587](https://www.irs.gov/publications/p587))?
- Equipment bought during the year: cost per invoice or item, date placed in service, and whether the business has audited financial statements.
- People paid for services: names, amounts paid in the year, how they were paid, and whether a Form W-9 was collected.
- Wages from any job, estimated tax payments already made, and the prior year's tax and adjusted gross income (AGI).
- Anything that may take the return outside this Guide: employees, foreign accounts or income, digital assets, rental property, K-1s, open IRS notices, unfiled years.

## The method, step by step

1. **Fix the year and the filing status first.** Use marital status on the last day of the year. If a spouse died during the year, the taxpayer is considered married for the whole year. If more than one filing status applies, the taxpayer may choose the one with the lowest tax ([Pub. 501](https://www.irs.gov/publications/p501)). Never assume a status. A married person cannot file as single, so a default of "single" can produce an invalid return. If the status is unknown, ask.
2. **Confirm residence.** This Guide assumes a US citizen or resident alien for the full year. For a first or last year in the US, or a dual-status year, use `us-tax-residency` before anything else.
3. **Classify the entity** ([IRS: single-member LLCs](https://www.irs.gov/businesses/small-businesses-self-employed/single-member-limited-liability-companies)). A single-member LLC is disregarded for income tax unless it files Form 8832 and elects to be a corporation. Its activity then goes on the owner's Schedule C. It is still a separate entity for employment tax and certain excise taxes. An LLC with at least two members is a partnership unless it elects corporate status. Stop and refer if the business is a partnership or a corporation.
4. **Test spouse-owned businesses** ([IRS: qualified joint venture](https://www.irs.gov/businesses/small-businesses-self-employed/election-for-married-couples-unincorporated-businesses)). A business co-owned by a married couple is generally a partnership. It can instead be a qualified joint venture, with each spouse filing a Schedule C, only if **all** of these hold: the only members are the married couple, they file a joint return, **both** spouses materially participate, and **both** elect. A business held through an LLC does not qualify. For a married couple's LLC in a community property state, check Rev. Proc. 2002-69 before choosing the treatment.
5. **Decide business or hobby.** An activity is a business if its primary purpose is income or profit and the owner is involved with continuity and regularity. A sporadic activity or a hobby is not a business ([Schedule C instructions](https://www.irs.gov/instructions/i1040sc)). There is a presumption of profit motive if gross income exceeds deductions in 3 or more of the 5 consecutive years ending with the current year. For horse breeding, training, showing or racing it is 2 of 7 years ([26 U.S.C. 183](https://www.law.cornell.edu/uscode/text/26/183)). Hobby income is still taxable. Hobby expenses give no deduction, because miscellaneous itemized deductions are disallowed for every tax year beginning after December 31, 2017. P.L. 119-21 removed the old end date ([26 U.S.C. 67(h)](https://www.law.cornell.edu/uscode/text/26/67)).
6. **Build gross receipts from the bank, not from the forms.** Start with deposits to every account the business used. Take out transfers between the owner's own accounts, loans, the owner's own capital, and refunds of expenses. Then tie the result to each Form 1099-NEC, 1099-MISC and 1099-K. Card and payment-network receipts are reported on Form 1099-K by the payment settlement entity, not on Form 1099-NEC ([Form 1099-MISC and 1099-NEC instructions](https://www.irs.gov/instructions/i1099mec)). For the reconciliation, use `us-1099-k-and-payment-processors`.
7. **Classify each expense.** Deduct it only if it is an ordinary and necessary cost of this business and not personal. Then apply the limits in "Figures for 2026" below: meals, gifts, vehicles, home office, and whether an asset is expensed or capitalized. Entertainment is not deductible, and neither is commuting between home and a regular place of work ([Pub. 463](https://www.irs.gov/publications/p463)).
8. **Check that the records exist.** Travel, gifts and cars need records of the amount, the date, the place and the business purpose. The taxpayer needs documentary evidence such as receipts for lodging, and for any other expense of $75 or more ([Pub. 463](https://www.irs.gov/publications/p463)). No record means no deduction for these items, however likely the spending was.
9. **Work out the business's own filing duties to others.** Decide whether each person paid was a worker or an independent contractor (see the boundary table). Collect a Form W-9 before paying. Then decide which Forms 1099-NEC and 1099-MISC are due for the year the payments were made ([Form 1099-MISC and 1099-NEC instructions](https://www.irs.gov/instructions/i1099mec)).
10. **Test self-employment tax.** SE tax usually applies when net earnings from self-employment are $400 or more. Net earnings are generally 92.35% of net profit ([Topic 554](https://www.irs.gov/taxtopics/tc554)). Then use `us-federal-return-assembly` for Schedule SE, the retirement and health insurance deductions, and QBI, in that order.
11. **Test estimated tax for the coming year** (see the 2026 figures). A new or growing business often owes estimated tax for the first time.
12. **Record every open fact as an open fact.** Where a fact is missing, use the provisional treatment in the defaults table below, flag it, and ask. Do not file on a provisional treatment. Resolve it, or take the position the facts support and disclose it where needed.
13. **Review before filing.** The return may be signed only when every position has authority behind it. A preparer is penalized for an understatement due to an undisclosed position without substantial authority. For a disclosed position, the test is a reasonable basis ([26 U.S.C. 6694](https://www.law.cornell.edu/uscode/text/26/6694)).

## Figures for 2026, with years ([Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Pub. 505 (2026)](https://www.irs.gov/publications/p505); [IRS standard mileage rates](https://www.irs.gov/tax-professionals/standard-mileage-rates))

| Item | 2026 | 2025 | Condition that decides it |
| --- | --- | --- | --- |
| Business standard mileage rate | 72.5 cents a mile from January 1 to June 30; 76 cents a mile from July 1 to December 31 | 70 cents a mile | 2026 has two rates. Apply each to the miles driven in its own period ([IRS standard mileage rates](https://www.irs.gov/tax-professionals/standard-mileage-rates)) |
| Simplified home office | $5 a square foot, up to 300 square feet | Same | Part of the home used exclusively and regularly as the principal place of business or to meet clients, or a separate structure used for the business. Storage and daycare have their own rules ([IRS simplified option](https://www.irs.gov/businesses/small-businesses-self-employed/simplified-option-for-home-office-deduction); [Pub. 587](https://www.irs.gov/publications/p587)) |
| De minimis safe harbor, no audited financial statement | $2,500 per invoice or item | Same | Annual election on a timely filed original return, and the amounts must be expensed on the books under a policy in place at the start of the year ([IRS tangible property regulations](https://www.irs.gov/businesses/small-businesses-self-employed/tangible-property-final-regulations)) |
| De minimis safe harbor, with an applicable financial statement | $5,000 per invoice or item | Same | Same election. The book policy must be in writing ([IRS tangible property regulations](https://www.irs.gov/businesses/small-businesses-self-employed/tangible-property-final-regulations)) |
| Section 179 expensing limit | $2,560,000 | $2,500,000 | Reduced dollar for dollar once §179 property placed in service in the year exceeds the phase-out amount ([Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)) |
| Section 179 phase-out starts above | $4,090,000 | $4,000,000 | See the row above |
| Section 179 limit for a sport utility vehicle | $32,000 | Not shown here; check the 2025 Form 4562 instructions | Applies to the cost of an SUV taken into account under §179 |
| Business meals | 50% deductible | Same | 80% for someone subject to Department of Transportation hours-of-service limits ([Pub. 463](https://www.irs.gov/publications/p463)) |
| Business gifts | $25 per recipient per year | Same | Counts gifts given directly or indirectly to each person ([Pub. 463](https://www.irs.gov/publications/p463)) |
| Receipts required for | Lodging, and any other expense of $75 or more | Same | [Pub. 463](https://www.irs.gov/publications/p463) |
| Form 1099-NEC nonemployee compensation | $2,000 or more | $600 or more | The payment year decides. The $2,000 applies from 2026 and may be adjusted for inflation from 2027 ([2026 instructions](https://www.irs.gov/instructions/i1099mec); [2025 instructions](https://www.irs.gov/pub/irs-prior/i1099mec--2025.pdf)) |
| Form 1099-MISC gross proceeds paid to an attorney | $600 or more | $600 or more | Box 10. This one did not move to $2,000 ([2026 instructions](https://www.irs.gov/instructions/i1099mec)) |
| Backup withholding rate | 24% | 24% | Applies when a payee does not give a correct TIN, among other cases ([IRS backup withholding](https://www.irs.gov/businesses/small-businesses-self-employed/backup-withholding)) |
| Self-employment tax applies | Net earnings of $400 or more | Same | [Topic 554](https://www.irs.gov/taxtopics/tc554) |
| Share of net profit that counts as net earnings | 92.35% | Same | [Topic 554](https://www.irs.gov/taxtopics/tc554) |
| SE tax rates | 12.4% social security plus 2.9% Medicare | Same | Social security part only up to the wage base ([Topic 554](https://www.irs.gov/taxtopics/tc554)) |
| Social security wage base | $184,500 | $176,100 | Wages already taxed for social security use up part of the base ([Pub. 505 (2026)](https://www.irs.gov/publications/p505); [Schedule SE (2025)](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf)) |
| Estimated tax needed if expected balance due is | At least $1,000 | Same | And withholding and credits fall short of the safe harbor. The prior-year test needs a 2025 return covering all 12 months ([Pub. 505 (2026)](https://www.irs.gov/publications/p505)) |
| Safe harbor | Smaller of 90% of 2026 tax or 100% of 2025 tax | Not repeated here | The 2025 return must cover 12 months. 110% instead of 100% if 2025 AGI was more than $150,000 ($75,000 if married filing separately for 2026), unless at least two-thirds of gross income is from farming or fishing ([Pub. 505 (2026)](https://www.irs.gov/publications/p505)) |

The QBI thresholds, the Additional Medicare Tax and the net investment income tax are in `us-federal-return-assembly` and `us-capital-gains`. They are not repeated here.

## Boundaries and exceptions ([Pub. 463](https://www.irs.gov/publications/p463); [IRS: employee or contractor](https://www.irs.gov/businesses/small-businesses-self-employed/independent-contractor-self-employed-or-employee))

| Rule | The condition that decides it | Source |
| --- | --- | --- |
| Standard mileage rate: first year | For a car the taxpayer owns, the standard rate must be chosen in the **first year** the car is available for business use. In later years, either method can be used. For a leased car, the standard rate must be used for the whole lease period. | [Pub. 463](https://www.irs.gov/publications/p463) |
| Standard mileage rate: not allowed | Not allowed if five or more cars are used **at the same time**, or if the car was depreciated under MACRS, by any method other than straight line, or under §179. Also not allowed if the special depreciation allowance (bonus depreciation) was claimed on the car, or, for a leased car, if actual car expenses were claimed after 1997. | [Pub. 463](https://www.irs.gov/publications/p463) |
| Commuting | Travel between home and a regular place of work is personal. Travel from home to a temporary work location outside the metropolitan area is deductible. If the taxpayer has one or more regular work locations away from home, trips between home and a temporary work location in the same business are deductible regardless of distance. If home is the principal place of business, trips between home and another work location in the same business are deductible, whether the work is temporary or permanent and regardless of distance. | [Pub. 463](https://www.irs.gov/publications/p463) |
| Home office | Only the part of the home used **exclusively** and **regularly** as (a) the principal place of business, or (b) a place where the taxpayer meets or deals with patients, clients or customers in the normal course of business; or (c) a separate structure not attached to the home, used in connection with the business. Storage of inventory or product samples, and daycare, have their own rules ([Pub. 587](https://www.irs.gov/publications/p587)). The method is chosen on the timely filed original return and cannot be changed for that year. The deduction cannot exceed the gross income from the business use of the home, less business expenses. Under the simplified method any excess is lost, and there is no depreciation and no later recapture. The method can be changed from year to year. An employee working from home gets no home office deduction. | [IRS simplified option](https://www.irs.gov/businesses/small-businesses-self-employed/simplified-option-for-home-office-deduction) |
| De minimis safe harbor | The amounts must also be expensed on the books under a consistent accounting procedure in place at the start of the tax year. With an applicable financial statement (AFS) the procedure must be written; without one it need not be. Attach a statement titled "Section 1.263(a)-1(f) de minimis safe harbor election" to the timely filed **original** return, including extensions, for each year it applies. An item costing more than the limit is not covered by the safe harbor, but may still be deductible under other rules. | [IRS tangible property regulations](https://www.irs.gov/businesses/small-businesses-self-employed/tangible-property-final-regulations) |
| Entertainment and meals | Entertainment is not deductible. Food and drink bought separately from entertainment, or shown separately on the invoice, is a meal subject to the 50% limit. | [Pub. 463](https://www.irs.gov/publications/p463) |
| Worker or contractor | The test is the right to control what is done and how it is done, looking at behavioral control, financial control and the type of relationship. If it is still unclear, Form SS-8 can be filed. A worker who is an employee takes the business outside this Guide. | [IRS: employee or contractor](https://www.irs.gov/businesses/small-businesses-self-employed/independent-contractor-self-employed-or-employee) |
| Form 1099-NEC due date | January 31 after the payment year, on paper or electronically. A due date on a weekend or legal holiday moves to the next business day. January 31, 2027 is a Sunday, so 2026 forms are due February 1, 2027. | [Form 1099-MISC and 1099-NEC instructions](https://www.irs.gov/instructions/i1099mec) |
| E-filing information returns | Required if the business files 10 or more information returns in total (all types counted together), for returns due on or after January 1, 2024. | [Form 1099-MISC and 1099-NEC instructions](https://www.irs.gov/instructions/i1099mec) |
| Single-member LLC with employees | Disregarded for income tax, but a separate entity for employment tax. Payroll is outside this Guide. | [IRS: single-member LLCs](https://www.irs.gov/businesses/small-businesses-self-employed/single-member-limited-liability-companies) |
| Hobby presumption | Needs gross income above deductions in 3 or more of the 5 years ending with this year (2 of 7 for horses). Failing it is not proof of a hobby. It only removes the presumption. | [26 U.S.C. 183(d)](https://www.law.cornell.edu/uscode/text/26/183) |
| Records: how long | Generally 3 years after filing. For a refund claim filed later, 3 years from filing the original return or 2 years from paying the tax, whichever is later. 6 years if unreported income is more than 25% of the gross income shown. 7 years for a claim for a loss from worthless securities or a bad debt deduction. Indefinitely if no return or a fraudulent return was filed. Employment tax records: at least 4 years after the tax becomes due or is paid, whichever is later. | [IRS: how long to keep records](https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records) |

## Provisional treatments while a fact is missing ([Pub. 463](https://www.irs.gov/publications/p463); [26 U.S.C. 6694](https://www.law.cornell.edu/uscode/text/26/6694))

Use these only as working positions in the file. Each one must be flagged, turned into a question, and resolved before filing. They are not filing positions. The return must show the correct tax, not the highest one.

| Missing fact | Provisional treatment | What resolves it |
| --- | --- | --- |
| Filing status | None. Ask; do not assume "single". | Marital status on December 31 ([Pub. 501](https://www.irs.gov/publications/p501)) |
| Business-use share of a car | No vehicle deduction | A mileage log or other record of business and total miles |
| Substantiation for travel, gifts or a car | Not deductible | Records of the amount, date, place and business purpose |
| Whether a deposit is income | Treat as income | Evidence it was a transfer, loan, capital or refund |
| Whether an activity is a business | Flag. Do not deduct losses until settled. | The facts in step 5 |
| Whether a de minimis election was made in a past year | Not made. It is an annual election. | Check the return for that year |
| Whether estimated tax was paid | Not paid | IRS account transcript or payment confirmations |
| Whether a payee gave a TIN | Treat as missing. Check backup withholding. | A signed Form W-9 |

## Worked cases

The amounts in these cases are made up for illustration. The rates, limits and thresholds come from the sources linked in each heading.

### Case 1: SE tax on a 2026 Schedule C profit ([Topic 554](https://www.irs.gov/taxtopics/tc554))

- A single freelancer has 2026 Schedule C net profit of $60,000 and no wages.
- Net earnings: $60,000 × 92.35% = $55,410. That is $400 or more, so SE tax applies.
- Social security part: $55,410 × 12.4% = $6,870.84. The wage base of $184,500 is not reached.
- Medicare part: $55,410 × 2.9% = $1,606.89.
- SE tax: $6,870.84 + $1,606.89 = $8,477.73. Half of it (about $4,239) is an adjustment to income. Finish the return in `us-federal-return-assembly`.

### Case 2: 2026 mileage across the mid-year rate change ([IRS standard mileage rates](https://www.irs.gov/tax-professionals/standard-mileage-rates))

- One car, owned, used for business since 2024 with the standard rate chosen that year. There is a mileage log.
- Business miles January 1 to June 30: 6,000 at 72.5 cents = $4,350.
- Business miles July 1 to December 31: 4,000 at 76 cents = $3,040.
- Vehicle deduction: $4,350 + $3,040 = $7,390. Using a single rate for the whole year would be wrong.

### Case 3: home office capped by the simplified method ([IRS simplified option](https://www.irs.gov/businesses/small-businesses-self-employed/simplified-option-for-home-office-deduction))

- A 400-square-foot room is used only and regularly for the business, and it is the principal place of business: the owner does the administrative and management work there and has no other fixed location for it ([Pub. 587](https://www.irs.gov/publications/p587)). Gross income from the business is well above its expenses.
- The simplified method counts at most 300 square feet: 300 × $5 = $1,500.
- If the regular method would give more, it may be used for this year instead. It requires actual expenses, and it brings depreciation and later recapture. The choice is made on the timely filed original return and cannot be changed for that year.

### Case 4: which contractors get a Form 1099-NEC ([2026 instructions](https://www.irs.gov/instructions/i1099mec); [2025 instructions](https://www.irs.gov/pub/irs-prior/i1099mec--2025.pdf))

- In 2026 the business paid contractor A $1,800 and contractor B $2,000, both by bank transfer and both for services.
- A: $1,800 is under $2,000, so no Form 1099-NEC is required for 2026. The payment is still deductible if it is a business expense.
- B: $2,000 meets "$2,000 or more", so a Form 1099-NEC is due by February 1, 2027. The normal date is January 31, but January 31, 2027 is a Sunday.
- The same $1,800 paid in 2025 would have needed a Form 1099-NEC, because the 2025 threshold was $600 or more.
- If either contractor had been paid by card or a payment network, the payment would go on the processor's Form 1099-K, not on a Form 1099-NEC.

### Case 5: 2026 estimated tax with the 110% rule ([Pub. 505 (2026)](https://www.irs.gov/publications/p505))

- 2025 AGI was $180,000 (more than $150,000) and 2025 tax was $30,000, on a 12-month return. The expected 2026 tax is $40,000, with no withholding.
- 90% of the 2026 tax: $40,000 × 90% = $36,000. 110% of the 2025 tax: $30,000 × 110% = $33,000.
- The required annual payment is the smaller amount, $33,000. In four equal installments that is $8,250 each, due April 15, June 15 and September 15, 2026, and January 15, 2027.

### Case 6: gifts and meals ([Pub. 463](https://www.irs.gov/publications/p463))

- In 2026 the owner gives one client three gifts of $60 each, and pays $300 for business meals with clients.
- Gifts: the limit is $25 per person for the year, so $25 is deductible, not $180.
- Meals: $300 × 50% = $150 is deductible, if the records show the business purpose.

### Case 7: asset under the de minimis safe harbor ([IRS tangible property regulations](https://www.irs.gov/businesses/small-businesses-self-employed/tangible-property-final-regulations))

- A sole proprietor with no applicable financial statement buys a laptop on one invoice for $2,200, and a machine for $2,800.
- The business has expensed items under $2,500 on its books under a policy in place since January 1, 2026. With the election attached to the timely filed 2026 original return, the $2,200 laptop is deducted as an expense.
- The $2,800 machine is over $2,500. It is outside the safe harbor, so capitalize it, or consider §179 or other depreciation rules.
- Without the election, both are tested under the normal capitalization rules.

### Case 8: hobby or business ([26 U.S.C. 183](https://www.law.cornell.edu/uscode/text/26/183); [Schedule C instructions](https://www.irs.gov/instructions/i1040sc))

- A photographer has made a profit in 2 of the last 5 years, including this one. The presumption needs 3 of 5, so it does not apply.
- That is not the end of the question. Look at the facts: a business plan, separate books, time spent, marketing, and changes made to become profitable. If these show a profit motive and regular work, it is a business on Schedule C.
- If it is a hobby, the income is reported as other income. The expenses give no deduction for any year after 2017.

### Case 9: filing status when the data suggests "single" ([Pub. 501](https://www.irs.gov/publications/p501))

- The draft return used "single" because the status was unknown. The client was married on December 31.
- A married person cannot file as single. The choices are married filing jointly or married filing separately, or head of household only if the Pub. 501 tests for being considered unmarried are met.
- If the client's spouse had died during the year instead, the client is considered married for the whole year and may file jointly for that year if they did not remarry before year-end.

### Case 10: spouses who run a business together ([IRS: qualified joint venture](https://www.irs.gov/businesses/small-businesses-self-employed/election-for-married-couples-unincorporated-businesses))

- A married couple co-own a business in their own names, file jointly, and both materially participate. They both elect qualified joint venture treatment, so each spouse files a Schedule C and a Schedule SE for their share.
- The same business held through the couple's LLC does not qualify for the election. Outside a community property state it is a partnership: refer it. Inside one, check Rev. Proc. 2002-69 first.

## When to refuse or refer

- **Refer** partnerships, multi-member LLCs, S corporations and C corporations. Also refer a married couple's business that fails any qualified joint venture condition and is not covered by Rev. Proc. 2002-69.
- **Refer** a business with employees. Payroll (Forms 941, 940, W-2) is outside this Guide, even when the business is a single-member LLC.
- **Refer** nonresident aliens and dual-status years to `us-tax-residency`.
- **Refer** foreign accounts or income. A US person must file an FBAR when foreign accounts total more than $10,000 at any time in the year ([FinCEN](https://www.fincen.gov/report-foreign-bank-and-financial-accounts)). Form 8938 may also be needed where the specified foreign financial asset thresholds are met; see `us-fbar-fatca-reporting`. Foreign income brings in the foreign tax credit and treaty rules.
- **Refer** digital asset activity. Every Form 1040 asks the digital asset question ([IRS: digital assets](https://www.irs.gov/filing/digital-assets)). Use `us-capital-gains` for sales held as investments, and a professional for mining, staking or payment in digital assets.
- **Refer** rental real estate, K-1 income, and prior-year carryovers (net operating loss, capital loss, passive loss, charitable, §179 or home office carryovers). They need the prior-year return and their own rules.
- **Refer** open IRS notices, audits, balances due or unfiled years to `us-irs-collections-and-controversy`.
- **Refer** the sale of a home or of the business, or a death or divorce during the year. Use `us-capital-gains` for the gain rules, with professional review.
- **Refuse to state as settled:** any business-or-hobby conclusion that rests on missing facts, any worker classification where control is unclear, and any state tax result. Say what is uncertain and which official source settles it.

## Filing and payment ([IRS: when to file](https://www.irs.gov/filing/individuals/when-to-file); [IRS: extensions](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return); [Pub. 505 (2026)](https://www.irs.gov/publications/p505))

- **Return:** Form 1040 with Schedule C, and Schedule SE where net earnings are $400 or more ([Topic 554](https://www.irs.gov/taxtopics/tc554)). Calendar-year returns are due April 15 after the year ends. If that date falls on a weekend or legal holiday, it moves to the next business day. For 2026 returns, confirm the April 2027 date in the 2026 Form 1040 instructions once they are published.
- **Extension:** it gives until October 15 to **file**. It does not extend the time to **pay**. Tax unpaid after the April date draws interest and any late-payment penalty.
- **2026 estimated tax:** due April 15, June 15 and September 15, 2026, and January 15, 2027. The January payment is not needed if the 2026 return is filed by January 31, 2027 and the balance is paid then ([Pub. 505 (2026)](https://www.irs.gov/publications/p505)).
- **Business information returns for 2026 payments:** Form 1099-NEC to the recipient and the IRS by February 1, 2027, because January 31, 2027 is a Sunday. Form 1099-MISC to the IRS by March 1, 2027 on paper (February 28, 2027 is a Sunday), or March 31, 2027 electronically. A due date on a weekend or legal holiday moves to the next business day. Check the 10-return e-file rule ([Form 1099-MISC and 1099-NEC instructions](https://www.irs.gov/instructions/i1099mec)).
- **Elections that ride on a timely filed original return:** the de minimis safe harbor election, the choice of home office method for the year, and the choice of the standard mileage rate in a car's first business year. A late or amended return can lose them.

## 2025 returns: extended deadline October 15, 2026 ([IRS: extensions](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return); [Schedule SE (2025)](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf))

- Use the 2025 forms and the 2025 column of the figures table: 70 cents a mile for the whole of 2025 ([IRS standard mileage rates](https://www.irs.gov/tax-professionals/standard-mileage-rates)), and a social security wage base of $176,100 ([Schedule SE (2025)](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf)).
- Section 179 for 2025 is $2,500,000, reduced above $4,000,000, as amended by P.L. 119-21 ([Rev. Proc. 2025-32 §3](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)). Older 2025 tables printed before the law changed are out of date.
- Forms 1099-NEC for 2025 payments used the $600 threshold and were due January 31, 2026 ([2025 instructions](https://www.irs.gov/pub/irs-prior/i1099mec--2025.pdf)). If some were missed, file them now. Penalties for late information returns are handled in `us-irs-collections-and-controversy`.
- An extension to October 15, 2026 covered filing only. Tax was due by April 15, 2026, so interest runs from that date.
- The Pub. 463 rules on meals, gifts and receipts cited here are from the 2025 edition, which applies to 2025 returns ([Pub. 463](https://www.irs.gov/publications/p463)).

## Completion checklist

- The tax year is stated, and each figure used belongs to that year. In 2026, mileage is split at July 1.
- The filing status comes from marital status on December 31 and was not assumed.
- Residence is confirmed, or the case has gone to `us-tax-residency`.
- The entity is classified: sole proprietor, disregarded single-member LLC, or qualified joint venture, with every condition met. Nothing that is a partnership or corporation is on Schedule C.
- The business-or-hobby question is answered on facts ([26 U.S.C. 183](https://www.law.cornell.edu/uscode/text/26/183)).
- Gross receipts tie to bank deposits and to every Form 1099. Transfers, loans and capital are excluded, with the reason recorded.
- Each expense is business, ordinary and necessary. The meals, gifts, vehicle, home office and capitalization limits are applied ([Pub. 463](https://www.irs.gov/publications/p463)).
- Travel, gift and car records exist, with receipts for lodging and for other items of $75 or more.
- Workers are classified. W-9s are on file. Forms 1099-NEC are issued at the right threshold for the payment year ($2,000 or more in 2026; $600 or more in 2025).
- SE tax is tested at $400 of net earnings, and the return has gone through `us-federal-return-assembly`.
- The 2026 estimated tax is set against the right safe harbor, including 110% where 2025 AGI was more than $150,000 ($75,000 MFS).
- Every provisional treatment is resolved or disclosed, and nothing is filed on a guess ([26 U.S.C. 6694](https://www.law.cornell.edu/uscode/text/26/6694)).
- Referral items are listed, and state tax is flagged as a separate check.

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
