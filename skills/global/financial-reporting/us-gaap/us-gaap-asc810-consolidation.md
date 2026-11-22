---
name: us-gaap-asc810-consolidation
description: "Draft US GAAP consolidation working paper separating voting-interest and VIE scope, power and economics, the private-company common-control alternative, acquisition identity and conditional elimination schedules. Current complete control, NCI and consolidation mechanics remain source-held. Load financial-reporting-workflow-base."
jurisdiction: US
category: financial-statements
domain: financial-reporting
type: computation
standard: "ASC 810 Consolidation (ASU 2015-02, ASU 2018-17 and ASU 2025-03 amendment basis)"
effective_date: 2026-12-16
tier: 2
status: needs_sources
last_updated: 2026-11-22
version: 0.1
depends_on:
  - financial-reporting-workflow-base
---

# US GAAP consolidation : ASC 810 v0.1

> **General reference only.** Draft working papers for AI-assisted accounting; no accountant has approved this version. Outputs need a qualified professional's review for the entity's actual facts.

## Scope

**Publication hold.** Current authoritative Codification access is unresolved. This file is held with `status: needs_sources`; do not publish it as a complete current-US-GAAP method. The specifically cited FASB Updates support the amendment-basis research below, not an assertion that every intervening amendment has been incorporated. Unrecovered conclusions are listed individually under Sources and are not usable instructions.

Load `financial-reporting-workflow-base`. Prepare a source-linked working paper, proposed balanced journal entries, disclosure checklist and reviewer brief. Keep assumptions separate from source-confirmed rules. Do not issue financial statements, an audit opinion or a tax return from this file.

This job identifies the consolidation question and assembles the group working paper. It does not infer control from a cap-table percentage alone. The date key 2026-12-16 marks the first possible annual-period start after 15 December 2026 for ASU 2025-03, including interims; early adoption is allowed at an interim/annual-period beginning for financial statements not yet issued or made available for issuance, and prospective application includes acquisition dates on or after the initial-application date. That amendment changes specified accounting-acquirer assessments, not every consolidation conclusion. [ASU 2025-03, Summary and 805-10-65-5](https://storage.fasb.org/ASU%202025-03.pdf).

## Ask the client first

- Group/legal-entity chart, ownership/voting rights, agreements, related parties and de facto agents.
- Each entity's design, activities, equity funding, guarantees, leases, management fees and other variable interests.
- Who directs economically significant activities; substantive participating/kick-out rights and who can exercise them.
- Reporting-entity and investee PBE status, common controlling parent, and actual policy/adoption elections.
- Reporting dates, accounting policies, trial balances, intercompany balances/profits and acquisition history.
- Prior control conclusions, changes during the period, valuations and acquisition/NCI workpapers.

## The method, step by step

1. **Build the scope register.** For every legal entity document scope, applicable exceptions, business/ownership design and whether the VIE or voting-interest analysis applies. Do not start by consolidating all majority-owned entities and stop there. Under the read voting-interest rule, more than 50% of voting shares is the usual pointer for entities other than limited partnerships; contractual rights or loss of actual control can change the result. Limited partnerships use their own substantive-rights analysis. [ASU 2015-02, 810-10-15-8/-15-8A/-15-10](https://storage.fasb.org/ASU%202015-02.pdf).
2. **Assess VIE status separately from who consolidates.** The read VIE conditions include insufficient equity at risk; equity holders as a group lacking required power, loss absorption or residual-return characteristics; and the specified disproportionate-voting/activity circumstances. Document the entire applicable test rather than a single capital ratio. Purpose/design and substantive terms matter. [ASU 2015-02, 810-10-15-13A through -15-14](https://storage.fasb.org/ASU%202015-02.pdf).
3. **Assess the primary beneficiary's two characteristics together.** The read rule requires power over the activities that most significantly affect VIE economic performance and the obligation to absorb potentially significant losses or the right to potentially significant benefits. Economic exposure alone is insufficient, and this is not a fixed ownership-percentage threshold. Consider related parties and substantive rights using the current rules, whose full refinements remain held. [ASU 2015-02, 810-10-25-38 through -25-38C](https://storage.fasb.org/ASU%202015-02.pdf).
4. **Check all common-control alternative conditions.** Under the read private-company policy, the reporting entity and legal entity must be under common control, neither under common control of a PBE, the legal entity must not be a PBE, and the reporting entity must not have a controlling financial interest under the General Subsections. Apply the election to all eligible legal entities, continue other applicable guidance and the required disclosures. It is not permission to avoid consolidating an actually controlled subsidiary. Use only the parent's direct/indirect voting-interest analysis for the specified common-control determination. [ASU 2018-17, 810-10-15-17AD through -15-17AF](https://storage.fasb.org/ASU%202018-17.pdf).
5. **Distinguish accounting acquirer from consolidation.** When adopted, ASU 2025-03 requires the stated ASC 805 factors for a business combination effected primarily by exchanging equity interests when the legal acquiree is a VIE that is a business. Do not assume the primary beneficiary is always accounting acquirer in that branch, or apply this change to an asset acquisition. Link `us-gaap-asc805-business-combinations` and document legal versus accounting identities. [ASU 2025-03, 805-10-25-5 and -55-10 through -55-15](https://storage.fasb.org/ASU%202025-03.pdf).
6. **Prepare conditional consolidation schedules.** After current control and measurement rules are recovered, align the entity trial balances, record supported acquisition/policy adjustments, reconcile each intercompany pair and prepare reviewed elimination instructions, unrealized-profit and NCI schedules. Do not simply multiply subsidiary assets by the ownership percentage. The examples below only recompute supplied worksheet instructions; complete current mechanics, NCI allocation and deconsolidation are held and no posting is cleared by them.

## Worked cases

All amounts and percentages are hypothetical. The consolidation scope, measurement and elimination instructions are assumed separately approved; these cases do not supply the missing current rules.

**Conditional balance-sheet worksheet.** Parent assets are $500,000, including a $100,000 subsidiary investment and a $20,000 intercompany receivable. Subsidiary assets are $250,000. A separately approved worksheet instructs removal of the investment and that receivable, with matched equity/liability eliminations in the companion columns. Consolidated asset arithmetic is $630,000. This is not a complete acquisition/NCI example and does not establish measurement of any asset or goodwill.

```oa-check
name: Conditional consolidation asset-column arithmetic
inputs:
  parent_assets: 500000
  subsidiary_assets: 250000
  investment_to_eliminate: 100000
  intercompany_receivable_to_eliminate: 20000
steps:
  - combined_assets: parent_assets + subsidiary_assets
  - reviewed_eliminations: investment_to_eliminate + intercompany_receivable_to_eliminate
  - conditional_group_assets: combined_assets - reviewed_eliminations
expected:
  combined_assets: 750000
  reviewed_eliminations: 120000
  conditional_group_assets: 630000
```

**Unrealized-profit worksheet boundary.** Assume the reviewer has separately cleared a $50,000 intercompany sale of inventory costing the selling entity $35,000. Under the supplied worksheet instruction, 40% of that profit remains in inventory at reporting date and must be eliminated. The conditional profit elimination is $6,000; the instruction must also address tax and any NCI consequences separately. If all goods had instead been sold outside the group, the retained fraction would be zero and this specific inventory-profit elimination would be zero. A current GAAP conclusion about the correct fraction and treatment is not provided by the arithmetic.

```oa-check
name: Supplied intercompany inventory-profit elimination instruction
inputs:
  intercompany_sale: 50000
  seller_cost: 35000
  unsold_fraction: 0.40
steps:
  - intercompany_profit: intercompany_sale - seller_cost
  - conditional_inventory_elimination: intercompany_profit * unsold_fraction
  - all_sold_outside_elimination: intercompany_profit * 0
expected:
  intercompany_profit: 15000
  conditional_inventory_elimination: 6000
  all_sold_outside_elimination: 0
```

## When to refuse or refer

Hold missing agreements, significant-activity evidence, scope exceptions or conflicting control rights. Refer funds, partnerships, related-party VIEs, structured entities, protective/participating rights, common-control transactions, reverse acquisitions, foreign subsidiaries and changes/loss of control. Combined statements of entities under common ownership are not automatically the same as consolidated statements of a controlling reporting entity.

## Sources

| Official source | Passages actually read | Read date |
|---|---|---|
| [ASU 2015-02](https://storage.fasb.org/ASU%202015-02.pdf) | 810-10-15-8/-15-8A/-15-10; -15-13A through -15-14; -25-38 through -25-38C. Amendment-basis scope/power/economics, not the full subsequent related-party refinements. | 2026-11-21 |
| [ASU 2018-17](https://storage.fasb.org/ASU%202018-17.pdf) | 810-10-15-17AD through -15-17AF. Private-company common-control alternative conditions and continuation of other guidance. | 2026-11-21 |
| [ASU 2025-03](https://storage.fasb.org/ASU%202025-03.pdf) | Summary; 805-10-25-5/-55-10 through -55-15; effective/transition summary. Specified accounting-acquirer change only. | 2026-11-22 |

**Not yet confirmed:** Complete current ASC 810 scope/exceptions, variable-interest definitions, related-party and decision-maker-fee refinements; full control/NCI/elimination mechanics; deconsolidation; current disclosure requirements; complete intervening-amendment applicability. The example elimination instructions are assumptions, not source-confirmed current accounting rules. Current ASC access attempted 2026-11-21 stopped at CAPTCHA/terms. These gaps remain non-usable.
