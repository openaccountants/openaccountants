---
name: liechtenstein-vat
description: >
  Prepare 2026 Liechtenstein VAT workpapers for ordinary registered businesses.
  Use for MWST registration, eMWST, rate selection, domestic sales, qualifying
  service acquisition tax, input deductions, period reconciliation and corrections.
  Establish the responsible authority, actual supply and evidence before using a
  return field. This Guide replaces the earlier blanket Swiss-filing instruction
  and merchant-name defaults with Liechtenstein law and authority instructions.
  It does not decide all cross-border supplies, platform sales, margin or net-tax
  methods, property, groups, sector exemptions or complex partial recovery. Bank
  statements alone do not establish VAT treatment. The source-cited draft remains
  subject to named local accountant review.
version: 2.2
jurisdiction: LI
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
---

# Liechtenstein VAT preparation v2.2

Independent source/editorial review evidence and correction status are in the [dated whole-pack review record](../../../docs/research/2026-10-24-liechtenstein-pack-review.md). Apply its exact revision and scope limits. Named Liechtenstein accountant review remains open.

## Who this applies to

Use this 2026 source-cited draft for an ordinary business whose VAT affairs belong to the Liechtenstein Tax Administration. The country has its own [VAT Act, consolidated 1 January 2026][law]. Swiss ESTV practice applies by analogy with local deviations; it is not a replacement for Liechtenstein law, authority allocation or filing access. [Official practice-publications page][practice]

The earlier Guide's merchant-name classification, unknown-country/rate defaults and universal Swiss-portal instruction are superseded. Their history remains in Git. An invoice, contract, supply/location evidence, registration decision, deduction record and actual reporting period are required; a bank statement or the customer's name cannot establish taxable supply, export or recovery.

## Rates, threshold and authority screen

| Item | Rule or 2026 figure | Primary source |
|---|---|---|
| Normal rate | 8.1% | MWSTG article 25(1); [rate page][rates] |
| Reduced rate | 2.6% for statutory categories | Article 25(2); [rate page][rates] |
| Accommodation | 3.8% for qualifying accommodation, including breakfast | Article 25(4) |
| Ordinary small-business exemption | Annual worldwide relevant turnover **less than CHF 100,000**, excluding article 21(2) exempt supplies | Articles 10(2)(a), 10(2a) |
| Specified nonprofit bodies | Separate **less than CHF 250,000** test | Article 10(2)(c), not every business |
| Registered domestic taxpayer: acquisition tax | Assess each qualifying acquisition; no CHF 10,000 exemption | Article 45(2)(a) |
| Recipient not already liable under article 10 | Acquisition-tax screen for qualifying acquisitions **over CHF 10,000** in the calendar year | Articles 45(2)(b), 47(2), 53(3) |

These tests do not alone establish liability: review the foreign-supplier, domestic/foreign-only and exempt-activity provisions in article 10. Article 14 distinguishes activity commencement, the end of exemption when prior-year turnover reaches the limit or a 12-month exceedance is foreseeable on commencement/expansion, and deregistration. Do not import another country's crossing-sale rule. Preserve a dated turnover forecast and authority registration decision. [MWSTG, articles 10–14][law]

For a foreign enterprise established outside Liechtenstein/Switzerland, the authority says an existing Swiss VAT registration or taxable Swiss supplies put collection with the Swiss ESTV; additional Liechtenstein sales are accounted for there. Check the actual registration/authority allocation before choosing a portal. A Liechtenstein-administered taxpayer uses [eMWST][portal], mandatory since January 2025 for registration, returns, corrections and communications; old lilog accounts/authorisations are not sufficient. Retain current access and representation evidence. [Registration guidance][registration]; [eMWST instructions][portal]

## Build the transaction workpaper

For every line retain seller and recipient, registration details, supply type and date, goods movement or receiving establishment, net/gross currency amount, tax shown, invoice and credit note, and documented business/deductible use. Separate taxable sales, exempt-without-deduction supplies, evidenced exempt-with-deduction supplies, acquisition tax, import tax and non-supply movements.

1. **Find the supply and place.** Articles 7–8 control goods and services. Article 8(1) normally looks to the receiving business/establishment; special rules cover property/accommodation, restaurant, transport and other services. A foreign hotel or an EU customer's name does not establish domestic acquisition tax or export. Preserve the applicable rule and evidence.
2. **Choose the category and rate.** Article 25(3) applies the normal rate to restaurant services. Qualifying takeaway/delivery food needs the stated organisational separation to use the reduced rate. Do not split a dine-in bill's food to 2.6% merely because groceries can be reduced. Alcohol is outside the reduced food category. The supply date/period, rather than invoice/payment date alone, controls a rate transition. [Rate page][rates]; [MWSTG, article 25][law]
3. **Test exemption/option separately.** Articles 21–23 distinguish excluded supplies, options and exempt supplies. No generic bank, government, SaaS, restaurant or internal-transfer label decides the legal treatment. Exports need goods-movement and statutory evidence; services to a foreign customer require their own place rule.
4. **Assess acquisition tax only when its gates hold.** For an ordinary article 8(1) service, establish domestic place, a foreign supplier not entered in the relevant register, and no article 45a exclusion. Article 45 contains other acquisition categories too; article 46 applies the ordinary base/rates. Registration of the recipient and the CHF 10,000 test differ as shown above. Telecom/electronic consumer supplies and emission rights need separate screens. Under article 48, the tax point depends on payment or, for an article-10 taxpayer using agreed consideration, receipt of the invoice. Do not classify every foreign debit as an import of services. [Articles 45–48][law]
5. **Determine input entitlement.** Articles 28–30 require the qualifying business purpose and exclude inputs for exempt supplies without an option, with specified exceptions. Preserve article 28(3) payment proof, invoice/import-assessment evidence and the use allocation. Article 30 corrects mixed use; article 31 addresses later loss of entitlement. Acquisition output and input can both be reportable even when the net is zero. No universal entertainment half-deduction, vehicle percentage or automatic zero-net recovery is supplied here. [Articles 26, 28–31][law]
6. Reconcile the supported bases/tax to the actual eMWST return fields and method. Under effective accounting, article 36 combines domestic/acquisition tax and the stated deferred-import tax with eligible input credits. The ordinary effective method must not be mixed with approved net-tax or flat-rate methods. Net-tax rates are not customer invoice rates. [Articles 36–38][law]

## Periods, filing, payment and correction

- Article 35 provides quarterly periods, half-years for the net-tax method, and application routes for monthly regular input-credit cases or annual reporting where taxable annual turnover does not exceed CHF 5,005,000. Obtain the actual approval; article 35a adds annual-method restrictions. Annual filing does not mean there are no interim payments: article 76a provides authority-set instalments. This draft does not select an election for the taxpayer.
- Article 53 requires ordinary registration within 30 days of liability; solely acquisition-tax-liable recipients have the separate year-end 60-day registration/declaration route. Follow the mandatory current eMWST channel.
- File within 60 days after the allocated period under article 58; article 76 separately requires payment within 60 days. Reconcile any authority extension notice: a filing extension does not prove payment was extended. Confirm actual calendar/holiday treatment and period-specific notices; this Guide does not assign unverified 2026 exceptional dates.
- Article 59 requires annual-account errors to be corrected by the return covering the 180th day after year-end, and known past-period errors to be corrected within the stated finality/limitation rules. Use the authority-prescribed correction form in eMWST. The actual current field workflow remains to be exercised; preserve both original and corrective evidence.
- Article 77 imposes late-payment interest without reminder, with its stated no-loss exception; the current applicable interest rate has not been verified here. Article 86 permits a fine up to CHF 10,000 for its specified intentional/negligent procedural breaches, including late filing after reminder. It is not an automatic charge on every late return. Tax evasion, estimates, interest, payment enforcement and criminal cases require separate analysis. [MWSTG, cited articles][law]

## Worked controls

Amounts are hypothetical unless expressly identified otherwise. A passing calculation establishes neither classification nor permission to file.

### VAT-inclusive ordinary domestic invoice

Assume an established domestic standard-rate taxable supply for CHF 10,810 gross. The customer country/name alone is not that evidence.

```oa-check
name: Liechtenstein assumed standard VAT inclusive invoice
inputs:
  established_gross_price: 10810
  established_rate: 0.081
steps:
  net_price: established_gross_price / (1 + established_rate)
  output_vat: established_gross_price - net_price
expected:
  net_price: 10000
  output_vat: 810
```

### Qualifying reduced goods and accommodation

Assume separately classified domestic supplies: CHF 1,000 net qualifying reduced-rate goods and CHF 200 net qualifying accommodation. A restaurant meal is not included in the reduced goods assumption.

```oa-check
name: Liechtenstein assumed reduced goods and accommodation rates
inputs:
  established_reduced_net: 1000
  reduced_rate: 0.026
  established_accommodation_net: 200
  accommodation_rate: 0.038
steps:
  reduced_vat: established_reduced_net * reduced_rate
  accommodation_vat: established_accommodation_net * accommodation_rate
  combined_output_vat: reduced_vat + accommodation_vat
expected:
  reduced_vat: 26
  accommodation_vat: 7.60
  combined_output_vat: 33.60
```

### Acquisition tax with supported partial input entitlement

Assume an article-10 registered recipient, an established domestic article 8(1) service from a qualifying unregistered foreign supplier, no article 45a exclusion, a CHF 1,000 net base and documented 70% input entitlement under the effective method. Assess CHF 81 acquisition tax, with CHF 56.70 deductible and CHF 24.30 remaining. The supplier brand does not establish these gates.

```oa-check
name: Liechtenstein assumed acquisition tax with partial input entitlement
inputs:
  established_service_base: 1000
  established_rate: 0.081
  established_deductible_fraction: 0.70
steps:
  acquisition_tax: established_service_base * established_rate
  deductible_input: acquisition_tax * established_deductible_fraction
  net_tax_effect: acquisition_tax - deductible_input
expected:
  acquisition_tax: 81
  deductible_input: 56.70
  net_tax_effect: 24.30
```

### Invoice food versus restaurant classification

The same CHF 500 net food value gives CHF 13 at 2.6% only on established qualifying goods/takeaway facts, versus CHF 40.50 for a normal-rate restaurant service. The CHF 27.50 difference is a classification control, not an election for the cheaper result.

```oa-check
name: Liechtenstein assumed food supply classification comparison
inputs:
  established_net_price: 500
  qualifying_reduced_rate: 0.026
  restaurant_rate: 0.081
steps:
  qualifying_goods_vat: established_net_price * qualifying_reduced_rate
  restaurant_vat: established_net_price * restaurant_rate
  difference: restaurant_vat - qualifying_goods_vat
expected:
  qualifying_goods_vat: 13
  restaurant_vat: 40.50
  difference: 27.50
```

## Ask and refer

Obtain the registration/authority decision, approved method/period, portal representation, invoices, contracts, location/transport/customs evidence, VAT bases and actual use. Retain prior returns, advance payments and notices. Refer uncertain supply location, foreign enterprise allocation, agency/platform transactions, exemption/option, groups, property, partial exemption, method changes, refunds/late interest and contested tax. No actual return, payment or production account was accessed. Full legal/amendment scope, operational field testing and named accountant review remain open; VAT coverage stays partial.

## Sources and read limits

Read 24 October 2026:

- [Liechtenstein MWSTG, consolidated 1 January 2026][law]: selected articles 3, 7–8, 10–14, 25–31, 35–38, 45–48, 52–54, 58–59, 66, 76–77 and 86. Direct official PDF retrieval/text was available when the web reader failed. This is not a complete amendment, ordinance, exemption or treaty review.
- [Actual Liechtenstein eMWST channel][portal], [registration/authority allocation][registration], [current rate categories][rates], [practice-publication status][practice] and [2025 changes][changes]. These authority pages were read through the web reader; the direct bulk HTML reader encountered HTTP 403 and is not represented as successful transport evidence.

[law]: https://www.gesetze.li/konso/pdf/2009330000
[portal]: https://www.llv.li/de/landesverwaltung/steuerverwaltung/mehrwertsteuer/e-mwst
[registration]: https://www.llv.li/de/landesverwaltung/steuerverwaltung/mehrwertsteuer/wer-ist-mwst-steuerpflichtig
[rates]: https://www.llv.li/de/unternehmen/steuern-abgaben-versicherung/mehrwertsteuer/mwst-steuersaetze
[practice]: https://www.llv.li/de/landesverwaltung/steuerverwaltung/mehrwertsteuer/publikationen-zur-mehrwertsteuerpraxis
[changes]: https://www.llv.li/de/landesverwaltung/steuerverwaltung/mehrwertsteuer/aenderungen-ab-01012025

<!-- openaccountants-cta-block -->

---

## Talk to an accountant

Find the current Guide and professional-review status at [OpenAccountants](https://www.openaccountants.com).
