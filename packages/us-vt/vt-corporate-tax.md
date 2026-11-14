---
name: vt-corporate-tax
description: "Compute ordinary Vermont C corporation income tax for 2026, including the graduated 6%, 7% and 8.5% schedule, receipts-based minimum tax, state modifications, single-sales-factor apportionment, Vermont NOL, CO-411 workflow and estimates. Trigger on Vermont corporation tax, CO-411, corporate minimum tax and Vermont apportionment."
version: "0.1"
jurisdiction: US-VT
category: state-tax
tax_year: 2026
last_updated: 2026-11-13
tier: 2
domain: income-tax
type: computation
---

# Vermont corporate income tax, tax year 2026

> **Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant. General reference for AI-assisted working papers. A qualified professional must review the established facts and filing result. Circular 230 section 10.37: consider relevant facts and circumstances; do not assume missing facts or rely on audit risk.

**Answer first.** Vermont C corporations pay the greater of graduated income tax and the applicable gross-receipts-based minimum. The minimum is not an additional tax. Current law uses a single sales factor, with special combined-group and receipt-sourcing rules. [5832](https://legislature.vermont.gov/statutes/section/32/151/05832); [5833](https://legislature.vermont.gov/statutes/section/32/151/05833).

## Scope

Ordinary Vermont-taxable C corporations and LLCs electing C-corporation treatment. S corporations/partnerships use business-income returns outside this computation. Unitary groups require combined reporting; special small-farm and digital-entity rules require a separate eligibility review. Federal corporate amounts belong to `us-form-1120-c-corp`.

## Ask the client first

1. Entity classification, active/inactive status, Vermont registration/account and tax-year end.
2. Federal taxable income, state tax deductions, bonus depreciation, research expenditure and separate Vermont basis schedules.
3. Vermont/everywhere receipts and delivery markets, allocable income and intercompany transactions.
4. Affiliates, common ownership, unitary activities, consolidation and Public Law 86-272 claim facts.
5. Vermont gross receipts, historical Vermont losses, credits and estimated payments.

## The method, step by step

### Rates, bands and thresholds

| Item and condition | Amount, 2026 | Official source |
| --- | --- | --- |
| Vermont net income through USD 10,000 | 6% | [5832(1)](https://legislature.vermont.gov/statutes/section/32/151/05832) |
| Over USD 10,000 through USD 25,000 | USD 600 plus 7% of excess over USD 10,000 | [5832(1)](https://legislature.vermont.gov/statutes/section/32/151/05832) |
| Over USD 25,000 | USD 1,650 plus 8.5% of excess over USD 25,000 | [5832(1)](https://legislature.vermont.gov/statutes/section/32/151/05832) |
| Ordinary minimum, Vermont gross receipts USD 0-500,000 inclusive | USD 100 | [5832(2)(C)](https://legislature.vermont.gov/statutes/section/32/151/05832) |
| Minimum, Vermont gross receipts over USD 500,000 through USD 1 million | USD 500 | [5832(2)(D)](https://legislature.vermont.gov/statutes/section/32/151/05832) |
| Minimum, over USD 1 million through USD 5 million | USD 2,000 | [5832(2)(E)](https://legislature.vermont.gov/statutes/section/32/151/05832) |
| Minimum, over USD 5 million through USD 300 million | USD 6,000 | [5832(2)(F)](https://legislature.vermont.gov/statutes/section/32/151/05832) |
| Minimum, over USD 300 million | USD 100,000 | [5832(2)(G)](https://legislature.vermont.gov/statutes/section/32/151/05832) |
| Qualifying small farm corporation minimum | USD 75; active-participant ownership and under USD 100,000 Vermont farm receipts excluding forest crops | [5832(2)(A)](https://legislature.vermont.gov/statutes/section/32/151/05832) |
| Corporate estimate trigger | Expected Vermont tax over USD 500 | [Department corporate page](https://tax.vermont.gov/business/corporate-income-tax) |
| Vermont NOL | Carryforward 10 years after loss year; distinct from federal deduction | [5888(4)(B)](https://legislature.vermont.gov/statutes/section/32/151/05888) |

The Department table abbreviates the first minimum band as less than USD 500,000, but the statute expressly includes USD 500,000 in its first band. Follow the statute at the boundary; do not silently use the higher minimum.

1. Establish Vermont filing/nexus and the correct group. Current state law defines taxable corporations in 5811(15); the read 2025 instructions also require an inactive return to keep an otherwise inactive account open. A substantiated no-activity return differs from a loss-making active company subject to minimum tax.
2. Begin with federal taxable income, then reconcile [5811(18)](https://legislature.vermont.gov/statutes/section/32/151/05811) additions/subtractions. Add back deducted state income/franchise taxes, non-Vermont municipal interest, federal NOL and federal bonus depreciation. Subtract protected US-obligation income and allowable substitute state depreciation. Keep federal and Vermont loss/basis records separate.
3. Current 5811(18) also addresses domestic research expensing: noneligible taxpayers add back the federal 174A deduction and take the prescribed historical 174 amortization subtraction. Eligible small-business taxpayers have separate election/transition provisions. Section 250 deducted income is added back under the current statutory text. Obtain eligibility and election facts before using these provisions; do not follow an older form where current law differs.
4. Under 5833, wholly Vermont income allocates in full; multistate business uses Vermont receipts divided by total includible receipts. Goods use delivery; services use their Vermont market/delivery location; statutory intangible, approximation and denominator exclusions require review. Property/payroll are still reportable where required but are not coequal apportionment factors.
5. Deduct the allowed Vermont NOL after the appropriate allocation/apportionment. Apply the graduated rates, compare to the gross-receipts minimum, then reconcile credits and payments in the required order. Loss or zero regular tax does not automatically eliminate an active corporation's minimum.
6. **2025-2026 filing-cycle form mapping:** CO-411 line 1 starts from federal 1120 line 28, with special deductions separately reconciled; line 2 is bonus-depreciation adjustment; lines 4 a/b add municipal interest and state/franchise taxes; BA-402 supplies apportionment to line 6; historical Vermont NOL goes to line 11 and gross receipts to line 17. These are reference mappings until final 2026 forms are checked. PL 86-272 claimants still complete the minimum-tax gross-receipts calculation under the read instructions.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Active corporation with loss | Determine minimum using Vermont gross receipts |
| Truly inactive open account | File supported no-Vermont-activity return; do not equate an operating loss with inactivity |
| Unitary group | Finnigan treatment applies from 2023; evaluate group nexus and all includible Vermont sales |
| Special digital entity/small farm/insurance/UBIT | Verify special regime rather than applying ordinary minimum mechanically |
| Research or foreign-income adjustment | Current statutory treatment and eligibility may override older form text |

## Worked cases

**Case 1.** An invented standalone active corporation has final Vermont taxable income USD 40,000 and Vermont gross receipts USD 300,000. Graduated tax is 600 +1,050 +1,275 =USD 2,925, greater than its USD 100 minimum.

```oa-check
name: Vermont corporate graduated tax versus minimum
inputs:
  vt_taxable: 40000
  minimum: 100
steps:
  - band1: min(vt_taxable, 10000) * 0.06
  - band2: max(min(vt_taxable, 25000) - 10000, 0) * 0.07
  - band3: max(vt_taxable - 25000, 0) * 0.085
  - regular: band1 + band2 + band3
  - selected_tax: max(regular, minimum)
expected:
  regular: 2925
  selected_tax: 2925
```

**Case 2, minimum decision.** An invented active corporation has no taxable income and exactly USD 500,000 Vermont gross receipts. Its minimum is USD 100 under the statute. If instead gross receipts are USD 500,001, the minimum is USD 500. Those receipts affect the minimum even though regular income tax remains zero.

```oa-check
name: Vermont minimum-tax boundary decision
inputs:
  regular_tax: 0
  first_band_minimum: 100
  next_band_minimum: 500
steps:
  - at_500000: max(regular_tax, first_band_minimum)
  - at_500001: max(regular_tax, next_band_minimum)
  - difference: at_500001 - at_500000
expected:
  at_500000: 100
  at_500001: 500
  difference: 400
```

## When to refuse or refer

Refer unitary membership, special digital/farm eligibility, insurance/financial-industry regimes, foreign-income modifications, complex losses, research transition elections and contested nexus or PL 86-272. Do not infer exemptions from the sales-tax nexus threshold.

## Filing and payment

Use CO-411 with BA-402 and necessary group, loss and credit schedules; reconcile to the federal return. myVTax handles registration/accounts, payments, extension and return records. Check the current e-file mandate and accepted software, submit the completed return with required attachments, retain acceptance and verify the separately scheduled payment posted correctly.

The ordinary return follows the federal original date, ordinarily April 15,2027 for calendar 2026. Estimates use CO-414, due the 15 th of the 4 th,6 th,9 th and 12 th months. [5868](https://legislature.vermont.gov/statutes/section/32/151/05868) gives a corporate extension to **one month** after the federal extended date; payment remains due originally. The older Department page says 30 days, which can differ from a calendar month; the statute controls. BA-403 and federal 7004 attachment procedures in read 2025 instructions remain labelled 2025-2026 cycle pending final 2026 form confirmation.

Under [3202](https://legislature.vermont.gov/statutes/section/32/103/03202), late filing generally adds 5% of unpaid liability per month/part up to 25%, with a USD 50 minimum after 60 days; late payment of corporate income tax generally adds 1% per month/part up to 25%, subject to statutory conditions. Apply the annually announced interest rate for each delinquency period.

## Completion checklist

- Entity/group, activity and special regimes established.
- Current law adjustments reconciled separately from older form instructions.
- Receipt factor, denominator exclusions and state NOL supported.
- Gross-receipts minimum compared with graduated tax.
- Attachments, extension/payment dates, acceptance and account posting confirmed.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 32 V.S.A. 5832. Read for graduated rates, statutory minimum bands and small-farm conditions. | https://legislature.vermont.gov/statutes/section/32/151/05832 | 2026-11-13 |
| 32 V.S.A. 5811. Read for corporate nexus/base, bonus depreciation, research and 250 modifications. | https://legislature.vermont.gov/statutes/section/32/151/05811 | 2026-11-13 |
| 32 V.S.A. 5833. Read for single-sales factor, market sourcing and denominator exclusions. | https://legislature.vermont.gov/statutes/section/32/151/05833 | 2026-11-13 |
| 32 V.S.A. 5888. Read for 10-year Vermont loss carryforward. | https://legislature.vermont.gov/statutes/section/32/151/05888 | 2026-11-13 |
| Department corporate page. Read for CO-411, active/inactive return distinction and estimates. | https://tax.vermont.gov/business/corporate-income-tax | 2026-11-13 |
| 2025 CO-411 instructions, 2025-2026 filing cycle. Read for form mapping, PL 86-272 minimum, Finnigan groups and extension workflow. | https://tax.vermont.gov/sites/tax/files/documents/CO-411-Instr-2025.pdf | 2026-11-13 |
| 32 V.S.A. 5868. Read for corporate calendar-month extension and payment distinction. | https://legislature.vermont.gov/statutes/section/32/151/05868 | 2026-11-13 |
| 32 V.S.A. 3202. Read for late filing/payment and interest framework. | https://legislature.vermont.gov/statutes/section/32/103/03202 | 2026-11-13 |

Not yet confirmed: final 2026 CO-411/BA-402/BA-403 mappings and filing-method details;2026 interest announcement; specialized group, digital-business, farm, insurance, research-election and foreign-income computations beyond the explicit ordinary workflow.
