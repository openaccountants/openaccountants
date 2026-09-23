---
name: uk-return-assembly
description: Final orchestrator skill that assembles the complete UK filing package for UK-resident sole traders. Consumes outputs from all UK content skills (uk-vat-return for VAT100, uk-self-employment-sa103 for trading income, uk-income-tax-sa100 for personal tax, uk-national-insurance for Class 2+4 NIC, uk-student-loan-repayment for student loan, uk-payments-on-account for payments on account) to produce a single unified reviewer package containing every worksheet, every form, every brief section, all cross-skill reconciliations, and the final action list with payment instructions, filing instructions, and next-year planning. This is the capstone skill that runs last and produces the final deliverable. MUST be loaded alongside all UK content skills listed above. UK full-year residents only. Sole traders only.
version: 0.1
jurisdiction: GB
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK sole trader return assembly (Self Assessment)

## UK Return Assembly Guide v0.1

This Guide assembles the Self Assessment package for a UK-resident sole trader: the main return (SA100), the self-employment pages (SA103S or SA103F), the employment pages (SA102) where the client also had a job, the tax calculation (SA302), Class 4 National Insurance, student loan and High Income Child Benefit Charge pointers, payments on account and the filing calendar. It runs last, after `uk-freelance-intake` and the content Guides. Figures are for tax year 2026, which in the UK is 6 April 2026 to 5 April 2027, written "2026 to 2027" by HMRC and 2026-27 here. Two sources are older: the SA103S, SA103F and SA102 box numbers come from the notes for the 2025 to 2026 return, the latest HMRC has published, and the Making Tax Digital table tests earlier years, each row naming its year. For a 2025-26 return the workflow is the same, but read the year beside every number on the linked page: several figures changed on 6 April 2026.

- **Year applicability.** Rates here are 2026-27; the rate-bearing Guides carry the detail. Where a 2025-26 figure is printed on the 2025-26 form itself, this Guide says so.

## CRITICAL EXECUTION DIRECTIVE: READ FIRST

This section is about how an assistant paces the work. It is not advice to the taxpayer. Intake has already run and the user has consented to the whole workflow, so work through the steps without pausing for permission.

- Do not ask how deep to go, or whether they want the full package. They asked for their tax return. Produce it.
- Do not announce how much work it will take, and do not ask which deliverable to do first. Produce everything in Section 4. If context runs short, finish the numbers, positions and flags, then say which deliverables are missing and why.
- Do not re-check scope that intake settled, and do not pause between content Guides for a status update. One status message at the end is enough.
- Self-checks are targets, not blockers. If one fails, put it in the open flags and carry on.
- Source citations belong in the reviewer brief, not in the intermediate steps.

Intake has already said the package needs chartered accountant sign-off before filing. Say it once at the end and move on. The failure mode to avoid is stopping mid-way to ask about pacing: take the most defensible path and flag the decision so the reviewer can challenge it.

## What this file is

The capstone Guide for UK sole trader returns. Every UK content Guide feeds into this one. It coordinates them, checks cross-Guide consistency and assembles the package a chartered accountant signs off. The figures below are here so the assembly can be checked; the content Guides do the detailed computation.

## Section 1: Scope

Produces the complete UK filing package for:
- Full-year UK residents who are sole traders, including those who also had a job
- Tax year 2026-27 (6 April 2026 to 5 April 2027), or 2025-26 with each figure read again on the linked page
- SA100 with SA103S or SA103F, SA102 where there was employment income, VAT returns if registered, Class 4 (and voluntary Class 2 where chosen), student loan if applicable, and payments on account for the following year

Scottish taxpayers are in scope, but Scottish rates and bands differ and are applied by `uk-income-tax-sa100`: https://www.gov.uk/scottish-income-tax. National Insurance and the Personal Allowance are UK-wide.

### Which self-employment pages

| Rule | Amount | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://assets.publishing.service.gov.uk/media/69ce15395cf899414a0bc69f/SA103S_Notes_2026.pdf |
| Short pages (SA103S) if turnover was below this, or would have been below it had the client traded for a full year, otherwise the full pages (SA103F) | GBP 90,000 | "turnover was less than £90,000 (or would have been" |
| 2025-26 only: below this, Class 2 may be paid voluntarily (box 36). The 2026-27 figure is in the National Insurance table | GBP 6,845 | "less than £6,845 and you choose to pay" |

The full pages are also needed, whatever the turnover, if the profits or losses of the accounting period need adjusting because it ended before 31 March or was not 12 months long or did not end in the tax year, if there is adjustment income from a change of accounting basis, if profits chargeable to Class 4 need adjusting, or if the client was within the Managing Serious Defaulters programme during the year: https://assets.publishing.service.gov.uk/media/69c26565cfa346b9d4704b35/SA103F_Notes_2026.pdf

## Section 2: Execution order and dependency chain

The Guide enforces this order:

0. **Step 1**: `uk-vat-return`, the VAT return (if VAT registered). Runs first because VAT decides whether SA103 figures are net or gross. Standard: prepare any outstanding return and check prior periods. Flat Rate Scheme: apply the sector rate to VAT-inclusive turnover. Unregistered: skip, but test turnover against the registration limit below. Output: box values, input VAT recovered or the Flat Rate position, turnover excluding VAT.
0. **Step 2**: `uk-self-employment-sa103`, the self-employment pages, with turnover excluding VAT for a registered trader. The boxes are:

| Item | Short pages (SA103S) | Full pages (SA103F) |
| --- | --- | --- |
| Turnover, other business income, trading income allowance | 9, 10, 10.1 | 15, 16, 16.1 |
| Expenses, then the total | 11 to 19, total 20 | 17 to 30, total 31 |
| Net profit, net loss | 21, 22 | 47, 48 |
| Annual Investment Allowance | 23 | 49 |
| All capital allowances | 23 to 25.2, no total box | 49 to 56, total in 57 |
| Balancing charges, goods for own use | 26, 27 | 59, 60 |
| Taxable profit, and the loss carried into the loss boxes | 31, 32 | 76, 77 |
| Net business profit or loss for tax purposes | 28, 32 | 64, 65 |
| Traditional accounting ticked | 8 | 10 |
| Construction Industry Scheme deductions | 38 | 81 |

   Cash basis is the default; traditional accounting is the opt-out. Output: box values, net profit, taxable profit, capital allowances schedule.
0. **Step 3**: `uk-income-tax-sa100`, the main return and tax computation. Taxable profit comes from the SA103 (box 31 short, box 76 full). Employment income and tax deducted go from the P60 onto the SA102 (boxes 1 and 2). Covers total income, the Personal Allowance and its taper, tax at the rates in the income tax table or the Scottish rates, and Marriage Allowance. Output: total income, taxable income, income tax, tax already paid, balancing payment or refund.
0. **Step 4**: `uk-national-insurance`, Class 4 and any voluntary Class 2, on the taxable profit at the rates and limits in the National Insurance table. Class 2 is no longer charged: at or above the small profits threshold it is treated as paid, and below it the client may pay voluntarily. Output: Class 4, any voluntary Class 2, total through Self Assessment.
0. **Step 5**: `uk-student-loan-repayment`, the student loan (if applicable). Repayment is a share of income over the plan threshold in the student loan table, less what the payroll already took. If that Guide is a stub, compute from the table and flag it. Output: total due, amount through the payroll, amount through Self Assessment.
0. **Step 6**: `uk-payments-on-account`, the payments on account for the following year. Each is half of the year's tax including Class 4; the two switch-off tests are in the payments on account table. Capital gains and student loan go with the balancing payment, not by instalment. If that Guide is a stub, compute and flag it. Output: two amounts and dates.

- **Upstream failure handling.** If any content Guide fails to produce validated output, note the failure in the reviewer brief and continue with the data available.

## Section 3: Cross-Guide reconciliation

### Cross-check 1: SA103 taxable profit = SA100 self-employment income

**Cross-check 1 table**  _(Must match exactly)_

| SA103 output | SA100 input | Rule |
| --- | --- | --- |
| Taxable profit: box 31 short, box 76 full | SA100 self-employment income | Must match exactly |
| Turnover: box 9 short, box 15 full | Excluding VAT if registered | VAT collected is not turnover |

- **If mismatch.** Flag it. Common causes: VAT periods that do not line up with the tax year, private use adjustments, goods taken for own use.

### Cross-check 2: SA103 taxable profit feeds the Class 4 computation

**Cross-check 2 table**  _(Taxable profit)_

| Input | Source | Rule |
| --- | --- | --- |
| Profit chargeable to Class 4 | Box 31 short, box 76 full with any box 102 adjustment | Class 4 base = taxable profit |
| Rates and limits | The National Insurance table | Main rate between the limits, lower rate above |
| Exemption | Box 37 short, box 101 full | Exempt clients pay no Class 4 |

- **If mismatch.** Check the profit. With more than one self-employment, profits are combined.

### Cross-check 3: Payments on account = half of prior year SA balance

**Cross-check 3 table**  _(Prior year SA302)_

| Input | Source | Rule |
| --- | --- | --- |
| Prior year tax, including Class 4 | Prior year SA302 | Each instalment is half of it |
| Tax paid outside Self Assessment | P60, prior year SA302 | Feeds the second switch-off test |
| Capital gains, student loan | Balancing payment only | Not part of the instalments |

- **If mismatch.** Common causes: a first year of self-employment, or a claim to reduce the instalments (online or on form SA303).

### Cross-check 4: VAT turnover consistency with SA103

**Cross-check 4 table**  _(Should broadly match, adjusted for timing)_

| VAT output | SA103 input | Rule |
| --- | --- | --- |
| Total sales excluding VAT | Box 9 short, box 15 full | Should broadly match |
| Flat Rate Scheme: sector rate on VAT-inclusive turnover | Turnover from actual takings | SA103 uses actual turnover, not the flat rate sum |

- **If mismatch.** VAT periods rarely line up with 6 April to 5 April. Small differences are expected; large ones need investigation.

### Cross-check 5: Student loan computation consistent with total income

**Cross-check 5 table**  _(SA100 total income)_

| Input | Source | Rule |
| --- | --- | --- |
| Total income | SA100 computation | Plan rate on income over the plan threshold |
| Repaid through the payroll | P60 | Deducted from the total due |
| Net through Self Assessment | Total less payroll | Cannot be negative; a refund is claimed from the Student Loans Company |

- **If no student loan.** This cross-check does not apply.

## The rates and limits the assembly checks against

| Item | Amount | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below, England, Wales and Northern Ireland only | https://www.gov.uk/income-tax-rates |
| Personal Allowance | GBP 12,570 | "Personal Allowance Up to £12,570 0%" |
| Allowance starts to fall above this adjusted net income | GBP 100,000 | "If you earn more than £100,000" |
| Rate of reduction | GBP 1 for every GBP 2 | "goes down by £1 for every £2 that your adjusted net income is above £100,000" |
| Allowance is nil at or above | GBP 125,140 | "your allowance is zero if your income is £125,140 or above" |
| Basic rate | 20% | "£50,270 20%" |
| Top of the basic rate band, with a full Personal Allowance | GBP 50,270 | "£50,270 20%" |
| Higher rate, up to the additional rate threshold | 40% | "£125,140 40%" |
| Additional rate | 45% | "Additional rate over £125,140 45%" |

The taper is on adjusted net income, and it is a taper, not a cliff. Dividends and savings have their own rates: route to `uk-dividends`. Scottish rates are in `uk-income-tax-sa100`.

Self-employed National Insurance:

| Item | Amount | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/self-employed-national-insurance-rates |
| Class 4 lower profits limit | GBP 12,570 | "6% on profits over £12,570 up to £50,270" |
| Class 4 main rate | 6% | "6% on profits over £12,570 up to £50,270" |
| Class 4 upper profits limit | GBP 50,270 | "2% on profits over £50,270" |
| Class 4 rate above the upper profits limit, with no cap | 2% | "2% on profits over £50,270" |
| Small profits threshold: at or above it, Class 2 is treated as paid | GBP 7,105 | "If your profits are £7,105 or more a year Class 2 contributions are treated as having been paid" |
| Voluntary Class 2 rate for 2026-27 | GBP 3.65 a week | "The Class 2 rate for tax year 2026 to 2027 is £3.65 a week." |

Payments on account:

| Item | Amount | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/understand-self-assessment-bill/payments-on-account |
| None due if last year's tax was below this. A cliff | GBP 1,000 | "the amount of tax you owed last year was less than £1,000" |
| None due if more than this share of last year's tax was paid outside Self Assessment | 80% | "you paid more than 80% of the tax you owed outside of Self Assessment" |
| Each instalment | half of the previous year's tax | "Each payment is half of the tax you owed last year." |

Student loan, yearly thresholds:

| Plan | Amount | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/repaying-your-student-loan/what-you-pay |
| Plan 1 | GBP 26,900 | "Plan 1 £26,900" |
| Plan 2 | GBP 29,385 | "Plan 2 £29,385" |
| Plan 4 | GBP 33,795 | "Plan 4 £33,795" |
| Plan 5 | GBP 25,000 | "Plan 5 £25,000" |
| Postgraduate Loan | GBP 21,000 | "Postgraduate Loan £21,000" |
| Rate for Plans 1, 2, 4 and 5 | 9% | "9% of your income over the threshold if you’re on Plan 1, 2, 4 or 5" |
| Rate for a Postgraduate Loan | 6% | "6% of your income over the threshold if you’re on a Postgraduate Loan plan" |

High Income Child Benefit Charge. This Guide flags it and does not compute it.

| Item | Amount | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/child-benefit-tax-charge |
| Charge starts above this income | GBP 60,000 | "If you or your partner earn more than £60,000 a year" |
| All Child Benefit repaid at or above | GBP 80,000 | "If you or your partner earn £80,000 or more" |
| Rate of clawback | 1% for every GBP 200 | "You’ll pay back 1% of your Child Benefit for every £200 you earn over the threshold." |

The charge falls on the partner with the higher adjusted net income. It can also apply where someone else receives Child Benefit for a child living with the client and the client contributes at least an equal amount towards that child's upkeep. Flag it whenever Child Benefit was received and income is above the start point.

VAT registration:

| Item | Amount | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/how-vat-works/vat-thresholds |
| Taxable turnover above this makes registration compulsory. A cliff, on a rolling 12 months | GBP 90,000 | "Total taxable turnover More than £90,000 Register for VAT" |

Making Tax Digital for Income Tax. Qualifying income is self-employment and property income worked out the way the gov.uk page sets out, tested on an earlier year:

| Qualifying income over, in the year tested | Amount | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/guidance/check-if-youre-eligible-for-making-tax-digital-for-income-tax |
| 2024 to 2025: should have started from 6 April 2026 | GBP 50,000 | "£50,000 for the 2024 to 2025 tax year, you should’ve started" |
| 2025 to 2026: start 6 April 2027 | GBP 30,000 | "£30,000 for the 2025 to 2026 tax year, you will need to use it from 6 April 2027" |
| 2026 to 2027: start 6 April 2028 | GBP 20,000 | "£20,000 for the 2026 to 2027 tax year, you will need to use it from 6 April 2028" |

Capital allowances: the Annual Investment Allowance, the writing down allowance rates and the small pools rule are applied by `uk-self-employment-sa103`. The main pool rate changed during 2026, so take every rate from the page itself and never from an older Guide: https://www.gov.uk/work-out-capital-allowances/rates-and-pools

Simplified expenses, used only where the client elected them:

| Item | Amount | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/simpler-income-tax-simplified-expenses/vehicles |
| Cars and goods vehicles, first 10,000 business miles, 2026-27 | 55p per mile | "Cars and goods vehicles first 10,000 miles 55p 45p" |
| Cars and goods vehicles, after 10,000 business miles | 25p per mile | "Cars and goods vehicles after 10,000 miles 25p 25p" |

| Item | Amount | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/simpler-income-tax-simplified-expenses/working-from-home |
| Working from home, 101 or more hours a month | GBP 26 a month | "101 and more £26" |

The first mileage rate rose on 6 April 2026; the page prints the older rate for earlier years.

## Section 4: Final reviewer package contents

1. Executive summary: filing status, income, tax, VAT, National Insurance, student loan, instalments, balancing payment or refund
2. VAT return worksheet, box by box (if registered)
3. SA103 worksheet: short pages boxes 1 to 38, or full pages boxes 1 to 103, with supporting schedules
4. SA102 worksheet from the P60, benefits and expenses flagged (if employed)
5. SA100 computation: total income, Personal Allowance, taxable income, tax, Class 4, student loan, less tax already paid, balancing payment
6. Capital allowances schedule: cost, date, allowance claimed, pool balance carried forward
7. National Insurance, and student loan where there is one
8. Payments on account: the two instalments for the following year
9. Cross-Guide reconciliation: the five cross-checks with pass or fail
10. Reviewer brief: positions, citations, flags and self-check results
11. Client action list: what the client must do, with dates and amounts

### Reviewer brief contents

~~~markdown
# Complete Return Package: [Client Name], Tax Year 2026-27

## Executive Summary
- Filing status, residence, Scottish taxpayer yes or no, sole trader
- VAT status, accounting basis, and whether the short (SA103S) or full (SA103F) pages were used
- VAT position for the latest period: GBP X due or refund
- Net profit (box 21 short, box 47 full) and taxable profit (box 31 short, box 76 full): GBP X
- Total income, Personal Allowance, income tax: GBP X
- Class 4, and voluntary Class 2 if chosen: GBP X
- Student loan through Self Assessment: GBP X. High Income Child Benefit Charge: not applicable or flagged
- Total liability, tax already paid, balancing payment or refund: GBP X
- Payments on account for the following year: GBP X each, two of them

## VAT Return
[Content from uk-vat-return output: registration type and period, output VAT by rate, input VAT reclaimable and blocked, any Flat Rate computation, box by box summary, VAT due or refund]

## Self-Employment (SA103)
[Content from uk-self-employment-sa103 output]
- Turnover by client, allowable expenses, net profit, capital allowances, taxable profit: the boxes are in the Section 2 table
- Accounting basis, simplified expenses used, Construction Industry Scheme deductions

## Employment (SA102, if applicable)
- Pay from the P60 (box 1) and UK tax taken off (box 2). Benefits and employment expenses: flagged.

## Income Tax (SA100)
[Content from uk-income-tax-sa100 output]
- Self-employment income, employment income, other income routed to its own Guide, total income
- Personal Allowance with the taper, taxable income, tax at the right rate table, Marriage Allowance, tax already deducted, net liability

## National Insurance
[Content from uk-national-insurance output]
- Class 4 between the profits limits and above the upper limit: GBP X
- Voluntary Class 2 only where profits are below the small profits threshold and the client chose to pay
- Total through Self Assessment: GBP X. Class 1 paid through the payroll, for information: GBP X

## Student Loan (if applicable)
[From uk-student-loan-repayment, or computed here: plan type, threshold, total due, less repaid through the payroll, net through Self Assessment]

## Payments on Account (2027-28)
[From uk-payments-on-account, or computed here]
- Based on this year's tax including Class 4, and excluding capital gains and student loan
- First instalment 31 January 2028, second 31 July 2028: GBP X each, half of the year's tax
- None due if either switch-off test in the payments on account table is met

## Cross-Guide Reconciliation
- Taxable profit against SA100 self-employment income, and against the Class 4 base: [pass/fail]
- Payments on account against the prior year SA302; VAT turnover against SA103 turnover: [pass/fail]
- Student loan against total income: [pass/fail, or not applicable]

## Reviewer Attention Flags
- Mixed use shares (vehicle, phone, broadband), use of home claim, simplified expenses elections
- Capital allowances: which allowance, which pool, and the 2026-27 rate. Traditional accounting opt-out, if used
- Scottish taxpayer determination, Personal Allowance taper, Marriage Allowance
- High Income Child Benefit Charge where Child Benefit was received and income is above the start point
- VAT registration limit, Making Tax Digital start year, student loan plan type, Construction Industry Scheme

## Positions Taken
Every position names the Act and the section. Examples:
- "Use of home at the simplified rate for 101 or more hours a month, Income Tax (Trading and Other Income) Act 2005, section 94H"
- "Laptop claimed under the Annual Investment Allowance, Capital Allowances Act 2001, section 51A"
- "Class 4 at the main and upper rates, Social Security Contributions and Benefits Act 1992, section 15"
- "Student loan Plan 2 repayment above the plan threshold, Education (Student Loans) (Repayment) Regulations 2009"

## Planning Notes for 2027-28
- The two instalments with amounts and dates; VAT registration limit; capital allowance pool balances carried forward
- Making Tax Digital for Income Tax: the year this client must start
- Announced changes: read the gov.uk page, because an announcement is not a rate
- Voluntary Class 2, where profits are below the small profits threshold

## Client Action List

### Immediate (before 31 January 2028, the online filing deadline and the payment deadline; a paper return must reach HMRC by the 31 October before it):
1. Review this package with your chartered accountant
2. File the SA100 with the SA103, and the SA102 if you were employed
3. Pay the balancing payment of GBP X
4. Pay the first payment on account of GBP X, same deadline
5. File any outstanding VAT return, if applicable
6. If you want any balancing payment collected through your tax code instead, the return must be filed by the 30 December before the January deadline

### Before 31 July 2028:
1. Pay the second payment on account of GBP X

### VAT filing calendar (if VAT registered, quarterly):
- Each return and payment is due 1 calendar month and 7 days after the end of the period: [dates]

### If claim to reduce payments on account (SA303):
- You can ask HMRC to reduce your payments on account, online or on form SA303. If the bill turns out higher, interest is charged on the difference.

### Ongoing:
1. Issue VAT invoices for all sales, if VAT registered, and file VAT returns through Making Tax Digital software
2. Keep all records for at least 5 years after the 31 January submission deadline of the tax year
3. Keep a mileage log if claiming simplified vehicle expenses, and track capital assets for the allowance pools
4. Watch turnover against the VAT registration limit, on a rolling 12 months
5. Prepare for Making Tax Digital for Income Tax from the start date that applies to you
~~~

## Section 5: Refusals

- **R-UK-1.** An upstream Guide did not run. Name it. A warning, not a hard stop: continue and flag the gap.  _(R-UK-1)_
- **R-UK-2.** An upstream self-check failed. Name it in the reviewer brief and continue.  _(R-UK-2)_
- **R-UK-3.** A reconciliation failed. Name it, describe the difference, flag it and continue.  _(R-UK-3)_
- **R-UK-4.** Intake is incomplete. List what is missing and ask for that data point.  _(R-UK-4)_
- **R-UK-5.** An out-of-scope item appears: rental income (route to `uk-rental-sa105`), capital gains (`uk-capital-gains-sa108`), foreign income (SA106, refer). Flag it and leave it out of the computation.  _(R-UK-5)_

## Section 6: Self-checks

- **Check UK1: all upstream Guides ran.** Each content Guide produced output, was computed here, or was not applicable.
- **Check UK2: taxable profit matches the SA100 self-employment income.** Exact match.
- **Check UK3: Class 4 is on the right profit.** Box 31 on the short pages. On the full pages box 76, adjusted by box 102 if there is an entry there. The short pages have no Class 4 adjustment box.
- **Check UK4: payments on account are right.** Each is half of the year's tax including Class 4, capital gains and student loan excluded, both switch-off tests applied.
- **Check UK5: VAT treatment right for a registered trader.** Output VAT out of turnover, reclaimable input VAT out of expenses.
- **Check UK6: VAT treatment right for an unregistered trader.** Gross amounts throughout.
- **Check UK7: capital allowances right.** Annual Investment Allowance within its limit, writing down allowances at the 2026-27 rates and not an older rate, small pools claimed in full where the balance is within the limit. Figures from `uk-self-employment-sa103`.
- **Check UK8: Personal Allowance right.** Full allowance, tapered above the limit, nil at the level in the income tax table.
- **Check UK9: the right rate table.** Scottish rates for a Scottish taxpayer, otherwise England, Wales and Northern Ireland.
- **Check UK10: the calendar is complete.** Every VAT, Self Assessment and instalment deadline has a date and an amount.
- **Check UK11: Class 2 treated correctly.** Treated as paid at or above the small profits threshold; voluntary below it, and only where the client chose to pay (box 36 short, box 100 full).
- **Check UK12: the reviewer brief cites legislation.** Every position names the Act and section.
- **Check UK13: student loan plan confirmed.** Each plan has its own threshold.
- **Check UK14: the accounting basis is consistent.** Cash basis: no accruals adjustments. Traditional accounting: debtor and creditor adjustments present.

## Section 7: Output files

The final output is three files:

1. [client_slug]_2026-27_uk_master.xlsx: one workbook with every worksheet. Sheets: Cover, VAT, SA103, SA102 if employed, SA100 computation, Capital Allowances, Expense Detail, National Insurance, Student Loan, Payments on Account, Cross-Check Summary. Use live formulas where possible: the SA100 self-employment income points at the SA103 taxable profit cell, Class 4 at the SA103 sheet, the instalments at the liability. Check there are no #REF! errors and that values match the computation to the nearest pound.
2. reviewer_brief.md: every section listed in Section 4.
3. client_action_list.md: filings and payments, the instalments, the quarterly VAT calendar, ongoing reminders.

If execution runs out of context mid-build, produce whatever is complete, then say which of the three files are missing or partial. All files go to /mnt/user-data/outputs/ and are presented with the present_files tool.

## Section 8: Cross-Guide references

Inputs: `uk-freelance-intake` (the intake package), `uk-vat-return` (if registered), `uk-self-employment-sa103`, `uk-income-tax-sa100`, `uk-national-insurance`, `uk-student-loan-repayment` and `uk-payments-on-account`, the last two with a fallback computed here.

Outputs: the final reviewer package. No downstream Guide.

## Section 9: Known gaps

1. Filling the PDF forms is not automated. The reviewer uses the worksheets to file online.
2. Filing is the reviewer's job, paying is the client's. This Guide gives the instructions and the amounts.
3. Nothing here is filed or paid automatically.
4. The SA102 is only partly supported: pay (box 1) and tax taken off (box 2) come from the P60, but benefits in kind and employment expenses do not. Flag them.
5. Capital allowance tracking assumes the prior year pool balance is given. Without it, only this year's purchases are relieved.
6. If `uk-student-loan-repayment` is a stub, the loan is computed from the student loan table. Education (Student Loans) (Repayment) Regulations 2009.
7. If `uk-payments-on-account` is a stub, each instalment is half of the year's tax including Class 4. Taxes Management Act 1970, section 59A.
8. Out of scope: foreign income (no SA106, no double tax relief), rental income (`uk-rental-sa105`) and capital gains (`uk-capital-gains-sa108`).
9. The High Income Child Benefit Charge is flagged, not computed.
10. Marriage Allowance, dividends and savings income are handled by `uk-income-tax-sa100` and `uk-dividends`.
11. Benefits in kind on the SA102 are not computed here.
12. The SA103 and SA102 box numbers come from the 2025 to 2026 notes. Check them against the 2026 to 2027 notes once HMRC publishes them.
13. Making Tax Digital for Income Tax changes in-year record keeping. Settle the start year with the table above and put it in the planning notes.

### Change log

- **v0.1 (April 2026):** Initial draft, modelled on `mt-return-assembly` v0.1.
- **Refresh (September 2026):** Figures read again on gov.uk for tax year 2026 and moved into sourced tables. SA103 box numbers corrected against the SA103S and SA103F notes. Class 2 shown as treated as paid or voluntary, not charged. Student loan thresholds, small profits threshold and mileage rate updated, the cash basis turnover limit removed, Making Tax Digital added, and the SA102 and the High Income Child Benefit Charge added as pointers.

## The method, step by step

1. Fix the tax year and pick the short or full self-employment pages on the turnover test: https://assets.publishing.service.gov.uk/media/69ce15395cf899414a0bc69f/SA103S_Notes_2026.pdf and https://assets.publishing.service.gov.uk/media/69c26565cfa346b9d4704b35/SA103F_Notes_2026.pdf
2. If VAT registered, run `uk-vat-return` first and take VAT out of turnover. Otherwise test turnover against the registration limit: https://www.gov.uk/how-vat-works/vat-thresholds
3. Run `uk-self-employment-sa103` for net profit, capital allowances (https://www.gov.uk/work-out-capital-allowances/rates-and-pools) and the taxable profit in box 31 short or box 76 full.
4. If the client also had a job, carry pay and tax from the P60 onto the SA102, boxes 1 and 2: https://assets.publishing.service.gov.uk/media/6a9ea0015a0c25165ae469d3/SA102_-Notes_2026.pdf
5. Run `uk-income-tax-sa100` for total income, the Personal Allowance and its taper, and the tax: https://www.gov.uk/income-tax-rates
6. Run `uk-national-insurance` for Class 4, and voluntary Class 2 only where the client chose it: https://www.gov.uk/self-employed-national-insurance-rates
7. Add the student loan (https://www.gov.uk/repaying-your-student-loan/what-you-pay) and flag the High Income Child Benefit Charge where it may apply: https://www.gov.uk/child-benefit-tax-charge
8. Work out the payments on account and test both switch-off tests: https://www.gov.uk/understand-self-assessment-bill/payments-on-account
9. Run the cross-checks and self-checks, build the calendar from https://www.gov.uk/self-assessment-tax-returns/deadlines, and hand the package to the reviewer.

## Ask the client first

- Was your turnover below the short pages limit, and do your accounts end between 31 March and 5 April?
- Did you have a job as well, with a P60 or P45? Did you or your partner receive Child Benefit?
- Do you have a student loan, and which plan? How much was taken through your pay?
- What tax did you owe last year, and how much of it was collected through your tax code? Did you ask HMRC to reduce your payments on account?
- Do you live in Scotland?
- Has HMRC written to you about Making Tax Digital for Income Tax?

## When to refuse or refer

- Part-year residents, non-residents and split-year treatment: refer, reading `uk-statutory-residence-test` first if unclear.
- Limited companies, LLPs and partnerships as the business: refer to a chartered accountant.
- Rental income, capital gains and crypto: route to `uk-rental-sa105`, `uk-capital-gains-sa108` and `uk-crypto-tax`. Foreign income: refer.
- Domicile, remittances, or the foreign income and gains regime: route to `uk-non-dom`.
- An accounting period that does not end between 31 March and 5 April: the full pages carry it, but the apportionment is a judgement, so refer. Losses to carry back or set against other income: refer.
- Benefits in kind or employment expenses on the SA102: refer.
- Records that will not support a return: route to `uk-bookkeeping` first.

## Sources

- https://assets.publishing.service.gov.uk/media/69ce15395cf899414a0bc69f/SA103S_Notes_2026.pdf
- https://assets.publishing.service.gov.uk/media/69c26565cfa346b9d4704b35/SA103F_Notes_2026.pdf
- https://assets.publishing.service.gov.uk/media/6a9ea0015a0c25165ae469d3/SA102_-Notes_2026.pdf
- https://www.gov.uk/income-tax-rates
- https://www.gov.uk/scottish-income-tax
- https://www.gov.uk/self-employed-national-insurance-rates
- https://www.gov.uk/understand-self-assessment-bill/payments-on-account
- https://www.gov.uk/repaying-your-student-loan/what-you-pay
- https://www.gov.uk/child-benefit-tax-charge
- https://www.gov.uk/how-vat-works/vat-thresholds
- https://www.gov.uk/guidance/check-if-youre-eligible-for-making-tax-digital-for-income-tax
- https://www.gov.uk/work-out-capital-allowances/rates-and-pools
- https://www.gov.uk/simpler-income-tax-simplified-expenses/vehicles
- https://www.gov.uk/simpler-income-tax-simplified-expenses/working-from-home
- https://www.gov.uk/self-assessment-tax-returns/deadlines
- https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012
- https://www.gov.uk/self-employed-records/how-long-to-keep-your-records

## End of Guide

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a chartered accountant, ACCA member, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this Guide is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

> Contributed by OpenAccountants.

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
