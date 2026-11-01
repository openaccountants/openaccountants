---
name: bh-corporate-income-tax
description: "Bahrain hydrocarbon income tax and Domestic Minimum Top-up Tax (DMTT) screening and simplified computations for tax year 2026. Covers statutory taxpayer scope, adjusted income, returns and penalties. Current general corporate-tax enactment status and electronic filing/payment workflows remain unconfirmed."
jurisdiction: BH
tax_year: 2026
last_updated: 2026-11-01
version: 0.4
category: international
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bahrain Corporate Income Tax v0.4

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Bahrain hydrocarbon taxpayers under Legislative Decree 22/1979 and Bahrain entities in multinational groups under Decree-Law 11/2024. Screen both regimes separately. The old claim that every other business pays no profits tax in 2026 is held pending verification of current general corporate-tax enactment status; an older EDB article omits the enacted DMTT and cannot support that blanket answer.

## Rates, bands and thresholds

| Item | Rate or condition | Year | Official source |
|---|---|---|---|
| Hydrocarbon income tax, art. 2 | 46% of statutory income for direct exploration/production for the taxpayer's own account from Bahrain land, or refining in own Bahrain facilities of crude owned by the taxpayer or others, wherever extracted | 2026 | https://www.lloc.gov.bh/Legislation/HTM/L2279 |
| DMTT minimum rate, art. 1 | 15%, applied through the jurisdictional effective-rate and top-up calculation, not flat tax on each company's accounting profit | Fiscal years from 1 January 2025 | https://www.lloc.gov.bh/Legislation/HTM/L1124 |
| DMTT revenue test, art. 3(C)-(D) | At least EUR 750 million consolidated revenue in at least two of the four immediately preceding fiscal years; prorate the threshold for years other than twelve months; include excluded entities' revenue | 2026 fiscal years | same |
| DMTT return, ER art. 66(A)-(C) | Filing Constituent Entity: within 15 months of reporting fiscal year end, in the NBR form and manner | 2026 fiscal years | https://www.lloc.gov.bh/Legislation/HTM/RFNE17224 |

## The base

For this activity test, Bahrain land includes territorial subsoil and seabed (art. 1(f)). Hydrocarbon income is gross receipts from the activities in art. 1(d), less art. 4 deductions. Deduct reasonable production costs and business expenses without double counting; apply the statute's capital-cost/depreciation and loss provisions, rather than using book profit unchanged. Articles 5 to 7 govern asset cost, accounting year and accounting method. The Gregorian accounting year applies unless the Minister approves an alternative (art. 6).

DMTT scope includes Bahrain Constituent Entities and qualifying joint ventures/subsidiaries (art. 3); review the multinational-group definition and excluded-entity provisions (arts. 1, 4) before computing. Under arts. 8 to 10, aggregate adjusted covered taxes and net Constituent Entity income for the relevant Bahrain jurisdictional pool; divide to find the effective rate. The top-up percentage is the positive gap to the minimum rate. Apply it to net income less substance-based income exclusion, floored at zero, then add any current additional tax and permanent-difference top-up. Special investment, stateless and minority pools require their own analysis. Do not treat the simplified example as a complete GloBE model.

Safe harbours, newly internationalised-group relief and detailed adjustments route to [bh-transfer-pricing](bh-transfer-pricing.md) and the law, rather than duplicating sibling figures.

## Deadlines and filing

Hydrocarbon art. 8: submit the estimated declaration to the Minister-designated body by the fifteenth day of the third month of the tax year. Pay twelve equal monthly instalments beginning on the fifteenth day of the next month; revise the estimate at the third, sixth, ninth and twelfth instalment months unless the final declaration has been filed. Allocate revised balances across remaining instalments; pay a final shortfall on filing if all instalments have already been paid. The Minister can grant an appropriate extension for a satisfactory reason. The law does not supply a public portal, final-return form or a fixed final-return deadline; those procedural details are held.

DMTT: identify the Filing Constituent Entity, register with NBR under law art. 17, and prepare the self-assessment calculation schedule and information schedule under ER art. 66. The information-schedule exception requires the qualifying exchange conditions in art. 66(D)-(F). Keep an NBR submission receipt and reconcile payment. Exact current login screens, field/box identifiers, advance-payment dates and payment-reference workflow are held; do not file from this Guide alone.

## Penalties and interest

Hydrocarbon art. 8 imposes 1% of amounts due for each thirty days or part of default in filing or payment, unless the Minister considers the reason reasonable. For DMTT penalties use [bh-transfer-pricing](bh-transfer-pricing.md) and law art. 28; the hydrocarbon penalty must not be applied to DMTT.

## Cross-border points

Hydrocarbon art. 2 applies irrespective of incorporation location. DMTT concerns Bahrain-located entities of qualifying multinational groups, not an automatic charge on all foreign receipts. For residence, treaties, cross-border payments and withholding use [bh-cross-border-tax](bh-cross-border-tax.md); no blanket withholding exemption is established here.

## Two worked examples that recompute

A hydrocarbon taxpayer has BHD 1,200,000 gross statutory income and BHD 200,000 allowable costs, with no other deductions or credits. Statutory net income is BHD 1,000,000 and tax is BHD 460,000.
```oa-check
name: Hydrocarbon statutory income
inputs:
  gross: 1200000
  allowable_costs: 200000
steps:
  - income: gross - allowable_costs
  - tax: income * 0.46
expected:
  income: 1000000
  tax: 460000
```

Decision: is a DMTT top-up due for an already in-scope group? Assume one relevant Bahrain pool, adjusted income BHD 1,000,000, adjusted covered tax BHD 100,000, zero substance exclusion, no safe harbour/election or special-pool issue, and zero additional amounts under art. 9(D)-(F). Compare that with covered tax of BHD 150,000: the first gives BHD 50,000, the second zero. Group eligibility must be established before this calculation.
```oa-check
name: DMTT below versus at minimum
inputs:
  income: 1000000
  covered_a: 100000
  covered_b: 150000
steps:
  - etr_a: covered_a / income
  - etr_b: covered_b / income
  - topup_a: max(0.15 - etr_a, 0) * income
  - topup_b: max(0.15 - etr_b, 0) * income
expected:
  topup_a: 50000
  topup_b: 0
```

## Ask the client first

- Which hydrocarbon activities and facilities are involved?
- What are statutory income, costs, capital allowances, losses and credits?
- What is the group structure and consolidated revenue for each preceding fiscal year, including year lengths?
- Which Bahrain entities, joint ventures and excluded entities are present?
- What are adjusted covered taxes, adjusted income, substance exclusion and safe-harbour facts?
- Which fiscal year and NBR registration/filing status apply?

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| Income Tax Law, whole enactment and arts. 1 to 13 read, including commencement | https://www.lloc.gov.bh/Legislation/HTM/L2279 | 2026-11-01 |
| DMTT Law, arts. 1 to 4, 6 to 10, 17 to 22, 28 and 44 read with neighbours | https://www.lloc.gov.bh/Legislation/HTM/L1124 | 2026-11-01 |
| DMTT ER, promulgation and arts. 65 to 70 read with surrounding filing provisions | https://www.lloc.gov.bh/Legislation/HTM/RFNE17224 | 2026-11-01 |

Not yet confirmed: current general corporate-tax enactment status, blanket zero withholding, the former 2025 advance-payment dates, permanent-safe-harbour/newly internationalised-group implementation, current NBR form boxes/payment workflow and hydrocarbon final-return administrative procedure. Full predecessor text and exact destinations are preserved in [the country evidence](../../evidence/ledgers/bahrain-20261101/README.md). These are NON-OPERATIVE holds, never defaults or authority to compute.

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
