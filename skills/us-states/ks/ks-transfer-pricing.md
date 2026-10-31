---
name: ks-transfer-pricing
description: >
  Use this skill whenever asked about Kansas transfer pricing and
  related-party adjustments for tax year 2026 — Kansas has no standalone
  TP documentation regime; related-party exposure runs through combined
  reporting, intangible/management-fee addbacks, and the apportionment
  base. Trigger on "Kansas transfer pricing", "Kansas combined report",
  "Kansas related party", "Kansas addback", "Kansas unitary".
  Source-cited draft; consolidated-return and allocation-authority rules
  cited to archived statutes; addback rules not yet confirmed.
version: 0.1
jurisdiction: US-KS
tax_year: 2026
last_updated: 2026-10-29
authored_by: Jeff Watts
review_status: pending_review
trust_label: Accountant-authored
depends_on:
  - ks-corporate-income-tax
category: transfer-pricing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kansas transfer pricing, tax year 2026

> **Source-cited draft.** Built from the KDOR Corporate Income page, the KDOR 2025 Corporate Tax Booklet and K.S.A. 79-32,141 and 79-32,142, read on 2026-10-28. Most related-party rules a Kansas reviewer would apply (addbacks, combined-report ownership tests, penalties) are not yet confirmed and are listed at the end. Treat this skill as a map of where the exposure lives, not as authority. No accountant has reviewed it.

Tax year: the corporation's federal tax year. Authority: Kansas Department of Revenue (KDOR). Currency: US dollars. Related-party pricing risk in Kansas arises from three mechanisms: (1) **combined / consolidated reporting** for affiliated or unitary groups, (2) **addback adjustments** for intangible and management-fee payments to related affiliates, and (3) the **apportionment base** itself (intercompany sales shift the sales factor). No Kansas transfer-pricing documentation statute or Kansas country-by-country report was found in the sources read; that absence is listed under Not yet confirmed.

See also: `ks-corporate-income-tax`, `ks-cross-border`.

## Who this applies to

- Members of an **affiliated or unitary group** doing business in Kansas — combined / consolidated-return exposure.
- Any K-120 filer making **intercompany payments** (royalties, interest, management fees) to out-of-state affiliates — addback exposure.
- Multistate filers whose **intercompany sales** move the Kansas apportionment factor.
- S corporations: distributive-share pricing issues flow to shareholders.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Corporate rate applied to any adjustment | 4% normal tax + 3% surtax on Kansas taxable income over $50,000 | 2026 | [K.S.A. 79-32,110(c)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110.html); see `ks-corporate-income-tax` |

No Kansas-specific transfer-pricing threshold, addback percentage or documentation penalty is confirmed; see Not yet confirmed.

## The taxable base

| Mechanism | Rule | Source |
|---|---|---|
| Starting point | Federal taxable income with Kansas modifications, so federal §482 adjustments flow into the Kansas base | [2025 Corporate Tax Booklet](https://www.ksrevenue.gov/corpbook25.html) |
| Allocation authority | The director may allocate income among affiliated or controlled corporations | [K.S.A. 79-32,141](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0141.html) |
| Consolidated returns | Federal-consolidated groups with all-Kansas income must file consolidated; the director may permit or require it for affiliated groups (Schedule K-121) | [K.S.A. 79-32,142](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0142.html); Booklet |
| Apportionment | Three-factor formula; intercompany sales move the sales factor | Booklet |

## Deadlines and filing

- No separate Kansas TP filing calendar; adjustments ride the K-120 return and any combined or consolidated attachment, due with the return — the 15th day of the 4th month after year end (April 15 for calendar-year filers) ([2025 Corporate Tax Booklet](https://www.ksrevenue.gov/corpbook25.html)).
- Keep contemporaneous federal §6662(e) documentation for audit defense; Kansas examiners use it.

## Penalties and interest

Understatement adjustments carry interest. The accuracy-penalty tiers, and whether any Kansas-specific TP documentation penalty exists, are listed under Not yet confirmed.

## Cross-border points

- Foreign-parent groups: Kansas starts from federal taxable income, so §482 adjustments carry in; state adjustments layer on top.
- Intangible holding companies in zero-tax states (DE / NV / WY patterns) are the classic addback target.
- Combined or consolidated reporting pulls out-of-state affiliates' results into one factor set.

## Worked examples

Both examples apply the Kansas corporate rates in K.S.A. 79-32,110(c): a 4% normal tax on all Kansas taxable income plus a 3% surtax on Kansas taxable income over $50,000. They show the Kansas tax effect of a transfer-pricing adjustment that increases Kansas taxable income; how the adjustment itself is measured (addback rules, combined reporting) is not yet confirmed and is not modelled here.

### Example 1: adjustment for a company already above the surtax threshold

A Kansas corporation has Kansas taxable income of $400,000 before the adjustment. A related-party royalty is found to be above an arm's-length amount and $100,000 is added back to Kansas taxable income. The company is already over $50,000, so the whole $100,000 bears both the 4% normal tax and the 3% surtax: $4,000 + $3,000 = $7,000 of additional Kansas tax.

```oa-check
name: KS TP adjustment, already over the surtax threshold
inputs:
  income_before: 400000
  adjustment: 100000
steps:
  - income_after: income_before + adjustment
  - tax_before: income_before * 0.04 + max(income_before - 50000, 0) * 0.03
  - tax_after: income_after * 0.04 + max(income_after - 50000, 0) * 0.03
  - extra_tax: tax_after - tax_before
expected:
  income_after: 500000
  tax_before: 26500
  tax_after: 33500
  extra_tax: 7000
```

### Example 2: adjustment that pushes income across the $50,000 surtax threshold

A small Kansas corporation reports $20,000 of Kansas taxable income. A $60,000 adjustment brings it to $80,000. Normal tax rises by 4% of $60,000 = $2,400. The surtax only applies to the $30,000 above $50,000: 3% x $30,000 = $900. Additional Kansas tax: $3,300.

```oa-check
name: KS TP adjustment crossing the surtax threshold
inputs:
  income_before: 20000
  adjustment: 60000
steps:
  - income_after: income_before + adjustment
  - tax_before: income_before * 0.04 + max(income_before - 50000, 0) * 0.03
  - tax_after: income_after * 0.04 + max(income_after - 50000, 0) * 0.03
  - extra_tax: tax_after - tax_before
expected:
  income_after: 80000
  tax_before: 800
  tax_after: 4100
  extra_tax: 3300
```

## Ask the client first

1. **Entity map:** which affiliates receive intercompany payments, and where are they taxed?
2. **Is the group unitary** (common control, integrated operations)? Combined / consolidated-return trigger.
3. **Is federal §6662(e) documentation on file?** Kansas examiners will ask for it.
4. **Intercompany sales volumes** that could swing the Kansas sales factor.

## Sources

| Source | URL | Read on |
|---|---|---|
| KDOR Corporate Income (entity scope, filing duty) | https://www.ksrevenue.gov/bustaxtypescorp.html | 2026-10-28 |
| KDOR 2025 Corporate Tax Booklet (starting point, three-factor formula, K-121, due date) | https://www.ksrevenue.gov/corpbook25.html | 2026-10-28 |
| K.S.A. 79-32,110 (corporate rates) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110.html | 2026-10-28 |
| K.S.A. 79-32,141 (allocation among affiliated / controlled corporations) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0141.html | 2026-10-28 |
| K.S.A. 79-32,142 (consolidated returns) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0142.html | 2026-10-28 |

Not yet confirmed: that Kansas has no standalone transfer-pricing documentation statute and no state country-by-country report; the combined-report ownership test (v0.1 expected an 80%-type test) and form ID (v0.1 named K-120M); whether Kansas has an intangible / royalty addback for payments to related low-tax affiliates, its statute (v0.1 guessed the 79-32.140 series) and scope; a management-fee / service-fee addback; any related-party interest addback beyond federal §163(j); whether combined reporting applies to S corporations; the accuracy-penalty tiers under K.S.A. 79-32 and whether any Kansas-specific TP documentation penalty exists; the linkage between federal §6662(e) documentation and Kansas penalties.

> Contributed by Jeff Watts.

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
