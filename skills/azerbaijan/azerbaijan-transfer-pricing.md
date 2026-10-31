---
name: azerbaijan-transfer-pricing
description: 'Use this skill for 2026 Azerbaijan transfer-pricing working papers for residents and non-resident permanent establishments conducting controlled cross-border transactions. It covers related-party and preferential-jurisdiction scope, commodity and counterparty-concentration cases, statement thresholds, method selection, comparability, current interquartile adjustments, documentation, authority requests and advance method agreements. Trigger on Azerbaijan transfer pricing, controlled transactions, arm length, CUP, cost plus, master file, local file, TP statement and CbCR screening. The complete CbCR parent, surrogate and secondary-filing workflow is not implemented. Use the cross-border skill for withholding, treaties, foreign-tax credit and CFCs. Checked against the law (tier 2); no accountant has signed it off.'
jurisdiction: AZ
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-31
version: 0.1
trust_label: Built by Michael Cutajar and the OpenAccountants team
---

# Azerbaijan Transfer Pricing v0.1

> **Checked against the law.** Tax year 2026. Figures independently re-checked against the official sources on 31 October 2026. General reference for working papers; a qualified professional must review the facts and filing position. No accountant has signed this skill off.

## Who this applies to

Azerbaijan residents and non-resident permanent establishments (PEs) conducting the cross-border transactions in [Tax Code art. 14-1.2](https://e-qanun.az/frameworks/46/f_46948.html). This is not a rule for all domestic related-party payments. Domestic market-price and deductibility rules remain relevant separately under arts. 14 and 108.

The controlled classes are resident/related non-resident and foreign branch transactions; a non-resident PE's transactions with its head office, foreign units or specified related parties; transactions with entities registered in preferential-tax jurisdictions; and the additional non-resident commodity/large-counterparty cases in art. 14-1.2.4. Art. 18 defines related parties: at least 20% direct/indirect participation or votes is one test, alongside subordination, control/common control and specified family relationships. Do not reduce the definition to ownership alone.

Apply the [current registered TP Rules](https://frameworks.e-qanun.az/35/f_35074.html), consolidated with the 2023 amendments. The tax authority's older 2017 transfer.pdf predates those amendments and is not the operative source for current documentation or interval rules.

## Rates, bands and thresholds

| Item | Amount / rule | Tax year | Official source |
|---|---|---|---|
| Related ownership/vote limb | At least 20% | 2026 | [Tax Code art. 18.2.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Controlled-transaction statement, art. 14-1.2.1–.3 classes | Aggregate relevant transactions above 500,000 | 2026 | [Tax Code art. 16.1.4](https://e-qanun.az/frameworks/46/f_46948.html) |
| Additional non-resident concentration limb | Total annual income above 30 million and each counterparty share above 30% of total income/expenses | 2026 | [Tax Code art. 14-1.2.4.2](https://e-qanun.az/frameworks/46/f_46948.html) |
| International exchange-traded commodity limb | Applicable independently of the 500,000 statement threshold | 2026 | [Tax Code art. 14-1.2.4.1, 16.1.4](https://e-qanun.az/frameworks/46/f_46948.html) |
| Corporate tax effect of an adjustment | 20% ordinary profit-tax rate | 2026 | [Tax Code art. 105.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Documentation response period relevant to sanction | 60 days from request | 2026 | [Tax Code art. 57.4](https://e-qanun.az/frameworks/46/f_46948.html) |
| Statement/required-document sanction | 6,000 | 2026 | [Tax Code art. 57.4](https://e-qanun.az/frameworks/46/f_46948.html) |
| CbCR group-revenue screen | Above EUR 750 million equivalent, prior financial year under current implementing rule | 2026 | [Tax Code art. 16.9](https://e-qanun.az/frameworks/46/f_46948.html); [STS current CbCR rule summary](https://www.taxes.gov.az/az/page/cbcr-auto-info-exchange) |
| CbCR report/notification sanction | 10,000 for failure in prescribed time/form/manner | 2026 | [Tax Code art. 57.1-2](https://e-qanun.az/frameworks/46/f_46948.html) |

## The base

Build a transaction inventory by counterparty, residence, relationship, jurisdiction, product/service, currency and value. Test the actual art. 14-1.2 classes. The 500,000 threshold determines statement filing for the first three classes; it is not a blanket arm's-length exemption. Current TP Rules paragraph 7.2 permits testing controlled transactions in a tax-control procedure even where no statement was due. The commodity and concentration cases follow art. 16.1.4's separate rule rather than borrowing the 500,000 floor.

Perform the functional analysis in Rules paragraphs 4.1–4.5: product characteristics, contract terms, volume, timing, markets, functions, assets and risks. Compare actual independent transactions, including reliable internal comparables, and document adjustments. For intangibles consider geographic rights, exclusivity and development rights. For financing consider borrower credit, security, maturity, currency and interest terms. A group policy or benchmark from another country is not sufficient without the transaction comparability analysis.

Select the method under Rules 5.1–5.4. Use comparable uncontrolled price whenever feasible. If it cannot be used, choose the method best supported by reliable comparables; where both a resale/cost-plus method and a profit method are supportable, the rules prefer resale/cost-plus. The calculations are:

- CUP: compare the controlled unit price with the comparable uncontrolled price, after justified comparability adjustments.
- Resale: work back from independent resale revenue using the comparable resale margin and the relevant acquisition/import costs; distinguish a margin on sales from a markup on cost.
- Cost plus: eligible cost base × (1 + comparable markup).
- Transactional profitability: compare net profit/selected revenue, cost or asset base, using the justified tested party and consistent financial data.
- Profit split: allocate the combined relevant profit using the supported allocation factors and functions/assets/risks, not an invented equal split.

For one reliable comparable, Rules 6.2 uses that indicator. For multiple comparables, Rules 2.0.9 and 6.3 require the interquartile interval. The current official Appendix, Example 1, sorts indicators, calculates positions Q1=(n+1)×0.25, Q2=(n+1)×0.5 and Q3=(n+1)×0.75, and averages the two surrounding indicators when the position is fractional. Follow that stated averaging method; do not silently substitute a statistical software interpolation default. In the official four-observation example (55,000; 62,000; 66,000; 70,000), Q1 is 58,500, Q2 is 64,000 and Q3 is 68,000. An in-range indicator uses the actual price. The rules use the median when the indicator requires an upward taxable-income correction outside the range, read with the one-direction protections in art. 14-1.3 and Rules 6.5.

For an underpriced sale, raise taxable revenue to the required TP result. For an overpriced deductible purchase, cap the tax deduction at the TP result. An above-range selling price or below-range purchase price does not automatically reduce Azerbaijan taxable income. Art. 14-1.4 confines the adjustment to income/profit tax; do not mechanically amend VAT or customs on the same basis. Rules 6.6 requires comparison with the selected uncontrolled enterprises' averages for the tested period and prior two years without changing the enterprises between those years. Retain the reconciliation to the actual profit-tax return.

Prepare the group and local information in Rules 7.4. Group information includes structure, business, geography, revenue sources, intangibles, cost-sharing, financial agreements, strategy, functional analyses and relevant financial statements. Local information includes the tested entity's financials for the period and prior two years, restructuring/intangible transfers, organisation/headcounts and competitors. Transaction information includes category costs, detailed functions/assets/risks, linked transactions, method and tested-party selection, comparable search, adjustments, arm's-length support and the financial data used. The Rules' actual content requirements govern even where a file is labelled master/local file in the authority FAQ.

## Deadlines and filing

File the Nəzarət olunan əməliyyatlar barədə Arayış and required appendix by the income/profit-tax return deadline under art. 16.1.4: ordinarily 31 March 2027 for 2026 (art. 149.2). Keep the documentation ready for an authority request under art. 16.1.4-1; art. 57.4 addresses failure to provide it within 60 days. A self-adjustment requires the statement's adjustment information and supporting documents under Rules 7.3 and 10.2–10.3; it is not satisfied by a net journal alone.

For advance agreement of the method, apply at least three months before the controlled transaction begins. Rules 9.3 gives 30 days for consideration, extendable twice by 30 days with reasons; the agreement letter lasts three years. Identical earlier transactions not covered by an audit can qualify under Rules 9.3-1; transactions already covered by a started/ongoing audit cannot. The agreed method is not mandatory for the taxpayer under Rules 9.3-3, and must remain consistent with uncontrolled pricing. This is a method agreement, not professional approval of every invoice.

Separately screen CbCR. The authority's current page describes the prior-year group-revenue test, a report within 12 months of the group's financial year-end and notification by 30 June of the reporting year. Use the CbCR portal described on that official page. The full parent/surrogate/local-filing exceptions and exchange-failure triggers remain unimplemented here; identify the group reporting entity before filing. Do not infer a CbCR exemption from being below the TP statement threshold.

## Penalties and interest

Art. 57.4 applies the 6,000 sanction for late/incorrect controlled-transaction statements and non-delivery of requested documentation within 60 days. Art. 57.1-2 applies the separate 10,000 CbCR report/notification sanction. Under [Tax Code art. 57.1](https://e-qanun.az/frameworks/46/f_46948.html), failure without grounds to submit a required return for a period with taxable or exempt operations or tax objects attracts AZN 40. Under [Tax Code art. 58.1](https://e-qanun.az/frameworks/46/f_46948.html), an understated or evaded tax amount attracts a 50% financial sanction, excluding additional tax assessed by a desk audit; the horizontal-monitoring case in art. 58.1-1 uses 25%. Under [Tax Code art. 59.1–59.2](https://e-qanun.az/frameworks/46/f_46948.html), late tax or advance payments bear 0.1% per overdue day, for at most one year. For additional tax identified by field audit or horizontal monitoring, interest starts on the assessment date under art. 59.2. Apply the facts and procedural exceptions before assessing a sanction.

## Cross-border points

TP Rules 12 provides information/correspondence for double taxation and refers unresolved cross-border disagreement to the applicable treaty mutual-agreement procedure. There is no automatic corresponding foreign adjustment. Confirm treaty text, eligibility and the applicable MAP deadline for the actual counterparty country. Foreign loans also require the separate art. 110 interest limitations. Preferential-jurisdiction payment tax and CFC inclusion are separate from TP; use the cross-border skill.

## Two worked examples that recompute

### One comparable, underpriced export

Assume a controlled export of 1,000 units for 500 each and one reliable CUP of 550 after adjustments. Taxable revenue increases from 500,000 to 550,000. At 20%, incremental corporate tax is 10,000. The example assumes no relief or loss and no price-comparability dispute (Rules 6.2, 6.5.1).

```oa-check
name: AZ CUP upward export adjustment 2026
inputs:
  units: 1000
  actual_price: 500
  cup_price: 550
steps:
  - actual_revenue: units*actual_price
  - tax_revenue: units*max(actual_price,cup_price)
  - adjustment: tax_revenue-actual_revenue
  - extra_tax: adjustment*0.20
expected:
  tax_revenue: 550000
  adjustment: 50000
  extra_tax: 10000
```

### Multiple comparables, overpriced purchase

Assume comparable unit prices of 100, 110, 120 and 130, with 1,000 controlled units bought at 140 and otherwise deductible. Applying the official Appendix's surrounding-value averages gives Q1=105, median=115 and Q3=125. Because the purchase is above the interval, the allowable price is the median 115. Deduction falls by 25,000 and tax increases by 5,000 (Rules 2.0.9, 6.3–6.5.2). This is a synthetic example, not an actual benchmark.

```oa-check
name: AZ purchase interval median adjustment 2026
inputs:
  c1: 100
  c2: 110
  c3: 120
  c4: 130
  actual_price: 140
  units: 1000
steps:
  - q1: (c1+c2)/2
  - median: (c2+c3)/2
  - q3: (c3+c4)/2
  - actual_cost: actual_price*units
  - allowed_cost: median*units
  - adjustment: actual_cost-allowed_cost
  - extra_tax: adjustment*0.20
expected:
  q1: 105
  median: 115
  q3: 125
  adjustment: 25000
  extra_tax: 5000
```

## Ask the client first

- Which counterparties, jurisdictions, ownership/control/family relationships and foreign units are involved?
- What are annual controlled values, total income/expenses, counterparty concentrations and commodity transactions?
- What do the contracts, actual conduct, functions/assets/risks and financial reconciliations show?
- Which internal/external comparables and tested-party data support the method and interval?
- Has an authority request, advance-agreement letter, audit or foreign adjustment occurred?
- What are the group's prior-year consolidated revenue, financial year and CbCR reporting entity?

## Sources

| Source and provisions read | Official URL | Read on |
|---|---|---|
| Tax Code, arts. 14-1, 16, 18, 57–59, 105, 149 | https://e-qanun.az/frameworks/46/f_46948.html | 2026-10-31 |
| TP Rules, current registered text, paras. 1–12 and Appendix Example 1 | https://frameworks.e-qanun.az/35/f_35074.html | 2026-10-31 |
| STS current CbCR implementing-rule summary | https://www.taxes.gov.az/az/page/cbcr-auto-info-exchange | 2026-10-31 |

Not yet confirmed: Complete CbCR parent/surrogate/local-filing exceptions and exchange-failure triggers. No filing exemption is inferred from that gap.
