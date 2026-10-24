---
name: sm-vat-gst
description: >
  Prepare selected 2026 San Marino monofase import-tax workpapers by actual goods, connected services, origin, importer, transaction date, taxable base and established tariff classification. This is not a generic VAT credit/return model. Distinguishes ordinary 17% import tax, conditional capital-goods relief, export-refund evidence, Italy VAT exchange procedures and the 2026-2028 domestic-invoice transition. Includes three arithmetic controls with explicit eligibility assumptions. Full tariff amendments, complementary/excise duties, exemptions, refund amounts/time limits and current operational import/payment instructions remain partial. Named San Marino accountant review remains open.
jurisdiction: SM
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.2
sources:
  - url: "https://www.consigliograndeegenerale.sm/contents/instance18/files/document/19029leggi_2560.pdf"
    title: "Law 40/1972; import tax original framework"
    as_of: "2026-10-24"
  - url: "https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17021434.html"
    title: "Decree 50/1993; selected base and documentary rules"
    as_of: "2026-10-24"
  - url: "https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17022004.html"
    title: "Decree 108/1997; original tariff-table framework"
    as_of: "2026-10-24"
  - url: "https://www.consigliograndeegenerale.sm/on-line/home/documento17046854.html"
    title: "DD 183/2011; ordinary 17 percent rate and commencement"
    as_of: "2026-10-24"
  - url: "https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17022916.html"
    title: "Decree 135/2003; capital-goods framework requiring amendment checks"
    as_of: "2026-10-24"
  - url: "https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=e54431a0e32f941616323ba3300c13a32828e853"
    title: "Authentic DD 98/2026; selected tariff change from August"
    as_of: "2026-10-24"
  - url: "https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=4d7f1ffcf645b166ffc567d328d888e43fcdd538"
    title: "Authentic DD 133/2026; domestic invoice transition"
    as_of: "2026-10-24"
  - url: "https://www.gazzettaufficiale.it/eli/id/2021/07/15/21A04244/SG"
    title: "Italy DM 21 June 2021; VAT exchange framework"
    as_of: "2026-10-24"
  - url: "https://www.finanze.sm/pub2/FinanzeSM/FISCALITA-NAZIONALE.html"
    title: "San Marino Finance; current indirect-tax source map"
    as_of: "2026-10-24"
---

# San Marino monofase and VAT interface v0.2

## Scope and transaction questions

San Marino's Finance ministry identifies **monofase import tax**, complementary tax and related procedures as the domestic indirect-tax system. For this 2026 preparation, start with actual imports of goods and connected services under Law 40/1972, not a generic domestic output-VAT less input-VAT return. Establish the importer, parties and IDs, goods description and intended use, origin/destination, transport and delivery dates, invoice, consideration, duties and supporting customs documents. A service classification or Italian VAT consequence requires its own rule; not every standalone service is an import-taxable good or automatically tax free. [Finance ministry][finance]; [Law 40/1972, articles 1–5][monolaw]

The Guide's inherited `vat-gst` filename is retained for compatibility. Its subject is monofase and the VAT interface with Italy. It does not establish that a future proposed domestic VAT reform has been enacted or supplies a future VAT start date.

## Base and rate preparation

Law 40/1972 article 3 starts with the total consideration due to the supplier. Decree 50/1993 article 3 adds exigible excise, levies, duties and equivalent charges and has distinct exchange/customs-value rules for extra-community imports and purchases from the Community customs territory. Where price is missing or not the sole consideration, use its normal-value rule. Obtain the applicable current official conversion and customs valuation rather than copying the 1972 payment-day exchange wording alone. [Law 40/1972, article 3][monolaw]; [Decree 50/1993, article 3][base]

The ordinary import-tax rate is **17%** under DD 183/2011 article 1, effective for operations from 1 January 2012. That decree also increases the specified Table C 20% rate to 21%. Decree 108/1997 supplies the table framework but its original ordinary 16% is superseded, and Law 40's original 7% is not the current ordinary rate. Classification and later amendments govern exceptions; 17% is not a universal rate for every import. [DD 183/2011, articles 1–2][ordinary]; [Decree 108/1997, article 1 and tables][rates]

For the full table, obtain the actual current goods description/code and every relevant amendment before selecting a reduced, increased, fixed or exempt treatment. DD 98/2026 adds feminine-hygiene absorbent products, tampons or cups to **Table A number 23-ter** and repeals Table B 95-bis, for imports **from 1 August 2026**. Table A in the retrieved framework is the 2% table. This selected amendment does not verify all table entries or all 2026 classifications. The old broad list of reduced rates without exact primary classification is replaced. [Decree 108/1997, Table A][rates]; [DD 98/2026, articles 1–2][july]

## Liability, relief and export evidence

Law 40/1972 article 5 puts tax on the importer and makes the persons on whose behalf importation occurs and those materially introducing the goods jointly liable. Identify the actual parties and retain the transport/customs evidence. An invoice addressed to someone else does not alone settle the importer's liability. [Law 40/1972, article 5][monolaw]

Decree 135/2003 articles 1–3 provide a **conditional 1%** capital-goods route for directly instrumental material/intangible assets and eligible operators. The retrieved text requires unit value over 250 or, for lower unit values, homogeneous purchases with a base over 500, and has separate vehicle/rental/property rules and retention/early-disposal consequences. Business ownership alone does not prove the 1% route. Later amendments, current authorisation, asset use and disposal history must be reconciled before applying it. The old blanket new/used car percentages are not treated as a complete current vehicle method. [Decree 135/2003, articles 1–8][capital]

Law 40/1972 articles 1,9 and 14 establish the export-refund route for relevant previously imported goods, including the stated transformation case. It is **not an automatic input-VAT credit** against domestic sales. Retain import tax paid, traceability from imported goods/material to exported goods, transformation/stock records, export invoices and actual customs/validation evidence. Articles 9/17 and later implementing rules govern the claim; eligibility does not establish a 100% refund of every cost, current filing form or payment date. Current refund rates, time limits, adjustments and execution remain open. [Law 40/1972, articles 1,9,14–17][monolaw]

## Italy trade: use the current exchange framework

Italy's DM 21 June 2021 replaced its 24 December 1993 decree from **1 October 2021**. For covered goods trade, electronic invoices through SDI became the general route **1 July 2022**, with the statutory exclusions preserved. Do not reproduce the 1972 paper-copy workflow as the normal current electronic process. Match the actual counterparty ID, movement, invoice and validation result. [Italian DM, articles 1–2 and 22][italy]

For Italy-to-San Marino covered business goods, article 3 transmits the invoice with the San Marino recipient ID through SDI to the Tax Office. The Office checks import tax and communicates validation. If the invoice has not been validated within four months of issue, the Italian supplier issues the specified variation within the following thirty days. Paper-exempt cases have their distinct article 4 communication route. Do not assume an Italian supplier's invoice alone proves completed San Marino import-tax compliance. [Italian DM, articles 3–5][italy]

For covered San Marino-to-Italy business goods, article 6 sends the electronic invoice through the Tax Office to SDI. Articles 7–8 distinguish an invoice with Italian VAT, with the specific payment/control route, from an invoice without VAT, for which the Italian recipient accounts under the referenced reverse-charge/integration rules. A domestic monofase rate does not determine the Italian VAT rate or deductibility. Confirm actual validation/payment before treating Italian input VAT as deductible. [Italian DM, articles 6–8][italy]

Private buyers, new transport, distance sales, noncommercial bodies and services have separate articles 13–16 and 20. Do not extend the business-goods non-taxable or reverse-charge result to every consumer or service transaction. Current Italian implementation, exceptions, territoriality, distance-sale threshold/application and every later amendment are outside this completed method. The decree was read as the primary framework; no SDI transmission or foreign VAT return was performed. [Italian DM, articles 13–16,20–22][italy]

## Domestic invoices: dated transition

DD 133/2026 is separate from Italy trade. Article 11 makes the following distinctions:

| Period/route | Enacted transition |
|---|---|
| 1 October–31 December 2026 | Covered operators/delegates can opt to transmit domestic business invoices/variation notes electronically instead of paper |
| From 1 January 2027 | Electronic issue for the covered domestic COE-to-COE route, subject to the article 2 exclusion; the decree's paper-invoice provisions also begin |
| From 1 January 2028 | The decree's administrative penalties in articles 6–7 apply |
| State, public administration and public entities | Application depends on the specified implementing regulation coming into force |

[DD 133/2026, article 11][invoice]

Article 2(2) excludes operators with previous-calendar-year declared revenues **below 100,000**, while permitting an option. Exactly 100,000 is outside that exclusion and therefore brings the covered obligation for that year. Article 2(3) separately requires continuing electronic use in later years where operators have **exceeded** the amount or exercised the option. The text does not establish the same continuing-use result for exact equality alone; obtain official interpretation before treating a year at exactly 100,000 as permanent entry. This is an invoice-format rule, **not a VAT-registration or import-tax exemption threshold**. The general article 3 timing is by the second month following delivery/shipment for goods, completion for services or payment for advances, with special delayed/continuous-supply rules. An HUB SM rejection means the electronic invoice is not issued under 4(3). The actual 2026 option, technical Regulation 28/2026, certificate, corrections, retention and live workflow still need validation; these statements do not claim a successful filing. [DD 133/2026, articles 2–5 and 8–11][invoice]

## Documentation, calendar and sanctions gaps

Decree 50/1993 articles 4–5 specifies import-document/control routes for extra-community and other Community purchases, but those older texts must be reconciled with current electronic, customs and delegated instructions before execution. This Guide has not completed every import registration, declaration/payment due date, exemption certificate, customs procedure or sanction. Obtain the current Tax Office/Customs instructions and actual portal route before filing or payment. Do not transplant an income-tax deadline or describe monofase as a periodic VAT return. [Decree 50/1993, articles 4–5][base]; [Italian DM, articles 2–5 and 22][italy]

DD 133's 100 administrative charge under article 6 and recipient self-documentation under 7 have their **2028 sanction commencement**, not an immediate October 2026 penalty. Other current import-tax/IGR invoice sanctions are distinct and remain to be reconciled. [DD 133/2026, articles 6–7 and 11(4)][invoice]

## Worked controls

### Ordinary established import base

Assume final ordinary taxable base 12,000 after all consideration, connected costs, exigible duties and valuation adjustments have been independently established, with no reduced/exempt/special classification. Monofase is 2,040. No domestic VAT output/input offset is inferred.

```oa-check
name: San Marino ordinary monofase on established import base
inputs:
  established_import_base: 12000
  ordinary_monofase_rate: 0.17
steps:
  import_tax: established_import_base * ordinary_monofase_rate
  base_plus_import_tax: established_import_base + import_tax
expected:
  import_tax: 2040
  base_plus_import_tax: 14040
```

### Separately established classifications

Assume two separately classified imports: ordinary base 10,000 at 17% and a confirmed current Table A eligible base 2,000 at 2%, with all date/category conditions independently established. Total tax 1,740. This tests the arithmetic, not entitlement to the Table A classification.

```oa-check
name: San Marino assumed ordinary and Table A import classifications
inputs:
  ordinary_base: 10000
  confirmed_table_a_base: 2000
  ordinary_rate: 0.17
  confirmed_table_a_rate: 0.02
steps:
  ordinary_tax: ordinary_base * ordinary_rate
  table_a_tax: confirmed_table_a_base * confirmed_table_a_rate
  total_import_tax: ordinary_tax + table_a_tax
expected:
  ordinary_tax: 1700
  table_a_tax: 40
  total_import_tax: 1740
```

### Already established capital-goods relief

Assume a 50,000 base asset independently confirmed eligible for the current 1% capital-goods route, with operator, use, value and retention conditions established and no special exception. The isolated import tax is 500. There is no automatic early-sale recapture/refund conclusion.

```oa-check
name: San Marino assumed eligible capital-goods import tax
inputs:
  established_eligible_asset_base: 50000
  confirmed_capital_goods_rate: 0.01
steps:
  conditional_import_tax: established_eligible_asset_base * confirmed_capital_goods_rate
expected:
  conditional_import_tax: 500
```

## Limits and referral

VAT/indirect tax remains partial. Complete tariff chains, current exemptions/fixed amounts, capital-goods/vehicle amendments, complementary taxes and excise, customs valuation/clearance, current import calendar, export-refund computation/forms/time limits, Italian special cases and technical/live invoice execution remain open. Resolve the actual transaction-specific gap before execution. No accountant verification or country completeness is claimed. Named San Marino accountant review remains open.

## Sources

Read 24 October 2026: Law 40/1972 selected scope/base/liability/export provisions; Decree 50/1993 selected base/document provisions; Decree 108/1997 articles 1–4 and selected table framework; all two articles of DD 183/2011; capital-goods Decree 135/2003 articles 1–11, with later-amendment limits retained; full authentic DD 98/2026 and DD 133/2026 including commencement. Italy's DM 21 June 2021 was read in the official Gazette, with detailed checks on the cited ordinary business-goods and commencement provisions. Retrieval is not a complete later-amendment audit or live filing. Earlier secondary wording remains in Git history.

[law]: https://www.consigliograndeegenerale.sm/on-line/documento17086436.html
[reform]: https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17155359.html
[october]: https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=9c3a0dfeb72a7aeab52d1c5c0440879b4cf2ad33
[iss]: https://www.iss.sm/on-line/home/menudestra/area-modulistica/modulistica-ufficio-contributi/documento49158490.html
[calculator]: https://www.pa.sm/portalepa/servlet/portalepa.hic.servizi.HGCalcoloIGRLegge141_2025?MPasso=1&MTipo=G&profondita=1

## Source-review status

See the [independent source-review record](../../../docs/research/2026-10-24-san-marino-pack-review.md) for its exact revision, scope and findings. Named San Marino accountant review remains open. This record is separate from comprehensive coverage, named professional approval and live filing.

<!-- openaccountants-cta-block -->

---

## Talk to an accountant

Find the current Guide and professional-review status at [OpenAccountants](https://www.openaccountants.com).

[monolaw]: https://www.consigliograndeegenerale.sm/contents/instance18/files/document/19029leggi_2560.pdf
[base]: https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17021434.html
[rates]: https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17022004.html
[ordinary]: https://www.consigliograndeegenerale.sm/on-line/home/documento17046854.html
[capital]: https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17022916.html
[july]: https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=e54431a0e32f941616323ba3300c13a32828e853
[invoice]: https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=4d7f1ffcf645b166ffc567d328d888e43fcdd538
[italy]: https://www.gazzettaufficiale.it/eli/id/2021/07/15/21A04244/SG
[finance]: https://www.finanze.sm/pub2/FinanzeSM/FISCALITA-NAZIONALE.html
