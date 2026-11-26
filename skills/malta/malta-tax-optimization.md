---
name: malta-tax-optimization
description: "Use this skill when asked how a self-employed individual or small business owner in Malta can lawfully reduce or time income tax for basis year 2026 (year of assessment 2027). Covers the 10% part-time final tax and its EUR 12,000 cap, joint and parent rate tables, the sole trader or company choice (35% with shareholder refunds, the elective 15% final tax), deductions people miss (article 14 test, home for the elderly fees, the car cost cap), wear and tear timing, losses, provisional tax, VAT registration choice, pension tax credits, and the anti-avoidance rule in article 51. Trigger on reduce tax Malta, tax planning Malta, save tax Malta, pay less tax Malta, deductions I'm missing, part-time 10% Malta, incorporate in Malta, pension tax credit Malta. Links the computation skills instead of repeating them."
version: 2.1
jurisdiction: MT
tax_year: 2026
last_updated: 2026-11-26
category: tax-optimization
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax-optimization
type: decision
---

# Malta Tax Optimization v2.1

## Scope and who this is for
Tax year 2026: basis year 2026, year of assessment 2027. This skill lists the lawful levers and points to the skill that computes each one. It does not repeat the rate tables or the computations:

- individual rates, residence, part-time and rental final taxes: `malta-income-tax`
- provisional tax: `mt-estimated-tax`
- companies, refunds and the 15% election: `mt-corporate-tax`
- rent: `mt-rental-income`; property and share gains: `mt-capital-gains`, `selling-a-company-in-malta`
- related-party pricing: `malta-transfer-pricing`; moving to Malta: `moving-to-malta-tax-residence`
- VAT: `malta-vat-return`; social security: `malta-ssc`

## Ask the client first
1. Are you in full-time employment registered with Jobsplus, a pensioner, or a full-time student? Is the side work registered and for different customers?
2. Married or single in 2026? Children, their ages, custody, and nationality of each spouse?
3. Expected 2026 profit, and will profits be paid out or kept in the business?
4. What did your last self-assessment show (the provisional tax benchmark)?
5. Which assets will you buy, when, and what share is business use?
6. Turnover in 2025 and so far in 2026, and who are your customers (businesses or consumers)?

## The method, step by step
1. Fix the year (basis year 2026, YA 2027) and the person's status (single, married, parent; employee with side work, self-employed, pensioner).
2. Run the levers in order: part-time final tax, family rate tables, sole trader or company, deductions, wear and tear timing, losses, provisional tax, VAT choice, pension credits.
3. For each lever, compute both ways and keep the cheaper lawful one; the worked cases show the pattern.
4. Test every step against article 51 (anti-avoidance) and the article 14(1) and 26 deduction rules.
5. Diarise the calendar dates.

The levers, one by one:

### Income Splitting and Structuring
#### The part-time 10% final tax (article 90A, S.L. 123.39)

| Point | Rule | Source |
| --- | --- | --- |
| Who | A Malta resident in full-time employment registered with Jobsplus, a pensioner taxed in Malta, or a full-time student or apprentice. The spouse extension applies only when living together and no article 49A separate-return election is effective; if qualification depends on this extension, rule 3(2) excludes income from the specified spouse/family members and companies in which they are direct or indirect shareholders. | S.L. 123.39 rule 2; art. 90A(9) |
| Rate and cap | 10% final tax on part-time self-employed profit up to EUR 12,000 (EUR 10,000 where the part-time income is employment income under art. 4(1)(b)). Profit above the cap goes into the return at normal rates. | art. 90A(11); rule 3(2) |
| Conditions | Part-time work registered with Jobsplus; at most two part-time employees; proper books; work for someone other than the full-time employer; VAT registration unless not required or exempt. For the different-employer test, rule 6 treats companies controlled and beneficially owned more than 50% by the same shareholders as one employer, and specified controlled Government entities likewise. | rules 4 and 6 |
| Payment | By 30 April after the basis year (30 April 2027 for 2026 profit), with a statement of accounts | Cap. 372 art. 42(4)(a) |
| Risk | If tax on all the relevant part-time income is not paid by the prescribed date and an article 13(7) written enquiry notice is received, all the part-time income is taxed at normal rates. The Commissioner can refuse the regime where the work is the person's normal activity. | art. 90A(8), (10) |

Planning point: profit above EUR 12,000 is not lost, it is taxed at the person's normal marginal rate. Invoice dates alone do not establish the correct year of taxable income. Any proposed income-recognition change: Check this point with one of our partner accountants. Do not move income artificially (article 51). Part-time employment has separate registration/different-employer and weekly-hours tests, benefit/director/office exclusions and specific exceptions under rules 3, 5 and 6; do not apply the self-employment checklist to wages.

#### Rate tables and family status (article 56)

- Married couples are taxed jointly by default under article 49. Separate returns (article 49A) require the qualifying employment/trade/past-employment-pension or marital property-system conditions and an effective election; they are not an unrestricted retrospective choice. Article 50 separately computes specified active/past-employment-pension income, generally allocates other income to the higher active-income spouse, excludes benefit-only income and cannot operate with an effective article 49A election. Compare only lawful available methods; `malta-income-tax` has the tables.
- For basis year 2026 the married and parent tables with qualifying children give wider 0% bands (for example EUR 22,500 for a married couple with two or more qualifying children). Each table has distinct custody/maintenance, age and nationality/residence conditions. The married child tables require custody; do not substitute maintenance. See `malta-income-tax`; unresolved status or election eligibility: Check this point with one of our partner accountants.

#### Employing a family member

A salary to a spouse or child is deductible only if it meets the article 14(1) test (wholly and exclusively incurred in producing the income) and is not barred by article 26. Rule 4(1) of the Income Tax (Deductions) Rules, S.L. 123.07, limits the deduction for emoluments to emoluments "duly accounted for", under rule 4(4): correctly reported in the FS3 and annual reconciliation furnished within twelve months after the relevant FSS deadline. Rule 4(5) also requires a spouse receiving the salary to have paid social security contributions on the basic wage or salary. Keep evidence of real duties and commercial pay; employment registration and payroll: see `malta-payroll`. See `malta-payroll`.

#### Sole trader or company

| Factor | Sole trader | Private limited company |
| --- | --- | --- |
| Rate on profit | 0% to 35% on the individual tables | Ordinary 35%, subject to an applicable special/elective regime |
| Profit paid out as dividend | Not applicable | Refund eligibility depends on the company, profit/tax-account, distribution, shareholder and claim conditions. Do not present non-residence alone as a 5% result. Articles 12(1)(c)(iii) and 43(6) also affect resident shareholders. Check this point with one of our partner accountants; see `mt-corporate-tax` |
| Profit kept in the company | Taxed in the year earned | Ordinary company taxation subject to its regime; a retained-profit/dividend/refund comparison requires actual tax accounts and eligible claims. Check this point with one of our partner accountants |
| Elective 15% final tax | Not available | An eligible entity can elect under S.L. 123.217 from fiscal year preceding YA 2025; excludes specified dividends/other final-tax income. Election notice/form/deadline apply. Minimum five YAs; electing out also commits to ordinary tax for five YAs. Tax floor is ordinary liability less all shareholder refunds claimed/claimable, with art. 43(6) where applicable; final, no credit/set-off/refund, profits allocated to final tax account. Check this point with one of our partner accountants before choosing |
| Compliance | Return and provisional tax | Annual accounts, tax return and MBR annual return obligations require entity-specific preparation; a Companies Act audit exemption does not by itself settle income-tax audit requirements. Check this point with one of our partner accountants |

The refund route, the 15% election and the Malta-resident individual shareholder rules (article 43(6) and article 12(1)(c)(iii)) are worked through in `mt-corporate-tax`. Formation steps and costs: `malta-formation`. Accounts and audit: `malta-financial-statements`.

### Deductions Most People Miss
Business outgoings must pass article 14(1) (“wholly and exclusively incurred in the production of the income”) and article 26. Statutory personal reliefs such as article 14D care-home fees instead follow their own conditions; they do not require business use. Article 26 bars private expenses except where specifically allowed, capital spending except statutory allowances, recoverable expenses and voluntary/criminal payments. Mixed-use items are apportioned. Default to 0% business use until the client documents it.

| Deduction | Rule | Source |
| --- | --- | --- |
| Home office share | Business share of rent, utilities and internet for a room used for the business. A room also used privately fails the "wholly and exclusively" test on the private share. | Cap. 123 art. 14(1), 26 |
| Professional subscriptions, training, bank and payment fees, professional indemnity insurance, software subscriptions | Candidate business outgoings only: apply actual production purpose, revenue/capital nature and article 26. This category is not an automatic deduction | Cap. 123 art. 14(1), 26 |
| Bad debts | Deductible when proved to the Commissioner to have become bad in the year; a general provision is not sufficient; later recoveries of previously allowed amounts are taxable receipts | Cap. 123 art. 14(1)(d) |
| Scientific research | Qualifying basic/applied research or development for the use/benefit of the trade must be proved to the Commissioner. Capital spending is spread equally over expenditure year and five subsequent years except qualifying plant/machinery/premises allowances; no double deduction under (f)/(j) | Cap. 123 art. 14(1)(h) |
| Research, development and innovation at 175% | In the Act (article 14(1)(ha), Act III of 2026), marked applicable from year of assessment 2027, but it only starts on a date the Minister sets by Gazette notice, with rules to define the activities. Current commencement, eligible activities and interaction with ordinary research/allowances: Check this point with one of our partner accountants. No 175% deduction is supplied for use here. | Cap. 123 art. 14(1)(ha) |
| Fees for a private home for the elderly or disabled, or a respite centre | Individual paying for self or family: lower of the amount paid and EUR 4,500, from year of assessment 2027 (basis year 2026). The home must report the payment and claimant details to MTCA. The cap is the aggregate for each resident, not a separate cap for each family member paying. | Cap. 123 art. 14D |
| Car cost cap | For a car costing more than EUR 14,000, wear and tear is computed as if it cost EUR 14,000. The rule also affects initial allowances and balancing adjustments. Lease payments use EUR 14,000/listed price, with specific no-deduction, short-use and replacement rules. It excludes unsuitable private vehicles and vehicles mainly for public hire/carriage or ordinary-course driving instruction. Leasing or excluded vehicles: Check this point with one of our partner accountants. | S.L. 123.07 rule 3 |

Entertainment: record the actual business purpose and private element. No blanket deduction or prohibition follows from the label. Check this point with one of our partner accountants.

Social security Class 2 deductibility is unresolved here. Record the payment separately without asserting that this Guide has proved either deductibility or a statutory prohibition. Check this point with one of our partner accountants.

### Capital Allowances (Wear and Tear)
**Legislation:** Cap. 123 art. 14(1)(f); Deduction for Wear and Tear of Plant and Machinery Rules, S.L. 123.01.

#### Timing of purchases

Rule 7(a) of S.L. 123.01: an asset acquired on any day other than the first day of the year is treated "as if the asset had been used for the whole year". Rule 7(b): no allowance for a sale, scrapping or other listed event before the year's last day; a last-day event requires separate analysis. The rule applies where part-year production use is only owing to the acquisition/completion event; buying an idle asset is insufficient. Apply business use, ownership/burden, related-party/non-onerous acquisition, same-source profit and cumulative-cost conditions before claiming. Last-day disposal: Check this point with one of our partner accountants.

#### Minimum years (S.L. 123.01 Schedule, straight line on cost)

| Asset | Minimum years | Maximum annual rate |
| --- | --- | --- |
| Computers and electronic equipment; computer software | 4 | 25% |
| Motor vehicles; other machinery | 5 | 20% |
| Catering equipment; air-conditioners; medical equipment; communication and broadcasting equipment | 6 | about 16.67% |
| Furniture, fixtures, fittings and soft furnishings; lifts; other plant | 10 | 10% |
| Electrical and plumbing installations and sanitary fittings | 15 | about 6.67% |

Industrial buildings/structures: article 14(1)(f)/(j) includes a 2% annual ceiling excluding land and one-tenth initial allowance, subject to classification, source-profit limits and cumulative cost. No usable industrial-building computation is supplied: Check this point with one of our partner accountants.

Article 14(1)(j) also gives an initial deduction of one-fifth on plant and machinery first used in the year, but its proviso lets the Minister end it by order in the Gazette. Current operative availability: Check this point with one of our partner accountants. The examples do not claim it.

Allowances are only given where proper records of cost are kept (rule 5) and are cut to the business-use share (rule 11). Unused allowances carry forward against the same source when profits are insufficient; aggregate allowances cannot exceed relevant original cost (article 14(1)(f)(ii)–(iii)). S.L. 123.01 itself supplies no small-item immediate-write-off threshold; do not infer that a small purchase is automatically deductible.

#### Asset disposal

Disposals may require a balancing statement under article 24. The operative event, source continuity, proceeds, allowance history and statutory limits must be established; a simple sale-price-minus-written-down-value comparison is not a complete rule. Check this point with one of our partner accountants.

### Loss Utilization
**Legislation:** Cap. 123 art. 14(1)(g).

| Point | Rule |
| --- | --- |
| Same year | An allowable trading loss can offset other income/capital gains of the same year; compute it excluding wear-and-tear/initial allowances under article 14(1)(f)/(j), which have their own source restrictions |
| Carry-forward | What is left is carried forward against later years' total income in succession, with no time limit |
| Carry-back | None |
| Final tax income | No set-off against income allocated to the final tax account, nor loss from a source whose profits would go there. No excluded foreign loss that would escape tax if retained abroad; no other person's loss except statutory group/merger rules |
| Group relief | Companies only: see `mt-corporate-tax` |

Losses must come from genuine commercial activity. A manufactured loss is open to article 51.

### Timing Strategies
| Strategy | Detail | Source |
| --- | --- | --- |
| Asset purchase before year end | Possible full-year wear and tear only under rule 7 acquisition/use conditions above | S.L. 123.01 rule 7(a) |
| Provisional tax reduction | Submit the prescribed reduction statement by the relevant instalment date, using the official required liability estimate; later estimates cannot undo earlier defaults. Underestimation can carry additional tax; see `mt-estimated-tax` | S.L. 372.18 rule 10 |
| Pay provisional tax on time | Ordinary instalments 20%/30%/50% by 30 April/31 August/21 December 2026, rounded to nearest euro; increased benchmarks require cumulative catch-up and late-return revisions can affect earlier instalments. Late rule 14 charge is 0.6% per month/part for current periods, with caps/90%-reduction/appropriation conditions; see `mt-estimated-tax` | S.L. 372.18 rules 3–7, 10–14 |
| Part-time cap | Keep part-time records clean so profit up to EUR 12,000 stays at 10% | S.L. 123.39 rule 3(2) |
| Pension contributions before 31 December | For personal/employee credits, qualifying payments must be made in the relevant year; unused credit is not carried forward. Employer occupational credits have different rules | Cap. 123 art. 57(3) |

Detail on provisional tax: `mt-estimated-tax`.

### VAT Choice
| Strategy | Detail | Source |
| --- | --- | --- |
| Article 11 small enterprise | For an eligible Malta-established person: preceding-year domestic turnover not above EUR 35,000 at entry, and current-year qualification ceases when threshold exceeded. Turnover definition, related-person aggregation for non-individuals, article 10 waiting/exception rules, registration effective dates and residual article 12 obligations also apply. Qualifying domestic supplies exempt without credit. Compare actual customers/costs; see `malta-vat-return` | VAT Act, Cap. 406, art. 11 |
| Article 10 registration | Taxable underlying supplies use their applicable rate (ordinary 18%); exemptions, place-of-supply and reverse charges may change treatment. Input recovery requires entitlement, valid evidence/use and no blocking provision; customers' recovery also requires their entitlement. See `malta-vat-return` | Cap. 406 art. 10 |
| Capital goods | Long-term tangible fixed assets used as working tools/economic means qualify; small equipment/tools/office furniture below EUR 1,160 price or open-market value and packaging excluded. Repairs/maintenance/spares and renting/granting use excluded from capital-goods input tax. Reference periods of 5 years / 20 years for immovable rights; starts from the relevant deduction tax-period month, delayed until first-use tax period if unused. Actual use/disposal/cessation adjustment: Check this point with one of our partner accountants | S.L. 406.12 |

Registration rules, deadlines and the EUR 100,000 Union threshold are in `malta-vat-return`.

### Social Security
Class 2 liability is governed by the Social Security Act, Cap. 318, including age/status, self-occupied/self-employed definitions and exemptions/certificates. Net earnings and relevant prior-year basis differ by category; use the completed `malta-ssc` Guide for the 2026 bands and weekly amounts.

Planning points:

- Concurrent employed/self-occupied work requires the actual Class 1/Class 2 statutory test and any article 14 request/approval; do not automatically impose both. See `malta-ssc`.
- Ordinary bands include floors/ceilings, but low-income certificates, part-time elections and special categories alter the result. Check the actual category and conditions in `malta-ssc`.

### Investment and Retirement
| Relief | Rule | Source |
| --- | --- | --- |
| Personal retirement scheme tax credit | 25% up to EUR 750 under current S.L.123.163 rule8. Age at least 18, Malta domicile/residence, administrator certificate and annual statement, qualifying scheme and own/spouse-funded application and ordinary-residence declaration requirements apply (rules 4–7). Malta-resident married spouses may each claim under article 57(2). Subject to tax liability; no carry-forward or credit-generated refund | S.L.123.163 rules4–8; Cap.123 art.57 |
| Voluntary occupational pension scheme | 25% up to EUR 750, capped by current chargeable tax (joint couple tax can count). Qualifying employment income/registration/employer, scheme approval/benefit-age and non-HQPR conditions apply; employer contributions have distinct rules, not this employee credit | S.L.123.175 rules2–7 |
| Pension income exemption, age 61 and over | Basis year 2026: 100% of pension income under art. 4(1)(d), up to EUR 37,104. Basis year 2025: 80%, up to EUR 13,309 | Pensions (Tax Exemption) Rules, S.L. 123.204 rule 3 (L.N. 53 of 2026) |
| Pensioner rebate | From year of assessment 2027, a pensioner using the exemption and taxed at the married rates in art. 56(1)(a)(i) (the married table without qualifying children) gets a rebate of (chargeable income less 15,000) × 15%, capped at EUR 540. No refund and no carry-forward. | S.L. 123.204 rule 4 |

Article 57 permits prescribed amounts; the current S.L.123.163 rule8 resolves the former 15%/EUR 150 versus 25%/EUR 750 hold. Personal scheme: approved registration/withdrawal structure and normal benefit commencement at 61–70 (permanent disability/death exceptions); retain the required licence-holder certificate and reporting. An unresolved personal/occupational scheme, funding/status requirement, special-employment-scheme beneficiary or withdrawal treatment: Check this point with one of our partner accountants.

Malta Enterprise runs grant and tax-credit schemes for small businesses (for example Micro Invest). Their rates and caps change by call and are not in the Income Tax Act. No current scheme award/rate is asserted here. Check this point with one of our partner accountants.

### Red Lines
| Risk | Detail | Source |
| --- | --- | --- |
| Anti-avoidance | Malta has a general anti-avoidance rule. An artificial or fictitious scheme is disregarded. A scheme whose sole or main purpose is a tax advantage can be nullified by the Commissioner's order. Company ATAD and restructuring implications require separate analysis. Check this point with one of our partner accountants. | Cap. 123 art. 51 |
| Family employment | Must be real work, paid at a matching rate, run through FSS payroll | Cap. 123 art. 14(1); S.L. 123.07 rule 4 |
| Capital items expensed | Article26 permits statutory exceptions, not an automatic wear-and-tear entitlement for every capital item; classify the item and relief first | Cap. 123 art. 26 |
| Undeclared income | Ordinary 1.5% per month/part of endangered tax, maximum 60 times applicable monthly rate; rectified before enquiry and within 12 months of the due date: fully remitted; later before enquiry 0.1%, after enquiry before assessment 0.75%. FSS-paid amount excluded from endangered tax where Commissioner satisfied; remission conditions apply | Cap. 123 Schedule, items 5 to 9 |
| Late return (individual) | EUR 10 within 6 months, rising to EUR 500 after 60 months (Table A) | Cap. 123 Schedule, item 2 |

### Annual Tax Planning Calendar (basis year 2026)
| Month | Action |
| --- | --- |
| January | Receive FS3s for 2025 by 31 January; earlier termination generally requires copies within 7 days subject rule28. Review 2026 provisional tax benchmark. |
| April | **30 April 2026**: first provisional tax instalment (20%). Part-time 10% tax and 15% rental tax for 2025 due. |
| July | **31 July 2026**: individual return for basis year 2025, manual and electronic, and the tax due. MTCA moved this from 30 June ([MTCA notice, 3 June 2026](https://mtca.gov.mt/news-results-page/2026/06/03/tax-returns-submission-deadline)). |
| August | **31 August 2026**: second provisional tax instalment (30%). |
| September to November | Estimate 2026 profit. File the P.T. reduction form if tax will fall. Plan asset purchases. |
| December | **21 December 2026**: third provisional tax instalment (50%). Buy and start using planned assets. Pay pension contributions. |
| 2027 | 30 April 2027: part-time 10% tax on 2026 profit. 30 June 2027: return for basis year 2026. |

Sources: S.L. 372.16; S.L. 372.18; Cap. 372 art. 42(4); S.L. 372.14 rule 21; MTCA notice of 3 June 2026.

## Rates, bands and thresholds

| Item | Figure and conditions | Tax year | Source |
|---|---|---|---|
| Single table, art. 56(1) | 0% to EUR 12,000; 15% minus EUR 1,800 to EUR 16,000; 25% minus EUR 3,400 to EUR 60,000; 35% minus EUR 9,400 above | YA 2027 (Act III of 2026) | https://legislation.mt/eli/cap/123/eng/pdf |
| Married joint table, no qualifying child, art. 56(1) | 0% to EUR 15,000; 15% minus EUR 2,250 to EUR 23,000; 25% minus EUR 4,550 to EUR 60,000; 35% minus EUR 10,550 above | YA 2027 | same |
| Part-time final tax, art. 90A(11) | 10 cents per euro from YA 2023 (in place of 15 cents) | Current | same |
| Part-time cap, S.L. 123.39 rule 3(2) | EUR 12,000 of part-time trade or profession income (art. 4(1)(a)); EUR 10,000 of part-time employment income (art. 4(1)(b)); the excess goes in the return at normal rates | Current | https://legislation.mt/eli/sl/123.39/eng/pdf |
| Company ordinary rate, art. 56(6) | 35%, subject to applicable special/elective regime | YA 2027 | https://legislation.mt/eli/cap/123/eng/pdf |
| Elderly or disabled home fees, art. 14D | lower of the amount paid and EUR 4,500 | From YA 2027 | same |
| R&D deduction, art. 14(1)(ha) | 175%, only from a date the Minister sets by Gazette notice | Marked YA 2027 | same |
| Personal retirement scheme credit, art. 57(1) | 25% up to EUR 750 under current S.L. 123.163 rule 8, subject to qualification and article 57 tax-credit limits | Current | https://legislation.mt/eli/sl/123.163/eng/pdf |
| Late individual return, Schedule Table A | EUR 10 within 6 months, rising to EUR 500 after 60 months | Current | https://legislation.mt/eli/cap/123/eng/pdf |
| Omission from a return, Schedule | 1.5% a month of the endangered tax | Current | https://legislation.mt/eli/cap/123/eng/pdf |
| Car cost cap, S.L. 123.07 rule 3 | wear and tear on a car costing over EUR 14,000 computed as if it cost EUR 14,000 | Current | https://legislation.mt/eli/sl/123.7/eng/pdf |
| Wear and tear minimum years, S.L. 123.01 Schedule | computers 4, motor vehicles 5, catering 6, furniture 10, electrical and plumbing 15 | Current | https://legislation.mt/eli/sl/123.1/eng/pdf |
| Pension income exemption, S.L. 123.204 rule 3 | 100% up to EUR 37,104 (basis year 2026); 80% up to EUR 13,309 (basis year 2025) | YA 2027 / YA 2026 | https://legislation.mt/eli/sl/123.204/eng/pdf |
| Pensioner rebate, S.L. 123.204 rule 4 | (chargeable income less 15,000) x 15%, capped at EUR 540 | From YA 2027 | same |
| Provisional tax, S.L. 372.18 rule 4 | Twenty per cent by 30 April, a further thirty per cent by 31 August, a further fifty per cent by 21 December of the basis year (the rule writes the percentages in words) | Each basis year | https://legislation.mt/eli/sl/372.18/eng/pdf |
| Interest on late tax, Cap. 372 art. 44(2A) | 0.6% a month or part, capped at the tax, for tax due on/after31August2022; article44(2B) exceptions require review (specified FSS direction/additional tax/mutual-agreement procedure) | Current | https://legislation.mt/eli/cap/372/eng/pdf |
| Small enterprise VAT exemption, Cap. 406 art. 11 | domestic annual turnover not above the "domestic threshold" of EUR 35,000, subject to entry/current turnover, aggregation/registration and other eligibility conditions above | Current | https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4 |
| Capital goods for VAT, S.L. 406.12 | Capital-goods definition/exclusions above; EUR 1,160 is specific small-equipment exclusion. Reference periods 5/20 years with actual deduction/first-use starting rules | Current | https://legislation.mt/eli/sl/406.12/eng/pdf |

## Worked cases
All figures are invented. Rates are from the 2026 single table and the rules cited above.

#### Example 1: part-time 10% final tax against declaring the profit

A single person, a full-time employee registered with Jobsplus, has chargeable employment income of EUR 30,000 in 2026. She also has EUR 10,000 of part-time design profit from her own clients, registered with Jobsplus, with no employees. Every part-time condition is met.

- With the 10% final tax: EUR 10,000 × 10% = EUR 1,000, paid by 30 April 2027.
- If she declared the profit instead: tax on EUR 40,000 is 40,000 × 25% − 3,400 = EUR 6,600; tax on EUR 30,000 alone is EUR 4,100. The extra tax would be EUR 2,500.
- The 10% route saves EUR 1,500.

```oa-check
name: Part-time 10% final tax against progressive rates, single, basis year 2026
inputs:
  employment: 30000
  part_time_profit: 10000
  cap: 12000
steps:
  - final_tax: min(part_time_profit, cap) * 0.10
  - tax_with_profit: (employment + part_time_profit) * 0.25 - 3400
  - tax_without_profit: employment * 0.25 - 3400
  - extra_if_declared: tax_with_profit - tax_without_profit
  - saving: extra_if_declared - final_tax
expected:
  final_tax: 1000
  tax_with_profit: 6600
  tax_without_profit: 4100
  extra_if_declared: 2500
  saving: 1500
```

#### Example 2: a car bought in December, with the EUR 14,000 cap

A self-employed consultant, single, chargeable income well inside the 25% band, buys a car for EUR 30,000 on 15 December 2026 and starts using it at once. A mileage log shows80% business use. Assume an ordinary purchase at documented eligible cost, a vehicle within rule3(4), no related-party/non-onerous limitation or previous allowance, part-year use only because of acquisition, no disposal and sufficient same-source profits; no initial allowance claimed.

- The cost is capped at EUR 14,000 (S.L. 123.07 rule 3). Minimum life is 5 years.
- Allowance for 2026: 14,000 ÷ 5 × 80% = EUR 2,240. Rule 7(a) gives the full year even though the car was bought in December.
- Without the cap it would have been 30,000 ÷ 5 × 80% = EUR 4,800.
- Tax value of the 2026 allowance at 25%: EUR 560. Had she bought in January 2027, the first allowance would fall in basis year 2027.

```oa-check
name: Car wear and tear with the EUR 14,000 cap, 80% business use, bought December 2026
inputs:
  cost: 30000
  cap: 14000
  years: 5
  business_share: 0.80
  marginal_rate: 0.25
steps:
  - allowed_cost: min(cost, cap)
  - allowance_2026: allowed_cost / years * business_share
  - uncapped_allowance: cost / years * business_share
  - tax_value: allowance_2026 * marginal_rate
expected:
  allowed_cost: 14000
  allowance_2026: 2240
  uncapped_allowance: 4800
  tax_value: 560
```

## When to refuse or refer
- Refuse any step that moves income artificially or creates a manufactured loss (article 51).
- Refer the company route for a Malta-resident individual shareholder (articles 12(1)(c)(iii) and 43(6)) to `mt-corporate-tax` and a Malta accountant.
- Refer Malta Enterprise grant and tax-credit schemes: rates and caps change by call.
- R&D 175% commencement/eligibility, plant initial allowance, Class 2 deductibility, complex relief/election and scheme awards: Check this point with one of our partner accountants.
- This skill and its outputs do not constitute tax, legal or financial advice; outputs must be reviewed and signed off by a qualified professional before filing or acting.

## Sources
| Source | URL | Read on |
|---|---|---|
| Income Tax Act, Cap. 123: read for arts. 14, 14(1)(ha), 14D, 26, 51, 56(1) YA 2027 tables, 56(6), 57(1), 90A(11) and the Schedule (late return Table A, 1.5% omission) | https://legislation.mt/eli/cap/123/eng/pdf | 2026-11-26 |
| Income Tax Management Act, Cap. 372: read for arts. 42(4), 44(2A) and 48(4A) | https://legislation.mt/eli/cap/372/eng/pdf | 2026-11-26 |
| Part-Time Work Rules, S.L. 123.39: read for rules 2 to 4 (EUR 12,000 and EUR 10,000 caps) | https://legislation.mt/eli/sl/123.39/eng/pdf | 2026-11-26 |
| Deduction for Wear and Tear of Plant and Machinery Rules, S.L. 123.01: read for rules 5, 7, 11 and the Schedule | https://legislation.mt/eli/sl/123.1/eng/pdf | 2026-11-26 |
| Income Tax (Deductions) Rules, S.L. 123.07: read for rules 3 (EUR 14,000) and 4 | https://legislation.mt/eli/sl/123.7/eng/pdf | 2026-11-26 |
| Pensions (Tax Exemption) Rules, S.L. 123.204: read for rules 3 and 4 (EUR 37,104, EUR 13,309, EUR 540) | https://legislation.mt/eli/sl/123.204/eng/pdf | 2026-11-26 |
| Voluntary Occupational Pension Scheme Rules, S.L. 123.175: read for the tax credit rule | https://legislation.mt/eli/sl/123.175/eng/pdf | 2026-11-26 |
| Provisional Tax Rules, S.L. 372.18: read for rules 4, 5, 10 and 14 | https://legislation.mt/eli/sl/372.18/eng/pdf | 2026-11-26 |
| Income Tax (Statutory Dates) Rules, S.L. 372.16: read for rule 2(c)(ii) (30 June) | https://legislation.mt/eli/sl/372.16/eng/pdf | 2026-11-26 |
| S.L. 372.14: read for rule 21 (FS3 by 31 January) | https://legislation.mt/eli/sl/372.14/eng/pdf | 2026-11-26 |
| VAT Act, Cap. 406: read for arts. 10, 11 and 19 (18%) | https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4 | 2026-11-26 |
| VAT capital goods regulations, S.L. 406.12: read for the EUR 1,160 threshold and adjustment periods | https://legislation.mt/eli/sl/406.12/eng/pdf | 2026-11-26 |
| Final Income Tax Without Imputation Regulations, S.L. 123.217: read for regulation 3 | https://legislation.mt/eli/sl/123.217/eng/pdf | 2026-11-26 |
| MTCA notice of 3 June 2026: read for the 31 July 2026 deadline | https://mtca.gov.mt/news-results-page/2026/06/03/tax-returns-submission-deadline | 2026-11-26 |
| MTCA tax return booklet2026 (basis 2025): actual pension-credit table read; historical corroboration only, not the current-year authority | https://mtca.gov.mt/docs/default-source/documents/personal-tax/individual/tax-return-booklet-individuals/mtca-tax-booklet-2026-eng-17-03.pdf?sfvrsn=5ca02b73_1 | 2026-11-26 |
| Personal Retirement Scheme Rules, S.L.123.163: whole 4 pages, eligibility/application/certificates/scheme/25%/750 current law | https://legislation.mt/eli/sl/123.163/eng/pdf | 2026-11-26 |
| Income Tax Rate of Interest Rules, rule2, completed26 November read reused | https://legislation.mt/eli/sl/372.28/eng/pdf | 2026-11-26 |

Not yet confirmed: R&D 175% commencement/eligibility, plant initial allowance, Class 2 deductibility, specialist company/family elections, industrial buildings, complex VAT adjustments and current Malta Enterprise awards are non-usable referrals above. Check this point with one of our partner accountants. Completed26 November source reads from SSC/PT/bookkeeping/capital-gains audits reused after applicability checks; no claim of source-copy completeness here.
