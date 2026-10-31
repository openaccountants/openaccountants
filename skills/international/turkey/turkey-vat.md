---
name: turkey-vat
description: "Turkish value added tax (katma değer vergisi, KDV) for tax year 2026 under the VAT Law no. 3065 and the KDV General Implementation Communiqué, for companies, sole traders and foreign suppliers. Covers what is taxable, who must register (no threshold), place of supply and services used in Türkiye, the 20% general rate and the 10% and 1% list rates, export and other exemptions, input VAT deduction and its time limit, blocked VAT on passenger cars, excess VAT carried forward, refunds for exempt supplies, reverse charge on services bought from abroad (return no. 2), electronic services sold to consumers by foreign suppliers, monthly returns by the 28th, payment, penalties and late-payment interest. Trigger on: KDV, Turkish VAT, KDV beyannamesi, 1 No.lu, 2 No.lu, sorumlu sıfatıyla KDV, KDV iadesi, ihracat istisnası. Out of scope: income tax (turkey-pit), company tax (tr-corporate-income-tax), payroll (tr-payroll-social), special consumption tax (ÖTV), customs duty."
version: 2.1
jurisdiction: TR
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - vat-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Türkiye: VAT (katma değer vergisi, KDV) (2026) v2.1

Turkish VAT is charged under the Katma Değer Vergisi Kanunu no. 3065 and collected by the Revenue Administration (GİB). The KDV General Implementation Communiqué (KDV Genel Uygulama Tebliği, KDVGUT) sets the detailed rules. Figures below come from the consolidated law on mevzuat.gov.tr, which includes the 2026 amending laws 7573, 7577, 7578, 7587 and 7590, from the consolidated KDVGUT, and from GİB's current table of filing and payment dates.

## Who this applies to

- **Taxable transactions** (art. 1): supplies of goods and services made in Türkiye in the course of commercial, industrial, agricultural or professional activity; imports of all goods and services; and listed other supplies (post and telecoms, broadcasting, gambling, shows with professional artists or athletes, auction sales, pipeline transport and others).
- **Made in Türkiye** (art. 6): goods are supplied in Türkiye if they are in Türkiye when delivered. Services are supplied in Türkiye if they are performed in Türkiye or used (benefited from) in Türkiye.
- **Who is liable** (art. 8): the supplier of the goods or services; the importer; the person letting property and rights listed in GVK art. 70; and anyone who shows VAT on an invoice without the right to do so (they must pay it).
- **No registration threshold.** Liability follows from making taxable supplies in the course of business (art. 1, 8). There is no turnover test in the law. Businesses taxed under the simple method (basit usul) for income tax are exempt under art. 17(4)(a) unless they opt out (KDVGUT V/B-1).
- **Foreign suppliers.** Where the supplier has no domicile, workplace, legal seat or business seat in Türkiye, the Turkish customer is made responsible for the VAT and pays it by reverse charge (art. 9(1); KDVGUT I/C-2.1.2.1). A foreign supplier of electronic services to Turkish individuals who are not VAT taxpayers registers and pays the VAT itself (art. 9(1)).
- **Out of this skill:** special consumption tax (ÖTV) and customs duty; partial withholding (kısmi tevkifat) ratios; special VAT bases (özel matrah); investment incentive and tourism VAT refund schemes.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| General rate (goods and services on no list) | 20% | 2026 | Decision 2007/13033 art. 1(1)(a) as amended by Presidential Decision 7346, in force 10 July 2023, https://www.resmigazete.gov.tr/eskiler/2023/07/20230707-11.pdf |
| Reduced rate, list (II) | 10% | 2026 | Decision 2007/13033 art. 1(1)(c) as amended by Decision 7346 |
| Reduced rate, list (I) | 1% | 2026 | Decision 2007/13033 art. 1(1)(b), cited in KDVGUT; https://www.mevzuat.gov.tr/File/GeneratePdf?mevzuatNo=19631&mevzuatTur=Teblig&mevzuatTertip=5 |
| Food and non-alcoholic drink served in restaurants, cafés and patisseries | 10% (alcoholic drinks 20%) | 2026 | KDVGUT, reduced-rate section |
| Statutory rate the President may vary | 10% in the law, range 1% to four times | 2026 | KDV Law art. 28, https://www.mevzuat.gov.tr/MevzuatMetin/1.5.3065.pdf |
| Registration threshold | None | 2026 | KDV Law art. 1, 8 |
| Tax period | Calendar month for real-method taxpayers (quarters for some transport businesses, housing co-operatives and simple-method opt-ins) | 2026 | KDV Law art. 39; KDVGUT V/B-1 |
| Return no. 1 (KDV 1), filed and paid by | 28th of the following month, 23:59 | 2026 | GİB filing table (VUK Circular 149), https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Fyardim-kaynaklar%2Fyararli-bilgiler%2FBeyannameVermeveOdemeSureleri.pdf |
| Return no. 2 (reverse charge, sorumlu sıfatıyla), filed and paid by | 25th of the following month | 2026 | GİB filing table (VUK Circular 164) |
| Return no. 3 (foreign electronic service providers) | 28th of the following month | 2026 | GİB filing table (VUK Circular 149) |
| Input VAT time limit | By the end of the calendar year after the year of the tax point | 2026 | KDV Law art. 29(3) |
| Refund claim for exempt supplies with deduction | By the end of the second calendar year after the transaction | 2026 | KDV Law art. 32 |
| Late-payment surcharge | 3.7% a month | 2026 | Law 6183 art. 51, Presidential Decision 10556, https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6183.pdf |
| Missing invoice | 10% of the amount, at least TRY 17,000 for the first finding | 2026 | VUK art. 353(1), https://www.mevzuat.gov.tr/MevzuatMetin/1.5.213.pdf |

## The taxable base

**Exempt with the right to deduct.** Exports of goods and related services, services for customers abroad, toll processing for free-zone customers and inbound roaming are exempt, and the VAT on related purchases stays deductible (art. 11(1)(a), art. 32). A supply of goods is an export if it is made to a customer abroad (or in a free zone, or to a duty-free shop or authorised bonded warehouse) and the goods leave the Turkish customs area (art. 12(1)). A service is for a customer abroad only if the customer's domicile, workplace, legal seat and business seat are abroad (or it is a foreign branch of a Turkish firm acting on its own account) **and** the service is used abroad (art. 12(2)). Foreign passengers can recover VAT on goods they take out of the country (art. 11(1)(b)).

**Exempt without the right to deduct (main items).** Transactions within the scope of the banking and insurance transactions tax (BSMV) and insurance intermediaries' transactions with insurers (art. 17(4)(e)); lettings of immovable property that is not part of a business (art. 17(4)(d)); supplies by simple-method businesses (art. 17(4)(a)); sales by companies of participations held for at least two full years (art. 17(4)(r)). VAT on purchases used for exempt-without-deduction supplies is not deductible (art. 30(a)).

**Input VAT deduction** (art. 29). A taxpayer deducts, against the output VAT of the period: VAT shown on invoices for goods and services bought for the business; VAT paid on imports of goods and services; and, from the January 2024 period, VAT it declared and paid itself as the responsible party (reverse charge or withholding) (art. 29(1)(a), (b), (ç)). VAT declared on return no. 2 is deducted on the return no. 1 for the period in which it is paid. If return no. 2 is filed and paid on time and before return no. 1 for the same month, the VAT is deducted on that month's return no. 1 (KDVGUT III/C-1). The deduction must be taken in the period the invoice is entered in the books, and no later than the end of the calendar year after the tax point (art. 29(3)). If deductible VAT is more than output VAT, the excess is carried forward and is not refunded, except under the special rules for reduced-rate supplies and exempt supplies (art. 29(2), 32).

**Blocked input VAT** (art. 30). Not deductible: VAT on purchases for exempt-without-deduction supplies; VAT on passenger cars (binek otomobil) of the business, unless the business rents out or operates passenger cars; VAT on goods lost (except in declared disasters); VAT on expenses that are not deductible for income or corporate tax; and VAT on receivables written off as worthless and not paid by the buyer.

**Refunds.** VAT that cannot be deducted because of exports and other art. 11, 13, 14 and 15 exemptions is refunded, if claimed by the end of the second calendar year after the transaction (art. 32). The refund procedure and documents are in KDVGUT part IV and are not covered here.

## Deadlines and filing

- **Monthly return no. 1 (KDV 1).** The law says the return is filed by the 24th of the following month and paid by the 26th (art. 41, 46). GİB's current table sets the 28th, 23:59, for both, under VUK Circular 149. A taxpayer files even in a month with no taxable transactions (art. 40(3)).
- **Return no. 2 (KDV 2).** The Turkish buyer who must pay VAT as the responsible party (reverse charge on services from abroad, full or partial withholding) files return no. 2 for the month the transaction took place, and only in months with such transactions. GİB's table sets the 25th of the following month for filing and payment (VUK Circular 164). A late invoice from the supplier does not delay the filing (KDVGUT I/C-2.1.1.1).
- **Return no. 3 (foreign e-service providers).** Filed and paid by the 28th of the following month (GİB table).
- **Ceasing business.** The return is filed by the 24th of the month after the business stops (art. 41(4)).
- **Imports.** VAT on imports is declared on the customs declaration and paid with customs duty (art. 40(4), 46(2)).

## Penalties and interest

- **Late return.** A first-degree irregularity (VUK art. 352): in 2026, TRY 35,000 for capital companies, TRY 17,000 for other first-class traders and professionals, TRY 8,700 for second-class traders (VUK table 1, Communiqué 588).
- **Tax loss.** One times the VAT lost; three times where fake or misleading documents are used; halved for a late return filed before an audit starts; increased by 50% for unregistered business (VUK art. 344).
- **Late payment.** 3.7% a month, daily for part months (Law 6183 art. 51).
- **Invoices.** For each invoice not issued or not received, or issued on paper when it had to be electronic, a special irregularity penalty of 10% of the amount, at least TRY 17,000 for the first finding in a calendar year (VUK art. 353(1)).

## Cross-border points

- **Services bought from abroad.** Services performed in Türkiye, or performed abroad but used in Türkiye, by a supplier with no domicile, workplace, legal seat or business seat in Türkiye are taxable. The Turkish customer computes VAT on the price and declares and pays it on return no. 2 (KDV Law art. 6(b), 9(1); KDVGUT I/C-2.1.2.1). It is then deductible as above.
- **Services sold abroad.** A Turkish business selling services to a customer abroad charges no VAT only if both tests in art. 12(2) are met: the customer is abroad and the service is used abroad. A service used in Türkiye is taxed at the normal rate even if the customer is foreign.
- **Foreign e-service providers to consumers.** A provider with no Turkish presence that sells electronic services to individuals who are not VAT taxpayers declares and pays the VAT itself on return no. 3 (art. 9(1); KDVGUT I/C-2.1.2.1.2).
- **Imports of goods.** Taxed at customs with customs duty (art. 46(2)). Deductible as import VAT (art. 29(1)(b)).
- **Foreign transport businesses and fair participants** may recover VAT on purchases for transport activity or for fairs and exhibitions, on a reciprocal basis (art. 11(1)(b)).

## Worked examples

### Example 1: Monthly return no. 1 with a carried-forward credit

A trading company in Istanbul sells goods for TRY 500,000 at 20% and restaurant meals for TRY 200,000 at 10% in March 2026 (net of VAT). Output VAT is TRY 100,000 plus TRY 20,000, so TRY 120,000. Its purchase invoices for March show TRY 60,000 of deductible VAT, and it carried forward TRY 5,000 of excess VAT from February. VAT payable for March is TRY 55,000. The return is filed and the tax paid by 28 April 2026.

```oa-check
name: Monthly KDV 1, TRY 700,000 sales at 20% and 10% (March 2026)
inputs:
  sales_20: 500000
  sales_10: 200000
  input_vat: 60000
  carried_forward: 5000
steps:
  - output_vat: sales_20 * 0.20 + sales_10 * 0.10
  - payable: output_vat - input_vat - carried_forward
expected:
  output_vat: 120000
  payable: 55000
```

### Example 2: Reverse charge on a foreign service, and a passenger car

A software company sells TRY 300,000 of services to Turkish customers in May 2026 (20% output VAT, TRY 60,000). It buys a cloud service for TRY 100,000 from a supplier with no Turkish presence, used in Türkiye, so it must declare TRY 20,000 of VAT on return no. 2 and pay it by 25 June. It has TRY 25,000 of VAT on domestic purchase invoices. It also buys a passenger car for the managers for TRY 1,000,000 plus TRY 200,000 VAT; that VAT is blocked by art. 30(b). Because return no. 2 is filed and paid on time and before return no. 1, the TRY 20,000 is deducted on the May return no. 1. Deductible VAT is TRY 45,000 and VAT payable on return no. 1 is TRY 15,000. Total VAT cash for May is TRY 35,000.

```oa-check
name: KDV 2 reverse charge plus blocked car VAT (May 2026)
inputs:
  sales_20: 300000
  domestic_input_vat: 25000
  foreign_service: 100000
  car_net: 1000000
steps:
  - output_vat: sales_20 * 0.20
  - reverse_charge_vat: foreign_service * 0.20
  - blocked_car_vat: car_net * 0.20
  - deductible_vat: domestic_input_vat + reverse_charge_vat
  - payable_kdv1: output_vat - deductible_vat
  - total_cash: reverse_charge_vat + payable_kdv1
expected:
  reverse_charge_vat: 20000
  blocked_car_vat: 200000
  deductible_vat: 45000
  payable_kdv1: 15000
  total_cash: 35000
```

## Ask the client first

1. Are you taxed under the real method (gerçek usul) or the simple method (basit usul) for income tax, and do you file monthly?
2. What do you sell, and are any of your goods or services on list (I) at 1% or list (II) at 10%?
3. Do you sell to customers abroad, and is the service used abroad? Do you have customs export declarations for goods?
4. Do you buy services from suppliers with no Turkish presence (software, advertising, cloud, consulting)? Were the 2 No.lu returns filed and paid on time?
5. Do you buy or lease passenger cars, or have expenses that are not deductible for income or corporate tax?
6. Do you have excess VAT carried forward, or a refund claim from exports?

## Sources

| Source | URL | Read on |
|---|---|---|
| Katma Değer Vergisi Kanunu no. 3065, consolidated (to Law 7590): arts. 1, 6, 8, 9, 11, 12, 17(4), 28, 29, 30, 32, 39, 40, 41, 46 | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.3065.pdf | 2026-10-31 |
| KDV Genel Uygulama Tebliği, consolidated: I/C-2.1 (withholding and reverse charge), III/C-1 (deduction), V/B-1 (tax period), reduced-rate section | https://www.mevzuat.gov.tr/File/GeneratePdf?mevzuatNo=19631&mevzuatTur=Teblig&mevzuatTertip=5 | 2026-10-31 |
| Presidential Decision 7346 amending Decision 2007/13033 (18% to 20%, 8% to 10%), Official Gazette 7 July 2023 no. 32241 | https://www.resmigazete.gov.tr/eskiler/2023/07/20230707-11.pdf | 2026-10-31 |
| GİB, Beyanname verme ve ödeme süreleri | https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Fyardim-kaynaklar%2Fyararli-bilgiler%2FBeyannameVermeveOdemeSureleri.pdf | 2026-10-31 |
| Vergi Usul Kanunu no. 213, consolidated: arts. 344, 352, 353, table 1 (2026 amounts, Communiqué 588) | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.213.pdf | 2026-10-31 |
| Law 6183, art. 51 | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6183.pdf | 2026-10-31 |

Not yet confirmed: the full contents of lists (I) and (II) of Decision 2007/13033 (which goods and services are at 1% and 10%; the old version listed basic food, residential first sales, medicines, medical equipment, hotels and domestic flights without a source), and whether item changes since 2023 moved any goods between lists; the e-invoice (e-Fatura) and e-archive thresholds under VUK Communiqué 509 (the old version said TRY 3 million); the return boxes on KDV 1 (the old version listed boxes 101 to 113 without a source); partial withholding (kısmi tevkifat) ratios for construction, cleaning, security, scrap and other services; the export refund procedure, documents and the role of a YMM report; the input VAT rule for entertainment (the old version gave a 50% block without a source); exemptions for education, health, land and residential first sales; whether the 1% rate still applies to residential sales and on what conditions; the capital goods adjustment; special bases (özel matrah) for used cars and gold; the tourism VAT refund to foreigners; the legal basis of GİB's 28th and 25th deadlines beyond the circular numbers in GİB's table.
<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
