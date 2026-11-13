---
name: us-transfer-pricing
description: >
  Apply US federal transfer-pricing rules for tax year 2026 to controlled
  transactions involving goods, services, intangibles, loans and property use.
  Covers the section 482 best-method rule, functional and comparability analysis,
  arm's-length ranges, tested-party financial reconciliation, contemporaneous
  documentation and section 6662 penalties. Use for intercompany pricing,
  management charges, distributor margins, royalties, year-end adjustments and
  transfer-pricing study requests. Includes recomputing resale-price and
  comparable-profits examples and routes treaty double-tax disputes and complex
  cost-sharing arrangements for separate review. Produces a documented working
  paper for a qualified US tax professional, not a filed return or an approved
  taxpayer-specific transfer-pricing position.
jurisdiction: US
category: transfer-pricing
domain: tax
type: situation-rules
tax_year: 2026
tier: 2
last_updated: 2026-11-13
version: 1.0
---

# US federal transfer pricing v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Circular 230 disclosure:** This is general reference material. A practitioner giving written advice must establish the relevant facts, use reasonable factual and legal assumptions, apply the law to those facts, and consider all relevant circumstances. Advice cannot rely on the chance that a return will escape audit or an issue will not be raised. See [31 CFR 10.37(a)](https://www.ecfr.gov/current/title-31/section-10.37).

## Who this applies to

For tax year 2026, apply section 482 when organizations, trades or businesses under common control transact on terms that may distort their US taxable income. It covers domestic as well as cross-border dealings and is not limited to corporations. Control includes direct, indirect and practical control, whether legally enforceable or not; a universal shareholding percentage is not the section 482 test. A lack of tax-avoidance intent does not prevent an adjustment. [26 CFR 1.482-1(a), (f)(1), (i)](https://www.ecfr.gov/current/title-26/section-1.482-1).

The output is a working paper identifying the actual transactions, best method, comparable data, arm's-length result, book-to-tax reconciliation, documentation status and unresolved facts. There is no universal acceptable distributor margin, royalty or management-fee markup. A contract or group policy alone does not establish an arm's-length result.

| Situation | Apply this guide | Condition or separate work needed |
|---|---|---|
| Related entities sell goods, license IP or provide services | Identify the actual transaction and select its most reliable method | Compare actual conduct, functions, resources and risks with the written agreement; [1.482-1(c)-(d)](https://www.ecfr.gov/current/title-26/section-1.482-1) |
| Routine support services charged at cost | Test every services cost method condition | Cost-only treatment is conditional; strategic, excluded or non-beneficial activity does not become eligible merely because it is called a management fee; [1.482-9(b), (l)](https://www.ecfr.gov/current/title-26/section-1.482-9) |
| Related-party loan or tangible property lease | Determine arm's-length interest or rent | Loan terms and borrower credit, or property and use conditions, matter; separate debt characterization, deduction and withholding rules still need review; [1.482-2(a), (c)](https://www.ecfr.gov/current/title-26/section-1.482-2) |
| Cost-sharing arrangement or transfer of a developed intangible | Identify the issue and obtain a specialist analysis | This guide does not compute cost-sharing or platform-contribution payments; 1.482-2(e) directs cost-sharing arrangements to 1.482-7; [1.482-2(e)](https://www.ecfr.gov/current/title-26/section-1.482-2) |
| Existing APA, examination adjustment or treaty dispute | Obtain the agreement, covered years and procedural deadlines first | Apply the actual agreement and competent-authority process; do not substitute these generic examples; [IRS APMA](https://www.irs.gov/businesses/corporations/apma) |

## Rates, bands and thresholds

These are standing rules used for 2026, checked on 2026-11-13. They are not annual inflation-adjusted tax brackets. The source excerpts identify the exact numeric rule; the conditions in the same row are part of that rule.

| Rule | Amount and conditions | Exact source wording and official URL |
|---|---|---|
| Interquartile range (IQR) | From the 25th to the 75th percentile, using the regulatory rank-and-average definition below, when statistical narrowing is required | "25th to the 75th percentile"; [1.482-1(e)(2)(iii)(C)](https://www.ecfr.gov/current/title-26/section-1.482-1) |
| Median for an IRS adjustment using the IQR | Ordinarily the 50th percentile if the tested result is outside the range; not a required adjustment for an in-range result | "50th percentile"; [1.482-1(e)(3)](https://www.ecfr.gov/current/title-26/section-1.482-1) |
| Low-margin services route to SCM eligibility | Median comparable markup on total services costs must be no more than 7%; all other SCM conditions still apply. This is an eligibility ceiling, not an allowed markup | "less than or equal to seven percent"; [1.482-9(b)(3)(ii)](https://www.ecfr.gov/current/title-26/section-1.482-9) |
| Substantial transactional valuation misstatement | Reported price is at least 200% or at most 50% of the correct section 482 price, subject to relief and the minimum attributable underpayment below | "200 percent or more (or 50 percent or less)"; [1.6662-6(b)(1)](https://www.ecfr.gov/current/title-26/section-1.6662-6) |
| Gross transactional valuation misstatement | Reported price is at least 400% or at most 25% of the correct price, subject to relief and the minimum attributable underpayment | "400 percent or more (or 25 percent or less)"; [1.6662-6(b)(2)](https://www.ecfr.gov/current/title-26/section-1.6662-6) |
| Substantial net-adjustment misstatement | Net section 482 adjustment must exceed the lesser of USD 5 million or 10% of gross receipts, after permitted exclusions | "5 million dollars or ten percent"; [1.6662-6(c)(2)](https://www.ecfr.gov/current/title-26/section-1.6662-6) |
| Gross net-adjustment misstatement | Net section 482 adjustment must exceed the lesser of USD 20 million or 20% of gross receipts, after permitted exclusions | "20 million dollars or twenty percent"; [1.6662-6(c)(3)](https://www.ecfr.gov/current/title-26/section-1.6662-6) |
| Substantial / gross penalty rates | 20% / 40% of the tax underpayment attributable to the misstatement, not of the transfer-price adjustment; relief, minimum and coordination rules apply | "20 percent" / "40 percent"; [1.6662-6(a)(1)](https://www.ecfr.gov/current/title-26/section-1.6662-6) |
| Minimum attributable underpayment | Must exceed USD 5,000; USD 10,000 for a corporation other than an S corporation or personal holding company. Apply per tax year | "$5,000 ($10,000 in the case of a corporation other than an S corporation"; remaining exclusions in [1.6662-5(b)](https://www.ecfr.gov/current/title-26/section-1.6662-5) |
| Principal documentation production | Within 30 days of an IRS examination request; documentation generally must already exist when the return is filed | "within 30 days"; [1.6662-6(d)(2)(iii)(A)](https://www.ecfr.gov/current/title-26/section-1.6662-6) |
| Background-document production | Within 30 days of a subsequent request; the district director may extend that background-document period | "within 30 days"; [1.6662-6(d)(2)(iii)(C)](https://www.ecfr.gov/current/title-26/section-1.6662-6) |

## The base

### Establish the transaction and choose the best method

1. Map each party, jurisdiction, ownership/control relationship, transaction type, currency, contract and actual payment. Reconcile the transaction population to the general ledger and related-party balances. Separate goods, services, licenses, loans and rentals before deciding whether aggregation gives a more reliable result.
2. Record who actually performs functions, employs assets/resources and bears risks. Cover product/service characteristics, significant contract terms, economic conditions and realistic alternatives. Explain inconsistent conduct or contractual allocations. These are the comparability factors in [1.482-1(d)](https://www.ecfr.gov/current/title-26/section-1.482-1).
3. Search available internal uncontrolled transactions and appropriate external data. Record search dates, inclusion/exclusion decisions and data limitations. Evaluate credible alternative methods; choose the one producing the most reliable arm's-length measure. There is no mandatory hierarchy, but a close, reliably adjusted uncontrolled price may be more reliable than an indirect margin comparison. [1.482-1(c)](https://www.ecfr.gov/current/title-26/section-1.482-1).
4. Quantify material differences where reliable adjustments improve comparability. Examples include freight, payment terms, product mix, accounting classification and working-capital differences. Show the unadjusted data, adjustment formula, evidence and adjusted result. An unadjusted industry average is not an arm's-length study. Do not manufacture a missing comparable or use an unsupported adjustment to force a desired answer. [1.482-1(d)(2)](https://www.ecfr.gov/current/title-26/section-1.482-1).
5. Calculate the selected method on the relevant business activity, explain any aggregation or multiple-year analysis, and reconcile the tested financials to books and the return. Use the same accounting definitions on both sides of the comparison. Document abnormal costs and business conditions, rather than automatically deleting losses. [1.482-1(f)(2)](https://www.ecfr.gov/current/title-26/section-1.482-1); [IRS documentation FAQs, questions 3-4](https://www.irs.gov/businesses/international-businesses/transfer-pricing-documentation-frequently-asked-questions-faqs).

### Match the method to the evidence

| Transaction / method | Mechanical base and application | Reliability or exception to test |
|---|---|---|
| Tangible goods: comparable uncontrolled price (CUP) | Comparable uncontrolled unit price, reliably adjusted for differences, multiplied by controlled quantity | Close product and transaction comparability; internal third-party sales may supply useful evidence; [1.482-3(b)](https://www.ecfr.gov/current/title-26/section-1.482-3) |
| Tangible goods: resale price | Applicable unrelated resale price less an arm's-length gross profit; remove other costs included in COGS when isolating the controlled purchase price | Reseller functions and accounting classification must be comparable; generally suited to resale without substantial alteration or substantial value added through intangible property; [1.482-3(c), including example 2](https://www.ecfr.gov/current/title-26/section-1.482-3) |
| Tangible goods: cost plus | Appropriate production cost base plus comparable gross-profit markup on that base | Match cost definitions and functions; a gross markup on production costs is different from an operating margin on sales; [1.482-3(d)](https://www.ecfr.gov/current/title-26/section-1.482-3) |
| Comparable profits method (CPM) | Apply a reliable profit-level indicator to the tested party's relevant activity: for a sales-margin indicator, target operating profit = relevant sales x benchmark operating margin | Select the party for which reliable data and the fewest adjustments are available, ordinarily the less complex party without unique valuable intangibles. Select the indicator on facts, not desired income; [1.482-5(b)-(d)](https://www.ecfr.gov/current/title-26/section-1.482-5) |
| Intangibles | Evaluate comparable uncontrolled transaction (CUT), CPM, profit split or an unspecified method; a CUT may support a royalty applied to the contractual sales base | Consider the rights, market, duration and expected benefits; income must be commensurate with the intangible's income, and periodic adjustments may apply. There is no standard royalty percentage; [1.482-4(a), (c), (f)(2)](https://www.ecfr.gov/current/title-26/section-1.482-4) |
| Profit split | Define combined operating profit/loss of the relevant activity, then allocate using a comparable profit split or a residual profit split | Residual method first rewards routine contributions, then allocates residual profit by relative value of nonroutine contributions. Do not assume equal shares or that development cost equals intangible value; [1.482-6(a)-(c)](https://www.ecfr.gov/current/title-26/section-1.482-6) |
| Services | Evaluate SCM, comparable uncontrolled services price, gross services margin, cost of services plus, CPM, profit split or an unspecified method | Confirm a compensable benefit, cost pool and allocation key before applying any markup; [1.482-9(a), (k), (l)](https://www.ecfr.gov/current/title-26/section-1.482-9) |
| Loans and property use | Compare interest given principal, maturity, security, borrower credit and market; compare rent for similar property and use | No blanket interest rate or rent is supplied here. Examine the specific financing/property rules and any applicable exceptions; [1.482-2(a)(2), (c)](https://www.ecfr.gov/current/title-26/section-1.482-2) |

Unspecified methods remain subject to the best-method rule. For the penalty-protection route in 1.6662-6(d)(3)(ii)(B), the taxpayer must make a reasonable effort to evaluate the applicable specified methods and reasonably conclude that none was likely to provide a reliable arm's-length measure, and that the selected unspecified method was likely to do so. The separate (C) route concerns a transaction for which no specified methods apply; document its own conditions. A conclusion that an unspecified method is merely more reliable does not by itself satisfy the (B) defense. [1.6662-6(d)(3)](https://www.ecfr.gov/current/title-26/section-1.6662-6).

### Services cost method is conditional

SCM permits total services costs without a profit markup only when all requirements in [1.482-9(b)](https://www.ecfr.gov/current/title-26/section-1.482-9) are met. The service must qualify as a specified covered service or satisfy the low-margin route in the table. It must not be an excluded activity, and the taxpayer must reasonably conclude that it does not contribute significantly to key competitive advantages, core capabilities or fundamental business risks. Maintain adequate books, the intent to apply SCM, the parties, costs and allocation method.

Excluded activities include manufacturing/production, extraction of natural resources, construction, reselling/distribution and sales agency, research and development, engineering/scientific activity, financial transactions including guarantees, and insurance/reinsurance. A service label does not override that exclusion. Under the benefit rules, distinguish compensable services from solely shareholder activity, passive association, remote benefits and duplication with no additional benefit. Allocate costs to actual beneficiaries using a defensible expected-benefit measure, such as employee counts when relevant to the service. [1.482-9(b)(4)-(6), (k), (l)(3)](https://www.ecfr.gov/current/title-26/section-1.482-9).

### Build a valid range and compute the adjustment

The full range is available when the comparables and data meet the stringent conditions for identifying all material differences and reliably adjusting them. Otherwise, if residual comparability defects remain, improve reliability using a valid statistical method; ordinarily this is the IQR. A range cannot rescue incomparable data. [1.482-1(e)(2)](https://www.ecfr.gov/current/title-26/section-1.482-1).

Sort the accepted comparable results. For each regulatory percentile, select the lowest result with at least the specified percentage of observations at or below it. If exactly that percentage lies at or below the selected result, average that result and the next higher result. Apply this definition to the quartiles and median; do not silently substitute a spreadsheet's interpolated percentile convention. [1.482-1(e)(2)(iii)(C), (e)(3)](https://www.ecfr.gov/current/title-26/section-1.482-1).

An adequately supported result within the arm's-length range is not adjusted under the range rule. If outside it, the IRS may adjust to a point in the range: ordinarily the median when the IQR is used, and ordinarily the arithmetic mean in other cases. This does not authorize choosing an extreme point without a reliability analysis. [1.482-1(e)(1), (3)](https://www.ecfr.gov/current/title-26/section-1.482-1); [1.6662-6(d)(2)(ii)(A)(5)](https://www.ecfr.gov/current/title-26/section-1.6662-6).

For a US distributor using an operating-margin CPM, reconcile relevant sales less COGS less operating expenses to operating profit. Compare the operating profit with the supported range in dollars. If a purchase-price adjustment is the identified correction, reducing controlled purchase COGS raises US operating profit by the same amount, assuming all affected goods were sold and no other tax differences. Unsold inventory requires an inventory/basis analysis; do not automatically deduct or add the entire invoice adjustment to current-year income. [1.482-5(b), (d)](https://www.ecfr.gov/current/title-26/section-1.482-5); [1.482-1(a)(2)](https://www.ecfr.gov/current/title-26/section-1.482-1).

## Deadlines and filing

Prepare the analysis while pricing and preparing the return. The documentation exception to the net-adjustment penalty generally requires the supporting documentation to exist when the return is filed and to be produced within the request period shown above. The regulation excepts the post-year-end information summary and general index in items (9) and (10) from the existence-at-filing condition. This is a penalty-defense documentation rule, not a stand-alone annual filing of a TP study. [1.6662-6(d)(2)(iii)](https://www.ecfr.gov/current/title-26/section-1.6662-6).

The principal documentation must contain:

- Business overview and economic/legal factors, plus the organization chart and relevant related parties.
- Any documentation specifically required by the section 482 regulations.
- The selected method, why it satisfies its conditions, alternatives considered and reasons for rejection.
- Controlled transactions and terms, internal data, and cost/financial allocations needed by the method.
- Comparables, selection process, comparability adjustments, economic analysis and projections.
- Relevant data obtained after year-end but before filing, plus an index of principal/background documents and a description of the recordkeeping system.

These grouped items cover the regulatory list in [1.6662-6(d)(2)(iii)(B)(1)-(10)](https://www.ecfr.gov/current/title-26/section-1.6662-6). Retain underlying agreements, invoices, searches, source financials and calculations as background support. Update the study for material changes; prior-year work is usable only if still reliable or appropriately modified. Having a document titled "transfer-pricing report" does not itself establish reasonable method selection or penalty protection. [1.6662-6(d)(2)(ii)-(iii)](https://www.ecfr.gov/current/title-26/section-1.6662-6); [IRS documentation FAQs](https://www.irs.gov/businesses/international-businesses/transfer-pricing-documentation-frequently-asked-questions-faqs).

A taxpayer may report arm's-length results using prices different from those actually charged on a timely filed US income tax return, including extensions. Section 482 does not give a taxpayer a right to reduce taxable income through an untimely or amended return applying section 482. Document any permitted year-end true-up, book entries, inventory effects, cash settlement and foreign consequences. [1.482-1(a)(3)](https://www.ecfr.gov/current/title-26/section-1.482-1).

Use the entity's return instructions to establish its filing/payment dates. Review information-return obligations separately; the local guides [Form 5471](us-form-5471-cfc-information.md) and [Form 5472](us-form-5472-foreign-owned-us.md) address those filings. A TP study does not replace an applicable information return.

## Penalties and interest

**AUDIT FLASH POINT**: Test both the transactional misstatement and net-adjustment rules. The dollar amount of an adjustment alone does not establish the penalty. Apply the inclusive price-ratio boundaries, strict greater-than net-adjustment thresholds, minimum attributable tax underpayment, exclusions and coordination rules in the table. [1.6662-6(a)-(f)](https://www.ecfr.gov/current/title-26/section-1.6662-6); [1.6662-5(b)](https://www.ecfr.gov/current/title-26/section-1.6662-5).

For the net test, begin with section 482 taxable-income increases for the year, subtract permitted collateral decreases, and apply the documented exclusions in paragraph (d). Gross receipts are computed under the rule cross-referenced in paragraph (c)(5), adjusted for section 482 allocations; the consolidated-return examples apply the test to the group. Do not test invoice turnover or each member in isolation without that computation. [1.6662-6(c), including examples 3-5](https://www.ecfr.gov/current/title-26/section-1.6662-6).

A reasonably selected and applied specified method, supported by timely adequate documentation, may exclude an adjustment from the net test. Documentation alone is insufficient. Unspecified methods have additional requirements. The reasonable-cause rules for a transactional penalty and the statutory documentation requirements for a net-adjustment penalty are not interchangeable. Do not stack the substantial and gross penalties on the same underpayment; apply the coordination rules. [1.6662-6(b)(3), (c)(6), (d), (f)](https://www.ecfr.gov/current/title-26/section-1.6662-6).

Compute any penalty on the resulting attributable tax underpayment after the actual taxpayer's tax computation, rather than multiplying the transfer-price adjustment by a penalty rate. Interest is separate; rates may change quarterly and an extension to file does not stop interest on unpaid tax. Obtain the rates for each affected period instead of using a fixed annual interest assumption. [IRS interest guidance](https://www.irs.gov/payments/interest).

## Cross-border points

An IRS adjustment and a foreign corresponding adjustment are separate procedural matters. Economic double taxation may require treaty competent-authority assistance. APMA handles section 482-type disputes under applicable treaties. Seek assistance promptly and protect US refund and foreign procedural rights; do not assume a pending discussion suspends either country's limitation periods. The IRS cannot provide competent-authority assistance for a country without an applicable treaty. [IRS competent-authority assistance](https://www.irs.gov/individuals/international-taxpayers/competent-authority-assistance).

For material recurring transactions, assess whether an advance pricing agreement is appropriate and obtain current application guidance from [IRS APMA](https://www.irs.gov/businesses/corporations/apma). A transfer-price conclusion does not by itself settle withholding, customs valuation, deductibility or international information reporting. Identify those separate workstreams before implementing a cross-border payment or true-up.

## Two worked examples that recompute

All business facts, prices and comparable margins below are hypothetical inputs illustrating mechanics, not published benchmark data or safe harbors. Dollars are USD. Assume all purchased goods are sold in the year, with no inventory or other tax differences. The examples determine income adjustments, not final income tax or penalties.

### Example 1: resale price with other COGS

A US reseller buys finished goods from a foreign affiliate and resells them without substantial alteration or valuable intangible contributions. Assume the documented best-method analysis establishes a single reliable gross margin of 25% of unrelated sales, after all comparability adjustments. Sales are USD 1,000,000. Separately purchased third-party goods included in the resale package create USD 200,000 of other COGS. The controlled goods were charged at USD 600,000.

Under [1.482-3(c), including example 2](https://www.ecfr.gov/current/title-26/section-1.482-3), target gross profit is USD 250,000 and total target COGS is USD 750,000. Subtract the third-party COGS to isolate the controlled purchase price: USD 550,000. Reducing that price by USD 50,000 raises US gross profit from USD 200,000 to USD 250,000 and US taxable income by USD 50,000 on these assumptions. Forgetting the separate COGS would incorrectly allow USD 750,000 for the controlled purchase.

```oa-check
name: Resale price isolates the controlled purchase (2026)
inputs:
  sales: 1000000
  arm_length_gross_margin: 0.25
  third_party_cogs: 200000
  reported_controlled_cogs: 600000
steps:
  - target_gross_profit: sales * arm_length_gross_margin
  - target_total_cogs: sales - target_gross_profit
  - target_controlled_cogs: target_total_cogs - third_party_cogs
  - reported_gross_profit: sales - third_party_cogs - reported_controlled_cogs
  - us_income_increase: reported_controlled_cogs - target_controlled_cogs
  - corrected_gross_profit: reported_gross_profit + us_income_increase
expected:
  target_gross_profit: 250000
  target_total_cogs: 750000
  target_controlled_cogs: 550000
  reported_gross_profit: 200000
  us_income_increase: 50000
  corrected_gross_profit: 250000
```

### Example 2: does a CPM result require a range adjustment?

Assume CPM with operating profit/sales is the best method for a US routine distributor. Four equally reliable, adjusted comparable margins are 2%, 4%, 6% and 8%. Residual comparability defects require statistical narrowing; the IQR is appropriate. These are invented demonstration data, not a sufficient real-world study. Under the rank-and-average definition in [1.482-1(e)(2)(iii)(C)](https://www.ecfr.gov/current/title-26/section-1.482-1), the lower quartile is (2% + 4%)/2 = 3%, the upper is (6% + 8%)/2 = 7%, and the median is (4% + 6%)/2 = 5%.

With USD 20,000,000 sales and reported operating profit USD 200,000, the margin is 1%, below the 3%-7% range. An ordinary IRS median adjustment under [1.482-1(e)(3)](https://www.ecfr.gov/current/title-26/section-1.482-1) produces target profit USD 1,000,000 and an income increase of USD 800,000. If controlled purchase COGS is the correction, it falls from USD 17,800,000 to USD 17,000,000, keeping USD 2,000,000 operating expenses unchanged.

Decision variant: if the same distributor instead reports USD 800,000 operating profit, its 4% margin is inside the supported range. The range rule calls for no adjustment. Forcing the median would add USD 200,000 unnecessarily; the block shows that difference for comparison, not as a required true-up. Both conclusions depend on the range and method actually being reliable.

```oa-check
name: CPM outside-range versus inside-range decision (2026)
inputs:
  sales: 20000000
  comparable_a: 0.02
  comparable_b: 0.04
  comparable_c: 0.06
  comparable_d: 0.08
  reported_operating_profit: 200000
  operating_expenses: 2000000
  alternative_operating_profit: 800000
steps:
  - lower_quartile: (comparable_a + comparable_b) / 2
  - upper_quartile: (comparable_c + comparable_d) / 2
  - median: (comparable_b + comparable_c) / 2
  - lower_profit: sales * lower_quartile
  - upper_profit: sales * upper_quartile
  - reported_margin: reported_operating_profit / sales
  - target_profit: sales * median
  - income_increase: target_profit - reported_operating_profit
  - reported_controlled_cogs: sales - operating_expenses - reported_operating_profit
  - corrected_controlled_cogs: reported_controlled_cogs - income_increase
  - alternative_margin: alternative_operating_profit / sales
  - alternative_below_range: max(0, lower_profit - alternative_operating_profit)
  - alternative_above_range: max(0, alternative_operating_profit - upper_profit)
  - unnecessary_median_increase: target_profit - alternative_operating_profit
expected:
  lower_quartile: 0.03
  upper_quartile: 0.07
  median: 0.05
  lower_profit: 600000
  upper_profit: 1400000
  reported_margin: 0.01
  target_profit: 1000000
  income_increase: 800000
  reported_controlled_cogs: 17800000
  corrected_controlled_cogs: 17000000
  alternative_margin: 0.04
  alternative_below_range: 0
  alternative_above_range: 0
  unnecessary_median_increase: 200000
```

## Ask the client first

- Which entities, countries, control relationships, tax years and existing APAs or audits are involved?
- What was actually supplied, by whom and on what terms; do contracts, invoices and conduct agree?
- Who performs the functions, uses or owns relevant assets/IP, controls activities and bears the actual risks?
- What transaction-level accounts, third-party dealings and comparable-data searches support the method and reconcile to the return?
- Which pricing changes, losses, unusual expenses or year-end adjustments occurred, and are affected goods still in inventory?
- When will the return be filed; what documentation already exists; and are any IRS requests, foreign adjustments or treaty/refund deadlines running?

## Sources

Read dates below mean the identified provisions or page sections were opened and read on 2026-11-13. The eCFR Title 26 pages displayed November 2026 currency; no claim is made that every unrelated provision in each long regulation was reviewed. These sources support standing rules used for tax year 2026, rather than historical figures copied into a new-year table.

| Official source | Specific material read and used | Read date |
|---|---|---|
| [26 CFR 1.482-1](https://www.ecfr.gov/current/title-26/section-1.482-1) | Read for (a)-(e): scope, taxpayer adjustments, best method, comparability and range; (f)(1)-(2): scope, aggregation and multiple years; (i): control and taxpayer definitions; range examples | 2026-11-13 |
| [26 CFR 1.482-2](https://www.ecfr.gov/current/title-26/section-1.482-2) | Read for (a)(2) arm's-length interest factors; (c) tangible property rental; (d)-(e) property and cost-sharing cross-references | 2026-11-13 |
| [26 CFR 1.482-3](https://www.ecfr.gov/current/title-26/section-1.482-3) | Read for (a)-(d): tangible methods, CUP comparability, resale-price rule and example 2, cost-plus base | 2026-11-13 |
| [26 CFR 1.482-4](https://www.ecfr.gov/current/title-26/section-1.482-4) | Read for (a), (c), (f)(2): intangible methods, CUT considerations and periodic adjustments | 2026-11-13 |
| [26 CFR 1.482-5](https://www.ecfr.gov/current/title-26/section-1.482-5) | Read for (a)-(d): CPM, tested party, profit indicators, comparability and financial definitions | 2026-11-13 |
| [26 CFR 1.482-6](https://www.ecfr.gov/current/title-26/section-1.482-6) | Read for (a)-(c): profit/loss allocation, comparable and residual splits, routine and nonroutine contributions | 2026-11-13 |
| [26 CFR 1.482-9](https://www.ecfr.gov/current/title-26/section-1.482-9) | Read for (a), (b), (k), (l)(3): service methods, SCM eligibility/exclusions/records, cost allocation and benefit test | 2026-11-13 |
| [26 CFR 1.6662-6](https://www.ecfr.gov/current/title-26/section-1.6662-6) | Read for (a)-(d), (f): rates, transaction/net thresholds, gross receipts, consolidated examples, method/documentation exclusions, principal/background records and penalty coordination | 2026-11-13 |
| [26 CFR 1.6662-5](https://www.ecfr.gov/current/title-26/section-1.6662-5) | Read for (b)-(c): minimum attributable underpayment and carryover application | 2026-11-13 |
| [IRS transfer-pricing documentation FAQs](https://www.irs.gov/businesses/international-businesses/transfer-pricing-documentation-frequently-asked-questions-faqs) | Read for Questions 3-4: documentation quality, reliability, functional analysis, comparables and actual financial results | 2026-11-13 |
| [IRS APMA](https://www.irs.gov/businesses/corporations/apma) | Read for Program purpose and links to current APA/competent-authority procedures | 2026-11-13 |
| [IRS competent-authority assistance](https://www.irs.gov/individuals/international-taxpayers/competent-authority-assistance) | Read for Section 482 double taxation, applicable treaties, timely requests, protective refund claims and foreign procedural rights | 2026-11-13 |
| [IRS interest](https://www.irs.gov/payments/interest) | Read for Underpayment interest, filing extensions and quarterly rate changes | 2026-11-13 |
| [31 CFR 10.37](https://www.ecfr.gov/current/title-31/section-10.37) | Read for (a): written-advice factual/legal assumptions, relevant facts and audit-lottery prohibition | 2026-11-13 |

**Not yet confirmed:** No unconfirmed legal figures are used. Taxpayer-specific comparables, method selection, treaty deadlines, APA terms and cost-sharing calculations require the actual facts and separate analysis; the hypothetical margins above cannot be used as market evidence.
