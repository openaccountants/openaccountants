---
name: ks-transfer-pricing
description: >
  Use this skill whenever asked about Kansas transfer pricing and
  related-party adjustments for tax year 2026: a standalone Kansas
  TP documentation regime is not confirmed; related-party exposure runs through combined
  reporting, intangible/management-fee addbacks, and the apportionment
  base. Trigger on "Kansas transfer pricing", "Kansas combined report",
  "Kansas related party", "Kansas addback", "Kansas unitary".
  Built from law, not yet approved; consolidated-return and allocation-authority rules
  cited to archived statutes; addback rules not yet confirmed.
version: "0.2"
jurisdiction: US-KS
tax_year: 2026
last_updated: 2026-11-13
depends_on:
  - ks-corporate-income-tax
category: transfer-pricing
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
type: computation
domain: transfer-pricing
---

# Kansas transfer pricing, tax year 2026

> **Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant. Circular 230 section 10.37: establish relevant facts and law; do not assume missing facts or rely on audit risk. A qualified professional must review filing outputs.

Tax year: the corporation's federal tax year. Authority: Kansas Department of Revenue (KDOR). Currency: US dollars. Related-party pricing risk in Kansas arises from (1) the director's **allocation authority** over commonly controlled businesses (K.S.A. 79-32,141), (2) **consolidated reporting** for affiliated groups (K.S.A. 79-32,142) and (3) the **apportionment base** itself (intercompany sales shift the sales factor, with the 2027 transition and special-industry conditions owned by `ks-corporate-income-tax`). Whether Kansas has an addback for related-party intangible or management-fee payments is not yet confirmed. No Kansas transfer-pricing documentation statute or Kansas country-by-country report was found in the sources read; that absence is listed under Not yet confirmed.

See also: `ks-corporate-income-tax`, `ks-cross-border`.

## Scope

- Members of an **affiliated or unitary group** doing business in Kansas, combined / consolidated-return exposure.
- Any K-120 filer making **intercompany payments** (royalties, interest, management fees) to out-of-state affiliates: allocation exposure under K.S.A. 79-32,141.
- Multistate filers whose **intercompany sales** move the Kansas apportionment factor.
- S corporations: distributive-share pricing issues flow to shareholders.

## Ask the client first

1. **Entity map:** which affiliates receive intercompany payments, and where are they taxed?
2. **Is the group unitary** (common control, integrated operations)? Combined / consolidated-return trigger.
3. **Is federal §6662(e) documentation on file?** Preserve it for applicable federal rules; a specific Kansas documentation demand/penalty linkage is not established here.
4. **Intercompany sales volumes** that could swing the Kansas sales factor.

## The method, step by step

### Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Corporate tax on an established adjustment | Compute before/after liabilities using the sole rate/computation owner `ks-corporate-income-tax`; no duplicated rate here | 2026 | [KDOR current available corporate booklet](https://www.ksrevenue.gov/corpbook25.html); [APEX rate adjustment notice](https://www.ksrevenue.gov/taxnotices/notice23-10.pdf) |

No Kansas-specific transfer-pricing threshold, addback percentage or documentation penalty is confirmed; see Not yet confirmed.

### The taxable base

| Mechanism | Rule | Source |
|---|---|---|
| Starting point | Federal taxable income with Kansas modifications, so federal §482 adjustments flow into the Kansas base | [2025 Corporate Tax Booklet](https://www.ksrevenue.gov/corpbook25.html) |
| Allocation authority | The director may allocate income among affiliated or controlled corporations | [K.S.A. 79-32,141](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0141.html) |
| Consolidated returns | Federal-consolidated groups with all-Kansas income must file consolidated; the director may permit or require it for affiliated groups (Schedule K-121) | [K.S.A. 79-32,142](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0142.html); Booklet |
| Apportionment | Tax years starting before 2027: (property + payroll + sales) / 3, or elective (property + sales) / 2 for a qualifying taxpayer; from 2027: single sales factor subject to statutory special-industry conditions; see the corporate owner. Intercompany sales move the sales factor | [K.S.A. 79-3279](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0079.html) |

## Filing and payment

- No separate Kansas TP filing calendar; adjustments ride the K-120 return and any combined or consolidated attachment, due with the return, one month after the federal due date including extensions (apply the actual federal deadline and business-day rule; payment is separate under the corporate owner) ([K.S.A. 79-3221(c)(2)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0021.html)).
- Keep contemporaneous federal §6662(e) documentation for audit defense (whether Kansas ties any penalty to it is not yet confirmed).

### Penalties and interest

Understatement adjustments carry interest. The accuracy-penalty tiers, and whether any Kansas-specific TP documentation penalty exists, are listed under Not yet confirmed.

### Cross-border points

- Foreign-parent groups: Kansas starts from federal taxable income, so §482 adjustments carry in; state adjustments layer on top.
- Intangible holding companies in other states fall under the K.S.A. 79-32,141 allocation power when commonly controlled.
- Combined or consolidated reporting pulls out-of-state affiliates' results into one factor set.

## Worked cases

Both examples preserve the original income/adjustment facts, but the adjustment is hypothetical and does not establish an actual Kansas royalty addback rule. Corporate tax must first be computed by `ks-corporate-income-tax`; this skill compares those outputs. The former duplicated normal-rate assumptions were incorrect. No separate related-party rate is created here.

### Example 1: adjustment above the corporate surtax threshold

Original invented Kansas income 400,000, assumed royalty adjustment 100,000, resulting income 500,000. The corporate owner computes before-tax 24,500 and after-tax 31,000 on the stated ordinary facts; additional tax is 6,500. This supersedes the old 7,000 result, which used a stale normal rate. Actual arm's-length measurement/eligibility must be established independently.

```oa-check
name: KS TP above-threshold adjustment uses corporate owner outputs
inputs:
  income_before: 400000
  adjustment: 100000
  owner_tax_before: 24500
  owner_tax_after: 31000
steps:
  - income_after: income_before + adjustment
  - extra_tax: owner_tax_after - owner_tax_before
expected:
  income_after: 500000
  extra_tax: 6500
```

### Example 2: adjustment crossing the corporate threshold

Original invented income 20,000 plus 60,000 adjustment gives 80,000. The corporate owner returns tax 700 before and 3,700 after, difference 3,000. The old 3,300 result used the stale normal rate. Only the owner applies corporate bands; this comparison does not confirm any particular addback or combined-group ownership test.

```oa-check
name: KS TP threshold-crossing adjustment uses corporate owner outputs
inputs:
  income_before: 20000
  adjustment: 60000
  owner_tax_before: 700
  owner_tax_after: 3700
steps:
  - income_after: income_before + adjustment
  - extra_tax: owner_tax_after - owner_tax_before
expected:
  income_after: 80000
  extra_tax: 3000
```

## Boundary and exception table

| Facts | Treatment |
| --- | --- |
| Established allocation adjustment | Reconcile federal/Kansas base; corporate owner computes tax |
| Alleged related-party addback | Exact law/exception not established here; refer |
| Unitary or affiliated group | Apply researched allocation/consolidation rules; do not guess an ownership percentage |
| Federal documentation exists | Preserve it; do not assume a Kansas-specific safe harbor |

## When to refuse or refer

Refer disputed arm's-length measurement, an unsupported addback, uncertain group perimeter or a claimed Kansas documentation penalty. Do not assert absence of state requirements from an unsuccessful search.

## Completion checklist

- Preserve entity/payment map and actual adjustment authority.
- Reconcile related-party entries, federal starting point and allocation/group treatment.
- Obtain before/after tax from the corporate owner; do not duplicate its rate.
- Preserve required schedules and documentation; unresolved legal points remain explicit.

## Disclaimer

Informational and computational material only; qualified professional review is required before filing, paying or taking a tax position.

## Sources

| Source | URL | Read on |
|---|---|---|
| Read for KDOR Corporate Income (entity scope, filing duty). | https://www.ksrevenue.gov/bustaxtypescorp.html | 2026-10-28 |
| Read for KDOR 2025 Corporate Tax Booklet (starting point, three-factor formula, K-121, due date). | https://www.ksrevenue.gov/corpbook25.html | 2026-11-13 |
| Read for K.S.A. 79-32,110 (corporate rates). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110.html | 2026-11-13 |
| Read for K.S.A. 79-3279 (apportionment; single sales factor from 2027). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0079.html | 2026-11-13 |
| Read for K.S.A. 79-3221 (corporate due date). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0021.html | 2026-11-13 |
| Read for K.S.A. 79-32,141 (allocation among affiliated / controlled corporations). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0141.html | 2026-11-13 |
| Read for K.S.A. 79-32,142 (consolidated returns). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0142.html | 2026-11-13 |
| Read for effective APEX rate correction; rate computation is delegated to corporate owner. | https://www.ksrevenue.gov/taxnotices/notice23-10.pdf | 2026-11-13 |

Not yet confirmed: that Kansas has no standalone transfer-pricing documentation statute and no state country-by-country report; the combined-report ownership test (v 0.1 expected an 80%-type test) and form ID (v 0.1 named K-120M); whether Kansas has an intangible / royalty addback for payments to related low-tax affiliates, its statute (v 0.1 guessed the 79-32.140 series) and scope; a management-fee / service-fee addback; any related-party interest addback beyond federal §163(j); whether combined reporting applies to S corporations; the accuracy-penalty tiers under K.S.A. 79-32 and whether any Kansas-specific TP documentation penalty exists; the linkage between federal §6662(e) documentation and Kansas penalties.

> Contributed by Jeff Watts.
