---
name: us-gaap-asc330-inventory
description: "Draft US GAAP inventory closing working paper: cost-basis evidence, FIFO/average versus LIFO/retail measurement branches, net realizable value, write-downs, grouping and entries. Named FASB amendment research with full current-ASC cost and measurement holds. Load financial-reporting-workflow-base."
jurisdiction: US
category: financial-statements
domain: financial-reporting
type: computation
standard: "ASC 330 Inventory (ASU 2015-11 amendment basis)"
effective_date: 2016-12-16
tier: 2
status: needs_sources
last_updated: 2026-11-22
version: 0.1
depends_on:
  - financial-reporting-workflow-base
---

# US GAAP inventory : ASC 330 v0.1

> **General reference only.** Draft working papers for AI-assisted accounting; no accountant has approved this version. Outputs need a qualified professional's review for the entity's actual facts.

## Scope

**Publication hold.** Current authoritative Codification access is unresolved. This file is held with `status: needs_sources`; do not publish it as a complete current-US-GAAP method. The specifically cited FASB Updates support the amendment-basis research below, not an assertion that every intervening amendment has been incorporated. Unrecovered conclusions are listed individually under Sources and are not usable instructions.

Load `financial-reporting-workflow-base`. Prepare a source-linked working paper, proposed balanced journal entries, disclosure checklist and reviewer brief. Keep assumptions separate from source-confirmed rules. Do not issue financial statements, an audit opinion or a tax return from this file.

This job reconciles stock and tests the supported carrying cost for loss. It does not establish tax inventory conformity, a new cost-flow policy or a universal capitalization threshold. The date key 2016-12-16 identifies the first possible fiscal-year start after 15 December 2016 for ASU 2015-11. PBEs apply it to interims within those years; other entities' interims begin within fiscal years after 15 December 2017. Application is prospective, with permitted earlier application at an interim/annual-period beginning. [ASU 2015-11 transition summary and 330-10-65-1](https://storage.fasb.org/ASU%202015-11.pdf).

## Ask the client first

- Count sheets, stock ledger, quantities/units, inventory locations, ownership and cutoff documents.
- Existing cost-flow method by class and documented cost components; changes from the prior period.
- Supplier invoices, freight and production/overhead allocation evidence; abnormal waste and capacity issues for separate review.
- Selling prices, expected discounts/returns, completion, disposal and transportation costs.
- Damaged/obsolete/excess goods, firm contracts, turnover by product and prior write-downs.
- Grouping policy, interim versus annual date and any hedging or industry-specific measurement.

## The method, step by step

1. **Reconcile quantity and cost first.** Tie count, ownership, cutoff and stock movement to the ledger. Recompute the approved cost method from purchase/production evidence. Do not decide which costs are capitalizable from this amendment alone: complete cost inclusion, idle capacity and abnormal-waste rules remain held. Record those unresolved costs separately rather than inventing a reserve.
2. **Select the right subsequent-measurement branch.** For methods other than LIFO or retail, including FIFO and average cost, the read rule is lower of cost and net realizable value (NRV), with a loss in earnings when NRV is below cost. LIFO/retail retain the separate lower-of-cost-or-market framework. Do not substitute a FIFO NRV formula for the LIFO/retail market test. [ASU 2015-11, 330-10-35-1A through -35-1C](https://storage.fasb.org/ASU%202015-11.pdf).
3. **Build NRV with all stated deductions.** Use estimated ordinary-course selling price less reasonably predictable completion, disposal and transportation costs. Link each estimate to actual evidence. For a cleared item-level FIFO/average-cost assessment, loss equals the excess of supported cost over NRV, if positive. The examples below assume no special measurement exception. [ASU 2015-11, Master Glossary NRV and 330-10-35-1B](https://storage.fasb.org/ASU%202015-11.pdf).
4. **Support the grouping decision.** The read guidance permits item, total or major-category assessment where the character/composition and income-reflection objective support it. Consistency and balanced component quantities matter. Excess components and unrelated products require their own consideration; do not offset an obsolete product's loss against another product's margin merely to avoid a write-down. [ASU 2015-11, 330-10-35-8 through -35-11](https://storage.fasb.org/ASU%202015-11.pdf).
5. **Keep the market branch and hedges distinct.** Replacement cost alone is not an unconditional LIFO/retail answer; the read paragraphs discuss utility, recoverability and firm-sales circumstances. Full ceiling/floor definitions and all current exceptions remain held. A fair-value hedge can adjust the inventory cost basis used for subsequent measurement. [ASU 2015-11, 330-10-35-3 through -35-7A](https://storage.fasb.org/ASU%202015-11.pdf).
6. **Prepare the loss entry and bridge.** After source/current-policy clearance, propose Dr inventory loss or the entity's appropriate expense line / Cr inventory or its valuation account for the measured reduction. Reconcile gross cost, allowance/write-down and net inventory to the statement. Separate physical shortage, cost correction and value decline; do not treat them as the same adjustment. The specific expense caption, reversal/new-cost-basis and full disclosure conclusions require the current sources held below.

## Worked cases

Amounts are hypothetical; both cases assume approved item-by-item FIFO cost and cleared current measurement, not LIFO or retail.

**Ordinary NRV decline.** There are 100 units at $20 carrying cost. Ordinary-course selling price is $19 per unit, completion $1, disposal $0.50 and transportation $0.50. NRV is $17 per unit, total $1,700, versus $2,000 cost. Proposed loss is $300. A calculation using selling price alone would miss $200 of the loss.

```oa-check
name: Inventory NRV includes completion disposal and transportation
inputs:
  units: 100
  unit_cost: 20
  unit_selling_price: 19
  completion: 1
  disposal: 0.5
  transportation: 0.5
steps:
  - unit_nrv: unit_selling_price - completion - disposal - transportation
  - total_cost: units * unit_cost
  - total_nrv: units * unit_nrv
  - carrying_amount: min(total_cost, total_nrv)
  - loss: total_cost - carrying_amount
expected:
  unit_nrv: 17
  total_cost: 2000
  total_nrv: 1700
  carrying_amount: 1700
  loss: 300
```

**Unrelated-product boundary.** Assume two unrelated products must be evaluated individually. Each costs $1,000; damaged product A has $700 NRV, product B $1,400 NRV. A loses $300, B remains $1,000 with no uplift; closing total is $1,700. Pooling them into one $2,100 NRV would conceal A's loss under these assumed grouping facts. Do not treat the example as a universal ban on every category approach.

```oa-check
name: Separate unrelated products without offsetting gains
inputs:
  cost_a: 1000
  nrv_a: 700
  cost_b: 1000
  nrv_b: 1400
steps:
  - carrying_a: min(cost_a, nrv_a)
  - carrying_b: min(cost_b, nrv_b)
  - total_carrying: carrying_a + carrying_b
  - total_loss: cost_a + cost_b - total_carrying
expected:
  carrying_a: 700
  carrying_b: 1000
  total_carrying: 1700
  total_loss: 300
```

## When to refuse or refer

Hold unreliable counts, ownership, cutoff, cost policy or NRV evidence. Refer LIFO/retail market measurement, special industry measurement, tax conformity, hedges, abnormal production costs and interim recoveries. Do not record an upward revaluation merely because the illustrated NRV exceeds cost.

## Sources

| Official source | Passages actually read | Read date |
|---|---|---|
| [ASU 2015-11](https://storage.fasb.org/ASU%202015-11.pdf) | Summary/transition; NRV glossary; 330-10-35-1A through -35-11. Read the subsequent-measurement amendment, not the complete current cost model. | 2026-11-21 |

**Not yet confirmed:** Complete current ASC 330 scope and initial cost rules; overhead/capacity/waste; cost-flow policy changes; LIFO/retail market ceiling/floor and exceptions; annual/interim reversal or new-cost-basis rules; complete disclosures and later-amendment applicability. These are non-usable holds. Official ASC access attempted on 2026-11-21 stopped at CAPTCHA/terms. The subsequent-measurement source does not clear initial costing.
