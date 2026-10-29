---
name: am-transfer-pricing
description: "Prepare Armenia transfer-pricing workpapers for 2026: identify related persons, controlled cross-border and specified domestic transactions, separate the annual regulation and notification thresholds, select a supported pricing method, calculate a range and reconcile adjustments. Covers local/master documentation, the statutory country-reporting trigger, notification form structure, deadlines and sanctions. Includes two reproducible examples and preserved supplementary research controls for aggregation, CUP, cost-plus, resale, net margin, financing and missing documentation. Use for Armenian related-party pricing, permanent-establishment allocations, market margins and controlled-transaction notices. Supplies the actual local/master documentation and country-report forms, contents, reporting-entity notice, currencies, languages and delivery clocks. Specialist transactions, large-group statutory/order scope mismatches, remedies, actual portal acceptance and independent accountant review remain separate boundaries. Checked against the law."
version: 0.2
jurisdiction: AM
tax_year: 2026
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: transfer-pricing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Armenia transfer-pricing preparation v0.2

## Who this applies to

Use this method for the 2026 tax year after identifying the taxpayer, actual transactions and applicable law. Chapter 73 addresses profit tax and natural-resource utilisation royalty. It does not supply a general VAT valuation adjustment. Article 360(3) excludes transactions with the stated public/local bodies, Central Bank, regulated tariffs and transactions with tax-base peculiarities prescribed by ratified treaties. Test exclusions before aggregating. [Code Articles 360–363][code]

Article 362 covers direct/indirect participation of at least 20% and practical control, including common control. Ownership alone is insufficient screening: also check voting rights/board formation, financing or guarantees exceeding 51% of opening assets, the specified more-than-80% income/expense dependencies with their exclusions, joint activity, gratuitous use and actual management. Record the exact limb, percentage denominator and measurement date. [Article 362][code]

Article 363 distinguishes related resident/nonresident transactions; specified **resident/resident** transactions where one party is a natural-resource royalty payer or enjoys the relevant profit-tax/royalty benefit; transactions with persons registered in a liberal-tax jurisdiction even without relatedness; and head-office/Armenian-PE dealings and expense allocation. Article 361's liberal-tax definition includes the stated 10%-or-lower/exemption tests, including person-specific regimes. Establish the counterparty's actual regime rather than making a country-name assumption. Specific regulated financial services in Article 363(5) are uncontrolled; this is not an exemption for every intercompany loan. [Articles 361–363][code]

**Translation check:** the English reproduction's Article 363(2) incorrectly repeats resident/nonresident wording. The Armenian text says related resident persons. Its Article 363(5) financial-services cross-reference also differs. Use the Armenian provision and actual underlying financial-service classification. The current consolidation includes later 2026 changes elsewhere; the English version is supporting translation, not a complete current-law substitute. [Armenian Code][code]; [English translation][english]

## Rates, bands and thresholds

| Item | Statutory amount/test | Period and source |
|---|---|---|
| Participation limb | At least 20%; practical control can apply independently | 2026, [362][code] |
| Chapter 73 annual application | All controlled transactions exceed AMD 200 million, excluding VAT, excise and environmental tax | 2026, [363(6)][code] |
| Annual notification | Exceeds AMD 200 million on its separate population, excluding Article 363(4) PE/head-office transactions | 2026, [375(1)][code] |
| Liberal-tax definition | Stated 10%-or-lower profit-tax rate or exemption, including qualifying person-specific regimes | 2026, [361(1)(5)][code] |
| Statutory country-report trigger | Parent organisation's prior-year gross revenue **exceeds** EUR 750 million | 2026 text, [376(1.1)(3)][code] |

The 200-million test is strict: equality does not exceed it. The general application and notification populations differ; do not remove PE/head-office transactions from both merely because Article 375 excludes them from notification. Loan principal/interest valuation, foreign-exchange dates, repeated balances and unusual transactions require classification under the Code and current instructions before aggregation. No blanket netting of sales against purchases. A proposal for a higher threshold or later deadline is not operative law verified here. [Articles 16, 363, 375][code]; [notification instructions][notice]

## The base

### Establish the transaction and method

Reconcile contracts with actual conduct, counterparties, ledger flows and segmentation. Article 373 gives actual transactions priority where their content differs from the contract. Prepare the Article 365 functions/assets/risks analysis, product/service/financing/intangible characteristics, contractual terms, market circumstances and business strategy. A comparability adjustment under Article 366 needs reliable information and an explanation of how it improves comparability. [Articles 365–366, 373][code]

Select the most appropriate method from CUP, resale price, cost-plus, transactional net margin and profit split. Use CUP when it and another method are equally reliable; internal comparables also take priority over external ones when equally reliable. More than one method is not mandatory. Select the simpler or more reliably benchmarked tested party for resale/cost-plus/net margin; a foreign tested party requires evidence, not automatic rejection. Do not use inaccessible tax-secret information as an undisclosed benchmark. [Articles 367–369][code]; [556-N points 3–15][methods]

| Method | Workpaper computation | Evidence needed |
|---|---|---|
| CUP | Comparable adjusted price × matched quantity | Actual comparability; a single comparable is sufficient only under the rule's full comparability conditions |
| Resale | Gross profit / net sales; implied purchase amount = sales × (1 − established margin) | Reseller functions, no material added value, consistent gross-cost classification |
| Cost-plus | Gross profit / relevant direct and indirect costs; remuneration = costs × (1 + established markup) | Consistent cost pool; do not substitute a sales margin for a cost markup |
| Net margin | Transaction-related net profit / appropriate costs, sales or assets | Segmented results, suitable denominator and accounting comparability; exclude unrelated income/expense |
| Profit split | Allocate established combined/residual profit on a supported economic basis | Highly integrated activities or valuable intangibles; no invented universal allocation percentage |

Sources: [Code Article 368][code]; [556-N method provisions][methods]. The example margins below are hypothetical already-supported benchmark inputs, not Armenian safe harbours or results of a real database search. Current-year data is the starting point; Article 370 permits its stated prior-year and up-to-three-prior-year circumstances. It does not prescribe a universal three-year weighted average for every taxpayer. Closely linked transactions can be combined under Article 372 when separate analysis is unreliable. [Articles 370, 372][code]

### Range and adjustment

853-N point 3 uses the full minimum–maximum range where all observations are reliable uncontrolled comparables. Where point 4's reliability condition applies after comparability adjustments, sort the observations, keeping duplicates as separate entries. For the lower/upper bounds calculate n × 0.25 / n × 0.75: an integer position uses the arithmetic mean of that observation and the next; a fractional position uses the observation at the next whole position. Do not substitute a spreadsheet's default percentile interpolation. The Code's median is the middle observation for odd n and the mean of the middle pair for even n. [853-N points 3–4][range]; [Article 361(1)(15)][code]

Article 371 permits authority adjustment of an out-of-range indicator to the median, with its stated burden of proof; the taxpayer must support a different proposed indicator. Article 364 deals with additional profit-tax base/reduction of tax loss and royalty base, and contains separate restrictions on recalculating reporting-period liabilities/advances and the domestic natural-resource-royalty case. Keep the pricing/base bridge separate from tax due, contractual settlements and corresponding relief. Do not apply a universal 18% multiplier or amend historic CIT/advance returns automatically. The separate current calculation and loss-sensitive reconciliation are set out below; they do not authorise automatic amendments of ordinary historic CIT/advance returns. [Articles 364, 371, 374][code]

### Separate pricing-to-tax calculation

Use SRC **Order 1032-N**, current consolidation **178495** incorporating 477-N, for the distinct TP tax calculation, including an adjusted calculation under Code article 374. It is different from the 671-N controlled-transaction notification. Start from the actual filed reporting-year income, deductions, taxable profit and profit tax. Identify the particular controlled transaction through the notification part/row reference in **field 27**; the current field was added from 15 June 2023. [1032-N annex and instructions 1–18, 28][tp-return]; [Code 54, 364, 374][code].

| Current form field | Reconciliation |
|---|---|
| 5 / 6 / 7 | Filed gross income / identified income addition / after-adjustment income = 5 + 6 |
| 8 / 9 / 10 | Filed deductions / identified deduction reduction / after-adjustment deductions = 8 − 9 |
| 11 / 12 / 13 | Filed taxable profit / adjustment = 6 + 9 / after-adjustment result = 7 − 10 |
| 14 / 15 | Applicable statutory rate / tax on the established adjusted taxable base |
| 16 / 17 | Profit tax already reported for the year / additional tax payable = 15 − 16 |
| 27 | Controlled-transaction notification part and row, keeping the adjustment tied to its transaction |

For the ordinary resident company under article 125(1), the rate is 18%, but article 105 defines its taxable profit as the **positive** income-minus-deductions difference. Therefore a pricing increase can reduce a tax loss without generating the same amount of immediate taxable profit. Reconcile the remaining loss and applicable loss use, rate, relief and original tax before populating fields 13–17; do not create a negative tax liability from a loss or charge 18% of every pricing difference. Where no other relief/deduction changes apply, the control is `new_tax = max(adjusted_income − adjusted_deductions, 0) × applicable_rate`, with additional TP tax equal to the new tax less the correctly established original tax. This is a qualified ordinary-company control, not a formula for every entity or natural-resource royalty. [Code 105(1), 125(1), 364][code]; [1032-N instructions 6–18][tp-return].

The royalty side separately records original/adjusted base, profit and rate in fields 18–25, with payable royalty in field 26 = 25 − 24. Its actual royalty-rate calculation and article 364's domestic resource-royalty exception need their own qualified facts; do not treat royalty as 18% corporation tax. Preserve the computation, filed-return evidence, transaction register and amended-loss reconciliation together. Submit the separate calculation electronically under article 53(5), subject to its express paper exceptions, and use article 54/374 for corrections. No taxpayer portal submission or accepted return is claimed. [Code 53–54, 364, 374][code]; [1032-N instructions 19–28][tp-return].

## Deadlines and filing

| Event | Statutory clock | Source |
|---|---|---|
| Controlled-transaction notification | By 20 April inclusive of the following tax year; for 2026, statutory date 20 April 2027 before any separately established extension/calendar rule | [375(3)][code] |
| Local/master information requested | 30 working days after receipt of written notification | [376(2)][code] |
| Additional requested information | 10 working days after receipt | [376(2)][code] |
| Requested interview arrangements | Provide venue/time/participant information within 5 working days after receipt | [376(2)][code] |
| Armenian translation requested for English/Russian documents | 10 working days after receipt | [376(3)][code] |
| Statutory country report | Within the 12 months immediately following each tax-year end | [376(2)][code] |
| Authority-study adjustment proposal | Submit the separate TP calculation, including a corrected calculation, within **one month** under article 374(2); do not substitute a thirty-working-day documentation clock | [374(2)][code] |

Notification, documentation and TP tax calculation are distinct outputs. Article 375 permits self-corrected notifications before receipt of the documentation request. If the authority detects wrong/missing transaction information, its notification and the taxpayer's corrected notification/objection have separate 10- and 30-working-day clocks. Both parties notify qualifying domestic transactions. Keep service/receipt proof and a working-day calendar; do not count every clock as ordinary calendar days. [375][code]

The actual 671-N notification consolidation incorporates 948-N amendments and is identified as applicable from 1 January 2026. Its instructions require **electronic-only** notification. Map identity/TIN/year/contact in Part 1, resident/nonresident selection in 1.1, nonresident controlled transactions in Part 2 and domestic controlled transactions in Part 5; both parts apply if both populations exist. Parts 2.1–2.4 and 5.1–5.4 collect goods/loans/intangibles/claim-transfer detail. Part 4 records internal uncontrolled transactions; Part 6 records activity codes and proportions. Loan supplementary fields distinguish opening/closing principal and payable interest, rather than treating all fields as a second transaction total. Amounts are AMD under the referenced Article 16 conversion rules. Actual login/schema, rounding, validation errors and accepted filing have not been tested. [671-N form and instructions, especially 1, 6.1, 14–18, 27–31, 35–45][notice]

### Build the statutory documentation package by actual filer

Current native 376(1.1) distinguishes these files; a local subsidiary does not become the group parent merely because its transactions exceed 200 million. The statutory parent definition requires direct/indirect management/control/capital participation sufficient to include at least one other member's financial statements in its consolidated statements. Record the consolidation perimeter, entity residence and prior-year revenue evidence before assigning a parent reporting obligation. [376(1.1)(2)–(3)][code]

| File and filer | Statutory contents and delivery |
|---|---|
|Local: all taxpayers notifying controlled transactions; SRC can also require it from a nonresident operating through an Armenian PE|Business functions and economic pricing factors; actual controlled transactions/comparability/functions-assets-risks; method and justification; counterparties/tax residence; uncontrolled-comparable information sources; range where applicable; tested-party financial/other necessary information. Link each transaction to its notification row, ledger segment, supporting agreement and adjustment workpaper. |
|Master: multinational group's parent|Group structure and activities; intangibles; financing with member organisations/foreign nonlegal entities; financial statements and general worldwide income/economic-activity information. This parent test differs from the local-notification gate. |
|Country report: multinational parent whose **prior-year gross revenue exceeds EUR 750 million**|Income allocation by country, taxes paid by country, economic activity by country and assets by country. Preserve the underlying year/revenue/consolidation evidence; equality is not “exceeds.” The country-report deadline is the 12 months immediately following the tax year, not the 30-working-day response-to-request clock. |

### Use the prescribed local, master and country-report instruments

The actual SRC instruments are **941-L (local)**, **942-L (master)** and **939-L (country report)**, all dated **9 September 2022**, linked on SRC's current transfer-pricing page. They are distinct from notification 671-N and adjustment calculation 1032-N. Order 939-L expressly starts **1 January 2024**. The signed instruments and complete annexes were read; no accepted electronic submission or automatic exchange is claimed. [941-L][localorder]; [942-L][masterorder]; [939-L][countryorder]

**Local file, 941-L Annex 2–3.** Apply the notified-taxpayer population and separately any written PE request. Prepare a free-form document with an indexed evidence package:

| Part | Required workpaper and reconciliation |
|---|---|
| Taxpayer organisation | Management/organisation chart; individuals receiving management reports and their usual work countries; business and strategy, current/prior-year restructuring or intangible transfers affecting it, and principal competitors. |
| Each controlled-transaction class | Actual transaction and context; counterparties, their relationship and tax residence; agreements; functions/assets/risks and changes; tested-party choice; selected method, reasons and rejected alternatives; material assumptions; comparable-search sources, search/selection steps and financial data; comparability adjustments and why reliable; range and reasons the result is arm's length. Explain multi-year data use rather than assuming it. Include relevant unilateral/bilateral/multilateral APAs or rulings involving other countries that affect the transaction. |
| Financial bridge | Reporting-year financial statements and schedules tying the financial inputs used in the pricing analysis to them; underlying financial data for the comparables. Tie the transaction to its ledger segment, notification row and any 1032-N adjustment once. |

The response is **electronic**, in Armenian, English or Russian, within **30 working days after receipt** of the written request. A requested Armenian translation has its own **10-working-day** clock. Additional information is due within **10 working days**, and written interview venue/time/participants information within **5 working days**, each from its respective notice. A prepared file is not an acknowledgement of delivery. [941-L Annex 4–6][localorder]; [376(2)–(3)][code]

**Master file, 942-L Annex 2–4.** Establish the Code 376 parent/consolidation test first. The order describes a **resident parent** with prior-year **consolidated group revenue not exceeding EUR 750 million** and routes an above-threshold resident parent to the country report. This is the order's express routing: Code 376(1.1)(2) itself states the parent master-file obligation without printing that revenue qualification, while 376(1.1)(3) states the parent organisation's prior-year **gross-income** threshold for the country report. Keep both statutory and order tests in the workpaper, including the parent's own and consolidated revenue, residence and actual request. Do not replace the statute with a new universal “no master file above EUR 750m” exemption or apply a parent's obligation to every Armenian subsidiary. A nonmatching large-group perimeter/revenue case needs specific authority before omitting a requested file. [376(1.1)][code]; [942-L Annex 2–3][masterorder]

For the order's ordinary resident-parent branch, supply the group ownership/legal chart and geography; business and profit drivers; supply chains for the five largest products/services and any others exceeding **5% of group turnover**; significant intragroup service arrangements, provider capability/location and cost-allocation/pricing policy; geographic markets, member contributions/functions/assets/risks and restructurings/acquisitions/divestments; intangible strategy, legal owners, significant agreements and transfers, countries and compensation; group financing, independent financing and central financing entities with residence/place of management; consolidated financial statements and relevant APAs/rulings on income allocation. The master document is free-form. Delivery, translation, additional-information and interview-information clocks are respectively **30/10/10/5 working days** from the relevant notice, with **electronic** Armenian/English/Russian delivery under Annex 5–7. [942-L Annex 4–7][masterorder]

**Country report, 939-L Annex 2–11 and Form 1.** Test the resident reporting parent and prior-year consolidated revenue **strictly above EUR 750 million**, alongside Code 376's statutory wording just described. The order also requires a **resident constituent entity to notify SRC of the reporting parent by 31 December of the reporting year**. That notification differs from the report due **within 12 months after the reporting year**. A local subsidiary does not automatically file the parent's report. [939-L Annex 2–3][countryorder]; [376(1.1)(3)/(2)][code]

Use the reporting group's consolidated reporting **currency**, identified in the form, with a consistent information basis and an explanation of source/method changes. Supply Form 1's three tables:

| Table | Required mapping |
|---|---|
| 1, country aggregates | Group name, reporting year and currency; each tax-residence jurisdiction, with the separate stateless line and treaty tie-breaker/registration fallback in Annex 9(1); related-party revenue, unrelated-party revenue and total, excluding the specified intragroup dividends; profit/loss before tax; income tax **paid** (including withholding paid on members' income) separately from current-year income tax **accrued but unpaid**; stated capital; accumulated earnings; average staff under the order's month-end method; year-end carrying amount of tangible assets excluding cash/equivalents, intangibles and financial assets. Do not substitute accrued tax for cash tax. |
| 2, constituent entities | Jurisdiction of tax residence; entity names; incorporation jurisdiction if different; all applicable principal activity boxes. Do not omit an entity merely because it has several activities or is a PE. |
| 3, explanations | Information sources, calculation method, source/method changes and other explanations needed to understand the reported amounts. |

Submit **electronically only**, in Armenian, Russian or English. Before an authority request, the reporting parent can correct the report under Annex 6; that is not a blanket right to overwrite an already requested report. Reconcile all tables and the notification to the consolidated perimeter, retain delivery evidence and distinguish these reporting mechanics from any separately established international exchange/surrogate obligation. [939-L Annex 4–11/Form 1][countryorder]

### File and settle the distinct adjustment

Keep a transaction-to-notification-to-1032-N bridge, the filing receipt and separate liability/account reconciliation. Code 53(7) uses the electronic system's receipt/registration notice as the filing date; preparing a form locally is not filing. Under 53(10), the ordinary period restrictions include a distinct **five-year TP** limit rather than the ordinary three years, with the specific TP checked-period exception. The liability-increasing/credit-reducing route in 53(10.1) qualifies those restrictions; do not turn five years into unconditional permission to revise any assessed amount. Article 54 permits the specified 374 TPcorrections, separately from correcting the 375 notification. [53–54/374–375][code]

Code 325 distinguishes self-declared unified-account settlement from liabilities raised by an inspection/administrative act, which use the administrative-act unified account. Each route prioritises pension obligations, then the statutory oldest-due ordering and principal/interest/fine order. Reconcile the actual assessed/self-declared amount and its account allocation; a bank payment into an account is not tax revenue until a liability is discharged. An intercompany cash settlement is not an authority tax payment or a foreign corresponding adjustment. The 374 interest branches below still govern and do not supply a new notification/documentation deadline. [325(1)–(8)/374][code]

## Penalties and interest

The current Armenian Article 402.1 provides organisation notification fines of AMD 1 million where prior-year gross income does not exceed AMD 1 billion, AMD 3 million for the over-1-billion band, and AMD 5 million for over AMD 2 billion. Read the upper band first. Wrong/missing information after the specified written correction process can attract AMD 500,000 per error/missing transaction under paragraphs 2–3; it is not an automatic charge for any innocent draft typo. [402.1][code]

Article 402.2 charges 10% of each documentation-subject controlled transaction's value for failure to provide documentation by the required deadline. If still not provided within 30 days after the fine is imposed, it provides 0.04% per overdue day on that transaction value. Do not confuse this with ordinary tax late-payment interest or recalculate its base as only the proposed TP adjustment. The exact service, first overdue day, assessed transaction population and procedural remedies need the actual notice/act. [402.2][code]

Article 401 ordinary tax late-payment interest is 0.075% a day, capped at 730 days under its stated scope. Article 374 separates three TP branches: **self-adjustment under paragraph 1**, no late-payment interest on the resulting amounts (paragraph 3); **authority-study proposal under paragraph 2**, interest on the additional amounts starts the day after the authority presents the proposal to adjust to the median (paragraph 4); **TP inspection**, interest starts from the statutory calculation-filing date for the reporting period containing the relevant transaction (paragraph 5). Keep the actual proposal, calculation and inspection dates; do not start every branch from the original sale date or grant blanket immunity from other fines/offences. Detailed assessment, appeal, suspension and settlement remedies remain separate. [374, 401][code]

## Cross-border points

Analyse PE/head-office dealings separately from annual notification, while retaining Article 376's PE documentation request power. Withholding, deductibility, customs and VAT are separate from the pricing calculation. An adjustment does not prove a foreign corresponding deduction/refund. Article 377 provides MAP where an effective treaty exists; Article 378 permits an application for an advance pricing agreement for transactions with nonresident related parties. Actual treaty, competent-authority procedure, deadlines and current APA conditions require their own primary instruments. No bilateral treaty/MLI or granted agreement is verified in this Guide. [363–364, 376–378][code]

## Two worked examples that recompute

### 2. CUP sales shortfall

Assume the annual gate is separately met, matched goods/terms and a reliable adjusted uncontrolled price of AMD 12,000 per unit versus charged AMD 10,000 for 10,000 units. Revenue difference 20 million. This is a pricing/base bridge, not a certified tax payable or automatic contractual invoice. [368][code]; [556-N 16–25.1][methods]

```oa-check
name: Armenia CUP revenue bridge
inputs:
  quantity: 10000
  charged_unit_price: 10000
  supported_unit_price: 12000
steps:
  - charged_revenue: quantity * charged_unit_price
  - supported_revenue: quantity * supported_unit_price
  - positive_revenue_difference: max(supported_revenue - charged_revenue, 0)
expected:
  charged_revenue: 100000000
  supported_revenue: 120000000
  positive_revenue_difference: 20000000
```

### 5. Statutory quartiles and median

Assume 853-N point 4 applies to eight sorted observations: 2%, 3%, 4%, 5%, 6%, 7%, 8%, 9%. Positions 2 and 6 are integers: lower bound (3% + 4%)/2 = 3.5%; upper (7% + 8%)/2 = 7.5%. Median (5% + 6%)/2 = 5.5%. A tested 2% cost-based net margin lies below the range. On 100 million segmented costs, hypothetical median profit 5.5 million versus actual 2 million yields 3.5 million difference, subject to the statutory adjustment/burden rules. [853-N 4][range]; [361, 368, 371][code]

```oa-check
name: Armenia statutory eight observation range and net margin
inputs:
  second: 0.03
  third: 0.04
  fourth: 0.05
  fifth: 0.06
  sixth: 0.07
  seventh: 0.08
  segmented_costs: 100000000
  actual_margin: 0.02
steps:
  - lower_bound: (second + third) / 2
  - upper_bound: (sixth + seventh) / 2
  - median: (fourth + fifth) / 2
  - actual_profit: segmented_costs * actual_margin
  - median_profit: segmented_costs * median
  - profit_difference: max(median_profit - actual_profit, 0)
expected:
  lower_bound: 0.035
  upper_bound: 0.075
  median: 0.055
  profit_difference: 3500000
```

## Ask the client first

- What are each entity's residence, ownership/control links, tax benefits and natural-resource royalty status?
- Which actual annual transactions, currencies, taxes and PE/head-office allocations reconcile to the ledger?
- What functions, assets, risks, segmented results and genuine comparables support the method?
- Is there a parent/consolidation group, prior-year revenue and existing local/master/country-report package?
- What returns, requests, receipt dates, adjustments, assessments or treaty/APA procedures already exist?

Handoff: scope/aggregation register; exact legal limbs and date gates; transaction and functional analysis; method/comparable search trail; segmented accounts and range; separate pricing/base/tax bridge; notification/documentation/form reconciliation; request calendar and acknowledgements. The prescribed ordinary documentation method is supplied. Actual portal delivery, mismatched large-group statutory/order scope, specialist financial/intangible/restructuring and royalty-rate methods, MAP/APA/remedies and independent country/accountant review remain separate boundaries. The country README retains the specific unresolved treaty-procedure gap.

## Sources

Read on **24 October 2026**. Targeted current Armenian Chapter 73 and Articles 401, 402.1–402.2; English Chapter 73 compared with Armenian, with translation errors disclosed. Actual 556-N methods, 853-N range and 671-N notification text/form read. No client data, real benchmark search, accepted filing or professional attestation obtained.

| Primary source | URL | Read on |
|---|---|---|
| Current Armenian Tax Code | https://www.arlis.am/hy/acts/215611/latest | 2026-10-24 |
| Official English translation, limited currency | https://www.arlis.am/en/acts/231892 | 2026-10-24 |
| Government 556-N, methods | https://www.arlis.am/hy/acts/169936 | 2026-10-24 |
| Government 853-N, range | https://www.arlis.am/hy/acts/169904 | 2026-10-24 |
| SRC 671-N, notification | https://www.arlis.am/hy/acts/218049 | 2026-10-24 |
| Code, native arts. 53(5), 54(1), 105(1), 125(1), 364 and 374; current adjustment/loss/electronic-filing branches | https://www.arlis.am/hy/acts/215611/latest | 2026-10-25 |
| Current SRC 1032-N, form fields 1–27 and instructions 1–28, including 477-N amendment/current metadata | https://www.arlis.am/hy/acts/178495 | 2026-10-25 |

| Fresh native 376(1.1)–(3) complete statutory documentation/filer/language/clock provisions; 53–54 filing/correction restrictions and 325 ordinary settlement, with 364/374–375 rechecked | https://www.arlis.am/hy/acts/215611/latest |2026-10-26|
| Actual signed SRC 941-L, all 5 PDF pages and complete local-file Annex 1–6; independently retrieved bytes match writer retrieval | https://www.src.am/storage/menu_contents_227/hr_hhpekn_2022_941l_64647ea664962.pdf | 2026-10-26 |
| Actual signed SRC 942-L, all 5 PDF pages and complete master-file Annex 1–7; compare native 376 scope | https://www.src.am/storage/menu_contents_227/hr_hhpekn_2022_942l_64647ea6633b1.pdf | 2026-10-26 |
| Actual signed SRC 939-L, all 8 PDF pages, operative date, complete Annex 1–11 and Form 1 tables 1–3 | https://www.src.am/storage/menu_contents_227/hr_hhpekn_2022_939l_64647ea66105f.pdf | 2026-10-26 |

[localorder]: https://www.src.am/storage/menu_contents_227/hr_hhpekn_2022_941l_64647ea664962.pdf
[masterorder]: https://www.src.am/storage/menu_contents_227/hr_hhpekn_2022_942l_64647ea6633b1.pdf
[countryorder]: https://www.src.am/storage/menu_contents_227/hr_hhpekn_2022_939l_64647ea66105f.pdf

[code]: https://www.arlis.am/hy/acts/215611/latest
[english]: https://www.arlis.am/en/acts/231892
[methods]: https://www.arlis.am/hy/acts/169936
[range]: https://www.arlis.am/hy/acts/169904
[notice]: https://www.arlis.am/hy/acts/218049

[tp-return]: https://www.arlis.am/hy/acts/178495

**Not yet confirmed:** authority treatment of a large-group parent/revenue perimeter that differs between Code 376 and the express 942-L/939-L resident/consolidated-revenue wording; actual international exchange or foreign surrogate obligations; specialist finance/intangible/restructuring and royalty-rate methods, MAP/APA and detailed assessment/remedies. The prescribed ordinary local/master/country-report contents and delivery method are supplied above. No live filing acceptance or named professional attestation is claimed.

> Contributed by Michael Cutajar.

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
