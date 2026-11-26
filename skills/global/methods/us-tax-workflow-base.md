---
name: us-tax-workflow-base
description: "US federal 2026 individual and sole-proprietor preparation workflow with separate 2025 comparisons: establish the taxpayer and entity, reconcile records, test ordinary deductions and Schedule SE, preserve missing facts, route specialist issues and hand off the return for professional review."
version: 0.4
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-26
type: filing-howto
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# US federal individual and self-employed return workflow

Use this method for 2026 federal preparation; every 2025 comparison is labelled separately. Establish the facts before calculating, then use the appropriate companion Guide. A route to another Guide does not certify its contents or resolve a hold in it. This method does not approve a taxpayer's return.

Historical method credit: James Wallach. That earlier credit is not professional approval of this revision.

## Scope and who this is for

This workflow covers an individual citizen or full-year resident with a sole-proprietor trade or business reported on Schedule C. A domestic single-member LLC generally uses its owner's Schedule C, E or F, as appropriate, unless it elected corporate treatment; only the Schedule C activity is handled here ([Schedule C instructions, opening](https://www.irs.gov/instructions/i1040sc)). Residence, special entity elections, rental/farm activity and employer payroll require their own review.

Load `us-sole-prop-bookkeeping`, `us-schedule-c-and-se-computation` and `us-federal-return-assembly` as the task requires. The assembly route includes retirement, health insurance, QBI, Schedules 1/1-A/2/3, credits and payment reconciliation. Use `us-quarterly-estimated-tax` for estimates, `us-1099-k-and-payment-processors` for processor reconciliation, `us-secure-2-and-retirement-updates` for plan issues, `us-tax-residency` for residence and `us-irs-collections-and-controversy` for notices. These are navigation instructions.

## Ask the client first

Read the whole existing taxpayer record, prior returns/elections, source documents and latest answers before asking. Record each fact's source and year. Bank-account names and merchant descriptions are clues, not confirmed entity, filing status, deductibility or payment facts.

- Establish actual year, citizenship/residence, marital status and changes/death/remarriage, dependents, state of residence/business, entity ownership and elections, business activity and profit history.
- Reconcile all bank/card/processor/cash/invoice records, non-cash items and the actual accounting method. Count every transaction once or record its exclusion and evidence; preserve unreadable rows and separate years/currencies. Obtain documented conversion where needed.
- Collect each vehicle's ownership/lease, first business year/method, depreciation/election history, dated business/total miles and evidence; home-office use, area, duration, other locations, actual expenses and carryovers; asset invoices, business use, service dates, book policy and applicable financial statements.
- Identify everyone paid, work/control facts, payment method, identity/TIN documentation and exceptions; collect wages, prior-year AGI/tax, withholding/credits, estimated-payment dates/year, health/retirement records and all referral items below.
- Ask only for remaining gaps, grouped by topic and consequence. Keep incomplete answers open; do not invent a one-round-trip limit, consent, election, zero basis, zero business use, missing payment or higher-tax filing status.

## The method, step by step

1. **Set the year and status.** Ordinary marital status is determined at year-end. A married person's eligibility for a joint/separate or considered-unmarried status must be established; do not default to Single or infer joint consent from a lower calculation ([Pub. 501, Filing Status](https://www.irs.gov/publications/p501)). Death, divorce, remarriage and unusual status cases are referred below.
2. **Confirm residence and entity before applying Schedule C.** For a spouse-owned unincorporated trade/business, qualified joint venture (QJV) requires only the married couple as members, a joint return, both materially participating and both electing. A state-law entity such as an LLC does not qualify for this election. Allocate items according to each spouse's interest; each files a separate Schedule C and, **if otherwise required**, Schedule SE ([IRS QJV, definition and reporting](https://www.irs.gov/businesses/small-businesses-self-employed/election-for-married-couples-unincorporated-businesses)). Community-property treatment is a separate referred question.
3. **Establish business status.** The primary purpose must be income/profit and involvement continuous and regular ([Schedule C instructions](https://www.irs.gov/instructions/i1040sc)). **AUDIT FLASH POINT:** the section 183 presumption requires gross income exceeding deductions in at least 3 of 5 consecutive years ending with this year; an activity consisting mainly of breeding/training/showing/racing horses uses 2 of 7. It is rebuttable; failing it does not itself establish a hobby ([26 USC 183(d)](https://uscode.house.gov/us/usc/t26/s183/)). Hobby income/deduction outcomes are referred.
4. **Reconcile receipts and costs.** Trace each information return to the correct activity, with documented duplicate/transfer/loan/capital/recovery treatment. Neither bank deposits nor an information form alone determines taxable receipts. Retain unresolved alternatives rather than silently excluding refunds or treating every unexplained deposit as income. Ordinary and necessary trade/business costs are the starting deduction rule, subject to substantiation, capitalization and specific restrictions ([26 USC 162(a)](https://uscode.house.gov/us/usc/t26/s162/)).
5. **Substantiate travel, gifts and listed property.** Section 274(d) requires adequate records **or sufficient corroborating evidence** of amount, time/place or gift description, business purpose and relationship; qualified nonpersonal-use vehicles are excepted. Missing an original receipt is not automatically the absence of lawful evidence ([26 USC 274(d)](https://uscode.house.gov/us/usc/t26/s274/)). Detailed receipt/per-diem/casualty exceptions are referred.
6. **Apply only the supported ordinary rules below.** Keep personal/commuting and exceptional expenses unresolved until their actual treatment is established. Work out payee classification and information-return duties separately from deductibility. Refer worker-status disputes and backup-withholding cases; do not fabricate a TIN or assume an app name establishes settlement treatment.
7. **Compute the ordinary Schedule SE case, then assemble.** Combine the person's covered businesses, including eligible losses, on one Schedule SE; spouses' computations are separate ([Schedule SE instructions](https://www.irs.gov/pub/irs-pdf/i1040sse.pdf)). Resolve optional methods/church/farm/partnership and Additional Medicare issues through the relevant Guide or referral before serving a final liability. Feed retirement and health insurance before QBI into the assembly review; do not assume those deductions are allowed.
8. **Test estimates for the actual estimate year.** Use the dated rule below and the estimated-tax Guide. If preparing 2026 returns, distinguish 2026 payment reconciliation from 2027 estimates; the latter require their own current figures.
9. **Review the work.** Give the professional reviewer the cited computations, evidence, actual-year form destinations, judgments and outstanding questions. A provisional amount is not a completed return. Stop the affected position for a missing fact, unsupported source, failed check or companion hold; resolve it before filing.

## Figures for 2026, with years

| Item | 2026 | 2025 | Condition that decides it |
| --- | --- | --- | --- |
| Business standard mileage | 72.5 cents Jan–June; 76 cents July–December | 70 cents | Apply supported miles in each dated period; eligibility below ([IRS mileage table](https://www.irs.gov/tax-professionals/standard-mileage-rates)) |
| Social security wage base | $184,500 | $176,100 | Wages already taxed for social security use up part of the base ([2026 SE instructions](https://www.irs.gov/pub/irs-pdf/i1040sse.pdf); [2025 SE](https://www.irs.gov/pub/irs-prior/f1040sse--2025.pdf)) |
| Ordinary net SE earnings | 92.35% of covered net profit | Same | Ordinary method only; generally tax applies at net earnings of $400 or more ([Schedule SE](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf)) |
| Regular SE rates | 12.4% Social Security; 2.9% Medicare | Same | Social Security capped after wage coordination; Medicare uncapped. Additional Medicare separately referred ([26 USC 1401](https://uscode.house.gov/us/usc/t26/s1401/)) |
| Deductible regular SE part | One-half | Same | Excludes Additional Medicare Tax ([26 USC 164(f)](https://uscode.house.gov/us/usc/t26/s164/)) |
| Ordinary qualifying business meals | 50% | Same | Otherwise deductible, nonlavish, owner/employee present; actual business purpose and substantiation. Exceptions/entertainment/DOT meals referred ([26 USC 274(k), (n)](https://uscode.house.gov/us/usc/t26/s274/)) |
| Covered business gifts | $25 per individual per year | Same | Aggregate direct/indirect covered gifts; spouse/partnership, promotional and incidental-cost issues referred ([26 USC 274(b)](https://uscode.house.gov/us/usc/t26/s274/)) |
| Simplified home office | $5 per allowable square foot, at most 300 | Same | Qualifying business use and income limit; full-year unchanged area assumed here; part-year/changing area referred ([Rev. Proc. 2013-13 §4](https://www.irs.gov/pub/irs-drop/rp-13-13.pdf)) |
| De minimis safe harbor | $2,500 without AFS; $5,000 with AFS, per invoice/item | Same | Book expensing, start-of-year policy, annual election and exclusions below; not a blanket asset deduction ([IRS tangible-property FAQs](https://www.irs.gov/businesses/small-businesses-self-employed/tangible-property-final-regulations)) |
| Ordinary Form 1099-NEC service threshold | $2,000 or more | $600 or more | Business payments to nonemployees; actual exemptions, payee and settlement treatment matter. Reporting after backup withholding can apply below threshold ([2026 instructions](https://www.irs.gov/instructions/i1099mec); [2025 instructions](https://www.irs.gov/pub/irs-prior/i1099mec--2025.pdf)) |

### Conditions that must be established

- **Mileage:** an owned car must start with the standard rate in its first business year, chosen by the return due date including extensions; later actual-cost switching uses straight-line remaining-life depreciation, subject to limits. A leased car using mileage must continue for the entire lease period. Mileage is unavailable for five simultaneous cars, prior non-straight-line/MACRS depreciation, section 179/bonus allowance, or post-1997 actual costs on a leased car. Do not add the same year's fuel, insurance, repairs, lease payments or depreciation to mileage ([Pub. 463, Standard Mileage Rate](https://www.irs.gov/publications/p463)).
- **Home office:** exclusive, regular use must meet the principal-place, normal client-meeting or separate-structure route. Administrative/management use is principal-place use only if there is no other fixed location for substantial administrative/management work ([26 USC 280A(c)(1)](https://uscode.house.gov/us/usc/t26/s280A/)). The simplified deduction cannot exceed business-use gross income less unrelated business deductions; unused simplified excess cannot carry forward. Elect by using it on a timely original return; that year's election is irrevocable. Storage, daycare, multiple homes, partial years, actual-method depreciation/recapture and prior carryovers are referred ([Rev. Proc. 2013-13 §4](https://www.irs.gov/pub/irs-drop/rp-13-13.pdf)).
- **De minimis:** expense qualifying costs on books under a policy existing at the beginning of the year; an AFS requires a written policy. AFS includes qualifying SEC statements, certified audited statements and required government statements, not merely any management accounts. Attach the annual “Section 1.263(a)-1(f) de minimis safe harbor election” to the timely original federal return including extensions, with identity/TIN and election statement; apply it to all qualifying expenditures. Inventory, land and specified spare parts are excluded; section 263A can still require capitalization. Above-ceiling costs follow normal rules and are not automatically capitalized ([IRS FAQs, eligibility and election](https://www.irs.gov/businesses/small-businesses-self-employed/tangible-property-final-regulations)).
- **Payment settlement:** actual payment-card/qualifying third-party-network payments within section 6050W are excluded from NEC/MISC reporting; an ordinary bank transfer or app name alone proves no such classification ([1099 instructions, Form 1099-K](https://www.irs.gov/instructions/i1099mec)). Attorney gross proceeds, other MISC categories, foreign/exempt payees and backup withholding need separate review.

## Estimated tax and filing

For ordinary domestic calendar-year individuals, the 2026 return is due **April 15, 2027**. A timely ordinary extension permits filing by October 15, 2027; payment remains due without that filing extension. Ordinary 2025 dates were April 15, 2026 and, if validly extended, October 15, 2026, which has passed. Do not assume specific disaster/overseas or other relief ([26 USC 6072(a)](https://uscode.house.gov/us/usc/t26/s6072/), [6081](https://uscode.house.gov/us/usc/t26/s6081/), [6151](https://uscode.house.gov/us/usc/t26/s6151/)).

Generally test estimates if expected 2026 tax after withholding/refundable credits is at least **$1,000**, and those payments/credits do not cover the smaller of **90% of 2026 tax** or **100% of 2025 tax**. The prior-year alternative requires a filed, full 12-month return. Use **110%** instead of 100% where 2025 AGI exceeds **$150,000**, or **$75,000** when MFS for 2026. The full-year prior-zero-tax/citizenship-residence exception and farmer/fisher rules must be checked first; annualization and actual payment/withholding timing require the estimates Guide ([2026 Form 1040-ES, General Rule and Special Rules](https://www.irs.gov/pub/irs-pdf/f1040es.pdf)).

Ordinary 2026 instalments are due **April 15, June 15, September 15, 2026 and January 15, 2027**. Filing and paying the whole 2026 balance by **February 1, 2027** avoids the fourth instalment requirement, not earlier shortages ([2026 Form 1040-ES](https://www.irs.gov/pub/irs-pdf/f1040es.pdf); [26 USC 6654(h)](https://uscode.house.gov/us/usc/t26/s6654/)).

For 2026 information returns, NEC recipient/IRS date is **February 1, 2027**, from January 31 falling on Sunday. MISC IRS dates are **March 1, 2027** on paper or **March 31, 2027** electronically; recipient deadlines require the category-specific rule. The ordinary 2025 NEC date was **February 2, 2026**. The e-file threshold is **10** aggregated information returns, subject to applicable exemptions/waivers, not ten of each type ([1099 instructions, filing dates, e-filing and recipient statements](https://www.irs.gov/instructions/i1099mec)). Actual relief, late filing, elections and penalties are referred.

## Worked cases

These hypothetical inputs retain their original years. Each usable result assumes the stated eligibility; missing eligibility holds the result.

### Case 1: 2026 Schedule C profit

A single freelancer has $60,000 profit, no wages or other businesses, using the ordinary method. $60,000 × 92.35% = $55,410 net earnings; ×12.4% = $6,870.84 Social Security (below $184,500), ×2.9% = $1,606.89 Medicare. Total $8,477.73; deductible regular half $4,238.865 before form rounding (about $4,239). These are SE results, not a completed income-tax return ([2026 Schedule SE](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf)).

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

### Case 2: 2026 mileage

One owned car has been in business use since 2024 with the standard rate chosen that year and a mileage log. Assuming the eligibility conditions above, 6,000 January–June miles × $0.725 = $4,350 and 4,000 July–December miles × $0.76 = $3,040: total $7,390, before any separately substantiated allowable extras ([IRS mileage table](https://www.irs.gov/tax-professionals/standard-mileage-rates); [Pub. 463](https://www.irs.gov/publications/p463)).

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

### Case 3: simplified home office

The original 400-square-foot room is exclusively and regularly the principal business location: administrative/management work occurs there, with no other fixed location for that work. With full-year unchanged use and sufficient income after unrelated business deductions, min(400, 300) × $5 = $1,500. Timely electing the simplified method is required. Compare the actual method only after its expenses, limits and depreciation/recapture are independently established. Check this point with one of our partner accountants. ([26 USC 280A(c)(1)](https://uscode.house.gov/us/usc/t26/s280A/); [Rev. Proc. 2013-13](https://www.irs.gov/pub/irs-drop/rp-13-13.pdf)).

### Case 4: contractor information returns

In 2026 A received $1,800 and B $2,000 for qualifying services by ordinary bank transfer. Assume US individual nonemployees, correct TINs, no exemption or backup withholding, and no section 6050W settlement. A is below the $2,000 threshold; B meets it and needs NEC by February 1, 2027. The same $1,800 paid in 2025 exceeded that year's $600 threshold. This does not itself decide deduction eligibility ([2026 instructions](https://www.irs.gov/instructions/i1099mec); [2025 instructions](https://www.irs.gov/pub/irs-prior/i1099mec--2025.pdf)).

### Case 5: 2026 high-AGI estimates

2025 AGI $180,000, tax $30,000 on a filed 12-month return; expected 2026 tax $40,000, no withholding. Assume ordinary nonfarmer/nonfisher facts, no other credits or exception, and these are the applicable tax bases. $40,000 × 90% = $36,000; $30,000 × 110% = $33,000. Required annual amount $33,000; ordinary equal instalments $8,250 on the four dates above. Actual annualization/payment history can change period results ([2026 Form 1040-ES](https://www.irs.gov/pub/irs-pdf/f1040es.pdf); [26 USC 6654(d)](https://uscode.house.gov/us/usc/t26/s6654/)).

### Case 6: 2026 gifts and meals

Three $60 gifts to one client total $180; $300 was spent on client meals. Assume ordinary deductible, substantiated covered gifts with no exception/incidental costs, and otherwise deductible nonlavish meals with owner/employee present and genuine business purpose. Covered gifts: min($180, $25) = $25. Meals under the ordinary limit: $300 × 50% = $150. Special gifts, entertainment, transport-duty or other meal exceptions: Check this point with one of our partner accountants. ([26 USC 274(b), (k), (n)](https://uscode.house.gov/us/usc/t26/s274/)).

### Case 7: 2026 de minimis election

No-AFS sole proprietor: laptop $2,200 on one invoice; machine $2,800. The book policy to expense items under $2,500 existed January 1, 2026. Assume both costs were actually book-expensed, full business use, no excluded property or section 263A capitalization, and the timely original return carries the valid annual election. The $2,200 laptop qualifies; $2,800 exceeds the safe-harbor ceiling. With no election, test both under normal rules. The machine's actual capitalization/repair/materials/section 179/depreciation result remains held: Check this point with one of our partner accountants. ([IRS tangible-property FAQs](https://www.irs.gov/businesses/small-businesses-self-employed/tangible-property-final-regulations)).

### Case 8: business or hobby

A photographer made a profit in 2 of the last 5 years, including this year. Two is below three, so the ordinary presumption does not apply. That alone proves neither business nor hobby. Preserve the plan, books, time, marketing and changes to improve profit as evidence; the complete profit-motive and income/deduction conclusion remains held. Check this point with one of our partner accountants. ([26 USC 183(d)](https://uscode.house.gov/us/usc/t26/s183/)).

### Case 9: unknown status incorrectly defaulted to Single

The draft used Single; the taxpayer was married on December 31. Withdraw the unsupported status. Determine actual joint/separate eligibility, any considered-unmarried tests and consent from the record rather than choosing a new default. Preserve the original alternative that the spouse died during the year: death/remarriage and final-joint-return conditions need separate review. Check this point with one of our partner accountants. ([Pub. 501, Filing Status](https://www.irs.gov/publications/p501)).

### Case 10: spouses in business

Spouses co-own an unincorporated trade/business in their own names, file jointly, both materially participate and both elect QJV. Allocate by their respective interests and file separate Schedule Cs; each files SE **if otherwise required**. The same business through their LLC is ineligible for the QJV election. Community-property Rev. Proc. 2002-69 and any other entity-election treatment remain held: Check this point with one of our partner accountants. ([IRS QJV](https://www.irs.gov/businesses/small-businesses-self-employed/election-for-married-couples-unincorporated-businesses)).

## When to refuse or refer

For each affected topic below withhold the unresolved tax/filing result and say: **“Check this point with one of our partner accountants.”** Preserve the topic and supporting records in the reviewer brief.

- Partnerships/multi-member LLCs and community property, corporate elections/S or C corporations, estates/trusts, fiduciary/final returns, rental/farm/K-1 activity, payroll/worker disputes and Employee Retention Credit claims/unwinds.
- Nonresident/dual-status or treaty matters (`us-tax-residency`), foreign income/credit/Form 2555, FBAR/Form 8938 (`us-fbar-fatca-reporting`, `us-foreign-tax-credit-1116`), undocumented currency conversion, state/local or multistate treatment. No foreign-account threshold alone decides an obligation here.
- Digital assets, including investment sales, mining, staking and payments. Preserve the actual-year return question and transaction-record task; any specialist result is non-usable pending review. Do not treat this workflow or another routing link as completion of held crypto proof. Material investments, basis/holding period, home/business sales and other major assets route to `us-capital-gains` for the appropriate task.
- NOL, capital/charitable/passive/foreign-credit/AMT/section 179/home-office carryovers, startup amortization, QBI/SSTB, retirement/health/Marketplace interactions, Additional Medicare/NIIT, and other unproved full-return positions.
- Hobby deductions, commuting/temporary-work travel, entertainment/DOT meals, special gifts, detailed receipt/per-diem/reconstruction exceptions, actual/part-year home office, asset eligibility and section 179/bonus limitations. Earlier stand-alone section 179 limits, backup rates, receipt thresholds and record-destruction periods are not usable guidance here.
- Attorney gross proceeds and other MISC categories, foreign/exempt payees, backup withholding, unclear worker status, late/amended elections, special filing relief, penalties, preparer section 6694 standards, open notices/audits/collection and unfiled/amended returns.

## Completion checklist

As preparation controls, confirm year/entity/status; record every source transaction once with an evidence-backed classification/exclusion/hold; tie forms and payments without duplicates; independently recompute arithmetic and actual-year form mappings; read each operative primary-source passage and its exceptions; clear failed checks and companion holds before affected filing results. One Guide does not override law or an unresolved condition in another.

For spreadsheet work retain source inputs, live formulas, recalculated results, and formula-error checks; a hardcoded snapshot is identified as such. The working paper and brief must agree. The brief gives the job/year/entity/status/state, reviewer, scope and routes, bottom line only if supported, judgments, held alternatives, missing documents/questions and referral trace. State the actual artifact and filing status; never claim rendering, review, e-filing, approval or payment execution that did not occur.

Circular 230 written-advice control: this is preparation guidance. Establish reasonable factual/legal assumptions, identify missing facts and consider relevant circumstances; do not base advice on an audit-lottery assumption. Professional review is required by this workflow before filing; this is not an assertion that only a professional may file their own return ([31 CFR 10.37](https://www.ecfr.gov/current/title-31/section-10.37)).

## Sources

| Source and bounded use | Official URL | Read date |
| --- | --- | --- |
| Schedule C opening: sole proprietor, LLC and continuous regular business test; prior completed read reused | https://www.irs.gov/instructions/i1040sc | 2026-11-22 |
| 2026 Schedule SE and instructions: ordinary earnings, threshold, wage cap, combining businesses; prior completed reads reused | https://www.irs.gov/pub/irs-pdf/f1040sse.pdf ; https://www.irs.gov/pub/irs-pdf/i1040sse.pdf | 2026-11-22; combined-business condition 2026-11-26 |
| Archived 2025 Schedule SE, Part I wage base | https://www.irs.gov/pub/irs-prior/f1040sse--2025.pdf | 2026-11-26 |
| Sections 1401 and 164(f): regular SE rates and deductible half; prior completed reads reused | https://uscode.house.gov/us/usc/t26/s1401/ ; https://uscode.house.gov/us/usc/t26/s164/ | 2026-11-22 |
| Section 162(a), ordinary/necessary cost; section 274(b)/(d)/(k)/(n), gifts/substantiation/meals | https://uscode.house.gov/us/usc/t26/s162/ ; https://uscode.house.gov/us/usc/t26/s274/ | 2026-11-26 |
| Mileage table and Pub. 463 vehicle-method restrictions; completed vehicle-method read reused; mileage table read 2026-11-26 | https://www.irs.gov/tax-professionals/standard-mileage-rates ; https://www.irs.gov/publications/p463 | 2026-11-22; mileage table 2026-11-26 |
| Home-office statute and Rev. Proc. 2013-13 §§4.01–4.04, eligibility/simplified method; completed reads reused | https://uscode.house.gov/us/usc/t26/s280A/ ; https://www.irs.gov/pub/irs-drop/rp-13-13.pdf | 2026-11-22; operative conditions 2026-11-26 |
| Tangible-property FAQs: ceiling, policy, AFS, election, exclusions and above-ceiling treatment | https://www.irs.gov/businesses/small-businesses-self-employed/tangible-property-final-regulations | 2026-11-26 |
| Current instructions served as December 2026 revision: 2026 NEC, settlement, filing/e-file and recipient rules; archived 2025 NEC rule kept separate | https://www.irs.gov/instructions/i1099mec ; https://www.irs.gov/pub/irs-prior/i1099mec--2025.pdf | 2026-11-26 |
| 2026 Form 1040-ES and section 6654: ordinary test/dates and exceptions, prior completed reads reused | https://www.irs.gov/pub/irs-pdf/f1040es.pdf ; https://uscode.house.gov/us/usc/t26/s6654/ | 2026-11-26 |
| Sections 6072(a), 6081 and 6151: calendar-year return, ordinary filing extension and payment; completed reads reused | https://uscode.house.gov/us/usc/t26/s6072/ ; https://uscode.house.gov/us/usc/t26/s6081/ ; https://uscode.house.gov/us/usc/t26/s6151/ | 2026-11-26 |
| Pub. 501 Filing Status: prior completed structural read reused, no prior-year amounts imported | https://www.irs.gov/publications/p501 | 2026-11-26 |
| QJV definition, state-law exclusion and conditional separate SE reporting | https://www.irs.gov/businesses/small-businesses-self-employed/election-for-married-couples-unincorporated-businesses | 2026-11-26 |
| Section 183(d), rebuttable ordinary/horse presumption | https://uscode.house.gov/us/usc/t26/s183/ | 2026-11-26 |
| Circular 230 written-advice requirements, operative paragraphs read | https://www.ecfr.gov/current/title-31/section-10.37 | 2026-11-26 |

Not yet confirmed: any actual taxpayer's eligibility, final full-return form mapping, special relief, or referred outcome above. These are explicit non-usable holds, not completed determinations. Earlier source-reading descriptions are not reused as proof of passages that were never quoted.
