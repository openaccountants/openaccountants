---
name: india-corporate-income-tax
description: "Corporate income tax in India for tax year 2026-27 (1 April 2026 to 31 March 2027) under the Income-tax Act, 2025 and the Finance Act, 2026: domestic company rates (25%, 30%), the 22% and 15% optional regimes, foreign company rate, surcharge, cess, minimum alternate tax, depreciation, common disallowances, losses, dividends, advance tax, ITR-6 due dates, tax audit, interest and late fee. Use for questions like 'how is my Indian company's profit taxed', 'Pvt Ltd tax rate India', 'section 115BAA or section 200 22% regime', 'MAT India', 'company advance tax India', 'ITR-6 due date'. Out of scope: individuals and sole proprietors (india-income-tax), GST (india-gst), payroll (india-payroll), company formation (india-formation), transfer pricing detail (india-transfer-pricing), withholding detail (in-tds-freelance), LLP and firm computations."
jurisdiction: IN
tax_year: 2026
last_updated: 2026-11-20
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
category: international
type: computation
version: 1.0
---

# India Corporate Income Tax v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Prepare a corporate income tax working paper for a company for tax year 2026-27, the twelve months from 1 April 2026 to 31 March 2027. It covers a domestic company and, in outline, a foreign company with Indian income: which Act applies, the rate, surcharge and cess, minimum alternate tax, the main steps from book profit to total income, losses, dividends, advance tax, the return and its due dates, interest and the late fee.

Which Act applies. The Income-tax Act, 2025 (30 of 2025) came into force on 1 April 2026 and repealed the Income-tax Act, 1961. It taxes a "tax year", the twelve months of the financial year starting 1 April. The words "previous year" and "assessment year" belong to the 1961 Act. All section numbers in this skill are those of the 2025 Act, as amended by the Finance Act, 2026 (4 of 2026). The Finance Act, 2026 sets the rates for tax year 2026-27 in section 3 and Part I-B of its First Schedule. Source: [2025 Act sections 1, 3, 536](https://egazette.gov.in/WriteReadData/2025/265620.pdf); [Finance Act, 2026 section 3](https://egazette.gov.in/WriteReadData/2026/271439.pdf).

What the 1961 Act still governs. Any year that began before 1 April 2026 (including financial year 2025-26, the old assessment year 2026-27) stays under the 1961 Act: its return, assessment, penalties and appeals. Losses, unabsorbed depreciation and minimum alternate tax credit brought forward from those years are carried into the 2025 Act by section 536(2); see the losses and minimum alternate tax steps below.

Out of scope. Individuals and sole proprietors: [india-income-tax](india-income-tax.md). GST: [india-gst](india-gst.md). Payroll: [india-payroll](india-payroll.md). Forming the company: [india-formation](india-formation.md). Transfer pricing method and documentation: [india-transfer-pricing](india-transfer-pricing.md). Tax deducted at source on payments the company makes: [in-tds-freelance](in-tds-freelance.md). Partnership firms and LLPs are taxed as a "firm", not as a company; only their headline rate is given in the boundary table and their computation is not covered. Capital gains computations, banks, insurers, shipping, co-operative societies, non-profit companies and units in an International Financial Services Centre are not covered.

## Ask the client first

1. Is it an Indian company (formed and registered in India) or a foreign company? If foreign, does it have a place of effective management, a branch or other presence in India, and which treaty country is it resident in?
2. Which year? This skill is only for 1 April 2026 to 31 March 2027. Is this the company's first year?
3. Total turnover or gross receipts in tax year 2024-25, the twelve months from 1 April 2024 (this decides the 25% or 30% base rate), and turnover and the share of cash receipts and payments in 2026-27 (this decides the tax audit).
4. Has the company already opted for the 22% regime or the 15% regime in an earlier year? Before 1 April 2026 that option was made under section 115BAA (22%) or section 115BAB (15%) of the 1961 Act. An option in force on 31 March 2026 is deemed to be an option under the corresponding provision of the 2025 Act (section 536(2)(f)), which this skill reads as section 200 and section 201 (see step 2). The option cannot be withdrawn.
5. Profit before tax per the audited statement of profit and loss, book depreciation, the fixed asset register by block, and any incentive deductions claimed (additional depreciation, scientific research, Chapter VIII deductions).
6. Brought-forward losses, unabsorbed depreciation and minimum alternate tax credit, by year, and any change of more than 49% in shareholding.
7. Payments made without deducting tax at source, cash payments, statutory dues and amounts owed to micro and small enterprises unpaid at year end.
8. Dividends received and dividends paid, with dates. Any international or specified domestic transaction with a related party.
9. Tax deducted at source on the company's income and advance tax already paid, with dates.

## The method, step by step

### 1. Fix residence and the charge [2025 Act sections 2(42), 2(46), 5, 6(10)](https://egazette.gov.in/WriteReadData/2025/265620.pdf)

A company is resident in India in a tax year if it is an Indian company, or if its place of effective management is in India in that year. Place of effective management means the place where key management and commercial decisions necessary for the conduct of the business as a whole are, in substance, made. A resident is taxed on income from whatever source; a non-resident on income received, accruing or arising (or deemed to) in India.

"Domestic company" means an Indian company, or any other company that has made the prescribed arrangements in India for declaring and paying dividends out of income liable to tax. "Foreign company" means a company that is not a domestic company. The rate follows this label, not residence.

### 2. Pick the rate [Finance Act, 2026, First Schedule Part I-B Paragraph E](https://egazette.gov.in/WriteReadData/2026/271439.pdf) and [2025 Act sections 199 to 201](https://egazette.gov.in/WriteReadData/2025/265620.pdf)

| Company | Rate on total income | Conditions | Official source |
|---|---|---|---|
| Domestic company, total turnover or gross receipts in tax year 2024-25 not over INR 400 crore | 25% | Standard regime. Minimum alternate tax applies. | [Finance Act, 2026, Part I-B Paragraph E](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |
| Any other domestic company | 30% | Standard regime. Minimum alternate tax applies. | [Finance Act, 2026, Part I-B Paragraph E](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |
| Domestic company opting under section 200 | 22% | Total income computed without the deductions listed below. Outside minimum alternate tax. Option cannot be withdrawn. | [2025 Act section 200](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| New manufacturing domestic company opting under section 201 | 15% | Set up and registered on or after 1 October 2019 and manufacturing commenced on or before 31 March 2024, plus the section 205(2) conditions. Non-manufacturing income and short-term gains on non-depreciable assets 22%; income deemed under section 205(4) 30%. Outside minimum alternate tax. | [2025 Act section 201](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Manufacturing domestic company opting under section 199 | 25% | Set up and registered on or after 1 March 2016, engaged only in manufacture or production and related research or distribution, without the listed deductions. | [2025 Act section 199](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Company other than a domestic company (foreign company) | 35% | On total income other than the old pre-1976 approved royalties and technical fees, which the Paragraph taxes at 50%. Special rates in section 207 apply to dividends, interest, royalties and fees for technical services. | [Finance Act, 2026, Part I-B Paragraph E](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |

Income with its own rate (capital gains under sections 196 to 198 and the other special-rate sections of Chapter XIII) is taxed at that rate, not at the rate above. Capital gains are not computed in this skill.

What the section 200 option costs. Total income is computed without: additional depreciation under section 33(8); the deductions in sections 45(2), 45(3)(a) to (c), 46, 47(1)(a), 47(1)(b), 48, 49 and 144; and any Chapter VIII deduction other than section 146 and section 148. Brought-forward loss or unabsorbed depreciation attributable to those deductions cannot be set off and is treated as fully given effect to, so it is lost. If the company fails the conditions in any year the option becomes invalid for that year and later years. The option is exercised in the return of income, on or before the section 263(1) due date, and applies to later years; once exercised it cannot be withdrawn. Depreciation on any block is capped at 40% for a company that has opted under section 199, 200 or 201. Sources: [2025 Act sections 200, 205](https://egazette.gov.in/WriteReadData/2025/265620.pdf); [Income-tax Rules, 2026, rules 25(2) and 136](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf).

Section 201 is closed to a company that had not commenced manufacturing by 31 March 2024. Do not offer the 15% rate to a company starting now.

Old and new section numbers. Tax year 2026-27 is the first year of the 2025 Act, so a company that opted earlier did so under the 1961 Act. Section 536(2)(f) of the 2025 Act deems an option exercised under the 1961 Act and in force immediately before 1 April 2026 to be an option under "the corresponding provision" of the 2025 Act. The Act prints no table of corresponding sections. This skill reads section 200 as the successor of section 115BAA and section 201 as the successor of section 115BAB on three grounds: section 115BAA and section 200 carry the same heading ("Tax on income of certain domestic companies") and the same 22% rate; section 115BAB and section 201 carry the same heading ("Tax on income of new manufacturing domestic companies"); and the Finance Act, 2026 gives the flat 10% surcharge to "section 115BAA or section 115BAB" for the 1961 Act year (section 2) and to "section 200 or 201" for the 2025 Act year (section 3). Sources: [2025 Act sections 200, 201, 536(2)(f)](https://egazette.gov.in/WriteReadData/2025/265620.pdf); [Finance Act, 2026 sections 2 and 3](https://egazette.gov.in/WriteReadData/2026/271439.pdf); [Income Tax Department, section 115BAA of the 1961 Act](https://wm.incometaxindia.gov.in/w/section-115baa-8); [Income Tax Department, section 115BAB of the 1961 Act](https://wm.incometaxindia.gov.in/w/section-115bab-7).

### 3. Add surcharge and cess [Finance Act, 2026 section 3(4), 3(15) and Part I-B Paragraph F](https://egazette.gov.in/WriteReadData/2026/271439.pdf)

Surcharge is a percentage of the income tax. The test is total income, not turnover.

| Company | Total income | Surcharge on income tax | Official source |
|---|---|---|---|
| Domestic company, standard regime or section 199 | Not over INR 10000000 (1 crore) | None | [Finance Act, 2026, Paragraph F Table 1 Sl. No. 5](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |
| Domestic company, standard regime or section 199 | Over INR 10000000 (1 crore) up to INR 100000000 (10 crore) | 7% | [Finance Act, 2026, Paragraph F Table 1 Sl. No. 5](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |
| Domestic company, standard regime or section 199 | Over INR 100000000 (10 crore) | 12% | [Finance Act, 2026, Paragraph F Table 1 Sl. No. 5](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |
| Domestic company taxed under section 200 or 201 | Any amount | 10% | [Finance Act, 2026, section 3(4)(b) Table Sl. No. 9](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |
| Foreign company | Not over INR 10000000 (1 crore) | None | [Finance Act, 2026, Paragraph F Table 1 Sl. No. 6](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |
| Foreign company | Over INR 10000000 (1 crore) up to INR 100000000 (10 crore) | 2% | [Finance Act, 2026, Paragraph F Table 1 Sl. No. 6](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |
| Foreign company | Over INR 100000000 (10 crore) | 5% | [Finance Act, 2026, Paragraph F Table 1 Sl. No. 6](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |

Health and Education Cess is 4% of the income tax plus surcharge, for every company (Finance Act, 2026 section 3(15)).

Marginal relief. For the 7%/12% and 2%/5% tiers, tax plus surcharge on income just over INR 1 crore or INR 10 crore cannot exceed the tax plus surcharge on the threshold amount plus the income over the threshold (Paragraph F, formula Wn = Un + Vn and Table 2). Apply it before cess whenever total income is slightly above a threshold. The flat 10% surcharge under sections 200 and 201 has no threshold and no marginal relief. Where the company pays minimum alternate tax (step 6), the same relief at the same two thresholds is given by section 3(5) of the Finance Act, 2026 (formula Tn = Rn + Sn).

Effective rates. Each figure is computed: rate x (1 + surcharge) x 1.04. The Finance Act does not print them.

| Company | No surcharge | Middle tier | Top tier | Official source |
|---|---|---|---|---|
| Domestic, 25% | 26.00% (computed: 25 x 1.04) | 27.82% (computed: 25 x 1.07 x 1.04) | 29.12% (computed: 25 x 1.12 x 1.04) | [Finance Act, 2026](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |
| Domestic, 30% | 31.20% (computed: 30 x 1.04) | 33.384% (computed: 30 x 1.07 x 1.04) | 34.944% (computed: 30 x 1.12 x 1.04) | [Finance Act, 2026](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |
| Domestic, section 200, 22% | not applicable | 25.168% at every income level (computed: 22 x 1.10 x 1.04) | same | [Finance Act, 2026](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |
| Domestic, section 201, 15% | not applicable | 17.16% at every income level (computed: 15 x 1.10 x 1.04) | same | [Finance Act, 2026](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |
| Foreign, 35% | 36.40% (computed: 35 x 1.04) | 37.128% (computed: 35 x 1.02 x 1.04) | 38.22% (computed: 35 x 1.05 x 1.04) | [Finance Act, 2026](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |
| Minimum alternate tax, domestic, 14% of book profit | 14.56% (computed: 14 x 1.04) | 15.5792% (computed: 14 x 1.07 x 1.04) | 16.3072% (computed: 14 x 1.12 x 1.04) | [Finance Act, 2026](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |

### 4. Compute total income [2025 Act sections 13, 26 to 37, 516](https://egazette.gov.in/WriteReadData/2025/265620.pdf)

Income is classified under five heads: Salaries; Income from house property; Profits and gains of business or profession; Capital gains; Income from other sources. A company has no salary income. Most of a trading company's income is business profit; interest on deposits and dividends usually fall under other sources.

Start from profit before tax in the statement of profit and loss and adjust:

1. Add back the income tax charge and any surcharge or cess on it. Tax on income is not deductible (section 35(a)).
2. Add back book depreciation and deduct tax depreciation (below).
3. Add back expenses that are capital, personal, or not wholly and exclusively for the business; expenditure on corporate social responsibility under section 135 of the Companies Act, 2013; and expenditure for a purpose that is an offence or prohibited by law (section 34).
4. Apply the disallowances in the table below.
5. Move income that belongs to another head (rent, capital gains, dividends, interest) to that head.
6. Set off losses and unabsorbed depreciation (step 5), then deduct any Chapter VIII deduction the regime allows.
7. Round total income, and the tax payable, to the nearest multiple of INR 10 (section 516).

Depreciation. It is allowed on blocks of assets, as a percentage of the written down value of the block, at the rates in Appendix I to the Income-tax Rules, 2026. It applies whether or not the company claims it. An asset acquired in the year and put to use for less than 180 days gets 50% of the rate. A manufacturer can also claim additional depreciation of 20% of the actual cost of new plant or machinery (10% if used for less than 180 days, with the other 10% in the next year); this is given up under sections 199, 200 and 201.

| Block (Appendix I) | Rate on written down value | Official source |
|---|---|---|
| Buildings mainly for residential use (not hotels or boarding houses) | 5% | [Income-tax Rules, 2026, Appendix I](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf) |
| Other buildings (offices, factories) | 10% | same |
| Furniture and fittings, including electrical fittings | 10% | same |
| Machinery and plant, general rate | 15% | same |
| Motor cars not used in a business of running them on hire | 15% | same |
| Computers including computer software | 40% | same |
| Intangible assets: know-how, patents, copyrights, trademarks, licences, franchises and similar rights (goodwill is excluded by section 33) | 25% | same |

Disallowances most small companies meet:

| Item | Rule | Official source |
|---|---|---|
| Payment to a resident with no tax deducted at source, or tax deducted but not paid by the section 263(1) due date | 30% of the sum is disallowed. It is allowed in the year the tax is paid. | [2025 Act section 35(b)(i)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Interest, royalty, fees for technical services or other chargeable sum paid outside India or to a non-resident, same failure | The whole sum is disallowed until the tax is paid. | [2025 Act section 35(b)(ii)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Payments to one person in one day over INR 10,000 not made through specified banking or online mode | The expenditure is disallowed. The limit is INR 35,000 for plying, hiring or leasing goods carriages. Prescribed exceptions exist. | [2025 Act section 36(4) to (7)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Excessive or unreasonable payment to a director, a director's relative or a person with a substantial interest (20% of voting power) | The excess part is disallowed. | [2025 Act section 36(2), (3)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Taxes, duties and fees; employer contributions to provident, superannuation, gratuity or welfare funds; leave encashment; bonus or commission to employees; interest to specified financial entities | Deductible only in the year actually paid. If paid after year end but on or before the section 263(1) due date, deductible in the year the liability arose. | [2025 Act section 37(1) to (3)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Amount owed to a micro or small enterprise and paid beyond the time limit in section 15 of the Micro, Small and Medium Enterprises Development Act, 2006 | Deductible only in the year actually paid. The return due date grace does not apply to this item. | [2025 Act section 37(2)(g), (3)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |

For which payments need tax deducted at source and at what rate, use [in-tds-freelance](in-tds-freelance.md).

### 5. Losses and unabsorbed depreciation [2025 Act sections 33(11), 108 to 121, 536(2)](https://egazette.gov.in/WriteReadData/2025/265620.pdf)

| Item | Rule | Official source |
|---|---|---|
| Same year | A loss under one head (other than capital gains) is set off against income under another head. A capital loss is set off only against capital gains. A house property loss is set off against other heads only up to INR 200000. | [2025 Act sections 108, 109](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Business loss carried forward | Set off only against business profits, for not more than eight tax years after the year the loss was first computed. | [2025 Act section 112](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Speculation business loss | Set off only against speculation profits, for not more than four tax years. | [2025 Act section 113](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Capital loss carried forward | Eight tax years. A long-term loss is set off only against long-term gains. | [2025 Act section 111](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Unabsorbed depreciation | Added to the depreciation of the next year and so on, with no time limit stated. Brought-forward business loss is set off first. | [2025 Act sections 33(11), 112(3)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Late return | A business, speculation or capital loss is carried forward only if it was determined in a return filed under section 263(1), which means by the due date. | [2025 Act section 121](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Change in shareholding of a closely held company | A loss of an earlier year is not set off unless shares carrying not less than 51% of the voting power are beneficially held, on the last day of the tax year, by the persons who held not less than 51% on the last day of the loss year. An eligible start-up has a separate rule. | [2025 Act section 119(3)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Losses from years under the 1961 Act | Brought-forward losses are set off against income computed under the 2025 Act in the manner of the 1961 Act section they arose under (sections 71B, 72, 73, 73A, 74A). Unabsorbed depreciation under section 32(2) of the 1961 Act is added to the allowance for the tax year beginning 1 April 2026. | [2025 Act section 536(2)(m), (n), (r)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |

### 6. Test minimum alternate tax [2025 Act section 206(1)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) as amended by [Finance Act, 2026 section 59](https://egazette.gov.in/WriteReadData/2026/271439.pdf)

Skip this step for a domestic company that has opted under section 200 or 201: section 206(1) does not apply to it.

For every other company, compute income tax on total income under the normal rules, and compute minimum alternate tax on book profit. If the normal tax is less than the minimum alternate tax, book profit is deemed to be the total income and the company pays the minimum alternate tax. Surcharge and cess are added on top in the same way.

| Item | Rule | Official source |
|---|---|---|
| Rate | 14% of book profit. The 2025 Act as enacted said 15%; the Finance Act, 2026 substituted 14%. | [Finance Act, 2026 section 59(a)(i)](https://egazette.gov.in/WriteReadData/2026/271439.pdf); [2025 Act section 206(1)(b)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Rate for a unit in an International Financial Services Centre earning solely in convertible foreign exchange | 9% | [2025 Act section 206(1)(b)(i)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Base | Profit as shown in the statement of profit and loss, increased by income tax and its provision, amounts carried to reserves, provisions for unascertained liabilities, provisions for losses of subsidiaries, dividends paid or proposed and the other items in section 206(1)(c), then adjusted under clauses (d) onwards. | [2025 Act section 206(1)(c), (d)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Outside it | A company that has exercised the option under section 200(5) or 201(2); life insurance business; a foreign company resident in a treaty country with no permanent establishment in India, and the other foreign company cases in section 206(1)(l). | [2025 Act section 206(1)(l), (q)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Report | A report from an accountant certifying the book profit, in Form No. 66, before the section 63 specified date. | [2025 Act section 206(1)(s)](https://egazette.gov.in/WriteReadData/2025/265620.pdf); [Income-tax Rules, 2026, rule 137](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf) |
| New credit | None. The Finance Act, 2026 omitted clauses (m) to (p) of section 206(1), which gave and carried forward the credit. Minimum alternate tax paid for 2026-27 does not create a credit. | [Finance Act, 2026 section 59(a)(iv)](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |
| Old credit (section 115JAA of the 1961 Act, as on 31 March 2026), domestic company | Usable only by a domestic company that has exercised the option under section 200(5) or 201(2) for a tax year beginning on or after 1 April 2026. Set-off in a year is limited to 25% of the tax payable on total income. The rest is carried forward, not beyond the fifteenth tax year after the year the credit first became allowable. | [Finance Act, 2026 section 59(b), new section 206(3)](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |
| Old credit, foreign company | Set off in a year when normal tax exceeds minimum alternate tax, up to the difference, within the same fifteen-year limit. | [Finance Act, 2026 section 59(b), new section 206(4)](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |

Read the last three rows together. From tax year 2026-27 a domestic company that stays in the standard regime pays minimum alternate tax as a final cost when it applies, and section 206(3) gives it no route to use old credit while it stays there. A company holding old credit should model the section 200 option with the 25% yearly cap before deciding.

### 7. Dividends [2025 Act sections 92, 93, 148, 393](https://egazette.gov.in/WriteReadData/2025/265620.pdf); [Finance Act, 2026 section 44 and First Schedule Part II](https://egazette.gov.in/WriteReadData/2026/271439.pdf)

The company pays no separate tax on distributing a dividend. The dividend is income of the shareholder under "Income from other sources", and the company deducts tax at source.

| Item | Rule | Official source |
|---|---|---|
| Tax deducted at source on a dividend paid by a domestic company to a resident | 10%, deducted before making any distribution or payment. Threshold limit: nil. | [2025 Act section 393(1) Table Sl. No. 7](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| No deduction: individual shareholder | Where the dividend is paid by a mode other than cash and the total for the tax year does not exceed INR 10,000. | [2025 Act section 393(4) Table Sl. No. 10](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Dividend paid to a non-resident or a foreign company | Rates in force: 20% (10% for a dividend from a unit in an International Financial Services Centre), before surcharge and cess, unless a treaty gives a lower rate. | [Finance Act, 2026, First Schedule Part II items 1(b) and 2(b)(xii), (xiii)](https://egazette.gov.in/WriteReadData/2026/271439.pdf); [2025 Act section 207(1)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Expenses against dividend income | No deduction is allowed against dividend income (section 93(2) as substituted by the Finance Act, 2026). | [Finance Act, 2026 section 44](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |
| Inter-corporate dividends | A domestic company that receives dividends from another domestic company, a foreign company or a business trust deducts the amount received, up to the dividend it distributes itself at least one month before the section 263(1) due date. The same distribution cannot be used twice. This deduction survives the section 200 and 201 options. | [2025 Act section 148](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |

### 8. Advance tax [2025 Act sections 403, 404, 408, 424, 425](https://egazette.gov.in/WriteReadData/2025/265620.pdf)

Advance tax is payable when the tax for the year, after tax deducted or collected at source, is INR 10000 or more. A company pays in four instalments.

| Instalment for tax year 2026-27 | Cumulative amount | Official source |
|---|---|---|
| On or before 15 June 2026 | Not less than 15% of the advance tax | [2025 Act section 408(1)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| On or before 15 September 2026 | Not less than 45% | same |
| On or before 15 December 2026 | Not less than 75% | same |
| On or before 15 March 2027 | 100% | same |

An amount paid on or before 31 March counts as advance tax of that financial year.

| Interest | Rule | Official source |
|---|---|---|
| Instalment shortfall (section 425) | 3% of the shortfall for each of the June, September and December instalments and 1% for the March instalment. No interest for June or September if at least 12% or 36% of the tax due on returned income was paid by those dates. | [2025 Act section 425(1), (2)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Year-end shortfall (section 424) | If advance tax paid is less than 90% of the assessed tax, simple interest at 1% for every month or part of a month from 1 April after the tax year, on the shortfall. | [2025 Act section 424(1)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |

The general advance tax mechanics are in [in-advance-tax](in-advance-tax.md), which is written for individuals; the table above is the company schedule.

### 9. Return, audit, interest and late fee [2025 Act sections 63, 172, 263, 266, 423](https://egazette.gov.in/WriteReadData/2025/265620.pdf); [Finance Act, 2026 sections 66, 96](https://egazette.gov.in/WriteReadData/2026/271439.pdf); [Income-tax Rules, 2026, rules 47, 85, 164](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf)

Every company must file a return for the tax year, whatever its income or loss. The form is Form No. ITR-6 (a company that must file under the non-profit provisions uses ITR-7). The due date falls in the financial year after the tax year.

| Item for tax year 2026-27 | Date or amount | Official source |
|---|---|---|
| Return, company with no section 172 report | 31 October 2027 | [Finance Act, 2026 section 66, section 263(1)(c) Table Sl. No. 2](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |
| Return, company to which section 172 applies (international or specified domestic transaction) | 30 November 2027 | [Finance Act, 2026 section 66, section 263(1)(c) Table Sl. No. 1](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |
| Tax audit threshold | Business turnover or gross receipts over one crore rupees in the tax year. Ten crore rupees where cash receipts and cash payments are each not more than 5% of the totals. | [2025 Act section 63(1)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Tax audit report (Form No. 26) | One month before the return due date: 30 September 2027, or 31 October 2027 where section 172 applies. A company already audited under the Companies Act furnishes that audit report with the prescribed particulars. | [2025 Act section 63(4), (5)](https://egazette.gov.in/WriteReadData/2025/265620.pdf); [Income-tax Rules, 2026, rule 47](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf) |
| Transfer pricing report (Form No. 48) | At least one month before the return due date: 31 October 2027. | [Income-tax Rules, 2026, rule 85](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf) |
| Belated return | Within nine months from the end of the tax year (31 December 2027) or before assessment is completed, if earlier. | [2025 Act section 263(4)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Revised return | Within twelve months from the end of the tax year (31 March 2028) or before assessment is completed, if earlier. A fee applies if revised beyond nine months. | [Finance Act, 2026 section 66(b), section 96](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |
| Balance of tax | Paid with interest and fee before furnishing the return (self-assessment). | [2025 Act section 266(1)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Interest for a late return (section 423) | Simple interest, 1% x tax payable x number of months from the day after the due date to the date of filing. | [2025 Act section 423(1)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Fee for a late return (section 428(a)) | INR 5000. INR 1000 if total income does not exceed INR 500000. | [Finance Act, 2026 section 96](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |
| Fee for a late tax audit report (section 428(c)) | INR 75000 for a delay up to one month, INR 150000 after that. | [Finance Act, 2026 section 96](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |
| Fee for a late section 172 report (section 428(d)) | INR 50000 for a delay up to one month, INR 100000 after that. | [Finance Act, 2026 section 96](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |

A late return also blocks the carry-forward of that year's business and capital losses (step 5) and misses the date for exercising the section 200 option.

### 10. Cross-border pointers [2025 Act sections 5, 6(10), 172, 207](https://egazette.gov.in/WriteReadData/2025/265620.pdf)

A foreign company is taxed only on Indian-source income, at 35% plus surcharge and cess on business income, and at the section 207 rates on specified income: dividends 20%, royalties and fees for technical services 20% (for agreements meeting section 207(2)), each before surcharge and cess. A treaty may give a lower rate. A foreign company whose place of effective management is in India is resident but is still a "foreign company" for the rate unless it is a domestic company under section 2(42). For pricing transactions with associated enterprises and the Form No. 48 report, use [india-transfer-pricing](india-transfer-pricing.md). For deducting tax on payments, use [in-tds-freelance](in-tds-freelance.md). For treaty residence conflicts of individuals, use [in-cross-border-india-dual-resident-treaty](in-cross-border-india-dual-resident-treaty.md).

## Boundary and exception table

| Situation | Action |
|---|---|
| Year began before 1 April 2026 (financial year 2025-26 or earlier) | The Income-tax Act, 1961 governs it. Do not apply this skill's section numbers, due dates or the 14% minimum alternate tax rate. Refer. |
| LLP or partnership firm | Not a company. A firm (which includes an LLP under section 2(45)) pays 30% on total income, with a 12% surcharge when total income exceeds INR 1 crore, and 4% cess ([Finance Act, 2026, Part I-B Paragraphs C and F](https://egazette.gov.in/WriteReadData/2026/271439.pdf)). Partner remuneration limits and the firm computation are not covered. |
| Sole proprietor or one-person business without a company | [india-income-tax](india-income-tax.md). |
| Company with no turnover in tax year 2024-25 (formed on or after 1 April 2025) | Paragraph E gives 25% where turnover in tax year 2024-25 "does not exceed" INR 400 crore and says nothing separate about a company that did not exist in that year ([Finance Act, 2026, Part I-B Paragraph E](https://egazette.gov.in/WriteReadData/2026/271439.pdf)). Flag the point and refer before relying on 25%. |
| Company deciding on the section 200 option | Work it both ways as in worked case 2. The option is permanent. Check incentive deductions, old minimum alternate tax credit and losses tied to those deductions before electing. |
| Total income just over INR 1 crore or INR 10 crore (standard regime or foreign company) | Apply marginal relief before cess. |
| Company holds old minimum alternate tax credit | Usable by a domestic company only after the section 200 or 201 option, capped at 25% of the year's tax. Model it. |
| Change of more than 49% in voting power of a closely held company with losses | Section 119(3) may deny the losses. Refer. |
| Payments to a micro or small enterprise outstanding at year end | Check the section 15 time limit of the 2006 Act for each invoice; the return-date grace does not apply. |
| Capital gains, slump sale, buy-back, amalgamation or demerger | Not covered. Refer. |
| Foreign company with a possible permanent establishment or place of effective management in India | Refer before computing. |

## Worked cases

All amounts are hypothetical inputs in INR. They are not thresholds.

### 1. Small domestic company on the 22% option, book profit to tax payable

A private limited trading company opted for the 22% regime under section 115BAA of the 1961 Act in an earlier year, so for tax year 2026-27 it is treated as having opted under section 200 (section 536(2)(f); see step 2). Profit before tax per the statement of profit and loss is 5,910,000. Book depreciation is 420,000. Tax depreciation is 500,000 (plant at 15% on a written down value of 2,000,000 is 300,000; computers at 40% on 500,000 is 200,000). It paid a contractor 400,000 without deducting tax at source, so 30% (120,000) is disallowed. It paid one supplier 50,000 in cash in a day, which is disallowed. Tax deducted at source on its income is 150,000 and it paid advance tax of 1,200,000.

Total income = 5,910,000 + 420,000 - 500,000 + 120,000 + 50,000 = 6,000,000. Tax at 22% = 1,320,000. Surcharge test: total income is under INR 1 crore, but a section 200 company pays the flat 10% surcharge at any income level, so surcharge = 132,000. Cess at 4% of 1,452,000 = 58,080. Total tax = 1,510,080. Minimum alternate tax does not apply. Balance payable with the return = 1,510,080 - 150,000 - 1,200,000 = 160,080, plus any section 424 and 425 interest. Advance tax paid (1,200,000) is under 90% of the assessed tax of 1,360,080 (1,510,080 less tax deducted at source), which is 1,224,072, so section 424 interest runs on the shortfall.

```oa-check
name: Section 200 company, book profit to balance payable
inputs:
  profit_before_tax: 5910000
  book_depreciation: 420000
  plant_wdv: 2000000
  computer_wdv: 500000
  contractor_no_tds: 400000
  cash_payment: 50000
  tds_credit: 150000
  advance_tax: 1200000
steps:
  tax_depreciation: plant_wdv * 0.15 + computer_wdv * 0.40
  tds_disallowance: contractor_no_tds * 0.30
  total_income: profit_before_tax + book_depreciation - tax_depreciation + tds_disallowance + cash_payment
  income_tax: total_income * 0.22
  surcharge: income_tax * 0.10
  cess: (income_tax + surcharge) * 0.04
  total_tax: income_tax + surcharge + cess
  balance: total_tax - tds_credit - advance_tax
  assessed_tax: total_tax - tds_credit
  ninety_percent: assessed_tax * 0.90
expected:
  tax_depreciation: 500000
  tds_disallowance: 120000
  total_income: 6000000
  income_tax: 1320000
  surcharge: 132000
  cess: 58080
  total_tax: 1510080
  balance: 160080
  assessed_tax: 1360080
  ninety_percent: 1224072
```

### 2. Decision: stay in the standard 25% regime or opt for section 200

A manufacturing company (turnover in tax year 2024-25 under INR 400 crore, never opted) has income of 8,000,000 before additional depreciation, and can claim additional depreciation of 1,000,000 under section 33(8). Book profit for minimum alternate tax is 8,000,000. It has no old minimum alternate tax credit.

Standard regime: total income 7,000,000. Tax at 25% = 1,750,000. Total income is not over INR 1 crore, so no surcharge. Cess 4% = 70,000. Tax = 1,820,000. Minimum alternate tax = 8,000,000 x 14% = 1,120,000, plus cess = 1,164,800, which is lower, so normal tax applies.

Section 200: additional depreciation is given up, so total income is 8,000,000. Tax at 22% = 1,760,000. Surcharge 10% = 176,000. Cess 4% of 1,936,000 = 77,440. Tax = 2,013,440.

The standard regime is cheaper by 193,440 this year. The figure that decides it: with total income not over INR 1 crore, the two regimes cost the same when the deductions given up equal 3.2% of the income before those deductions (1 - 25.168 / 26). Here that is 256,000; the company gives up 1,000,000, so it should stay. Under 256,000 of incentive deductions, section 200 would win. Above INR 1 crore of total income the standard effective rate rises to 27.82% and the break-even moves to about 9.5%. Because the option cannot be withdrawn, test later years too, not only this one.

```oa-check
name: Standard 25 percent regime against the section 200 option
inputs:
  income_before_additional_depreciation: 8000000
  additional_depreciation: 1000000
  book_profit: 8000000
steps:
  standard_income: income_before_additional_depreciation - additional_depreciation
  standard_tax: standard_income * 0.25 * 1.04
  mat: book_profit * 0.14 * 1.04
  standard_payable: max(standard_tax, mat)
  option_tax: income_before_additional_depreciation * 0.22 * 1.10 * 1.04
  saving_by_staying: option_tax - standard_payable
  breakeven_deduction: income_before_additional_depreciation * (1 - 0.25168 / 0.26)
expected:
  standard_income: 7000000
  standard_tax: 1820000
  mat: 1164800
  standard_payable: 1820000
  option_tax: 2013440
  saving_by_staying: 193440
  breakeven_deduction: 256000
```

## When to refuse or refer

Refer to a chartered accountant in India: any year under the 1961 Act; a first-time section 200 or 201 election, since it is permanent; companies with old minimum alternate tax credit or losses tied to incentive deductions; a change in shareholding with losses; capital gains, reorganisations and buy-backs; foreign companies where a permanent establishment, place of effective management or treaty relief is in question; banks, insurers, shipping, IFSC units, co-operatives and non-profit companies. Hold the computation if the 2024-25 turnover, the regime already chosen, or the dates of advance tax payments are unknown. This skill does not authorise filing, payment, an election or a dividend.

## Sources

| Source | URL | Read for | Read on |
|---|---|---|---|
| Income-tax Act, 2025 (30 of 2025), Gazette of India Extraordinary, 21 August 2025 (as enacted) | https://egazette.gov.in/WriteReadData/2025/265620.pdf | Sections 1, 2(42), 2(45), 2(46), 3, 5, 6(10), 13, 33 to 37, 63, 92, 93, 108 to 113, 119, 121, 148, 172, 199 to 201, 205 to 207, 263, 266, 393, 403, 404, 408, 423 to 425, 516, 536 | 2026-11-20 |
| Finance Act, 2026 (4 of 2026), Gazette of India Extraordinary, 30 March 2026 | https://egazette.gov.in/WriteReadData/2026/271439.pdf | Section 1 (commencement), section 2(4) (surcharge under the 1961 Act, for the old section numbers only), section 3 (rates for tax year 2026-27, surcharge, marginal relief, cess), First Schedule Part I-B Paragraphs C, E and F and Part II; sections 35, 39, 44, 59, 66, 67, 84, 93 to 96 and 122 amending sections 2, 29, 93, 206, 263, 266, 393, 423 to 425, 427, 428 and 536 of the 2025 Act | 2026-11-20 |
| Income-tax Rules, 2026, notified 20 March 2026, in force 1 April 2026 | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf | Rules 25 and Appendix I (depreciation), 47 (Form No. 26), 85 (Form No. 48), 136 (regime options in the return), 137 (Form No. 66), 164 (Form No. ITR-6) | 2026-11-20 |
| Income Tax Department, Income-tax Act, 1961, section 115BAA (text as on the department's site) | https://wm.incometaxindia.gov.in/w/section-115baa-8 | Heading and 22% rate of the old section, to match it to section 200 | 2026-11-20 |
| Income Tax Department, Income-tax Act, 1961, section 115BAB (text as on the department's site) | https://wm.incometaxindia.gov.in/w/section-115bab-7 | Heading of the old section, to match it to section 201 | 2026-11-20 |
| Ministry of Finance, Memorandum explaining the provisions in the Finance Bill, 2026 | https://www.indiabudget.gov.in/doc/memo.pdf | Part G, "Rationalization of Minimum Alternate Tax provisions" only: read to check the meaning of the section 206 changes. It describes the Bill; the Finance Act, 2026 is the authority | 2026-11-20 |

The 2025 Act was read as enacted, together with the Finance Act, 2026 amendments. No official consolidated text was used. Sections of the 2025 Act cited above that the Finance Act, 2026 amended are 2, 29, 93, 206, 263, 266, 393, 423, 424, 425, 427, 428 and 536. The amendments to sections 2 (clauses (32) and (40)), 29 (clause (1)(e)), 266 (tax credit cross-references) and 393 (interest rows and declarations) do not touch the provisions this skill uses. The other sections cited were checked against the list of sections the Finance Act, 2026 amends and are not on it.

Not yet confirmed: any amendment, CBDT notification or circular issued after 30 March 2026, including any extension of the return or audit due dates for tax year 2026-27. The Income-tax Rules, 2026 have been amended by later notifications since 20 March 2026; those amendments were not read, so every rule number, form number and Appendix I rate here is as notified on 20 March 2026.
Not yet confirmed: an official table of corresponding sections of the 1961 Act and the 2025 Act (the Income Tax Department's section navigator could not be opened: HTTP 403). The reading of section 200 as the successor of section 115BAA and section 201 as the successor of section 115BAB rests on the grounds set out in step 2.
Not yet confirmed: the rate for a company with no turnover in tax year 2024-25 (formed on or after 1 April 2025); Paragraph E does not deal with it expressly.
Not yet confirmed: the number of days in section 15 of the Micro, Small and Medium Enterprises Development Act, 2006 (that Act was not read; the skill cites the section without the figure).
Not yet confirmed: the prescribed exceptions to the cash payment rule under section 36(7) and the prescribed manner of computing additional depreciation for section 205(1)(a).
Not yet confirmed: which regime most small companies use in practice (no official statistic was read; worked case 1 uses the section 200 option as an example only).
Not yet confirmed: the full list of book profit adjustments in section 206(1)(c) to (k) is summarised, not reproduced; capital gains rates under sections 196 to 198 are not stated.
