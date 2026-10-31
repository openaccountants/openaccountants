# Preserved Gibraltar corporate controls

Six original executable blocks are retained byte-exact with original assumptions and source context. The two selected main controls remain in the Guide’s section 7. Full original v0.17 text is preserved in gi-corporate-tax.before.txt. No historical control is removed or represented as a fresh legal acceptance.

## UK treaty: permanent establishments and business profits

Apply this section only after establishing entitlement under the UK–Gibraltar agreement, its effective period and Article 4 residence. For dual-resident companies, authority agreement is required for relief except to the extent authorities otherwise agree; incorporation alone is not the treaty tie-breaker. See [UK treaty entitlement](gi-uk-investment-income-treaty.md). Article 7(1) generally allocates enterprise profits exclusively to its territory unless it conducts business through a permanent establishment in the other territory, which can then tax attributable profits. Items separately dealt with elsewhere in the agreement retain their own rules under Article 7(4); absence of a PE is not a universal exemption for property income or investment payments. [Articles 4 and 7](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force).

### Fixed places and projects

Article 5(1) defines a PE as a fixed business location through which the enterprise conducts all or part of its business. Paragraph (2) lists management places, branches, offices, factories, workshops and natural-resource extraction locations. Paragraph (3) sets a **more-than-twelve-month** duration for a building site or construction/installation project. Exactly twelve months does not pass that project-duration limb. It is not a twelve-month grace period for every office, agent or other business activity. Verify project start, completion, interruptions and any aggregation issue before drawing a conclusion; the text alone does not settle every project-timing fact. [Article 5(1)–(3)](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force#article-5-permanent-establishment).

### Activity exclusions and combined operations

Article 5(4) contains specific exclusions for facilities/stock used solely for storage, display or delivery of the enterprise's goods, stock solely for processing by another enterprise, and fixed places solely for purchasing goods or collecting information. Its separate residual-activity exclusion requires preparatory or auxiliary character; a combination of listed activities must be preparatory or auxiliary overall. Do not rewrite these different limbs into a single assumed test. Establish what the location actually does. [Article 5(4)](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force#article-5-permanent-establishment).

Paragraph (5) withdraws paragraph (4)'s exclusion where the same or a closely related enterprise operates at that or another place in the same territory, the activities are complementary parts of a cohesive business operation, and either the relevant place is a PE or the combined activities are not preparatory or auxiliary. A separately incorporated warehouse and sales operation therefore require a combined factual analysis, not automatic exemption merely because one location stores goods. [Article 5(5)](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force#article-5-permanent-establishment).

For this rule, paragraph (6) includes factual control or common control, and in any event specified **more-than-50%** direct/indirect beneficial ownership. For companies it refers to aggregate vote and share value or beneficial equity interest. Exactly 50% does not trigger that numerical route, but factual control can still establish close relationship. The test is not the same as a universal 51% share-count requirement. [Article 5(6)](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force#article-5-permanent-establishment).

**Ownership example:** assume one equal-right class, no indirect holdings and 1,000 total shares. Holdings of 500 give 50%; 510 give 51%. The second passes the stated numerical limb; the first still needs the factual-control inquiry. Even established close relationship does not itself prove the remaining paragraph (5) conditions or a PE.

```oa-check
name: UK Gibraltar close enterprise ownership boundary
inputs:
  equal_right_shares: 1000
steps:
  - at_boundary_percent: 500 / equal_right_shares * 100
  - above_boundary_percent: 510 / equal_right_shares * 100
expected:
  at_boundary_percent: 50
  above_boundary_percent: 51
```

### Contracting agents and subsidiaries

Under Article 5(7), a person acting for the enterprise who has and habitually exercises authority to conclude contracts on its behalf can create a deemed PE, subject to the independent-agent and limited-activity exceptions in the text. Examine actual authority and conduct; a job title or unsigned internal policy is not conclusive. Paragraph (8) protects an independent broker, commission agent or other independent agent acting in the ordinary course of its business. Paragraph (9) says control of one company by another does not **of itself** make either a PE of the other. It does not disapply the fixed-place, agency or combined-operation tests. [Article 5(7)–(9)](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force#article-5-permanent-establishment).

### Attribute profits rather than taxing all sales

Article 7(2) uses a hypothetical separate and independent enterprise undertaking comparable activities under comparable conditions. Consider functions, assets and risks through the PE and elsewhere, including internal dealings. Do not allocate all customer revenue to the PE merely because customers are located there, or select a profit percentage without evidence. Keep a reconciled functional analysis and accounts supporting revenue, expense and internal-dealing allocations. Article 7(3) requires an appropriate other-territory tax adjustment to eliminate double taxation of qualifying adjusted profits, with authority consultation where necessary. [Article 7](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force#article-7-business-profits).

Article 9 concerns separate associated enterprises, including direct/indirect participation in management, control or capital and common participation. Where non-independent commercial/financial conditions suppress profits, the article permits inclusion of profits that would otherwise have accrued; its corresponding-adjustment provision is conditional on those being independent-party profits. It does not automatically accept every foreign adjustment. Use [connected-party rules](gi-connected-party-pricing-and-interest.md) and the [MAP route](gi-income-tax-assessment-appeals.md#treaty-map-a-separate-submission-and-collection-decision) for the relevant domestic and dispute questions. [Article 9](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force#article-9-associated-enterprises).

### Shipping and offshore overrides

Article 8 allocates profits from international-traffic ship/aircraft operations exclusively to the enterprise's territory. Bareboat rentals and container activities are included only when incidental to those operations; participation in pools, joint businesses and international operating agencies is also covered. Verify the Article 3 definition of international traffic and actual operations. [Articles 3(1)(h), 8](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force).

Article 21 takes priority for defined offshore exploration/exploitation activities. Paragraph (3) deems a PE, subject to paragraphs (4)–(5). The paragraph (4) exception is **not exceeding 30 days in aggregate in any twelve-month period beginning or ending in the fiscal year concerned**. Associated enterprises' substantially similar offshore activities are aggregated, excluding simultaneous activity. Its association definition is participation in management, control or capital or common participation; do not import Article 5(6)'s numerical route as its sole test. Paragraph (5) separately allocates specified offshore supply/personnel transportation and towing/anchor-handling profits exclusively to residence. [Article 21(1)–(5)](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force#article-21-miscellaneous-rules-applicable-to-certain-offshore-activities).

**Offshore example:** assume enterprise A performs 28 counted days, an associated enterprise performs 12 substantially similar days, and 10 of those days coincide with A's activity. Within the relevant window, the aggregate is **28 + 12 − 10 = 30 days**. One further non-overlapping day gives 31 and fails that paragraph (4) exception. This does not resolve paragraph (5), other PE rules, domestic charge or the distinct employee rules in the [employment treaty Guide](gi-uk-employment-pensions-treaty.md).

```oa-check
name: UK Gibraltar offshore associated activity aggregation
inputs:
  own_days: 28
  associated_days: 12
  overlapping_days: 10
steps:
  - aggregate_days: own_days + associated_days - overlapping_days
  - with_extra_nonoverlapping_day: aggregate_days + 1
expected:
  aggregate_days: 30
  with_extra_nonoverlapping_day: 31
```

This section establishes treaty rules, not a case-specific PE clearance, home-office ruling or profit-allocation approval. Current registration/return treatment for a particular non-resident enterprise, project-timing interpretations, valuation and internal-dealing evidence, other corridors and Article 28 anti-abuse application remain subject to further source and professional review.

## Trading stock when a trade ends

Section 21 supplies a separate valuation rule when a trade or business is discontinued. Use the **amount realised or value of consideration** if the stock is sold/transferred for valuable consideration to a person carrying on, or intending to carry on, a trade or business in Gibraltar **and** its cost can be deducted by that purchaser in computing the relevant assessable income/profits. Both conditions matter. A purchaser's Gibraltar address alone does not establish them. [Section 21(1)(a)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

For other stock, use what it would have realised on an **open-market sale at discontinuance**. Do not automatically use historic cost, accounting carrying value, zero because it was given away, or the actual price of a transaction that does not meet paragraph (a). Establish the cessation date and a supportable valuation as at that date. This rule determines the stock value for the cessation profit computation; it does not itself quantify the whole taxable profit. [Section 21(1)(b)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

The statutory stock definition extends beyond finished retail goods. It includes real or personal property ordinarily sold in the trade, items that would be sold when mature or complete, and materials used in manufacture, preparation or construction. It also includes services, articles or materials treated as professional work in progress. Identify the business's actual stock/WIP rather than applying the rule only to warehouse goods. [Section 21(2)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

**Example 1: qualifying purchaser.** Assume a discontinued trade transfers its stock for £25,000 cash and non-cash consideration independently valued at £5,000. The buyer intends to carry on the relevant Gibraltar trade and the stock cost is deductible in the buyer's taxable computation. Section 21(1)(a)'s value is **£30,000**. A £40,000 open-market estimate is not substituted merely because it is higher, though other applicable anti-avoidance/connected-party rules must still be checked. These facts and consideration values are assumed, not statutory safe harbours.

```oa-check
name: Gibraltar cessation stock qualifying consideration
inputs:
  cash_consideration: 25000
  noncash_consideration_value: 5000
steps:
  - cessation_stock_value: cash_consideration + noncash_consideration_value
expected:
  cessation_stock_value: 30000
```

**Example 2: other stock.** Assume the paragraph (a) buyer/deductibility conditions are not met. Supported open-market values at cessation are £18,000 for finished goods and £12,000 for qualifying unfinished stock. The section 21(1)(b) total is **£30,000**, even if the actual disposal proceeds are £20,000. The £10,000 difference is a valuation reconciliation, not automatically the final taxable gain or tax bill; reconcile it to the accounts without counting a receipt twice.

```oa-check
name: Gibraltar cessation stock open-market alternative
inputs:
  finished_goods_market_value: 18000
  unfinished_stock_market_value: 12000
  actual_disposal_proceeds: 20000
steps:
  - cessation_stock_value: finished_goods_market_value + unfinished_stock_market_value
  - valuation_difference: cessation_stock_value - actual_disposal_proceeds
expected:
  cessation_stock_value: 30000
  valuation_difference: 10000
```

Recommended working papers: cessation date and stock/WIP inventory; buyer's trade and deductible-cost evidence where paragraph (a) is used; contract and cash/non-cash consideration; market valuation where paragraph (b) applies; and the bridge to the cessation accounts. Keep stock valuation separate from capital-allowance disposals and transferred-loss eligibility. Interactions with connected-party provisions, actual valuation disputes and return-field mechanics remain case-specific review work. [Sections 20A–21; Schedule 3 Part II](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

## Designated persons: 50% loss limit and exceptions

For accounting periods ending **on or after 31 July 2024**, section 20(6) limits a designated person's loss set-off to **50% of the Schedule 3 measure of profits or gains**. Section 20(7) covers persons carrying on regulated activities within section 5 of the Financial Services Act 2019, activities licensable under section 3(1) of the Gambling Act, and their connected persons. A company outside the regulated industry can therefore still fall within the rule through connection. Check the statutory activity definitions and [connected-person rules](gi-connected-party-pricing-and-interest.md) before classifying it. [Section 20(6)–(7)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Example: assume a designated company has a Schedule 3 profit measure of £100,000 and £80,000 of eligible carried-forward losses, all outside the protected periods below, with no insolvency exception. The cap is £50,000; set off £50,000, leaving £50,000 of profits before other applicable adjustments and £30,000 of unused losses. At exactly £50,000 of eligible losses the entire pool fits the cap. This calculation does not establish the company's status or eligibility. [Section 20(6)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

```oa-check
name: Designated company restricted losses without protected pool
inputs:
  schedule_three_profit: 100000
  eligible_restricted_losses: 80000
steps:
  - cap: schedule_three_profit * 0.50
  - used: min(eligible_restricted_losses, cap)
  - remaining_profit: schedule_three_profit - used
  - unused_losses: eligible_restricted_losses - used
expected:
  cap: 50000
  used: 50000
  remaining_profit: 50000
  unused_losses: 30000
```


The restriction does not apply to losses incurred in periods ending **from 1 July 2021 through 30 June 2023**. Designated persons must use these losses before losses from other periods. Identify the loss period's **end date**: a period ending 30 June 2023 falls within the window; one ending 1 July 2023 does not. Section 20(8) separately excludes the specified designated companies subject to insolvency proceedings. Neither exception removes the other loss eligibility conditions. [Section 20(8)–(10)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

## Payments-on-account control

Keep three fields separate: the **basis period** used to calculate an instalment, the **payment due date**, and the **accounting period receiving the credit**. Section 39(4) requires payments by **28 February and 30 September**. Each is 50% of the tax payable for the relevant basis period determined using Schedule 10. The basis period is not automatically the most recently completed accounts: its due-and-payable date must precede the first instalment date as prescribed by the table. [Section 39(4)(a)–(d) and Schedule 10](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

The ITO publishes a 2022–2033 allocation table, but its footer still states **10%**. That is not the current standard company rate. Do not use that footer as rate authority or silently apply it to a 2026 computation. Check the basis liability, applicable rate provisions and any period spanning a rate change against the Act and the company's tax record. The table also has irregular month-end dates in certain rows; resolve any affected row before relying on it. [ITO allocation table](https://www.gibraltar.gov.gi/uploads/Income%20Tax%20Office/Corporate/Schedule%2010%20Table%20-%20Payments%20on%20Account%20-%202022%20to%202033.pdf); [current company rate guidance](https://www.gibraltar.gov.gi/income-tax-office/businesses-and-corporations/corporate).

For a verified basis-period liability of **£20,000**, with no reduction or adjustment required, each instalment is **£10,000**. If the final tax for the credited accounting period is £26,000, the balance is £6,000. If final tax is £18,000, the £2,000 excess is repayable under section 39(4)(e); obtain the account reconciliation rather than automatically crediting another period. The normal company balance date is nine months after the end of the month containing the period end. Section 39(9) separately gives **60 days after the assessment date** for an assessment under section 33(1)(b); do not apply the normal balance date to every additional assessment. [Section 39(1)(b), (4)(e), (9)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

For a changed accounting date, section 39(4)(f) retains the previous-date basis until an accounting period under the Act has been made up to the new date. An extended basis period within paragraph (g) is apportioned to an equivalent twelve months; a basis period shorter than twelve months is grossed up by time under paragraph (h). Example: a six-month basis liability of £6,000 annualises to £12,000, giving £6,000 per 50% instalment, before any other applicable adjustment. Keep the original period, time calculation and statutory basis in the working paper. [Section 39(4)(f)–(h)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

The instalment example above also recomputes under its stated, verified basis-liability assumptions:

```oa-check
name: Company instalments and higher or lower final liability
inputs:
  verified_basis_liability: 20000
  higher_final_tax: 26000
  lower_final_tax: 18000
steps:
  - each_instalment: verified_basis_liability * 0.50
  - total_paid: each_instalment * 2
  - balance_due: higher_final_tax - total_paid
  - excess_paid: total_paid - lower_final_tax
expected:
  each_instalment: 10000
  balance_due: 6000
  excess_paid: 2000
```

