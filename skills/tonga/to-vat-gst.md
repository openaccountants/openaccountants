---
name: to-vat-gst
description: >
  Classify Tonga 2026 Consumption Tax supplies, registration, import values and eligible input credits; compute ordinary CT working papers and filing reconciliations. Use for Tonga VAT/GST queries while keeping unrecovered special Orders, live form mapping and disputed classifications outside usable instructions.
jurisdiction: TO
category: international
type: computation
tax_year: 2026
last_updated: 2026-11-22
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
version: 0.2
---

# Tonga Consumption Tax v0.2

**General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Prepare a Tonga 2026 Consumption Tax (CT) classification, registration and ordinary return working paper. CT is the VAT-type consumption tax; it is not an additional tax on an already CT-inclusive amount. Determine taxable person, enterprise, place, time, value and exemption/zero-rating before calculating. Employment and a hobby/leisure activity are outside the enterprise definition; a foreign customer or a supplier name alone does not establish export or exemption.

| Item | Amount / rule and complete conditions | Official source |
|---|---|---|
| Standard CT | 15% on taxable supplies by a taxable person and taxable imports; do not charge on a proved exempt supply/import. | [s 5(1)-(4)](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2003/2003-0029/ConsumptionTaxAct_3.pdf) |
| Compulsory ordinary registration | TOP 100,000 or more taxable supplies in a past 12-month-or-less period, or reasonable expectation at beginning of a 12-month period; consider associates. Exactly TOP 100,000 qualifies. | [s 6(1)-(2)](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2003/2003-0029/ConsumptionTaxAct_3.pdf) |
| Registration exceptions/additions | Licensing authorities must apply under s 6(3); specified foreign-service recipients include received services plus their taxable supplies in the TOP 100,000 test. Apply within 7 days of obligation. | [s 6(2A),(3),(5)](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2003/2003-0029/ConsumptionTaxAct_3.pdf) |
| Voluntary registration | Below-threshold taxable supplier may apply; fixed business place, proper past/current records, revenue-law compliance and reliable regular returns are conditions. | [ss 6(4),7(3)](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2003/2003-0029/ConsumptionTaxAct_3.pdf) |
| Exports | 0% (0 in words on the page) for exported goods and services supplied for use outside Tonga under the recovered 2005 Order, corroborated by current guidance; prove actual export/use and applicable current classification. | [GS3B/2005 Order para 2(a)-(b); MORC Taxable Supplies](https://www.revenue.gov.to/sites/default/files/inline-files/ConsumptionTaxRegulations2005.pdf) |
| Exempt supply categories | Recovered Order lists medical prescription/dental/nursing/health, education, financial, public transport and residential land lease categories. Current guidance excludes tour-operator passenger transport from its public-transport description. Do not claim an input credit for exempt use. | [GS3B/2005 Order para 1; CT Act s 17(5)](https://www.revenue.gov.to/sites/default/files/inline-files/ConsumptionTaxRegulations2005.pdf) |
| Normal tax period/deadline | Current Ministry guidance:1 calendar month; return and payment by 28 days after period end, with next-business-day tax rule. Nil returns remain required. | [What is a CT Period?; CT Act ss 21-22; MORC CT Returns](https://www.revenue.gov.to/consumption-tax-obligations) |
| Inclusive amount | CT fraction 15/115 derived from r/(100+r) at the confirmed standard rate; a CT-inclusive price is not taxed again at 15% of that whole price. | [s 11(1),(6)](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2003/2003-0029/ConsumptionTaxAct_3.pdf) |
| Import base | Customs value + customs duty/excise/other fiscal charges other than CT + relevant incidental services not already included; no universal duty rate is supplied. | [ss 4(7),13-14A](https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2003/2003-0029/ConsumptionTaxAct_3.pdf) |

## Ask the client first

Obtain actual CT/TIN registration and effective date, all business activities/trading names/associates and historic/forecast taxable supplies; actual period and Ministry notices; sales, invoices, advance receipts, exports and destination/use proof; supplier CT status/invoices, import entries and customs/charge/service breakdown; business/private/exempt/entertainment/vehicle/fuel use; credit/debit adjustments, stock on registration/cancellation and prior carryforwards/refund records. Obtain the actual exemption/zero-rating instrument for disputed items.

## The method, step by step

### Establish classification, registration and the period

Use CT Act ss 2,5-8. The ordinary turnover test counts the value of taxable supplies, excluding exempt supplies and CT itself, across the person's trading names. The Minister must have regard to the value of taxable supplies made by an associate when determining whether the person must apply under s 6(1). Licensing authorities and imported-service recipients have their own registration branches. Do not substitute the old “exceeds” test for “or more”, or assume the threshold excuses every licensing authority. Voluntary registration is conditional, not automatic merely because turnover is low.

Get a TIN first if needed; submit the current CT Application for Registration (MORC identifies Form 1/Regulation 10) with the actual compulsory checklist/supporting documents. Retain the decision letter, effective date, first-return date and registration certificate. The published amendment changes certificate display/copies, but its commencement condition is unresolved. Hold that amendment-dependent application and obtain the actual certificate/display direction from the authority; unofficial copies are not proof of registration. A saved application is not proof of registration. Do not charge CT before the actual legal effective date or claim a credit for a supply not taxable at its time.

For an actual cessation, apply to cancel within 7 days under s 8; voluntary registration ordinarily cannot be cancelled just for falling below threshold until 2 years from registration. A licensing authority may cancel only on cessation under s 8(3). The written cancellation notice determines the cancellation date. Under s 8(8)-(9), goods on hand for which a credit was allowed are deemed supplied immediately before cancellation at their original acquisition consideration; assess that deemed supply, stop holding out/charging as registered, return the certificate and lodge/pay the final return within 28 days of cancellation. Resolve the actual ownership/entity transition rather than carry the old registration automatically into a new company.

### Determine time, place and taxable value

Normal time of supply is the earlier invoice or payment/part-payment date under s 9(1). Gifts, application of goods to private/exempt use and periodic/lease supplies have their own s 9 rules. Goods are generally supplied where delivered/made available, or where transport starts. Services normally use the supplier's business place, but s 10 brings specified rights, professional/data/advertising/personnel/agency services used in Tonga, real-property services and licensing into its special Tonga place rules. Do not zero-rate a service just because the invoice is overseas.

Use consideration excluding CT; strip CT from an inclusive price using the statutory fraction. Special rules apply to associate under-value supplies, private/exempt use and post-sale changes. Imports are valued using the full statutory customs/charges/incidental-service base, not only the foreign supplier's invoice. Check alternative valuation under s14A if the ordinary customs value cannot be determined or is not correct. Import CT is payable at import; the current Ministry page says before customs release, whether or not the importer is CT-registered.

Under s 15, an otherwise taxable foreign service not made in Tonga is treated as a supply by the Tonga taxable recipient to the extent used for exempt supplies, personal/domestic use or the specified entertainment. Apply the own-establishment deemed separate-person rule if relevant. This is a conditional reverse charge, not an automatic claim that every foreign B2B service has equal output/input CT. Establish any s 6(2A) registration branch first.

### Separate zero-rated and exempt supplies

The recovered Order's export-goods/services-for-use-outside-Tonga rules are not a blanket exemption for every foreign invoice. Exempt and zero-rated supplies have different credit consequences: eligible taxable/zero-rated business inputs can qualify, while exempt/private use cannot. The recovered Order also contains conditional international transport, going-concern transfer, domestic electricity/water and specified dated agricultural/charitable-import categories. They are not presented here as a complete current 2026 list. Obtain the actual current Order and every condition before applying a special category; unspecified “essential items” stay unconfirmed.

### Check input credits and documents before netting

Under s 16, start with output CT and subtract only credits allowed by ss 12,17,24 and the applicable transitional rule. Section 17 permits a taxable person's eligible input tax payable, but requires the proper CT invoice for a local supply or prescribed customs entry/document for an import in the claim period. A mere receipt from an unregistered supplier or a registration effective only after the supply does not create CT input tax. Pre-registration trading stock has a separate rule:held immediately before registration, acquired in a taxable supply/import no more than 4 months before registration, and satisfactory evidence of input tax paid.

Section 17 blocks passenger vehicles/spares/repair/maintenance unless in the vehicle-dealing/hiring business and acquired for that business; a passenger vehicle is designed/adapted for 9 or fewer seated passengers. Petroleum products require wholly business use. Entertainment is food, beverages, tobacco, accommodation, amusement, recreation or hospitality; credit requires the ordinary business of providing entertainment and excludes provision to an associate/employee. Exempt/private-use portions are denied. A logbook or business label does not override the statutory passenger-vehicle rule. Do not infer the old blanket credit for every registered business purchase.

Issue proper B2B original CT invoices at the time of supply under s 18, with CT wording, supplier/recipient names/addresses/TINs, serial/date, goods/services and supply date, and consideration/CT. The published amendment adds an original CT receipt for a paid supply to an unregistered customer; that amendment-dependent requirement is held pending commencement evidence. Do not treat an ordinary receipt as proof of a registered customer's input-credit entitlement. Keep credit/debit notes and import/export documents. For a post-sale change under ss 12,19, adjust the proper supplier/recipient period and issue the original note; a downward adjustment to an unregistered recipient requires repayment of excess CT before the supplier's credit. Preserve the original invoice linkage and proof of refund/credit.

### Complete and reconcile the actual return

Use the Ministry's current CT return for the actual calendar-month period or actual valid exceptional direction. Reconcile taxable/zero-rated/exempt sales, output tax, allowable input by source/period, credit/debit adjustments and brought-forward credits, then calculate net CT. Complete the actual current taxpayer/TIN, period, sales/output, input/adjustment and balance fields; exact live box mapping is not verified, so obtain the approved form/instructions before transmitting. File a nil return even when no tax/activity is reported. Keep submission acceptance and pay the actual balance through the authorized channel in TOP; retain the official receipt.

An excess input balance normally carries into the following period and then the next; refund applications require the applicable s 24 rules and current operative limitation. The published amendment's proposed 2-year limit after lodging the related CT return is held pending commencement evidence; no competing old limitation is assumed current. Regular-excess businesses have a specific application route; a carryforward is not an automatic cash refund. The Ministry describes application in the third period after 2 carryforward periods. Obtain the actual approved refund form and supporting evidence. Keep claimed, approved, credited and paid refunds distinct; no promise of immediate repayment is made.

## Boundary and exception table

| Situation | Treatment |
|---|---|
| Exactly TOP 100,000 relevant taxable supplies | Ordinary compulsory-registration boundary is met; test the actual historic/forecast period and associates. |
| Export, financial service, health, education, transport or essential-item claim | Verify the actual current category and conditions; no classification by label. |
| Passenger car, entertainment, mixed/private/exempt use or fuel | Apply the statutory credit restrictions before netting; no blanket input allowance. |
| Foreign service | Determine place, use, recipient status and conditional s 15 reverse charge; do not copy another country's digital VAT method. |
| Cancellation, return correction, refund or special supply scheme | Use the complete event-specific rules and actual forms; hold unsupported applications. |

## Worked cases

Hypothetical TOP inputs, ordinary confirmed 15% taxable supplies, no special exemption/transition and valid period-matched documentation. All outputs are derived from the sources above.

### CT-inclusive sales and a credit-eligibility decision

Registered trader sales are TOP 11,500 inclusive, so output CT is TOP 1,500. A proper ordinary wholly taxable-business purchase invoice separately shows TOP 500 of allowable input CT, leaving TOP 1,000. If that same purchase instead is a passenger car for the trader's own use, outside the dealer/hirer exception, the TOP 500 input is blocked and tax remains TOP 1,500. Documentation and classification determine the difference.

```oa-check
name: Inclusive-price extraction with eligible versus blocked passenger-vehicle input
inputs:
  inclusive_sales: 11500
  eligible_input_ct: 500
steps:
  output_ct: inclusive_sales * 15 / 115
  eligible_case_due: output_ct - eligible_input_ct
  blocked_vehicle_input: 0
  blocked_case_due: output_ct - blocked_vehicle_input
  difference: blocked_case_due - eligible_case_due
expected:
  output_ct: 1500
  eligible_case_due: 1000
  blocked_case_due: 1500
  difference: 500
```

### Import value includes the border charges

The Ministry's illustrative import facts are goods TOP 1,000, insurance/freight TOP 200, customs duty TOP 120 and quarantine charge TOP 50. These are example inputs, not a claim that every import has 10% duty or that charge. The CT base is TOP 1,370 and CT TOP 205.50. Using only the goods invoice would understate CT by TOP 55.50. Actual imports require their assessed customs/charge/incidental-service values and exemptions.

```oa-check
name: Full statutory import-value components rather than supplier invoice alone
inputs:
  goods: 1000
  insurance_freight: 200
  customs_duty: 120
  quarantine_charge: 50
steps:
  import_ct_base: goods + insurance_freight + customs_duty + quarantine_charge
  import_ct: import_ct_base * 0.15
  invoice_only_ct: goods * 0.15
  understatement: import_ct - invoice_only_ct
expected:
  import_ct_base: 1370
  import_ct: 205.50
  understatement: 55.50
```

## When to refuse or refer

Hold an unsupported exemption/zero-rating, input-credit, registration or refund claim. Refer unclear place of service, related-party value, reverse-charge use, special schemes or disputes. A secondary rate, unread Order or a receipt without statutory entitlement is not sufficient to finalize CT. Late-payment interest and possible penalties need current operative inputs/commencement; no blanket penalty bill is supplied.

## Filing and payment

Lodge and pay by the confirmed deadline for the actual period, including nil filings. Tax weekends/public holidays move to the next business day under RSAA Regulations reg 25. Retain accepted return, source reconciliation, proper invoices/notes, customs/export evidence, credit balances and payment receipt. An extension of filing does not itself extend payment under RSAA 2021 s 11. Confirm any actual electronic direction and account details through the authority.

## Completion checklist

Confirm registration/effective date, period, classification, source documents, time/place/value, all credit conditions and adjustments, net payable/carryforward, actual accepted return/payment and unresolved refund/special applications. No professional accountant approval is claimed.

## Sources

| Source and actual reading scope | Official URL | Read on |
|---|---|---|
| Consumption Tax Act, Cap.11.01, 2020 consolidation: Read for s 2 enterprise/taxable definitions, ss 3-24 with registration, timing, value, reverse-charge, credit/documentation and refund neighbors; amendment-dependent procedure changes not assumed operative | https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2003/2003-0029/ConsumptionTaxAct_3.pdf | 2026-11-15 |
| Consumption Tax (Amendment) Act 2020: Read for all published ss 1-12, including conditional commencement, receipts, certificate copies, procedure changes and proposed refund 2-year limit; affected applications held | https://ago.gov.to/cms/images/LEGISLATION/AMENDING/2021/2021-0037/ConsumptionTaxAmendmentAct2020.pdf | 2026-11-15 |
| MORC CT Regulations with appended Orders: Read for regs 9-12 and complete appended 2005,2009,2011 Orders/conditions, not assumed a complete 2026 exemption register | https://www.revenue.gov.to/sites/default/files/inline-files/ConsumptionTaxRegulations2005.pdf | 2026-11-15 |
| MORC Consumption Tax Overview: Read for complete tax scope, import-value example, credit explanation and restriction list compared with statute | https://www.revenue.gov.to/consumption-tax-overview | 2026-11-15 |
| MORC Consumption Tax Registration: Read for complete compulsory/voluntary conditions, Form 1/TIN/certificate/cancellation procedure; malformed threshold prose checked against Act | https://www.revenue.gov.to/consumption-tax-registration | 2026-11-15 |
| MORC Consumption Tax Returns: Read for complete filing, nil-return and refund guidance | https://www.revenue.gov.to/consumption-tax-returns | 2026-11-15 |
| MORC Consumption Tax Obligations: Read for complete records, invoice, credit/debit notes and calendar-month accounting-period instructions | https://www.revenue.gov.to/consumption-tax-obligations | 2026-11-15 |
| MORC Taxable Supplies: Read for complete place/time, exempt/zero-rated and inclusive-price guidance | https://www.revenue.gov.to/Taxable-Supplies | 2026-11-15 |
| Revenue Services Administration Act 2021: Read for ss 1,9-13,33,89-91; currentPart 14 commencement not independently established | https://www.revenue.gov.to/sites/default/files/inline-files/RevenueServicesAdministrationAct2021_1_4.pdf | 2026-11-15 |
| Revenue Services Administration Regulations 2021: Read for regs 14-18 and 24-26, currency/receipt/interest/weekend/procedure rules | https://www.revenue.gov.to/sites/default/files/inline-files/RevenueServicesAdministrationRegulations2021_FINAL_Eng_0.pdf | 2026-11-15 |

Not yet confirmed: The published Income Tax Amendment Act 2020 and Consumption Tax Amendment Act 2020 make commencement conditional on the Revenue Services Administration Act 2020, whereas the recovered administration Act is named 2021. No official provision resolving that identity/commencement condition has been recovered; do not infer it from an index or passage history. Amendment-dependent original-main-certificate/official-copy requirements, original receipts for unregistered customers, the proposed 2-year refund application limit and procedural repeals are held. Do not activate either a new or superseded default while that condition is unresolved; obtain the governing instrument and actual authority direction before those applications. The complete current set of exemption/zero-rating Orders, particularly later 2013 and special-sector/event measures, has not been recovered; do not infer a blanket essential-item exemption or classify a disputed financial/medical/education/transport supply from its name. The appended 2005/2009/2011 Orders are dated texts; ordinary export/financial-service treatment is also corroborated by current Ministry guidance, but a comprehensive 2026 list is not claimed. Exact live eTax/current return box mapping and assigned exceptional periods require actual Ministry documents; the current authority describes calendar-month periods, not an assumed two-month category. Numeric administrative penalties and an interest bill require current RSAA Part 14 commencement and the actual quarter-linked lending rate. Special used-goods/voucher/lay-by/periodic-supply implementations and bespoke refund/export evidence require the applicable full rules before use. The old threshold “exceeding TOP 100,000” is corrected to TOP 100,000 or more; the old unqualified input-credit/import-value defaults are not retained as usable shortcuts.
