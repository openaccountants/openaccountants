---
name: india-tax-optimization
description: Use this skill when advising on LEGAL tax minimization strategies for Indian taxpayers — salaried individuals, self-employed professionals, and business owners. Trigger on phrases like "reduce my tax India", "tax planning", "80C", "80D", "old vs new regime", "HRA", "NPS", "Section 24", "presumptive taxation", "capital gains", "GST input credit", or any question about legally minimizing Indian income tax. Covers regime selection, deduction optimization, capital allowances, loss set-off, timing, GST planning, social security, and red lines. ALWAYS read this skill before giving Indian tax optimization advice.
version: 1.0
jurisdiction: IN
tax_year: 2026
last_updated: 2026-10-17
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - bookkeeping-workflow-base
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# India Tax Optimization: Legal Planning for Individuals and Small Businesses

This Guide covers legal ways to reduce Indian income tax for resident salaried individuals, self-employed professionals and small business owners: the choice between the new and old regimes, the deductions each regime allows, presumptive income, depreciation, losses, capital gains timing, GST choices and social security. Figures are for tax year 2026. For Indian income tax this means the tax year from 1 April 2026 to 31 March 2027 under the Income-tax Act, 2025, which replaced the Income-tax Act, 1961 from 1 April 2026. Section numbers below are those of the 2025 Act; most of them changed from the 1961 Act, so an old reference such as "80C" or "44AD" must be read as the 2025 section named here. Returns for the income year 2025-26 (assessment year 2026-27) still fall under the 1961 Act and are not covered. GST is not year-based: the GST rules below are those in force on 17 October 2026, with their start dates.

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | India (Republic of India) |
| Currency | INR |
| Tax year | 1 April 2026 to 31 March 2027 (the 2025 Act calls it "tax year 2026-27") |
| Primary legislation | Income-tax Act, 2025 (30 of 2025); rates for the year in the Finance Act, 2026 (4 of 2026) |
| Rules | Income-tax Rules, 2026 (notified 20 March 2026) |
| Anti-avoidance | General Anti-Avoidance Rule, Chapter XI of the 2025 Act (sections 178 onward) |
| Default regime for individuals | New regime under section 202(1), unless the person opts out under section 202(4) |
| GST | Central Goods and Services Tax Act, 2017 and the State Acts; rates restructured from 22 September 2025 |

### New regime slabs (section 202(1), the default)

Section 202(1) applies to an individual, a Hindu undivided family (HUF), an association of persons (other than a co-operative society), a body of individuals and an artificial juridical person, unless the person opts out. The slabs are the same for every age.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Income taxed at nil: up to | INR 400,000 | "1. Upto ₹400000 Nil" |
| Rate above INR 400,000 up to INR 800,000 | 5% | "to ₹800000 5%" |
| Rate above INR 800,000 up to INR 1,200,000 | 10% | "to ₹1200000 10%" |
| Rate above INR 1,200,000 up to INR 1,600,000 | 15% | "to ₹1600000 15%" |
| Rate above INR 1,600,000 up to INR 2,000,000 | 20% | "to ₹2000000 20%" |
| Rate above INR 2,000,000 up to INR 2,400,000 | 25% | "to ₹2400000 25%" |
| Rate above INR 2,400,000 | 30% | "7. Above ₹2400000 30%" |
| Rebate, new regime (section 156(2)): the lower of 100% of the tax or | INR 60,000 | "100% of the income-tax payable or ₹ 60000, whichever is less" |
| Rebate income limit, new regime (section 156(2)(a)) | twelve lakh rupees | "(a) the income does not exceed twelve lakh rupees" |
| Standard deduction from salary, new regime (section 19(1), Table serial 2(a)) | INR 75,000 | "(a) ₹ 75000 or the salary, whichever is less, where income-tax is computed under section 202(1)" |
| Family pension deduction, new regime: one-third of the pension or | INR 25,000 | "one-third of such income or ₹ 25000, whichever is less, where income-tax is computed under section 202(1)" |

The rebate under section 156(2) is for a resident individual taxed under section 202(1). The income limit is printed in words in the Act. It is a test on total income, so salary before the standard deduction can be higher than the limit. Above the limit, section 156(2)(b) gives marginal relief: the tax payable is cut to the amount by which income exceeds the limit, where that is lower. INR 1,200,000 as the top of the 10% slab and "twelve lakh rupees" as the rebate limit are the same amount used for two different rules.

### Old regime slabs (only if the person opts out of section 202)

The old regime rates for tax year 2026-27 are in the Finance Act, 2026, First Schedule, Part I-B, Paragraph A.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Nil band, individual under 60 (resident or not), HUF, AOP, BOI: up to | INR 250,000 | "(1) where the total income does not Nil; exceed ₹ 250000" |
| Rate above INR 250,000 up to INR 500,000 (under 60) | 5% | "(2) where the total income exceeds 5% of the amount by which the total ₹ 250000" |
| Tax on the first INR 500,000 (under 60) | INR 12,500 | "₹ 12500 plus 20% of the amount by ₹ 500000" |
| Rate above INR 500,000 up to INR 1,000,000 (all ages) | 20% | "₹ 12500 plus 20% of the amount by ₹ 500000" |
| Tax on the first INR 1,000,000 (under 60) | INR 112,500 | "₹ 112500 plus 30% of the amount by ₹ 1000000" |
| Rate above INR 1,000,000 (all ages) | 30% | "₹ 112500 plus 30% of the amount by ₹ 1000000" |
| Nil band, resident individual aged 60 or more but under 80 | INR 300,000 | "(1) where the total income does not Nil; exceed ₹ 300000" |
| Nil band, resident individual aged 80 or more (no 5% band; 20% starts above it) | INR 500,000 | "(1) where the total income does Nil; not exceed ₹ 500000" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Rebate, old regime (section 156(1)), resident individual: the lower of 100% of the tax or | INR 12,500 | "deduction of 100% of income-tax payable or ₹ 12500, whichever is less" |
| Old regime rebate available only if total income does not exceed | INR 500,000 | "if such total income does not exceed ₹ 500000" |
| Standard deduction from salary, old regime (section 19(1), Table serial 2(b)) | INR 50,000 | "(b) ₹ 50000 or the salary, whichever is less, in any other case" |
| Family pension deduction, old regime: one-third of the pension or | INR 15,000 | "one-third of such income or ₹ 15000, whichever is less, in any other case" |

The old regime rebate is a cliff: one rupee of total income above the limit loses the whole rebate, because section 156(1) has no marginal relief.

### Surcharge, cess and other entities (tax year 2026-27)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Top surcharge, new regime (section 3(4) Table serial 10), on total income (excluding dividends and capital gains under sections 196 to 198) above INR 20,000,000 | 25% | "198 of the said Act) exceeds ₹ 20000000, at the rate of 25%" |
| Top surcharge, old regime (Part I-B, Paragraph F, Table 1, serial 1), on total income excluding dividend income and capital gains under sections 196 to 198, above INR 50,000,000 | 37% | "196, 197 and 198 of the said Act) exceeds incorporated or ₹ 50000000, at the rate of 37%" |
| Health and Education Cess, on income-tax plus surcharge, both regimes | 4% | "calculated at the rate of 4% of such income-tax and surcharge" |
| Firm, including an LLP (Part I-B Paragraph C), on the whole total income | 30% | "On the whole of the total income 30%." |
| Domestic company whose turnover or gross receipts in tax year 2024-25 did not exceed INR 400 crore (Part I-B, Paragraph E) | 25% | "(i) where its total turnover or the gross 25% of the total income; receipt in the tax year 2024-25 does not exceed ₹ 400 crores;" |
| Any other domestic company not opting for section 200 or 201 | 30% | "other than that referred to in item (i). 30% of the total income." |
| Minimum alternate tax on book profit, section 206 as amended (from 1 April 2026) | 14% | "for the figures and symbol “15%”, the figures and symbol “14%” shall be substituted" |

The two turnover-based company rates are in Part I-B, Paragraph E of the First Schedule, which section 3(1) of the Finance Act, 2026 applies to tax year 2026-27. Part III prints the same rates for advance tax and tax deducted from salaries. The turnover test looks at tax year 2024-25, not the current year, and it is a cliff: above the limit the whole income is taxed at the higher rate.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Domestic company opting for section 200 (no listed deductions, no set-off of losses from them) | 22% | "the income-tax payable for a tax year shall be at the rate of 22%, at the option of a person being a domestic company" |
| New domestic manufacturing company opting for section 201 | 15% | "1. A (a) 15% on the total Such domestic company" |

### GST rate structure (in force 17 October 2026)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2025-09/press_release_press_information_bureau_0.pdf |
| Standard rate | 18% | "a 2 rate structure with a Standard Rate of 18% and a Merit Rate of 5%" |
| Merit rate | 5% | "a 2 rate structure with a Standard Rate of 18% and a Merit Rate of 5%" |
| Special de-merit rate for a few goods and services | 40% | "a special de-merit rate of 40% for a select few goods and services" |

The revised rates apply to services and to most goods from 22 September 2025. Pan masala, gutkha, cigarettes, chewing tobacco and similar products moved later, on 1 February 2026. The old four-slab structure no longer exists as a set of general rates. Exemptions (nil-rated supplies) continue for listed goods and services. For the rate of a specific item, check the rate notification, not this Guide.

## Section 2: Income Splitting and Structuring

### Old regime vs new regime

- **What the new regime takes away.** Under section 202(2), total income in the new regime is computed without most exemptions and deductions. The list includes the Schedule III exemptions at serials 5, 6, 7, 8, 11 and 17 (serial 11 is the special allowance for rent, the house rent allowance), the interest deduction on a self-occupied house (section 22(1)(b) for property under section 21(6)), and every Chapter VIII deduction except sections 124(1) and 124(2) (employer pension contribution), 125(2) (the Central Government's contribution to the Agniveer Corpus Fund) and 146. A loss under "Income from house property" cannot be set off against any other head in the new regime (section 202(2)(b)(ii)).
- **What the new regime keeps.** The higher standard deduction and family pension deduction (tables in Section 1), the employer's contribution to the notified pension scheme (Section 3), and the interest deduction on a let-out property against that property's rent.
- **How to choose.** Compute the tax both ways every year, including surcharge and cess. There is no fixed break-even amount: it depends on which old regime deductions the person can actually claim. Section 11, Example 1, shows the method.
- **How to opt out, and how often.** A person with no business or profession income opts out "along with the return of income to be furnished under section 263(1)" for the year (section 202(4)(b)), so the choice can differ each year. A person with business or profession income must opt out on or before the return due date under section 263(1). That option then applies to later years, can be withdrawn only once, and after withdrawal the person can never opt out again unless the business or profession income ends (section 202(4)(a)).

### Sole proprietor vs firm (including LLP) vs company

- **Sole proprietor.** Profit is taxed at the individual's slab rates. A small business or professional can use the presumptive scheme in section 58 (Section 4) and avoid computing actual profit.
- **Firm or LLP.** A firm, including an LLP, pays the flat firm rate in the Section 1 table on its whole total income, before surcharge and cess. Check the partner's own treatment of the profit share and of interest and remuneration from the firm in the 2025 Act before modelling it; this Guide does not state it.
- **Private limited company.** A domestic company may opt for section 200 (rate in the Section 1 table) and give up the listed deductions; once exercised, that option cannot be withdrawn. Otherwise the Part I-B rate depends on turnover in tax year 2024-25. Minimum alternate tax under section 206 applies where the tax on total income is less than the minimum alternate tax on book profit (rate in the Section 1 table); check section 206 for the companies it does not cover. A company that opts for section 200 or 201 from 1 April 2026 may use minimum alternate tax credit from earlier years only within the limit the Finance Act, 2026 sets. For company formation see `india-formation`.

### Family structuring

- **HUF.** A Hindu undivided family is a separate taxpayer. It is named in section 202(1) for the new regime, it gets its own nil band under the old regime (Section 1 table), and it can claim the section 153 savings interest deduction in its own right.
- **Spouse and son's wife.** Section 99 adds to an individual's income any salary, commission, fees or other remuneration paid to the spouse by a concern in which the individual has a substantial interest. It does not add income solely attributable to the application of the spouse's own technical or professional knowledge, experience and qualification; only that income stays the spouse's. Income from assets transferred to the spouse or to the son's wife without adequate consideration is also added back.
- **Minor child.** Section 99 adds a minor child's income to the parent's income, except income from work done by the child, income from activities where the child's own skill, talent, specialised knowledge or experience is applied, and income of a minor child with a disability of the kind in section 154. Any small exemption per child must be checked in the 2025 Act's Schedules before it is applied; this Guide does not state one.

## Section 3: Deductions Most People Miss

### Old regime deductions (Chapter VIII of the 2025 Act)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 123: life insurance, provident fund and the other sums in Schedule XV, combined cap per year | INR 150,000 | "aggregate of the sums enumerated in Schedule XV, as does not exceed ₹ 150000" |
| Section 124(3): the individual's own contribution to the notified pension scheme, over and above section 123 | INR 50,000 | "shall be allowed a deduction not exceeding ₹50000" |
| Section 126(a): health insurance and preventive health check-up for self and family, in aggregate | INR 25,000 | "preventive health check-up of the assessee or his family, up to ₹25000 in aggregate" |
| Section 126: cap where the insured person is a senior citizen (replaces the INR 25,000) | INR 50,000 | "shall be substituted with ₹50000 for ₹25000" |
| Section 22(2)(a): interest on a loan for a self-occupied house, cap per year | INR 200,000 | "(a) ₹ 200000" (section 22(2)) |
| Section 127: maintenance of a dependant with disability | INR 75,000 | "shall be substituted with “₹ 125000” for “₹ 75000”" |
| Section 127: severe disability amount | INR 125,000 | "shall be substituted with “₹ 125000” for “₹ 75000”" |
| Section 134: rent paid for one's own residence: rent above this share of total income | 10% | "on payment of such rent exceeding 10% of his total income, subject to a maximum of ₹ 5000 per month, or 25% of total income" |
| Section 134: monthly cap | INR 5,000 | "on payment of such rent exceeding 10% of his total income, subject to a maximum of ₹ 5000 per month, or 25% of total income" |
| Section 134: alternative cap as a share of total income (the lower cap applies) | 25% | "on payment of such rent exceeding 10% of his total income, subject to a maximum of ₹ 5000 per month, or 25% of total income" |
| Section 133(b): donations to the funds and institutions in that clause, share deductible | 50% | "an amount equal to 50% of the aggregate of the sums paid as donation" |
| Section 153(2)(a): savings account interest, individual who is not a senior citizen, or HUF | INR 10,000 | "the whole of the interest up to a maximum amount of ₹ 10000 on deposits in a savings account" |
| Section 153: interest on deposits including time deposits, individual who is a senior citizen | INR 50,000 | "the whole of the interest up to a maximum amount of ₹ 50000 on deposits in any account, including time deposits" |

Notes on the table:
- **Section 129 (education loan interest).** The whole of the interest on a loan from a financial institution or an approved charitable institution for higher education of the individual or a relative is deductible, with no amount cap, for the initial tax year and the seven tax years immediately after it.
- **Section 133 (donations).** Clause (a) gives the whole of the donation for the funds it lists; clause (b) gives the share in the table for the others. Qualifying limits and conditions apply; check the fund's status before the donation.
- **Section 134 (rent without house rent allowance).** The deduction is the rent above the share of total income in the table, capped at the lower of the monthly cap and the share of total income in the table. Other conditions are prescribed in the Rules.
- **Section 154.** A resident individual certified as a person with disability gets a deduction of the same two amounts as section 127, for his own disability.
- **Senior citizen health cover.** The same section 126 cap applies separately to premiums for the parents.
- None of these deductions is available in the new regime (section 202(2)(a)(v) and (xii)).

### Employer pension contributions (both regimes)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 124(1)(a): employer contribution to the notified pension scheme, cap as a share of salary, Central or State Government employer | 14% | "(a) 14%, where such contribution is made by the employer being the Central Government" |
| Section 124(1)(b): cap for any other employer (raised to the government rate by section 124(2) where tax is computed under section 202(1)) | 10% | "(b) 10%, where such contribution is made by an employer other than an employer referred to in clause (a)" |
| Employer contributions to a recognised provident fund, the section 124(1) scheme and an approved superannuation fund, combined, taxed as a perquisite above | INR 750,000 | "contribution, in excess of ₹ 750000 in a tax year, made to the account of the assessee by the employer" |

### New regime: what remains

| Item | Available in the new regime | Where |
| --- | --- | --- |
| Standard deduction from salary | Yes, the new regime amount | Section 1 table |
| Family pension deduction | Yes, the new regime amount | Section 1 table |
| Employer contribution to the notified pension scheme | Yes | Sections 124(1) and 124(2), table above |
| Central Government contribution to the Agniveer Corpus Fund | Yes | Section 125(2) |
| Interest on a loan for a let-out house | Yes, against that property's income, but a loss from house property cannot be set off against other heads | Sections 22 and 202(2)(b)(ii) |
| House rent allowance, section 123, 126, 129, 133, 134, 153 and the other Chapter VIII deductions | No | Section 202(2) |

## Section 4: Capital Allowances Optimization

### Depreciation (business income, written down value)

The rates are in Appendix I to the Income-tax Rules, 2026 (rule 25). Depreciation is allowed by block of assets on the written down value.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Buildings used mainly for residential purposes, except hotels and boarding houses | 5% | "Buildings which are used mainly for residential purposes 5" |
| Other buildings | 10% | "Buildings other than those used mainly for residential 10" |
| Furniture and fittings, including electrical fittings | 10% | "Furniture and fittings including electrical fittings [See Note 5 10" |
| Machinery and plant (general) | 15% | "Machinery and plant other than those covered by sub-items 15" |
| Motor cars, other than those used in a business of running them on hire | 15% | "Motor cars, other than those used in a business of running 15" |
| Motor buses, motor lorries and motor taxis used in a business of running them on hire | 30% | "Motor buses, motor lorries and motor taxis used in a business 30" |
| Computers including computer software | 40% | "Computers including computer software (See Note 7 below) 40" |
| Know-how, patents, copyrights, trademarks, licences, franchises and similar rights (intangible assets) | 25% | "Know-how, patents, copyrights, trademarks, licences, 25" |

### Additional depreciation (section 33(8) and (9))

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Additional depreciation on new machinery or plant, in the year it is acquired and put to use | 20% | "(a) 20% of the actual cost of the new machinery or plant" |
| If put to use for less than one hundred and eighty days in the year: this share in that year and the same share in the next year | 10% | "(b) 10% of the actual cost, if the new machinery or plant is acquired and put to use for less than one hundred and eighty days" |

Additional depreciation is only for a business of manufacture or production of an article or thing, or of generation, transmission or distribution of power. The machinery must be new: not used by anyone before, in or outside India. It does not apply to a ship or aircraft, to machinery installed in an office or residential accommodation (including a guest house), to office appliances or road transport vehicles, or to an asset whose whole cost is deducted in one year. Additional depreciation is one of the deductions a business gives up in the new regime (section 202(2)(a)(vi)).

### Presumptive taxation (section 58)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Eligible business (Table serial 1): turnover or gross receipts limit | two crore rupees | interleaved table text: "exceed two" ... "than the crore rupees" |
| Eligible business: higher limit where cash receipts are not more than the cash share below | three crore rupees | "exceed three receipts which is against serial crore rupees" |
| Cash share allowed for the higher limit (business and profession) | 5% | "in cash, does not respect of that tax exceed 5% of year; the total" |
| Deemed profit on turnover received through a bank or other specified non-cash mode | 6% | "(i) 6% of total business (b) does not turnover or gross" |
| Deemed profit on the rest of the turnover | 8% | "(ii) 8% of total turnover or turnover or gross" |
| Specified profession (Table serial 3): deemed profit as a share of gross receipts, or a higher amount claimed | 50% | "3. Specified Specified (a) Does 50% of the gross" |
| Specified profession: gross receipts limit | fifty lakh rupees | "not exceed fifty receipts or profit as referred lakh rupees;" |
| Specified profession: higher limit where cash is not more than the cash share above | seventy-five lakh rupees | "seventy-five higher. lakh rupees" |

- The 6% rate applies to turnover received by banking or online mode during the tax year or before the return due date under section 263(1) for that year (Table serial 1). A cheque or bank draft that is not account payee counts as cash (section 58(9)).
- Who can use it: Table serial 1 is for a resident individual, Hindu undivided family or firm other than a limited liability partnership that has not claimed a deduction under section 144 or Chapter VIII-C for the year, does not carry on a specified profession, and does not earn commission or brokerage or carry on an agency business (section 58(11)(a)). Table serial 3 is for a resident individual or firm other than a limited liability partnership (section 58(11)(b)). Companies and LLPs cannot use section 58.
- The higher limits are an AND test: turnover within the higher limit AND cash receipts not more than the cash share.
- The specified professions are those listed in section 62(4).
- A person who declares profit under Table serial 1 for a year and then declares outside it in any of the five following tax years cannot use the scheme for the five tax years after that year (section 58(7)). A person who claims a profit lower than the deemed profit, with total income above the maximum amount not chargeable to tax, must keep books and get them audited under sections 62 and 63 (section 58(3) and (8)).
- A presumptive taxpayer under Table serial 1 or 3 pays all advance tax by 15 March (section 408(2)).
- Deemed profit already covers depreciation and other expenses; no separate claim is made.

## Section 5: Loss Utilization

### Set-off in the same year (sections 108 and 109)

| Loss | Set off against |
| --- | --- |
| Loss from one source under a head (other than capital gains) | Income from another source under the same head (section 108(1)) |
| Business or profession loss | Any other head except "Salaries" (section 109(1)(a)) |
| House property loss | Any other head, up to the cap in the table below (section 109(1)(b)); not at all in the new regime (section 202(2)(b)(ii)) |
| Short-term capital loss | Gains on any other capital asset (section 108(2)(a)) |
| Long-term capital loss | Gains on another long-term capital asset only (section 108(2)(b)) |
| Capital loss | Never against any other head (section 109(2)) |
| Speculation business loss | Profits of another speculation business only (section 113(1)) |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| House property loss set off against other heads, cap per year | INR 200,000 | "loss under the head “Income from house property” shall be set off to the extent of ₹ 200000" |

### Carry forward

| Loss | Carried forward against | Period |
| --- | --- | --- |
| House property | House property income only | Eight tax years after the year of loss (section 110) |
| Capital loss | Capital gains only, long-term loss against long-term gains only | Eight tax years (section 111) |
| Business loss (not speculation) | Profits of any business or profession | Eight tax years (section 112) |
| Speculation business loss | Speculation profits only | Four tax years (section 113(3)) |
| Loss from owning and maintaining race horses | Income from that activity only | Four tax years (section 115) |

- Where depreciation allowance under section 33(11) or 45(7) is also carried forward, the business loss under section 112 is set off first (section 112(3)).
- In the new regime, a loss or depreciation carried forward from an earlier year is not set off if it comes from a deduction the new regime denies, and it is treated as used up (sections 202(2)(b)(i) and 202(3)).
- A capital, business, speculation or race-horse loss is carried forward only if it was determined in a return filed under section 263(1) (section 121). The house property loss in section 110 is not on that list.

## Section 6: Timing Strategies

### Advance tax (sections 404 and 408)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Advance tax payable when tax for the year is this amount or more | INR 10,000 | "is ₹10000 or more" |
| By 15 June: at least this share of advance tax | 15% | "1. On or before Not less than 15% of such advance tax. the 15th June." |
| By 15 September: at least this share, cumulative | 45% | "2. On or Not less than 45% of such advance tax" |
| By 15 December: at least this share, cumulative | 75% | "3. On or Not less than 75% of such advance tax" |
| Interest for default (section 424(1)), simple, per month or part of a month | 1% | "simple interest at the rate of 1% for every month or part of a month" |
| Section 424(1)(b): default where advance tax paid is less than this share of assessed tax | 90% | "less than 90% of the assessed tax" |
| Interest for deferment (section 425(1)), flat, on the June, September and December shortfall | 3% | "Shortfall till 15th day of 3% of June." |

The whole amount is due by 15 March. Section 403(3) exempts a resident aged 60 or more who has no business or profession income. Spreading income or gains so that payment falls in a later instalment reduces deferment interest only where the income genuinely arises later; interest runs on the shortfall against what was due at each date.

### Other timing points

| Strategy | Detail |
| --- | --- |
| Old regime deductions by 31 March | Payments under sections 123, 124(3), 126 and 133 count in the tax year in which they are paid. Paying by 31 March 2027 brings them into tax year 2026-27. |
| Harvesting the listed equity exemption | The section 198 exemption for long-term gains on listed equity (Section 9 table) is per year. Realising gains up to it each year uses the exemption; buying back resets the cost. Check GAAR (Section 9) for a sale and buy-back done only for tax. |
| Reinvesting a long-term gain | Section 82 (gain on a residential house reinvested in one residential house in India, bought within one year before or two years after the transfer, or built within three years) and section 85 (a long-term gain on land or building, or both, invested within six months after the transfer in long-term specified assets, up to the cap in the Section 9 table) defer or exempt the gain. Section 86 gives a similar relief when the original asset is not a house. |
| Employer certificates | The employer issues the salary TDS certificate in Form No. 130 under the Income-tax Rules, 2026. Check that employer pension contributions appear in it. |
| Returns for tax year 2026-27 | Due dates fall in 2027 (Section 10). |

## Section 7: GST Optimization

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://cbic-gst.gov.in/pdf/01062019-GST-An-Update.pdf |
| Registration threshold, suppliers of goods only, in States that opted for the higher limit | INR 40 lakh | "for the suppliers of goods would be Rs. 40 lakhs and Rs. 20 lakhs" |
| Registration threshold, goods only, in the States CBIC listed on 1 June 2019: Arunachal Pradesh, Manipur, Meghalaya, Mizoram, Nagaland, Puducherry, Sikkim, Telangana, Tripura and Uttarakhand (list as of 2019; confirm the State's current position) | INR 20 lakh | "Rs. 40 lakhs and Rs. 20 lakhs (in the States of Arunachal Pradesh, Manipur, Meghalaya, Mizoram, Nagaland, Pudu" |
| Registration threshold, suppliers of services (and mixed suppliers) | INR 20 lakh | "for suppliers of services would be Rs. 20 lakhs and Rs. 10 lakhs (for States of Manipur, Mizoram, Nagaland and Tripura)" |
| Registration threshold, services, in Manipur, Mizoram, Nagaland and Tripura | INR 10 lakh | "for suppliers of services would be Rs. 20 lakhs and Rs. 10 lakhs (for States of Manipur, Mizoram, Nagaland and Tripura)" |
| Composition limit (preceding year aggregate turnover), goods suppliers, manufacturers and restaurants | INR 1.5 crore | "Composition threshold limit increased to be Rs. 1.5 Crore" |
| Composition limit in the special category States: Arunachal Pradesh, Manipur, Meghalaya, Mizoram, Nagaland, Sikkim, Tripura and Uttarakhand | INR 75 lakh | "have the said limit as Rs. 75 lakh" |
| Composition rate, manufacturers (central plus State) | 1% | "Manufacturers 1%" |
| Composition rate, traders, on turnover of taxable supplies | 1% | "specified Traders 1%" |
| Composition rate, restaurants | 5% | "Restaurants 5%" |
| Composition option for service providers (section 10(2A)), rate | 6% | "with a tax rate of 6% (3% CGST +3% SGST) having an Annual Turnover in the preceding Financial Year up to Rs. 5" |
| Section 10(2A) limit (preceding year turnover) | INR 50 lakh | "having an Annual Turnover in the preceding Financial Year up to Rs. 50 lakhs" |

The statutory thresholds in section 22(1) of the CGST Act are printed in words: twenty lakh rupees generally and ten lakh rupees in special category States (https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter6/section22_v1.00.html). The higher goods-only limit applies only in States that adopted it.

| Topic | Rule | Source |
| --- | --- | --- |
| Composition: who cannot use it | A composition taxpayer may not make inter-State outward supplies, supplies not leviable to tax, or supplies through an e-commerce operator that collects tax at source, and does not take input tax credit (section 10) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter3/section10_v1.00.html |
| Input tax credit: invoice must be reported | Credit needs a tax invoice AND the supplier must have furnished its details in the statement of outward supplies, communicated to the recipient (section 16(2)(aa)) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter5/section16_v1.00.html |
| Input tax credit: time limit | Credit for an invoice cannot be taken after the thirtieth day of November following the end of the financial year, or after the annual return is filed, whichever is earlier (section 16(4)) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter5/section16_v1.00.html |
| E-invoicing | Required where aggregate turnover in any financial year from 2017-18 exceeds five crore rupees, from 1 August 2023 (Notification 10/2023-Central Tax) | https://gstcouncil.gov.in/sites/default/files/2024-05/10ct_eng.pdf |
| Rate planning | Since 22 September 2025 most goods and services fall in the standard or merit rate (Section 1). Recheck the rate of every main supply and input; a business whose input rate is now above its output rate should review its credit position with `india-gst`. | https://gstcouncil.gov.in/sites/default/files/2025-09/press_release_press_information_bureau_0.pdf |

The 57th GST Council meeting (8 October 2026) recommended further changes, for example to arrest provisions, the prosecution threshold and the general penalty. These are recommendations, not law, until the CGST Act or Rules are amended and notified (press release: https://gstcouncil.gov.in/sites/default/files/2026-10/press_release_0.pdf). Do not plan on them yet. Exports, place of supply and refunds are in `india-gst`.

## Section 8: Social Security Optimization

The Code on Social Security, 2020 and the Code on Wages, 2019 came into force on 21 November 2025. The Employees' Provident Funds Scheme, 2026 replaced the 1952 Scheme, and the Social Security (Central) Rules, 2026 now set the ESI contributions. Employer obligations are in `in-pf-esi-employer` and `india-payroll`.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2026/273957.pdf |
| EPF: employer contribution, as a share of wages; the employee contributes an equal amount | twelve per cent | "at the rate of twelve per cent of the wages payable to the employee" |

The rate is ten per cent for the class of establishments the Central Government notifies (EPF Scheme 2026, paragraph 18(2), proviso).

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2026/272366.pdf |
| ESI: employer contribution (rule 19(1)(a)) | three and one-fourth per cent | "three and one- fourth per cent. of the wages payable to an employee" |
| ESI: employee contribution (rule 19(1)(b)) | three-fourth per cent | "three-fourth per cent. of the wages payable to an employee" |

- **Tax on provident fund.** The employee's own provident fund contribution counts towards the section 123 cap (old regime only). Employer contributions to a recognised provident fund, the section 124(1) pension scheme and an approved superannuation fund are taxed as a perquisite above the combined limit in the Section 3 table.
- **Pension scheme.** The employer's contribution is the one deduction that survives in the new regime (Section 3). On closure of the account or opting out, Schedule II (Table serial 6) exempts a payment up to the share in the table below.
- **Wage ceilings.** The EPF and ESI wage ceilings are "as notified" under the Codes. No allowed page prints the current ceilings, so check the notification before using one.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| National Pension System payment on closure or opting out, exempt up to this share of the total amount payable | 60% | "the said payment does not exceed 60% of the total amount payable at the time of such closure" |

## Section 9: Investment and Retirement

### Capital gains rates and limits (2025 Act)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Short-term gains on listed equity shares, equity-oriented fund units and business trust units where securities transaction tax applies (section 196) | 20% | "income-tax calculated on such short-term capital gains at the rate of 20%" |
| Long-term gains on those assets (section 198): exempt amount per year | INR 125,000 | "on such long-term capital gains exceeding ₹ 125000 at the rate of 12.5%" |
| Long-term gains on those assets above the exempt amount | 12.5% | "on such long-term capital gains exceeding ₹ 125000 at the rate of 12.5%" |
| Other long-term capital gains (section 197) | 12.5% | "income-tax calculated on such long-term capital gains at the rate of 12.5%" |
| Section 85(2): cap on investment in long-term specified assets, during any tax year, and in the year of transfer and the next year together | fifty lakh rupees | "shall not exceed fifty lakh rupees" |
| Unit linked insurance policy issued on or after 1 February 2021 (Schedule II): maturity sum exempt only if aggregate premium in any year is not more than | INR 250,000 | "aggregate of premium for all such policies (in any of the tax years during the term of all of such policies) ≤ ₹ 2,50,000" |

- **Land or building bought before 23 July 2024.** For a resident individual or HUF, section 197 lets the tax on the long-term gain be capped at what it would have been under the earlier method with indexation; the excess is ignored (section 197, the formula after sub-section (1)). Compute both and keep the lower only where the section applies.
- **Debt funds, unlisted bonds and debentures** have their own capital gains rules in the 2025 Act (some unlisted bonds and debentures transferred, redeemed or maturing on or after 23 July 2024 are dealt with separately). Check the definitions in the Act before quoting a rate.
- **Long-term gains and the rebate.** Sections 196(2), 197(2) and 198(3) let a resident individual or HUF use any unused part of the nil band against these gains. The new regime rebate is capped by section 156(3): "The deduction under sub-section (2), shall not exceed income-tax payable as per the rates provided in section 202(1)." Our reading: the rebate does not reduce tax charged at the special rates in sections 196 to 198.
- **Instruments.** Section 123 covers the sums in Schedule XV (including life insurance premiums and provident fund contributions). Which instruments qualify, their lock-in periods and whether their interest or maturity is exempt are set by Schedule XV and Schedule II and by each scheme's own rules; check them for the instrument in hand.

### GAAR (General Anti-Avoidance Rule)

- Chapter XI of the 2025 Act (sections 178 onward). An arrangement can be declared an impermissible avoidance arrangement and its tax consequence determined under the Chapter.
- Section 179: an impermissible avoidance arrangement is one whose main purpose is to obtain a tax benefit AND that also does at least one of the things the section lists (for example, creates rights or obligations not ordinarily created between persons dealing at arm's length, or lacks commercial substance).
- Rule 128 of the Income-tax Rules, 2026 keeps Chapter XI from applying to an arrangement where the aggregate tax benefit in the tax year, to all parties together, does not exceed three crore rupees (https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf).

### Scrutiny triggers

| Trigger | Risk |
| --- | --- |
| House rent allowance or section 134 rent claimed without genuine rent | Disallowed; penalty |
| Receipts for section 123 or 126 that do not match the insurer or fund records | Disallowed; penalty |
| Income that does not match the Annual Information Statement | Notice and reassessment; reconcile before filing |
| Capital gains with no advance tax | Interest under sections 424 and 425 (Section 6) |
| Money or property received without consideration above the section 92(2)(m) limit (table below) | Taxed as income of the recipient; gifts from relatives, on marriage, by will or inheritance and the other listed cases are excluded |
| Assets transferred to a spouse, son's wife or minor child | Income added back under section 99 |
| Presumptive income that does not fit the lifestyle or bank credits | Scrutiny risk |
| Benami transactions | A separate law, the Benami Transactions (Prohibition) Act, applies; refer |

### Absolute prohibitions

- **NEVER** advise fabricating rent receipts for a house rent allowance or section 134 claim.
- **NEVER** advise backdating an investment or payment to claim it in an earlier tax year.
- **NEVER** advise receiving cash at or above the section 186 limit (table below) from one person in a day, for one transaction, or for transactions relating to one event or occasion. Section 451 allows a penalty equal to the sum received.
- **NEVER** advise paying a business expense in cash above the section 36(4) limit in a day to one person. The expense is disallowed (the Rules list exceptions; the limit is higher for payments to transport operators under section 36(6)).
- **NEVER** advise splitting an arrangement only to keep the tax benefit under the GAAR threshold.
- **NEVER** advise ignoring differences in the Annual Information Statement; resolve them before filing.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 92(2)(m): money received without consideration in a year, taxed in full if the total exceeds | INR 50,000 | "any sum of money without consideration, the total of which exceeds ₹ 50000, the whole of such sum" |
| Section 186: no cash receipt of this amount or more | INR 200,000 | "No person shall receive an amount of ₹ 200000 or more" |
| Section 36(4): cash expense limit per person per day | INR 10,000 | "made in a day to a person exceeds ₹10000 and is not made through specified banking or online mode" |
| Section 36(6): limit for payments to transport operators | INR 35,000 | "the figures “₹10000” shall be read as “₹35000” in case the payment is mad" |

## Section 10: Annual Tax Planning Calendar (tax year 2026-27)

| When | Action |
| --- | --- |
| April 2026 | Tax year starts. Compute tax both ways and decide the regime (salaried: the final choice is made with the return; business: see section 202(4)(a) in Section 2). Review salary structure. |
| By 15 June 2026 | First advance tax instalment (Section 6). |
| By 15 September 2026 | Second advance tax instalment. Mid-year review of gains and deductions. |
| By 15 December 2026 | Third advance tax instalment. Review capital gains for the year and harvesting (Section 9). |
| January to March 2027 | Collect rent, insurance, donation and loan interest certificates. Old regime payments under sections 123, 124(3), 126 and 133 by 31 March 2027. |
| By 15 March 2027 | Last advance tax instalment; presumptive taxpayers pay all of it by this date. |
| 2027 return dates | See the table below. |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Return due date (section 263(1)(c) as substituted), where a transfer pricing report under section 172 is required | 30 November | "Where the 30th November. of the firm or the spouse of such" |
| Companies and assessees whose accounts must be audited | 31 October | "2. (i) Company; Where the 31st October." |
| Business or profession income where accounts need no audit | 31 August | "3. (i) Assessee having income Where the 31st August." |
| Any other assessee (salary, rent, capital gains, no business) | 31 July | "4. Any other assessee. 31st July." |

The dates are in the financial year after the tax year, so for tax year 2026-27 they fall in 2027. A revised return can be filed within twelve months from the end of the tax year or before assessment, whichever is earlier, subject to section 428(b) (section 263(5) as substituted). An updated return can be filed within forty-eight months from the end of the financial year after the tax year (section 263(6)(a)).

## Section 11: Cash Impact Examples

All amounts in this section are hypothetical and in INR. Tax figures are our arithmetic using the tables in Section 1; they are checked in the test cases.

### Example 1: Old vs new regime (resident salaried individual under 60, gross salary 1,500,000)

| Step | New regime | Old regime |
| --- | --- | --- |
| Gross salary | 1,500,000 | 1,500,000 |
| Standard deduction | 75,000 | 50,000 |
| House rent allowance exempt (hypothetical amount) | not allowed | 240,000 |
| Section 22(2) self-occupied house interest | not allowed | 200,000 |
| Section 123 | not allowed | 150,000 |
| Section 124(3) | not allowed | 50,000 |
| Section 126 | not allowed | 25,000 |
| Taxable income | 1,425,000 | 785,000 |
| Tax before cess | 93,750 | 69,500 |
| Cess | 3,750 | 2,780 |
| Tax payable | 97,500 | 72,280 |

New regime: nil on the first 400,000; 5% on the next 400,000 is 20,000; 10% on the next 400,000 is 40,000; 15% on the 225,000 above 1,200,000 is 33,750; total 93,750. Total income is above the rebate limit, and the marginal relief test does not help because the tax is far less than the 225,000 by which income exceeds the limit. Old regime: 12,500 on the first 500,000, plus 20% on the 285,000 above 500,000 (57,000), total 69,500. The old regime saves 25,220 here only because the person has a home loan, rent and full investments. Without the house rent allowance and the home loan, the new regime wins.

### Example 2: Employer pension contribution in the new regime

Salary 1,600,000 (hypothetical, including basic salary of 800,000), private employer, new regime. The employer also pays 112,000 (14% of the basic salary, assumed to be the salary base section 124 uses) into the notified pension scheme. Section 16(k) makes that contribution part of salary, and section 124(2) allows the same amount as a deduction in the new regime, up to the cap in the Section 3 table. Total income is 1,525,000 (1,600,000 plus 112,000, less the 75,000 standard deduction and the 112,000 deduction) and tax before cess is 108,750. Paid as cash salary instead, total income would be 1,637,000 and tax before cess 127,400, so the contribution saves 18,650 before cess.

### Example 3: Harvesting the listed equity exemption

An investor holds listed equity shares with an unrealised long-term gain of 300,000. Selling units that carry 125,000 of long-term gain in the tax year, with securities transaction tax paid, uses the section 198 exemption, so no tax arises on that sale. Buying back resets the cost. If the whole 300,000 were realised in one later year, tax under section 198 would be 12.5% on 175,000, which is 21,875 before surcharge and cess. Keep the sale and buy-back as genuine market trades; GAAR (Section 9) applies to arrangements whose main purpose is a tax benefit.

### Example 4: Presumptive business income (section 58)

A trader has turnover of 15,000,000, all received through a bank (cash share nil, within the higher limit). Deemed profit at 6% is 900,000. In the new regime, tax before cess is 20,000 plus 10% on 100,000 above 800,000, which is 30,000. Total income is below twelve lakh rupees, so the section 156(2) rebate removes the whole 30,000 for a resident individual with no special-rate income. If the trader's actual profit is higher, the scheme still taxes only the deemed profit. If it is lower, the trader may declare the lower profit, but must then keep books and have them audited if total income exceeds the maximum amount not chargeable to tax (section 58(3)); if the trader used the scheme in any of the five preceding tax years, section 58(7) also bars the scheme for the next five tax years.

## The method, step by step

1. **Confirm the year and the law.** Tax year 2026-27 (1 April 2026 to 31 March 2027) under the Income-tax Act, 2025 (https://egazette.gov.in/WriteReadData/2025/265620.pdf), with rates from the Finance Act, 2026 (https://egazette.gov.in/WriteReadData/2026/271439.pdf). For income of 2025-26 use the 1961 Act.
2. **Fix residence and the person.** Individual, HUF, firm or company; residence decides the rebate and the senior bands. See `in-tax-residency`.
3. **List income by head** (salary, house property, business or profession, capital gains, other sources) and the special-rate items (sections 196 to 198, virtual digital assets in `india-crypto-tax`).
4. **Test presumptive income** under section 58 for a small business or professional (Section 4), and depreciation under Appendix I of the Income-tax Rules, 2026 (https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf) for anyone on actual profit.
5. **Compute total income twice**: under section 202 (new regime, Section 3 "what remains") and under the old regime with every Chapter VIII deduction the person can prove.
6. **Apply set-off and carry forward** under sections 108 to 115 (Section 5), remembering the new regime limits in section 202(2)(b).
7. **Apply the slabs, rebate, surcharge and cess** from the Section 1 tables for each regime, and pick the lower. For a business, remember the once-only withdrawal rule in section 202(4)(a).
8. **Plan payments**: advance tax under sections 404 and 408 (Section 6, `in-advance-tax`), and old regime payments by 31 March.
9. **Check GST** registration, composition and credit (Section 7, with detail in `india-gst`; CBIC update: https://cbic-gst.gov.in/pdf/01062019-GST-An-Update.pdf).
10. **Run the GAAR and prohibition checks** (Section 9, rule 128 of the Rules), then file by the section 263(1)(c) date (Section 10).

## Ask the client first

- Do you have any business or profession income this year, and have you ever opted out of the new regime and then withdrawn? (Section 202(4) decides whether you can still choose each year.)
- What will you actually pay this year: rent (and do you receive a house rent allowance), home loan interest on a self-occupied house, insurance and provident fund under section 123, health insurance, education loan interest, donations?
- What was your business turnover or professional receipts, and what share was received in cash? (Presumptive limits and rates, Section 4.)
- Will you sell shares, fund units, property or other assets this year, how long have you held them, and when did you buy any land or building? (Section 9.)
- Does your employer contribute to the National Pension System, provident fund or superannuation, and how much? (Section 3 and Section 8.)
- Are you resident, and how old will you be during the year? (Rebate and senior bands, Section 1.)

## When to refuse or refer

- Any request to fabricate, backdate or disguise a transaction (Section 9 prohibitions): refuse.
- A plan whose main purpose is the tax benefit and whose combined benefit may exceed the GAAR threshold: refer to a chartered accountant before acting.
- Non-residents, RNOR status, foreign income or treaty claims: refer; see `in-tax-residency` and `in-cross-border-india-dual-resident-treaty`.
- Companies choosing between section 200, section 201 and the normal rates with minimum alternate tax credit to use, and any transfer pricing question: refer; see `india-transfer-pricing`.
- Virtual digital assets: see `india-crypto-tax`.
- Income of the year 2025-26 (assessment year 2026-27) or earlier: the 1961 Act applies; this Guide does not cover it.
- GST exports or refunds: see `india-gst` and `india-einvoice`. Multi-State registration or e-commerce operator registration: refer to a GST practitioner.
- Anything that depends on a figure this Guide says to check (wage ceilings, receipt deadlines, instrument rules): confirm on the official source first.

## Sources

- Income-tax Act, 2025 (30 of 2025), Gazette of India, 22 August 2025: https://egazette.gov.in/WriteReadData/2025/265620.pdf
- Finance Act, 2026 (4 of 2026), Gazette of India, 30 March 2026: https://egazette.gov.in/WriteReadData/2026/271439.pdf
- Income-tax Rules, 2026 (G.S.R. 198(E), 20 March 2026): https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf
- GST Council, 56th meeting press release (3 September 2025): https://gstcouncil.gov.in/sites/default/files/2025-09/press_release_press_information_bureau_0.pdf
- GST Council newsletter, December 2025 (tobacco rates from 1 February 2026): https://gstcouncil.gov.in/sites/default/files/2026-01/monthly_newsletter_december_2025_1_0.pdf
- GST Council, 57th meeting press release (8 October 2026, recommendations): https://gstcouncil.gov.in/sites/default/files/2026-10/press_release_0.pdf
- CBIC, "GST: An Update" (1 June 2019): https://cbic-gst.gov.in/pdf/01062019-GST-An-Update.pdf
- CGST Act section 10: https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter3/section10_v1.00.html
- CGST Act section 16: https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter5/section16_v1.00.html
- CGST Act section 22: https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter6/section22_v1.00.html
- Notification 10/2023-Central Tax (e-invoice threshold): https://gstcouncil.gov.in/sites/default/files/2024-05/10ct_eng.pdf
- Employees' Provident Funds Scheme, 2026 (G.S.R. 525(E)): https://egazette.gov.in/WriteReadData/2026/273957.pdf
- Social Security (Central) Rules, 2026 (G.S.R. 344(E)): https://egazette.gov.in/WriteReadData/2026/272366.pdf

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a Chartered Accountant (CA), tax consultant, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this Guide is maintained on the OpenAccountants site.

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
