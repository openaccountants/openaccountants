---
name: mu-transfer-pricing
description: >
  Mauritius transfer pricing for the 2026/27 income year. Covers the arm's length test in section 75 of the Income Tax Act, who it reaches, connected persons, the Director-General's power to reset net income, record keeping, country-by-country reporting for groups with EUR 750 million revenue, and how it sits with the domestic minimum top-up tax. Use for related-party pricing, intra-group charges, management fees, or loans with a Mauritius company, and for CbCR questions.
jurisdiction: MU
category: transfer-pricing
tax_year: 2026
tax_year_notes: "Income year 1 July 2026 to 30 June 2027 (year of assessment 2027/28)"
version: 0.1
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mauritius Transfer Pricing v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year covered: Income year 1 July 2026 to 30 June 2027 (year of assessment 2027/28).

## Who this applies to

Any business or income-earning activity carried on in or from Mauritius that is controlled by a non-resident, carried on by a non-resident company or a company more than half held by a non-resident, or whose controller is not at arm's length with another person, and that appears to produce no net income or less than expected (Income Tax Act s.75(1)). It has applied to all such activity since the Act began (s.75(1A)).

## Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Source |
|---|---|---|---|---|
| Arm's length adjustment | Net income reset to what arm's length dealings would have given | s.75(2), at the Director-General's determination | 2026/27 | https://www.mra.mu/download/ITAConsolidated.pdf |
| Tax on an adjustment | 15% standard rate | See [Corporate income tax](mu-corporate-income-tax.md) | 2026/27 | same |
| CbCR threshold | Consolidated revenue of EUR 750 million | In the fiscal year before the reporting year; below it the group is excluded | 2026/27 | https://www.mra.mu/download/GN20ITCbCR.pdf |
| CbCR filing | 12 months from the last day of the reporting fiscal year | Ultimate or surrogate parent resident in Mauritius | 2026/27 | same |
| CbCR notification | Same 12 month limit | Parent gives written notice | 2026/27 | same |

## The base

"Connected persons" are two or more persons where one controls the other's business or activity, by relationship or otherwise. "Transaction" covers any transaction or series, direct or indirect, enforceable or not, and also dealings between a person and its own cross-border business (s.75(4)). A company in such a transaction must prepare and keep records as prescribed (s.75(2A)).

## Deadlines and filing

1. Identify connected persons and every transaction with them.
2. Record the pricing basis during the year, under s.75(2A).
3. Disclose in the company return (see [Corporate income tax](mu-corporate-income-tax.md)).
4. Groups above the threshold file the CbCR under the regulations through the MRA.
5. A taxpayer unsure of a treatment may use s.116A (doubt on interpretation) with the return.

## Penalties and interest

Tax from an adjustment takes the ordinary income tax penalties and interest: see [Corporate income tax](mu-corporate-income-tax.md).

## Cross-border points

Treaty relief does not displace s.75. Treaty rates are in [Cross-border](mu-cross-border.md). Section 90 addresses transactions designed to avoid tax.

## Two worked examples that recompute

**Example 1.** Mauritius subsidiary pays its foreign parent a Rs 5,000,000 fee where arm's length is Rs 3,000,000. Add back Rs 2,000,000. Extra tax at 15% is Rs 300,000.

```oa-check
name: Excess related-party fee
inputs:
  paid: 5000000
  arm: 3000000
steps:
  - adjustment: paid - arm
  - tax: adjustment * 0.15
expected:
  tax: 300000.00
```

**Example 2. Decision: keep the current fee or benchmark first?** With a Rs 20,000,000 fee and a possible 10% excess, tax at risk is Rs 300,000 plus 2.5% penalty, Rs 7,500, before interest. Compare that with the cost of a benchmark.

```oa-check
name: Exposure against benchmark cost
inputs:
  fee: 20000000
  excess: 0.10
steps:
  - tax: fee * excess * 0.15
  - penalty: tax * 0.025
  - exposure: tax + penalty
expected:
  exposure: 307500.00
```

## Ask the client first

1. Who controls the Mauritius business?
2. What flows between connected persons, and at what price?
3. Is there any pricing study or contract?
4. Global Business Licence?
5. Group revenue against EUR 750 million?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act consolidated: s.75, s.90 heading, s.116A heading read | https://www.mra.mu/download/ITAConsolidated.pdf | 2026-11-01 |
| Income Tax (Country-by-Country Reporting) Regulations, GN 20: definitions and regs 3 to 5 read | https://www.mra.mu/download/GN20ITCbCR.pdf | 2026-11-01 |

Not yet confirmed: any regulations prescribing the s.75(2A) records (s.75(3) allows them, none found on the MRA list); a preferred pricing method; advance pricing arrangements; the exact field for related parties in the company return.
