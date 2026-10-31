---
name: north-macedonia-transfer-pricing
description: "Use this skill for North Macedonia related-party pricing and documentation for calendar year 2026. Trigger on transfer pricing, arm’s length, related-party transactions, P/TC, master file, local file, shortened report, interest benchmarking or interquartile range. It covers the corporate relationship tests, exclusions from the main pricing/documentation provisions, method selection, comparable transactions, upward profit adjustments, documentation contents, retention and UJP request deadlines. It separately preserves related-party lending, thin-capitalisation, hidden-distribution and sole-trader rules that are not removed by the corporate documentation exemption. It contains two recomputing controls based on explicitly assumed comparables. This tier 2 skill, checked against the law, awaits a licensed accountant’s review."
jurisdiction: MK
category: transfer-pricing
tax_year: 2026
tier: 2
trust_label: Built by Michael Cutajar and the OpenAccountants team
last_updated: 2026-10-30
version: 0.1
---

# North Macedonia transfer pricing v0.1

**Tax year: 2026. Checked against the law, tier 2.** Amounts are MKD unless stated otherwise. Professional review remains outstanding.

## Who this applies to

[Profit Tax Law arts. 12-16][cit] govern related-party transactions and associated documentation. Art. 16 relationships extend beyond ownership: at least 20% capital/votes directly or indirectly; common 20% ownership/control; overlapping directors/boards; qualifying loans/guarantees exceeding 20% of the other's book assets; contractual entitlement to at least 20% profits; head-office/PE relationships; and transactions with a resident of a state whose profit-tax rate is 25% below the local rate. Family attribution applies under art. 16(2). Do not test shareholding alone.

Art. 12-b expressly excludes **transactions between resident related parties** and **taxpayers with total annual revenue up to 300,000,000** from **arts. 12 and 12-a**. Thus it affects both that pricing-adjustment provision and its documentation regime, not documentation alone. It does not remove separate arts. 9(1)(7), 13-15, VAT valuations or [PIT art. 27(8)][pit] sole-trader adjustments.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official provision |
|---|---|---|---|
| Main corporate TP revenue exclusion | Total annual revenue up to and including 300,000,000 | 2026 | [Profit Tax Law art. 12-b][cit] |
| Shortened report | Covered annual related-party transaction total not exceeding 10,000,000; otherwise full report | 2026 | [Art. 12-a(1)-(2)][cit] |
| Ownership/votes/common-ownership threshold | At least 20% | 2026 | [Art. 16(1)(1)-(2)][cit] |
| Loan/guarantee relationship | More than 20% of other's total book assets | 2026 | [Art. 16(1)(4)][cit] |
| Contractual profit relationship | At least 20% | 2026 | [Art. 16(1)(5)][cit] |
| Low-tax jurisdiction relationship test | Foreign profit-tax rate 25% below North Macedonia's rate | 2026 | [Art. 16(1)(7)][cit] |
| Arm's-length accepted range | 25th-75th percentiles; outside range use median | 2026 | [TP Rulebook art. 16(5)-(6)][tp] |
| Main-report retention | 10 years from year-end covered by report | 2026 | [Profit Tax Law art. 12-a(4)][cit] |
| Report on UJP request | Within 15 days after receipt; UJP request after 30 days from DB deadline | 2026 | [Art. 12-a(5)-(6)][cit] |
| Profit-tax effect of a taxable uplift | 10% | 2026 | [Art. 2][cit] |

The 10 million test chooses report format **after** establishing that arts. 12/12-a apply. A shortened report is not a price safe harbour. Record total revenue and the annual transaction aggregate separately and test exact boundaries.

## The base

For an in-scope transaction, art. 12 adds the positive difference between booked expense and arm's-length expense, or arm's-length revenue and booked revenue. Calculate each transaction category without creating an automatic downward adjustment or netting excess revenue against another category's excessive expense. Controlled transactions include tangible/intangible property, financing, services, royalties, shares, derivatives and other profit-affecting dealings.

**Method selection:** choose the most appropriate method per transaction category under art. 12(4)-(5), supported by [Rulebook arts. 14-24][tp].

- Comparable uncontrolled price: compare the controlled price with a genuinely comparable independent price (art. 18).
- Resale price: resale revenue less comparable gross margin; gross margin is `(sales - acquisition cost) / sales` (art. 19).
- Cost plus: eligible direct/indirect production/service costs plus comparable gross cost markup; markup is `(sales - cost) / cost` (arts. 20-21).
- Transactional net margin: compare a supported net-profit indicator against appropriate independent revenue/cost/asset benchmarks (art. 22).
- Profit split: allocate combined controlled profit using economically supported contributions, including functions, risks and assets (art. 23).
- Another method only where the listed methods are inappropriate, with reasons (art. 24).

Use internal or public external comparables; document product/service characteristics, contracts, market conditions, strategy, risks and functions. Make reasonable reliable comparability adjustments where needed (arts. 16-17). Derive the 25th-75th percentile range; if the tested result is outside it, the rulebook uses the median. The examples assume benchmark statistics have already been properly established; no illustrative margin is a statutory safe harbour.

**Financing:** apply art. 13 independently of the art. 12-b exclusions: excessive related-party borrowing interest is disallowed and lending interest is brought to at least the comparable independent rate at origination, based on domestic/international financial-market evidence. [Profit Rulebook art. 4][profit-rules] independently prescribes matching-maturity **EURIBOR (FX) or SKIBOR (MKD) plus one percentage point** when the unrelated-party origination-rate evidence is absent: a borrowing deduction ceiling and a lending-income floor. This is the corporate rulebook rule, not the PIT provision imported by analogy. Related-party default interest is disallowed under art. 14. Separately test art. 15's 20% nonresident shareholder and three-times-equity thin-capitalisation rule, including covered guarantees, its first-three-operating-years exception and financial-shareholder exception. Do not disallow the same amount twice; reconcile statutory grounds to a single adjustment ledger.

**Sole traders:** [PIT art. 27(7)-(8)][pit] has its own excessive interest and nonmarket related-party adjustment. It prescribes comparable domestic/foreign market prices, or cost plus ordinary profit if that comparison is not possible. For loan interest, art. 27(7) uses comparable commercial-bank credit evidence; if that is not substantiated, deduction is capped at matching-maturity **EURIBOR for foreign-currency loans or SKIBOR for MKD loans plus one percentage point**. Obtain the actual benchmark and period calculation, not a hard-coded rate. Do not import the 300 million corporate exclusion into PIT.

**Documentation:** [Rulebook arts. 2-12][tp] full report contains master file, local file and annexes. Include ownership and location, group business/value chain, intangibles and financing, financial/tax positions, local management/activity, transaction descriptions and agreements, amounts/counterparties, functional/risk analysis, selected method, comparables/search, calculations and reconciliation to annual accounts. Annex group/local financial statements, relevant contracts, pricing agreements/rulings and benchmark evidence. Art. 13 shortened report identifies each transaction category, value and related counterparty. Maintain evidence supporting the tax-return figure even when the shortened form applies.

## Deadlines and filing

Prepare and keep the report for the covered tax year. [Profit Tax Law art. 39(5)][cit] requires **P/TC** related-transaction information with the **DB** return where TP-report obligations apply. DB follows the annual-account deadline: end of February next year or 15 March where the annual account is filed electronically ([UJP filing instructions][cit-filing]). Apply the nonworking-day rule. For 2026 activity, filing is in 2027; the cited 2026 announcement is evidence of the recurring rule, not a special 2027 extension.

The current art. 12-a is a **prepare-and-retain / on-request** regime. Do not use a superseded blanket 30 September annual report-submission date. UJP can request the report after 30 days from the DB deadline; respond within 15 days of receipt. Retain for ten years from covered year-end. The annual corporate balance is due within 30 days after the annual-account deadline under art. 41; include the TP adjustment in that calculation, rather than treating report delivery as a tax-payment extension. Company cessation/reorganisation does not erase the records or adjustment for the final period.

## Penalties and interest

[Profit Tax Law art. 46][cit] failure to retain/deliver reports or submit the form on time attracts legal-person ranges micro **EUR 300-1,000**, small **600-2,000**, medium **1,800-6,000**, large **3,000-10,000**, in MKD equivalent; responsible-person ranges respectively **EUR 50-250**, **100-500**, **150-500**, **200-500**. Art. 43 separately covers inaccurate data reducing the base, with higher company ranges **EUR 600-2,000**, **1,200-4,000**, **3,600-12,000**, **6,000-20,000**. [Tax Procedure Law art. 123][procedure] interest is 0.03% daily from the day after the underlying tax matured. Do not confuse an adjustment, a fine and interest.

## Cross-border points

A cross-border transaction does not by itself establish related status; apply art. 16. Conversely the low-tax relationship test can capture dealings without a shareholding link. Check treaty associated-enterprise, corresponding-adjustment and mutual-agreement articles before seeking bilateral relief; this skill does not grant an automatic foreign corresponding deduction. WHT and VAT apply separately to the same fee/royalty/interest. Preserve the treaty version and application dates using the cross-border skill; an arm's-length result alone does not establish a treaty exemption.

## Two worked examples that recompute

**Simple: excessive purchase price.** A company above the 300 million revenue exclusion buys 100 units from a foreign related party at 1,200 each. A properly established comparable independent price is 1,000. Art. 12 disallows 20,000 expense; incremental tax is 2,000 at 10%. Assumed prices are facts of the illustration, not official price benchmarks.

```oa-check
name: MK 2026 CUP expense adjustment
inputs:
  units: 100
  actual_price: 1200
  comparable_price: 1000
steps:
  - actual_cost: units * actual_price
  - allowable_cost: units * comparable_price
  - adjustment: max(0, actual_cost - allowable_cost)
  - extra_tax: adjustment * 0.10
expected:
  actual_cost: 120000
  allowable_cost: 100000
  adjustment: 20000
  extra_tax: 2000
```

**Edge: cost-plus result outside the accepted range.** The same in-scope status is assumed. Eligible costs are 800,000 and actual related-party service revenue 816,000, a 2% markup. The evidenced comparable interquartile range is 5%-9%, with median 7%. Outside the range, Rulebook art. 16 uses the median: arm's-length revenue 856,000, uplift 40,000 and extra tax 4,000. The 7% is hypothetical benchmark evidence, not a legal safe harbour.

```oa-check
name: MK 2026 outside range median adjustment
inputs:
  costs: 800000
  actual_revenue: 816000
  median_markup: 0.07
steps:
  - actual_markup: (actual_revenue - costs) / costs
  - benchmark_revenue: costs * (1 + median_markup)
  - adjustment: max(0, benchmark_revenue - actual_revenue)
  - extra_tax: adjustment * 0.10
expected:
  actual_markup: 0.02
  benchmark_revenue: 856000
  adjustment: 40000
  extra_tax: 4000
```

## Ask the client first

- What are annual total revenue, all ownership/control/family links and counterparty residences?
- What transactions and annual aggregates exist, including loans/guarantees and intangible rights?
- Which functions, risks, assets, contracts and independent comparables support the method?
- Have financing, hidden-distribution, WHT and VAT adjustments already been recorded?
- What DB/P/TC deadlines, retained files and UJP requests apply?

## Sources

| Official source | URL | Read on |
|---|---|---|
| Profit Tax implementing rulebook, art. 4 | https://www.ujp.gov.mk/files/attachment/0000/0990/______________________________________________________________________________________________________________________________________________.pdf | 2026-10-24 |
| Profit Tax Law, consolidated through Gazette 199/2023 | https://www.ujp.gov.mk/files/attachment/0000/0965/Zakon_za_danok_na_dobivka_199_2023.pdf | 2026-10-24; 2026-10-30 (web.archive.org copy, UJP site offline) |
| Personal Income Tax Law, consolidated through Gazette 274/2022 | https://www.ujp.gov.mk/files/attachment/0000/1466/ZAKON_ZA_DANOKOT_NA_LICEN_DOHOD_-_Azuriran_so_Sl.vesnik____274___od_20.12.2022.pdf | 2026-10-24; 2026-10-30 (web.archive.org copy, UJP site offline) |
| Transfer Pricing Rulebook, Gazette 59/2019 | https://www.ujp.gov.mk/files/attachment/0000/1155/Plavilnik_za_transferni_ceni_59-2019.pdf | 2026-10-24; 2026-10-30 (web.archive.org copy, UJP site offline) |
| Tax Procedure Law, through Gazette 3/2025 | https://www.ujp.gov.mk/files/attachment/0000/0900/_________________________.pdf | 2026-10-24; 2026-10-30 (web.archive.org copy, UJP site offline) |
| UJP, 25 February 2026 DB/DB-VP filing instructions (2025 returns filed in 2026) | https://www.ujp.gov.mk/mk/javnost/soopstenija/pogledni/1204 | 2026-10-24 |

[profit-rules]: https://www.ujp.gov.mk/files/attachment/0000/0990/______________________________________________________________________________________________________________________________________________.pdf
[cit]: https://www.ujp.gov.mk/files/attachment/0000/0965/Zakon_za_danok_na_dobivka_199_2023.pdf
[pit]: https://www.ujp.gov.mk/files/attachment/0000/1466/ZAKON_ZA_DANOKOT_NA_LICEN_DOHOD_-_Azuriran_so_Sl.vesnik____274___od_20.12.2022.pdf
[tp]: https://www.ujp.gov.mk/files/attachment/0000/1155/Plavilnik_za_transferni_ceni_59-2019.pdf
[procedure]: https://www.ujp.gov.mk/files/attachment/0000/0900/_________________________.pdf
[cit-filing]: https://www.ujp.gov.mk/mk/javnost/soopstenija/pogledni/1204

Not yet confirmed: None within the stated scope.

