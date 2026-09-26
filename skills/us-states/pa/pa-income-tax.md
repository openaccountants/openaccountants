---
name: pa-income-tax
description: Triggers when the taxpayer is a Pennsylvania resident sole proprietor or single-member LLC needing to file Pennsylvania Form PA-40. Covers Pennsylvania's flat 3.07% income tax on eight classes of income, the unique PA rules that disallow many federal deductions, net profits computation for self-employed, and interaction with local earned income taxes. Must be loaded alongside us-tax-workflow-base and us-federal-return-assembly.
version: "0.1"
jurisdiction: US-PA
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Pennsylvania personal income tax (Form PA-40), including sole proprietors

## Scope and who this is for ([2025 PA-40 instructions](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2025/2025_pa-40in.pdf))

This Guide covers the Pennsylvania personal income tax return for individuals, **Form PA-40**, for **tax year 2026** (returns filed in 2027), with a dated section for **2025 returns** (due 15 April 2026, or 15 October 2026 on a six-month extension). It is written for full-year Pennsylvania residents, including sole proprietors and owners of a single-member LLC that is disregarded for federal tax (they file PA Schedule C). Part-year residents and nonresidents use the same PA-40; the points where their rules differ are flagged.

The tax rate is a flat **3.07%** for both years. The 2025 instructions say "The state income tax rate for 2025 is 3.07 percent (0.0307)", and the 2026 estimated tax worksheet says "Multiply Line 1 by 3.07 percent (0.0307)" ([2026 REV-413 (I)](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2026/2026_rev-413i.pdf)). The 2026 PA-40 instructions and the 2026 Schedule SP had not been published when this Guide was written (25 September 2026). Where a 2026 point comes only from 2025 material, it is labelled 2025.

Pennsylvania does **not** start from federal adjusted gross income or federal taxable income. It taxes eight separate classes of income under its own rules. "PA law does not allow standard deductions, deductions for personal exemptions, itemized deductions, or deductions for personal expenses", and only the deductions listed for Line 10 are allowed against income. So federal deductions taken after AGI (such as the qualified business income deduction and the new federal Schedule 1-A deductions) have no Pennsylvania equivalent. Tips and overtime stay in PA compensation: "PA-taxable compensation includes, but is not limited to: salaries; wages; tips; gratuities" ([2025 PA-40 instructions, Line 1a](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2025/2025_pa-40in.pdf)).

This Guide does **not** cover local earned income tax, Philadelphia wage or net profits tax, or school district income tax. Those are separate local returns: see the **pa-local-eit** Guide. It also does not cover the PA-41 fiduciary return or the PA-20S/PA-65 entity return.

**Who must file (2025)** ([2025 PA-40 instructions, page 3](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2025/2025_pa-40in.pdf)). A resident, nonresident or part-year resident must file if they "received total PA gross taxable income in excess of $33 during 2025, even if no tax is due", or "incurred a loss from any transaction as an individual, sole proprietor, partner in a partnership or PA S corporation shareholder". The test is gross taxable income, and it applies to minors claimed as dependents. A person must file even if they qualify for tax forgiveness, because the credit is claimed on the return ([PA PIT Guide, Brief Overview](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/papersonalincometaxguide/documents/pitguide_overviewrequirements.pdf)).

**Who is a resident** ([PA PIT Guide, Brief Overview](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/papersonalincometaxguide/documents/pitguide_overviewrequirements.pdf)). A resident is domiciled in Pennsylvania, or is a **statutory resident**: domiciled elsewhere, but "Has a permanent place of abode in Pennsylvania; and ... Spends more than 183 days (midnight to midnight) of the taxable year in Pennsylvania". Both parts must be met. A Pennsylvania domiciliary is still a nonresident only if all three conditions hold: no permanent place of abode in Pennsylvania, a permanent place of abode outside Pennsylvania throughout the whole year, and not more than 30 days in Pennsylvania in the year ([Personal Income Tax Preparation Guide DFO-02](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/dfo-02.pdf)). A move changes domicile only with evidence of intent to stop using the old home as the base, intent to make the new place the base, and actual physical presence there; the change date is the first day of physical presence.

## Ask the client first

- Which tax year: 2025 (return due 15 April 2026, extended to 15 October 2026) or 2026?
- Resident all year? Domicile, any Pennsylvania home kept, days in Pennsylvania (more than 183), and any move in or out with its date. Part-year residents and nonresidents need extra work (see "When to refuse or refer").
- Married? If so, does each spouse have their own income, gains and losses? Pennsylvania computes each spouse separately even on a joint return.
- Every income item, sorted into the eight classes: W-2s (Box 16 PA wages), 1099-NEC and 1099-MISC, 1099-INT and 1099-DIV, 1099-B, K-1s (and PA Schedules RK-1 or NRK-1), rental and royalty records, W-2G, estate or trust income.
- For the business: separate books for PA purposes, and a fixed asset list showing, for each asset, the federal bonus depreciation, the federal section 179 amount, and the PA basis and depreciation. Any home office: actual costs, not the federal simplified method.
- Retirement income: plan type (employer plan eligible under PA rules, IRA, Roth IRA), Form 1099-R Box 7 code, age at distribution, whether the client had retired after meeting the plan's age or service conditions, and unrecovered contributions.
- Contributions to an HSA, Archer MSA, section 529 plan or PA ABLE account, and student loan interest paid (Schedule O).
- Income taxed by another state (with that state's return), and whether the client works in Indiana, Maryland, New Jersey, Ohio, Virginia or West Virginia.
- Household for tax forgiveness: marital status on 31 December, dependent children, and all nontaxable income (tax-exempt interest, gifts, alimony, inheritances, non-PA income).
- Did the client get the federal earned income tax credit? The amount drives the Working Pennsylvanians Tax Credit.
- PA withholding, 2025 and 2026 estimated payments with dates, any credit carried from the prior year, any extension payment.

## The method, step by step

Line numbers are from the 2025 PA-40 ([2025 PA-40 instructions](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2025/2025_pa-40in.pdf)).

1. **Classify every item into one of the eight classes.** Line 1c net compensation (Line 1a gross compensation less Line 1b allowable unreimbursed employee expenses on PA Schedule UE); Line 2 interest; Line 3 dividends and capital gain distributions; Line 4 net income or loss from a business, profession or farm; Line 5 net gain or loss from the sale, exchange or disposition of property; Line 6 net income or loss from rents, royalties, patents or copyrights; Line 7 estate or trust income; Line 8 gambling and lottery winnings. "Federal income classifications are disregarded to the extent they are inconsistent with PA classifications."
2. **Compute each class under Pennsylvania rules, per person.** Interest, dividends and gambling are gross classes: no expenses, except that gambling winnings may be reduced by the cost of the wagers themselves. Compensation allows only PA Schedule UE expenses. Losses can be reported only on Lines 4, 5 and 6. Within a class, a person may net their own income and losses, but spouses "may not use each other's expenses to reduce income or offset each other's income and losses", even on a joint return.
3. **Business income (Line 4) on PA Schedule C.** Start from separate PA books, not the federal Schedule C. Apply the Pennsylvania differences in "Business income: Pennsylvania differences" below. Short-term rentals of less than 30 days, and rentals that meet the business test, go on Line 4. Add partnership and PA S corporation business income from PA Schedules RK-1 or NRK-1.
4. **Line 9, total PA taxable income.** "Add only the positive income amounts from Lines 1c through 8. Do not add, subtract, or take losses into consideration." A loss in one class cannot reduce another class, and "You cannot carry forward or carry back gains or losses to other tax years."
5. **Line 10, other deductions (Schedule O).** Only these are allowed: Archer MSA and HSA contributions (following the federal rules and limits, and only if deductible federally), section 529 plan contributions (up to **$19,000** per beneficiary per taxpayer for 2025), PA ABLE contributions (up to the federal gift tax exclusion, **$19,000** for 2025), and student loan interest (up to **$2,500**, new for 2025). The total cannot take Line 9 below zero ([2025 PA-40 instructions, pages 20 and 21](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2025/2025_pa-40in.pdf)).
6. **Line 11 and Line 12.** Line 11 = Line 9 less Line 10. **Line 12 = Line 11 x 3.07%.**
7. **Line 21, tax forgiveness (Schedule SP).** Work out eligibility income and the forgiveness percentage (see below). The credit is the percentage times the Line 12 tax after subtracting the Line 22 resident credit.
8. **Line 22, resident credit (Schedule G-L).** For each other state, the lesser of the tax due and paid there or 3.07% of the Pennsylvania-classified income that state taxed, class by class.
9. **Line 23, other credits.** PA Schedule OC (restricted credits, which must be awarded first) and PA Schedule DC (Child and Dependent Care Enhancement credit, which needs the federal section 21 credit).
10. **Payments.** Line 13 PA withholding; Line 14 credit carried from the prior year; Line 15 estimated payments; Line 16 extension payment; Line 17 nonresident withholding from NRK-1s.
11. **Working Pennsylvanians Tax Credit (2025 returns).** Not a line on the 2025 PA-40. The department computes it from the federal earned income credit, so include a copy of federal Form 1040 (see below).
12. **Finish.** Line 25 use tax (0 if none), Line 27 penalties and interest (with Form REV-1630 for estimated underpayment), then Line 26 or Line 28 tax due, or Line 29 overpayment.

## Rates, thresholds and figures by year

### Rate and filing threshold ([2025 PA-40 instructions](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2025/2025_pa-40in.pdf))

| Item | 2025 | 2026 |
| --- | --- | --- |
| Tax rate | 3.07% flat | 3.07% flat ([2026 REV-413 (I)](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2026/2026_rev-413i.pdf)) |
| Must file if PA gross taxable income is | more than $33, or any loss from a transaction | 2026 instructions not yet published; the 2025 test is the reference |
| Estimated tax: income not subject to PA withholding | $11,000 ($338 of tax) | $14,000 ($430 of tax) |

The estimated tax income threshold is set to rise to $17,000 for 2027 and $20,000 for 2028 ([2026 REV-413 (I)](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2026/2026_rev-413i.pdf)). It is **not** a filing threshold.

### Tax forgiveness, Schedule SP (2025 tables) ([2025 PA-40 instructions, pages 36 to 39](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2025/2025_pa-40in.pdf))

Who is eligible: the person is subject to PA tax, is **not** a dependent on another person's federal return, and meets the income test. Eligibility income is PA taxable income (Line 9) **plus** nontaxable income: tax-exempt interest and gains, alimony, insurance proceeds and inheritances, gifts and prizes, non-PA income of part-year residents and nonresidents, nontaxable military pay, excluded home-sale gain, nontaxable education grants, and cash support from outside the home. It does **not** include Social Security, retirement benefits from eligible plans after retiring, child support (except in a dependent child's own claim), workers' compensation, or sick and disability pay.

Married claimants use joint eligibility income and Table 2 **even if filing separately**; a married person cannot claim forgiveness independently of their spouse. "Married" includes spouses who lived apart for less than the last six months of 2025, or apart without a written separation agreement.

| Eligibility income not more than (2025) | 100% | 90% | 50% | 10% (last step) |
| --- | --- | --- | --- | --- |
| Table 1, unmarried, no dependent children | $6,500 | $6,750 | $7,750 | $8,750 |
| Table 1, unmarried, 1 dependent child | $16,000 | $16,250 | $17,250 | $18,250 |
| Table 1, unmarried, 2 dependent children | $25,500 | $25,750 | $26,750 | $27,750 |
| Table 2, married, no dependent children | $13,000 | $13,250 | $14,250 | $15,250 |
| Table 2, married, 1 dependent child | $22,500 | $22,750 | $23,750 | $24,750 |
| Table 2, married, 2 dependent children | $32,000 | $32,250 | $33,250 | $34,250 |

Each dependent child adds **$9,500** to every column. Each **$250** step above the 100% amount cuts forgiveness by 10 points, so there are ten columns from 100% down to 10%; above the last column there is no forgiveness. A dependent child must be the claimant's child, stepchild, grandchild or foster child **and** claimable as a dependent on the claimant's federal return; no other adult can be a dependent. Credit: Schedule SP Line 16 = (Line 12 tax less Line 22 resident credit) x the percentage. The 2026 Schedule SP had not been published at writing; confirm the 2026 table before filing a 2026 return.

### Working Pennsylvanians Tax Credit ([PA Tax Update No. 240](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/news-and-statistics/taxupdate/documents/taxupdate_240.pdf); [DFO-02, What's new](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/dfo-02.pdf))

Created in the 2025-26 state budget, signed in November 2025, and first claimed on **2025** PA-40s filed in 2026. "The state credit will be equal to 10% of the federal Earned Income Tax Credit (EITC)", and "The maximum state credit is $805."

- Conditions (DFO-02): the person has earned income in Pennsylvania (wages, salary and/or self-employment income), qualifies for the federal EITC, and files **both** federal Form 1040 and a PA-40. "IMPORTANT: You must include a copy of your federal Form 1040 with you PA-40 tax return."
- The department calculates the credit and applies it "to reduce your PA taxes or increase your refund", so it can produce a refund when no PA tax is due.
- 2025 maximums by qualifying children (federal EITC maximum, then state maximum): zero, $649 and $65; one, $4,328 and $433; two, $7,152 and $715; three or more, $8,046 and $805.
- Not confirmed from a department PDF at writing: how the credit applies to part-year residents and nonresidents, and where it goes on the 2026 PA-40. Check the 2026 PA-40 instructions, or ask the department, before relying on either.

### Estimated tax (2026) ([2026 REV-413 (I)](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2026/2026_rev-413i.pdf))

Estimated payments are required if **both**: the individual "can reasonably expect to owe at least $430 ($14,000 of income not subject to employer withholding) in tax after subtracting withholding and credits"; **and** withholding and credits will be less than the smaller of 90% of the 2026 tax, or 100% of the 2025 PA-40 net taxable income (Line 11) x 3.07%. The prior-year method is available only if a full-year 2025 PA-40 was filed. For 2025 the figures were $338 and $11,000 ([2025 REV-413 (I)](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2025/2025_rev-413i.pdf)).

Due dates for 2026: 15 April 2026, 15 June 2026, 15 September 2026 and 15 January 2027, **25%** each if the requirement is first met before 1 April 2026. If first met later, there are fewer, larger installments (for example 50%, 25%, 25% if first met from 1 April to 31 May 2026). A farmer (at least two-thirds of gross income from farming) may instead pay all by 15 January 2027, or file and pay in full by 1 March 2027. A PA resident working in a reciprocal state whose employer does not withhold PA tax must count those wages as income not subject to withholding, and must make estimated payments if the $14,000 income and $430 tax tests above are met.

### Retirement income ([2025 PA-40 instructions, pages 8 and 11 to 14](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2025/2025_pa-40in.pdf))

- **Not taxable:** Social Security and Railroad Retirement; "Commonly recognized pension, old age, or retirement benefits paid after becoming eligible to retire, and retiring"; military pensions; distributions from SERS, PSERS, PMRS and the U.S. Civil Service Commission Retirement Disability Plan, whatever the Box 7 code.
- **Employer plans:** a distribution is exempt only if the plan is an **eligible employer-sponsored plan** under PA rules **and** the person retired after meeting the plan's age or years-of-service conditions. Otherwise, the excess over the person's previously taxed contributions (cost recovery) is compensation on Line 1a. Ask the plan administrator whether the plan is eligible.
- **IRAs (including Roth IRAs):** exempt if received on or after age **59½**, or paid to an estate or beneficiary on death. Before 59½, the amount over the person's contributions is taxable even if the person retired, and "PA law does not have any exceptions similar to the federal exceptions for withdrawal before age 591/2". Full rollovers within 60 days, or trustee to trustee, are not taxable.
- **Contributions are not deductible:** employee contributions to an employer plan are PA-taxable compensation even when not federally taxable, and "PA law does not allow you to deduct your contributions to any IRA". A sole proprietor may not deduct their own pension or profit-sharing participation ([PA Schedule C instructions](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/pa-40c.pdf)).

### Resident credit for tax paid to other states ([PA Schedule G-L instructions](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/pa-40_pa-41g-l.pdf))

- Available to residents, and to part-year residents for the resident part of the year only. Nonresidents cannot claim it.
- "State" means a US state, the District of Columbia, Puerto Rico, or a US territory or possession. "A resident credit may not be obtained for taxes paid to any foreign government or for any local tax subdivision within a state."
- The credit for each state is "the lesser amount of: The tax due to the other state (as may be adjusted), or ... the PA classified taxable income earned, received, or realized in the other state multiplied by the Pennsylvania tax rate of 3.07 percent". Income is compared class by class, taking the lesser of the PA amount and the other state's amount in each class, and the tax used is the lesser of the tax due and the tax paid.
- One Schedule G-L per state, and separate schedules for each spouse even on a joint return. Include the other state's return.
- **Reciprocal agreements** ([2025 PA-40 instructions, page 11](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2025/2025_pa-40in.pdf)): Indiana, Maryland, New Jersey, Ohio, Virginia and West Virginia. They cover employee compensation only, not "miscellaneous and non-employee compensation", and not compensation paid to Ohio resident shareholder-employees owning 20% or more of a PA S corporation. A PA resident working there claims a refund of that state's withholding from that state; no PA resident credit is allowed on that compensation unless the other state taxed the person as a resident ([DFO-02](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/dfo-02.pdf)).

### Business income: Pennsylvania differences ([PA Schedule C instructions](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/pa-40c.pdf))

| Item | Federal | Pennsylvania (PA Schedule C) |
| --- | --- | --- |
| Bonus depreciation, IRC 168(k) | Allowed | Not allowed: "Pennsylvania PIT law does not conform to Federal law to allow federal bonus depreciation." Where PA and federal basis differ, use straight-line for PA. |
| Section 179, property placed in service in tax years beginning on or after 1 January 2023 | Federal dollar and phase-out limits | Same dollar limit and phase-out as federal (Act 53 of 2022), but limited to PA net profits; any excess carries forward. PA may take section 179 even if not elected federally ([PIT Bulletin 2023-02](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/taxlawpoliciesbulletinsnotices/taxbulletins/pit/documents/pit_bulletin_2023-02.pdf)) |
| Section 179, property placed in service before 2023 | Federal limits | $25,000 for 2003 to 2022 (lower before 2003) |
| Half of self-employment tax | Deductible | Not deductible; do not report self-employment taxes |
| Owner's own health insurance and benefits | Deductible | Not deductible: "You may not deduct any payments you make for your own personal coverage." |
| Owner's own pension or profit-sharing | Deductible | Not deductible; plans for employees are deductible |
| Home office | Actual or simplified method | Actual costs only; no safe harbor method |
| Travel, meals and entertainment | Limited | 100% of actual travel and entertainment expense if a valid business expense |
| Taxes based on income | Varies | Not deductible (federal, other states, foreign) |
| Start-up costs | IRC 195 | Up to $5,000 expensed in the first year, the rest amortized |
| Business loss | Federal limits apply | Offsets only other Line 4 business income of the same person; no carryover |

Keep a separate PA basis and depreciation record for every asset where federal bonus depreciation or a different section 179 amount was used, and track any unused PA section 179 carryforward separately from the federal one.

### Penalties and interest ([PA PIT Guide, Brief Overview](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/papersonalincometaxguide/documents/pitguide_overviewrequirements.pdf))

| Penalty | Amount |
| --- | --- |
| Late filing | 5% of the unpaid tax for each month or fraction of a month late, maximum 25%, minimum $5, unless reasonable cause |
| Underpayment (tax not paid in full with the return or extension) | 5% |
| Unreported income more than 25% of the taxable income shown | Additional 25% of the tax due on the unreported income |
| Fraud | 50% of the underpayment |
| Frivolous return | $500 |
| Dishonoured check or EFT | 10% of the payment, not more than $100 or less than $25 ([2025 PA-40 instructions](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2025/2025_pa-40in.pdf)) |
| Estimated underpayment | Form REV-1630, per installment |
| Interest | From the due date to payment, at the federal rate set by the U.S. Secretary of the Treasury in effect on 1 January of each year |

Penalties can be abated only for reasonable cause, by a petition for reassessment to the Board of Appeals within **90 days** of the mailing date of the assessment. "Act 123 of 2024 changed the time period in which a taxpayer may file a Petition for Reassessment for any tax imposed under Article III from 60 days to 90 days" ([PA PIT Guide, Brief Overview](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/papersonalincometaxguide/documents/pitguide_overviewrequirements.pdf); [DFO-02](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/dfo-02.pdf)). The 2025 PA-40 instructions still print the old 60 days; do not treat 60 days as the limit. The other route is to pay the assessment and file a petition for refund with the Board of Appeals; check the start date of its six-month window in the PIT Guide.

## Boundary and exception table

| Situation | Rule |
| --- | --- |
| Gross taxable income exactly $33, no loss | Not required to file: the test is "in excess of $33" ([2025 PA-40 instructions](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2025/2025_pa-40in.pdf)) |
| Schedule C loss, W-2 wages | Loss stays in Line 4; Line 9 counts the wages in full. No carryback or carryforward |
| Spouse A business profit, spouse B business loss, joint return | Report only A's profit on Line 4; B's loss cannot reduce it |
| Statutory residency | Needs **both** a permanent place of abode in PA and **more than** 183 days |
| Exactly 183 days with a PA abode | The PIT Guide says "more than 183 days" (so not a statutory resident), but DFO-02 says "183 days or more". Refer, and document the day count ([PIT Guide](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/papersonalincometaxguide/documents/pitguide_overviewrequirements.pdf); [DFO-02](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/dfo-02.pdf)) |
| Domiciliary living abroad | Nonresident only if no PA abode, an abode elsewhere all year, **and** not more than 30 days in PA |
| IRA distribution at 59, retired | Taxable above contributions (cost recovery); exempt from age 59½ |
| Employer pension, retired before meeting plan conditions | Taxable above contributions |
| Tax forgiveness, unmarried, no dependents, eligibility income $6,500 | 100% (the limit is "does not exceed") |
| Same, $6,750 | 90% |
| Same, more than $8,750 | No forgiveness |
| Married, filing separately | Must use joint eligibility income and Table 2 |
| Tax paid to Canada, or a city wage tax in another state | No resident credit |
| NJ wages, NJ tax withheld, PA resident | Reciprocal: claim the NJ refund; no PA resident credit on those wages |
| Self-employment income earned in Maryland by a PA resident | Not covered by reciprocity; resident credit via Schedule G-L if Maryland taxed it |
| 2026 non-withheld income of $13,999 | Below the $14,000 income test; check the $430 tax test too |
| Federal bonus depreciation on a 2026 asset | Add back for PA; use PA section 179 or straight-line PA depreciation instead |
| Extension with 90% paid by 15 April | No underpayment penalty if the rest is paid by the extended date; interest still runs on the unpaid part |

## Worked cases ([2025 PA-40 instructions](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2025/2025_pa-40in.pdf); [2026 REV-413 (I)](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2026/2026_rev-413i.pdf))

Illustrations with assumed facts.

**Case 1: sole proprietor, 2026, with estimated tax.** Single, full-year resident. PA Schedule C net profit $60,000 (after PA adjustments); bank interest $1,000; HSA contribution $4,000, deductible federally. Line 4 $60,000 + Line 2 $1,000 = Line 9 $61,000. Line 10 is $4,000, so Line 11 is $57,000. **Line 12: $57,000 x 3.07% = $1,749.90.** No withholding, non-withheld income is over $14,000 and tax is over $430, so estimates are due. The 2025 PA-40 was a full-year return with Line 11 of $50,000, so the prior-year amount is $50,000 x 3.07% = $1,535, which is less than 90% of the 2026 tax ($1,574.91). Pay four installments of $383.75 on 15 April, 15 June, 15 September 2026 and 15 January 2027.

**Case 2: business loss does not reduce wages, 2025.** Single. W-2 PA wages $80,000; PA Schedule C loss $20,000; net rental income $5,000. Line 1c $80,000, Line 4 a loss (oval filled), Line 6 $5,000. **Line 9 = $85,000** (the loss is ignored). **Tax: $85,000 x 3.07% = $2,609.50.** The $20,000 loss is not carried to 2026.

**Case 3: tax forgiveness and the Working Pennsylvanians Tax Credit, 2025.** Married, filing jointly, two dependent children. PA taxable wages $31,000; tax-exempt interest $2,000. Eligibility income is $33,000. Table 2, two children: $33,000 is in the 60% column. Tax: $31,000 x 3.07% = $951.70. No resident credit. **Forgiveness: 60% x $951.70 = $571.02**, leaving $380.68. The family's federal EITC on Form 1040 is $5,000 (assumed), so the **WPTC is 10% = $500**, computed by the department from the attached Form 1040.

**Case 4: resident credit, 2025.** PA resident commutes to New York. New York wages $50,000, taxed by New York; New York tax due and paid $2,000 (assumed). Schedule G-L: income taxed in both states $50,000; 3.07% x $50,000 = $1,535. **Resident credit: the lesser, $1,535.**

**Case 5: early IRA distribution, 2025.** Age 55, retired. Traditional IRA distribution $20,000; unrecovered contributions $12,000 (assumed from records). Before 59½, cost recovery applies: **$8,000 is PA compensation on Line 1a.** At 59½ or later, none of it would be taxable. A pension from an eligible employer plan, received after retiring under the plan's age or service conditions, would be exempt.

**Case 6: equipment purchase, 2026.** A sole proprietor places $300,000 of equipment in service in 2026 and claims federal bonus depreciation on all of it. For PA: add back the bonus depreciation. The owner elects PA section 179 for the whole $300,000 (within the federal dollar limit). PA net profit before the deduction is $200,000, so the business income limit caps the 2026 deduction at $200,000 and **$100,000 carries forward** ([PIT Bulletin 2023-02](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/taxlawpoliciesbulletinsnotices/taxbulletins/pit/documents/pit_bulletin_2023-02.pdf)). PA net profit for 2026 is zero. Keep a separate PA basis record.

**Case 7: late filing, 2025.** Tax due $1,000, no extension, filed and paid three months late. **Late filing penalty: 5% x 3 = 15% of $1,000 = $150**, plus the 5% underpayment penalty if the department imposes it, plus interest from 15 April 2026. With a valid extension and at least 90% paid by 15 April 2026, there is no late filing penalty and no underpayment penalty, but interest still runs on the part paid late.

## When to refuse or refer

- Part-year residents and nonresidents with business or compensation from both inside and outside Pennsylvania (PA Schedule NRH apportionment or separate books), and disputed domicile or statutory residency.
- Dual residents (for example taxed as a statutory resident by another state), and resident credits for more than one state that need the cross-state class limit.
- Partnership, PA S corporation, estate or trust income where the entity issued no PA Schedule RK-1 or NRK-1, or where the corporation elected not to be a PA S corporation.
- Retirement distributions where it is unclear whether the employer plan is eligible under PA rules, nonqualified deferred compensation, or ESOP and KSOP distributions.
- Restricted credits on PA Schedule OC, and intangible drilling cost elections.
- Working Pennsylvanians Tax Credit questions for part-year residents or nonresidents, until the department publishes the rule.
- Local earned income tax, Philadelphia wage or net profits tax, and school district income tax: use the **pa-local-eit** Guide.
- Department notices, assessments, penalty abatement petitions and Board of Appeals matters.
- Any request to hide income, invent expenses or take an aggressive position.

## Filing and payment ([PA PIT Guide, Brief Overview](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/papersonalincometaxguide/documents/pitguide_overviewrequirements.pdf))

- **2025 returns:** due midnight, Wednesday, 15 April 2026. File free on myPATH, or by approved software or paper.
- **Extension:** up to six months (to 15 October 2026 for 2025 returns); longer only for people outside the US. "An extension of time for filing will not extend the time for the payment of tax." If the client has an approved federal extension and owes **no** PA tax, the department grants the same extension; no form is needed. Otherwise file Form REV-276 by the due date, with payment if tax is owed, or pay the extension payment by EFT or card on myPATH (not available to someone who never filed a PA return or made an estimated payment before). Fill in the extension oval on the PA-40, and attach federal Form 4868 if REV-276 was not filed ([2025 PA-40 instructions, page 40](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2025/2025_pa-40in.pdf)).
- **Extension payment:** "No underpayment of tax penalty will be charged if at least 90 percent of the total tax liability was paid by the original due date and all additional tax is paid with the extension on or before the extended due date." Interest runs on anything unpaid at the original due date.
- **2026 returns:** confirm the due date on the 2026 PA-40 instructions when published (the 2025 return was due 15 April).
- **Estimated payments for 2026:** 15 April, 15 June, 15 September 2026 and 15 January 2027 (see "Estimated tax (2026)").
- **Amended returns:** a PA-40 marked amended, with Schedule PA-40 X. Underreported income must be corrected within 30 days of discovery. Refund claims within three years of the original due date or payment of tax ([2025 PA-40 instructions, page 41](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2025/2025_pa-40in.pdf)).

## Completion checklist ([2025 PA-40 instructions](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2025/2025_pa-40in.pdf))

- [ ] Residency tested: domicile, or permanent place of abode **and** more than 183 days; the 30-day exception only if all three conditions are met.
- [ ] Every item in one of the eight classes, per spouse; no loss used across classes or across spouses; no carryover.
- [ ] PA Schedule C prepared from PA books: bonus depreciation added back, PA section 179 limited to PA net profits, no deduction for half of self-employment tax, the owner's own coverage or own retirement plan; home office at actual cost.
- [ ] Retirement distributions tested: eligible plan, retired after meeting plan conditions, IRA age 59½, cost recovery.
- [ ] Line 10 limited to HSA, MSA, 529, ABLE and student loan interest, with Schedule O.
- [ ] Line 12 = Line 11 x 3.07%.
- [ ] Schedule SP: joint eligibility income for married people, dependent test, right table; credit on tax net of the resident credit.
- [ ] Schedule G-L per state and per spouse; no credit for foreign or local taxes; reciprocal-state wages handled.
- [ ] Federal Form 1040 attached (needed for the Working Pennsylvanians Tax Credit).
- [ ] W-2s, 1099-Rs and other required schedules included; Line 25 use tax entered (0 if none).
- [ ] Line 27 penalties with the right code; REV-1630 if an estimated-tax exception applies.
- [ ] 2026 estimated payments set up if the $14,000 income and $430 tax tests are met.
- [ ] Local earned income tax handled separately (pa-local-eit Guide).

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
