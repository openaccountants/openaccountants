---
name: poland-vat-return
description: "Polish VAT (podatek od towarów i usług) for tax year 2026: who must register, the 23%, 8%, 5% and 0% rates, the small-business exemption of PLN 240,000 (raised from PLN 200,000 on 1 January 2026) and the EU SME scheme, the JPK_V7M and JPK_V7K files due on the 25th, refunds in 40 days, KSeF structured e-invoicing (mandatory from 1 February 2026 for businesses with 2024 sales over PLN 200 million, from 1 April 2026 for the rest, with a PLN 10,000 a month carve-out to the end of 2026), split payment above PLN 15,000 for Annex 15 goods, the white list, reverse charge, the 30% additional liability and 10.50% late interest. Trigger on: Polish VAT, JPK_V7, KSeF, zwolnienie podmiotowe, MPP, biała lista, VAT-R. Out of scope: KSeF schema detail (poland-einvoice), income tax (pl-income-tax, pl-cit-corporate-tax), cross-border income (pl-cross-border)."
version: 2.1
jurisdiction: PL
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
verified_by: pending
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Poland VAT return (2026)

Source-cited draft: not reviewed by an accountant. Built by Michael Cutajar and the OpenAccountants team.

This skill covers Polish VAT for a business registered in Poland: when to register, the rates, the monthly or quarterly JPK_V7 file, KSeF e-invoicing, split payment and the white list. It links to the other Poland skills and does not repeat them:

- [poland-einvoice](poland-einvoice.md): the FA(3) structured invoice, KSeF access, offline modes.
- [pl-income-tax](pl-income-tax.md) and [pl-cit-corporate-tax](pl-cit-corporate-tax.md): income tax of sole traders and companies, including the cost rules tied to the white list.
- [pl-cross-border](pl-cross-border.md): income tax for people moving in or out of Poland.
- EU rules on place of supply, intra-EU supplies and OSS are in [eu-vat-directive](../eu/eu-vat-directive.md); the general return workflow is in [vat-workflow-base](../../foundation/vat-workflow-base.md).

**Which text of the law.** VAT Act (ustawa z dnia 11 marca 2004 r. o podatku od towarów i usług), consolidated text Dz.U. 2026 poz. 1263, the law as at 26 August 2026. The next amendment, Dz.U. 2026 poz. 1270, takes effect on 1 January 2027 and is not covered here. Tax Ordinance, Dz.U. 2026 poz. 622.

## Who this applies to

- **Taxable persons.** Anyone carrying on a business independently, whatever its purpose or result (VAT Act art. 15). Taxable supplies are supplies of goods and services for consideration in Poland, exports, imports, intra-EU acquisitions and intra-EU supplies (art. 5).
- **Registration.** A business must file the VAT-R registration form with its tax office before its first taxable supply (art. 96 ust. 1). A business that only makes exempt supplies, or uses the small-business exemption, may register but need not (art. 96 ust. 3).
- **Small-business exemption (zwolnienie podmiotowe).** A business seated in Poland whose sales, without VAT, did not exceed PLN 240,000 in the previous year and do not exceed it in the current year is exempt (art. 113 ust. 1, amended by Dz.U. 2025 poz. 896 from 1 January 2026). A business that starts during the year uses the limit in proportion to the part of the year it trades (art. 113 ust. 9). The exemption is lost from the sale that crosses the limit (art. 113 ust. 5 and 10).
- **Who cannot use the exemption.** Sellers of goods in Annex 12, most excise goods, new buildings, building land, new means of transport, certain goods sold at a distance online, and car parts; and providers of legal services, advisory services (except agricultural advice), jewellery services and debt collection, including factoring (art. 113 ust. 13). They register from the first sale.
- **EU businesses (SME scheme).** A business seated in another EU state can be exempt in Poland if its EU-wide turnover is not over EUR 100,000 and its Polish sales are within PLN 240,000, using an EX number issued by its home state (art. 113a). A Polish business can use the other states' exemptions on the same EUR 100,000 test, after a prior notice to its Polish tax office (art. 113b).
- **Small taxpayer (mały podatnik).** A business whose sales including VAT were not over EUR 2,000,000 in the previous year (art. 2 pkt 25). For 2026 this is PLN 8,517,000 at the NBP rate of 1 October 2025 (4.2586), rounded to PLN 1,000. A small taxpayer may file quarterly and may elect the cash method (art. 21, art. 99 ust. 2-3).
- **Out of scope.** VAT groups, the margin schemes, flat-rate farmers, fiscal representatives and OSS or IOSS returns.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate | 23% (the base rate of 22% in art. 41 ust. 1 is raised by art. 146ef while defence spending is above 3% of GDP; no end has been announced) | 2026 | https://api.sejm.gov.pl/eli/acts/DU/2026/1263/text.pdf (art. 41 ust. 1, art. 146ef ust. 1) |
| Reduced rate, Annex 3 goods and services | 8% | 2026 | same, art. 41 ust. 2, art. 146ef ust. 1 pkt 2 |
| Reduced rate, restaurant and catering services (PKWiU 56), with exceptions such as alcohol | 8% | 2026 | Minister of Finance regulation of 9 December 2023 on reduced rates, as summarised at https://www.podatki.gov.pl/podatki-firmowe/vat/stawki-i-limity |
| Reduced rate, Annex 10 goods (basic foods, books, some hygiene goods) | 5% | 2026 | same, art. 41 ust. 2a |
| Intra-EU supply of goods; export of goods | 0% (export needs proof of exit before the return deadline) | 2026 | same, art. 41 ust. 3, 4, 6 |
| Small-business exemption: sales without VAT, previous and current year | PLN 240,000 | 2026 | same, art. 113 ust. 1; https://www.podatki.gov.pl/podatki-firmowe/vat/stawki-i-limity |
| Businesses with 2025 sales over PLN 200,000 and up to PLN 240,000 | may use the exemption in 2026 | 2026 | Dz.U. 2025 poz. 896 art. 2, quoted in the notice to Dz.U. 2026 poz. 1263 |
| EU SME scheme: EU-wide turnover cap | EUR 100,000 | 2026 | VAT Act art. 113a ust. 1, art. 113b ust. 1 |
| Small taxpayer: previous-year sales including VAT | EUR 2,000,000 = PLN 8,517,000 | 2026 | VAT Act art. 2 pkt 25; https://api.nbp.pl/api/exchangerates/rates/a/eur/2025-10-01/?format=json |
| Split payment (MPP) compulsory: Annex 15 goods or services on an invoice with a gross total over | PLN 15,000 | 2026 | VAT Act art. 108a ust. 1a |
| Payment between businesses must go through a bank account if one transaction is over | PLN 15,000 | 2026 | https://api.sejm.gov.pl/eli/acts/DU/2025/1480/text.pdf (Business Law art. 19) |
| Input VAT on cars used also privately | 50% | 2026 | VAT Act art. 86a ust. 1 |
| KSeF: last month a business may issue paper or PDF invoices if 2024 sales with VAT were up to PLN 200,000,000 | March 2026 | 2026 | VAT Act art. 145l |
| KSeF: invoices outside KSeF still allowed if invoices issued in the month total PLN 10,000 or less with VAT | to 31 December 2026 | 2026 | VAT Act art. 145m |
| Refund of excess input VAT | 40 days from filing (25 days if the conditions of art. 87 ust. 6 are met) | 2026 | VAT Act art. 87 ust. 2, 6 |
| Late payment interest | 10.50% a year from 5 March 2026; reduced 5.25%; higher 15.75% | 2026 | https://api.sejm.gov.pl/eli/acts/MP/2026/269/text.pdf; Tax Ordinance art. 56 § 1; https://static.nbp.pl/dane/stopy/stopy_procentowe_archiwum.xml |

## The taxable base

- **Output VAT.** The base is everything the seller receives for the supply, without the VAT itself (art. 29a). The tax point is generally the supply of the goods or the completion of the service (art. 19a). A small taxpayer on the cash method pays VAT when paid, and for buyers who are not active VAT payers no later than the 180th day after the supply (art. 21).
- **Input VAT.** VAT on purchases used for taxed sales can be deducted (art. 86). Not deductible: hotel and restaurant services, except some packaged ones; purchases from a business that does not exist; and invoices for supplies that did not take place or show false amounts (art. 88). For cars used also privately only 50% is deductible, including fuel and running costs; 100% needs exclusive business use, a mileage log and a VAT-26 notice (art. 86a).
- **Exempt supplies.** Financial, insurance, health, education and most residential rental services are exempt without the right to deduct (art. 43). A business with mixed supplies deducts by the turnover ratio (art. 90).
- **Reverse charge.** The Polish buyer accounts for the VAT when:
  - it buys services from a foreign business under the general B2B rule (import of services, art. 17 ust. 1 pkt 4, art. 28b);
  - it acquires goods from another EU state (intra-EU acquisition, art. 9);
  - it buys goods in Poland from a foreign business not registered here, for example gas or electricity through the network (art. 17 ust. 1 pkt 5).
  Output and input VAT on the same purchase usually cancel out, if the buyer has full deduction.
- **Excess input VAT** is carried forward or refunded to a Polish bank account in 40 days (art. 87 ust. 1-2).
- **Rounding.** Tax amounts in the return are in whole złoty (Tax Ordinance art. 63).

## Deadlines and filing

| What | When | Rule |
|---|---|---|
| Registration (VAT-R) | before the first taxable supply | VAT Act art. 96 ust. 1 |
| Monthly JPK_V7M (return and VAT records in one file) and payment | 25th of the following month | art. 99 ust. 1, 11c; art. 103 ust. 1; art. 109 ust. 3b |
| Quarterly JPK_V7K and payment (small taxpayers on notice, or on the cash method) | return and payment by the 25th after the quarter; the records for months 1 and 2 by the 25th of the next month | art. 99 ust. 2-3, art. 103 ust. 2, art. 109 ust. 3c |
| Notice to switch to quarterly filing | by the 25th of the second month of the first quarter | art. 99 ust. 3 |
| Correction of a JPK file the business finds wrong | within 14 days of finding the error | art. 109 ust. 3e |
| Response to a tax office notice of errors in the JPK file | within 14 days of delivery | art. 109 ust. 3g |
| KSeF structured invoices, businesses with 2024 sales over PLN 200,000,000 | from 1 February 2026 | art. 106ga, art. 145l |
| KSeF structured invoices, all other Polish businesses | from 1 April 2026; those issuing PLN 10,000 a month or less may stay outside KSeF until 31 December 2026 | art. 145l, art. 145m |
| Invoices from cash registers and receipts treated as invoices | allowed outside KSeF until 31 December 2026 | art. 145n |
| Invoice deadline | by the 15th of the month after the supply | art. 106i ust. 1 |

Quarterly filing is not open to a newly registered business for its first 12 months, nor to anyone who supplied over PLN 50,000 a month of Annex 15 goods in the quarter or the previous four quarters, imported goods under the simplified procedure of art. 33a in the quarter, or failed to accept card or other electronic payment where Business Law art. 19a requires it (art. 99 ust. 3a). KSeF does not apply to invoices issued to consumers, by businesses with no seat or fixed establishment in Poland, or by EU businesses using the SME scheme (art. 106ga ust. 2). All files go through e-Urząd Skarbowy or interface software; there is no paper return (art. 99 ust. 11b).

## Penalties and interest

- **Additional VAT liability.** If an audit finds VAT understated or a refund overstated, the tax office sets an additional liability of up to 30% of the difference (art. 112b ust. 1). It is up to 20% if the business files a correction and pays after a tax audit, and up to 15% after a customs and tax audit (art. 112b ust. 2, 2a). It is 100% of the input VAT on a fake or false invoice used knowingly (art. 112c). It does not apply if the business corrects and pays with interest before an audit starts, or to arithmetic errors and VAT booked in the wrong period before an audit (art. 112b ust. 3).
- **Split payment.** Paying an Annex 15 invoice over PLN 15,000 without split payment costs an additional liability of 30% of the VAT on that invoice, unless the supplier paid the full VAT (art. 108a ust. 7-8). The buyer also cannot book the cost for income tax (PIT Act art. 22p ust. 1 pkt 3; CIT Act art. 15d).
- **White list.** Paying an invoice over PLN 15,000 to an account not on the VAT payers list (wykaz podatników VAT) on the day the transfer is ordered makes the buyer jointly liable for the seller's unpaid VAT on that supply (Tax Ordinance art. 117ba). The buyer escapes this by paying through split payment or notifying its tax office within 7 days of ordering the transfer (art. 117ba § 3 pkt 2 and 4). The same payment is also not a deductible cost (PIT Act art. 22p ust. 1 pkt 2).
- **JPK errors.** The tax office may charge PLN 500 for each error the business fails to correct or explain within 14 days of a tax office notice (art. 109 ust. 3h). Not charged to an individual who is liable under the Fiscal Penal Code for the same act.
- **KSeF.** Fines of up to 100% of the VAT on an invoice issued outside KSeF, or up to 18.7% of the total on an invoice without VAT, apply only from 1 January 2027 (art. 106ni).
- **Late payment interest.** 200% of the NBP lombard rate plus 2 points, at least 8% (Tax Ordinance art. 56 § 1): 10.50% a year from 5 March 2026, when the lombard rate fell to 4.25% (M.P. 2026 poz. 269). It is reduced to 5.25% if a correction is filed within 6 months of the deadline and the tax is paid within 7 days (Tax Ordinance art. 56a). It rises to 15.75% on VAT understatements found in an audit, or corrected after one starts, that exceed 25% of the tax due and five times the minimum wage (art. 56b).
- **Fiscal Penal Code.** A false return or failure to file that puts tax at risk can lead to a fine of up to 720 daily rates or prison (art. 54, 56). Persistent late payment is a petty offence (art. 57). Not issuing an invoice, or issuing a faulty one, carries a fine of up to 180 daily rates (art. 62). A valid correction (art. 16a) removes liability for the return itself.

## Cross-border points

- **Services from abroad.** B2B services from a foreign supplier are taxed where the buyer is established (art. 28b) and reported by the Polish buyer under the reverse charge. They appear in the JPK file as import of services, as output and input tax.
- **Goods within the EU.** Intra-EU supplies are 0% if the buyer has a valid EU VAT number checked in VIES and the seller holds proof of transport (art. 41 ust. 3, art. 42). Intra-EU acquisitions are taxed by the Polish buyer (art. 9). Recapitulative statements and OSS are covered in [eu-vat-directive](../eu/eu-vat-directive.md).
- **Imports.** VAT on imports is paid to customs, or settled in the JPK file under the simplified procedure of art. 33a.
- **Foreign businesses.** A business without a seat or fixed establishment in Poland registers before its first taxable supply in Poland, does not issue KSeF invoices (art. 106ga ust. 2 pkt 1) and is refunded under its own rules. EU businesses can use the SME scheme above.
- **From 1 January 2027.** Dz.U. 2026 poz. 1270 changes the reverse charge on supplies exempt under art. 43 and art. 113a, and the rules on deregistration. Not covered here.

## Worked examples

### Example 1: a company's monthly JPK_V7M

Alfa sp. z o.o. files monthly. In March 2026 it sells goods for PLN 100,000 net at 23% and catering for PLN 20,000 net at 8%. It buys software from an Irish supplier for PLN 5,000 (reverse charge, 23%). Domestic purchase invoices show input VAT of PLN 9,200. Its director's car is also used privately; the fuel and service invoices show VAT of PLN 1,000, of which 50% is deductible.

Output VAT: 23,000 + 1,600 + 1,150 (reverse charge) = PLN 25,750. Input VAT: 1,150 (reverse charge) + 9,200 + 500 (car) = PLN 10,850. Alfa pays PLN 14,900 by 25 April 2026, with the JPK_V7M for March.

```oa-check
name: Alfa sp. z o.o., JPK_V7M March 2026
inputs:
  sales_23: 100000
  sales_8: 20000
  saas_eu: 5000
  domestic_input: 9200
  car_vat: 1000
steps:
  - out_23: sales_23 * 0.23
  - out_8: sales_8 * 0.08
  - rc: saas_eu * 0.23
  - car_input: car_vat * 0.5
  - output_vat: out_23 + out_8 + rc
  - input_vat: rc + domestic_input + car_input
  - payable: output_vat - input_vat
expected:
  output_vat: 25750
  input_vat: 10850
  payable: 14900
```

### Example 2: a new sole trader crosses the pro-rata exemption limit

Ewa starts a graphic design business on 1 April 2026 and uses the small-business exemption. Design is not on the excluded list. Her limit for 2026 is PLN 240,000 in proportion to the 275 days from 1 April to 31 December: PLN 180,821.92. By mid-November her sales total PLN 178,000. Her next invoice, for PLN 6,000 net to a business client, takes her to PLN 184,000. The exemption ends with that invoice (art. 113 ust. 10). She charges 23% on it and on the PLN 20,000 she invoices for the rest of the year, and registers as an active VAT payer.

VAT due: 6,000 x 23% = PLN 1,380, plus 20,000 x 23% = PLN 4,600, total PLN 5,980. As a new registrant she files monthly for her first 12 months (art. 99 ust. 3a pkt 1).

```oa-check
name: Ewa, start 1 April 2026, exemption lost mid-November
inputs:
  annual_limit: 240000
  days_trading: 275
  days_in_year: 365
  sales_before: 178000
  crossing_sale: 6000
  later_sales: 20000
steps:
  - limit: round(annual_limit * days_trading / days_in_year, 2)
  - total_after: sales_before + crossing_sale
  - over: total_after - limit
  - vat_crossing: crossing_sale * 0.23
  - vat_later: later_sales * 0.23
  - vat_due: vat_crossing + vat_later
expected:
  limit: 180821.92
  total_after: 184000
  over: 3178.08
  vat_due: 5980
```

## Ask the client first

1. What were sales without VAT in 2025, and to date in 2026? When did the business start? (Exemption, small-taxpayer status.)
2. What does the business sell? Anything on the art. 113 ust. 13 list, in Annex 15, or at 8% or 5%?
3. Monthly or quarterly filing, cash method, and since when? Was the business registered in the last 12 months?
4. Are invoices issued in KSeF, and from what date? What were 2024 sales including VAT? How much is invoiced each month outside KSeF?
5. Any purchases or sales with other EU states or outside the EU? Any foreign software or advertising suppliers?
6. Cars: used only for business with a mileage log and VAT-26 notice, or also privately? Payments over PLN 15,000: by split payment, and to accounts on the white list?

## Sources

| Source | URL | Read on |
|---|---|---|
| VAT Act, consolidated text Dz.U. 2026 poz. 1263, with the transitional provisions of Dz.U. 2025 poz. 896 and 1203 quoted in the notice (art. 2 pkt 25, 5, 9, 15, 17, 19a, 21, 28b, 29a, 41, 43, 86, 86a, 87, 88, 96, 99, 103, 106ga, 106i, 106ni, 108a, 109, 112b, 112c, 113, 113a, 113b, 145l-145n, 146ef) | https://api.sejm.gov.pl/eli/acts/DU/2026/1263/text.pdf | 2026-10-23 |
| Amending act Dz.U. 2026 poz. 1270, in force 1 January 2027 (not applied) | https://api.sejm.gov.pl/eli/acts/DU/2026/1270/text.pdf | 2026-10-23 |
| Tax Ordinance, Dz.U. 2026 poz. 622 (art. 56, 56a, 56b, 63, 117ba) | https://api.sejm.gov.pl/eli/acts/DU/2026/622/text.pdf | 2026-10-23 |
| Minister of Finance notice on late payment interest, M.P. 2026 poz. 269 | https://api.sejm.gov.pl/eli/acts/MP/2026/269/text.pdf | 2026-10-23 |
| Business Law (Prawo przedsiębiorców), Dz.U. 2025 poz. 1480 (art. 19) | https://api.sejm.gov.pl/eli/acts/DU/2025/1480/text.pdf | 2026-10-23 |
| PIT Act, Dz.U. 2026 poz. 592 (art. 22p) | https://api.sejm.gov.pl/eli/acts/DU/2026/592/text.pdf | 2026-10-23 |
| Fiscal Penal Code, Dz.U. 2025 poz. 633 (art. 16a, 54, 56, 57, 62) | https://api.sejm.gov.pl/eli/acts/DU/2025/633/text.pdf | 2026-10-23 |
| Ministry of Finance, VAT rates and limits (PLN 240,000 exemption) | https://www.podatki.gov.pl/podatki-firmowe/vat/stawki-i-limity | 2026-10-23 |
| Ministry of Finance, KSeF portal | https://ksef.podatki.gov.pl/ | 2026-10-23 |
| NBP base rates archive (lombard rate 4.25% from 5 March 2026) | https://static.nbp.pl/dane/stopy/stopy_procentowe_archiwum.xml | 2026-10-23 |
| NBP EUR mid rate of 1 October 2025 (4.2586) | https://api.nbp.pl/api/exchangerates/rates/a/eur/2025-10-01/?format=json | 2026-10-23 |

Not yet confirmed: the PLN 8,517,000 small-taxpayer limit is computed here from the NBP rate; the Ministry page states the EUR 2,000,000 rule but no PLN figure. The CIT Act article on split payment and the white list (art. 15d) was not re-read for this version. When a business that has lost the small-business exemption must have filed VAT-R (before the crossing sale or before the next one) was not settled from the text of art. 96. The date the EU SME scheme (art. 113a-113b) first applied is not given in the consolidated text.
