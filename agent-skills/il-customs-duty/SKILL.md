---
name: il-customs-duty
description: "Use this skill when calculating Israeli customs duty, VAT, and purchase tax on imports, or advising on free trade agreement preferences. Trigger on phrases like \"import tax Israel\", \"customs duty Israel\", \"מכס\", \"mas kniya\", \"מס קנייה\", \"personal import Israel\", \"Amazon import Israel\", \"AliExpress import Israel\", \"Shaar Olami\", \"שער עולמי\", \"HS code Israel\", \"EUR.1 Israel\", \"FTA Israel\", \"landed cost Israel\", or any Israeli customs and import duty query. ALWAYS read this skill before advising on Israeli import duties."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/il-customs-duty"
  jurisdiction: "IL"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Israel: import classification, tax base and landed cost

> **Based on work by [Skills IL](https://github.com/skills-il/tax-and-finance)**, licensed under MIT. Adapted for the OpenAccountants format.

## Scope

Prepare a 2026 import working paper for review by an Israeli customs professional/CPA. Separate personal-import eligibility, import legality, classification, customs valuation, origin preference, purchase tax, import VAT and carrier fees. This is not a tariff ruling. Tax amounts are usable only once the actual product, entry date, accepted valuation and applicable tariff/exemption have been established.

| Quick reference | Rate or threshold and conditions | Official source |
|---|---|---|
| Standard VAT | 18% from 1 January 2025; determine exemption/zero-rating and the import tax point separately | ITA Interpretation01/2025, https://www.gov.il/BlobFolder/policy/vat_11/he/vat_represent-info-051224-2.pdf |
| Ordinary goods import VAT base | Customs value under Customs Ordinance ss.129-134A plus customs duty and other applicable import taxes/levies; s.11(b)/(c) special cases separate | VAT Law s.11, https://www.btl.gov.il/Laws1/00_0022_000000.pdf |
| Classification information service | Free; service describes a 10-digit customs item and applicant/identical-goods/legal-change limitations; not proof of a universal 8-digit rule | ITA classification service, https://www.gov.il/he/service/classification-of-goods-in-imports |
| US origin document | Signed US Origin Invoice Declaration replaces the old hard-copy Green Form/Form A from 10 January 2018, subject to origin eligibility | US International Trade Administration, https://www.trade.gov/us-israel-free-trade-agreement |

## Ask the client first

Obtain importer identity/status and intended personal/family/business use; product material/function/composition, packaging, quantity, brand/model/catalogue; seller and actual origin/manufacturing evidence; invoice, payment and freight/insurance breakdown; Incoterms, currency and entry date; related-party/royalty/assists or valuation adjustments; classification/ruling and live tariff; licences/standards/health/agriculture approvals; carrier/broker charges; origin proof and exporter status; customs assessment and import declaration; VAT registration/taxable use; gifts, immigrant or temporary-import eligibility and prior linked shipments. Unknown facts remain open items.

## The method, step by step

### Determine the import category before a tax threshold

The Personal Import Order s.3 requires import other than through a dealer, not for supply/production/services, in reasonable quantity and for the individual's personal/family use. Its quantity tests, exclusions and authority discretion must be checked for the actual goods; food and regulated products have separate conditions. The order combines consignments sent by the same supplier to the same importer within **72 hours** for its shipment test. A licensing/quantity rule is not a tax exemption, and splitting a purchase does not establish separate tax eligibility ([Personal Import Order ss.2-4](https://apps.economy.gov.il/Apps/PersonalImport/Home/Digital_Order/)).

Treat ordinary commercial stock imports, personal high-value parcels, gifts and new-immigrant belongings as separate screens. A commercial dealer's import VAT is not automatically recoverable: it requires a qualifying document and taxable business use under ss.38/41, as explained in [israel-vat](israel-vat.md). A gift or an immigrant certificate does not establish an unlimited import exemption. Refer immigrant baggage/household relief to the actual customs schedule and [il-new-immigrant](il-new-immigrant.md).

The personal-parcel guidance and official calculator could not be reopened. The old USD 75/USD 500 bands and USD 150 reversal history remain excluded below. Do not quote a tax-free ceiling from a search snippet or the unrelated Personal Import Order's licensing provisions. A higher shipment value does not by itself mean every kind of duty/purchase tax is charged or that all personal-import conditions disappear.

### Resolve the current Israeli classification

Describe the goods precisely, then use the official tariff classification and its legal notes for the entry date. Do not transplant the last digits of a US HTS or EU CN code, or turn an illustrative chapter into a final rate. The old chapter 85 electronics and chapter 61 apparel cues are only starting points requiring the actual product. Request classification information through the official service when uncertain; the service says it is free, describes a **10-digit** item, valid for **1 year** subject to legal change, for the applicant and identical described goods only. It does not protect a different importer or product, and does not itself settle valuation, origin or every tax ([classification service](https://www.gov.il/he/service/classification-of-goods-in-imports)).

The older separate commercial pre-ruling page's 8-digit wording could not be reopened. Do not assert that “6 international digits plus 2 Israeli digits” is the complete current declaration format. Retain the actual ruling, product catalogue and all information supplied; obtain a customs professional's confirmation of its scope before relying on it.

### Establish valuation, duty and purchase tax separately

Use the accepted customs value and legally applicable customs exchange rate, supported by invoice, freight, insurance and required adjustments. The old simple CIF illustration (goods plus freight plus insurance converted to NIS) is arithmetic, not a complete valuation rule or evidence that the Bank of Israel daily clearance-date rate always governs. Separate the product-value threshold test, if applicable, from the import tax base.

Apply the actual tariff duty, purchase-tax method/rate and other levies to their own statutory bases. Do not invent a typical 0%-12% customs range or treat a camera, bag, perfume, electronic item, alcohol, tobacco or passenger car as having a universal rate. Purchase tax can materially affect both cost and VAT base; product-specific rates, exemptions and any statutory valuation uplift must be established. The old formula “purchase tax = value after duty x rate” is not adopted for every item.

For ordinary goods covered by s.11(a), VAT base = accepted customs value + actual customs duty + other applicable import taxes/levies. Section 11(b) has a separate s.26(b) goods rule, and s.11(c) concerns goods exported for repair/renewal/improvement and reimported; those require separate computation. Landed cost then adds the actual broker/carrier/handling charges, distinguishing any VAT on those fees ([VAT Law s.11](https://www.btl.gov.il/Laws1/00_0022_000000.pdf)). Postal/courier clearance routes may use different agents and fees; DHL, FedEx, UPS and Israel Post names do not establish a tax rate or a fixed fee range.

### Origin preference: agreement, product and proof

Origin means the applicable agreement's origin rules, not simply the shipping country or invoice seller. Check the actual tariff preference, product rules, production, direct-shipment/non-alteration and documentation conditions before claiming it. A preference claim does not automatically remove purchase tax, VAT or other levies; compute those independently. Missing origin evidence is a reason to withhold the preference claim pending review, not proof of a particular MFN rate.

The US official page confirms the FTA entered into force on 1 September 1985 and the US-Israel FTA document route: from 10 January 2018, the exporter/producer completes and signs the US Origin Invoice Declaration instead of the hard-copy Green Form/Form A. This does not waive the agreement's substantive origin conditions ([US official FTA page](https://www.trade.gov/us-israel-free-trade-agreement)). The European Commission confirms the EU-Israel Association Agreement framework and separate agricultural provisions; it does not establish every product's preference or the old bag example's tariff ([EU official overview](https://policy.trade.ec.europa.eu/eu-trade-relationships-country-and-region/countries-and-regions/israel_en)).

Do not retain the old universal “Israel never accepts electronic EUR.1; wet ink always required” as an instruction. The Commission's official electronic-certificates annex lists Israel's **Global Gate from 1 April 2024** and an authenticity-check link. This confirms an electronic origin-certificate system, not that any PDF from any partner is acceptable for every import. Verify the agreement, direction, issuing system, authenticity and current receiving-authority conditions. The old EUR 6,000 invoice declaration/approved-exporter and courier-original requirements remain unresolved for the actual transaction ([Commission notice, Annex I](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ%3AC_202506212)).

## Worked cases

### Camera: conditional accepted value, no assumed tariff exemption

Retain the Amazon US camera, USD 200 goods plus USD 20 shipping, no insurance. **Assume** customs accepts this USD 220 value, the applicable customs conversion rate is NIS 3.65/USD, the actual duty and purchase tax are zero, and ordinary 18% import VAT applies. Accepted NIS value is NIS 803; VAT NIS 144.54; subtotal NIS 947.54. If the independently quoted all-in clearance fee is NIS 100 or NIS 400, total cash is NIS 1,047.54 or NIS 1,347.54. These fees/rates are assumed scenario inputs, not verified typical fees, camera tariff or personal-import exemption. VAT recovery is a separate test.

```oa-check
name: Conditional camera valuation and fee sensitivity
inputs:
  goods_usd: 200
  freight_usd: 20
  confirmed_fx: 3.65
  actual_duty: 0
  actual_purchase_tax: 0
steps:
  - customs_value: (goods_usd+freight_usd)*confirmed_fx
  - vat_base: customs_value+actual_duty+actual_purchase_tax
  - import_vat: vat_base*0.18
  - subtotal: vat_base+import_vat
  - total_low_fee: subtotal+100
  - total_high_fee: subtotal+400
expected:
  customs_value: 803
  import_vat: 144.54
  subtotal: 947.54
  total_low_fee: 1047.54
  total_high_fee: 1347.54
```

### Italian bags: duty preference versus import VAT cash

Retain 50 Italian leather bags and the old illustrative HS 4202.21.xx, value EUR 12,000. That incomplete code is **not a classification**. For comparison only, assume an accepted converted customs value of NIS 48,000 (assumed NIS 4/EUR), ordinary 18% VAT, no purchase tax/other levy, and a verified non-preferential duty of 6% versus a separately valid zero-duty preference. Duty is NIS 2,880 versus zero; VAT NIS 9,158.40 versus NIS 8,640; import-tax cash difference NIS 3,398.40. Of this, duty difference is NIS 2,880 and VAT cash difference NIS 518.40. A fully eligible dealer's later VAT recovery can change economic cost, not the customs cash payment.

The old EUR illustration at assumed 6%-12% duty gave EUR 720-1,440 duty, VAT EUR 2,289.60-2,419.20 versus EUR 2,160 at zero duty; these remain arithmetic equivalents, not verified leather-bag tariffs or permission to pay Israeli taxes in EUR. The EUR 6,000 document assertion is not used to approve the preference.

```oa-check
name: Conditional preference changes duty and VAT cash
inputs:
  eur_value: 12000
  confirmed_fx: 4
  assumed_duty_rate: 0.06
steps:
  - customs_value: eur_value*confirmed_fx
  - ordinary_duty: customs_value*assumed_duty_rate
  - ordinary_vat: (customs_value+ordinary_duty)*0.18
  - preferred_duty: 0
  - preferred_vat: customs_value*0.18
  - cash_difference: ordinary_duty+ordinary_vat-preferred_duty-preferred_vat
  - vat_difference: ordinary_vat-preferred_vat
expected:
  customs_value: 48000
  ordinary_duty: 2880
  ordinary_vat: 9158.40
  preferred_vat: 8640
  cash_difference: 3398.40
  vat_difference: 518.40
```

## When to refuse or refer

Refer uncertain product classification/ruling, personal-use quantities, origin proof/preferences, related-party or complex customs valuation, purchase-tax uplifts, alcohol/tobacco/cars, ATA Carnet/temporary imports, Eilat, immigrant belongings, anti-dumping duties and agricultural quotas/seasonal levies. Do not guess a final code, currency rate or threshold to produce a landed-cost number. A customs assessment and input-VAT eligibility are separate reviews.

## Filing and payment

Prepare the applicable import declaration and supporting invoice, transport, origin, licence and valuation records through the authorized customs/broker channel; reconcile assessed duty, purchase tax, import VAT and fees to payments. Retain the accepted declaration/release and any classification/origin decision. For a dealer's VAT input claim, retain the qualifying document in its name and taxable-use evidence for the VAT return. Actual courier/postal processes, calculator results, objection/refund dates and declarations require the live service for that shipment; this skill authorizes no customs submission or payment.

## Completion checklist

Confirm import category and legality, product/ruling scope, current tariff and valuation/currency basis; verify all preference conditions and proof; calculate each tax on its correct base; separate fees and VAT recovery; reconcile declaration/payment/release; obtain professional review and preserve unresolved items.

## Sources

| Source | URL | Read on |
|---|---|---|
| Consolidated VAT Law; Read for s.11 ordinary customs-value/duty/other-tax base and special s.11(b)/(c) cases; ss.38/41 import input conditions | https://www.btl.gov.il/Laws1/00_0022_000000.pdf | 2026-11-14 |
| ITA Interpretation01/2025; Read for introduction giving standard18% on Israeli transactions and goods imports with tax point from1January2025 under the2024 amending order | https://www.gov.il/BlobFolder/policy/vat_11/he/vat_represent-info-051224-2.pdf | 2026-11-14 |
| ITA 2025 rights guide, 2025-2026 filing cycle; Read for VAT annex input documentation, not product-specific tariff exemptions | https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf | 2026-11-14 |
| Personal Import Order digital text; Read for ss.2-4 personal/family/nonbusiness/quantity and regulatory boundaries, 72-hour shipment combination; not a tax-exemption schedule | https://apps.economy.gov.il/Apps/PersonalImport/Home/Digital_Order/ | 2026-11-14 |
| ITA classification information service; Read for free service,10-digit item,1-year/legal-change/applicant/identical-goods limits | https://www.gov.il/he/service/classification-of-goods-in-imports | 2026-11-14 |
| US International Trade Administration FTA page; Read for signed Origin Invoice Declaration replacing hardcopy Green Form/FormA from10January2018, subject to origin rules | https://www.trade.gov/us-israel-free-trade-agreement | 2026-11-14 |
| European Commission Israel trade overview; Read for Association Agreement framework and separate agricultural provisions, not a product tariff ruling | https://policy.trade.ec.europa.eu/eu-trade-relationships-country-and-region/countries-and-regions/israel_en | 2026-11-14 |
| Final Official Journal notice C/2025/6212 of13November2025, AnnexI; Read for electronic-certificates notification, Israel GlobalGate1April2024 and authenticity-check link; not universal inbound acceptance | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ%3AC_202506212 | 2026-11-14 |

Not yet confirmed: personal tax-free USD75 ceiling, USD75-500 customs-only band, shipping/insurance exclusion from threshold but inclusion in tax base, and exact higher-value treatment. The old history attributed the USD150 increase to a Smotrich decree in November2025 and reversal to24February2026; no operative decree/revocation was opened, so neither is a usable current threshold. Official parcel guide/calculator returned403 and ordinary direct recovery also403. Current commodity duty/purchase-tax rates including old0%-12%range, camera0%, bags6%-12%, purchase-tax categories/ranges, customs FX rule and complete valuation adjustments remain unconfirmed. The old universal8-digit structure/6+2claim and separate commercial pre-ruling8-digit page are not current-format instructions. UK-Israel2019/EUR.1, Canada modernizedCIFTASeptember2019/FormB239, EFTA(CH,NO,IS,LI)/EUR.1, Mercosur(BR,AR,UY,PY)June2010/certificate, and EU/UK EUR6000/approved-exporter/wet-ink rules require their actual current agreement/direction/product conditions. None of these legacy rows establishes a current preferential rate. Temporary/Eilat/immigrant/anti-dumping/agricultural relief and courier/postalfees/timelines need case-specific sources.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `il-customs-duty` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/il-customs-duty. If neither is available, confirm every figure against the official source pages cited above before relying on it.
