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
version: 2.4
jurisdiction: LI
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
---

# Liechtenstein VAT preparation v2.4

Historical source/editorial evidence is in the [24 October review record](../../../docs/research/2026-10-24-liechtenstein-pack-review.md), confined to its exact predecessor and scope. The [current country review register](../../../ledgers/li-pack-review-evidence/README.md) identifies the 30 October review, repairs and exact-file verification. Named Liechtenstein accountant review remains open.

## Who this applies to

Use this 2026 source-cited draft for an ordinary business whose VAT affairs belong to the Liechtenstein Tax Administration. The country has its own [VAT Act, consolidated 1 January 2026][law]. Swiss ESTV practice applies by analogy with local deviations; it is not a replacement for Liechtenstein law, authority allocation or filing access. [Official practice-publications page][practice]

The earlier Guide's merchant-name classification, unknown-country/rate defaults and universal Swiss-portal instruction are superseded. Their history remains in Git. An invoice, contract, supply/location evidence, registration decision, deduction record and actual reporting period are required; a bank statement or the customer's name cannot establish taxable supply, export or recovery.

## Rates, bands and thresholds

| Item | Rule or 2026 figure | Primary source |
|---|---|---|
| Normal rate | 8.1% | MWSTG article 25(1); [rate page][rates] |
| Reduced rate | 2.6% for statutory categories | Article 25(2); [rate page][rates] |
| Accommodation | 3.8% for qualifying accommodation, including breakfast | Article 25(4) |
| Ordinary small-business exemption | Annual worldwide relevant turnover **less than CHF 100,000**, excluding article 21(2) exempt supplies | Articles 10(2)(a), 10(2a) |
| Specified nonprofit bodies | Separate **less than CHF 250,000** test | Article 10(2)(c), not every business |
| Registered domestic taxpayer: acquisition tax | Assess each qualifying acquisition; no CHF 10,000 exemption | Article 45(2)(a) |
| Recipient not already liable under article 10 | Acquisition-tax screen for qualifying acquisitions **over CHF 10,000** in the calendar year | Articles 45(2)(b), 47(2), 53(3) |

These tests do not alone establish liability: review the foreign-supplier, domestic/foreign-only and exempt-activity provisions in article 10. Article 14 distinguishes activity commencement, the end of exemption when prior-year turnover reaches the limit or a 12-month exceedance is foreseeable on commencement/expansion, and deregistration. Do not import another country's crossing-sale rule. Preserve a dated turnover forecast and authority registration decision. Compute the turnover limit from agreed consideration **excluding VAT**. Article 10(2)(d) separately exempts a Liechtenstein-established enterprise making only foreign supplies, with a possible article 11 waiver. For a foreign enterprise, article 10(2)(b) separately exempts the stated exclusively exempt/service/energy supplies; its article 8(1) service category does not exempt telecommunications/electronic supplies to non-taxable recipients. Establish the actual supply mix rather than deciding registration from the CHF 100,000 total alone. [MWSTG, articles 10–14][law]

| Additional 2026 control | Figure/rule | Official source |
|---|---|---|
| Annual movable/service input-tax use-change reduction |One fifth of the relevant input VAT per counted year; actual timing rules below |[MWSTG articles 31–32][law] |
| Annual immovable input-tax use-change reduction |One twentieth per counted year; property-base/special rules remain necessary |[MWSTG articles 31–32][law] |
| Late-payment and ordinary domestic refund interest |4% per year from 1 January 2026 |[MWSTV articles 142–143][ordinance]; [enacted 2025/548][interest-amendment] |
| Collection/payment threshold for those interest amounts |CHF 100 interest amount, not the underlying VAT/refund principal |[MWSTV articles 142(3),143(3)][ordinance] |

## The base

For every line retain seller and recipient, registration details, supply type and date, goods movement or receiving establishment, net/gross currency amount, tax shown, invoice and credit note, and documented business/deductible use. Separate taxable sales, exempt-without-deduction supplies, evidenced exempt-with-deduction supplies, acquisition tax, import tax and non-supply movements.

1. **Find the supply and place.** Articles 7–8 control goods and services. Article 8(1) normally looks to the receiving business/establishment; special rules cover property/accommodation, restaurant, transport and other services. A foreign hotel or an EU customer's name does not establish domestic acquisition tax or export. Preserve the applicable rule and evidence.
2. **Choose the category and rate.** Article 25(3) applies the normal rate to restaurant services. Qualifying takeaway/delivery food needs the stated organisational separation to use the reduced rate. Do not split a dine-in bill's food to 2.6% merely because groceries can be reduced. Alcohol is outside the reduced food category. The supply date/period, rather than invoice/payment date alone, controls a rate transition. [Rate page][rates]; [MWSTG, article 25][law]
3. **Test exemption/option separately.** Articles 21–23 distinguish excluded supplies, options and exempt supplies. No generic bank, government, SaaS, restaurant or internal-transfer label decides the legal treatment. Exports need goods-movement and statutory evidence; services to a foreign customer require their own place rule.
4. **Assess acquisition tax only when its gates hold.** For an ordinary article 8(1) service, establish domestic place, a foreign supplier not entered in the relevant register, and no article 45a exclusion. Article 45 contains other acquisition categories too; article 46 applies the ordinary base/rates. Registration of the recipient and the CHF 10,000 test differ as shown above. Telecom/electronic consumer supplies and emission rights need separate screens. Under article 48, the tax point depends on payment or, for an article-10 taxpayer using agreed consideration, receipt of the invoice. Do not classify every foreign debit as an import of services. [Articles 45–48][law]
5. **Determine input entitlement.** Articles 28–30 require the qualifying business purpose and exclude inputs for exempt supplies without an option, with specified exceptions. Preserve article 28(3) payment proof, invoice/import-assessment evidence and the use allocation. Article 30 corrects mixed use; article 31 addresses later loss of entitlement. Acquisition output and input can both be reportable even when the net is zero. No universal entertainment half-deduction, vehicle percentage or automatic zero-net recovery is supplied here. [Articles 26, 28–31][law]
6. Reconcile the supported bases/tax to the actual eMWST return fields and method. Under effective accounting, article 36 combines domestic/acquisition tax and the stated deferred-import tax with eligible input credits. The ordinary effective method must not be mixed with approved net-tax or flat-rate methods. Net-tax rates are not customer invoice rates. [Articles 36–38][law]

### Direct, shared and changing input entitlement

Keep three cost pools: directly deductible business use, directly excluded/nonbusiness use, and genuinely shared use. MWSTG article 30 requires correction according to actual use. MWSTV article 65 permits effective-use, authority flat methods and own calculations; articles 67–68 require the facts behind an own method to be comprehensively supported and plausibility-checked, with one or more methods giving an economically traceable, use-based result. A turnover ratio is not a universal statutory recovery percentage. If article 30(2)'s predominantly deductible-business-use condition is established, full provisional deduction with the permitted tax-period-end correction is a separate route. Reconcile provisional and final recovery so it is not claimed twice. [MWSTG article 30][law]; [MWSTV articles 65–68][ordinance]

For permanent loss of entitlement, article 31 corrects at the time entitlement ceases; article 32 permits later recovery in the period entitlement arises. Retain original VAT, initial recovery and every previous adjustment, use/asset dates, current existence and eligible/noneligible use fractions. Unused assets/services are corrected in full; used assets still present with a remaining value use the statutory time-value method. The stated consulting, accounting, recruitment, management and advertising services are presumed consumed on receipt, so do not retain an artificial five-year VAT balance for every old service bill. Temporary ineligible/eligible use instead uses the tax on an arm's-length rental, not automatic full permanent recapture. [MWSTG articles 31–32][law]; [MWSTV articles 69 and 72][ordinance]

For the ordinary time-value method, reduce the relevant input VAT by **one fifth per counted year for movable goods/services**, or **one twentieth for immovables**; book depreciation is not the VAT rule. MWSTV article 70(2) counts the entire first tax period of use, and no depreciation for the last still-unfinished period unless the use change occurs on that period's last day. MWSTG article 34 ordinarily uses the calendar year; an approved different business-year tax period changes the period facts. Do not count days/anniversaries or mistake the quarterly return period for the annual tax period. For a partial change, apply the remaining eligible/ineligible fraction under articles 69(4)/72(4), accounting for prior recovery. [MWSTG articles 31–34][law]; [MWSTV articles 69–70 and 72][ordinance]

For immovables, article 70(1)'s valuation excludes land and distinguishes value-enhancing from maintenance expenditure; major renovations have their own article 71 rule. Self-manufactured assets, property reconstruction/renovation, disputed values, special schemes and successive mixed-use changes still need their actual detailed method. The ordinary movable example below does not decide those cases. [MWSTV articles 69–72][ordinance]


### Retained predecessor rate and acquisition workpapers

#### Qualifying reduced goods and accommodation

Assume separately classified domestic supplies: CHF 1,000 net qualifying reduced-rate goods and CHF 200 net qualifying accommodation. A restaurant meal is not included in the reduced goods assumption.

The original executable block remains in the [retained-controls annex](../../../ledgers/liechtenstein-vat-evidence/retained-original-controls.md).

#### Acquisition tax with supported partial input entitlement

Assume an article-10 registered recipient, an established domestic article 8(1) service from a qualifying unregistered foreign supplier, no article 45a exclusion, a CHF 1,000 net base and documented 70% input entitlement under the effective method. Assess CHF 81 acquisition tax, with CHF 56.70 deductible and CHF 24.30 remaining. The supplier brand does not establish these gates.

The original executable block remains in the [retained-controls annex](../../../ledgers/liechtenstein-vat-evidence/retained-original-controls.md).

#### Invoice food versus restaurant classification

The same CHF 500 net food value gives CHF 13 at 2.6% only on established qualifying goods/takeaway facts, versus CHF 40.50 for a normal-rate restaurant service. The CHF 27.50 difference is a classification control, not an election for the cheaper result.

The original executable block remains in the [retained-controls annex](../../../ledgers/liechtenstein-vat-evidence/retained-original-controls.md).

## Deadlines and filing

- Article 35 provides quarterly periods, half-years for the net-tax method, and application routes for monthly regular input-credit cases or annual reporting where taxable annual turnover does not exceed CHF 5,005,000. Obtain the actual approval; article 35a adds annual-method restrictions. Annual filing does not mean there are no interim payments: article 76a provides authority-set instalments. This draft does not select an election for the taxpayer.
- Article 53 requires ordinary registration within 30 days of liability; solely acquisition-tax-liable recipients have the separate year-end 60-day registration/declaration route. Follow the mandatory current eMWST channel. For the acquisition-tax-only route, the authority instructs the recipient to select and submit **„Anmeldung Bezugsteuer“** in eMWST; the former register number was deactivated from 1 January 2025 and acquisition-tax return forms are no longer supplied automatically. Retain the actual period and submission evidence instead of waiting for an old paper form. [Current eMWST instructions, read 30 October 2026][portal]
- File within 60 days after the allocated period under article 58; article 76 separately requires payment within 60 days. Reconcile any authority extension notice: a filing extension does not prove payment was extended. Confirm actual calendar/holiday treatment and period-specific notices; this Guide does not assign unverified 2026 exceptional dates.
- Article 59 requires annual-account errors to be corrected by the return covering the 180th day after year-end, and known past-period errors to be corrected within the stated finality/limitation rules. Use the authority-prescribed correction form in eMWST. The actual current field workflow remains to be exercised; preserve both original and corrective evidence.

## Penalties and interest

- Article 77 imposes late-payment interest without reminder, with its stated no-loss exception; the 2026 rate and threshold are now supplied below. Article 86 permits a fine up to CHF 10,000 for its specified intentional/negligent procedural breaches, including late filing after reminder. It is not an automatic charge on every late return. Tax evasion, estimates, interest, payment enforcement and criminal cases require separate analysis. [MWSTG, cited articles][law]

MWSTV articles 142–143 set the 2026 late-payment and article 78(4) ordinary refund rates at **4% per year from 1 January 2026**. Their preceding 2024–2025 rate is 4.5%; split a period crossing the rate change by the applicable dates instead of applying today's rate to every earlier day. Article 77 also covers late/incomplete instalments under annual reporting and exempts its stated error-with-no-tax-loss reassessment case. Establish tax amount, due/receipt/payment dates and the applicable interest duration before calculating; the exact day-count convention is not supplied here. [MWSTG article 77][law]; [MWSTV articles 142–143][ordinance]; [enacted amendment 2025/548][interest-amendment]

Late interest is collected, and the stated refund interest is paid, only from an **interest amount of CHF 100**. The threshold concerns interest, not the amount of tax owed or principal refund. For ordinary taxable-person refunds under MWSTG article 78(4), interest runs from the 61st day after receipt of the return or written refund request until payment; the Act reserves its set-off/security routes. This is not the separate foreign-business reimbursement timetable. [MWSTG article 78][law]; [MWSTV articles 142(3),143(3)][ordinance]

## Cross-border points

For a foreign enterprise established outside Liechtenstein/Switzerland, the authority says an existing Swiss VAT registration or taxable Swiss supplies put collection with the Swiss ESTV; additional Liechtenstein sales are accounted for there. Check the actual registration/authority allocation before choosing a portal. A Liechtenstein-administered taxpayer uses [eMWST][portal], mandatory since January 2025 for registration, returns, corrections and communications; old lilog accounts/authorisations are not sufficient. Retain current access and representation evidence. [Registration guidance][registration]; [eMWST instructions][portal]

## Two worked examples that recompute

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

### A partial use change counts tax periods rather than anniversaries

Assume a movable asset with CHF 10,000 documented original input VAT, fully and properly recovered, first used on 1 December 2023. The taxpayer uses calendar-year tax periods. On 1 June 2026, 50% of its use permanently ceases to qualify. The first 2023 tax period counts in full, as do 2024 and 2025; the unfinished 2026 period does not. Three fifths are depreciated for VAT purposes, leaving CHF 4,000. The 50% loss of entitlement produces a CHF 2,000 correction. The original VAT is an established case input, not an assertion about a historical invoice rate. No special asset, prior correction, temporary use or disputed allocation is present. [MWSTG articles 30–31][law]; [MWSTV articles 69–70][ordinance]

```oa-check
name: Liechtenstein assumed movable asset partial use change calendar periods
inputs:
  documented_original_input_vat: 10000
  established_counted_tax_periods: 3
  statutory_movable_annual_reduction: 0.20
  established_fraction_losing_entitlement: 0.50
steps:
  cumulative_vat_reduction_fraction: established_counted_tax_periods * statutory_movable_annual_reduction
  remaining_vat_fraction: max(0, 1 - cumulative_vat_reduction_fraction)
  remaining_time_value_vat: documented_original_input_vat * remaining_vat_fraction
  required_partial_correction: remaining_time_value_vat * established_fraction_losing_entitlement
expected:
  cumulative_vat_reduction_fraction: 0.60
  remaining_vat_fraction: 0.40
  remaining_time_value_vat: 4000
  required_partial_correction: 2000
```

## Ask the client first

Obtain the registration/authority decision, approved method/period, portal representation, invoices, contracts, location/transport/customs evidence, VAT bases and actual use. Retain prior returns, advance payments and notices. Refer uncertain supply location, foreign enterprise allocation, agency/platform transactions, exemption/option, groups, property, partial exemption, method changes, foreign/special refunds, disputed interest periods and contested tax. No actual return, payment or production account was accessed. Complete special-case/amendment scope, operational field testing and named accountant review remain open; VAT coverage stays partial.

## Sources

The 24 October reviewed scope remains pinned to its predecessor. The selected 30 October statutory and actual browser reads below support the new writer methods; they do not extend the historical independent review.

- [Liechtenstein MWSTG, consolidated1 January 2026][law]: historical 24 October selected articles3,7–8,10–14,25–31,35–38,45–48,52–54,58–59,66,76–77 and86. The ledger separately records the 30 October ordinary registration/input-use-change/tax-period/payment/refund passages, including32–34 and78. Official PDF/text retrieval is distinguished from web-reader transport; neither is a complete amendment/exemption/treaty audit.
- [MWSTV, consolidated1 January 2026][ordinance], selected 65–72 and142–143, and [enacted 2025/548][interest-amendment], effective1 January 2026, read 30 October 2026 for the ordinary input-correction and interest method.
- [Actual eMWST channel][portal], [registration/authority allocation][registration] and [Swiss-practice-by-analogy page][practice]: selected relevant paragraphs read in the normal browser30October2026, with exact selected excerpts retained in the ledger evidence. This does not assert every page, every accordion or private portal field was audited.
- [Current rate categories][rates] and [2025 changes][changes]: historical 24 October access retained; no fresh whole-page read claimed. The original direct bulk HTML attempt met HTTP 403; successful web/browser observations remain separately identified.

Not yet confirmed: complete special-supply/sector/group/property/renovation/self-manufactured methods; contested successive changes, valuations and allocation evidence; exact interest day-count/application; current authenticated return fields, upload/correction execution and final calendar adjustments. Source access and writer checks do not establish comprehensive coverage or accountant attestation.

[ordinance]: https://www.gesetze.li/konso/pdf/2009340000
[interest-amendment]: https://www.gesetze.li/chrono/pdf/2025548000
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
