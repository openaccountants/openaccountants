---
name: au-employee-share-schemes
description: >
  Use this guide for Australian employee share scheme (ESS) work under Division 83A of
  the ITAA 1997 in the 2026-27 income year: resident individual employees who receive
  discounted shares, rights, options or RSUs, and the companies that report them.
  Covers the upfront taxing point and $1,000 reduction, deferral and the deferred
  taxing point, the 30-day rule, the start-up concession, forfeiture, ESS statements
  and TFN withholding, and the boundary with CGT on later disposal. Trigger on
  'ESS', 'employee share scheme', 'RSU vesting', 'employee options', 'ESS
  statement', 'start-up concession', 'deferred taxing point' or 'Division 83A'.
jurisdiction: AU
category: international
tax_year: 2026
tax_year_notes: "2026-27"
tier: 2
last_updated: 2026-11-12
version: 0.1
review_status: pending_review
verified_by: pending
license: FSL-1.1-ALv2
depends_on:
  - workflow-base
---

# Australian Employee Share Schemes (Division 83A) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This guide decides when and how much of an employee's ESS discount is assessable under Division 83A of the *Income Tax Assessment Act 1997* (ITAA 1997), and where the ESS rules stop and the CGT rules start. It loads on top of `workflow-base`, whose outputs, refusal mechanics and self-checks still apply.

**Covered:**

- ESS interests (beneficial interests in shares, or in rights to acquire shares) that an Australian resident individual acquires under an employee share scheme at a discount, including interests an associate acquires in relation to the individual's employment (the Act treats these as the individual's: note to s 83A-20).
- The upfront taxing point (Subdivision 83A-B), the $1,000 reduction (s 83A-35) and the start-up concession (s 83A-33).
- Deferral (Subdivision 83A-C): the conditions, the deferred taxing point for shares and for rights, the 30-day rule and the inclusion amount.
- Forfeiture (s 83A-310), and the CGT boundary: market-value acquisition, the reset at the deferred taxing point, the CGT exemption up to the taxing point and the start-up acquisition-date rule.
- The provider's statements and TFN withholding tax (ESS) as checks on the employee's figures.

**Not covered (routed elsewhere):**

- The CGT calculation on a later sale, capital losses, the discount and the changes for CGT events from 1 July 2027: `au-capital-gains` (Section 9 holds the enacted reform and the Bill).
- Foreign-source apportionment, foreign tax offsets and ESS discounts from a foreign employer: `au-foreign-income`. Residence status: `au-tax-residency`. ESS interests held when leaving Australia: `leaving-australia-tax-residency-cgt`.
- Fringe benefits tax, which that guide treats as generally excluding ESS interests: `au-fbt`. Payroll tax on ESS benefits: `au-payroll-tax`. ESS amounts and termination payments: `au-employment-termination-payments`.
- The rest of the individual return, including the return labels for the year: `au-individual-return`.
- Employee share trusts, takeovers and restructures, indeterminate rights, interests acquired before 1 July 2015, share traders and scheme design (refusals below).

**Period coverage.** Law as at 2 November 2026: ITAA 1997 compilation 268 (in force from 1 October 2026) and the *Taxation Administration Act 1953* (TAA) compilation 227 (in force from 1 October 2026). The Federal Register lists a later ITAA 1997 compilation from 1 December 2026 that was not yet published when read; recheck before relying on this guide after that date. The rules here are for ESS interests acquired on or after 1 July 2015 and for deferred taxing points on or after 1 July 2022 (the cessation-of-employment change below).

## Ask the client first

Confirm these before classifying a scheme or computing an inclusion:

1. The income year, the employee's residence for the whole period from grant to the taxing point and every period of employment outside Australia.
2. The plan rules, offer letter and grant agreement for each grant: what was granted (shares, rights, options, RSUs), the consideration and exercise price, vesting and forfeiture conditions, disposal restrictions, and whether the rules state that Subdivision 83A-C (deferral) applies.
3. The employer's statements of scheme category: upfront, deferral (real risk of forfeiture, salary sacrifice or rights with a disposal restriction) or start-up. Treat these as claims to test, not conclusions.
4. Dates for each grant: acquisition, vesting, lapse of any forfeiture risk, release of any disposal restriction, exercise, forfeiture, cessation of employment and disposal, with quantities at each step.
5. Market value evidence at acquisition and at each candidate taxing point, including any valuation the employer used under the regulations made for s 83A-315.
6. The ESS statements for each year, with any amended statement, and the broker or registry records of sales and closing holdings.
7. For the $1,000 reduction: taxable income before the reduction, reportable fringe benefits total, reportable superannuation contributions and total net investment loss for the year.
8. The employee's shareholding and voting power in the company immediately after each acquisition, counting shares obtainable under rights.
9. Whether the employee quoted a TFN (or, for services through an enterprise, an ABN) to the provider before the end of the income year.
10. Earlier returns that included an ESS amount for the same interests, and any amendment already lodged.

If only an ESS statement and broker records are available, build the event register from them, mark every scheme condition as unverified and return Needs Input for the scheme category, the taxing point and any CGT result that depends on them.

## The method, step by step

### Key figures

Every figure below was read on 2 November 2026 in the source named, with the full URL in Sources. 'ITAA 1997' means compilation 268 and 'TAA' means compilation 227.

| Item | Value | Source |
| --- | --- | --- |
| Upfront reduction cap | Reduce the total upfront inclusion by no more than $1,000 | ITAA 1997 s 83A-35(2)(a) |
| Upfront income test | Only if taxable income (before the reduction, excluding any assessable FHSS released amount), reportable fringe benefits total, reportable superannuation contributions and total net investment loss together do not exceed $180,000 | ITAA 1997 s 83A-35(2)(b) |
| Non-discriminatory scheme (upfront reduction) | Operated on a non-discriminatory basis for at least 75% of the employer's permanent employees with at least 3 years of service who are Australian residents | ITAA 1997 s 83A-35(6) |
| Ownership and voting limit (reduction, start-up, deferral) | Immediately after acquisition, no beneficial interest in more than 10% of the shares and no control of more than 10% of the votes, counting shares obtainable under rights | ITAA 1997 s 83A-45(6)-(7) |
| Minimum holding period (reduction and start-up) | No disposal for 3 years after acquisition, or until earlier cessation of employment; the Commissioner may allow an earlier time on a disposal of all membership interests in the company | ITAA 1997 s 83A-45(4)-(5) |
| Start-up: not listed | No equity interests in the company or its group listed at the end of the company's most recent income year before the acquisition | ITAA 1997 s 83A-33(2) |
| Start-up: age | Company and group incorporated less than 10 years before the end of that income year | ITAA 1997 s 83A-33(3) |
| Start-up: turnover | Aggregated turnover not exceeding $50 million for the most recent income year before the income year of acquisition | ITAA 1997 s 83A-33(4) |
| Start-up: shares | Discount no more than 15% of market value at acquisition | ITAA 1997 s 83A-33(5)(a) |
| Start-up: rights | Exercise price at least the market value of an ordinary share at acquisition | ITAA 1997 s 83A-33(5)(b) |
| Broad availability (deferred shares and start-up shares) | At least 75% of the employer's permanent employees with at least 3 years of service who are Australian residents are, or had been, entitled to acquire ESS interests | ITAA 1997 ss 83A-105(2), 83A-33(1)(c) |
| Salary sacrifice deferral cap | Total market value of the year's salary-sacrificed ESS interests in the employer and its holding company not more than $5,000 | ITAA 1997 s 83A-105(4)(c), (5) |
| Maximum deferral | End of the 15 year period starting at acquisition | ITAA 1997 ss 83A-115(6), 83A-120(6) |
| 30-day rule | A disposal within 30 days after the time otherwise worked out moves the deferred taxing point to the disposal | ITAA 1997 ss 83A-115(3), 83A-120(3) |
| Cessation of employment | Not a deferred taxing point for deferred taxing points on or after 1 July 2022: Act No. 8 of 2022, Sch 10, applies from the first 1 July after Royal Assent, which was 22 February 2022 | ATO legal database history notes to ss 83A-115(2) and 83A-120(2), (5); Federal Register title record C2022A00008 |
| ESS statement to the employee | No later than 14 July after the end of the financial year | TAA Sch 1 s 392-5(5)(a) |
| ESS statement to the Commissioner | No later than 14 August after the end of the financial year | TAA Sch 1 s 392-5(5)(b) |
| Correcting a statement | No later than 30 days after the provider becomes aware of a material change or omission | TAA Sch 1 s 392-10(2) |
| TFN withholding tax (ESS) | Payable by the provider at the end of 21 days after the end of the income year, where no TFN (or ABN) was quoted | TAA Sch 1 s 14-155(1), (4) |
| CGT discount holding test | The asset must have been acquired at least 12 months before the CGT event | ITAA 1997 s 115-25(1) |
| CGT discount for an individual | 50% for a discount capital gain from a CGT event before 1 July 2027 where ss 115-105 and 115-110 do not apply; later events and other entities: `au-capital-gains` | ITAA 1997 s 115-100(aa) |

The rate of TFN withholding tax (ESS) is set by the *Income Tax (TFN Withholding Tax (ESS)) Act 2009*, which this guide has not read. Do not state a rate; return Needs Input if the employee's credit for it matters.

### Step 1: Build one event history per grant

Reconcile each grant through acquisition, vesting, exercise, forfeiture, sale and closing holding to the employer and broker records. A label such as 'RSU', 'option' or 'performance right' describes the instrument, not the Division 83A category. Keep superseded ESS statements, but use each corrected figure once.

### Step 2: Confirm Division 83A applies

Subdivision 83A-B applies to an ESS interest acquired under an employee share scheme at a discount (s 83A-20(1)). If there is no discount, Division 83A does not tax the interest, although CGT can still apply on disposal (ATO, Employees). A share acquired by exercising a right that was itself acquired under the scheme is not a new upfront interest (s 83A-20(2)); the right is the ESS interest.

### Step 3: Select the regime, in this order

1. **Start-up concession (s 83A-33).** Test subsections (2) to (6), all of s 83A-45 and, for shares, the broad-availability test in s 83A-105(2). If it applies, the upfront inclusion is reduced to nil, deferral cannot apply (s 83A-105(1)(ab)) and the $1,000 reduction cannot apply (s 83A-35(2)(c)).
2. **Deferral (s 83A-105).** Deferral replaces the upfront regime if a discount remains after s 83A-315, the start-up concession does not apply, s 83A-45(1), (2), (3) and (6) are met and:
   - for a share, the broad-availability test in s 83A-105(2) is met and either there is a real risk of forfeiture at acquisition (s 83A-105(3)) or the salary sacrifice conditions in s 83A-105(4) are met (including the $5,000 cap); or
   - for a right, there is a real risk of forfeiture (s 83A-105(3)(b)) or s 83A-105(6) applies (the scheme genuinely restricted immediate disposal of the right and its rules state that Subdivision 83A-C applies, with the remaining conditions in that subsection checked against the plan rules).
3. **Upfront (s 83A-25).** Otherwise the discount is assessable in the income year of acquisition. Apply the $1,000 reduction only if s 83A-35(6) and (7), all of s 83A-45 and the $180,000 income test are met.

Each condition is tested at the time the statute names (usually acquisition). Evidence for each goes in the taxing-point matrix. A missing condition returns Needs Input; it does not default to the concession.

### Step 4: Compute the inclusion

- **Upfront:** the discount, which is market value less the consideration paid, is assessable in the year of acquisition (s 83A-25(1)), less any s 83A-35 reduction. Market value means the amount in the regulations where they specify one (s 83A-315).
- **Deferred:** at the deferred taxing point, include the market value of the interest at that time less its cost base (s 83A-110(1)).
- **Foreign employment:** the part of either amount that relates to employment outside Australia is treated as foreign source (ss 83A-25(2), 83A-110(2)). Stop and route under R-AU-ESS-1.

### Step 5: Find the deferred taxing point

- **Shares (s 83A-115):** the earlier of (a) the first time there is no real risk of forfeiture and any genuine disposal restriction has lifted, and (b) the end of 15 years from acquisition.
- **Rights (s 83A-120):** the earliest of (a) the first time, before exercise, that there is no real risk of forfeiting the right and any genuine disposal restriction on the right has lifted, (b) the end of 15 years from acquisition, and (c) the first time after exercise that there is no real risk of forfeiting the share and any genuine disposal restriction on the share has lifted.
- **30-day rule:** if the interest (or, for an exercised right, the share) is disposed of within 30 days after the time worked out above, the taxing point is the disposal (ss 83A-115(3), 83A-120(3)).
- **Cessation of employment is no longer a taxing point** for deferred taxing points on or after 1 July 2022 (key figures). The ATO's concessional schemes page (last updated 21 December 2015) still lists it; that page is superseded on this point. Ceasing employment can still end a minimum holding period (s 83A-45(5)(b)) or trigger forfeiture under the plan rules.

### Step 6: Draw the CGT boundary

- **Upfront interests:** the interest (and the share or right it forms part of) is taken to have been acquired for its market value, not its discounted value (s 83A-30(1)). That does not apply to a start-up right (s 83A-30(2)).
- **Deferred interests:** the interest is taken to have been acquired immediately after the deferred taxing point for its market value, unless the taxing point is the disposal itself (s 83A-125). The new acquisition date restarts the 12-month discount test (s 115-25(1); ATO, ESS and capital gains tax).
- **CGT exemption up to the taxing point:** a capital gain or loss on an ESS interest is disregarded where the CGT event happens at acquisition (upfront) or, for a deferred interest, at acquisition or on or before the deferred taxing point, except CGT events E4, G1 and K8 and a forfeiture on or before the deferred taxing point (s 130-80(1)-(2)). A disposal that sets the taxing point under the 30-day rule is therefore taxed under Division 83A only.
- **Start-up shares:** acquired for market value (s 83A-30(1)), so the cost base starts at market value, not the price paid. **Start-up rights:** the cost base is what was paid for the right, plus the exercise price if the right is exercised; a share acquired by exercising a start-up right is treated, for the discount tests, as acquired when the right was acquired (s 115-30(1) item 9A; ATO, ESS and capital gains tax).
- Carry the resulting cost base and acquisition date to `au-capital-gains` for the disposal. Never tax the same increase in value under both regimes, and never exempt a later gain because a discount was taxed earlier.

### Step 7: Forfeiture

If an amount was included under Division 83A and the employee later forfeits the interest (or a right lapses or is forfeited unexercised), Division 83A is taken never to have applied, unless the loss resulted from the employee's own choice (other than choosing to cease employment, or letting a right lapse or be cancelled) or from a scheme condition that protects against a fall in market value (s 83A-310). The remedy is an amendment of the earlier assessment: route to `au-amending-individual-income-tax-return-period`.

### Step 8: Check the provider's reporting

The provider must give the employee and the Commissioner a statement for each year in which it provides upfront or deferred interests, or in which a deferred taxing point occurs (TAA Sch 1 s 392-5(1)). Reconcile each statement figure to the event register. If the provider did not know of a disposal within 30 days by the statement date, it reports as though the 30-day rule did not apply (s 392-5(6)-(7)); the employee's return still follows s 83A-115(3) or s 83A-120(3), so expect and document that difference. If no TFN or ABN was quoted, check whether TFN withholding tax (ESS) was paid (s 14-155) and route the credit to the return.

### Permitted factual defaults

Each default below resolves a missing fact under settled law, produces the higher or earlier liability and must be disclosed with its alternative and effect.

| Missing fact | Default | Disclose |
| --- | --- | --- |
| Any of the four s 83A-35(2)(b) income-test components | Do not apply the $1,000 reduction | Up to $1,000 more income if the test is later met |
| Evidence of a non-discriminatory scheme or no real risk of forfeiture for the upfront reduction | Do not apply the reduction | As above |
| Incidental CGT costs (brokerage) on a later sale | Omit them from the cost base | Gain overstated by the omitted costs |
| Whether a sale was within 30 days, where both dates are known | Compute it from the dates; no default needed | |

No default is permitted for the scheme category, a start-up or deferral condition, a taxing-point date, a market value, residence or foreign service. Return Needs Input for each.

### Working paper additions

Add to the base outputs: (1) a grant and event register; (2) a taxing-point matrix showing, per grant, each statutory condition, its evidence and the resulting regime and date; (3) a bridge from the ESS statement discount to the computed inclusion; (4) a disposal and cost-base schedule handed to `au-capital-gains`.

## Worked cases

All facts are hypothetical. Each case assumes a resident individual employed in Australia throughout, plan rules sighted and every condition not discussed already evidenced.

### Case 1: Upfront discount with the $1,000 reduction (2026-27)

A listed employer gives an employee 400 shares on 1 September 2026 for nil consideration under a non-discriminatory upfront scheme with no real risk of forfeiture. Market value at acquisition is $5.00 a share. The employee's 2026-27 taxable income before the reduction is $120,000 (including the $2,000 discount); reportable fringe benefits total nil, reportable superannuation contributions $3,000, total net investment loss $1,500. The s 83A-45 conditions, including the 3-year holding lock and the 10% limit, are evidenced.

```oa-check
name: Upfront ESS discount with the 1000 dollar reduction 2026-27
inputs:
  shares: 400
  market_value_per_share: 5.00
  paid_per_share: 0
  taxable_income_before_reduction: 120000
  reportable_fringe_benefits: 0
  reportable_super_contributions: 3000
  total_net_investment_loss: 1500
  income_test_limit: 180000
  reduction_cap: 1000
steps:
  - discount: shares * (market_value_per_share - paid_per_share)
  - income_test_total: taxable_income_before_reduction + reportable_fringe_benefits + reportable_super_contributions + total_net_investment_loss
  - income_test_headroom: income_test_limit - income_test_total
  - reduction: min(reduction_cap, discount)
  - assessable_ess_amount: discount - reduction
  - cgt_first_element: shares * market_value_per_share
expected:
  discount: 2000
  income_test_total: 124500
  income_test_headroom: 55500
  reduction: 1000
  assessable_ess_amount: 1000
  cgt_first_element: 2000
```

$1,000 is assessable in 2026-27 (ss 83A-25, 83A-35). For CGT the shares were acquired on 1 September 2026 for $2,000 (s 83A-30(1)), not for the nil paid.

**Decision variant: the income test fails.** Same discount, but taxable income before the reduction is $172,000, reportable fringe benefits total $5,000, reportable superannuation contributions $4,000 and total net investment loss nil. The test total is $181,000, which exceeds $180,000, so no reduction applies and the whole $2,000 is assessable. The test uses the sum of all four components; do not test taxable income alone.

### Case 2: Deferred RSUs, with and without the 30-day rule (2026-27)

On 1 August 2024 a listed employer grants 1,000 rights for nil consideration, forfeited if the employee leaves before 15 March 2027 (a real risk of forfeiture, so s 83A-105(3)(b) defers tax). On 15 March 2027 the rights vest and are exercised automatically into shares with no disposal restriction; market value is $12.00 a share. That is the deferred taxing point under s 83A-120(7), with a cost base of nil.

- **Branch A:** the employee sells all 1,000 shares on 2 April 2027, 18 days later, at $12.50 in an arm's-length on-market sale, which is stipulated to be the market value at that time. The 30-day rule moves the taxing point to the sale (s 83A-120(3)(b)), the ESS inclusion is $12,500 and no CGT gain arises (s 83A-125; s 130-80(1)(d)).
- **Branch B:** the employee keeps the shares and sells them on 30 June 2027, 107 days later, at $12.80. The inclusion is $12,000 at 15 March 2027 (s 83A-110). The shares are taken to be reacquired then for $12,000 (s 83A-125), so the sale gives a $800 capital gain. They were held for less than 12 months from the reset date, so the gain is not a discount capital gain (s 115-25(1)). Brokerage is ignored.

```oa-check
name: Deferred RSU taxing point with and without the 30-day rule 2026-27
inputs:
  shares: 1000
  cost_base_per_share: 0
  market_value_at_vesting: 12.00
  sale_price_within_30_days: 12.50
  sale_price_after_30_days: 12.80
  days_to_branch_a_sale: 18
  thirty_day_window: 30
steps:
  - days_inside_window: thirty_day_window - days_to_branch_a_sale
  - ess_income_if_sold_within_30_days: shares * (sale_price_within_30_days - cost_base_per_share)
  - ess_income_if_held: shares * (market_value_at_vesting - cost_base_per_share)
  - cgt_cost_base_if_held: shares * market_value_at_vesting
  - capital_gain_if_held: shares * sale_price_after_30_days - cgt_cost_base_if_held
  - total_assessed_if_held: ess_income_if_held + capital_gain_if_held
expected:
  days_inside_window: 12
  ess_income_if_sold_within_30_days: 12500
  ess_income_if_held: 12000
  cgt_cost_base_if_held: 12000
  capital_gain_if_held: 800
  total_assessed_if_held: 12800
```

The provider may report Branch A as a $12,000 taxing point at 15 March 2027 if it did not know of the sale by the statement date (TAA Sch 1 s 392-5(6)). Document the $500 difference in the statement bridge instead of adopting the statement.

### Case 3: Start-up shares and a later sale (acquired 2025-26, sold 2026-27)

An unlisted Australian resident company incorporated in 2021, with aggregated turnover of $3.2 million in 2024-25 and no listed group member, issues an employee 2,000 shares on 1 October 2025 for $1.70 each. Market value at acquisition is $2.00. The s 83A-45 conditions and the broad-availability test are evidenced. The employee leaves the employer on 1 February 2027, which ends the minimum holding period (s 83A-45(5)(b)), and sells the shares on 1 March 2027 for $3.50 each, with no capital losses and no foreign or temporary residence in the ownership period.

```oa-check
name: Start-up concession shares acquired 2025-26 and sold 2026-27
inputs:
  shares: 2000
  market_value_at_acquisition: 2.00
  price_paid: 1.70
  start_up_discount_limit_percent: 15
  sale_price: 3.50
  discount_percent: 50
steps:
  - discount_as_percent_of_market_value: (market_value_at_acquisition - price_paid) / market_value_at_acquisition * 100
  - headroom_to_limit: start_up_discount_limit_percent - discount_as_percent_of_market_value
  - discount_reduced_to_nil: shares * (market_value_at_acquisition - price_paid)
  - cost_base: shares * market_value_at_acquisition
  - capital_gain: shares * sale_price - cost_base
  - discounted_gain: capital_gain - pct(capital_gain, discount_percent)
expected:
  discount_as_percent_of_market_value: 15
  headroom_to_limit: 0
  discount_reduced_to_nil: 600
  cost_base: 4000
  capital_gain: 3000
  discounted_gain: 1500
```

A 15% discount meets 'no more than 15%' (s 83A-33(5)(a)), so the $600 discount is reduced to nil in 2025-26. The cost base is market value, $4,000 (s 83A-30(1); ATO, ESS and capital gains tax, Example 2). The shares were held for more than 12 months and the sale is before 1 July 2027, so the 50% discount applies (ss 115-25(1), 115-100(aa)). A sale on or after 1 July 2027 goes to `au-capital-gains` Section 9 instead.

### Case 4: Leaving the job is no longer a taxing point

Shares acquired in 2023 under a real-risk-of-forfeiture scheme stay restricted until 2028. The employee resigns in May 2027 and the plan lets departing employees keep their shares, still restricted. Because the deferred taxing point falls after 1 July 2022, cessation is not a taxing point; the taxing point remains the earlier of the restriction lifting and 15 years after acquisition (s 83A-115(2), (4), (6)). An ESS statement or prior-year working that taxes the shares at resignation needs correcting.

### Case 5: Forfeiture after an upfront inclusion

An employee who held 12% of the company's voting power (so s 83A-45(6) failed and neither deferral nor a concession was available) included a $3,000 discount in 2025-26 on rights. In 2026-27 the rights lapse unexercised because a performance hurdle was not met. The loss was not the employee's choice and the hurdle does not protect against a fall in market value, so Division 83A is taken never to have applied to the rights (s 83A-310(1)). Prepare an amendment request for 2025-26 through `au-amending-individual-income-tax-return-period`; do not claim a deduction or capital loss in 2026-27 for the forfeited rights.

### Case 6: Foreign service period

An employee granted rights while working in Singapore, who moved to Australia before the deferred taxing point, has an inclusion partly from employment outside Australia (s 83A-110(2)). Stop at R-AU-ESS-1: record the service days in each country and route the apportionment, foreign tax and residence questions to `au-foreign-income` and `au-tax-residency`.

## When to refuse or refer

Stop the affected calculation where a fact, condition or source in this guide is unresolved, and return Needs Input or refer it for qualified review.

| Code | Trigger | Message (verbatim) |
| --- | --- | --- |
| R-AU-ESS-1 | Any employment outside Australia between grant and taxing point, a change of residence, a temporary resident or foreign tax on the ESS amount | 'Cross-border ESS income needs a source apportionment, residence and foreign tax analysis this guide does not perform. I have recorded the dates and service periods; route to au-foreign-income and a qualified reviewer.' |
| R-AU-ESS-2 | Employee share trust, takeover or restructure (s 83A-130) or indeterminate rights | 'This arrangement has its own Division 83A rules that this guide does not apply. I have built the event register; refer to a specialist reviewer before any inclusion is computed.' |
| R-AU-ESS-3 | Unlisted shares or rights with no market value evidence, or a valuation under the s 83A-315 regulations | 'The inclusion depends on a market value I cannot establish from the documents. Provide the employer's valuation and its method; until then the inclusion and cost base stay blank.' |
| R-AU-ESS-4 | ESS interests acquired before 1 July 2015, or a deferred taxing point before 1 July 2022 | 'Earlier versions of Division 83A apply to these interests and this guide covers only the current rules. Refer for review against the law in force at the time.' |
| R-AU-ESS-5 | The employee holds the shares as trading stock or revenue assets | 'Share-trading holdings need a revenue analysis outside this guide. Refer the disposal treatment to a qualified reviewer.' |
| R-AU-ESS-6 | An employer asks whether a planned scheme will qualify for a concession, or how to design one | 'Scheme design and eligibility planning are advice. I can list the statutory conditions; the design decision and any ruling application are for a qualified adviser.' |

**Reviewer attention thresholds.** These are this guide's review settings, not statutory figures. Flag for reviewer attention regardless of confidence:

| Threshold | Why |
| --- | --- |
| Any single ESS inclusion of $10,000 or more | Material income; market value and date evidence must be complete |
| An s 83A-35(2)(b) income-test total within $5,000 of $180,000 | A small correction to any component removes or restores the reduction |
| Any start-up concession claim | It reduces the inclusion to nil and every s 83A-33 condition is a group-level fact |
| Any difference between the ESS statement and the computed inclusion | Statement errors and the s 392-5(6) 30-day reporting rule both produce one |
| Any forfeiture, or any amendment of an earlier year | Time limits and the s 83A-310 exceptions decide the outcome |

Common errors: treating cessation of employment as a taxing point for a deferred interest, and treating a share acquired on exercise of a right as a fresh upfront interest. Both misstate the year and the amount.

## Completion checklist

- [ ] One event register per grant reconciles to the plan, the ESS statements and the broker records.
- [ ] Each grant's regime was selected in the Step 3 order, with each statutory condition evidenced or marked Needs Input.
- [ ] The $1,000 reduction was applied only with all four income-test components evidenced and the total at or below $180,000.
- [ ] Each deferred taxing point uses the current s 83A-115 or s 83A-120 tests, with cessation of employment excluded and the 30-day rule checked.
- [ ] Each inclusion uses market value at the right time less the right cost base, with any s 83A-315 valuation identified.
- [ ] The CGT cost base and acquisition date handed to `au-capital-gains` follow s 83A-30, s 83A-125 or s 115-30 item 9A, and no gain is taxed under both regimes.
- [ ] Foreign service, residence change, trusts, restructures and pre-2015 interests were stopped at their refusal codes.
- [ ] Differences from the ESS statement are explained in the bridge.
- [ ] Every figure used matches the key figures table and its source.

Change log: v0.1 (2 November 2026), first draft from Division 83A of ITAA 1997 compilation 268 and Divisions 14-C and 392 of TAA Schedule 1, compilation 227.

## Sources

All read on 2 November 2026; figures and dates rechecked against the same sources on 11 November 2026.

| Source | URL | Read on |
| --- | --- | --- |
| ITAA 1997, compilation 268 (from 1 October 2026), Volume 3: ss 83A-20, 83A-25, 83A-30, 83A-33, 83A-35, 83A-45, 83A-105, 83A-110, 83A-115, 83A-120, 83A-125, 83A-130, 83A-310, 83A-315, 115-25, 115-30 item 9A, 115-100 | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html | 2 November 2026 |
| ITAA 1997, compilation 268, Volume 4: s 130-80 | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_4/document_4.html | 2 November 2026 |
| TAA 1953, compilation 227 (from 1 October 2026), Volume 1: Sch 1 s 14-155 | https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html | 2 November 2026 |
| TAA 1953, compilation 227, Volume 3: Sch 1 ss 392-5, 392-10 | https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html | 2 November 2026 |
| ATO legal database, ITAA 1997 s 83A-115, with history notes on Act No. 8 of 2022 | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/83A-115 | 2 November 2026 |
| ATO legal database, ITAA 1997 s 83A-120, with history notes on Act No. 8 of 2022 and repealed s 83A-120(5) | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/83A-120 | 2 November 2026 |
| ATO legal database, ITAA 1997 s 83A-35 (cross-check of the compilation text; ss 83A-30, 83A-33, 83A-45 and 83A-105 were cross-checked on the same database) | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/83A-35 | 2 November 2026 |
| Federal Register of Legislation API, title record C2022A00008 (Corporate Collective Investment Vehicle Framework and Other Measures Act 2022, Act No. 8 of 2022): making date 22 February 2022 | https://api.prod.legislation.gov.au/v1/Titles('C2022A00008') | 2 November 2026 |
| ATO, Employees (QC47638, last updated 7 May 2020): no discount means no ESS rules; ESS statement by 14 July | https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/employee-share-schemes/employees | 2 November 2026 |
| ATO, Concessional schemes (QC47641, last updated 21 December 2015): scheme types and the 30-day rule. Superseded on cessation of employment | https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/employee-share-schemes/employees/types-of-ess/concessional-schemes-concessional-tax-treatment-can-apply | 2 November 2026 |
| ATO, ESS and capital gains tax (QC47654, last updated 21 December 2015): cost base and acquisition-date resets, start-up examples | https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/employee-share-schemes/employees/ess-and-your-tax/ess-and-capital-gains-tax | 2 November 2026 |

Not yet confirmed: the rate of TFN withholding tax (ESS); the 2026-27 return labels for ESS amounts; the s 83A-315 valuation regulations; the Subdivision 130-B and Division 134 rules for exercised rights beyond the points stated here; and any amendment in the ITAA 1997 compilation from 1 December 2026. No accountant has reviewed this draft.

Method adapted by its author from the `au-employee-share-schemes` skill in ryanduguid/australian-accounting-skills (commit 3e110da). This guide is licensed under FSL-1.1-ALv2, not the OA Guide License; see LICENSING.md.

Copyright 2026 Ryan Duguid. From github.com/ryanduguid/australian-accounting-skills, FSL-1.1-ALv2. Copies and adaptations of this file must keep this notice.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
