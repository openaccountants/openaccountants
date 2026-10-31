---
name: li-transfer-pricing
description: >
  Prepare 2026 Liechtenstein related-party and permanent-establishment pricing
  workpapers. Use for the arm's-length rule, connected persons, method selection,
  Master File and Local File screening, the separate company-size route, transaction
  thresholds, documentation requests and reconciliation to corporate taxable profit.
  Read the actual Tax Act, Tax Ordinance and company-size cross-reference before
  treating a documentation threshold as an exemption. This Guide distinguishes
  formal documentation from the residual evidence duty. It does not supply a
  benchmark, approved margin, complete CbCR method, APA, dispute outcome or an
  accountant's approval. All example prices, margins and transaction facts are
  assumptions requiring separate evidence.
jurisdiction: LI
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.2
---

# Liechtenstein transfer pricing v0.2

Independent source/editorial review evidence and correction status are in the [dated whole-pack review record](../../../docs/research/2026-10-24-liechtenstein-pack-review.md). Apply its exact revision and scope limits. Named Liechtenstein accountant review remains open.

## Who this applies to

SteG article 49 requires related-party and PE dealings to use conditions that independent parties would agree in comparable circumstances, and documentation for material transactions. SteV article 31b implements the methods and evidence routes. These are Liechtenstein rules; no Swiss documentation exemption is imported. This source-cited draft supplies preparation, not an accepted benchmark or complete TP coverage. [Tax Act][law]; [Tax Ordinance][ordinance]

## Related persons and transaction record

SteV article 31a includes direct/indirect participation or beneficial interests in either direction, organs, close personal relationships (including family/friendship), their stated connections and connected participations. Its reach is broader than one percentage test. Article 31b(7)'s at-least-25% participation/benefit condition applies to the formal-documentation duty under paragraphs 2–6 for the relationships in article 31a(a) and (c); it does not erase the residual evidence duty in paragraph 8. Retain the exact relationship and direct/indirect chain, not only an ownership percentage. [SteV, articles 31a–31b][ordinance]

Create a transaction register by party/PE, country, relationship, category, year, amount, currency, contract, invoicing, actual conduct and accounting line. Record functions, risks, assets, personnel/control, value chain and any PE allocation. Reconcile gross flows before testing thresholds; do not net opposite payments or unrelated categories to manufacture a smaller amount. The treatment of an unusual aggregation/currency/period case still needs specific confirmation.

## Choose the documentation route

All thresholds below are from current SteV article 31b. “More than” and “exceeds” are strict; an equal amount does not itself cross that particular threshold. This does not exempt the transaction from arm's-length pricing or paragraph 8 evidence.

| Route | Entry gate | Cross-border transaction threshold and content |
|---|---|---|
| Article 31b(2)–(3) | Part of a group with consolidated turnover **more than CHF 900 million** | OECD Master File and Local File; goods purchases/sales **over CHF 1 million** per connected party/PE/year, or other expenses/income **over CHF 250,000** per expense/income category, party/PE/year |
| Article 31b(4)–(5) | Outside the above group route but exceeding **all** size criteria referenced in PGR article 1064(2) | Specified company/business/structure description, relationship register, functions/risks/assets, reasoned method selection and pricing/arm's-length analyses; goods **over CHF 500,000**, other expenses/income **over CHF 125,000**, on the stated party/category/year bases |
| Article 31b(8) | Transactions/relationships not captured by paragraphs 2–5 and 7 | Suitable evidence of arm's-length compliance on authority request; no blanket small-company or domestic-transaction exemption |

The PGR article 1064(2) criteria currently state CHF 32.4 million balance sheet, CHF 64.8 million net sales and 250 average employees. PGR company classification ordinarily uses two of three, whereas SteV's formal-documentation cross-reference expressly says **all** criteria. Do not replace the latter with the generic “large company” label. PGR article 1064(4) also has a two-consecutive-balance-date rule and an initial-application rule; article 1064(5) addresses other reporting currencies. Retain both years, initial-application and currency evidence and confirm any contested interaction before deciding a formal-duty exemption. [PGR, article 1064, current 1 September 2026 consolidation][pgr]; [SteV, article 31b(4)][ordinance]

For the formal files under paragraphs 2–5, paragraph 6 requires submission **within 60 days of request**, in **German or English**. It is a request deadline, not an invented annual automatic filing date. Record receipt, scope, due date and submitted version. The CHF 900 million TP group screen is not established here as a CbCR threshold: separate reporting law, filer roles, schema and exchange conditions require separate verification. [SteV, article 31b(6)][ordinance]

## Method and workpaper

Article 31b(1) applies the current OECD TP Guidelines and requires the most suitable method for the actual transaction facts. It lists CUP, resale price, cost plus, TNMM and profit split; another method is permitted if the listed methods cannot suitably represent the arm's-length result. Do not select a method merely because a markup is easy to compute. [SteV, article 31b(1)][ordinance]

1. Delineate what the parties actually did and identify comparable circumstances, tested transactions, functions, risks and assets.
2. Explain the selected method and rejected alternatives, data reliability, comparability adjustments and limitations. Preserve the underlying search/financial evidence. This draft supplies no local benchmark or safe-harbour margin.
3. Reconcile the method's base and profit measure to the accounts. A gross cost-plus markup on cost is different from a net return on cost or profit as a percentage of sales; the example below illustrates the denominator distinction only.
4. Reconcile any proposed adjustment to SteG article 49 and corporate income, with the actual tax, loss, equity-deduction and foreign/treaty implications separately assessed. A ledger correction is not an agreed corresponding adjustment abroad.
5. Retain contracts, evidence, calculations, file contents, approval/authority communications and the annual refresh record. Actual CbCR, country reporting and any specialist transactions remain separate.

## Requests, disputes and sanctions

SteG article 135 provides fines for intentional/negligent noncompliance after a reminder, with the stated ordinary and serious/repeat maxima. It is not a specific automatic TP file fine. Incorrect profit, tax evasion and procedural noncompliance have different legal bases. Do not calculate a penalty or treat 60 days as extended without an actual authority decision. [SteG, articles 49 and 135][law]

SteG article 63 addresses treaty/reciprocity relief and specified corresponding adjustments. Articles 124a and the actual foreign finality/treaty facts need separate review before seeking a change to a final assessment. This draft does not promise double-tax relief, an APA, a MAP result or an accepted transfer-price range.

## Worked controls

### Same-party goods aggregation in the assumed Master/Local route

Assume the group route, qualifying relationship and cross-border goods purchases from one party in one year are established. Two purchases of CHF 600,000 and CHF 500,000 total CHF 1.1 million, over the CHF 1 million threshold. No other party/category is included.

```oa-check
name: Liechtenstein assumed group route goods threshold
inputs:
  first_goods_purchase: 600000
  second_goods_purchase: 500000
  established_route_threshold: 1000000
steps:
  party_year_purchases: first_goods_purchase + second_goods_purchase
  excess_over_threshold: party_year_purchases - established_route_threshold
expected:
  party_year_purchases: 1100000
  excess_over_threshold: 100000
```

### Separate-size route category aggregation

Assume the separate-size route and relationship conditions are established, with two cross-border service expenses in the same category to one party, CHF 80,000 and CHF 60,000. CHF 140,000 exceeds CHF 125,000 by CHF 15,000. This does not establish the company-size or relationship gates.

```oa-check
name: Liechtenstein assumed separate size route service category
inputs:
  first_category_expense: 80000
  second_category_expense: 60000
  established_route_threshold: 125000
steps:
  party_category_year_total: first_category_expense + second_category_expense
  excess_over_threshold: party_category_year_total - established_route_threshold
expected:
  party_category_year_total: 140000
  excess_over_threshold: 15000
```

### Gross cost-plus is not margin on sales

Assume an independently supported gross cost-plus method, CHF 100,000 eligible cost and 8% markup solely for the case. Gross profit is CHF 8,000, revenue CHF 108,000 and profit/revenue approximately 7.407407%. Neither percentage is a Liechtenstein safe harbour; no TNMM benchmark is inferred.

```oa-check
name: Liechtenstein assumed gross cost plus denominator control
inputs:
  established_cost_base: 100000
  assumed_supported_markup: 0.08
steps:
  gross_profit: established_cost_base * assumed_supported_markup
  transaction_revenue: established_cost_base + gross_profit
  profit_as_percent_of_sales: gross_profit / transaction_revenue * 100
expected:
  gross_profit: 8000
  transaction_revenue: 108000
  profit_as_percent_of_sales: 7.407407407407407
```

## Ask and refer

Obtain the full group/benefit/relationship chart, turnover and consolidation evidence, both years' company-size data, currency, all party/category transactions, PE facts and actual authority requests. Require the functions/risks/assets record, method/comparable support and accounts reconciliation. Refer financing, guarantees, intangibles, restructurings, PE allocation, contested aggregation/size tests, CbCR, advance agreements and cross-border disputes. Full legal/application and named local accountant review remain open; TP coverage is partial.

## Sources

Read 24 October 2026, from direct official consolidated PDF text:

- [SteG, current 1 July 2026 consolidation][law], selected articles 49, 63, 124a and 135. The adjustment/finality procedure is flagged for further reconciliation, not completed here.
- [SteV, current 1 July 2026 consolidation][ordinance], full articles 31a–31b. Older search-index versions are not substituted for this text.
- [PGR, current 1 September 2026 consolidation][pgr], article 1064 only for the size cross-reference; whole-statute retrieval is not whole-statute verification.

[law]: https://www.gesetze.li/konso/pdf/2010340000
[ordinance]: https://www.gesetze.li/konso/pdf/2010437000
[pgr]: https://www.gesetze.li/konso/pdf/1926004000

<!-- openaccountants-cta-block -->

---

## Talk to an accountant

Find the current Guide and professional-review status at [OpenAccountants](https://www.openaccountants.com).
