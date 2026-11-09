---
name: al-transfer-pricing
description: >
  Use this skill whenever asked about Alabama transfer pricing and
  combined reporting for tax year 2026 -- how related-party economics
  are handled through combined reporting for unitary business groups
  and single-sales-factor apportionment rather than a standalone
  addback statute. Trigger on "Alabama combined reporting",
  "Alabama unitary group", "Alabama transfer pricing", "Alabama
  intercompany elimination", "Alabama addback".
jurisdiction: US-AL
category: transfer-pricing
domain: transfer-pricing
type: situation-rules
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.3
verified_by: pending
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - al-corporate-income-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Alabama transfer pricing / combined reporting

> **Source-cited draft.** Built from the ALDOR Corporate Income Tax page, read 2026-10-28. The combined-reporting statute (§40-18-50) was not retrievable this run -- every combined-reporting mechanic below is flagged as unconfirmed. No accountant has reviewed it.

## Who this applies to

- Corporations that are part of a **unitary business group** may be required to combine -- the mandate, its effective date and the unitary definition are unconfirmed.
- Standalone corporations outside a unitary group file separately; intercompany dealings with non-members surface through the single-sales-factor numerator.
- The prior draft's ownership thresholds (">50% shared ownership, with 80% for the classic unitary definition") were not tied to an archived primary source and are now in unconfirmed.

## Rates, bands and thresholds

| Item | Rule | Tax year | Source |
|---|---|---|---|
| Apportionment | Single sales factor (TYB >= 2021) | current | [ALDOR Corporate Income Tax page](https://revenue.alabama.gov/taxes-fees/corporate-income-tax/) |
| Corporate rate | 6.5% of annual net income with federal-tax deduction | current | [ALDOR Corporate Income Tax page](https://revenue.alabama.gov/taxes-fees/corporate-income-tax/) |
| Combined return for unitary groups | Ala. Code §40-18-50 | current | Section text not archived -- see Not yet confirmed |
| Addback statutes | None found for royalties/interest | current | unconfirmed |

## The taxable base

- Related-party economics are policed structurally -- combined reporting for unitary groups plus market-based single-sales-factor apportionment -- rather than through a standalone transfer-pricing documentation statute (the §40-18-50 text is unconfirmed).
- Intercompany eliminations: the combined computation eliminates intercompany transactions and unrealized profits -- per §40-18-50, whose text is unconfirmed.
- Federal taxable income is the starting point, so federal intercompany rules carry through.

## Deadlines and filing

- The combined return follows the corporate return calendar (see `al-corporate-income-tax`; the Form 20C/20CR due dates are unconfirmed there).
- Which member files as the common reporting entity, and the statutory window for reporting federal audit changes, are unconfirmed.

## Penalties and interest

- No Alabama transfer-pricing documentation penalty has been confirmed; exposure would run through the ordinary underpayment penalty and interest (percentages unconfirmed).
- Common failure modes: (1) filing separate returns when the group is unitary; (2) leaving intercompany management fees or royalties in a combined computation; (3) pricing intangibles on a "cost-plus" default that the single sales factor then amplifies into the Alabama fraction.

## Cross-border points

- Interstate only: Alabama's related-party surface is the unitary-combined computation plus market-based sales sourcing (see `al-cross-border`).
- No Alabama analog to §267A or EU arm's-length documentation has been confirmed.

## Worked examples

Client facts in these examples are hypothetical. Only rates from the confirmed table above are used (6.5% rate, single sales factor). The elimination mechanics shown are the standard combined-reporting pattern; Alabama's statutory language is unconfirmed.

**Example 1: elimination effect on group income**

Unitary group (hypothetical), two members: OpCo (Alabama sales $900,000, other sales $1,100,000) pays MgmtCo (no sales) a $200,000 management fee.

```oa-check
name: AL combined elimination effect on group income
inputs:
  opco_income: 700000
  mgmtco_income: 180000
  fee: 200000
steps:
  - separate_total: opco_income + mgmtco_income
  - combined_total: separate_total
  - drift: separate_total - combined_total
expected:
  separate_total: 880000.00
  combined_total: 880000.00
  drift: 0.00
```

(The elimination is income-neutral inside the group but moves each member's separate fraction -- the combined factor uses group sales.)

**Example 2: combined single sales factor**

Group apportionment (hypothetical) with the fee eliminated:

```oa-check
name: AL combined single sales factor
inputs:
  group_al_sales: 900000
  group_total_sales: 2000000
  combined_income: 880000
  rate: 0.065
steps:
  - factor: group_al_sales / group_total_sales
  - apportioned: combined_income * factor
  - tax: apportioned * rate
expected:
  factor: 0.45
  apportioned: 396000.00
  tax: 25740.00
```

## Ask the client first

- Is the group unitary under Alabama's combining rule -- has anyone run the ownership + integration test? (The statutory thresholds are unconfirmed here.)
- Are intercompany fees, royalties, and interest fully eliminated in the combined workpapers?
- Does the sales-factor numerator use the same market rules for every member?
- Any foreign affiliates -- is a water's-edge election being applied? (The water's-edge rule is unconfirmed.)

## Sources

| Source | URL | Read on |
|---|---|---|
| ALDOR Corporate Income Tax page (single sales factor from TYB 2021, 6.5% rate, federal-tax deduction) | https://revenue.alabama.gov/taxes-fees/corporate-income-tax/ | 2026-10-28 |

Not yet confirmed: the combined-reporting mandate, intercompany-elimination requirement, unitary-group definition and ownership thresholds under Ala. Code §40-18-50 (the prior draft carried ">50% shared ownership, with 80% for the classic unitary definition" -- confirm against the statute); whether combining is mandatory or elective and its effective date (the 2021 income-tax reform detail); the water's-edge rule; the common-reporting-entity mechanics; the absence of royalty/interest addback statutes (a negative not provable from archived sources); the statutory window for reporting federal audit changes; Code of Alabama section text (legislative mirror not retrievable this run).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at openaccountants.com.

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
