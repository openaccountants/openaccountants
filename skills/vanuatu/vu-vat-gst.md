---
name: vu-vat-gst
description: "Vanuatu VAT, tax year 2026: 15% standard rate and 0% Schedule 3 supplies, exempt supplies, the VT 4 million registration test and 21-day application, monthly and quarterly periods, returns by the 27th (5 January for November), accounting basis, import VAT base, from the VAT Act [Cap 247] and DCIR."
version: 1.4
jurisdiction: VU
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: computation
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
| Quarterly (Category B) periods, on written application | Taxable supplies of VT 8 million or less in the relevant 12 months, subject to ss 15(3) and (4) | 2026 | https://vanuatucustoms.gov.vu/images/Laws_Regulations/VAT/247_Value_Added_Tax_Consolidated_2020.pdf |
| Application to register once liable | Within 21 days (s 12(3)) | 2026 | https://vanuatucustoms.gov.vu/images/Laws_Regulations/VAT/247_Value_Added_Tax_Consolidated_2020.pdf |
| Interest the Director pays on a late refund | 15% per annum after 15 working days (s 42) | 2026 | https://vanuatucustoms.gov.vu/images/Laws_Regulations/VAT/247_Value_Added_Tax_Consolidated_2020.pdf |

The Act tests registration at the end of each month over the past 12 months and at the start of each month over the coming 12 (s 12(1)). Disregard exempt supplies and, where the Director is satisfied, supplies caused solely by cessation, substantial permanent reduction or capital asset replacement (s 12(2)). For Category B, the 12 months end on the last day of a month. Section 15(4) deals with excesses solely due to cessation, substantial permanent reduction or capital asset replacement. The Minister may change the Category B limit by order.

## The base

- **Domestic supplies.** VAT on the value of the supply (s 10, s 11(1)(a)).
- **Imports.** VAT on the customs value, plus customs duty, plus excise, plus the cost of transport to Vanuatu and insurance for it (s 11(1)(b)). DCIR's no-excise clearance calculation takes the cost, insurance and freight value once and adds duty before applying 15%.
- **Zero-rated (Sch 3).** Exports meeting the conditions, goods outside Vanuatu at supply, international transport, services physically performed outside Vanuatu, services meeting para 5, eligible direct supplies for approved aid projects and a going concern sold to a registered person where both agree in writing (para 9). For para 5, check the non-resident's business and location, the connection to tangible property in Vanuatu and whether an unregistered person receives performance in Vanuatu. From 22 July 2021 the Tax Administration Act residency definitions apply (VAT Amendment Act No. 13 of 2021).
- **Exempt (Sch 1).** Financial services, hire of accommodation in a residential dwelling, qualifying leasehold rent, education supplied by an educational institution and donated goods and services supplied by a non-profit body. The property disposal rule covers a dwelling or the reversionary interest in the fee simple estate of leasehold land sold by a registered person in a taxable activity. The person must have used it exclusively for exempt residential or qualifying leasehold rental for at least 5 years before the sale. No input credit for acquisitions used solely for exempt supplies.
- **Input credit.** Claim only to the extent the goods or services are acquired for making taxable supplies. Hold a tax invoice or debit or credit note at filing for a domestic purchase or adjustment unless none is required. Section 19 specifies separate rules for imports and eligible second-hand goods. A registered supplier providing a taxable supply must issue a required invoice within 28 days of a registered customer's request. Section 21(5) allows an exception for cash consideration of VT 5,000 or less, subject to any higher limit set by order, and where the Director makes the specified determination.

## Deadlines and filing

- **Periods.** Category A is monthly; Category B is three-monthly on written application (s 15).
- **Returns and payment.** For a period ending 30 November, by 5 January; for any other period, by the 27th of the following month; a non-working day moves the ordinary due date to the next working day (ss 16 and 20). A creditor selling a registered debtor's goods in satisfaction of debt files a special return by the 27th of the month after the taxable period and remits the VAT. Both parties exclude the sale and VAT from their other returns (s 16(2)).
- **Extensions.** An individual filing extension under Tax Administration Act s 11 leaves the payment date unchanged; a general extension the Director grants to all taxpayers or a class under s 11(7) also extends payment.
- **Accounting basis.** Invoice or payments basis, elected in the approved form; with no election, the payments basis applies (s 17).

## Penalties and interest

DCIR's guide says late payment penalties are assessed. The Tax Administration Act No. 37 of 2018 sets out penalties and interest. The Director pays interest at 15% a year from the day after an excess-credit refund required under s 41 is due (s 42). The ordinary refund deadline is 15 working days after receiving the return. Check s 41 for investigation, set-off and outstanding-return provisions.

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
