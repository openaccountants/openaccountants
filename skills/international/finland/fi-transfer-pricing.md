---
name: fi-transfer-pricing
description: >
  Finland transfer-pricing documentation and arm's-length pricing for tax year
  2026. Covers Finnish taxpayers with foreign related-party transactions and
  foreign enterprises with Finnish permanent establishments. Explains related
  control, the SME exemption, group-size aggregation, Master File and Local
  File contents, the EUR 500,000 counterparty simplification, Form 78,
  documentation requests and sanctions. Use for Finnish intercompany sales,
  services, financing, intangibles, restructuring, transfer-pricing adjustments,
  tax returns and evidence preparation. Distinguishes pricing, documentation
  and separate country-by-country reporting obligations. Includes ordinary transaction calculations and two
  recomputable examples. Specialist arrangements require a separately scoped
  transaction analysis; no professional attestation is claimed.
jurisdiction: FI
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-26
version: 0.7
---

# Finland transfer-pricing documentation v0.7

## Who this applies to

The Finnish Tax Administration's guidance addresses foreign related-party transactions of Finnish taxpayers and dealings between a foreign enterprise and its Finnish PE. The pricing principle also applies to small enterprises outside the full documentation obligation. [Obligation guidance][obligation]

Apply the current Assessment Procedure Act §§14a–14c and 31–32a. The older Vero documentation page is flagged for updating; use the current statute where wording differs. This Guide supplies the ordinary documentation and pricing method, not a benchmark rate for an unidentified business. [Current Act][law].

### Related parties and the actual transaction

Section 31 covers direct/indirect majority capital or votes, majority appointment rights, common management and other actual control, including common third-party control. Analyse contracts, functions, assets, risks, transaction characteristics, economic conditions and strategies before pricing the actual transaction. Replacing that transaction is an exceptional statutory route with additional conditions, not an ordinary benchmarking shortcut. [Assessment Procedure Act, section 31][law]

## Rates, bands and thresholds

| Item | 2026 rule | Official source |
|---|---|---|
| SME employee condition | Fewer than 250 employees; this and the other SME conditions must all hold. | [Act, section 14a][law] |
| SME financial condition | Turnover at most EUR 50 million **or** balance-sheet total at most EUR 43 million; apply the Commission recommendation's independence and aggregation rules too. | [Act, section 14a][law] |
| Documentation simplification | At most EUR 500,000 of annual arm's-length transactions per counterparty; specified Master/Local File information is relieved, not the pricing obligation. | [Act, section 14b(5)][law] |
| Documentation request | 60 days, subject to the six-month earliest presentation rule. | [Act, section 14c][law] |
| Supplement request | 90 days. | [Act, section 14c][law] |
| Documentation penalty maximum | EUR 25,000 for the specified failures; separate from substantive tax. | [Act, sections 32 and 32a][law] |

The detailed guidance defines the SME exclusion using all three requirements: fewer than 250 employees; turnover at most EUR 50 million **or** balance sheet at most EUR 43 million; and compliance with the Commission recommendation's SME criteria. Group and linked/partner-enterprise relationships matter. A small Finnish subsidiary cannot determine its status using its standalone figures alone. [Detailed guidance, section 4.3][detailed]

The detailed guidance and Form 78 instructions use turnover **exceeding** EUR 50 million and balance sheet **exceeding** EUR 43 million for that financial-size route. A separate FAQ uses “or more”. Section 14a supports the inclusive SME financial ceilings in the detailed guidance, so the FAQ wording must not replace that statutory test. Employee count, EU SME status, group relationships and changes across years still require their own checks. [Assessment Procedure Act, section 14a][law]; [Detailed guidance][detailed]; [Form 78][form]; [FAQ][faq]

### Counterparty aggregation

Detailed guidance section 4.4 describes reduced documentation where annual controlled dealings with a particular associated enterprise have an arm's-length value no greater than EUR 500,000. Aggregate that counterparty's dealings; do not test each invoice separately. Its examples include service income plus loan interest, and separately a newly drawn loan principal. Repayment of that principal is not counted as another borrowing. [Detailed guidance, section 4.4][detailed]

The simplification can remove the Master File requirement when no counterparty exceeds the threshold. For qualifying below-threshold dealings, it removes specified Local File functional/comparability/method content, while other taxpayer information remains required. It does not exempt the pricing from the arm's-length principle. Keep loan movements and valuation evidence for the applicability check. [Section 4.4][detailed]

## The base

Select the most reliable method for the delineated transaction and available comparables. Vero distinguishes CUP (price), resale price/cost plus (gross margin), TNMM (net indicator) and profit split. If equally reliable, traditional transaction methods take preference over profit methods, and CUP over other methods. Record the tested party, base, adjustments and calculation; avoid a universal markup. [Detailed guidance, sections 6.6–6.7][detailed]

Gross cost plus and a net-cost TNMM are different analyses. Do not import every overhead into a gross cost base or transfer a net margin to gross costs without supporting comparability. [Detailed guidance, section 6.7.2][detailed]

### Execute the selected method

Prepare a separate transaction segment, reconcile revenue/costs/assets to the ledger, explain consistent accounting classifications and apply only comparables matching functions, assets, controlled risks and economic circumstances. Document the reason for each comparability adjustment and why rejected methods are less reliable. A tax adjustment under §31 requires the arm's-length conditions and the resulting understated income/overstated loss; the result is carried into the [corporate computation](fi-corporate-income-tax.md), with interest deductibility tested separately. [Act §§14b,31][law].

The following are calculation identities for the **supported selected method**, not statutory safe-harbour margins:

| Method | Execution once comparability is established |
|---|---|
| CUP | Comparable unit price, adjusted for supported differences, × controlled quantity; reconcile with booked consideration. |
| Resale price | Independent resale revenue × (1 − comparable **gross** resale margin) gives supported purchase price, after consistent functional/accounting adjustments. |
| Cost plus | Comparable qualifying gross cost base × (1 + supported gross markup). Reconcile cost inclusions consistently with comparables. |
| TNMM | Select the less complex tested party and reliable net indicator. Net-cost route: qualifying operating costs × supported net markup = target operating profit; required revenue = those costs + target profit. Sales route: target profit = comparable net margin × sales, and derive the controlled price from the segment reconciliation. |
| Profit split | Establish combined relevant profit and supported allocation of contributions; where residual analysis is selected, compensate routine functions first, then allocate the residual on evidenced contributions. The allocation key is not automatically ownership or country revenue. |

Method selection and the gross/net distinction follow [Vero detailed guidance §§6.6–6.7][detailed]. The algebra above is a workpaper implementation; it does not establish the comparable margin or authorise selection of a convenient point in a range. Keep internal/external searches, acceptance/rejection criteria, comparability adjustments and the actual calculation with the file.

For routine intragroup services, establish a concrete recipient benefit and exclude shareholder-only activities. Identify direct/indirect service costs and support allocation keys reflecting use, then apply a supported method/markup; do not charge all central costs by revenue merely because it is available. CUP is useful where comparable independent services exist; a net-cost TNMM must use a consistent operating-cost base. A higher-value activity involving unique intangibles is not automatically routine support. [Vero services guidance][services].

For an ordinary loan, delineate debt, actual borrower capacity and terms first. Price the borrower/instrument at the origination date using internal/external comparable lending adjusted for currency, maturity, security, subordination, repayment, fixed/floating rate and creditworthiness. A parent's external borrowing rate is not automatically its subsidiary's rate. Compute interest from principal outstanding by period × supported annual rate × contractual day fraction; separate fees and retain the interest-limit calculation. Guarantees, cash pools and intangibles/restructuring require their own economic analysis; do not reuse the routine-loan spread blindly. [Vero loan guidance][loans]; [Act §31][law].

### Documentation contents

Section 14b identifies these group-level categories: organisation; business; intangibles activity; financing; financial statements or corresponding available information; and advance tax positions/agreements concerning cross-border income allocation. [Section 14b(1); 2016 amending Act][amendment]

At taxpayer level it requires organisation/management; business; related-party relationships; controlled transactions and PE dealings; functional analysis; comparability analysis and available comparables; method and application; financial statements or equivalent; and relevant foreign advance tax positions/agreements. These are content categories, not permission to replace transaction evidence with headings. [Section 14b(2)][amendment]

A separable independently operated business area can be described at group level, but central group functions/transactions remain included and the authority can request other business areas. Section 14b also addresses a standalone foreign enterprise with a Finnish PE. Apply the specific simplifications above separately. [Section 14b(3)–(5)][law]

### Preparation workpaper

Use this as an evidence checklist, not a claim that it reproduces every statutory local-file requirement:

- Identify the taxpayer, PE, related parties, residences and period.
- Record group structure and reconcile the size/SME calculation to the underlying accounts.
- List each transaction, agreement, booked amount and relevant currency.
- Describe actual conduct, functions, assets and risks; preserve evidence supporting the chosen pricing analysis.
- Connect the analysis and any adjustment to the accounts, tax computation and Form 78.
- Keep the authority's request, receipt date, requested scope, response calendar and delivery acknowledgement together.

A documentation exemption does not establish an acceptable price. Nor does an authority request establish the correct margin: the transaction evidence still needs substantive analysis. No benchmark markup or interest rate is supplied by this checklist.

## Deadlines and filing

The obligation guidance states: annual documentation; Finnish, Swedish or English; submission within 60 days of request; supplementary information within 90 days. Section 14c sets the earliest presentation date for that year's documentation at six months after the financial-year-end month; this is not worded as a ban on issuing an earlier request. Extensions can be requested. It describes a two-consecutive-year size transition and a maximum EUR 25,000 documentation sanction. Calendar the request and statutory presentation restriction together. The authority may extend the presentation/supplement deadlines on request; section 14c says that extension decision cannot be appealed. Current penalty conditions remain a separate check. [Section 14c][law]; [Obligation guidance][obligation]

Form 78 is separate from the documentation. Its instructions say documentation is provided on request rather than attached to the return. Where no foreign related-party transactions occurred during the year, those instructions say Form 78 is unnecessary. Check the taxpayer's facts and the applicable return instructions before filing. [Form 78][form]

## Penalties and interest

Sections 32(1)(2) and 32a provide a maximum EUR 25,000 increase for the specified late, materially incomplete or incorrect documentation/supplement failures. It is not an automatic fixed fee or a ceiling on every substantive tax adjustment. Check the failure, hearing, applicable penalty provision and decision separately. [Assessment Procedure Act][law]

For income tax paid after its due date, the 2026 ordinary late-payment interest rate is 9.5% annually. It runs from the day after the due date through the payment date using actual calendar days. The separate interest rate with relief is 4.5% in 2026. The assessment and reporting circumstances determine which type and start date apply; a period spanning calendar years requires the relevant year's rate. [Vero, interest rules][interest]

## Cross-border points

Reconcile a proposed adjustment with the foreign counterparty, accounts and returns. Corresponding adjustment, treaty dispute relief and APA routes need a separate verified procedure; this draft establishes neither automatic foreign relief nor an agreed pricing result. The [CbCR Guide](fi-country-by-country-reporting.md) addresses a separate reporting obligation.

## Two worked examples that recompute

Assume a supported independent-party price of EUR 120 per unit for 2,000 units sold at EUR 105. The assumed revenue difference is EUR 30,000. The comparable price and all legal conditions are assumptions; this block tests arithmetic only and does not select a tax rate.

```oa-check
name: Finland assumed controlled sale price reconciliation
inputs:
  units: 2000
  booked_unit_price: 105
  supported_unit_price: 120
steps:
  booked_revenue: units * booked_unit_price
  supported_revenue: units * supported_unit_price
  assumed_adjustment: supported_revenue - booked_revenue
expected:
  booked_revenue: 210000
  supported_revenue: 240000
  assumed_adjustment: 30000
```

### 2. Routine service net-cost TNMM

Assume a delineated routine service, EUR 90,000 direct and EUR 10,000 attributable indirect operating costs, EUR 5,000 excluded shareholder costs, a supported comparable net-cost markup of **6%** and booked charge EUR 102,000. Qualifying cost is EUR 100,000, target profit EUR 6,000 and supported charge EUR 106,000; the assumed revenue adjustment is EUR 4,000. The 6% and allocation are hypothetical supported inputs, not Finnish safe harbours.

```oa-check
name: Finland routine service net cost transaction calculation
inputs:
  direct_costs: 90000
  indirect_costs: 10000
  shareholder_costs: 5000
  supported_net_markup: 0.06
  booked_charge: 102000
steps:
  total_booked_cost: direct_costs + indirect_costs + shareholder_costs
  qualifying_cost: total_booked_cost - shareholder_costs
  target_operating_profit: qualifying_cost * supported_net_markup
  supported_charge: qualifying_cost + target_operating_profit
  revenue_adjustment: supported_charge - booked_charge
expected:
  total_booked_cost: 105000
  qualifying_cost: 100000
  target_operating_profit: 6000
  supported_charge: 106000
  revenue_adjustment: 4000
```

## Ask the client first

- Which foreign parties and PE dealings exist, and what establishes the relationships?
- What are the group size figures, ownership links and prior-year changes?
- What transactions and pricing evidence reconcile to the accounts?
- Has an authority requested documents or supplements, and when was it received?
- What return and Form 78 submissions already exist?

## Sources

The 23 October source work and independent review remain preserved in the country research records. On 26 October, the current Act and Vero documentation/return sources were rechecked for this revision. The English documentation guidance is a translation; Finnish and Swedish versions prevail.

| Official source | URL | Read on |
|---|---|---|
| Finlex, current Act on Assessment Procedure 1558/1995, sections 14a–14c, 31, 32 and 32a | https://www.finlex.fi/fi/lainsaadanto/1995/1558 | 2026-10-26 |
| Vero, documentation obligation (page flagged for updating) | https://www.vero.fi/en/businesses-and-corporations/business-operations/transfer-pricing/transfer-pricing-documentation/obligation-to-compile-a-transfer-pricing-documentation/ | 2026-10-26 |
| Vero, detailed documentation guidance, including method selection and simplification | https://www.vero.fi/en/detailed-guidance/guidance/47978/transfer-pricing-documentation/ | 2026-10-26 |
| Vero, Form 78 instructions | https://www.vero.fi/en/About-us/contact-us/forms/filling-instructions/78-explanation-of-transfer-prices-how-to-fill-out-the-form/ | 2026-10-26 |
| Vero, 2026 Form 78 | https://vero.fi/en/About-us/contact-us/forms/descriptions/78_explanation_of_transfer_prices_3054/ | 2026-10-26 |
| Vero, documentation FAQ (retained source for the recorded threshold-wording discrepancy) | https://www.vero.fi/en/businesses-and-corporations/business-operations/foreign-business-in-finland/supporting-high-growth-companies-with-international-tax-questions/faq---transfer-pricing/faq/when-does-a-company-need-to-maintain-and-submit-transfer-pricing-documentation-in-finland/ | 2026-10-23 |
| Finlex, 2016 amending Act (historical source retained; current Act governs) | https://www.finlex.fi/api/media/statute/699004/mainPdf/main.pdf?timestamp=2016-12-28T22%3A00%3A00.000Z | 2026-10-23 |
| Vero, routine services | https://www.vero.fi/en/businesses-and-corporations/business-operations/transfer-pricing/transfer-pricing-of-sale-of-services/ | 2026-10-26 |
| Vero, intragroup loans | https://www.vero.fi/en/businesses-and-corporations/business-operations/transfer-pricing/intra-group-financing/intercompany-lending-and-borrowing/ | 2026-10-26 |
| Vero, 2026 late-payment interest and interest with relief | https://www.vero.fi/en/individuals/payments/paying-taxes/interest-on-late-payments/ | 2026-10-26 |

Not yet confirmed: taxpayer-specific benchmarks, foreign corresponding adjustments, APA/MAP case outcomes and special financing/intangible/restructuring terms. These are transaction inputs or specialist procedures; no universal margin, treaty outcome or professional sign-off is asserted. Fresh whole-pack independent review is required for this revision.


[obligation]: https://www.vero.fi/en/businesses-and-corporations/business-operations/transfer-pricing/transfer-pricing-documentation/obligation-to-compile-a-transfer-pricing-documentation/
[detailed]: https://www.vero.fi/en/detailed-guidance/guidance/47978/transfer-pricing-documentation/
[form]: https://www.vero.fi/en/About-us/contact-us/forms/filling-instructions/78-explanation-of-transfer-prices-how-to-fill-out-the-form/
[faq]: https://www.vero.fi/en/businesses-and-corporations/business-operations/foreign-business-in-finland/supporting-high-growth-companies-with-international-tax-questions/faq---transfer-pricing/faq/when-does-a-company-need-to-maintain-and-submit-transfer-pricing-documentation-in-finland/

[law]: https://www.finlex.fi/fi/lainsaadanto/1995/1558
[amendment]: https://www.finlex.fi/api/media/statute/699004/mainPdf/main.pdf?timestamp=2016-12-28T22%3A00%3A00.000Z

[interest]: https://www.vero.fi/en/individuals/payments/paying-taxes/interest-on-late-payments/

[services]: https://www.vero.fi/en/businesses-and-corporations/business-operations/transfer-pricing/transfer-pricing-of-sale-of-services/
[loans]: https://www.vero.fi/en/businesses-and-corporations/business-operations/transfer-pricing/intra-group-financing/intercompany-lending-and-borrowing/
