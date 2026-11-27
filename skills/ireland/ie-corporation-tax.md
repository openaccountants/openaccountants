---
name: ie-corporation-tax
description: "Irish corporation tax for accounting periods ending in 2026: trading and passive income, company gains, ordinary plant allowances, trading losses, close-company investment surcharge, preliminary tax and CT1 filing on ROS. Includes conditional R&D instalment computations, a Pillar Two scope screen and explicit specialist holds. Preserves dated 2025 cases without changing their year. Trigger on Ireland corporation tax, CT1, preliminary CT, close-company surcharge and R&D credit Ireland."
version: 1.5
jurisdiction: IE
tax_year: 2026
last_updated: 2026-11-27
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# Irish corporation tax (CT1): 2026

## Who this applies to

Prepare the CT1 of a company whose Irish residence and ordinary trading status are established. Confirm the accounting period, income categories, ownership, earlier CT1s, losses and payments before computing. Do not infer a trade from incorporation or a bank description. The main period is 2026; dated 2025 examples retain their original year.

Collect signed accounts, trial balance, fixed-asset and allowance schedules, evidence for deductions, group structure, R&D records, dividend resolutions and preliminary-tax receipts. Missing facts mean a provisional working, not a filing-ready result. Residence, non-resident branches and Irish rental income of non-resident companies require [ie-foreign-tax-and-withholding](ie-foreign-tax-and-withholding.md); uncertain residence or branch attribution remains a hold. Check this point with one of our partner accountants.

## Rates, bands and thresholds

| Item and operative condition | 2026 treatment | Official source |
|---|---|---|
| Ordinary trading income, after confirming classification and excluding special regimes | 12.5%; TCA section 21 as amended by Finance Act 1999 section 71 | https://www.irishstatutebook.ie/eli/1999/act/2/section/71/enacted/en/html ; https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx |
| Ordinary non-trading rental/investment income and excepted-trade income | 25%; TCA section 21A; foreign-dividend exceptions and land classification require separate examination | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx |
| Ordinary company gains other than development land, with no exemption or special rate | CGT rate 33% before 7 October 2026; provisional 31% from that date; adjust gain so CT at 12.5% gives the CGT liability | https://www.revenue.ie/en/companies-and-charities/capital-gains-for-companies/index.aspx ; https://data.oireachtas.ie/akn/ie/debateRecord/dail/2026-10-06/debate/mul@/main.xml |
| Ordinary plant acquired in 2026, owned and wholly used for the trade, in use at period end | 12.5% of qualifying cost annually, subject to short-period adjustment and the total-cost cap; cars and special allowances excluded | https://www.irishstatutebook.ie/eli/2003/act/3/section/23/enacted/en/html ; https://www.irishstatutebook.ie/eli/1997/act/39/section/284/enacted/en/html |
| Small-company preliminary-tax limit | EUR 200,000 for a full year; use corresponding prior-period CT and reduce the relevant limit for a short current period | https://www.irishstatutebook.ie/eli/2012/act/9/schedule/4/enacted/en/html |
| Ordinary section 766C R&D expenditure credit, eligibility already established | 30% for periods commencing from 1 January 2024; 35% where the specified return date is on or after 23 September 2027 | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-29/29-02-03.pdf ; https://www.irishstatutebook.ie/eli/2025/act/18/section/35/enacted/en/html |

The accounting period cannot exceed 12 months. Split longer accounts into CT periods; time-apportion profits if a rate changes within a period ([Revenue](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx)).

**Provisional CGT rate.** The 6 October resolution substitutes 31% for 33% for disposals from 7 October 2026 and expressly has statutory effect. The [Bill status](https://www.oireachtas.ie/en/bills/bill/2026/98/) records Dáil completion on 25 November, not enactment; the [passed Dáil text, clause 41](https://data.oireachtas.ie/ie/oireachtas/bill/2026/98/eng/ver_b/b98b26d.pdf) retains the change. Under [1927 Act section 4](https://www.irishstatutebook.ie/eli/1927/act/7/section/4/enacted/en/html), provisional effect can end on rejection, dissolution, enactment or expiry of four months, with a Second Stage timing condition. Recheck the operative position before filing a post-change gain; do not assume this dated confirmation proves a future filing position. [Finance Act 2010 section 160](https://www.irishstatutebook.ie/eli/2010/act/5/section/160/enacted/en/html) brings CGT within that Act.

## The taxable base

Reconcile accounts profit to taxable profit; keep trading income, passive income and gains separate. Section 81 disallows private, capital and non-trade expenditure: a revenue expense must be wholly and exclusively for the trade. Add back accounting depreciation and claim only an evidenced tax allowance. For ordinary qualifying plant costing EUR 25,000, a full year's 12.5% allowance is EUR 3,125; do not exceed unrecovered cost. [Section 81](https://www.irishstatutebook.ie/eli/1997/act/39/section/81/enacted/en/html); [section 284](https://www.irishstatutebook.ie/eli/1997/act/39/section/284/enacted/en/html).

For an ordinary non-development-land chargeable gain, calculate the CGT liability, then divide by 12.5% to obtain the adjusted gain for the CT1 capital-gains section. Development-land gains stay outside CT profits and are reported in the CT1 Capital Gains (Development Land) section under CGT payment/filing rules. Do not apply the ordinary rate or capital-loss rules to a development-land transaction without a separate check. Check this point with one of our partner accountants. [Revenue: company gains](https://www.revenue.ie/en/companies-and-charities/capital-gains-for-companies/index.aspx).

**Ordinary trading losses.** A section 396A claim offsets a relevant trading loss against eligible income of the same period and, if claimed and the trade was carried on then, the preceding period of corresponding length; relieve the later period first and apportion a period that overlaps the carryback window. Section 396B value relief is available only for the excess over amounts that could have been relieved under a timely section 396A claim. It reduces relevant CT by the loss multiplied by the section 21 rate, subject to available relevant CT; it does not reduce section 239/241 liabilities or close-company surcharges. Both claims have a two-year deadline from the loss-period end. Carry unused losses forward against the same continuing trade under section 396(1), without using a loss twice. Foreign-dividend extensions, excepted trades, leasing restrictions, terminal losses, ownership changes and group/consortium relief are specialist holds. Check this point with one of our partner accountants. [Finance Act 2001 section 90](https://www.irishstatutebook.ie/eli/2001/act/7/section/90/enacted/en/html), [2006 Schedule 2, paragraph 1(h)](https://www.irishstatutebook.ie/eli/2006/act/6/schedule/2/enacted/en/html), [2012 Schedule 1, paragraphs 14–15](https://www.irishstatutebook.ie/eli/2012/act/9/schedule/1/enacted/en/html), [2003 section 59](https://www.irishstatutebook.ie/eli/2003/act/3/section/59/enacted/en/html), [section 396](https://www.irishstatutebook.ie/eli/1997/act/39/section/396/enacted/en/html).

**Close-company estate/investment surcharge.** First establish close-company and trading-company status; uncertain participator/control status is a hold. For an ordinary trading close company, section 434 determines estate/investment income after the relevant CT and a 7.5% trading-company reduction. Deduct the distributions attributable to the period; dividends must be declared for that period and paid/payable in the period or within 18 months after it. Apply section 440's 20% charge to the excess, with these conditions:

- The exemption limit is EUR 2,000 for a full year without associated companies. Reduce it for a short period and divide by one plus the relevant associated-company count; apply section 440(3)–(4), not just a year-end company count.
- Above that limit, surcharge cannot exceed 80% of the amount by which the excess exceeds the adjusted limit. Apply the section 440(2) accumulated-income limitation too.
- Collection is in the earliest period ending on or after 12 months after the original period end; if there is no such period, collection falls in the original period. It is not invariably the immediately following short period.

[Section 434](https://www.irishstatutebook.ie/eli/1997/act/39/section/434/enacted/en/html), [Finance Act 2001 section 91](https://www.irishstatutebook.ie/eli/2001/act/7/section/91/enacted/en/html), [section 440](https://www.irishstatutebook.ie/eli/1997/act/39/section/440/enacted/en/html), [Finance Act 2013 section 33](https://www.irishstatutebook.ie/eli/2013/act/8/section/33/enacted/en/html). Service-company surcharge, inter-close-company elections, exempt dividends, legal distribution restrictions and participator loans/benefits require a separate computation. Check this point with one of our partner accountants.

**R&D mechanics, not an eligibility determination.** Confirm qualifying activities, attributable expenditure and the period before using the rate table. Do not assume that software, staff, agency work, subcontracting, third-level research, grants or expenditure deductible abroad qualifies. These eligibility and allocation questions, and section 766D building claims with a different instalment rule, are holds. Check this point with one of our partner accountants.

For the original example of a period ending 30 November 2026 and commencing on or after 1 January 2024, the specified return date falls in August 2027, so the rate remains 30%.

For an established section 766C claim, the first instalment is the greater of half the credit and the lower of the credit and the applicable first-instalment limit: EUR 75,000 for periods commencing from 1 January 2025 until the later rule applies; EUR 87,500 where the specified return date is on or after 23 September 2027. The second instalment is three fifths of the balance; the third is the remainder. Elect for each instalment to be paid or treated as an overpayment for offset. An elected first instalment actually offset against that period's CT reduces CT for preliminary-tax purposes for that period and the next. Do not automatically subtract the whole credit from the tax charge. Specify the instalments on the relevant CT1s; non-standard succeeding periods need the statutory timing check. Claim within 12 months of the expenditure-period end; notify Revenue at least 90 days before the claim unless the company claimed under section 766C or 766 in any of the three immediately preceding periods. [Finance Act 2022 section 27](https://www.irishstatutebook.ie/eli/2022/act/44/section/27/enacted/en/html), [2023 section 34](https://www.irishstatutebook.ie/eli/2023/act/39/section/34/enacted/en/html), [2024 section 41](https://www.irishstatutebook.ie/eli/2024/act/43/section/41/enacted/en/html), [2025 section 35](https://www.irishstatutebook.ie/eli/2025/act/18/section/35/enacted/en/html).

### Boundary and exception table

Each hold below is non-usable for deciding tax or filing until resolved. Check this point with one of our partner accountants.

| Original topic | Retained destination and boundary |
|---|---|
| Trading classification; general expense categories | Require evidence under section 81. Specific entertainment, doubtful-debt provisions, pensions, director pay, fines, CT/interest deductions, travel/RCT, pre-trading expenditure and charitable donations: hold the specific deduction or relief. |
| Capital allowances beyond ordinary plant | Cars/CO2/cost caps; buildings; accelerated energy-efficient, gas/electric, refuelling, creche/gym allowances; intangible amortisation/elections, interest and balancing-allowance caps; part-use and disposal adjustments: hold. |
| Losses and groups | Terminal loss, ownership/trade change, excepted/foreign trades, leasing, management expenses, charges, Case V allowances, group/consortium membership, cross-border final losses, time apportionment and consent: hold these outcomes. |
| Interest limitation and anti-hybrids | Hold the de minimis, EBITDA, standalone/individual ownership, interest-group allocation, group/equity ratios, legacy debt and carryforward computations; do not infer exemption from ownership or gross interest alone. |
| Start-up relief | Hold qualification, trade/incorporation dates, exclusions, full/marginal bands, employer/Class S PRSI caps and carryforward. A new company or a low balance after R&D does not establish relief. |
| KDB | Hold asset eligibility, effective rate, nexus/uplift, tracking, election and expiry. No old effective rate is usable for 2026. |
| Special regimes | Section 110/PPN/property restrictions, banks/IFSC, life assurance, REIT/IREF, funds/ICAV, tonnage, petroleum/mining and Islamic finance: hold. |
| Structuring and compliance | Functional currency, transfer pricing/SME documentation, CbCR, debt push-down, IP/residence migration, GAAR/PPT, mandatory/protective disclosure, audits, interventions and penalties for incorrect returns: hold. |
| Legislation proposed for later periods | The former preliminary-tax limit/top-up, start-up extension, KDB extension and R&D instalment proposals are not usable rules here. Confirm enactment, final text and commencement for the period concerned. |

## Deadlines and filing

Use ROS to file the CT1 and applicable Form 46G (Company), pay preliminary CT and pay the balance. For an ordinary company not winding up, section 959A gives nine months after period end, capped at the 23rd of that month where both return and required payments meet the electronic conditions. A period ending 31 December 2026 is due 23 September 2027; the calendar 2025 CT1 was due 23 September 2026. A period ending 5 December is due 5 September, not automatically the 23rd. Winding-up deadlines and non-electronic cases require a separate check. [Finance Act 2012 Schedule 4, section 959A](https://www.irishstatutebook.ie/eli/2012/act/9/schedule/4/enacted/en/html); [payment and filing](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/payment-and-filing.aspx).

**Preliminary CT for 2026.** Use the statutory corresponding CT calculation: prior-period CT × days in the current period ÷ days in the prior period. The small-company test is corresponding prior CT not exceeding the relevant limit, EUR 200,000 reduced proportionately for a short current period. Exclude the late-filing surcharge and section 239 income tax for classification; include section 440/441 close-company surcharges. A payment calculation also needs section 239/241 liabilities where relevant. [Section 959AM, Schedule 4](https://www.irishstatutebook.ie/eli/2012/act/9/schedule/4/enacted/en/html); [TDM 41A-07-02, sections 3–4](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41a/41A-07-02.pdf).

| Situation | Required amount and ROS timing for an ordinary period | Source |
|---|---|---|
| Small company | At least the lower of 90% of current tax and corresponding prior CT plus corresponding prior section 239/241 income tax. Normally due 31 days before period end, subject to the statutory day-21/day-23 electronic adjustment; 23 November for a calendar 2026 period. | https://www.irishstatutebook.ie/eli/2012/act/9/schedule/4/enacted/en/html |
| Large company with two-instalment period | First: lower of 45% current tax and 50% corresponding prior tax; first-period entrant uses 45% current tax. Due within six months from start, with the statutory electronic adjustment. Final instalment brings total to 90% current tax, due 31 days before end with that adjustment. Calendar 2026 dates: 23 June and 23 November. | https://www.irishstatutebook.ie/eli/2012/act/9/schedule/4/enacted/en/html |
| Short large-company period | Section 959AM(2) switches to one instalment if the final instalment would fall on/before the first. Pay at least 90% under section 959AR. Do not use “exactly seven months” as a universal boundary. A period shorter than one month and one day uses the period-end rule in section 959AR(1)(b). | https://www.irishstatutebook.ie/eli/2012/act/9/schedule/4/enacted/en/html |
| First period on entering the CT charge | Section 959AN(4): preliminary CT is nil if tax does not exceed the relevant limit, including equality; the short-period limit still applies. The tax definition includes section 239 income tax, excluding the late-filing surcharge. Pay the final balance by the return date. | https://www.irishstatutebook.ie/eli/2012/act/9/schedule/4/enacted/en/html ; https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41a/41A-07-02.pdf |

The day-23 electronic adjustment is conditional: use the statutory date rule, not “always the earlier of day 23 and 31 days before year end” for an unusual month-end. Underpayment can accelerate the final liability's due date. Gains/financial-asset exceptions, leap-year comparisons, first-period mismatches and notional group allocations require a separate computation. Check this point with one of our partner accountants.

**iXBRL.** Large Corporates Division, High Wealth and Financial Services Division and section 110 cases require iXBRL. For ordinary other CT filers, the small exclusion requires all three: total assets without liabilities deducted below EUR 4.4 million, turnover below EUR 8.8 million and average employees 50 or fewer. Other exceptions and the required tags/submission timing need the applicable iXBRL manual. Do not assume every company files iXBRL or that two tests suffice. [Revenue: who must submit](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/submitting-financial-statements/who-submit.aspx).

## Penalties and interest

Late or insufficient payment carries daily interest of 0.0219%, computed on the underpaid amount and days late; a preliminary-tax failure can change which liability is overdue. [Revenue payment and filing](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/payment-and-filing.aspx).

A late return has a section 1084 surcharge: 5% capped at EUR 12,695 if delivered before expiry of two months from the specified return date; otherwise 10% capped at EUR 63,485. It can apply despite timely payment. Section 1085 separately restricts excess capital allowances, the specified loss-relief claims and group claims/surrenders: ordinarily 25% with maximum EUR 31,740 for a return before expiry of two months, otherwise 50% with maximum EUR 158,715. The group-claim restriction is measured against reduced profits, not simply a percentage of tax. Do not infer that R&D credits are one of these listed relief restrictions. [Sections 1084](https://www.irishstatutebook.ie/eli/1997/act/39/section/1084/enacted/en/html) and [1085](https://www.irishstatutebook.ie/eli/1997/act/39/section/1085/enacted/en/html); [TDM 47-06-08](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-47/47-06-08.pdf) and [47-06-04](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-47/47-06-04.pdf).

**Exact-boundary hold:** the original case of a calendar 2025 CT1 filed on 23 November 2026 must not be answered as “5% surcharge but 50% relief restriction” from inconsistent summary wording. Both statutory provisions use “before the expiry of 2 months”; resolve the exact expiry/application before a final filing calculation. Check this point with one of our partner accountants. Incorrect/incomplete returns, penalties versus surcharge, interest on surcharge, assessments and the enquiry time limit are separate holds; no blanket four-year protection is offered. Check this point with one of our partner accountants.

## Cross-border points

**Pillar Two scope screen.** Section 111C tests consolidated revenue including excluded entities against EUR 750 million for at least two of four preceding fiscal years; adjust the revenue threshold pro rata for fiscal years other than 12 months. Passing that screen does not establish that every entity is taxable: excluded-entity rules, elections, mergers and section 111AL matter. Hold entity classification, the 15% minimum/top-up computation, IIR/UTPR/domestic tax, safe harbours, Side-by-Side changes, registration and TIR/GIR/payment deadlines. Check this point with one of our partner accountants. [Finance (No. 2) Act 2023 section 94, sections 111A/111C](https://www.irishstatutebook.ie/eli/2023/act/39/section/94/enacted/en/html).

Foreign dividends and participation exemption (including the original 2025 versus 2026 look-back distinction), foreign-tax credits/pooling, withholding, branch attribution, foreign rental income and final foreign losses are held for [ie-foreign-tax-and-withholding](ie-foreign-tax-and-withholding.md). Transfer pricing and associated-party/SME documentation route to [ie-transfer-pricing](ie-transfer-pricing.md). Migration, residence and exit tax route to [ie-cross-border](ie-cross-border.md). A companion link is not proof of an outcome. Check this point with one of our partner accountants.

## Worked examples

### 1. Hill Ltd: calendar 2026

Original inputs: trading profit EUR 400,000; net rent EUR 40,000; 2025 CT EUR 48,000; dividends EUR 20,000 within 18 months. Assume full-year periods, established ordinary trading close-company status, no associates, no other adjustments/credits/section 239 tax, dividends attributable to this period, sufficient accumulated income, and a calendar 2027 following period.

Trading CT EUR 50,000 plus rental CT EUR 10,000 gives EUR 60,000. Preliminary CT is min(EUR 48,000, EUR 54,000) = EUR 48,000 by 23 November 2026; balance EUR 12,000 by 23 September 2027. Distributable rent is EUR 30,000 × 92.5% = EUR 27,750; after dividends excess is EUR 7,750. Ordinary surcharge EUR 1,550 is below marginal cap EUR 4,600, and is collected with calendar 2027 CT. Dependencies: rate table, sections 434/440 and preliminary-tax rules above.

```oa-check
name: Hill Ltd calendar 2026
inputs:
  trading: 400000
  rent: 40000
  prior_ct: 48000
  dividends: 20000
steps:
  - ct_trading: trading * 0.125
  - ct_rent: rent * 0.25
  - ct_total: ct_trading + ct_rent
  - prelim_minimum: min(prior_ct, ct_total * 0.90)
  - balance_with_ct1: ct_total - prelim_minimum
  - distributable: (rent - ct_rent) * 0.925
  - excess: distributable - dividends
  - marginal_cap: max(0, excess - 2000) * 0.8
  - surcharge: min(excess * 0.20, marginal_cap)
expected:
  ct_total: 60000
  prelim_minimum: 48000
  balance_with_ct1: 12000
  distributable: 27750
  excess: 7750
  marginal_cap: 4600
  surcharge: 1550
```

### 2. Atlas Ltd: gain on 15 November 2026

Original inputs: calendar 2026, trading loss EUR 100,000, no trading income in 2025/2026, ordinary non-development-land building gain EUR 150,000. Assume no eligible foreign-dividend income, no earlier relief/group surrender, no other adjustments, a valid timely section 396B claim and the provisional rate still operative.

At 31%, tax on the gain is EUR 46,500; adjusted gain EUR 372,000. Value relief is EUR 12,500, leaving CT EUR 34,000. The original comparison disposal date, 6 October 2026, gives 33%, tax EUR 49,500, adjusted gain EUR 396,000 and CT EUR 37,000; difference EUR 3,000. The rate-status recheck above is required; these are conditional computations, not evidence of a later enactment.

```oa-check
name: Atlas Ltd original 2026 disposal dates
inputs:
  gain: 150000
  loss: 100000
  cgt_rate_new: 0.31
  cgt_rate_old: 0.33
  ct_rate: 0.125
steps:
  - cgt_new: gain * cgt_rate_new
  - adjusted_gain_new: cgt_new / ct_rate
  - ct_on_gain_new: adjusted_gain_new * ct_rate
  - value_relief: loss * ct_rate
  - ct_payable_new: ct_on_gain_new - value_relief
  - cgt_old: gain * cgt_rate_old
  - adjusted_gain_old: cgt_old / ct_rate
  - ct_payable_old: cgt_old - value_relief
  - difference: ct_payable_old - ct_payable_new
expected:
  cgt_new: 46500
  adjusted_gain_new: 372000
  ct_on_gain_new: 46500
  value_relief: 12500
  ct_payable_new: 34000
  adjusted_gain_old: 396000
  ct_payable_old: 37000
  difference: 3000
```

### Other original cases and their destinations

- **Coast Ltd, calendar 2026:** prior CT EUR 900,000, current CT EUR 1,200,000, full-year periods/no adjustments. First instalment min(EUR 450,000, EUR 540,000) = EUR 450,000 by 23 June; second EUR 630,000 by 23 November reaches EUR 1,080,000; balance EUR 120,000 by 23 September 2027.
- **Lab Ltd:** assumed confirmed section 766C qualifying expenditure EUR 400,000 in each calendar year. 2026 at 35% gives EUR 140,000, instalments EUR 87,500 / EUR 31,500 / EUR 21,000; 2025 at 30% gives EUR 120,000, instalments EUR 75,000 / EUR 27,000 / EUR 18,000. Claims by 31 December 2027 and 31 December 2026 respectively, subject to notification; eligibility remains the hold above.
- **Brook Ltd, calendar 2025:** CT EUR 150,000, due 23 September 2026. Assuming that is the surcharge base, filing 20 October 2026 gives surcharge EUR 7,500; filing 15 December gives EUR 15,000. Any section 1085 restriction needs the actual relief/profit figures. The exact 23 November case remains held above.
- **Historical loss/gain case:** loss EUR 100,000, gain EUR 100,000, stated tax on the gain EUR 33,000. If that supplied gain-tax input and section 396B eligibility are confirmed for its original period, relief EUR 12,500 leaves EUR 20,500. Do not treat the supplied EUR 33,000 as the rate for a November 2026 gain.
- **2026 Pillar Two screen:** original consolidated revenues EUR 700m (2022), EUR 760m (2023), EUR 720m (2024), EUR 800m (2025), assuming full-year figures; two years reach EUR 750m. Entity exclusions and all tax/filing outcomes remain held. Check this point with one of our partner accountants.
- **Start-up PRSI case, calendar 2025:** preserve CT EUR 25,000, employer PRSI EUR 9,000, directors' Class S EUR 500 and EUR 1,200. The former EUR 10,500 relief / EUR 14,500 balance is non-usable until qualifying trade, PRSI allocation/caps and section 486C eligibility are confirmed. Check this point with one of our partner accountants.
- **TechCo Ltd, 1 January–31 December 2025:** preserve accounts trading profit EUR 500,000, depreciation EUR 20,000, plant allowances supplied EUR 25,000, R&D expenditure EUR 100,000, no passive income and prior CT EUR 0/first trade year. Conditional arithmetic gives taxable profit EUR 495,000 and CT before credits/relief EUR 61,875. Hold the former automatic zero-tax/start-up outcome, R&D election, allowance entitlement, preliminary-tax and iXBRL conclusions; the original ROS date is 23 September 2026. Check this point with one of our partner accountants.
- **GlobalCo Ireland Ltd, calendar 2025:** preserve US ownership, EUR 1.2bn consolidated revenue in each of 2023/2024, trading profit EUR 40m, the ambiguously described “foreign branch dividend” EUR 3m, 80 employees, payroll EUR 8m and assets EUR 15m. Preserve the original assumed foreign withholding EUR 450,000 (15%) as an unverified input. Hold income classification/exemption/credit, covered taxes, GloBE income, substance exclusion and the former top-up result; none is a usable tax computation. Check this point with one of our partner accountants.
- **PropTradeCo Ltd, FY 2025:** preserve trading profit EUR 200,000, net rent EUR 80,000, close-company status and no rent distribution by the 18-month mark. Conditional ordinary CT is EUR 45,000. If it is a trading company with no associates/other adjustments and no accumulated-income cap restriction, estate/investment income after CT and reduction is EUR 55,500, giving EUR 11,100 surcharge (below marginal cap), not the old EUR 12,000. Without those facts, hold the surcharge. Check this point with one of our partner accountants.
- **Other original illustrations:** a EUR 150,000 ordinary gain gives adjusted gain EUR 372,000 at 31% or EUR 396,000 at 33%, as in Atlas; ordinary EUR 25,000 plant gives EUR 3,125 as above. A non-trading close company's original EUR 50,000 Irish-dividend case remains held for dividend classification/exclusions and distributions; do not infer EUR 10,000 surcharge solely from the receipt. Check this point with one of our partner accountants.

## Ask the client first

Confirm period dates and residence; each income/gain category and disposal date; original accounts and adjustments; prior CT and period length; preliminary payments; ownership, associates, service-company and group links; dividends and accumulated income; losses and earlier claims; R&D evidence and notification; interest/IP/foreign flows; filing delays; iXBRL tests and any winding up. Use the existing records before asking for missing facts. No merchant, industry, company-size or “conservative” default establishes an exemption.

## Sources

| Official authority and passage actually read | URL | Read date |
|---|---|---|
| Finance Act 1999 section 71, section 21 rate; Revenue basis/period rules | https://www.irishstatutebook.ie/eli/1999/act/2/section/71/enacted/en/html ; https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx | 2026-11-27 |
| Finance Act 2000 section 75, section 21A higher rate and land exclusions | https://www.irishstatutebook.ie/eli/2000/act/3/section/75/enacted/en/html | 2026-11-27 |
| Company gains, gross-up/reporting; Dáil resolution 3 operative paragraphs | https://www.revenue.ie/en/companies-and-charities/capital-gains-for-companies/index.aspx ; https://data.oireachtas.ie/akn/ie/debateRecord/dail/2026-10-06/debate/mul@/main.xml | 2026-11-27 |
| Bill status and passed Dáil clause 41, not an Act | https://www.oireachtas.ie/en/bills/bill/2026/98/ ; https://data.oireachtas.ie/ie/oireachtas/bill/2026/98/eng/ver_b/b98b26d.pdf | 2026-11-27 |
| Provisional Collection Act section 4; 2010 section 160 definition | https://www.irishstatutebook.ie/eli/1927/act/7/section/4/enacted/en/html ; https://www.irishstatutebook.ie/eli/2010/act/5/section/160/enacted/en/html | 2026-11-27 |
| TCA sections 81, 284; Finance Act 2003 section 23 operative plant rate; Revenue ordinary plant example | https://www.irishstatutebook.ie/eli/1997/act/39/section/81/enacted/en/html ; https://www.irishstatutebook.ie/eli/1997/act/39/section/284/enacted/en/html ; https://www.irishstatutebook.ie/eli/2003/act/3/section/23/enacted/en/html ; https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/capital-allowances-and-deductions.aspx | 2026-11-27 |
| Loss law: section 396; 2001 section 90; 2002 section 54; 2003 section 59; 2006 Schedule 2 paragraph 1(h); 2012 Schedule 1 paragraphs 14–15 | https://www.irishstatutebook.ie/eli/1997/act/39/section/396/enacted/en/html ; https://www.irishstatutebook.ie/eli/2001/act/7/section/90/enacted/en/html ; https://www.irishstatutebook.ie/eli/2002/act/5/section/54/enacted/en/html ; https://www.irishstatutebook.ie/eli/2003/act/3/section/59/enacted/en/html ; https://www.irishstatutebook.ie/eli/2006/act/6/schedule/2/enacted/en/html ; https://www.irishstatutebook.ie/eli/2012/act/9/schedule/1/enacted/en/html | 2026-11-27 |
| Sections 434/440, 2001 section 91 and 2013 section 33: distributions, reduction, cap and collection | https://www.irishstatutebook.ie/eli/1997/act/39/section/434/enacted/en/html ; https://www.irishstatutebook.ie/eli/1997/act/39/section/440/enacted/en/html ; https://www.irishstatutebook.ie/eli/2001/act/7/section/91/enacted/en/html ; https://www.irishstatutebook.ie/eli/2013/act/8/section/33/enacted/en/html | 2026-11-27 |
| R&D section 766C: 2022 section 27; 2023 section 34 notification/rate; 2024 section 41; 2025 section 35 commencement/elections | https://www.irishstatutebook.ie/eli/2022/act/44/section/27/enacted/en/html ; https://www.irishstatutebook.ie/eli/2023/act/39/section/34/enacted/en/html ; https://www.irishstatutebook.ie/eli/2024/act/43/section/41/enacted/en/html ; https://www.irishstatutebook.ie/eli/2025/act/18/section/35/enacted/en/html | 2026-11-27 |
| TDM 29-02-03, sections 2–2.3: rates, instalments and offset, eligibility warning | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-29/29-02-03.pdf | 2026-11-27 |
| Schedule 4: sections 959A, 959AM–AN, 959AR–AT; TDM 41A-07-02 sections 2–5 | https://www.irishstatutebook.ie/eli/2012/act/9/schedule/4/enacted/en/html ; https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41a/41A-07-02.pdf | 2026-11-27 |
| Revenue ROS CT1/46G, interest and iXBRL exclusion/other-exception warning | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/payment-and-filing.aspx ; https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/submitting-financial-statements/who-submit.aspx | 2026-11-27 |
| Sections 1084/1085: timing language; manuals' euro caps/restrictions and incomplete-return conditions | https://www.irishstatutebook.ie/eli/1997/act/39/section/1084/enacted/en/html ; https://www.irishstatutebook.ie/eli/1997/act/39/section/1085/enacted/en/html ; https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-47/47-06-08.pdf ; https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-47/47-06-04.pdf | 2026-11-27 |
| Finance (No. 2) Act 2023 section 94: section 111A threshold and 111C screen/exclusions | https://www.irishstatutebook.ie/eli/2023/act/39/section/94/enacted/en/html | 2026-11-27 |

Not yet confirmed: all explicitly named specialist and exact-boundary holds above are non-usable tax outcomes. Check this point with one of our partner accountants. This includes future provisional-rate status; no hold is a permission to guess or file.
