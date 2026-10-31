---
name: tr-cross-border
description: "Turkish cross-border tax for tax year 2026: payments to non-residents and foreign income of Turkish companies. Covers full and limited liability, Turkish-source rules, workplace and permanent representative (PE), withholding on payments to non-resident companies under Corporate Tax Law art. 30 and Decision 2009/14593 (20% on fees, rent and royalties, 15% on dividends and branch remittances, 10% on most loan interest, 0% on foreign bank loans, 30% to listed countries), withholding on non-resident individuals under Income Tax Law art. 94, gross-up when the payer bears the tax, treaty relief and residence certificates, VAT reverse charge on imported services (return no. 2), CFC rules (art. 7), foreign tax credit (art. 33), deadlines and penalties. Trigger on: dar mükellef stopaj, yurt dışı hizmet alımı vergi, KVK 30, mukimlik belgesi, kontrol edilen yabancı kurum, Turkish withholding tax non-resident. Out of scope: treaty-by-treaty rates, transfer pricing (tr-transfer-pricing), corporate tax (tr-corporate-income-tax), VAT detail (turkey-vat)."
jurisdiction: TR
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-31
version: 0.1
---

# Türkiye: cross-border tax (2026) v0.1

This skill covers what a Turkish business must do when it pays a foreign person, and how Türkiye taxes a Turkish company's foreign subsidiaries and foreign tax. The rules are in the Corporate Tax Law no. 5520 (KVK) arts. 3, 7, 30 and 33, the Income Tax Law no. 193 (GVK) arts. 7, 8 and 94, the Tax Procedure Law no. 213 (VUK) art. 156 and the VAT Law no. 3065 (KDV) arts. 6, 9 and 29. The withholding rates are set by Presidential (formerly Council of Ministers) Decisions 2009/14593 (companies) and 2009/14592 (individuals), as changed; the Revenue Administration (GİB) publishes the current rates in two tables. Corporate tax itself is in [tr-corporate-income-tax](tr-corporate-income-tax.md), individuals in [turkey-pit](turkey-pit.md), VAT in [turkey-vat](turkey-vat.md) and related-party pricing in [tr-transfer-pricing](tr-transfer-pricing.md).

## Who this applies to

- **Resident companies.** A company whose legal seat or business seat (iş merkezi) is in Türkiye is fully liable on its worldwide profit (KVK art. 3(1)). The business seat is where the business is in fact run and managed (GVK art. 7(1)).
- **Non-resident companies.** A company with neither its legal seat nor its business seat in Türkiye is taxed only on Turkish income: trading profit through a Turkish workplace or permanent representative, Turkish farm income, professional income earned in Türkiye, rent for property or rights used in Türkiye, Turkish investment income and other Turkish income (KVK art. 3(2)-(3)). The GVK source rules apply (KVK art. 3(4)).
- **Individuals.** A person is resident if domiciled in Türkiye or staying more than six months in a calendar year, with exceptions for temporary assignments and study (GVK arts. 4 and 5). Residence and the 20-year foreign income exemption for new residents are in [turkey-pit](turkey-pit.md).
- **Turkish source** (GVK art. 7). Professional income is Turkish if the work is done in Türkiye or "evaluated" in Türkiye. Rent is Turkish if the property or right is used or evaluated in Türkiye. Investment income is Turkish if the capital is invested in Türkiye. "Evaluated" means the payment is made in Türkiye or, if paid abroad, is booked by or charged to the profit of the Turkish payer.
- **Who must withhold.** Anyone who pays or accrues income listed in KVK art. 30 to a non-resident company, in cash or on account, including advances (art. 30(1)). On payments to individuals, public bodies, companies, partnerships, associations, foundations, and traders and the self-employed who must declare actual income withhold under GVK art. 94.

## Rates, bands and thresholds

Domestic rates on payments to non-resident companies (KVK art. 30, Decision 2009/14593 as changed, GİB table) and to non-resident individuals (GVK art. 94, Decision 2009/14592 as changed, GİB table). A treaty can lower them (see Cross-border points).

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Professional (self-employment) fees to a non-resident company | 20% (5% for oil exploration) | 2026 | KVK art. 30(1)(b); GİB KVK 30 table, https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Fyardim-kaynaklar%2Fyararli-bilgiler%2Fkvk-nun-30-ve-gecici14-ile-gvk-nun-gecici-67inci-maddeleri-uyarinca-dar-mukellef.pdf |
| Rent for property or rights used in Türkiye, non-resident company | 20% (1% under financial leasing) | 2026 | KVK art. 30(1)(c); GİB KVK 30 table |
| Royalties and sale of intangible rights (copyright, patent, know-how, trade name, trade mark), non-resident company | 20% | 2026 | KVK art. 30(2); GİB KVK 30 table |
| Dividends from a Turkish company to a non-resident company | 15% | 2026 | KVK art. 30(3); Decision 9286, https://www.resmigazete.gov.tr/eskiler/2024/12/20241222-15.pdf; GİB KVK 30 table |
| Branch profit remitted to head office | 15% | 2026 | KVK art. 30(6); GİB KVK 30 table |
| Interest on loans from foreign states, international bodies, foreign banks and lenders that lend to the public | 0% | 2026 | KVK art. 30(1)(ç); GİB KVK 30 table |
| Late-payment charges on supplies of goods (vade farkı) | 5% | 2026 | GİB KVK 30 table |
| Other loan interest to a non-resident company | 10% | 2026 | GİB KVK 30 table |
| Payments for online advertising services | 15% | 2026 | KVK art. 30(1)(d); GİB KVK 30 table |
| Construction and repair spread over more than one year (general) | 5% (1% for rail, shipbuilding and nuclear plants) | 2026 | KVK art. 30(1)(a); Decisions 9707 and 11344; GİB KVK 30 table |
| Profits at authorised trade fairs | 0% | 2026 | KVK art. 30(5); GİB KVK 30 table |
| Any payment to a company in a country listed by the President | 30% | 2026 | KVK art. 30(7) |
| Professional fees to a non-resident individual | 20% (17% for GVK art. 18 work such as authors and inventors) | 2026 | GVK art. 94(2); GİB GVK 94 table, https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Fyardim-kaynaklar%2Fyararli-bilgiler%2Fgelir-vergisi-kanununun-94uncu-maddesinde-yer-alan-kesinti-oranlari.pdf |
| Sale of copyright and patent rights by a non-resident individual | 20% | 2026 | GVK art. 94(4); GİB GVK 94 table |
| Rent to an individual for property and rights under GVK art. 70 | 20% | 2026 | GVK art. 94(5)(a); GİB GVK 94 table |
| Dividends to a non-resident individual | 15% | 2026 | GVK art. 94(6)(b)(ii); Decision 9286 art. 1; GİB GVK 94 table |
| VAT on services bought from abroad (reverse charge), general rate | 20% | 2026 | KDV arts. 6(b), 9(1), 28; see [turkey-vat](turkey-vat.md) |
| CFC: control | At least 50% of capital, profit or votes | 2026 | KVK art. 7(1), https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5520.pdf |
| CFC: passive income share of gross revenue | 25% or more | 2026 | KVK art. 7(1)(a) |
| CFC: foreign tax burden on commercial profit | Below 10% | 2026 | KVK art. 7(1)(b) |
| CFC: gross revenue of the subsidiary | Above TRY 100,000 equivalent (YTL 100,000 in the law) | 2026 | KVK art. 7(1)(c) |
| Foreign tax credit carry-forward | 3 periods | 2026 | KVK art. 33(4) |
| Indirect foreign tax credit on dividends | Holding of at least 25% | 2026 | KVK art. 33(3) |
| Late-payment surcharge and late interest | 3.7% a month | 2026 | Law 6183 art. 51, Decision 10556, https://www.mevzuat.gov.tr/MevzuatMetin/1.3.6183.pdf; VUK art. 112(3) |

## The taxable base

- **Gross amount.** Withholding is worked out on the gross amount of the income (KVK art. 30(11)).
- **Gross-up.** If the payer takes on the tax, the base is the amount actually paid plus the tax the payer bears (art. 30(11)). At 20%, the gross is the net payment divided by 0.8.
- **On account counts.** Withholding is due on payment or accrual, including "payment on account": any entry that shows the payer owing the income to the recipient (art. 30(10)).
- **Final tax.** For a non-resident with no Turkish workplace, tax withheld on income other than trading and farm profit is final; filing a return for it is optional (art. 30(9)). A non-resident individual does not file for professional, investment, rental or other income fully taxed by withholding (GVK art. 86(2); see [turkey-pit](turkey-pit.md)).
- **Listed countries** (art. 30(7)). Every payment to a company in a country the President lists (judged on tax capacity and information exchange) bears 30%, whether or not the income is taxable and whether or not the recipient is a taxpayer. Not covered: arm's length payments for goods and shareholdings, ship and aircraft charters and similar payments, for which the President may set a lower rate; and principal, interest and profit share on loans from foreign financial institutions, and insurance and reinsurance payments. A payment taxed under this rule is not withheld again under the other rules.
- **Permanent establishment.** A workplace (iş yeri) is any place used for or allotted to a business or professional activity, such as a shop, office, branch, warehouse, factory, mine or construction site (VUK art. 156; GVK art. 8). A permanent representative (daimi temsilci) is a person tied to the principal by a service or agency contract and authorised to carry out its business for a fixed or open period; commercial agents and agents under the Commercial Code are always permanent representatives (GVK art. 8). A non-resident with a workplace or permanent representative is taxed on the trading profit made through it. Buying goods in Türkiye to export without selling them in Türkiye is not Turkish income (KVK art. 3(3)(a)).
- **Controlled foreign company** (KVK art. 7). A foreign subsidiary that Turkish residents control directly or indirectly, alone or together, with at least 50% of its capital, profit rights or votes is taxed in Türkiye on its profit, distributed or not, when all three tests are met: (a) 25% or more of its gross revenue is passive income (interest, dividends, rent, licence fees, gains on securities and similar) not from a real business with matching capital, organisation and staff; (b) its total income tax burden on commercial profit is below 10%; (c) its gross revenue for the year exceeds the equivalent of TRY 100,000. The highest control share held at any time in the period counts. The profit is added to the corporate tax base of the fully liable Turkish company shareholders pro rata, in the period that includes the subsidiary's year-end. A later distribution of profit already taxed is taxed only on the part not taxed before (art. 7(5)).
- **Foreign tax credit** (KVK art. 33). Foreign corporate tax on foreign profits included in Turkish results is credited against the Turkish tax on them, capped at Turkish tax at the KVK art. 32 rate on that foreign profit. An unused credit can be carried to the end of the third following period. A company holding at least 25% of a foreign subsidiary can also credit the underlying foreign tax on the dividend, grossing the dividend up for it. For a CFC, the foreign tax paid by the subsidiary is credited against the Turkish tax on the CFC income. Foreign tax must be shown by documents from the foreign authority certified by the Turkish embassy or consulate (art. 33(6)); if they are missing at assessment, the tax is deferred for up to a year while they are produced (art. 33(7)).
- **Foreign dividends.** The participation exemption for dividends from foreign subsidiaries (10% for one year, 15% tax burden) is in [tr-corporate-income-tax](tr-corporate-income-tax.md).

## Deadlines and filing

- **Withholding return.** The tax withheld under KVK art. 30 and GVK art. 94 is declared on the withholding return (muhtasar ve prim hizmet beyannamesi) to the payer's tax office (KVK art. 31). GİB's calendar sets the monthly return by 23:59 on the 26th of the following month, paid in the same period (GVK art. 98 still says the 23rd). A payer on quarterly withholding returns files by the 26th of the month after the quarter.
- **VAT on imported services.** The Turkish customer declares the reverse-charge VAT on return no. 2 (2 No.lu KDV Beyannamesi) for the month of the transaction. GİB's calendar sets filing and payment by the 25th of the following month (VUK Circular 164). The customer need not be a VAT taxpayer: anyone who uses the service in Türkiye files return no. 2 (KDVGUT I/C-2.1.2.1.1). A VAT taxpayer deducts it on return no. 1 for the period it is paid, or for the same month if return no. 2 was filed and paid on time before return no. 1 (KDV art. 29(1); KDVGUT III/C-1.1).
- **Electronic services to consumers.** A foreign supplier of electronic services to Turkish individuals who are not VAT taxpayers declares and pays the VAT itself (KDV art. 9(1)); see [turkey-vat](turkey-vat.md).
- **Non-resident company with Turkish income but no annual return.** If its only Turkish income is other income (not royalties or the sale of intangibles), it files a special return within 15 days of earning it (GİB calendar).
- **Branch or PE.** The annual corporate tax return is due by the end of the fourth month after the period, so 30 April 2027 for a 2026 calendar year (GİB calendar). Quarterly provisional tax applies to its trading profit (KVK art. 32(2)).
- **CFC and transfer pricing form.** CFC income goes into the annual corporate tax return of the Turkish shareholder. The transfer pricing, controlled foreign company and thin capitalisation form is filed with that return (TP Communiqué Serial No. 4, section 7.5; see [tr-transfer-pricing](tr-transfer-pricing.md)).

## Penalties and interest

- **Tax not withheld.** The payer is the responsible party (vergi sorumlusu). Tax not withheld or under-withheld is assessed on the payer with a tax loss penalty of one times the tax lost (VUK art. 344), three times for fraud under VUK art. 359. A return filed late, before an audit or a referral to the assessment committee, halves the penalty (art. 344).
- **Late interest.** Tax assessed later carries late interest from the normal due date at the late-payment surcharge rate, 3.7% a month for 2026, part months not counted (VUK art. 112(3)).
- **Late payment.** Tax not paid by its due date carries a late-payment surcharge of 3.7% for each month, computed daily for part months (Law 6183 art. 51; Decision 10556, Official Gazette 13 November 2025).
- **Late or missing return.** A late withholding or VAT return is an irregularity under VUK art. 352; the 2026 amounts are in [turkey-vat](turkey-vat.md).
- **Treaty relief claimed without a certificate.** If the residence certificate is not produced, domestic rates apply instead of treaty rates (GİB ruling, Kayseri Tax Office, 2 November 2023), so the payer is assessed on the difference.

## Cross-border points

- **Treaties.** A tax treaty overrides the domestic rate where it gives Türkiye less taxing right. For example, under a treaty's business profits or independent services article, a foreign company's fee for a service bought from abroad is taxable only in its home country unless it has a PE or fixed base in Türkiye (GİB ruling, 2 November 2023, on the Türkiye-Iran treaty, arts. 7 and 14). Treaty rates for dividends, interest and royalties are not covered here.
- **Residence certificate.** To apply a treaty where it changes the domestic result, the foreign recipient must prove with a certificate from its home tax authority (mukimlik belgesi) that it is fully liable and taxed on worldwide income there. The original and a Turkish translation certified by a notary or a Turkish consulate are given to the payer or the tax office. Without it, domestic law applies (GİB ruling, 2 November 2023).
- **Services bought from abroad.** A fee for a service used in Türkiye is Turkish professional income if it is evaluated in Türkiye (GVK art. 7(4)). The GİB ruling of 2 November 2023 treated a foreign firm's supply-sourcing service to a Turkish importer as professional income subject to 20% withholding under KVK art. 30(1)(b), subject to the treaty, and as a service used in Türkiye subject to VAT on return no. 2.
- **Intra-group service and cost-sharing charges.** These are taxed by their real nature; a charge for the use of an intangible is a royalty (TP Communiqué Serial No. 4, section 11.3).
- **Deemed dividends.** Transfer pricing adjustments and thin capital interest are treated as dividends to the foreign party and bear dividend withholding; see [tr-transfer-pricing](tr-transfer-pricing.md).

## Worked examples

### Example 1: Consulting fee to a foreign company, no residence certificate

A Turkish company buys consulting from a foreign company with no presence in Türkiye. The fee is TRY 500,000 gross and the service is used in Türkiye. The foreign company gives no residence certificate, so the domestic rate applies. The Turkish company withholds 20%, TRY 100,000, pays the consultant TRY 400,000, and declares the TRY 100,000 on the withholding return by the 26th of the next month. It also computes VAT of 20% on the TRY 500,000 fee, TRY 100,000, and declares and pays it on return no. 2 by the 25th of the next month. As a VAT taxpayer it deducts the TRY 100,000 on return no. 1. Cash to GİB is TRY 200,000; after the VAT deduction the company's net tax cost is the TRY 100,000 withheld, which is the consultant's tax.

```oa-check
name: TR consulting fee to a non-resident company with reverse-charge VAT (2026)
inputs:
  gross_fee: 500000
  wht_rate_pct: 20
  vat_rate_pct: 20
steps:
  - withholding: gross_fee * wht_rate_pct / 100
  - paid_to_supplier: gross_fee - withholding
  - reverse_charge_vat: gross_fee * vat_rate_pct / 100
  - vat_deducted: reverse_charge_vat
  - cash_to_gib: withholding + reverse_charge_vat
  - net_vat_cost: reverse_charge_vat - vat_deducted
expected:
  withholding: 100000
  paid_to_supplier: 400000
  reverse_charge_vat: 100000
  cash_to_gib: 200000
  net_vat_cost: 0
```

### Example 2: Royalty with the tax borne by the payer, plus a dividend

A Turkish company agrees to pay a foreign licensor TRY 340,000 net for a software licence and to bear the Turkish tax. No residence certificate is given. Because the payer bears the tax, the base is the net payment plus the tax: TRY 340,000 / 0.8 = TRY 425,000 gross, so the withholding is TRY 85,000. In the same month it pays a TRY 1,000,000 dividend to its foreign parent company, which bears 15% withholding, TRY 150,000. The withholding return for the month shows TRY 235,000.

```oa-check
name: TR royalty gross-up and dividend withholding (2026)
inputs:
  net_royalty: 340000
  royalty_rate_pct: 20
  dividend: 1000000
  dividend_rate_pct: 15
steps:
  - gross_royalty: net_royalty / (1 - royalty_rate_pct / 100)
  - royalty_wht: gross_royalty * royalty_rate_pct / 100
  - dividend_wht: dividend * dividend_rate_pct / 100
  - total_wht: royalty_wht + dividend_wht
expected:
  gross_royalty: 425000
  royalty_wht: 85000
  dividend_wht: 150000
  total_wht: 235000
```

## Ask the client first

1. What exactly is being paid for (service, licence, rent, interest, dividend, goods), and is the service done in Türkiye or used in Türkiye?
2. Where is the recipient resident, and can it give a residence certificate from its home tax authority, with a certified Turkish translation?
3. Does the recipient have an office, site, staff or agent in Türkiye that could be a workplace or permanent representative?
4. Is the price gross, or has the Turkish payer agreed to bear the Turkish tax?
5. Is the payer a VAT taxpayer, and on monthly or quarterly withholding returns?
6. For Turkish companies with foreign subsidiaries: what share does it hold, and what are each subsidiary's gross revenue, passive income share and tax burden?

## Sources

| Source | URL | Read on |
|---|---|---|
| Kurumlar Vergisi Kanunu no. 5520, consolidated: arts. 3, 7, 12, 13, 14, 30, 31, 32, 33 | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5520.pdf | 2026-10-31 |
| Gelir Vergisi Kanunu no. 193, consolidated: arts. 4, 5, 7, 8, 86, 94, 98 | https://www.mevzuat.gov.tr/MevzuatMetin/1.4.193.pdf | 2026-10-31 |
| Vergi Usul Kanunu no. 213, consolidated: arts. 112, 156, 344 | https://www.mevzuat.gov.tr/MevzuatMetin/1.4.213.pdf | 2026-10-31 |
| Katma Değer Vergisi Kanunu no. 3065, consolidated: arts. 6, 9, 20, 29 | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.3065.pdf | 2026-10-31 |
| KDV Genel Uygulama Tebliği, consolidated: I/C-2.1.2.1.1, III/C-1.1 | https://www.mevzuat.gov.tr/File/GeneratePdf?mevzuatNo=19631&mevzuatTur=Teblig&mevzuatTertip=5 | 2026-10-31 |
| Amme Alacaklarının Tahsil Usulü Hakkında Kanun no. 6183, consolidated: art. 51 and note on Decision 10556 | https://www.mevzuat.gov.tr/MevzuatMetin/1.3.6183.pdf | 2026-10-31 |
| Decision 2009/14593 (KVK art. 30 rates), Official Gazette 3 February 2009 no. 27130 | https://www.resmigazete.gov.tr/eskiler/2009/02/20090203-4.htm | 2026-10-31 |
| Decision 2009/14592 (GVK art. 94 rates), Official Gazette 3 February 2009 no. 27130 | https://www.resmigazete.gov.tr/eskiler/2009/02/20090203-3.htm | 2026-10-31 |
| Decision 9286 (dividends to 15%), Official Gazette 22 December 2024 no. 32760 | https://www.resmigazete.gov.tr/eskiler/2024/12/20241222-15.pdf | 2026-10-31 |
| Decision 9707 (construction rates), Official Gazette 30 March 2025 no. 32857 | https://www.resmigazete.gov.tr/eskiler/2025/03/20250330-4.pdf | 2026-10-31 |
| GİB, KVK art. 30 withholding rates for non-resident companies (table) | https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Fyardim-kaynaklar%2Fyararli-bilgiler%2Fkvk-nun-30-ve-gecici14-ile-gvk-nun-gecici-67inci-maddeleri-uyarinca-dar-mukellef.pdf | 2026-10-31 |
| GİB, GVK art. 94 withholding rates (table) | https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Fyardim-kaynaklar%2Fyararli-bilgiler%2Fgelir-vergisi-kanununun-94uncu-maddesinde-yer-alan-kesinti-oranlari.pdf | 2026-10-31 |
| GİB, Kurumlar Vergisinde Oran Uygulamaları (publication no. 605, March 2026) | https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Fonceki-dokumanlar%2F2026_KurumlarVergisiOran.pdf | 2026-10-31 |
| GİB ruling, Kayseri Tax Office, 2 November 2023, service bought from an Iranian firm (KVK, treaty, KDV) | https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Fmevzuat%2Fuluslararasi_mevzuat%2F02112023_498.pdf | 2026-10-31 |
| GİB, Beyanname verme ve ödeme süreleri (filing calendar) | https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Fyardim-kaynaklar%2Fyararli-bilgiler%2FBeyannameVermeveOdemeSureleri.pdf | 2026-10-31 |
| Transfer pricing General Communiqué Serial No. 4, Official Gazette 1 September 2020 no. 31231 | https://www.resmigazete.gov.tr/eskiler/2020/09/20200901-3.htm | 2026-10-31 |

Not yet confirmed: treaty-by-treaty rates and the list of treaties in force; whether the President has announced any country list under KVK art. 30(7) (no list found); the text of Decision 11344 (18 May 2026, nuclear plant construction), taken from GİB's tables only; the full amendment history of Decisions 2009/14593 and 2009/14592 between 2009 and 2021 (the rates above are as GİB's current tables state them); whether the Turkish payer's borne withholding is part of the VAT base on an imported service; how the CFC profit is measured (before or after the subsidiary's own tax) and how the CFC tax credit is shared pro rata, set out in the KVK General Communiqué, which was not read; the VUK art. 352 penalty amounts for a late withholding return (see turkey-vat); exit taxation on a transfer of seat or assets abroad; withholding on deposit interest and investment fund income under GVK provisional art. 67.
