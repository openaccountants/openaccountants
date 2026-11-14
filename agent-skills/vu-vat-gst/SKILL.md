---
name: vu-vat-gst
description: "Vanuatu VAT, tax year 2026: 15% standard rate and 0% Schedule 3 supplies, exempt supplies, the VT 4 million registration test and 21-day application, monthly and quarterly periods, returns by the 27th (5 January for November), accounting basis, import VAT base, from the VAT Act [Cap 247] and DCIR."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/vu-vat-gst"
  jurisdiction: "VU"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Vanuatu VAT / GST

> **General reference only.** Source-cited draft, not reviewed by an accountant. Do not use it to file or take a position without professional review.

## Who this applies to

Anyone carrying on a taxable activity in Vanuatu and every importer. VAT is administered by the Department of Customs and Inland Revenue (DCIR) under the Value Added Tax Act [Cap 247] (2020 consolidation) and the Tax Administration Act No. 37 of 2018. DCIR's guide notes that activities carried on by international companies, employment and exempt-supply activities are not taxable activities.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Standard rate | 15% (s 11(1)) | 2026 | https://vanuatucustoms.gov.vu/images/Laws_Regulations/VAT/247_Value_Added_Tax_Consolidated_2020.pdf |
| Zero rate | 0% on Schedule 3 supplies made in Vanuatu by a registered person (s 11(2)) | 2026 | https://vanuatucustoms.gov.vu/images/Laws_Regulations/VAT/247_Value_Added_Tax_Consolidated_2020.pdf |
| Compulsory registration | Taxable supplies in any 12-month period exceed, or are expected to exceed, VT4 million | 2026 | https://vanuatucustoms.gov.vu/taxes-and-licensing/taxes/value-added-tax-vat/introduction.html |
| Quarterly (Category B) periods, on written application | Taxable supplies less than VT8 million a year | 2026 | https://vanuatucustoms.gov.vu/taxes-and-licensing/taxes/value-added-tax-vat/introduction.html |
| Application to register once liable | Within 21 days (s 12(3)) | 2026 | https://vanuatucustoms.gov.vu/images/Laws_Regulations/VAT/247_Value_Added_Tax_Consolidated_2020.pdf |
| Interest the Director pays on a late refund | 15% per annum after 15 working days (s 42) | 2026 | https://vanuatucustoms.gov.vu/images/Laws_Regulations/VAT/247_Value_Added_Tax_Consolidated_2020.pdf |

The Act tests registration at the end of each month over the past twelve months and at the start of each month over the coming twelve (s 12(1)), disregarding exempt supplies and supplies caused only by winding down or replacing capital assets (s 12(2)). For Category B the Act's words are "has not ... exceeded eight million vatu", so exactly VT 8 million still qualifies (s 15(3)); the Minister may change the limit by order.

## The base

- **Domestic supplies.** VAT on the value of the supply (s 10, s 11(1)(a)).
- **Imports.** VAT on the customs value, plus customs duty, plus excise, plus the cost of transport to Vanuatu and insurance for it (s 11(1)(b)). DCIR's no-excise clearance calculation takes the cost, insurance and freight value once and adds duty before applying 15%.
- **Zero-rated (Sch 3).** Exports meeting the conditions, goods outside Vanuatu at supply, international transport, services physically performed outside Vanuatu, services to a non-resident outside Vanuatu (para 5: not services directly connected with Vanuatu land or goods, and not services received in Vanuatu by an unregistered person), supplies to approved educational institutions and aid projects, and a going concern sold to a registered person where both agree in writing (para 9). From 22 July 2021 the Tax Administration Act definitions apply to Schedule 3 (VAT Amendment Act No. 13 of 2021).
- **Exempt (Sch 1).** Financial services, hire of accommodation in a residential dwelling, qualifying leasehold rent, education by an approved institution, donated goods and services sold by a non-profit body, and the sale of a property used for exempt residential rental for at least 5 years. No input credit on exempt supplies.
- **Input credit.** Only against a valid tax invoice; a registered supplier must issue one within 28 days of a registered customer's request (DCIR guide).

## Deadlines and filing

- **Periods.** Category A is monthly; Category B is three-monthly on written application (s 15).
- **Returns and payment.** For a period ending 30 November, by 5 January; for any other period, by the 27th of the following month; a non-working day moves the date to the next working day (ss 16 and 20). A creditor selling a registered debtor's goods files a special return by the 27th (s 16(2)).
- **Extensions.** An individual filing extension under Tax Administration Act s 11 leaves the payment date unchanged; a general extension the Director grants to all taxpayers or a class under s 11(7) also extends payment.
- **Accounting basis.** Invoice or payments basis, elected in the approved form; with no election, the payments basis applies (s 17).

## Penalties and interest

DCIR's guide says late payment penalties are assessed; the amounts sit in the Tax Administration Act No. 37 of 2018 and were not read for this guide. The Director pays interest at 15% a year on a refund not made within 15 working days (s 42).

## Cross-border points

Imports bear VAT at the border on the duty-inclusive base above. Act No. 24 of 2023 repealed, from 29 December 2023, the parts of the import duty tariff that VAT Schedule 2 refers to, and added a new tariff schedule with separate duty, excise and VAT columns; check the concession and its VAT treatment for the entry date. Services to non-residents are zero-rated only within Schedule 3 para 5.

## Two worked examples that recompute

**1. Monthly return.** Standard-rated sales VT 1,000,000 (VAT exclusive); input VAT on valid tax invoices VT 60,000. Output VAT 150,000; payable VT 90,000 by the 27th of the next month (derived).

```oa-check
name: Vanuatu monthly VAT
inputs:
  sales: 1000000
  input_vat: 60000
steps:
  - output_vat: sales * 0.15
  - payable: output_vat - input_vat
expected:
  output_vat: 150000
  payable: 90000
```

**2. Import, no excise.** Customs value including freight and insurance VT 2,000,000; customs duty VT 200,000. Import VAT is 15% of 2,200,000 = VT 330,000 (derived).

```oa-check
name: Vanuatu import VAT no excise
inputs:
  cif: 2000000
  duty: 200000
steps:
  - base: cif + duty
  - vat: base * 0.15
expected:
  base: 2200000
  vat: 330000
```

## Ask the client first

- Taxable supplies in the last 12 months and expected in the next 12?
- Monthly or quarterly filer, and invoice or payments basis?
- Any exports, services to non-residents, or a business sale?
- Imports: tariff line, customs value, duty and excise?
- Any residential rent, financial services or education supplies?

## Sources

| Source | URL | Read on |
|---|---|---|
| Value Added Tax Act [Cap 247], Consolidated Edition 2020, ss 10 to 17, 20, 42, Sch 1 and 3 (Read for rates, registration, periods and dates) | https://vanuatucustoms.gov.vu/images/Laws_Regulations/VAT/247_Value_Added_Tax_Consolidated_2020.pdf | 2026-11-14 |
| DCIR, Introduction to VAT (Read for VT4 million, VT8 million, due dates, tax invoices) | https://vanuatucustoms.gov.vu/taxes-and-licensing/taxes/value-added-tax-vat/introduction.html | 2026-11-14 |
| VAT Amendment Act No. 13 of 2021 (Read by Ryan Duguid for the 22 July 2021 Schedule 3 change) | https://doft.gov.vu/images/2021/TaxPolicy/Tax/Value_Added_Tax_Amendment_Act_No_13_of_2021.pdf | 2026-11-11 |
| Tax Administration Act No. 37 of 2018, s 11 (Read by Ryan Duguid for extensions) | https://vanuatucustoms.gov.vu/images/TAA/Tax_Administration_Act_No_37_of_2018.pdf | 2026-11-11 |
| Import Duties Amendment Act No. 24 of 2023 (Read by Ryan Duguid for the new tariff schedule) | https://vanuatucustoms.gov.vu/images/Customs_Tariff/2024/IMPORT%20DUTIES%20CONSOLIDATION%20AMENDMENT%20ACT%20NO.%2024%20OF%202023.pdf | 2026-11-11 |

Not yet confirmed: late filing and payment penalty amounts under the Tax Administration Act; import VAT where excise also applies; individual tariff rates and concession eligibility after Act No. 24 of 2023; whether any order has changed the VT 8 million Category B limit.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `vu-vat-gst` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/vu-vat-gst. If neither is available, confirm every figure against the official source pages cited above before relying on it.
