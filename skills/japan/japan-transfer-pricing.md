---
name: japan-transfer-pricing
description: Use this skill whenever asked about Japan transfer pricing rules, documentation requirements, or 移転価格税制 compliance. Trigger on phrases like "transfer pricing Japan", "Japanese TP documentation", "移転価格", "master file Japan", "local file Japan", "CbCR Japan", "APA Japan", "Article 66-4 ASMT", "NTA transfer pricing", or any question about intercompany pricing for Japanese entities.
version: 1.1
jurisdiction: JP
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - transfer-pricing-workflow-base
category: transfer-pricing
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
status: needs_sources
domain: transfer-pricing
type: computation
---

# Japan Transfer Pricing

> **General reference only.** This skill produces working papers for professional review. It has not been approved by an accountant for any particular person, entity, election or filing. Confirm the applicable facts and official forms before filing, paying or taking a position.

## Scope

2026 Japanese corporate foreign-related-party pricing and documentation under Special Measures Act art.66-4. Prepare a relationship/transaction inventory, functional and comparability analysis, arm's-length computation, documentation obligations and filing handoff. This is not an APA or accountant approval. PE attribution, interest limitations, customs/consumption-tax effects and Pillar Two require separate analyses.

Quick reference: the local-file test is gross transactions with each foreign related party, including services and intangibles, not tangible goods alone. Exactly JPY 5,000,000,000 aggregate transactions or JPY 300,000,000 intangible transactions triggers contemporaneous documentation. Master File/CbCR have a separate consolidated-revenue test. Source: Special Measures Act art.66-4(6)-(7), https://laws.e-gov.go.jp/law/332AC0000000026; NTA FAQ66-72, https://www.nta.go.jp/taxes/shiraberu/kokusai/takokuseki/pdf/04.pdf.

## Ask the client first

- Entity, fiscal year and direct/indirect ownership/control relationships, including foreign entities and PEs.
- Counterparty-by-counterparty prior-year gross receipts/payments and intangible components; current year if no prior year.
- Contracts, actual conduct, functions, assets, risks, cost allocation and segmented accounts.
- Group ultimate parent, residence, fiscal year, preceding consolidated revenue and reporting-entity/exchange arrangements.
- Existing local/master files, CbCR/parent notification, APA/MAP, audits and outstanding information requests.
- Method, tested party, comparables and material transaction/market changes.

## The method, step by step

### Identify covered relationships and price at arm's length

The statutory foreign-related-party definition includes direct/indirect ownership at least 50% and other prescribed special relationships; do not stop at a direct-shareholding test. Identify sales, purchases, services, loans, guarantees, licences, other intangible rights and actual controlled transactions. If receipts are below or payments above arm's length, art.66-4 can increase Japanese taxable income. Documentation exemption does not exempt the pricing rule. Source: Special Measures Act art.66-4(1), https://laws.e-gov.go.jp/law/332AC0000000026 (50% in words on the page).

Select the most appropriate method for the transaction and parties' functions/circumstances. CUP compares a properly adjusted uncontrolled price; resale price backs out an arm's-length gross profit from resale; cost plus adds an arm's-length gross profit to the relevant cost. Other authorized methods include transactional net margin and profit-split methods, including residual profit split; valuation of hard-to-value intangibles may require DCF and special statutory analysis. Do not invent a method hierarchy or assume a group's global margin is the Japanese result. Source: Special Measures Act art.66-4(2), https://laws.e-gov.go.jp/law/332AC0000000026; obtain the applicable implementing provisions for a non-basic method before executing it.

Reconcile contractual form to actual conduct, identify functions/assets/risk control and segment accounts. Record comparable search, adjustments, financial data dates and reasons for rejecting alternatives. Explain each allocation key. Compute actual versus arm's-length profit, map any adjustment to the Japanese tax computation and check treaty corresponding relief/MAP. An example markup below is an assumed benchmark, not a statutory safe harbour.

### Determine the documentation obligations

| Obligation | Threshold/condition, timing and exception | Official source |
|---|---|---|
| Contemporaneous local file | Each foreign related party: preceding-year gross consideration receipts plus payments at least JPY 5,000,000,000 OR intangible consideration at least JPY 300,000,000; all transactions, including services, not just tangibles; use current year where no preceding year ; monetary amounts derived from Japanese 万/億 units | Special Measures Act art.66-4(6)-(7); NTA FAQ66,70-72, https://www.nta.go.jp/taxes/shiraberu/kokusai/takokuseki/pdf/04.pdf |
| Local-file exemption | Both gross aggregate below JPY 5,000,000,000 AND intangible aggregate below JPY 300,000,000, subject to statutory no-prior-transaction rules; no netting receivables/payables and include APA-covered transactions ; monetary amounts derived from Japanese 万/億 units | same, https://www.nta.go.jp/taxes/shiraberu/kokusai/takokuseki/pdf/04.pdf |
| Local-file preparation | By the actual final corporate-return due date, including valid extension; keep latest information available at transaction/filing | NTA FAQ66,68; https://www.nta.go.jp/taxes/shiraberu/kokusai/takokuseki/pdf/04.pdf |
| Local-file retention | Ordinarily 7 years in Japan; loss-year documents generally 10 years, historical 9-year exception; establish correct period | NTA FAQ66; https://www.nta.go.jp/taxes/shiraberu/kokusai/takokuseki/pdf/04.pdf |
| Requested contemporaneous local file | Examiner's appointed day no later than 45 days from request; not a guaranteed grace period | Special Measures Act art.66-4; NTA FAQ85-91, https://www.nta.go.jp/taxes/shiraberu/kokusai/takokuseki/pdf/04.pdf |
| Other important documents and exempt-transaction equivalent file | Examiner's appointed day no later than 60 days from request; applies also to important underlying/related documents for covered transactions | same, https://www.nta.go.jp/taxes/shiraberu/kokusai/takokuseki/pdf/04.pdf |
| Master File | Specified multinational group preceding consolidated total revenue at least JPY 100,000,000,000; applicable Japanese constituent entity/PE supplies within 1 year after ultimate-parent year-end; Japanese or English ; monetary amounts derived from Japanese 万/億 units | Special Measures Act art.66-4-5; NTA FAQ1-10,60-65, https://www.nta.go.jp/taxes/shiraberu/kokusai/takokuseki/pdf/04.pdf |
| CbCR | Same specified-group revenue boundary; determine ultimate/surrogate parent and any secondary filing obligation or exchange-based relief; English, e-Tax, within 1 year after ultimate-parent year-end | Special Measures Act art.66-4-4; NTA FAQ12-59, https://www.nta.go.jp/taxes/shiraberu/kokusai/takokuseki/pdf/04.pdf |
| Ultimate-parent notification | Japanese constituent entity/PE in the specified group identifies ultimate/surrogate parent by the last day of the ultimate-parent reporting year; designated joint submission can avoid duplicative notices | NTA FAQ1-10, https://www.nta.go.jp/taxes/shiraberu/kokusai/takokuseki/pdf/04.pdf |

The official FAQ expresses the group threshold as 1,000億円; the JPY 100,000,000,000 rendering above is derived by decimal-unit conversion. Do not replace the Japanese statutory threshold with an approximate EUR figure. For shortened parent years and overseas currency thresholds, use the FAQ's special analysis instead of blindly annualising every Japanese figure.

Prepare the local file in usable form; foreign-language material can require Japanese translation. Master File may be Japanese or English; CbCR is in English. Use e-Tax's multinational reporting procedures and designated forms for group information, not an ordinary attachment labelled TP file. The annual return also discloses relevant foreign-related-party information in the applicable 別表17(4); reconcile it to the transaction inventory. Source: NTA documentation FAQ and Special Measures Act art.66-4.

### APA, safe-harbour and cross-border boundaries

Use NTA pre-filing consultation for an APA; decide unilateral versus treaty-supported bilateral/multilateral treatment with a specialist. The NTA application is 独立企業間価格の算定方法等の確認に関する申出書 (prescribed form), submitted by the first day of the first proposed covered year (if that day is a Sunday, national/general holiday or a day specified in General Tax Enforcement Order art.2(2), submission is allowed by the following day under guidance6-2(2), including the applicable non-business-day extension), with functional, method, financial and critical-assumption evidence. The covered period is in principle 3–5 business years under guidance6-7. Comply with agreed annual reporting and any approved rollback; no outcome or processing-time promise. Source: NTA transfer-pricing administrative guidance chapter6, https://www.nta.go.jp/law/jimu-unei/hojin/010601/05.htm.

Japan's official Amount B FAQ says the simplified and streamlined approach is not implemented for the time being. An overseas subsidiary's adoption does not make its margin automatically valid in Japan; retain a traditional Japanese arm's-length analysis and assess double-tax/MAP implications. Source: NTA Amount B FAQ1-5, https://www.nta.go.jp/taxes/shiraberu/kokusai/pdf/0025006-011.pdf. Do not assert that the OECD low-value-service approach is an unconditional Japanese statutory safe harbour.

## Boundary and exception table

| Boundary | Action |
|---|---|
| Below documentation threshold | Prepare support anyway; requested equivalent documents and the arm's-length rule still apply |
| Net-settled transactions | Add gross receipts and payments before comparing thresholds; NTA FAQ70, https://www.nta.go.jp/taxes/shiraberu/kokusai/takokuseki/pdf/04.pdf |
| Management fee labelled service | Determine whether its substance includes an intangible licence/transfer; NTA FAQ71, https://www.nta.go.jp/taxes/shiraberu/kokusai/takokuseki/pdf/04.pdf |
| Document errors or missing material | Correct by the appointed deadline; inaccurate records may not constitute submission; NTA FAQ87, https://www.nta.go.jp/taxes/shiraberu/kokusai/takokuseki/pdf/04.pdf |
| Non-submission | Can trigger estimation and comparable-business inquiries under art.66-4; ordinary tax, additions and interest may follow an adjustment |
| Master File/CbCR failure ; monetary amounts derived from Japanese 万/億 units | Without justifiable reason, applicable reporting failures can attract a fine up to JPY 300,000; distinguish the statutory offence from automatic late charges; NTA FAQ reporting-penalty discussion, https://www.nta.go.jp/taxes/shiraberu/kokusai/takokuseki/pdf/04.pdf |
| NUPE/parent notice | Do not assume every late notification has the same JPY 300,000 penalty; obtain the exact operative offence before stating a fine |

## Worked cases

A hypothetical counterparty receives goods JPY 2,800,000,000, supplies goods/services JPY 1,950,000,000 and receives royalties JPY 300,000,000. Gross aggregate is JPY 5,050,000,000 including the royalty, so the total test triggers. Intangible transactions also meet the boundary exactly. Net cash settlement of JPY 850,000,000 for the goods/services does not change either test.

```oa-check
name: Gross consideration and exact intangible boundary both trigger local-file preparation
inputs:
  receipts: 2800000000
  payments: 1950000000
  royalty: 300000000
steps:
  - gross_total: receipts + payments + royalty
  - excess_total: gross_total - 5000000000
  - intangible_excess: royalty - 300000000
  - goods_services_net: receipts - payments
expected:
  gross_total: 5050000000
  excess_total: 50000000
  intangible_excess: 0
  goods_services_net: 850000000
```

For a hypothetical independently supported cost-plus method, qualifying cost is JPY 100,000,000 and the arm's-length markup is 8%. Appropriate revenue is JPY 108,000,000. Actual related-party revenue is JPY 104,000,000, leaving a JPY 4,000,000 potential upward income adjustment before other relevant facts. This 8% is an example assumption, never a Japanese safe-harbour rate.

```oa-check
name: Cost-plus comparison quantifies potential Japanese income adjustment
inputs:
  supported_cost: 100000000
  assumed_markup_percent: 8
  actual_revenue: 104000000
steps:
  - benchmark_revenue: supported_cost * (1 + assumed_markup_percent / 100)
  - actual_profit: actual_revenue - supported_cost
  - benchmark_profit: benchmark_revenue - supported_cost
  - potential_upward_adjustment: max(benchmark_revenue - actual_revenue, 0)
expected:
  benchmark_revenue: 108000000
  actual_profit: 4000000
  benchmark_profit: 8000000
  potential_upward_adjustment: 4000000
```

## When to refuse or refer

Do not certify arm's-length pricing from one financial ratio, net transactions to avoid documentation, treat a threshold as tax exemption, or claim an automatic right to the full 45/60-day maximum. Refer missing comparables, intangibles/DCF, restructuring, financing, PE attribution, APA/MAP and conflicting foreign adjustments. Do not use untested secret-comparable rhetoric as a computation method for the taxpayer.

## Filing and payment

Maintain a local-file index and return-schedule reconciliation; confirm the actual corporate return deadline. Submit parent notification, Master File and CbCR through the applicable e-Tax multinational-information forms, retaining accepted-data receipts. A group parent filing may relieve duplicate local CbCR only when the statutory/exchange conditions actually hold. Respond to each audit request by its appointed date, record corrections and preserve a copy of the submitted evidence.

## Completion checklist

Relationships and gross flows complete; both thresholds tested per party; method/segmentation/comparables documented; local-file preparation/retention scheduled; group revenue and reporting role established; e-Tax notifications/reports accepted; information-request deadlines and any APA obligations tracked; tax/customs/consumption/interest-limit interactions referred.

## Sources

| Source | URL | Read on |
|---|---|---|
| Special Measures Act; Read for art.66-4 relationship, pricing, documentation exemption and requests; arts.66-4-4 and 66-4-5 reporting | https://laws.e-gov.go.jp/law/332AC0000000026 | 2026-11-14 |
| NTA documentation FAQ; Read for introductory table; questions1-10,12-19, reporting/penalty sections,60-91 including exact thresholds, retention and deadline exceptions | https://www.nta.go.jp/taxes/shiraberu/kokusai/takokuseki/pdf/04.pdf | 2026-11-14 |
| NTA TP administrative guidance; Read for chapter6 pre-consultation, application, evidence, critical assumptions and compliance reporting | https://www.nta.go.jp/law/jimu-unei/hojin/010601/05.htm | 2026-11-14 |
| NTA Amount B FAQ; Read for questions1-5 domestic non-adoption, foreign use and documentation/MAP consequences | https://www.nta.go.jp/taxes/shiraberu/kokusai/pdf/0025006-011.pdf | 2026-11-14 |

Not yet confirmed: Precise implementing-rule criteria for DCF/HTVI, TNMM and residual profit split and all loan/thin-cap details; generic 35%-40% concealment penalty; alleged automatic JPY 300,000 late NUPE penalty; unconditional APA duration guarantee, no-fee claim, 12-36-month timelines and 130-150 annual statistics; blanket service safe harbour and immateriality discretion; unsupported dated digital-economy/Pillar Two implementation assertions. These legacy topics are retained as referral boundaries or excluded numerical claims, not usable rates or guaranteed concessions.
