---
name: uk-return-assembly
description: Final orchestrator skill that assembles the complete UK filing package for UK-resident sole traders. Consumes outputs from all UK content skills (uk-vat-return for VAT100, uk-self-employment-sa103 for trading income, uk-income-tax-sa100 for personal tax, uk-national-insurance for Class 2+4 NIC, uk-student-loan-repayment for student loan, uk-payments-on-account for payments on account) to produce a single unified reviewer package containing every worksheet, every form, every brief section, all cross-skill reconciliations, and the final action list with payment instructions, filing instructions, and next-year planning. This is the capstone skill that runs last and produces the final deliverable. MUST be loaded alongside all UK content skills listed above. UK full-year residents only. Sole traders only.
version: 0.1
jurisdiction: GB
tax_year: 2026
last_updated: 2026-09-27
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK Self Assessment return assembly: putting the SA100 and its pages together

This Guide is the last step for a UK individual's Self Assessment return. It picks the SA100 pages, runs the part Guides in order, builds the computation in the statutory order, reconciles the pieces, checks the result against HMRC's own calculation, and sets the filing and payment calendar. Detail stays in each part Guide.

Two tax years matter on 25 September 2026:

- **2026-27** (6 April 2026 to 5 April 2027) is the year in force. Planning, payments on account and the next return use it.
- **2025-26** (6 April 2025 to 5 April 2026) is the year whose return is being filed now. HMRC calls the form "Tax Return 2026". It is due online by 31 January 2027.

Every figure names its year. Never carry a 2026-27 figure into a 2025-26 return.

## Scope

**In scope.** An individual who is UK resident for the whole year, with a main home in England, Wales or Northern Ireland, filing an SA100 with any mix of employment (SA102), sole trade (SA103S or SA103F, with VAT if registered), UK property (SA105), capital gains (SA108), and interest, dividends, pensions, Gift Aid and pension contributions on the main return. It also covers Class 4 and voluntary Class 2, student loan repayments, the High Income Child Benefit Charge, and payments on account for the next year.

**Refer, do not assemble.** Scottish taxpayers, because their non-savings bands and rates differ ([Income Tax in Scotland](https://www.gov.uk/scottish-income-tax)). Non-residents, split years and dual residents (SA109; start with `uk-statutory-residence-test`). Foreign income and the 4-year foreign income and gains regime (SA106; see `uk-non-dom`). Partnerships (SA104), trusts and estates (SA107), and limited companies. Details are under "When to refuse or refer".

The output is a reviewer package. A qualified accountant must check it before it is filed.

## Ask the client first

Ask these before any number is worked out. Each answer changes which pages apply or which figure is used.

- **Which return?** The 2025-26 return being filed now, or planning for 2026-27?
- **Main home and residence.** Scotland, or any time living abroad, means refer.
- **Filed before?** A first-time filer for 2025-26 had to tell HMRC by 5 October 2026. Unique Taxpayer Reference?
- **Jobs.** P60, P45 and P11D for each job; tips, bonuses, termination payments.
- **Self-employment.** Turnover, accounting date, cash basis or traditional accounting, VAT registration, Construction Industry Scheme deductions.
- **Property, gains, anything abroad.** Rent, disposals of shares, property or crypto, foreign income or gains.
- **Savings.** Interest and dividends outside ISAs, by account and company.
- **Pensions and gifts.** Pension income; personal pension contributions (relief at source or not); Gift Aid.
- **Family.** Marriage Allowance? Child Benefit in the household, and each partner's adjusted net income? For 2025-26: a Winter Fuel Payment?
- **Student loan.** Plan, and the amount taken through payroll.
- **Last year.** The last SA302, payments on account made on 31 January and 31 July, and any claim to reduce them (form SA303).
- **Making Tax Digital.** Any letter from HMRC about it?

If an answer is missing, list it and ask for it. Do not guess an amount into the return.

## The method, step by step

### Stage 1: decide which pages apply

The SA100 is the main return. HMRC lists the supplementary pages that go with it ([SA100 and supplementary pages](https://www.gov.uk/government/publications/self-assessment-tax-return-sa100)). Tick each one the facts call for, and route it:

| Page | When it applies | Where the detail is |
| --- | --- | --- |
| SA100 main return | Always: interest, dividends, UK pensions and benefits, pension contributions, Gift Aid, Child Benefit charge, Marriage Allowance | `uk-income-tax-sa100` |
| SA101 Additional information | Less common income, deductions and reliefs, and the pension annual allowance charge | Refer if material |
| SA102 Employment | An employee or company director | P60, P11D; pay in box 1, UK tax taken off in box 2 |
| SA103S or SA103F Self-employment | A sole trader | This Guide, Stage 2 below, then `uk-bookkeeping` |
| SA104S or SA104F Partnership | A partner | Refer |
| SA105 UK property | Rental income | `uk-rental-sa105` |
| SA106 Foreign | Foreign income or gains | Refer; `uk-non-dom` |
| SA107 Trusts etc | Income from a trust, settlement or deceased person's estate | Refer |
| SA108 Capital Gains summary | Disposals to report | `uk-capital-gains-sa108` |
| SA109 Residence, remittance basis etc | A non-UK resident or dual resident | Refer |
| SA110 Tax calculation | A paper filer who works out their own tax | See Stage 5 |

**Short or full self-employment pages.** HMRC's notes for the 2025-26 return say to use the short pages (SA103S) if turnover "was less than £90,000 (or would have been if you had traded for a full year)" ([SA103S notes 2026](https://assets.publishing.service.gov.uk/media/69ce15395cf899414a0bc69f/SA103S_Notes_2026.pdf)). At £90,000 or more, use the full pages (SA103F). The full pages are also needed, whatever the turnover, if any of these applies ([SA103F notes 2026](https://assets.publishing.service.gov.uk/media/69c26565cfa346b9d4704b35/SA103F_Notes_2026.pdf)):

- the profits or losses of the accounting period need adjusting because it ended before 31 March 2026, was not 12 months long, or did not end in the tax year;
- there is adjustment income from a change of accounting basis;
- profits chargeable to Class 4 need adjusting;
- the client was within the Managing Serious Defaulters programme during the year.

HMRC has not yet published the notes for the 2026-27 return. Until it does, treat the 2025-26 box numbers below as provisional for 2026-27.

### Stage 2: run the part Guides in dependency order

Each step feeds the next.

1. **VAT, if registered** (`uk-vat-return`). It runs first because it decides whether SA103 figures are net or gross: for a registered trader, VAT charged is not turnover and reclaimable VAT is not an expense. For an unregistered trader, test turnover against the threshold: registration is compulsory when taxable turnover is more than £90,000 on a rolling 12 months ([VAT thresholds](https://www.gov.uk/how-vat-works/vat-thresholds)).
2. **Self-employment pages** (`uk-bookkeeping` for expenses, capital allowances and simplified expenses). Output: turnover, expenses, net profit, capital allowances, taxable profit. The box map for the 2025-26 return:

| Item | Short pages (SA103S) | Full pages (SA103F) |
| --- | --- | --- |
| Turnover, other business income, trading income allowance | 9, 10, 10.1 | 15, 16, 16.1 |
| Expenses, then the total | 11 to 19, total 20 | 17 to 30, total 31 |
| Net profit, net loss | 21, 22 | 47, 48 |
| Annual Investment Allowance | 23 | 49 |
| All capital allowances | 23 to 25.2, no total box | 49 to 56, total in 57 |
| Balancing charges, goods for own use | 26, 27 | 59, 60 |
| Net business profit or loss for tax purposes | 28, 32 | 64, 65 |
| Total taxable profits, and the loss carried into the loss boxes | 31, 32 | 76, 77 |
| Traditional accounting ticked | 8 | 10 |
| Voluntary Class 2; exempt from Class 4 | 36; 37 | 100; 101 |
| Adjustment to profits chargeable to Class 4 | none | 102 |
| Construction Industry Scheme deductions | 38 | 81 |

3. **Employment pages.** Pay from the P60 in SA102 box 1 and UK tax taken off in box 2 ([SA102 notes 2026](https://assets.publishing.service.gov.uk/media/6a9ea0015a0c25165ae469d3/SA102_-Notes_2026.pdf)). Benefits in kind and employment expenses come from the P11D: flag them for the reviewer.
4. **Property and gains.** Run `uk-rental-sa105` and `uk-capital-gains-sa108` if they apply. Take their SA105 profit or loss and their Capital Gains Tax figure as given. Route crypto disposals and crypto income to `uk-crypto-tax`.
5. **The main return and the tax computation** (`uk-income-tax-sa100`), in the statutory order in Stage 3.
6. **National Insurance** (`uk-national-insurance`): Class 4 on the taxable profit, and voluntary Class 2 only where the client chose it.
7. **Student loan and Child Benefit charge**, on the total income from step 5, using the student loan threshold for the return's year.
8. **Payments on account for the next year** (`uk-payments-on-account`), from the Self Assessment balance.

If a part Guide cannot produce its output, say which one and why in the reviewer brief. Continue with the rest, and do not file until the gap is closed.

### Stage 3: put the computation together in the statutory order

The Income Tax Act 2007, section 23, sets seven steps ([ITA 2007 s.23](https://www.legislation.gov.uk/ukpga/2007/3/section/23)). Follow them in this order:

1. **Total income.** "Identify the amounts of income on which the taxpayer is charged to income tax for the tax year." Keep three components apart: non-savings (employment, self-employment, pensions, property), savings (interest) and dividends.
2. **Reliefs.** Deduct reliefs such as trading losses set against other income and pension contributions paid gross. The result is net income.
3. **Allowances.** Deduct the Personal Allowance, after the taper (below). It is set against non-savings income first, then savings, then dividends.
4. **Tax at each rate** on what is left, in the order in section 16: non-savings first, then savings, then dividends. Where both are present, "the savings income and dividend income are together treated as the highest part of the person's total income", and dividends sit on top ([ITA 2007 s.16](https://www.legislation.gov.uk/ukpga/2007/3/section/16)).
5. **Add** the tax at each rate.
6. **Tax reductions.** Take off reducers such as the Marriage Allowance reduction for the spouse who receives it.
7. **Add charges** that sit outside the rates, such as the High Income Child Benefit Charge, and the pension annual allowance charge. The result is the Income Tax liability.

Then, outside the Income Tax steps:

8. **Add Class 4 National Insurance** on the self-employment profit, and any voluntary Class 2.
9. **Add the student loan** repayment worked out through Self Assessment, and any Capital Gains Tax from the SA108.
10. **Take off tax already paid**: PAYE from the SA102, tax taken off at source, Construction Industry Scheme deductions, and the payments on account already made for the year.
11. The result is the balancing payment, or the repayment due.

**The Personal Allowance taper.** "For an individual whose adjusted net income exceeds £100,000, the allowance ... is reduced by one-half of the excess", rounded up to a whole pound ([ITA 2007 s.35](https://www.legislation.gov.uk/ukpga/2007/3/section/35)). HMRC puts it as "£1 for every £2" above £100,000. The allowance is nil at £125,140 or more ([Income Tax rates](https://www.gov.uk/income-tax-rates)). Adjusted net income is net income less grossed-up Gift Aid and grossed-up relief-at-source pension contributions ([adjusted net income](https://www.gov.uk/guidance/adjusted-net-income)). The same grossed-up amounts extend the basic rate band.

**Savings.** Apply, in order: any unused Personal Allowance, the starting rate for savings, the Personal Savings Allowance, then the savings rates. The starting rate is available only if other taxable income "is less than £17,570". It covers "up to £5,000 of interest", reduced £1 for every £1 of other income above the Personal Allowance. The Personal Savings Allowance depends on the band: "To work out your tax band, add all the interest you've earned to your other income" ([savings allowances](https://www.gov.uk/apply-tax-free-interest-on-savings/how-much-is-tax-free)).

**Dividends.** Dividends within any unused Personal Allowance are tax-free. Then the dividend allowance applies, then the dividend rates. The allowance is a band taxed at nil, not a deduction. Dividends inside it still use up the basic and higher rate bands ([tax on dividends](https://www.gov.uk/tax-on-dividends)).

### Stage 4: reconcile the pieces

Run these six checks before the numbers go to the reviewer. Record each as pass, fail or not applicable.

| Check | Compare | Rule |
| --- | --- | --- |
| 1. Profit carried across | SA103 taxable profit (box 31 short, box 76 full) against the self-employment income in the SA100 computation | Must match exactly. Common causes of a difference: private-use adjustments, goods taken for own use, a second trade left out |
| 2. Class 4 base | Class 4 profit against the SA103 taxable profit, adjusted by box 102 on the full pages | Class 4 is on taxable profit from all trades added together. Box 37 or 101 ticked means no Class 4 |
| 3. Payments on account | Payments on account made for this year against half of last year's Self Assessment balance on the prior SA302 | A difference means a claim to reduce (SA303), a first year, or a missed payment. Find out which |
| 4. VAT turnover | Sales excluding VAT on the VAT returns against SA103 turnover (box 9 short, box 15 full) | Should broadly match. VAT periods rarely line up with 6 April to 5 April. On the Flat Rate Scheme the SA103 uses actual turnover, not the flat-rate sum |
| 5. Student loan | The repayment against total income from the computation | Plan rate on income over the threshold for that year, less what payroll took. Cannot be negative: if payroll took too much, the refund is claimed from the Student Loans Company, not through the return ([getting a refund](https://www.gov.uk/repaying-your-student-loan/getting-a-refund)) |
| 6. Accounting basis | SA103 traditional accounting box (8 short, 10 full) against the workings | Cash basis: no debtor, creditor or accrual adjustments. Traditional accounting: debtor and creditor adjustments present |

A failed check is not a reason to stop the work. It is a reason not to file. Name it, give the difference in pounds, and send it to the reviewer.

### Stage 5: check against HMRC's own calculation

HMRC works out the tax itself from the boxes. The assembled computation has to agree with it.

- **Online filers.** The online return and commercial software calculate the tax before submission. Compare that figure with the assembled computation line by line: total income, Personal Allowance, tax at each rate, Class 4, student loan, tax deducted, balancing payment and payments on account. Any difference means a box is wrong or an input is missing. Find it before submitting.
- **After filing.** The SA302 tax calculation and a tax year overview can be printed from the HMRC online account, or the software may call it a "tax computation". "You cannot print your documents until 72 hours after you sent your tax return" ([SA302 tax calculation](https://www.gov.uk/sa302-tax-calculation)). File the SA302 with the working papers.
- **Paper filers.** HMRC lists the SA110 as the page for "the results of your tax calculation". If the paper return reaches HMRC by the deadline, HMRC says "we'll work out if you have any tax to pay and tell you before 31 January 2027" for a 2025-26 return, including whether payments on account are due ([SA150 notes 2026](https://assets.publishing.service.gov.uk/media/6a9ea8a5df4246cf45e469e0/SA150_Notes_2026.pdf)).
- **Fixing a mistake.** "You can correct a tax return within 12 months of the Self Assessment deadline", online or by sending another paper return. Online, "You must wait 3 days (72 hours) after filing before updating your return". After the 12 months, write to HMRC ([changing a return](https://www.gov.uk/self-assessment-tax-returns/corrections)). For a 2025-26 return filed online, the 12 months end on 31 January 2028.

### Stage 6: payments on account and the calendar ([payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account))

Payments on account are advance payments towards the next year's bill, including Class 4 for the self-employed. "Each payment is half of the tax you owed last year", due "by midnight on 31 January and 31 July" ([payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account)). The base is last year's Self Assessment balance: Income Tax and Class 4 after tax deducted at source. Capital Gains Tax and student loan repayments are paid with the balancing payment and are not part of the instalments. Keep the detail, including a claim to reduce on form SA303, in `uk-payments-on-account`.

No payments on account are due if either:

- "the amount of tax you owed last year was less than £1,000", or
- "last year you paid more than 80% of the tax you owed outside of Self Assessment".

At exactly 80% paid outside Self Assessment, they are still due. The statute switches them off only where the Self Assessment balance is less than the prescribed share of the assessed tax ([Taxes Management Act, s.59A](https://www.legislation.gov.uk/ukpga/1970/9/section/59A)).

A reduced payment on account that turns out too low costs interest: "you'll be charged interest on the difference".

## Figures with years

These are the figures the assembly checks against. For England, Wales and Northern Ireland, with a standard Personal Allowance. The part Guides carry the detail.

### Income Tax ([Income Tax rates](https://www.gov.uk/income-tax-rates); [previous tax years](https://www.gov.uk/income-tax-rates/previous-tax-years); [Finance Act 2026 s.2](https://www.legislation.gov.uk/ukpga/2026/11/section/2); [s.10](https://www.legislation.gov.uk/ukpga/2026/11/section/10))

| Item | 2025-26 (return due 31 January 2027) | 2026-27 (year in force) |
| --- | --- | --- |
| Personal Allowance | £12,570 | £12,570 |
| Taper | £1 for every £2 of adjusted net income above £100,000 | Same |
| Allowance nil at | £125,140 or more | £125,140 or more |
| Basic rate 20% | £12,571 to £50,270 | £12,571 to £50,270 |
| Higher rate 40% | £50,271 to £125,140 | £50,271 to £125,140 |
| Additional rate 45% | Over £125,140 | Over £125,140 |
| Basic rate limit (band above the allowance) | £37,700 | £37,700 |

Finance Act 2026 section 10 keeps the basic rate limit at £37,700 up to 2030-31.

### Savings and dividends ([savings allowances](https://www.gov.uk/apply-tax-free-interest-on-savings/how-much-is-tax-free); [tax on dividends](https://www.gov.uk/tax-on-dividends); [Finance Act 2026 s.4](https://www.legislation.gov.uk/ukpga/2026/11/section/4); [s.5](https://www.legislation.gov.uk/ukpga/2026/11/section/5))

| Item | 2025-26 | 2026-27 |
| --- | --- | --- |
| Starting rate for savings band | Up to £5,000; only if other income is less than £17,570 | Same |
| Personal Savings Allowance | £1,000 basic rate, £500 higher rate, £0 additional rate | Same |
| Savings rates | 20%, 40%, 45% | 20%, 40%, 45% |
| Dividend allowance | £500 | £500 |
| Dividend ordinary rate | 8.75% | 10.75% |
| Dividend upper rate | 33.75% | 35.75% |
| Dividend additional rate | 39.35% | 39.35% |

Finance Act 2026 section 4 substitutes "10.75%" for "8.75%" and "35.75%" for "33.75%" from 2026-27. Section 5 raises the savings rates to 22%, 42% and 47% only from 2027-28. Do not apply them to either year here. `uk-income-tax-sa100` carries the detail.

### National Insurance for the self-employed ([self-employed rates](https://www.gov.uk/self-employed-national-insurance-rates); [rates by year](https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions); `uk-national-insurance`)

| Item | 2025-26 | 2026-27 |
| --- | --- | --- |
| Class 4 main rate, profits over £12,570 up to £50,270 | 6% | 6% |
| Class 4 rate on profits over £50,270 | 2% | 2% |
| Small profits threshold: at or above it, Class 2 is treated as paid | £6,845 | £7,105 |
| Voluntary Class 2, only below the threshold and only if the client chooses | £3.50 a week | £3.65 a week |

Class 2 is no longer charged. On the 2025-26 short pages, box 36 is ticked only "If your total profits for 2025 to 2026 are less than £6,845 and you choose to pay" ([SA103S notes 2026](https://assets.publishing.service.gov.uk/media/69ce15395cf899414a0bc69f/SA103S_Notes_2026.pdf)).

### Other thresholds the assembly tests

| Item | Figure | Year |
| --- | --- | --- |
| Trading allowance and property allowance ([allowances](https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income)) | Up to £1,000 each | Each year since 6 April 2017 |
| High Income Child Benefit Charge ([Child Benefit charge](https://www.gov.uk/child-benefit-tax-charge)) | Adjusted net income over £60,000; 1% of the Child Benefit for every £200 over; all of it at £80,000 or more | 2024-25 onwards |
| Student loan yearly thresholds, 2025-26 ([employer rates 2025 to 2026](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026)) | Plan 1 £26,065; Plan 2 £28,470; Plan 4 £32,745; Postgraduate Loan £21,000. The page gives no Plan 5 threshold for 2025-26, so check any Plan 5 case with HMRC | 2025-26 return |
| Student loan yearly thresholds, 2026-27 ([employer rates 2026 to 2027](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027); [what you pay](https://www.gov.uk/repaying-your-student-loan/what-you-pay)) | Plan 1 £26,900; Plan 2 £29,385; Plan 4 £33,795; Plan 5 £25,000; Postgraduate Loan £21,000 | 2026-27 |
| Student loan rate | 9% over the threshold (Plans 1, 2, 4, 5); 6% (Postgraduate Loan) | Both years |
| Child Benefit claimed by someone else ([Child Benefit charge](https://www.gov.uk/child-benefit-tax-charge)) | In HMRC's words, the charge "may also apply if someone else gets Child Benefit for a child living with you and they contribute at least an equal amount towards the child's upkeep". The child need not be the client's own | 2024-25 onwards |
| Payments on account switched off | Last year's tax owed less than £1,000, or more than 80% paid outside Self Assessment | Standing rule |
| VAT registration ([VAT thresholds](https://www.gov.uk/how-vat-works/vat-thresholds)) | Taxable turnover more than £90,000 on a rolling 12 months | In force |
| Making Tax Digital for Income Tax ([who needs it](https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax)) | Qualifying income over £50,000 in 2024-25: should have started from 6 April 2026. Over £30,000 in 2025-26: from 6 April 2027. Over £20,000 in 2026-27: from 6 April 2028 | As stated |
| Tax code collection of a 2025-26 balance ([SA150 notes 2026](https://assets.publishing.service.gov.uk/media/6a9ea8a5df4246cf45e469e0/SA150_Notes_2026.pdf)) | Owe less than £3,000, have a job or UK pension paid through PAYE (HMRC will "try to collect it through your wages or pension"), and file online by 30 December 2026 (paper by 31 October 2026). A sole trader with no PAYE income cannot use it and pays by 31 January 2027 | 2025-26 return |
| Simplified expenses: cars and goods vehicles ([vehicles](https://www.gov.uk/simpler-income-tax-simplified-expenses/vehicles)) | 55p a mile for the first 10,000 business miles and 25p after, for 2026-27; before 6 April 2026, 45p and 25p | As stated |
| Simplified expenses: working from home ([working from home](https://www.gov.uk/simpler-income-tax-simplified-expenses/working-from-home)) | £10 a month for 25 to 50 hours, £18 for 51 to 100, £26 for 101 and more | Current page |

Capital allowances, including the Annual Investment Allowance and the pool rates, are applied in `uk-bookkeeping`. Take each rate from HMRC's page for the right date, never from an older workpaper ([capital allowance rates and pools](https://www.gov.uk/work-out-capital-allowances/rates-and-pools)).

## Boundary and exception table ([Income Tax rates](https://www.gov.uk/income-tax-rates); [SA103S notes 2026](https://assets.publishing.service.gov.uk/media/69ce15395cf899414a0bc69f/SA103S_Notes_2026.pdf); [payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account))

| Situation | Rule |
| --- | --- |
| Turnover exactly £90,000 (2025-26 return) | Full pages. The short pages need turnover "less than £90,000" |
| Turnover under £90,000 but the accounting period ended before 31 March 2026 or was not 12 months long | Full pages |
| Adjusted net income exactly £100,000 | No taper. It starts only above £100,000 |
| Adjusted net income £125,140 or more | Personal Allowance nil |
| Other taxable income £17,570 or more | No starting rate for savings |
| Dividends inside the £500 allowance | Not taxed, but still reported and still use up the bands |
| Profits exactly £7,105 (2026-27) or £6,845 (2025-26) | Class 2 treated as paid. Voluntary Class 2 is only for profits below the threshold |
| Profits exactly £12,570 | No Class 4. It starts on profits over £12,570 |
| Adjusted net income exactly £60,000 | No Child Benefit charge. It applies over £60,000 |
| Both partners over £60,000 | The partner with the higher adjusted net income pays the charge |
| Last year's Self Assessment balance under £1,000 | No payments on account. At £1,000 they are due unless the 80% test is met |
| Exactly 80% of last year's tax paid outside Self Assessment | Payments on account still due. The gov.uk test is "more than 80%" |
| Capital Gains Tax or student loan in the bill | Balancing payment only; not in the payments on account |
| Registered after 5 October 2026 for 2025-26 | Return due 3 months from HMRC's letter; tax still due by 31 January 2027 |
| 2025-26 balance of £3,000 or more, or no PAYE wages or pension (for example Case D) | Not collectable through the tax code. Pay by 31 January 2027 |
| Someone else claims Child Benefit for a child living with the client | The charge may still apply to the client (see the Child Benefit row in the thresholds table). Flag it for the reviewer |

## Worked cases

All cases are for England, with a standard Personal Allowance, and use the figures in the tables above. They check the assembly; the part Guides check each input.

### Case A: employee and sole trader, 2026-27 ([Income Tax rates](https://www.gov.uk/income-tax-rates))

Salary £30,000, with PAYE of £3,486 on the P60. Sole trade taxable profit £25,000 (SA103S box 31). No other income.

- Total income £55,000. Personal Allowance £12,570.
- Basic rate: £37,700 × 20% = £7,540. Higher rate: £4,730 × 40% = £1,892. Income Tax £9,432.
- Class 4: (£25,000 − £12,570) = £12,430 × 6% = £745.80. Profits are at least £7,105, so Class 2 is treated as paid.
- Self Assessment balance: £9,432 − £3,486 + £745.80 = £6,691.80. Tax at source is about a third of the total, well under 80%, and the balance is over £1,000. So each payment on account for 2027-28 is £3,345.90.
- If the client is on student loan Plan 2: 9% × (£55,000 − £29,385) = 9% × £25,615 = £2,305.35 for the year, less what payroll took. This goes in the balancing payment only.
- Reconciliation: check 1 passes if the SA100 self-employment figure is £25,000; check 2 passes if Class 4 is on £25,000.

### Case B: the Personal Allowance taper, and a pension contribution that restores it, 2026-27 ([ITA 2007 s.35](https://www.legislation.gov.uk/ukpga/2007/3/section/35))

Self-employment profit £110,000 and nothing else.

- Adjusted net income is £10,000 over £100,000, so the allowance falls by £5,000 to £7,570.
- Taxable income £102,430. Basic rate £7,540. Higher rate £64,730 × 40% = £25,892. Income Tax £33,432.
- With a relief-at-source pension contribution of £8,000 net (£10,000 gross): adjusted net income is £100,000, so the full £12,570 comes back. The basic rate band extends to £47,700. Taxable income £97,430: £47,700 × 20% = £9,540, plus £49,730 × 40% = £19,892. Income Tax £29,432, which is £4,000 less. The pension provider's basic rate relief is on top.
- Class 4 is not affected by the pension contribution.

### Case C: savings and dividends in the right order, 2026-27 against 2025-26 ([tax on dividends](https://www.gov.uk/tax-on-dividends))

Pension income £40,000, bank interest £2,000, UK dividends £6,000. Total income £48,000, so the client is a basic rate taxpayer.

- Non-savings: £40,000 − £12,570 = £27,430 × 20% = £5,486.
- Savings: other income is over £17,570, so no starting rate. The Personal Savings Allowance is £1,000. The other £1,000 × 20% = £200.
- Dividends: £500 at nil, then £5,500 in the basic rate band (£7,770 of the band is left).
- 2026-27: £5,500 × 10.75% = £591.25. Total £6,277.25.
- 2025-26: £5,500 × 8.75% = £481.25. Total £6,167.25. The £110 difference is the dividend rate rise alone.

### Case D: first return for 2025-26, with payments on account starting ([previous tax years](https://www.gov.uk/income-tax-rates/previous-tax-years))

A new sole trader with 2025-26 taxable profit of £30,000 and no other income. Registered by 5 October 2026.

- Income Tax: (£30,000 − £12,570) × 20% = £3,486. Class 4: £17,430 × 6% = £1,045.80. Profits are at least £6,845, so Class 2 is treated as paid.
- Self Assessment balance £4,531.80. No payments on account were made for 2025-26, so all of it is due.
- The balance is over £1,000 and nothing was paid at source, so payments on account for 2026-27 start: £2,265.90 each.
- By 31 January 2027: £4,531.80 + £2,265.90 = £6,797.70. By 31 July 2027: £2,265.90.
- With no job or pension paid through PAYE, the tax-code route is not available, even for a balance under £3,000.

### Case E: the Case D return filed late ([penalties](https://www.gov.uk/self-assessment-tax-returns/penalties))

The Case D return is filed online on 15 August 2027 and the £4,531.80 is paid the same day.

- Late filing: £100, plus £10 a day for 90 days (£900, the maximum), plus the 6-month penalty, the greater of 5% × £4,531.80 = £226.59 and £300, so £300. Total £1,300.
- Late payment: 5% at 30 days and 5% at 6 months, so £453.18, plus interest on the late tax.

### Case F: High Income Child Benefit Charge, 2026-27 ([Child Benefit charge](https://www.gov.uk/child-benefit-tax-charge))

Adjusted net income £70,000; the household received £2,000 of Child Benefit; the partner earns less.

- £10,000 over £60,000 ÷ £200 = 50, so 50% of the Child Benefit: £1,000. It is added at step 7 of the computation.

## When to refuse or refer

- **Scottish taxpayers** (main home in Scotland, or unclear between homes): refer. Their non-savings bands differ; savings and dividends use UK rates ([Income Tax in Scotland](https://www.gov.uk/scottish-income-tax)). This matches `uk-income-tax-sa100`.
- **Non-residents, split years and dual residents** (SA109): refer. Read `uk-statutory-residence-test` first if residence is unclear.
- **Foreign income or gains, the 4-year foreign income and gains regime, or pre-2025 remittances**: refer; see `uk-non-dom`.
- **Partnerships (SA104), trusts and estates (SA107), and limited companies**: refer.
- **Accounting periods that do not end between 31 March and 5 April, and losses** to carry back or set against other income: the full pages carry them, but the figures need judgement. Refer.
- **Benefits in kind, employment expenses, termination payments, and pensions near the annual allowance**: refer with the documents.
- **Records that will not support a return**: send the client to `uk-bookkeeping` first. If the profit for the year cannot be known by the deadline, HMRC's rule is to include 'provisional figures' and "tell HMRC that you've used provisional figures when you submit your return", then amend within 12 months; interest runs on any extra tax from the original due date ([sending a return](https://www.gov.uk/self-assessment-tax-returns/sending-return)).
- **A request to apply 2027-28 savings or property rates to 2025-26 or 2026-27**: refuse. They are not in force until 6 April 2027.
- **Enquiries, disputes, penalty appeals and reasonable excuse**: refer.

## Filing and payment

### The 2025-26 return, being filed now ([deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines); [SA150 notes 2026](https://assets.publishing.service.gov.uk/media/6a9ea8a5df4246cf45e469e0/SA150_Notes_2026.pdf))

| Event | Deadline |
| --- | --- |
| Tell HMRC you need a return, if new to Self Assessment or no 2024-25 return was needed | 5 October 2026 |
| Paper return received by HMRC | 11:59pm on 31 October 2026 |
| Online return, if a balance under £3,000 is to be collected through the tax code (only with PAYE wages or a pension) | 11:59pm on 30 December 2026 |
| Online return | 11:59pm on 31 January 2027 |
| Balancing payment for 2025-26 and first payment on account for 2026-27 | 11:59pm on 31 January 2027 |
| Second payment on account for 2026-27 | 31 July 2027 |
| Last day to amend the 2025-26 return | 31 January 2028 |

HMRC says it "must receive your tax return and any money you owe by the deadline", and that if you do not know your profit for the whole tax year, "you still need to send a tax return". Registered after 5 October 2026? The return is due 3 months from the date on HMRC's letter, but the tax is still due by 31 January 2027.

**New on the 2025-26 return.** A Winter Fuel Payment or Pension Age Winter Heating Payment charge section: "If your total income is over £35,000, you may be liable to the WFP or PAWHP charge". Ask the client and route the entry through `uk-income-tax-sa100`.

### The 2026-27 return

Online by 31 January 2028, with the balancing payment and the first 2027-28 payment on account; the second is due by 31 July 2028. Paper by 31 October 2027. A client in Making Tax Digital for Income Tax from 6 April 2026 sends quarterly updates during 2026-27, then submits the return through the software by "31 January following the end of the relevant tax year" ([MTD: submit your tax return](https://www.gov.uk/guidance/use-making-tax-digital-for-income-tax/submit-your-tax-return)). See `uk-bookkeeping`.

### Penalties and interest ([penalties](https://www.gov.uk/self-assessment-tax-returns/penalties); [HMRC interest rates](https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates))

- **Late filing.** "an initial £100 penalty". After 3 months, "additional daily penalties of £10 per day, up to a maximum of £900". After 6 months, "a further penalty of 5% of the tax due or £300, whichever is greater". After 12 months, "another 5% or £300 charge, whichever is greater".
- **Late payment.** "penalties of 5% of the tax unpaid at: 30 days 6 months 12 months", plus interest.
- **Late registration.** A failure-to-notify penalty can apply to someone who registers after 5 October and does not pay all the tax by 31 January.
- **Interest.** Late payment interest is "set at base rate plus 4% from 6 April 2025". HMRC's page shows "late payment interest rate — 7.75% from 9 January 2026" and a repayment rate of 2.75% from the same date. The rate moves with Bank of England base rate, so read the page on the day.
- For clients using Making Tax Digital for Income Tax, points-based penalties replace these from the year they join. Details are in `uk-income-tax-sa100` and `uk-bookkeeping` ([Making Tax Digital penalties](https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax)).

### Records

The client must keep records "for at least 5 years after the 31 January submission deadline of the relevant tax year" ([how long to keep records](https://www.gov.uk/self-employed-records/how-long-to-keep-your-records)). A VAT-registered trader files each VAT return and pays "one calendar month and 7 days after the end of an accounting period" ([VAT return deadlines](https://www.gov.uk/vat-returns/deadlines)).

## The reviewer package

1. **Summary**: year, pages used, total income, each tax and charge, tax already paid, balancing payment or repayment, next year's payments on account.
2. **Worksheets** from each part Guide (VAT, SA103, SA102, SA105, SA108, SA100 entries) and the capital allowances schedule with pool balances carried forward.
3. **The computation** in the Stage 3 order, the six reconciliations, and the HMRC calculation check.
4. **Positions and flags**: each judgement (mixed-use shares, use of home, simplified expenses, accounting basis, capital allowances, Child Benefit charge, Marriage Allowance) with the law or HMRC page it rests on.
5. **Client action list**: each filing and payment with date and amount, the VAT calendar, any Making Tax Digital start date, and records to keep.

### Known gaps

- The SA103 and SA102 box numbers come from HMRC's notes for the 2025-26 return. Check them against the 2026-27 notes when HMRC publishes them.
- Benefits in kind and employment expenses on the SA102 are flagged, not computed.
- Capital allowance pools need last year's closing balances. Without them, only this year's purchases can be relieved.
- The High Income Child Benefit Charge needs both partners' adjusted net incomes. If the partner's is unknown, flag it.

## Completion checklist ([Income Tax rates](https://www.gov.uk/income-tax-rates); [payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account))

- [ ] Tax year fixed; every figure checked against that year's column (for example dividends at 8.75% and 33.75% for 2025-26, 10.75% and 35.75% for 2026-27).
- [ ] Residence and main home confirmed; referral cases referred; 5 October registration checked for a first-time filer.
- [ ] Pages chosen, including short or full self-employment pages on the £90,000 test and the full-pages triggers.
- [ ] Part Guides run in the Stage 2 order, VAT first; the computation built in the section 23 order, savings and dividends on top.
- [ ] Personal Allowance taper applied above £100,000 of adjusted net income; basic rate band extended for relief-at-source pensions and Gift Aid.
- [ ] Starting rate for savings, Personal Savings Allowance and £500 dividend allowance applied as bands.
- [ ] Class 4 at 6% and 2%; Class 2 treated as paid or voluntary.
- [ ] Student loan by plan, less payroll deductions; Child Benefit charge on the higher-income partner.
- [ ] Winter Fuel Payment charge considered on the 2025-26 return.
- [ ] Turnover and expenses net of VAT for a registered trader, gross for an unregistered one.
- [ ] Tax already paid taken off: PAYE, tax at source, Construction Industry Scheme deductions, payments on account made.
- [ ] Six reconciliations recorded; the assembled figure agrees with HMRC's or the software's calculation.
- [ ] Next year's payments on account worked out, with the £1,000 and 80% tests.
- [ ] Dates and amounts given to the client (31 October paper, 30 December tax-code route, 31 January, 31 July); Making Tax Digital start year recorded.
- [ ] Package handed to a qualified accountant for review before filing.

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
