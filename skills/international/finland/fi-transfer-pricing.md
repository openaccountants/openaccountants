---
name: fi-transfer-pricing
description: >
  Screen Finnish transfer-pricing documentation obligations, prepare
  cross-border related-party evidence, distinguish Form 78 from the full
  documentation, and track authority requests. Detailed statutory, method,
  reporting and named Finnish accountant review remain outstanding.
jurisdiction: FI
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.5
---

# Finland transfer-pricing documentation v0.5

## Who this applies to

The Finnish Tax Administration's guidance addresses foreign related-party transactions of Finnish taxpayers and dealings between a foreign enterprise and its Finnish PE. The pricing principle also applies to small enterprises outside the full documentation obligation. [Obligation guidance][obligation]

This draft uses official administrative guidance read on 23 October 2026. The obligation page says it will be updated and displays a 2022 update date. Consolidated Finnish sections 14a–14c, 31, 32 and 32a have now been read directly from the official Finlex page's embedded statutory text; the earlier indexed and 2016-amendment work is preserved. Full specialist scope, procedural interaction and named Finnish accountant review remain open.

## Related parties and the actual transaction

Section 31 covers direct/indirect majority capital or votes, majority appointment rights, common management and other actual control, including common third-party control. Analyse contracts, functions, assets, risks, transaction characteristics, economic conditions and strategies before pricing the actual transaction. Replacing that transaction is an exceptional statutory route with additional conditions, not an ordinary benchmarking shortcut. [Assessment Procedure Act, section 31][law]

## Rates, bands and thresholds

The detailed guidance defines the SME exclusion using all three requirements: fewer than 250 employees; turnover at most EUR 50 million **or** balance sheet at most EUR 43 million; and compliance with the Commission recommendation's SME criteria. Group and linked/partner-enterprise relationships matter. A small Finnish subsidiary cannot determine its status using its standalone figures alone. [Detailed guidance, section 4.3][detailed]

The detailed guidance and Form 78 instructions use turnover **exceeding** EUR 50 million and balance sheet **exceeding** EUR 43 million for that financial-size route. A separate FAQ uses “or more”. Section 14a supports the inclusive SME financial ceilings in the detailed guidance, so the FAQ wording must not replace that statutory test. Employee count, EU SME status, group relationships and changes across years still require their own checks. [Assessment Procedure Act, section 14a][law]; [Detailed guidance][detailed]; [Form 78][form]; [FAQ][faq]

## Requests and filing

The obligation guidance states: annual documentation; Finnish, Swedish or English; submission within 60 days of request; supplementary information within 90 days. Section 14c sets the earliest presentation date for that year's documentation at six months after the financial-year-end month; this is not worded as a ban on issuing an earlier request. Extensions can be requested. It describes a two-consecutive-year size transition and a maximum EUR 25,000 documentation sanction. Calendar the request and statutory presentation restriction together. The authority may extend the presentation/supplement deadlines on request; section 14c says that extension decision cannot be appealed. Current penalty conditions remain a separate check. [Section 14c][law]; [Obligation guidance][obligation]

Form 78 is separate from the documentation. Its instructions say documentation is provided on request rather than attached to the return. Where no foreign related-party transactions occurred during the year, those instructions say Form 78 is unnecessary. Check the taxpayer's facts and the applicable return instructions before filing. [Form 78][form]

### EUR 500,000 simplification is assessed by counterparty

Detailed guidance section 4.4 describes reduced documentation where annual controlled dealings with a particular associated enterprise have an arm's-length value no greater than EUR 500,000. Aggregate that counterparty's dealings; do not test each invoice separately. Its examples include service income plus loan interest, and separately a newly drawn loan principal. Repayment of that principal is not counted as another borrowing. [Detailed guidance, section 4.4][detailed]

The simplification can remove the Master File requirement when no counterparty exceeds the threshold. For qualifying below-threshold dealings, it removes specified Local File functional/comparability/method content, while other taxpayer information remains required. It does not exempt the pricing from the arm's-length principle. Keep loan movements and valuation evidence for the applicability check. [Section 4.4][detailed]

### Statutory documentation contents

Section 14b identifies these group-level categories: organisation; business; intangibles activity; financing; financial statements or corresponding available information; and advance tax positions/agreements concerning cross-border income allocation. [Section 14b(1); 2016 amending Act][amendment]

At taxpayer level it requires organisation/management; business; related-party relationships; controlled transactions and PE dealings; functional analysis; comparability analysis and available comparables; method and application; financial statements or equivalent; and relevant foreign advance tax positions/agreements. These are content categories, not permission to replace transaction evidence with headings. [Section 14b(2)][amendment]

A separable independently operated business area can be described at group level, but central group functions/transactions remain included and the authority can request other business areas. Section 14b also addresses a standalone foreign enterprise with a Finnish PE. Apply the specific simplifications above separately. [Section 14b(3)–(5)][law]

## Method selection and calculation evidence

Select the most reliable method for the delineated transaction and available comparables. Vero distinguishes CUP (price), resale price/cost plus (gross margin), TNMM (net indicator) and profit split. If equally reliable, traditional transaction methods take preference over profit methods, and CUP over other methods. Record the tested party, base, adjustments and calculation; avoid a universal markup. [Detailed guidance, sections 6.6–6.7][detailed]

Gross cost plus and a net-cost TNMM are different analyses. Do not import every overhead into a gross cost base or transfer a net margin to gross costs without supporting comparability. [Detailed guidance, section 6.7.2][detailed]

## Penalties and cross-border follow-through

Sections 32(1)(2) and 32a provide a maximum EUR 25,000 increase for the specified late, materially incomplete or incorrect documentation/supplement failures. It is not an automatic fixed fee or a ceiling on every substantive tax adjustment. Check the failure, hearing, applicable penalty provision and decision separately. [Assessment Procedure Act][law]

Reconcile a proposed adjustment with the foreign counterparty, accounts and returns. Corresponding adjustment, treaty dispute relief and APA routes need a separate verified procedure; this draft establishes neither automatic foreign relief nor an agreed pricing result. The [CbCR Guide](fi-country-by-country-reporting.md) addresses a separate reporting obligation.

## Preparation workpaper

Use this as an evidence checklist, not a claim that it reproduces every statutory local-file requirement:

- Identify the taxpayer, PE, related parties, residences and period.
- Record group structure and reconcile the size/SME calculation to the underlying accounts.
- List each transaction, agreement, booked amount and relevant currency.
- Describe actual conduct, functions, assets and risks; preserve evidence supporting the chosen pricing analysis.
- Connect the analysis and any adjustment to the accounts, tax computation and Form 78.
- Keep the authority's request, receipt date, requested scope, response calendar and delivery acknowledgement together.

A documentation exemption does not establish an acceptable price. Nor does an authority request establish the correct margin: the transaction evidence still needs substantive analysis. No benchmark markup or interest rate is supplied by this checklist.

## Worked example

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

### 2. Counterparty aggregation

Assume EUR 350,000 services and EUR 180,000 interest with one associated enterprise, both at established arm's-length values. EUR 530,000 exceeds the simplification threshold by EUR 30,000. The example assumes no disputed classification or double counting.

```oa-check
name: Finland documentation counterparty aggregation
inputs:
  service_value: 350000
  interest_value: 180000
  simplification_limit: 500000
steps:
  counterparty_total: service_value + interest_value
  excess_over_limit: counterparty_total - simplification_limit
expected:
  counterparty_total: 530000
  excess_over_limit: 30000
```

### 3. Gross cost-plus arithmetic on established assumptions

Assume a properly supported gross cost base of EUR 100,000 and an invented 8% comparable markup, with method/base/benchmark eligibility already established. Revenue is EUR 108,000; the markup is not an 8% sales margin. No Finnish safe harbour or recommended rate is implied.

```oa-check
name: Finland assumed gross cost plus computation
inputs:
  established_gross_cost_base: 100000
  assumed_supported_markup: 0.08
steps:
  gross_profit: established_gross_cost_base * assumed_supported_markup
  transaction_revenue: established_gross_cost_base + gross_profit
  sales_margin_percent: gross_profit / transaction_revenue * 100
expected:
  gross_profit: 8000
  transaction_revenue: 108000
  sales_margin_percent: 7.407407407407407
```

## Ask the client first

- Which foreign parties and PE dealings exist, and what establishes the relationships?
- What are the group size figures, ownership links and prior-year changes?
- What transactions and pricing evidence reconcile to the accounts?
- Has an authority requested documents or supplements, and when was it received?
- What return and Form 78 submissions already exist?

## Sources and review limits

Read 23 October 2026. The obligation page was opened directly; detailed guidance, including sections 6.6–6.7, Form 78 and FAQ passages were retrieved from indexed official text.

- [Finlex consolidated Assessment Procedure Act][law], sections 14a–14c, 31, 32 and 32a: direct official HTML statutory text extracted on 23 October after the browser reader returned a navigation shell. The retrieval/hashes are in the country research record. Earlier [2016 amending Act][amendment] work is retained.
- [Documentation obligation][obligation], referring to Assessment Procedure Act sections 14a and 14c.
- [Detailed documentation guidance][detailed], SME definition and related calculations.
- [Form 78 instructions][form]; [documentation FAQ][faq].

Not yet confirmed: remaining amendment/procedural scope, detailed application of master/local content and simplification eligibility, benchmark searches and transaction-specific method application, financing/intangibles/restructuring cases, dispute/APA procedures and live filing. Named Finnish accountant review remains outstanding; the independent source-review scope is recorded in the [country README](README.md#evidence-and-next-action). TP and the country pack remain partial.

[obligation]: https://www.vero.fi/en/businesses-and-corporations/business-operations/transfer-pricing/transfer-pricing-documentation/obligation-to-compile-a-transfer-pricing-documentation/
[detailed]: https://www.vero.fi/en/detailed-guidance/guidance/47978/transfer-pricing-documentation/
[form]: https://www.vero.fi/en/About-us/contact-us/forms/filling-instructions/78-explanation-of-transfer-prices-how-to-fill-out-the-form/
[faq]: https://www.vero.fi/en/businesses-and-corporations/business-operations/foreign-business-in-finland/supporting-high-growth-companies-with-international-tax-questions/faq---transfer-pricing/faq/when-does-a-company-need-to-maintain-and-submit-transfer-pricing-documentation-in-finland/

[law]: https://www.finlex.fi/fi/lainsaadanto/1995/1558
[amendment]: https://www.finlex.fi/api/media/statute/699004/mainPdf/main.pdf?timestamp=2016-12-28T22%3A00%3A00.000Z
