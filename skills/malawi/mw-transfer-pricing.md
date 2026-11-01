---
name: mw-transfer-pricing
description: "Malawi 2026 TP information-notice handling, audit evidence retention and amended currency-point penalties; full pricing/documentation scope remains partial."
jurisdiction: MW
category: transfer-pricing
tax_year: 2026
last_updated: 2026-11-01
tier: 2
version: 1.0
---

# Malawi transfer pricing: information-notice response and retention v 1.0

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person’s facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in Malawi.

## Who this applies to

Use when a taxpayer receives a Commissioner General information notice under the Taxation (Transfer Pricing Documentation) Regulations, or a notice of an audit concerning TP/other related-party arrangements. This is a notice-response and preservation job. It does not determine the unverified annual documentation threshold, TP method or associated-party definition. The 2025 amendment renames 127A’s marginal note; that title alone cannot supply substantive pricing rules. [TAA 91](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content); [Act 14/2025 s 2](https://elibrary.rat.gov.mw/server/api/core/bitstreams/fb807c0f-1335-442a-a1ce-9d6644186525/content); [Act 6/2026 ss 2–5](https://elibrary.rat.gov.mw/server/api/core/bitstreams/21540b28-6bfd-45b5-a910-b80f13db59b4/content).

## Rates, bands and thresholds

| Notice/retention condition | Current statutory measure | Official source |
|---|---|---|
| Failure to comply with the specified TP information notice, first month, after Act 6/2026 amendment applies | 40,000 currency points | [TAA 91(a)](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content); [Act 6/2026 s 5](https://elibrary.rat.gov.mw/server/api/core/bitstreams/21540b28-6bfd-45b5-a910-b80f13db59b4/content) |
| Each further month or part the failure continues | 1,500 additional currency points | [TAA 91(b)](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content) |
| Ordinary record retention | At least six years from statutory relevant date, or longer specified situation | [TAA 39(3),(7)](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content) |
| Notice of TP/related-party audit | Relevant records retained until written notice that audit completed, where longer | [Act 6/2026 s 3, TAA 39(3)(e)](https://elibrary.rat.gov.mw/server/api/core/bitstreams/21540b28-6bfd-45b5-a910-b80f13db59b4/content) |

Act 6 replaces “one” with “forty” in the first-month penalty’s “one thousand” wording. It does **not** create a forty-million turnover/documentation threshold. Currency points are not kwacha: the cases retain the statutory point unit; obtain the current currency-point order before converting a penalty into money.

## The base

Log the actual notice, taxpayer/period, requested transaction/document categories, service evidence and stated deadline. Assemble contracts, controlled-transaction ledger, invoice/payment records, ownership information and any existing pricing workpapers relevant to the request; do not invent an accepted method or safe margin. Reconcile supplied totals to the accounts and index each document to the question answered. Preserve originals, the submitted copy, submission evidence and any written extension/completion decision. TAA 39 requires underlying documents and extractable electronic records, with the ordinary period measured from income-year end, VAT-period end or the other statutory relevant date. Pending disputes, applications, refunds, investigations and the amended TP-audit rule can extend that period. [TAA 39](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content); [Act 6/2026 s 3](https://elibrary.rat.gov.mw/server/api/core/bitstreams/21540b28-6bfd-45b5-a910-b80f13db59b4/content).

## Deadlines and filing

Use the deadline and response channel in the actual notice; no generic thirty-day response is assumed. Under amended 37, electronic service uses the last-known registered/email/fax address and successful email transmission or fax receipt signal; do not begin the response calendar only when someone reads the inbox. Verify the notice and service facts before treating a deadline as started. Diary each request, any extension request/decision, delivery acknowledgement and written audit-completion notification. [Act 6/2026 s 2](https://elibrary.rat.gov.mw/server/api/core/bitstreams/21540b28-6bfd-45b5-a910-b80f13db59b4/content). Annual TP return dates, standardized annexes and portal fields are not established here.

## Penalties and interest

Apply 91 only after establishing failure to comply with a qualifying information notice. The initial penalty is the amended 40,000 currency points; add 1,500 for each further month or part the failure continues. The former 1,000-point first month remains historical, not a current threshold. Do not assume a penalty starts simply because a taxpayer has a related party. Other understatement/avoidance sanctions require their own facts and sources. [TAA 91](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content); [Act 6/2026 s 5](https://elibrary.rat.gov.mw/server/api/core/bitstreams/21540b28-6bfd-45b5-a910-b80f13db59b4/content).

## Cross-border points

Collect domestic/foreign counterparties and group transaction facts needed by the actual notice, but do not infer a domestic-only or cross-border-only exemption without the operative regulations. Treaty corresponding adjustments, MAP and CbCR are outside this notice-response job.

## Two worked examples that recompute

First, a hypothetical qualifying failure starts after the amended penalty applies and continues for a first month plus two further months/parts. This computes points, not kwacha.

```oa-check
name: Current notice penalty in currency points
inputs:
  first_month_points: 40000
  further_periods: 2
  further_month_points: 1500
steps:
  - penalty_points: first_month_points + further_periods * further_month_points
expected:
  penalty_points: 43000
```

Second, a hypothetical income-year record would reach its ordinary six-year floor in 2026, but a qualifying TP audit has written completion in 2028. All other longer-retention grounds are assumed absent; do not destroy records merely on an estimated completion date.

```oa-check
name: Longer TP audit retention controls
inputs:
  income_year_end: 2020
  ordinary_years: 6
  written_audit_completion_year: 2028
steps:
  - ordinary_floor_year: income_year_end + ordinary_years
  - earliest_year_under_stated_facts: max(ordinary_floor_year, written_audit_completion_year)
expected:
  ordinary_floor_year: 2026
  earliest_year_under_stated_facts: 2028
```

## Ask the client first

Get the exact notice and service/transmission evidence, stated response date, all requests/extension decisions, periods/transactions and counterparties, relevant accounts/documents, earlier submissions, current currency-point order and any written audit-completion letter. Confirm other disputes/refunds that extend retention.

## Sources

| Official source and portions actually read | Read on |
|---|---|
| [TAA 2021](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content), ss 37–40,91;39 relevant-date/extension conditions | 2026-11-01 |
| [Act 6/2026 in official gazette bundle](https://elibrary.rat.gov.mw/server/api/core/bitstreams/21540b28-6bfd-45b5-a910-b80f13db59b4/content), ss 2–5, last two PDFpages; last page visually inspected to confirm amendment wording | 2026-11-01 |
| [Act 14/2025](https://elibrary.rat.gov.mw/server/api/core/bitstreams/fb807c0f-1335-442a-a1ce-9d6644186525/content), s 2 marginal-note amendment | 2026-11-01 |

**Not yet confirmed:** actual current TP Regulations and full 127A operative text, scope/related-party definitions, annual documentation/filing requirements and thresholds, permitted methods, current currency-point conversion order, exact 2026 commencement boundary and authenticated response portal. No full annual TP compliance claim follows from this bounded job.

